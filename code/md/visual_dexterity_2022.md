# visual_dexterity_2022

source: https://github.com/Improbable-AI/dexenv


commit: ad9634e9d26cf5555d18728244a58f5b412c1eb2


## README

# Visual Dexterity

---

This is the codebase for [Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes](https://arxiv.org/abs/2211.11744), accepted by Science Robotics. While we provide the code that uses the D'Claw robot hand, it can be easily adapted to other robot hands.

### [[Project Page]](https://taochenshh.github.io/projects/visual-dexterity), [[Science Robotics]](https://www.science.org/doi/10.1126/scirobotics.adc9244), [[arXiv]](https://arxiv.org/abs/2211.11744), [[Github]](https://github.com/Improbable-AI/dexenv)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10039109.svg)](https://doi.org/10.5281/zenodo.10039109)


## :books: Citation

```
@article{chen2023visual,
    author = {Tao Chen  and Megha Tippur  and Siyang Wu  and Vikash Kumar  and Edward Adelson  and Pulkit Agrawal },
    title = {Visual dexterity: In-hand reorientation of novel and complex object shapes},
    journal = {Science Robotics},
    volume = {8},
    number = {84},
    pages = {eadc9244},
    year = {2023},
    doi = {10.1126/scirobotics.adc9244},
    URL = {https://www.science.org/doi/abs/10.1126/scirobotics.adc9244},
    eprint = {https://www.science.org/doi/pdf/10.1126/scirobotics.adc9244},
}
```

```
@article{chen2021system,
    title={A System for General In-Hand Object Re-Orientation},
    author={Chen, Tao and Xu, Jie and Agrawal, Pulkit},
    journal={Conference on Robot Learning},
    year={2021}
}
```

## :gear: Installation

#### Dependencies
* [PyTorch](https://pytorch.org/)
* [PyTorch3D](https://pytorch3d.org/)
* [Isaac Gym](https://developer.nvidia.com/isaac-gym) (results in the paper are trained with Preview 3.)
* [IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)
* [Minkowski Engine](https://github.com/NVIDIA/MinkowskiEngine)
* [Wandb](https://wandb.ai/site)


#### Download packages
You can either use a virtual python environment or a docker for training. Below we show the process to set up the docker image. If you prefer using a virtual python environment, you can just install the dependencies in the virtual environment.

Here is how the directory looks like:
```
-- Root
---- dexenv
---- IsaacGymEnvs
---- isaacgym
```

```
# download packages
git clone git@github.com:Improbable-AI/dexenv.git
git clone https://github.com/NVIDIA-Omniverse/IsaacGymEnvs.git

# download IsaacGym from: 
# (https://developer.nvidia.com/isaac-gym)
# unzip it in the current directory

# remove the package dependencies in the setup.py in isaacgym/python and IsaacGymEnvs/
```

#### Download the assets

Download the robot and object assets from [here](https://huggingface.co/datasets/taochenshh/dexenv/blob/main/assets.zip), and unzip it to `dexenv/dexenv/`.

#### Download the pretrained models

Download the pretrained checkpoints from [here](https://huggingface.co/datasets/taochenshh/dexenv/blob/main/pretrained.zip), and unzip it to `dexenv/dexenv/`.

#### Prepare the docker image
1. You can download a pre-built docker image:
```
docker pull improbableailab/dexenv:latest
```
2. Or you can build the docker image locally:
```
cd dexenv/docker
python docker_build.py -f Dockerfile
```

#### Launch the docker image

To run the docker image, you would need to have the nvidia-docker installed. Follow the instructions [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
```bash
# launch docker
./run_image.sh # you would need to have wandb installed in the python environment
```

In another terminal
```bash
./visualize_access.sh
# after this, you can close it, just need to run this once after every machine reboot
```


## :scroll: Usage

#### :bulb: Training Teacher

```bash
# if you are running in the docker, you might need to run the following line
git config --global --add safe.directory /workspace/dexenv

# debug teacher (run debug first to make sure everything runs)
cd /workspace/dexenv/dexenv/train/teacher
python mlp.py -cn=debug_dclaw # show the GUI
python mlp.py task.headless=True -cn=debug_dclaw # in headless mode

# if you wanna just train the hand to reorient a cube, add `task.env.name=DClawBase`
python mlp.py task.env.name=DClawBase -cn=debug_dclaw 

# training teacher
cd /workspace/dexenv/dexenv/train/teacher
python mlp.py -cn=dclaw
python mlp.py task.task.randomize=False -cn=dclaw # turn off domain randomization
python mlp.py task.env.name=DClawBase task.task.randomize=False -cn=dclaw # reorient a cube without domain randomization

# if you wanna change the number of objects or the number of environments
python mlp.py alg.num_envs=4000 task.obj.num_objs=10 -cn=dclaw

# testing teacher
cd /workspace/dexenv/dexenv/train/teacher
python mlp.py alg.num_envs=20 resume_id=<wandb exp ID> -cn=test_dclaw
# e.g. python mlp.py alg.num_envs=20 resume_id=dexenv/1d1tvd0b -cn=test_dclaw

```

#### :high_brightness: Training Student with Synthetic Point Cloud (student stage 1)

```
# debug student
cd /workspace/dexenv/dexenv/train/student
python rnn.py -cn=debug_dclaw_fptd
# by default, the command above used the pretrained teacher model you downloaded above, 
#if you wanna use another teacher model, add `alg.expert_path=<path>`
python rnn.py alg.expert_path=<path to teacher model> -cn=debug_dclaw_fptd

# training student
cd /workspace/dexenv/dexenv/train/student
python rnn.py -cn=dclaw_fptd

# testing student
cd /workspace/dexenv/dexenv/train/student
python rnn.py resume_id=<wandb exp ID> -cn=test_dclaw_fptd
```

#### :tada: Training Student with rendered Point Cloud (student stage 2)

```
# debug student
cd /workspace/dexenv/dexenv/train/student
python rnn.py -cn=debug_dclaw_rptd

# training student
cd /workspace/dexenv/dexenv/train/student
python rnn.py -cn=dclaw_rptd

# testing student
cd /workspace/dexenv/dexenv/train/student
python rnn.py resume_id=<wandb exp ID> -cn=test_dclaw_rptd
```

## :rocket: Pre-trained models

We provide the pre-trained models for both the teacher and the student (stage 2) in `dexenv/expert/artifacts`. The models were trained using Isaac Gym preview 3.

```
# to see the teacher pretrained model
cd /workspace/dexenv/dexenv/train/teacher
python demo.py

# to see the student pretrained model
cd /workspace/dexenv/dexenv/train/student
python rnn.py alg.num_envs=20 task.obj.num_objs=10  alg.pretrain_model=/workspace/dexenv/dexenv/pretrained/artifacts/student/train-model.pt test_pretrain=True test_num=3 -cn=debug_dclaw_rptd
```



## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
dexenv/
  __init__.py
  agent/
    ppo_agent.py
    rnn_agent.py
  conf/
    dclaw.yaml
    dclaw_fptd.yaml
    dclaw_rptd.yaml
    debug_dclaw.yaml
    debug_dclaw_fptd.yaml
    debug_dclaw_rptd.yaml
    hand_default.yaml
    hydra/
    logging/
    task/
    test_dclaw.yaml
    test_dclaw_fptd.yaml
    test_dclaw_rptd.yaml
  engine/
    base_engine.py
    ppo_engine.py
    rnn_engine.py
  envs/
    __init__.py
    base/
    dclaw_base.py
    dclaw_fptd.py
    dclaw_multiobjs.py
    dclaw_rptd.py
    rewards.py
  models/
    diag_gaussian_pol/
    sequence/
    sparse_cnn_rnn_models.py
    state_model.py
    utils.py
    value_nets/
    voxel_impala.py
    voxel_model.py
  runner/
    base_runner.py
    nstep_runner.py
    rnn_runner.py
  train/
    __init__.py
    student/
    teacher/
  utils/
    __init__.py
    common.py
    constants.py
    create_task_env.py
    data.py
    dataset.py
    gae.py
    hand_color.py
    hydra_util.py
    info_util.py
    isaac_utils.py
    minkowski_utils.py
    os_utils.py
    pcd_augmentation.py
    point_cloud_utils.py
    rand_util.py
    torch_utils.py
    voxel_utils.py
    wandb_utils.py
docker/
  10_nvidia.json
  Dockerfile
  docker_build.py
  entrypoint.sh
  gym_rendering.sh
  install_mk.sh
  install_py_packages.sh
  install_python_3_8.sh
  install_pytorch3d.sh
  nvidia_icd.json
  run_image.sh
  visualize_access.sh
requirements.txt
setup.py
```

## Config files (20)


### dexenv/conf/dclaw.yaml

```yaml
defaults:
  - hand_default.yaml
  - _self_

alg:
  env_name: DclawMultiObjs
  num_envs: 8000
  init_logstd: -0.2

task:
  env:
    name: DclawMultiObjs
  obj:
    dataset: miscnet

logging:
  eval_interval: 600
```

### dexenv/conf/dclaw_fptd.yaml

```yaml
defaults:
  - dclaw.yaml
  - _self_

alg:
  env_name: DclawFakePTD
  expert_path: pretrained/artifacts/teacher/train-model.pt
  batch_size: 40
  num_envs: 400
  num_batches: null
  train_rollout_steps: 80
  traj_keys_in_cpu: [ 'ob', 'action', 'reward', 'done', 'true_done', 'state' ]
  opt_epochs: 4
  max_grad_norm: 5.
  reset_first_in_rollout: True
  std_cond_in: True
  loss: 'mle'
  decay_lr: True
  deque_size: 1800
  run_eval: True
  det_eval: True
  sto_eval: False
  sample_action: True
  lr: 0.0003

task:
  env:
    loadCADPTD: True
    name: DclawFakePTD
  task:
    randomization_params:
      frequency: 240


vision:
  clip_action: False
  clip_eps: 0.
  encoder: 'impala'
  embed_dim: 256
  batch_norm: True
  layer_norm: False
  act: gelu
  mink_act: relu
  channel_groups: [ 32, 64, 128, 256 ]
  no_pool: False
  quantization_size: 0.005
  speed_optimized: True
  quantization_mode: 'random'
  optim_empty_cache: True
  color_channels: 1
  pred_rot_dist: True
  rot_dist_loss_coef: 0.5
  rot_loss_type: 'mse'
  ptd_noise: True
  ptd_noise_prob: 0.4
  act_in: True

  rnn_features: 256
  rnn_layers: 1

  roll_thresh: 5.
  loss_queue: 10
  roll_min_interval: 100
  deter_policy: False
  spatial_shape: [ 150, 150, 130 ]


logging:
  log_interval: 1
  ckpt_interval: 30
  eval_interval: 60

```

### dexenv/conf/dclaw_rptd.yaml

```yaml
defaults:
  - dclaw_fptd.yaml
  - _self_


alg:
  env_name: DclawRealPTD
  batch_size: 20
  num_envs: 260

task:
  env:
    loadCADPTD: True
    name: DclawRealPTD

logging:
  wandb:
    project: dexenv
  log_interval: 1
```

### dexenv/conf/debug_dclaw.yaml

```yaml
defaults:
  - dclaw.yaml
  - _self_

task:
  headless: False
  obj:
    num_objs: 2

alg:
  num_envs: 40

logging:
  wandb:
    mode: offline


```

### dexenv/conf/debug_dclaw_fptd.yaml

```yaml
defaults:
  - dclaw_fptd.yaml
  - _self_


task:
  headless: False
  obj:
    num_objs: 2

alg:
  num_envs: 20
  batch_size: 20
  train_rollout_steps: 60
  opt_epochs: 2

logging:
  wandb:
    mode: offline
```

### dexenv/conf/debug_dclaw_rptd.yaml

```yaml
defaults:
  - dclaw_rptd.yaml
  - _self_


task:
  headless: False
  obj:
    num_objs: 2

alg:
  num_envs: 20
  batch_size: 10
  train_rollout_steps: 60
  opt_epochs: 2

logging:
  wandb:
    mode: offline
```

### dexenv/conf/hand_default.yaml

```yaml
defaults:
  - task: dclaw
  - hydra: default
  - logging: default
  - _self_

task:
  env:
    rew:
      fallDistance: 0.15
  sim:
    device: 'cuda'
    rl_device: 'cuda'

alg:
  env_name: DClawBase
  num_envs: 16384
  all_in_torch: True
  env_always_return_true_info: True
  train_rollout_steps: 8
  eval_rollout_steps: 120
  run_eval: False
  opt_epochs: 12
  vf_coef: 0.0005
  clip_range: 0.1
  num_batches: 4
  deque_size: 60000
  tqdm: False
  max_steps: 100000000000000
  act: elu
  max_grad_norm: 1.0
  seed: 0
  device: 'cuda'
  policy_lr: 0.0003
  value_lr: 0.001
  smooth_eval_tau: 0.70
  pretrain_model: null
  reset_first_in_rollout: False
  traj_keys_in_cpu: null
  rew_discount: 0.99
  gae_lambda: 0.95
  ent_coef: 0


resume: False
resume_id: null # the run id of wandb run
resume_to_diff_id: False
resume_root: null # used to specify the root directory created by the hydra run
resume_optim: True
render: False
test: False
test_num: 1
test_dir: null
test_pretrain: False
test_eval_best: False
save_eval_ckpt: False
save_ob_in_eval: False
save_test_traj: False
save_type: null # s for success and f for failure, if 's', it will only save successfull trajectories
save_best_on_success: False

logging:
  log_interval: 20
  ckpt_interval: 600
  wandb:
    project: dexenv
```

### dexenv/conf/hydra/default.yaml

```yaml
#run:
#  dir: ${oc.env:PROJECT_ROOT}/outputs/${now:%Y-%m-%d-%H-%M-%S}
#
#sweep:
#  dir: ${oc.env:PROJECT_ROOT}/outputs/mrun-${now:%Y-%m-%d-%H-%M-%S}/
#  subdir: ${hydra.job.num}_${hydra.job.id}

run:
  dir: ${oc.env:HYDRA_OUT_ROOT}/outputs/${uuid:}

sweep:
  dir: ${oc.env:HYDRA_OUT_ROOT}/outputs/${uuid:}

job:
  env_set:
    WANDB_START_METHOD: thread
    WANDB_DIR: '.'

```

### dexenv/conf/hydra/hydra_logging/custom.yaml

```yaml
version: 1
formatters:
  colorlog:
    '()': 'colorlog.ColoredFormatter'
    format: "[%(cyan)s%(asctime)s%(reset)s][%(log_color)s%(levelname)s%(reset)s] %(message)s"
handlers:
  console:
    class: logging.StreamHandler
    formatter: colorlog
    stream: ext://sys.stdout
root:
  level: INFO
  handlers: [ console ]

disable_existing_loggers: false
```

### dexenv/conf/hydra/job_logging/custom.yaml

```yaml
version: 1
formatters:
  colorlog:
    '()': 'colorlog.ColoredFormatter'
    format: "[%(cyan)s%(asctime)s%(reset)s][%(log_color)s%(levelname)s%(reset)s] %(message)s"
handlers:
  console:
    class: logging.StreamHandler
    formatter: colorlog
    stream: ext://sys.stdout
root:
  level: INFO
  handlers: [ console ]

disable_existing_loggers: false
```

### dexenv/conf/logging/default.yaml

```yaml
wandb:
  project: dexenv
  mode: 'online'
  tags: null
  group: null
  entity: null
  name: null
  settings:
    ignore_globs: [ '*.pt' ]

eval_interval: 100
ckpt_interval: 100
log_interval: 10
```

### dexenv/conf/task/dclaw.yaml

```yaml
defaults:
  - isaacgym_config.yaml
  - obj: miscnet
  - task: obj_rand
  - _self_

cam:
  height: 180
  width: 320
  hov: 64
  cuda: True
  cam_num: 1
  sample_num: 6000
  debug_rgb: False
  visual_render_height: 960 # to save images for visualization purpose
  visual_render_width: 1280

env:
  name: DClawBase
  robot: 'dclaw_4f'
  numEnvs: ${...alg.num_envs}
  envSpacing: 0.5
  episodeLength: 80 # Not used, but would be 8 sec if resetTime is not set
  resetTime: 10 # Max time till reset, in seconds, if a goal wasn't achieved. Will overwrite the episodeLength if is > 0.
  enableDebugVis: False
  aggregateMode: 1

  clipActions: 1.0

  numObservations: null
  numStates: null
  numActions: null

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: True
  relativeToPrevTarget: False
  limitAbsoluteCommand: False


  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 15.0
  forceProbRange: [ 0.19,0.2 ]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  rew:
    distRewardScale: -10.0
    ftipRewardScale: -1.
    rotRewardScale: 1.0
    rotEps: 0.1
    reachGoalBonus: 800
    fallDistance: 0.24
    fallPenalty: -100
    successTolerance: 0.4
    time_due_penalty: False
    max_dof_vel: ${..dof_vel_pol_limit}
    action_norm_thresh: 1.0
    obj_lin_vel_thresh: 0.04
    obj_ang_vel_thresh: 0.5
    dof_vel_thresh: 0.25
    energy_scale: 20
    clip_energy_reward: True
    energy_upper_bound: 10
    timeout_not_done: False
    rew_scale: 1.
    pen_tb_contact: False
    tb_cf_scale: 1


  objectType: "block" # can be block, egg or pen
  observationType: "full" # can be "openai", "full_no_vel", "full","full_state"
  blockscale: null

  printNumSuccesses: False
  maxConsecutiveSuccesses: 50
  averFactor: 0.1 # running mean factor for consecutive successes calculation

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False
  loadCADPTD: False
  robotCadNumPts: 500
  objCadNumPts: 500
  vhacd: True
  stiffness: [ 2.7724128689655174, 3.558619503448275, 3.5586195034482757 ]
  damping: [ 0.273946924137931, 0.382384248275862, 0.382384248275862 ]
  tableInitialFriction: 0.5
  scaleDyn: False
  dofSpeedScale: 24
  controlFrequencyInv: 5
  predDyn: False
  tactile: False
  obj_init_delta_pos: null
  dof_vel_hard_limit: [ 6.55172413793103, 7.758620689655173, 7.7586206896551 ]
  effort_limit: 2.6
  dof_vel_pol_limit: 3.5
  ptd_to_robot_base: True

  soft_control: False

  gated_action: False
  action_ema: 0.8
  dof_torque_on: True
  latency_max_steps: 1
  sim_latency: False
  latency_rand_freq: 6000
  rand_once: False
  rm_obj_dark_part: False
  obj_ratio: [ 0.25, 0.7 ]
  sn_layers: null
  record_obj_id: False


  obj:
    restitution: 0.5
    friction: 0.8
    torsion_friction: 0.1
    rolling_friction: 0.1

  table:
    restitution: 0.5
    friction: 0.5
    torsion_friction: 0.1
    rolling_friction: 0.1

  hand:
    restitution: 0.5
    friction: 0.8
    torsion_friction: 0.1
    rolling_friction: 0.1



```

### dexenv/conf/task/isaacgym_config.yaml

```yaml
# used to create the object
name: ShadowHand

physics_engine: physx
# disables rendering
headless: True
rgb_render: False

sim:
  device: 'cuda'
  rl_device: 'cuda'
  dt: 0.01667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: True
  gravity: [ 0.0, 0.0, -9.81 ]
  physx:
    num_threads: 8
    solver_type: 1
    num_position_iterations: 8
    num_velocity_iterations: 0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: 4
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    contact_collection: 1

```

### dexenv/conf/task/obj/default.yaml

```yaml
dataset: null
path: null
load_texture: False
object_id: null
start_id: null
end_id: null
num_objs: 500000
```

### dexenv/conf/task/obj/egad.yaml

```yaml
defaults:
  - default.yaml
  - _self_

dataset: egad
```

### dexenv/conf/task/obj/miscnet.yaml

```yaml
defaults:
  - default.yaml
  - _self_

dataset: miscnet
```

### dexenv/conf/task/task/obj_rand.yaml

```yaml
randomize: True
randomization_params:
  frequency: 1200
  observations:
    range: [ 0, .002 ]
    range_correlated: [ 0, .001 ]
    operation: "additive"
    distribution: "gaussian"
  actions:
    range: [ 0., .05 ]
    range_correlated: [ 0, .015 ]
    operation: "additive"
    distribution: "gaussian"
  sim_params:
    gravity:
      range: [ 0, 0.4 ]
      operation: "additive"
      distribution: "gaussian"
  actor_params:
    hand:
      dof_properties:
        damping:
          range: [ 0.8, 1.2 ]
          operation: "scaling"
          distribution: "uniform"
        stiffness:
          range: [ 0.8, 1.2 ]
          operation: "scaling"
          distribution: "uniform"
      rigid_body_properties:
        mass:
          range: [ 0.8, 1.2 ]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True
      rigid_shape_properties:
        friction:
          num_buckets: 100
          range: [ 0.3, 2.0 ]
          operation: "scaling"
          distribution: "uniform"
          same_for_all: True
        restitution:
          num_buckets: 100
          range: [ 0.0, 2 ]
          operation: "scaling"
          distribution: "uniform"
    object:
      scale:
        range: [ 0.95, 1.05 ]
        operation: "scaling"
        distribution: "uniform"
        setup_only: True
      rigid_body_properties:
        mass:
          range: [ 0.3, 1.8 ]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True
      rigid_shape_properties:
        friction:
          num_buckets: 100
          range: [ 0.3, 2.0 ]
          operation: "scaling"
          distribution: "uniform"
          same_for_all: True
        restitution:
          num_buckets: 100
          range: [ 0.0, 2 ]
          operation: "scaling"
          distribution: "uniform"
    table:
      rigid_shape_properties:
        friction:
          num_buckets: 100
          range: [ 0.01, 2 ]
          operation: "scaling"
          distribution: "uniform"
          same_for_all: True
        restitution:
          num_buckets: 100
          range: [ 0.0, 2 ]
          operation: "scaling"
          distribution: "uniform"
          same_for_all: True
```

### dexenv/conf/test_dclaw.yaml

```yaml
defaults:
  - dclaw.yaml
  - _self_

task:
  headless: False
  obj:
    num_objs: 30

alg:
  num_envs: 500
  sample_action: False

test: True
test_num: 10


```

### dexenv/conf/test_dclaw_fptd.yaml

```yaml
defaults:
  - dclaw_fptd.yaml
  - _self_

task:
  headless: False
  obj:
    num_objs: 15

alg:
  num_envs: 100
  sample_action: False

test: True
test_num: 3


```

### dexenv/conf/test_dclaw_rptd.yaml

```yaml
defaults:
  - dclaw_rptd.yaml
  - _self_

task:
  headless: False
  obj:
    num_objs: 15

alg:
  num_envs: 100
  sample_action: False

test: True
test_num: 3


```

## Python signatures and reward/observation bodies (53 files)


### dexenv/agent/ppo_agent.py

```
class PPOAgent()
    def __post_init__(self)
    def get_action(self, ob, sample, get_action_only)
    def get_act_val(self, ob, no_val)
    def get_val(self, ob)
    def optimize(self, data)
    def optim_preprocess(self, data)
    def cal_loss(self, val, old_val, ret, log_prob, old_log_prob, adv, entropy)
    def cal_val_loss(self, val, old_val, ret)
    def train_mode(self)
    def eval_mode(self)
    def save_model(self, wandb_run, is_best, step, eval)
    def load_model(self, pretrain_model, eval)
    def print_param_grad_status(self)
```

### dexenv/agent/rnn_agent.py

```
class RNNAgent()
    def __post_init__(self)
    def extract_obs(self, ob)
    def get_action(self, ob, sample, hidden_state, get_action_only)
    def optim_preprocess(self, data)
    def optimize(self, data)
    def clear_optim_grad(self)
    def cal_loss(self, act_dist, exp_act_loc, exp_act_scale, mask)
    def train_mode(self)
    def eval_mode(self)
    def save_model(self, wandb_run, is_best, step, eval)
    def load_model(self, pretrain_model, eval)
    def load_expert_model(self)
```

### dexenv/engine/base_engine.py

```
class BaseEngine()
    def __post_init__(self)
    def train(self)
    def rollout_once(self)
    def do_eval(self, det, sto)
    def eval(self, render, eval_num, sleep_time, sample, no_tqdm)
    def get_train_log(self, optim_infos, traj)
    def get_dataloader(self, dataset, batch_size)
    def _check_ckpt_is_best(self, cur_val, best_history_val, bigger_is_better)
    def _get_batch_size(self, dataset)
```

### dexenv/engine/ppo_engine.py

```
class PPOEngine(BaseEngine)
    def train(self)
    def train_once(self, traj)
    def traj_preprocess(self, traj)
    def cal_advantages(self, traj, start_time)
```

### dexenv/engine/rnn_engine.py

```
def extract_traj_data_rnn(cfg, states, data, act_dim)
class RNNEngine(BaseEngine)
    def train(self)
    def traj_preprocess(self, traj)
    def train_once(self, traj)
    def eval(self, render, eval_num, sleep_time, sample, smooth, no_tqdm, return_on_done)
```

### dexenv/envs/base/vec_task.py

```
class Env(ABC)
    def __init__(self, config, sim_device, rl_device, graphics_device_id, headless)
    def create_ob_act_space(self)
    def allocate_buffers(self)
    def step(self, actions)
    def reset(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTask(Env)
    def __init__(self, config, sim_device, rl_device, graphics_device_id, headless)
    def set_viewer(self)
    def allocate_buffers(self)
    def allocate_ob_buffers(self)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def get_state(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def step(self, actions)
    def update_obs(self)
    def zero_actions(self)
    def reset(self)
    def render(self)
    def __parse_sim_params(self, physics_engine, config_sim)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)

```python
def observation_space(self) -> gym.Space:
        """Get the environment's observation space."""
        return self.obs_space
```
```

### dexenv/envs/dclaw_base.py

```
class DClawBase(VecTask)
    def __init__(self, cfg, sim_device, rl_device, graphics_device_id)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def create_camera(self, camera_poses, env_ptr, camera_params)
    def get_visual_render_camera_setup(self)
    def create_hand_actor(self, env_ptr, dclaw_asset, dclaw_start_pose, dclaw_dof_props, env_id)
    def set_hand_color(self, env_ptr, dclaw_actor)
    def get_table_asset(self)
    def get_table_pose(self)
    def get_dclaw_start_pose(self)
    def setup_torch_states(self)
    def get_dclaw_asset(self, asset_root, asset_options)
    def get_object_start_pose(self, dclaw_start_pose)
    def get_goal_object_start_pose(self, object_start_pose)
    def set_dof_props(self, props_dict)
    def update_obj_mass(self, env_ids)
    def reset(self)
    def compute_reward(self, actions)
    def get_images(self)
    def compute_observations(self)
    def allocate_ob_buffers(self)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self)
    def update_obs(self)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def get_numpy_rgb_images(self, camera_handles)
    def pre_physics_step(self, actions)
    def post_physics_step(self)

```python
def compute_reward(self, actions):
        res = compute_dclaw_reward(
            self.reset_buf, self.reset_goal_buf, self.progress_buf,
            self.successes, self.max_episode_length,
            self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.cfg['env']['rew'], self.actions,
            self.fingertip_pos, self.fingertip_vel, self.object_linvel, self.object_angvel,
            self.dclaw_dof_vel, self.dclaw_dof_torque,
            table_cf=self.table_contact_force if self.cfg.env.rew.pen_tb_contact else None
        )
        self.rew_buf[:] = res[0] * self.cfg.env.rew.rew_scale
        self.done_buf[:] = res[1]
        self.reset_buf[:] = res[2]
        self.reset_goal_buf[:] = res[3]
        self.progress_buf[:] = res[4]
        self.successes[:] = res[5]
        abs_rot_dist = res[6]
        reward_terms = res[7]
        timeout_envs = res[8]

        self.extras['success'] = self.reset_goal_buf.detach().to(self.rl_device).flatten()
        self.extras['abs_dist'] = abs_rot_dist.detach().to(self.rl_device)
        self.extras['TimeLimit.truncated'] = timeout_envs.detach().to(self.rl_device)
        for reward_key, reward_val in reward_terms.items():
            self.extras[reward_key] = reward_val.detach()
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        if self.cfg.env.dof_torque_on:
            self.gym.refresh_dof_force_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state":
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        if self.cfg.env.rew.pen_tb_contact:
            self.gym.refresh_net_contact_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_vel = self.rigid_body_states[:, self.fingertip_handles][:, :, 7:13]

        if self.obs_type == "full_no_vel":
            obs_buf = self.compute_full_observations(no_vel=True)
        elif self.obs_type == "full":
            obs_buf = self.compute_full_observations()
        elif self.obs_type == "full_state":
            obs_buf = self.compute_full_state()
        else:
            print("Unkown observations type!")
        self.obs_buf = obs_buf

        if self.cfg.rgb_render:
            self.gym.fetch_results(self.sim, True)
            self.gym.step_graphics(self.sim)
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)
            self.render_rgb_obs_buf = self.get_numpy_rgb_images(self.render_camera_handles)
            self.gym.end_access_image_tensors(self.sim)
```

```python
def compute_full_observations(self, no_vel=False):
        scaled_dof_pos = unscale(
            self.dclaw_dof_pos,
            self.dclaw_dof_lower_limits,
            self.dclaw_dof_upper_limits
        )
        quat_dist = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

        if no_vel:
            out = torch.cat(
                [
                    scaled_dof_pos,
                    self.object_pose,
                    self.goal_rot,
                    quat_dist,
                    self.fingertip_pos.reshape(self.num_envs, 3 * self.num_fingertips),
                    self.actions
                ],
                dim=-1
            )
        else:
            out = torch.cat(
                [
                    scaled_dof_pos,
                    self.vel_obs_scale * self.dclaw_dof_vel,
                    self.object_pose,
                    self.object_linvel,
                    self.vel_obs_scale * self.object_angvel,
                    self.goal_rot,
                    quat_dist,
                    self.fingertip_state.reshape(self.num_envs, 13 * self.num_fingertips),
                    self.actions
                ],
                dim=-1
            )
        return out
```
```

### dexenv/envs/dclaw_fptd.py

```
class DclawFakePTD(DclawMultiObjs)
    def __init__(self, cfg, sim_device, rl_device, graphics_device_id, quantization_size)
    def read_finger_ptd(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def reset(self)
    def update_obs(self)
    def compute_observations(self)
    def compute_ptd_observations(self)
    def allocate_ob_buffers(self)
    def setup_cam_pose(self)

```python
def compute_observations(self):
        super().compute_observations()
        self.scene_ptd_buf = self.compute_ptd_observations()
```

```python
def compute_ptd_observations(self):
        self.hand_link_pos = self.rigid_body_states[:, self.hand_body_handles][:, :, 0:3]
        self.hand_link_quat = self.rigid_body_states[:, self.hand_body_handles][:, :, 3:7]
        object_pos = self.object_pos
        object_quat = self.object_rot

        goal_pos = self.goal_pos + self.goal_displacement_tensor[None, :]
        goal_quat = self.goal_rot
        quats = torch.cat((self.hand_link_quat, object_quat[:, None, :], goal_quat[:, None, :]), dim=1)
        trans = torch.cat((self.hand_link_pos, object_pos[:, None, :], goal_pos[:, None, :]), dim=1)
        quats_in_p3d = quat_xyzw_to_wxyz(quats)
        rot_mat = p3dtf.quaternion_to_matrix(quats_in_p3d)
        if self.cfg.env.ptd_to_robot_base:
            if self.base_link_pose_inv_rot is None:
                base_link_pos = self.rigid_body_states[:, self.base_link_handle][..., :3]
                base_link_quat = self.rigid_body_states[:, self.base_link_handle][..., 3:7]
                base_link_quat_in_p3d = quat_xyzw_to_wxyz(base_link_quat)
                base_link_rot_mat = p3dtf.quaternion_to_matrix(base_link_quat_in_p3d)
                self.base_link_pose_inv_rot = base_link_rot_mat.transpose(-2, -1)
                self.base_link_pose_inv_pos = -self.base_link_pose_inv_rot @ base_link_pos.unsqueeze(-1)
            composed_rot = self.base_link_pose_inv_rot @ rot_mat
            composed_pos = self.base_link_pose_inv_rot @ trans.unsqueeze(-1) + self.base_link_pose_inv_pos
            rot_mat = composed_rot
            trans = composed_pos.squeeze(-1)

        rot_mat_T = rot_mat.transpose(-2, -1)
        self.se3_T_hand_buf[:, :3, :3] = rot_mat_T[:, :-2, :3, :3].reshape(-1, 3, 3)
        self.se3_T_hand_buf[:, 3, :3] = trans[:, :-2].reshape(-1, 3)
        self.se3_T_obj_buf[:, :3, :3] = rot_mat_T[:, -2:, :3, :3].reshape(-1, 3, 3)
        self.se3_T_obj_buf[:, 3, :3] = trans[:, -2:].reshape(-1, 3)
        hand_transform = p3dtf.Transform3d(matrix=self.se3_T_hand_buf)
        obj_transform = p3dtf.Transform3d(matrix=self.se3_T_obj_buf)

        hand_obs = hand_transform.transform_points(points=self.hand_cad_ptd)
        obj_obs = obj_transform.transform_points(points=self.obj_cad_ptd)
        hand_obs = hand_obs.view(self.num_envs, -1, 3)
        obj_obs = obj_obs.view(self.num_envs, -1, 3)
        ptd_obs = torch.cat((hand_obs, obj_obs), dim=1)
        if self.quantization_size is not None:
            ptd_obs = ptd_obs / self.quantization_size
            ptd_obs = ptd_obs.int()
        return ptd_obs
```
```

### dexenv/envs/dclaw_multiobjs.py

```
class DclawMultiObjs(DClawBase)
    def __init__(self, cfg, sim_device, rl_device, graphics_device_id)
    def set_random_gen(self, seed)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def parse_obj_dataset(self, dataset)
    def get_object_category(self, urdf_path)
    def load_object_asset(self)
    def load_an_object(self, asset_root, object_urdf)
    def change_obj_asset_dyn(self, obj_asset)
```

### dexenv/envs/dclaw_rptd.py

```
class DclawRealPTD(DclawMultiObjs)
    def __init__(self, cfg, sim_device, rl_device, graphics_device_id, quantization_size)
    def read_finger_ptd(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def update_obs(self)
    def compute_observations(self)
    def compute_ptd_observations(self)
    def setup_ptd_cam(self, camera_params)
    def get_camera_pose(self)
    def get_camera_setup(self)
def filter_hand_base(pts)

```python
def compute_observations(self):
        super().compute_observations()
        self.scene_ptd_buf[:] = self.compute_ptd_observations()
```

```python
def compute_ptd_observations(self):
        self.gym.fetch_results(self.sim, True)
        self.gym.step_graphics(self.sim)
        self.gym.render_all_camera_sensors(self.sim)
        self.gym.start_access_image_tensors(self.sim)
        pts = self.ptd_cam.get_point_cloud(filter_func=filter_hand_base)
        self.gym.end_access_image_tensors(self.sim)

        if self.cfg.env.ptd_to_robot_base:
            base_link_pos = self.rigid_body_states[:, self.base_link_handle][..., :3]
            base_link_quat = self.rigid_body_states[:, self.base_link_handle][..., 3:7]
            base_link_quat_in_p3d = quat_xyzw_to_wxyz(base_link_quat)
            base_link_rot_mat = p3dtf.quaternion_to_matrix(base_link_quat_in_p3d)
            base_link_pose_inv_rot = base_link_rot_mat.transpose(-2, -1)
            base_link_pose_inv_pos = -base_link_pose_inv_rot @ base_link_pos.unsqueeze(-1)
            base_link_pose_transform_T = torch.eye(4, device=self.device).repeat(base_link_pose_inv_pos.shape[0],
                                                                                 1,
                                                                                 1)
            base_link_pose_transform_T[:, :3, :3] = base_link_pose_inv_rot.view(-1, 3, 3).permute((0, 2, 1))
            base_link_pose_transform_T[:, 3, :3] = base_link_pose_inv_pos.view(-1, 3)
            base_link_pose_transform = p3dtf.Transform3d(matrix=base_link_pose_transform_T)

            pts = base_link_pose_transform.transform_points(points=pts)

        self.hand_link_pos = self.rigid_body_states[:, self.hand_body_handles][:, :, 0:3]
        self.hand_link_quat = self.rigid_body_states[:, self.hand_body_handles][:, :, 3:7]

        goal_pos = self.goal_pos + self.goal_displacement_tensor[None, :]
        goal_quat = self.goal_rot

        quats = torch.cat((self.hand_link_quat, goal_quat[:, None, :]), dim=1)
        trans = torch.cat((self.hand_link_pos, goal_pos[:, None, :]), dim=1)
        quats_in_p3d = quat_xyzw_to_wxyz(quats)
        rot_mat = p3dtf.quaternion_to_matrix(quats_in_p3d)

        if self.cfg.env.ptd_to_robot_base:
            composed_rot = base_link_pose_inv_rot @ rot_mat
            composed_pos = base_link_pose_inv_rot @ trans.unsqueeze(-1) + base_link_pose_inv_pos
            rot_mat = composed_rot
            trans = composed_pos.squeeze(-1)

        self.se3_T_buf[:, :3, :3] = rot_mat.view(-1, 3, 3).permute((0, 2, 1))
        self.se3_T_buf[:, 3, :3] = trans.view(-1, 3)
        transform = p3dtf.Transform3d(matrix=self.se3_T_buf)

        cad_ptd_obs = transform.transform_points(points=self.scene_cad_ptd)
        cad_ptd_obs = cad_ptd_obs.view(self.num_envs, -1, 3)

        ptd_obs = torch.cat((pts, cad_ptd_obs), dim=-2)
        if self.quantization_size is not None:
            ptd_obs = ptd_obs / self.quantization_size
            ptd_obs = ptd_obs.int()
        return ptd_obs.to(self.rl_device)
```
```

### dexenv/envs/rewards.py

```
def compute_reward(reset_buf, reset_goal_buf, progress_buf, successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, actions, fingertip_pos, object_linvel, object_angvel, dof_vel, dof_torque, rot_reward_scale, rot_eps, reach_goal_bonus, fall_dist, fall_penalty, success_tolerance, ftip_reward_scale, energy_scale, dof_vel_thresh, obj_lin_vel_thresh, obj_ang_vel_thresh, action_norm_thresh, penalize_tb_contact, table_cf, tb_cf_scale, clip_energy_reward, energy_upper_bound)
def compute_dclaw_reward(reset_buf, reset_goal_buf, progress_buf, successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, reward_cfg, actions, fingertip_pos, fingertip_vel, object_linvel, object_angvel, dof_vel, dof_torque, table_cf)

```python
def compute_reward(reset_buf, reset_goal_buf, progress_buf,
                   successes, max_episode_length: float,
                   object_pos, object_rot, target_pos, target_rot,
                   actions,
                   fingertip_pos,
                   object_linvel, object_angvel, dof_vel,
                   dof_torque,
                   rot_reward_scale: float, rot_eps: float,
                   reach_goal_bonus: float, fall_dist: float,
                   fall_penalty: float, success_tolerance: float,
                   ftip_reward_scale: float,
                   energy_scale: float, dof_vel_thresh: float,
                   obj_lin_vel_thresh: float, obj_ang_vel_thresh: float, action_norm_thresh: float,
                   penalize_tb_contact: bool, table_cf, tb_cf_scale: float,
                   clip_energy_reward: bool, energy_upper_bound: float,
                   ):
    goal_dist = torch.norm(object_pos - target_pos, p=2, dim=-1)
    num_envs = object_pos.shape[0]

    reward_terms = dict()
    if ftip_reward_scale is not None and ftip_reward_scale < 0:
        ftip_diff = (fingertip_pos.view(num_envs, -1, 3) - object_pos[:, None, :])
        ftip_dist = torch.linalg.norm(ftip_diff, dim=-1).view(num_envs, -1)
        ftip_dist_mean = ftip_dist.mean(dim=-1)
        ftip_reward = ftip_dist_mean * ftip_reward_scale
        reward_terms['ftip_reward'] = ftip_reward

    object_linvel_norm = torch.linalg.norm(object_linvel, dim=-1)
    object_angvel_norm = torch.linalg.norm(object_angvel, dim=-1)

    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))
    abs_rot_dist = torch.abs(rot_dist)

    rot_rew = 1.0 / (abs_rot_dist + rot_eps) * rot_reward_scale
    reward_terms['rot_reward'] = rot_rew
    action_norm = torch.linalg.norm(actions, dim=-1)
    energy_cost = torch.abs(dof_vel * dof_torque).sum(dim=-1)
    if clip_energy_reward:
        energy_cost = torch.clamp(energy_cost, max=energy_upper_bound)
    reward_terms['energy_reward'] = -energy_cost * energy_scale

    if penalize_tb_contact:
        in_contact = torch.abs(table_cf).sum(-1) > 0.2
        reward_terms['tb_contact_reward'] = -in_contact.float() * tb_cf_scale

    dof_vel_norm = torch.linalg.norm(dof_vel, dim=-1)

    goal_reach = (abs_rot_dist <= success_tolerance) & (dof_vel_norm <= dof_vel_thresh) \
                 & (object_linvel_norm <= obj_lin_vel_thresh) & (object_angvel_norm <= obj_ang_vel_thresh)
    if penalize_tb_contact:
        goal_reach = goal_reach & (torch.abs(table_cf).sum(-1) < 0.2)
    goal_reach = goal_reach & (action_norm <= action_norm_thresh)
    goal_resets = torch.where(goal_reach, torch.ones_like(reset_goal_buf), reset_goal_buf)

    fall_envs = goal_dist >= fall_dist
    dones = torch.logical_or(goal_reach, fall_envs)
    resets = torch.where(fall_envs, torch.ones_like(reset_buf), reset_buf)
    successes = successes + goal_resets

    reward = torch.sum(torch.stack(list(reward_terms.values())), dim=0)
    reward = torch.where(goal_reach, reward + reach_goal_bonus, reward)
    reward = torch.where(fall_envs, reward + fall_penalty, reward)
    time_due_envs = progress_buf >= max_episode_length - 1
    resets = torch.where(time_due_envs, torch.ones_like(resets), resets)
    dones = torch.logical_or(dones, time_due_envs)
    return reward, dones.int(), resets, goal_resets, progress_buf, successes, abs_rot_dist, reward_terms, time_due_envs
```

```python
def compute_dclaw_reward(reset_buf, reset_goal_buf, progress_buf,
                         successes, max_episode_length: float,
                         object_pos, object_rot, target_pos, target_rot,
                         reward_cfg, actions,
                         fingertip_pos=None, fingertip_vel=None,
                         object_linvel=None, object_angvel=None, dof_vel=None,
                         dof_torque=None, table_cf=None
                         ):
    rot_reward_scale = reward_cfg.rotRewardScale
    rot_eps = reward_cfg.rotEps
    reach_goal_bonus = reward_cfg.reachGoalBonus
    fall_dist = reward_cfg.fallDistance
    fall_penalty = reward_cfg.fallPenalty
    success_tolerance = reward_cfg.successTolerance
    ftip_reward_scale = reward_cfg.ftipRewardScale
    penalize_tb_contact = reward_cfg.pen_tb_contact
    kwargs = dict(
        reset_buf=reset_buf,
        reset_goal_buf=reset_goal_buf,
        progress_buf=progress_buf,
        successes=successes,
        max_episode_length=max_episode_length,
        object_pos=object_pos,
        object_rot=object_rot,
        target_pos=target_pos,
        target_rot=target_rot,
        actions=actions,
        fingertip_pos=fingertip_pos,
        object_linvel=object_linvel,
        object_angvel=object_angvel,
        dof_vel=dof_vel,
        dof_torque=dof_torque,
        rot_reward_scale=rot_reward_scale,
        rot_eps=rot_eps,
        reach_goal_bonus=reach_goal_bonus,
        fall_dist=fall_dist,
        fall_penalty=fall_penalty,
        success_tolerance=success_tolerance,
        ftip_reward_scale=ftip_reward_scale,
        energy_scale=reward_cfg.energy_scale,
        dof_vel_thresh=reward_cfg.dof_vel_thresh,
        obj_lin_vel_thresh=reward_cfg.obj_lin_vel_thresh,
        obj_ang_vel_thresh=reward_cfg.obj_ang_vel_thresh,
        action_norm_thresh=reward_cfg.action_norm_thresh,
        penalize_tb_contact=penalize_tb_contact,
        table_cf=table_cf if table_cf is not None else torch.ones(1),
        tb_cf_scale=reward_cfg.tb_cf_scale,
        clip_energy_reward=reward_cfg.clip_energy_reward,
        energy_upper_bound=reward_cfg.energy_upper_bound,
    )
    out = compute_reward(**kwargs)
    return out
```
```

### dexenv/models/diag_gaussian_pol/diag_gaussian_policy.py

```
class DiagGaussianPolicy(Module)
    def __init__(self, body_net, action_dim, init_log_std, std_cond_in, tanh_on_dist, in_features, clamp_log_std)
    def forward(self, x, body_x)
```

### dexenv/models/diag_gaussian_pol/rnn_diag_gaussian_policy.py

```
class RNNDiagGaussianPolicy(Module)
    def __init__(self, body_net, action_dim, init_log_std, std_cond_in, tanh_on_dist, in_features, clamp_log_std)
    def forward(self, x, body_x, hidden_state, return_hidden_state)
```

### dexenv/models/sequence/rnn_base.py

```
class RNNBase(Module)
    def __init__(self, body_net, rnn_features, in_features, rnn_layers, act)
    def forward(self, x, hidden_state, done)
    def forward_gru(self, input_features, done, hidden_state)
```

### dexenv/models/sparse_cnn_rnn_models.py

```
class VoxelRNN(RNNBase)
    def __init__(self, cfg, act_dim)
    def forward(self, x, hidden_state, done)
    def convert_to_sparse_tensor(self, coords, color)
    def flat_batch_time(self, x)
    def unflat_batch_time(self, x, b, t)
def get_voxel_rnn_model(cfg, env, act_dim)
```

### dexenv/models/state_model.py

```
class SimpleMLP(Module)
    def __init__(self, in_dim, out_dim, act)
    def forward(self, x)
def get_mlp_critic(ob_size, act)
def get_mlp_actor(ob_size, env, act, init_log_std)
def get_expert_actor(ob_size, action_dim, act, init_log_std)
def get_mlp_models(ob_size, env, act, init_log_std)
```

### dexenv/models/utils.py

```
def get_activation(act)
```

### dexenv/models/value_nets/value_net.py

```
class ValueNet(Module)
    def __init__(self, body_net, in_features)
    def forward(self, x, body_x)
```

### dexenv/models/voxel_impala.py

```
def _calculate_fan_in_and_fan_out(tensor)
def _calculate_correct_fan(tensor, mode)
def kaiming_normal_(tensor, a, mode, nonlinearity, gain)
class ImpalaVoxelConvBlock(Module)
    def __init__(self, in_channels, out_channels, batch_norm, kernel_size, stride)
    def forward(self, x)
class ImpalaVoxelResidualBlockPreAct(Module)
    def __init__(self, num_channels, batch_norm, act)
    def forward(self, x)
class ImpalaVoxelCNN(Module)
    def __init__(self, in_channels, out_channels, batch_norm, channel_groups, act, no_stride, no_pool)
    def forward(self, x, return_before_pool)
    def weight_initialization(self, act)
```

### dexenv/models/voxel_model.py

```
class VoxelModel(Module)
    def __init__(self, embed_dim, out_features, batch_norm, act, channel_groups, in_channels, layer_norm, no_pool)
    def forward(self, scene_voxels)
```

### dexenv/runner/base_runner.py

```
class BasicRunner()
    def __post_init__(self)
    def __call__(self)
    def reset(self, env)
    def reset_record(self)
    def create_traj(self, evaluation)
    def handle_timeout(self, next_ob, done, reward, info, skip_record)
```

### dexenv/runner/nstep_runner.py

```
class NStepRunner(BasicRunner)
    def __init__(self)
    def __call__(self, time_steps, sample, evaluation, return_on_done, render, sleep_time, reset_first, reset_kwargs, action_kwargs, random_action, get_last_val)
```

### dexenv/runner/rnn_runner.py

```
class RNNRunner(BasicRunner)
    def __init__(self)
    def __call__(self, time_steps, sample, evaluation, return_on_done, render, sleep_time, reset_first, reset_kwargs, action_kwargs, get_last_val)
    def reset(self, env)
    def get_hidden_state_shape(self, hidden_state)
    def get_tensor_shape(self, tensor)
```

### dexenv/train/student/rnn.py

```
def main(cfg)
```

### dexenv/train/teacher/demo.py

```
class SimpleMLP(Module)
    def __init__(self, in_dim, out_dim)
    def forward(self, x)
class DiagGaussianPolicy(Module)
    def __init__(self, body_net, action_dim, init_log_std, in_features)
    def forward(self, x)
def get_actor(ob_size, act_dim)
def load_expert(actor, expert_path)
def random(cfg)
def main(cfg)
```

### dexenv/train/teacher/mlp.py

```
def main(cfg)
```

### dexenv/utils/common.py

```
def stat_for_traj_data(traj_data, dones, op)
def check_torch_tensor(data)
def stack_data(data, torch_to_numpy, dim)
def get_module_path(module)
def ask_before_remake_dir(directory)
def flatten_nested_dict(d, parent_key, sep)
def make_dir(directory, ask, delete)
def get_all_subdirs(directory, exclude_patterns, sort)
def get_all_subfiles(directory, exclude_patterns, sort)
def get_all_files_with_suffix(directory, suffix, exclude_patterns, include_patterns, sort)
def get_all_files_with_name(directory, name, exclude_patterns, include_patterns, sort)
def filter_with_exclude_patterns(filenames, exclude_patterns)
def filter_with_include_patterns(filenames, include_patterns)
def set_random_seed(seed)
def chunker_list(seq_list, nchunks)
def module_available(module_path)
def get_env_var(key, default)
def list_to_numpy(data, expand_dims)
def save_to_pickle(data, file_name)
def load_from_pickle(file_name)
def pathlib_file(file_name)
def linear_decay_percent(epoch, total_epochs)
def smooth_value(current_value, past_value, tau)
def get_list_stats(data)
def get_git_infos(path)
def generate_id(length)
def generate_id(length)
def pathlib_file(file_name)
def make_dir(directory, ask, delete)
def set_random_seed(seed)
def restore_hydra_cfg(cfg)
def get_hydra_run_dir(pathlib)
def override_hydra_cfg(cfg, overrides)
def set_print_formatting()
def random_z_orientation()
def list_class_names(dir_path)
def load_class_from_path(cls_name, path)
def chunker_list(seq_list, nchunks)
def resolve_expert_model_path(model_path)
def string_list_to_list(list_in_str)
def process_cfg(cfg)
def plot_ecff(dist)
```

### dexenv/utils/constants.py

```
class StateDim(Enum)
class RandKey(Enum)
```

### dexenv/utils/create_task_env.py

```
def create_task_env(cfg)
```

### dexenv/utils/data.py

```
class StepData()
    def __post_init__(self)
    def _split_dict(self, data, next)
    def get_info_data(self)
    def split_first_dim(self)
class StateActionData()
    def __post_init__(self)
    def _split_dict(self, data)
    def split_first_dim(self)
class InfoData()
class TorchTrajectory()
    def allocate_memory(self, step_data)
    def convert_dict_key(self, parent_key, child_key)
    def _allocate_memory_with_key(self, key, val)
    def __getitem__(self, item)
    def add(self, step_data)
    def _assign_value(self, key, val, cur_id)
    def reset(self)
    def add_extra(self, key, value)
    def obs(self)
    def states(self)
    def actions(self)
    def action_infos(self)
    def next_obs(self)
    def next_states(self)
    def rewards(self)
    def true_dones(self)
    def dones(self)
    def infos(self)
    def total_steps(self)
    def num_envs(self)
    def done_indices(self)
    def episode_steps(self)

```python
def rewards(self):
        rewards = self.data.get('reward', None)
        return rewards[:self.capacity]
```
```

### dexenv/utils/dataset.py

```
class DictDataset(Dataset)
    def __init__(self)
    def __len__(self)
    def __getitem__(self, idx)
def process_data(data)
class TrajDatasetSplitByDone(Dataset)
    def __init__(self, max_steps, pad)
    def __len__(self)
    def __getitem__(self, idx)
    def data(self)
```

### dexenv/utils/gae.py

```
def cal_gae(gamma, lam, rewards, value_estimates, last_value, dones, timeout)
```

### dexenv/utils/hydra_util.py

```
def get_hydra_run_dir(pathlib)
def override_hydra_cfg(cfg, overrides)
```

### dexenv/utils/info_util.py

```
def get_element_from_traj_infos(infos, key, i, j)
def get_element_from_traj_infos_row_ids(infos, key, row_ids)
def torch_to_np(tensor)
def info_has_key(infos, key, single_info)
def aggregate_traj_info(infos, key, single_info)
def add_data_to_info(info, key, data)
def get_key_from_info(info, key, env_id)
```

### dexenv/utils/isaac_utils.py

```
def load_an_object_asset(gym, sim, asset_root, object_urdf, asset_options, vhacd)
def load_a_goal_object_asset(gym, sim, asset_root, object_urdf, asset_options, vhacd)
def get_camera_params(width, height, hov, cuda)
def load_obj_texture(gym, sim, object_urdf)
def apply_prop_samples(prop, og_prop, attr, attr_randomization_params, sample)
```

### dexenv/utils/minkowski_utils.py

```
def batched_coordinates_array(coords, device)
```

### dexenv/utils/os_utils.py

```
"""modified from
https://github.com/lucmos/nn-template/blob/main/src/common/utils.py"""
def get_env(env_name, default)
def load_envs(env_file)
```

### dexenv/utils/pcd_augmentation.py

```
class JitterPoints()
    def __init__(self, sigma, clip)
    def __call__(self, coords, color)
class RandomDropout()
    def __init__(self, dropout_ratio)
    def __call__(self, coords, color)
class ProbCompose()
    def __init__(self, transforms)
    def __call__(self, coords, color)
```

### dexenv/utils/point_cloud_utils.py

```
class PointCloudGenerator()
    def __init__(self, proj_matrix, view_matrix, camera_props, height, width, sample_num, depth_max, device)
    def convert(self, depth_buffer)
    def sample_n(self, pts)
class CameraPointCloud()
    def __init__(self, isc_sim, isc_gym, envs, camera_handles, camera_props, sample_num, filter_func, pt_in_local, depth_max, graphics_device, compute_device)
    def get_point_cloud(self, env_ids, filter_func, sample_num)
    def _proc_pts(self, camera_id, env_id, depth_images, filter_func)
    def sample_n(self, pts, sample_num)
    def get_ptd_cuda(self, env_ids, filter_func)
    def clone_img_tensor(self, img_tensors, env_ids)
```

### dexenv/utils/rand_util.py

```
def add_noise_to_var(tensor, noise_cfg, rng)
def add_noise_to_envs(env_ids, all_env_ptrs, ref_props, handle_dict, prop_name, attr, attr_rand_cfg, param_getters_map, param_setters_map, param_setter_defaults_map, sample)
def add_noise_to_prop(prop, ref_prop, attr, attr_rand_cfg, sample, need_operation)
def process_sample_val(ref_val, sample, attr_rand_cfg)
def get_rand_sample(noise_cfg, shape, rng, scale)
def scale_low_high_bound(low, high, scale)
def get_rand_sample_torch(noise_cfg, shape, device)
def get_bucketed_val(val, attr_randomization_params)
def bucket_val(val, lo, hi, num_buckets)
```

### dexenv/utils/torch_utils.py

```
def random_quaternions(num, dtype, device, order)
def quat_xyzw_to_wxyz(quat_xyzw)
def quat_wxyz_to_xyzw(quat_wxyz)
def torch_to_np(tensor)
def swap_flatten_leading_axes(array)
def unique(x, dim)
def swap_axes(data, axes)
def torch_long(array, device)
def action_entropy(action_dist, log_prob)
def freeze_model(model, eval)
def action_from_dist(action_dist, sample)
def action_log_prob(action, action_dist)
def torch_rand_uniform(lower, upper, shape, device)
def torch_rand_choice(values, size, replace)
def clip_grad(params, max_grad_norm)
def get_grad_norm(model)
def load_state_dict(model, pretrained_dict, exclude_keys)
def load_ckpt_data(wandb_run_id, project_name, pretrain_model, eval)
def parse_ckpt_path(wandb_run_id, project_name, eval)
def reset_hidden_state_at_done(hidden_state, done)
def detach_tensors(tensor)
def load_torch_model(model_file)
def save_model(data, wandb_run, env, is_best, step, eval)
def get_latest_ckpt(path)
def torch_float(array, device)
def move_to(models, device)
def to_torch(x, dtype, device, requires_grad)
```

### dexenv/utils/voxel_utils.py

```
def create_input_batch(batch, device, quantization_size, speed_optimized, quantization_mode)
```

### dexenv/utils/wandb_utils.py

```
def create_artifact_download_path(artifact_name)
def create_artifact_name(run_id, eval)
def create_model_name(eval)
```