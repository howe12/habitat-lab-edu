import re
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

LOG_DIR = Path("/root/gpufree-data/habitat-lab-edu/logs")
OUT_DIR = Path("/root/gpufree-data/habitat-lab-edu/screenshots/training_curves")
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({"font.size": 13, "figure.dpi": 150, "axes.grid": True, "grid.alpha": 0.3})

PAT = re.compile(r"\[Epoch (\d+)/\d+\] train_loss=([\d.]+) val_loss=([\d.]+) val_acc=([\d.]+)")

def parse_log(path):
    epochs, train_loss, val_loss, val_acc = [], [], [], []
    with open(path) as f:
        for line in f:
            m = PAT.search(line)
            if m:
                epochs.append(int(m.group(1)))
                train_loss.append(float(m.group(2)))
                val_loss.append(float(m.group(3)))
                val_acc.append(float(m.group(4)) * 100.0)
    return epochs, train_loss, val_loss, val_acc

def plot_curves(epochs, train_loss, val_loss, val_acc, title, path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    ax1.plot(epochs, train_loss, "b-o", markersize=6, label="Train Loss", linewidth=1.5)
    ax1.plot(epochs, val_loss, "r-s", markersize=6, label="Val Loss", linewidth=1.5)
    ax1.set_xlabel("Epoch"); ax1.set_ylabel("Loss")
    ax1.set_title(f"{title} - Loss"); ax1.legend()
    ax2.plot(epochs, val_acc, "g-^", markersize=7, label="Val Accuracy", linewidth=1.5)
    ax2.set_xlabel("Epoch"); ax2.set_ylabel("Accuracy (%)")
    ax2.set_title(f"{title} - Val Accuracy"); ax2.legend()
    ax2.set_ylim(0, 100)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white"); plt.close(fig)
    print(f"  Saved: {path}")

def plot_comparison(e1, va1, e2, va2, path):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(e1, va1, "r-o", markersize=6, label="Before Fix (cheating: rand text + leaked data)", linewidth=1.5, alpha=0.8)
    ax.plot(e2, va2, "g-s", markersize=6, label="After Fix (honest: real text + clean split)", linewidth=2)
    ax.set_xlabel("Epoch"); ax.set_ylabel("Val Accuracy (%)")
    ax.set_title("Val Accuracy: Before vs After Fix"); ax.legend(fontsize=11)
    ax.set_ylim(0, 100)
    for i, (e, v) in enumerate(zip(e1, va1)):
        ax.annotate(f"{v:.1f}%", (e, v), fontsize=8, color="red", ha="center", va="bottom")
    for i, (e, v) in enumerate(zip(e2, va2)):
        ax.annotate(f"{v:.1f}%", (e, v), fontsize=8, color="green", ha="center", va="bottom")
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white"); plt.close(fig)
    print(f"  Saved: {path}")

print("[Plot] Parsing logs...")
e1, tl1, vl1, va1 = parse_log(LOG_DIR / "run1_before_fix.log")
e2, tl2, vl2, va2 = parse_log(LOG_DIR / "vln_train_train_10ep.log")
print(f"  Before: {len(e1)} epochs, final val_acc={va1[-1]:.1f}%")
print(f"  After:  {len(e2)} epochs, final val_acc={va2[-1]:.1f}%")

plot_curves(e1, tl1, vl1, va1, "Before Fix", OUT_DIR / "before_fix_curves.png")
plot_curves(e2, tl2, vl2, va2, "After Fix", OUT_DIR / "after_fix_curves.png")
plot_comparison(e1, va1, e2, va2, OUT_DIR / "val_acc_comparison.png")
print("[Plot] Done!")
