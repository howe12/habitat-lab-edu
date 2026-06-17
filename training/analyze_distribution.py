"""Analyze distribution shift: MMD, cosine similarity histograms, t-SNE"""
import numpy as np, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FEAT_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/features")
OUT_DIR = Path("/root/gpufree-data/habitat-lab-edu/screenshots/clip_comparison")
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({"font.size": 12, "figure.dpi": 150})

def mmd_rbf(X, Y, sigma=1.0):
    XX = np.dot(X, X.T); YY = np.dot(Y, Y.T); XY = np.dot(X, Y.T)
    X_sqnorms = np.diag(XX); Y_sqnorms = np.diag(YY)
    K_XX = np.exp(-(X_sqnorms[:,None]+X_sqnorms[None,:]-2*XX)/(2*sigma**2))
    K_YY = np.exp(-(Y_sqnorms[:,None]+Y_sqnorms[None,:]-2*YY)/(2*sigma**2))
    K_XY = np.exp(-(X_sqnorms[:,None]+Y_sqnorms[None,:]-2*XY)/(2*sigma**2))
    return K_XX.mean() + K_YY.mean() - 2*K_XY.mean()

def cosine_dist(X, Y, ax, label, n=500):
    n = min(n, len(X), len(Y))
    ix = np.random.choice(len(X), n, replace=False)
    iy = np.random.choice(len(Y), n, replace=False)
    cos_x, cos_xy = [], []
    for i in range(0, n, 50):
        b = X[ix[i:i+50]] @ X[ix[i:i+50]].T
        nx = np.linalg.norm(X[ix[i:i+50]], axis=1)
        b /= nx[:,None] * nx[None,:] + 1e-8
        cos_x.extend(b[np.triu_indices(len(b), k=1)])
    for i in range(0, n, 50):
        b = X[ix[i:i+50]] @ Y[iy[i:i+50]].T
        nx = np.linalg.norm(X[ix[i:i+50]], axis=1)
        ny = np.linalg.norm(Y[iy[i:i+50]], axis=1)
        b /= nx[:,None] * ny[None,:] + 1e-8
        cos_xy.extend(b.flatten())
    ax.hist(cos_x, bins=50, alpha=0.5, label="Within Prerendered", density=True)
    ax.hist(cos_xy, bins=50, alpha=0.5, label="Pre vs Online", density=True)
    ax.set_xlabel("Cosine Similarity")
    ax.set_ylabel("Density")
    ax.set_title(label)
    ax.legend(fontsize=9)

def tsne_plot(X, Y, label, path, n=1000):
    from sklearn.manifold import TSNE
    n = min(n, len(X), len(Y))
    ix = np.random.choice(len(X), n, replace=False)
    iy = np.random.choice(len(Y), n, replace=False)
    combined = np.concatenate([X[ix], Y[iy]], axis=0)
    labels = np.array([0]*n + [1]*n)
    reduced = TSNE(n_components=2, random_state=42, perplexity=30).fit_transform(combined)
    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(reduced[:n,0], reduced[:n,1], c="blue", alpha=0.4, s=5, label="Prerendered")
    ax.scatter(reduced[n:,0], reduced[n:,1], c="red", alpha=0.4, s=5, label="Online")
    ax.set_title(f"t-SNE: {label}")
    ax.legend(fontsize=10); ax.set_xticks([]); ax.set_yticks([])
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"  t-SNE saved: {path}")

print("[Analyze] Loading features...")
pre_r = np.load(FEAT_DIR / "pre_resnet.npy")
pre_c = np.load(FEAT_DIR / "pre_clip.npy")
on_r  = np.load(FEAT_DIR / "online_resnet.npy")
on_c  = np.load(FEAT_DIR / "online_clip.npy")
print(f"  pre_resnet: {pre_r.shape}, online_resnet: {on_r.shape}")
print(f"  pre_clip:   {pre_c.shape}, online_clip:   {on_c.shape}")

print("\n[Analyze] Computing MMD...")
mmd_r = mmd_rbf(pre_r, on_r)
mmd_c = mmd_rbf(pre_c, on_c)
print(f"  ResNet MMD: {mmd_r:.4f}")
print(f"  CLIP   MMD: {mmd_c:.4f}")

print("\n[Analyze] Cosine similarity...")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
cosine_dist(pre_r, on_r, axes[0], f"ResNet (MMD={mmd_r:.4f})")
cosine_dist(pre_c, on_c, axes[1], f"CLIP (MMD={mmd_c:.4f})")
cs_path = OUT_DIR / "cosine_similarity.png"
fig.savefig(cs_path, bbox_inches="tight"); plt.close(fig)
print(f"  Saved: {cs_path}")

print("\n[Analyze] t-SNE...")
tsne_plot(pre_r, on_r, f"ResNet (MMD={mmd_r:.4f})", OUT_DIR / "tsne_resnet.png")
tsne_plot(pre_c, on_c, f"CLIP (MMD={mmd_c:.4f})", OUT_DIR / "tsne_clip.png")

summary = {
    "pre_frames": int(pre_r.shape[0]),
    "online_frames": int(on_r.shape[0]),
    "resnet_mmd": float(mmd_r),
    "clip_mmd": float(mmd_c),
}
with open(OUT_DIR / "summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print(f"\n[Analyze] Done! Results: {OUT_DIR}")
print(json.dumps(summary, indent=2))
