# 第3章：读核心代码 — Habitat 从零理解

> 以运行时逻辑为主线，模块化探索 env.step() 从用户代码到 C++ 引擎的完整旅程。 每个模块可独立展开，每个参数可实时调整观察效果。

<div class="section-title">

模块全景：6 个模块，一条调用链

</div>

点击任一模块跳转到详细代码分析。模块按 **运行时调用顺序** 排列。

<div class="arch-map">

<div class="arch-node" style="border-top: 3px solid var(--accent-config);">

<span class="arch-icon">📋</span> <span class="arch-name">注册中心</span> <span class="arch-file">core/registry.py</span> <span class="arch-role">全局字典 · 装饰器模式  
管理所有可插拔组件</span>

</div>

<div class="arch-node" style="border-top: 3px solid var(--accent-data);">

<span class="arch-icon">📦</span> <span class="arch-name">数据层</span> <span class="arch-file">core/dataset.py</span> <span class="arch-role">Episode · 场景+起点+目标  
每次任务实例的元数据</span>

</div>

<div class="arch-node" style="border-top: 3px solid var(--accent-sim);">

<span class="arch-icon">🎥</span> <span class="arch-name">模拟器层</span> <span class="arch-file">core/simulator.py</span> <span class="arch-role">Sensor · Simulator 抽象  
定义统一接口</span>

</div>

<div class="arch-node" style="border-top: 3px solid var(--accent-task);">

<span class="arch-icon">🎯</span> <span class="arch-name">任务系统</span> <span class="arch-file">core/embodied\_task.py</span> <span class="arch-role">Action · Measure · Task  
连接 Sim 和 Dataset</span>

</div>

<div class="arch-node" style="border-top: 3px solid var(--accent-core);">

<span class="arch-icon">🌐</span> <span class="arch-name">环境入口</span> <span class="arch-file">core/env.py</span> <span class="arch-role">Env · RLEnv  
顶层 reset/step 接口</span>

</div>

<div class="arch-node" style="border-top: 3px solid var(--accent-rl);">

<span class="arch-icon">🧭</span> <span class="arch-name">导航实现</span> <span class="arch-file">tasks/nav/nav.py</span> <span class="arch-role">NavigationTask · 6动作  
10+传感器 · 8评估指标</span>

