# 第5B章：DD-PPO 分布式训练 — Habitat 从零理解

> Step5 的 PPO 训练是单机单卡版本。本章教你如何使用 DD-PPO（Decentralized Distributed PPO）
    在单机多卡或多机上并行采样，将训练吞吐量线性扩展到数十甚至数百个 GPU。

##  案例总览

| # | 案例 | 难度 | 学什么 |
| --- | --- | --- | --- |
| 1 | DD-PPO 原理：PPO vs DD-PPO 架构对比 | ⭐ | 数据并行、all-reduce 梯度同步、straggler preemption |
| 2 | 配置对比：PPO → DD-PPO 的逐项差异 | ⭐⭐ | trainer_name, sync_frac, backbone, pretrained_encoder |
| 3 | 单机多卡运行 | ⭐⭐ | torch.distributed.launch, 环境变量, 吞吐量对比 |
| 4 | 常见故障排查 | ⭐⭐ | NCCL 超时、OOM、端口冲突、评估异常 |

##  案例 1：DD-PPO 原理 — PPO vs DD-PPO 架构对比

**① 案例含义**

DD-PPO **不是新算法**，而是 PPO 的一种**分布式系统架构**。
它和单机 PPO 使用同一个 `PPOTrainer` 类（在 `ppo_trainer.py` 中同时注册为 `"ppo"` 和 `"ddppo"`），
区别在于分布式模式下多了三样东西：**去中心化梯度同步**、**全局优势归一化**、**掉队者预emption**。

```
# 单机 PPO 架构
┌──────────────────────────────────────┐
│  GPU 0                               │
│  ┌────────────────────────────────┐  │
│  │ 6 envs × 128 steps = 768 样本  │  │
│  │       ↓                        │  │
│  │ 局部优势归一化                    │  │
│  │       ↓                        │  │
│  │ PPO update (4 epochs)           │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
  有效 batch：768 步

# DD-PPO 架构（4 GPU 示例）
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│  GPU 0   │ │  GPU 1   │ │  GPU 2   │ │  GPU 3   │
│  4 envs  │ │  4 envs  │ │  4 envs  │ │  4 envs  │
│    ↓     │ │    ↓     │ │    ↓     │ │    ↓     │
│  512 样本│ │  512 样本│ │  512 样本│ │  512 样本│
└────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
     └───────────┐ │ ┌─────────┘ ┌──────────┘
            distributed_var_mean()   ← 全局统计
                 │ │ │ │
            all-reduce gradients     ← DDP 同步
                 │ │ │ │
            optimizer.step()         ← 统一更新
  有效 batch：4 × 4 × 128 = 2048 步
```

### DD-PPO 的三个核心机制

| 机制 | 单机 PPO | DD-PPO |
| --- | --- | --- |
| **梯度同步** | 本地 `loss.backward()`，无同步 | PyTorch DDP 的 `all_reduce` 在各 GPU 间平均梯度
代码位置：`rl/ddppo/algo/ddppo.py` → `DecentralizedDistributedMixin` |
| **优势归一化** | `torch.var_mean(x)` — 仅在本地样本上计算 | `distributed_var_mean(x)` — 跨所有 worker 计算真实均值/方差
这对 PPO 的 clipped objective 至关重要——全局统计更稳定 |
| **掉队者预emption** | 不适用（只有一个 worker） | 当 `sync_frac` (默认 60%) 的 worker 已收集完 rollout，剩余慢 worker 被提前终止
这样整体不需要等待最慢的 GPU |

**② 关键函数调用**

