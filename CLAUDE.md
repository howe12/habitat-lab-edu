# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Habitat-Lab is a modular high-level library for embodied AI — defining tasks (navigation, rearrangement, instruction following, question answering), configuring agents (sensors, robots), training agents (RL/imitation/SensePlanAct), and benchmarking performance. It uses **Habitat-Sim** as the physics/rendering simulator.

The repo has two installable packages:
- `habitat-lab/` — core library (`habitat` package)
- `habitat-baselines/` — training baselines (`habitat_baselines` package, optional install)

## Essential Commands

```bash
# Development install
pip install -e habitat-lab
pip install -e habitat-baselines  # optional, for training

# Run all tests
python -m pytest

# Run a single test file
python -m pytest test/test_habitat_env.py

# Run a specific test
python -m pytest test/test_habitat_env.py -k test_name

# Lint / type-check
black habitat-lab/. habitat-baselines/. examples/. test/. --diff
isort habitat-lab/. habitat-baselines/. examples/. test/. --diff
mypy

# Run pre-commit on all files
pre-commit run --all-files

# Training (from repo root)
python -u -m habitat_baselines.run --config-name=pointnav/ppo_pointnav_example.yaml

# Evaluation
python -u -m habitat_baselines.run --config-name=pointnav/ppo_pointnav_example.yaml habitat_baselines.evaluate=True

# Demo example (PointNav, works offline with local test data)
python examples/example_pointnav.py

# Debugging vectorized env issues
export HABITAT_ENV_DEBUG=1  # uses slower ThreadedVectorEnv instead of VectorEnv
```

## Architecture

### Core Abstractions (`habitat-lab/habitat/core/`)

`Env` ties together three components: a **Dataset** (episodes), a **Simulator** (Habitat-Sim), and an **EmbodiedTask**.

- `env.py` — `Env` (base) and `RLEnv` (adds reward). `Env.reset()` returns observations dict; `Env.step(action)` advances one step.
- `embodied_task.py` — `EmbodiedTask`, `Action` (agent behaviors), `Measure` (metrics like distance-to-goal, SPL, success).
- `simulator.py` — `Simulator` interface, `Sensor` and `SensorSuite` abstractions.
- `dataset.py` — `Dataset` (container of `Episode`s), `Episode` (start state + goal in a scene).
- `vector_env.py` — `VectorEnv` (multiprocessing-based parallel envs). Default for training.
- `registry.py` — Global `Registry` singleton. Everything is registered via decorators: `@registry.register_task`, `@registry.register_sensor`, `@registry.register_measure`, `@registry.register_simulator`, `@registry.register_dataset`, `@registry.register_task_action`.

### Configuration System (`habitat-lab/habitat/config/`)

Uses **Hydra/OmegaConf** with Structured Configs (dataclasses) as schema. Key files:
- `default_structured_configs.py` — all Structured Config definitions and `HabitatConfigPlugin` (Hydra SearchPathPlugin).
- `default.py` — `get_config()` creates configs via Hydra Compose API, `read_write()` context manager enables mutating frozen OmegaConf nodes.

Config directory structure:
```
config/
  benchmark/          # primary configs fed to habitat.get_config()
    nav/              # PointNav, ObjectNav, InstanceImageNav
    rearrange/        # Pick, Place, Open/Close drawer/fridge, etc.
  habitat/            # config group options (composed into benchmarks)
    dataset/          # dataset configs (gibson, mp3d, replica_cad)
    simulator/        # sim + agent sensor configs
    task/             # task-specific configs
```

**Changing a config value from CLI:** `python -m habitat_baselines.run ... habitat.task.measurements.success.success_distance=0.2`

### Tasks (`habitat-lab/habitat/tasks/`)

- `nav/` — PointNav (`nav.py`), ObjectNav (`object_nav_task.py`), InstanceImageNav (`instance_image_nav_task.py`), shortest_path_follower
- `rearrange/` — Mobile manipulation tasks (pick, place, open/close drawer/fridge, composite PDDL tasks) + articulated agent management
- `eqa/` — Embodied Question Answering
- `vln/` — Vision-and-Language Navigation

### Datasets (`habitat-lab/habitat/datasets/`)

Each task has a corresponding dataset class registered via `@registry.register_dataset`. Datasets provide episodes (start position, goal, scene ID).

### Simulators (`habitat-lab/habitat/sims/`)

- `habitat_simulator/` — Primary backend wrapping Habitat-Sim. Contains `HabitatSim` class, sensor/action implementations.
- `pyrobot/` — Alternative backend for real robots.

### Gym Interface (`habitat-lab/habitat/gym/`)