> 💡
> 
> <div class="tip-title">
> 
> 💡 推荐阅读顺序
> 
> 如果你是第一次读：**注册中心 → 环境入口 → 任务系统 → 导航实现 → 模拟器层 → 数据层**  
> 这个顺序从"框架怎么找到组件"开始，逐步深入到"一次 step 调用穿过了什么"，最后回到"数据从哪来"。
> 
> <div class="section">
> 
> <div class="container">
> 
> <div class="section-title">
> 
> 调用链追踪器：一次 `env.step("move_forward")` 的完整旅程
> 
> </div>
> 
> 点击每一步展开源码细节。这是整个框架的 **运行时主循环**。
> 
> <div id="chainTracer" class="chain-container">
> 
> <div class="chain-node expanded">
> 
> <div class="chain-node-header">
> 
> <div class="step-num" style="background:#fbbf2430; color:#fbbf24;">
> 
> 1
> 
> </div>
> 
> <div class="step-info">
> 
> <div class="step-func">
> 
> 用户代码调用 env.step()
> 
> </div>
> 
> <div class="step-desc">
> 
> 传入动作名 "move\_forward" 或动作字典
> 
> </div>
> 
> <div class="step-file">
> 
> your\_training\_script.py
> 
> <div class="step-expand">
> 
> ▼
> 
> <div class="chain-node-body">
> 
>     # 用户代码 — 最简单的调用
>     env = Env(config, dataset)
>     env.reset()
>     for i in range(100):
>         observations = env.step("move_forward")  # ← 从这里开始
>     
>     # 也支持传字典（参数化动作）
>     observations = env.step({"action": "velocity_control",
>                                "action_args": {"linear_velocity": 0.5,
>                                               "angular_velocity": 0.0}})
> 
> <div>
> 
> **📌 动作可以怎么传？**
> 
> 支持三种形式：`"move_forward"`（字符串）、`0`（动作索引）、`{"action": "move_forward"}`（字典，可附带参数）。 在 `Env.step()` 内部，字符串和索引会被统一转换为字典。
> 
> </div>
> 
> <div class="chain-arrow">
> 
> │
> 
> </div>
> 
> <div class="chain-node expanded">
> 
> <div class="chain-node-header">
> 
> <div class="step-num" style="background:#3b82f630; color:#60a5fa;">
> 
> 2
> 
> </div>
> 
> <div class="step-info">
> 
> <div class="step-func">
> 
> Env.step() — 动作格式化 + 委派给 Task
> 
> </div>
> 
> <div class="step-desc">
> 
> 将动作统一为 dict → 调用 task.step() → 更新测量指标 → 更新步数统计
> 
> </div>
> 
> <div class="step-file">
> 
> core/env.py · 282-322 行
> 
> <div class="step-expand">
> 
> ▼
> 
> <div class="chain-node-body">
> 
>     # env.py — Env.step() 的核心逻辑
>     def step(self, action, **kwargs):
>         # ① 将字符串/数字统一转换为 {"action": "move_forward"}
>         if isinstance(action, (str, int, np.integer)):
>             action = {"action": action}
>     
>         # ② 核心：委派给 Task 执行动作
>         observations = self.task.step(
>             action=action, episode=self.current_episode
>         )
>     
>         # ③ 更新所有评估指标（Success, SPL, DistanceToGoal...）
>         self._task.measurements.update_measures(
>             episode=self.current_episode, action=action,
>             task=self.task, observations=observations
>         )
>     
>         # ④ 递增步数、检查 episode 是否结束
>         self._update_step_stats()
>     
>         return observations
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 💡 Env 的本质
> > 
> > Env 不执行动作 —— 它只做 **格式转换 + 委派 + 收尾统计**。真正的动作执行在 Task 层。
> > 
> > </div>
> > 
> > <div class="chain-arrow">
> > 
> > │
> > 
> > </div>
> > 
> > <div class="chain-node expanded">
> > 
> > <div class="chain-node-header">
> > 
> > <div class="step-num" style="background:#8b5cf630; color:#a78bfa;">
> > 
> > 3
> > 
> > </div>
> > 
> > <div class="step-info">
> > 
> > <div class="step-func">
> > 
> > EmbodiedTask.step() — 查表找到 Action 实例
> > 
> > </div>
> > 
> > <div class="step-desc">
> > 
> > 从 self.actions 字典取出 MoveForwardAction → 调用其 step() → 收集传感器观测 → 检查终止条件
> > 
> > </div>
> > 
> > <div class="step-file">
> > 
> > core/embodied\_task.py · 328-363 行
> > 
> > <div class="step-expand">
> > 
> > ▼
> > 
> > <div class="chain-node-body">
> > 
> >     # embodied_task.py — EmbodiedTask.step() 的核心逻辑
> >     def step(self, action, episode):
> >         action_name = action["action"]  # "move_forward"
> >     
> >         # ① 从 actions 字典取出 MoveForwardAction 实例
> >         task_action = self.actions[action_name]
> >     
> >         # ② 调用 Action 的 step 方法（核心！）
> >         observations = task_action.step(
> >             **action.get("action_args", {}), task=self
> >         )
> >     
> >         # ③ 推进物理仿真（重力、碰撞检测）
> >         self._sim.step_physics(1.0 / self._physics_target_sps)
> >     
> >         # ④ 收集 Task 层传感器的观测（如 PointGoal, GPS, Compass）
> >         observations.update(
> >             self.sensor_suite.get_observations(
> >                 observations=observations, episode=episode,
> >                 action=action, task=self
> >             )
> >         )
> >     
> >         # ⑤ 检查 episode 是否应该终止（如 stop 被调用）
> >         self._is_episode_active = self._check_episode_is_active(
> >             observations, action, episode
> >         )
> >         return observations
> > 
> > <div class="chain-arrow">
> > 
> > │
> > 
> > </div>
> > 
> > <div class="chain-node expanded">
> > 
> > <div class="chain-node-header">
> > 
> > <div class="step-num" style="background:#f472b630; color:#f472b6;">
> > 
> > 4
> > 
> > </div>
> > 
> > <div class="step-info">
> > 
> > <div class="step-func">
> > 
> > MoveForwardAction.step() — 翻译为模拟器指令
> > 
> > </div>
> > 
> > <div class="step-desc">
> > 
> > 一行代码：self.\_sim.step(HabitatSimActions.move\_forward)
> > 
> > </div>
> > 
> > <div class="step-file">
> > 
> > tasks/nav/nav.py · 1061-1069 行
> > 
> > <div class="step-expand">
> > 
> > ▼
> > 
> > <div class="chain-node-body">
> > 
> >     # nav.py — MoveForwardAction：整个框架最简洁的 Action
> >     @registry.register_task_action
> >     class MoveForwardAction(SimulatorTaskAction):
> >         name: str = "move_forward"
> >     
> >         def step(self, *args, **kwargs):
> >             return self._sim.step(HabitatSimActions.move_forward)
> >     
> >     # 对比：StopAction 不调用 sim.step，只设置标志位
> >     @registry.register_task_action
> >     class StopAction(SimulatorTaskAction):
> >         name: str = "stop"
> >     
> >         def step(self, task, *args, **kwargs):
> >             task.is_stop_called = True  # 只设标志，不移动
> > 
> > <div>
> > 
> > **📌 Action 的两类实现**
> > 
> > **运动类 Action**（MoveForward, TurnLeft, TurnRight）→ 调用 `sim.step(动作枚举)`  
> > **状态类 Action**（Stop, VelocityAction）→ 设置 Task 属性或操作模拟器内部状态
> > 
> > </div>
> > 
> > <div class="chain-arrow">
> > 
> > │
> > 
> > </div>
> > 
> > <div class="chain-node expanded">
> > 
> > <div class="chain-node-header">
> > 
> > <div class="step-num" style="background:#10b98130; color:#34d399;">
> > 
> > 5
> > 
> > </div>
> > 
> > <div class="step-info">
> > 
> > <div class="step-func">
> > 
> > HabitatSim.step() — Python → C++ 引擎
> > 
> > </div>
> > 
> > <div class="step-desc">
> > 
> > 将动作枚举传给 C++ 引擎：更新 Agent 位姿 → 渲染新帧 → 返回 rgb/depth 等观测
> > 
> > </div>
> > 
> > <div class="step-file">
> > 
> > sims/habitat\_simulator/habitat\_simulator.py
> > 
> > <div class="step-expand">
> > 
> > ▼
> > 
> > <div class="chain-node-body">
> > 
> >     # habitat_simulator.py — HabitatSim 封装 C++ 引擎
> >     # 动作枚举 → C++ 引擎
> >     class HabitatSimActions:
> >         move_forward = 0   # 前进 0.25m（沿 -Z 轴）
> >         turn_left    = 1   # 左转 10°
> >         turn_right   = 2   # 右转 10°
> >         stop         = 3   # 停止
> >     
> >     # C++ 引擎做的事（Python 层不可见）：
> >     # ① agent.act("move_forward") → 更新 position/rotation
> >     # ② 碰撞检测 → 如果撞墙，回弹到最近的可导航点
> >     # ③ 渲染管线 → 从 agent 视角生成 RGB / Depth / Semantic
> >     # ④ 返回 {"rgb": np.array(H,W,3), "depth": np.array(H,W,1), ...}
> > 
> > <div class="chain-arrow">
> > 
> > │
> > 
> > </div>
> > 
> > <div class="chain-node expanded">
> > 
> > <div class="chain-node-header">
> > 
> > <div class="step-num" style="background:#06b6d430; color:#22d3ee;">
> > 
> > 6
> > 
> > </div>
> > 
> > <div class="step-info">
> > 
> > <div class="step-func">
> > 
> > 返回路径：逐层回传 Observations
> > 
> > </div>
> > 
> > <div class="step-desc">
> > 
> > C++ → Sim → Action → Task（合并传感器） → Env（更新指标） → 用户代码
> > 
> > </div>
> > 
> > <div class="step-file">
> > 
> > 沿调用栈反向传播
> > 
> > <div class="step-expand">
> > 
> > ▼
> > 
> > <div class="chain-node-body">
> > 
> >     # 返回路径中的关键操作：
> >     
> >     # 4→3: Task.step() 在 action 返回后追加 Task 传感器
> >     observations.update(
> >         self.sensor_suite.get_observations(...)  # 追加 pointgoal/gps/compass
> >     )
> >     
> >     # 3→2: Env.step() 在 task 返回后更新所有 Measure
> >     self._task.measurements.update_measures(
> >         episode, action, task, observations
> >     )  # 每个 measure 计算一次：Success? SPL? DistanceToGoal?
> >     
> >     # 最终用户拿到的 observations 包含：
> >     # {"rgb": (H,W,3), "depth": (H,W,1),           ← Sim 传感器
> >     #  "pointgoal_with_gps_compass": (2,),          ← Task 传感器
> >     #  "compass": (1,), "gps": (2,)}                ← Task 传感器
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > <div class="section-title">
> > 
> > 参数调控台：改动一个参数，观察全局影响
> > 
> > </div>
> > 
> > 调整下方参数，观察不同模块的输出如何变化。理解参数如何沿调用链传播。
> > 
> > <div class="param-grid">
> > 
> > <div class="param-controls">
> > 
> > ### 🎛️ 调整参数
> > 
> > <div class="param-row">
> > 
> > RGB 分辨率 256×256 (默认) 128×128 (低) 512×512 (高) 1024×1024 (极高)
> > 
> > </div>
> > 
> > <div class="param-row">
> > 
> > HFOV (水平视场角) 90° (默认) 60° (窄) 120° (广角)
> > 
> > </div>
> > 
> > <div class="param-row">
> > 
> > 动作空间 4 动作 (默认: MF+TL+TR+Stop) 2 动作 (MF+TL) 1 动作 (仅 Forward) 6 动作 (+LookUp+LookDown)
> > 
> > </div>
> > 
> > <div class="param-row">
> > 
> > 传感器组合 RGB + Depth (默认) 仅 RGB RGB + Depth + GPS+Compass 全部传感器
> > 
> > </div>
> > 
> > <div class="param-row">
> > 
> > success\_distance 0.1m (默认 / 严格) 0.5m (宽松) 1.0m (很宽松)
> > 
> > </div>
> > 
> > <div class="param-row">
> > 
> > max\_episode\_steps 500 步 (默认) 100 步 (短) 1000 步 (长)
> > 
> > <div id="param-effect-panel" class="param-effect">
> > 
> > ### 📊 影响分析
> > 
> > 下方展示每个参数**当前值**对各个模块的影响。改动参数后对应条目会**高亮闪烁**。
> > 
> > <div id="effect-content">
> > 
> > <div class="effect-item" style="border-left-color:#3b82f6;">
> > 
> > <div class="effect-label" style="color:#3b82f6;">
> > 
> > 📷 RGB 分辨率
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`(256, 256, 3)` <span style="font-size:0.7rem;color:#64748b;">\~192 KB / 实时</span>
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 默认配置，观测和计算量平衡。影响 `Sensor._get_observation_space()` 返回的 Box shape。
> > 
> > <div class="effect-item" style="border-left-color:#06b6d4;">
> > 
> > <div class="effect-label" style="color:#06b6d4;">
> > 
> > 🔭 水平视场角
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`90°`
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 标准人眼视场。配置位于 `simulator.agents.main_agent.sim_sensors.rgb.hfov`。
> > 
> > <div class="effect-item" style="border-left-color:#f59e0b;">
> > 
> > <div class="effect-label" style="color:#f59e0b;">
> > 
> > 🎮 动作空间
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`{move_forward, turn_left, turn_right, stop}`
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 标准离散动作空间。由 `EmbodiedTask._init_entities()` 从 registry 实例化对应 Action 类。
> > 
> > <div class="effect-item" style="border-left-color:#8b5cf6;">
> > 
> > <div class="effect-label" style="color:#8b5cf6;">
> > 
> > 📡 传感器组合
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`{rgb, depth}`
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 标准组合。最终 `Observations` dict 由 Sim sensors + Task sensors 合并而成。
> > 
> > <div class="effect-item" style="border-left-color:#10b981;">
> > 
> > <div class="effect-label" style="color:#10b981;">
> > 
> > 🎯 success\_distance
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`≤ 0.1m`
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 严格阈值。在 `Success.update_metric()` 中判断 **stop 时距离 \< 阈值** 才记为成功。
> > 
> > <div class="effect-item" style="border-left-color:#ec4899;">
> > 
> > <div class="effect-label" style="color:#ec4899;">
> > 
> > ⏱️ max\_episode\_steps
> > 
> > </div>
> > 
> > <div style="margin-top:4px;">
> > 
> > **当前值：**`500 步`
> > 
> > </div>
> > 
> > <div style="margin-top:6px;font-size:0.82rem;line-height:1.6;color:var(--text-dim);">
> > 
> > 标准配置。在 `Env._past_limit()` 中检查，超限则 `episode_over = True`。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > <div class="section-title">
> > 
> > 模块化代码分析
> > 
> > </div>
> > 
> > 6 个模块，每个独立展开。按运行时调用顺序排列，可跳读。
> > 
> > <div id="moduleTabs" class="tab-bar">
> > 
> > <span class="tab-dot" style="background:var(--accent-config);"></span> 注册中心
> > 
> > <span class="tab-dot" style="background:var(--accent-data);"></span> 数据层
> > 
> > <span class="tab-dot" style="background:var(--accent-sim);"></span> 模拟器层
> > 
> > <span class="tab-dot" style="background:var(--accent-task);"></span> 任务系统
> > 
> > <span class="tab-dot" style="background:var(--accent-core);"></span> 环境入口
> > 
> > <span class="tab-dot" style="background:var(--accent-rl);"></span> 导航实现
> > 
> > </div>
> > 
> > <div id="tab-registry" class="tab-panel active">
> > 
> > <div class="file-tree">
> > 
> > <span class="dir">habitat-lab/habitat/core/</span> <span class="file">└── <span class="hl">registry.py</span></span> <span class="cmt">(231 行)</span>
> > 
> > </div>
> > 
> > <div class="collapsible open">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">核心数据结构：一个字典统治一切</span> <span class="badge">mapping</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     # 全局单例 — 整个框架的唯一"注册表"
> >     registry = Registry()
> >     
> >     # Registry 内部只维护一个数据结构：
> >     mapping: DefaultDict[str, dict] = {
> >         "task":        {"Nav-v0": NavigationTask, "Rearrangement-v0": ...},
> >         "task_action": {"MoveForwardAction": MoveForwardAction,
> >                          "TurnLeftAction": TurnLeftAction, ...},
> >         "sensor":      {"PointGoalSensor": PointGoalSensor,
> >                          "HeadingSensor": HeadingSensor, ...},
> >         "measure":     {"Success": Success, "SPL": SPL, ...},
> >         "sim":         {"Sim-v0": HabitatSim, ...},
> >         "dataset":     {"PointNav-v1": PointNavDatasetV1, ...},
> >         "env":         {"RLEnv-v0": RLEnv, ...},
> >     }
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">\_register\_impl：装饰器的核心</span> <span class="badge">50 行核心逻辑</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     @classmethod
> >     def _register_impl(cls, _type, to_register, name, assert_type=None):
> >         def wrap(to_register):
> >             if assert_type is not None:
> >                 assert issubclass(to_register, assert_type) # 类型检查
> >             register_name = to_register.__name__ if name is None else name
> >             cls.mapping[_type][register_name] = to_register  # ← 本质就是这一行
> >             return to_register
> >         return wrap if to_register is None else wrap(to_register)
> >     
> >     # 所有 register_* 方法都是对 _register_impl 的薄封装
> >     @classmethod
> >     def register_task(cls, to_register=None, *, name=None):
> >         return cls._register_impl("task", to_register, name, assert_type=EmbodiedTask)
> >     
> >     @classmethod
> >     def register_sensor(cls, to_register=None, *, name=None):
> >         return cls._register_impl("sensor", to_register, name, assert_type=Sensor)
> >     
> >     # ... register_measure, register_task_action, register_simulator, register_dataset, register_env
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">get 方法族：从配置字符串找到类</span> <span class="badge">6 个 getter</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     # 6 个 get 方法 — 全部从 mapping 字典取值
> >     @classmethod
> >     def get_task(cls, name):        return cls.mapping["task"].get(name, None)
> >     @classmethod
> >     def get_sensor(cls, name):      return cls.mapping["sensor"].get(name, None)
> >     @classmethod
> >     def get_measure(cls, name):     return cls.mapping["measure"].get(name, None)
> >     @classmethod
> >     def get_task_action(cls, name): return cls.mapping["task_action"].get(name, None)
> >     @classmethod
> >     def get_simulator(cls, name):   return cls.mapping["sim"].get(name, None)
> >     @classmethod
> >     def get_dataset(cls, name):     return cls.mapping["dataset"].get(name, None)
> >     
> >     # 调用流程：YAML 配置 type: "Nav-v0" → registry.get_task("Nav-v0") → mapping["task"]["Nav-v0"]
> > 
> > </div>
> > 
> > <div id="tab-dataset" class="tab-panel">
> > 
> > <div class="file-tree">
> > 
> > <span class="dir">habitat-lab/habitat/core/</span> <span class="file">└── <span class="hl">dataset.py</span></span> <span class="cmt">(547 行)</span>
> > 
> > </div>
> > 
> > <div class="collapsible open">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">Episode — 一次任务实例的完整描述</span> <span class="badge">@attr.s</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     @attr.s(auto_attribs=True)
> >     class BaseEpisode:
> >         episode_id: str   # "0", "1", ...
> >         scene_id: str     # "skokloster-castle"
> >     
> >     @attr.s(auto_attribs=True, kw_only=True)
> >     class Episode(BaseEpisode):
> >         scene_dataset_config: str         # *.scene_dataset_config.json 路径
> >         start_position: List[float]       # [x, y, z]  世界坐标
> >         start_rotation: List[float]       # [x, y, z, w] 四元数朝向
> >     
> >     @attr.s(auto_attribs=True, kw_only=True)
> >     class NavigationEpisode(Episode):
> >         goals: List[NavigationGoal]              # 每个 goal 有 position + radius
> >         shortest_paths: Optional[List]           # 预计算的最短路径
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">EpisodeIterator — 场景切换的智能调度</span> <span class="badge">性能关键</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class EpisodeIterator:
> >         # 关键参数：
> >         #   group_by_scene=True         → 同场景 episode 连续加载（减少 GPU 切换开销）
> >         #   max_scene_repeat_episodes=N → 同场景最多连续 N 个 episode（防止过拟合）
> >         #   cycle=True                  → 遍历完所有 episode 后循环
> >         #   shuffle=True                → 循环时打乱场景顺序
> >     
> >         def __next__(self):
> >             self._forced_scene_switch_if()  # 检查是否需要切换场景
> >             next_episode = next(self._iterator)
> >             if next_episode is None:
> >                 if not self.cycle:
> >                     raise StopIteration
> >                 if self.shuffle:
> >                     self._shuffle()
> >                 next_episode = next(self._iterator)
> >             return next_episode
> > 
> > </div>
> > 
> > <div id="tab-simulator" class="tab-panel">
> > 
> > <div class="file-tree">
> > 
> > <span class="dir">habitat-lab/habitat/core/</span> <span class="file">└── <span class="hl">simulator.py</span></span> <span class="cmt">(423 行)</span>
> > 
> > </div>
> > 
> > <div class="collapsible open">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">Sensor 基类：3 要素 + 1 方法</span> <span class="badge">abc.ABCMeta</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class Sensor(metaclass=abc.ABCMeta):
> >         # ── 3 个必须定义的属性 ──
> >         uuid: str                     # "rgb", "depth", "pointgoal", ...
> >         sensor_type: SensorTypes      # COLOR=1, DEPTH=2, SEMANTIC=4, PATH=5, ...
> >         observation_space: Space      # gym.Space，如 Box(low=0, high=255, shape=(H,W,3))
> >     
> >         def __init__(self, *args, **kwargs):
> >             self.config = kwargs["config"]
> >             self.uuid = self._get_uuid(*args, **kwargs)
> >             self.sensor_type = self._get_sensor_type(*args, **kwargs)
> >             self.observation_space = self._get_observation_space(*args, **kwargs)
> >     
> >         # ── 1 个必须实现的方法 ──
> >         @abc.abstractmethod
> >         def get_observation(self, *args, **kwargs) -> Any:
> >             raise NotImplementedError
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">SensorSuite — 批量采集所有传感器</span> <span class="badge">Dict\[str,Sensor\]</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class SensorSuite:
> >         sensors: Dict[str, Sensor]
> >     
> >         def get_observations(self, *args, **kwargs) -> Observations:
> >             # 遍历每个 sensor，逐一调用 .get_observation()
> >             return Observations(self.sensors, *args, **kwargs)
> >     
> >         # Observations.__init__ 内部：
> >         # data = [(uuid, sensor.get_observation(*args, **kwargs))
> >         #         for uuid, sensor in sensors.items()]
> >         # super().__init__(data)  # 变成普通 dict
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">Simulator 抽象基类 — 统一所有后端的接口</span> <span class="badge">12 个抽象方法</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class Simulator:
> >         # ── 生命周期 ──
> >         def reset(self) -> Observations       # 重置场景，返回初始观测
> >         def step(self, action) -> Observations  # 执行动作，返回新观测
> >         def reconfigure(self, config)          # 运行时切换场景/传感器
> >         def close(self)                       # 释放 3D 资源
> >     
> >         # ── 状态查询 ──
> >         def get_agent_state(self) -> AgentState    # → (position, rotation)
> >         def geodesic_distance(self, a, b) -> float  # 沿可导航区域的最短距离
> >         def is_navigable(self, point) -> bool       # 该点是否可站立
> >         def sample_navigable_point(self)           # 随机采样可站立点
> >     
> >         # ── 路径规划 ──
> >         def action_space_shortest_path(self, src, tgts)  # 动作序列最短路径
> >         def get_straight_shortest_path_points(self, a, b) # 几何路径点
> >     
> >         # ── 渲染 + 碰撞 ──
> >         def render(self, mode="rgb") -> np.ndarray
> >         def previous_step_collided(self) -> bool
> > 
> > </div>
> > 
> > <div id="tab-task" class="tab-panel">
> > 
> > <div class="file-tree">
> > 
> > <span class="dir">habitat-lab/habitat/core/</span> <span class="file">└── <span class="hl">embodied\_task.py</span></span> <span class="cmt">(404 行)</span>
> > 
> > </div>
> > 
> > <div class="collapsible open">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">EmbodiedTask — 连接 Sim 和 Dataset 的胶水</span> <span class="badge">\_\_init\_\_</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class EmbodiedTask:
> >         def __init__(self, config, sim, dataset=None):
> >             self._config = config
> >             self._sim = sim              # ← 持有模拟器引用
> >             self._dataset = dataset      # ← 持有数据集引用
> >     
> >             # 通过 _init_entities 统一创建三大组件集合：
> >             self.measurements = Measurements(
> >                 self._init_entities(config.measurements, registry.get_measure)
> >                 .values()
> >             )
> >             self.sensor_suite = SensorSuite(
> >                 self._init_entities(config.lab_sensors, registry.get_sensor)
> >                 .values()
> >             )
> >             self.actions = self._init_entities(
> >                 config.actions, registry.get_task_action
> >             )
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">\_init\_entities — 统一工厂方法</span> <span class="badge">依赖注入</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     def _init_entities(self, entities_configs, register_func):
> >         entities = OrderedDict()
> >         for entity_name, entity_cfg in entities_configs.items():
> >             # ① 从 YAML 的 type 字段查到类
> >             entity_type = register_func(entity_cfg.type)
> >             # ② 用依赖注入创建实例
> >             entities[entity_name] = entity_type(
> >                 sim=self._sim,          # 注入 Simulator
> >                 config=entity_cfg,     # 注入配置
> >                 dataset=self._dataset,  # 注入 Dataset
> >                 task=self,             # 注入 Task 自身
> >             )
> >         return entities
> > 
> > <div>
> > 
> > **📌 为什么这是手动 DI？**
> > 
> > 每个 Action/Sensor/Measure 构造时都收到 `sim=`, `config=`, `dataset=`, `task=` 四个引用。 这保证子组件可以自由访问它们需要的任何上下文，而不依赖全局变量或 import。
> > 
> > </div>
> > 
> > <div class="collapsible">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">Measure 体系 — 每步更新的评估指标</span> <span class="badge">Measure → Measurements → Metrics</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     # Measure 基类 — 3 个生命周期方法
> >     class Measure:
> >         uuid: str
> >         _metric: Any           # 当前值
> >     
> >         def reset_metric(self, episode, task, **kwargs):
> >             # 每个 episode 开始时调用
> >     
> >         def update_metric(self, episode, task, **kwargs):
> >             # 每步 step 后调用（在 Env.step 中触发）
> >     
> >         def get_metric(self):
> >             return self._metric
> > 
> > </div>
> > 
> > <div id="tab-env" class="tab-panel">
> > 
> > <div class="file-tree">
> > 
> > <span class="dir">habitat-lab/habitat/core/</span> <span class="file">└── <span class="hl">env.py</span></span> <span class="cmt">(494 行)</span>
> > 
> > </div>
> > 
> > <div class="collapsible open">
> > 
> > <div class="collapsible-header">
> > 
> > <span class="title">Env.\_\_init\_\_ — 初始化顺序决定依赖关系</span> <span class="badge">3 步初始化</span>
> > 
> > </div>
> > 
> > <div class="collapsible-body">
> > 
> >     class Env:
> >         def __init__(self, config, dataset=None):
> >             # 第1章: 加载 Dataset → 取第一个 episode → 写 scene_id 到 config
> >             self._dataset = dataset or make_dataset(config.dataset.type, config.dataset)
> >             self.current_episode = next(self.episode_iterator)
> >             config.simulator.scene = self.current_episode.scene_id
> >     
> >             # 第2章: 创建 Simulator（此时 config.simulator.scene 已就绪）
> >             self._sim = make_sim(config.simulator.type, config.simulator)
> >     
> >             # 第3章: 创建 EmbodiedTask（传入已就绪的 sim 和 dataset）
> >             self._task = make_task(config.task.type, config.task, sim=self._sim, dataset=self._dataset)
> >     
> >             # 合并 Sim + Task 的观测空间
> >             self.observation_space = spaces.Dict({
> >                 **self._sim.sensor_suite.observation_spaces.spaces,
> >                 **self._task.sensor_suite.observation_spaces.spaces,
> >             })
> >             self.action_space = self._task.action_space
> > 
> > > ⚠️
> > > 
> > > <div class="warn-title">
> > > 
> > > ⚠️ 初始化顺序不能颠倒
> > > 
> > > `make_sim` 必须先于 `make_task`，因为 Task 构造时需要传入 Sim。 同理，`config.simulator.scene` 必须在 `make_sim` 前设置好。
> > > 
> > > </div>
> > > 
> > > <div class="collapsible">
> > > 
> > > <div class="collapsible-header">
> > > 
> > > <span class="title">RLEnv — Gym 接口适配层</span> <span class="badge">gym.Env</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible-body">
> > > 
> > >     class RLEnv(gym.Env):
> > >         # 把 Env 包装成标准 Gym 接口
> > >         def reset(self):
> > >             observations = self._env.reset()
> > >             return observations
> > >     
> > >         def step(self, action):
> > >             observations = self._env.step(action)
> > >             reward = self.get_reward(observations)   # 子类实现
> > >             done = self.get_done(observations)        # 子类实现
> > >             info = self.get_info(observations)        # 子类实现
> > >             return observations, reward, done, info
> > > 
> > > </div>
> > > 
> > > <div id="tab-nav" class="tab-panel">
> > > 
> > > <div class="file-tree">
> > > 
> > > <span class="dir">habitat-lab/habitat/tasks/nav/</span> <span class="file">└── <span class="hl">nav.py</span></span> <span class="cmt">(1344 行 — 最长的核心文件)</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible open">
> > > 
> > > <div class="collapsible-header">
> > > 
> > > <span class="title">NavigationTask — 最精简的子类实现</span> <span class="badge">@registry.register\_task(name="Nav-v0")</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible-body">
> > > 
> > >     @registry.register_task(name="Nav-v0")
> > >     class NavigationTask(EmbodiedTask):
> > >         def overwrite_sim_config(self, config, episode):
> > >             # 每个 episode 开始前：把起点/朝向/场景写入 sim 配置
> > >             with read_write(config):
> > >                 config.simulator.scene = episode.scene_id
> > >                 agent_config = get_agent_config(config.simulator)
> > >                 agent_config.start_position = episode.start_position
> > >                 agent_config.start_rotation = episode.start_rotation
> > >     
> > >         def _check_episode_is_active(self, *args, **kwargs):
> > >             # 终止条件：agent 调用了 stop
> > >             return not getattr(self, "is_stop_called", False)
> > > 
> > > <div class="collapsible">
> > > 
> > > <div class="collapsible-header">
> > > 
> > > <span class="title">6 种 Action 实现对比</span> <span class="badge">SimulatorTaskAction</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible-body">
> > > 
> > > | Action              | step() 做了什么                                      | 是否调用 sim.step |
> > > | ------------------- | ------------------------------------------------ | ------------- |
> > > | `MoveForwardAction` | `self._sim.step(HabitatSimActions.move_forward)` | ✅ 前进 0.25m    |
> > > | `TurnLeftAction`    | `self._sim.step(HabitatSimActions.turn_left)`    | ✅ 左转 10°      |
> > > | `TurnRightAction`   | `self._sim.step(HabitatSimActions.turn_right)`   | ✅ 右转 10°      |
> > > | `StopAction`        | `task.is_stop_called = True`                     | ❌ 仅设标志        |
> > > | `LookUpAction`      | `self._move_camera_vertical(+tilt)`              | ❌ 相机俯仰        |
> > > | `LookDownAction`    | `self._move_camera_vertical(-tilt)`              | ❌ 相机俯仰        |
> > > | `VelocityAction`    | 积分线速度+角速度 → snap 到 navmesh                       | ❌ 直接设位姿       |
> > > | `TeleportAction`    | 直接 `set_agent_state(position, rotation)`         | ❌ 直接设位姿       |
> > > 

