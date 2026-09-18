# bidexhd_2024

source: https://github.com/zhoubohan0/BiDexHD


commit: 172737bf20274abb817478ce4f2864f7577a1627


## README

# BiDexHD 🤖
🙌 Official implementation of "Learning Diverse Bimanual Dexterous Manipulation Skills from Human Demonstrations"

## 0. Overview
we propose a unified and scalable three-phase framework BiDexHD
- Task Construction: construct a bimanual tool-using task from each demonstration in TACO dataset
- Teacher Learning: train state-based multi-task teacher policies for constructed bimanual dexterous tasks in parallel
- Student Learning: Distill teacher policies into single vision-based (pointcloud) policy

## 1. Install 🚀
### 1.1 Download isaac gym preview 📑
Refer to https://developer.nvidia.com/isaac-gym/download .

### 1.2 Download TACO dataset 🍔
Follow the instructions in https://github.com/leolyliu/TACO-Instructions .
All triplets can be found in `${dataset_root}/overall/Object_Poses/*` .

### 1.3 Build up virtual environment 🛰️
```bash
conda create -y -n bidexhd python=3.8
conda activate bidexhd
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
cd rl_policy/taco_dataset/
pip install -e .
cd rl_policy/Pointnet2_PyTorch/pointnet2_ops_lib
pip install -e .
# 
cd /home/zbh/Downloads/IsaacGym_Preview_4_Package/isaacgym/python
pip install -e .
cd /home/zbh/Downloads/IsaacGymEnvs/
pip install -e .
pip install ipdb addict yapf h5py sorcery pynvml seaborn einops tensorboard accelerate open3d anytree chumpy kornia pytransform3d nlopt natsort hydra omegaconf nvitop trimesh gym git+https://github.com/isaac-sim/IsaacGymEnvs.git -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

## 2. Implement 📚
### 2.1 Task construction 🗂️
Run the code below to store all task data including pose sequences of tool, target object and hands in `rl_policy/taco_dataset/sampled_data/${triplet}.json` and visualize all tasks under ${triplet} in Isaac Gym with different object ids.  
```bash
bash vis_all.sh "'$triplet'"
```
triplet can be:
- "(empty, bowl, bowl)"
- "(stir-fry, spatula, pan)"
- ...

### 2.2 Multi-Task Reinforcement Learning 📥
Train and evaluate IPPO:
```bash
bash scripts/exe6.sh "'$triplet'" "$train_ids" 
# or parallel: bash scripts/exe6p.sh
```

### 2.3 Policy Distillation 🏆
Train and evaluate DAgger:
```bash
bash scripts/exem3dagger.sh "$device_id" "'$verb'" 
```



## File tree (depth 3, assets pruned)

```
.gitignore
README.md
rl_policy/
  Pointnet2_PyTorch/
    .gitignore
    .pre-commit-config.yaml
    .travis.yml
    MANIFEST.in
    README.rst
    UNLICENSE
    pointnet2/
    pointnet2_ops_lib/
    pyproject.toml
    requirements.txt
    setup.py
    tests/
    tox.ini
  algo/
    bc/
    common/
    dagger/
    marl/
    pn_utils/
    ppo/
  cfgs/
    config.yaml
    task/
    train/
  main.py
  taco_dataset/
    TACOdataset.py
    __init__.py
    dex_retargeting/
    manopth/
    setup.py
    task_data/
  tasks/
    __init__.py
    bi_leap_hand_grasp_bc.py
    bi_leap_hand_grasp_dagger.py
    bi_leap_hand_grasp_m2dagger.py
    bi_leap_hand_grasp_m3dagger.py
    bi_leap_hand_grasp_multidagger.py
    bi_leap_hand_grasp_v0.py
    bi_leap_hand_grasp_v1.py
    bi_leap_hand_grasp_v2.py
    bi_leap_hand_grasp_v3.py
    bi_leap_hand_grasp_v4.py
    bi_leap_hand_grasp_v5.py
    bi_leap_hand_grasp_v6.py
    bi_leap_hand_grasp_vision.py
    leap_hand_grasp.py
    shadow_hand_grasp.py
scripts/
  ablate_ippo.sh
  ablate_k.sh
  baseline_bc.sh
  baseline_ppo.sh
  baseline_ppodagger.sh
  collect_result.sh
  exe0.sh
  exe1.sh
  exe2.sh
  exe3.sh
  exe3p.sh
  exe4.sh
  exe5.sh
  exe6.sh
  exe6p.sh
  exe6p2.sh
  exem2dagger.sh
  exem3dagger.sh
  exemultidagger.sh
  exev.sh
  gen_task.sh
  kill.sh
  label_all_dof.sh
  vis_all.sh
```

## Config files (67)


### rl_policy/Pointnet2_PyTorch/.pre-commit-config.yaml

```yaml
exclude: 'build|egg-info|dist'

default_language_version:
    python: python3

repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    -   id: trailing-whitespace
    -   id: check-added-large-files
    -   id: end-of-file-fixer

-   repo: https://github.com/asottile/seed-isort-config
    rev: v1.9.2
    hooks:
    -   id: seed-isort-config
        language_version: python3

-   repo: https://github.com/pre-commit/mirrors-isort
    rev: v4.3.20
    hooks:
    -   id: isort
        exclude: docs/
        additional_dependencies: [toml]

-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3

-   repo: local
    hooks:
    - id: clang-format
      name: Run clang-format
      entry: clang-format --style google -i
      types: [text]
      files: '.*\.cpp$|.*\.h$|.*\.cu$|.*\.hpp$'
      language: system

```

### rl_policy/Pointnet2_PyTorch/.travis.yml

```yaml
dist: trusty

language: python

python:
  - "3.6"
install:
  - pip install black
script:
  - black --check .
  - find . -not -path '*/\.*' | grep -E ".*\.cpp$|.*\.h$|.*\.cu$|.*\.hpp$" | xargs -I {} bash -c "diff -u <(cat {}) <(clang-format --style google {})"

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/config.yaml

```yaml
defaults:
    - task: cls
    - model: ssg
    - task_model: ${defaults.0.task}-${defaults.1.model}

hydra:
  run:
    dir: outputs

gpus:
    - 0

optimizer: ???

task_model: ???

model: ???

distrib_backend: dp

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/model/msg.yaml

```yaml
model:
    use_xyz: True

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/model/ssg.yaml

```yaml
model:
    use_xyz: True

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task/cls.yaml

```yaml
optimizer:
    weight_decay: 0.0
    lr: 1e-3
    lr_decay: 0.7
    bn_momentum: 0.5
    bnm_decay: 0.5
    decay_step: 2e4


num_points: 4096
epochs: 200
batch_size: 32

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task/semseg.yaml

```yaml
optimizer:
    weight_decay: 0.0
    lr: 1e-3
    lr_decay: 0.5
    bn_momentum: 0.5
    bnm_decay: 0.5
    decay_step: 3e5

num_points: 4096
epochs: 50
batch_size: 24

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task_model/cls-msg.yaml

```yaml
task_model:
    class: pointnet2.models.PointNet2ClassificationMSG
    name: cls-msg

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task_model/cls-ssg.yaml

```yaml
task_model:
    class: pointnet2.models.PointNet2ClassificationSSG
    name: cls-ssg

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task_model/semseg-msg.yaml

```yaml
task_model:
    class: pointnet2.models.PointNet2SemSegMSG
    name: sem-msg

```

### rl_policy/Pointnet2_PyTorch/pointnet2/config/task_model/semseg-ssg.yaml

```yaml
task_model:
    class: pointnet2.models.PointNet2SemSegSSG
    name: sem-ssg

```

### rl_policy/cfgs/config.yaml

```yaml

# Task name - used to pick the class to load
task_name: ${task.name}
# experiment name. defaults to name of training config
experiment: ''
algo: 'ippo'
# if set to positive integer, overrides the default number of environments
num_envs: 8192

# seed - set to -1 to choose random seed
seed: 42
# set to True for deterministic performance
torch_deterministic: False

# set the maximum number of learning iterations to train for. overrides default per-environment setting
max_iterations: ''

## Device config
#  'physx' or 'flex'
physics_engine: 'physx'
# whether to use cpu or gpu pipeline
pipeline: 'gpu'
# device for running physics simulation
sim_device: 'cuda:0'
# device to run RL
rl_device: 'cuda:0'
graphics_device_id: 0

## PhysX arguments
num_threads: 4 # Number of worker threads per scene used by PhysX - for CPU PhysX only.
solver_type: 1 # 0: pgs, 1: tgs
num_subscenes: 4 # Splits the simulation into N physics scenes and runs each one in a separate thread

# test - if set, run policy in inference mode (requires setting checkpoint to load)
test: False
# used to set checkpoint path
checkpoint: ''
# set sigma when restoring network
sigma: ''
# set to True to use multi-gpu training
multi_gpu: False

capture_video: False
capture_video_freq: 1464
capture_video_len: 100
force_render: True

# disables rendering
headless: False

# set default task and default training config based on task
defaults:
  - task: ShadowHandGrasp
  - train: ${task}PPO
  - override hydra/job_logging: disabled
  - _self_

# set the directory where the output files get saved
hydra:
  output_subdir: null
  run:
    dir: .

record: False
debug: False
mode: train  # debug  visualize
triplet: "(empty, bowl, bowl)" #(pour in some, teapot, cup) (stir, spoon, pan) (stir, spatula, pan) (smear, eraser, plate) (stir-fry, spatula, pan) (empty, bowl, bowl) (pour in some, bowl, bowl)
exp_name: ""
task_id: 1
# orders: ['dofps', 'dofvel', 'ftps', 'ftstate', 'lastact', 'objpose', 'objstate', 'palmps', 'palmpose', 'palmstate', 'relps']
# observationType: 'dofps+dofvel+ftstate+lastact+objstate+palmstate+relps'  # 'full'
# observationType: 'dofps+ftps+lastact+objpose+palmpose'  # minimal  
# observationType: 'dofps+dofvel+ftps+lastact+objstate+palmpose+relps'  # 'full_no_vel'
# observationType: 'dofps+ftps+lastact+palmps+camerapc'  # 'camera'
# observationType: "dofps+ftps+lastact+palmps+meshpc"     # 'pcd'
# observationType: 'dofps+dofvel+ftps+lastact+objstate+palmpose+relps+meshpc'  # 'multidagger' ('v3')               113
# observationType: 'dofps+dofvel+ftps+lastact+objstate+palmpose+relps+meshpc+objlabel'  # 'multidagger' ('v4')        114
# observationType: 'dofps+ftps+lastact+objpose+palmps+relps+meshpc+objlabel'  # 'multidagger' ('v5')                82
# observationType: 'dofps+ftps+lastact+objstate+palmpose+relps+meshpc+objlabel'  # 'multidagger' ('v5')             92
observationType: 'dofps+dofvel+ftps+lastact+objstate+palmpose+relps+meshpc+objlabel+futureps'  # 'multidagger' ('v6')        3330
isStage1HOReward: 0
isStage1LinReward: 0
isStage2PosRewExp: 1

# vision
numDownsample: 512
numEachPoint: 3

objectOffset: 0.1
train_ids: 0 #[1, 2, 3, 5, 6, 7, 8, 10]

rewfunc: 'multippo'  # ab_stage1, ab_funcgrasp, ab_bonus
expertModel: "IPPO"
Kfuturestep: 5


```

### rl_policy/cfgs/task/BiLeapHandGraspBC.yaml

```yaml
# used to create the object
name: BiLeapHandGraspBC
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 1000
  enableDebugVis: ${debug}
  aggregateMode: 1
  objectOffset: ${objectOffset}

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 2.0]
  vision:
    pointclouds:
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
      nResample: 32
      nMaxSamplePoints: 4096
      nSamplePoints: 512
    noise: 
      apply: False
      scale: 0.004
      threshold: 0.4

task:
  is_all_task: ${...test}
  frequency: 3
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  Kfuturestep: ${Kfuturestep}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### rl_policy/cfgs/task/BiLeapHandGraspDagger.yaml

```yaml
# used to create the object
name: BiLeapHandGraspDagger
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 1.0]
  cameraTarget: [0.0, 0.0, 0.5]
  vision:
    pointclouds:
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
task:
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspM2Dagger.yaml

```yaml
# used to create the object
name: BiLeapHandGraspM2Dagger
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 800
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 2.0]
  vision:
    pointclouds:
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
      nResample: 32
      nMaxSamplePoints: 4096
      nSamplePoints: 512
    noise: 
      apply: False
      scale: 0.004
      threshold: 0.4

task:
  is_all_task: ${...test}
  frequency: 3
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### rl_policy/cfgs/task/BiLeapHandGraspM3Dagger.yaml

```yaml
# used to create the object
name: BiLeapHandGraspM3Dagger
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 1000
  enableDebugVis: ${debug}
  aggregateMode: 1
  objectOffset: ${objectOffset}

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 2.0]
  vision:
    pointclouds:
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
      nResample: 32
      nMaxSamplePoints: 4096
      nSamplePoints: 512
    noise: 
      apply: False
      scale: 0.005
      threshold: 0.4

task:
  is_all_task: ${...test}
  frequency: 3
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  Kfuturestep: ${Kfuturestep}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### rl_policy/cfgs/task/BiLeapHandGraspMultiDagger.yaml

```yaml
# used to create the object
name: BiLeapHandGraspMultiDagger
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 2.0]
  vision:
    pointclouds:
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
task:
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV0.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV0
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.5
  actionPenaltyScale: 0.001

  observationType: "full" # can be "full_no_vel", "full", "full_state"
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  frequency: 1.5
  horizon: 2
  onlyObjectReward: 1
  onlyGraspReward: 0
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/sampled_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV1.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV1
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.5
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    textureFile: "texture/texture_wood_brown_1033760.jpg"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 1.0]
  cameraTarget: [0.0, 0.0, 0.5]
  imageWidth: 128
  imageHeight: 128
  imageSaveDir: "/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/taco_dataset/sampled_data"

task:
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/sampled_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV2.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV2
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 1.0]
  cameraTarget: [0.0, 0.0, 0.5]
  imageWidth: 128
  imageHeight: 128
  imageSaveDir: "/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/taco_dataset/sampled_data"

task:
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV3.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV3
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 1.5]
  imageWidth: 128
  imageHeight: 128
  imageSaveDir: "/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/taco_dataset/sampled_data"

task:
  is_all_task: ${...test}
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV4.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV4
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 2.0]

task:
  is_all_task: ${...test}
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV5.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV5
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 1.5]
  imageWidth: 128
  imageHeight: 128
  imageSaveDir: "/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/taco_dataset/sampled_data"

task:
  is_all_task: ${...test}
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
```

### rl_policy/cfgs/task/BiLeapHandGraspV6.yaml

```yaml
# used to create the object
name: BiLeapHandGraspV6
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  objectOffset: ${objectOffset}
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1
  episodeLength: 1000
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.1
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.3
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  cameraPosition: [0.0, -2.0, 3.0]
  cameraTarget: [0.0, 0.0, 1.5]
  imageWidth: 128
  imageHeight: 128
  imageSaveDir: "/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/taco_dataset/sampled_data"

task:
  rewfunc: ${...rewfunc}
  is_all_task: ${...test}
  task_id: ${...task_id}
  frequency: 3.0
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/task_data/${...triplet}.json
  train_task_id_list: ${...train_ids}
```

### rl_policy/cfgs/task/BiLeapHandGraspVision.yaml

```yaml
# used to create the object
name: BiLeapHandGraspVision
mode: ${mode}
physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: ${debug}
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.5
  actionPenaltyScale: 0.001

  observationType: ${observationType}
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    leftAssetFile: "rm65_leap_right/rm65_leap_left_m1.urdf"
    rightAssetFile: "rm65_leap_right/rm65_leap_right_m1.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    toolAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  # palm_offset: [0.0, 0.0, 0.0]
  # finger_offset: [0.0, -0.05, 0.015]
  # thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: True
  cameraPosition: [0.0, -2.0, 1.0]
  cameraTarget: [0.0, 0.0, 0.5]
  vision:
    pointclouds:
      numPresample: 65536
      numDownsample: ${numDownsample}
      numEachPoint: ${numEachPoint}
    camera:
      width: 256
      height: 256
      # relative to table center
      eye: [
        [ 0.0, 0.0, 0.85 ],
        # [ 0.8, 0.0, 0.05 ],
        # [ -0.8, 0.0, 0.05 ],
        # [ 0.0, 0.8, 0.05 ],
        # [ 0.0, -0.8, 0.05 ]
      ]
      lookat: [ # camera cannot look at accurate -z
        [ 0.01, 0.0, 0.05 ],
        # [ 0.0, 0.0, 0.05 ],
        # [ 0.0, 0.0, 0.05 ],
        # [ 0.0, 0.0, 0.05 ],
        # [ 0.0, 0.0, 0.05 ],
      ]
    bar:
      x_n: -1
      x_p: 1
      y_n: -1
      y_p: 1
      z_n: 0.61
      z_p: 1.3
      depth: 1.5

task:
  task_id: ${...task_id}
  frequency: 2
  horizon: 2
  isStage1HOReward: ${isStage1HOReward}
  isStage1LinReward: ${isStage1LinReward}
  isStage2PosRewExp: ${isStage2PosRewExp}
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

dataset:
  meta_data_path: taco_dataset/sampled_data/${...triplet}.json
```

### rl_policy/cfgs/task/LeapHandGrasp.yaml

```yaml
# used to create the object
name: LeapHandGrasp

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.2
  episodeLength: 300
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.5
  actionPenaltyScale: -0.0002

  observationType: "full" # can be "full_no_vel", "full", "full_state"
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  asset:
    assetRoot: "../assets"
    robotAssetFile: "rm65_leap_right/rm65_leap_right.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf"
  
  palm_offset: [0.0, 0.0, 0.0]
  finger_offset: [0.0, -0.05, 0.015]
  thumb_offset: [0.0, -0.06, -0.01]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### rl_policy/cfgs/task/ShadowHandGrasp.yaml