| 函数/类 | 文件 | 作用 |
| --- | --- | --- |
| `PPOTrainer.__init__` | `ppo_trainer.py:98` | `self._is_distributed = world_size > 1` 判断是否启用分布式 |
| `init_distrib_slurm()` | `ddp_utils.py:271` | 初始化 torch.distributed，解析 SLURM/launch 环境变量 |
| `DecentralizedDistributedMixin.init_distributed()` | `algo/ddppo.py` | 将 Actor-Critic 包装在 DDP 中（包装 `_EvalActionsWrapper` 而非直接的 forward） |
| `should_end_early()` | `ppo_trainer.py:634` | 掉队者 preemption 判断逻辑 |
| `distributed_var_mean()` | `algo/ddppo.py` | 跨 GPU 的 all-reduce 方差/均值计算 |

> 💡 **种子偏移机制**

每个 worker 的种子会被偏移 `rank × num_environments`，确保：

Worker 0: 种子 = base_seed + 0

Worker 1: 种子 = base_seed + num_environments

Worker 2: 种子 = base_seed + 2×num_environments

这保证了所有 worker 的所有环境都有独一无二的种子，避免重复数据。

##  案例 2：配置对比 — PPO → DD-PPO 的逐项差异

**① 案例含义**

从 PPO 切换到 DD-PPO，核心就是改配置。理解每一项的含义，才能根据自己的硬件环境合理调参。

### PPO 配置 vs DD-PPO 配置 — 并排对比

| 配置项 | PPO (ppo_pointnav_example.yaml) | DD-PPO (ddppo_pointnav.yaml) | 说明 |
| --- | --- | --- | --- |
| `trainer_name` | `"ppo"` | **`"ddppo"`** | 触发 DDP 包装和全局统计 |
| `num_environments` | 6 (per GPU) | **4** (per GPU) | 分布式下有额外通信开销，降低单 GPU 负载 |
| `ppo_epoch` | 4 | **2** | 样本量增大后减少 epoch 防过拟合 |
| `hidden_size` | 小（如 256） | **512** | 更大的模型容量 |
| `backbone` | resnet18 | **resnet50** | 更强的视觉编码器 |
| `rnn_type` | GRU | **LSTM** | LSTM 对长序列更稳定 |
| `num_recurrent_layers` | 1 | **2** | 更深的状态编码 |
| `sync_frac` | N/A | **0.6** | 60% worker 完成就 preempt 慢者 |

DD-PPO 专属配置段

```
# DD-PPO 专属配置（ddppo_pointnav.yaml 中的 ddppo 段）
habitat_baselines:
  trainer_name: ddppo
  rl:
    ddppo:
      sync_frac: 0.6            # preemption 阈值
      distrib_backend: NCCL       # GPU 用 NCCL（更快），CPU 用 GLOO
      backbone: resnet50         # 视觉编码器架构
      rnn_type: LSTM            # GRU 或 LSTM
      num_recurrent_layers: 2  # RNN 层数
      pretrained: False         # 是否加载完整预训练权重
      pretrained_encoder: False  # 是否只加载 encoder 预训练权重
      pretrained_weights: "data/ddppo-models/gibson-2plus-resnet50.pth"
      train_encoder: True       # 是否训练 encoder（False = 冻结）
      reset_critic: True        # 加载预训练时是否重置 Critic 头
      force_distributed: False  # True = 单 GPU 也启用分布式（调试用）
```

| 关键参数 | 含义 | 建议 |
| --- | --- | --- |
| `sync_frac` | 多少比例的 worker 完成后触发 preemption | 0.6 是默认值。如果 worker 速度差异大，可降低到 0.4 |
| `pretrained_encoder` | 加载预训练视觉 backbone（不加载 RL 策略部分） | 推荐设为 True，用官方 `gibson-2plus-resnet50.pth` |
| `reset_critic` | 预训练后重置 value head | 设为 True，避免 value 估计与新环境不匹配导致训练崩溃 |
| `train_encoder` | 是否微调视觉 backbone | True = 全训练；False = 冻结 encoder（类似微调 CLIP） |

##  案例 3：单机多卡运行

**① 案例含义**

