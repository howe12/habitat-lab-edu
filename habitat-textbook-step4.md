# 第4章：改配置实验 — Habitat 从零理解

> 修改 Habitat 的配置参数，观察对观测输出、传感器数据、任务指标的影响。从"读配置"到"改配置"，建立配置→效果的因果直觉。

## 0\. 本章路线图

5 个递进实验，从改分辨率到自定义传感器，循序渐进掌握配置体系。

<div class="flow-box">

<div class="flow-step">

<div class="step-tag">

实验 4-1

</div>

<div class="step-name">

改 RGB 分辨率

</div>

<div class="step-desc">

观察内存与画质变化 <span class="flow-arrow">→</span>

<div class="flow-step">

<div class="step-tag">

实验 4-2

</div>

<div class="step-name">

切换传感器组合

</div>

<div class="step-desc">

理解 sim vs lab sensors <span class="flow-arrow">→</span>

<div class="flow-step">

<div class="step-tag">

实验 4-3

</div>

<div class="step-name">

注册自定义传感器

</div>

<div class="step-desc">

LiDAR 传感器实战 <span class="flow-arrow">→</span>

<div class="flow-step">

<div class="step-tag">

实验 4-4

</div>

<div class="step-name">

自定义 YAML 配置

</div>

<div class="step-desc">

创建自己的 Benchmark <span class="flow-arrow">→</span>

<div class="flow-step">

<div class="step-tag">

实验 4-5

</div>

<div class="step-name">

对比 success\_distance

</div>

<div class="step-desc">

理解指标对训练的影响

</div>

<div>

**💡 前置知识**

本章假设你已理解： **(1)** 第3章中的参数模型（摄像头、动作、传感器）；  
**(2)** Hydra 的 `defaults:` 配置继承机制；  
**(3)** `habitat.config.read_write()` 上下文管理器的用法。

## 实验 4-1：修改 RGB 分辨率

修改 `rgb_sensor` 的宽度和高度，观察观测张量 shape 和内存占用的变化。

<div class="exp-card" style="border-left-color:#3b82f6;">

### 📐 实验设置

对比 128×128、256×256、512×512 三种分辨率下 RGB 和 Depth 观测的变化。

    # 修改配置的核心代码
    with habitat.config.read_write(cfg):
        cfg.habitat.simulator.agents.main_agent.sim_sensors.rgb_sensor.width = 128
        cfg.habitat.simulator.agents.main_agent.sim_sensors.rgb_sensor.height = 128
        cfg.habitat.simulator.agents.main_agent.sim_sensors.depth_sensor.width = 128
        cfg.habitat.simulator.agents.main_agent.sim_sensors.depth_sensor.height = 128

📊 运行结果：

<div class="exp-result">

<span class="label">128x128</span>: rgb=<span class="num">(128, 128, 3)</span>, depth=<span class="num">(128, 128, 1)</span>, memory≈<span class="num">48 KB</span> <span class="label">256x256</span>: rgb=<span class="num">(256, 256, 3)</span>, depth=<span class="num">(256, 256, 1)</span>, memory≈<span class="num">192 KB</span> <span class="label">512x512</span>: rgb=<span class="num">(512, 512, 3)</span>, depth=<span class="num">(512, 512, 1)</span>, memory≈<span class="num">768 KB</span>

### 📸 实际截图对比

<div class="screenshot-row">

<div class="screenshot-card">

![128x128 RGB](step4_outputs/4-1_rgb_128x128.png)

<div class="caption">

128×128 — 48 KB

<div class="screenshot-card">

![256x256 RGB](step4_outputs/4-1_rgb_256x256.png)

<div class="caption">

256×256 — 192 KB (默认)

<div class="screenshot-card">

![512x512 RGB](step4_outputs/4-1_rgb_512x512.png)

<div class="caption">

512×512 — 768 KB

</div>

<div class="key-finding">

<span class="icon">💡</span>

<div>

**关键发现：**分辨率每翻倍（128→256→512），RGB 内存占用变为 **4 倍**（宽×高×3通道）。 深度图为 1 通道，占用为 RGB 的 1/3。**工程权衡：**高分辨率提供更清晰视觉，但显著增加 GPU 显存和 I/O 开销。 训练时常用 128×128 或 256×256 以平衡精度与效率。

</div>

