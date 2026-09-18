# dexgraspvla_2025

source: https://github.com/Psi-Robot/DexGraspVLA


commit: 0144c7928817c5149ae836da2682291360828a21


## README

<h1 align="center"> DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping </h1>


### 📝 [Paper](https://arxiv.org/abs/2502.20900) | 🌍 [Project Page](https://dexgraspvla.github.io/) | 📺 [Video](https://www.youtube.com/watch?v=ucm3I2iHHaI)


![](./assets/teaser.jpg)


**DexGraspVLA** is a **hierarchical vision-language-action framework** that reaches a **90+\%** success rate in **dexterous grasping in cluttered scenes** under **thousands** of **unseen** object, lighting, and background combinations in a "**zero-shot**" real-world environment. It robustly handles **adversarial objects**, **human disturbance**, and **failure recovery**, and can complete **long-horizon grasping tasks** that require **complex vision-language reasoning**. The framework utilizes a pre-trained vision-language model as the high-level task planner and learns a diffusion-based policy as the low-level action controller. Its key insight lies in leveraging foundation models for strong generalization and using diffusion-based imitation learning for acquiring dexterous actions.



![](./assets/method.jpg)

# Environment Setup

First, please create and activate the conda environment:
```bash
conda create -n dexgraspvla python=3.9
conda activate dexgraspvla
git clone https://github.com/Psi-Robot/DexGraspVLA.git
cd DexGraspVLA
pip install -r requirements.txt
```

