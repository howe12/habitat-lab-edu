# Habitat 学习资源中心 — 从零理解具身智能

> 从零理解具身智能 — 基于 Meta AI Habitat-Lab 的工程化教学体系。
    主线教程、专题深度、架构可视化，三条路径助你建立完整的知识体系。

📗 主线教程：Habitat 从零理解

11 章教科书。从概念到运行到源码，按 **工程依赖顺序** 编排。

📗

Habitat 教科书（11 章全覆盖）

模块化设计，从「它是什么」到「我该怎么学」。涵盖：架构总览 → 传感器与观测 → 任务体系 → 模拟器 → 数据管道 → RL 训练 → 评估基准 → 学习路线。

[打开教科书 →](habitat-textbook.html)

🔧

第1章：安装环境
Conda 环境 → 代理配置 → habitat-sim → habitat-lab → 数据下载验证。交互式检查清单。

[📖 开始安装](habitat-textbook-step1.html)
[→](habitat-textbook-step1.html)

📦

第1B章：完整数据集下载
**7 种场景 + 6 种任务数据集**：Gibson/MP3D/HM3D 获取流程、目录结构规范、授权申请指南。

[📖 下载数据](habitat-textbook-step1b.html)
[→](habitat-textbook-step1b.html)

▶️

第2章：跑通示例
5 个渐进式示例 + **4 组真实运行结果**（含终端输出、RGB 图像、GPS 轨迹、Top-down 地图）。

[📖 查看示例](habitat-textbook-step2.html)
[→](habitat-textbook-step2.html)

💻

第3章：读核心代码
**交互式调用链追踪器** + 参数调控台 + 6 模块可折叠源码分析。从注册中心到 C++ 引擎。

[📖 阅读源码](habitat-textbook-step3.html)
[→](habitat-textbook-step3.html)

⚙️

第4章：改配置实验
**5 组配置实验**：RGB 分辨率、RGB vs RGBD、自定义 LiDAR 传感器、YAML 配置继承、success_distance 参数。

[📖 动手实验](habitat-textbook-step4.html)
[→](habitat-textbook-step4.html)

🏋️

第5章：导航任务全景
**5 种导航任务全览**：PointNav · ObjectNav · ImageNav · InstanceImageNav · VLN。训练架构、评估指标、术语速查。

[📖 学习训练](habitat-textbook-step5.html)
[→](habitat-textbook-step5.html)

🚀

第5B章：DD-PPO 分布式训练
**单机多卡 PPO 扩展**：架构原理、配置对比、分布式启动命令、吞吐量缩放、6 种常见故障排查。

[📖 分布式训练](habitat-textbook-step5b.html)
[→](habitat-textbook-step5b.html)

🧭

第6章：RL 训练入门
**PointNav + PPO 实战**：训练全景图、策略网络结构（CNN+RNN）、RL 环境封装链、Benchmark 评估。

[📖 开始训练](habitat-textbook-step6.html)
[→](habitat-textbook-step6.html)

🔀 研究轨 → 部署轨
第1–6章 掌握 Habitat 平台 · 第7–9章 仿真训练 → 真机部署

🤖

第7章：VLN 视觉语言导航
**从零训练 VLN 模型**：VLN-v0 任务配置、R2R 数据集、InstructionSensor、模仿学习 + 评估导出 + SOTA实战(JanusVLN) + 避坑诊断。

[📖 方法一](habitat-textbook-step7.html)
[→](habitat-textbook-step7.html)

🧠

第8章：真机部署
**两种方案全覆盖**：VLN+ROS Nav2 分层式 + VLM 端到端直控。含 Spark-I / Leo ROS 软件包骨架。

[📖 方法二](habitat-textbook-step8.html)
[→](habitat-textbook-step8.html)

🦾

