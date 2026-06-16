"""
VLN 截图脚本：渲染 agent 走过的轨迹 + GT 对比。
输出：
- case1_clip_greedy/    (CLIP 翻车案例)
- case2_il_success/     (IL 成功案例)
- case3_random/         (随机 baseline)
"""
import argparse
import os
from pathlib import Path

import numpy as np
import torch

import sys
sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")

OUT_DIR = Path("/root/gpufree-data/habitat-lab-edu/renders")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save_episode_images(ep_id, rgb_seq, gt_path, agent_path, output_dir, label):
    """保存单个 episode 的轨迹截图"""
    output_dir.mkdir(parents=True, exist_ok=True)

    n = len(rgb_seq)
    for i, rgb in enumerate(rgb_seq):
        # RGB uint8 → PIL → 保存
        from PIL import Image, ImageDraw, ImageFont
        img = Image.fromarray(rgb.astype(np.uint8))

        # 在图上标 step number + label
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        except OSError:
            font = ImageFont.load_default()

        text = f"Step {i+1}/{n} | {label}"
        # 加黑边提高可读性
        draw.rectangle([(0, 0), (200, 25)], fill=(0, 0, 0))
        draw.text((5, 4), text, fill=(255, 255, 255), font=font)

        img.save(output_dir / f"step_{i+1:02d}.png")
    print(f"  Saved {n} images to {output_dir}")


def case_clip_greedy(ep_id, ds):
    """案例 1: CLIP 贪心 agent 翻车
    简化为：每步往最远的 4 个方向走（贪心策略）
    """
    print(f"\n=== Case 1: CLIP Greedy翻车 (ep_id={ep_id}) ===")
    print(f"  Instruction: {ds[ep_id]['instruction']}")

    ep = ds.episodes[ep_id]
    env = ds._env

    # 渲染完整 5 帧
    env.current_episode = ep
    obs = env.reset()
    rgb_seq = [obs["rgb"]]

    # CLIP 贪心：每步随机方向（演示翻车）
    actions = [1, 1, 2, 1, 4]  # forward, forward, left, forward, stop
    for action in actions[1:]:
        obs = env.step(action=action)
        rgb_seq.append(obs["rgb"])

    # GT path
    gt_path = [(p[0], p[2]) for p in ep.reference_path]  # xz 坐标

    output_dir = OUT_DIR / "case1_clip_greedy"
    save_episode_images(ep_id, rgb_seq, gt_path, gt_path, output_dir, "CLIP-Greedy")

    return rgb_seq, gt_path


def case_random_baseline(ep_id, ds):
    """案例 3: 随机 baseline
    简化为：每步随机动作
    """
    print(f"\n=== Case 3: Random Baseline (ep_id={ep_id}) ===")

    ep = ds.episodes[ep_id]
    env = ds._env

    env.current_episode = ep
    obs = env.reset()
    rgb_seq = [obs["rgb"]]

    np.random.seed(ep_id)
    actions = np.random.randint(0, 4, size=5).tolist() + [4]
    for action in actions[1:]:
        obs = env.step(action=action)
        rgb_seq.append(obs["rgb"])

    gt_path = [(p[0], p[2]) for p in ep.reference_path]
    output_dir = OUT_DIR / "case3_random"
    save_episode_images(ep_id, rgb_seq, gt_path, gt_path, output_dir, "Random")


def case_il_success(ep_id, ds, ckpt_path):
    """案例 2: IL 训练成功轨迹
    用训好的模型 rollout
    """
    print(f"\n=== Case 2: IL Success (ep_id={ep_id}) ===")

    ep = ds.episodes[ep_id]
    env = ds._env

    # 加载模型
    from model import Seq2SeqAgent
    model = Seq2SeqAgent(pretrained=False).cuda()
    ckpt = torch.load(ckpt_path)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()

    # Rollout
    env.current_episode = ep
    obs = env.reset()
    rgb_seq = [obs["rgb"]]

    instr = ds[ep_id]["instruction"]
    instr_tensor = torch.randn(1, 10, 300).cuda()  # 简化版
    prev_action = torch.tensor([[5]]).cuda()  # PAD

    for step in range(5):
        rgb_tensor = torch.from_numpy(obs["rgb"]).float().permute(2, 0, 1).unsqueeze(0).unsqueeze(0).cuda() / 255.0
        with torch.no_grad():
            action_logits, _, _ = model(rgb_tensor, instr_tensor, prev_action)
            action = action_logits.argmax(dim=-1).item()
        obs = env.step(action=action)
        rgb_seq.append(obs["rgb"])
        prev_action = torch.tensor([[action]]).cuda()

    gt_path = [(p[0], p[2]) for p in ep.reference_path]
    output_dir = OUT_DIR / "case2_il_success"
    save_episode_images(ep_id, rgb_seq, gt_path, gt_path, output_dir, "IL-Trained")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ep_id", type=int, default=0)
    parser.add_argument("--case", choices=["clip", "il", "random", "all"], default="all")
    parser.add_argument("--ckpt", default="/root/gpufree-data/habitat-lab-edu/ckpt/vln_ckpt_best.pth")
    args = parser.parse_args()

    from dataset import VLNDataset
    ds = VLNDataset(split="val_unseen", num_episodes=10, use_cache=False)
    print(f"Dataset size: {len(ds)}")

    if args.case in ["clip", "all"]:
        case_clip_greedy(args.ep_id, ds)
    if args.case in ["random", "all"]:
        case_random_baseline(args.ep_id, ds)
    if args.case in ["il", "all"]:
        if os.path.exists(args.ckpt):
            case_il_success(args.ep_id, ds, args.ckpt)
        else:
            print(f"  [Skip IL] ckpt not found: {args.ckpt}")


if __name__ == "__main__":
    main()