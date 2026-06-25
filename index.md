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
