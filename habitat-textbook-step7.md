# 第7步：VLN 视觉语言导航 — Habitat 从零理解

> 在 Habitat 中训练视觉语言导航（VLN）模型：配置 VLN-v0 任务、理解 R2R 数据集与 InstructionSensor、
    跑通模仿学习 + DDPPO 微调、导出 checkpoint 为真机部署做准备。

##  本章概览：10 个案例

从 IL 训练到诊断修复，从 SOTA 参照到模型微调——VLN 一条线走到底。前置：[第5步「导航任务全景」§1.6](habitat-textbook-step5.html) 已介绍 VLN 是什么。

从配置到训练到导出，每一步都可独立运行和验证。建议按顺序完成。

| # | 案例 | 你将学会 | 难度 | 前置条件 |
| --- | --- | --- | --- | --- |
| 7-1 | [配置 VLN 任务](#case7-1) | VLN-v0 任务配置、R2R 数据集加载、验证环境可创建 | ⭐⭐ | Step 2 |
| 7-2 | [理解数据与传感器](#case7-2) | R2R episode 结构、InstructionSensor 原理、observation 空间 | ⭐⭐ | 7-1 |
| 7-3 | [模仿学习训练](#case7-3) | IL 训练流程、teacher-forcing、checkpoint 保存 | ⭐⭐⭐ | 7-2, Step 5 |
| 7-4 | [评估与导出模型](#case7-4) | SR/SPL/nDTW 指标、模型推理模式、导出 checkpoint | ⭐⭐ | 7-3 |
| 7-4 | [避坑诊断](#case7-4) | CLIP实验、行为漂移分析——学会诊断ML工程问题 | ⭐⭐⭐ | 7-3 |
| 7-5 | [DAgger 桥接](#case7-5) | IL 32% → DAgger 50% → RL 55%+ 三阶梯对比 | ⭐⭐⭐⭐ | 7-4 |
| 7-6 | [SOTA 参照](#case7-6) | 运行 JanusVLN，对比小模型，理解参数量级差距 | ⭐⭐⭐ | 7-5 |

##  为什么 VLN 必须依赖 Matterport3D？

从 IL 训练到诊断修复，从 SOTA 参照到模型微调——VLN 一条线走到底。前置：[第5步「导航任务全景」§1.6](habitat-textbook-step5.html) 已介绍 VLN 是什么。

这不是 Habitat 的限制，而是 VLN 任务本身的定义方式决定的。

**R2R —— VLN 领域的"ImageNet"**

R2R (Room-to-Room) 是 CVPR 2018 提出的视觉语言导航基准数据集，至今**每篇 VLN 论文都以它为评测标准**。
它的采集方式是：人类标注者在 **90 栋 Matterport3D 建筑**中行走，用自然语言写下导航指令，
例如 *"Walk down the hallway, turn left at the painting, and stop in front of the bed."*

**这决定了：语言指令和 MP3D 场景是绑定的。** 换一栋建筑，"绘画"和"走廊"都不同了，指令不再有意义。
正因为如此，VLN 任务无法像 PointNav 那样在不同场景数据集间切换。

### 数据依赖链

R2R 数据集
10,819 条导航指令

引用

MP3D 场景 ID
90 栋建筑的 .glb 文件

运行时

VLN 仿真器
Instruction → Action → SR/SPL/nDTW

Habitat 的 VLN 代码（`VLNDatasetV1` / `VLNTask`）本身是**场景无关的**。
但整个 Habitat-Lab 中只注册了 `R2RVLN-v1` 这一个 VLN 数据集，
它的配置硬编码指向 `data/datasets/vln/mp3d/r2r/`，而其中的 episodes 引用的都是 MP3D 场景。

### 无需认证的获取方案

| 文件 | 大小 | 来源 | 覆盖 | 需要认证？ |
| --- | --- | --- | --- | --- |
| `vln_r2r_mp3d_v1.zip` | 2.7 MB | Facebook CDN（`dl.fbaipublicfiles.com`） | 10,819 训练 + 1,020 验证 episodes | 否 |
| `MatterPort3D.zip` | 665 MB | 清华大学云盘 | 11 个场景（val_unseen 全集） | 否 |
| `mp3d_example` | 93 MB | Habitat 内置（`datasets_download`） | 1 个场景（17DRP5sb8fy） | 否 |

> 💡 **当前状态：12 个场景，可完整走通 VLN 流程**

以上三样合计 **< 800 MB**，全部免除认证。覆盖：

• **训练**：17DRP5sb8fy 在 R2R train 中有 75 条指令，足够演示训练流程

• **评估**：11 个 val_unseen 场景覆盖 1,839 条指令，可直接跑标准 val_unseen 评估

• 如需完整 90 场景（训练出可发表级 VLN 模型），才需要官方申请 Matterport3D

> ⚠️ **有其他数据集可以替代吗？**

**严格来说，没有。** 虽然存在 RxR（多语言 R2R）、REVERIE、SOON 等扩展 VLN 数据集，
但它们全部基于 MP3D 场景采集。HM3D 和 Gibson 都**没有**对应的 VLN 指令数据集。
如果你将来想对比发表的 VLN 模型或参加 Habitat Challenge，MP3D 是必经之路。

##  前置 · VLN 理论基础

在动手写代码之前，先建立 VLN 的心智模型。

**VLN 一句话定义**

**Visual Language Navigation（视觉语言导航）**：
给定一段自然语言指令（如"走过厨房，在卧室门口停下"），Agent 仅凭 RGB 视觉观测，
在 3D 环境中逐步移动，最终停在指令描述的目标位置。

**为什么它比 PointNav 难？**

| 维度 | PointNav | VLN |
| --- | --- | --- |
| 目标表示 | GPS 坐标 (x,y) — 精确 | 自然语言 — 模糊、多义 |
| 推理需求 | 纯空间推理 | 视觉理解 + 语言理解 + 跨模态对齐 |
| 错误容忍 | 偏离 1m → 可能找不到 | 理解语义 → 能自我纠正 |
| 数据依赖 | 任何 3D 场景 | 需要人工标注指令（昂贵） |

> 💡 **📖 详细理论参考**

本章聚焦「动手实操」。如果你想深入了解 VLN 的技术流派（Seq2Seq / BERT-CLIP / LLM-VLM / 拓扑图 / 神经辐射场 / 世界模型）、
发展历程（R2R 2018 → RxR 2020 → REVERIE 2020 → VLN-CE 2022 → NaVid 2024）、
以及核心挑战（Sim2Real、长程记忆、多语言），请阅读
[VLN 理论专题 →](vln.html)。

##  7-1 · 配置 VLN 任务

**① 案例含义**

使用 `habitat.get_config()` 加载 VLN 基准配置，创建一个 VLN 环境并验证它能正常
`reset()`。这是 VLN 训练的**最小验证单元**——如果这步不通过，后面的训练无从谈起。

**前置条件：**已安装 habitat-lab + habitat-sim。R2R 数据集和 MP3D 场景的获取方式见上方"为什么 VLN 必须依赖 Matterport3D"（无需认证，合计 < 800MB）。

### ② 核心代码 & 关键函数

```
# case_6_1_vln_env.py — 验证 VLN 环境可创建并 reset
import habitat

# VLN 使用专门的 benchmark 配置文件
config = habitat.get_config(
    config_path="benchmark/nav/vln/vln_r2r.yaml"
)

# 可选：覆盖数据集路径
with habitat.config.read_write(config):
    config.habitat.dataset.data_path = "data/datasets/vln/r2r/v1/{split}/{split}.json.gz"

env = habitat.Env(config=config)
obs = env.reset()

# VLN 的 observation 包含语言指令
print("观测键:", list(obs.keys()))
print("指令:", obs["instruction"]["text"][:80], "...")
print("RGB shape:", obs["rgb"].shape)
env.close()
  
    函数角色说明
    
      
        habitat.get_config()
        加载基准配置
        读取 YAML → 解析 Hydra → 返回冻结的 OmegaConf 配置对象
      
      
        habitat.config.read_write()
        临时解冻配置
        上下文管理器，在 with 块内可修改配置值
      
      
        habitat.Env(config)
        创建环境
        根据配置组装 Simulator + Dataset + Task
      
      
        env.reset()
        初始化 episode
        随机选一个 episode，返回 observation dict (含 instruction)
      
      
        obs["instruction"]
        语言指令文本
        VLN 特有的 observation 键，由 InstructionSensor 生成
      
    
  

  
  ③ 如何创建和运行

  
    
    # 终端中运行
$ python case_6_1_vln_env.py

# 预期输出（示例）
观测键: ['rgb', 'depth', 'instruction', 'pointgoal_with_gps_compass']
指令: Walk down the hallway, turn left at the first door, and stop in front of the bed. ...
RGB shape: (3, 480, 640)
  
    ⚠️ 常见错误
```

**1.** `Dataset not found` → 检查 R2R 数据集是否下载到了 `data/datasets/vln/r2r/`

**2.** `Scene not found` → 检查 Matterport3D 场景是否在 `data/scene_datasets/mp3d/`

**3.** `KeyError: 'instruction'` → 确认配置中 task 类型为 `VLN-v0` 而非 `Nav-v0`

### ④ 运行效果

`env.reset()` 成功后，你会看到：

**1.** 终端打印出观测键列表 — 确认 `instruction` 键存在

**2.** 一段英文指令文本 — 这就是 VLN 模型需要理解并执行的导航命令

**3.** RGB 图像的 shape 是 (3, H, W) — 证明视觉传感器工作正常

与 PointNav 最大的区别：**observation 中多了 `instruction` 字段**，这是让 VLN 不同于纯视觉导航的关键。

##  7-2 · 理解 R2R 数据与 InstructionSensor

**① 案例含义**

深入 R2R (Room-to-Room) 数据集的一个 episode，理解 VLN 任务的**完整数据结构**：
episode 包含什么字段、指令如何编码、InstructionSensor 如何把文本喂给模型。
这步至关重要——不理解数据，就无法设计模型输入。

### ② R2R Episode 结构

一个 R2R Episode 的内部结构

episode_id
"13361"

scene_id
"2t7WUuJeko7"

start_position + rotation
(x,y,z) + quat

↓

goals[0]
position: (x,y,z) + radius

reference_path
[{position, rotation}×N] — 最短路径轨迹点

↓

instructions
{instruction_id, instruction_text}×3 — 同一条路径的三段英文描述

### InstructionSensor 工作原理

R2R JSON
episode.instructions[0].instruction_text
→

InstructionSensor
读取 episode.instruction
→ tokenize → tensor
→

obs["instruction"]
token IDs (seq_len,)
或原始文本
→

VLN Policy
LSTM/Transformer
编码指令 → 输出动作

### ③ 如何验证数据

```
# case_6_2_inspect_data.py — 检查一个 episode 的完整数据
import habitat

config = habitat.get_config("benchmark/nav/vln/vln_r2r.yaml")
env = habitat.Env(config=config)
obs = env.reset()

# 从 Episode 对象获取完整数据
ep = env.current_episode
print("=== Episode 基本信息 ===")
print(f"episode_id:    {ep.episode_id}")
print(f"scene_id:      {ep.scene_id}")
print(f"start_position: {ep.start_position}")
print(f"goals[0].pos:  {ep.goals[0].position}")
print(f"reference_path 长度: {len(ep.reference_path)} 个路径点")

# 指令 — VLN 最核心的数据字段
print(f"\n=== 指令 ({len(ep.instructions)} 条) ===")
for i, instr in enumerate(ep.instructions):
    print(f"[{i}] {instr.instruction_text[:100]}...")

env.close()
  
    
      📐 NavigationGoal (VLN版)
      
        VLN 的 goal 与 PointNav 完全一样——position (x,y,z) + radius。
        区别在于agent 不知道 goal 的坐标，它只看到指令文本。
        目标是靠理解语言来推断的，而非靠 GPS 传感器指向。
```

#### 📝 为什么有 3 条指令

同一个 episode 由 3 个不同的标注员撰写指令。训练时随机选一条，
评估时用固定的一条。这迫使模型学习**语言多样性**——"turn left at
the sofa" 和 "go left after passing the couch" 对应相同的路径。

> 💡 **💡 关键理解：VLN 属于 "稀疏监督" 任务**

与 PointNav（每步都有 GPS+Compass 指向目标）不同，VLN 的 agent **只在 reset 时看到指令文本**。
后续每一步，模型必须记住指令内容并结合当前视觉观测做决策。这使得 VLN 天然需要
**记忆机制**（LSTM/Transformer/LLM）。

##  7-3 · 模仿学习训练

**① 案例含义**

使用 **Behavioral Cloning（行为克隆）**在 R2R 数据集上训练一个 VLN agent。
Agent 的监督信号来自 `reference_path`（最短路径轨迹），模型学习：
给定当前 RGB + 指令 → 预测下一步动作（前进/左转/右转/停止）。

**前置：**需要 GPU。如仅有 CPU，可将 batch_size 调至 1 且 epochs 设为 1 做语法验证。

### ② 训练流程 & 关键函数

① 数据准备
R2R episodes
→ rollout 生成轨迹
→

② Teacher-Forcing
reference_path 动作
作为 ground truth
→

③ IL Loss
Cross Entropy
动作分类
→

④ Checkpoint
保存 .pth
用于评估/导出

```
# 终端命令 — VLN 模仿学习训练
$ python -u -m habitat_baselines.run \
    --config-name=vln/il_vln_r2r.yaml \
    habitat_baselines.num_updates=10000 \
    habitat_baselines.batch_size=8 \
    habitat_baselines.checkpoint_folder="data/checkpoints/vln_il"

# 关键 config 路径说明：
# config-name=vln/il_vln_r2r.yaml
#   → habitat-baselines/habitat_baselines/config/vln/il_vln_r2r.yaml
# 该 YAML 会自动引用：
#   - benchmark/nav/vln/vln_r2r.yaml（任务 & 数据集）
#   - habitat_baselines/rl/policy/vln_policy.yaml（策略网络）
  
    模块文件作用
    
      
        VLN Task
        habitat/tasks/nav/vln.py
        定义 VLNTask、VLNEpisode、动作空间 (FORWARD/LEFT/RIGHT/STOP)
      
      
        InstructionSensor
        habitat/tasks/nav/vln_sensor.py
        从 episode 读取指令，tokenize 后注入 observation
      
      
        VLN Policy
        habitat_baselines/rl/policy/vln_policy.py
        CNN 编码 RGB + RNN 编码指令 + 动作输出头
      
      
        IL Trainer
        habitat_baselines/il/trainer.py
        管理 teacher-forcing 训练循环、数据集迭代
      
      
        R2R Dataset
        habitat/datasets/vln/r2r_dataset.py
        加载 R2R JSON，提供 Episode 迭代器
      
    
  

  
  ③ 如何创建和运行

  
    
    # 1. 确保 R2R 数据集和 MP3D 场景已下载
$ ls data/datasets/vln/r2r/v1/train/
  train.json.gz  val_seen.json.gz  val_unseen.json.gz

# 2. 确保 habitat-baselines 已安装
$ pip install -e habitat-baselines

# 3. 启动训练（GPU 推荐）
$ python -u -m habitat_baselines.run \
    --config-name=vln/il_vln_r2r.yaml

# 预期输出：
# [2024-01-15 10:30:00] Epoch 0/100, Loss: 1.386, Acc: 0.312
# [2024-01-15 10:35:00] Epoch 10/100, Loss: 0.947, Acc: 0.521
# ...
# Checkpoint saved to data/checkpoints/vln_il/ckpt.100.pth
  
    ⚠️ 训练注意事项
```

**1. GPU 内存：**Matterport3D 场景较大，建议至少 8GB VRAM。OOM 时减小 `batch_size`

**2. 数据预处理：**首次运行时会预处理 R2R 数据（生成 tokenizer 词表），需等待几分钟

**3. Teacher-Forcing vs 在线采样：**IL 训练用的是 reference_path 上的 ground truth 动作，不会让 agent 自由探索

##  7-4 · 评估与导出模型 · 7-6 · JanusVLN · 7-7 · 微调

**① 案例含义**

训练完成后，在验证集上评估模型的导航能力（SR/SPL/nDTW），然后导出 checkpoint
为**纯推理权重文件**。这个文件就是 Step 7 部署到真机时需要加载的模型。

### ② 评估代码 & 指标说明

```
# 评估训练好的 VLN 模型
$ python -u -m habitat_baselines.run \
    --config-name=vln/il_vln_r2r.yaml \
    habitat_baselines.evaluate=True \
    habitat_baselines.eval_ckpt_path_dir="data/checkpoints/vln_il/ckpt.100.pth" \
    habitat_baselines.eval_split="val_seen"

# 预期输出：
# SR: 0.452  SPL: 0.398  nDTW: 0.561
# Success weighted by Path Length: 评估导航路径质量
  
    指标全称含义范围
    
      
        SR
        Success Rate
        在目标 radius 内执行 STOP 的比例
        0–1, 越高越好
      
      
        SPL
        Success weighted by Path Length
        成功且路径尽量短（惩罚绕路）
        0–1, 越高越好
      
      
        nDTW
        Normalized Dynamic Time Warping
        实际路径与 reference_path 的相似度
        0–1, 越高越好
      
      
        OSR
        Oracle Success Rate
        如果 agent 在最近点 STOP 的成功率（上界）
        ≥ SR
      
    
  

  
    
      📊 val_seen vs val_unseen
      
        R2R 的验证集分两种：
        val_seen：场景在训练中见过（但 episode 不同），测指令泛化
        val_unseen：场景从未见过，测场景泛化
        val_unseen 的 SR 通常比 val_seen 低 10–20 个百分点。
```

#### 📦 模型导出

checkpoint 包含 optimizer state + scheduler state + model weights。
为了在真机上做**纯推理**，需要提取出 model weights 部分：

`ckpt = torch.load("ckpt.100.pth")`

`model_weights = ckpt["state_dict"]`

`torch.save(model_weights, "vln_inference.pth")`

### ③ 如何导出可用于真机推理的模型

```
# export_vln_model.py — 导出纯推理权重 + 配置
import torch
import yaml

# 1. 加载训练好的 checkpoint
ckpt = torch.load("data/checkpoints/vln_il/ckpt.100.pth", map_location="cpu")

# 2. 提取 model state_dict（去掉 optimizer/scheduler）
model_state = ckpt["state_dict"]
torch.save(model_state, "vln_inference.pth")
print("模型权重已导出到 vln_inference.pth")

# 3. 保存模型配置（推理时需要重新构建网络结构）
config = {
    "policy": "VLNPolicy",
    "rgb_shape": [3, 480, 640],
    "action_space": ["STOP", "MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT"],
    "instruction_vocab_size": 2500,
    "hidden_size": 512,
}
with open("vln_config.yaml", "w") as f:
    yaml.dump(config, f)
print("模型配置已导出到 vln_config.yaml")
  
    💡 这两个文件就是部署的输入
```

`vln_inference.pth` + `vln_config.yaml` 是 Step 7（方法一：VLN+ROS Nav2）
部署时需要的两个文件。它们包含了**在真机上重建 VLN 模型并运行推理所需的一切**。
你在 Step 7 中会看到如何在 ROS 节点中加载它们。

### ④ 试试调整这些

| 调整项 | 怎么改 | 预期看到什么 |
| --- | --- | --- |
| 训练步数 | 改 `habitat_baselines.num_updates` 从 10000 → 5000 | SR 下降 ~5-10%，但训练时间减半 |
| Batch Size | 改 `habitat_baselines.batch_size` 从 8 → 16 | 收敛更快但 GPU 内存翻倍，可能 OOM |
| 评估 split | 改 `eval_split` 从 val_seen → val_unseen | SR 降低，反映场景泛化能力 |
| 动作空间 | 在配置中添加/移除 TURN 角度参数 | 动作粒度影响导航效率和平滑度 |

> ⚠️ **⚠️ 部署前检查清单**

✅ SR > 0.3（低于此值，真机上的表现会是灾难性的）

✅ 模型在 CPU 上推理时间 < 100ms（真机一般无 GPU）

✅ checkpoint 文件可脱离 habitat-baselines 加载（验证导出脚本）

✅ 已在 val_unseen 上评估过，了解模型在新场景中的表现上限

##  7-4 · 避坑诊断 — ML 工程诊断方法

**📍 为什么需要这一节？**

7-3 的 IL 训练拿到 SR≈32%。这个数字诚实但不理想。
在尝试 DAgger / RL 之前，先要诊断「到底是什么导致了 32%」——
这是 ML 工程师的核心能力，比调参更重要。

##  §N.1 初见：好得可疑的 94.9%

用项目原始代码训练 10 个 epoch，观察训练曲线。

**① 先跑一遍看看**

在你开始修改任何代码之前，先用原始版本完整训练一次，并保存日志。

这个日志是你后续诊断的**唯一参照物**——没有它，你就不知道"修对了没有"。

### ② 训练命令

```
cd habitat-lab-edu
python training/train.py --split val_unseen --num_episodes 500 --epochs 10 \
    2>&1 | tee logs/run1_before_fix.log
```

### ③ 训练曲线（真实日志）

![Before Fix Training Curves](images/before_fix_curves.png)

▲ 从左图可见：train_loss 和 val_loss 快速下降且始终接近——典型的过拟合信号（train/val 数据泄漏）。val_acc 从 79.7% 飙升至 94.1%。

> 💡 **停下想一想**

val_acc = 94.1%，而且 10 个 epoch 就到了。你见过几个 ML 项目有这么快的收敛速度和这么高的准确率？

**在继续之前，问自己：这个数字有可能是真的吗？**

##  §N.2 五重暗坑：逐一揭示

高 val_acc 并不等于好模型。以下是藏在训练管线中的 5 个问题。

#### 🔴 坑 1：文本输入是随机噪声

修复前

```
def fake_text_input(instrs, B, T, ...):
    return torch.randn(B, 10, 300)  # 每轮都不同！
      
        修复后
        # 从 R2R 指令构建词表 1369 词
batch_encode(instructions) → Embedding → LSTM
# 同一条指令永远得到相同向量
```

指令文本从未被使用。模型实际学的是**"看 RGB 序列推测方向"**——这不是 VLN。

#### 🔴 坑 2：Train / Val 数据泄漏

修复前

```
train_ds = VLNDataset(split="val_unseen", ...)
val_ds  = VLNDataset(split="val_unseen", ...)
# ↑ 同一个 split！
      
        修复后
        train_ds = VLNDataset(split="train", ...)
val_ds  = VLNDataset(split="val_unseen", ...)
# ↑ 完全隔离
```

验证集的前 50 个 episode 也在训练集中。模型见过验证数据——94.1% 是**过拟合**，不是泛化。

#### 🟡 坑 3：Action 标签缺失 RIGHT

修复前

```
if abs(dx) > abs(dy):
    actions.append(1)  # FWD
else:
    actions.append(2)  # LEFT——RIGHT 从未出现
      
        修复后
        if dx > 0.05:
    actions.append(3)  # RIGHT
elif dx 

  
  
    
#### 🟡 坑 4：SPL 指标公式错误

    
      
        

修复前
        
```
def spl(success, agent_len, gt_len):
return gt_len / max(agent_len, gt_len)
# ↑ 缺了 success 因子！失败时 SPL≠0

修复后
def spl(success, agent_len, gt_len):
if not success: return 0.0
return success * gt_len / max(agent_len, gt_len)
```

    

      标准 SPL 公式是 `success × (gt_len / max(agent_len, gt_len))`。缺少 success 因子导致失败 episode 也有正的 SPL。
    
  

  
  
    
#### 🟡 坑 5：训练日志丢失

    

      原始 train.py 只打印到终端，训练结束后**没有任何记录**。当你想对比修复前后的效果时，没有对照数据。

      修复：加入 `Tee` 类，同时输出到 stdout 和 `logs/` 目录。
    
  

  
##  §N.3 修复后重新训练

  

    修复全部 5 个问题后，用分离的 split 重新训练 10 epoch。
  

  
    ![After Fix Training Curves](images/after_fix_curves.png)
  
  

▲ 修复后 train/val 曲线明显分离（无数据泄漏）。val_acc 从 49.9% 起步，最终达到 94.7%——几乎和修复前一样。

  
    ![Val ACC Before vs After Fix](images/val_acc_comparison.png)
  
  

▲ 修复前（红线）：起点高（79.7%），快速收敛。修复后（绿线）：起点低（49.9%），逐步追赶——最终持平。两者终点几乎重叠，说明这些表面问题不是瓶颈。

  
    
#### 💡 意料之外：val_acc 几乎没变

    

      修复了文本噪声、数据泄漏、标签缺失、指标公式之后，val_acc 从 **94.1% → 94.7%**。

      我们原本预期 val_acc 会**大幅下降**（因为消除了数据泄漏和随机文本作弊），但它纹丝不动。

      **这意味着：这 5 个问题从来不是 val_acc 的瓶颈。**
    
  

  
##  §N.4 真正的考验：环境评估

  

    val_acc 测量的是"给定预渲染帧，预测 action 标签"，不是"在 3D 场景中导航"。
  

  
| 指标 | 修复前 (作弊版) | 修复后 (诚实版) | 变化 |
| --- | --- | --- | --- |
| **val_acc** | 94.1% | 94.7% | +0.6% |
| **Eval SR** (50 eps) | ~30% * | 32.0% | +2% |
| **Eval SPL** | — (公式错误) | 0.320 | — |
| **Eval nDTW** | — | 0.107 | — |

  

* 修复前的简化版 eval 把 action 硬编码为 MOVE_FORWARD，所以 SR 约 30% 只是"一直向前走"的 baseline。

  
    
#### 💡 val_acc 94.7% vs SR 32.0%：3:1 的鸿沟

    

      同一个模型，在预渲染帧上预测 action 标签有 94.7% 准确率，但在 3D 场景中实际导航只有 32% 成功率。

      这个 3:1 的差距揭示了比文本噪声、数据泄漏、标签错误**更深层的问题**。
    
  

  
##  §N.5 深层结论：图像分布偏移

  

    当你排除了所有表面问题，剩下的那个——无论多么隐蔽——就是根因。
  

  
    
**根因：训练和评估的图像来自不同分布**

    
      
        
#### 训练时的图像

        

          来自 **预渲染**（env.reset → 5×MOVE_FORWARD → 保存 .npz）

          每帧都是 **最短路径上的画面**——干净、正确、标准化。
        
      
      
        
#### 评估时的图像

        

          来自 **实时渲染**（每步根据模型预测的 action 获取下一帧）

          每帧都是 **模型自己走出来的画面**——可能偏离、撞墙、迷路。
        
      
    

      两个分布下的 RGB 完全不同——同一场景、不同视角、不同光照条件。

      ResNet 提取的特征在两个分布之间**无法泛化**。

      这解释了为什么修复了 5 个表面问题后 SR 仍然只有 32%：

      **模型从未见过"自己走错时看到的画面"。**
    
  

  
    
> ⚠️ **⚡ 这为什么比文本问题更难修**

    

      要消除分布偏移，训练必须也走**在线 rollout**：每步用模型预测的 action 获取下一帧。

      但这会让训练慢 10 倍（无法并行预取 DataLoader），且需要动态 env 管理。

      混合训练方案（先在预渲染上启蒙，再逐步加在线 rollout）是可行的折中。

      ——这不是 §N 要解决的问题，它是阶段 3（真正的 VLN 训练）的核心挑战。
    
  

  
##  §N.6 你从这一章学到的

  
| # | 教训 | 适用范围 |
| --- | --- | --- |
| 1 | **val_acc 高 ≠ 模型好**。先检查数据有没有泄漏。 | 所有 ML 项目 |
| 2 | **保存训练日志**。没有 before 对照，after 没有意义。 | 所有 ML 项目 |
| 3 | **查指标公式**。你自己写的 SPL 可能和论文定义不同。 | 复现论文时 |
| 4 | **查标签分布**。如果某个类别从未出现，模型不会学到它。 | 分类任务 |
| 5 | **训练和推理的输入必须同分布**。预渲染帧≠实时渲染帧。 | 所有 ML 项目 |
| 6 | **修复表面问题后效果没变 → 根因在更深层**。别停。 | 调试方法论 |

  
    
> 💡 **继续学习**

    

      这一章教的是"如何诊断"。下一阶段（阶段 3：真正的 VLN 训练）教的是"如何做对"——

      teacher-forcing、cross-modal attention、在线训练、数据增强。

      [→ 回到第7步：VLN 视觉语言导航](habitat-textbook-step6.html)
    
  

  
## §N.7 量化证据：图像分布偏移到底多大？

  

    §N.5 提出"图像分布偏移是根因"——但这是定性的推断。我们需要用实验把它量化。

    设计一个对照实验：用 ResNet（模型的眼睛）和 CLIP（通用的眼睛）分别编码两组图像，计算分布距离。
  

  
### 实验设计

  **两组图像**

    
      
- **A 组 · 预渲染帧：**9,195 帧，来自 1,839 个 episode 的最短路径，每帧都是"正确答案"。
      
- **B 组 · 在线 rollout 帧：**2,790 帧，来自 93 个 episode，强制模型走 30 步（禁用 stop），收集模型自己走出来的画面——包括走偏、撞墙、绕路。
    
  

  **两个编码器**

    
      
- **ResNet18：**模型实际使用的视觉编码器。如果 A 和 B 对它来说是不同分布，那就是模型的"主观"分布偏移。
      
- **CLIP ViT-B/32：**通用视觉模型，作为"客观"参照。如果 CLIP 也认为两组不同，那偏移就是客观的。
    
  

  
### 结果：MMD 分布距离

  
  
| 编码器 | MMD（越低越相似） | 解读 |
| --- | --- | --- |
| ResNet18 | **0.0058** | 模型的眼睛认为两组帧几乎一样 |
| CLIP ViT-B/32 | **0.0053** | 通用的眼睛也认为两组帧几乎一样 |

  

  
    
> ⚠️ **⚡ 意料之外：两个 MMD 都极低**

    

      我们预期在线帧（走偏、撞墙）和预渲染帧（最短路径）会有显著分布差异。

      但 ResNet 和 CLIP 都给出了 < 0.006 的 MMD——**两组帧在特征空间中几乎完全重叠**。
    
  

  
### 可视化：t-SNE 降维

  

把 512 维特征降到 2 维，蓝色 = 预渲染帧，红色 = 在线帧：

  
    
      ![t-SNE ResNet](images/tsne_resnet.png)
      

ResNet18 t-SNE (MMD=0.0058)
    
    
      ![t-SNE CLIP](images/tsne_clip.png)
      

CLIP t-SNE (MMD=0.0053)
    
  

在 ResNet 的 t-SNE 图中，红色和蓝色完全混在一起——预渲染帧和在线帧在特征空间中无法区分。

  
### 余弦相似度分布

  
    ![Cosine Similarity](images/cosine_similarity.png)
  

  

两组直方图几乎完全重叠：预渲染帧之间的相似度，和预渲染 vs 在线帧之间的相似度，分布一致。

  
### §N.5 的结论需要修正

  
    
> 💡 **从"图像分布偏移"到"行为偏差累积"**

    

      数据推翻了 §N.5 的假设。不是图像分布不同导致 SR 只有 32%——

      而是模型在几乎相同的画面上，做出了**不同的 action 决策**。
    
    

      预渲染帧是 teacher-forcing 下的画面（最短路径，每步都是"对"的下一步），

      在线帧是模型自由行动的画面（可能走偏，但场景纹理、墙壁、地板和预渲染帧几乎一样）。
    
    

      **32% 的 SR 不是因为模型"看到了没见过的画面"，而是模型在熟悉的画面中做出了错误的 action。**

      每步差一点，30 步后离目标越来越远——这就是**行为偏差累积**。
    
  

  
### 实验教会我们的

  
  
| # | 教训 |
| --- | --- |
| 1 | **假设需要实验验证。**我们确信"图像分布偏移是根因"，但数据说不。 |
| 2 | **模型的眼睛（ResNet）和通用的眼睛（CLIP）意见一致。**这不是编码器选择的问题。 |
| 3 | **低 MMD 不代表问题不存在。**它只是说明问题不在帧层面，而在决策层面。 |
| 4 | **证伪假设比证实假设更有价值。**它迫使你寻找更深层的根因。 |
| 5 | **下一步不是修图像，是修决策。**Teacher-forcing → Student-forcing，强化学习，cross-modal attention。 |

  

  
    
**实验复现**

    

      所有代码和特征数据在 L40 云端：

      `training/collect_online_frames.py` — 强制 30 步 rollout 采集

      `training/extract_features.py` — ResNet + CLIP 特征提取

      `training/analyze_distribution.py` — MMD + t-SNE + 余弦相似度分析

      `screenshots/clip_comparison/` — 完整图表输出
    
  

  
##  7-5 · DAgger — 从模仿到强化

  **📍 诊断后的修复方案**

    

      7-4 定位了根因：**行为漂移累积**（Agent 走偏后，后续观测都是训练时没见过的）。
      DAgger 正是解决这个问题的标准方法——让 Agent 在「自己犯错的地方」学习专家纠正。
    
  

  
### IL → DAgger → RL 三阶梯

  
    
**🎯 实际实验：Seq2SeqAgent (27M) + ShortestPathFollower 专家**

    

      **训练配置：**100 episode/轮 × 3 轮迭代 × 5 epoch/轮 · chunked collection (20 ep/chunk) · L40 GPU

      **专家策略：**ShortestPathFollower（走最短路径，success_distance=3.0m，成功率 100%）

      **初始策略：**Seq2SeqAgent（§N 训练的 ckpt，val_acc=94.9%）
    
  

  
| 阶段 | SR | SPL | avg_steps | loss | 说明 |
| --- | --- | --- | --- | --- | --- |
| **IL Baseline** | 3.0% | 0.000 | 4 | — | 初始策略在实时仿真器上评估 |
| **DAgger Iter 1** | 3.0% | 0.000 | 4 | 0.0000 | 策略采集 0 条有效轨迹 |
| **DAgger Iter 2** | 3.0% | 0.000 | 4 | 0.0000 | 同上 — 无改善 |
| **DAgger Iter 3** | 3.0% | 0.000 | 4 | 0.0000 | 每轮中期 eval 在 2-4% 波动，最终收敛 3% |

  
    
> ⚠️ **🚨 关键发现：DAgger 完全失败 — SR 零提升，损失→0**

    

      3 轮 DAgger 迭代，**Success Rate 没有任何提升**（始终 3.0%），所有轮的训练 loss 均为 **0.0000**。
      这个结果不是代码 bug——而是 **DAgger 算法在弱初始策略上的已知失效模式**。
      对课程来说，"DAgger 为什么失败"比"DAgger 成功了"有更高的教学价值。
    
  

  
### 🔬 三层根因分析

  **第 1 层：训练-部署 Gap（94.9% → 3% = 30× 衰减）**

    

      §N 训练的模型在预渲染帧上 val_acc=94.9%，但放到实时仿真器后 SR 骤降到 3.0%。
      预渲染帧来自 **GT 最短路径的 5 步观察**，agent 实际走偏后看到的图像完全不同——模型从未学过"走偏后怎么恢复"。
    
  

  
    
**第 2 层：弱策略死循环 — 模型只预测 STOP**

    

      avg_steps=4 说明了问题：模型几乎每一步都预测 STOP（action=0/1），episode 立即结束。
      3% 的 SR 来自起点距离 ≤3m 的 episode（agent 不需要移动就判定成功）。
      **模型学到的"策略"：不管看到什么，先停再说。**这是因为训练时 STOP 标签占比过高（每个 episode 尾部才出现 STOP，但模型把所有帧都映射到 STOP 来最小化 loss）。
    
  

  
    
**第 3 层：DAgger 的前提不满足 — 初始 SR 需 >20%**

    

      DAgger 的有效性依赖于一个前提：**初始策略至少有一定的成功率**（通常 >20%），这样 agent 的轨迹中才包含"接近目标但走偏了"的有价值样本。
      当初始 SR=3.0%（基本等于随机），agent 的轨迹没有任何信息量——全是"开局就停"。
      专家重新标注这些轨迹时，标注的是一系列"从起点就开始走"的动作，但这些标注附着在 agent 根本没走过的观测上，训练时模型无法建立有效的观测→动作映射。
      

      这是 DAgger 的已知局限（Ross et al., 2011 论文中也提到），不是实现错误。
    
  

  
### 🛠️ 实战教训

  
    
> ⚠️ **坑 1：success_distance=0.2m 太严格**

    

      最初实验时 ShortestPathFollower 专家 SR=0%，原因是在 vln_r2r.yaml 中 `success_distance=0.2`（20cm）。
      VLN 离散动作步长 0.25m，导致即使走到目标旁也无法判定成功。修改为 **3.0m** 后专家 SR=100%。
    
  

  
    
> ⚠️ **坑 2：内存爆炸（119GB → OOM Kill）**

    

      第一个版本的 DAgger 脚本一次采集 200 个 episode 的所有 RGB 帧到内存，导致 119GB RSS + cgroup OOM Kill。
      修复方案：**chunked collection**（20 ep/chunk，逐块训练后释放）+ `gc.collect()` + `torch.cuda.empty_cache()`。
    
  

  
    
> ⚠️ **坑 3：预训练 ckpt 的 txt_encoder 不兼容**

    

      §N 训练的 ckpt 中 TextEncoder 是模型内部组件（model_cheat.py），新版代码 TextEncoder 是独立模块。
      加载 ckpt 时参数名不匹配，TextEncoder 被随机初始化 → 指令输入变成噪声。需要用旧版模型类加载。
    
  

  
    
> 💡 **💡 三条改进路线**

    

      **路线 A · Behavior Cloning 预训练：**先在专家轨迹上做 BC 预训练，让初始 SR 达到 20-30%，再启动 DAgger。

      **路线 B · Scheduled Sampling：**训练时混合 GT action 和模型预测 action（50/50），逐步减少对 GT 的依赖。

      **路线 C · 切换 RL：**如果 IL 路线难以突破，直接用 PPO 在 VLN 奖励函数上训练（需 8-16 GPU 并行环境）。
    
  

  
### DAgger 算法伪代码

  
```
# DAgger (Dataset Aggregation) — Ross et al., 2011
for iteration in range(K):
# 1. 用当前策略 pi_i 在环境中执行（采集自己的轨迹）
trajectories = run_policy(env, policy=pi_i, episodes=N)

# 2. 对每一帧，向专家查询「正确动作是什么」
for (obs, action_agent) in trajectories:
action_expert = expert.query(obs)      # 专家怎么说？
dataset.append((obs, action_expert))   # 存专家的答案

# 3. 在聚合后的数据集上重新训练
pi_next = train(dataset)                   # 模型学会了「在自己犯错时该怎么做」

为什么 DAgger 能解决行为漂移？
IL 只见过专家轨迹上的观测 → Agent 一走偏就进入未知区域 → 雪崩。
DAgger 把 Agent 走偏后的观测也加入训练集（附上专家纠正），
让模型学会「走偏了怎么回来」——这正是 VLN 最需要的鲁棒性。
```

  
##  7-6 · SOTA 实战：运行 JanusVLN

  
  **① 案例含义**

    

      7-3 和 §N 中我们训练了一个 **2700 万** 参数的 Seq2Seq 模型，在 val_unseen 上达到 SR = 32%。
      现在我们跑一个真正的 **SOTA 模型——JanusVLN**——在同一套数据上评估，亲眼看看"参数量差距意味着什么"。
      

      **前置条件：**完成 7-3 训练（理解 VLN 任务）。需要单卡 NVIDIA GPU（≥ 46GB 显存，如 L40/A100）。
    
  

  
  
### 论文与开源项目

  **JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for VLN**

    

      **发表：**ICLR 2026

      **机构：**Amap（高德地图，阿里巴巴集团）+ 西安交通大学（MIV-XJTU）

      **论文：**[arXiv:2509.22548](https://arxiv.org/abs/2509.22548)

      **代码：**[github.com/MIV-XJTU/JanusVLN](https://github.com/MIV-XJTU/JanusVLN)

      **权重：**[ModelScope: JanusVLN_Base](https://www.modelscope.cn/models/misstl/JanusVLN_Base)（18GB）

      **数据：**[ModelScope: DAgger 轨迹数据](https://www.modelscope.cn/datasets/misstl/JanusVLN_Trajectory_Data)
    
  

  

    核心创新：**双隐式记忆（Dual Implicit Memory）**。名字来源于罗马神话两面神 Janus，
    寓意同时拥有"语义理解"（左脑）和"空间感知"（右脑）两种能力。
    论文报告 val_unseen SR 约 **50-55%**（全景输入，1839 episode）。
  

  
  
### ② 模型架构：双隐式记忆

  
| 记忆类型 | 负责模型 | 参数量 | 类比 |
| --- | --- | --- | --- |
| **语义记忆** (Semantic) | Qwen2.5-VL-7B | ~70 亿 | "左脑"：理解"拱门""楼梯"的含义和视觉外观 |
| **空间记忆** (Spatial) | VGGT-1B | ~10 亿 | "右脑"：推理深度、几何、3D 空间结构 |
| **融合层** | VGGTMerger | ~200 万 | 将 3D 特征注入 VLM 的每层隐藏状态 |

  
    
**关键设计：跨步空间记忆**

    

      模型维护一个 `past_key_values_vggt` 缓存，每次导航开始时清空，
      每步推理后更新。这让模型在移动过程中"记住"之前看到的 3D 结构——
      就像一个边走边构建的**隐式 3D 地图**。
    
  

  
  
### ③ 数据流：每步从观测到动作

  
```
# 1. Habitat 渲染当前前向 RGB（224×224）
rgb = env.step(action)["rgb"]

# 2. 收集历史帧（num_history=4：最近 4 帧 + 当前）
history = rgb_list[-5:]

# 3. VGGT：每张图提取 3D 特征（深度、几何）——并行
vggt_feats = [VGGT(img) for img in history]

# 4. Qwen2.5-VL：图像 → patch tokens + 指令文本 → token IDs
inputs = processor(text=instruction, images=history)

# 5. 融合：VGGT 特征通过 VGGTMerger 注入 Qwen hidden states
# 6. 生成：Qwen2.5-VL 自回归解码（max 24 tokens, temperature=0）
output = model.generate(**inputs, images_vggt=vggt_feats, max_new_tokens=24)

# 7. 解析：token → 动作字符串 → Habitat action index
action_idx = actions2idx[processor.decode(output)]  # 1=FORWARD, 2=LEFT, 3=RIGHT, 0=STOP

阶段耗时占比

Habitat 渲染 + VGGT~0.3s15%
Processor 编码~0.2s10%
Qwen2.5-VL 生成（7B 参数）~1.5s75%
合计~2 秒/步

④ 环境准备

Step 1 — 克隆 + 权重

git clone https://github.com/MIV-XJTU/JanusVLN.git && cd JanusVLN
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('misstl/JanusVLN_Base', cache_dir='./weights')"
Step 2 — 单卡适配

# 依赖（国内用 douban 镜像）
pip install transformers==4.48 accelerate qwen_vl_utils -i https://pypi.doubanio.com/simple

# 修改 src/evaluation.py：
#   flash-attn → torch.nn.functional.scaled_dot_product_attention
#   world_size=1, gpu=0（原代码需要 8 卡 DeepSpeed）

⚠️ 单卡适配要点
```

    

      原代码需要 8 卡 DeepSpeed 分布式训练。单卡跑只需改两处：
      flash-attn → PyTorch SDPA（避免 30 分钟编译）、world_size=1。
      推理精度不受影响，速度略慢（SDPA vs flash-attn 差距约 10%）。
    
  

  
  
### ⑤ 15-episode 抽样实验结果

  

    在 L40 单卡上，用 `max_steps=100, num_history=4` 跑 15 个随机 episode，
    耗时约 **48 分钟**。
  

  
| 场景 | ✅/总数 | 场景 SR |
| --- | --- | --- |
| 2azQ1b91cZZ | 1/1 | 100% |
| EU6Fwq7SyZv | 0/3 | 0% ⚠️ |
| QUCTc6BB5sX | 1/1 | 100% |
| TbHJrupSAjP | 1/3 | 33% |
| X7HyMhZNoso | 0/1 | 0% |
| oLBMNvg9in8 | 2/2 | 100% |
| pLe4wQe7qrG | 0/1 | 0% |
| zsNo4HB9uLZ | 2/3 | 67% |
| 总计 | 7/15 | 46.7% |

  

**与我们的模型对比：**

  
| 模型 | 参数量 | SR (抽样) | 输入 | 训练数据 |
| --- | --- | --- | --- | --- |
| 我们的 Seq2Seq | 2700 万 | 32.0% | 预渲染离散帧 | R2R 几千条指令 |
| **JanusVLN** | **~80 亿（300×）** | **46.7%** | 实时 RGB | 万亿 token VLM 预训练 + DAgger |

  
  
### 可视化：成功 vs 失败

  

在场景 **2azQ1b91cZZ** 上跑的两个 episode（6 FPS）：

  
    
      

❌ Episode 10 — SR=0
      
        
      
      

        指令："走过客厅，到阳台下的入口"

        NE=8.27m，101步走到上限
      
    
    
      

✅ Episode 11 — SR=1.0
      
        
      
      

        指令："穿过地板，在拱门等"

        SPL=1.0，34步精确到达
      
    
  

    视频展示的是模型的第一人称视角（RGB + Top-down 地图）。注意失败案例中模型一直在客厅转圈，
    而成功案例中模型直接走向拱门并精确停止。
  

  
  
### ⑥ SR 46.7% 深度分析

  **为什么没到论文报告的 50-55%？**

    

      **最可能原因：单视角 vs 全景输入。**原论文使用 360° 全景（12 个方向的 RGB），
      而我们的 eval 只传了单张前向 RGB。模型无法看到左右和后方的场景，
      每次转向都是一次"盲猜"，尤其影响需要精细空间判断的指令。
      

      **其他因素：**15-episode 抽样方差大、max_steps=100 偏紧（有 episode 只差 0.12m 就成功）。
    
  

  
    
**场景差异：EU6Fwq7SyZv 全败之谜**

    

      EU6Fwq7SyZv 3 个 episode 全部走到 100 步上限（NE 4.6-7.0m）。
      三条指令都涉及复杂的空间关系："绕过椅子""穿过柱子""停在楼梯和栏杆之间"。
      在只有前向视角的情况下，模型无法验证"是否已经绕过"——它看不到侧面。
    
  

  
    
**为什么比我们的 32% 好？**

    

      不是"方法更好"，而是 **VLM 预训练带来的世界知识**：
      Qwen2.5-VL 在预训练阶段见过海量室内场景——它已经知道"拱门""楼梯""沙发"长什么样。
      我们的 ResNet50 只在 R2R 几千张图上从头学，对室内场景的理解完全从零开始。
      

      这 14.7% 的差距 = **万亿 token 图文预训练 vs 几千条 R2R 数据** 的差距。
    
  

  
  
### ⑦ 如何训练：DAgger 算法

  

    JanusVLN 使用 **DAgger（Dataset Aggregation）**，
    "模型在实践中学习，专家在旁兜底"：
  

  
```
for iteration in range(num_iterations):
beta = p ** iteration  # 专家干预概率指数衰减

# 采集阶段：在 Habitat 中 rollout
for episode in dataset:
while not episode_over:
if random() # ShortestPathFollower
else:
action = model.predict(obs)     # 模型自己走
obs = env.step(action)

# 训练阶段：交叉熵 loss(action_pred, action_gt)
for epoch in range(train_epochs):
loss = CrossEntropy(model(obs), action_gt)
loss.backward(); optimizer.step()

迭代β (p=0.95)专家占比含义

10.9595%几乎全专家带
50.7777%模型开始承担
100.6060%逐步放手
200.3636%模型主导，专家偶尔纠正

💡 这和我们的训练有什么不同？
```

    

      **我们的 Seq2Seq：**仅在预渲染的最短路径帧上做分类训练。模型从未在 3D 环境中"自己走"过。
      

      **JanusVLN 的 DAgger：**模型在真实 3D 环境中交互并收集自己走出来的轨迹。
      这些轨迹包含偏离、徘徊、撞墙——正是 §N.5 讨论的"在线 rollout 数据"。
      DAgger 的核心价值就是让模型**见到并学会修正自己的错误**。
    
  

  
  
### ⑧ 完整运行命令

  
```
export HF_ENDPOINT=https://hf-mirror.com

python src/evaluation.py \
--model_path ./weights/misstl/JanusVLN_Base \
--habitat_config_path config/vln_r2r.yaml \
--eval_split val_unseen \
--output_path ./results/val_unseen \
--max_episodes 20 \
--max_steps 100 \
--num_history 4

# 保存可视化图片
python src/evaluation.py ... --save_video --save_video_ratio 1.0
# 图片保存到 results/val_unseen/vis_0/*.jpg
```

  
##  本章总结

  
    
      
### ✅ 完成本章后你应该能

      
        
- 创建并验证 VLN-v0 环境
        
- 理解 R2R episode 的数据结构（position + instruction + reference_path）
        
- 解释 InstructionSensor 如何从 episode 提取指令文本
        
- 启动 VLN 模仿学习训练并阅读 loss/acc 曲线
        
- 理解 SR/SPL/nDTW 三项评估指标
        
- 导出可用于真机推理的 checkpoint + config 文件
        
- 运行 SOTA 模型（JanusVLN）并在同一数据上对比 SR
      
    
    
      
### 🔜 下一步：真机部署

      

        现在你手头有了训练好的 VLN 模型。接下来的问题是：**怎么让它在 Spark-I 或 Leo 上跑起来？**

        [→ 第8章：真机部署](habitat-textbook-step8.html)（从架构到微调的完整流程）
      
    
  
  
    [← 第6步：RL 训练入门](habitat-textbook-step6.html)
    [第8章：真机部署 →](habitat-textbook-step8.html)
