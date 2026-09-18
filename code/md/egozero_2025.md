# egozero_2025

source: https://github.com/vliu15/egozero


commit: 51dc1c622b564bcc10515777c6a8489b5833b3b5


## README

<p align="center">
    <img src="assets/egozero_github.gif" width="70%">
</p>


<h1 align="center" style="font-size: 2.0em; font-weight: bold; margin-bottom: 0; border: none; border-bottom: none;">EgoZero:<br>Robot Learning from Smart Glasses</h1>

##### <p align="center">[Vincent Liu<sup>*1</sup>](https://vliu15.github.io)&emsp;[Ademi Adeniji<sup>*12</sup>](https://ademiadeniji.github.io/)&emsp;[David Zhan<sup>*1</sup>](https://linkedin.com/in/david-zhan-96935126a)</p>
##### <p align="center">[Siddhant Haldar<sup>1</sup>](https://siddhanthaldar.github.io/)&emsp;[Raunaq Bhirangi<sup>1</sup>](https://raunaqbhirangi.github.io/)&emsp;[Pieter Abbeel<sup>2</sup>](https://people.eecs.berkeley.edu/~pabbeel/)&emsp;[Lerrel Pinto<sup>1</sup>](https://lerrelpinto.com)</p>
##### <p align="center"><sup>1</sup>New York University&emsp;<sup>2</sup>UC Berkeley</p>
##### <p align="center"><sup>*</sup>Equal contribution</p>

<div align="center">
    <a href="https://arxiv.org/abs/2505.20290"><img src="https://img.shields.io/static/v1?label=Paper&message=arXiv&color=red"></a> &ensp;
    <a href="https://egozero-robot.github.io/"><img src="https://img.shields.io/static/v1?label=Project%20Page&message=Website&color=blue"></a> &ensp;
</div>