## 实验 4-2：切换传感器组合

区分 `sim_sensors`（模拟器级物理传感器）和 `lab_sensors`（任务级逻辑传感器）。

<div class="exp-card" style="border-left-color:#06b6d4;">

### 🔬 两个传感器层级

默认配置加载了 RGB + Depth 作为 sim\_sensors，PointGoalWithGPSCompass 作为 lab\_sensor。

<div class="exp-result">

<span class="label">默认 (RGB + Depth):</span> 观测 keys = \[<span class="str">'rgb'</span>, <span class="str">'depth'</span>, <span class="str">'pointgoal\_with\_gps\_compass'</span>\] rgb: shape=<span class="num">(256, 256, 3)</span> depth: shape=<span class="num">(256, 256, 1)</span> pointgoal\_with\_gps\_compass: shape=<span class="num">(2,)</span> <span class="label">仅 RGB (移除 Depth):</span> 观测 keys = \[<span class="str">'rgb'</span>, <span class="str">'pointgoal\_with\_gps\_compass'</span>\]

</div>

### 📸 实际观测截图对比

<div class="screenshot-row">

<div class="screenshot-card">

![RGB Default](step4_outputs/4-2_rgb_default.png)

<div class="caption">

RGB (默认 256×256)

<div class="screenshot-card">

![Depth Colorized](step4_outputs/4-2_depth_colorized.png)

<div class="caption">

Depth 热力图 (INFERNO)

<div class="screenshot-card">

![RGB Only](step4_outputs/4-2_rgb_only.png)

<div class="caption">

仅 RGB (移除 Depth)

<div class="module-grid" style="margin-top:18px;">

<div class="module" style="border-left-color:#06b6d4;">

### 🎮 sim\_sensors

Simulator 级别的传感器，直接挂载在 Agent 身上，由渲染引擎驱动。

  - `rgb_sensor` — RGB 相机
  - `depth_sensor` — 深度相机
  - `semantic_sensor` — 语义分割
  - 控制分辨率、HFOV、位置偏移
  - 可添加/移除来改变观测内容

</div>

<div class="module" style="border-left-color:#8b5cf6;">

### 🧠 lab\_sensors

Task 级别的传感器，与具体任务绑定，提供任务相关的高级信息。

  - `pointgoal_with_gps_compass` — 目标方向+距离
  - `heading_sensor` — 朝向角
  - `gps_sensor` — 绝对坐标
  - 可通过注册机制扩展
  - 不依赖渲染，计算量小

<div class="key-finding">

<span class="icon">💡</span>

<div>

**关键发现：**`sim_sensors` 和 `lab_sensors` 是两个独立的配置路径。 sim\_sensors 的添加/移除直接影响 GPU 渲染负载；lab\_sensors 则几乎零开销。 设计自定义任务时，应优先考虑用 lab\_sensors 提供任务信息。

</div>

## 实验 4-3：注册自定义传感器

通过 `@registry.register_sensor` 注册一个自定义 LiDAR 传感器，理解 Sensor 基类接口。

<div class="exp-card" style="border-left-color:#10b981;">

### 🛰️ SimpleLidarSensor — 8 方向射线 LiDAR

继承 `Sensor` 基类，实现 5 个接口方法，使用 `habitat_sim.geo.Ray` 做射线检测。

    # 注册自定义传感器 — 只需一个装饰器
    @registry.register_sensor(name="SimpleLidarSensor")
    class SimpleLidarSensor(Sensor):
        """模拟 LiDAR：返回 8 个方向的射线距离"""
        cls_uuid: str = "simple_lidar"
    
        def __init__(self, sim, config, *args, **kwargs):
            self._sim = sim
            self._num_rays = getattr(config, 'num_rays', 8)
            self._max_range = getattr(config, 'max_range', 5.0)
            super().__init__(config=config)
    
        def _get_uuid(self, *args, **kwargs):
            return self.cls_uuid
    
        def _get_sensor_type(self, *args, **kwargs):
            return SensorTypes.TACTILE
    
        def _get_observation_space(self, *args, **kwargs):
            return spaces.Box(low=0.0, high=self._max_range,
                              shape=(self._num_rays,), dtype=np.float32)
    
        def get_observation(self, observations, episode, *args, **kwargs):
            pos = self._sim.get_agent_state().position
            for i, angle in enumerate(np.linspace(0, 2*np.pi, self._num_rays)):
                ray = habitat_sim.geo.Ray()
                ray.origin = pos
                ray.direction = np.array([np.cos(angle), 0, np.sin(angle)])
                result = self._sim.cast_ray(ray)
                if result.has_hits():
                    distances[i] = result.hits[0].ray_distance
            return distances

