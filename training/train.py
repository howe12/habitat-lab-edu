"""
VLN 训练主脚本。

§N 避坑实战 — 训练脚本修复：
  修复前：fake_text_input() → torch.randn() 随机噪声
         train/val 同 split → 数据泄漏
         输出不保存 → 日志丢失
  修复后：TextEncoder 真实语义编码
         train/val 分离 split
         Tee 输出到文件

用法: python3.9 training/train.py --split train --num_episodes 500 --epochs 10
"""
import argparse
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, "/root/gpufree-data/habitat-lab-edu/training")
from dataset import VLNDataset
from model import Seq2SeqAgent
from text_encoder import TextEncoder, batch_encode, get_vocab

CKPT_DIR = Path("/root/gpufree-data/habitat-lab-edu/ckpt")
LOG_DIR = Path("/root/gpufree-data/habitat-lab-edu/logs")
CKPT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


class Tee:
    """同时输出到 stdout 和文件"""
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("--split", default="train")
    p.add_argument("--val_split", default="val_unseen")
    p.add_argument("--num_episodes", type=int, default=500)
    p.add_argument("--epochs", type=int, default=10)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--num_workers", type=int, default=2)
    p.add_argument("--hidden_dim", type=int, default=256)
    p.add_argument("--save_every", type=int, default=1)
    return p.parse_args()


def pad_collate(batch):
    """把不同长度的 seq pad 到一样长"""
    max_T = max(s["actions"].shape[0] for s in batch)
    B = len(batch)

    rgb_seqs, instrs = [], []
    actions_list, progress_list, stop_list = [], [], []

    for s in batch:
        T = s["actions"].shape[0]
        pad_T = max_T - T

        rgb = s["rgb_seq"]
        if pad_T > 0:
            rgb_pad = torch.zeros(pad_T, *rgb.shape[1:])
            rgb = torch.cat([rgb, rgb_pad], dim=0)
        rgb_seqs.append(rgb)

        act = s["actions"]
        if pad_T > 0:
            act = torch.cat([act, torch.full((pad_T,), 5, dtype=torch.long)])
        actions_list.append(act)

        prog = s["progress"]
        if pad_T > 0:
            prog = torch.cat([prog, torch.zeros(pad_T)])
        progress_list.append(prog)

        stop = s["stop"]
        if pad_T > 0:
            stop = torch.cat([stop, torch.zeros(pad_T)])
        stop_list.append(stop)

        instrs.append(s["instruction"])

    return {
        "rgb_seq": torch.stack(rgb_seqs),
        "instruction": instrs,
        "actions": torch.stack(actions_list),
        "progress": torch.stack(progress_list),
        "stop": torch.stack(stop_list),
    }


def fake_prev_actions(actions, device="cuda"):
    """prev_actions[i] = actions[i-1]，第一个用 5 (PAD)"""
    B, T = actions.shape
    prev = torch.zeros_like(actions)
    prev[:, 1:] = actions[:, :-1]
    prev[:, 0] = 5
    return prev.to(device)


def train_one_epoch(model, text_encoder, loader, optim, device, epoch, total_epochs):
    model.train()
    text_encoder.train()
    total_loss = 0
    n_batch = 0

    for batch_idx, batch in enumerate(loader):
        rgb_seq = batch["rgb_seq"].to(device)
        actions = batch["actions"].to(device)
        progress = batch["progress"].to(device)
        stop = batch["stop"].to(device)

        B, T = actions.shape

        # §N 修复: 真实文本编码 → TextEncoder
        token_ids = batch_encode(batch["instruction"], device=device)
        instr_feat = text_encoder(token_ids)  # (B, hidden_dim)

        prev_actions = fake_prev_actions(actions, device=device)

        action_logits, prog_pred, stop_pred = model(rgb_seq, instr_feat, prev_actions)

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


