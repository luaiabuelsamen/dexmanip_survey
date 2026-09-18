# unidexgrasp_pp_2023

source: https://github.com/PKU-EPIC/UniDexGrasp2


commit: 6c9e710b04769bf5d9765e3233820101cb3d718f


## README

<h2 align="center">
  <b>UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning</b>

<div align="center">
    <a href="https://arxiv.org/abs/2304.00464" target="_blank">
    <img src="https://img.shields.io/badge/Paper-arXiv-green" alt="Paper arXiv"></a>
    <a href="https://pku-epic.github.io/UniDexGrasp++/" target="_blank">
    <img src="https://img.shields.io/badge/Page-UniDexGrasp++-blue" alt="Project Page"/></a>
</div>
</h2>

This is the official repository of [**UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning**](https://arxiv.org/abs/2304.00464).

For more information, please visit our [**project page**](https://pku-epic.github.io/UniDexGrasp++/).

## Update
[2023.10.29] Release code and state-based checkpoints and results summary.

## Overview
![](imgs/teaser.jpg)
In this work, we present a novel dexterous grasping policy learning pipeline, **UniDexGrasp++**. Same to UniDexGrasp, UniDexGrasp++ is trained on 3000+ different object instances with
random object poses under a table-top setting. It significantly outperforms the previous
SOTA and achieves **85.4%** and **78.2%** success rates on the train and test set.

## Pipeline
![](imgs/pipe.jpg)
We propose a novel, object-agnostic method for learning a universal policy for dexterous 
object grasping from realistic point cloud observations and proprioceptive information 
under a table-top setting, namely UniDexGrasp++. To address the challenge of learning 
the vision-based policy across thousands of object instances, we propose Geometry-aware 
Curriculum Learning (**GeoCurriculum**) and Geometry-aware iterative Generalist-Specialist 
Learning (**GiGSL**) which leverage the geometry feature of the task and significantly improve 
the generalizability. With our proposed techniques, our final policy shows universal 
dexterous grasping on thousands of object instances with **85.4%** and **78.2%** success rate 
on the train set and test set which outperforms the state-of-the-art baseline UniDexGrasp 
by **11.7%** and **11.3%**, respectively.



## Installation

Details regarding installation of IsaacGym can be found [here](https://developer.nvidia.com/isaac-gym). We test with `Preview Release 3/4` and `Preview Release 4/4` version of IsaacGym and use the `Preview Release 3/4` in our paper experiment.

Please follow the steps below to perform the installation：


### 1. Create virtual environment
```bash
conda create -n dexgrasp python==3.8
conda activate dexgrasp
```

### 2. Install isaacgym
Once you have downloaded IsaacGym:
```bash
cd <PATH_TO_ISAACGYM_INSTALL_DIR>/python
pip install -e .
```
Ensure that Isaac Gym works on your system by running one of the examples from the `python/examples` 
directory, like `joint_monkey.py`. Please follow troubleshooting steps described in the Isaac Gym Preview Release 3/4
install instructions if you have any trouble running the samples.

### 3. Install dexgrasp
Once Isaac Gym is installed and samples work within your current python environment, install this repo from source code:
```bash
cd <PATH_TO_DEXGRASP_POLICY_DIR>
pip install -e .
```
```
cd DexGrasp-test
pip install -e .
```

### 4. Install pointnet2_ops
```bash
pip install "git+https://github.com/erikwijmans/Pointnet2_PyTorch.git#egg=pointnet2_ops&subdirectory=pointnet2_ops_lib"
```
## Dataset
We use the UniDexGrasp [dataset](https://mirrors.pku.edu.cn/dl-release/UniDexGrasp_CVPR2023/dexgrasp_policy/assets/). Addtionaly please download [datasetv4.1_posedata.npy](https://drive.google.com/file/d/1DajtOFyTPC5YhsO-Fd3Gv17x7eAysI1b/view?usp=share_link) under `assets`. Please unpack them put them under the directory dexgrasp_policy/assets. The full objects and their corresponding scales informations we used are in dexgrasp/cfg/train_set.yaml, dexgrasp/cfg/test_set_seen_cat.yaml, dexgrasp/cfg/test_set_unseen_cat.yaml.

## Training/Evaluation
We provide two tasks: for the state-based policy task, please see `dexgrasp/tasks/shadow_hand_grasp.py`; Please modify `object_code_dict` in `cfg/shadow_hand_grasp.yaml` in order to change the training objects; for the vision-based policy tasks, in order to train on more objects within a certain GPU memory limit, we randomly load objects from the dataset in the beginning of each episode during training. please see `dexgrasp/tasks/shadow_hand_random_load_vision.py`.

Run the following lines in `dexgrasp` folder.

training state-based policy training using ppo:
```bash
bash script/run_train_ppo_state.sh 
```

training state-based policy distillation using DAgger (Please modify `expert` in `dexgrasp/cfg/dagger_value` in order to assign training objects with different teacher policy):
```bash
bash script/run_train_dagger_state.sh 
```

training state to vision policy distillation using DAgger:
```bash
bash script/run_train_dagger_state_to_vision.sh
```

training vision-based policy training using ppo:
```bash
bash script/run_train_ppo_vision.sh
```


Add `--test` in the training scripts for evaluation. For more provided args (e.g., backbone type, test mode), please check these scripts and `utils/config.py`.

## Results and Checkpoints
We provide our trained state-based policy checkpoint at dexgrasp/state_based_model and its detailed evaluation results on all training and test objects at `results/state_based/train_set_results.yaml`, `results/state_based/test_set_seen_cat_results.yaml`, `results/state_based/test_set_unseen_cat_results.yaml`.

## Acknowledgement
The code base used in this project is sourced from these repository:

[NVIDIA-Omniverse/IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)

[PKU-MARL/DexterousHands](https://github.com/PKU-MARL/DexterousHands)

[PKU-EPIC/UniDexGrasp](https://github.com/PKU-EPIC/UniDexGrasp)

## Citation
If you find our papers helpful, please consider cite:
```
@article{xu2023unidexgrasp,
  title={UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy},
  author={Xu, Yinzhen and Wan, Weikang and Zhang, Jialiang and Liu, Haoran and Shan, Zikang and Shen, Hao and Wang, Ruicheng and Geng, Haoran and Weng, Yijia and Chen, Jiayi and others},
  journal={arXiv preprint arXiv:2303.00938},
  year={2023}
}
@article{wan2023unidexgrasp++,
  title={UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning},
  author={Wan, Weikang and Geng, Haoran and Liu, Yun and Shan, Zikang and Yang, Yaodong and Yi, Li and Wang, He},
  journal={arXiv preprint arXiv:2304.00464},
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
LICENSE
README.md
dexgrasp/
  algo/
    pn_utils/
  algorithms/
    __init__.py
    rl/
    utils/
  cfg/
    dagger/
    dagger_value/
    ppo/
    shadow_hand_grasp.yaml
    shadow_hand_random_load_vision.yaml
    test_set_seen_cat.yaml
    test_set_unseen_cat.yaml
    train_set.yaml
  example_model/
    state_based_model.pt
  script/
    run_train_dagger_state.sh
    run_train_dagger_state_to_vision.sh
    run_train_ppo_state.sh
    run_train_ppo_vision.sh
  tasks/
    __init__.py
    hand_base/
    shadow_hand_grasp.py
    shadow_hand_random_load_vision.py
  train.py
  utils/
    autoencoding/
    config.py
    data_info.py
    logger/
    parse_task.py
    process_marl.py
    process_sarl.py
    torch_jit_utils.py
    util.py
imgs/
  pipe.jpg
  teaser.jpg
results/
  state_based/
    test_set_seen_cat_results.yaml
    test_set_unseen_cat_results.yaml
    train_set_results.yaml
setup.py
```

## Config files (7)


### dexgrasp/cfg/dagger/config.yaml

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

### dexgrasp/cfg/dagger_value/config.yaml

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
      path: 'example_model/state_based_model.pt',
      object_code_dict: {
      'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
      }
    },
    {
      name: '1',
      path: 'example_model/state_based_model.pt',
      object_code_dict: {
      'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
      }
    },
    {
      name: '2',
      path: 'example_model/state_based_model.pt',
      object_code_dict: {
      'sem/Car-669043a8ce40d9d78781f76a6db4ab62':[0.06],
      }
    },
  ]

```

### dexgrasp/cfg/ppo/config.yaml

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

### dexgrasp/cfg/shadow_hand_grasp.yaml

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

### dexgrasp/cfg/shadow_hand_random_load_vision.yaml

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

### dexgrasp/cfg/test_set_seen_cat.yaml

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

### dexgrasp/cfg/test_set_unseen_cat.yaml

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

## Python signatures and reward/observation bodies (32 files)


### dexgrasp/algo/pn_utils/maniskill_learn/apis/train_rl.py

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

### dexgrasp/algo/pn_utils/maniskill_learn/networks/policy_network/continuous_policy.py

```
class ContinuousPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, num_actions, mode, detach_encoder)
```

### dexgrasp/algo/pn_utils/maniskill_learn/networks/policy_network/vae_policy.py

```
class VAEPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action, decode)
```

### dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/base.py

```
class BaseFileHandler()
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
    def load_from_path(self, filepath, mode)
    def dump_to_path(self, obj, filepath, mode)
```

### dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/csv_handler.py

```
class CSVHandler(BaseFileHandler)
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
```

### dexgrasp/algo/pn_utils/maniskill_learn/utils/fileio/serialization/handlers/pickle_handler.py

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

### dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/collect_env.py

```
def get_PIL_version()
def collect_base_env()
def collect_env()
```

### dexgrasp/algo/pn_utils/maniskill_learn/utils/meta/config.py

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

### dexgrasp/tasks/hand_base/base_task.py

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

### dexgrasp/tasks/hand_base/multi_vec_task.py

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

### dexgrasp/tasks/hand_base/vec_task.py

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

### dexgrasp/tasks/shadow_hand_grasp.py

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

### dexgrasp/tasks/shadow_hand_random_load_vision.py

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

### dexgrasp/train.py

```
def train()
```

### dexgrasp/utils/autoencoding/maniskill_learn/apis/train_rl.py

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

### dexgrasp/utils/autoencoding/maniskill_learn/networks/policy_network/continuous_policy.py

```
class ContinuousPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape, encoder_cfg, if_contrast)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, num_actions, mode, detach_encoder)
```

### dexgrasp/utils/autoencoding/maniskill_learn/networks/policy_network/vae_policy.py

```
class VAEPolicy(ExtendedModule)
    def __init__(self, nn_cfg, policy_head_cfg, action_space, obs_shape, action_shape)
    def init_weights(self, pretrained, init_cfg)
    def forward(self, state, action, decode)
