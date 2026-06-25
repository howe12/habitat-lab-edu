# 第1章：安装环境 — Habitat 从零理解

> 从零开始，在你的机器上搭建一个可以运行的 Habitat 开发环境。
    本章假设你有一台 Linux 机器（或 WSL2），并且可以联网。

##  0. 开始之前 — 你需要什么

先确认你的环境满足这些条件，跳过这一步是后续所有报错的根源。

| 需求 | 最低要求 | 如何检查 |
| --- | --- | --- |
| **操作系统** | Ubuntu 20.04+ / WSL2 | `lsb_release -a` 或 `uname -a` |
| **GPU 驱动** | NVIDIA driver ≥ 450 | `nvidia-smi` |
| **Conda** | Miniconda 或 Anaconda | `conda --version` |
| **磁盘空间** | ≥ 20 GB 空闲 | `df -h`（场景数据需 10-15G） |
| **内存** | ≥ 16 GB | `free -h` |
| **网络** | 能访问 conda-forge / GitHub | `curl -I https://conda.anaconda.org` |

> ⚠️ **如果你在非 Linux 环境**

Habitat-Sim 官方只提供 **Linux conda 包**。macOS 用户需要通过源码编译 habitat-sim（高级操作，不推荐小白）。
Windows 用户建议使用 **WSL2 + Ubuntu 22.04**，体验与原生 Linux 基本一致。
如果你是在远程服务器上操作，确认有 sudo 或 conda 已在用户目录安装。

##  安装流程总览

整个安装流程分为 5 个阶段。每完成一个，勾选对应的复选框。

**1. Conda 环境**

python=3.9
cmake=3.14

→

**2. 配置代理**

conda proxy
channel 精简

→

**3. habitat-sim**

仿真引擎
conda install

→

**4. habitat-lab**

任务框架
pip install -e

→

**5. 验证 + 数据**

import 测试
下载场景

##  阶段 1：创建 Conda 环境

Habitat 对 Python 版本**非常敏感** — 必须使用 Python 3.9。3.10+ 会导致 habitat-sim 的 conda 包安装失败。

### 安装 Miniconda（如果还没有）

```
# 下载 Miniconda 安装脚本
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 运行安装（一路回车 + yes）
$ bash Miniconda3-latest-Linux-x86_64.sh

# 重新加载 shell 配置
$ source ~/.bashrc
$ conda --version  # 应输出: conda 24.x.x
```

### 创建 Habitat 专用环境

```
# 创建名为 "habitat" 的环境，同时装好 cmake
$ conda create -n habitat python=3.9 cmake=3.14.0 -y

# 激活环境 — 后续所有操作都在这个环境下
$ conda activate habitat

# 验证
(habitat) $ python --version  # Python 3.9.x ✓
(habitat) $ cmake --version    # cmake 3.14.0 ✓
```

**为什么要 cmake？**

`cmake` 只在**从源码编译** habitat-sim 时才需要。如果你只用 conda 安装预编译包，可以跳过 cmake。
但预装 cmake 不会增加任何负担，推荐保留。

> ⚠️ **Python 3.9 是硬性要求**

habitat-sim 的 conda 包 (`aihabitat/habitat-sim`) 目前只提供 Python 3.9 版本。
如果你尝试 `python=3.10` 或更高，conda 会报依赖冲突。
**不要试图绕过这个限制** — 这不是 bug，是当前的兼容性边界。

##  阶段 2：配置代理与 Channel

如果你在境外服务器上操作，可以跳过本章。如果你在大陆环境，这是**最容易卡住的环节**。

### 为什么 conda 需要单独配代理？

conda 的底层网络库不会自动读取系统的 `HTTP_PROXY` 环境变量。
你即使 export 了 `HTTP_PROXY=http://127.0.0.1:7897`，conda 仍然直连 —
这在有代理的环境中会导致 SSL EOF 或连接超时。必须**显式在 conda 配置中写入代理**。

