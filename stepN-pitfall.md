# §N 避坑实战：一个 VLN 训练管线的诊断与修复 — Habitat 从零理解

> 你接手了一个 VLN 训练项目，val_acc = 94.9%——看起来非常好。但这是真的吗？
    本章带你逐一发现并修复 5 个工程暗坑，最终面对一个诚实但残酷的结论。

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

      [→ 回到第6章：VLN 仿真训练](habitat-textbook-step6.html)
    
  

  
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
