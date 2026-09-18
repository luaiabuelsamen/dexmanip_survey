# dexplore_2025

source: https://github.com/NVlabs/dexplore


commit: d0b9320aa0495bf3df78d0cd44c2fad718f8a622


## README

<p align="center">
<h1 align="center"><strong>[CoRL 2025] Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration</strong></h1>
  <p align="center">
    <a href='https://sirui-xu.github.io/' target='_blank'>Sirui Xu</a><sup>1,2</sup>&emsp;
    <a href='https://research.nvidia.com/person/yu-wei-chao' target='_blank'>Yu-Wei Chao</a><sup>2</sup>&emsp;
    <a href='https://scholar.google.com/citations?user=J2z-0lgAAAAJ' target='_blank'>Liuyu Bian</a><sup>2</sup>&emsp;
    <a href='https://scholar.google.com/citations?user=fcA9m88AAAAJ' target='_blank'>Arsalan Mousavian</a><sup>2</sup>&emsp;
    <a href='https://yxw.web.illinois.edu/' target='_blank'>Yu-Xiong Wang</a><sup>1</sup>&emsp;
    <a href='https://lgui.web.illinois.edu/' target='_blank'>Liang-Yan Gui</a><sup>1</sup>&emsp;
    <a href='https://wyang.me/' target='_blank'>Wei Yang</a><sup>2</sup>&emsp;
    <br>
    <sup>1</sup>University of Illinois Urbana-Champaign&emsp;
    <sup>2</sup>NVIDIA
  </p>
</p>

<p align="center">
  <a href='https://arxiv.org/abs/2509.09671'>
    <img src='https://img.shields.io/badge/Arxiv-2509.09671-A42C25?style=flat&logo=arXiv&logoColor=A42C25'></a>
  <a href='https://arxiv.org/pdf/2509.09671.pdf'>
    <img src='https://img.shields.io/badge/Paper-PDF-yellow?style=flat&logo=arXiv&logoColor=yellow'></a>
  <a href='https://sirui-xu.github.io/dexplore/'>
    <img src='https://img.shields.io/badge/Project-Page-green?style=flat&logo=Google%20chrome&logoColor=green'></a>
</p>


<p align="center">
  <img src="assets/teaser.png" width="100%">
</p>

> **Dexplore** is a **unified optimization framework** that combines **retargeting** and **tracking** into a single learning loop for **dexterous manipulation** — using human demonstrations as **soft guidance** with adaptive spatial scopes to train policies across **diverse robot hands**.

## Installation

### Prerequisites

