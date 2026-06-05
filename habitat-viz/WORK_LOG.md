# Habitat-Viz 工作记录

> 记录日期：2026-05-26
> 工程师：Claude (DeepSeek-V4-Pro)

---

## 一、本次会话工作内容

### 1. 连接 Step 5 导航链

**问题**：`habitat-textbook-step5.html` 已在上个会话创建，但未被链接到站点导航中。

**操作**：
- 更新 `habitat-textbook-step4.html` 底部导航：将 "(即将上线)" 替换为真实链接 `<a href="habitat-textbook-step5.html" class="next">`
- 更新 `index.html`：将 STEP 5 从虚线边框占位符改为可点击链接卡片（琥珀色主题）
- `habitat-textbook-step5.html` 底部已有正确的 prev/next 链接，无需修改

**结果**：Step 1→2→3→4→5 完整导航链打通。

---

### 2. 将 Steps 4/5 添加到 hub-card 主区域

**问题**：用户指出 `index.html` 的 `hub-grid` 区域（主页卡片区）只显示 Steps 1-3，Steps 4/5 仅在下方 `step-road` 中显示。

**操作**：
- 将 `step-road` CSS grid 从 `repeat(3, 1fr)` 扩展为 `repeat(5, 1fr)`
- 在 `hub-grid` 中添加 Step 4（粉色 `#ec4899` 顶部边框）和 Step 5（琥珀色 `#f59e0b` 顶部边框）两个完整的 hub-card
- 下方的 "Future steps preview" 区域仅保留 Step 6 占位符

**涉及文件**：`/develop/habitat-lab/habitat-viz/index.html`

**结果**：`hub-grid` 和 `step-road` 两个区域均包含 Steps 1-5，视觉一致。

---

### 3. 修复 example.py 运行问题（核心问题）

**问题**：用户在运行 `examples/example.py` 时遇到 TLS 握手失败错误：

```
fatal: unable to access 'https://huggingface.co/datasets/ai-habitat/ReplicaCAD_dataset.git/':
gnutls_handshake() failed: The TLS connection was non-properly terminated.
```

原因：`HabitatRenderPick-v0` 需要从 HuggingFace 下载 ReplicaCAD 数据集（约 500MB），国内网络无法访问。

**解决方案**：
1. 创建新示例文件 `examples/example_pointnav.py`，使用 PointNav 任务 + 本地 `habitat-test` 数据集
2. PointNav 数据集已存在于 `/develop/habitat-lab/data/datasets/pointnav/habitat-test-scenes/`（无需网络）
3. 运行验证成功：RGB(256,256,3)、Depth(256,256,1)、GPS Compass，8 步 episode 结束

**新文件**：`/develop/habitat-lab/examples/example_pointnav.py`

```python
#!/usr/bin/env python3
"""PointNav gym example — no network download needed."""
import gym
import habitat.gym  # noqa: F401 — registers Habitat-v0

env = gym.make(
    "Habitat-v0",
    cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
)
obs = env.reset()
print("Keys:", obs.keys())  # → ['depth', 'pointgoal_with_gps_compass', 'rgb']
```

---

### 4. 更新 Step 2 HTML 页面

**问题**：`habitat-textbook-step2.html` 中的 2-1 示例引用的是 `example.py` + `HabitatRenderPick-v0`，无法实际运行。

**操作**（涉及文件 `habitat-textbook-step2.html`）：

| 位置 | 旧内容 | 新内容 |
|---|---|---|
| 总览表 2-1 | `example.py`, "Gym API 接口" | `example_pointnav.py`, "PointNav 任务...无需联网" |
| 进度清单 | `example.py` 随机动作循环 | `example_pointnav.py` PointNav 随机动作循环 |
| 2-1 标题/副标题 | "example.py — 31 行代码" | "example_pointnav.py — 35 行代码...无需联网" |
| 代码块 | `HabitatRenderPick-v0` + Rearrange 注释 | `Habitat-v0` + PointNav 完整代码 |
| 运行命令 | `python examples/example.py` + 247 steps | `python examples/example_pointnav.py` + 实际输出 |
| "你在看什么？" | 机械臂/物体重排说明 | PointNav 导航任务说明 |
| 警告框 | "没有 display" (render_mode) | "关于官方 example.py"（解释网络问题） |
| Q6 | "打开 example.py" | "打开 example_pointnav.py" |

---

## 二、关键文件清单

### 新增文件
- `/develop/habitat-lab/examples/example_pointnav.py` — PointNav Gym 示例（无需网络）

### 修改文件
- `/develop/habitat-lab/habitat-viz/index.html` — 添加 Steps 4/5 到 hub-grid 和 step-road
- `/develop/habitat-lab/habitat-viz/habitat-textbook-step4.html` — Step 5 导航链接
- `/develop/habitat-lab/habitat-viz/habitat-textbook-step2.html` — 2-1 示例全面更新

### 上个会话已创建（本会话未修改）
- `/develop/habitat-lab/habitat-viz/habitat-textbook-step5.html` — 训练与评测完整教程
- `/develop/habitat-lab/habitat-viz/step4_outputs/` — Step 4 实验截图和数据

---

## 三、环境说明

- **Python 环境**：`/develop/conda_envs/habitat` (conda)
- **工作目录**：`/develop/habitat-lab`
- **本地数据集**：已存在 `habitat-test` PointNav 数据（路径 `data/datasets/pointnav/habitat-test-scenes/`）
- **GPU**：NVIDIA GeForce RTX 2070 SUPER
- **OS**：Ubuntu 22.04
- **Habitat 版本**：habitat-lab v0.2.5, habitat-sim 0.2.5

---

## 四、运行验证命令

```bash
cd /develop/habitat-lab
source activate habitat
python examples/example_pointnav.py
```

期望输出：
```
Observation keys: ['depth', 'pointgoal_with_gps_compass', 'rgb']
RGB shape: (256, 256, 3)
Depth shape: (256, 256, 1)
Agent acting inside environment (random actions).
Episode finished after 8 steps.
Metrics: {'distance_to_goal': 11.90, 'success': 0.0, 'spl': 0.0, ...}
```