```yaml
# used to create the object
name: ShadowHandGrasp

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 1.2
  episodeLength: 300
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  armController: "qpos" # can be "ik" or "qpos" 
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.02
  startRotationNoise: 0.0

  resetPositionNoise: 0.02
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: 0.5
  actionPenaltyScale: -0.0002

  observationType: "full" # can be "full_no_vel", "full", "full_state"
  asymmetric_observations: False
  successTolerance: 0.05
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  multiTask: False
  useContactFeatures: False
  contactFeatureDir: "../contact/data"
  asset:
    assetRoot: "../assets"
    robotAssetFile: "rm65_shadow_right/rm65_shadow_right.urdf"
    objectAssetFile: "obj/urdf/cup.urdf"
    objectAssetDir: "obj/urdf" # used for multi-task
  
  palm_offset: [0.0, 0.0, 0.05]
  finger_offset: [0.0, 0.0, 0.03]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
    actor_params:
      hand:
        color: True
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

sim:
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2 
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### rl_policy/cfgs/train/LeapHandGraspBaselineBC.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 300
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 2.e-4
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/LeapHandGraspBaselinePPO.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-baselineppo' 
  policy: # only works for MlpPolicy right now
    backbone_type: ''
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
    objlabel_dim: 128

  test: ${...test}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.8

```

### rl_policy/cfgs/train/LeapHandGraspM2Dagger.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 128
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 1000
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
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
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(brush, brush, bowl)/ema0.1+ol2/model_21000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(dust, brush, bowl)/ema0.1+ol2/model_17000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(dust, brush, pan)/ema0.1+ol2/model_22000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(dust, roller, bowl)/ema0.1+ol2/model_22500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(empty, bowl, bowl)/ema0.1+ol2/model_18000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(empty, bowl, plate)/ema0.1+ol2/model_29500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(empty, cup, teapot)/ema0.1+ol2/model_12500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(empty, teapot, plate)/ema0.1+ol2/model_20500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(empty, teapot, teapot)/ema0.1+ol2/model_19000.pt',
    '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(put out, bowl, bowl)/ema0.1+ol2/model_18000.pt',
    '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(put out, bowl, pan)/ema0.1+ol2/model_11500.pt',
    '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(put out, bowl, plate)/ema0.1+ol2/model_30000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(pour in some, bowl, bowl)/ema0.1+ol2/model_14000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(pour in some, cup, cup)/ema0.1+ol2/model_17500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(scrape off, knife, bowl)/ema0.1+ol2/model_37000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(smear, glue gun, box)/ema0.1+ol2/model_34000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready/(brush, brush, box)/ema0.1+ol2/model_15000.pt',

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(brush, brush, bowl)/ema0.1+ol2/model_21000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(dust, brush, bowl)/ema0.1+ol2/model_17000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(dust, brush, pan)/ema0.1+ol2/model_22000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(dust, roller, bowl)/ema0.1+ol2/model_22500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(empty, bowl, bowl)/ema0.1+ol2/model_18000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(empty, bowl, plate)/ema0.1+ol2/model_29500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(empty, cup, teapot)/ema0.1+ol2/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(empty, teapot, plate)/ema0.1+ol2/model_20500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(empty, teapot, teapot)/ema0.1+ol2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(put out, bowl, bowl)/ema0.1+ol2/model_18000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(put out, bowl, pan)/ema0.1+ol2/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(put out, bowl, plate)/ema0.1+ol2/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(pour in some, bowl, bowl)/ema0.1+ol2/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(pour in some, cup, cup)/ema0.1+ol2/model_17500.pt',
    #'/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(scrape off, knife, bowl)/ema0.1+ol2/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(smear, glue gun, box)/ema0.1+ol2/model_34000.pt',
    
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/114-cgpos-clip/(brush, brush, box)/ema0.1+ol2/model_15000.pt',
  ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  clipAction: False
  lossFunc: "huber"
```

### rl_policy/cfgs/train/LeapHandGraspM3Dagger.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # [-1,1] action
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready2.0/(brush, brush, bowl)/ema0.1+ol2_sel[1,2,3,5,9,10,11]/model_11500.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/ready2.0/(dust, brush, bowl)/ema0.1+ol2/model_18000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(pour in some, bowl, bowl)/ema0.1+ol2/model_24000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(pour in some, cup, cup)/ema0.1+ol2/model_7000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(scrape off, knife, bowl)/ema0.1+ol2/model_24000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, cup, teapot)/ema0.1+ol2/model_6000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, bowl, bowl)/ema0.1+ol2/model_23000.pt',
    # '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, teapot, teapot)/ema0.1+ol2/model_6000.pt',

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1_sel/(brush, brush, bowl)/ema0.1+ol2/model_20000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(dust, roller, bowl)/ema0.1+ol2/model_38000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(dust, brush, pan)/ema0.1+ol2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(pour in some, bowl, bowl)/ema0.1+ol2/model_24000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(pour in some, cup, cup)/ema0.1+ol2/model_7000.pt'
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(pour in some, cup, teapot)/ema0.1+ol2/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, cup, teapot)/ema0.1+ol2/model_6000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, bowl, bowl)/ema0.1+ol2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, teapot, teapot)/ema0.1+ol2/model_6000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(empty, bowl, plate)/ema0.1+ol2/model_28000.pt'
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(scrape off, knife, bowl)/ema0.1+ol2/model_24000.pt'
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp1/(skim off, bowl, bowl)/ema0.1+ol2/model_20000.pt',
  
  
  
    # action
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    '/home/zbh/Desktop/zbh/robot/BiDexHD/rl_policy/runs-multippo/real_ippo/(pour in some, cup, teapot)/ema0.1+ol2/1w/model_6500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.
```

### rl_policy/cfgs/train/LeapHandGraspMultiDagger.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 128
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
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

  value_loss:
    apply: True
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5
    
  expertCkptFile: '/home/zbh/Desktop/zbh/robot/BVDex/rl_policy/runs-multippo/(empty, bowl, bowl)/task1/ema0.1+ol2/model_18000.pt'
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"
  
```

### rl_policy/cfgs/train/LeapHandGraspMultiPPO.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-multippo' 
  policy: # only works for MlpPolicy right now
    backbone_type: ''
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
    objlabel_dim: 128

  test: ${...test}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 2.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.8

```

### rl_policy/cfgs/train/LeapHandGraspPPO.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs' 
  policy: # only works for MlpPolicy right now
    backbone_type: ''
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
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
  
```

### rl_policy/cfgs/train/LeapHandGraspVisionPPO.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 128
    useSeg: False
    freeze_backbone: False  # useless now
    pi_hid_sizes: [1024, 1024, 512, 512]
    vf_hid_sizes: [1024, 1024, 512, 512]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
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
  
```

### rl_policy/cfgs/train/dust.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/empty.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/pourinsome.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/putout.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/skimoff.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/cfgs/train/smear.yaml

```yaml
params:
  name: ${algo}
  log_dir: './runs-dagger' 
  policy: # only works for MlpPolicy right now
    backbone_type: 'PointNetBackbone'
    numDownsample: ${numDownsample}
    numEachPoint: ${numEachPoint}
    pcEmbDim: 256
    useSeg: False
    freeze_backbone: False
    pi_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    vf_hid_sizes: [1024, 1024, 512, 512, 512, 256, 256]
    activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid

  test: ${...test}
  checkpoint: ${...checkpoint}
  resume: 0
  # check for potential saves every this many iterations
  save_interval: 500
  print_log: True

  # rollout params
  max_iterations: 1000000

  # training params
  cliprange: 0.2
  ent_coef: 0.0001
  nsteps: 8
  noptepochs: 3
  nminibatches: 32 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.96
  lam: 0.95
  init_noise_std: 0.1

  log_interval: 1
  asymmetric: False

  value_loss:
    apply: False
    use_clipped_value_loss: True
    value_loss_coef: 0.1
    clip_range: 0.5

  expertCkptFiles: [
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/model_21500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/model_15000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/model_23000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/4w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/model_3500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/model_19000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/model_10500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/model_15500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/6w/model_9.5k.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/4w/model_14000.pt',
    '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-multippo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/model_13500.pt',
    
    
    

    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_29000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_30000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, cup, plate)/ema0.1+ol2_oo0.2/2w/model_9000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(empty, teapot, teapot)/ema0.1+ol2_oo0.2/2w/model_16500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, cup)/ema0.1+ol2_oo0.2/2w/model_2000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, plate)/ema0.1+ol2_oo0.2/2w/model_31500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, cup, teapot)/ema0.1+ol2_oo0.2/2w/model_11500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, bowl)/ema0.1+ol2_oo0.2/2w/model_12500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(pour in some, teapot, cup)/ema0.1+ol2_oo0.2/2w/model_8500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(put out, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_11000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_36000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(dust, brush, pan)/ema0.1+ol2_oo0.2/2w/model_17500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(smear, glue gun, plate)/ema0.1+ol2_oo0.2/2w/model_37000.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(skim off, bowl, plate)/ema0.1+ol2_oo0.2/2w/model_18500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(brush, brush, bowl)/ema0.1+ol2_oo0.2/2w/model_19500.pt',
    # '/mnt/hpfs/baairl/zbh/BVDex/rl_policy/runs-baselineppo/freq3/exp2/(scrape off, knife, bowl)/ema0.1+ol2_oo0.2/2w/model_3000.pt',
    ]
  expertObservationType: "dofps+dofvel+ftps+lastact+objstate+palmpose+relps+objlabel"  
  train_task_id_dict: {
    "(brush, brush, bowl)": [1,2,3,5,9,10,11],
    "(dust, roller, bowl)": [3,4,5,6,7,8,9,10,11,12,13,14],
    "(dust, brush, bowl)":[],
    "(dust, brush, pan)": [],
    "(pour in some, bowl, bowl)": [2,3,4,5,6],
    "(pour in some, cup, cup)": [],
    "(pour in some, cup, plate)": [0],
    "(pour in some, cup, teapot)": [],
    "(pour in some, teapot, bowl)": [],
    "(pour in some, teapot, cup)": [],
    "(empty, bowl, bowl)": [2,3,4,6,7],
    "(empty, bowl, plate)": [],
    "(empty, cup, teapot)": [],
    "(empty, cup, plate)": [],
    "(empty, teapot, teapot)": [0,2],
    "(empty, teapot, plate)": [],
    "(put out, bowl, bowl)": [],
    "(put out, bowl, plate)": [],
    "(scrape off, knife, bowl)": [],
    "(skim off, bowl, bowl)": [],
    "(skim off, bowl, plate)": [],
    "(smear, glue gun, plate)": [],
  }
  clipAction: False
  lossFunc: "huber" #"l1"
  expertModel: ${...expertModel}
  Kfuturestep: ${...Kfuturestep} 
```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/ability_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: ability_hand/ability_hand_right.urdf
  wrist_link_name: "base_link"

  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False
```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/allegro_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: allegro_hand/allegro_hand_right.urdf
  wrist_link_name: "wrist"

  target_joint_names: null
  target_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip", "link_14.0",
                       "link_2.0", "link_6.0", "link_10.0" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/leap_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: ../assets/rm65_leap_right/my_leap_left.urdf # assets/mjcf/leap_hand_description/leap_hand_left.urdf 
  wrist_link_name: "base"

  target_joint_names: null
  target_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head", "thumb_dip", "dip", "dip_2", "dip_3" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/leap_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: ../assets/rm65_leap_right/my_leap_right.urdf #assets/mjcf/leap_hand_description/leap_hand_right.urdf
  wrist_link_name: "base"

  target_joint_names: null
  target_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head", "thumb_dip", "dip", "dip_2", "dip_3" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/schunk_svh_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: schunk_hand/schunk_svh_hand_right.urdf
  wrist_link_name: "right_hand_base_link"

  target_joint_names: [ 'right_hand_Thumb_Opposition', 'right_hand_Thumb_Flexion', 'right_hand_Index_Finger_Proximal',
                        'right_hand_Index_Finger_Distal', 'right_hand_Finger_Spread', 'right_hand_Pinky',
                        'right_hand_Ring_Finger', 'right_hand_Middle_Finger_Proximal', 'right_hand_Middle_Finger_Distal' ]
  target_link_names: [ "right_hand_c", "right_hand_t", "right_hand_s", "right_hand_r",
                        "right_hand_q", "right_hand_b", "right_hand_p", "right_hand_o", "right_hand_n", "right_hand_i"]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/shadow_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: shadow_hand/shadow_hand_right.urdf
  wrist_link_name: "ee_link"

  target_joint_names: null
  target_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",
                       "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/offline/shadow_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: shadow_hand/shadow_hand_right.urdf
  wrist_link_name: "ee_link"

  target_joint_names: null
  target_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",
                       "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/ability_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: ability_hand/ability_hand_left.urdf
  wrist_link_name: "base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_origin_link_names: [ "base_link", "base_link", "base_link", "base_link", "base_link" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip", ]
  scaling_factor: 1.0

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/ability_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ability_hand/ability_hand_left.urdf
  wrist_link_name: "base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.0

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/ability_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: ability_hand/ability_hand_right.urdf
  wrist_link_name: "base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_origin_link_names: [ "base_link", "base_link", "base_link", "base_link", "base_link" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip", ]
  scaling_factor: 1.0

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/ability_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ability_hand/ability_hand_right.urdf
  wrist_link_name: "base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.0

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/allegro_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: allegro_hand/allegro_hand_left.urdf
  wrist_link_name: "wrist"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  target_origin_link_names: [ "wrist", "wrist", "wrist", "wrist" ]
  target_task_link_names: [ "link_15.0_tip", "link_11.0_tip", "link_7.0_tip", "link_3.0_tip" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/allegro_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: allegro_hand/allegro_hand_left.urdf
  wrist_link_name: "wrist"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  finger_tip_link_names: [ "link_15.0_tip", "link_11.0_tip", "link_7.0_tip", "link_3.0_tip" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/allegro_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: allegro_hand/allegro_hand_right.urdf
  wrist_link_name: "wrist"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  target_origin_link_names: [ "wrist", "wrist", "wrist", "wrist" ]
  target_task_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/allegro_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: allegro_hand/allegro_hand_right.urdf
  wrist_link_name: "wrist"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  finger_tip_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/leap_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ../assets/leap_hand_description/leap_hand_left.urdf #leap_hand/leap_hand_left.urdf
  wrist_link_name: "base"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  finger_tip_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/leap_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: leap_hand/leap_hand_right.urdf
  wrist_link_name: "base"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  target_origin_link_names: [ "base", "base", "base", "base" ]
  target_task_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/leap_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ../assets/leap_hand_description/leap_hand_right.urdf  #leap_hand/leap_hand_right.urdf
  wrist_link_name: "base"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  finger_tip_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### rl_policy/taco_dataset/dex_retargeting/configs/teleop/schunk_svh_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: schunk_hand/schunk_svh_hand_left.urdf
  wrist_link_name: "left_hand_base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'left_hand_Thumb_Opposition', 'left_hand_Thumb_Flexion', 'left_hand_Index_Finger_Proximal',
                        'left_hand_Index_Finger_Distal', 'left_hand_Finger_Spread', 'left_hand_Pinky',
                        'left_hand_Ring_Finger', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal' ]
  target_origin_link_names: [ "left_hand_base_link","left_hand_base_link", "left_hand_base_link", "left_hand_base_link", "left_hand_base_link", ]
  target_task_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2


  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20, ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

## Python signatures and reward/observation bodies (174 files)


### rl_policy/Pointnet2_PyTorch/pointnet2/models/pointnet2_msg_cls.py

```
class PointNet2ClassificationMSG(PointNet2ClassificationSSG)
    def _build_model(self)
```

### rl_policy/Pointnet2_PyTorch/pointnet2/models/pointnet2_msg_sem.py

```
class PointNet2SemSegMSG(PointNet2SemSegSSG)
    def _build_model(self)
```

### rl_policy/Pointnet2_PyTorch/pointnet2/models/pointnet2_ssg_cls.py

```
def set_bn_momentum_default(bn_momentum)
class BNMomentumScheduler(LambdaLR)
    def __init__(self, model, bn_lambda, last_epoch, setter)
    def step(self, epoch)
    def state_dict(self)
    def load_state_dict(self, state)
class PointNet2ClassificationSSG(LightningModule)
    def __init__(self, hparams)
    def _build_model(self)
    def _break_up_pc(self, pc)
    def forward(self, pointcloud)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def validation_end(self, outputs)
    def configure_optimizers(self)
    def prepare_data(self)
    def _build_dataloader(self, dset, mode)
    def train_dataloader(self)
    def val_dataloader(self)
```

### rl_policy/Pointnet2_PyTorch/pointnet2/models/pointnet2_ssg_sem.py

```
class PointNet2SemSegSSG(PointNet2ClassificationSSG)
    def _build_model(self)
    def forward(self, pointcloud)
    def prepare_data(self)
```

### rl_policy/Pointnet2_PyTorch/pointnet2/train.py

```
def hydra_params_to_dotdict(hparams)
def main(cfg)
```

### rl_policy/Pointnet2_PyTorch/pointnet2_ops_lib/pointnet2_ops/pointnet2_modules.py

```
def build_shared_mlp(mlp_spec, bn)
class _PointnetSAModuleBase(Module)
    def __init__(self)
    def forward(self, xyz, features)
