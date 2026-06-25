# 第9章：Rearrange 操作任务 — Habitat 从零理解

> Habitat 2.0 的核心贡献——从"导航到目标点"升级为"与物体交互"。
    本章覆盖 Pick/Place、关节物体、PDDL 复合任务，从简单的抓取到复杂的多阶段家居操作。

##  案例总览

| # | 案例 | 难度 | 学什么 |
| --- | --- | --- | --- |
| 1 | Navigation vs Rearrange 全景对比 | ⭐ | 任务空间、动作空间、物理仿真的本质差异 |
| 2 | Pick 任务：抓取物体 | ⭐⭐ | ArmRelPos + SuctionGrasp + 物体会话 |
| 3 | Place 任务：放置物体 | ⭐⭐ | 持物约束、目标位姿传感器 |
| 4 | NavToObj：纯导航子任务 | ⭐⭐ | 无手臂控制的底盘导航 |
| 5 | 关节物体：开关抽屉/冰箱 | ⭐⭐⭐ | Marker 交互 + 关节物体物理 |
| 6 | PDDL 复合任务：TidyHouse | ⭐⭐⭐ | Pick→Nav→Place 多阶段编排 |

##  案例 1：Navigation vs Rearrange — 全景对比

**① 案例含义**

理解 Rearrange 和 Navigation 的本质差异。Rearrange 引入了**物理仿真、机器人本体、物体交互**，
是 Habitat 2.0 论文的核心升级。对初学者而言，最关键的认知转换是：
**不再是"走到某个点"，而是"改变这个世界的状态"**。

| 维度 | Navigation (PointNav) | Rearrange (Pick/Place) |
| --- | --- | --- |
| **智能体** | 看不见的"点"（radius=0.1 碰撞球） | Fetch 机器人（有底盘+手臂+夹爪的 URDF 模型） |
| **物理引擎** | 无（只有碰撞检测） | 必须开启 Bullet 物理仿真 |
| **动作空间** | 离散：STOP/FWD/LEFT/RIGHT | 连续：ArmJoint(7维) + Grip(1维) + BaseVel(2维) |
| **场景内容** | 静态网格 | 场景 + 可抓取物体(YCB) + 接收器(receptacle) |
| **成功条件** | 智能体停在 target 附近（

② 核心代码 & 关键函数

```
import habitat
import numpy as np

# ① 加载配置 — 使用预置的 pick benchmark
config = habitat.get_config("benchmark/rearrange/pick.yaml")

# ② (可选) 重写部分配置
with habitat.config.read_write(config):
    config.habitat.environment.max_episode_steps = 300

# ③ 创建环境 — 自动下载 ReplicaCAD + YCB + robot URDF
env = habitat.Env(config=config)

# ④ 观察空间
obs = env.reset()
print("Observation keys:", list(obs.keys()))
for k, v in obs.items():
    print(f"  {k:30s} shape={v.shape}")

# ⑤ 动作空间 — 与 PointNav 完全不同！
print("\nAction space:", env.action_space)
# 输出类似: Dict(arm_action: Box(0.0, 1.0, (10,)), ...)

# ⑥ 采样并执行一个随机动作
action = env.action_space.sample()
obs, reward, done, info = env.step(action)
print(f"\nReward: {reward:.4f}, Done: {done}")
print(f"Info: {info}")
env.close()
```

| 关键函数/配置 | 角色 | 说明 |
| --- | --- | --- |
| `habitat.get_config("benchmark/rearrange/pick.yaml")` | 加载预置配置 | 自动设置 RearrangeSim + Fetch robot + Pick task |
| `env.action_space` | 动作空间定义 | Dict: {"arm_action": Box(10,), "grip_action": Box(1,), "base_vel": Box(2,)} |
| `arm_action` | 机械臂关节控制 | 7 维 delta joint position（相对关节角度变化） |
| `SuctionGraspAction` | 吸盘抓取 | 1 维: 正值=吸, 负值=放 |
| `is_holding` | 持物状态传感器 | 0/1: 是否正吸着物体 |
| `joint` | 关节角度传感器 | 7 维: 每个关节的当前角度 |

> 💡 **③ 如何运行**

```
$ python pick_demo.py
```

首次运行会自动下载 `rearrange_task_assets`（约 2-5 分钟），之后不再需要等待。

**④ 预期传感器输出**

head_depth → `shape=(256, 256, 1)`
机器人头部深度相机
joint → `shape=(7,)`
手臂 7 个关节角度
is_holding → `shape=(1,)`
0 = 未抓取，1 = 已抓取
obj_start_sensor → `shape=(3,)`
物体相对 EE 的位置
relative_resting_position → `shape=(3,)`
EE 到休息位的向量
joint_vel → `shape=(7,)`
关节速度

**⑤ 输出含义**

**obj_start_sensor**：物体中心在机器人末端执行器坐标系下的 3D 偏移量 (Δx, Δy, Δz)。

机械臂控制的目标就是把这个向量趋近于 0——即 EE 接触到物体。

**is_holding** 从 0 → 1 的瞬间标志着一次成功的抓取。

