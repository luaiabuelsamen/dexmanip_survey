# dexmachina_2025

source: https://github.com/MandiZhao/dexmachina


commit: adae5bf620c57723d185b2757ee3ce9656927c20


## README

# DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation 

[Mandi Zhao](https://mandizhao.github.io), [Yifan Hou](https://yifan-hou.github.io), [Dieter Fox](https://homes.cs.washington.edu/~fox), [Yashraj Narang](https://research.nvidia.com/person/yashraj-narang), [Shuran Song*](https://shurans.github.io), [Ajay Mandlekar*](https://ai.stanford.edu/~amandlek)

*Equal Advising

[arXiv](http://arxiv.org/abs/2505.24853) | [Project Website](https://project-dexmachina.github.io) | [Code Documentation](https://mandizhao.github.io/dexmachina-docs) 

![Teaser](dexmachina-teaser-website.png)

## Code Release Status 
- 06/11/2025: 
Released all dexterous hand assets and ARCTIC assets used in our recent [arXiv preprint](http://arxiv.org/abs/2505.24853). Released detailed instructions for processing new hand assets: see code in `dexmachina/hand_proc` and [hand processing doc page](https://mandizhao.github.io/dexmachina-docs/1_process_hands.html). Pushed a new `dexmachina.yaml` file for conda env install. RL training example in `examples/train_rl.sh`
- 06/03/2025: Initial Release


TODOs 
- [ ] Advanced rendering code
- [ ] RL eval code
- [x] Instructions for processing new hands and demonstrations 

## Installation
 
1. We recommend using conda environment with Python=3.10
```
conda create -n dexmachina python=3.10
conda activate dexmachina
```
2. Clone and install the below custom forks of Genesis and rl-games:

```
pip install torch==2.5.1
git clone https://github.com/MandiZhao/Genesis.git
cd Genesis
pip install -e .
pip install libigl==2.5.1 # NOTE: this is a temporary fix specifically for my fork of Genesis

git clone https://github.com/MandiZhao/rl_games.git
cd rl_games
pip install -e .
```
Additional packages needed for RL training:
```
pip install gymnasium ray seaborn wandb trimesh open3d
# an old version of moviepy
pip install moviepy==1.0.3
```

**If you'd like to install the full conda environment that includes all the packages, use the below yaml file:**
```
# this is obtained from: conda export -f dexmachina.yaml
conda env create -f dexmachina.yaml
```
4. Local install the `dexmachina` package:
```
cd dexmachina
pip install -e .
```

See the full [documentation](https://mandizhao.github.io/dexmachina-docs) for additional installation instructions for dexterous hand and demonstration data processing, kinematic retargeting, raytracer rendering, etc. 


## Citation
This codebase is released with the following preprint:

Zhao Mandi, Yifan Hou, Dieter Fox, Yashraj Narang, Ajay Mandlekar*, Shuran Song*. DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation. arXiV, 2025.

*Equal Advising 

If you find this codebase useful, please consider citing:
```
@misc{mandi2025dexmachinafunctionalretargetingbimanual,
      title={DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation}, 
      author={Zhao Mandi and Yifan Hou and Dieter Fox and Yashraj Narang and Ajay Mandlekar and Shuran Song},
      year={2025},
      eprint={2505.24853},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2505.24853}, 
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
dexmachina/
  __init__.py
  asset_utils.py
  dexmachina.yaml
  envs/
    __init__.py
    base_env.py
    constructors.py
    contacts.py
    curriculum.py
    demo_data.py
    hand_cfgs/
    maniptrans_curr.py
    math_utils.py
    object.py
    randomizations.py
    reward_utils.py
    rewards.py
    robot.py
  eval/
    compute_add.py
    eval.md
    group_cfgs/
    group_results.py
    stats/
    utils.py
  hand_proc/
    __init__.py
    add_wrist_dof.py
    hand_utils.py
    inspect_raw_urdf.py
    minimal_retarget.py
    tune_gains.py
  retargeting/
    __init__.py
    map_contacts.py
    parallel_retarget.py
    process_arctic.py
    retarget_utils.py
  rl/
    configs/
    eval_rl_games.py
    rl_games_wrapper.py
    train_rl_games.py
  tests/
    test_new_hand_cfg.py
dexmachina-teaser-website.png
dexmachina.yaml
examples/
  inspect_hand.py
  load_object.py
  train_dex3.sh
  train_rl.sh
setup.py
```

## Config files (2)


### dexmachina/eval/group_cfgs/dexmachina_main.yaml

```yaml
object_clips:
  - ketchup30-130-s01-u01
  - box30-230-s01-u01
  - mixer30-200-s01-u01
  - ketchup40-340-s01-u02
  - mixer40-340-s01-u01
  - notebook40-340-s02-u02
  - waffleiron40-340-s01-u01

filter_conditions:
  env_kwargs.robot_cfgs.left.action_mode: [hybrid, kinematic]

methods:
  method1:
    name: "DexMachina"
    conditions:
      - key: env_kwargs.robot_cfgs.left.hybrid_scales
        value: [0.1, 1]
      - key: env_kwargs.curriculum_cfg.schedule
        value: uniform
    or_conditions:
      - key: env_kwargs.object_cfgs.box.actuated
        value: True
      - key: env_kwargs.object_cfgs.mixer.actuated
        value: True
      - key: env_kwargs.object_cfgs.ketchup.actuated
        value: True
      - key: env_kwargs.object_cfgs.waffleiron.actuated
        value: True
      - key: env_kwargs.object_cfgs.notebook.actuated
        value: True
    condition_sets:
      - name: "10k curr low6"
        keywords: [fast1-420]
        and:
          - key: env_kwargs.curriculum_cfg.lower_ratios.kp
            value: 0.6
          - key: env_kwargs.robot_cfgs.left.hybrid_scales
            value: [0.1, 1]
          - key: env_kwargs.reward_cfg.imi_rew_weight
            value: 0.2
          - key: env_kwargs.reward_cfg.contact_rew_weight
            value: 2
        or:
          - key: env_kwargs.env_cfg.episode_length
            value: 200
          - key: env_kwargs.env_cfg.episode_length
            value: 170
          - key: env_kwargs.env_cfg.episode_length
            value: 100
          - key: env_kwargs.object_cfgs.mixer.actuated
            value: True
      - name: "13k inspire imi3"
        keywords: [f424-low5-imi3]
        and:
          - key: env_kwargs.robot_cfgs.left.hybrid_scales
            value: [0.1, 1]
          - key: env_kwargs.curriculum_cfg.lower_ratios.kp
            value: 0.5
          - key: env_kwargs.reward_cfg.imi_rew_weight
            value: 0.3
          - key: env_kwargs.robot_cfgs.left.name
            value: inspire_hand_left
      - name: "f422 low5 th0 13k"
        keywords: [f422]
        and:
          - key: env_kwargs.curriculum_cfg.lower_ratios.kp
            value: 0.5
          - key: env_kwargs.reward_cfg.imi_rew_weight
            value: 0.2
          - key: env_kwargs.reward_cfg.contact_rew_weight
            value: 2
          - key: env_kwargs.robot_cfgs.left.hybrid_scales
            value: [0.1, 1]
          - key: env_kwargs.env_cfg.episode_length
            value: 300
          - key: env_kwargs.curriculum_cfg.rew_thresholds.imi
            value: 0
        or:
          - key: env_kwargs.robot_cfgs.left.name
            value: xhand_left
          - key: env_kwargs.robot_cfgs.left.name
            value: schunk_hand_left
          - key: env_kwargs.robot_cfgs.left.name
            value: allegro_hand_left

hand_types:
  inspire_hand:
    name: "Inspire Hand"
    conditions:
      - key: env_kwargs.robot_cfgs.left.name
        value: inspire_hand_left
  allegro_hand:
    name: "Allegro Hand"
    conditions:
      - key: env_kwargs.robot_cfgs.left.name
        value: allegro_hand_left
  xhand:
    name: "XHand"
    conditions:
      - key: env_kwargs.robot_cfgs.left.name
        value: xhand_left
  schunk_hand:
    name: "Schunk Hand"
    conditions:
      - key: env_kwargs.robot_cfgs.left.name
        value: schunk_hand_left

seeds:
  - 42
  - 24
  - 66
  - 15
  - 113

```

### dexmachina/rl/configs/rl_games_ppo_cfg.yaml

```yaml
params:
  seed: 42

  # environment wrapper clipping
  env:
    # added to the wrapper
    clip_observations: 5.0
    # can make custom wrapper?
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  # doesn't have this fine grained control but made it close
  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None

        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [512, 512, 256, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False # flag which sets whether to load the checkpoint
  load_path: '' # path to the checkpoint to load

  config:
    name: inspire_arctic
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: False
    normalize_input: False #True
    normalize_value: True
    value_bootstrap: True
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 0.1 # 0.01
    normalize_advantage: True
    gamma: 0.99
    tau : 0.95
    learning_rate: 3e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 100000
    max_epochs: 1000
    save_best_after: 10
    save_frequency: 1500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size:  2048 #16384 # 32768 # 16384 # 32768 # 16384 # 65536 # 32768 # 1024 for num_envs=128  # 8192 for num_envs=1024
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0001

    player:
      deterministic: True
      games_num: 100000
      print_stats: True


params:
  seed: 42

  # environment wrapper clipping
  env:
    # added to the wrapper
    clip_observations: 5.0
    # can make custom wrapper?
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  # doesn't have this fine grained control but made it close
  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None

        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [512, 512, 256, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False # flag which sets whether to load the checkpoint
  load_path: '' # path to the checkpoint to load

  config:
    name: inspire # overwrite later
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: False
    normalize_input: False #True
    normalize_value: True
    value_bootstrap: True
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 0.1 # 0.01
    normalize_advantage: True
    gamma: 0.99
    tau : 0.95
    learning_rate: 3e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 100000
    max_epochs: 1000
    save_best_after: 10
    save_frequency: 1500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size:  2048 #16384 # 32768 # 16384 # 32768 # 16384 # 65536 # 32768 # 1024 for num_envs=128  # 8192 for num_envs=1024
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0001

    player:
      deterministic: True
      games_num: 100000
      print_stats: True


params:
  seed: 42 
  # environment wrapper clipping
  env:
    # added to the wrapper
    clip_observations: 5.0
    # can make custom wrapper?
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  # doesn't have this fine grained control but made it close
  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None

        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [512, 512, 256, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False # flag which sets whether to load the checkpoint
  load_path: '' # path to the checkpoint to load

  config:
    name: inspire_arctic
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: False
    normalize_input: False #True
    normalize_value: True
    value_bootstrap: True
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 0.1 # 0.01
    normalize_advantage: True
    gamma: 0.99
    tau : 0.95
    learning_rate: 3e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 100000
    max_epochs: 1000
    save_best_after: 10
    save_frequency: 1500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size:  2048 #16384 # 32768 # 16384 # 32768 # 16384 # 65536 # 32768 # 1024 for num_envs=128  # 8192 for num_envs=1024
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0001

    player:
      deterministic: True
      games_num: 100000
      print_stats: True




```

## Python signatures and reward/observation bodies (34 files)


### dexmachina/envs/__init__.py

```
"""Environment modules for DexMachina."""
```

### dexmachina/envs/base_env.py

```
def get_scene_cfg(dt, zero_gravity, show_viewer, show_fps, batch_dofs_info, use_visualizer, n_rendered_envs, raytrace, visualize_contact, enable_joint_limit)
def get_env_cfg(dt, use_visualizer, show_viewer, show_fps, zero_gravity)
class BaseEnv()
    """Support multiple different embodiments, and either bimanual or single hand"""
    def __init__(self, env_cfg, robot_cfgs, object_cfgs, reward_cfg, demo_data, retarget_data, rand_cfg, curriculum_cfg, device, visualize_contact, contact_marker_cfgs, group_collisions, render_figure, hide_cardbox, postpone_build)
    def build_scene(self)
    def post_scene_build_setup(self)
    def setup_actions(self, robots)
    def update_contact_markers(self, contact_dict)
    def compute_obs_dim(self)
    def initialize_value_buffers(self)
    def set_retarget_states(self, step, env_idxs)
    def pre_scene_step(self, actions)
    def step(self, actions)
    def _get_rewards(self)
    def _get_dones(self)
    def prepare_sliced_contact(self, source, part, side)
    def _compute_intermediate_values(self)
    def get_observations(self)
    def get_privileged_observations(self)
    def normalize_episode_rew(self, rewards)
    def reset_idx(self, env_idxs)
    def reset(self)
    def transform_vertice_frame(self, vertices, pose)
    def compute_closest_vertice_dist_single(self, verts, keypoint_pos, pose)
    def _add_camera(self, camera_kwargs)
    def _set_camera(self, pos, lookat, fov, name)
    def start_recording(self)
    def _render_headless(self)
    def get_recorded_frames(self, wait_for_max)
    def export_video(self, path, wait_for_max)
    def randomize(self, env_idxs)
    def set_curriculum(self, epoch_num)

```python
def compute_obs_dim(self):
        
        obs_dim = 0
        obs_dim_info = dict()
        obs_idxs = dict()
        for k, robot in self.robots.items():
            dim, dim_info = robot.compute_obs_dim()
            obs_dim_info[k] = dim_info
            obs_idxs[k] = (obs_dim, obs_dim + dim)
            obs_dim += dim
        for k, obj in self.objects.items():
            dim, dim_info = obj.compute_obs_dim()
            obs_dim_info[k] = dim_info
            obs_idxs[k] = (obs_dim, obs_dim + dim)
            obs_dim += dim
        if self.observe_tip_dist:
            n_kpts = self.robots['left'].n_kpts + self.robots['right'].n_kpts
            obs_dim += n_kpts * 2 # because two obj parts!
        
        if self.observe_contact_force:
            obs_dim += self.num_obj_links * self.num_robot_links * 1 # 3 for force vec

        obs_idxs['episode_length'] = (obs_dim, obs_dim + 1) 
        ep_len_dim = 1 #* 10
        obs_dim += ep_len_dim

        # return 20, obs_idxs
        return obs_dim, obs_idxs
```

```python
def _get_rewards(self):
        if self.n_objects == 1:
            obj = self.objects[self.object_names[0]]
            obj_pos, obj_quat, obj_arti = obj.root_pos, obj.root_quat, obj.dof_pos
        else:
            obj_pos, obj_quat, obj_arti = None, None, None
        bc_dist = torch.cat([robot.get_bc_dist() for robot in self.robots.values()], dim=-1)
        reward_kwargs = dict(
            actions=self.actions,
            bc_dist=bc_dist,
            obj_pos=obj_pos,
            obj_quat=obj_quat,
            obj_arti=obj_arti,
            kpts_left=self.robots['left'].kpt_pos,
            kpts_right=self.robots['right'].kpt_pos,
            episode_length_buf=self.episode_length_buf,
            contact_link_pos_left=None,
            contact_link_valid_left=None,
            contact_link_pos_right=None,
            contact_link_valid_right=None,
            wrist_pose_left=self.robots['left'].wrist_pose,
            wrist_pose_right=self.robots['right'].wrist_pose,
            contact_forces=None,
            )
        if self.use_contact_reward:
            reward_kwargs.update(
                contact_link_pos_left=self.contact_link_pos[:, :, :self.num_left_contact_links], # N, 2, 13, 3
                contact_link_valid_left=self.contact_link_valid[:, :, :self.num_left_contact_links],
                contact_link_pos_right=self.contact_link_pos[:, :, self.num_left_contact_links:],
                contact_link_valid_right=self.contact_link_valid[:, :, self.num_left_contact_links:],
            )
        if self.observe_contact_force:
            reward_kwargs.update(
                contact_forces=self.contact_forces
            )
        rewards, rew_dict = self.reward_module.compute_reward(
            **reward_kwargs
        )
        
        if not self.use_rl_games:
            # scale the reward by 0.1 manually to match the scale in rl_games
            rewards *= 0.1

        self.rew_dict = rew_dict 
        self.rew_buf[:] = rewards
        # there's potentially nan values 
        self.rew_buf[self.nan_envs] = -1.0
        task_rewards = rew_dict['task_rew'] # use task_rew for reset
        task_rewards[self.nan_envs] = -1.0
        rew_dict['task_rew'] = task_rewards
        self.cumulative_task_rew[:] += task_rewards if self.n_objects == 1 else rewards 
        
        if 'con_rew' in rew_dict:
            con_rew = rew_dict['con_rew']
            con_rew[self.nan_envs] = -1.0
            self.cumulative_con_rew[:] += con_rew
        if 'imi_rew' in rew_dict:
            imi_rew = rew_dict['imi_rew']
            imi_rew[self.nan_envs] = -1.0
            self.cumulative_imi_rew[:] += imi_rew
        if 'bc_rew' in rew_dict:
            bc_rew = rew_dict['bc_rew']
            bc_rew[self.nan_envs] = -1.0
            self.cumulative_bc_rew[:] += bc_rew
        return rew_dict
```

```python
def get_observations(self):
        value_list = []
        all_obs_dict = dict()
        for name, robot in self.robots.items():
            obs_dict = robot.get_observations()
            value_list.extend(list(obs_dict.values()))
            all_obs_dict[name] = obs_dict
        for name, obj in self.objects.items():
            obs_dict = obj.get_observations()
            value_list.extend(list(obs_dict.values()))
            all_obs_dict[name] = obs_dict
        left = self.robots['left']
        right = self.robots['right'] 
        # contact_info = left.entity.get_contacts(obj.entity)
        # force, mask = contact_info['force_a'], contact_info['valid_mask']
        # print(force[mask].shape)
        if self.chunk_ep_length > 0:
            normalize_ep_len = 2.0 * self.episode_length_buf[:, None].float() / self.demo_length - 1.0
        else:
            normalize_ep_len = 2.0 * self.episode_length_buf[:, None].float() / self.max_episode_length - 1.0
        value_list.append(normalize_ep_len)

        # value_list = []
        # value_list.append(normalize_ep_len.repeat(1, 20))

        if self.observe_tip_dist:
            assert self.n_objects == 1, "Only support one object for now"
            obj = self.objects[self.object_names[0]]
            # compute the kpt distances to the object surface
            for side, dists_tensor in zip(['left', 'right'], [self.kpt_dists_left, self.kpt_dists_right]):
                robot = self.robots[side]
                for i, part in enumerate(['top', 'bottom']):
                    part_pose = obj.get_part_pose(part)
                    dists_tensor[:, :, i] = self.compute_closest_vertice_dist_single(
                        self.obj_verts[part], robot.kpt_pos, part_pose
                    )
                    name = f"{side}_kpt_dist_{part}"
                    # print(name, np.round(dists_tensor[:, :, i].cpu().numpy(), 2))
            value_list.extend([
                self.kpt_dists_left.flatten(start_dim=1),
                self.kpt_dists_right.flatten(start_dim=1),
                ])

        if self.observe_contact_force:
            force_norm = torch.norm(self.contact_forces, dim=-1) * 0.01 # scale down! max contact force can go to 1000+
            value_list.append(force_norm.flatten(start_dim=1))

        obs = torch.cat(value_list, dim=-1)
        self.obs_dict = all_obs_dict
        # if sum(torch.isnan(obs).flatten()) > 0:
        #     print("NAN OBSERVATIONS")
        #     breakpoint()
        nan_mask = torch.isnan(obs) 
        obs[nan_mask] = -self.obs_clip
        # if there's nan, need immediately reset 
        all_obs_dict['nan_mask'] = nan_mask
        obs = torch.clamp(obs, -self.obs_clip, self.obs_clip)

        if self.use_rl_games:
            return dict(policy=obs, itemized=all_obs_dict, critic=obs) # critic for sil
        return obs
```

```python
def get_privileged_observations(self): 
        return None
```
```

### dexmachina/envs/constructors.py

```
def parse_clip_string(clip)
def get_all_env_cfg(args, device, load_retarget_data)
def get_common_argparser()
```

### dexmachina/envs/contacts.py

```
def get_contact_marker_cfgs(num_vis_contacts, radius, sources, obj_parts, hand_sides)
def get_expanded_mask(n_contacts, pair_a, pair_b, a_idxs, b_idxs)
def get_filtered_contact_force_from_mask(force, mask)
def get_all_contact_pos_from_mask(contact_pos, mask)
def get_grouped_contact_pos(contact_pos, contact_force_norm, mask)
def get_filtered_contacts(entity_a, entity_b, filter_geoms_a, filter_geoms_b, filter_links_a, filter_links_b, return_geom_force, return_link_force, return_geom_pos, return_link_pos, device)
def index_contact_force(n_contacts, force, geom_a, geom_b, geom_a_idxs, geom_b_idxs)
def get_per_link_a_contact_pos(n_contacts, contact_pos, contact_force_norm, link_a, link_b, link_a_idxs, link_b_idxs)
def get_per_geom_a_contact_pos(n_contacts, contact_pos, contact_force_norm, geom_a, geom_b, geom_a_idxs, geom_b_idxs)
```

### dexmachina/envs/curriculum.py

```
def get_curriculum_cfg(kwargs)
class Curriculum()
    def __init__(self, curr_cfg, task_object, reward_keys, num_envs, achieved_length, max_episode_length)
    def post_scene_build_setup(self)
    def set_fixed_decay(self, epoch_num)
    def determine_decay(self, epoch_num)
    def determine_dialback(self, epoch_num)
    def set_auto_exp_decay(self, epoch_num)
    def set_auto_uniform_decay(self, epoch_num)
    def update_progress(self, rewards, achieved_length)
    def get_current_gains(self)
    def reset_object_gains(self)
    def reset_solimp(self)
    def get_reward_grads(self)
    def update_reward_grads(self)
    def decay_reward_weights(self, reward_module)
    def set_curriculum(self, epoch_num)

```python
def get_reward_grads(self):
        return self.rew_grads
```

```python
def update_reward_grads(self):
        for key in self.rew_deques.keys():
            if len(self.rew_deques[key]) < self.deque_len:
                continue 
            grad = np.gradient(self.rew_deques[key]).mean()
            self.rew_grads[key] = grad
```

```python
def decay_reward_weights(self, reward_module):
        decayed = False
        if not self.decay_rew:
            return decayed
        info = ""
        for attr in ['imi_rew_weight', 'bc_rew_weight', 'contact_rew_weight']:
            if hasattr(reward_module, attr):
                val = getattr(reward_module, attr)
                if val > 0.01:
                    setattr(reward_module, attr, val * 0.95)
                    info += f"{attr}: to {val * 0.95} "
                    decayed = True
        # also decay the rew thresholds
        for key in self.rew_thresholds.keys():
            self.rew_thresholds[key] = self.rew_thresholds[key] * 0.95
        if len(info) > 0:
            print(info)
        return decayed
```
```

### dexmachina/envs/demo_data.py

```
def get_demo_data(obj_name, frame_start, frame_end, hand_name, subject_name, use_clip, load_retarget_contact)
def get_joint_init_limits(joint_pos_dict)
def load_genesis_retarget_data(obj_name, hand_name, frame_start, frame_end, save_name, use_clip, subject_name, given_data_fname)
def load_contact_retarget_data(obj_name, hand_name, frame_start, frame_end, save_name, use_clip, subject_name)
```

### dexmachina/envs/maniptrans_curr.py

```
def get_maniptrans_cfg(kwargs)
class ManipTransCurriculum()
    """all curriculums should have: 
- post_scene_build_setup()
- get_reward_grads()
- get_current_gains()
- update_progress()
- set_curriculum()
- decay_reward_weights()
New to maniptrans: use the eps_ values to determine environment early termination """
    def __init__(self, curr_cfg, task_object, reward_keys, num_envs, achieved_length, max_episode_length, sim, rigid_solver)
    def post_scene_build_setup(self)
    def get_reward_grads(self)
    def decay_reward_weights(self)
    def get_current_gains(self)
    def update_progress(self, rewards, achieved_length)
    def set_curriculum(self, epoch_num)
    def determine_early_term(self, obj_pos_err, obj_rot_err, finger_pos_err)
    def set_fixed_decay(self, epoch_num)
    def set_auto_decay(self, epoch_num)
    def get_fixed_decay_param(self, epoch_num, range, zero_epoch, schedule, fixed_interval)
    def determine_decay(self, epoch_num)

```python
def get_reward_grads(self):
        return dict()
```

```python
def decay_reward_weights(self):
        return False
```
```

### dexmachina/envs/math_utils.py

```
def quat_conjugate(q)
def quat_mul(q1, q2)
def matrix_from_quat(quaternions)
```

### dexmachina/envs/object.py

```
def get_arctic_object_cfg(name, convexify, decomp, texture_mesh)
class ArticulatedObject()
    """Assume only one joint """
    def __init__(self, obj_cfg, device, scene, num_envs, obs_scale, demo_data, visualize_contact, disable_collision)
    def post_scene_build_setup(self)
    def set_demo_states(self, demo_data)
    def set_to_demo_step(self, step)
    def fill_gain_tensor(self, val, num_dofs, num_envs, device)
    def interpolate_demo_states(self, multiplier)
    def set_joint_gains(self, kp, kv, force_range, env_idxs)
    def sample_mesh_vertices(self, num_samples, part, seed)
    def initialize_value_buffers(self)
    def update_value_buffers(self)
    def get_nan_envs(self)
    def get_observations(self)
    def get_part_pose(self, part)
    def compute_obs_dim(self)
    def reset_idx(self, env_idxs, episode_start, reset_gains)
    def reset(self)
    def set_object_state(self, root_pos, root_quat, joint_qpos, env_idxs)
    def step(self, env_idxs)
    def flush_episode_data(self)
    def collect_data_step(self)
    def transform_part_vertices(self, mesh_verts, part)
    def get_part_vertices(self, part, num_verts)
    def get_object_vertices(self, num_verts)

```python
def get_observations(self):
        assert self.initialized, "Object not initialized" 
        obs_dict = { 
            "parts_pos": self.part_pos.flatten(start_dim=1),
            "parts_quat": self.part_quat.flatten(start_dim=1),
            "dof_pos": self.dof_pos, 
            "state_diff": self.state_diff,
            "root_ang_vel": self.root_ang_vel,
            "root_lin_vel": self.root_lin_vel, 
        }
        for k, scale in self.obs_scale.items():
            if k in obs_dict:
                obs_dict[k] *= scale 
        return obs_dict
```

```python
def compute_obs_dim(self):
        dims = dict( 
            parts_pose_dim=7*self.n_links,
            root_ang_vel_dim=3,
            root_lin_vel_dim=3,
            dof_pos_dim=self.num_joints, 
            state_diff_dim=8,
        )
        return sum(dims.values()), dims
```
```

### dexmachina/envs/randomizations.py

```
def get_randomization_cfg(randomize, on_friction, on_com, on_mass, external_force, force_prob, force_scale, torque_scale)
class RandomizationModule()
    """Handles randomization of the environment physics """
    def __init__(self, rand_cfg, solver, task_object, num_envs)
    def on_step(self, episode_length_buf)
    def on_reset_idx(self, env_idxs)
    def _randomize_link_friction(self, friction_range, env_idxs)
    def _randomize_com_displacement(self, com_range, env_idxs)
    def _randomize_mass(self, mass_range, env_idxs)
    def _random_force_torque(self, episode_length_buf)
```

### dexmachina/envs/reward_utils.py

```
def rotation_distance(object_rot, target_rot)
def position_distance(object_pos, target_pos)
def chamfer_distance(pts1, pts2, pts1_valid, pts2_valid)
def transform_contact(contact_positions, new_frame)
```

### dexmachina/envs/rewards.py

```
def get_reward_cfg(last_n_frame)
class RewardModule()
    def __init__(self, reward_cfg, demo_data, retarget_data, device)
    def load_demo(self, demo_data, retarget_data, device)
    def get_demo_length(self)
    def match_demo_state(self, demo_key, episode_length_buf)
    def compute_task_reward(self, obj_pos, obj_quat, obj_arti, demo_pos, demo_quat, episode_length_buf)
    def compute_keypoint_dist(self, keypoint_pos, episode_length_buf, left_hand)
    def compute_wrist_reward(self, wrist_pose, episode_length_buf, side)
    def compute_imitation_reward(self, wrist_pose_left, wrist_pose_right, kpts_left, kpts_right, episode_length_buf)
    def contact_dist_to_rew(self, dist, function)
    def compute_hand_contact_reward(self, contact_link_pos, contact_link_valid, wrist_pose, obj_pose, episode_length_buf, demo_obj_pose, side)
    def compute_matched_contact_per_hand(self, contact_link_pos, contact_link_valid, episode_length_buf, obj_pose, demo_obj_pose, side, max_distance)
    def compute_matched_contact_reward(self, contacts_link_left, contacts_link_valid_left, contacts_link_right, contacts_link_valid_right, obj_pose, demo_obj_pose, episode_length_buf)
    def compute_contact_reward(self, obj_pose, wrist_pose_left, wrist_pose_right, contacts_link_left, contacts_link_valid_left, contacts_link_right, contacts_link_valid_right, episode_length_buf)
    def reshape_contact_with_label(self, contact_link_pos, contact_link_valid)
    def compute_reward(self, actions, bc_dist, obj_pos, obj_quat, obj_arti, kpts_left, kpts_right, contact_link_pos_left, contact_link_valid_left, contact_link_pos_right, contact_link_valid_right, wrist_pose_left, wrist_pose_right, contact_forces, episode_length_buf)
    def get_reward_keys(self)

```python
def get_reward_cfg(last_n_frame=-1):
    reward_cfg = {
        "obj_pos_beta": 20.0,
        "obj_rot_beta": 5.0,
        "obj_arti_beta": 20.0,
        "obj_pos_weight": 2.0,
        "obj_rot_weight": 3.0,
        "obj_arti_weight": 5.0,  
        
        "last_n_frame": last_n_frame,
        "multiply_task_rew": True,
        "multiply_all_rew": False, 
        "task_rew_weight": 1.0,

        "exp_kpt_first": True,
        "imi_rew_weight":  0.0, 
        "imi_wrist_weight": 0.0, # do a weighted avg between fingertip and wrist poses
        "imi_wrist_rot_beta": 3.0,
        "imi_wrist_pos_beta": 10.0,
        "imi_fingertip_beta": 20.0,

        "bc_rew_weight": 0.0,
        "bc_beta": 500.0,

        "contact_rew_weight": 0.0,
        "contact_rew_function": "exp", # exp or sigmoid
        "wrist_frame_contact": True,
        "contact_beta": 30.0,
        "contact_a": 100.0,
        "contact_b": 5.0,
        "multiply_frame_contact": True,
        "mask_zero_contact": True, # if both policy and demo has no contact, reward is 0 (1 if False)
        "contact_phase_penalty": 0,

        "mask_well_track": False, 
        "scale_well_track": 1.0,
        "force_penalty": 0.1,  # ~60 contact pairs in each env
        "action_penalty": 0.0,
        "objdex_baseline": False,
        "use_retarget_contact": False,
        "retarget_objframe": True, # if True, the contact is in the object frame, otherwise in the wrist frame

    } 
    return reward_cfg
```

```python
def compute_task_reward(self, obj_pos, obj_quat, obj_arti, demo_pos, demo_quat, episode_length_buf):
        if obj_pos is None or obj_quat is None or obj_arti is None or self.task_rew_weight == 0.0:
            # dummy reward
            task_rew = torch.zeros(episode_length_buf.shape, device=episode_length_buf.device)
            return task_rew, dict(task_rew=task_rew)
        
        demo_arti = self.match_demo_state("obj_arti", episode_length_buf)
        pos_dist = position_distance(obj_pos, demo_pos)
        rot_dist = rotation_distance(obj_quat, demo_quat)
        # arti_dist = torch.mean((obj_arti - demo_arti)**2, dim=-1)

        if len(obj_arti.shape) > 1:
            obj_arti = obj_arti.flatten(start_dim=0)
            
        arti_dist = (obj_arti - demo_arti)**2 / 2.0
        
        # these should all be shape (num_envs, )!!
        obj_pos_rew = torch.exp(-self.obj_pos_beta * pos_dist)  
        obj_rot_rew = torch.exp(-self.obj_rot_beta * rot_dist)
        obj_arti_rew = torch.exp(-self.obj_arti_beta * arti_dist)
        assert obj_pos_rew.shape == obj_rot_rew.shape == obj_arti_rew.shape, "Shape mismatch"
        # if joint is closed, don't compute arti reward 
        if self.multiply_task_rew:
            task_rew = self.task_rew_weight * obj_pos_rew * obj_rot_rew * obj_arti_rew # scale is stil [0,1]
            # print(f"========= weighted task rew: {task_rew} | rew weight: {self.task_rew_weight * 10 } obj pos rew: {obj_pos_rew} | obj rot rew: {obj_rot_rew} | obj arti rew: {obj_arti_rew} =========")
        else:
            # obj_arti_rew = torch.where(demo_arti <= 0.0001, torch.zeros_like(obj_arti_rew), obj_arti_rew)
            task_rew = self.task_rew_weight * (
                self.obj_pos_weight * obj_pos_rew + 
                self.obj_rot_weight * obj_rot_rew + 
                self.obj_arti_weight * obj_arti_rew
                )
            
        # give a bonus if obj state is well tracked and articulation joint is open 
        well_track = (pos_dist < 0.005) & (rot_dist < 0.1) & (arti_dist < 0.1)  & (demo_arti > 0.1)
        if self.scale_well_track > 1.0:
            task_rew = torch.where(well_track, task_rew * self.scale_well_track, task_rew)

        rew_dict = dict(
            pos_dist=pos_dist,
            rot_dist=rot_dist,
            arti_dist=arti_dist,
            obj_pos_rew=obj_pos_rew,
            obj_rot_rew=obj_rot_rew,
            obj_arti_rew=obj_arti_rew,
            task_rew=task_rew.clone(), # NOTE: otherwise it's the same tensor as the total reward
            well_track=well_track,
        )  

        if self.last_n_frame > 0:
            # mask out rewards that are not from the last n frames
            tomask = torch.where(
                episode_length_buf < self.demo_length - self.last_n_frame, 
                torch.zeros(task_rew.shape, device=task_rew.device, dtype=torch.bool),
                torch.ones(task_rew.shape, device=task_rew.device, dtype=torch.bool)
                )
            task_rew[tomask] = 0.0
        return task_rew, rew_dict
```

```python
def compute_wrist_reward(self, wrist_pose, episode_length_buf, side='left'):
        demo_wrist = self.match_demo_state(f"wrist_pose_{side}", episode_length_buf)
        wrist_rot_dist = rotation_distance(wrist_pose[:, 3:], demo_wrist[:, 3:])
        wrist_pos_dist = position_distance(wrist_pose[:, :3], demo_wrist[:, :3])
        rot_beta = self.cfg["imi_wrist_rot_beta"]
        pos_beta = self.cfg["imi_wrist_pos_beta"]
        wrist_rew = (torch.exp(-rot_beta * wrist_rot_dist) + torch.exp(-pos_beta * wrist_pos_dist)) / 2.0 
        return wrist_rew, wrist_pos_dist, wrist_rot_dist
```

```python
def compute_imitation_reward(
        self,
        wrist_pose_left,
        wrist_pose_right,
        kpts_left: torch.Tensor,
        kpts_right: torch.Tensor,
        episode_length_buf: torch.Tensor,
    ): 
        fingertip_dist_left = self.compute_keypoint_dist(kpts_left, episode_length_buf, left_hand=True)
        fingertip_dist_right = self.compute_keypoint_dist(kpts_right, episode_length_buf, left_hand=False)
        fingertip_dist = torch.mean( (fingertip_dist_left + fingertip_dist_right) / 2.0 , dim=-1) # (B, num_links) -> (B,)
        beta = self.cfg["imi_fingertip_beta"]
        if self.exp_kpt_first:
            fingertip_rew_left = torch.exp(- beta * fingertip_dist_left)
            fingertip_rew_right = torch.exp(- beta * fingertip_dist_right)
            fingertip_rew = torch.mean( (fingertip_rew_left + fingertip_rew_right) / 2.0 , dim=-1) # (B, num_links) -> (B,) 
        else:  
            fingertip_rew = torch.exp(-self.cfg["imi_fingertip_beta"] * fingertip_dist) 
        # 
        if self.imi_wrist_weight > 0.0:
            # do a rotation + position distance for wrist pose
            wrist_rew_left, pos_dist_left, rot_dist_left = self.compute_wrist_reward(wrist_pose_left, episode_length_buf, side='left')
            wrist_rew_right, pos_dist_right, rot_dist_right = self.compute_wrist_reward(wrist_pose_right, episode_length_buf, side='right')
            wrist_rew = (wrist_rew_left + wrist_rew_right) / 2.0
            imi_rew = self.imi_wrist_weight * wrist_rew + (1.0 - self.imi_wrist_weight) * fingertip_rew

            wrist_dist = torch.mean( (pos_dist_left + pos_dist_right) / 2.0 , dim=-1) # (B, num_links) -> (B,)
            keypoint_dist = self.imi_wrist_weight * wrist_dist + (1.0 - self.imi_wrist_weight) * fingertip_dist
        else:
            imi_rew = fingertip_rew
            keypoint_dist = fingertip_dist
            
        imi_rew *= self.imi_rew_weight

        rew_dict = dict(
            kpts_dist_left=fingertip_dist_left,
            kpts_dist_right=fingertip_dist_right,  
            imi_rew=imi_rew, 
            keypoint_dist=keypoint_dist,
        )
        if self.imi_wrist_weight > 0.0:
            rew_dict["wrist_pdist_left"] = pos_dist_left
            rew_dict["wrist_pdist_right"] = pos_dist_right
            rew_dict["wrist_rdist_left"] = rot_dist_left
            rew_dict["wrist_rdist_right"] = rot_dist_right
            rew_dict["wrist_rew_left"] = wrist_rew_left  
            rew_dict["wrist_rew_right"] = wrist_rew_right 
            rew_dict["fingertip_rew"] = fingertip_rew
            if not self.exp_kpt_first:
                rew_dict["fingertip_dist"] = fingertip_dist
                

        if self.last_n_frame > 0:
            # mask out rewards that are not from the last n frames
            tomask = torch.where(
                episode_length_buf < self.demo_length - self.last_n_frame, 
                torch.zeros(imi_rew.shape, device=task_rew.device, dtype=torch.bool),
                torch.ones(imi_rew.shape, device=task_rew.device, dtype=torch.bool)
                )
            imi_rew[tomask] = 0.0
        return imi_rew, rew_dict
```

```python
def compute_hand_contact_reward(
        self,
        contact_link_pos, # shape (N, num_obj_links * num_hand_links, 4)
        contact_link_valid, # shape (N, num_obj_links * num_hand_links, 1)
        wrist_pose, # shape (N, 7)
        obj_pose, # shape (N, 7)
        episode_length_buf,
        demo_obj_pose, # shape (N, 7)
        side='left',
    ):
        demo_wrist_pose = self.match_demo_state(f"wrist_pose_{side}", episode_length_buf)
        demo_contacts = self.match_demo_state(f"contact_links_{side}", episode_length_buf) 
        # N, num_links * 2, 4 (last dim is contact pair ID) -> NOTE in ARCTIC, part_id=2 is 'bottom' link, part_id=1 is 'top' 
        demo_positions = demo_contacts[:, :, :3]
        demo_valid_contact = demo_contacts[:, :, -1] > 0.0 # (part id is <= 0 if no contact)
        chamfer_dists = dict()
        contact_rewards = dict()

        positions = contact_link_pos[:, :, :3]
        valid_mask = contact_link_pos[:, :, -1] > 0.0 
        for part_id in [1, 2]:
            # consider contact invalid if part_id is different
            demo_part_valid = (demo_contacts[:, :, -1] == part_id) & demo_valid_contact
            part_valid = (contact_link_pos[:, :, -1] == part_id ) & valid_mask
                 
            for frame in ['obj', 'wrist']:
                if not self.wrist_frame_contact and frame == 'wrist':
                    continue
                demo_pose = demo_obj_pose if frame == 'obj' else demo_wrist_pose
                demo_in_frame = transform_contact(
                    demo_positions, demo_pose
                )
                pose = obj_pose if frame == 'obj' else wrist_pose
                in_frame = transform_contact(
                    positions, pose
                )
                dist = chamfer_distance(
                    in_frame, demo_in_frame, part_valid, demo_part_valid
             
```

### dexmachina/envs/robot.py

```
def unscale(x, lower, upper)
def get_hand_specific_cfg(name)
def get_default_robot_cfg(name, side, wrist_only, group_collisions)
class BaseRobot()
    def __init__(self, robot_cfg, device, scene, num_envs, obs_scale, retarget_data, visualize_contact, is_eval, disable_collision)
    def get_collision_groups(self)
    def set_kpt_links(self, kpt_link_names)
    def set_custom_init_qpos(self, joint_qpos)
    def set_residual_qpos(self, num_frames, residual_qpos_dict, qpos_targets_dict)
    def smooth_residual_qpos(self, joint_idxs)
    def interpolate_residual_qpos(self, mutiplier)
    def set_relative_step_size(self, residual_qpos)
    def set_custom_joint_limits(self, joint_limits_dict)
    def setup_action_mapping(self, actuated_joints, mimic_joint_map)
    def get_action_dim(self)
    def set_joint_gains(self, kp, kv, fr, joint_idxs)
    def set_inspire_gains(self)
    def post_scene_build_setup(self)
    def find_joints_in_group(self, joint_exprs)
    def set_dof_gains_by_group(self, actuator_cfgs)
    def initialize_value_buffers(self)
    def update_value_buffers(self)
    def get_nan_envs(self)
    def get_observations(self)
    def compute_obs_dim(self)
    def translate_actions(self, actions, episode_length_buf)
    def map_joint_targets_to_actions(self, joint_targets)
    def reset_idx(self, env_idxs, episode_start)
    def check_env_idxs(self, env_idxs)
    def set_joint_position(self, joint_targets, joint_idxs, env_idxs)
    def get_wrist_xyz_joints(self)
    def get_control_force(self)
    def control_joint_position(self, joint_targets, joint_idxs, env_idxs)
    def step(self, actions, env_idxs)
    def get_bc_dist(self)
    def flush_episode_data(self)
    def get_control_errors(self)
    def collect_data_step(self, collect_all_envs)

```python
def get_observations(self):
        assert self.initialized, "Robot not initialized"  
        target_pos_diff = self.curr_targets - self.dof_pos
        obs_dict = { 
            "dof_target_pos": target_pos_diff,
            "dof_pos": unscale(
                self.dof_pos,
                self.dof_limits[:, 0],
                self.dof_limits[:, 1],
            ),
            "dof_vel": self.dof_vel,
            "kpt_pos": self.kpt_pos.view(self.num_envs, -1),
            "wrist_pose": self.wrist_pose, 
        }

        for k, scale in self.obs_scale.items():
            if k in obs_dict:
                obs_dict[k] *= scale 
        return obs_dict
```

```python
def compute_obs_dim(self): 
        dims = dict( 
            qpos_dim = self.ndof,   
            qpos_target_dim = self.ndof,
            qvel_dim = self.ndof,
            kpt_dim = int(len(self.kpt_link_names) * 3),  
            wrist_dim = 7, 
        )
        return sum(dims.values()), dims
```
```

### dexmachina/hand_proc/add_wrist_dof.py

```
"""Reference implementation: 
https://github.com/google-research/robopianist/blob/d9cde23e46cb30ebb8eeebb375a9c52191238a30/robopianist/models/hands/shadow_hand.py#L41C1-L41C14


==== to print out all the joint names: ====
from lxml import etree
lxml_parser = etree.XMLParser(remove_comments=True, remove_blank_text=True)
tree = etree.parse("xxx.urdf", parser=lxml_parser)
print([j.attrib['name'] for j in tree.findall("joint") if j.attrib['type'] != 'fixed'])"""
class Dof()
    """Forearm degree of freedom."""
def add_new_elem_for_dof(dof, root_elem, prev_joint_elem, new_link_name, base_link_name, left_hand)
def add_forearm_dof(input_fname, output_fname, dof_choices, base_link_name, left_hand, skip_side_prefix)
```

### dexmachina/hand_proc/hand_utils.py

```
def common_hand_proc_args()
def parse_clip_string(clip)
def generate_90degree_rotation_quaternions(max_combined_rotations)
def get_rotation_description(rotation_name)
```

### dexmachina/hand_proc/inspect_raw_urdf.py

```
"""Load and inspect the raw URDF files into a minimal Genesis scene

- Iterate all the rotations to find proper camera 
URDF=filename
python hand_proc/inspect_raw_urdf.py --record_video --render_image --urdf_path $URDF --skip_wrist_interp  --group_collisions --interp_step 30 --iterate_quat"""
def render_image(camera, transparent)
def get_base_rotation(name)
def interpolate_hand_joints(hand, n_steps, skip_wrist)
def interpolate_wrist_finger_separately(hand, n_steps, skip_wrist, wrist_only, wrist_rot_only)
def export_video(frames, path, fps)
def gather_geom_link_groups(hand)
def find_all_parents(link, all_links)
def divide_hand_groups(hand, palm_link_name)
def main(args)
```

### dexmachina/hand_proc/minimal_retarget.py

```
def get_entity_info(entity)
def create_scene(args, hand_urdfs, obj_name)
def set_object_state(obj, params, step)
def main(args)
```

### dexmachina/hand_proc/tune_gains.py

```
def create_scene(args, hand_urdfs, obj_name)
def control_set_hand_to_step(hand_entities, dof_idxs, tuned_dof_idxs, init_step, retar_data, step, device, env_idxs, control_joints)
def find_joints_in_group(entity, exprs)
def interpolate_gain_val(vals, num_iters, num_joints, multiplier)
def set_joint_gains(args, hand_entities, dof_idxs, kp, kv, fr, env_idxs)
def set_gains_from_cfg(entity, actuator_cfgs)
def main(args)
```

### dexmachina/retargeting/map_contacts.py

```
def show_contact_plt(contact_links)
def render_transparent_img(cam)
def create_scene(args, object_name, urdfs, num_raw_contact_markers, num_grouped_contact_markers)
def show_hand_joints_links_plt(hand_entites)
def show_hand_kpts_scene(scene, hand_entites, markers)
def group_contacts(links, raw_contacts, valids, num_obj_parts)
def set_entities_to_step(hand_entities, retargeter_results, step)
def set_object_to_step(obj, obj_states, step)
def visualize_markers(markers_dict, raw_contacts, grouped_contacts)
```

### dexmachina/retargeting/parallel_retarget.py

```
def create_scene(num_envs, robot_cfgs, object_cfgs, demo_data, vis, record_video, render_image, dt, visualize_contact, device, n_rendered_envs, group_collisions, enable_self_collision)
def prepare_cfgs(args, hand_name, obj_name, start, end, subject_name, use_clip)
def prepare_retarget_cfgs(args, hand_name, obj_name, robot_cfgs, subject_name, use_clip)
def set_init_object_states(obj, obj_pos, obj_quat, obj_arti, joint_only)
def get_obj_demo_tensors(demo_data, device)
def set_hand_to_step(hands, retar_data, step, env_idxs)
def prepare_robot_actions(hand, side_retar_data)
def gather_parallel_save_data(hands, retar_data)
def resample_hand_qpos(hand, hand_qpos, c_steps, min_controlled_steps, resample_range, error_threshold)
def get_save_fname(args, hand_name, input_fname, retarget_type, subject_name)
def get_retargeter_save_fname(args, hand_name, input_fname, retarget_type, subject_name)
def main(args)
```

### dexmachina/retargeting/process_arctic.py

```
def axis_angle_to_quaternion(axis_angle)
def approximate_contact(verts1, verts2, dist_min, dist_max, threshold)
def approximate_contact_with_id(obj_verts, obj_part_ids, hand_verts, threshold, dist_min, dist_max)
def farthest_sample_contact(contact_pts, num_sample)
def find_closest_link(contact_points, joint_points)
```

### dexmachina/retargeting/retarget_utils.py

```
def get_link_names(urdf_path)
def compose_retarget_config(input, retarget_type, low_pass_alpha, scaling_factor, add_dummy_free_joint, ignore_mimic_joint)
def get_ref_val(joint_pos, indices)
def get_demo_obj_tensors(loaded_data, step, device)
def retarget_one_hand(wrist_pos, retarget_type, ref_value, retargeter, hand_init_qpos, actuated_dof_names, actuated_dof_idxs)
def control_hand(hand, hand_qpos, wrist_qpos, wrist_idxs, set_finger, set_wrist)
def retarget_all_steps(dof_limits, hand_init_qpos, actuated_dof_names, actuated_dof_idxs, retargeter, num_steps, joint_pos_demo, retarget_type, frame_start)
```

### dexmachina/rl/train_rl_games.py

```
def dump_yaml(filename, data, sort_keys)
def main()
```

### dexmachina/tests/test_new_hand_cfg.py

```
def main(args)
```

### examples/inspect_hand.py

```
def main(args)
```