class PointnetSAModuleMSG(_PointnetSAModuleBase)
    """Pointnet set abstrction layer with multiscale grouping

Parameters
----------
npoint : int
    Number of features
radii : list of float32
    list of radii to group with
nsamples : list of int32
    Number of samples in each ball query
mlps : list of list of int32
    Spec of the pointnet before the"""
    def __init__(self, npoint, radii, nsamples, mlps, bn, use_xyz)
class PointnetSAModule(PointnetSAModuleMSG)
    """Pointnet set abstrction layer

Parameters
----------
npoint : int
    Number of features
radius : float
    Radius of ball
nsample : int
    Number of samples in the ball query
mlp : list
    Spec of the pointnet before the global max_pool
bn : bool
    Use batchnorm"""
    def __init__(self, mlp, npoint, radius, nsample, bn, use_xyz)
class PointnetFPModule(Module)
    """Propigates the features of one set to another

Parameters
----------
mlp : list
    Pointnet module parameters
bn : bool
    Use batchnorm"""
    def __init__(self, mlp, bn)
    def forward(self, unknown, known, unknow_feats, known_feats)
```

### rl_policy/Pointnet2_PyTorch/pointnet2_ops_lib/pointnet2_ops/pointnet2_utils.py

```
class FurthestPointSampling(Function)
    def forward(ctx, xyz, npoint)
    def backward(ctx, grad_out)
class GatherOperation(Function)
    def forward(ctx, features, idx)
    def backward(ctx, grad_out)
class ThreeNN(Function)
    def forward(ctx, unknown, known)
    def backward(ctx, grad_dist, grad_idx)
class ThreeInterpolate(Function)
    def forward(ctx, features, idx, weight)
    def backward(ctx, grad_out)
class GroupingOperation(Function)
    def forward(ctx, features, idx)
    def backward(ctx, grad_out)
class BallQuery(Function)
    def forward(ctx, radius, nsample, xyz, new_xyz)
    def backward(ctx, grad_out)
class QueryAndGroup(Module)
    """Groups with a ball query of radius

Parameters
---------
radius : float32
    Radius of ball
nsample : int32
    Maximum number of features to gather in the ball"""
    def __init__(self, radius, nsample, use_xyz)
    def forward(self, xyz, new_xyz, features)
class GroupAll(Module)
    """Groups all features

Parameters
---------"""
    def __init__(self, use_xyz)
    def forward(self, xyz, new_xyz, features)
```

### rl_policy/Pointnet2_PyTorch/tests/conftest.py

```
def build_cfg(overrides)
def get_model(overrides)
def _test_loop(model, inputs, labels)
def cls_test(model)
def semseg_test(model)
```

### rl_policy/Pointnet2_PyTorch/tests/test_cls.py

```
def test_cls(use_xyz, model)
```

### rl_policy/Pointnet2_PyTorch/tests/test_semseg.py

```
def test_semseg(use_xyz, model)
```

### rl_policy/algo/bc/bc.py

```
class Visualizer3D()
    def reset(self)
    def __init__(self)
    def visualize_point_clouds(self, points, poses, colors)
    def visualize_poses(self, poses, size)
    def draw(self, discard)
class BCPPO(Module)
    def __init__(self, vec_env, train_param, dataset_file, log_dir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def update(self)
    def log(self, locs, width, pad)
```

### rl_policy/algo/common/module.py

```
class PointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, pretrained_model_path)
    def forward(self, input_obs)
class TransPointNetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, state_dim, use_seg)
    def forward(self, input_obs)
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def get_pc_observation(self, observations)
    def get_all_observation(self, observations)
    def act(self, observations, grad)
    def act_inference(self, observations)
    def evaluate(self, observations, actions)
def get_activation(act_name)

```python
def get_pc_observation(self, observations):
        robot_state = observations[:, self.robostate_indices]
        pc = observations[:, self.pointcloud_indices].reshape(-1, self.num_downsample, self.each_point_dim)
        input_data = dict(pc=pc)
        if self.use_seg:
            raise NotImplementedError   
            mask = observations[:, -2 * self.num_downsample-1:-1].reshape(-1, self.num_downsample, 2)
            input_data.update(dict(mask=mask,))
        if self.backbone_type == "TransPointNetBackbone":
            raise NotImplementedError 
            input_data.update(dict(state=robot_state,))
        pc_feature = self.backbone(input_data).reshape(len(observations), -1)
        return pc_feature
```

```python
def get_all_observation(self, observations):
        all_observation = observations[:, self.robostate_indices]
        if self.use_pc:
            pc_feature = self.get_pc_observation(observations)
            all_observation = torch.cat([all_observation, pc_feature], dim=1)
        if self.use_objlabel:
            obj_label = observations[:, self.objlabel_indices] * 255
            objlabel_feature = self.objlabel_emb(obj_label.long()).mean(dim=1)
            all_observation = all_observation + objlabel_feature
        if self.use_futureobjps:
            future_objps = observations[:, self.futureobjps_indices]
            all_observation = torch.cat([all_observation, future_objps], dim=1)
        return all_observation
```
```

### rl_policy/algo/common/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class DaggerStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, left_actions, right_actions, left_rewards, right_rewards, dones, left_values, right_values, expert_left_actions, expert_right_actions, expert_left_values, expert_right_values)
    def clear(self)
    def compute_returns(self, last_left_values, last_right_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class IPPODaggerStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, left_actions, right_actions, left_rewards, right_rewards, dones, left_values, right_values, expert_id)
    def add_transitions_with_expert_labels(self, observations, states, left_actions, right_actions, left_rewards, right_rewards, dones, left_values, right_values, expert_left_actions, expert_left_values, expert_right_actions, expert_right_values, expert_id)
    def clear(self)
    def compute_returns(self, last_left_values, last_right_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class PPODaggerStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, expert_id)
    def add_transitions_with_expert_labels(self, observations, states, actions, rewards, dones, values, expert_actions, expert_values, expert_id)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
class BCStorage()
    def __init__(self, dataset_obs, dataset_act, device, sampler)
    def mini_batch_generator(self, num_mini_batches)
```

### rl_policy/algo/dagger/dagger.py

```
class DaggerValue(Module)
    def __init__(self, vec_env, train_param, expert_class, log_dir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def update(self)
    def expert_batch_act(self, current_obs)
    def symlog(x)
    def log(self, locs, width, pad)
```

### rl_policy/algo/dagger/m2dagger.py

```
class M2DaggerValue(Module)
    def __init__(self, vec_env, train_param, expert_class, log_dir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def update(self)
    def expert_batch_act(self, current_obs, expertid_batch)
    def add_expert_labels(self)
    def symlog(x)
    def log(self, locs, width, pad)
```

### rl_policy/algo/dagger/m3dagger.py

```
def nonzero_mean(x)
class M3DaggerValueIPPO(Module)
    def __init__(self, vec_env, train_param, expert_class, log_dir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def update(self)
    def expert_batch_act(self, current_obs, expertid_batch)
    def add_expert_labels(self)
    def symlog(x)
    def log(self, locs, width, pad)
class M3DaggerValuePPO(Module)
    def __init__(self, vec_env, train_param, expert_class, log_dir)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def update(self)
    def expert_batch_act(self, current_obs, expertid_batch)
    def add_expert_labels(self)
    def symlog(x)
    def log(self, locs, width, pad)
```

### rl_policy/algo/marl/happo.py

```
class HAPPO()
    """Trainer class for HAPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (HAPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### rl_policy/algo/marl/mappo.py

```
"""# @Time    : 2021/7/1 6:52 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : r_mappo.py"""
class MAPPO()
    """Trainer class for MAPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (R_MAPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### rl_policy/algo/pn_utils/act.py

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

### rl_policy/algo/pn_utils/cnn.py

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

### rl_policy/algo/pn_utils/distributions.py

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

### rl_policy/algo/pn_utils/maniskill_learn/apis/train_rl.py

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

### rl_policy/algo/pn_utils/maniskill_learn/methods/brl/bc.py

```
"""Behavior cloning(BC)"""
class BC(BaseAgent)
    def __init__(self, policy_cfg, obs_shape, action_shape, action_space, batch_size)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/brl/bcq.py

```
"""Off-Policy Deep Reinforcement Learning without Exploration
    https://arxiv.org/abs/1812.02900"""
class BCQ(BaseAgent)
    def __init__(self, value_cfg, policy_vae_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, lmbda, num_random_action_train, num_random_action_eval, target_update_interval)
    def forward(self, obs)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/brl/cql.py

```
"""Conservative Q-Learning for Offline Reinforcement Learning:
    https://arxiv.org/pdf/2006.04779"""
class CQL(SAC)
    def __init__(self, num_action_sample, forward_block, automatic_regularization_tuning, lagrange_thresh, alpha_prime, temperature, min_q_weight, min_q_with_entropy, alpha_prime_optim_cfg, target_q_with_entropy, reward_scale)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/brl/td3_bc.py

```
"""A Minimalist Approach toOffline Reinforcement Learning:
    https://arxiv.org/pdf/2106.06860.pdf"""
class TD3_BC(TD3)
    def __init__(self, alpha, reward_scale)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/builder.py

```
def build_mfrl(cfg, default_args)
def build_brl(cfg, default_args)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/curl.py

```
class CURL(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, feature_dim)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/curl_old.py

```
class CURL(BaseAgent)
    def __init__(self, encoder_cfg, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, feature_dim, encoder_optim_cfg)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/gail.py

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

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/sac.py

```
"""Soft Actor-Critic Algorithms and Applications:
    https://arxiv.org/abs/1812.05905
Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor:
   https://arxiv.org/abs/1801.01290"""
class SAC(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/sac_bc.py

```
"""Soft Actor-Critic Algorithms and Applications:
    https://arxiv.org/abs/1812.05905
Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor:
   https://arxiv.org/abs/1801.01290"""
class SAC_BC(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, discrim_batch, update_coeff, alpha, target_update_interval, automatic_alpha_tuning, alpha_optim_cfg, alpha2)
    def update_parameters(self, memory, updates, expert_replay)
```

### rl_policy/algo/pn_utils/maniskill_learn/methods/mfrl/td3.py

```
class TD3(BaseAgent)
    def __init__(self, policy_cfg, value_cfg, obs_shape, action_shape, action_space, batch_size, gamma, update_coeff, action_noise, noise_clip, policy_update_interval)
    def update_parameters(self, memory, updates)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/backbones/mlp.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/backbones/nn_utils.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/backbones/pointnet.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/backbones/transformer.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/backbones/vae.py

```
class CVAE(Module)
    def __init__(self, encoder_cfg, decoder_cfg, latent_dim, log_sig_min, log_sig_max)
    def forward(self, cond, var)
    def decode(self, cond, z)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/builder.py

```
def build(cfg, registry, default_args)
def build_dense_head(cfg)
def build_backbone(cfg)
def build_model(cfg, default_args)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/dense_heads/deterministic.py

```
class DeterministicHead(ExtendedModule)
    def __init__(self, scale_prior, bias_prior, noise_std)
    def forward(self, feature, num_actions)
    def clamp_action(self, action)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/dense_heads/gaussian.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/activation.py

```
class Clamp(Module)
    def __init__(self, min, max)
    def forward(self, x)
def build_activation_layer(cfg)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/attention.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/conv.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/conv_module.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/norm.py

```
def infer_abbr(class_type)
def build_norm_layer(cfg, num_features, postfix)
def is_norm(layer, exclude)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/padding.py

```
def build_padding_layer(cfg)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/modules/weight_init.py

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

### rl_policy/algo/pn_utils/maniskill_learn/networks/policy_network/continuous_policy.py

```
class ContinuousPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, num_actions, mode, detach_encoder)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/policy_network/vae_policy.py

```
class VAEPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action, decode)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/utils.py

```
def combine_obs_with_action(obs, action)
def get_kwargs_from_shape(obs_shape, action_shape)
def replace_placeholder_with_args(parameters)
def soft_update(target, source, tau)
def hard_update(target, source)
```

### rl_policy/algo/pn_utils/maniskill_learn/networks/value_network/continuous_value.py

```
class ContinuousValue(ExtendedModule)
    def __init__(self, nn_cfg, obs_shape, action_shape, num_heads, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action)
```

### rl_policy/algo/pn_utils/maniskill_learn/optimizers/builder.py

```
def register_torch_optimizers()
def build_optimizer_constructor(cfg)
def build_optimizer(model, cfg)
```

### rl_policy/algo/pn_utils/maniskill_learn/optimizers/default_constructor.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/external/web_utils.py

```
def check_url_exists(url)
def get_confirm_token(response)
def save_response_content(response, destination)
def get_google_file_index(file_url)
def md5sum(filename, block_size)
def check_md5sum(filename, md5, block_size)
def download_file_from_google_drive(file_url, destination, cached, md5)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/h5_utils.py

```
def load_h5_as_dict_array(h5)
def load_h5s_as_list_dict_array(h5)
def merge_h5_trajectory(h5_files, output_name)
def generate_chunked_h5_replay(h5_files, name, folder, num_files)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/hash_utils.py

```
def md5sum(filename, block_size)
def check_md5sum(filename, md5, block_size)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/base.py

```
class BaseFileHandler()
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
    def load_from_path(self, filepath, mode)
    def dump_to_path(self, obj, filepath, mode)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/csv_handler.py

```
class CSVHandler(BaseFileHandler)
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/pickle_handler.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/serialization/io.py

```
def load(file, file_format)
def dump(obj, file, file_format)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/fileio/serialization/utils.py

```
def serialize(obj)
def deserialize(obj)
def list_from_file(filename, prefix, offset, max_num)
def dict_from_file(filename, key_type, offset, max_num)
def dict_to_csv_table(x)
def csv_table_to_dict(x)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/math/split_array.py

```
def split_num(num, n)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/collect_env.py

```
def get_PIL_version()
def collect_base_env()
def collect_env()
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/config.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/logger.py

```
def get_logger(name, with_stream, log_file, log_level)
def get_root_logger(log_file, log_level)
def print_log(msg, logger, level)
def flush_print()
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/module_utils.py

```
def import_modules_from_strings(imports, allow_failed_imports)
def check_prerequisites(prerequisites, checker, msg_tmpl)
def requires_package(prerequisites)
def requires_executable(prerequisites)
def deprecated_api_warning(name_dict, cls_name)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/path_utils.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/process_utils.py

```
def format_memory_str(x, unit, number_only)
def get_total_memory(unit, number_only, init_pid)
def get_memory_list(unit, number_only, init_pid)
def get_memory_dict(unit, number_only, init_pid)
def get_subprocess_ids(init_pid)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/random_utils.py

```
def set_random_seed(seed)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/registry.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/meta/timer.py

```
def td_format(td_object)
def get_time_stamp()
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/checkpoint.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/cuda_utils.py

```
def get_gpu_memory_info(device, unit, number_only)
def get_gpu_memory_usage_by_process(process, device, unit, number_only)
def get_gpu_memory_usage_by_current_program(device, unit, number_only)
def get_gpu_utilization(device)
def get_cuda_info(device, unit, number_only)
def get_one_device(x)
def get_device(x)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/distributed_utils.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/misc.py

```
def disable_gradients(network)
def worker_init_fn(worker_id)
def no_grad(f)
def run_with_mini_batch(function, data, batch_size)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/module_utils.py

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

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/ops.py

```
def masked_average(x, axis, mask, keepdim)
def masked_max(x, axis, mask, keepdim, empty_value)
```

### rl_policy/algo/pn_utils/maniskill_learn/utils/torch/tensorboard/tensorboard_logger.py

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

### rl_policy/algo/pn_utils/maniskill_learn/version.py

```
def parse_version_info(version_str)
```

### rl_policy/algo/pn_utils/mlp.py

```
class MLPLayer(Module)
    def __init__(self, input_dim, hidden_size, layer_N, use_orthogonal, use_ReLU)
    def forward(self, x)
class MLPBase(Module)
    def __init__(self, config, obs_shape, cat_self, attn_internal)
    def forward(self, x)
```

### rl_policy/algo/pn_utils/model_3d.py

```
"""Full model"""
class PointNet2Feature(PointNet2ClassificationSSG)
    def _build_model(self)
    def forward(self, pointcloud)
```

### rl_policy/algo/pn_utils/pointnet.py

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

### rl_policy/algo/pn_utils/rnn.py

```
class RNNLayer(Module)
    def __init__(self, inputs_dim, outputs_dim, recurrent_N, use_orthogonal)
    def forward(self, x, hxs, masks)
```

### rl_policy/algo/pn_utils/sparseunet.py

```
class SparseUnetBackbone(Module)
    def __init__(self, pc_dim, feature_dim, channels, block_repeat, pretrained_model_path, use_domain_discrimination)
    def forward(self, input_pc)
    def apply_voxelization_batch(self, pc)
```

### rl_policy/algo/pn_utils/util.py

```
def init(module, weight_init, bias_init, gain)
def get_clones(module, N)
def check(input)
def masked_average(x, axis, mask, keepdim)
def masked_max(x, axis, mask, keepdim, empty_value)
```

### rl_policy/algo/ppo/ippo.py

```
class IPPO(Module)
    """indepenent PPO"""
    def __init__(self, vec_env, train_param, log_dir, apply_reset, obs_type)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def log(self, locs, width, pad)
class IPPOAgent(Module)
    def __init__(self, vec_env, train_param, obs_type)
    def update(self)
```

### rl_policy/algo/ppo/ppo.py

```
class PPO()
    def __init__(self, vec_env, train_param, log_dir, obs_type, apply_reset)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self)
    def log(self, locs, width, pad)
    def update(self)
```

### rl_policy/main.py

```
def build_runner(cfg, env)
def main(cfg)
```

### rl_policy/taco_dataset/TACOdataset.py

```
def transformation_inverse_np(quat, pos)
def compute_relative_position_pos(a_position, b_position, b_orientation)
def compute_relative_position_pose(a_position, b_pose)
class Visualizer3D()
    def reset(self)
    def __init__(self)
    def visualize_point_clouds(self, points, poses, colors)
    def visualize_poses(self, poses, size)
    def draw(self, discard)