#### 如果你有 Clash / V2Ray

```
$ conda config --set proxy_servers.http \
	    http://127.0.0.1:7897
$ conda config --set proxy_servers.https \
	    http://127.0.0.1:7897

# 验证
$ conda config --show proxy_servers
```

端口号根据你的代理软件调整（Clash 默认 7897，V2Ray 默认 10809）

#### 精简 Channel 列表

```
# 先清空再添加 → 避免混用多个源
$ conda config --remove-key channels
$ conda config --add channels conda-forge
$ conda config --add channels aihabitat

# 查看最终 channel 列表
$ conda config --show channels
```

只保留 conda-forge + aihabitat 两个 channel，避免连接数爆炸

> ⚠️ **常见坑：清华镜像混用导致 SSL EOF**

很多教程推荐用清华 tuna 镜像，但如果你同时保留了 conda-forge 和 aihabitat 的境外源，
三个源的 TLS 实现差异会导致 SSL EOF 错误。**要么全用境外源（配代理），要么全用镜像源。**
混用是大多数网络问题的根源。

##  阶段 3：安装 habitat-sim

habitat-sim 是底层 3D 仿真引擎。它不在 PyPI 上，**必须通过 conda 安装**。

```
# 核心安装命令 — 选择适合你的版本

# 选项 A：服务器版本（无 GUI，最常见）
$ conda install habitat-sim=0.2.5 withbullet headless \
    -c conda-forge -c aihabitat -y

# 选项 B：桌面版本（有 3D 窗口，需要显示器）
$ conda install habitat-sim=0.2.5 withbullet \
    -c conda-forge -c aihabitat -y
```

| 参数 | 含义 | 适合场景 |
| --- | --- | --- |
| `withbullet` | 带 Bullet 物理引擎（碰撞检测） | 几乎所有任务都需要 |
| `headless` | 不渲染 GUI 窗口，纯 GPU 离屏渲染 | 服务器 / SSH 无显示器 / 训练时 |
| `=0.2.5` | 与 habitat-lab v0.2.5 匹配的版本 | 保持与仓库一致 |

```
# 验证安装
$ python -c "import habitat_sim; print('habitat-sim', habitat_sim.__version__)"
# 期望输出: habitat-sim 0.2.5

# 更进一步：验证渲染管线
$ python -c "
import habitat_sim
sim_cfg = habitat_sim.SimulatorConfiguration()
print('Simulator config created — GPU rendering is ready')
"
```

> 💡 **如果你需要源码编译（macOS 或自定义版本）**

conda 包只有 Linux 版。macOS 或 ARM 架构需要用 `build.sh` 从源码编译 —
这需要安装大量依赖（包括 Bullet Physics、Assimp、GLFW 等），预计额外需要半天到一天。
如果你是初学者且用 macOS，建议先在云 GPU 服务器上跑通，再考虑本地编译。

##  阶段 4：安装 habitat-lab

habitat-lab 是纯 Python 包，安装简单。关键是用 `-e`（editable 模式），方便修改源码后即时生效。

```
# 确认你在 habitat-lab 仓库根目录
$ cd /develop/habitat-lab

# 以可编辑模式安装核心包
$ pip install -e habitat-lab

# (可选) 安装基线算法包 — 需要训练时再装
$ pip install -e habitat-baselines

# 验证
$ python -c "import habitat; print('habitat-lab ready')"
```

**`pip install -e` 是什么意思？**

`-e`（editable，可编辑模式）不会把代码复制到 site-packages，而是创建一个指向源码目录的符号链接。
这意味着你修改 `habitat/core/env.py` 之后，**不需要重新 pip install**，改动即时生效。
这是研究和开发的标准做法 — 你会频繁地修改、调试、添加打印语句。

> ⚠️ **必须先装 habitat-sim 再装 habitat-lab**