```

### dexgrasp/utils/autoencoding/maniskill_learn/utils/fileio/serialization/handlers/base.py

```
class BaseFileHandler()
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
    def load_from_path(self, filepath, mode)
    def dump_to_path(self, obj, filepath, mode)
```

### dexgrasp/utils/autoencoding/maniskill_learn/utils/fileio/serialization/handlers/csv_handler.py

```
class CSVHandler(BaseFileHandler)
    def load_from_fileobj(self, file)
    def dump_to_fileobj(self, obj, file)
    def dump_to_str(self, obj)
```

### dexgrasp/utils/autoencoding/maniskill_learn/utils/fileio/serialization/handlers/pickle_handler.py

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

### dexgrasp/utils/autoencoding/maniskill_learn/utils/meta/collect_env.py

```
def get_PIL_version()
def collect_base_env()
def collect_env()
```

### dexgrasp/utils/autoencoding/maniskill_learn/utils/meta/config.py

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

### dexgrasp/utils/autoencoding/train.py

```
def save_point_cloud_to_ply(points, colors, save_name, save_root)
def train_and_evaluate()
```

### dexgrasp/utils/autoencoding/trainer.py

```
class Trainer()
    def __init__(self, num_steps, device)
    def train_step(self, x)
    def save(self, path)
    def load(self, path)
    def evaluate(self, x)
```

### dexgrasp/utils/config.py

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

### dexgrasp/utils/parse_task.py

```
def parse_task(args, cfg, cfg_train, sim_params, agent_index)
```