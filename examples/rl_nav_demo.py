#!/usr/bin/env python3
"""RL Navigation Demo — complete walkthrough of RL-based PointNav training.

This script demonstrates the full RL pipeline for visual navigation:
  Part 1 — Environment: observation space, action space, reward signal
  Part 2 — Policy: network architecture (CNN + GRU + Actor/Critic)
  Part 3 — Training: run PPO for N updates and show learning progress
  Part 4 — Inference: run the trained policy step-by-step

Usage:
  # Quick explore (no training needed)
  python examples/rl_nav_demo.py --explore-only

  # Full demo (explore + train + inference)
  python examples/rl_nav_demo.py --train-steps 50000

  # Skip training, use existing checkpoint for inference
  python examples/rl_nav_demo.py --skip-train

  # Use a specific checkpoint
  python examples/rl_nav_demo.py --skip-train --ckpt data/new_checkpoints/ckpt.50.pth

  # Only inference (skip env exploration)
  python examples/rl_nav_demo.py --skip-train --inference-only

Requirements:
  pip install -e habitat-lab
  pip install -e habitat-baselines
"""

import argparse
import os
import sys
import time

import numpy as np


# ---------------------------------------------------------------------------
# Part 1 + Part 4 combined: env exploration + policy inference (single env lifecycle)
# ---------------------------------------------------------------------------

def demo_env_and_inference(do_inference=True, ckpt_path=None):
    """Create env once, show observations + actions, optionally run trained policy."""
    import gym
    import habitat.gym  # noqa: F401 — registers Habitat-v0

    env = gym.make(
        "Habitat-v0",
        cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
    )

    # ---- Part 1: Environment ----
    print("=" * 70)
    print("PART 1: Understanding the RL Environment")
    print("=" * 70)

    print("\n[1.1] Task & Dataset")
    print(f"  Env:     Habitat-v0 (Gym API)")
    print(f"  Task:    PointNav (navigate to point goal)")
    print(f"  Dataset: habitat-test-scenes (3 scenes, offline)")

    print("\n[1.2] Observation Space")
    obs = env.reset()
    for key, val in obs.items():
        print(f"  {key:20s}  shape={str(val.shape):20s}  dtype={val.dtype}")

    print("\n[1.3] Action Space (discrete)")
    action_names = ["STOP", "MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT"]
    for i, name in enumerate(action_names):
        print(f"  [{i}] {name}")

    print("\n[1.4] Reward Signal")
    print("  reward = -(new_distance_to_goal - old_distance_to_goal)")
    print("  → Moving closer = +reward, moving away = -reward")

    print("\n[1.5] Sample Episode (random actions)")
    obs = env.reset()
    total_reward = 0.0
    for step in range(50):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            print(f"  Episode ended at step {step+1}")
            print(f"  Total reward: {total_reward:.3f}")
            print(f"  Info: {info}")
            break
    else:
        print(f"  Reached step limit (50), total reward: {total_reward:.3f}")

    # ---- Part 4: Inference ----
    if not do_inference:
        env.close()
        return

    print("\n" + "=" * 70)
    print("PART 4: Inference — Watch the Trained Policy")
    print("=" * 70)

    if ckpt_path is None:
        ckpt_dir = "data/new_checkpoints"
        if not os.path.isdir(ckpt_dir):
            print("  No checkpoints found. Run training first.\n")
            env.close()
            return
        ckpts = sorted(
            [
                f for f in os.listdir(ckpt_dir)
                if f.startswith("ckpt.") and f.endswith(".pth")
                and f.replace("ckpt.", "").replace(".pth", "").isdigit()
            ],
            key=lambda x: int(x.replace("ckpt.", "").replace(".pth", "")),
        )
        if not ckpts:
            print("  No checkpoints found. Run training first.\n")
            env.close()
            return
        ckpt_path = os.path.join(ckpt_dir, ckpts[-1])

    # Build the full config (benchmark + baselines) via Hydra
    # Must register both plugins so Hydra can resolve cross-repo defaults
    from habitat.config.default_structured_configs import register_hydra_plugin
    from habitat_baselines.config.default_structured_configs import (
        HabitatBaselinesConfigPlugin,
    )
    register_hydra_plugin(HabitatBaselinesConfigPlugin)

    from hydra import compose, initialize_config_dir
    from omegaconf import OmegaConf

    config_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..",
                     "habitat-baselines", "habitat_baselines", "config")
    )
    with initialize_config_dir(config_dir=config_dir, version_base=None):
        full_cfg = compose(config_name="pointnav/ppo_pointnav_example.yaml")
    OmegaConf.set_readonly(full_cfg, False)
    full_cfg.habitat_baselines.num_environments = 1
    OmegaConf.set_readonly(full_cfg, True)

    import torch
    from habitat_baselines.rl.ddppo.policy.resnet_policy import PointNavResNetPolicy

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    policy = PointNavResNetPolicy.from_config(
        full_cfg, env.observation_space, env.action_space,
    )
    policy.to(device)

    print(f"\n  Loading checkpoint: {ckpt_path}")
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    policy.load_state_dict(ckpt["state_dict"])
    policy.eval()

    n_params = sum(p.numel() for p in policy.parameters())
    print(f"  Policy: {n_params:,} parameters.")
    print(f"  Running 3 evaluation episodes...\n")

    for ep in range(3):
        obs = env.reset()
        rnn_state = torch.zeros(1, 1, 512, device=device)
        masks = torch.zeros(1, 1, device=device)
        prev_actions = torch.zeros(1, 1, dtype=torch.long, device=device)

        ep_reward = 0.0
        ep_steps = 0
        actions_taken = []

        for _step in range(200):
            batch = {
                k: torch.from_numpy(np.expand_dims(v, 0)).to(device)
                for k, v in obs.items()
            }
            batch["recurrent_hidden_states"] = rnn_state
            batch["prev_actions"] = prev_actions
            batch["masks"] = masks

            with torch.no_grad():
                result = policy.act(
                    batch, rnn_state, prev_actions, masks, deterministic=True,
                )
            rnn_state = result.rnn_hidden_states
            prev_actions.copy_(result.actions)
            action_idx = result.actions.item()
            actions_taken.append(action_names[action_idx])

            obs, reward, done, info = env.step(action_idx)
            ep_reward += reward
            ep_steps += 1
            if done:
                break

        success = info.get("success", 0)
        status = "SUCCESS" if success > 0 else "FAILED"
        dist = info.get("distance_to_goal", "?")
        spl = info.get("spl", 0)
        print(
            f"  Ep {ep+1}: [{status}]  steps={ep_steps:3d}  "
            f"reward={ep_reward:+.3f}  dist_to_goal={dist}  SPL={spl:.3f}"
        )
        acts = " → ".join(actions_taken[:25])
        if len(actions_taken) > 25:
            acts += " ..."
        print(f"         Actions: {acts}")

    env.close()