在不使用 SLURM 的普通机器上，使用 PyTorch 的 `torch.distributed.launch`
启动多 GPU DD-PPO 训练。这是科研场景中最常见的用法。

② 核心代码 — 启动命令

```
# 单机 2 卡 DD-PPO 训练（来自 single_node.sh 模式）
export GLOG_minloglevel=2          # 减少 C++ 日志噪音
export MAGNUM_LOG=quiet            # 减少 Magnum 引擎日志

python -u -m torch.distributed.launch \
    --use_env \
    --nproc_per_node 2 \
    habitat_baselines/run.py \
    --config-name=pointnav/ddppo_pointnav.yaml \
    habitat_baselines.num_environments=4 \
    habitat_baselines.total_num_steps=1000000 \
    habitat_baselines.checkpoint_folder=data/ddppo_checkpoints
```

**环境变量解析**

| 变量 | 由谁设置 | 含义 |
| --- | --- | --- |
| `LOCAL_RANK` | `torch.distributed.launch` | 当前进程在节点内的 GPU ID（0, 1, ...） |
| `RANK` | `torch.distributed.launch` | 全局进程 ID |
| `WORLD_SIZE` | `torch.distributed.launch` | 总进程数（= GPU 总数） |
| `MAIN_ADDR` | 用户手动设置 | 主节点 IP（单机默认 127.0.0.1） |
| `MAIN_PORT` | 用户手动设置 | 通信端口（默认 8738） |

④ 预期训练日志

```
# 启动后每个 GPU 会产生类似输出：
2026-06-05 12:00:01 [rank0] Initializing distributed backend (NCCL)
2026-06-05 12:00:02 [rank0] Distributed init complete: world_size=2
2026-06-05 12:00:05 [rank0] ResNet50 encoder loaded
2026-06-05 12:00:06 [rank0] Creating 4 environments per GPU

# 训练循环：
update: 0   loss: 0.523   reward: -1.234   steps/sec: 2847   ← 2 GPU 的吞吐量
update: 1   loss: 0.487   reward: -0.983   steps/sec: 2850

# 对比单 GPU PPO（相同硬件）：
# update: 0   loss: 0.523   reward: -1.234   steps/sec: 1523  ← 单 GPU
```

**⑤ 输出含义**

**steps/sec** 是核心吞吐量指标。DD-PPO 的吞吐量随 GPU 数量**近似线性增长**——4 GPU 约 = 单 GPU × 3.6~3.8 倍（非完美的 4 倍是因为通信开销）。

每个 GPU 的 **loss** 应大致相同（因为梯度同步保证了模型参数一致），但 reward 可能不同（不同 GPU 探索不同场景）。

### 吞吐量缩放参考

| GPU 数量 | 有效 batch size | steps/sec (典型) | 达到 100M 步所需时间 |
| --- | --- | --- | --- |
| 1 (PPO) | 768 | ~1,500 | ~18.5 小时 |
| 2 (DD-PPO) | 1,024 | ~2,800 | ~9.9 小时 |
| 4 (DD-PPO) | 2,048 | ~5,500 | ~5.1 小时 |
| 8 (DD-PPO) | 4,096 | ~10,500 | ~2.6 小时 |

注意：以上数值为 AI Habitat 论文中的典型数据，实际吞吐量取决于场景复杂度、传感器分辨率、GPU 型号。

##  案例 4：常见故障排查

**① 案例含义**

DD-PPO 的分布式特性带来了新的故障模式。以下是从社区和论文中整理的常见问题及解决方法。

#### NCCL 超时 / 训练卡住

**症状：**训练启动后卡在 "Initializing distributed" 不动

修复：

① 确认 `MAIN_ADDR=127.0.0.1`（单机）

② 检查防火墙是否拦截了端口 `8738`

③ 改用 GLOO backend：`distrib_backend: GLOO`

④ 确认所有 GPU 都可被 PyTorch 访问：`torch.cuda.device_count()`