**joint** 是 7 自由度 Fetch 手臂的当前位姿: shoulder_pan, shoulder_lift, upperarm_roll, elbow_flex, forearm_roll, wrist_flex, wrist_roll。

##  案例 3：Place 任务 — 放置物体

**① 案例含义**

智能体**已持有一个物体**（初始状态 is_holding=1），需要导航到底座目标位置并释放物体。
Pick vs Place 的最大区别：Pick 需要先接近物体→抓取；Place 已经持有物体→只需导航+释放。

```
import habitat

config = habitat.get_config("benchmark/rearrange/place.yaml")

with habitat.config.read_write(config):
    config.habitat.environment.max_episode_steps = 300

env = habitat.Env(config=config)
obs = env.reset()

# 关键差异：初始状态下 is_holding=1
print("is_holding at start:", obs["is_holding"])
# → [1.0] — agent 已经抓着物体

# obj_goal_sensor: 目标位置（不是物体位置！）
print("goal_pos (relative to EE):", obs["obj_goal_sensor"])

# Place 特有传感器
for key in ["obj_goal_sensor", "obj_start_sensor",
           "obj_goal_gps_compass"]:
    print(f"  {key:30s} = {obs[key]}")

env.close()
```

| 传感器 | Pick 有? | Place 有? | 含义 |
| --- | --- | --- | --- |
| `obj_start_sensor` | ✅ | ✅ | 物体位置（EE 坐标系） |
| `obj_goal_sensor` | ❌ | ✅ | 目标放置位置（EE 坐标系） |
| `obj_goal_gps_compass` | ❌ | ✅ | 目标在 robot base 坐标系的极坐标 (ρ, φ) |
| `is_holding` | ✅ (初始 0) | ✅ (初始 1) | 抓取状态 |

##  案例 4：NavToObj — 纯导航子任务

**① 案例含义**

NavToObj 是 Rearrange 系列中最接近 PointNav 的任务——**没有机械臂控制**，
只需要用底盘速度控制导航到目标物体或接收器。这使它成为从 Navigation 过渡到 Rearrange 的理想跳板。

```
import habitat

config = habitat.get_config("benchmark/rearrange/nav_to_obj.yaml")
env = habitat.Env(config=config)
obs = env.reset()

# 动作空间：只需 chassis 速度控制（线性 + 角速度）
print("Action space:", env.action_space)
# base_vel: [linear_vel, angular_vel] — 2 维连续

# 观察空间：有 GPS+Compass 类传感器
print("nav goal sensor (polar):", obs["obj_start_gps_compass"])
# [distance, angle] — 目标物体相对机器人底座的极坐标

# 简单控制：以固定速度向目标移动
for step in range(200):
    dist, angle = obs["obj_start_gps_compass"]
    # 简单策略：转向目标，然后前进
    if abs(angle) > 0.2:
        action = {"base_vel": np.array([0.0, np.sign(angle) * 0.5])}
    else:
        action = {"base_vel": np.array([1.0, 0.0])}
    obs, reward, done, info = env.step(action)
    if done:
        break

env.close()
```

| 对比维度 | PointNav | NavToObj |
| --- | --- | --- |
| 导航目标 | 3D 坐标点 | 物体 / 接收器 |
| 动作空间 | 离散（4 动作） | 连续速度（base_vel） |
| 模拟器 | HabitatSim | RearrangeSim |
| 物理引擎 | 关闭 | 开启 |
| 智能体 | 无形态点 | Fetch robot 底盘 |

##  案例 5：关节物体 — 开关抽屉与冰箱

**① 案例含义**

Habitat-Sim 支持**可动关节物体**（ArticulatedObject）——抽屉、柜门、冰箱门等。
操作这类物体需要一种不同的交互方式：通过 **marker**（交互标记点）来指定抓取位置，
然后以 **关节角度** 为目标进行控制。

```
import habitat

# 开抽屉任务
config = habitat.get_config("benchmark/rearrange/open_cab.yaml")
env = habitat.Env(config=config)
obs = env.reset()

print("Articulated object task sensors:")
for k, v in obs.items():
    print(f"  {k:30s} shape={v.shape}")

# 关节物体特有的组件：
# - marker: 手柄/拉手位置（用于指定抓取点）
# - joint_state: 当前关节开合角度
# - target_joint_state: 目标关节角度（全开/全关）

env.close()

print("\n=== 可用的关节物体任务 ===")
print("  open_cab.yaml    — 开柜门")
print("  close_cab.yaml   — 关柜门")
print("  open_fridge.yaml — 开冰箱")
print("  close_fridge.yaml— 关冰箱")
```

**⑤ 输出含义**

关节物体任务的 **核心指标** 是关节角度与目标角度的差值。

例如 OpenDrawer：目标角度 = 0.45 rad（全开），初始角度 = 0.0 rad（全关）。

Agent 需要抓取把手（marker），施加力拉开抽屉，直到达到目标角度。

关节类型有：prismatic（滑动，如抽屉）和 revolute（旋转，如冰箱门）。

**⑥ 可调参数**

