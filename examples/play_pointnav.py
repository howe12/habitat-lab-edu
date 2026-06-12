#!/usr/bin/env python3
"""Native API PointNav — WASD 交互控制 + 实时画面显示。

   W → move_forward    A → turn_left    D → turn_right
   S → stop            Q → 退出

运行时窗口不会一闪而过——会一直显示直到你按 Q 退出。
和 example_pointnav.py 一样使用 rgb_array 方式，不会触发 GLX 错误。
"""
import cv2
import numpy as np
import habitat


def make_display_frame(obs):
    """拼接 RGB（左）+ 深度可视化（右），匹配 env.render('rgb_array') 的 256×512 输出。"""
    rgb = obs["rgb"].copy()  # (256, 256, 3) uint8

    # 深度归一化并灰度化 (256, 256) → 转 3 通道以便拼接
    depth = obs["depth"].squeeze().copy()  # (256, 256) float32

    # 防止全零或 NaN 导致除零
    dmin, dmax = depth.min(), depth.max()
    if dmax - dmin < 1e-6:
        depth_norm = np.zeros_like(depth)
    else:
        depth_norm = (depth - dmin) / (dmax - dmin)
    depth_norm = np.nan_to_num(depth_norm, nan=0.0, posinf=1.0, neginf=0.0)

    depth_gray = (depth_norm * 255).astype(np.uint8)
    depth_vis = cv2.cvtColor(depth_gray, cv2.COLOR_GRAY2BGR)

    return np.hstack([rgb, depth_vis])  # → (256, 512, 3)


def show_frame(win_name, obs):
    """显示画面并立即刷新窗口事件循环。"""
    frame = make_display_frame(obs)
    # RGB → BGR for OpenCV
    cv2.imshow(win_name, frame[..., ::-1])
    # 必须调用 waitKey 才能让 OpenCV 渲染窗口内容
    cv2.waitKey(1)


def play():
    """主循环：用 WASD 交互控制 Agent，Q 退出。"""
    config = habitat.get_config(
        "benchmark/nav/pointnav/pointnav_habitat_test.yaml"
    )
    env = habitat.Env(config)
    try:
        obs = env.reset()

        WIN = "Native API PointNav — WASD 控制, Q 退出  [左=RGB  右=深度]"
        print("=" * 55)
        print("  控制键: W=前进  A=左转  D=右转  S=停止  Q=退出")
        print("  画面: 左半 = RGB  |  右半 = 深度图 (depth)")
        print("=" * 55)

        gps = obs["pointgoal_with_gps_compass"]
        print(f"初始状态 — 到目标距离: {gps[0]:.2f}m,  角度: {gps[1]:.2f}rad")

        # 创建窗口并显示第一帧
        cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
        show_frame(WIN, obs)

        step = 0
        action = None
        while True:
            key = cv2.waitKey(100) & 0xFF

            if key == ord("q"):
                break
            elif key == ord("w") or key == ord("W"):
                action = {"action": "move_forward"}
            elif key == ord("a") or key == ord("A"):
                action = {"action": "turn_left"}
            elif key == ord("d") or key == ord("D"):
                action = {"action": "turn_right"}
            elif key == ord("s") or key == ord("S"):
                action = {"action": "stop"}
            elif key != 255:  # 忽略无按键事件 (cv2.waitKey 在无按键时返回 255)
                print(f"  未知按键: {key}, 请用 W/A/D/S/Q")

            if action is not None:
                obs = env.step(action)
                step += 1
                gps = obs["pointgoal_with_gps_compass"]
                done = env.episode_over
                status = " (episode 结束!)" if done else ""
                print(
                    f"  Step {step:2d}: {action['action']:>14s}"
                    f"  dist={gps[0]:.2f}m  angle={gps[1]:.2f}rad{status}"
                )
                show_frame(WIN, obs)

                if done:
                    print(f"\nEpisode 结束!\nMetrics: {env.get_metrics()}")
                    print("按 R 重新开始, 或按 Q 退出...")
                    # 等待用户决定
                    while True:
                        k = cv2.waitKey(100) & 0xFF
                        if k == ord("r") or k == ord("R"):
                            obs = env.reset()
                            step = 0
                            gps = obs["pointgoal_with_gps_compass"]
                            print(f"\n新 episode — 到目标距离: {gps[0]:.2f}m")
                            show_frame(WIN, obs)
                            break
                        elif k == ord("q") or k == ord("Q"):
                            action = "quit"  # 触发外层退出
                            break
                    if action == "quit":
                        break

                action = None
    finally:
        env.close()
        cv2.destroyAllWindows()
        print("Done — 窗口已关闭")


if __name__ == "__main__":
    play()
