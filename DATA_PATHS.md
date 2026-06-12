# 数据集上传路径参考

运行 `bash setup_cloud.sh` 后，以下目录已自动创建。将本地数据上传到对应路径即可。

## 场景数据集 → `data/scene_datasets/`

| 数据集 | 上传目标路径 | 本机大小 | 内容 |
|--------|-------------|---------|------|
| habitat-test-scenes | `data/scene_datasets/habitat-test-scenes/` | 218MB | 3 个测试场景 (.glb) |
| mp3d_example | `data/scene_datasets/mp3d_example/` | 93MB | 1 个 MP3D 场景 (17DRP5sb8fy) |
| mp3d (来自清华云盘) | `data/scene_datasets/mp3d/` | 754MB | 12 个 MP3D 场景 (.glb + .navmesh) |
| hm3d example | `data/scene_datasets/hm3d/` | 341MB | 3 个 HM3D 场景 (.glb + .basis.glb + .navmesh) |
| replica_cad | `data/scene_datasets/replica_cad/` | 302MB | 5 stages + objects (Rearrange 用) |

**上传命令示例（从本机执行）：**
```bash
# 全部场景（~1.7GB）
rsync -avzP /develop/habitat-lab/data/scene_datasets/ \
    user@cloud:/path/to/habitat-lab/data/scene_datasets/

# 或者只传最小集（~220MB，够跑 ppo_pointnav_example）
rsync -avzP \
    /develop/habitat-lab/data/versioned_data/habitat_test_scenes/ \
    user@cloud:/path/to/habitat-lab/data/versioned_data/habitat_test_scenes/
```

**注意**：hm3d 和 replica_cad 在 `scene_datasets/` 下是 symlink，指向 `versioned_data/`。如果用 rsync，加 `-l` 保留符号链接；如果用 scp，需要单独传 `versioned_data/` 目录并在服务器上手动创建 symlink：

```bash
# 在云服务器上创建 symlink（如果 scp 破坏了链接）
cd data/scene_datasets
ln -sf ../versioned_data/hm3d-0.2/hm3d hm3d
ln -sf ../versioned_data/replica_cad_dataset replica_cad
```

## 任务数据集 → `data/datasets/`

| 任务 | 上传目标路径 | 大小 | 训练场景 |
|------|-------------|------|---------|
| **PointNav** | | | |
| pointnav_gibson_v1 | `data/datasets/pointnav/gibson/v1/` | 已解压 | PointNav on Gibson |
| pointnav_gibson_v2 | `data/datasets/pointnav/gibson/v2/` | zip (150MB) | PointNav on Gibson v2 |
| pointnav_habitat_test | `data/datasets/pointnav/habitat-test-scenes/v1/` | 900KB | **快速验证 (ppo_pointnav_example)** |
| pointnav_mp3d_v1 | `data/datasets/pointnav/mp3d/v1/` | 已解压 | PointNav on MP3D |
| pointnav_hm3d_v1 | `data/datasets/pointnav/hm3d/v1/` | zip | PointNav on HM3D |
| **ObjectNav** | | | |
| objectnav_mp3d_v1 | `data/datasets/objectnav/mp3d/v1/` | zip (170MB) | ObjectNav on MP3D |
| objectnav_hm3d_v1 | `data/datasets/objectnav/hm3d/v1/` | zip | ObjectNav on HM3D |
| objectnav_hm3d_v2 | `data/datasets/objectnav/hm3d/v2/` | zip | ObjectNav on HM3D v2 |
| **VLN** | | | |
| vln_r2r_mp3d_v1 | `data/datasets/vln/mp3d/r2r/v1/` | 2.7MB | VLN (R2R) |
| **EQA** | | | |
| eqa_mp3d_v1 | `data/datasets/eqa/mp3d/v1/{split}/` | 44MB | EQA on MP3D |
| **Rearrange** | | | |
| rearrange_pick | `data/datasets/rearrange_pick/replica_cad/v0/` | 11MB | Pick/Place |

**上传命令示例：**
```bash
# 全部任务数据集（~3.1GB）
rsync -avzP /develop/habitat-lab/data/datasets/ \
    user@cloud:/path/to/habitat-lab/data/datasets/

# 或者只传需要的（例如只做 PointNav 快速验证 + MP3D PointNav + VLN）
rsync -avzP \
    /develop/habitat-lab/data/datasets/pointnav/habitat-test-scenes/ \
    /develop/habitat-lab/data/datasets/pointnav/mp3d/ \
    /develop/habitat-lab/data/datasets/vln/ \
    user@cloud:/path/to/habitat-lab/data/datasets/
```

## 上传后的目录结构检查

上传完成后，`data/` 目录应该类似这样：

```
data/
├── scene_datasets/
│   ├── habitat-test-scenes/
│   │   ├── apartment_1.glb -> ../versioned_data/habitat_test_scenes/apartment_1.glb
│   │   ├── skokloster-castle.glb -> ...
│   │   └── van-gogh-room.glb -> ...
│   ├── mp3d/
│   │   ├── 17DRP5sb8fy/       # 训练场景 (来自 mp3d_example)
│   │   ├── 2azQ1b91cZZ/       # val_unseen 场景 (来自清华云盘)
│   │   └── ... (共 12 个场景)
│   ├── mp3d_example/
│   ├── hm3d -> ../versioned_data/hm3d-0.2/hm3d/
│   └── replica_cad -> ../versioned_data/replica_cad_dataset/
├── datasets/
│   ├── pointnav/
│   │   ├── habitat-test-scenes/v1/   # ← ppo_pointnav_example 的最小依赖
│   │   ├── mp3d/v1/                  # ← PointNav on MP3D (需要 mp3d 场景)
│   │   └── ...
│   ├── objectnav/
│   ├── vln/mp3d/r2r/v1/             # ← VLN 训练
│   └── rearrange_pick/
└── versioned_data/
    ├── habitat_test_scenes/
    ├── hm3d-0.2/
    └── replica_cad_dataset/
```

## 快速验证

上传完成后，跑最小训练验证 pipeline：

```bash
conda activate habitat
cd /path/to/habitat-lab

python -u -m habitat_baselines.run \
    --config-name=pointnav/ppo_pointnav_example \
    habitat_baselines.total_num_steps=50000 \
    habitat_baselines.num_environments=1
```

如果成功输出训练日志（update: 1, fps: xxx, total_reward: xxx），则部署完成。
