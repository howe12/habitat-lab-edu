"""
预渲染脚本 v2 - 每个 episode 独立 env，崩溃隔离。
- 断点续传（已存在则跳过）
- 单 episode 失败不影响整个进程
- 失败计数 + 详细日志

修复 v1 错误：使用 habitat.Env(config=config)，不是 make_env。
"""
import numpy as np
from pathlib import Path
import time
import sys
import traceback

sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")

import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--split", default="val_unseen")
args, _ = parser.parse_known_args()
CACHE_DIR = Path(f"/root/gpufree-data/habitat-lab-edu/cache/renders/{args.split}")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

NUM_STEPS = 5


def render_one_episode(idx, ep, config_path):
    """渲染单个 episode（独立 env）。

    返回 (success: bool, msg: str)。
    """
    out_path = CACHE_DIR / f"ep_{idx:05d}.npz"

    # 断点续传：已存在跳过
    if out_path.exists():
        return True, "skip"

    import habitat

    # 加载配置
    config = habitat.get_config(config_path)

    # 关键：直接构造 env（habitat 0.2.5 API）
    env = habitat.Env(config=config)

    try:
        env.current_episode = ep
        obs = env.reset()
        rgb_seq = []
        for step in range(NUM_STEPS):
            rgb_seq.append(obs["rgb"].astype(np.uint8))
            obs = env.step(action=2)  # MOVE_FORWARD
        rgb_seq = np.stack(rgb_seq)  # (5, 256, 256, 3)
        np.savez_compressed(out_path, rgb=rgb_seq, scene_id=str(ep.scene_id))
        return True, "ok"
    finally:
        env.close()


def main():
    print(f"[PreRender v2] Cache dir: {CACHE_DIR}")

    import habitat

    # 用 dataset 模式加载 episodes 列表
    config = habitat.get_config("benchmark/nav/vln_r2r.yaml")
    config_path = "/root/gpufree-data/habitat-lab-edu/habitat-lab/habitat/config/benchmark/nav/vln_r2r.yaml"
    env = habitat.Env(config=config)
    episodes = list(env.episodes)
    total = len(episodes)
    env.close()
    del env

    print(f"[PreRender v2] Total episodes: {total}")

    done_count = 0
    skip_count = 0
    fail_count = 0
    failed_episodes = []
    start_time = time.time()

    for idx in range(total):
        ep = episodes[idx]

        try:
            success, msg = render_one_episode(idx, ep, config_path)
            if msg == "skip":
                skip_count += 1
            elif msg == "ok":
                done_count += 1
            else:
                fail_count += 1
                failed_episodes.append((idx, str(ep.scene_id), msg))
        except Exception as e:
            fail_count += 1
            err_msg = str(e)[:150]
            failed_episodes.append((idx, str(ep.scene_id), err_msg))
            # 只打印前 5 个 + 每 50 个
            if fail_count <= 5 or fail_count % 50 == 0:
                print(f"[PreRender v2] FAILED idx={idx}: {err_msg}")

        # 每 50 个汇报一次进度
        processed = done_count + skip_count + fail_count
        if processed % 50 == 0:
            elapsed = time.time() - start_time
            rate = done_count / elapsed if elapsed > 0 else 0
            remaining = total - processed
            eta = remaining / rate / 60 if rate > 0 else 0
            print(f"[PreRender v2] {processed}/{total} | "
                  f"done={done_count} skip={skip_count} fail={fail_count} | "
                  f"{rate:.2f} ep/s | ETA: {eta:.1f} min")

    elapsed_total = time.time() - start_time
    print(f"\n[PreRender v2] ========== DONE ==========")
    print(f"[PreRender v2] Rendered: {done_count}")
    print(f"[PreRender v2] Skipped: {skip_count}")
    print(f"[PreRender v2] Failed: {fail_count}")
    print(f"[PreRender v2] Total time: {elapsed_total / 60:.1f} min")

    if failed_episodes:
        print(f"\n[PreRender v2] Failed episodes (showing all):")
        for idx, scene_id, err in failed_episodes:
            print(f"  idx={idx:5d} scene={scene_id:60s} err={err[:80]}")

    cache_size_mb = sum(f.stat().st_size for f in CACHE_DIR.glob('*.npz')) / 1024 / 1024
    print(f"[PreRender v2] Cache size: {cache_size_mb:.1f} MB")


if __name__ == "__main__":
    main()