# unidexgrasp_2023

source: https://github.com/PKU-EPIC/UniDexGrasp


commit: 36c9bfcf7cedc987dd15e2384c548e51d5aadc21


## README

# UniDexGrasp
Official code for "**UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy**" *(CVPR 2023)*

[Project Page](https://pku-epic.github.io/UniDexGrasp/) | [Paper](https://arxiv.org/abs/2303.00938)


![image](./images/teaser.png)



### Diverse Proposal Generation for Dexterous Grasping

Please see [README](https://github.com/PKU-EPIC/UniDexGrasp/blob/main/dexgrasp_generation) in `dexgrasp_generation` folder.

### Execution Policy Learning for Dexterous Grasping

Please see [README](https://github.com/PKU-EPIC/UniDexGrasp/blob/main/dexgrasp_policy) in `dexgrasp_policy` folder.


## Citation

```
@article{xu2023unidexgrasp,
  title={UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy},
  author={Xu, Yinzhen and Wan, Weikang and Zhang, Jialiang and Liu, Haoran and Shan, Zikang and Shen, Hao and Wang, Ruicheng and Geng, Haoran and Weng, Yijia and Chen, Jiayi and others},
  journal={arXiv preprint arXiv:2303.00938},
  year={2023}
}
```

## License
This work and the dataset are licensed under [CC BY-NC 4.0][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png


## File tree (depth 3, assets pruned)

```
.gitignore
README.md
dexgrasp_generation/
  README.md
  configs/
    cm_net_config.yaml
    dataset/
    eval_config.yaml
    glow_config.yaml
    glow_joint_config.yaml
    ipdf_config.yaml
    model/
  network/
    eval.py
    models/
    train.py
    trainer.py
  requirements.txt
  scripts/
    generate_object_pc.py
    generate_object_pose.py
    generate_object_table_pc.py
  tests/
    visualize_data.py
    visualize_pcs_table.py
    visualize_result.py
  thirdparty/
    nflows/
    pytorch_kinematics/
  utils/
    __init__.py
    eval_utils.py
    global_utils.py
    hand_model.py
    interrupt_handler.py
    visualize.py
dexgrasp_policy/
  README.md
  dexgrasp/
    algo/
    algorithms/
    cfg/
    example_model/
    script/
    tasks/
    train.py
    utils/
  setup.py
```

## Config files (21)


### dexgrasp_generation/configs/cm_net_config.yaml

```yaml
defaults:
    - _self_
    - model: cm_net
    - dataset: cm_net_data
    - override hydra/hydra_logging: none
    - override hydra/job_logging: none

network_type: cm_net
use_DFCData: True
use_Shadow: True

# dirs
exp_dir: ./runs/exp_cm

# wandb
wandb_offline: True
wandb_debug_mode: True  # and only program error will be reported

# frequency
freq:
    step_epoch: 100
    save: 10000  # per iter
    plot: 100  # per iter
    test: 50000 # per iter

# optimization options
optimizer: Adam
weight_decay: 0.0001
learning_rate: 0.001
lr_policy: step
lr_gamma: 0.5 # lr decay rate
lr_step_size: 40
lr_clip: 0.00001 # min lr

# bn momentum adjustment
momentum_original: 0.1
momentum_decay: 0.5
momentum_step_size: 20  # = lr_step_size
momentum_min: 0.01

# training options
weight_init: xavier
total_epoch: 250
resume_epoch: -1

# device
cuda_id: 0

# data loader
num_workers: 1
batch_size: 16

# hydra
hydra:
    output_subdir: null

```

### dexgrasp_generation/configs/dataset/cm_net_data.yaml

```yaml
root_path: "data"
# Comment the line below to train on all categories. (i.e., do not specify the categories)
#categories: ["bottle"]
dataset_dir: "DFCData"
hand_global_trans: [0, -0.7, 0.2]
hand_global_rotation_xyz: [-1.57, 0, 3.14]

##### DFCData #####
num_obj_points: 1024
num_hand_points: 1024

# shadow_hand_mesh_dir: "shadow_urdf/sr_grasp_description/meshes"
# shadow_urdf_path: "shadow_urdf/sr_grasp_description/urdf/shadowhand.urdf"
shadow_hand_mesh_dir: "mjcf/meshes"
shadow_urdf_path: "mjcf/shadow_hand.xml"

perturb: True
fps: True
```

### dexgrasp_generation/configs/dataset/eval_data.yaml

```yaml
root_path: "data"
# Comment the line below to train on all categories. (i.e., do not specify the categories)
#categories: ["bottle"]
dataset_dir: "DFCData"
hand_global_trans: [0, -0.7, 0.2]
hand_global_rotation_xyz: [-1.57, 0, 3.14]

##### DFCData #####
num_obj_points: 1024
num_hand_points: 1024

# shadow_hand_mesh_dir: "shadow_urdf/sr_grasp_description/meshes"
# shadow_urdf_path: "shadow_urdf/sr_grasp_description/urdf/shadowhand.urdf"
shadow_hand_mesh_dir: "mjcf/meshes"
shadow_urdf_path: "mjcf/shadow_hand.xml"

fps: True
```

### dexgrasp_generation/configs/dataset/glow_data.yaml

```yaml
root_path: "data"
# Comment the line below to train on all categories. (i.e., do not specify the categories)
#categories: ["bottle"]
dataset_dir: "DFCData"
hand_global_trans: [0, -0.7, 0.2]
hand_global_rotation_xyz: [-1.57, 0, 3.14]

##### DFCData #####
num_obj_points: 3000
num_hand_points: 1024

# shadow_hand_mesh_dir: "shadow_urdf/sr_grasp_description/meshes"
# shadow_urdf_path: "shadow_urdf/sr_grasp_description/urdf/shadowhand.urdf"
shadow_hand_mesh_dir: "mjcf/meshes"
shadow_urdf_path: "mjcf/shadow_hand.xml"

fps: False
```

### dexgrasp_generation/configs/dataset/ipdf_data.yaml

```yaml
root_path: "data"
# Comment the line below to train on all categories. (i.e., do not specify the categories)
#categories: ["bottle"]
dataset_dir: "DFCData"
hand_global_trans: [0, -0.7, 0.2]
hand_global_rotation_xyz: [-1.57, 0, 3.14]

##### DFCData #####
num_obj_points: 1024
num_hand_points: 1024

# shadow_hand_mesh_dir: "shadow_urdf/sr_grasp_description/meshes"
# shadow_urdf_path: "shadow_urdf/sr_grasp_description/urdf/shadowhand.urdf"
shadow_hand_mesh_dir: "mjcf/meshes"
shadow_urdf_path: "mjcf/shadow_hand.xml"

fps: True
```

### dexgrasp_generation/configs/eval_config.yaml

```yaml
defaults:
    - _self_
    - dataset: eval_data
    - override hydra/hydra_logging: none
    - override hydra/job_logging: none

models:
    rotation: 
        type: ipdf
        sample_num: 1
    pose: 
        type: glow
        sample_num: 1

tta:
    contact_net:
        type: cm_net
    batch_size: 50
    iterations: 300
    lr: 0.001
    normalize_factor: 60
    weight_cmap: 0.07
    weight_dis: 0.0
    weight_pen: 10000
    weight_spen: 10
    weight_tpen: 1000
    thres_dis: 0.01

q1:
    thres_pen: 0.005
    thres_tpen: 0.01
    m: 8
    mu: 1
    thres_contact: 0.01
    nms: True
    lambda_torque: 10

# dirs
exp_dir: ./runs/exp_tmp

# wandb
wandb_offline: True
wandb_debug_mode: True  # and only program error will be reported

resume_epoch: -1

# device
cuda_id: 0

# data loader
num_workers: 1
batch_size: 16
n_samples: 100

# hydra
hydra:
    output_subdir: null

```

### dexgrasp_generation/configs/glow_config.yaml

```yaml
defaults:
    - _self_
    - model: glow
    - dataset: glow_data
    - override hydra/hydra_logging: none
    - override hydra/job_logging: none

network_type: glow
use_DFCData: True
use_Shadow: True

# dirs
exp_dir: ./runs/exp_glow

# wandb
wandb_offline: True
wandb_debug_mode: True  # and only program error will be reported

# frequency
freq:
    step_epoch: 100
    save: 10000  # per iter
    plot: 100  # per iter
    test: 50000 # per iter

# optimization options
optimizer: Adam
weight_decay: 0.0001
learning_rate: 0.001
lr_policy: step
lr_gamma: 0.5 # lr decay rate
lr_step_size: 40
lr_clip: 0.00001 # min lr

# bn momentum adjustment
momentum_original: 0.1
momentum_decay: 0.5
momentum_step_size: 20  # = lr_step_size
momentum_min: 0.01

# training options
weight_init: xavier
total_epoch: 250
resume_epoch: -1

# device
cuda_id: 0

# data loader
num_workers: 4
batch_size: 64

# hydra
hydra:
    output_subdir: null

```

### dexgrasp_generation/configs/glow_joint_config.yaml

```yaml
defaults:
    - _self_
    - model: glow_joint
    - dataset: glow_data
    - override hydra/hydra_logging: none
    - override hydra/job_logging: none

network_type: glow
use_DFCData: True
use_Shadow: True

# dirs
exp_dir: ./runs/exp_glow

# wandb
wandb_offline: True
wandb_debug_mode: True  # and only program error will be reported

# frequency
freq:
    step_epoch: 100
    save: 10000  # per iter
    plot: 100  # per iter
    test: 50000 # per iter

# optimization options
optimizer: Adam
weight_decay: 0.0001
learning_rate: 0.001
lr_policy: step
lr_gamma: 0.5 # lr decay rate
lr_step_size: 40
lr_clip: 0.00001 # min lr

# bn momentum adjustment
momentum_original: 0.1
momentum_decay: 0.5
momentum_step_size: 20  # = lr_step_size
momentum_min: 0.01

# training options
weight_init: xavier
total_epoch: 2000
resume_epoch: -1

# device
cuda_id: 0

# data loader
num_workers: 1
batch_size: 32

# hydra
hydra:
    output_subdir: null

```

### dexgrasp_generation/configs/ipdf_config.yaml

```yaml
defaults:
    - _self_
    - model: ipdf
    - dataset: ipdf_data
    - override hydra/hydra_logging: none
    - override hydra/job_logging: none

network_type: ipdf
use_DFCData: True
use_Shadow: True

# dirs
exp_dir: ./runs/exp_ipdf

# wandb
wandb_offline: True
wandb_debug_mode: True  # and only program error will be reported

# frequency
freq:
    step_epoch: 100
    save: 10000  # per iter
    plot: 100  # per iter
    test: 75000 # per iter

# optimization options
optimizer: Adam
weight_decay: 0.0001
learning_rate: 0.001
lr_policy: step
lr_gamma: 0.5 # lr decay rate
lr_step_size: 40
lr_clip: 0.00001 # min lr

# bn momentum adjustment
momentum_original: 0.1
momentum_decay: 0.5
momentum_step_size: 20  # = lr_step_size
momentum_min: 0.01

# training options
weight_init: xavier
total_epoch: 250
resume_epoch: -1

# device
cuda_id: 0

# data loader
num_workers: 1
batch_size: 16

# hydra
hydra:
    output_subdir: null

```

### dexgrasp_generation/configs/model/cm_net.yaml

```yaml
network:
  out_channel: 10

loss_weight:
  contact_map: 1.0

```

### dexgrasp_generation/configs/model/glow.yaml

```yaml
joint_training: False

network:
  type: pointnet

flow:
  points: 22
  feature_dim: 1024
  hidden_dim: 64
  layer: 21
  block: 2


sample_num: 8

loss_weight:
  nll: 1.0
  cmap_loss: 1.0

```

### dexgrasp_generation/configs/model/glow_joint.yaml

```yaml
joint_training: True

rotation_net:
  type: ipdf
  ckpt_path: exp/temp_ipdf_train/ckpt/model_000001.pt

contact_net:
  type: cm_net
  ckpt_path: exp/temp_cmap_train/ckpt/model_000001.pt

network:
  type: pointnet

flow:
  points: 22
  feature_dim: 1024
  hidden_dim: 64
  layer: 21
  block: 2

tta:
  normalize_factor: 60
  weight_cmap: 0.02
  weight_dis: 0.0
  weight_pen: 500
  weight_spen: 10
  weight_tpen: 50
  thres_dis: 0.01

sample_num: 8

loss_weight:
  nll: 1.0
  cmap_loss: 1.0

```

### dexgrasp_generation/configs/model/ipdf.yaml

```yaml
network:
  type: pn_rotation_net

number_fourier_components: 1
mlp_layer_sizes: [256, 256, 256]
num_train_queries: 4096

loss_weight:
  nll: 1.0

```

### dexgrasp_generation/thirdparty/nflows/environment.yml

```yaml
# create:
# conda env create --file environment.yml
# update:
# conda env update --file environment.yml --prune
name: nflows

channels:
  - conda-forge
  - pytorch

dependencies:
  - autoflake
  - black
  - cudatoolkit
  - flake8
  - isort
  - jupyter
  - matplotlib
  - numpy
  - pip
  - pip:
    - torchtestcase
    - -e .  # install package in development mode
    - umnn
  - pytest
  - python
  - pytorch
  - pyyaml
  - tensorboard
  - tqdm
 

```

### dexgrasp_policy/dexgrasp/cfg/dagger/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  backbone_type: pn
  freeze_backbone: False
  pi_hid_sizes: [1024, 1024, 512, 512]
  vf_hid_sizes: [1024, 1024, 512, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 50000

  # training params
  cliprange: 0.2
  ent_coef: 0
  buffer_size: 2000
  nsteps: 1
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False
```

### dexgrasp_policy/dexgrasp/cfg/dagger_value/config.yaml

```yaml
seed: -1
vision: True
clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512, 512]
  vf_hid_sizes: [1024, 1024, 512, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 10000

  # training params
  cliprange: 0.2
  ent_coef: 0
  buffer_size: 2000
  nsteps: 1
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: True
    use_clipped_value_loss: True
    value_loss_coef: 1.0
    gamma: 0.96
    lam: 0.95
    clip_range: 0.2

  expert: [
    {
      name: '0',
      path: 'example_model/model.pt',
      object_code_dict: {
      'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
      }
    },
  ]

```

### dexgrasp_policy/dexgrasp/cfg/ppo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512, 512]
  vf_hid_sizes: [1024, 1024, 512, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500 # 500
  print_log: True

  # rollout params
  max_iterations: 10000

  # training params
  cliprange: 0.2
  ent_coef: 0
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False
```

### dexgrasp_policy/dexgrasp/cfg/shadow_hand_grasp.yaml

```yaml
graphics_device_id: 0
env:
  env_name: "shadow_hand_grasp"
  numEnvs: 1000
  envSpacing: 1.5
  episodeLength: 200 # 250
  enableDebugVis: False
  aggregateMode: 1

  random_prior: True
  random_time: True
  repose_z: True
  goal_cond: False

  object_code_dict: {
    'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
  }

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.5
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" 
  observationType: "full_state"
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [ 0, .002 ] # range for the white noise
      range_correlated: [ 0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [ 0., .05 ]
      range_correlated: [ 0, .015 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params:
      gravity:
        range: [ 0, 0.4 ]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [ 0.3, 3.0 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [ 0.75, 1.5 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping:
            range: [ 0.3, 3.0 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [ 0.75, 1.5 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [ 0, 0.01 ]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [ 0, 0.01 ]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.7, 1.3 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [ 0.95, 1.05 ]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.7, 1.3 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### dexgrasp_policy/dexgrasp/cfg/shadow_hand_random_load_vision.yaml

```yaml
graphics_device_id: 0
env:
  env_name: "shadow_hand_random_load_vision"
  numEnvs: 20 #9 5
  envSpacing: 10 #4.501  # will assert if spacing isn't sufficient
  episodeLength: 250
  enableDebugVis: False
  aggregateMode: 1

  random_prior: True
  random_time: True
  repose_z: True
  goal_cond: False

  random_load:
    sequential: True
    num_obj_per_env: 2  # maximum a * b * 4 + 1 # 257
    obj_width: 0.5
    a: 8 #4
    b: 8

  object_code_dict: {
    'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
  }


  numObservations: 300  # save states(excludes pc)  real_obs = 300 - 64 - 16 + 128 = 348
  vision:
    color:
      hand: [ 0.50, 0.50, 0.50 ] # gray
      # 0.6, 0.72, 0.98
      object: [ 1.00, 0.20, 0.20 ] # red
      goal: [ 0.50, 1.00, 0.35 ] # green
    pointclouds:
      numPresample: 65536
      numDownsample: 1024
      numEachPoint: 6
    camera:
      # relative to table center
      eye: [
        [ 0.0, 0.0, 0.55 ],
        [ 0.5, 0.0, 0.05 ],
        [ -0.5, 0.0, 0.05 ],
        [ 0.0, 0.5, 0.05 ],
        [ 0.0, -0.5, 0.05 ]
      ]
      lookat: [
        [ 0.01, 0.0, 0.05 ], # camera cannot look at accurate -z
        [ 0.0, 0.0, 0.05 ],
        [ 0.0, 0.0, 0.05 ],
        [ 0.0, 0.0, 0.05 ],
        [ 0.0, 0.0, 0.05 ],
      ]
    #      eye: [[0.2, -0.5, 0.4], [1.0, 0.2, 0.4], [0.2, 0.2, 0.8]]
    #      lookat: [[0.2, 3.5, 0.4], [-3.0, 0.2, 0.4], [0.2, 0.19, -1.2]]
    probe:
      num_probes: 0 # set this to 0
      width: 256
      height: 256
      eye: [
        [ 1.6, 0.0, 2.5 ],
      ]
      forward: [
        [ -0.8, 0.0, -2.0 ],
      ]
    bar:
      x_n: -1
      x_p: 1
      y_n: -1
      y_p: 1
      z_n: 0.61
      z_p: 1.3
      depth: 1.2

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.5
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [ 0, .002 ] # range for the white noise
      range_correlated: [ 0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [ 0., .05 ]
      range_correlated: [ 0, .015 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params:
      gravity:
        range: [ 0, 0.4 ]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [ 0.3, 3.0 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [ 0.75, 1.5 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping:
            range: [ 0.3, 3.0 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [ 0.75, 1.5 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [ 0, 0.01 ]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [ 0, 0.01 ]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.7, 1.3 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [ 0.95, 1.05 ]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.7, 1.3 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### dexgrasp_policy/dexgrasp/cfg/test_set_seen_cat.yaml

```yaml
    'core/remote-4df6e942001af26f16a077c4c0fc1181':[0.1],
    'core/bottle-244894af3ba967ccd957eaf7f4edb205':[0.08],
    'sem/SoapBottle-a5912dff7ed43650cf6ede117dc51e3d':[0.12],
    'sem/Vase-7a971531ff72a48d5706d1c54190f27a':[0.06],
    'sem/TableClock-fc5e57ba9bade79a86a499d1a4d80ea4':[0.1],
    'core/bottle-7bf5bbcff98f3d272561bfd89201eee3':[0.08],
    'core/bottle-cc399bb619ddddf7c13f8623d10d3404':[0.06],
    'sem/FoodItem-dac29f127351294b1df7f7df80536e76':[0.06],
    'core/camera-e57aa404a000df88d5d4532c6bb4bd2b':[0.06],
    'sem/Ship-426dad839f0b0ce8cad9e942409f4e39':[0.1],
    'sem/Flashlight-b8a2d0816b4e4dd9be0355c8334334a8':[0.06],
    'core/mug-d75af64aa166c24eacbe2257d0988c9c':[0.06],
    'sem/Piano-1f7301bb64526ce9d4cdf759998ef5c2':[0.1],
    'core/camera-f1540b3d6da38fbf1d908355fc20d631':[0.06],
    'sem/Ipod-ec6f37b5bb4ec4fe90cfcd62331f983':[0.06],
    'core/bottle-dc2c07ff617d1da0197a35146ee825cd':[0.06],
    'sem/ToyFigure-5d7cfdd7b9b1f314ccb9d5278825aef9':[0.08],
    'sem/Telephone-fb040b309c45cf3e85d624cfcd9a37a7':[0.06],
    'core/pistol-c3906de76406ea607086518c859a3e32':[0.08],
    'core/mug-7a8ea24474846c5c2f23d8349a133d2b':[0.06],
    'core/camera-5265ff657b9db80cafae29a76344a143':[0.06],
    'core/bottle-134c723696216addedee8d59893c8633':[0.08],
    'sem/Gun-5dfed385de1d8d56eae5cab1248d1ec6':[0.15],
    'core/remote-f3366e751820f0f77e1c85c5c15da7fb':[0.06],
    'sem/DrinkingUtensil-46ed9dad0440c043d33646b0990bb4a':[0.08],
    'sem/FoodItem-8991b73bfcfb51ea644be92422ae0abe':[0.08],
    'core/remote-29310c9b5bc234155eec6d8d24f1fde1':[0.12],
    'core/pillow-757be11305637a815b68a464a9cbfadf':[0.1],
    'sem/Bottle-83fd5e88eca47f1dab298e30fc6f45ba':[0.1],
    'sem/Clock-cf0208d1c19e8313cc63543a91bdd558':[0.1],
    'sem/Telephone-fb040b309c45cf3e85d624cfcd9a37a7':[0.08],
    'core/cellphone-d8071a38bb3dd8f097c8d78b9aede742':[0.12],
    'sem/SodaCan-744a65dd5c5fec90289ae987a66e0b37':[0.08],
    'core/jar-4b574003434d2ba041034a9ebee74b0c':[0.08],
    'core/bottle-950d6ca1d2b53ce52f71dfd07ef088cf':[0.12],
    'core/mug-68f4428c0b38ae0e2469963e6d044dfe':[0.12],
    'sem/Fruit-b095a1c41447e9da887d2d6e4a6617b3':[0.06],
    'sem/Bottle-20b7adb178ea2c71d8892a9c05c4aa0e':[0.06],
    'core/jar-58c9d6575d62fbaf12bc68f36f3bdd45':[0.06],
    'core/jar-2ddd2ef6c8ed56afbfec1075852e48f':[0.08],
    'sem/Bottle-6b810dbc89542fd8a531220b48579115':[0.08],
    'sem/LightBulb-9bc4b599b49a85f4cb1aec8410bf4988':[0.08],
    'core/jar-fa9e6aa9d67d5329e5c3c7284848bbfe':[0.06],
    'core/cellphone-7f6a27f44d8c9f2bbcde31492651e03':[0.08],
    'core/jar-8e7b2732b637559976fd405e95f98511':[0.08],
    'sem/Airplane-d0198fd427a58492dd8dc6d5a969eed':[0.12],
    'core/cellphone-4e2f684b3cebdbc344f470fdd42caac6':[0.12],
    'core/pillow-94e39fb5f01f15118998b3b64a143d42':[0.06],
    'core/can-f6316c6702c49126193d9e76bb15876':[0.06],
    'sem/Telephone-26f4aa1be6ff59ecc77d45d65dc3714':[0.1],
    'sem/Vase-c2bd95766b5cade2621a1668752723db':[0.06],
    'sem/Vase-1ee405020c96221ec3648f83bb1262ce':[0.08],
    'sem/ToyFigure-7cc11810eaa479e177e21aa92afd81b0':[0.08],
    'sem/CellPhone-345415c84aee5e1e99f14d125f819dd1':[0.08],
    'core/cellphone-57657c2b0d983a1658975870bb96a55c':[0.06],
    'core/camera-6d036fd1c70e5a5849493d905c02fa86':[0.08],
    'sem/Car-bf6e89e4fef8c547ff23af07d9064736':[0.1],
    'sem/Bottle-9f2bb4a157164af19a7c9976093a710d':[0.1],
    'sem/Piano-5574c469aae489c355005b4420ff0a5':[0.1],
    'core/bottle-ee007f1aac12fbe549a44197486ae284':[0.08],
    'sem/Candle-e045c2ee95aa4a6730c65e6f579cf287':[0.12],
    'core/jar-a88577a2ecffa8e858323e30458acc42':[0.08],
    'sem/Candle-a988e15b97a2c332ad8c1b052ddb26d0':[0.1],
    'sem/Radio-4bc977c07357c3be452f233142155aa6':[0.06],
    'sem/Bowl-9bc687dcffc25b955d20b6ca8788556a':[0.06],
    'sem/Bottle-83fd5e88eca47f1dab298e30fc6f45ba':[0.12],
    'core/bottle-3de5abb596766c5380dd154b5d9c087':[0.06],
    'sem/ComputerMouse-6ff315614cde9b42e58e58ea74bf6c0a':[0.06],
    'core/cellphone-6753572868705eacdd043998582f5fa':[0.1],
    'core/pistol-f4cf735786b69d7a5d0dded52efeb4fd':[0.06],
    'core/jar-d9a35f5bcc527fb3a982675e6ec522a0':[0.06],
    'sem/Pencil-8e41e635833699d72eb0505088d40b01':[0.08],
    'sem/SodaCan-38dd2a8d2c984e2b6c1cd53dbc9f7b8e':[0.06],
    'sem/Bottle-109d55a137c042f5760315ac3bf2c13e':[0.1],
    'sem/Vase-9097ce398b9700a27e561f865dc44fc5':[0.06],
    'core/remote-8e167ac56b1a437017d17fdfb5740281':[0.06],
    'core/bowl-d1addad5931dd337713f2e93cbeac35d':[0.08],
    'core/camera-98fc1afc8dec9773b10c2418bc64b141':[0.06],
    'sem/Telescope-a230fd500f22980ea4e0807819d752ad':[0.08],
    'sem/Bottle-7446fa250adf49c5e7ef9fff09638f8e':[0.1],
    'sem/CellPhone-b305303ce10b9caad197a144490f1a7c':[0.06],
    'sem/Camera-a006914d2b0c727bb837f8bbf7b05587':[0.06],
    'core/mug-9d8c711750a73b06ad1d789f3b2120d0':[0.06],
    'core/bottle-ad33ed7da4ef1b1cca18d703b8006093':[0.06],
    'sem/Detergent-c02d623423a67ed9bda72093f9b5aa73':[0.08],
    'core/pillow-15c98bfa322106a0d291861d5bc3e7c8':[0.06],
    'core/jar-eb344ece6d6669fe68dd306b8ea5e1c2':[0.06],
    'core/bottle-2d912be96504cb8cd5473a45f1da0225':[0.08],
    'sem/Bottle-621e786d6343d3aa2c96718b14a4add9':[0.12],
    'sem/TissueBox-fd9c40cd2ff2aab4a843bb865a04c01a':[0.06],
    'sem/ToyFigure-36b13c92d0d23f1433eddc4ad251356e':[0.15],
    'core/pistol-d4705e348edc0e405f4103077989355c':[0.1],
    'core/bottle-546111e6869f41aca577e3e5353dd356':[0.1],
    'sem/Bear-2f55f20282971f7125c70fb1df3f879b':[0.08],
    'core/bottle-ab51424e92acace2a1c3f37422b63004':[0.1],
    'sem/Snowman-dee9e56b9946037a226eabe1cca3e850':[0.06],
    'core/pistol-a8aee0ed266811e5cad3066323224194':[0.06],
    'sem/TissueBox-a65eb3d3898cdd9a48e2056fc010654d':[0.06],
    'core/mug-d38295b8d83e8cdec712af445786fe':[0.06],
    'core/jar-b7f03dab9501bad647be29e6263b8b5e':[0.06],
    'core/bottle-ac131ac1bbe3dd10846564a8a219239b':[0.15],
    'sem/Car-bf6e89e4fef8c547ff23af07d9064736':[0.06],
    'core/bowl-ae5c7d8a453d3ef736b0f2a1430e993a':[0.08],
    'sem/Showerhead-ac2cca058aadcea43321831d2245cf06':[0.15],
    'sem/Stapler-a5cafa3a913187dd8f9dd7647048a0c':[0.12],
    'core/jar-72cd871f8335f911fe9e40361c13f085':[0.06],
    'sem/Bottle-5ad47181a9026fc728cc22dce7529b69':[0.08],
    'core/mug-39361b14ba19303ee42cfae782879837':[0.08],
    'core/cellphone-dca3f5a8ab0b850c8c8e7e9e3310fb01':[0.1],
    'core/cellphone-609321c1351a955c1e1f8455cdf1c0bb':[0.06],
    'core/bottle-c3767df815e0e43e4c3a35cee92bb95b':[0.1],
    'sem/Motorcycle-9f5286f2bd2abcaab4e8c1a281d48fc8':[0.1],
    'core/camera-17a010f0ade4d1fd83a3e53900c6cbba':[0.08],
    'core/jar-31b0a01063a976104725f67267e31c89':[0.06],
    'sem/Piano-14755c2ee8e693aba508f621166382b0':[0.06],
    'sem/Bottle-d35ad6fe1db522f8593a35122199a8ce':[0.06],
    'sem/Radio-278964940bbd742bf260956be71b3917':[0.08],
    'core/bottle-3dbd66422997d234b811ffed11682339':[0.06],
    'sem/MilkCarton-f5b5a24adc6826ace41b639931f9ca1':[0.06],
    'core/bottle-f03f9704001d2055ab8a56962d772d13':[0.06],
    'core/bottle-5561fe6ad83a5000fc0eb7bdb358f874':[0.1],
    'sem/RubiksCube-f449ec743900234bb7f39bf08785db2f':[0.08],
    'sem/WallClock-b029b05ae3761f0b582ed853b74eeebb':[0.06],
    'core/bottle-114509277e76e413c8724d5673a063a6':[0.1],
    'core/bottle-13d991326c6e8b14fce33f1a52ee07f2':[0.08],
    'sem/Camera-5265ff657b9db80cafae29a76344a143':[0.08],
    'sem/PillBottle-81bbf3134d1ca27a58449bd132e3a3fe':[0.06],
    'sem/Battery-1d8fb5872696c64b62fb74d013fec4f1':[0.08],
    'sem/Telephone-4daa7c0f1d640f0375aa7f24a9b6003a':[0.06],
    'core/bottle-114509277e76e413c8724d5673a063a6':[0.12],
    'sem/Camera-4b99c1df215aa8e0fb1dc300162ac931':[0.06],
    'core/bottle-1071fa4cddb2da2fc8724d5673a063a6':[0.06],
    'core/pistol-e9ae98d8679409f8f52692247799a350':[0.15],
    'core/bottle-9eccbc942fc8c0011ee059e8e1a2ee9':[0.08],
    'sem/Fruit-e36e008ee74c2ffcf338a37c4adf9d76':[0.06],
    'sem/Car-d4586d32eec8134cba6d6cddf62a644b':[0.06],
    'sem/SodaCan-836ec249048214a6c8724d5673a063a6':[
```

### dexgrasp_policy/dexgrasp/cfg/test_set_unseen_cat.yaml

```yaml
    'sem/PowerStrip-6cb9ba94a63ff60888bf39e10d433fc8':[0.08],
    'sem/Microscope-3a6cd06d50e0f37e59ceafb827a4418d':[0.06],
    'sem/PowerStrip-c3f1944d562738f7daaccab222ac90bc':[0.12],
    'sem/Teapot-3d2cafbf9a6a2da44212ff51b27f0221':[0.08],
    'sem/TapeMeasure-d7ae45c05243250fb85d7b26e23c80bf':[0.06],
    'sem/Teapot-3d2cafbf9a6a2da44212ff51b27f0221':[0.06],
    'sem/Watch-e743856943ce4fa49a9248bc70f7492':[0.06],
    'sem/Cat-f0b4f696e91f59af18b14db3b83de9ff':[0.12],
    'sem/MediaChest-9ac71997e9eee1c1af5ada3edc49839':[0.06],
    'sem/Teapot-c7a70db33a8c900dab5b523beb03efcd':[0.06],
    'sem/CanOpener-ef6762a35438931aec2282dd8bc87a':[0.15],
    'sem/TapeMeasure-8e032ae0d6bf11795b8aa067abf14878':[0.06],
    'sem/Bus-418ecddf4297b8051138452c33de4a3d':[0.08],
    'sem/Cow-720025ba8f1ca815bec6be80de02c183':[0.08],
    'sem/Bus-418ecddf4297b8051138452c33de4a3d':[0.06],
    'sem/PicnicTableSet-66add7facfc1942886b3f898d28dd325':[0.06],
    'sem/Toaster-3ffbb0ab0f8da32f86271197b958e3d5':[0.08],
    'sem/Bus-28d8eafb888cd457e8784f880dac0f61':[0.1],
    'sem/TapeMeasure-948850694831c2644fdfafc90a1f296':[0.08],
    'sem/Teapot-93c6553dc3f2ad11012cc02986a86c3':[0.06],
    'sem/TapeMeasure-68c411e8b84a6f16ca6895dabdbc0ada':[0.06],
    'sem/Teapot-139af10e719186bddaa266217a65f9d7':[0.06],
    'sem/Microscope-3a6cd06d50e0f37e59ceafb827a4418d':[0.1],
    'sem/Cat-f0b4f696e91f59af18b14db3b83de9ff':[0.12],
    'sem/CanOpener-ef6762a35438931aec2282dd8bc87a':[0.12],
    'sem/TapeMeasure-948850694831c2644fdfafc90a1f296':[0.06],
    'sem/Cat-2163e8058aaa96a771879a51f4bce289':[0.06],
    'sem/Bus-418ecddf4297b8051138452c33de4a3d':[0.15],
    'sem/PicnicTableSet-66add7facfc1942886b3f898d28dd325':[0.06],
    'sem/Thermostat-c2b73966ca4024ef38b28f94c165f833':[0.08],
    'sem/Watch-e743856943ce4fa49a9248bc70f7492':[0.08],
    'sem/Mug-10f6e09036350e92b3f21f1137c3c347':[0.06],
    'sem/Donkey-b09e0a52bd3b1b4eab2bd7322386ffd':[0.12],
    'sem/Hat-78ffdd0f1440161ca7591d4119c4254f':[0.08],
    'sem/Thermostat-c2b73966ca4024ef38b28f94c165f833':[0.06],
    'sem/Microscope-c111643047f34e8c84fc81a3117e11ad':[0.08],
    'sem/Controller-61c6c6a47e5b9d34496c7671bf276db5':[0.1],
    'sem/Hat-78ffdd0f1440161ca7591d4119c4254f':[0.06],
    'sem/Watch-3a5351666689a7b2b788559e93c74a0f':[0.1],
    'sem/Microscope-3a6cd06d50e0f37e59ceafb827a4418d':[0.12],
    'sem/Plate-6907973366e2d8ca7f181d2694cd239b':[0.06],
    'sem/Toothbrush-3fd2220368ddb07112c1524f812438c7':[0.08],
    'sem/Bus-418ecddf4297b8051138452c33de4a3d':[0.12],
    'sem/TapeMeasure-e8951611e2c25ac1314b44839465ec00':[0.1],
    'sem/Kettle-9c5b0553b7a7088759ac5a8e79274552':[0.06],
    'sem/Thermostat-c2b73966ca4024ef38b28f94c165f833':[0.06],
    'sem/Toothbrush-3fd2220368ddb07112c1524f812438c7':[0.1],
    'sem/Cookie-a8e3118bec4c495f737a00f007529fbf':[0.06],
    'sem/Cow-720025ba8f1ca815bec6be80de02c183':[0.06],
    'sem/CanOpener-ef6762a35438931aec2282dd8bc87a':[0.15],
    'sem/Toaster-3ffbb0ab0f8da32f86271197b958e3d5':[0.06],
    'sem/Bus-28d8eafb888cd457e8784f880dac0f61':[0.1],
    'sem/Teapot-93c6553dc3f2ad11012cc02986a86c3':[0.06],
    'sem/Toothbrush-3fd2220368ddb07112c1524f812438c7':[0.15],
    'sem/Microscope-c111643047f34e8c84fc81a3117e11ad':[0.06],
    'sem/Cat-f0b4f696e91f59af18b14db3b83de9ff':[0.1],
    'sem/Toaster-2fb52b43697b9341b785a4ac4a0dbd73':[0.06],
    'sem/Toothbrush-3fd2220368ddb07112c1524f812438c7':[0.12],
    'sem/PowerStrip-c3f1944d562738f7daaccab222ac90bc':[0.12],
    'sem/Hat-d0919880bdf7eec8fe5dfc44db6ed8eb':[0.1],
    'sem/Watch-f57628258e99f63c5cd95682b31d27c1':[0.1],
    'sem/Hat-d0919880bdf7eec8fe5dfc44db6ed8eb':[0.08],
    'sem/Controller-61c6c6a47e5b9d34496c7671bf276db5':[0.08],
    'sem/PicnicTableSet-27a6dc6d930db4bf5da6aef87fc49e72':[0.06],
    'sem/Microscope-c111643047f34e8c84fc81a3117e11ad':[0.1],
    'sem/TapeMeasure-8f0a948bdcf8a65d43a73aba20837492':[0.06],
    'sem/Donkey-b09e0a52bd3b1b4eab2bd7322386ffd':[0.12],
    'sem/Hat-78ffdd0f1440161ca7591d4119c4254f':[0.08],
    'sem/Microscope-3a6cd06d50e0f37e59ceafb827a4418d':[0.08],
    'sem/Teapot-ef16485d8a6750e84212ff51b27f0221':[0.08],
    'sem/Tape-81fd4ab44df90d8ad84b8ba651dfb8ac':[0.06],
    'sem/Controller-61c6c6a47e5b9d34496c7671bf276db5':[0.1],
    'sem/Watch-f57628258e99f63c5cd95682b31d27c1':[0.12],
    'sem/Watch-3a5351666689a7b2b788559e93c74a0f':[0.08],
    'sem/TapeMeasure-948850694831c2644fdfafc90a1f296':[0.08],
    'sem/MediaChest-9ac71997e9eee1c1af5ada3edc49839':[0.06],
    'sem/Microscope-3a6cd06d50e0f37e59ceafb827a4418d':[0.1],
    'sem/Kettle-9c5b0553b7a7088759ac5a8e79274552':[0.06],
    'sem/Watch-3a5351666689a7b2b788559e93c74a0f':[0.06],
    'sem/Teapot-5a471458da447600fea9cf313bd7758b':[0.08],
    'sem/Cow-720025ba8f1ca815bec6be80de02c183':[0.08],
    'sem/Teapot-5a471458da447600fea9cf313bd7758b':[0.06],
    'sem/Plate-6907973366e2d8ca7f181d2694cd239b':[0.06],
    'sem/Bus-e299444f1a4c7457fa9ee9b3a7eba069':[0.06],
    'sem/Bus-28d8eafb888cd457e8784f880dac0f61':[0.08],
    'sem/Cow-67d466a374e88c3de80df3c23687288a':[0.08],
    'sem/Cookie-a8e3118bec4c495f737a00f007529fbf':[0.06],
    'sem/Cow-720025ba8f1ca815bec6be80de02c183':[0.1],
    'sem/Tape-81fd4ab44df90d8ad84b8ba651dfb8ac':[0.06],
    'sem/Teapot-ef16485d8a6750e84212ff51b27f0221':[0.06],
    'sem/Cow-67d466a374e88c3de80df3c23687288a':[0.06],
    'sem/Bus-418ecddf4297b8051138452c33de4a3d':[0.1],
    'sem/Toaster-3ffbb0ab0f8da32f86271197b958e3d5':[0.06],
    'sem/Mug-10f6e09036350e92b3f21f1137c3c347':[0.06],
    'sem/Kettle-9c5b0553b7a7088759ac5a8e79274552':[0.08],
    'sem/Teapot-139af10e719186bddaa266217a65f9d7':[0.08],
    'sem/Watch-f57628258e99f63c5cd95682b31d27c1':[0.1],
    'sem/Teapot-93c6553dc3f2ad11012cc02986a86c3':[0.08],
    'sem/Toothbrush-3fd2220368ddb07112c1524f812438c7':[0.15],
    'sem/Microscope-c111643047f34e8c84fc81a3117e11ad':[0.12],
```

## Python signatures and reward/observation bodies (133 files)


### dexgrasp_generation/network/train.py

```
def process_config(cfg, save)
def log_tensorboard(writer, mode, loss_dict, cnt, epoch)
def main(cfg)
def parse_args()
```

### dexgrasp_generation/network/trainer.py

```
def weights_init(init_type)
def get_scheduler(optimizer, cfg, it)
def get_optimizer(params, cfg)
class Trainer(Module)
    def __init__(self, cfg, logger)
    def log_string(self, out_str)
    def step_epoch(self)
    def resume(self)
    def save(self, name)
    def update(self, data)
    def test(self, data, save, no_eval)
```

### dexgrasp_generation/utils/hand_model.py

```
"""Last modified date: 2022.08.07
Author: mzhmxzh
Description: class HandModel"""
class AdditionalLoss(Module)
    def __init__(self, tta_cfg, device, num_obj_points, num_hand_points, cmap_net)
    def forward(self, points, plane_parameters, translation, hand_qpos)
    def tta_loss(self, hand_pose, points, cmap_pred, plane_parameters)
def cal_loss(hand, cmap_labels, cmap_pred, object_pc, plane_parameters, num_obj_points, verbose, weight_cmap, weight_pen, weight_dis, weight_spen, weight_tpen, thres_dis)
class HandModel()
    def __init__(self, mjcf_path, mesh_path, n_surface_points, contact_points_path, penetration_points_path, device)
    def __call__(self, hand_pose, object_pc, plane_parameters, with_meshes, with_surface_points, with_contact_candidates, with_penetration_keypoints, with_penetration)
def add_rotation_to_hand_pose(hand_pose, rotation)
```

### dexgrasp_generation/utils/interrupt_handler.py

```
class InterruptHandler(object)
    def __init__(self, sig)
    def __enter__(self)
    def __exit__(self, type, value, tb)
    def release(self)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/act.py

```
class ACTLayer(Module)
    """MLP Module to compute actions.
:param action_space: (gym.Space) action space.
:param inputs_dim: (int) dimension of network input.
:param use_orthogonal: (bool) whether to use orthogonal initialization.
:param gain: (float) gain of the output layer of the network."""
    def __init__(self, action_space, inputs_dim, use_orthogonal, gain, args)
    def forward(self, x, available_actions, deterministic)
    def get_probs(self, x, available_actions)
    def evaluate_actions(self, x, action, available_actions, active_masks)
    def evaluate_actions_trpo(self, x, action, available_actions, active_masks)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/cnn.py

```
class Flatten(Module)
    def forward(self, x)
class CNNLayer(Module)
    def __init__(self, obs_shape, hidden_size, use_orthogonal, use_ReLU, kernel_size, stride)
    def forward(self, x)
class CNNBase(Module)
    def __init__(self, args, obs_shape)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/distributions.py

```
class FixedCategorical(Categorical)
    def sample(self)
    def log_probs(self, actions)
    def mode(self)
class FixedNormal(Normal)
    def log_probs(self, actions)
    def entrop(self)
    def mode(self)
class FixedBernoulli(Bernoulli)
    def log_probs(self, actions)
    def entropy(self)
    def mode(self)
class Categorical(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x, available_actions)
class DiagGaussian(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain, config)
    def forward(self, x, available_actions)
class Bernoulli(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x)
class AddBias(Module)
    def __init__(self, bias)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/apis/train_rl.py

```
class EpisodicStatistics()
    def __init__(self, num_procs)
    def push(self, rewards, dones)
    def reset_history(self)
    def reset_current(self)
    def get_mean(self)
    def print_current(self)
    def print_history(self)
class EveryNSteps()
    def __init__(self, interval)
    def reset(self)
    def check(self, x)
    def standard(self, x)
def train_rl(agent, rollout, evaluator, env_cfg, replay, on_policy, work_dir, total_steps, warm_steps, n_steps, n_updates, n_checkpoint, n_eval, init_replay_buffers, expert_replay_buffers, expert_replay, tmp_replay, init_replay_with_split, eval_cfg, replicate_init_buffer, num_trajs_per_demo_file, m_steps, discrim_steps, rl_steps, is_GAIL, is_SAC_BC)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/brl/bc.py

```
"""Behavior cloning(BC)"""
class BC(BaseAgent)
    def __init__(self, policy_cfg, obs_shape, action_shape, action_space, batch_size)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/brl/bcq.py

```
"""Off-Policy Deep Reinforcement Learning without Exploration
    https://arxiv.org/abs/1812.02900"""
class BCQ(BaseAgent)
    def __init__(self, value_cfg, policy_vae_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, lmbda, num_random_action_train, num_random_action_eval, target_update_interval)
    def forward(self, obs)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/brl/cql.py

```
"""Conservative Q-Learning for Offline Reinforcement Learning:
    https://arxiv.org/pdf/2006.04779"""
class CQL(SAC)
    def __init__(self, num_action_sample, forward_block, automatic_regularization_tuning, lagrange_thresh, alpha_prime, temperature, min_q_weight, min_q_with_entropy, alpha_prime_optim_cfg, target_q_with_entropy, reward_scale)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/brl/td3_bc.py

```
"""A Minimalist Approach toOffline Reinforcement Learning:
    https://arxiv.org/pdf/2106.06860.pdf"""
class TD3_BC(TD3)
    def __init__(self, alpha, reward_scale)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/builder.py

```
def build_mfrl(cfg, default_args)
def build_brl(cfg, default_args)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/curl.py

```
class CURL(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, feature_dim)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/curl_old.py

```
class CURL(BaseAgent)
    def __init__(self, encoder_cfg, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, feature_dim, encoder_optim_cfg)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/gail.py

```
"""Soft Actor-Critic Algorithms and Applications:
    https://arxiv.org/abs/1812.05905
Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor:
   https://arxiv.org/abs/1801.01290"""
class GAIL(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, discriminator_cfg, obs_shape, action_shape, action_space, batch_size, discrim_batch, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg)
    def update_discriminator(self, expert_replay, tmp_replay)
    def expert_reward(self, obs, action)
    def update_parameters(self, memory, updates)

```python
def expert_reward(self, obs, action):
        obs = to_torch(obs, dtype='float32', device=self.device, non_blocking=True)
        action = to_torch(action, dtype='float32', device=self.device, non_blocking=True)
        exr = -torch.log(self.discriminator(obs, action))
        return exr.cpu().detach().numpy()
```
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/sac.py

```
"""Soft Actor-Critic Algorithms and Applications:
    https://arxiv.org/abs/1812.05905
Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor:
   https://arxiv.org/abs/1801.01290"""
class SAC(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/sac_bc.py

```
"""Soft Actor-Critic Algorithms and Applications:
    https://arxiv.org/abs/1812.05905
Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor:
   https://arxiv.org/abs/1801.01290"""
class SAC_BC(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, discrim_batch, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, alpha2)
    def update_parameters(self, memory, updates, expert_replay)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/methods/mfrl/td3.py

```
class TD3(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, action_noise, noise_clip, policy_update_interval)
    def update_parameters(self, memory, updates)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/backbones/mlp.py

```
class LinearMLP(Module)
    def __init__(self, mlp_spec, norm_cfg, bias, inactivated_output, pretrained, linear_init_cfg, norm_init_cfg)
    def forward(self, input)
    def init_weights(self, pretrained, linear_init_cfg, norm_init_cfg)
class ConvMLP(Module)
    def __init__(self, mlp_spec, norm_cfg, bias, inactivated_output, pretrained, conv_init_cfg, norm_init_cfg)
    def forward(self, input)
    def init_weights(self, pretrained, conv_init_cfg, norm_init_cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/backbones/nn_utils.py

```
class LinearBNReLU(Module)
    """Applies a 1D convolution over an input signal composed of several input planes,
optionally followed by batch normalization and ReLU activation."""
    def __init__(self, in_channels, out_channels, relu, bn)
    def forward(self, x)
class MLP(ModuleList)
    def __init__(self, in_channels, mlp_channels, bn, out_relu)
    def forward(self, x)
class SharedMLP(ModuleList)
    def __init__(self, in_channels, mlp_channels, ndim, bn)
    def forward(self, x)
class Conv1dBNReLU(Module)
    """Applies a 1D convolution over an input signal composed of several input planes,
optionally followed by batch normalization and ReLU activation."""
    def __init__(self, in_channels, out_channels, kernel_size, relu, bn)
    def forward(self, x)
class Conv2dBNReLU(Module)
    """Applies a 2D convolution (optionally with batch normalization and relu activation)
over an input signal composed of several input planes."""
    def __init__(self, in_channels, out_channels, kernel_size, relu, bn)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/backbones/pointnet.py

```
class PointBackbone(Module)
    def __init__(self)
    def forward(self, pcd)
    def forward_raw(self, pcd, state)
class SimplePointNetV0(PointBackbone)
    def __init__(self, conv_cfg, mlp_cfg, stack_frame, subtract_mean_coords, max_mean_mix_aggregation, with_activation)
    def forward_raw(self, pcd, mask)
class NaivePointNetV0(PointBackbone)
    def __init__(self, conv_cfg, state_cfg, mlp_cfg, stack_frame, subtract_mean_coords, max_mean_mix_aggregation, with_activation)
    def forward_raw(self, pcd, mask)
class PointNetV0(PointBackbone)
    def __init__(self, conv_cfg, mlp_cfg, stack_frame, subtract_mean_coords, max_mean_mix_aggregation, with_activation)
    def forward_raw(self, pcd, state, mask)
class SparseUnetV0(PointBackbone)
    def __init__(self, conv_cfg, mlp_cfg, stack_frame, subtract_mean_coords, max_mean_mix_aggregation, with_activation)
    def forward_raw(self, pcd, state, mask)
def getNaivePointNet(cfg)
def getPointNet(cfg)
def getPointNet_(cfg, backbone_cfg)
def getNewPointNet(cfg)
class PointNetWithInstanceInfoV0(PointBackbone)
    def __init__(self, pcd_pn_cfg, state_mlp_cfg, final_mlp_cfg, stack_frame, num_objs, transformer_cfg, with_activation, xyz_dim, mask_dim, state_dim)
    def forward(self, data)
def getPointNetWithInstanceInfo(cfg)
class SparseUnetWithInstanceInfoV0(PointBackbone)
    def __init__(self, pcd_pn_cfg, state_mlp_cfg, final_mlp_cfg, stack_frame, num_objs, transformer_cfg, with_activation, xyz_dim, mask_dim, state_dim)
    def forward(self, data)
def getSparseUnetWithInstanceInfo(cfg)
class PointNetDex(PointBackbone)
    def __init__(self, conv_cfg, mlp_cfg, stack_frame, subtract_mean_coords, max_mean_mix_aggregation, with_activation)
    def forward_raw(self, pcd, mask)
class PointNetWithInstanceInfoDex(PointBackbone)
    def __init__(self, pcd_pn_cfg, state_mlp_cfg, final_mlp_cfg, stack_frame, num_objs, transformer_cfg, with_activation, xyz_dim, mask_dim)
    def forward_raw(self, data)
def getPointNetWithInstanceInfoDex(cfg)
class SparseUnetWithInstanceInfoDex(PointBackbone)
    def __init__(self, pcd_pn_cfg, state_mlp_cfg, final_mlp_cfg, stack_frame, num_objs, transformer_cfg, with_activation, xyz_dim, mask_dim)
    def forward_raw(self, data)
def getSparseUnetWithInstanceInfoDex(cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/backbones/transformer.py

```
class TransformerBlock(Module)
    def __init__(self, attention_cfg, mlp_cfg, dropout)
    def forward(self, x, mask)
class TransformerEncoder(Module)
    def __init__(self, block_cfg, pooling_cfg, mlp_cfg, num_blocks)
    def forward(self, x, mask)
class TransformerDex(Module)
    def __init__(self, block_cfg, pooling_cfg, mlp_cfg, num_blocks)
    def forward(self, x, mask)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/backbones/vae.py

```
class CVAE(Module)
    def __init__(self, encoder_cfg, decoder_cfg, latent_dim, log_sig_min, log_sig_max)
    def forward(self, cond, var)
    def decode(self, cond, z)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/builder.py

```
def build(cfg, registry, default_args)
def build_dense_head(cfg)
def build_backbone(cfg)
def build_model(cfg, default_args)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/dense_heads/deterministic.py

```
class DeterministicHead(ExtendedModule)
    def __init__(self, scale_prior, bias_prior, noise_std)
    def forward(self, feature, num_actions)
    def clamp_action(self, action)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/dense_heads/gaussian.py

```
class GaussianHeadBase(ExtendedModule)
    def __init__(self, scale_prior, bias_prior, dim_action, epsilon)
    def uniform(self, sample_shape)
    def sample(self, mean, log_std, num_actions)
class GaussianHead(GaussianHeadBase)
    def __init__(self, scale_prior, bias_prior, dim_action, log_sig_min, log_sig_max, epsilon)
    def forward(self, feature, num_actions)
class SharedGaussianHead(GaussianHeadBase)
    def __init__(self, scale_prior, bias_prior, dim_action, epsilon)
    def forward(self, mean, num_actions)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/activation.py

```
class Clamp(Module)
    def __init__(self, min, max)
    def forward(self, x)
def build_activation_layer(cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/attention.py

```
def compute_attention(q, k, v, dropout, mask)
class MultiHeadedAttentionBase(Module)
    def __init__(self, embed_dim, num_heads, latent_dim, dropout)
    def _reset_parameters(self)
class AttentionPooling(MultiHeadedAttentionBase)
    def __init__(self, embed_dim, num_heads, latent_dim, dropout)
    def forward(self, x, mask)
class MultiHeadSelfAttention(MultiHeadedAttentionBase)
    def __init__(self, embed_dim, num_heads, latent_dim, dropout)
    def forward(self, x, mask)
def build_attention_layer(cfg, default_args)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/conv.py

```
class Conv2dAdaptivePadding(Conv2d)
    """Copy from https://github.com/open-mmlab/mmcv/blob/master/mmcv/cnn/bricks/conv2d_adaptive_padding.py
Implementation of 2D convolution in tensorflow with `padding` as "same",
which applies padding to input so that input image gets fully covered by filter and stride you specified.
For example:
    With"""
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias)
    def forward(self, x)
def build_conv_layer(cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/conv_module.py

```
class ConvModule(Module)
    """A conv block that bundles conv/norm/activation layers.

This block simplifies the usage of convolution layers, which are commonly
used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).
It is based upon three build methods: `build_conv_layer()`,
`build_norm_layer()` and `build_ac"""
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, conv_cfg, norm_cfg, act_cfg, inplace, with_spectral_norm, padding_mode, order)
    def norm(self)
    def init_weights(self)
    def forward(self, x, activate, norm)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/norm.py

```
def infer_abbr(class_type)
def build_norm_layer(cfg, num_features, postfix)
def is_norm(layer, exclude)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/padding.py

```
def build_padding_layer(cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/modules/weight_init.py

```
def constant_init(module, val, bias)
def xavier_init(module, gain, bias, distribution)
def normal_init(module, mean, std, bias)
def uniform_init(module, a, b, bias)
def kaiming_init(module, a, mode, nonlinearity, bias, distribution)
def caffe2_xavier_init(module, bias)
def bias_init_with_prob(prior_prob)
def build_init(cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/policy_network/continuous_policy.py

```
class ContinuousPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, num_actions, mode, detach_encoder)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/policy_network/vae_policy.py

```
class VAEPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action, decode)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/utils.py

```
def combine_obs_with_action(obs, action)
def get_kwargs_from_shape(obs_shape, action_shape)
def replace_placeholder_with_args(parameters)
def soft_update(target, source, tau)
def hard_update(target, source)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/networks/value_network/continuous_value.py

```
class ContinuousValue(ExtendedModule)
    def __init__(self, nn_cfg, obs_shape, action_shape, num_heads, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/optimizers/builder.py

```
def register_torch_optimizers()
def build_optimizer_constructor(cfg)
def build_optimizer(model, cfg)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/optimizers/default_constructor.py

```
class DefaultOptimizerConstructor()
    """Default constructor for optimizers.

By default each parameter share the same optimizer settings, and we
provide an argument ``paramwise_cfg`` to specify parameter-wise settings.
It is a dict and may contain the following fields:

- ``custom_keys`` (dict): Specified parameters-wise settings by keys."""
    def __init__(self, optimizer_cfg, paramwise_cfg)
    def _validate_cfg(self)
    def _is_in(self, param_group, param_group_list)
    def add_params(self, params, module, prefix, is_dcn_module)
    def __call__(self, model)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/external/web_utils.py

```
def check_url_exists(url)
def get_confirm_token(response)
def save_response_content(response, destination)
def get_google_file_index(file_url)
def md5sum(filename, block_size)
def check_md5sum(filename, md5, block_size)
def download_file_from_google_drive(file_url, destination, cached, md5)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/h5_utils.py

```
def load_h5_as_dict_array(h5)
def load_h5s_as_list_dict_array(h5)
def merge_h5_trajectory(h5_files, output_name)
def generate_chunked_h5_replay(h5_files, name, folder, num_files)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/hash_utils.py

```
def md5sum(filename, block_size)
def check_md5sum(filename, md5, block_size)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/base.py

```
class BaseFileHandler()
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
    def load_from_path(self, filepath, mode)
    def dump_to_path(self, obj, filepath, mode)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/csv_handler.py

```
class CSVHandler(BaseFileHandler)
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/pickle_handler.py

```
class PickleProtocol()
    def __init__(self, level)
    def __enter__(self)
    def __exit__(self)
class PickleHandler(BaseFileHandler)
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
    def load_from_path(self, filepath)
    def dump_to_path(self, obj, filepath)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/io.py

```
def load(file, file_format)
def dump(obj, file, file_format)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/utils.py

```
def serialize(obj)
def deserialize(obj)
def list_from_file(filename, prefix, offset, max_num)
def dict_from_file(filename, key_type, offset, max_num)
def dict_to_csv_table(x)
def csv_table_to_dict(x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/math/split_array.py

```
def split_num(num, n)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/collect_env.py

```
def get_PIL_version()
def collect_base_env()
def collect_env()
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/config.py

```
class ConfigDict(Dict)
    def __missing__(self, name)
    def __getattr__(self, name)
def add_args(parser, cfg, prefix)
class Config()
    """A facility for config and config files.
It supports common file formats as configs: python/json/yaml. The interface is the same as a dict object and also
allows access config values as attributes.

Example:
    >>> cfg = Config(dict(a=1, b=dict(b1=[0, 1])))
    >>> cfg.a
    1
    >>> cfg.b
    {'b1"""
    def _validate_py_syntax(filename)
    def _substitute_predefined_vars(filename, temp_config_name)
    def _file2dict(filename, use_predefined_variables)
    def _merge_a_into_b(a, b, allow_list_keys)
    def fromfile(filename, use_predefined_variables, import_custom_modules)
    def auto_argparser(description)
    def __init__(self, cfg_dict, cfg_text, filename)
    def filename(self)
    def text(self)
    def pretty_text(self)
    def __repr__(self)
    def __len__(self)
    def __getattr__(self, name)
    def __getitem__(self, name)
    def __setattr__(self, name, value)
    def __setitem__(self, name, value)
    def __iter__(self)
    def __getstate__(self)
    def __setstate__(self, state)
    def dump(self, file)
    def merge_from_dict(self, options, allow_list_keys)
class DictAction(Action)
    """argparse action to split an argument into KEY=VALUE form
on the first = and append to a dictionary. List options can
be passed as comma separated values, i.e 'KEY=V1,V2,V3', or with explicit
brackets, i.e. 'KEY=[V1,V2,V3]'. It also support nested brackets to build
list/tuple values. e.g. 'KEY=[(V1,V"""
    def _parse_int_float_bool(val)
    def _parse_iterable(val)
    def __call__(self, parser, namespace, values, option_string)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/logger.py

```
def get_logger(name, with_stream, log_file, log_level)
def get_root_logger(log_file, log_level)
def print_log(msg, logger, level)
def flush_print()
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/module_utils.py

```
def import_modules_from_strings(imports, allow_failed_imports)
def check_prerequisites(prerequisites, checker, msg_tmpl)
def requires_package(prerequisites)
def requires_executable(prerequisites)
def deprecated_api_warning(name_dict, cls_name)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/path_utils.py

```
def to_abspath(x)
def get_filename(x)
def get_dirname(x)
def get_filename_suffix(x)
def is_filepath(x)
def add_suffix_to_filename(x, suffix)
def replace_suffix(x, suffix)
def fopen(filepath)
def check_file_exist(filename, msg_tmpl)
def mkdir_or_exist(dir_name, mode)
def symlink(src, dst, overwrite)
def copy_folder(from_path, to_path, overwrite)
def copy_folders(source_dir, folder_list, target_dir, overwrite)
def scandir(dir_path, suffix, recursive)
def find_vcs_root(path, markers)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/process_utils.py

```
def format_memory_str(x, unit, number_only)
def get_total_memory(unit, number_only, init_pid)
def get_memory_list(unit, number_only, init_pid)
def get_memory_dict(unit, number_only, init_pid)
def get_subprocess_ids(init_pid)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/random_utils.py

```
def set_random_seed(seed)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/registry.py

```
class Registry()
    """A registry to map strings to classes.
Args:
    name (str): Registry name."""
    def __init__(self, name)
    def __len__(self)
    def __contains__(self, key)
    def __repr__(self)
    def name(self)
    def module_dict(self)
    def get(self, key)
    def _register_module(self, module_class, module_name, force)
    def register_module(self, name, force, module)
def build_from_cfg(cfg, registry, default_args)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/timer.py

```
def td_format(td_object)
def get_time_stamp()
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/checkpoint.py

```
"""Modified from https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/checkpoint.py"""
def load_state_dict(module, state_dict, strict, logger)
def load_url_dist(url, model_dir)
def get_torchvision_models()
def _load_checkpoint(filename, map_location)
def load_checkpoint(model, filename, map_location, strict, logger)
def weights_to_cpu(state_dict)
def _save_to_state_dict(module, destination, prefix, keep_vars)
def get_state_dict(module, destination, prefix, keep_vars)
def save_checkpoint(model, filename, optimizer, meta)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/cuda_utils.py

```
def get_gpu_memory_info(device, unit, number_only)
def get_gpu_memory_usage_by_process(process, device, unit, number_only)
def get_gpu_memory_usage_by_current_program(device, unit, number_only)
def get_gpu_utilization(device)
def get_cuda_info(device, unit, number_only)
def get_one_device(x)
def get_device(x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/distributed_utils.py

```
"""Modified from https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/dist_utils.py"""
def init_dist(launcher, backend)
def _init_dist_pytorch(backend)
def _init_dist_mpi(backend)
def _init_dist_slurm(backend, port)
def get_dist_info()
def master_only(func)
def allreduce_params(params, coalesce, bucket_size_mb)
def allreduce_grads(params, coalesce, bucket_size_mb)
def _allreduce_coalesced(tensors, world_size, bucket_size_mb)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/misc.py

```
def disable_gradients(network)
def worker_init_fn(worker_id)
def no_grad(f)
def run_with_mini_batch(function, data, batch_size)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/module_utils.py

```
class CustomDataParallel(DataParallel)
    def __init__(self)
    def __getitem__(self, name)
    def device(self)
class ExtendedModule(Module)
    def device(self)
    def __getitem__(self, name)
class BaseAgent(ExtendedModule)
    def __init__(self)
    def to_data_parallel(self, device_ids, output_device, axis)
    def to_normal(self)
    def recover_data_parallel(self)
    def is_data_parallel(self)
    def device(self)
    def forward(self, obs)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/ops.py

```
def masked_average(x, axis, mask, keepdim)
def masked_max(x, axis, mask, keepdim, empty_value)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/utils/torch/tensorboard/tensorboard_logger.py

```
class TensorboardLogger()
    def __init__(self, log_dir)
    def get_lr_tags(self, runner)
    def get_momentum_tags(self, runner)
    def is_scalar(val, include_np, include_torch)
    def get_loggable_tags(self, output, allow_scalar, allow_text, tags_to_skip, add_mode, eval)
    def log(self, tags, n_iter, eval)
    def close(self)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/maniskill_learn/version.py

```
def parse_version_info(version_str)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/mlp.py

```
class MLPLayer(Module)
    def __init__(self, input_dim, hidden_size, layer_N, use_orthogonal, use_ReLU)
    def forward(self, x)
class MLPBase(Module)
    def __init__(self, config, obs_shape, cat_self, attn_internal)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/model_3d.py

```
"""Full model"""
class PointNet2Feature(PointNet2ClassificationSSG)
    def _build_model(self)
    def forward(self, pointcloud)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/pointnet.py

```
class STN3d(Module)
    def __init__(self)
    def forward(self, x)
class STNkd(Module)
    def __init__(self, k)
    def forward(self, x)
class PointNetfeat(Module)
    def __init__(self, global_feat, feature_transform)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/rnn.py

```
class RNNLayer(Module)
    def __init__(self, inputs_dim, outputs_dim, recurrent_N, use_orthogonal)
    def forward(self, x, hxs, masks)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/sparseunet.py

```
class SparseUnetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, channels, block_repeat, pretrained_model_path, use_domain_discrimination)
    def forward(self, input_pc)
    def apply_voxelization_batch(self, pc)
```

### dexgrasp_policy/dexgrasp/algo/pn_utils/util.py

```
def init(module, weight_init, bias_init, gain)
def get_clones(module, N)
def check(input)
def masked_average(x, axis, mask, keepdim)
def masked_max(x, axis, mask, keepdim, empty_value)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger/dagger.py

```
class DAGGER()
    def __init__(self, vec_env, actor_class, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, buffer_size, init_noise_std, learning_rate, schedule, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, expert_chkpt_path, is_vision)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger/module.py

```
class PointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, pretrained_model_path)
    def forward(self, input_pc)
class TransPointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, state_dim, use_seg)
    def forward(self, input_pc)
class Actor(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations)
    def act_inference(self, observations)
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, buffer_size, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, actions, rewards, dones)
    def clear(self)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger_value/dagger.py

```
class DAGGERVALUE()
    def __init__(self, vec_env, actor_class, actor_critic_class, actor_critic_class_expert, num_transitions_per_env, num_learning_epochs, num_mini_batches, buffer_size, init_noise_std, learning_rate, schedule, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, expert_chkpt_path, is_vision)
    def get_all_checkpoints_in_dir(self, workdir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def expert_inference(self, current_obs)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger_value/module.py

```
class PointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, pretrained_model_path)
    def forward(self, input_pc)
class TransPointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, state_dim, use_seg)
    def forward(self, input_pc)
class Actor(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations)
    def act_inference(self, observations)
class ActorCriticDagger(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_withgrad(self, observations)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/dagger_value/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, buffer_size, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, actions, rewards, dones)
    def clear(self)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class PPORolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class PERBuffer()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, per_cfg, device)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def sample(self, batch_size)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/ppo/module.py

```
class PointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, pretrained_model_path)
    def forward(self, input_pc)
class TransPointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, state_dim, use_seg)
    def forward(self, input_pc)
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric, use_pc)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/ppo/ppo.py

```
class PPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, is_vision)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### dexgrasp_policy/dexgrasp/algorithms/rl/ppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/act.py

```
class ACTLayer(Module)
    """MLP Module to compute actions.
:param action_space: (gym.Space) action space.
:param inputs_dim: (int) dimension of network input.
:param use_orthogonal: (bool) whether to use orthogonal initialization.
:param gain: (float) gain of the output layer of the network."""
    def __init__(self, action_space, inputs_dim, use_orthogonal, gain, args)
    def forward(self, x, available_actions, deterministic)
    def get_probs(self, x, available_actions)
    def evaluate_actions(self, x, action, available_actions, active_masks)
    def evaluate_actions_trpo(self, x, action, available_actions, active_masks)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/cnn.py

```
class Flatten(Module)
    def forward(self, x)
class CNNLayer(Module)
    def __init__(self, obs_shape, hidden_size, use_orthogonal, use_ReLU, kernel_size, stride)
    def forward(self, x)
class CNNBase(Module)
    def __init__(self, args, obs_shape)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/distributions.py

```
class FixedCategorical(Categorical)
    def sample(self)
    def log_probs(self, actions)
    def mode(self)
class FixedNormal(Normal)
    def log_probs(self, actions)
    def entrop(self)
    def mode(self)
class FixedBernoulli(Bernoulli)
    def log_probs(self, actions)
    def entropy(self)
    def mode(self)
class Categorical(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x, available_actions)
class DiagGaussian(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain, config)
    def forward(self, x, available_actions)
class Bernoulli(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x)
class AddBias(Module)
    def __init__(self, bias)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/mlp.py

```
class MLPLayer(Module)
    def __init__(self, input_dim, hidden_size, layer_N, use_orthogonal, use_ReLU)
    def forward(self, x)
class MLPBase(Module)
    def __init__(self, config, obs_shape, cat_self, attn_internal)
    def forward(self, x)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/rnn.py

```
class RNNLayer(Module)
    def __init__(self, inputs_dim, outputs_dim, recurrent_N, use_orthogonal)
    def forward(self, x, hxs, masks)
```

### dexgrasp_policy/dexgrasp/algorithms/utils/util.py

```
def init(module, weight_init, bias_init, gain)
def get_clones(module, N)
def check(input)
```

### dexgrasp_policy/dexgrasp/tasks/hand_base/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors, is_meta, task_num)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions, id)
    def get_states(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### dexgrasp_policy/dexgrasp/tasks/hand_base/multi_vec_task.py

```
class MultiVecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MultiVecTaskPython(MultiVecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)
class SingleVecTaskPythonArm()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)

```python
def observation_space(self):
        return self.obs_space
```

```python
def observation_space(self):
        return self.obs_space
```
```

### dexgrasp_policy/dexgrasp/tasks/hand_base/vec_task.py

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
    def step(self, actions, id)
    def reserve_step(self, actions, id)
    def reset(self)
    def reserve_reset(self)
    def set_state_tensor_dict(self, state_tensor_dict)
class VecTaskPythonArm(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### dexgrasp_policy/dexgrasp/tasks/shadow_hand_grasp.py

```
class ShadowHandGrasp(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions, id)
    def compute_observations(self)
    def get_unpose_quat(self)
    def unpose_point(self, point)
    def unpose_vec(self, vec)
    def unpose_quat(self, quat)
    def unpose_state(self, state)
    def get_pose_quat(self)
    def pose_vec(self, vec)
    def pose_point(self, point)
    def pose_quat(self, quat)
    def pose_state(self, state)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
def compute_hand_reward(object_init_z, delta_qpos, delta_target_hand_pos, delta_target_hand_rot, id, object_id, dof_pos, rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, object_handle_pos, object_back_pos, object_rot, target_pos, target_rot, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, goal_cond)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
        object_init_z, delta_qpos, delta_target_hand_pos, delta_target_hand_rot,
        id: int, object_id, dof_pos, rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, current_successes, consecutive_successes,
        max_episode_length: float, object_pos, object_handle_pos, object_back_pos, object_rot, target_pos, target_rot,
        right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
        dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
        actions, action_penalty_scale: float,
        success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
        fall_penalty: float, max_consecutive_successes: int, av_factor: float, goal_cond: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    goal_hand_dist = torch.norm(target_pos - right_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(object_handle_pos - right_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.where(right_hand_dist >= 0.5, 0.5 + 0 * right_hand_dist, right_hand_dist)

    right_hand_finger_dist = (torch.norm(object_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(
        object_handle_pos - right_hand_mf_pos, p=2, dim=-1)+ torch.norm(object_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(
                object_handle_pos - right_hand_lf_pos, p=2, dim=-1) + torch.norm(object_handle_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = torch.where(right_hand_finger_dist >= 3.0, 3.0 + 0 * right_hand_finger_dist,right_hand_finger_dist)

    right_hand_dist_rew = right_hand_dist
    right_hand_finger_dist_rew = right_hand_finger_dist

    action_penalty = torch.sum(actions ** 2, dim=-1)

    delta_hand_pos_value = torch.norm(delta_target_hand_pos, p=1, dim=-1)
    delta_hand_rot_value = 2.0 * torch.asin(torch.clamp(torch.norm(delta_target_hand_rot[:, 0:3], p=2, dim=-1), max=1.0))
    delta_qpos_value = torch.norm(delta_qpos, p=1, dim=-1)
    delta_value = 0.6 * delta_hand_pos_value + 0.04 * delta_hand_rot_value + 0.1 * delta_qpos_value 
    target_flag = (delta_hand_pos_value <= 0.4).int() + (delta_hand_rot_value <= 1.0).int() + (delta_qpos_value <= 6.0).int()
        
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))
    lowest = object_pos[:, 2]
    lift_z = object_init_z[:, 0] + 0.6 +0.003

    if goal_cond:
        flag = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()  + target_flag
        goal_hand_rew = torch.zeros_like(right_hand_finger_dist)
        goal_hand_rew = torch.where(flag == 5, 1 * (0.9 - 2 * goal_dist), goal_hand_rew)
        
        flag2 = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()
        hand_up = torch.zeros_like(right_hand_finger_dist)
        hand_up = torch.where(lowest >= lift_z, torch.where(flag2 == 2, 0.1 + 0.1 * actions[:, 2], hand_up), hand_up)
        hand_up = torch.where(lowest >= 0.80, torch.where(flag2 == 2, 0.2 - goal_hand_dist * 0, hand_up), hand_up)

        bonus = torch.zeros_like(goal_dist)
        bonus = torch.where(goal_dist <= 0.05, 1.0 / (1 + 10 * goal_dist), bonus)

        reward = -0.5 * right_hand_finger_dist - 1.0 * right_hand_dist + goal_hand_rew + hand_up + bonus  - 0.5*delta_value

    else:
        flag = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()
        goal_hand_rew = torch.zeros_like(right_hand_finger_dist)
        goal_hand_rew = torch.where(flag == 2, 1 * (0.9 - 2 * goal_dist), goal_hand_rew)

        hand_up = torch.zeros_like(right_hand_finger_dist)
        hand_up = torch.where(lowest >= 0.630, torch.where(flag == 2, 0.1 + 0.1 * actions[:, 2], hand_up), hand_up)
        hand_up = torch.where(lowest >= 0.80, torch.where(flag == 2, 0.2 - goal_hand_dist * 0, hand_up), hand_up)

  
```

```python
def compute_reward(self, actions, id=-1):
        self.dof_pos = self.shadow_hand_dof_pos
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.current_successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.object_init_z, self.delta_qpos, self.delta_target_hand_pos, self.delta_target_hand_rot,
            self.id, self.object_id_buf, self.dof_pos, self.rew_buf, self.reset_buf, self.reset_goal_buf,
            self.progress_buf, self.successes, self.current_successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_handle_pos, self.object_back_pos, self.object_rot,
            self.goal_pos, self.goal_rot,
            self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos,
            self.right_hand_lf_pos, self.right_hand_th_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor,self.goal_cond
        )

        self.extras['successes'] = self.successes
        self.extras['current_successes'] = self.current_successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(
                direct_average_successes / (self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(
                    self.total_successes / self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_handle_pos = self.object_pos  ##+ quat_apply(self.object_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.06)
        self.object_back_pos = self.object_pos + quat_apply(self.object_rot,to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.04)
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]



        idx = self.hand_body_idx_dict['palm']
        self.right_hand_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot,to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        idx = self.hand_body_idx_dict['index']
        self.right_hand_ff_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
                                                              
        idx = self.hand_body_idx_dict['middle']
        self.right_hand_mf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        idx = self.hand_body_idx_dict['ring']
        self.right_hand_rf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        idx = self.hand_body_idx_dict['little']
        self.right_hand_lf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_lf_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_lf_pos = self.right_hand_lf_pos + quat_apply(self.right_hand_lf_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
                                                                         
        idx = self.hand_body_idx_dict['thumb']
        self.right_hand_th_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_th_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_th_pos = self.right_hand_th_pos + quat_apply(self.right_hand_th_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]

        def world2obj_vec(vec):
            return quat_apply(quat_conjugate(self.object_rot), vec - self.object_pos)
        def obj2world_vec(vec):
            return quat_apply(
```
```

### dexgrasp_policy/dexgrasp/tasks/shadow_hand_random_load_vision.py

```
class ShadowHandRandomLoadVision(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _init_waiting_pose(self)
    def _load_shadow_hand(self, env_ptr, env_id, shadow_hand_asset, hand_dof_props, init_hand_actor_pose)
    def _load_object(self, env_ptr, env_id, object_asset, init_object_pose, scale)
    def _load_goal(self, env_ptr, env_id, goal_asset, init_goal_pose, scale)
    def _cfg_camera_props(self)
    def _cfg_camera_pose(self)
    def _load_cameras(self, env_ptr, env_id, camera_props, camera_eye_list, camera_lookat_list)
    def compute_reward(self, actions, id)
    def compute_observations(self)
    def get_unpose_quat(self)
    def unpose_point(self, point)
    def unpose_vec(self, vec)
    def unpose_quat(self, quat)
    def unpose_state(self, state)
    def unpose_pc(self, pc)
    def get_pose_quat(self)
    def pose_vec(self, vec)
    def pose_point(self, point)
    def pose_quat(self, quat)
    def pose_state(self, state)
    def compute_full_state(self, asymm_obs)
    def _collect_pointclouds(self)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _switch_active(self, env_ids, first_frame)
    def _reset_hand(self, env_ids, dof_pos, dof_vel, prev_targets, cur_targets, hand_positions, hand_orientations, hand_linvels, hand_angvels)
    def _reset_object(self, env_ids, object_positions, object_orientations, object_linvels, object_angvels, goal_positions, goal_orientations, goal_linvels, goal_angvels)
    def _reset_table(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
def compute_hand_reward(object_id_buf, object_init_z, delta_qpos, delta_target_hand_pos, delta_target_hand_rot, id, object_id, dof_pos, rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, object_handle_pos, object_back_pos, object_rot, target_pos, target_rot, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, goal_cond)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def mov(tensor, device)
def depth_image_to_point_cloud_GPU_batch(camera_depth_tensor_batch, camera_rgb_tensor_batch, camera_seg_tensor_batch, camera_view_matrix_inv_batch, camera_proj_matrix_batch, u, v, width, height, depth_bar, device)
def sample_points(points, sample_num, sample_method, device)

```python
def compute_hand_reward(
        object_id_buf, object_init_z, delta_qpos, delta_target_hand_pos, delta_target_hand_rot,
        id: int, object_id, dof_pos, rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, current_successes, consecutive_successes,
        max_episode_length: float, object_pos, object_handle_pos, object_back_pos, object_rot, target_pos, target_rot,
        right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
        dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
        actions, action_penalty_scale: float,
        success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
        fall_penalty: float, max_consecutive_successes: int, av_factor: float, goal_cond: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    goal_hand_dist = torch.norm(target_pos - right_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(object_handle_pos - right_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.where(right_hand_dist >= 0.5, 0.5 + 0 * right_hand_dist, right_hand_dist)

    right_hand_finger_dist = (torch.norm(object_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(
        object_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                              + torch.norm(object_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(
                object_handle_pos - right_hand_lf_pos, p=2, dim=-1)
                              + torch.norm(object_handle_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = torch.where(right_hand_finger_dist >= 3.0, 3.0 + 0 * right_hand_finger_dist,
                                         right_hand_finger_dist)
    right_hand_dist_rew = right_hand_dist
    right_hand_finger_dist_rew = right_hand_finger_dist

    action_penalty = torch.sum(actions ** 2, dim=-1)

    delta_hand_pos_value = torch.norm(delta_target_hand_pos, p=1, dim=-1)
    delta_hand_rot_value = 2.0 * torch.asin(
        torch.clamp(torch.norm(delta_target_hand_rot[:, 0:3], p=2, dim=-1), max=1.0))
    delta_qpos_value = torch.norm(delta_qpos, p=1, dim=-1)
    delta_value = 0.3 * delta_hand_pos_value + 0.04 * delta_hand_rot_value + 0.02 * delta_qpos_value
    target_flag = (delta_hand_pos_value <= 0.6).int() + (delta_hand_rot_value <= 1.8).int() + (delta_qpos_value <= 9.0).int()
    
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))
    lowest = object_pos[:, 2]
    lift_z = object_init_z[:, 0] + 0.6 +0.003

    if goal_cond:
        flag = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()  + target_flag
        goal_hand_rew = torch.zeros_like(right_hand_finger_dist)
        goal_hand_rew = torch.where(flag == 5, 1 * (0.9 - 2 * goal_dist), goal_hand_rew)
        
        hand_up = torch.zeros_like(right_hand_finger_dist)
        hand_up = torch.where(lowest >= lift_z, torch.where(flag == 5, 0.1 + 0.1 * actions[:, 2], hand_up), hand_up)
        hand_up = torch.where(lowest >= 0.80, torch.where(flag == 5, 0.2 - goal_hand_dist * 0, hand_up), hand_up)

        flag = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()  #+ target_flag 
        bonus = torch.zeros_like(goal_dist)
        bonus = torch.where(flag == 2, torch.where(goal_dist <= 0.05, 1.0 / (1 + 10 * goal_dist), bonus), bonus)

        reward = -0.5 * right_hand_finger_dist - 1.0 * right_hand_dist + goal_hand_rew + hand_up + bonus  - 0.5*delta_value

    else:
        flag = (right_hand_finger_dist <= 0.6).int() + (right_hand_dist <= 0.12).int()
        goal_hand_rew = torch.zeros_like(right_hand_finger_dist)
        goal_hand_rew = torch.where(flag == 2, 1 * (0.9 - 2 * goal_dist), goal_hand_rew)

        hand_up = torch.zeros_like(right_hand_finger_dist)
        hand_up = torch.where(lowest >= lift_z, torch.where(flag =
```

```python
def compute_reward(self, actions, id=-1):
        self.dof_pos = self.shadow_hand_dof_pos
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.current_successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.object_id_buf, self.object_init_z, self.delta_qpos, self.delta_target_hand_pos, self.delta_target_hand_rot,
            self.id, self.object_id_buf, self.dof_pos, self.rew_buf, self.reset_buf, self.reset_goal_buf,
            self.progress_buf, self.successes, self.current_successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_handle_pos, self.object_back_pos, self.object_rot,
            self.goal_pos, self.goal_rot,
            self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos,
            self.right_hand_lf_pos, self.right_hand_th_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, self.goal_cond
        )

        self.extras['successes'] = self.successes
        self.extras['current_successes'] = self.current_successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(
                direct_average_successes / (self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(
                    self.total_successes / self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.has_sensor:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_handle_pos = self.object_pos
        self.object_back_pos = self.object_pos + quat_apply(self.object_rot,to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.04)
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        idx = self.hand_body_idx_dict['palm']
        self.right_hand_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot,to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        idx = self.hand_body_idx_dict['index']
        self.right_hand_ff_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
                                                                         
        idx = self.hand_body_idx_dict['middle']
        self.right_hand_mf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
                                                                         
        idx = self.hand_body_idx_dict['ring']
        self.right_hand_rf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, idx, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot,to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
                                                                         
        idx = self.hand_body_idx_dict['little']
        self.right_hand_lf_pos = self.rigid_body_states[:, idx, 0:3]
        self.right_hand_lf_rot = self.rigid_body_states[:, idx, 3
```

### dexgrasp_policy/dexgrasp/train.py

```
def train()
```

### dexgrasp_policy/dexgrasp/utils/config.py

```
def set_np_formatting()
def warn_task_name()
def warn_algorithm_name()
def set_seed(seed, torch_deterministic)
def retrieve_cfg(args, use_rlg_config)
def load_cfg(args, use_rlg_config)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark, use_rlg_config)
```

### dexgrasp_policy/dexgrasp/utils/data_info.py

```
def plane2pose(plane_parameters)
def plane2euler(plane_parameters, axes)
```

### dexgrasp_policy/dexgrasp/utils/logger/plotter.py

```
def smooth(y, radius, mode, valid_only)
def plot_ax(ax, file_lists, legend_pattern, xlabel, ylabel, title, xlim, xkey, ykey, smooth_radius, shaded_std, legend_outside)
def plot_figure(file_lists, group_pattern, fig_length, fig_width, sharex, sharey, title)
```

### dexgrasp_policy/dexgrasp/utils/logger/tools.py

```
def find_all_files(root_dir, pattern)
def group_files(file_list, pattern)
def csv2numpy(csv_file)
def convert_tfevents_to_csv(root_dir, alg_type, env_num, env_step, refresh)
def merge_csv(csv_files, root_dir, remove_zero)
```

### dexgrasp_policy/dexgrasp/utils/parse_task.py

```
def parse_task(args, cfg, cfg_train, sim_params, agent_index)
```

### dexgrasp_policy/dexgrasp/utils/process_marl.py

```
def get_AgentIndex(config)
def process_MultiAgentRL(args, env, config, model_dir)
```

### dexgrasp_policy/dexgrasp/utils/process_sarl.py

```
def process_dagger_value(args, env, cfg_train, logdir)
def process_ppo(args, env, cfg_train, logdir)
def process_dagger(args, env, cfg_train, logdir)
```

### dexgrasp_policy/dexgrasp/utils/torch_jit_utils.py

```
def compute_heading_and_up(torso_rotation, inv_start_rot, to_target, vec0, vec1, up_idx)
def compute_rot(torso_quat, velocity, ang_velocity, targets, torso_positions)
def quat_axis(q, axis)
```

### dexgrasp_policy/dexgrasp/utils/util.py

```
def check(input)
def get_gard_norm(it)
def update_linear_schedule(optimizer, epoch, total_num_epochs, initial_lr)
def huber_loss(e, d)
def mse_loss(e)
def get_shape_from_obs_space(obs_space)
def get_shape_from_act_space(act_space)
def tile_images(img_nhwc)
```

### dexgrasp_policy/setup.py

```
"""Installation script for the 'isaacgymenvs' python package."""
```