def validate(model, text_encoder, loader, device):
    model.eval()
    text_encoder.eval()
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
            token_ids = batch_encode(batch["instruction"], device=device)
            instr_feat = text_encoder(token_ids)
            prev_actions = fake_prev_actions(actions, device=device)

            action_logits, prog_pred, stop_pred = model(rgb_seq, instr_feat, prev_actions)

            action_loss = nn.functional.cross_entropy(
                action_logits.reshape(-1, 5), actions.reshape(-1), ignore_index=5
            )
            progress_loss = nn.functional.mse_loss(prog_pred, progress)
            stop_loss = nn.functional.binary_cross_entropy(stop_pred, stop)
            loss = action_loss + 0.1 * progress_loss + 0.05 * stop_loss

            total_loss += loss.item()
            n_batch += 1

            preds = action_logits.argmax(dim=-1)
            mask = actions != 5
            correct += ((preds == actions) & mask).sum().item()
            total += mask.sum().item()

    return total_loss / n_batch, correct / max(total, 1)


def save_checkpoint(model, text_encoder, epoch, val_loss, is_best=False):
    ckpt = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "text_encoder_state_dict": text_encoder.state_dict(),
        "val_loss": val_loss,
    }
    torch.save(ckpt, CKPT_DIR / "vln_ckpt_latest.pth")
    if epoch % 5 == 0:
        torch.save(ckpt, CKPT_DIR / f"vln_ckpt_epoch{epoch}.pth")
    if is_best:
        torch.save(ckpt, CKPT_DIR / "vln_ckpt_best.pth")


def main():
    args = get_args()
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Tee 输出到文件
    log_path = LOG_DIR / f"vln_train_{args.split}_{args.epochs}ep.log"
    log_file = open(log_path, "w")
    sys.stdout = Tee(sys.stdout, log_file)

    print(f"[Args] {args}")
    print(f"[Device] {device}")
    print(f"[Log] {log_path}")

    # §N 修复: train/val 分离 split
    print(f"[Data] Loading train={args.split}, val={args.val_split}...")
    train_ds = VLNDataset(split=args.split, num_episodes=args.num_episodes, use_cache=True)
    val_ds = VLNDataset(split=args.val_split, num_episodes=min(200, args.num_episodes), use_cache=True)
    print(f"[Data] train={len(train_ds)}, val={len(val_ds)}")

    train_loader = DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True,
        num_workers=args.num_workers, collate_fn=pad_collate,
    )
    val_loader = DataLoader(
        val_ds, batch_size=args.batch_size, shuffle=False,
        num_workers=args.num_workers, collate_fn=pad_collate,
    )

    # Model + TextEncoder
    print("[Model] Building...")
    vocab = get_vocab()
    text_encoder = TextEncoder(len(vocab), hidden_dim=args.hidden_dim).to(device)
    model = Seq2SeqAgent(hidden_dim=args.hidden_dim, pretrained=True).to(device)

    # Optimizer: model + text_encoder 一起优化
    optim = torch.optim.AdamW(
        list(model.parameters()) + list(text_encoder.parameters()), lr=args.lr
    )

    best_val_loss = float("inf")
    print(f"[Train] Starting {args.epochs} epochs...")

    for epoch in range(1, args.epochs + 1):
        t0 = time.time()
        train_loss = train_one_epoch(
            model, text_encoder, train_loader, optim, device, epoch, args.epochs
        )
        val_loss, val_acc = validate(model, text_encoder, val_loader, device)
        elapsed = time.time() - t0

        is_best = val_loss < best_val_loss
        if is_best:
            best_val_loss = val_loss

        print(f"[Epoch {epoch}/{args.epochs}] "
              f"train_loss={train_loss:.3f} val_loss={val_loss:.3f} val_acc={val_acc:.3f} "
              f"time={elapsed:.1f}s {'*BEST*' if is_best else ''}")

        if epoch % args.save_every == 0:
            save_checkpoint(model, text_encoder, epoch, val_loss, is_best)

    print(f"[Train] Done. Best val_loss: {best_val_loss:.3f}")
    print(f"[Train] ckpts saved to {CKPT_DIR}")
    print(f"[Train] log saved to {log_path}")
    log_file.close()


if __name__ == "__main__":
    main()
