#!/usr/bin/env python3
"""PointNav gym example — no network download needed (uses local habitat-test dataset).

Note: Uses cv2.imshow for visualization to avoid GLX context issues with
env.render(mode="human"). To re-enable native GUI rendering, add +iglx to Xorg:
  sudo mkdir -p /etc/X11/xorg.conf.d
  echo 'Section "ServerFlags"\n    Option "IndirectGLX" "on"\nEndSection' \
    | sudo tee /etc/X11/xorg.conf.d/20-iglx.conf
Then reboot.
"""
import cv2
import gym
import habitat.gym  # noqa: F401 — registers Habitat-v0


def example():
    print("Creating Habitat PointNav environment...")
    env = gym.make(
        "Habitat-v0",
        cfg_file_path="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
    )

    print("Environment creation successful")
    observations = env.reset()
    print(f"  Observation keys: {list(observations.keys())}")
    print(f"  RGB shape: {observations['rgb'].shape}")
    print(f"  Depth shape: {observations['depth'].shape}")

    # Render to numpy array, then display with OpenCV (avoids GLX issues)
    frame = env.render(mode="rgb_array")
    window_name = "Habitat PointNav (press Q or close window to exit)"
    cv2.imshow(window_name, frame[..., ::-1])  # RGB -> BGR for OpenCV

    print("Agent acting inside environment (random actions).")
    print("  Viewer window opened — close it or press Q to exit.")
    count_steps = 0
    group_size = 10
    group_count = 0
    while True:
        group_count += 1
        print(f"\n  === Group {group_count}: {group_size} random actions ===")
        for i in range(group_size):
            action = env.action_space.sample()
            observations, reward, done, info = env.step(action)
            count_steps += 1

            frame = env.render(mode="rgb_array")
            cv2.imshow(window_name, frame[..., ::-1])  # RGB -> BGR

            # Check for keypress — exit on 'q' or window close
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                raise KeyboardInterrupt

            if done:
                print(f"Episode finished after {count_steps} steps. Metrics: {info}")
                observations = env.reset()
                count_steps = 0
        print(f"  Group {group_count} done. Waiting 1 second...")
        import time

        time.sleep(1.0)


if __name__ == "__main__":
    try:
        example()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        cv2.destroyAllWindows()
        print("Closing environment...")
