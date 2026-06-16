"""
VLN Dataset for PyTorch training.
直接用 habitat.Env 加载 episode 对象，不再自己解析 JSON。

§N 避坑实战 — 数据集模块
  修复：Action 标签从 {FWD, LEFT} 扩展到 {FWD, LEFT, RIGHT, STOP}
  详见 _path_to_actions_and_progress() 的文档。
"""
import numpy as np
import torch
from torch.utils.data import Dataset
from pathlib import Path
import os

CACHE_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/renders")
SCENES_DIR = "/root/gpufree-data/habitat-lab-edu/data/scene_datasets/mp3d"


class VLNDataset(Dataset):
    """PyTorch Dataset for VLN training."""

    def __init__(self, split="train", num_episodes=None, use_cache=True):
        import habitat
        config = habitat.get_config("benchmark/nav/vln_r2r.yaml")
        self._env = habitat.Env(config=config)
        self.episodes = list(self._env.episodes)

        if num_episodes:
            self.episodes = self.episodes[:num_episodes]

        available_scenes = set(os.listdir(SCENES_DIR))
        before = len(self.episodes)
        self.episodes = [
            ep for ep in self.episodes
            if Path(ep.scene_id).stem in available_scenes
        ]
        print(f"[VLNDataset] {split}: {len(self.episodes)}/{before} episodes have local scenes")

        self.use_cache = use_cache
        self.split = split
        self.render_dir = CACHE_DIR / split
        self.render_dir.mkdir(parents=True, exist_ok=True)

        if self.use_cache:
            self.valid_indices = [
                i for i in range(len(self.episodes))
                if (self.render_dir / f"ep_{i:05d}.npz").exists()
            ]
            print(f"[VLNDataset] {split}: {len(self.valid_indices)}/{len(self.episodes)} episodes have cache")

    def __len__(self):
        if self.use_cache:
            return len(self.valid_indices)
        return len(self.episodes)

    def __getitem__(self, idx):
        if self.use_cache:
            real_idx = self.valid_indices[idx]
        else:
            real_idx = idx
        ep = self.episodes[real_idx]

        # 决定这次 episode 的步数
        ref_path = list(ep.reference_path) if ep.reference_path else []
        T = max(len(ref_path), 1)  # 至少 1 帧

        if self.use_cache:
            npz_path = self.render_dir / f"ep_{real_idx:05d}.npz"
            cached = np.load(npz_path)
            rgb_seq = cached["rgb"]
            # 取前 T 帧（如果缓存比 T 多）或 0-pad（如果缓存比 T 少）
            if rgb_seq.shape[0] >= T:
                rgb_seq = rgb_seq[:T]
            else:
                # 缓存不够，用 0 padding
                pad = np.zeros((T - rgb_seq.shape[0], *rgb_seq.shape[1:]), dtype=rgb_seq.dtype)
                rgb_seq = np.concatenate([rgb_seq, pad], axis=0)
            rgb_seq = torch.from_numpy(rgb_seq).float() / 255.0
            rgb_seq = rgb_seq.permute(0, 3, 1, 2)
        else:
            rgb_seq = self._render_episode(ep, T)

        # 算 actions 和 progress（基于 T 长度）
        actions, progress = self._path_to_actions_and_progress(ref_path)

        instr_text = ep.instruction.text if hasattr(ep.instruction, "text") else str(ep.instruction)

        return {
            "rgb_seq": rgb_seq,
            "instruction": instr_text,
            "actions": torch.tensor(actions, dtype=torch.long),
            "progress": torch.tensor(progress, dtype=torch.float32),
            "stop": torch.tensor(
                [1.0 if i == len(actions) - 1 else 0.0 for i in range(len(actions))],
                dtype=torch.float32
            ),
            "scene_id": ep.scene_id,
            "ep_id": real_idx,
        }

    def _path_to_actions_and_progress(self, ref_path):
        """§N 避坑实战 — Action 标签生成

        修复前：只有 FWD(1) 和 LEFT(2)，RIGHT(3) 永远不出现
          → abs(dx) > abs(dy) → 1, else → 2
          → 模型从未见过右转的标签

        修复后：基于 (dx, dy) 方向生成 4 种 action
          Action mapping: 0=PAD, 1=FWD, 2=LEFT, 3=RIGHT, 4=STOP
          dx 增大 → RIGHT(3), dx 减小 → LEFT(2), 其余 → FWD(1)

        注意：这是启发式标签，不是 VLN 的 ground truth expert action。
        课程定位：演示"标签错误如何影响训练"，而非教 VLN 正确做法。
        """
        if not ref_path or len(ref_path) < 2:
            return [4], [1.0]
        actions = []
        for i in range(len(ref_path) - 1):
            dx = ref_path[i + 1][0] - ref_path[i][0]
            dy = ref_path[i + 1][1] - ref_path[i][1]
            if abs(dx) < 0.01 and abs(dy) < 0.01:
                actions.append(4)  # STOP: 几乎不动
            elif dx > 0.05:
                actions.append(3)  # RIGHT: x 增大
            elif dx < -0.05:
                actions.append(2)  # LEFT: x 减小
            else:
                actions.append(1)  # FWD: 前进方向
        actions.append(4)  # STOP at end
        progress = [1.0 - i / max(len(actions) - 1, 1) for i in range(len(actions))]
        return actions, progress

    def _render_episode(self, ep, num_steps):
        self._env.current_episode = ep
        obs = self._env.reset()
        rgb_seq = []
        for _ in range(num_steps):
            rgb_seq.append(obs["rgb"])
            obs = self._env.step(action=2)
        rgb_seq = np.stack(rgb_seq).astype(np.uint8)
        rgb_seq = torch.from_numpy(rgb_seq).float() / 255.0
        rgb_seq = rgb_seq.permute(0, 3, 1, 2)
        return rgb_seq
