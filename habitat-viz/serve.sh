#!/usr/bin/env bash
# ============================================================
#  Habitat 学习资源中心 — 局域网静态服务
# ============================================================
#  用法:
#    ./serve.sh              # 自动探测 IP，默认端口 9000
#    ./serve.sh 9090         # 自定义端口
#    ./serve.sh 0.0.0.0 8080 # 显式绑定地址和端口
#
#  按 Ctrl+C 停止服务
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SERVE_DIR="$SCRIPT_DIR"           # 服务根目录 = habitat-viz/
PORT="${1:-9000}"                 # 默认 9000（避开 80/443/3000/5000/8000/8080）

# ── 颜色 ──────────────────────────────────
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

# ── 探测本机局域网 IPv4 ───────────────────
detect_ip() {
    # 优先取非 lo、非 docker、非 virbr 的第一个 IPv4
    ip -4 -o addr show scope global 2>/dev/null \
        | awk '{print $4}' \
        | cut -d/ -f1 \
        | grep -vE '^(172\.(1[7-9]|2[0-9]|3[0-1])|10\.|192\.168\.)' \
        | head -1 \
        || ip -4 -o addr show scope global 2>/dev/null \
            | awk '{print $4}' \
            | cut -d/ -f1 \
            | head -1 \
        || hostname -I 2>/dev/null | awk '{print $1}' \
        || echo "127.0.0.1"
}

IP="$(detect_ip)"

# ── 检查端口是否被占用 ────────────────────
if command -v ss &>/dev/null; then
    if ss -tlnp | grep -q ":$PORT "; then
        echo -e "${YELLOW}⚠ 端口 $PORT 被占用，自动选择下一个可用端口...${NC}"
        PORT=$((PORT + 1))
        while ss -tlnp | grep -q ":$PORT "; do
            PORT=$((PORT + 1))
        done
        echo -e "  使用端口: $PORT"
    fi
fi

# ── 启动服务 ──────────────────────────────
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   Habitat 学习资源中心 — 局域网访问          ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  服务目录: ${CYAN}$SERVE_DIR${NC}"
echo -e "  监听地址: 0.0.0.0:$PORT"
echo ""
echo -e "  ${YELLOW}📱 局域网内其他设备打开以下地址：${NC}"
echo ""
echo -e "     ${CYAN}http://${IP}:${PORT}${NC}"
echo ""
echo -e "  💻 本机也可用:"
echo -e "     ${CYAN}http://localhost:${PORT}${NC}"
echo ""

# 进入服务目录，启动 HTTP Server
cd "$SERVE_DIR"

# Python 3 内置 HTTP 服务器（无需安装任何依赖）
python3 -m http.server "$PORT" --bind 0.0.0.0
