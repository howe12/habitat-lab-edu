"""
完整版 VLN 评估：模型预测 action → env 执行 → 滚动窗口更新 RGB

§N 避坑实战 — 评估脚本修复：
  修复前：模型内部 txt_encoder 用随机噪声
  修复后：加载 TextEncoder + 实时编码指令文本
"""
import sys
import numpy as np
import torch
import torch.nn.functional as F
from pathlib import Path

sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")

from model import Seq2SeqAgent
from text_encoder import TextEncoder, encode_instruction, get_vocab
from eval_metrics import success_metric, spl, ndtw
from dataset import VLNDataset

import habitat

CKPT_PATH = "/root/gpufree-data/habitat-lab-edu/ckpt/vln_ckpt_best.pth"
NUM_EVAL = 50
MAX_STEPS = 30
WINDOW_SIZE = 5
DISTANCE_THRESHOLD = 3.0

MODEL_TO_ENV_ACTION = {0: 0, 1: 0, 2: 2, 3: 3, 4: 1}


def load_model_and_encoder(ckpt_path, device="cuda"):
    """加载模型 + TextEncoder"""
    vocab = get_vocab()
    text_encoder = TextEncoder(len(vocab), hidden_dim=256).to(device)
    model = Seq2SeqAgent(hidden_dim=256, num_actions=5, pretrained=False).to(device)
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model.load_state_dict(ckpt["model_state_dict"])
    if "text_encoder_state_dict" in ckpt:
        text_encoder.load_state_dict(ckpt["text_encoder_state_dict"])
    model.eval()
    text_encoder.eval()
    print(f"[Eval] Loaded ckpt: epoch={ckpt.get('epoch', '?')} val_loss={ckpt.get('val_loss', '?'):.3f}")
    return model, text_encoder


def get_model_action(model, text_encoder, instruction, rgb_window, prev_actions, device="cuda"):
    rgb_arr = np.stack(rgb_window, axis=0)
    rgb_tensor = torch.from_numpy(rgb_arr).float().permute(0, 3, 1, 2).unsqueeze(0).to(device) / 255.0
    rgb_tensor = F.interpolate(
        rgb_tensor.view(-1, 3, *rgb_tensor.shape[-2:]), size=(224, 224),
        mode="bilinear", align_corners=False
    ).view(1, WINDOW_SIZE, 3, 224, 224)

    # §N 修复: 真实文本编码
    token_ids = encode_instruction(instruction).unsqueeze(0).to(device)
    instr_feat = text_encoder(token_ids)

    prev_act = torch.tensor([prev_actions], dtype=torch.long).to(device)

    with torch.no_grad():
        action_logits, prog, stop = model(rgb_tensor, instr_feat, prev_act)
        action = action_logits[0, -1].argmax().item()
        stop_prob = stop[0, -1].item()

    return action, stop_prob