# ---------------------------------------------------------------------------
# Part 2: Policy Architecture
# ---------------------------------------------------------------------------

def explain_policy():
    """Explain the neural network architecture (no env needed)."""
    print("\n" + "=" * 70)
    print("PART 2: Policy Network Architecture")
    print("=" * 70)

    print("""
  Input (Observations)            Neural Network              Output (Actions)
  ═══════════════════════        ══════════════════          ═══════════════════

  ┌─────────────────────┐       ┌──────────────────┐
  │ RGB   256x256x3     │──┐    │  SimpleCNN       │      ┌─► STOP        [0]
  │ Depth 256x256x1     │──┤ →  │  3 Conv layers   │→512  │
  └─────────────────────┘  │    │  (32→64→32 ch)   │      ├─► MOVE_FWD    [1]
                            │    └──────────────────┘      │
  ┌─────────────────────┐  │                              ├─► TURN_LEFT   [2]
  │ PointGoal [ρ, φ]    │──┘    ┌──────────────────┐      │
  │ (distance, angle)   │       │  GRU (512-dim)   │      └─► TURN_RIGHT  [3]
  └─────────────────────┘  ┌───→│  hidden=512       │→512
                            │    └──────────────────┘       Categorical
                            │         │                    Distribution
                            │    ┌────┴────┐              (4 discrete actions)
                            │    │         │
                            │  Actor   Critic
                            │  (π)     (V)
                            │  action  value
                            │  logits  estimate

  Total parameters: ~5.8M (for ResNet18 backbone: ~29M)

  Key design choices:
  1. GPS+Compass sensor = PRIVILEGED geometric info (perfect relative goal)
     → Bypasses SLAM — policy focuses purely on visual navigation
  2. GRU hidden state = implicit map / memory
     → Remembers corridors, dead-ends without explicit grid map
  3. Actor-Critic: Actor selects actions, Critic estimates future return
     → PPO uses Advantage = (actual - predicted) to guide policy updates
""")


