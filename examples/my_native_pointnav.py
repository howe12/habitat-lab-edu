#!/usr/bin/env python3
"""Native API PointNav 最小演示 — 加载配置、重置环境、前进 5 步并打印距离。

这是 Habitat Native API（非 Gym）的最小例子，用于演示观测字典的结构。
"""
import habitat


def main():
    # (1) 加载 PointNav 测试配置
    config = habitat.get_config("benchmark/nav/pointnav/pointnav_habitat_test.yaml")

    # (2) 创建环境（Native API，非 Gym）
    env = habitat.Env(config)
    try:
        # (3) 重置 — 返回观测字典
        obs = env.reset()

        # (4) 看看观测字典里有什么
        print("观测类型:", list(obs.keys()))

        # (5) 执行几步，观察数据变化
        for step in range(5):
            action = {"action": "move_forward"}  # 前进 0.25m
            obs = env.step(action)
            gps = obs["pointgoal_with_gps_compass"]
            print(f"第{step}步 — 到目标的距离: {gps[0]:.2f}m, 角度: {gps[1]:.2f}rad")
    finally:
        env.close()


if __name__ == "__main__":
    main()
