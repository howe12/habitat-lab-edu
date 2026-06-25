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
