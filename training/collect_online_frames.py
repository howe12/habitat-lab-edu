"""收集在线rollout帧：禁用stop，强制走满30步，收集偏航/撞墙帧"""
import sys, os, numpy as np, torch, torch.nn.functional as F
from pathlib import Path

sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")
from model import Seq2SeqAgent
from text_encoder import TextEncoder, encode_instruction, get_vocab
from eval_vln_full import load_model_and_encoder, get_model_action

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import habitat

CKPT = "/root/gpufree-data/habitat-lab-edu/ckpt/vln_ckpt_best.pth"
OUT_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/online_frames")
OUT_DIR.mkdir(parents=True, exist_ok=True)
NUM_EPISODES = 100
MAX_STEPS = 30
WINDOW = 5
DEVICE = "cuda"

MODEL_TO_ENV = {0: 0, 1: 0, 2: 2, 3: 3, 4: 1}

print("[Collect] Loading model...")
model, text_encoder = load_model_and_encoder(CKPT, DEVICE)

config_path = "/root/gpufree-data/habitat-lab-edu/habitat-lab/habitat/config/benchmark/nav/vln_r2r.yaml"
config = habitat.get_config(config_path)
env = habitat.Env(config=config)
episodes = list(env.episodes)
print(f"[Collect] {len(episodes)} episodes, collecting {NUM_EPISODES} (force 30 steps, no stop)")

collected = 0
for ep_idx in range(min(NUM_EPISODES, len(episodes))):
    out_path = OUT_DIR / f"ep_{ep_idx:05d}.npz"
    if out_path.exists():
        collected += 1
        continue

    ep = episodes[ep_idx]
    env.current_episode = ep
    obs = env.reset()
    instruction = ep.instruction.text if hasattr(ep.instruction, "text") else str(ep.instruction)

    rgb_online = []
    rgb_window = [obs["rgb"]] * WINDOW
    prev_actions = [0] * WINDOW

    for step in range(MAX_STEPS):
        rgb_online.append(obs["rgb"].astype(np.uint8))

        action, stop_prob = get_model_action(model, text_encoder, instruction, rgb_window, prev_actions, DEVICE)
        env_action = MODEL_TO_ENV.get(action, 0)

        obs = env.step(action=env_action)
        rgb_window = rgb_window[1:] + [obs["rgb"]]
        prev_actions = prev_actions[1:] + [action]

    rgb_online = np.stack(rgb_online)
    np.savez_compressed(out_path, rgb=rgb_online, scene_id=str(ep.scene_id))
    collected += 1

    if (ep_idx + 1) % 10 == 0:
        print(f"[Collect] {ep_idx+1}/{NUM_EPISODES} episodes, {collected} saved")

env.close()
total = 0
for f in OUT_DIR.glob("*.npz"):
    total += np.load(f)["rgb"].shape[0]
print(f"[Collect] Done: {collected} episodes, {total} frames (avg {total/collected:.1f}/ep)")
