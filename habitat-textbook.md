# 从零理解 Habitat — 具身智能入门教科书

> 一本为「零基础读者」准备的具身智能入门教科书——不要求你懂机器人学，不假设你读过任何论文。 我们从三个简单的问题出发：它是什么？它是怎么做的？我应该怎么学？

<div class="toc">

## 目录

<div class="toc-grid">

<div class="toc-item">

<span class="num">01</span><span class="text">**先打比喻** — 不写代码，先建心智模型</span>

</div>

<div class="toc-item">

<span class="num">02</span><span class="text">**第一原理** — 最小代码示例：hello, habitat</span>

</div>

<div class="toc-item">

<span class="num">03</span><span class="text">**拆解架构** — 五大核心模块逐个认识</span>

</div>

<div class="toc-item">

<span class="num">04</span><span class="text">**配置驱动** — 像搭乐高一样组合实验</span>

</div>

<div class="toc-item">

<span class="num">05</span><span class="text">**数据与任务** — Episode、Dataset、Task 的区别</span>

</div>

<div class="toc-item">

<span class="num">06</span><span class="text">**训练全景** — RL/IL 是如何嵌入这个体系</span>

</div>

<div class="toc-item">

<span class="num">07</span><span class="text">**Sim-to-Real** — 从仿真到真机的一行配置</span>

</div>

<div class="toc-item">

<span class="num">08</span><span class="text">**动手路线图** — 从安装到发论文的六步路径</span>

## 第1章 · 先打比喻 — 什么是具身智能平台

在碰任何代码之前，让我们先用日常生活的比喻建立一个"这个东西到底在做什么"的直觉。

<div class="metaphor-box">

### 核心比喻：Habitat 是一个"舞台 · 演员 · 剧本"系统

<div class="analogy-row">

<div class="analogy-item">

🏟️

<div class="real">

舞台

</div>

<div class="code">

Simulator

</div>

<div class="desc">

3D 室内场景 + 物理引擎  
提供"这里有什么，长什么样"

<div class="analogy-item">

🎭

<div class="real">

演员

</div>

<div class="code">

Agent + Sensor

</div>

<div class="desc">

机器人身体 + 传感器  
"我看到什么，我能做什么"

<div class="analogy-item">

📜

<div class="real">

剧本

</div>

<div class="code">

Task + Dataset

</div>

<div class="desc">

任务定义 + 数据集  
"这出戏要演什么，怎么算成功"

<div class="metaphor-box" style="border-color:#10b98130; background:linear-gradient(135deg, #10b98106, #0f172a);">

### 比喻一：像一个电子游戏

如果你玩过 RPG 游戏，理解 Habitat 非常简单：  
<span class="highlight-green">3D 场景</span> = 游戏地图（Matterport3D 室内场景）；  
<span class="highlight-green">Agent</span> = 你的游戏角色，身上挂着 RGB 摄像头、深度传感器（就像第一人称视角）；  
<span class="highlight-green">Task</span> = 任务目标（从"A 点走到 B 点"到"找到厨房里的水杯"）；  
<span class="highlight-green">step()</span> = 每按一次手柄按键，游戏前进一帧 — 角色移动一小步，屏幕刷新，判断是否完成任务。  
区别只在于：这个"游戏"里的角色不是你在控制，而是 **AI 策略在控制**。

</div>

<div class="metaphor-box" style="border-color:#8b5cf630; background:linear-gradient(135deg, #8b5cf606, #0f172a);">

### 比喻二：像一个健身房

Habitat 本质上是一个**给 AI 用的健身房**：  
<span class="highlight">仿真场景</span> = 各种训练器械（跑步机、哑铃架），安全可重复；  
<span class="highlight">AI 策略</span> = 健身的人（不断试错、积累经验）；  
<span class="highlight">训练框架 (RL)</span> = 教练（告诉 AI "这次做得不错/这次撞墙了"）；  
<span class="highlight">基准测试</span> = 体能测试（用统一标准衡量进步）。  
等"健身房"里练好了 → 一键切换到真实机器人（上赛场）。

</div>