如果先 pip install habitat-lab，pip 可能尝试从 PyPI 安装一个名为 `habitat-sim` 的包（不存在），导致混乱。
正确的顺序：**conda install habitat-sim → pip install -e habitat-lab**。

##  阶段 5：下载测试数据 & 跑通验证

安装完成 ≠ 可以使用。你需要下载最小测试场景来验证整个安装链路。

```
# 方法 1 (推荐)：用 habitat-sim 内置下载工具
$ python -m habitat_sim.utils.datasets_download \
    --uids habitat_test_scenes habitat_test_pointnav_dataset \
    --data-path data/

# 方法 2：查看所有可用数据集
$ python -m habitat_sim.utils.datasets_download --list

# 方法 3 (备选)：如果下载脚本遇到网络问题，手动下载
# 从 https://dl.fbaipublicfiles.com/habitat/ 下载对应 .tar.gz 解压到 data/
```

### 终极验证：跑通 example.py

```
# 这是你的"Hello World" — 跑通它，环境就装好了
$ cd /develop/habitat-lab
$ python examples/example.py

# 期望输出（不含报错）：
# Episode 0: agent moving...
# Episode 1: agent moving...
# ...
# 程序正常结束，exit code = 0
```

> 💡 **如果你看到 3D 窗口（非 headless 模式）**

如果你安装的是不带 `headless` 的版本，`example.py` 会弹出一个 3D 窗口显示 Agent 的视角。
按 ESC 退出。服务器用户（SSH 连接）不会有这个窗口，只能看到终端输出 — 这是正常的。

**安装成功后，你的环境里有什么？**

`conda list | grep habitat` 应该显示：

· **habitat-sim** 0.2.5（C++ 渲染引擎，conda 包）

· **habitat-lab**（Python 任务框架，pip editable 安装）

· **habitat-baselines**（可选，算法训练包）

##  Docker 容器化部署（可选方案）

如果你的环境不方便直接安装 conda 和 habitat-sim，可以使用 Docker 容器方案。
官方镜像预装了完整的 Habitat 环境，一条命令就能跑。

**方案对比：Conda 安装 vs Docker 容器**

| 维度 | Conda 安装（推荐） | Docker 容器 |
| --- | --- | --- |
| **适用场景** | 日常开发、训练、调试 | 快速验证、CI/CD、环境隔离 |
| **安装难度** | 中等（需配置 conda + proxy） | 低（docker pull + run） |
| **GUI 支持** | ✅ 完整（可弹出渲染窗口） | ⚠️ 需额外配置 X11 forward |
| **磁盘占用** | ~3GB（conda env） | ~15GB（Docker 镜像） |
| **GPU 支持** | ✅ 直接使用 | ✅ 需要 nvidia-container-runtime |

```
Docker 部署三步骤
```

```
# 步骤 1：拉取官方镜像（约 15GB，仅首次）
$ docker pull fairembodied/habitat-challenge:testing_2022_habitat_base_docker

# 步骤 2：启动容器（挂载 data 目录以复用数据集）
$ docker run --runtime=nvidia -it --rm \
    -v $(pwd)/data:/data \
    fairembodied/habitat-challenge:testing_2022_habitat_base_docker \
    /bin/bash

# 步骤 3：容器内激活 conda 环境并验证
$ conda init; source ~/.bashrc; source activate habitat
$ python -c "import habitat_sim; import habitat; print('Docker OK')"
```

> ⚠️ **Docker 方案的注意事项**

· **镜像更新频率低**：官方镜像约每年更新一次（最新 tag 为 2022），版本可能落后于 pip 安装

· **需要 nvidia-container-runtime**：`apt install nvidia-container-runtime`，否则 GPU 不可用

· **数据挂载**：用 `-v` 将宿主机的 `data/` 目录挂入容器，避免每个容器内部重复下载

· **无 GUI**：默认 headless 模式，如需渲染窗口需额外配置 X11 forward (`-e DISPLAY` + `-v /tmp/.X11-unix`)

