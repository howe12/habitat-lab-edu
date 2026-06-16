"""
VLN 评估指标：SR, SPL, nDTW

§N 避坑实战 — 评估指标模块
  修复：SPL 公式加上 success 因子
  修复前：spl = gt / max(agent, gt)  → 失败时 SPL 仍可能非零
  修复后：spl = success * gt / max(agent, gt)  → 失败强制为 0
"""
import numpy as np


def success_metric(agent_path, gt_end, threshold=3.0):
    """成功率：agent 最后位置离 GT 终点 < threshold 米"""
    if not agent_path:
        return 0.0
    final = np.array(agent_path[-1])
    gt = np.array(gt_end)
    dist = np.linalg.norm(final - gt)
    return 1.0 if dist < threshold else 0.0


def spl(success, agent_path_len_meters, gt_path_len_meters):
    """§N 避坑实战 — SPL 公式修复
    
    修复前：只返回 gt/agent 比率，缺少 success 因子
      → 失败时 SPL 仍可能是非零值（公式错误）
    
    修复后：success * gt / max(agent, gt)
      → 失败时 SPL 强制为 0

    Args:
        success: bool or float (1.0 or 0.0)
        agent_path_len_meters: agent 实际走过的路径长度（米）
        gt_path_len_meters: GT 最短路径长度（米）
    """
    if not success:
        return 0.0
    if gt_path_len_meters <= 0:
        return 1.0 if success else 0.0
    return success * gt_path_len_meters / max(agent_path_len_meters, gt_path_len_meters)


def _dtw_distance(seq1, seq2):
    """经典 DTW 距离算法"""
    n, m = len(seq1), len(seq2)
    dp = np.full((n + 1, m + 1), np.inf)
    dp[0, 0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = np.linalg.norm(seq1[i - 1] - seq2[j - 1])
            dp[i, j] = cost + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])
    return dp[n, m]


def ndtw(agent_trajectory, gt_trajectory, threshold=3.0):
    """nDTW: normalized Dynamic Time Warping"""
    if not agent_trajectory or not gt_trajectory:
        return 0.0
    agent = np.array(agent_trajectory, dtype=float)
    gt = np.array(gt_trajectory, dtype=float)
    dtw_dist = _dtw_distance(agent, gt)
    ndtw_score = np.exp(-dtw_dist / threshold)
    return float(ndtw_score)


def evaluate_episode(agent_trajectory, gt_trajectory, threshold=3.0):
    """评估单个 episode，返回 (SR, SPL, nDTW)"""
    if not gt_trajectory:
        return 0.0, 0.0, 0.0
    sr = success_metric(agent_trajectory, gt_trajectory[-1], threshold)
    agent_len = sum(
        np.linalg.norm(np.array(agent_trajectory[i+1]) - np.array(agent_trajectory[i]))
        for i in range(len(agent_trajectory) - 1)
    ) if len(agent_trajectory) > 1 else 0.0
    gt_len = sum(
        np.linalg.norm(np.array(gt_trajectory[i+1]) - np.array(gt_trajectory[i]))
        for i in range(len(gt_trajectory) - 1)
    ) if len(gt_trajectory) > 1 else 0.0
    spl_score = spl(sr, agent_len, gt_len)
    ndtw_score = ndtw(agent_trajectory, gt_trajectory, threshold)
    return sr, spl_score, ndtw_score


def aggregate_metrics(results):
    """汇总多个 episode 的指标"""
    if not results:
        return {"SR": 0.0, "SPL": 0.0, "nDTW": 0.0}
    sr = np.mean([r[0] for r in results])
    spl_ = np.mean([r[1] for r in results])
    ndtw_ = np.mean([r[2] for r in results])
    return {"SR": sr, "SPL": spl_, "nDTW": ndtw_}


if __name__ == "__main__":
    # 测试
    gt_path = [(0, 0), (1, 0), (2, 0), (3, 0)]

    # Test 1: 完美走
    agent_path = [(0, 0), (1, 0), (2, 0), (3.0, 0)]
    sr, spl_, ndtw_ = evaluate_episode(agent_path, gt_path)
    print(f"Test 1 (perfect): SR={sr:.2f} SPL={spl_:.2f} nDTW={ndtw_:.3f}")

    # Test 2: 偏离但到终点
    agent_path = [(0, 0), (0.5, 1.5), (2, 1.5), (3.0, 0)]
    sr, spl_, ndtw_ = evaluate_episode(agent_path, gt_path)
    print(f"Test 2 (detour): SR={sr:.2f} SPL={spl_:.2f} nDTW={ndtw_:.3f}")

    # Test 3: 没到终点 → SPL 必须为 0
    agent_path = [(0, 0), (0.5, 0)]
    sr, spl_, ndtw_ = evaluate_episode(agent_path, gt_path)
    print(f"Test 3 (failed): SR={sr:.2f} SPL={spl_:.2f} nDTW={ndtw_:.3f}")
    assert spl_ == 0.0, f"SPL should be 0 on failure, got {spl_}"

    print("All tests passed")
