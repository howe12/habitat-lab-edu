"""
VLN Seq2Seq Agent (简化版)。
三预测头：action / progress / stop

§N 避坑实战 — 模型架构修复：
  修复前：instr 是 torch.randn(B, 10, 300) 随机噪声
  修复后：instr_feat 是 TextEncoder 输出 (B, hidden_dim) 真实语义
  变化：删除内部 txt_encoder LSTM，改为接受预编码的文本特征
"""
import torch
import torch.nn as nn
import torchvision.models as tv_models


class Seq2SeqAgent(nn.Module):
    """Seq2Seq Imitation Learning Agent for VLN.

    - RGB encoder: ResNet50 (ImageNet pretrained)
    - Text: 由外部 TextEncoder 预编码，传入 (B, hidden_dim)
    - Action embed: 6 个动作的 embedding (5+1 PAD)
    - Fuser: 2 层 LSTM
    - 三个预测头：action / progress / stop
    """

    def __init__(self, hidden_dim=256, num_actions=5, pretrained=True):
        super().__init__()
        self.hidden_dim = hidden_dim

        # RGB encoder (ResNet50, 去掉最后 fc)
        if pretrained:
            weights = tv_models.ResNet50_Weights.DEFAULT
        else:
            weights = None
        resnet = tv_models.resnet50(weights=weights)
        self.rgb_encoder = nn.Sequential(*list(resnet.children())[:-1])
        rgb_feat_dim = 2048

        # Action embedding
        self.action_embed = nn.Embedding(num_actions + 1, 32)  # +1 for PAD

        # Fuser (2 层 LSTM): RGB + Text + Action
        fusion_dim = rgb_feat_dim + hidden_dim + 32
        self.fuser = nn.LSTM(
            input_size=fusion_dim,
            hidden_size=hidden_dim,
            num_layers=2,
            batch_first=True,
        )

        # 三个预测头
        self.action_head = nn.Linear(hidden_dim, num_actions)
        self.progress_head = nn.Linear(hidden_dim, 1)
        self.stop_head = nn.Linear(hidden_dim, 1)

    def forward(self, rgb_seq, instr_feat, prev_actions):
        """
        Args:
            rgb_seq:   (B, T, 3, H, W) — RGB 序列
            instr_feat: (B, hidden_dim) — TextEncoder 预编码的文本特征
            prev_actions: (B, T) — 历史动作索引

        Returns:
            action_logits: (B, T, num_actions)
            progress_pred: (B, T) — sigmoid 后
            stop_pred:     (B, T) — sigmoid 后
        """
        B, T, C, H, W = rgb_seq.shape

        # 1. RGB 编码
        rgb_flat = rgb_seq.view(B * T, C, H, W)
        rgb_feat = self.rgb_encoder(rgb_flat).view(B, T, -1)  # (B, T, 2048)

        # 2. 文本特征 — 从外部 TextEncoder 传入
        txt_pool = instr_feat.unsqueeze(1).expand(-1, T, -1)  # (B, T, hidden_dim)

        # 3. 动作 embedding
        act_feat = self.action_embed(prev_actions)  # (B, T, 32)

        # 4. 拼接 + LSTM 融合
        fused = torch.cat([rgb_feat, txt_pool, act_feat], dim=-1)  # (B, T, fusion_dim)
        out, _ = self.fuser(fused)  # (B, T, hidden_dim)

        # 5. 三个预测头
        action_logits = self.action_head(out)  # (B, T, num_actions)
        progress_pred = torch.sigmoid(self.progress_head(out).squeeze(-1))  # (B, T)
        stop_pred = torch.sigmoid(self.stop_head(out).squeeze(-1))  # (B, T)

        return action_logits, progress_pred, stop_pred


if __name__ == "__main__":
    model = Seq2SeqAgent(pretrained=False).cuda()
    print(f"参数量: {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M")

    B, T = 2, 5
    rgb_seq = torch.randn(B, T, 3, 256, 256).cuda()
    instr_feat = torch.randn(B, 256).cuda()  # TextEncoder output
    prev_actions = torch.zeros(B, T, dtype=torch.long).cuda()

    action_logits, prog, stop = model(rgb_seq, instr_feat, prev_actions)
    print(f"action_logits: {action_logits.shape}")
    print(f"progress_pred: {prog.shape}")
    print(f"stop_pred: {stop.shape}")
    print("forward OK")
