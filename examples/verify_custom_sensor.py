#!/usr/bin/env python3
"""验证自定义传感器和指标是否注册成功。
运行方式:  python examples/verify_custom_sensor.py
"""
from dataclasses import dataclass
from typing import Any

import numpy as np
from gym import spaces
from omegaconf import MISSING

import habitat
from habitat.config.default_structured_configs import LabSensorConfig, MeasurementConfig


# ── 自定义 Measure ────────────────────────────
@habitat.registry.register_measure
class EpisodeInfoExample(habitat.Measure):
    def __init__(self, sim, config, **kwargs: Any):
        self._config = config
        super().__init__()

    def _get_uuid(self, *args: Any, **kwargs: Any) -> str:
        return "episode_info"

    def reset_metric(self, *args: Any, episode, **kwargs: Any):
        self._metric = vars(episode).copy()
        self._metric["my_value"] = self._config.VALUE

    def update_metric(self, *args: Any, episode, action, **kwargs: Any):
        self._metric = vars(episode).copy()


@dataclass
class EpisodeInfoExampleConfig(MeasurementConfig):
    type: str = "EpisodeInfoExample"
    VALUE: int = -1


# ── 自定义 Sensor ─────────────────────────────
@habitat.registry.register_sensor(name="my_supercool_sensor")
class AgentPositionSensor(habitat.Sensor):
    def __init__(self, sim, config, **kwargs: Any):
        super().__init__(config=config)
        self._sim = sim
        print("[INIT]  传感器接收到的配置: answer_to_life =", self.config.answer_to_life)

    def _get_uuid(self, *args: Any, **kwargs: Any) -> str:
        return "agent_position"

    def _get_sensor_type(self, *args: Any, **kwargs: Any):
        return habitat.SensorTypes.POSITION

    def _get_observation_space(self, *args: Any, **kwargs: Any):
        return spaces.Box(
            low=np.finfo(np.float32).min,
            high=np.finfo(np.float32).max,
            shape=(3,),
            dtype=np.float32,
        )

    def get_observation(self, observations, *args: Any, episode, **kwargs: Any):
        return self._sim.get_agent_state().position


@dataclass
class AgentPositionSensorConfig(LabSensorConfig):
    type: str = "my_supercool_sensor"
    answer_to_life: int = MISSING


def print_section(title):
    print()
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)


def main():
    config = habitat.get_config(
        config_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml"
    )
    with habitat.config.read_write(config):
        my_value = 5
        config.habitat.task.measurements["episode_info_example"] = (
            EpisodeInfoExampleConfig(VALUE=my_value)
        )
        config.habitat.task.lab_sensors["agent_position_sensor"] = (
            AgentPositionSensorConfig(answer_to_life=42)
        )

    with habitat.Env(config=config) as env:
        # ── 验证点 0: Env 创建成功 ──
        print_section("验证 0: 环境创建成功")
        print("[PASS] habitat.Env(config=config) 正常返回，无异常")

        # ── 验证点 1: reset 后自定义传感器出现在 obs 中 ──
        print_section("验证 1: reset() 后自定义传感器 agent_position 出现在 obs 中")
        obs = env.reset()
        builtin_keys = [k for k in obs.keys() if k != "agent_position"]
        print(f"  内置传感器:     {builtin_keys}")
        print(f"  自定义传感器:   agent_position = {obs['agent_position']}")
        if "agent_position" not in obs:
            raise AssertionError("FAIL: agent_position 不在 obs 中!")
        print("  [PASS] agent_position 已被注册并返回 Agent 的 3D 坐标")

        # ── 验证点 2: reset 后自定义指标包含 my_value ──
        print_section("验证 2: reset() 后 episode_info 包含 my_value=5")
        metrics = env.get_metrics()
        ep_info = metrics["episode_info"]
        print(f"  episode_id:    {ep_info['episode_id']}")
        print(f"  start_position:{ep_info['start_position']}")
        print(f"  goals[0].pos:  {ep_info['goals'][0].position}")
        print(f"  my_value:      {ep_info['my_value']}  ← reset_metric() 写入")
        if ep_info["my_value"] != my_value:
            raise AssertionError(f"FAIL: my_value != {my_value}!")
        print("  [PASS] reset_metric() 被调用，my_value == 5")

        # ── 验证点 3: step 后坐标改变 ──
        print_section("验证 3: step('move_forward') 后 agent_position 发生变化")
        pos_before = obs["agent_position"].copy()
        obs = env.step("move_forward")
        pos_after = obs["agent_position"]
        distance = np.linalg.norm(pos_after - pos_before)
        print(f"  step 前坐标:      {pos_before}")
        print(f"  step 后坐标:      {pos_after}")
        print(f"  移动距离:         {distance:.3f}m  (forward_step_size=0.25m)")
        if distance <= 0.01:
            raise AssertionError("FAIL: Agent 似乎没有移动!")
        print("  [PASS] 自定义传感器正确跟踪了 Agent 位置变化")

        # ── 验证点 4: step 后 my_value 消失 ──
        print_section("验证 4: step() 后 my_value 从 episode_info 中消失")
        metrics = env.get_metrics()
        ep_info = metrics["episode_info"]
        has_my_value = "my_value" in ep_info
        print(f"  'my_value' in episode_info: {has_my_value}")
        print(f"  episode_info keys:          {list(ep_info.keys())[:5]}...")
        if has_my_value:
            raise AssertionError("FAIL: my_value 仍然存在!")
        print("  [PASS] update_metric() 不写入 my_value，只在 reset_metric() 出现")

        # ── 总结 ──
        print_section("总结: 5 项验证全部通过")
        print("  ✅ 自定义 Sensor 已注册并出现在 obs 中")
        print("  ✅ 传感器正确返回 Agent 3D 坐标")
        print("  ✅ 传感器正确跟踪 step() 后的坐标变化")
        print("  ✅ 自定义 Measure 已注册并出现在 metrics 中")
        print("  ✅ reset_metric / update_metric 生命周期正确")


if __name__ == "__main__":
    main()
