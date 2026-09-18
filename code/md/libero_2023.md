# libero_2023

source: https://github.com/Lifelong-Robot-Learning/LIBERO


commit: 8f1084e3132a39270c3a13ebe37270a43ece2a01


## README

<div align="center">
<img src="https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/images/libero_logo.png" width="360">


<p align="center">
<a href="https://github.com/Lifelong-Robot-Learning/LIBERO/actions">
<img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg" />
</a>
<a href="https://github.com/Lifelong-Robot-Learning/LIBERO/graphs/contributors">
<img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/Lifelong-Robot-Learning/LIBERO" />
</a>
<a href="https://github.com/Lifelong-Robot-Learning/LIBERO/issues">
<img alt="Issues" src="https://img.shields.io/github/issues/Lifelong-Robot-Learning/LIBERO?color=0088ff" />

## **Benchmarking Knowledge Transfer for Lifelong Robot Learning**

Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone

[[Website]](https://libero-project.github.io)
[[Paper]](https://arxiv.org/pdf/2306.03310.pdf)
[[Docs]](https://lifelong-robot-learning.github.io/LIBERO/)
______________________________________________________________________
![pull_figure](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/images//fig1.png)
</div>

**LIBERO** is designed for studying knowledge transfer in multitask and lifelong robot learning problems. Successfully resolving these problems require both declarative knowledge about objects/spatial relationships and procedural knowledge about motion/behaviors. **LIBERO** provides:
- a procedural generation pipeline that could in principle generate an infinite number of manipulation tasks.
- 130 tasks grouped into four task suites: **LIBERO-Spatial**, **LIBERO-Object**, **LIBERO-Goal**, and **LIBERO-100**. The first three task suites have controlled distribution shifts, meaning that they require the transfer of a specific type of knowledge. In contrast, **LIBERO-100** consists of 100 manipulation tasks that require the transfer of entangled knowledge. **LIBERO-100** is further splitted into **LIBERO-90** for pretraining a policy and **LIBERO-10** for testing the agent's downstream lifelong learning performance.
- five research topics.
- three visuomotor policy network architectures.
- three lifelong learning algorithms with the sequential finetuning and multitask learning baselines.

---


# Contents

- [Installation](#Installation)
- [Datasets](#Dataset)
- [Getting Started](#Getting-Started)
  - [Task](#Task)
  - [Training](#Training)
  - [Evaluation](#Evaluation)
- [Citation](#Citation)
- [License](#License)


# Installtion
Please run the following commands in the given order to install the dependency for **LIBERO**.
```
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

Then install the `libero` package:
```
pip install -e .
```

# Datasets
We provide high-quality human teleoperation demonstrations for the four task suites in **LIBERO**. To download the demonstration dataset, run:
```python
python benchmark_scripts/download_libero_datasets.py
```
By default, the dataset will be stored under the ```LIBERO``` folder and all four datasets will be downloaded. To download a specific dataset, use
```python
python benchmark_scripts/download_libero_datasets.py --datasets DATASET
```
where ```DATASET``` is chosen from `[libero_spatial, libero_object, libero_100, libero_goal`.

**NEW!!!**

Alternatively, you can download the dataset from HuggingFace by using:
```python
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```

This option can also be combined with the specific dataset selection:
```python
python benchmark_scripts/download_libero_datasets.py --datasets DATASET --use-huggingface
```

The datasets hosted on HuggingFace are available at [here](https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets).


# Getting Started

For a detailed walk-through, please either refer to the documentation or the notebook examples provided under the `notebooks` folder. In the following, we provide example scripts for retrieving a task, training and evaluation.

## Task

The following is a minimal example of retrieving a specific task from a specific task suite.
```python
from libero.libero import benchmark
from libero.libero.envs import OffScreenRenderEnv


benchmark_dict = benchmark.get_benchmark_dict()
task_suite_name = "libero_10" # can also choose libero_spatial, libero_object, etc.
task_suite = benchmark_dict[task_suite_name]()

# retrieve a specific task
task_id = 0
task = task_suite.get_task(task_id)
task_name = task.name
task_description = task.language
task_bddl_file = os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file)
print(f"[info] retrieving task {task_id} from suite {task_suite_name}, the " + \
      f"language instruction is {task_description}, and the bddl file is {task_bddl_file}")

# step over the environment
env_args = {
    "bddl_file_name": task_bddl_file,
    "camera_heights": 128,
    "camera_widths": 128
}
env = OffScreenRenderEnv(**env_args)
env.seed(0)
env.reset()
init_states = task_suite.get_task_init_states(task_id) # for benchmarking purpose, we fix the a set of initial states
init_state_id = 0
env.set_init_state(init_states[init_state_id])

dummy_action = [0.] * 7
for step in range(10):
    obs, reward, done, info = env.step(dummy_action)
env.close()
```
Currently, we only support sparse reward function (i.e., the agent receives `+1` when the task is finished). As sparse-reward RL is extremely hard to learn, currently we mainly focus on lifelong imitation learning.

## Training
To start a lifelong learning experiment, please choose:
- `BENCHMARK` from `[LIBERO_SPATIAL, LIBERO_OBJECT, LIBERO_GOAL, LIBERO_90, LIBERO_10]`
- `POLICY` from `[bc_rnn_policy, bc_transformer_policy, bc_vilt_policy]`
- `ALGO` from `[base, er, ewc, packnet, multitask]`

then run the following:

```shell
export CUDA_VISIBLE_DEVICES=GPU_ID && \
export MUJOCO_EGL_DEVICE_ID=GPU_ID && \
python libero/lifelong/main.py seed=SEED \
                               benchmark_name=BENCHMARK \
                               policy=POLICY \
                               lifelong=ALGO
```
Please see the documentation for the details of reproducing the study results.

## Evaluation

By default the policies will be evaluated on the fly during training. If you have limited computing resource of GPUs, we offer an evaluation script for you to evaluate models separately.

```shell
python libero/lifelong/evaluate.py --benchmark BENCHMARK_NAME \
                                   --task_id TASK_ID \ 
                                   --algo ALGO_NAME \
                                   --policy POLICY_NAME \
                                   --seed SEED \
                                   --ep EPOCH \
                                   --load_task LOAD_TASK \
                                   --device_id CUDA_ID
```

# Citation
If you find **LIBERO** to be useful in your own research, please consider citing our paper:

```bibtex
@article{liu2023libero,
  title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
  journal={arXiv preprint arXiv:2306.03310},
  year={2023}
}
```

# License
| Component        | License                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Codebase         | [MIT License](LICENSE)                                                                                                                      |
| Datasets         | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode)                 |


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
benchmark_scripts/
  check_task_suites.py
  download_libero_datasets.py
  init_path.py
  render_single_task.py
  shasum_files.py
libero/
  configs/
    __init__.py
    config.yaml
    eval/
    lifelong/
    policy/
    reproduce_experiment/
    train/
  libero/
    __init__.py
    bddl_files/
    benchmark/
    envs/
    init_files/
    utils/
  lifelong/
    __init__.py
    algos/
    datasets.py
    evaluate.py
    init_path.py
    main.py
    metric.py
    models/
    utils.py
notebooks/
  custom_assets/
    libero_mug/
    libero_mug_yellow/
  custom_object_example.ipynb
  procedural_creation_walkthrough.ipynb
  quick_guide_algo.ipynb
  quick_walkthrough.ipynb
requirements.txt
scripts/
  check_dataset_integrity.py
  collect_demonstration.py
  config_copy.py
  create_dataset.py
  create_libero_task_example.py
  create_template.py
  get_affordance_info.py
  get_dataset_info.py
  init_path.py
  libero_100_collect_demonstrations.py
setup.py
templates/
  problem_class_template.py
  scene_template.xml
```

## Config files (29)


### libero/configs/config.yaml

```yaml
# @package _global_

defaults:
  - _self_
  - data: default
  - policy: bc_transformer_policy
  - train: default
  - eval: default
  - lifelong: base
  - test: null

seed: 10000
use_wandb: false
wandb_project: "lifelong learning"
folder: null # use default path
bddl_folder: null # use default path
init_states_folder: null # use default path
load_previous_model: false
device: "cuda"
task_embedding_format: "bert"
task_embedding_one_hot_offset: 1
pretrain: false
pretrain_model_path: ""
benchmark_name: "LIBERO_SPATIAL"

```

### libero/configs/eval/default.yaml

```yaml
load_path: "" # only used when separately evaluating a pretrained model
eval: true
batch_size: 64
num_workers: 4
n_eval: 20
eval_every: 5
max_steps: 600
use_mp: true
num_procs: 20
save_sim_states: false

```

### libero/configs/lifelong/agem.yaml

```yaml
algo: AGEM
n_memories: 1000

```

### libero/configs/lifelong/base.yaml

```yaml
algo: Sequential

```

### libero/configs/lifelong/er.yaml

```yaml
algo: ER
n_memories: 1000

```

### libero/configs/lifelong/ewc.yaml

```yaml
algo: EWC
e_lambda: 50000
gamma: 0.9

```

### libero/configs/lifelong/multitask.yaml

```yaml
algo: Multitask
eval_in_train: false

```

### libero/configs/lifelong/packnet.yaml

```yaml
algo: PackNet
prune_perc: 0.75
post_prune_epochs: 50
post_eval_every: 5

```

### libero/configs/lifelong/single_task.yaml

```yaml
algo: SingleTask

```

### libero/configs/policy/bc_rnn_policy.yaml

```yaml
policy_type: BCRNNPolicy
image_embed_size: 64
text_embed_size: 32

rnn_hidden_size: 1024
rnn_num_layers: 2
rnn_dropout: 0.0
rnn_bidirectional: false

defaults:
    - data_augmentation@color_aug: batch_wise_img_color_jitter_group_aug.yaml
    - data_augmentation@translation_aug: translation_aug.yaml
    - image_encoder: resnet_encoder
    - language_encoder: mlp_encoder
    - policy_head: gmm_head

```

### libero/configs/policy/bc_transformer_policy.yaml

```yaml
policy_type: BCTransformerPolicy 
extra_num_layers: 0
extra_hidden_size: 128
embed_size: 64

transformer_input_size: null
transformer_num_layers: 4
transformer_num_heads: 6
transformer_head_output_size: 64
transformer_mlp_hidden_size: 256
transformer_dropout: 0.1
transformer_max_seq_len: 10

defaults:
    - data_augmentation@color_aug: batch_wise_img_color_jitter_group_aug.yaml
    - data_augmentation@translation_aug: translation_aug.yaml
    - image_encoder: resnet_encoder.yaml
    - language_encoder: mlp_encoder.yaml
    - position_encoding@temporal_position_encoding: sinusoidal_position_encoding.yaml
    - policy_head: gmm_head.yaml

```

### libero/configs/policy/bc_vilt_policy.yaml

```yaml
policy_type: BCViLTPolicy
extra_num_layers: 0
extra_hidden_size: 128
embed_size: 128

spatial_transformer_input_size: null
spatial_transformer_num_layers: 7
spatial_transformer_num_heads: 8
spatial_transformer_head_output_size: 120
spatial_transformer_mlp_hidden_size: 256
spatial_transformer_dropout: 0.1

spatial_down_sample: true
spatial_down_sample_embed_size: 64

transformer_input_size: null
transformer_num_layers: 4
transformer_num_heads: 6
transformer_head_output_size: 64
transformer_mlp_hidden_size: 256
transformer_dropout: 0.1
transformer_max_seq_len: 10

defaults:
    - data_augmentation@color_aug: batch_wise_img_color_jitter_group_aug.yaml
    - data_augmentation@translation_aug: translation_aug.yaml
    - image_encoder: patch_encoder.yaml
    - language_encoder: mlp_encoder.yaml
    - position_encoding@temporal_position_encoding: sinusoidal_position_encoding.yaml
    - policy_head: gmm_head.yaml

```

### libero/configs/policy/data_augmentation/batch_wise_img_color_jitter_group_aug.yaml

```yaml
network: BatchWiseImgColorJitterAug

network_kwargs:
  input_shape: null
  brightness: 0.3
  contrast: 0.3
  saturation: 0.3
  hue: 0.3
  epsilon: 0.1
```

### libero/configs/policy/data_augmentation/identity_aug.yaml

```yaml
network: IdentityAug

network_kwargs:
  input_shape: null
```

### libero/configs/policy/data_augmentation/img_color_jitter_group_aug.yaml

```yaml

```

### libero/configs/policy/data_augmentation/translation_aug.yaml

```yaml
network: TranslationAug

network_kwargs:
  input_shape: null
  translation: 8
```

### libero/configs/policy/data_augmentation/translation_aug_group.yaml

```yaml
network: TranslationAugGroup

network_kwargs:
  input_shapes: {}
  translation: 8
```

### libero/configs/policy/image_encoder/patch_encoder.yaml

```yaml
network: PatchEncoder
network_kwargs:
    patch_size: [8, 8]
    no_patch_embed_bias: false

```

### libero/configs/policy/image_encoder/resnet_encoder.yaml

```yaml
network: ResnetEncoder
network_kwargs:
    pretrained: false
    freeze: false
    remove_layer_num: 4
    no_stride: false
    language_fusion: 'film'

```

### libero/configs/policy/language_encoder/clip_encoder.yaml

```yaml
network: CLIPEncoder
network_kwargs:
    model_type: "ViT-B/32"
    hidden_size: 128
    output_size: 128
    num_layers: 1
    download_path: "./clip"

```

### libero/configs/policy/language_encoder/identity_encoder.yaml

```yaml
network: IdentityEncoder
network_kwargs:
    dummy: true

```

### libero/configs/policy/language_encoder/mlp_encoder.yaml

```yaml
network: MLPEncoder
network_kwargs:
    input_size: 768
    hidden_size: 128
    output_size: 128
    num_layers: 1

```

### libero/configs/policy/language_encoder/rnn_encoder.yaml

```yaml
network: RNNEncoder
network_kwargs:
    input_size: 768
    hidden_size: 128
    output_size: 16
    num_layers: 1

```

### libero/configs/policy/policy_head/gmm_head.yaml

```yaml
network: GMMHead

network_kwargs:
    hidden_size: 1024
    num_layers: 2
    min_std: 0.0001
    num_modes: 5
    low_eval_noise: false
    activation: "softplus"

loss_kwargs:
    loss_coef: 1.0

```

### libero/configs/policy/position_encoding/sinusoidal_position_encoding.yaml

```yaml
network: SinusoidalPositionEncoding
network_kwargs:
    input_size: null
    inv_freq_factor: 10
    factor_ratio: null


```

### libero/configs/reproduce_experiment/default_experiment.yaml

```yaml
# @package _global_

default:
- override /policy: bc_transformer_policy

train:
  use_augmentation: true
  grad_clip: 100
  loss_scale: 1.0

eval:
  eval_every: 5
  n_epochs: 50


```

### libero/configs/train/default.yaml

```yaml
# training
n_epochs: 50
batch_size: 32
num_workers: 4
grad_clip: 100.
loss_scale: 1.0

# resume training
resume: false
resume_path: ""
debug: false

use_augmentation: true

defaults:
    - optimizer@optimizer: adam_w.yaml
    - scheduler@scheduler: cosine_annealing.yaml

```

### libero/configs/train/optimizer/adam_w.yaml

```yaml
name: torch.optim.AdamW

kwargs: 
    lr: 0.0001
    betas: [0.9, 0.999]    
    weight_decay: 0.0001

```

### libero/configs/train/scheduler/cosine_annealing.yaml

```yaml
name: torch.optim.lr_scheduler.CosineAnnealingLR

kwargs:
    eta_min: 1e-5
    last_epoch: -1

```

## Python signatures and reward/observation bodies (55 files)


### benchmark_scripts/check_task_suites.py

```
"""This script is to test if users can successfully load all the environments, the benchmark initial states in their machines"""
def main()
```

### benchmark_scripts/render_single_task.py

```
def render_task(task, bddl_file, init_states, demo_file)
def main()
```

### libero/libero/envs/arenas/coffee_table_arena.py

```
class CoffeeTableArena(Arena)
    """Empty workspace."""
    def __init__(self, xml, floor_style, wall_style)
```

### libero/libero/envs/arenas/empty_arena.py

```
class EmptyArena(Arena)
    """Empty workspace."""
    def __init__(self, xml, floor_style, wall_style)
```

### libero/libero/envs/arenas/kitchen_arena.py

```
class KitchenTableArena(Arena)
    """Workspace that contains an empty table.


Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of arena when placing table.
       """
    def __init__(self, table_full_size, table_friction, table_offset, has_legs, xml, floor_style, wall_style)
    def configure_location(self)
    def table_top_abs(self)
```

### libero/libero/envs/arenas/living_room_arena.py

```
class LivingRoomTableArena(Arena)
    """Empty workspace."""
    def __init__(self, table_full_size, table_friction, table_offset, xml, floor_style, wall_style)
```

### libero/libero/envs/arenas/study_arena.py

```
class StudyTableArena(Arena)
    """Workspace that contains an empty table.


Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of arena when placing table.
       """
    def __init__(self, table_full_size, table_friction, table_offset, has_legs, xml, floor_style, wall_style)
    def configure_location(self)
    def table_top_abs(self)
```

### libero/libero/envs/arenas/style.py

```
def get_texture_filename(type, style)
```

### libero/libero/envs/arenas/table_arena.py

```
class TableArena(Arena)
    """Workspace that contains an empty table.


Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of arena when placing table.
       """
    def __init__(self, table_full_size, table_friction, table_offset, has_legs, xml, floor_style, wall_style)
    def configure_location(self)
    def table_top_abs(self)
```

### libero/libero/envs/base_object.py

```
def register_object(target_class)
def register_visual_change_object(target_class)
```

### libero/libero/envs/bddl_base_domain.py

```
def register_problem(target_class)
class BDDLBaseDomain(SingleArmEnv)
    """A base domain for parsing bddl files."""
    def __init__(self, bddl_file_name, robots, env_configuration, controller_configs, gripper_types, initialization_noise, use_latch, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, object_property_initializers, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, table_full_size, workspace_offset, arena_type, scene_xml, scene_properties)
    def seed(self, seed)
    def reward(self, action)
    def _assert_problem_name(self)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _generate_object_state_wrapper(self, skip_object_names)
    def _load_distracting_objects(self, mujoco_arena)
    def _load_custom_material(self)
    def _setup_camera(self, mujoco_arena)
    def _load_model(self)
    def _setup_placement_initializer(self, mujoco_arena)
    def _setup_references(self)
    def _setup_observables(self)
    def _create_obj_sensors(self, obj_name, modality)
    def _add_placement_initializer(self)
    def _reset_internal(self)
    def _check_success(self)
    def visualize(self, vis_settings)
    def step(self, action)
    def _pre_action(self, action, policy_step)
    def _post_action(self, action)
    def _post_process(self)
    def get_robot_state_vector(self, obs)
    def is_fixture(self, object_name)
    def language_instruction(self)
    def get_object(self, object_name)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 1.0 is provided if the task succeeds.

        Args:
            action (np.array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # Scale reward if requested
        if self.reward_scale is not None:
            reward *= self.reward_scale / 1.0

        return reward
```
```

### libero/libero/envs/bddl_utils.py

```
def get_regions(t, regions, group)
def get_scenes(t, scene_properties, group)
def get_problem_info(problem_filename)
def robosuite_parse_problem(problem_filename)
```

### libero/libero/envs/env_wrapper.py

```
class ControlEnv()
    def __init__(self, bddl_file_name, robots, controller, gripper_types, initialization_noise, use_camera_obs, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def obj_of_interest(self)
    def step(self, action)
    def reset(self)
    def check_success(self)
    def _visualizations(self)
    def robots(self)
    def sim(self)
    def get_sim_state(self)
    def _post_process(self)
    def _update_observables(self, force)
    def set_state(self, mujoco_state)
    def reset_from_xml_string(self, xml_string)
    def seed(self, seed)
    def set_init_state(self, init_state)
    def regenerate_obs_from_state(self, mujoco_state)
    def close(self)
class OffScreenRenderEnv(ControlEnv)
    """For visualization and evaluation."""
    def __init__(self)
class SegmentationRenderEnv(OffScreenRenderEnv)
    """This wrapper will additionally generate the segmentation mask of objects,
which is useful for comparing attention."""
    def __init__(self, camera_segmentations, camera_heights, camera_widths)
    def step(self, action)
    def reset(self)
    def get_segmentation_instances(self, segmentation_image)
    def get_segmentation_of_interest(self, segmentation_image)
    def segmentation_to_rgb(self, seg_im, random_colors)
class DemoRenderEnv(ControlEnv)
    """For visualization and evaluation."""
    def __init__(self)
    def _get_observations(self)

```python
def _get_observations(self):
        return self.env._get_observations()
```
```

### libero/libero/envs/object_states/base_object_states.py

```
class BaseObjectState()
    def __init__(self)
    def get_geom_state(self)
    def check_contact(self, other)
    def check_contain(self, other)
    def get_joint_state(self)
    def is_open(self)
    def is_close(self)
    def get_size(self)
    def check_ontop(self, other)
class ObjectState(BaseObjectState)
    def __init__(self, env, object_name, is_fixture)
    def get_geom_state(self)
    def check_contact(self, other)
    def check_contain(self, other)
    def get_joint_state(self)
    def check_ontop(self, other)
    def set_joint(self, qpos)
    def is_open(self)
    def is_close(self)
    def turn_on(self)
    def turn_off(self)
    def update_state(self)
class SiteObjectState(BaseObjectState)
    """This is to make site based objects to have the same API as normal Object State."""
    def __init__(self, env, object_name, parent_name, is_fixture)
    def get_geom_state(self)
    def check_contain(self, other)
    def check_contact(self, other)
    def check_ontop(self, other)
    def set_joint(self, qpos)
    def is_open(self)
    def is_close(self)
```

### libero/libero/envs/objects/__init__.py

```
def get_object_fn(category_name)
def get_object_dict()
```

### libero/libero/envs/objects/articulated_objects.py

```
class ArticulatedObject(MujocoXMLObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class Microwave(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class SlideCabinet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
class Window(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
class Faucet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
class BasinFaucet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
class ShortCabinet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class ShortFridge(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class WoodenCabinet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class WhiteCabinet(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def is_open(self, qpos)
    def is_close(self, qpos)
class FlatStove(ArticulatedObject)
    def __init__(self, name, obj_name, joints)
    def turn_on(self, qpos)
    def turn_off(self, qpos)
```

### libero/libero/envs/objects/google_scanned_objects.py

```
class GoogleScannedObject(MujocoXMLObject)
    def __init__(self, name, obj_name, joints)
class Rack(GoogleScannedObject)
    def __init__(self, name, obj_name, joints)
class WhiteBowl(GoogleScannedObject)
    def __init__(self, name, obj_name)
class AkitaBlackBowl(GoogleScannedObject)
    def __init__(self, name, obj_name)
class Plate(GoogleScannedObject)
    def __init__(self, name, obj_name)
class Basket(GoogleScannedObject)
    def __init__(self, name, obj_name)
class Chefmate8Frypan(GoogleScannedObject)
    def __init__(self, name, obj_name)
class GlazedRimPorcelainRamekin(GoogleScannedObject)
    def __init__(self, name, obj_name)
```

### libero/libero/envs/objects/hope_objects.py

```
class HopeBaseObject(MujocoXMLObject)
    def __init__(self, name, obj_name)
class AlphabetSoup(HopeBaseObject)
    def __init__(self, name, obj_name)
class BbqSauce(HopeBaseObject)
    def __init__(self, name, obj_name)
class Butter(HopeBaseObject)
    def __init__(self, name, obj_name)
class Cherries(HopeBaseObject)
    def __init__(self, name, obj_name)
class ChocolatePudding(HopeBaseObject)
    def __init__(self, name, obj_name)
class Cookies(HopeBaseObject)
    def __init__(self, name, obj_name)
class Corn(HopeBaseObject)
    def __init__(self, name, obj_name)
class CreamCheese(HopeBaseObject)
    def __init__(self, name, obj_name)
class Ketchup(HopeBaseObject)
    def __init__(self, name, obj_name)
class MacaroniAndCheese(HopeBaseObject)
    def __init__(self, name, obj_name)
class Mayo(HopeBaseObject)
    def __init__(self, name, obj_name)
class Milk(HopeBaseObject)
    def __init__(self, name, obj_name)
class OrangeJuice(HopeBaseObject)
    def __init__(self, name, obj_name)
class Popcorn(HopeBaseObject)
    def __init__(self, name, obj_name)
class SaladDressing(HopeBaseObject)
    def __init__(self, name, obj_name)
class NewSaladDressing(HopeBaseObject)
    def __init__(self, name, obj_name)
class TomatoSauce(HopeBaseObject)
    def __init__(self, name, obj_name)
```

### libero/libero/envs/objects/site_object.py

```
class SiteObject()
    def __init__(self, name, parent_name, joints, size, rgba, site_type, site_pos, site_quat, object_properties)
    def in_box(self, this_position, this_mat, other_position)
    def __str__(self)
    def under(self, this_position, this_mat, other_position, other_height)
```

### libero/libero/envs/objects/target_zones.py

```
class TargetZone(SiteObject)
    def __init__(self, name, zone_height, z_offset, rgba, joints, zone_size, zone_centroid_xy)
    def in_box(self, this_position, this_mat, other_position)
    def on_top(self, this_position, this_mat, other_position)
```

### libero/libero/envs/objects/turbosquid_objects.py

```
class TurbosquidObjects(MujocoXMLObject)
    def __init__(self, name, obj_name, joints)
class WoodenTray(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WhiteStorageBox(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WoodenShelf(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WoodenTwoLayerShelf(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WineRack(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WineBottle(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class DiningSetGroup(TurbosquidObjects)
    """This dining set group is mostly for visualization"""
    def __init__(self, name, obj_name, joints)
class BowlDrainer(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class MokaPot(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class BlackBook(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class YellowBook(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class RedCoffeeMug(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class DeskCaddy(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class PorcelainMug(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
class WhiteYellowMug(TurbosquidObjects)
    def __init__(self, name, obj_name, joints)
```

### libero/libero/envs/predicates/__init__.py

```
def update_predicate_fn_dict(fn_key, fn_name)
def eval_predicate_fn(predicate_fn_name)
def get_predicate_fn_dict()
def get_predicate_fn(predicate_fn_name)
```

### libero/libero/envs/predicates/base_predicates.py

```
class Expression()
    def __init__(self)
    def __call__(self)
class UnaryAtomic(Expression)
    def __init__(self)
    def __call__(self, arg1)
class BinaryAtomic(Expression)
    def __init__(self)
    def __call__(self, arg1, arg2)
class MultiarayAtomic(Expression)
    def __init__(self)
    def __call__(self)
class TruePredicateFn(MultiarayAtomic)
    def __init__(self)
    def __call__(self)
class FalsePredicateFn(MultiarayAtomic)
    def __init__(self)
    def __call__(self)
class InContactPredicateFn(BinaryAtomic)
    def __call__(self, arg1, arg2)
class In(BinaryAtomic)
    def __call__(self, arg1, arg2)
class On(BinaryAtomic)
    def __call__(self, arg1, arg2)
class Up(BinaryAtomic)
    def __call__(self, arg1)
class Stack(BinaryAtomic)
    def __call__(self, arg1, arg2)
class PrintJointState(UnaryAtomic)
    """This is a debug predicate to allow you print the joint values of the object you care"""
    def __call__(self, arg)
class Open(UnaryAtomic)
    def __call__(self, arg)
class Close(UnaryAtomic)
    def __call__(self, arg)
class TurnOn(UnaryAtomic)
    def __call__(self, arg)
class TurnOff(UnaryAtomic)
    def __call__(self, arg)
```

### libero/libero/envs/problems/libero_coffee_table_manipulation.py

```
class Libero_Coffee_Table_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/problems/libero_floor_manipulation.py

```
class Libero_Floor_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/problems/libero_kitchen_tabletop_manipulation.py

```
class Libero_Kitchen_Tabletop_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/problems/libero_living_room_tabletop_manipulation.py

```
class Libero_Living_Room_Tabletop_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/problems/libero_study_tabletop_manipulation.py

```
class Libero_Study_Tabletop_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/problems/libero_tabletop_manipulation.py

```
class Libero_Tabletop_Manipulation(BDDLBaseDomain)
    def __init__(self, bddl_file_name)
    def _load_fixtures_in_arena(self, mujoco_arena)
    def _load_objects_in_arena(self, mujoco_arena)
    def _load_sites_in_arena(self, mujoco_arena)
    def _add_placement_initializer(self)
    def _check_success(self)
    def _eval_predicate(self, state)
    def _setup_references(self)
    def _post_process(self)
    def set_visualization(self)
    def _setup_camera(self, mujoco_arena)
```

### libero/libero/envs/regions/__init__.py

```
def update_region_samplers(problem_name, region_sampler_name, region_sampler_class_name)
def get_region_samplers(problem_name, region_sampler_name)
```

### libero/libero/envs/regions/base_region_sampler.py

```
class MultiRegionRandomSampler(ObjectPositionSampler)
    """Places all objects within the table uniformly random.
Args:
    name (str): Name of this sampler.
    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models
    x_range (2-array of float): Specify the (min, max) relative x_range used to uniformly pl"""
    def __init__(self, name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_x(self, object_horizontal_radius)
    def _sample_y(self, object_horizontal_radius)
    def _sample_quat(self)
    def sample(self, fixtures, reference, on_top)
class SiteRegionRandomSampler(ObjectPositionSampler)
    """Places all objects on a site
Args:
    name (str): Name of this sampler.
    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models
    x_range (2-array of float): Specify the (min, max) relative x_range used to uniformly place objects
    y_range ("""
    def __init__(self, name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset, sim)
    def _sample_x(self, object_horizontal_radius)
    def _sample_y(self, object_horizontal_radius)
    def _sample_quat(self)
    def sample(self, sim, fixtures, reference, site_name, on_top)
class InSiteRegionRandomSampler(SiteRegionRandomSampler)
    """Places an object inside a site
Args:
    name (str): Name of this sampler.
    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models
    x_range (2-array of float): Specify the (min, max) relative x_range used to uniformly place objects
    y_range"""
    def __init__(self, name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_quat(self)
    def sample(self, sim, fixtures, reference, site_name, on_top)
class SiteSequentialCompositeSampler(ObjectPositionSampler)
    """Samples position for each object sequentially. Allows chaining
multiple placement initializers together - so that object locations can
be sampled on top of other objects or relative to other object placements.
Args:
    name (str): Name of this sampler."""
    def __init__(self, name)
    def append_sampler(self, sampler, sample_args)
    def hide(self, mujoco_objects)
    def add_objects(self, mujoco_objects)
    def add_objects_to_sampler(self, sampler_name, mujoco_objects)
    def reset(self)
    def sample(self, sim, fixtures, reference, on_top)
```

### libero/libero/envs/regions/object_property_sampler.py

```
class ObjectPropertySampler()
    """Base class of object placement sampler.
Args:
    name (str): Name of this sampler.
    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models
    ensure_object_boundary_in_range (bool): If True, will ensure that the object is enclosed within a give"""
    def __init__(self, name, mujoco_objects)
    def add_objects(self, mujoco_objects)
    def reset(self)
    def sample(self, predicate_name)
class OpenCloseSampler(ObjectPropertySampler)
    def __init__(self, name, state_type, mujoco_objects, joint_ranges)
    def sample(self)
class TurnOnOffSampler(ObjectPropertySampler)
    def __init__(self, name, state_type, mujoco_objects, joint_ranges)
    def sample(self)
```

### libero/libero/envs/regions/workspace_region_sampler.py

```
class TableRegionSampler(MultiRegionRandomSampler)
    def __init__(self, object_name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_quat(self)
class Libero100TableRegionSampler(MultiRegionRandomSampler)
    def __init__(self, object_name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_quat(self)
class ObjectBasedSampler(MultiRegionRandomSampler)
    def __init__(self, object_name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_quat(self)
```

### libero/libero/envs/robots/mounted_panda.py

```
class MountedPanda(ManipulatorModel)
    """Panda is a sensitive single-arm robot designed by Franka.
Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_mount(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### libero/libero/envs/robots/on_the_ground_panda.py

```
class OnTheGroundPanda(ManipulatorModel)
    """Panda is a sensitive single-arm robot designed by Franka.
Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_mount(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### libero/libero/envs/textures.py

```
def get_texture_file_list(type, texture_path)
```

### libero/libero/envs/utils.py

```
class MultiRegionRandomSampler(ObjectPositionSampler)
    """Places all objects within the table uniformly random.
Args:
    name (str): Name of this sampler.
    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models
    x_range (2-array of float): Specify the (min, max) relative x_range used to uniformly pl"""
    def __init__(self, name, mujoco_objects, x_ranges, y_ranges, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_x(self, object_horizontal_radius)
    def _sample_y(self, object_horizontal_radius)
    def _sample_quat(self)
    def sample(self, fixtures, reference, on_top)
def postprocess_model_xml(xml_str, cameras_dict, demo_generation)
def rectangle2xyrange(rect_ranges)
```

### libero/libero/envs/venv.py

```
def deprecation(msg)
class CloudpickleWrapper(object)
    """A cloudpickle wrapper used in SubprocVectorEnv."""
    def __init__(self, data)
    def __getstate__(self)
    def __setstate__(self, data)
class EnvWorker(ABC)
    """An abstract worker for an environment."""
    def __init__(self, env_fn)
    def get_env_attr(self, key)
    def set_env_attr(self, key, value)
    def send(self, action)
    def recv(self)
    def reset(self)
    def step(self, action)
    def wait(workers, wait_num, timeout)
    def seed(self, seed)
    def render(self)
    def close_env(self)
    def close(self)
class ShArray()
    """Wrapper of multiprocessing Array."""
    def __init__(self, dtype, shape)
    def save(self, ndarray)
    def get(self)
def _setup_buf(space)
def _worker(parent, p, env_fn_wrapper, obs_bufs)
class DummyEnvWorker(EnvWorker)
    """Dummy worker used in sequential vector environments."""
    def __init__(self, env_fn)
    def get_env_attr(self, key)
    def set_env_attr(self, key, value)
    def reset(self)
    def wait(workers, wait_num, timeout)
    def send(self, action)
    def seed(self, seed)
    def render(self)
    def close_env(self)
    def check_success(self)
    def get_segmentation_of_interest(self, segmentation_image)
    def get_sim_state(self)
    def set_init_state(self, init_state)
class SubprocEnvWorker(EnvWorker)
    """Subprocess worker used in SubprocVectorEnv and ShmemVectorEnv."""
    def __init__(self, env_fn, share_memory)
    def get_env_attr(self, key)
    def set_env_attr(self, key, value)
    def _decode_obs(self)
    def wait(workers, wait_num, timeout)
    def send(self, action)
    def recv(self)
    def reset(self)
    def seed(self, seed)
    def render(self)
    def close_env(self)
    def check_success(self)
    def get_segmentation_of_interest(self, segmentation_image)
    def get_sim_state(self)
    def set_init_state(self, init_state)
class BaseVectorEnv(object)
    """Base class for vectorized environments.

Usage:
::

    env_num = 8
    envs = DummyVectorEnv([lambda: gym.make(task) for _ in range(env_num)])
    assert len(envs) == env_num

It accepts a list of environment generators. In other words, an environment
generator ``efn`` of a specific task means that"""
    def __init__(self, env_fns, worker_fn, wait_num, timeout)
    def _assert_is_not_closed(self)
    def __len__(self)
    def __getattribute__(self, key)
    def get_env_attr(self, key, id)
    def set_env_attr(self, key, value, id)
    def _wrap_id(self, id)
    def _assert_id(self, id)
    def reset(self, id)
    def step(self, action, id)
    def seed(self, seed)
    def render(self)
    def close(self)
class DummyVectorEnv(BaseVectorEnv)
    """Dummy vectorized environment wrapper, implemented in for-loop.

.. seealso::

    Please refer to :class:`~tianshou.env.BaseVectorEnv` for other APIs' usage."""
    def __init__(self, env_fns)
    def check_success(self)
    def get_segmentation_of_interest(self, segmentation_images)
    def get_sim_state(self)
    def set_init_state(self, init_state, id)
class SubprocVectorEnv(BaseVectorEnv)
    """Vectorized environment wrapper based on subprocess.

.. seealso::

    Please refer to :class:`~tianshou.env.BaseVectorEnv` for other APIs' usage."""
    def __init__(self, env_fns)
    def check_success(self)
    def get_segmentation_of_interest(self, segmentation_images)
    def get_sim_state(self)
    def set_init_state(self, init_state, id)
```

### libero/libero/utils/task_generation_utils.py

```
def register_task_info(language, scene_name, objects_of_interest, goal_states)
def get_task_info(scene_name)
def get_suite_generator_func(workspace_name)
def generate_bddl_from_task_info(folder)
```

### libero/lifelong/algos/multitask.py

```
class Multitask(Sequential)
    """The multitask learning baseline/upperbound."""
    def __init__(self, n_tasks, cfg)
    def learn_all_tasks(self, datasets, benchmark, result_summary)
```

### libero/lifelong/algos/single_task.py

```
class SingleTask(Sequential)
    """The sequential BC baseline."""
    def __init__(self, n_tasks, cfg)
    def start_task(self, task)
```

### libero/lifelong/models/base_policy.py

```
def register_policy(policy_class)
def get_policy_class(policy_name)
def get_policy_list()
class PolicyMeta(type)
    """Metaclass for registering environments"""
    def __new__(meta, name, bases, class_dict)
class BasePolicy(Module)
    def __init__(self, cfg, shape_meta)
    def forward(self, data)
    def get_action(self, data)
    def _get_img_tuple(self, data)
    def _get_aug_output_dict(self, out)
    def preprocess_input(self, data, train_mode)
    def compute_loss(self, data, reduction)
    def reset(self)
```

### libero/lifelong/models/bc_rnn_policy.py

```
class ExtraModalities()
    def __init__(self, use_joint, use_gripper, use_ee, extra_hidden_size, extra_embedding_size)
    def __call__(self, obs_dict)
    def output_shape(self, input_shape, shape_meta)
class BCRNNPolicy(BasePolicy)
    """Input: (o_{t-H}, ... , o_t)
Output: a_t or distribution of a_t"""
    def __init__(self, cfg, shape_meta)
    def forward(self, data, train_mode)
    def get_action(self, data)
    def reset(self)
```

### libero/lifelong/models/bc_transformer_policy.py

```
class ExtraModalityTokens(Module)
    def __init__(self, use_joint, use_gripper, use_ee, extra_num_layers, extra_hidden_size, extra_embedding_size)
    def forward(self, obs_dict)
class PerturbationAttention()
    """See https://arxiv.org/pdf/1711.00138.pdf for perturbation-based visualization
for understanding a control agent."""
    def __init__(self, model, image_size, patch_size, device)
    def __call__(self, data)
class BCTransformerPolicy(BasePolicy)
    """Input: (o_{t-H}, ... , o_t)
Output: a_t or distribution of a_t"""
    def __init__(self, cfg, shape_meta)
    def temporal_encode(self, x)
    def spatial_encode(self, data)
    def forward(self, data)
    def get_action(self, data)
    def reset(self)
```

### libero/lifelong/models/bc_vilt_policy.py

```
def reshape_transform(tensor, h, w)
class BCViLTPolicy(BasePolicy)
    """Input: (o_{t-H}, ... , o_t)
Output: a_t or distribution of a_t"""
    def __init__(self, cfg, shape_meta)
    def spatial_encode(self, data)
    def temporal_encode(self, x)
    def forward(self, data)
    def get_action(self, data)
    def reset(self)
```

### libero/lifelong/models/policy_head.py

```
class DeterministicHead(Module)
    def __init__(self, input_size, output_size, hidden_size, num_layers)
    def forward(self, x)
class GMMHead(Module)
    def __init__(self, input_size, output_size, hidden_size, num_layers, min_std, num_modes, activation, low_eval_noise, loss_coef)
    def forward_fn(self, x)
    def forward(self, x)
    def loss_fn(self, gmm, target, reduction)
```

### scripts/config_copy.py

```
def main()
```

### scripts/create_libero_task_example.py

```
"""This is a standalone file for create a task in libero."""
class KitchenScene1(InitialSceneTemplates)
    def __init__(self)
    def define_regions(self)
    def init_states(self)
def main()
```