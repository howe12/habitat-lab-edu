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