Then, please install [SAM](https://github.com/facebookresearch/segment-anything) and [Cutie](https://github.com/hkchengrex/Cutie) following the official instructions.

The CUDA version we use is 12.6.

# DexGraspVLA Controller

## Prepare Dataset

We provide a tiny [dataset](https://drive.google.com/file/d/1Z4QIibZwudz_qUazAGQAF7lAFAoRROnK/view?usp=drive_link) containing 51 human demonstration data samples, allowing users to understand the content and format of our data, as well as run the code to get a hands-on experience of the training process. 

First, create a `data` folder under the repo root:

```bash
[DexGraspVLA]$ mkdir data && cd data
```

Download the dataset and put it in the `data` folder. Then, decompress the dataset:

```bash
[data]$ tar -zxvf grasp_demo_example.tar.gz && rm -rf grasp_demo_example.tar.gz
```

After decompression, you'll find the dataset organized in [Zarr format](https://zarr.readthedocs.io/en/stable/) with the following groups:

### Dataset Structure

#### `data` Group
- **action**: $(K, 13)$ 
  - Contains action data of right robotic arm and hand at each timestep, represented by 13 degrees of freedom (DoFs).
- **right_state**: $(K, 13)$
  - Contains state data of the right robotic arm and hand at each timestep, represented by 13 DoFs.
- **rgbm**: $(K, H, W, 4)$
  - Third-view images from the head camera with 4 channels, where the first 3 channels are RGB and the 4th channel is a binary mask.
- **right_cam_img**: $(K, H, W, 3)$
  - First-view images from the wrist camera with 3 RGB channels.

#### `meta` Group
- **episode_ends**: $(J,)$
  - Marks the ending indices of each demonstration episode, used to segment different demonstration sequences.

Here, $K$ represents the total number of samples and $J$ denotes the number of demonstration episodes. 

## Launch Training

To train the DexGraspVLA controller on a single GPU, run

```
python train.py --config-name train_dexgraspvla_controller_workspace
```

To train the DexGraspVLA controller on 8 GPUs, first configure [accelerate](https://huggingface.co/docs/accelerate/index) with `accelerate config`, where we enable BF16 mixed precision training, and then run `./train.sh` or 

```
accelerate launch --num_processes=8 train.py --config-name train_dexgraspvla_controller_workspace
```

Users can also start from an existing checkpoint by specifying `policy.start_ckpt_path` in `controller/config/train_dexgraspvla_controller_workspace.yaml`. To support application and fine-tuning, we provide an open-source, high-performing model checkpoint ([dexgraspvla-controller-20250320](https://drive.google.com/file/d/1ge1FYD2wUqBnFewWzpsjQ5v6pEDBraOH/view?usp=sharing)), which has been deployed and evaluated across five zero-shot locations at the time of release, demonstrating strong generalization capabilities. Additionally, other training settings can also be customized by modifying the configuration files in the `controller/config` folder.

To help understand the internal model behaviors, we provide the functionality to generate, save, and visualize the attention maps of the controller. To enable this, please set `gen_attn_map` to `True` in the config file before training. During each sampling step, the attention maps will be saved as pickle files in the `train_sample_attn_maps` folder under the experiment directory. To visualize them, please run `python attention_map_visualizer.py --attn_maps_dir <path to train_sample_attn_maps>`. This will generate the images of attention maps under newly-created folders inside `train_sample_attn_maps` with the same names as the corresponding pickle files.



# DexGraspVLA Planner


We provide the code for the DexGraspVLA planner based on [Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) in the `planner` directory. Our interface currently supports calling the API or querying a deployed model on cloud servers.

```python
# Instantiate a planner that calls the API
planner = DexGraspVLAPlanner(
    api_key="your_api_key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model_name="qwen2.5-vl-72b-instruct"
)

# Instantiate a planner that queries a deployed model
planner = DexGraspVLAPlanner(
    base_url="your_deployed_model_url"
)
```

For deployment, we utilize an 8-A800 GPU server to host the Qwen2.5-VL-72B-Instruct model. The deployment is managed using vllm version 0.7.3, leveraging the Qwen2.5-VL-7B-Instruct model for speculative decoding. The deployment process utilizes four GPUs.

The following command is used to deploy the model:

```bash
python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8001 \
 --model <path to Qwen2.5-VL-72B-Instruct> --seed 42 -tp 1 \
 --speculative_model <path to Qwen2.5-VL-7B-Instruct> --num_speculative_tokens 5 \
 --gpu_memory_utilization 0.9 --tensor-parallel-size 4 --limit-mm-per-prompt "image=10"
```



# DexGraspVLA Inference

The hardware platform we use for dexterous grasping is shown in the following figure.

<div align="center"> <img src="./assets/hardware.jpg" width="400px" height="auto"/> </div>

Due to intellectual property constraints, we are unable to open-source the hardware-related code. However, we have released the rest of the code for reference, and below, we provide instructions on how to run DexGraspVLA on this platform.

## Installation

First, install the required dependencies:

```
pip install pymodbus==2.5.3 pyrealsense2==2.55.1.6486
```

## Configuration

### 1. Hardware Setup:
Configure the hardware settings in `inference_utils/config.yaml`.

### 2. Controller Checkpoint:
Specify the trained controller model checkpoint in `controller/config/train_dexgraspvla_controller_workspace.yaml`.
Alternatively, users can use our pre-trained checkpoint for quick deployment:
[dexgraspvla-controller-20250320](https://drive.google.com/file/d/1ge1FYD2wUqBnFewWzpsjQ5v6pEDBraOH/view?usp=sharing).

## Customizing the Inference Command
Modify `inference.sh` by adjusting the following arguments based on users' needs:

- `--manual`: Enables manual mode, allowing users to manually mark the bounding box, monitor the grasping process, and reset when necessary. If omitted, the full DexGraspVLA planner is used, leveraging a vision-language model (VLM) to plan and monitor the grasping trajectory autonomously.
- `--save_deployment_data`: Saves rollout data from the inference episodes, including raw data and recorded videos.
- `--gen_attn_map`: Generates and saves attention maps from the controller.

## Running the Inference
Once everything is set up, start the inference process with the following command:

```bash
./inference.sh
```

This command executes the configured grasping pipeline on the specified hardware platform.

During execution, detailed logs are generated and stored in the `logs` directory. These logs include:

- **Pipeline status** – real-time updates on the grasping process
- **Camera images** – captured frames from the execution
- **Planner prompts & responses** – inputs and outputs from the vision-language model (VLM)
- **Optional data** – attention maps and rollout data, if enabled



# Citation

If you find our project helpful, please consider citing it as

```bibtex
@misc{zhong2025dexgraspvla,
      title={DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping}, 
      author={Yifan Zhong and Xuchuan Huang and Ruochong Li and Ceyao Zhang and Zhang Chen and Tianrui Guan and Fanlian Zeng and Ka Num Lui and Yuyao Ye and Yitao Liang and Yaodong Yang and Yuanpei Chen},
      year={2025},
      eprint={2502.20900},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2502.20900}, 
}
```


# Acknowledgements

This codebase is based on [Diffusion Policy](https://github.com/real-stanford/diffusion_policy), [RDT](https://github.com/thu-ml/RoboticsDiffusionTransformer), [DiT](https://github.com/facebookresearch/DiT), and [pi_zero_pytorch](https://github.com/lucidrains/pi-zero-pytorch/).


## File tree (depth 3, assets pruned)

```
.gitignore
README.md
attention_map_visualizer.py
controller/
  common/
    checkpoint_util.py
    json_logger.py
    pytorch_util.py
    replay_buffer.py
    sampler.py
    streaming_replay_buffer.py
  config/
    task/
    train_dexgraspvla_controller_workspace.yaml
  dataset/
    base_dataset.py
    mask_image_dataset.py
  env_runner/
    base_image_runner.py
    real_grasp_image_runner.py
  model/
    common/
    diffusion/
    vision/
  policy/
    base_image_policy.py
    dexgraspvla_controller.py
  workspace/
    base_workspace.py
    train_dexgraspvla_controller_workspace.py
inference.py
inference.sh
inference_utils/
  config.yaml
  utils.py
planner/
  dexgraspvla_planner.py
  utils.py
requirements.txt
train.py
train.sh
```

## Config files (3)


### controller/config/task/grasp.yaml

```yaml
name: grasp

image_shape: [3, 518, 518]
mask_image_shape: [4, 518, 518]
dataset_paths:
 - data/grasp_demo_example

shape_meta: &shape_meta
  obs:
    right_cam_img:
      shape: ${task.image_shape}
      type: rgb
      horizon: ${n_obs_steps}
    rgbm:
      shape: ${task.mask_image_shape}
      type: rgbm
      horizon: ${n_obs_steps}
    right_state:
      shape: [13]
      type: low_dim
      horizon: ${n_obs_steps}
  action:
    shape: [13]
    horizon: ${n_action_steps}

env_runner:
  _target_: controller.env_runner.real_grasp_image_runner.RealGraspImageRunner

dataset:
  _target_: controller.dataset.mask_image_dataset.MaskImageDataset
  zarr_paths: ${task.dataset_paths}
  horizon: ${n_action_steps}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  seed: 42
  val_ratio: 0

```

### controller/config/train_dexgraspvla_controller_workspace.yaml

```yaml
defaults:
  - _self_
  - task: grasp


name: train_dexgraspvla_controller
_target_: controller.workspace.train_dexgraspvla_controller_workspace.TrainDexGraspVLAControllerWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

n_action_steps: 64
n_obs_steps: 1  # we currently do not support multi-step observation
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True

policy:
  _target_: controller.policy.dexgraspvla_controller.DexGraspVLAController

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.DDIMScheduler
    num_train_timesteps: 50
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  obs_encoder:
    _target_: controller.model.vision.obs_encoder.ObsEncoder
    shape_meta: ${shape_meta}
    model_config:
      head:
        model_type: dinov2_vitb14
        # local weights path, null for online loading
        local_weights_path: null
      wrist:
        model_type: dinov2_vitl14
        # local weights path, null for online loading
        local_weights_path: null

  num_inference_steps: 16
  n_layer: 12
  n_head: 8
  p_drop_attn: 0.1
  use_attn_mask: False
  start_ckpt_path: null

ema:
  _target_: controller.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 48
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 48
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: True

optimizer:
  lr: 1.0e-4
  weight_decay: 1e-4
  betas: [0.95, 0.999]
  
training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: False
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 2000
  num_epochs: 125
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: False
  # training loop control
  # in epochs
  rollout_every: 10
  checkpoint_every: 1
  val_every: 10000
  sample_every: 10
  gen_attn_map: True
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: train_dexgraspvla_controller
  resume: False
  mode: online
  name: ${now:%Y.%m.%d-%H.%M}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 1
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: False
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### inference_utils/config.yaml

```yaml
# Robot Configuration
robot:
  # DOF limits for robot arms
  dof_limits:
    lower: [-3.1, -2.268, -3.1, -2.355, -3.1, -2.233, -6.28]
    upper: [3.1, 2.268, 3.1, 2.355, 3.1, 2.233, 6.28]
  
  # Hand configuration
  hands:
    left:
      port: null
      default_open: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    right:
      port: null
      default_open: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

  # Arm configuration
  arms:
    left:
      ip: null
      init_qpos: [-0.10979866, -1.37397554, -1.11486395, -0.99602451, 0.28651326, -0.55909878, 0.59166664]
    right:
      ip: null
      init_qpos: [0.36939895, -1.42726047, 0.32529447, -0.78829542, -1.78686804, 0.85681702, 2.33696087]
      placement_joint: [0.95171058, -1.10870292, 0.30105185, -1.85312083, -2.63649433, 0.25455627, 2.43874849]
      return_medium_joint: [0.58597687, -0.72916365, 0.20774654, -1.24625233, -2.82404745, 1.29088039, 2.68651541]

# Camera Configuration
cameras:
  right_first:
    sn: null
    resolution: [640, 480]
  third:
    sn: null
    resolution: [640, 480]

# Model Configuration
sam:
  checkpoint: null
  model_type: "vit_h"

planner:
  api_key: "EMPTY"
  base_url: null
  model_name: null

# Logging Configuration
logging:
  exp_name: "demo"

# Control Parameters
control:
  arm_trajectory:
    interpolation_num: 20  # 轨迹插值点数
    position_error_threshold: 0.03  # 位置误差阈值
  monitor:
    max_episode_duration: 100  # 最大执行时间(秒)

# Visualization Configuration
visualization:
  bbox:
    color: [0.8, 0.2, 0.2]  # 边界框颜色 [R, G, B] 绿色
    linewidth: 2        # 边界框线宽
  mask:
    color: [0.1, 0.5, 1, 0.6]  # 掩码颜色 [R, G, B, Alpha] 蓝色半透明

```

## Python signatures and reward/observation bodies (7 files)


### controller/env_runner/base_image_runner.py

```
class BaseImageRunner()
    def __init__(self, output_dir)
    def run(self, policy)
```

### controller/env_runner/real_grasp_image_runner.py

```
class RealGraspImageRunner(BaseImageRunner)
    def __init__(self, output_dir)
    def run(self, policy)
```

### controller/model/diffusion/transformer_for_action_diffusion.py

```
class TimestepEmbedder(Module)
    """Embeds scalar timesteps into vector representations."""
    def __init__(self, hidden_size, frequency_embedding_size, dtype)
    def timestep_embedding(self, t, dim, max_period)
    def forward(self, t)
class CrossAttention(Module)
    """A cross-attention layer with flash attention,
to incorporate the conditional information into main sequence."""
    def __init__(self, dim, num_heads, qkv_bias, qk_norm, attn_drop, proj_drop, norm_layer, attn_mask_kwargs)
    def forward(self, x, c, training, gen_attn_map)
class RDTBlock(Module)
    def __init__(self, hidden_size, num_heads, attn_mask_kwargs)
    def forward(self, x, c, training, gen_attn_map)
class TransformerForActionDiffusion(ModuleAttrMixin)
    def __init__(self, input_dim, output_dim, action_horizon, n_layer, n_head, n_emb, max_cond_tokens, p_drop_attn, obs_part_length, use_attn_mask)
    def _init_weights(self, module)
    def forward(self, sample, timestep, cond, training, gen_attn_map)
```

### controller/policy/base_image_policy.py

```
class BaseImagePolicy(ModuleAttrMixin)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
```

### controller/policy/dexgraspvla_controller.py

```
def noise_assignment(data, noise)
class DexGraspVLAController(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, obs_encoder, num_inference_steps, n_layer, n_head, p_drop_attn, use_attn_mask, start_ckpt_path)
    def conditional_sample(self, cond, gen_attn_map)
    def predict_action(self, obs_dict, output_path)
    def set_normalizer(self, normalizer)
    def get_optimizer(self, lr, weight_decay, betas)
    def compute_loss(self, batch, training)
    def forward(self, batch, training)
```

### controller/workspace/train_dexgraspvla_controller_workspace.py

```
class TrainDexGraspVLAControllerWorkspace(BaseWorkspace)
    def __init__(self, cfg)
    def run(self)
def main(cfg)
```

### train.py

```
def main(cfg)
```