def run_episode(env, model, text_encoder, dataset, ep_idx, device="cuda"):
    ep = dataset.episodes[ep_idx]
    npz_path = dataset.render_dir / f"ep_{ep_idx:05d}.npz"
    if not npz_path.exists():
        return None
    cached = np.load(npz_path)
    rgb_seq = cached["rgb"]

    env.current_episode = ep
    obs = env.reset()

    instruction = ep.instruction.text if hasattr(ep.instruction, "text") else str(ep.instruction)
    rgb_window = [rgb_seq[i] for i in range(min(WINDOW_SIZE, len(rgb_seq)))]
    prev_actions = [0] * WINDOW_SIZE

    agent_positions = []
    gt_positions = []
    state = env.sim.get_agent_state()
    agent_positions.append(np.array(state.position[:2]))
    gt_end = np.array(ep.reference_path[-1][:2])
    for p in ep.reference_path:
        gt_positions.append(np.array(p[:2]))
    agent_path_len = 0.0

    for step in range(MAX_STEPS):
        model_action, stop_prob = get_model_action(
            model, text_encoder, instruction, rgb_window, prev_actions, device=device
        )
        action = MODEL_TO_ENV_ACTION.get(model_action, 0)

        if action == 1 or stop_prob > 0.5:
            break

        obs = env.step(action=action)
        new_pos = np.array(env.sim.get_agent_state().position[:2])

        if len(agent_positions) > 0:
            agent_path_len += np.linalg.norm(new_pos - agent_positions[-1])
        agent_positions.append(new_pos)

        rgb_window = rgb_window[1:] + [obs["rgb"].astype(np.uint8)]
        prev_actions = prev_actions[1:] + [action]

        if len(agent_positions) > 1 and np.linalg.norm(new_pos - agent_positions[-2]) < 0.01:
            break
        if np.linalg.norm(new_pos - gt_end) < DISTANCE_THRESHOLD:
            break

    gt_path_len = sum(
        np.linalg.norm(gt_positions[i+1] - gt_positions[i])
        for i in range(len(gt_positions) - 1)
    )

    sr = success_metric(agent_positions, gt_end, threshold=DISTANCE_THRESHOLD)
    s = spl(sr > 0, agent_path_len, max(gt_path_len, 0.01))
    n_dtw = ndtw(agent_positions, gt_positions, threshold=DISTANCE_THRESHOLD)

    return {"sr": sr, "spl": s, "ndtw": n_dtw, "agent_len": agent_path_len,
            "gt_len": gt_path_len, "steps": len(agent_positions)}


def main():
    print(f"[Eval] Loading ckpt from {CKPT_PATH}")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, text_encoder = load_model_and_encoder(CKPT_PATH, device=device)

    print("[Eval] Loading dataset (for prerender RGB)...")
    ds = VLNDataset(split="val_unseen", num_episodes=None, use_cache=True)
    print(f"[Eval] Dataset: {len(ds)} episodes with cache")

    print("[Eval] Loading env for action execution...")
    config = habitat.get_config("benchmark/nav/vln_r2r.yaml")
    env = habitat.Env(config=config)

    eval_indices = ds.valid_indices[:NUM_EVAL]
    print(f"[Eval] Evaluating on {len(eval_indices)} episodes")

    results = []
    for i, idx in enumerate(eval_indices):
        try:
            r = run_episode(env, model, text_encoder, ds, idx, device=device)
            if r is not None:
                results.append(r)
        except Exception as e:
            print(f"  [Eval] Episode idx={idx} failed: {str(e)[:100]}")
            continue

        if (i + 1) % 10 == 0:
            sr_mean = np.mean([r["sr"] for r in results])
            spl_mean = np.mean([r["spl"] for r in results])
            ndtw_mean = np.mean([r["ndtw"] for r in results])
            print(f"[Eval] {i+1}/{len(eval_indices)} | SR={sr_mean:.3f} SPL={spl_mean:.3f} nDTW={ndtw_mean:.3f}")

    env.close()

    if results:
        sr_mean = np.mean([r["sr"] for r in results])
        spl_mean = np.mean([r["spl"] for r in results])
        ndtw_mean = np.mean([r["ndtw"] for r in results])
        print(f"\n[Eval] ========== FINAL ==========")
        print(f"[Eval] Episodes evaluated: {len(results)}")
        print(f"[Eval] SR   = {sr_mean:.3f} ({sr_mean*100:.1f}%)")
        print(f"[Eval] SPL  = {spl_mean:.3f}")
        print(f"[Eval] nDTW = {ndtw_mean:.3f}")
        print(f"[Eval] Avg steps = {np.mean([r['steps'] for r in results]):.1f}")
        print(f"[Eval] Avg agent_len = {np.mean([r['agent_len'] for r in results]):.2f}m")
        print(f"[Eval] Avg gt_len = {np.mean([r['gt_len'] for r in results]):.2f}m")
    else:
        print("[Eval] No successful episodes")


if __name__ == "__main__":
    main()