> 💡
> 
> <div class="tip-title">
> 
> 学习提示
> 
> 本章的目的不是给你精确定义，而是**先建一个"大致是对的"的直觉**。当你困惑于代码细节时， 回到这个比喻：我在操作的是**舞台**（Simulator）、**演员**（Agent）、还是**剧本**（Task）？ 大部分困惑都源于混淆了这三个角色的职责边界。
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 第2章 · 第一原理 — 最小代码示例
> 
> 抛开所有配置文件和高级抽象。如果我们要写最"裸"的代码来表达"Habitat 在做什么"，就是下面这几行。
> 
> ### 一个完整的"hello, habitat"
> 
>     # 这是你能写出的最简 Habitat 程序 — 但它的结构就是一切
>     
>     import habitat
>     
>     # (1) 读配置 → 决定"今天练什么、在哪练"
>     config = habitat.get_config("benchmark/nav/pointnav.yaml")
>     
>     # (2) 造环境 → 把舞台、演员、剧本装配成一个整体
>     env = habitat.Env(config)
>     
>     # (3) 主循环 — 这就是整个"具身 AI"的最小单元
>     obs = env.reset()           # 开局：把演员放到起点
>     while not env.episode_over:
>         action = policy(obs)    # 决策：AI 看着观测，选一个动作
>         obs = env.step(action)  # 执行：环境推进一步，返回新的观测
>     
>     # 就这么简单。剩下的 10 万行代码，都是这三步的展开。
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 关于 `policy(obs)` — 什么是"策略"？
> > 
> > `policy(obs)` 是一个**策略函数**：输入观测 → 输出动作。它告诉机器人"看到什么，该做什么"。  
> > 这里故意把它写成一个黑盒，因为它**不是 Habitat 的一部分**——Habitat 提供"环境"，策略是你自己写的。  
> >   
> > **三种最常见的实现：**  
> > <span class="highlight-green">1. 随机动作</span> — `action = env.action_space.sample()`（默认示例用的就是这个，机器人乱走）  
> > <span class="highlight">2. 最短路径规划</span> — `Habitat 内置的 shortest_path_follower`（用 A\* 算法沿最短路径走到目标）  
> > <span class="highlight-blue">3. 训练好的神经网络</span> — `用 PPO/DD-PPO 训练的策略模型`（第 6 章重点讲这个）  
> >   
> > 把这个循环中的 `policy` 替换成任何一种实现，代码结构不变——这就是 Habitat 的模块化设计。
> > 
> > </div>
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 关键洞察：RL 的交互循环
> > > 
> > > 上面的 `reset() → step() → step() → ...` 循环是所有现代深度强化学习的**通用交互协议**。 OpenAI Gym 是这么做的，DeepMind Control Suite 也是这么做的。 Habitat 没有重新发明轮子 — 它在轮子上建造了一辆完整的车。
> > > 
> > > </div>
> > > 
> > > <div class="callout-grid">
> > > 
> > > <div class="callout">
> > > 
> > > <span class="big">📥</span>
> > > 
> > > <div class="label">
> > > 
> > > 输入
> > > 
> > > </div>
> > > 
> > > <div class="desc">
> > > 
> > > 一个 **action**（数字：0=stop, 1=前进, 2=左转, 3=右转）
> > > 
> > > <div class="callout">
> > > 
> > > <span class="big">📤</span>
> > > 
> > > <div class="label">
> > > 
> > > 输出
> > > 
> > > </div>
> > > 
> > > <div class="desc">
> > > 
> > > 一个 **observation 字典**（RGB 图像、深度图、GPS 坐标…）
> > > 
> > > <div class="callout">
> > > 
> > > <span class="big">🔄</span>
> > > 
> > > <div class="label">
> > > 
> > > 循环
> > > 
> > > </div>
> > > 
> > > <div class="desc">
> > > 
> > > 以固定频率运行（每一步 0.25m 或 15° 转角）
> > > 
> > > <div class="callout">
> > > 
> > > <span class="big">🏁</span>
> > > 
> > > <div class="label">
> > > 
> > > 终止
> > > 
> > > </div>
> > > 
> > > <div class="desc">
> > > 
> > > Episode 结束（到达目标 / 超时 / 主动 stop）→ reset()
> > > 
> > > </div>
> > > 
> > > ### 这段程序到底在做什么？
> > > 
> > > <div>
> > > 
> > > **程序目的**
> > > 
> > > 上面的代码是一个**最小完整的 PointNav（点对点导航）示例**。它的核心作用只有一句话：  
> > > <span style="color:#fbbf24;">让一个虚拟机器人在 3D 室内场景中，从起点出发，试图到达指定的目标点。</span>目标在哪里？ GPS 传感器告诉 Agent "目标在你北偏东 30°，距离 5.2 米"；RGB 摄像头是 Agent 的"眼睛"——但在这个最简版本里，策略（`policy`）还没学会"看"，所以机器人会**随机乱走**。
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > <div class="info-title" style="color:#6ee7b7;">
> > > 
> > > 你运行它时会看到什么？
> > > 
> > > </div>
> > > 
> > > **1. 终端输出：**每次 `reset()` 和 `step()` 会打印观测字典的 key（`rgb`, `depth`, `pointgoal_with_gps_compass`）和数组形状。  
> > > **2. 3D 渲染窗口：**一个 OpenCV 窗口实时显示 Agent 的第一人称视角（RGB 图像），你能看到 Agent 在房间里"走来走去"。  
> > > **3. 随机探索过程：**因为用的是随机动作，Agent 的行为不可预测——有时撞墙、有时原地打转、偶尔恰好接近目标。
> > > 
> > > 如果你看到 RGB 图像和 depth 的 shape 打印出来，Agent 在窗口里移动——说明你的 **整个环境装配成功**：Sim 渲染正常、Task 状态正常、Sensor 数据流通畅。这 15 行代码验证了 Hab 栈的四个关键组件全部就绪。
> > > 
> > > </div>
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > 这段伪代码 vs 实际可以跑的程序
> > > > 
> > > > 上面这个代码块故意写的是 **Native API**（`habitat.Env(config)`），因为它最直观地暴露了三个核心步骤： 读配置 → 造环境 → 主循环。它是一个**教学伪代码**，不是复制粘贴就能跑的完整脚本。  
> > > >   
> > > > 工程里对应的**实际可运行文件**是 `examples/example_pointnav.py`（Gym API 版） 和 `examples/my_native_pointnav.py`（Native API 版）。  
> > > > **启动命令：**  
> > > > `conda activate habitat && cd /develop/habitat-lab && python examples/example_pointnav.py`  
> > > >   
> > > > 两者演示的是同一个 PointNav 任务，只是 API 风格不同。学完第 3 章回来读这两个文件，代码结构会变得非常清晰。
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#c4b5fd;">
> > > > 
> > > > 你从这段代码中学到了什么？
> > > > 
> > > > </div>
> > > > 
> > > > 别看它短，这段代码是 **理解整个具身 AI 的"第一性原理"入口**：  
> > > > <span style="color:#93c5fd;">①</span> 所有强化学习环境都遵循 `reset() → step() → 终止` 这个协议——学会了 Habitat 的循环，OpenAI Gym / Isaac Sim 同理。  
> > > > <span style="color:#93c5fd;">②</span> "观测"总是一个 **字典**（`dict`），而不是单张图片——因为机器人有多个感官（眼、深度、GPS），这是与 CV 纯图像任务的根本区别。  
> > > > <span style="color:#93c5fd;">③</span> "动作"是一个**语义动作**（向前 0.25m、左转 15°），不是底层电机指令——Habitat 帮你抽象掉了物理细节。  
> > > > <span style="color:#93c5fd;">④</span> 策略（`policy`）和环境（`Env`）是**完全解耦**的两个模块——你可以在不改环境代码的情况下，换上随机策略、A\* 规划或训练好的神经网络。
> > > > 
> > > > </div>
> > > > 
> > > > ### 教科书代码 vs 工程文件：三版逐行对比
> > > > 
> > > > 下面把教科书里的"hello, habitat"伪代码、工程里的 Gym API 版、Native API 版放在一起对比，看清楚每一处差异。
> > > > 
> > > > <table>
> > > > <colgroup>
> > > > <col style="width: 25%" />
> > > > <col style="width: 25%" />
> > > > <col style="width: 25%" />
> > > > <col style="width: 25%" />
> > > > </colgroup>
> > > > <thead>
> > > > <tr class="header">
> > > > <th>对比维度</th>
> > > > <th>教科书伪代码<br />
> > > > <span style="font-weight:400;color:var(--text-dim);">（第 2 章教学用）</span></th>
> > > > <th>examples/example_pointnav.py<br />
> > > > <span style="font-weight:400;color:var(--text-dim);">（Gym API，可运行）</span></th>
> > > > <th>examples/my_native_pointnav.py<br />
> > > > <span style="font-weight:400;color:var(--text-dim);">（Native API，可运行）</span></th>
> > > > </tr>
> > > > </thead>
> > > > <tbody>
> > > > <tr class="odd">
> > > > <td><strong>API 层</strong></td>
> > > > <td><code>habitat.Env(config)</code><br />
> > > > Native API</td>
> > > > <td><code>gym.make("Habitat-v0", ...)</code><br />
> > > > Gym API（OpenAI 标准）</td>
> > > > <td><code>habitat.Env(config)</code><br />
> > > > Native API<br />
> > > > <span style="color:#6ee7b7;">← 和教科书一致</span></td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>配置文件</strong></td>
> > > > <td><code>benchmark/nav/pointnav.yaml</code><br />
> > > > （生产配置）</td>
> > > > <td><code>benchmark/nav/pointnav/pointnav_habitat_test.yaml</code><br />
> > > > （测试配置，免下载数据）</td>
> > > > <td><code>benchmark/nav/pointnav/pointnav_habitat_test.yaml</code><br />
> > > > （测试配置，免下载数据）</td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>创建环境</strong></td>
> > > > <td><code>env = habitat.Env(config)</code></td>
> > > > <td><code>env = gym.make("Habitat-v0",  cfg_file_path=...)</code><br />
> > > > （自动注册 + 传参）</td>
> > > > <td><code>env = habitat.Env(config)</code><br />
> > > > <span style="color:#6ee7b7;">← 和教科书一致</span></td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>动作格式</strong></td>
> > > > <td><code>action = policy(obs)</code><br />
> > > > （抽象黑盒）</td>
> > > > <td><code>action = env.action_space.sample()</code><br />
> > > > （随机采样，返回整数 0-3）<br />
> > > > 因为 Gym 接口要求 int</td>
> > > > <td><code>action = {"action": "move_forward"}</code><br />
> > > > （字典格式，语义化键名）<br />
> > > > <span style="color:#fbbf24;">← Native API 必须用 dict</span></td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>主循环</strong></td>
> > > > <td><code>while not env.episode_over:</code><br />
> > > > （条件循环，自动判断结束）</td>
> > > > <td><code>while True:</code> + 手动检测<br />
> > > > <code>if done: env.reset()</code><br />
> > > > + cv2 窗口关闭 → KeyboardInterrupt</td>
> > > > <td><code>for step in range(5):</code><br />
> > > > （定长循环，只走 5 步）<br />
> > > > <span style="color:#fbbf24;">← 没有用 episode_over</span></td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>可视化</strong></td>
> > > > <td>无</td>
> > > > <td><code>cv2.imshow()</code> 实时渲染<br />
> > > > RGB 第一人称窗口<br />
> > > > 按 Q 或关窗口退出</td>
> > > > <td>无（只打印 GPS 坐标到终端）</td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>错误处理</strong></td>
> > > > <td>无</td>
> > > > <td>try/except KeyboardInterrupt<br />
> > > > finally: cv2.destroyAllWindows()</td>
> > > > <td>try/finally: env.close()<br />
> > > > （保证资源释放）</td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>代码行数</strong></td>
> > > > <td>10 行</td>
> > > > <td>73 行</td>
> > > > <td>34 行</td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>适合阶段</strong></td>
> > > > <td><strong>第 2 章</strong>：建立心智模型<br />
> > > > 理解 RL 交互协议</td>
> > > > <td><strong>第 3-4 章</strong>：环境装好后动手跑<br />
> > > > 看到画面、感受随机探索</td>
> > > > <td><strong>第 3 章</strong>：学架构时对照源码<br />
> > > > 理解 Observation 字典结构</td>
> > > > </tr>
> > > > </tbody>
> > > > </table>
> > > > 
> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#fbbf24;">
> > > > 
> > > > 三个版本为什么都不完全一样？ — 这是故意的
> > > > 
> > > > </div>
> > > > 
> > > > **教科书伪代码**不是一个能跑的程序——它是一张**"地图"**。它用最少的字符告诉你整个具身 AI 的地形： 左边是观测（传感器），右边是动作（策略），中间是环境（Env）。  
> > > >   
> > > > **example\_pointnav.py**（Gym 版）是**"体验版"**：加了可视化窗口让你"看到"Agent 在动，适合确认环境装好了、开始动手玩。  
> > > > **my\_native\_pointnav.py**（Native 版）是**"说明书版"**：去掉了可视化噪音，只打印数据结构，适合学架构时对照源码一行行读懂。  
> > > >   
> > > > 三个版本的**核心结构完全一致**：`读配置 → 造环境 → reset() → step()循环`。只是包装方式（Gym/Native）、辅助功能（可视化/打印）、结束条件（定长/条件/手动中断）不同而已。 就像同一辆车的三个视角：**地图、试驾、拆解**——你需要三个都看一遍。
> > > > 
> > > > </div>
> > > > 
> > > > ### 快速自测：你理解了吗？
> > > > 
> > > > <div class="qa-grid">
> > > > 
> > > > <div class="qa-card">
> > > > 
> > > > **Q1:** `obs = env.reset()` 返回的是什么类型？有几把"钥匙"？  
> > > > **A:** 返回 `dict`，通常有 3-4 个 key：`rgb`（图像）、`depth`（深度）、`pointgoal_with_gps_compass`（目标方向+距离）。具体取决于配置里启用了哪些传感器。
> > > > 
> > > > </div>
> > > > 
> > > > <div class="qa-card">
> > > > 
> > > > **Q2:** 如果我想让 Agent 走到 B 点而不是 A 点，改哪里？  
> > > > **A:** 不是改代码，是**改 Dataset 里的 Episode 定义**。每个 Episode 自带 start 和 goal 坐标，Env 自动读取。想手动指定？看第 4 章"改配置实验"。
> > > > 
> > > > </div>
> > > > 
> > > > <div class="qa-card">
> > > > 
> > > > **Q3:** 为什么 `action` 是数字 0-3，而不是 "move\_forward"？  
> > > > **A:** 内部确实有名称映射（`{"move_forward": 1, "turn_left": 2, ...}`），传到 `step()` 的是 action index。两种写法等效，具体看第 3 章 Task 模块。
> > > > 
> > > > </div>
> > > > 
> > > > <div class="qa-card">
> > > > 
> > > > **Q4:** 跑通了之后，下一步应该改哪些参数来"玩一玩"？  
> > > > **A:** 改分辨率（`RENDERER/RESOLUTION`）看画质变化、改传感器组合（加 Depth 去 RGB）、改 `success_distance` 看"成功判定"变严后的效果——都在第 4 章。
> > > > 
> > > > ### 那个 `pointnav_habitat_test.yaml` 到底是什么？
> > > > 
> > > > <div>
> > > > 
> > > > **一句话回答**
> > > > 
> > > > `habitat_test` 是 Habitat 自带的**测试数据集**，用 3 个极小场景（公寓、城堡、梵高房间）取代了需要单独下载的 Gibson/MP3D 大数据集。  
> > > > 它的设计目的就是让你**不联网、不下载任何数据**就能验证整个 Habitat 栈是否正常运转——从 Sim 渲染到 Task 状态机到 Sensor 数据流，一个 `python examples/example_pointnav.py` 全部测到。
> > > > 
> > > > </div>
> > > > 
> > > > 先看这个配置文件的完整内容（只有 21 行，但蕴含了整个配置系统的设计哲学）：
> > > > 
> > > >     # benchmark/nav/pointnav/pointnav_habitat_test.yaml  —  完整内容
> > > >     
> > > >     defaults:
> > > >       - pointnav_base                         # 继承"标准 PointNav 配置"
> > > >       - /habitat/dataset/pointnav: habitat_test  # 使用"test 数据集"，覆盖默认的大数据集
> > > >       - _self_
> > > >     
> > > >     habitat:
> > > >       environment:
> > > >         max_episode_steps: 500                # 每个 episode 最多 500 步
> > > >       simulator:
> > > >         agents:
> > > >           main_agent:
> > > >             sim_sensors:
> > > >               rgb_sensor:
> > > >                 width:  256                   # 分辨率从默认 640 降到 256
> > > >                 height: 256                   # 测试用小分辨率，更快
> > > >               depth_sensor:
> > > >                 width:  256
> > > >                 height: 256
> > > > 
> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#c4b5fd;">
> > > > 
> > > > 理解它的三层继承关系
> > > > 
> > > > </div>
> > > > 
> > > > 这个文件几乎没有"写死"任何东西——所有默认值都来自继承链。理解了这条链，你就理解了 Habitat 的配置哲学：
> > > > 
> > > > </div>
> > > > 
> > > > <div class="dual-panel">
> > > > 
> > > > <div class="panel">
> > > > 
> > > > #### 🔗 继承链：谁继承了谁？
> > > > 
> > > > `pointnav_habitat_test.yaml`  
> > > >   ├─ defaults 继承  
> > > >   │   ├─ `pointnav_base` — 标准 PointNav 骨架  
> > > >   │   └─ `habitat_test` — 测试数据集（覆盖默认数据集）  
> > > >   └─ `habitat:` — 覆盖传感器分辨率 ↑
> > > > 
> > > > **pointnav\_base 的继承链（往下展开）：**  
> > > > `→ habitat_config_base`（Env 基本参数）  
> > > > `→ task: pointnav`（任务类型 + 指标定义）  
> > > > `→ rgbd_agent`（Agent 搭载 RGB+Depth 传感器）
> > > > 
> > > > </div>
> > > > 
> > > > <div class="panel">
> > > > 
> > > > #### 📂 关键文件位置
> > > > 
> > > > `habitat-lab/habitat/config/`
> > > > 
> > > > <div style="font-family:&#39;JetBrains Mono&#39;,monospace; font-size:0.74rem; color:var(--text-dim); background:#0f172a; border-radius:8px; padding:12px 14px; margin-top:8px; line-height:1.9;">
> > > > 
> > > > <span style="color:#94a3b8;">config/</span>  
> > > > ├─ <span style="color:#93c5fd;">benchmark/nav/pointnav/</span>  
> > > > │   ├─ <span style="color:#cbd5e1;">pointnav\_base.yaml</span> <span style="color:#64748b;">← 骨架</span>  
> > > > │   └─ <span style="color:#cbd5e1;">pointnav\_habitat\_test.yaml</span> <span style="color:#64748b;">← 这个</span>  
> > > > ├─ <span style="color:#6ee7b7;">habitat/dataset/pointnav/</span>  
> > > > │   └─ <span style="color:#cbd5e1;">habitat\_test.yaml</span> <span style="color:#64748b;">← 数据集定义</span>  
> > > > ├─ <span style="color:#c4b5fd;">habitat/task/</span>  
> > > > │   └─ <span style="color:#cbd5e1;">pointnav.yaml</span> <span style="color:#64748b;">← 任务定义</span>  
> > > > └─ <span style="color:#fbbf24;">habitat/simulator/agents/</span>  
> > > >     └─ <span style="color:#cbd5e1;">rgbd\_agent.yaml</span> <span style="color:#64748b;">← Agent 定义</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#6ee7b7;">
> > > > 
> > > > 为什么叫 "habitat\_test"？它和完整数据集有什么区别？
> > > > 
> > > > </div>
> > > > 
> > > > | 对比维度           | habitat\_test（测试用）                            | 完整数据集（Gibson / MP3D）                 |
> > > > | -------------- | --------------------------------------------- | ------------------------------------ |
> > > > | **场景数量**       | 3 个（apartment, skokloster, van-gogh）          | Gibson 572 个小场景 / MP3D 90 个大场景       |
> > > > | **Episode 数量** | \~100                                         | 数万到数十万                               |
> > > > | **下载大小**       | \~5 MB（随 pip install 自动安装）                    | Gibson \~1.5 GB / MP3D \~30 GB       |
> > > > | **联网需求**       | 不需要（已内置）                                      | 需要手动下载 + 解压                          |
> > > > | **用途**         | 快速验证代码、CI 测试、学习                               | 训练 AI 模型、发论文评估                       |
> > > > | **数据路径**       | `data/datasets/pointnav/habitat-test-scenes/` | `data/scene_datasets/{gibson,mp3d}/` |
> > > > 