class TACODataset()
    def __init__(self, dataset_dir, mano_model_path, optimize_wrist)
    def make_task(self, triplet, sequence_name, is_visualize)
    def make_dataset(self, triplet, save_dir, vis_ref, num_max, num_finger)
    def make_mano_dataset(self, triplet, save_dir, num_finger, num_max)
    def get_key_timesteps(self, object_poses, tool_poses)
    def conjugate(self, objrot)
    def low_pass_filter(data, cutoff, fs, order)
    def mano_params_to_hand_info(self, hand_pose_path, mano_beta, side, max_cnt, return_pose, return_faces, device)
    def create_urdf(self, tool_dict, target_dict, save_path)
    def visualize_open3d(self, tool_model, target_model, tool_poses, target_poses, right_hand_meshes, left_hand_meshes, save_path, sampling_rate, device)
    def _trimesh_to_open3d(self, trimesh_mesh)
    def _generate_urdf(self, object_dict)
    def visualize_robot_and_mano(self, triplet, side)
    def sample_grasp_center_from_pointcloud(self, object_mesh_file, rel_keypoints, scale, topk, num_samples)
class BiRetargetor()
    def __init__(self, robot_name, retarget_type, add_dummy_free_joint)
    def get_retargetor(self, config_path, add_dummy_free_joint, return_robot)
    def retarget_to_robot_poses(self, left_joint_pos, right_joint_pos, num_optimize)
    def retarget_to_armrobot_poses(self, left_joint_pos, right_joint_pos, num_optimize)
    def get_joint_keypoints(self, hand_pose_frame, use_camera_frame)
    def estimate_frame_from_hand_points(keypoint_3d_array, side)
```

### rl_policy/taco_dataset/dex_retargeting/constants.py

```
class RobotName(Enum)
class RetargetingType(Enum)
class HandType(Enum)
def get_default_config_path(robot_name, retargeting_type, hand_type)
```

### rl_policy/taco_dataset/dex_retargeting/kinematics_adaptor.py

```
class KinematicAdaptor()
    def __init__(self, robot, target_joint_names)
    def forward_qpos(self, qpos)
    def backward_jacobian(self, jacobian)
class MimicJointKinematicAdaptor(KinematicAdaptor)
    def __init__(self, robot, target_joint_names, source_joint_names, mimic_joint_names, multipliers, offsets)
    def forward_qpos(self, pin_qpos)
    def backward_jacobian(self, jacobian)
```

### rl_policy/taco_dataset/dex_retargeting/optimizer.py

```
class Optimizer()
    def __init__(self, robot, wrist_link_name, target_joint_names, target_link_human_indices)
    def set_joint_limit(self, joint_limits, epsilon)
    def get_link_indices(self, target_link_names)
    def set_kinematic_adaptor(self, adaptor)
    def retarget(self, ref_value, fixed_qpos, last_qpos)
    def get_objective_function(self, ref_value, fixed_qpos, last_qpos)
    def fixed_joint_names(self)
class PositionOptimizer(Optimizer)
    def __init__(self, robot, wrist_link_name, target_joint_names, target_link_names, target_link_human_indices, huber_delta, norm_delta)
    def get_objective_function(self, target_pos, fixed_qpos, last_qpos)
class VectorOptimizer(Optimizer)
    def __init__(self, robot, wrist_link_name, target_joint_names, target_origin_link_names, target_task_link_names, target_link_human_indices, huber_delta, norm_delta, scaling)
    def get_objective_function(self, target_vector, fixed_qpos, last_qpos)
class DexPilotOptimizer(Optimizer)
    """Retargeting optimizer using the method proposed in DexPilot

This is a broader adaptation of the original optimizer delineated in the DexPilot paper.
While the initial DexPilot study focused solely on the four-fingered Allegro Hand, this version of the optimizer
embraces the same principles for both"""
    def __init__(self, robot, target_joint_names, finger_tip_link_names, wrist_link_name, target_link_human_indices, huber_delta, norm_delta, project_dist, escape_dist, eta1, eta2, scaling)
    def get_objective_function(self, target_vector, fixed_qpos, last_qpos)
```

### rl_policy/taco_dataset/dex_retargeting/optimizer_utils.py

```
class LPFilter()
    def __init__(self, alpha)
    def next(self, x)
    def reset(self)
```

### rl_policy/taco_dataset/dex_retargeting/retargeting_config.py

```
class RetargetingConfig()
    def __post_init__(self)
    def set_default_urdf_dir(cls, urdf_dir)
    def load_from_file(cls, config_path, override)
    def from_dict(cls, cfg, override)
    def build(self)
def get_retargeting_config(config_path)
def parse_mimic_joint(robot_urdf)
```

### rl_policy/taco_dataset/dex_retargeting/robot_wrapper.py

```
class RobotWrapper()
    """This class does not take mimic joint into consideration"""
    def __init__(self, urdf_path, use_collision, use_visual)
    def joint_names(self)
    def dof_joint_names(self)
    def dof(self)
    def link_names(self)
    def joint_limits(self)
    def get_joint_index(self, name)
    def get_link_index(self, name)
    def compute_forward_kinematics(self, qpos)
    def get_link_pose(self, link_id)
    def get_link_pose_inv(self, link_id)
    def compute_single_link_local_jacobian(self, qpos, link_id)
```

### rl_policy/taco_dataset/dex_retargeting/seq_retarget.py

```
class SeqRetargeting()
    def __init__(self, optimizer, has_joint_limits, lp_filter)
    def warm_start(self, wrist_pos, wrist_orientation, global_rot)
    def retarget(self, ref_value, fixed_qpos)
    def verbose(self)
    def reset(self)
    def joint_names(self)
```

### rl_policy/taco_dataset/dex_retargeting/yourdfpy.py

```
def _array_eq(arr1, arr2)
class TransmissionJoint()
    def __eq__(self, other)
class Actuator()
    def __eq__(self, other)
class Transmission()
    def __eq__(self, other)
class Calibration()
class Mimic()
class SafetyController()
class Sphere()
class Cylinder()
class Box()
    def __eq__(self, other)
class Mesh()
    def __eq__(self, other)
class Geometry()
class Color()
    def __eq__(self, other)
class Texture()
class Material()
class Visual()
    def __eq__(self, other)
class Collision()
    def __eq__(self, other)
class Inertial()
    def __eq__(self, other)
class Link()
    def __eq__(self, other)
class Dynamics()
class Limit()
class Joint()
    def __eq__(self, other)
class Robot()
    def __eq__(self, other)
class URDFError(Exception)
    """General URDF exception."""
    def __init__(self, msg)
    def __str__(self)
    def __repr__(self)
class URDFIncompleteError(URDFError)
    """Raised when needed data for an object isn't there."""
class URDFAttributeValueError(URDFError)
    """Raised when attribute value is not contained in the set of allowed values."""
class URDFBrokenRefError(URDFError)
    """Raised when a referenced object is not found in the scope."""
class URDFMalformedError(URDFError)
    """Raised when data is found to be corrupted in some way."""
class URDFUnsupportedError(URDFError)
    """Raised when some unexpectedly unsupported feature is found."""
class URDFSaveValidationError(URDFError)
    """Raised when XML validation fails when saving."""
def _str2float(s)
def apply_visual_color(geom, visual, material_map)
def filename_handler_null(fname)
def filename_handler_ignore_directive(fname)
def filename_handler_ignore_directive_package(fname)
def filename_handler_add_prefix(fname, prefix)
def filename_handler_absolute2relative(fname, dir)
def filename_handler_relative(fname, dir)
def filename_handler_relative_to_urdf_file(fname, urdf_fname)
def filename_handler_relative_to_urdf_file_recursive(fname, urdf_fname, level)
def _create_filename_handlers_to_urdf_file_recursive(urdf_fname)
def filename_handler_meta(fname, filename_handlers)
def filename_handler_magic(fname, dir)
def validation_handler_strict(errors)
class URDF()
    def __init__(self, robot, build_scene_graph, build_collision_scene_graph, load_meshes, load_collision_meshes, filename_handler, mesh_dir, force_mesh, force_collision_mesh, build_tree)
    def scene(self)
    def collision_scene(self)
    def link_map(self)
    def joint_map(self)
    def joint_names(self)
    def actuated_joints(self)
    def actuated_dof_indices(self)
    def actuated_joint_indices(self)
    def actuated_joint_names(self)
    def num_actuated_joints(self)
    def num_dofs(self)
    def zero_cfg(self)
    def center_cfg(self)
    def cfg(self)
    def base_link(self)
    def errors(self)
    def clear_errors(self)
    def show(self, collision_geometry, callback)
    def validate(self, validation_fn)
    def _create_maps(self)
    def _update_actuated_joints(self)
    def _validate_required_attribute(self, attribute, error_msg, allowed_values)
    def load(fname_or_file, add_dummy_free_joints)
    def contains(self, key, value, element)
    def _determine_base_link(self)
    def _forward_kinematics_joint(self, joint, q)
    def update_cfg(self, configuration)
    def get_transform(self, frame_to, frame_from, collision_geometry)
    def _link_mesh(self, link, collision_geometry)
    def _geometry2trimeshscene(self, geometry, load_file, force_mesh, skip_materials)
    def _add_geometries_to_scene(self, s, geometries, link_name, load_geometry, force_mesh, force_single_geometry, skip_materials)
    def _create_scene(self, use_collision_geometry, load_geometry, force_mesh, force_single_geometry_per_link)
    def _successors(self, node)
    def _create_subrobot(self, robot_name, root_link_name)
    def split_along_joints(self, joint_type)
    def validate_filenames(self)
    def write_xml(self)
    def write_xml_string(self)
    def write_xml_file(self, fname)
    def _parse_mimic(xml_element)
    def _write_mimic(self, xml_parent, mimic)
    def _parse_safety_controller(xml_element)
    def _write_safety_controller(self, xml_parent, safety_controller)
    def _parse_transmission_joint(xml_element)
    def _write_transmission_joint(self, xml_parent, transmission_joint)
    def _parse_actuator(xml_element)
    def _write_actuator(self, xml_parent, actuator)
    def _parse_transmission(xml_element)
    def _write_transmission(self, xml_parent, transmission)
    def _parse_calibration(xml_element)
    def _write_calibration(self, xml_parent, calibration)
    def _parse_box(xml_element)
    def _write_box(self, xml_parent, box)
    def _parse_cylinder(xml_element)
    def _write_cylinder(self, xml_parent, cylinder)
    def _parse_sphere(xml_element)
    def _write_sphere(self, xml_parent, sphere)
    def _parse_scale(xml_element)
    def _write_scale(self, xml_parent, scale)
    def _parse_mesh(xml_element)
    def _write_mesh(self, xml_parent, mesh)
    def _parse_geometry(xml_element)
    def _validate_geometry(self, geometry)
    def _write_geometry(self, xml_parent, geometry)
    def _parse_origin(xml_element)
    def _write_origin(self, xml_parent, origin)
    def _parse_color(xml_element)
    def _write_color(self, xml_parent, color)
    def _parse_texture(xml_element)
    def _write_texture(self, xml_parent, texture)
    def _parse_material(xml_element)
    def _write_material(self, xml_parent, material)
    def _parse_visual(xml_element)
    def _validate_visual(self, visual)
    def _write_visual(self, xml_parent, visual)
    def _parse_collision(xml_element)
    def _validate_collision(self, collision)
    def _write_collision(self, xml_parent, collision)
    def _parse_inertia(xml_element)
    def _write_inertia(self, xml_parent, inertia)
    def _parse_mass(xml_element)
    def _write_mass(self, xml_parent, mass)
    def _parse_inertial(xml_element)
    def _write_inertial(self, xml_parent, inertial)
    def _parse_link(xml_element)
    def _validate_link(self, link)
    def _write_link(self, xml_parent, link)
    def _parse_axis(xml_element)
    def _write_axis(self, xml_parent, axis)
    def _parse_limit(xml_element)
    def _validate_limit(self, limit, type)
    def _write_limit(self, xml_parent, limit)
    def _parse_dynamics(xml_element)
    def _write_dynamics(self, xml_parent, dynamics)
    def _parse_joint(xml_element)
    def _validate_joint(self, joint)
    def _write_joint(self, xml_parent, joint)
    def _parse_robot(xml_element, add_dummy_free_joints)
    def _validate_robot(self, robot)
    def _write_robot(self, robot)
    def __eq__(self, other)
    def filename_handler(self)
    def build_tree(self)
    def update_kinematics(self, configuration)
    def get_link_global_transform(self, link_name)
def _add_dummy_joints(robot, root_link_name)
```

### rl_policy/taco_dataset/manopth/mano/webuser/lbs.py

```
"""Copyright 2017 Javier Romero, Dimitrios Tzionas, Michael J Black and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the MANO/SMPL+H Model license here http://mano.is.tue.mpg.de/license

More information about MANO/SMPL+H is available at http://mano.is.tue.mpg.de.
For comments or questions, please email us at: mano@tue.mpg.de


About this file:
================
This file defines a wrapper for the loading functions of the MANO model.

Modules included:
- load_model:
  loads the MANO model f"""
def global_rigid_transformation(pose, J, kintree_table, xp)
def verts_core(pose, v, J, weights, kintree_table, want_Jtr, xp)
```

### rl_policy/taco_dataset/manopth/mano/webuser/posemapper.py

```
"""Copyright 2017 Javier Romero, Dimitrios Tzionas, Michael J Black and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the MANO/SMPL+H Model license here http://mano.is.tue.mpg.de/license

More information about MANO/SMPL+H is available at http://mano.is.tue.mpg.de.
For comments or questions, please email us at: mano@tue.mpg.de


About this file:
================
This file defines a wrapper for the loading functions of the MANO model.

Modules included:
- load_model:
  loads the MANO model f"""
class Rodrigues(Ch)
    def compute_r(self)
    def compute_dr_wrt(self, wrt)
def lrotmin(p)
def posemap(s)
```

### rl_policy/taco_dataset/manopth/mano/webuser/serialization.py

```
"""Copyright 2017 Javier Romero, Dimitrios Tzionas, Michael J Black and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the MANO/SMPL+H Model license here http://mano.is.tue.mpg.de/license

More information about MANO/SMPL+H is available at http://mano.is.tue.mpg.de.
For comments or questions, please email us at: mano@tue.mpg.de


About this file:
================
This file defines a wrapper for the loading functions of the MANO model.

Modules included:
- load_model:
  loads the MANO model f"""
def ready_arguments(fname_or_dict)
def load_model(fname_or_dict)
```

### rl_policy/taco_dataset/manopth/mano/webuser/smpl_handpca_wrapper_HAND_only.py

```
"""Copyright 2017 Javier Romero, Dimitrios Tzionas, Michael J Black and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the MANO/SMPL+H Model license here http://mano.is.tue.mpg.de/license

More information about MANO/SMPL+H is available at http://mano.is.tue.mpg.de.
For comments or questions, please email us at: mano@tue.mpg.de


About this file:
================
This file defines a wrapper for the loading functions of the MANO model.

Modules included:
- load_model:
  loads the MANO model f"""
def ready_arguments(fname_or_dict, posekey4vposed)
def load_model(fname_or_dict, ncomps, flat_hand_mean, v_template)
```

### rl_policy/taco_dataset/manopth/mano/webuser/verts.py

```
"""Copyright 2017 Javier Romero, Dimitrios Tzionas, Michael J Black and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the MANO/SMPL+H Model license here http://mano.is.tue.mpg.de/license

More information about MANO/SMPL+H is available at http://mano.is.tue.mpg.de.
For comments or questions, please email us at: mano@tue.mpg.de


About this file:
================
This file defines a wrapper for the loading functions of the MANO model.

Modules included:
- load_model:
  loads the MANO model f"""
def ischumpy(x)
def verts_decorated(trans, pose, v_template, J_regressor, weights, kintree_table, bs_style, f, bs_type, posedirs, betas, shapedirs, want_Jtr)
def verts_core(pose, v, J, weights, kintree_table, bs_style, want_Jtr, xp)
```

### rl_policy/taco_dataset/manopth/manopth/argutils.py

```
def print_args(args)
def save_args(args, save_folder, opt_prefix, verbose)
```

### rl_policy/taco_dataset/manopth/manopth/axislayer.py

```
class AxisLayer(Module)
    def __init__(self)
    def forward(self, hand_joints, transf)
```

### rl_policy/taco_dataset/manopth/manopth/demo.py

```
def generate_random_hand(batch_size, ncomps, mano_root)
def display_hand(hand_info, mano_faces, ax, alpha, batch_idx, show)
def cam_equal_aspect_3d(ax, verts, flip_x)
```

### rl_policy/taco_dataset/manopth/manopth/manolayer.py

```
class ManoLayer(Module)
    def __init__(self, center_idx, flat_hand_mean, ncomps, side, mano_root, use_pca, root_rot_mode, joint_rot_mode, robust_rot)
    def forward(self, th_pose_coeffs, th_betas, th_trans, root_palm, share_betas)
```

### rl_policy/taco_dataset/manopth/manopth/manolayer_axis.py

```
class ManoLayer(Module)
    def __init__(self, center_idx, flat_hand_mean, ncomps, side, mano_root, use_pca, root_rot_mode, joint_rot_mode, robust_rot)
    def forward(self, th_pose_coeffs, th_betas, th_trans, root_palm, share_betas)
