# dexart_2023

source: https://github.com/Kami-code/dexart-release


commit: d6ab75e1a0b81384d1ac918cbfd4d97b1f230149


## README

# DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects

[[Project Page]](https://www.chenbao.tech/dexart/) [[arXiv]](https://arxiv.org/abs/2305.05706) [[Paper]](https://www.chenbao.tech/dexart/static/paper/dexart.pdf)
-----

[DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects](https://www.chenbao.tech/dexart/), 


[Chen Bao](https://chenbao.tech)\*, [Helin Xu](https://helinxu.github.io/)\*, [Yuzhe Qin](https://yzqin.github.io/), [Xiaolong Wang](https://xiaolonw.github.io/), CVPR 2023.


DexArt is a novel benchmark and pipeline for learning multiple dexterous manipulation tasks.
This repo contains the **simulated environment** and **training code** for DexArt.

![DexArt Teaser](docs/teaser.png)

## News
**[2023.11.21]** All the RL checkpoints are available now!🎈 They are included in the assets. See [Main Results](https://github.com/Kami-code/dexart-release#main-results) to reproduce the results in the paper! <br>
**[2023.4.18]**  Code and vision pre-trained models are available now! <br>
**[2023.3.24]**  DexArt is accepted by CVPR 2023! 🎉 <br>

## Installation

1. Clone the repo and Create a conda env with all the Python dependencies.

```bash
git clone git@github.com:Kami-code/dexart-release.git
cd dexart-release
conda create --name dexart python=3.8
conda activate dexart
pip install -e .    # for simulation environment
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 -c pytorch    # for visualizing trained policy and training 
```

2. Download the assets from
the [Google Drive](https://drive.usercontent.google.com/download?id=1DxRfB4087PeM3Aejd6cR-RQVgOKdNrL4&export=download&authuser=0) and place 
the `asset` directory at the project root directory.

## File Structure
The file structure is listed as follows:

`dexart/env/`: environments

`assets/`: tasks annotations, object, robot URDFs and RL checkpoints

`examples/`: example code to try DexArt

`stable_baselines3/`: RL training code modified from [stable_baselines3](https://github.com/DLR-RM/stable-baselines3)



## Quick Start

### Example of Random Action


```bash
python examples/random_action.py --task_name=laptop
```

`task_name`: name of the environment [`faucet`, `laptop`, `bucket`, `toilet`]

### Example for Visualizing Point Cloud Observation 

```bash
python examples/visualize_observation.py --task_name=laptop
```
`task_name`: name of the environment [`faucet`, `laptop`, `bucket`, `toilet`]


### Example for Visualizing Policy

```bash
python examples/visualize_policy.py --task_name=laptop --checkpoint_path assets/rl_checkpoints/laptop/laptop_nopretrain_0.zip
```

`task_name`: name of the environment [`faucet`, `laptop`, `bucket`, `toilet`]

`use_test_set`: flag to determine evaluating with seen or unseen instances

### Example for Training RL Agent

```bash
python3 examples/train.py --n 100 --workers 10 --iter 5000 --lr 0.0001 &&
--seed 100 --bs 500 --task_name laptop --extractor_name smallpn &&
--pretrain_path ./assets/vision_pretrain/laptop_smallpn_fulldata.pth 
```
`n`: the number of rollouts to be collected in a single episode

`workers`: the number of simulation progress

`iter`: the total episode number to be trained

`lr`: learning rate of RL

`seed`: seed of RL

`bs`: batch size of RL update

`task_name`: name of training environment [`faucet`, `laptop`, `bucket`, `toilet`]

`extractor_name`: different PointNet architectures [`smallpn`, `meduimpn`, `largepn`]

`pretrain_path`: path to downloaded pre-trained model. [Default: `None`]

`save_freq`: save the model every `save_freq` episodes. [Default: `1`]

`save_path`: path to save the model. [Default: `./examples`]

## Main Results
```bash
python examples/evaluate_policy.py --task_name=laptop --checkpoint_path assets/rl_checkpoints/laptop/laptop_nopretrain_0.zip --eval_per_instance 100
python examples/evaluate_policy.py --task_name=laptop --use_test_set --checkpoint_path assets/rl_checkpoints/laptop/laptop_nopretrain_0.zip --eval_per_instance 100
```

`task_name`: name of the environment [`faucet`, `laptop`, `bucket`, `toilet`]

`use_test_set`: flag to determine evaluating with seen or unseen instances

### Faucet

| Method                | Split       | Seed 0    | Seed 1    | Seed 2    | Avg               | Std               |
|-----------------------|-------------|-----------|-----------|-----------|-------------------|-------------------|
| No Pre-train          | train/test  | 0.52/0.34 | 0.00/0.00 | 0.44/0.43 | 0.32/0.26         | 0.23/0.18         |
| Segmentation on PMM   | train/test  | 0.42/0.38 | 0.25/0.15 | 0.14/0.11 | 0.27/0.21         | 0.11/0.12         |
| Classification on PMM | train/test  | 0.40/0.33 | 0.19/0.14 | 0.07/0.09 | 0.22/0.18         | 0.14/0.10         |
| Reconstruction on DAM | train/test  | 0.27/0.17 | 0.37/0.30 | 0.36/0.21 | 0.33/0.22         | 0.05/**0.05**     |
| SimSiam on DAM        | train/test  | 0.80/0.60 | 0.40/0.24 | 0.72/0.53 | 0.64/0.46         | 0.17/0.16         |
| Segmentation on DAM   | train/test  | 0.80/0.56 | 0.76/0.53 | 0.82/0.66 | **0.79**/**0.59** | **0.02**/**0.05** |

### Laptop

| Method                | Split       | Seed 0    | Seed 1    | Seed 2    | Avg               | Std               |
|-----------------------|-------------|-----------|-----------|-----------|-------------------|-------------------|
| No Pre-train          | train/test  | 0.78/0.41 | 0.78/0.31 | 0.81/0.50 | 0.79/0.41         | **0.02**/0.08     |
| Segmentation on PMM   | train/test  | 0.91/0.62 | 0.90/0.53 | 0.77/0.48 | 0.86/0.54         | 0.06/0.08         |
| Classification on PMM | train/test  | 0.96/0.51 | 0.58/0.35 | 0.96/0.62 | 0.83/0.49         | 0.18/0.11         |
| Reconstruction on DAM | train/test  | 0.85/0.56 | 0.91/0.63 | 0.80/0.43 | 0.85/0.54         | 0.05/0.08         |
| SimSiam on DAM        | train/test  | 0.84/0.59 | 0.83/0.34 | 0.89/0.51 | 0.86/0.48         | 0.03/0.10         |
| Segmentation on DAM   | train/test  | 0.89/0.57 | 0.94/0.67 | 0.89/0.58 | **0.91**/**0.60** | **0.02**/**0.04** |

### Bucket

| Method                | Split       | Seed 0    | Seed 1    | Seed 2    | Avg               | Std           |
|-----------------------|-------------|-----------|-----------|-----------|-------------------|---------------|
| No Pre-train          | train/test  | 0.36/0.55 | 0.58/0.69 | 0.52/0.49 | 0.49/0.57         | 0.09/0.08     |
| Segmentation on PMM   | train/test  | 0.62/0.62 | 0.00/0.00 | 0.40/0.41 | 0.34/0.34         | 0.26/0.26     |
| Classification on PMM | train/test  | 0.55/0.47 | 0.50/0.51 | 0.67/0.73 | 0.57/0.57         | 0.07/0.11     |
| Reconstruction on DAM | train/test  | 0.49/0.49 | 0.58/0.46 | 0.40/0.59 | 0.49/0.51         | 0.07/**0.05** |
| SimSiam on DAM        | train/test  | 0.00/0.00 | 0.53/0.38 | 0.73/0.78 | 0.42/0.39         | 0.30/0.32     |
| Segmentation on DAM   | train/test  | 0.70/0.68 | 0.70/0.74 | 0.79/0.85 | **0.73**/**0.75** | **0.04**/0.07 |

### Toilet

| Method                | Split       | Seed 0    | Seed 1    | Seed 2    | Avg               | Std               |
|-----------------------|-------------|-----------|-----------|-----------|-------------------|-------------------|
| No Pre-train          | train/test  | 0.80/0.47 | 0.75/0.51 | 0.63/0.43 | 0.72/0.47         | 0.07/0.03         |
| Segmentation on PMM   | train/test  | 0.78/0.42 | 0.62/0.46 | 0.64/0.47 | 0.68/0.45         | 0.07/0.02         |
| Classification on PMM | train/test  | 0.78/0.33 | 0.65/0.43 | 0.66/0.44 | 0.69/0.40         | 0.06/0.05         |
| Reconstruction on DAM | train/test  | 0.78/0.58 | 0.73/0.48 | 0.75/0.49 | 0.75/0.52         | 0.02/0.05         |
| SimSiam on DAM        | train/test  | 0.84/0.54 | 0.81/0.49 | 0.84/0.45 | 0.83/0.50         | **0.01**/0.04     |
| Segmentation on DAM   | train/test  | 0.86/0.54 | 0.84/0.53 | 0.86/0.56 | **0.85**/**0.54** | **0.01**/**0.01** |

## Visual Pretraining

We have uploaded the code to generate a dataset and pretrain our models in [examples/pretrain](https://github.com/Kami-code/dexart-release/tree/main/examples/pretrain). You can refer to [examples/pretrain/run.sh](https://github.com/Kami-code/dexart-release/blob/main/examples/pretrain/run.sh) for a detailed usage.

## Bibtex

```
@inproceedings{bao2023dexart,
  title={DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects},
  author={Bao, Chen and Xu, Helin and Qin, Yuzhe and Wang, Xiaolong},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={21190--21200},
  year={2023}
}
```

## Acknowledgements

This repository employs the same code structure for simulation environment and training code to that used in [DexPoint](https://github.com/yzqin/dexpoint-release).


## File tree (depth 3, assets pruned)

```
LICENSE
README.md
dexart/
  env/
    create_env.py
    rl_env/
    sim_env/
    task_setting.py
  utils/
    camera_utils.py
    common_robot_utils.py
    kinematics_helper.py
    mesh_utils.py
    model_utils.py
    physical_scene_utils.py
    random_utils.py
    render_scene_utils.py
examples/
  evaluate_policy.py
  pretrain/
    generate_dataset.py
    reconstruction/
    run.sh
    segmentation/
    simsiam/
  random_action.py
  train.py
  utils.py
  visualize_observation.py
  visualize_policy.py
setup.py
stable_baselines3/
  __init__.py
  a2c/
    __init__.py
    a2c.py
    policies.py
  common/
    __init__.py
    base_class.py
    buffers.py
    callbacks.py
    distributions.py
    env_util.py
    evaluation.py
    logger.py
    monitor.py
    noise.py
    on_policy_algorithm.py
    policies.py
    preprocessing.py
    running_mean_std.py
    save_util.py
    torch_layers.py
    type_aliases.py
    utils.py
    vec_env/
  networks/
    pretrain_nets.py
  pickle_utils.py
  ppo/
    __init__.py
    policies.py
    ppo.py
  py.typed
  simple_callback.py
  version.txt
```

## Config files (0)


## Python signatures and reward/observation bodies (51 files)


### dexart/env/create_env.py

```
def create_env(task_name, use_visual_obs, use_gui, is_eval, pc_seg, pc_noise, index, img_type, rand_pos, rand_degree, frame_skip)
```

### dexart/env/rl_env/base.py

```
def recover_action(action, limit)
class BaseRLEnv(BaseSimulationEnv, Env)
    def __init__(self, use_gui, frame_skip, use_visual_obs, renderer)
    def seed(self, seed)
    def get_observation(self)
    def get_reward(self, action)
    def get_info(self)
    def update_cached_state(self)
    def is_done(self)
    def obs_dim(self)
    def action_dim(self)
    def horizon(self)
    def setup(self, robot_name)
    def free_sim_step(self, action)
    def arm_sim_step(self, action)
    def arm_kinematic_step(self, action)
    def reset_internal(self)
    def step(self, action)
    def configure_robot_contact_reward(self)
    def grouping_info(self)
    def setup_visual_obs_config(self, config)
    def setup_imagination_config(self, config)
    def flush_imagination_config(self)
    def update_imagination(self, reset_goal)
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
def configure_robot_contact_reward(self):
        if self.is_robot_free:
            info = generate_free_robot_hand_info()[self.robot_name]
        else:
            info = generate_arm_robot_hand_info()[self.robot_name]
        robot_link_names = [link.get_name() for link in self.robot.get_links()]
        robot_links = self.robot.get_links()
        # configure palm
        self.palm_link_name = info.palm_name
        self.palm_link = [link for link in self.robot.get_links() if link.get_name() == 'base_link'][0]
        # configure fingers
        finger_tip_names = ["link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip"]
        thumb_link_name = ["link_15.0_tip", "link_15.0", "link_14.0"]
        index_link_name = ["link_3.0_tip", "link_3.0", "link_2.0", "link_1.0"]
        middle_link_name = ["link_7.0_tip", "link_7.0", "link_6.0", "link_5.0"]
        ring_link_name = ["link_11.0_tip", "link_11.0", "link_10.0", "link_9.0"]
        self.thumb_links = [robot_links[robot_link_names.index(name)] for name in thumb_link_name]
        self.index_links = [robot_links[robot_link_names.index(name)] for name in index_link_name]
        self.middle_links = [robot_links[robot_link_names.index(name)] for name in middle_link_name]
        self.ring_links = [robot_links[robot_link_names.index(name)] for name in ring_link_name]
        self.finger_tip_links = [robot_links[robot_link_names.index(name)] for name in finger_tip_names]
        self.finger_contact_links = self.thumb_links + self.index_links + self.middle_links + self.ring_links
        self.finger_contact_ids = np.array([0] * 3 + [1] * 4 + [2] * 4 + [3] * 4 + [4])
        self.finger_tip_pos = np.zeros([len(finger_tip_names), 3])
        self.finger_reward_scale = np.ones(len(self.finger_tip_links)) * 0.01
        self.finger_reward_scale[0] = 0.04
        # configure arm
        arm_contact_link_name = ["link_base", "link1", "link2", "link3", "link4", "link5", "link6"]
        self.arm_contact_links = [self.robot.get_links()[robot_link_names.index(name)] for name in
                                  arm_contact_link_name]
        self.robot_object_contact = np.zeros(len(finger_tip_names) + 1)  # contact buffer of four tip and palm
        self.robot_object_contact_handle = np.zeros(len(finger_tip_names) + 1)
        self.robot_object_contact_no_handle = np.zeros(len(finger_tip_names) + 1)
        self.hand_base_contact = np.zeros(len(finger_tip_names) + 1)
        self.robot_instance_base_contact = np.zeros(len(finger_tip_names) + 1)
        # configure hand / palm /robot id (for segmentation)
        self.thumb_ids = [link.get_id() for link in self.thumb_links] + [
            robot_links[robot_link_names.index("link_13.0")].get_id()]
        self.index_ids = [link.get_id() for link in self.index_links] + [
            robot_links[robot_link_names.index("link_0.0")].get_id()]
        self.middle_ids = [link.get_id() for link in self.middle_links] + [
            robot_links[robot_link_names.index("link_4.0")].get_id()]
        self.ring_ids = [link.get_id() for link in self.ring_links] + [
            robot_links[robot_link_names.index("link_8.0")].get_id()]
        self.palm_id = [self.palm_link.get_id()] + [robot_links[robot_link_names.index("link_12.0")].get_id()]
```

```python
def get_visual_observation(self):
        camera_obs = self.get_camera_obs()
        robot_obs = self.get_robot_state()
        oracle_obs = self.get_oracle_state()
        camera_obs.update(dict(state=robot_obs, oracle_state=oracle_obs))
        # ================ add the history frame if use_history_obs ===============
        if self.use_history_obs:
            current_obs = camera_obs.copy()
            if self.last_obs is None or len(self.last_obs.keys()) != 2 * len(current_obs):  # handle the first frame
                self.last_obs = current_obs
            for key, value in self.last_obs.items():
                if 'previous' in key:
                    self.last_obs.pop(key)
            for key, value in self.last_obs.items():
                camera_obs.update({'previous-' + key: value})
            self.last_obs = current_obs  # self.last_obs does not contain the previous history
        # =========================================================================
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
            if self.use_history_obs:
                obs_dict.update({"previous-state": state_space, "previous-oracle_state": oracle_space})
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
                        obs_dict[f"{cam_name}-seg_gt"] = gym.spaces.Box(low=-np.inf, high=np.inf,
                                                                        shape=(cam_cfg[modality_name]["num_points"],)
                                                                              + (4,))
                    elif modality_name == "segmentation":
                        spec = gym.spaces.Box(low=0, high=255, shape=resolution + (2,), dtype=np.uint8)
                    else:
                        raise RuntimeError("What happen? you should not see this error!")
                    obs_dict[key_name] = spec
                    if self.use_history_obs:
                        obs_dict['previous-' + key_name] = spec

            if len(self.imagination_infos) > 0:
                self.update_imagination(reset_goal=True)
                for img_name, points in self.imaginations.items():
                    num_points = points.shape[0]
                    obs_dict[img_name] = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(num_points, 7))
                    if self.use_history_obs:
                        obs_dict['previous-' + img_name] = gym.spaces.Box(low=-np.inf, high=np.inf,
                                                                          shape=(num_points, 7))

            return gym.spaces.Dict(obs_dict)
```
```

### dexart/env/rl_env/bucket_env.py

```
def getAngle(P, Q)
class BucketRLEnv(BucketEnv, BaseRLEnv)
    def __init__(self, use_gui, frame_skip, robot_name, friction, index, rand_pos, rand_orn, thick_handle)
    def update_cached_state(self)
    def get_oracle_state(self)
    def get_robot_state(self)
    def get_reward(self, action)
    def reset(self)
    def setup_robot_annotation(self, robot_name)
    def obs_dim(self)
    def is_done(self)
    def horizon(self)

```python
def get_reward(self, action):
        reward = 0
        reward += 0.2 * self.palm_vector[2]
        reward -= 0.2 * self.finger_base_touched_percent  # under no circumstances should hand touch bucket base
        if self.state == 1:
            reward = -0.1 * min(np.linalg.norm(self.palm_pose.p - self.handle_pose.p),
                                0.5)  # encourage palm be close to handle
        elif self.state == 2:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            reward -= 0.01 * np.linalg.norm(self.instance_base_link.get_velocity())
            reward -= 0.01 * np.linalg.norm(self.instance_base_link.get_angular_velocity())
            reward += 0.5 * self.progress
            reward += (0.2 * self.progress) * self.finger_touched_percent
        elif self.state == 3:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            reward += 0.5 * self.progress
            reward += (0.2 * self.progress) * self.finger_touched_percent
            if self.delta_height < 0.3:
                reward += 100 * (self.palm_height - self.last_palm_height)
                reward += self.delta_height / 0.3 * 10  # lift to 0.6m is enough

        action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * 0.01
        controller_penalty = (self.cartesian_error ** 2) * 1e3
        reward -= 0.1 * (action_penalty + controller_penalty)
        return reward
```
```

### dexart/env/rl_env/faucet_env.py

```
class FaucetRLEnv(FaucetEnv, BaseRLEnv)
    def __init__(self, use_gui, frame_skip, robot_name, friction, index, rand_pos, rand_orn)
    def update_cached_state(self)
    def get_oracle_state(self)
    def get_robot_state(self)
    def get_reward(self, action)
    def reset(self)
    def setup_robot_annotation(self, robot_name)
    def obs_dim(self)
    def is_done(self)
    def horizon(self)

```python
def get_reward(self, action):
        reward = 0
        if self.state == 1:
            reward = -0.1 * min(np.linalg.norm(self.palm_pose.p - self.handle_pose.p),
                                0.5)  # encourage palm be close to handle
        elif self.state == 2:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
        elif self.state == 3:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            reward += 1.0 * self.openness
        if self.early_done:
            reward += (self.horizon - self.current_step) * 1.2 * self.openness
        action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * 0.01
        controller_penalty = (self.cartesian_error ** 2) * 1e3
        reward -= 0.01 * (action_penalty + controller_penalty)
        return reward
```
```

### dexart/env/rl_env/laptop_env.py

```
class LaptopRLEnv(LaptopEnv, BaseRLEnv)
    def __init__(self, use_gui, frame_skip, robot_name, friction, index, rand_pos, rand_orn)
    def update_cached_state(self)
    def get_oracle_state(self)
    def get_robot_state(self)
    def get_reward(self, action)
    def reset(self)
    def setup_robot_annotation(self, robot_name)
    def obs_dim(self)
    def is_done(self)
    def horizon(self)

```python
def get_reward(self, action):
        reward = 0
        if self.state == 1:
            reward = -0.1 * min(np.linalg.norm(self.palm_pose.p - self.handle_pose.p), 0.5)  # encourage palm be close to handle
            if self.progress < 0:
                reward += 0.5 * self.progress
        elif self.state == 2:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            if self.progress < 0:
                reward += 0.5 * self.progress
        elif self.state == 3:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            reward += 1.0 * self.progress
        if self.early_done:
            reward += (self.horizon - self.current_step) * 1.2 * self.progress
        action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * 0.01
        controller_penalty = (self.cartesian_error ** 2) * 1e3
        reward -= 0.01 * (action_penalty + controller_penalty)
        return reward
```
```

### dexart/env/rl_env/pc_processing.py

```
def process_pc(task_name, cloud, camera_pose, num_points, np_random, noise_level, grouping_info, segmentation)
def add_gaussian_noise(cloud, np_random, noise_level)
```

### dexart/env/rl_env/toilet_env.py

```
"""@Project ：hand_teleop 
@File    ：toiletv2_env.py
@Author  ：Chen Bao
@Date    ：2023/1/19 上午1:19 """
class ToiletRLEnv(ToiletEnv, BaseRLEnv)
    def __init__(self, use_gui, frame_skip, robot_name, friction, index, rand_pos, rand_orn)
    def update_cached_state(self)
    def get_oracle_state(self)
    def get_robot_state(self)
    def get_reward(self, action)
    def reset(self)
    def setup_robot_annotation(self, robot_name)
    def obs_dim(self)
    def is_done(self)
    def horizon(self)

```python
def get_reward(self, action):
        reward = 0
        if self.state == 1:
            reward = -0.1 * min(np.linalg.norm(self.palm_pose.p - self.handle_pose.p),
                                0.5)  # encourage palm be close to handle
            if self.progress < 0:
                reward += 0.5 * self.progress
        elif self.state == 2:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            if self.progress < 0:
                reward += 0.5 * self.progress
        elif self.state == 3:
            reward += 0.2 * (int(self.is_contact))
            reward -= 0.1 * (int(self.is_arm_contact))
            reward += 1.0 * self.progress
        if self.early_done:
            reward += (self.horizon - self.current_step) * 1.2 * self.progress
        action_penalty = np.sum(np.clip(self.robot.get_qvel(), -1, 1) ** 2) * 0.01
        controller_penalty = (self.cartesian_error ** 2) * 1e3
        reward -= 0.005 * (action_penalty + controller_penalty)
        return reward
```
```

### dexart/env/sim_env/base.py

```
def recover_action(action, limit)
class BaseSimulationEnv(object)
    def __init__(self, use_gui, frame_skip, use_visual_obs, no_rgb, need_offscreen_render)
    def simple_step(self)
    def pre_step(self)
    def post_step(self)
    def reset_env(self)
    def __del__(self)
    def seed(self, seed)
    def set_seed(self, seed)
    def render(self, mode)
    def check_contact(self, actors1, actors2, impulse_threshold)
    def check_actor_pair_contact(self, actor1, actor2, impulse_threshold)
    def check_actor_pair_contacts(self, actors1, actor2, impulse_threshold)
    def check_actors_pair_contacts(self, actors1, actors2, impulse_threshold)
    def check_actor_pair_contacts_in_distances(self, actors1, actor2, centers, radii, impulse_threshold, reverse)
    def check_actors_pair_contacts_in_distance(self, actors1, actors2, centers, radii, impulse_threshold, reverse)
    def joint_limits(self)
    def create_viewer(self)
    def create_table(self, table_height, table_half_size)
    def create_box(self, pose, half_size, color, name)
    def create_room(self, length)
    def create_camera(self, position, look_at_dir, right_dir, name, resolution, fov, mount_actor_name)
    def create_camera_from_pose(self, pose, name, resolution, fov, use_opencv_trans)
    def setup_camera_from_config(self, config, use_opencv_trans)
```

### dexart/env/sim_env/bucket_env.py

```
class BucketEnv(BaseSimulationEnv)
    def __init__(self, use_gui, frame_skip, friction, iter, handle_type, fix_root_link)
    def setup_instance_annotation(self)
    def load_instance(self, index)
    def reset_env(self)
    def update_handle_relative_pose(self)
    def get_handle_global_pose(self)
```

### dexart/env/sim_env/constructor.py

```
def get_engine_and_renderer(use_gui, use_ray_tracing, device, mipmap_levels, need_offscreen_render, no_rgb)
def add_default_scene_light(scene, renderer, add_ground, cast_shadow)
```

### dexart/env/sim_env/faucet_env.py

```
class FaucetEnv(BaseSimulationEnv)
    def __init__(self, use_gui, frame_skip, friction, iter)
    def setup_instance_annotation(self)
    def load_instance(self, index)
    def reset_env(self)
```

### dexart/env/sim_env/laptop_env.py

```
class LaptopEnv(BaseSimulationEnv)
    def __init__(self, use_gui, frame_skip, friction, iter)
    def setup_instance_annotation(self)
    def load_instance(self, index)
    def reset_env(self)
    def update_handle_relative_pose(self)
    def get_handle_global_pose(self)
```

### dexart/env/sim_env/toilet_env.py

```
class ToiletEnv(BaseSimulationEnv)
    def __init__(self, use_gui, frame_skip, friction, iter)
    def setup_instance_annotation(self)
    def load_instance(self, index)
    def reset_env(self)
    def update_handle_relative_pose(self)
    def get_handle_global_pose(self)
```

### examples/pretrain/generate_dataset.py

```
def gen_single_data(task_name, index, split, n_fold, img_type, save_path)
def merge_data(category, save_path, merge_half)
```

### examples/pretrain/reconstruction/data_utils.py

```
class SemSegDataset(Dataset)
    def __init__(self, root_dir, split, use_img, point_channel)
    def load_data(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### examples/pretrain/reconstruction/models/pcn_util.py

```
class PCNEncoder(Module)
    def __init__(self, global_feat, channel)
    def forward(self, x)
class PCNPartSegEncoder(Module)
    def __init__(self, channel)
    def forward(self, x, label)
class encoder(Module)
    def __init__(self, num_channel)
    def forward(self, x)
```

### examples/pretrain/reconstruction/models/pointnet.py

```
class PointNet(Module)
    def __init__(self, point_channel)
    def reset_parameters_(self)
    def forward(self, x)
class EncoderDecoder(Module)
    def __init__(self)
    def build_grid(self, batch_size)
    def tile(self, tensor, multiples)
    def expand_dims(tensor, dim)
    def forward(self, x)
class ChamLoss(Module)
    def __init__(self)
    def dist_cd(pc2, pc1)
    def forward(self, coarse, fine, gt, alpha)
```

### examples/pretrain/reconstruction/train_reconstruction.py

```
class Solver(object)
    def __init__(self, config, train_loader, val_loader, test_loader)
    def train(self)
    def save(self, epoch)
    def load(self, path)
    def visualize(self, split)
def main()
```

### examples/pretrain/segmentation/data_utils.py

```
class SemSegDataset(Dataset)
    def __init__(self, root_dir, split, use_img, point_channel, half)
    def load_data(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### examples/pretrain/segmentation/models/pointnet.py

```
class PointNet(Module)
    def __init__(self, point_channel, classes)
    def reset_parameters_(self)
    def forward(self, x)
class PointNetMedium(Module)
    def __init__(self, point_channel, classes)
    def reset_parameters_(self)
    def forward(self, x)
class PointNetLarge(Module)
    def __init__(self, point_channel, classes)
    def reset_parameters_(self)
    def forward(self, x)
```

### examples/pretrain/segmentation/train_segmentation.py

```
class Solver(object)
    def __init__(self, config, train_loader, val_loader, test_loader)
    def train(self)
    def validate(self, epoch, split)
    def save(self, epoch)
    def load(self, path)
    def visualize(self, split, num)
def main()
```

### examples/pretrain/simsiam/data_utils.py

```
class SemSegDataset(Dataset)
    def __init__(self, root_dir, split, use_img, point_channel)
    def load_data(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### examples/pretrain/simsiam/models/pointnet.py

```
class PointNet(Module)
    def __init__(self, point_channel)
    def reset_parameters_(self)
    def forward(self, x)
class SimSiam(Module)
    def __init__(self, rotate)
    def reset_parameters_(self)
    def point_augment(self, x)
    def forward(self, x)
def D(p, z)
def test()
```

### examples/pretrain/simsiam/train_simsiam.py

```
class Solver(object)
    def __init__(self, config, train_loader, val_loader, test_loader)
    def train(self)
    def save(self, epoch)
    def load(self, path)
    def visualize(self, split)
def main()
```

### examples/train.py

```
def get_3d_policy_kwargs(extractor_name)
```

### stable_baselines3/common/env_util.py

```
def unwrap_wrapper(env, wrapper_class)
def is_wrapped(env, wrapper_class)
def make_vec_env(env_id, n_envs, seed, start_index, monitor_dir, wrapper_class, env_kwargs, vec_env_cls, vec_env_kwargs, monitor_kwargs, wrapper_kwargs)
```

### stable_baselines3/common/on_policy_algorithm.py

```
class OnPolicyAlgorithm(BaseAlgorithm)
    """The base for On-Policy algorithms (ex: A2C/PPO).

:param policy: The policy model to use (MlpPolicy, CnnPolicy, ...)
:param env: The environment to learn from (if registered in Gym, can be str)
:param learning_rate: The learning rate, it can be a function
    of the current progress remaining (from """
    def __init__(self, policy, env, learning_rate, n_steps, gamma, gae_lambda, ent_coef, vf_coef, max_grad_norm, use_sde, sde_sample_freq, tensorboard_log, create_eval_env, monitor_wrapper, policy_kwargs, verbose, seed, device, _init_setup_model, supported_action_spaces)
    def _setup_model(self)
    def collect_rollouts(self, env, callback, rollout_buffer, n_rollout_steps)
    def train(self)
    def learn(self, total_timesteps, callback, log_interval, eval_env, eval_freq, n_eval_episodes, tb_log_name, eval_log_path, reset_num_timesteps, iter_start)
    def _get_torch_save_params(self)
    def _excluded_save_params(self)
```

### stable_baselines3/common/vec_env/__init__.py

```
def unwrap_vec_wrapper(env, vec_wrapper_class)
def unwrap_vec_normalize(env)
def is_vecenv_wrapped(env, vec_wrapper_class)
def sync_envs_normalization(env, eval_env)
```

### stable_baselines3/common/vec_env/base_vec_env.py

```
def tile_images(img_nhwc)
class VecEnv(ABC)
    """An abstract asynchronous, vectorized environment.

:param num_envs: the number of environments
:param observation_space: the observation space
:param action_space: the action space"""
    def __init__(self, num_envs, observation_space, action_space)
    def reset(self)
    def step_async(self, actions)
    def step_wait(self)
    def close(self)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def step(self, actions)
    def get_images(self)
    def render(self, mode)
    def seed(self, seed)
    def unwrapped(self)
    def getattr_depth_check(self, name, already_found)
    def _get_indices(self, indices)
class VecEnvWrapper(VecEnv)
    """Vectorized environment base class

:param venv: the vectorized environment to wrap
:param observation_space: the observation space (can be None to load from venv)
:param action_space: the action space (can be None to load from venv)"""
    def __init__(self, venv, observation_space, action_space)
    def step_async(self, actions)
    def reset(self)
    def step_wait(self)
    def seed(self, seed)
    def close(self)
    def render(self, mode)
    def get_images(self)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def __getattr__(self, name)
    def _get_all_attributes(self)
    def getattr_recursive(self, name)
    def getattr_depth_check(self, name, already_found)
class CloudpickleWrapper()
    """Uses cloudpickle to serialize contents (otherwise multiprocessing tries to use pickle)

:param var: the variable you wish to wrap for pickling with cloudpickle"""
    def __init__(self, var)
    def __getstate__(self)
    def __setstate__(self, var)
```

### stable_baselines3/common/vec_env/dummy_vec_env.py

```
class DummyVecEnv(VecEnv)
    """Creates a simple vectorized wrapper for multiple environments, calling each environment in sequence on the current
Python process. This is useful for computationally simple environment such as ``cartpole-v1``,
as the overhead of multiprocess or multithread outweighs the environment computation time."""
    def __init__(self, env_fns)
    def step_async(self, actions)
    def step_wait(self)
    def seed(self, seed)
    def reset(self)
    def close(self)
    def get_images(self)
    def render(self, mode)
    def _save_obs(self, env_idx, obs)
    def _obs_from_buf(self)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def _get_target_envs(self, indices)
```

### stable_baselines3/common/vec_env/maniskill2_utils_common.py

```
def merge_dicts(ds, asarray)
def normalize_vector(x, eps)
def compute_angle_between(x1, x2)
class np_random()
    """Context manager for numpy random state"""
    def __init__(self, seed)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
def random_choice(x, rng)
def get_dtype_bounds(dtype)
def convert_observation_to_space(observation, prefix)
def normalize_action_space(action_space)
def clip_and_scale_action(action, low, high)
def inv_clip_and_scale_action(action, low, high)
def inv_scale_action(action, low, high)
def flatten_state_dict(state_dict)
def flatten_dict_keys(d, prefix)
def extract_scalars_from_info(info, blacklist)
def flatten_dict_space_keys(space, prefix)

```python
def convert_observation_to_space(observation, prefix=""):
    """Convert observation to OpenAI gym observation space (recursively).
    Modified from `gym.envs.mujoco_env`
    """
    if isinstance(observation, (dict)):
        space = spaces.Dict(
            {
                k: convert_observation_to_space(v, prefix + "/" + k)
                for k, v in observation.items()
            }
        )
    elif isinstance(observation, np.ndarray):
        shape = observation.shape
        dtype = observation.dtype
        low, high = get_dtype_bounds(dtype)
        if np.issubdtype(dtype, np.floating):
            low, high = -np.inf, np.inf
        space = spaces.Box(low, high, shape=shape, dtype=dtype)
    elif isinstance(observation, (float, np.float32, np.float64)):
        print(f"The observation ({prefix}) is a (float) scalar")
        space = spaces.Box(-np.inf, np.inf, shape=[1], dtype=np.float32)
    elif isinstance(observation, (int, np.int32, np.int64)):
        print(f"The observation ({prefix}) is a (integer) scalar")
        space = spaces.Box(-np.inf, np.inf, shape=[1], dtype=int)
    elif isinstance(observation, (bool, np.bool_)):
        print(f"The observation ({prefix}) is a (bool) scalar")
        space = spaces.Box(0, 1, shape=[1], dtype=np.bool_)
    else:
        raise NotImplementedError(type(observation), observation)

    return space
```
```

### stable_baselines3/common/vec_env/maniskill2_utils_wrappers_obs.py

```
class RGBDObservationWrapper(ObservationWrapper)
    """Map raw textures (Color and Position) to rgb and depth."""
    def __init__(self, env)
    def update_observation_space(space)
    def observation(self, observation)
def merge_dict_spaces(dict_spaces)
class PointCloudObservationWrapper(ObservationWrapper)
    """Convert Position textures to world-space point cloud."""
    def __init__(self, env)
    def update_observation_space(space)
    def observation(self, observation)
class RobotSegmentationObservationWrapper(ObservationWrapper)
    """Add a binary mask for robot links."""
    def __init__(self, env, replace)
    def init_observation_space(space, replace)
    def reset(self)
    def observation_image(self, observation)
    def observation_pointcloud(self, observation)
    def observation(self, observation)
class FlattenObservationWrapper(ObservationWrapper)
    def __init__(self, env)
    def observation(self, observation)

```python
def update_observation_space(space: spaces.Dict):
        # Update image observation space
        image_space: spaces.Dict = space.spaces["image"]
        for cam_uid in image_space:
            ori_cam_space = image_space[cam_uid]
            new_cam_space = OrderedDict()
            for key in ori_cam_space:
                if key == "Color":
                    height, width = ori_cam_space[key].shape[:2]
                    new_cam_space["rgb"] = spaces.Box(
                        low=0, high=255, shape=(height, width, 3), dtype=np.uint8
                    )
                elif key == "Position":
                    height, width = ori_cam_space[key].shape[:2]
                    new_cam_space["depth"] = spaces.Box(
                        low=0, high=np.inf, shape=(height, width, 1), dtype=np.float32
                    )
                else:
                    new_cam_space[key] = ori_cam_space[key]
            image_space.spaces[cam_uid] = spaces.Dict(new_cam_space)
```

```python
def observation(self, observation: dict):
        image_obs = observation["image"]
        for cam_uid, ori_images in image_obs.items():
            new_images = OrderedDict()
            for key in ori_images:
                if key == "Color":
                    rgb = ori_images[key][..., :3]  # [H, W, 4]
                    rgb = np.clip(rgb * 255, 0, 255).astype(np.uint8)
                    new_images["rgb"] = rgb  # [H, W, 4]
                elif key == "Position":
                    depth = -ori_images[key][..., [2]]  # [H, W, 1]
                    new_images["depth"] = depth
                else:
                    new_images[key] = ori_images[key]
            image_obs[cam_uid] = new_images
        return observation
```

```python
def update_observation_space(space: spaces.Dict):
        # Replace image observation spaces with point cloud ones
        image_space: spaces.Dict = space.spaces.pop("image")
        space.spaces.pop("camera_param")
        pcd_space = OrderedDict()

        for cam_uid in image_space:
            cam_image_space = image_space[cam_uid]
            cam_pcd_space = OrderedDict()

            h, w = cam_image_space["Position"].shape[:2]
            cam_pcd_space["xyzw"] = spaces.Box(
                low=-np.inf, high=np.inf, shape=(h * w, 4), dtype=np.float32
            )

            # Extra keys
            if "Color" in cam_image_space.spaces:
                cam_pcd_space["rgb"] = spaces.Box(
                    low=0, high=255, shape=(h * w, 3), dtype=np.uint8
                )
            if "Segmentation" in cam_image_space.spaces:
                cam_pcd_space["Segmentation"] = spaces.Box(
                    low=0, high=(2 ** 32 - 1), shape=(h * w, 4), dtype=np.uint32
                )

            pcd_space[cam_uid] = spaces.Dict(cam_pcd_space)

        pcd_space = merge_dict_spaces(pcd_space.values())
        space.spaces["pointcloud"] = pcd_space
```

```python
def observation(self, observation: dict):
        image_obs = observation.pop("image")
        camera_params = observation.pop("camera_param")
        pointcloud_obs = OrderedDict()

        for cam_uid, images in image_obs.items():
            cam_pcd = {}

            # Each pixel is (x, y, z, z_buffer_depth) in OpenGL camera space
            position = images["Position"]
            # position[..., 3] = position[..., 3] < 1
            position[..., 3] = position[..., 2] < 0

            # Convert to world space
            cam2world = camera_params[cam_uid]["cam2world_gl"]
            xyzw = position.reshape(-1, 4) @ cam2world.T
            cam_pcd["xyzw"] = xyzw

            # Extra keys
            if "Color" in images:
                rgb = images["Color"][..., :3]
                rgb = np.clip(rgb * 255, 0, 255).astype(np.uint8)
                cam_pcd["rgb"] = rgb.reshape(-1, 3)
            if "Segmentation" in images:
                cam_pcd["Segmentation"] = images["Segmentation"].reshape(-1, 4)

            pointcloud_obs[cam_uid] = cam_pcd

        pointcloud_obs = merge_dicts(pointcloud_obs.values())
        for key, value in pointcloud_obs.items():
            buffer = self._buffer.get(key, None)
            pointcloud_obs[key] = np.concatenate(value, out=buffer)
            self._buffer[key] = pointcloud_obs[key]

        observation["pointcloud"] = pointcloud_obs
        return observation
```

```python
def init_observation_space(space: spaces.Dict, replace: bool):
        # Update image observation spaces
        if "image" in space.spaces:
            image_space = space["image"]
            for cam_uid in image_space:
                cam_space = image_space[cam_uid]
                if "Segmentation" not in cam_space.spaces:
                    continue
                height, width = cam_space["Segmentation"].shape[:2]
                new_space = spaces.Box(
                    low=0, high=1, shape=(height, width, 1), dtype="bool"
                )
                if replace:
                    cam_space.spaces.pop("Segmentation")
                cam_space.spaces["robot_seg"] = new_space

        # Update pointcloud observation spaces
        if "pointcloud" in space.spaces:
            pcd_space = space["pointcloud"]
            if "Segmentation" in pcd_space.spaces:
                n = pcd_space["Segmentation"].shape[0]
                new_space = spaces.Box(low=0, high=1, shape=(n, 1), dtype="bool")
                if replace:
                    pcd_space.spaces.pop("Segmentation")
                pcd_space.spaces["robot_seg"] = new_space
```

```python
def observation_image(self, observation: dict):
        image_obs = observation["image"]
        for cam_images in image_obs.values():
            if "Segmentation" not in cam_images:
                continue
            seg = cam_images["Segmentation"]
            robot_seg = np.isin(seg[..., 1:2], self.robot_link_ids)
            if self.replace:
                cam_images.pop("Segmentation")
            cam_images["robot_seg"] = robot_seg
        return observation
```

```python
def observation_pointcloud(self, observation: dict):
        pointcloud_obs = observation["pointcloud"]
        if "Segmentation" not in pointcloud_obs:
            return observation
        seg = pointcloud_obs["Segmentation"]
        robot_seg = np.isin(seg[..., 1:2], self.robot_link_ids)
        if self.replace:
            pointcloud_obs.pop("Segmentation")
        pointcloud_obs["robot_seg"] = robot_seg
        return observation
```

```python
def observation(self, observation: dict):
        if "image" in observation:
            observation = self.observation_image(observation)
        if "pointcloud" in observation:
            observation = self.observation_pointcloud(observation)
        return observation
```

```python
def observation(self, observation):
        return flatten_dict_keys(observation)
```
```

### stable_baselines3/common/vec_env/maniskill2_vec_env.py

```
"""ManiSkill2 vectorized environment.

See also:
    https://github.com/DLR-RM/stable-baselines3/blob/master/stable_baselines3/common/vec_env/subproc_vec_env.py"""
def find_available_port()
def _worker(rank, remote, parent_remote, env_fn)
class VecEnv()
    """Vectorized environment modified from Stable Baselines3 for ManiSkill2.
Image observations can stay on GPU to avoid unnecessary data transfer.

Creates a multiprocess vectorized wrapper for multiple environments, distributing each environment to its own
process, allowing significant speed up when the"""
    def __init__(self, env_fns, start_method, server_address, server_kwargs)
    def _update_np_buffer(self, obs_list, indices)
    def _get_torch_observations(self)
    def seed(self, seed)
    def reset_async(self, indices)
    def reset_wait(self, indices)
    def reset(self, indices)
    def step_async(self, actions)
    def step_wait(self)
    def step(self, actions)
    def close(self)
    def render(self, mode)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def unwrapped(self)
    def _get_indices(self, indices)
    def _get_target_remotes(self, indices)
    def __repr__(self)
def stack_observation_space(space, n)
def create_np_buffer(space, n)
def stack_obs(obs, space, buffer)
class RGBDVecEnv(VecEnv)
    def __init__(self)
    def _get_torch_observations(self)
class PointCloudVecEnv(VecEnv)
    def __init__(self)
    def _get_torch_observations(self)
    def observation(self, observation)
    def reset_wait(self)
    def step_wait(self)
class VecEnvWrapper(VecEnv)
    def __init__(self, venv)
    def seed(self, seed)
    def reset_async(self)
    def reset_wait(self)
    def step_async(self, actions)
    def step_wait(self)
    def close(self)
    def render(self, mode)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def __getattr__(self, name)
class VecEnvObservationWrapper(VecEnvWrapper)
    def reset_wait(self)
    def step_wait(self)
    def observation(self, observation)

```python
def stack_observation_space(space: spaces.Space, n: int):
    if isinstance(space, spaces.Dict):
        sub_spaces = [
            (key, stack_observation_space(subspace, n))
            for key, subspace in space.spaces.items()
        ]
        return spaces.Dict(sub_spaces)
    elif isinstance(space, spaces.Box):
        shape = (n,) + space.shape
        low = np.broadcast_to(space.low, shape)
        high = np.broadcast_to(space.high, shape)
        return spaces.Box(low=low, high=high, shape=shape, dtype=space.dtype)
    else:
        raise NotImplementedError(
            "Unsupported observation space: {}".format(type(space))
        )
```

```python
def _get_torch_observations(self):
        self.server.wait_all()

        tensor_dict = {}
        for i, name in enumerate(self.texture_names):
            tensor_dict[name] = self._obs_torch_buffer[i]

        # NOTE(jigu): Efficiency might not be optimized when using more cameras
        image_obs = {}
        for cam_idx, cam_uid in enumerate(self.image_obs_space.spaces.keys()):
            image_obs[cam_uid] = {}
            cam_space = self.image_obs_space[cam_uid]
            for tex_name in cam_space:
                tensor = tensor_dict[tex_name][:, cam_idx]  # [B, H, W, C]
                if tensor.shape[1:3] != cam_space[tex_name].shape[0:2]:
                    h, w = cam_space[tex_name].shape[0:2]
                    tensor = tensor[:, :h, :w]
                image_obs[cam_uid][tex_name] = tensor

        return dict(image=image_obs)
```

```python
def _get_torch_observations(self):
        observation = super()._get_torch_observations()

        image_obs = observation["image"]
        for cam_uid, ori_images in image_obs.items():
            new_images = {}
            for key in ori_images:
                if key == "Color":
                    rgb = ori_images[key][..., :3]
                    rgb = torch.clamp(rgb * 255, 0, 255).to(dtype=torch.uint8)
                    new_images["rgb"] = rgb
                elif key == "Position":
                    depth = -ori_images[key][..., [2]]
                    new_images["depth"] = depth
                else:
                    new_images[key] = ori_images[key]
            image_obs[cam_uid] = new_images
        return observation
```

```python
def _get_torch_observations(self):
        observation = super()._get_torch_observations()

        image_obs = observation.pop("image")
        pointcloud_obs = {}

        for cam_uid, cam_images in image_obs.items():
            cam_pcd = {}

            # Each pixel is (x, y, z, z_buffer_depth) in OpenGL camera space
            position = cam_images["Position"]
            bs = position.size(0)

            # Homogeneous coordinates
            xyzw = torch.cat([position[..., :3], position[..., [3]] < 1], dim=-1)
            cam_pcd["xyzw"] = xyzw.reshape(bs, -1, 4)

            if "Color" in cam_images:
                rgb = cam_images["Color"][..., :3]
                rgb = torch.clamp(rgb * 255, 0, 255).to(torch.uint8)
                cam_pcd["rgb"] = rgb.reshape(bs, -1, 3)

            if "Segmentation" in cam_images:
                seg = cam_images["Segmentation"]
                cam_pcd["Segmentation"] = seg.reshape(bs, -1, 4)

            pointcloud_obs[cam_uid] = cam_pcd

        observation["pointcloud"] = pointcloud_obs
        return observation
```

```python
def observation(self, observation: dict):
        # Move camera parameters to device
        camera_params = observation.pop("camera_param")
        camera_params2 = {}
        for cam_uid in camera_params:
            cam2world = camera_params[cam_uid]["cam2world_gl"]
            cam2world = torch.from_numpy(cam2world).to(
                device=self.device, non_blocking=True
            )
            camera_params2[cam_uid] = cam2world

        pointcloud_obs = observation["pointcloud"]
        pointcloud_obs2 = defaultdict(list)
        for cam_uid, cam_pcd in pointcloud_obs.items():
            # Transform coordinates to world space
            xyzw = cam_pcd["xyzw"]  # [B, H*W, 4]
            cam2world = camera_params2[cam_uid]  # [B, 4, 4]
            cam_pcd["xyzw"] = torch.bmm(xyzw, cam2world.transpose(1, 2))
            for k, v in cam_pcd.items():
                pointcloud_obs2[k].append(v)

        for key, value in pointcloud_obs2.items():
            buffer = self._buffer.get(key, None)
            self._buffer[key] = torch.cat(value, dim=1, out=buffer)
            pointcloud_obs2[key] = self._buffer[key]

        observation["pointcloud"] = pointcloud_obs2
        return observation
```

```python
def observation(self, observation):
        raise NotImplementedError
```
```

### stable_baselines3/common/vec_env/maniskill2_wrapper_obs.py

```
def batch_isin(x, inds)
class VecRobotSegmentationObservationWrapper(VecEnvObservationWrapper)
    """Add a binary mask for robot links."""
    def __init__(self, venv, replace)
    def update_robot_link_ids(self, indices)
    def observation_image(self, observation)
    def observation_pointcloud(self, observation)
    def observation(self, observation)
    def reset_wait(self, indices)

```python
def observation_image(self, observation: dict):
        image_obs = observation["image"]
        for cam_images in image_obs.values():
            if "Segmentation" not in cam_images:
                continue
            seg = cam_images["Segmentation"]  # [B, H, W, 4]
            # [B, H, W, 1]
            robot_seg = batch_isin(seg[..., 1:2], self.robot_link_ids)
            if self.replace:
                cam_images.pop("Segmentation")
            cam_images["robot_seg"] = robot_seg
        return observation
```

```python
def observation_pointcloud(self, observation: dict):
        pointcloud_obs = observation["pointcloud"]
        if "Segmentation" not in pointcloud_obs:
            return observation
        seg = pointcloud_obs["Segmentation"]  # [N, 4]
        robot_seg = batch_isin(seg[..., 1:2], self.robot_link_ids)  # [N, 1]
        if self.replace:
            pointcloud_obs.pop("Segmentation")
        pointcloud_obs["robot_seg"] = robot_seg
        return observation
```

```python
def observation(self, observation: dict):
        if "image" in observation:
            observation = self.observation_image(observation)
        if "pointcloud" in observation:
            observation = self.observation_pointcloud(observation)
        return observation
```
```

### stable_baselines3/common/vec_env/stacked_observations.py

```
class StackedObservations()
    """Frame stacking wrapper for data.

Dimension to stack over is either first (channels-first) or
last (channels-last), which is detected automatically using
``common.preprocessing.is_image_space_channels_first`` if
observation is an image space.

:param num_envs: number of environments
:param n_stack: """
    def __init__(self, num_envs, n_stack, observation_space, channels_order)
    def compute_stacking(num_envs, n_stack, observation_space, channels_order)
    def stack_observation_space(self, observation_space)
    def reset(self, observation)
    def update(self, observations, dones, infos)
class StackedDictObservations(StackedObservations)
    """Frame stacking wrapper for dictionary data.

Dimension to stack over is either first (channels-first) or
last (channels-last), which is detected automatically using
``common.preprocessing.is_image_space_channels_first`` if
observation is an image space.

:param num_envs: number of environments
:para"""
    def __init__(self, num_envs, n_stack, observation_space, channels_order)
    def stack_observation_space(self, observation_space)
    def reset(self, observation)
    def update(self, observations, dones, infos)

```python
def stack_observation_space(self, observation_space: spaces.Box) -> spaces.Box:
        """
        Given an observation space, returns a new observation space with stacked observations

        :return: New observation space with stacked dimensions
        """
        low = np.repeat(observation_space.low, self.n_stack, axis=self.repeat_axis)
        high = np.repeat(observation_space.high, self.n_stack, axis=self.repeat_axis)
        return spaces.Box(low=low, high=high, dtype=observation_space.dtype)
```

```python
def stack_observation_space(self, observation_space: spaces.Dict) -> spaces.Dict:
        """
        Returns the stacked verson of a Dict observation space

        :param observation_space: Dict observation space to stack
        :return: stacked observation space
        """
        spaces_dict = {}
        for key, subspace in observation_space.spaces.items():
            low = np.repeat(subspace.low, self.n_stack, axis=self.repeat_axis[key])
            high = np.repeat(subspace.high, self.n_stack, axis=self.repeat_axis[key])
            spaces_dict[key] = spaces.Box(low=low, high=high, dtype=subspace.dtype)
        return spaces.Dict(spaces=spaces_dict)
```
```

### stable_baselines3/common/vec_env/subproc_vec_env.py

```
def _worker(remote, parent_remote, env_fn_wrapper)
class SubprocVecEnv(VecEnv)
    """Creates a multiprocess vectorized wrapper for multiple environments, distributing each environment to its own
process, allowing significant speed up when the environment is computationally complex.

For performance reasons, if your environment is not IO bound, the number of environments should not e"""
    def __init__(self, env_fns, start_method)
    def step_async(self, actions)
    def step_wait(self)
    def seed(self, seed)
    def reset(self)
    def close(self)
    def get_images(self)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def env_method(self, method_name)
    def env_is_wrapped(self, wrapper_class, indices)
    def _get_target_remotes(self, indices)
def _flatten_obs(obs, space)
```

### stable_baselines3/common/vec_env/util.py

```
"""Helpers for dealing with vectorized environments."""
def copy_obs_dict(obs)
def dict_to_obs(obs_space, obs_dict)
def obs_space_info(obs_space)
```

### stable_baselines3/common/vec_env/vec_check_nan.py

```
class VecCheckNan(VecEnvWrapper)
    """NaN and inf checking wrapper for vectorized environment, will raise a warning by default,
allowing you to know from what the NaN of inf originated from.

:param venv: the vectorized environment to wrap
:param raise_exception: Whether or not to raise a ValueError, instead of a UserWarning
:param warn"""
    def __init__(self, venv, raise_exception, warn_once, check_inf)
    def step_async(self, actions)
    def step_wait(self)
    def reset(self)
    def _check_val(self)
```

### stable_baselines3/common/vec_env/vec_extract_dict_obs.py

```
class VecExtractDictObs(VecEnvWrapper)
    """A vectorized wrapper for extracting dictionary observations.

:param venv: The vectorized environment
:param key: The key of the dictionary observation"""
    def __init__(self, venv, key)
    def reset(self)
    def step_wait(self)
```

### stable_baselines3/common/vec_env/vec_frame_stack.py

```
class VecFrameStack(VecEnvWrapper)
    """Frame stacking wrapper for vectorized environment. Designed for image observations.

Uses the StackedObservations class, or StackedDictObservations depending on the observations space

:param venv: the vectorized environment to wrap
:param n_stack: Number of frames to stack
:param channels_order: If"""
    def __init__(self, venv, n_stack, channels_order)
    def step_wait(self)
    def reset(self)
    def close(self)
```

### stable_baselines3/common/vec_env/vec_monitor.py

```
class VecMonitor(VecEnvWrapper)
    """A vectorized monitor wrapper for *vectorized* Gym environments,
it is used to record the episode reward, length, time and other data.

Some environments like `openai/procgen <https://github.com/openai/procgen>`_
or `gym3 <https://github.com/openai/gym3>`_ directly initialize the
vectorized environme"""
    def __init__(self, venv, filename, info_keywords)
    def reset(self)
    def step_wait(self)
    def close(self)
```

### stable_baselines3/common/vec_env/vec_normalize.py

```
class VecNormalize(VecEnvWrapper)
    """A moving average, normalizing wrapper for vectorized environment.
has support for saving/loading moving average,

:param venv: the vectorized environment to wrap
:param training: Whether to update or not the moving average
:param norm_obs: Whether to normalize observation or not (default: True)
:par"""
    def __init__(self, venv, training, norm_obs, norm_reward, clip_obs, clip_reward, gamma, epsilon, norm_obs_keys)
    def _sanity_checks(self)
    def __getstate__(self)
    def __setstate__(self, state)
    def set_venv(self, venv)
    def step_wait(self)
    def _update_reward(self, reward)
    def _normalize_obs(self, obs, obs_rms)
    def _unnormalize_obs(self, obs, obs_rms)
    def normalize_obs(self, obs)
    def normalize_reward(self, reward)
    def unnormalize_obs(self, obs)
    def unnormalize_reward(self, reward)
    def get_original_obs(self)
    def get_original_reward(self)
    def reset(self)
    def load(load_path, venv)
    def save(self, save_path)
    def ret(self)

```python
def _update_reward(self, reward: np.ndarray) -> None:
        """Update reward normalization statistics."""
        self.returns = self.returns * self.gamma + reward
        self.ret_rms.update(self.returns)
```

```python
def normalize_reward(self, reward: np.ndarray) -> np.ndarray:
        """
        Normalize rewards using this VecNormalize's rewards statistics.
        Calling this method does not update statistics.
        """
        if self.norm_reward:
            reward = np.clip(reward / np.sqrt(self.ret_rms.var + self.epsilon), -self.clip_reward, self.clip_reward)
        return reward
```

```python
def unnormalize_reward(self, reward: np.ndarray) -> np.ndarray:
        if self.norm_reward:
            return reward * np.sqrt(self.ret_rms.var + self.epsilon)
        return reward
```

```python
def get_original_reward(self) -> np.ndarray:
        """
        Returns an unnormalized version of the rewards from the most recent step.
        """
        return self.old_reward.copy()
```
```

### stable_baselines3/common/vec_env/vec_transpose.py

```
class VecTransposeImage(VecEnvWrapper)
    """Re-order channels, from HxWxC to CxHxW.
It is required for PyTorch convolution layers.

:param venv:
:param skip: Skip this wrapper if needed as we rely on heuristic to apply it or not,
    which may result in unwanted behavior, see GH issue #671."""
    def __init__(self, venv, skip)
    def transpose_space(observation_space, key)
    def transpose_image(image)
    def transpose_observations(self, observations)
    def step_wait(self)
    def reset(self)
    def close(self)

```python
def transpose_observations(self, observations: Union[np.ndarray, Dict]) -> Union[np.ndarray, Dict]:
        """
        Transpose (if needed) and return new observations.

        :param observations:
        :return: Transposed observations
        """
        # Do nothing
        if self.skip:
            return observations

        if isinstance(observations, dict):
            # Avoid modifying the original object in place
            observations = deepcopy(observations)
            for k in self.image_space_keys:
                observations[k] = self.transpose_image(observations[k])
        else:
            observations = self.transpose_image(observations)
        return observations
```
```

### stable_baselines3/common/vec_env/vec_video_recorder.py

```
class VecVideoRecorder(VecEnvWrapper)
    """Wraps a VecEnv or VecEnvWrapper object to record rendered image as mp4 video.
It requires ffmpeg or avconv to be installed on the machine.

:param venv:
:param video_folder: Where to save videos
:param record_video_trigger: Function that defines when to start recording.
                             """
    def __init__(self, venv, video_folder, record_video_trigger, video_length, name_prefix)
    def reset(self)
    def start_video_recorder(self)
    def _video_enabled(self)
    def step_wait(self)
    def close_video_recorder(self)
    def close(self)
    def __del__(self)
```

### stable_baselines3/networks/pretrain_nets.py

```
class PointNet(Module)
    def __init__(self, point_channel, output_dim)
    def reset_parameters_(self)
    def forward(self, x)
class PointNetMedium(Module)
    def __init__(self, point_channel, output_dim)
    def reset_parameters_(self)
    def forward(self, x)
class PointNetLarge(Module)
    def __init__(self, point_channel, output_dim)
    def reset_parameters_(self)
    def forward(self, x)
```

### stable_baselines3/simple_callback.py

```
class SimpleCallback(BaseCallback)
    def __init__(self, verbose, model_save_path, model_save_freq, rollout)
    def _on_rollout_end(self)
    def _on_training_end(self)
    def save_model(self)
    def _on_step(self)
```