> > > <div class="collapsible">
> > > 
> > > <div class="collapsible-header">
> > > 
> > > <span class="title">Sensor 族谱 — 从起点到目标的观测变换</span> <span class="badge">PointGoal / GPS / Compass / Heading / Proximity</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible-body">
> > > 
> > >     # PointGoalSensor — 起点→目标 的固定相对向量（episode 全程不变）
> > >     class PointGoalSensor(Sensor):
> > >         def get_observation(self, observations, episode, **kwargs):
> > >             source_position = episode.start_position    # 固定起点
> > >             rotation_world_start = quaternion_from_coeff(episode.start_rotation)
> > >             goal_position = episode.goals[0].position  # 固定终点
> > >             return self._compute_pointgoal(source, rotation, goal)
> > >             # → 返回 (dx, dz) 或 (ρ, φ) 在 agent 坐标系中
> > >     
> > >     # PointGoalWithGPSCompassSensor — 当前位置→目标（每步变化）
> > >     class IntegratedPointGoalGPSAndCompassSensor(PointGoalSensor):
> > >         def get_observation(self, observations, episode, **kwargs):
> > >             agent_state = self._sim.get_agent_state()  # 每步查询！
> > >             agent_position = agent_state.position
> > >             goal_position = episode.goals[0].position
> > >             return self._compute_pointgoal(agent_position, agent_rotation, goal)
> > >     
> > >     # EpisodicGPSSensor — 相对于起点的位移
> > >     class EpisodicGPSSensor(Sensor):
> > >         def get_observation(self, observations, episode, **kwargs):
> > >             agent_position = self._sim.get_agent_state().position
> > >             origin = episode.start_position
> > >             return quaternion_rotate_vector(rotation_start.inv(), agent_position - origin)
> > >     
> > >     # HeadingSensor — 世界坐标系中的绝对朝向
> > >     class HeadingSensor(Sensor):
> > >         def get_observation(self, observations, episode, **kwargs):
> > >             rotation = self._sim.get_agent_state().rotation
> > >             return self._quat_to_xy_heading(rotation.inverse())
> > >     
> > >     # EpisodicCompassSensor — 相对于起点朝向的偏角
> > >     class EpisodicCompassSensor(HeadingSensor):
> > >         def get_observation(self, observations, episode, **kwargs):
> > >             rotation_agent = self._sim.get_agent_state().rotation
> > >             rotation_start = quaternion_from_coeff(episode.start_rotation)
> > >             return self._quat_to_xy_heading(rotation_agent.inverse() * rotation_start)
> > > 
> > > <div class="collapsible">
> > > 
> > > <div class="collapsible-header">
> > > 
> > > <span class="title">核心 Measure：Success + SPL 的计算逻辑</span> <span class="badge">评估核心</span>
> > > 
> > > </div>
> > > 
> > > <div class="collapsible-body">
> > > 
> > >     # Success — 两个条件必须同时满足
> > >     class Success(Measure):
> > >         def update_metric(self, episode, task, **kwargs):
> > >             distance_to_target = task.measurements["distance_to_goal"].get_metric()
> > >     
> > >             if (
> > >                 task.is_stop_called                          # ① 调用了 stop
> > >                 and distance_to_target 
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > <div class="section-title">
> > > 
> > > 文件速查表
> > > 
> > > </div>
> > > 
> > > 6 个核心文件，按运行时依赖关系排列（从上到下 = 从上层到底层）。
> > > 
> > > | 文件                      | 行数   | 关键类                                             | 在调用链中的位置                                  |
> > > | ----------------------- | ---- | ----------------------------------------------- | ----------------------------------------- |
> > > | `core/registry.py`      | 231  | Registry                                        | 框架启动时填充；运行时通过 `get_*()` 按名字查找组件           |
> > > | `core/dataset.py`       | 547  | Episode, Dataset, EpisodeIterator               | Env.\_\_init\_\_ 阶段加载；reset 时取下一个 episode |
> > > | `core/simulator.py`     | 423  | Sensor, SensorSuite, Simulator                  | 抽象层，不直接执行；HabitatSim 是实现                  |
> > > | `core/embodied_task.py` | 404  | Action, Measure, EmbodiedTask                   | env.step → task.step → action.step 的主链路   |
> > > | `core/env.py`           | 494  | Env, RLEnv                                      | 用户代码入口；串联 Sim + Task + Dataset            |
> > > | `tasks/nav/nav.py`      | 1344 | NavigationTask, 6 Action, 10+ Sensor, 8 Measure | 导航任务全链路实现；MoveForwardAction 直接驱动模拟器       |
> > > 

> > > </div>
> > > 
> > > </div>
> > > 
> > > <div class="container">
> > > 
> > > <div class="page-nav">
> > > 
> > > [← 第2章：跑通示例](habitat-textbook-step2.html) [第4章：改配置实验 →](habitat-textbook-step4.html)
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > > 
> > > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
>

</div>