# ---------------------------------------------------------------------------
# Part 3: Training
# ---------------------------------------------------------------------------

def run_training(total_steps=100000, log_interval=10, num_checkpoints=10):
    """Run PPO training via the official habitat_baselines.run entry point."""
    print("=" * 70)
    print("PART 3: PPO Training")
    print("=" * 70)

    import subprocess

    cmd = [
        sys.executable, "-u", "-m", "habitat_baselines.run",
        "--config-name=pointnav/ppo_pointnav_example.yaml",
        f"habitat_baselines.total_num_steps={total_steps}",
        f"habitat_baselines.num_updates=-1",
        f"habitat_baselines.log_interval={log_interval}",
        f"habitat_baselines.num_checkpoints={num_checkpoints}",
        "habitat_baselines.checkpoint_folder=data/new_checkpoints",
        "habitat_baselines.tensorboard_dir=data/tb",
        "habitat_baselines.video_dir=data/video_dir",
    ]

    print(f"\n  Training for {total_steps:,} steps...")
    print(f"  (This runs as a subprocess — training happens in a fresh process)")
    print(f"  Equivalent command:")
    print(f"  $ {' '.join(cmd)}\n")

    result = subprocess.run(cmd, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"\n  Training exited with code {result.returncode}")
        return None
    return "data/new_checkpoints"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="RL Navigation Demo for Habitat PointNav"
    )
    parser.add_argument(
        "--train-steps", type=int, default=50000,
        help="Total training steps (default: 50000)",
    )
    parser.add_argument(
        "--ckpt", type=str, default=None,
        help="Path to checkpoint for inference",
    )
    parser.add_argument(
        "--skip-train", action="store_true",
        help="Skip training, use existing checkpoint for inference",
    )
    parser.add_argument(
        "--explore-only", action="store_true",
        help="Only explore environment, skip training/inference",
    )
    parser.add_argument(
        "--inference-only", action="store_true",
        help="Skip env exploration, only run inference",
    )
    args = parser.parse_args()

    if not args.inference_only:
        # Part 2: Architecture (print only)
        explain_policy()

        # Part 1+4: Environment + Inference (single env lifecycle)
        if args.explore_only:
            demo_env_and_inference(do_inference=False)
            print("\nDone (--explore-only).")
            return

        if not args.skip_train:
            # Part 3: Training (runs in subprocess)
            run_training(total_steps=args.train_steps)

        # Part 4: Inference (reuses the env created in Part 1)
        demo_env_and_inference(do_inference=True, ckpt_path=args.ckpt)
    else:
        demo_env_and_inference(do_inference=True, ckpt_path=args.ckpt)

    print("\n" + "=" * 70)
    print("Demo complete! Key takeaways:")
    print("=" * 70)
    print("""
  1. Habitat PointNav trains an END-TO-END visuomotor policy
     RGB+Depth+GoalVector → CNN+GRU → (STOP|FWD|LEFT|RIGHT)

  2. The ONLY reward signal is geodesic distance change
     No explicit map, no planner, no controller — learned from pixels

  3. The GRU hidden state acts as an IMPLICIT MAP
     Storing corridor layouts and dead-end memory in 512 floats

  4. GPS+Compass is PRIVILEGED INFORMATION
     Perfect relative goal vector bypasses the SLAM problem
     Real robots use visual odometry or SLAM to approximate this

  5. Training is SAMPLE-INEFFICIENT by nature
     Production configs use DD-PPO with multi-GPU (millions of steps)

  Next steps for the course:
  - Run inference:  python examples/rl_nav_demo.py --skip-train
  - Train longer:   python examples/rl_nav_demo.py --train-steps 500000
  - View tensorboard logs: tensorboard --logdir data/tb
  - Try ImageNav:   change config to imagenav/ppo_imagenav_example.yaml
""")


if __name__ == "__main__":
    main()