```

### rl_policy/taco_dataset/manopth/manopth/quatutils.py

```
def normalize_quaternion(quaternion, eps)
def quaternion_inv(q)
def quaternion_mul(q, r)
def quaternion_to_angle_axis(quaternion)
def angle_axis_to_quaternion(angle_axis)
def quaternion_to_rotation_matrix(quaternion)
def quaternion_norm(quaternion)
def quaternion_norm_squared(quaternion)
def __quaternion_to_angle(quaternion)
```

### rl_policy/taco_dataset/manopth/manopth/rodrigues_layer.py

```
"""This part reuses code from https://github.com/MandyMo/pytorch_HMR/blob/master/src/util.py
which is part of a PyTorch port of SMPL.
Thanks to Zhang Xiong (MandyMo) for making this great code available on github !"""
def quat2mat(quat)
def batch_rodrigues(axisang)
def th_get_axis_angle(vector)
```

### rl_policy/taco_dataset/manopth/manopth/rot6d.py

```
def compute_rotation_matrix_from_ortho6d(poses)
def robust_compute_rotation_matrix_from_ortho6d(poses)
def normalize_vector(v)
def cross_product(u, v)
```

### rl_policy/taco_dataset/manopth/manopth/rotproj.py

```
def batch_rotprojs(batches_rotmats)
```

### rl_policy/taco_dataset/manopth/manopth/tensutils.py

```
def th_posemap_axisang(pose_vectors)
def th_with_zeros(tensor)
def th_pack(tensor)
def subtract_flat_id(rot_mats)
def make_list(tensor)
```

### rl_policy/taco_dataset/manopth/setup.py

```
def check_dependencies()
```

### rl_policy/taco_dataset/manopth/test/test_demo.py

```
def test_generate_random_hand()
```

### rl_policy/taco_dataset/setup.py

```
def setup_package()
```

### rl_policy/tasks/bi_leap_hand_grasp_bc.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def farthest_point_sample(xyz, npoint, device, init)
def index_points(points, idx, device)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
def read_pointcloud_from_urdf(urdf_file, num_sample)
class BiLeapHandGraspBC(VecTask)
    """Dagger for multi object objects diversities and ids"""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights, left_robot_link1_pos, right_robot_link1_pos,
    frequency: float,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    object_grasp_pos, tool_grasp_pos,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_grasp_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_grasp_pos - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_grasp_pos, dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_grasp_pos, dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    # info["left_is_grasp"] = is_grasp_left
    # info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    # ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    # ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    # left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    # left_lift_object_rot_rew1 = ref_object_rot_rew
    # right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    # right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            self.is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:], self.stage1_cul_left_successes[:], self.stage1_cul_right_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes, self.stage1_cul_left_successes, self.stage1_cul_right_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights, self.left_robot_link1_pos, self.right_robot_link1_pos,
                self.frequency,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                self.actual_object_grasp_pos, self.actual_tool_grasp_pos,
                self.is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_pal
```

### rl_policy/tasks/bi_leap_hand_grasp_dagger.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_grasp_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, tool_pos, goal_height, left_palm_pos, right_palm_pos, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, object_init_states, tool_init_states, action_penalty_scale, success_tolerance, av_factor, table_height, actions)
def compute_bvdex_stage1_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff, object_hand_joint_rot_diff)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff, is_stage1_hand_object_rew, is_stage1_lin_rew, is_stage2_pos_rew_exp)
def read_pointcloud_from_urdf(urdf_file, num_sample)
def get_pointcloud_from_src(asset_dir, device, num_sample)
class BiLeapHandGraspDagger(VecTask)
    """Dagger for single object id"""
    def get_obs_idx_num(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_urdf(self, tool_id, target_id, save_path)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_dataset(self)
    def _prepare_task(self, task_id)
    def _prepare_object_tool_pair(self, asset_root, vhacd_enabled)
    def _prepare_table_asset(self)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_grasp_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos, tool_pos,
    goal_height: float,
    left_palm_pos, right_palm_pos,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    object_init_states, tool_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    goal_tool_dist = torch.abs(goal_height - tool_pos[:, 2])
    left_palm_object_dist = torch.norm(object_pos - left_palm_pos, dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pos, dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)
    object_offset = torch.norm(object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1)
    tool_offset = torch.norm(tool_pos[:, 0:2] - tool_init_states[:, 0:2], dim=-1)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(goal_tool_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    lift_object_rew = torch.zeros_like(goal_object_dist)
    lift_object_rew = torch.where(
        is_grasp_left == True, 3 * (goal_height - table_height) - 2 * goal_object_dist, lift_object_rew
    )
    lift_tool_rew = torch.zeros_like(goal_tool_dist)
    lift_tool_rew = torch.where(
        is_grasp_right == True, 3 * (goal_height - table_height) - 2 * goal_tool_dist, lift_tool_rew
    )
    # stage 2: lift up reward
    left_hand_up_rew = torch.zeros_like(goal_object_dist)
    left_hand_up_rew = torch.where(is_grasp_left == True, 1 * (left_palm_pos[:, 2] - goal_height), left_hand_up_rew)
    right_hand_up_rew = torch.zeros_like(goal_tool_dist)
    right_hand_up_rew = torch.where(is_grasp_right == True, 1 * (right_palm_pos[:, 2] - goal_height), right_hand_up_rew)

    # stage 3: lift near goal bonus
    left_bonus = torch.zeros_like(goal_object_dist)
    left_bonus = torch.where(
        is_grasp_left == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), left_bonus
        ),
        left_bonus,
    )
    right_bonus = torch.zeros_like(goal_tool_dist)
    right_bonus = torch.where(
        is_grasp_right == True,
        torch.where(
            goal_tool_dist <= success_tolerance, 1.0 / (0.5 + goal_tool_dist), right_bonus
        ),
        right_bonus,
    )

    left_approach_penalty = dist_reward_scale * left_fingertips_object_dist + 2 * dist_reward_scale * left_palm_object_dist
    right_approach_penalty = dist_reward_scale * right_fingers_tool_dist + 2 * dist_reward_scale * right_palm_object_dist
    left_after_grasp_reward = lift_object_rew + left_hand_up_rew + left_bonus
    right_after_grasp_reward = lift_tool_rew + right_hand_up_rew + right_bonus
    object_offset_penalty = 0.3 * object_offset
    tool_offset_penalty = 0.3 * tool_offs
```

```python
def compute_bvdex_stage1_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff,
    ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff,
    object_hand_joint_rot_diff: int,
):
    object_pos = object_pose[:, :3]
    tool_pos = tool_pose[:, :3]
    info = {}

    left_palm_object_dist = torch.norm(object_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pose[:, :3], dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(right_palm_object_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pos, dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7].repeat(len(object_pose),1), object_pose[:, 3:7]) # [-1,1]
    left_lift_object_pos_rew, left_lift_object_rot_rew = torch.zeros_like(ref_object_pos_dist), torch.zeros_like(ref_object_rot_rew)
    left_lift_object_pos_rew = torch.where(is_grasp_left == True, 1 - ref_object_pos_dist / ref_init_object_pos_dist, left_lift_object_pos_rew)
    left_lift_object_rot_rew = torch.where(is_grasp_left == True, ref_object_rot_rew, left_lift_object_rot_rew)

    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pos, dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7].repeat(len(tool_pose),1), tool_pose[:, 3:7])  # [-1,1]
    right_lift_tool_pos_rew, right_lift_tool_rot_rew = torch.zeros_like(ref_tool_pos_dist), torch.zeros_like(ref_tool_rot_rew)
    right_lift_tool_pos_rew = torch.where(is_grasp_right == True, 1 - ref_tool_pos_dist / ref_init_tool_pos_dist, right_lift_tool_pos_rew)
    right_lift_tool_rot_rew = torch.where(is_grasp_right == True, ref_tool_rot_rew, right_lift_tool_rot_rew)

    # stage 2: hand-object joint rotation, no grasp condition
    if object_hand_joint_rot_diff:
        object_hand_rot_diff = quat_diff_theta(object_pose[:, 3:7], left_palm_pose[:, 3:7])
        left_object_hand_rot_rew = - torch.abs((ref_init_object_hand_rot_diff - object_hand_rot_diff))  # [0, -2pi]
        left_object_hand_rot_rew = 0.5 + left_object_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
        tool_hand_rot_diff = quat_diff_theta(tool_pose[:, 3:7], right_palm_pose[:, 3:7])
        right_tool_hand_rot_rew = - torch.abs((ref_init_tool_hand_rot_diff - tool_hand_rot_diff))  # [0, -2pi]
        right_tool_hand_rot_rew = 0.5 + right_tool_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
    else:
        left_object_hand_rot_rew = torch.
```

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    ta
```

### rl_policy/tasks/bi_leap_hand_grasp_m2dagger.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def farthest_point_sample(xyz, npoint, device, init)
def index_points(points, idx, device)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, actions, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, is_expect_end)
def read_pointcloud_from_urdf(urdf_file, num_sample)
class BiLeapHandGraspM2Dagger(VecTask)
    """Dagger for multi object objects diversities and ids"""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights,
    actions,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_pose[:, :3] - left_palm_pose[:, :3], dim=-1) 
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_pose[:, :3] - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_pose[:, :3], dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_pose[:, :3], dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch.logical_and(ref_object_pos_dist <= success_tolerance, left_fingertips_object_dist + left_palm_object_dist < 0.12 * (num_fingers + 1)).float()
    ri
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights,
                self.actions,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.left_fingertip_state[..., :3]
        self.left_fingertip_rot = self.left_fingertip_state[..., 3:7]

        self.rig
```

### rl_policy/tasks/bi_leap_hand_grasp_m3dagger.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def farthest_point_sample(xyz, npoint, device, init)
def index_points(points, idx, device)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
def read_pointcloud_from_urdf(urdf_file, num_sample)
class BiLeapHandGraspM3Dagger(VecTask)
    """Dagger for multi object objects diversities and ids"""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data, retargeting_data)
    def _prepare_table_asset(self, table_dims)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)
    def visualize(self)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights, left_robot_link1_pos, right_robot_link1_pos,
    frequency: float,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    object_grasp_pos, tool_grasp_pos,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_grasp_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_grasp_pos - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_grasp_pos, dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_grasp_pos, dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    # info["left_is_grasp"] = is_grasp_left
    # info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    # ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    # ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    # left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    # left_lift_object_rot_rew1 = ref_object_rot_rew
    # right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    # right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).long()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            self.is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:], self.stage1_cul_left_successes[:], self.stage1_cul_right_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes, self.stage1_cul_left_successes, self.stage1_cul_right_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights, self.left_robot_link1_pos, self.right_robot_link1_pos,
                self.frequency,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                self.actual_object_grasp_pos, self.actual_tool_grasp_pos,
                self.is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., 
```

### rl_policy/tasks/bi_leap_hand_grasp_multidagger.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, actions, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, is_expect_end)
def read_pointcloud_from_urdf(urdf_file, num_sample)
class BiLeapHandGraspMultiDagger(VecTask)
    """Dagger for multi object objects diversities and ids"""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights,
    actions,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_pose[:, :3] - left_palm_pose[:, :3], dim=-1) 
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_pose[:, :3] - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5, right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_pose[:, :3], dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_pose[:, :3], dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0, right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch.logical_and(ref_object_pos_dist <= success_tolerance, left_fingertips_object_dist + left_palm_object_dist < 0.12 * (num_fingers + 1)).float()
    right_successes = torch.logical_and(ref_tool_pos_dist <= success_tolerance, right_fingertips_tool_dist + right_palm_tool_dist < 0.12 * (num_fingers + 1)).float()
    left_reach_ref_
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights,
                self.actions,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.left_fingertip_state[..., :3]
        self.left_fingertip_rot = self.left_fingertip_state[..., 3:7]

        self.right_fingertip_state = self.rigid_body_states[:, self.right_fingertip_handles][..., :13]
    
```

### rl_policy/tasks/bi_leap_hand_grasp_v0.py

```
class BiLeapHandGraspV0(VecTask)
    """Initial bimanual grasping attempt"""
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file)
    def _prepare_object_asset(self, asset_root, asset_file)
    def _prepare_table_asset(self)
    def compute_reward(self)
    def compute_observations(self)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose)
def orientation_error(desired, current)
def rotation_6d_to_matrix(d6)
def standardize_quaternion(quaternions)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def compute_task_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, tool_pos, goal_height, left_palm_pos, right_palm_pos, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, object_init_states, tool_init_states, action_penalty_scale, success_tolerance, av_factor, table_height)

```python
def compute_task_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos, tool_pos,
    goal_height: float,
    left_palm_pos, right_palm_pos,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    object_init_states, tool_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    gool_tool_dist = torch.abs(goal_height - tool_pos[:, 2])
    left_palm_object_dist = torch.norm(object_pos - left_palm_pos, dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pos, dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)
    object_offset = torch.norm(object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1)
    tool_offset = torch.norm(tool_pos[:, 0:2] - tool_init_states[:, 0:2], dim=-1)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(gool_tool_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    lift_object_rew = torch.zeros_like(goal_object_dist)
    lift_object_rew = torch.where(
        is_grasp_left == True, 3 * (goal_height - table_height) - 2 * goal_object_dist, lift_object_rew
    )
    lift_tool_rew = torch.zeros_like(gool_tool_dist)
    lift_tool_rew = torch.where(
        is_grasp_right == True, 3 * (goal_height - table_height) - 2 * gool_tool_dist, lift_tool_rew
    )
    # stage 2: lift up reward
    left_hand_up_rew = torch.zeros_like(goal_object_dist)
    left_hand_up_rew = torch.where(is_grasp_left == True, 1 * (left_palm_pos[:, 2] - goal_height), left_hand_up_rew)
    right_hand_up_rew = torch.zeros_like(gool_tool_dist)
    right_hand_up_rew = torch.where(is_grasp_right == True, 1 * (right_palm_pos[:, 2] - goal_height), right_hand_up_rew)

    # stage 3: lift near goal bonus
    left_bonus = torch.zeros_like(goal_object_dist)
    left_bonus = torch.where(
        is_grasp_left == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), left_bonus
        ),
        left_bonus,
    )
    right_bonus = torch.zeros_like(gool_tool_dist)
    right_bonus = torch.where(
        is_grasp_right == True,
        torch.where(
            gool_tool_dist <= success_tolerance, 1.0 / (0.5 + gool_tool_dist), right_bonus
        ),
        right_bonus,
    )

    left_approach_penalty = dist_reward_scale * left_fingertips_object_dist + 2 * dist_reward_scale * left_palm_object_dist
    right_approach_penalty = dist_reward_scale * right_fingers_tool_dist + 2 * dist_reward_scale * right_palm_object_dist
    left_after_grasp_reward = lift_object_rew + left_hand_up_rew + left_bonus
    right_after_grasp_reward = lift_tool_rew + right_hand_up_rew + right_bonus
    object_offset_penalty = 0.3 * object_offset
    tool_offset_penalty = 0.3 * tool_offset
    
    # 
```

```python
def compute_reward(self):
        (
            self.rew_buf[:],
            self.reset_buf[:],
            self.progress_buf[:],
            self.successes[:],
            self.current_successes[:],
            self.consecutive_successes[:],
            reward_info,
        ) = compute_task_rewards(
            self.reset_buf,
            self.progress_buf,
            self.successes,
            self.current_successes,
            self.consecutive_successes,
            self.max_episode_length,
            self.object_pos, self.tool_pos,
            self.goal_height,
            self.left_palm_center_pos, self.right_palm_center_pos,
            self.left_fingertip_center_pos, self.right_fingertip_center_pos,
            self.dist_reward_scale,
            self.object_init_states, self.tool_init_states,
            self.action_penalty_scale,
            self.success_tolerance,
            self.av_factor,
            self.table_start_pose.p.z*2,
        )

        self.extras.update(reward_info)
        self.extras["successes"] = self.successes
        self.extras["current_successes"] = self.current_successes
        self.extras["consecutive_successes"] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term policy performance.
            print(
                "Direct average consecutive successes = {:.1f}".format(
                    direct_average_successes / (self.total_resets + self.num_envs)
                )
            )
            if self.total_resets > 0:
                print(
                    "Post-Reset average consecutive successes = {:.1f}".format(
                        self.total_successes / self.total_resets
                    )
                )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.left_palm_center_pos = self.left_palm_pos#  + quat_apply(self.left_palm_rot, to_torch(self.palm_offset).repeat(self.num_envs, 1))
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]
        self.right_palm_center_pos = self.right_palm_pos#  + quat_apply(self.right_palm_rot, to_torch(self.palm_offset).repeat(self.num_envs, 1))

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.left_fingertip_state[..., :3]
        self.left_fingertip_rot = self.left_fingertip_state[..., 3:7]
        self.left_fingertip_center_pos = self.left_fingertip_pos
        # self.left_fingertip_center_pos = torch.zeros_like(self.left_fingertip_pos)
        # for i in range(len(self.fingertips)):
        #     if i == 0:
        #         self.left_fingertip_center_pos[:, i, :] = self.left_fingertip_pos[:, i, :] + quat_apply(self.left_fingertip_rot[:, i, :],to_torch(self.thumb_offset).repeat(self.num_envs, 1),)
        #     else:
        #         self.left_fingertip_center_pos[:, i, :] = self.left_fingertip_pos[:, i, :] + quat_apply(self.left_fingertip_rot[:, i, :],to_torch(self.fingertip_offset).repeat(self.num_envs, 1),)

        self.right_fingertip_state = self.rigid_body_states[:, self.right_fingertip_handles][..., :13]
        self.right_fingertip_pose = self.right_fingertip_state[..., :7]
        self.right_fingertip_pos = self.right_fingertip_state[..., :3]
        self.right_fingertip_rot = self.right_fingertip_state[..., 3:7]
        self.right_fingertip_center_pos = self.right_fingertip_pos
        # self.right_fingertip_center_pos = torch.zeros_like(self.right_fingertip_pos)
        # for i in range(len(self.fingertips)):
        #     if i == 0:
        #         self.right_fingertip_center_pos[:, i, :] = self.right_fingertip_pos[:, i, :] + quat_apply(self.right_fingertip_rot[:, i, :],to_torch(self.thumb_offset).repeat(self.num_envs, 1),)
        #     else:
        #         self.right_fingertip_center_pos[:, i, :] = self.right_fingertip_pos[:, i, :] + quat_apply(self.right_fingertip_rot[:, i, :],to_torch(self.fingertip_offset).repeat(self.num_envs, 1),)

        if self.obs_type == "full_no_vel":
            self.compute_full_observations()
        elif self.obs_type == "full":
            self.compute_full_
```

