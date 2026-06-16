"""
§N 避坑实战 — 文本编码器（词表 + Embedding + LSTM）

修复前：train.py 用 torch.randn() 生成随机文本向量
  → 每轮训练指令都不同，模型无法从文本学到任何信息
  → 模型实际学的是"看 RGB 序列推测方向"（Vision-only）

修复后：从 R2R 指令集构建词表 → nn.Embedding → LSTM 编码
  → 同一条指令永远得到相同的向量
  → 模型真正开始学习"理解指令"
  → Embedding 从零训练（不依赖预训练词向量，无需外部下载）

课程定位：展示"从零学习词嵌入"的完整流程
"""
import re
import torch
import torch.nn as nn
from pathlib import Path

# ——— 词表构建 ———
# 首次使用时会自动从 R2R 数据集构建
_VOCAB = None
_EMBEDDING_DIM = 300
_MAX_SEQ_LEN = 30
_PAD_TOKEN = "<PAD>"
_UNK_TOKEN = "<UNK>"


def _build_vocab_from_r2r():
    """从 R2R train split 的指令文本构建词表。
    只取出现 >=2 次的词，加 PAD/UNK 特殊 token。
    """
    print("[TextEncoder] Building vocabulary from R2R instructions...")
    import habitat
    config = habitat.get_config("benchmark/nav/vln_r2r.yaml")
    env = habitat.Env(config=config)
    episodes = list(env.episodes)
    env.close()

    word_counts = {}
    for ep in episodes:
        instr = ep.instruction.text if hasattr(ep.instruction, "text") else str(ep.instruction)
        text = instr.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        for w in text.split():
            word_counts[w] = word_counts.get(w, 0) + 1

    # 过滤：出现 >=2 次的词
    words = sorted([w for w, c in word_counts.items() if c >= 2])
    vocab = {_PAD_TOKEN: 0, _UNK_TOKEN: 1}
    for w in words:
        vocab[w] = len(vocab)

    print(f"[TextEncoder] Vocabulary size: {len(vocab)} (from {len(episodes)} episodes)")
    return vocab


def get_vocab():
    global _VOCAB
    if _VOCAB is None:
        _VOCAB = _build_vocab_from_r2r()
    return _VOCAB


# ——— Tokenize & Encode ———


def tokenize(text):
    """小写 + 去标点 + 空格分词"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


def encode_instruction(text, vocab=None, max_len=_MAX_SEQ_LEN):
    """把指令文本转成 token ID 序列。

    Returns:
        torch.LongTensor (max_len,) — PAD=0, UNK=1, 实际词从 2 开始
    """
    if vocab is None:
        vocab = get_vocab()
    tokens = tokenize(text)[:max_len]
    ids = [vocab.get(t, vocab[_UNK_TOKEN]) for t in tokens]
    # Pad to max_len
    ids += [vocab[_PAD_TOKEN]] * (max_len - len(ids))
    return torch.tensor(ids[:max_len], dtype=torch.long)


def batch_encode(instructions, vocab=None, device="cuda", max_len=_MAX_SEQ_LEN):
    """批量编码 → (B, max_len)"""
    B = len(instructions)
    ids = torch.zeros(B, max_len, dtype=torch.long)
    for i, text in enumerate(instructions):
        ids[i] = encode_instruction(text, vocab=vocab, max_len=max_len)
    return ids.to(device)


# ——— TextEncoder Module ———


class TextEncoder(nn.Module):
    """Embedding → LSTM → 最后一帧 pooling

    Args:
        vocab_size: 词表大小（从 get_vocab() 获取）
        embed_dim: Embedding 维度（默认 300，与模型 hidden_dim 解耦）
        hidden_dim: LSTM 隐层维度（需要匹配模型的 hidden_dim）
    """

    def __init__(self, vocab_size, embed_dim=300, hidden_dim=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            batch_first=True,
        )

    def forward(self, token_ids):
        """token_ids: (B, L) → (B, hidden_dim)"""
        emb = self.embedding(token_ids)  # (B, L, embed_dim)
        out, _ = self.lstm(emb)  # (B, L, hidden_dim)
        return out[:, -1, :]  # pool 最后一帧


# ——— Test ———
if __name__ == "__main__":
    vocab = get_vocab()
    print(f"Vocab: {len(vocab)} words")

    # Test encode
    ids = encode_instruction("Go down the hallway and turn left at the couch", vocab=vocab)
    print(f"Token IDs: {ids[:15]}... (shape={ids.shape})")
    print(f"Non-PAD tokens: {(ids > 0).sum().item()}")

    # Test batch
    batch = batch_encode(["turn right", "go straight ahead"], vocab=vocab, device="cpu")
    print(f"Batch shape: {batch.shape}")

    # Test encoder
    encoder = TextEncoder(len(vocab))
    out = encoder(batch)
    print(f"Encoder output shape: {out.shape}")  # (2, 256)
    print("All tests passed")
