# physhoi_2023

source: https://github.com/wyhuai/PhysHOI


commit: 6095c605e22bd01f78ed356e8b08250edf3c5da6


## README

# Human-Object Interaction Imitation

### 📖[*Paper*](https://arxiv.org/abs/2312.04393)|🖼️[*Project Page*](https://wyhuai.github.io/physhoi-page/)

This repository contains the **code** and **dataset** release for the paper: "PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction"

Our whole-body humanoid follows the **SMPL-X** kinematic tree and has a total of **51x3 DoF** actuators, with fully **dextrous hands**.

🏀 Now simulated humanoids can learn diverse basketball interactions **without designing task-specific rewards!**

![image](https://github.com/wyhuai/PhysHOI_dev/assets/95485229/6013e448-05ed-4a12-9164-aa5b34896598)


## TODOs

- [ ] Add more data to the BallPlay dataset.

- [ ] Provide a physically rectified version of basic BallPlay (using PhysHOI).

- [x] Release the basic BallPlay dataset.

- [x] Release training and evaluation code. 


## Requirements 🖥️

It is suggested to perform inference with a graphical interface, which may need a local computer with a screen.

You may need an NVIDIA GPU. The inference needs at least 6G memory. The training needs at least 12G memory (with 1024 envs).

## Installation 💽

Download Isaac Gym from the [website](https://developer.nvidia.com/isaac-gym), then
follow the installation instructions.

Once Isaac Gym is installed, install the external dependencies for this repo:

```
pip install -r requirements.txt
```


## PhysHOI 🎯

### Pre-Trained Models 📁
Download the trained models from this [link](https://drive.google.com/file/d/1jPnzd6PVVpiWNA1-MTVuUgIR_GOJMcLu/view?usp=sharing), unzip the files, and put them into `physhoi/data/models/`. The directory structure should be like `physhoi/data/models/backdribble/nn/PhysHOI.pth`, `physhoi/data/models/pass/nn/PhysHOI.pth`, etc.

### Inference ⛹️‍♂️

#### Basic Evaluation ⛹️‍♂️
For toss, fingerspin, pass, walkpick, and backspin, use the following command. Please change the `[task]` correspondingly.
```
python physhoi/run.py --test --task PhysHOI_BallPlay --num_envs 16 --cfg_env physhoi/data/cfg/physhoi.yaml --cfg_train physhoi/data/cfg/train/rlg/physhoi.yaml --motion_file physhoi/data/motions/BallPlay/[task].pt --checkpoint physhoi/data/models/[task]/nn/PhysHOI.pth
```
For rebound, we need to give the ball an initial velocity, otherwise it will fall vertically downward:
```
python physhoi/run.py --test --task PhysHOI_BallPlay --num_envs 16 --cfg_env physhoi/data/cfg/physhoi.yaml --cfg_train physhoi/data/cfg/train/rlg/physhoi.yaml --motion_file physhoi/data/motions/BallPlay/rebound.pt --checkpoint physhoi/data/models/rebound/nn/PhysHOI.pth --init_vel
```
For changeleg, we provide a trained model that use 60hz control frequency and 60fps data frame rate:
```
python physhoi/run.py --test --task PhysHOI_BallPlay --num_envs 16 --cfg_env physhoi/data/cfg/physhoi_60hz.yaml --cfg_train physhoi/data/cfg/train/rlg/physhoi.yaml --motion_file physhoi/data/motions/BallPlay/changeleg.pt --checkpoint physhoi/data/models/changeleg_60fps/nn/PhysHOI.pth
```
For backdribble, we provide a trained model that use 30hz control frequency and 25fps data frame rate:
```
python physhoi/run.py --test --task PhysHOI_BallPlay --num_envs 16 --cfg_env physhoi/data/cfg/physhoi.yaml --cfg_train physhoi/data/cfg/train/rlg/physhoi.yaml --motion_file physhoi/data/motions/BallPlay/backdribble.pt --checkpoint physhoi/data/models/backdribble/nn/PhysHOI.pth --frames_scale 1.
```

#### Other Options 💡
To view the HOI dataset, add `--play_dataset`.

To throw projectiles at the humanoid, add `--projtype Mouse`, and keep on clicking the screen with your mouse:

To change the size of the ball, add `--ball_size 1.5`, and you can change the value as you like:

To test with different data frame rates, change the value of `--frames_scale` as you like, e.g., 1.5.

To save the images, add `--save_images` to the command, and the images will be saved in `physhoi/data/images`.

To transform the images into a video, run the following command, and the video can be found in `physhoi/data/videos`.
```
python physhoi/utils/make_video.py --image_path physhoi/data/images/backdribble --fps 30
```

&nbsp;

### Training 🏋️

All tasks share the same training code and most of the Hyper-parameters. To train the model, run the following command, and you may change the `--motion_file` to different HOI data: 
```
python physhoi/run.py --task PhysHOI_BallPlay --cfg_env physhoi/data/cfg/physhoi.yaml --cfg_train physhoi/data/cfg/train/rlg/physhoi.yaml --motion_file physhoi/data/motions/BallPlay/toss.pt --headless
```
During the training, the latest checkpoint PhysHOI.pth will be regularly saved to output/, along with a Tensorboard log.

It takes different epochs to reach convergence depending on the difficulty and data quality. For example, it takes 10000 epochs for toss and backdribble to converge, which takes about 9 hours on an NVIDIA 4090 Ti GPU.

#### Tips for Hyper-Parameters 💡
- For fingerspin, `cg2` is suggested to be `0.01`, considering the default contact graph is not detailed enough for finger-level operations.
- For walkpick, `stateInit` is suggested to be Random, due to the data inaccuracy.
- Too large `cg2` and `cg2` may yield unnatural movements; Too small `cg2` and `cg2` may lead to fail grabs or false interaction. 

&nbsp;

### The BallPlay dataset 🏀

The basic BallPlay HOI dataset, including 8 human-basketball interactions, is placed in `physhoi/data/motions/BallPlay`. The frame rate is 25 FPS. The contact label denotes the contact between the ball and hands. The details of the data structure can be found in function `_load_motion` in `physhoi/env/tasks/physhoi.py`. The humanoid robot and basketball model are placed in `physhoi/data/assets/smplx/smplx_capsule.xml` and `physhoi/data/assets/mjcf/ball.urdf`, respectively. 

&nbsp;

## References
If you find this repository useful for your research, please cite the following work.
```
@article{wang2023physhoi,
  author    = {Wang, Yinhuai and Lin, Jing and Zeng, Ailing and Luo, Zhengyi and Zhang, Jian and Zhang, Lei},
  title     = {PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction},
  journal   = {arXiv preprint arXiv:2312.04393},
  year      = {2023},
}
```
The code implementation is based on ASE:
- https://github.com/nv-tlabs/ASE

The SMPL-X humanoid robot is generated using UHC:
- https://github.com/ZhengyiLuo/UniversalHumanoidControl

Further extension:
- https://github.com/wyhuai/SkillMimic




## File tree (depth 3, assets pruned)

```
LICENSE.txt
README.md
physhoi/
  __init__.py
  env/
    tasks/
  learning/
    amp_datasets.py
    common_agent.py
    common_player.py
    physhoi_agent.py
    physhoi_models.py
    physhoi_network_builder.py
    physhoi_players.py
    replay_buffer.py
  run.py
  utils/
    __init__.py
    config.py
    gym_util.py
    logger.py
    make_video.py
    motion_lib.py
    parse_task.py
    torch_utils.py
requirements.txt
```

## Config files (0)


## Python signatures and reward/observation bodies (7 files)


### physhoi/env/tasks/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions)
    def get_states(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def _physics_step(self)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### physhoi/env/tasks/physhoi.py

```
class Humanoid_SMPLX(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def get_obs_size(self)
    def get_action_size(self)
    def get_num_actors_per_env(self)
    def create_sim(self)
    def reset(self, env_ids)
    def set_char_color(self, col, env_ids)
    def _reset_envs(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _create_ground_plane(self)
    def _setup_character_props(self, key_bodies)
    def _build_termination_heights(self)
    def get_num_amp_obs(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_pd_action_offset_scale(self)
    def _get_humanoid_collision_filter(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _refresh_sim_tensors(self)
    def _compute_task_obs(self, env_ids)
    def _compute_observations(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _reset_actors(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def render(self, sync_frame_time)
    def _build_key_body_ids_tensor(self, key_body_names)
    def _build_contact_body_ids_tensor(self, contact_body_names)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
class PhysHOI_BallPlay(Humanoid_SMPLX)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def post_physics_step(self)
    def _update_hist_hoi_obs(self, env_ids)
    def _setup_character_props(self, key_bodies)
    def _load_motion(self, motion_file)
    def _update_marker(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_proj(self, env_id, env_ptr)
    def _build_proj_tensors(self)
    def _load_proj_asset(self)
    def _load_marker_asset(self)
    def _load_target_asset(self)
    def _build_target(self, env_id, env_ptr)
    def _build_marker(self, env_id, env_ptr)
    def _build_target_tensors(self)
    def _build_marker_state_tensors(self)
    def _reset_target(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _reset_envs(self, env_ids)
    def _reset_actors(self, env_ids)
    def _reset_default(self, env_ids)
    def _reset_ref_state_init(self, env_ids)
    def _reset_hybrid_state_init(self, env_ids)
    def _set_env_state(self, env_ids, root_pos, root_rot, dof_pos, root_vel, root_ang_vel, dof_vel)
    def _compute_hoi_observations(self, env_ids)
    def _calc_perturb_times(self)
    def _update_proj(self)
    def play_dataset_step(self, time)
    def _draw_task_play(self, t)
    def render(self, sync_frame_time, t)
    def _draw_task(self)
def build_hoi_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, target_states, dof_diffvel)
def compute_obj_observations(root_states, tar_states)
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs, contact_forces, contact_body_ids)
def compute_humanoid_reward(hoi_ref, hoi_obs, contact_buf, tar_contact_forces, len_keypos, w)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, rigid_body_pos, max_episode_length, enable_early_termination, termination_heights, hoi_ref, hoi_obs)

```python
def build_hoi_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, 
                           local_root_obs, root_height_obs, dof_obs_size, target_states, dof_diffvel):


    contact = torch.zeros(key_body_pos.shape[0],1).cuda()
    obs = torch.cat((root_pos, root_rot, dof_pos, dof_diffvel, target_states[:,:10], key_body_pos.contiguous().view(-1,key_body_pos.shape[1]*key_body_pos.shape[2]), contact), dim=-1)
    return obs
```

```python
def compute_obj_observations(root_states, tar_states):
    # type: (Tensor, Tensor) -> Tensor
    root_pos = root_states[:, 0:3]
    root_rot = root_states[:, 3:7]

    tar_pos = tar_states[:, 0:3]
    tar_rot = tar_states[:, 3:7]
    tar_vel = tar_states[:, 7:10]
    tar_ang_vel = tar_states[:, 10:13]

    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    
    local_tar_pos = tar_pos - root_pos
    local_tar_pos[..., -1] = tar_pos[..., -1]
    local_tar_pos = quat_rotate(heading_rot, local_tar_pos)
    local_tar_vel = quat_rotate(heading_rot, tar_vel)
    local_tar_ang_vel = quat_rotate(heading_rot, tar_ang_vel)

    local_tar_rot = quat_mul(heading_rot, tar_rot)
    local_tar_rot_obs = torch_utils.quat_to_tan_norm(local_tar_rot)

    obs = torch.cat([local_tar_pos, local_tar_rot_obs, local_tar_vel, local_tar_ang_vel], dim=-1)
    return obs
```

```python
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs, contact_forces, contact_body_ids):
    # type: (Tensor, Tensor, Tensor, Tensor, bool, bool, Tensor, Tensor) -> Tensor
    root_pos = body_pos[:, 0, :]
    root_rot = body_rot[:, 0, :]

    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    
    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h
    
    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, body_pos.shape[1], 1))
    flat_heading_rot = heading_rot_expand.reshape(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], 
                                               heading_rot_expand.shape[2])
    
    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = quat_rotate(flat_heading_rot, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:] # remove root pos

    flat_body_rot = body_rot.reshape(body_rot.shape[0] * body_rot.shape[1], body_rot.shape[2])
    flat_local_body_rot = quat_mul(flat_heading_rot, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_rot_obs = flat_local_body_rot_obs.reshape(body_rot.shape[0], body_rot.shape[1] * flat_local_body_rot_obs.shape[1])
    
    if (local_root_obs):
        root_rot_obs = torch_utils.quat_to_tan_norm(root_rot)
        local_body_rot_obs[..., 0:6] = root_rot_obs

    flat_body_vel = body_vel.reshape(body_vel.shape[0] * body_vel.shape[1], body_vel.shape[2])
    flat_local_body_vel = quat_rotate(flat_heading_rot, flat_body_vel)
    local_body_vel = flat_local_body_vel.reshape(body_vel.shape[0], body_vel.shape[1] * body_vel.shape[2])
    
    flat_body_ang_vel = body_ang_vel.reshape(body_ang_vel.shape[0] * body_ang_vel.shape[1], body_ang_vel.shape[2])
    flat_local_body_ang_vel = quat_rotate(flat_heading_rot, flat_body_ang_vel)
    local_body_ang_vel = flat_local_body_ang_vel.reshape(body_ang_vel.shape[0], body_ang_vel.shape[1] * body_ang_vel.shape[2])

    body_contact_buf = contact_forces[:, contact_body_ids, :].clone().view(contact_forces.shape[0],-1)
    
    obs = torch.cat((root_h_obs, local_body_pos, local_body_rot_obs, local_body_vel, local_body_ang_vel, body_contact_buf), dim=-1)
    return obs
```

```python
def compute_humanoid_reward(hoi_ref, hoi_obs, contact_buf, tar_contact_forces, len_keypos, w):
    ## type: (Tensor, Tensor, Tensor, Tensor, Int, float) -> Tensor

    ### data preprocess ###

    # simulated states
    root_pos = hoi_obs[:,:3]
    root_rot = hoi_obs[:,3:3+4]
    dof_pos = hoi_obs[:,7:7+51*3]
    dof_pos_vel = hoi_obs[:,160:160+51*3]
    obj_pos = hoi_obs[:,313:313+3]
    obj_rot = hoi_obs[:,316:316+4]
    obj_pos_vel = hoi_obs[:,320:320+3]
    key_pos = hoi_obs[:,323:323+len_keypos*3]
    contact = hoi_obs[:,-1:]# fake one
    key_pos = torch.cat((root_pos, key_pos),dim=-1)
    body_rot = torch.cat((root_rot, dof_pos),dim=-1)
    ig = key_pos.view(-1,len_keypos+1,3).transpose(0,1) - obj_pos[:,:3]
    ig = ig.transpose(0,1).view(-1,(len_keypos+1)*3)

    # reference states
    ref_root_pos = hoi_ref[:,:3]
    ref_root_rot = hoi_ref[:,3:3+4]
    ref_dof_pos = hoi_ref[:,7:7+51*3]
    ref_dof_pos_vel = hoi_ref[:,160:160+51*3]
    ref_obj_pos = hoi_ref[:,313:313+3]
    ref_obj_rot = hoi_ref[:,316:316+4]
    ref_obj_pos_vel = hoi_ref[:,320:320+3]
    ref_key_pos = hoi_ref[:,323:323+len_keypos*3]
    ref_obj_contact = hoi_ref[:,-1:]
    ref_key_pos = torch.cat((ref_root_pos, ref_key_pos),dim=-1)
    ref_body_rot = torch.cat((ref_root_rot, ref_dof_pos),dim=-1)
    ref_ig = ref_key_pos.view(-1,len_keypos+1,3).transpose(0,1) - ref_obj_pos[:,:3]
    ref_ig = ref_ig.transpose(0,1).view(-1,(len_keypos+1)*3)


    ### body reward ###

    # body pos reward
    ep = torch.mean((ref_key_pos - key_pos)**2,dim=-1)
    rp = torch.exp(-ep*w['p'])

    # body rot reward
    er = torch.mean((ref_body_rot - body_rot)**2,dim=-1)
    rr = torch.exp(-er*w['r'])

    # body pos vel reward
    epv = torch.zeros_like(ep)
    rpv = torch.exp(-epv*w['pv'])

    # body rot vel reward
    erv = torch.mean((ref_dof_pos_vel - dof_pos_vel)**2,dim=-1)
    rrv = torch.exp(-erv*w['rv'])

    rb = rp*rr*rpv*rrv


    ### object reward ###

    # object pos reward
    eop = torch.mean((ref_obj_pos - obj_pos)**2,dim=-1)
    rop = torch.exp(-eop*w['op'])

    # object rot reward
    eor = torch.zeros_like(ep) #torch.mean((ref_obj_rot - obj_rot)**2,dim=-1)
    ror = torch.exp(-eor*w['or'])

    # object pos vel reward
    eopv = torch.mean((ref_obj_pos_vel - obj_pos_vel)**2,dim=-1)
    ropv = torch.exp(-eopv*w['opv'])

    # object rot vel reward
    eorv = torch.zeros_like(ep) #torch.mean((ref_obj_rot_vel - obj_rot_vel)**2,dim=-1)
    rorv = torch.exp(-eorv*w['orv'])

    ro = rop*ror*ropv*rorv


    ### interaction graph reward ###

    eig = torch.mean((ref_ig - ig)**2,dim=-1)
    rig = torch.exp(-eig*w['ig'])


    ### simplified contact graph reward ###

    # Since Isaac Gym does not yet provide API for detailed collision detection in GPU pipeline, 
    # we use force detection to approximate the contact status.
    # In this case we use the CG node istead of the CG edge for imitation.
    # TODO: update the code once collision detection API is available.

    ## body ids
    # Pelvis, 0 
    # L_Hip, 1 
    # L_Knee, 2
    # L_Ankle, 3
    # L_Toe, 4
    # R_Hip, 5 
    # R_Knee, 6
    # R_Ankle, 7
    # R_Toe, 8
    # Torso, 9
    # Spine, 10 
    # Chest, 11
    # Neck, 12
    # Head, 13
    # L_Thorax, 14 
    # L_Shoulder, 15
    # L_Elbow, 16
    # L_Wrist, 17
    # L_Hand, 18-32
    # R_Thorax, 33 
    # R_Shoulder, 34
    # R_Elbow, 35
    # R_Wrist, 36 
    # R_Hand, 37-51

    # body contact
    contact_body_ids = [0,1,2,5,6,9,10,11,12,13,14,15,16,33,34,35]
    body_contact_buf = contact_buf[:, contact_body_ids, :].clone()
    body_contact = torch.all(torch.abs(body_contact_buf) < 0.1, dim=-1)
    body_contact = torch.all(body_contact, dim=-1).to(float) # =1 when no contact happens to the body

    # object contact
    obj_contact = torch.any(torch.abs(tar_contact_forces[..., 0:2]) > 0.1, dim=-1).to(float) # =1 when contact happens to the object

    ref_body_contact = torch.ones_like(ref_obj_contact) # no body contact for all time
    
```

```python
def _compute_reward(self, actions):
        self.rew_buf[:] = compute_humanoid_reward(
                                                  self._curr_ref_obs,
                                                  self._curr_obs,
                                                  self._contact_forces,
                                                  self._tar_contact_forces,
                                                  len(self._key_body_ids),
                    
```

### physhoi/env/tasks/vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### physhoi/env/tasks/vec_task_wrappers.py

```
class VecTaskCPUWrapper(VecTaskCPU)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations, clip_actions)
class VecTaskGPUWrapper(VecTaskGPU)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
class VecTaskPythonWrapper(VecTaskPython)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def reset(self, env_ids)
    def amp_observation_space(self)
    def fetch_amp_obs_demo(self, num_samples)

```python
def amp_observation_space(self):
        return self._amp_obs_space
```
```

### physhoi/utils/config.py

```
def set_np_formatting()
def warn_task_name()
def set_seed(seed, torch_deterministic)
def load_cfg(args)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark)
```

### physhoi/utils/parse_task.py

```
def warn_task_name()
def parse_task(args, cfg, cfg_train, sim_params)
```