```python
def compute_full_observations(self, no_vel=False):
        # dof state, pos vel 44 * 2 
        cnt = 0
        self.obs_buf[:, cnt : cnt + self.num_robot_dofs] = unscale(
            self.robot_dof_pos,
            self.robot_dof_lower_limits,
            self.robot_dof_upper_limits,
        )
        self.obs_buf[:, self.num_robot_dofs : 2 * self.num_robot_dofs] = self.vel_obs_scale * self.robot_dof_vel

        # fingertip state, 13 * 4 * 2 
        cnt += 2 * self.num_robot_dofs
        num_ft_states = len(self.fingertips) * 13
 
```

### rl_policy/tasks/bi_leap_hand_grasp_v1.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(quat, pos, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_grasp_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, tool_pos, goal_height, left_palm_pos, right_palm_pos, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, object_init_states, tool_init_states, action_penalty_scale, success_tolerance, av_factor, table_height, actions)
def compute_bvdex_stage1_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff, object_hand_joint_rot_diff)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_pose_diff, ref_init_object_left_fingers_pose_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_pose_diff, ref_init_tool_right_fingers_pose_diff, is_stage1_hand_object_rew, is_stage1_lin_rew, is_stage2_pos_rew_exp)
class BiLeapHandGraspV1(VecTask)
    """For visualization purpose"""
    def get_obs_idx_num(self)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_urdf(self, tool_id, target_id, save_path)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, max_shape)
    def _prepare_dataset(self)
    def _prepare_task(self, task_id, trans)
    def _prepare_object_tool_pair(self, asset_root, vhacd_enabled)
    def _prepare_table_asset(self)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)
    def visualize(self, replay_times, debug, vis_metrics)

```python
def compute_grasp_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos, tool_pos,
    goal_height: float,
    left_palm_pos, right_palm_pos,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    object_init_states, tool_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    goal_tool_dist = torch.abs(goal_height - tool_pos[:, 2])
    left_palm_object_dist = torch.norm(object_pos - left_palm_pos, dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pos, dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)
    object_offset = torch.norm(object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1)
    tool_offset = torch.norm(tool_pos[:, 0:2] - tool_init_states[:, 0:2], dim=-1)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(goal_tool_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    lift_object_rew = torch.zeros_like(goal_object_dist)
    lift_object_rew = torch.where(
        is_grasp_left, 3 * (goal_height - table_height) - 2 * goal_object_dist, lift_object_rew
    )
    lift_tool_rew = torch.zeros_like(goal_tool_dist)
    lift_tool_rew = torch.where(
        is_grasp_right, 3 * (goal_height - table_height) - 2 * goal_tool_dist, lift_tool_rew
    )
    # stage 2: lift up reward
    left_hand_up_rew = torch.zeros_like(goal_object_dist)
    left_hand_up_rew = torch.where(is_grasp_left, 1 * (left_palm_pos[:, 2] - goal_height), left_hand_up_rew)
    right_hand_up_rew = torch.zeros_like(goal_tool_dist)
    right_hand_up_rew = torch.where(is_grasp_right, 1 * (right_palm_pos[:, 2] - goal_height), right_hand_up_rew)

    # stage 3: lift near goal bonus
    left_bonus = torch.zeros_like(goal_object_dist)
    left_bonus = torch.where(
        is_grasp_left,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), left_bonus
        ),
        left_bonus,
    )
    right_bonus = torch.zeros_like(goal_tool_dist)
    right_bonus = torch.where(
        is_grasp_right,
        torch.where(
            goal_tool_dist <= success_tolerance, 1.0 / (0.5 + goal_tool_dist), right_bonus
        ),
        right_bonus,
    )

    left_approach_penalty = dist_reward_scale * left_fingertips_object_dist + 2 * dist_reward_scale * left_palm_object_dist
    right_approach_penalty = dist_reward_scale * right_fingers_tool_dist + 2 * dist_reward_scale * right_palm_object_dist
    left_after_grasp_reward = lift_object_rew + left_hand_up_rew + left_bonus
    right_after_grasp_reward = lift_tool_rew + right_hand_up_rew + right_bonus
    object_offset_penalty = 0.3 * object_offset
    tool_offset_penalty = 0.3 * tool_offset

    # total reward
    left_reward = - left_
```

```python
def compute_bvdex_stage1_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff,
    ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff,
    object_hand_joint_rot_diff: int,
):
    object_pos = object_pose[:, :3]
    tool_pos = tool_pose[:, :3]
    info = {}

    left_palm_object_dist = torch.norm(object_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pose[:, :3], dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(right_palm_object_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pos, dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7].repeat(len(object_pose),1), object_pose[:, 3:7]) # [-1,1]
    left_lift_object_pos_rew, left_lift_object_rot_rew = torch.zeros_like(ref_object_pos_dist), torch.zeros_like(ref_object_rot_rew)
    left_lift_object_pos_rew = torch.where(is_grasp_left, 1 - ref_object_pos_dist / ref_init_object_pos_dist, left_lift_object_pos_rew)
    left_lift_object_rot_rew = torch.where(is_grasp_left, ref_object_rot_rew, left_lift_object_rot_rew)

    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pos, dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7].repeat(len(tool_pose),1), tool_pose[:, 3:7])  # [-1,1]
    right_lift_tool_pos_rew, right_lift_tool_rot_rew = torch.zeros_like(ref_tool_pos_dist), torch.zeros_like(ref_tool_rot_rew)
    right_lift_tool_pos_rew = torch.where(is_grasp_right, 1 - ref_tool_pos_dist / ref_init_tool_pos_dist, right_lift_tool_pos_rew)
    right_lift_tool_rot_rew = torch.where(is_grasp_right, ref_tool_rot_rew, right_lift_tool_rot_rew)

    # stage 2: hand-object joint rotation, no grasp condition
    if object_hand_joint_rot_diff:
        object_hand_rot_diff = quat_diff_theta(object_pose[:, 3:7], left_palm_pose[:, 3:7])
        left_object_hand_rot_rew = - torch.abs((ref_init_object_hand_rot_diff - object_hand_rot_diff))  # [0, -2pi]
        left_object_hand_rot_rew = 0.5 + left_object_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
        tool_hand_rot_diff = quat_diff_theta(tool_pose[:, 3:7], right_palm_pose[:, 3:7])
        right_tool_hand_rot_rew = - torch.abs((ref_init_tool_hand_rot_diff - tool_hand_rot_diff))  # [0, -2pi]
        right_tool_hand_rot_rew = 0.5 + right_tool_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
    else:
        left_object_hand_rot_rew = torch.zeros_like(ref_object_pos_dist)

```

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist, ref_init_object_
```

### rl_policy/tasks/bi_leap_hand_grasp_v2.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def pos_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_grasp_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, tool_pos, goal_height, left_palm_pos, right_palm_pos, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, object_init_states, tool_init_states, action_penalty_scale, success_tolerance, av_factor, table_height, actions)
def compute_bvdex_stage1_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff, object_hand_joint_rot_diff)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff, is_stage1_hand_object_rew, is_stage1_lin_rew, is_stage2_pos_rew_exp)
class BiLeapHandGraspV2(VecTask)
    """Single-object training for bimanual manipulation from demonstrations."""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_urdf(self, tool_id, target_id, save_path)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_dataset(self)
    def _prepare_task(self, task_id)
    def _prepare_object_tool_pair(self, asset_root, vhacd_enabled)
    def _prepare_table_asset(self)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_grasp_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos, tool_pos,
    goal_height: float,
    left_palm_pos, right_palm_pos,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    object_init_states, tool_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    goal_tool_dist = torch.abs(goal_height - tool_pos[:, 2])
    left_palm_object_dist = torch.norm(object_pos - left_palm_pos, dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pos, dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)
    object_offset = torch.norm(object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1)
    tool_offset = torch.norm(tool_pos[:, 0:2] - tool_init_states[:, 0:2], dim=-1)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(goal_tool_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    lift_object_rew = torch.zeros_like(goal_object_dist)
    lift_object_rew = torch.where(
        is_grasp_left == True, 3 * (goal_height - table_height) - 2 * goal_object_dist, lift_object_rew
    )
    lift_tool_rew = torch.zeros_like(goal_tool_dist)
    lift_tool_rew = torch.where(
        is_grasp_right == True, 3 * (goal_height - table_height) - 2 * goal_tool_dist, lift_tool_rew
    )
    # stage 2: lift up reward
    left_hand_up_rew = torch.zeros_like(goal_object_dist)
    left_hand_up_rew = torch.where(is_grasp_left == True, 1 * (left_palm_pos[:, 2] - goal_height), left_hand_up_rew)
    right_hand_up_rew = torch.zeros_like(goal_tool_dist)
    right_hand_up_rew = torch.where(is_grasp_right == True, 1 * (right_palm_pos[:, 2] - goal_height), right_hand_up_rew)

    # stage 3: lift near goal bonus
    left_bonus = torch.zeros_like(goal_object_dist)
    left_bonus = torch.where(
        is_grasp_left == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), left_bonus
        ),
        left_bonus,
    )
    right_bonus = torch.zeros_like(goal_tool_dist)
    right_bonus = torch.where(
        is_grasp_right == True,
        torch.where(
            goal_tool_dist <= success_tolerance, 1.0 / (0.5 + goal_tool_dist), right_bonus
        ),
        right_bonus,
    )

    left_approach_penalty = dist_reward_scale * left_fingertips_object_dist + 2 * dist_reward_scale * left_palm_object_dist
    right_approach_penalty = dist_reward_scale * right_fingers_tool_dist + 2 * dist_reward_scale * right_palm_object_dist
    left_after_grasp_reward = lift_object_rew + left_hand_up_rew + left_bonus
    right_after_grasp_reward = lift_tool_rew + right_hand_up_rew + right_bonus
    object_offset_penalty = 0.3 * object_offset
    tool_offset_penalty = 0.3 * tool_offs
```

```python
def compute_bvdex_stage1_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff,
    ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff,
    object_hand_joint_rot_diff: int,
):
    object_pos = object_pose[:, :3]
    tool_pos = tool_pose[:, :3]
    info = {}

    left_palm_object_dist = torch.norm(object_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pose[:, :3], dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(right_palm_object_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pos, dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7].repeat(len(object_pose),1), object_pose[:, 3:7]) # [-1,1]
    left_lift_object_pos_rew, left_lift_object_rot_rew = torch.zeros_like(ref_object_pos_dist), torch.zeros_like(ref_object_rot_rew)
    left_lift_object_pos_rew = torch.where(is_grasp_left == True, 1 - ref_object_pos_dist / ref_init_object_pos_dist, left_lift_object_pos_rew)
    left_lift_object_rot_rew = torch.where(is_grasp_left == True, ref_object_rot_rew, left_lift_object_rot_rew)

    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pos, dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7].repeat(len(tool_pose),1), tool_pose[:, 3:7])  # [-1,1]
    right_lift_tool_pos_rew, right_lift_tool_rot_rew = torch.zeros_like(ref_tool_pos_dist), torch.zeros_like(ref_tool_rot_rew)
    right_lift_tool_pos_rew = torch.where(is_grasp_right == True, 1 - ref_tool_pos_dist / ref_init_tool_pos_dist, right_lift_tool_pos_rew)
    right_lift_tool_rot_rew = torch.where(is_grasp_right == True, ref_tool_rot_rew, right_lift_tool_rot_rew)

    # stage 2: hand-object joint rotation, no grasp condition
    if object_hand_joint_rot_diff:
        object_hand_rot_diff = quat_diff_theta(object_pose[:, 3:7], left_palm_pose[:, 3:7])
        left_object_hand_rot_rew = - torch.abs((ref_init_object_hand_rot_diff - object_hand_rot_diff))  # [0, -2pi]
        left_object_hand_rot_rew = 0.5 + left_object_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
        tool_hand_rot_diff = quat_diff_theta(tool_pose[:, 3:7], right_palm_pose[:, 3:7])
        right_tool_hand_rot_rew = - torch.abs((ref_init_tool_hand_rot_diff - tool_hand_rot_diff))  # [0, -2pi]
        right_tool_hand_rot_rew = 0.5 + right_tool_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
    else:
        left_object_hand_rot_rew = torch.
```

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    times
```

### rl_policy/tasks/bi_leap_hand_grasp_v3.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def pos_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, actions, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, is_expect_end)
class BiLeapHandGraspV3(VecTask)
    """Multi-object training for bimanual manipulation from demonstrations."""
    def get_obs_idx_num(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights,
    actions,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_pose[:, :3] - left_palm_pose[:, :3], dim=-1) 
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_pose[:, :3] - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5, right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_pose[:, :3], dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_pose[:, :3], dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0, right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch.logical_and(ref_object_pos_dist <= success_tolerance, left_fingertips_object_dist + left_palm_object_dist < 0.12 * (num_fingers + 1)).float()
    right_successes = torch.logical_and(ref_tool_pos_dist <= success_tolerance, right_fingertips_tool_dist + right_palm_tool_dist < 0.12 * (num_fingers + 1)).float()
    left_reach_ref_
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights,
                self.actions,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.left_fingertip_state[..., :3]
        self.left_fingertip_rot = self.left_fingertip_state[..., 3:7]

        self.right_fingertip_state = self.rigid_body_states[:, self.right_fingertip_handles]
```

### rl_policy/tasks/bi_leap_hand_grasp_v4.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def pos_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, actions, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, is_expect_end)
class BiLeapHandGraspV4(VecTask)
    """Multi-object training with object label for bimanual manipulation from demonstrations."""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights,
    actions,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    left_palm_object_dist = torch.norm(object_pose[:, :3] - left_palm_pose[:, :3], dim=-1) 
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_pose[:, :3] - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_pose[:, :3], dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_pose[:, :3], dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch.logical_and(ref_object_pos_dist <= success_tolerance, left_fingertips_object_dist + left_palm_object_dist < 0.12 * (num_fingers + 1)).float()
    right_s
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights,
                self.actions,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.left_fingertip_state[..., :3]
        self.left_fingertip_rot = self.left_fingertip_state[..., 3:7]

        self.right_fingertip_state = self.rigid_body_states[:, self.right_fingertip_handles][..., :13]
        self.right_
```

### rl_policy/tasks/bi_leap_hand_grasp_v5.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def pos_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, actions, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
class BiLeapHandGraspV5(VecTask)
    """Multi-object training with object label for bimanual manipulation from demonstrations. Stage 1 apporach reward modify to approach grasp point"""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def _prepare_side_panel_asset(self)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights,
    actions,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    object_grasp_pos, tool_grasp_pos,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    # approach penalty
    left_palm_object_dist = torch.norm(object_grasp_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_grasp_pos - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_grasp_pos, dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_grasp_pos, dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes = torch.logical_and(ref_object_pos_dist <= success_tolerance, left_fingertips_object_dist + left_palm_object_
```

