"""
VLN 训练主脚本。
- 用 dataset.py 加载（use_cache=True 走预渲染）
- 用 model.py 定义网络
- 标准 30 epoch 训练循环
- ckpt 保存：latest + best + epoch{N}
"""
import argparse
import os
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

import sys
sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")
from dataset_cheat import VLNDataset
from model_cheat import Seq2SeqAgent

CKPT_DIR = Path("/root/gpufree-data/habitat-lab-edu/ckpt")
LOG_DIR = Path("/root/gpufree-data/habitat-lab-edu/logs")
CKPT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("--split", default="val_unseen")
    p.add_argument("--num_episodes", type=int, default=500)
    p.add_argument("--epochs", type=int, default=10)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--num_workers", type=int, default=2)
    p.add_argument("--hidden_dim", type=int, default=256)
    p.add_argument("--save_every", type=int, default=1)  # 每 N epoch 保存 latest
    return p.parse_args()


def pad_collate(batch):
    """把不同长度的 seq pad 到一样长"""
    max_T = max(s["actions"].shape[0] for s in batch)
    B = len(batch)

    rgb_seqs = []
    instrs = []
    actions_list = []
    progress_list = []
    stop_list = []

    for s in batch:
        T = s["actions"].shape[0]
        pad_T = max_T - T

        # pad rgb
        rgb = s["rgb_seq"]  # (T, 3, H, W)
        if pad_T > 0:
            rgb_pad = torch.zeros(pad_T, *rgb.shape[1:])
            rgb = torch.cat([rgb, rgb_pad], dim=0)
        rgb_seqs.append(rgb)

        # pad action (用 5=PAD index)
        act = s["actions"]
        if pad_T > 0:
            act = torch.cat([act, torch.full((pad_T,), 5, dtype=torch.long)])
        actions_list.append(act)

        # pad progress
        prog = s["progress"]
        if pad_T > 0:
            prog = torch.cat([prog, torch.zeros(pad_T)])
        progress_list.append(prog)

        # pad stop
        stop = s["stop"]
        if pad_T > 0:
            stop = torch.cat([stop, torch.zeros(pad_T)])
        stop_list.append(stop)

        instrs.append(s["instruction"])

    return {
        "rgb_seq": torch.stack(rgb_seqs),
        "instruction": instrs,  # 留 string，不 token 化（简化版）
        "actions": torch.stack(actions_list),
        "progress": torch.stack(progress_list),
        "stop": torch.stack(stop_list),
    }


def fake_text_input(instrs, B, T, hidden_dim=256, device="cuda"):
    """简化版：用 LSTM 处理 string（这里用随机向量替代，等真接 BERT 再改）"""
    L = 10
    return torch.randn(B, L, 300, device=device)


def fake_prev_actions(actions, device="cuda"):
    """prev_actions[i] = actions[i-1]，第一个用 5 (PAD)"""
    B, T = actions.shape
    prev = torch.zeros_like(actions)
    prev[:, 1:] = actions[:, :-1]
    prev[:, 0] = 5  # PAD
    return prev.to(device)


def train_one_epoch(model, loader, optim, device, epoch, total_epochs):
    model.train()
    total_loss = 0
    n_batch = 0

    for batch_idx, batch in enumerate(loader):
        rgb_seq = batch["rgb_seq"].to(device)
        actions = batch["actions"].to(device)
        progress = batch["progress"].to(device)
        stop = batch["stop"].to(device)

        B, T = actions.shape

        # 简化文本输入（后期接 BERT）
        instr = fake_text_input(batch["instruction"], B, T, device=device)
        prev_actions = fake_prev_actions(actions, device=device)

        # 前向
        action_logits, prog_pred, stop_pred = model(rgb_seq, instr, prev_actions)

        # Loss
        action_loss = nn.functional.cross_entropy(
            action_logits.reshape(-1, 5), actions.reshape(-1), ignore_index=5
        )
        progress_loss = nn.functional.mse_loss(prog_pred, progress)
        stop_loss = nn.functional.binary_cross_entropy(stop_pred, stop)
        loss = action_loss + 0.1 * progress_loss + 0.05 * stop_loss

        optim.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        optim.step()

        total_loss += loss.item()
        n_batch += 1

        if batch_idx % 10 == 0:
            print(f"[Epoch {epoch}/{total_epochs}] batch {batch_idx}/{len(loader)} | "
                  f"loss={loss.item():.3f} (a={action_loss.item():.3f}, "
                  f"p={progress_loss.item():.3f}, s={stop_loss.item():.3f})")

    return total_loss / n_batch


