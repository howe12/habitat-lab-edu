import json, random, sys, os, gzip
sys.path.insert(0, "/root/gpufree-data/JanusVLN/src")

# 随机抽 20 个 episode
data_path = "/root/gpufree-data/habitat-lab-edu/data/datasets/vln/mp3d/r2r/v1/val_unseen/val_unseen.json.gz"
with gzip.open(data_path) as f:
    data = json.load(f)

all_eps = data["episodes"]
random.seed(42)
sampled = random.sample(all_eps, min(20, len(all_eps)))

# 写临时数据集
tmp_path = "/tmp/val_20eps.json"
with open(tmp_path, "w") as f:
    json.dump({"episodes": sampled}, f)

print(f"抽样: {len(sampled)}/{len(all_eps)} episodes")
print("场景:", sorted(set(ep["scene_id"].split("/")[-2] for ep in sampled)))
print()

# 修改 habitat config 指向临时数据
import yaml
from evaluation import Evaluator

# 直接调用 Evaluator，但需要 hack env.episodes
# 更简单: 使用 habitat API
import habitat
from habitat.config.default import get_config

config = get_config("/root/gpufree-data/JanusVLN/config/vln_r2r.yaml")
config.defrost()
config.habitat.dataset.data_path = tmp_path
config.habitat.dataset.split = "val_unseen"
config.freeze()

print("开始 eval...")
# 直接调 evaluation.py 的 Evaluator，传 override dataset
