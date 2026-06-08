# 课程优化计划

> 基于 2025-06-05 Daisy (全景扫描) + Wendy (教材审查) 的联合分析报告
> 状态：规划中 | 负责人：Monica (协调)

---

## 一、现状总览

| 维度 | 已覆盖 | 未覆盖 |
|------|--------|--------|
| 任务类型 | PointNav, VLN, 5种导航(理论) | Rearrange全系, EQA |
| 训练方法 | PPO (单机) | DD-PPO实操, HRL, VER |
| 传感器 | RGB, Depth, GPS+Compass, Proximity | 语义实操, 全景/鱼眼, 关节/末端传感器 |
| 数据集 | 测试数据 | 完整数据集获取流程 |
| 部署 | ROS桥接(代码) | Docker容器化 |
| 指标 | Success, SPL, DistanceToGoal | soft_spl, nDTW, 自定义Measure |

**现有7章**：安装 → PointNav演示 → 源码精读 → 配置实验 → 训练全景 → VLN仿真 → ROS桥接 (+ 第8步VLM)

---

## 二、实施路线图

### Phase 1：核心缺口 (P0 — 补齐后覆盖 Habitat 80%+ 能力)

| ID | 任务 | 目标 | 新增文件 | 预估 |
|----|------|------|---------|------|
| P0-1 | **Step1B — 完整数据集下载指南** | 教会用户获取 Gibson/MP3D/HM3D/ReplicaCAD 的完整流程 | `habitat-viz/habitat-textbook-step1b.html` | 1天 |
| P0-2 | **Step9 — Rearrange 操作任务** | Pick/Place/Open/Close + PDDL 复合任务，4-5案例 | `habitat-viz/habitat-textbook-step9.html` | 4天 |
| P0-3 | **Step5B — DD-PPO 分布式训练** | 单机2卡/4卡完整配置、命令、排错 | `habitat-viz/habitat-textbook-step5b.html` 或合并入 Step5 | 1天 |

#### P0-1 Step1B 大纲

① 场景数据集全景：Gibson vs MP3D vs HM3D vs ReplicaCAD 对比
② 获取流程：官网申请 → 签署协议 → 下载 → 解压到正确目录
③ 任务数据集：PointNav/ObjectNav/ImageNav/Rearrange episode 文件
④ 目录结构规范：`data/scene_datasets/` vs `data/datasets/`
⑤ 验证：完整性检查命令、场景ID确认

#### P0-2 Step9 大纲

① 概述：Rearrange vs Navigation 的本质区别（交互 vs 观察）
② Case 1 — 理解 Rearrange 环境：robot + 物体 + 动作空间
③ Case 2 — Pick 任务：抓取物体，ArmRelPos + Gripper + 约束
④ Case 3 — Place 任务：放置到目标位置
⑤ Case 4 — Open/Close 关节物体（抽屉/冰箱）
⑥ Case 5 — PDDL 复合任务：TidyHouse 完整流程
⑦ 训练：Rearrange 的 PPO/HRL 配置

#### P0-3 Step5B 大纲

① DD-PPO 原理：数据并行 vs 模型并行，场景级采样
② 单机多卡配置：`num_processes` / `num_processes_per_gpu`
③ 完整运行命令 + 预期输出
④ 性能对比：单机1卡 vs 4卡吞吐量
⑤ 常见故障：NCCL超时、OOM、负载不均

---

### Phase 2：深度提升 (P1)

| ID | 任务 | 新增文件 | 预估 |
|----|------|---------|------|
| P1-1 | 语义传感器实操案例（合并到 Step4） | 修改 Step4 | 0.5天 |
| P1-2 | 碰撞检测 + 自定义 Measure 教程 | 修改 Step4 或新增专题 | 0.5天 |
| P1-3 | HRL + VER 训练方法对比（合并到 Step5） | 修改 Step5 | 1天 |
| P1-4 | Docker 部署方案（合并到 Step1 或 Step7） | 修改现有 | 1天 |
| P1-5 | EQA 任务补充到 Step5 任务全景 | 修改 Step5 | 0.5天 |
| P1-6 | Gym 环境完整注册表（合并到 Step2） | 修改 Step2 | 0.5天 |

---

### Phase 3：锦上添花 (P2)

| ID | 任务 | 新增文件 | 预估 |
|----|------|---------|------|
| P2-1 | 论文精读专题（Habitat 1.0/2.0, PointNav基准, VLN） | 新专题页 | 2天 |
| P2-2 | Habitat Challenge 参赛指南 | 新专题页 | 1天 |
| P2-3 | 传感器深度专题 | 新专题页 | 1天 |
| P2-4 | Jupyter Notebook 版本 | `notebooks/` | 1天 |
| P2-5 | 多智能体仿真专题 | 新专题页 | 1天 |

---

## 三、进度跟踪

### Phase 1

- [x] P0-1: Step1B — 完整数据集下载指南
- [x] P0-2: Step9 — Rearrange 操作任务全教程
- [x] P0-3: Step5B — DD-PPO 分布式训练实操

### Phase 2

- [x] P1-1: 语义传感器实操案例
- [x] P1-2: 碰撞检测 + 自定义 Measure
- [x] P1-3: HRL/VER 训练方法对比
- [x] P1-4: Docker 部署方案
- [x] P1-5: EQA 任务补充
- [x] P1-6: Gym 环境注册表

### Phase 3

- [ ] P2-1: 论文精读专题
- [ ] P2-2: Habitat Challenge 参赛指南
- [ ] P2-3: 传感器深度专题
- [ ] P2-4: Jupyter Notebook 版本
- [ ] P2-5: 多智能体仿真专题

---

## 四、检查清单（Hook 用）

以下标记供 `check_curriculum.sh` hook 自动扫描：

<!-- CHECK:STEP1B --> Step1B 数据集下载指南 — 文件: habitat-viz/habitat-textbook-step1b.html
<!-- CHECK:STEP9 --> Step9 Rearrange 操作任务 — 文件: habitat-viz/habitat-textbook-step9.html
<!-- CHECK:STEP5B --> Step5B DD-PPO 训练 — 文件: habitat-viz/habitat-textbook-step5b.html (或 Step5 扩展)

<!-- CHECK:P1_SEMANTIC --> 语义传感器实操 — 文件: Step4 扩展
<!-- CHECK:P1_MEASURE --> 自定义 Measure — 文件: Step4 扩展或专题
<!-- CHECK:P1_HRL --> HRL/VER 训练对比 — 文件: Step5 扩展
<!-- CHECK:P1_DOCKER --> Docker 部署 — 文件: Step1 或 Step7 扩展
<!-- CHECK:P1_EQA --> EQA 补充 — 文件: Step5 扩展
<!-- CHECK:P1_GYM --> Gym 注册表 — 文件: Step2 扩展