def validate(model, loader, device):
    model.eval()
    total_loss = 0
    n_batch = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for batch in loader:
            rgb_seq = batch["rgb_seq"].to(device)
            actions = batch["actions"].to(device)
            progress = batch["progress"].to(device)
            stop = batch["stop"].to(device)

            B, T = actions.shape
            instr = fake_text_input(batch["instruction"], B, T, device=device)
            prev_actions = fake_prev_actions(actions, device=device)

            action_logits, prog_pred, stop_pred = model(rgb_seq, instr, prev_actions)

            action_loss = nn.functional.cross_entropy(
                action_logits.reshape(-1, 5), actions.reshape(-1), ignore_index=5
            )
            progress_loss = nn.functional.mse_loss(prog_pred, progress)
            stop_loss = nn.functional.binary_cross_entropy(stop_pred, stop)
            loss = action_loss + 0.1 * progress_loss + 0.05 * stop_loss

            total_loss += loss.item()
            n_batch += 1

            preds = action_logits.argmax(dim=-1)
            mask = actions != 5  # ignore pad
            correct += ((preds == actions) & mask).sum().item()
            total += mask.sum().item()

    return total_loss / n_batch, correct / max(total, 1)


def save_checkpoint(model, epoch, val_loss, is_best=False):
    """保存 ckpt"""
    # latest（覆盖）
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "val_loss": val_loss,
    }, CKPT_DIR / "vln_ckpt_latest.pth")

    # 每 N epoch 一个快照
    if epoch % 5 == 0:
        torch.save({
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "val_loss": val_loss,
        }, CKPT_DIR / f"vln_ckpt_epoch{epoch}.pth")

    # best（覆盖）
    if is_best:
        torch.save({
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "val_loss": val_loss,
        }, CKPT_DIR / "vln_ckpt_best.pth")


def cleanup_old_ckpts():
    """清理中间 epoch 快照，只保留 latest + best + 每 10 epoch"""
    import glob
    keep = {"vln_ckpt_latest.pth", "vln_ckpt_best.pth"}
    for ckpt in glob.glob(str(CKPT_DIR / "vln_ckpt_epoch*.pth")):
        name = Path(ckpt).name
        epoch_num = int(name.split("epoch")[1].split(".")[0])
        if epoch_num % 10 != 0:
            print(f"  [Cleanup] Remove {name}")
            os.remove(ckpt)


def main():
    args = get_args()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[Args] {args}")
    print(f"[Device] {device}")

    # Dataset
    print("[Data] Loading...")
    train_ds = VLNDataset(split=args.split, num_episodes=args.num_episodes, use_cache=True)
    # val 用同 split 的子集（简单起见）
    val_n = min(50, len(train_ds))
    val_ds = VLNDataset(split=args.split, num_episodes=args.num_episodes, use_cache=True)
    print(f"[Data] train={len(train_ds)}, val={val_n}")

    train_loader = DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True,
        num_workers=args.num_workers, collate_fn=pad_collate
    )
    val_loader = DataLoader(
        val_ds, batch_size=args.batch_size, shuffle=False,
        num_workers=args.num_workers, collate_fn=pad_collate
    )

    # Model
    print("[Model] Building...")
    model = Seq2SeqAgent(hidden_dim=args.hidden_dim, pretrained=True).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=args.lr)

    best_val_loss = float("inf")
    print(f"[Train] Starting {args.epochs} epochs...")

    for epoch in range(1, args.epochs + 1):
        t0 = time.time()
        train_loss = train_one_epoch(model, train_loader, optim, device, epoch, args.epochs)
        val_loss, val_acc = validate(model, val_loader, device)
        elapsed = time.time() - t0

        is_best = val_loss < best_val_loss
        if is_best:
            best_val_loss = val_loss

        print(f"[Epoch {epoch}/{args.epochs}] "
              f"train_loss={train_loss:.3f} val_loss={val_loss:.3f} val_acc={val_acc:.3f} "
              f"time={elapsed:.1f}s {'★' if is_best else ''}")

        if epoch % args.save_every == 0:
            save_checkpoint(model, epoch, val_loss, is_best)

    # 训练结束
    save_checkpoint(model, args.epochs, best_val_loss, is_best=False)
    cleanup_old_ckpts()
    print(f"[Train] Done. Best val_loss: {best_val_loss:.3f}")
    print(f"[Train] ckpts saved to {CKPT_DIR}")


if __name__ == "__main__":
    main()