```python
def compute_reward(self, mode):
        if mode == 's12':
            t = torch.where(self.reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tl = torch.where(self.left_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.left_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            tr = torch.where(self.right_reach_ref_timestep == -1, torch.zeros_like(self.timestep), torch.ceil((self.timestep - self.right_reach_ref_timestep) / self.frequency).int()) + self.dataset_ref_timesteps[self.all_task_idx]
            ref_object_pose = self.dataset_object_poses[self.all_task_idx,tl.clip(max=self.dataset_end_timesteps[self.all_task_idx])] 
            ref_tool_pose = self.dataset_tool_poses[self.all_task_idx,tr.clip(max=self.dataset_end_timesteps[self.all_task_idx])]
            is_expect_end = (self.dataset_end_timesteps[self.all_task_idx] == t.clip(max=self.dataset_end_timesteps[self.all_task_idx]))
            (
                self.rew_buf[:],
                self.reset_buf[:],
                self.progress_buf[:],
                self.stage1_left_successes[:], self.stage1_right_successes[:], self.stage1_successes[:],
                self.stage2_left_successes[:], self.stage2_right_successes[:], self.stage2_successes[:],
                self.timestep[:], self.reach_ref_timestep[:], self.left_reach_ref_timestep[:], self.right_reach_ref_timestep[:],
                reward_info
            ) = compute_bvdex_stage12_rewards(
                self.reset_buf,
                self.progress_buf,
                self.stage1_left_successes, self.stage1_right_successes, self.stage1_successes,
                self.stage2_left_successes, self.stage2_right_successes, self.stage2_successes,
                self.max_episode_length,
                self.object_pose, self.tool_pose,
                self.left_palm_pose, self.right_palm_pose,
                self.left_fingertip_pose, self.right_fingertip_pose,
                self.dist_reward_scale,
                self.action_penalty_scale,
                self.success_tolerance,
                self.av_factor,
                self.table_heights,
                self.actions,
                self.timestep, self.reach_ref_timestep, self.left_reach_ref_timestep, self.right_reach_ref_timestep,
                ref_object_pose, self.ref_init_object_pos_dist, #self.ref_ref_object_palm_pose_diff, self.ref_ref_object_left_fingers_pos_diff,
                ref_tool_pose, self.ref_init_tool_pos_dist,     #self.ref_ref_tool_palm_pose_diff, self.ref_ref_tool_right_fingers_pos_diff,
                self.actual_object_grasp_pos, self.actual_tool_grasp_pos,
                is_expect_end, # self.is_stage1_hand_object_rew, self.is_stage1_lin_rew, self.is_stage2_pos_rew_exp,
            )

        self.extras.update(reward_info)
        self.extras["stage1_left_successes"] = self.stage1_left_successes
        self.extras["stage1_right_successes"] = self.stage1_right_successes
        self.extras["stage1_successes"] = self.stage1_successes
        self.extras["stage2_left_successes"] = self.stage2_left_successes
        self.extras["stage2_right_successes"] = self.stage2_right_successes
        self.extras["stage2_successes"] = self.stage2_successes

        return reward_info
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        # get refreshed objects
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]
        self.tool_pose = self.root_state_tensor[self.tool_indices, 0:7]
        self.tool_pos = self.root_state_tensor[self.tool_indices, 0:3]
        self.tool_rot = self.root_state_tensor[self.tool_indices, 3:7]
        self.tool_linvel = self.root_state_tensor[self.tool_indices, 7:10]
        self.tool_angvel = self.root_state_tensor[self.tool_indices, 10:13]


        self.left_palm_state = self.rigid_body_states[:, self.left_palm_handle][..., :13]
        self.left_palm_pose = self.left_palm_state[..., :7]
        self.left_palm_pos = self.left_palm_state[..., :3]
        self.left_palm_rot = self.left_palm_state[..., 3:7]
        self.right_palm_state = self.rigid_body_states[:, self.right_palm_handle][..., :13]
        self.right_palm_pose = self.right_palm_state[..., :7]
        self.right_palm_pos = self.right_palm_state[..., :3]
        self.right_palm_rot = self.right_palm_state[..., 3:7]

        self.left_fingertip_state = self.rigid_body_states[:, self.left_fingertip_handles][..., :13]
        self.left_fingertip_pose = self.left_fingertip_state[..., :7]
        self.left_fingertip_pos = self.
```

### rl_policy/tasks/bi_leap_hand_grasp_v6.py

```
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def pos_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(pos, quat, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
def compute_ab_stage1_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
def compute_ab_functional_grasping_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
def compute_ab_bonus_rewards(reset_buf, progress_buf, stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes, stage2_left_successes, stage2_right_successes, stage2_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_heights, left_robot_link1_pos, right_robot_link1_pos, frequency, timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_tool_pose, ref_init_tool_pos_dist, object_grasp_pos, tool_grasp_pos, is_expect_end)
class BiLeapHandGraspV6(VecTask)
    """Multi-object training with object label for bimanual manipulation from demonstrations. Stage 1 apporach reward modify to approach grasp point and resets when dataset terminates.
initial setting modifies."""
    def get_obs_idx_dict(self, obs_type)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled, obj_asset_storage, max_shape)
    def _prepare_dataset(self, vhacd_enabled)
    def _initialize_task(self, taco_task_data)
    def _prepare_table_asset(self, table_dims)
    def _prepare_side_panel_asset(self)
    def compute_reward(self)
    def compute_observations(self)
    def compute_full_observations(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights, left_robot_link1_pos, right_robot_link1_pos,
    frequency: float,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    object_grasp_pos, tool_grasp_pos,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    '''
    stage 1: reach a static ref object pose (linear reward)
    stage 2: stage 1 finished, follow a dynamic ref object pose (exponential reward)   
    '''
    info = {}

    # approach penalty
    left_palm_object_dist = torch.norm(object_grasp_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_grasp_pos - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_grasp_pos, dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_grasp_pos, dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7], object_pose[:, 3:7]) # [-1,1]
    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pose[:, :3], dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7], tool_pose[:, 3:7])  # [-1,1]

    '''lift object reward for stage 1'''
    left_lift_object_pos_rew1 = (1 - ref_object_pos_dist / ref_init_object_pos_dist).clip(min=0)  # [-1, 1]
    left_lift_object_rot_rew1 = ref_object_rot_rew
    right_lift_tool_pos_rew1 = (1 - ref_tool_pos_dist / ref_init_tool_pos_dist).clip(min=0)  # [-1, 1]
    right_lift_tool_rot_rew1 = ref_tool_rot_rew
    '''lift object reward for stage 2: trajectory following'''
    # trajectory following
    left_successes 
```

```python
def compute_ab_stage1_rewards(
    reset_buf,
    progress_buf,
    stage1_left_successes, stage1_right_successes, stage1_successes, stage1_cul_left_successes, stage1_cul_right_successes,
    stage2_left_successes, stage2_right_successes, stage2_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pose, right_fingertip_pose,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_heights, left_robot_link1_pos, right_robot_link1_pos,
    frequency: float,
    timestep, reach_ref_timestep, left_reach_ref_timestep, right_reach_ref_timestep,
    ref_object_pose, ref_init_object_pos_dist,  #ref_ref_object_palm_pose_diff, ref_ref_object_left_fingers_pos_diff,
    ref_tool_pose, ref_init_tool_pos_dist,      #ref_ref_tool_palm_pose_diff, ref_ref_tool_right_fingers_pos_diff,
    object_grasp_pos, tool_grasp_pos,
    is_expect_end, # is_stage1_hand_object_rew: int, is_stage1_lin_rew:int, is_stage2_pos_rew_exp: int,
):
    info = {}

    # approach penalty
    left_palm_object_dist = torch.norm(object_pose[:, :3] - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5 * torch.ones_like(left_palm_object_dist), left_palm_object_dist)
    right_palm_tool_dist = torch.norm(tool_pose[:, :3] - right_palm_pose[:, :3], dim=-1)  
    right_palm_tool_dist = torch.where(right_palm_tool_dist >= 0.5, 0.5 * torch.ones_like(right_palm_tool_dist), right_palm_tool_dist)

    num_fingers = left_fingertip_pose.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(left_fingertip_pose[:, i, :3] - object_pose[:, :3], dim=-1)
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0 * torch.ones_like(left_fingertips_object_dist), left_fingertips_object_dist
    )  # Important!

    right_fingertips_tool_dist = torch.zeros_like(right_palm_tool_dist)
    for i in range(num_fingers):
        right_fingertips_tool_dist += torch.norm(right_fingertip_pose[:, i, :3] - tool_pose[:, :3], dim=-1)
    right_fingertips_tool_dist = torch.where(
        right_fingertips_tool_dist >= 3.0, 3.0 * torch.ones_like(right_fingertips_tool_dist), right_fingertips_tool_dist
    )  # Important!
    info["left_palm_object_dist"] = left_palm_object_dist
    info["right_palm_tool_dist"] = right_palm_tool_dist
    info["left_fingertips_object_dist"] = left_fingertips_object_dist
    info["right_fingertips_tool_dist"] = right_fingertips_tool_dist

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingertips_tool_dist <= 0.12 * num_fingers) + (right_palm_tool_dist <= 0.12)).float()
    info["left_is_grasp"] = is_grasp_left
    info["right_is_grasp"] = is_grasp_right

    # after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pose[:, :3], dim=-1)
    ref_object_rot_rew = quat_rew
```

### rl_policy/tasks/bi_leap_hand_grasp_vision.py

```
def mov(tensor, device)
def depth_image_to_point_cloud_GPU_batch(camera_depth_tensor_batch, camera_rgb_tensor_batch, camera_seg_tensor_batch, camera_view_matrix_inv_batch, camera_proj_matrix_batch, u, v, width, height, depth_bar, device)
def sample_points(points, sample_num, sample_method, device)
def standardize_quaternion(quaternions)
def orientation_error(desired, current)
def quat_diff_theta(desired, current)
def quat_rew(desired, current)
def rotmat_dist(desired, current)
def rotmat_rew(desired, current)
def rotation_6d_to_matrix(d6)
def rotation_matrix_z(angles)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def transformation_multiply(quat1, pos1, quat2, pos2)
def transformation_inverse(quat, pos)
def transformation_apply(quat, pos, vec)
def compute_relative_pose(a_position, a_orientation, b_position, b_orientation)
def compute_relative_position(a_position, b_orientation, b_position)
def compute_grasp_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, tool_pos, goal_height, left_palm_pos, right_palm_pos, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, object_init_states, tool_init_states, action_penalty_scale, success_tolerance, av_factor, table_height, actions)
def compute_bvdex_stage1_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pos, right_fingertip_pos, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff, object_hand_joint_rot_diff)
def compute_bvdex_stage12_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pose, tool_pose, left_palm_pose, right_palm_pose, left_fingertip_pose, right_fingertip_pose, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor, table_height, actions, timestep, left_reach_ref_timestep, right_reach_ref_timestep, ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_pose_diff, ref_init_object_left_fingers_pose_diff, ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_pose_diff, ref_init_tool_right_fingers_pose_diff, is_stage1_hand_object_rew, is_stage1_lin_rew, is_stage2_pos_rew_exp)
class BiLeapHandGraspVision(VecTask)
    def get_obs_idx_num(self)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _generate_urdf(self, object_dict)
    def _create_urdf(self, tool_id, target_id, save_path)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_object_asset(self, asset_root, asset_file, vhacd_enabled)
    def _prepare_dataset(self)
    def _prepare_task(self, task_id, trans)
    def _prepare_object_tool_pair(self, asset_root, vhacd_enabled)
    def _prepare_table_asset(self)
    def _prepare_side_panel_asset(self)
    def _cfg_camera_props(self)
    def _cfg_camera_pose(self, table_x, table_y, table_z)
    def _load_cameras(self, env_ptr, env_id, camera_props, camera_eye_list, camera_lookat_list)
    def compute_reward(self, mode)
    def compute_observations(self)
    def compute_full_observations(self)
    def _collect_pointclouds(self)
    def calculate_ik(self, target_left_pose, target_right_pose)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose, j_eef)
    def visualize(self, replay_times, debug, vis_metrics, vis_mode, append_data)

```python
def compute_grasp_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos, tool_pos,
    goal_height: float,
    left_palm_pos, right_palm_pos,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    object_init_states, tool_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    goal_tool_dist = torch.abs(goal_height - tool_pos[:, 2])
    left_palm_object_dist = torch.norm(object_pos - left_palm_pos, dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pos, dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)
    object_offset = torch.norm(object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1)
    tool_offset = torch.norm(tool_pos[:, 0:2] - tool_init_states[:, 0:2], dim=-1)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(goal_tool_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    lift_object_rew = torch.zeros_like(goal_object_dist)
    lift_object_rew = torch.where(
        is_grasp_left == True, 3 * (goal_height - table_height) - 2 * goal_object_dist, lift_object_rew
    )
    lift_tool_rew = torch.zeros_like(goal_tool_dist)
    lift_tool_rew = torch.where(
        is_grasp_right == True, 3 * (goal_height - table_height) - 2 * goal_tool_dist, lift_tool_rew
    )
    # stage 2: lift up reward
    left_hand_up_rew = torch.zeros_like(goal_object_dist)
    left_hand_up_rew = torch.where(is_grasp_left == True, 1 * (left_palm_pos[:, 2] - goal_height), left_hand_up_rew)
    right_hand_up_rew = torch.zeros_like(goal_tool_dist)
    right_hand_up_rew = torch.where(is_grasp_right == True, 1 * (right_palm_pos[:, 2] - goal_height), right_hand_up_rew)

    # stage 3: lift near goal bonus
    left_bonus = torch.zeros_like(goal_object_dist)
    left_bonus = torch.where(
        is_grasp_left == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), left_bonus
        ),
        left_bonus,
    )
    right_bonus = torch.zeros_like(goal_tool_dist)
    right_bonus = torch.where(
        is_grasp_right == True,
        torch.where(
            goal_tool_dist <= success_tolerance, 1.0 / (0.5 + goal_tool_dist), right_bonus
        ),
        right_bonus,
    )

    left_approach_penalty = dist_reward_scale * left_fingertips_object_dist + 2 * dist_reward_scale * left_palm_object_dist
    right_approach_penalty = dist_reward_scale * right_fingers_tool_dist + 2 * dist_reward_scale * right_palm_object_dist
    left_after_grasp_reward = lift_object_rew + left_hand_up_rew + left_bonus
    right_after_grasp_reward = lift_tool_rew + right_hand_up_rew + right_bonus
    object_offset_penalty = 0.3 * object_offset
    tool_offset_penalty = 0.3 * tool_offs
```

```python
def compute_bvdex_stage1_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pose, tool_pose,
    left_palm_pose, right_palm_pose,
    left_fingertip_pos, right_fingertip_pos,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    table_height: float,
    actions,
    ref_object_pose, ref_init_object_pos_dist, ref_init_object_hand_rot_diff,
    ref_tool_pose, ref_init_tool_pos_dist, ref_init_tool_hand_rot_diff,
    object_hand_joint_rot_diff: int,
):
    object_pos = object_pose[:, :3]
    tool_pos = tool_pose[:, :3]
    info = {}

    left_palm_object_dist = torch.norm(object_pos - left_palm_pose[:, :3], dim=-1)
    left_palm_object_dist = torch.where(left_palm_object_dist >= 0.5, 0.5, left_palm_object_dist)
    right_palm_object_dist = torch.norm(tool_pos - right_palm_pose[:, :3], dim=-1)
    right_palm_object_dist = torch.where(right_palm_object_dist >= 0.5, 0.5, right_palm_object_dist)

    num_fingers = left_fingertip_pos.shape[1]
    left_fingertips_object_dist = torch.zeros_like(left_palm_object_dist)
    for i in range(num_fingers):
        left_fingertips_object_dist += torch.norm(
            left_fingertip_pos[:, i, :] - object_pos, dim=-1
        )
    left_fingertips_object_dist = torch.where(
        left_fingertips_object_dist >= 3.0, 3.0, left_fingertips_object_dist
    )

    right_fingers_tool_dist = torch.zeros_like(right_palm_object_dist)
    for i in range(num_fingers):
        right_fingers_tool_dist += torch.norm(
            right_fingertip_pos[:, i, :] - tool_pos, dim=-1
        )
    right_fingers_tool_dist = torch.where(
        right_fingers_tool_dist >= 3.0, 3.0, right_fingers_tool_dist
    )

    is_grasp_left = ((left_fingertips_object_dist <= 0.12 * num_fingers) + (left_palm_object_dist <= 0.12)).float()
    is_grasp_right = ((right_fingers_tool_dist <= 0.12 * num_fingers) + (right_palm_object_dist <= 0.12)).float()

    # stage 1: after hand approach object, lift_object
    ref_object_pos_dist = torch.norm(ref_object_pose[:, :3] - object_pos, dim=-1)
    ref_object_rot_rew = quat_rew(ref_object_pose[:, 3:7].repeat(len(object_pose),1), object_pose[:, 3:7]) # [-1,1]
    left_lift_object_pos_rew, left_lift_object_rot_rew = torch.zeros_like(ref_object_pos_dist), torch.zeros_like(ref_object_rot_rew)
    left_lift_object_pos_rew = torch.where(is_grasp_left == True, 1 - ref_object_pos_dist / ref_init_object_pos_dist, left_lift_object_pos_rew)
    left_lift_object_rot_rew = torch.where(is_grasp_left == True, ref_object_rot_rew, left_lift_object_rot_rew)

    ref_tool_pos_dist = torch.norm(ref_tool_pose[:, :3] - tool_pos, dim=-1)
    ref_tool_rot_rew = quat_rew(ref_tool_pose[:, 3:7].repeat(len(tool_pose),1), tool_pose[:, 3:7])  # [-1,1]
    right_lift_tool_pos_rew, right_lift_tool_rot_rew = torch.zeros_like(ref_tool_pos_dist), torch.zeros_like(ref_tool_rot_rew)
    right_lift_tool_pos_rew = torch.where(is_grasp_right == True, 1 - ref_tool_pos_dist / ref_init_tool_pos_dist, right_lift_tool_pos_rew)
    right_lift_tool_rot_rew = torch.where(is_grasp_right == True, ref_tool_rot_rew, right_lift_tool_rot_rew)

    # stage 2: hand-object joint rotation, no grasp condition
    if object_hand_joint_rot_diff:
        object_hand_rot_diff = quat_diff_theta(object_pose[:, 3:7], left_palm_pose[:, 3:7])
        left_object_hand_rot_rew = - torch.abs((ref_init_object_hand_rot_diff - object_hand_rot_diff))  # [0, -2pi]
        left_object_hand_rot_rew = 0.5 + left_object_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
        tool_hand_rot_diff = quat_diff_theta(tool_pose[:, 3:7], right_palm_pose[:, 3:7])
        right_tool_hand_rot_rew = - torch.abs((ref_init_tool_hand_rot_diff - tool_hand_rot_diff))  # [0, -2pi]
        right_tool_hand_rot_rew = 0.5 + right_tool_hand_rot_rew * (0.5 / torch.pi)  # [0.5, -0.5]
    else:
        left_object_hand_rot_rew = torch.
```

```python
def compute_bvdex_stage12_rewards(
    reset_buf,
    pro
```

### rl_policy/tasks/leap_hand_grasp.py

```
class LeapHandGrasp(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file)
    def _prepare_object_asset(self, asset_root, asset_file)
    def _prepare_table_asset(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose)
def orientation_error(desired, current)
def rotation_6d_to_matrix(d6)
def standardize_quaternion(quaternions)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def compute_task_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, goal_height, palm_pos, fingertip_pos, actions, dist_reward_scale, action_penalty_scale, success_tolerance, av_factor)