| 调整项 | 怎么改 | 预期看到什么 |
| --- | --- | --- |
| 目标关节角度 | 修改 task config 中的 `target_joint_state` | 部分开合 vs 全开全合 |
| 力阈值 | 修改 `force_terminate.max_accum_force` | 更早/更晚因力过大而终止 |
| 任务类型 | 切换 `open_cab` → `open_fridge` | 不同的关节物体形态和交互方式 |

##  案例 6：PDDL 复合任务 — 多阶段家居操作

**① 案例含义**

**PDDL**（Planning Domain Definition Language）是一种符号化任务规划语言。
在 Habitat 中，一个"收拾桌子"的任务会被分解为：

`nav(碗) → pick(碗) → nav(桌子) → place(碗, 桌子) → nav(杯子) → ...`

高层用 PDDL 规划，低层用 RL/脚本执行每个原子动作——这就是 HRL（Hierarchical RL）的核心思想。

```
import habitat

# 简单复合任务（有预定义 solution）
config = habitat.get_config("benchmark/rearrange/rearrange_easy.yaml")

with habitat.config.read_write(config):
    config.habitat.environment.max_episode_steps = 500

env = habitat.Env(config=config)
obs = env.reset()

print("Composite task PDDL predicates:")
# all_predicates 传感器告诉你当前所有 PDDL 谓词的真值
if "all_predicates" in obs:
    print(obs["all_predicates"])

env.close()
```

### PDDL Domain 定义示例

```
# 来自 config/habitat/task/rearrange/pddl/rearrange_easy.yaml
# 定义场景中有什么、目标是什么、怎么做

objects:            # 场景实体
  - name: goal0|0        # 要移动的物体
    expr_type: movable_entity_type
  - name: TARGET_goal0|0  # 目标位置（接收器）
    expr_type: goal_entity_type
  - name: robot_0         # 机器人自己
    expr_type: robot_entity_type

goal:               # 最终目标：物体在目标位置 AND 机器人不持物
  expr_type: AND
  sub_exprs:
    - at(goal0|0, TARGET_goal0|0)
    - not_holding(robot_0)

solution:           # 预定义的执行计划（easy mode）
  - nav(goal0|0, robot_0)          # 1. 导航到物体
  - pick(goal0|0, robot_0)         # 2. 抓取
  - nav(TARGET_goal0|0, robot_0)  # 3. 导航到目标
  - place(goal0|0, TARGET_goal0|0, robot_0) # 4. 放置
```

| PDDL 元素 | 角色 | 例子 |
| --- | --- | --- |
| **Entity** | 场景中的对象 | goal0|0（物）、TARGET_goal0|0（位置）、robot_0（机器人） |
| **Predicate** | 描述世界状态的真/假断言 | `at(goal0|0, TARGET)`, `holding(robot_0)`, `not_holding(robot_0)` |
| **Goal** | 目标状态（谓词的逻辑组合） | `AND(at(...), not_holding(...))` |
| **Solution** | 到达目标的动作序列 | `nav → pick → nav → place` |
| **Action** | 可执行的原子动作 | `nav(entity, robot)`, `pick(entity, robot)` |

### 可用复合任务

| Benchmark Config | 任务描述 | 物体数 |
| --- | --- | --- |
| `rearrange_easy.yaml` | 单个物体：抓取→搬运→放置 | 1 |
| `rearrange.yaml` | 同上但无预定义 solution（需要 planner） | 1 |
| `set_table.yaml` | 摆桌子：多个物体→多个位置 | 3-5 |
| `tidy_house.yaml` | 整理房间：物体归位 | 3-5 |
| `prepare_groceries.yaml` | 准备食材：多物体→不同接收器 | 3-5 |

##  学后自检 — 你掌握了什么

#### Q1：Rearrange 和 Navigation 的核心区别是什么？

Navigation 是"走到点"，Rearrange 是"改变世界状态"。后者需要物理引擎、机器人 URDF、关节手臂控制和物体交互（抓取/放置）。Sim 类型从 HabitatSim-v0 切换为 RearrangeSim-v0。

#### Q2：Pick 任务中的 is_holding=1 意味着什么？

吸盘已成功吸住目标物体。这是 pick_reward 的峰值信号，也是 pick_success 的判断依据。此后物体会跟随机械臂末端执行器运动。

#### Q3：PDDL 中的 solution 字段是做什么的？

预定义的动作序列（nav→pick→nav→place）。在"easy"模式下，CompositeTask 按 solution 顺序执行每个原子动作。在"hard"模式下需要运行时 planner。

#### Q4：为什么不直接在 PointNav 的 Env 里加一个"抓取"动作？

因为操作任务需要物理仿真、碰撞检测、抓取约束、关节限制——这些都需要 Bullet 物理引擎和完整的 URDF 机器人模型，不是在一个离散动作空间里加一个 action_id 能实现的。

#### Q5：Rearrange 的数据集需要手动下载吗？

不需要。RearrangeDatasetV0 的 __init__ 方法会自动调用 datasets_download --uids rearrange_task_assets，首次运行时会自动完成。

[← 第8章：真机部署](habitat-textbook-step8.html)
[回到学习中心 →](index.html)
