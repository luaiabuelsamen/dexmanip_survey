# maniskill3_2024

source: https://github.com/haosulab/ManiSkill


commit: 62ff3a5896b4d5b4cf0ac4c8d79afe600c9404a3


## README

# ManiSkill 3


![teaser](figures/teaser.jpg)
<p style="text-align: center; font-size: 0.8rem; color: #999;margin-top: -1rem;">Sample of environments/robots rendered with ray-tracing. Scene datasets sourced from AI2THOR and ReplicaCAD</p>

[![Downloads](https://static.pepy.tech/badge/mani_skill)](https://pepy.tech/project/mani_skill)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mani-skill/ManiSkill/blob/main/examples/tutorials/1_quickstart.ipynb)
[![PyPI version](https://badge.fury.io/py/mani-skill.svg)](https://badge.fury.io/py/mani-skill)
[![Docs status](https://img.shields.io/badge/docs-passing-brightgreen.svg)](https://maniskill.readthedocs.io/en/latest/)
[![Discord](https://img.shields.io/discord/996566046414753822?logo=discord)](https://discord.gg/x8yUZe5AdN)

ManiSkill is an open-source framework for robot simulation and training powered by [SAPIEN](https://sapien.ucsd.edu/), with a strong focus on manipulation skills. Among its features include:
- GPU parallelized visual data collection system. On the high end you can collect RGBD + Segmentation data at 30,000+ FPS on a 4090 GPU
- GPU parallelized simulation, enabling high throughput state-based synthetic data collection in simulation
- GPU parallelized heterogeneous simulation, where every parallel environment has a completely different scene/set of objects
- Example tasks cover a wide range of different robot embodiments (humanoids, mobile manipulators, single-arm robots) as well as a wide range of different tasks (table-top, drawing/cleaning, dexterous manipulation)
- Flexible and simple task building API that abstracts away much of the complex GPU memory management code via an object oriented design
- Real2sim environments for scalably evaluating real-world policies 100x faster via GPU simulation.
- Sim2real examples for deploying policies trained in simulation to the real world
- Many tuned robot learning baselines in Reinforcement Learning (e.g. PPO, SAC, [TD-MPC2](https://github.com/nicklashansen/tdmpc2)), Imitation Learning (e.g. Behavior Cloning, [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)), and large Vision Language Action (VLA) models (e.g. [Octo](https://github.com/octo-models/octo), [RDT-1B](https://github.com/thu-ml/RoboticsDiffusionTransformer), [RT-x](https://robotics-transformer-x.github.io/))

For more details we encourage you to take a look at our [paper](https://arxiv.org/abs/2410.00425), published at [RSS 2025](https://roboticsconference.org/).

Please refer to our [documentation](https://maniskill.readthedocs.io/en/latest/user_guide) to learn more information from tutorials on building tasks to sim2real to running baselines. If you find any bugs or have any feature requests please post them to our [GitHub issues](https://github.com/mani-skill/ManiSkill/issues/) or discuss about them on [GitHub discussions](https://github.com/mani-skill/ManiSkill/discussions/). We also have a [Discord Server](https://discord.gg/x8yUZe5AdN) through which we make announcements and discuss about ManiSkill.

Users looking for the original ManiSkill2 can find the commit for that codebase at the [v0.5.3 tag](https://github.com/mani-skill/ManiSkill/tree/v0.5.3)

## Installation
Installation of ManiSkill is extremely simple, you only need to run a few pip installs and setup Vulkan for rendering.

```bash
# install the package
pip install --upgrade mani_skill
# install a version of torch that is compatible with your system
pip install torch
```

Finally you also need to set up Vulkan with [instructions here](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html#vulkan)

For more details about installation (e.g. from source, or doing troubleshooting) see [the documentation](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html
)

## Getting Started

To get started, check out the quick start documentation: https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html

We also have a quick start [colab notebook](https://colab.research.google.com/github/mani-skill/ManiSkill/blob/main/examples/tutorials/1_quickstart.ipynb) that lets you try out GPU parallelized simulation without needing your own hardware. Everything is runnable on Colab free tier.

For a full list of example scripts you can run, see [the docs](https://maniskill.readthedocs.io/en/latest/user_guide/demos/index.html).

## System Support

We currently best support Linux based systems. There is limited support for windows and MacOS at the moment. We are working on trying to support more features on other systems but this may take some time. Most constraints stem from what the [SAPIEN](https://github.com/haosulab/SAPIEN/) package is capable of supporting.

| System / GPU         | CPU Sim | GPU Sim | Rendering |
| -------------------- | ------- | ------- | --------- |
| Linux / NVIDIA GPU   | ✅      | ✅      | ✅        |
| Windows / NVIDIA GPU | ✅      | ❌      | ✅        |
| Windows / AMD GPU    | ✅      | ❌      | ✅        |
| WSL / Anything       | ✅      | ❌      | ❌        |
| MacOS / Anything     | ✅      | ❌      | ✅        |

## Citation


If you use ManiSkill3 (versions `mani_skill>=3.0.0`) in your work please cite our [ManiSkill3 paper](https://arxiv.org/abs/2410.00425) as so:

```
@article{taomaniskill3,
  title={ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI},
  author={Stone Tao and Fanbo Xiang and Arth Shukla and Yuzhe Qin and Xander Hinrichsen and Xiaodi Yuan and Chen Bao and Xinsong Lin and Yulin Liu and Tse-kai Chan and Yuan Gao and Xuanlin Li and Tongzhou Mu and Nan Xiao and Arnav Gurha and Viswesh Nagaswamy Rajesh and Yong Woo Choi and Yen-Ru Chen and Zhiao Huang and Roberto Calandra and Rui Chen and Shan Luo and Hao Su},
  journal = {Robotics: Science and Systems},
  year={2025},
} 
```

If you use ManiSkill2 (version `mani_skill==0.5.3` or lower) in your work please cite the ManiSkill2 paper as so:
```
@inproceedings{gu2023maniskill2,
  title={ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills},
  author={Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and Yuan, Xiaodi and Xie, Pengwei and Huang, Zhiao and Chen, Rui and Su, Hao},
  booktitle={International Conference on Learning Representations},
  year={2023}
}
```

Note that some other assets, algorithms, etc. in ManiSkill are from other sources/research. We try our best to include the correct citation bibtex where possible when introducing the different components provided by ManiSkill.

## License

All rigid body environments in ManiSkill are licensed under fully permissive licenses (e.g., Apache-2.0).

The assets are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    publish-nightly.yml
    publish-to-pypi.yml
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
CITATION.cff
CITATION_MS2.cff
CONTRIBUTING.md
LICENSE
LICENSE-3RD-PARTY
README.md
docker/
  10_nvidia.json
  Dockerfile
  nvidia_icd.json
  nvidia_layers.json
examples/
  baselines/
    README.md
    act/
    bc/
    diffusion_policy/
    experimental/
    ppo/
    rfcl/
    rlpd/
    sac/
    stable_baselines3/
    tdmpc2/
  tutorials/
    1_quickstart.ipynb
    README.md
figures/
  environment_demos/
    AnymalC-Reach-v1_rt.mp4
    AnymalC-Spin-v1_rt.mp4
    AssemblingKits-v1_rt.mp4
    DrawSVG-v1_rt.mp4
    DrawTriangle-v1_rt.mp4
    FMBAssembly1Easy.mp4
    LiftPegUpright-v1_rt.mp4
    MS-CartpoleBalance-v1_rt.mp4
    ManiSkill-HAB_rt.mp4
    OpenCabinetDrawer-v1_rt.mp4
    PegInsertionSide-v1_rt.mp4
    PickClutterYCB-v1_rt.mp4
    PickCube-v1_rt.mp4
    PickCubeSO100-v1_rt.mp4
    PickCubeWidowXAI-v1_rt.mp4
    PickSingleYCB-v1_rt.mp4
    PlaceSphere-v1_rt.mp4
    PlugCharger-v1_rt.mp4
    PokeCube-v1_rt.mp4
    PullCube-v1_rt.mp4
    PullCubeTool-v1_rt.mp4
    PushCube-v1_rt.mp4
    PushT-v1_rt.mp4
    RollBall-v1_rt.mp4
    RotateSingleObjectInHandLevel3-v1_rt.mp4
    RotateValveLevel1-v1_rt.mp4
    StackCube-v1_rt.mp4
    StackPyramid-v1_rt.mp4
    TableTopFreeDraw-v1_rt.mp4
    TwoRobotPickCube-v1_rt.mp4
    TwoRobotStackCube-v1_rt.mp4
    UnitreeG1PlaceAppleInBowl-v1_rt.mp4
    UnitreeG1TransportBox-v1_rt.mp4
    digital_twins/
    stack_cube.mp4
  teaser.jpg
mani_skill/
  __init__.py
  agents/
    README.md
    __init__.py
    base_agent.py
    base_real_agent.py
    controllers/
    multi_agent.py
    registration.py
    robots/
    utils.py
  envs/
    __init__.py
    minimal_template.py
    sapien_env.py
    scene.py
    scenes/
    sim2real_env.py
    tasks/
    template.py
    utils/
  examples/
    .gitignore
    __init__.py
    benchmarking/
    demo_manual_control.py
    demo_manual_control_continuous.py
    demo_random_action.py
    demo_reset_distribution.py
    demo_robot.py
    demo_vis_pcd.py
    demo_vis_segmentation.py
    demo_vis_textures.py
    motionplanning/
    teleoperation/
  render/
    __init__.py
    shaders.py
    utils.py
    version.py
  sensors/
    __init__.py
    base_sensor.py
    camera.py
    depth_camera.py
  shaders/
    postprocessing.comp
  trajectory/
    __init__.py
    convert_to_lerobot.py
    dataset.py
    merge_trajectory.py
    replay_trajectory.py
    utils/
  utils/
    README.md
    __init__.py
    building/
    common.py
    download_asset.py
    download_demo.py
    geometry/
    gym_utils.py
    io_utils.py
    logging_utils.py
    registration.py
    sapien_utils.py
    scene_builder/
    structs/
    tree.py
    visualization/
    wrappers/
  vector/
    __init__.py
    wrappers/
pyproject.toml
pyrightconfig.json
scripts/
  data_generation/
    README.md
    learning_from_demos.sh
    motionplanning.sh
    process_rl_trajectories.py
    replay_for_il_baselines.sh
    rl.sh
  mesh/
    generate_convex_mesh.py
setup.py
tests/
  __init__.py
  run.sh
  structs/
    test_actor.py
    test_link.py
    test_obs_mode_struct.py
    test_pose.py
  test_downloads.py
  test_envs.py
  test_examples.py
  test_gpu_envs.py
  test_ik_controller.py
  test_replay_trajectory.py
  test_sim_state.py
  test_venv.py
  test_wrapper_attribute_access.py
  test_wrappers.py
  utils.py
```

## Config files (7)


### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-ast
      - id: check-merge-conflict
      - id: check-toml
      # - id: check-yaml
      - id: end-of-file-fixer
        files: \.py$
      - id: trailing-whitespace
        files: \.py$
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        exclude: 'warp_maniskill/.*|docs/.*|examples/.*'
        args:
          - --line-length=88
  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        exclude: 'warp_maniskill/.*|docs/.*|examples/.*'
        args:
          - --profile=black
  - repo: https://github.com/myint/autoflake
    rev: v1.4
    hooks:
      - id: autoflake
        exclude: 'warp_maniskill/.*|docs/.*|examples/.*'
        args:
          - -r
          - --in-place
          - --remove-unused-variables
          # - --remove-all-unused-imports
```

### examples/baselines/rfcl/configs/base_sac_ms3.yml

```yaml
jax_env: False

seed: 0
algo: sac
verbose: 1
# Environment configuration
env:
  env_id: None
  max_episode_steps: 50
  num_envs: 8
  env_type: "gym:cpu"
  env_kwargs:
    control_mode: "pd_joint_delta_pos"
    render_mode: "rgb_array"
    reward_mode: "sparse"
eval_env:
  num_envs: 2
  max_episode_steps: 50

sac:
  num_seed_steps: 5_000
  seed_with_policy: False
  replay_buffer_capacity: 1_000_000
  batch_size: 256
  steps_per_env: 4
  grad_updates_per_step: 16
  actor_update_freq: 1

  num_qs: 2
  num_min_qs: 2

  discount: 0.9
  tau: 0.005
  backup_entropy: False

  eval_freq: 50_000
  eval_steps: 250

  log_freq: 1000
  save_freq: 50_000

  learnable_temp: True
  initial_temperature: 1.0
  
network:
  actor:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
  critic:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
      use_layer_norm: True

train:
  actor_lr: 3e-4
  critic_lr: 3e-4
  steps: 100_000_000
  dataset_path: None
  shuffle_demos: True
  num_demos: 1000

  data_action_scale: null

  ## Reverse curriculum configs
  reverse_step_size: 4
  start_step_sampler: "geometric"
  curriculum_method: "per_demo"
  per_demo_buffer_size: 3
  demo_horizon_to_max_steps_ratio: 3
  train_on_demo_actions: True

  load_actor: True
  load_critic: True
  load_as_offline_buffer: True
  load_as_online_buffer: False

  ## Forward curriculum configs
  forward_curriculum: "success_once_score"
  staleness_coef: 0.1
  staleness_temperature: 0.1
  staleness_transform: "rankmin"
  score_transform: "rankmin"
  score_temperature: 0.1
  num_seeds: 1000

logger:
  tensorboard: True
  wandb: False

  workspace: "exps"
  project_name: "ManiSkill"
  wandb_cfg:
    group: "RFCL"

```

### examples/baselines/rfcl/configs/base_sac_ms3_sample_efficient.yml

```yaml
jax_env: False

seed: 0
algo: sac
verbose: 1
# Environment configuration
env:
  env_id: None
  max_episode_steps: 50
  num_envs: 8
  env_type: "gym:cpu"
  env_kwargs:
    control_mode: "pd_joint_delta_pos"
    render_mode: "rgb_array"
    reward_mode: "sparse"
eval_env:
  num_envs: 2
  max_episode_steps: 50

sac:
  num_seed_steps: 5_000
  seed_with_policy: False
  replay_buffer_capacity: 1_000_000
  batch_size: 256
  steps_per_env: 1
  grad_updates_per_step: 80
  actor_update_freq: 20

  num_qs: 10
  num_min_qs: 2

  discount: 0.9
  tau: 0.005
  backup_entropy: False

  eval_freq: 5_000
  eval_steps: 500

  log_freq: 1000
  save_freq: 10_000

  learnable_temp: True
  initial_temperature: 1.0
  
network:
  actor:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
  critic:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
      use_layer_norm: True

train:
  actor_lr: 3e-4
  critic_lr: 3e-4
  steps: 100_000_000
  dataset_path: None
  shuffle_demos: True
  num_demos: 1000

  data_action_scale: null

  ## Reverse curriculum configs
  reverse_step_size: 4
  start_step_sampler: "geometric"
  curriculum_method: "per_demo"
  per_demo_buffer_size: 3
  demo_horizon_to_max_steps_ratio: 3
  train_on_demo_actions: True

  load_actor: True
  load_critic: True
  load_as_offline_buffer: True
  load_as_online_buffer: False

  ## Forward curriculum configs
  forward_curriculum: "success_once_score"
  staleness_coef: 0.1
  staleness_temperature: 0.1
  staleness_transform: "rankmin"
  score_transform: "rankmin"
  score_temperature: 0.1
  num_seeds: 1000

logger:
  tensorboard: True
  wandb: False

  workspace: "exps"
  project_name: "ManiSkill"
  wandb_cfg:
    group: "RFCL"

```

### examples/baselines/rlpd/configs/base_rlpd_ms3.yml

```yaml
jax_env: False

seed: 0
algo: sac
verbose: 1
# Environment configuration
env:
  env_id: None
  max_episode_steps: 50
  num_envs: 8
  env_type: "gym:cpu"
  env_kwargs:
    control_mode: "pd_joint_delta_pos"
    render_mode: "rgb_array"
    reward_mode: "sparse"
eval_env:
  num_envs: 2
  max_episode_steps: 50

sac:
  num_seed_steps: 5_000
  seed_with_policy: False
  replay_buffer_capacity: 1_000_000
  batch_size: 256
  steps_per_env: 4
  grad_updates_per_step: 16
  actor_update_freq: 1

  num_qs: 2
  num_min_qs: 2

  discount: 0.9
  tau: 0.005
  backup_entropy: False

  eval_freq: 50_000
  eval_steps: 250

  log_freq: 1000
  save_freq: 50_000

  learnable_temp: True
  initial_temperature: 1.0
  
network:
  actor:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
  critic:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
      use_layer_norm: True

train:
  actor_lr: 3e-4
  critic_lr: 3e-4
  steps: 100_000_000
  dataset_path: None
  shuffle_demos: True
  num_demos: 1000

  data_action_scale: null

logger:
  tensorboard: True
  wandb: False

  workspace: "exps"
  project_name: "ManiSkill"
  wandb_cfg:
    group: "RLPD"

```

### examples/baselines/rlpd/configs/base_rlpd_ms3_sample_efficient.yml

```yaml
jax_env: False

seed: 0
algo: sac
verbose: 1
# Environment configuration
env:
  env_id: None
  max_episode_steps: 50
  num_envs: 1
  env_type: "gym:cpu"
  env_kwargs:
    control_mode: "pd_joint_delta_pos"
    render_mode: "rgb_array"
    reward_mode: "sparse"
eval_env:
  num_envs: 2
  max_episode_steps: 50

sac:
  num_seed_steps: 5_000
  seed_with_policy: False
  replay_buffer_capacity: 1_000_000
  batch_size: 256
  steps_per_env: 1
  grad_updates_per_step: 16
  actor_update_freq: 1

  num_qs: 10
  num_min_qs: 2

  discount: 0.9
  tau: 0.005
  backup_entropy: False

  eval_freq: 5_000
  eval_steps: 250

  log_freq: 1000
  save_freq: 5_000

  learnable_temp: True
  initial_temperature: 1.0
  
network:
  actor:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
  critic:
    type: "mlp"
    arch_cfg:
      features: [256, 256, 256]
      output_activation: "relu"
      use_layer_norm: True

train:
  actor_lr: 3e-4
  critic_lr: 3e-4
  steps: 100_000_000
  dataset_path: None
  shuffle_demos: True
  num_demos: 1000

  data_action_scale: null

logger:
  tensorboard: True
  wandb: False

  workspace: "exps"
  project_name: "ManiSkill"
  wandb_cfg:
    group: "RLPD"

```

### examples/baselines/tdmpc2/config.yaml

```yaml
defaults:
    - override hydra/launcher: submitit_local

# environment
env_id: PushCube-v1
obs: state # or rgb
control_mode: default # or pd_joint_delta_pos or pd_ee_delta_pose
num_envs: 32
num_eval_envs: 4
env_type: gpu # cpu
include_state: true # for rgb mode, if we want to use extra state data like qpos, goal position, etc.
render_mode: rgb_array # ['rgb_array' for quality, or 'sensors' for speed]
render_size: 64
setting_tag: none # ['none', 'walltime_efficient', 'sample_efficient', ...] for wandb tags

# evaluation
checkpoint: ???
eval_episodes_per_env: 2 # total (eval_episodes_per_env * num_eval_envs number) of eval episodes
eval_freq: 50000
eval_reconfiguration_frequency: 1

# training
steps: 1_000_000
batch_size: 256
reward_coef: 0.1
value_coef: 0.1
consistency_coef: 20
rho: 0.5
lr: 3e-4
enc_lr_scale: 0.3
grad_clip_norm: 20
tau: 0.01
discount_denom: 5
discount_min: 0.95
discount_max: 0.995
buffer_size: 1_000_000
exp_name: default
data_dir: ???
steps_per_update: 1

# planning
mpc: true
iterations: 6
num_samples: 512
num_elites: 64
num_pi_trajs: 24
horizon: 3
min_std: 0.05
max_std: 2
temperature: 0.5

# actor
log_std_min: -10
log_std_max: 2
entropy_coef: 1e-4

# critic
num_bins: 101
vmin: -10
vmax: +10

# architecture
model_size: ???
num_enc_layers: 2
enc_dim: 256
rgb_state_enc_dim: 64
rgb_state_num_enc_layers: 1
rgb_state_latent_dim: 64
num_channels: 32
mlp_dim: 512
latent_dim: 512
task_dim: 0
num_q: 5
dropout: 0.01
simnorm_dim: 8

# logging
wandb_project:
wandb_group: 
wandb_name:
wandb_entity: 
wandb_silent: false
wandb: false # enable wandb
save_csv: true

# misc
save_video_local: false # save video in eval_video for evaluation during training
save_agent: true
seed: 1

# convenience
work_dir: ???
task_title: ???
multitask: ???
tasks: ???
obs_shape: ???
action_dim: ???
episode_length: ???
obs_shapes: ???
action_dims: ???
episode_lengths: ???
seed_steps: ???
bin_size: ???
true_latent_dim: ???

# Added for Maniskill RL Baselines Config Convention (don't assign to them)
env_cfg:
    env_id: ???
    control_mode: ??? # pd_joint_delta_pos or pd_ee_delta_pose
    obs_mode: ???
    reward_mode: ??? 
    num_envs: ???
    sim_backend: ??? # cpu or gpu
    partial_reset: false
    env_horizon: ???
eval_env_cfg:
    env_id: ???
    control_mode: ???
    obs_mode: ???
    reward_mode: ???
    num_envs: ???
    sim_backend: ???
    env_horizon: ???
    partial_reset: false
    num_eval_episodes: ???
discount: ???
```

### examples/baselines/tdmpc2/environment.yaml

```yaml
name: tdmpc2-ms
channels:
  - pytorch-nightly
  - nvidia
  - conda-forge
  - defaults
dependencies:
  - cudatoolkit=11.7
  - glew=2.1.0
  - glib=2.68.4
  - pip=21.0
  - python=3.9.0
  - pytorch>=2.2.2
  - torchvision>=0.16.2
  - pip:
    - absl-py==2.0.0
    - "cython<3"
    - dm-control==1.0.8
    - ffmpeg==1.4
    - glfw==2.6.4
    - hydra-core==1.3.2
    - hydra-submitit-launcher==1.2.0
    - imageio==2.33.1
    - imageio-ffmpeg==0.4.9
    - kornia==0.7.1
    - moviepy==1.0.3
    - mujoco==2.3.1
    - mujoco-py==2.1.2.14
    - numpy==1.23.5
    - omegaconf==2.3.0
    - open3d==0.18.0
    - opencv-contrib-python==4.9.0.80
    - opencv-python==4.9.0.80
    - pandas==2.1.4
    - sapien==3.0.0.b1
    - submitit==1.5.1
    - setuptools==65.5.0
    - patchelf==0.17.2.1
    - protobuf==4.25.2
    - pillow==10.2.0
    - pyquaternion==0.9.9
    - tensordict-nightly==2024.3.26
    - termcolor==2.4.0
    - torchrl-nightly==2024.3.26
    - transforms3d==0.4.1
    - trimesh==4.0.9
    - tqdm==4.66.1
    - wandb==0.16.2
    - wheel==0.38.0
    - mani_skill>=3.0.0b12
    ####################
    # Gym:
    # (unmaintained but required for maniskill2/meta-world/myosuite)
    # - gym==0.21.0
    ####################
    # ManiSkill2:
    # (requires gym==0.21.0 which occasionally breaks)
    # - mani-skill2==0.4.1
    ####################
    # Meta-World:
    # (requires gym==0.21.0 which occasionally breaks)
    # - git+https://github.com/Farama-Foundation/Metaworld.git@04be337a12305e393c0caf0cbf5ec7755c7c8feb
    ####################
    # MyoSuite:
    # (requires gym==0.13 which conflicts with meta-world / mani-skill2)
    # - myosuite
    ####################

```

## Python signatures and reward/observation bodies (133 files)


### examples/baselines/act/act/make_env.py

```
def make_eval_envs(env_id, num_envs, sim_backend, env_kwargs, other_kwargs, video_dir, wrappers)
```

### examples/baselines/act/train.py

```
class Args()
class SmallDemoDataset_ACTPolicy(Dataset)
    def __init__(self, data_path, num_queries, device, num_traj)
    def __getitem__(self, index)
    def __len__(self)
    def get_norm_stats(self)
class Agent(Module)
    def __init__(self, env, args)
    def compute_loss(self, obs, action_seq)
    def get_action(self, obs)
def kl_divergence(mu, logvar)
def save_ckpt(run_name, tag)
```

### examples/baselines/act/train_rgbd.py

```
class Args()
class FlattenRGBDObservationWrapper(ObservationWrapper)
    """Flattens the rgbd mode observations into a dictionary with two keys, "rgbd" and "state"

Args:
    rgb (bool): Whether to include rgb images in the observation
    depth (bool): Whether to include depth images in the observation
    state (bool): Whether to include state data in the observation

Not"""
    def __init__(self, env, rgb, depth, state)
    def observation(self, observation)
class SmallDemoDataset_ACTPolicy(Dataset)
    def __init__(self, data_path, num_queries, num_traj, include_depth)
    def __getitem__(self, index)
    def __len__(self)
    def process_obs(self, obs_dict)
    def get_norm_stats(self)
class Agent(Module)
    def __init__(self, env, args)
    def compute_loss(self, obs, action_seq)
    def get_action(self, obs)
def kl_divergence(mu, logvar)
def save_ckpt(run_name, tag)

```python
def observation(self, observation: Dict):
        sensor_data = observation.pop("sensor_data")
        del observation["sensor_param"]
        images_rgb = []
        images_depth = []
        for cam_data in sensor_data.values():
            if self.include_rgb:
                resized_rgb = self.transforms(
                    cam_data["rgb"].permute(0, 3, 1, 2)
                )  # (1, 3, 224, 224)
                images_rgb.append(resized_rgb)
            if self.include_depth:
                depth = (cam_data["depth"].to(torch.float32) / 1024).to(torch.float16)
                resized_depth = self.transforms(
                    depth.permute(0, 3, 1, 2)
                )  # (1, 1, 224, 224)
                images_depth.append(resized_depth)

        rgb = torch.stack(images_rgb, dim=1) # (1, num_cams, C, 224, 224), uint8
        if self.include_depth:
            depth = torch.stack(images_depth, dim=1) # (1, num_cams, C, 224, 224), float16

        # flatten the rest of the data which should just be state data
        observation = common.flatten_state_dict(observation, use_torch=True)
        ret = dict()
        if self.include_state:
            ret["state"] = observation
        if self.include_rgb and not self.include_depth:
            ret["rgb"] = rgb
        elif self.include_rgb and self.include_depth:
            ret["rgb"] = rgb
            ret["depth"] = depth
        elif self.include_depth and not self.include_rgb:
            ret["depth"] = depth
        return ret
```
```

### examples/baselines/bc/behavior_cloning/make_env.py

```
def make_eval_envs(env_id, num_envs, sim_backend, env_kwargs, video_dir, wrappers)
```

### examples/baselines/diffusion_policy/diffusion_policy/conditional_unet1d.py

```
"""Note: This is copied from the colab notebook.
The main difference with the github repo code is in `class ConditionalUnet1D` -- this version makes some simplifications."""
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
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups)
    def forward(self, sample, timestep, global_cond)
```

### examples/baselines/diffusion_policy/diffusion_policy/evaluate.py

```
def evaluate(n, agent, eval_envs, device, sim_backend, progress_bar)
```

### examples/baselines/diffusion_policy/diffusion_policy/make_env.py

```
def make_eval_envs(env_id, num_envs, sim_backend, env_kwargs, other_kwargs, video_dir, wrappers)
```

### examples/baselines/diffusion_policy/diffusion_policy/plain_conv.py

```
def make_mlp(in_channels, mlp_channels, act_builder, last_act)
class PlainConv(Module)
    def __init__(self, in_channels, out_dim, pool_feature_map, last_act)
    def reset_parameters(self)
    def forward(self, image)
```

### examples/baselines/diffusion_policy/diffusion_policy/utils.py

```
class IterationBasedBatchSampler(Sampler)
    """Wraps a BatchSampler.
Resampling from it until a specified number of iterations have been sampled
References:
    https://github.com/facebookresearch/maskrcnn-benchmark/blob/master/maskrcnn_benchmark/data/samplers/iteration_based_batch_sampler.py"""
    def __init__(self, batch_sampler, num_iterations, start_iter)
    def __iter__(self)
    def __len__(self)
def worker_init_fn(worker_id, base_seed)
def load_content_from_h5_file(file)
def load_hdf5(path)
def load_traj_hdf5(path, num_traj)
def load_demo_dataset(path, keys, num_traj, concat)
def convert_obs(obs, concat_fn, transpose_fn, state_obs_extractor, depth)
def build_obs_space(env, depth_dtype, state_obs_extractor)
def build_state_obs_extractor(env_id)
```

### examples/baselines/diffusion_policy/train.py

```
class Args()
class SmallDemoDataset_DiffusionPolicy(Dataset)
    def __init__(self, data_path, device, num_traj)
    def __getitem__(self, index)
    def __len__(self)
class Agent(Module)
    def __init__(self, env, args)
    def compute_loss(self, obs_seq, action_seq)
    def get_action(self, obs_seq)
def save_ckpt(run_name, tag)
```

### examples/baselines/diffusion_policy/train_rgbd.py

```
class Args()
def reorder_keys(d, ref_dict)
class SmallDemoDataset_DiffusionPolicy(Dataset)
    def __init__(self, data_path, obs_process_fn, obs_space, include_rgb, include_depth, device, num_traj)
    def __getitem__(self, index)
    def __len__(self)
class Agent(Module)
    def __init__(self, env, args)
    def encode_obs(self, obs_seq, eval_mode)
    def compute_loss(self, obs_seq, action_seq)
    def get_action(self, obs_seq)
def save_ckpt(run_name, tag)
```

### examples/baselines/rfcl/train.py

```
"""Code to run Reverse Forward Curriculum Learning.
Configs can be a bit complicated, we recommend directly looking at configs/ms2/base_sac_ms2_sample_efficient.yml for what options are available.
Alternatively, go to the file defining each of the nested configurations and see the comments."""
class TrainConfig()
class SACNetworkConfig()
class SACExperiment()
def main(cfg)
```

### examples/baselines/rlpd/train_ms3.py

```
"""Code to run Reverse Forward Curriculum Learning.
Configs can be a bit complicated, we recommend directly looking at configs/ms2/base_sac_ms2_sample_efficient.yml for what options are available.
Alternatively, go to the file defining each of the nested configurations and see the comments."""
class TrainConfig()
class SACNetworkConfig()
class SACExperiment()
def main(cfg)
```

### examples/baselines/tdmpc2/envs/__init__.py

```
def missing_dependencies(task)
def make_envs(cfg, num_envs, video_path, is_eval, logger)
```

### examples/baselines/tdmpc2/envs/maniskill.py

```
def cpu_env_factory(env_make_fn, idx, wrappers, record_video_path, record_episode_kwargs, logger)
def make_envs(cfg, num_envs, record_video_path, is_eval, logger)
```

### examples/baselines/tdmpc2/envs/wrappers/multitask.py

```
class MultitaskWrapper(Wrapper)
    """Wrapper for multi-task environments."""
    def __init__(self, cfg, envs)
    def task(self)
    def task_idx(self)
    def _env(self)
    def rand_act(self)
    def _pad_obs(self, obs)
    def reset(self, task_idx)
    def step(self, action)
```

### examples/baselines/tdmpc2/envs/wrappers/pixels.py

```
class PixelWrapper(ObservationWrapper)
    """Wrapper for pixel observations. Works with Maniskill vectorized environments"""
    def __init__(self, cfg, env, num_envs, num_frames)
    def observation(self, obs)
    def reset(self)
    def step(self, action)

```python
def observation(self, obs):
		self.rgb_stack[..., self._stack_idx] = obs['rgb']
		if self.include_state:
			self.state_stack[..., self._stack_idx] = obs['state']
		self._stack_idx = (self._stack_idx + 1) % self.num_frames
		rgb = self.rgb_stack.roll(shifts=-self._stack_idx, dims=-1).permute(0,1,2,4,3).reshape((*self.rgb_shape[:-1], -1)).permute(0, 3, 1, 2)		
		if self.include_state:
			state = self.state_stack.roll(shifts=-self._stack_idx, dims=-1).permute(0,2,1).reshape((*self.state_shape[:-1], -1))
			return {'rgb': rgb, 'rgb-state': state}
		else:
			return rgb
```
```

### examples/baselines/tdmpc2/envs/wrappers/record_episode.py

```
class RecordEpisodeWrapper(RecordEpisode)
    def __init__(self, env, output_dir, save_trajectory, trajectory_name, save_video, info_on_video, save_on_reset, save_video_trigger, max_steps_per_video, clean_on_close, record_reward, video_fps, source_type, source_desc, logger)
    def capture_image(self)
    def flush_video(self, name, suffix, verbose, ignore_empty_transition, save)
```

### examples/baselines/tdmpc2/envs/wrappers/tensor.py

```
class TensorWrapper(Wrapper)
    """Wrapper for converting numpy arrays to torch tensors."""
    def __init__(self, env)
    def rand_act(self)
    def _try_f32_tensor(self, x)
    def _obs_to_tensor(self, obs)
    def _info_to_tensor(self, info)
    def reset(self, task_idx)
    def step(self, action)
```

### examples/baselines/tdmpc2/envs/wrappers/time_limit.py

```
"""Wrapper for limiting the time steps of an environment.
Source: https://github.com/openai/gym/blob/3498617bf031538a808b75b932f4ed2c11896a3e/gym/wrappers/time_limit.py"""
class TimeLimit(Wrapper)
    """This wrapper will issue a `done` signal if a maximum number of timesteps is exceeded.

Oftentimes, it is **very** important to distinguish `done` signals that were produced by the
:class:`TimeLimit` wrapper (truncations) and those that originate from the underlying environment (terminations).
This c"""
    def __init__(self, env, max_episode_steps)
    def step(self, action)
    def reset(self)
```

### examples/baselines/tdmpc2/train.py

```
def train(cfg)
```

### examples/baselines/tdmpc2/trainer/base.py

```
class Trainer()
    """Base trainer class for TD-MPC2."""
    def __init__(self, cfg, env, eval_env, agent, buffer, logger)
    def eval(self)
    def train(self)
```

### examples/baselines/tdmpc2/trainer/offline_trainer.py

```
class OfflineTrainer(Trainer)
    """Trainer class for multi-task offline TD-MPC2 training. Not currently supported for Maniskill"""
    def __init__(self)
    def eval(self)
    def train(self)
```

### examples/baselines/tdmpc2/trainer/online_trainer.py

```
class OnlineTrainer(Trainer)
    """Trainer class for single-task online TD-MPC2 training."""
    def __init__(self)
    def final_info_metrics(self, info)
    def common_metrics(self)
    def eval(self)
    def to_td(self, obs, num_envs, action, reward)
    def train(self)
```

### mani_skill/agents/robots/allegro_hand/allegro.py

```
class AllegroHandRight(BaseAgent)
    def __init__(self)
    def _after_init(self)
    def _controller_configs(self)
    def get_proprioception(self)
    def tip_poses(self)
    def palm_pose(self)
class AllegroHandLeft(AllegroHandRight)
```

### mani_skill/agents/robots/allegro_hand/allegro_touch.py

```
class AllegroHandRightTouch(AllegroHandRight)
    def __init__(self)
    def _after_init(self)
    def get_fsr_obj_impulse(self, obj)
    def get_fsr_impulse(self)
    def get_proprioception(self)
```

### mani_skill/agents/robots/floating_ability_hand/floating_ability_hand.py

```
class FloatingAbilityHandRight(BaseAgent)
    def __init__(self)
    def _controller_configs(self)
    def _after_init(self)
```

### mani_skill/agents/robots/inspire_hand/fixed_inspire_hand.py

```
class FixedInspireHandRight(FloatingInspireHandRight)
    def _controller_configs(self)
class FixedInspireHandLeft(FloatingInspireHandLeft)
    def _controller_configs(self)
```

### mani_skill/agents/robots/inspire_hand/floating_inspire_hand.py

```
class FloatingInspireHandRight(BaseAgent)
    def _controller_configs(self)
class FloatingInspireHandLeft(BaseAgent)
    def _controller_configs(self)
```

### mani_skill/envs/minimal_template.py

```
class CustomEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        return torch.zeros(self.num_envs, device=self.device)
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        max_reward = 1.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/sapien_env.py

```
class BaseEnv(Env)
    """Superclass for ManiSkill environments.

Args:
    num_envs: number of parallel environments to run. By default this is 1, which means a CPU simulation is used. If greater than 1,
        then we initialize the GPU simulation setup. Note that not all environments are faster when simulated on the GPU """
    def __init__(self, num_envs, obs_mode, reward_mode, control_mode, render_mode, shader_dir, enable_shadow, sensor_configs, human_render_camera_configs, viewer_camera_configs, robot_uids, sim_config, reconfiguration_freq, sim_backend, render_backend, parallel_in_single_scene, enhanced_determinism)
    def update_obs_space(self, obs)
    def single_observation_space(self)
    def observation_space(self)
    def gpu_sim_enabled(self)
    def _default_sim_config(self)
    def _load_agent(self, options, initial_agent_poses, build_separate)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _default_viewer_camera_configs(self)
    def sim_freq(self)
    def control_freq(self)
    def sim_timestep(self)
    def control_timestep(self)
    def control_mode(self)
    def elapsed_steps(self)
    def obs_mode(self)
    def get_obs(self, info, unflattened)
    def _flatten_raw_obs(self, obs)
    def _get_obs_state_dict(self, info)
    def _get_obs_agent(self)
    def _get_obs_extra(self, info)
    def capture_sensor_data(self)
    def get_sensor_images(self)
    def get_sensor_params(self)
    def _get_obs_sensor_data(self, apply_texture_transforms)
    def _get_obs_with_sensor_data(self, info, apply_texture_transforms)
    def robot_link_names(self)
    def reward_mode(self)
    def get_reward(self, obs, action, info)
    def compute_sparse_reward(self, obs, action, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
    def _reconfigure(self, options)
    def _after_reconfigure(self, options)
    def _load_scene(self, options)
    def _setup_sensors(self, options)
    def _load_lighting(self, options)
    def reset(self, seed, options)
    def _set_main_rng(self, seed)
    def _set_episode_rng(self, seed, env_idx)
    def _initialize_episode(self, env_idx, options)
    def _clear_sim_state(self)
    def step(self, action)
    def _step_action(self, action)
    def evaluate(self)
    def get_info(self)
    def _before_control_step(self)
    def _after_control_step(self)
    def _before_simulation_step(self)
    def _after_simulation_step(self)
    def _set_scene_config(self)
    def _setup_scene(self)
    def _clear(self)
    def close(self)
    def _close_viewer(self)
    def segmentation_id_map(self)
    def add_to_state_dict_registry(self, object)
    def remove_from_state_dict_registry(self, object)
    def get_state_dict(self)
    def get_state(self)
    def set_state_dict(self, state, env_idx)
    def set_state(self, state, env_idx)
    def viewer(self)
    def _setup_viewer(self)
    def render_human(self)
    def render_rgb_array(self, camera_name)
    def render_sensors(self)
    def render_all(self)
    def render(self)
    def print_sim_details(self)

```python
def single_observation_space(self) -> gym.Space:
        """the unbatched observation space of the environment"""
        return gym_utils.convert_observation_to_space(common.to_numpy(self._init_raw_obs), unbatched=True)
```

```python
def observation_space(self) -> gym.Space:
        """the batched observation space of the environment"""
        return batch_space(self.single_observation_space, n=self.num_envs)
```

```python
def _get_obs_state_dict(self, info: dict):
        """Get (ground-truth) state-based observations."""
        return dict(
            agent=self._get_obs_agent(),
            extra=self._get_obs_extra(info),
        )
```

```python
def _get_obs_agent(self):
        """Get observations about the agent's state. By default it is proprioceptive observations which include qpos and qvel.
        Controller state is also included although most default controllers do not have any state."""
        return self.agent.get_proprioception()
```

```python
def _get_obs_extra(self, info: dict):
        """Get task-relevant extra observations. Usually defined on a task by task basis"""
        return dict()
```

```python
def _get_obs_sensor_data(self, apply_texture_transforms: bool = True) -> dict:
        """
        Get data from all registered sensors. Auto hides any objects that are designated to be hidden

        Args:
            apply_texture_transforms (bool): Whether to apply texture transforms to the simulated sensor data to map to standard texture formats. Default is True.

        Returns:
            dict: A dictionary containing the sensor data mapping sensor name to its respective dictionary of data. The dictionary maps texture names to the data. For example the return could look like

            .. code-block:: python

                {
                    "sensor_1": {
                        "rgb": torch.Tensor,
                        "depth": torch.Tensor
                    },
                    "sensor_2": {
                        "rgb": torch.Tensor,
                        "depth": torch.Tensor
                    }
                }
        """
        for obj in self._hidden_objects:
            obj.hide_visual()
        self.scene.update_render(update_sensors=True, update_human_render_cameras=False)
        self.capture_sensor_data()
        sensor_obs = dict()
        for name, sensor in self.scene.sensors.items():
            if isinstance(sensor, Camera):
                if self.obs_mode in ["state", "state_dict"]:
                    # normally in non visual observation modes we do not render sensor observations. But some users may want to render sensor data for debugging or various algorithms
                    sensor_obs[name] = sensor.get_obs(position=False, segmentation=False, apply_texture_transforms=apply_texture_transforms)
                else:
                    sensor_obs[name] = sensor.get_obs(
                        rgb=self.obs_mode_struct.visual.rgb,
                        depth=self.obs_mode_struct.visual.depth,
                        position=self.obs_mode_struct.visual.position,
                        segmentation=self.obs_mode_struct.visual.segmentation,
                        normal=self.obs_mode_struct.visual.normal,
                        albedo=self.obs_mode_struct.visual.albedo,
                        apply_texture_transforms=apply_texture_transforms
                    )
        # explicitly synchronize and wait for cuda kernels to finish
        # this prevents the GPU from making poor scheduling decisions when other physx code begins to run
        if self.backend.render_device.is_cuda():  # pyright: ignore[reportOptionalMemberAccess]
            torch.cuda.synchronize()
        return sensor_obs
```

```python
def _get_obs_with_sensor_data(self, info: dict, apply_texture_transforms: bool = True) -> dict:
        """Get the observation with sensor data"""
        return dict(
            agent=self._get_obs_agent(),
            extra=self._get_obs_extra(info),
            sensor_param=self.get_sensor_params(),
            sensor_data=self._get_obs_sensor_data(apply_texture_transforms),
        )
```

```python
def reward_mode(self):
        return self._reward_mode
```

```python
def get_reward(self, obs: Any, action: Any, info: dict):
        """
        Compute the reward for environment at its current state. observation data, the most recent action, and the info dictionary (generated by the self.evaluate() function)
        are provided as inputs. By default the observation data will be in its most raw form, a dictionary (no flattening, wrappers etc.)

        Args:
            obs (Any): The observation data.
            action (torch.Tensor): The most recent action.
            info (dict): The info dictionary.
        """
        if self._reward_mode == "sparse":
            reward = self.compute_sparse_reward(obs=obs, action=action, info=info)
        elif self._reward_mode == "dense":
            reward = self.compute_dense_reward(obs=obs, action=action, info=info)
        elif self._reward_mode == "normalized_dense":
            reward = self.compute_normalized_dense_reward(
                obs=obs, action=action, info=info
            )
        elif self._reward_mode == "none":
            reward = torch.zeros((self.num_envs, ), dtype=torch.float, device=self.device)
        else:
            raise NotImplementedError(self._reward_mode)
        return reward
```

```python
def compute_sparse_reward(self, obs: Any, action: torch.Tensor, info: dict):
        """

        Computes the sparse reward. By default this function tries to use the success/fail information in
        returned by the evaluate function and gives +1 if success, -1 if fail, 0 otherwise.

        Args:
            obs (Any): The observation data. By default the observation data will be in its most raw form, a dictionary (no flattening, wrappers etc.)
            action (torch.Tensor): The most recent action.
            info (dict): The info dictionary.
        """
        if "success" in info:
            if "fail" in info:
                if isinstance(info["success"], torch.Tensor):
                    reward = info["success"].to(torch.float) - info["fail"].to(torch.float)
                else:
                    reward = info["success"] - info["fail"]
            else:
                reward = info["success"]
        else:
            if "fail" in info:
                reward = -info["fail"]
            else:
                reward = torch.zeros(self.num_envs, dtype=torch.float, device=self.device)
        return reward
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        """
        Compute the dense reward.

        Args:
            obs (Any): The observation data. By default the observation data will be in its most raw form, a dictionary (no flattening, wrappers etc.)
            action (torch.Tensor): The most recent action.
            info (dict): The info dictionary.
        """
        raise NotImplementedError()
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        """
        Compute the normalized dense reward.

        Args:
            obs (Any): The observation data. By default the observation data will be in its most raw form, a dictionary (no flattening, wrappers etc.)
            action (torch.Tensor): The most recent action.
            info (dict): The info dictionary.
        """
        raise NotImplementedError()
```
```

### mani_skill/envs/scene.py

```
class StateDictRegistry()
class ManiSkillScene()
    """Class that manages a list of sub-scenes (sapien.Scene). In CPU simulation there should only be one sub-scene.
In GPU simulation, there can be many sub-scenes, and this wrapper ensures that use calls to many of the original sapien.Scene API
are applied to all sub-scenes. This includes calls to change"""
    def __init__(self, sub_scenes, sim_config, device, parallel_in_single_scene, backend)
    def can_render(self)
    def timestep(self)
    def timestep(self, timestep)
    def set_timestep(self, timestep)
    def get_timestep(self)
    def create_actor_builder(self)
    def create_articulation_builder(self)
    def create_urdf_loader(self)
    def create_mjcf_loader(self)
    def remove_actor(self, actor)
    def remove_articulation(self, articulation)
    def add_camera(self, name, pose, width, height, near, far, fovy, intrinsic, mount)
    def _sapien_add_camera(self, name, pose, width, height, near, far, fovy, intrinsic, mount)
    def _sapien_31_add_camera(self, name, pose, width, height, near, far, fovy, intrinsic, mount)
    def step(self)
    def update_render(self, update_sensors, update_human_render_cameras)
    def _sapien_update_render(self, update_sensors, update_human_render_cameras)
    def _sapien_31_update_render(self, update_sensors, update_human_render_cameras)
    def get_contacts(self)
    def get_all_actors(self)
    def get_all_articulations(self)
    def create_drive(self, body0, pose0, body1, pose1)
    def ambient_light(self)
    def ambient_light(self, color)
    def set_ambient_light(self, color)
    def add_point_light(self, position, color, shadow, shadow_near, shadow_far, shadow_map_size, scene_idxs)
    def add_directional_light(self, direction, color, shadow, position, shadow_scale, shadow_near, shadow_far, shadow_map_size, scene_idxs)
    def add_spot_light(self, position, direction, inner_fov, outer_fov, color, shadow, shadow_near, shadow_far, shadow_map_size, scene_idxs)
    def add_area_light_for_ray_tracing(self, pose, color, half_width, half_height, scene_idxs)
    def num_envs(self)
    def get_pairwise_contact_impulses(self, obj1, obj2)
    def get_pairwise_contact_forces(self, obj1, obj2)
    def scene_offsets(self)
    def scene_offsets_np(self)
    def add_to_state_dict_registry(self, object)
    def remove_from_state_dict_registry(self, object)
    def get_sim_state(self)
    def set_sim_state(self, state, env_idx)
    def _setup(self, enable_gpu)
    def _gpu_apply_all(self)
    def _gpu_fetch_all(self)
    def _get_all_render_bodies(self)
    def _setup_gpu_rendering(self)
    def _sapien_setup_gpu_rendering(self)
    def _sapien_31_setup_gpu_rendering(self)
    def _gpu_setup_sensors(self, sensors)
    def _sapien_gpu_setup_sensors(self, sensors)
    def _sapien_31_gpu_setup_sensors(self, sensors)
    def get_sensor_images(self, obs)
    def get_human_render_camera_images(self, camera_name)
```

### mani_skill/envs/scenes/base_env.py

```
class SceneManipulationEnv(BaseEnv)
    """A base environment for simulating manipulation tasks in more complex scenes. Creating this base environment is only useful
for explorations/visualization, there are no success/failure metrics or rewards.

Args:
    robot_uids: Which robot to place into the scene. Default is "fetch"

    fixed_scene:"""
    def __init__(self)
    def _default_sim_config(self)
    def reset(self, seed, options)
    def _load_lighting(self, options)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        return 0
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 1
```
```

### mani_skill/envs/sim2real_env.py

```
class Sim2RealEnv(Env)
    """Sim2RealEnv is a class that lets you interface with a real robot and align the real robot and environment with a simulation environment. It tries to ensure the action and observation space
are the exact same in the real and simulation environments. Any wrappers you apply to the simulation environmen"""
    def __init__(self, sim_env, agent, real_reset_function, sensor_data_preprocessing_function, render_mode, skip_data_checks, control_freq)
    def base_sim_env(self)
    def elapsed_steps(self)
    def _step_action(self, action)
    def step(self, action)
    def reset(self, seed, options)
    def get_obs(self, info, unflattened)
    def _flatten_raw_obs(self, obs)
    def _get_obs_agent(self)
    def _get_obs_extra(self, info)
    def _get_obs_sensor_data(self, apply_texture_transforms)
    def _get_obs_with_sensor_data(self, info, apply_texture_transforms)
    def get_sensor_params(self)
    def get_info(self)
    def render(self)
    def render_sensors(self)
    def get_sensor_images(self)
    def get_reward(self, obs, action, info)
    def compute_sparse_reward(self, obs, action, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
    def _check_observations(self, sample_sim_obs, sample_real_obs)
    def close(self)
    def preprocess_sensor_data(self, sensor_data, sensor_names)
    def __getattr__(self, name)

```python
def _get_obs_agent(self):
        # using the original user implemented sim env's _get_obs_agent function in case they modify it e.g. to remove qvel values as they might be too noisy
        return self.base_sim_env.__class__._get_obs_agent(cast(BaseEnv, self))
```

```python
def _get_obs_extra(self, info: dict):
        # using the original user implemented sim env's _get_obs_extra function in case they modify it e.g. to include engineered features like the tcp_pose of the robot
        try:
            return self.base_sim_env.__class__._get_obs_extra(cast(BaseEnv, self), info)
        except:
            # Print the original error
            import traceback

            print(f"Error in _get_obs_extra: {traceback.format_exc()}")

            # Print another message
            print(
                "If there is an error above a common cause is that the _get_obs_extra function defined in the simulation environment is using information not available in the real environment or real agent."
                "In this case you can override the _get_obs_extra function in the Sim2RealEnv class to compute the desired information in the real environment via a e.g., perception pipeline."
            )
            exit(-1)
```

```python
def _get_obs_sensor_data(self, apply_texture_transforms: bool = True):
        # note apply_texture_transforms is not used for real envs, data is expected to already be transformed to standard texture names, types, and shapes.
        self.agent.capture_sensor_data(self._sensor_names)
        data = self.agent.get_sensor_data(self._sensor_names)
        # observation data needs to be processed to be the same shape in simulation
        # default strategy is to do a center crop to the same shape as simulation and then resize image to the same shape as simulation
        data = self.preprocess_sensor_data(data)
        return data
```

```python
def _get_obs_with_sensor_data(
        self, info: dict, apply_texture_transforms: bool = True
    ) -> dict:
        """Get the observation with sensor data"""
        return self.base_sim_env.__class__._get_obs_with_sensor_data(
            cast(BaseEnv, self), info, apply_texture_transforms
        )
```

```python
def get_reward(self, obs, action, info):
        return self.base_sim_env.__class__.get_reward(
            cast(BaseEnv, self), obs, action, info
        )
```

```python
def compute_sparse_reward(self, obs: Any, action: torch.Tensor, info: dict):
        """
        Computes the sparse reward. By default this function tries to use the success/fail information in
        returned by the evaluate function and gives +1 if success, -1 if fail, 0 otherwise"""
        return self.base_sim_env.__class__.compute_sparse_reward(
            cast(BaseEnv, self), obs, action, info
        )
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        raise NotImplementedError()
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        raise NotImplementedError()
```

```python
def _check_observations(self, sample_sim_obs, sample_real_obs):
        """checks if the visual observations are aligned in terms of shape and resolution and expected data types"""

        # recursive check if the data is all the same shape
        def check_observation_match(sim_obs, real_obs, path=[]):
            """Recursively check if observations match in shape and dtype"""
            if isinstance(sim_obs, dict):
                for key in sim_obs.keys():
                    if key not in real_obs:
                        raise KeyError(
                            f"Key obs[\"{'.'.join(path + [key])}]\"] found in simulation observation but not in real observation"
                        )
                    check_observation_match(
                        sim_obs[key], real_obs[key], path=path + [key]
                    )
            else:
                assert (
                    sim_obs.shape == real_obs.shape
                ), f"Shape mismatch: obs[\"{'.'.join(path)}\"]: {sim_obs.shape} vs {real_obs.shape}"
                assert (
                    sim_obs.dtype == real_obs.dtype
                ), f"Dtype mismatch: obs[\"{'.'.join(path)}\"]: {sim_obs.dtype} vs {real_obs.dtype}"

        # Call the recursive function to check observations
        check_observation_match(sample_sim_obs, sample_real_obs)
```

```python
def check_observation_match(sim_obs, real_obs, path=[]):
            """Recursively check if observations match in shape and dtype"""
            if isinstance(sim_obs, dict):
                for key in sim_obs.keys():
                    if key not in real_obs:
                        raise KeyError(
                            f"Key obs[\"{'.'.join(path + [key])}]\"] found in simulation observation but not in real observation"
                        )
                    check_observation_match(
                        sim_obs[key], real_obs[key], path=path + [key]
                    )
            else:
                assert (
                    sim_obs.shape == real_obs.shape
                ), f"Shape mismatch: obs[\"{'.'.join(path)}\"]: {sim_obs.shape} vs {real_obs.shape}"
                assert (
                    sim_obs.dtype == real_obs.dtype
                ), f"Dtype mismatch: obs[\"{'.'.join(path)}\"]: {sim_obs.dtype} vs {real_obs.dtype}"
```
```

### mani_skill/envs/tasks/control/ant.py

```
class AntRobot(BaseAgent)
    def __init__(self)
    def _controller_configs(self)
    def _load_articulation(self, initial_pose)
class AntEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _after_control_step(self)
    def get_vels(self)
    def torso_height(self)
    def foot_contact_forces(self)
    def link_orientations(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def move_x_rew(self, info, move_speed)
    def standing_rew(self)
    def control_rew(self, action)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class AntWalk(AntEnv)
    """**Task Description:**
Ant moves in x direction at 0.5 m/s

**Randomizations:**
- Ant qpos and qvel have added noise from uniform distribution [-1e-2, 1e-2]

**Success Conditions:**
- No specific success conditions."""
    def __init__(self)
class AntRun(AntEnv)
    """**Task Description:**
Ant moves in x direction at 4 m/s

**Randomizations:**
- Ant qpos and qvel have added noise from uniform distribution [-1e-2, 1e-2]

**Success Conditions:**
- No specific success conditions."""
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        obs = super()._get_obs_extra(info)
        if self.obs_mode_struct.use_state:
            obs.update(
                cmass=info["cmass_linvel"],
                link_angvels=info["link_angvels"],
                link_linvels=info["link_linvels"],
                height=self.torso_height.view(-1, 1),
                link_orientations=self.link_orientations,
                foot_contact_forces=self.foot_contact_forces,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        small_control = (4 + self.control_rew(action)) / 5
        return (
            small_control * self.move_x_rew(info, self.move_speed) * self.standing_rew()
        )
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs, action, info)
```
```

### mani_skill/envs/tasks/control/cartpole.py

```
"""Adapted from https://github.com/google-deepmind/dm_control/blob/main/dm_control/suite/cartpole.py"""
class CartPoleRobot(BaseAgent)
    def _controller_configs(self)
    def _load_articulation(self, initial_pose)
class CartpoleEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def pole_angle_cosine(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class CartpoleBalanceEnv(CartpoleEnv)
    """**Task Description:**
Use the Cartpole robot to balance a pole on a cart.

**Randomizations:**
- Pole direction is randomized around the vertical axis. the range is [-0.05, 0.05] radians.

**Fail Conditions:**
- Pole is lower than the horizontal plane"""
    def __init__(self)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
class CartpoleSwingUpEnv(CartpoleEnv)
    """**Task Description:**
Use the Cartpole robot to swing up a pole on a cart.

**Randomizations:**
- Pole direction is randomized around the whole circle. the range is [-pi, pi] radians.

**Success Conditions:**
- No specific success conditions. The task is considered successful if the pole is upright """
    def __init__(self)
    def _initialize_episode(self, env_idx, options)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            velocity=self.agent.robot.links_map["pole_1"].linear_velocity,
            angular_velocity=self.agent.robot.links_map["pole_1"].angular_velocity,
        )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        cart_pos = self.agent.robot.links_map["cart"].pose.p[
            :, 0
        ]  # (B, ), we only care about x position
        centered = rewards.tolerance(cart_pos, margin=2)
        centered = (1 + centered) / 2  # (B, )

        small_control = rewards.tolerance(
            action, margin=1, value_at_margin=0, sigmoid="quadratic"
        )[:, 0]
        small_control = (4 + small_control) / 5

        angular_vel = self.agent.robot.get_qvel()[:, 1]
        small_velocity = rewards.tolerance(angular_vel, margin=5)
        small_velocity = (1 + small_velocity) / 2  # (B, )

        upright = (self.pole_angle_cosine + 1) / 2  # (B, )

        # upright is 1 when the pole is upright, 0 when the pole is upside down
        # small_control is 1 when the action is small, 0.8 when the action is large
        # small_velocity is 1 when the angular velocity is small, 0.5 when the angular velocity is large
        # centered is 1 when the cart is centered, 0 when the cart is at the edge of the screen

        reward = upright * centered * small_control * small_velocity
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        max_reward = 1.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/control/hopper.py

```
"""Adapted from https://github.com/google-deepmind/dm_control/blob/main/dm_control/suite/hopper.py"""
class HopperRobot(BaseAgent)
    def __init__(self)
    def _controller_configs(self)
    def _load_articulation(self, initial_pose)
    def get_proprioception(self)
class HopperEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def height(self)
    def subtreelinvelx(self)
    def touch(self, link_name)
    def _get_obs_state_dict(self, info)
class HopperStandEnv(HopperEnv)
    """**Task Description:**
Hopper robot stands upright

**Randomizations:**
- Hopper robot is randomly rotated [-pi, pi] radians about y axis.
- Hopper qpos are uniformly sampled within their allowed ranges

**Success Conditions:**
- No specific success conditions."""
    def __init__(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class HopperHopEnv(HopperEnv)
    """**Task Description:**
Hopper robot stays upright and moves in positive x direction with hopping motion

**Randomizations:**
- Hopper robot is randomly rotated [-pi, pi] radians about y axis.
- Hopper qpos are uniformly sampled within their allowed ranges

**Success Conditions:**
- No specific succes"""
    def __init__(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_state_dict(self, info: dict):
        return dict(
            agent=self._get_obs_agent(),
            toe_touch=self.touch("foot_toe"),
            heel_touch=self.touch("foot_heel"),
        )
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        standing = rewards.tolerance(self.height, lower=_STAND_HEIGHT, upper=2.0)
        return standing.view(-1)
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        max_reward = 1.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        standing = rewards.tolerance(self.height, lower=_STAND_HEIGHT, upper=2.0)
        hopping = rewards.tolerance(
            self.subtreelinvelx,
            lower=_HOP_SPEED,
            upper=float("inf"),
            margin=_HOP_SPEED / 2,
            value_at_margin=0.5,
            sigmoid="linear",
        )

        return standing.view(-1) * hopping.view(-1)
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        max_reward = 1.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/control/humanoid.py

```
"""Adapted from https://github.com/google-deepmind/dm_control/blob/main/dm_control/suite/humanoid.py"""
class HumanoidEnvBase(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _before_control_step(self)
    def head_height(self)
    def torso_upright(self, info)
    def torso_vertical_orientation(self, info)
    def extremities(self, info)
    def center_of_mass_velocity(self)
    def evaluate(self)
    def _load_scene(self, options)
    def control_rew(self, action)
    def dont_move_rew(self, info)
    def move_rew(self, info, move_speed)
    def standing_rew(self)
    def upright_rew(self, info)
class HumanoidEnvStandard(HumanoidEnvBase)
    def __init__(self)
    def _get_obs_state_dict(self, info)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def move_x_rew(self, info, move_speed)
class HumanoidStand(HumanoidEnvStandard)
    """**Task Description:**
Humanoid robot stands upright

**Randomizations:**
- Humanoid robot is randomly rotated [-pi, pi] radians about z axis.
- Humanoid qpos and qvel have added noise from uniform distribution [-1e-2, 1e-2]

**Fail Conditions:**
- Humanoid robot torso link leaves z range [0.7, 1.0]"""
    def __init__(self)
    def _get_obs_state_dict(self, info)
    def _initialize_episode(self, env_idx, options)
    def compute_normalized_dense_reward(self, obs, action, info)
class HumanoidWalk(HumanoidEnvStandard)
    """**Task Description:**
Humanoid moves in x direction at walking pace

**Randomizations:**
- Humanoid qpos and qvel have added noise from uniform distribution [-1e-2, 1e-2]

**Fail Conditions:**
- Humanoid robot torso link leaves z range [0.7, 1.0]"""
    def __init__(self)
    def compute_normalized_dense_reward(self, obs, action, info)
class HumanoidRun(HumanoidEnvStandard)
    """**Task Description:**
Humanoid moves in x direction at running pace

**Randomizations:**
- Humanoid qpos and qvel have added noise from uniform distribution [-1e-2, 1e-2]

**Fail Conditions:**
- Humanoid robot torso link leaves z range [0.7, 1.0]"""
    def __init__(self)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_state_dict(self, info: dict):
        # our qpos model doesn't include the free joint, meaning qpos and qvel are 21 dims, not 27
        # global dpos/dt and root (torso) dquaterion/dt are lost as result
        # we replace them with linear root linvel and root angularvel (equivalent info)
        return dict(
            agent=self._get_obs_agent(),  # (b, 21*2) root joint not included in our qpos
            root_vel=self.agent.robot.links_map[
                "dummy_root_0"
            ].get_linear_velocity(),  # free joint info, (b, 3)
            root_quat_vel=self.agent.robot.links_map[
                "dummy_root_0"
            ].get_angular_velocity(),  # free joint info, (b, 3)
            head_height=self.head_height,  # (b,1)
            com_velocity=info["cmass_linvel"],  # (b, 3)
            extremities=self.extremities(info),
            link_linvels=torch.stack(
                [link.get_linear_velocity() for link in self.active_links], dim=1
            ).view(-1, 16 * 3),
            link_angvels=torch.stack(
                [link.get_angular_velocity() for link in self.active_links], dim=1
            ).view(-1, 16 * 3),
            qfrc=self.agent.robot.get_qf(),
            orient=self.agent.robot.links_map["dummy_root_0"].pose.q,
        )
```

```python
def _get_obs_state_dict(self, info: dict):
        # make all obs completely egocentric, for z rotation invariance, since stand has z rot randomization
        root_pose_mat = self.agent.robot.links_map[
            "dummy_root_0"
        ].pose.to_transformation_matrix()[:, :3, :3]
        lin_vels = [
            link.get_linear_velocity() for link in self.active_links
        ]  # (links, b, 3)
        ang_vels = [
            link.get_angular_velocity() for link in self.active_links
        ]  # (links, b, 3)
        non_ego_vels = torch.stack(
            [*lin_vels, *ang_vels, info["cmass_linvel"]], dim=1
        )  # (b, len(lin_vels)+len(ang_vels)+1, 3)
        ego_vels = (non_ego_vels @ root_pose_mat).view(
            -1, (len(lin_vels) + len(ang_vels) + 1) * 3
        )
        return dict(
            agent=self._get_obs_agent(),  # (b, 21*2) root joint not included in our qpos
            head_height=self.head_height,  # (b,1)
            egocentric_vels=ego_vels,
            extremities=self.extremities(info),
        )
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        small_control = (4 + self.control_rew(action)) / 5
        stand_rew = (
            small_control
            * self.standing_rew()
            * self.upright_rew(info)
            * self.dont_move_rew(info)
        )

        return stand_rew
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        small_control = (4 + self.control_rew(action)) / 5
        walk_rew = (
            small_control
            * self.move_x_rew(info, _WALK_SPEED)
            * self.upright_rew(info)
            * self.standing_rew()
        )
        alive_rew = 1
        return (alive_rew + walk_rew) / 2
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        # reward function used by mjx for ppo humanoid run
        rew_scale = 0.1
        run_x_rew = info["cmass_linvel"][:, 0]
        alive_rew = 5
        return rew_scale * (
            alive_rew + 1.25 * run_x_rew - 0.1 * action.pow(2).sum(dim=-1)
        )
```
```

### mani_skill/envs/tasks/dexterity/insert_flower.py

```
class InsertFlowerEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _after_reconfigure(self, options)
    def _initialize_episode(self, env_idx, options)
    def _initialize_actors(self, env_idx)
    def _initialize_agent(self, env_idx)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        return {}
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict) -> float:
        object_pos = self.flower.pose.p
        dist_outside = torch.max(
            torch.max(
                self.target_area_box[0] - object_pos, torch.zeros_like(object_pos)
            ),  # lower bound
            torch.max(
                object_pos - self.target_area_box[1], torch.zeros_like(object_pos)
            ),  # upper bound
        )
        reward = torch.exp(-5 * torch.norm(dist_outside)).reshape(-1)

        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 4.0
```
```

### mani_skill/envs/tasks/dexterity/rotate_single_object_in_hand.py

```
class RotateSingleObjectInHand(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _after_reconfigure(self, options)
    def _initialize_episode(self, env_idx, options)
    def _initialize_actors(self, env_idx)
    def _initialize_agent(self, env_idx)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class RotateSingleObjectInHandLevel0(RotateSingleObjectInHand)
    def __init__(self)
class RotateSingleObjectInHandLevel1(RotateSingleObjectInHand)
    def __init__(self)
class RotateSingleObjectInHandLevel2(RotateSingleObjectInHand)
    def __init__(self)
class RotateSingleObjectInHandLevel3(RotateSingleObjectInHand)
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        with torch.device(self.device):
            obs = dict(rotate_dir=self.rot_dir)
            if self.obs_mode_struct.use_state:
                obs.update(
                    obj_pose=vectorize_pose(self.obj.pose),
                    obj_tip_vec=info["obj_tip_vec"].view(self.num_envs, 12),
                )
            return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        # 1. rotation reward
        angle = info["rotation_angle"]
        reward = 20 * angle

        # 2. velocity penalty
        obj_vel = info["obj_vel"]
        reward += -0.1 * obj_vel

        # 3. falling penalty
        obj_fall = info["obj_fall"]
        reward += -50.0 * obj_fall

        # 4. effort penalty
        power = torch.abs(info["power"])
        reward += -0.0003 * power

        # 5. torque penalty
        qf = info["qf"]
        qf_norm = torch.linalg.norm(qf, dim=-1)
        reward += -0.0003 * qf_norm

        # 6. finger object distance reward
        obj_tip_dist = info["obj_tip_dist"]
        distance_rew = 0.1 / (0.02 + 4 * obj_tip_dist)
        reward += torch.mean(torch.clip(distance_rew, 0, 1), dim=-1)

        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 4.0
```
```

### mani_skill/envs/tasks/dexterity/rotate_valve.py

```
class RotateValveEnv(BaseEnv)
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _load_articulations(self)
    def _initialize_episode(self, env_idx, options)
    def _initialize_actors(self, env_idx)
    def _initialize_agent(self, env_idx)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
def sample_valve_angles(num_head, random_state, min_angle_diff, num_max_attempts)
class RotateValveEnvLevel0(RotateValveEnv)
    def __init__(self)
class RotateValveEnvLevel1(RotateValveEnv)
    def __init__(self)
class RotateValveEnvLevel2(RotateValveEnv)
    def __init__(self)
class RotateValveEnvLevel3(RotateValveEnv)
    def __init__(self)
class RotateValveEnvLevel4(RotateValveEnv)
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        with torch.device(self.device):
            valve_qpos = self.valve.qpos
            valve_qvel = self.valve.qvel
            obs = dict(
                rotate_dir=self.rotate_direction.to(torch.float32),
                valve_qpos=valve_qpos,
                valve_qvel=valve_qvel,
                valve_x=torch.cos(valve_qpos[:, 0]),
                valve_y=torch.sin(valve_qpos[:, 0]),
            )
            if self.obs_mode_struct.use_state:
                obs.update(
                    valve_pose=vectorize_pose(self.valve.pose),
                )
            return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        rotation = info["valve_rotation"]
        qvel = self.valve.qvel

        # Distance between fingertips and the circle grouned by valve tips
        tip_poses = self.agent.tip_poses  # (b, 3, 7)
        tip_pos = tip_poses[:, :, :2]  # (b, 3, 2)
        valve_pos = self.valve_link.pose.p[:, :2]  # (b, 2)
        valve_tip_dist = torch.linalg.norm(tip_pos - valve_pos[:, None, :], dim=-1)
        desired_valve_tip_dist = self.capsule_lens[:, None] - self.capsule_offset
        error = torch.norm(valve_tip_dist - desired_valve_tip_dist, dim=-1)
        reward = 1 - torch.tanh(error * 10)

        directed_velocity = qvel[:, 0] * self.rotate_direction
        reward += torch.tanh(5 * directed_velocity) * 4

        motion_reward = torch.clip(rotation / torch.pi / 2, -1, 1)
        reward += motion_reward

        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 6.0
```
```

### mani_skill/envs/tasks/digital_twins/base_env.py

```
class BaseDigitalTwinEnv(BaseEnv)
    """Base Environment class for easily setting up evaluation digital twins for real2sim and sim2real

This is based on the [SIMPLER](https://simpler-env.github.io/) and currently has the following tricks for
making accurate simulated environments of real world datasets

Greenscreening: Add a greenscreene"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def remove_object_from_greenscreen(self, object)
    def _after_reconfigure(self, options)
    def _green_sceen_rgb(self, rgb, segmentation, overlay_img)
    def _get_obs_sensor_data(self, apply_texture_transforms)

```python
def _get_obs_sensor_data(self, apply_texture_transforms: bool = True):
        obs = super()._get_obs_sensor_data(apply_texture_transforms)

        # "greenscreen" process
        if self.rgb_overlay_mode == "none":
            return obs
        if (
            self.obs_mode_struct.visual.rgb
            and self.obs_mode_struct.visual.segmentation
            and self.rgb_overlay_paths is not None
        ):
            # get the actor ids of objects to manipulate; note that objects here are not articulated
            for camera_name in self._rgb_overlay_images.keys():
                # obtain overlay mask based on segmentation info
                assert (
                    "segmentation" in obs[camera_name].keys()
                ), "Image overlay requires segment info in the observation!"
                if (
                    self._rgb_overlay_images[camera_name].device
                    != obs[camera_name]["rgb"].device
                ):
                    self._rgb_overlay_images[camera_name] = self._rgb_overlay_images[
                        camera_name
                    ].to(obs[camera_name]["rgb"].device)
                overlay_img = self._rgb_overlay_images[camera_name]
                green_screened_rgb = self._green_sceen_rgb(
                    obs[camera_name]["rgb"],
                    obs[camera_name]["segmentation"],
                    overlay_img,
                )
                obs[camera_name]["rgb"] = green_screened_rgb
        return obs
```
```

### mani_skill/envs/tasks/digital_twins/bridge_dataset_eval/base_env.py

```
"""Base environment for Bridge dataset environments"""
class WidowX250SBridgeDatasetFlatTable(WidowX250S)
    def _sensor_configs(self)
    def _controller_configs(self)
class WidowX250SBridgeDatasetSink(WidowX250SBridgeDatasetFlatTable)
    def _sensor_configs(self)
class BaseBridgeEnv(BaseDigitalTwinEnv)
    """Base Digital Twin environment for digital twins of the BridgeData v2"""
    def __init__(self, obj_names, xyz_configs, quat_configs)
    def _default_sim_config(self)
    def _default_human_render_camera_configs(self)
    def _build_actor_helper(self, model_id, scale, kinematic, initial_pose)
    def _load_lighting(self, options)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _settle(self, t)
    def _evaluate(self, success_require_src_completely_on_target, z_flag_required_offset)
    def is_final_subtask(self)
```

### mani_skill/envs/tasks/digital_twins/bridge_dataset_eval/put_on_in_scene.py

```
class PutCarrotOnPlateInScene(BaseBridgeEnv)
    def __init__(self)
    def evaluate(self)
    def get_language_instruction(self)
class PutEggplantInBasketScene(BaseBridgeEnv)
    def __init__(self)
    def evaluate(self)
    def get_language_instruction(self)
    def _load_lighting(self, options)
class StackGreenCubeOnYellowCubeBakedTexInScene(BaseBridgeEnv)
    def __init__(self)
    def evaluate(self)
    def get_language_instruction(self)
class PutSpoonOnTableClothInScene(BaseBridgeEnv)
    def __init__(self)
    def evaluate(self)
    def get_language_instruction(self)
```

### mani_skill/envs/tasks/digital_twins/so100_arm/grasp_cube.py

```
class SO100GraspCubeDomainRandomizationConfig()
    def dict(self)
class SO100GraspCubeEnv(BaseDigitalTwinEnv)
    """**Task Description:**
A simple task where the objective is to grasp a cube with the SO100 arm and bring it up to a target rest pose.

**Randomizations:**
- the cube's xy position is randomized on top of a table in a region of size [0.2, 0.2] x [-0.2, -0.2]. It is placed flat on the table
- the cube'"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_lighting(self, options)
    def _load_scene(self, options)
    def sample_camera_poses(self, n)
    def _initialize_episode(self, env_idx, options)
    def _before_control_step(self)
    def _get_obs_agent(self)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_agent(self):
        # the default get_obs_agent function in ManiSkill records qpos and qvel. However
        # SO100 arm qvel are likely too noisy to learn from and not implemented.
        obs = dict(qpos=self.agent.robot.get_qpos())
        controller_state = self.agent.controller.get_state()
        if len(controller_state) > 0:
            obs.update(controller=controller_state)
        return obs
```

```python
def _get_obs_extra(self, info: dict):
        # we ensure that the observation data is always retrievable in the real world, using only real world
        # available data (joint positions or the controllers target joint positions in this case).
        obs = dict(
            dist_to_rest_qpos=self.agent.controller._target_qpos[:, :-1]
            - self.rest_qpos[:-1],
        )
        if self.obs_mode_struct.state:
            # state based policies can gain access to more information that helps learning
            obs.update(
                is_grasped=info["is_grasped"],
                obj_pose=self.cube.pose.raw_pose,
                tcp_pos=self.agent.tcp_pos,
                tcp_to_obj_pos=self.cube.pose.p - self.agent.tcp_pos,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # note the info object is the data returned by the evaluate function. We can reuse information
        # to save compute time.
        # this reward function essentially has two stages, before and after grasping.
        # in stage 1 we reward the robot for reaching the object and grasping it.
        # in stage 2 if the robot is grasping the object, we reward it for controlling the robot returning to the predefined rest pose.
        # in all stages we penalize the robot for touching the table.
        # this reward function is very simple and can easily be improved to learn more robust behaviors or solve more complex problems.

        tcp_to_obj_dist = torch.linalg.norm(
            self.cube.pose.p - self.agent.tcp_pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)
        reward = reaching_reward + info["is_grasped"]
        place_reward = torch.exp(-2 * info["distance_to_rest_qpos"])
        reward += place_reward * info["is_grasped"]
        reward -= 2 * info["touching_table"].float()
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        # for more stable RL we often also permit defining a noramlized reward function where you manually scale the reward down by its max value like so
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 3
```
```

### mani_skill/envs/tasks/drawing/draw.py

```
class TableTopFreeDrawEnv(BaseEnv)
    """**Task Description:**
Instantiates a table with a white canvas on it and a robot with a stick that draws red lines. This environment is primarily for a reference / for others to copy
to make their own drawing tasks.

**Randomizations:**
None

**Success Conditions:**
None

**Goal Specification:**
Non"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _after_control_step(self)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        return dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
```
```

### mani_skill/envs/tasks/drawing/draw_svg.py

```
class DrawSVGEnv(BaseEnv)
    """**Task Description:**
Instantiates a table with a white canvas on it and a svg path specified with an outline. A robot with a stick is to draw the triangle with a red line.

**Randomizations:**
- the goal svg's position on the xy-plane is randomized
- the goal svg's z-rotation is randomized in range"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _after_control_step(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def success_check(self)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )

        if "state" in self.obs_mode:
            obs.update(
                goal_pose=self.goal_outline.pose.raw_pose.reshape(self.num_envs, -1),
                tcp_to_verts_pos=(
                    self.points - self.agent.tcp.pose.p.unsqueeze(1)
                ).reshape(self.num_envs, -1),
                goal_pos=(self.goal_outline.pose.p).reshape(self.num_envs, -1),
                vertices=self.points.reshape(self.num_envs, -1),
                continuous=torch.ones((self.num_envs, 1), device=self.device)
                * self.continuous,  # if the path is continuous
            )

        return obs
```
```

### mani_skill/envs/tasks/drawing/draw_triangle.py

```
class DrawTriangleEnv(BaseEnv)
    """**Task Description:**
Instantiates a table with a white canvas on it and a goal triangle with an outline. A robot with a stick is to draw the triangle with a red line.

**Randomizations:**
- the goal triangle's position on the xy-plane is randomized
- the goal triangle's z-rotation is randomized in """
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _after_control_step(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def generate_triangle_with_points(self, n, vertices)
    def success_check(self)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )

        if "state" in self.obs_mode:
            obs.update(
                goal_pose=self.goal_tri.pose.raw_pose.reshape(self.num_envs, -1),
                tcp_to_verts_pos=(
                    self.vertices - self.agent.tcp.pose.p.unsqueeze(1)
                ).reshape(self.num_envs, -1),
                goal_pos=self.goal_tri.pose.p.reshape(self.num_envs, -1),
                vertices=self.vertices.reshape(self.num_envs, -1),
            )

        return obs
```
```

### mani_skill/envs/tasks/empty_env.py

```
class EmptyEnv(BaseEnv)
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```
```

### mani_skill/envs/tasks/fmb/fmb.py

```
class FMBAssembly1Env(BaseEnv)
    """Task Description
----------------
This task is a simulation version of one of the Multi-Object Multi-Stage Manipulation Tasks (Assembly1) from [Functional Manipulation Benchmark (Luo et. al)](https://functional-manipulation-benchmark.github.io/index.html).
The goal here is to assemble parts together"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(tcp_pose=self.agent.tcp.pose.raw_pose)
        if self.obs_mode_struct.use_state:
            obs.update(
                board_pos=self.board.pose.p,
                bridge_pose=self.bridge.pose.raw_pose,
                reorienting_fixture_pose=self.reorienting_fixture.pose.raw_pose,
            )
        return dict()
```
```

### mani_skill/envs/tasks/humanoid/humanoid_pick_place.py

```
class HumanoidPickPlaceEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
class HumanoidPlaceAppleInBowl(HumanoidPickPlaceEnv)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def _grasp_release_reward(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class UnitreeG1PlaceAppleInBowlEnv(HumanoidPlaceAppleInBowl)
    """**Task Description:**
Control the humanoid unitree G1 robot to grab an apple with its right arm and place it in a bowl to the side

**Randomizations:**
- the bowl's xy position is randomized on top of a table in the region [0.025, 0.025] x [-0.025, -0.025]. It is placed flat on the table
- the apple"""
    def __init__(self)
    def _default_sim_config(self)
    def _initialize_episode(self, env_idx, options)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```

```python
def _get_obs_extra(self, info: dict):
        # in reality some people hack is_grasped into observations by checking if the gripper can close fully or not
        obs = dict(
            is_grasped=info["is_grasped"],
            tcp_pose=self.agent.right_tcp.pose.raw_pose,
        )
        if "state" in self.obs_mode:
            obs.update(
                bowl_pos=self.bowl.pose.p,
                obj_pose=self.apple.pose.raw_pose,
                tcp_to_obj_pos=self.apple.pose.p - self.agent.right_tcp.pose.p,
                obj_to_goal_pos=self.bowl.pose.p - self.apple.pose.p,
            )
        return obs
```

```python
def _grasp_release_reward(self):
        """a dense reward that rewards the agent for opening their hand"""
        return 1 - torch.tanh(self.agent.right_hand_dist_to_open_grasp())
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        tcp_to_obj_dist = torch.linalg.norm(
            self.apple.pose.p - self.agent.right_tcp.pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)
        reward = reaching_reward

        is_grasped = info["is_grasped"]
        reward += is_grasped

        # encourage to bring apple to above the bowl then drop it.
        obj_to_goal_dist = torch.linalg.norm(
            (self.bowl.pose.p + torch.tensor([0, 0, 0.15], device=self.device))
            - self.apple.pose.p,
            axis=1,
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        reward += place_reward * is_grasped

        # once above the goal, encourage to have the hand above the bowl still and begin releasing the grasp
        obj_high_above_bowl = obj_to_goal_dist < 0.025
        grasp_release_reward = self._grasp_release_reward()
        reward[obj_high_above_bowl] = (
            4
            + place_reward[obj_high_above_bowl]
            + grasp_release_reward[obj_high_above_bowl]
        )
        reward[info["success"]] = (
            8 + (place_reward + grasp_release_reward)[info["success"]]
        )
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 10
```
```

### mani_skill/envs/tasks/humanoid/humanoid_stand.py

```
class HumanoidStandEnv(BaseEnv)
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_sparse_reward(self, obs, action, info)
class UnitreeH1StandEnv(HumanoidStandEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_human_render_camera_configs(self)
    def _initialize_episode(self, env_idx, options)
class UnitreeG1StandEnv(HumanoidStandEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_human_render_camera_configs(self)
    def _initialize_episode(self, env_idx, options)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```

```python
def compute_sparse_reward(self, obs: Any, action: torch.Tensor, info: dict):
        return info["is_standing"]
```
```

### mani_skill/envs/tasks/humanoid/transport_box.py

```
class TransportBoxEnv(BaseEnv)
    """**Task Description:**
A G1 humanoid robot must find a box on a table and transport it to the other table and place it there.

**Randomizations:**
- the box's xy position is randomized in the region [-0.05, -0.05] x [0.2, 0.05]
- the box's z-axis rotation is randomized to a random angle in [0, np.pi/"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def box_right_grasp_point(self)
    def box_left_grasp_point(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            right_tcp_pose=self.agent.right_tcp.pose.raw_pose,
            left_tcp_pose=self.agent.left_tcp.pose.raw_pose,
        )

        if "state" in self.obs_mode:
            obs.update(
                box_pose=self.box.pose.raw_pose,
                right_tcp_to_box_pos=self.box.pose.p - self.agent.right_tcp.pose.p,
                left_tcp_to_box_pos=self.box.pose.p - self.agent.left_tcp.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # Stage 1, move to face the box on the table. Succeeds if facing_table_with_box
        reward = 1 - torch.tanh((self.agent.robot.qpos[:, 0] + 1.4).abs())

        # Stage 2, grasp the box stably. Succeeds if box_grasped
        # encourage arms to go down essentially and for tcps to be close to the edge of the box
        stage_2_reward = (
            1
            + (1 - torch.tanh((self.agent.robot.qpos[:, 3]).abs())) / 4
            + (1 - torch.tanh((self.agent.robot.qpos[:, 4]).abs())) / 4
            + (
                1
                - torch.tanh(
                    3
                    * torch.linalg.norm(
                        self.agent.right_tcp.pose.p - self.box_right_grasp_point.p,
                        dim=1,
                    )
                )
            )
            / 4
            + (
                1
                - torch.tanh(
                    3
                    * torch.linalg.norm(
                        self.agent.left_tcp.pose.p - self.box_left_grasp_point.p, dim=1
                    )
                )
            )
            / 4
        )
        reward[info["facing_table_with_box"]] = stage_2_reward[
            info["facing_table_with_box"]
        ]
        # Stage 3 transport box to above the other table, Succeeds if box_at_correct_table_xy
        stage_3_reward = (
            2 + 1 - torch.tanh((self.agent.robot.qpos[:, 0] - 1.4).abs() / 5)
        )
        reward[info["box_grasped"]] = stage_3_reward[info["box_grasped"]]
        # Stage 4 let go of the box. Succeeds if success (~box_grasped & box_at_correct_table)
        stage_4_reward = (
            3
            + (1 - torch.tanh((self.agent.robot.qpos[:, 3] - 1.25).abs())) / 2
            + (1 - torch.tanh((self.agent.robot.qpos[:, 4] + 1.25).abs())) / 2
        )
        reward[info["box_at_correct_table_xy"]] = stage_4_reward[
            info["box_at_correct_table_xy"]
        ]
        # encourage agent to stay close to a target qposition?
        reward[info["success"]] = 5
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs, action, info) / 5
```
```

### mani_skill/envs/tasks/mobile_manipulation/open_cabinet_drawer.py

```
class OpenCabinetDrawerEnv(BaseEnv)
    """**Task Description:**
Use the Fetch mobile manipulation robot to move towards a target cabinet and open the target drawer out.

**Randomizations:**
- Robot is randomly initialized 1.6 to 1.8 meters away from the cabinet and positioned to face it
- Robot's base orientation is randomized by -9 to 9 de"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _load_cabinets(self, joint_types)
    def _after_reconfigure(self, options)
    def handle_link_positions(self, env_idx)
    def _initialize_episode(self, env_idx, options)
    def _after_control_step(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class OpenCabinetDoorEnv(OpenCabinetDrawerEnv)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )

        if "state" in self.obs_mode:
            obs.update(
                tcp_to_handle_pos=info["handle_link_pos"] - self.agent.tcp.pose.p,
                target_link_qpos=self.handle_link.joint.qpos,
                target_handle_pos=info["handle_link_pos"],
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        tcp_to_handle_dist = torch.linalg.norm(
            self.agent.tcp.pose.p - info["handle_link_pos"], axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_handle_dist)
        amount_to_open_left = torch.div(
            self.target_qpos - self.handle_link.joint.qpos, self.target_qpos
        )
        open_reward = 2 * (1 - amount_to_open_left)
        reaching_reward[
            amount_to_open_left < 0.999
        ] = 2  # if joint opens even a tiny bit, we don't need reach reward anymore
        # print(open_reward.shape)
        open_reward[info["open_enough"]] = 3  # give max reward here
        reward = reaching_reward + open_reward
        reward[info["success"]] = 5.0
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        max_reward = 5.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/mobile_manipulation/robocasa/kitchen.py

```
class RoboCasaKitchenEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _default_viewer_camera_config(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def _setup_kitchen_references(self)
    def register_fixture_ref(self, ref_name, fn_kwargs)
    def sample_object(self, groups, exclude_groups, graspable, microwavable, washable, cookable, freezable, split, obj_registries, max_size, object_scale, rng)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```
```

### mani_skill/envs/tasks/quadruped/quadruped_reach.py

```
class QuadrupedReachEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def _compute_undesired_contacts(self, threshold)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class AnymalCReachEnv(QuadrupedReachEnv)
    """**Task Description:**
Control the AnymalC robot to reach a target location in front of it. Note the current reward function works but more needs to be added to constrain the learned quadruped gait looks more natural

**Randomizations:**
- Robot is initialized in a stable rest/standing position
- The"""
    def __init__(self)
class UnitreeGo2ReachEnv(QuadrupedReachEnv)
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            root_linear_velocity=self.agent.robot.root_linear_velocity,
            root_angular_velocity=self.agent.robot.root_angular_velocity,
            reached_goal=info["success"],
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                goal_pos=self.goal.pose.p[:, :2],
                robot_to_goal=self.goal.pose.p[:, :2] - self.agent.robot.pose.p[:, :2],
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        robot_to_goal_dist = info["robot_to_goal_dist"]
        reaching_reward = 1 - torch.tanh(1 * robot_to_goal_dist)

        # various penalties:
        lin_vel_z_l2 = torch.square(self.agent.robot.root_linear_velocity[:, 2])
        ang_vel_xy_l2 = (
            torch.square(self.agent.robot.root_angular_velocity[:, :2])
        ).sum(axis=1)
        penalties = (
            lin_vel_z_l2 * -2
            + ang_vel_xy_l2 * -0.05
            + self._compute_undesired_contacts() * -1
            + torch.linalg.norm(self.agent.robot.qpos - self.default_qpos, axis=1)
            * -0.05
        )
        reward = 1 + 2 * reaching_reward + penalties
        reward[info["fail"]] = 0
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        max_reward = 3.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/quadruped/quadruped_spin.py

```
class QuadrupedSpinEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def _compute_undesired_contacts(self, threshold)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class AnymalCSpinEnv(QuadrupedSpinEnv)
    """**Task Description:**
Control the AnymalC robot to spin around in place as fast as possible and is rewarded by its angular velocity.

**Randomizations:**
- Robot is initialized in a stable rest/standing position

**Fail Conditions:**
- If the robot has fallen over, which is considered True when the """
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            root_linear_velocity=self.agent.robot.root_linear_velocity,
            root_angular_velocity=self.agent.robot.root_angular_velocity,
        )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        rotation_reward = self.agent.robot.root_angular_velocity[:, 2]
        # various penalties:
        lin_vel_z_l2 = torch.square(self.agent.robot.root_linear_velocity[:, 2])
        ang_vel_xy_l2 = (
            torch.square(self.agent.robot.root_angular_velocity[:, :2])
        ).sum(axis=1)
        penalties = (
            lin_vel_z_l2 * -2
            + ang_vel_xy_l2 * -0.05
            + self._compute_undesired_contacts() * -1
            + torch.linalg.norm(self.agent.robot.qpos - self.default_qpos, axis=1)
            * -0.05
        )
        reward = 2 * rotation_reward + penalties
        reward[info["fail"]] = -100
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        max_reward = 2.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/rotate_cube.py

```
class RotateCubeEnv(BaseEnv)
    """Modified from https://github.com/NVIDIA-Omniverse/IsaacGymEnvs/blob/main/isaacgymenvs/tasks/trifinger.py
https://github.com/NVIDIA-Omniverse/IsaacGymEnvs/blob/main/isaacgymenvs/cfg/task/Trifinger.yaml"""
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_actors(self, env_idx)
    def _initialize_episode(self, env_idx, options)
    def _sample_object_goal_poses(self, env_idx, difficulty)
    def evaluate(self)
    def _initialize_agent(self, env_idx)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class RotateCubeEnvLevel0(RotateCubeEnv)
    def __init__(self)
class RotateCubeEnvLevel1(RotateCubeEnv)
    def __init__(self)
class RotateCubeEnvLevel2(RotateCubeEnv)
    def __init__(self)
class RotateCubeEnvLevel3(RotateCubeEnv)
    def __init__(self)
class RotateCubeEnvLevel4(RotateCubeEnv)
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            goal_pos=self.obj_goal.pose.p,
            goal_q=self.obj_goal.pose.q,
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                obj_p=self.obj.pose.p,
                obj_q=self.obj.pose.q,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        obj_pos = self.obj.pose.p
        obj_q = self.obj.pose.q
        goal_pos = self.obj_goal.pose.p
        goal_q = self.obj_goal.pose.q

        object_dist_weight = 5
        object_rot_weight = 5

        # Reward penalising finger movement

        tip_poses = self.agent.tip_poses
        # shape (N, 3 + 4, 3 fingers)

        finger_reach_object_dist_1 = torch.norm(
            tip_poses[:, :3, 0] - obj_pos, p=2, dim=-1
        )
        finger_reach_object_dist_2 = torch.norm(
            tip_poses[:, :3, 1] - obj_pos, p=2, dim=-1
        )
        finger_reach_object_dist_3 = torch.norm(
            tip_poses[:, :3, 2] - obj_pos, p=2, dim=-1
        )
        finger_reach_object_reward1 = 1 - torch.tanh(5 * finger_reach_object_dist_1)
        finger_reach_object_reward2 = 1 - torch.tanh(5 * finger_reach_object_dist_2)
        finger_reach_object_reward3 = 1 - torch.tanh(5 * finger_reach_object_dist_3)
        finger_reach_object_reward = (
            object_dist_weight
            * (
                finger_reach_object_reward1
                + finger_reach_object_reward2
                + finger_reach_object_reward3
            )
            / 3
        )

        # Reward for object distance
        object_dist = torch.norm(obj_pos - goal_pos, p=2, dim=-1)

        init_xyz_tensor = torch.tensor(
            [0, 0, 0.032], dtype=torch.float, device=self.device
        ).reshape(1, 3)
        init_z_dist = torch.norm(
            init_xyz_tensor
            - goal_pos[
                ...,
            ],
            p=2,
            dim=-1,
        )

        # object_dist_reward = object_dist_weight * dt * lgsk_kernel(object_dist, scale=50., eps=2.)

        object_dist_reward = 1 - torch.tanh(5 * object_dist)
        object_init_dist_reward = 1 - torch.tanh(5 * init_z_dist)
        object_dist_reward -= object_init_dist_reward

        init_z_tensor = torch.tensor(
            [0.032], dtype=torch.float, device=self.device
        ).reshape(1, 1)
        object_z_dist = torch.norm(obj_pos[..., 2:3] - goal_pos[..., 2:3], p=2, dim=-1)
        init_z_dist = torch.norm(init_z_tensor - goal_pos[..., 2:3], p=2, dim=-1)
        object_lift_reward = 5 * ((1 - torch.tanh(5 * object_z_dist)))
        object_init_z_reward = 5 * ((1 - torch.tanh(5 * init_z_dist)))

        object_lift_reward -= object_init_z_reward

        # extract quaternion orientation
        angles = common.quat_diff_rad(obj_q, goal_q)
        object_rot_reward = -1 * torch.abs(angles)
        pose_reward = (
            object_dist_weight * (object_dist_reward + object_lift_reward)
            + object_rot_weight * object_rot_reward
        )
        total_reward = finger_reach_object_reward + pose_reward
        total_reward = total_reward.clamp(-15, 15)
        total_reward[info["success"]] = 15
        return total_reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        self.max_reward = 15
        dense_reward = self.compute_dense_reward(obs=obs, action=action, info=info)
        norm_dense_reward = dense_reward / (2 * self.max_reward) + 0.5
        return norm_dense_reward
```
```

### mani_skill/envs/tasks/tabletop/assembling_kits.py

```
class AssemblingKitsEnv(BaseEnv)
    """**Task Description:**
The robot must pick up one of the misplaced shapes on the board/kit and insert it into the correct empty slot.

**Randomizations:**
- the kit geometry is randomized, with different already inserted shapes and different holes affording insertion of specific shapes. (during recon"""
    def __init__(self, asset_root, robot_uids, num_envs, reconfiguration_freq)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _parse_json(self, path)
    def _get_kit_builder_and_goals(self, kit_id)
    def _get_object_builder(self, object_id, static, color_id)
    def _initialize_episode(self, env_idx, options)
    def _check_pos_diff(self, pos_eps)
    def _check_rot_diff(self, rot_eps)
    def _check_in_slot(self, obj, height_eps)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                obj_pose=self.obj.pose.raw_pose,
                tcp_to_obj_pos=self.obj.pose.p - self.agent.tcp.pose.p,
                goal_pos=self.goal_pos,
                goal_rot=self.goal_rot,
                obj_to_goal_pos=self.goal_pos - self.obj.pose.p,
            )
        return obs
```
```

### mani_skill/envs/tasks/tabletop/lift_peg_upright.py

```
class LiftPegUprightEnv(BaseEnv)
    """**Task Description:**
A simple task where the objective is to move a peg laying on the table to any upright position on the table

**Randomizations:**
- the peg's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1]. It is placed flat along it's length on the table

**"""
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                obj_pose=self.peg.pose.raw_pose,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        # rotation reward as cosine similarity between peg direction vectors
        # peg center of mass to end of peg, (1,0,0), rotated by peg pose rotation
        # dot product with its goal orientation: (0,0,1) or (0,0,-1)
        qmats = rotation_conversions.quaternion_to_matrix(self.peg.pose.q)
        vec = torch.tensor([1.0, 0, 0], device=self.device)
        goal_vec = torch.tensor([0, 0, 1.0], device=self.device)
        rot_vec = (qmats @ vec).view(-1, 3)
        # abs since (0,0,-1) is also valid, values in [0,1]
        rot_rew = (rot_vec @ goal_vec).view(-1).abs()
        reward = rot_rew

        # position reward using common maniskill distance reward pattern
        # giving reward in [0,1] for moving center of mass toward half length above table
        z_dist = torch.abs(self.peg.pose.p[:, 2] - self.peg_half_length)
        reward += 1 - torch.tanh(5 * z_dist)

        # small reward to motivate initial reaching
        # initially, we want to reach and grip peg
        to_grip_vec = self.peg.pose.p - self.agent.tcp.pose.p
        to_grip_dist = torch.linalg.norm(to_grip_vec, axis=1)
        reaching_rew = 1 - torch.tanh(5 * to_grip_dist)
        # reaching reward granted if gripping block
        reaching_rew[self.agent.is_grasping(self.peg)] = 1
        # weight reaching reward less
        reaching_rew = reaching_rew / 5
        reward += reaching_rew

        reward[info["success"]] = 3
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        max_reward = 3.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/peg_insertion_side.py

```
def _build_box_with_hole(scene, inner_radius, outer_radius, depth, center)
class PegInsertionSideEnv(BaseEnv)
    """**Task Description:**
Pick up a orange-white peg and insert the orange end into the box with a hole in it.

**Randomizations:**
- Peg half length is randomized between 0.085 and 0.125 meters. Box half length is the same value. (during reconfiguration)
- Peg radius/half-width is randomized between 0."""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def peg_head_pos(self)
    def peg_head_pose(self)
    def box_hole_pose(self)
    def goal_pose(self)
    def has_peg_inserted(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(tcp_pose=self.agent.tcp.pose.raw_pose)
        if self.obs_mode_struct.use_state:
            obs.update(
                peg_pose=self.peg.pose.raw_pose,
                peg_half_size=self.peg_half_sizes,
                box_hole_pose=self.box_hole_pose.raw_pose,
                box_hole_radius=self.box_hole_radii,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # Stage 1: Encourage gripper to be rotated to be lined up with the peg

        # Stage 2: Encourage gripper to move close to peg tail and grasp it
        gripper_pos = self.agent.tcp.pose.p
        tgt_gripper_pose = self.peg.pose
        offset = sapien.Pose(
            [-0.06, 0, 0]
        )  # account for panda gripper width with a bit more leeway
        tgt_gripper_pose = tgt_gripper_pose * (offset)
        gripper_to_peg_dist = torch.linalg.norm(
            gripper_pos - tgt_gripper_pose.p, axis=1
        )

        reaching_reward = 1 - torch.tanh(4.0 * gripper_to_peg_dist)

        # check with max_angle=20 to ensure gripper isn't grasping peg at an awkward pose
        is_grasped = self.agent.is_grasping(self.peg, max_angle=20)
        reward = reaching_reward + is_grasped

        # Stage 3: Orient the grasped peg properly towards the hole

        # pre-insertion award, encouraging both the peg center and the peg head to match the yz coordinates of goal_pose
        peg_head_wrt_goal = self.goal_pose.inv() * self.peg_head_pose
        peg_head_wrt_goal_yz_dist = torch.linalg.norm(
            peg_head_wrt_goal.p[:, 1:], axis=1
        )
        peg_wrt_goal = self.goal_pose.inv() * self.peg.pose
        peg_wrt_goal_yz_dist = torch.linalg.norm(peg_wrt_goal.p[:, 1:], axis=1)

        pre_insertion_reward = 3 * (
            1
            - torch.tanh(
                0.5 * (peg_head_wrt_goal_yz_dist + peg_wrt_goal_yz_dist)
                + 4.5 * torch.maximum(peg_head_wrt_goal_yz_dist, peg_wrt_goal_yz_dist)
            )
        )
        reward += pre_insertion_reward * is_grasped
        # stage 3 passes if peg is correctly oriented in order to insert into hole easily
        pre_inserted = (peg_head_wrt_goal_yz_dist < 0.01) & (
            peg_wrt_goal_yz_dist < 0.01
        )

        # Stage 4: Insert the peg into the hole once it is grasped and lined up
        peg_head_wrt_goal_inside_hole = self.box_hole_pose.inv() * self.peg_head_pose
        insertion_reward = 5 * (
            1
            - torch.tanh(
                5.0 * torch.linalg.norm(peg_head_wrt_goal_inside_hole.p, axis=1)
            )
        )
        reward += insertion_reward * (is_grasped & pre_inserted)

        reward[info["success"]] = 10

        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs, action, info) / 10
```
```

### mani_skill/envs/tasks/tabletop/pick_clutter_ycb.py

```
class PickClutterEnv(BaseEnv)
    """Base environment picking items out of clutter type of tasks. Flexibly supports using different configurations and object datasets"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_model(self, model_id)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _sample_target_objects(self)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
class PickClutterYCBEnv(PickClutterEnv)
    def _load_model(self, model_id)

```python
def _get_obs_extra(self, info: dict):

        return dict()
```
```

### mani_skill/envs/tasks/tabletop/pick_cube.py

```
class PickCubeEnv(BaseEnv)
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
class PickCubeSO100Env(PickCubeEnv)
    def __init__(self)
class PickCubeWidowXAIEnv(PickCubeEnv)
    def __init__(self)

```python
def _get_obs_extra(self, info: dict):
        # in reality some people hack is_grasped into observations by checking if the gripper can close fully or not
        obs = dict(
            is_grasped=info["is_grasped"],
            tcp_pose=self.agent.tcp_pose.raw_pose,
            goal_pos=self.goal_site.pose.p,
        )
        if "state" in self.obs_mode:
            obs.update(
                obj_pose=self.cube.pose.raw_pose,
                tcp_to_obj_pos=self.cube.pose.p - self.agent.tcp_pose.p,
                obj_to_goal_pos=self.goal_site.pose.p - self.cube.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        tcp_to_obj_dist = torch.linalg.norm(
            self.cube.pose.p - self.agent.tcp_pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)
        reward = reaching_reward

        is_grasped = info["is_grasped"]
        reward += is_grasped

        obj_to_goal_dist = torch.linalg.norm(
            self.goal_site.pose.p - self.cube.pose.p, axis=1
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        reward += place_reward * is_grasped

        qvel = self.agent.robot.get_qvel()
        if self.robot_uids in ["panda", "widowxai"]:
            qvel = qvel[..., :-2]
        elif self.robot_uids == "so100":
            qvel = qvel[..., :-1]
        static_reward = 1 - torch.tanh(5 * torch.linalg.norm(qvel, axis=1))
        reward += static_reward * info["is_obj_placed"]

        reward[info["success"]] = 5
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 5
```
```

### mani_skill/envs/tasks/tabletop/pick_cube_cfgs.py

```
"""PickCube-v1 is a basic/common task which defaults to using the panda robot. It is also used as a testing task to check whether a robot with manipulation
capabilities can be simulated and trained properly. The configs below set the pick cube task differently to ensure the cube is within reach of the robot tested
and the camera angles are reasonable."""
```

### mani_skill/envs/tasks/tabletop/pick_single_ycb.py

```
class PickSingleYCBEnv(BaseEnv)
    """**Task Description:**
Pick up a random object sampled from the [YCB dataset](https://www.ycbbenchmarks.com/) and move it to a random goal position

**Randomizations:**
- the object's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1]. It is placed flat on the table
-"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _after_reconfigure(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
            goal_pos=self.goal_site.pose.p,
            is_grasped=info["is_grasped"],
        )
        if "state" in self.obs_mode:
            obs.update(
                tcp_to_goal_pos=self.goal_site.pose.p - self.agent.tcp.pose.p,
                obj_pose=self.obj.pose.raw_pose,
                tcp_to_obj_pos=self.obj.pose.p - self.agent.tcp.pose.p,
                obj_to_goal_pos=self.goal_site.pose.p - self.obj.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        tcp_to_obj_dist = torch.linalg.norm(
            self.obj.pose.p - self.agent.tcp.pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)
        reward = reaching_reward

        is_grasped = info["is_grasped"]
        reward += is_grasped

        obj_to_goal_dist = torch.linalg.norm(
            self.goal_site.pose.p - self.obj.pose.p, axis=1
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        reward += place_reward * is_grasped

        reward += info["is_obj_placed"] * is_grasped

        static_reward = 1 - torch.tanh(
            5 * torch.linalg.norm(self.agent.robot.get_qvel()[..., :-2], axis=1)
        )
        reward += static_reward * info["is_obj_placed"] * is_grasped

        reward[info["success"]] = 6
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 6
```
```

### mani_skill/envs/tasks/tabletop/place_sphere.py

```
class PlaceSphereEnv(BaseEnv)
    """**Task Description:**
Place the sphere into the shallow bin.

**Randomizations:**
- The position of the bin and the sphere are randomized: The bin is initialized in [0, 0.1] x [-0.1, 0.1],
and the sphere is initialized in [-0.1, -0.05] x [-0.1, 0.1]

**Success Conditions:**
- The sphere is placed on"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _build_bin(self, radius)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            is_grasped=info["is_obj_grasped"],
            tcp_pose=self.agent.tcp.pose.raw_pose,
            bin_pos=self.bin.pose.p,
        )
        if "state" in self.obs_mode:
            obs.update(
                obj_pose=self.obj.pose.raw_pose,
                tcp_to_obj_pos=self.obj.pose.p - self.agent.tcp.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # reaching reward
        tcp_pose = self.agent.tcp.pose.p
        obj_pos = self.obj.pose.p
        obj_to_tcp_dist = torch.linalg.norm(tcp_pose - obj_pos, axis=1)
        reward = 2 * (1 - torch.tanh(5 * obj_to_tcp_dist))

        # grasp and place reward
        obj_pos = self.obj.pose.p
        self.bin.pose.p
        bin_top_pos = self.bin.pose.p.clone()
        bin_top_pos[:, 2] = bin_top_pos[:, 2] + self.block_half_size[0] + self.radius
        obj_to_bin_top_dist = torch.linalg.norm(bin_top_pos - obj_pos, axis=1)
        place_reward = 1 - torch.tanh(5.0 * obj_to_bin_top_dist)
        reward[info["is_obj_grasped"]] = (4 + place_reward)[info["is_obj_grasped"]]

        # ungrasp and static reward
        gripper_width = (self.agent.robot.get_qlimits()[0, -1, 1] * 2).to(self.device)
        is_obj_grasped = info["is_obj_grasped"]
        ungrasp_reward = (
            torch.sum(self.agent.robot.get_qpos()[:, -2:], axis=1) / gripper_width
        )
        ungrasp_reward[
            ~is_obj_grasped
        ] = 16.0  # give ungrasp a bigger reward, so that it exceeds the robot static reward and the gripper can close
        v = torch.linalg.norm(self.obj.linear_velocity, axis=1)
        av = torch.linalg.norm(self.obj.angular_velocity, axis=1)
        static_reward = 1 - torch.tanh(v * 10 + av)
        robot_static_reward = self.agent.is_static(
            0.2
        )  # keep the robot static at the end state, since the sphere may spin when being placed on top
        reward[info["is_obj_on_bin"]] = (
            6 + (ungrasp_reward + static_reward + robot_static_reward) / 3.0
        )[info["is_obj_on_bin"]]

        # success reward
        reward[info["success"]] = 13
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        max_reward = 13.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/plug_charger.py

```
class PlugChargerEnv(BaseEnv)
    """**Task Description:**
The robot must pick up one of the misplaced shapes on the board/kit and insert it into the correct empty slot.

**Randomizations:**
- The charger position is randomized on the XY plane on top of the table. The rotation is also randomized
- The receptacle position is randomized """
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _build_charger(self, peg_size, base_size, gap)
    def _build_receptacle(self, peg_size, receptacle_size, gap)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def charger_base_pose(self)
    def _compute_distance(self)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(tcp_pose=self.agent.tcp.pose.raw_pose)
        if self.obs_mode_struct.use_state:
            obs.update(
                charger_pose=self.charger.pose.raw_pose,
                receptacle_pose=self.receptacle.pose.raw_pose,
                goal_pose=self.goal_pose.raw_pose,
            )
        return obs
```
```

### mani_skill/envs/tasks/tabletop/poke_cube.py

```
class PokeCubeEnv(BaseEnv)
    """**Task Description:**
A simple task where the objective is to poke a red cube with a peg and push it to a target goal position.

**Randomizations:**
- the peg's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1]. It is placed flat along it's length on the table
- the"""
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def peg_head_pos(self)
    def peg_head_pose(self)
    def _initialize_episode(self, env_idx, options)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )

        if self.obs_mode_struct.use_state:
            obs.update(
                cube_pose=self.cube.pose.raw_pose,
                peg_pose=self.peg.pose.raw_pose,
                goal_pos=self.peg.pose.p,
                tcp_to_peg_pos=self.peg.pose.p - self.agent.tcp.pose.p,
                peg_to_cube_pos=self.cube.pose.p - self.peg.pose.p,
                cube_to_goal_pos=self.goal_region.pose.p - self.cube.pose.p,
                peghead_to_cube_pos=self.peg_head_pos - self.cube.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # reach peg
        tcp_pos = self.agent.tcp.pose.p
        tgt_tcp_pose = self.peg.pose
        tcp_to_peg_dist = torch.linalg.norm(tcp_pos - tgt_tcp_pose.p, axis=1)
        reached = tcp_to_peg_dist < 0.01
        reaching_reward = 2 * (1 - torch.tanh(5.0 * tcp_to_peg_dist))
        reward = reaching_reward

        # peg to cube
        angle_diff = info["angle_diff"]
        align_reward = 1 - torch.tanh(5.0 * angle_diff)
        head_to_cube_dist = info["head_to_cube_dist"]
        close_reward = 1 - torch.tanh(5.0 * head_to_cube_dist)
        is_peg_grasped = info["is_peg_grasped"] * reached
        reward[is_peg_grasped] = (4 + close_reward + align_reward)[is_peg_grasped]

        # cube to goal
        cube_to_goal_dist = torch.linalg.norm(
            self.goal_region.pose.p - self.cube.pose.p, axis=1
        )
        place_reward = 1 - torch.tanh(5 * cube_to_goal_dist)
        is_peg_cube_fit = info["is_peg_cube_fit"] * is_peg_grasped
        reward[is_peg_cube_fit] = (7 + place_reward)[is_peg_cube_fit]

        static_reward = 1 - torch.tanh(
            5 * torch.linalg.norm(self.agent.robot.get_qvel()[..., :-2], axis=1)
        )
        reward[info["is_cube_placed"]] += static_reward[info["is_cube_placed"]]

        reward[info["success"]] = 10
        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        max_reward = 10.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/pull_cube.py

```
class PullCubeEnv(BaseEnv)
    """**Task Description:**
A simple task where the objective is to pull a cube onto a target.

**Randomizations:**
- the cube's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1].
- the target goal region is marked by a red and white target. The position of the target is """
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
            goal_pos=self.goal_region.pose.p,
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                obj_pose=self.obj.pose.raw_pose,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        # grippers should close and pull from behind the cube, not grip it
        # distance to backside of cube (+ 2*0.005) sufficiently encourages this
        tcp_pull_pos = self.obj.pose.p + torch.tensor(
            [self.cube_half_size + 2 * 0.005, 0, 0], device=self.device
        )
        tcp_to_pull_pose = tcp_pull_pos - self.agent.tcp.pose.p
        tcp_to_pull_pose_dist = torch.linalg.norm(tcp_to_pull_pose, axis=1)
        reaching_reward = 1 - torch.tanh(5 * tcp_to_pull_pose_dist)
        reward = reaching_reward

        reached = tcp_to_pull_pose_dist < 0.01
        obj_to_goal_dist = torch.linalg.norm(
            self.obj.pose.p[..., :2] - self.goal_region.pose.p[..., :2], axis=1
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        reward += place_reward * reached

        reward[info["success"]] = 3
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        max_reward = 3.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/pull_cube_tool.py

```
class PullCubeToolEnv(BaseEnv)
    """**Task Description**
Given an L-shaped tool that is within the reach of the robot, leverage the
tool to pull a cube that is out of it's reach

**Randomizations**
- The cube's position (x,y) is randomized on top of a table in the region "<out of manipulator
reach, but within reach of tool>". It is pl"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _build_l_shaped_tool(self, handle_length, hook_length, width, height)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _get_obs_extra(self, info)
    def evaluate(self)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )

        if self.obs_mode_struct.use_state:
            obs.update(
                cube_pose=self.cube.pose.raw_pose,
                tool_pose=self.l_shape_tool.pose.raw_pose,
            )

        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):

        tcp_pos = self.agent.tcp.pose.p
        cube_pos = self.cube.pose.p
        tool_pos = self.l_shape_tool.pose.p
        robot_base_pos = self.agent.robot.get_links()[0].pose.p

        # Stage 1: Reach and grasp tool
        tool_grasp_pos = tool_pos + torch.tensor([0.02, 0, 0], device=self.device)
        tcp_to_tool_dist = torch.linalg.norm(tcp_pos - tool_grasp_pos, dim=1)
        reaching_reward = 2.0 * (1 - torch.tanh(5.0 * tcp_to_tool_dist))

        # Add specific grasping reward
        is_grasping = self.agent.is_grasping(self.l_shape_tool, max_angle=20)
        grasping_reward = 2.0 * is_grasping

        # Stage 2: Position tool behind cube
        ideal_hook_pos = cube_pos + torch.tensor(
            [-(self.hook_length + self.cube_half_size), -0.067, 0], device=self.device
        )
        tool_positioning_dist = torch.linalg.norm(tool_pos - ideal_hook_pos, dim=1)
        positioning_reward = 1.5 * (1 - torch.tanh(3.0 * tool_positioning_dist))
        tool_positioned = tool_positioning_dist < 0.05

        # Stage 3: Pull cube to workspace
        workspace_target = robot_base_pos + torch.tensor(
            [0.05, 0, 0], device=self.device
        )
        cube_to_workspace_dist = torch.linalg.norm(cube_pos - workspace_target, dim=1)
        initial_dist = torch.linalg.norm(
            torch.tensor(
                [self.arm_reach + 0.1, 0, self.cube_size / 2], device=self.device
            )
            - workspace_target,
            dim=1,
        )
        pulling_progress = (initial_dist - cube_to_workspace_dist) / initial_dist
        pulling_reward = 3.0 * pulling_progress * tool_positioned

        # Combine rewards with staging and grasping dependency
        reward = reaching_reward + grasping_reward
        reward += positioning_reward * is_grasping
        reward += pulling_reward * is_grasping

        # Penalties
        cube_pushed_away = cube_pos[:, 0] > (self.arm_reach + 0.15)
        reward[cube_pushed_away] -= 2.0

        # Success bonus
        if "success" in info:
            reward[info["success"]] += 5.0

        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        """
        Normalizes the dense reward by the maximum possible reward (success bonus)
        """
        max_reward = 5.0  # Maximum possible reward from success bonus
        dense_reward = self.compute_dense_reward(obs=obs, action=action, info=info)
        return dense_reward / max_reward
```
```

### mani_skill/envs/tasks/tabletop/push_cube.py

```
"""Code for a minimal environment/task with just a robot being loaded. We recommend copying this template and modifying as you need.

At a high-level, ManiSkill tasks can minimally be defined by how the environment resets, what agents/objects are
loaded, goal parameterization, and success conditions

Environment reset is comprised of running two functions, `self._reconfigure` and `self.initialize_episode`, which is auto
run by ManiSkill. As a user, you can override a number of functions that affect reconfiguration and episode initialization.

Reconfiguration will reset the entire environment scen"""
class PushCubeEnv(BaseEnv)
    """**Task Description:**
A simple task where the objective is to push and move a cube to a goal region in front of it

**Randomizations:**
- the cube's xy position is randomized on top of a table in the region [0.1, 0.1] x [-0.1, -0.1]. It is placed flat on the table
- the target goal region is marked """
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        # some useful observation info for solving the task includes the pose of the tcp (tool center point) which is the point between the
        # grippers of the robot
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
        if self.obs_mode_struct.use_state:
            # if the observation mode requests to use state, we provide ground truth information about where the cube is.
            # for visual observation modes one should rely on the sensed visual data to determine where the cube is
            obs.update(
                goal_pos=self.goal_region.pose.p,
                obj_pose=self.obj.pose.raw_pose,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        # We also create a pose marking where the robot should push the cube from that is easiest (pushing from behind the cube)
        tcp_push_pose = Pose.create_from_pq(
            p=self.obj.pose.p
            + torch.tensor([-self.cube_half_size - 0.005, 0, 0], device=self.device)
        )
        tcp_to_push_pose = tcp_push_pose.p - self.agent.tcp.pose.p
        tcp_to_push_pose_dist = torch.linalg.norm(tcp_to_push_pose, axis=1)
        reaching_reward = 1 - torch.tanh(5 * tcp_to_push_pose_dist)
        reward = reaching_reward

        # compute a placement reward to encourage robot to move the cube to the center of the goal region
        # we further multiply the place_reward by a mask reached so we only add the place reward if the robot has reached the desired push pose
        # This reward design helps train RL agents faster by staging the reward out.
        reached = tcp_to_push_pose_dist < 0.01
        obj_to_goal_dist = torch.linalg.norm(
            self.obj.pose.p[..., :2] - self.goal_region.pose.p[..., :2], axis=1
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        reward += place_reward * reached

        # Compute a z reward to encourage the robot to keep the cube on the table
        desired_obj_z = self.cube_half_size
        current_obj_z = self.obj.pose.p[..., 2]
        z_deviation = torch.abs(current_obj_z - desired_obj_z)
        z_reward = 1 - torch.tanh(5 * z_deviation)
        # We multiply the z reward by the place_reward and reached mask so that
        #   we only add the z reward if the robot has reached the desired push pose
        #   and the z reward becomes more important as the robot gets closer to the goal.
        reward += place_reward * z_reward * reached

        # assign rewards to parallel environments that achieved success to the maximum of 3.
        reward[info["success"]] = 4
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        # this should be equal to compute_dense_reward / max possible reward
        max_reward = 4.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/push_t.py

```
class WhiteTableSceneBuilder(TableSceneBuilder)
    def initialize(self, env_idx)
    def build(self)
class PushTEnv(BaseEnv)
    """**Task Description:**
A simulated version of the real-world push-T task from Diffusion Policy: https://diffusion-policy.cs.columbia.edu/

In this task, the robot needs to:
1. Precisely push the T-shaped block into the target region, and
2. Move the end-effector to the end-zone which terminates the e"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def quat_to_z_euler(self, quats)
    def quat_to_zrot(self, quats)
    def pseudo_render_intersection(self)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        # ee position is super useful for pandastick robot
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
        if self.obs_mode_struct.use_state:
            # state based gets info on goal position and t full pose - necessary to learn task
            obs.update(
                goal_pos=self.goal_tee.pose.p,
                obj_pose=self.tee.pose.raw_pose,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        # reward for overlap of the tees

        # legacy reward
        # reward = self.pseudo_render_reward()
        # Pose based reward below is preferred over legacy reward
        # legacy reward gets stuck in local maxs of 50-75% intersection
        # and then fails to promote large explorations to perfectly orient the T, for PPO algorithm

        # new pose based reward: cos(z_rot_euler) + function of translation, between target and goal both in [0,1]
        # z euler cosine similarity reward: -- quat_to_z_euler guarenteed to reutrn value from [0,2pi]
        tee_z_eulers = self.quat_to_z_euler(self.tee.pose.q)
        # subtract the goal z rotatation to get relative rotation
        rot_rew = (tee_z_eulers - self.goal_z_rot).cos()
        # cos output [-1,1], we want reward of 0.5
        reward = (((rot_rew + 1) / 2) ** 2) / 2

        # x and y distance as reward
        tee_to_goal_pose = self.tee.pose.p[:, 0:2] - self.goal_tee.pose.p[:, 0:2]
        tee_to_goal_pose_dist = torch.linalg.norm(tee_to_goal_pose, axis=1)
        reward += ((1 - torch.tanh(5 * tee_to_goal_pose_dist)) ** 2) / 2

        # giving the robot a little help by rewarding it for having its end-effector close to the tee center of mass
        tcp_to_push_pose = self.tee.pose.p - self.agent.tcp.pose.p
        tcp_to_push_pose_dist = torch.linalg.norm(tcp_to_push_pose, axis=1)
        reward += ((1 - torch.tanh(5 * tcp_to_push_pose_dist)).sqrt()) / 20

        # assign rewards to parallel environments that achieved success to the maximum of 3.
        reward[info["success"]] = 3
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        max_reward = 3.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/roll_ball.py

```
class RollBallEnv(BaseEnv)
    """**Task Description:**
A simple task where the objective is to push and roll a ball to a goal region at the other end of the table

**Randomizations:**
- The ball's xy position is randomized on top of a table in the region [0.2, 0.5] x [-0.4, 0.7]. It is placed flat on the table
- The target goal reg"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):

        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
        )
        if self.obs_mode_struct.use_state:
            obs.update(
                goal_pos=self.goal_region.pose.p,
                ball_pose=self.ball.pose.raw_pose,
                ball_vel=self.ball.linear_velocity,
                tcp_to_ball_pos=self.ball.pose.p - self.agent.tcp.pose.p,
                ball_to_goal_pos=self.goal_region.pose.p - self.ball.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: Array, info: dict):
        unit_vec = self.ball.pose.p - self.goal_region.pose.p
        unit_vec = unit_vec / torch.linalg.norm(unit_vec, axis=1, keepdim=True)
        tcp_hit_pose = Pose.create_from_pq(
            p=self.ball.pose.p + unit_vec * (self.ball_radius + 0.05),
        )
        tcp_to_hit_pose = tcp_hit_pose.p - self.agent.tcp.pose.p
        tcp_to_hit_pose_dist = torch.linalg.norm(tcp_to_hit_pose, axis=1)
        self.reached_status[tcp_to_hit_pose_dist < 0.04] = 1.0
        reaching_reward = 1 - torch.tanh(2 * tcp_to_hit_pose_dist)

        obj_to_goal_dist = torch.linalg.norm(
            self.ball.pose.p[..., :2] - self.goal_region.pose.p[..., :2], axis=1
        )

        reached_reward = 1 - torch.tanh(obj_to_goal_dist)

        reward = (
            20 * reached_reward * self.reached_status
            + reaching_reward * (1 - self.reached_status)
            + self.reached_status
        )

        reward[info["success"]] = 30.0
        return reward
```

```python
def compute_normalized_dense_reward(self, obs: Any, action: Array, info: dict):
        max_reward = 30.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/tasks/tabletop/stack_cube.py

```
class StackCubeEnv(BaseEnv)
    """**Task Description:**
The goal is to pick up a red cube and stack it on top of a green cube and let go of the cube without it falling

**Randomizations:**
- both cubes have their z-axis rotation randomized
- both cubes have their xy positions on top of the table scene randomized. The positions are s"""
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(tcp_pose=self.agent.tcp.pose.raw_pose)
        if "state" in self.obs_mode:
            obs.update(
                cubeA_pose=self.cubeA.pose.raw_pose,
                cubeB_pose=self.cubeB.pose.raw_pose,
                tcp_to_cubeA_pos=self.cubeA.pose.p - self.agent.tcp.pose.p,
                tcp_to_cubeB_pos=self.cubeB.pose.p - self.agent.tcp.pose.p,
                cubeA_to_cubeB_pos=self.cubeB.pose.p - self.cubeA.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # reaching reward
        tcp_pose = self.agent.tcp.pose.p
        cubeA_pos = self.cubeA.pose.p
        cubeA_to_tcp_dist = torch.linalg.norm(tcp_pose - cubeA_pos, axis=1)
        reward = 2 * (1 - torch.tanh(5 * cubeA_to_tcp_dist))

        # grasp and place reward
        cubeA_pos = self.cubeA.pose.p
        cubeB_pos = self.cubeB.pose.p
        goal_xyz = torch.hstack(
            [cubeB_pos[:, 0:2], (cubeB_pos[:, 2] + self.cube_half_size[2] * 2)[:, None]]
        )
        cubeA_to_goal_dist = torch.linalg.norm(goal_xyz - cubeA_pos, axis=1)
        place_reward = 1 - torch.tanh(5.0 * cubeA_to_goal_dist)

        reward[info["is_cubeA_grasped"]] = (4 + place_reward)[info["is_cubeA_grasped"]]

        # ungrasp and static reward
        gripper_width = (self.agent.robot.get_qlimits()[0, -1, 1] * 2).to(
            self.device
        )  # NOTE: hard-coded with panda
        is_cubeA_grasped = info["is_cubeA_grasped"]
        ungrasp_reward = (
            torch.sum(self.agent.robot.get_qpos()[:, -2:], axis=1) / gripper_width
        )
        ungrasp_reward[~is_cubeA_grasped] = 1.0
        v = torch.linalg.norm(self.cubeA.linear_velocity, axis=1)
        av = torch.linalg.norm(self.cubeA.angular_velocity, axis=1)
        static_reward = 1 - torch.tanh(v * 10 + av)
        reward[info["is_cubeA_on_cubeB"]] = (
            6 + (ungrasp_reward + static_reward) / 2.0
        )[info["is_cubeA_on_cubeB"]]

        reward[info["success"]] = 8

        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 8
```
```

### mani_skill/envs/tasks/tabletop/stack_pyramid.py

```
class StackPyramidEnv(BaseEnv)
    """**Task Description:**
- The goal is to pick up a red cube, place it next to the green cube, and stack the blue cube on top of the red and green cube without it falling off.

**Randomizations:**
- all cubes have their z-axis rotation randomized
- all cubes have their xy positions on top of the table """
    def __init__(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(tcp_pose=self.agent.tcp.pose.raw_pose)
        if "state" in self.obs_mode:
            obs.update(
                cubeA_pose=self.cubeA.pose.raw_pose,
                cubeB_pose=self.cubeB.pose.raw_pose,
                cubeC_pose=self.cubeC.pose.raw_pose,
                tcp_to_cubeA_pos=self.cubeA.pose.p - self.agent.tcp.pose.p,
                tcp_to_cubeB_pos=self.cubeB.pose.p - self.agent.tcp.pose.p,
                tcp_to_cubeC_pos=self.cubeC.pose.p - self.agent.tcp.pose.p,
                cubeA_to_cubeB_pos=self.cubeB.pose.p - self.cubeA.pose.p,
                cubeB_to_cubeC_pos=self.cubeC.pose.p - self.cubeB.pose.p,
                cubeA_to_cubeC_pos=self.cubeC.pose.p - self.cubeA.pose.p,
            )
        return obs
```
```

### mani_skill/envs/tasks/tabletop/turn_faucet.py

```
class TurnFaucetEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def current_angle(self)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            tcp_pose=self.agent.tcp.pose.raw_pose,
            target_angle_diff=self.target_angle_diff,
            target_joint_axis=self.target_joint_axis,
            target_link_pos=self.target_link_pos,
        )

        if "state" in self.obs_mode:
            angle_dist = self.target_angle - self.current_angle
            obs["angle_dist"] = angle_dist
        return obs
```
```

### mani_skill/envs/tasks/tabletop/two_robot_pick_cube.py

```
class TwoRobotPickCube(BaseEnv)
    """**Task Description:**
The goal is to pick up a red cube and lift it to a goal location. There are two robots in this task and the
goal location is out of reach of the left robot while the cube is out of reach of the right robot, thus the two robots must work together
to move the cube to the goal.

*"""
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def left_agent(self)
    def right_agent(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            left_arm_tcp=self.left_agent.tcp.pose.raw_pose,
            right_arm_tcp=self.right_agent.tcp.pose.raw_pose,
        )
        if "state" in self.obs_mode:
            obs.update(
                cube_pose=self.cube.pose.raw_pose,
                left_arm_tcp_to_cube_pos=self.cube.pose.p - self.left_agent.tcp.pose.p,
                right_arm_tcp_to_cube_pos=self.cube.pose.p
                - self.right_agent.tcp.pose.p,
                cube_to_goal_pos=self.goal_site.pose.p - self.cube.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # Stage 1: Reach and push cube to be near other robot
        tcp_to_obj_dist = torch.linalg.norm(
            self.cube.pose.p - self.left_agent.tcp.pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)

        # set a sub_goal here where we want the cube to first be pushed to close to the right arm robot
        # by moving cube past y = 0.05
        cube_to_other_side_reward = 1 - torch.tanh(
            5
            * (
                torch.max(
                    0.05 - self.cube.pose.p[:, 1], torch.zeros_like(reaching_reward)
                )
            )
        )
        reward = (reaching_reward + cube_to_other_side_reward) / 2

        # stage 1 passes if cube is near a sub-goal
        cube_at_other_side = self.cube.pose.p[:, 1] >= 0.0

        # Stage 2: reach and grasp cube with right robot and make left robot leave space
        tcp_to_obj_dist = torch.linalg.norm(
            self.cube.pose.p - self.right_agent.tcp.pose.p, axis=1
        )
        reaching_reward = 1 - torch.tanh(5 * tcp_to_obj_dist)
        stage_2_reward = reaching_reward

        # condition for good grasp: both fingers are at the same height and open
        self.right_agent: Panda
        right_tip_1_height = self.right_agent.finger1_link.pose.p[:, 2]
        right_tip_2_height = self.right_agent.finger2_link.pose.p[:, 2]
        tip_height_reward = 1 - torch.tanh(
            5 * torch.abs(right_tip_1_height - right_tip_2_height)
        )
        tip_width_reward = 1 - torch.tanh(
            5
            * torch.abs(
                torch.linalg.norm(
                    self.right_agent.finger1_link.pose.p
                    - self.right_agent.finger2_link.pose.p,
                    axis=1,
                )
                - 0.07
            )
        )
        tip_reward = (tip_height_reward + tip_width_reward) / 2
        stage_2_reward += tip_reward

        # make left arm move as close as possible to the y=-0.2 line
        left_arm_leave_reward = 1 - torch.tanh(
            5 * (self.left_agent.tcp.pose.p[:, 1] + 0.2).abs()
        )
        stage_2_reward += left_arm_leave_reward

        # stage 2 passes if cube is grasped
        is_grasped = self.right_agent.is_grasping(self.cube)
        stage_2_reward += 2 * is_grasped

        reward[cube_at_other_side] = 2 + stage_2_reward[cube_at_other_side]

        # Stage 3: bring cube towards goal
        obj_to_goal_dist = torch.linalg.norm(
            self.goal_site.pose.p - self.right_agent.tcp.pose.p, axis=1
        )
        place_reward = 1 - torch.tanh(5 * obj_to_goal_dist)
        stage_3_reward = 2 * place_reward

        # return left arm to original position
        left_qpos_reward = 1 - torch.tanh(
            torch.linalg.norm(
                self.left_agent.robot.get_qpos() - self.left_init_qpos, axis=1
            )
        )
        stage_3_reward += left_qpos_reward

        reward[is_grasped] = 8 + stage_3_reward[is_grasped]

        # stage 3 passes if object is near goal (within 0.25m) - intermediate reward
        is_obj_near = torch.logical_and(obj_to_goal_dist < 0.25, is_grasped)
        # Stage 4: reuse same reward as stage 3 but stronger incentive
        reward[is_obj_near] = 12 + 2 * stage_3_reward[is_obj_near]

        # stage 4 passes if object is placed
        is_obj_placed = info["is_obj_placed"]

        # Stage 5: keep robot static at the goal
        right_static_reward = 1 - torch.tanh(
            5 * torch.linalg.norm(self.right_agent.robot.get_qvel()[..., :-2], axis=1)
        )
        left_static_reward = 1 - torch.tanh(
            5 * torch.linalg.norm(self.left_agent.robot.get_qvel()[..., :-2], axis=1)
        )
        static_reward = (right_static_reward + left_static_reward) / 2

        reward[is_obj_placed] = 19 + static_reward[is_obj_placed]

        reward[info["success"]] = 21

        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 21
```
```

### mani_skill/envs/tasks/tabletop/two_robot_stack_cube.py

```
class TwoRobotStackCube(BaseEnv)
    """**Task Description:**
A collaborative task where two robot arms need to work together to stack two cubes. One robot must pick up the green cube and place it on the target region, while the other robot picks up the blue cube and stacks it on top of the green cube.

The cubes are initially positioned """
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def left_agent(self)
    def right_agent(self)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)

```python
def _get_obs_extra(self, info: dict):
        obs = dict(
            left_arm_tcp=self.left_agent.tcp.pose.raw_pose,
            right_arm_tcp=self.right_agent.tcp.pose.raw_pose,
        )
        if "state" in self.obs_mode:
            obs.update(
                goal_region_pos=self.goal_region.pose.p,
                cubeA_pose=self.cubeA.pose.raw_pose,
                cubeB_pose=self.cubeB.pose.raw_pose,
                left_arm_tcp_to_cubeA_pos=self.cubeA.pose.p
                - self.left_agent.tcp.pose.p,
                right_arm_tcp_to_cubeB_pos=self.cubeB.pose.p
                - self.right_agent.tcp.pose.p,
                cubeA_to_cubeB_pos=self.cubeB.pose.p - self.cubeA.pose.p,
            )
        return obs
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # Stage 1: Reach and grasp
        # reaching reward for both robots to their respective cubes
        cubeA_to_left_arm_tcp_dist = torch.linalg.norm(
            self.left_agent.tcp.pose.p - self.cubeA.pose.p, axis=1
        )
        right_arm_push_pose = Pose.create_from_pq(
            p=self.cubeB.pose.p
            + torch.tensor([0, self.cube_half_size[0] + 0.005, 0], device=self.device)
        )
        right_arm_to_push_pose_dist = torch.linalg.norm(
            right_arm_push_pose.p - self.right_agent.tcp.pose.p, axis=1
        )
        reach_reward = (
            1
            - torch.tanh(5 * cubeA_to_left_arm_tcp_dist)
            + 1
            - torch.tanh(5 * right_arm_to_push_pose_dist)
        ) / 2

        # grasp reward for left robot which needs to lift cubeA up eventually
        cubeA_pos = self.cubeA.pose.p
        cubeB_pos = self.cubeB.pose.p
        reward = (reach_reward + info["is_cubeA_grasped"]) / 2

        # pass condition for stage 1
        place_stage_reached = info["is_cubeA_grasped"]

        # Stage 2: Place bottom cube and still hold to cube A
        # place reward for bottom cube (cube B)
        cubeB_to_goal_dist = torch.linalg.norm(
            cubeB_pos[:, :2] - self.goal_region.pose.p[..., :2], axis=1
        )
        place_reward = 1 - torch.tanh(5 * cubeB_to_goal_dist)
        stage_2_reward = place_reward + info["is_cubeA_grasped"]
        reward[place_stage_reached] = 2 + stage_2_reward[place_stage_reached] / 2

        # pass condition for stage 2
        cubeB_placed_and_cubeA_grasped = info["cubeB_placed"] * info["is_cubeA_grasped"]

        # Stage 3: Place top cube while moving right arm away to give left arm space
        # place reward for top cube (cube A)
        goal_xyz = torch.hstack(
            [cubeB_pos[:, :2], (cubeB_pos[:, 2] + self.cube_half_size[2] * 2)[:, None]]
        )
        cubeA_to_goal_dist = torch.linalg.norm(goal_xyz - cubeA_pos, axis=1)
        place_reward = 1 - torch.tanh(5 * cubeA_to_goal_dist)

        # move right arm as close as possible to the y=0.2 line
        right_arm_leave_reward = 1 - torch.tanh(
            5 * (self.right_agent.tcp.pose.p[:, 1] - 0.2).abs()
        )
        stage_3_reward = place_reward * 2 + right_arm_leave_reward
        reward[cubeB_placed_and_cubeA_grasped] = (
            4 + stage_3_reward[cubeB_placed_and_cubeA_grasped]
        )
        # pass condition for stage 3
        cubes_placed = info["is_cubeA_on_cubeB"] * info["cubeB_placed"]
        # Stage 4: get both robots to stop grasping
        gripper_width = (self.left_agent.robot.get_qlimits()[0, -1, 1] * 2).to(
            self.device
        )  # NOTE: hard-coded with panda
        ungrasp_reward_left = (
            torch.sum(self.left_agent.robot.get_qpos()[:, -2:], axis=1) / gripper_width
        )
        ungrasp_reward_left[~info["is_cubeA_grasped"]] = 1.0
        ungrasp_reward_right = (
            torch.sum(self.right_agent.robot.get_qpos()[:, -2:], axis=1) / gripper_width
        )
        ungrasp_reward_right[~info["is_cubeB_grasped"]] = 1.0

        reward[cubes_placed] = (
            8 + (ungrasp_reward_left + ungrasp_reward_right)[cubes_placed] / 2
        )

        reward[info["success"]] = 10

        return reward
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        return self.compute_dense_reward(obs=obs, action=action, info=info) / 10
```
```

### mani_skill/envs/template.py

```
"""Code for a minimal environment/task with just a robot being loaded. We recommend copying this template and modifying as you need.

At a high-level, ManiSkill tasks can minimally be defined by what agents/actors are
loaded, how agents/actors are randomly initialized during env resets, how goals are randomized and parameterized in observations, and success conditions

Environment reset is comprised of running two functions, `self._reconfigure` and `self.initialize_episode`, which is auto
run by ManiSkill. As a user, you can override a number of functions that affect reconfiguration and episode i"""
class CustomEnv(BaseEnv)
    """Task Description
----------------
Add a task description here

Randomizations
--------------
- how is it randomized?
- how is that randomized?

Success Conditions
------------------
- what is done to check if this task is solved?

Visualization: link to a video/gif of the task being solved"""
    def __init__(self)
    def _default_sim_config(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _setup_sensors(self, options)
    def _load_lighting(self, options)
    def _initialize_episode(self, env_idx, options)
    def evaluate(self)
    def _get_obs_extra(self, info)
    def compute_dense_reward(self, obs, action, info)
    def compute_normalized_dense_reward(self, obs, action, info)
    def get_state_dict(self)
    def set_state_dict(self, state, env_idx)

```python
def _get_obs_extra(self, info: dict):
        # should return an dict of additional observation data for your tasks
        # this will be included as part of the observation in the "extra" key when obs_mode="state_dict" or any of the visual obs_modes
        # and included as part of a flattened observation when obs_mode="state". Moreover, you have access to the info object
        # which is generated by the `evaluate` function above
        return dict()
```

```python
def compute_dense_reward(self, obs: Any, action: torch.Tensor, info: dict):
        # you can optionally provide a dense reward function by returning a scalar value here. This is used when reward_mode="dense"
        # note that as everything is batched, you must return a batch of of self.num_envs rewards as done in the example below.
        # Moreover, you have access to the info object which is generated by the `evaluate` function above
        return torch.zeros(self.num_envs, device=self.device)
```

```python
def compute_normalized_dense_reward(
        self, obs: Any, action: torch.Tensor, info: dict
    ):
        # this should be equal to compute_dense_reward / max possible reward
        max_reward = 1.0
        return self.compute_dense_reward(obs=obs, action=action, info=info) / max_reward
```
```

### mani_skill/envs/utils/observations/__init__.py

```
class CameraObsTextures()
class ObservationModeStruct()
    """A dataclass describing what observation data is being requested by the user"""
    def use_state(self)
def parse_obs_mode_to_struct(obs_mode)
```

### mani_skill/envs/utils/observations/observations.py

```
"""Functions that map a observation to a particular format, e.g. mapping the raw images to rgbd or pointcloud formats"""
def sensor_data_to_pointcloud(observation, sensors)
```

### mani_skill/envs/utils/randomization/batched_rng.py

```
"""Code implementation for a batched random number generator. The goal is to enable seeding a batched random number generator with a batch of seeds to ensure randomization
in CPU simulators and GPU simulators are the same"""
class BatchedRNG(RandomState)
    def __init__(self, rngs)
    def from_seeds(cls, seeds, backend)
    def from_rngs(cls, rngs)
    def __getitem__(self, idx)
    def __setitem__(self, idx, value)
    def __getattribute__(self, item)
```

### mani_skill/envs/utils/randomization/camera.py

```
def make_camera_rectangular_prism(n, scale, center, theta, device)
def noised_look_at(eye, target, look_at_noise, view_axis_rot_noise, device)
```

### mani_skill/envs/utils/randomization/common.py

```
def uniform(low, high, size, device)
```

### mani_skill/envs/utils/randomization/pose.py

```
def random_quaternions(n, device, lock_x, lock_y, lock_z, bounds)
```

### mani_skill/envs/utils/randomization/samplers.py

```
"""Various sampling functions/classes for fast, vectorized sampling of e.g. object poses"""
class UniformPlacementSampler()
    """Uniform placement sampler that lets you sequentially sample data such that the data is within given bounds and
not too close to previously sampled data. This sampler is also batched so you can use this easily for GPU simulated tasks

Args:
    bounds: ((low1, low2, ...), (high1, high2, ...))
    bat"""
    def __init__(self, bounds, batch_size, device)
    def sample(self, radius, max_trials, append, verbose)
```

### mani_skill/envs/utils/rewards/common.py

```
def tolerance(x, lower, upper, margin, sigmoid, value_at_margin)
```

### mani_skill/envs/utils/system/backend.py

```
"""Utilities for determining the simulation backend and devices"""
class BackendInfo()
def parse_backend_device_id(backend)
def parse_sim_and_render_backend(sim_backend, render_backend)
```

### mani_skill/examples/benchmarking/envs/isaaclab/cartpole_state.py

```
class CartpoleEnvCfg(DirectRLEnvCfg)
class CartpoleBenchmarkEnv(DirectRLEnv)
    def __init__(self, cfg, render_mode)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_observations(self)
    def _get_rewards(self)
    def _get_dones(self)
    def _reset_idx(self, env_ids)

```python
def _get_observations(self) -> dict:
        obs = torch.cat(
            (
                self.joint_pos[:, self._pole_dof_idx[0]].unsqueeze(dim=1),
                self.joint_vel[:, self._pole_dof_idx[0]].unsqueeze(dim=1),
                self.joint_pos[:, self._cart_dof_idx[0]].unsqueeze(dim=1),
                self.joint_vel[:, self._cart_dof_idx[0]].unsqueeze(dim=1),
            ),
            dim=-1,
        )
        observations = {"policy": obs}
        return observations
```

```python
def _get_rewards(self) -> torch.Tensor:
        total_reward = torch.zeros((self.num_envs,), device=self.sim.device)
        return total_reward
```
```

### mani_skill/examples/benchmarking/envs/isaaclab/cartpole_visual.py

```
class CartpoleRGBCameraBenchmarkEnvCfg(DirectRLEnvCfg)
class CartpoleCameraBenchmarkEnv(DirectRLEnv)
    """Benchmark environment for CartPole task with a camera.

Modification from original:
- Remove reward / evaluation functions
- Support RGB+Depth and multiple camera setups"""
    def __init__(self, cfg, render_mode, camera_width, camera_height, num_cameras, obs_mode)
    def close(self)
    def _configure_gym_env_spaces(self)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_observations(self)
    def _get_rewards(self)
    def _get_dones(self)
    def _reset_idx(self, env_ids)

```python
def _get_observations(self) -> dict:
        # data_type = "rgb" if "rgb" in self.cfg.tiled_camera.data_types else "depth"
        # observations = {"policy": self._tiled_camera.data.output[data_type].clone()}
        observations = {"sensors": {}}
        for i in range(self.num_cameras):
            observations["sensors"][f"cam_{i}"] = {}
        for i, (cam, cfg) in enumerate(zip(self.tiled_cameras, self.tiled_camera_cfgs)):
            for data_type in self.data_types:
                observations["sensors"][f"cam_{i}"][data_type] = cam.data.output[data_type].clone()
        # if self.has_depth:
        #     for i, (cam, cfg) in enumerate(zip(self.tiled_depth_cameras, self.tiled_depth_camera_cfgs)):
        #         observations["sensors"][f"cam_{i}"]["depth"] = cam.data.output["depth"].clone()
        return observations
```

```python
def _get_rewards(self) -> torch.Tensor:
        total_reward = torch.zeros((self.num_envs,), device=self.sim.device)
        return total_reward
```
```

### mani_skill/examples/benchmarking/envs/isaaclab/franka.py

```
class FrankaEnvCfg(DirectRLEnvCfg)
class FrankaBenchmarkEnv(DirectRLEnv)
    def __init__(self, cfg, render_mode, camera_width, camera_height, num_cameras, obs_mode)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_dones(self)
    def _get_rewards(self)
    def _reset_idx(self, env_ids)
    def _get_visual_observations(self)
    def _get_observations(self)

```python
def _get_rewards(self) -> torch.Tensor:
        total_reward = torch.zeros((self.num_envs,), device=self.sim.device)
        return total_reward
```

```python
def _get_visual_observations(self) -> dict:
        observations = {"sensors": {}}
        for i in range(self.num_cameras):
            observations["sensors"][f"cam_{i}"] = {}
        for i, (cam, cfg) in enumerate(zip(self.tiled_cameras, self.tiled_camera_cfgs)):
            for data_type in self.data_types:
                observations["sensors"][f"cam_{i}"][data_type] = cam.data.output[data_type].clone()
        return observations
```

```python
def _get_observations(self) -> dict:
        dof_pos_scaled = (
            2.0
            * (self._robot.data.joint_pos - self.robot_dof_lower_limits)
            / (self.robot_dof_upper_limits - self.robot_dof_lower_limits)
            - 1.0
        )
        obs = torch.cat(
            (
                dof_pos_scaled,
                self._robot.data.joint_vel * self.cfg.dof_velocity_scale,
            ),
            dim=-1,
        )
        obs = {"state": torch.clamp(obs, -5.0, 5.0)}
        if self.obs_mode != "state":
            obs["sensors"] = self._get_visual_observations()["sensors"]
        return obs
```
```

### mani_skill/examples/benchmarking/envs/maniskill/cartpole.py

```
class CartPoleRobot(BaseAgent)
    def _controller_configs(self)
    def _load_articulation(self, initial_pose)
class CartPoleBalanceBenchmarkEnv(CartpoleBalanceEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _load_lighting(self, options)
    def compute_dense_reward(self, obs, action, info)

```python
def compute_dense_reward(self, obs, action, info):
        return torch.zeros(self.num_envs, device=self.device)
```
```

### mani_skill/examples/benchmarking/envs/maniskill/franka_move.py

```
class FrankaMoveBenchmarkEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _load_lighting(self, options)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```
```

### mani_skill/examples/benchmarking/envs/maniskill/franka_pick_cube.py

```
class FrankaPickCubeBenchmarkEnv(BaseEnv)
    def __init__(self)
    def _default_sim_config(self)
    def _default_sensor_configs(self)
    def _default_human_render_camera_configs(self)
    def _load_agent(self, options)
    def _load_scene(self, options)
    def _initialize_episode(self, env_idx, options)
    def _load_lighting(self, options)
    def evaluate(self)
    def _get_obs_extra(self, info)

```python
def _get_obs_extra(self, info: dict):
        return dict()
```
```

### mani_skill/examples/benchmarking/gpu_sim.py

```
class Args()
def main(args)
```

### mani_skill/examples/benchmarking/isaac_lab_gpu_sim.py

```
def main()
```

### mani_skill/examples/demo_random_action.py

```
class Args()
def main(args)
```

### mani_skill/trajectory/utils/actions/conversion.py

```
"""Utilities to convert actions between different control modes. Note that this code is specifically designed for the Franka Panda robot arm, it is not guaranteed to work for other robots."""
def qpos_to_pd_joint_delta_pos(controller, qpos)
def qpos_to_pd_joint_target_delta_pos(controller, qpos)
def qpos_to_pd_joint_vel(controller, qpos)
def compact_axis_angle_from_quaternion(quat)
def delta_pose_to_pd_ee_delta(controller, delta_pose, pos_only)
def from_pd_joint_pos_to_ee(output_mode, ori_actions, ori_env, env, render, pbar, verbose)
def from_pd_joint_pos(output_mode, ori_actions, ori_env, env, render, pbar, verbose)
def from_pd_joint_delta_pos(output_mode, ori_actions, ori_env, env, render, pbar, verbose)
```

### mani_skill/utils/scene_builder/robocasa/fixtures/handles.py

```
class Handle(MujocoObject)
    """Base class for all handles attached to cabinet/drawer panels

Args:
    name (str): Name of the handle

    xml (str): Path to the xml file of the handle

    panel_w (float): Width of the panel to attach the handle to

    panel_h (float): Height of the panel to attach the handle to

    texture (s"""
    def __init__(self, scene, name, xml, panel_w, panel_h, texture, orientation, length)
    def _get_components(self)
    def _create_handle(self, positions, sizes)
    def exclude_from_prefixing(self, inp)
    def _set_texture(self)
class BarHandle(Handle)
    """Creates a bar handle

Args:
    length (float): Length of the handle

    handle_pad (float): A minimum difference between handle length and cabinet panel height"""
    def __init__(self, length, handle_pad)
    def _get_components(self)
    def _create_handle(self)
class BoxedHandle(Handle)
    """Creates a boxed handle

Args:
    length (float): Length of the handle

    handle_pad (float):  A minimum difference between handle length and cabinet panel height"""
    def __init__(self, length, handle_pad)
    def _create_handle(self)
class KnobHandle(Handle)
    """Creates a knob handle"""
    def __init__(self, handle_pad)
    def _get_components(self)
    def _create_handle(self)
```

### mani_skill/utils/wrappers/action_repeat.py

```
class ActionRepeatWrapper(Wrapper)
    def __init__(self, env, repeat)
    def num_envs(self)
    def base_env(self)
    def step(self, action)
    def _update_dict_values(self, from_dict, to_dict, not_dones)
```

### tests/test_envs.py

```
def test_all_envs(env_id)
def test_envs_obs_modes(env_id, obs_mode)
def test_envs_obs_modes_without_cpu_gym_wrapper(env_id, obs_mode)
def test_env_control_modes(env_id, control_mode)
def test_env_seeded_reset()
def test_env_seeded_sequence_reset()
def test_env_raise_value_error_for_nan_actions()
def test_states(env_id)
def test_robots(env_id, robot_uids)
def test_multi_agent(env_id)
def test_envs_time_limit_typing()
```

### tests/test_gpu_envs.py

```
def make_vec(env_id, num_envs, env_kwargs)
def test_all_envs(env_id)
def test_envs_obs_modes(env_id, obs_mode)
def test_env_control_modes(env_id, control_mode)
def test_env_reconfiguration(env_id)
def test_seeded_then_unseeded_reset_keeps_episode_seed_batch_size()
def test_robots(env_id, robot_uids)
def test_multi_agent(env_id)
def test_partial_resets(env_id)
def test_timelimits()
def test_hidden_objs(env_id)
```

### tests/test_sim_state.py

```
def test_raw_sim_states()
def test_raw_heterogeneous_actor_sim_states()
def test_raw_heterogeneous_articulations_sim_states()
```

### tests/test_venv.py

```
def test_gymnasium_cpu_vecenv(env_id, obs_mode)
```