✅ 注册验证 & 输出测试：

<div class="exp-result">

<span class="label">registry.get\_sensor('SimpleLidarSensor')</span> → \<class SimpleLidarSensor\> <span class="label">UUID:</span> simple\_lidar <span class="label">观测空间:</span> Box(<span class="num">0.0</span>, <span class="num">5.0</span>, (<span class="num">8</span>,), float32) <span class="label">LiDAR 输出:</span> \[<span class="num">5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0</span>\] <span class="cmt">← 开放空间，无遮挡</span>

</div>

> 💡
> 
> <div class="tip-title">
> 
> 💡 在 YAML 中使用自定义传感器
> 
> 将以下配置添加到你的 Benchmark YAML 中：  
> `            habitat:             task:               lab_sensors:                 simple_lidar:                   type: SimpleLidarSensor                   num_rays: 8                   max_range: 5.0          `
> 
> </div>
> 
> ### 📸 LiDAR 可视化结果
> 
> <div class="screenshot-row" style="grid-template-columns:1fr;">
> 
> <div class="screenshot-card">
> 
> ![LiDAR Visualization](step4_outputs/4-3_lidar_visualization.png)
> 
> <div class="caption">
> 
> 左：极坐标 LiDAR 16射线距离图 · 右：RGB 观测上下文（skokloster-castle 场景）
> 
> <div class="key-finding">
> 
> <span class="icon">💡</span>
> 
> <div>
> 
> **关键发现：**Sensorn 接口只需实现 5 个方法：`_get_uuid`、`_get_sensor_type`、 `_get_observation_space`、`get_observation`（以及可选的 `__init__`）。 通过 `@registry.register_sensor` 装饰器即可将传感器注册到全局注册表， Habitat 的 SensorSuite 会自动管理其生命周期。
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 实验 4-4：创建自定义 Benchmark 配置
> 
> 从零编写一个 YAML 配置文件，理解 Hydra 配置继承和 `_self_` 覆盖机制。
> 
> <div class="exp-card" style="border-left-color:#ec4899;">
> 
> ### 📝 my\_custom\_pointnav.yaml
> 
> 降低分辨率到 128×128、减少步数到 200、放宽成功距离到 0.5m。
> 
> <div class="config-tree">
> 
> <span class="cmt">\# @package \_global\_</span> <span class="cmt">\# 自定义 PointNav 配置 — 降低分辨率 + 减少步数 + 放宽成功条件</span> <span class="kw">defaults:</span> - /benchmark/nav/pointnav: pointnav\_base <span class="cmt">← 继承基础任务结构</span> - /habitat/dataset/pointnav: habitat\_test <span class="cmt">← 使用 habitat-test 数据集</span> - <span class="warn">\_self\_</span> <span class="cmt">← 让下方配置覆盖上方（关键！）</span> <span class="key">habitat:</span> <span class="key">environment:</span> <span class="key">max\_episode\_steps:</span> <span class="num">200</span> <span class="cmt">← 原默认 500</span> <span class="key">simulator:</span> <span class="key">agents:</span> <span class="key">main\_agent:</span> <span class="key">sim\_sensors:</span> <span class="key">rgb\_sensor:</span> <span class="key">width:</span> <span class="num">128</span> <span class="cmt">← 原 256</span> <span class="key">height:</span> <span class="num">128</span> <span class="key">depth\_sensor:</span> <span class="key">width:</span> <span class="num">128</span> <span class="key">height:</span> <span class="num">128</span> <span class="key">task:</span> <span class="key">measurements:</span> <span class="key">success:</span> <span class="key">success\_distance:</span> <span class="num">0.5</span> <span class="cmt">← 原 0.1</span>
> 
> </div>
> 
> ✅ 配置验证通过：
> 
> <div class="exp-result">
> 
> <span class="label">加载方式:</span> cfg = get\_config(<span class="str">'step4\_outputs/my\_custom\_pointnav.yaml'</span>) <span class="label">分辨率:</span> <span class="num">128</span>x<span class="num">128</span> <span class="label">max\_episode\_steps:</span> <span class="num">200</span> <span class="label">success\_distance:</span> <span class="num">0.5</span>
> 
> </div>
> 
> ### 📸 默认 vs 自定义配置对比
> 
> <div class="screenshot-row" style="grid-template-columns:1fr;">
> 
> <div class="screenshot-card">
> 
> ![Config Comparison](step4_outputs/4-4_config_comparison.png)
> 
> <div class="caption">
> 
> 各项参数改动一目了然：分辨率↓ / 步数↓ / 成功距离↑
> 
> ### 配置解析顺序
> 
> <div class="flow-box">
> 
> <div class="flow-step">
> 
> <div class="step-tag">
> 
> 第1层
> 
> </div>
> 
> <div class="step-name">
> 
> pointnav\_base
> 
> </div>
> 
> <div class="step-desc">
> 
> 定义所有默认值 <span class="flow-arrow">→</span>
> 
> <div class="flow-step">
> 
> <div class="step-tag">
> 
> 第2层
> 
> </div>
> 
> <div class="step-name">
> 
> habitat\_test
> 
> </div>
> 
> <div class="step-desc">
> 
> 覆盖数据集路径 <span class="flow-arrow">→</span>
> 
> <div class="flow-step" style="border:2px solid #f59e0b;">
> 
> <div class="step-tag" style="color:#fbbf24;">
> 
> 第3层 \_self\_
> 
> </div>
> 
> <div class="step-name">
> 
> 你的覆盖值
> 
> </div>
> 
> <div class="step-desc">
> 
> 最终生效的配置
> 
> </div>
> 
> <div>
> 
> **💡 `_self_` 的作用**
> 
> Hydra 的 `defaults:` 列表中，**后面的配置覆盖前面的**。`_self_` 代表"当前文件自身的配置值"， 把它放在最后意味着当前文件中定义的参数会覆盖 `defaults:` 中所有继承配置的对应值。
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 实验 4-5：对比 success\_distance 阈值
> 
> 修改 `success_distance` 参数，观察对评测指标（成功率）的影响。这是连接"配置"与"训练"的桥梁。
> 
> <div class="exp-card" style="border-left-color:#f59e0b;">
> 
> ### 📊 同一 Agent，不同阈值下的表现
> 
> 使用一个固定的简单 Agent（每 5 步前进一次，偶尔转弯），在 10 个 episode 上评估不同 success\_distance 阈值。
> 
> | 阈值设置             | 平均终点距离 | 成功率 | 含义                        |
> | ---------------- | ------ | --- | ------------------------- |
> | **严格 0.1m** (默认) | 9.01m  | 0%  | Agent 必须精确站在目标 0.1m 内才算成功 |
> | **中等 0.2m**      | 9.01m  | 0%  | 稍微放宽，但仍要求较高精度             |
> | **宽松 0.5m**      | 9.01m  | 0%  | Agent 在目标半米范围内即算成功        |
> | **极宽 1.0m**      | 9.01m  | 0%  | 只需大致在目标附近即可判定成功           |
> 

