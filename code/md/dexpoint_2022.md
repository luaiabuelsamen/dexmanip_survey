# dexpoint_2022

source: https://github.com/yzqin/dexpoint-release


commit: 17f1e238bb120d92baabe8207494d48476fea289


## README

# DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation 

[[Project Page]](https://yzqin.github.io/dexpoint/) [[Paper]](https://arxiv.org/abs/2211.09423) [[Poster]](https://docs.google.com/presentation/d/1dDtAPQ49k1emhETRPAib5R0wCGdwlz5l/edit?usp=sharing&ouid=108317450590466198031&rtpof=true&sd=true)[[ShapeNet Object Models]](https://drive.google.com/file/d/1liqE8Zin4tAlfFcJBIpT1Qn2Nyzl3Nke/view?usp=sharing)
-----

[DexPoint: Generalizable Point Cloud Reinforcement Learning for
Sim-to-Real Dexterous Manipulation ](https://yzqin.github.io/dexpoint/)

Yuzhe Qin*, Binghao Huang*, Zhao-Heng Yin, Hao Su, Xiaolong Wang, CoRL 2022.

DexPoint is a novel system and algorithm for RL from point cloud. This repo contains the simulated environment and
training code for DexPoint.

![Teaser](docs/teaser.png)

## Bibtex

```
@article{dexpoint,
  title          = {DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation },
  author         = {Qin, Yuzhe and Huang, Binghao and Yin, Zhao-Heng and Su, Hao and Wang, Xiaolong},
  journal        = {Conference on Robot Learning (CoRL)},
  year           = {2022},
}
```

## Installation

```shell
git clone git@github.com:yzqin/dexpoint-release.git
cd dexart-release
conda create --name dexpoint python=3.8
conda activate dexpoint
pip install -e .
```

Download data file for the scene
from [Google Drive Link](https://drive.google.com/file/d/1Xe3jgcIUZm_8yaFUsHnO7WJWr8cV41fE/view?usp=sharing).
Place the `day.ktx` at `assets/misc/ktx/day.ktx`.

```shell
pip install gdown
gdown https://drive.google.com/uc?id=1Xe3jgcIUZm_8yaFUsHnO7WJWr8cV41fE
```

## File Structure

- `dexpoint`: main content for the environment, utils, and other staff needs for RL training.
- `assets`: robot and object models, and other static files
- `example`: entry files to learn how to use the DexPoint environment
- `docker`: dockerfile that can create container to be used for headless training on server

## Quick Start

### Use DexPoint environment and extend it for your project

Run and explore the comments in the file below provided to familiarize yourself with the basic architecture of the
DexPoint environment. Check the printed messages to understand the observation, action, camera, and speed for these
environments.

- [state_only_env.py](example/example_use_state_only_env.py): minimal state only environment
- [example_use_pc_env.py](example/example_use_pc_env.py): minimal point cloud environment
- [example_use_imagination_env.py](example/example_use_imagination_env.py): point cloud environment with imagined point
  proposed
  in DexPoint
- [example_use_multi_camera_visual_env.py](example/example_use_multi_camera_visual_env.py): environment with multiple
  different visual modalities, including depth, rgb, segmentation. We provide it for your reference, although it is not
  used in DexPoint

The environment we used in the training of DexPoint paper can be found here
in [example_dexpoint_grasping.py](example/example_dexpoint_grasping.py).

### Training

Download the ShapeNet models from [Google Drive](https://drive.google.com/file/d/1liqE8Zin4tAlfFcJBIpT1Qn2Nyzl3Nke/view?usp=sharing) can place it inside the following directory `dexpoint-release/assets/shapenet/`.

The `DexPoint` repo is using the same training code as [DexArt](https://github.com/Kami-code/dexart-release) and environment interface for RL training. Please check the training code [here](https://github.com/Kami-code/dexart-release/tree/main/stable_baselines3) to train DexPoint with PPO.

## Acknowledgements

We would like to thank the following people for making this project possible:

- [Tongzhou Mu](https://cseweb.ucsd.edu//~t3mu/) and [Ruihan Yang](https://rchalyang.github.io/) for helpful discussion
  and feedback.
- [Fanbo Xiang](https://www.fbxiang.com/) for invaluable help on rendering.

### Example extension of DexPoint environment framework in other project

[DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects (CVPR 2023)](https://github.com/Kami-code/dexart-release):
extend DexPoint to articulated object manipulation.

[From One Hand to Multiple Hands: Imitation Learning for Dexterous Manipulation from Single-Camera Teleoperation (RA-L 2022)](https://github.com/yzqin/dex-hand-teleop):
use teleoperation for data collection in DexPoint environment.







## File tree (depth 3, assets pruned)

```
.editorconfig
.gitignore
CITATION.cff
LICENSE
README.md
dexpoint/
  __init__.py
  env/
    rl_env/
    sim_env/
  kinematics/
    __init__.py
    kinematics_helper.py
  real_world/
    __init__.py
    lab.py
    lab_door.py
    task_setting.py
  utils/
    __init__.py
    camera_utils.py
    common_robot_utils.py
    egad_object_utils.py
    mesh_utils.py
    model_utils.py
    physical_scene_utils.py
    pose_utils.py
    random_utils.py
    render_scene_utils.py
    shapenet_utils.py
    ycb_object_utils.py
docker/
  Dockerfile
example/
  example_dexpoint_grasping.py
  example_use_imagination_env.py
  example_use_multi_camera_visual_env.py
  example_use_pc_env.py
  example_use_state_only_env.py
pyproject.toml
setup.py
```

## Config files (0)


## Python signatures and reward/observation bodies (12 files)


### dexpoint/env/rl_env/allegro_env.py

```
class AllegroRLEnv(BaseRLEnv, ABC)
    """This base environment are design for RL with allegro hand, either flying allegro or allegro hand with robot arm.
It provides basic utilities based on the link name of Allegro hand and can not be used with other robot hand."""
    def __init__(self, use_gui, frame_skip, use_visual_obs)
    def setup_allegro(self, robot_name, root_frame)
    def reset_allegro(self)
```

### dexpoint/env/rl_env/base.py

```
def recover_action(action, limit)
class BaseRLEnv(BaseSimulationEnv, Env)
    def __init__(self, use_gui, frame_skip, use_visual_obs)
    def seed(self, seed)
    def get_observation(self)
    def get_reward(self, action)
    def get_info(self)
    def update_cached_state(self)
    def is_done(self)
    def action_dim(self)
    def horizon(self)
    def setup(self, robot_name)
    def free_sim_step(self, action)
    def arm_sim_step(self, action)
    def arm_kinematic_step(self, action)
    def reset_internal(self)
    def step(self, action)
    def setup_visual_obs_config(self, config)
    def setup_imagination_config(self, config)
    def update_imagination(self, reset_goal)
    def obs_dim(self)
    def get_robot_state(self)
    def get_oracle_state(self)
    def get_visual_observation(self)
    def get_camera_obs(self)
    def get_camera_to_robot_pose(self, camera_name)
    def action_space(self)
    def observation_space(self)
def compute_inverse_kinematics(delta_pose_world, palm_jacobian, damping)

```python
def get_observation(self):
        raise NotImplementedError
```

```python
def get_reward(self, action):
        pass
```

```python
def get_visual_observation(self):
        camera_obs = self.get_camera_obs()
        robot_obs = self.get_robot_state()
        oracle_obs = self.get_oracle_state()
        camera_obs.update(dict(state=robot_obs, oracle_state=oracle_obs))
        return camera_obs
```

```python
def observation_space(self):
        high = np.inf * np.ones(self.obs_dim)
        low = -high
        state_space = gym.spaces.Box(low=low, high=high)
        if not self.use_visual_obs:
            return state_space
        else:
            oracle_dim = len(self.get_oracle_state())
            oracle_space = gym.spaces.Box(low=-np.inf * np.ones(oracle_dim), high=np.inf * np.ones(oracle_dim))
            obs_dict = {"state": state_space, "oracle_state": oracle_space}
            for cam_name, cam_cfg in self.camera_infos.items():
                cam = self.cameras[cam_name]
                resolution = (cam.height, cam.width)
                for modality_name in cam_cfg.keys():
                    key_name = f"{cam_name}-{modality_name}"
                    if modality_name == "rgb":
                        spec = gym.spaces.Box(low=0, high=1, shape=resolution + (3,))
                    elif modality_name == "depth":
                        spec = gym.spaces.Box(low=0, high=MAX_DEPTH_RANGE, shape=resolution + (1,))
                    elif modality_name == "point_cloud":
                        spec = gym.spaces.Box(low=-np.inf, high=np.inf,
                                              shape=(cam_cfg[modality_name]["num_points"],) + (3,))
                    elif modality_name == "segmentation":
                        spec = gym.spaces.Box(low=0, high=255, shape=resolution + (2,), dtype=np.uint8)
                    else:
                        raise RuntimeError("What happen? you should not see this error!")
                    obs_dict[key_name] = spec

            if len(self.imagination_infos) > 0:
                self.update_imagination(reset_goal=True)
                for img_name, points in self.imaginations.items():
                    num_points = points.shape[0]
                    obs_dict[img_name] = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(num_points, 3))

            return gym.spaces.Dict(obs_dict)
```
```

### dexpoint/env/rl_env/pc_processing.py

```
def process_relocate_pc(cloud, camera_pose, num_points, np_random, segmentation)
def process_relocate_pc_noise(cloud, camera_pose, num_points, np_random, segmentation, noise_level)
def add_gaussian_noise(cloud, np_random, noise_level)
```

### dexpoint/env/rl_env/relocate_env.py

```
class AllegroRelocateRLEnv(LabRelocateEnv, BaseRLEnv)
    def __init__(self, use_gui, frame_skip, robot_name, rotation_reward_weight, object_category, object_name, randomness_scale, friction, root_frame)
    def update_cached_state(self)
    def get_oracle_state(self)
    def get_robot_state(self)
    def get_reward(self, action)
    def reset(self)
    def is_done(self)
    def horizon(self)
def main_env()

```python
def get_reward(self, action):
        finger_object_dist = np.linalg.norm(self.object_in_tip, axis=1, keepdims=False)
        finger_object_dist = np.clip(finger_object_dist, 0.03, 0.8)
        reward = np.sum(1.0 / (0.06 + finger_object_dist) * self.finger_reward_scale)
        # at least one tip and palm or two tips are contacting obj. Thumb contact is required.
        is_contact = np.sum(self.robot_object_contact) >= 2

        if is_contact:
            reward += 0.5
            lift = np.clip(self.object_lift, 0, 0.2)
            reward += 10 * lift
            if lift > 0.02:
                reward += 1
                target_obj_dist = np.linalg.norm(self.target_in_object)
                reward += 1.0 / (0.04 + target_obj_dist)

                if target_obj_dist < 0.1:
                    theta = self.target_in_object_angle[0]
                    reward += 4.0 / (0.4 + theta) * self.rotation_reward_weight

        action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * -0.01
        controller_penalty = (self.cartesian_error ** 2) * -1e3
        return (reward + action_penalty + controller_penalty) / 10
```
```

### dexpoint/env/sim_env/base.py

```
def recover_action(action, limit)
class BaseSimulationEnv(object)
    def __init__(self, use_gui, frame_skip, use_visual_obs, no_rgb, need_offscreen_render)
    def __del__(self)
    def simple_step(self)
    def reset_env(self)
    def seed(self, seed)
    def set_seed(self, seed)
    def render(self, mode)
    def check_contact(self, actors1, actors2, impulse_threshold)
    def check_actor_pair_contact(self, actor1, actor2, impulse_threshold)
    def check_actor_pair_contacts(self, actors1, actor2, impulse_threshold)
    def joint_limits(self)
    def create_viewer(self)
    def create_table(self, table_height, table_half_size)
    def create_camera(self, position, look_at_dir, right_dir, name, resolution, fov, mount_actor_name)
    def create_camera_from_pose(self, pose, name, resolution, fov)
    def setup_camera_from_config(self, config)
```

### dexpoint/env/sim_env/constructor.py

```
def get_engine_and_renderer(use_gui, use_ray_tracing, device, mipmap_levels, need_offscreen_render, no_rgb)
def download_maniskill(model_id, directory)
def add_default_scene_light(scene, renderer, add_ground, cast_shadow)
```

### dexpoint/env/sim_env/relocate_env.py

```
class LabRelocateEnv(BaseSimulationEnv)
    def __init__(self, use_gui, frame_skip, object_category, object_name, randomness_scale, friction, use_visual_obs)
    def load_object(self, object_name)
    def generate_random_object_pose(self, randomness_scale)
    def generate_random_target_pose(self, randomness_scale)
    def reset_env(self)
    def create_lab_tables(self, table_height)
def env_test()
```