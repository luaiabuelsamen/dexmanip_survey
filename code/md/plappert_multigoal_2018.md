# plappert_multigoal_2018

source: https://github.com/Farama-Foundation/Gymnasium-Robotics


commit: 4d1ebecbc6436806cfbc0e42ebc36f594d05844e


## README

[![Python](https://img.shields.io/pypi/pyversions/gymnasium-robotics.svg)](https://badge.fury.io/py/gymnasium-robotics)
[![PyPI](https://badge.fury.io/py/gymnasium-robotics.svg)](https://badge.fury.io/py/gymnasium-robotics)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<p align="center">
  <a href = "https://robotics.farama.org/" target = "_blank"> <img src="https://raw.githubusercontent.com/Farama-Foundation/Gymnasium-Robotics/main/docs/gymnasium-robotics.png" width="500px"/> </a>
</p>

This library contains a collection of Reinforcement Learning robotic environments that use the [Gymnasium](https://gymnasium.farama.org/) API. The environments run with the [MuJoCo](https://mujoco.org/) physics engine and the maintained [mujoco python bindings](https://mujoco.readthedocs.io/en/latest/python.html).

The documentation website is at [robotics.farama.org](https://robotics.farama.org/), and we have a public discord server (which we also use to coordinate development work) that you can join here: [https://discord.gg/YymmHrvS](https://discord.gg/YymmHrvS)

## Installation

To install the Gymnasium-Robotics environments use `pip install gymnasium-robotics`

These environments also require the MuJoCo engine from Deepmind to be installed. Instructions to install the physics engine can be found at the [MuJoCo website](https://mujoco.org/) and the [MuJoCo Github repository](https://github.com/deepmind/mujoco).

Note that the latest environment versions use the latest mujoco python bindings maintained by the MuJoCo team. If you wish to use the old versions of the environments that depend on [mujoco-py](https://github.com/openai/mujoco-py), please install this library with `pip install gymnasium-robotics[mujoco-py]`

We support and test for Linux and macOS. We will accept PRs related to Windows, but do not officially support it.

## Environments

`Gymnasium-Robotics` includes the following groups of environments:

* [Fetch](https://robotics.farama.org/envs/fetch/) - A collection of environments with a 7-DoF robot arm that has to perform manipulation tasks such as Reach, Push, Slide or Pick and Place.
* [Shadow Dexterous Hand](https://robotics.farama.org/envs/shadow_dexterous_hand/) - A collection of environments with a 24-DoF anthropomorphic robotic hand that has to perform object manipulation tasks with a cube, egg-object, or pen. There are variations of these environments that also include data from 92 touch sensors in the observation space.
* [MaMuJoCo](https://robotics.farama.org/envs/MaMuJoCo/) - A collection of multi agent factorizations of the [Gymnasium/MuJoCo](https://gymnasium.farama.org/environments/mujoco/) environments and a framework for factorizing robotic environments, uses the [pettingzoo.ParallelEnv](https://pettingzoo.farama.org/api/parallel/) API.

The [D4RL](https://github.com/Farama-Foundation/D4RL) environments are now available. These environments have been refactored and may not have the same action/observation spaces as the original, please read their documentation:

* [Maze Environments](https://robotics.farama.org/envs/maze/) - An agent has to navigate through a maze to reach certain goal position. Two different agents can be used: a 2-DoF force-controlled ball, or the classic `Ant` agent from the [Gymnasium MuJoCo environments](https://gymnasium.farama.org/environments/mujoco/ant/). The environment can be initialized with a variety of maze shapes with increasing levels of difficulty.
* [Adroit Arm](https://robotics.farama.org/envs/adroit_hand/) - A collection of environments that use the Shadow Dexterous Hand with additional degrees of freedom for the arm movement.
The different tasks involve hammering a nail, opening a door, twirling a pen, or picking up and moving a ball.
* [Franka Kitchen](https://robotics.farama.org/envs/franka_kitchen/) - Multitask environment in which a 9-DoF Franka robot is placed in a kitchen containing several common household items. The goal of each task is to interact with the items in order to reach a desired goal configuration.

**WIP**: generate new `D4RL` environment datasets with [Minari](https://github.com/Farama-Foundation/Minari).

## Multi-goal API

The robotic environments use an extension of the core Gymnasium API by inheriting from [GoalEnv](https://robotics.farama.org/content/multi-goal_api/) class. The new API forces the environments to have a dictionary observation space that contains 3 keys:

* `observation` - The actual observation of the environment
* `desired_goal` - The goal that the agent has to achieved
* `achieved_goal` - The goal that the agent has currently achieved instead. The objective of the environments is for this value to be close to `desired_goal`

This API also exposes the function of the reward, as well as the terminated and truncated signals to re-compute their values with different goals. This functionality is useful for algorithms that use Hindsight Experience Replay (HER).

The following example demonstrates how the exposed reward, terminated, and truncated functions
can be used to re-compute the values with substituted goals. The info dictionary can be used to store
additional information that may be necessary to re-compute the reward, but that is independent of the
goal, e.g. state derived from the simulation.

```python
import gymnasium as gym
import gymnasium_robotics

gym.register_envs(gymnasium_robotics)

env = gym.make("FetchReach-v4")
env.reset()
obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

# The following always has to hold:
assert reward == env.compute_reward(obs["achieved_goal"], obs["desired_goal"], info)
assert truncated == env.compute_truncated(obs["achieved_goal"], obs["desired_goal"], info)
assert terminated == env.compute_terminated(obs["achieved_goal"], obs["desired_goal"], info)

# However goals can also be substituted:
substitute_goal = obs["achieved_goal"].copy()
substitute_reward = env.compute_reward(obs["achieved_goal"], substitute_goal, info)
substitute_terminated = env.compute_terminated(obs["achieved_goal"], substitute_goal, info)
substitute_truncated = env.compute_truncated(obs["achieved_goal"], substitute_goal, info)
```

The `GoalEnv` class can also be used for custom environments.

## Project Maintainer
Kallinteris Andreas](https://github.com/Kallinteris-Andreas)

Maintenance for this project is also contributed by the broader Farama team: [farama.org/team](https://farama.org/team).

## Citation

If you use this in your research, please cite:
```
@software{gymnasium_robotics2023github,
  author = {Rodrigo de Lazcano and Kallinteris Andreas and Jun Jet Tai and Seungjae Ryan Lee and Jordan Terry},
  title = {Gymnasium Robotics},
  url = {http://github.com/Farama-Foundation/Gymnasium-Robotics},
  version = {1.4.0},
  year = {2024},
}
```


## File tree (depth 3, assets pruned)

```
.github/
  FUNDING.yml
  ISSUE_TEMPLATE/
    bug.md
    proposal.md
    question.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  docker/
    entrypoint
    py.Dockerfile
  stale.yml
  workflows/
    build-docs-dev.yml
    build-docs-version.yml
    build.yml
    manual-build-docs-version.yml
    pre-commit.yml
    pypi-publish.yml
.gitignore
.pre-commit-config.yaml
CITATION.cff
CODE_OF_CONDUCT.rst
LICENSE
README.md
gymnasium_robotics/
  __init__.py
  core.py
  envs/
    __init__.py
    adroit_hand/
    fetch/
    franka_kitchen/
    maze/
    mujoco/
    multiagent_mujoco/
    robot_env.py
    shadow_dexterous_hand/
  utils/
    __init__.py
    mujoco_py_utils.py
    mujoco_utils.py
    rotations.py
pyproject.toml
setup.py
tests/
  __init__.py
  envs/
    MaMuJoCo/
    __init__.py
    adroit_hand/
    franka_kitchen/
    hand/
    maze/
    mujoco/
  test_envs.py
  test_goal_env_api.py
  test_mujoco_utils.py
  utils.py
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-symlinks
      - id: destroyed-symlinks
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-ast
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: detect-private-key
      - id: debug-statements
  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
        exclude: .svg
        args:
          - --ignore-words-list=nd,reacher,thist,ths, arry
  - repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
      - id: flake8
        args:
          - '--per-file-ignores=*/__init__.py:F401 /gymnasium_robotics/envs/multiagent_mujoco/__init__.py:F401'
          - --ignore=E203,W503
          - --max-complexity=30
          - --max-line-length=456
          - --show-source
          - --statistics
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.20.0
    hooks:
      - id: pyupgrade
        args: ["--py38-plus"]
  - repo: https://github.com/PyCQA/isort
    rev: 6.0.1
    hooks:
      - id: isort
        args: ["--profile", "black"]
  - repo: https://github.com/python/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/pydocstyle
    rev: 6.3.0
    hooks:
      - id: pydocstyle
        exclude: ^(tests/envs/hand)|(tests/test_envs.py)|(tests/__init__.py)|(tests/utils.py)|(tests/envs/__init__.py)|(tests/envs/mujoco)|(docs)|(gymnasium_robotics/utils)|(gymnasium_robotics/envs/fetch)|(gymnasium_robotics/envs/shadow_dexterous_hand)|(gymnasium_robotics/envs/maze)|(gymnasium_robotics/envs/adroit_hand)|(gymnasium_robotics/envs/franka_kitchen)|(gymnasium_robotics/envs/mujoco)
        args:
          - --convention=google
          - --add-ignore=D100
          - --source
          - --explain
        additional_dependencies: ["tomli"]
  - repo: local
    hooks:
      - id: pyright
        name: pyright
        entry: pyright
        language: node
        pass_filenames: false
        types: [python]
        additional_dependencies: ["pyright@1.1.347"]
        args:
          - --project=pyproject.toml

```

## Python signatures and reward/observation bodies (79 files)


### gymnasium_robotics/envs/adroit_hand/adroit_door.py

```
"""An Adroit arm environment with door task using the Gymnasium API.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files adding support for the Gymnasium API.

This project is covered by the Apache 2.0 License."""
class AdroitHandDoorEnv(MujocoEnv, EzPickle)
    """## Description

This environment was introduced in ["Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations"](https://arxiv.org/abs/1709.10087)
by Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine."""
    def __init__(self, reward_type)
    def step(self, a)
    def _get_obs(self)
    def reset(self)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def _get_obs(self):
        # qpos for hand
        # xpos for obj
        # xpos for target
        qpos = self.data.qpos.ravel()
        handle_pos = self.data.site_xpos[self.handle_site_id].ravel()
        palm_pos = self.data.site_xpos[self.grasp_site_id].ravel()
        door_pos = np.array([self.data.qpos[self.door_hinge_addrs]])
        if door_pos > 1.0:
            door_open = 1.0
        else:
            door_open = -1.0
        latch_pos = qpos[-1]

        return np.concatenate(
            [
                qpos[1:-2],
                [latch_pos],
                door_pos,
                palm_pos,
                handle_pos,
                palm_pos - handle_pos,
                [door_open],
            ]
        )
```
```

### gymnasium_robotics/envs/adroit_hand/adroit_hammer.py

```
"""An Adroit arm environment with hammer and nail task using the Gymnasium API.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files adding support for the Gymnasium API.

This project is covered by the Apache 2.0 License."""
class AdroitHandHammerEnv(MujocoEnv, EzPickle)
    """## Description

This environment was introduced in ["Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations"](https://arxiv.org/abs/1709.10087)
by Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine."""
    def __init__(self, reward_type)
    def step(self, a)
    def _get_obs(self)
    def reset(self)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def _get_obs(self):
        # qpos for hand
        # xpos for obj
        # xpos for target
        qp = self.data.qpos.ravel()
        qv = np.clip(self.data.qvel.ravel(), -1.0, 1.0)
        obj_pos = self.data.xpos[self.obj_body_id].ravel()
        obj_rot = quat2euler(self.data.xquat[self.obj_body_id].ravel()).ravel()
        palm_pos = self.data.site_xpos[self.S_grasp_site_id].ravel()
        target_pos = self.data.site_xpos[self.target_obj_site_id].ravel()
        nail_impact = np.clip(
            self.data.sensordata[self._model_names.sensor_name2id["S_nail"]], -1.0, 1.0
        )
        return np.concatenate(
            [
                qp[:-6],
                qv[-6:],
                palm_pos,
                obj_pos,
                obj_rot,
                target_pos,
                np.array([nail_impact]),
            ]
        )
```
```

### gymnasium_robotics/envs/adroit_hand/adroit_pen.py

```
"""An Adroit arm environment with pen task using the Gymnasium API.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files adding support for the Gymnasium API.

This project is covered by the Apache 2.0 License."""
class AdroitHandPenEnv(MujocoEnv, EzPickle)
    """## Description

This environment was introduced in ["Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations"](https://arxiv.org/abs/1709.10087)
by Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine."""
    def __init__(self, reward_type)
    def step(self, a)
    def _get_obs(self)
    def reset(self)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def _get_obs(self):
        qpos = self.data.qpos.ravel()
        obj_vel = self.data.qvel[-6:].ravel()
        obj_pos = self.data.xpos[self.obj_body_id].ravel()
        desired_pos = self.data.site_xpos[self.eps_ball_site_id].ravel()
        obj_orien = (
            self.data.site_xpos[self.obj_t_site_id]
            - self.data.site_xpos[self.obj_b_site_id]
        ) / self.pen_length
        desired_orien = (
            self.data.site_xpos[self.tar_t_site_id]
            - self.data.site_xpos[self.tar_b_site_id]
        ) / self.tar_length

        return np.concatenate(
            [
                qpos[:-6],
                obj_pos,
                obj_vel,
                obj_orien,
                desired_orien,
                obj_pos - desired_pos,
                obj_orien - desired_orien,
            ]
        )
```
```

### gymnasium_robotics/envs/adroit_hand/adroit_relocate.py

```
"""An Adroit arm environment with ball relocation task using the Gymnasium API.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files adding support for the Gymnasium API.

This project is covered by the Apache 2.0 License."""
class AdroitHandRelocateEnv(MujocoEnv, EzPickle)
    """## Description

This environment was introduced in ["Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations"](https://arxiv.org/abs/1709.10087)
by Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, and Sergey Levine."""
    def __init__(self, reward_type)
    def step(self, a)
    def _get_obs(self)
    def reset(self)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def _get_obs(self):
        # qpos for hand
        # xpos for obj
        # xpos for target
        qpos = self.data.qpos.ravel()
        obj_pos = self.data.xpos[self.obj_body_id].ravel()
        palm_pos = self.data.site_xpos[self.S_grasp_site_id].ravel()
        target_pos = self.data.site_xpos[self.target_obj_site_id].ravel()
        return np.concatenate(
            [qpos[:-6], palm_pos - obj_pos, palm_pos - target_pos, obj_pos - target_pos]
        )
```
```

### gymnasium_robotics/envs/fetch/fetch_env.py

```
def goal_distance(goal_a, goal_b)
def get_base_fetch_env(RobotEnvClass)
class MujocoPyFetchEnv(?)
    def _step_callback(self)
    def _set_action(self, action)
    def generate_mujoco_observations(self)
    def _get_gripper_xpos(self)
    def _render_callback(self)
    def _viewer_setup(self)
    def _reset_sim(self)
    def _env_setup(self, initial_qpos)
class MujocoFetchEnv(?)
    def __init__(self, default_camera_config)
    def _step_callback(self)
    def _set_action(self, action)
    def generate_mujoco_observations(self)
    def _get_gripper_xpos(self)
    def _render_callback(self)
    def _reset_sim(self)
    def _env_setup(self, initial_qpos)

```python
def generate_mujoco_observations(self):
        # positions
        grip_pos = self.sim.data.get_site_xpos("robot0:grip")

        dt = self.sim.nsubsteps * self.sim.model.opt.timestep
        grip_velp = self.sim.data.get_site_xvelp("robot0:grip") * dt

        robot_qpos, robot_qvel = self._utils.robot_get_obs(self.sim)
        if self.has_object:
            object_pos = self.sim.data.get_site_xpos("object0")
            # rotations
            object_rot = rotations.mat2euler(self.sim.data.get_site_xmat("object0"))
            # velocities
            object_velp = self.sim.data.get_site_xvelp("object0") * dt
            object_velr = self.sim.data.get_site_xvelr("object0") * dt
            # gripper state
            object_rel_pos = object_pos - grip_pos
            object_velp -= grip_velp
        else:
            object_pos = object_rot = object_velp = object_velr = object_rel_pos = (
                np.zeros(0)
            )
        gripper_state = robot_qpos[-2:]

        gripper_vel = (
            robot_qvel[-2:] * dt
        )  # change to a scalar if the gripper is made symmetric

        return (
            grip_pos,
            object_pos,
            object_rel_pos,
            gripper_state,
            object_rot,
            object_velp,
            object_velr,
            grip_velp,
            gripper_vel,
        )
```

```python
def generate_mujoco_observations(self):
        # positions
        grip_pos = self._utils.get_site_xpos(self.model, self.data, "robot0:grip")

        dt = self.n_substeps * self.model.opt.timestep
        grip_velp = (
            self._utils.get_site_xvelp(self.model, self.data, "robot0:grip") * dt
        )

        robot_qpos, robot_qvel = self._utils.robot_get_obs(
            self.model, self.data, self._model_names.joint_names
        )
        if self.has_object:
            object_pos = self._utils.get_site_xpos(self.model, self.data, "object0")
            # rotations
            object_rot = rotations.mat2euler(
                self._utils.get_site_xmat(self.model, self.data, "object0")
            )
            # velocities
            object_velp = (
                self._utils.get_site_xvelp(self.model, self.data, "object0") * dt
            )
            object_velr = (
                self._utils.get_site_xvelr(self.model, self.data, "object0") * dt
            )
            # gripper state
            object_rel_pos = object_pos - grip_pos
            object_velp -= grip_velp
        else:
            object_pos = object_rot = object_velp = object_velr = object_rel_pos = (
                np.zeros(0)
            )
        gripper_state = robot_qpos[-2:]

        gripper_vel = (
            robot_qvel[-2:] * dt
        )  # change to a scalar if the gripper is made symmetric

        return (
            grip_pos,
            object_pos,
            object_rel_pos,
            gripper_state,
            object_rot,
            object_velp,
            object_velr,
            grip_velp,
            gripper_vel,
        )
```

```python
def compute_reward(self, achieved_goal, desired_goal, info):
            # Compute distance between goal and the achieved goal.
            d = goal_distance(achieved_goal, desired_goal)
            if self.reward_type == "sparse":
                return -(d > self.distance_threshold).astype(np.float32)
            else:
                return -d
```

```python
def _get_obs(self):
            (
                grip_pos,
                object_pos,
                object_rel_pos,
                gripper_state,
                object_rot,
                object_velp,
                object_velr,
                grip_velp,
                gripper_vel,
            ) = self.generate_mujoco_observations()

            if not self.has_object:
                achieved_goal = grip_pos.copy()
            else:
                achieved_goal = np.squeeze(object_pos.copy())

            obs = np.concatenate(
                [
                    grip_pos,
                    object_pos.ravel(),
                    object_rel_pos.ravel(),
                    gripper_state,
                    object_rot.ravel(),
                    object_velp.ravel(),
                    object_velr.ravel(),
                    grip_velp,
                    gripper_vel,
                ]
            )

            return {
                "observation": obs.copy(),
                "achieved_goal": achieved_goal.copy(),
                "desired_goal": self.goal.copy(),
            }
```

```python
def generate_mujoco_observations(self):

            raise NotImplementedError
```
```

### gymnasium_robotics/envs/fetch/pick_and_place.py

```
class MujocoFetchPickAndPlaceEnv(MujocoFetchEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The task in the environment is for a manipulator to move a block to a target position on top of a table or in mid-a"""
    def __init__(self, reward_type)
class MujocoPyFetchPickAndPlaceEnv(MujocoPyFetchEnv, EzPickle)
    def __init__(self, reward_type)
```

### gymnasium_robotics/envs/fetch/push.py

```
class MujocoPyFetchPushEnv(MujocoPyFetchEnv, EzPickle)
    def __init__(self, reward_type)
class MujocoFetchPushEnv(MujocoFetchEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The task in the environment is for a manipulator to move a block to a target position on top of a table by pushing """
    def __init__(self, reward_type)
```

### gymnasium_robotics/envs/fetch/reach.py

```
class MujocoFetchReachEnv(MujocoFetchEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The task in the environment is for a manipulator to move the end effector to a randomly selected position in the ro"""
    def __init__(self, reward_type)
class MujocoPyFetchReachEnv(MujocoPyFetchEnv, EzPickle)
    def __init__(self, reward_type)
```

### gymnasium_robotics/envs/fetch/slide.py

```
class MujocoPyFetchSlideEnv(MujocoPyFetchEnv, EzPickle)
    def __init__(self, reward_type)
class MujocoFetchSlideEnv(MujocoFetchEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The task in the environment is for a manipulator hit a puck in order to reach a target position on top of a long an"""
    def __init__(self, reward_type)
```

### gymnasium_robotics/envs/franka_kitchen/franka_env.py

```
"""Environment using Gymnasium API for Franka robot.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

This code was also implemented over the repository relay-policy-learning on GitHub (https://github.com/google-research/relay-policy-learning),
published in Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning, by
Abhishek Gupta, Vikash Kumar, Corey """
class FrankaRobot(MujocoEnv)
    def __init__(self, model_path, frame_skip, robot_noise_ratio, default_camera_config)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def _ctrl_velocity_limits(self, ctrl_velocity)
    def _ctrl_position_limits(self, ctrl_position)
    def _read_specs_from_config(self, robot_configs)

```python
def _get_obs(self):
        # Gather simulated observation
        robot_qpos, robot_qvel = robot_get_obs(
            self.model, self.data, self.model_names.joint_names
        )
        # Simulate observation noise
        robot_qpos += (
            self.robot_noise_ratio
            * self.robot_pos_noise_amp[:9]
            * self.np_random.uniform(low=-1.0, high=1.0, size=robot_qpos.shape)
        )
        robot_qvel += (
            self.robot_noise_ratio
            * self.robot_vel_noise_amp[:9]
            * self.np_random.uniform(low=-1.0, high=1.0, size=robot_qvel.shape)
        )

        self._last_robot_qpos = robot_qpos

        return np.concatenate((robot_qpos.copy(), robot_qvel.copy()))
```
```

### gymnasium_robotics/envs/franka_kitchen/kitchen_env.py

```
"""Environment using Gymnasium API and Multi-goal API for kitchen and Franka robot.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

This code was also implemented over the repository relay-policy-learning on GitHub (https://github.com/google-research/relay-policy-learning),
published in Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning, by
Abhis"""
class KitchenEnv(GoalEnv, EzPickle)
    """## Description

This environment was introduced in ["Relay policy learning: Solving long-horizon tasks via imitation and reinforcement learning"](https://arxiv.org/abs/1910.11956)
by Abhishek Gupta, Vikash Kumar, Corey Lynch, Sergey Levine, Karol Hausman.

The environment is based on the 9 degrees o"""
    def __init__(self, tasks_to_complete, terminate_on_tasks_completed, remove_task_when_completed, object_noise_ratio)
    def compute_reward(self, achieved_goal, desired_goal, info)
    def _get_obs(self, robot_obs)
    def step(self, action)
    def reset(self)
    def render(self)
    def close(self)

```python
def compute_reward(
        self,
        achieved_goal: "dict[str, np.ndarray]",
        desired_goal: "dict[str, np.ndarray]",
        info: "dict[str, Any]",
    ):
        self.step_task_completions.clear()
        for task in self.tasks_to_complete:
            distance = np.linalg.norm(achieved_goal[task] - desired_goal[task])
            complete = distance < BONUS_THRESH
            if complete:
                self.step_task_completions.append(task)

        return float(len(self.step_task_completions))
```

```python
def _get_obs(self, robot_obs):
        obj_qpos = self.data.qpos[9:].copy()
        obj_qvel = self.data.qvel[9:].copy()

        # Simulate observation noise
        obj_qpos += (
            self.object_noise_ratio
            * self.robot_env.robot_pos_noise_amp[8:]
            * self.robot_env.np_random.uniform(low=-1.0, high=1.0, size=obj_qpos.shape)
        )
        obj_qvel += (
            self.object_noise_ratio
            * self.robot_env.robot_vel_noise_amp[9:]
            * self.robot_env.np_random.uniform(low=-1.0, high=1.0, size=obj_qvel.shape)
        )

        achieved_goal = {
            task: self.data.qpos[OBS_ELEMENT_INDICES[task]] for task in self.goal.keys()
        }

        obs = {
            "observation": np.concatenate((robot_obs, obj_qpos, obj_qvel)),
            "achieved_goal": achieved_goal,
            "desired_goal": self.goal,
        }

        return obs
```
```

### gymnasium_robotics/envs/franka_kitchen/utils.py

```
"""Utility functions to read the file with the joints configuration of the Franka robot located at '../assets/kitchen_franka/franka_assets/franka_config.xml'."""
def read_config_from_node(root_node, parent_name, child_name, dtype)
def get_config_root_node(config_file_name, config_file_data)
def read_config_from_xml(config_file_name, parent_name, child_name, dtype)
```

### gymnasium_robotics/envs/maze/ant_maze_v3.py

```
class AntMazeEnv(MazeEnv, EzPickle)
    def __init__(self, render_mode, maze_map, reward_type, continuing_task)
    def reset(self)
    def step(self, action)
    def _get_obs(self, ant_obs)
    def update_target_site_pos(self)
    def render(self)
    def close(self)
    def model(self)
    def data(self)

```python
def _get_obs(self, ant_obs: np.ndarray) -> Dict[str, np.ndarray]:
        achieved_goal = ant_obs[:2]
        observation = ant_obs[2:]

        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```
```

### gymnasium_robotics/envs/maze/ant_maze_v4.py

```
"""A maze environment with the Gymnasium Ant agent (https://github.com/Farama-Foundation/Gymnasium/blob/main/gymnasium/envs/mujoco/ant_v4.py).

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve reusing the code in Gymnasium for the Ant environment and in `point_maze/maze_env.py`.
The new code also follows the Gymnasium"""
class AntMazeEnv(MazeEnv, EzPickle)
    def __init__(self, render_mode, maze_map, reward_type, continuing_task, reset_target)
    def reset(self)
    def step(self, action)
    def _get_obs(self, ant_obs)
    def update_target_site_pos(self)
    def render(self)
    def close(self)
    def model(self)
    def data(self)

```python
def _get_obs(self, ant_obs: np.ndarray) -> Dict[str, np.ndarray]:
        achieved_goal = ant_obs[:2]
        observation = ant_obs[2:]

        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```
```

### gymnasium_robotics/envs/maze/ant_maze_v5.py

```
"""A maze environment with the Gymnasium Ant agent (https://github.com/Farama-Foundation/Gymnasium/blob/main/gymnasium/envs/mujoco/ant_v5.py).

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve reusing the code in Gymnasium for the Ant environment and in `point_maze/maze_env.py`.
The new code also follows the Gymnasium"""
class AntMazeEnv(MazeEnv, EzPickle)
    """### Description

This environment was refactored from the [D4RL](https://github.com/Farama-Foundation/D4RL) repository, introduced by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine
in ["D4RL: Datasets for Deep Data-Driven Reinforcement Learning"](https://arxiv.org/abs/2004.07"""
    def __init__(self, render_mode, maze_map, reward_type, continuing_task, reset_target, xml_file)
    def reset(self)
    def step(self, action)
    def _get_obs(self, ant_obs)
    def update_target_site_pos(self)
    def render(self)
    def close(self)
    def model(self)
    def data(self)

```python
def _get_obs(self, ant_obs: np.ndarray) -> Dict[str, np.ndarray]:
        achieved_goal = ant_obs[:2]
        observation = ant_obs[2:]

        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```
```

### gymnasium_robotics/envs/maze/maps.py

```
"""A collection of maze map structures for the Gymnasium-Robotics PointMaze environments.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files: `maps.py`, `maze_env.py`, `point_env.py`, and `point_maze_env.py`.
As well as adding support for the Gymnasium API.

This project is cove"""
```

### gymnasium_robotics/envs/maze/maze.py

```
class Maze()
    def __init__(self, maze_map, maze_size_scaling, maze_height)
    def maze_map(self)
    def maze_size_scaling(self)
    def maze_height(self)
    def unique_goal_locations(self)
    def unique_reset_locations(self)
    def combined_locations(self)
    def map_length(self)
    def map_width(self)
    def x_map_center(self)
    def y_map_center(self)
    def cell_rowcol_to_xy(self, rowcol_pos)
    def cell_xy_to_rowcol(self, xy_pos)
    def make_maze(cls, agent_xml_path, maze_map, maze_size_scaling, maze_height)
class MazeEnv(GoalEnv)
    def __init__(self, agent_xml_path, reward_type, continuing_task, maze_map, maze_size_scaling, maze_height, position_noise_range)
    def generate_target_goal(self)
    def generate_reset_pos(self)
    def reset(self)
    def add_xy_position_noise(self, xy_pos)
    def compute_reward(self, achieved_goal, desired_goal, info)
    def compute_terminated(self, achieved_goal, desired_goal, info)
    def compute_truncated(self, achieved_goal, desired_goal, info)
    def update_target_site_pos(self, pos)

```python
def compute_reward(
        self, achieved_goal: np.ndarray, desired_goal: np.ndarray, info
    ) -> float:
        distance = np.linalg.norm(achieved_goal - desired_goal, axis=-1)
        if self.reward_type == "dense":
            return np.exp(-distance)
        elif self.reward_type == "sparse":
            return (distance <= 0.45).astype(np.float64)
```
```

### gymnasium_robotics/envs/maze/maze_v4.py

```
"""A maze environment with Gymnasium API for the Gymnasium-Robotics PointMaze environments.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files: `maps.py`, `maze_env.py`, `point_env.py`, and `point_maze_env.py`.
As well as adding support for the Gymnasium API.

This project is co"""
class Maze()
    """This class creates and holds information about the maze in the MuJoCo simulation.

The accessible attributes are the following:
- :attr:`maze_map` - The maze discrete data structure.
- :attr:`maze_size_scaling` - The maze scaling for the continuous coordinates in the MuJoCo simulation.
- :attr:`maze"""
    def __init__(self, maze_map, maze_size_scaling, maze_height)
    def maze_map(self)
    def maze_size_scaling(self)
    def maze_height(self)
    def unique_goal_locations(self)
    def unique_reset_locations(self)
    def combined_locations(self)
    def map_length(self)
    def map_width(self)
    def x_map_center(self)
    def y_map_center(self)
    def cell_rowcol_to_xy(self, rowcol_pos)
    def cell_xy_to_rowcol(self, xy_pos)
    def make_maze(cls, agent_xml_path, maze_map, maze_size_scaling, maze_height)
class MazeEnv(GoalEnv)
    def __init__(self, agent_xml_path, reward_type, continuing_task, reset_target, maze_map, maze_size_scaling, maze_height, position_noise_range)
    def close(self)
    def generate_target_goal(self)
    def generate_reset_pos(self)
    def reset(self)
    def add_xy_position_noise(self, xy_pos)
    def compute_reward(self, achieved_goal, desired_goal, info)
    def compute_terminated(self, achieved_goal, desired_goal, info)
    def update_goal(self, achieved_goal)
    def compute_truncated(self, achieved_goal, desired_goal, info)
    def update_target_site_pos(self, pos)

```python
def compute_reward(
        self, achieved_goal: np.ndarray, desired_goal: np.ndarray, info
    ) -> float:
        distance = np.linalg.norm(achieved_goal - desired_goal, axis=-1)
        if self.reward_type == "dense":
            return np.exp(-distance)
        elif self.reward_type == "sparse":
            return (distance <= 0.45).astype(np.float64)
```
```

### gymnasium_robotics/envs/maze/point.py

```
"""A point mass environment with Gymnasium API for the Gymnasium-Robotics PointMaze environments.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files: `maps.py`, `maze_env.py`, `point_env.py`, and `point_maze_env.py`.
As well as adding support for the Gymnasium API.

This project"""
class PointEnv(MujocoEnv)
    def __init__(self, xml_file)
    def reset_model(self)
    def step(self, action)
    def _get_obs(self)
    def _clip_velocity(self)

```python
def _get_obs(self) -> np.ndarray:
        return np.concatenate([self.data.qpos, self.data.qvel]).ravel(), {}
```
```

### gymnasium_robotics/envs/maze/point_maze.py

```
"""A point mass maze environment with Gymnasium API.

The code is inspired by the D4RL repository hosted on GitHub (https://github.com/Farama-Foundation/D4RL), published in the paper
'D4RL: Datasets for Deep Data-Driven Reinforcement Learning' by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine.

Original Author of the code: Justin Fu

The modifications made involve organizing the code into different files: `maps.py`, `maze_env.py`, `point_env.py`, and `point_maze_env.py`.
As well as adding support for the Gymnasium API.

This project is covered by the Apache 2.0 License."""
class PointMazeEnv(MazeEnv, EzPickle)
    """### Description

This environment was refactored from the [D4RL](https://github.com/Farama-Foundation/D4RL) repository, introduced by Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine
in ["D4RL: Datasets for Deep Data-Driven Reinforcement Learning"](https://arxiv.org/abs/2004.07"""
    def __init__(self, maze_map, render_mode, reward_type, continuing_task, reset_target)
    def reset(self)
    def step(self, action)
    def update_target_site_pos(self)
    def _get_obs(self, point_obs)
    def render(self)
    def close(self)
    def model(self)
    def data(self)

```python
def _get_obs(self, point_obs) -> Dict[str, np.ndarray]:
        achieved_goal = point_obs[:2]
        return {
            "observation": point_obs.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```
```

### gymnasium_robotics/envs/mujoco/ant_v2.py

```
class AntEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        return np.concatenate(
            [
                self.sim.data.qpos.flat[2:],
                self.sim.data.qvel.flat,
                np.clip(self.sim.data.cfrc_ext, -1, 1).flat,
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/ant_v3.py

```
class AntEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, ctrl_cost_weight, contact_cost_weight, healthy_reward, terminate_when_unhealthy, healthy_z_range, contact_force_range, reset_noise_scale, exclude_current_positions_from_observation)
    def healthy_reward(self)
    def control_cost(self, action)
    def contact_forces(self)
    def contact_cost(self)
    def is_healthy(self)
    def terminated(self)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def healthy_reward(self):
        return (
            float(self.is_healthy or self._terminate_when_unhealthy)
            * self._healthy_reward
        )
```

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = self.sim.data.qvel.flat.copy()
        contact_force = self.contact_forces.flat.copy()

        if self._exclude_current_positions_from_observation:
            position = position[2:]

        observations = np.concatenate((position, velocity, contact_force))

        return observations
```
```

### gymnasium_robotics/envs/mujoco/half_cheetah_v2.py

```
class HalfCheetahEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        return np.concatenate(
            [
                self.sim.data.qpos.flat[1:],
                self.sim.data.qvel.flat,
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/half_cheetah_v3.py

```
class HalfCheetahEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, forward_reward_weight, ctrl_cost_weight, reset_noise_scale, exclude_current_positions_from_observation)
    def control_cost(self, action)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = self.sim.data.qvel.flat.copy()

        if self._exclude_current_positions_from_observation:
            position = position[1:]

        observation = np.concatenate((position, velocity)).ravel()
        return observation
```
```

### gymnasium_robotics/envs/mujoco/hopper_v2.py

```
class HopperEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        return np.concatenate(
            [self.sim.data.qpos.flat[1:], np.clip(self.sim.data.qvel.flat, -10, 10)]
        )
```
```

### gymnasium_robotics/envs/mujoco/hopper_v3.py

```
class HopperEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, forward_reward_weight, ctrl_cost_weight, healthy_reward, terminate_when_unhealthy, healthy_state_range, healthy_z_range, healthy_angle_range, reset_noise_scale, exclude_current_positions_from_observation)
    def healthy_reward(self)
    def control_cost(self, action)
    def is_healthy(self)
    def terminated(self)
    def _get_obs(self)
    def step(self, action)
    def reset_model(self)
    def viewer_setup(self)

```python
def healthy_reward(self):
        return (
            float(self.is_healthy or self._terminate_when_unhealthy)
            * self._healthy_reward
        )
```

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = np.clip(self.sim.data.qvel.flat.copy(), -10, 10)

        if self._exclude_current_positions_from_observation:
            position = position[1:]

        observation = np.concatenate((position, velocity)).ravel()
        return observation
```
```

### gymnasium_robotics/envs/mujoco/humanoid_v2.py

```
def mass_center(model, sim)
class HumanoidEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def _get_obs(self)
    def step(self, a)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        data = self.sim.data
        return np.concatenate(
            [
                data.qpos.flat[2:],
                data.qvel.flat,
                data.cinert.flat,
                data.cvel.flat,
                data.qfrc_actuator.flat,
                data.cfrc_ext.flat,
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/humanoid_v3.py

```
def mass_center(model, sim)
class HumanoidEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, forward_reward_weight, ctrl_cost_weight, contact_cost_weight, contact_cost_range, healthy_reward, terminate_when_unhealthy, healthy_z_range, reset_noise_scale, exclude_current_positions_from_observation)
    def healthy_reward(self)
    def control_cost(self, action)
    def contact_cost(self)
    def is_healthy(self)
    def terminated(self)
    def _get_obs(self)
    def step(self, action)
    def reset_model(self)
    def viewer_setup(self)

```python
def healthy_reward(self):
        return (
            float(self.is_healthy or self._terminate_when_unhealthy)
            * self._healthy_reward
        )
```

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = self.sim.data.qvel.flat.copy()

        com_inertia = self.sim.data.cinert.flat.copy()
        com_velocity = self.sim.data.cvel.flat.copy()

        actuator_forces = self.sim.data.qfrc_actuator.flat.copy()
        external_contact_forces = self.sim.data.cfrc_ext.flat.copy()

        if self._exclude_current_positions_from_observation:
            position = position[2:]

        return np.concatenate(
            (
                position,
                velocity,
                com_inertia,
                com_velocity,
                actuator_forces,
                external_contact_forces,
            )
        )
```
```

### gymnasium_robotics/envs/mujoco/humanoidstandup_v2.py

```
class HumanoidStandupEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def _get_obs(self)
    def step(self, a)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        data = self.sim.data
        return np.concatenate(
            [
                data.qpos.flat[2:],
                data.qvel.flat,
                data.cinert.flat,
                data.cvel.flat,
                data.qfrc_actuator.flat,
                data.cfrc_ext.flat,
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/inverted_double_pendulum_v2.py

```
class InvertedDoublePendulumEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        return np.concatenate(
            [
                self.sim.data.qpos[:1],  # cart x pos
                np.sin(self.sim.data.qpos[1:]),  # link angles
                np.cos(self.sim.data.qpos[1:]),
                np.clip(self.sim.data.qvel, -10, 10),
                np.clip(self.sim.data.qfrc_constraint, -10, 10),
            ]
        ).ravel()
```
```

### gymnasium_robotics/envs/mujoco/inverted_pendulum_v2.py

```
class InvertedPendulumEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def reset_model(self)
    def _get_obs(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        return np.concatenate([self.sim.data.qpos, self.sim.data.qvel]).ravel()
```
```

### gymnasium_robotics/envs/mujoco/mujoco_py_env.py

```
def expand_model_path(model_path)
class BaseMujocoPyEnv(?)
    """Superclass for all MuJoCo environments."""
    def __init__(self, model_path, frame_skip, observation_space, render_mode, width, height, camera_id, camera_name)
    def _set_action_space(self)
    def step(self, action)
    def reset_model(self)
    def _initialize_simulation(self)
    def _reset_simulation(self)
    def _step_mujoco_simulation(self, ctrl, n_frames)
    def render(self)
    def _get_reset_info(self)
    def reset(self)
    def set_state(self, qpos, qvel)
    def dt(self)
    def do_simulation(self, ctrl, n_frames)
    def close(self)
    def get_body_com(self, body_name)
    def state_vector(self)
class MuJocoPyEnv(BaseMujocoPyEnv)
    def __init__(self, model_path, frame_skip, observation_space, render_mode, width, height, camera_id, camera_name)
    def _initialize_simulation(self)
    def _reset_simulation(self)
    def set_state(self, qpos, qvel)
    def get_body_com(self, body_name)
    def _step_mujoco_simulation(self, ctrl, n_frames)
    def render(self)
    def _get_viewer(self, mode)
    def close(self)
    def viewer_setup(self)
```

### gymnasium_robotics/envs/mujoco/pusher_v2.py

```
class PusherEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def viewer_setup(self)
    def reset_model(self)
    def _get_obs(self)

```python
def _get_obs(self):
        return np.concatenate(
            [
                self.sim.data.qpos.flat[:7],
                self.sim.data.qvel.flat[:7],
                self.get_body_com("tips_arm"),
                self.get_body_com("object"),
                self.get_body_com("goal"),
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/reacher_v2.py

```
class ReacherEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def viewer_setup(self)
    def reset_model(self)
    def _get_obs(self)

```python
def _get_obs(self):
        theta = self.sim.data.qpos.flat[:2]
        return np.concatenate(
            [
                np.cos(theta),
                np.sin(theta),
                self.sim.data.qpos.flat[2:],
                self.sim.data.qvel.flat[:2],
                self.get_body_com("fingertip") - self.get_body_com("target"),
            ]
        )
```
```

### gymnasium_robotics/envs/mujoco/swimmer_v2.py

```
class SwimmerEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        qpos = self.sim.data.qpos
        qvel = self.sim.data.qvel
        return np.concatenate([qpos.flat[2:], qvel.flat])
```
```

### gymnasium_robotics/envs/mujoco/swimmer_v3.py

```
class SwimmerEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, forward_reward_weight, ctrl_cost_weight, reset_noise_scale, exclude_current_positions_from_observation)
    def control_cost(self, action)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = self.sim.data.qvel.flat.copy()

        if self._exclude_current_positions_from_observation:
            position = position[2:]

        observation = np.concatenate([position, velocity]).ravel()
        return observation
```
```

### gymnasium_robotics/envs/mujoco/walker2d_v2.py

```
class Walker2dEnv(MuJocoPyEnv, EzPickle)
    def __init__(self)
    def step(self, a)
    def _get_obs(self)
    def reset_model(self)
    def viewer_setup(self)

```python
def _get_obs(self):
        qpos = self.sim.data.qpos
        qvel = self.sim.data.qvel
        return np.concatenate([qpos[1:], np.clip(qvel, -10, 10)]).ravel()
```
```

### gymnasium_robotics/envs/mujoco/walker2d_v3.py

```
class Walker2dEnv(MuJocoPyEnv, EzPickle)
    def __init__(self, xml_file, forward_reward_weight, ctrl_cost_weight, healthy_reward, terminate_when_unhealthy, healthy_z_range, healthy_angle_range, reset_noise_scale, exclude_current_positions_from_observation)
    def healthy_reward(self)
    def control_cost(self, action)
    def is_healthy(self)
    def terminated(self)
    def _get_obs(self)
    def step(self, action)
    def reset_model(self)
    def viewer_setup(self)

```python
def healthy_reward(self):
        return (
            float(self.is_healthy or self._terminate_when_unhealthy)
            * self._healthy_reward
        )
```

```python
def _get_obs(self):
        position = self.sim.data.qpos.flat.copy()
        velocity = np.clip(self.sim.data.qvel.flat.copy(), -10, 10)

        if self._exclude_current_positions_from_observation:
            position = position[1:]

        observation = np.concatenate((position, velocity)).ravel()
        return observation
```
```

### gymnasium_robotics/envs/multiagent_mujoco/__init__.py

```
"""See the [Doc Page](https://robotics.farama.org/envs/fetch/MaMuJoCo)."""
```

### gymnasium_robotics/envs/multiagent_mujoco/coupled_half_cheetah.py

```
"""File for CoupledHalfCheetahEnv.

This file is originally from the `schroederdewitt/multiagent_mujoco` repository hosted on GitHub
(https://github.com/schroederdewitt/multiagent_mujoco/blob/master/multiagent_mujoco/coupled_half_cheetah.py)
Original Author: Schroeder de Witt

 - General code cleanup, factorization, type hinting, adding documentation and comments
- updated API to Gymnasium.MuJoCo v4
- increase returned info
- fixed `_get_obs()` (now also returns tendon related observations)
- renamed CoupledHalfCheetah -> CoupledHalfCheetahEnv"""
class CoupledHalfCheetahEnv(MujocoEnv, EzPickle)
    """Class for CoupledHalfCheetah mujoco environment.

## Description
This environment was first (half-)implemented in the [original_mamujoco](https://github.com/schroederdewitt/multiagent_mujoco)
This environment consists of 2 half cheetahs coupled by an elastic tendon.

## Action Space
The action space"""
    def __init__(self, render_mode)
    def step(self, action)
    def _get_obs(self)
    def reset_model(self)

```python
def _get_obs(self) -> np.ndarray:
        # NOTE: does not return tendon data
        return np.concatenate(
            [
                self.data.qpos.flat[1:9],  # exclude rootx0
                self.data.qpos.flat[10:18],  # exclude rootx1
                self.data.qvel.flat,
                self.data.ten_J[0][:2],
                self.data.ten_J[0][9:11],
                self.data.ten_length,
                self.data.ten_velocity,
            ]
        )
```
```

### gymnasium_robotics/envs/multiagent_mujoco/many_segment_ant.py

```
"""File for ManySegmentAntEnv.

This file is originally from the `schroederdewitt/multiagent_mujoco` repository hosted on GitHub
(https://github.com/schroederdewitt/multiagent_mujoco/blob/master/multiagent_mujoco/manyagent_ant.py)
Original Author: Schroeder de Witt

 - General code cleanup, factorization, type hinting, adding documentation and comments
 - Removed the class (but kept the `gen_asset` function)"""
def gen_asset(n_segs, asset_path)
```

### gymnasium_robotics/envs/multiagent_mujoco/many_segment_swimmer.py

```
"""File for ManySegmentSwimmerEnv.

This file is originally from the `schroederdewitt/multiagent_mujoco` repository hosted on GitHub
(https://github.com/schroederdewitt/multiagent_mujoco/blob/master/multiagent_mujoco/manyagent_swimmer.py)
Original Author: Schroeder de Witt

 - General code cleanup, factorization, type hinting, adding documentation and comments
 - Removed the class (but kept the `gen_asset` function)"""
def gen_asset(n_segs, asset_path)
```

### gymnasium_robotics/envs/multiagent_mujoco/mujoco_multi.py

```
"""Main file for MaMuJoCo includes the MultiAgentMujocoEnv class.

This file is originally from the `schroederdewitt/multiagent_mujoco` repository hosted on GitHub
(https://github.com/schroederdewitt/multiagent_mujoco/blob/master/multiagent_mujoco/mujoco_multi.py)
Original Author: Schroeder de Witt

Then Modified by @Kallinteris-Andreas for this project
changes:
 - General code cleanup, factorization, type hinting, adding documentation and code comments.
 - Now uses PettingZoo APIs instead of an original API.
 - Now supports custom agent factorizations.
 - Added `gym_env` argument, which can be u"""
class MultiAgentMujocoEnv(ParallelEnv)
    """Class for multi agent factorizing mujoco environments.

Doc can be found at (https://robotics.farama.org/envs/mamujoco/)"""
    def __init__(self, scenario, agent_conf, agent_obsk, agent_factorization, local_categories, global_categories, render_mode, gym_env)
    def _create_base_gym_env(self, scenario, agent_conf, render_mode)
    def step(self, actions)
    def map_local_actions_to_global_action(self, actions)
    def map_global_action_to_local_actions(self, action)
    def map_global_state_to_local_observations(self, global_state)
    def map_local_observations_to_global_state(self, local_observation)
    def create_observation_mapping(self)
    def observation_space(self, agent)
    def action_space(self, agent)
    def state(self)
    def _get_obs(self)
    def _get_obs_agent(self, agent_id, data)
    def reset(self, seed, options)
    def render(self)
    def close(self)
    def _generate_local_categories(self, scenario)

```python
def map_global_state_to_local_observations(
        self, global_state: np.ndarray[np.float64]
    ) -> dict[str, np.ndarray[np.float64]]:
        """Maps single agent observation into multi agent observation spaces.

        Args:
            global_state:
                the global_state (generated from MaMuJoCo.state())

        Returns:
            A dictionary of states that would be observed by each agent given the 'global_state'
        """
        assert (
            self.observation_factorization is not None
        ), "to map states the MuJoCo environment must have `observation_structure` member variable"
        global_state = np.array(global_state)

        local_observation = {}
        for agent, partition in self.observation_factorization.items():
            local_observation[agent] = global_state[partition]

        # assert sizes
        assert len(local_observation) == len(self.action_spaces)
        for agent in self.possible_agents:
            assert (
                len(local_observation[agent]) == self.observation_spaces[agent].shape[0]
            )

        return local_observation
```

```python
def map_local_observations_to_global_state(
        self, local_observation: np.ndarray[np.float64]
    ) -> np.ndarray[np.float64]:
        """Maps multi agent observations into single agent observation space.

        Args:
            local_obserations:
                the local observation of each agents (generated from MaMuJoCo.step())

        Returns:
            the global observations that correspond to a single agent (what you would get with MaMuJoCo.state())
        """
        assert (
            self.observation_factorization is not None
        ), "to map states the MuJoCo environment must have `observation_structure` member variable"

        global_observation = (
            np.zeros((self.single_agent_env.observation_space.shape[0],)) + np.nan
        )

        for agent, partition in self.observation_factorization.items():
            for local_idx, global_idx in enumerate(partition):
                assert (
                    np.isnan(global_observation[global_idx])
                    or global_observation[global_idx]
                    == local_observation[agent][local_idx]
                ), "FATAL: At least one gym_env observation is doubly defined!"
                global_observation[global_idx] = local_observation[agent][local_idx]

        assert not np.isnan(
            global_observation
        ).any(), "FATAL: At least one gym_env observation is undefined, observations can not be mapped."
        return global_observation
```

```python
def create_observation_mapping(self) -> dict[str, np.ndarray[np.float64]]:
        """Creates a cache of the observation factorization.

        The cache is intended to be used with `map_global_state_to_local_observations` & `map_local_observations_to_global_state`.

        Returns:
            A cache that indexes global osbervations to local.
        """
        if self.agent_obsk is None:
            return {
                self.possible_agents[0]: np.arange(
                    self.single_agent_env.observation_space.shape[0]
                )
            }
        if not hasattr(self.single_agent_env.unwrapped, "observation_structure"):
            return None

        class data_struct:
            def __init__(self, qpos, qvel, cinert, cvel, qfrc_actuator, cfrc_ext):
                self.qpos = qpos
                self.qvel = qvel
                self.cinert = cinert
                self.cvel = cvel
                self.qfrc_actuator = qfrc_actuator
                self.cfrc_ext = cfrc_ext

        obs_struct = self.single_agent_env.unwrapped.observation_structure
        qpos_end_index = obs_struct["qpos"]
        qvel_end_index = qpos_end_index + obs_struct["qvel"]
        cinert_end_index = qvel_end_index + obs_struct.get("cinert", 0)
        cvel_end_index = cinert_end_index + obs_struct.get("cvel", 0)
        qfrc_actuator_end_index = cvel_end_index + obs_struct.get("qfrc_actuator", 0)
        cfrc_ext_end_index = qfrc_actuator_end_index + obs_struct.get("cfrc_ext", 0)

        global_index = np.arange(self.single_agent_env.observation_space.shape[0])
        assert len(global_index) == cfrc_ext_end_index, "wrong indexing"

        mujoco_data = data_struct(
            qpos=np.concatenate(
                [
                    np.zeros(obs_struct["skipped_qpos"], dtype=np.int64),
                    global_index[0:qpos_end_index],
                ]
            ),
            qvel=np.array(global_index[qpos_end_index:qvel_end_index]),
            cinert=np.concatenate(
                [
                    np.zeros(10, dtype=np.int64),
                    global_index[qvel_end_index:cinert_end_index],
                ]
            ),
            cvel=np.concatenate(
                [
                    np.zeros(6, dtype=np.int64),
                    global_index[cinert_end_index:cvel_end_index],
                ]
            ),
            qfrc_actuator=np.concatenate(
                [
                    np.zeros(6, dtype=np.int64),
                    global_index[cvel_end_index:qfrc_actuator_end_index],
                ]
            ),
            cfrc_ext=np.concatenate(
                [
                    np.zeros(6, dtype=np.int64),
                    global_index[qfrc_actuator_end_index:cfrc_ext_end_index],
                ]
            ),
        )

        if len(mujoco_data.cinert) > 10:
            mujoco_data.cinert = np.reshape(
                mujoco_data.cinert, self.single_agent_env.unwrapped.data.cinert.shape
            )
        if len(mujoco_data.cvel) > 6:
            mujoco_data.cvel = np.reshape(
                mujoco_data.cvel, self.single_agent_env.unwrapped.data.cvel.shape
            )
        if len(mujoco_data.cfrc_ext) > 6:
            mujoco_data.cfrc_ext = np.reshape(
                mujoco_data.cfrc_ext,
                self.single_agent_env.unwrapped.data.cfrc_ext.shape,
            )

        assert len(self.single_agent_env.unwrapped.data.qpos.flat) == len(
            mujoco_data.qpos
        )
        assert len(self.single_agent_env.unwrapped.data.qvel.flat) == len(
            mujoco_data.qvel
        )

        local_index = {}
        for agent_id, agent in enumerate(self.possible_agents):
            local_index[agent] = self._get_obs_agent(agent_id, mujoco_data)
        return local_index
```

```python
def observation_space(self, agent: str) -> gymnasium.spaces.Box:
        """See [pettingzoo.utils.env.ParallelEnv.observation_space](https://pettingzoo.farama.org/api/parallel/#pettingzoo.utils.env.ParallelEnv.observation_space)."""
        return self.observation_spaces[agent]
```

```python
def _get_obs(self) -> dict[str, np.ndarray]:
        """Returns: all agent's observations in a dict[str, ActionType]."""
        # dev NOTE: ignores `self.single_agent_env._get_obs()` and builds observations using obsk.build_obs()
        observations = {}
        for agent_id, agent in enumerate(self.possible_agents):
            observations[agent] = self._get_obs_agent(agent_id)
        return observations
```

```python
def _get_obs_agent(self, agent_id: int, data=None) -> np.ndarray:
        """Get the observation of single agent.

        Args:
            agent_id: The id in self.possible_agents.values()
            data: An optional overwrite of the MuJoCo data, defaults to the data at the current time step

        Returns:
            The observation of the agent given the data
        """
        if self.agent_obsk is None:
            return self.single_agent_env.unwrapped._get_obs()

        index_only = True
        if data is None:
            data = self.single_agent_env.unwrapped.data
            index_only = False

        return build_obs(
            data,
            self.k_dicts[agent_id],
            self.local_categories,
            self.mujoco_globals,
            self.global_categories,
            index_only,
        )
```
```

### gymnasium_robotics/envs/multiagent_mujoco/obsk.py

```
"""file Containing utily functions for MaMuJoCo.

This file is originally from the `schroederdewitt/multiagent_mujoco` repository hosted on GitHub
(https://github.com/schroederdewitt/multiagent_mujoco/blob/master/multiagent_mujoco/obsk.py)
Original Author: Schroeder de Witt

Then Modified by @Kallinteris-Andreas for this project
changes:
 -  General code cleanup, factorization, type hinting, adding documentation and code comments
 - `build_obs`: fixed global observations, fixed body observations (cvel, cinert, cfrc_ext), how uses mujoco.data, instead of gym.env
 - `HalfCheetah`: fix action orderi"""
class Node()
    """A node of the mujoco graph representing a single body part and it's corresponding single action & observetions."""
    def __init__(self, label, qpos_ids, qvel_ids, act_ids, body_fn, bodies, extra_obs, tendons)
    def __str__(self)
    def __repr__(self)
class HyperEdge()
    """A collection of nodes, that are fully connected (with edges).

If a HyperEdge consists of 2 Nodes, then it is simply an Edge of those Nodes.

More at: https://en.wikipedia.org/wiki/Hypergraph"""
    def __init__(self)
    def __contains__(self, item)
    def __str__(self)
    def __repr__(self)
def get_joints_at_kdist(agent_partition, hyperedges, k)
def build_obs(data, k_dict, local_categories, global_nodes, global_categories, ignore_body_fn)
def get_parts_and_edges(label, partitioning)
```

### gymnasium_robotics/envs/robot_env.py

```
class BaseRobotEnv(GoalEnv)
    """Superclass for all MuJoCo fetch and hand robotic environments."""
    def __init__(self, model_path, initial_qpos, n_actions, n_substeps, render_mode, width, height)
    def compute_terminated(self, achieved_goal, desired_goal, info)
    def compute_truncated(self, achieved_goal, desired_goal, info)
    def step(self, action)
    def reset(self)
    def _mujoco_step(self, action)
    def _reset_sim(self)
    def _initialize_simulation(self)
    def _get_obs(self)
    def _set_action(self, action)
    def _is_success(self, achieved_goal, desired_goal)
    def _sample_goal(self)
    def _env_setup(self, initial_qpos)
    def _render_callback(self)
    def _step_callback(self)
class MujocoRobotEnv(BaseRobotEnv)
    """Robot base class for fetch and hand environment versions that depend on new mujoco bindings from Deepmind."""
    def __init__(self, default_camera_config)
    def _initialize_simulation(self)
    def _reset_sim(self)
    def render(self)
    def close(self)
    def dt(self)
    def _mujoco_step(self, action)
class MujocoPyRobotEnv(BaseRobotEnv)
    """Robot base class for fetch and hand environment versions that depend on mujoco_py bindings."""
    def __init__(self)
    def _initialize_simulation(self)
    def _reset_sim(self)
    def render(self)
    def close(self)
    def _get_viewer(self, mode)
    def dt(self)
    def _mujoco_step(self, action)
    def _viewer_setup(self)

```python
def _get_obs(self):
        """Returns the observation."""
        raise NotImplementedError()
```
```

### gymnasium_robotics/envs/shadow_dexterous_hand/hand_env.py

```
def get_base_hand_env(RobotEnvClass)
class MujocoHandEnv(?)
    def __init__(self, default_camera_config)
    def _set_action(self, action)
class MujocoPyHandEnv(?)
    """Base class for all Hand environments that use mujoco-py as the python bindings."""
    def _set_action(self, action)
    def _get_palm_xpos(self)
    def _viewer_setup(self)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate.py

```
def quat_from_angle_and_axis(angle, axis)
def get_base_manipulate_env(HandEnvClass)
class MujocoManipulateEnv(?)
    def _get_achieved_goal(self)
    def _env_setup(self, initial_qpos)
    def _reset_sim(self)
    def _sample_goal(self)
    def _render_callback(self)
    def _get_obs(self)
class MujocoPyManipulateEnv(?)
    def _get_achieved_goal(self)
    def _env_setup(self, initial_qpos)
    def _reset_sim(self)
    def _sample_goal(self)
    def _render_callback(self)
    def _get_obs(self)

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(
            self.model, self.data, self._model_names.joint_names
        )
        object_qvel = self._utils.get_joint_qvel(self.model, self.data, "object:joint")
        achieved_goal = (
            self._get_achieved_goal().ravel()
        )  # this contains the object position + rotation

        observation = np.concatenate(
            [robot_qpos, robot_qvel, object_qvel, achieved_goal]
        )
        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.ravel().copy(),
        }
```

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(self.sim)
        object_qvel = self.sim.data.get_joint_qvel("object:joint")

        achieved_goal = (
            self._get_achieved_goal().ravel()
        )  # this contains the object position + rotation
        observation = np.concatenate(
            [robot_qpos, robot_qvel, object_qvel, achieved_goal]
        )
        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.ravel().copy(),
        }
```

```python
def compute_reward(self, achieved_goal, desired_goal, info):
            if self.reward_type == "sparse":
                success = self._is_success(achieved_goal, desired_goal).astype(
                    np.float32
                )
                return success - 1.0
            else:
                d_pos, d_rot = self._goal_distance(achieved_goal, desired_goal)
                # We weigh the difference in position to avoid that `d_pos` (in meters) is completely
                # dominated by `d_rot` (in radians).
                return -(10.0 * d_pos + d_rot)
```
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_block.py

```
class MujocoHandBlockEnv(MujocoManipulateEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The environment is based on the same robot hand as in the `HandReach` environment, the [Shadow Dexterous Hand](http"""
    def __init__(self, target_position, target_rotation, reward_type)
class MujocoPyHandBlockEnv(MujocoPyManipulateEnv, EzPickle)
    def __init__(self, target_position, target_rotation, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_block_touch_sensors.py

```
class MujocoHandBlockTouchSensorsEnv(MujocoManipulateTouchSensorsEnv, EzPickle)
    """## Description

This environment was introduced in ["Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks"](https://www.frontiersin.org/articles/10.3389/frobt.2021.538773/full).

The environment is base"""
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
class MujocoPyHandBlockTouchSensorsEnv(MujocoPyManipulateTouchSensorsEnv, EzPickle)
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_egg.py

```
class MujocoHandEggEnv(MujocoManipulateEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The environment is based on the same robot hand as in the `HandReach` environment, the [Shadow Dexterous Hand](http"""
    def __init__(self, target_position, target_rotation, reward_type)
class MujocoPyHandEggEnv(MujocoPyManipulateEnv, EzPickle)
    def __init__(self, target_position, target_rotation, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_egg_touch_sensors.py

```
class MujocoHandEggTouchSensorsEnv(MujocoManipulateTouchSensorsEnv, EzPickle)
    """## Description

This environment was introduced in ["Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks"](https://www.frontiersin.org/articles/10.3389/frobt.2021.538773/full).

The environment is base"""
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
class MujocoPyHandEggTouchSensorsEnv(MujocoPyManipulateTouchSensorsEnv, EzPickle)
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_pen.py

```
class MujocoHandPenEnv(MujocoManipulateEnv, EzPickle)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The environment is based on the same robot hand as in the `HandReach` environment, the [Shadow Dexterous Hand](http"""
    def __init__(self, target_position, target_rotation, reward_type)
class MujocoPyHandPenEnv(MujocoPyManipulateEnv, EzPickle)
    def __init__(self, target_position, target_rotation, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_pen_touch_sensors.py

```
class MujocoHandPenTouchSensorsEnv(MujocoManipulateTouchSensorsEnv, EzPickle)
    """## Description

This environment was introduced in ["Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks"](https://www.frontiersin.org/articles/10.3389/frobt.2021.538773/full).

The environment is base"""
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
class MujocoPyHandPenTouchSensorsEnv(MujocoPyManipulateTouchSensorsEnv, EzPickle)
    def __init__(self, target_position, target_rotation, touch_get_obs, reward_type)
```

### gymnasium_robotics/envs/shadow_dexterous_hand/manipulate_touch_sensors.py

```
class MujocoManipulateTouchSensorsEnv(MujocoManipulateEnv)
    def __init__(self, target_position, target_rotation, target_position_range, reward_type, initial_qpos, randomize_initial_position, randomize_initial_rotation, distance_threshold, rotation_threshold, n_substeps, relative_control, ignore_z_target_rotation, touch_visualisation, touch_get_obs)
    def _render_callback(self)
    def _get_obs(self)
class MujocoPyManipulateTouchSensorsEnv(MujocoPyManipulateEnv)
    def __init__(self, target_position, target_rotation, target_position_range, reward_type, initial_qpos, randomize_initial_position, randomize_initial_rotation, distance_threshold, rotation_threshold, n_substeps, relative_control, ignore_z_target_rotation, touch_visualisation, touch_get_obs)
    def _render_callback(self)
    def _get_obs(self)

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(
            self.model, self.data, self._model_names.joint_names
        )
        object_qvel = self._utils.get_joint_qvel(self.model, self.data, "object:joint")

        achieved_goal = (
            self._get_achieved_goal().ravel()
        )  # this contains the object position + rotation
        touch_values = []  # get touch sensor readings. if there is one, set value to 1

        if self.touch_get_obs == "sensordata":
            touch_values = self.data.sensordata[self._touch_sensor_id]
        elif self.touch_get_obs == "boolean":
            touch_values = self.data.sensordata[self._touch_sensor_id] > 0.0
        elif self.touch_get_obs == "log":
            touch_values = np.log(self.data.sensordata[self._touch_sensor_id] + 1.0)
        observation = np.concatenate(
            [robot_qpos, robot_qvel, object_qvel, achieved_goal, touch_values]
        )

        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.ravel().copy(),
        }
```

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(self.sim)
        object_qvel = self.sim.data.get_joint_qvel("object:joint")

        achieved_goal = (
            self._get_achieved_goal().ravel()
        )  # this contains the object position + rotation
        touch_values = []  # get touch sensor readings. if there is one, set value to 1

        if self.touch_get_obs == "sensordata":
            touch_values = self.sim.data.sensordata[self._touch_sensor_id]
        elif self.touch_get_obs == "boolean":
            touch_values = self.sim.data.sensordata[self._touch_sensor_id] > 0.0
        elif self.touch_get_obs == "log":
            touch_values = np.log(self.sim.data.sensordata[self._touch_sensor_id] + 1.0)

        observation = np.concatenate(
            [
                robot_qpos,
                robot_qvel,
                object_qvel,
                achieved_goal,
                touch_values,
            ]
        )

        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.ravel().copy(),
        }
```
```

### gymnasium_robotics/envs/shadow_dexterous_hand/reach.py

```
def goal_distance(goal_a, goal_b)
def get_base_hand_reach_env(HandEnvClass)
class MujocoHandReachEnv(?)
    """## Description

This environment was introduced in ["Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research"](https://arxiv.org/abs/1802.09464).

The environment is based on the [Shadow Dexterous Hand](https://www.shadowrobot.com/), which is an antropomorphic r"""
    def _get_achieved_goal(self)
    def _env_setup(self, initial_qpos)
    def _get_obs(self)
    def _render_callback(self)
class MujocoPyHandReachEnv(?)
    def _get_achieved_goal(self)
    def _env_setup(self, initial_qpos)
    def _get_obs(self)
    def _render_callback(self)

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(
            self.model, self.data, self._model_names.joint_names
        )
        achieved_goal = self._get_achieved_goal().ravel()
        observation = np.concatenate([robot_qpos, robot_qvel, achieved_goal])
        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```

```python
def _get_obs(self):
        robot_qpos, robot_qvel = self._utils.robot_get_obs(self.sim)

        achieved_goal = self._get_achieved_goal().ravel()
        observation = np.concatenate([robot_qpos, robot_qvel, achieved_goal])
        return {
            "observation": observation.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }
```

```python
def compute_reward(self, achieved_goal, desired_goal, info):
            d = goal_distance(achieved_goal, desired_goal)
            if self.reward_type == "sparse":
                return -(d > self.distance_threshold).astype(np.float32)
            else:
                return -d
```
```

### tests/envs/MaMuJoCo/test_MaMuJoCo.py

```
def test_general(observation_depth, task)
def test_action_and_observation_mapping(observation_depth, task)
def test_k_dict(task)
def test_swimmer_gen()

```python
def test_action_and_observation_mapping(observation_depth, task):
    """Assert that converting local <-> global <-> local observations/actions results in the same observation/actions."""
    test_env = mamujoco_v1.parallel_env(
        task.scenario, task.conf, agent_obsk=observation_depth, **task.kwargs
    )

    # assert action mapping
    global_action = test_env.single_agent_env.action_space.sample()
    assert (
        global_action
        == test_env.map_local_actions_to_global_action(
            test_env.map_global_action_to_local_actions(global_action)
        )
    ).all()

    if (
        task.scenario in ["Reacher", "Pusher", "CoupledHalfCheetah"]
        and task.conf is not None
    ):
        return  # observation mapping not implemented on those environments

    # assert observation mapping
    test_env.reset()
    global_observations = test_env.state()
    local_observations = test_env.unwrapped._get_obs()
    test_env.reset()
    data_equivalence(
        test_env.map_global_state_to_local_observations(global_observations),
        local_observations,
    )

    if (
        task.scenario in ["ManySegmentSwimmer", "ManySegmentAnt"]
        and task.conf is not None
    ):
        return  # mapping local to global observation is not supported on these environments since the local observation do not observe the full environment

    data_equivalence(
        test_env.map_local_observations_to_global_state(local_observations),
        global_observations,
    )

    # sanity check making sure the observation factorizations are sane
    for agent_obs_factor in test_env.observation_factorization.values():
        len(agent_obs_factor) != len(
            set(agent_obs_factor)
        ), "an agent observes the same state value multiple times"
```
```

### tests/envs/adroit_hand/test_adroit_hammer.py

```
def test_set_env_state_accepts_full_hammer_state(env_id)
```

### tests/envs/adroit_hand/test_adroit_relocate.py

```
def test_set_env_state_preserves_relocated_object_position()
```

### tests/envs/franka_kitchen/test_kitchen_env.py

```
def test_task_completion(remove_task_when_completed, terminate_on_tasks_completed)
```

### tests/envs/hand/test_manipulate.py

```
def test_serialize_deserialize(environment_id)
```

### tests/envs/hand/test_manipulate_touch_sensors.py

```
def test_serialize_deserialize(environment_id)
```

### tests/envs/hand/test_reach.py

```
def test_serialize_deserialize()
```

### tests/envs/maze/test_ant_maze.py

```
def test_reset(version)
def test_temp_xml_file_lifecycle(version)
```

### tests/envs/maze/test_point_maze.py

```
def test_reset()
def test_reset_cell()
def test_goal_cell()
```

### tests/envs/mujoco/test_mujoco_v3.py

```
def verify_environments_match(old_env_id, new_env_id, seed, num_actions)
def test_mujoco_v2_to_v3_conversion(env_name)
def test_mujoco_incompatible_v3_to_v2(env_name)
```

### tests/envs/mujoco/test_mujoco_v5.py

```
def test_verify_info_x_position(env_id)
def test_verify_info_y_position(env_id)
def test_verify_info_x_velocity(env_name, version)
def test_verify_info_y_velocity(env_id)
def test_verify_info_xy_velocity_xpos(env_id)
def test_verify_info_xy_velocity_com(env_id)
def test_set_state(version)
def test_distance_from_origin_info(env_id)
def test_model_sensors(version)
def test_reset_noise_scale(env_id)
```

### tests/test_envs.py

```
def test_env(spec)
def test_env_determinism_rollout(env_spec)
def test_mujoco_reset_state_seeding(env_spec)
def test_render_modes(spec)
def test_pickle_env(env_spec)
def test_robot_env_reset(spec)
```

### tests/test_goal_env_api.py

```
def test_goal_methods_take_the_documented_keywords(env_id, method)
```