第9章：Rearrange 操作任务（Habitat 2.0）
**6 个案例从零掌握交互式操作**：Pick/Place 抓取放置、关节物体（抽屉/冰箱）、PDDL 复合任务（TidyHouse）。Fetch 机器人 + 物理仿真。

[📖 学习 Rearrange](habitat-textbook-step9.html)
[→](habitat-textbook-step9.html)

🔬 研究轨：掌握 Habitat 平台

第1章
安装环境
Conda + pip + 代理
habitat-sim + habitat-lab
交互式检查清单

第2章
跑通示例
5 个渐进示例
真实运行结果 + 图像
PointNav / Benchmark

第3章
读核心代码
调用链追踪器
参数调控台
6 模块源码分析

第4章
改配置实验
5 组配置实验
传感器 / 自定义 LiDAR
真实运行结果

第5章
导航任务全景
5 种导航任务全览
训练架构 + 术语速查
PointNav→ObjectNav→VLN

📎 研究轨扩展：专项深入

第1B章
完整数据集下载
7 种场景 + 6 种任务
Gibson/MP3D/HM3D
授权申请 + 目录规范

第5B章
DD-PPO 分布式训练
PPO → 多GPU扩展
NCCL + preemption
单机多卡吞吐量翻倍

第6章
RL 训练入门
PointNav + PPO 实战
策略网络结构解析
RL 环境封装链

🤖 部署轨：VLN → 真机

第7章
VLN 视觉语言导航
VLN-v0 + R2R 数据集
模仿学习 → 评估导出
避坑诊断 + DAgger

第8章
真机部署
VLN+ROS Nav2 分层
VLM 端到端控制
Spark-I / Leo 适配

🦾 进阶轨：Habitat 2.0 交互式操作

第9章
Rearrange 操作任务
Pick/Place/Open/Close
PDDL 复合任务
Fetch + 物理仿真

📚 专题深度 & 参考资源

主线教程之外的补充材料，深入特定主题。

🧭

VLN 视觉语言导航 · 专题
6 大技术范型 · 11 维对比表 · 核心架构维度分析 · 从 R2R 到 LLM Planning · Habitat 中的 VLN 实现

🔌

工程架构可视化
Habitat-Lab 完整模块依赖图 · 核心层/任务层/数据层/RL 层/配置层 · 10 大模块对比

🤖

VLN → 真机部署 · 实战
两种部署方案对比：VLN+ROS Nav2 vs VLM 端到端 · Spark-I / Leo 机器人 ROS 软件包骨架

🧭

VLN 仿真训练 · 实战
从配置 VLN-v0 任务到导出 checkpoint · R2R 数据集 · InstructionSensor · 评估指标解读

🗺️ 站点导航图

所有页面的关系一览。建议按箭头方向阅读。

[🏠 学习中心](index.html)

↓

[📗 教科书（11章总览）](habitat-textbook.html)

↓

[第1章 · 安装](habitat-textbook-step1.html)
→
[第2章 · 跑示例](habitat-textbook-step2.html)
→
[第3章 · 读代码](habitat-textbook-step3.html)
→
[第4章 · 改配置](habitat-textbook-step4.html)
→
[第5章 · 任务全景](habitat-textbook-step5.html)

┌ 扩展 ────────────────────────────────┐

[第1B章 · 数据集](habitat-textbook-step1b.html)
|
[第5B章 · DD-PPO](habitat-textbook-step5b.html)
|
[第6章 · RL 训练](habitat-textbook-step6.html)

└ ─────────────────────────────────────┘
┊

[第7章 · VLN](habitat-textbook-step7.html)
→
[第8章 · 真机部署](habitat-textbook-step8.html)

┊

[第9章 · Rearrange](habitat-textbook-step9.html)

└ ─ ─ ─ ─ ─ 横向扩展（专题页） ─ ─ ─ ─ ─ ┘

[🧭 VLN 专题](vln.html)
[🔌 架构可视化](architecture.html)
传感器深度 (即将上线)
论文精读 (即将上线)
