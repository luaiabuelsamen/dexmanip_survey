# mujoco_playground_2025

source: https://github.com/google-deepmind/mujoco_playground


commit: 4057c147714b6ac09b395377f1a1724bbeacc4d3


## README

# MuJoCo Playground

[![Build](https://img.shields.io/github/actions/workflow/status/google-deepmind/mujoco_playground/ci.yml?branch=main)](https://github.com/google-deepmind/mujoco_playground/actions)
[![PyPI version](https://img.shields.io/pypi/v/playground)](https://pypi.org/project/playground/)
![Banner for playground](https://github.com/google-deepmind/mujoco_playground/blob/main/assets/banner.png?raw=true)

A comprehensive suite of GPU-accelerated environments for robot learning research and sim-to-real, built with [MuJoCo MJX](https://github.com/google-deepmind/mujoco/tree/main/mjx).

Features include:

- Classic control environments from `dm_control`.
- Quadruped and bipedal locomotion environments.
- Non-prehensile and dexterous manipulation environments.
- Vision-based support available via the [MJWarp Batch Renderer](https://mujoco.readthedocs.io/en/stable/mjwarp/index.html#batch-rendering).

For more details, check out the project [website](https://playground.mujoco.org/).

> [!NOTE]
> We now support training with both the MuJoCo MJX JAX implementation, as well as the [MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp) implementation at HEAD. See this [discussion post](https://github.com/google-deepmind/mujoco_playground/discussions/197) for more details.

## Installation

You can install MuJoCo Playground directly from PyPI:

```sh
pip install playground
```

> [!IMPORTANT]
> We recommend users to install [from source](#from-source) to get the latest features and bug fixes from MuJoCo.

### <a id="from-source">From Source</a>

> [!IMPORTANT]
> Requires Python 3.10 or later.

1. `git clone git@github.com:google-deepmind/mujoco_playground.git && cd mujoco_playground`
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/), a faster alternative to `pip`
3. Create a virtual environment: `uv venv --python 3.12`
4. Activate it: `source .venv/bin/activate`
5. Install CUDA 12 jax: `uv pip install -U "jax[cuda12]" --index-url https://pypi.org/simple`
    * Verify GPU backend: `python -c "import jax; print(jax.default_backend())"` should print gpu. `unset LD_LIBRARY_PATH` may need to be run before running this command.
6. Install playground from source: `uv --no-config sync --all-extras`
7. Verify installation: `uv --no-config run python -c "import mujoco_playground; print('Success')"`
    * **Note**: Menagerie assets will be downloaded automatically the first time you load a locomotion or manipulation environment. You can trigger this with: `uv --no-config run python -c "from mujoco_playground import locomotion; locomotion.load('G1JoystickFlatTerrain')"`

## Getting started

### Running from CLI
For basic usage, navigate to the repo's directory, install [from source](#from-source) with `jax[cuda12]`, and run:

```bash
train-jax-ppo --env_name CartpoleBalance
```

To train with [MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp):

```bash
train-jax-ppo --env_name CartpoleBalance --impl warp
```

Or with `uv`:

```bash
uv --no-config run train-jax-ppo --env_name CartpoleBalance --impl warp
uv --no-config run train-rsl-ppo --env_name CartpoleBalance --impl warp
```

### Basic Tutorials
| Colab | Description |
|-------|-------------|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco_playground/blob/main/learning/notebooks/dm_control_suite.ipynb) | Introduction to the Playground with DM Control Suite |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco_playground/blob/main/learning/notebooks/locomotion.ipynb) | Locomotion Environments |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco_playground/blob/main/learning/notebooks/manipulation.ipynb) | Manipulation Environments |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco_playground/blob/main/learning/notebooks/vision.ipynb) | Vision Environments |

### Training Visualization

To interactively view trajectories throughout training with [rscope](https://github.com/Andrew-Luo1/rscope/tree/main), install it (`pip install rscope`) and run:

```
python learning/train_jax_ppo.py --env_name PandaPickCube --rscope_envs 16 --run_evals=False --deterministic_rscope=True
# In a separate terminal
python -m rscope
```

## FAQ

### How can I contribute?

Get started by installing the library and exploring its features! Found a bug? Report it in the issue tracker. Interested in contributing? If you are a developer with robotics experience, we would love your help—check out the [contribution guidelines](CONTRIBUTING.md) for more details.

### Reproducibility / GPU Precision Issues

Users with NVIDIA Ampere architecture GPUs (e.g., RTX 30 and 40 series) may experience reproducibility [issues](https://github.com/google-deepmind/mujoco_playground/issues/86) in mujoco_playground due to JAX’s default use of TF32 for matrix multiplications. This lower precision can adversely affect RL training stability. To ensure consistent behavior with systems using full float32 precision (as on Turing GPUs), please run `export JAX_DEFAULT_MATMUL_PRECISION=highest` in your terminal before starting your experiments (or add it to the end of `~/.bashrc`).

To reproduce results using the same exact learning script as used in the paper, run the brax training script which is available [here](https://github.com/google/brax/blob/1ed3be220c9fdc9ef17c5cf80b1fa6ddc4fb34fa/brax/training/learner.py#L1). There are slight differences in results when using the `learning/train_jax_ppo.py` script, see the issue [here](https://github.com/google-deepmind/mujoco_playground/issues/171) for more context.

## Citation

If you use Playground in your scientific works, please cite it as follows:

```bibtex
@misc{mujoco_playground_2025,
  title = {MuJoCo Playground: An open-source framework for GPU-accelerated robot learning and sim-to-real transfer.},
  author = {Zakka, Kevin and Tabanpour, Baruch and Liao, Qiayuan and Haiderbhai, Mustafa and Holt, Samuel and Luo, Jing Yuan and Allshire, Arthur and Frey, Erik and Sreenath, Koushil and Kahrs, Lueder A. and Sferrazza, Carlo and Tassa, Yuval and Abbeel, Pieter},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/google-deepmind/mujoco_playground}
}
```

## License and Disclaimer

The texture used in the rough terrain for the locomotion environments is from [Polyhaven](https://polyhaven.com/a/rock_face) and licensed under [CC0](https://creativecommons.org/public-domain/cc0/).

All other content in this repository is licensed under the Apache License, Version 2.0. A copy of this license is provided in the top-level [LICENSE](LICENSE) file in this repository. You can also obtain it from https://www.apache.org/licenses/LICENSE-2.0.

This is not an officially supported Google product.


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    ci.yml
    pypi.yml
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
learning/
  README.md
  __init__.py
  notebooks/
    dm_control_suite.ipynb
    locomotion.ipynb
    manipulation.ipynb
    vision.ipynb
  train_jax_ppo.py
  train_rsl_rl.py
mujoco_playground/
  __init__.py
  _src/
    __init__.py
    dm_control_suite/
    gait.py
    locomotion/
    manipulation/
    mjx_env.py
    registry.py
    registry_test.py
    reward.py
    wrapper.py
    wrapper_test.py
    wrapper_torch.py
  config/
    README.md
    __init__.py
    dm_control_suite_params.py
    locomotion_params.py
    manipulation_params.py
  experimental/
    brax_network_to_onnx.ipynb
    learning/
    madrona_benchmarking/
    sim2sim/
    utils/
  py.typed
pylintrc
pyproject.toml
uv.lock
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
default_stages: [pre-commit]
exclude: '.*__init__\.py$'

# Install
# 1. pip install -e .
# 2. pre-commit install
# 3. pre-commit run --all-files  # make sure all files are clean
repos:
  - repo: https://github.com/google/pyink
    rev: 24.10.0
    hooks:
      - id: pyink
        name: Pyink (Formatting)
        # pyink will automatically read configuration from pyproject.toml

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: Isort (Import Sorting)
        # isort will automatically read configuration from pyproject.toml

  - repo: local
    hooks:
      - id: check-copyright
        name: Check Copyright Notice
        entry: python3 -c "import sys, re; pattern = re.compile(r'Copyright \d{4} Google LLC'); bad = [f for f in sys.argv[1:] if not pattern.search(open(f, errors='ignore').read())]; sys.exit('\n'.join(['Files missing Copyright notice:'] + bad)) if bad else None"
        language: system
        types_or: [python, c, c++, cuda]

  # - repo: local
  #   hooks:
  #     - id: pylint
  #       name: Pylint (Google Style)
  #       entry: pylint
  #       args: ['--rcfile=pylintrc']
  #       language: system
  #       types: [python]

  # - repo: local # re-using locally installed libraries
  #   hooks:
  #     - id: pytype
  #       name: Pytype (Type Checking)
  #       entry: pytype
  #       language: system
  #       types: [python]
  #       always_run: true

  # - repo: local
  #   hooks:
  #     - id: pytest
  #       name: Run Pytest
  #       entry: pytest
  #       language: system
  #       pass_filenames: false
  #       always_run: true
  #       args: ["-n", "auto"]  # Execute tests in parallel
  #       verbose: true

```

## Python signatures and reward/observation bodies (26 files)


### learning/train_jax_ppo.py

```
"""Train a PPO agent using JAX on the specified environment."""
def get_rl_config(env_name)
def rscope_fn(full_states, obs, rew, done)
def main(argv)
def run()
```

### learning/train_rsl_rl.py

```
"""Train a PPO agent using RSL-RL for the specified environment."""
def get_rl_config(env_name)
def main(argv)
def run()
```

### mujoco_playground/_src/locomotion/go1/handstand.py

```
"""Handstand task for Go1."""
def default_config()
class Handstand(Go1Env)
    """Handstand task for Go1."""
    def __init__(self, config, config_overrides)
    def _post_init(self)
    def reset(self, rng)
    def step(self, state, action)
    def _get_termination(self, data, info, contact)
    def _get_obs(self, data, info, contact)
    def _get_reward(self, data, action, info, done)
    def _cost_stay_still(self, qvel)
    def _reward_orientation(self, forward_vec, up_vec)
    def _reward_height(self, torso_height)
    def _cost_contact(self, data)
    def _cost_pose(self, qpos)
    def _cost_torques(self, torques)
    def _cost_energy(self, qvel, qfrc_actuator)
    def _cost_action_rate(self, act, info)
    def _cost_joint_pos_limits(self, qpos)
    def _cost_dof_acc(self, qacc)
class Footstand(Handstand)
    """Footstand task for Go1."""
    def _post_init(self)

```python
def _get_obs(
      self, data: mjx.Data, info: dict[str, Any], contact: jax.Array
  ) -> Dict[str, jax.Array]:
    del contact  # Unused.

    gyro = self.get_gyro(data)
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_gyro = (
        gyro
        + (2 * jax.random.uniform(noise_rng, shape=gyro.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.gyro
    )

    gravity = self.get_gravity(data)
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_gravity = (
        gravity
        + (2 * jax.random.uniform(noise_rng, shape=gravity.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.gravity
    )

    joint_angles = data.qpos[7:]
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_joint_angles = (
        joint_angles
        + (2 * jax.random.uniform(noise_rng, shape=joint_angles.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.joint_pos
    )

    joint_vel = data.qvel[6:]
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_joint_vel = (
        joint_vel
        + (2 * jax.random.uniform(noise_rng, shape=joint_vel.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.joint_vel
    )

    linvel = self.get_local_linvel(data)
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_linvel = (
        linvel
        + (2 * jax.random.uniform(noise_rng, shape=linvel.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.linvel
    )

    state = jp.hstack([
        noisy_linvel,
        noisy_gyro,
        noisy_gravity,
        noisy_joint_angles - self._default_pose,
        noisy_joint_vel,
        info["last_act"],
    ])

    accelerometer = self.get_accelerometer(data)
    linvel = self.get_local_linvel(data)
    angvel = self.get_global_angvel(data)
    torso_height = data.site_xpos[self._imu_site_id][2]

    privileged_state = jp.hstack([
        state,
        gyro,
        accelerometer,
        linvel,
        angvel,
        joint_angles,
        joint_vel,
        data.actuator_force,
        torso_height,
    ])

    return {
        "state": state,
        "privileged_state": privileged_state,
    }
```

```python
def _get_reward(
      self,
      data: mjx.Data,
      action: jax.Array,
      info: dict[str, Any],
      done: jax.Array,
  ) -> dict[str, jax.Array]:
    forward = data.site_xmat[self._imu_site_id] @ jp.array([1.0, 0.0, 0.0])
    joint_torques = data.actuator_force
    torso_height = data.site_xpos[self._imu_site_id][2]
    return {
        "height": self._reward_height(torso_height),
        "orientation": self._reward_orientation(
            forward, self._desired_forward_vec
        ),
        "contact": self._cost_contact(data),
        "action_rate": self._cost_action_rate(action, info),
        "torques": self._cost_torques(joint_torques),
        "termination": done,
        "dof_pos_limits": self._cost_joint_pos_limits(data.qpos[7:]),
        "dof_acc": self._cost_dof_acc(data.qacc[6:]),
        "pose": self._cost_pose(data.qpos[7:]),
        "stay_still": self._cost_stay_still(data.qvel[:6]),
        "energy": self._cost_energy(data.qvel[6:], data.actuator_force),
    }
```

```python
def _reward_orientation(
      self, forward_vec: jax.Array, up_vec: jax.Array
  ) -> jax.Array:
    cos_dist = jp.dot(forward_vec, up_vec)
    normalized = 0.5 * cos_dist + 0.5
    return jp.square(normalized)
```

```python
def _reward_height(self, torso_height: jax.Array) -> jax.Array:
    height = jp.min(jp.array([torso_height, self._z_des]))
    error = self._z_des - height
    return jp.exp(-error / 1.0)
```
```

### mujoco_playground/_src/manipulation/aero_hand/aero_hand_constants.py

```
"""Constants for TetherIA Aero Hand Open."""
```

### mujoco_playground/_src/manipulation/aero_hand/base.py

```
"""Base classes for TetherIA Aero Hand Open."""
def get_assets()
class AeroHandEnv(MjxEnv)
    """Base class for Aero Hand environments."""
    def __init__(self, xml_path, config, config_overrides)
    def get_palm_position(self, data)
    def get_cube_position(self, data)
    def get_cube_orientation(self, data)
    def get_cube_linvel(self, data)
    def get_cube_angvel(self, data)
    def get_cube_angacc(self, data)
    def get_cube_upvector(self, data)
    def get_cube_goal_orientation(self, data)
    def get_cube_goal_upvector(self, data)
    def get_fingertip_positions(self, data)
    def xml_path(self)
    def action_size(self)
    def mj_model(self)
    def mjx_model(self)
def uniform_quat(rng)
```

### mujoco_playground/_src/manipulation/aero_hand/rotate_z.py

```
"""Rotate-z with TetherIA Aero Hand Open."""
def default_config()
class CubeRotateZAxis(AeroHandEnv)
    """Rotate a cube around the z-axis as fast as possible wihout dropping it."""
    def __init__(self, config, config_overrides)
    def _post_init(self)
    def reset(self, rng)
    def step(self, state, action)
    def _get_termination(self, data)
    def _get_obs(self, data, info, obs_history)
    def _get_reward(self, data, action, info, metrics, done)
    def _cost_torques(self, torques)
    def _cost_energy(self, qvel, qfrc_actuator)
    def _cost_linvel(self, cube_linvel)
    def _reward_angvel(self, cube_angvel, cube_pos_error)
    def _cost_action_rate(self, act, last_act, last_last_act)
    def _cost_pose(self, joint_angles)
def domain_randomize(model, rng)

```python
def _get_obs(
      self, data: mjx.Data, info: dict[str, Any], obs_history: jax.Array
  ) -> Dict[str, jax.Array]:

    info["rng"], noise_rng = jax.random.split(info["rng"])

    # ------- tendon length sensor -------
    tendon_lengths = jp.zeros(
        (len(consts.SENSOR_TENDON_NAMES),), dtype=jp.float32
    )
    for idx, name in enumerate(consts.SENSOR_TENDON_NAMES):
      v = mjx_env.get_sensor_data(self.mj_model, data, name)
      v = jp.ravel(v)[0]
      tendon_lengths = tendon_lengths.at[idx].set(v)

    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_tendon_lengths = (
        tendon_lengths
        + (2 * jax.random.uniform(noise_rng, shape=tendon_lengths.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.tendon_length
    )

    # ------- joint angle sensor -------
    joint_angles = jp.zeros((len(consts.SENSOR_JOINT_NAMES),), dtype=jp.float32)
    for idx, name in enumerate(consts.SENSOR_JOINT_NAMES):
      v = mjx_env.get_sensor_data(self.mj_model, data, name)
      v = jp.ravel(v)[0]
      joint_angles = joint_angles.at[idx].set(v)

    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_joint_angles = (
        joint_angles
        + (2 * jax.random.uniform(noise_rng, shape=joint_angles.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.joint_pos
    )

    state = jp.concatenate([
        noisy_tendon_lengths,
        noisy_joint_angles,
        info["last_act"],
    ])

    joint_angles = data.qpos[self._hand_qids]
    info["rng"], noise_rng = jax.random.split(info["rng"])
    obs_history = jp.roll(obs_history, state.size)
    obs_history = obs_history.at[: state.size].set(state)

    cube_pos = self.get_cube_position(data)
    palm_pos = self.get_palm_position(data)
    cube_pos_error = palm_pos - cube_pos
    cube_quat = self.get_cube_orientation(data)
    cube_angvel = self.get_cube_angvel(data)
    cube_linvel = self.get_cube_linvel(data)
    fingertip_positions = self.get_fingertip_positions(data)
    joint_torques = data.actuator_force

    privileged_state = jp.concatenate([
        state,
        joint_angles,
        data.qvel[self._hand_dqids],
        joint_torques,
        fingertip_positions,
        cube_pos_error,
        cube_quat,
        cube_angvel,
        cube_linvel,
    ])

    return {
        "state": obs_history,
        "privileged_state": privileged_state,
    }
```

```python
def _get_reward(
      self,
      data: mjx.Data,
      action: jax.Array,
      info: dict[str, Any],
      metrics: dict[str, Any],
      done: jax.Array,
  ) -> dict[str, jax.Array]:
    del metrics  # Unused.
    cube_pos = self.get_cube_position(data)
    palm_pos = self.get_palm_position(data)
    cube_pos_error = palm_pos - cube_pos
    cube_angvel = self.get_cube_angvel(data)
    cube_linvel = self.get_cube_linvel(data)
    return {
        "angvel": self._reward_angvel(cube_angvel, cube_pos_error),
        "linvel": self._cost_linvel(cube_linvel),
        "termination": done,
        "action_rate": self._cost_action_rate(
            action, info["last_act"], info["last_last_act"]
        ),
        "pose": self._cost_pose(data.qpos[self._hand_qids]),
        "torques": self._cost_torques(data.actuator_force),
        "energy": self._cost_energy(
            data.qvel[self._hand_dqids], data.qfrc_actuator[self._hand_dqids]
        ),
    }
```

```python
def _reward_angvel(
      self, cube_angvel: jax.Array, cube_pos_error: jax.Array
  ) -> jax.Array:
    # Unconditionally maximize angvel in the z-direction.
    del cube_pos_error  # Unused.
    return cube_angvel @ jp.array([0.0, 0.0, 1.0])
```
```

### mujoco_playground/_src/manipulation/aloha/handover.py

```
"""Handover task for ALOHA."""
def default_config()
def logistic_barrier(x, x0, k, direction)
class HandOver(AlohaEnv)
    """Single peg insertion task for ALOHA."""
    def __init__(self, config, config_overrides)
    def _post_init(self)
    def reset(self, rng)
    def step(self, state, action)
    def _get_reward(self, data, info)
    def _get_obs(self, data, info)

```python
def _get_reward(self, data: mjx.Data, info: Dict[str, Any]) -> Dict[str, Any]:
    def distance(x, y):
      return jp.exp(-10 * jp.linalg.norm(x - y))

    box_top = data.site_xpos[self._box_top_site]
    box_bottom = data.site_xpos[self._box_bottom_site]
    box = data.xpos[self._box_body]
    l_gripper = data.site_xpos[self._left_gripper_site]
    r_gripper = data.site_xpos[self._right_gripper_site]

    pre = jp.where(box[0] < self._left_thresh, 1.0, 0.0)
    past = jp.where(box[0] >= self._right_thresh, 1.0, 0.0)
    btwn = (1 - pre) * (1 - past)

    #### Gripper Box
    r_lg = distance(box_top, l_gripper) * (pre + btwn)
    # If you're past the left threshold, also reward the right gripper.
    r_rg = distance(box_bottom, r_gripper) * (btwn + past)
    # Maintain reward level after left out of range.
    r_rg_bias = distance(box_bottom, r_gripper) * past

    #### Box Handover to handover point
    box_handover = distance(box, self._handover_pos)
    # Maintain this term after RH takes box away.
    hand_handover = distance(l_gripper, self._handover_pos) * past
    box_handover = jp.maximum(box_handover, hand_handover)

    #### Bring box to target
    box_target = distance(info['target_pos'], box) * (r_rg + r_rg_bias)
    # Don't let the left hand do it.
    box_target *= logistic_barrier(l_gripper[0], direction=-1)

    #### Avoid table collision - unstable simulation.
    table_collision = self.hand_table_collision(data)

    return {
        'gripper_box': r_lg + r_rg + r_rg_bias,
        'box_handover': box_handover,
        'handover_target': box_target,
        'no_table_collision': 1 - table_collision,
    }
```

```python
def _get_obs(self, data: mjx.Data, info: Dict[str, Any]) -> jax.Array:
    left_gripper_pos = data.site_xpos[self._left_gripper_site]
    left_gripper_mat = data.site_xmat[self._left_gripper_site]
    right_gripper_pos = data.site_xpos[self._right_gripper_site]
    right_gripper_mat = data.site_xmat[self._right_gripper_site]
    box_mat = data.xmat[self._box_body]
    box_top = data.site_xpos[self._box_top_site]
    box_bottom = data.site_xpos[self._box_bottom_site]
    finger_qposadr = data.qpos[self._finger_qposadr]
    box_width = self.mjx_model.geom_size[self._box_geom][1]

    obs = jp.concatenate([
        data.qpos,
        data.qvel,
        (finger_qposadr - box_width),
        box_top,
        box_bottom,
        left_gripper_pos,
        left_gripper_mat.ravel()[3:],
        right_gripper_pos,
        right_gripper_mat.ravel()[3:],
        box_mat.ravel()[3:],
        data.xpos[self._box_body] - info['target_pos'],
        (info['_steps'].reshape((1,)) / self._config.episode_length).astype(
            float
        ),
    ])

    return obs
```
```

### mujoco_playground/_src/manipulation/leap_hand/base.py

```
"""Base classes for leap hand."""
def get_assets()
class LeapHandEnv(MjxEnv)
    """Base class for LEAP hand environments."""
    def __init__(self, xml_path, config, config_overrides)
    def get_palm_position(self, data)
    def get_cube_position(self, data)
    def get_cube_orientation(self, data)
    def get_cube_linvel(self, data)
    def get_cube_angvel(self, data)
    def get_cube_angacc(self, data)
    def get_cube_upvector(self, data)
    def get_cube_goal_orientation(self, data)
    def get_cube_goal_upvector(self, data)
    def get_fingertip_positions(self, data)
    def xml_path(self)
    def action_size(self)
    def mj_model(self)
    def mjx_model(self)
def uniform_quat(rng)
```

### mujoco_playground/_src/manipulation/leap_hand/leap_hand_constants.py

```
"""Constants for leap hand."""
```

### mujoco_playground/_src/manipulation/leap_hand/reorient.py

```
"""Reorient task for leap hand."""
def default_config()
class CubeReorient(LeapHandEnv)
    """Reorient a cube to match a goal orientation."""
    def __init__(self, config, config_overrides)
    def _post_init(self)
    def reset(self, rng)
    def step(self, state, action)
    def _get_termination(self, data, info)
    def _get_obs(self, data, info)
    def _get_reward(self, data, action, info, metrics, done)
    def _cost_energy(self, qvel, qfrc_actuator)
    def _cube_orientation_error(self, data)
    def _reward_cube_orientation(self, data)
    def _cost_action_rate(self, act, last_act, last_last_act)
    def _cost_joint_vel(self, data)
    def _maybe_apply_perturbation(self, state, rng)
def domain_randomize(model, rng)

```python
def _get_obs(
      self, data: mjx.Data, info: dict[str, Any]
  ) -> mjx_env.Observation:
    # Hand joint angles.
    joint_angles = data.qpos[self._hand_qids]
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_joint_angles = (
        joint_angles
        + (2 * jax.random.uniform(noise_rng, shape=joint_angles.shape) - 1)
        * self._config.obs_noise.level
        * self._config.obs_noise.scales.joint_pos
    )

    # Joint position error history.
    qpos_error_history = (
        jp.roll(info["qpos_error_history"], 16)
        .at[:16]
        .set(noisy_joint_angles - info["motor_targets"])
    )
    info["qpos_error_history"] = qpos_error_history

    def _get_cube_pose(data: mjx.Data) -> jax.Array:
      """Returns (potentially) noisy cube pose (xyz,wxyz)."""
      cube_pos = self.get_cube_position(data)
      cube_quat = self.get_cube_orientation(data)
      info["rng"], pos_rng, ori_rng = jax.random.split(info["rng"], 3)
      noisy_cube_quat = mjx._src.math.normalize(
          cube_quat
          + jax.random.normal(ori_rng, shape=(4,))
          * self._config.obs_noise.level
          * self._config.obs_noise.scales.cube_ori
      )
      noisy_cube_pos = (
          cube_pos
          + (2 * jax.random.uniform(pos_rng, shape=cube_pos.shape) - 1)
          * self._config.obs_noise.level
          * self._config.obs_noise.scales.cube_pos
      )
      return jp.concatenate([noisy_cube_pos, noisy_cube_quat])

    # Noisy cube pose.
    noisy_pose = _get_cube_pose(data)
    info["rng"], key1, key2, key3 = jax.random.split(info["rng"], 4)
    rand_quat = leap_hand_base.uniform_quat(key1)
    rand_pos = jax.random.uniform(key2, (3,), minval=-0.5, maxval=0.5)
    rand_pose = jp.concatenate([rand_pos, rand_quat])
    m = self._config.obs_noise.level * jax.random.bernoulli(
        key3, self._config.obs_noise.random_ori_injection_prob
    )
    noisy_pose = noisy_pose * (1 - m) + rand_pose * m

    # Cube position error history.
    palm_pos = self.get_palm_position(data)
    cube_pos_error = palm_pos - noisy_pose[:3]
    cube_pos_error_history = (
        jp.roll(info["cube_pos_error_history"], 3).at[:3].set(cube_pos_error)
    )
    info["cube_pos_error_history"] = cube_pos_error_history

    # Cube orientation error history.
    goal_quat = self.get_cube_goal_orientation(data)
    quat_diff = mjx._src.math.quat_mul(
        noisy_pose[3:], mjx._src.math.quat_inv(goal_quat)
    )
    xmat_diff = mjx._src.math.quat_to_mat(quat_diff).ravel()[3:]
    cube_ori_error_history = (
        jp.roll(info["cube_ori_error_history"], 6).at[:6].set(xmat_diff)
    )
    info["cube_ori_error_history"] = cube_ori_error_history

    # Uncorrupted cube pose for critic.
    cube_pos_error_uncorrupted = palm_pos - self.get_cube_position(data)
    cube_quat_uncorrupted = self.get_cube_orientation(data)
    quat_diff_uncorrupted = math.quat_mul(
        cube_quat_uncorrupted, math.quat_inv(goal_quat)
    )
    xmat_diff_uncorrupted = math.quat_to_mat(quat_diff_uncorrupted).ravel()[3:]

    state = jp.concatenate([
        noisy_joint_angles,  # 16
        qpos_error_history,  # 16 * history_len
        cube_pos_error_history,  # 3 * history_len
        cube_ori_error_history,  # 6 * history_len
        info["last_act"],  # 16
    ])

    privileged_state = jp.concatenate([
        state,
        data.qpos[self._hand_qids],
        data.qvel[self._hand_dqids],
        self.get_fingertip_positions(data),
        cube_pos_error_uncorrupted,
        xmat_diff_uncorrupted,
        self.get_cube_linvel(data),
        self.get_cube_angvel(data),
        info["pert_dir"],
        data.xfrc_applied[self._cube_body_id],
    ])

    return {
        "state": state,
        "privileged_state": privileged_state,
    }
```

```python
def _get_reward(
      self,
      data: mjx.Data,
      action: jax.Array,
      info: dict[str, Any],
      metrics: dict[str, Any],
      done: jax.Array,
  ) -> dict[str, jax.Array]:
    del done, metrics  # Unused.

    cube_pos = self.get_cube_position(data)
    palm_pos = self.get_palm_position(data)
    cube_pose_mse = jp.linalg.norm(palm_pos - cube_pos)
    cube_pos_reward = reward.tolerance(
        cube_pose_mse, (0, 0.02), margin=0.05, sigmoid="linear"
    )

    terminated = self._get_termination(data, info)

    hand_pose_reward = jp.sum(
        jp.square(data.qpos[self._hand_qids] - self._default_pose)
    )

    return {
        "orientation": self._reward_cube_orientation(data),
        "position": cube_pos_reward,
        "termination": terminated,
        "hand_pose": hand_pose_reward,
        "action_rate": self._cost_action_rate(
            action, info["last_act"], info["last_last_act"]
        ),
        "joint_vel": self._cost_joint_vel(data),
        "energy": self._cost_energy(
            data.qvel[self._hand_dqids], data.actuator_force
        ),
    }
```

```python
def _reward_cube_orientation(self, data: mjx.Data) -> jax.Array:
    ori_error = self._cube_orientation_error(data)
    return reward.tolerance(ori_error, (0, 0.2), margin=jp.pi, sigmoid="linear")
```
```

### mujoco_playground/_src/manipulation/leap_hand/rotate_z.py

```
"""Rotate-z with leap hand."""
def default_config()
class CubeRotateZAxis(LeapHandEnv)
    """Rotate a cube around the z-axis as fast as possible wihout dropping it."""
    def __init__(self, config, config_overrides)
    def _post_init(self)
    def reset(self, rng)
    def step(self, state, action)
    def _get_termination(self, data)
    def _get_obs(self, data, info, obs_history)
    def _get_reward(self, data, action, info, metrics, done)
    def _cost_torques(self, torques)
    def _cost_energy(self, qvel, qfrc_actuator)
    def _cost_linvel(self, cube_linvel)
    def _reward_angvel(self, cube_angvel, cube_pos_error)
    def _cost_action_rate(self, act, last_act, last_last_act)
    def _cost_pose(self, joint_angles)
def domain_randomize(model, rng)

```python
def _get_obs(
      self, data: mjx.Data, info: dict[str, Any], obs_history: jax.Array
  ) -> Dict[str, jax.Array]:
    joint_angles = data.qpos[self._hand_qids]
    info["rng"], noise_rng = jax.random.split(info["rng"])
    noisy_joint_angles = (
        joint_angles
        + (2 * jax.random.uniform(noise_rng, shape=joint_angles.shape) - 1)
        * self._config.noise_config.level
        * self._config.noise_config.scales.joint_pos
    )

    state = jp.concatenate([
        noisy_joint_angles,  # 16
        info["last_act"],  # 16
    ])  # 48
    obs_history = jp.roll(obs_history, state.size)
    obs_history = obs_history.at[: state.size].set(state)

    cube_pos = self.get_cube_position(data)
    palm_pos = self.get_palm_position(data)
    cube_pos_error = palm_pos - cube_pos
    cube_quat = self.get_cube_orientation(data)
    cube_angvel = self.get_cube_angvel(data)
    cube_linvel = self.get_cube_linvel(data)
    fingertip_positions = self.get_fingertip_positions(data)
    joint_torques = data.actuator_force

    privileged_state = jp.concatenate([
        state,
        joint_angles,
        data.qvel[self._hand_dqids],
        joint_torques,
        fingertip_positions,
        cube_pos_error,
        cube_quat,
        cube_angvel,
        cube_linvel,
    ])

    return {
        "state": obs_history,
        "privileged_state": privileged_state,
    }
```

```python
def _get_reward(
      self,
      data: mjx.Data,
      action: jax.Array,
      info: dict[str, Any],
      metrics: dict[str, Any],
      done: jax.Array,
  ) -> dict[str, jax.Array]:
    del metrics  # Unused.
    cube_pos = self.get_cube_position(data)
    palm_pos = self.get_palm_position(data)
    cube_pos_error = palm_pos - cube_pos
    cube_angvel = self.get_cube_angvel(data)
    cube_linvel = self.get_cube_linvel(data)
    return {
        "angvel": self._reward_angvel(cube_angvel, cube_pos_error),
        "linvel": self._cost_linvel(cube_linvel),
        "termination": done,
        "action_rate": self._cost_action_rate(
            action, info["last_act"], info["last_last_act"]
        ),
        "pose": self._cost_pose(data.qpos[self._hand_qids]),
        "torques": self._cost_torques(data.actuator_force),
        "energy": self._cost_energy(
            data.qvel[self._hand_dqids], data.actuator_force
        ),
    }
```

```python
def _reward_angvel(
      self, cube_angvel: jax.Array, cube_pos_error: jax.Array
  ) -> jax.Array:
    # Unconditionally maximize angvel in the z-direction.
    del cube_pos_error  # Unused.
    return cube_angvel @ jp.array([0.0, 0.0, 1.0])
```
```

### mujoco_playground/_src/mjx_env.py

```
"""Core classes for MuJoCo Playground."""
def _clone_with_progress(repo_url, target_path, commit_sha)
def ensure_menagerie_exists()
def update_assets(assets, path, glob, recursive)
def put_model(model, device, impl)
def make_data(model, qpos, qvel, ctrl, act, mocap_pos, mocap_quat, impl, naconmax, naccdmax, njmax, device)
def step(model, data, action, n_substeps)
class State()
    """Environment state for training and inference."""
    def tree_replace(self, params)
def _tree_replace(base, attr, val)
class MjxEnv(ABC)
    """Base class for playground environments."""
    def __init__(self, config, config_overrides)
    def reset(self, rng)
    def step(self, state, action)
    def xml_path(self)
    def action_size(self)
    def mj_model(self)
    def mjx_model(self)
    def dt(self)
    def sim_dt(self)
    def n_substeps(self)
    def observation_size(self)
    def model_assets(self)
    def render(self, trajectory, height, width, camera, scene_option, modify_scene_fns)
    def unwrapped(self)
def render_array(mj_model, trajectory, height, width, camera, scene_option, modify_scene_fns, hfield_data)
def get_sensor_data(model, data, sensor_name)
def dof_width(joint_type)
def qpos_width(joint_type)
def get_qpos_ids(model, joint_names)
def get_qvel_ids(model, joint_names)

```python
def observation_size(self) -> ObservationSize:
    abstract_state = jax.eval_shape(self.reset, jax.random.PRNGKey(0))
    obs = abstract_state.obs
    if isinstance(obs, Mapping):
      return jax.tree_util.tree_map(lambda x: x.shape, obs)
    return obs.shape[-1]
```
```

### mujoco_playground/_src/reward.py

```
"""A port of dm_control.utils.rewards to JAX."""
def _sigmoids(x, value_at_1, sigmoid)
def tolerance(x, bounds, margin, sigmoid, value_at_margin)
```

### mujoco_playground/config/dm_control_suite_params.py

```
"""RL config for DM Control Suite."""
def brax_ppo_config(env_name, impl)
def brax_vision_ppo_config(env_name, unused_impl)
def brax_sac_config(env_name, unused_impl)
```

### mujoco_playground/config/locomotion_params.py

```
"""RL config for Locomotion envs."""
def brax_ppo_config(env_name, impl)
def rsl_rl_config(env_name, unused_impl)
```

### mujoco_playground/config/manipulation_params.py

```
"""RL config for Manipulation envs."""
def brax_ppo_config(env_name, impl)
def brax_vision_ppo_config(env_name, unused_impl)
def rsl_rl_config(env_name, unused_impl)
```

### mujoco_playground/experimental/sim2sim/gamepad_reader.py

```
"""Logitech F710 Gamepad class that uses HID under the hood.

Adapted from motion_imitation: https://github.com/erwincoumans/motion_imitation/tree/master/motion_imitation/robots/gamepad/gamepad_reader.py."""
def _interpolate(value, old_max, new_scale, deadzone)
class Gamepad()
    """Gamepad class that reads from a Logitech F710 gamepad."""
    def __init__(self, vendor_id, product_id, vel_scale_x, vel_scale_y, vel_scale_rot)
    def _connect_device(self)
    def read_loop(self)
    def update_command(self, data)
    def get_command(self)
    def stop(self)
```

### mujoco_playground/experimental/sim2sim/play_apollo_joystick.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Booster Apollo humanoid."""
    def __init__(self, policy_path, default_angles, ctrl_dt, n_substeps, action_scale, vel_scale_x, vel_scale_y, vel_scale_rot)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```

### mujoco_playground/experimental/sim2sim/play_bh_joystick.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Berkeley humanoid."""
    def __init__(self, policy_path, default_angles, ctrl_dt, n_substeps, action_scale, vel_scale_x, vel_scale_y, vel_scale_rot)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```

### mujoco_playground/experimental/sim2sim/play_g1_joystick.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Go-1 robot."""
    def __init__(self, policy_path, default_angles, ctrl_dt, n_substeps, action_scale, vel_scale_x, vel_scale_y, vel_scale_rot)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```

### mujoco_playground/experimental/sim2sim/play_go1_joystick.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Go-1 robot."""
    def __init__(self, policy_path, default_angles, n_substeps, action_scale, vel_scale_x, vel_scale_y, vel_scale_rot)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```

### mujoco_playground/experimental/sim2sim/play_leap_reorient.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Leap hand."""
    def __init__(self, policy_path, hand_qids, hand_dqids, ctrl_init, lowers, uppers, n_substeps, action_scale)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```

### mujoco_playground/experimental/sim2sim/play_t1_joystick.py

```
"""Deploy an MJX policy in ONNX format to C MuJoCo and play with it."""
class OnnxController()
    """ONNX controller for the Booster T1 humanoid."""
    def __init__(self, policy_path, default_angles, ctrl_dt, n_substeps, action_scale, vel_scale_x, vel_scale_y, vel_scale_rot)
    def get_obs(self, model, data)
    def get_control(self, model, data)
def load_callback(model, data)
```