## table of contents
- [Installation](#installation)
- [Data Collection](#data-collection)
- [Preprocessing](#preprocessing)
- [Training](#training)
- [Inference](#inference)
- [Franka-Teach](#franka-teach)

## installation
```bash
git submodule update --init --recursive
conda create -y -n egozero python=3.10
conda activate egozero
bash setup.sh
```

Add the following environment variables to your `~/.bashrc` or `~/.zshrc` with your institution's username and password
```bash
export ARIA_MPS_UNAME="your_uname"
export ARIA_MPS_PASSW="your_passw"
```

Verify that your dependencies have been installed correctly, run
```bash
aria-doctor
```

Pair the glasses via USB to your computer
```bash
aria auth pair
```

## data collection
To record offline so that the complete `.vrs` file can be submitted to the MPS server for data postprocessing, you must first install the [Aria mobile app](https://facebookresearch.github.io/projectaria_tools/docs/ARK/mobile_companion_app) and the [Aria studio](https://facebookresearch.github.io/projectaria_tools/docs/ARK/aria_studio). Then,
1. Connect to the glasses on the Aria mobile app
2. Create a new recording session
3. Transfer the `.vrs` file onto your computer

Submit the video for data processing on the MPS server and reorganize the output folder. Job submission may take anywhere from 5 to 30 minutes. For example, if your `.vrs` file is `pick_bread_1.vrs`, you would run
```bash
bash scripts/submit_mps.sh pick_bread_1
```

> In our experiments, we collect all our data with only the right hand and reset the task with the left hand. You may swap this, but our preprocessing script segments individual demonstrations based on absence of the specified hand.

## preprocessing
Copy the collect data to this repo on a machine where you will run preprocessing. Ideally this machine has GPU compute.

Label the expert points on your demonstration by opening `label_points.ipynb` with a Python kernel. Modify the paths in the first cell and run the entire notebook. Label points on the displayed image by clicking points and click the `Save Points` button. Run full preprocessing with
```bash
python preprocess.py --mps_sample_path mps_pick_bread_1_vrs/ --is_right_hand --prompts "a bread slice." "a plate."
```

## training
1. Create a new config yaml for your new task at `point_policy/cfgs/suite/task/franka_env/` and customize the `num_object_points`, `root_dir`, and `prompts` fields. See `point_policy/cfgs/suite/task/franka_env/pick_bread.yaml` for reference.
2. Modify `scripts/train.sh` to point to your new dataset and task config. Set the `data_dirs` and `experiment` variables.
3. Train the model with `bash scripts/train.sh`. See `point_policy/cfgs/config.yaml` and `point_policy/cfgs/suite/aria.yaml` for hydra flags from command line.

## inference
First go through the [Franka-Teach](#franka-teach) section to make sure the hardware is running correctly.
1. Modify `scripts/eval.sh` to point to your new dataset, task config, and checkpoint weights (should be saved in `point_policy/exp_local`).
2. Inference the model with `bash scripts/eval.sh`. See `point_policy/cfgs/config.yaml` and `point_policy/cfgs/suite/aria.yaml` for hydra flags from command line.

To stream the iPhone to get RGBD for robot rollout, run
```bash
python scripts/stream_iphone.py
```

## franka-teach
To run the robot, see the [Franka-Teach](https://github.com/NYU-robot-learning/Franka-Teach) repository for how to run Franka robots


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    lint.yaml
.gitignore
.gitmodules
Franka-Teach/
LICENSE
README.md
camera_calibration/
  constants.py
  convert_to_pkl_human.py
  generate_r2c_extrinsic.py
  process_data_human.py
  utils.py
franka-env/
  franka_env/
    __init__.py
    envs/
  setup.py
hamer/
label_points.ipynb
point_policy/
  README.md
  agent/
    baku.py
    mtpi.py
    networks/
    p3po.py
    point_policy.py
  cfgs/
    agent/
    config.yaml
    config_eval.yaml
    dataloader/
    suite/
  dift/
  eval.py
  eval_point_track.py
  logger.py
  point_utils/
    correspondence.py
    depth.py
    points_class.py
  read_data/
    __init__.py
    aria.py
    baku.py
    mtpi.py
    p3po.py
    point_policy.py
  replay_buffer.py
  robot_utils/
    franka/
  suite/
    baku.py
    mtpi.py
    p3po.py
    point_policy.py
  train.py
  utils.py
  video.py
preprocess.py
pyproject.toml
requirements.txt
scripts/
  eval.sh
  preprocess.sh
  stream_aria.py
  stream_iphone.py
  submit_mps.sh
  train.sh
setup.sh
utils/
  data_utils.py
  depth_utils.py
  hand_utils.py
  io_utils.py
  segment_utils.py
  transform_utils.py
  vis_utils.py
```

## Config files (16)


### point_policy/cfgs/agent/p3po.yaml

```yaml
# @package agent
_target_: agent.p3po.BCAgent
obs_shape: ??? # to be specified later
action_shape: ??? # to be specified later
device: ${device}
lr: 1e-4
hidden_dim: ${suite.hidden_dim}
stddev_schedule: 0.1
use_tb: ${use_tb}
policy_head: ${policy_head}
pixel_keys: ${suite.pixel_keys}
history: ${suite.history}
history_len: ${suite.history_len}
eval_history_len: ${suite.eval_history_len}
temporal_agg: ${temporal_agg}
max_episode_len: ${suite.task_make_fn.max_episode_len}
num_queries: ${num_queries}
use_robot_points: ${suite.use_robot_points}
num_robot_points: ${suite.num_robot_points}
use_object_points: ${suite.use_object_points}
num_object_points: ${suite.num_object_points}
point_dim: ${suite.point_dim}

```

### point_policy/cfgs/config.yaml

```yaml
defaults:
  - _self_
  - agent: point_policy
  - suite: point_policy
  - dataloader: point_policy
  - override hydra/launcher: submitit_local

# Dir
root_dir: ~/egozero
data_dir: /path/to/dir

# misc
seed: 2
device: cuda
save_video: true
use_tb: true
batch_size: 512

# experiment
num_demos_per_task: 100
policy_head: deterministic
use_proprio: false
eval: false
experiment: train
experiment_label: ${policy_head}

# action chunking
temporal_agg: false  # aggregate actions over time
num_queries: 12

# expert dataset
expert_dataset: ${dataloader.bc_dataset}

# Load weights
load_bc: false
bc_weight: path/to/weight

hydra:
  run:
    dir: ./exp_local/${now:%Y.%m.%d}/${experiment}/${experiment_label}/${now:%H%M%S}_hidden_dim_${suite.hidden_dim}
  sweep:
    dir: ./exp_local/${now:%Y.%m.%d}/${now:%H%M%S}
    subdir: ${hydra.job.num}
  launcher:
    tasks_per_node: 1
    nodes: 1
    submitit_folder: ./exp_local/${now:%Y.%m.%d}/${now:%H%M%S}_${experiment}/.slurm

```

### point_policy/cfgs/config_eval.yaml

```yaml
defaults:
  - _self_
  - agent: point_policy
  - suite: point_policy
  - dataloader: point_policy
  - override hydra/launcher: submitit_local

# Dir
root_dir: ~/egozero
data_dir: /path/to/expert_demos
prompts: []

# misc
seed: 2
device: cuda
save_video: true
use_tb: true
batch_size: 64

# experiment
num_demos_per_task: 100
policy_head: deterministic
use_proprio: false
eval: true
experiment: eval
experiment_label: ${policy_head}

simulate: true

# action chunking
temporal_agg: false # aggregate actions over time
num_queries: 12

# expert dataset
expert_dataset: ${dataloader.bc_dataset}

# Load weights
bc_weight: path/to/weight

hydra:
  run:
    dir: ./exp_local/eval/${now:%Y.%m.%d}_${experiment}/${experiment_label}/${now:%H%M%S}_hidden_dim_${suite.hidden_dim}
  sweep:
    dir: ./exp_local/${now:%Y.%m.%d}/${now:%H%M%S}
    subdir: ${hydra.job.num}
  launcher:
    tasks_per_node: 1
    nodes: 1
    submitit_folder: ./exp_local/${now:%Y.%m.%d}/${now:%H%M%S}_${experiment}/.slurm

```

### point_policy/cfgs/dataloader/aria.yaml

```yaml
bc_dataset:
  _target_: read_data.aria.BCDataset
  path: ${data_dir}
  tasks: ${suite.task.task_name}
  num_demos_per_task: ${num_demos_per_task}
  history: ${suite.history}
  history_len: ${suite.history_len}
  temporal_agg: ${temporal_agg}
  num_queries: ${num_queries}
  img_size: ${suite.img_size}
  action_after_steps: ${suite.action_after_steps}
  pixel_keys: ${suite.pixel_keys}
  subsample: 1
  skip_first_n: 0
  action_type: ${suite.action_type}
  gt_depth: ${suite.gt_depth}

```

### point_policy/cfgs/suite/aria.yaml

```yaml
# @package suite
defaults:
  - _self_
  - task: franka_env

suite: franka_env
name: "franka_env"

# obs dims
img_size: [720, 960]  # width, height
use_robot_points: false
num_robot_points: null
gt_depth: true

# action compute
point_dim: 3
action_type: "absolute" # absolute, delta

# object points
use_object_points: true
num_object_points: ${suite.task.num_object_points}

# task settings
action_repeat: 1
hidden_dim: 512

# train settings
num_train_steps: 400010
log_every_steps: 100
save_every_steps: 50000
history: false
history_len: 10

# eval
eval_every_steps: 200000
num_eval_episodes: 1
eval_history_len: 10

# data loading
action_after_steps: 1

# obs_keys
pixel_keys: ["pixels6"]
proprio_key: ""
feature_key: "features"

# snapshot
save_snapshot: true

task_make_fn:
  _target_: suite.p3po.make
  task_name: ${suite.task.task_name}
  object_labels: ${suite.task.object_labels}
  root_dir: ${suite.task.root_dir}
  action_repeat: ${suite.action_repeat}
  height: ${suite.img_size[1]}
  width: ${suite.img_size[0]}
  max_episode_len: ??? # to be specified later
  max_state_dim: ??? # to be specified later
  calib_path: ${root_dir}/calib/0331_calib_left_demo_7.npy
  eval: ${eval} # eval true mean use robot
  pixel_keys: ${suite.pixel_keys}
  use_robot_points: ${suite.use_robot_points}
  num_robot_points: ${suite.num_robot_points}
  use_object_points: ${suite.use_object_points}
  num_object_points: ${suite.num_object_points}
  action_type: ${suite.action_type}
  points_cfg: ??? # to be specified later
  use_gt_depth: ${suite.gt_depth}
  point_dim: ${suite.point_dim}
  prompts: ${suite.task.prompts}

```

### point_policy/cfgs/suite/points_cfg.yaml

```yaml
defaults:
  - _self_
  - task: p3po

# TODO: this is hard-coded
root_dir: null
dift_path: point_policy/dift
cotracker_checkpoint: ~/egozero/checkpoints/scaled_online.pth

prompts: []
pixel_keys: null
device: "cuda"

width: -1
height: -1
image_size_multiplier: 1

ensemble_size: 8
dift_layer: 1
dift_steps: 50
use_segmentation: true

num_points: -1

object_labels: null

```

### point_policy/cfgs/suite/task/franka_env/collect_ball.yaml

```yaml
defaults:
  - _self_

task_name: collect_ball
object_labels: [objects]
num_object_points: 5

root_dir: "/path/to/mps"
prompts: ["an orange.", "a ball.", "an orange ball.", "a green cup."]

```

### point_policy/cfgs/suite/task/franka_env/fold_towel.yaml

```yaml
defaults:
  - _self_

task_name: fold_towel
object_labels: [objects]
num_object_points: 6

root_dir: "/path/to/mps"
prompts: ["a towel.", "a rag.", "a cloth rag.", "a bath towel."]

```

### point_policy/cfgs/suite/task/franka_env/open_oven.yaml

```yaml
defaults:
  - _self_

task_name: open_oven
object_labels: [objects]
num_object_points: 9

root_dir: "/path/to/mps"
prompts: ["an oven.", "a toaster oven.", "a microwave."]

```

### point_policy/cfgs/suite/task/franka_env/pick_bread.yaml

```yaml
defaults:
  - _self_

task_name: pick_bread
object_labels: [objects]
num_object_points: 11

root_dir: "/path/to/mps"
prompts: ["an orange bread.", "a bread slice.", "a white plate."]

```

### point_policy/cfgs/suite/task/franka_env/place_bottle.yaml

```yaml
defaults:
  - _self_

task_name: place_bottle
object_labels: [objects]
num_object_points: 9

root_dir: "/path/to/mps"
prompts: ["a bamboo rack.", "a wood rack.", "a coca cola bottle.", "a plastic bottle."]

```

### point_policy/cfgs/suite/task/franka_env/put_book.yaml

```yaml
defaults:
  - _self_

task_name: put_book
object_labels: [objects]
num_object_points: 8

root_dir: "/path/to/mps"
prompts: ["a black notebook.", "a blue notebook.", "a gray metal shelf.", "a gray metal book rack."]

```

### point_policy/cfgs/suite/task/franka_env/sort_fruit.yaml

```yaml
defaults:
  - _self_

task_name: sort_fruit
object_labels: [objects]
num_object_points: 10

root_dir: "/path/to/mps"
prompts: ["a bowl.", "a white bowl.", "a lemon.", "a lime.", "a tangerine."]

```

### point_policy/cfgs/suite/task/franka_env/sweep_board.yaml

```yaml
defaults:
  - _self_

task_name: sweep_board
object_labels: [objects]
num_object_points: 8

root_dir: "/path/to/mps"
prompts: ["a black board with green tape in the middle.", "a small gray rectangular cuboid on the table.", "a small gray eraser block."]
```

### point_policy/cfgs/suite/task/franka_env/sweep_broom.yaml

```yaml
defaults:
  - _self_

task_name: sweep_broom
object_labels: [objects]
num_object_points: 5

root_dir: "/path/to/mps"
prompts: ["a yellow ball.", "a yellow orange.", "a small ball.", "a green plastic cup."]

```

### point_policy/cfgs/suite/task/franka_env.yaml

```yaml
defaults:
  - _self_
  - franka_env: 0121_bottle_on_rack

suite: franka_env

task_name: ${suite.task.franka_env.task_name}
object_labels: ${suite.task.franka_env.object_labels}
num_object_points: ${suite.task.franka_env.num_object_points}

root_dir: ${suite.task.franka_env.root_dir}
prompts: ${suite.task.franka_env.prompts}

```

## Python signatures and reward/observation bodies (46 files)


### franka-env/franka_env/envs/franka_env.py

```
class FrankaEnv(Env)
    def __init__(self, width, height, use_robot, use_gt_depth, crop_h, crop_w, cam_ids)
    def get_state(self)
    def step(self, abs_action)
    def reset(self)
    def render(self, mode, cam_idx, width, height)
```

### point_policy/agent/baku.py

```
class Actor(Module)
    def __init__(self, repr_dim, act_dim, hidden_dim, policy_head, num_feat_per_step, device)
    def forward(self, obs, stddev, action)
class BCAgent()
    def __init__(self, obs_shape, action_shape, device, lr, hidden_dim, stddev_schedule, use_tb, policy_head, pixel_keys, proprio_key, use_proprio, history, history_len, eval_history_len, temporal_agg, max_episode_len, num_queries, use_depth)
    def __repr__(self)
    def train(self, training)
    def buffer_reset(self)
    def clear_buffers(self)
    def act(self, obs, norm_stats, step, global_step, eval_mode)
    def update(self, expert_replay_iter, step)
    def save_snapshot(self)
    def load_snapshot(self, payload, eval)
```

### point_policy/agent/mtpi.py

```
class Actor(Module)
    def __init__(self, repr_dim, act_dim, hidden_dim, policy_head, num_feat_per_step, num_track_points, device, num_points)
    def forward(self, obs, past_tracks, stddev, target, mask)
class BCAgent()
    def __init__(self, obs_shape, action_shape, device, lr, hidden_dim, stddev_schedule, use_tb, policy_head, pixel_keys, history, history_len, eval_history_len, temporal_agg, max_episode_len, num_queries, num_robot_points, use_object_points, num_object_points, pred_gripper)
    def __repr__(self)
    def train(self, training)
    def buffer_reset(self)
    def clear_buffers(self)
    def act(self, obs, norm_stats, step, global_step, eval_mode)
    def update(self, expert_replay_iter, step)
    def save_snapshot(self)
    def load_snapshot(self, payload, eval)
```

### point_policy/agent/networks/dit.py

```
"""DiT like transformer for point-tracks
Adapted from: https://github.com/facebookresearch/DiT/blob/main/models.py
Inspired by: https://github.com/homangab/Track-2-Act/blob/main/single_script.py"""
def modulate(x, shift, scale)
class DiTBlock(Module)
    """A DiT block with adaptive layer norm zero (adaLN-Zero) conditioning."""
    def __init__(self, hidden_size, num_heads, mlp_ratio)
    def forward(self, x, c)
class FinalLayer(Module)
    """The final layer of DiT."""
    def __init__(self, hidden_size, patch_size, out_channels)
    def forward(self, x, c)
class DiT(Module)
    """Diffusion model with a Transformer backbone."""
    def __init__(self, horizon, hidden_size, depth, num_heads, mlp_ratio, learn_sigma, cond_dim, num_points, with_pos_emb, num_conds)
    def initialize_weights(self)
    def unpatchify(self, x)
    def forward(self, x, y)
def get_2d_sincos_pos_embed(embed_dim, grid_size, cls_token, extra_tokens)
def get_2d_sincos_pos_embed_from_grid(embed_dim, grid)
def get_1d_sincos_pos_embed_from_grid(embed_dim, pos)
```

### point_policy/agent/networks/gpt.py

```
"""An adaptation of Andrej Karpathy's nanoGPT implementation in PyTorch.
Original source: https://github.com/karpathy/nanoGPT

Original License:
MIT License

Copyright (c) 2022 Andrej Karpathy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to th"""
def new_gelu(x)
class CausalSelfAttention(Module)
    def __init__(self, config)
    def forward(self, x)
class MLP(Module)
    def __init__(self, config)
    def forward(self, x)
class Block(Module)
    def __init__(self, config)
    def forward(self, x)
class GPTConfig()
class GPT(Module)
    def __init__(self, config)
    def forward(self, input, targets)
    def _init_weights(self, module)
    def crop_block_size(self, block_size)
    def configure_optimizers(self, weight_decay, learning_rate, betas)
```

### point_policy/agent/networks/mlp.py

```
class MLP(Sequential)
    """This block implements the multi-layer perceptron (MLP) module.
Adapted for backward compatibility from the torchvision library:
https://pytorch.org/vision/0.14/generated/torchvision.ops.MLP.html

LICENSE:

From PyTorch:

Copyright (c) 2016-     Facebook, Inc            (Adam Paszke)
Copyright (c) 20"""
    def __init__(self, in_channels, hidden_channels, activation_layer, inplace, bias, dropout)
```

### point_policy/agent/networks/policy_head.py

```
class DeterministicHead(Module)
    def __init__(self, input_size, output_size, hidden_size, num_layers, action_squash, loss_coef)
    def forward(self, x, stddev, ret_action_value)
    def loss_fn(self, dist, target, mask, reduction)
    def pred_loss_fn(self, pred, target, reduction)
class DiffusionHead(Module)
    def __init__(self, input_size, output_size, obs_horizon, pred_horizon, hidden_size, num_layers, device, loss_coef)
    def forward(self, x, stddev, ret_action_value)
    def loss_fn(self, out, target, mask, reduction)
```

### point_policy/agent/networks/rgb_modules.py

```
"""Code from: https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/libero/lifelong/models/modules/rgb_modules.py

This file contains all neural modules related to encoding the spatial
information of obs_t, i.e., the abstracted knowledge of the current visual
input conditioned on the language."""
class SpatialSoftmax(Module)
    """The spatial softmax layer (https://rll.berkeley.edu/dsae/dsae.pdf)"""
    def __init__(self, in_c, in_h, in_w, num_kp)
    def forward(self, x)
class SpatialProjection(Module)
    def __init__(self, input_shape, out_dim)
    def forward(self, x)
    def output_shape(self, input_shape)
class ResnetEncoder(Module)
    """A Resnet-18-based encoder for mapping an image to a latent vector

Encode (f) an image into a latent vector.

y = f(x), where
    x: (B, C, H, W)
    y: (B, H_out)

Args:
    input_shape:      (C, H, W), the shape of the image
    output_size:      H_out, the latent vector size
    pretrained:      """
    def __init__(self, input_shape, output_size, pretrained, freeze, remove_layer_num, no_stride, language_dim, language_fusion)
    def forward(self, x, lang, return_intermediate)
    def output_shape(self)
class DinoV2Encoder(Module)
    def __init__(self, input_shape, output_size, pretrained, freeze, remove_layer_num, no_stride, language_dim, language_fusion)
    def forward(self, x, lang, return_intermediate)
```

### point_policy/agent/networks/utils/diffusion_policy.py

```
class SinusoidalPosEmb(Module)
    def __init__(self, dim)
    def forward(self, x)
class Downsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Upsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Conv1dBlock(Module)
    """Conv1d --> GroupNorm --> Mish"""
    def __init__(self, inp_channels, out_channels, kernel_size, n_groups)
    def forward(self, x)
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups)
    def forward(self, x, cond)
class ModuleAttrMixin(Module)
    def __init__(self)
    def device(self)
    def dtype(self)
class TransformerForDiffusion(ModuleAttrMixin)
    def __init__(self, input_dim, output_dim, horizon, n_obs_steps, cond_dim, n_layer, n_head, n_emb, p_drop_emb, p_drop_attn, causal_attn, time_as_cond, obs_as_cond, n_cond_layers)
    def _init_weights(self, module)
    def get_optim_groups(self, weight_decay)
    def configure_optimizers(self, learning_rate, weight_decay, betas)
    def forward(self, sample, timestep, cond)
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups)
    def forward(self, sample, timestep, global_cond)
class DiffusionPolicy(Module)
    def __init__(self, obs_dim, act_dim, obs_horizon, pred_horizon, hidden_dim, num_layers, data_act_scale, data_obs_scale, policy_type, device)
    def forward(self, obs_seq, action_seq)
    def _update(self, obs_seq, action_seq)
    def normalize_obs_data(self, data)
    def unnormalize_obs_data(self, data)
    def normalize_act_data(self, data)
    def unnormalize_act_data(self, data)
    def _predict(self, obs_seq)
    def ema_step(self)
    def _begin_epoch(self, optimizer)
```

### point_policy/agent/p3po.py

```
"""Model that divides image into patches and performs cross attention with patches around points
to predict future point tracks."""
class Actor(Module)
    def __init__(self, repr_dim, act_dim, history_len, hidden_dim, policy_head, device)
    def forward(self, past_tracks, stddev, action)
class BCAgent()
    def __init__(self, obs_shape, action_shape, device, lr, hidden_dim, stddev_schedule, use_tb, policy_head, pixel_keys, history, history_len, eval_history_len, temporal_agg, max_episode_len, num_queries, use_robot_points, num_robot_points, use_object_points, num_object_points, point_dim)
    def __repr__(self)
    def train(self, training)
    def buffer_reset(self)
    def clear_buffers(self)
    def act(self, obs, norm_stats, step, global_step, eval_mode)
    def update(self, expert_replay_iter, step)
    def save_snapshot(self)
    def load_snapshot(self, payload, eval)
```

### point_policy/agent/point_policy.py

```
class Actor(Module)
    def __init__(self, repr_dim, act_dim, num_track_points, hidden_dim, policy_head, device, pred_gripper)
    def forward(self, past_tracks, stddev, target, mask)
class BCAgent()
    def __init__(self, obs_shape, action_shape, device, lr, hidden_dim, stddev_schedule, use_tb, policy_head, pixel_keys, history, history_len, eval_history_len, temporal_agg, max_episode_len, num_queries, use_robot_points, num_robot_points, use_object_points, num_object_points, point_dim, pred_gripper)
    def __repr__(self)
    def train(self, training)
    def buffer_reset(self)
    def clear_buffers(self)
    def act(self, obs, norm_stats, step, global_step, eval_mode)
    def update(self, expert_replay_iter, step)
    def save_snapshot(self)
    def load_snapshot(self, payload, eval)
```

### point_policy/eval.py

```
def make_agent(obs_spec, action_spec, cfg)
class WorkspaceIL()
    def __init__(self, cfg)
    def global_step(self)
    def global_episode(self)
    def global_frame(self)
    def eval(self)
    def save_snapshot(self)
    def load_snapshot(self, snapshots)
def main(cfg)
```

### point_policy/eval_point_track.py

```
def make_agent(obs_spec, action_spec, cfg)
class Workspace()
    def __init__(self, cfg)
    def global_step(self)
    def global_episode(self)
    def global_frame(self)
    def T_ego_to_robot(self)
    def robot_wrist_to_eeff(self)
    def ego_to_robot(self, pos_in_ego)
    def robot_to_ego(self, pos_in_robot)
    def unproject(self, time_step, visualize)
    def plot_points_with_depth(self, frame, points)
    def eval(self)
    def save_snapshot(self)
    def load_snapshot(self, snapshots)
def main(cfg)
```

### point_policy/logger.py

```
class AverageMeter(object)
    def __init__(self)
    def update(self, value, n)
    def value(self)
class MetersGroup(object)
    def __init__(self, csv_file_name, formating)
    def log(self, key, value, n)
    def _prime_meters(self)
    def _remove_old_entries(self, data)
    def _dump_to_csv(self, data)
    def _format(self, key, value, ty)
    def _dump_to_console(self, data, prefix)
    def dump(self, step, prefix)
class Logger(object)
    def __init__(self, log_dir, use_tb)
    def _try_sw_log(self, key, value, step)
    def log(self, key, value, step)
    def log_metrics(self, metrics, step, ty)
    def dump(self, step, ty)
    def log_and_dump_ctx(self, step, ty)
class LogAndDumpCtx()
    def __init__(self, logger, step, ty)
    def __enter__(self)
    def __call__(self, key, value)
    def __exit__(self)
```

### point_policy/point_utils/correspondence.py

```
class Correspondence()
    def __init__(self, device, width, height, image_size_multiplier, ensemble_size, dift_layer, dift_steps, use_segmentation)
    def _forward_grounded_dino(self, image, prompts, crop_size, box_threshold, text_threshold)
    def _forward_dift(self, image, prompt)
    def set_expert_correspondence(self, expert_image, prompts)
    def find_correspondence(self, current_image, coords)
```

### point_policy/point_utils/depth.py

```
class Depth()
    def __init__(self, depth_path, device)
    def get_depth(self, image)
```

### point_policy/point_utils/points_class.py

```
class PointsClass()
    def __init__(self, root_dir, dift_path, cotracker_checkpoint, prompts, pixel_keys, device, width, height, image_size_multiplier, ensemble_size, dift_layer, dift_steps, use_segmentation, num_points, object_labels, use_gt_depth)
    def add_to_image_list(self, image, pixel_key)
    def reset_episode(self)
    def find_semantic_similar_points(self, pixel_key, object_label)
    def get_depth(self, pixel_key, last_n_frames)
    def set_depth(self, depth, pixel_key, original_image_size, current_image_size, crop_ratios)
    def track_points(self, pixel_key, last_n_frames, is_first_step, one_frame)
    def track_points_hand(self, pixel_key)
    def get_points(self, pixel_key, last_n_frames)
    def get_points_on_image(self, pixel_key, last_n_frames)
    def plot_image(self, pixel_key, last_n_frames)
```

### point_policy/read_data/aria.py

```
"""Implements an IterableDataset for Aria data"""
def break_long_segments(trajectory, labels, max_eps)
def _remove_stationary_points(points, labels, min_eps)
def remove_stationary_points(points, labels, min_eps, iters)
def keep_longest_true_segment(arr)
def load_eeff_in_aruco_frame(demonstration_dir)
def load_eeff_in_first_frame(demonstration_dir)
def plot_scalar_boxplots(data1, data2, save_path, labels)
def plot_consecutive_distances_with_bools(points_and_bools, save_path, anchors, reference_points)
class Random3DAugmentation()
    def __init__(self, std, mean, lower, upper)
    def __repr__(self)
    def _sample(self, size)
    def __call__(self, states_and_actions)
class RandomTranslation(Random3DAugmentation)
    """Applies a fixed 3D translation to all input keypoints"""
    def __call__(self, states_and_actions)
class RandomRotation(Random3DAugmentation)
    """Applies a fixed 3D rotation to all input keypoints wrt states centroid"""
    def __call__(self, states_and_actions)
def get_relative_action(actions, action_after_steps)
class BCDataset(IterableDataset)
    def __init__(self, path, pixel_keys, history, history_len, num_queries, temporal_agg, action_type, subsample, num_demos_per_task, random_translation_std, random_translation_mean, random_translation_lower, random_translation_upper, random_rotation_std, random_rotation_mean, random_rotation_lower, random_rotation_upper, point_aug_prob, history_aug_prob)
    def _sample(self)
    def __iter__(self)
    def __len__(self)
```

### point_policy/read_data/baku.py

```
def get_relative_action(actions, action_after_steps)
def get_quaternion_orientation(cartesian)
class BCDataset(IterableDataset)
    def __init__(self, path, tasks, num_demos_per_task, history, history_len, temporal_agg, num_queries, img_size, action_after_steps, pixel_keys, subsample, skip_first_n, action_type, gt_depth)
    def _sample_episode(self, env_idx)
    def _sample(self)
    def sample_actions(self, env_idx)
    def __iter__(self)
    def __len__(self)
```

### point_policy/read_data/mtpi.py

```
def get_relative_action(actions, action_after_steps)
class BCDataset(IterableDataset)
    def __init__(self, path, tasks, num_demos_per_task, history, history_len, temporal_agg, num_queries, img_size, action_after_steps, use_robot_points, num_robot_points, use_object_points, num_object_points, point_dim, pixel_keys, subsample, skip_first_n)
    def _sample_episode(self, env_idx)
    def _sample(self)
    def sample_actions(self, env_idx)
    def __iter__(self)
    def __len__(self)
```

### point_policy/read_data/p3po.py

```
def get_relative_action(actions, action_after_steps)
class BCDataset(IterableDataset)
    def __init__(self, path, tasks, num_demos_per_task, history, history_len, temporal_agg, num_queries, img_size, action_after_steps, use_robot_points, num_robot_points, use_object_points, num_object_points, point_dim, pixel_keys, action_type, subsample, skip_first_n, gt_depth)
    def _sample_episode(self, env_idx)
    def _sample(self)
    def sample_actions(self, env_idx)
    def __iter__(self)
    def __len__(self)
```

### point_policy/read_data/point_policy.py

```
class BCDataset(IterableDataset)
    def __init__(self, path, tasks, num_demos_per_task, history, history_len, temporal_agg, num_queries, img_size, action_after_steps, use_robot_points, num_robot_points, use_object_points, num_object_points, point_dim, pixel_keys, subsample, skip_first_n, gt_depth)
    def _sample_episode(self, env_idx)
    def _sample(self)
    def sample_actions(self, env_idx)
    def __iter__(self)
    def __len__(self)
```

### point_policy/replay_buffer.py

```
def _worker_init_fn(worker_id)
def make_expert_replay_loader(iterable, batch_size)
```

### point_policy/robot_utils/franka/calibration/generate_r2c_extrinsic.py

```
"""A script which given camera intrinsics computes te robot to camera transformation
for each camera and uses that as extrinsics to save in a calib.pkl file"""
```

### point_policy/robot_utils/franka/convert_pkl_human_to_robot.py

```
def resize_depth_image(depth_image, new_size)
```

### point_policy/robot_utils/franka/convert_to_pkl_human.py

```
def extract_number(s)
```

### point_policy/robot_utils/franka/convert_to_pkl_robot.py

```
def extract_number(s)
```

### point_policy/robot_utils/franka/utils.py

```
def pixel2d_to_3d_torch(points2d, depths, intrinsic_matrix, extrinsic_matrix)
def pixel2d_to_3d(points2d, depths, intrinsic_matrix, extrinsic_matrix)
def pixel3d_to_2d(points3d, intrinsic_matrix, camera_projection_matrix)
def triangulate_points(P, points)
def rigid_transform_3D(A, B)
def rotation_6d_to_matrix(d6)
def matrix_to_rotation_6d(matrix)
```

### point_policy/suite/baku.py

```
class RGBArrayAsObservationWrapper(Environment)
    """Use env.render(rgb_array) as observation
rather than the observation environment provides

From: https://github.com/hill-a/stable-baselines/issues/915"""
    def __init__(self, env, max_episode_len, max_state_dim, pixel_keys, use_robot, action_type, use_gt_depth)
    def reset(self)
    def get_state(self)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def render(self, mode, cam_idx, width, height)
    def __getattr__(self, name)
class ActionRepeatWrapper(Environment)
    def __init__(self, env, num_repeats)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class FrameStackWrapper(Environment)
    def __init__(self, env, num_frames)
    def _transform_observation(self, time_step)
    def _extract_pixels(self, time_step)
    def reset(self)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
class ActionDTypeWrapper(Environment)
    def __init__(self, env, dtype)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ExtendedTimeStep(NamedTuple)
    def first(self)
    def mid(self)
    def last(self)
    def __getitem__(self, attr)
class ExtendedTimeStepWrapper(Environment)
    def __init__(self, env)
    def reset(self)
    def step(self, action)
    def _augment_time_step(self, time_step, action)
    def _replace(self, time_step, observation, action, reward, discount)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
def make(action_repeat, seed, height, width, max_episode_len, max_state_dim, pixel_keys, eval, action_type, use_gt_depth)

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def _transform_observation(self, time_step):
        for key in self.pixel_keys:
            assert len(self._frames[key]) == self._num_frames
        obs = {}
        obs["features"] = time_step.observation["features"]
        for key in self.pixel_keys:
            obs[key] = np.concatenate(list(self._frames[key]), axis=0)
        obs["proprioceptive"] = time_step.observation["proprioceptive"]
        obs["goal_achieved"] = time_step.observation["goal_achieved"]
        return time_step._replace(observation=obs)
```

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```
```

### point_policy/suite/mtpi.py

```
class RGBArrayAsObservationWrapper(Environment)
    """Use env.render(rgb_array) as observation
rather than the observation environment provides

From: https://github.com/hill-a/stable-baselines/issues/915"""
    def __init__(self, env, task_name, object_labels, calib_path, width, height, calib_height, calib_width, use_robot, max_episode_len, max_state_dim, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, points_cfg)
    def reset(self)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def render(self, mode, width, height)
    def get_pixel_on_robot(self)
    def init_track_points(self, obs)
    def point2action(self, action)
    def compute_action_from_3dpoints(self, points3d)
    def compute_gripper(self, action)
    def compute_robot_action(self, target_position, target_orientation, gripper)
    def __getattr__(self, name)
class ActionRepeatWrapper(Environment)
    def __init__(self, env, num_repeats)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class FrameStackWrapper(Environment)
    def __init__(self, env, num_frames, pixel_keys)
    def _transform_observation(self, time_step)
    def _extract_pixels(self, time_step, key)
    def reset(self)
    def step(self, action)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
class ActionDTypeWrapper(Environment)
    def __init__(self, env, dtype)
    def step(self, action)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ExtendedTimeStep(NamedTuple)
    def first(self)
    def mid(self)
    def last(self)
    def __getitem__(self, attr)
class ExtendedTimeStepWrapper(Environment)
    def __init__(self, env)
    def reset(self)
    def step(self, action)
    def _augment_time_step(self, time_step, action)
    def _replace(self, time_step, observation, action, reward, discount)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
def make(task_name, object_labels, action_repeat, height, width, calib_height, calib_width, max_episode_len, max_state_dim, calib_path, eval, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, points_cfg)

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def _transform_observation(self, time_step):
        obs = {}
        for key in self._pixel_keys:
            assert len(self._frames[key]) == self._num_frames
            assert len(self._track_pts[key]) == self._num_frames
            obs[key] = np.concatenate(list(self._frames[key]), axis=0)
            obs[f"point_tracks_{key}"] = np.concatenate(
                list(self._track_pts[key]), axis=0
            )
        obs["features"] = time_step.observation["features"]
        obs["proprioceptive"] = time_step.observation["proprioceptive"]
        obs["goal_achieved"] = time_step.observation["goal_achieved"]
        return time_step._replace(observation=obs)
```

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```
```

### point_policy/suite/p3po.py

```
class RGBArrayAsObservationWrapper(Environment)
    """Use env.render(rgb_array) as observation
rather than the observation environment provides

From: https://github.com/hill-a/stable-baselines/issues/915"""
    def __init__(self, env, task_name, object_labels, root_dir, calib_path, width, height, use_robot, max_episode_len, max_state_dim, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, action_type, points_cfg, use_gt_depth, point_dim, prompts)
    def reset(self)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def render(self, mode, cam_idx, width, height)
    def get_pixel_on_robot(self)
    def init_track_points(self, obs, robot_points, robot_points_3d)
    def __getattr__(self, name)
class ActionRepeatWrapper(Environment)
    def __init__(self, env, num_repeats)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ActionDTypeWrapper(Environment)
    def __init__(self, env, dtype)
    def step(self, action)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ExtendedTimeStep(NamedTuple)
    def first(self)
    def mid(self)
    def last(self)
    def __getitem__(self, attr)
class ExtendedTimeStepWrapper(Environment)
    def __init__(self, env)
    def reset(self)
    def step(self, action)
    def _augment_time_step(self, time_step, action)
    def _replace(self, time_step, observation, action, reward, discount)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
def make(task_name, object_labels, root_dir, action_repeat, height, width, max_episode_len, max_state_dim, calib_path, eval, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, action_type, points_cfg, use_gt_depth, point_dim, prompts)

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```
```

### point_policy/suite/point_policy.py

```
class RGBArrayAsObservationWrapper(Environment)
    """Use env.render(rgb_array) as observation
rather than the observation environment provides

From: https://github.com/hill-a/stable-baselines/issues/915"""
    def __init__(self, env, task_name, object_labels, calib_path, width, height, use_robot, max_episode_len, max_state_dim, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, points_cfg, use_gt_depth, point_dim)
    def reset(self)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def render(self, mode, width, height)
    def get_pixel_on_robot(self)
    def init_track_points(self, obs, robot_points, robot_points_3d)
    def point2action(self, action)
    def compute_action_from_3dpoints(self, points3d)
    def compute_gripper(self, action)
    def compute_robot_action(self, target_position, target_orientation, gripper)
    def __getattr__(self, name)
class ActionRepeatWrapper(Environment)
    def __init__(self, env, num_repeats)
    def step(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ActionDTypeWrapper(Environment)
    def __init__(self, env, dtype)
    def step(self, action)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ExtendedTimeStep(NamedTuple)
    def first(self)
    def mid(self)
    def last(self)
    def __getitem__(self, attr)
class ExtendedTimeStepWrapper(Environment)
    def __init__(self, env)
    def reset(self)
    def step(self, action)
    def _augment_time_step(self, time_step, action)
    def _replace(self, time_step, observation, action, reward, discount)
    def point2action(self, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
def make(task_name, object_labels, action_repeat, height, width, max_episode_len, max_state_dim, calib_path, eval, pixel_keys, use_robot_points, num_robot_points, use_object_points, num_object_points, points_cfg, use_gt_depth, point_dim)

```python
def observation_spec(self):
        return self._obs_spec
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```

```python
def observation_spec(self):
        return self._env.observation_spec()
```
```

### point_policy/train.py

```
def make_agent(obs_spec, action_spec, cfg)
class WorkspaceIL()
    def __init__(self, cfg)
    def global_step(self)
    def global_episode(self)
    def global_frame(self)
    def eval(self)
    def train(self)
    def save_snapshot(self)
    def load_snapshot(self, snapshots)
def main(cfg)
```

### point_policy/utils.py

```
class eval_mode()
    def __init__(self)
    def __enter__(self)
    def __exit__(self)
def set_seed_everywhere(seed)
def soft_update_params(net, target_net, tau)
def to_torch(xs, device)
def weight_init(m)
class Until()
    def __init__(self, until, action_repeat)
    def __call__(self, step)
class Every()
    def __init__(self, every, action_repeat)
    def __call__(self, step)
class Timer()
    def __init__(self)
    def reset(self)
    def eval(self)
    def total_time(self)
class TruncatedNormal(Normal)
    def __init__(self, loc, scale, low, high, eps)
    def _clamp(self, x)
    def sample(self, clip, sample_shape)
class Normal(Normal)
    def __init__(self, loc, scale, eps)
    def sample(self, clip, sample_shape)
def schedule(schdl, step)
class RandomShiftsAug(Module)
    def __init__(self, pad)
    def forward(self, x)
class TorchRunningMeanStd()
    def __init__(self, epsilon, shape, device)
    def update(self, x)
    def update_from_moments(self, batch_mean, batch_var, batch_count)
    def std(self)
def update_mean_var_count_from_moments(mean, var, count, batch_mean, batch_var, batch_count)
def batch_norm_to_group_norm(layer)
```

### point_policy/video.py

```
class VideoRecorder()
    def __init__(self, root_dir, render_size, fps)
    def init(self, env, enabled)
    def record(self, env)
    def save(self, file_name)
class TrainVideoRecorder()
    def __init__(self, root_dir, render_size, fps)
    def init(self, obs, enabled)
    def record(self, obs)
    def save(self, file_name)
```

### utils/hand_utils.py

```
def homogenize_mps_wrist_and_palm(wrist_and_palm_pose, T_camera_to_device, threshold)
def run_hamer_from_video(video, checkpoint, body_detector, render, is_right_hand)
def load_hamer_model(checkpoint, body_detector)
def detect_hamer_in_frame(model, model_cfg, detector, cpm, device, renderer, img_cv2, render, focal_length, rescale_factor, is_right_hand)
def load_wilor_model(checkpoint, cfg_path, detector_path)
def detect_wilor_in_frame(model, model_cfg, detector, device, renderer, img_cv2, render, focal_length, rescale_factor, is_right_hand)
def run_wilor_from_video(video, checkpoint, cfg_path, detector_path, render, is_right_hand)
def correct_hand_model_from_aria(fingerskeypoints, aria_poses)
def absolute_ori_from_robot_frame_fingertips(fingerkeypoints_robot_frame, robot_base_orientation)
def relative_ori_from_robot_frame_fingertips(fingerkeypoints_robot_frame, base_hand_points, robot_base_orientation)
```