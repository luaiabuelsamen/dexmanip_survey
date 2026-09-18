# humanplus_2024

source: https://github.com/MarkFzp/humanplus


commit: ff7148903303ac2951857cf0b7df686d77323917


## README

# HumanPlus: Humanoid Shadowing and Imitation from Humans


#### Project Website: https://humanoid-ai.github.io/

This repository contains the updating implementation for the Humanoid Shadowing Transformer (HST) and the Humanoid Imitation Transformer (HIT), along with instructions for whole-body pose estimation and the associated hardware codebase.


## Humanoid Shadowing Transformer (HST)
Reinforcement learning in simulation is based on [legged_gym](https://github.com/leggedrobotics/legged_gym) and [rsl_rl](https://github.com/leggedrobotics/rsl_rl).
#### Installation
Install IsaacGym v4 first from the [official source](https://developer.nvidia.com/isaac-gym). Place the isaacgym fold inside the HST folder.

    cd HST/rsl_rl && pip install -e . 
    cd HST/legged_gym && pip install -e .

#### Example Usages
To train HST:

    python legged_gym/scripts/train.py --run_name 0001_test --headless --sim_device cuda:0 --rl_device cuda:0

To play a trained policy:

    python legged_gym/scripts/play.py --run_name 0001_test --checkpoint -1 --headless --sim_device cuda:0 --rl_device cuda:0


## Humanoid Imitation Transformer (HIT)
Imitation learning in the real world is based on [ACT repo](https://github.com/tonyzhaozh/act) and [Mobile ALOHA repo](https://github.com/MarkFzp/act-plus-plus).
#### Installation
    conda create -n HIT python=3.8.10
    conda activate HIT
    pip install torchvision
    pip install torch
    pip install pyquaternion
    pip install pyyaml
    pip install rospkg
    pip install pexpect
    pip install mujoco==2.3.7
    pip install dm_control==1.0.14
    pip install opencv-python
    pip install matplotlib
    pip install einops
    pip install packaging
    pip install h5py
    pip install ipython
    pip install getkey
    pip install wandb
    pip install chardet
    pip install h5py_cache
    cd HIT/detr && pip install -e .
#### Example Usages
Collect your own data or download our dataset from [here](https://drive.google.com/drive/folders/1i3eGTd9Nl_tSieoE0grxuKqUAumBr2EV?usp=drive_link) and place it in the HIT folder.

To set up a new terminal, run:

    conda activate HIT
    cd HIT

To train HIT:

    # Fold Clothes task
    python imitate_episodes_h1_train.py --task_name data_fold_clothes --ckpt_dir fold_clothes/ --policy_class HIT --chunk_size 50 --hidden_dim 512 --batch_size 48 --dim_feedforward 512 --lr 1e-5 --seed 0 --num_steps 100000 --eval_every 100000 --validate_every 1000 --save_every 10000 --no_encoder --backbone resnet18 --same_backbones --use_pos_embd_image 1 --use_pos_embd_action 1 --dec_layers 6 --gpu_id 0 --feature_loss_weight 0.005 --use_mask --data_aug --wandb

## Hardware Codebase
Hardware codebase is based on [unitree_ros2](https://github.com/unitreerobotics/unitree_ros2).

#### Installation

install [unitree_sdk](https://github.com/unitreerobotics/unitree_sdk2)

install [unitree_ros2](https://support.unitree.com/home/en/developer/ROS2_service)

    conda create -n lowlevel python=3.8
    conda activate lowlevel

install [nvidia-jetpack](https://docs.nvidia.com/jetson/archives/jetpack-archived/jetpack-461/install-jetpack/index.html)

install torch==1.11.0 and torchvision==0.12.0:  
please refer to the following links:   
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048
https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html

#### Example Usages
Put your trained policy in the `hardware-script/ckpt` folder and rename it to `policy.pt`

    conda activate lowlevel
    cd hardware-script
    python hardware_whole_body.py --task_name stand


## Pose Estimation
For body pose estimation, please refer to [WHAM](https://github.com/yohanshin/WHAM). 
For hand pose estimation, please refer to [HaMeR](https://github.com/geopavlakos/hamer). 


## File tree (depth 3, assets pruned)

```
.gitignore
HIT/
  constants.py
  detr/
    LICENSE
    README.md
    build/
    main.py
    models/
    setup.py
    util/
  imitate_episodes_h1_train.py
  model_util.py
  policy.py
  utils.py
HST/
  legged_gym/
    .gitattributes
    legged_gym/
    resources/
    setup.py
  rsl_rl/
    rsl_rl/
    setup.py
README.md
hardware/
  crc_module.so
  dynamixel_client.py
  hardware_whole_body.py
  web_hand.py
```

## Config files (0)


## Python signatures and reward/observation bodies (23 files)


### HIT/imitate_episodes_h1_train.py

```
def forward_pass(data, policy)
def train_bc(train_dataloader, val_dataloader, config)
def repeater(data_loader)
def main_train(args)
```

### HIT/policy.py

```
class HITPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def forward_inf(self, qpos, image)
    def configure_optimizers(self)
    def serialize(self)
    def deserialize(self, model_dict)
class DiffusionPolicy(Module)
    def __init__(self, args_override)
    def configure_optimizers(self)
    def __call__(self, qpos, image, actions, is_pad)
    def serialize(self)
    def deserialize(self, model_dict)
class ACTPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad, vq_sample)
    def forward_inf(self, qpos, image)
    def configure_optimizers(self)
    def vq_encode(self, qpos, actions, is_pad)
    def serialize(self)
    def deserialize(self, model_dict)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
```

### HST/legged_gym/legged_gym/envs/a1/a1_config.py

```
class A1RoughCfg(LeggedRobotCfg)
class A1RoughCfgPPO(LeggedRobotCfgPPO)
```

### HST/legged_gym/legged_gym/envs/anymal_b/anymal_b_config.py

```
class AnymalBRoughCfg(AnymalCRoughCfg)
class AnymalBRoughCfgPPO(AnymalCRoughCfgPPO)
```

### HST/legged_gym/legged_gym/envs/anymal_c/anymal.py

```
class Anymal(LeggedRobot)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def reset_idx(self, env_ids)
    def _init_buffers(self)
    def _compute_torques(self, actions)
```

### HST/legged_gym/legged_gym/envs/anymal_c/flat/anymal_c_flat_config.py

```
class AnymalCFlatCfg(AnymalCRoughCfg)
class AnymalCFlatCfgPPO(AnymalCRoughCfgPPO)
```

### HST/legged_gym/legged_gym/envs/anymal_c/mixed_terrains/anymal_c_rough_config.py

```
class AnymalCRoughCfg(LeggedRobotCfg)
class AnymalCRoughCfgPPO(LeggedRobotCfgPPO)
```

### HST/legged_gym/legged_gym/envs/base/base_config.py

```
class BaseConfig()
    def __init__(self)
    def init_member_classes(obj)
```

### HST/legged_gym/legged_gym/envs/base/base_task.py

```
class BaseTask()
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def get_observations(self)
    def get_privileged_observations(self)
    def reset_idx(self, env_ids)
    def reset(self)
    def step(self, actions)
    def create_sim(self)
    def render(self, sync_frame_time)

```python
def get_observations(self):
        return self.obs_buf
```

```python
def get_privileged_observations(self):
        return self.privileged_obs_buf
```
```

### HST/legged_gym/legged_gym/envs/base/legged_robot.py

```
class LeggedRobot(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def step(self, actions)
    def post_physics_step(self)
    def check_termination(self)
    def reset_idx(self, env_ids)
    def compute_reward(self)
    def compute_observations(self)
    def create_sim(self)
    def set_camera(self, position, lookat)
    def _process_rigid_shape_props(self, props, env_id)
    def _process_dof_props(self, props, env_id)
    def _process_rigid_body_props(self, props, env_id)
    def _post_physics_step_callback(self)
    def _resample_commands(self, env_ids)
    def _compute_torques(self, actions)
    def _reset_dofs(self, env_ids)
    def _reset_root_states(self, env_ids)
    def _push_robots(self)
    def _update_terrain_curriculum(self, env_ids)
    def update_command_curriculum(self, env_ids)
    def _get_noise_scale_vec(self, cfg)
    def _init_buffers(self)
    def _prepare_reward_function(self)
    def _create_ground_plane(self)
    def _create_heightfield(self)
    def _create_trimesh(self)
    def _create_envs(self)
    def _get_env_origins(self)
    def _parse_cfg(self, cfg)
    def _draw_debug_vis(self)
    def _init_height_points(self)
    def _get_heights(self, env_ids)
    def _reward_lin_vel_z(self)
    def _reward_ang_vel_xy(self)
    def _reward_orientation(self)
    def _reward_base_height(self)
    def _reward_torques(self)
    def _reward_dof_vel(self)
    def _reward_dof_acc(self)
    def _reward_action_rate(self)
    def _reward_collision(self)
    def _reward_termination(self)
    def _reward_dof_pos_limits(self)
    def _reward_dof_vel_limits(self)
    def _reward_torque_limits(self)
    def _reward_tracking_lin_vel(self)
    def _reward_tracking_ang_vel(self)
    def _reward_feet_air_time(self)
    def _reward_stumble(self)
    def _reward_stand_still(self)
    def _reward_feet_contact_forces(self)

```python
def compute_reward(self):
        """ Compute rewards
            Calls each reward function which had a non-zero scale (processed in self._prepare_reward_function())
            adds each terms to the episode sums and to the total reward
        """
        self.rew_buf[:] = 0.
        for i in range(len(self.reward_functions)):
            name = self.reward_names[i]
            rew = self.reward_functions[i]() * self.reward_scales[name]
            self.rew_buf += rew
            self.episode_sums[name] += rew
        if self.cfg.rewards.only_positive_rewards:
            self.rew_buf[:] = torch.clip(self.rew_buf[:], min=0.)
        # add termination reward after clipping
        if "termination" in self.reward_scales:
            rew = self._reward_termination() * self.reward_scales["termination"]
            self.rew_buf += rew
            self.episode_sums["termination"] += rew
```

```python
def compute_observations(self):
        """ Computes observations
        """
        self.obs_buf = torch.cat((  self.base_lin_vel * self.obs_scales.lin_vel,  # [0:3]
                                    self.base_ang_vel  * self.obs_scales.ang_vel,  # [3:6]
                                    self.projected_gravity,  # [6:9]
                                    self.commands[:, :3] * self.commands_scale,  # [9:12]
                                    (self.dof_pos - self.default_dof_pos) * self.obs_scales.dof_pos,  # [12:12+num_dof]
                                    self.dof_vel * self.obs_scales.dof_vel,  # [12+num_dof:12+2*num_dof]
                                    self.actions,  # [12+2*num_dof:12+3*num_dof]
                                    ),dim=-1)
        # add perceptive inputs if not blind
        if self.cfg.terrain.measure_heights:
            heights = torch.clip(self.root_states[:, 2].unsqueeze(1) - 0.5 - self.measured_heights, -1, 1.) * self.obs_scales.height_measurements
            self.obs_buf = torch.cat((self.obs_buf, heights), dim=-1)
        # add noise if needed
        if self.add_noise:
            self.obs_buf += (2 * torch.rand_like(self.obs_buf) - 1) * self.noise_scale_vec
```

```python
def _prepare_reward_function(self):
        """ Prepares a list of reward functions, whcih will be called to compute the total reward.
            Looks for self._reward_<REWARD_NAME>, where <REWARD_NAME> are names of all non zero reward scales in the cfg.
        """
        # remove zero scales + multiply non-zero ones by dt
        for key in list(self.reward_scales.keys()):
            scale = self.reward_scales[key]
            if scale==0:
                self.reward_scales.pop(key) 
            else:
                self.reward_scales[key] *= self.dt
        # prepare list of functions
        self.reward_functions = []
        self.reward_names = []
        for name, scale in self.reward_scales.items():
            if name=="termination":
                continue
            self.reward_names.append(name)
            name = '_reward_' + name
            self.reward_functions.append(getattr(self, name))

        # reward episode sums
        self.episode_sums = {name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
                             for name in self.reward_scales.keys()}
```

```python
def _reward_lin_vel_z(self):
        # Penalize z axis base linear velocity
        return torch.square(self.base_lin_vel[:, 2])
```

```python
def _reward_ang_vel_xy(self):
        # Penalize xy axes base angular velocity
        return torch.sum(torch.square(self.base_ang_vel[:, :2]), dim=1)
```

```python
def _reward_orientation(self):
        # Penalize non flat base orientation
        return torch.sum(torch.square(self.projected_gravity[:, :2]), dim=1)
```

```python
def _reward_base_height(self):
        # Penalize base height away from target
        base_height = torch.mean(self.root_states[:, 2].unsqueeze(1) - self.measured_heights, dim=1)
        return torch.square(base_height - self.cfg.rewards.base_height_target)
```

```python
def _reward_torques(self):
        # Penalize torques
        return torch.sum(torch.square(self.torques), dim=1)
```

```python
def _reward_dof_vel(self):
        # Penalize dof velocities
        return torch.sum(torch.square(self.dof_vel), dim=1)
```

```python
def _reward_dof_acc(self):
        # Penalize dof accelerations
        return torch.sum(torch.square((self.last_dof_vel - self.dof_vel) / self.dt), dim=1)
```

```python
def _reward_action_rate(self):
        # Penalize changes in actions
        return torch.sum(torch.square(self.last_actions - self.actions), dim=1)
```

```python
def _reward_collision(self):
        # Penalize collisions on selected bodies
        return torch.sum(1.*(torch.norm(self.contact_forces[:, self.penalised_contact_indices, :], dim=-1) > 0.1), dim=1)
```

```python
def _reward_termination(self):
        # Terminal reward / penalty
        return self.reset_buf * ~self.time_out_buf
```

```python
def _reward_dof_pos_limits(self):
        # Penalize dof positions too close to the limit
        out_of_limits = -(self.dof_pos - self.dof_pos_limits[:, 0]).clip(max=0.) # lower limit
        out_of_limits += (self.dof_pos - self.dof_pos_limits[:, 1]).clip(min=0.)
        return torch.sum(out_of_limits, dim=1)
```

```python
def _reward_dof_vel_limits(self):
        # Penalize dof velocities too close to the limit
        # clip to max error = 1 rad/s per joint to avoid huge penalties
        return torch.sum((torch.abs(self.dof_vel) - self.dof_vel_limits*self.cfg.rewards.soft_dof_vel_limit).clip(min=0., max=1.), dim=1)
```

```python
def _reward_torque_limits(self):
        # penalize torques too close to the limit
        return torch.sum((torch.abs(self.torques) - self.torque_limits*self.cfg.rewards.soft_torque_limit).clip(min=0.), dim=1)
```

```python
def _reward_tracking_lin_vel(self):
        # Tracking of linear velocity commands (xy axes)
        lin_vel_error = torch.sum(torch.square(self.commands[:, :2] - self.base_lin_vel[:, :2]), dim=1)
        return torch.exp(-lin_vel_error/self.cfg.rewards.tracking_sigma)
```

```python
def _reward_tracking_ang_vel(self):
        # Tracking of angular velocity commands (yaw) 
        ang_vel_error = torch.square(self.commands[:, 2] - self.base_ang_vel[:, 2])
        return torch.exp(-ang_vel_error/self.cfg.rewards.tracking_sigma)
```

```python
def _reward_feet_air_time(self):
        # Reward long steps
        # Need to filter the contacts because the contact reporting of PhysX is unreliable on meshes
        contact = self.contact_forces[:, self.feet_indices, 2] > 1.
        contact_filt = torch.logical_or(contact, self.last_contacts) 
        self.last_contacts = contact
        first_contact = (self.feet_air_time > 0.) * contact_filt
        self.feet_air_time += self.dt
        rew_airTime = torch.sum((self.feet_air_time - 0.5) * first_contact, dim=1) # reward only on first contact with the ground
        rew_airTime *= torch.norm(self.commands[:, :2], dim=1) > 0.1 #no reward for zero command
        self.feet_air_time *= ~contact_filt
        return rew_airTime
```

```python
def _reward_stumble(self):
        # Penalize feet hitting vertical surfaces
        return torch.any(torch.norm(self.contact_forces[:, self.feet_indices, :2], dim=2) >\
             5 *torch.abs(self.contact_forces[:, self.feet_indices, 2]), dim=1)
```

```python
def _reward_stand_still(self):
        # Penalize motion at zero commands
        return torch.sum(torch.abs(self.dof_pos - self.default_dof_pos), dim=1) * (torch.norm(self.commands[:, :2], dim=1) < 0.1)
```

```python
def _reward_feet_contact_forces(self):
        # penalize high contact forces
        return torch.sum((torch.norm(self.contact_forces[:, self.feet_indices, :], dim=-1) -  self.cfg.rewards.max_contact_force).clip(min=0.), dim=1)
```
```

### HST/legged_gym/legged_gym/envs/base/legged_robot_config.py

```
class LeggedRobotCfg(BaseConfig)
class LeggedRobotCfgPPO(BaseConfig)
```

### HST/legged_gym/legged_gym/envs/cassie/cassie.py

```
class Cassie(LeggedRobot)
    def _reward_no_fly(self)

```python
def _reward_no_fly(self):
        contacts = self.contact_forces[:, self.feet_indices, 2] > 0.1
        single_contact = torch.sum(1.*contacts, dim=1)==1
        return 1.*single_contact
```
```

### HST/legged_gym/legged_gym/envs/cassie/cassie_config.py

```
class CassieRoughCfg(LeggedRobotCfg)
class CassieRoughCfgPPO(LeggedRobotCfgPPO)
```

### HST/legged_gym/legged_gym/envs/h1/h1.py

```
def sample_int_from_float(x)
class H1()
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def _super_init(self, cfg, sim_params, physics_engine, sim_device, headless)
    def get_observations(self)
    def get_privileged_observations(self)
    def _init_target_jt(self)
    def update_target_jt(self, reset_env_ids)
    def step(self, actions)
    def post_physics_step(self)
    def check_termination(self)
    def reset(self)
    def reset_idx(self, env_ids)
    def compute_reward(self)
    def compute_observations(self)
    def get_body_orientation(self, return_yaw)
    def create_sim(self)
    def set_camera(self, position, lookat)
    def _process_rigid_shape_props(self, props, env_id)
    def _process_dof_props(self, props, env_id)
    def _process_rigid_body_props(self, props, env_id)
    def _post_physics_step_callback(self)
    def _resample_commands(self, env_ids)
    def _compute_torques(self, actions)
    def _reset_dofs(self, env_ids)
    def _reset_root_states(self, env_ids)
    def _push_robots(self)
    def _update_terrain_curriculum(self, env_ids)
    def update_command_curriculum(self, env_ids)
    def _get_noise_scale_vec(self, cfg)
    def _init_buffers(self)
    def _prepare_reward_function(self)
    def _create_ground_plane(self)
    def _create_heightfield(self)
    def _create_trimesh(self)
    def _create_envs(self)
    def _get_env_origins(self)
    def _parse_cfg(self, cfg)
    def _draw_debug_vis(self)
    def _init_height_points(self)
    def _get_heights(self, env_ids)
    def render(self, sync_frame_time)
    def _reward_lin_vel_z(self)
    def _reward_ang_vel_xy(self)
    def _reward_orientation(self)
    def _reward_base_height(self)
    def _reward_torques(self)
    def _reward_dof_vel(self)
    def _reward_dof_acc(self)
    def _reward_action_rate(self)
    def _reward_collision(self)
    def _reward_termination(self)
    def _reward_dof_pos_limits(self)
    def _reward_dof_vel_limits(self)
    def _reward_torque_limits(self)
    def _reward_tracking_lin_vel(self)
    def _reward_tracking_ang_vel(self)
    def _reward_feet_air_time(self)
    def _reward_stumble(self)
    def _reward_stand_still(self)
    def _reward_feet_contact_forces(self)
    def _reward_target_jt(self)

```python
def get_observations(self):
        return self.obs_history_buf
```

```python
def get_privileged_observations(self):
        return None
```

```python
def compute_reward(self):
        """ Compute rewards
            Calls each reward function which had a non-zero scale (processed in self._prepare_reward_function())
            adds each terms to the episode sums and to the total reward
        """
        self.rew_buf[:] = 0.
        for i in range(len(self.reward_functions)):
            name = self.reward_names[i]
            unscaled_rew, metric = self.reward_functions[i]()
            rew = unscaled_rew * self.reward_scales[name]
            self.rew_buf += rew
            self.episode_sums[name] += rew
            self.episode_metrics[name] = metric.mean().item()
        if self.cfg.rewards.only_positive_rewards:
            self.rew_buf[:] = torch.clip(self.rew_buf[:], min=0.)
        # add termination reward after clipping
        if "termination" in self.reward_scales:
            rew = self._reward_termination() * self.reward_scales["termination"]
            self.rew_buf += rew
            self.episode_sums["termination"] += rew
```

```python
def compute_observations(self):
        """ Computes observations
        """
        self.obs_buf = torch.cat((  self.base_orn_rp * self.obs_scales.orn,  # [0:2]
                                    self.base_ang_vel * self.obs_scales.ang_vel,  # [2:5]
                                    self.commands[:, :3] * self.commands_scale[:3],  # [5:8]
                                    (self.dof_pos - self.default_dof_pos) * self.obs_scales.dof_pos,  # [8:8+num_dofs]
                                    self.dof_vel * self.obs_scales.dof_vel,  # [8+num_dofs:8+2*num_dofs]
                                    self.actions,  # [8+2*num_dofs:8+3*num_dofs]
                                    ),dim=-1)
        # print(self.target_jt_j[:3], self.target_jt_i[:3])
        self.obs_buf = torch.cat([self.obs_buf, self.delayed_obs_target_jt * self.obs_scales.dof_pos], dim=-1)

        # add perceptive inputs if not blind
        if self.cfg.terrain.measure_heights:
            heights = torch.clip(self.root_states[:, 2].unsqueeze(1) - 0.5 - self.measured_heights, -1, 1.) * self.obs_scales.height_measurements
            self.obs_buf = torch.cat((self.obs_buf, heights), dim=-1)
        # add noise if needed
        if self.cfg.noise.add_noise:
            self.obs_buf += (2 * torch.rand_like(self.obs_buf) - 1) * self.noise_scale_vec

        self.obs_history_buf = torch.cat([
            self.obs_history_buf[:, 1:],
            self.obs_buf.unsqueeze(1)
        ], dim=1)
```

```python
def _prepare_reward_function(self):
        """ Prepares a list of reward functions, whcih will be called to compute the total reward.
            Looks for self._reward_<REWARD_NAME>, where <REWARD_NAME> are names of all non zero reward scales in the cfg.
        """
        # remove zero scales + multiply non-zero ones by dt
        for key in list(self.reward_scales.keys()):
            scale = self.reward_scales[key]
            if scale==0:
                self.reward_scales.pop(key) 
            else:
                self.reward_scales[key] *= self.dt
        # prepare list of functions
        self.reward_functions = []
        self.reward_names = []
        for name, scale in self.reward_scales.items():
            if name=="termination":
                continue
            self.reward_names.append(name)
            name = '_reward_' + name
            self.reward_functions.append(getattr(self, name))

        # reward episode sums
        self.episode_sums = {name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
                             for name in self.reward_scales.keys()}
        self.episode_metrics = {name: 0 for name in self.reward_scales.keys()}
```

```python
def _reward_lin_vel_z(self):
        # Penalize z axis base linear velocity
        return torch.square(self.base_lin_vel[:, 2])
```

```python
def _reward_ang_vel_xy(self):
        # Penalize xy axes base angular velocity
        return torch.sum(torch.square(self.base_ang_vel[:, :2]), dim=1)
```

```python
def _reward_orientation(self):
        # Penalize non flat base orientation
        return torch.sum(torch.square(self.projected_gravity[:, :2]), dim=1)
```

```python
def _reward_base_height(self):
        # Penalize base height away from target
        base_height = torch.mean(self.root_states[:, 2].unsqueeze(1) - self.measured_heights, dim=1)
        return torch.square(base_height - self.cfg.rewards.base_height_target)
```

```python
def _reward_torques(self):
        # Penalize torques
        return torch.sum(torch.square(self.torques), dim=1)
```

```python
def _reward_dof_vel(self):
        # Penalize dof velocities
        return torch.sum(torch.square(self.dof_vel), dim=1)
```

```python
def _reward_dof_acc(self):
        # Penalize dof accelerations
        return torch.sum(torch.square((self.last_dof_vel - self.dof_vel) / self.dt), dim=1)
```

```python
def _reward_action_rate(self):
        # Penalize changes in actions
        return torch.sum(torch.square(self.last_actions - self.actions), dim=1)
```

```python
def _reward_collision(self):
        # Penalize collisions on selected bodies
        return torch.sum(1.*(torch.norm(self.contact_forces[:, self.penalized_contact_indices, :], dim=-1) > 0.1), dim=1)
```

```python
def _reward_termination(self):
        # Terminal reward / penalty
        return self.reset_buf * ~self.time_out_buf
```

```python
def _reward_dof_pos_limits(self):
        # Penalize dof positions too close to the limit
        out_of_limits = -(self.dof_pos - self.dof_pos_limits[:, 0]).clip(max=0.) # lower limit
        out_of_limits += (self.dof_pos - self.dof_pos_limits[:, 1]).clip(min=0.)
        return torch.sum(out_of_limits, dim=1)
```

```python
def _reward_dof_vel_limits(self):
        # Penalize dof velocities too close to the limit
        # clip to max error = 1 rad/s per joint to avoid huge penalties
        return torch.sum((torch.abs(self.dof_vel) - self.dof_vel_limits*self.cfg.rewards.soft_dof_vel_limit).clip(min=0., max=1.), dim=1)
```

```python
def _reward_torque_limits(self):
        # penalize torques too close to the limit
        return torch.sum((torch.abs(self.torques) - self.torque_limits*self.cfg.rewards.soft_torque_limit).clip(min=0.), dim=1)
```

```python
def _reward_tracking_lin_vel(self):
        # Tracking of linear velocity commands (xy axes)
        lin_vel_error = torch.sum(torch.square(self.commands[:, :2] - self.base_lin_vel[:, :2]), dim=1)
        return torch.exp(-lin_vel_error/self.cfg.rewards.tracking_sigma), lin_vel_error
```

```python
def _reward_tracking_ang_vel(self):
        # Tracking of angular velocity commands (yaw) 
        ang_vel_error = torch.square(self.commands[:, 2] - self.base_ang_vel[:, 2])
        return torch.exp(-ang_vel_error/self.cfg.rewards.tracking_sigma), ang_vel_error
```

```python
def _reward_feet_air_time(self):
        # Reward long steps
        # Need to filter the contacts because the contact reporting of PhysX is unreliable on meshes
        contact = self.contact_forces[:, self.feet_indices, 2] > 1.
        contact_filt = torch.logical_or(contact, self.last_contacts) 
        self.last_contacts = contact
        first_contact = (self.feet_air_time > 0.) * contact_filt
        self.feet_air_time += self.dt
        rew_airTime = torch.sum((self.feet_air_time - 0.5) * first_contact, dim=1) # reward only on first contact with the ground
        rew_airTime *= torch.norm(self.commands[:, :2], dim=1) > 0.1 #no reward for zero command
        self.feet_air_time *= ~contact_filt
        return rew_airTime
```

```python
def _reward_stumble(self):
        # Penalize feet hitting vertical surfaces
        return torch.any(torch.norm(self.contact_forces[:, self.feet_indices, :2], dim=2) >\
             5 *torch.abs(self.contact_forces[:, self.feet_indices, 2]), dim=1)
```

```python
def _reward_stand_still(self):
        # Penalize motion at zero commands
        return torch.sum(torch.abs(self.dof_pos - self.default_dof_pos), dim=1) * (torch.norm(self.commands[:, :2], dim=1) < 0.1)
```

```python
def _reward_feet_contact_forces(self):
        # penalize high contact forces
        return torch.sum((torch.norm(self.contact_forces[:, self.feet_indices, :], dim=-1) -  self.cfg.rewards.max_contact_force).clip(min=0.), dim=1)
```

```python
def _reward_target_jt(self):
        # Penalize distance to target joint angles
        target_jt_error = torch.mean(torch.abs(self.dof_pos - self.target_jt), dim=1)
        return torch.exp(-4 * target_jt_error), target_jt_error
```
```

### HST/legged_gym/legged_gym/envs/h1/h1_config.py

```
class H1RoughCfg(BaseConfig)
class H1RoughCfgPPO(BaseConfig)
```

### HST/legged_gym/legged_gym/scripts/train.py

```
def train(args)
```

### HST/legged_gym/legged_gym/tests/test_env.py

```
def test_env(args)
```

### HST/legged_gym/legged_gym/utils/task_registry.py

```
class TaskRegistry()
    def __init__(self)
    def register(self, name, task_class, env_cfg, train_cfg, path)
    def get_task_class(self, name)
    def get_cfgs(self, name, load_run)
    def make_env(self, name, args, env_cfg)
    def make_alg_runner(self, env, name, args, train_cfg, log_root)
```

### HST/rsl_rl/rsl_rl/env/vec_env.py

```
class VecEnv(ABC)
    def step(self, actions)
    def reset(self, env_ids)
    def get_observations(self)
    def get_privileged_observations(self)

```python
def get_observations(self) -> torch.Tensor:
        pass
```

```python
def get_privileged_observations(self) -> Union[torch.Tensor, None]:
        pass
```
```

### HST/rsl_rl/rsl_rl/runners/on_policy_runner.py

```
class OnPolicyRunner()
    def __init__(self, env, train_cfg, log_dir, device)
    def learn(self, num_learning_iterations, init_at_random_ep_len)
    def log(self, locs, width, pad)
    def save(self, path, infos)
    def load(self, path, load_optimizer)
    def get_inference_policy(self, device)
```

### hardware/web_hand.py

```
def openSerial(port, baudrate)
def writeRegister(ser, id, add, num, val)
def readRegister(ser, id, add, num, mute)
def write6(ser, id, str, val)
def read6(ser, id, str)
```