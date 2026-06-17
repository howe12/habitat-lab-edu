"""提取两组帧的ResNet和CLIP特征"""
import sys, os, numpy as np, torch, torch.nn.functional as F
from pathlib import Path

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

DEVICE = "cuda"
BATCH = 64
OUT_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/features")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Printer
PRERENDER_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/renders/val_unseen")
ONLINE_DIR = Path("/root/gpufree-data/habitat-lab-edu/cache/online_frames")

def load_resnet():
    import torchvision.models as tv
    resnet = tv.resnet18(weights=tv.ResNet18_Weights.DEFAULT)
    resnet = torch.nn.Sequential(*list(resnet.children())[:-1])
    resnet = resnet.to(DEVICE).eval()
    return resnet

def load_clip():
    import open_clip
    m, _, p = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
    m = m.to(DEVICE).eval()
    return m

def load_frames(npz_dir, max_frames=None):
    """Load all frames from npz files, return (N, 3, 224, 224) tensor"""
    files = sorted(npz_dir.glob("*.npz"))
    frames = []
    for f in files:
        data = np.load(f)
        rgb = data["rgb"]  # (T, H, W, 3)
        for i in range(rgb.shape[0]):
            frame = rgb[i]
            frame_t = torch.from_numpy(frame).float().permute(2, 0, 1).unsqueeze(0) / 255.0
            frame_t = F.interpolate(frame_t, size=(224, 224), mode="bilinear", align_corners=False)
            frames.append(frame_t.squeeze(0))
            if max_frames and len(frames) >= max_frames:
                break
        if max_frames and len(frames) >= max_frames:
            break
    return torch.stack(frames)

@torch.no_grad()
def extract_resnet(model, frames):
    feats = []
    for i in range(0, len(frames), BATCH):
        batch = frames[i:i+BATCH].to(DEVICE)
        f = model(batch).squeeze(-1).squeeze(-1)
        feats.append(f.cpu().numpy())
    return np.concatenate(feats, axis=0)

@torch.no_grad()
def extract_clip(model, frames):
    feats = []
    for i in range(0, len(frames), BATCH):
        batch = frames[i:i+BATCH].to(DEVICE)
        f = model.encode_image(batch)
        feats.append(f.cpu().numpy())
    return np.concatenate(feats, axis=0)

print("[Extract] Loading ResNet...")
resnet = load_resnet()
print("[Extract] Loading CLIP...")
clip_model = load_clip()

# Prerendered frames
print("[Extract] Loading prerendered frames...")
pre_frames = load_frames(PRERENDER_DIR)
print(f"[Extract] Prerendered: {pre_frames.shape[0]} frames")

print("[Extract] ResNet features (prerendered)...")
pre_resnet = extract_resnet(resnet, pre_frames)
np.save(OUT_DIR / "pre_resnet.npy", pre_resnet)
print(f"[Extract] pre_resnet: {pre_resnet.shape}")

print("[Extract] CLIP features (prerendered)...")
pre_clip = extract_clip(clip_model, pre_frames)
np.save(OUT_DIR / "pre_clip.npy", pre_clip)
print(f"[Extract] pre_clip: {pre_clip.shape}")

# Online frames
print("[Extract] Loading online frames...")
online_frames = load_frames(ONLINE_DIR)
print(f"[Extract] Online: {online_frames.shape[0]} frames")

print("[Extract] ResNet features (online)...")
online_resnet = extract_resnet(resnet, online_frames)
np.save(OUT_DIR / "online_resnet.npy", online_resnet)
print(f"[Extract] online_resnet: {online_resnet.shape}")

print("[Extract] CLIP features (online)...")
online_clip = extract_clip(clip_model, online_frames)
np.save(OUT_DIR / "online_clip.npy", online_clip)
print(f"[Extract] online_clip: {online_clip.shape}")

del pre_frames, online_frames, resnet, clip_model
torch.cuda.empty_cache()
print("[Extract] Done!")