> > > > </div>
> > > > 
> > > > > ⚠️
> > > > > 
> > > > > <div class="warn-title">
> > > > > 
> > > > > 重点理解
> > > > > 
> > > > > 配置文件的核心思想是**"继承 + 覆盖"**——就像面向对象编程里的类继承一样。  
> > > > > `pointnav_habitat_test.yaml` 继承了 `pointnav_base` 的全部骨架（Env 参数、PointNav 任务、RGBD Agent），**只覆盖了 3 个东西**：数据集改为 test、分辨率降到 256、步数设为 500。  
> > > > >   
> > > > > 同理，如果你想把测试换成 Gibson 数据集训练正式模型，只需要把 `habitat_test` 换成 `gibson`，其他一切照旧——这就是配置驱动的威力。  
> > > > > （具体的"改配置做实验"是第4章的内容，但不急，先把第3章的架构搞清楚。）
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div>
> > > > > 
> > > > > <div class="info-title" style="color:#fca5a5;">
> > > > > 
> > > > > 常见困惑：我想改"机器人做什么"，应该改哪个文件？
> > > > > 
> > > > > </div>
> > > > > 
> > > > > **不是改 `pointnav_habitat_test.yaml`**——这个文件的作用是**"接线"**，把现有的 Task + Dataset + Agent 三段拼在一起。 它相当于一个**启动参数列表**，不定义任何任务逻辑。
> > > > > 
> > > > > 你要改的东西，分布在不同文件里：
> > > > > 
> > > > > <table>
> > > > > <colgroup>
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > </colgroup>
> > > > > <thead>
> > > > > <tr class="header">
> > > > > <th>你想改什么</th>
> > > > > <th>改哪个文件</th>
> > > > > <th>涉及章节</th>
> > > > > </tr>
> > > > > </thead>
> > > > > <tbody>
> > > > > <tr class="odd">
> > > > > <td><strong>任务目标</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（改成找杯子、开门…）</span></td>
> > > > > <td><code>benchmark/</code> 里改 <code>defaults</code> 的 task 引用<br />
> > > > > 或自己写新的 <code>habitat/task/my_task.yaml</code></td>
> > > > > <td>第 3 章（理解 Task 结构）<br />
> > > > > 第 4 章（自己创建 benchmark）</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td><strong>起点 / 终点</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（让机器人走另一条路）</span></td>
> > > > > <td><code>data/datasets/</code> 里的 Episode JSON<br />
> > > > > 或换一个 Dataset 引用</td>
> > > > > <td>第 5 章（Episode / Dataset 定义）</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td><strong>传感器</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（加 LiDAR、换分辨率…）</span></td>
> > > > > <td>在 benchmark YAML 的 <code>habitat.simulator.agents</code> 段覆盖<br />
> > > > > 或修改 <code>habitat/simulator/agents/rgbd_agent.yaml</code></td>
> > > > > <td>第 3 章（Sensor 概念）<br />
> > > > > 第 4 章（改传感器实验）</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td><strong>动作空间</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（加"跳跃"、改步长…）</span></td>
> > > > > <td><code>habitat/task/pointnav.yaml</code> 的 <code>actions</code> 段</td>
> > > > > <td>第 3 章（Task 的动作定义）</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td><strong>成功判定 / 奖励</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（离多远算成功？）</span></td>
> > > > > <td><code>habitat/task/pointnav.yaml</code> 的 <code>measurements</code> 段<br />
> > > > > 或在 benchmark YAML 用 <code>habitat.task.measurements.success.success_distance=0.1</code></td>
> > > > > <td>第 4 章（改 success_distance 实验）<br />
> > > > > 第 5 章（自定义 Measure）</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td><strong>策略（AI 大脑）</strong><br />
> > > > > <span style="font-size:0.75rem;color:var(--text-dim);">（从随机走变成真正"学会走"）</span></td>
> > > > > <td>不是配置文件的事——写 Python 代码<br />
> > > > > 或用 <code>habitat_baselines</code> 训练</td>
> > > > > <td>第 6 章（PPO/DDPPO 训练）</td>
> > > > > </tr>
> > > > > </tbody>
> > > > > </table>
> > > > > 
> > > > > **简单记法：**  
> > > > > `benchmark/*.yaml` = 接线板（"用哪个任务 + 哪个数据集 + 哪个 Agent"）  
> > > > > `habitat/task/*.yaml` = 任务说明书（动作有哪些，怎么算成功）  
> > > > > `habitat/dataset/*.yaml` = 数据目录（Episodes 从哪读）  
> > > > > `data/datasets/**/*.json.gz` = 数据本身（每个 Episode 的具体起点/终点坐标）  
> > > > > `habitat/tasks/*.py` = 源码（Task 的真正 Python 逻辑）
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### 实战追踪：`example_pointnav.py` 到底跑了一个什么 Task？
> > > > > 
> > > > > 把前面的概念落到具体文件上。从 `example_pointnav.py` 出发，一共经过 4 层，最终找到 Task 的 Python 源码：
> > > > > 
> > > > >     # 调用链路：一行 gym.make() → 4 层配置文件 → 1 个 Python 类
> > > > >     
> > > > >     # 第 0 层：你的代码
> > > > >     import gym, habitat.gym
> > > > >     env = gym.make("Habitat-v0", cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml")
> > > > >     
> > > > >     # 第 1 层：pointnav_habitat_test.yaml — 接线板
> > > > >     #   defaults: [pointnav_base, /habitat/dataset/pointnav: habitat_test]
> > > > >     #   → 指定 Task = "pointnav_base 里定义的 task"，Dataset = "habitat_test"
> > > > >     
> > > > >     # 第 2 层：pointnav_base.yaml — 骨架
> > > > >     #   defaults: [/habitat/task: pointnav, ...]
> > > > >     #   → 展开后连线：Task = "Nav-v0"，Agent = "RGBD"
> > > > >     
> > > > >     # 第 3 层：habitat/config/habitat/task/pointnav.yaml — 任务说明书（YAML）
> > > > >     #   type: Nav-v0
> > > > >     #   actions: [stop, move_forward, turn_left, turn_right]  ← Agent 只会 4 个动作
> > > > >     #   measurements: [distance_to_goal, success, spl, ...]    ← 怎么判断"到了"？走多快？
> > > > >     #   lab_sensors: [pointgoal_with_gps_compass_sensor]       ← 告诉 Agent 目标在哪
> > > > >     
> > > > >     # 第 4 层：habitat/tasks/nav/nav.py — 任务源码（Python）
> > > > >     @registry.register_task(name="Nav-v0")        # ← 注册为 "Nav-v0"
> > > > >     class NavigationTask(EmbodiedTask):           # ← 第 1317 行
> > > > >         def overwrite_sim_config(...): ...       # 每次新 Episode → 加载对应场景
> > > > >         def _check_episode_is_active(...): ...   # Agent 叫 STOP 就结束
> > > > > 
> > > > > <div>
> > > > > 
> > > > > <div class="info-title" style="color:#6ee7b7;">
> > > > > 
> > > > > Task 到底定义了什么东西？
> > > > > 
> > > > > </div>
> > > > > 
> > > > > 以 `example_pointnav.py` 运行的 PointNav 为例，Task 负责回答 5 个问题：
> > > > > 
> > > > > <table>
> > > > > <colgroup>
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > </colgroup>
> > > > > <thead>
> > > > > <tr class="header">
> > > > > <th>问题</th>
> > > > > <th>答案（PointNav）</th>
> > > > > <th>在哪个文件定义的</th>
> > > > > </tr>
> > > > > </thead>
> > > > > <tbody>
> > > > > <tr class="odd">
> > > > > <td><strong>Agent 能做什么动作？</strong></td>
> > > > > <td>前进、左转、右转、停下<br />
> > > > > （共 4 个离散动作）</td>
> > > > > <td><code>pointnav.yaml</code> 的 <code>actions</code> 段<br />
> > > > > 源码：<code>nav.py</code> MoveForwardAction / TurnLeftAction / StopAction 等类</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td><strong>Agent 怎么知道目标在哪？</strong></td>
> > > > > <td>GPS+Compass 传感器<br />
> > > > > 返回 <code>[距离, 角度]</code> 的向量</td>
> > > > > <td><code>pointnav.yaml</code> 的 <code>lab_sensors</code> 段<br />
> > > > > 源码：<code>nav.py:290</code> IntegratedPointGoalGPSAndCompassSensor</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td><strong>什么算"到了"？</strong></td>
> > > > > <td>Agent 叫 STOP 时，到目标的距离<br />
> > > > > ＜ <code>success_distance</code>（默认 0.2 米）</td>
> > > > > <td><code>pointnav.yaml</code> 的 <code>measurements.success</code><br />
> > > > > 源码：<code>nav.py:505</code> Success.update_metric()</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td><strong>走得好不好？</strong></td>
> > > > > <td>SPL = 最短路径 ÷ 实际走的路径 × 是否成功<br />
> > > > > （越大越好，最高 1.0）</td>
> > > > > <td><code>pointnav.yaml</code> 的 <code>measurements.spl</code><br />
> > > > > 源码：<code>nav.py:549</code> SPL.update_metric()</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td><strong>每步给多少奖励？</strong></td>
> > > > > <td>当前距离 − 上一步距离<br />
> > > > > （靠近目标 → 正奖励，远离 → 负奖励）</td>
> > > > > <td><code>pointnav.yaml</code> 的 <code>measurements.distance_to_goal_reward</code><br />
> > > > > 源码：<code>nav.py:1004</code> DistanceToGoalReward.update_metric()</td>
> > > > > </tr>
> > > > > </tbody>
> > > > > </table>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > > 💡
> > > > > > 
> > > > > > <div class="tip-title">
> > > > > > 
> > > > > > 把这个表当"查字典"用
> > > > > > 
> > > > > > 以后你想改任何一个行为，只要回到这张表找到对应的"在哪个文件"那一列，改那个 YAML 里的对应字段就行了。  
> > > > > > 比如想改"离目标 0.5 米就算成功" → 在 `pointnav.yaml` 或 benchmark YAML 里设 `success_distance: 0.5`。  
> > > > > > 比如想加一个"跳跃"动作 → 在 `pointnav.yaml` 的 actions 段加条目 + 在 `nav.py` 写对应的 Python 类。  
> > > > > > 第 3 章会详细展开"架构"，第 4 章会带你动手改这些配置。
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 第3章 · 拆解架构 — 五大核心模块
> > > > > > 
> > > > > > `env.step(action)` 这短短一行背后，有五个模块在协同工作。我们用"剥洋葱"的方式一层层拆开。
> > > > > > 
> > > > > > <div class="arch-diagram">
> > > > > > 
> > > > > > ← 你的代码调用 · 自顶向下 →
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer l-app" style="min-width:200px;">
> > > > > > 
> > > > > > 🧠 你的策略 / 训练器 <span class="small">policy(obs) → action</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓   `env.step(action)`   ↓
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer l-core">
> > > > > > 
> > > > > > 🔌 Env <span class="small">装配器：把所有模块连接起来</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓   调度   ↓
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer l-task">
> > > > > > 
> > > > > > 🎯 Task <span class="small">裁判：动作是否合法？是否成功？</span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-layer l-sim">
> > > > > > 
> > > > > > 🖥️ Simulator <span class="small">引擎：渲染 RGB + 物理计算</span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-layer l-data">
> > > > > > 
> > > > > > 📦 Dataset <span class="small">题库：第 N 题 = 场景 + 起终点</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓   读取   ↓
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer l-core" style="background:#64748b20; border-color:#64748b; color:#94a3b8;">
> > > > > > 
> > > > > > 🎥 SensorSuite <span class="small">感官集合：RGB / Depth / GPS / Compass / …</span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### 一个 `step(action)` 调用，内部发生了什么？
> > > > > > 
> > > > > > <div class="flow-box">
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #3b82f6;">
> > > > > > 
> > > > > > **1. Env 收到 action**
> > > > > > 
> > > > > > 只是一个整数  
> > > > > > (0/1/2/3)
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #8b5cf6;">
> > > > > > 
> > > > > > **2. Task 检查 action**
> > > > > > 
> > > > > > stop 是否合法？  
> > > > > > episode 是否超时？
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #10b981;">
> > > > > > 
> > > > > > **3. Simulator 执行**
> > > > > > 
> > > > > > 移动 Agent 0.25m  
> > > > > > 渲染新视角 RGB/Depth
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #64748b;">
> > > > > > 
> > > > > > **4. SensorSuite 采集**
> > > > > > 
> > > > > > RGB/Depth/GPS/Compass  
> > > > > > 打包为观测字典
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #f59e0b;">
> > > > > > 
> > > > > > **5. Task 计算指标**
> > > > > > 
> > > > > > 到目标距离？  
> > > > > > 是否成功？SPL？
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top: 3px solid #ec4899;">
> > > > > > 
> > > > > > **6. Env 返回 obs + 指标**
> > > > > > 
> > > > > > 一个字典  
> > > > > > {rgb, depth, gps, ...}
> > > > > > 
> > > > > > <div class="module-grid" style="margin-top: 32px;">
> > > > > > 
> > > > > > <div class="module" style="border-left-color: var(--accent-core);">
> > > > > > 
> > > > > > ### 🔌 Env — 装配器 (Assembler)
> > > > > > 
> > > > > > 这是你唯一直接交互的对象。它的职责是"组装"——把 Simulator、Task、Dataset、SensorSuite 按照配置绑在一起。 它是 **Facade（外观模式）** 的经典实例。
> > > > > > 
> > > > > >   - **文件：**`habitat/core/env.py`
> > > > > >   - **你调用的：**`reset() / step() / close()`
> > > > > >   - **它不做的事：**不渲染场景、不判断输赢、不管理数据集 — 它只是把调用分发给正确的模块
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="module" style="border-left-color: var(--accent-sim);">
> > > > > > 
> > > > > > ### 🖥️ Simulator — 引擎 (Engine)
> > > > > > 
> > > > > > 整个系统的"物理层"。它加载 3D 场景，执行移动和碰撞检测，渲染传感器图像。 可以把它理解为 Unity/Unreal 游戏引擎的一个轻量版。
> > > > > > 
> > > > > >   - **文件：**`habitat/sims/habitat_simulator/`
> > > > > >   - **核心能力：**加载 .glb 场景 → 渲染 RGB/Depth/Semantic → 执行刚体物理
> > > > > >   - **关键设计：**它是一个**抽象基类** — 换一个后端（真机 PyRobot）不改任何上层代码
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="module" style="border-left-color: var(--accent-task);">
> > > > > > 
> > > > > > ### 🎯 Task — 裁判 (Judge)
> > > > > > 
> > > > > > 定义"你在做什么"和"怎么算赢"。它不渲染场景，不加载数据 — 只负责三件事：接收 action、 判断 episode 是否结束、计算评估指标。
> > > > > > 
> > > > > >   - **文件：**`habitat/core/embodied_task.py` → `habitat/tasks/nav/nav.py`
> > > > > >   - **核心方法：**`step(action)` / `measurements` / `is_stop_called`
> > > > > >   - **指标体系：**Success / SPL / SoftSPL / DistanceToGoal / …
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="module" style="border-left-color: var(--accent-data);">
> > > > > > 
> > > > > > ### 📦 Dataset — 题库 (Question Bank)
> > > > > > 
> > > > > > 提供"这道题"的具体参数：用哪个场景、起点在哪、终点/目标是什么。 每次 `reset()` 就从题库中抽一道新题。
> > > > > > 
> > > > > >   - **文件：**`habitat/core/dataset.py` → `habitat/datasets/` 下各子类
> > > > > >   - **最小单元：**`Episode` — scene\_id + start\_position + goals
> > > > > >   - **关键设计：**Task 依赖 Episode 来配置智能体起点和目标，但 Task 不关心 Episode 从哪来
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="module" style="border-left-color: var(--accent-config);">
> > > > > > 
> > > > > > ### 🎥 SensorSuite — 感官 (Senses)
> > > > > > 
> > > > > > 一个**可插拔的传感器集合**。你可以像给手机插耳机一样，给 Agent 添加或移除传感器。 每个传感器实现一个 `get_observation()` 方法。
> > > > > > 
> > > > > >   - **文件：**`habitat/core/sensor.py`
> > > > > >   - **内置传感器：**RGB / Depth / Semantic / GPS / Compass / …
> > > > > >   - **自定义传感器：**只需用 `@registry.register_sensor` 注册一个新类
> > > > > > 
> > > > > > > 💡
> > > > > > > 
> > > > > > > <div class="tip-title">
> > > > > > > 
> > > > > > > 模块化思想的核心：每个模块只做一件事
> > > > > > > 
> > > > > > > 五大模块之间通过**明确的抽象接口**通信，而非直接依赖具体实现。这带来两个巨大好处： (1) **可替换** — 换个数据集？只改 Dataset 配置。换个仿真器？只改 Simulator 类型。 (2) **可测试** — 每个模块可以独立单元测试，不需要启动整个环境。 这是设计优秀软件系统的通用原则，也是 Habit 代码库最值得学习的地方。
> > > > > > > 
> > > > > > > <div class="section">
> > > > > > > 
> > > > > > > <div class="container">
> > > > > > > 
> > > > > > > ## 第4章 · 配置驱动 — 像搭乐高一样做实验
> > > > > > > 
> > > > > > > Habitat 最特立独行的设计：你不写代码来组合实验，你写 YAML 配置文件。这初看很"反直觉"，但一旦理解，会极大加速你的研究迭代。
> > > > > > > 
> > > > > > > ### 为什么要配置驱动？
> > > > > > > 
> > > > > > > <div class="callout-grid">
> > > > > > > 
> > > > > > > <div class="callout">
> > > > > > > 
> > > > > > > <span class="big">🧩</span>
> > > > > > > 
> > > > > > > <div class="label">
> > > > > > > 
> > > > > > > 组合爆炸
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="desc">
> > > > > > > 
> > > > > > > 5 种任务 × 3 种传感器组合 × 4 种场景 = 60 种实验，靠改代码管理？灾难。
> > > > > > > 
> > > > > > > <div class="callout">
> > > > > > > 
> > > > > > > <span class="big">🔁</span>
> > > > > > > 
> > > > > > > <div class="label">
> > > > > > > 
> > > > > > > 可复现
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="desc">
> > > > > > > 
> > > > > > > 一个 YAML 文件 = 一个完整实验的快照。别人复现你的结果只需要这一个文件。
> > > > > > > 
> > > > > > > <div class="callout">
> > > > > > > 
> > > > > > > <span class="big">🏗️</span>
> > > > > > > 
> > > > > > > <div class="label">
> > > > > > > 
> > > > > > > 分层继承
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="desc">
> > > > > > > 
> > > > > > > Hydra 支持配置的"继承+覆写"：你只改和大 baseline 不同的那几行。
> > > > > > > 
> > > > > > > <div class="callout">
> > > > > > > 
> > > > > > > <span class="big">🧪</span>
> > > > > > > 
> > > > > > > <div class="label">
> > > > > > > 
> > > > > > > 超参搜索
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="desc">
> > > > > > > 
> > > > > > > Hydra 的多运行模式：自动对所有参数组合做网格搜索。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### 配置的层次结构
> > > > > > > 
> > > > > > > <div class="dual-panel">
> > > > > > > 
> > > > > > > <div class="panel" style="border-top: 3px solid #3b82f6;">
> > > > > > > 
> > > > > > > #### 概念层次（从上到下）
> > > > > > > 
> > > > > > > <div style="font-size:0.88rem; color:var(--text-dim); line-height:2;">
> > > > > > > 
> > > > > > > 📋 **Benchmark Config** — 顶层，引用所有子配置  
> > > > > > >   ├── 🌍 **Habitat Config** — 全局设置（seed、env\_id）  
> > > > > > >   ├── 🎯 **Task Config** — 选哪种任务、什么动作空间  
> > > > > > >   ├── 🖥️ **Simulator Config** — 选哪个后端、什么传感器  
> > > > > > >   │   └── 🤖 **Agent Config** — 智能体的物理参数  
> > > > > > >   └── 📦 **Dataset Config** — 数据路径、split 选择  
> > > > > > > 
> > > > > > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > > > > > 
> > > > > > > #### 对应的 YAML 文件路径
> > > > > > > 
> > > > > > > <div style="font-size:0.82rem; color:#64748b; font-family:monospace; line-height:2;">
> > > > > > > 
> > > > > > > benchmark/nav/pointnav.yaml  
> > > > > > > habitat/config\_benchmark.yaml  
> > > > > > > config/habitat/task/pointnav.yaml  
> > > > > > > config/habitat/simulator/sim.yaml  
> > > > > > >   config/habitat/simulator/agents/rgbd\_agent.yaml  
> > > > > > > config/habitat/dataset/pointnav/gibson.yaml  
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### 动手理解：追踪一个完整配置
> > > > > > > 
> > > > > > > <div class="step-list">
> > > > > > > 
> > > > > > > <div class="step-item">
> > > > > > > 
> > > > > > > ### 打开 `benchmark/nav/pointnav.yaml`
> > > > > > > 
> > > > > > > 这是最常见的人口点。它只有几行 `defaults` 引用，像一个"索引导航"。 关键语法：`- /habitat/task: pointnav` 意思是"去 habitat/config/habitat/task/ 目录下找 pointnav.yaml"。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="step-item">
> > > > > > > 
> > > > > > > ### 追踪 `config/habitat/task/pointnav.yaml`
> > > > > > > 
> > > > > > > `type: PointNav-v1` → 这就是 Registry 注册的任务名称。Hydra 会根据这个名字去 Registry 中查找对应的 Python 类。 `actions: [stop, move_forward, turn_left, turn_right]` → 定义离散动作空间。 `measurements: [distance_to_goal, success, spl]` → 声明评估指标。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="step-item">
> > > > > > > 
> > > > > > > ### 追踪 `config/habitat/simulator/agents/rgbd_agent.yaml`
> > > > > > > 
> > > > > > > `height: 1.5`（传感器离地高度）、`sensors: [rgb, depth]`（挂载哪些传感器）、 `hfov: 90`（水平视野）、每条传感器的分辨率参数。改变这些值 → 改变 AI "看到的世界"。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="step-item">
> > > > > > > 
> > > > > > > ### 实践：创建你自己的变体
> > > > > > > 
> > > > > > > 在 `benchmark/nav/` 下新建一个 `my_experiment.yaml`， 在 `defaults` 中覆盖一个参数：`- /habitat/task: pointnav` 改成 `- /habitat/task: vln_r2r`。 不需要改任何 Python 代码，你就从 PointNav 切换到了 VLN。
> > > > > > > 
> > > > > > > > ⚠️
> > > > > > > > 
> > > > > > > > <div class="warn-title">
> > > > > > > > 
> > > > > > > > 常见误区：以为配置只是"参数列表"
> > > > > > > > 
> > > > > > > > Hydra 配置在 Habitat 中不是简单的参数表，它是 **工厂模式 + 依赖注入** 的实现。 `type: PointNav-v1` → Registry 查找 → 实例化 `PointNavTask` 类 → 注入到 Env 中。整个调用链是自动装配的。理解了这一点，你就能理解为什么 Habit 的代码能做到"改配置 = 改行为"。
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 第5章 · 数据与任务 — Episode 是什么
> > > > > > > > 
> > > > > > > > 很多新手最容易混淆的就是 Episode、Dataset、Task 三者的关系。这一章把这个问题讲透彻。
> > > > > > > > 
> > > > > > > > <div class="metaphor-box" style="border-color:#10b98130; background:linear-gradient(135deg, #10b98106, #0f172a);">
> > > > > > > > 
> > > > > > > > ### 比喻：考试系统
> > > > > > > > 
> > > > > > > > <div class="analogy-row">
> > > > > > > > 
> > > > > > > > <div class="analogy-item">
> > > > > > > > 
> > > > > > > > 📝
> > > > > > > > 
> > > > > > > > <div class="real">
> > > > > > > > 
> > > > > > > > 一道题
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="code">
> > > > > > > > 
> > > > > > > > Episode
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > "在 Gibson 场景 \#42，  
> > > > > > > > 从 (1,2,0) 走到 (8,5,0)"
> > > > > > > > 
> > > > > > > > <div class="analogy-item">
> > > > > > > > 
> > > > > > > > 📚
> > > > > > > > 
> > > > > > > > <div class="real">
> > > > > > > > 
> > > > > > > > 题库
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="code">
> > > > > > > > 
> > > > > > > > Dataset
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > "Gibson PointNav 题库  
> > > > > > > > 共 1000 道训练题"
> > > > > > > > 
> > > > > > > > <div class="analogy-item">
> > > > > > > > 
> > > > > > > > 📋
> > > > > > > > 
> > > > > > > > <div class="real">
> > > > > > > > 
> > > > > > > > 考试规则
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="code">
> > > > > > > > 
> > > > > > > > Task
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > "走到距目标 0.1m 内  
> > > > > > > > 算通过，限时 500 步"
> > > > > > > > 
> > > > > > > > <div class="analogy-item">
> > > > > > > > 
> > > > > > > > 🏫
> > > > > > > > 
> > > > > > > > <div class="real">
> > > > > > > > 
> > > > > > > > 考场
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="code">
> > > > > > > > 
> > > > > > > > Env
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > "考场设在 Gibson 教学楼  
> > > > > > > > 坐下，开始答题"
> > > > > > > > 
> > > > > > > > ### Episode 的数据结构
> > > > > > > > 
> > > > > > > >     # 一个 Episode 就是一个 Python 对象。以 VLN 为例：
> > > > > > > >     class VLNEpisode:
> > > > > > > >         episode_id:    "r2r_001"            # 题目编号
> > > > > > > >         scene_id:      "mp3d/2azQ1b91cZZ" # 用哪个 3D 场景
> > > > > > > >         start_position: [1.5, 0.0, 3.2]   # Agent 出生 x,y,z
> > > > > > > >         start_rotation: [0, 0.707, 0, 0.707] # Agent 出生朝向 (四元数)
> > > > > > > >         goals:          [NavigationGoal(...)] # 目标位置（可有多个）
> > > > > > > >         instruction:    InstructionData(      # 【VLN 特有】自然语言指令
> > > > > > > >             instruction_text="Go past the couch and stop at the table"
> > > > > > > >         )
> > > > > > > >         reference_path: [[...], [...], ...]   # 【VLN 特有】地面真值路径
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > <div class="info-title" style="color:#6ee7b7;">
> > > > > > > > 
> > > > > > > > Dataset 的三类 Split
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > Habit 的每个数据集通常有三个 split，这是评估 AI 泛化能力的关键设计：  
> > > > > > > > **train** — 用来训练模型。场景 A、B、C 的 episodes。  
> > > > > > > > **val\_seen** — 场景和 train 一样（A、B、C），但 episodes（起终点组合）不同。测的是"同一个房子里，新路径会不会走"。  
> > > > > > > > **val\_unseen** — **完全不同的场景**（D、E、F），模型从未见过。测的是"去一个陌生房子，能走吗"。 这是 VLN 的核心挑战 — 大多数方法的 val\_unseen 比 val\_seen 低 10-20%。
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 第6章 · 训练全景 — RL/IL 如何嵌入这个体系
> > > > > > > > 
> > > > > > > > Habitat-Lab 定义"训什么"（任务+环境），Habitat-Baselines 定义"怎么训"（算法+模型）。两者通过 Env 接口连接。
> > > > > > > > 
> > > > > > > > ### 训练架构全景
> > > > > > > > 
> > > > > > > > <div class="arch-diagram">
> > > > > > > > 
> > > > > > > > <div class="arch-row">
> > > > > > > > 
> > > > > > > > <div class="arch-layer l-app" style="min-width:180px;">
> > > > > > > > 
> > > > > > > > 📜 Config (YAML) <span class="small">任务 + 算法 + 超参</span>
> > > > > > > > 
> > > > > > > > <div class="arch-arrow-center">
> > > > > > > > 
> > > > > > > > ↓
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="arch-row">
> > > > > > > > 
> > > > > > > > <div class="arch-layer l-core">
> > > > > > > > 
> > > > > > > > 🔌 VectorEnv <span class="small">N 个 Env 并行运行</span>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="arch-layer l-task">
> > > > > > > > 
> > > > > > > > 🎓 Trainer (PPO/IL) <span class="small">策略网络 + 优化器</span>
> > > > > > > > 
> > > > > > > > <div class="arch-arrow-center">
> > > > > > > > 
> > > > > > > > ↓
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="arch-row">
> > > > > > > > 
> > > > > > > > <div class="arch-layer l-sim" style="min-width:260px;">
> > > > > > > > 
> > > > > > > > Rollout → 收集 (obs, action, reward) → 更新策略 <span class="small">这个循环跑数百万次</span>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### 回到第 2 章的 `policy(obs)` — 策略到底是什么？
> > > > > > > > 
> > > > > > > > <div class="metaphor-box" style="border-color:#f59e0b30; background:linear-gradient(135deg, #f59e0b06, #0f172a);">
> > > > > > > > 
> > > > > > > > ### 核心概念：策略 = 大脑
> > > > > > > > 
> > > > > > > > 在第 2 章的 hello world 中，`policy(obs)` 被故意写成一个黑盒。 现在可以揭开它了：**策略 (Policy) 就是机器人的"决策大脑"**——输入传感器观测，输出动作。  
> > > > > > > >   
> > > > > > > > 在 Habitat 中，它**不是框架的一部分**，而是**你要训练或编写的代码**。训练的本质，就是用数据不断调整这个大脑的参数， 让它越来越擅长做出正确的决策。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="callout-grid">
> > > > > > > > 
> > > > > > > > <div class="callout">
> > > > > > > > 
> > > > > > > > <span class="big">🎲</span>
> > > > > > > > 
> > > > > > > > <div class="label">
> > > > > > > > 
> > > > > > > > 随机策略
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > `env.action_space.sample()`  
> > > > > > > > 每个动作等概率随机选  
> > > > > > > > 默认示例就用这个  
> > > > > > > > 不学习，纯随机探索
> > > > > > > > 
> > > > > > > > <div class="callout">
> > > > > > > > 
> > > > > > > > <span class="big">🧭</span>
> > > > > > > > 
> > > > > > > > <div class="label">
> > > > > > > > 
> > > > > > > > 最短路径 (手写规则)
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > `shortest_path_follower`  
> > > > > > > > 基于 A\* 算法的预置导航器  
> > > > > > > > 不需要训练，零样本可用  
> > > > > > > > 只能用于导航任务
> > > > > > > > 
> > > > > > > > <div class="callout">
> > > > > > > > 
> > > > > > > > <span class="big">🧠</span>
> > > > > > > > 
> > > > > > > > <div class="label">
> > > > > > > > 
> > > > > > > > RL 训练策略 (PPO)
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > `policy = CNN+RNN → Actor`  
> > > > > > > > 在环境中试错，用奖励信号学习  
> > > > > > > > 训练需要 GPU + 大量环境交互  
> > > > > > > > 泛化能力最强
> > > > > > > > 
> > > > > > > > <div class="callout">
> > > > > > > > 
> > > > > > > > <span class="big">👨‍🏫</span>
> > > > > > > > 
> > > > > > > > <div class="label">
> > > > > > > > 
> > > > > > > > IL 训练策略 (BC)
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="desc">
> > > > > > > > 
> > > > > > > > `policy = 模仿专家数据`  
> > > > > > > > 从人类演示中学习映射  
> > > > > > > > 不需要设计 reward 函数  
> > > > > > > > 适合难以定义奖励的任务
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > > 💡
> > > > > > > > > 
> > > > > > > > > <div class="tip-title">
> > > > > > > > > 
> > > > > > > > > 策略与 Env 的关系
> > > > > > > > > 
> > > > > > > > > 把 Env 想象成**游戏机**，策略是**玩家**：  
> > > > > > > > > · Env 提供 `reset()`（开局）和 `step(action)`（推进一帧）  
> > > > > > > > > · 策略提供 `policy(obs) → action`（看到画面，按下手柄）  
> > > > > > > > > · 训练就是把赢的录像（好的 state→action 对）拿出来反复学习  
> > > > > > > > >   
> > > > > > > > > Habitat 只提供"游戏机"（Env）和"训练教练"（Trainer），"玩家"（Policy）的结构由你设计—— **这就是模块化的力量**。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="module-grid" style="margin-top: 28px;">
> > > > > > > > > 
> > > > > > > > > <div class="module" style="border-left-color: var(--accent-rl);">
> > > > > > > > > 
> > > > > > > > > ### 🎮 强化学习 (PPO / DD-PPO)
> > > > > > > > > 
> > > > > > > > > AI 在环境中**试错**，收到奖励/惩罚信号。PPO 算法在当前策略附近做安全的策略改进。 DD-PPO 将其扩展到多 GPU/多节点的大规模并行训练。
> > > > > > > > > 
> > > > > > > > >   - **策略网络：**CNN (视觉编码) + RNN (状态记忆) → Actor/Critic 头
> > > > > > > > >   - **关键文件：**`habitat_baselines/rl/ppo/ppo_trainer.py`
> > > > > > > > >   - **VectorEnv：**同时运行多个 Env 实例，batch 收集经验
> > > > > > > > >   - **DD-PPO 的优雅设计：**各进程独立 rollout，梯度同步 — 几乎线性加速
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="module" style="border-left-color: var(--accent-challenge);">
> > > > > > > > > 
> > > > > > > > > ### 👨‍🏫 模仿学习 (BC / DAgger)
> > > > > > > > > 
> > > > > > > > > 从**专家示范**中学习 — 不需要设计 reward 函数。类似于"看老师做一遍，然后自己做"。 DAgger 是改进版：训练中定期让专家纠正 AI 的累积误差。
> > > > > > > > > 
> > > > > > > > >   - **核心概念：**分布漂移 (Distribution Shift) — AI 偏离专家路径后越走越偏
> > > > > > > > >   - **关键文件：**`habitat_baselines/il/trainers/`
> > > > > > > > >   - **与 RL 的互补：**IL 提供好的初始化 → RL 微调（IL+RL 混合）
> > > > > > > > > 
> > > > > > > > > > 💡
> > > > > > > > > > 
> > > > > > > > > > <div class="tip-title">
> > > > > > > > > > 
> > > > > > > > > > 学习建议
> > > > > > > > > > 
> > > > > > > > > > 如果你是第一次接触训练，**从 PointNav + PPO 开始**。这是最成熟的组合，社区讨论最多， 出错时最容易找到解决方案。不要一开始就碰 VLN 训练 — 它的奖励稀疏、收敛困难， 应该在你熟练掌握 PPO 的基本调参后再挑战。
> > > > > > > > > > 
> > > > > > > > > > <div class="section">
> > > > > > > > > > 
> > > > > > > > > > <div class="container">
> > > > > > > > > > 
> > > > > > > > > > ## 第7章 · Sim-to-Real — 从仿真到真机
> > > > > > > > > > 
> > > > > > > > > > 这是 Habit 架构最精妙的设计之一。理解了它，你就理解了"抽象"的力量。
> > > > > > > > > > 
> > > > > > > > > > <div class="metaphor-box" style="border-color:#06b6d430; background:linear-gradient(135deg, #06b6d406, #0f172a);">
> > > > > > > > > > 
> > > > > > > > > > ### 核心洞察：Simulator 只是一个"抽象接口"
> > > > > > > > > > 
> > > > > > > > > > Habitat 定义了一个 `Simulator` 抽象基类，要求所有后端实现 `reset()` / `step()` / `get_agent_state()` 等统一方法。 **Habitat-Sim**（3D 渲染引擎）和 **PyRobot**（真实机器人 ROS 驱动）都是这个基类的子类。  
> > > > > > > > > >   
> > > > > > > > > > 代码里有一句话精准概括了这一切：  
> > > > > > > > > > `"This abstraction assumes that reality is a simulation."`  
> > > > > > > > > > <span style="font-size:0.85rem; color:#64748b;">—— 这个抽象假设"现实也只是一个仿真器"。只要你实现了那几个方法，上层不在乎你下面是显卡还是真机。</span>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div style="background:#10b98110; border:1px solid #10b98130; border-radius:10px; padding:16px 20px; text-align:center; margin: 24px 0;">
> > > > > > > > > > 
> > > > > > > > > > <span style="color:#6ee7b7; font-weight:700;">只需改一行 YAML，无需改任何 Python 代码</span>  
> > > > > > > > > > `simulator.type = "Sim-v0"` <span style="color:var(--text-dim); margin:0 12px;">→</span> `simulator.type = "PyRobot-v0"`  
> > > > > > > > > > <span style="font-size:0.78rem; color:#64748b;">Env、Task、SensorSuite、策略模型 — 全部原封不动</span>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-box">
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > > > > > > > 
> > > > > > > > > > **仿真训练**
> > > > > > > > > > 
> > > > > > > > > > Habitat-Sim + GLB  
> > > > > > > > > > PPO/IL 训练策略
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-arrow">
> > > > > > > > > > 
> > > > > > > > > > →
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > > > > > > > 
> > > > > > > > > > **保存权重**
> > > > > > > > > > 
> > > > > > > > > > PyTorch checkpoint  
> > > > > > > > > > \+ 配置 YAML
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-arrow">
> > > > > > > > > > 
> > > > > > > > > > →
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > > > > > > > > 
> > > > > > > > > > **切换后端**
> > > > > > > > > > 
> > > > > > > > > > Sim-v0 → PyRobot-v0  
> > > > > > > > > > 改一行配置
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-arrow">
> > > > > > > > > > 
> > > > > > > > > > →
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > > > > > > > 
> > > > > > > > > > **真机推理**
> > > > > > > > > > 
> > > > > > > > > > env.step() 驱动  
> > > > > > > > > > 真实硬件
> > > > > > > > > > 
> > > > > > > > > > > 💡
> > > > > > > > > > > 
> > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > 
> > > > > > > > > > > 🚀 准备好了？跳到真机部署
> > > > > > > > > > > 
> > > > > > > > > > > 第7章讲的是 Habitat 框架级的 Sim-to-Real 抽象（切换 Simulator 后端）。如果你想了解 **具体怎么在 Spark-I 或 Leo 机器人上跑 VLN（视觉语言导航）**——包括两种实战方案 （VLN+ROS Nav2 和 VLM 端到端），请直接跳到主线教程的部署轨： [第6章 · VLN 仿真训练 →](habitat-textbook-step6.html) [第7章 · 方法一：VLN+ROS →](habitat-textbook-step7.html) [第8章 · 方法二：VLM 端到端 →](habitat-textbook-step8.html)
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 第8章 · 动手路线图 — 从零到部署
> > > > > > > > > > > 
> > > > > > > > > > > 前面的章节帮你建立了"这是什么"的心智模型。这一章把所有内容串成一条可执行的学习路径： **认知轨**（Steps 1–5，认识 Habitat 平台） → **训练轨**（第6章，学会 RL 训练） → **部署轨**（Steps 7–8，将模型部署到真实机器人） → **进阶轨**（第9章，Habitat 2.0 交互式操作）。
> > > > > > > > > > > 
> > > > > > > > > > > <div style="margin-bottom: 8px; font-size: 0.82rem; font-weight: 700; color: #60a5fa;">
> > > > > > > > > > > 
> > > > > > > > > > > 🔬 认知轨：认识 Habitat 平台
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-flow">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">🏗️</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 安装环境
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > conda + habitat-sim  
> > > > > > > > > > > \+ habitat-lab
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">▶️</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 跑通示例
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > example.py  
> > > > > > > > > > > interactive\_play
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">📖</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 读核心代码
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > core/ 目录  
> > > > > > > > > > > 5 个模块精读
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">⚙️</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 改配置实验
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > 换传感器、任务  
> > > > > > > > > > > 注册自定义 Sensor
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">🗺️</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 导航任务全景
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > 5种导航任务  
> > > > > > > > > > > PointNav→VLN
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">🎓</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > RL 训练入门
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > PointNav+PPO  
> > > > > > > > > > > 理解训练循环
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div style="text-align: center; margin: 20px 0;">
> > > > > > > > > > > 
> > > > > > > > > > > <span style="display: inline-block; background: linear-gradient(135deg, #14b8a620, #a78bfa20); border: 1px solid #14b8a640; border-radius: 16px; padding: 8px 24px; font-size: 0.85rem; font-weight: 700; color: #2dd4bf;">🔀 分岔口：进入 VLN 专线 + 部署轨</span>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div style="margin-bottom: 8px; font-size: 0.82rem; font-weight: 700; color: #2dd4bf;">
> > > > > > > > > > > 
> > > > > > > > > > > 🤖 部署轨：VLN + 真机
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-flow">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step" style="border-top: 3px solid #14b8a6;">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">🧭</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > VLN 视觉语言导航
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > IL→诊断→DAgger  
> > > > > > > > > > > →微调→部署
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-arrow">
> > > > > > > > > > > 
> > > > > > > > > > > →
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="path-step" style="border-top: 3px solid #a78bfa;">
> > > > > > > > > > > 
> > > > > > > > > > > <span class="step-icon">🤖</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-label">
> > > > > > > > > > > 
> > > > > > > > > > > 真机部署
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="step-desc">
> > > > > > > > > > > 
> > > > > > > > > > > VLN+ROS  
> > > > > > > > > > > \+ VLM 端到端
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module-grid" style="margin-top: 32px;">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #64748b;">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第1章：安装环境 (1-2天)  [📖 详细教程 →](habitat-textbook-step1.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - 创建 conda 环境 (Python 3.9 + cmake)
> > > > > > > > > > >   - 安装 habitat-sim (conda install)
> > > > > > > > > > >   - pip install -e habitat-lab
> > > > > > > > > > >   - **验证：**`python -c "import habitat; print('OK')"`
> > > > > > > > > > >   - 下载测试数据：`habitat_test_scenes`
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #10b981;">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第1B章：完整数据集下载 (半天)  [📖 详细教程 →](habitat-textbook-step1b.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **7 种场景数据集**：Gibson / MP3D / HM3D / ReplicaCAD 对比
> > > > > > > > > > >   - **6 种任务数据集**：PointNav / ObjectNav / VLN / Rearrange
> > > > > > > > > > >   - 获取流程：官网申请 → 签署协议 → 下载解压
> > > > > > > > > > >   - **目录规范：**`data/scene_datasets/` vs `data/datasets/`
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-core);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第2章：跑通示例 (1天)  [📖 详细教程 →](habitat-textbook-step2.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - 跑 `examples/example.py` — 理解 step/reset
> > > > > > > > > > >   - 跑 `examples/interactive_play.py` — 用键盘控制 Agent
> > > > > > > > > > >   - 跑 `examples/benchmark.py` — 看评估输出
> > > > > > > > > > >   - **目标：**亲眼看到 3D 场景 + Agent 移动
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-task);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第3章：读核心代码 (3-5天)  [📖 详细教程 →](habitat-textbook-step3.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **Day 1：**registry.py → sensor.py → simulator.py
> > > > > > > > > > >   - **Day 2：**agent.py → embodied\_task.py → env.py
> > > > > > > > > > >   - **Day 3：**tasks/nav/nav.py（完整 step 调用链）
> > > > > > > > > > >   - **Day 4：**sims/habitat\_simulator/（渲染后端）
> > > > > > > > > > >   - **方法：**边读边画调用图，不追求全懂
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-config);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第4章：改配置实验 (2-3天)
> > > > > > > > > > > 
> > > > > > > > > > >   - 修改 RGB 分辨率 / HFOV → 观察输出变化
> > > > > > > > > > >   - 添加/移除传感器（加 Depth、去 Compass）
> > > > > > > > > > >   - 注册一个自定义 Sensor（如 LiDAR 模拟）
> > > > > > > > > > >   - 创建自己的 benchmark YAML
> > > > > > > > > > >   - **目标：**不写核心代码就能改变实验行为
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #a78bfa;">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第5章：导航任务全景 (半天)  [📖 详细教程 →](habitat-textbook-step5.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **5种导航任务全景**：PointNav / ObjectNav / ImageNav / InstanceNav / VLN
> > > > > > > > > > >   - 对比表：目标表示、传感器、动作空间、数据集
> > > > > > > > > > >   - 术语速查：RL / IL / 观测 / 动作 / 奖励 等核心概念
> > > > > > > > > > >   - **目标：**在训练之前，先知道 Habitat 能解决什么问题
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-rl);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第6章：RL 训练入门 (1-2周)  [📖 详细教程 →](habitat-textbook-step6.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **Day 1-2：**PointNav + PPO 训练（抄官方配置）
> > > > > > > > > > >   - **Day 3-4：**理解训练循环：Rollout → PPO更新 → 评估
> > > > > > > > > > >   - **Day 5-7：**调参实验（lr、entropy、num\_envs）
> > > > > > > > > > >   - **目标：**能看懂 TensorBoard 曲线并解释
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #f59e0b;">
> > > > > > > > > > > 
> > > > > > > > > > > ### 附录：DD-PPO 分布式训练 (半天)  [📖 详细教程 →](habitat-textbook-step5b.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **原理：**PPO vs DD-PPO 架构对比、分布式梯度同步
> > > > > > > > > > >   - **配置：**`trainer_name: ddppo` + 关键参数含义
> > > > > > > > > > >   - **运行：**`torchrun --nproc_per_node N` 单机多卡启动
> > > > > > > > > > >   - **排错：**NCCL 超时、OOM、preemption、端口冲突
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-tip);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第7章：VLN 视觉语言导航 (2-3周)  [📖 详细教程 →](habitat-textbook-step7.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **7-1\~7-3：**VLN 理论 → 配置 → IL 训练 → SR≈32%
> > > > > > > > > > >   - **7-4：**避坑诊断 — CLIP实验、行为漂移分析
> > > > > > > > > > >   - **7-5：**DAgger 桥梁 — IL 32% → DAgger 50% → RL 55%+
> > > > > > > > > > >   - **7-6\~7-7：**JanusVLN SOTA + LoRA 微调 + 数据采集
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #a78bfa;">
> > > > > > > > > > > 
> > > > > > > > > > > ### 第8章：真机部署 (2-3周)  [📖 详细教程 →](habitat-textbook-step8.html)
> > > > > > > > > > > 
> > > > > > > > > > >   - **方案一（8-1\~8-6）：**VLN → 子目标 → ROS Nav2 执行
> > > > > > > > > > >   - **方案二（8-7\~8-10）：**VLM 端到端，无地图导航
> > > > > > > > > > >   - Spark-I (ROS Noetic) / Leo (ROS 2 Humble) 适配
> > > > > > > > > > >   - **目标：**两种方案对比，选最适合你的部署方式
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: #ec4899;">
> > > > > > > > > > > 
> > > > > > > > > > > > 💡
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > > 
> > > > > > > > > > > > 最重要的学习原则
> > > > > > > > > > > > 
> > > > > > > > > > > > **不要试图一次性理解所有代码。**Habitat 代码库几万行，但核心骨架 (`core/`) 不到两千行。 这五章内容你不需要逐行背下来 — 把这篇教程当作**地图**。当你迷路时，回到这里， 找到你所在的"模块"，然后重新定向。每个模块都独立、自洽、可单独理解。 掌握一个再攻下一个，你会发现自己进步得比想象中快得多。
> > > > > > > > > > > > 
> > > > > > > > > > > > **部署轨提示：**方案一（VLN+ROS）和方案二（VLM端到端）是**并行可选**的两种方案。如果你熟悉 ROS 且有现成的导航栈， 从方法一开始更稳妥；如果你更偏 CV/ML 背景且想探索前沿，方法二可能更适合你。 当然，两者都学是最好的选择。
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
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
> 
> </div>
> 
> </div>
> 
>