>     # 修改 success_distance 的方法
>     with habitat.config.read_write(cfg):
>         cfg.habitat.task.measurements.success.success_distance = 0.5  # 从 0.1 改为 0.5
> 
> ### 📸 实验结果图表
> 
> <div class="screenshot-row" style="grid-template-columns:1fr;">
> 
> <div class="screenshot-card">
> 
> ![Success Distance Chart](step4_outputs/4-5_success_distance_chart.png)
> 
> <div class="caption">
> 
> 4 种阈值的成功率对比（简单 Agent，10 episodes，max\_steps=100）
> 
> </div>
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 📖 解读
> > 
> > 本实验中成功率全为 0% 是因为简单 Agent 没有导航能力，终点距离始终 \~9m。 这恰恰说明了 **success\_distance 的影响机制**：它只在 Agent **最终位置接近目标时** 起作用。 对于能导航到目标附近的 Agent，更宽松的 success\_distance 会显著提高成功率。 常见实践：**训练初期用宽松值（0.5m）加速收敛，后期收紧（0.1m）提升精度**。
> > 
> > <div class="key-finding">
> > 
> > <span class="icon">💡</span>
> > 
> > <div>
> > 
> > **关键发现：**`success_distance` 是 **评测指标** 而非 **训练信号**。 修改它不改变 Agent 的行为，只改变"什么算成功"的定义。 训练时通常用 `distance_to_goal` 作为 reward 信号，`success_distance` 仅用于评估。 在 RL 训练中，设置合理的 success\_distance 对奖励稀疏程度有直接影响。
> > 
> > </div>
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 实验 4-6：语义传感器实操
> > 
> > 加载 Semantic Sensor，理解每个像素值的含义，用 semantic\_annotations() 查询物体名称。
> > 
> > <div>
> > 
> > **Semantic 传感器原理**
> > 
> > Semantic 传感器返回 **物体实例 ID 图**，每个像素值不是颜色而是**该位置可见物体的实例编号**。 数据类型是 `int32`，shape 为 `(H, W, 1)`。0 表示背景（无物体），1+ 表示不同的物体实例。 **Semantic 传感器零额外渲染成本** — 渲染器在生成 RGB 的同时输出语义信息。
> > 
> > </div>
> > 
> > ``` 
> >       加载语义传感器并解读观测
> > ```
> > 
> >     import numpy as np
> >     import habitat
> >     from habitat.config.default import get_config
> >     
> >     # ObjectNav semantic 配置自带 Semantic Sensor
> >     config = get_config("benchmark/nav/objectnav/objectnav_hm3d_with_semantic.yaml")
> >     env = habitat.Env(config)
> >     obs = env.reset()
> >     
> >     sem = obs["semantic"]
> >     print("shape:", sem.shape)   # (480, 640, 1) — 取决于 config 的 width/height
> >     print("dtype:", sem.dtype)   # int32
> >     print("unique IDs:", np.unique(sem))  # [0, 1, 3, 5, 12, ...] 场景中的物体实例
> >     
> >     # 查询物体类别：用 semantic_annotations() 映射 ID → 名称
> >     sim = env.sim
> >     sem_scene = sim.semantic_annotations()
> >     for obj in sem_scene.objects:
> >         print(f"ID={obj.id:3d}  category={obj.category.name():20s}  bbox={obj.aabb}")
> > 
> > </div>
> > 
> > <div>
> > 
> > **Semantic 传感器在哪里配置？**
> > 
> > Semantic 传感器通过 agent YAML 添加。两种方式：  
> > · **专用 agent**：`semantic_agent.yaml` — 只有 semantic 传感器，无 RGB/Depth  
> > · **组合 agent**：`rgbds_agent.yaml` — RGB + Depth + Semantic 四通道（推荐）  
> > 配置文件中通过 `defaults → /habitat/simulator/agents@...` 选择 agent 类型。
> > 
> > </div>
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 实操技巧
> > > 
> > > 如果你的测试场景没有 semantic 标注，返回的是全零数组。 可以用 `habitat-test-scenes`（van-gogh-room）或 MP3D/HM3D 完整场景测试。 用 `np.bincount(sem.flatten())` 可以统计每个物体 ID 在画面中的像素占比。
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 实验 4-7：自定义 Measure 指标教程
> > > 
> > > 用 @registry.register\_measure 注册自定义指标，理解 Measure 生命周期，实现碰撞计数器。
> > > 
> > > <div>
> > > 
> > > **Measure 的三个生命周期方法**
> > > 
> > > 每个 Measure 必须实现 3 个方法，由 `EmbodiedTask` 在 episode 的不同时刻调用：  
> > > · `_get_uuid()` — 返回字符串（如 `"collision_count"`），作为 metrics dict 的 key  
> > > · `reset_metric(*, episode, task)` — episode 开始时重置，初始化 `self._metric`  
> > > · `update_metric(*, episode, task, action)` — 每个 step 后更新，修改 `self._metric`  
> > > 用 `@registry.register_measure` 装饰器注册，类名即为注册 key。
> > > 
> > > </div>
> > > 
> > > ``` 
> > >       自定义碰撞计数器 Measure
> > > ```
> > > 
> > >     from habitat.core.registry import registry
> > >     from habitat.core.embodied_task import Measure
> > >     
> > >     @registry.register_measure
> > >     class CollisionCount(Measure):
> > >         """统计每个 episode 中 agent 碰撞到障碍物的次数"""
> > >         cls_uuid = "collision_count"
> > >     
> > >         def __init__(self, sim, config, *args, **kwargs):
> > >             self._sim = sim
> > >             super().__init__()
> > >     
> > >         def _get_uuid(self, *args, **kwargs):
> > >             return self.cls_uuid
> > >     
> > >         def reset_metric(self, episode, *args, **kwargs):
> > >             self._metric = {"count": 0, "is_collision": False}
> > >     
> > >         def update_metric(self, episode, action, *args, **kwargs):
> > >             self._metric["is_collision"] = False
> > >             if self._sim.previous_step_collided:
> > >                 self._metric["count"] += 1
> > >                 self._metric["is_collision"] = True
> > > 
> > > </div>
> > > 
> > > ``` 
> > >       在配置中启用自定义 Measure
> > > ```
> > > 
> > >     # 方法 1：通过代码动态添加
> > >     from habitat.config.default import get_config
> > >     config = get_config("benchmark/nav/pointnav/pointnav_habitat_test.yaml")
> > >     with habitat.config.read_write(config):
> > >         config.habitat.task.measurements["collision_count"] = {
> > >             "type": "CollisionCount"
> > >         }
> > >     
> > >     env = habitat.Env(config)
> > >     env.reset()
> > >     for _ in range(50):
> > >         env.step(env.action_space.sample())
> > >     print(env.get_metrics())  # {'collision_count': {'count': 12, 'is_collision': True}, ...}
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > 注册时机
> > > > 
> > > > `@registry.register_measure` 是模块级装饰器，Python 在 `import` 时执行。 **自定义 Measure 的 .py 文件必须在创建 Env 之前被导入**，否则 registry 中找不到这个类。 官方的 20+ Measure 实例在 `habitat/tasks/nav/nav.py` 和 `habitat/tasks/rearrange/rearrange_sensors.py` 中。
> > > > 
> > > > <div class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > ## 📝 本章总结
> > > > 
> > > > 7 个实验覆盖了 config 修改的主要维度：传感器、任务、指标。
> > > > 
> > > > | 实验      | 修改了什么             | 配置路径                          | 你学到的                                     |
> > > > | ------- | ----------------- | ----------------------------- | ---------------------------------------- |
> > > > | **4-1** | RGB 分辨率           | `sim_sensors.rgb_sensor`      | 分辨率影响内存（O(w×h)），与画质正相关                   |
> > > > | **4-2** | 传感器组合             | `sim_sensors / lab_sensors`   | sim\_sensors 挂载渲染传感器，lab\_sensors 提供任务信息 |
> > > > | **4-3** | 注册自定义传感器          | `@registry.register_sensor`   | 继承 Sensor 基类 → 5 个接口 → 全局注册              |
> > > > | **4-4** | 编写自定义 YAML        | `defaults → _self_`           | Hydra 配置继承 + 覆盖机制                        |
> > > > | **4-5** | success\_distance | `task.measurements.success`   | 评测指标 vs 训练信号的区别                          |
> > > > | **4-6** | Semantic 传感器      | `sim_sensors.semantic_sensor` | 物体实例 ID 图、semantic\_annotations() 查询类别名  |
> > > > | **4-7** | 自定义 Measure       | `@registry.register_measure`  | 实现碰撞计数器、理解 Measure 生命周期                  |
> > > > 

> > > > <div class="exercise">
> > > > 
> > > > #### 🏋️ 课后练习
> > > > 
> > > > **1.** 修改 `depth_sensor` 的 `min_depth` 和 `max_depth`，观察深度图的数值范围变化。  
> > > > **2.** 试着给 SimpleLidarSensor 添加 `min_range` 参数，过滤掉太近的射线值。  
> > > > **3.** 将实验 4-4 的自定义 YAML 配置用于实际训练（`python habitat-baselines/run.py ...`）， 观察分辨率降低对训练速度的影响。  
> > > > **4.** 修改 `spl`（Success weighted by Path Length）指标的权重，理解 SPL vs Success 的区别。
> > > > 
> > > > <div class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > <div class="page-nav">
> > > > 
> > > > [← 第3章：解剖参数](habitat-textbook-step3.html) [第5章：训练与评测 →](habitat-textbook-step5.html)
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
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