```python
def compute_task_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos,
    goal_height: float,
    palm_pos,
    fingertip_pos,
    actions,
    dist_reward_scale: float,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    palm_object_dist = torch.norm(object_pos - palm_pos, dim=-1)
    palm_object_dist = torch.where(palm_object_dist >= 0.5, 0.5, palm_object_dist)

    fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(fingertip_pos.shape[-2]):
        fingertips_object_dist += torch.norm(
            fingertip_pos[:, i, :] - object_pos, dim=-1
        )

    fingertips_object_dist = torch.where(
        fingertips_object_dist >= 3.0, 3.0, fingertips_object_dist
    )

    flag = (fingertips_object_dist <= 0.07 * 4) + (palm_object_dist <= 0.15)
    # stage 1: approach reward
    hand_approach_reward = torch.zeros_like(goal_object_dist)
    hand_approach_reward = torch.where(
        flag == True, 1 * (0.9 - 2 * goal_object_dist), hand_approach_reward
    )
    # stage 2: lift reward
    object_height = object_pos[:, 2]
    hand_up = torch.zeros_like(goal_object_dist)
    hand_up = torch.where(flag == True, 1 * (object_height - goal_height), hand_up)

    # stage 3: lift to goal bonus
    bonus = torch.zeros_like(goal_object_dist)
    bonus = torch.where(
        flag == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (1 + goal_object_dist), bonus
        ),
        bonus,
    )

    # TODO reward shaping
    reward = (
        -dist_reward_scale * fingertips_object_dist
        - 2 * dist_reward_scale * palm_object_dist
        + hand_approach_reward
        + hand_up
        + bonus
    )

    info["fingertips_object_dist"] = fingertips_object_dist
    info["palm_object_dist"] = palm_object_dist
    info["hand_approach_reward"] = hand_approach_reward
    info["hand_up"] = hand_up
    info["bonus"] = bonus
    info["reward"] = reward

    resets = reset_buf.clone()
    resets = torch.where(
        progress_buf >= max_episode_length, torch.ones_like(resets), resets
    )
    resets = torch.where(object_height <= 0.3, torch.ones_like(resets), resets)
    successes = torch.where(
        goal_object_dist <= success_tolerance,
        torch.where(
            fingertips_object_dist + palm_object_dist < 0.4, torch.ones_like(successes), successes
        ),
        torch.zeros_like(successes),
    )
    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())
    current_successes = torch.where(resets, successes, current_successes)
    cons_successes = torch.where(
        num_resets > 0,
        av_factor * finished_cons_successes / num_resets
        + (1.0 - av_factor) * consecutive_successes,
        consecutive_successes,
    )

    return (
        reward,
        resets,
        progress_buf,
        successes,
        current_successes,
        cons_successes,
        info,
    )
```

```python
def compute_reward(self, actions):
        # TODO fill in the reward computation
        (
            self.rew_buf[:],
            self.reset_buf[:],
            self.progress_buf[:],
            self.successes[:],
            self.current_successes[:],
            self.consecutive_successes[:],
            reward_info,
        ) = compute_task_rewards(
            self.reset_buf,
            self.progress_buf,
            self.successes,
            self.current_successes,
            self.consecutive_successes,
            self.max_episode_length,
            self.object_pos,
            self.goal_height,
            self.palm_center_pos,
            self.fingertip_center_pos,
            self.actions,
            self.dist_reward_scale,
            self.action_penalty_scale,
            self.success_tolerance,
            self.av_factor,
        )

        self.extras.update(reward_info)
        self.extras["successes"] = self.successes
        self.extras["current_successes"] = self.current_successes
        self.extras["consecutive_successes"] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = (
                self.total_successes + (self.successes * self.reset_buf).sum()
            )

            # The direct average shows the overall result more quickly, but slightly undershoots long term policy performance.
            print(
                "Direct average consecutive successes = {:.1f}".format(
                    direct_average_successes / (self.total_resets + self.num_envs)
                )
            )
            if self.total_resets > 0:
                print(
                    "Post-Reset average consecutive successes = {:.1f}".format(
                        self.total_successes / self.total_resets
                    )
                )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.palm_state = self.rigid_body_states[:, self.palm_handle][..., :13]
        self.palm_pos = self.palm_state[..., :3]
        self.palm_rot = self.palm_state[..., 3:7]
        self.palm_center_pos = self.palm_pos + quat_apply(
            self.palm_rot, to_torch(self.palm_offset).repeat(self.num_envs, 1)
        )

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][
            ..., :13
        ]
        self.fingertip_pose = self.fingertip_state[..., :7]
        self.fingertip_pos = self.fingertip_state[..., :3]
        self.fingertip_rot = self.fingertip_state[..., 3:7]
        self.fingertip_center_pos = torch.zeros_like(self.fingertip_pos)
        for i in range(self.num_fingers):
            if i == 0:
                self.fingertip_center_pos[:, i, :] = self.fingertip_pos[
                    :, i, :
                ] + quat_apply(
                    self.fingertip_rot[:, i, :],
                    to_torch(self.thumb_offset).repeat(self.num_envs, 1),
                )
            else:
                self.fingertip_center_pos[:, i, :] = self.fingertip_pos[
                    :, i, :
                ] + quat_apply(
                    self.fingertip_rot[:, i, :],
                    to_torch(self.fingertip_offset).repeat(self.num_envs, 1),
                )

        if self.obs_type == "full_no_vel":
            self.compute_full_observations(no_vel=True)
        elif self.obs_type == "full":
            self.compute_full_observations()
        elif self.obs_type == "full_state":
            self.compute_full_state()
```

```python
def compute_full_observations(self, no_vel=False):
        if no_vel:
            # dof state, pos. 22
            self.obs_buf[:, 0 : self.num_robot_dofs] = unscale(
                self.robot_dof_pos,
                self.robot_dof_lower_limits,
                self.robot_dof_upper_limits,
            )
            # object pose, pos, rot. 7 (22+7=29)
            self.obs_buf[:, self.num_robot_dofs : self.num_robot_dofs + 7] = (
                self.object_pose
            )

            # fingertip observations, 7 * 4 = 28 (29+28=57)
            ft_obs_start = self.num_robot_dofs + 7
            num_ft_states = self.num_fingers * 3
            self.obs_buf[:, ft_obs_start : ft_obs_start + num_ft_states] = (
                self.fingertip_pose.reshape(self.num_envs, num_ft_states)
            )

            # action observations, 22 (57+22=79)
            obs_end = ft_obs_start + num_ft_states
            self.obs_buf[:, obs_end : obs_end + self.num_actions] = self.actions
        else:
            # dof state, pos vel 22 * 2 = 44
            self.obs_buf[:, 0 : self.num_robot_dofs] = unscale(
                self.robot_dof_pos,
                self.robot_dof_lower_limits,
                self.robot_dof_upper_limits,
            )
            self.obs_buf[:, self.num_robot_dofs : 2 * self.num_robot_dofs] = (
                self.vel_obs_scale * self.robot_dof_vel
            )

            # object state, pose, linvel, angvel. 13 (44+13=57)
            obj_obs_start = 2 * self.num_robot_dofs
            self.obs_buf[:, obj_obs_start : obj_obs_start + 7] = self.object_pose
            self.obs_buf[:, obj_obs_start + 7 : obj_obs_start + 10] = self.object_linvel
            self.obs_buf[:, obj_obs_start + 10 : obj_obs_start + 13] = (
                self.object_angvel
            )

            # fingertip state, 13 * 4 = 52 (57+52=109)
            ft_obs_start = obj_obs_start + 13
            num_ft_states = self.num_fingers * 13
            self.obs_buf[:, ft_obs_start : ft_obs_start + num_ft_states] = (
                self.fingertip_state.reshape(self.num_envs, num_ft_states)
            )

            # action observations, 22 (109+22=131)
            obs_end = ft_obs_start + num_ft_states
            self.obs_buf[:, obs_end : obs_end + self.num_actions] = self.actions
```
```

### rl_policy/tasks/shadow_hand_grasp.py

```
class ShadowHandGrasp(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _prepare_robot_asset(self, asset_root, asset_file)
    def _prepare_object_asset(self, asset_root, asset_file)
    def _prepare_table_asset(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _add_debug_lines(self, env, pos, rot, line_len)
    def _control_ik(self, dpose)
    def _add_contact_feat(self, obj_asset_path)
def orientation_error(desired, current)
def rotation_6d_to_matrix(d6)
def standardize_quaternion(quaternions)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def compute_task_rewards(reset_buf, progress_buf, successes, current_successes, consecutive_successes, max_episode_length, object_pos, goal_height, palm_pos, fingertip_pos, contact_point_pos, actions, dist_reward_scale, object_init_states, action_penalty_scale, success_tolerance, av_factor, use_contact_feat)

```python
def compute_task_rewards(
    reset_buf,
    progress_buf,
    successes,
    current_successes,
    consecutive_successes,
    max_episode_length: float,
    object_pos,
    goal_height: float,
    palm_pos,
    fingertip_pos,
    contact_point_pos,
    actions,
    dist_reward_scale: float,
    object_init_states,
    action_penalty_scale: float,
    success_tolerance: float,
    av_factor: float,
    use_contact_feat: bool,
):
    info = {}
    goal_object_dist = torch.abs(goal_height - object_pos[:, 2])
    palm_object_dist = torch.norm(object_pos - palm_pos, dim=-1)
    palm_object_dist = torch.where(palm_object_dist >= 0.5, 0.5, palm_object_dist)
    horizontal_offset = torch.norm(
        object_pos[:, 0:2] - object_init_states[:, 0:2], dim=-1
    )

    fingertips_object_dist = torch.zeros_like(goal_object_dist)
    for i in range(fingertip_pos.shape[-2]):
        fingertips_object_dist += torch.norm(
            fingertip_pos[:, i, :] - object_pos, dim=-1
        )

    fingertips_object_dist = torch.where(
        fingertips_object_dist >= 3.0, 3.0, fingertips_object_dist
    )

    flag = (fingertips_object_dist <= 0.12 * 5) + (palm_object_dist <= 0.12)

    # stage 1: after hand approach object, lift_object
    lift_object = torch.zeros_like(goal_object_dist)
    lift_object = torch.where(
        flag == True, 1 * (0.6 - 2 * goal_object_dist), lift_object
    )
    # stage 2: hand_lift reward
    hand_up = torch.zeros_like(goal_object_dist)
    hand_up = torch.where(flag == True, 1 * (palm_pos[:, 2] - goal_height), hand_up)

    # stage 3: lift to goal bonus
    bonus = torch.zeros_like(goal_object_dist)
    bonus = torch.where(
        flag == True,
        torch.where(
            goal_object_dist <= success_tolerance, 1.0 / (0.5 + goal_object_dist), bonus
        ),
        bonus,
    )

    fingertips_contact_dist = torch.zeros_like(goal_object_dist)
    if use_contact_feat:
        num_contact_point = 0
        for i in range(fingertip_pos.shape[-2]):
            if (contact_point_pos[:, i * 4] == 1).all():
                num_contact_point += 1
                fingertips_contact_dist += torch.norm(
                    fingertip_pos[:, i, :]
                    - contact_point_pos[:, i * 4 + 1 : i * 4 + 4],
                    dim=-1,
                )

        fingertips_contact_dist = torch.where(
            fingertips_object_dist >= 0.2 * num_contact_point,
            0.2 * num_contact_point,
            fingertips_object_dist,
        )

    # TODO reward shaping
    reward = (
        -dist_reward_scale * fingertips_object_dist
        - 2 * dist_reward_scale * palm_object_dist
        + lift_object
        + hand_up
        + bonus
        - 0.3 * horizontal_offset
    )

    if use_contact_feat:
        reward = reward + 1.0 / (0.5 + fingertips_contact_dist)

    info["fingertips_object_dist"] = fingertips_object_dist
    info["fingertips_contact_dist"] = fingertips_contact_dist
    info["palm_object_dist"] = palm_object_dist
    info["lift_object"] = lift_object
    info["hand_up"] = hand_up
    info["horizontal_offset"] = horizontal_offset
    info["bonus"] = bonus
    info["reward"] = reward

    resets = reset_buf.clone()
    resets = torch.where(
        progress_buf >= max_episode_length, torch.ones_like(resets), resets
    )
    resets = torch.where(object_pos[:, 2] <= 0.3, torch.ones_like(resets), resets)
    successes = torch.where(
        goal_object_dist <= success_tolerance,
        torch.where(
            fingertips_object_dist + palm_object_dist < 0.6,
            torch.ones_like(successes),
            successes,
        ),
        torch.zeros_like(successes),
    )
    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())
    current_successes = torch.where(resets, successes, current_successes)
    cons_successes = torch.where(
        num_resets > 0,
        av_factor * finished_cons_successes / num_resets
        + (1.0 - av_factor) * c
```

```python
def compute_reward(self, actions):
        # TODO fill in the reward computation
        (
            self.rew_buf[:],
            self.reset_buf[:],
            self.progress_buf[:],
            self.successes[:],
            self.current_successes[:],
            self.consecutive_successes[:],
            reward_info,
        ) = compute_task_rewards(
            self.reset_buf,
            self.progress_buf,
            self.successes,
            self.current_successes,
            self.consecutive_successes,
            self.max_episode_length,
            self.object_pos,
            self.goal_height,
            self.palm_center_pos,
            self.fingertip_center_pos,
            self.contact_point_pos,
            self.actions,
            self.dist_reward_scale,
            self.object_init_states,
            self.action_penalty_scale,
            self.success_tolerance,
            self.av_factor,
            self.use_contact_feat,
        )

        self.extras.update(reward_info)
        self.extras["successes"] = self.successes
        self.extras["current_successes"] = self.current_successes
        self.extras["consecutive_successes"] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = (
                self.total_successes + (self.successes * self.reset_buf).sum()
            )

            # The direct average shows the overall result more quickly, but slightly undershoots long term policy performance.
            print(
                "Direct average consecutive successes = {:.1f}".format(
                    direct_average_successes / (self.total_resets + self.num_envs)
                )
            )
            if self.total_resets > 0:
                print(
                    "Post-Reset average consecutive successes = {:.1f}".format(
                        self.total_successes / self.total_resets
                    )
                )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.palm_state = self.rigid_body_states[:, self.palm_handle][..., :13]
        self.palm_pos = self.palm_state[..., :3]
        self.palm_rot = self.palm_state[..., 3:7]
        self.palm_center_pos = self.palm_pos + quat_apply(
            self.palm_rot, to_torch(self.palm_offset).repeat(self.num_envs, 1)
        )

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][
            ..., :13
        ]
        self.fingertip_pose = self.fingertip_state[..., :7]
        self.fingertip_pos = self.fingertip_state[..., :3]
        self.fingertip_rot = self.fingertip_state[..., 3:7]
        self.fingertip_center_pos = torch.zeros_like(self.fingertip_pos)
        for i in range(len(self.fingertips)):
            self.fingertip_center_pos[:, i, :] = self.fingertip_pos[
                :, i, :
            ] + quat_apply(
                self.fingertip_rot[:, i, :],
                to_torch(self.fingertip_offset).repeat(self.num_envs, 1),
            )

        self.contact_point_pos = torch.zeros((self.num_envs, 20), device=self.device)
        if self.use_contact_feat:
            for i in range(len(self.fingertips)):
                self.contact_point_pos[:, i * 4] = self.contact_feature_per_env[
                    :, i * 4
                ]
                if self.contact_point_pos[0, i * 4] == 1:
                    self.contact_point_pos[:, i * 4 + 1 : i * 4 + 4] = self.object_pos[
                        :, 0:3
                    ] + quat_apply(
                        self.object_rot,
                        self.contact_feature_per_env[:, i * 4 + 1 : i * 4 + 4],
                    )

        if self.obs_type == "full_no_vel":
            self.compute_full_observations(no_vel=True)
        elif self.obs_type == "full":
            self.compute_full_observations()
        elif self.obs_type == "full_state":
            self.compute_full_state()
```

```python
def compute_full_observations(self, no_vel=False):
        if no_vel:
            # dof state, pos. 29
            self.obs_buf[:, 0 : self.num_robot_dofs] = unscale(
                self.robot_dof_pos,
                self.robot_dof_lower_limits,
                self.robot_dof_upper_limits,
            )
            # object pose, pos, rot. 7 (29+7=36)
            self.obs_buf[:, self.num_robot_dofs : self.num_robot_dofs + 7] = (
                self.object_pose
            )

            # fingertip observations, 7 * 5 = 35 (36+35=71)
            ft_obs_start = self.num_robot_dofs + 7
            num_ft_states = len(self.fingertips) * 7
            self.obs_buf[:, ft_obs_start : ft_obs_start + num_ft_states] = (
                self.fingertip_pose.reshape(self.num_envs, num_ft_states)
            )

            # action observations, 29 (71+29=100)
            obs_end = ft_obs_start + num_ft_states
            self.obs_buf[:, obs_end : obs_end + self.num_actions] = self.actions

            if self.use_contact_feat:
                self.obs_buf[:, obs_end + self.num_actions :] = self.contact_point_pos
        else:
            # dof state, pos vel 29 * 2 = 58
            self.obs_buf[:, 0 : self.num_robot_dofs] = unscale(
                self.robot_dof_pos,
                self.robot_dof_lower_limits,
                self.robot_dof_upper_limits,
            )
            self.obs_buf[:, self.num_robot_dofs : 2 * self.num_robot_dofs] = (
                self.vel_obs_scale * self.robot_dof_vel
            )

            # object state, pose, linvel, angvel. 13 (58+13=71)
            obj_obs_start = 2 * self.num_robot_dofs
            self.obs_buf[:, obj_obs_start : obj_obs_start + 7] = self.object_pose
            self.obs_buf[:, obj_obs_start + 7 : obj_obs_start + 10] = s
```