`gym_definitions.py` registers Gym environments: `Habitat-v0`, `HabitatRender-v0`, plus task-specific ones like `HabitatPick-v0`, `HabitatPlace-v0`, etc. Import `habitat.gym` to register them, then use `gym.make()`.

### Baselines (`habitat-baselines/habitat_baselines/`)

- `run.py` — Main entry point (Hydra-based). Uses `--config-name=<path>` for config selection.
- `rl/ppo/` — PPO trainer, policy (CNN+RNN), updater
- `rl/ddppo/` — Distributed PPO (multi-GPU)
- `rl/hrl/` — Hierarchical RL (high-level policy + low-level skills)
- `rl/ver/` — VER (faster alternative trainer)
- `common/` — `RolloutStorage`, `baseline_registry` (extends core registry with trainer), `env_factory`, `obs_transformers`, `tensor_dict`

Config overrides at CLI use Hydra syntax: `habitat_baselines.trainer_name=ddppo`, `habitat_baselines.num_updates=100`, etc.

## Key Patterns

1. **Two Env APIs**: Native `habitat.Env(config)` for direct use; Gym `gym.make("Habitat-v0", cfg_file_path=...)` for standard RL workflows.
2. **Registry-driven**: Adding a new task/sensor/measure means (a) subclass the base, (b) decorate with `@registry.register_*`, (c) provide a config YAML/Structured Config.
3. **Config via Hydra**: All knobs (task type, dataset, simulator, agent sensors, reward measures) go through Hydra config composition. Use `read_write(config)` to mutate frozen configs.
4. **Observations are dicts**: `env.reset()` and `env.step()` return `Dict[str, np.ndarray]` with keys like `rgb`, `depth`, `pointgoal_with_gps_compass`, etc.
5. **Actions are dicts**: `env.step({"action": "move_forward"})` or `env.step({"action": "arm_action", "arm_action": <numpy_array>})` for rearrangement tasks.

## HTML Course Writing Standards (`habitat-viz/`)

The `habitat-viz/` directory contains a Chinese-language HTML textbook ("从零理解 Habitat"). Every code example within a chapter MUST follow the **six-section format** established in `habitat-textbook-step2.html`. Each example is a self-contained block with numbered sections (①–⑥), using the CSS classes already defined in the existing pages (`info-box`, `code-block`, `compare-table`, `tip-box`, `warn-box`).

### Six-Section Template

For every case/example in a chapter page:

```
① 案例含义 — What does this case do? (info-box)
    - One-sentence purpose + why it's worth learning
    - What task/dataset/API is demonstrated
    - Prerequisites or dependencies (e.g., "works offline", "needs GPU")

② 核心代码 & 关键函数调用 — Code + function call table
    - Complete runnable code in a code-block with syntax highlighting spans
    - A compare-table listing each key function: name, role, explanation
    - Optional: a flow-box diagram showing the execution sequence

③ 如何创建和运行 — How to create and run (bash code-block)
    - Exact terminal commands with $ prompt prefix
    - Expected console output
    - Common startup errors and their fixes (warn-box)

④ 运行效果 — What the output looks like
    - Actual screenshots from real runs (images/ directory)
    - Actual terminal output logs (verbatim, not fabricated)
    - Side-by-side comparisons when showing different actions/params

⑤ 输出结果的含义 — What the output means (info-box, numbered list)
    - Line-by-line or field-by-field interpretation
    - Connect numbers back to physical meaning (distance, angle, reward, etc.)
    - Explain WHY a result looks the way it does, not just WHAT it shows

⑥ 试试调整这些 — Tunable parameters (compare-table)
    - Columns: 调整项 | 怎么改 | 预期看到什么
    - Concrete code changes, not vague suggestions
    - What the reader should observe after each change
```

### Additional Chapter-Wide Elements

- **Overview table** at the top of the chapter listing all cases with difficulty ratings (⭐–⭐⭐⭐)
- **Checklist** with interactive checkboxes for progress tracking
- **Progress bar** tied to the checklist
- **学后自检** (self-check Q&A) at the end of the chapter
- **Page nav** with prev/next links to adjacent chapters

### CSS Variables (reuse, don't redefine)

All pages share the same `:root` variables: `--bg: #0f172a`, `--card-bg: #1e293b`, `--border: #334155`, `--text: #e2e8f0`, `--text-dim: #94a3b8`, plus accent colors for core/task/data/RL/sim/config/tip/warn. Do not invent new color schemes per page — copy the `<style>` block from an existing step page.

## Code Style

- **Black** with `line_length=79`, **isort**, **flake8**, **mypy** (strict mode off)
- Pre-commit hooks manage all formatting (see `.pre-commit-config.yaml`)
- Python 3.9+ required
- MIT license, Meta/Facebook copyright headers on source files
