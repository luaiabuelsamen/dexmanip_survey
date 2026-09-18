# humanoid_policy_human_policy_2025

source: https://github.com/RogerQi/human-policy


commit: 2d9d73cc5a3859094ef705f35b8f2faecfc2bc4f


## README

<h1 align="center">Humanoid Policy ~ Human Policy</h1>

<p align="center">
    <img src="repo_assets/UCSanDiegoLogo-BlueGold.png" height=50"> &nbsp; &nbsp;
    <img src="repo_assets/cmu_ri_logo.png" height="50"> &nbsp; &nbsp;
    <img src="repo_assets/uw_logo.png" height="50"> &nbsp; &nbsp;
    <img src="repo_assets/mit-logo.png" height="50">
</p>

<p align="center">
<h3 align="center"><a href="https://human-as-robot.github.io/">Website</a> | <a href="https://arxiv.org/">arXiv</a> | <a href="https://huggingface.co/datasets/RogerQi/PH2D">Data</a> | <a href="https://docs.google.com/document/d/1Uv1rq5z7xdVqhdSUz7M4Yce71tjLqtkIqcCxfBlN5NI/edit?usp=sharing">Hardware</a>
  <div align="center"></div>
</p>

<p align="center">
<img src="./repo_assets/alpha_blending.webp" width="80%"/>
<img src="./repo_assets/dataset_viz.webp" width="80%"/>
</p>

## Introduction

This repository contains the codebase for the paper "Humanoid Policy ~ Human Policy".

It trains egocentric (i.e., without wrist camera) humanoid manipulation policies, with few wrappers to focus on the core components.

## Repo Structure

```
| - assets: robot URDFs and meshes
| - cet: Mujoco simulation for replaying/rollouting out policies for code development and adding new embodiments.
| - configs: configs for robots and simulation environments
| - data: placeholder for data with some visualization scripts
| - docs: documentations
| - hdt: main learning framework
| - human_data: script and interface for collecting human demonstration data
| - sim_test (legacy): legacy ALOHA cube transferring test as a dummy example for sanity check
```

## Supported Algorithms