- NVIDIA GPU with CUDA support
- [Isaac Gym Preview 4](https://developer.nvidia.com/isaac-gym) (requires NVIDIA developer account)

### Setup

This project shares the same environment setup as [InterMimic](https://github.com/Sirui-Xu/InterMimic). Follow their installation instructions, or use the steps below:

```bash
conda create -n dexplore python=3.8
conda activate dexplore
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia

# Install Isaac Gym (follow NVIDIA's instructions)
cd isaacgym/python && pip install -e .

# Install pinned dependencies (rl-games version must be 1.1.4)
pip install -r requirement.txt

# Optional: for distillation (PointNet++ encoder)
pip install torch-geometric
```

### Robot hand assets

The robot hand URDFs and meshes shipped under [dexplore/data/assets/](dexplore/data/assets/) are derived from [dex-urdf](https://github.com/dexsuite/dex-urdf) with Dexplore-specific modifications: each hand has a 6-DOF floating-base wrist prepended (3 prismatic + 3 revolute joints), and the inspire hand is rebuilt from a SolidWorks export to match our lab hardware. Custom decimated collision meshes are added for sim performance. See [NOTICE](NOTICE) for upstream attribution and license aggregation.

## Data Preparation

The training data comes from the [GRAB](https://grab.is.tue.mpg.de/) dataset, which cannot be redistributed. You must download it yourself and run our conversion pipeline.

### Step 1: Download and Process Required Data

**GRAB dataset** — Register and download from [grab.is.tue.mpg.de](https://grab.is.tue.mpg.de/). Use [InterAct](https://github.com/wzyabcas/InterAct) to process the raw GRAB data — follow both the main processing pipeline and the [Data for Simulation](https://github.com/wzyabcas/InterAct#-data-for-simulation) section. Run the simulation step **for GRAB only** (`python interact2mimic.py --dataset_name grab`); the other datasets are not used here. This writes per-subject MuJoCo skeletons to `simulation/intermimic/data/assets/smplx/` named `smplx_grab_s{N}.xml`. You will also need the **SMPL-X body model** from [smpl-x.is.tue.mpg.de](https://smpl-x.is.tue.mpg.de/).

### Step 2: Organize Data

Extract the downloaded files into a single directory with the following structure:

```
grab_dir/
├── sequences/              # Processed sequences (from InterAct pipeline)
│   ├── s1_airplane_fly_1/
│   │   ├── motion.npz
│   │   └── object.npz
│   └── ...
├── objects/                # Object meshes (extracted from tools__object_meshes__contact_meshes.zip)
│   ├── cup/
│   │   ├── cup.ply
│   │   ├── sample_points.npy
│   │   └── ...
│   └── ...
├── tools/                  # Body templates (from GRAB download)
│   ├── male/               # Extracted from tools__subject_meshes__male.zip
│   │   ├── s1.ply
│   │   └── ...
│   └── female/             # Extracted from tools__subject_meshes__female.zip
│       └── ...
└── raw/                    # Raw per-subject data
    ├── s1/                 # Extracted from grab__s1.zip
    │   ├── airplane_fly_1.npz
    │   └── ...
    └── ...
```

> **Note:** After organizing the above, copy object meshes and the InterMimic-generated SMPL-X skeleton assets into the project:
> ```bash
> cp -r grab_dir/objects dexplore/data/assets/mjcf/
> cp -r /path/to/InterAct/simulation/intermimic/data/assets/smplx dexplore/data/assets/
> ```

### Step 3: Install Dependencies

```bash
pip install dex-retargeting sapien smplx
```

> **Note:** `dex-retargeting` and `sapien` require Python >= 3.9. If your training env uses Python 3.8 (required by isaacgym), create a separate env for data processing.

### Step 4: Run Conversion

```bash
python data_processing/convert_grab.py \
    --robot inspire \
    --grab_dir /path/to/grab_dir \
    --original_grab_dir /path/to/grab_dir/raw \
    --smplx_model_dir /path/to/smplx/models
```

Supported robots: `inspire`, `leap`, `allegro`, `shadow`.

## Quick Start

### Stage 1: Reference-Scoped Tracking (Teacher Policy)

Train a state-based teacher policy from human demonstrations:

```bash
# Replace {robot} with: inspire, leap, allegro, or shadow
python dexplore/run.py \
    --task Dexplore_{Robot} \
    --cfg_env dexplore/data/cfg/{robot}.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/{robot}.yaml \
    --output checkpoint/ --headless
```

### Stage 2: Vision-Based Distillation (Student Policy)

Distill the teacher into a vision-based controller using DAgger with a PointNet++ encoder and VAE:

```bash
python dexplore/run.py \
    --task Dexplore_Distill --distill \
    --cfg_env dexplore/data/cfg/inspire_distill.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/inspire_distill.yaml \
    --output checkpoint/ --headless
```


## Evaluation

### Stage 1: Teacher Policy Evaluation

Test a trained teacher checkpoint:

```bash
python dexplore/run.py \
    --task Dexplore_Inspire \
    --cfg_env dexplore/data/cfg/inspire.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/inspire.yaml \
    --test --checkpoint checkpoint/inspire.pth \
    --num_envs 16
```

Compute success rate metrics:

```bash
python dexplore/evaluate.py \
    --task Dexplore_Inspire \
    --cfg_env dexplore/data/cfg/inspire.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/inspire.yaml \
    --checkpoint checkpoint/inspire.pth \
    --headless --num_envs 64 --output eval_results.json
```

### Stage 2: Student Policy Evaluation

Visualize a distilled student checkpoint in the viewer (uses `eval_distill.py` without `--headless` since the distill checkpoint format requires its custom restore logic):

```bash
python dexplore/eval_distill.py \
    --task Dexplore_Distill --distill \
    --cfg_env dexplore/data/cfg/inspire_distill.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/inspire_distill.yaml \
    --checkpoint checkpoint/inspire_distill/nn/latest.pth \
    --num_envs 4 --output eval_results_distill.json
```

Or use the convenience script:

```bash
./scripts/vis_distill.sh
```

Compute success rate metrics:

```bash
python dexplore/eval_distill.py \
    --task Dexplore_Distill --distill \
    --cfg_env dexplore/data/cfg/inspire_distill.yaml \
    --cfg_train dexplore/data/cfg/train/rlg/inspire_distill.yaml \
    --checkpoint checkpoint/inspire_distill/nn/latest.pth \
    --headless --num_envs 64 --output eval_results_distill.json
```

Or use the convenience script:

```bash
./scripts/eval_distill.sh
```


## Robot Hands

We provide a pretrained checkpoint for the [Inspire](https://www.interbotix.com/) hand (18 DOFs). The framework is designed to be robot-agnostic — adding a new hand requires only a URDF and a thin task subclass. We include example implementations for several hands as reference:

| Robot | DOFs | Task Class | Config |
|-------|------|-----------|--------|
| [Inspire](https://www.interbotix.com/) | 18 (6 wrist + 12 finger) | `Dexplore_Inspire` | `inspire.yaml` |
| [LEAP](https://leaphand.com/) | 22 (6 wrist + 16 finger) | `Dexplore_Leap` | `leap.yaml` |
| [Allegro](https://www.wonikrobotics.com/) | 22 (6 wrist + 16 finger) | `Dexplore_Allegro` | `allegro.yaml` |
| [Shadow](https://www.shadowrobot.com/) | 30 (6 wrist + 24 finger) | `Dexplore_Shadow` | `shadow.yaml` |

### Adding a new robot hand

1. Create a URDF in `dexplore/data/assets/`
2. Create a subclass in `dexplore/env/tasks/dexplore_<name>.py`:

```python
from env.tasks.base_dexplore_task import DexploreTask

class Dexplore_MyRobot(DexploreTask):
    # Example: 18 DOFs = 6 wrist + 12 finger
    DOF_VELOCITY = (7,) * 18
    DOF_STIFFNESS = (200,) * 6 + (100,) * 12
    DOF_DAMPING = (20,) * 6 + (10,) * 12

    def _get_robot_type(self):
        return "my_robot_hand/my_robot_hand_right.urdf"

    def _apply_collision_filter(self, env_ptr, humanoid_handle):
        ...  # set per-link collision filters

    def _action_to_pd_targets(self, action):
        ...  # map actions to PD targets (handle coupled joints)

    def _set_env_state(self, env_ids, dof_pos, dof_vel):
        ...  # reset joint states (handle coupled joints at reset)
```

3. Register in `dexplore/utils/parse_task.py`
4. Create config YAMLs in `dexplore/data/cfg/`


## Citation

```bibtex
@inproceedings{xu2025dexplore,
    title={Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration},
    author={Xu, Sirui and Chao, Yu-Wei and Bian, Liuyu and Mousavian, Arsalan and Wang, Yu-Xiong and Gui, Liang-Yan and Yang, Wei},
    booktitle={CoRL},
    year={2025}
}

@inproceedings{xu2025intermimic,
  title = {{InterMimic}: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions},
  author = {Xu, Sirui and Ling, Hung Yu and Wang, Yu-Xiong and Gui, Liang-Yan},
  booktitle = {CVPR},
  year = {2025},
}
```

If you use the data processing pipeline, please also cite:

```bibtex
@inproceedings{xu2025interact,
  title = {{InterAct}: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation},
  author = {Xu, Sirui and Li, Dongting and Zhang, Yucheng and Xu, Xiyan and Long, Qi and Wang, Ziyin and Lu, Yunzhi and Dong, Shuchang and Jiang, Hezi and Gupta, Akshat and Wang, Yu-Xiong and Gui, Liang-Yan},
  booktitle = {CVPR},
  year = {2025},
}
```

## Acknowledgements

This codebase builds on [Isaac Gym](https://developer.nvidia.com/isaac-gym) and [rl_games](https://github.com/Denys88/rl_games). The core training algorithm is based on [InterMimic](https://github.com/Sirui-Xu/InterMimic). The data processing pipeline uses [InterAct](https://github.com/wzyabcas/InterAct) for GRAB data conversion, [dex-retargeting](https://github.com/dexsuite/dex-retargeting) for hand pose retargeting, and [dex-urdf](https://github.com/dexsuite/dex-urdf) for robot hand URDF models.

Note: The retargeting step in data processing is not strictly necessary for training -- we provide it as a convenient data preparation tool. Users can supply their own retargeted motion data in the expected format.


## File tree (depth 3, assets pruned)

```
.gitattributes
.gitignore
LICENSE
MODEL_CARD.md
NOTICE
README.md
SECURITY.md
checkpoint/
  inspire.pth
  inspire_distill.pth
data_processing/
  __init__.py
  convert_grab.py
  robot_configs.py
  skeleton_utils.py
  smpl_constants.py
dexplore/
  __init__.py
  env/
    tasks/
  eval_distill.py
  evaluate.py
  learning/
    amp_datasets.py
    common_agent.py
    common_player.py
    dexplore_agent.py
    dexplore_agent_distill.py
    dexplore_models.py
    dexplore_network_builder.py
    dexplore_network_builder_student.py
    dexplore_players.py
    models.py
    network_builder.py
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
requirement.txt
scripts/
  eval.sh
  eval_distill.sh
  train_allegro.sh
  train_inspire.sh
  train_leap.sh
  train_shadow.sh
  vis.sh
  vis_distill.sh
```

## Config files (0)


## Python signatures and reward/observation bodies (13 files)


### data_processing/robot_configs.py

```
"""Per-robot hand configurations for GRAB data conversion.

Each robot defines:
  - robot_name: name used for dex_retargeting RobotName enum and output filenames
  - urdf_subpath: path relative to dex_retargeting's robot hands directory
  - num_dof: number of DOFs (including 6 dummy wrist DOFs)
  - hand_joint_reorder: reordering of SMPL-X hand joints before retargeting (if needed)
  - sapien2isaac: mapping from SAPIEN joint order to Isaac Gym joint order"""
class RobotConfig()
    def get_sapien2isaac(self)
```

### dexplore/env/tasks/base_dexplore_task.py

```
"""Base task classes for Dexplore dexterous manipulation.

InterMimic: base class for motion-imitation tasks with Isaac Gym.
DexploreTask: extends InterMimic with motion loading, object handling,
              reward computation, and reference-scoped exploration."""
class InterMimic(BaseTask)
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
    def _apply_collision_filter(self, env_ptr, humanoid_handle)
    def _build_pd_action_offset_scale(self)
    def _get_humanoid_collision_filter(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _refresh_sim_tensors(self)
    def _compute_task_obs(self, env_ids, ref_obs)
    def _compute_observations_iter(self, env_ids, delta_t)
    def _compute_observations(self, env_ids)
    def _compute_humanoid_obs(self, env_ids, ref_obs, next_ts)
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
class DexploreTask(InterMimic)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _get_robot_type(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def post_physics_step(self)
    def _update_hist_hoi_obs(self, env_ids)
    def _setup_character_props(self, key_bodies)
    def _load_table(self, motion_file)
    def _load_motion(self, motion_file)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_proj(self, env_id, env_ptr)
    def _build_proj_tensors(self)
    def _load_proj_asset(self)
    def _load_marker_asset(self)
    def _load_target_asset(self)
    def _load_table_asset(self)
    def _build_target(self, env_id, env_ptr)
    def _build_table(self, env_id, env_ptr)
    def _build_marker(self, env_id, env_ptr)
    def _build_target_tensors(self)
    def _build_marker_state_tensors(self)
    def _reset_target(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _reset_envs(self, env_ids)
    def _reset_actors(self, env_ids)
    def _reset_default(self, env_ids)
    def _reset_ref_state_init(self, env_ids)
    def cal_cdf(self, i, e)
    def _reset_hybrid_state_init(self, env_ids)
    def _set_env_state(self, env_ids, dof_pos, dof_vel)
    def _compute_hoi_observations(self, env_ids)
    def _calc_perturb_times(self)
    def _update_proj(self)
    def play_dataset_step(self, time)
    def _draw_task_play(self, t)
    def render(self, sync_frame_time, t)
    def _draw_task(self)
def build_hoi_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, target_states, target_contact_buf, contact_buf, object_points, body_rot, body_vel, body_rot_vel)
def compute_obj_observations(body_pos, body_rot, tar_states, object_points, ref_obs)
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs, contact_forces, contact_body_ids, ref_obs, key_body_ids)
def huber_loss(diff, sigma)
def compute_humanoid_reward(hoi_ref, hoi_obs, contact_buf, tar_contact_forces, len_keypos, w, pos_actions, actions, object_points, object_pos_action, object_rot_action, num_dof, ball_size, t_sat, kappa)
def compute_humanoid_reset(reset_buf, progress_buf, max_episode_length, enable_early_termination, start_times, rollout_length, reset_ig, contact_reset)
def compute_sdf(points1, points2)

```python
def build_hoi_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos,
                           local_root_obs, root_height_obs, dof_obs_size, target_states, target_contact_buf, contact_buf, object_points, body_rot, body_vel, body_rot_vel):
    """Build the HOI observation vector from current state (for reward computation).
    Includes: root state, object state, key body positions, contact flags, interaction graph.
    """
    contact = torch.any(torch.abs(contact_buf) > 0.1, dim=-1).float()
    target_contact = torch.any(torch.abs(target_contact_buf) > 0.1, dim=-1).float().unsqueeze(1)

    tar_pos = target_states[:, 0:3]
    tar_rot = target_states[:, 3:7]
    obj_rot_extend = tar_rot.unsqueeze(1).repeat(1, object_points.shape[1], 1).view(-1, 4)
    object_points_extend = object_points.view(-1, 3)
    obj_points = torch_utils.quat_rotate(obj_rot_extend, object_points_extend).view(tar_rot.shape[0], object_points.shape[1], 3) + tar_pos.unsqueeze(1)
    ig = compute_sdf(key_body_pos, obj_points).view(-1, 3)
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot_extend = heading_rot.unsqueeze(1).repeat(1, key_body_pos.shape[1], 1).view(-1, 4)
    ig = quat_rotate(heading_rot_extend, ig).view(tar_pos.shape[0], -1)
    obs = torch.cat((root_rot, root_pos, torch.zeros((root_pos.shape[0], 48), device=root_pos.device), root_vel, torch.zeros((root_pos.shape[0], 48), device=root_pos.device), target_states, key_body_pos.contiguous().view(-1,key_body_pos.shape[1]*key_body_pos.shape[2]), target_contact, contact, ig, body_rot.view(-1, key_body_pos.shape[1]*4), body_vel.view(-1,key_body_pos.shape[1]*key_body_pos.shape[2]), body_rot_vel.view(-1, key_body_pos.shape[1]*3), dof_pos, dof_vel), dim=-1)
    return obs
```

```python
def compute_obj_observations(body_pos, body_rot, tar_states, object_points, ref_obs):
    """Compute object-centric observations: local object pose, velocity, and diffs from reference."""
    tar_pos = tar_states[:, 0:3]
    tar_rot = tar_states[:, 3:7]
    tar_vel = tar_states[:, 7:10]
    tar_ang_vel = tar_states[:, 10:13]
    root_pos = body_pos[:, 7]
    root_rot = body_rot[:, 7]
    ref_root_pos = ref_obs[:, 4:7]
    obj_rot_extend = tar_rot.unsqueeze(1).repeat(1, object_points.shape[1], 1).view(-1, 4)
    object_points_extend = object_points.view(-1, 3)
    obj_points = torch_utils.quat_rotate(obj_rot_extend, object_points_extend).view(tar_rot.shape[0], object_points.shape[1], 3) + tar_pos.unsqueeze(1)

    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_inv_rot = torch_utils.calc_heading_quat(root_rot)

    local_tar_pos = tar_pos - root_pos
    local_tar_pos = quat_rotate(heading_rot, local_tar_pos)
    local_tar_vel = quat_rotate(heading_rot, tar_vel)
    local_tar_ang_vel = quat_rotate(heading_rot, tar_ang_vel)

    local_tar_rot = quat_mul(heading_rot, tar_rot)
    local_tar_rot_obs = torch_utils.quat_to_tan_norm(local_tar_rot)

    _ref_obj_pos = ref_obs[:,106:109]
    diff_global_obj_pos = _ref_obj_pos - tar_pos
    diff_local_obj_pos_flat = torch_utils.quat_rotate(heading_rot, diff_global_obj_pos)

    local_ref_obj_pos = _ref_obj_pos - ref_root_pos
    local_ref_obj_pos = torch_utils.quat_rotate(heading_rot, local_ref_obj_pos)

    ref_obj_rot = ref_obs[:,109:113]
    diff_global_obj_rot = torch_utils.quat_mul_norm(torch_utils.quat_inverse(ref_obj_rot), tar_rot)
    diff_local_obj_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_rot, diff_global_obj_rot.view(-1, 4)), heading_inv_rot)
    diff_local_obj_rot_obs = torch_utils.quat_to_tan_norm(diff_local_obj_rot_flat)

    local_ref_obj_rot = torch_utils.quat_mul(heading_rot, ref_obj_rot)
    local_ref_obj_rot = torch_utils.quat_to_tan_norm(local_ref_obj_rot)

    ref_obj_vel = ref_obs[:, 113:116]
    diff_global_vel = ref_obj_vel - tar_vel
    diff_local_vel = torch_utils.quat_rotate(heading_rot, diff_global_vel)

    ref_obj_ang_vel = ref_obs[:, 116:119]
    diff_global_ang_vel = ref_obj_ang_vel - tar_ang_vel
    diff_local_ang_vel = torch_utils.quat_rotate(heading_rot, diff_global_ang_vel)

    obs = torch.cat([local_tar_pos, local_tar_rot_obs, local_tar_vel, local_tar_ang_vel, diff_local_obj_pos_flat, diff_local_obj_rot_obs, local_ref_obj_pos, local_ref_obj_rot, diff_local_vel, diff_local_ang_vel], dim=-1)
    return obs, obj_points
```

```python
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs, contact_forces, contact_body_ids, ref_obs, key_body_ids):
    """Compute policy observation: body state in root-local frame + diffs from reference.
    Includes position, rotation, velocity diffs and contact diffs for all key bodies.
    """
    # type: (Tensor, Tensor, Tensor, Tensor, bool, bool, Tensor, Tensor, Tensor, Tensor) -> Tensor
    root_pos = body_pos[:, 7, :]
    root_rot = body_rot[:, 7, :]

    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_inv_rot = torch_utils.calc_heading_quat(root_rot)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    len_keypos = len(key_body_ids)
    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand_2 = heading_rot_expand.repeat((1, len_keypos, 1))
    flat_heading_rot_2 = heading_rot_expand_2.reshape(heading_rot_expand_2.shape[0] * heading_rot_expand_2.shape[1],
                                               heading_rot_expand_2.shape[2])

    heading_rot_expand = heading_rot_expand.repeat((1, len_keypos, 1))
    flat_heading_rot = heading_rot_expand.reshape(heading_rot_expand.shape[0] * heading_rot_expand.shape[1],
                                               heading_rot_expand.shape[2])

    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2)
    heading_inv_rot_expand = heading_inv_rot_expand.repeat((1, len_keypos, 1))
    flat_heading_inv_rot = heading_inv_rot_expand.reshape(heading_inv_rot_expand.shape[0] * heading_inv_rot_expand.shape[1],
                                               heading_inv_rot_expand.shape[2])

    _ref_body_pos = ref_obs[:,119:119+len_keypos*3].view(-1, len_keypos, 3)
    _body_pos = body_pos[:, key_body_ids, :]
    diff_global_body_pos = _ref_body_pos - _body_pos
    diff_local_body_pos_flat = torch_utils.quat_rotate(flat_heading_rot_2, diff_global_body_pos.view(-1, 3)).view(-1, len_keypos * 3)

    local_ref_body_pos = _body_pos - root_pos.unsqueeze(1)
    local_ref_body_pos = torch_utils.quat_rotate(flat_heading_rot_2, local_ref_body_pos.view(-1, 3)).view(-1, len_keypos * 3)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos[:, key_body_ids, :] - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = quat_rotate(flat_heading_rot, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:] # remove root pos
    flat_body_rot = body_rot[:, key_body_ids, :].reshape(body_rot.shape[0] * len_keypos, body_rot.shape[2])
    flat_local_body_rot = quat_mul(flat_heading_rot, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_rot_obs = flat_local_body_rot_obs.reshape(body_rot.shape[0], len_keypos * flat_local_body_rot_obs.shape[1])

    ref_body_rot = ref_obs[:, 119+len_keypos*3+1+16+len_keypos*3: 119+len_keypos*3+1+16+len_keypos*3+16*4]
    diff_global_body_rot = torch_utils.quat_mul_norm(torch_utils.quat_in
```

### dexplore/env/tasks/base_task.py

```
"""Base task class for IsaacGym reinforcement learning environments."""
class BaseTask()
    """Base class for IsaacGym RL tasks, handling sim creation, stepping, rendering,
and domain randomization."""
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

### dexplore/env/tasks/dexplore_allegro.py

```
"""Dexplore task for the Allegro dexterous hand."""
class Dexplore_Allegro(DexploreTask)
    def _get_robot_type(self)
    def _apply_collision_filter(self, env_ptr, humanoid_handle)
    def _action_to_pd_targets(self, action)
    def _set_env_state(self, env_ids, dof_pos, dof_vel)
```

### dexplore/env/tasks/dexplore_distill.py

```
def get_all_paths(dir_path)
class Dexplore_Distill(Dexplore_Inspire)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _build_table(self, env_id, env_ptr)
    def create_camera_actors(self)
    def setup_env_cameras(self, env_ptr, camera_spec_dict)
    def sample_camera_rel_pos(self, radius, height)
    def sample_camera_rel_target(self, radius)
    def reset_env_cameras(self, env_id, camera_spec_dict)
    def create_tensors_for_env_cameras(self, env_ptr, env_camera_handles, camera_spec_dict)
    def get_camera_image_tensors_dict(self)
    def depth_image_to_point_cloud_GPU(self, depth_buffer, seg_buffer, camera_view_matrix_inv, camera_proj_matrix, v, u, width, height, depth_bar, device)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def post_physics_step(self)
    def _reset_envs(self, env_ids)
    def _compute_observations_distill(self, env_ids, delta_t)
    def collate(self, batch, N_lo, N_hi, training)
    def calculate_intersection_ratio(self, obj_points, pointcloud_camera_to_world, distance_threshold)
    def _setup_character_props(self, key_bodies)
    def step(self, weights)
    def reset(self, env_ids)
    def render(self, sync_frame_time, t)
    def _compute_humanoid_obs_pro(self, env_ids, ref_obs)
def compute_humanoid_observations_pro(body_pos, body_rot, dof_pos, contact_forces, contact_body_ids, ref_obs, key_body_ids, at_begin, keep_prob, obs_noise)

```python
def compute_humanoid_observations_pro(body_pos, body_rot, dof_pos, contact_forces, contact_body_ids, ref_obs, key_body_ids, at_begin, keep_prob=1.0, obs_noise=True):
    root_pos = body_pos[:, 7, :]
    root_rot = body_rot[:, 7, :]

    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    len_keypos = len(key_body_ids)
    heading_rot_expand = heading_rot.unsqueeze(-2)


    heading_rot_expand = heading_rot_expand.repeat((1, len_keypos, 1))
    flat_heading_rot = heading_rot_expand.reshape(heading_rot_expand.shape[0] * heading_rot_expand.shape[1],
                                               heading_rot_expand.shape[2])


    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos[:, key_body_ids, :] - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = quat_rotate(flat_heading_rot, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:] # remove root pos

    body_contact_buf = contact_forces[:, contact_body_ids, :].clone()
    contact = torch.any(torch.abs(body_contact_buf) > 0.1, dim=-1).float()
    ref_body_contact = torch.any((ref_obs[:,119+len_keypos*3+1:119+len_keypos*3+1+16][:, [3, 6, 9, 12, 15]] + 1) / 2 > 0.5, dim=-1)
    todo = torch.logical_or(at_begin, ref_body_contact).unsqueeze(1)

    root_pos = body_pos[:, 6, :]
    root_rot = body_rot[:, 6, :]

    # Wrist reference delta: translation (3D) + rotation (6D) in local frame
    ref_root_pos = ref_obs[:, 4:7]
    ref_root_rot = ref_obs[:, 0:4]
    wrist_trans_delta = ref_root_pos - root_pos
    wrist_trans_delta_local = quat_rotate(heading_rot, wrist_trans_delta)  # 3D
    rot_delta = torch_utils.quat_mul(torch_utils.quat_inverse(root_rot), ref_root_rot)
    rot_delta_6d = torch_utils.quat_to_tan_norm(rot_delta)  # 6D

    # Apply masking curriculum: zero out wrist delta with probability (1 - keep_prob)
    wrist_mask = (torch.rand(root_pos.shape[0], 1, device=root_pos.device) < keep_prob).float()
    wrist_trans_delta_local = wrist_trans_delta_local * wrist_mask
    rot_delta_6d = rot_delta_6d * wrist_mask

    local_obs = torch.cat((dof_pos[:, 3:], contact, todo, wrist_trans_delta_local, rot_delta_6d), dim=-1)
    # local_obs: 15 + 5 + 1 + 3 + 6 = 30D
    global_obs = torch.cat((root_pos, body_pos[:, key_body_ids, :][:, [3, 6, 9, 12, 15], :].view(-1, 5*3)), dim=-1)
    if obs_noise:
        global_obs = global_obs + 1e-2*torch.randn_like(global_obs)
    return local_obs, global_obs
```

```python
def _compute_observations_distill(self, env_ids=None, delta_t=16):

        cameras, camera_vinv, camera_proj = self.get_camera_image_tensors_dict()
        camera_names = list(self.camera_spec_dict.keys())
        name = "fix_camera_depth"
        cam_width = self.camera_spec_dict[name]["image_size"][0]
        cam_height = self.camera_spec_dict[name]["image_size"][1]
        # print(self.camera_u, self.camera_v)
        
        # depth_image_to_point_cloud_GPU(self, depth_buffer, seg_buffer, camera_view_matrix_inv, camera_proj_matrix, u, v, width:float, height:float, depth_bar:float, device:torch.device):

        points = self.depth_image_to_point_cloud_GPU(cameras["fix_camera_depth"], cameras["fix_camera_seg"], camera_vinv[name], camera_proj[name], self.camera_u, self.camera_v, cam_width, cam_height, 10, self.device)
        # # print(points[0][:, 0].max(), points[0][:, 1].max(), points[0][:, 2].max())
        # selected_points = self.sample_points(points, sample_num=self.pointCloudDownsampleNum, sample_mathed='random')
        # print(points.shape, selected_points.shape)
        # obs_images = cameras[camera_names[0]]
        # print(obs_images.max(), obs_images.min())
        # pointcloud_camera_to_world = self._get_pointcloud(self.camera_spec_dict[camera_names[0]], obs_images[0].cpu().numpy())
        # print(pointcloud_camera_to_world.shape)
        
        # points = self.depth_image_to_point_cloud_GPU(self.camera_tensors[i], self.camera_view_matrixs[i], self.camera_proj_matrixs[i], self.camera_u2, self.camera_v2, self.camera_props.width, self.camera_props.height, 10, self.device)
        # selected_points = self.sample_points(points, sample_num=self.pointCloudDownsampleNum, sample_mathed='random')
        # print(pointcloud_camera_to_world)
        # # Add coordicates
        visualize = False
        env_ids = to_torch(np.arange(self.num_envs), device=self.device, dtype=torch.long)
        ts = self.progress_buf.clone()
        self._curr_ref_obs = self.hoi_data[self.data_id[env_ids], ts].clone() 
        next_ts = torch.clamp(ts + delta_t, max=self.max_episode_length[self.data_id[env_ids]]-1)
        ref_obs = self.hoi_data[self.data_id[env_ids], next_ts].clone()
        local_obs, global_obs = self._compute_humanoid_obs_pro(env_ids, ref_obs)
        global_obs = global_obs.view(env_ids.shape[0], -1, 3)
        
        # if visualize:
        #     _, curr_obj_points = self._compute_task_obs(ref_obs=self.hoi_data[self.data_id, 0].clone())
        #     visualizer3d = Visualizer3D(
        #         view_config="o3d_view_conf.json", overwrite_view_config=True, non_blocking=True
        #     )

        #     visualizer3d.create_coordinate_frame(size=0.2)
        #     # camera_frame = True
        #     # if camera_frame:
        #     #     # Add point cloud from camera to world
        #     #     visualizer3d.create_pointcloud(
        #     #         pointcloud_camera["xyz"][pointcloud_camera["index"]],
        #     #         rgb=None,
        #     #         name="pointcloud_camera",
        #     #         radius=0.1,
        #     #     )
        #     # else:
        #     #     # Add point cloud from camera to world
        #     visualizer3d.create_pointcloud(
        #         points[0].cpu().numpy(),
        #         color=[0.5, 0.5, 0.5],
        #         name="pointcloud_camera_to_world",
        #         radius=0.1,
        #     )

        #     visualizer3d.create_pointcloud(
        #         curr_obj_points[0].cpu().numpy(),
        #         color=[0, 1.0, 0],
        #         name="oracle",
        #         radius=0.1,
        #     )
            
        #     visualizer3d.create_pointcloud(
        #         global_obs[0].cpu().numpy(),
        #         color=[0, 0, 1.0],
        #         name="hand",
        #         radius=1.0,
        #     )
        #     # Visualize the scene
        #     visualizer3d.draw_geometries()

        # Collate raw point cloud (no hand kp). Force ex
```
```

### dexplore/env/tasks/dexplore_inspire.py

```
"""Dexplore task for the Inspire dexterous hand."""
class Dexplore_Inspire(DexploreTask)
    def _get_robot_type(self)
    def _apply_collision_filter(self, env_ptr, humanoid_handle)
    def _action_to_pd_targets(self, action)
    def _set_env_state(self, env_ids, dof_pos, dof_vel)
```

### dexplore/env/tasks/dexplore_leap.py

```
"""Dexplore task for the LEAP dexterous hand."""
class Dexplore_Leap(DexploreTask)
    def _get_robot_type(self)
    def _apply_collision_filter(self, env_ptr, humanoid_handle)
    def _action_to_pd_targets(self, action)
    def _set_env_state(self, env_ids, dof_pos, dof_vel)
```

### dexplore/env/tasks/dexplore_shadow.py

```
"""Dexplore task for the Shadow dexterous hand."""
class Dexplore_Shadow(DexploreTask)
    def _get_robot_type(self)
    def _apply_collision_filter(self, env_ptr, humanoid_handle)
    def _action_to_pd_targets(self, action)
    def _set_env_state(self, env_ids, dof_pos, dof_vel)
```

### dexplore/env/tasks/vec_task.py

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

### dexplore/env/tasks/vec_task_wrappers.py

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
class VecTaskDAggerWrapper(VecTaskPythonWrapper)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def reset(self)
    def reset(self, env_ids)
    def step(self, actions)

```python
def amp_observation_space(self):
        return self._amp_obs_space
```
```

### dexplore/utils/config.py

```
def set_np_formatting()
def set_seed(seed, torch_deterministic)
def load_cfg(args)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark)
```

### dexplore/utils/parse_task.py

```
def parse_task(args, cfg, cfg_train, sim_params, distill)
```