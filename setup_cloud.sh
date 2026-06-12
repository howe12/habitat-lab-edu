#!/usr/bin/env bash
# ============================================================
# Habitat-Lab 云服务器一键部署脚本
# 适用: 有显示器 (with_bullet) 的 GPU 云服务器
# 用法: bash setup_cloud.sh
# ============================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ENV_NAME="habitat"
PYTHON_VER="3.9"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log()  { echo -e "${GREEN}[OK]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
err()  { echo -e "${RED}[ERR]${NC} $1"; exit 1; }

echo "============================================"
echo " Habitat-Lab 云服务器部署"
echo "============================================"
echo ""

# ── Step 1: 检查前置条件 ──────────────────────────
log "Step 1/6: 检查前置条件..."

if ! command -v conda &>/dev/null; then
    err "未找到 conda，请先安装 Miniconda: https://docs.conda.io/en/latest/miniconda.html"
fi
log "conda: $(conda --version 2>&1 | head -1)"

if ! command -v nvidia-smi &>/dev/null; then
    err "未找到 nvidia-smi，请确认 GPU 驱动已安装"
fi
GPU_COUNT=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null | wc -l)
log "GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null | head -1 | xargs) (共 ${GPU_COUNT} 卡)"

CUDA_VER=$(nvidia-smi | grep -oP "CUDA Version: \K[0-9.]+" 2>/dev/null || echo "未知")
log "CUDA Driver: ${CUDA_VER}"

# ── Step 2: 创建 conda 环境 ──────────────────────────
log "Step 2/6: 创建 conda 环境 '${ENV_NAME}' (Python ${PYTHON_VER})..."

if conda env list | grep -q "^${ENV_NAME} "; then
    warn "环境 '${ENV_NAME}' 已存在，跳过创建"
else
    conda create -n ${ENV_NAME} python=${PYTHON_VER} -y
    log "环境创建完成"
fi

# 激活环境
eval "$(conda shell.bash hook)"
conda activate ${ENV_NAME}

# ── Step 3: 安装 PyTorch ──────────────────────────
log "Step 3/6: 安装 PyTorch (CUDA 12.1)..."

python -c "import torch; print('PyTorch', torch.__version__, '已安装')" 2>/dev/null && {
    log "PyTorch 已安装，跳过"
} || {
    pip install torch==2.5.1 torchvision --index-url https://download.pytorch.org/whl/cu121
    log "PyTorch 安装完成"
}

# ── Step 4: 安装 habitat-sim (with_bullet — 有显示器) ──
log "Step 4/6: 安装 habitat-sim (with_bullet 模式，支持渲染窗口)..."

python -c "import habitat_sim; print('habitat_sim', habitat_sim.__version__, '已安装')" 2>/dev/null && {
    log "habitat-sim 已安装，跳过"
} || {
    conda install habitat-sim-mutex=1.0=with_bullet -c aihabitat -c conda-forge -y
    conda install habitat-sim=0.2.5 -c aihabitat -c conda-forge -y
    log "habitat-sim 安装完成"
}

# ── Step 5: 安装 habitat-lab + baselines ─────────
log "Step 5/6: 安装 habitat-lab + habitat-baselines (从本地源码)..."

pip install -e "${SCRIPT_DIR}/habitat-lab" -q
log "habitat-lab 安装完成"

pip install -e "${SCRIPT_DIR}/habitat-baselines" -q
log "habitat-baselines 安装完成"

# ── Step 6: 创建数据目录结构 ───────────────────────
log "Step 6/6: 创建数据目录结构..."

mkdir -p "${SCRIPT_DIR}/data"/{scene_datasets,datasets,versioned_data,new_checkpoints,tb,tb_eval,video_dir}

# 场景数据集目录
mkdir -p "${SCRIPT_DIR}/data/scene_datasets"/{
    habitat-test-scenes,
    mp3d_example,
    mp3d,
    hm3d,
    gibson,
    replica_cad
}

# 任务数据集目录
mkdir -p "${SCRIPT_DIR}/data/datasets"/{
    pointnav/{gibson/{v1,v2},habitat-test-scenes/v1,mp3d/v1,hm3d/v1},
    objectnav/{mp3d/v1,hm3d/{v1,v2},hssd-hab},
    vln/mp3d/r2r/v1,
    eqa/mp3d/v1,
    instance_imagenav/hm3d/v1,
    rearrange_pick/replica_cad/v0
}

log "数据目录创建完成"

# ── 验证 ──────────────────────────────────────────
echo ""
echo "============================================"
echo " 验证安装"
echo "============================================"

python -c "
import habitat
import habitat_baselines
import habitat_sim
import torch

print(f'habitat-lab:   {habitat.__version__}')
print(f'habitat-sim:   {habitat_sim.__version__}')
print(f'habitat-baselines: 已导入')
print(f'PyTorch:       {torch.__version__}')
print(f'CUDA 可用:     {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'GPU 数量:      {torch.cuda.device_count()}')
    print(f'GPU 名称:      {torch.cuda.get_device_name(0)}')
" || err "导入验证失败，请检查安装日志"

echo ""
echo "============================================"
echo " 部署完成!"
echo "============================================"
echo ""
echo "下一步：上传数据集到以下位置（详见 DATA_PATHS.md）："
echo ""
echo "  场景数据 → data/scene_datasets/<数据集名>/"
echo "  任务数据 → data/datasets/<任务名>/<数据集名>/<版本>/"
echo ""
echo "上传完成后运行验证："
echo "  conda activate ${ENV_NAME}"
echo "  python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path data/"
echo "  python examples/example_pointnav.py"
echo ""