- [x] ACT (with options to use ResNet, DinoV2, and CLIP backbones)
- [x] Vanilla DP (based on [official colab](https://colab.research.google.com/drive/18GIHeOQ5DyjMN8iIRZL2EKZ0745NLIpg?usp=sharing))
- [x] [RDT](https://github.com/thu-ml/RoboticsDiffusionTransformer) (Trainer works, but not tested)

## Setup dependency

Clone the codebase.

```bash
cd ~
git clone --recursive https://github.com/RogerQi/human-policy
```

Follow [INSTALL.md](./docs/INSTALL.md) to install required dependencies.

## Download open-sourced data

We open-source recordings on [HuggingFace](https://huggingface.co/datasets/RogerQi/PH2D):

- Many humans performing tasks described in the paper in diverse in-the-wild scenes.
- Two Unitree H1 humanoid robots physically located in UCSD and CMU. Collected via teleoperation.
- One Unitree H1 humanoid robot in Mujoco. Collected via teleoperation.

To download the data, run

```bash
cd data/recordings
bash download_data.sh
```

## Visualize downloaded data

We provide scripts to examine the actions and visual observations in downloaded data.

```bash
cd data/
# You can take a look at the argparse inside the script to change data path for visualization
python plot_keypoints.py
python plot_visual_obs.py
```

## Converting your own data to our human-centric representation format

Human data is a scalable source for manipulation policy learning and we believe humanoid policies should
make good use of it. To process your own human/humanoid data to our format, please refer to these files:

- [data/plot_keypoints.py](./data/plot_keypoints.py): 3D visualization of human-centric representations
- [docs/humanoid_mujoco.md](./docs/humanoid_mujoco.md): replay processed data in Mujoco to make sure representatiosn are well-aligned
- [hdt/constants.py](./hdt/constants.py): element-wise interpretation of human-centric representations in trainable formats

## Training

Let's take the toy humanoid manipulation data in Mujoco and simple ACT policy with ResNet as an example.
Other data/model options are available in [model configs](./hdt/configs/models/) and [dataset configs](./hdt/configs/datasets/).

To launch simple training on a single GPU (with at least 24GB VRAM), run

```bash
python main.py --chunk_size 100 --batch_size 64 --num_epochs 50000 --lr 1e-4 --seed 0 --exptid 'mujoco_sim_test_resnet_100cs' --dataset_json_path configs/datasets/mujoco_sim.json  --model_cfg_path configs/models/act_resnet.yaml --no_wandb
```

For more sophisticated training, such as BF16, torch.compile, or multi-GPU training, the training script supports huggingface accelerator.

Start by configuring a `config.yaml` file.

```bash
accelerate config --config_file ./accelerator_setup.yaml
```

Then

```bash
accelerate launch --config_file ./accelerator_setup.yaml  main.py --chunk_size 100 --batch_size 64 --num_epochs 50000 --lr 1e-4 --seed 0 --exptid 'mujoco_sim_test_resnet_100cs' --dataset_json_path configs/datasets/mujoco_sim.json  --model_cfg_path configs/models/act_resnet.yaml --no_wandb
```

For policies without complex architectures, such as ACT, we recommend using the `val_and_jit_trace` option to create traced models.

```bash
accelerate launch --config_file ./accelerator_setup.yaml  main.py --chunk_size 100 --batch_size 64 --num_epochs 50000 --lr 1e-4 --seed 0 --exptid 'mujoco_sim_test_resnet_100cs' --dataset_json_path configs/datasets/mujoco_sim.json  --model_cfg_path configs/models/act_resnet.yaml --no_wandb --val_and_jit_trace
```

By default, the main trainer uses `accelerator.load_state` to resume model/optimizer states from the latest checkpoint specified in `(exptid)`.
The `val_and_jit_trace` flag then skips the training loop, and uses data format in the training data loader to create a traced model in `(exptid)/policy_traced.pt`.

## (Virtual) Policy Rollout

Continuing from the previous example, after the policy is trained and traced, we can rollout the policy in Mujoco/real robot.
The needed components are the dataset statistics and the traced policy weights. We include an example command below, for complete
details please refer to [docs/humanoid_mujoco.md](./docs/humanoid_mujoco.md).

```bash
cd ../cet
python mujoco_rollout_replay.py  --hdf_file_path ../data/recordings/processed/1061new_sim_pepsi_grasp_h1_2_inspire-2025_02_11-22_20_48/processed_episode_0.hdf5 --norm_stats_path ../hdt/mujoco_sim_test_resnet_100cs/dataset_stats.pkl  --plot --model_path ../hdt/mujoco_sim_test_resnet_100cs/policy_traced.pt  --tasktype pepsi --chunk_size 100 --policy_config_path ../hdt/configs/models/act_resnet.yaml
```

## Human Data Collection Guide

After setting up the **ZED camera mount** following our [hardware documentation](https://docs.google.com/document/d/1Uv1rq5z7xdVqhdSUz7M4Yce71tjLqtkIqcCxfBlN5NI/edit?usp=sharing), you can start collecting human data.

### Step 1: Install Dependencies

First, initialize and update the [opentv](https://robot-tv.github.io/) submodule:

```bash
git submodule update --init --recursive
```

Then follow the [README](./human_data/opentv/README.md) to complete the environment setup.

---

### Step 2: Collect Human Data

Run the following command to start the data collection process:

```bash
cd ./human_data
python human_data.py --des task_name --description "description of the task"
```

- `--des`: A short name for the task (e.g., `pouring`, `cutting`)
- `--description`: A more detailed description of the task

---

### Gesture-Based Control

We use simple hand gestures to control the data collection flow:

<p align="center">
  <img src="./repo_assets/gesture.png" width="60%"/>
</p>

- **Record Gesture**: Start and stop recording a demonstration.
- **Drop Gesture**: Cancel the current recording.

---

### Recording Pipeline

The following diagram shows the internal state transitions during the data collection process:

<p align="center">
  <img src="./repo_assets/pipeline.png" width="80%"/>
</p>

1. Use the **Record Gesture** to enter and exit the `RECORDING` state.
2. Use the **Drop Gesture** to cancel the current gesture and return to `WAITING`.

### Step 3: Post-process Human Data

Run the following command to start the data collection process:

```bash
cd ./cet
python post_process_zed.py --taskid task_name --multiprocess
```

---

## TODOs

- [ ] Add teleoperation scripts to collect more Mujoco data
- [ ] Alleviate the known 'sticky finger' friction issue in Mujoco sim rollout
- [ ] Add example for forward kinematrics / retargeting for a new humanoid


## File tree (depth 3, assets pruned)

```
.gitignore
.gitmodules
LICENSE
README.md
cet/
  __init__.py
  eval_6d.py
  mujoco_rollout_replay.py
  placeholder_text.txt
  post_process_zed.py
  sim_mujoco.py
  utils.py
  utils_fk.py
configs/
  all_tasks.yml
  h1_inspire_sim.yml
hdt/
  .gitignore
  1_gpu.yaml
  __init__.py
  configs/
    models/
  constants.py
  data_utils_hdt.py
  detr/
    LICENSE
    README.md
    main.py
    models/
    setup.py
    util/
  empty_lang_embed.pt
  inference_utils.py
  main.py
  modeling/
    modeling_hdt.py
    modeling_siglip.py
    modeling_t5.py
    modeling_vanilla_dp.py
    rdt_blocks.py
    rdt_trunk.py
    utils.py
  policy.py
human_data/
  human_data.py
  opentv/
repo_assets/
  UCSanDiegoLogo-BlueGold.png
  alpha_blending.webp
  cmu_ri_logo.png
  dataset_viz.webp
  gesture.png
  mit-logo.png
  pipeline.png
  uw_logo.png
requirements.txt
setup.py
sim_test/
  README.md
  eval_sim.py
  sim_env.py
```

## Config files (11)


### configs/all_tasks.yml

```yaml
tasks:
  h1_inspire_sim:
    file: h1_inspire_sim.yml
    name: H1 7DoF + 6DoF Hand (Sim)
    img: h1_inspire.png

```

### configs/h1_inspire_sim.yml

```yaml
robot_cfg:
  name: h1_inspire_sim
  urdf_path: h1_inspire_sim/urdf/h1_inspire.urdf
  xml_path: h1_inspire_sim/
  mesh_path: h1_inspire_sim/meshes/

  robot_indices: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
  body_indices: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  left_arm_indices: [13, 14, 15, 16, 17, 18, 19]
  right_arm_indices: [32, 33, 34, 35, 36, 37, 38]
  left_hand_indices: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
  right_hand_indices: [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
  waist_index: 12

  arm_motor_indices: [13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39, 41, 43, 45, 47, 48]

  head_pos: [ 0.2, 0.0, 0.5 ]
  # head_pos: [ 0.0, 0.0, 0.0 ]
  left_wrist_name: L_hand_base_link
  right_wrist_name: R_hand_base_link

  body:
    in_lp_alpha: 0.9

  arm:
    dt: 0.016667

    scaling_factor: 1.0
    base_damping: 1e-2
    max_damping: 1e-2
    eps: 1e-2

    in_lp_alpha: 0.5
    out_lp_alpha: 0.5

  hand:
    left_hand:
      scaling_factor: [ 1.1, 1.1, 1.1, 1.1, 1.2, 1.0, 1.0 ]
      in_lp_alpha: 0.5
      out_lp_alpha: 0.5

      target_origin_link_names: [  "L_hand_base_link", "L_hand_base_link", "L_hand_base_link", "L_hand_base_link", "L_hand_base_link", "L_thumb_tip", "L_thumb_tip" ]
      target_task_link_names: [ "L_thumb_tip", "L_index_tip", "L_middle_tip", "L_ring_tip", "L_pinky_tip", "L_index_tip", "L_middle_tip" ]
      target_link_human_indices: [ [0, 0, 0, 0, 0, 4, 4], [4, 9, 14, 19, 24, 9, 14] ]
      dex_pilot: [None, None, None, None, None, ['<=', 0.03, 1e-4, 200], ['<=', 0.03, 1e-4, 200]]

      mimic:
        parent_joints: ["L_thumb_proximal_pitch_joint", "L_thumb_proximal_pitch_joint", "L_index_proximal_joint", "L_middle_proximal_joint", "L_ring_proximal_joint", "L_pinky_proximal_joint"]
        child_joints: ["L_thumb_intermediate_joint", "L_thumb_distal_joint", "L_index_intermediate_joint", "L_middle_intermediate_joint", "L_ring_intermediate_joint", "L_pinky_intermediate_joint"]
        mimic_factors: [1.6, 2.4, 1, 1, 1, 1]

    right_hand:
      scaling_factor: [ 1.1, 1.1, 1.1, 1.1, 1.2, 1.0, 1.0 ]
      in_lp_alpha: 0.5
      out_lp_alpha: 0.5

      target_origin_link_names: [ "R_hand_base_link", "R_hand_base_link", "R_hand_base_link", "R_hand_base_link", "R_hand_base_link", "R_thumb_tip", "R_thumb_tip"]
      target_task_link_names: [ "R_thumb_tip", "R_index_tip", "R_middle_tip", "R_ring_tip", "R_pinky_tip", "R_index_tip", "R_middle_tip" ]
      target_link_human_indices: [ [0, 0, 0, 0, 0, 4, 4], [4, 9, 14, 19, 24, 9, 14] ]
      dex_pilot: [None, None, None, None, None, ['<=', 0.015, 1e-4, 200], ['<=', 0.015, 1e-4, 200]]

      mimic:
        parent_joints: [ "R_thumb_proximal_pitch_joint", "R_thumb_proximal_pitch_joint", "R_index_proximal_joint", "R_middle_proximal_joint", "R_ring_proximal_joint", "R_pinky_proximal_joint" ]
        child_joints: [ "R_thumb_intermediate_joint", "R_thumb_distal_joint", "R_index_intermediate_joint", "R_middle_intermediate_joint", "R_ring_intermediate_joint", "R_pinky_intermediate_joint" ]
        mimic_factors: [ 1.6, 2.4, 1, 1, 1, 1 ]
```

### hdt/configs/models/act_resnet.yaml

```yaml
common:
  policy_class: ACT
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

model:
  enc_layers: 4
  dec_layers: 7
  nheads: 8
  hidden_dim: 512
  kl_weight: 10
  dim_feedforward: 3200
  lr_backbone: 1e-5
  backbone: resnet18
  image_feature_strategy: ACT_linear
  use_language_conditioning: False

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/hat_language_act_linear.yaml

```yaml
common:
  policy_class: ACT
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

model:
  enc_layers: 4
  dec_layers: 7
  nheads: 8
  hidden_dim: 512
  kl_weight: 10
  dim_feedforward: 3200
  lr_backbone: 0
  backbone: dinov2_vits14
  image_feature_strategy: ACT_linear
  use_language_conditioning: True

data:
  image_resolution_hw: [240, 320]
```

### hdt/configs/models/hat_linear.yaml

```yaml
common:
  policy_class: ACT
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

model:
  enc_layers: 4
  dec_layers: 7
  nheads: 8
  hidden_dim: 512
  kl_weight: 10
  dim_feedforward: 3200
  lr_backbone: 0
  backbone: dinov2_vits14
  image_feature_strategy: linear
  use_language_conditioning: False

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/hat_linear4.yaml

```yaml
common:
  policy_class: ACT
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

model:
  enc_layers: 4
  dec_layers: 7
  nheads: 8
  hidden_dim: 512
  kl_weight: 10
  dim_feedforward: 3200
  lr_backbone: 0
  backbone: dinov2_vits14
  image_feature_strategy: linear4
  use_language_conditioning: False

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/opentv_act.yaml

```yaml
common:
  policy_class: ACT
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

model:
  enc_layers: 4
  dec_layers: 7
  nheads: 8
  hidden_dim: 512
  kl_weight: 10
  dim_feedforward: 3200
  lr_backbone: 0
  backbone: dinov2_vits14
  image_feature_strategy: ACT_linear
  use_language_conditioning: False

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/rdt_base.yaml

```yaml
common:
  # The number of historical images
  img_history_size: 1
  # The number of future actions to predict
  action_chunk_size: 64
  # The number of cameras to be used in the model
  num_cameras: 2
  # Dimension for state/action, we use the same space for both state and action
  # This MUST be equal to configs/state_vec.py
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']
  policy_class: RDT


dataset:
  # We will extract the data from raw dataset
  # and store them in the disk buffer by producer
  # When training, we will read the data 
  # randomly from the buffer by consumer
  # The producer will replace the data which has been 
  # read by the consumer with new data

  # The path to the buffer (at least 400GB)
  buf_path: /data/rdt_buffer
  # The number of chunks in the buffer
  buf_num_chunks: 32
  # The number of samples (step rather than episode) in each chunk
  buf_chunk_size: 512

  # We will filter the episodes with length less than `epsd_len_thresh_low`
  epsd_len_thresh_low: 32
  # For those more than `epsd_len_thresh_high`,
  # we will randomly sample `epsd_len_thresh_high` steps each time we load the episode
  # to better balance the training datasets
  epsd_len_thresh_high: 2048
  # How to fit the image size
  image_aspect_ratio: pad
  # Maximum number of language tokens
  tokenizer_max_length: 1024

model:
  # Config for condition adpators
  backbone: SIGLIP
  lang_adaptor: mlp2x_gelu
  img_adaptor: mlp2x_gelu
  state_adaptor: mlp3x_gelu
  lang_token_dim: 4096
  img_token_dim: 1152
  # Dim of action or proprioception vector
  # A `state` refers to an action or a proprioception vector
  state_token_dim: 128
  # Config for RDT structure
  rdt:
    # 1B: num_head 32 hidden_size 2048
    hidden_size: 2048
    depth: 28
    num_heads: 32
    cond_pos_embed_type: multimodal 
  # For noise scheduler
  noise_scheduler:
    type: ddpm
    num_train_timesteps: 1000
    num_inference_timesteps: 5
    beta_schedule: squaredcos_cap_v2  # Critical choice
    prediction_type: sample
    clip_sample: False
  # For EMA (params averaging)
  # We do not use EMA currently
  ema:
    update_after_step: 0
    inv_gamma: 1.0
    power: 0.75
    min_value: 0.0
    max_value: 0.9999

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/rdt_small.yaml

```yaml
common:
  # The number of historical images
  img_history_size: 1
  # The number of future actions to predict
  action_chunk_size: 64
  # The number of cameras to be used in the model
  num_cameras: 2
  # Dimension for state/action, we use the same space for both state and action
  # This MUST be equal to configs/state_vec.py
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']
  policy_class: RDT

dataset:
  # We will extract the data from raw dataset
  # and store them in the disk buffer by producer
  # When training, we will read the data 
  # randomly from the buffer by consumer
  # The producer will replace the data which has been 
  # read by the consumer with new data

  # The path to the buffer (at least 400GB)
  buf_path: /data/rdt_buffer
  # The number of chunks in the buffer
  buf_num_chunks: 32
  # The number of samples (step rather than episode) in each chunk
  buf_chunk_size: 512

  # We will filter the episodes with length less than `epsd_len_thresh_low`
  epsd_len_thresh_low: 32
  # For those more than `epsd_len_thresh_high`,
  # we will randomly sample `epsd_len_thresh_high` steps each time we load the episode
  # to better balance the training datasets
  epsd_len_thresh_high: 2048
  # How to fit the image size
  image_aspect_ratio: pad
  # Maximum number of language tokens
  tokenizer_max_length: 1024

model:
  # Config for condition adpators
  backbone: SIGLIP
  lang_adaptor: mlp2x_gelu
  img_adaptor: mlp2x_gelu
  state_adaptor: mlp3x_gelu
  lang_token_dim: 4096
  img_token_dim: 1152
  # Dim of action or proprioception vector
  # A `state` refers to an action or a proprioception vector
  state_token_dim: 128
  # Config for RDT structure
  rdt:
    # 1B: num_head 32 hidden_size 2048
    hidden_size: 1024
    depth: 14
    num_heads: 32
    cond_pos_embed_type: multimodal 
  # For noise scheduler
  noise_scheduler:
    type: ddpm
    num_train_timesteps: 1000
    num_inference_timesteps: 5
    beta_schedule: squaredcos_cap_v2  # Critical choice
    prediction_type: sample
    clip_sample: False
  # For EMA (params averaging)
  # We do not use EMA currently
  ema:
    update_after_step: 0
    inv_gamma: 1.0
    power: 0.75
    min_value: 0.0
    max_value: 0.9999

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/rdt_tiny.yaml

```yaml
common:
  # The number of historical images
  img_history_size: 1
  # The number of future actions to predict
  action_chunk_size: 64
  # The number of cameras to be used in the model
  num_cameras: 2
  # Dimension for state/action, we use the same space for both state and action
  # This MUST be equal to configs/state_vec.py
  state_dim: 128
  action_dim: 128
  policy_class: RDT
  camera_names: ['left', 'right']

dataset:
  # We will extract the data from raw dataset
  # and store them in the disk buffer by producer
  # When training, we will read the data 
  # randomly from the buffer by consumer
  # The producer will replace the data which has been 
  # read by the consumer with new data

  # The path to the buffer (at least 400GB)
  buf_path: /data/rdt_buffer
  # The number of chunks in the buffer
  buf_num_chunks: 32
  # The number of samples (step rather than episode) in each chunk
  buf_chunk_size: 512

  # We will filter the episodes with length less than `epsd_len_thresh_low`
  epsd_len_thresh_low: 32
  # For those more than `epsd_len_thresh_high`,
  # we will randomly sample `epsd_len_thresh_high` steps each time we load the episode
  # to better balance the training datasets
  epsd_len_thresh_high: 2048
  # How to fit the image size
  image_aspect_ratio: pad
  # Maximum number of language tokens
  tokenizer_max_length: 1024

model:
  # Config for condition adpators
  backbone: MASKCLIP
  lang_adaptor: mlp2x_gelu
  img_adaptor: mlp2x_gelu
  state_adaptor: mlp3x_gelu
  lang_token_dim: 4096
  img_token_dim: 512
  # Dim of action or proprioception vector
  # A `state` refers to an action or a proprioception vector
  state_token_dim: 128
  # Config for RDT structure
  rdt:
    # 1B: num_head 32 hidden_size 2048
    hidden_size: 512
    depth: 14
    num_heads: 32
    cond_pos_embed_type: multimodal 
  # For noise scheduler
  noise_scheduler:
    type: ddpm
    num_train_timesteps: 1000
    num_inference_timesteps: 5
    beta_schedule: squaredcos_cap_v2  # Critical choice
    prediction_type: sample
    clip_sample: False
  # For EMA (params averaging)
  # We do not use EMA currently
  ema:
    update_after_step: 0
    inv_gamma: 1.0
    power: 0.75
    min_value: 0.0
    max_value: 0.9999

data:
  image_resolution_hw: [240, 320]

```

### hdt/configs/models/vanilla_dp.yaml

```yaml
common:
  policy_class: DP
  state_dim: 128
  action_dim: 128
  camera_names: ['left', 'right']

data:
  image_resolution_hw: [240, 320]

```

## Python signatures and reward/observation bodies (4 files)


### cet/sim_mujoco.py

```
class MujocoSim()
    def __init__(self, config_files, root_path, print_freq, teleop_control, task_id, tasktype, path, shm_name, img_shape, is_viewer, control_dict, toggle_recording, crop_size_w, crop_size_h, cfgs)
    def _init_teleop(self, path, shm_name, img_shape, control_dict, toggle_recording)
    def _load_configs(self, config_files, cfgs)
    def _init_ui_params(self)
    def _init_mujoco(self, task_id)
    def create_envs(self)
    def _apply_pd_gains(self, cfg, robot_dof_props)
    def get_dof_properties(self)
    def setup_viewer(self, viewer)
    def sim_config(self)
    def all_sim_configs(self)
    def step(self, cmd, head_rmat, viewer)
    def step_init(self, action, viewer, init_state, init_qos)
    def generate_qpos(self, action, init_state, init_qos)
    def step_camera(self, head_rmat)
    def get_camera_image(self, cam_id)
    def set_torque_servo(self, actuator_indices, flag)
    def fetch_pos(self, body_name)
    def reset_env_randomize(self, record_obj_pose, randomize_lighting)
    def _tap_reset(self)
    def _randomize_lighting(self)
    def end(self)
```

### hdt/policy.py

```
class ACTPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, image, qpos, actions, is_pad, conditioning_dict)
    def configure_optimizers(self)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, image, qpos, actions, is_pad, conditioning_dict)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
```

### sim_test/eval_sim.py

```
def sample_box_pose()
def sample_insertion_pose()
def set_seed(seed)
def main(args)
def eval_bc(config, num_rollouts)
```

### sim_test/sim_env.py

```
def make_sim_env(task_name)
class BimanualViperXTask(Task)
    def __init__(self, random)
    def before_step(self, action, physics)
    def initialize_episode(self, physics)
    def get_qpos(physics)
    def get_qvel(physics)
    def get_env_state(physics)
    def get_observation(self, physics)
    def get_reward(self, physics)
class TransferCubeTask(BimanualViperXTask)
    def __init__(self, random)
    def initialize_episode(self, physics)
    def get_env_state(physics)
    def get_reward(self, physics)
class InsertionTask(BimanualViperXTask)
    def __init__(self, random)
    def initialize_episode(self, physics)
    def get_env_state(physics)
    def get_reward(self, physics)
def get_action(master_bot_left, master_bot_right)
def test_sim_teleop()

```python
def get_observation(self, physics):
        obs = collections.OrderedDict()
        obs['qpos'] = self.get_qpos(physics)
        obs['qvel'] = self.get_qvel(physics)
        obs['env_state'] = self.get_env_state(physics)
        obs['images'] = dict()
        obs['images']['top'] = physics.render(height=480, width=640, camera_id='top')
        obs['images']['left_wrist'] = physics.render(height=480, width=640, camera_id='left_wrist')
        obs['images']['right_wrist'] = physics.render(height=480, width=640, camera_id='right_wrist')
        # obs['images']['angle'] = physics.render(height=480, width=640, camera_id='angle')
        # obs['images']['vis'] = physics.render(height=480, width=640, camera_id='front_close')

        return obs
```

```python
def get_reward(self, physics):
        # return whether left gripper is holding the box
        raise NotImplementedError
```

```python
def get_reward(self, physics):
        # return whether left gripper is holding the box
        all_contact_pairs = []
        for i_contact in range(physics.data.ncon):
            id_geom_1 = physics.data.contact[i_contact].geom1
            id_geom_2 = physics.data.contact[i_contact].geom2
            name_geom_1 = physics.model.id2name(id_geom_1, 'geom')
            name_geom_2 = physics.model.id2name(id_geom_2, 'geom')
            contact_pair = (name_geom_1, name_geom_2)
            all_contact_pairs.append(contact_pair)

        touch_left_gripper = ("red_box", "vx300s_left/10_left_gripper_finger") in all_contact_pairs
        touch_right_gripper = ("red_box", "vx300s_right/10_right_gripper_finger") in all_contact_pairs
        touch_table = ("red_box", "table") in all_contact_pairs

        reward = 0
        if touch_right_gripper:
            reward = 1
        if touch_right_gripper and not touch_table: # lifted
            reward = 2
        if touch_left_gripper: # attempted transfer
            reward = 3
        if touch_left_gripper and not touch_table: # successful transfer
            reward = 4
        return reward
```

```python
def get_reward(self, physics):
        # return whether peg touches the pin
        all_contact_pairs = []
        for i_contact in range(physics.data.ncon):
            id_geom_1 = physics.data.contact[i_contact].geom1
            id_geom_2 = physics.data.contact[i_contact].geom2
            name_geom_1 = physics.model.id2name(id_geom_1, 'geom')
            name_geom_2 = physics.model.id2name(id_geom_2, 'geom')
            contact_pair = (name_geom_1, name_geom_2)
            all_contact_pairs.append(contact_pair)

        touch_right_gripper = ("red_peg", "vx300s_right/10_right_gripper_finger") in all_contact_pairs
        touch_left_gripper = ("socket-1", "vx300s_left/10_left_gripper_finger") in all_contact_pairs or \
                             ("socket-2", "vx300s_left/10_left_gripper_finger") in all_contact_pairs or \
                             ("socket-3", "vx300s_left/10_left_gripper_finger") in all_contact_pairs or \
                             ("socket-4", "vx300s_left/10_left_gripper_finger") in all_contact_pairs

        peg_touch_table = ("red_peg", "table") in all_contact_pairs
        socket_touch_table = ("socket-1", "table") in all_contact_pairs or \
                             ("socket-2", "table") in all_contact_pairs or \
                             ("socket-3", "table") in all_contact_pairs or \
                             ("socket-4", "table") in all_contact_pairs
        peg_touch_socket = ("red_peg", "socket-1") in all_contact_pairs or \
                           ("red_peg", "socket-2") in all_contact_pairs or \
                           ("red_peg", "socket-3") in all_contact_pairs or \
                           ("red_peg", "socket-4") in all_contact_pairs
        pin_touched = ("red_peg", "pin") in all_contact_pairs

        reward = 0
        if touch_left_gripper and touch_right_gripper: # touch both
            reward = 1
        if touch_left_gripper and touch_right_gripper and (not peg_touch_table) and (not socket_touch_table): # grasp both
            reward = 2
        if peg_touch_socket and (not peg_touch_table) and (not socket_touch_table): # peg and socket touching
            reward = 3
        if pin_touched: # successful insertion
            reward = 4
        return reward
```
```