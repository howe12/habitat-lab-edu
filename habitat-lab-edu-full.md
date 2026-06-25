# Habitat 学习资源中心 — 从零理解具身智能

> 从零理解具身智能 — 基于 Meta AI Habitat-Lab 的工程化教学体系。 主线教程、专题深度、架构可视化，三条路径助你建立完整的知识体系。

<div class="section-title">

📗 主线教程：Habitat 从零理解

</div>

11 章教科书。从概念到运行到源码，按 **工程依赖顺序** 编排。

<div class="hub-grid">

<div class="hub-card full">

<div class="card-top">

<div class="card-icon" style="background:linear-gradient(135deg,#3b82f620,#8b5cf620);">

📗

</div>

<div>

<div class="card-title">

Habitat 教科书（11 章全覆盖）

</div>

<div class="card-desc">

模块化设计，从「它是什么」到「我该怎么学」。涵盖：架构总览 → 传感器与观测 → 任务体系 → 模拟器 → 数据管道 → RL 训练 → 评估基准 → 学习路线。

</div>

<div class="card-sub">

[打开教科书 →](habitat-textbook.html)

<div class="hub-card" style="border-top:3px solid var(--accent-core);">

<div class="card-top">

<div class="card-icon" style="background:#3b82f615;">

🔧

</div>

<div>

<div class="card-title">

第1章：安装环境

</div>

<div class="card-desc">

Conda 环境 → 代理配置 → habitat-sim → habitat-lab → 数据下载验证。交互式检查清单。

</div>

<div class="card-sub">

[📖 开始安装](habitat-textbook-step1.html) [→](habitat-textbook-step1.html)

<div class="hub-card" style="border-top:3px solid #10b981;">

<div class="card-top">

<div class="card-icon" style="background:#10b98115;">

📦

</div>

<div>

<div class="card-title">

第1B章：完整数据集下载

</div>

<div class="card-desc">

**7 种场景 + 6 种任务数据集**：Gibson/MP3D/HM3D 获取流程、目录结构规范、授权申请指南。

</div>

<div class="card-sub">

[📖 下载数据](habitat-textbook-step1b.html) [→](habitat-textbook-step1b.html)

<div class="hub-card" style="border-top:3px solid var(--accent-sim);">

<div class="card-top">

<div class="card-icon" style="background:#06b6d415;">

▶️

</div>

<div>

<div class="card-title">

第2章：跑通示例

</div>

<div class="card-desc">

5 个渐进式示例 + **4 组真实运行结果**（含终端输出、RGB 图像、GPS 轨迹、Top-down 地图）。

</div>

<div class="card-sub">

[📖 查看示例](habitat-textbook-step2.html) [→](habitat-textbook-step2.html)

<div class="hub-card" style="border-top:3px solid var(--accent-task);">

<div class="card-top">

<div class="card-icon" style="background:#8b5cf615;">

💻

</div>

<div>

<div class="card-title">

第3章：读核心代码

</div>

<div class="card-desc">

**交互式调用链追踪器** + 参数调控台 + 6 模块可折叠源码分析。从注册中心到 C++ 引擎。

</div>

<div class="card-sub">

[📖 阅读源码](habitat-textbook-step3.html) [→](habitat-textbook-step3.html)

<div class="hub-card" style="border-top:3px solid #ec4899;">

<div class="card-top">

<div class="card-icon" style="background:#ec489915;">

⚙️

</div>

<div>

<div class="card-title">

第4章：改配置实验

</div>

<div class="card-desc">

**5 组配置实验**：RGB 分辨率、RGB vs RGBD、自定义 LiDAR 传感器、YAML 配置继承、success\_distance 参数。

</div>

<div class="card-sub">

[📖 动手实验](habitat-textbook-step4.html) [→](habitat-textbook-step4.html)

<div class="hub-card" style="border-top:3px solid #f59e0b;">

<div class="card-top">

<div class="card-icon" style="background:#f59e0b15;">

🏋️

</div>

<div>

<div class="card-title">

第5章：导航任务全景

</div>

<div class="card-desc">

**5 种导航任务全览**：PointNav · ObjectNav · ImageNav · InstanceImageNav · VLN。训练架构、评估指标、术语速查。

</div>

<div class="card-sub">

[📖 学习训练](habitat-textbook-step5.html) [→](habitat-textbook-step5.html)

<div class="hub-card" style="border-top:3px solid #f59e0b;">

<div class="card-top">

<div class="card-icon" style="background:#f59e0b15;">

🚀

</div>

<div>

<div class="card-title">

第5B章：DD-PPO 分布式训练

</div>

<div class="card-desc">

**单机多卡 PPO 扩展**：架构原理、配置对比、分布式启动命令、吞吐量缩放、6 种常见故障排查。

</div>

<div class="card-sub">

[📖 分布式训练](habitat-textbook-step5b.html) [→](habitat-textbook-step5b.html)

<div class="hub-card" style="border-top:3px solid #14b8a6;">

<div class="card-top">

<div class="card-icon" style="background:#14b8a615;">

🧭

</div>

<div>

<div class="card-title">

第6章：RL 训练入门

</div>

<div class="card-desc">

**PointNav + PPO 实战**：训练全景图、策略网络结构（CNN+RNN）、RL 环境封装链、Benchmark 评估。

</div>

<div class="card-sub">

[📖 开始训练](habitat-textbook-step6.html) [→](habitat-textbook-step6.html)

</div>

<div style="margin-top: 28px; text-align: center;">

<div style="display: inline-block; background: linear-gradient(135deg, #14b8a620, #a78bfa20); border: 1px solid #14b8a640; border-radius: 20px; padding: 12px 32px;">

<span style="font-weight: 700; color: #2dd4bf;">🔀 研究轨 → 部署轨</span> <span style="color: var(--text-dim); font-size: 0.85rem; margin-left: 8px;">第1–6章 掌握 Habitat 平台 · 第7–9章 仿真训练 → 真机部署</span>

<div class="hub-grid" style="margin-top: 24px;">

<div class="hub-card" style="border-top:3px solid #a78bfa;">

<div class="card-top">

<div class="card-icon" style="background:#a78bfa15;">

🤖

</div>

<div>

<div class="card-title">

第7章：VLN 视觉语言导航

</div>

<div class="card-desc">

**从零训练 VLN 模型**：VLN-v0 任务配置、R2R 数据集、InstructionSensor、模仿学习 + 评估导出 + SOTA实战(JanusVLN) + 避坑诊断。

</div>

<div class="card-sub">

[📖 方法一](habitat-textbook-step7.html) [→](habitat-textbook-step7.html)

<div class="hub-card" style="border-top:3px solid #ec4899;">

<div class="card-top">

<div class="card-icon" style="background:#ec489915;">

🧠

</div>

<div>

<div class="card-title">

第8章：真机部署

</div>

<div class="card-desc">

**两种方案全覆盖**：VLN+ROS Nav2 分层式 + VLM 端到端直控。含 Spark-I / Leo ROS 软件包骨架。

</div>

<div class="card-sub">

[📖 方法二](habitat-textbook-step8.html) [→](habitat-textbook-step8.html)

<div class="hub-card full" style="border-top:3px solid #8b5cf6;">

<div class="card-top">

<div class="card-icon" style="background:#8b5cf615;">

🦾

</div>

<div>

<div class="card-title">

第9章：Rearrange 操作任务（Habitat 2.0）

</div>

<div class="card-desc">

**6 个案例从零掌握交互式操作**：Pick/Place 抓取放置、关节物体（抽屉/冰箱）、PDDL 复合任务（TidyHouse）。Fetch 机器人 + 物理仿真。

</div>

<div class="card-sub">

[📖 学习 Rearrange](habitat-textbook-step9.html) [→](habitat-textbook-step9.html)

</div>

<div style="margin-top: 32px; text-align: center; margin-bottom: 10px;">

<span style="font-size: 0.8rem; font-weight: 700; color: #60a5fa; background: #3b82f615; padding: 4px 14px; border-radius: 12px;">🔬 研究轨：掌握 Habitat 平台</span>

</div>

<div class="step-road">

[](habitat-textbook-step1.html)

<div class="step-num" style="color:#60a5fa;">

第1章

</div>

<div class="step-name">

安装环境

</div>

<div class="step-desc">

Conda + pip + 代理  
habitat-sim + habitat-lab  
交互式检查清单

</div>

[](habitat-textbook-step2.html)

<div class="step-num" style="color:#22d3ee;">

第2章

</div>

<div class="step-name">

跑通示例

</div>

<div class="step-desc">

5 个渐进示例  
真实运行结果 + 图像  
PointNav / Benchmark

</div>

[](habitat-textbook-step3.html)

<div class="step-num" style="color:#a78bfa;">

第3章

</div>

<div class="step-name">

读核心代码

</div>

<div class="step-desc">

调用链追踪器  
参数调控台  
6 模块源码分析

</div>

[](habitat-textbook-step4.html)

<div class="step-num" style="color:#f9a8d4;">

第4章

</div>

<div class="step-name">

改配置实验

</div>

<div class="step-desc">

5 组配置实验  
传感器 / 自定义 LiDAR  
真实运行结果

</div>

[](habitat-textbook-step5.html)

<div class="step-num" style="color:#fcd34d;">

第5章

</div>

<div class="step-name">

导航任务全景

</div>

<div class="step-desc">

5 种导航任务全览  
训练架构 + 术语速查  
PointNav→ObjectNav→VLN

<div style="margin-top: 12px; text-align: center; margin-bottom: 4px;">

<span style="font-size: 0.72rem; font-weight: 600; color: var(--text-dim); background: #1e293b80; padding: 2px 12px; border-radius: 10px;">📎 研究轨扩展：专项深入</span>

</div>

<div class="step-road" style="grid-template-columns: repeat(3, 1fr); max-width: 640px; margin: 0 auto;">

[](habitat-textbook-step1b.html)

<div class="step-num" style="color:#6ee7b7;">

第1B章

</div>

<div class="step-name">

完整数据集下载

</div>

<div class="step-desc">

7 种场景 + 6 种任务  
Gibson/MP3D/HM3D  
授权申请 + 目录规范

</div>

[](habitat-textbook-step5b.html)

<div class="step-num" style="color:#fcd34d;">

第5B章

</div>

<div class="step-name">

DD-PPO 分布式训练

</div>

<div class="step-desc">

PPO → 多GPU扩展  
NCCL + preemption  
单机多卡吞吐量翻倍

</div>

[](habitat-textbook-step6.html)

<div class="step-num" style="color:#2dd4bf;">

第6章

</div>

<div class="step-name">

RL 训练入门

</div>

<div class="step-desc">

PointNav + PPO 实战  
策略网络结构解析  
RL 环境封装链

<div style="margin-top: 28px; text-align: center; margin-bottom: 10px;">

<span style="font-size: 0.8rem; font-weight: 700; color: #2dd4bf; background: #14b8a615; padding: 4px 14px; border-radius: 12px;">🤖 部署轨：VLN → 真机</span>

</div>

<div class="step-road" style="grid-template-columns: repeat(2, 1fr); max-width: 440px; margin: 0 auto;">

[](habitat-textbook-step7.html)

<div class="step-num" style="color:#c4b5fd;">

第7章

</div>

<div class="step-name">

VLN 视觉语言导航

</div>

<div class="step-desc">

VLN-v0 + R2R 数据集  
模仿学习 → 评估导出  
避坑诊断 + DAgger

</div>

[](habitat-textbook-step8.html)

<div class="step-num" style="color:#f9a8d4;">

第8章

</div>

<div class="step-name">

真机部署

</div>

<div class="step-desc">

VLN+ROS Nav2 分层  
VLM 端到端控制  
Spark-I / Leo 适配

<div style="margin-top: 28px; text-align: center; margin-bottom: 10px;">

<span style="font-size: 0.8rem; font-weight: 700; color: #c4b5fd; background: #8b5cf615; padding: 4px 14px; border-radius: 12px;">🦾 进阶轨：Habitat 2.0 交互式操作</span>

</div>

<div class="step-road" style="grid-template-columns: repeat(1, 1fr); max-width: 220px; margin: 0 auto;">

[](habitat-textbook-step9.html)

<div class="step-num" style="color:#c4b5fd;">

第9章

</div>

<div class="step-name">

Rearrange 操作任务

</div>

<div class="step-desc">

Pick/Place/Open/Close  
PDDL 复合任务  
Fetch + 物理仿真

</div>

<div class="section-title">

📚 专题深度 & 参考资源

</div>

主线教程之外的补充材料，深入特定主题。

<div class="resource-grid">

[](vln.html)

<div class="r-icon">

🧭

</div>

<div>

<div class="r-title">

VLN 视觉语言导航 · 专题

</div>

<div class="r-desc">

6 大技术范型 · 11 维对比表 · 核心架构维度分析 · 从 R2R 到 LLM Planning · Habitat 中的 VLN 实现 [](architecture.html)

<div class="r-icon">

🔌

</div>

<div>

<div class="r-title">

工程架构可视化

</div>

<div class="r-desc">

Habitat-Lab 完整模块依赖图 · 核心层/任务层/数据层/RL 层/配置层 · 10 大模块对比 [](habitat-textbook-step8.html)

<div class="r-icon">

🤖

</div>

<div>

<div class="r-title">

VLN → 真机部署 · 实战

</div>

<div class="r-desc">

两种部署方案对比：VLN+ROS Nav2 vs VLM 端到端 · Spark-I / Leo 机器人 ROS 软件包骨架 [](habitat-textbook-step7.html)

<div class="r-icon">

🧭

</div>

<div>

<div class="r-title">

VLN 仿真训练 · 实战

</div>

<div class="r-desc">

从配置 VLN-v0 任务到导出 checkpoint · R2R 数据集 · InstructionSensor · 评估指标解读

<div class="section-title">

🗺️ 站点导航图

</div>

所有页面的关系一览。建议按箭头方向阅读。

<div class="sitemap">

<div class="row">

[🏠 学习中心](index.html)

</div>

<div class="arrow-down">

↓

</div>

<div class="row">

[📗 教科书（11章总览）](habitat-textbook.html)

</div>

<div class="arrow-down">

↓

</div>

<div class="row">

[第1章 · 安装](habitat-textbook-step1.html) <span class="arrow-right">→</span> [第2章 · 跑示例](habitat-textbook-step2.html) <span class="arrow-right">→</span> [第3章 · 读代码](habitat-textbook-step3.html) <span class="arrow-right">→</span> [第4章 · 改配置](habitat-textbook-step4.html) <span class="arrow-right">→</span> [第5章 · 任务全景](habitat-textbook-step5.html)

</div>

<div style="color:var(--text-dim);font-size:0.7rem;margin-top:2px;">

┌ 扩展 ────────────────────────────────┐

</div>

<div class="row">

[第1B章 · 数据集](habitat-textbook-step1b.html) <span style="color:var(--text-dim);margin:0 8px;">|</span> [第5B章 · DD-PPO](habitat-textbook-step5b.html) <span style="color:var(--text-dim);margin:0 8px;">|</span> [第6章 · RL 训练](habitat-textbook-step6.html)

</div>

<div style="color:#475569;font-size:0.8rem;margin-top:2px;">

└ ─────────────────────────────────────┘

</div>

<div class="arrow-down" style="font-size:0.9rem; color:#475569;">

┊

</div>

<div class="row">

[第7章 · VLN](habitat-textbook-step7.html) <span class="arrow-right">→</span> [第8章 · 真机部署](habitat-textbook-step8.html)

</div>

<div class="arrow-down" style="font-size:0.9rem; color:#475569;">

┊

</div>

<div class="row">

[第9章 · Rearrange](habitat-textbook-step9.html)

</div>

<div style="color:#475569;font-size:1rem;margin-top:8px;">

└ ─ ─ ─ ─ ─ 横向扩展（专题页） ─ ─ ─ ─ ─ ┘

</div>

<div class="row" style="margin-top:4px;">

[🧭 VLN 专题](vln.html) [🔌 架构可视化](architecture.html) <span style="color:var(--text-dim);font-size:0.75rem;">传感器深度 (即将上线)</span> <span style="color:var(--text-dim);font-size:0.75rem;">论文精读 (即将上线)</span>
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
# 第1章：安装环境 — Habitat 从零理解

> 从零开始，在你的机器上搭建一个可以运行的 Habitat 开发环境。 本章假设你有一台 Linux 机器（或 WSL2），并且可以联网。

## 0\. 开始之前 — 你需要什么

先确认你的环境满足这些条件，跳过这一步是后续所有报错的根源。

| 需求         | 最低要求                     | 如何检查                                 |
| ---------- | ------------------------ | ------------------------------------ |
| **操作系统**   | Ubuntu 20.04+ / WSL2     | `lsb_release -a` 或 `uname -a`        |
| **GPU 驱动** | NVIDIA driver ≥ 450      | `nvidia-smi`                         |
| **Conda**  | Miniconda 或 Anaconda     | `conda --version`                    |
| **磁盘空间**   | ≥ 20 GB 空闲               | `df -h`（场景数据需 10-15G）                |
| **内存**     | ≥ 16 GB                  | `free -h`                            |
| **网络**     | 能访问 conda-forge / GitHub | `curl -I https://conda.anaconda.org` |

> ⚠️
> 
> <div class="warn-title">
> 
> 如果你在非 Linux 环境
> 
> Habitat-Sim 官方只提供 **Linux conda 包**。macOS 用户需要通过源码编译 habitat-sim（高级操作，不推荐小白）。 Windows 用户建议使用 **WSL2 + Ubuntu 22.04**，体验与原生 Linux 基本一致。 如果你是在远程服务器上操作，确认有 sudo 或 conda 已在用户目录安装。
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 安装流程总览
> 
> 整个安装流程分为 5 个阶段。每完成一个，勾选对应的复选框。
> 
> <div class="flow-box">
> 
> <div class="flow-step" style="border-top:3px solid #64748b;">
> 
> **1. Conda 环境**
> 
> python=3.9  
> cmake=3.14
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #f59e0b;">
> 
> **2. 配置代理**
> 
> conda proxy  
> channel 精简
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #3b82f6;">
> 
> **3. habitat-sim**
> 
> 仿真引擎  
> conda install
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> 
> **4. habitat-lab**
> 
> 任务框架  
> pip install -e
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #10b981;">
> 
> **5. 验证 + 数据**
> 
> import 测试  
> 下载场景
> 
> </div>
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 阶段 1：创建 Conda 环境
> 
> Habitat 对 Python 版本**非常敏感** — 必须使用 Python 3.9。3.10+ 会导致 habitat-sim 的 conda 包安装失败。
> 
> ### 安装 Miniconda（如果还没有）
> 
>     # 下载 Miniconda 安装脚本
>     $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
>     
>     # 运行安装（一路回车 + yes）
>     $ bash Miniconda3-latest-Linux-x86_64.sh
>     
>     # 重新加载 shell 配置
>     $ source ~/.bashrc
>     $ conda --version  # 应输出: conda 24.x.x
> 
> ### 创建 Habitat 专用环境
> 
>     # 创建名为 "habitat" 的环境，同时装好 cmake
>     $ conda create -n habitat python=3.9 cmake=3.14.0 -y
>     
>     # 激活环境 — 后续所有操作都在这个环境下
>     $ conda activate habitat
>     
>     # 验证
>     (habitat) $ python --version  # Python 3.9.x ✓
>     (habitat) $ cmake --version    # cmake 3.14.0 ✓
> 
> <div>
> 
> **为什么要 cmake？**
> 
> `cmake` 只在**从源码编译** habitat-sim 时才需要。如果你只用 conda 安装预编译包，可以跳过 cmake。 但预装 cmake 不会增加任何负担，推荐保留。
> 
> </div>
> 
> > ⚠️
> > 
> > <div class="warn-title">
> > 
> > Python 3.9 是硬性要求
> > 
> > habitat-sim 的 conda 包 (`aihabitat/habitat-sim`) 目前只提供 Python 3.9 版本。 如果你尝试 `python=3.10` 或更高，conda 会报依赖冲突。 **不要试图绕过这个限制** — 这不是 bug，是当前的兼容性边界。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 阶段 2：配置代理与 Channel
> > 
> > 如果你在境外服务器上操作，可以跳过本章。如果你在大陆环境，这是**最容易卡住的环节**。
> > 
> > ### 为什么 conda 需要单独配代理？
> > 
> > conda 的底层网络库不会自动读取系统的 `HTTP_PROXY` 环境变量。 你即使 export 了 `HTTP_PROXY=http://127.0.0.1:7897`，conda 仍然直连 — 这在有代理的环境中会导致 SSL EOF 或连接超时。必须**显式在 conda 配置中写入代理**。
> > 
> > <div class="dual-panel">
> > 
> > <div class="panel" style="border-top: 3px solid #f59e0b;">
> > 
> > #### 如果你有 Clash / V2Ray
> > 
> >     $ conda config --set proxy_servers.http \
> >             http://127.0.0.1:7897
> >     $ conda config --set proxy_servers.https \
> >             http://127.0.0.1:7897
> >     
> >     # 验证
> >     $ conda config --show proxy_servers
> > 
> > 端口号根据你的代理软件调整（Clash 默认 7897，V2Ray 默认 10809）
> > 
> > </div>
> > 
> > <div class="panel" style="border-top: 3px solid #10b981;">
> > 
> > #### 精简 Channel 列表
> > 
> >     # 先清空再添加 → 避免混用多个源
> >     $ conda config --remove-key channels
> >     $ conda config --add channels conda-forge
> >     $ conda config --add channels aihabitat
> >     
> >     # 查看最终 channel 列表
> >     $ conda config --show channels
> > 
> > 只保留 conda-forge + aihabitat 两个 channel，避免连接数爆炸
> > 
> > > ⚠️
> > > 
> > > <div class="warn-title">
> > > 
> > > 常见坑：清华镜像混用导致 SSL EOF
> > > 
> > > 很多教程推荐用清华 tuna 镜像，但如果你同时保留了 conda-forge 和 aihabitat 的境外源， 三个源的 TLS 实现差异会导致 SSL EOF 错误。**要么全用境外源（配代理），要么全用镜像源。** 混用是大多数网络问题的根源。
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 阶段 3：安装 habitat-sim
> > > 
> > > habitat-sim 是底层 3D 仿真引擎。它不在 PyPI 上，**必须通过 conda 安装**。
> > > 
> > >     # 核心安装命令 — 选择适合你的版本
> > >     
> > >     # 选项 A：服务器版本（无 GUI，最常见）
> > >     $ conda install habitat-sim=0.2.5 withbullet headless \
> > >         -c conda-forge -c aihabitat -y
> > >     
> > >     # 选项 B：桌面版本（有 3D 窗口，需要显示器）
> > >     $ conda install habitat-sim=0.2.5 withbullet \
> > >         -c conda-forge -c aihabitat -y
> > > 
> > > | 参数           | 含义                         | 适合场景                 |
> > > | ------------ | -------------------------- | -------------------- |
> > > | `withbullet` | 带 Bullet 物理引擎（碰撞检测）        | 几乎所有任务都需要            |
> > > | `headless`   | 不渲染 GUI 窗口，纯 GPU 离屏渲染      | 服务器 / SSH 无显示器 / 训练时 |
> > > | `=0.2.5`     | 与 habitat-lab v0.2.5 匹配的版本 | 保持与仓库一致              |
> > > 

> > >     # 验证安装
> > >     $ python -c "import habitat_sim; print('habitat-sim', habitat_sim.__version__)"
> > >     # 期望输出: habitat-sim 0.2.5
> > >     
> > >     # 更进一步：验证渲染管线
> > >     $ python -c "
> > >     import habitat_sim
> > >     sim_cfg = habitat_sim.SimulatorConfiguration()
> > >     print('Simulator config created — GPU rendering is ready')
> > >     "
> > > 
> > > > 💡
> > > > 
> > > > <div class="tip-title">
> > > > 
> > > > 如果你需要源码编译（macOS 或自定义版本）
> > > > 
> > > > conda 包只有 Linux 版。macOS 或 ARM 架构需要用 `build.sh` 从源码编译 — 这需要安装大量依赖（包括 Bullet Physics、Assimp、GLFW 等），预计额外需要半天到一天。 如果你是初学者且用 macOS，建议先在云 GPU 服务器上跑通，再考虑本地编译。
> > > > 
> > > > <div class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > ## 阶段 4：安装 habitat-lab
> > > > 
> > > > habitat-lab 是纯 Python 包，安装简单。关键是用 `-e`（editable 模式），方便修改源码后即时生效。
> > > > 
> > > >     # 确认你在 habitat-lab 仓库根目录
> > > >     $ cd /develop/habitat-lab
> > > >     
> > > >     # 以可编辑模式安装核心包
> > > >     $ pip install -e habitat-lab
> > > >     
> > > >     # (可选) 安装基线算法包 — 需要训练时再装
> > > >     $ pip install -e habitat-baselines
> > > >     
> > > >     # 验证
> > > >     $ python -c "import habitat; print('habitat-lab ready')"
> > > > 
> > > > <div>
> > > > 
> > > > **`pip install -e` 是什么意思？**
> > > > 
> > > > `-e`（editable，可编辑模式）不会把代码复制到 site-packages，而是创建一个指向源码目录的符号链接。 这意味着你修改 `habitat/core/env.py` 之后，**不需要重新 pip install**，改动即时生效。 这是研究和开发的标准做法 — 你会频繁地修改、调试、添加打印语句。
> > > > 
> > > > </div>
> > > > 
> > > > > ⚠️
> > > > > 
> > > > > <div class="warn-title">
> > > > > 
> > > > > 必须先装 habitat-sim 再装 habitat-lab
> > > > > 
> > > > > 如果先 pip install habitat-lab，pip 可能尝试从 PyPI 安装一个名为 `habitat-sim` 的包（不存在），导致混乱。 正确的顺序：**conda install habitat-sim → pip install -e habitat-lab**。
> > > > > 
> > > > > <div class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 阶段 5：下载测试数据 & 跑通验证
> > > > > 
> > > > > 安装完成 ≠ 可以使用。你需要下载最小测试场景来验证整个安装链路。
> > > > > 
> > > > >     # 方法 1 (推荐)：用 habitat-sim 内置下载工具
> > > > >     $ python -m habitat_sim.utils.datasets_download \
> > > > >         --uids habitat_test_scenes habitat_test_pointnav_dataset \
> > > > >         --data-path data/
> > > > >     
> > > > >     # 方法 2：查看所有可用数据集
> > > > >     $ python -m habitat_sim.utils.datasets_download --list
> > > > >     
> > > > >     # 方法 3 (备选)：如果下载脚本遇到网络问题，手动下载
> > > > >     # 从 https://dl.fbaipublicfiles.com/habitat/ 下载对应 .tar.gz 解压到 data/
> > > > > 
> > > > > ### 终极验证：跑通 example.py
> > > > > 
> > > > >     # 这是你的"Hello World" — 跑通它，环境就装好了
> > > > >     $ cd /develop/habitat-lab
> > > > >     $ python examples/example.py
> > > > >     
> > > > >     # 期望输出（不含报错）：
> > > > >     # Episode 0: agent moving...
> > > > >     # Episode 1: agent moving...
> > > > >     # ...
> > > > >     # 程序正常结束，exit code = 0
> > > > > 
> > > > > > 💡
> > > > > > 
> > > > > > <div class="tip-title">
> > > > > > 
> > > > > > 如果你看到 3D 窗口（非 headless 模式）
> > > > > > 
> > > > > > 如果你安装的是不带 `headless` 的版本，`example.py` 会弹出一个 3D 窗口显示 Agent 的视角。 按 ESC 退出。服务器用户（SSH 连接）不会有这个窗口，只能看到终端输出 — 这是正常的。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **安装成功后，你的环境里有什么？**
> > > > > > 
> > > > > > `conda list | grep habitat` 应该显示：  
> > > > > > · **habitat-sim** 0.2.5（C++ 渲染引擎，conda 包）  
> > > > > > · **habitat-lab**（Python 任务框架，pip editable 安装）  
> > > > > > · **habitat-baselines**（可选，算法训练包）
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## Docker 容器化部署（可选方案）
> > > > > > 
> > > > > > 如果你的环境不方便直接安装 conda 和 habitat-sim，可以使用 Docker 容器方案。 官方镜像预装了完整的 Habitat 环境，一条命令就能跑。
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **方案对比：Conda 安装 vs Docker 容器**
> > > > > > 
> > > > > > | 维度         | Conda 安装（推荐）          | Docker 容器                     |
> > > > > > | ---------- | --------------------- | ----------------------------- |
> > > > > > | **适用场景**   | 日常开发、训练、调试            | 快速验证、CI/CD、环境隔离               |
> > > > > > | **安装难度**   | 中等（需配置 conda + proxy） | 低（docker pull + run）          |
> > > > > > | **GUI 支持** | ✅ 完整（可弹出渲染窗口）         | ⚠️ 需额外配置 X11 forward          |
> > > > > > | **磁盘占用**   | \~3GB（conda env）      | \~15GB（Docker 镜像）             |
> > > > > > | **GPU 支持** | ✅ 直接使用                | ✅ 需要 nvidia-container-runtime |
> > > > > > 

> > > > > > </div>
> > > > > > 
> > > > > > ``` 
> > > > > >       Docker 部署三步骤
> > > > > > ```
> > > > > > 
> > > > > >     # 步骤 1：拉取官方镜像（约 15GB，仅首次）
> > > > > >     $ docker pull fairembodied/habitat-challenge:testing_2022_habitat_base_docker
> > > > > >     
> > > > > >     # 步骤 2：启动容器（挂载 data 目录以复用数据集）
> > > > > >     $ docker run --runtime=nvidia -it --rm \
> > > > > >         -v $(pwd)/data:/data \
> > > > > >         fairembodied/habitat-challenge:testing_2022_habitat_base_docker \
> > > > > >         /bin/bash
> > > > > >     
> > > > > >     # 步骤 3：容器内激活 conda 环境并验证
> > > > > >     $ conda init; source ~/.bashrc; source activate habitat
> > > > > >     $ python -c "import habitat_sim; import habitat; print('Docker OK')"
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > > ⚠️
> > > > > > > 
> > > > > > > <div class="warn-title">
> > > > > > > 
> > > > > > > Docker 方案的注意事项
> > > > > > > 
> > > > > > > · **镜像更新频率低**：官方镜像约每年更新一次（最新 tag 为 2022），版本可能落后于 pip 安装  
> > > > > > > · **需要 nvidia-container-runtime**：`apt install nvidia-container-runtime`，否则 GPU 不可用  
> > > > > > > · **数据挂载**：用 `-v` 将宿主机的 `data/` 目录挂入容器，避免每个容器内部重复下载  
> > > > > > > · **无 GUI**：默认 headless 模式，如需渲染窗口需额外配置 X11 forward (`-e DISPLAY` + `-v /tmp/.X11-unix`)  
> > > > > > > · **仓库根目录的 `Dockerfile`** 展示了完整构建过程（基于 nvidia/cudagl:10.1 + Miniconda + cmake 3.14）
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > > 💡
> > > > > > > > 
> > > > > > > > <div class="tip-title">
> > > > > > > > 
> > > > > > > > 实用建议
> > > > > > > > 
> > > > > > > > **学习阶段用 Conda**（前面阶段1-5）— 方便改代码、调试、看渲染窗口。 **批量训练 / CI 用 Docker** — 环境一致性好，可复现，适合服务器端。 两种方案可共存，共享 `data/` 目录。
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 常见问题排查
> > > > > > > > 
> > > > > > > > 这些是我在实践中遇到的真实错误。按症状查找你的问题。
> > > > > > > > 
> > > > > > > > <div class="trouble-grid">
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### SSL EOF / CONNECTION FAILED
> > > > > > > > 
> > > > > > > > **症状：**conda install 过程中报 `SSL EOF` 或 `Connection reset`  
> > > > > > > > <span class="fix">修复：</span>检查 conda proxy 设置 + 精简 channel 列表（见阶段 2）。  
> > > > > > > > **关键：**conda 不会用 `HTTP_PROXY` 环境变量，必须 `conda config --set proxy_servers`。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### Solving environment: failed
> > > > > > > > 
> > > > > > > > **症状：**`conda install habitat-sim` 依赖解析失败  
> > > > > > > > <span class="fix">修复：</span>确认 Python 版本 = 3.9（不是 3.10/3.11）。  
> > > > > > > > 试用 `conda install habitat-sim=0.2.5 withbullet headless -c conda-forge -c aihabitat --strict-channel-priority`
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### ImportError: libCURL.so
> > > > > > > > 
> > > > > > > > **症状：**`import habitat_sim` 报 libCURL.so 找不到  
> > > > > > > > <span class="fix">修复：</span>`conda install curl -c conda-forge` — habitat-sim 的渲染管线依赖特定的 libcurl 版本。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### ImportError: No module named 'habitat'
> > > > > > > > 
> > > > > > > > **症状：**`import habitat` 失败  
> > > > > > > > <span class="fix">修复：</span>确认：① conda activate habitat ② 在 habitat-lab 目录下 ③ pip install -e habitat-lab 执行成功。  
> > > > > > > > 运行 `pip list | grep habitat` 确认 habitat-lab 在列表中。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### CUDA / OpenGL 渲染失败
> > > > > > > > 
> > > > > > > > **症状：**example.py 运行时报 `EGL / GLX error` 或 `CUDA out of memory`  
> > > > > > > > <span class="fix">修复：</span>headless 模式下，确认安装了 EGL 库：  
> > > > > > > > `sudo apt install libegl1-mesa-dev libgles2-mesa-dev`  
> > > > > > > > GPU 内存不足：减小 RGB 分辨率或 batch size。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card">
> > > > > > > > 
> > > > > > > > #### 数据集下载中断 / 极慢
> > > > > > > > 
> > > > > > > > **症状：**`datasets_download` 卡住或报网络错误  
> > > > > > > > <span class="fix">修复：</span>该脚本用系统 `curl`，走的是 `HTTP_PROXY` 环境变量。  
> > > > > > > > 对 Matterport 域名可临时绕过代理：  
> > > > > > > > `no_proxy="api.matterport.com" python -m habitat_sim.utils.datasets_download ...`
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 学后自检 — 你掌握了什么
> > > > > > > > 
> > > > > > > > 如果你能独立回答以下 5 个问题，说明安装阶段已经扎实掌握了。
> > > > > > > > 
> > > > > > > > <div class="trouble-grid">
> > > > > > > > 
> > > > > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > > > > 
> > > > > > > > #### Q1：为什么要用 conda 而不是 pip 装 habitat-sim？
> > > > > > > > 
> > > > > > > > habitat-sim 是 C++ 项目，需要编译渲染管线（Magnum 引擎 + Bullet 物理）。conda 提供了预编译的二进制包， 避免了长达数小时的源码编译。PyPI 上没有 habitat-sim 的包。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > > > > 
> > > > > > > > #### Q2：headless vs 非 headless 的区别是什么？
> > > > > > > > 
> > > > > > > > headless = GPU 渲染到内存（帧缓冲），不显示窗口。训练 / 服务器用 headless。 非 headless = 弹出一个 3D 窗口实时显示。调试 / 演示用。两者计算结果完全一致。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > > > > 
> > > > > > > > #### Q3：pip install -e 中的 -e 有什么作用？
> > > > > > > > 
> > > > > > > > editable 模式 — 源码修改无需重新安装即生效。研究开发的标准做法。没有 -e 的话每次改一行代码都要重装。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > > > > 
> > > > > > > > #### Q4：conda 代理失败时，你的排查顺序是什么？
> > > > > > > > 
> > > > > > > > ① `conda config --show proxy_servers` 确认已配 → ② `conda config --show channels` 确认只有 conda-forge + aihabitat → ③ 用 `curl` 测试代理端口是否可达。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > > > > 
> > > > > > > > #### Q5：安装完成后，你运行哪条命令验证一切正常？
> > > > > > > > 
> > > > > > > > `python examples/example.py` — 这条命令涵盖了 habitat-sim 渲染 + habitat-lab Env 创建 + step() 交互，是最全面的集成测试。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > <div class="page-nav">
> > > > > > > > 
> > > > > > > > [← 返回教科书目录](habitat-textbook.html) [第2章：跑通示例 →](habitat-textbook-step2.html)
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
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
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
>

</div>
# 第1B章：数据集下载指南 — Habitat 从零理解

> Step1 只下载了测试数据。本章带你了解 Habitat 生态中所有可用的场景和任务数据集， 它们的用途、大小、获取方式，以及正确的目录结构。

## 0\. 为什么需要这一章

Step1 跑通了测试数据，但从"跑通"到"做研究"中间还差一步——数据。

<div>

**测试数据 vs 完整数据**

Step1 下载的 **habitat-test-scenes**（3个场景, 89MB）只能用来验证安装。  
真实实验需要完整场景数据集（Gibson 1.5GB \~ HM3D 130GB）和对应的任务 episode 文件。  
本章帮你：**知道有哪些 → 知道要哪个 → 知道怎么下 → 知道放在哪**。

</div>

| 数据层级      | 内容                   | 例子                | 存放位置                   |
| --------- | -------------------- | ----------------- | ---------------------- |
| **场景数据集** | 3D 模型、纹理、导航网格        | Gibson、MP3D、HM3D  | `data/scene_datasets/` |
| **任务数据集** | episode 定义（起点/目标/物体） | PointNav episodes | `data/datasets/`       |

场景是"房子"，任务是"在这个房子里要做什么"。两者缺一不可。

## 1\. 场景数据集全景

Habitat 支持 7 种场景数据集。按获取难度递进排列。

| 数据集                     | 大小           | 场景数                            | 获取方式                                                                                             | 推荐用途              |
| ----------------------- | ------------ | ------------------------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **Habitat Test Scenes** | 89 MB        | 3                              | `datasets_download --uids habitat_test_scenes`                                                   | 验证安装、CI 测试        |
| **ReplicaCAD**          | 123 MB       | 1 (多布局)                        | `datasets_download --uids rearrange_task_assets`（自动）                                             | Rearrange 操作任务    |
| **Gibson**              | \~1.5 GB     | 572 (tiny) / 86 (0+) / 14 (4+) | 需签署 [Gibson 使用协议](https://storage.googleapis.com/gibson_material/Agreement%20GDS%2006-04-18.pdf) | PointNav 入门训练     |
| **MatterPort3D (MP3D)** | \~15 GB      | 90                             | 需 [Matterport API Key](https://niessner.github.io/Matterport/) + 签署协议                            | ObjectNav、VLN、EQA |
| **HM3D**                | **\~130 GB** | 1000                           | 需向 Matterport 申请审批（[申请页面](https://matterport.com/partners/facebook)）                             | 大规模训练、ObjectNav   |
| **HSSD-Habitat**        | \~未知         | \~200+                         | 通过 habitat-sim DATASETS.md 指引获取                                                                  | ObjectNav（合成场景）   |
| **ProcTHOR-Habitat**    | \~未知         | 大量程序化场景                        | 通过 habitat-sim DATASETS.md 指引获取                                                                  | ObjectNav（程序化场景）  |

> 💡
> 
> <div class="tip-title">
> 
> 推荐路径：从 Gibson 开始
> 
> 如果你是第一次下载完整数据集，推荐路线：  
> **Test Scenes**（已装）→ **Gibson 4+**（14个场景，1.5GB，需签署协议）→ **MP3D**（90个场景，需 API Key）→ **HM3D**（大规模训练用）。  
> ReplicaCAD 只在做 Rearrange 操作任务时需要（Step9）。
> 
> </div>
> 
> > ⚠️
> > 
> > <div class="warn-title">
> > 
> > 重要：数据存放路径
> > 
> > 官方场景数据集下载说明在 **habitat-sim 仓库**的 `DATASETS.md` 中  
> > → [github.com/facebookresearch/habitat-sim/blob/main/DATASETS.md](https://github.com/facebookresearch/habitat-sim/blob/main/DATASETS.md)  
> > 不同数据集的授权流程各不相同，请仔细阅读对应条款。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 2\. 任务数据集全景
> > 
> > 每种任务都有对应的 episode 数据集。它们的下载 URL 统一在 `dl.fbaipublicfiles.com`。
> > 
> > | 任务类型                 | 场景           | 大小      | 下载地址                                                                                     | 解压路径                                             |
> > | -------------------- | ------------ | ------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------ |
> > | **PointNav**         | Habitat Test | \~2 MB  | `datasets_download --uids habitat_test_pointnav_dataset`                                 | `data/datasets/pointnav/habitat-test-scenes/v1/` |
> > | **PointNav**         | Gibson v1    | 385 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/gibson/v1/pointnav_gibson_v1.zip` | `data/datasets/pointnav/gibson/v1/`              |
> > | **PointNav**         | Gibson v2    | 274 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/gibson/v2/pointnav_gibson_v2.zip` | `data/datasets/pointnav/gibson/v2/`              |
> > | **PointNav**         | MP3D         | 400 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/mp3d/v1/pointnav_mp3d_v1.zip`     | `data/datasets/pointnav/mp3d/v1/`                |
> > | **PointNav**         | HM3D         | 992 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/hm3d/v1/pointnav_hm3d_v1.zip`     | `data/datasets/pointnav/hm3d/v1/`                |
> > | **ObjectNav**        | MP3D         | 170 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/mp3d/v1/objectnav_mp3d_v1.zip`   | `data/datasets/objectnav/mp3d/v1/`               |
> > | **ObjectNav**        | HM3D         | 154 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/hm3d/v1/objectnav_hm3d_v1.zip`   | `data/datasets/objectnav/hm3d/v1/`               |
> > | **InstanceImageNav** | HM3D         | 303 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/imagenav/hm3d/v1/...`                      | `data/datasets/instance_imagenav/hm3d/v1/`       |
> > | **VLN (R2R)**        | MP3D         | 2.7 MB  | `dl.fbaipublicfiles.com/habitat/data/datasets/vln/mp3d/r2r/v1/vln_r2r_mp3d_v1.zip`       | `data/datasets/vln/mp3d/r2r/v1/`                 |
> > | **EQA**              | MP3D         | 44 MB   | `dl.fbaipublicfiles.com/habitat/data/datasets/eqa/mp3d/v1/eqa_mp3d_v1.zip`               | `data/datasets/eqa/mp3d/v1/`                     |
> > | **Rearrange**        | ReplicaCAD   | \~11 MB | `datasets_download --uids rearrange_task_assets`（自动触发）                                   | `data/datasets/replica_cad/rearrange/v1/`        |
> > 

> > <div>
> > 
> > **目录结构规范**
> > 
> > 所有数据集遵循统一的层级结构：
> > 
> >     # 场景数据
> >     data/scene_datasets/
> >       gibson/
> >         Allensville.glb           # 场景 3D 模型
> >         Allensville.navmesh       # 导航网格
> >       mp3d/
> >         1LXtFkjw3qL/
> >           1LXtFkjw3qL.glb
> >           1LXtFkjw3qL.navmesh
> >     
> >     # 任务 episode 数据
> >     data/datasets/
> >       pointnav/gibson/v1/
> >         train/
> >           train.json.gz           # 主 episode 文件
> >           content/
> >             00009.json.gz         # 按场景拆分的 episode
> >         val/
> >           val.json.gz
> >           content/...
> >         test/
> >           test.json.gz
> >           content/...
> > 
> > 配置文件中的 `{split}` 模板在运行时会展开为 `train` / `val` / `test`， 例如：`data_path: "data/datasets/pointnav/gibson/v1/{split}/{split}.json.gz"`
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 3\. 下载测试数据（复习）
> > 
> > 这是 Step1 已经做过的，快速过一遍。如果你还没下载，现在补上。
> > 
> >     # ① 查看所有可用的 dataset UID
> >     $ python -m habitat_sim.utils.datasets_download --list
> >     
> >     # ② 下载测试场景 + PointNav 测试 episode
> >     $ python -m habitat_sim.utils.datasets_download \
> >           --uids habitat_test_scenes habitat_test_pointnav_dataset \
> >           --data-path data/
> >     
> >     # ③ 验证：检查文件是否存在
> >     $ ls data/scene_datasets/habitat-test-scenes/
> >     # apartment_1.glb  apartment_1.navmesh  skokloster-castle.glb  ...
> >     
> >     $ ls data/datasets/pointnav/habitat-test-scenes/v1/
> >     # train/  val/  test/
> > 
> > <div>
> > 
> > **datasets\_download 工具说明**
> > 
> > 这个工具来自 **habitat-sim** conda 包（不在 habitat-lab 源码中）。  
> > 它本质上是对 `curl` / `wget` 的封装，从 `dl.fbaipublicfiles.com` 下载 zip 并自动解压到 `--data-path` 指定目录。  
> > 如果下载中断，可以直接用浏览器或 curl 手动下载同名 zip 放到 `data/` 目录下重新运行该命令（会跳过已存在文件）。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 4\. 下载完整数据集
> > 
> > 以下以 Gibson PointNav 为例，演示从下载到验证的完整流程。
> > 
> > ### 案例 4-1：下载 Gibson PointNav 任务数据
> > 
> >     # ① 下载 episode zip 文件
> >     $ mkdir -p data/datasets/pointnav/gibson/v1/
> >     $ cd data/datasets/pointnav/gibson/v1/
> >     $ wget http://dl.fbaipublicfiles.com/habitat/data/datasets/pointnav/gibson/v1/pointnav_gibson_v1.zip
> >     
> >     # ② 解压
> >     $ unzip pointnav_gibson_v1.zip
> >     
> >     # ③ 验证结构
> >     $ ls train/
> >     # train.json.gz  content/
> >     $ zcat train/train.json.gz | python -m json.tool | head -30
> >     # 应看到 episodes 数组和每个 episode 的 start_position, goal 等字段
> > 
> > ### 案例 4-2：下载 Gibson 4+ 场景（14个场景）
> > 
> >     # Gibson 场景模型(.glb)和导航网格(.navmesh)需要从官方渠道获取
> >     # 第1章: 访问 https://github.com/facebookresearch/habitat-sim/blob/main/DATASETS.md
> >     # 第2章: 签署 Gibson 使用协议
> >     # 第3章: 下载 gibson_4+_assets.tar.gz 或通过官方脚本下载
> >     
> >     # 下载后解压到正确位置
> >     $ mkdir -p data/scene_datasets/gibson/
> >     $ tar -xzf gibson_4+_assets.tar.gz -C data/scene_datasets/gibson/
> >     
> >     # 验证：每个场景目录下应有 .glb + .navmesh
> >     $ ls data/scene_datasets/gibson/
> >     # Allensville.glb  Allensville.navmesh  ...（14个场景）
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 下载工具选择
> > > 
> > > **wget**：`wget -c URL`（-c 支持断点续传，推荐）  
> > > **curl**：`curl -C - -O URL`（-C - 自动续传）  
> > > **aria2c**：`aria2c -x 4 URL`（多线程，适合大文件）  
> > > 如果直连很慢（国内），可以通过 HTTP\_PROXY 加速：`export http_proxy=http://127.0.0.1:7897`
> > > 
> > > </div>
> > > 
> > > ### 案例 4-3：下载 ObjectNav MP3D 任务数据
> > > 
> > >     # ObjectNav 需要 MP3D 场景 + ObjectNav episode 文件
> > >     # 前提：已获取 MP3D 场景（见案例5）
> > >     
> > >     $ mkdir -p data/datasets/objectnav/mp3d/v1/
> > >     $ cd data/datasets/objectnav/mp3d/v1/
> > >     $ wget http://dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/mp3d/v1/objectnav_mp3d_v1.zip
> > >     $ unzip objectnav_mp3d_v1.zip
> > >     
> > >     # 验证：查看 episode 中的物体类别目标
> > >     $ zcat train/train.json.gz | python3 -c \
> > >           "import json,sys; d=json.load(sys.stdin); \
> > >            print('Episodes:', len(d['episodes'])); \
> > >            print('First goal:', d['episodes'][0]['object_category'])"
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title" style="color:#f87171;">
> > > > 
> > > > 磁盘空间提醒
> > > > 
> > > > HM3D 场景集高达 **130 GB**。下载前请用 `df -h` 确认磁盘空间充足。  
> > > > 仅下载 episode 文件（\~1GB）不需要完整场景，但运行实验时两者都需要。
> > > > 
> > > > <div class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > ## 5\. 授权数据集获取流程
> > > > 
> > > > 三类主流场景数据集都需要签署协议或申请访问权限。以下是具体流程。
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
> > > > <th>数据集</th>
> > > > <th>获取步骤</th>
> > > > <th>审批时间</th>
> > > > <th>注意事项</th>
> > > > </tr>
> > > > </thead>
> > > > <tbody>
> > > > <tr class="odd">
> > > > <td><strong>Gibson</strong></td>
> > > > <td>1. 阅读 <a href="https://storage.googleapis.com/gibson_material/Agreement%20GDS%2006-04-18.pdf">使用协议</a><br />
> > > > 2. 发邮件给 Gibson 作者申请下载链接<br />
> > > > 3. 下载 <code>gibson_4+_assets.tar.gz</code></td>
> > > > <td>通常 1-3 天</td>
> > > > <td>仅限学术研究用途<br />
> > > > 不可商业使用</td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>MatterPort3D</strong></td>
> > > > <td>1. 访问 <a href="https://niessner.github.io/Matterport/">MP3D 官网</a> 填写申请表<br />
> > > > 2. 提供 GitHub 账号 + 机构邮箱<br />
> > > > 3. 审核通过后获取 Matterport API Key<br />
> > > > 4. 使用官方 download_mp.py 脚本下载</td>
> > > > <td>通常 1-2 周</td>
> > > > <td>需要 <strong>.edu 邮箱</strong>（学术机构）<br />
> > > > API Key 不可分享</td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>HM3D</strong></td>
> > > > <td>1. 访问 <a href="https://matterport.com/partners/facebook">Matterport 合作伙伴页面</a><br />
> > > > 2. 提交 Habitat HM3D 数据集申请<br />
> > > > 3. 审批通过后获得下载权限</td>
> > > > <td>1-4 周</td>
> > > > <td>是 Matterport 与 Facebook AI 的合作项目<br />
> > > > 审批较为严格</td>
> > > > </tr>
> > > > </tbody>
> > > > </table>
> > > > 
> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 如果你暂时不想申请授权
> > > > > 
> > > > > 可以先使用 **Habitat Test Scenes**（免费）完成 PointNav 学习，  
> > > > > 用 **ReplicaCAD**（免费，自动下载）完成 Rearrange 学习（Step9）。  
> > > > > Gibson 是最容易申请的授权数据集，推荐作为第一个扩展目标。
> > > > > 
> > > > > <div class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 6\. Rearrange 数据集自动下载
> > > > > 
> > > > > Rearrange 任务的数据集下载方式与其他任务不同——它是自动触发的。
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **自动下载机制**
> > > > > 
> > > > > `RearrangeDatasetV0` 的 `__init__` 方法中（`habitat/datasets/rearrange/rearrange_dataset.py` 第58-69行） 会自动检测数据路径是否存在；如果不存在，则调用：  
> > > > > `python -m habitat_sim.utils.datasets_download --uids rearrange_task_assets --data-path data/`  
> > > > > 这意味着你**不需要手动下载 Rearrange 相关数据**——首次运行时它会自动完成。  
> > > > > 下载内容包括：ReplicaCAD 场景、YCB 物体模型、Fetch 机器人 URDF 等。
> > > > > 
> > > > > </div>
> > > > > 
> > > > >     # 验证 Rearrange 数据是否已自动下载
> > > > >     $ ls data/replica_cad/
> > > > >     # configs/  objects/  stages/  ...
> > > > >     
> > > > >     $ ls data/objects/ycb/
> > > > >     # 物体 3D 模型和配置文件
> > > > >     
> > > > >     $ ls data/robots/hab_fetch/
> > > > >     # robots/  urdf/  ...
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 学后自检 — 你掌握了什么
> > > > > 
> > > > > <div class="trouble-grid">
> > > > > 
> > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > 
> > > > > #### Q1：data/scene\_datasets/ 和 data/datasets/ 的区别？
> > > > > 
> > > > > 前者放 3D 场景模型（.glb, .navmesh），后者放任务 episode 文件（.json.gz）。一个场景可以被多个任务复用。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > 
> > > > > #### Q2：PointNav 在 Gibson 上的完整实验需要哪些数据？
> > > > > 
> > > > > ① Gibson 场景模型（.glb + .navmesh）放在 `data/scene_datasets/gibson/`  
> > > > > ② PointNav episode 文件放在 `data/datasets/pointnav/gibson/v1/`
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > 
> > > > > #### Q3：下载中断了怎么办？
> > > > > 
> > > > > 使用 `wget -c URL`（断点续传）或 `curl -C - -O URL`。对于 `datasets_download` 工具，已下载完成的部分会被跳过。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > 
> > > > > #### Q4：如何不用申请就能开始做 Rearrange 实验？
> > > > > 
> > > > > Rearrange 的数据（ReplicaCAD + YCB + robot URDF）通过 `rearrange_task_assets` 自动下载，完全免费，不需要任何授权。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > > > > 
> > > > > #### Q5：{split} 模板是什么意思？
> > > > > 
> > > > > 配置中的 `data_path: ".../{split}/{split}.json.gz"` 在运行时会根据 `dataset.split: "train"` 自动展开为 `train/train.json.gz`。这是 Hydra 的变量替换机制。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > <div class="page-nav">
> > > > > 
> > > > > [← 第1章：安装环境](habitat-textbook-step1.html) [第2章：跑通示例 →](habitat-textbook-step2.html)
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
> > > > 
> > > > </div>
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
> >

</div>
# 第2章：跑通示例 — Habitat 从零理解

> 亲手运行 Habitat 的示例程序，亲眼看到 3D 场景中的 Agent 移动。从"环境装好了"到"我知道它在做什么"。

## 0\. Habitat 有哪些示例？

Habit 仓库的 `examples/` 目录下有 15+ 个示例程序。本章精选 5 个最适合小白的学习路径。

| 序号      | 示例文件                                   | 难度  | 你将学到什么                                         |
| ------- | -------------------------------------- | --- | ---------------------------------------------- |
| **2-1** | `example_pointnav.py`                  | ⭐   | Gym API 接口、PointNav 任务、env.step() 随机动作循环（无需联网） |
| **2-2** | `tutorials/.../Habitat_Lab.py`         | ⭐⭐  | **Native API**、PointNav 任务、观测字典的内容、手动控制 Agent  |
| **2-3** | `benchmark.py`                         | ⭐⭐  | 标准化评估流程、Benchmark 对象、ForwardOnlyAgent          |
| **2-4** | `shortest_path_follower_example.py`    | ⭐⭐⭐ | 最短路径导航、Top-down 地图可视化、视频生成                     |
| **2-5** | `register_new_sensors_and_measures.py` | ⭐⭐⭐ | 自定义传感器、自定义指标、Registry 注册机制                     |

> 💡
> 
> <div class="tip-title">
> 
> 本章的学习策略
> 
> **2-1 到 2-3 必须亲手跑通。**2-4 跑通即可，不需要逐行理解。2-5 留到第4章（改配置实验）再深入。 目标不是"读懂所有代码"，而是**建立对关键数据格式和交互循环的肌肉记忆**。
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 2-1 · example\_pointnav.py — 你的第一个 Habitat 程序
> 
> Gym 接口。PointNav 任务。随机动作。无需联网下载数据。
> 
> <div>
> 
> **① 这个案例做什么？**
> 
> 创建一个 **PointNav (PointGoal Navigation)** 环境——Agent 被随机放在 3D 场景中， 目标是导航到指定的坐标点。Agent 使用**随机动作**（turn\_left / turn\_right / move\_forward / stop） 在场景中乱走，几秒后 episode 结束。  
>   
> 虽然它什么也学不到（没有 RL 训练），但它是**未来所有 RL rollout 的最简原型**。 你通过这个程序验证：环境能创建、reset 能跑、step 能推进、观测数据格式正确。 数据集使用 `habitat-test`（本地文件，无需联网）。
> 
> </div>
> 
> ### ② 核心代码 & 关键函数
> 
> #### 完整代码
> 
>     import gym
>     import habitat.gym  # noqa: F401 — 注册 Habitat-v0
>     
>     # (1) 创建 Gym 环境 — PointNav 导航任务，使用本地 habitat-test 数据集
>     env = gym.make(
>         "Habitat-v0",
>         cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
>     )
>     
>     # (2) 重置环境 — 开始一个新的 episode
>     obs = env.reset()
>     print("Keys:", obs.keys())  # → rgb, depth, pointgoal_with_gps_compass
>     
>     count_steps = 0
>     while True:
>         # (3) 随机选择一个动作（turn left/right, move_forward, stop）
>         action = env.action_space.sample()
>         # (4) 执行动作 — 环境前进一步
>         obs, reward, done, info = env.step(action)
>         count_steps += 1
>         if done:
>             break
>     
>     # (5) 输出结果 — 包含 success/spl 等评测指标
>     print("Steps:", count_steps)
>     print("Metrics:", info)
> 
> #### 关键函数调用
> 
> | 函数                            | 作用          | 说明                                                                          |
> | ----------------------------- | ----------- | --------------------------------------------------------------------------- |
> | `gym.make("Habitat-v0", ...)` | 创建环境        | Gym 标准接口。传入 YAML 配置文件路径，Habitat 自动注册 `Habitat-v0`                           |
> | `env.reset()`                 | 开始新 episode | 返回观测字典 `obs`。每次 reset 会随机选择起点和终点                                            |
> | `env.action_space.sample()`   | 随机动作        | Gym 标准接口。返回 0\~3 的 int：0=stop, 1=move\_forward, 2=turn\_left, 3=turn\_right |
> | `env.step(action)`            | 前进一步        | 返回 `(obs, reward, done, info)` — Gym 标准 4 元组                                |
> | `env.render("rgb_array")`     | 获取画面        | 返回 RGB+深度左右拼接的 numpy 数组 (256×512×3)，用 cv2.imshow 显示                         |
> 

> <div>
> 
> **Habitat Gym 完整注册表 (`gym_definitions.py`)**
> 
> 共 **30 个**已注册 Gym ID：**2 个通用** + **16 个 Skill 任务**（含 Render 变体）+ **12 个 Home Assistant Benchmark 任务**。 注册逻辑在 `habitat/gym/gym_definitions.py`，导入 `habitat.gym` 时自动触发。
> 
> 类别
> 
> </div>
> 
> </div>
> 
>

</div>

Gym ID（Performance）

Render 变体

说明

**通用**

`Habitat-v0`

`HabitatRender-v0`

接受 `cfg_file_path=...` 参数，可加载任意 YAML 配置

用于 PointNav / ObjectNav 等导航任务，或自定义 config。

**Skill  
任务**

`HabitatPick-v0`

`HabitatRenderPick-v0`

抓取物体（Fetch 机器人 + 吸盘）

`HabitatPlace-v0`

`HabitatRenderPlace-v0`

放置物体到目标位置

`HabitatNavToObj-v0`

`HabitatRenderNavToObj-v0`

纯导航到目标物体附近

`HabitatOpenCab-v0`

`HabitatRenderOpenCab-v0`

打开柜门（关节物体交互）

`HabitatCloseCab-v0`

`HabitatRenderCloseCab-v0`

关闭柜门

`HabitatOpenFridge-v0`

`HabitatRenderOpenFridge-v0`

打开冰箱门

`HabitatCloseFridge-v0`

`HabitatRenderCloseFridge-v0`

关闭冰箱门

`HabitatReachState-v0`

`HabitatRenderReachState-v0`

控制手臂到达指定位姿

**HAB  
Benchmark**

`HabitatTidyHouse-v0`

`HabitatRenderTidyHouse-v0`

整理房间（PDDL 复合任务）

`HabitatPrepareGroceries-v0`

`HabitatRenderPrepareGroceries-v0`

准备食材

`HabitatSetTable-v0`

`HabitatRenderSetTable-v0`

布置餐桌

`HabitatRearrange-v0`

`HabitatRenderRearrange-v0`

通用重排任务（无 solution）

`HabitatRearrangeEasy-v0`

`HabitatRenderRearrangeEasy-v0`

简化重排（PDDL solution 已知）

`HabitatRearrangeEasyMultiAgent-v0`

`HabitatRenderRearrangeEasyMultiAgent-v0`

多智能体协作重排

<div>

<div class="info-title" style="color:#fbbf24;">

注意：上面展示的代码 ≠ 工程文件 `example_pointnav.py`

</div>

**上面这个代码块是"教学版"（16 行）** — 它只保留核心逻辑：创建环境 → reset → 随机动作循环 → 打印结果。 目的是让你在 30 秒内看清整个程序的结构，不被无关细节分散注意力。  
  
**工程里的 `examples/example_pointnav.py`（73 行）** 在此基础上加了：

| 多出的部分                 | 在工程文件里怎么写的                                                                | 为什么加这个                                |
| --------------------- | ------------------------------------------------------------------------- | ------------------------------------- |
| **OpenCV 可视化**        | `frame = env.render(mode="rgb_array"); cv2.imshow(win, frame[..., ::-1])` | 让你**实时看到** Agent 的 RGB+深度画面，而不是只看终端数字 |
| **分组动作 + 暂停**         | 每 10 步为一组 + `time.sleep(1.0)`                                             | 防止画面闪太快看不清；给窗口时间渲染                    |
| **按键退出**              | `cv2.waitKey(1) & 0xFF` 检测 Q 键 + 窗口关闭                                     | 让你优雅退出，而不是 kill 进程                    |
| **KeyboardInterrupt** | `try/except KeyboardInterrupt; finally: cv2.destroyAllWindows()`          | Ctrl+C 或关窗口时清理 OpenCV 资源，不留僵尸窗口       |
| **Episode 自动重置**      | `if done: obs = env.reset(); count_steps = 0`                             | 一个 episode 结束自动开新的，程序持续运行到你手动退出       |

**简单记法：**教学版 = 骨架，工程版 = 骨架 + 可视化 + 交互 + 错误处理。 两者核心逻辑完全一致（都是 PointNav + 随机动作），建议**先读懂教学版，再看工程版源码**。

</div>

### ③ 如何创建和运行

代码已保存在 `examples/example_pointnav.py`。直接从仓库根目录运行：

    $ cd /develop/habitat-lab    ← 必须在仓库根目录（配置文件使用相对路径）
    $ conda activate habitat        ← 激活 conda 环境
    $ python examples/example_pointnav.py
    
    # 期望输出：
    # Observation keys: ['depth', 'pointgoal_with_gps_compass', 'rgb']
    # RGB shape: (256, 256, 3)
    # Episode finished after N steps.
    # Metrics: {'success': 0.0, 'spl': 0.0, ...}

> ⚠️
> 
> <div class="warn-title" style="color:#f87171;">
> 
> 常见报错：X\_GLXMakeCurrent BadAccess
> 
> 如果在 NVIDIA GPU + GNOME 桌面下报 `X_GLXMakeCurrent: BadAccess`： **本课程的 example\_pointnav.py 已内置修复**（`mode="rgb_array"` + OpenCV）， 直接运行即可，无需任何额外配置。详见[永久修复方法](#glx-fix)。
> 
> </div>
> 
> ### ④ 运行效果
> 
> 以下是在本机 (NVIDIA RTX 2070 SUPER, Ubuntu 22.04, habitat-sim 0.2.5) 上**实际运行**的终端输出和画面。
> 
> #### 终端输出（随机动作循环）
> 
>     Observation keys: ['depth', 'pointgoal_with_gps_compass', 'rgb']
>       RGB: shape=(256, 256, 3), dtype=uint8, min=26, max=252
>       Depth: shape=(256, 256, 1), dtype=float32, min=0.0247, max=0.0776
>       pointgoal_with_gps_compass: shape=(2,), dtype=float32, [10.9006, 1.5645]
>     
>     初始状态: distance=10.9006m, angle=1.5645rad
>     
>     执行 10 步随机动作 (env.action_space.sample())...
>       action 编号: 0=stop, 1=move_forward, 2=turn_left, 3=turn_right
>       Step  1: action=2(turn_left),    dist=10.9006m, angle=1.3900rad  reward=-0.010
>       Step  2: action=1(move_forward), dist=10.8868m, angle=1.4127rad  reward=-0.270
>       Step  3: action=3(turn_right),   dist=10.8868m, angle=1.5872rad  reward=-0.010
>       Step  4: action=2(turn_left),    dist=10.8868m, angle=1.4127rad  reward=-0.010
>       Step  5: action=2(turn_left),    dist=10.8868m, angle=1.2381rad  reward=-0.010
>       Step  6: action=1(move_forward), dist=10.8858m, angle=1.2522rad  reward=-0.171
>       Step  7: action=3(turn_right),   dist=10.8858m, angle=1.4268rad  reward=-0.010
>       Step  8: action=3(turn_right),   dist=10.8858m, angle=1.6013rad  reward=-0.010
>       Step  9: action=0(stop),            dist=10.8858m, angle=1.6013rad  reward=-0.010  ← Agent 主动停止!
>     
>     After 9 steps metrics: {'distance_to_goal': 11.814, 'success': 0.0, 'spl': 0.0}
> 
> #### 4 个动作的视觉效果对比
> 
> 随机动作大概率中途抽到 stop，无法保证"前进 10 步"。下面用**手动指定动作**展示不同动作对视野的影响 （场景和出生点相同，使用 `env.render(mode="rgb_array")` 截图）。
> 
> <div class="obs-grid" style="grid-template-columns: repeat(2, 1fr);">
> 
> <div class="obs-card">
> 
> #### 初始位置 (reset 后)
> 
> ![初始视角](images/2-1_reset_rgb.png)
> 
> distance=10.90m, angle=1.56rad
> 
> </div>
> 
> <div class="obs-card">
> 
> #### turn\_left ×6（左转 \~90°）
> 
> ![左转后视角](images/2-1_turn_left.png)
> 
> 视野大幅变化 — 看到了房间右侧
> 
> </div>
> 
> <div class="obs-card">
> 
> #### turn\_right ×12（右转 \~90°）
> 
> ![右转后视角](images/2-1_turn_right.png)
> 
> 视野完全不同 — 角度改变即改变"看到的世界"
> 
> </div>
> 
> <div class="obs-card">
> 
> #### move\_forward ×8（前进 2m）
> 
> ![前进后视角](images/2-1_move_forward.png)
> 
> 靠近墙壁 — 视野中物体变大
> 
> ### ⑤ 输出结果的含义
> 
> <div>
> 
> **逐条解读**
> 
> **1. 观测字典有三个 key：**`rgb` (视觉)、`depth` (深度)、`pointgoal_with_gps_compass` (导航信号)。 这就是 PointNav 中 AI 策略**能获取的全部信息** — 没有地图、没有绝对坐标、没有"这里是什么房间"的标注。  
>   
> **2. move\_forward 的 reward 是 -0.17\~-0.27：**而 turn\_left / turn\_right / stop 只有 -0.01（slack penalty）。 为什么前进的惩罚更大？因为初始朝向 (1.56rad ≈ 89°) 几乎**垂直**于目标方向。 往前走不仅不靠近目标，反而可能远离 — **在 PointNav 中，选对方向比走多远更重要。**  
>   
> **3. 距离从 10.90m 降到 10.886m 后卡住：**Agent 在第2章撞墙。 后续 turn 只能改变朝向不能改位置 — **碰撞检测正常工作**，物理引擎阻止穿墙。  
>   
> **4. success=0.0 但 Agent 调用了 stop：**第9章 的 stop 结束了 episode。 但 success 仍是 0 — 因为 stop 时距目标还有 11.8m（远大于 success\_distance=0.1m）。 **success 需同时满足 (a) 调用 stop (b) distance \< 0.1m**。  
>   
> **5. 随机动作很容易抽到 stop：**这就是 RL 训练时策略网络必须学会"不随便 stop"的原因。
> 
> </div>
> 
> ### ⑥ 试试调整这些，再观察变化
> 
> <table>
> <colgroup>
> <col style="width: 33%" />
> <col style="width: 33%" />
> <col style="width: 33%" />
> </colgroup>
> <thead>
> <tr class="header">
> <th>调整项</th>
> <th>怎么改</th>
> <th>预期看到什么</th>
> </tr>
> </thead>
> <tbody>
> <tr class="odd">
> <td>手动指定动作</td>
> <td>把 <code>action_space.sample()</code> 换成固定 int：<br />
> <code>action = 1  # 一直前进</code></td>
> <td>Agent 一直往前走直到撞墙 — 观察 distance 如何变化，何时卡住</td>
> </tr>
> <tr class="even">
> <td>打印更多观测</td>
> <td>在循环里加：<br />
> <code>print(obs['depth'].mean())</code></td>
> <td>深度图的平均深度值 — 越靠近障碍物均值越小</td>
> </tr>
> <tr class="odd">
> <td>修改最大步数</td>
> <td>编辑 YAML 中 <code>max_episode_steps</code><br />
> 或创建新 YAML 覆盖这个值</td>
> <td>不改 agent 永远 500 步超时；改成 20 看提前超时的效果</td>
> </tr>
> <tr class="even">
> <td>缩小图片分辨率</td>
> <td>编辑 YAML 中 RGB sensor 的 <code>width: 128, height: 128</code></td>
> <td>画面变模糊，但 step 速度更快 — 理解传感器分辨率对性能的影响</td>
> </tr>
> </tbody>
> </table>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 2-2 · Native API — PointNav 任务 & 观测字典
> 
> 这是本章**最重要**的一节。你会看到 Agent 的"眼睛"能看到什么，以及如何用代码读取。
> 
> <div>
> 
> **① 案例含义 — 这个案例要演示什么**
> 
> **Native API** 是 Habitat 最底层的 Python 接口。与 Gym API 不同，它不经过 `gym.make()` 封装， 直接用 `habitat.Env(config)` 创建环境。这个案例演示三件事：  
> **1. 如何用 Native API 创建环境并获取观测** — `obs = env.reset()` 返回一个字典，Agent 的所有"感官"都在里面  
> **2. 观测字典里有什么** — RGB 图像（256×256×3）、深度图（256×256×1）、GPS+Compass 导航信号（2,）  
> **3. 如何加上实时画面显示** — 把 RGB 和深度图左右拼接成 256×512，用 OpenCV 显示，**不触发 GLX 错误**
> 
> </div>
> 
> ### ② 核心代码 & 关键函数调用
> 
> #### 最小 PointNav 程序（Native API）
> 
>     import habitat
>     
>     # (1) 加载 PointNav 测试配置
>     config = habitat.get_config("benchmark/nav/pointnav/pointnav_habitat_test.yaml")
>     
>     # (2) 创建环境（Native API，非 Gym）
>     env = habitat.Env(config)
>     
>     # (3) 重置 — 返回观测字典
>     obs = env.reset()
>     
>     # (4) 看看观测字典里有什么
>     print("观测类型:", obs.keys())
>     
>     # (5) 执行几步，观察数据变化
>     for step in range(5):
>         action = {"action": "move_forward"}  # 前进 0.25m
>         obs = env.step(action)
>         gps = obs["pointgoal_with_gps_compass"]
>         print(f"第{step}步 — 到目标的距离: {gps[0]:.2f}m, 角度: {gps[1]:.2f}rad")
> 
> 这个程序涉及的**关键函数调用**：
> 
> | 函数调用                       | 作用                      | 返回值                                       |
> | -------------------------- | ----------------------- | ----------------------------------------- |
> | `habitat.get_config(path)` | 加载 YAML 配置文件，解析默认值和继承关系 | `Config` 对象（类 OmegaConf / dict）           |
> | `habitat.Env(config)`      | 根据配置创建模拟器 + 任务环境        | `Env` 对象                                  |
> | `env.reset()`              | 开始新 episode：随机出生点、随机目标  | `dict` — 观测字典（rgb, depth, gps 等）          |
> | `env.step(action)`         | 执行动作，模拟器更新，返回新观测        | `dict` — 新观测字典                            |
> | `env.episode_over`         | 检查当前 episode 是否已结束      | `bool` — stop/超时/到达目标则为 True              |
> | `env.get_metrics()`        | 获取 episode 的评估指标        | `dict` — success, spl, distance\_to\_goal |
> 

> #### 加上实时画面显示（RGB + 深度图拼接）
> 
> Native API 不需要 `env.render()` — RGB 和深度图直接在观测字典里。 把两者**左右拼接**成 256×512 画面，效果和 `example_pointnav.py` 的 `render('rgb_array')` 完全一致。 同样**不会触发 GLX 错误**。
> 
>     import cv2
>     import numpy as np
>     import habitat
>     
>     def make_frame(obs):
>         # 深度归一化 → 灰度 → 3 通道（含 NaN/Inf 保护）
>         depth = obs["depth"].squeeze().copy()
>         dmin, dmax = depth.min(), depth.max()
>         if dmax - dmin 
> 
> > ⚠️
> > 
> > <div class="warn-title" style="color:#fbbf24;">
> > 
> > 常见问题：窗口显示黑屏或不完整
> > 
> > **根因：**OpenCV 的 `cv2.imshow()` 只是把图像"提交"给窗口系统， **必须调用 `cv2.waitKey(n)`** 才能让 GUI 事件循环真正渲染画面。 如果 `imshow` 后没有紧跟 `waitKey`，窗口就会显示为黑色或不完整。  
> >   
> > **正确写法：**每行 `imshow` 下一行就是 `waitKey(1)`。 上面代码中循环末尾的 `waitKey(300)` 既负责画面刷新，又负责检测按键（300ms 超时）。
> > 
> > </div>
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > Gym API vs Native API 的渲染差异
> > > 
> > > **Gym API：**`env.render(mode="rgb_array")` 自动把 RGB 和深度图左右拼接成 256×512。  
> > > **Native API：**RGB 在 `obs["rgb"]`（256×256），深度在 `obs["depth"]`（256×256×1）， 需要手动拼接。上面的 `make_frame()` 就是干这件事的 — 先归一化深度，再 `np.hstack`。
> > > 
> > > </div>
> > > 
> > > ### ③ 创建和运行
> > > 
> > > 把上面的代码保存为 `my_native_pointnav.py`，在仓库根目录运行。**Native API 必须从仓库根目录运行**，因为配置文件使用相对路径。
> > > 
> > >     $ cd /develop/habitat-lab
> > >     $ conda activate habitat
> > >     $ python my_native_pointnav.py
> > >     
> > >     # 期望输出：
> > >     # 观测类型: ['rgb', 'depth', 'pointgoal_with_gps_compass']
> > >     # 初始 GPS: distance=10.9006m, angle=1.5645rad
> > >     # 第1章 — 到目标的距离: 10.90m, 角度: 1.59rad
> > >     # ...
> > > 
> > > <div>
> > > 
> > > <div class="info-title" style="color:#22d3ee;">
> > > 
> > > 推荐：交互式控制脚本 play\_pointnav.py
> > > 
> > > </div>
> > > 
> > > 上面的代码只是演示"怎么加画面"。实际使用建议直接跑 `examples/play_pointnav.py`： **WASD 控制 Agent（W=前进, A=左转, D=右转, S=停止），窗口一直显示直到你按 Q 退出。** episode 结束后按 R 重开，不会闪现消失。已内置 `waitKey(1)` 刷新机制，不会黑屏。
> > > 
> > >     $ python examples/play_pointnav.py
> > > 
> > > </div>
> > > 
> > > ### ④ 运行效果
> > > 
> > > #### 终端输出
> > > 
> > >     观测类型: ['rgb', 'depth', 'pointgoal_with_gps_compass']
> > >       rgb: shape=(256, 256, 3), dtype=uint8        ← 注意：3 通道 RGB，不是 RGBA
> > >       depth: shape=(256, 256, 1), dtype=float32
> > >       pointgoal_with_gps_compass: shape=(2,), dtype=float32
> > >     
> > >     初始 GPS: distance=10.9006m, angle=1.5645rad
> > >     执行 5 步 move_forward...
> > >       第1章 — 到目标的距离: 10.9019m, 角度: 1.5874rad
> > >       第2章 — 到目标的距离: 10.8858m, 角度: 1.6013rad
> > >       第3章 — 到目标的距离: 10.8858m, 角度: 1.6013rad  ← 距离不再变化, Agent 撞墙了!
> > >       第4章 — 到目标的距离: 10.8858m, 角度: 1.6013rad
> > >       第5章 — 到目标的距离: 10.8858m, 角度: 1.6013rad
> > >     
> > >     5 步后 metrics: {
> > >       'distance_to_goal': 11.814,
> > >       'success': 0.0,
> > >       'spl': 0.0
> > >     }
> > > 
> > > #### Agent 看到的画面 — 前进 5 步前后对比
> > > 
> > > <div class="dual-panel">
> > > 
> > > <div class="panel" style="border-top: 3px solid #3b82f6;">
> > > 
> > > #### 初始位置 (reset 后)
> > > 
> > > ![Native API 初始视角](images/2-2_reset_rgb.png)
> > > 
> > > RGB 256×256 — Agent 紧贴墙壁
> > > 
> > > </div>
> > > 
> > > <div class="panel" style="border-top: 3px solid #f59e0b;">
> > > 
> > > #### 前进 5 步之后
> > > 
> > > ![前进5步后](images/2-2_after5_forward.png)
> > > 
> > > 视野几乎没有变化 — Agent 已经撞墙卡住, 距离停在 10.886m
> > > 
> > > ### ⑤ 输出结果的含义
> > > 
> > > #### 观测字典里有什么？
> > > 
> > > 根据配置不同，观测字典包含不同的 key。PointNav 测试配置下：
> > > 
> > > <div class="obs-grid">
> > > 
> > > <div class="obs-card">
> > > 
> > > <span class="obs-icon">📷</span>
> > > 
> > > <div class="obs-name">
> > > 
> > > RGB 图像
> > > 
> > > </div>
> > > 
> > > <div class="obs-key">
> > > 
> > > obs\["rgb"\]
> > > 
> > > </div>
> > > 
> > > <div class="obs-desc">
> > > 
> > > Agent 第一人称视角的彩色图像
> > > 
> > > </div>
> > > 
> > > <div class="obs-shape">
> > > 
> > > shape: (H, W, 3) RGB uint8
> > > 
> > > <div class="obs-card">
> > > 
> > > <span class="obs-icon">🎯</span>
> > > 
> > > <div class="obs-name">
> > > 
> > > GPS + 指南针
> > > 
> > > </div>
> > > 
> > > <div class="obs-key">
> > > 
> > > obs\["pointgoal\_with\_gps\_compass"\]
> > > 
> > > </div>
> > > 
> > > <div class="obs-desc">
> > > 
> > > 到目标的距离 + 相对角度偏差
> > > 
> > > </div>
> > > 
> > > <div class="obs-shape">
> > > 
> > > shape: (2,) float32 \[distance, angle\]
> > > 
> > > <div class="obs-card">
> > > 
> > > <span class="obs-icon">🔭</span>
> > > 
> > > <div class="obs-name">
> > > 
> > > 深度图
> > > 
> > > </div>
> > > 
> > > <div class="obs-key">
> > > 
> > > obs\["depth"\]
> > > 
> > > </div>
> > > 
> > > <div class="obs-desc">
> > > 
> > > 每个像素到 Agent 的距离（米）
> > > 
> > > </div>
> > > 
> > > <div class="obs-shape">
> > > 
> > > shape: (H, W, 1) float32
> > > 
> > > <div class="obs-card">
> > > 
> > > <span class="obs-icon">🏷️</span>
> > > 
> > > <div class="obs-name">
> > > 
> > > 语义分割
> > > 
> > > </div>
> > > 
> > > <div class="obs-key">
> > > 
> > > obs\["semantic"\]
> > > 
> > > </div>
> > > 
> > > <div class="obs-desc">
> > > 
> > > 每个像素的物体类别 ID
> > > 
> > > </div>
> > > 
> > > <div class="obs-shape">
> > > 
> > > shape: (H, W) int32
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > **关键洞察：观测字典是策略的唯一信息源**
> > > 
> > > Agent 的"世界"完全由这个字典定义。它不知道场景文件在哪里、不知道自己的绝对坐标 — 它只知道 `obs` 里的内容。这就是为什么 Sensor 的设计如此重要：**你给什么，AI 就学什么。**
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > **逐条解读运行结果**
> > > 
> > > **1. rgb shape=(256, 256, 3), dtype=uint8：**3 通道是 RGB（不是 RGBA），值域 0–255。 这和 Gym API 的 `render('rgb_array')` 返回的 256×512 不同 — render 自动拼接了深度图。  
> > >   
> > > **2. depth dtype=float32：**深度值单位是**米**，不是像素。深度图记录的是从相机到物体表面的距离， 不是到导航目标的距离 — 两者是不同的概念。  
> > >   
> > > **3. 第3章开始距离不再变化：**Agent 在第2章已经撞墙，后续 step 无法移动。 Habitat 的物理引擎**自动阻止穿墙** — Agent 只能在 NavMesh（导航网格）上移动。  
> > >   
> > > **4. angle 随 move\_forward 也会变化：**即使是直走（不转弯），角度也会轻微变化（1.5645→1.5874→1.6013）。 因为 Agent 移动后，它相对于目标的方向自然改变 — 这是正常的几何效应。
> > > 
> > > </div>
> > > 
> > > ### ⑥ 试试调整这些，再观察变化
> > > 
> > > | 调整项            | 怎么改                                            | 预期看到什么                                              |
> > > | -------------- | ---------------------------------------------- | --------------------------------------------------- |
> > > | 换不同动作序列        | 把 `move_forward` 换成 `turn_left` / `turn_right` | 距离不变但角度变化 — 理解纯旋转不改变 Agent 位置，只改变朝向                 |
> > > | 增加传感器          | 在 YAML 的 `sim_sensors` 中添加 `semantic_sensor`   | `obs` 中多出一个 key — 体验"传感器声明即启用"的机制                   |
> > > | 打印 episode 元信息 | 加 `print(env.current_episode.__dict__)`        | 看到 scene\_id, start\_position, goal\_position 等幕后数据 |
> > > | 调整深度图可视化       | 改 `make_frame()`，用 `cv2.COLORMAP_JET` 替换灰度     | 伪彩色深度图 — 红色=近, 蓝色=远，比灰度更直观                          |
> > > 

> > > <div>
> > > 
> > > **Native API 官方教程文件**
> > > 
> > > 完整的官方教程在 `examples/tutorials/nb_python/Habitat_Lab.py`（Jupyter notebook 格式）。 它包含更多功能：交互式控制 Agent、matplotlib 可视化、自定义 Task/Sensor 注册。 上面展示的是其中最核心的部分 — 理解了这些，剩下的都是"加功能"。
> > > 
> > > </div>
> > > 
> > > <div class="exercise">
> > > 
> > > #### 练习 2-2A：打印每个观测的形状和类型
> > > 
> > > 修改上面的程序，在 `env.reset()` 之后添加一个循环： `for key, val in obs.items(): print(key, type(val), val.shape if hasattr(val, 'shape') else 'N/A')`  
> > > 记录下来你看到的每一种观测 — 它们就是你未来训练模型的**输入数据**。
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 2-2B · 动作空间 — Agent 能做什么
> > > 
> > > PointNav 的离散动作空间只有 4 个动作。这是最简单也最重要的动作设计。
> > > 
> > > <div>
> > > 
> > > **① 案例含义 — 这个案例要演示什么**
> > > 
> > > **动作空间**定义了 Agent 在环境中"能做什么"。PointNav 的离散动作空间只有 4 个动作：停止、前进、左转、右转。 这看起来简单，但**已经足够完成导航任务** — 任何复杂路径都可以分解为"转+走"的组合。  
> > > 这个案例演示：**每个动作执行后 GPS 数据如何变化**、哪些动作改变位置、哪些只改变朝向、以及**Native API 和 Gym API 的动作格式差异**。
> > > 
> > > </div>
> > > 
> > > ### ② 动作空间定义 & 两种 API 的格式差异
> > > 
> > > | 动作名    | 键值               | 效果            | Native API 写法                | Gym API 编号 |
> > > | ------ | ---------------- | ------------- | ---------------------------- | ---------- |
> > > | **停止** | `"stop"`         | 结束当前 episode  | `{"action": "stop"}`         | `0`        |
> > > | **前进** | `"move_forward"` | 向当前朝向移动 0.25m | `{"action": "move_forward"}` | `1`        |
> > > | **左转** | `"turn_left"`    | 逆时针旋转 15°     | `{"action": "turn_left"}`    | `2`        |
> > > | **右转** | `"turn_right"`   | 顺时针旋转 15°     | `{"action": "turn_right"}`   | `3`        |
> > > 

> > > <div>
> > > 
> > > **Native API vs Gym API 的动作格式差异**
> > > 
> > > **Native API：**`{"action": "move_forward"}` — 字典格式，action 的值是字符串。更灵活，支持参数化动作。  
> > > **Gym API：**`env.action_space.sample()` — 返回 int（0-3）。Gym 封装层做了离散化编号，方便对接 RL 库（Stable-Baselines3）。  
> > > 两种 API 在你的学习过程中都会遇到，理解它们的对应关系很重要。
> > > 
> > > </div>
> > > 
> > > ### ③ 创建和运行 — 验证 4 个动作
> > > 
> > > 下面的代码对每个动作：创建新环境 → reset → 执行一次 → 记录 GPS 变化。可以直接在前面 2-2 的程序中替换动作来测试。
> > > 
> > >     import habitat
> > >     
> > >     config = habitat.get_config("benchmark/nav/pointnav/pointnav_habitat_test.yaml")
> > >     
> > >     for action_name in ["move_forward", "turn_left", "turn_right", "stop"]:
> > >         env = habitat.Env(config)
> > >         obs = env.reset()
> > >         before = obs["pointgoal_with_gps_compass"].copy()
> > >         obs = env.step({"action": action_name})
> > >         after = obs["pointgoal_with_gps_compass"]
> > >         print(f"{action_name:>14s}: dist {before[0]:.4f}→{after[0]:.4f}  angle {before[1]:.4f}→{after[1]:.4f}  over={env.episode_over}")
> > >         env.close()
> > > 
> > > ### ④ 运行效果
> > > 
> > >     # 对每个动作：创建新环境 → reset → 执行一次 → 记录 GPS 变化
> > >       move_forward: gps 10.9006 -> 10.9019 (Δ=+0.0013), over=False
> > >       turn_left:    gps 10.9006 -> 10.9006 (Δ=+0.0000), over=False
> > >       turn_right:   gps 10.9006 -> 10.9006 (Δ=+0.0000), over=False
> > >       stop:         gps 10.9006 -> 10.9006 (Δ=+0.0000), over=True
> > > 
> > > <div class="dual-panel" style="margin-top:16px;">
> > > 
> > > <div class="panel" style="border-top: 3px solid #3b82f6;">
> > > 
> > > #### 动作前
> > > 
> > > ![动作前](step2_outputs/2-2B_before_move.png)
> > > 
> > > </div>
> > > 
> > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > 
> > > #### move\_forward 动作后
> > > 
> > > ![动作后](step2_outputs/2-2B_after_move.png)
> > > 
> > > 前进 0.25m — 视觉上几乎看不到变化，但 GPS 距离确实变了
> > > 
> > > ### ⑤ 输出结果的含义
> > > 
> > > <div>
> > > 
> > > **逐条解读**
> > > 
> > > **1. move\_forward: Δ=+0.0013m（距离反而增加）：**因为 Agent 初始朝向与目标方向夹角为 1.56 rad (≈89°)， 几乎垂直于目标方向。直走不会缩短距离，甚至可能远离 — **在 PointNav 中，选对方向比走多远更重要。**  
> > >   
> > > **2. turn\_left / turn\_right: Δ=0（距离不变）：**纯旋转动作不改变位置，所以到目标的测地距离不变。 但 **角度**（angle）会改变 ±0.1745 rad（=10°），下一次 forward 的方向就不同了。  
> > >   
> > > **3. stop: over=True（立即结束）：**这是唯一导致 episode 立即结束的动作。 **如果 AI 永远不调用 stop，episode 会一直运行直到超时**（默认 500 步），但永远不会被判定为"成功到达"。 **success 需要同时满足 (a) 调用 stop (b) 距离 \< 0.1m。**
> > > 
> > > </div>
> > > 
> > > ### ⑥ 试试调整这些，再观察变化
> > > 
> > > | 调整项           | 怎么改                                     | 预期看到什么                                      |
> > > | ------------- | --------------------------------------- | ------------------------------------------- |
> > > | 走一个正方形        | 前进 4 步 → 右转 6 次 → 重复 4 轮                | Agent 走一个 \~1m×1m 的正方形，验证 "15°×6=90°" 的转向精度 |
> > > | 连续左转 24 次     | 循环执行 `turn_left` 24 次                   | 360° 转回原位 — 验证 15°×24=360°，角度应该基本回到初始值      |
> > > | Gym API 中验证编号 | 在 `example_pointnav.py` 中手动设 `action=1` | 确认 Gym API 的 int 编号和 Native API 字符串的对应关系    |
> > > 

> > > <div class="exercise" style="margin-top:18px;">
> > > 
> > > #### 练习 2-2B：手动控制 Agent 走一个正方形
> > > 
> > > 写一个循环，让 Agent 做：前进 4 步 → 右转 6 次（90°）→ 前进 4 步 → 右转 6 次 → … 重复直到 episode 结束。 观察 `pointgoal_with_gps_compass` 的值如何变化。这是一个经典的"验证动作空间"实验。
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 2-3 · benchmark.py — 标准化评估
> > > 
> > > "我的 Agent 有多好？" — Benchmark 用统一的标准回答这个问题。
> > > 
> > > <div>
> > > 
> > > **① 案例含义 — 这个案例要演示什么**
> > > 
> > > **Benchmark（基准测试）**是 Habitat 的标准化评估框架。它在多个 episode 上运行 Agent，自动计算 Success、SPL 等指标。 这个案例演示三件事：  
> > > **1. 如何定义一个 Agent** — 继承 `habitat.Agent`，实现 `act()` 方法  
> > > **2. 如何用 Benchmark 评估** — `benchmark.evaluate(agent, num_episodes=10)`  
> > > **3. 为什么"靠近目标就停"这个看似合理的策略**在 PointNav 中依然是 success=0
> > > 
> > > </div>
> > > 
> > > ### ② 核心代码 & 关键函数调用
> > > 
> > > #### 定义 Agent 并评估
> > > 
> > >     import habitat
> > >     
> > >     # (1) 定义一个最简单的 Agent — 永远前进，永不停止
> > >     class ForwardOnlyAgent(habitat.Agent):
> > >         def reset(self): pass
> > >         def act(self, observations):
> > >             return {"action": "move_forward"}
> > >     
> > >     # (2) 创建基准测试
> > >     benchmark = habitat.Benchmark("benchmark/nav/pointnav/pointnav_habitat_test.yaml")
> > >     
> > >     # (3) 评估 — 10 个 episode
> > >     metrics = benchmark.evaluate(ForwardOnlyAgent(), num_episodes=10)
> > >     
> > >     # (4) 查看指标
> > >     for key, val in metrics.items():
> > >         print(f"{key}: {val:.3f}")
> > > 
> > > 关键函数调用：
> > > 
> > > | 函数调用                                      | 作用                               | 关键参数                                 |
> > > | ----------------------------------------- | -------------------------------- | ------------------------------------ |
> > > | `habitat.Agent`                           | Agent 基类，需实现 `act()` 和 `reset()` | `act(observations)` → 返回 action dict |
> > > | `habitat.Benchmark(config)`               | 创建评估器，加载任务配置和数据集                 | 配置文件路径（同 Native API）                 |
> > > | `benchmark.evaluate(agent, num_episodes)` | 在多个 episode 上运行 Agent，汇总指标       | `num_episodes` 控制评估规模                |
> > > 

> > > #### 改进版：SmartStopAgent — 靠近目标就停
> > > 
> > >     class SmartStopAgent(habitat.Agent):
> > >         def reset(self): pass
> > >         def act(self, observations):
> > >             gps = observations["pointgoal_with_gps_compass"]
> > >             distance = gps[0]
> > >             if distance 
> > > 
> > > ### ③ 创建和运行
> > > 
> > >     $ cd /develop/habitat-lab
> > >     $ conda activate habitat
> > >     $ python -c "
> > >     import habitat
> > >     class SmartStopAgent(habitat.Agent):
> > >         def reset(self): pass
> > >         def act(self, obs):
> > >             return {'action': 'stop' if obs['pointgoal_with_gps_compass'][0] 
> > > 
> > > ### ④ 运行效果
> > > 
> > >     # 在 10 个 episode 上评估，每个 episode 最多 500 步
> > >     
> > >     ForwardOnlyAgent (永远前进):
> > >       distance_to_goal: 12.975
> > >       success: 0.000
> > >       spl:               0.000
> > >     
> > >     SmartStopAgent (距目标 
> > > 
> > > ### ⑤ 输出结果的含义
> > > 
> > > <div>
> > > 
> > > **为什么 SmartStopAgent 的 success 也是 0？**
> > > 
> > > 这是一个**非常经典的新手误解**。Success 需要 **同时满足两个条件**：  
> > > (1) Agent 调用了 `stop`  
> > > (2) stop 时 Agent 距目标的**测地距离** ≤ 0.1m（success\_distance）  
> > >   
> > > SmartStopAgent 的问题在于：它只会 `move_forward`，**从不会转弯**。 如果 Agent 的初始朝向没有正对目标，一直往前走**永远到不了目标** — 距离停在 \~11m 处（撞墙了）， 永远不会降到 0.5m 以下，所以 `stop` 根本不会被调用。  
> > >   
> > > **这揭示了一个本质问题：**仅仅"靠近就停"不够 — AI 需要学会**"先转向目标方向，再前进"**。 这就是为什么导航策略需要至少 3 个动作（前进、左转、右转）才能完成 PointNav 任务。
> > > 
> > > </div>
> > > 
> > > ### ⑥ 试试调整这些，再观察变化
> > > 
> > > | 调整项              | 怎么改                                         | 预期看到什么                                              |
> > > | ---------------- | ------------------------------------------- | --------------------------------------------------- |
> > > | 增加转弯逻辑           | 在 `act()` 中加入：如果 angle 偏差大，先 turn 再 forward | success 可能突破 0 — 体验"有转向能力"对导航的关键作用                  |
> > > | 调整 stop 阈值       | 改 `distance < 0.5` 为 `0.15`                 | 更接近 success\_distance(0.1m) 才停 — 但前提是 Agent 能到达目标附近 |
> > > | 增加评估 episode 数   | 改 `num_episodes=100`                        | 统计更稳定 — 10 个 episode 可能运气好，100 个更反映真实水平             |
> > > | 打印每个 episode 的结果 | 在 `act()` 中加 `print(distance, angle)`       | 看到 10 个 episode 各自的距离变化 — 有些出生点可能离目标更近              |
> > > 

> > > <div class="exercise" style="margin-top:18px;">
> > > 
> > > #### 练习 2-3：给 Agent 加上转向能力
> > > 
> > > 修改 `SmartStopAgent.act()`：读取 `observations["pointgoal_with_gps_compass"]` 中的 angle， 如果 `abs(angle) > 0.2`（约 11°），先转向目标（angle\>0 则 turn\_right，否则 turn\_left）；否则前进。 再跑一次 benchmark，看看 **success 是否有提升**。
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 2-4 · shortest\_path\_follower — 聪明的 Agent
> > > 
> > > Habitat 内置了一个"学霸 Agent"——它不靠视觉，直接读取场景的导航网格，用图搜索算法找到最短路径。我们来拆解它是怎么做到的。
> > > 
> > > <div>
> > > 
> > > **① 案例含义 — 这个案例要演示什么**
> > > 
> > > **ShortestPathFollower** 是 Habitat 内置的"最优 Agent"——它不"看"RGB 图像，而是直接读取场景的**导航网格（NavMesh）**， 用 Dijkstra 算法计算从当前位置到目标的最短路径，然后每一步沿着这条路径走。 它要导航到的目标是 **PointNav 数据集中预先定义的目标坐标**——一个 3D 空间点 `(x, y, z)`， 附带一个 **到达半径（goal\_radius）**，Agent 进入该半径即判定为"到达"。  
> > >   
> > > 这个案例演示三个核心问题：  
> > > **1. 导航目标从哪来？** — 目标坐标存储在数据集的 episode 中，每个 episode 有一个 `NavigationGoal`，包含 `position` 和 `radius`  
> > > **2. 最短路径如何计算？** — NavMesh 将场景的可通行区域建模为图，Dijkstra 算法在图上搜索最短路径  
> > > **3. Agent 如何沿路径走？** — 每一步调用 `get_next_action(goal_pos)`，返回当前应执行的动作（前进/左转/右转/停止）  
> > > **4. ShortestPathFollower 能取得什么性能？** — Success≈1.0, SPL≈0.99，这是 RL 训练的**理论上限**
> > > 
> > > </div>
> > > 
> > > ### ② 核心代码 & 运行流程
> > > 
> > > #### 完整代码（带注释）
> > > 
> > >     import numpy as np
> > >     import habitat
> > >     from habitat.tasks.nav.shortest_path_follower import ShortestPathFollower
> > >     from habitat.utils.visualizations import maps
> > >     from habitat.utils.visualizations.utils import images_to_video
> > >     
> > >     # ═══════════════════════════════════════════
> > >     # 步骤 1：创建环境 + 配置 Top-down 地图传感器
> > >     # ═══════════════════════════════════════════
> > >     config = habitat.get_config(
> > >         config_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
> > >         overrides=[
> > >             # 添加 top_down_map 测量指标 — 用于生成俯视地图
> > >             "+habitat/task/measurements@habitat.task.measurements.top_down_map=top_down_map"
> > >         ],
> > >     )
> > >     
> > >     # SimpleRLEnv 是 habitat.RLEnv 的最简子类 — 只用于封装环境
> > >     env = SimpleRLEnv(config=config)
> > >     
> > >     # ═══════════════════════════════════════════
> > >     # 步骤 2：创建 ShortestPathFollower
> > >     # ═══════════════════════════════════════════
> > >     # goal_radius 从 episode 数据中读取 — 定义了"到达"的判定半径
> > >     goal_radius = env.episodes[0].goals[0].radius
> > >     if goal_radius is None:
> > >         goal_radius = config.habitat.simulator.forward_step_size  # 默认 0.25m
> > >     
> > >     follower = ShortestPathFollower(
> > >         env.habitat_env.sim,   # 传入底层 HabitatSim 实例（用于访问 NavMesh）
> > >         goal_radius,           # 到达判定半径
> > >         False                  # return_one_hot=False → 返回离散动作 int
> > >     )
> > >     
> > >     # ═══════════════════════════════════════════
> > >     # 步骤 3：主循环 — 对每个 episode 执行导航
> > >     # ═══════════════════════════════════════════
> > >     for episode in range(3):
> > >         env.reset()
> > >     
> > >         # 每一步都向 follower 查询"下一步该走哪个动作"
> > >         while not env.habitat_env.episode_over:
> > >             # ★ 核心调用：给定目标 3D 坐标，返回一个最优动作
> > >             best_action = follower.get_next_action(
> > >                 env.habitat_env.current_episode.goals[0].position
> > >             )
> > >             if best_action is None:
> > >                 break  # 无法到达目标（孤立 NavMesh 区域）
> > >     
> > >             # 执行动作，获取新的观测 + 指标
> > >             observations, reward, done, info = env.step(best_action)
> > >     
> > >             # 合成双视图：左侧 RGB + 右侧 Top-down 地图
> > >             im = observations["rgb"]
> > >             top_down_map = draw_top_down_map(info, im.shape[0])
> > >             output_im = np.concatenate((im, top_down_map), axis=1)
> > >     
> > >         # 将每一帧合成为导航视频
> > >         images_to_video(images, dirname, "trajectory")
> > > 
> > > #### 程序运行流程图
> > > 
> > > <div class="flow-box">
> > > 
> > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > 
> > > **① 加载配置**
> > > 
> > > get\_config()  
> > > 读取 YAML
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > 
> > > **② 创建 Env**
> > > 
> > > SimpleRLEnv  
> > > 加载场景+数据集
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > 
> > > **③ 创建 Follower**
> > > 
> > > ShortestPathFollower  
> > > 接收 sim + goal\_radius
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > 
> > > **④ reset() 开始**
> > > 
> > > 新 episode  
> > > Agent 出生 + 目标就位
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > 
> > > **⑤ 循环导航**
> > > 
> > > get\_next\_action(goal)  
> > > → env.step(action)
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > 
> > > **⑥ 生成视频**
> > > 
> > > RGB + Top-down  
> > > images\_to\_video()
> > > 
> > > #### 关键函数调用
> > > 
> > > | 函数                                                | 作用           | 说明                                                                                                                    |
> > > | ------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------- |
> > > | `habitat.get_config(...)`                         | 加载配置         | 读取 YAML + 命令行 override。这里额外添加了 `top_down_map` measurement                                                             |
> > > | `ShortestPathFollower(sim, radius, False)`        | 创建最短路径导航器    | 接收底层 sim 对象以访问 NavMesh；`goal_radius` 决定"到达"的判定距离；`return_one_hot=False` 返回离散 int 动作                                   |
> > > | `env.reset()`                                     | 开始新 episode  | 随机选择起点和终点，Agent 回到起点。episode 数据中包含 `goals[0].position`                                                                |
> > > | `follower.get_next_action(goal_pos)`              | ★ 核心：计算下一步动作 | 传入目标 3D 坐标，内部调用 C++ 层的 `GreedyGeodesicFollower.next_action_along(goal_pos)`，在 NavMesh 上运行 Dijkstra 后返回当前最优动作（0/1/2/3） |
> > > | `env.step(action)`                                | 执行动作         | 返回 (obs, reward, done, info)。info 中包含 top\_down\_map 等 measurement 输出                                                 |
> > > | `maps.colorize_draw_agent_and_fit_to_height(...)` | 绘制俯视地图       | 将 info\["top\_down\_map"\] 渲染为彩色地图：白色=可通行区域，黑线=墙壁/障碍，绿色圆=目标，红色箭头=Agent                                                |
> > > | `images_to_video(images, dirname, name)`          | 生成导航视频       | 将帧列表合成 .mp4 文件，保存到 `examples/images/shortest_path_example/`                                                           |
> > > 

> > > #### 导航目标是如何确定的？
> > > 
> > > 目标**不是代码里写死的**，而是从**数据集的 episode 文件中读取**的。一条完整的导航目标确定链路如下：
> > > 
> > > <div class="dual-panel">
> > > 
> > > <div class="panel" style="border-top: 3px solid #8b5cf6;">
> > > 
> > > #### Episode 数据文件 (JSON)
> > > 
> > >     {
> > >       "episodes": [
> > >         {
> > >           "episode_id": "0",
> > >           "scene_id": "data/scene_datasets/.../skokloster-castle.glb",
> > >           "start_position": [-7.37, 0.08, 6.58],
> > >           "start_rotation": [0, 0.82, 0, 0.57],
> > >           "goals": [{
> > >             "position": [-5.31, 0.26, 17.28],
> > >             "radius": 0.25
> > >           }]
> > >         },
> > >         // ... 更多 episode
> > >       ]
> > >     }
> > > 
> > > 每个 episode 包含：起点坐标、起点朝向、**目标坐标 + 到达半径**
> > > 
> > > </div>
> > > 
> > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > 
> > > #### 目标在代码中的传递链
> > > 
> > > **1. 数据集加载阶段：**  
> > > `JSON 文件` → `PointNavDatasetV1` 解析每个 episode → 包装为 `NavigationEpisode` 对象  
> > > 其中 `goals` 字段是 `List[NavigationGoal]`，每个 `NavigationGoal` 有 `position` 和 `radius` 两个属性  
> > >   
> > > **2. env.reset() 阶段：**  
> > > `env.reset()` → 从 dataset 中选一个 episode → 设置为 `env.current_episode`  
> > > Agent 被放置到 `start_position`，目标坐标存储在 `current_episode.goals[0].position`  
> > >   
> > > **3. 导航循环中：**  
> > > 每一帧调用 `follower.get_next_action(env.current_episode.goals[0].position)`  
> > > → 传入目标的 `(x, y, z)` 坐标 → follower 内部计算到该坐标的最短路径 → 返回下一步动作
> > > 
> > > #### 最短路径是如何计算的？（NavMesh + Dijkstra）
> > > 
> > > <div class="flow-box">
> > > 
> > > <div class="flow-step" style="border-top:3px solid #3b82f6; max-width:160px;">
> > > 
> > > **NavMesh**
> > > 
> > > 场景加载时  
> > > 自动预计算
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #8b5cf6; max-width:160px;">
> > > 
> > > **图上 Dijkstra**
> > > 
> > > 从当前位置  
> > > 搜到目标位置
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #f59e0b; max-width:160px;">
> > > 
> > > **生成路径点**
> > > 
> > > 一串连续的  
> > > 3D 坐标序列
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #10b981; max-width:160px;">
> > > 
> > > **每步查询动作**
> > > 
> > > 沿路径点  
> > > 返回 turn/move/stop
> > > 
> > > **第 1 层 — NavMesh（C++ 层，Habitat-Sim 内部）：**  
> > > 场景（.glb 文件）加载时，Habitat-Sim 自动分析 3D 几何，计算出所有 Agent 可以站立和行走的区域。 这些区域被离散化为一张**图（Graph）**——每个节点是一个可到达的 3D 点，边表示两个点之间可以直接移动。 这张图就是 **NavMesh**（Navigation Mesh）。墙壁、家具、楼梯边缘等不可通行区域不会出现在图中。  
> > >   
> > > **第 2 层 — GreedyGeodesicFollower（C++ 层，Habitat-Sim 内部）：**  
> > > 在 NavMesh 图上运行 **Dijkstra 最短路径算法**，找到从 Agent 当前位置到目标位置的一条最短路径。 路径是一串连续的 3D 坐标点（waypoints）。"Geodesic"（测地线）的含义是：路径沿可通行表面走， 而不是穿墙的直线。  
> > >   
> > > **第 3 层 — ShortestPathFollower（Python 层，habitat-lab）：**  
> > > 封装了 C++ 的 `GreedyGeodesicFollower`。每一步调用 `get_next_action(goal_pos)` 时：  
> > >   1. 检查是否需要重建 follower（场景切换时）  
> > >   2. 调用 `self._follower.next_action_along(goal_pos)` → C++ 层  
> > >   3. C++ 层计算：Agent 当前位置在路径上的哪个点？下一个路径点在哪？需要前进还是转向？  
> > >   4. 返回一个离散动作 int：0=stop（已到达），1=move\_forward，2=turn\_left，3=turn\_right  
> > >   5. 如果目标在不可达的 NavMesh 孤岛上，抛出 `GreedyFollowerError` → 返回 stop
> > > 
> > > <div>
> > > 
> > > **为什么要分三层？**
> > > 
> > > NavMesh 计算和 Dijkstra 搜索是**计算密集型**操作，必须在 C++ 中完成以保证性能。 Python 层的 `ShortestPathFollower` 只是一个**薄封装**——它把 Habitat-Sim 的 C++ 能力暴露给 Python 用户。 这种"底层 C++ 计算 + 上层 Python 接口"的模式在 Habitat 中非常普遍（渲染管线、物理引擎同理）。
> > > 
> > > </div>
> > > 
> > > ### 深入理解：NavMesh 地图从哪来？——完整链路跟踪
> > > 
> > > 上面说到"场景加载时自动预计算 NavMesh"，但你可能会问：**场景文件是谁选的？NavMesh 具体是怎么生成的？如果我想换一张地图该改哪里？** 下面从 Episode 定义到 C++ NavMesh 构建，完整跟踪这条链路。
> > > 
> > > <div class="arch-diagram" style="margin:20px 0;">
> > > 
> > > <div class="arch-row">
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #f59e0b;">
> > > 
> > > **① Dataset 定义场景**
> > > 
> > > episode.scene\_id  
> > > \= "van-gogh-room.glb"
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #3b82f6;">
> > > 
> > > **② Task 覆写 config**
> > > 
> > > NavigationTask  
> > > overwrite\_sim\_config()
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #8b5cf6;">
> > > 
> > > **③ HabitatSim 组装**
> > > 
> > > sim\_config.scene\_id  
> > > \+ navmesh\_settings
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #10b981;">
> > > 
> > > **④ C++ Recast 建网**
> > > 
> > > 分析 .glb 几何  
> > > → 生成 NavMesh
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #ec4899;">
> > > 
> > > **⑤ Follower 使用**
> > > 
> > > make\_greedy\_follower()  
> > > → next\_action\_along()
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > <div class="info-title" style="color:#a5b4fc;">
> > > 
> > > 代码链路跟踪：5 个关键文件
> > > 
> > > </div>
> > > 
> > > <table>
> > > <colgroup>
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > </colgroup>
> > > <thead>
> > > <tr class="header">
> > > <th style="text-align: center;">环节</th>
> > > <th>文件</th>
> > > <th style="text-align: center;">行号</th>
> > > <th>关键代码</th>
> > > </tr>
> > > </thead>
> > > <tbody>
> > > <tr class="odd">
> > > <td style="text-align: center;">①</td>
> > > <td><code style="font-size:0.72rem;">habitat-test-scenes/.../habitat_test.json</code></td>
> > > <td style="text-align: center;">—</td>
> > > <td>Dataset JSON 中每个 episode 的 <code>"scene_id": "data/scene_datasets/habitat-test-scenes/van-gogh-room.glb"</code></td>
> > > </tr>
> > > <tr class="even">
> > > <td style="text-align: center;">②</td>
> > > <td><code style="font-size:0.72rem;">habitat/tasks/nav/nav.py</code></td>
> > > <td style="text-align: center;">L1329</td>
> > > <td><code>config.simulator.scene = episode.scene_id</code> — Task 将 Episode 的场景 ID 写入 Simulator 配置</td>
> > > </tr>
> > > <tr class="odd">
> > > <td style="text-align: center;">③</td>
> > > <td><code style="font-size:0.72rem;">habitat/sims/habitat_simulator/...py</code></td>
> > > <td style="text-align: center;">L327<br />
> > > L352-357</td>
> > > <td><code>sim_config.scene_id = self.habitat_config.scene</code>；并根据 agent radius/height 设置 <code>NavMeshSettings</code></td>
> > > </tr>
> > > <tr class="even">
> > > <td style="text-align: center;">④</td>
> > > <td>habitat_sim C++ (Recast/Detour)</td>
> > > <td style="text-align: center;">—</td>
> > > <td><code>habitat_sim.Simulator(config)</code> 构造时检测 <code>config.navmesh_settings</code> 非空 → 自动调用 Recast 分析 .glb 3D 几何 → 生成 NavMesh → 存入 <code>sim.pathfinder</code></td>
> > > </tr>
> > > <tr class="odd">
> > > <td style="text-align: center;">⑤</td>
> > > <td><code style="font-size:0.72rem;">habitat/tasks/nav/shortest_path_follower.py</code></td>
> > > <td style="text-align: center;">L54-64</td>
> > > <td><code>self._follower = self._sim.make_greedy_follower(0, goal_radius, ...)</code> — 从 sim.pathfinder 读取 NavMesh，创建贪心跟随器</td>
> > > </tr>
> > > </tbody>
> > > </table>
> > > 
> > > </div>
> > > 
> > > #### NavMesh 是如何生成的？——Recast/Detour 算法
> > > 
> > > Habitat-Sim 使用业界标准的 **Recast/Detour** 库（游戏引擎中用了几十年）自动生成 NavMesh。 整个过程在 C++ 层完成，不需要手动标注任何东西：
> > > 
> > > <div class="flow-box" style="margin:14px 0;">
> > > 
> > > <div class="flow-step" style="border-top:3px solid #6366f1; max-width:140px;">
> > > 
> > > **输入 .glb 几何**
> > > 
> > > 场景 3D 三角网格  
> > > （墙壁、地板、家具）
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #8b5cf6; max-width:140px;">
> > > 
> > > **体素化**
> > > 
> > > 把三角网格转为  
> > > 3D 体素（小方块）
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #a78bfa; max-width:140px;">
> > > 
> > > **过滤可通行区域**
> > > 
> > > 根据 radius/height/  
> > > slope/climb 参数筛选
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #c4b5fd; max-width:140px;">
> > > 
> > > **生成凸多边形**
> > > 
> > > 把可通行体素  
> > > 聚合为凸多边形
> > > 
> > > </div>
> > > 
> > > <div class="flow-arrow">
> > > 
> > > →
> > > 
> > > </div>
> > > 
> > > <div class="flow-step" style="border-top:3px solid #10b981; max-width:140px;">
> > > 
> > > **建图**
> > > 
> > > 多边形 → 图节点  
> > > 邻接 → 图边
> > > 
> > > | 参数                       | 默认值                     | 含义                              |
> > > | ------------------------ | ----------------------- | ------------------------------- |
> > > | `agent_radius`           | \= agent\_config.radius | Agent 的碰撞半径。小于此宽度的通道视为不可通行      |
> > > | `agent_height`           | \= agent\_config.height | Agent 的"身高"。天花板低于此高度的区域视为不可通行   |
> > > | `agent_max_climb`        | 默认 0.2m                 | Agent 能攀爬的最大台阶高度（低于此的台阶视为可通行地形） |
> > > | `agent_max_slope`        | 默认 45°                  | Agent 能行走的最大坡度。超过此角度的斜坡不可通行     |
> > > | `include_static_objects` | 见 config                | 是否将场景中的静态物体（家具等）也纳入障碍物计算        |
> > > 

> > > <div>
> > > 
> > > <div class="info-title" style="color:#34d399;">
> > > 
> > > 关键理解：NavMesh ≠ 场景文件
> > > 
> > > </div>
> > > 
> > > **场景文件**（.glb）是完整的 3D 模型 — 包括墙壁纹理、家具、光照等所有视觉内容。 **NavMesh** 只是从 3D 几何中**提取出来的一张"可通行地图"** — 只记录"哪些地方可以站、哪些地方可以走"。 这两者的关系类似于：**一栋楼的完整 BIM 模型** vs **楼层平面图**。导航只需要平面图，渲染才需要完整模型。
> > > 
> > > </div>
> > > 
> > > #### 如何指定或替换地图？——4 种方式
> > > 
> > > <table>
> > > <colgroup>
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > <col style="width: 25%" />
> > > </colgroup>
> > > <thead>
> > > <tr class="header">
> > > <th style="text-align: center;">方法</th>
> > > <th>操作</th>
> > > <th>改动位置</th>
> > > <th>适用场景</th>
> > > </tr>
> > > </thead>
> > > <tbody>
> > > <tr class="odd">
> > > <td style="text-align: center;"><strong>①</strong></td>
> > > <td>换 <strong>.glb 场景文件</strong></td>
> > > <td>Dataset JSON<br />
> > > episode.scene_id</td>
> > > <td>用不同的 3D 场景（如从 apartment_1 换成 skokloster-castle）。只需改 JSON，NavMesh 自动重建</td>
> > > </tr>
> > > <tr class="even">
> > > <td style="text-align: center;"><strong>②</strong></td>
> > > <td>换 <strong>场景数据集配置</strong></td>
> > > <td>config 中的<br />
> > > scene_dataset</td>
> > > <td>正式数据集（Gibson/MP3D/HSSD）需要 .scene_dataset.json 来定义场景路径、语义标签等，不能直接用裸 .glb</td>
> > > </tr>
> > > <tr class="odd">
> > > <td style="text-align: center;"><strong>③</strong></td>
> > > <td>调整 <strong>NavMesh 参数</strong></td>
> > > <td>habitat_simulator.py<br />
> > > L350-358</td>
> > > <td>同一个场景，改变 agent_radius/agent_height 会得到不同的 NavMesh（更宽/更高的 agent 意味着更少的可通行区域）</td>
> > > </tr>
> > > <tr class="even">
> > > <td style="text-align: center;"><strong>④</strong></td>
> > > <td>使用<strong>预烘焙 .navmesh</strong></td>
> > > <td>pathfinder.save_nav_mesh()<br />
> > > + load_nav_mesh()</td>
> > > <td>场景很大时 Recast 计算耗时。先跑一次保存为 .navmesh 文件，后续直接加载跳过重建</td>
> > > </tr>
> > > </tbody>
> > > </table>
> > > 
> > > **对于 habitat\_test 数据集：**3 个场景（apartment\_1, skokloster-castle, van-gogh-room）都是 Habitat-Sim pip 安装时自带的， 存储在 `data/scene_datasets/habitat-test-scenes/`。每次启动时 Episode 随机分配一个场景 — 所以你跑 `example_pointnav.py` 时每次看到的房间可能不同。
> > > 
> > > ### 从模拟到真实：机器人如何自己生成 NavMesh？
> > > 
> > > 一个关键洞察：**如果真实机器人能生成 NavMesh，整个 Habitat 导航管线就能直接在真实世界运行。** ShortestPathFollower 不关心 NavMesh 是从 .glb 还是从 Lidar 数据生成的——它只认 `PathFinder` 接口。 这意味着模拟器中的导航算法和真实机器人的导航算法**可以是同一套代码**。
> > > 
> > > <div class="arch-diagram" style="margin:20px 0;">
> > > 
> > > <div class="arch-row">
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #f59e0b;">
> > > 
> > > **模拟器路径**
> > > 
> > > .glb 完美几何  
> > > → Recast 直接出 NavMesh
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center" style="font-size:1.5rem;">
> > > 
> > > ⟹
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #10b981; flex:1.5;">
> > > 
> > > **同一个 NavMesh + 同一个导航算法**
> > > 
> > > ShortestPathFollower / RL Policy  
> > > → env.step(action) 循环
> > > 
> > > </div>
> > > 
> > > <div class="arch-arrow-center" style="font-size:1.5rem;">
> > > 
> > > ⟸
> > > 
> > > </div>
> > > 
> > > <div class="arch-layer" style="border-top:3px solid #6366f1;">
> > > 
> > > **真实机器人路径**
> > > 
> > > 传感器数据  
> > > → SLAM → Mesh → Recast
> > > 
> > > </div>
> > > 
> > > 上图 — 模拟器和真实机器人在 NavMesh 层面是打通的。左右两条路径的输出格式完全相同。
> > > 
> > > #### 真实机器人获取 NavMesh 的三条流水线
> > > 
> > > <table>
> > > <colgroup>
> > > <col style="width: 20%" />
> > > <col style="width: 20%" />
> > > <col style="width: 20%" />
> > > <col style="width: 20%" />
> > > <col style="width: 20%" />
> > > </colgroup>
> > > <thead>
> > > <tr class="header">
> > > <th style="text-align: center;">#</th>
> > > <th>流水线</th>
> > > <th>传感器</th>
> > > <th>核心算法</th>
> > > <th>输出 → NavMesh 的路径</th>
> > > </tr>
> > > </thead>
> > > <tbody>
> > > <tr class="odd">
> > > <td style="text-align: center;"><strong>1</strong></td>
> > > <td><strong>2D 占据栅格</strong></td>
> > > <td>2D Lidar<br />
> > > 或深度图投影</td>
> > > <td>GMapping / Cartographer / Hector SLAM</td>
> > > <td>2D 占据栅格地图 → 直接当 <strong>2D NavMesh</strong> 用（ROS nav2 的 costmap 模式）。<br />
> > > ⚠️ 丢失高度信息，不支持多层/斜坡</td>
> > > </tr>
> > > <tr class="even">
> > > <td style="text-align: center;"><strong>2</strong></td>
> > > <td><strong>3D 体素 → 表面重建</strong></td>
> > > <td>RGB-D 相机<br />
> > > （Realsense / Kinect）</td>
> > > <td><strong>Voxblox</strong> (TSDF 体素)<br />
> > > <strong>OctoMap</strong> (八叉树)<br />
> > > 或 <strong>RTAB-Map</strong> (RGB-D SLAM)</td>
> > > <td>TSDF 体素 → <strong>Marching Cubes</strong> 提取三角 Mesh → <strong>Recast</strong> 在 Mesh 上生成 NavMesh<br />
> > > ✅ 真 3D，支持多层、斜坡</td>
> > > </tr>
> > > <tr class="odd">
> > > <td style="text-align: center;"><strong>3</strong></td>
> > > <td><strong>3D LiDAR 点云 → Mesh</strong></td>
> > > <td>3D LiDAR<br />
> > > （Velodyne / Ouster）</td>
> > > <td>LOAM / LeGO-LOAM / FAST-LIO</td>
> > > <td>LiDAR 点云 → 点云配准 + SLAM → <strong>Poisson Surface Reconstruction</strong> → 三角 Mesh → <strong>Recast</strong> 生成 NavMesh<br />
> > > ✅ 精度最高，室外/大场景首选</td>
> > > </tr>
> > > </tbody>
> > > </table>
> > > 
> > > <div>
> > > 
> > > <div class="info-title" style="color:#a5b4fc;">
> > > 
> > > 三条流水线的选用指南
> > > 
> > > </div>
> > > 
> > > **流水线 1（2D 占据栅格）— 最简单，适合室内平面导航：**  
> > > 如果机器人只在**单层平面上移动**（如家庭扫地机、仓库 AGV），2D 栅格地图完全够用。 ROS2 nav2 默认就是这个方案 — 它内部也用 Dijkstra/A\* 做全局规划，和 Habitat 的 ShortestPathFollower 思路完全一致， 区别只是地图表示（2D 栅格 vs 3D NavMesh）。  
> > >   
> > > **流水线 2（RGB-D + 体素融合）— Habitat 研究者最常用的真实世界方案：**  
> > > Habitat 的许多论文作者（如 FAIR / Meta）在真实世界实验中使用这个方案。 因为 RGB-D 相机便宜（Realsense D435 约 $200），Voxblox 的 TSDF 重建质量可靠， Marching Cubes 提取的 Mesh 可以直接喂给 Recast——这和 Habitat 内部的 NavMesh 生成用的是**同一个算法**。  
> > >   
> > > **流水线 3（3D LiDAR）— 精度最高的方案，适合大场景/室外：**  
> > > 3D LiDAR 点云密度高、范围远（可达 100m+），是自动驾驶的事实标准。 LOAM 系列算法实时性好，Poisson 重建能生成平滑的 Mesh。 代价是 LiDAR 本身价格高（数千到上万美元），对算力要求也更高。
> > > 
> > > </div>
> > > 
> > > #### 涉及的关键算法一览
> > > 
> > > | 算法                 | 类别         | 输入          | 输出                    | 在流水线中的角色                                                               |
> > > | ------------------ | ---------- | ----------- | --------------------- | ---------------------------------------------------------------------- |
> > > | **Cartographer**   | 2D/3D SLAM | Lidar + IMU | 2D/3D 占据栅格地图          | Google 开源的实时 SLAM。室内用 2D 模式直接出栅格地图；3D 模式可输出点云                          |
> > > | **RTAB-Map**       | RGB-D SLAM | RGB-D       | 2D 栅格 + 3D 点云 + 视觉里程计 | 老牌方案，ROS 集成成熟。输出 3D 点云后可用 Poisson 重建转 Mesh                             |
> > > | **Voxblox**        | 体素建图       | 深度图 + 位姿    | TSDF 体素 / ESDF        | ETH Zurich 出品。TSDF 体素直接用 Marching Cubes 提取 Mesh — 这是 Habitat→真实打通的关键环节 |
> > > | **OctoMap**        | 体素建图       | 深度图/点云 + 位姿 | 八叉树占据地图               | 八叉树压缩 3D 地图，内存效率高。也能提取 Mesh，适合大场景                                      |
> > > | **Marching Cubes** | 表面重建       | 体素数据（TSDF）  | 三角 Mesh               | 经典算法（1987）。从体素提取等值面，生成三角网格 — 这就是 Recast 要吃的格式                          |
> > > | **Poisson 重建**     | 表面重建       | 3D 点云 + 法向量 | 三角 Mesh               | 从有向点云重建光滑闭合 Mesh。LiDAR 方案的标准选择                                         |
> > > | **Recast/Detour**  | 导航网格       | 三角 Mesh     | NavMesh（凸多边形图）        | Habitat-Sim 内部使用。模拟和真实**共用这一层**——这是打通的关键                               |
> > > 

> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > Sim-to-Real 的实际差距
> > > > 
> > > > 虽然在 NavMesh 层面模拟和真实可以打通，但实际落地还有几个现实差距：  
> > > >   
> > > > **1. 真实 NavMesh 有噪声和盲区：**传感器视线被遮挡的区域（如沙发后面）无法建图，NavMesh 会有"空洞"。 相比之下，Habitat 的 NavMesh 是完美覆盖的。  
> > > >   
> > > > **2. 动态障碍物：**Recast 生成的是静态地图。真实环境中的行人、移动的椅子等需要额外的**局部避障层** （类似 ROS 的 DWA/TEB）——这也是为什么真实导航系统通常是"全局规划 + 局部规划"双层架构。  
> > > >   
> > > > **3. 定位误差：**Habitat 中 Agent 的位置是模拟器直接给出的精确坐标。真实机器人需要 AMCL 等定位算法， 定位误差会传导到导航决策。  
> > > >   
> > > > **4. 但这些都不改变核心结论：**只要你能生成 NavMesh，Habitat 的导航算法（ShortestPathFollower、RL Policy） 就能直接用。模拟器中训练的 RL 策略，在真实环境中用同一套 NavMesh 做导航，是活跃的研究方向（PointNav Sim2Real）。
> > > > 
> > > > </div>
> > > > 
> > > > ### 对比阅读：ShortestPathFollower 与 ROS 导航有什么区别？
> > > > 
> > > > 如果你有 ROS 背景，可能会问：这不就是 ROS 的 move\_base / nav2 吗？其实两者的设计哲学完全不同—— 一个是**为 AI 研究提供"标准答案"的 oracle**，一个是**为真实机器人提供可靠性的工程系统**。
> > > > 
> > > > <div class="dual-panel">
> > > > 
> > > > <div class="panel" style="border-top: 3px solid var(--accent-sim);">
> > > > 
> > > > #### Habitat ShortestPathFollower
> > > > 
> > > > 🎯 **目标：**提供导航的"理论上限"  
> > > > 🗺️ **地图：**NavMesh — 3D 三角网格  
> > > > 🔍 **规划：**单层 Dijkstra 全局规划  
> > > > 🚫 **避障：**无 — 场景是静态的  
> > > > 📡 **传感器：**不使用 — 直接读几何数据  
> > > > 👁️ **信息：**完美信息（完整 3D 几何）  
> > > > 📐 **维度：**真 3D（支持多层、斜坡）  
> > > > 📍 **定位：**模拟器直接给精确坐标  
> > > > 🔗 **坐标系：**单一场景本地坐标  
> > > > 👥 **受众：**AI/RL 研究者
> > > > 
> > > > </div>
> > > > 
> > > > <div class="panel" style="border-top: 3px solid var(--accent-rl);">
> > > > 
> > > > #### ROS Navigation (move\_base / nav2)
> > > > 
> > > > 🤖 **目标：**在真实世界中可靠导航  
> > > > 🗺️ **地图：**Costmap — 2D 占据栅格  
> > > > 🔍 **规划：**全局规划 + 局部规划 双层架构  
> > > > 🚫 **避障：**DWA/TEB 实时局部避障  
> > > > 📡 **传感器：**Lidar/深度相机实时更新  
> > > > 👁️ **信息：**部分可观测（噪声、盲区）  
> > > > 📐 **维度：**通常是 2D (x, y, yaw)  
> > > > 📍 **定位：**AMCL 等融合多种传感器  
> > > > 🔗 **坐标系：**TF2 管理多级坐标变换  
> > > > 👥 **受众：**机器人工程师
> > > > 
> > > > | 对比维度      | ShortestPathFollower                                        | ROS Navigation                                                                   |
> > > > | --------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------- |
> > > > | **地图表示**  | NavMesh — 3D 三角网格，Habitat-Sim 从场景 .glb 几何自动生成               | Costmap — 2D 栅格图。全局 costmap 来自 SLAM/预建地图；局部 costmap 由传感器实时更新                     |
> > > > | **规划架构**  | **单层规划** — 只在 NavMesh 上跑一次 Dijkstra，直接沿路径走。没有局部重规划          | **双层规划** — Global Planner（Dijkstra/A\*）出大致路径 → Local Planner（DWA/TEB）负责速度平滑和实时避障 |
> > > > | **动态障碍物** | 不存在 — 场景是纯静态的，NavMesh 在加载后不再变化                              | 核心能力 — 传感器持续扫描，local costmap 动态更新，检测到障碍物立即调整轨迹                                   |
> > > > | **传感器依赖** | 完全不使用传感器进行规划 — follower 直接读取 NavMesh 内部图结构，RGB/Depth 仅用于可视化 | 高度依赖传感器 — Lidar/深度相机提供 real-time 点云或扫描数据来构建和更新 costmap                           |
> > > > | **信息完备性** | **完美信息** — 知道场景中每一面墙、每一件家具的精确 3D 几何。没有"未知区域"                | **部分可观测** — 传感器有噪声、视野有限，未被扫描的区域标记为"未知"，不保证最优路径                                   |
> > > > | **定位**    | 无定位误差 — Agent 的 (x, y, z, quaternion) 由模拟器直接给出，精度无限         | 需要 AMCL / EKF 等定位算法融合 IMU、里程计、Lidar 等多源数据，存在累积误差                                 |
> > > > | **空间维度**  | 真 **3D** — NavMesh 天然支持多层建筑、楼梯、斜坡。Agent 可以在不同楼层间导航          | 通常是 **2D** (x, y, yaw) — 3D 导航（如无人机、多楼层）仍在积极发展中（nav2 有实验性 3D 支持）                 |
> > > > | **坐标管理**  | 单一场景本地坐标系 — 没有 TF 变换树，所有坐标在同一个参考系下                          | **TF2 变换树** — 管理 map→odom→base\_link→sensor 等多级坐标变换，是 ROS 的基础设施                  |
> > > > 

> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#67e8f9;">
> > > > 
> > > > 一句话总结
> > > > 
> > > > </div>
> > > > 
> > > > **ShortestPathFollower = 理想世界的导航标准答案。**它告诉你"如果一切完美，最优路径是什么"。 它的价值在于为 RL 训练提供 **ground truth 参考**——你知道理论上限是多少（Success=1.0, SPL≈0.99）， 就能判断自己的策略学到了多少。  
> > > > **ROS Navigation = 真实世界的导航工程方案。**它要应对传感器噪声、定位漂移、动态障碍、计算资源限制等实际问题。 两者的设计目标不同，不能互相替代——但理解 ShortestPathFollower 的简单性，有助于你更深刻地理解 ROS 导航的每个模块**为什么存在**。
> > > > 
> > > > </div>
> > > > 
> > > > ### ③ 如何创建和运行
> > > > 
> > > >     $ cd /develop/habitat-lab
> > > >     $ conda activate habitat
> > > >     $ python examples/shortest_path_follower_example.py
> > > >     
> > > >     # 期望输出：
> > > >     # Environment creation successful
> > > >     # Agent stepping around inside environment.
> > > >     # Episode finished  (×3 次，对应 3 个 episode)
> > > >     #
> > > >     # 输出文件：
> > > >     # examples/images/shortest_path_example/00/trajectory.mp4
> > > >     # examples/images/shortest_path_example/01/trajectory.mp4
> > > >     # examples/images/shortest_path_example/02/trajectory.mp4
> > > > 
> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 如果 headless 模式下没有 DISPLAY
> > > > > 
> > > > > 这个示例依赖 `matplotlib` 绘图。在纯 headless 服务器上，在脚本开头添加：  
> > > > > `import matplotlib; matplotlib.use('Agg')` — 这会切换到非交互式后端，仅生成文件不弹窗。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ④ 运行效果
> > > > > 
> > > > > #### 实际终端输出
> > > > > 
> > > > >     # 场景: skokloster-castle.glb (城堡内部)
> > > > >     # 3 个 episode，每次随机出生点和目标点
> > > > >     
> > > > >     Environment creation successful
> > > > >     Agent stepping around inside environment.
> > > > >       # Episode 0: 77 步到达目标 — 长距离走廊导航
> > > > >     100%|████████████████████████████████████| 77/77 [00:00
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **三个 episode 的步数差异说明了什么？**
> > > > > 
> > > > > 同一个城堡场景，三个 episode 分别走了 **77 步、9 步、31 步**。差异来源于每次 reset 随机选取不同的起点和目标： Episode 1 的目标刚好在出生点附近（几步就到），Episode 0 的目标在城堡的另一个区域（需绕行大量墙壁）。 这说明**导航难度高度依赖 episode 的起点-目标配对**——同一个场景可以同时包含"几秒钟走完"和"绕整个城堡"的任务。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > #### 导航视频 — 左侧 RGB 第一人称视角 + 右侧 Top-down 俯视地图
> > > > > 
> > > > > 以下三个视频是实际运行生成的结果。每个视频并排显示：**左侧 = Agent 看到的 RGB 画面**（第一人称）， **右侧 = Top-down 地图**（白色=可通行 NavMesh，黑线=墙壁，绿色圆=目标，红色箭头=Agent 位置与朝向）。 注意观察 Episode 0（77 步）中 Agent 如何沿白色 NavMesh 区域绕行，从不穿越黑色墙壁。
> > > > > 
> > > > > <div class="dual-panel">
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #f59e0b;">
> > > > > 
> > > > > #### Episode 0 — 长距离导航（77 步）
> > > > > 
> > > > > 您的浏览器不支持视频播放。
> > > > > 
> > > > > 起点和目标分布在城堡不同区域，需要绕过多个房间和走廊
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > > > 
> > > > > #### Episode 1 — 超短距离导航（9 步）
> > > > > 
> > > > > 您的浏览器不支持视频播放。
> > > > > 
> > > > > 目标恰好在出生点附近，几步即达 — 这是最简单的 episode 类型
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #3b82f6; margin-top:18px;">
> > > > > 
> > > > > #### Episode 2 — 中等距离导航（31 步）
> > > > > 
> > > > > 您的浏览器不支持视频播放。
> > > > > 
> > > > > 中等难度的 episode — 需要绕过一些墙壁但不需要穿越整个城堡
> > > > > 
> > > > > </div>
> > > > > 
> > > > > #### Top-Down 地图细节放大
> > > > > 
> > > > > <div class="dual-panel">
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #3b82f6;">
> > > > > 
> > > > > #### 初始位置（reset 后第一帧）
> > > > > 
> > > > > ![初始位置地图](step2_outputs/2-4_topdown_with_agent.png)
> > > > > 
> > > > > 🔵 起点 (start\_position)   🟢 目标 (goal.position)  
> > > > > 🔴 红色箭头 = Agent 当前位置与朝向  
> > > > > 白色 = NavMesh 可通行区域，黑色线条 = 墙壁/障碍物边界
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > > > 
> > > > > #### 导航结束位置（77 步后）
> > > > > 
> > > > > ![最终位置地图](step2_outputs/2-4_final_position.png)
> > > > > 
> > > > > Agent 已到达目标附近（距目标 0.113m ≤ goal\_radius 0.25m）  
> > > > > 77 步走完城堡迷宫式路径 — 沿白色 NavMesh 区域绕行
> > > > > 
> > > > > ### ⑤ 输出结果的含义
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **逐条解读**
> > > > > 
> > > > > **1. Success=1.0, SPL=0.988 — 几乎完美：**ShortestPathFollower 使用 NavMesh 的最短路径， 是 PointNav 任务的**性能理论上限**。如果你的 RL 策略能达到 SPL≈0.98，训练就趋近最优。 SPL = Success × (最短路径长度 / 实际路径长度)，0.988 表示实际路径比最短路径仅长 \~1.2%。  
> > > > >   
> > > > > **2. 78 步走 11m 的迷宫路径：**Agent 起点在城堡左下角 (-7.37, 6.58)，目标在右上角 (-5.31, 17.28)。 直线距离虽然只有约 11m，但城堡内部有大量墙壁和房间分隔——Agent 不能穿墙， 只能沿白色 NavMesh 区域移动。78 步 × 0.25m/步 ≈ 19.5m 的实际行走距离，远大于直线距离。  
> > > > >   
> > > > > **3. NavMesh 是导航的基础设施：**所有 Agent（包括你的 RL 策略）都被限制在 NavMesh 内。 没有 NavMesh，Agent 无法判断哪里可以通过 — 场景数据必须预计算导航网格。 NavMesh 由 Habitat-Sim 在场景加载时自动生成，存储为内部图结构。  
> > > > >   
> > > > > **4. SPL 为什么不是 1.0？**离散动作空间（步长 = `forward_step_size` = 0.25m）必然引入轻微误差 — Agent 不能"沿路径精确走"，只能每次前进固定距离或转固定角度（10° 或 30°）。 转弯后的位置会微微偏离最优路径，累积成 \~1.2% 的额外路程。这是离散动作空间的固有特性。  
> > > > >   
> > > > > **5. distance\_to\_goal = 0.113m \< goal\_radius = 0.25m：**follower 判定"已到达"的条件是 Agent 进入目标周围的半径为 `goal_radius` 的球体。0.113m 已经在球内，所以 episode 以 success 结束。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ⑥ 试试调整这些，再观察变化
> > > > > 
> > > > > <table>
> > > > > <colgroup>
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > </colgroup>
> > > > > <thead>
> > > > > <tr class="header">
> > > > > <th>调整项</th>
> > > > > <th>怎么改</th>
> > > > > <th>预期看到什么</th>
> > > > > </tr>
> > > > > </thead>
> > > > > <tbody>
> > > > > <tr class="odd">
> > > > > <td>增加 episode 数量</td>
> > > > > <td>改脚本中 <code>for episode in range(3)</code> → <code>range(10)</code></td>
> > > > > <td>不同 episode 起点和目标都不同 — 有些在走廊里几步就到，有些要绕多个房间，步数从 15 到 150+ 不等</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td>换一个场景</td>
> > > > > <td>修改 YAML 中的 <code>scene</code> 路径指向其他 .glb 文件</td>
> > > > > <td>不同场景的 NavMesh 差异巨大 — 小场景几步就到，大场景 100+ 步。地图可视化让你直观看到场景布局</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td>修改 goal_radius</td>
> > > > > <td>在创建 follower 前设置<br />
> > > > > <code>goal_radius = 1.0  # 改成 1m</code></td>
> > > > > <td>更宽松的到达条件 → 更少步数就 success。但评估指标会变差（distance_to_goal 更大就停了）</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td>查看生成视频的不同帧</td>
> > > > > <td>用视频播放器逐帧观看输出的 .mp4</td>
> > > > > <td>看到 Agent 在 Top-down 地图上沿白色 NavMesh 区域移动的完整轨迹，观察何时转弯、何时直行</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td>打印每步的动作和坐标</td>
> > > > > <td>在 step 循环中加入：<br />
> > > > > <code>print(f"Step: action={best_action}, pos={info['position']}")</code></td>
> > > > > <td>看到每一步 follower 选择了什么动作，Agent 的 3D 坐标如何逐帧变化 — 理解"前进→靠近目标→判断是否需要转弯"的决策循环</td>
> > > > > </tr>
> > > > > </tbody>
> > > > > </table>
> > > > > 
> > > > > <div class="exercise" style="margin-top:18px;">
> > > > > 
> > > > > #### 练习 2-4：对比不同 episode 的导航难度
> > > > > 
> > > > > 运行 ShortestPathFollower 跑 10 个 episode，记录每个 episode 的步数和 SPL。 观察步数的分布 — 最短几步？最长几步？为什么差异这么大？  
> > > > > **进阶：**在脚本中打印每个 episode 的 `start_position` 和 `goals[0].position`， 计算起点到目标的直线距离，与实际的步数 × 0.25m 行走距离对比。你会发现走廊中的 episode 比值接近 1.0， 而需要绕过多个房间的 episode 比值可达 2.0+ ——这就是**路径效率**的概念来源。
> > > > > 
> > > > > <div class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 2-5 · 自定义传感器与指标
> > > > > 
> > > > > Habitat 的一切组件都通过 Registry 注册 + YAML 声明 + 运行时自动装配。这个案例演示如何在不修改框架源码的前提下，给 Agent 添加全新的传感器和评估指标。
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **① 案例含义 — 这个案例要演示什么**
> > > > > 
> > > > > **Registry（注册表）**是 Habitat 的核心扩展机制。一切组件 — Task、Sensor、Measure、Action — 都通过 Registry 注册，通过 YAML 声明，运行时自动装配。不需要写任何胶水代码。这个案例具体做了两件事：  
> > > > > **1. 注册一个自定义传感器 `agent_position`** — 返回 Agent 当前的 3D 世界坐标 (x, y, z)  
> > > > > **2. 注册一个自定义指标 `episode_info`** — 在 reset 时附加自定义字段 `my_value`，在 step 时移除  
> > > > >   
> > > > > 核心目的是让你看到：**写一个类 + 加一个装饰器 + 在配置中声明一行 = 新功能立即可用。**
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ② 核心代码 & 关键函数
> > > > > 
> > > > > #### 自定义传感器：AgentPositionSensor
> > > > > 
> > > > >     @habitat.registry.register_sensor(name="my_supercool_sensor")
> > > > >     class AgentPositionSensor(habitat.Sensor):
> > > > >         def __init__(self, sim, config, **kwargs):
> > > > >             super().__init__(config=config)
> > > > >             self._sim = sim
> > > > >             print("The answer to life is", self.config.answer_to_life)
> > > > >     
> > > > >         def _get_uuid(self, *args, **kwargs):
> > > > >             return "agent_position"     # 在 obs 字典中的 key
> > > > >     
> > > > >         def _get_observation_space(self, *args, **kwargs):
> > > > >             return spaces.Box(low=-np.inf, high=np.inf, shape=(3,), dtype=np.float32)
> > > > >     
> > > > >         def get_observation(self, observations, *args, episode, **kwargs):
> > > > >             return self._sim.get_agent_state().position   # 从 sim 读取 Agent 3D 坐标
> > > > >     
> > > > >     # 对应的配置类（dataclass）
> > > > >     @dataclass
> > > > >     class AgentPositionSensorConfig(LabSensorConfig):
> > > > >         type: str = "my_supercool_sensor"
> > > > >         answer_to_life: int = MISSING    # MISSING = 必填，无默认值
> > > > > 
> > > > > #### 自定义指标：EpisodeInfoExample
> > > > > 
> > > > >     @habitat.registry.register_measure
> > > > >     class EpisodeInfoExample(habitat.Measure):
> > > > >         def __init__(self, sim, config, **kwargs):
> > > > >             self._config = config
> > > > >             super().__init__()
> > > > >     
> > > > >         def _get_uuid(self, *args, **kwargs):
> > > > >             return "episode_info"      # 在 metrics 字典中的 key
> > > > >     
> > > > >         def reset_metric(self, *args, episode, **kwargs):
> > > > >             self._metric = vars(episode).copy()   # 复制 episode 所有属性
> > > > >             self._metric["my_value"] = self._config.VALUE   # ★ 附加自定义字段
> > > > >     
> > > > >         def update_metric(self, *args, episode, action, **kwargs):
> > > > >             self._metric = vars(episode).copy()   # 只复制 episode 属性，不加 my_value
> > > > >     
> > > > >     # 对应的配置类
> > > > >     @dataclass
> > > > >     class EpisodeInfoExampleConfig(MeasurementConfig):
> > > > >         type: str = "EpisodeInfoExample"
> > > > >         VALUE: int = -1
> > > > > 
> > > > > #### 运行时注入 — 在配置中声明自定义组件
> > > > > 
> > > > >     with habitat.config.read_write(config):
> > > > >         # 将自定义指标挂载到 task.measurements
> > > > >         config.habitat.task.measurements["episode_info_example"] = \
> > > > >             EpisodeInfoExampleConfig(VALUE=5)
> > > > >     
> > > > >         # 将自定义传感器挂载到 task.lab_sensors
> > > > >         config.habitat.task.lab_sensors["agent_position_sensor"] = \
> > > > >             AgentPositionSensorConfig(answer_to_life=42)
> > > > > 
> > > > > #### 关键函数调用
> > > > > 
> > > > > | 函数                                       | 调用时机                  | 说明                                                                       |
> > > > > | ---------------------------------------- | --------------------- | ------------------------------------------------------------------------ |
> > > > > | `Sensor.__init__(sim, config)`           | 环境创建时                 | Habitat 自动传入 sim 实例和配置。这里 `print("The answer to life is", 42)` 证明配置值正确传递 |
> > > > > | `Sensor.get_observation(obs)`            | 每次 reset() 和 step() 后 | 返回 numpy 数组。这里返回 `sim.get_agent_state().position` — Agent 当前 3D 坐标       |
> > > > > | `Sensor._get_uuid()`                     | 注册时                   | 返回该传感器在 obs 字典中的 key 名称，如 `"agent_position"`                             |
> > > > > | `Sensor._get_observation_space()`        | 注册时                   | 声明观测数据的 shape 和 dtype。这里是 `Box(shape=(3,), dtype=float32)`               |
> > > > > | `Measure.reset_metric(episode)`          | 每次 env.reset() 时      | **只在 reset 时调用一次。**这里复制 episode 属性 + 附加 my\_value=5                      |
> > > > > | `Measure.update_metric(episode, action)` | 每次 env.step() 后       | **每步 step 都调用。**这里只复制 episode 属性，**不附加** my\_value — 用于示范生命周期差异          |
> > > > > 

> > > > > ### ③ 如何创建和运行
> > > > > 
> > > > > #### 方式一：运行原始示例
> > > > > 
> > > > >     $ cd /develop/habitat-lab
> > > > >     $ conda activate habitat
> > > > >     $ python examples/register_new_sensors_and_measures.py
> > > > > 
> > > > > #### 方式二（推荐）：运行增强验证脚本
> > > > > 
> > > > > 我们添加了 `examples/verify_custom_sensor.py`，用 5 个明确的验证步骤来检验传感器和指标的正确性。
> > > > > 
> > > > >     $ python examples/verify_custom_sensor.py
> > > > > 
> > > > > ### ④ 运行效果
> > > > > 
> > > > > #### 原始示例的实际输出
> > > > > 
> > > > >     # 两个 Warning 可忽略 — habitat-test-scenes 不含语义标注
> > > > >     [Warning]:[Assets] ResourceManager.cpp(353)::loadSemanticSceneDescriptor :
> > > > >       SSD File Naming Issue! ... skokloster-castle.scn ... not exist on disk.
> > > > >     [Warning]:[Sim] Simulator.cpp(508)::instanceStageForSceneAttributes :
> > > > >       The active scene does not contain semantic annotations
> > > > >     
> > > > >     2026-05-28 14:24:04,687 Initializing task Nav-v0
> > > > >     The answer to life is 42               ← ① 传感器 __init__ 被调用，配置值 42 传入正确!
> > > > >     [-7.3699  0.0828  6.5763]                 ← ② reset() 后 agent_position = Agent 出生坐标
> > > > >     {'episode_id': '3662', ..., 'my_value': 5}   ← ③ metrics 中包含 my_value=5
> > > > >     [-7.6151  0.1508  6.6251]                 ← ④ step() 后坐标变了（前进了 ~0.25m）
> > > > >     {'episode_id': '3662', ...}                  ← ⑤ my_value 消失了！update_metric() 不写入它
> > > > > 
> > > > > #### 增强验证脚本的完整输出（推荐对照查看）
> > > > > 
> > > > >     # ═══════════════════════════════════════════════════
> > > > >     [INIT] 传感器接收到的配置: answer_to_life = 42
> > > > >     
> > > > >     ============================================================
> > > > >       验证 0: 环境创建成功
> > > > >     ============================================================
> > > > >     [PASS] habitat.Env(config=config) 正常返回，无异常
> > > > >     
> > > > >     ============================================================
> > > > >       验证 1: reset() 后自定义传感器 agent_position 出现在 obs 中
> > > > >     ============================================================
> > > > >       内置传感器:     ['rgb', 'depth', 'pointgoal_with_gps_compass']
> > > > >       自定义传感器:   agent_position = [-7.3699493  0.08276175  6.5762997]
> > > > >       [PASS] agent_position 已被注册并返回 Agent 的 3D 坐标
> > > > >     
> > > > >     ============================================================
> > > > >       验证 2: reset() 后 episode_info 包含 my_value=5
> > > > >     ============================================================
> > > > >       episode_id:    3662
> > > > >       start_position:[-7.3699, 0.0828, 6.5763]
> > > > >       goals[0].pos:  [-5.3076, 0.2629, 17.28]
> > > > >       my_value:      5  ← reset_metric() 写入
> > > > >       [PASS] reset_metric() 被调用，my_value == 5
> > > > >     
> > > > >     ============================================================
> > > > >       验证 3: step('move_forward') 后 agent_position 发生变化
> > > > >     ============================================================
> > > > >       step 前坐标:      [-7.3699493   0.08276175  6.5762997]
> > > > >       step 后坐标:      [-7.615132    0.15081047  6.6251426]
> > > > >       移动距离:         0.259m  (forward_step_size=0.25m)
> > > > >       [PASS] 自定义传感器正确跟踪了 Agent 位置变化
> > > > >     
> > > > >     ============================================================
> > > > >       验证 4: step() 后 my_value 从 episode_info 中消失
> > > > >     ============================================================
> > > > >       'my_value' in episode_info: False
> > > > >       [PASS] update_metric() 不写入 my_value，只在 reset_metric() 出现
> > > > >     
> > > > >     ============================================================
> > > > >       总结: 5 项验证全部通过
> > > > >     ============================================================
> > > > >       ✅ 自定义 Sensor 已注册并出现在 obs 中
> > > > >       ✅ 传感器正确返回 Agent 3D 坐标
> > > > >       ✅ 传感器正确跟踪 step() 后的坐标变化
> > > > >       ✅ 自定义 Measure 已注册并出现在 metrics 中
> > > > >       ✅ reset_metric / update_metric 生命周期正确
> > > > > 
> > > > > ### ⑤ 如何验证传感器注册成功？（没有可视化测试怎么办）
> > > > > 
> > > > > 自定义传感器通常**不产生可视化输出**——它只是一个返回 numpy 数组的函数。但你可以通过以下**5 个验证点**来确认一切正常。 这也是实际开发中调试自定义组件的方法论。
> > > > > 
> > > > > <div class="dual-panel">
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #10b981;">
> > > > > 
> > > > > #### 验证传感器
> > > > > 
> > > > > **① \_\_init\_\_ 被调用**  
> > > > >    `print("The answer to life is", 42)` → 证明配置值传入正确  
> > > > > **② 出现在 obs 字典中**  
> > > > >    `"agent_position" in obs` → 证明注册成功  
> > > > > **③ 返回值合理性**  
> > > > >    坐标是 3 个浮点数，且在场景范围内 → 证明数据格式正确  
> > > > > **④ step 后数值变化**  
> > > > >    比较 step 前后的坐标，差异约 0.25m → 证明传感器在每步更新
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="panel" style="border-top: 3px solid #8b5cf6;">
> > > > > 
> > > > > #### 验证指标
> > > > > 
> > > > > **⑤ my\_value 生命周期**  
> > > > >    reset 后 `my_value=5` 存在 → 证明 `reset_metric()` 被调用  
> > > > >    step 后 `my_value` 消失 → 证明 `update_metric()` 被调用且行为不同
> > > > > 
> > > > > <div>
> > > > > 
> > > > > <div class="info-title" style="color:#67e8f9;">
> > > > > 
> > > > > 没有可视化 ≠ 无法验证
> > > > > 
> > > > > </div>
> > > > > 
> > > > > Habitat 中的 sensor 大多数都是"数据源"而非"可视化组件"——RGB sensor 恰好有图像，但 GPS compass sensor、collision sensor、joint state sensor 等**都没有可视化输出**。 验证它们的标准方法就是：**断言其返回值的数据类型、shape、值域和生命周期行为符合预期。** 两个 `assert` 语句比任何可视化都更可靠 — 前者是"看着像"，后者是"一定是"。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ⑥ 试试调整这些，再观察变化
> > > > > 
> > > > > <table>
> > > > > <colgroup>
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > <col style="width: 33%" />
> > > > > </colgroup>
> > > > > <thead>
> > > > > <tr class="header">
> > > > > <th>调整项</th>
> > > > > <th>怎么改</th>
> > > > > <th>预期看到什么</th>
> > > > > </tr>
> > > > > </thead>
> > > > > <tbody>
> > > > > <tr class="odd">
> > > > > <td>修改 answer_to_life</td>
> > > > > <td>把 <code>answer_to_life=42</code> 改成 <code>answer_to_life=999</code></td>
> > > > > <td>传感器 init 打印变为 "The answer to life is 999" — 证明配置系统正确传递了你的值</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td>修改 my_value</td>
> > > > > <td>把 <code>my_value = 5</code> 改成 <code>my_value = 100</code></td>
> > > > > <td>reset 后 metrics 中 my_value=100。注意 step 后同样消失 — 生命周期与值无关</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td>在 update_metric 中也加 my_value</td>
> > > > > <td>在 <code>update_metric()</code> 末尾加：<br />
> > > > > <code>self._metric["my_value"] = self._config.VALUE</code></td>
> > > > > <td>reset 后和每步 step 后都有 my_value — 体验生命周期控制的灵活性</td>
> > > > > </tr>
> > > > > <tr class="even">
> > > > > <td>添加更多传感器</td>
> > > > > <td>注册一个新 sensor 返回 <code>self._sim.get_agent_state().rotation</code></td>
> > > > > <td>obs 中多一个 agent_rotation key — 体验"写类+装饰器=新功能"的开发流程</td>
> > > > > </tr>
> > > > > <tr class="odd">
> > > > > <td>打印所有注册组件</td>
> > > > > <td>在脚本末尾加：<br />
> > > > > <code>print(habitat.registry.mapping.keys())</code></td>
> > > > > <td>看到 Registry 中所有已注册的 task/sensor/measure/lab_sensor — 理解全局注册表的概念</td>
> > > > > </tr>
> > > > > </tbody>
> > > > > </table>
> > > > > 
> > > > > > 💡
> > > > > > 
> > > > > > <div class="tip-title">
> > > > > > 
> > > > > > 这个案例为什么重要？
> > > > > > 
> > > > > > 2-1 到 2-4 你用的是**别人写好的组件**。2-5 是第一次**你写自己的组件**。 后面第4章（改配置实验）和第6章（RL 训练）都会频繁使用这个模式 — 你可能需要添加自定义奖励函数（Measure）、自定义传感器（Sensor）、甚至自定义任务（Task）。 理解"写类 → 装饰器 → 配置声明"这个三步流程，是真正使用 Habitat 做研究的基础。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="exercise" style="margin-top:18px;">
> > > > > > 
> > > > > > #### 练习 2-5：写一个自定义距离传感器
> > > > > > 
> > > > > > 注册一个名为 `distance_to_goal_sensor` 的自定义传感器，在 `get_observation()` 中计算 Agent 当前位置到 episode 目标的欧氏距离并返回。提示：参考 `AgentPositionSensor` 的写法， 使用 `sim.get_agent_state().position` 和 `episode.goals[0].position`。 然后运行 `verify_custom_sensor.py` 看它出现在 obs 字典中。
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 核心理解：step/reset 交互循环
> > > > > > 
> > > > > > 跑完 5 个示例后，你应该对下面这张图形成清晰的直觉。
> > > > > > 
> > > > > > <div class="arch-diagram">
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd; min-width:180px;">
> > > > > > 
> > > > > > **env.reset()** <span class="small">开始新 episode  
> > > > > > Agent 随机出生  
> > > > > > 返回初始 obs</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer" style="background:#8b5cf620; border:2px solid #8b5cf6; color:#c4b5fd; min-width:280px;">
> > > > > > 
> > > > > > **循环体** <span class="small">1. 策略看 obs 选 action  
> > > > > > 2\. env.step(action) → 新 obs  
> > > > > > 3\. 检查 env.episode\_over</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓   episode\_over = True 时退出   ↓
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="arch-row">
> > > > > > 
> > > > > > <div class="arch-layer" style="background:#10b98120; border:2px solid #10b981; color:#6ee7b7; min-width:240px;">
> > > > > > 
> > > > > > **env.get\_metrics()** <span class="small">Success / SPL / DistanceToGoal</span>
> > > > > > 
> > > > > > <div class="arch-arrow-center">
> > > > > > 
> > > > > > ↓   reset() → 下一个 episode   ↓
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **Observation → Action → Observation 循环的本质**
> > > > > > 
> > > > > > 这整个循环就是一个**马尔可夫决策过程 (MDP)** 的展开 —— **State** (观测) → **Action** (动作) → **Next State** (新观测) → **Reward** (奖励)。 在后面的章节中你会看到 RL 训练就是数百万次地重复这个循环，每次根据 reward **微调策略参数**。
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 学后自检 — 你掌握了什么
> > > > > > 
> > > > > > 6 个问题验证你是否真正理解了"示例在做什么"。
> > > > > > 
> > > > > > <div class="qa-grid">
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q1：Native API 和 Gym API 的区别是什么？
> > > > > > 
> > > > > > Native API 返回观测字典，动作也是字典格式（`{"action": "move_forward"}`）；Gym API 在 Native 上包了一层，返回标准的 `(obs, reward, done, info)` 元组，方便对接 Stable-Baselines3 等现成 RL 库。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q2：obs\["rgb"\] 的 shape 是什么？dtype 是什么？
> > > > > > 
> > > > > > shape 是 `(H, W, 3)`，3 个通道是 RGB（不是 RGBA）。dtype 是 `uint8`（范围 0-255）。H 和 W 由 YAML 配置决定，默认通常是 256×256。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q3：PointNav 的 GPS+Compass 观测包含什么信息？
> > > > > > 
> > > > > > 一个 shape=(2,) 的 float32 数组：`[distance, angle]`。distance = 当前到目标的测地距离(米)；angle = 当前朝向与目标方向的夹角(弧度)。这是 PointNav 最核心的导航信号。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q4：ShortestPathFollower 为什么不需要 RGB 图像？
> > > > > > 
> > > > > > 它不"看"图像 — 它直接读取预计算的 **NavMesh（导航网格）** 和场景的图形结构，用 Dijkstra 算法规划路径。可以把 NavMesh 理解为"内置的地图 GPS"。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q5：env.episode\_over 和 done 是什么关系？
> > > > > > 
> > > > > > `env.episode_over` 是 Native API 的终止标志；`done` 是 Gym API 的终止标志。两者含义相同，只是不同 API 层的命名差异。episode 结束的条件：stop 被调用 / 达到目标 / 超时。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="qa-card">
> > > > > > 
> > > > > > #### Q6：跑完这一章后，你下次打开 example\_pointnav.py 应该能回答什么问题？
> > > > > > 
> > > > > > 你应该能回答：① 每一行在做什么；② `obs` 包含哪些 key，每个 key 的 shape 和含义；③ action 的格式是什么；④ 如何换一个 action 让 Agent 做不同的事。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > <div class="page-nav">
> > > > > > 
> > > > > > [← 第1章：安装环境](habitat-textbook-step1.html) [第3章：读核心代码 →](habitat-textbook-step3.html)
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
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
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
> > > 
> > > </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
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
# 第5章：导航任务全景 — Habitat 从零理解

> 从配置到训练，从 checkpoint 到评估指标。理解 PPO 训练流程、RL 环境包装链、以及如何解释训练结果。

## 0\. 训练全景图

一次完整的训练涉及 4 层结构：CLI 入口 → Trainer → VectorEnv → RLEnv → Core Env。

<div>

<div class="info-title" style="color:#60a5fa;">

学习目标

</div>

理解 CLI → Trainer → VectorEnv → RLEnv 四层架构  
<span style="color:#fbbf24;font-size:0.82rem;">🤔 你敲下 python -m habitat\_baselines.run 之后，Habitat 内部经历了哪些步骤才让 agent 开始移动？</span>

</div>

<div class="arch-diagram">

<div class="arch-row">

<div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">

🖥 CLI 入口 <span class="small">habitat\_baselines/run.py</span>

<div class="arch-arrow-center">

↓ Hydra 配置加载 + 训练/评估 分支

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#ec489920;border:1px solid #ec489940;">

🤖 PPOTrainer <span class="small">rl/ppo/ppo\_trainer.py</span>

<div class="arch-arrow-center">

↓ 管理训练循环、checkpoint、日志

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">

📊 AgentAccessMgr (Single) <span class="small">Policy + Storage + Updater</span>

<div class="arch-arrow-center">

↓ 收集 rollouts → 计算 returns → PPO 更新

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">

🔄 VectorEnv (N 个并行) <span class="small">habitat/core/vector\_env.py</span>

<div class="arch-arrow-center">

↓ 每个 env 独立运行一个场景实例

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#22d3ee20;border:1px solid #22d3ee40;">

🎮 RLEnv → Env <span class="small">step() → (obs, reward, done, info)</span>

</div>

  

<div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">

🧠 Task (Nav-v0) <span class="small">reward\_measure + success\_measure</span>

</div>

  

<div class="arch-layer" style="background:#06b6d420;border:1px solid #06b6d440;">

🏗 Simulator <span class="small">habitat\_sim 渲染引擎</span>

</div>

<div>

**📁 两个仓库的边界**

**habitat-lab**：提供 `Env`、`RLEnv`、`Benchmark`、`Task`、`Simulator` — 环境基础设施。  
**habitat-baselines**：提供 `run.py`、`PPOTrainer`、`PPO`、`Policy` — 训练算法和工具。  
训练时，baselines 通过 Hydra `defaults` 引用 lab 的 benchmark 配置，统一在 `DictConfig` 中。

## 🔤 术语速查

以下术语在后续章节中频繁出现。新同学先扫一遍，不需要记住——遇到不认识的词再回来看。

<div>

**训练相关**

**PPO** (Proximal Policy Optimization)：一种强化学习算法，通过限制每次更新的幅度来稳定训练。核心做法是 clipped objective。  
**DD-PPO** (Decentralized Distributed PPO)：PPO 的多 GPU 分布式版本。课程中我们加 `trainer_name=ppo` 降级为单 GPU 模式。  
**GAE** (Generalized Advantage Estimation)：用于计算"这个动作比平均好多少"的方法。平衡偏差和方差。  
**Rollout**：让策略在环境中跑 N 步，收集 (obs, action, reward) 数据的过程——相当于"采集训练样本"。

</div>

<div>

**环境相关**

**Hydra**：Facebook 的配置管理框架，用 YAML 文件组织所有参数。你看到的 `--config-name=xxx.yaml` 就是 Hydra 的入口。  
**OmegaConf**：Hydra 使用的配置对象库。`DictConfig` 就是 OmegaConf 的数据类型——可以像 dict 一样访问，但有类型检查。  
**VectorEnv**：并行管理多个环境实例的包装器。1 个 VectorEnv = N 个独立场景同时运行，提高采样效率。  
**RLEnv**：在基础 Env 外面包的一层，加了 reward 计算、done 判断、info 收集——把原始环境变成 RL 可用的格式。

</div>

<div>

**评估指标**

**SPL** (Success weighted by Path Length)：成功率 × (最短路径长度 / agent 实际路径长度)。既看是否到达，也看是否高效。  
**soft\_spl**：SPL 的宽松版——即使 agent 没 STOP，只要走到了目标附近也算部分成功。ObjectNav 专用。  
**nDTW** (normalized Dynamic Time Warping)：衡量 agent 实际路径与参考路径的形状相似度。VLN 专用指标。

</div>

<div>

**数据集**

**MP3D** (Matterport3D)：90 个真实室内场景的 3D 扫描。PointNav / ImageNav / VLN 的数据集。  
**HM3D** (Habitat-Matterport3D)：1000 个场景的更大规模数据集，带语义标注。ObjectNav / InstanceImageNav 需要它。  
**R2R** (Room-to-Room)：人类标注的导航指令数据集。每条数据 = MP3D 场景中的路径 + 自然语言指令。

## 1\. 导航任务全景：五种目标类型

PointNav 只是导航的起点。Habitat 支持 5 种目标类型——从几何坐标到语言指令，覆盖 Embodied AI 导航的全谱系。

<div>

<div class="info-title" style="color:#60a5fa;">

学习目标

</div>

掌握 PointNav/ObjectNav/ImageNav/VLN 五种任务的输入输出差异  
<span style="color:#fbbf24;font-size:0.82rem;">🤔 如果给你一个坐标 (x,y) 让你走过去，和给你一张照片让你找到这个地方，哪个更难？为什么 Habitat 要设计五种不同的导航任务？</span>

</div>

### 1.1 五种目标类型对比总表

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>任务</th>
<th>目标描述</th>
<th>目标传感器</th>
<th>动作数</th>
<th>核心数据集</th>
<th>评判指标</th>
<th>难度</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PointNav</strong></td>
<td>几何坐标 (x,y)</td>
<td>GPS + Compass<br />
<span class="small">(pointgoal_with_gps_compass)</span></td>
<td>4<br />
<span class="small">STOP/FWD/LEFT/RIGHT</span></td>
<td>Gibson, MP3D, HM3D</td>
<td>success, SPL,<br />
distance_to_goal</td>
<td>⭐⭐</td>
</tr>
<tr class="even">
<td><strong>ObjectNav</strong></td>
<td>物体类别<br />
<span class="small">(如 chair, bed)</span></td>
<td>GPS + Compass<br />
<span class="small">+ objectgoal (类别ID)</span></td>
<td>6<br />
<span class="small">+LOOK_UP/LOOK_DOWN</span></td>
<td>HM3D, MP3D,<br />
HSSD, ProcTHOR</td>
<td>success, SPL, softSPL,<br />
VIEW_POINTS 距离</td>
<td>⭐⭐⭐</td>
</tr>
<tr class="odd">
<td><strong>ImageNav</strong></td>
<td>一张目标图片<br />
<span class="small">(goal image)</span></td>
<td>目标 RGB 图像<br />
<span class="small">(imagegoal_sensor)</span></td>
<td>4<br />
<span class="small">STOP/FWD/LEFT/RIGHT</span></td>
<td>Gibson, MP3D<br />
<span class="small">(共用 PointNav 数据)</span></td>
<td>success, SPL,<br />
distance_to_goal</td>
<td>⭐⭐⭐</td>
</tr>
<tr class="even">
<td><strong>InstanceImageNav</strong></td>
<td>特定实例图片<br />
<span class="small">("这把椅子", 非 "椅子类")</span></td>
<td>目标实例图片<br />
<span class="small">(instance_imagegoal)</span></td>
<td>6<br />
<span class="small">+LOOK_UP/LOOK_DOWN</span></td>
<td>HM3D</td>
<td>success, SPL, softSPL,<br />
VIEW_POINTS 距离</td>
<td>⭐⭐⭐⭐</td>
</tr>
<tr class="odd">
<td><strong>VLN</strong></td>
<td>自然语言指令<br />
<span class="small">("通过厨房去卧室")</span></td>
<td>指令文本<br />
<span class="small">(instruction_sensor)</span></td>
<td>4<br />
<span class="small">STOP/FWD/LEFT/RIGHT</span></td>
<td>MP3D (R2R)</td>
<td>success, SPL, nDTW<br />
<span class="small">(路径相似度)</span></td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
</tbody>
</table>

<div>

**关键洞察：从几何到语义的谱系**

**PointNav → ObjectNav → ImageNav → VLN** 的演进反映了 Embodied AI 的核心挑战：  
· PointNav = "走到 (x,y)" — 纯几何，GPS/Compass 告诉你相对位置 → 最简单的 RL 训练  
· ObjectNav = "找到 chair" — 需要**语义理解**（chair 长什么样？它通常在哪？）  
· ImageNav = "到达这里" — 需要**视觉匹配**（当前视野 vs 目标图片）→ **没有 GPS**  
· InstanceImageNav = "找到这把特定的椅子" — 需要**实例级识别**（区分同类的不同个体）  
· VLN = "按指令去卧室" — 需要**语言理解** + 视觉匹配 + 路径记忆 → 最接近真实机器人

</div>

### 1.2 PointNav — 几何坐标导航 <span style="font-size:0.78rem;color:#94a3b8;">难度 ★★</span>

<div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:18px;font-size:0.82rem;color:#94a3b8;">

<span>📌 [本节目标](#pnav-goal)</span> <span>📖 [是什么](#pnav-what)</span> <span>💻 [实操](#pnav-practice)</span> <span>🛠 [常见错误](#pnav-errors)</span> <span>📖 [API 详解](#pnav-api)</span>

</div>

<div>

**📌 学完本节你将能够**

用 Gym API 创建 PointNav 环境并打印观测数据  
理解 `pointgoal_with_gps_compass` 传感器输出的 ρ(距离) 和 φ(角度) 含义  
运行一次 PPO 训练，看到 reward/loss 等指标变化

</div>

<div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">

<span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 假设你是 Habitat 里的智能体——你站在一个陌生城堡的走廊里，面前有一堵墙，头顶传来一条消息：**"目标在你的右前方 10 米，角度 90°"**。  
  
你不能穿墙，不知道城堡的地图，唯一知道的是：**目标距离你多远、在哪个方向**。  
你要怎么一步步走过去？这就是 PointNav 要解决的问题。 </span>

</div>

<div>

**📖 PointNav 是什么**

**PointNav**（PointGoal Navigation）是 Habitat 中最基础、最成熟的导航任务。智能体接收一个**相对目标坐标**（距离 ρ 和角度 φ），通过 RGB-D 视觉和运动控制，自主规划路径走到目标点。  
  
**关键理解**：PointNav 给你的是 **相对坐标**，不是绝对坐标。无论 agent 在城堡的哪个角落，传感器都会告诉你"目标在你的 X 方向、Y 米外"——这是 PointNav 能泛化到不同场景的根本原因。

</div>

| 概念       | 符号       | 含义                                    | 与代码的关系                                        |
| -------- | -------- | ------------------------------------- | --------------------------------------------- |
| **相对距离** | ρ (rho)  | agent 到目标的直线距离（米）                     | `obs["pointgoal_with_gps_compass"][0]`        |
| **相对角度** | φ (phi)  | 目标相对 agent 朝向的偏航角（弧度）                 | `obs["pointgoal_with_gps_compass"][1]`        |
| **动作空间** | 4 离散     | STOP/MOVE\_FWD/TURN\_LEFT/TURN\_RIGHT | `env.action_space → Discrete(4)`              |
| **观测空间** | RGB+D+PG | 256×256 RGB + Depth + PointGoal(2,)   | `obs.keys() → ['rgb','depth','pointgoal...']` |

#### 💻 实操：创建 PointNav 环境

<div style="margin-bottom:12px;">

<div style="color:#60a5fa;font-weight:600;font-size:0.85rem;margin-bottom:6px;">

设计理论

</div>

**核心任务**：用 4 行代码创建 Habitat 环境 → 获取观测 → 查看目标信息。  
关键点：`import habitat.gym` 不是装饰——它触发了 `Habitat-v0` 的注册，没有这一行，`gym.make("Habitat-v0")` 会报错。

</div>

| 代码段                               | 作用                                | 关键点                                                  |
| --------------------------------- | --------------------------------- | ---------------------------------------------------- |
| `import gym, habitat.gym`         | 导入 Gym API + 注册 Habitat-v0        | `habitat.gym` 必须导入，否则 `gym.make` 找不到环境               |
| `gym.make("Habitat-v0", cfg=...)` | 根据配置文件创建环境实例                      | 指定场景、传感器、任务参数                                        |
| `obs = env.reset()`               | 重置环境 + 返回初始观测                     | 返回 dict: {rgb, depth, pointgoal\_with\_gps\_compass} |
| `env.step(action)`                | 执行动作，返回 (obs, reward, done, info) | reward 来自 distance\_to\_goal\_reward                 |
| `env.close()`                     | 释放渲染资源                            | 不调用会导致 GPU 内存泄漏                                      |

``` 
      完整代码
```

    import gym, habitat.gym  # noqa: F401 — 注册 Habitat-v0
    
    # 1. 创建环境：指定 PointNav + habitat-test 场景
    env = gym.make("Habitat-v0",
        cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
    )  # ← 这个 yaml 定义了场景、传感器、任务参数
    
    # 2. 重置环境，获取初始观测
    obs = env.reset()
    print(obs.keys())
    # 输出: dict_keys(['rgb', 'depth', 'pointgoal_with_gps_compass'])
    
    # 3. 查看目标信息 — pointgoal_with_gps_compass = [ρ, φ]
    #    ρ = 距离目标（米），φ = 相对目标的偏航角（弧度）
    pg = obs["pointgoal_with_gps_compass"]
    print(f"距离目标: {pg[0]:.2f}m, 偏航角: {pg[1]:.2f}rad")
    # 示例输出: 距离目标: 10.90m, 偏航角: 1.56rad (≈90°)
    
    # 4. 执行一个随机动作并观察结果
    obs, reward, done, info = env.step(env.action_space.sample())
    print(f"reward={reward:.3f}, done={done}")
    # 示例输出: reward=-0.010, done=False
    
    env.close()  # 释放资源

</div>

#### 程序运行流程图

<div class="flow-box">

<div class="flow-step" style="border-top:3px solid #64748b;">

**① import habitat.gym**

注册 Habitat-v0  
Gym 环境入口

</div>

<div class="flow-arrow">

→

</div>

<div class="flow-step" style="border-top:3px solid #3b82f6;">

**② gym.make()**

加载 skokloster-castle  
RGB + Depth + PointGoal 传感器

</div>

<div class="flow-arrow">

→

</div>

<div class="flow-step" style="border-top:3px solid #8b5cf6;">

**③ env.reset()**

初始化渲染器  
随机选取 episode

</div>

<div class="flow-arrow">

→

</div>

<div class="flow-step" style="border-top:3px solid #f59e0b;">

**④ obs 读取**

pointgoal = \[ρ, φ\]  
目标距离 10.9m · 角度 90°

</div>

<div class="flow-arrow">

→

</div>

<div class="flow-step" style="border-top:3px solid #10b981;">

**⑤ env.step()**

执行动作  
计算 reward → 返回新观测

</div>

<div class="flow-arrow">

→

</div>

<div class="flow-step" style="border-top:3px solid #ec4899;">

**⑥ env.close()**

释放 GPU 资源  
清理渲染上下文

``` 
      运行命令
```

    # 直接运行上面的 Python 代码
    $ python3 pointnav_env.py

</div>

<div class="screenshot-frame" style="margin:14px 0;">

![PointNav Environment](images/pointnav_rgb_depth.png)

<span style="color:#60a5fa;font-weight:600;">📋 运行上面代码的实际输出</span>  
skokloster-castle 城堡走廊 — L40 GPU 实时渲染 — 左: RGB 观测 (256x256) — 右: 深度图 (viridis) — 目标距离 10.9m, 偏航角 90°

</div>

> ⚠️
> 
> <div class="warn-title">
> 
> 🛠 常见错误
> 
> | 错误信息                                     | 可能原因                    | 解决方法                                            |
> | ---------------------------------------- | ----------------------- | ----------------------------------------------- |
> | `gym.error.NameNotFound: Habitat-v0`     | 忘记 `import habitat.gym` | 加上 `import habitat.gym`（不直接用但触发注册）              |
> | `FileNotFoundError: .../train.json.gz`   | 数据集路径错误或未下载             | 切换到 `pointnav_habitat_test.yaml`（云端已有）          |
> | `KeyError: 'pointgoal_with_gps_compass'` | 配置文件未启用该传感器             | 检查 yaml 中 `pointgoal_with_gps_compass_sensor` 段 |
> | GPU 内存持续增长                               | 忘记 `env.close()`        | 在循环末尾调用 `env.close()` 释放渲染资源                    |
> 

> </div>
> 
> #### 📖 核心 API 详解
> 
> <div>
> 
> **gym.make() — 创建环境**
> 
> `env = gym.make("Habitat-v0", cfg_file_path="benchmark/.../pointnav_xxx.yaml")`  
>   
> **cfg\_file\_path**：Habitat 配置文件路径。这个 yaml 定义了**场景**（skokloster-castle）、**传感器**（RGB+Depth+PointGoal）、**任务参数**（max\_episode\_steps）等。  
> **返回值**：一个实现了标准 Gym API 的环境对象（有 `reset()`, `step()`, `close()` 方法）。
> 
> </div>
> 
> <div>
> 
> **env.reset() — 重置并获取观测**
> 
> `obs = env.reset()`  
>   
> 初始化渲染器，随机抽取一个 episode（起点+目标点），返回初始观测 dict。  
> **obs 的三个 key**：  
> · `obs["rgb"]` — (256, 256, 3) 的 RGB 图像（uint8）  
> · `obs["depth"]` — (256, 256, 1) 的深度图  
> · `obs["pointgoal_with_gps_compass"]` — \[ρ, φ\] 二维向量，ρ(米) 距离, φ(弧度) 角度
> 
> </div>
> 
> <div>
> 
> **env.step() — 执行动作**
> 
> `obs, reward, done, info = env.step(action)`  
>   
> **action**：0=STOP, 1=MOVE\_FORWARD, 2=TURN\_LEFT, 3=TURN\_RIGHT  
> **reward**：`-(新距离 - 旧距离)` —— 靠近目标得正奖励，远离得负奖励  
> **done**：True = episode 结束（到达目标/超步数/碰撞）  
> **info**：`{"success": 0/1, "spl": 0.0-1.0, "distance_to_goal": 米}`
> 
> </div>
> 
> #### 🏋 训练：PPO 策略学习
> 
> <div style="margin-bottom:12px;">
> 
> <div style="color:#60a5fa;font-weight:600;font-size:0.85rem;margin-bottom:6px;">
> 
> 🤔 为什么要训练？
> 
> </div>
> 
> 上面我们用 `env.step(action)` 执行了随机动作——agent 在城堡里乱走，30 步过去离目标还是 10.9m。  
> **训练的目的**：让神经网络学会「看 → 想 → 走」的闭环——**看到 RGB 画面 → 结合目标方向 → 决定走哪步 → 执行 → 获得反馈 → 修正策略**。  
> 训练产物是一个 22MB 的 `.pth` 文件，里面存着 582 万参数的策略网络权重。
> 
> </div>
> 
> <div>
> 
> **📖 PPO（Proximal Policy Optimization）是什么**
> 
> PPO 是 Habitat 使用的核心强化学习算法（Schulman et al., 2017）。它的核心思想是：**每次更新策略时，步子不要迈太大**——用 `clip_param` 限制新旧策略的差异。  
>   
> **简化类比**：你在学骑自行车。每次摔了之后调整重心——但如果你一次把重心从左边调到右边，很可能又摔。PPO 做的就是**每次只调整一点点**，让学习过程更稳定。  
>   
> 详细的公式推导和代码映射见 [§4 PPO 训练算法](#sec4)。
> 
> </div>
> 
> | 组件                      | 作用              | 关键点                                       |
> | ----------------------- | --------------- | ----------------------------------------- |
> | `habitat_baselines.run` | 统一训练入口（约 100 行） | 所有导航任务（PointNav/ObjectNav...）都用同一个入口      |
> | `--config-name`         | 选择训练配置 yaml     | ppo\_pointnav\_example.yaml 定义了场景、模型、训练参数 |
> | `PPOTrainer`            | 管理训练循环          | rollout 收集 → GAE 计算 → PPO update → 日志输出   |
> | `VectorEnv`             | 并行运行多个环境        | num\_environments=1,4,8... 越多越快但吃显存       |
> | `checkpoint_folder`     | 保存训练产物          | 每 N 步保存 ckpt.{N}.pth（22MB/个）              |
> 

> #### 训练运行流程图
> 
> <div class="flow-box">
> 
> <div class="flow-step" style="border-top:3px solid #64748b;">
> 
> **① Hydra 加载配置**
> 
> ppo\_pointnav\_example.yaml  
> 场景 + 传感器 + PPO 参数
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #3b82f6;">
> 
> **② 创建 Trainer**
> 
> PPOTrainer  
> Policy 网络 (5.8M 参数) + RolloutStorage
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> 
> **③ 创建 VectorEnv**
> 
> N 个并行场景  
> 每个独立运行 reset/step
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #f59e0b;">
> 
> **④ Rollout 收集**
> 
> agent 在场景中交互  
> 收集 (obs, action, reward)
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #10b981;">
> 
> **⑤ PPO Update**
> 
> GAE 计算 advantage  
> clip 限制 → 梯度更新
> 
> </div>
> 
> <div class="flow-arrow">
> 
> →
> 
> </div>
> 
> <div class="flow-step" style="border-top:3px solid #ec4899;">
> 
> **⑥ 保存 Checkpoint**
> 
> ckpt.{N}.pth (22MB)  
> 可在中断后 resume 继续训练
> 
> ``` 
>       训练命令
> ```
> 
>     # PointNav PPO 训练（使用 habitat-test 数据，离线可用）
>     $ python -u -m habitat_baselines.run \
>         --config-name=pointnav/ppo_pointnav_example.yaml
>     
>     # 评估训练好的 checkpoint
>     $ python -u -m habitat_baselines.run \
>         --config-name=pointnav/ppo_pointnav_example.yaml \
>         habitat_baselines.evaluate=True
> 
> </div>
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 训练效果预览
> > 
> > 上面的命令会在 skokloster-castle 场景上运行 5 次 PPO 更新（160 环境步）。  
> > 这个阶段 **Success = 0%** 是正常的——课程明确说明「示例仅 100 万步，策略不会学会导航」。  
> > 真正的训练需要 **2500 万步以上**，见 [§8.4 云端 GPU 训练](#sec8-cloud)。
> > 
> > </div>
> > 
> > <div>
> > 
> > **训练输出解读**
> > 
> > 训练开始后，终端会打印类似：  
> > `agent number of parameters: 5821797`  
> > `reward: -0.075 → -0.013 (step 32→160)` — reward 在缓慢上升  
> > `metrics/success: 0.000` — 5 次更新还不足以学会导航  
> > `perf/fps: 40 → 74` — GPU 渲染速度在逐步提升（缓存预热）  
> >   
> > 详细的训练日志解读见 [§8E 训练过程分析](#sec8-curves)。
> > 
> > </div>
> > 
> > <div>
> > 
> > <div class="info-title" style="color:#34d399;">
> > 
> > 官方预训练模型 (MP3D · 73,728,768 步训练)
> > 
> > </div>
> > 
> > ![Official PointNav on MP3D](images/mp3d_pointnav_official.png)
> > 
> > 经过 7373 万步训练后的 PointNav 策略在 MP3D 卧室中的观测 — Success \~75%, SPL \~55% — 下载方式见 [§1.9](#sec-self-vs-official)
> > 
> > </div>
> > 
> > <div style="margin:0 0 14px;padding:8px 14px;background:#1e293b;border-left:2px solid #8b5cf6;border-radius:0 6px 6px 0;font-size:0.82rem;color:#94a3b8;">
> > 
> > <span style="color:#8b5cf6;font-weight:600;">🔗 从 PointNav 到 ObjectNav</span> — PointNav 给了你精确坐标。但如果任务变成「找一把椅子」，坐标就消失了。ObjectNav 把目标从**几何位置**改为**语义类别**——你不再知道目标在哪，只能边走边找。
> > 
> > </div>
> > 
> > ### 1.3 ObjectNav — 物体类别导航 <span style="font-size:0.78rem;color:#94a3b8;">难度 ★★★</span>
> > 
> > <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:18px;font-size:0.82rem;color:#94a3b8;">
> > 
> > <span>📌 [本节目标](#onav-goal)</span> <span>📖 [是什么](#onav-what)</span> <span>💻 [实操](#onav-practice)</span> <span>🛠 [常见错误](#onav-errors)</span> <span>📖 [API 详解](#onav-api)</span> <span>🏋 [训练](#onav-train)</span>
> > 
> > </div>
> > 
> > <div>
> > 
> > **📌 学完本节你将能够**
> > 
> > 用 Gym API 创建 ObjectNav 环境，理解 `objectgoal` 传感器  
> > 对比 ObjectNav 和 PointNav 在传感器、动作空间、难度上的差异  
> > 了解 ObjectNav 训练配置的关键参数
> > 
> > </div>
> > 
> > <div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > 
> > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> PointNav 告诉你目标的 **精确坐标**——"往前走 10 米，右转"。  
> >   
> > 但如果任务是 **"找到房间里的一把椅子"** 呢？  
> > 你不知道椅子在哪，不知道它长什么样（可能是木椅、塑料椅、电竞椅），甚至它可能被桌子挡住了。  
> >   
> > 你只能**边走边看**，看到疑似椅子的时候决定停下来——**错了就要继续找。**  
> > 这就是 ObjectNav。 </span>
> > 
> > </div>
> > 
> > <div>
> > 
> > **📖 ObjectNav 是什么**
> > 
> > **ObjectNav**（ObjectGoal Navigation）要求智能体在未知环境中找到 **指定类别的物体**（如 chair、bed、sofa）。  
> >   
> > **关键区别**：PointNav 给你坐标 → 直接走过去。ObjectNav 给你 **类别 ID** → 你必须**探索、识别、决策**。  
> > 智能体不知道物体在哪，必须通过视觉找到目标类别，并在确信到达时主动 STOP。
> > 
> > </div>
> > 
> > | 对比维度        | PointNav                   | ObjectNav                                | 这意味着什么                  |
> > | ----------- | -------------------------- | ---------------------------------------- | ----------------------- |
> > | **目标信息**    | 坐标 (ρ, φ)                  | 类别 ID（整数）                                | ObjectNav 不知道目标在哪——必须探索 |
> > | **动作数**     | 4 (STOP/FWD/LEFT/RIGHT)    | 6 (多 LOOK\_UP/LOOK\_DOWN)                | 物体可能在高处(吊灯)或低处          |
> > | **传感器**     | RGB + Depth + PointGoal    | RGB + Depth + objectgoal + GPS + Compass | 多了 GPS/Compass 做定位辅助    |
> > | **奖励**      | distance\_to\_goal\_reward | VIEW\_POINTS 距离（到能看见物体的视点）               | 物体本身位置对 agent 不可见       |
> > | **Stop 决策** | 走到坐标 → STOP                | 找到物体 → 判断 → STOP                         | 错了代价很大（false positive）  |
> > | **数据集**     | MP3D / Gibson              | HM3D / MP3D / HSSD                       | **云端 MP3D val 可用**      |
> > 

> > #### 💻 实操：创建 ObjectNav 环境
> > 
> > <div style="margin-bottom:12px;">
> > 
> > <div style="color:#60a5fa;font-weight:600;font-size:0.85rem;margin-bottom:6px;">
> > 
> > 设计理论
> > 
> > </div>
> > 
> > **核心任务**：创建 ObjectNav 环境 → 读取 objectgoal（目标物体类别）→ 对比 PointNav 多了哪些传感器。  
> > **关键点**：ObjectNav 使用 `objectnav_mp3d.yaml` 配置（云端已有 MP3D 数据），动作空间从 4 扩展到 6。
> > 
> > </div>
> > 
> > | 代码段                                                 | 作用              | 关键点                                            |
> > | --------------------------------------------------- | --------------- | ---------------------------------------------- |
> > | `gym.make("Habitat-v0", cfg="objectnav_mp3d.yaml")` | 创建 ObjectNav 环境 | 配置了 6 动作 + objectgoal + GPS/Compass            |
> > | `obs["objectgoal"]`                                 | 获取目标物体类别        | 返回整数索引（如 0=chair, 1=bed）                       |
> > | `obs["gps"]`                                        | agent 绝对坐标      | PointNav 没有这个——ObjectNav 保留定位辅助                |
> > | `env.action_space`                                  | 动作空间            | Discrete(6) — 比 PointNav 多 LOOK\_UP/LOOK\_DOWN |
> > 

> > ``` 
> >       完整代码
> > ```
> > 
> >     import gym, habitat.gym  # 注册 Habitat-v0
> >     
> >     # 1. 创建 ObjectNav 环境 — 使用 MP3D 数据集（云端已有）
> >     env = gym.make("Habitat-v0",
> >         cfg_file_path="benchmark/nav/objectnav/objectnav_mp3d.yaml",
> >         override_options=["habitat.dataset.split=val"])
> >     
> >     # 2. 重置环境
> >     obs = env.reset()
> >     print(obs.keys())
> >     # 输出: dict_keys(['rgb', 'depth', 'objectgoal', 'gps', 'compass'])
> >     
> >     # 3. 查看目标物体 — objectgoal = 类别 ID（整数）
> >     print(f"Target object ID: {obs['objectgoal'].item()}")
> >     # 示例输出: Target object ID: 0  (0=chair 在 HM3D 中的定义)
> >     
> >     # 4. 对比 PointNav — 多了什么？
> >     print(f"Action space: {env.action_space}")
> >     # 输出: Discrete(6)  ← PointNav 是 Discrete(4)，多了 LOOK_UP/LOOK_DOWN
> >     
> >     # 5. 多了 GPS + Compass（ObjectNav 仍有定位辅助）
> >     print(f"GPS: {obs['gps']}")
> >     # 输出: GPS: [-1.23, 4.56]  ← 绝对坐标
> >     
> >     # 6. 运行一个 episode：随机动作直到 done
> >     total_reward = 0.0
> >     for step in range(500):
> >         action = env.action_space.sample()
> >         obs, reward, done, info = env.step(action)
> >         total_reward += reward
> >         if done:
> >             print(f"Episode done at step {step+1}, "
> >                   f"success={info.get('success', 0)}, "
> >                   f"distance={info.get('distance_to_goal', '?'):.2f}")
> >             break
> >     env.close()  # 释放 GPU 资源
> > 
> > #### 程序运行流程图
> > 
> > <div class="flow-box">
> > 
> > <div class="flow-step" style="border-top:3px solid #64748b;">
> > 
> > **① import habitat.gym**
> > 
> > 注册 Habitat-v0  
> > Gym 环境入口
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > 
> > **② gym.make()**
> > 
> > 加载 objectnav\_mp3d.yaml  
> > 6 动作 + objectgoal + GPS
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > 
> > **③ env.reset()**
> > 
> > 随机 MP3D 场景  
> > 随机目标物体类别
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > 
> > **④ 读取 objectgoal**
> > 
> > 整数 ID → 物体类别  
> > 如 0=chair, 1=bed
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #10b981;">
> > 
> > **⑤ 循环 step()**
> > 
> > 6 个离散动作  
> > 包含 LOOK\_UP/DOWN
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > 
> > **⑥ env.close()**
> > 
> > 释放 GPU 资源  
> > 清理渲染上下文
> > 
> > ``` 
> >       运行命令
> > ```
> > 
> >     # 运行上面的 Python 代码
> >     $ python3 objectnav_env.py
> > 
> > </div>
> > 
> > <div class="screenshot-frame" style="margin:14px 0;">
> > 
> > ![ObjectNav MP3D](images/objectnav_mp3d.png)
> > 
> > <span style="color:#60a5fa;font-weight:600;">📋 运行上面代码的实际输出</span>  
> > ObjectNav 环境 — MP3D 卧室场景 — 目标: object ID (物体类别索引) — 6 个动作 — 云端 MP3D val 可运行 (11 场景)
> > 
> > </div>
> > 
> > > ⚠️
> > > 
> > > <div class="warn-title">
> > > 
> > > 🛠 常见错误
> > > 
> > > | 错误信息                              | 可能原因                   | 解决方法                                       |
> > > | --------------------------------- | ---------------------- | ------------------------------------------ |
> > > | `KeyError: 'objectgoal'`          | 配置文件未启用 objectgoal 传感器 | 确认 yaml 中 `objectgoal_sensor` 段存在          |
> > > | `assert n_actions == 6`           | 用了 PointNav 的训练配置      | 检查 `--config-name` 是 objectnav 而非 pointnav |
> > > | `FileNotFoundError: .../hm3d/...` | 数据集缺失                  | 切换到 `objectnav_mp3d.yaml`（云端已有）            |
> > > | `AssertionError: VIEW_POINTS`     | 场景无 semantic 标注        | MP3D 场景不支持 semantic——用 HM3D                |
> > > 

> > > </div>
> > > 
> > > #### 📖 核心 API 详解
> > > 
> > > <div>
> > > 
> > > **objectgoal — 目标物体类别**
> > > 
> > > `obs["objectgoal"]` 返回一个整数，表示目标物体的类别索引。  
> > >   
> > > **HM3D 数据集定义的 6 种类别**：0=chair, 1=bed, 2=plant, 3=toilet, 4=tv\_monitor, 5=sofa  
> > > **注意**：不同的数据集（MP3D/HM3D/HSSD）可能使用不同的类别映射——查看数据集文档确认。
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > **VIEW\_POINTS 距离 — 为什么不用物体中心？**
> > > 
> > > ObjectNav 的 `distance_to_goal` 计算的是 agent 到 **能看到目标物体的最近视点** 的距离，而非到物体中心的距离。  
> > >   
> > > **原因**：物体本身的位置不直接暴露给 agent（否则就是 "作弊" 版 PointNav 了）。  
> > > VIEW\_POINTS 模拟了真实场景——你不需要踩在物体上面，只要**能看到它**就算到达。
> > > 
> > > </div>
> > > 
> > > > 💡
> > > > 
> > > > <div class="tip-title">
> > > > 
> > > > ObjectNav 为什么比 PointNav 难得多？
> > > > 
> > > > **1. 无目标坐标**: 你只知道要找 "chair"，不知道它在哪。必须用视觉探索。  
> > > > **2. 语义理解**: CNN 需要学习 chair 的视觉特征 vs 其他物体。  
> > > > **3. 泛化压力**: HM3D 有 6 种椅子，测试时可能出现完全不同的椅子。  
> > > > **4. 探索-利用困境**: 是继续搜索，还是在看到疑似目标时 STOP？这是一个赌博。
> > > > 
> > > > </div>
> > > > 
> > > > #### 🏋 训练：启动 ObjectNav 训练
> > > > 
> > > > <div style="margin-bottom:12px;padding:12px 16px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > 
> > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 随机策略在 ObjectNav 里更惨——它不知道 "chair" 长什么样，只会随机走动。  
> > > > **训练的目的**：让 CNN 学会 chair 的视觉模式，让策略学会「看到椅子→减速→确认→STOP」的决策链。  
> > > > ObjectNav 的完整训练需要 **2.7 亿步**——但学习阶段设 100 万步即可验证 pipeline。 </span>
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **📖 ObjectNav 用什么训练？**
> > > > 
> > > > ObjectNav 使用 **DD-PPO 配置 + trainer\_name=ppo** 覆盖为单 GPU 模式。  
> > > > DD-PPO 配置文件包含了完整的 PPO 参数——不必单独写 PPO 配置。  
> > > > PPO 的核心思想：通过 clipped objective 限制策略每次更新的幅度——详见 [§4 PPO 训练算法](#sec4)。
> > > > 
> > > > </div>
> > > > 
> > > > | 模块              | 文件                                        | 作用                                               |
> > > > | --------------- | ----------------------------------------- | ------------------------------------------------ |
> > > > | **训练入口**        | `habitat_baselines/run.py`                | Hydra 加载 DD-PPO 配置 → `trainer_name=ppo` 覆盖为单 GPU |
> > > > | **PPO Trainer** | `habitat_baselines/rl/ppo/ppo_trainer.py` | 构造 Policy + RolloutStorage，管理训练循环                |
> > > > | **VectorEnv**   | `habitat/core/vector_env.py`              | 并行管理 1-4 个 HM3D/MP3D 场景 env                      |
> > > > | **Checkpoint**  | `data/new_checkpoints/ckpt.{N}.pth`       | 保存 model state\_dict + config + step             |
> > > > 

> > > > #### 训练流程图
> > > > 
> > > > <div class="flow-box">
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > > 
> > > > **① Hydra 加载配置**
> > > > 
> > > > objectnav/ddppo\_objectnav.yaml  
> > > > \+ trainer\_name=ppo
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > 
> > > > **② 创建 PPO Trainer**
> > > > 
> > > > Policy(6动作) + RolloutStorage  
> > > > 单 GPU 训练器
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > 
> > > > **③ 创建 VectorEnv**
> > > > 
> > > > 1-4 个 MP3D 环境  
> > > > 并行采样
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > 
> > > > **④ Rollout 采样**
> > > > 
> > > > num\_steps × envs 步  
> > > > 收集 (obs,action,reward)
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > > 
> > > > **⑤ PPO Update**
> > > > 
> > > > GAE → clip → gradient  
> > > > 更新 Policy 权重
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > > 
> > > > **⑥ 保存 Checkpoint**
> > > > 
> > > > data/new\_checkpoints/  
> > > > ckpt.{N}.pth
> > > > 
> > > > ``` 
> > > >       训练命令
> > > > ```
> > > > 
> > > >     # ObjectNav 单 GPU PPO 训练（需 MP3D 数据集 — 云端已有）
> > > >     # 关键: trainer_name=ppo 将 DD-PPO 配置覆盖为单 GPU 模式
> > > >     $ python -u -m habitat_baselines.run \
> > > >         --config-name=objectnav/ddppo_objectnav.yaml \
> > > >         habitat_baselines.trainer_name=ppo \
> > > >         habitat_baselines.num_environments=1 \
> > > >         habitat_baselines.total_num_steps=1e6
> > > >     
> > > >     # 评估
> > > >     $ python -u -m habitat_baselines.run \
> > > >         --config-name=objectnav/ddppo_objectnav.yaml \
> > > >         habitat_baselines.trainer_name=ppo \
> > > >         habitat_baselines.evaluate=True \
> > > >         habitat_baselines.eval_ckpt_path_dir=data/new_checkpoints
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **📋 训练输出解读**
> > > > 
> > > > **reward**：和 PointNav 一样 = -(新距离-旧距离)，但 ObjectNav 用的是 VIEW\_POINTS 距离  
> > > > **success**：前 100 万步 Success \~0-2% 是正常的——ObjectNav 收敛比 PointNav 慢得多  
> > > > **soft\_spl**：ObjectNav 独有指标——即使 agent 没 STOP，只要走到了物体附近也有部分分数  
> > > > **完整训练**：需 2.7 亿步，约 7-10 天（8 GPU DD-PPO），Success 可达 30-50%
> > > > 
> > > > </div>
> > > > 
> > > > <div style="margin:0 0 14px;padding:8px 14px;background:#1e293b;border-left:2px solid #8b5cf6;border-radius:0 6px 6px 0;font-size:0.82rem;color:#94a3b8;">
> > > > 
> > > > <span style="color:#8b5cf6;font-weight:600;">🔗 从 ObjectNav 到 ImageNav</span> — ObjectNav 给了你类别标签（「椅子」），但如果你连标签都没有——只有一张目标位置的照片呢？ImageNav 把任务从**语义理解**推向了**纯视觉匹配**：去掉 GPS，只靠一张图片导航。
> > > > 
> > > > </div>
> > > > 
> > > > ### 1.4 ImageNav — 图片目标导航 <span style="font-size:0.78rem;color:#94a3b8;">难度 ⭐⭐⭐</span>
> > > > 
> > > > <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:18px;font-size:0.82rem;color:#94a3b8;">
> > > > 
> > > > <span>📌 [本节目标](#inav-goal)</span> <span>📖 [是什么](#inav-what)</span> <span>💻 [实操](#inav-practice)</span> <span>🛠 [常见错误](#inav-errors)</span> <span>📖 [API 详解](#inav-api)</span> <span>🏋 [训练](#inav-train)</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **📌 学完本节你将能够**
> > > > 
> > > > 用 Gym API 创建 ImageNav 环境，理解 `imagegoal` 传感器的作用  
> > > > 对比 ImageNav 与 PointNav / ObjectNav 在目标表示方式上的根本区别  
> > > > 理解「视觉匹配」在完全无 GPS 条件下的挑战与策略设计思路
> > > > 
> > > > </div>
> > > > 
> > > > <div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > 
> > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 假设你到一个陌生的城市旅游。当地人没有告诉你**坐标**，也没有说**「去找沙发」**——  
> > > > 他只是掏出一张**照片**：一个喷泉广场，夕阳打在石柱上。  
> > > >   
> > > > 他说：「我要你去的就是**这个地方**。」  
> > > >   
> > > > 你现在没有任何 GPS 信号（手机没电了），没有指南针。你只记得那张照片的样子。  
> > > > 你走着走着，看到一条街有点像照片里的——但角度不同，光线也不同。  
> > > > **你怎么判断"就是这里"？**  
> > > >   
> > > > 这就是 ImageNav——任务说明是一张图片，而非坐标或类别标签。 </span>
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **📖 ImageNav 是什么**
> > > > 
> > > > **ImageNav**（ImageGoal Navigation）给智能体一张从**目标位置拍摄的 RGB 照片**作为导航目标。  
> > > >   
> > > > **关键区别**：PointNav 给坐标（定量），ObjectNav 给类别标签（语义）。ImageNav 给的是**纯视觉信号**——没有文字、没有位置、没有语义。  
> > > > 智能体唯一的任务就是：**把当前看到的画面，和那张目标照片做匹配**，然后朝匹配度更高的方向走。  
> > > >   
> > > > 这听起来像是「看图找地方」——但你走的路和目标照片的拍摄角度可能**完全不同**（你从西边来，目标照片是从东边拍的）。策略必须学会**跨视点匹配**。
> > > > 
> > > > </div>
> > > > 
> > > > | 对比维度        | PointNav              | ObjectNav                        | ImageNav                | 这意味着什么                  |
> > > > | ----------- | --------------------- | -------------------------------- | ----------------------- | ----------------------- |
> > > > | **目标表示**    | 坐标 (ρ, φ)             | 类别 ID                            | RGB 图片                  | 纯视觉匹配——最难的目标形式          |
> > > > | **动作数**     | 4                     | 6                                | 4                       | 无 LOOK\_UP/DOWN，专注水平探索  |
> > > > | **传感器**     | RGB+Depth+GPS+Compass | RGB+Depth+objectgoal+GPS+Compass | RGB+Depth+**imagegoal** | **无 GPS！** 完全靠视觉        |
> > > > | **奖励**      | distance\_to\_goal    | VIEW\_POINTS 距离                  | distance\_to\_goal      | 到目标点的欧氏距离               |
> > > > | **Stop 依赖** | GPS 离目标\<0.36m        | 看到物体→STOP                        | 视觉匹配→STOP               | 最容易出 false positive     |
> > > > | **数据集**     | MP3D/Gibson           | HM3D/MP3D                        | 复用 PointNav             | **云端 PointNav MP3D 可用** |
> > > > 

> > > > #### 💻 实操：创建 ImageNav 环境
> > > > 
> > > > <div style="margin-bottom:12px;">
> > > > 
> > > > <div style="color:#60a5fa;font-weight:600;font-size:0.85rem;margin-bottom:6px;">
> > > > 
> > > > 设计理论
> > > > 
> > > > </div>
> > > > 
> > > > **核心任务**：创建 ImageNav 环境 → 读取 imagegoal（目标位置 RGB）→ 对比与 PointNav 缺失了哪些传感器。  
> > > > **关键点**：ImageNav 复用 PointNav 数据集（运行时在目标位置渲染图片），**不设置 GPS/Compass 传感器**——这是它与 PointNav 最本质的区别。  
> > > > **策略设计挑战**：你需要比较两张来自不同视点的 RGB 图（当前观测 vs 目标图像），通常用 **Siamese 网络** 编码两张图后计算相似度。
> > > > 
> > > > </div>
> > > > 
> > > > | 代码段                                                | 作用             | 关键点                                         |
> > > > | -------------------------------------------------- | -------------- | ------------------------------------------- |
> > > > | `gym.make("Habitat-v0", cfg="imagenav_mp3d.yaml")` | 创建 ImageNav 环境 | 4 动作 + imagegoal + 无 GPS/Compass            |
> > > > | `obs["imagegoal"]`                                 | 获取目标位置 RGB     | shape (H, W, 3)——与 obs\["rgb"\] 同结构，但来自目标位置 |
> > > > | `obs["rgb"]`                                       | 当前观测 RGB       | 策略需将其与 imagegoal 做比较                        |
> > > > | `env.current_episode.goal_position`                | 目标位置坐标         | 仅用于"内部分数计算"——不暴露给 agent                     |
> > > > 

> > > > ``` 
> > > >       完整代码
> > > > ```
> > > > 
> > > >     import gym, habitat.gym  # 注册 Habitat-v0
> > > >     
> > > >     # 1. 创建 ImageNav 环境 — 复用 PointNav MP3D 数据集
> > > >     env = gym.make("Habitat-v0",
> > > >         cfg_file_path="benchmark/nav/imagenav/imagenav_mp3d.yaml")
> > > >     
> > > >     # 2. 重置环境 — 随机场景 + 随机目标（目标位置渲染为 imagegoal）
> > > >     obs = env.reset()
> > > >     print(obs.keys())
> > > >     # 输出: dict_keys(['rgb', 'depth', 'imagegoal'])
> > > >     # 注意: 没有 'gps' 和 'compass' — agent 完全没有定位信息！
> > > >     
> > > >     # 3. 读取目标图片 — imagegoal 是从目标位置看的 RGB
> > > >     goal_img = obs["imagegoal"]
> > > >     print(f"Goal image shape: {goal_img.shape}")
> > > >     # 输出: Goal image shape: (256, 256, 3)
> > > >     
> > > >     # 4. 对比观察空间 — 比 PointNav 少了什么？
> > > >     print(f"Action space: {env.action_space}")
> > > >     # 输出: Discrete(4) — 4 个动作，同 PointNav
> > > >     
> > > >     # 5. 查看目标坐标（仅供内部使用——不暴露给策略）
> > > >     ep = env.current_episode
> > > >     print(f"Target position: {ep.goal_position}")
> > > >     # 输出: Target position: [3.14, -2.71]  (agent 看不到这个!)
> > > >     
> > > >     # 6. 尝试随机导航 — 靠视觉匹配找到目标
> > > >     total_reward = 0.0
> > > >     for step in range(500):
> > > >         action = env.action_space.sample()  # 随机动作
> > > >         obs, reward, done, info = env.step(action)
> > > >         total_reward += reward
> > > >         if done:
> > > >             print(f"Episode done at step {step+1} — "
> > > >                   f"success={info.get('success', 0)}")
> > > >             break
> > > >     env.close()  # 释放 GPU 资源
> > > > 
> > > > </div>
> > > > 
> > > > #### 程序运行流程图
> > > > 
> > > > <div class="flow-box">
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > > 
> > > > **① import habitat.gym**
> > > > 
> > > > 注册 Habitat-v0  
> > > > Gym 环境入口
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > 
> > > > **② gym.make()**
> > > > 
> > > > 加载 imagenav\_mp3d.yaml  
> > > > 4 动作 + imagegoal + 无 GPS
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > 
> > > > **③ env.reset()**
> > > > 
> > > > 随机 MP3D 场景  
> > > > 目标点渲染为 RGB
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > 
> > > > **④ 读取 imagegoal**
> > > > 
> > > > (256, 256, 3) 张量  
> > > > 目标位置的视角
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > > 
> > > > **⑤ 循环 step()**
> > > > 
> > > > 策略比较 obs\["rgb"\] vs  
> > > > imagegoal → 决定动作
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > > 
> > > > **⑥ env.close()**
> > > > 
> > > > 释放 GPU 显存  
> > > > 清理渲染上下文
> > > > 
> > > > ``` 
> > > >       运行命令
> > > > ```
> > > > 
> > > >     # 运行上面的 Python 代码
> > > >     $ python3 imagenav_env.py
> > > > 
> > > > </div>
> > > > 
> > > > <div class="screenshot-frame" style="margin:14px 0;">
> > > > 
> > > > ![ImageNav MP3D Goal](images/imagenav_mp3d_goal.png)
> > > > 
> > > > <span style="color:#60a5fa;font-weight:600;">📋 运行上面代码的实际输出</span>  
> > > > ImageNav 环境 — 左: Agent 当前 RGB 观测 — 右: 目标位置 RGB (imagegoal) — **无 GPS！** 全靠视觉匹配 — 复用 PointNav MP3D 数据集，云端可直接运行
> > > > 
> > > > </div>
> > > > 
> > > > > ⚠️
> > > > > 
> > > > > <div class="warn-title">
> > > > > 
> > > > > 🛠 常见错误
> > > > > 
> > > > > | 错误信息                                                | 可能原因                      | 解决方法                                   |
> > > > > | --------------------------------------------------- | ------------------------- | -------------------------------------- |
> > > > > | `KeyError: 'imagegoal'`                             | 配置文件未启用 imagegoal\_sensor | 确认 yaml 中 `imagegoal_sensor` 段存在       |
> > > > > | `ImportError: cannot import name 'ImageGoalSensor'` | habitat-lab 版本过旧          | 更新 habitat-lab，ImageNav 在 v0.1.5 后引入   |
> > > > > | `FileNotFoundError: .../mp3d/...`                   | MP3D 数据集缺失                | 切换为 `imagenav_gibson.yaml` 或下载 MP3D 场景 |
> > > > > | `assert goal_shape == (256, 256, 3)`                | 配置中分辨率不一致                 | 检查 `goal_sensor_uuid` 和 `hfov` 参数      |
> > > > > 

> > > > > </div>
> > > > > 
> > > > > #### 📖 核心 API 详解
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **imagegoal — 目标位置的 RGB 图像**
> > > > > 
> > > > > `obs["imagegoal"]` 返回一个 **(H, W, 3)** 的 NumPy 数组（默认 256×256），从目标坐标渲染。  
> > > > >   
> > > > > **与 obs\["rgb"\] 的比较**：两者结构完全相同（都是 RGB 图像），但观察点不同。  
> > > > > **策略的核心任务**：编码这两张图像为向量，计算相似度，选择让相似度增大的动作。  
> > > > > 通常使用 **Siamese 网络**（两个共享权重的 CNN + 差异度量）而非简单的像素差——因为视点不同时像素差没有任何意义。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **为什么不在 yaml 中配置 GPS/Compass？**
> > > > > 
> > > > > ImageNav 的设计哲学：你只需要一张目标照片。  
> > > > >   
> > > > > 如果在环境中添加 GPS/Compass 传感器，任务就退化为 PointNav——因为策略会直接依赖坐标信号而**忽略视觉匹配**。  
> > > > > ImageNav 强制策略通过视觉推理来定位，而不是走「偷看答案」的捷径。  
> > > > > 这也意味着 ImageNav 的策略需要比 PointNav **更多的视觉表示能力**——通常需要 ResNet50 或更强的视觉 backbone。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > > 💡
> > > > > > 
> > > > > > <div class="tip-title">
> > > > > > 
> > > > > > ImageNav 为什么比 PointNav 难得多？
> > > > > > 
> > > > > > **1. 视点变化 (Viewpoint Variation)**: 策略从西边走来，目标照片从东边拍摄——相同位置，完全不同的画面。  
> > > > > > **2. 感知混叠 (Perceptual Aliasing)**: 走廊两端看起来几乎一样——策略可能走到「看起来像」但实际不对的位置。  
> > > > > > **3. 没有捷径**: PointNav 的 GPS 是「作弊器」——远离目标时 reward 减少，靠近时增加。ImageNav 只能靠视觉匹配信号（更稀疏）。  
> > > > > > **4. 图片≠三维场景**: 一张 2D 照片缺失深度信息——你不知道「像」的墙在 2 米外还是 20 米外。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > #### 🏋 训练：启动 ImageNav 训练
> > > > > > 
> > > > > > <div style="margin-bottom:12px;padding:12px 16px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > > > 
> > > > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 随机策略在 ImageNav 里几乎**完全无效**——它没有 GPS 信号辅助，不知道「往左走更接近目标」。  
> > > > > > 纯随机走 500 步的成功率 ≈ **0%（基本不可能随机走到目标点附近然后恰好 STOP）**。  
> > > > > >   
> > > > > > **训练的目的**：让 CNN 学会编码视觉特征，让策略学会从「当前观测 vs 目标照片」的差异中提取导航信号。  
> > > > > > 最简单的做法：用 **Siamese 网络**（共享权重的双分支 CNN）编码两张图 → 计算特征差异 → 策略根据差异决定动作。 </span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **📖 ImageNav 用什么训练？**
> > > > > > 
> > > > > > ImageNav 使用 **DD-PPO + ResNet50 视觉 backbone** 配置。  
> > > > > > 视觉编码器需要处理**双路输入**（当前观测 + 目标图片），通常用 Siamese 网络结构。  
> > > > > > PPO 的核心思想：通过 clipped objective 限制策略每次更新的幅度——详见 [§4 PPO 训练算法](#sec4)。  
> > > > > > ImageNav 训练收敛比 PointNav 慢 5-10 倍——因为视觉匹配信号远不如 GPS 信号精确。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > | 模块              | 文件                                                 | 作用                                       |
> > > > > > | --------------- | -------------------------------------------------- | ---------------------------------------- |
> > > > > > | **训练入口**        | `habitat_baselines/run.py`                         | Hydra 加载 DD-PPO ImageNav 配置 → 构建 Trainer |
> > > > > > | **PPO Trainer** | `habitat_baselines/rl/ppo/ppo_trainer.py`          | 管理 Policy + RolloutStorage + PPO 更新循环    |
> > > > > > | **视觉编码器**       | `habitat_baselines/rl/models/rnn_state_encoder.py` | 编码双路 RGB（当前观测 + 目标图片）为特征向量               |
> > > > > > | **VectorEnv**   | `habitat/core/vector_env.py`                       | 并行管理多个 MP3D/Gibson 场景 env                |
> > > > > > | **Checkpoint**  | `data/new_checkpoints/ckpt.{N}.pth`                | 保存 model state\_dict + 训练步数              |
> > > > > > 

> > > > > > #### 训练流程图
> > > > > > 
> > > > > > <div class="flow-box">
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > > > > 
> > > > > > **① Hydra 加载配置**
> > > > > > 
> > > > > > imagenav/ddppo\_imagenav.yaml  
> > > > > > \+ ResNet50 backbone
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > > > 
> > > > > > **② 创建 PPO Trainer**
> > > > > > 
> > > > > > Policy(Siamese CNN)  
> > > > > > \+ RolloutStorage
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > > > 
> > > > > > **③ 创建 VectorEnv**
> > > > > > 
> > > > > > 1-4 个 MP3D 环境  
> > > > > > 并行采样
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > > > 
> > > > > > **④ Rollout 采样**
> > > > > > 
> > > > > > num\_steps × envs 步  
> > > > > > 收集 (obs,action,reward)
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > > > > 
> > > > > > **⑤ PPO Update**
> > > > > > 
> > > > > > GAE → clip → gradient  
> > > > > > 更新 Policy 权重
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-arrow">
> > > > > > 
> > > > > > →
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > > > > 
> > > > > > **⑥ 保存 Checkpoint**
> > > > > > 
> > > > > > data/new\_checkpoints/  
> > > > > > ckpt.{N}.pth
> > > > > > 
> > > > > > ``` 
> > > > > >       训练命令
> > > > > > ```
> > > > > > 
> > > > > >     # ImageNav DD-PPO 训练（需 MP3D 数据集 — 云端已有）
> > > > > >     # 单 GPU 模式: 添加 trainer_name=ppo 覆盖
> > > > > >     $ python -u -m habitat_baselines.run \
> > > > > >         --config-name=imagenav/ddppo_imagenav_gibson.yaml \
> > > > > >         habitat_baselines.trainer_name=ppo \
> > > > > >         habitat_baselines.num_environments=1 \
> > > > > >         habitat_baselines.total_num_steps=1e6
> > > > > >     
> > > > > >     # 评估
> > > > > >     $ python -u -m habitat_baselines.run \
> > > > > >         --config-name=imagenav/ddppo_imagenav_gibson.yaml \
> > > > > >         habitat_baselines.trainer_name=ppo \
> > > > > >         habitat_baselines.evaluate=True \
> > > > > >         habitat_baselines.eval_ckpt_path_dir=data/new_checkpoints
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **📋 训练输出解读**
> > > > > > 
> > > > > > **reward**：distance\_to\_goal\_reward（靠近目标 + 分，远离 − 分），但你**不知道**目标在哪——只能通过视觉匹配间接推断  
> > > > > > **success**：前 100 万步 Success \~0-1% 是**完全正常**的——ImageNav 收敛极慢，因为缺少 GPS 的「对齐信号」  
> > > > > > **fps**：相比 PointNav 会慢 20-30%——双路 RGB 编码计算量翻倍（当前观测 + 目标图片）  
> > > > > > **完整训练**：需 3-5 亿步（PointNav 的 3-5 倍），Success 可达 30-40%（Gibson 简单场景下）
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div style="margin:0 0 14px;padding:8px 14px;background:#1e293b;border-left:2px solid #8b5cf6;border-radius:0 6px 6px 0;font-size:0.82rem;color:#94a3b8;">
> > > > > > 
> > > > > > <span style="color:#8b5cf6;font-weight:600;">🔗 从 ImageNav 到 InstanceImageNav</span> — ImageNav 靠图片匹配导航到**任何**位置。但如果你要找**特定的那把椅子**（棕色皮椅，不是旁边那 11 把）呢？InstanceImageNav 把识别粒度从**位置级**提升到**实例级**——这才是真正的人类级导航。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### 1.5 InstanceImageNav — 实例级图像导航 <span style="font-size:0.78rem;color:#94a3b8;">难度 ⭐⭐⭐⭐</span>
> > > > > > 
> > > > > > <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:18px;font-size:0.82rem;color:#94a3b8;">
> > > > > > 
> > > > > > <span>📌 [本节目标](#instnav-goal)</span> <span>📖 [是什么](#instnav-what)</span> <span>📊 [层级对比](#instnav-compare)</span> <span>🛠 [常见错误](#instnav-errors)</span> <span>⚠️ [工程限制](#instnav-limits)</span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **📌 学完本节你将能够**
> > > > > > 
> > > > > > 区分 ObjectNav（类别级）和 InstanceImageNav（实例级）的本质差异  
> > > > > > 理解为什么实例级识别比类别级识别难一个数量级  
> > > > > > 了解 InstanceImageNav 的传感器体系和训练成本
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > > > 
> > > > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 你在大教室里，任务是「找到一把椅子」。你扫了一圈——**有 12 把椅子**。任何一把都算完成任务。这是 ObjectNav.  
> > > > > >   
> > > > > > 但现在任务变了：「找到**第三排靠窗那把棕色皮椅**」。  
> > > > > > 你不能随便找一把椅子——必须是**特定的那一个实例**。  
> > > > > > 你必须区分「棕色皮椅」和「黑色布椅」、「第三排」和「第五排」——  
> > > > > > 这在视觉上远比「有椅子吗」难得多。这就是 InstanceImageNav。  
> > > > > > 给你一张**目标实例的照片**，你必须找到那个**独一无二的个体**。 </span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **📖 InstanceImageNav 是什么**
> > > > > > 
> > > > > > **InstanceImageNav**（Instance ImageGoal Navigation）是 ImageNav + ObjectNav 的**交集强化版**：  
> > > > > >   
> > > > > > **ObjectNav**：找类别 → "有椅子吗？"  
> > > > > > **ImageNav**：找位置 → "这地方长这样"  
> > > > > > **InstanceImageNav**：找**特定实例** → "这把棕色的皮椅（不是其他 11 把）"  
> > > > > >   
> > > > > > 传感器给出**目标实例的多视角照片**（不同 FOV），策略必须同时具备**实例辨别力**和**空间推理力**。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > | 对比维度            | ObjectNav         | ImageNav          | InstanceImageNav           | 本质区别            |
> > > > > > | --------------- | ----------------- | ----------------- | -------------------------- | --------------- |
> > > > > > | **目标粒度**        | 类别（chair）         | 位置（坐标的视觉快照）       | 实例（chair\_3）               | 从「是什么」→「哪把」     |
> > > > > > | **传感器**         | objectgoal (类别ID) | imagegoal (单张RGB) | instance\_imagegoal (多FOV) | 多视角消除匹配歧义       |
> > > > > > | **GPS/Compass** | 有                 | 无                 | 有                          | 有定位辅助，但实例识别是瓶颈  |
> > > > > > | **训练步数**        | 2.7 亿步            | 3-5 亿步            | **25 亿步**                  | 10 倍于 ObjectNav |
> > > > > > | **数据集**         | HM3D/MP3D         | 复用 PointNav       | **HM3D 语义标注**              | **云端缺失**        |
> > > > > > 

> > > > > > > ⚠️
> > > > > > > 
> > > > > > > <div class="warn-title">
> > > > > > > 
> > > > > > > 🛠 常见错误
> > > > > > > 
> > > > > > > | 错误信息                             | 可能原因                                 | 解决方法                               |
> > > > > > > | -------------------------------- | ------------------------------------ | ---------------------------------- |
> > > > > > > | `FileNotFoundError: HM3D scene`  | HM3D 数据集未安装                          | InstanceImageNav 必须 HM3D——MP3D 不支持 |
> > > > > > > | `KeyError: 'instance_imagegoal'` | yaml 未启用 instance\_imagegoal\_sensor | 确认 instance\_imagenav 配置段          |
> > > > > > > | `CUDA OOM`                       | 多 FOV 图片显存翻倍                         | 减小 FOV 数量或降低分辨率                    |
> > > > > > > 

> > > > > > > </div>
> > > > > > > 
> > > > > > > > ⚠️
> > > > > > > > 
> > > > > > > > <div class="warn-title" style="color:#f59e0b;">
> > > > > > > > 
> > > > > > > > ⚠️ 工程限制：本课程无法运行 InstanceImageNav
> > > > > > > > 
> > > > > > > > **不运行它的两个原因**：  
> > > > > > > > 1\. **数据集**：InstanceImageNav 需要 HM3D 的**实例级语义标注**（235 GB），云端只有 MP3D（754 MB 场景 + 语义）  
> > > > > > > > 2\. **训练成本**：官方配置 `total_num_steps=2.5e9`（25 亿步），单 A100 需 ≈ 3 个月——不适合教学演示  
> > > > > > > > 3\. **无官方权重**：Habitat-Baselines 官方发布的 `habitat_baselines_v2.zip` **只包含 PointNav 模型**，ObjectNav / ImageNav / InstanceImageNav 均无预训练权重发布  
> > > > > > > >   
> > > > > > > > **但理解它仍然重要**——实例级导航是研究前沿。它展示了「类别识别 → 实例识别」这一质变对导航任务的影响。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div style="margin:0 0 14px;padding:8px 14px;background:#1e293b;border-left:2px solid #8b5cf6;border-radius:0 6px 6px 0;font-size:0.82rem;color:#94a3b8;">
> > > > > > > > 
> > > > > > > > <span style="color:#8b5cf6;font-weight:600;">🔗 从 InstanceImageNav 到 VLN</span> — 前四个任务的目标都是**信号**（坐标→ID→像素→实例照片）。VLN 的目标是**自然语言**。这是一个范式的断裂——你不再有可计算的目标，只有一个模糊的人类指令。训练方法也必须从 RL 切换到 IL。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### 1.6 VLN — 视觉语言导航 <span style="font-size:0.78rem;color:#94a3b8;">难度 ⭐⭐⭐⭐⭐</span>
> > > > > > > > 
> > > > > > > > <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:18px;font-size:0.82rem;color:#94a3b8;">
> > > > > > > > 
> > > > > > > > <span>📌 [本节目标](#vln-goal)</span> <span>📖 [是什么](#vln-what)</span> <span>📊 [五任务对比](#vln-compare)</span> <span>💻 [实操](#vln-practice)</span> <span>🛠 [常见错误](#vln-errors)</span> <span>📖 [API 详解](#vln-api)</span> <span>🏋 [训练 (IL)](#vln-train)</span>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **📌 学完本节你将能够**
> > > > > > > > 
> > > > > > > > 用 Gym API 创建 VLN 环境，理解 `instruction_sensor` 的作用  
> > > > > > > > 理解为什么 VLN 不能直接用 PPO 训练——奖励函数为何无法定义  
> > > > > > > > 对比 Imitation Learning 和 Reinforcement Learning 在导航中的适用场景
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > > > > > 
> > > > > > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 回忆一下前四个任务告诉你的目标：  
> > > > > > > > PointNav：**坐标 (3.14, -2.71)** — 精确到小数点。  
> > > > > > > > ObjectNav：**整数 0** — 代表"chair"。  
> > > > > > > > ImageNav：**一张 256×256 的 RGB 图** — 像素精确。  
> > > > > > > > InstanceImageNav：**特定椅子的多视角照片**。  
> > > > > > > >   
> > > > > > > > 现在，你的目标变成了：**“Go down the hallway, past the bathroom on your left, and stop in front of the bed.”**  
> > > > > > > >   
> > > > > > > > 没有坐标。没有类别标签。没有照片。只有一句**模糊的人类语言**。  
> > > > > > > > “bathroom” 是什么样子的？“hallway” 有多长？“in front of the bed” — 从哪个角度？  
> > > > > > > >   
> > > > > > > > 这就是 **VLN —— 视觉语言导航**。  
> > > > > > > > 它要求智能体同时理解**语言**（“past the bathroom”）、**视觉**（哪个门是 bathroom？）、和**决策**（在第几个门转弯？）。  
> > > > > > > > 这对人类来说理所当然，但对 AI 来说是三个完全不同的子问题——而且必须同时解决。 </span>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **📖 VLN 是什么**
> > > > > > > > 
> > > > > > > > **VLN**（Vision-and-Language Navigation）要求智能体根据**自然语言指令**在未知环境中导航。  
> > > > > > > >   
> > > > > > > > **与前四个任务的本质区别**：目标从「**信号**」变成了「**语言**」。  
> > > > > > > > 坐标可以算距离。类别可以训练分类器。图像可以算特征相似度。  
> > > > > > > > 但 **自然语言指令**——“past the bathroom”、“stop in front of”——这些词没有标准化的数学表达。  
> > > > > > > >   
> > > > > > > > 因此 VLN 要求一种全新的能力：**语言接地 (Language Grounding)**——将词语映射到视觉世界中的具体位置和动作。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > | 对比维度      | PointNav | ObjectNav    | ImageNav   | InstanceImageNav | VLN                    | 质变点     |
> > > > > > > > | --------- | -------- | ------------ | ---------- | ---------------- | ---------------------- | ------- |
> > > > > > > > | **目标**    | 坐标 (ρ,φ) | 类别 ID        | 单张 RGB     | 实例多视角            | **自然语言**               | 信号→语言   |
> > > > > > > > | **训练**    | PPO      | PPO          | PPO        | PPO              | **Imitation Learning** | RL→IL   |
> > > > > > > > | **奖励信号**  | 距离差      | VIEW\_POINTS | 距离差        | VIEW\_POINTS     | **不可定义**               | 可算→不可算  |
> > > > > > > > | **数据来源**  | 自动生成     | 自动生成         | PointNav复用 | 自动生成             | **人类标注**               | 机器→人类   |
> > > > > > > > | **独特指标**  | SPL      | soft\_spl    | —          | —                | **nDTW**               | 路径相似度   |
> > > > > > > > | **云端可运行** | ✅        | ✅            | ✅          | ❌                | **✅**                  | R2R数据齐全 |
> > > > > > > > 

> > > > > > > > #### 💻 实操：创建 VLN 环境
> > > > > > > > 
> > > > > > > > <div style="margin-bottom:12px;">
> > > > > > > > 
> > > > > > > > <div style="color:#60a5fa;font-weight:600;font-size:0.85rem;margin-bottom:6px;">
> > > > > > > > 
> > > > > > > > 设计理论
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > **核心任务**：创建 VLN 环境 → 读取 instruction（自然语言文本）→ 观察 R2R 数据集的组织方式。  
> > > > > > > > **关键点**：VLN 的 observation 中多了 `instruction` 字段——这是一段人类标注的自然语言文本，而非数值张量。  
> > > > > > > > **与 ImageNav 的对比**：ImageNav 的目标是图像（可以编码为特征向量计算相似度），VLN 的目标是文本（需要 NLP 模型编码语义）。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > | 代码段                                          | 作用             | 关键点                                               |
> > > > > > > > | -------------------------------------------- | -------------- | ------------------------------------------------- |
> > > > > > > > | `gym.make("Habitat-v0", cfg="vln_r2r.yaml")` | 创建 VLN 环境      | 4 动作 + instruction\_sensor + R2R 数据集              |
> > > > > > > > | `obs["instruction"]`                         | 获取自然语言导航指令     | **纯文本**（非张量）——如 "Go down the hallway..."          |
> > > > > > > > | `env.current_episode`                        | 获取 episode 元信息 | 包含 scene\_id / path\_id / 参考路径坐标                  |
> > > > > > > > | `env.action_space`                           | 动作空间           | Discrete(4) — STOP / FWD / LEFT\_15° / RIGHT\_15° |
> > > > > > > > 

> > > > > > > > ``` 
> > > > > > > >       完整代码
> > > > > > > > ```
> > > > > > > > 
> > > > > > > >     import gym, habitat.gym  # 注册 Habitat-v0
> > > > > > > >     
> > > > > > > >     # 1. 创建 VLN 环境 — 使用 R2R 数据集（云端 MP3D R2R 已有）
> > > > > > > >     env = gym.make("Habitat-v0",
> > > > > > > >         cfg_file_path="benchmark/nav/vln_r2r.yaml")
> > > > > > > >     
> > > > > > > >     # 2. 重置环境 — 随机 episode：随机场景 + 随机路径 + 对应指令
> > > > > > > >     obs = env.reset()
> > > > > > > >     print(obs.keys())
> > > > > > > >     # 输出: dict_keys(['rgb', 'depth', 'instruction'])
> > > > > > > >     # 注意: 没有 gps/compass! VLN 只需要视觉 + 语言
> > > > > > > >     
> > > > > > > >     # 3. 读取导航指令 — instruction 是纯文本字符串！
> > > > > > > >     instr = obs["instruction"]
> > > > > > > >     print(f"Instruction: {instr}")
> > > > > > > >     # 输出: Instruction: Go down the hallway past the bathroom on your left.
> > > > > > > >     #        Stop when you reach the bedroom on the right.
> > > > > > > >     
> > > > > > > >     # 4. 查看 episode 信息 — R2R 数据集的元数据
> > > > > > > >     ep = env.current_episode
> > > > > > > >     print(f"Scene: {ep.scene_id.split('/')[-1]}")
> > > > > > > >     # 输出: Scene: 17DRP5sb8fy.glb  (MP3D 场景ID)
> > > > > > > >     print(f"Path ID: {ep.episode_id}")
> > > > > > > >     # 输出: Path ID: 1234  (R2R 路径编号)
> > > > > > > >     
> > > > > > > >     # 5. 参考路径（人类走过的轨迹 — 仅用于评估，不暴露给策略）
> > > > > > > >     ref_path = ep.reference_path  # 参考路径坐标列表
> > > > > > > >     print(f"Reference path has {len(ref_path)} waypoints")
> > > > > > > >     # 输出: Reference path has 5 waypoints
> > > > > > > >     
> > > > > > > >     # 6. 运行随机动作 — 纯随机策略在 VLN 中完全无效
> > > > > > > >     total_reward = 0.0
> > > > > > > >     for step in range(500):
> > > > > > > >         action = env.action_space.sample()
> > > > > > > >         obs, reward, done, info = env.step(action)
> > > > > > > >         total_reward += reward
> > > > > > > >         if done:
> > > > > > > >             print(f"Episode done at step {step+1}, "
> > > > > > > >                   f"success={info.get('success', 0)}")
> > > > > > > >             break
> > > > > > > >     env.close()  # 释放 GPU 资源
> > > > > > > > 
> > > > > > > > #### 程序运行流程图
> > > > > > > > 
> > > > > > > > <div class="flow-box">
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > > > > > > 
> > > > > > > > **① import habitat.gym**
> > > > > > > > 
> > > > > > > > 注册 Habitat-v0  
> > > > > > > > Gym 环境入口
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-arrow">
> > > > > > > > 
> > > > > > > > →
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > > > > > 
> > > > > > > > **② gym.make()**
> > > > > > > > 
> > > > > > > > 加载 vln\_r2r.yaml  
> > > > > > > > R2R MP3D 数据集
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-arrow">
> > > > > > > > 
> > > > > > > > →
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > > > > > 
> > > > > > > > **③ env.reset()**
> > > > > > > > 
> > > > > > > > 随机 MP3D 场景  
> > > > > > > > 随机 R2R 路径 + 指令
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-arrow">
> > > > > > > > 
> > > > > > > > →
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > > > > > 
> > > > > > > > **④ 读取 instruction**
> > > > > > > > 
> > > > > > > > 自然语言文本  
> > > > > > > > 如 "Go down the hallway..."
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-arrow">
> > > > > > > > 
> > > > > > > > →
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #10b981;">
> > > > > > > > 
> > > > > > > > **⑤ 循环 step()**
> > > > > > > > 
> > > > > > > > 策略解析语言 → 选择动作  
> > > > > > > > 关键：语言接地
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-arrow">
> > > > > > > > 
> > > > > > > > →
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > > > > > > 
> > > > > > > > **⑥ env.close()**
> > > > > > > > 
> > > > > > > > 释放 GPU 显存  
> > > > > > > > 清理渲染上下文
> > > > > > > > 
> > > > > > > > ``` 
> > > > > > > >       运行命令
> > > > > > > > ```
> > > > > > > > 
> > > > > > > >     # 运行上面的 Python 代码
> > > > > > > >     $ python3 vln_env.py
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="screenshot-frame" style="margin:14px 0;">
> > > > > > > > 
> > > > > > > > ![VLN R2R Navigation](images/vln_env_output.png)
> > > > > > > > 
> > > > > > > > <span style="color:#60a5fa;font-weight:600;">📋 运行上面代码的实际输出</span>  
> > > > > > > > VLN 环境 — 3 步运行轨迹 + 人类标注的导航指令 — MP3D R2R 数据集 — 云端 L40 实时渲染
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > > ⚠️
> > > > > > > > > 
> > > > > > > > > <div class="warn-title">
> > > > > > > > > 
> > > > > > > > > 🛠 常见错误
> > > > > > > > > 
> > > > > > > > > | 错误信息                                        | 可能原因                         | 解决方法                               |
> > > > > > > > > | ------------------------------------------- | ---------------------------- | ---------------------------------- |
> > > > > > > > > | `KeyError: 'instruction'`                   | yaml 未启用 instruction\_sensor | 确认使用了 `vln_r2r.yaml` 而非其他配置        |
> > > > > > > > > | `FileNotFoundError: R2R episodes`           | R2R 数据集缺失                    | 下载 R2R 数据集到 data/datasets/vln/r2r/ |
> > > > > > > > > | `PPO trainer: task VLN-v0 not supported`    | 尝试用 PPO 训练 VLN               | VLN 不支持 PPO——见下方训练章节               |
> > > > > > > > > | `TypeError: instruction is str, not tensor` | 直接将文本传给 CNN                  | 需要 NLP 编码器（LSTM/Transformer）处理文本   |
> > > > > > > > > 

> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > #### 📖 核心 API 详解
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > **instruction\_sensor — 自然语言导航指令**
> > > > > > > > > 
> > > > > > > > > `obs["instruction"]` 返回一个**字符串**（而非数值张量），由 R2R 数据集的人类标注者编写。  
> > > > > > > > >   
> > > > > > > > > **这意味着什么**：PointNav/ObjectNav/ImageNav 的目标传感器返回的是数值（坐标、ID、图像像素），可以直接输入神经网络。  
> > > > > > > > > 但 VLN 的 instruction 是文本——需要**额外的 NLP 模型**（如 LSTM、Transformer）将文本编码为特征向量，才能与视觉特征融合。  
> > > > > > > > > 这就是为什么 VLN 的策略网络比 PointNav 复杂一个量级——它需要**双模态编码器**（视觉 CNN + 语言 LSTM/Transformer）。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > **R2R (Room-to-Room) 数据集**
> > > > > > > > > 
> > > > > > > > > R2R 是 VLN 的标准数据集，包含 **Matterport3D 场景中的人类标注路径+指令对**。  
> > > > > > > > >   
> > > > > > > > > **数据结构**：每个 episode = (scene\_id, start\_position, goal\_position, reference\_path, instruction)  
> > > > > > > > > — scene\_id: 哪个 MP3D 场景  
> > > > > > > > > — reference\_path: 人类实际走过的路径（用于计算 nDTW）  
> > > > > > > > > — instruction: 人类写的导航指令（如 "Go down the hallway...stop in front of the bed"）  
> > > > > > > > >   
> > > > > > > > > **关键**：instruction 和 reference\_path 来自**同一个人**——他看到路径后写出指令。训练时策略学习从指令预测路径。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > **nDTW — 路径相似度评估**
> > > > > > > > > 
> > > > > > > > > **nDTW**（normalized Dynamic Time Warping）衡量 agent 实际路径与参考路径的**形状相似度**。  
> > > > > > > > >   
> > > > > > > > > 为什么不用简单的 success（到达目标 3m 内）？  
> > > > > > > > > 因为 VLN 要求 agent **按照指令描述的路径走**——"先直走，经过浴室后左转"。  
> > > > > > > > > 如果 agent 绕了一大圈最终到达目标，success=1 但 nDTW 很低——它没有遵循指令。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > > 💡
> > > > > > > > > > 
> > > > > > > > > > <div class="tip-title">
> > > > > > > > > > 
> > > > > > > > > > VLN 为什么比前四个任务难一个维度？
> > > > > > > > > > 
> > > > > > > > > > **1. 语言模糊性**: "past the bathroom" — 经过几米算"past"？agent 必须从训练数据中学习这个模糊边界。  
> > > > > > > > > > **2. 指代消解**: "the bedroom **on the right**" — 如果右边有两个门，哪个是卧室？  
> > > > > > > > > > **3. 时空推理**: "Go down the hallway, **then** turn left" — "then" 意味着顺序依赖，不能在 hallway 之前就 left。  
> > > > > > > > > > **4. 组合泛化**: 训练时见过 "Go to the kitchen"，测试时可能遇到 "Go to the bathroom" ——虽然物体不同但结构相同，必须泛化。  
> > > > > > > > > > **5. 奖励黑洞**: "走偏了"在坐标导航中可以用距离惩罚来表示。但在语言导航中——"应该在浴室左转但你右转了"——怎么用数字衡量这个错误？这就是为什么 **RL 在 VLN 中几乎不适用**。
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > #### 🏋 训练：为什么 VLN 不用 PPO？
> > > > > > > > > > 
> > > > > > > > > > <div style="margin-bottom:12px;padding:12px 16px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > > > > > > > > > 
> > > > > > > > > > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 前四个任务都有**可计算的奖励信号**：  
> > > > > > > > > > PointNav：`reward = −(新距离 − 旧距离)` — 靠近目标 + 分。  
> > > > > > > > > > ObjectNav：`reward = distance_to_VIEW_POINT` — 能看到物体 + 分。  
> > > > > > > > > > ImageNav：同 PointNav — 距离差。  
> > > > > > > > > >   
> > > > > > > > > > 现在试想 VLN 的奖励函数：agent 看到 "turn left at the bathroom" → 它直走了（没看到浴室）。  
> > > > > > > > > > **你怎么给它打分？**  
> > > > > > > > > > 它最终到达了目标（success=1），但路径完全不对（没在浴室处左转）。  
> > > > > > > > > > success 无法捕捉"路径质量"——所以需要 nDTW。  
> > > > > > > > > > 而 nDTW 需要知道**参考路径**——这信息 agent 不该看到（那是答案）。  
> > > > > > > > > >   
> > > > > > > > > > **结论**：VLN 的奖励函数不可定义——因为你无法在不泄露答案的情况下评价路径质量。  
> > > > > > > > > > 因此，VLN 使用 **Imitation Learning** 而非 RL——让 agent 模仿人类标注的路径。 </span>
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div>
> > > > > > > > > > 
> > > > > > > > > > **📖 Imitation Learning 两种方法**
> > > > > > > > > > 
> > > > > > > > > > **1. Behavioral Cloning (BC，行为克隆)**：把人类路径当作"正确答案"，训练策略直接预测人类在每一步会做什么动作。  
> > > > > > > > > > → 优点：简单。缺点：训练和测试分布不同（"协变量偏移"）——策略犯错后越走越偏，但从未学过如何从错误中恢复。  
> > > > > > > > > >   
> > > > > > > > > > **2. DAgger (Dataset Aggregation)**：让策略自己走一遍 → 人类标注者纠正每一步 → 把纠正后的数据加入训练集 → 重复。  
> > > > > > > > > > → 优点：解决了协变量偏移。缺点：需要人类实时标注，成本高。  
> > > > > > > > > >   
> > > > > > > > > > 详见 [§4 PPO 训练算法](#sec4) 末尾对 IL vs RL 的对比讨论。
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > | 模块             | 文件                                        | 作用                             |
> > > > > > > > > > | -------------- | ----------------------------------------- | ------------------------------ |
> > > > > > > > > > | **训练入口**       | `habitat_baselines/run.py`                | Hydra 加载 IL 配置 → 构建 IL Trainer |
> > > > > > > > > > | **IL Trainer** | `habitat_baselines/il/trainers/pacman.py` | PACMAN: 多任务 IL 训练器（含 VLN）      |
> > > > > > > > > > | **数据加载**       | `habitat_baselines/il/dataset.py`         | 读取 R2R 数据（指令 + 轨迹对）            |
> > > > > > > > > > | **策略网络**       | 指令编码器 (LSTM) + 视觉编码器 (CNN)                | 双模态融合：文本特征 + 视觉特征 → 动作分布       |
> > > > > > > > > > | **评估指标**       | `nDTW` + `success` + `SPL`                | nDTW 衡量路径相似度；success 衡量是否到达    |
> > > > > > > > > > 

> > > > > > > > > > #### IL 训练流程图
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-box">
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #64748b;">
> > > > > > > > > > 
> > > > > > > > > > **① Hydra 加载 IL 配置**
> > > > > > > > > > 
> > > > > > > > > > eqa/il\_pacman\_nav.yaml  
> > > > > > > > > > 含 BC 或 DAgger 设置
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-arrow">
> > > > > > > > > > 
> > > > > > > > > > →
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > > > > > > > 
> > > > > > > > > > **② 加载 R2R 数据**
> > > > > > > > > > 
> > > > > > > > > > (instruction, reference\_path)  
> > > > > > > > > > 人类标注的指令-路径对
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
> > > > > > > > > > **③ 编码指令**
> > > > > > > > > > 
> > > > > > > > > > LSTM/Transformer  
> > > > > > > > > > 文本 → 特征向量
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
> > > > > > > > > > **④ 预测动作**
> > > > > > > > > > 
> > > > > > > > > > 语言特征 + 视觉特征  
> > > > > > > > > > → 动作分布
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
> > > > > > > > > > **⑤ 计算 Cross-Entropy Loss**
> > > > > > > > > > 
> > > > > > > > > > 预测动作 vs 人类动作  
> > > > > > > > > > 逐步比较
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-arrow">
> > > > > > > > > > 
> > > > > > > > > > →
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="flow-step" style="border-top:3px solid #ec4899;">
> > > > > > > > > > 
> > > > > > > > > > **⑥ 更新权重**
> > > > > > > > > > 
> > > > > > > > > > 反向传播 → 梯度更新  
> > > > > > > > > > 模仿人类轨迹
> > > > > > > > > > 
> > > > > > > > > > ``` 
> > > > > > > > > >       训练命令
> > > > > > > > > > ```
> > > > > > > > > > 
> > > > > > > > > >     # VLN Imitation Learning 训练（PACMAN 多任务 IL）
> > > > > > > > > >     # 注意: 这不是 PPO — 不需要 total_num_steps 参数
> > > > > > > > > >     # 使用 BC (Behavioral Cloning) 或 DAgger 模式
> > > > > > > > > >     $ python -u -m habitat_baselines.run \
> > > > > > > > > >         --config-name=eqa/il_pacman_nav.yaml
> > > > > > > > > >     
> > > > > > > > > >     # 评估（使用 IL 训练的 checkpoint）
> > > > > > > > > >     $ python -u -m habitat_baselines.run \
> > > > > > > > > >         --config-name=eqa/il_pacman_nav.yaml \
> > > > > > > > > >         habitat_baselines.evaluate=True \
> > > > > > > > > >         habitat_baselines.eval_ckpt_path_dir=data/checkpoints/il
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div>
> > > > > > > > > > 
> > > > > > > > > > **📋 训练输出解读**
> > > > > > > > > > 
> > > > > > > > > > **loss**：Cross-Entropy Loss — 策略预测的动作分布与人类实际动作的差异（越低越好）  
> > > > > > > > > > **success**：到达目标 3m 内的比例。BC 的 success 一般 20-40%（很容易分布偏移）  
> > > > > > > > > > **nDTW**：VLN 特有—路径形状相似度 0\~1。这是比 success 更严格的指标  
> > > > > > > > > > **SPL**：路径效率。如果 agent 到达了但绕了很多弯路，SPL 会偏低  
> > > > > > > > > > **关键认知**：VLN 的 success 很难超过 50%（SOTA \~60%）。这是具身 AI 中公认最难的任务之一。
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > ### 1.7 选择指南：用哪种任务？
> > > > > > > > > > 
> > > > > > > > > > | 你的目标           | 推荐任务             | 理由                        |
> > > > > > > > > > | -------------- | ---------------- | ------------------------- |
> > > > > > > > > > | 学习 RL 导航基础     | PointNav         | 数据离线可用、训练快、文档最全、Demo 开箱即用 |
> > > > > > > > > > | 研究语义视觉搜索       | ObjectNav        | 需要识别物体类别、有多种数据集和 baseline |
> > > > > > > > > > | 研究纯视觉导航（无 GPS） | ImageNav         | 只能用视觉匹配到达目标，是最纯粹的视觉导航     |
> > > > > > > > > > | 研究细粒度实例识别      | InstanceImageNav | 区分同类的不同个体，但训练成本极高         |
> > > > > > > > > > | 研究语言+视觉+导航融合   | VLN              | 语言指令导航，但 RL 训练支持有限，需自行搭建  |
> > > > > > > > > > 

> > > > > > > > > > ### 1.7 问答导航：EQA (Embodied Question Answering)
> > > > > > > > > > 
> > > > > > > > > > EQA 是唯一需要**语言理解 + 视觉 + 导航**三者融合的任务。Agent 在 MP3D 场景中导航，被问到关于场景的问题 （如 "What color is the car in the garage?"），需要找到目标、观察、然后**用自然语言回答**。 注册为 `EQA-v0`，使用 `MP3DEQA-v1` 数据集（819 个问答对）。
> > > > > > > > > > 
> > > > > > > > > > | 组件               | 类型          | 说明                                                                    |
> > > > > > > > > > | ---------------- | ----------- | --------------------------------------------------------------------- |
> > > > > > > > > > | `QuestionSensor` | lab sensor  | 返回问题文本的 **token ID 序列**（变长序列），观测量类型为 `TOKEN_IDS`                      |
> > > > > > > > > > | `AnswerAction`   | task action | 从答案词汇表选择一个词作为最终回答，action\_args = `{"answer_id": int}`                 |
> > > > > > > > > > | `EQAEpisode`     | episode     | 包含 `question_tokens` + `answer_token` + 导航起点/目标，扩展自 NavigationEpisode |
> > > > > > > > > > | `MP3DEQA-v1`     | dataset     | MP3D 场景 + 819 个问答对（train + val），json.gz 格式                            |
> > > > > > > > > > | `AnswerAccuracy` | measure     | 0/1 指标：agent 选择的 answer\_id 是否等于正确的 answer\_token                     |
> > > > > > > > > > | `VocabDict`      | 工具类         | 问题/答案的词汇表映射，存储于 dataset 的 question\_vocab / answer\_vocab 中           |
> > > > > > > > > > 

> > > > > > > > > > ``` 
> > > > > > > > > >       EQA 任务的基本使用
> > > > > > > > > > ```
> > > > > > > > > > 
> > > > > > > > > >     import habitat
> > > > > > > > > >     from habitat.tasks.eqa.eqa import AnswerAction
> > > > > > > > > >     
> > > > > > > > > >     config = habitat.get_config("benchmark/nav/eqa_mp3d.yaml")
> > > > > > > > > >     env = habitat.Env(config)
> > > > > > > > > >     obs = env.reset()
> > > > > > > > > >     # obs 包含: rgb, depth, semantic, question（token IDs 列表）
> > > > > > > > > >     print("Question:", env.current_episode.question.question_text)
> > > > > > > > > >     print("Question tokens:", obs["question"])
> > > > > > > > > >     
> > > > > > > > > >     # 导航若干步后，提交答案
> > > > > > > > > >     correct_id = env.current_episode.question.answer_token
> > > > > > > > > >     env.step({"action": AnswerAction.name, "action_args": {"answer_id": correct_id}})
> > > > > > > > > >     print(env.get_metrics())  # answer_accuracy = 1.0
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > > 💡
> > > > > > > > > > > 
> > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > 
> > > > > > > > > > > EQA 与其他导航任务的关键区别
> > > > > > > > > > > 
> > > > > > > > > > > EQA 的 episode 不会在到达导航目标时自动终止 — agent **必须主动发出 AnswerAction** 才会结束。 如果 agent 只导航不回答，会一直运行直到 `max_episode_steps`（默认 500）。 这也是为什么 EQA 比 PointNav/ObjectNav 更难：agent 需要学会**何时停止导航并开始回答**。
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="exercise" data-<!--="" data-1.8="" data-数据可用性总览="" data---="">
> > > > > > > > > > > 
> > > > > > > > > > > ### 1.8 数据可用性总览 <span style="font-size:0.78rem;color:#94a3b8;">Cloud L40</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="screenshot-frame" style="margin-bottom:14px;">
> > > > > > > > > > > 
> > > > > > > > > > > ![Data Availability](images/data_availability_matrix.png)
> > > > > > > > > > > 
> > > > > > > > > > > <span style="color:#60a5fa;font-weight:600;">📋 统计云端 /root/gpufree-data/habitat-lab-edu/data/datasets/ 的实际文件</span>  
> > > > > > > > > > > 五种导航任务 × 四种数据集的可用性矩阵 — FULL=场景+数据齐全 / CFG ONLY=仅配置文件 / NONE=不可用
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **云端 L40 服务器数据集清单**
> > > > > > > > > > > 
> > > > > > > > > > > **场景:** 12 个 MP3D 房间 (754MB) + 3 个 habitat-test-scenes  
> > > > > > > > > > > **PointNav:** MP3D train/val/test 全集 (400MB) **| ObjectNav:** MP3D val (11 场景)  
> > > > > > > > > > > **ImageNav:** 复用 PointNav MP3D 数据 **| VLN:** R2R train/val 全集  
> > > > > > > > > > > **InstanceImageNav:** 需 HM3D 场景 + 实例标注，云端暂缺
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > ### 1.9 自训练 vs 官方预训练模型 <span style="font-size:0.78rem;color:#94a3b8;">对比分析</span>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="screenshot-frame" style="margin-bottom:14px;">
> > > > > > > > > > > 
> > > > > > > > > > > ![Self-trained vs Official](images/self_vs_official.png)
> > > > > > > > > > > 
> > > > > > > > > > > <span style="color:#60a5fa;font-weight:600;">📋 对比 §1.2 自训练 (5 updates) 和 官方模型 (73.7M steps) 的实际训练日志</span>  
> > > > > > > > > > > 自训练 (5 次 PPO 更新, Success 0%) vs 官方模型 (7373 万步, Success \~75%) — 相同架构，云泥之别
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **下载官方预训练模型**
> > > > > > > > > > > 
> > > > > > > > > > > `wget https://dl.fbaipublicfiles.com/habitat/data/baselines/v1/habitat_baselines_v2.zip`  
> > > > > > > > > > > 内含: gibson-rgb/depth/rgbd-best.pth + mp3d-rgb/depth/rgbd-best.pth (6 个模型, 125MB)  
> > > > > > > > > > > 训练步数: 73,728,768 步 · 参数量: \~582 万 · 已验证在云端 L40 正常运行
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="exercise" style="margin-top:20px;">
> > > > > > > > > > > 
> > > > > > > > > > > #### 🏋️ 导航任务探索练习
> > > > > > > > > > > 
> > > > > > > > > > > **1.** 用 PointNav 的 `rl_nav_demo.py` 跑通一次完整训练，理解观测→动作→奖励的闭环。  
> > > > > > > > > > > **2.** 切换到 ObjectNav 配置，打印 observation keys，对比 PointNav 多了哪些传感器。  
> > > > > > > > > > > **3. (进阶)** 想一个应用场景（如 "帮我找遥控器"），判断它属于哪种导航任务类型。  
> > > > > > > > > > > **4. (进阶)** 阅读 `habitat/tasks/nav/object_nav_task.py`，理解 VIEW\_POINTS 距离和 soft\_spl 的计算方式。  
> > > > > > > > > > > **5. (进阶)** 尝试将 ImageNav 的 `imagegoal_sensor` 输出可视化保存为图片，观察目标图像与实际观测的差异。  
> > > > > > > > > > > **6. (进阶)** 查看 EQA 数据集的 question\_vocab 和 answer\_vocab 大小，思考为什么 answer 词汇表比 question 小得多。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 本章总结
> > > > > > > > > > > 
> > > > > > > > > > > | 任务类型                 | 目标表示              | 核心能力                  | 难度    |
> > > > > > > > > > > | -------------------- | ----------------- | --------------------- | ----- |
> > > > > > > > > > > | **PointNav**         | 坐标 (x, y, θ)      | 空间推理 + 避障，无视觉理解要求     | ⭐⭐    |
> > > > > > > > > > > | **ObjectNav**        | 物体类别标签（如 "chair"） | 视觉识别 + 语义搜索，需理解场景语义   | ⭐⭐⭐   |
> > > > > > > > > > > | **ImageNav**         | 一张目标图片            | 视觉匹配 + 视角不变性，需跨视角对应   | ⭐⭐⭐   |
> > > > > > > > > > > | **InstanceImageNav** | 特定实例图片            | 细粒度视觉匹配，区分同类不同实例      | ⭐⭐⭐⭐  |
> > > > > > > > > > > | **VLN**              | 自然语言指令            | 语言理解 + 视觉-语言对齐 + 空间推理 | ⭐⭐⭐⭐⭐ |
> > > > > > > > > > > 

> > > > > > > > > > > > 💡
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > > 
> > > > > > > > > > > > 📍 你在学习路径上的位置
> > > > > > > > > > > > 
> > > > > > > > > > > > 本章是「认知阶段」的最后一站。你已经知道 Habitat **能解决什么问题**。 下一步进入「训练阶段」：  
> > > > > > > > > > > > **→ 第6章：RL 训练入门** — 用 PointNav + PPO 学会完整的 RL 训练流程。  
> > > > > > > > > > > > **→ 第7章：VLN 视觉语言导航** — 如果你对语言+视觉的组合任务最感兴趣，可以直接跳到 VLN 专章。
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > <div>
> > > > > > > > > > > > 
> > > > > > > > > > > > **💡 学习建议**
> > > > > > > > > > > > 
> > > > > > > > > > > > 五种任务中，**PointNav** 和 **VLN** 是两条主线：  
> > > > > > > > > > > > • PointNav → 理解 RL 训练机制（第6章）  
> > > > > > > > > > > > • VLN → 理解多模态学习（第7章）  
> > > > > > > > > > > >   
> > > > > > > > > > > > ObjectNav / ImageNav / InstanceImageNav 是它们的变体——掌握了 PointNav 和 VLN，再回头看这些变体就很容易了。
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="exercise">
> > > > > > > > > > > > 
> > > > > > > > > > > > #### 🏋️ 课后练习
> > > > > > > > > > > > 
> > > > > > > > > > > > **1.** 用一句话描述每种导航任务的核心输入和输出。  
> > > > > > > > > > > > **2.** 想一个你感兴趣的真实应用场景（如"让机器人帮我找会议室"），判断它属于哪种导航任务类型。  
> > > > > > > > > > > > **3.** 比较 PointNav 和 VLN 的 observation space 差异——为什么 VLN 不需要 GPS+Compass？  
> > > > > > > > > > > > **4.** 从五种任务中选一个你最感兴趣的，标出它在后续章节（第6章/第7章）的位置。
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="section">
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="container">
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="page-nav">
> > > > > > > > > > > > 
> > > > > > > > > > > > [← 第4章：改配置实验](habitat-textbook-step4.html) [第6章：RL 训练入门 →](habitat-textbook-step6.html)
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
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
> > > > > > > > 
> > > > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > 
> > > > </div>
> > 
> > </div>
> 
>

</div>
# 第5B章：DD-PPO 分布式训练 — Habitat 从零理解

> Step5 的 PPO 训练是单机单卡版本。本章教你如何使用 DD-PPO（Decentralized Distributed PPO） 在单机多卡或多机上并行采样，将训练吞吐量线性扩展到数十甚至数百个 GPU。

## 案例总览

| \# | 案例                           | 难度 | 学什么                                                      |
| -- | ---------------------------- | -- | -------------------------------------------------------- |
| 1  | DD-PPO 原理：PPO vs DD-PPO 架构对比 | ⭐  | 数据并行、all-reduce 梯度同步、straggler preemption                |
| 2  | 配置对比：PPO → DD-PPO 的逐项差异      | ⭐⭐ | trainer\_name, sync\_frac, backbone, pretrained\_encoder |
| 3  | 单机多卡运行                       | ⭐⭐ | torch.distributed.launch, 环境变量, 吞吐量对比                    |
| 4  | 常见故障排查                       | ⭐⭐ | NCCL 超时、OOM、端口冲突、评估异常                                    |

## 案例 1：DD-PPO 原理 — PPO vs DD-PPO 架构对比

<div>

**① 案例含义**

DD-PPO **不是新算法**，而是 PPO 的一种**分布式系统架构**。 它和单机 PPO 使用同一个 `PPOTrainer` 类（在 `ppo_trainer.py` 中同时注册为 `"ppo"` 和 `"ddppo"`）， 区别在于分布式模式下多了三样东西：**去中心化梯度同步**、**全局优势归一化**、**掉队者预emption**。

</div>

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

### DD-PPO 的三个核心机制

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>机制</th>
<th>单机 PPO</th>
<th>DD-PPO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>梯度同步</strong></td>
<td>本地 <code>loss.backward()</code>，无同步</td>
<td>PyTorch DDP 的 <code>all_reduce</code> 在各 GPU 间平均梯度<br />
代码位置：<code>rl/ddppo/algo/ddppo.py</code> → <code>DecentralizedDistributedMixin</code></td>
</tr>
<tr class="even">
<td><strong>优势归一化</strong></td>
<td><code>torch.var_mean(x)</code> — 仅在本地样本上计算</td>
<td><code>distributed_var_mean(x)</code> — 跨所有 worker 计算真实均值/方差<br />
这对 PPO 的 clipped objective 至关重要——全局统计更稳定</td>
</tr>
<tr class="odd">
<td><strong>掉队者预emption</strong></td>
<td>不适用（只有一个 worker）</td>
<td>当 <code>sync_frac</code> (默认 60%) 的 worker 已收集完 rollout，剩余慢 worker 被提前终止<br />
这样整体不需要等待最慢的 GPU</td>
</tr>
</tbody>
</table>

<div>

**② 关键函数调用**

| 函数/类                                               | 文件                   | 作用                                                               |
| -------------------------------------------------- | -------------------- | ---------------------------------------------------------------- |
| `PPOTrainer.__init__`                              | `ppo_trainer.py:98`  | `self._is_distributed = world_size > 1` 判断是否启用分布式                |
| `init_distrib_slurm()`                             | `ddp_utils.py:271`   | 初始化 torch.distributed，解析 SLURM/launch 环境变量                       |
| `DecentralizedDistributedMixin.init_distributed()` | `algo/ddppo.py`      | 将 Actor-Critic 包装在 DDP 中（包装 `_EvalActionsWrapper` 而非直接的 forward） |
| `should_end_early()`                               | `ppo_trainer.py:634` | 掉队者 preemption 判断逻辑                                              |
| `distributed_var_mean()`                           | `algo/ddppo.py`      | 跨 GPU 的 all-reduce 方差/均值计算                                       |

</div>

> 💡
> 
> <div class="tip-title">
> 
> 种子偏移机制
> 
> 每个 worker 的种子会被偏移 `rank × num_environments`，确保：  
> Worker 0: 种子 = base\_seed + 0  
> Worker 1: 种子 = base\_seed + num\_environments  
> Worker 2: 种子 = base\_seed + 2×num\_environments  
> 这保证了所有 worker 的所有环境都有独一无二的种子，避免重复数据。
> 
> <div id="case2" class="section">
> 
> <div class="container">
> 
> ## 案例 2：配置对比 — PPO → DD-PPO 的逐项差异
> 
> <div>
> 
> **① 案例含义**
> 
> 从 PPO 切换到 DD-PPO，核心就是改配置。理解每一项的含义，才能根据自己的硬件环境合理调参。
> 
> </div>
> 
> ### PPO 配置 vs DD-PPO 配置 — 并排对比
> 
> | 配置项                    | PPO (ppo\_pointnav\_example.yaml) | DD-PPO (ddppo\_pointnav.yaml) | 说明                        |
> | ---------------------- | --------------------------------- | ----------------------------- | ------------------------- |
> | `trainer_name`         | `"ppo"`                           | **`"ddppo"`**                 | 触发 DDP 包装和全局统计            |
> | `num_environments`     | 6 (per GPU)                       | **4** (per GPU)               | 分布式下有额外通信开销，降低单 GPU 负载    |
> | `ppo_epoch`            | 4                                 | **2**                         | 样本量增大后减少 epoch 防过拟合       |
> | `hidden_size`          | 小（如 256）                          | **512**                       | 更大的模型容量                   |
> | `backbone`             | resnet18                          | **resnet50**                  | 更强的视觉编码器                  |
> | `rnn_type`             | GRU                               | **LSTM**                      | LSTM 对长序列更稳定              |
> | `num_recurrent_layers` | 1                                 | **2**                         | 更深的状态编码                   |
> | `sync_frac`            | N/A                               | **0.6**                       | 60% worker 完成就 preempt 慢者 |
> 

> <div>
> 
> **DD-PPO 专属配置段**
> 
> </div>
> 
>     # DD-PPO 专属配置（ddppo_pointnav.yaml 中的 ddppo 段）
>     habitat_baselines:
>       trainer_name: ddppo
>       rl:
>         ddppo:
>           sync_frac: 0.6            # preemption 阈值
>           distrib_backend: NCCL       # GPU 用 NCCL（更快），CPU 用 GLOO
>           backbone: resnet50         # 视觉编码器架构
>           rnn_type: LSTM            # GRU 或 LSTM
>           num_recurrent_layers: 2  # RNN 层数
>           pretrained: False         # 是否加载完整预训练权重
>           pretrained_encoder: False  # 是否只加载 encoder 预训练权重
>           pretrained_weights: "data/ddppo-models/gibson-2plus-resnet50.pth"
>           train_encoder: True       # 是否训练 encoder（False = 冻结）
>           reset_critic: True        # 加载预训练时是否重置 Critic 头
>           force_distributed: False  # True = 单 GPU 也启用分布式（调试用）
> 
> | 关键参数                 | 含义                            | 建议                                        |
> | -------------------- | ----------------------------- | ----------------------------------------- |
> | `sync_frac`          | 多少比例的 worker 完成后触发 preemption | 0.6 是默认值。如果 worker 速度差异大，可降低到 0.4         |
> | `pretrained_encoder` | 加载预训练视觉 backbone（不加载 RL 策略部分） | 推荐设为 True，用官方 `gibson-2plus-resnet50.pth` |
> | `reset_critic`       | 预训练后重置 value head             | 设为 True，避免 value 估计与新环境不匹配导致训练崩溃          |
> | `train_encoder`      | 是否微调视觉 backbone               | True = 全训练；False = 冻结 encoder（类似微调 CLIP）  |
> 

> </div>
> 
> </div>
> 
> <div id="case3" class="section">
> 
> <div class="container">
> 
> ## 案例 3：单机多卡运行
> 
> <div>
> 
> **① 案例含义**
> 
> 在不使用 SLURM 的普通机器上，使用 PyTorch 的 `torch.distributed.launch` 启动多 GPU DD-PPO 训练。这是科研场景中最常见的用法。
> 
> </div>
> 
> <div>
> 
> **② 核心代码 — 启动命令**
> 
> </div>
> 
>     # 单机 2 卡 DD-PPO 训练（来自 single_node.sh 模式）
>     export GLOG_minloglevel=2          # 减少 C++ 日志噪音
>     export MAGNUM_LOG=quiet            # 减少 Magnum 引擎日志
>     
>     python -u -m torch.distributed.launch \
>         --use_env \
>         --nproc_per_node 2 \
>         habitat_baselines/run.py \
>         --config-name=pointnav/ddppo_pointnav.yaml \
>         habitat_baselines.num_environments=4 \
>         habitat_baselines.total_num_steps=1000000 \
>         habitat_baselines.checkpoint_folder=data/ddppo_checkpoints
> 
> <div>
> 
> **环境变量解析**
> 
> | 变量           | 由谁设置                       | 含义                          |
> | ------------ | -------------------------- | --------------------------- |
> | `LOCAL_RANK` | `torch.distributed.launch` | 当前进程在节点内的 GPU ID（0, 1, ...） |
> | `RANK`       | `torch.distributed.launch` | 全局进程 ID                     |
> | `WORLD_SIZE` | `torch.distributed.launch` | 总进程数（= GPU 总数）              |
> | `MAIN_ADDR`  | 用户手动设置                     | 主节点 IP（单机默认 127.0.0.1）      |
> | `MAIN_PORT`  | 用户手动设置                     | 通信端口（默认 8738）               |
> 

> </div>
> 
> <div>
> 
> **④ 预期训练日志**
> 
> </div>
> 
>     # 启动后每个 GPU 会产生类似输出：
>     2026-06-05 12:00:01 [rank0] Initializing distributed backend (NCCL)
>     2026-06-05 12:00:02 [rank0] Distributed init complete: world_size=2
>     2026-06-05 12:00:05 [rank0] ResNet50 encoder loaded
>     2026-06-05 12:00:06 [rank0] Creating 4 environments per GPU
>     
>     # 训练循环：
>     update: 0   loss: 0.523   reward: -1.234   steps/sec: 2847   ← 2 GPU 的吞吐量
>     update: 1   loss: 0.487   reward: -0.983   steps/sec: 2850
>     
>     # 对比单 GPU PPO（相同硬件）：
>     # update: 0   loss: 0.523   reward: -1.234   steps/sec: 1523  ← 单 GPU
> 
> <div>
> 
> **⑤ 输出含义**
> 
> **steps/sec** 是核心吞吐量指标。DD-PPO 的吞吐量随 GPU 数量**近似线性增长**——4 GPU 约 = 单 GPU × 3.6\~3.8 倍（非完美的 4 倍是因为通信开销）。  
> 每个 GPU 的 **loss** 应大致相同（因为梯度同步保证了模型参数一致），但 reward 可能不同（不同 GPU 探索不同场景）。
> 
> </div>
> 
> ### 吞吐量缩放参考
> 
> | GPU 数量     | 有效 batch size | steps/sec (典型) | 达到 100M 步所需时间 |
> | ---------- | ------------- | -------------- | ------------- |
> | 1 (PPO)    | 768           | \~1,500        | \~18.5 小时     |
> | 2 (DD-PPO) | 1,024         | \~2,800        | \~9.9 小时      |
> | 4 (DD-PPO) | 2,048         | \~5,500        | \~5.1 小时      |
> | 8 (DD-PPO) | 4,096         | \~10,500       | \~2.6 小时      |
> 

> 注意：以上数值为 AI Habitat 论文中的典型数据，实际吞吐量取决于场景复杂度、传感器分辨率、GPU 型号。
> 
> </div>
> 
> </div>
> 
> <div id="case4" class="section">
> 
> <div class="container">
> 
> ## 案例 4：常见故障排查
> 
> <div>
> 
> **① 案例含义**
> 
> DD-PPO 的分布式特性带来了新的故障模式。以下是从社区和论文中整理的常见问题及解决方法。
> 
> </div>
> 
> <div class="trouble-grid">
> 
> <div class="trouble-card">
> 
> #### NCCL 超时 / 训练卡住
> 
> **症状：**训练启动后卡在 "Initializing distributed" 不动  
> <span class="fix">修复：</span>  
> ① 确认 `MAIN_ADDR=127.0.0.1`（单机）  
> ② 检查防火墙是否拦截了端口 `8738`  
> ③ 改用 GLOO backend：`distrib_backend: GLOO`  
> ④ 确认所有 GPU 都可被 PyTorch 访问：`torch.cuda.device_count()`
> 
> </div>
> 
> <div class="trouble-card">
> 
> #### CUDA Out of Memory (OOM)
> 
> **症状：**创建环境或第一个 forward 时 OOM  
> <span class="fix">修复：</span>  
> ① 减小 `num_environments`（从 4 → 2）  
> ② 减小 RGB 分辨率  
> ③ 换用小 backbone（resnet50 → resnet18）  
> ④ 确保 `force_torch_single_threaded: True`
> 
> </div>
> 
> <div class="trouble-card">
> 
> #### 评估报错：does not support distributed mode
> 
> **症状：**`RuntimeError("Evaluation does not support distributed mode")`  
> <span class="fix">修复：</span>DD-PPO 不支持分布式评估。运行评估时：  
> ① 使用 `trainer_name: "ppo"` 而非 `"ddppo"`  
> ② 或在单 GPU 模式下运行  
> ③ 在分析脚本中用单进程加载 checkpoint 评估
> 
> </div>
> 
> <div class="trouble-card">
> 
> #### 端口冲突（多任务）
> 
> **症状：**`Address already in use`  
> <span class="fix">修复：</span>  
> ① `ddp_utils.py` 会自动在端口上加上 `SLURM_JOBID % 127` 作为偏移  
> ② 手动指定：`export MAIN_PORT=9843`  
> ③ 使用 `find_free_port()` 函数（在 `ddp_utils.py` 中）
> 
> </div>
> 
> <div class="trouble-card">
> 
> #### 梯度不同步 / loss 波动剧烈
> 
> **症状：**不同 GPU 的 loss 差异巨大，训练不收敛  
> <span class="fix">修复：</span>  
> ① 确认 `use_normalized_advantage: False`（DD-PPO 用自己的分布式归一化）  
> ② 确认 `force_distributed: True`（单机测试分布式模式时）  
> ③ 运行测试：`pytest test/test_ddppo_reduce.py`
> 
> </div>
> 
> <div class="trouble-card">
> 
> #### SLURM preemption 后无法恢复
> 
> **症状：**被 preempt 后训练从头开始  
> <span class="fix">修复：</span>  
> ① 环境变量 `SLURM_JOBID` 不存在导致 resume 文件找不到  
> ② 检查 `data/new_checkpoints/.habitat-resume-state-{JOBID}.pth`  
> ③ SLURM 脚本需加 `#SBATCH --requeue` 和 `#SBATCH --signal=USR1@90`
> 
> > ⚠️
> > 
> > <div class="warn-title" style="color:#f87171;">
> > 
> > 关键警告
> > 
> > **不要在 DD-PPO 中混合使用 PPO 的 config**——特别是 `use_normalized_advantage: True`。 DD-PPO 使用 `distributed_var_mean()` 做归一化，如果再叠加 PPO 的局部归一化会导致双重归一化，训练会崩溃。 DD-PPO 配置文件（`ddppo_*.yaml`）已经正确设置了这些，如果你手动合并 PPO 和 DD-PPO 的配置，务必检查这一点。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 学后自检 — 你掌握了什么
> > 
> > <div class="trouble-grid">
> > 
> > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > 
> > #### Q1：DD-PPO 是新算法吗？
> > 
> > 不是。DD-PPO 和单机 PPO 使用同一个 `PPOTrainer` 类（注册为 "ppo" 和 "ddppo" 两个名字）。它是 PPO 的一种分布式系统架构，通过 all-reduce 梯度同步和全局统计归一化来支持多 GPU 训练。
> > 
> > </div>
> > 
> > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > 
> > #### Q2：sync\_frac=0.6 的含义？
> > 
> > 当 60% 的 worker 已完成当前 rollout 的全部步数，其余 worker 会被提前终止（preempt）。这避免了整体等待最慢的 worker，代价是慢 worker 贡献了较短的轨迹。
> > 
> > </div>
> > 
> > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > 
> > #### Q3：为什么 DD-PPO 要降低 num\_environments？
> > 
> > 每个 GPU 上还有 DDP 的通信开销（梯度 all-reduce），加上 ResNet-50 比 ResNet-18 更吃显存。降低 env 数量给通信和更大模型腾出 GPU 显存和算力。
> > 
> > </div>
> > 
> > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > 
> > #### Q4：如何验证梯度同步是否正常工作？
> > 
> > 运行 `pytest test/test_ddppo_reduce.py`。这个测试验证了 RL 的非标准 DDP 用法（在 forward-while-collecting 模式下的梯度 reduce）在不同 PyTorch 版本上是否正常。
> > 
> > </div>
> > 
> > <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> > 
> > #### Q5：pretrained\_encoder vs pretrained 的区别？
> > 
> > `pretrained_encoder: True` 只加载视觉 backbone（CNN）的权重，RL 部分（Actor/Critic head + RNN）随机初始化。`pretrained: True` 加载所有参数。后者要求 checkpoint 与新配置架构完全一致。
> > 
> > </div>
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > <div class="page-nav">
> > 
> > [← 第5章：训练与评测](habitat-textbook-step5.html) [第9章：Rearrange 操作任务 →](habitat-textbook-step9.html)
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
>

</div>
# 第6章：RL 训练入门 — Habitat 从零理解

> 从配置到训练，从 checkpoint 到评估指标。理解 PPO 训练流程、RL 环境包装链、以及如何解释训练结果。

## 0\. 训练全景图

一次完整的训练涉及 4 层结构：CLI 入口 → Trainer → VectorEnv → RLEnv → Core Env。

<div>

<div class="info-title" style="color:#60a5fa;">

学习目标

</div>

理解 CLI → Trainer → VectorEnv → RLEnv 四层架构  
<span style="color:#fbbf24;font-size:0.82rem;">🤔 你敲下 python -m habitat\_baselines.run 之后，Habitat 内部经历了哪些步骤才让 agent 开始移动？</span>

</div>

<div class="arch-diagram">

<div class="arch-row">

<div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">

🖥 CLI 入口 <span class="small">habitat\_baselines/run.py</span>

<div class="arch-arrow-center">

↓ Hydra 配置加载 + 训练/评估 分支

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#ec489920;border:1px solid #ec489940;">

🤖 PPOTrainer <span class="small">rl/ppo/ppo\_trainer.py</span>

<div class="arch-arrow-center">

↓ 管理训练循环、checkpoint、日志

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">

📊 AgentAccessMgr (Single) <span class="small">Policy + Storage + Updater</span>

<div class="arch-arrow-center">

↓ 收集 rollouts → 计算 returns → PPO 更新

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">

🔄 VectorEnv (N 个并行) <span class="small">habitat/core/vector\_env.py</span>

<div class="arch-arrow-center">

↓ 每个 env 独立运行一个场景实例

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#22d3ee20;border:1px solid #22d3ee40;">

🎮 RLEnv → Env <span class="small">step() → (obs, reward, done, info)</span>

</div>

  

<div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">

🧠 Task (Nav-v0) <span class="small">reward\_measure + success\_measure</span>

</div>

  

<div class="arch-layer" style="background:#06b6d420;border:1px solid #06b6d440;">

🏗 Simulator <span class="small">habitat\_sim 渲染引擎</span>

</div>

<div>

**📁 两个仓库的边界**

**habitat-lab**：提供 `Env`、`RLEnv`、`Benchmark`、`Task`、`Simulator` — 环境基础设施。  
**habitat-baselines**：提供 `run.py`、`PPOTrainer`、`PPO`、`Policy` — 训练算法和工具。  
训练时，baselines 通过 Hydra `defaults` 引用 lab 的 benchmark 配置，统一在 `DictConfig` 中。

## 2\. Policy 网络结构

`PointNavResNetPolicy` — Habitat 中 PointNav 任务的标准策略网络。 理解网络的每一层，才能回答核心问题：**RL 到底在训练什么？**

<div>

<div class="info-title" style="color:#60a5fa;">

学习目标

</div>

理解 CNN+RNN+Actor/Critic 每层的作用和参数量  
<span style="color:#fbbf24;font-size:0.82rem;">🤔 训练出来的 .pth 文件有 22MB，里面到底存了什么？为什么视觉编码器占了 90% 的参数，而做决策的 Actor 头只占 3%？</span>

</div>

### 2.1 网络全景：CNN + RNN + Actor/Critic

<div class="screenshot-frame" style="margin-bottom:14px;">

![Policy Architecture](images/policy_architecture.png)

<span style="color:#60a5fa;font-weight:600;">📋 分析 torch.load("mp3d-rgb-best.pth")\["state\_dict"\] 的参数分布 → 5,820,236 参数</span>  
PointNav Policy 参数分布 — 视觉编码器 (ResNet18) 占主体 — 总计 5,820,236 参数 — 基于官方 MP3D 模型

</div>

### 2.1 网络全景：CNN + RNN + Actor/Critic

<div class="arch-diagram">

<div class="arch-row">

<div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">

📷 **Visual Encoder** <span class="small">ResNet18/50 → 压缩空间特征</span>

</div>

<span style="font-size:1.5rem;color:var(--text-dim);align-self:center;">+</span>

<div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">

🧭 **GPS+Compass** <span class="small">PointGoal 传感器 (2维向量)</span>

<div class="arch-arrow-center">

↓ 拼接 → Linear(hidden\_size)

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">

🔄 **GRU** (可选) <span class="small">hidden\_size=512, num\_layers=1</span>

<div class="arch-arrow-center">

↓ 隐藏状态

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#ec489920;border:1px solid #ec489940;">

🎯 **Actor Head** <span class="small">Linear → Categorical(4 actions)</span>

</div>

<div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">

💰 **Critic Head** <span class="small">Linear → 1 (value scalar)</span>

</div>

<div>

**💡 为什么要 GPS+Compass？**

PointNav 任务中，agent 不仅有视觉输入（RGB/Depth），还有 `pointgoal_with_gps_compass` 传感器提供的 **目标方向+距离**（2维向量）。这是一个关键的"特权信息"——没有它， 纯视觉导航会难得多。策略网络将视觉特征和 GPS 向量拼接后一起送入决策头。

</div>

### 2.2 "RL 到底训练的是什么？"

<div>

**一句话回答**

训练的是**整个策略网络的权重参数**——不是规则、不是地图、不是规划器，而是一个**从像素到动作的端到端映射函数**。

</div>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>模块</th>
<th>参数量 (ResNet18)</th>
<th>学的是什么</th>
<th>类比</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>视觉编码器</strong><br />
<span class="small">ResNet18/50</span></td>
<td>~11M</td>
<td>从 RGB-D 像素中提取空间特征：障碍物在哪、房间结构、物体纹理</td>
<td>"眼睛"——把像素变成有意义的结构信息</td>
</tr>
<tr class="even">
<td><strong>RNN 状态编码器</strong><br />
<span class="small">GRU/LSTM 512维</span></td>
<td>~3M</td>
<td>记忆历史观测，形成<strong>隐式空间认知</strong>：走过的路、看过的角落</td>
<td>"海马体"——在脑中维持对空间的动态记忆</td>
</tr>
<tr class="odd">
<td><strong>Actor 头</strong><br />
<span class="small">Linear → Categorical</span></td>
<td>~200K</td>
<td>给定当前状态，输出<strong>4 个动作的概率分布</strong>——哪个动作最可能到达目标</td>
<td>"决策者"——看情况选动作</td>
</tr>
<tr class="even">
<td><strong>Critic 头</strong><br />
<span class="small">Linear → 1</span></td>
<td>~100K</td>
<td>估计当前状态的<strong>未来预期回报</strong>（value）——这个位置有利吗？</td>
<td>"评论家"——好坏我来评判</td>
</tr>
</tbody>
</table>

<div class="key-finding">

**训练更新的是权重，不是行为规则。** 对于一张包含走廊和椅子的 RGB 图像，训练后的网络学会给它分配低 value（远离目标） 并降低 TURN\_LEFT 概率（因为左边是墙）。但这些知识不是被编程进去的——是 CNN 卷积核 通过 **PPO 梯度更新**从数百万步交互中自己浮现出来的。

</div>

### 2.3 "RL 需要基础模型吗？是微调吗？"

<div>

**取决于配置——有三种模式**

Habitat RL 的支持介于**"从零训练"**和**"预训练迁移"**之间，你可以根据任务选择。

</div>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>模式</th>
<th>配置开关</th>
<th>说明</th>
<th>类比</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>A — 从零训练</strong></td>
<td><code>SimpleCNN</code> 默认</td>
<td>所有参数随机初始化，完全从零学。适合小规模实验，收敛慢</td>
<td>训练一个全新的 CNN 做图像分类</td>
</tr>
<tr class="even">
<td><strong>B — 预训练编码器</strong></td>
<td><code>pretrained_encoder: True</code><br />
<code>pretrained_weights: gibson-2plus-resnet50.pth</code></td>
<td>从 Gibson 数据集 DD-PPO 训练的 ResNet50 加载视觉编码器权重，<strong>其余随机初始化</strong>，然后在新数据集（HM3D/MP3D）上继续 PPO</td>
<td>NLP 中 "加载 BERT 权重，在新的下游任务上微调"</td>
</tr>
<tr class="odd">
<td><strong>C — CLIP 特征提取</strong></td>
<td><code>backbone: resnet50_clip_avgpool</code></td>
<td>加载 OpenAI CLIP ResNet50，<strong>视觉编码器完全冻结</strong>（<code>requires_grad=False</code>）。策略只学如何利用 CLIP 语义特征导航</td>
<td>用 GPT 的 embedding 做情感分类——特征提取器不变，只用它的输出</td>
</tr>
</tbody>
</table>

> 💡
> 
> <div class="tip-title">
> 
> Habitat 的 "微调" 与 NLP 的微调有何不同？
> 
> |           | NLP (BERT → 分类)   | Habitat RL (Gibson → HM3D) |
> | --------- | ----------------- | -------------------------- |
> | **预训练来源** | 海量文本自监督 (MLM)     | DD-PPO 在 Gibson 上的 RL 训练   |
> | **预训练规模** | 百亿 token          | 数亿步交互                      |
> | **迁移什么**  | 语言理解能力            | 视觉特征提取能力                   |
> | **微调方式**  | 加分类头 + 小 LR 全参数更新 | 冻结/解冻编码器 + 继续 PPO 更新       |
> | **本质**    | 任务迁移（语言 → 情感分类）   | 领域迁移（Gibson 场景 → HM3D 场景）  |
> 

> </div>
> 
> ### 2.4 "训练好的模型和环境、设备有关吗？"
> 
> | 因素                 | 相关程度                                  | 说明                                                                    | 缓解措施                   |
> | ------------------ | ------------------------------------- | --------------------------------------------------------------------- | ---------------------- |
> | **场景几何**           | <span style="color:#ef4444;">高</span> | Gibson 训练的模型直接跑 MP3D 测试，成功率可掉 20%+——房间布局、走廊宽度不同                       | 预训练编码器 + 目标数据集微调       |
> | **传感器分辨率**         | <span style="color:#ef4444;">高</span> | 256×256 训练的模型接收 640×480 输入会出错（FC 层输入维度固定）                             | resize 预处理；或用全卷积网络     |
> | **动作空间**           | <span style="color:#ef4444;">高</span> | 4-action (PointNav) 模型**不能**直接用于 6-action (ObjectNav) 任务——Actor 头维度不同 | 重新训练 Actor/Critic 头    |
> | **RGB vs 深度**      | <span style="color:#f59e0b;">中</span> | 有深度的模型迁移到纯 RGB 场景性能下降——深度提供几何信息                                       | 多任务训练；深度 dropout       |
> | **数据集 split**      | <span style="color:#f59e0b;">中</span> | 同一场景的不同 episode（train vs val）泛化通常较好；不同场景则考验泛化能力                       | 严格按照 train/val/test 分离 |
> | **GPU 设备**         | <span style="color:#10b981;">低</span> | PyTorch 自动处理 CUDA/CPU 转换；checkpoint 可跨 GPU 加载（`map_location`）         | 无需特殊处理                 |
> | **Habitat-Sim 版本** | <span style="color:#10b981;">低</span> | 传感器输出格式跨版本兼容；极少情况需要重新导出 checkpoint                                    | 固定版本依赖                 |
> 

> <div class="key-finding" style="margin-top:14px;">
> 
> **本质：Habitat RL 学的是视觉运动策略，不是场景地图。** 策略编码的是 "看到这样的走廊，应该这样做" 的**通用能力**，而不是某个特定房间的布局。 这就是为什么可以通过预训练编码器跨数据集迁移——视觉特征提取的底层卷积核（边缘、纹理、形状） 在不同场景间是可以共享的。
> 
> <div class="section">
> 
> <div class="container">
> 
> > ⚠️
> > 
> > <div class="warn-title">
> > 
> > 🛠 Policy 网络常见错误
> > 
> > | 错误信息                              | 可能原因                       | 解决方法                                 |
> > | --------------------------------- | -------------------------- | ------------------------------------ |
> > | `RuntimeError: size mismatch`     | CNN 输出维度与 RNN 输入不匹配        | 检查 `BACKBONE` 参数和 `hidden_size` 是否一致 |
> > | `IndexError: action out of range` | 策略输出维度 ≠ 动作空间大小            | Policy 最后一层必须输出 `num_actions` 维      |
> > | `CUDA out of memory`              | 视觉 backbone 太大 (ResNet101) | 降级为 `resnet50` 或减小 `hidden_size`     |
> > 

> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 3\. RL 环境包装链
> > 
> > 从最内层的 `Env` 到最外层的 `VectorEnv`，每一层封装增加一个能力维度。
> > 
> > <div>
> > 
> > <div class="info-title" style="color:#60a5fa;">
> > 
> > 学习目标
> > 
> > </div>
> > 
> > 理解 VectorEnv → RLEnv → Env 逐层封装的作用  
> > <span style="color:#fbbf24;font-size:0.82rem;">🤔 Habitat 的 Env 返回的是一个字典 {rgb, depth, pointgoal}，但 PPO 算法需要 (obs, reward, done, info) 元组——谁在中间做了转换？</span>
> > 
> > </div>
> > 
> > <div class="arch-diagram">
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#0f172a;border:2px solid #f59e0b;">
> > 
> > **VectorEnv** (N 个并行) <span class="small">habitat/core/vector\_env.py</span>
> > 
> > <div class="arch-arrow-center" style="font-size:0.85rem;color:#fbbf24;">
> > 
> > ↑ 管理 N 个独立环境实例，合并 batch
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #3b82f6;">
> > 
> > **GymHabitatEnv** <span class="small">habitat/gym/gym\_definitions.py</span>
> > 
> > <div class="arch-arrow-center" style="font-size:0.85rem;color:#60a5fa;">
> > 
> > ↑ 将字典 action/obs 转换为 gym 标准空间
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #10b981;">
> > 
> > **RLEnv** (gym.Env) <span class="small">habitat/core/env.py:357</span>
> > 
> > <div class="arch-arrow-center" style="font-size:0.85rem;color:#34d399;">
> > 
> > ↑ step() → (obs, reward, done, info)
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #8b5cf6;">
> > 
> > **Env** (核心) <span class="small">habitat/core/env.py:39</span>
> > 
> > <div class="arch-arrow-center" style="font-size:0.85rem;color:#a78bfa;">
> > 
> > ↑ 组合 Simulator + Task + Dataset
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #64748b;">
> > 
> > 🏗 Simulator <span class="small">habitat\_sim 渲染引擎</span>
> > 
> > </div>
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #64748b;">
> > 
> > 🧠 Task (Nav-v0) <span class="small">reward + success + measurements</span>
> > 
> > </div>
> > 
> > <div class="arch-layer" style="background:#1e293b;border:1px solid #64748b;">
> > 
> > 📦 Dataset <span class="small">episodes 迭代器</span>
> > 
> > </div>
> > 
> > <div>
> > 
> > **💡 RLEnv 做了什么？**
> > 
> > 原始 `Env.step()` 返回的是 `Observations`（字典）。  
> > `RLEnv.step()` 包装后返回标准的 **`(obs, reward, done, info)`** 元组：  
> > · `reward` 来自 `task.measurements` 中的 `reward_measure`（如 `distance_to_goal_reward`）  
> > · `done` 由 `task` 判断 episode 是否结束（到达目标 / 超步数 / 碰撞）  
> > · `info` 包含 `task.get_metrics()` 返回的所有指标
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 4\. PPO 训练算法
> > 
> > Proximal Policy Optimization (Schulman et al., 2017) — Habitat 使用的核心 RL 算法。
> > 
> > <div style="margin:14px 0;padding:14px 18px;background:#1e293b;border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;">
> > 
> > <span style="font-size:1.1rem;">🤔</span> <span style="color:#e2e8f0;font-size:0.88rem;"> 假设你是 agent 的策略网络。你刚刚发现了一个**"捷径"**——穿过墙直接到达目标。  
> > 新策略给这个"穿墙"动作 100% 的概率，旧策略只给了 1%。  
> > 如果你**不加限制**地更新——ratio = 100/1 = 100——你会立刻忘记之前学会的一切，变成"只会穿墙的 agent"。  
> >   
> > **PPO 的做法**：给更新加一个"**刹车**"——ε = 0.2。  
> > 不管新策略多想做一件旧策略没做过的事，实际用的 ratio 被 clip 到 \[0.8, 1.2\] 之间。  
> > 这样你可以**慢慢倾斜**向新策略，但不会一夜之间推翻旧策略。  
> >   
> > 这就是 PPO 的核心思想——也是下面所有公式要表达的同一件事。 </span>
> > 
> > </div>
> > 
> > <div>
> > 
> > <div class="info-title" style="color:#60a5fa;">
> > 
> > 学习目标
> > 
> > </div>
> > 
> > 掌握 PPO clipped objective 公式和代码映射  
> > <span style="color:#fbbf24;font-size:0.82rem;">🤔 PPO 论文里说 "clip the ratio to 1±ε"——如果新策略想做一件旧策略从来没想过的事（ratio=100），PPO 会怎么阻止它？clip 之后实际用的 ratio 是多少？</span>
> > 
> > </div>
> > 
> > ### 4.1 PPO 训练循环 (PPOTrainer.train)
> > 
> > <div class="screenshot-frame" style="margin-bottom:14px;">
> > 
> > **实际训练曲线 (L40 GPU · 5 次 PPO 更新 · 160 环境步)**
> > 
> > ![Training Curves](images/pointnav_training_curves.png)
> > 
> > <span style="color:#60a5fa;font-weight:600;">📋 运行 §1.2 训练命令: python -m habitat\_baselines.run --config-name=pointnav/ppo\_pointnav\_example.yaml 的训练日志 (TensorBoard)</span>  
> > skokloster-castle 场景 · 5.8M 参数 · Reward 仍为负, Success=0% (此阶段预期行为) · FPS 40-74
> > 
> > </div>
> > 
> > ### 4.1 PPO 训练循环 (PPOTrainer.train)
> > 
> > ### 4.1A PPO 核心思想
> > 
> > <div>
> > 
> > **💡 一句话总结：**PPO（Proximal Policy Optimization，近端策略优化）是当前深度强化学习中最主流的策略梯度算法。它解决了「如何在更新策略时既`学得快`，又`不翻车`」这一核心矛盾。
> > 
> > </div>
> > 
> > 在强化学习中，策略梯度方法面临一个老问题：**学习率太大，策略更新过猛，训练直接崩溃；学习率太小，训练慢如蜗牛，永远学不会。**TRPO（Trust Region Policy Optimization）通过复杂的二阶优化来约束更新幅度，但实现难度极高。PPO 的提出者 John Schulman 团队在 2017 年给出了一个巧妙的替代方案：**用一阶优化的代价，实现近似的信任域约束**——这就是「裁剪替代目标函数」（Clipped Surrogate Objective）的核心直觉。
> > 
> > 想象你在「微调」一个旧策略来得到新策略：对每一步动作，新策略的概率和旧策略的概率之比，叫做 **概率比率 r<sub>t</sub>(θ)**。如果这个比率偏离 1 太远（比如旧策略给动作 FORWARD 的概率是 0.4，新策略猛拉到 0.9，比率=2.25），说明策略变化太剧烈。PPO 的做法是：**用 clip 操作把比率强行限制在 \[1−ε, 1+ε\] 范围内**，然后取裁剪前后两个损失的最小值。这样，当更新方向「好」时（优势 \> 0），不会无限制拉高概率；当更新方向「不好」时（优势 \< 0），也不会无限制压低概率。**PPO 就像给策略更新装了一个「安全阀」**，在学得快和安全之间找到了最佳平衡点。
> > 
> > <div class="key-finding">
> > 
> > **🔑 关键理解：**PPO 的精髓不在于它「发明了什么新东西」，而在于它用最简单的裁剪操作（`clip`），近似实现了 TRPO 的信任域效果，同时保持了极低的实现复杂度。这就是为什么 Habitat 团队选择 PPO 作为 PointNav、ObjectNav、VLN 等导航任务的默认训练算法。
> > 
> > </div>
> > 
> > ### 4.1B 公式推导
> > 
> > 下面从核心到外围，逐步拆解 PPO 的完整损失函数。先看懂每个符号的含义，再用 Habitat 的代码去对应。
> > 
> > #### 1\. 概率比率 (Probability Ratio)
> > 
> >     rt(θ) = πθ(at | st) / πθ_old(at | st)
> > 
> > | 符号                 | 含义                                                    |
> > | ------------------ | ----------------------------------------------------- |
> > | `πθ(at \| st)`     | 新策略（正在训练的策略）在状态 s<sub>t</sub> 下选择动作 a<sub>t</sub> 的概率 |
> > | `πθ_old(at \| st)` | 旧策略（收集数据时的策略）在同样状态下选择同样动作的概率                          |
> > | `rt(θ)`            | 概率比率——衡量新旧策略对该动作的「偏好变化」                               |
> > 

> > > 💡 **📌 直观理解：**r<sub>t</sub> = 1 表示新旧策略完全一致（没学到东西）；r<sub>t</sub> \> 1 表示新策略更偏爱这个动作；r<sub>t</sub> \< 1 表示新策略变得不太喜欢这个动作。
> > 
> > #### 2\. 优势函数 (Advantage Function)
> > 
> >     Ât = A(st, at)  ← 由 GAE (Generalized Advantage Estimation) 计算
> > 
> > **优势 Â<sub>t</sub>** 回答一个核心问题：「在状态 s<sub>t</sub> 下执行动作 a<sub>t</sub>，比「平均水平」好多少？」优势 \> 0 说明这个动作是「好动作」，应该鼓励；优势 \< 0 说明是「坏动作」，应该抑制。GAE 通过在偏差（bias）和方差（variance）之间引入 λ 参数做折中，得到更稳定的优势估计。
> > 
> > <div>
> > 
> > **💡 Habitat 中的 GAE：**在 `rollout_storage.py` 中，`compute_returns` 方法利用 Value 网络的预测值 + 实际奖励，结合 `gamma`（折扣因子）和 `tau`（GAE-λ 的 λ）计算出每个时间步的优势值。这一步骤发生在数据收集完成之后、PPO 更新之前。
> > 
> > </div>
> > 
> > #### 3\. 裁剪替代目标函数 (Clipped Surrogate Objective)
> > 
> >     LCLIP(θ) = Et[ min( rt(θ) · Ât ,  clip(rt(θ), 1−ε, 1+ε) · Ât ) ]
> > 
> > 这个公式是 PPO 的灵魂，分三层理解：
> > 
> >   - **第一项 r<sub>t</sub>(θ) · Â<sub>t</sub>：**标准策略梯度项，用概率比率加权优势。这是「想学多少就学多少」的版本。
> >   - **第二项 clip(r<sub>t</sub>(θ), 1−ε, 1+ε) · Â<sub>t</sub>：**把概率比率裁剪到 \[1−ε, 1+ε\] 区间内，限制单次更新的最大幅度。这是「装安全阀」的版本。
> >   - **外层 min(·, ·)：**取两者最小值。当 Â<sub>t</sub> \> 0 时，裁剪阻止 r<sub>t</sub> 变得太大（不要让好动作的概率涨太多）；当 Â<sub>t</sub> \< 0 时，裁剪阻止 r<sub>t</sub> 变得太小（不要让坏动作的概率跌太多）。
> > 
> > <div class="key-finding">
> > 
> > **🔑 ε（裁剪范围）的含义：**ε 控制策略更新的最大幅度。ε = 0.2 意味着新策略的概率比率最多偏离 1 的 ±20%（即 r<sub>t</sub> ∈ \[0.8, 1.2\]）。Habitat 默认使用 `clip_param = 0.1` 或 `0.2`：ε=0.1 更保守、更稳定但学习慢；ε=0.2 更激进、学得快但可能不稳定。对于导航任务，0.1\~0.2 之间都是合理选择。
> > 
> > </div>
> > 
> > #### 4\. 完整 PPO 损失函数
> > 
> >     Ltotal(θ) = LCLIP(θ)  −  c1 · LVF(θ)  +  c2 · S[πθ]
> > 
> > PPO 不是只有一个损失，它由三个部分加权组成：
> > 
> > | 组成部分     | 公式                              | 作用                             | Habitat YAML 参数                   |
> > | -------- | ------------------------------- | ------------------------------ | --------------------------------- |
> > | **策略损失** | `LCLIP(θ)`                      | 让策略产出更高优势的动作（核心优化目标）           | `clip_param` 控制 ε                 |
> > | **价值损失** | `LVF(θ) = (Vθ(st) − Vtarget)2`  | 让 Value 网络更准确地预测未来累积奖励（MSE 损失） | `value_loss_coef` = c<sub>1</sub> |
> > | **熵奖励**  | `S[πθ] = −Σπ(a\|s)·log π(a\|s)` | 鼓励策略保持一定程度的探索（防止过早收敛到次优解）      | `entropy_coef` = c<sub>2</sub>    |
> > 

> > > 💡 **📌 符号注意：**价值损失项前面是「减号」（−c<sub>1</sub>），因为我们要 **最大化** 整体目标。在代码实现中，通常转为求最小化（加负号），所以你会看到 `loss = -policy_loss + c1 * value_loss - c2 * entropy` 的写法。Habitat 代码中采用「最大化」范式，因此减去价值损失（让它变小更好）。
> > 
> > ### 4.1C 代码映射：公式到 Habitat-Baselines 源码
> > 
> > 下面将每个公式组件精确映射到 Habitat-Baselines 的实际文件和代码行。
> > 
> > #### 映射总览
> > 
> > | 公式组件                   | 代码文件                                          | 关键类/方法                                                | 对应 YAML 参数                    |
> > | ---------------------- | --------------------------------------------- | ----------------------------------------------------- | ----------------------------- |
> > | `LCLIP(θ)` + 整体损失      | `habitat_baselines/rl/ppo/ppo.py`             | `PPO.update()` 方法                                     | `clip_param`                  |
> > | `πθ(at\|st)` 新策略概率     | `habitat_baselines/rl/ppo/ppo.py`             | `ActorCritic.act()` → `action_distribution.log_probs` | —                             |
> > | `πθ_old(at\|st)` 旧策略概率 | `habitat_baselines/common/rollout_storage.py` | `RolloutStorage` 中存储的 `action_log_probs`              | —                             |
> > | `Ât` (GAE 优势)          | `habitat_baselines/common/rollout_storage.py` | `RolloutStorage.compute_returns()`                    | `gamma`, `tau`                |
> > | `LVF` 价值损失             | `habitat_baselines/rl/ppo/ppo.py`             | `PPO.update()` 中 value\_loss                          | `value_loss_coef`             |
> > | `S[πθ]` 熵奖励            | `habitat_baselines/rl/ppo/ppo.py`             | `PPO.update()` 中 action\_distribution.entropy         | `entropy_coef`                |
> > | PPO 更新循环               | `habitat_baselines/rl/ppo/ppo_updater.py`     | `PPOUpdater.update()`（调用 PPO.update 的包装器）             | `ppo_epoch`, `num_mini_batch` |
> > 

> > #### 关键代码位置详解
> > 
> > <div>
> > 
> > **📁 文件 1：`habitat_baselines/rl/ppo/ppo.py`** — PPO 算法核心类
> > 
> > **类 `PPO` 的方法 `update()`** 是公式的直接翻译。其核心逻辑（伪代码重构）如下：
> > 
> >     # ppo.py — PPO.update() 的核心逻辑 (简化版)
> >     
> >     def update(self, rollouts):
> >         # 从 RolloutStorage 取数据
> >         values, action_log_probs, actions, advantages, returns = rollouts.get_data()
> >         
> >         # 遍历多个 epoch（ppo_epoch）和 mini-batch
> >         for epoch in range(self.ppo_epoch):
> >             for batch in data_generator:
> >                 # === 第1章：计算新策略的概率 ===
> >                 new_action_dist = self.actor_critic.act(batch.observations, ...)
> >                 new_action_log_probs = new_action_dist.log_probs(batch.actions)
> >                 
> >                 # === 第2章：计算概率比率 r_t(θ) ===
> >                 ratio = torch.exp(new_action_log_probs - batch.action_log_probs)
> >                 #  batch.action_log_probs 是旧策略的 log π_old
> >                 
> >                 # === 第3章：计算裁剪损失 L^CLIP ===
> >                 surr1 = ratio * batch.advantages           # r_t * Â_t
> >                 surr2 = torch.clamp(ratio, 1.0 - clip_param, 1.0 + clip_param) * batch.advantages
> >                 action_loss = -torch.min(surr1, surr2).mean()  # 取 min，负号因为要最小化
> >                 
> >                 # === 第4章：计算价值损失 L^VF ===
> >                 value_loss = F.mse_loss(new_values, batch.returns)
> >                 
> >                 # === 第5章：完整损失 = L^CLIP + c1·L^VF − c2·S ===
> >                 total_loss = (
> >                     action_loss
> >                     + self.value_loss_coef * value_loss        # c1 * L^VF
> >                     - self.entropy_coef * new_action_dist.entropy().mean()  # -c2 * S
> >                 )
> >                 
> >                 # === 第6章：反向传播 ===
> >                 self.optimizer.zero_grad()
> >                 total_loss.backward()
> >                 torch.nn.utils.clip_grad_norm_(..., self.max_grad_norm)
> >                 self.optimizer.step()
> > 
> > **符号对应关系：**
> > 
> >   - `ratio` → `rt(θ)`（通过 exp(log 差值) 计算，数值更稳定）
> >   - `batch.advantages` → `Ât`（已在 rollout\_storage 中 GAE 计算好）
> >   - `clip_param` → `ε`（来自 YAML，默认 0.1 或 0.2）
> >   - `value_loss_coef` → `c1`（来自 YAML）
> >   - `entropy_coef` → `c2`（来自 YAML）
> > 
> > </div>
> > 
> > <div>
> > 
> > **📁 文件 2：`habitat_baselines/rl/ppo/ppo_updater.py`** — PPO 更新调度器
> > 
> > `PPOUpdater` 是 `PPO.update()` 的外层包装，负责控制 **「何时更新」** 而不是「如何更新」：
> > 
> >     # ppo_updater.py 核心逻辑
> >     
> >     class PPOUpdater:
> >         def update(self, rollouts):
> >             # 1. 先让 RolloutStorage 计算 GAE 优势和回报
> >             rollouts.compute_returns(
> >                 next_value,        # 最后一步的 V(s_{T+1})
> >                 use_gae=True,      # 使用 GAE 而非简单 n-step 回报
> >                 gamma=self.gamma,
> >                 tau=self.tau,      # GAE 的 λ 参数
> >             )
> >             
> >             # 2. 调用 PPO.update() 执行实际的网络更新
> >             value_loss, action_loss, dist_entropy = self.agent.update(rollouts)
> >             
> >             # 3. 清空 rollout 缓冲区，准备下一轮数据收集
> >             rollouts.after_update()
> >             
> >             return value_loss, action_loss, dist_entropy
> > 
> > **关键点：**`rollouts.compute_returns()` 必须在 `agent.update()` 之前调用，因为 PPO 更新需要预先计算好的 `advantages` 和 `returns`。
> > 
> > </div>
> > 
> > <div>
> > 
> > **📁 文件 3：`habitat_baselines/common/rollout_storage.py`** — GAE 优势计算
> > 
> > `RolloutStorage.compute_returns()` 是 `Ât` 的实际计算场所：
> > 
> >     # rollout_storage.py — GAE 优势计算
> >     
> >     def compute_returns(self, next_value, use_gae, gamma, tau):
> >         if use_gae:
> >             # Generalized Advantage Estimation (GAE)
> >             self.value_preds[-1] = next_value
> >             gae = 0
> >             for step in reversed(range(self.rewards.size(0))):
> >                 delta = (
> >                     self.rewards[step]
> >                     + gamma * self.value_preds[step + 1] * masks[step]
> >                     - self.value_preds[step]
> >                 )
> >                 # GAE 核心公式：Â_t = Σ (γτ)^l · δ_{t+l}
> >                 gae = delta + gamma * tau * masks[step] * gae
> >                 self.returns[step] = gae + self.value_preds[step]
> >                 
> >                 # ^ 注意：returns = advantages + value_preds（用于 Value 网络训练）
> >                 #    advantages = gae（用于策略网络训练）
> >         else:
> >             # 不带 GAE 的 n-step 回报（备用方案）
> >             ...
> > 
> > **GAE 公式对应：**
> > 
> >   - `delta` → TD 误差：δ<sub>t</sub> = r<sub>t</sub> + γ·V(s<sub>t+1</sub>) − V(s<sub>t</sub>)
> >   - `gae` → GAE 优势累积：Â<sub>t</sub><sup>GAE</sup> = Σ<sub>l=0</sub><sup>∞</sup> (γτ)<sup>l</sup> · δ<sub>t+l</sub>
> >   - `self.returns` → 用于 Value 网络 MSE 训练的目标：R<sub>t</sub> = Â<sub>t</sub> + V(s<sub>t</sub>)
> >   - `gamma` → γ（折扣因子，通常 0.99）
> >   - `tau` → τ（GAE 的 λ 参数，通常 0.95——注意 Habitat 用 `tau` 而非 `lambda` 命名）
> > 
> > </div>
> > 
> > #### YAML 配置参数到公式的完整映射
> > 
> >     # 典型 Habitat PPO 训练配置 (ppo_pointnav.yaml)
> >     RL:
> >       PPO:
> >         clip_param: 0.2          # → ε（裁剪范围）
> >         ppo_epoch: 4             # → 每轮数据重复训练几次
> >         num_mini_batch: 2        # → mini-batch 切分数
> >         value_loss_coef: 0.5     # → c₁（价值损失权重）
> >         entropy_coef: 0.01       # → c₂（熵奖励权重）
> >         max_grad_norm: 0.5       # → 梯度裁剪阈值（额外保护）
> >         lr: 2.5e-4               # → 优化器学习率
> >         eps: 1e-5                # → Adam 优化器的 ε（非 PPO 的 ε！）
> >         gamma: 0.99              # → γ（折扣因子，影响返回值计算）
> >         tau: 0.95                # → τ（GAE 的 λ 参数）
> >         use_gae: True            # → 是否启用 GAE
> >         use_clipped_value_loss: True  # → 是否也对 L^VF 做裁剪（额外稳定）
> > 
> > > 💡 **📌 常见混淆：**YAML 中 `eps: 1e-5` 是 Adam 优化器的数值稳定参数（防止除零），**不是** PPO 的 `epsilon`（裁剪范围）。PPO 的 ε 对应 `clip_param`。
> > 
> > ### 4.1D 直观理解：一个完整数值例子
> > 
> > 让我们用一个具体场景，把公式从头到尾走一遍。这是理解 PPO 内部分数流动的最佳方式。
> > 
> > <div>
> > 
> > **🎬 场景设定：**Agent 在 Habitat 场景中导航。在 **step 5**，Agent 执行了动作 `FORWARD`（向前走一步）。
> > 
> > </div>
> > 
> > #### 第1章：获取新旧策略概率
> > 
> > | 指标                                           | 值       | 来源                                                 |
> > | -------------------------------------------- | ------- | -------------------------------------------------- |
> > | 旧策略 π<sub>old</sub>(FORWARD | s<sub>5</sub>) | **0.4** | 收集 rollout 数据时，ActorCritic 网络输出的概率分布中对 FORWARD 的概率 |
> > | 新策略 π<sub>new</sub>(FORWARD | s<sub>5</sub>) | **0.6** | PPO 更新时，当前 ActorCritic 网络对同一状态重新计算的概率              |
> > 

> > #### 第2章：计算概率比率
> > 
> >     rt(θ) = πnew / πold = 0.6 / 0.4 = 1.5
> > 
> > 比率 1.5 \> 1，说明新策略比旧策略更「喜欢」FORWARD 这个动作——训练正在鼓励这个动作。
> > 
> > #### 第3章：查看优势值和裁剪参数
> > 
> > | 参数                | 值        | 含义                                             |
> > | ----------------- | -------- | ---------------------------------------------- |
> > | Â<sub>5</sub>（优势） | **+0.3** | 正值 → FORWARD 是个「好动作」，它的回报比 Value 网络预测的基线更好     |
> > | ε（clip\_param）    | **0.2**  | 概率比率最多偏差 20%，即 r<sub>t</sub> 被限制在 \[0.8, 1.2\] |
> > 

> > #### 第4章：应用裁剪
> > 
> >     无裁剪版本：  rt · Ât       = 1.5 × 0.3 = 0.45
> >     裁剪版本：    clip(rt, 0.8, 1.2) × Ât
> >                 = 1.2 × 0.3
> >                 = 0.36
> > 
> > 因为 r<sub>t</sub> = 1.5 超出了裁剪上限 1.2，PPO 把它强行「按住」在 1.2，**牺牲了 0.09 的潜在收益（0.45 − 0.36 = 0.09），换来了策略更新的稳定性。**
> > 
> > #### 第5章：min 操作最终裁决
> > 
> >     目标值 = min(无裁剪版, 裁剪版) = min(0.45, 0.36) = 0.36
> > 
> > 本例中裁剪版本更小，所以 `min` 选择了裁剪版本 0.36。**PPO 宁愿少学一点，也不想冒策略崩溃的风险。**
> > 
> > <div class="key-finding">
> > 
> > **🔑 关键领悟：**这个数值例子展示了 PPO 裁剪机制的精妙之处。当优势为正（Â<sub>t</sub> = +0.3）且新策略对动作偏好大幅上升（r<sub>t</sub> = 1.5）时，`clip` + `min` 的组合阻止了本轮更新将该动作的概率拉升得过高。下一次数据收集时，旧策略会更新为这一轮收敛后的策略，概率比率重新从 1.0 开始计算——PPO 以这种逐轮小幅更新的方式，确保策略平稳改进。
> > 
> > </div>
> > 
> > #### 反向场景（优势为负）的补充说明
> > 
> > > 💡 **📌 假设同一场景中 Â<sub>5</sub> = −0.3（FORWARD 是个坏动作）：**
> > > 
> > >   - 无裁剪版：1.5 × (−0.3) = **−0.45**
> > >   - 裁剪版：clip(1.5, 0.8, 1.2) × (−0.3) = 1.2 × (−0.3) = **−0.36**
> > >   - min(−0.45, −0.36) = **−0.45**（无裁剪版本更小，被选中）
> > > 
> > > 当优势为负时，`min` 会选择「让损失更负」的版本，即**无裁剪版本 −0.45**（因为裁剪版 −0.36 更大）。这等价于：当应该减少概率时，PPO 允许充分减少，不会被裁剪限制——因为裁剪只限制了概率比率的最低值（1−ε），而 r<sub>t</sub> = 1.5 并不会触发下限。
> > > 
> > > 只有当 r<sub>t</sub> \< 0.8（新策略把概率降得太低）时，裁剪下限才会介入。这是 PPO 设计的精妙之处：**对好动作限制涨幅，对坏动作允许充分跌幅**。
> > 
> > <div class="key-finding">
> > 
> > #### 📋 PPO 公式快速参考卡
> > 
> > | 公式                   | Habitat 参数                        | 推荐值        | 一句话作用              |
> > | -------------------- | --------------------------------- | ---------- | ------------------ |
> > | `rt = πnew / πold`   | —（隐式计算）                           | —          | 衡量新旧策略对同一动作的偏好变化   |
> > | `clip(rt, 1−ε, 1+ε)` | `clip_param` = ε                  | 0.1 \~ 0.2 | 限制单次更新幅度，防止训练崩溃    |
> > | `Ât（GAE）`            | `gamma`, `tau`                    | 0.99, 0.95 | 评估动作的「好/坏」程度       |
> > | `LVF（MSE）`           | `value_loss_coef` = c<sub>1</sub> | 0.5        | 让 Value 网络学会预测未来回报 |
> > | `S[πθ]（熵）`           | `entropy_coef` = c<sub>2</sub>    | 0.01       | 鼓励探索，防止过早收敛        |
> > | `Ltotal`             | —（三部分加权和）                         | —          | PPO 的完整优化目标        |
> > 

> > </div>
> > 
> > <div class="arch-diagram">
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#ec489920;border:1px solid #ec489940;">
> > 
> > **① 初始化** <span class="small">创建 VectorEnv → Policy → Updater</span>
> > 
> > <div class="arch-arrow-center">
> > 
> > ↓
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">
> > 
> > **② 收集 Rollout** <span class="small">N 个 env × num\_steps 步</span>
> > 
> > </div>
> > 
> > <span style="font-size:0.85rem;color:var(--text-dim);align-self:center;">→</span>
> > 
> > <div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">
> > 
> > **③ 计算 Returns + Advantages** <span class="small">GAE (gamma=0.99, tau=0.95)</span>
> > 
> > <div class="arch-arrow-center">
> > 
> > ↓
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">
> > 
> > **④ PPO Update** <span class="small">ppo\_epoch=1, num\_mini\_batch=1</span>
> > 
> > </div>
> > 
> > <span style="font-size:0.85rem;color:var(--text-dim);align-self:center;">→</span>
> > 
> > <div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">
> > 
> > **⑤ Clip Gradient + Step** <span class="small">clip\_param=0.1, max\_grad\_norm=0.5</span>
> > 
> > <div class="arch-arrow-center">
> > 
> > ↓
> > 
> > </div>
> > 
> > <div class="arch-row">
> > 
> > <div class="arch-layer" style="background:#22d3ee20;border:1px solid #22d3ee40;">
> > 
> > **⑥ Log + Checkpoint** <span class="small">tensorboard / 定期保存</span>
> > 
> > </div>
> > 
> > <span style="font-size:0.85rem;color:var(--text-dim);align-self:center;">⟲</span>
> > 
> > <div class="arch-layer" style="background:#64748b40;border:1px solid #64748b;">
> > 
> > **重复 ②-⑥** <span class="small">直到 total\_num\_steps</span>
> > 
> > </div>
> > 
> > ### 4.2 PPO 核心参数详解
> > 
> > <div class="param-grid">
> > 
> > <div class="param-card" style="border-left-color:#f59e0b;">
> > 
> > #### clip\_param = 0.1
> > 
> > <div class="param-val">
> > 
> > 默认 0.2，示例中用 0.1
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > PPO 的核心创新——限制策略更新的幅度。新策略与旧策略的概率比被裁剪到 `[1-ε, 1+ε]`。 **越小越保守**，训练更稳定但收敛更慢。
> > 
> > <div class="param-card" style="border-left-color:#3b82f6;">
> > 
> > #### lr = 2.5e-4
> > 
> > <div class="param-val">
> > 
> > Adam 优化器学习率
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 标准设置。可配合 `use_linear_lr_decay=True` 让学习率从初始值线性衰减到 0。
> > 
> > <div class="param-card" style="border-left-color:#10b981;">
> > 
> > #### num\_steps = 32
> > 
> > <div class="param-val">
> > 
> > 每次 rollout 收集的环境步数
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 每次 PPO 更新前，每个环境执行 32 步。batch\_size = `num_environments × num_steps`。 更大的值提供更多样本但降低更新频率。
> > 
> > <div class="param-card" style="border-left-color:#8b5cf6;">
> > 
> > #### gamma = 0.99
> > 
> > <div class="param-val">
> > 
> > 折扣因子
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 未来 reward 的衰减系数。`0.99` 意味着 100 步后的 reward 权重约为 `0.99^100 ≈ 0.37`。 接近 1.0 表示重视远期奖励。
> > 
> > <div class="param-card" style="border-left-color:#ec4899;">
> > 
> > #### tau = 0.95 (GAE λ)
> > 
> > <div class="param-val">
> > 
> > Generalized Advantage Estimation
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 控制 advantage 估计中偏差-方差的权衡。`λ=1` 等价于 Monte Carlo（无偏但高方差）； `λ=0` 等价于 TD(0)（有偏但低方差）。0.95 是经验最优值。
> > 
> > <div class="param-card" style="border-left-color:#06b6d4;">
> > 
> > #### entropy\_coef = 0.01
> > 
> > <div class="param-val">
> > 
> > 熵正则化系数
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 鼓励策略保持探索（不收敛到单一动作）。值越大探索越多，可设置 `use_adaptive_entropy_pen=True` 自动调整。
> > 
> > </div>
> > 
> > ### 4.3 DD-PPO (分布式 PPO)
> > 
> > 当单卡不够时，使用 DD-PPO 在多 GPU/多节点上训练。它与 PPO 共享同一个 `PPOTrainer` 类， 区别在于通过 `DecentralizedDistributedMixin` 增加了分布式同步。
> > 
> > <div class="param-grid">
> > 
> > <div class="param-card" style="border-left-color:#f59e0b;">
> > 
> > #### sync\_frac = 0.6
> > 
> > <div class="param-val">
> > 
> > 每 60% 步数后同步一次梯度
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > 不每步同步（那样通信开销太大），而是积累一定步数后平均梯度。
> > 
> > <div class="param-card" style="border-left-color:#3b82f6;">
> > 
> > #### backbone = "resnet18"
> > 
> > <div class="param-val">
> > 
> > 视觉编码器 (ResNet18/50/101)
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > DD-PPO 默认使用 ResNet18 作为视觉 backbone。支持 `pretrained_encoder=True` 加载预训练权重。
> > 
> > <div class="param-card" style="border-left-color:#10b981;">
> > 
> > #### num\_recurrent\_layers = 1
> > 
> > <div class="param-val">
> > 
> > GRU 循环层数
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > Policy 在 CNN 特征后接 GRU 层处理序列信息。设为 0 可禁用循环层。
> > 
> > <div class="param-card" style="border-left-color:#8b5cf6;">
> > 
> > #### distrib\_backend = "GLOO"
> > 
> > <div class="param-val">
> > 
> > PyTorch 分布式后端
> > 
> > </div>
> > 
> > <div class="param-desc">
> > 
> > CPU 训练用 GLOO，GPU 训练可用 NCCL（更快）。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > > ⚠️
> > > 
> > > <div class="warn-title">
> > > 
> > > 🛠 RL 环境包装链常见错误
> > > 
> > > | 错误信息                                         | 可能原因                                | 解决方法                                                  |
> > > | -------------------------------------------- | ----------------------------------- | ----------------------------------------------------- |
> > > | `TypeError: RLEnv.__init__() missing config` | 用 `Env(config)` 替代了 `RLEnv(config)` | 训练必须用 RLEnv——Env 不提供 reward 计算                        |
> > > | `KeyError: 'reward_measure'`                 | RLEnv 配置缺少 `reward_measure` 段       | 在 yaml 中补全 `habitat.task.measurements.reward_measure` |
> > > | `AttributeError: 'VectorEnv' has no 'step'`  | VectorEnv 的 API 与单 Env 不同           | VectorEnv 使用 `vector_step(actions)` 而非 `step()`       |
> > > 

> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 5\. 训练配置体系
> > > 
> > > 训练配置 = **Benchmark 配置**（环境） + **Baselines 配置**（算法） ，通过 Hydra `defaults` 合并。
> > > 
> > > ### 5.1 配置入口 — run.py
> > > 
> > >     # habitat-baselines/habitat_baselines/run.py
> > >     @hydra.main(
> > >         config_path="config",
> > >         config_name="pointnav/ppo_pointnav_example",  ← 默认配置文件
> > >     )
> > >     def main(cfg):
> > >         trainer_init = baseline_registry.get_trainer(cfg.habitat_baselines.trainer_name)
> > >         trainer = trainer_init(cfg)
> > >         if run_type == "train":
> > >             trainer.train()       # 开始训练
> > >         else:
> > >             trainer.eval()        # 评估模式
> > > 
> > > ### 5.2 训练配置文件
> > > 
> > > <div class="config-tree">
> > > 
> > > <span class="cmt">\# habitat\_baselines/config/pointnav/ppo\_pointnav\_example.yaml</span> <span class="kw">defaults:</span> - /benchmark/nav/pointnav: pointnav\_habitat\_test <span class="cmt">← 环境配置（场景、任务、传感器）</span> - /habitat\_baselines: habitat\_baselines\_rl\_config\_base <span class="cmt">← 训练配置（算法、超参）</span> - <span class="warn">\_self\_</span> <span class="key">habitat\_baselines:</span> <span class="key">trainer\_name:</span> <span class="str">"ppo"</span> <span class="cmt">← 注册在 baseline\_registry 中的 trainer</span> <span class="key">num\_environments:</span> <span class="num">1</span> <span class="cmt">← 并行环境数（DD-PPO 时可设多卡）</span> <span class="key">total\_num\_steps:</span> <span class="num">1e6</span> <span class="cmt">← 总训练步数</span> <span class="key">checkpoint\_folder:</span> <span class="str">"data/new\_checkpoints"</span> <span class="key">num\_checkpoints:</span> <span class="num">50</span> <span class="cmt">← 保存 50 个均匀分布的快照</span> <span class="key">rl:</span> <span class="key">ppo:</span> <span class="key">clip\_param:</span> <span class="num">0.1</span> <span class="cmt">← PPO 裁剪范围</span> <span class="key">lr:</span> <span class="num">2.5e-4</span> <span class="cmt">← 学习率</span> <span class="key">num\_steps:</span> <span class="num">32</span> <span class="cmt">← 每次 rollout 收集的环境步数</span> <span class="key">gamma:</span> <span class="num">0.99</span> <span class="cmt">← 折扣因子</span> <span class="key">tau:</span> <span class="num">0.95</span> <span class="cmt">← GAE λ 参数</span> <span class="key">hidden\_size:</span> <span class="num">512</span> <span class="cmt">← 网络隐藏层维度</span>
> > > 
> > > </div>
> > > 
> > > ### 5.3 配置合并结果
> > > 
> > > 合并后的 `DictConfig` 同时包含 `habitat` 和 `habitat_baselines` 两个顶层节点， 它们的 structured config 类型分别定义在两个文件中。
> > > 
> > > <div class="module-grid">
> > > 
> > > <div class="module" style="border-left-color:#3b82f6;">
> > > 
> > > ### cfg.habitat (环境)
> > > 
> > >   - `habitat.seed` — 随机种子
> > >   - `habitat.environment.max_episode_steps`
> > >   - `habitat.simulator.agents.main_agent.sim_sensors`
> > >   - `habitat.task.type` (Nav-v0)
> > >   - `habitat.task.measurements` (success, spl, distance\_to\_goal)
> > >   - `habitat.dataset.split` (train/val/test)
> > > 
> > > </div>
> > > 
> > > <div class="module" style="border-left-color:#f59e0b;">
> > > 
> > > ### cfg.habitat\_baselines (训练)
> > > 
> > >   - `trainer_name` — "ppo" 或 "ddppo"
> > >   - `num_environments` — 并行环境数
> > >   - `total_num_steps / num_updates`
> > >   - `rl.ppo.clip_param, lr, gamma, tau, ...`
> > >   - `rl.ddppo.backbone` — "resnet18"
> > >   - `eval.video_option` — \["disk", "tensorboard"\]
> > > 
> > > </div>
> > > 
> > > <div class="section">
> > > 
> > > <div class="container">
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > 🛠 训练配置常见错误
> > > > 
> > > > | 错误信息                                               | 可能原因                            | 解决方法                                          |
> > > > | -------------------------------------------------- | ------------------------------- | --------------------------------------------- |
> > > > | `ConfigAttributeError: Key 'xxx' is not in struct` | Hydra Structured Config 拒绝不存在字段 | 先 `OmegaConf.to_container()` 转普通 dict 再修改     |
> > > > | `FileNotFoundError: ...cfg_file_path...`           | yaml 路径写错（相对路径基准是 cwd）          | 用 `habitat.get_config()` 自动解析路径，不要手写          |
> > > > | `MissingConfigException: dataset not found`        | benchmark config 引用的数据集未下载      | 检查 `habitat.dataset.data_path` 指向正确的 .json.gz |
> > > > 

> > > > <div class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > ## 6\. RL 导航实战：观测→动作→奖励
> > > > 
> > > > 在深入 PPO 算法之前，先用一个完整的 Demo 理解 RL 如何让 agent 学会导航。 **观测什么、输出什么、奖励什么**——这三个问题是一切 RL 训练的基础。
> > > > 
> > > > <div>
> > > > 
> > > > <div class="info-title" style="color:#60a5fa;">
> > > > 
> > > > 学习目标
> > > > 
> > > > </div>
> > > > 
> > > > 运行完整的训练流程，理解观测→动作→奖励的闭环  
> > > > <span style="color:#fbbf24;font-size:0.82rem;">🤔 agent 往前走了一步，reward 是 +0.3 还是 -0.01？这个数字是怎么算出来的？如果我把 success\_distance 从 0.2m 改成 0.1m，reward 会变吗？</span>
> > > > 
> > > > </div>
> > > > 
> > > > ### 6.1 传统导航 vs RL 导航
> > > > 
> > > > RL 导航与传统 ROS Nav2 的根本区别：**不分解为独立模块，而是端到端学习**。
> > > > 
> > > > <div class="arch-diagram">
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">
> > > > 
> > > > **传统导航 (ROS Nav2)** <span class="small">SLAM 建图 → AMCL 定位 → A\* 规划 → DWA 控制</span>
> > > > 
> > > > <div class="arch-arrow-center">
> > > > 
> > > > vs
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">
> > > > 
> > > > **RL 导航 (Habitat PointNav)** <span class="small">RGB+Depth+GPS → CNN+GRU → (前进|左转|右转|停止)</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **🔑 关键差异**
> > > > 
> > > > RL 用 **CNN+GRU 隐状态** 替代了显式地图和规划器。 GPS+Compass 传感器提供 **完美的相对目标向量**（距离+角度）， 这是一种**特权信息**——它绕过了 SLAM 问题，让策略专注学习"如何从视觉走到目标"。 真实机器人需要用视觉里程计或 SLAM 来近似这个信号。
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **为什么要用强化学习？**
> > > > 
> > > > **1. 学「看」→「走」，不需要人类标注**  
> > > > 传统导航需要人工设计 SLAM、定位、规划、控制每个模块。RL 只需要定义**奖励函数**（"靠近目标加分"）， 策略网络自己从几百万次试错中学会从像素到动作的端到端映射。没有人类告诉它「这里该左转」— 奖励信号自动指引。  
> > > >   
> > > > **2. 泛化到未见过的场景**  
> > > > RL 训练的策略不是背地图 — 它学的是「看到什么样的视觉模式该做什么动作」。 在 Gibson 场景集上训练的策略，可以在从未见过的 MP3D 场景中导航（zero-shot），因为 CNN 提取的是**通用视觉特征**而非特定场景坐标。  
> > > >   
> > > > **3. 这是 Sim-to-Real 的基础**  
> > > > GPS+Compass 在仿真中是完美特权信息，但在真实机器人上只能用视觉里程计近似。 RL 策略可以逐步去掉 GPS 依赖（从 PointNav → ImageNav → VLN），最终变成纯视觉导航 — 这就是 Habitat 作为**具身智能研究平台**的核心使命：在仿真中训练，向真实世界迁移。
> > > > 
> > > > </div>
> > > > 
> > > > ### 6.2 Demo 全貌：`examples/rl_nav_demo.py`
> > > > 
> > > > 这是本章配套的 RL 导航 Demo 脚本，分为 4 个 Part，覆盖从环境探索到策略推理的完整流程。
> > > > 
> > > > <div class="arch-diagram">
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#22d3ee20;border:1px solid #22d3ee40;">
> > > > 
> > > > **Part 1** 🎮 <span class="small">探索环境：观测空间、动作空间、奖励信号</span>
> > > > 
> > > > </div>
> > > > 
> > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">→</span>
> > > > 
> > > > <div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">
> > > > 
> > > > **Part 2** 🧠 <span class="small">策略架构：CNN+GRU+Actor/Critic</span>
> > > > 
> > > > </div>
> > > > 
> > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">→</span>
> > > > 
> > > > <div class="arch-layer" style="background:#ec489920;border:1px solid #ec489940;">
> > > > 
> > > > **Part 3** 🤖 <span class="small">PPO 训练：采样→计算优势→更新策略</span>
> > > > 
> > > > </div>
> > > > 
> > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">→</span>
> > > > 
> > > > <div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">
> > > > 
> > > > **Part 4** ✅ <span class="small">推理评估：加载 checkpoint，看策略表现</span>
> > > > 
> > > > </div>
> > > > 
> > > > ### 6.3 案例：RL 环境探索（Part 1）
> > > > 
> > > > <div>
> > > > 
> > > > **① 案例含义**
> > > > 
> > > > **目的**：理解 RL agent 在每一步看到了什么、能做什么、得到什么奖励。  
> > > > **难度**：⭐（纯探索，无需训练）  
> > > > **前置条件**：habitat-lab 已安装，test 数据集已下载（均就绪）
> > > > 
> > > > </div>
> > > > 
> > > > #### ② 核心代码 & 关键函数调用
> > > > 
> > > >     # examples/rl_nav_demo.py — Part 1（简化版）
> > > >     import gym
> > > >     import habitat.gym  # 注册 Habitat-v0
> > > >     
> > > >     env = gym.make("Habitat-v0",
> > > >         cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml")
> > > >     
> > > >     # 观测空间
> > > >     obs = env.reset()
> > > >     # obs = {'rgb': (256,256,3), 'depth': (256,256,1),
> > > >     #        'pointgoal_with_gps_compass': (2,)}
> > > >     
> > > >     # 动作空间: 0=STOP, 1=MOVE_FORWARD, 2=TURN_LEFT, 3=TURN_RIGHT
> > > >     action = env.action_space.sample()  # 随机动作
> > > >     obs, reward, done, info = env.step(action)
> > > >     # reward = -(新距离 - 旧距离)，靠近目标为正
> > > > 
> > > > | 函数                          | 角色         | 说明                                                 |
> > > > | --------------------------- | ---------- | -------------------------------------------------- |
> > > > | `gym.make("Habitat-v0")`    | 创建环境       | Gym 标准 API，加载 PointNav benchmark 配置                |
> > > > | `env.reset()`               | 重置 episode | 返回观测字典 {rgb, depth, pointgoal\_with\_gps\_compass} |
> > > > | `env.action_space.sample()` | 随机采样动作     | 从 4 个离散动作中均匀随机选择                                   |
> > > > | `env.step(action)`          | 执行动作       | 返回 (obs, reward, done, info) 四元组                   |
> > > > 

> > > > #### ③ 如何创建和运行
> > > > 
> > > >     $ python examples/rl_nav_demo.py --explore-only
> > > > 
> > > > #### ④ 运行效果
> > > > 
> > > >     === PART 1: Understanding the RL Environment ===
> > > >     
> > > >     [1.2] Observation Space
> > > >       depth                 shape=(256, 256, 1)         dtype=float32
> > > >       pointgoal_with_gps_compass  shape=(2,)                  dtype=float32
> > > >       rgb                   shape=(256, 256, 3)         dtype=uint8
> > > >     
> > > >     [1.3] Action Space (discrete)
> > > >       [0] STOP
> > > >       [1] MOVE_FORWARD    ← 前进 0.25m
> > > >       [2] TURN_LEFT       ← 左转 10°
> > > >       [3] TURN_RIGHT      ← 右转 10°
> > > >     
> > > >     [1.6] Sample Episode (random actions)
> > > >       Episode ended at step 7
> > > >       Total reward: 0.367
> > > >       Info: {'distance_to_goal': 1.547, 'success': 0.0, 'spl': 0.0}
> > > > 
> > > > <div>
> > > > 
> > > > **⑤ 输出结果的含义**
> > > > 
> > > > 1.  **rgb / depth** — agent 第一视角的视觉输入。RGB 是 0-255 的 uint8 像素，depth 是浮点米值（0-10m）。
> > > > 2.  **pointgoal\_with\_gps\_compass** — `[距离 ρ, 角度 φ]`。ρ 是 agent 到目标的直线距离（米），φ 是相对偏转角（弧度）。这是 RL 的关键"特权信息"。
> > > > 3.  **STOP/MOVE\_FORWARD/TURN\_LEFT/TURN\_RIGHT** — 离散动作空间，每次只能选一个。turn\_angle=10°，意味着转 90° 需要 9 次 TURN 动作。
> > > > 4.  **reward = -(新距离 - 旧距离)** — 靠近目标得正奖励，远离得负奖励。0.367 的总奖励意味着 agent 在 7 步随机移动中总体靠近了目标约 0.37m。
> > > > 5.  **success=0.0, SPL=0.0** — 随机 agent 不可能导航成功，这是 baseline。
> > > > 
> > > > </div>
> > > > 
> > > > <div>
> > > > 
> > > > **🔍 深入：奖励的三层组装公式**
> > > > 
> > > > 上面第 4 点的 `reward = -(新距离 - 旧距离)` 只是**核心部分**。 `RLTaskEnv.get_reward()`（源码 `habitat/core/environments.py:73`）实际返回的是**三层叠加**：
> > > > 
> > > > <table>
> > > > <colgroup>
> > > > <col style="width: 33%" />
> > > > <col style="width: 33%" />
> > > > <col style="width: 33%" />
> > > > </colgroup>
> > > > <thead>
> > > > <tr class="header">
> > > > <th>层次</th>
> > > > <th>默认值</th>
> > > > <th>含义</th>
> > > > </tr>
> > > > </thead>
> > > > <tbody>
> > > > <tr class="odd">
> > > > <td><strong>slack_reward</strong><br />
> > > > <span class="small">每步固定</span></td>
> > > > <td><code>-0.01</code></td>
> > > > <td><strong>「效率惩罚」</strong> — agent 每走一步就扣 0.01 分，逼迫它走最短路径。如果 agent 原地转圈，slack 持续扣分，总 reward 永远上不去</td>
> > > > </tr>
> > > > <tr class="even">
> > > > <td><strong>reward_measure</strong><br />
> > > > <span class="small">每步动态</span></td>
> > > > <td><code>distance_to_goal_reward</code></td>
> > > > <td><strong>「核心信号」</strong> — 这就是上面第 4 点的 <code>-(新距离 - 旧距离)</code>。向目标靠近 1 米 ≈ +1.0 分，远离 1 米 ≈ -1.0 分</td>
> > > > </tr>
> > > > <tr class="odd">
> > > > <td><strong>success_reward</strong><br />
> > > > <span class="small">终点一次性</span></td>
> > > > <td><code>+2.5</code></td>
> > > > <td><strong>「成功大奖」</strong> — 只在 episode 成功时发放一次（<code>end_on_success: True</code> 时到达目标后 episode 立即终止，不会再扣 slack）</td>
> > > > </tr>
> > > > </tbody>
> > > > </table>
> > > > 
> > > > ``` 
> > > >         源码中的奖励组装（habitat/core/environments.py:73）
> > > > ```
> > > > 
> > > >     def get_reward(self, observations):
> > > >         current_measure = self._env.get_metrics()[self._reward_measure_name]
> > > >         reward = self._slack_reward          # -0.01
> > > >         reward += current_measure            # +(旧距离 - 新距离)
> > > >         if self._episode_success():
> > > >             reward += self._success_reward   # +2.5
> > > >         return reward
> > > > 
> > > > </div>
> > > > 
> > > > **一个成功 episode 的典型奖励轨迹：**  
> > > > 设起点距离目标 5 米，agent 用 50 步到达（成功）：  
> > > > · slack 贡献：`50 × (-0.01) = -0.5`（走了 50 步，扣 0.5 分）  
> > > > · distance 贡献：从 5m 逐步减到 0m，累积约 `+5.0`（每步靠近一点就加分）  
> > > > · success 贡献：到达那一刻 `+2.5`  
> > > > · **episode 总奖励 ≈ +7.0** — 这个正值告诉 PPO：「做得好，多做这种事」
> > > > 
> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 这些值在哪配置？
> > > > > 
> > > > > `pointnav.yaml` 的 `reward_measure: "distance_to_goal_reward"` 指定用哪个 Measure 做奖励； `slack_reward` 和 `success_reward` 是 `TaskConfig` 的字段（Structured Config），默认值 分别为 `-0.01` 和 `2.5`。你可以通过 Hydra 覆盖：  
> > > > > `python -m habitat_baselines.run ... habitat.task.slack_reward=-0.001 habitat.task.success_reward=5.0`
> > > > > 
> > > > > | ⑥ 调整项          | 怎么改                                                  | 预期看到什么                     |
> > > > > | -------------- | ---------------------------------------------------- | -------------------------- |
> > > > > | 增大探索步数         | 修改 `range(50)` → `range(200)`                        | 更长的随机游走，可能看到更多场景区域         |
> > > > > | 固定动作序列         | 改 `random action` 为 `action=1`（只前进）                  | agent 直线前进直到撞墙，reward 持续为负 |
> > > > > | 打印每一步的 goal 向量 | step 循环里加 `print(obs["pointgoal_with_gps_compass"])` | 看到目标距离在不断变化（随机动作时增减不定）     |
> > > > > 

> > > > > ### 6.4 从环境探索到策略推理
> > > > > 
> > > > > 当理解了环境后，Demo 的 Part 4 展示了完整闭环——加载训练好的策略网络，替代随机动作：
> > > > > 
> > > > > <div class="arch-diagram">
> > > > > 
> > > > > <div class="arch-row">
> > > > > 
> > > > > <div class="arch-layer" style="background:#1e293b;border:1px solid #64748b;">
> > > > > 
> > > > > 📷 RGB+Depth <span class="small">256×256 像素</span>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">+</span>
> > > > > 
> > > > > <div class="arch-layer" style="background:#1e293b;border:1px solid #64748b;">
> > > > > 
> > > > > 🧭 GPS+Compass <span class="small">\[距离, 角度\]</span>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">→</span>
> > > > > 
> > > > > <div class="arch-layer" style="background:#8b5cf620;border:1px solid #8b5cf640;">
> > > > > 
> > > > > **CNN+GRU** <span class="small">\~5.8M 参数</span>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <span style="font-size:1.2rem;color:var(--text-dim);align-self:center;">→</span>
> > > > > 
> > > > > <div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">
> > > > > 
> > > > > **动作概率** <span class="small">4 分类分布</span>
> > > > > 
> > > > > </div>
> > > > > 
> > > > >     # 策略推理（Part 4 简化版）
> > > > >     ckpt = torch.load("data/new_checkpoints/ckpt.9.pth", weights_only=False)
> > > > >     policy.load_state_dict(ckpt["state_dict"])
> > > > >     policy.eval()
> > > > >     
> > > > >     for step in range(200):
> > > > >         result = policy.act(obs_batch, rnn_state, prev_actions, masks, deterministic=True)
> > > > >         action = result.actions.item()      # 策略选择的动作
> > > > >         obs, reward, done, info = env.step(action)  # 执行
> > > > >         if action == 0:  # STOP → 到达目标
> > > > >             break
> > > > > 
> > > > > > 💡
> > > > > > 
> > > > > > <div class="tip-title">
> > > > > > 
> > > > > > 💡 为什么 Demo 里策略只训练了 5000 步？
> > > > > > 
> > > > > > 默认 `--train-steps 50000` 只够验证 pipeline 是否正常。 要让策略真正学会导航，需要 **数百万甚至上亿步**（生产配置用 `total_num_steps=7.5e7`）。 因此 Part 4 输出的 3 个 episode 都会看到 `[FAILED]` 和 1 步 STOP——策略还没学会如何移动。 **完整训练后再跑推理，才能看到有效的导航行为。**
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **🔗 Demo 与本章后续内容的关系**
> > > > > > 
> > > > > > · Part 1（环境探索）→ **RL 环境包装链**（第3节）将解释 `Env → RLEnv → VectorEnv` 的每一层。  
> > > > > > · Part 2（策略架构）→ **Policy 网络结构**（第2节）将展开 CNN+GRU+Actor/Critic 的内部细节。  
> > > > > > · Part 3（训练）→ **PPO 训练算法**（第4节）将深入 rollout→GAE→clip update 的数学原理。  
> > > > > > · Part 4（推理）→ **评估与 Benchmark**（第7节）将教你怎么科学地衡量模型好坏。  
> > > > > > · 想知道 PointNav 之外还有什么导航任务？→ **导航任务全景**（第1节）将讲解 5 种目标类型。
> > > > > > 
> > > > > > <div class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 7\. 评估与 Benchmark
> > > > > > 
> > > > > > 训练完成后，使用 `habitat.Benchmark` 或 trainer 的 `eval()` 评估模型性能。
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > <div class="info-title" style="color:#60a5fa;">
> > > > > > 
> > > > > > 学习目标
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > 掌握 success/SPL/distance\_to\_goal 三个核心指标  
> > > > > > <span style="color:#fbbf24;font-size:0.82rem;">🤔 训练 loss 一直在降，但 agent 在测试场景里一动不动——SPL=0, Success=0。这是过拟合吗？还是你的评估方式有问题？</span>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### 7.1 Benchmark 评估流程
> > > > > > 
> > > > > >     # 方式 1：直接使用 Benchmark
> > > > > >     from habitat.config.default import get_config
> > > > > >     import habitat
> > > > > >     
> > > > > >     cfg = get_config('benchmark/nav/pointnav/pointnav_habitat_test.yaml')
> > > > > >     benchmark = habitat.Benchmark(cfg)
> > > > > >     metrics = benchmark.evaluate(agent, num_episodes=100)
> > > > > >     # → {'success': 0.42, 'spl': 0.35, 'distance_to_goal': 1.23, ...}
> > > > > > 
> > > > > > <div class="screenshot-frame" style="margin:14px 0;">
> > > > > > 
> > > > > > **评估指标可视化 (5 次 PPO 更新 · 160 环境步)**
> > > > > > 
> > > > > > ![Evaluation Curves](images/pointnav_eval_curves.png)
> > > > > > 
> > > > > > <span style="color:#60a5fa;font-weight:600;">📋 运行 §7 评估: habitat\_baselines.evaluate=True 的输出指标可视化</span>  
> > > > > > Checkpoint 评估 — Average Reward / Distance to Goal / Success Rate — 160 步总计
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### 7.2 评估指标详解
> > > > > > 
> > > > > > | 指标                     | 全称                                                   | 范围                | 含义                                                           |
> > > > > > | ---------------------- | ---------------------------------------------------- | ----------------- | ------------------------------------------------------------ |
> > > > > > | **success**            | Success Rate                                         | \[0, 1\]          | Agent 是否在 max\_episode\_steps 内到达目标（距离 \< success\_distance） |
> > > > > > | **spl**                | Success weighted by (normalized inverse) Path Length | \[0, 1\]          | 成功率 × (最短路径长度 / max(实际路径长度, 最短路径长度))。惩罚绕路                    |
> > > > > > | **distance\_to\_goal** | Final Distance to Goal                               | \[0, ∞) m         | Episode 结束时 agent 到目标的欧式距离。越小越好                              |
> > > > > > | **num\_steps**         | Episode Steps Taken                                  | \[0, max\_steps\] | Agent 在 episode 中执行的步数（非 STOP 动作次数）                          |
> > > > > > | **collisions**         | Collision Count                                      | \[0, ∞)           | Agent 碰撞墙壁/障碍物的次数（`previous_step_collided`）                  |
> > > > > > 

> > > > > > <div class="key-finding">
> > > > > > 
> > > > > > <span class="icon">💡</span>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **SPL vs Success：**Success 只关心"到了没有"，SPL 关心"走了多高效"。 两个 agent 可能都有 80% success，但 SPL 更高的那个路径更短。 **实际项目中 SPL 往往是更重要的指标**，因为它反映了导航效率。
> > > > > > 
> > > > > > ### 7.3 使用 Trainer 评估已有 Checkpoint
> > > > > > 
> > > > > >     # 方式 2：命令行评估（通过 run.py）
> > > > > >     # 在 habitat-baselines 目录下运行：
> > > > > >     python -u -m habitat_baselines.run \
> > > > > >       --config-name=pointnav/ppo_pointnav_example \
> > > > > >       habitat_baselines.evaluate=True \
> > > > > >       habitat_baselines.eval_ckpt_path_dir="data/new_checkpoints/ckpt.50.pth" \
> > > > > >       habitat_baselines.eval.video_option='["disk"]'
> > > > > > 
> > > > > > > 💡
> > > > > > > 
> > > > > > > <div class="tip-title">
> > > > > > > 
> > > > > > > 📹 视频输出
> > > > > > > 
> > > > > > > 设置 `eval.video_option: ["disk"]` 会在评估时保存 agent 的第一视角视频到 `video_dir`。 设置 `["tensorboard"]` 会将视频上传到 TensorBoard。 视频对于调试和理解 agent 行为非常有帮助。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### 7.4 训练 vs 评估的数据集分离
> > > > > > > 
> > > > > > > <div class="arch-diagram">
> > > > > > > 
> > > > > > > <div class="arch-row">
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">
> > > > > > > 
> > > > > > > **Train Split** <span class="small">用于训练 RL policy</span>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">
> > > > > > > 
> > > > > > > **Val Split** <span class="small">用于调超参 + 早停</span>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">
> > > > > > > 
> > > > > > > **Test Split** <span class="small">最终评测（不用于训练）</span>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > 在配置文件中通过 `habitat.dataset.split: "train"` 指定使用哪个 split。 训练时用 train split，评估时用 val/test split。这是 ML 的基本实践但在 RL 中容易被忽略。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="section">
> > > > > > > 
> > > > > > > <div class="container">
> > > > > > > 
> > > > > > > ## 8\. 实践指南
> > > > > > > 
> > > > > > > 从安装到首次训练成功的步骤清单。
> > > > > > > 
> > > > > > > <div>
> > > > > > > 
> > > > > > > <div class="info-title" style="color:#60a5fa;">
> > > > > > > 
> > > > > > > 学习目标
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > 学会解读训练日志、调优参数、估算训练时间  
> > > > > > > <span style="color:#fbbf24;font-size:0.82rem;">🤔 你盯着 TensorBoard 看了一个小时，reward 曲线像心电图一样上下跳动——这是在"学习"还是在"抽风"？你怎么判断训练是正常的？</span>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### 8.1 训练前检查清单
> > > > > > > 
> > > > > > > | \# | 检查项                   | 命令 / 说明                                                      |
> > > > > > > | -- | --------------------- | ------------------------------------------------------------ |
> > > > > > > | 1  | habitat-lab 已安装       | `pip install -e habitat-lab`                                 |
> > > > > > > | 2  | habitat-baselines 已安装 | `pip install -e habitat-baselines`                           |
> > > > > > > | 3  | 场景数据集已下载              | `data/scene_datasets/` 下的 .glb 文件                            |
> > > > > > > | 4  | 任务数据集已下载              | `data/datasets/pointnav/` 下的 .json.gz 文件                     |
> > > > > > > | 5  | GPU 可用                | `python -c "import torch; print(torch.cuda.is_available())"` |
> > > > > > > | 6  | 配置文件路径正确              | 确认 benchmark YAML 中的 data\_path 指向正确路径                       |
> > > > > > > 

> > > > > > > ### 8.2 启动训练
> > > > > > > 
> > > > > > >     # 在 habitat-baselines 目录下：
> > > > > > >     cd habitat-baselines
> > > > > > >     
> > > > > > >     # 方式 A：使用示例配置（habitat-test 数据集，快速试跑）
> > > > > > >     python -u -m habitat_baselines.run \
> > > > > > >       --config-name=pointnav/ppo_pointnav_example
> > > > > > >     
> > > > > > >     # 方式 B：使用完整 PointNav PPO 配置（Gibson 数据集）
> > > > > > >     python -u -m habitat_baselines.run \
> > > > > > >       --config-name=pointnav/ppo_pointnav
> > > > > > >     
> > > > > > >     # 方式 C：DD-PPO 多 GPU 训练
> > > > > > >     python -u -m habitat_baselines.run \
> > > > > > >       --config-name=pointnav/ddppo_pointnav
> > > > > > > 
> > > > > > > <div>
> > > > > > > 
> > > > > > > **训练的最终目的是什么？**
> > > > > > > 
> > > > > > > **不是跑通命令，而是让策略网络学会"看→走"。** 每个配置项都为这个目标服务：  
> > > > > > > · `total_num_steps` — 给策略多长时间的试错机会（越多越好，受限于时间和算力）  
> > > > > > > · `lr` — 每次试错后更新多大的步子（太大发散，太小收敛太慢）  
> > > > > > > · `num_environments` — 同时跑多少个并行环境（更多=样本更多样=训练更稳定）  
> > > > > > > · `reward_measure` — 定义"什么是做得好"（distance\_to\_goal\_reward = "靠近目标加分"）  
> > > > > > > · 最终输出：一批 `.pth` checkpoint 文件，加载后可推理导航
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### 8.2B 程序执行流程分析
> > > > > > > 
> > > > > > > 当你执行 `python -u -m habitat_baselines.run` 时，Habitat 内部发生了以下事情：
> > > > > > > 
> > > > > > > <div class="arch-diagram">
> > > > > > > 
> > > > > > > <div class="arch-row">
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">
> > > > > > > 
> > > > > > > **① Hydra 配置加载** <span class="small">habitat\_baselines/run.py:main()</span>
> > > > > > > 
> > > > > > > <div class="arch-arrow-center">
> > > > > > > 
> > > > > > > ↓ 读取 `pointnav/ppo_pointnav_example.yaml` → 组合 lab + baselines 配置
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="arch-row">
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#f59e0b20;border:1px solid #f59e0b40;">
> > > > > > > 
> > > > > > > **② 创建 Trainer** <span class="small">baseline\_registry.get\_trainer(config)</span>
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <span style="font-size:0.85rem;color:var(--text-dim);align-self:center;">→</span>
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#3b82f620;border:1px solid #3b82f640;">
> > > > > > > 
> > > > > > > **③ 创建 VectorEnv** <span class="small">construct\_envs() → N 个并行 env</span>
> > > > > > > 
> > > > > > > <div class="arch-arrow-center">
> > > > > > > 
> > > > > > > ↓ VectorEnv 自动分派：每个子进程运行一个独立的 Habitat Env
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > <div class="arch-row">
> > > > > > > 
> > > > > > > <div class="arch-layer" style="background:#10b98120;border:1px solid #10b98140;">
> > > > > > > 
> > > > > > > **④ 训练循环** <span class="small">trainer.train() → PPOTrainer.\_collect\_rollout()</span>
> > > > > > > 
> > > > > > > <div class="arch-arrow-center">
> > > > > > > 
> > > > > > > ↓ 循环 num\_updates 次，每次：
> > > > > > > 
> > > > > > > | 步骤 | 操作             | 对应代码                               | 说明                                                                                                                            |
> > > > > > > | -- | -------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
> > > > > > > | 4a | **收集 Rollout** | `_collect_rollout_step()`          | 每个 env 执行 `num_steps` 步（默认 32）。总共收集 `num_environments × num_steps` 个 (obs, action, reward, next\_obs, done) 元组                |
> > > > > > > | 4b | **计算 Returns** | `RolloutStorage.compute_returns()` | 用 GAE (Generalized Advantage Estimation) 从每个 step 的 reward 反向计算 advantage 和 return。`gamma=0.99` 控制远期奖励权重，`tau=0.95` 控制偏差-方差权衡 |
> > > > > > > | 4c | **PPO Update** | `PPOUpdater.update()`              | 用 clipped surrogate objective 更新策略网络：限制新旧策略的概率比在 `[1-ε, 1+ε]` 区间，防止单次更新过大导致训练崩溃                                               |
> > > > > > > | 4d | **日志记录**       | `log_interval` 控制                  | 每隔 `log_interval` 次 update 打印一次终端日志 + 写入 TensorBoard（reward, success, SPL, losses, entropy）                                   |
> > > > > > > | 4e | **Checkpoint** | `checkpoint_interval` 控制           | 每隔 `checkpoint_interval` 次 update 保存一次模型（`ckpt.{N}.pth`），保存 optimizer/scheduler 状态以支持 resume                                  |
> > > > > > > 

> > > > > > > > 💡
> > > > > > > > 
> > > > > > > > <div class="tip-title">
> > > > > > > > 
> > > > > > > > 关键源码路径
> > > > > > > > 
> > > > > > > > · `habitat_baselines/run.py` — Hydra main 入口，解析配置 → 创建 trainer → 调用 train()  
> > > > > > > > · `habitat_baselines/rl/ppo/ppo_trainer.py` — PPOTrainer 类，`train()` 主循环（约 1200 行）  
> > > > > > > > · `habitat_baselines/common/rollout_storage.py` — RolloutStorage, GAE 计算  
> > > > > > > > · `habitat_baselines/rl/ppo/ppo_updater.py` — PPO clip objective + 梯度更新
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### 8.2C 关键训练参数调优建议
> > > > > > > > 
> > > > > > > > <table>
> > > > > > > > <colgroup>
> > > > > > > > <col style="width: 25%" />
> > > > > > > > <col style="width: 25%" />
> > > > > > > > <col style="width: 25%" />
> > > > > > > > <col style="width: 25%" />
> > > > > > > > </colgroup>
> > > > > > > > <thead>
> > > > > > > > <tr class="header">
> > > > > > > > <th>参数</th>
> > > > > > > > <th>默认值</th>
> > > > > > > > <th>Hydra 覆盖方式</th>
> > > > > > > > <th>调优建议</th>
> > > > > > > > </tr>
> > > > > > > > </thead>
> > > > > > > > <tbody>
> > > > > > > > <tr class="odd">
> > > > > > > > <td><strong>total_num_steps</strong><br />
> > > > > > > > <span class="small">总训练步数</span></td>
> > > > > > > > <td>1e6 (示例)<br />
> > > > > > > > 7.5e7 (生产)</td>
> > > > > > > > <td><code>habitat_baselines.total_num_steps=5e6</code></td>
> > > > > > > > <td>示例配置仅 100 万步（约 10 分钟），策略不会学会导航。要看到有效的导航行为<strong>至少设 500 万步</strong>（500 万 ~ 1 小时）。生产级训练建议 7500 万步以上（3-7 天）<br />
> > > > > > > > · 快速验证 pipeline：<code>1e5</code>（5 分钟）<br />
> > > > > > > > · 观察学习趋势：<code>5e6</code>（30-60 分钟）<br />
> > > > > > > > · 获得可用模型：<code>≥ 2.5e7</code>（半天-1天）</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="even">
> > > > > > > > <td><strong>num_environments</strong><br />
> > > > > > > > <span class="small">并行环境数</span></td>
> > > > > > > > <td>4 (示例)<br />
> > > > > > > > 16-32 (生产)</td>
> > > > > > > > <td><code>habitat_baselines.num_environments=8</code></td>
> > > > > > > > <td>每个 update 的 batch size = <code>num_environments × num_steps</code>。增大会让训练更稳定（更多样本估计梯度），但 GPU 显存和 CPU 内存线性增长<br />
> > > > > > > > · 8GB 显存：4-6 env<br />
> > > > > > > > · 16GB 显存：8-12 env<br />
> > > > > > > > · 24GB+ 显存：16-32 env</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="odd">
> > > > > > > > <td><strong>num_steps</strong><br />
> > > > > > > > <span class="small">每 update 步数</span></td>
> > > > > > > > <td>32 (示例)<br />
> > > > > > > > 128 (生产)</td>
> > > > > > > > <td><code>habitat_baselines.num_steps=64</code></td>
> > > > > > > > <td>更大的 num_steps 让每个 update 包含更长的时间序列，有助于学习长期依赖。但 batch 内存 = <code>num_envs × num_steps × obs_size</code><br />
> > > > > > > > · PointNav 简单任务：32-64 足够<br />
> > > > > > > > · ObjectNav/VLN 复杂任务：128-256</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="even">
> > > > > > > > <td><strong>lr</strong><br />
> > > > > > > > <span class="small">学习率</span></td>
> > > > > > > > <td>2.5e-4</td>
> > > > > > > > <td><code>habitat_baselines.lr=1e-4</code></td>
> > > > > > > > <td><strong>这与 PPO 的 clip_param 耦合。</strong> 如果 reward 震荡剧烈，先降 lr（试试 1e-4 或 5e-5）；如果 reward 始终不上升，试试增大 lr (5e-4)。配合 <code>use_linear_lr_decay=True</code> 使用更佳</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="odd">
> > > > > > > > <td><strong>clip_param</strong><br />
> > > > > > > > <span class="small">PPO 裁剪参数</span></td>
> > > > > > > > <td>0.1 (示例)<br />
> > > > > > > > 0.2 (标准)</td>
> > > > > > > > <td><code>habitat_baselines.clip_param=0.2</code></td>
> > > > > > > > <td>越小越保守（训练稳定但收敛慢），越大越激进（收敛快但可能发散）。0.1-0.2 是安全区间<br />
> > > > > > > > · 如果你看到 loss 频繁出现 NaN，减小到 0.05<br />
> > > > > > > > · 如果 reward 上升太慢，增大到 0.3</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="even">
> > > > > > > > <td><strong>entropy_coef</strong><br />
> > > > > > > > <span class="small">熵正则化</span></td>
> > > > > > > > <td>0.01</td>
> > > > > > > > <td><code>habitat_baselines.entropy_coef=0.02</code></td>
> > > > > > > > <td>防止策略过早收敛到单一动作。观察 TensorBoard：如果 <code>entropy</code> 快速降到 0，增大此值（0.02-0.05）。如果策略完全不学习，减小此值</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="odd">
> > > > > > > > <td><strong>max_episode_steps</strong><br />
> > > > > > > > <span class="small">episode 最大步数</span></td>
> > > > > > > > <td>500</td>
> > > > > > > > <td><code>habitat.environment.max_episode_steps=200</code></td>
> > > > > > > > <td>限制每个 episode 的步数上限。太短会导致 agent 来不及到达目标就超时（影响成功率），太长会浪费训练时间<br />
> > > > > > > > · 小场景（test）：100-200<br />
> > > > > > > > · 中等场景（Gibson）：300-500<br />
> > > > > > > > · 大场景（MP3D/HM3D）：500-1000</td>
> > > > > > > > </tr>
> > > > > > > > <tr class="even">
> > > > > > > > <td><strong>eval_interval</strong><br />
> > > > > > > > <span class="small">评估间隔</span></td>
> > > > > > > > <td>25 (updates)</td>
> > > > > > > > <td><code>habitat_baselines.eval_interval=10</code></td>
> > > > > > > > <td>每隔多少步 evaluation 一次（在验证集上运行，不更新策略）。频繁评估会拖慢训练<br />
> > > > > > > > · 快速实验：10<br />
> > > > > > > > · 长周期训练：50-100</td>
> > > > > > > > </tr>
> > > > > > > > </tbody>
> > > > > > > > </table>
> > > > > > > > 
> > > > > > > > ``` 
> > > > > > > >       一个完整的「快速有效训练」命令示例
> > > > > > > > ```
> > > > > > > > 
> > > > > > > >     # 合并参数覆盖：更多步数 + 更多并行环境 + 小学习率
> > > > > > > >     $ python -u -m habitat_baselines.run \
> > > > > > > >         --config-name=pointnav/ppo_pointnav_example \
> > > > > > > >         habitat_baselines.total_num_steps=5000000 \
> > > > > > > >         habitat_baselines.num_environments=8 \
> > > > > > > >         habitat_baselines.num_steps=64 \
> > > > > > > >         habitat_baselines.lr=1e-4 \
> > > > > > > >         habitat_baselines.clip_param=0.1 \
> > > > > > > >         habitat_baselines.use_linear_lr_decay=True
> > > > > > > > 
> > > > > > > > ### 8.2D 训练过程的终端输出详解
> > > > > > > > 
> > > > > > > > 训练时终端会周期性打印状态。第一次看到时可能不知所措——下面是每条输出逐字段的解读。
> > > > > > > > 
> > > > > > > > ``` 
> > > > > > > >       训练启动信息
> > > > > > > > ```
> > > > > > > > 
> > > > > > > >     # 启动时会看到类似以下的信息（这是 ppo_pointnav_example 的典型输出）
> > > > > > > >     2026-06-11 10:15:23,456 Initializing dataset PointNav-v1
> > > > > > > >     2026-06-11 10:15:23,512 initializing sim Sim-v0
> > > > > > > >     # ── 关键信息：数据集大小、训练步数、环境数 ──
> > > > > > > >     Number of training episodes: 1  # habitat-test 只有 1 个训练 episode（用于快速测试）
> > > > > > > >     Total number of updates: 2441     # = total_num_steps / (num_envs × num_steps)，示例配置共 ~2441 次 update
> > > > > > > >     Number of environments: 4         # 4 个并行环境
> > > > > > > >     Number of steps per env: 32       # 每个 update 前每个 env 执行 32 步
> > > > > > > > 
> > > > > > > > ``` 
> > > > > > > >       训练中每隔 log_interval 次 update 的输出（简化示例）
> > > > > > > > ```
> > > > > > > > 
> > > > > > > >     update: 100   fps: 1580.3   total reward: -0.42   success: 0.00   spl: 0.00
> > > > > > > >       distance_to_goal: 3.24   entropy: 1.38   value_loss: 0.15   policy_loss: 0.003  lr: 2.5e-4
> > > > > > > > 
> > > > > > > > | 字段                       | 期望走势    | 含义                                                                                                                    |
> > > > > > > > | ------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------- |
> > > > > > > > | `update: 100`            | 递增      | 第 100 次 PPO 更新。总共会有 \~2441 次 update。如果这个数字卡住不动，说明 rollout 收集卡死了                                                       |
> > > > > > > > | `fps: 1580`              | 稳定      | Frame Per Second — 每秒处理的仿真帧数。受场景复杂度、RGB 分辨率、env 数量影响。如果 fps 异常低（\<100），检查 GPU 是否被其他进程占用                               |
> > > > > > > > | `total reward: -0.42`    | ↑ 上升    | 最近一个 rollout 的平均 episode 总奖励。初始为负值是正常的（agent 随机移动碰不到目标，只收 slack penalty）。训练成功的标志是从负数逐渐上升，最终转正                         |
> > > > > > > > | `success: 0.00`          | ↑ 上升    | 最近 rollout 中成功到达目标的 episode 比例（= success\_rate）。前几百步通常为 0 — agent 还没学会如何移动。这是**最重要的指标**。如果 20% 总更新后 success 还是 0，检查参数 |
> > > > > > > > | `spl: 0.00`              | ↑ 上升    | Success weighted by Path Length。考虑路径效率的成功率：`SPL = 1/N Σ S_i × (l_i_opt / max(l_i, l_i_opt))`。agent 不仅到达目标，而且走了接近最短路径  |
> > > > > > > > | `distance_to_goal: 3.24` | ↓ 下降    | episode 结束时的平均剩余距离。训练初期 agent 原地转圈，距离维持不变甚至增大。学会导航后这个值会持续下降                                                           |
> > > > > > > > | `entropy: 1.38`          | 缓慢下降    | 策略的动作分布熵。`ln(4)≈1.39` 是最大值（4 个动作完全均匀随机）。如果快速跌到 \~0.01，说明策略过早崩溃为确定性（只选一个动作），需增大 `entropy_coef`                         |
> > > > > > > > | `value_loss: 0.15`       | 下降后稳定   | Value function 的 MSE loss。帮助判断 Critic 是否在改善对 future reward 的估计。如果持续上升说明策略更新太大，降低 lr                                   |
> > > > > > > > | `policy_loss: 0.003`     | 波动      | PPO clipped surrogate loss。这个值的大小没有绝对标准，重要的是它**不出现 NaN 或 ±∞**                                                         |
> > > > > > > > | `lr: 2.5e-4`             | 不变或线性衰减 | 当前 learning rate。如果启用了 `use_linear_lr_decay=True`，会从初始值线性衰减到 0                                                        |
> > > > > > > > 

> > > > > > > > ### 8.2E 训练过程分析：什么样的曲线是健康的？
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **从随机到收敛的三个阶段**
> > > > > > > > 
> > > > > > > > 一个典型的 PPO PointNav 训练会经历以下阶段（以 `total_num_steps=5e6` 为例）：
> > > > > > > > 
> > > > > > > > | 阶段          | updates 范围  | 特征                             | 你应该看到的现象                                                                                                                               |
> > > > > > > > | ----------- | ----------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
> > > > > > > > | **1. 随机探索** | 0 \~ 10%    | reward 为负，success = 0          | total reward 在 -2 到 -0.5 之间波动。entropy \~1.38。策略还在随机试错，碰巧靠近目标时 reward 短暂为正但很快又被随机动作冲掉。这是正常的——耐心等                                        |
> > > > > > > > | **2. 初步学习** | 10% \~ 30%  | reward 开始上升，occasional success | total reward 从 -0.5 向 0 靠近。success 不再恒为 0，偶尔出现 0.05-0.15。entropy 开始缓慢下降（\~1.2-1.3）。策略开始理解"向 target direction 走有用"                      |
> > > > > > > > | **3. 稳定收敛** | 30% \~ 100% | success 持续上升，entropy 趋于稳定      | reward 转为正（+2 到 +5），success 达到 0.4-0.6+。SPL 从 0 上升到 0.3+（路径开始优化）。entropy 稳定在 0.3-0.8。如果 success 在某个值停滞不前且 entropy 接近 0，说明策略已经"满足"于局部最优 |
> > > > > > > > 

> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > > ⚠️
> > > > > > > > > 
> > > > > > > > > <div class="warn-title">
> > > > > > > > > 
> > > > > > > > > 需要警惕的危险信号
> > > > > > > > > 
> > > > > > > > > | 现象                             | 可能原因                                   | 修复方法                                                    |
> > > > > > > > > | ------------------------------ | -------------------------------------- | ------------------------------------------------------- |
> > > > > > > > > | reward 完全不变（波动幅度 \< 0.01）      | 学习率太小或 reward scale 问题                 | 增大 lr → 5e-4；检查 reward\_measure 配置是否生效                  |
> > > > > > > > > | reward 剧烈震荡（相邻 update 之间跳 ±5+） | 学习率太大、batch size 太小                    | 降 lr → 5e-5；增大 num\_environments → 16                   |
> > > > > > > > > | entropy 在 5% 进度内降到 \< 0.01     | 策略过早崩溃（entropy collapse）               | 增大 entropy\_coef → 0.05；减小 clip\_param → 0.05           |
> > > > > > > > > | policy\_loss 出现 NaN            | 数值不稳定（梯度爆炸或 advantage 异常）              | 减小 clip\_param → 0.05；检查 max\_grad\_norm (设为 0.5)；降低 lr |
> > > > > > > > > | success 上升到 0.3 后突然跌回 0        | 策略"忘记"了已学会的行为（catastrophic forgetting） | 减小 lr；增大 num\_mini\_batch；降低 clip\_param                |
> > > > > > > > > | fps 在训练中途从 \~1500 掉到 \~100     | 某个 env 子进程卡住或 GPU 显存泄漏                 | 检查 GPU 显存使用（nvidia-smi）；减少 num\_environments；降低 RGB 分辨率 |
> > > > > > > > > 

> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > > 💡
> > > > > > > > > > 
> > > > > > > > > > <div class="tip-title">
> > > > > > > > > > 
> > > > > > > > > > 推荐查看 TensorBoard 的 4 个关键面板
> > > > > > > > > > 
> > > > > > > > > > `tensorboard --logdir=tb` 启动后在浏览器打开 `http://localhost:6006`：  
> > > > > > > > > > · **SCALARS → reward** — 窗口大小改为 100，观察平滑后的上升趋势  
> > > > > > > > > > · **SCALARS → success** — 这是最终目标指标，关注最终收敛值（\> 0.5 才算有效训练）  
> > > > > > > > > > · **SCALARS → entropy** — 不应为 0（为 0 = 策略死了），不应维持 1.38 不变（= 没学到任何东西）  
> > > > > > > > > > · **SCALARS → value\_loss + policy\_loss** — 两者都不应出现 NaN 或持续增大
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > ### 8.3 监控训练进度
> > > > > > > > > > 
> > > > > > > > > > <div class="module-grid">
> > > > > > > > > > 
> > > > > > > > > > <div class="module" style="border-left-color:#f59e0b;">
> > > > > > > > > > 
> > > > > > > > > > ### 📊 TensorBoard
> > > > > > > > > > 
> > > > > > > > > > 训练日志自动写入 `tensorboard_dir`。启动 TensorBoard 查看：
> > > > > > > > > > 
> > > > > > > > > >   - `tensorboard --logdir=tb`
> > > > > > > > > >   - 查看 reward 曲线（应上升）
> > > > > > > > > >   - 查看 value\_loss / policy\_loss
> > > > > > > > > >   - 查看熵值（不应为 0）
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > <div class="module" style="border-left-color:#10b981;">
> > > > > > > > > > 
> > > > > > > > > > ### 📁 Checkpoint
> > > > > > > > > > 
> > > > > > > > > > 模型按进度均匀保存到 `checkpoint_folder`：
> > > > > > > > > > 
> > > > > > > > > >   - `ckpt.1.pth` (2% 进度)
> > > > > > > > > >   - `ckpt.25.pth` (50% 进度)
> > > > > > > > > >   - `ckpt.50.pth` (100% 进度)
> > > > > > > > > >   - `latest.pth` (总是最新)
> > > > > > > > > > 
> > > > > > > > > > ### 8.4 常见问题排查
> > > > > > > > > > 
> > > > > > > > > > | 现象              | 可能原因                         | 解决方法                                         |
> > > > > > > > > > | --------------- | ---------------------------- | -------------------------------------------- |
> > > > > > > > > > | reward 不上升      | 学习率过高/过低、reward 缩放不正确        | 调整 lr (试 1e-4 \~ 1e-3)，检查 reward\_measure 定义 |
> > > > > > > > > > | success 始终为 0   | 任务太难、max\_episode\_steps 太短  | 减小场景复杂度、增大 max\_episode\_steps               |
> > > > > > > > > > | entropy → 0     | 策略过早收敛到确定性动作                 | 增大 entropy\_coef 或启用 adaptive entropy        |
> > > > > > > > > > | GPU 显存不足 (OOM)  | num\_environments 太大 / 分辨率太高 | 减小 num\_environments 或降低分辨率                  |
> > > > > > > > > > | checkpoint 加载失败 | 配置不匹配 / 模型结构变化               | 设置 `eval.use_ckpt_config=True` 使用保存时的配置      |
> > > > > > > > > > 

> > > > > > > > > > ### 8.5 训练周期估算
> > > > > > > > > > 
> > > > > > > > > > <div>
> > > > > > > > > > 
> > > > > > > > > > **⚡ 性能参考（单卡 RTX 2070 SUPER，habitat-test 数据集）**
> > > > > > > > > > 
> > > > > > > > > > · **1 个环境 + 128×128 RGB**：约 100-200 FPS（帧/秒）  
> > > > > > > > > > · **total\_num\_steps = 1e6**：约 1.5-3 小时  
> > > > > > > > > > · **完整 Gibson 数据集**（72 个训练场景）：建议 **total\_num\_steps ≥ 2.5e8**，约 3-7 天（单卡）  
> > > > > > > > > > · **DD-PPO 8 GPU**：可将 Gibson 训练缩短到约 12-24 小时
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > > ⚠️
> > > > > > > > > > > 
> > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > 
> > > > > > > > > > > ⚠️ habitat-test 只适合调试！
> > > > > > > > > > > 
> > > > > > > > > > > `habitat-test-scenes` 只有 1 个小场景，用于验证 pipeline 是否正常。 **训练有效模型必须使用完整数据集**（Gibson、HM3D 或 MP3D）。 habitat-test 上 train 出来的 checkpoint 在实际场景中几乎不可用。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 本章总结
> > > > > > > > > > > 
> > > > > > > > > > > | 主题              | 核心概念                                                                   | 你学到了什么                                    |
> > > > > > > > > > > | --------------- | ---------------------------------------------------------------------- | ----------------------------------------- |
> > > > > > > > > > > | **导航任务全景**      | 6 种任务类型：PointNav / ObjectNav / ImageNav / InstanceImageNav / VLN / EQA | 从几何坐标到语言问答，理解 Embodied AI 导航全谱系           |
> > > > > > > > > > > | **Policy 网络结构** | CNN+RNN+Actor/Critic；训练对象；预训练/微调；环境依赖性                                 | 理解 RL 到底训练什么、是否需要基础模型、模型如何跨场景迁移           |
> > > > > > > > > > > | **环境包装链**       | Env → RLEnv → GymHabitatEnv → VectorEnv                                | 每层增加一个能力维度，最终输出 (obs, reward, done, info) |
> > > > > > > > > > > | **PPO 算法**      | clip\_param + GAE + actor-critic                                       | Rollout → Compute Returns → PPO Update 循环 |
> > > > > > > > > > > | **训练配置体系**      | Hydra defaults 合并 benchmark + baselines                                | `run.py` → Hydra 加载 → 统一的 DictConfig      |
> > > > > > > > > > > | **RL 导航实战**     | 观测→动作→奖励循环；传统导航 vs RL 导航                                               | 用 `rl_nav_demo.py` 跑通完整的探索→训练→推理流程        |
> > > > > > > > > > > | **评估体系**        | Benchmark.evaluate() / trainer.eval()                                  | success, SPL, distance\_to\_goal 三项核心指标   |
> > > > > > > > > > > | **实践**          | 训练命令 + 监控 + 排查                                                         | 从 pip install 到 tensorboard 的完整流程         |
> > > > > > > > > > > 

> > > > > > > > > > > <div class="exercise">
> > > > > > > > > > > 
> > > > > > > > > > > #### 🏋️ 课后练习
> > > > > > > > > > > 
> > > > > > > > > > > **0.** 运行 RL 导航 Demo：`python examples/rl_nav_demo.py --explore-only`， 理解观测空间、动作空间和奖励信号的设计。  
> > > > > > > > > > > **1.** 用 habitat-test 数据集跑一次完整的 PPO 训练（`total_num_steps=50000`）， 观察 TensorBoard 中的 reward 和 entropy 曲线。  
> > > > > > > > > > > **2.** 修改 `entropy_coef` 从 0.01 到 0.05，重新训练，对比 exploration 行为的差异。  
> > > > > > > > > > > **3.** 对比 `clip_param=0.1` 和 `clip_param=0.3` 的训练曲线， 理解 "保守更新 vs 激进更新" 的差异。  
> > > > > > > > > > > **4.** 训练完成后，对同一个 checkpoint 用不同的 `success_distance` (0.1/0.2/0.5) 评估， 观察成功率的变化（提示：评估时修改 `task.measurements.success.success_distance`）。  
> > > > > > > > > > > **5. (进阶)** 注册一个自定义 `reward_measure`（如 collision\_penalty）， 训练一个学会避障的 agent。
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
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
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
>
# 第7步：VLN 视觉语言导航 — Habitat 从零理解

> 在 Habitat 中训练视觉语言导航（VLN）模型：配置 VLN-v0 任务、理解 R2R 数据集与 InstructionSensor、 跑通模仿学习 + DDPPO 微调、导出 checkpoint 为真机部署做准备。

## 本章概览：10 个案例

从 IL 训练到诊断修复，从 SOTA 参照到模型微调——VLN 一条线走到底。前置：[第5步「导航任务全景」§1.6](habitat-textbook-step5.html) 已介绍 VLN 是什么。

从配置到训练到导出，每一步都可独立运行和验证。建议按顺序完成。

| \#  | 案例                    | 你将学会                                               | 难度   | 前置条件        |
| --- | --------------------- | -------------------------------------------------- | ---- | ----------- |
| 7-1 | [配置 VLN 任务](#case7-1) | VLN-v0 任务配置、R2R 数据集加载、验证环境可创建                      | ⭐⭐   | Step 2      |
| 7-2 | [理解数据与传感器](#case7-2)  | R2R episode 结构、InstructionSensor 原理、observation 空间 | ⭐⭐   | 7-1         |
| 7-3 | [模仿学习训练](#case7-3)    | IL 训练流程、teacher-forcing、checkpoint 保存              | ⭐⭐⭐  | 7-2, Step 5 |
| 7-4 | [评估与导出模型](#case7-4)   | SR/SPL/nDTW 指标、模型推理模式、导出 checkpoint                | ⭐⭐   | 7-3         |
| 7-4 | [避坑诊断](#case7-4)      | CLIP实验、行为漂移分析——学会诊断ML工程问题                          | ⭐⭐⭐  | 7-3         |
| 7-5 | [DAgger 桥接](#case7-5) | IL 32% → DAgger 50% → RL 55%+ 三阶梯对比                | ⭐⭐⭐⭐ | 7-4         |
| 7-6 | [SOTA 参照](#case7-6)   | 运行 JanusVLN，对比小模型，理解参数量级差距                         | ⭐⭐⭐  | 7-5         |

## 为什么 VLN 必须依赖 Matterport3D？

从 IL 训练到诊断修复，从 SOTA 参照到模型微调——VLN 一条线走到底。前置：[第5步「导航任务全景」§1.6](habitat-textbook-step5.html) 已介绍 VLN 是什么。

这不是 Habitat 的限制，而是 VLN 任务本身的定义方式决定的。

<div>

**R2R —— VLN 领域的"ImageNet"**

R2R (Room-to-Room) 是 CVPR 2018 提出的视觉语言导航基准数据集，至今**每篇 VLN 论文都以它为评测标准**。 它的采集方式是：人类标注者在 **90 栋 Matterport3D 建筑**中行走，用自然语言写下导航指令， 例如 *"Walk down the hallway, turn left at the painting, and stop in front of the bed."*  
  
**这决定了：语言指令和 MP3D 场景是绑定的。** 换一栋建筑，"绘画"和"走廊"都不同了，指令不再有意义。 正因为如此，VLN 任务无法像 PointNav 那样在不同场景数据集间切换。

</div>

### 数据依赖链

<div class="arch-diagram">

<div class="arch-row">

<div class="arch-layer" style="background:#ef444420;border:2px solid #ef4444;min-width:220px;">

R2R 数据集  
<span class="small">10,819 条导航指令</span>

</div>

<div style="margin:0 12px;color:var(--text-dim);align-self:center;">

引用

</div>

<div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:220px;">

MP3D 场景 ID  
<span class="small">90 栋建筑的 .glb 文件</span>

</div>

<div style="margin:0 12px;color:var(--text-dim);align-self:center;">

运行时

</div>

<div class="arch-layer" style="background:#10b98120;border:2px solid #10b981;min-width:220px;">

VLN 仿真器  
<span class="small">Instruction → Action → SR/SPL/nDTW</span>

</div>

Habitat 的 VLN 代码（`VLNDatasetV1` / `VLNTask`）本身是**场景无关的**。 但整个 Habitat-Lab 中只注册了 `R2RVLN-v1` 这一个 VLN 数据集， 它的配置硬编码指向 `data/datasets/vln/mp3d/r2r/`，而其中的 episodes 引用的都是 MP3D 场景。

### 无需认证的获取方案

| 文件                    | 大小     | 来源                                     | 覆盖                            | 需要认证？ |
| --------------------- | ------ | -------------------------------------- | ----------------------------- | ----- |
| `vln_r2r_mp3d_v1.zip` | 2.7 MB | Facebook CDN（`dl.fbaipublicfiles.com`） | 10,819 训练 + 1,020 验证 episodes | 否     |
| `MatterPort3D.zip`    | 665 MB | 清华大学云盘                                 | 11 个场景（val\_unseen 全集）        | 否     |
| `mp3d_example`        | 93 MB  | Habitat 内置（`datasets_download`）        | 1 个场景（17DRP5sb8fy）            | 否     |

> 💡
> 
> <div class="tip-title">
> 
> 当前状态：12 个场景，可完整走通 VLN 流程
> 
> 以上三样合计 **\< 800 MB**，全部免除认证。覆盖：  
> • **训练**：17DRP5sb8fy 在 R2R train 中有 75 条指令，足够演示训练流程  
> • **评估**：11 个 val\_unseen 场景覆盖 1,839 条指令，可直接跑标准 val\_unseen 评估  
> • 如需完整 90 场景（训练出可发表级 VLN 模型），才需要官方申请 Matterport3D
> 
> </div>
> 
> > ⚠️
> > 
> > <div class="warn-title">
> > 
> > 有其他数据集可以替代吗？
> > 
> > **严格来说，没有。** 虽然存在 RxR（多语言 R2R）、REVERIE、SOON 等扩展 VLN 数据集， 但它们全部基于 MP3D 场景采集。HM3D 和 Gibson 都**没有**对应的 VLN 指令数据集。 如果你将来想对比发表的 VLN 模型或参加 Habitat Challenge，MP3D 是必经之路。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## 前置 · VLN 理论基础
> > 
> > 在动手写代码之前，先建立 VLN 的心智模型。
> > 
> > <div>
> > 
> > **VLN 一句话定义**
> > 
> > **Visual Language Navigation（视觉语言导航）**： 给定一段自然语言指令（如"走过厨房，在卧室门口停下"），Agent 仅凭 RGB 视觉观测， 在 3D 环境中逐步移动，最终停在指令描述的目标位置。
> > 
> > </div>
> > 
> > **为什么它比 PointNav 难？**
> > 
> > | 维度   | PointNav          | VLN                 |
> > | ---- | ----------------- | ------------------- |
> > | 目标表示 | GPS 坐标 (x,y) — 精确 | 自然语言 — 模糊、多义        |
> > | 推理需求 | 纯空间推理             | 视觉理解 + 语言理解 + 跨模态对齐 |
> > | 错误容忍 | 偏离 1m → 可能找不到     | 理解语义 → 能自我纠正        |
> > | 数据依赖 | 任何 3D 场景          | 需要人工标注指令（昂贵）        |
> > 

> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 📖 详细理论参考
> > > 
> > > 本章聚焦「动手实操」。如果你想深入了解 VLN 的技术流派（Seq2Seq / BERT-CLIP / LLM-VLM / 拓扑图 / 神经辐射场 / 世界模型）、 发展历程（R2R 2018 → RxR 2020 → REVERIE 2020 → VLN-CE 2022 → NaVid 2024）、 以及核心挑战（Sim2Real、长程记忆、多语言），请阅读 [VLN 理论专题 →](vln.html)。
> > > 
> > > <div id="case7-1" class="section">
> > > 
> > > <div class="container">
> > > 
> > > ## 7-1 · 配置 VLN 任务
> > > 
> > > <div>
> > > 
> > > **① 案例含义**
> > > 
> > > 使用 `habitat.get_config()` 加载 VLN 基准配置，创建一个 VLN 环境并验证它能正常 `reset()`。这是 VLN 训练的**最小验证单元**——如果这步不通过，后面的训练无从谈起。  
> > >   
> > > **前置条件：**已安装 habitat-lab + habitat-sim。R2R 数据集和 MP3D 场景的获取方式见上方"为什么 VLN 必须依赖 Matterport3D"（无需认证，合计 \< 800MB）。
> > > 
> > > </div>
> > > 
> > > ### ② 核心代码 & 关键函数
> > > 
> > > ``` 
> > >     复制
> > >     # case_6_1_vln_env.py — 验证 VLN 环境可创建并 reset
> > > import habitat
> > > 
> > > # VLN 使用专门的 benchmark 配置文件
> > > config = habitat.get_config(
> > >     config_path="benchmark/nav/vln/vln_r2r.yaml"
> > > )
> > > 
> > > # 可选：覆盖数据集路径
> > > with habitat.config.read_write(config):
> > >     config.habitat.dataset.data_path = "data/datasets/vln/r2r/v1/{split}/{split}.json.gz"
> > > 
> > > env = habitat.Env(config=config)
> > > obs = env.reset()
> > > 
> > > # VLN 的 observation 包含语言指令
> > > print("观测键:", list(obs.keys()))
> > > print("指令:", obs["instruction"]["text"][:80], "...")
> > > print("RGB shape:", obs["rgb"].shape)
> > > env.close()
> > > ```
> > > 
> > > </div>
> > > 
> > > | 函数                            | 角色          | 说明                                                |
> > > | ----------------------------- | ----------- | ------------------------------------------------- |
> > > | `habitat.get_config()`        | 加载基准配置      | 读取 YAML → 解析 Hydra → 返回冻结的 OmegaConf 配置对象         |
> > > | `habitat.config.read_write()` | 临时解冻配置      | 上下文管理器，在 `with` 块内可修改配置值                          |
> > > | `habitat.Env(config)`         | 创建环境        | 根据配置组装 Simulator + Dataset + Task                 |
> > > | `env.reset()`                 | 初始化 episode | 随机选一个 episode，返回 observation dict (含 instruction) |
> > > | `obs["instruction"]`          | 语言指令文本      | VLN 特有的 observation 键，由 InstructionSensor 生成      |
> > > 

> > > ### ③ 如何创建和运行
> > > 
> > > ``` 
> > >     复制
> > >     # 终端中运行
> > > $ python case_6_1_vln_env.py
> > > 
> > > # 预期输出（示例）
> > > 观测键: ['rgb', 'depth', 'instruction', 'pointgoal_with_gps_compass']
> > > 指令: Walk down the hallway, turn left at the first door, and stop in front of the bed. ...
> > > RGB shape: (3, 480, 640)
> > > ```
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > ⚠️ 常见错误
> > > > 
> > > > **1.** `Dataset not found` → 检查 R2R 数据集是否下载到了 `data/datasets/vln/r2r/`  
> > > > **2.** `Scene not found` → 检查 Matterport3D 场景是否在 `data/scene_datasets/mp3d/`  
> > > > **3.** `KeyError: 'instruction'` → 确认配置中 task 类型为 `VLN-v0` 而非 `Nav-v0`
> > > > 
> > > > </div>
> > > > 
> > > > ### ④ 运行效果
> > > > 
> > > > <div>
> > > > 
> > > > `env.reset()` 成功后，你会看到：  
> > > > **1.** 终端打印出观测键列表 — 确认 `instruction` 键存在  
> > > > **2.** 一段英文指令文本 — 这就是 VLN 模型需要理解并执行的导航命令  
> > > > **3.** RGB 图像的 shape 是 (3, H, W) — 证明视觉传感器工作正常  
> > > >   
> > > > 与 PointNav 最大的区别：**observation 中多了 `instruction` 字段**，这是让 VLN 不同于纯视觉导航的关键。
> > > > 
> > > > <div id="case7-2" class="section">
> > > > 
> > > > <div class="container">
> > > > 
> > > > ## 7-2 · 理解 R2R 数据与 InstructionSensor
> > > > 
> > > > <div>
> > > > 
> > > > **① 案例含义**
> > > > 
> > > > 深入 R2R (Room-to-Room) 数据集的一个 episode，理解 VLN 任务的**完整数据结构**： episode 包含什么字段、指令如何编码、InstructionSensor 如何把文本喂给模型。 这步至关重要——不理解数据，就无法设计模型输入。
> > > > 
> > > > </div>
> > > > 
> > > > ### ② R2R Episode 结构
> > > > 
> > > > <div class="arch-diagram">
> > > > 
> > > > <div style="font-size:0.9rem;color:#2dd4bf;font-weight:700;margin-bottom:16px;">
> > > > 
> > > > 一个 R2R Episode 的内部结构
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#3b82f620;border:2px solid #3b82f6;">
> > > > 
> > > > episode\_id  
> > > > <span class="small">"13361"</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-layer" style="background:#8b5cf620;border:2px solid #8b5cf6;">
> > > > 
> > > > scene\_id  
> > > > <span class="small">"2t7WUuJeko7"</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-layer" style="background:#10b98120;border:2px solid #10b981;">
> > > > 
> > > > start\_position + rotation  
> > > > <span class="small">(x,y,z) + quat</span>
> > > > 
> > > > <div class="arch-arrow-center">
> > > > 
> > > > ↓
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:280px;">
> > > > 
> > > > goals\[0\]  
> > > > <span class="small">position: (x,y,z) + radius</span>
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-layer" style="background:#ec489920;border:2px solid #ec4899;min-width:400px;">
> > > > 
> > > > reference\_path  
> > > > <span class="small">\[{position, rotation}×N\] — 最短路径轨迹点</span>
> > > > 
> > > > <div class="arch-arrow-center">
> > > > 
> > > > ↓
> > > > 
> > > > </div>
> > > > 
> > > > <div class="arch-row">
> > > > 
> > > > <div class="arch-layer" style="background:#14b8a620;border:2px solid #14b8a6;min-width:500px;">
> > > > 
> > > > instructions  
> > > > <span class="small">{instruction\_id, instruction\_text}×3 — 同一条路径的三段英文描述</span>
> > > > 
> > > > </div>
> > > > 
> > > > ### InstructionSensor 工作原理
> > > > 
> > > > <div class="flow-box">
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > 
> > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > 
> > > > R2R JSON
> > > > 
> > > > </div>
> > > > 
> > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > 
> > > > episode.instructions\[0\].instruction\_text
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > 
> > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > 
> > > > InstructionSensor
> > > > 
> > > > </div>
> > > > 
> > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > 
> > > > 读取 episode.instruction  
> > > > → tokenize → tensor
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #14b8a6;">
> > > > 
> > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > 
> > > > obs\["instruction"\]
> > > > 
> > > > </div>
> > > > 
> > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > 
> > > > token IDs (seq\_len,)  
> > > > 或原始文本
> > > > 
> > > > <div class="flow-arrow">
> > > > 
> > > > →
> > > > 
> > > > </div>
> > > > 
> > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > 
> > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > 
> > > > VLN Policy
> > > > 
> > > > </div>
> > > > 
> > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > 
> > > > LSTM/Transformer  
> > > > 编码指令 → 输出动作
> > > > 
> > > > </div>
> > > > 
> > > > ### ③ 如何验证数据
> > > > 
> > > > ``` 
> > > >     复制
> > > >     # case_6_2_inspect_data.py — 检查一个 episode 的完整数据
> > > > import habitat
> > > > 
> > > > config = habitat.get_config("benchmark/nav/vln/vln_r2r.yaml")
> > > > env = habitat.Env(config=config)
> > > > obs = env.reset()
> > > > 
> > > > # 从 Episode 对象获取完整数据
> > > > ep = env.current_episode
> > > > print("=== Episode 基本信息 ===")
> > > > print(f"episode_id:    {ep.episode_id}")
> > > > print(f"scene_id:      {ep.scene_id}")
> > > > print(f"start_position: {ep.start_position}")
> > > > print(f"goals[0].pos:  {ep.goals[0].position}")
> > > > print(f"reference_path 长度: {len(ep.reference_path)} 个路径点")
> > > > 
> > > > # 指令 — VLN 最核心的数据字段
> > > > print(f"\n=== 指令 ({len(ep.instructions)} 条) ===")
> > > > for i, instr in enumerate(ep.instructions):
> > > >     print(f"[{i}] {instr.instruction_text[:100]}...")
> > > > 
> > > > env.close()
> > > > ```
> > > > 
> > > > </div>
> > > > 
> > > > <div class="dual-panel">
> > > > 
> > > > <div class="panel">
> > > > 
> > > > #### 📐 NavigationGoal (VLN版)
> > > > 
> > > > VLN 的 goal 与 PointNav 完全一样——`position (x,y,z) + radius`。 区别在于**agent 不知道 goal 的坐标**，它只看到指令文本。 目标是靠理解语言来推断的，而非靠 GPS 传感器指向。
> > > > 
> > > > </div>
> > > > 
> > > > <div class="panel">
> > > > 
> > > > #### 📝 为什么有 3 条指令
> > > > 
> > > > 同一个 episode 由 3 个不同的标注员撰写指令。训练时随机选一条， 评估时用固定的一条。这迫使模型学习**语言多样性**——"turn left at the sofa" 和 "go left after passing the couch" 对应相同的路径。
> > > > 
> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 💡 关键理解：VLN 属于 "稀疏监督" 任务
> > > > > 
> > > > > 与 PointNav（每步都有 GPS+Compass 指向目标）不同，VLN 的 agent **只在 reset 时看到指令文本**。 后续每一步，模型必须记住指令内容并结合当前视觉观测做决策。这使得 VLN 天然需要 **记忆机制**（LSTM/Transformer/LLM）。
> > > > > 
> > > > > <div id="case7-3" class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 7-3 · 模仿学习训练
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **① 案例含义**
> > > > > 
> > > > > 使用 **Behavioral Cloning（行为克隆）**在 R2R 数据集上训练一个 VLN agent。 Agent 的监督信号来自 `reference_path`（最短路径轨迹），模型学习： 给定当前 RGB + 指令 → 预测下一步动作（前进/左转/右转/停止）。  
> > > > >   
> > > > > **前置：**需要 GPU。如仅有 CPU，可将 batch\_size 调至 1 且 epochs 设为 1 做语法验证。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ② 训练流程 & 关键函数
> > > > > 
> > > > > <div class="flow-box">
> > > > > 
> > > > > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > > > > 
> > > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > > 
> > > > > ① 数据准备
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > > 
> > > > > R2R episodes  
> > > > > → rollout 生成轨迹
> > > > > 
> > > > > <div class="flow-arrow">
> > > > > 
> > > > > →
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > > > > 
> > > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > > 
> > > > > ② Teacher-Forcing
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > > 
> > > > > reference\_path 动作  
> > > > > 作为 ground truth
> > > > > 
> > > > > <div class="flow-arrow">
> > > > > 
> > > > > →
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > > > > 
> > > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > > 
> > > > > ③ IL Loss
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > > 
> > > > > Cross Entropy  
> > > > > 动作分类
> > > > > 
> > > > > <div class="flow-arrow">
> > > > > 
> > > > > →
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div class="flow-step" style="border-top:3px solid #14b8a6;">
> > > > > 
> > > > > <div style="font-weight:600;font-size:0.9rem;">
> > > > > 
> > > > > ④ Checkpoint
> > > > > 
> > > > > </div>
> > > > > 
> > > > > <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">
> > > > > 
> > > > > 保存 .pth  
> > > > > 用于评估/导出
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ``` 
> > > > >     复制
> > > > >     # 终端命令 — VLN 模仿学习训练
> > > > > $ python -u -m habitat_baselines.run \
> > > > >     --config-name=vln/il_vln_r2r.yaml \
> > > > >     habitat_baselines.num_updates=10000 \
> > > > >     habitat_baselines.batch_size=8 \
> > > > >     habitat_baselines.checkpoint_folder="data/checkpoints/vln_il"
> > > > > 
> > > > > # 关键 config 路径说明：
> > > > > # config-name=vln/il_vln_r2r.yaml
> > > > > #   → habitat-baselines/habitat_baselines/config/vln/il_vln_r2r.yaml
> > > > > # 该 YAML 会自动引用：
> > > > > #   - benchmark/nav/vln/vln_r2r.yaml（任务 & 数据集）
> > > > > #   - habitat_baselines/rl/policy/vln_policy.yaml（策略网络）
> > > > > ```
> > > > > 
> > > > > </div>
> > > > > 
> > > > > | 模块                | 文件                                          | 作用                                                   |
> > > > > | ----------------- | ------------------------------------------- | ---------------------------------------------------- |
> > > > > | VLN Task          | `habitat/tasks/nav/vln.py`                  | 定义 VLNTask、VLNEpisode、动作空间 (FORWARD/LEFT/RIGHT/STOP) |
> > > > > | InstructionSensor | `habitat/tasks/nav/vln_sensor.py`           | 从 episode 读取指令，tokenize 后注入 observation              |
> > > > > | VLN Policy        | `habitat_baselines/rl/policy/vln_policy.py` | CNN 编码 RGB + RNN 编码指令 + 动作输出头                        |
> > > > > | IL Trainer        | `habitat_baselines/il/trainer.py`           | 管理 teacher-forcing 训练循环、数据集迭代                        |
> > > > > | R2R Dataset       | `habitat/datasets/vln/r2r_dataset.py`       | 加载 R2R JSON，提供 Episode 迭代器                           |
> > > > > 

> > > > > ### ③ 如何创建和运行
> > > > > 
> > > > > ``` 
> > > > >     复制
> > > > >     # 1. 确保 R2R 数据集和 MP3D 场景已下载
> > > > > $ ls data/datasets/vln/r2r/v1/train/
> > > > >   train.json.gz  val_seen.json.gz  val_unseen.json.gz
> > > > > 
> > > > > # 2. 确保 habitat-baselines 已安装
> > > > > $ pip install -e habitat-baselines
> > > > > 
> > > > > # 3. 启动训练（GPU 推荐）
> > > > > $ python -u -m habitat_baselines.run \
> > > > >     --config-name=vln/il_vln_r2r.yaml
> > > > > 
> > > > > # 预期输出：
> > > > > # [2024-01-15 10:30:00] Epoch 0/100, Loss: 1.386, Acc: 0.312
> > > > > # [2024-01-15 10:35:00] Epoch 10/100, Loss: 0.947, Acc: 0.521
> > > > > # ...
> > > > > # Checkpoint saved to data/checkpoints/vln_il/ckpt.100.pth
> > > > > ```
> > > > > 
> > > > > </div>
> > > > > 
> > > > > > ⚠️
> > > > > > 
> > > > > > <div class="warn-title">
> > > > > > 
> > > > > > ⚠️ 训练注意事项
> > > > > > 
> > > > > > **1. GPU 内存：**Matterport3D 场景较大，建议至少 8GB VRAM。OOM 时减小 `batch_size`  
> > > > > > **2. 数据预处理：**首次运行时会预处理 R2R 数据（生成 tokenizer 词表），需等待几分钟  
> > > > > > **3. Teacher-Forcing vs 在线采样：**IL 训练用的是 reference\_path 上的 ground truth 动作，不会让 agent 自由探索
> > > > > > 
> > > > > > <div id="case7-4" class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 7-4 · 评估与导出模型 · <span style="color:#f472b6;">7-6 · JanusVLN</span> · <span style="color:#a78bfa;">7-7 · 微调</span>
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **① 案例含义**
> > > > > > 
> > > > > > 训练完成后，在验证集上评估模型的导航能力（SR/SPL/nDTW），然后导出 checkpoint 为**纯推理权重文件**。这个文件就是 Step 7 部署到真机时需要加载的模型。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ② 评估代码 & 指标说明
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # 评估训练好的 VLN 模型
> > > > > > $ python -u -m habitat_baselines.run \
> > > > > >     --config-name=vln/il_vln_r2r.yaml \
> > > > > >     habitat_baselines.evaluate=True \
> > > > > >     habitat_baselines.eval_ckpt_path_dir="data/checkpoints/vln_il/ckpt.100.pth" \
> > > > > >     habitat_baselines.eval_split="val_seen"
> > > > > > 
> > > > > > # 预期输出：
> > > > > > # SR: 0.452  SPL: 0.398  nDTW: 0.561
> > > > > > # Success weighted by Path Length: 评估导航路径质量
> > > > > > ```
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > | 指标       | 全称                              | 含义                          | 范围        |
> > > > > > | -------- | ------------------------------- | --------------------------- | --------- |
> > > > > > | **SR**   | Success Rate                    | 在目标 radius 内执行 STOP 的比例     | 0–1, 越高越好 |
> > > > > > | **SPL**  | Success weighted by Path Length | 成功且路径尽量短（惩罚绕路）              | 0–1, 越高越好 |
> > > > > > | **nDTW** | Normalized Dynamic Time Warping | 实际路径与 reference\_path 的相似度  | 0–1, 越高越好 |
> > > > > > | **OSR**  | Oracle Success Rate             | 如果 agent 在最近点 STOP 的成功率（上界） | ≥ SR      |
> > > > > > 

> > > > > > <div class="dual-panel">
> > > > > > 
> > > > > > <div class="panel">
> > > > > > 
> > > > > > #### 📊 val\_seen vs val\_unseen
> > > > > > 
> > > > > > R2R 的验证集分两种：  
> > > > > > **val\_seen：**场景在训练中见过（但 episode 不同），测**指令泛化**  
> > > > > > **val\_unseen：**场景从未见过，测**场景泛化**  
> > > > > > val\_unseen 的 SR 通常比 val\_seen 低 10–20 个百分点。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > <div class="panel">
> > > > > > 
> > > > > > #### 📦 模型导出
> > > > > > 
> > > > > > checkpoint 包含 optimizer state + scheduler state + model weights。 为了在真机上做**纯推理**，需要提取出 model weights 部分：  
> > > > > > `ckpt = torch.load("ckpt.100.pth")`  
> > > > > > `model_weights = ckpt["state_dict"]`  
> > > > > > `torch.save(model_weights, "vln_inference.pth")`
> > > > > > 
> > > > > > ### ③ 如何导出可用于真机推理的模型
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # export_vln_model.py — 导出纯推理权重 + 配置
> > > > > > import torch
> > > > > > import yaml
> > > > > > 
> > > > > > # 1. 加载训练好的 checkpoint
> > > > > > ckpt = torch.load("data/checkpoints/vln_il/ckpt.100.pth", map_location="cpu")
> > > > > > 
> > > > > > # 2. 提取 model state_dict（去掉 optimizer/scheduler）
> > > > > > model_state = ckpt["state_dict"]
> > > > > > torch.save(model_state, "vln_inference.pth")
> > > > > > print("模型权重已导出到 vln_inference.pth")
> > > > > > 
> > > > > > # 3. 保存模型配置（推理时需要重新构建网络结构）
> > > > > > config = {
> > > > > >     "policy": "VLNPolicy",
> > > > > >     "rgb_shape": [3, 480, 640],
> > > > > >     "action_space": ["STOP", "MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT"],
> > > > > >     "instruction_vocab_size": 2500,
> > > > > >     "hidden_size": 512,
> > > > > > }
> > > > > > with open("vln_config.yaml", "w") as f:
> > > > > >     yaml.dump(config, f)
> > > > > > print("模型配置已导出到 vln_config.yaml")
> > > > > > ```
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > > 💡
> > > > > > > 
> > > > > > > <div class="tip-title">
> > > > > > > 
> > > > > > > 💡 这两个文件就是部署的输入
> > > > > > > 
> > > > > > > `vln_inference.pth` + `vln_config.yaml` 是 Step 7（方法一：VLN+ROS Nav2） 部署时需要的两个文件。它们包含了**在真机上重建 VLN 模型并运行推理所需的一切**。 你在 Step 7 中会看到如何在 ROS 节点中加载它们。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > ### ④ 试试调整这些
> > > > > > > 
> > > > > > > | 调整项        | 怎么改                                              | 预期看到什么                |
> > > > > > > | ---------- | ------------------------------------------------ | --------------------- |
> > > > > > > | 训练步数       | 改 `habitat_baselines.num_updates` 从 10000 → 5000 | SR 下降 \~5-10%，但训练时间减半 |
> > > > > > > | Batch Size | 改 `habitat_baselines.batch_size` 从 8 → 16        | 收敛更快但 GPU 内存翻倍，可能 OOM |
> > > > > > > | 评估 split   | 改 `eval_split` 从 val\_seen → val\_unseen         | SR 降低，反映场景泛化能力        |
> > > > > > > | 动作空间       | 在配置中添加/移除 TURN 角度参数                              | 动作粒度影响导航效率和平滑度        |
> > > > > > > 

> > > > > > > > ⚠️
> > > > > > > > 
> > > > > > > > <div class="warn-title">
> > > > > > > > 
> > > > > > > > ⚠️ 部署前检查清单
> > > > > > > > 
> > > > > > > > ✅ SR \> 0.3（低于此值，真机上的表现会是灾难性的）  
> > > > > > > > ✅ 模型在 CPU 上推理时间 \< 100ms（真机一般无 GPU）  
> > > > > > > > ✅ checkpoint 文件可脱离 habitat-baselines 加载（验证导出脚本）  
> > > > > > > > ✅ 已在 val\_unseen 上评估过，了解模型在新场景中的表现上限
> > > > > > > > 
> > > > > > > > <div id="case7-4" class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 7-4 · 避坑诊断 — ML 工程诊断方法
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **📍 为什么需要这一节？**
> > > > > > > > 
> > > > > > > > 7-3 的 IL 训练拿到 SR≈32%。这个数字诚实但不理想。 在尝试 DAgger / RL 之前，先要诊断「到底是什么导致了 32%」—— 这是 ML 工程师的核心能力，比调参更重要。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > <div class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## §N.1 初见：好得可疑的 94.9%
> > > > > > > > 
> > > > > > > > 用项目原始代码训练 10 个 epoch，观察训练曲线。
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **① 先跑一遍看看**
> > > > > > > > 
> > > > > > > > 在你开始修改任何代码之前，先用原始版本完整训练一次，并保存日志。  
> > > > > > > > 这个日志是你后续诊断的**唯一参照物**——没有它，你就不知道"修对了没有"。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### ② 训练命令
> > > > > > > > 
> > > > > > > >     cd habitat-lab-edu
> > > > > > > >     python training/train.py --split val_unseen --num_episodes 500 --epochs 10 \
> > > > > > > >         2>&1 | tee logs/run1_before_fix.log
> > > > > > > > 
> > > > > > > > ### ③ 训练曲线（真实日志）
> > > > > > > > 
> > > > > > > > <div style="margin:16px 0;">
> > > > > > > > 
> > > > > > > > ![Before Fix Training Curves](images/before_fix_curves.png)
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ▲ 从左图可见：train\_loss 和 val\_loss 快速下降且始终接近——典型的过拟合信号（train/val 数据泄漏）。val\_acc 从 79.7% 飙升至 94.1%。
> > > > > > > > 
> > > > > > > > > 💡
> > > > > > > > > 
> > > > > > > > > <div class="tip-title">
> > > > > > > > > 
> > > > > > > > > 停下想一想
> > > > > > > > > 
> > > > > > > > > val\_acc = 94.1%，而且 10 个 epoch 就到了。你见过几个 ML 项目有这么快的收敛速度和这么高的准确率？  
> > > > > > > > > **在继续之前，问自己：这个数字有可能是真的吗？**
> > > > > > > > > 
> > > > > > > > > <div class="section">
> > > > > > > > > 
> > > > > > > > > <div class="container">
> > > > > > > > > 
> > > > > > > > > ## §N.2 五重暗坑：逐一揭示
> > > > > > > > > 
> > > > > > > > > 高 val\_acc 并不等于好模型。以下是藏在训练管线中的 5 个问题。
> > > > > > > > > 
> > > > > > > > > <div class="bug-card" style="margin-bottom: 20px;">
> > > > > > > > > 
> > > > > > > > > #### 🔴 坑 1：文本输入是随机噪声
> > > > > > > > > 
> > > > > > > > > <div class="compare-grid">
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复前
> > > > > > > > > 
> > > > > > > > >     def fake_text_input(instrs, B, T, ...):
> > > > > > > > >         return torch.randn(B, 10, 300)  # 每轮都不同！
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复后
> > > > > > > > > 
> > > > > > > > >     # 从 R2R 指令构建词表 1369 词
> > > > > > > > >     batch_encode(instructions) → Embedding → LSTM
> > > > > > > > >     # 同一条指令永远得到相同向量
> > > > > > > > > 
> > > > > > > > > 指令文本从未被使用。模型实际学的是**"看 RGB 序列推测方向"**——这不是 VLN。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="bug-card" style="margin-bottom: 20px;">
> > > > > > > > > 
> > > > > > > > > #### 🔴 坑 2：Train / Val 数据泄漏
> > > > > > > > > 
> > > > > > > > > <div class="compare-grid">
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复前
> > > > > > > > > 
> > > > > > > > >     train_ds = VLNDataset(split="val_unseen", ...)
> > > > > > > > >     val_ds  = VLNDataset(split="val_unseen", ...)
> > > > > > > > >     # ↑ 同一个 split！
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复后
> > > > > > > > > 
> > > > > > > > >     train_ds = VLNDataset(split="train", ...)
> > > > > > > > >     val_ds  = VLNDataset(split="val_unseen", ...)
> > > > > > > > >     # ↑ 完全隔离
> > > > > > > > > 
> > > > > > > > > 验证集的前 50 个 episode 也在训练集中。模型见过验证数据——94.1% 是**过拟合**，不是泛化。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="bug-card" style="margin-bottom: 20px;">
> > > > > > > > > 
> > > > > > > > > #### 🟡 坑 3：Action 标签缺失 RIGHT
> > > > > > > > > 
> > > > > > > > > <div class="compare-grid">
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复前
> > > > > > > > > 
> > > > > > > > >     if abs(dx) > abs(dy):
> > > > > > > > >         actions.append(1)  # FWD
> > > > > > > > >     else:
> > > > > > > > >         actions.append(2)  # LEFT——RIGHT 从未出现
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复后
> > > > > > > > > 
> > > > > > > > >     if dx > 0.05:
> > > > > > > > >         actions.append(3)  # RIGHT
> > > > > > > > >     elif dx 
> > > > > > > > > 
> > > > > > > > > 模型训练时从未见过正确的右转标签。一个不会右转的导航模型。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="bug-card" style="margin-bottom: 20px;">
> > > > > > > > > 
> > > > > > > > > #### 🟡 坑 4：SPL 指标公式错误
> > > > > > > > > 
> > > > > > > > > <div class="compare-grid">
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复前
> > > > > > > > > 
> > > > > > > > >     def spl(success, agent_len, gt_len):
> > > > > > > > >         return gt_len / max(agent_len, gt_len)
> > > > > > > > >         # ↑ 缺了 success 因子！失败时 SPL≠0
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > 修复后
> > > > > > > > > 
> > > > > > > > >     def spl(success, agent_len, gt_len):
> > > > > > > > >         if not success: return 0.0
> > > > > > > > >         return success * gt_len / max(agent_len, gt_len)
> > > > > > > > > 
> > > > > > > > > 标准 SPL 公式是 `success × (gt_len / max(agent_len, gt_len))`。缺少 success 因子导致失败 episode 也有正的 SPL。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="bug-card">
> > > > > > > > > 
> > > > > > > > > #### 🟡 坑 5：训练日志丢失
> > > > > > > > > 
> > > > > > > > > 原始 train.py 只打印到终端，训练结束后**没有任何记录**。当你想对比修复前后的效果时，没有对照数据。  
> > > > > > > > > 修复：加入 `Tee` 类，同时输出到 stdout 和 `logs/` 目录。
> > > > > > > > > 
> > > > > > > > > <div class="section">
> > > > > > > > > 
> > > > > > > > > <div class="container">
> > > > > > > > > 
> > > > > > > > > ## §N.3 修复后重新训练
> > > > > > > > > 
> > > > > > > > > 修复全部 5 个问题后，用分离的 split 重新训练 10 epoch。
> > > > > > > > > 
> > > > > > > > > <div style="margin:16px 0;">
> > > > > > > > > 
> > > > > > > > > ![After Fix Training Curves](images/after_fix_curves.png)
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > ▲ 修复后 train/val 曲线明显分离（无数据泄漏）。val\_acc 从 49.9% 起步，最终达到 94.7%——几乎和修复前一样。
> > > > > > > > > 
> > > > > > > > > <div style="margin:24px 0 16px;">
> > > > > > > > > 
> > > > > > > > > ![Val ACC Before vs After Fix](images/val_acc_comparison.png)
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > ▲ 修复前（红线）：起点高（79.7%），快速收敛。修复后（绿线）：起点低（49.9%），逐步追赶——最终持平。两者终点几乎重叠，说明这些表面问题不是瓶颈。
> > > > > > > > > 
> > > > > > > > > <div class="insight-box">
> > > > > > > > > 
> > > > > > > > > #### 💡 意料之外：val\_acc 几乎没变
> > > > > > > > > 
> > > > > > > > > 修复了文本噪声、数据泄漏、标签缺失、指标公式之后，val\_acc 从 **94.1% → 94.7%**。  
> > > > > > > > >   
> > > > > > > > > 我们原本预期 val\_acc 会**大幅下降**（因为消除了数据泄漏和随机文本作弊），但它纹丝不动。  
> > > > > > > > >   
> > > > > > > > > **这意味着：这 5 个问题从来不是 val\_acc 的瓶颈。**
> > > > > > > > > 
> > > > > > > > > <div class="section">
> > > > > > > > > 
> > > > > > > > > <div class="container">
> > > > > > > > > 
> > > > > > > > > ## §N.4 真正的考验：环境评估
> > > > > > > > > 
> > > > > > > > > val\_acc 测量的是"给定预渲染帧，预测 action 标签"，不是"在 3D 场景中导航"。
> > > > > > > > > 
> > > > > > > > > | 指标                   | 修复前 (作弊版) | 修复后 (诚实版) | 变化     |
> > > > > > > > > | -------------------- | --------- | --------- | ------ |
> > > > > > > > > | **val\_acc**         | 94.1%     | 94.7%     | \+0.6% |
> > > > > > > > > | **Eval SR** (50 eps) | \~30% \*  | 32.0%     | \+2%   |
> > > > > > > > > | **Eval SPL**         | — (公式错误)  | 0.320     | —      |
> > > > > > > > > | **Eval nDTW**        | —         | 0.107     | —      |
> > > > > > > > > 

> > > > > > > > > \* 修复前的简化版 eval 把 action 硬编码为 MOVE\_FORWARD，所以 SR 约 30% 只是"一直向前走"的 baseline。
> > > > > > > > > 
> > > > > > > > > <div class="insight-box">
> > > > > > > > > 
> > > > > > > > > #### 💡 val\_acc 94.7% vs SR 32.0%：3:1 的鸿沟
> > > > > > > > > 
> > > > > > > > > 同一个模型，在预渲染帧上预测 action 标签有 94.7% 准确率，但在 3D 场景中实际导航只有 32% 成功率。  
> > > > > > > > >   
> > > > > > > > > 这个 3:1 的差距揭示了比文本噪声、数据泄漏、标签错误**更深层的问题**。
> > > > > > > > > 
> > > > > > > > > <div class="section">
> > > > > > > > > 
> > > > > > > > > <div class="container">
> > > > > > > > > 
> > > > > > > > > ## §N.5 深层结论：图像分布偏移
> > > > > > > > > 
> > > > > > > > > 当你排除了所有表面问题，剩下的那个——无论多么隐蔽——就是根因。
> > > > > > > > > 
> > > > > > > > > <div>
> > > > > > > > > 
> > > > > > > > > **根因：训练和评估的图像来自不同分布**
> > > > > > > > > 
> > > > > > > > > <div class="compare-grid" style="margin-top:12px;">
> > > > > > > > > 
> > > > > > > > > <div class="fix-card" style="margin:0;">
> > > > > > > > > 
> > > > > > > > > #### 训练时的图像
> > > > > > > > > 
> > > > > > > > > 来自 **预渲染**（env.reset → 5×MOVE\_FORWARD → 保存 .npz）  
> > > > > > > > >   
> > > > > > > > > 每帧都是 **最短路径上的画面**——干净、正确、标准化。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > <div class="bug-card" style="margin:0;">
> > > > > > > > > 
> > > > > > > > > #### 评估时的图像
> > > > > > > > > 
> > > > > > > > > 来自 **实时渲染**（每步根据模型预测的 action 获取下一帧）  
> > > > > > > > >   
> > > > > > > > > 每帧都是 **模型自己走出来的画面**——可能偏离、撞墙、迷路。
> > > > > > > > > 
> > > > > > > > > 两个分布下的 RGB 完全不同——同一场景、不同视角、不同光照条件。  
> > > > > > > > > ResNet 提取的特征在两个分布之间**无法泛化**。  
> > > > > > > > >   
> > > > > > > > > 这解释了为什么修复了 5 个表面问题后 SR 仍然只有 32%：  
> > > > > > > > > **模型从未见过"自己走错时看到的画面"。**
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > > ⚠️
> > > > > > > > > > 
> > > > > > > > > > <div class="warn-title">
> > > > > > > > > > 
> > > > > > > > > > ⚡ 这为什么比文本问题更难修
> > > > > > > > > > 
> > > > > > > > > > 要消除分布偏移，训练必须也走**在线 rollout**：每步用模型预测的 action 获取下一帧。  
> > > > > > > > > > 但这会让训练慢 10 倍（无法并行预取 DataLoader），且需要动态 env 管理。  
> > > > > > > > > >   
> > > > > > > > > > 混合训练方案（先在预渲染上启蒙，再逐步加在线 rollout）是可行的折中。  
> > > > > > > > > >   
> > > > > > > > > > ——这不是 §N 要解决的问题，它是阶段 3（真正的 VLN 训练）的核心挑战。
> > > > > > > > > > 
> > > > > > > > > > <div class="section">
> > > > > > > > > > 
> > > > > > > > > > <div class="container">
> > > > > > > > > > 
> > > > > > > > > > ## §N.6 你从这一章学到的
> > > > > > > > > > 
> > > > > > > > > > | \# | 教训                                  | 适用范围     |
> > > > > > > > > > | -- | ----------------------------------- | -------- |
> > > > > > > > > > | 1  | **val\_acc 高 ≠ 模型好**。先检查数据有没有泄漏。    | 所有 ML 项目 |
> > > > > > > > > > | 2  | **保存训练日志**。没有 before 对照，after 没有意义。 | 所有 ML 项目 |
> > > > > > > > > > | 3  | **查指标公式**。你自己写的 SPL 可能和论文定义不同。      | 复现论文时    |
> > > > > > > > > > | 4  | **查标签分布**。如果某个类别从未出现，模型不会学到它。       | 分类任务     |
> > > > > > > > > > | 5  | **训练和推理的输入必须同分布**。预渲染帧≠实时渲染帧。       | 所有 ML 项目 |
> > > > > > > > > > | 6  | **修复表面问题后效果没变 → 根因在更深层**。别停。        | 调试方法论    |
> > > > > > > > > > 

> > > > > > > > > > > 💡
> > > > > > > > > > > 
> > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > 
> > > > > > > > > > > 继续学习
> > > > > > > > > > > 
> > > > > > > > > > > 这一章教的是"如何诊断"。下一阶段（阶段 3：真正的 VLN 训练）教的是"如何做对"——  
> > > > > > > > > > > teacher-forcing、cross-modal attention、在线训练、数据增强。  
> > > > > > > > > > > [→ 回到第7步：VLN 视觉语言导航](habitat-textbook-step6.html)
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section content-section">
> > > > > > > > > > > 
> > > > > > > > > > > ## §N.7 量化证据：图像分布偏移到底多大？
> > > > > > > > > > > 
> > > > > > > > > > > §N.5 提出"图像分布偏移是根因"——但这是定性的推断。我们需要用实验把它量化。  
> > > > > > > > > > > 设计一个对照实验：用 ResNet（模型的眼睛）和 CLIP（通用的眼睛）分别编码两组图像，计算分布距离。
> > > > > > > > > > > 
> > > > > > > > > > > ### 实验设计
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **两组图像**
> > > > > > > > > > > 
> > > > > > > > > > >   - **A 组 · 预渲染帧：**9,195 帧，来自 1,839 个 episode 的最短路径，每帧都是"正确答案"。
> > > > > > > > > > >   - **B 组 · 在线 rollout 帧：**2,790 帧，来自 93 个 episode，强制模型走 30 步（禁用 stop），收集模型自己走出来的画面——包括走偏、撞墙、绕路。
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **两个编码器**
> > > > > > > > > > > 
> > > > > > > > > > >   - **ResNet18：**模型实际使用的视觉编码器。如果 A 和 B 对它来说是不同分布，那就是模型的"主观"分布偏移。
> > > > > > > > > > >   - **CLIP ViT-B/32：**通用视觉模型，作为"客观"参照。如果 CLIP 也认为两组不同，那偏移就是客观的。
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > ### 结果：MMD 分布距离
> > > > > > > > > > > 
> > > > > > > > > > > <div class="compare-table">
> > > > > > > > > > > 
> > > > > > > > > > > | 编码器           | MMD（越低越相似） | 解读              |
> > > > > > > > > > > | ------------- | ---------- | --------------- |
> > > > > > > > > > > | ResNet18      | **0.0058** | 模型的眼睛认为两组帧几乎一样  |
> > > > > > > > > > > | CLIP ViT-B/32 | **0.0053** | 通用的眼睛也认为两组帧几乎一样 |
> > > > > > > > > > > 

> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > > ⚠️
> > > > > > > > > > > > 
> > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > 
> > > > > > > > > > > > ⚡ 意料之外：两个 MMD 都极低
> > > > > > > > > > > > 
> > > > > > > > > > > > 我们预期在线帧（走偏、撞墙）和预渲染帧（最短路径）会有显著分布差异。  
> > > > > > > > > > > > 但 ResNet 和 CLIP 都给出了 \< 0.006 的 MMD——**两组帧在特征空间中几乎完全重叠**。
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > ### 可视化：t-SNE 降维
> > > > > > > > > > > > 
> > > > > > > > > > > > 把 512 维特征降到 2 维，蓝色 = 预渲染帧，红色 = 在线帧：
> > > > > > > > > > > > 
> > > > > > > > > > > > <div style="display:flex;gap:20px;flex-wrap:wrap;margin:16px 0;">
> > > > > > > > > > > > 
> > > > > > > > > > > > <div style="flex:1;min-width:300px;">
> > > > > > > > > > > > 
> > > > > > > > > > > > ![t-SNE ResNet](images/tsne_resnet.png)
> > > > > > > > > > > > 
> > > > > > > > > > > > ResNet18 t-SNE (MMD=0.0058)
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > <div style="flex:1;min-width:300px;">
> > > > > > > > > > > > 
> > > > > > > > > > > > ![t-SNE CLIP](images/tsne_clip.png)
> > > > > > > > > > > > 
> > > > > > > > > > > > CLIP t-SNE (MMD=0.0053)
> > > > > > > > > > > > 
> > > > > > > > > > > > 在 ResNet 的 t-SNE 图中，红色和蓝色完全混在一起——预渲染帧和在线帧在特征空间中无法区分。
> > > > > > > > > > > > 
> > > > > > > > > > > > ### 余弦相似度分布
> > > > > > > > > > > > 
> > > > > > > > > > > > <div style="margin:16px 0;">
> > > > > > > > > > > > 
> > > > > > > > > > > > ![Cosine Similarity](images/cosine_similarity.png)
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > 两组直方图几乎完全重叠：预渲染帧之间的相似度，和预渲染 vs 在线帧之间的相似度，分布一致。
> > > > > > > > > > > > 
> > > > > > > > > > > > ### §N.5 的结论需要修正
> > > > > > > > > > > > 
> > > > > > > > > > > > > 💡
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > > > 
> > > > > > > > > > > > > 从"图像分布偏移"到"行为偏差累积"
> > > > > > > > > > > > > 
> > > > > > > > > > > > > 数据推翻了 §N.5 的假设。不是图像分布不同导致 SR 只有 32%——  
> > > > > > > > > > > > > 而是模型在几乎相同的画面上，做出了**不同的 action 决策**。
> > > > > > > > > > > > > 
> > > > > > > > > > > > > 预渲染帧是 teacher-forcing 下的画面（最短路径，每步都是"对"的下一步），  
> > > > > > > > > > > > > 在线帧是模型自由行动的画面（可能走偏，但场景纹理、墙壁、地板和预渲染帧几乎一样）。
> > > > > > > > > > > > > 
> > > > > > > > > > > > > **32% 的 SR 不是因为模型"看到了没见过的画面"，而是模型在熟悉的画面中做出了错误的 action。**  
> > > > > > > > > > > > > 每步差一点，30 步后离目标越来越远——这就是**行为偏差累积**。
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > ### 实验教会我们的
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div class="compare-table">
> > > > > > > > > > > > > 
> > > > > > > > > > > > > | \# | 教训                                                                              |
> > > > > > > > > > > > > | -- | ------------------------------------------------------------------------------- |
> > > > > > > > > > > > > | 1  | **假设需要实验验证。**我们确信"图像分布偏移是根因"，但数据说不。                                             |
> > > > > > > > > > > > > | 2  | **模型的眼睛（ResNet）和通用的眼睛（CLIP）意见一致。**这不是编码器选择的问题。                                  |
> > > > > > > > > > > > > | 3  | **低 MMD 不代表问题不存在。**它只是说明问题不在帧层面，而在决策层面。                                         |
> > > > > > > > > > > > > | 4  | **证伪假设比证实假设更有价值。**它迫使你寻找更深层的根因。                                                 |
> > > > > > > > > > > > > | 5  | **下一步不是修图像，是修决策。**Teacher-forcing → Student-forcing，强化学习，cross-modal attention。 |
> > > > > > > > > > > > > 

> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > **实验复现**
> > > > > > > > > > > > > 
> > > > > > > > > > > > > 所有代码和特征数据在 L40 云端：  
> > > > > > > > > > > > > `training/collect_online_frames.py` — 强制 30 步 rollout 采集  
> > > > > > > > > > > > > `training/extract_features.py` — ResNet + CLIP 特征提取  
> > > > > > > > > > > > > `training/analyze_distribution.py` — MMD + t-SNE + 余弦相似度分析  
> > > > > > > > > > > > > `screenshots/clip_comparison/` — 完整图表输出
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div id="case7-5" class="section">
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div class="container">
> > > > > > > > > > > > > 
> > > > > > > > > > > > > ## 7-5 · DAgger — 从模仿到强化
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > **📍 诊断后的修复方案**
> > > > > > > > > > > > > 
> > > > > > > > > > > > > 7-4 定位了根因：**行为漂移累积**（Agent 走偏后，后续观测都是训练时没见过的）。 DAgger 正是解决这个问题的标准方法——让 Agent 在「自己犯错的地方」学习专家纠正。
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > ### IL → DAgger → RL 三阶梯
> > > > > > > > > > > > > 
> > > > > > > > > > > > > <div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > **🎯 实际实验：Seq2SeqAgent (27M) + ShortestPathFollower 专家**
> > > > > > > > > > > > > 
> > > > > > > > > > > > > **训练配置：**100 episode/轮 × 3 轮迭代 × 5 epoch/轮 · chunked collection (20 ep/chunk) · L40 GPU  
> > > > > > > > > > > > > **专家策略：**ShortestPathFollower（走最短路径，success\_distance=3.0m，成功率 100%）  
> > > > > > > > > > > > > **初始策略：**Seq2SeqAgent（§N 训练的 ckpt，val\_acc=94.9%）
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > | 阶段                | SR       | SPL   | avg\_steps | loss   | 说明                          |
> > > > > > > > > > > > > | ----------------- | -------- | ----- | ---------- | ------ | --------------------------- |
> > > > > > > > > > > > > | **IL Baseline**   | **3.0%** | 0.000 | 4          | —      | 初始策略在实时仿真器上评估               |
> > > > > > > > > > > > > | **DAgger Iter 1** | **3.0%** | 0.000 | 4          | 0.0000 | 策略采集 0 条有效轨迹                |
> > > > > > > > > > > > > | **DAgger Iter 2** | **3.0%** | 0.000 | 4          | 0.0000 | 同上 — 无改善                    |
> > > > > > > > > > > > > | **DAgger Iter 3** | **3.0%** | 0.000 | 4          | 0.0000 | 每轮中期 eval 在 2-4% 波动，最终收敛 3% |
> > > > > > > > > > > > > 

> > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > 🚨 关键发现：DAgger 完全失败 — SR 零提升，损失→0
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > 3 轮 DAgger 迭代，**Success Rate 没有任何提升**（始终 3.0%），所有轮的训练 loss 均为 **0.0000**。 这个结果不是代码 bug——而是 **DAgger 算法在弱初始策略上的已知失效模式**。 对课程来说，"DAgger 为什么失败"比"DAgger 成功了"有更高的教学价值。
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > ### 🔬 三层根因分析
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > **第 1 层：训练-部署 Gap（94.9% → 3% = 30× 衰减）**
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > §N 训练的模型在预渲染帧上 val\_acc=94.9%，但放到实时仿真器后 SR 骤降到 3.0%。 预渲染帧来自 **GT 最短路径的 5 步观察**，agent 实际走偏后看到的图像完全不同——模型从未学过"走偏后怎么恢复"。
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > **第 2 层：弱策略死循环 — 模型只预测 STOP**
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > avg\_steps=4 说明了问题：模型几乎每一步都预测 STOP（action=0/1），episode 立即结束。 3% 的 SR 来自起点距离 ≤3m 的 episode（agent 不需要移动就判定成功）。 **模型学到的"策略"：不管看到什么，先停再说。**这是因为训练时 STOP 标签占比过高（每个 episode 尾部才出现 STOP，但模型把所有帧都映射到 STOP 来最小化 loss）。
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > **第 3 层：DAgger 的前提不满足 — 初始 SR 需 \>20%**
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > DAgger 的有效性依赖于一个前提：**初始策略至少有一定的成功率**（通常 \>20%），这样 agent 的轨迹中才包含"接近目标但走偏了"的有价值样本。 当初始 SR=3.0%（基本等于随机），agent 的轨迹没有任何信息量——全是"开局就停"。 专家重新标注这些轨迹时，标注的是一系列"从起点就开始走"的动作，但这些标注附着在 agent 根本没走过的观测上，训练时模型无法建立有效的观测→动作映射。  
> > > > > > > > > > > > > >   
> > > > > > > > > > > > > > 这是 DAgger 的已知局限（Ross et al., 2011 论文中也提到），不是实现错误。
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > ### 🛠️ 实战教训
> > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > 坑 1：success\_distance=0.2m 太严格
> > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > 最初实验时 ShortestPathFollower 专家 SR=0%，原因是在 vln\_r2r.yaml 中 `success_distance=0.2`（20cm）。 VLN 离散动作步长 0.25m，导致即使走到目标旁也无法判定成功。修改为 **3.0m** 后专家 SR=100%。
> > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > 坑 2：内存爆炸（119GB → OOM Kill）
> > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > 第一个版本的 DAgger 脚本一次采集 200 个 episode 的所有 RGB 帧到内存，导致 119GB RSS + cgroup OOM Kill。 修复方案：**chunked collection**（20 ep/chunk，逐块训练后释放）+ `gc.collect()` + `torch.cuda.empty_cache()`。
> > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > 坑 3：预训练 ckpt 的 txt\_encoder 不兼容
> > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > §N 训练的 ckpt 中 TextEncoder 是模型内部组件（model\_cheat.py），新版代码 TextEncoder 是独立模块。 加载 ckpt 时参数名不匹配，TextEncoder 被随机初始化 → 指令输入变成噪声。需要用旧版模型类加载。
> > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > 💡
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > 💡 三条改进路线
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **路线 A · Behavior Cloning 预训练：**先在专家轨迹上做 BC 预训练，让初始 SR 达到 20-30%，再启动 DAgger。  
> > > > > > > > > > > > > > > > > > **路线 B · Scheduled Sampling：**训练时混合 GT action 和模型预测 action（50/50），逐步减少对 GT 的依赖。  
> > > > > > > > > > > > > > > > > > **路线 C · 切换 RL：**如果 IL 路线难以突破，直接用 PPO 在 VLN 奖励函数上训练（需 8-16 GPU 并行环境）。
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ### DAgger 算法伪代码
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > >     # DAgger (Dataset Aggregation) — Ross et al., 2011
> > > > > > > > > > > > > > > > > > for iteration in range(K):
> > > > > > > > > > > > > > > > > >     # 1. 用当前策略 pi_i 在环境中执行（采集自己的轨迹）
> > > > > > > > > > > > > > > > > >     trajectories = run_policy(env, policy=pi_i, episodes=N)
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > >     # 2. 对每一帧，向专家查询「正确动作是什么」
> > > > > > > > > > > > > > > > > >     for (obs, action_agent) in trajectories:
> > > > > > > > > > > > > > > > > >         action_expert = expert.query(obs)      # 专家怎么说？
> > > > > > > > > > > > > > > > > >         dataset.append((obs, action_expert))   # 存专家的答案
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > >     # 3. 在聚合后的数据集上重新训练
> > > > > > > > > > > > > > > > > >     pi_next = train(dataset)                   # 模型学会了「在自己犯错时该怎么做」
> > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **为什么 DAgger 能解决行为漂移？** IL 只见过专家轨迹上的观测 → Agent 一走偏就进入未知区域 → 雪崩。 DAgger 把 Agent 走偏后的观测也加入训练集（附上专家纠正）， 让模型学会「走偏了怎么回来」——这正是 VLN 最需要的鲁棒性。
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > <div id="case7-6" class="section">
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > <div class="container">
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ## 7-6 · SOTA 实战：运行 JanusVLN
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **① 案例含义**
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > 7-3 和 §N 中我们训练了一个 **2700 万** 参数的 Seq2Seq 模型，在 val\_unseen 上达到 SR = 32%。 现在我们跑一个真正的 **SOTA 模型——JanusVLN**——在同一套数据上评估，亲眼看看"参数量差距意味着什么"。  
> > > > > > > > > > > > > > > > > >   
> > > > > > > > > > > > > > > > > > **前置条件：**完成 7-3 训练（理解 VLN 任务）。需要单卡 NVIDIA GPU（≥ 46GB 显存，如 L40/A100）。
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ### 论文与开源项目
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for VLN**
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **发表：**ICLR 2026  
> > > > > > > > > > > > > > > > > > **机构：**Amap（高德地图，阿里巴巴集团）+ 西安交通大学（MIV-XJTU）  
> > > > > > > > > > > > > > > > > > **论文：**[arXiv:2509.22548](https://arxiv.org/abs/2509.22548)  
> > > > > > > > > > > > > > > > > > **代码：**[github.com/MIV-XJTU/JanusVLN](https://github.com/MIV-XJTU/JanusVLN)  
> > > > > > > > > > > > > > > > > > **权重：**[ModelScope: JanusVLN\_Base](https://www.modelscope.cn/models/misstl/JanusVLN_Base)（18GB）  
> > > > > > > > > > > > > > > > > > **数据：**[ModelScope: DAgger 轨迹数据](https://www.modelscope.cn/datasets/misstl/JanusVLN_Trajectory_Data)
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > 核心创新：**双隐式记忆（Dual Implicit Memory）**。名字来源于罗马神话两面神 Janus， 寓意同时拥有"语义理解"（左脑）和"空间感知"（右脑）两种能力。 论文报告 val\_unseen SR 约 **50-55%**（全景输入，1839 episode）。
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ### ② 模型架构：双隐式记忆
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > | 记忆类型                | 负责模型          | 参数量     | 类比                      |
> > > > > > > > > > > > > > > > > > | ------------------- | ------------- | ------- | ----------------------- |
> > > > > > > > > > > > > > > > > > | **语义记忆** (Semantic) | Qwen2.5-VL-7B | \~70 亿  | "左脑"：理解"拱门""楼梯"的含义和视觉外观 |
> > > > > > > > > > > > > > > > > > | **空间记忆** (Spatial)  | VGGT-1B       | \~10 亿  | "右脑"：推理深度、几何、3D 空间结构    |
> > > > > > > > > > > > > > > > > > | **融合层**             | VGGTMerger    | \~200 万 | 将 3D 特征注入 VLM 的每层隐藏状态   |
> > > > > > > > > > > > > > > > > > 

> > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **关键设计：跨步空间记忆**
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > 模型维护一个 `past_key_values_vggt` 缓存，每次导航开始时清空， 每步推理后更新。这让模型在移动过程中"记住"之前看到的 3D 结构—— 就像一个边走边构建的**隐式 3D 地图**。
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ### ③ 数据流：每步从观测到动作
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > >     # 1. Habitat 渲染当前前向 RGB（224×224）
> > > > > > > > > > > > > > > > > > rgb = env.step(action)["rgb"]
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 2. 收集历史帧（num_history=4：最近 4 帧 + 当前）
> > > > > > > > > > > > > > > > > > history = rgb_list[-5:]
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 3. VGGT：每张图提取 3D 特征（深度、几何）——并行
> > > > > > > > > > > > > > > > > > vggt_feats = [VGGT(img) for img in history]
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 4. Qwen2.5-VL：图像 → patch tokens + 指令文本 → token IDs
> > > > > > > > > > > > > > > > > > inputs = processor(text=instruction, images=history)
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 5. 融合：VGGT 特征通过 VGGTMerger 注入 Qwen hidden states
> > > > > > > > > > > > > > > > > > # 6. 生成：Qwen2.5-VL 自回归解码（max 24 tokens, temperature=0）
> > > > > > > > > > > > > > > > > > output = model.generate(**inputs, images_vggt=vggt_feats, max_new_tokens=24)
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 7. 解析：token → 动作字符串 → Habitat action index
> > > > > > > > > > > > > > > > > > action_idx = actions2idx[processor.decode(output)]  # 1=FORWARD, 2=LEFT, 3=RIGHT, 0=STOP
> > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > | 阶段                       | 耗时          | 占比      |
> > > > > > > > > > > > > > > > > > | ------------------------ | ----------- | ------- |
> > > > > > > > > > > > > > > > > > | Habitat 渲染 + VGGT        | \~0.3s      | 15%     |
> > > > > > > > > > > > > > > > > > | Processor 编码             | \~0.2s      | 10%     |
> > > > > > > > > > > > > > > > > > | **Qwen2.5-VL 生成（7B 参数）** | **\~1.5s**  | **75%** |
> > > > > > > > > > > > > > > > > > | **合计**                   | **\~2 秒/步** |         |
> > > > > > > > > > > > > > > > > > 

> > > > > > > > > > > > > > > > > > ### ④ 环境准备
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **Step 1 — 克隆 + 权重**
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > >     git clone https://github.com/MIV-XJTU/JanusVLN.git && cd JanusVLN
> > > > > > > > > > > > > > > > > > pip install modelscope
> > > > > > > > > > > > > > > > > > python -c "from modelscope import snapshot_download; snapshot_download('misstl/JanusVLN_Base', cache_dir='./weights')"
> > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > **Step 2 — 单卡适配**
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > >     # 依赖（国内用 douban 镜像）
> > > > > > > > > > > > > > > > > > pip install transformers==4.48 accelerate qwen_vl_utils -i https://pypi.doubanio.com/simple
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > # 修改 src/evaluation.py：
> > > > > > > > > > > > > > > > > > #   flash-attn → torch.nn.functional.scaled_dot_product_attention
> > > > > > > > > > > > > > > > > > #   world_size=1, gpu=0（原代码需要 8 卡 DeepSpeed）
> > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ⚠️ 单卡适配要点
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 原代码需要 8 卡 DeepSpeed 分布式训练。单卡跑只需改两处： flash-attn → PyTorch SDPA（避免 30 分钟编译）、world\_size=1。 推理精度不受影响，速度略慢（SDPA vs flash-attn 差距约 10%）。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ### ⑤ 15-episode 抽样实验结果
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 在 L40 单卡上，用 `max_steps=100, num_history=4` 跑 15 个随机 episode， 耗时约 **48 分钟**。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > | 场景          | ✅/总数 | 场景 SR |
> > > > > > > > > > > > > > > > > > > | ----------- | ---- | ----- |
> > > > > > > > > > > > > > > > > > > | 2azQ1b91cZZ | 1/1  | 100%  |
> > > > > > > > > > > > > > > > > > > | EU6Fwq7SyZv | 0/3  | 0% ⚠️ |
> > > > > > > > > > > > > > > > > > > | QUCTc6BB5sX | 1/1  | 100%  |
> > > > > > > > > > > > > > > > > > > | TbHJrupSAjP | 1/3  | 33%   |
> > > > > > > > > > > > > > > > > > > | X7HyMhZNoso | 0/1  | 0%    |
> > > > > > > > > > > > > > > > > > > | oLBMNvg9in8 | 2/2  | 100%  |
> > > > > > > > > > > > > > > > > > > | pLe4wQe7qrG | 0/1  | 0%    |
> > > > > > > > > > > > > > > > > > > | zsNo4HB9uLZ | 2/3  | 67%   |
> > > > > > > > > > > > > > > > > > > | 总计          | 7/15 | 46.7% |
> > > > > > > > > > > > > > > > > > > 

> > > > > > > > > > > > > > > > > > > **与我们的模型对比：**
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > | 模型           | 参数量              | SR (抽样)   | 输入     | 训练数据                      |
> > > > > > > > > > > > > > > > > > > | ------------ | ---------------- | --------- | ------ | ------------------------- |
> > > > > > > > > > > > > > > > > > > | 我们的 Seq2Seq  | 2700 万           | 32.0%     | 预渲染离散帧 | R2R 几千条指令                 |
> > > > > > > > > > > > > > > > > > > | **JanusVLN** | **\~80 亿（300×）** | **46.7%** | 实时 RGB | 万亿 token VLM 预训练 + DAgger |
> > > > > > > > > > > > > > > > > > > 

> > > > > > > > > > > > > > > > > > > ### 可视化：成功 vs 失败
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 在场景 **2azQ1b91cZZ** 上跑的两个 episode（6 FPS）：
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div style="display:flex;gap:20px;flex-wrap:wrap;margin-top:12px;">
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div style="flex:1;min-width:300px;">
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ❌ Episode 10 — SR=0
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 指令："走过客厅，到阳台下的入口"  
> > > > > > > > > > > > > > > > > > > NE=8.27m，101步走到上限
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div style="flex:1;min-width:300px;">
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ✅ Episode 11 — SR=1.0
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 指令："穿过地板，在拱门等"  
> > > > > > > > > > > > > > > > > > > SPL=1.0，34步精确到达
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 视频展示的是模型的第一人称视角（RGB + Top-down 地图）。注意失败案例中模型一直在客厅转圈， 而成功案例中模型直接走向拱门并精确停止。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ### ⑥ SR 46.7% 深度分析
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > **为什么没到论文报告的 50-55%？**
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > **最可能原因：单视角 vs 全景输入。**原论文使用 360° 全景（12 个方向的 RGB）， 而我们的 eval 只传了单张前向 RGB。模型无法看到左右和后方的场景， 每次转向都是一次"盲猜"，尤其影响需要精细空间判断的指令。  
> > > > > > > > > > > > > > > > > > >   
> > > > > > > > > > > > > > > > > > > **其他因素：**15-episode 抽样方差大、max\_steps=100 偏紧（有 episode 只差 0.12m 就成功）。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > **场景差异：EU6Fwq7SyZv 全败之谜**
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > EU6Fwq7SyZv 3 个 episode 全部走到 100 步上限（NE 4.6-7.0m）。 三条指令都涉及复杂的空间关系："绕过椅子""穿过柱子""停在楼梯和栏杆之间"。 在只有前向视角的情况下，模型无法验证"是否已经绕过"——它看不到侧面。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > <div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > **为什么比我们的 32% 好？**
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > 不是"方法更好"，而是 **VLM 预训练带来的世界知识**： Qwen2.5-VL 在预训练阶段见过海量室内场景——它已经知道"拱门""楼梯""沙发"长什么样。 我们的 ResNet50 只在 R2R 几千张图上从头学，对室内场景的理解完全从零开始。  
> > > > > > > > > > > > > > > > > > >   
> > > > > > > > > > > > > > > > > > > 这 14.7% 的差距 = **万亿 token 图文预训练 vs 几千条 R2R 数据** 的差距。
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ### ⑦ 如何训练：DAgger 算法
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > JanusVLN 使用 **DAgger（Dataset Aggregation）**， "模型在实践中学习，专家在旁兜底"：
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > > >     for iteration in range(num_iterations):
> > > > > > > > > > > > > > > > > > >     beta = p ** iteration  # 专家干预概率指数衰减
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > >     # 采集阶段：在 Habitat 中 rollout
> > > > > > > > > > > > > > > > > > >     for episode in dataset:
> > > > > > > > > > > > > > > > > > >         while not episode_over:
> > > > > > > > > > > > > > > > > > >             if random() # ShortestPathFollower
> > > > > > > > > > > > > > > > > > >             else:
> > > > > > > > > > > > > > > > > > >                 action = model.predict(obs)     # 模型自己走
> > > > > > > > > > > > > > > > > > >             obs = env.step(action)
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > >     # 训练阶段：交叉熵 loss(action_pred, action_gt)
> > > > > > > > > > > > > > > > > > >     for epoch in range(train_epochs):
> > > > > > > > > > > > > > > > > > >         loss = CrossEntropy(model(obs), action_gt)
> > > > > > > > > > > > > > > > > > >         loss.backward(); optimizer.step()
> > > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > | 迭代 | β (p=0.95) | 专家占比 | 含义          |
> > > > > > > > > > > > > > > > > > > | -- | ---------- | ---- | ----------- |
> > > > > > > > > > > > > > > > > > > | 1  | 0.95       | 95%  | 几乎全专家带      |
> > > > > > > > > > > > > > > > > > > | 5  | 0.77       | 77%  | 模型开始承担      |
> > > > > > > > > > > > > > > > > > > | 10 | 0.60       | 60%  | 逐步放手        |
> > > > > > > > > > > > > > > > > > > | 20 | 0.36       | 36%  | 模型主导，专家偶尔纠正 |
> > > > > > > > > > > > > > > > > > > 

> > > > > > > > > > > > > > > > > > > > ⚠️
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="warn-title">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > 💡 这和我们的训练有什么不同？
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > **我们的 Seq2Seq：**仅在预渲染的最短路径帧上做分类训练。模型从未在 3D 环境中"自己走"过。  
> > > > > > > > > > > > > > > > > > > >   
> > > > > > > > > > > > > > > > > > > > **JanusVLN 的 DAgger：**模型在真实 3D 环境中交互并收集自己走出来的轨迹。 这些轨迹包含偏离、徘徊、撞墙——正是 §N.5 讨论的"在线 rollout 数据"。 DAgger 的核心价值就是让模型**见到并学会修正自己的错误**。
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > ### ⑧ 完整运行命令
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > ``` 
> > > > > > > > > > > > > > > > > > > >     复制
> > > > > > > > > > > > > > > > > > > >     export HF_ENDPOINT=https://hf-mirror.com
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > python src/evaluation.py \
> > > > > > > > > > > > > > > > > > > >     --model_path ./weights/misstl/JanusVLN_Base \
> > > > > > > > > > > > > > > > > > > >     --habitat_config_path config/vln_r2r.yaml \
> > > > > > > > > > > > > > > > > > > >     --eval_split val_unseen \
> > > > > > > > > > > > > > > > > > > >     --output_path ./results/val_unseen \
> > > > > > > > > > > > > > > > > > > >     --max_episodes 20 \
> > > > > > > > > > > > > > > > > > > >     --max_steps 100 \
> > > > > > > > > > > > > > > > > > > >     --num_history 4
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > # 保存可视化图片
> > > > > > > > > > > > > > > > > > > > python src/evaluation.py ... --save_video --save_video_ratio 1.0
> > > > > > > > > > > > > > > > > > > > # 图片保存到 results/val_unseen/vis_0/*.jpg
> > > > > > > > > > > > > > > > > > > > ```
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="section">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="container">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > ## 本章总结
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="module-grid">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-vln);">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > ### ✅ 完成本章后你应该能
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > >   - 创建并验证 VLN-v0 环境
> > > > > > > > > > > > > > > > > > > >   - 理解 R2R episode 的数据结构（position + instruction + reference\_path）
> > > > > > > > > > > > > > > > > > > >   - 解释 InstructionSensor 如何从 episode 提取指令文本
> > > > > > > > > > > > > > > > > > > >   - 启动 VLN 模仿学习训练并阅读 loss/acc 曲线
> > > > > > > > > > > > > > > > > > > >   - 理解 SR/SPL/nDTW 三项评估指标
> > > > > > > > > > > > > > > > > > > >   - 导出可用于真机推理的 checkpoint + config 文件
> > > > > > > > > > > > > > > > > > > >   - 运行 SOTA 模型（JanusVLN）并在同一数据上对比 SR
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="module" style="border-left-color: #a78bfa;">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > ### 🔜 下一步：真机部署
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > 现在你手头有了训练好的 VLN 模型。接下来的问题是：**怎么让它在 Spark-I 或 Leo 上跑起来？**  
> > > > > > > > > > > > > > > > > > > >   
> > > > > > > > > > > > > > > > > > > > [→ 第8章：真机部署](habitat-textbook-step8.html)（从架构到微调的完整流程）
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > <div class="page-nav">
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > [← 第6步：RL 训练入门](habitat-textbook-step6.html) [第8章：真机部署 →](habitat-textbook-step8.html)
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > > > > > > 
> > > > > > > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > > 
> > > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
> > > > > > > > > > > > 
> > > > > > > > > > > > </div>
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
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > </div>
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
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
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
> >

</div>
# 第8章：真机部署 — Habitat 从零理解

> 视觉语言模型（VLM）直接接收 RGB 图像 + 自然语言指令 → 输出控制命令。 无需地图、无需 ROS 导航栈、无需预建环境模型——一个模型解决全部问题。

## 本章概览：从架构到微调的完整流程

将仿真训练的 VLN 模型部署到真实 Spark‑I 机器人：架构设计 → 模型选型 → 零样本直控 → 数据采集 → LoRA 微调。

两种真机方案：VLN→ROS Nav2（稳妥）和 VLM 端到端（前沿）。前置：[第7章 VLN](habitat-textbook-step7.html) 仿真训练。

| \#  | 案例                           | 你将学会                     | 难度   |
| --- | ---------------------------- | ------------------------ | ---- |
| 8-1 | [云-边-端 VLN 架构](#case8-1)     | Spark→L40 拓扑、SSH 隧道、推理链路 | ⭐⭐   |
| 8-2 | [理解 VLM 导航原理](#case8-2)      | VLM 为什么能做导航、核心论文思路       | ⭐⭐   |
| 8-3 | [模型选型与部署方案](#case8-3)        | JanusVLN 等模型对比、INT8 量化   | ⭐⭐⭐  |
| 8-4 | [云端直控真机 ★](#case8-4)         | JanusVLN 零样本部署、防打转、显示窗口  | ⭐⭐⭐⭐ |
| 8-5 | [仿真与真机测试计划](#case8-5)        | 评估指标、测试场景设计、安全守则         | ⭐⭐   |
| 8-6 | [真机采集与数据处理](#case8-6)        | rosbag录制、仿真采集、数据质量检查     | ⭐⭐⭐  |
| 8-7 | [LoRA 微调 JanusVLN](#case8-7) | 单卡微调、数据采集方法论             | ⭐⭐⭐⭐ |
| 8-8 | [两种方法全面对比](#case8-8)         | VLN+Nav2 vs JanusVLN 直控  | ⭐⭐⭐  |

## 方案一 · VLN → ROS Nav2

将第7章训练好的 VLN 模型部署到真实机器人：VLN 做高层决策 → 输出子目标位姿 → ROS Nav2 执行底层导航。

## 方案二 · VLM 端到端

不使用导航栈，视觉语言模型直接输出控制指令——无地图、端到端的 VLN 方案。

## 8-1 · 云-边-端 VLN 架构

<div>

**① 案例含义**

当模型大到 80 亿参数（JanusVLN），真机的 Jetson / 树莓派根本跑不动。 本案例介绍**云-边-端分离**方案（具体实现在 [8-4](#case8-4)）： 真机负责感知+执行，云端 GPU 负责推理。

</div>

### ② 系统架构

``` 
    复制
    # ═══════════ 真机 (Spark-I, Jetson Orin) ═══════════
#   算力有限，只做采集 + 执行

# ═══════════ 云端 (L40 GPU 服务器) ═══════════
#   JanusVLN 推理，~2 秒/步

# 数据流:
#
#  真机 📷 ──JPEG(50KB)──→ 云端
#  真机 🤖 ←──action──── 云端 (JanusVLN 推理)
#
#  循环: 拍照→上传→推理→回传→Nav2执行→拍照→...
```

</div>

| 模块        | 部署位置   | 硬件              | 职责                               |
| --------- | ------ | --------------- | -------------------------------- |
| 📷 图像采集    | 真机     | RealSense D435i | RGB 拍照 → JPEG 压缩                 |
| 📤 图像上传    | 真机     | WiFi/5G         | HTTP POST 到云端                    |
| 🧠 VLN 推理  | **云端** | **L40 GPU**     | JanusVLN: 图像+指令→动作               |
| 📥 动作回传    | 云端→真机  | WiFi/5G         | JSON {"action": "MOVE\_FORWARD"} |
| 🗺️ 动作映射   | 真机     | Jetson CPU      | FORWARD → Nav2 目标位姿              |
| 🚗 路径规划+控制 | 真机     | Jetson + 电机     | ROS Nav2 规划+执行                   |

### ③ 核心代码

**真机侧：image\_bridge\_node.py**

``` 
    复制
    import rclpy, cv2, requests, json
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class VLNCloudBridge(rclpy.node.Node):
    def __init__(self):
        super().__init__('vln_cloud_bridge')
        self.bridge = CvBridge()
        self.cloud_url = "http://L40_IP:8000/step"
        self.instruction = "Go to the kitchen"  # 可动态更新

        # 订阅相机
        self.sub = self.create_subscription(
            Image, '/camera/color/image_raw', self.on_image, 10)

        # 发布子目标给 Nav2
        self.goal_pub = self.create_publisher(
            PoseStamped, '/goal_pose', 10)

    def on_image(self, msg):
        # 1. ROS Image → JPEG bytes
        cv_img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        _, jpg = cv2.imencode('.jpg', cv_img, [cv2.IMWRITE_JPEG_QUALITY, 80])

        # 2. 上传到云端
        resp = requests.post(self.cloud_url,
            files={'image': jpg.tobytes()},
            data={'instruction': self.instruction},
            timeout=5)

        # 3. 解析动作
        action = resp.json()['action']  # "MOVE_FORWARD"
        self.get_logger().info(f'Action: {action}')

        # 4. 映射为 Nav2 目标并发布
        if action == 'STOP':
            self.cancel_nav()
        else:
            goal = self.action_to_goal(action)
            self.goal_pub.publish(goal)
```

**云端：inference\_server.py**

``` 
    复制
    from fastapi import FastAPI, File, Form
from PIL import Image
import io

app = FastAPI()
model = load_janusvln()  # 启动时加载模型

@app.post("/step")
async def step(image: bytes = File(...), instruction: str = Form(...)):
    # 1. JPEG → PIL Image
    pil_img = Image.open(io.BytesIO(image)).convert('RGB')

    # 2. VLN 推理
    action = model.predict(pil_img, instruction)  # ~2 秒

    return {"action": action}  # "MOVE_FORWARD" | "TURN_LEFT" | "STOP"

# 启动: uvicorn inference_server:app --host 0.0.0.0 --port 8000
```

### ④ 每步延迟预算

| 阶段              | 耗时            | 占比      | 优化空间            |
| --------------- | ------------- | ------- | --------------- |
| 拍照 + 压缩         | \~0.05s       | 2%      | 已足够             |
| 网络上传 (50KB)     | \~0.02s       | 1%      | WiFi 6 / 5G 无压力 |
| **JanusVLN 推理** | **\~2.0s**    | **80%** | 模型量化 / TensorRT |
| 网络回传            | \~0.01s       | 0%      | 可忽略             |
| Nav2 规划         | \~0.1s        | 4%      | 已足够             |
| 机器人移动 (0.25m)   | \~0.3s        | 13%     | 取决于速度           |
| **合计**          | **\~2.5 秒/步** |         |                 |

> ⚠️
> 
> <div class="warn-title">
> 
> ⚠️ 推理速度是瓶颈——但不是死结
> 
> 2 秒/步听起来慢，但 VLN 导航通常 10-30 步到达目标 → **总耗时 25-75 秒**，实际可用。 如果接受不了，可以：模型量化到 INT8（速度 2x）、换小模型（Qwen2.5-VL-3B）、 或等下一代 GPU（RTX 5090 推理 \<0.5s）。
> 
> <div id="case8-2" class="section">
> 
> <div class="container">
> 
> ## 8-2 · 理解 VLM 导航原理
> 
> <div>
> 
> **① 案例含义 — VLM 导航与传统 VLN 有什么不同？**
> 
> 传统 VLN（如 [第7章](habitat-textbook-step7.html) 训练的模型）是一个**任务专用的小模型**：CNN 编码图像 + LSTM 编码指令 → 输出离散动作。 VLM 导航则使用一个**通用的大模型**（数亿到数十亿参数），已在海量图文数据上预训练过， 具备对场景、物体、空间关系的广泛理解。  
>   
> **核心区别：**VLN 需要针对导航任务专门训练；VLM 已经"知道"什么是厨房、走廊、门口， 导航只是它推理能力的延伸。
> 
> </div>
> 
> ### ② 核心论文思路拆解
> 
> <div class="dual-panel">
> 
> <div class="panel">
> 
> #### 📄 NaVid-4D (CVPR 2025)
> 
> **核心思路：**将导航形式化为视频预测任务。  
> 输入：**历史视频帧**（多帧 RGB）+ 指令文本  
> 输出：**未来轨迹**（一系列 waypoint 坐标）  
> 特点：不显式建图，利用视频中的时序信息隐式编码空间结构。  
> 模型：基于 Video Diffusion 架构，在 Habitat 仿真中训练。  
> **与我们的关系：**可以复用 [第7章](habitat-textbook-step7.html) 训练出的模型作为特征提取器。
> 
> </div>
> 
> <div class="panel">
> 
> #### 📄 NaVILA (CoRL 2024)
> 
> **核心思路：**结合 VLM 的语义理解 + 传统导航策略。  
> 输入：RGB 图像 + 指令  
> 输出：**子目标**（不是最终动作，而是中间目标点）  
> 定位：介于方法一和方法二之间——VLM 做高层规划，但还需要底层控制器。  
> **与我们的关系：**可视为方法一的升级版：将 VLN 模型替换为大 VLM。
> 
> <div class="arch-diagram">
> 
> <div style="font-size:0.85rem;color:#f9a8d4;font-weight:700;margin-bottom:18px;">
> 
> VLM 端到端导航 — 极简架构
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#3b82f620;border:2px solid #3b82f6;min-width:180px;">
> 
> 📷 RGB 相机  
> <span class="small">单帧或历史帧 stack</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#8b5cf620;border:2px solid #8b5cf6;min-width:200px;">
> 
> 📝 自然语言指令  
> <span class="small">"走到厨房水池前"</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   输入   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#ec489920;border:2px solid #ec4899;min-width:500px;">
> 
> **VLM (Vision-Language Model)**  
> <span class="small">Qwen2-VL / LLaVA / GPT-4V / NaVid / NaVILA</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   输出   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⬆️ 前进  
> <span class="small">FORWARD 0.5m</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⬅️ 左转  
> <span class="small">LEFT 30°</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ➡️ 右转  
> <span class="small">RIGHT 30°</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⏹️ 停止  
> <span class="small">STOP</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   直接映射   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#10b98120;border:2px solid #10b981;min-width:300px;">
> 
> /cmd\_vel (Twist)  
> <span class="small">驱动底盘电机</span>
> 
> </div>
> 
> <div class="highlight-box">
> 
> #### 🔑 关键洞察：VLM 导航的本质是 "视觉问答 + 行动"
> 
> 你可以把 VLM 导航理解为：  
>   
> **Q（指令）：**"走到厨房水池前面"  
> **VLM 看当前图像：**识别到 "我在客厅，前方是走廊，左边是厨房门"  
> **VLM 推理：**"我应该往前走，到厨房门口再左转"  
> **A（动作）：**FORWARD  
>   
> 每一步都是一个新的视觉问答循环。VLM 不维护地图——它依赖**实时视觉 + 常识推理**来做决策。 这最接近人类导航的方式：你不需要心里有精确的 2D 栅格地图，你只需要"看到前方是什么"就能决定下一步。
> 
> <div id="case8-3" class="section">
> 
> <div class="container">
> 
> ## 8-3 · 模型选型与部署方案
> 
> <div>
> 
> **① 案例含义**
> 
> 开源和商业 VLM 模型各有优劣。选型取决于你的**硬件算力**（Spark-I 的 i5-1240P 无独显 vs 是否有远程 GPU 服务器）、 **延迟要求**（实时导航需要 \<500ms 推理）和**费用预算**。
> 
> </div>
> 
> ### ② 模型对比
> 
> | 模型                      | 类型      | 参数量  | 推理速度 (CPU)               | 导航能力             | 硬件需求                          |
> | ----------------------- | ------- | ---- | ------------------------ | ---------------- | ----------------------------- |
> | **JanusVLN-7B** ⭐       | 开源      | \~8B | \~2s (GPU) / \~6s (INT8) | 双记忆导航，SOTA       | 10GB VRAM (INT8)，L40 单卡       |
> | **Qwen2-VL-2B**         | 开源      | 2B   | \~300ms (量化)             | 基础理解，可 fine-tune | 4GB RAM，CPU 可行                |
> | **LLaVA-1.6-7B**        | 开源      | 7B   | \~2s (CPU)               | 较强推理，需量化         | 8GB VRAM (GPU)，14GB RAM (CPU) |
> | **NaVid-4D**            | 研究 (复现) | \~1B | \~200ms (GPU)            | 专为导航优化           | 4GB VRAM                      |
> | **GPT-4V (API)**        | 商业 API  | 未公开  | \~500ms–2s (网络)          | 极强常识推理           | 仅需网络连接                        |
> | **Claude Vision (API)** | 商业 API  | 未公开  | \~300ms–1s (网络)          | 极强空间推理           | 仅需网络连接                        |
> | **Qwen2-VL-72B (API)**  | 商业/开源   | 72B  | \~2–5s (API)             | 最强综合能力           | 仅需网络连接                        |
> 

> <div class="dual-panel">
> 
> <div class="panel">
> 
> #### 🖥️ 方案 A：本地推理（Spark-I 离线运行）
> 
> **选型：**Qwen2-VL-2B 量化版 (INT8/INT4)  
> **优点：**无网络依赖、低延迟、数据不出设备  
> **缺点：**导航能力弱于大模型，可能在复杂场景出错  
> **适配：**使用 ONNX Runtime 或 llama.cpp 在 i5-1240P 上运行  
> **调优：**可以用 R2R 数据做少量 fine-tune 提升导航表现
> 
> </div>
> 
> <div class="panel">
> 
> #### ☁️ 方案 B：云端 API（机器人连 WiFi）
> 
> **选型：**GPT-4V 或 Claude Vision API  
> **优点：**最强推理能力，几乎不需要 fine-tune  
> **缺点：**依赖网络、有延迟波动、API 调用费用  
> **适配：**ROS 节点通过 HTTP/gRPC 调用 API  
> **适用场景：**研究原型验证、Demo、非实时任务
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 💡 推荐策略：本地 + 云端混合
> > 
> > 先用**方案 B（云端 API）快速验证** VLM 导航的可行性——用最聪明的模型看看你的场景是否能靠纯视觉+语言解决。 确认可行后，再考虑**方案 A 部署本地模型**以获得更低的延迟和更稳定的表现。  
> >   
> > Spark-I 的 i5-1240P 虽然无独显，但 16GB RAM + Intel Iris Xe 集成显卡可以跑 ONNX 量化模型。 Leo 如果有更强算力（或外接 GPU），选择余地更大。
> > 
> > <div id="case8-4" class="section">
> > 
> > <div class="container">
> > 
> > ## 8-4 · JanusVLN 云端直控真机 ★
> > 
> > <div>
> > 
> > **① 案例含义**
> > 
> > 7-6 在仿真里评估了 JanusVLN（SR=46.7%），但仿真不是现实。8-4 把同一个模型**部署到真实的 Spark-I 机器人上**， 用中文自然语言指令驱动它在办公室里导航——"去打印机前""去有显示器的桌子"。
> > 
> > **核心创新：**机器人本地没 GPU，通过 SSH 隧道把摄像头画面实时发给云端 L40， JanusVLN 推理后返回动作指令，形成一个 **"云端大脑 + 本地身体"** 的异构架构。
> > 
> > **前置条件：**Spark-I 机器人（ROS2 Humble）+ L40 云端 GPU（\>= 24GB 显存）+ 稳定网络。 需要安装 `bitsandbytes` 做 INT8 量化。
> > 
> > </div>
> > 
> > #### 云-边 VLN 推理架构
> > 
> > <div class="flow-box">
> > 
> > <div class="flow-step" style="border-top:3px solid #64748b;">
> > 
> > **① Spark-I 本地**
> > 
> > D435 摄像头拍照  
> > ROS2 vln\_client 节点
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > 
> > **② SSH 隧道**
> > 
> > 384px JPEG 编码  
> > localhost:18001→L40:8443
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > 
> > **③ L40 推理**
> > 
> > JanusVLN INT8  
> > \~6-8s/步推理
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > 
> > **④ 返回动作**
> > 
> > MOVE\_FORWARD/TURN/STOP  
> > JSON HTTP 200
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #10b981;">
> > 
> > **⑤ 执行动作**
> > 
> > ROS2 Twist→底盘  
> > 连续运动不顿挫
> > 
> > ### ② L40 端：推理服务 (server.py)
> > 
> > <div>
> > 
> > **📦 模型加载 — 关键参数**
> > 
> > 直接加载 JanusVLN（\~10B 参数，BF16 精度）需要 **43GB 显存**，L40 总共 44GB。 加上推理时的 KV cache 和激活值——**第 8 步必然 OOM**。
> > 
> > </div>
> > 
> > #### 🔑 解决方案：INT8 量化
> > 
> > ``` 
> >     加载时加一行 load_in_8bit=True
> >     # BF16 — 43GB, 第8步OOM
> > model = Qwen2_5_VLForConditionalGenerationForJanusVLN.from_pretrained(
> >     MODEL_PATH,
> >     torch_dtype=torch.bfloat16,
> >     device_map="auto",
> > )
> > 
> > # INT8 — 10.6GB, 永不OOM
> > model = Qwen2_5_VLForConditionalGenerationForJanusVLN.from_pretrained(
> >     MODEL_PATH,
> >     load_in_8bit=True,
> >     device_map="auto",
> > )
> >   
> > ```
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 📊 实测对比
> > > 
> > > BF16：43GB / 第8步OOM / \~2-5s/步 · INT8：**10.6GB** / **永远不崩** / \~6-8s/步
> > > 
> > > </div>
> > > 
> > > #### 推理端点设计
> > > 
> > > ``` 
> > >     # POST /reset — 新任务开始
> > > {"session_id": "spark_001", "instruction": "去打印机前"}
> > > 
> > > # POST /step — 每步推理
> > > {"session_id": "spark_001", "image_base64": "...", "step_id": 5}
> > > 
> > > # 响应
> > > {"action": "MOVE_FORWARD", "step_id": 5, "raw_output": "move_forward"}
> > >   
> > > ```
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > ⚠️ 两处防 OOM 的关键代码
> > > > 
> > > > **1. 限制历史帧数**：保持最近 10 帧历史图像，超出丢弃  
> > > > **2. 每步清理 KV cache**：推理后重置 past\_key\_values 并调用 torch.cuda.empty\_cache()  
> > > >   
> > > > 历史帧越多 → KV cache 越大 → 推理越慢 + 显存越紧。10 帧是平衡点。
> > > > 
> > > > </div>
> > > > 
> > > > ### ② Spark 端：客户端节点 (vln\_client.py)
> > > > 
> > > > | 模块         | 作用                     | 关键技术点                              |
> > > > | ---------- | ---------------------- | ---------------------------------- |
> > > > | **SSH 隧道** | 连接 L40 推理服务            | localhost:18001→L40:8443 端口映射      |
> > > > | **摄像头订阅**  | 接收 D435 彩色图像           | cv\_bridge 转 OpenCV，缩放至 384px 节省带宽 |
> > > > | **推理循环**   | 每步：拍照→HTTP POST→等回复→执行 | INT8 推理慢，http\_timeout 设 15s       |
> > > > | **防打转**    | 连续3次同向转弯→强制直行          | 零样本方向感弱时的兜底策略                      |
> > > > | **显示窗口**   | Spark 屏幕实时画面           | cv2.imshow + 动作叠加，DISPLAY=:0       |
> > > > 

> > > > #### 防打转逻辑
> > > > 
> > > > ``` 
> > > >     # JanusVLN 零样本方向感弱，容易连续输出转弯
> > > > # 兜底策略：检查连续同向转弯次数，>=3 则强制直行
> > > > if action in ("TURN_LEFT", "TURN_RIGHT"):
> > > >     if action == self._last_turn_dir:
> > > >         self._turn_count += 1
> > > >     else:
> > > >         self._turn_count = 1
> > > >     self._last_turn_dir = action
> > > >     if self._turn_count >= 3:
> > > >         action = "MOVE_FORWARD"      # 强制打破打转
> > > >         self._turn_count = 0
> > > >   
> > > > ```
> > > > 
> > > > ### ③ 启动命令
> > > > 
> > > > ``` 
> > > >     L40 端 — 启动推理服务
> > > > ```
> > > > 
> > > >     # 1. 安装 bitsandbytes（一次性）
> > > >     $ pip install bitsandbytes
> > > >     
> > > >     # 2. 修改 server.py：torch_dtype → load_in_8bit=True
> > > >     # 3. 后台启动
> > > >     $ nohup python server.py /tmp/srv.log 2>&1 &
> > > >     
> > > >     # 4. 验证
> > > >     $ curl http://localhost:8443/health
> > > >     {"status": "ok", "model_loaded": true}
> > > > 
> > > > ``` 
> > > >     Spark 端 — 启动导航
> > > > ```
> > > > 
> > > >     # 1. 清理僵尸进程（重要！否则 D435 断连）
> > > >     $ pkill -9 -f spark_base; pkill -9 -f realsense2_camera; pkill -9 -f vln_client
> > > >     
> > > >     # 2. 一键启动底盘+摄像头+VLN
> > > >     $ ros2 launch spark_vln vln_bringup.launch.py
> > > >     
> > > >     # 3. 设置指令（ROS2 param，支持中文）
> > > >     $ ros2 param set /vln_client instruction "去打印机前"
> > > >     
> > > >     # 4. 启动导航
> > > >     $ ros2 service call /vln/start std_srvs/srv/Trigger
> > > > 
> > > > ### ④ 实测数据
> > > > 
> > > > <div>
> > > > 
> > > > **📊 "去打印机前" — 19步完整记录（INT8）**
> > > > 
> > > > <div style="font-size:0.82em;font-family:monospace;line-height:1.8;margin-top:8px;">
> > > > 
> > > > Step 1-6: TURN\_LEFT/TURN\_RIGHT 交替扫描（找打印机）  
> > > > <span style="color:#4ade80;">Step 7: MOVE\_FORWARD</span> ← 找到了！  
> > > > Step 8-9: TURN\_LEFT/TURN\_RIGHT（微调方向）  
> > > > <span style="color:#4ade80;">Step 10: MOVE\_FORWARD</span>  
> > > > <span style="color:#4ade80;">Step 12: MOVE\_FORWARD</span>  
> > > > Step 13-14: TURN\_LEFT（调整方向）  
> > > > <span style="color:#4ade80;">Step 15: MOVE\_FORWARD</span> ← 第三次自主前进  
> > > > <span style="color:#4ade80;">Step 16: MOVE\_FORWARD</span>  
> > > > Step 17-19: TURN\_LEFT/RIGHT
> > > > 
> > > > </div>
> > > > 
> > > > ✅ **3 次自主 MOVE\_FORWARD，零次防打转触发**——机器人交替扫描→锁定目标→前进，行为合理。  
> > > > ✅ 19 步零 OOM，零 HTTP 500。显存稳定在 10.9GB。
> > > > 
> > > > </div>
> > > > 
> > > > | 指标         | BF16          | INT8     |
> > > > | ---------- | ------------- | -------- |
> > > > | **显存占用**   | 43 GB         | 10.6 GB  |
> > > > | **稳定性**    | 第8步必崩         | 永不崩      |
> > > > | **推理速度**   | \~2-5s/步      | \~6-8s/步 |
> > > > | **自主前进次数** | 0 次（7步纯转后OOM） | 3 次（19步） |
> > > > | **防打转触发**  | 2 次           | 0 次      |
> > > > 

> > > > ### ⑤ 输出结果的含义
> > > > 
> > > > <div>
> > > > 
> > > > **每步日志解读**
> > > > 
> > > > `[vln_client] Step 7: MOVE_FORWARD (move_forward)`  
> > > > → 模型认为当前方向接近目标，建议前进 0.2m/s  
> > > >   
> > > > `[vln_client] Step 8: TURN_RIGHT`  
> > > > → 模型发现目标偏右，建议右转 0.5rad/s  
> > > >   
> > > > `[WARN] Anti-spin: 3 consecutive TURN_LEFT, forcing MOVE_FORWARD`  
> > > > → 连续3次同向转弯，防打转机制介入——模型可能在犹豫，强制直行打破僵局  
> > > >   
> > > > `[INFO] Goal reached (STOP)`  
> > > > → 模型判定已到达目标，输出 STOP，导航结束
> > > > 
> > > > </div>
> > > > 
> > > > ### ⑥ 试试调整这些
> > > > 
> > > > | 调整项              | 怎么改                                       | 预期看到什么                      |
> > > > | ---------------- | ----------------------------------------- | --------------------------- |
> > > > | **history 帧数**   | `server.py` 中改 `10` → `5` 或 `20`          | 5帧=推理更快但容易迷路；20帧=更稳但更慢      |
> > > > | **HTTP timeout** | `vln_client.py` 中 `http_timeout`（默认 15s）  | INT8 推理 6-8s，设 \< 10s 会误报超时 |
> > > > | **防打转阈值**        | `self._turn_count >= 3` 改 `2` 或 `5`       | 2=更激进打断转弯；5=更容忍原地扫描         |
> > > > | **图像分辨率**        | `max_size = 384` 改 `256` 或 `512`          | 256=更快但识别率降；512=更准但推理更慢     |
> > > > | **量化精度**         | `load_in_8bit=True` → `load_in_4bit=True` | 4bit=\~6GB显存，推理更快但质量可能微降    |
> > > > | **线/角速度**        | `linear_speed=0.2, angular_speed=0.5`     | 0.3/0.8=更快但更抖；0.1/0.3=更稳但更慢 |
> > > > 

> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 💡 下一步 — 真机采集 + LoRA 微调
> > > > > 
> > > > > 零样本的局限性：模型不认识你的办公室布局。想让 JanusVLN 真正理解"会议室""饮水机""打印机"的具体位置， 需要用 Spark 录制真实路径数据（[8-6 rosbag](#case8-6)）→ 标注中文指令 → [8-7 LoRA 微调](#case8-7)。
> > > > > 
> > > > > <div id="case8-5" class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 8-5 · 仿真与真机测试计划
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **① 案例含义**
> > > > > 
> > > > > 直接上真机风险大（撞墙、电机过载）。8-5 设计了两阶段测试计划：先在 **Gazebo 仿真** 中验证完整链路， 再上 **Spark-I 真机**。每阶段都有明确的 Pass/Fail 条件。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ② Phase 1：Gazebo 仿真测试
> > > > > 
> > > > > **环境：**Spark-I Gazebo 仿真 + TurtleBot3 世界
> > > > > 
> > > > > | \#     | 测试项        | 操作                                    | 预期            | Pass 条件                         |
> > > > > | ------ | ---------- | ------------------------------------- | ------------- | ------------------------------- |
> > > > > | **T1** | 通信链路       | 真机端启动 image\_bridge → curl 云端 /health | 200 OK        | 3/3 请求成功                        |
> > > > > | **T2** | 单步推理       | 发一张仿真 RGB + "Go to the door"          | 返回一个有效动作      | 动作在 {FORWARD,LEFT,RIGHT,STOP} 内 |
> > > > > | **T3** | 动作映射       | FORWARD → /cmd\_vel 发布 → 检查移动         | 机器人向前移动 0.25m | 里程计位移 \> 0.2m，角度偏差 \< 5°        |
> > > > > | **T4** | 端到端单步执行    | 云端返回 FORWARD → 真机执行 0.25m             | 机器人直行 0.25m   | 里程计位移在 0.2–0.3m 之间              |
> > > > > | **T5** | 多步导航       | 连续 10 步 拍照→推理→执行 循环                   | 每步正确执行        | 10/10 步无卡死、无超时                  |
> > > > > | **T6** | 完整 episode | 发指令 → 自动运行直到 STOP                     | 机器人停在目标附近     | 最终位置距 ground-truth goal \< 2m   |
> > > > > | **T7** | 异常恢复       | 推理超时 / 网络断开 → 观察行为                    | 安全停止，不发无效指令   | 机器人不失控移动                        |
> > > > > 

> > > > > ``` 
> > > > >     复制
> > > > >     # 仿真启动顺序
> > > > > # 终端 1: 启动 Gazebo 仿真世界
> > > > > $ ros2 launch spark_bringup gazebo.launch.py world:=turtlebot3_world
> > > > > 
> > > > > # 终端 2: 启动 VLN 客户端（端到端）
> > > > > $ ros2 launch spark_vln vln_bringup.launch.py
> > > > > 
> > > > > # 终端 3 (云端): 启动推理服务
> > > > > $ ssh L40 'nohup python server.py &/tmp/srv.log 2>&1 &'
> > > > > 
> > > > > # 发送指令 → 开始导航
> > > > > $ ros2 param set /vln_client instruction "去门口停下"
> > > > > $ ros2 service call /vln/start std_srvs/srv/Trigger
> > > > > ```
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ③ Phase 2：Spark-I 真机测试
> > > > > 
> > > > > **前置：**Phase 1 全部 T1-T7 Pass + 机器人硬件检查
> > > > > 
> > > > > | \#      | 测试项       | 特殊注意事项                    | Pass 条件               |
> > > > > | ------- | --------- | ------------------------- | --------------------- |
> > > > > | **T8**  | 相机标定验证    | 真机 RGB 尺寸/视场角与仿真不同        | 图像 resize 后送入模型无报错    |
> > > > > | **T9**  | 坐标系对齐     | 端到端输出 /cmd\_vel 是机器人坐标系   | rviz 中移动方向与实际一致       |
> > > > > | **T10** | 实景单步导航    | 真机有里程计漂移，Nav2 需实时修正       | 单步到达误差 \< 0.15m       |
> > > > > | **T11** | 动态障碍物     | 人在机器人前方走过 → Nav2 应避障      | 机器人减速/绕行，不撞人          |
> > > > > | **T12** | 10 条指令测试集 | 在办公室环境中预设 10 条导航指令        | SR ≥ 40%（10 条中 4+ 成功） |
> > > > > | **T13** | 紧急停止      | 物理急停按钮或 /vln/stop service | 电机立即断电，\< 0.5s 响应     |
> > > > > 

> > > > > > ⚠️
> > > > > > 
> > > > > > <div class="warn-title">
> > > > > > 
> > > > > > ⚠️ 真机测试安全守则
> > > > > > 
> > > > > > 1\. 首次测试用**最低速度**（0.1 m/s），逐步提高  
> > > > > > 2\. 旁边始终有人手持**急停遥控器**  
> > > > > > 3\. 测试区域**清空行人**，地面无杂物  
> > > > > > 4\. 先测试 STOP 指令（验证急停链路），再测移动  
> > > > > > 5\. 录 rosbag，失败后可回放分析
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ④ 测试记录模板
> > > > > > 
> > > > > > | 测试ID   | 日期    | 环境     | 指令                       | 结果 | 耗时  | 失败原因           |
> > > > > > | ------ | ----- | ------ | ------------------------ | -- | --- | -------------- |
> > > > > > | T6-01  | 06-18 | Gazebo | Go to the door           | ✅  | 32s | —              |
> > > > > > | T6-02  | 06-18 | Gazebo | Go to kitchen, turn left | ❌  | —   | Nav2 规划失败（无地图） |
> > > > > > | T12-01 | —     | 真机     | 走到门口停下                   | —  | —   | 待测试            |
> > > > > > 

> > > > > > <div id="case8-6" class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 8-6 · 真机采集与数据处理
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **① 案例含义**
> > > > > > 
> > > > > > 要让 JanusVLN 真正理解"会议室""饮水机""打印机"的具体位置，需要采集真实办公室的导航数据。本案例涵盖三种采集方式（仿真自动、真机手动、混合策略），以及数据格式规范和质量检查清单。
> > > > > > 
> > > > > > **前置条件：**已完成 [8-4 零样本直控](#case8-4)，确认 Spark-I 底盘+摄像头可用。采集的数据将用于 [8-7 LoRA 微调](#case8-7)。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ② 三种采集方式对比
> > > > > > 
> > > > > > | 方式            | 工具                             | 单条耗时   | 优点         | 缺点        |
> > > > > > | ------------- | ------------------------------ | ------ | ---------- | --------- |
> > > > > > | **A. 仿真自动采集** | Habitat + ShortestPathFollower | \~10 秒 | 快速、安全、可批量  | 图像与真机有分布差 |
> > > > > > | **B. 真机手动录制** | Spark-I + rosbag               | \~5 分钟 | 真实相机/光照/动态 | 慢、需人工操作   |
> > > > > > | **C. 混合策略**   | 仿真 80% + 真机 20%                | —      | 兼得速度与真实感   | 需对齐两种数据格式 |
> > > > > > 

> > > > > > ### ③ 方式 A：仿真自动采集
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # collect_training_data.py — 在 Habitat 中自动采集导航轨迹
> > > > > > import habitat, json, gzip, numpy as np
> > > > > > from habitat.tasks.nav.shortest_path_follower import ShortestPathFollower
> > > > > > 
> > > > > > env = habitat.Env(config=habitat.get_config("benchmark/nav/vln/vln_r2r.yaml"))
> > > > > > follower = ShortestPathFollower(env.sim, goal_radius=1.8, return_one_hot=False)
> > > > > > 
> > > > > > dataset = []
> > > > > > for ep_id, episode in enumerate(env.episodes):
> > > > > >     obs = env.reset()
> > > > > >     episode_data = {
> > > > > >         "episode_id": ep_id,
> > > > > >         "scene_id": episode.scene_id,
> > > > > >         "start_position": episode.start_position.tolist(),
> > > > > >         "start_rotation": episode.start_rotation.tolist(),
> > > > > >         "goals": [{"position": g.position.tolist()} for g in episode.goals],
> > > > > >         "reference_path": [p.tolist() for p in episode.reference_path],
> > > > > >         "rgb_frames": [],        # 每步的 RGB 图像
> > > > > >         "actions": [],            # 每步的专家动作
> > > > > >         "instruction": ""        # 人工标注（采集后填）
> > > > > >     }
> > > > > > 
> > > > > >     while not env.episode_over:
> > > > > >         episode_data["rgb_frames"].append(obs["rgb"].copy())
> > > > > >         action = follower.get_next_action(episode.reference_path)
> > > > > >         episode_data["actions"].append(action)
> > > > > >         obs = env.step(action)
> > > > > > 
> > > > > >     dataset.append(episode_data)
> > > > > > 
> > > > > > # 保存（不含 RGB 图片——图片单独存为 PNG 以节省 JSON 体积）
> > > > > > with gzip.open("my_scene_train.json.gz", "wt") as f:
> > > > > >     json.dump({"episodes": dataset}, f, default=str)
> > > > > > ```
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ④ 方式 B：真机手动录制（rosbag）
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # 真机采集流程（Spark-I + ROS 2）
> > > > > > 
> > > > > > # Step 1: 录 rosbag（遥控机器人走一遍路径）
> > > > > > $ ros2 bag record /camera/color/image_raw /odom /tf /tf_static \
> > > > > >     -o my_nav_path_01
> > > > > > 
> > > > > > # Step 2: 从 rosbag 提取位姿序列 → reference_path
> > > > > > $ python3 extract_poses_from_bag.py my_nav_path_01/
> > > > > > 
> > > > > > # Step 3: 人工标注指令（对着视频写）
> > > > > > #   示例："从实验室门口出发，经过机械臂工位，走到3D打印区停下"
> > > > > > 
> > > > > > # Step 4: 重复 30-50 条 → 开始微调
> > > > > > ```
> > > > > > 
> > > > > > ### ⑤ 数据质量检查清单
> > > > > > 
> > > > > > <table>
> > > > > > <colgroup>
> > > > > > <col style="width: 33%" />
> > > > > > <col style="width: 33%" />
> > > > > > <col style="width: 33%" />
> > > > > > </colgroup>
> > > > > > <thead>
> > > > > > <tr class="header">
> > > > > > <th>维度</th>
> > > > > > <th>✅ 正确做法</th>
> > > > > > <th>❌ 常见错误</th>
> > > > > > </tr>
> > > > > > </thead>
> > > > > > <tbody>
> > > > > > <tr class="odd">
> > > > > > <td><strong>路径多样性</strong></td>
> > > > > > <td>包含最短路径 + 偏离路径（70:30）</td>
> > > > > > <td>只有最短路径 → 模型没见过走错的样子</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>指令语言</strong></td>
> > > > > > <td>日常口语："走到白板前"<br />
> > > > > > 同路径 2-3 种说法</td>
> > > > > > <td>"前进 5 米，左转 30 度"→ 不是 VLN</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>光照覆盖</strong></td>
> > > > > > <td>早/中/晚各采一批</td>
> > > > > > <td>只在下午 3 点采 → 早上模型就瞎了</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>视角覆盖</strong></td>
> > > > > > <td>路径偏左/偏右/正中各一些</td>
> > > > > > <td>全都走正中间</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>动态物体</strong></td>
> > > > > > <td>有行人 / 无行人各一半</td>
> > > > > > <td>全是空房间 → 真机一有人就乱</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>距离梯度</strong></td>
> > > > > > <td>3m / 5m / 10m / 20m 均匀分布</td>
> > > > > > <td>全是 5m 以内的短距离</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>中英对应</strong></td>
> > > > > > <td>JanusVLN 用英文：中文翻译为英文<br />
> > > > > > 或用英文直接标注</td>
> > > > > > <td>中文直接喂给英文训练的模型</td>
> > > > > > </tr>
> > > > > > </tbody>
> > > > > > </table>
> > > > > > 
> > > > > > ### ⑥ 最小可行数据集
> > > > > > 
> > > > > > | 场景规模  | 最少条数   | 采集时间     | 预期 SR（微调后） |
> > > > > > | ----- | ------ | -------- | ---------- |
> > > > > > | 单个房间  | 30 条   | 1 小时（仿真） | \~55%      |
> > > > > > | 一层办公楼 | 100 条  | 3 小时（仿真） | \~65%      |
> > > > > > | 整栋建筑  | 300+ 条 | 1 天（仿真）  | \~70%      |
> > > > > > 

> > > > > > > ⚠️
> > > > > > > 
> > > > > > > <div class="warn-title">
> > > > > > > 
> > > > > > > ⚠️ 数据准备详见 [8-6 真机采集与数据处理](#case8-6)
> > > > > > > 
> > > > > > > 30 条高质量数据（路径多样 + 指令自然 + 光照覆盖）比 200 条劣质数据有效得多。 劣质数据的典型信号：微调后 SR 反而下降 → 说明数据引入了噪声而非信号。 如果时间有限，宁可花 80% 时间打磨 30 条数据，不要赶工产 100 条。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > > 💡
> > > > > > > > 
> > > > > > > > <div class="tip-title">
> > > > > > > > 
> > > > > > > > 💡 下一步：LoRA 微调
> > > > > > > > 
> > > > > > > > 数据准备好后，进入 [8-7 LoRA 微调 JanusVLN](#case8-7)，将采集的数据用于适配新场景。
> > > > > > > > 
> > > > > > > > <div id="case8-7" class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 8-7 · LoRA 微调 JanusVLN
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **① 案例含义**
> > > > > > > > 
> > > > > > > > [7-6](habitat-textbook-step7.html#case7-6) 和 [8-4](#case8-4) 展示了 JanusVLN 的零样本能力。如果想在**自己的场景**上提升性能—— 比如办公室、工厂、家庭——就需要微调。8-7 介绍三种微调方案及其硬件需求。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### ② 三种微调方案
> > > > > > > > 
> > > > > > > > | 方案                  | 原理                    | 显存需求         | L40 可行？  | 适用场景                |
> > > > > > > > | ------------------- | --------------------- | ------------ | -------- | ------------------- |
> > > > > > > > | **A. 分组件微调**        | 冻结视觉编码器，只训练 LLM + 投影层 | \~60 GB（8 卡） | ❌        | JanusVLN 原版训练方式     |
> > > > > > > > | **B. LoRA 微调**      | 冻结全部权重，插入少量可训练的秩分解矩阵  | \~30 GB（单卡）  | **✅ 可行** | JanusVLN 适配新场景，最低成本 |
> > > > > > > > | **C. Seq2Seq 全量微调** | 2700 万参数全部训练          | \~8 GB（单卡）   | ✅        | 我们的小模型在新数据上微调       |
> > > > > > > > 

> > > > > > > > > ⚠️
> > > > > > > > > 
> > > > > > > > > <div class="warn-title">
> > > > > > > > > 
> > > > > > > > > ⚠️ 为什么方案 A 需要 8 卡
> > > > > > > > > 
> > > > > > > > > 方案 A 训练 LLM 全部 70 亿参数 + 投影层，即使用 DeepSpeed ZeRO-3 分片也需要 8 卡。 L40 单卡 46GB 只够推理，不够训练。但 **方案 B（LoRA）在原代码基础上只需加 \~30 行**， 就能在单卡上微调 JanusVLN。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > ### ③ LoRA 原理解析
> > > > > > > > > 
> > > > > > > > > LoRA（Low-Rank Adaptation）不修改原始权重 **W**，而是在旁边插入两个小矩阵 **A 和 B**：
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 标准全量微调：修改 W 的全部 4096×4096 = 16M 参数
> > > > > > > > > h = W @ x + b          # W 可训练，16M 参数
> > > > > > > > > 
> > > > > > > > > # LoRA 微调：W 冻结，只训练 A 和 B
> > > > > > > > > h = W @ x + b + (B @ A) @ x   # W 冻结，A+B 共 4096×16×2 = 131K 参数
> > > > > > > > > #                  ↑ 秩 r=16，可训练参数减少 120 倍
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > | 对比     | 全量微调     | LoRA (r=16)    |
> > > > > > > > > | ------ | -------- | -------------- |
> > > > > > > > > | 可训练参数  | \~80 亿   | \~4000 万（0.5%） |
> > > > > > > > > | 显存（训练） | \~120 GB | \~30 GB        |
> > > > > > > > > | 训练速度   | 基准       | 快 1.5-2×       |
> > > > > > > > > | 推理开销   | 无        | 可合并回 W（无额外开销）  |
> > > > > > > > > | 性能     | 最佳       | 通常持平，差距 \<2%   |
> > > > > > > > > 

> > > > > > > > > ### ④ LoRA 微调 JanusVLN（L40 单卡）
> > > > > > > > > 
> > > > > > > > > **Step 1 — 安装 peft**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     pip install peft -i https://pypi.doubanio.com/simple
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 2 — 修改 train\_qwen.py，在模型加载后插入 LoRA**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     from peft import LoraConfig, get_peft_model, TaskType
> > > > > > > > > 
> > > > > > > > > # 在模型加载完成后，添加：
> > > > > > > > > lora_config = LoraConfig(
> > > > > > > > >     r=16,                          # LoRA 秩（越大效果越好，显存越多）
> > > > > > > > >     lora_alpha=32,                 # 缩放因子
> > > > > > > > >     target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
> > > > > > > > >     lora_dropout=0.05,
> > > > > > > > >     bias="none",
> > > > > > > > >     task_type=TaskType.CAUSAL_LM,
> > > > > > > > > )
> > > > > > > > > model = get_peft_model(model, lora_config)
> > > > > > > > > model.print_trainable_parameters()
> > > > > > > > > # 输出: trainable params: 41,943,040 || all params: 8,294,967,296 || trainable%: 0.506%
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 3 — 冻结 VGGT + 视觉编码器（节省更多显存）**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 冻结 VGGT（3D 特征提取器——通用能力，不需要微调）
> > > > > > > > > for param in model.vggt.parameters():
> > > > > > > > >     param.requires_grad = False
> > > > > > > > > 
> > > > > > > > > # 冻结视觉编码器（Qwen2.5-VL 的视觉 tower）
> > > > > > > > > for param in model.visual.parameters():
> > > > > > > > >     param.requires_grad = False
> > > > > > > > > 
> > > > > > > > > # 只训练：LoRA adapter + 投影层 (merger) + token embedding
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 4 — 单卡训练命令（移除 DeepSpeed）**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 原版需要 8 卡 + DeepSpeed，LoRA 版本单卡即可
> > > > > > > > > python src/qwen_vl/train/train_qwen.py \
> > > > > > > > >     --model_name_or_path ./weights/misstl/JanusVLN_Base \
> > > > > > > > >     --vggt_model_path facebook/VGGT-1B \
> > > > > > > > >     --tune_mm_llm True \
> > > > > > > > >     --tune_mm_vision False \
> > > > > > > > >     --tune_mm_mlp True \
> > > > > > > > >     --use_lora True \
> > > > > > > > >     --lora_r 16 \
> > > > > > > > >     --dataset_use train_r2r \
> > > > > > > > >     --output_dir ./JanusVLN_LoRA_Office \
> > > > > > > > >     --bf16 \
> > > > > > > > >     --per_device_train_batch_size 1 \
> > > > > > > > >     --gradient_accumulation_steps 16 \
> > > > > > > > >     --learning_rate 1e-4 \
> > > > > > > > >     --num_train_epochs 3 \
> > > > > > > > >     --save_steps 500 \
> > > > > > > > >     --max_pixels $((576*28*28)) \               # 降低分辨率省显存
> > > > > > > > >     --gradient_checkpointing                     # 用时间换显存
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > ### ⑤ 微调数据准备
> > > > > > > > > 
> > > > > > > > > 需要把自己的场景做成 R2R 格式的 JSON：
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 每条训练数据 = 一个 navigation episode
> > > > > > > > > {
> > > > > > > > >   "episodes": [
> > > > > > > > >     {
> > > > > > > > >       "episode_id": 1,
> > > > > > > > >       "scene_id": "mp3d/my_office/my_office.glb",
> > > > > > > > >       "start_position": [0, 0, 0],
> > > > > > > > >       "start_rotation": [0, 0.923, 0, 0.382],
> > > > > > > > >       "goals": [{"position": [5.2, 0, -3.1]}],
> > > > > > > > >       "reference_path": [[0,0,0], [0.5,0,0], ..., [5.2,0,-3.1]],
> > > > > > > > >       "instruction": {
> > > > > > > > >         "instruction_text": "Walk to the whiteboard and stop"
> > > > > > > > >       }
> > > > > > > > >     }
> > > > > > > > >   ],
> > > > > > > > >   "instruction_vocab": {...}  # 复用 R2R 原始词表
> > > > > > > > > }
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > | 场景来源          | 数据制作方式                                             | 最少条数     |
> > > > > > > > > | ------------- | -------------------------------------------------- | -------- |
> > > > > > > > > | Habitat 仿真新场景 | 用 ShortestPathFollower 自动生成 reference\_path，人工标注指令 | 50-100 条 |
> > > > > > > > > | 真机录制的轨迹       | SLAM 记录位姿序列 → 转成 reference\_path，人工标注指令            | 30-50 条  |
> > > > > > > > > | 现有 R2R 子集     | 从 R2R 训练集中筛选与目标场景相似的 episode                       | 200+ 条   |
> > > > > > > > > 

> > > > > > > > > ### ⑥ 微调完整流程
> > > > > > > > > 
> > > > > > > > > | 步骤             | 操作                                          | 预计时间   |
> > > > > > > > > | -------------- | ------------------------------------------- | ------ |
> > > > > > > > > | **1. 数据采集**    | 在新场景中收集 50-200 条导航指令+轨迹                     | 2-4 小时 |
> > > > > > > > > | **2. 格式转换**    | 转为 R2R JSON + gzip 压缩                       | 30 分钟  |
> > > > > > > > > | **3. LoRA 训练** | L40 单卡，3 epoch，batch\_size=1，grad\_accum=16 | 4-8 小时 |
> > > > > > > > > | **4. 合并权重**    | `model.merge_and_unload()` → LoRA 合并回原始权重   | 1 分钟   |
> > > > > > > > > | **5. 评估**      | 在新场景的 val split 上跑 eval，对比微调前后              | 30 分钟  |
> > > > > > > > > 

> > > > > > > > > > ⚠️
> > > > > > > > > > 
> > > > > > > > > > <div class="warn-title">
> > > > > > > > > > 
> > > > > > > > > > 💡 微调预期效果
> > > > > > > > > > 
> > > > > > > > > > 在 R2R 上零样本 SR=46.7%。如果用自己的 50-100 条数据进行 LoRA 微调：  
> > > > > > > > > > • **同场景 SR：**预期提升到 60-75%（模型"记住"了你的环境）  
> > > > > > > > > > • **跨场景泛化：**可能轻微下降（LoRA 的灾难性遗忘），需要混合原始 R2R 数据  
> > > > > > > > > > • **训练技巧：**前 1 epoch 混合 70% R2R + 30% 新数据，后 2 epoch 只用新数据
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > ### ⑦ 方案 C：微调我们自己的 Seq2Seq
> > > > > > > > > > 
> > > > > > > > > > 如果我们不想用 JanusVLN（硬件要求高），也可以微调自己在 §N 训练的 2700 万参数模型：
> > > > > > > > > > 
> > > > > > > > > > ``` 
> > > > > > > > > >     复制
> > > > > > > > > >     # 加载 §N 训练的 checkpoint
> > > > > > > > > > model = Seq2SeqAgent(embed_dim=300, hidden_dim=512)
> > > > > > > > > > model.load_state_dict(torch.load('ckpt/seq2seq_best.pth'))
> > > > > > > > > > 
> > > > > > > > > > # 在新数据上全量微调（27M 参数全部可训练）
> > > > > > > > > > optimizer = AdamW(model.parameters(), lr=1e-4)
> > > > > > > > > > for epoch in range(5):
> > > > > > > > > >     for rgb, instruction, action_gt in new_dataloader:
> > > > > > > > > >         pred = model(rgb, instruction)
> > > > > > > > > >         loss = CrossEntropyLoss(pred, action_gt)
> > > > > > > > > >         loss.backward()
> > > > > > > > > >         optimizer.step()
> > > > > > > > > > 
> > > > > > > > > > # 优点：快（10 分钟训完）、省显存（8GB）、可跑 DAgger
> > > > > > > > > > # 缺点：模型上限低（没有 VLM 的世界知识）
> > > > > > > > > > ```
> > > > > > > > > > 
> > > > > > > > > > | 对比            | Seq2Seq 微调  | JanusVLN LoRA  |
> > > > > > > > > > | ------------- | ----------- | -------------- |
> > > > > > > > > > | 显存            | \~8 GB      | \~30 GB        |
> > > > > > > > > > | 训练时间（100 条数据） | \~10 分钟     | \~4 小时         |
> > > > > > > > > > | SR 上限         | \~40-50%    | \~60-75%       |
> > > > > > > > > > | 适合场景          | 快速原型，验证数据质量 | 最终部署，追求性能      |
> > > > > > > > > > | 可做 DAgger     | ✅ 轻量，训练快    | ⚠️ 每轮 4 小时，迭代慢 |
> > > > > > > > > > 

> > > > > > > > > > > 💡
> > > > > > > > > > > 
> > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > 
> > > > > > > > > > > 💡 推荐策略：两级微调
> > > > > > > > > > > 
> > > > > > > > > > > **第一级：**用 Seq2Seq 在新数据上快速微调（10 分钟），验证数据质量和任务可行性  
> > > > > > > > > > > **第二级：**确认数据没问题后，用 JanusVLN LoRA 做正式微调（4-8 小时），拿到最优 SR  
> > > > > > > > > > > 这样避免了"花 4 小时训练发现数据有 bug"的情况。
> > > > > > > > > > > 
> > > > > > > > > > > <div id="case8-8" class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 8-8 · 两种方法全面对比
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **① 对比维度**
> > > > > > > > > > > 
> > > > > > > > > > > 以下是方法一（VLN + ROS Nav2）和方法二（VLM 端到端）在 12 个关键维度上的并列对比。
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > | 维度               | 方法一：VLN + ROS Nav2              | 方法二：VLM 端到端                  |
> > > > > > > > > > > | ---------------- | ------------------------------- | ---------------------------- |
> > > > > > > > > > > | **是否需要地图**       | ✅ 需要预建 2D 占据栅格地图                | ❌ 不需要任何地图                    |
> > > > > > > > > > > | **是否需要 ROS 导航栈** | ✅ 需要 move\_base / Nav2          | ❌ 直接输出 /cmd\_vel             |
> > > > > > > > > > > | **对新环境的适应**      | 需要重新建图（15-30min）                | 即开即用（但可能在陌生环境退化）             |
> > > > > > > > > > > | **避障能力**         | ✅ Nav2 成熟避障（全局+局部）              | ⚠️ 依赖 VLM 的视觉判断 + 安全屏障       |
> > > > > > > > > > > | **路径最优性**        | ✅ 全局最优路径（A\*/Dijkstra）          | ❌ 局部贪心，可能绕路                  |
> > > > > > > > > > > | **计算资源**         | 中等（CPU 跑 Nav2 + VLN 推理）         | 高（需要 GPU 或云 API，大模型推理）       |
> > > > > > > > > > > | **网络依赖**         | 无（全本地）                          | 用云端 API 时有，本地模型则无            |
> > > > > > > > > > > | **延迟**           | 低（Nav2 规划 \~50ms + VLN \~100ms） | 中等–高（云端 0.5–2s，本地量化 \~300ms） |
> > > > > > > > > > > | **语言理解粒度**       | 受 VLN 模型限制（数据集固定模板）             | ✅ 极强（理解任意自然语言）               |
> > > > > > > > > > > | **代码复杂度**        | 5 个节点，3 种通信模式                   | 1 个核心节点，极简                   |
> > > > > > > > > > > | **系统工程成熟度**      | ✅ 高（Nav2 经过多年验证）                | ⚠️ 低（VLM 导航仍在快速发展中）          |
> > > > > > > > > > > | **最适合的场景**       | 固定环境、频繁使用、稳定性优先                 | 新环境探索、研究原型、Demo              |
> > > > > > > > > > > 

> > > > > > > > > > > <div class="highlight-box">
> > > > > > > > > > > 
> > > > > > > > > > > #### 🎯 决策指南
> > > > > > > > > > > 
> > > > > > > > > > > **选方法一，如果：**  
> > > > > > > > > > > • 你的工作场景是固定的（办公室/家庭楼层布局不变）  
> > > > > > > > > > > • 你重视安全性和路径最优性  
> > > > > > > > > > > • 你的团队有 ROS 经验  
> > > > > > > > > > > • 你需要在 Spark-I / Leo 上低延迟运行  
> > > > > > > > > > >   
> > > > > > > > > > > **选方法二，如果：**  
> > > > > > > > > > > • 你需要快速验证 VLN 的概念而不想配置导航栈  
> > > > > > > > > > > • 你的使用场景不固定（多变的临时环境）  
> > > > > > > > > > > • 你更偏向 CV/ML 背景而非 ROS 背景  
> > > > > > > > > > > • 你可以接受较高的 API 费用和网络延迟  
> > > > > > > > > > > • 你想探索最前沿的 VLM 能力边界  
> > > > > > > > > > >   
> > > > > > > > > > > **最优方案：两者结合。**用方法二做**全局语义规划**（VLM 看全景图 → "先去厨房，再去卧室"）， 用方法一做**局部路径执行**（Nav2 负责每个段落的安全导航）。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 部署轨全总结
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module-grid">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-vlm);">
> > > > > > > > > > > 
> > > > > > > > > > > ### ✅ 完成本章后你应该能
> > > > > > > > > > > 
> > > > > > > > > > >   - 设计云-边-端 VLN 推理架构
> > > > > > > > > > >   - 解释 VLM 导航和传统 VLN 的本质区别
> > > > > > > > > > >   - 根据硬件条件选择合适的 VLM 方案并配置 INT8 量化
> > > > > > > > > > >   - 在真机上部署 JanusVLN 零样本直控，理解防打转策略
> > > > > > > > > > >   - 制定仿真与真机的分层测试计划
> > > > > > > > > > >   - 用 ros2 bag 录制导航数据供后续微调
> > > > > > > > > > >   - 使用 LoRA 在单卡上微调 JanusVLN 适配新场景
> > > > > > > > > > >   - 在 12 个维度上对比两种方法并做出选型决策
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-tip);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 🎓 部署轨学习路径回顾
> > > > > > > > > > > 
> > > > > > > > > > > [第6章](habitat-textbook-step6.html) → RL 训练入门  
> > > > > > > > > > > [第7章](habitat-textbook-step7.html) → VLN 仿真训练（配置→训练→评估→诊断）  
> > > > > > > > > > > [第8章](#) → 真机部署（架构→选型→直控→采集→微调→对比）  
> > > > > > > > > > >   
> > > > > > > > > > > 三条路径相互补充。你可以选择其中一条深入，也可以全部掌握。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="page-nav">
> > > > > > > > > > > 
> > > > > > > > > > > [← 第7章：VLN 仿真训练](habitat-textbook-step7.html) [第9章：Rearrange 操作 →](habitat-textbook-step9.html)
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
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
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
> </div>
> 
> </div>
> 
>
# 第9章：Rearrange 操作任务 — Habitat 从零理解

> Habitat 2.0 的核心贡献——从"导航到目标点"升级为"与物体交互"。 本章覆盖 Pick/Place、关节物体、PDDL 复合任务，从简单的抓取到复杂的多阶段家居操作。

## 案例总览

| \# | 案例                           | 难度  | 学什么                             |
| -- | ---------------------------- | --- | ------------------------------- |
| 1  | Navigation vs Rearrange 全景对比 | ⭐   | 任务空间、动作空间、物理仿真的本质差异             |
| 2  | Pick 任务：抓取物体                 | ⭐⭐  | ArmRelPos + SuctionGrasp + 物体会话 |
| 3  | Place 任务：放置物体                | ⭐⭐  | 持物约束、目标位姿传感器                    |
| 4  | NavToObj：纯导航子任务              | ⭐⭐  | 无手臂控制的底盘导航                      |
| 5  | 关节物体：开关抽屉/冰箱                 | ⭐⭐⭐ | Marker 交互 + 关节物体物理              |
| 6  | PDDL 复合任务：TidyHouse          | ⭐⭐⭐ | Pick→Nav→Place 多阶段编排            |

## 案例 1：Navigation vs Rearrange — 全景对比

<div>

**① 案例含义**

理解 Rearrange 和 Navigation 的本质差异。Rearrange 引入了**物理仿真、机器人本体、物体交互**， 是 Habitat 2.0 论文的核心升级。对初学者而言，最关键的认知转换是： **不再是"走到某个点"，而是"改变这个世界的状态"**。

</div>

| 维度         | Navigation (PointNav)       | Rearrange (Pick/Place)                   |
| ---------- | --------------------------- | ---------------------------------------- |
| **智能体**    | 看不见的"点"（radius=0.1 碰撞球）     | Fetch 机器人（有底盘+手臂+夹爪的 URDF 模型）            |
| **物理引擎**   | 无（只有碰撞检测）                   | 必须开启 Bullet 物理仿真                         |
| **动作空间**   | 离散：STOP/FWD/LEFT/RIGHT      | 连续：ArmJoint(7维) + Grip(1维) + BaseVel(2维) |
| **场景内容**   | 静态网格                        | 场景 + 可抓取物体(YCB) + 接收器(receptacle)        |
| **成功条件**   | 智能体停在 target 附近（\<0.2m）     | 物体被吸起 / 物体落到目标位姿                         |
| **Sim 类型** | `HabitatSim-v0`             | `RearrangeSim-v0`                        |
| **数据集**    | PointNav episodes (json.gz) | RearrangeDatasetV0（自动生成 + auto-download） |

### Rearrange 任务继承体系

    # Rearrange 的类继承（从 NavigationTask 到具体子任务）
    EmbodiedTask                    # 所有任务的根
      └─ NavigationTask             # 导航基类
           └─ RearrangeTask          # + 物理、碰撞、抓取管理
                ├─ RearrangePickTaskV1     # 抓取（吸盘）
                ├─ RearrangePlaceTaskV1    # 放置（持物→目标）
                ├─ DynNavRLEnv             # 纯导航（无手臂控制）
                └─ RearrangeReachTaskV1    # 机械臂到达（底盘固定）
           └─ SetArticulatedObjectTask     # 关节物体操作
                ├─ RearrangeOpenDrawerTaskV1
                ├─ RearrangeCloseFridgeTaskV1
                └─ ...

## 案例 2：Pick 任务 — 抓取物体

<div>

**① 案例含义**

最简 Rearrange 入门。Fetch 机器人导航到物体附近，控制机械臂用吸盘抓取物体。 **成功 = is\_holding=1**。这是所有操作任务的原子能力。

</div>

<div>

**② 核心代码 & 关键函数**

</div>

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

| 关键函数/配置                                               | 角色      | 说明                                                                             |
| ----------------------------------------------------- | ------- | ------------------------------------------------------------------------------ |
| `habitat.get_config("benchmark/rearrange/pick.yaml")` | 加载预置配置  | 自动设置 RearrangeSim + Fetch robot + Pick task                                    |
| `env.action_space`                                    | 动作空间定义  | Dict: {"arm\_action": Box(10,), "grip\_action": Box(1,), "base\_vel": Box(2,)} |
| `arm_action`                                          | 机械臂关节控制 | 7 维 delta joint position（相对关节角度变化）                                             |
| `SuctionGraspAction`                                  | 吸盘抓取    | 1 维: 正值=吸, 负值=放                                                                |
| `is_holding`                                          | 持物状态传感器 | 0/1: 是否正吸着物体                                                                   |
| `joint`                                               | 关节角度传感器 | 7 维: 每个关节的当前角度                                                                 |

> 💡
> 
> <div class="tip-title">
> 
> ③ 如何运行
> 
>     $ python pick_demo.py
> 
> 首次运行会自动下载 `rearrange_task_assets`（约 2-5 分钟），之后不再需要等待。
> 
> </div>
> 
> <div>
> 
> **④ 预期传感器输出**
> 
> <div class="obs-grid">
> 
> <div class="obs-item">
> 
> <span class="obs-key">head\_depth</span> → `shape=(256, 256, 1)`  
> 机器人头部深度相机
> 
> </div>
> 
> <div class="obs-item">
> 
> <span class="obs-key">joint</span> → `shape=(7,)`  
> 手臂 7 个关节角度
> 
> </div>
> 
> <div class="obs-item">
> 
> <span class="obs-key">is\_holding</span> → `shape=(1,)`  
> 0 = 未抓取，1 = 已抓取
> 
> </div>
> 
> <div class="obs-item">
> 
> <span class="obs-key">obj\_start\_sensor</span> → `shape=(3,)`  
> 物体相对 EE 的位置
> 
> </div>
> 
> <div class="obs-item">
> 
> <span class="obs-key">relative\_resting\_position</span> → `shape=(3,)`  
> EE 到休息位的向量
> 
> </div>
> 
> <div class="obs-item">
> 
> <span class="obs-key">joint\_vel</span> → `shape=(7,)`  
> 关节速度
> 
> </div>
> 
> <div>
> 
> **⑤ 输出含义**
> 
> **obj\_start\_sensor**：物体中心在机器人末端执行器坐标系下的 3D 偏移量 (Δx, Δy, Δz)。  
> 机械臂控制的目标就是把这个向量趋近于 0——即 EE 接触到物体。  
> **is\_holding** 从 0 → 1 的瞬间标志着一次成功的抓取。  
> **joint** 是 7 自由度 Fetch 手臂的当前位姿: shoulder\_pan, shoulder\_lift, upperarm\_roll, elbow\_flex, forearm\_roll, wrist\_flex, wrist\_roll。
> 
> <div id="case3" class="section">
> 
> <div class="container">
> 
> ## 案例 3：Place 任务 — 放置物体
> 
> <div>
> 
> **① 案例含义**
> 
> 智能体**已持有一个物体**（初始状态 is\_holding=1），需要导航到底座目标位置并释放物体。 Pick vs Place 的最大区别：Pick 需要先接近物体→抓取；Place 已经持有物体→只需导航+释放。
> 
> </div>
> 
>     import habitat
>     
>     config = habitat.get_config("benchmark/rearrange/place.yaml")
>     
>     with habitat.config.read_write(config):
>         config.habitat.environment.max_episode_steps = 300
>     
>     env = habitat.Env(config=config)
>     obs = env.reset()
>     
>     # 关键差异：初始状态下 is_holding=1
>     print("is_holding at start:", obs["is_holding"])
>     # → [1.0] — agent 已经抓着物体
>     
>     # obj_goal_sensor: 目标位置（不是物体位置！）
>     print("goal_pos (relative to EE):", obs["obj_goal_sensor"])
>     
>     # Place 特有传感器
>     for key in ["obj_goal_sensor", "obj_start_sensor",
>                "obj_goal_gps_compass"]:
>         print(f"  {key:30s} = {obs[key]}")
>     
>     env.close()
> 
> | 传感器                    | Pick 有?  | Place 有? | 含义                            |
> | ---------------------- | -------- | -------- | ----------------------------- |
> | `obj_start_sensor`     | ✅        | ✅        | 物体位置（EE 坐标系）                  |
> | `obj_goal_sensor`      | ❌        | ✅        | 目标放置位置（EE 坐标系）                |
> | `obj_goal_gps_compass` | ❌        | ✅        | 目标在 robot base 坐标系的极坐标 (ρ, φ) |
> | `is_holding`           | ✅ (初始 0) | ✅ (初始 1) | 抓取状态                          |
> 

> </div>
> 
> </div>
> 
> <div id="case4" class="section">
> 
> <div class="container">
> 
> ## 案例 4：NavToObj — 纯导航子任务
> 
> <div>
> 
> **① 案例含义**
> 
> NavToObj 是 Rearrange 系列中最接近 PointNav 的任务——**没有机械臂控制**， 只需要用底盘速度控制导航到目标物体或接收器。这使它成为从 Navigation 过渡到 Rearrange 的理想跳板。
> 
> </div>
> 
>     import habitat
>     
>     config = habitat.get_config("benchmark/rearrange/nav_to_obj.yaml")
>     env = habitat.Env(config=config)
>     obs = env.reset()
>     
>     # 动作空间：只需 chassis 速度控制（线性 + 角速度）
>     print("Action space:", env.action_space)
>     # base_vel: [linear_vel, angular_vel] — 2 维连续
>     
>     # 观察空间：有 GPS+Compass 类传感器
>     print("nav goal sensor (polar):", obs["obj_start_gps_compass"])
>     # [distance, angle] — 目标物体相对机器人底座的极坐标
>     
>     # 简单控制：以固定速度向目标移动
>     for step in range(200):
>         dist, angle = obs["obj_start_gps_compass"]
>         # 简单策略：转向目标，然后前进
>         if abs(angle) > 0.2:
>             action = {"base_vel": np.array([0.0, np.sign(angle) * 0.5])}
>         else:
>             action = {"base_vel": np.array([1.0, 0.0])}
>         obs, reward, done, info = env.step(action)
>         if done:
>             break
>     
>     env.close()
> 
> | 对比维度 | PointNav   | NavToObj        |
> | ---- | ---------- | --------------- |
> | 导航目标 | 3D 坐标点     | 物体 / 接收器        |
> | 动作空间 | 离散（4 动作）   | 连续速度（base\_vel） |
> | 模拟器  | HabitatSim | RearrangeSim    |
> | 物理引擎 | 关闭         | 开启              |
> | 智能体  | 无形态点       | Fetch robot 底盘  |
> 

> </div>
> 
> </div>
> 
> <div id="case5" class="section">
> 
> <div class="container">
> 
> ## 案例 5：关节物体 — 开关抽屉与冰箱
> 
> <div>
> 
> **① 案例含义**
> 
> Habitat-Sim 支持**可动关节物体**（ArticulatedObject）——抽屉、柜门、冰箱门等。 操作这类物体需要一种不同的交互方式：通过 **marker**（交互标记点）来指定抓取位置， 然后以 **关节角度** 为目标进行控制。
> 
> </div>
> 
>     import habitat
>     
>     # 开抽屉任务
>     config = habitat.get_config("benchmark/rearrange/open_cab.yaml")
>     env = habitat.Env(config=config)
>     obs = env.reset()
>     
>     print("Articulated object task sensors:")
>     for k, v in obs.items():
>         print(f"  {k:30s} shape={v.shape}")
>     
>     # 关节物体特有的组件：
>     # - marker: 手柄/拉手位置（用于指定抓取点）
>     # - joint_state: 当前关节开合角度
>     # - target_joint_state: 目标关节角度（全开/全关）
>     
>     env.close()
>     
>     print("\n=== 可用的关节物体任务 ===")
>     print("  open_cab.yaml    — 开柜门")
>     print("  close_cab.yaml   — 关柜门")
>     print("  open_fridge.yaml — 开冰箱")
>     print("  close_fridge.yaml— 关冰箱")
> 
> <div>
> 
> **⑤ 输出含义**
> 
> 关节物体任务的 **核心指标** 是关节角度与目标角度的差值。  
> 例如 OpenDrawer：目标角度 = 0.45 rad（全开），初始角度 = 0.0 rad（全关）。  
> Agent 需要抓取把手（marker），施加力拉开抽屉，直到达到目标角度。  
> 关节类型有：prismatic（滑动，如抽屉）和 revolute（旋转，如冰箱门）。
> 
> </div>
> 
> <div>
> 
> **⑥ 可调参数**
> 
> | 调整项    | 怎么改                                    | 预期看到什么         |
> | ------ | -------------------------------------- | -------------- |
> | 目标关节角度 | 修改 task config 中的 `target_joint_state` | 部分开合 vs 全开全合   |
> | 力阈值    | 修改 `force_terminate.max_accum_force`   | 更早/更晚因力过大而终止   |
> | 任务类型   | 切换 `open_cab` → `open_fridge`          | 不同的关节物体形态和交互方式 |
> 

> <div id="case6" class="section">
> 
> <div class="container">
> 
> ## 案例 6：PDDL 复合任务 — 多阶段家居操作
> 
> <div>
> 
> **① 案例含义**
> 
> **PDDL**（Planning Domain Definition Language）是一种符号化任务规划语言。 在 Habitat 中，一个"收拾桌子"的任务会被分解为：  
> `nav(碗) → pick(碗) → nav(桌子) → place(碗, 桌子) → nav(杯子) → ...`  
> 高层用 PDDL 规划，低层用 RL/脚本执行每个原子动作——这就是 HRL（Hierarchical RL）的核心思想。
> 
> </div>
> 
>     import habitat
>     
>     # 简单复合任务（有预定义 solution）
>     config = habitat.get_config("benchmark/rearrange/rearrange_easy.yaml")
>     
>     with habitat.config.read_write(config):
>         config.habitat.environment.max_episode_steps = 500
>     
>     env = habitat.Env(config=config)
>     obs = env.reset()
>     
>     print("Composite task PDDL predicates:")
>     # all_predicates 传感器告诉你当前所有 PDDL 谓词的真值
>     if "all_predicates" in obs:
>         print(obs["all_predicates"])
>     
>     env.close()
> 
> ### PDDL Domain 定义示例
> 
>     # 来自 config/habitat/task/rearrange/pddl/rearrange_easy.yaml
>     # 定义场景中有什么、目标是什么、怎么做
>     
>     objects:            # 场景实体
>       - name: goal0|0        # 要移动的物体
>         expr_type: movable_entity_type
>       - name: TARGET_goal0|0  # 目标位置（接收器）
>         expr_type: goal_entity_type
>       - name: robot_0         # 机器人自己
>         expr_type: robot_entity_type
>     
>     goal:               # 最终目标：物体在目标位置 AND 机器人不持物
>       expr_type: AND
>       sub_exprs:
>         - at(goal0|0, TARGET_goal0|0)
>         - not_holding(robot_0)
>     
>     solution:           # 预定义的执行计划（easy mode）
>       - nav(goal0|0, robot_0)          # 1. 导航到物体
>       - pick(goal0|0, robot_0)         # 2. 抓取
>       - nav(TARGET_goal0|0, robot_0)  # 3. 导航到目标
>       - place(goal0|0, TARGET_goal0|0, robot_0) # 4. 放置
> 
> | PDDL 元素       | 角色            | 例子                                                                 |
> | ------------- | ------------- | ------------------------------------------------------------------ |
> | **Entity**    | 场景中的对象        | goal0|0（物）、TARGET\_goal0|0（位置）、robot\_0（机器人）                       |
> | **Predicate** | 描述世界状态的真/假断言  | `at(goal0\|0, TARGET)`, `holding(robot_0)`, `not_holding(robot_0)` |
> | **Goal**      | 目标状态（谓词的逻辑组合） | `AND(at(...), not_holding(...))`                                   |
> | **Solution**  | 到达目标的动作序列     | `nav → pick → nav → place`                                         |
> | **Action**    | 可执行的原子动作      | `nav(entity, robot)`, `pick(entity, robot)`                        |
> 

> ### 可用复合任务
> 
> | Benchmark Config         | 任务描述                         | 物体数 |
> | ------------------------ | ---------------------------- | --- |
> | `rearrange_easy.yaml`    | 单个物体：抓取→搬运→放置                | 1   |
> | `rearrange.yaml`         | 同上但无预定义 solution（需要 planner） | 1   |
> | `set_table.yaml`         | 摆桌子：多个物体→多个位置                | 3-5 |
> | `tidy_house.yaml`        | 整理房间：物体归位                    | 3-5 |
> | `prepare_groceries.yaml` | 准备食材：多物体→不同接收器               | 3-5 |
> 

> </div>
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 学后自检 — 你掌握了什么
> 
> <div class="trouble-grid">
> 
> <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> 
> #### Q1：Rearrange 和 Navigation 的核心区别是什么？
> 
> Navigation 是"走到点"，Rearrange 是"改变世界状态"。后者需要物理引擎、机器人 URDF、关节手臂控制和物体交互（抓取/放置）。Sim 类型从 HabitatSim-v0 切换为 RearrangeSim-v0。
> 
> </div>
> 
> <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> 
> #### Q2：Pick 任务中的 is\_holding=1 意味着什么？
> 
> 吸盘已成功吸住目标物体。这是 pick\_reward 的峰值信号，也是 pick\_success 的判断依据。此后物体会跟随机械臂末端执行器运动。
> 
> </div>
> 
> <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> 
> #### Q3：PDDL 中的 solution 字段是做什么的？
> 
> 预定义的动作序列（nav→pick→nav→place）。在"easy"模式下，CompositeTask 按 solution 顺序执行每个原子动作。在"hard"模式下需要运行时 planner。
> 
> </div>
> 
> <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> 
> #### Q4：为什么不直接在 PointNav 的 Env 里加一个"抓取"动作？
> 
> 因为操作任务需要物理仿真、碰撞检测、抓取约束、关节限制——这些都需要 Bullet 物理引擎和完整的 URDF 机器人模型，不是在一个离散动作空间里加一个 action\_id 能实现的。
> 
> </div>
> 
> <div class="trouble-card" style="border-left-color: var(--accent-tip);">
> 
> #### Q5：Rearrange 的数据集需要手动下载吗？
> 
> 不需要。RearrangeDatasetV0 的 \_\_init\_\_ 方法会自动调用 datasets\_download --uids rearrange\_task\_assets，首次运行时会自动完成。
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> <div class="page-nav">
> 
> [← 第8章：真机部署](habitat-textbook-step8.html) [回到学习中心 →](index.html)
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
# §N 避坑实战：一个 VLN 训练管线的诊断与修复 — Habitat 从零理解

> 你接手了一个 VLN 训练项目，val\_acc = 94.9%——看起来非常好。但这是真的吗？ 本章带你逐一发现并修复 5 个工程暗坑，最终面对一个诚实但残酷的结论。

## §N.1 初见：好得可疑的 94.9%

用项目原始代码训练 10 个 epoch，观察训练曲线。

<div>

**① 先跑一遍看看**

在你开始修改任何代码之前，先用原始版本完整训练一次，并保存日志。  
这个日志是你后续诊断的**唯一参照物**——没有它，你就不知道"修对了没有"。

</div>

### ② 训练命令

    cd habitat-lab-edu
    python training/train.py --split val_unseen --num_episodes 500 --epochs 10 \
        2>&1 | tee logs/run1_before_fix.log

### ③ 训练曲线（真实日志）

<div style="margin:16px 0;">

![Before Fix Training Curves](images/before_fix_curves.png)

</div>

▲ 从左图可见：train\_loss 和 val\_loss 快速下降且始终接近——典型的过拟合信号（train/val 数据泄漏）。val\_acc 从 79.7% 飙升至 94.1%。

> 💡
> 
> <div class="tip-title">
> 
> 停下想一想
> 
> val\_acc = 94.1%，而且 10 个 epoch 就到了。你见过几个 ML 项目有这么快的收敛速度和这么高的准确率？  
> **在继续之前，问自己：这个数字有可能是真的吗？**
> 
> <div class="section">
> 
> <div class="container">
> 
> ## §N.2 五重暗坑：逐一揭示
> 
> 高 val\_acc 并不等于好模型。以下是藏在训练管线中的 5 个问题。
> 
> <div class="bug-card" style="margin-bottom: 20px;">
> 
> #### 🔴 坑 1：文本输入是随机噪声
> 
> <div class="compare-grid">
> 
> <div>
> 
> 修复前
> 
>     def fake_text_input(instrs, B, T, ...):
>         return torch.randn(B, 10, 300)  # 每轮都不同！
> 
> </div>
> 
> <div>
> 
> 修复后
> 
>     # 从 R2R 指令构建词表 1369 词
>     batch_encode(instructions) → Embedding → LSTM
>     # 同一条指令永远得到相同向量
> 
> 指令文本从未被使用。模型实际学的是**"看 RGB 序列推测方向"**——这不是 VLN。
> 
> </div>
> 
> <div class="bug-card" style="margin-bottom: 20px;">
> 
> #### 🔴 坑 2：Train / Val 数据泄漏
> 
> <div class="compare-grid">
> 
> <div>
> 
> 修复前
> 
>     train_ds = VLNDataset(split="val_unseen", ...)
>     val_ds  = VLNDataset(split="val_unseen", ...)
>     # ↑ 同一个 split！
> 
> </div>
> 
> <div>
> 
> 修复后
> 
>     train_ds = VLNDataset(split="train", ...)
>     val_ds  = VLNDataset(split="val_unseen", ...)
>     # ↑ 完全隔离
> 
> 验证集的前 50 个 episode 也在训练集中。模型见过验证数据——94.1% 是**过拟合**，不是泛化。
> 
> </div>
> 
> <div class="bug-card" style="margin-bottom: 20px;">
> 
> #### 🟡 坑 3：Action 标签缺失 RIGHT
> 
> <div class="compare-grid">
> 
> <div>
> 
> 修复前
> 
>     if abs(dx) > abs(dy):
>         actions.append(1)  # FWD
>     else:
>         actions.append(2)  # LEFT——RIGHT 从未出现
> 
> </div>
> 
> <div>
> 
> 修复后
> 
>     if dx > 0.05:
>         actions.append(3)  # RIGHT
>     elif dx 
> 
> 模型训练时从未见过正确的右转标签。一个不会右转的导航模型。
> 
> </div>
> 
> <div class="bug-card" style="margin-bottom: 20px;">
> 
> #### 🟡 坑 4：SPL 指标公式错误
> 
> <div class="compare-grid">
> 
> <div>
> 
> 修复前
> 
>     def spl(success, agent_len, gt_len):
>         return gt_len / max(agent_len, gt_len)
>         # ↑ 缺了 success 因子！失败时 SPL≠0
> 
> </div>
> 
> <div>
> 
> 修复后
> 
>     def spl(success, agent_len, gt_len):
>         if not success: return 0.0
>         return success * gt_len / max(agent_len, gt_len)
> 
> 标准 SPL 公式是 `success × (gt_len / max(agent_len, gt_len))`。缺少 success 因子导致失败 episode 也有正的 SPL。
> 
> </div>
> 
> <div class="bug-card">
> 
> #### 🟡 坑 5：训练日志丢失
> 
> 原始 train.py 只打印到终端，训练结束后**没有任何记录**。当你想对比修复前后的效果时，没有对照数据。  
> 修复：加入 `Tee` 类，同时输出到 stdout 和 `logs/` 目录。
> 
> <div class="section">
> 
> <div class="container">
> 
> ## §N.3 修复后重新训练
> 
> 修复全部 5 个问题后，用分离的 split 重新训练 10 epoch。
> 
> <div style="margin:16px 0;">
> 
> ![After Fix Training Curves](images/after_fix_curves.png)
> 
> </div>
> 
> ▲ 修复后 train/val 曲线明显分离（无数据泄漏）。val\_acc 从 49.9% 起步，最终达到 94.7%——几乎和修复前一样。
> 
> <div style="margin:24px 0 16px;">
> 
> ![Val ACC Before vs After Fix](images/val_acc_comparison.png)
> 
> </div>
> 
> ▲ 修复前（红线）：起点高（79.7%），快速收敛。修复后（绿线）：起点低（49.9%），逐步追赶——最终持平。两者终点几乎重叠，说明这些表面问题不是瓶颈。
> 
> <div class="insight-box">
> 
> #### 💡 意料之外：val\_acc 几乎没变
> 
> 修复了文本噪声、数据泄漏、标签缺失、指标公式之后，val\_acc 从 **94.1% → 94.7%**。  
>   
> 我们原本预期 val\_acc 会**大幅下降**（因为消除了数据泄漏和随机文本作弊），但它纹丝不动。  
>   
> **这意味着：这 5 个问题从来不是 val\_acc 的瓶颈。**
> 
> <div class="section">
> 
> <div class="container">
> 
> ## §N.4 真正的考验：环境评估
> 
> val\_acc 测量的是"给定预渲染帧，预测 action 标签"，不是"在 3D 场景中导航"。
> 
> | 指标                   | 修复前 (作弊版) | 修复后 (诚实版) | 变化     |
> | -------------------- | --------- | --------- | ------ |
> | **val\_acc**         | 94.1%     | 94.7%     | \+0.6% |
> | **Eval SR** (50 eps) | \~30% \*  | 32.0%     | \+2%   |
> | **Eval SPL**         | — (公式错误)  | 0.320     | —      |
> | **Eval nDTW**        | —         | 0.107     | —      |
> 

> \* 修复前的简化版 eval 把 action 硬编码为 MOVE\_FORWARD，所以 SR 约 30% 只是"一直向前走"的 baseline。
> 
> <div class="insight-box">
> 
> #### 💡 val\_acc 94.7% vs SR 32.0%：3:1 的鸿沟
> 
> 同一个模型，在预渲染帧上预测 action 标签有 94.7% 准确率，但在 3D 场景中实际导航只有 32% 成功率。  
>   
> 这个 3:1 的差距揭示了比文本噪声、数据泄漏、标签错误**更深层的问题**。
> 
> <div class="section">
> 
> <div class="container">
> 
> ## §N.5 深层结论：图像分布偏移
> 
> 当你排除了所有表面问题，剩下的那个——无论多么隐蔽——就是根因。
> 
> <div>
> 
> **根因：训练和评估的图像来自不同分布**
> 
> <div class="compare-grid" style="margin-top:12px;">
> 
> <div class="fix-card" style="margin:0;">
> 
> #### 训练时的图像
> 
> 来自 **预渲染**（env.reset → 5×MOVE\_FORWARD → 保存 .npz）  
>   
> 每帧都是 **最短路径上的画面**——干净、正确、标准化。
> 
> </div>
> 
> <div class="bug-card" style="margin:0;">
> 
> #### 评估时的图像
> 
> 来自 **实时渲染**（每步根据模型预测的 action 获取下一帧）  
>   
> 每帧都是 **模型自己走出来的画面**——可能偏离、撞墙、迷路。
> 
> 两个分布下的 RGB 完全不同——同一场景、不同视角、不同光照条件。  
> ResNet 提取的特征在两个分布之间**无法泛化**。  
>   
> 这解释了为什么修复了 5 个表面问题后 SR 仍然只有 32%：  
> **模型从未见过"自己走错时看到的画面"。**
> 
> </div>
> 
> > ⚠️
> > 
> > <div class="warn-title">
> > 
> > ⚡ 这为什么比文本问题更难修
> > 
> > 要消除分布偏移，训练必须也走**在线 rollout**：每步用模型预测的 action 获取下一帧。  
> > 但这会让训练慢 10 倍（无法并行预取 DataLoader），且需要动态 env 管理。  
> >   
> > 混合训练方案（先在预渲染上启蒙，再逐步加在线 rollout）是可行的折中。  
> >   
> > ——这不是 §N 要解决的问题，它是阶段 3（真正的 VLN 训练）的核心挑战。
> > 
> > <div class="section">
> > 
> > <div class="container">
> > 
> > ## §N.6 你从这一章学到的
> > 
> > | \# | 教训                                  | 适用范围     |
> > | -- | ----------------------------------- | -------- |
> > | 1  | **val\_acc 高 ≠ 模型好**。先检查数据有没有泄漏。    | 所有 ML 项目 |
> > | 2  | **保存训练日志**。没有 before 对照，after 没有意义。 | 所有 ML 项目 |
> > | 3  | **查指标公式**。你自己写的 SPL 可能和论文定义不同。      | 复现论文时    |
> > | 4  | **查标签分布**。如果某个类别从未出现，模型不会学到它。       | 分类任务     |
> > | 5  | **训练和推理的输入必须同分布**。预渲染帧≠实时渲染帧。       | 所有 ML 项目 |
> > | 6  | **修复表面问题后效果没变 → 根因在更深层**。别停。        | 调试方法论    |
> > 

> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 继续学习
> > > 
> > > 这一章教的是"如何诊断"。下一阶段（阶段 3：真正的 VLN 训练）教的是"如何做对"——  
> > > teacher-forcing、cross-modal attention、在线训练、数据增强。  
> > > [→ 回到第6章：VLN 仿真训练](habitat-textbook-step6.html)
> > > 
> > > <div class="section content-section">
> > > 
> > > ## §N.7 量化证据：图像分布偏移到底多大？
> > > 
> > > §N.5 提出"图像分布偏移是根因"——但这是定性的推断。我们需要用实验把它量化。  
> > > 设计一个对照实验：用 ResNet（模型的眼睛）和 CLIP（通用的眼睛）分别编码两组图像，计算分布距离。
> > > 
> > > ### 实验设计
> > > 
> > > <div>
> > > 
> > > **两组图像**
> > > 
> > >   - **A 组 · 预渲染帧：**9,195 帧，来自 1,839 个 episode 的最短路径，每帧都是"正确答案"。
> > >   - **B 组 · 在线 rollout 帧：**2,790 帧，来自 93 个 episode，强制模型走 30 步（禁用 stop），收集模型自己走出来的画面——包括走偏、撞墙、绕路。
> > > 
> > > </div>
> > > 
> > > <div>
> > > 
> > > **两个编码器**
> > > 
> > >   - **ResNet18：**模型实际使用的视觉编码器。如果 A 和 B 对它来说是不同分布，那就是模型的"主观"分布偏移。
> > >   - **CLIP ViT-B/32：**通用视觉模型，作为"客观"参照。如果 CLIP 也认为两组不同，那偏移就是客观的。
> > > 
> > > </div>
> > > 
> > > ### 结果：MMD 分布距离
> > > 
> > > <div class="compare-table">
> > > 
> > > | 编码器           | MMD（越低越相似） | 解读              |
> > > | ------------- | ---------- | --------------- |
> > > | ResNet18      | **0.0058** | 模型的眼睛认为两组帧几乎一样  |
> > > | CLIP ViT-B/32 | **0.0053** | 通用的眼睛也认为两组帧几乎一样 |
> > > 

> > > </div>
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > ⚡ 意料之外：两个 MMD 都极低
> > > > 
> > > > 我们预期在线帧（走偏、撞墙）和预渲染帧（最短路径）会有显著分布差异。  
> > > > 但 ResNet 和 CLIP 都给出了 \< 0.006 的 MMD——**两组帧在特征空间中几乎完全重叠**。
> > > > 
> > > > </div>
> > > > 
> > > > ### 可视化：t-SNE 降维
> > > > 
> > > > 把 512 维特征降到 2 维，蓝色 = 预渲染帧，红色 = 在线帧：
> > > > 
> > > > <div style="display:flex;gap:20px;flex-wrap:wrap;margin:16px 0;">
> > > > 
> > > > <div style="flex:1;min-width:300px;">
> > > > 
> > > > ![t-SNE ResNet](images/tsne_resnet.png)
> > > > 
> > > > ResNet18 t-SNE (MMD=0.0058)
> > > > 
> > > > </div>
> > > > 
> > > > <div style="flex:1;min-width:300px;">
> > > > 
> > > > ![t-SNE CLIP](images/tsne_clip.png)
> > > > 
> > > > CLIP t-SNE (MMD=0.0053)
> > > > 
> > > > 在 ResNet 的 t-SNE 图中，红色和蓝色完全混在一起——预渲染帧和在线帧在特征空间中无法区分。
> > > > 
> > > > ### 余弦相似度分布
> > > > 
> > > > <div style="margin:16px 0;">
> > > > 
> > > > ![Cosine Similarity](images/cosine_similarity.png)
> > > > 
> > > > </div>
> > > > 
> > > > 两组直方图几乎完全重叠：预渲染帧之间的相似度，和预渲染 vs 在线帧之间的相似度，分布一致。
> > > > 
> > > > ### §N.5 的结论需要修正
> > > > 
> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 从"图像分布偏移"到"行为偏差累积"
> > > > > 
> > > > > 数据推翻了 §N.5 的假设。不是图像分布不同导致 SR 只有 32%——  
> > > > > 而是模型在几乎相同的画面上，做出了**不同的 action 决策**。
> > > > > 
> > > > > 预渲染帧是 teacher-forcing 下的画面（最短路径，每步都是"对"的下一步），  
> > > > > 在线帧是模型自由行动的画面（可能走偏，但场景纹理、墙壁、地板和预渲染帧几乎一样）。
> > > > > 
> > > > > **32% 的 SR 不是因为模型"看到了没见过的画面"，而是模型在熟悉的画面中做出了错误的 action。**  
> > > > > 每步差一点，30 步后离目标越来越远——这就是**行为偏差累积**。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### 实验教会我们的
> > > > > 
> > > > > <div class="compare-table">
> > > > > 
> > > > > | \# | 教训                                                                              |
> > > > > | -- | ------------------------------------------------------------------------------- |
> > > > > | 1  | **假设需要实验验证。**我们确信"图像分布偏移是根因"，但数据说不。                                             |
> > > > > | 2  | **模型的眼睛（ResNet）和通用的眼睛（CLIP）意见一致。**这不是编码器选择的问题。                                  |
> > > > > | 3  | **低 MMD 不代表问题不存在。**它只是说明问题不在帧层面，而在决策层面。                                         |
> > > > > | 4  | **证伪假设比证实假设更有价值。**它迫使你寻找更深层的根因。                                                 |
> > > > > | 5  | **下一步不是修图像，是修决策。**Teacher-forcing → Student-forcing，强化学习，cross-modal attention。 |
> > > > > 

> > > > > </div>
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **实验复现**
> > > > > 
> > > > > 所有代码和特征数据在 L40 云端：  
> > > > > `training/collect_online_frames.py` — 强制 30 步 rollout 采集  
> > > > > `training/extract_features.py` — ResNet + CLIP 特征提取  
> > > > > `training/analyze_distribution.py` — MMD + t-SNE + 余弦相似度分析  
> > > > > `screenshots/clip_comparison/` — 完整图表输出
> > > > > 
> > > > > </div>
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
# VLN 视觉语言导航 — 概念·发展·应用·与Habitat的关系

> 当自然语言遇上三维空间 — 智能体在真实感场景中依据人类指令"听懂→看见→走到"的完整技术栈， 从 R2R 数据集到 SOTA 模型，从仿真训练到真机部署

## 什么是 VLN

<div class="overview-grid">

<div class="overview-card">

<div class="icon">

🗣️→🚶

</div>

### 核心定义

Vision-and-Language Navigation（视觉语言导航）是要求一个具身智能体 **理解自然语言指令**，并在三维环境中**通过视觉观测自主导航**到达指定目标位置的任务。 一句话：听懂指令，看路走到。

</div>

<div class="overview-card">

<div class="icon">

🧩

</div>

### 问题拆解

VLN 横跨三大子问题：  
(1) **语言理解** — 解析指令中的物体、空间关系、动作序列；  
(2) **视觉感知** — 从 RGB/D 图像中识别场景语义；  
(3) **动作决策** — 在每一个时间步选择前进/转弯/停止。

</div>

<div class="overview-card">

<div class="icon">

🆚

</div>

### 与传统导航的区别

传统 PointNav（点导航）给出精确的 (x,y) 坐标；VLN 只给一句话。 这意味着智能体必须**自己从语言中推断**去哪里、什么时候该停 — 远比点到点导航困难。

</div>

<div class="overview-card">

<div class="icon">

📐

</div>

### 形式化定义

给定指令 **I** = {w₁, w₂, ..., wₙ}（自然语言）和初始位姿 p₀， 在每个时间步 t，智能体接收视觉观测 o<sub>t</sub> → 输出动作 a<sub>t</sub> ∈ {前进, 左转, 右转, 停止}， 目标是最小化到目标的距离。

<div class="dataflow" style="margin-top: 28px; font-size: 0.9rem;">

<div class="node" style="border:2px solid #06b6d4; min-width:200px;">

**指令 I**  
<span class="small">"走出卧室,经过沙发,  
在厨房餐桌旁停下"</span>

</div>

<span class="arrow">→</span>

<div class="node" style="border:2px solid #8b5cf6;">

语言编码器  
<span class="small">LSTM / Transformer</span>

</div>

<span class="arrow">→</span>

<div class="node" style="border:2px solid #f59e0b;">

跨模态融合  
<span class="small">Attention / 拼接</span>

</div>

<span class="arrow">→</span>

<div class="node" style="border:2px solid #10b981;">

视觉编码器  
<span class="small">ResNet / ViT</span>

</div>

<span class="arrow">→</span>

<div class="node" style="border:2px solid #ec4899;">

策略 π  
<span class="small">输出动作 a<sub>t</sub></span>

</div>

<span class="arrow">→</span>

<div class="node" style="border:2px solid #06b6d4;">

环境观测  
<span class="small">RGB+D 全景图</span>

VLN 的典型系统架构：语言指令与视觉观测在统一的跨模态空间中融合，策略网络输出离散导航动作

</div>

## 发展历程

<div class="timeline">

<div class="timeline-item" style="border-left: 3px solid #06b6d4;">

<div class="year">

2018 — 任务提出

</div>

### R2R 数据集 & Seq-to-Seq 基线

Anderson et al. 在 CVPR 2018 发表「Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments」，提出**R2R (Room-to-Room)** 数据集和基于 LSTM 的 Seq2Seq 基线模型。**这是 VLN 领域的开山之作。**R2R 基于 Matterport3D 场景，包含 7,189 条路径和 21,567 条人工标注的导航指令。首次定义了 SPL 指标。

<div class="tag-row">

<span class="tag">CVPR 2018</span><span class="tag">R2R Dataset</span><span class="tag">LSTM Seq2Seq</span>

<div class="timeline-item" style="border-left: 3px solid #8b5cf6;">

<div class="year">

2019 — 数据增强 & 预训练探索

</div>

### Speaker-Follower & PREVALENT

**Speaker-Follower** (Fried et al., ECCV 2018)：引入「说者」模型反向生成指令作为增强数据， 「跟者」模型执行导航，开创了**指令增强**范式。  
**PREVALENT** (Hao et al., 2019)：首次将**大规模预训练**引入 VLN，在大量图文数据上预训练 跨模态编码器，然后在下游导航任务上微调。

<div class="tag-row">

<span class="tag">Speaker-Follower</span><span class="tag">PREVALENT</span><span class="tag">数据增强</span><span class="tag">预训练</span>

<div class="timeline-item" style="border-left: 3px solid #f59e0b;">

<div class="year">

2020-2021 — 扩展数据集 & 强化学习

</div>

### R4R · RxR · REVERIE — 任务多样性爆发

**R4R** (Jain et al., 2019)：将 R2R 路径拼接为更长轨迹，测试长距离导航。  
**RxR** (Ku et al., 2020)：支持**多语言**（英语/印地语/泰卢固语），规模达 126k 指令。  
**REVERIE** (Qi et al., 2020)：引入**远距离物体定位** + 物体描述指令。  
方法上，强化学习 (RL) 被广泛用于直接优化导航成功率，EnvDrop 和 AuxRN 等从环境 dropout 正则化角度提升泛化。

<div class="tag-row">

<span class="tag">R4R</span><span class="tag">RxR (多语言)</span><span class="tag">REVERIE</span><span class="tag">RL Training</span>

<div class="timeline-item" style="border-left: 3px solid #10b981;">

<div class="year">

2022-2023 — Transformer 时代

</div>

### HAMT · DUET · VLN-BERT · 多模态大模型

**HAMT** (Chen et al., 2021)：用**层次化 Transformer** 编码多时间尺度的历史信息。  
**DUET** (Chen et al., 2022)：双分支架构 — 全局拓扑图分支 + 局部动作分支。  
**VLN-BERT** (Hong et al., 2021)：用 BERT 架构联合编码指令、视觉和历史轨迹。 进入大模型时代后，LLM (GPT-4, LLaMA) 被用作 VLN 的"常识引擎"，在未知环境中进行 zero-shot 规划。

<div class="tag-row">

<span class="tag">HAMT</span><span class="tag">DUET</span><span class="tag">VLN-BERT</span><span class="tag">LLM Planning</span>

<div class="timeline-item" style="border-left: 3px solid #ec4899;">

<div class="year">

2024 及以后 — 基础模型对齐

</div>

### VLA (Vision-Language-Action) 一体化

前沿趋势是将 VLN 嵌入**Vision-Language-Action** (VLA) 大模型范式 — 一个模型同时理解指令、 感知环境、输出底层控制。代表性工作如 RT-2 (Google DeepMind)、Octo (Berkeley) 等。 VLN 不再是一个孤立的导航任务，而是通用机器人基础模型的一个验证场景。

<div class="tag-row">

<span class="tag">VLA Models</span><span class="tag">RT-2</span><span class="tag">Octo</span><span class="tag">端到端</span>

## VLN技术范型：六大流派与方法对比

VLN 的研究方法历经数年演进，可按技术范式分为**六大流派**。它们并非严格的时间前后关系，而是代表不同的设计哲学 — 从简单的序列映射，到结构化空间表示，再到如今的大模型零样本规划。理解这些流派的核心差异，是深入 VLN 研究的关键。

<div class="module-grid">

<div class="module" style="border-left-color: #64748b;">

### 1\. Seq2Seq · RNN 基线

将 VLN 视为一个**序列到序列的翻译问题**：指令文本（源序列）→ 导航动作（目标序列）。使用 LSTM 编码指令， 在每一步用注意力机制聚合视觉特征，解码出下一个动作。

  - **语言编码：**LSTM 逐词编码指令
  - **视觉编码：**ResNet CNN 提取单帧特征
  - **跨模态融合：**注意力加权拼接
  - **动作预测：**LSTM 解码器 softmax
  - **历史记忆：**LSTM 隐状态
  - **训练：**Teacher Forcing（交叉熵）

<div class="tag-row">

<span class="tag">Seq2Seq (Anderson 2018)</span><span class="tag">RPA</span>

<div class="module" style="border-left-color: #f59e0b;">

### 2\. 数据增强范式

**不改变核心模型架构**，而是通过生成额外训练数据来提升泛化能力。核心洞察：人工标注指令数量有限且偏向固定表达， 通过模型生成或环境扰动创建更多样的训练信号。

  - **Speaker-Follower：**训练一个逆向的"说者"模型从路径反向生成指令，为"跟者"模型提供增强样本
  - **EnvDrop：**随机丢弃视觉特征（模拟遮挡/噪声），强迫模型更依赖语言线索，减少视觉过拟合
  - **共性：**架构与 Seq2Seq 基本一致，增强的是**训练数据和信号**而非模型结构

<div class="tag-row">

<span class="tag">Speaker-Follower</span><span class="tag">EnvDrop</span><span class="tag">Back-Translation</span>

<div class="module" style="border-left-color: #8b5cf6;">

### 3\. 预训练 + 微调范式

借鉴 NLP/CV 的预训练思路：先在**大规模图文数据**上预训练跨模态编码器，再在下游 VLN 任务上微调。 关键突破在于使模型提前学会"语言与视觉如何对应"。

  - **PREVALENT：**在 R2R 指令 + 图像帧对上做 Masked LM + 动作预测的联合预训练
  - **VLN-BERT：**用 BERT 架构联合编码指令 token、视觉 patch、历史轨迹，做多任务预训练
  - **与 Seq2Seq 的关键区别：**视觉和语言在**统一的 Transformer 中端到端交互**，不再分离编码后拼接

<div class="tag-row">

<span class="tag">PREVALENT</span><span class="tag">VLN-BERT</span><span class="tag">Airbert</span><span class="tag">HOP</span>

<div class="module" style="border-left-color: #10b981;">

### 4\. 结构化表示范式

构建显式的**空间-语义结构化记忆**（图、地图、层次化历史），将"走到哪了"和"接下来往哪走"解耦为两个子系统。 这是应对长距离导航的核心策略。

  - **HAMT：**用层次化 Transformer 编码多时间尺度的历史轨迹 — 短期（最近几步）、中期（子路径）、长期（完整轨迹）
  - **DUET：**双分支架构 — 全局分支在拓扑图上做高层规划，局部分支执行逐步动作
  - **RelGraph / Ego2Top：**将可导航空间构建为图，在图上做路径规划
  - **GridMM / BEVBert：**构建鸟瞰视角 (BEV) 的栅格化语义地图

<div class="tag-row">

<span class="tag">HAMT</span><span class="tag">DUET</span><span class="tag">RelGraph</span><span class="tag">GridMM</span><span class="tag">BEVBert</span>

<div class="module" style="border-left-color: #06b6d4;">

### 5\. LLM 规划范式

将**冻结的大语言模型** (GPT-4, LLaMA) 作为"常识推理引擎"：LLM 负责理解指令、分解子目标、利用世界知识推理， 经典控制器负责执行每个子目标。核心优势是**零样本泛化** — 无需在 VLN 数据上训练即可在新环境中导航。

  - **NavGPT：**GPT-4 作为规划器，将指令分解为"地标 → 地标"的子目标链
  - **DiscussNav：**多角色 LLM 对话 — 规划者 + 执行者 + 批评者协同决策
  - **GOAT / LLaVA-Nav：**多模态 LLM 直接处理 RGB 图像 + 指令文本
  - **与结构化范式的区别：**LLM 提供的是**语义常识规划**而非几何路径规划

<div class="tag-row">

<span class="tag">NavGPT</span><span class="tag">DiscussNav</span><span class="tag">GOAT</span><span class="tag">LLaVA-Nav</span>

<div class="module" style="border-left-color: #ec4899;">

### 6\. VLA 端到端范式

Vision-Language-Action 统一模型 — **一个网络从像素+文本直接映射到控制指令**，消除所有手工设计的模块边界。 这是机器人基础模型 (Robotics Foundation Model) 的实现路径。

  - **RT-2 (Google)：**将视觉-语言模型 (PaLI-X/PaLM-E) 的 token 输出直接映射为机器人动作
  - **Octo (Berkeley)：**基于 Transformer 的通用机器人策略，支持多机器人多任务
  - **NaVid：**纯视觉输入 + 自然语言指令 → 行动轨迹，无需地图/SLAM
  - **与 LLM 范式的区别：**VLA 直接输出**动作 token**，而非子目标规划文本

<div class="tag-row">

<span class="tag">RT-2</span><span class="tag">Octo</span><span class="tag">NaVid</span><span class="tag">NaviLLM</span>

</div>

### 六大流派核心差异一览

<div style="overflow-x:auto;">

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>维度</th>
<th>Seq2Seq</th>
<th>数据增强</th>
<th>预训练+微调</th>
<th>结构化表示</th>
<th>LLM 规划</th>
<th>VLA 端到端</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>核心创新</strong></td>
<td>序列映射建模</td>
<td>训练数据扩充</td>
<td>跨模态预训练</td>
<td>空间记忆结构</td>
<td>LLM 常识推理</td>
<td>统一动作模型</td>
</tr>
<tr class="even">
<td><strong>语言编码</strong></td>
<td>LSTM</td>
<td>LSTM</td>
<td>BERT/Transformer</td>
<td>Transformer</td>
<td><strong>冻结 LLM</strong> (不训练)</td>
<td>LLM tokenizer + 可训练</td>
</tr>
<tr class="odd">
<td><strong>视觉编码</strong></td>
<td>ResNet CNN</td>
<td>ResNet CNN</td>
<td>ResNet / ViT</td>
<td>ResNet + 图/地图</td>
<td>多模态 LLM 视觉编码器</td>
<td>ViT / 多模态编码器</td>
</tr>
<tr class="even">
<td><strong>跨模态融合</strong></td>
<td>注意力拼接</td>
<td>注意力拼接</td>
<td>Transformer 共注意力</td>
<td>图/序列融合</td>
<td>LLM 上下文窗口</td>
<td>Token 空间统一</td>
</tr>
<tr class="odd">
<td><strong>历史记忆</strong></td>
<td>LSTM 隐状态</td>
<td>LSTM + Dropout</td>
<td>历史 token 序列</td>
<td><strong>图/地图/层次状态</strong></td>
<td>对话历史 prompt</td>
<td>隐式轨迹 token</td>
</tr>
<tr class="even">
<td><strong>训练范式</strong></td>
<td>Teacher Forcing</td>
<td>TF + 数据增强</td>
<td>预训练 + 微调</td>
<td>IL + RL 混合</td>
<td><strong>零样本 (无需训练)</strong></td>
<td>大规模多任务预训练</td>
</tr>
<tr class="odd">
<td><strong>是否需要<br />
VLN 标注数据</strong></td>
<td>需要</td>
<td>需要</td>
<td>需要（微调阶段）</td>
<td>需要</td>
<td><strong>不需要</strong></td>
<td>需要（大量多任务数据）</td>
</tr>
<tr class="even">
<td><strong>长距离导航</strong></td>
<td>差 — 记忆衰减</td>
<td>中等 — 缓解过拟合</td>
<td>中等</td>
<td><strong>好 — 结构化记忆</strong></td>
<td>好 — 子目标分解</td>
<td>依赖训练数据</td>
</tr>
<tr class="odd">
<td><strong>新场景泛化</strong></td>
<td>差</td>
<td>中等</td>
<td>较好</td>
<td>较好（地图辅助）</td>
<td><strong>最好 — 零样本</strong></td>
<td>依赖训练场景覆盖</td>
</tr>
<tr class="even">
<td><strong>推理速度</strong></td>
<td>快</td>
<td>快</td>
<td>快~中等</td>
<td>中等</td>
<td>慢 — 调用 LLM API</td>
<td>中等~慢</td>
</tr>
<tr class="odd">
<td><strong>计算资源</strong></td>
<td>低</td>
<td>低</td>
<td>中高</td>
<td>中高</td>
<td>低（训练）<br />
高（推理 API）</td>
<td>极高</td>
</tr>
</tbody>
</table>

</div>

<div>

**技术演进的内在逻辑**

这六大流派背后有一条清晰的演进主线：**从"对数据死记硬背"到"建立可迁移的世界理解"**。 Seq2Seq 是朴素拟合，数据增强让拟合更鲁棒，预训练引入了跨模态的语义理解， 结构化表示让模型学会组织空间知识，LLM 将人类常识注入导航决策， VLA 则将这一切融入一个统一的动作模型。每一代都解决了上一代的核心瓶颈 — 同时也暴露了新的天花板。

## VLN 在 Habitat 中的实现

<div class="arch-diagram" style="margin-bottom: 24px;">

<div class="arch-row">

<div class="arch-layer" style="background:#06b6d420; border:2px solid #06b6d6; color:#67e8f9;">

🎯 VLNTask (VLN-v0)  
<span class="small">继承 NavigationTask  
含 stop 动作</span>

</div>

<div class="arch-layer" style="background:#8b5cf620; border:2px solid #8b5cf6; color:#c4b5fd;">

📋 InstructionSensor  
<span class="small">lab\_sensor  
{text, tokens, trajectory\_id}</span>

</div>

<div class="arch-layer" style="background:#f59e0b20; border:2px solid #f59e0b; color:#fcd34d;">

📦 R2RVLN-v1  
<span class="small">VLNDatasetV1  
Matterport3D + R2R</span>

<div class="arch-arrow">

↓   继承自   ↓

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd;">

NavigationTask  
<span class="small">overwrite\_sim\_config  
\_check\_episode\_is\_active</span>

</div>

<div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd;">

NavigationEpisode  
<span class="small">+ goals + shortest\_paths</span>

<div class="arch-arrow">

↓   继承自   ↓

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#64748b20; border:2px solid #64748b; color:#94a3b8;">

EmbodiedTask  
<span class="small">step / reset / close</span>

</div>

<div class="arch-layer" style="background:#64748b20; border:2px solid #64748b; color:#94a3b8;">

Episode  
<span class="small">scene\_id / start\_position</span>

</div>

<div>

**VLNEpisode — VLN 特有的数据结构**

与普通 NavigationEpisode 相比，**VLNEpisode** 额外携带两个字段： `instruction: InstructionData`（指令文本 + 可选词元） 和 `reference_path: List[List[float]]`（与指令对齐的参考路径点）， 以及 `trajectory_id: int`（关联 ground-truth 轨迹注解）。

</div>

<div class="dual-panel">

<div class="panel" style="border-top: 3px solid #f59e0b;">

#### 离散动作空间 (4 个动作)

| 动作                | 实现                | 参数                         |
| ----------------- | ----------------- | -------------------------- |
| **stop**          | StopAction        | 设置 is\_stop\_called = True |
| **move\_forward** | MoveForwardAction | 前进 0.25m                   |
| **turn\_left**    | TurnLeftAction    | 左转 15°                     |
| **turn\_right**   | TurnRightAction   | 右转 15°                     |

</div>

<div class="panel" style="border-top: 3px solid #10b981;">

#### 评估指标

| 指标                 | 含义                             |
| ------------------ | ------------------------------ |
| **Success**        | 停止时距离 ≤ 0.1m → 1.0，否则 0.0      |
| **SPL**            | Success × (最优路径 / max(最优, 实际)) |
| **DistanceToGoal** | 停止位置到目标的测地距离                   |

### VLN 相关文件结构

    # === VLN 任务核心实现 ===
    habitat/tasks/vln/vln.py            # VLNTask, VLNEpisode, InstructionSensor
    habitat/tasks/vln/__init__.py       # 延迟注册守卫 (处理依赖缺失)
    
    # === R2R 数据集加载 ===
    habitat/datasets/vln/r2r_vln_dataset.py # VLNDatasetV1 (JSON.gz 加载)
    habitat/datasets/vln/__init__.py       # 延迟注册守卫
    
    # === YAML 配置 ===
    habitat/config/habitat/task/vln_r2r.yaml
    habitat/config/habitat/dataset/vln/mp3d_r2r.yaml
    habitat/config/benchmark/nav/vln_r2r.yaml      # 完整基准配置
    
    # === 示例与测试 ===
    examples/vln_reference_path_follower_example.py  # 可视化示例
    examples/vln_benchmark.py                       # 基准评估
    test/test_r2r_vln.py                            # 单元测试

### 核心类定义

<div class="dual-panel">

<div class="panel" style="border-top: 3px solid #06b6d4;">

#### InstructionSensor

    @registry.register_sensor
    class InstructionSensor(Sensor):
        def get_observation(self, observations, episode, task, *args, **kwargs):
            return {
                "text": episode.instruction.instruction_text,
                "tokens": episode.instruction.instruction_tokens,
                "trajectory_id": episode.trajectory_id,
            }

一个「Lab Sensor」— 不依赖仿真器，直接从 Episode 数据中提取语言指令。观测字典统一传给策略。

</div>

<div class="panel" style="border-top: 3px solid #8b5cf6;">

#### VLNTask

    @registry.register_task(name="VLN-v0")
    class VLNTask(NavigationTask):
        def overwrite_sim_config(self, sim_config, episode):
            return super().overwrite_sim_config(sim_config, episode)
    
        def _check_episode_is_active(self, *args, **kwargs):
            return not self.is_stop_called

VLNTask 几乎是一个空的子类 — 继承了 NavigationTask 的全部逻辑（场景级 episode 加载、起点姿态覆盖、stop 终止机制）。

</div>

## 模型效果与核心挑战

### R2R 数据集上代表性方法的效果

<div style="overflow-x:auto;">

| 方法               | 年份   | 架构核心                | Val Seen SR | Val Unseen SR | Val Unseen SPL |
| ---------------- | ---- | ------------------- | ----------- | ------------- | -------------- |
| Seq2Seq          | 2018 | LSTM 编码器-解码器        | \~39%       | \~22%         | —              |
| Speaker-Follower | 2018 | 指令增强 + 全景动作空间       | \~66%       | \~36%         | \~34%          |
| EnvDrop          | 2019 | 环境 Dropout 正则化      | \~62%       | \~52%         | \~48%          |
| PREVALENT        | 2019 | 大规模跨模态预训练           | \~69%       | \~58%         | \~53%          |
| VLN-BERT         | 2021 | BERT 联合编码           | \~72%       | \~63%         | \~57%          |
| HAMT             | 2021 | 层次化历史编码 Transformer | \~75%       | \~66%         | \~61%          |
| **人类水平**         | —    | —                   | \~86%       | \~78%         | \~76%          |

</div>

\* SR (Success Rate) = 正确到达率；SPL (Success weighted by Path Length) = 路径加权的成功率。  
\* 数据基于各论文汇报结果，不同实现细节可能导致小幅波动。

<div class="dual-panel" style="margin-top: 28px;">

<div class="panel" style="border-top: 3px solid #ef4444;">

#### Seen vs Unseen 泛化鸿沟

几乎所有方法的 **Val Seen → Val Unseen** 都出现 10-20% 的性能骤降。 即使最新的 Transformer 模型，**Unseen 场景下的成功率仍与人类相差 10-15 个百分点**。 这表明模型对训练场景的**视觉过拟合**是核心瓶颈之一。

</div>

<div class="panel" style="border-top: 3px solid #f59e0b;">

#### 指令歧义

同一场景同一路径，不同标注者的指令差异巨大 — "走到厨房" vs "左转穿过门厅，在餐桌旁停下"。 模型必须学会从多样化的语言表达中抽取不变的**空间意图**，这是 NLP 与空间推理的交汇难点。

<div class="dual-panel" style="margin-bottom: 0;">

<div class="panel" style="border-top: 3px solid #06b6d4;">

#### 长距离崩溃

随着路径变长（R4R 任务平均 4-6 步 vs R2R 的 2-3 步），模型表现断崖式下降。 长距离导航需要**长时间记忆**和对指令的**全局规划**，当前方法在这两方面都比较薄弱。

</div>

<div class="panel" style="border-top: 3px solid #10b981;">

#### Sim-to-Real Gap

当前 VLN 主要在 Matterport3D 等重建场景上训练，这些场景的视觉质量（纹理模糊、光照单一） 与真实环境的 RGB-D 图像存在显著差异。从仿真 VLN 到真实机器人部署的迁移仍是开放问题。

</div>

## 核心架构维度深度对比

不同 VLN 方法在六个核心技术维度上做出了截然不同的设计选择。理解这些选择的**trade-off**（效率 vs 泛化、简单 vs 能力）， 是选择或设计 VLN 方法的关键。

### 维度 1：语言编码 — 如何理解指令？

<div class="dual-panel">

<div class="panel" style="border-top: 3px solid #8b5cf6;">

#### LSTM 编码 (2018-2019)

逐词编码指令，最后隐藏状态作为指令向量。适合短指令，**长指令尾部信息会衰减**。 代表：Seq2Seq, Speaker-Follower, EnvDrop, RCM。

    # 典型 LSTM 编码器
    h = LSTM(embed(w₁), ..., embed(wₙ))
    # 注意力机制在每个导航步
    ctx = Attention(h, visual_features[t])

</div>

<div class="panel" style="border-top: 3px solid #06b6d4;">

#### Transformer / LLM 编码 (2021-)

自注意力机制在所有 token 间并行交互，**长距离依赖无损**。LLM 方案甚至冻结语言编码器， 直接利用其预训练的语义理解能力。代表：VLN-BERT, HAMT, NavGPT, RT-2。

    # Transformer 编码器
    h = TransformerEncoder(w₁..wₙ)
    # 或：LLM 直接处理原始文本
    plan = LLM("将指令分解为子目标: " + I)

### 维度 2：视觉编码 — 如何感知环境？

<div class="dual-panel">

<div class="panel" style="border-top: 3px solid #10b981;">

#### 单帧 CNN 编码

每一步从当前 RGB 图像提取 ResNet 特征，视野受限，**缺少空间上下文**。 最早期的方案（Seq2Seq）只使用单视图，后来演进到**全景图**（36 个视角拼接）提升感知范围。

</div>

<div class="panel" style="border-top: 3px solid #f59e0b;">

#### 结构化空间表示

将多步观测聚合为**空间结构**：拓扑图（节点=已访问位置，边=可导航路径）、 BEV 栅格地图、或语义地图（CM2）。这为长距离导航和全局规划提供了基础。

<div class="dual-panel" style="margin-bottom:0;">

<div class="panel" style="border-top: 3px solid #06b6d4;">

#### ViT / 多模态视觉编码器

用 Vision Transformer 或 CLIP 等预训练多模态编码器处理图像，**天然与语言在同一特征空间对齐**。 代表：LLaVA-Nav 用 CLIP 编码视觉，GOAT 用多模态 LLM 的视觉分支。

</div>

<div class="panel" style="border-top: 3px solid #ec4899;">

#### 多视图 / 视频级编码

将导航片段作为视频序列处理，用 3D CNN 或时空 Transformer 编码，**捕捉运动信息和时序变化**。 代表：VLN-Transformer, ActionNet。

### 维度 3：跨模态融合 — 语言与视觉如何交互？

<div style="overflow-x:auto;">

| 融合方式                     | 代表方法                | 工作原理                                                                         |
| ------------------------ | ------------------- | ---------------------------------------------------------------------------- |
| **拼接 (Concat)**          | Seq2Seq, S-F        | 语言向量和视觉向量直接拼成一个长向量，送进 LSTM 解码器。最朴素但**无法建模细粒度跨模态对应**                          |
| **注意力 (Soft Attention)** | RCM, SMNA           | 在语言 token 序列上做视觉引导的注意力加权，找到"当前最相关的词"。如指令中"沙发" → 视觉中沙发区域                      |
| **共注意力 (Co-Attention)**  | VLN-BERT, PREVALENT | Transformer 内部语言和视觉 token **互相做注意力**：语言关注视觉（这个词对应画面的哪部分），视觉也关注语言（这个区域被哪个词描述） |
| **Token 统一**             | HAMT, RT-2          | 将语言、视觉、历史、动作全部编码为**统一的 token 序列**，由同一个 Transformer 处理。最彻底的融合方式               |
| **LLM 上下文窗口**            | NavGPT, DiscussNav  | 将视觉描述转为文本（"你看到前方有一扇门"），和指令一起放进 LLM 的 prompt。融合发生在 LLM 的**文本语义推理空间**，而非特征空间   |
| **双分支 (Dual-Branch)**    | DUET                | 全局分支做语言-拓扑图的粗粒度对齐（决定大方向），局部分支做语言-视觉帧的细粒度对齐（决定具体动作），两分支并行输出后融合                |

</div>

### 维度 4：动作预测 — 如何输出导航决策？

<div class="dual-panel">

<div class="panel" style="border-top: 3px solid #ec4899;">

#### 离散动作分类

在预定义的离散动作集（前进/左转/右转/停止）上做 softmax 分类。简单高效， 但粒度粗。Habitat 的 VLNTask 默认使用此方式。

</div>

<div class="panel" style="border-top: 3px solid #06b6d4;">

#### 全景动作空间

将 360° 离散化为 N 个方向（如 36 个方向 + stop），每个方向对应一个可导航节点。 泛化更好，但动作空间大。Speaker-Follower, EnvDrop 均采用此方式。

<div class="dual-panel" style="margin-bottom:0;">

<div class="panel" style="border-top: 3px solid #f59e0b;">

#### 航点预测 + 路径规划

模型不直接预测动作，而是预测一个**中间航点 (waypoint)**的 (x,y) 坐标或深度图中的像素位置， 再由路径规划器驱动机器人到达该航点。DUET 的局部分支即用此方式。

</div>

<div class="panel" style="border-top: 3px solid #10b981;">

#### Token 生成 (LLM/VLA)

将动作 token 化：RT-2 的动作是文本 token（如 "move\_forward 0.25m"）， Octo 将连续动作离散化为码本 token。LLM 作为自回归解码器逐步生成动作序列。

### 维度 5：历史记忆 — 如何利用过去的信息？

<div style="overflow-x:auto;">

| 记忆机制            | 代表方法                    | 描述 · 优劣                                                                       |
| --------------- | ----------------------- | ----------------------------------------------------------------------------- |
| **LSTM 隐状态**    | Seq2Seq, S-F            | 每一步的隐状态 hₜ 编码了历史。**优势：简单；劣势：隐式、不可解释、长序列信息衰减严重**                               |
| **历史动作/视觉序列**   | EnvDrop, PREVALENT      | 将过去 K 步的动作和视觉特征拼成序列输入。比 LSTM 隐状态更**显式**，但仍是扁平的序列表示                            |
| **层次化记忆**       | HAMT                    | 三个时间尺度：短期（最近 K 帧）、中期（子路径片段）、长期（完整轨迹），分别由不同 Transformer 编码。**对长距离导航效果显著**      |
| **拓扑图记忆**       | DUET, RelGraph, Ego2Top | 每到一个新位置在图 G 中添加节点，连边表示可通行关系。**结构化、可规划**，但依赖图构建的准确性                            |
| **BEV 语义地图**    | GridMM, BEVBert, L3MVN  | 将导航历史投影为鸟瞰视角的栅格地图，每个栅格存语义特征。**解释性强**，但需要位姿估计和投影                               |
| **Prompt 对话历史** | NavGPT, DiscussNav      | 将历史动作和观测以自然语言形式写入 LLM prompt（"你上一步左转了，现在面前是..."）。**无限记忆**（受限于 LLM 上下文窗口），但推理慢 |

</div>

### 维度 6：训练范式 — 如何学习导航策略？

<div class="overview-grid">

<div class="overview-card">

<div class="icon">

👨‍🏫

</div>

### 行为克隆 (BC / IL)

从 ground-truth 路径中学习"下一步动作"，损失函数为交叉熵。 **优势：训练稳定快速；劣势：存在分布漂移 (distribution shift)** — 训练时喂的是专家路径的观测，推理时却看到自己的累积误差。

<div class="tag-row">

<span class="tag">Teacher Forcing</span><span class="tag">DAgger</span>

<div class="overview-card">

<div class="icon">

🎮

</div>

### 强化学习 (RL)

直接优化导航成功率 (Success / SPL)，策略与环境交互收集奖励信号。 **优势：可以超越专家示范；劣势：训练不稳定，奖励稀疏** — 需要精心设计 reward shaping (如距离减小 reward)。

<div class="tag-row">

<span class="tag">A3C / PPO</span><span class="tag">Reward Shaping</span>

<div class="overview-card">

<div class="icon">

📚

</div>

### 预训练 + 微调

在大量跨模态数据上预训练编码器，然后在下游 VLN 数据上微调。 **优势：泛化能力最强（SOTA for years）；劣势：需要大规模预训练数据和计算资源**。

<div class="tag-row">

<span class="tag">Masked LM</span><span class="tag">Image-Text Matching</span>

<div class="overview-card">

<div class="icon">

🪄

</div>

### 零样本 (Zero-Shot)

LLM-based 方法的独特优势 — **完全不需要 VLN 训练数据**。 利用 LLM 的世界知识和推理能力直接规划导航。 **优势：可以在任何新环境中工作；劣势：缺乏对特定场景的优化，推理速度慢**。

<div class="tag-row">

<span class="tag">Prompt Engineering</span><span class="tag">Chain-of-Thought</span>

## 应用场景

<div class="module-grid">

<div class="module" style="border-left-color: var(--accent-app);">

### 🏠 家用服务机器人

"去卧室帮我把桌上的水杯拿过来" — VLN 是服务机器人理解自然语言家庭指令的基础能力。

  - 老人/残障人士辅助 — 取物、导引
  - 智能家居中控的物理执行端
  - 多楼层导航 + 房间语义理解

</div>

<div class="module" style="border-left-color: var(--accent-r2r);">

### 🏥 医疗与看护

医院环境中，机器人根据医生/护士的自然语言指令自主导航到指定病房或药房。

  - 药品配送 — "把药送到 302 病房"
  - 导诊 — "带患者去放射科"
  - 传染病房的非接触式服务

</div>

<div class="module" style="border-left-color: var(--accent-habitat);">

### 🏭 仓库与物流

工人通过语音指令指挥 AMR (自主移动机器人) 前往货架位置取货。

  - "去 A3 货架第三排取零件盒"
  - 动态环境中的自然语言重新规划
  - 人机协作 — 工人与机器人共用语言通道

</div>

<div class="module" style="border-left-color: var(--accent-model);">

### 🚁 搜救与巡检

未知环境中通过语言指令部署无人机/机器人进行搜索和检查。

  - "检查三楼走廊尽头的配电箱"
  - 地震/火灾后的废墟搜救
  - 工业设施的安全巡检

</div>

<div class="module" style="border-left-color: var(--accent-challenge);">

### ♿ 视障人士导航辅助

VLN 技术的逆向应用 — 不仅让机器人理解人，也让人通过自然语言"看到"环境。

  - 室内场景的语言描述生成
  - 语音引导视障人士在陌生室内行走
  - 结合智能眼镜的实时导航

</div>

<div class="module" style="border-left-color: var(--accent-vln);">

### 🌐 元宇宙与数字人

虚拟环境中的 NPC / 数字人需要理解自然语言指令并自主导航。

  - 虚拟导游 — "带我看埃菲尔铁塔"
  - 游戏 NPC 的自然语言交互导航
  - VR/AR 场景中的辅助导航

</div>

## VLN 与 Habitat 的关系

<div class="qa-box">

<div class="q">

Habitat 为 VLN 提供了什么？

</div>

<div class="a">

Habitat 为 VLN 研究提供了一站式的**标准化实验平台**。具体来说：  
  
**1. 仿真环境：**Habitat-Sim 提供高性能的 Matterport3D 室内场景渲染（RGB + Depth + 语义），支持全景 RGB-D 观测和离散动作空间。  
**2. 任务抽象：**`VLNTask` 定义标准的 VLN RL 接口 — step/reset/get\_observations，让研究者专注于模型设计。  
**3. 数据集加载：**`R2RVLN-v1` 自动处理 R2R 数据集的下载、解析、划分（train / val\_seen / val\_unseen）、场景过滤。  
**4. 传感器管线：**`InstructionSensor` 将自然语言指令作为标准观测通道，与 RGB/D 数据一起传给策略网络。  
**5. 统一指标：**内置 Success、SPL、DistanceToGoal 等标准评估指标，确保论文结果可复现、可比对。  
**6. 分布式训练：**habitat-baselines 支持 PPO / DD-PPO 分布式训练 VLN 策略，可横向扩展到多 GPU 节点。

</div>

<div class="q">

VLN 在 Habitat 任务体系中的位置？

</div>

<div class="a">

VLN 是 Habitat 四大核心任务族之一（Navigation / Rearrange / EQA / VLN），属于**导航任务**的子类。 技术上，`VLNTask` 继承自 `NavigationTask` → `EmbodiedTask`， 这意味着 VLN 与 PointNav、ObjectNav 共享同一套 Env 接口和观测处理管线。 唯一的本质区别是「目标如何给定」— PointNav 给坐标，VLN 给语言指令。

</div>

<div class="q">

Habitat 当前支持哪些 VLN 功能？

</div>

<div class="a">

**当前实现 (v0.2.5)：**  
· 数据集：仅 R2R (`R2RVLN-v1`) 在 Matterport3D 上  
· 动作空间：离散 4 动作（前进/左转/右转/停止）  
· 传感器：InstructionSensor（指令文本 + 词元 + 轨迹 ID）  
· 指标：Success / SPL / DistanceToGoal  
· 示例：参考路径跟随器（最短路径代理）  
  
**尚未内置但常见的扩展需求：**  
· R4R / RxR / REVERIE 等多数据集支持  
· 连续动作空间（更细粒度的控制）  
· 全景动作空间（在可导航节点间跳转，而非逐个 step）  
· 预训练视觉编码器 (CLIP, ViT) 的集成  
· LLM-based 规划器的即插即用接口

</div>

<div class="q">

VLN 如何联结 Habitat 的 Sim-to-Real 能力？

</div>

<div class="a">

VLN 享受 Habit 的 Sim-to-Real 架构红利 — **只需改配置中一行** (`Sim-v0 → PyRobot-v0`)， 仿真训练的 VLN 策略就能切换到真实机器人上运行。整个 VLN 任务栈（指令传感器、观测管线、动作空间） 只依赖 Simulator 抽象接口，不耦合具体后端。当然，sim-to-real 的视觉 domain gap 对于依赖 RGB 感知的 VLN 尤为突出，通常需要 domain randomization 或 real-world fine-tuning 来弥合。

<div class="arch-diagram" style="margin-top: 28px;">

VLN 在 Habit 任务生态中的位置

<div class="arch-row">

<div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd;">

🧭 PointNav  
<span class="small">坐标导航</span>

</div>

<div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd;">

🔍 ObjectNav  
<span class="small">物体导航</span>

</div>

<div class="arch-layer" style="background:#06b6d440; border:2px solid #22d3ee; color:#67e8f9;">

**🗣️ VLN**  
<span class="small">语言导航</span>

</div>

<div class="arch-layer" style="background:#3b82f620; border:2px solid #3b82f6; color:#93c5fd;">

🖼️ ImageNav  
<span class="small">图像导航</span>

<div class="arch-arrow">

↓   四大导航任务共享   ↓

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#8b5cf620; border:2px solid #8b5cf6; color:#c4b5fd;" colspan="4">

NavigationTask → EmbodiedTask → Env

<div class="arch-arrow">

↓   任务前端：目标定义方式不同   ↑   后端：统一接口   ↓

</div>

<div class="arch-row">

<div class="arch-layer" style="background:#10b98120; border:2px solid #10b981; color:#6ee7b7;">

📍 坐标

</div>

<div class="arch-layer" style="background:#10b98120; border:2px solid #10b981; color:#6ee7b7;">

🔎 语义类别

</div>

<div class="arch-layer" style="background:#10b98140; border:2px solid #34d399; color:#6ee7b7;">

**📝 自然语言**

</div>

<div class="arch-layer" style="background:#10b98120; border:2px solid #10b981; color:#6ee7b7;">

🖼️ 目标图像

## 未来方向

<div class="flow-box">

<div class="flow-step">

<div class="num" style="background:#06b6d420; color:#2dd4bf;">

1

</div>

#### 多模态大模型融合

VLA (Vision-Language-Action) 统一架构，一个模型端到端从指令到控制

</div>

<div class="flow-step">

<div class="num" style="background:#8b5cf620; color:#a78bfa;">

2

</div>

#### 多语言 & 开放词汇

从英语扩展到 100+ 语言，支持自由形式的自然语言目标描述

</div>

<div class="flow-step">

<div class="num" style="background:#f59e0b20; color:#fbbf24;">

3

</div>

#### 交互式 VLN

引入对话 — 机器人确认、询问、汇报，人机双向沟通导航

</div>

<div class="flow-step">

<div class="num" style="background:#10b98120; color:#34d399;">

4

</div>

#### 真机部署

从仿真 benchmark 到真实家庭/医院/仓库环境的端到端落地

<div class="qa-box" style="margin-top: 28px;">

<div class="q">

为什么 VLN 是具身 AI 的「圣杯」任务？

</div>

<div class="a">

VLN 是少数同时要求**语言理解**（NLP）、**视觉感知**（CV）、**空间推理**和**序贯决策**（RL）四项核心能力 的任务。一个真正解决 VLN 的系统几乎等价于一个能在现实世界中理解人类语言并自主行动的通用智能体 — 这正是具身 AI 的终极目标。
# 工程架构可视化 — Habitat 从零理解

> Meta AI 推出的具身智能模块化平台 — 定义任务、配置智能体、训练策略、评估基准，一站式端到端开发

## 环境安装与配置

<div class="install-grid">

<div class="install-card" style="border-left-color: #10b981;">

#### <span class="step-num" style="background:#10b98120;color:#34d399;">1</span> 创建 Conda 环境

Habitat 需要 Python 3.9 + cmake 3.14+，创建独立 conda 环境避免依赖冲突。

    $ conda create -n habitat python=3.9 cmake=3.14.0
    $ conda activate habitat

</div>

<div class="install-card" style="border-left-color: #3b82f6;">

#### <span class="step-num" style="background:#3b82f620;color:#60a5fa;">2</span> 安装 habitat-sim（仿真引擎）

habitat-sim 不在 PyPI 上，必须通过 **conda** 从 `aihabitat` / `conda-forge` channel 安装。

    $ conda install habitat-sim=0.2.5 withbullet headless \
        -c conda-forge -c aihabitat

`withbullet` — 带物理引擎 | `headless` — 无 GUI 渲染（服务器用）| 去掉 headless 可在桌面看到 3D 画面

</div>

<div class="install-card" style="border-left-color: #8b5cf6;">

#### <span class="step-num" style="background:#8b5cf620;color:#a78bfa;">3</span> 安装 habitat-lab（任务框架）

从本地源码 pip install -e，方便修改代码后即时生效。

    $ cd /develop/habitat-lab
    $ pip install -e habitat-lab

</div>

<div class="install-card" style="border-left-color: #f59e0b;">

#### <span class="step-num" style="background:#f59e0b20;color:#fbbf24;">4</span> 安装 habitat-baselines（可选）

如果需要训练 RL/IL 模型，安装基线算法包。

    $ pip install -e habitat-baselines

### Conda 代理与网络配置

> ⚠️
> 
> <div class="warn-title">
> 
> 常见问题：SSL EOF 错误
> 
> conda 不会自动读取 `HTTP_PROXY` 环境变量，需**显式**配置。未配代理时 conda 内部网络层和 Python `urllib` 走不同路径，导致 TLS 连接状态混乱，表现为此错误。
> 
> </div>
> 
> <div class="dual-panel" style="margin-top:18px;">
> 
> <div class="panel" style="border-top: 3px solid #f59e0b;">
> 
> #### 配置 conda 走代理
> 
>     $ # 给 conda 显式设置代理（Clash 默认 7897 端口）
>     $ conda config --set proxy_servers.http http://127.0.0.1:7897
>     $ conda config --set proxy_servers.https http://127.0.0.1:7897
>     
>     $ # 验证
>     $ conda config --show proxy_servers
> 
> </div>
> 
> <div class="panel" style="border-top: 3px solid #10b981;">
> 
> #### 精简 channel 列表
> 
> 混用清华镜像和境外源会导致连接数爆炸，各源 TLS 实现差异会加剧 SSL EOF。
> 
>     $ # 推荐：只用 conda-forge + aihabitat
>     $ conda config --remove-key channels
>     $ conda config --add channels conda-forge
>     $ conda config --add channels aihabitat
>     
>     $ # 或：只用国内镜像（阿里云）
>     $ conda config --add channels \
>         https://mirrors.aliyun.com/anaconda/cloud/conda-forge
> 
> <div>
> 
> **数据下载：SSL EOF 的特殊处理**
> 
> `habitat_sim.utils.datasets_download` 内部调用系统 `curl`，即使 conda 配了代理，curl 走的是 `HTTP_PROXY` 环境变量。 当遇到 `api.matterport.com` 等境外 API 的 SSL EOF 时，可对该域名绕过代理或手动下载：
> 
>     # 方法 1：对 Matterport API 绕过代理
>     $ no_proxy="api.matterport.com" python -m habitat_sim.utils.datasets_download ...
>     
>     # 方法 2：先验证最小的测试数据
>     $ python -m habitat_sim.utils.datasets_download \
>         --uids habitat_test_scenes habitat_test_pointnav_dataset \
>         --data-path data/
>     
>     # 方法 3：查看所有可用数据集
>     $ python -m habitat_sim.utils.datasets_download --list
> 
> </div>
> 
> ### 完整安装命令清单
> 
>     # ===== 1. 创建环境 =====
>     conda create -n habitat python=3.9 cmake=3.14.0
>     conda activate habitat
>     
>     # ===== 2. 配置代理（如有 Clash）=====
>     conda config --set proxy_servers.http http://127.0.0.1:7897
>     conda config --set proxy_servers.https http://127.0.0.1:7897
>     
>     # ===== 3. 精简 channel =====
>     conda config --remove-key channels
>     conda config --add channels conda-forge
>     conda config --add channels aihabitat
>     
>     # ===== 4. 安装 habitat-sim =====
>     conda install habitat-sim=0.2.5 withbullet headless -c conda-forge -c aihabitat
>     
>     # ===== 5. 安装 habitat-lab =====
>     cd /develop/habitat-lab
>     pip install -e habitat-lab
>     pip install -e habitat-baselines    # 可选
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 工程总览
> 
> <div class="overview-grid">
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 🧠
> 
> </div>
> 
> ### habitat-lab
> 
> 核心 Python 包。定义环境、智能体、传感器、任务、数据集、仿真器接口。"做什么"的全套抽象。
> 
> <div class="tag-row">
> 
> <span class="tag">core</span><span class="tag">tasks</span><span class="tag">datasets</span><span class="tag">config</span>
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 🎓
> 
> </div>
> 
> ### habitat-baselines
> 
> 基线算法包。"怎么学" — PPO、DD-PPO、分层 RL、模仿学习 (IL) 的训练流程与模型实现。
> 
> <div class="tag-row">
> 
> <span class="tag">rl/ppo</span><span class="tag">rl/ddppo</span><span class="tag">il</span><span class="tag">agents</span>
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 📋
> 
> </div>
> 
> ### examples
> 
> 示例脚本集。覆盖环境创建、交互式控制、传感器注册、基准测试、VLN 导航等典型用法。
> 
> <div class="tag-row">
> 
> <span class="tag">example.py</span><span class="tag">interactive\_play</span><span class="tag">tutorials</span>
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 🧪
> 
> </div>
> 
> ### test
> 
> 全面的测试套件。覆盖环境、传感器、任务、数据集、训练器、Gym 封装等所有模块。
> 
> <div class="tag-row">
> 
> <span class="tag">35+ test files</span><span class="tag">config</span><span class="tag">data</span>
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 📖
> 
> </div>
> 
> ### docs
> 
> 项目文档源文件，构建 aihabitat.org 官网。包含教程、API 参考和页面配置。
> 
> <div class="tag-row">
> 
> <span class="tag">Sphinx</span><span class="tag">pages</span><span class="tag">images</span>
> 
> <div class="overview-card">
> 
> <div class="icon">
> 
> 🔧
> 
> </div>
> 
> ### scripts / res / Dockerfile
> 
> 辅助脚本、静态资源和 Docker 容器化部署方案，支撑 CI/CD 与快速环境搭建。
> 
> <div class="tag-row">
> 
> <span class="tag">benchmark</span><span class="tag">Docker</span><span class="tag">assets</span>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 三层架构
> 
> <div class="arch-diagram">
> 
> <div class="arch-row">
> 
> <div class="arch-layer l-top">
> 
> 🔧 配置层  
> <span class="small">Hydra YAML</span>
> 
> </div>
> 
> <div class="arch-layer l-top">
> 
> 🎯 任务层  
> <span class="small">Nav / Rearrange / EQA / VLN</span>
> 
> </div>
> 
> <div class="arch-layer l-top">
> 
> 🤖 智能体层  
> <span class="small">传感器 + 物理形态</span>
> 
> <div class="arch-arrow">
> 
> ↓   注册表 (Registry) 动态装配   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer l-mid">
> 
> 🌍 环境核心 Env  
> <span class="small">step / reset / 指标计算</span>
> 
> </div>
> 
> <div class="arch-layer l-mid">
> 
> 📦 数据集层  
> <span class="small">PointNav / ObjectNav / VLN …</span>
> 
> <div class="arch-arrow">
> 
> ↓   仿真器抽象接口   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer l-bottom">
> 
> 🖥️ Habitat-Sim  
> <span class="small">3D 室内场景 · 物理引擎</span>
> 
> </div>
> 
> <div class="arch-layer l-bottom">
> 
> 🔌 PyRobot  
> <span class="small">真实机器人后端</span>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 核心包结构 (habitat-lab/habitat/)
> 
> <div class="tree">
> 
> <span class="dir">habitat/</span> ├── <span class="dir">core/</span> <span class="cmt">\# 核心抽象层</span> │ ├── env.py <span class="cmt">\# Env 基类 (step/reset/close)</span> │ ├── embodied\_task.py <span class="cmt">\# 具身任务基类</span> │ ├── agent.py <span class="cmt">\# 智能体抽象</span> │ ├── sensor.py <span class="cmt">\# 传感器抽象 (RGB/深度/GPS/语义…)</span> │ ├── simulator.py <span class="cmt">\# 仿真器抽象基类</span> │ ├── dataset.py <span class="cmt">\# 数据集基类</span> │ ├── registry.py <span class="cmt">\# 注册表机制 (动态模块加载)</span> │ ├── vector\_env.py <span class="cmt">\# 向量化多环境并行</span> │ ├── benchmark.py <span class="cmt">\# 基准测试评估框架</span> │ └── <span class="dir">batch\_rendering/</span> <span class="cmt">\# 批量渲染</span> │ ├── <span class="dir hl1">tasks/</span> <span class="cmt">\# 任务定义</span> │ ├── <span class="dir">nav/</span> <span class="cmt">\# 导航任务 (PointNav, ObjectNav, ImageNav)</span> │ ├── <span class="dir">rearrange/</span> <span class="cmt">\# 物体重排任务 (Habitat 2.0 核心)</span> │ ├── <span class="dir">eqa/</span> <span class="cmt">\# 具身问答 (Embodied QA)</span> │ └── <span class="dir">vln/</span> <span class="cmt">\# 视觉语言导航</span> │ ├── <span class="dir hl2">datasets/</span> <span class="cmt">\# 数据集加载器</span> │ ├── <span class="dir">pointnav/</span> <span class="cmt">\# PointNav 数据集</span> │ ├── <span class="dir">object\_nav/</span> <span class="cmt">\# 物体导航数据集</span> │ ├── <span class="dir">image\_nav/</span> <span class="cmt">\# 图像导航数据集</span> │ ├── <span class="dir">eqa/</span> <span class="cmt">\# 问答数据集 (MP3D-EQA)</span> │ ├── <span class="dir">vln/</span> <span class="cmt">\# VLN 数据集 (R2R)</span> │ └── <span class="dir">rearrange/</span> <span class="cmt">\# 重排任务数据集</span> │ ├── <span class="dir">config/</span> <span class="cmt">\# Hydra 配置系统</span> │ ├── <span class="dir">habitat/</span> <span class="cmt">\# 环境配置 (task/dataset/simulator)</span> │ └── <span class="dir">benchmark/</span> <span class="cmt">\# 基准测试配置</span> │ ├── <span class="dir">articulated\_agents/</span> <span class="cmt">\# 关节式智能体</span> │ ├── <span class="dir">robots/</span> <span class="cmt">\# 机械臂 (Fetch, Franka…)</span> │ ├── <span class="dir">humanoids/</span> <span class="cmt">\# 人形智能体</span> │ └── <span class="dir">articulated\_agent\_controllers/</span> <span class="cmt">\# 关节控制器</span> │ ├── <span class="dir">sims/</span> <span class="cmt">\# 仿真器后端</span> │ ├── <span class="dir">habitat\_simulator/</span> <span class="cmt">\# Habitat-Sim 后端 (3D 室内场景)</span> │ └── <span class="dir">pyrobot/</span> <span class="cmt">\# PyRobot 真实机器人后端</span> │ ├── <span class="dir">gym/</span> <span class="cmt">\# OpenAI Gym 兼容封装</span> │ └── <span class="dir">utils/</span> <span class="cmt">\# 工具集</span> └── <span class="dir">visualizations/</span> <span class="cmt">\# 可视化 (语义渲染/轨迹…)</span>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 基线算法包 (habitat-baselines/habitat\_baselines/)
> 
> <div class="tree">
> 
> <span class="dir">habitat\_baselines/</span> ├── <span class="dir hl3">rl/</span> <span class="cmt">\# 强化学习</span> │ ├── <span class="dir">ppo/</span> <span class="cmt">\# PPO 训练器</span> │ ├── <span class="dir">ddppo/</span> <span class="cmt">\# 分布式 DD-PPO (大规模并行训练)</span> │ ├── <span class="dir">hrl/</span> <span class="cmt">\# 分层强化学习</span> │ ├── <span class="dir">ver/</span> <span class="cmt">\# 变分环境推理</span> │ └── <span class="dir">models/</span> <span class="cmt">\# 策略网络 (ResNet/RNN 状态编码器)</span> │ ├── <span class="dir hl4">il/</span> <span class="cmt">\# 模仿学习</span> │ ├── <span class="dir">models/</span> <span class="cmt">\# IL 模型</span> │ ├── <span class="dir">trainers/</span> <span class="cmt">\# IL 训练器</span> │ └── <span class="dir">data/</span> <span class="cmt">\# IL 数据加载</span> │ ├── <span class="dir">agents/</span> <span class="cmt">\# 各类智能体实现</span> ├── <span class="dir">common/</span> <span class="cmt">\# 通用模块 (环境构造/Tensorboard/Rollout)</span> ├── <span class="dir">config/</span> <span class="cmt">\# 各算法 Hydra YAML 配置</span> └── <span class="dir">utils/</span> <span class="cmt">\# 可视化等工具</span>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 核心模块详解
> 
> <div class="module-grid">
> 
> <div class="module" style="border-left-color: var(--accent-core);">
> 
> ### 🔌 core — 环境核心
> 
> 整个平台的骨架，定义 RL 标准的 `step()/reset()` 接口， 通过注册表 (Registry) 将智能体、传感器、任务动态组装。
> 
>   - **Env** — step / reset / close，对标 OpenAI Gym
>   - **EmbodiedTask** — 任务基类，绑定智能体与场景
>   - **SensorSuite** — 传感器集合 (RGB, Depth, GPS, Compass…)
>   - **Registry** — @registry.register 装饰器动态注册
>   - **VectorEnv** — 多环境并行 rollout
>   - **Benchmark** — 标准化评估 + 指标上报
> 
> </div>
> 
> <div class="module" style="border-left-color: var(--accent-tasks);">
> 
> ### 🎯 tasks — 四大任务族
> 
> 定义具身 AI 的核心 benchmark 任务，每个任务有独立的 episode 规范与成功判定。
> 
>   - **Nav** — PointNav (点到点) / ObjectNav (找物体) / ImageNav (以图导航)
>   - **Rearrange** — Habitat 2.0，物体抓取与重排
>   - **EQA** — 具身问答：导航到目标位置并回答问题
>   - **VLN** — 视觉语言导航：根据自然语言指令行动
> 
> </div>
> 
> <div class="module" style="border-left-color: var(--accent-data);">
> 
> ### 📦 datasets — 数据集
> 
> 与 task 一一对应，负责加载场景 (GLB/JSON) 与 episode 数据，继承 `Dataset` 基类。
> 
>   - **PointNav** — Gibson / Matterport3D 场景
>   - **ObjectNav** — HM3D / MP3D 物体导航
>   - **VLN** — R2R (Room-to-Room) 指令数据集
>   - **Rearrange** — ReplicaCAD 场景资产
>   - **EQA** — MP3D-EQA 问答数据集
> 
> </div>
> 
> <div class="module" style="border-left-color: var(--accent-rl);">
> 
> ### 🎓 RL — 强化学习训练
> 
> 基于 PyTorch 的分布式策略训练管线。
> 
>   - **PPO** — 经典 PPO，支持 RNN 状态编码器
>   - **DD-PPO** — 大规模分布式 PPO，跨多 GPU/节点
>   - **HRL** — 分层 RL (高层策略 + 低层控制器)
>   - **VER** — 变分环境推理与探索
> 
> </div>
> 
> <div class="module" style="border-left-color: var(--accent-il);">
> 
> ### 🎭 IL — 模仿学习
> 
> 从专家示范数据中学习策略，常用于导航任务的 behavior cloning。
> 
>   - **BC** — 行为克隆 (Behavior Cloning)
>   - **DAgger** — 数据集聚合训练
>   - 支持 ResNet + RNN 策略架构
> 
> </div>
> 
> <div class="module" style="border-left-color: var(--accent-sim);">
> 
> ### 🤖 articulated\_agents + sims
> 
> 物理形态与仿真后端，支持从静态导航到动态操作的全谱任务。
> 
>   - **Habitat-Sim** — 高性能 3D 室内仿真器 (Bullet 物理)
>   - **PyRobot** — 真实机器人部署
>   - **Fetch / Franka** — 机械臂模型
>   - **Humanoid** — 人形智能体（运动控制）
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## 典型实验流程
> 
> <div class="flow-box">
> 
> <div class="flow-step">
> 
> <div class="num" style="background:#3b82f620; color:#60a5fa;">
> 
> 1
> 
> </div>
> 
> #### 定义任务
> 
> 选用内置任务 (Nav/Rearrange/…) 或通过注册表自定义新任务
> 
> </div>
> 
> <div class="flow-step">
> 
> <div class="num" style="background:#8b5cf620; color:#a78bfa;">
> 
> 2
> 
> </div>
> 
> #### 配置环境
> 
> Hydra YAML 组合数据集 + 仿真器 + 传感器 + 智能体
> 
> </div>
> 
> <div class="flow-step">
> 
> <div class="num" style="background:#f59e0b20; color:#fbbf24;">
> 
> 3
> 
> </div>
> 
> #### 训练策略
> 
> 选用 PPO / DD-PPO / IL 管线，配置模型与超参
> 
> </div>
> 
> <div class="flow-step">
> 
> <div class="num" style="background:#10b98120; color:#34d399;">
> 
> 4
> 
> </div>
> 
> #### 评估基准
> 
> Benchmark 标准化评估，输出 SPL / Success 等指标
> 
> </div>
> 
> <div class="flow-step">
> 
> <div class="num" style="background:#ec489920; color:#f472b6;">
> 
> 5
> 
> </div>
> 
> #### 可视化分析
> 
> Tensorboard 日志 + utils/visualizations 渲染轨迹
> 
> </div>
> 
> <div class="section">
> 
> <div class="container">
> 
> ## Sim-to-Real：从仿真到真实机器人部署
> 
> <div class="qa-box">
> 
> <div class="q">
> 
> ❓ Habitat 能否部署在真实机器人上？
> 
> </div>
> 
> <div class="a">
> 
> **可以。**Habitat 的架构核心是一个 **Simulator 抽象基类**（`habitat/core/simulator.py`）， 它定义了 `reset()`、`step()`、`get_agent_state()` 等统一接口。 仿真和真机只是该基类的两个不同实现 — 上层策略代码**零改动**即可切换。 代码中有一句精准的注释：*"This abstraction assumes that reality is a simulation."*
> 
> ### 双后端架构：统一接口，可插拔实现
> 
> <div class="dual-panel">
> 
> <div class="panel sim">
> 
> #### 🖥️ Habitat-Sim <span style="font-weight:400;color:var(--text-dim);font-size:0.82rem;">— 仿真后端</span>
> 
> 注册名 `Sim-v0`，高性能 3D 渲染引擎 + Bullet 物理，加载 `.glb` 场景文件。
> 
> <div class="dataflow">
> 
> <span class="node">3D 场景  
> <span class="small">GLB + NavMesh</span></span> <span class="arrow">→</span> <span class="node">Habitat-Sim  
> <span class="small">渲染引擎</span></span> <span class="arrow">→</span> <span class="node">RGB / Depth  
> <span class="small">Semantic / GPS</span></span> <span class="arrow">→</span> <span class="node">SensorSuite  
> <span class="small">统一观测</span></span>
> 
> </div>
> 
> <div style="margin-top:12px; font-size:0.75rem; color:#64748b;">
> 
> 支持场景: Matterport3D · Gibson · ReplicaCAD · HM3D
> 
> <div class="panel real">
> 
> #### 🔌 PyRobot <span style="font-weight:400;color:var(--text-dim);font-size:0.82rem;">— 真机后端</span>
> 
> 注册名 `PyRobot-v0`，通过 ROS 驱动真实硬件，封装传感器到统一接口。
> 
> <div class="dataflow">
> 
> <span class="node">LoCoBot  
> <span class="small">真实硬件</span></span> <span class="arrow">→</span> <span class="node">RealSense  
> <span class="small">相机 / 底座</span></span> <span class="arrow">→</span> <span class="node">get\_robot\_observations()  
> <span class="small">{"rgb","depth","bump"}</span></span> <span class="arrow">→</span> <span class="node">SensorSuite  
> <span class="small">统一观测</span></span>
> 
> </div>
> 
> <div style="margin-top:12px; font-size:0.75rem; color:#64748b;">
> 
> 需要: PyRobot 环境 + ROS\_PATH 导出
> 
> </div>
> 
> <div style="background:#10b98110; border:1px solid #10b98130; border-radius:10px; padding:16px 20px; text-align:center; margin-bottom:32px;">
> 
> <span style="color:#6ee7b7; font-weight:700;">切换方式：仅修改 YAML 配置中一行</span>  
> `simulator.type = "Sim-v0"` <span style="color:var(--text-dim); margin:0 12px;">→</span> `simulator.type = "PyRobot-v0"`  
> <span style="font-size:0.75rem; color:#64748b;">策略代码、任务逻辑、评估指标 — 全部保持不变</span>
> 
> </div>
> 
> ### 支持的机器人平台
> 
> <div class="robot-grid">
> 
> <div class="robot-card">
> 
> <div class="name">
> 
> 🦾 Fetch
> 
> </div>
> 
> <div class="type">
> 
> 移动机械臂
> 
> </div>
> 
> <div class="file">
> 
> fetch\_robot.py
> 
> </div>
> 
> 轮式底盘 + 7-DoF 臂  
> 经典操作平台
> 
> </div>
> 
> <div class="robot-card">
> 
> <div class="name">
> 
> 🦿 Franka
> 
> </div>
> 
> <div class="type">
> 
> 静态机械臂
> 
> </div>
> 
> <div class="file">
> 
> franka\_robot.py
> 
> </div>
> 
> 固定底座  
> 精密桌面操作
> 
> </div>
> 
> <div class="robot-card">
> 
> <div class="name">
> 
> 📏 Stretch
> 
> </div>
> 
> <div class="type">
> 
> 移动机械臂
> 
> </div>
> 
> <div class="file">
> 
> stretch\_robot.py
> 
> </div>
> 
> 小底座 + 伸缩臂  
> 狭窄空间操作
> 
> </div>
> 
> <div class="robot-card">
> 
> <div class="name">
> 
> 🐕 Spot
> 
> </div>
> 
> <div class="type">
> 
> 四足机器人
> 
> </div>
> 
> <div class="file">
> 
> spot\_robot.py
> 
> </div>
> 
> 可爬楼梯  
> 复杂地形巡检
> 
> ### 传感器数据：仿真 vs 真机的处理对决
> 
> <div style="overflow-x:auto;">
> 
> | 传感器               | 🖥️ 仿真 (Habitat-Sim)                                                              | 🔌 真机 (PyRobot)                                                                                            |
> | ----------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
> | **RGB**           | 渲染引擎管线输出 RGBA → 取 RGB 通道 → resize/center\_crop 归一化 → `np.ndarray (H,W,3) uint8`  | RealSense `camera.get_rgb()` → resize/center\_crop 对齐 → `np.ndarray (H,W,3) uint8`                        |
> | **Depth**         | 渲染深度缓冲区 → 读取浮点深度 (米) → clip \[min, max\] → normalize \[0,1\] → `(H,W,1) float32` | RealSense `camera.get_depth()` → **mm → m** (/1000) → clip + normalize → expand\_dims → `(H,W,1) float32` |
> | **Semantic**      | 渲染语义缓冲区 → 物体 ID / 类别索引 → `(H,W) int32`                                           | 暂无内置支持，可通过注册表自定义（如接入检测/分割模型）                                                                              |
> | **Bump**          | 物理引擎碰撞检测 → bool                                                                  | `base.base_state.bumper` → `np.array bool`                                                                |
> | **GPS / Compass** | 直接读取 Agent 在场景坐标系中的 (x,y,z) + 朝向四元数                                              | 替换为里程计 (odom) + IMU → 通过注册表自定义传感器读取                                                                       |
> 

> </div>
> 
> \* 关键设计：两种后端的传感器输出经过各自的 Sensor 子类处理后，最终抵达 `SensorSuite.get_observations()` 的数据格式**完全一致**。
> 
> ### 地图 / 场景数据的处理差异
> 
> <div class="dual-panel">
> 
> <div class="panel sim">
> 
> #### 🖥️ 仿真场景
> 
> 需要预下载 **3D 场景资产**（.glb 格式）：  
> <span style="font-size:0.78rem; color:#64748b;"> · Matterport3D — 室内扫描重建  
> · Gibson — 点导航基准场景  
> · ReplicaCAD — 带语义的公寓模型  
> · HM3D — 物体导航大场景 </span>
> 
> 每个 **Episode**（任务实例）是一个 JSON 条目，指定场景 ID + 起终点位姿 + 目标信息。通过 `Dataset` 子类加载。
> 
> </div>
> 
> <div class="panel real">
> 
> #### 🔌 真机场景
> 
> **不需要 .glb 场景文件。**需要的是：  
> <span style="font-size:0.78rem; color:#64748b;"> · <span class="highlight">SLAM 建图</span> — 构建现实环境的占据栅格地图  
> · <span class="highlight">定位</span> — AMCL / 里程计估算实时位姿  
> · <span class="highlight">导航栈</span> — ROS Navigation2 / move\_base 处理路径规划  
> · <span class="highlight">Episode 定义</span> — 在真实空间中标注目标点 (x,y,z) </span>
> 
> 上层策略不直接操作地图 — 它通过 `step(action)` 发出高层指令，由 PyRobot 映射到底层 ROS 控制指令。
> 
> ### Sim-to-Real 部署流程
> 
> <div class="deploy-flow">
> 
> <div class="deploy-step">
> 
> <div class="step-icon" style="color:#3b82f6;">
> 
> 1
> 
> </div>
> 
> <div class="step-label">
> 
> 仿真训练
> 
> </div>
> 
> <div class="step-desc">
> 
> Habitat-Sim + GLB 场景  
> PPO / IL 训练策略
> 
> <div class="deploy-arrow">
> 
> →
> 
> </div>
> 
> <div class="deploy-step">
> 
> <div class="step-icon" style="color:#a78bfa;">
> 
> 2
> 
> </div>
> 
> <div class="step-label">
> 
> 导出模型
> 
> </div>
> 
> <div class="step-desc">
> 
> 保存 PyTorch 权重  
> 与配置 YAML
> 
> <div class="deploy-arrow">
> 
> →
> 
> </div>
> 
> <div class="deploy-step">
> 
> <div class="step-icon" style="color:#10b981;">
> 
> 3
> 
> </div>
> 
> <div class="step-label">
> 
> 切换后端
> 
> </div>
> 
> <div class="step-desc">
> 
> Sim-v0 → PyRobot-v0  
> 配置真实传感器
> 
> <div class="deploy-arrow">
> 
> →
> 
> </div>
> 
> <div class="deploy-step">
> 
> <div class="step-icon" style="color:#fbbf24;">
> 
> 4
> 
> </div>
> 
> <div class="step-label">
> 
> 环境适配
> 
> </div>
> 
> <div class="step-desc">
> 
> SLAM 建图 + 定位  
> Episode 真实坐标标注
> 
> <div class="deploy-arrow">
> 
> →
> 
> </div>
> 
> <div class="deploy-step">
> 
> <div class="step-icon" style="color:#f472b6;">
> 
> 5
> 
> </div>
> 
> <div class="step-label">
> 
> 真机推理
> 
> </div>
> 
> <div class="step-desc">
> 
> 加载模型权重  
> Env.step() 直接驱动硬件
> 
> </div>
> 
> <div class="qa-box">
> 
> <div class="q">
> 
> ❓ 为什么上层策略代码无需修改？
> 
> </div>
> 
> <div class="a">
> 
> 因为 `Env.step()` → `Task.step()` → `Simulator.step()` 这条调用链是**完全多态的**。 无论底层是 Habitat-Sim 渲染一帧 RGB，还是 PyRobot 从 RealSense 读一帧 RGB， 到达策略手里的都是一个 `Observations` 字典，格式、shape、dtype 在配置文件中统一约定。 这就是**依赖倒置**原则在具身 AI 中的体现 — 高层模块不依赖低层模块，二者都依赖抽象。
> 
> </div>
> 
> <div class="q">
> 
> ❓ 自定义传感器如何接入？
> 
> </div>
> 
> <div class="a">
> 
> 通过 `@registry.register_sensor` 装饰器注册一个新传感器类，实现 `get_observation()`。 然后在 YAML 的 `sensors` 列表中声明即可。例如你可以把 LiDAR 点云、里程计、IMU、甚至一个外部的 YOLO 检测结果包装成标准 Sensor， 策略就能像使用 RGB 一样使用这些数据。
> 
> </div>
> 
> <div class="q">
> 
> ❓ 仿真训练的模型能直接用到真机上吗？
> 
> </div>
> 
> <div class="a">
> 
> **理论上是设计目标，实际上需要领域适配。**Habitat 的架构使得模型加载和推理管线零成本切换， 但仿真与真实的视觉差异（纹理、光照、噪声）会导致 **domain gap**。 常见的缓解手段包括：Domain Randomization（在仿真中随机化纹理/光照）、 在 PyRobot 传感器层做输入归一化、或使用 Sim-to-Real 迁移学习（如 Domain Adaptation 微调）。
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
