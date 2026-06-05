[![CircleCI](https://circleci.com/gh/facebookresearch/habitat-lab.svg?style=shield)](https://circleci.com/gh/facebookresearch/habitat-lab)
[![codecov](https://codecov.io/gh/facebookresearch/habitat-lab/branch/main/graph/badge.svg)](https://codecov.io/gh/facebookresearch/habitat-lab)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebookresearch/habitat-lab/blob/main/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/facebookresearch/habitat-lab)](https://github.com/facebookresearch/habitat-lab/releases/latest)
[![Supports Habitat_Sim](https://img.shields.io/static/v1?label=supports&message=Habitat%20Sim&color=informational&link=https://github.com/facebookresearch/habitat-sim)](https://github.com/facebookresearch/habitat-sim)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
[![Twitter Follow](https://img.shields.io/twitter/follow/ai_habitat?style=social)](https://twitter.com/ai_habitat)

Habitat-Lab
==============================

<style>
/* ---- language toggle tabs ---- */
.lang-switch {
  display: flex;
  gap: 0;
  margin: 16px 0 8px 0;
  border-bottom: 2px solid #30363d;
}
.lang-switch label {
  display: inline-block;
  padding: 8px 20px;
  cursor: pointer;
  color: #8b949e;
  font-size: 14px;
  font-weight: 600;
  border: 1px solid transparent;
  border-bottom: none;
  border-radius: 6px 6px 0 0;
  margin-bottom: -2px;
  user-select: none;
  transition: color 0.15s, background 0.15s;
}
.lang-switch label:hover {
  color: #c9d1d9;
  background: #161b22;
}
#lang-cn:checked ~ .lang-switch label[for="lang-cn"],
#lang-en:checked ~ .lang-switch label[for="lang-en"] {
  color: #e2e8f0;
  background: #0d1117;
  border-color: #30363d;
  border-bottom-color: #0d1117;
}

/* ---- content visibility ---- */
.lang-content .cn,
.lang-content .en {
  display: none;
}
#lang-cn:checked ~ .lang-content .cn {
  display: block;
}
#lang-en:checked ~ .lang-content .en {
  display: block;
}

/* ---- dark override for GitHub light-theme users ---- */
@media (prefers-color-scheme: light) {
  #lang-cn:checked ~ .lang-switch label[for="lang-cn"],
  #lang-en:checked ~ .lang-switch label[for="lang-en"] {
    color: #1e293b;
    background: #ffffff;
    border-color: #d0d7de;
    border-bottom-color: #ffffff;
  }
}
</style>

<input type="radio" id="lang-cn" name="lang" checked style="display:none">
<input type="radio" id="lang-en" name="lang" style="display:none">

<div class="lang-switch">
  <label for="lang-cn">中文</label>
  <label for="lang-en">English</label>
</div>

<div class="lang-content">

<!-- ====================================================================== -->
<!--                         CHINESE VERSION                               -->
<!-- ====================================================================== -->

<div class="cn">

## 从零理解 Habitat — 中文教学版

本仓库是 [facebookresearch/habitat-lab](https://github.com/facebookresearch/habitat-lab) 的**教学分支**，在原工程基础上增加了：

| 新增内容 | 说明 |
|---------|------|
| **中文 HTML 教材** | `habitat-viz/` — 7 步渐进式课程：安装 → PointNav → 传感器配置 → RL 训练与评测 → 自定义扩展 → ROS 桥接 |
| **RL 导航 Demo** | `examples/rl_nav_demo.py` — 一键运行：环境探索 → 策略架构 → PPO 训练 → 推理评估 |
| **PyTorch 2.6 兼容** | 修复 `torch.load(weights_only)` 和 `torch.where` 的兼容性问题 |

### 快速开始

```bash
# 安装
pip install -e habitat-lab
pip install -e habitat-baselines

# 打开教材首页
open habitat-viz/index.html

# 或启动本地服务器
cd habitat-viz && python3 -m http.server 8080

# 运行 RL 导航 Demo
python examples/rl_nav_demo.py --explore-only
```

### 课程目录

| 步 | 主题 |
|----|------|
| 第1步 | 安装与环境配置 |
| 第2步 | 第一个 PointNav 程序 |
| 第3步 | 可视化与调试 |
| 第4步 | 改配置实验（传感器、分辨率、动作） |
| 第5步 | **训练与评测**（PPO、Policy 网络、5种目标类型） |
| 第6步 | 自定义扩展（传感器、任务、规则） |
| 第7步 | ROS 桥接（Habitat ↔ ROS 2） |

> 原工程 LICENSE 和版权声明保持不变，见下方。

---

## 概述

Habitat-Lab 是一个模块化的高层次库，用于具身 AI 的端到端开发——定义具身 AI 任务（如导航、重排、指令跟随、问答）、配置具身智能体（物理形态、传感器、能力）、训练这些智能体（通过模仿学习或强化学习，或者完全不学习如 SensePlanAct 流水线），并在定义的任务上使用标准指标对其性能进行基准测试。

Habitat-Lab 使用 [`Habitat-Sim`](https://github.com/facebookresearch/habitat-sim) 作为核心模拟器。文档参考[此处](https://aihabitat.org/docs/habitat-lab/)。

[![Habitat Demo](https://img.shields.io/static/v1?label=WebGL&message=Try%20AI%20Habitat%20In%20Your%20Browser%20&color=blue&logo=webgl&labelColor=%23990000&style=for-the-badge&link=https://aihabitat.org/demo)](https://aihabitat.org/demo)
<p align="center">
  <img src="res/img/habitat_compressed.gif"  height="400">
</p>

---

## 目录
   1. [引用 Habitat](#引用-habitat)
   1. [安装](#安装)
   1. [测试](#测试)
   1. [文档](#文档)
   1. [Docker 配置](#docker-配置)
   1. [数据集](#数据集)
   1. [基线方法](#基线方法)
   1. [许可证](#许可证)


## 引用 Habitat
如果您在研究中使用 Habitat 平台，请引用 [Habitat 1.0](https://arxiv.org/abs/1904.01201) 和 [Habitat 2.0](https://arxiv.org/abs/2106.14405) 论文：

```
@inproceedings{szot2021habitat,
  title     =     {Habitat 2.0: Training Home Assistants to Rearrange their Habitat},
  author    =     {Andrew Szot and Alex Clegg and Eric Undersander and Erik Wijmans and Yili Zhao and John Turner and Noah Maestre and Mustafa Mukadam and Devendra Chaplot and Oleksandr Maksymets and Aaron Gokaslan and Vladimir Vondrus and Sameer Dharur and Franziska Meier and Wojciech Galuba and Angel Chang and Zsolt Kira and Vladlen Koltun and Jitendra Malik and Manolis Savva and Dhruv Batra},
  booktitle =     {Advances in Neural Information Processing Systems (NeurIPS)},
  year      =     {2021}
}

@inproceedings{habitat19iccv,
  title     =     {Habitat: {A} {P}latform for {E}mbodied {AI} {R}esearch},
  author    =     {Manolis Savva and Abhishek Kadian and Oleksandr Maksymets and Yili Zhao and Erik Wijmans and Bhavana Jain and Julian Straub and Jia Liu and Vladlen Koltun and Jitendra Malik and Devi Parikh and Dhruv Batra},
  booktitle =     {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year      =     {2019}
}
```

## 安装

1. **准备 conda 环境**

   假设您已安装 [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)，请准备一个 conda 环境：
   ```bash
   # 需要 python>=3.9 和 cmake>=3.14
   conda create -n habitat python=3.9 cmake=3.14.0
   conda activate habitat
   ```

1. **conda 安装 habitat-sim**
   - 安装带有 bullet 物理引擎的 habitat-sim：
      ```
      conda install habitat-sim withbullet -c conda-forge -c aihabitat
      ```
      更多细节请参考 Habitat-Sim 的[安装说明](https://github.com/facebookresearch/habitat-sim#installation)。

1. **pip 安装 habitat-lab 稳定版**。

      ```bash
      git clone --branch stable https://github.com/facebookresearch/habitat-lab.git
      cd habitat-lab
      pip install -e habitat-lab  # 安装 habitat_lab
      ```
1. **安装 habitat-baselines**。

    上述命令只安装 Habitat-Lab 的核心。要包含 habitat_baselines 及其所有附加依赖，请在安装 habitat-lab 后使用以下命令：

      ```bash
      pip install -e habitat-baselines  # 安装 habitat_baselines
      ```

## 测试

1. 使用 Habitat-Sim 的 Python 数据下载工具下载一些 3D 资产：
   - 下载（测试用）3D 场景：
      ```bash
      python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path data/
      ```
      请注意，这些测试场景不提供语义标注。

   - 下载测试场景的点目标导航 episode：
      ```bash
      python -m habitat_sim.utils.datasets_download --uids habitat_test_pointnav_dataset --data-path data/
      ```

1. **非交互式测试**：测试 Pick 任务：运行示例 pick 任务脚本
    ```bash
    python examples/example.py
    ```

    它使用 [`habitat-lab/habitat/config/benchmark/rearrange/pick.yaml`](habitat-lab/habitat/config/benchmark/rearrange/pick.yaml) 来配置任务和智能体。该脚本大致做以下事情：

    ```python
    import gym
    import habitat.gym

    # 加载具身 AI 任务 (RearrangePick) 和一个预先指定的虚拟机器人
    env = gym.make("HabitatRenderPick-v0")
    observations = env.reset()

    terminal = False

    # 使用随机动作在环境中步进
    while not terminal:
        observations, reward, terminal, info = env.step(env.action_space.sample())
    ```

    要修改环境的一些配置，您也可以使用 `habitat.gym.make_gym_from_config` 方法，它允许您使用配置来创建 Habitat 环境。

    ```python
    config = habitat.get_config(
      "benchmark/rearrange/pick.yaml",
      overrides=["habitat.environment.max_episode_steps=20"]
    )
    env = habitat.gym.make_gym_from_config(config)
    ```

    如果您想了解更多关于不同配置键覆盖项的作用，可以参考[此文档](habitat-lab/habitat/config/CONFIG_KEYS.md)。

    参见 [`examples/register_new_sensors_and_measures.py`](examples/register_new_sensors_and_measures.py) 了解如何在源代码**之外**扩展 habitat-lab。

1. **交互式测试**：使用键盘和鼠标在 ReplicaCAD 环境中控制 Fetch 机器人：
    ```bash
    # Pygame 用于交互式可视化，pybullet 用于逆运动学
    pip install pygame==2.0.1 pybullet==3.0.4

    # 交互式操作脚本
    python examples/interactive_play.py --never-end
    ```

   使用 I/J/K/L 键移动机器人底座（前/左/后/右），W/A/S/D 移动机械臂末端执行器（前/左/后/右），E/Q 上下移动机械臂。通过末端执行器控制机械臂可能比较困难。更多细节请参考文档。尝试移动底座和机械臂去触碰桌上的红色碗。祝玩得开心！

   注意：交互式测试目前在 Ubuntu 20.04 上会失败，报错：`X Error of failed request: BadAccess (attempt to access private resource denied)`。我们正在修复此问题，修复后将更新说明。该脚本在 MacOS 上运行正常。

## 调试环境问题

我们的向量化环境非常快，但不够详细。使用 `VectorEnv` 时，某些错误可能会被静默吞没，导致进程挂起或难以解释的多进程错误。我们建议在调试时将环境变量 `HABITAT_ENV_DEBUG` 设置为 1（`export HABITAT_ENV_DEBUG=1`），因为这将使用更慢但更详细的 `ThreadedVectorEnv` 类。调试完成后不要忘记重置 `HABITAT_ENV_DEBUG`（`unset HABITAT_ENV_DEBUG`），因为 `VectorEnv` 比 `ThreadedVectorEnv` 快得多。

## 文档

浏览在线的 [Habitat-Lab 文档](https://aihabitat.org/docs/habitat-lab/index.html)以及关于[如何使用 Habitat 训练智能体](https://aihabitat.org/tutorial/2020/)的详细教程。对于 Habitat 2.0，请使用此[快速入门指南](https://aihabitat.org/docs/habitat2/)。


## Docker 配置
我们为 Habitat 提供了 Docker 容器，大约每年为 [Habitat Challenge](https://github.com/facebookresearch/habitat-challenge) 更新一次。这适用于配备 NVIDIA GPU 的机器，需要用户安装 [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)。按照以下步骤使用 Docker 配置 Habitat 技术栈：

1. 拉取 Habitat Docker 镜像：`docker pull fairembodied/habitat-challenge:testing_2022_habitat_base_docker`

1. 在 Habitat Docker 中启动交互式 bash 会话：`docker run --runtime=nvidia -it fairembodied/habitat-challenge:testing_2022_habitat_base_docker`

1. 激活 Habitat conda 环境：`conda init; source ~/.bashrc; source activate habitat`

1. 运行上述测试脚本：`cd habitat-lab; python examples/example.py`。这应该会打印出类似以下的输出：
    ```bash
    Agent acting inside environment.
    Episode finished after 200 steps.
    ```

### 有问题？
找不到问题的答案？尝试在我们的 [Discussions 论坛](https://github.com/facebookresearch/habitat-lab/discussions)向开发者和社区提问。

## 数据集

[与 Habitat-Lab 一起使用的常见任务和 episode 数据集](DATASETS.md)。

## 基线方法
Habitat-Lab 包含强化学习（通过 PPO）基线。有关在示例数据上运行 PPO 训练以及更多细节，请参考 [habitat_baselines/README.md](habitat-baselines/habitat_baselines/README.md)。

## ROS-X-Habitat
ROS-X-Habitat (https://github.com/ericchen321/ros_x_habitat) 是一个通过 ROS 将 AI Habitat 平台（Habitat Lab + Habitat Sim）与其他机器人资源桥接的框架。与 Habitat-PyRobot 相比，ROS-X-Habitat 侧重于 1) 利用 Habitat Sim v2 的基于物理的仿真能力，以及 2) 允许机器人专家从 ROS 访问仿真资产。该工作也已作为[论文](https://arxiv.org/abs/2109.07703)公开发表。

请注意，ROS-X-Habitat 由 UBC 计算智能实验室开发并维护；它尚未获得 Habitat Lab 团队的官方支持。请参考该框架的仓库获取文档和讨论。


## 许可证
Habitat-Lab 使用 MIT 许可证。详情见 [LICENSE 文件](/LICENSE)。

训练模型和任务数据集被视为源自相应场景数据集的数据。

- 基于 Matterport3D 的任务数据集和训练模型遵循 [Matterport3D 使用条款](http://kaldir.vc.in.tum.de/matterport/MP_TOS.pdf)和 [CC BY-NC-SA 3.0 US 许可证](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)分发。
- 基于 Gibson 的任务数据集、生成此类数据集的代码以及训练模型遵循 [Gibson 使用条款](https://storage.googleapis.com/gibson_material/Agreement%20GDS%2006-04-18.pdf)和 [CC BY-NC-SA 3.0 US 许可证](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)分发。

</div>

<!-- ====================================================================== -->
<!--                         ENGLISH VERSION                               -->
<!-- ====================================================================== -->

<div class="en">

Habitat-Lab is a modular high-level library for end-to-end development in embodied AI --
defining embodied AI tasks (e.g. navigation, rearrangement, instruction following, question answering), configuring embodied agents (physical form, sensors, capabilities), training these agents (via imitation or reinforcement learning, or no learning at all as in SensePlanAct pipelines), and benchmarking their performance on the defined tasks using standard metrics.

Habitat-Lab uses [`Habitat-Sim`](https://github.com/facebookresearch/habitat-sim) as the core simulator. For documentation refer [here](https://aihabitat.org/docs/habitat-lab/).

[![Habitat Demo](https://img.shields.io/static/v1?label=WebGL&message=Try%20AI%20Habitat%20In%20Your%20Browser%20&color=blue&logo=webgl&labelColor=%23990000&style=for-the-badge&link=https://aihabitat.org/demo)](https://aihabitat.org/demo)
<p align="center">
  <img src="res/img/habitat_compressed.gif"  height="400">
</p>

---

## Table of contents
   1. [Citing Habitat](#citing-habitat)
   1. [Installation](#installation)
   1. [Testing](#testing)
   1. [Documentation](#documentation)
   1. [Docker Setup](#docker-setup)
   1. [Datasets](#datasets)
   1. [Baselines](#baselines)
   1. [License](#license)


## Citing Habitat
If you use the Habitat platform in your research, please cite the [Habitat 1.0](https://arxiv.org/abs/1904.01201) and [Habitat 2.0](https://arxiv.org/abs/2106.14405) papers:

```
@inproceedings{szot2021habitat,
  title     =     {Habitat 2.0: Training Home Assistants to Rearrange their Habitat},
  author    =     {Andrew Szot and Alex Clegg and Eric Undersander and Erik Wijmans and Yili Zhao and John Turner and Noah Maestre and Mustafa Mukadam and Devendra Chaplot and Oleksandr Maksymets and Aaron Gokaslan and Vladimir Vondrus and Sameer Dharur and Franziska Meier and Wojciech Galuba and Angel Chang and Zsolt Kira and Vladlen Koltun and Jitendra Malik and Manolis Savva and Dhruv Batra},
  booktitle =     {Advances in Neural Information Processing Systems (NeurIPS)},
  year      =     {2021}
}

@inproceedings{habitat19iccv,
  title     =     {Habitat: {A} {P}latform for {E}mbodied {AI} {R}esearch},
  author    =     {Manolis Savva and Abhishek Kadian and Oleksandr Maksymets and Yili Zhao and Erik Wijmans and Bhavana Jain and Julian Straub and Jia Liu and Vladlen Koltun and Jitendra Malik and Devi Parikh and Dhruv Batra},
  booktitle =     {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year      =     {2019}
}
```

## Installation

1. **Preparing conda env**

   Assuming you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) installed, let's prepare a conda env:
   ```bash
   # We require python>=3.9 and cmake>=3.14
   conda create -n habitat python=3.9 cmake=3.14.0
   conda activate habitat
   ```

1. **conda install habitat-sim**
   - To install habitat-sim with bullet physics
      ```
      conda install habitat-sim withbullet -c conda-forge -c aihabitat
      ```
      See Habitat-Sim's [installation instructions](https://github.com/facebookresearch/habitat-sim#installation) for more details.

1. **pip install habitat-lab stable version**.

      ```bash
      git clone --branch stable https://github.com/facebookresearch/habitat-lab.git
      cd habitat-lab
      pip install -e habitat-lab  # install habitat_lab
      ```
1. **Install habitat-baselines**.

    The command above will install only core of Habitat-Lab. To include habitat_baselines along with all additional requirements, use the command below after installing habitat-lab:

      ```bash
      pip install -e habitat-baselines  # install habitat_baselines
      ```

## Testing

1. Let's download some 3D assets using Habitat-Sim's python data download utility:
   - Download (testing) 3D scenes:
      ```bash
      python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path data/
      ```
      Note that these testing scenes do not provide semantic annotations.

   - Download point-goal navigation episodes for the test scenes:
      ```bash
      python -m habitat_sim.utils.datasets_download --uids habitat_test_pointnav_dataset --data-path data/
      ```

1. **Non-interactive testing**: Test the Pick task: Run the example pick task script
    <!--- Please, update `examples/example.py` if you update example. -->
    ```bash
    python examples/example.py
    ```

    which uses [`habitat-lab/habitat/config/benchmark/rearrange/pick.yaml`](habitat-lab/habitat/config/benchmark/rearrange/pick.yaml) for configuration of task and agent. The script roughly does this:

    ```python
    import gym
    import habitat.gym

    # Load embodied AI task (RearrangePick) and a pre-specified virtual robot
    env = gym.make("HabitatRenderPick-v0")
    observations = env.reset()

    terminal = False

    # Step through environment with random actions
    while not terminal:
        observations, reward, terminal, info = env.step(env.action_space.sample())
    ```

    To modify some of the configurations of the environment, you can also use the `habitat.gym.make_gym_from_config` method that allows you to create a habitat environment using a configuration.

    ```python
    config = habitat.get_config(
      "benchmark/rearrange/pick.yaml",
      overrides=["habitat.environment.max_episode_steps=20"]
    )
    env = habitat.gym.make_gym_from_config(config)
    ```

    If you want to know more about what the different configuration keys overrides do, you can use [this reference](habitat-lab/habitat/config/CONFIG_KEYS.md).

    See [`examples/register_new_sensors_and_measures.py`](examples/register_new_sensors_and_measures.py) for an example of how to extend habitat-lab from _outside_ the source code.



1. **Interactive testing**: Using you keyboard and mouse to control a Fetch robot in a ReplicaCAD environment:
    ```bash
    # Pygame for interactive visualization, pybullet for inverse kinematics
    pip install pygame==2.0.1 pybullet==3.0.4

    # Interactive play script
    python examples/interactive_play.py --never-end
    ```

   Use I/J/K/L keys to move the robot base forward/left/backward/right and W/A/S/D to move the arm end-effector forward/left/backward/right and E/Q to move the arm up/down. The arm can be difficult to control via end-effector control. More details in documentation. Try to move the base and the arm to touch the red bowl on the table. Have fun!

   Note: Interactive testing currently fails on Ubuntu 20.04 with an error: `X Error of failed request:  BadAccess (attempt to access private resource denied)`. We are working on fixing this, and will update instructions once we have a fix. The script works without errors on MacOS.

## Debugging an environment issue

Our vectorized environments are very fast, but they are not very verbose. When using `VectorEnv` some errors may be silenced, resulting in process hanging or multiprocessing errors that are hard to interpret. We recommend setting the environment variable `HABITAT_ENV_DEBUG` to 1 when debugging (`export HABITAT_ENV_DEBUG=1`) as this will use the slower, but more verbose `ThreadedVectorEnv` class. Do not forget to reset `HABITAT_ENV_DEBUG` (`unset HABITAT_ENV_DEBUG`) when you are done debugging since `VectorEnv` is much faster than `ThreadedVectorEnv`.

## Documentation

Browse the online [Habitat-Lab documentation](https://aihabitat.org/docs/habitat-lab/index.html) and the extensive [tutorial on how to train your agents with Habitat](https://aihabitat.org/tutorial/2020/). For Habitat 2.0, use this [quickstart guide](https://aihabitat.org/docs/habitat2/).


## Docker Setup
We provide docker containers for Habitat, updated approximately once per year for the [Habitat Challenge](https://github.com/facebookresearch/habitat-challenge). This works on machines with an NVIDIA GPU and requires users to install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker). To setup the habitat stack using docker follow the below steps:

1. Pull the habitat docker image: `docker pull fairembodied/habitat-challenge:testing_2022_habitat_base_docker`

1. Start an interactive bash session inside the habitat docker: `docker run --runtime=nvidia -it fairembodied/habitat-challenge:testing_2022_habitat_base_docker`

1. Activate the habitat conda environment: `conda init; source ~/.bashrc; source activate habitat`

1. Run the testing scripts as above: `cd habitat-lab; python examples/example.py`. This should print out an output like:
    ```bash
    Agent acting inside environment.
    Episode finished after 200 steps.
    ```

### Questions?
Can't find the answer to your question? Try asking the developers and community on our [Discussions forum](https://github.com/facebookresearch/habitat-lab/discussions).

## Datasets

[Common task and episode datasets used with Habitat-Lab](DATASETS.md).

## Baselines
Habitat-Lab includes reinforcement learning (via PPO) baselines. For running PPO training on sample data and more details refer [habitat_baselines/README.md](habitat-baselines/habitat_baselines/README.md).

## ROS-X-Habitat
ROS-X-Habitat (https://github.com/ericchen321/ros_x_habitat) is a framework that bridges the AI Habitat platform (Habitat Lab + Habitat Sim) with other robotics resources via ROS. Compared with Habitat-PyRobot, ROS-X-Habitat places emphasis on 1) leveraging Habitat Sim v2's physics-based simulation capability and 2) allowing roboticists to access simulation assets from ROS. The work has also been made public as a [paper](https://arxiv.org/abs/2109.07703).

Note that ROS-X-Habitat was developed, and is maintained by the Lab for Computational Intelligence at UBC; it has not yet been officially supported by the Habitat Lab team. Please refer to the framework's repository for docs and discussions.


## License
Habitat-Lab is MIT licensed. See the [LICENSE file](/LICENSE) for details.

The trained models and the task datasets are considered data derived from the correspondent scene datasets.

- Matterport3D based task datasets and trained models are distributed with [Matterport3D Terms of Use](http://kaldir.vc.in.tum.de/matterport/MP_TOS.pdf) and under [CC BY-NC-SA 3.0 US license](https://creativecommons.org/licenses/by-nc-sa/3.0/us/).
- Gibson based task datasets, the code for generating such datasets, and trained models are distributed with [Gibson Terms of Use](https://storage.googleapis.com/gibson_material/Agreement%20GDS%2006-04-18.pdf) and under [CC BY-NC-SA 3.0 US license](https://creativecommons.org/licenses/by-nc-sa/3.0/us/).

</div>

</div>