· **仓库根目录的 `Dockerfile`** 展示了完整构建过程（基于 nvidia/cudagl:10.1 + Miniconda + cmake 3.14）

> 💡 **实用建议**

**学习阶段用 Conda**（前面阶段1-5）— 方便改代码、调试、看渲染窗口。
**批量训练 / CI 用 Docker** — 环境一致性好，可复现，适合服务器端。
两种方案可共存，共享 `data/` 目录。

##  常见问题排查

这些是我在实践中遇到的真实错误。按症状查找你的问题。

#### SSL EOF / CONNECTION FAILED

**症状：**conda install 过程中报 `SSL EOF` 或 `Connection reset`

修复：检查 conda proxy 设置 + 精简 channel 列表（见阶段 2）。

**关键：**conda 不会用 `HTTP_PROXY` 环境变量，必须 `conda config --set proxy_servers`。

#### Solving environment: failed

**症状：**`conda install habitat-sim` 依赖解析失败

修复：确认 Python 版本 = 3.9（不是 3.10/3.11）。

试用 `conda install habitat-sim=0.2.5 withbullet headless -c conda-forge -c aihabitat --strict-channel-priority`

#### ImportError: libCURL.so

**症状：**`import habitat_sim` 报 libCURL.so 找不到

修复：`conda install curl -c conda-forge` —
habitat-sim 的渲染管线依赖特定的 libcurl 版本。

#### ImportError: No module named 'habitat'

**症状：**`import habitat` 失败

修复：确认：① conda activate habitat ② 在 habitat-lab 目录下 ③ pip install -e habitat-lab 执行成功。

运行 `pip list | grep habitat` 确认 habitat-lab 在列表中。

#### CUDA / OpenGL 渲染失败

**症状：**example.py 运行时报 `EGL / GLX error` 或 `CUDA out of memory`

修复：headless 模式下，确认安装了 EGL 库：

`sudo apt install libegl1-mesa-dev libgles2-mesa-dev`

GPU 内存不足：减小 RGB 分辨率或 batch size。

#### 数据集下载中断 / 极慢

**症状：**`datasets_download` 卡住或报网络错误

修复：该脚本用系统 `curl`，走的是 `HTTP_PROXY` 环境变量。

对 Matterport 域名可临时绕过代理：

`no_proxy="api.matterport.com" python -m habitat_sim.utils.datasets_download ...`

##  学后自检 — 你掌握了什么

如果你能独立回答以下 5 个问题，说明安装阶段已经扎实掌握了。

#### Q1：为什么要用 conda 而不是 pip 装 habitat-sim？

habitat-sim 是 C++ 项目，需要编译渲染管线（Magnum 引擎 + Bullet 物理）。conda 提供了预编译的二进制包，
避免了长达数小时的源码编译。PyPI 上没有 habitat-sim 的包。

#### Q2：headless vs 非 headless 的区别是什么？

headless = GPU 渲染到内存（帧缓冲），不显示窗口。训练 / 服务器用 headless。
非 headless = 弹出一个 3D 窗口实时显示。调试 / 演示用。两者计算结果完全一致。

#### Q3：pip install -e 中的 -e 有什么作用？

editable 模式 — 源码修改无需重新安装即生效。研究开发的标准做法。没有 -e 的话每次改一行代码都要重装。

#### Q4：conda 代理失败时，你的排查顺序是什么？

① `conda config --show proxy_servers` 确认已配 → ② `conda config --show channels` 确认只有 conda-forge + aihabitat → ③ 用 `curl` 测试代理端口是否可达。

#### Q5：安装完成后，你运行哪条命令验证一切正常？

`python examples/example.py` — 这条命令涵盖了 habitat-sim 渲染 + habitat-lab Env 创建 + step() 交互，是最全面的集成测试。

[← 返回教科书目录](habitat-textbook.html)
[第2章：跑通示例 →](habitat-textbook-step2.html)