#### CUDA Out of Memory (OOM)

**症状：**创建环境或第一个 forward 时 OOM

修复：

① 减小 `num_environments`（从 4 → 2）

② 减小 RGB 分辨率

③ 换用小 backbone（resnet50 → resnet18）

④ 确保 `force_torch_single_threaded: True`

#### 评估报错：does not support distributed mode

**症状：**`RuntimeError("Evaluation does not support distributed mode")`

修复：DD-PPO 不支持分布式评估。运行评估时：

① 使用 `trainer_name: "ppo"` 而非 `"ddppo"`

② 或在单 GPU 模式下运行

③ 在分析脚本中用单进程加载 checkpoint 评估

#### 端口冲突（多任务）

**症状：**`Address already in use`

修复：

① `ddp_utils.py` 会自动在端口上加上 `SLURM_JOBID % 127` 作为偏移

② 手动指定：`export MAIN_PORT=9843`

③ 使用 `find_free_port()` 函数（在 `ddp_utils.py` 中）

#### 梯度不同步 / loss 波动剧烈

**症状：**不同 GPU 的 loss 差异巨大，训练不收敛

修复：

① 确认 `use_normalized_advantage: False`（DD-PPO 用自己的分布式归一化）

② 确认 `force_distributed: True`（单机测试分布式模式时）

③ 运行测试：`pytest test/test_ddppo_reduce.py`

#### SLURM preemption 后无法恢复

**症状：**被 preempt 后训练从头开始

修复：

① 环境变量 `SLURM_JOBID` 不存在导致 resume 文件找不到

② 检查 `data/new_checkpoints/.habitat-resume-state-{JOBID}.pth`

③ SLURM 脚本需加 `#SBATCH --requeue` 和 `#SBATCH --signal=USR1@90`

关键警告

**不要在 DD-PPO 中混合使用 PPO 的 config**——特别是 `use_normalized_advantage: True`。
DD-PPO 使用 `distributed_var_mean()` 做归一化，如果再叠加 PPO 的局部归一化会导致双重归一化，训练会崩溃。
DD-PPO 配置文件（`ddppo_*.yaml`）已经正确设置了这些，如果你手动合并 PPO 和 DD-PPO 的配置，务必检查这一点。

##  学后自检 — 你掌握了什么

#### Q1：DD-PPO 是新算法吗？

不是。DD-PPO 和单机 PPO 使用同一个 `PPOTrainer` 类（注册为 "ppo" 和 "ddppo" 两个名字）。它是 PPO 的一种分布式系统架构，通过 all-reduce 梯度同步和全局统计归一化来支持多 GPU 训练。

#### Q2：sync_frac=0.6 的含义？

当 60% 的 worker 已完成当前 rollout 的全部步数，其余 worker 会被提前终止（preempt）。这避免了整体等待最慢的 worker，代价是慢 worker 贡献了较短的轨迹。

#### Q3：为什么 DD-PPO 要降低 num_environments？

每个 GPU 上还有 DDP 的通信开销（梯度 all-reduce），加上 ResNet-50 比 ResNet-18 更吃显存。降低 env 数量给通信和更大模型腾出 GPU 显存和算力。

#### Q4：如何验证梯度同步是否正常工作？

运行 `pytest test/test_ddppo_reduce.py`。这个测试验证了 RL 的非标准 DDP 用法（在 forward-while-collecting 模式下的梯度 reduce）在不同 PyTorch 版本上是否正常。

#### Q5：pretrained_encoder vs pretrained 的区别？

`pretrained_encoder: True` 只加载视觉 backbone（CNN）的权重，RL 部分（Actor/Critic head + RNN）随机初始化。`pretrained: True` 加载所有参数。后者要求 checkpoint 与新配置架构完全一致。

[← 第5章：训练与评测](habitat-textbook-step5.html)
[第9章：Rearrange 操作任务 →](habitat-textbook-step9.html)
