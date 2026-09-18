# humanoidbench_2024

source: https://github.com/carlosferrazza/humanoid-bench


commit: cb1189039151c8aadaaa987b442da54383c87fab


## README

# HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

[Paper](https://arxiv.org/abs/2403.10506) [Website](https://sferrazza.cc/humanoidbench_site/)

We present [HumanoidBench](https://sferrazza.cc/humanoidbench_site/), a simulated humanoid robot benchmark consisting of $15$ whole-body manipulation and $12$ locomotion tasks. This repo contains the code for environments and training.

![image](humanoid_bench.jpg)

## Directories
Structure of the repository:
* `data`: Weights of the low-level skill policies
* `dreamerv3`: Training code for dreamerv3
* `humanoid_bench`: Core benchmark code
    * `assets`: Simulation assets
    * `envs`: Environment files
    * `mjx`: MuJoCo MJX training code
* `jaxrl_m`: Training code for SAC
* `ppo`: Training code for PPO
* `tdmpc2`: Training code for TD-MPC2

## Installation
Create a clean conda environment:
```
conda create -n humanoidbench python=3.11
conda activate humanoidbench
```
Then, install the required packages:
```
# Install HumanoidBench
pip install -e .

# jax GPU version
pip install "jax[cuda12]==0.4.28"
# Or, jax CPU version
pip install "jax[cpu]==0.4.28"

# Install jaxrl
pip install -r requirements_jaxrl.txt

# Install dreamer
pip install -r requirements_dreamer.txt

# Install td-mpc2
pip install -r requirements_tdmpc.txt

# Install stable-baselines3 (PPO)
pip install stable-baselines3==2.3.2
```


## Environments

### Main Benchmark Tasks
* `h1hand-walk-v0`
* `h1hand-reach-v0`
* `h1hand-hurdle-v0`
* `h1hand-crawl-v0`
* `h1hand-maze-v0`
* `h1hand-push-v0`
* `h1hand-cabinet-v0`
* `h1strong-highbar_hard-v0`  # Make hands stronger to be able to hang from the high bar
* `h1hand-door-v0`
* `h1hand-truck-v0`
* `h1hand-cube-v0`
* `h1hand-bookshelf_simple-v0`
* `h1hand-bookshelf_hard-v0`
* `h1hand-basketball-v0`
* `h1hand-window-v0`
* `h1hand-spoon-v0`
* `h1hand-kitchen-v0`
* `h1hand-package-v0`
* `h1hand-powerlift-v0`
* `h1hand-room-v0`
* `h1hand-stand-v0`
* `h1hand-run-v0`
* `h1hand-sit_simple-v0`
* `h1hand-sit_hard-v0`
* `h1hand-balance_simple-v0`
* `h1hand-balance_hard-v0`
* `h1hand-stair-v0`
* `h1hand-slide-v0`
* `h1hand-pole-v0`
* `h1hand-insert_normal-v0`
* `h1hand-insert_small-v0`

### Test Environments with Random Actions
```
python -m humanoid_bench.test_env --env h1hand-walk-v0
```

### Test Environments with Hierarchical Policy and Random Actions
```
# Define checkpoints to pre-trained low-level policy and obs normalization
export POLICY_PATH="data/reach_two_hands/torch_model.pt"
export MEAN_PATH="data/reach_two_hands/mean.npy"
export VAR_PATH="data/reach_two_hands/var.npy"

# Test the environment
python -m humanoid_bench.test_env --env h1hand-push-v0 --policy_path ${POLICY_PATH} --mean_path ${MEAN_PATH} --var_path ${VAR_PATH} --policy_type "reach_double_relative"
```

### Test Low-Level Reaching Policy (trained with MJX, testing on classical MuJoCo)
```
# One-hand reaching
python -m humanoid_bench.mjx.mjx_test --with_full_model 

# Two-hand reaching
python -m humanoid_bench.mjx.mjx_test --with_full_model --task=reach_two_hands --folder=./data/reach_two_hands
```

### Change Observations
As a default, the environment returns a privileged state of the environment (e.g., robot state + environment state). To get proprio, visual, and tactile sensing, set `obs_wrapper=True` and accordingly select the required sensors, e.g. `sensors="proprio,image,tactile"`. When using tactile sensing, make sure to use `h1touch` in place of `h1hand`.
Full test instruction:
```
python -m humanoid_bench.test_env --env h1touch-stand-v0 --obs_wrapper True --sensors "proprio,image,tactile"
```

### Other Environments
In addition to the main benchmark tasks listed above, you can run the following environements that feature the robot without hands:
* `h1-walk-v0`
* `h1-reach-v0`
* `h1-hurdle-v0`
* `h1-crawl-v0`
* `h1-maze-v0`
* `h1-push-v0`
* `h1-highbar_simple-v0`
* `h1-door-v0`
* `h1-truck-v0`
* `h1-basketball-v0`
* `h1-package-v0`
* `h1-stand-v0`
* `h1-run-v0`
* `h1-sit_simple-v0`
* `h1-sit_hard-v0`
* `h1-balance_simple-v0`
* `h1-balance_hard-v0`
* `h1-stair-v0`
* `h1-slide-v0`
* `h1-pole-v0`

The robot with low-dimensional hands:
* `h1simplehand-pole-v0`

And the Unitree G1 robot with three-finger hands:
* `g1-walk-v0`
* `g1-reach-v0`
* `g1-hurdle-v0`
* `g1-crawl-v0`
* `g1-maze-v0`
* `g1-push-v0`
* `g1-cabinet-v0`
* `g1-door-v0`
* `g1-truck-v0`
* `g1-cube-v0`
* `g1-bookshelf_simple-v0`
* `g1-bookshelf_hard-v0`
* `g1-basketball-v0`
* `g1-window-v0`
* `g1-spoon-v0`
* `g1-kitchen-v0`
* `g1-package-v0`
* `g1-powerlift-v0`
* `g1-room-v0`
* `g1-stand-v0`
* `g1-run-v0`
* `g1-sit_simple-v0`
* `g1-sit_hard-v0`
* `g1-balance_simple-v0`
* `g1-balance_hard-v0`
* `g1-stair-v0`
* `g1-slide-v0`
* `g1-pole-v0`
* `g1-insert_normal-v0`
* `g1-insert_small-v0`

## Training
```
# Define TASK
export TASK="h1hand-sit_simple-v0"

# Train TD-MPC2
python -m tdmpc2.train disable_wandb=False wandb_entity=[WANDB_ENTITY] exp_name=tdmpc task=humanoid_${TASK} seed=0

# Train DreamerV3
python -m embodied.agents.dreamerv3.train --configs humanoid_benchmark --run.wandb True --run.wandb_entity [WANDB_ENTITY] --method dreamer --logdir logs --task humanoid_${TASK} --seed 0

# Train SAC
python ./jaxrl_m/examples/mujoco/run_mujoco_sac.py --env_name ${TASK} --wandb_entity [WANDB_ENTITY] --seed 0

# Train PPO (not using MJX)
python ./ppo/run_sb3_ppo.py --env_name ${TASK} --wandb_entity [WANDB_ENTITY] --seed 0
```


## Training Hierarchical Policies
```
# Define TASK
export TASK="h1hand-push-v0"

# Define checkpoints to pre-trained low-level policy and obs normalization
export POLICY_PATH="data/reach_one_hand/torch_model.pt"
export MEAN_PATH="data/reach_one_hand/mean.npy"
export VAR_PATH="data/reach_one_hand/var.npy"

# Train TD-MPC2 with pre-trained low-level policy
python -m tdmpc2.train disable_wandb=False wandb_entity=[WANDB_ENTITY] exp_name=tdmpc task=humanoid_${TASK} seed=0 policy_path=${POLICY_PATH} mean_path=${MEAN_PATH} var_path=${VAR_PATH} policy_type="reach_single"

# Train DreamerV3 with pre-trained low-level policy
python -m embodied.agents.dreamerv3.train --configs humanoid_benchmark --run.wandb True --run.wandb_entity [WANDB_ENTITY] --method dreamer_${TASK}_hierarchical --logdir logs --env.humanoid.policy_path ${POLICY_PATH} --env.humanoid.mean_path ${MEAN_PATH} --env.humanoid.var_path ${VAR_PATH} --env.humanoid.policy_type="reach_single" --task humanoid_${TASK} --seed 0
```

## Paper Training Curves

Please find [here](https://github.com/carlosferrazza/humanoid-bench/tree/main/logs) json files including all the training curves, so that comparing with our baselines will not necessarily require re-running them in the future.

The json files follow this key structure: task -> method -> seed_X -> (million_steps or return). As an example to access the return sequence for one seed of the SAC run for the walk task, you can query the json data as `data['walk']['SAC']['seed_0']['return']`.


## Citation
If you find HumanoidBench useful for your research, please cite this work:
```
@article{sferrazza2024humanoidbench,
    title={HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation},
    author={Carmelo Sferrazza and Dun-Ming Huang and Xingyu Lin and Youngwoon Lee and Pieter Abbeel},
    journal={arXiv Preprint arxiv:2403.10506},
    year={2024}
}
```


## References
This codebase contains some files adapted from other sources:
* jaxrl_m: https://github.com/dibyaghosh/jaxrl_m/tree/main
* DreamerV3: https://github.com/danijar/dreamerv3
* TD-MPC2: https://github.com/nicklashansen/tdmpc2
* purejaxrl (JAX-PPO traning): https://github.com/luchris429/purejaxrl/tree/main
* Digit models: https://github.com/adubredu/KinodynamicFabrics.jl/tree/sim
* Unitree H1 models: https://github.com/unitreerobotics/unitree_ros/tree/master
* MuJoCo Menagerie (Unitree H1, Shadow Hands, Robotiq 2F-85 models): https://github.com/google-deepmind/mujoco_menagerie
* Robosuite (some texture files): https://github.com/ARISE-Initiative/robosuite


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
dreamerv3/
  LICENSE
  README.md
  embodied/
    __init__.py
    agents/
    benchmarks/
    core/
    distr/
    envs/
    replay/
    requirements.txt
    run/
    scripts/
    tests/
  setup.py
humanoid_bench/
  __init__.py
  dmc_deps/
    dmc_index.py
    dmc_sizes.py
    dmc_util.py
    dmc_wrapper.py
  env.py
  envs/
    balance.py
    basic_locomotion_envs.py
    basketball.py
    bookshelf.py
    cabinet.py
    cube.py
    door.py
    highbar.py
    insert.py
    kitchen.py
    maze.py
    package.py
    pole.py
    powerlift.py
    push.py
    reach.py
    room.py
    spoon.py
    truck.py
    window.py
  mjx/
    __init__.py
    envs/
    flax_to_torch.py
    mjx_test.py
    ppo_continuous_action.py
    video_utils.py
    visualization_utils.py
    wrappers.py
  robots.py
  tasks.py
  test_env.py
  wrappers.py
humanoid_bench.jpg
jaxrl_m/
  .gitignore
  LICENSE
  README.md
  contributing.md
  examples/
    mujoco/
  jaxrl_m/
    common.py
    dataset.py
    evaluation.py
    networks.py
    typing.py
    wandb.py
  setup.py
ppo/
  run_sb3_ppo.py
requirements_dreamer.txt
requirements_jaxrl.txt
requirements_tdmpc.txt
setup.py
tdmpc2/
  .gitignore
  CONTRIBUTING.md
  LICENSE
  README.md
  setup.py
  tdmpc2/
    __init__.py
    common/
    config.yaml
    envs/
    evaluate.py
    tdmpc2.py
    train.py
    trainer/
test_env_img.png
```

## Config files (2)


### dreamerv3/embodied/agents/dreamerv3/configs.yaml

```yaml
defaults:

  seed: 0
  method: name
  task: dummy_disc
  logdir: /dev/null
  replay_size: 1e6
  eval_dir: ''
  filter: '.*'
  tensorboard_videos: True

  jax:
    platform: gpu
    jit: True
    compute_dtype: float16
    param_dtype: float32
    prealloc: True
    checks: False
    logical_cpus: 0
    debug: False
    policy_devices: [0]
    train_devices: [0]
    sync_every: 10
    profiler: False  # True
    transfer_guard: True
    assert_num_devices: -1
    policy_keys: '/(actor|wm/enc|wm/rssm)/'

  run:
    script: train
    steps: 1e10
    duration: 0
    num_envs: 4
    expl_until: 0
    log_every: 120
    save_every: 900
    eval_every: 1e6
    eval_initial: True
    eval_eps: 1
    eval_samples: 1
    train_ratio: 32.0
    train_fill: 0
    eval_fill: 0
    log_zeros: True
    log_keys_video: [image]
    log_keys_sum: '^$'
    log_keys_avg: '^$'
    log_keys_max: '^$'
    log_video_fps: 20
    log_video_streams: 4
    log_episode_timeout: 60
    wandb: False
    wandb_entity: robot-learning
    wandb_project: humanoid-bench
    from_checkpoint: ''
    actor_addr: 'tcp://localhost:{random}'
    replay_addr: 'ipc:///tmp/replay{random}'
    logger_addr: 'ipc:///tmp/logger{random}'
    actor_batch: 32
    actor_threads: 4
    env_replica: -1
    ipv6: False
    usage: {psutil: True, nvsmi: True, gputil: False, malloc: False, gc: False, gil: False}
    timer: True  # A bit slow but useful.
    driver_parallel: True

  envs: {length: 0, reset: True, restarts: False, discretize: 0}
  wrapper: {length: 0, reset: True, discretize: 0, checks: False}
  env:
    atari: {size: [64, 64], repeat: 4, sticky: True, gray: True, actions: all, lives: unused, noops: 0, pooling: 2, aggregate: max, resize: pillow}
    crafter: {size: [64, 64], logs: False}
    atari100k: {size: [64, 64], repeat: 4, sticky: False, gray: False, actions: needed, lives: unused, noops: 30, resize: pillow}
    dmlab: {size: [64, 64], repeat: 4, episodic: True, use_seed: True}
    minecraft: {size: [64, 64], break_speed: 100.0, logs: False}
    dmc: {size: [64, 64], repeat: 2, camera: -1}
    loconav: {size: [64, 64], repeat: 2, camera: -1}
    humanoid: {obs_key: vector, policy_path: "", mean_path: "", var_path: "", policy_type: "", small_obs: "", is_eval: False, actuation: position, reward_dict: {hand_dist: 0.1, target_dist: 0.1, success: 10, terminate: False}}

  # Agent
  task_behavior: Greedy
  expl_behavior: None
  batch_size: 16
  batch_length: 64

  # World Model
  grad_heads: [decoder, reward, cont]
  rssm_type: rssm
  rssm: {deter: 6144, units: 1024, stoch: 32, classes: 32, act: silu, norm: layer, unimix: 0.01, unroll: False, bottleneck: 2048, winit: normal, fan: avg}
  encoder: {mlp_keys: '.*', cnn_keys: '.*', act: silu, norm: layer, mlp_layers: 5, mlp_units: 1024, cnn: resnet, cnn_depth: 96, cnn_blocks: 0, resize: stride, winit: normal, fan: avg, minres: 4, symlog: True}
  decoder: {mlp_keys: '.*', cnn_keys: '.*', act: silu, norm: layer, mlp_layers: 5, mlp_units: 1024, cnn: resnet, cnn_depth: 96, cnn_blocks: 0, cnn_dist: mse, mlp_dist: symlog_mse, inputs: [deter, stoch], resize: stride, winit: normal, fan: avg, outscale: 1.0, minres: 4, cnn_sigmoid: False}
  reward_head: {layers: 5, units: 1024, act: silu, norm: layer, dist: symexp_twohot, outscale: 0.0, inputs: [deter, stoch], winit: normal, fan: avg, bins: 255}
  cont_head: {layers: 5, units: 1024, act: silu, norm: layer, dist: binary, outscale: 1.0, inputs: [deter, stoch], winit: normal, fan: avg}
  loss_scales: {dec_cnn: 1.0, dec_mlp: 1.0, reward: 1.0, cont: 1.0, dyn: 0.5, rep: 0.1, actor: 1.0, critic: 1.0, slowreg: 1.0}
  rssm_loss: {free: 1.0}
  model_opt: {opt: adam, lr: 1e-4, eps: 1e-8, clip: 1000.0, wd: 0.0, warmup: 0, adaclip: 0.0}

  # Actor Critic
  actor: {layers: 5, units: 1024, act: silu, norm: layer, minstd: 0.1, maxstd: 1.0, outscale: 1.0, unimix: 0.01, inputs: [deter, stoch], winit: normal, fan: avg}
  critic: {layers: 5, units: 1024, act: silu, norm: layer, dist: symexp_twohot, outscale: 0.0, inputs: [deter, stoch], winit: normal, fan: avg, bins: 255}
  actor_opt: {opt: adam, lr: 3e-5, eps: 1e-5, clip: 100.0, wd: 0.0, warmup: 0, adaclip: 0.0}
  critic_opt: {opt: adam, lr: 3e-5, eps: 1e-5, clip: 100.0, wd: 0.0, warmup: 0, adaclip: 0.0}
  reward_scales: {extr: 1.0, disag: 100.0, expl: 100.0, goal: 1.0}
  actor_dist_disc: onehot
  actor_dist_cont: normal
  actor_grad_disc: reinforce
  actor_grad_cont: backprop
  critic_type: vfunction
  imag_horizon: 15
  imag_unroll: False
  imag_cont: mean  # mode
  horizon: 333
  return_lambda: 0.95
  critic_slowreg: logprob
  slow_critic_update: 1
  slow_critic_fraction: 0.02
  slow_critic_target: False
  retnorm: {impl: perc_ema, decay: 0.99, max: 1.0, perclo: 5.0, perchi: 95.0}
  actent: 3e-4
  talk_prior: False

  # Exploration
  expl_rewards: {extr: 1.0, disag: 0.1}
  expl_opt: {opt: adam, lr: 1e-4, eps: 1e-5, clip: 100.0, wd: 0.0, warmup: 0}
  disag_head: {layers: 5, units: 1024, act: silu, norm: layer, dist: mse, outscale: 1.0, inputs: [deter, stoch, action], winit: normal, fan: avg}
  disag_target: [stoch]
  disag_models: 8

  # Director
  director_jointly: True
  train_skill_duration: 8
  env_skill_duration: 8
  goal_enc: {layers: 5, units: 1024, act: silu, norm: layer, dist: onehot, outscale: 1.0, inputs: [goal]}
  goal_dec: {layers: 5, units: 1024, act: silu, norm: layer, dist: mse, outscale: 0.1, inputs: [skill]}
  goal_opt: {opt: adam, lr: 1e-4, eps: 1e-6, clip: 100.0, wd: 1e-2, wd_pattern: 'kernel'}
  goal_kl_scale: 0.1  # 1.0
  goal_kl_free: 1.0
  skill_shape: [8, 8]
  manager_rews: {extr: 1.0, expl: 0.1, goal: 0.0}
  worker_rews: {extr: 0.0, expl: 0.0, goal: 1.0}
  worker_inputs: [deter, stoch, goal]
  worker_goals: [manager]
  worker_report_horizon: 64
  manager_actent: 3e-4
  worker_actent: 3e-4

minecraft:
  task: minecraft_diamond
  run:
    script: train_save
    num_envs: 16
    eval_fill: 1e5
    train_ratio: 16
    log_keys_max: '^log_inventory.*'
  encoder: {mlp_keys: 'inventory|inventory_max|equipped|health|hunger|breath|reward', cnn_keys: 'image'}
  decoder: {mlp_keys: 'inventory|inventory_max|equipped|health|hunger|breath', cnn_keys: 'image'}

dmlab:
  task: dmlab_explore_goal_locations_small
  encoder: {mlp_keys: '$^', cnn_keys: 'image'}
  decoder: {mlp_keys: '$^', cnn_keys: 'image'}
  run:
    num_envs: 8
    train_ratio: 64

atari:
  task: atari_pong
  run:
    steps: 5.5e7
    eval_eps: 10
    num_envs: 8
    train_ratio: 64
  encoder: {mlp_keys: '$^', cnn_keys: 'image'}
  decoder: {mlp_keys: '$^', cnn_keys: 'image'}

atari100k:
  task: atari_pong
  run:
    script: train_eval
    steps: 1.5e5
    num_envs: 1
    eval_every: 1e5
    eval_initial: False
    eval_eps: 100
    train_ratio: 1024
  jax.precision: float32
  rssm.deter: 512
  .*\.cnn_depth: 32
  .*\.layers: 2
  .*\.units$: 512
  actor_eval_sample: True
  encoder: {mlp_keys: '$^', cnn_keys: 'image'}
  decoder: {mlp_keys: '$^', cnn_keys: 'image'}

crafter:
  task: crafter_reward
  run:
    num_envs: 1
    log_keys_max: '^log_achievement_.*'
    log_keys_sum: '^log_reward$'
    log_video_fps: 10
  run.train_ratio: 512
  encoder: {mlp_keys: '$^', cnn_keys: 'image'}
  decoder: {mlp_keys: '$^', cnn_keys: 'image'}

dmc_vision:
  task: dmc_walker_walk
  run.train_ratio: 512
  rssm.deter: 512
  .*\.cnn_depth: 32
  .*\.layers: 2
  .*\.units: 512
  encoder: {mlp_keys: '$^', cnn_keys: 'image'}
  decoder: {mlp_keys: '$^', cnn_keys: 'image'}

dmc_proprio:
  task: dmc_walker_walk
  run.train_ratio: 512
  rssm.deter: 512
  .*\.cnn_depth: 32
  .*\.layers: 2
  .*\.units: 512
  encoder: {mlp_keys: '.*', cnn_keys: '$^'}
  decoder: {mlp_keys: '.*', cnn_keys: '$^'}

bsuite:
  task: bsuite_mnist/0
  run:
    num_envs: 1
    script: train
    train_ratio: 1024  # 128 for cartpole
  rssm.deter: 512
  .*\.cnn_depth: 32
  .*\.layers: 2
  .*\.units: 512

loconav:
  task: loconav_ant_maze_m
    # env.loconav.repeat: 2
  env.loconav.repeat: 1
  run:
    train_ratio: 512
    log_keys_max: '^log_.*'
  encoder: 
```

### tdmpc2/tdmpc2/config.yaml

```yaml
defaults:
    - override hydra/launcher: submitit_local

# environment
task: dog-run
obs: state

# evaluation
checkpoint: ???
eval_episodes: 1
eval_freq: 50000

# training
steps: 10_000_000
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
buffer_size: 3_000_000
exp_name: default
data_dir: ???

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
num_channels: 32
mlp_dim: 512
latent_dim: 512
task_dim: 96
num_q: 5
dropout: 0.01
simnorm_dim: 8

# logging
wandb_project: humanoid-bench
wandb_entity: robot-learning
wandb_silent: false
disable_wandb: true
save_csv: true

# misc
save_video: true
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

# humanoid envs
policy_path: ???
mean_path: ???
var_path: ???
policy_type: ???
small_obs: ???

```

## Python signatures and reward/observation bodies (77 files)


### dreamerv3/embodied/agents/dreamerv3/train.py

```
def main(argv)
def make_agent(config)
def make_logger(config)
def make_replay(config, directory, is_eval, rate_limit)
def make_env(config, index)
def wrap_env(env, config)
```

### dreamerv3/embodied/core/config.py

```
class Config(dict)
    def __init__(self)
    def flat(self)
    def save(self, filename)
    def load(cls, filename)
    def __contains__(self, name)
    def __getattr__(self, name)
    def __getitem__(self, name)
    def __setattr__(self, key, value)
    def __setitem__(self, key, value)
    def __reduce__(self)
    def __str__(self)
    def update(self)
    def _flatten(self, mapping)
    def _nest(self, mapping)
    def _ensure_keys(self, mapping)
    def _ensure_values(self, mapping)
    def _format_value(self, value)
    def _format_type(self, value)
```

### dreamerv3/embodied/envs/atari.py

```
class Atari(Env)
    def __init__(self, name, repeat, size, gray, noops, lives, sticky, actions, length, pooling, aggregate, resize)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _reset(self)
    def _obs(self, reward, is_first, is_last, is_terminal)
```

### dreamerv3/embodied/envs/crafter.py

```
class Crafter(Env)
    def __init__(self, task, size, logs, outdir, seed)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, image, reward, info, is_first, is_last, is_terminal)
    def render(self)
```

### dreamerv3/embodied/envs/dmc.py

```
class DMC(Env)
    def __init__(self, env, repeat, render, size, camera)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def render(self)
```

### dreamerv3/embodied/envs/dmlab.py

```
class DMLab(Env)
    def __init__(self, level, repeat, size, mode, action_set, episodic, seed)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, reward, is_first, is_last)
    def render(self)
    def close(self)
class Cache()
    def __init__(self, cache_dir)
    def get_path(self, key)
    def fetch(self, key, pk3_path)
    def write(self, key, pk3_path)
```

### dreamerv3/embodied/envs/dummy.py

```
class Dummy(Env)
    def __init__(self, task, size, length)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, reward, is_first, is_last, is_terminal)
```

### dreamerv3/embodied/envs/from_dm.py

```
class FromDM(Env)
    def __init__(self, env, obs_key, act_key)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, time_step)
    def _convert(self, space)
```

### dreamerv3/embodied/envs/from_gym.py

```
class FromGym(Env)
    def __init__(self, env, obs_key, act_key)
    def info(self)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, obs, reward, is_first, is_last, is_terminal)
    def render(self)
    def close(self)
    def _flatten(self, nest, prefix)
    def _unflatten(self, flat)
    def _convert(self, space)
```

### dreamerv3/embodied/envs/from_gymnasium.py

```
class FromGymnasium(Env)
    def __init__(self, env, obs_key, act_key, is_eval)
    def info(self)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, obs, reward, is_first, is_last, is_terminal, success, success_subtasks)
    def render(self)
    def close(self)
    def _flatten(self, nest, prefix)
    def _unflatten(self, flat)
    def _convert(self, space)
```

### dreamerv3/embodied/envs/hrlgrid.py

```
class HRLGrid(Env)
    def __init__(self, grid, length)
    def act_space(self)
    def obs_space(self)
    def step(self, action)
    def render(self)
    def _obs(self, reward, is_first, is_last, is_terminal)
```

### dreamerv3/embodied/envs/langroom.py

```
class LangRoom(Env)
    def __init__(self, task, view, length, resolution, vocab_size, seed)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _obs(self, reward, is_first, is_last, is_terminal)
    def _new_words(self)
    def _new_colors(self)
    def render(self)
    def _display(self, lines)
    def _load_textures(self, view)
```

### dreamerv3/embodied/envs/loconav.py

```
class LocoNav(Env)
    def __init__(self, name, repeat, size, camera, again, termination, weaker)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def _make_walker(self, name)
    def _make_arena(self, name)
```

### dreamerv3/embodied/envs/loconav_quadruped.py

```
class Quadruped(Walker)
    def _build(self, name, initializer)
    def initialize_episode(self, physics, random_state)
    def apply_action(self, physics, action, random_state)
    def _build_observables(self)
    def mjcf_model(self)
    def upright_pose(self)
    def actuators(self)
    def root_body(self)
    def bodies(self)
    def mocap_tracking_bodies(self)
    def mocap_joints(self)
    def _foot_bodies(self)
    def end_effectors(self)
    def observable_joints(self)
    def egocentric_camera(self)
    def aliveness(self, physics)
    def ground_contact_geoms(self)
    def prev_action(self)
class QuadrupedObservables(WalkerObservables)
    def actuator_activations(self)
    def root_global_pos(self)
    def torso_global_pos(self)
    def proprioception(self)
```

### dreamerv3/embodied/envs/metaworld.py

```
class MetaWorld(Env)
    def __init__(self, task, mode, repeat, render, size, camera, seed)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
def quat(axis, angle)
def mult(quat1, quat2)
```

### dreamerv3/embodied/envs/minecraft.py

```
class Minecraft(Wrapper)
    def __init__(self, task)
class MinecraftWood(Wrapper)
    def __init__(self)
    def step(self, action)
class MinecraftClimb(Wrapper)
    def __init__(self)
    def step(self, action)
class MinecraftDiamond(Wrapper)
    def __init__(self)
    def step(self, action)
class CollectReward()
    def __init__(self, item, once, repeated)
    def __call__(self, obs, inventory)
class HealthReward()
    def __init__(self, scale)
    def __call__(self, obs, inventory)
```

### dreamerv3/embodied/envs/minecraft_base.py

```
class MinecraftBase(Env)
    def __init__(self, actions, repeat, size, break_speed, gamma, sticky_attack, sticky_jump, pitch_limit, log_inv_keys, logs)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
    def inventory(self)
    def _reset(self)
    def _obs(self, obs)
    def _action(self, action)
    def _insert_defaults(self, actions)
```

### dreamerv3/embodied/envs/minecraft_minerl.py

```
class MineRLEnv(EnvSpec)
    def __init__(self, resolution, break_speed, gamma)
    def create_agent_start(self)
    def create_agent_handlers(self)
    def create_server_world_generators(self)
    def create_server_quit_producers(self)
    def create_server_initial_conditions(self)
    def create_observables(self)
    def create_actionables(self)
    def is_from_folder(self, folder)
    def get_docstring(self)
    def determine_success_from_rewards(self, rewards)
    def create_rewardables(self)
    def create_server_decorators(self)
    def create_mission_handlers(self)
    def create_monitors(self)
class BreakSpeedMultiplier(Handler)
    def __init__(self, multiplier)
    def to_string(self)
    def xml_template(self)
class Gamma(Handler)
    def __init__(self, gamma)
    def to_string(self)
    def xml_template(self)

```python
def determine_success_from_rewards(self, rewards):
        return True
```

```python
def create_rewardables(self):
        return []
```
```

### dreamerv3/embodied/envs/pinpad.py

```
class PinPad(Env)
    def __init__(self, task, length)
    def act_space(self)
    def obs_space(self)
    def step(self, action)
    def render(self)
    def _obs(self, reward, is_first, is_last, is_terminal)
```

### dreamerv3/embodied/envs/robodesk.py

```
class RoboDesk(Env)
    def __init__(self, task, mode, repeat, length, resets)
    def obs_space(self)
    def act_space(self)
    def step(self, action)
```

### dreamerv3/embodied/run/train.py

```
def train(make_agent, make_replay, make_env, make_logger, args)
```

### dreamerv3/embodied/run/train_eval.py

```
def train_eval(make_agent, make_train_replay, make_eval_replay, make_train_env, make_eval_env, make_logger, args)
```

### dreamerv3/embodied/run/train_holdout.py

```
def train_holdout(make_agent, make_train_replay, make_eval_replay, make_env, make_logger, args)
```

### dreamerv3/embodied/tests/run/test_train.py

```
class TestTrain()
    def test_run_loop(self, tmpdir, strategy)
    def _make_agent(self)
    def _make_env(self, index)
    def _make_replay(self, args)
    def _make_logger(self)
    def _make_args(self, logdir)
```

### humanoid_bench/env.py

```
class HumanoidEnv(MujocoEnv, EzPickle)
    def __init__(self, robot, control, task, render_mode, width, height, randomness)
    def step(self, action)
    def reset_model(self)
    def seed(self, seed)
    def render(self)
```

### humanoid_bench/envs/balance.py

```
class BalanceBase(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
class BalanceSimple(BalanceBase)
class BalanceHard(BalanceBase)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof + self.vels,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT + 0.37, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        horizontal_velocity = self.robot.center_of_mass_velocity()[[0, 1]]
        dont_move = rewards.tolerance(horizontal_velocity, margin=2).mean()
        return small_control * stand_reward * dont_move, {
            "small_control": small_control,
            "stand_reward": stand_reward,
            "dont_move": dont_move,
            "standing": standing,
            "upright": upright,
        }
```
```

### humanoid_bench/envs/basic_locomotion_envs.py

```
class Walk(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
class Stand(Walk)
class Run(Walk)
class Crawl(Walk)
    def get_reward(self)
    def get_terminated(self)
class ClimbingUpwards(Walk)
    def get_reward(self)
    def get_terminated(self)
class Stair(ClimbingUpwards)
class Slide(ClimbingUpwards)
class Hurdle(Walk)
    def get_reward(self)
class Sit(Task)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
    def euler_to_quat(angles)
class SitHard(Sit)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf, high=np.inf, shape=(self.robot.dof * 2 - 1,), dtype=np.float64
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5
        if self._move_speed == 0:
            horizontal_velocity = self.robot.center_of_mass_velocity()[[0, 1]]
            dont_move = rewards.tolerance(horizontal_velocity, margin=2).mean()
            return small_control * stand_reward * dont_move, {
                "small_control": small_control,
                "stand_reward": stand_reward,
                "dont_move": dont_move,
                "standing": standing,
                "upright": upright,
            }
        else:
            com_velocity = self.robot.center_of_mass_velocity()[0]
            move = rewards.tolerance(
                com_velocity,
                bounds=(self._move_speed, float("inf")),
                margin=self._move_speed,
                value_at_margin=0,
                sigmoid="linear",
            )
            move = (5 * move + 1) / 6
            reward = small_control * stand_reward * move
            return reward, {
                "stand_reward": stand_reward,
                "small_control": small_control,
                "move": move,
                "standing": standing,
                "upright": upright,
            }
```

```python
def get_reward(self):
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        com_velocity = self.robot.center_of_mass_velocity()[0]
        move = rewards.tolerance(
            com_velocity,
            bounds=(1, float("inf")),
            margin=1,
            value_at_margin=0,
            sigmoid="linear",
        )
        move = (5 * move + 1) / 6

        crawling_head = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_CRAWL_HEIGHT - 0.2, _CRAWL_HEIGHT + 0.2),
            margin=1,
        )

        crawling = rewards.tolerance(
            self._env.named.data.site_xpos["imu", "z"],
            bounds=(_CRAWL_HEIGHT - 0.2, _CRAWL_HEIGHT + 0.2),
            margin=1,
        )

        reward_xquat = rewards.tolerance(
            np.linalg.norm(
                self._env.data.body("pelvis").xquat - np.array([0.75, 0, 0.65, 0])
            ),
            margin=1,
        )

        in_tunnel = rewards.tolerance(
            self._env.named.data.site_xpos["imu", "y"],
            bounds=(-1, 1),
            margin=0,
        )

        reward = (
            0.1 * small_control
            + 0.25 * min(crawling, crawling_head)
            + 0.4 * move
            + 0.25 * reward_xquat
        ) * in_tunnel
        return reward, {
            "crawling": crawling,
            "crawling_head": crawling_head,
            "small_control": small_control,
            "move": move,
            "in_tunnel": in_tunnel,
        }
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height() - self.robot.left_foot_height(),
            bounds=(1.2, float("inf")),
            margin=0.45,
        ) * rewards.tolerance(
            self.robot.head_height() - self.robot.right_foot_height(),
            bounds=(1.2, float("inf")),
            margin=0.45,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.5, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        com_velocity = self.robot.center_of_mass_velocity()[0]
        move = rewards.tolerance(
            com_velocity,
            bounds=(_WALK_SPEED, float("inf")),
            margin=_WALK_SPEED,
            value_at_margin=0,
            sigmoid="linear",
        )
        move = (5 * move + 1) / 6
        return stand_reward * small_control * move, {  # small_control *
            "stand_reward": stand_reward,
            "small_control": small_control,
            "move": move,
            "standing": standing,
            "upright": upright,
        }
```

```python
def get_reward(self):
        self.wall_collision_ids = [
            self._env.named.data.geom_xpos.axes.row.names.index(wall_name)
            for wall_name in [
                "left_barrier_collision",
                "right_barrier_collision",
                "behind_barrier_collision",
            ]
        ]

        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.8, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5
        com_velocity = self.robot.center_of_mass_velocity()[0]
        move = rewards.tolerance(
            com_velocity,
            bounds=(self._move_speed, float("inf")),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
        move = (5 * move + 1) / 6
        wall_collision_discount = 1

        for pair in self._env.data.contact.geom:
            if any(
                [
                    wall_collision_id in pair
                    for wall_collision_id in self.wall_collision_ids
                ]
            ):  # for no hand. if for hand, > 155
                wall_collision_discount = 0.1
                # print(pair)
                break

        reward = small_control * stand_reward * move * wall_collision_discount

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "move": move,
            "standing": standing,
            "upright": upright,
            "wall_collision_discount": wall_collision_discount,
        }
```

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof + self.vels,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        sitting = rewards.tolerance(
            self._env.data.qpos[2], bounds=(0.68, 0.72), margin=0.2
        )
        chair_location = self._env.named.data.xpos["chair"]
        on_chair = rewards.tolerance(
            self._env.data.qpos[0] - chair_location[0], bounds=(-0.19, 0.19), margin=0.2
        ) * rewards.tolerance(self._env.data.qpos[1] - chair_location[1], margin=0.1)
        sitting_posture = rewards.tolerance(
            self.robot.head_height() - self._env.named.data.site_xpos["imu", "z"],
            bounds=(0.35, 0.45),
            margin=0.3,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.95, float("inf")),
            sigmoid="linear",
            margin=0.9,
            value_at_margin=0,
        )
        sit_reward = (0.5 * sitting + 0.5 * on_chair) * upright * sitting_posture
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        horizontal_velocity = self.robot.center_of_mass_velocity()[[0, 1]]
        dont_move = rewards.tolerance(horizontal_velocity, margin=2).mean()
        return small_control * sit_reward * dont_move, {
            "small_control": small_control,
            "sit_reward": sit_reward,
            "dont_move": dont_move,
            "sitting": sitting,
            "upright": upright,
            "sitting_posture": sitting_posture,
        }
```
```

### humanoid_bench/envs/basketball.py

```
class Basketball(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=((self.robot.dof * 2 - 1) + self.dof * 2 - 1,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        self.ball_collision_id = self._env.named.data.geom_xpos.axes.row.names.index(
            "basketball_collision"
        )

        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        basketball_pos = self._env.named.data.xpos["basketball"]
        left_hand_distance = (
            self._env.named.data.site_xpos["left_hand"] - basketball_pos
        )
        right_hand_distance = (
            self._env.named.data.site_xpos["right_hand"] - basketball_pos
        )
        reward_hand_proximity = rewards.tolerance(
            max(
                [
                    np.linalg.norm(left_hand_distance),
                    np.linalg.norm(right_hand_distance),
                ]
            ),
            bounds=(0, 0.2),
            margin=1,
        )
        reward_ball_success = 0
        ball_hoop_distance = np.linalg.norm(
            basketball_pos - self._env.named.data.site_xpos["hoop_center"]
        )
        reward_ball_success = rewards.tolerance(
            ball_hoop_distance,
            margin=7,
            sigmoid="linear",
        )

        if self.stage == "catch":
            for pair in self._env.data.contact.geom:
                if self.ball_collision_id in pair:
                    self.stage = "throw"
                    break
        if self.stage == "throw":
            reward = (
                0.15 * (stand_reward * small_control)
                + 0.05 * reward_hand_proximity
                + 0.8 * reward_ball_success
            )
        elif self.stage == "catch":
            reward = 0.5 * (stand_reward * small_control) + 0.5 * reward_hand_proximity

        if ball_hoop_distance < 0.05:
            reward += 1000

        return reward, {
            "reward_hand_proximity": reward_hand_proximity,
            "reward_ball_success": reward_ball_success,
            "stand_reward": stand_reward,
            "small_control": small_control,
            "success_subtasks": 1 if self.stage == "throw" else 0,
            "success": ball_hoop_distance < 0.05,
        }
```
```

### humanoid_bench/envs/bookshelf.py

```
class BookshelfBase(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)
class BookshelfSimple(BookshelfBase)
class BookshelfHard(BookshelfBase)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 12 + 1,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        curr_reach_obj_pos = self._env.named.data.xpos[
            self.bookshelf_objects[self.task_index]
        ]
        curr_placement_goal = self.placement_goals[self.task_index]
        obj_goal_dist = np.linalg.norm(curr_reach_obj_pos - curr_placement_goal)

        reward_proximity = rewards.tolerance(
            obj_goal_dist, bounds=(0, 0.15), margin=1, sigmoid="linear"
        )
        left_hand_distance = (
            self._env.named.data.site_xpos["left_hand"] - curr_reach_obj_pos
        )
        righ_hand_distance = (
            self._env.named.data.site_xpos["right_hand"] - curr_reach_obj_pos
        )
        reward_hand_proximity = np.exp(
            -min(
                [np.linalg.norm(left_hand_distance), np.linalg.norm(righ_hand_distance)]
            )
        )

        reward = (
            0.2 * (stand_reward * small_control)
            + 0.4 * reward_proximity
            + 0.4 * reward_hand_proximity
        )
        if obj_goal_dist < 0.15:
            self.task_index += 1
            reward += 100 * self.task_index

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "reward_proximity": reward_proximity,
            "reward_hand_proximity": reward_hand_proximity,
            "obj_goal_dist": obj_goal_dist,
            "success_subtasks": self.task_index,
            "success": self.task_index == 5,
        }
```
```

### humanoid_bench/envs/cabinet.py

```
class Cabinet(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_reward_subtask_one(self)
    def get_reward_subtask_two(self)
    def get_reward_subtask_three(self)
    def get_reward_subtask_four(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 1 - 3,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5
        stabilization_reward = stand_reward * small_control

        subtask_get_reward = [
            self.get_reward_subtask_one,
            self.get_reward_subtask_two,
            self.get_reward_subtask_three,
            self.get_reward_subtask_four,
            lambda: (1000, {}, False),
        ]

        reward, reward_info, subtask_complete = subtask_get_reward[
            self.current_subtask - 1
        ]()
        if self.current_subtask < 5:
            reward = 0.2 * stabilization_reward + 0.8 * reward

        if subtask_complete:
            print("Completed subtask", self.current_subtask)
            reward += 100 * (self.current_subtask)
            self.current_subtask += 1

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "success_subtasks": self.current_subtask
            - 1,  # The first subtask is not automatically completed.
            "success": self.current_subtask == 5,
            **reward_info,
        }
```

```python
def get_reward_subtask_one(self):
        pulling_cabinet_joint_pos = self._env.data.qpos[-(4 * 7) - 2]
        door_openness_reward = abs(pulling_cabinet_joint_pos / 0.4)
        subtask_complete = door_openness_reward > 0.95
        return (
            door_openness_reward,
            {
                "door_openness_reward": door_openness_reward,
                "subtask_complete": subtask_complete,
            },
            subtask_complete,
        )
```

```python
def get_reward_subtask_two(self):
        drawer_joint_pos = self._env.data.qpos[-(4 * 7) - 5]
        door_openness_reward = abs(drawer_joint_pos / 0.45)
        subtask_complete = door_openness_reward > 0.95
        return (
            door_openness_reward,
            {
                "door_openness_reward": door_openness_reward,
                "subtask_complete": subtask_complete,
            },
            subtask_complete,
        )
```

```python
def get_reward_subtask_three(self):
        drawer_cube_pos = self._env.named.data.xpos["drawer_cube"]
        normal_cabinet_left_joint_pos = self._env.data.qpos[-(4 * 7) - 4]
        normal_cabinet_right_joint_pos = self._env.data.qpos[-(4 * 7) - 3]
        left_door_openness_reward = min(1, abs(normal_cabinet_left_joint_pos))
        right_door_openness_reward = min(1, abs(normal_cabinet_right_joint_pos))
        door_openness_reward = max(
            left_door_openness_reward, right_door_openness_reward
        )  # Any open door is sufficient

        cube_proximity_horizontal = (
            rewards.tolerance(
                drawer_cube_pos[0] - 0.9,
                bounds=(-0.3, 0.3),
                margin=0.3,
                sigmoid="linear",
            )
            + rewards.tolerance(
                drawer_cube_pos[1], bounds=(-0.6, 0.6), margin=0.3, sigmoid="linear"
            )
        ) / 2
        cube_proximity_vertical = rewards.tolerance(
            drawer_cube_pos[2] - 0.94,
            bounds=(-0.15, 0.15),
            margin=0.3,
            sigmoid="linear",
        )

        in_cabinet_x = 0.9 - 0.3 <= drawer_cube_pos[0] <= 0.9 + 0.3
        in_cabinet_y = 0 - 0.6 <= drawer_cube_pos[1] <= 0 + 0.6
        in_cabinet_z = 0.94 - 0.15 <= drawer_cube_pos[2] <= 0.94 + 0.15
        task_completed = in_cabinet_x and in_cabinet_y and in_cabinet_z

        drawer_cube_proximity_reward = (
            0.3 * cube_proximity_horizontal + 0.7 * cube_proximity_vertical
        )
        reward = 0.5 * (drawer_cube_proximity_reward) + 0.5 * door_openness_reward
        return (
            reward,
            {
                "door_openness_reward": door_openness_reward,
                "drawer_cube_proximity_reward": drawer_cube_proximity_reward,
                "subtask_complete": task_completed,
            },
            task_completed,
        )
```

```python
def get_reward_subtask_four(self):
        pullup_drawer_cube_pos = self._env.named.data.xpos["lateral_cabinet_cube"]
        pullup_drawer_joint_pos = self._env.data.qpos[-(4 * 7) - 1]
        door_openness_reward = min(1, abs(pullup_drawer_joint_pos))

        normal_cabinet_left_joint_pos = self._env.data.qpos[-(4 * 7) - 4]
        normal_cabinet_right_joint_pos = self._env.data.qpos[-(4 * 7) - 3]
        left_door_openness_reward = min(1, abs(normal_cabinet_left_joint_pos))
        right_door_openness_reward = min(1, abs(normal_cabinet_right_joint_pos))
        secondary_door_openness_reward = max(
            left_door_openness_reward, right_door_openness_reward
        )

        cube_proximity_horizontal = rewards.tolerance(
            pullup_drawer_cube_pos[0] - 0.9,
            bounds=(-0.3, 0.3),
            margin=0.3,
            sigmoid="linear",
        ) + rewards.tolerance(
            pullup_drawer_cube_pos[1], bounds=(-0.6, 0.6), margin=0.3, sigmoid="linear"
        )
        cube_proximity_vertical = rewards.tolerance(
            pullup_drawer_cube_pos[2] - 1.54,
            bounds=(-0.15, 0.15),
            margin=0.3,
            sigmoid="linear",
        )

        in_cabinet_x = 0.9 - 0.3 <= pullup_drawer_cube_pos[0] <= 0.9 + 0.3
        in_cabinet_y = 0 - 0.6 <= pullup_drawer_cube_pos[1] <= 0 + 0.6
        in_cabinet_z = 1.54 - 0.15 <= pullup_drawer_cube_pos[2] <= 1.54 + 0.15
        task_completed = in_cabinet_x and in_cabinet_y and in_cabinet_z

        drawer_cube_proximity_reward = (
            0.3 * cube_proximity_horizontal / 2 + 0.7 * cube_proximity_vertical
        )
        reward = 0.5 * (drawer_cube_proximity_reward) + 0.5 * door_openness_reward

        return (
            reward,
            {
                "door_openness_reward": door_openness_reward,
                "secondary_door_openness_reward": secondary_door_openness_reward,
                "drawer_cube_proximity_reward": drawer_cube_proximity_reward,
                "subtask_complete": task_completed,
            },
            task_completed,
        )
```
```

### humanoid_bench/envs/cube.py

```
class Cube(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)
    def euler_to_quat(angles)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 2 + 4,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        horizontal_velocity = self.robot.center_of_mass_velocity()[[0, 1]]
        dont_move = rewards.tolerance(horizontal_velocity, margin=2).mean()

        left_cube_orientation = self._env.data.body("left_cube_to_rotate").xquat
        right_cube_orientation = self._env.data.body("right_cube_to_rotate").xquat
        target_cube_orientation = self._env.data.body("target_cube").xquat

        left_orientation_alignment_reward = rewards.tolerance(
            np.linalg.norm(left_cube_orientation - target_cube_orientation), margin=0.3
        )
        right_orientation_alignment_reward = rewards.tolerance(
            np.linalg.norm(right_cube_orientation - target_cube_orientation), margin=0.3
        )
        orientation_alignment_reward = (
            left_orientation_alignment_reward + right_orientation_alignment_reward
        ) / 2

        left_hand_cube_distance = np.linalg.norm(
            self._env.named.data.site_xpos["left_hand"]
            - self._env.named.data.xpos["left_cube_to_rotate"]
        )
        right_hand_cube_distance = np.linalg.norm(
            self._env.named.data.site_xpos["right_hand"]
            - self._env.named.data.xpos["right_cube_to_rotate"]
        )
        left_hand_cube_proximity = rewards.tolerance(
            left_hand_cube_distance, bounds=(0, 0.1), margin=0.5
        )
        right_hand_cube_proximity = rewards.tolerance(
            right_hand_cube_distance, bounds=(0, 0.1), margin=0.5
        )

        cube_closeness_reward = (
            left_hand_cube_proximity + right_hand_cube_proximity
        ) / 2

        reward = (
            0.2 * (small_control * stand_reward * dont_move)
            + 0.5 * orientation_alignment_reward
            + 0.3 * cube_closeness_reward
        )

        return reward, {
            "small_control": small_control,
            "stand_reward": stand_reward,
            "dont_move": dont_move,
            "standing": standing,
            "upright": upright,
            "orientation_alignment_reward": orientation_alignment_reward,
            "cube_closeness_reward": cube_closeness_reward,
        }
```
```

### humanoid_bench/envs/door.py

```
class Door(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=0.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        door_openness_reward = min(
            1, (self._env.data.qpos[-2] / 1) * abs(self._env.data.qpos[-2] / 1)
        )
        door_hatch_openness_reward = rewards.tolerance(
            self._env.data.qpos[-1], bounds=(0.75, 2), margin=0.75, sigmoid="linear"
        )

        left_hand_hatch_closeness = np.linalg.norm(
            self._env.data.body("door_hatch").xpos
            - self._env.named.data.site_xpos["left_hand"]
        )
        right_hand_hatch_closeness = np.linalg.norm(
            self._env.data.body("door_hatch").xpos
            - self._env.named.data.site_xpos["right_hand"]
        )
        hand_hatch_proximity_reward = rewards.tolerance(
            min(right_hand_hatch_closeness, left_hand_hatch_closeness),
            bounds=(0, 0.25),
            margin=1,
            sigmoid="linear",
        )

        passage_reward = rewards.tolerance(
            self._env.named.data.site_xpos["imu", "x"],
            bounds=(1.2, float("inf")),
            margin=1,
            value_at_margin=0,
            sigmoid="linear",
        )

        reward = (
            0.1 * stand_reward * small_control
            + 0.45 * door_openness_reward
            + 0.05 * door_hatch_openness_reward
            + 0.05 * hand_hatch_proximity_reward
            + 0.35 * passage_reward
        )

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "door_openness_reward": door_openness_reward,
            "door_hatch_openness_reward": door_hatch_openness_reward,
            "hand_hatch_proximity_reward": hand_hatch_proximity_reward,
            "passage_reward": passage_reward,
        }
```
```

### humanoid_bench/envs/highbar.py

```
class HighBarBase(Task)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)
class HighBarSimple(HighBarBase)
class HighBarHard(HighBarBase)

```python
def observation_space(self):
        return Box(
            low=-np.inf, high=np.inf, shape=(self.robot.dof * 2 - 1,), dtype=np.float64
        )
```

```python
def get_reward(self):
        upright_reward = rewards.tolerance(
            -self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )

        feet_reward = rewards.tolerance(
            (self.robot.left_foot_height() + self.robot.right_foot_height()) / 2,
            bounds=(4.8, float("inf")),
            sigmoid="linear",
            margin=2.0,
            value_at_margin=0,
        )
        feet_reward = (1 + feet_reward) / 2

        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        reward = upright_reward * feet_reward * small_control

        return reward, {
            "upright_reward": upright_reward,
            "feet_reward": feet_reward,
            "small_control": small_control,
        }
```
```

### humanoid_bench/envs/insert.py

```
class Insert(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 3,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        cube_targets = [
            rewards.tolerance(
                np.linalg.norm(
                    self._env.named.data.site_xpos[f"block_peg_{ch}"]
                    - self._env.named.data.site_xpos[f"peg_{ch}"]
                ),
                margin=0.5,
                sigmoid="linear",
            )
            for ch in ["a", "b"]
        ]
        cube_target_reward = np.mean(cube_targets)
        peg_heights = [
            rewards.tolerance(
                self._env.named.data.site_xpos[f"peg_{ch}", "z"] - 1.1,
                margin=0.15,
                sigmoid="linear",
            )
            for ch in ["a", "b"]
        ]
        peg_height_reward = np.mean(peg_heights)

        left_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["left_hand"]
            - self._env.named.data.site_xpos["peg_a"]
        )
        right_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["right_hand"]
            - self._env.named.data.site_xpos["peg_b"]
        )
        hand_tool_proximity_reward = rewards.tolerance(
            min(left_hand_tool_distance, right_hand_tool_distance),
            bounds=(0, 0.2),
            margin=0.5,
        )

        reward = (0.5 * (small_control * stand_reward) + 0.5 * cube_target_reward) * (
            0.5 * peg_height_reward + 0.5 * hand_tool_proximity_reward
        )

        return reward, {
            "small_control": small_control,
            "stand_reward": stand_reward,
            "cube_target_reward": cube_target_reward,
            "hand_tool_proximity_reward": hand_tool_proximity_reward,
            "peg_height_reward": peg_height_reward,
        }
```
```

### humanoid_bench/envs/kitchen.py

```
class Kitchen(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def _get_task_goal(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof + self.dof,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        reward_dict = {}
        next_obj_obs = self.obs_dict["obj_qp"]
        completions = []
        all_completed_so_far = True
        for i, element in enumerate(self.tasks_to_complete):
            element_idx = OBS_ELEMENT_INDICES[element]
            distance = np.linalg.norm(
                next_obj_obs[..., element_idx] - self.goal[element_idx]
            )
            complete = distance < BONUS_THRESH
            if complete and (all_completed_so_far or not self.ENFORCE_TASK_ORDER):
                completions.append(element)
            all_completed_so_far = all_completed_so_far and complete
        if self.REMOVE_TASKS_WHEN_COMPLETE:
            for element in completions:
                del self.tasks_to_complete[element]
            # [self.tasks_to_complete.remove(element) for element in completions]
        bonus = float(len(completions))

        reward_dict["success_subtasks"] = len(self.TASK_ELEMENTS) - len(
            self.tasks_to_complete
        )
        reward_dict["success"] = 0
        if len(self.tasks_to_complete) == 0:
            reward_dict["success"] = 1

        return bonus, reward_dict
```
```

### humanoid_bench/envs/maze.py

```
class MazeBase(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def update_move_direction(self)
    def get_reward(self)
    def get_terminated(self)
class Maze(MazeBase)
    def __init__(self)
    def update_move_direction(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf, high=np.inf, shape=(self.robot.dof * 2 - 1,), dtype=np.float64
        )
```

```python
def get_reward(self):
        self.begining_wall_id = self._env.named.data.geom_xpos.axes.row.names.index(
            "block_collision_00"
        )

        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        wall_collision_discount = 1

        for pair in self._env.data.contact.geom:
            if pair[0] >= self.begining_wall_id or pair[1] >= self.begining_wall_id:
                wall_collision_discount = 0.1
                # print(pair)
                break

        stage_convert_reward = self.update_move_direction()

        move = rewards.tolerance(
            self.robot.center_of_mass_velocity()[0]
            - self.move_direction[0] * _MOVE_SPEED,
            margin=1,
            value_at_margin=0,
            sigmoid="linear",
        ) * rewards.tolerance(
            self.robot.center_of_mass_velocity()[1]
            - self.move_direction[1] * _MOVE_SPEED,
            margin=1,
            value_at_margin=0,
            sigmoid="linear",
        )

        if self.maze_stage == len(self.checkpoints) - 1:
            move = 1

        move = (5 * move + 1) / 6

        checkpoint_proximity = np.linalg.norm(
            self.checkpoints[self.maze_stage][:2]
            - self._env.named.data.site_xpos["imu"][:2]
        )

        checkpoint_proximity_reward = rewards.tolerance(checkpoint_proximity, margin=1)

        reward = (
            0.2 * (stand_reward * small_control)
            + 0.4 * move
            + 0.4 * checkpoint_proximity_reward
        ) * wall_collision_discount + stage_convert_reward

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "move": move,
            "wall_collision_discount": wall_collision_discount,
            "stage_convert_reward": stage_convert_reward,
            "checkpoint_proximity_reward": checkpoint_proximity_reward,
            "success_subtasks": self.maze_stage,
        }
```
```

### humanoid_bench/envs/package.py

```
class Package(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 1 + 9,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.8, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        package_destination = self._env.named.data.site_xpos["destination_loc"]
        package_location = self._env.named.data.qpos["free_package"][:3]

        dist_package_destination = np.linalg.norm(
            package_location - package_destination
        )
        dist_hand_package_right = np.linalg.norm(
            self._env.named.data.site_xpos["right_hand"] - package_location
        )
        dist_hand_package_left = np.linalg.norm(
            self._env.named.data.site_xpos["left_hand"] - package_location
        )
        package_height = np.min((package_location[2], 1))

        reward_success = dist_package_destination < 0.1

        reward = (
            stand_reward * small_control
            - 3 * dist_package_destination * 1
            - (dist_hand_package_left + dist_hand_package_right) * 0.1
            + package_height
            + reward_success * 1000
        )

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "dist_package_destination": dist_package_destination,
            "dist_hand_package_right": dist_hand_package_right,
            "dist_hand_package_left": dist_hand_package_left,
            "package_height": package_height,
            "success": reward_success > 0,
        }
```
```

### humanoid_bench/envs/pole.py

```
class Pole(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf, high=np.inf, shape=(self.robot.dof * 2 - 1,), dtype=np.float64
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        com_velocity = self.robot.center_of_mass_velocity()[0]
        move = rewards.tolerance(
            com_velocity,
            bounds=(self._move_speed, float("inf")),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
        move = (5 * move + 1) / 6

        all_geoms_id = self._env.named.data.geom_xpos.axes.row.names

        collision_discount = 1
        for pair in self._env.data.contact.geom:
            if (
                any(["pole_r" in all_geoms_id[p_val] for p_val in pair])
                and 0 not in pair
            ):  #
                collision_discount = 0.1
                break

        reward = (
            0.5 * (small_control * stand_reward) + 0.5 * move
        ) * collision_discount
        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "move": move,
            "standing": standing,
            "upright": upright,
            "collision_discount": collision_discount,
        }
```
```

### humanoid_bench/envs/powerlift.py

```
class Powerlift(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 1,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 3,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.8, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        dumbbell_height = self._env.named.data.xpos["dumbbell", "z"]
        reward_dumbbell_lifted = rewards.tolerance(
            dumbbell_height, bounds=(1.9, 2.1), margin=2
        )

        reward = 0.2 * (small_control * stand_reward) + 0.8 * reward_dumbbell_lifted
        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "reward_dumbbell_lifted": reward_dumbbell_lifted,
            "standing": standing,
            "upright": upright,
        }
```
```

### humanoid_bench/envs/push.py

```
class Push(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def goal_dist(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)
    def render(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + 12,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        goal_dist = self.goal_dist()
        penalty_dist = self.reward_dict["target_dist"] * goal_dist
        reward_success = self.reward_dict["success"] if goal_dist < 0.05 else 0

        left_hand = self.robot.left_hand_position()
        # box = self._env.data.qpos.flat.copy()[-7:-4]
        box = self._env.named.data.qpos["free_object"][:3]

        hand_dist = np.sqrt(np.square(left_hand - box).sum())
        hand_penalty = self.reward_dict["hand_dist"] * hand_dist

        reward = -hand_penalty - penalty_dist + reward_success
        info = {
            "target_dist": goal_dist,
            "hand_dist": hand_dist,
            "reward_success": reward_success,
            "success": reward_success > 0,
        }
        return reward, info
```
```

### humanoid_bench/envs/reach.py

```
class Reach(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def reset_model(self)
    def render(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=((self.robot.dof * 2 - 1) + 6,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        hand_dist = np.sqrt(
            np.square(self.robot.left_hand_position() - self.goal).sum()
        )

        healthy_reward = self._env.data.xmat[1, -1] * 5.0
        motion_penalty = np.square(self._env.data.qvel[: self.robot.dof - 1]).sum()
        reward_close = 5 if hand_dist < 1 else 0
        reward_success = 10 if hand_dist < 0.05 else 0
        reward = (
            healthy_reward - 0.0001 * motion_penalty + reward_close + reward_success
        )

        info = {
            "hand_dist": hand_dist,
            "healthy_reward": healthy_reward,
            "motion_penalty": motion_penalty,
            "reward_close": reward_close,
            "reward_success": reward_success,
        }
        return reward, info
```
```

### humanoid_bench/envs/room.py

```
class Room(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 6,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        room_object_positions = np.vstack(
            [
                self._env.named.data.xpos[obj_name]
                for obj_name in [
                    "chair",
                    "trophy",
                    "headphone",
                    "package_a",
                    "package_b",
                    "snow_globe",
                ]
            ]
        )
        room_object_entropies = np.array(
            [np.var(room_object_positions[:, col_id]) for col_id in range(2)]
        )

        room_object_organized = rewards.tolerance(
            np.max(room_object_entropies),
            margin=3,
        )

        reward = 0.2 * (small_control * stand_reward) + 0.8 * room_object_organized
        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "standing": standing,
            "upright": upright,
            "room_object_organized": room_object_organized,
        }
```
```

### humanoid_bench/envs/spoon.py

```
class Spoon(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 1 + 3,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        left_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["left_hand"]
            - self._env.named.data.geom_xpos["spoon_handle"]
        )
        right_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["right_hand"]
            - self._env.named.data.geom_xpos["spoon_handle"]
        )
        hand_tool_proximity_reward = rewards.tolerance(
            min(left_hand_tool_distance, right_hand_tool_distance),
            bounds=(0, 0.2),
            margin=0.5,
        )

        current_spin_angle = self.step_counter * (2 * np.pi / 40)
        spoon_target_pos = np.array([0.75, -0.1, 0.95]) + np.array(
            [np.cos(current_spin_angle) * 0.06, np.sin(current_spin_angle) * 0.06, 0]
        )
        self._env.named.data.site_xpos["goal"] = spoon_target_pos
        # spoon_velocity = self._env.named.data.sensordata["spoon_gyro"][2]
        spoon_plate_pos = self._env.named.data.geom_xpos["spoon_plate"]
        cup_pos = self._env.named.data.xpos["cup"]
        spoon_spinning_reward = rewards.tolerance(
            np.linalg.norm(spoon_plate_pos - spoon_target_pos),
            margin=0.15,
        )

        spoon_in_cup_x = abs(spoon_plate_pos[0] - cup_pos[0]) < 0.1
        spoon_in_cup_y = abs(spoon_plate_pos[1] - cup_pos[1]) < 0.1
        spoon_in_cup_z = abs(spoon_plate_pos[2] - (cup_pos[2] + 0.1)) < 0.1
        reward_spoon_in_cup = (
            int(spoon_in_cup_x) + int(spoon_in_cup_y) + int(spoon_in_cup_z)
        ) // 3

        self.step_counter += 1

        reward = (
            0.15 * (stand_reward * small_control)
            + 0.25 * hand_tool_proximity_reward
            + 0.25 * reward_spoon_in_cup
            + 0.35 * spoon_spinning_reward
        )

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "hand_tool_proximity_reward": hand_tool_proximity_reward,
            "reward_spoon_in_cup": reward_spoon_in_cup,
            "spoon_spinning_reward": spoon_spinning_reward,
        }
```
```

### humanoid_bench/envs/truck.py

```
class Truck(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def upon_table(self, package)
    def get_reward(self)
    def get_terminated(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=((self.robot.dof + self.dof) * 2 - 6,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        reward = 0

        # Store initial z positions of packages
        if self.initialized == False:
            self.initialized = True
            self.initial_zs = {}
            for package in self.package_list:
                self.initial_zs[package] = self._env.named.data.xpos[package][2]

        # Check if packages have been picked up from truck
        for package in self.packages_on_truck:
            if self._env.named.data.xpos[package][2] > self.initial_zs[package] + 0.1:
                self.packages_picked_up.append(package)
                self.packages_on_truck.remove(package)
                reward += 100

        # Check if packages have been placed on table
        for package in self.packages_picked_up:
            # print('Package: ', package, self._env.named.data.xpos[package])
            if self.upon_table(package):
                self.packages_on_table.append(package)
                self.packages_picked_up.remove(package)
                reward += 100

        # Check if packages are no longer on table
        for package in self.packages_on_table:
            if not self.upon_table(package):
                self.packages_on_table.remove(package)
                self.packages_picked_up.append(package)
                reward -= 100

        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )

        # minimize distance between robot and packages on truck
        reward_robot_package_truck = 0
        if len(self.packages_on_truck) > 0:
            dist_robot_package_truck = [
                np.linalg.norm(
                    self._env.named.data.xpos[package]
                    - self._env.named.data.qpos["free_base"][:3]
                )
                for package in self.packages_on_truck
            ]
            reward_robot_package_truck = rewards.tolerance(
                np.min(dist_robot_package_truck),
                bounds=(0, 0.2),
                margin=4,
                value_at_margin=0,
                sigmoid="linear",
            )

        # minimize distance between robot and packages picked up
        reward_robot_package_picked_up = 0
        if len(self.packages_picked_up) > 0:
            dist_robot_package_picked_up = [
                np.linalg.norm(
                    self._env.named.data.xpos[package]
                    - self._env.named.data.qpos["free_base"][:3]
                )
                for package in self.packages_picked_up
            ]
            reward_robot_package_picked_up = rewards.tolerance(
                np.min(dist_robot_package_picked_up),
                bounds=(0, 0.2),
                margin=4,
                value_at_margin=0,
                sigmoid="linear",
            )

        # minimize distance between picked up packages and table
        reward_package_table = 0
        if len(self.packages_picked_up) > 0:
            dist_package_table = [
                np.linalg.norm(
                    self._env.named.data.xpos[package]
                    - self._env.named.data.xpos["table"]
                )
                for package in self.packages_picked_up
            ]
            reward_package_table = rewards.tolerance(
                np.min(dist_package_table),
                bounds=(0, 0.2),
                margin=4,
                value_at_margin=0,
                sigmoid="linear",
            )

        reward += upright * (
            1
            + reward_robot_package_truck
            + reward_robot_package_picked_up
            + reward_package_table
        )

        reward_dict = {
            "upright": upright,
            "reward_robot_package_truck": reward_robot_package_truck,
            "reward_robot_package_picked_up": reward_robot_package_picked_up,
            "reward_package_table": reward_package_table,
            "p
```
```

### humanoid_bench/envs/window.py

```
class Window(Task)
    def __init__(self, robot, env)
    def observation_space(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)

```python
def observation_space(self):
        return Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.robot.dof * 2 - 1 + self.dof * 2 - 2,),
            dtype=np.float64,
        )
```

```python
def get_reward(self):
        self.window_pane_id = self._env.named.data.geom_xpos.axes.row.names.index(
            "window_pane_collision"
        )

        self.window_wipe_id = self._env.named.data.geom_xpos.axes.row.names.index(
            "window_wipe_collision"
        )

        standing = rewards.tolerance(
            self.robot.head_height(),
            bounds=(_STAND_HEIGHT, float("inf")),
            margin=_STAND_HEIGHT / 4,
        )
        upright = rewards.tolerance(
            self.robot.torso_upright(),
            bounds=(0.9, float("inf")),
            sigmoid="linear",
            margin=1.9,
            value_at_margin=0,
        )
        stand_reward = standing * upright
        small_control = rewards.tolerance(
            self.robot.actuator_forces(),
            margin=10,
            value_at_margin=0,
            sigmoid="quadratic",
        ).mean()
        small_control = (4 + small_control) / 5

        window_contact_reward = np.min(
            [
                rewards.tolerance(
                    self._env.named.data.site_xpos[site_name, "x"],
                    bounds=(0.92, 0.92),
                    margin=0.4,
                    sigmoid="linear",
                )
                for site_name in [
                    "wipe_contact_site_a",
                    "wipe_contact_site_b",
                    "wipe_contact_site_c",
                    "wipe_contact_site_d",
                    "wipe_contact_site_e",
                ]
            ]
        )
        window_contact_filter = 0
        for pair in self._env.data.contact.geom:
            if (
                self.window_pane_id in pair and self.window_wipe_id in pair
            ):  # if has hand
                window_contact_filter = 1
                break

        left_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["left_hand"]
            - self._env.named.data.xpos["window_wiping_tool"]
        )
        right_hand_tool_distance = np.linalg.norm(
            self._env.named.data.site_xpos["right_hand"]
            - self._env.named.data.xpos["window_wiping_tool"]
        )
        hand_tool_proximity_reward = min(
            [
                rewards.tolerance(left_hand_tool_distance, bounds=(0, 0.2), margin=0.5),
                rewards.tolerance(
                    right_hand_tool_distance, bounds=(0, 0.2), margin=0.5
                ),
            ]
        )

        moving_wipe_reward = rewards.tolerance(
            abs(self._env.named.data.sensordata["window_wiping_tool_subtreelinvel"][2]),
            bounds=(0.5, 0.5),
            margin=0.5,
        )

        head_window_distance_reward = rewards.tolerance(
            np.linalg.norm(self._env.named.data.site_xpos["head"] - self.head_pos0),
            bounds=(0.4, 0.4),
            margin=0.1,
        )

        manipulation_reward = (
            0.2 * (stand_reward * small_control * head_window_distance_reward)
            + 0.4 * moving_wipe_reward
            + 0.4 * hand_tool_proximity_reward
        )
        window_contact_total_reward = window_contact_filter * window_contact_reward
        reward = 0.5 * manipulation_reward + 0.5 * window_contact_total_reward

        return reward, {
            "stand_reward": stand_reward,
            "small_control": small_control,
            "moving_wipe_reward": moving_wipe_reward,
            "hand_tool_proximity_reward": hand_tool_proximity_reward,
            "window_contact_reward": window_contact_reward,
            "window_contact_filter": window_contact_filter,
            "window_contact_total_reward": window_contact_total_reward,
        }
```
```

### humanoid_bench/mjx/envs/base.py

```
class Humanoid(MjxEnv)
    def __init__(self, path, reward_weights_dict)
    def reset(self, rng)
    def unnorm_action(self, action)
    def compute_reward(self, data, info)
    def get_info(self, state, data)
    def _resample_target(self, state, log_info)
    def step(self, state, action)
    def _get_obs(self, data, target_left, target_right)

```python
def compute_reward(self, data, info):
        # implemented in task subclass
        raise NotImplementedError
```

```python
def _get_obs(
            self, data, target_left, target_right=None
    ) -> jp.ndarray:
        """Observes humanoid body position, velocities, and angles."""

        raise NotImplementedError
```
```

### humanoid_bench/mjx/envs/cpu_env.py

```
class HumanoidNumpyEnv()
    """A humanoid environment with PyTorch-compatible observations."""
    def __init__(self, path, task, physics_steps_per_control_step)
    def _sample_from_sphere(self, center, radius)
    def reset(self, seed)
    def get_info(self)
    def unnorm_action(self, action)
    def compute_reward(self, data)
    def step(self, action)
    def _get_obs(self, data)

```python
def compute_reward(self, data):
        lef_hand_dist = np.sqrt(np.square(data.site('left_hand').xpos - data.qpos[self.left_target_idxs]).sum())
        right_hand_dist = np.sqrt(np.square(data.site('right_hand').xpos - data.qpos[self.right_target_idxs]).sum())
        if self.task == 'reach':
            dist = lef_hand_dist
        elif self.task == 'reach_two_hands':
            dist = np.max((lef_hand_dist, right_hand_dist))
        reward = float(dist < 0.1) # Trained with 0.05, but 0.1 allows to evaluate the policy for a wider range of targets
        height = data.qpos[2]
        terminated = (height < 0.3) or (height > 1.2)
        return reward, terminated
```

```python
def _get_obs(self, data) -> np.ndarray:
        """Observes humanoid body position, velocities, and angles."""
        offset = np.array([data.qpos[0], data.qpos[1], 0])
        if self.task == 'reach':
            return np.concatenate(
                (
                    data.qpos.copy()[self.body_idxs][2:],
                    data.qvel.copy()[self.body_vel_idxs],
                    data.site('left_hand').xpos - offset,
                    data.qpos.copy()[self.left_target_idxs] - offset

                )
            )
        elif self.task == 'reach_two_hands':
            return np.concatenate(
                (
                    data.qpos.copy()[self.body_idxs][2:],
                    data.qvel.copy()[self.body_vel_idxs],
                    data.site('left_hand').xpos - offset,
                    data.site('right_hand').xpos - offset,
                    data.qpos.copy()[self.left_target_idxs] - offset,
                    data.qpos.copy()[self.right_target_idxs] - offset
                )
            )
        else:
            raise NotImplementedError
```
```

### humanoid_bench/mjx/envs/reach_continual.py

```
class HumanoidReachContinual(Humanoid)
    def __init__(self, path)
    def _sample_target(self, rng)
    def _resample_target(self, state, log_info)
    def reset(self, rng)
    def check_out_of_range(self, xpos)
    def compute_reward(self, data, info)
    def _get_obs(self, data, target_left, target_right)

```python
def compute_reward(self, data, info):
        healthy_reward = 5.0
        healthy_reward = data.data.xmat[1, -1, -1] * 5.0
        motion_penalty = jp.square(data.data.qvel[self.body_vel_idxs]).sum()


        dist = info['target_dist_left']
        reaching_reward_l1 = jp.where(dist < 1, x=1.0, y=0.0)

        reward = healthy_reward - 0.0001 * motion_penalty + 5 * reaching_reward_l1 + 1000.0 * info['success_left'] #+ 1e-4 * penalty

        # terminate if torso is out of range or body height is out of range
        height = data.data.qpos[2]
        terminated = jp.where(height < 0.3, x=1.0, y=0.0)
        terminated = jp.where(height > 1.8, x=1.0, y=terminated)
        # out_of_range = self.check_out_of_range(info['hand_pos'])
        # terminated = jp.where(out_of_range, x=1.0, y=terminated)
        reward = jp.where(jp.isnan(reward), x=-1, y=reward)
        return reward, terminated
```

```python
def _get_obs(
            self, data, target_left, target_right
    ) -> jp.ndarray:
        """Observes humanoid body position, velocities, and angles."""
        offset = jp.array([data.qpos[0], data.qpos[1], 0])
        return jp.concatenate(
            (   data.qpos[self.body_idxs][2:],
                data.qvel[self.body_vel_idxs],
                data.site_xpos[4]-offset,
                # data.site_xpos[5],
                target_left-offset,
                # target_right
            )
        )
```
```

### humanoid_bench/mjx/envs/reach_continual_two_hands.py

```
class HumanoidReachContinualTwoHands(Humanoid)
    def __init__(self, path)
    def _sample_from_sphere(self, rng, center, radius)
    def _sample_target(self, rng)
    def _resample_target(self, state, log_info)
    def reset(self, rng)
    def check_out_of_range(self, xpos)
    def compute_reward(self, data, info)
    def _get_obs(self, data, target_left, target_right)

```python
def compute_reward(self, data, info):
        
        # healthy_reward = data.data.xmat[1, -1, -1] * 5.0
        motion_penalty = jp.square(data.data.qvel[self.body_vel_idxs]).sum()
    
        angle_targets = info['angle_targets']
        angle_desired = angle_targets + jp.pi / 2
        quat_desired = jp.array([jp.cos(angle_desired / 2), 0., 0., jp.sin(angle_desired / 2)])
        quat_torso = data.data.xquat[12]/jp.linalg.norm(data.data.xquat[12])
        quat_pelvis = data.data.xquat[1]/jp.linalg.norm(data.data.xquat[1])
        healthy_reward = 1.0* jp.square(jp.dot(quat_desired, quat_torso)) + 1.0* jp.square(jp.dot(quat_desired, quat_pelvis))

        dist_left = info['target_dist_left'] 
        dist_right = info['target_dist_right']

        # reaching_reward_l1 = jp.where(dist_left < 1, x=1.0, y=0.0) + jp.where(dist_right < 1, x=1.0, y=0.0)
        reaching_reward_l1 = jp.where(jp.logical_and(dist_left < 1, dist_right < 1), x=1.0, y=0.0)
        reaching_reward_l1_bis = jp.where(jp.logical_and(dist_left < 0.5, dist_right < 0.5), x=1.0, y=0.0)
        reaching_reward_l1_tris = jp.where(jp.logical_and(dist_left < 0.25, dist_right < 0.25), x=1.0, y=0.0)
        reached_single_reward = jp.where(dist_left < 0.05, x=1.0, y=0.0) + jp.where(dist_right < 0.05, x=1.0, y=0.0)

        # reward = healthy_reward - 0.0001 * motion_penalty - 0*dist_left - 0*dist_right + reaching_reward_l1 + 5 * reaching_reward_l1_bis + 0 * reached_single_reward + 1000.0 * info['success'] #+ 1e-4 * penalty
        reward = healthy_reward - 0.0001 * motion_penalty + 1 * reaching_reward_l1 + 1 * reaching_reward_l1_bis + 1 * reaching_reward_l1_tris + 1000.0 * info['success']
        # reward = healthy_reward - 0.0001 * motion_penalty - jp.max(jp.array([dist_left, dist_right])) + 1 * reaching_reward_l1 + 5 * reaching_reward_l1_bis + 1000.0 * info['success']

        # terminate if torso is out of range or body height is out of range
        height = data.data.qpos[2]
        terminated = jp.where(height < 0.3, x=1.0, y=0.0)
        terminated = jp.where(height > 1.8, x=1.0, y=terminated)
        # out_of_range = self.check_out_of_range(info['hand_pos'])
        # terminated = jp.where(out_of_range, x=1.0, y=terminated)
        reward = jp.where(jp.isnan(reward), x=-1, y=reward)
        return reward, terminated
```

```python
def _get_obs(
            self, data, target_left, target_right
    ) -> jp.ndarray:
        """Observes humanoid body position, velocities, and angles."""

        offset = jp.array([data.qpos[0], data.qpos[1], 0])
        return jp.concatenate(
            (
                data.qpos[self.body_idxs][2:],
                data.qvel[self.body_vel_idxs],
                data.site_xpos[4]-offset,
                data.site_xpos[5]-offset,
                target_left-offset,
                target_right-offset
            )
        )
```
```

### humanoid_bench/mjx/envs/utils.py

```
def perturbed_pipeline_step(sys, pipeline_state, action, xfrc_applied, n_frames)
```

### humanoid_bench/mjx/ppo_continuous_action.py

```
class ActorCritic(Module)
    def __call__(self, x)
class Transition(NamedTuple)
def make_train(config, writer)
def main(_)
```

### humanoid_bench/tasks.py

```
class Task()
    def __init__(self, robot, env)
    def observation_space(self)
    def get_obs(self)
    def get_reward(self)
    def get_terminated(self)
    def reset_model(self)
    def normalize_action(self, action)
    def unnormalize_action(self, action)
    def step(self, action)
    def render(self)

```python
def observation_space(self):
        return None
```

```python
def get_reward(self):
        return 0, {}
```
```

### tdmpc2/tdmpc2/envs/__init__.py

```
def missing_dependencies(task)
def make_multitask_env(cfg)
def make_env(cfg)
```

### tdmpc2/tdmpc2/envs/dmcontrol.py

```
class ExtendedTimeStep(NamedTuple)
    def first(self)
    def mid(self)
    def last(self)
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
    def observation_spec(self)
    def action_spec(self)
    def reset(self)
    def __getattr__(self, name)
class ExtendedTimeStepWrapper(Environment)
    def __init__(self, env)
    def reset(self)
    def step(self, action)
    def _augment_time_step(self, time_step, action)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)
class TimeStepToGymWrapper()
    def __init__(self, env, domain, task)
    def unwrapped(self)
    def reward_range(self)
    def metadata(self)
    def _obs_to_array(self, obs)
    def reset(self)
    def step(self, action)
    def render(self, mode, width, height, camera_id)
def make_env(cfg)

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

```python
def reward_range(self):
        return None
```
```

### tdmpc2/tdmpc2/envs/humanoid.py

```
class HumanoidWrapper(Wrapper)
    def __init__(self, env, cfg)
    def step(self, action)
    def unwrapped(self)
    def render(self)
def make_env(cfg)
```

### tdmpc2/tdmpc2/envs/maniskill.py

```
class ManiSkillWrapper(Wrapper)
    def __init__(self, env, cfg)
    def reset(self)
    def step(self, action)
    def unwrapped(self)
    def render(self, args)
def make_env(cfg)
```

### tdmpc2/tdmpc2/envs/metaworld.py

```
class MetaWorldWrapper(Wrapper)
    def __init__(self, env, cfg)
    def reset(self)
    def step(self, action)
    def unwrapped(self)
    def render(self)
def make_env(cfg)
```

### tdmpc2/tdmpc2/envs/myosuite.py

```
class MyoSuiteWrapper(Wrapper)
    def __init__(self, env, cfg)
    def step(self, action)
    def unwrapped(self)
    def render(self)
def make_env(cfg)
```

### tdmpc2/tdmpc2/envs/tasks/ball_in_cup.py

```
def get_model_and_assets()
def spin(time_limit, random, environment_kwargs)
class Physics(Physics)
    """Physics with additional features for the Ball-in-Cup domain."""
    def ball_to_target(self)
    def in_target(self)
class CustomBallInCup(BallInCup)
    """Custom Ball-in-Cup tasks."""
    def initialize_episode(self, physics)
    def get_observation(self, physics)
    def get_reward(self, physics)

```python
def get_observation(self, physics):
        """Returns an observation of the state."""
        obs = collections.OrderedDict()
        obs["position"] = physics.position()
        obs["velocity"] = physics.velocity()
        return obs
```

```python
def get_reward(self, physics):
        dist = np.linalg.norm(physics.ball_to_target())
        ball_vel_x = abs(physics.named.data.qvel["ball_x"])
        ball_vel_z = abs(physics.named.data.qvel["ball_z"])
        ball_vel = np.linalg.norm([ball_vel_x, ball_vel_z])

        # reward: spin around target (maximize distance to target + ball velocity)
        dist_reward = rewards.tolerance(
            dist,
            bounds=(_DIST_TARGET, float("inf")),
            margin=_DIST_TARGET / 2,
            value_at_margin=0.5,
            sigmoid="linear",
        )
        not_in_target = 1 - physics.in_target()
        vel_reward = rewards.tolerance(
            ball_vel,
            bounds=(_TARGET_SPEED, float("inf")),
            margin=_TARGET_SPEED / 2,
            value_at_margin=0.5,
            sigmoid="linear",
        )
        spin_reward = not_in_target * (dist_reward + 2 * vel_reward) / 3
        return spin_reward
```
```

### tdmpc2/tdmpc2/envs/tasks/cheetah.py

```
def get_model_and_assets()
def run_backwards(time_limit, random, environment_kwargs)
def stand_front(time_limit, random, environment_kwargs)
def stand_back(time_limit, random, environment_kwargs)
def jump(time_limit, random, environment_kwargs)
def run_front(time_limit, random, environment_kwargs)
def run_back(time_limit, random, environment_kwargs)
def lie_down(time_limit, random, environment_kwargs)
def legs_up(time_limit, random, environment_kwargs)
def flip(time_limit, random, environment_kwargs)
def flip_backwards(time_limit, random, environment_kwargs)
class Physics(Physics)
    """Physics simulation with additional features for the Cheetah domain."""
    def angmomentum(self)
class CustomCheetah(Cheetah)
    """Custom Cheetah tasks."""
    def __init__(self, goal, move_speed, random)
    def _run_backwards_reward(self, physics)
    def _stand_one_foot_reward(self, physics, foot)
    def _stand_front_reward(self, physics)
    def _stand_back_reward(self, physics)
    def _jump_reward(self, physics)
    def _run_one_foot_reward(self, physics, foot)
    def _run_front_reward(self, physics)
    def _run_back_reward(self, physics)
    def _lie_down_reward(self, physics)
    def _legs_up_reward(self, physics)
    def _flip_reward(self, physics, forward)
    def get_reward(self, physics)

```python
def _run_backwards_reward(self, physics):
        return rewards.tolerance(
            physics.speed(),
            bounds=(-float("inf"), -self._move_speed),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
```

```python
def _stand_one_foot_reward(self, physics, foot):
        """Note: `foot` is the foot that is *not* on the ground."""
        torso_height = physics.named.data.xpos["torso", "z"]
        foot_height = physics.named.data.xpos[foot, "z"]
        height_reward = rewards.tolerance(
            (torso_height + foot_height) / 2,
            bounds=(_CHEETAH_JUMP_HEIGHT, float("inf")),
            margin=_CHEETAH_JUMP_HEIGHT / 2,
        )
        horizontal_speed_reward = rewards.tolerance(
            physics.speed(),
            bounds=(-self._move_speed, self._move_speed),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
        stand_reward = (5 * height_reward + horizontal_speed_reward) / 6
        return stand_reward
```

```python
def _stand_front_reward(self, physics):
        return self._stand_one_foot_reward(physics, "bfoot")
```

```python
def _stand_back_reward(self, physics):
        return self._stand_one_foot_reward(physics, "ffoot")
```

```python
def _jump_reward(self, physics):
        front_reward = self._stand_front_reward(physics)
        back_reward = self._stand_back_reward(physics)
        jump_reward = (front_reward + back_reward) / 2
        return jump_reward
```

```python
def _run_one_foot_reward(self, physics, foot):
        """Note: `foot` is the foot that is *not* on the ground."""
        torso_height = physics.named.data.xpos["torso", "z"]
        foot_height = physics.named.data.xpos[foot, "z"]
        torso_up = rewards.tolerance(
            torso_height,
            bounds=(_CHEETAH_JUMP_HEIGHT, float("inf")),
            margin=_CHEETAH_JUMP_HEIGHT / 2,
        )
        foot_up = rewards.tolerance(
            foot_height,
            bounds=(_CHEETAH_JUMP_HEIGHT, float("inf")),
            margin=_CHEETAH_JUMP_HEIGHT / 2,
        )
        up_reward = (3 * foot_up + 2 * torso_up) / 5
        if self._move_speed == 0:
            return up_reward
        horizontal_speed_reward = rewards.tolerance(
            physics.speed(),
            bounds=(self._move_speed, float("inf")),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
        return up_reward * (5 * horizontal_speed_reward + 1) / 6
```

```python
def _run_front_reward(self, physics):
        return self._run_one_foot_reward(physics, "bfoot")
```

```python
def _run_back_reward(self, physics):
        return self._run_one_foot_reward(physics, "ffoot")
```

```python
def _lie_down_reward(self, physics):
        torso_height = physics.named.data.xpos["torso", "z"]
        feet_height = (
            physics.named.data.xpos["ffoot", "z"]
            + physics.named.data.xpos["bfoot", "z"]
        ) / 2
        torso_down = rewards.tolerance(
            torso_height,
            bounds=(-float("inf"), _CHEETAH_LIE_HEIGHT),
            margin=_CHEETAH_LIE_HEIGHT,
            value_at_margin=0,
            sigmoid="linear",
        )
        feet_down = rewards.tolerance(
            feet_height,
            bounds=(-float("inf"), _CHEETAH_LIE_HEIGHT),
            margin=_CHEETAH_LIE_HEIGHT,
            value_at_margin=0,
            sigmoid="linear",
        )
        lie_down_reward = (3 * torso_down + feet_down) / 4
        return lie_down_reward
```

```python
def _legs_up_reward(self, physics):
        torso_height = physics.named.data.xpos["torso", "z"]
        torso_down = rewards.tolerance(
            torso_height,
            bounds=(-float("inf"), _CHEETAH_LIE_HEIGHT),
            margin=_CHEETAH_LIE_HEIGHT / 2,
        )
        get_up = self._run_one_foot_reward(physics, "bfoot")
        legs_up_reward = (5 * torso_down + get_up) / 6
        return legs_up_reward
```

```python
def _flip_reward(self, physics, forward=True):
        spin_reward = rewards.tolerance(
            (1.0 if forward else -1.0) * physics.angmomentum(),
            bounds=(_CHEETAH_SPIN_SPEED, float("inf")),
            margin=_CHEETAH_SPIN_SPEED,
            value_at_margin=0,
            sigmoid="linear",
        )
        horizontal_speed_reward = rewards.tolerance(
            (1.0 if forward else -1.0) * physics.speed(),
            bounds=(self._move_speed, float("inf")),
            margin=self._move_speed,
            value_at_margin=0,
            sigmoid="linear",
        )
        flip_reward = (2 * spin_reward + horizontal_speed_reward) / 3
        return flip_reward
```

```python
def get_reward(self, physics):
        if self._goal == "run-backwards":
            return self._run_backwards_reward(physics)
        elif self._goal == "stand-front":
            return self._stand_front_reward(physics)
        elif self._goal == "stand-back":
            return self._stand_back_reward(physics)
        elif self._goal == "jump":
            return self._jump_reward(physics)
        elif self._goal == "run-front":
            return self._run_front_reward(physics)
        elif self._goal == "run-back":
            return self._run_back_reward(physics)
        elif self._goal == "lie-down":
            return self._lie_down_reward(physics)
        elif self._goal == "legs-up":
            return self._legs_up_reward(physics)
        elif self._goal == "flip":
            return self._flip_reward(physics, forward=True)
        elif self._goal == "flip-backwards":
            return self._flip_reward(physics, forward=False)
        else:
            raise NotImplementedError(f"Goal {self._goal} is not implemented.")
```
```

### tdmpc2/tdmpc2/envs/tasks/fish.py

```
def get_model_and_assets()
def obstacles(time_limit, random, environment_kwargs)
class Obstacles(Swim)
    """A custom Fish Obstacles task."""
    def __init__(self, random)
    def in_wall(self, physics, name, min_distance)
    def initialize_episode(self, physics)
    def get_reward(self, physics)

```python
def get_reward(self, physics):
        radii = physics.named.model.geom_size[["mouth", "target"], 0].sum()
        in_target = rewards.tolerance(
            np.linalg.norm(physics.mouth_to_target()),
            bounds=(0, radii),
            margin=2 * radii,
        )
        is_upright = 0.5 * (physics.upright() + 1)
        is_not_in_wall = 1.0 - self.in_wall(physics, "torso", min_distance=0.06)
        return is_not_in_wall * (7 * in_target + is_upright) / 8
```
```

### tdmpc2/tdmpc2/envs/tasks/hopper.py

```
def get_model_and_assets()
def hop_backwards(time_limit, random, environment_kwargs)
def flip(time_limit, random, environment_kwargs)
def flip_backwards(time_limit, random, environment_kwargs)
class Physics(Physics)
    def angmomentum(self)
class CustomHopper(Hopper)
    """Custom Hopper tasks."""
    def __init__(self, goal, random)
    def _hop_backwards_reward(self, physics)
    def _flip_reward(self, physics, forward)
    def get_reward(self, physics)

```python
def _hop_backwards_reward(self, physics):
        standing = rewards.tolerance(physics.height(), (_STAND_HEIGHT, 2))
        hopping = rewards.tolerance(
            physics.speed(),
            bounds=(-float("inf"), -_HOP_SPEED / 2),
            margin=_HOP_SPEED / 4,
            value_at_margin=0.5,
            sigmoid="linear",
        )
        return standing * hopping
```

```python
def _flip_reward(self, physics, forward=True):
        reward = rewards.tolerance(
            (1.0 if forward else -1.0) * physics.angmomentum(),
            bounds=(_SPIN_SPEED, float("inf")),
            margin=_SPIN_SPEED / 2,
            value_at_margin=0,
            sigmoid="linear",
        )
        return reward
```

```python
def get_reward(self, physics):
        if self._goal == "hop-backwards":
            return self._hop_backwards_reward(physics)
        elif self._goal == "flip":
            return self._flip_reward(physics, forward=True)
        elif self._goal == "flip-backwards":
            return self._flip_reward(physics, forward=False)
        else:
            raise NotImplementedError(f"Goal {self._goal} is not implemented.")
```
```

### tdmpc2/tdmpc2/envs/tasks/pendulum.py

```
def get_model_and_assets()
def spin(time_limit, random, environment_kwargs)
class Spin(SwingUp)
    """A custom Pendulum Spin task."""
    def __init__(self, random)
    def get_reward(self, physics)

```python
def get_reward(self, physics):
        return rewards.tolerance(
            np.linalg.norm(physics.angular_velocity()),
            bounds=(_TARGET_SPEED, float("inf")),
            margin=_TARGET_SPEED / 2,
            value_at_margin=0.5,
            sigmoid="linear",
        )
```
```

### tdmpc2/tdmpc2/envs/tasks/reacher.py

```
def get_model_and_assets(links)
def three_easy(time_limit, random, environment_kwargs)
def three_hard(time_limit, random, environment_kwargs)
def four_easy(time_limit, random, environment_kwargs)
def four_hard(time_limit, random, environment_kwargs)
class Physics(Physics)
    """Physics simulation with additional features for the Reacher domain."""
    def finger_to_target(self)
    def finger_to_target_dist(self)
class CustomThreeLinkReacher(Reacher)
    """Custom Reacher tasks."""
    def __init__(self, target_size, random)
    def get_observation(self, physics)

```python
def get_observation(self, physics):
        obs = collections.OrderedDict()
        obs["position"] = physics.position()
        obs["to_target"] = physics.finger_to_target()
        obs["velocity"] = physics.velocity()
        return obs
```
```

### tdmpc2/tdmpc2/envs/tasks/walker.py

```
def get_model_and_assets()
def walk_backwards(time_limit, random, environment_kwargs)
def run_backwards(time_limit, random, environment_kwargs)
def arabesque(time_limit, random, environment_kwargs)
def lie_down(time_limit, random, environment_kwargs)
def legs_up(time_limit, random, environment_kwargs)
def headstand(time_limit, random, environment_kwargs)
def flip(time_limit, random, environment_kwargs)
def backflip(time_limit, random, environment_kwargs)
class BackwardsPlanarWalker(PlanarWalker)
    """Backwards PlanarWalker task."""
    def __init__(self, move_speed, random)
    def get_reward(self, physics)
class YogaPlanarWalker(PlanarWalker)
    """Yoga PlanarWalker tasks."""
    def __init__(self, goal, move_speed, random)
    def _arabesque_reward(self, physics)
    def _lie_down_reward(self, physics)
    def _legs_up_reward(self, physics)
    def _flip_reward(self, physics)
    def get_reward(self, physics)

```python
def get_reward(self, physics):
        standing = rewards.tolerance(
            physics.torso_height(),
            bounds=(walker._STAND_HEIGHT, float("inf")),
            margin=walker._STAND_HEIGHT / 2,
        )
        upright = (1 + physics.torso_upright()) / 2
        stand_reward = (3 * standing + upright) / 4
        if self._move_speed == 0:
            return stand_reward
        else:
            move_reward = rewards.tolerance(
                physics.horizontal_velocity(),
                bounds=(-float("inf"), -self._move_speed),
                margin=self._move_speed / 2,
                value_at_margin=0.5,
                sigmoid="linear",
            )
            return stand_reward * (5 * move_reward + 1) / 6
```

```python
def _arabesque_reward(self, physics):
        standing = rewards.tolerance(
            physics.torso_height(),
            bounds=(_YOGA_STAND_HEIGHT, float("inf")),
            margin=_YOGA_STAND_HEIGHT / 2,
        )
        left_foot_height = physics.named.data.xpos["left_foot", "z"]
        right_foot_height = physics.named.data.xpos["right_foot", "z"]
        left_foot_down = rewards.tolerance(
            left_foot_height,
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_STAND_HEIGHT / 2,
        )
        right_foot_up = rewards.tolerance(
            right_foot_height,
            bounds=(_YOGA_STAND_HEIGHT, float("inf")),
            margin=_YOGA_STAND_HEIGHT / 2,
        )
        upright = (1 - physics.torso_upright()) / 2
        arabesque_reward = (3 * standing + left_foot_down + right_foot_up + upright) / 6
        return arabesque_reward
```

```python
def _lie_down_reward(self, physics):
        torso_down = rewards.tolerance(
            physics.torso_height(),
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_LIE_DOWN_HEIGHT / 2,
        )
        thigh_height = (
            physics.named.data.xpos["left_thigh", "z"]
            + physics.named.data.xpos["right_thigh", "z"]
        ) / 2
        thigh_down = rewards.tolerance(
            thigh_height,
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_LIE_DOWN_HEIGHT / 2,
        )
        feet_height = (
            physics.named.data.xpos["left_foot", "z"]
            + physics.named.data.xpos["right_foot", "z"]
        ) / 2
        feet_down = rewards.tolerance(
            feet_height,
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_LIE_DOWN_HEIGHT / 2,
        )
        upright = (1 - physics.torso_upright()) / 2
        lie_down_reward = (3 * torso_down + thigh_down + upright) / 5
        return lie_down_reward
```

```python
def _legs_up_reward(self, physics):
        torso_down = rewards.tolerance(
            physics.torso_height(),
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_LIE_DOWN_HEIGHT / 2,
        )
        thigh_height = (
            physics.named.data.xpos["left_thigh", "z"]
            + physics.named.data.xpos["right_thigh", "z"]
        ) / 2
        thigh_down = rewards.tolerance(
            thigh_height,
            bounds=(-float("inf"), _YOGA_LIE_DOWN_HEIGHT),
            margin=_YOGA_LIE_DOWN_HEIGHT / 2,
        )
        feet_height = (
            physics.named.data.xpos["left_foot", "z"]
            + physics.named.data.xpos["right_foot", "z"]
        ) / 2
        legs_up = rewards.tolerance(
            feet_height,
            bounds=(_YOGA_LEGS_UP_HEIGHT, float("inf")),
            margin=_YOGA_LEGS_UP_HEIGHT / 2,
        )
        upright = (1 - physics.torso_upright()) / 2
        legs_up_reward = (3 * torso_down + 2 * legs_up + thigh_down + upright) / 7
        return legs_up_reward
```

```python
def _flip_reward(self, physics):
        thigh_height = (
            physics.named.data.xpos["left_thigh", "z"]
            + physics.named.data.xpos["right_thigh", "z"]
        ) / 2
        thigh_up = rewards.tolerance(
            thigh_height,
            bounds=(_YOGA_STAND_HEIGHT, float("inf")),
            margin=_YOGA_STAND_HEIGHT / 2,
        )
        feet_height = (
            physics.named.data.xpos["left_foot", "z"]
            + physics.named.data.xpos["right_foot", "z"]
        ) / 2
        legs_up = rewards.tolerance(
            feet_height,
            bounds=(_YOGA_LEGS_UP_HEIGHT, float("inf")),
            margin=_YOGA_LEGS_UP_HEIGHT / 2,
        )
        upside_down_reward = (3 * legs_up + 2 * thigh_up) / 5
        if self._move_speed == 0:
            return upside_down_reward
        move_reward = rewards.tolerance(
            physics.horizontal_velocity(),
            bounds=(self._move_speed, float("inf"))
            if self._move_speed > 0
            else (-float("inf"), self._move_speed),
            margin=abs(self._move_speed) / 2,
            value_at_margin=0.5,
            sigmoid="linear",
        )
        return upside_down_reward * (5 * move_reward + 1) / 6
```

```python
def get_reward(self, physics):
        if self._goal == "arabesque":
            return self._arabesque_reward(physics)
        elif self._goal == "lie_down":
            return self._lie_down_reward(physics)
        elif self._goal == "legs_up":
            return self._legs_up_reward(physics)
        elif self._goal == "flip":
            return self._flip_reward(physics)
        else:
            raise NotImplementedError(f"Goal {self._goal} is not implemented.")
```
```

### tdmpc2/tdmpc2/envs/wrappers/multitask.py

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

### tdmpc2/tdmpc2/envs/wrappers/pixels.py

```
class PixelWrapper(Wrapper)
    """Wrapper for pixel observations. Compatible with DMControl environments."""
    def __init__(self, cfg, env, num_frames, render_size)
    def _get_obs(self)
    def reset(self)
    def step(self, action)

```python
def _get_obs(self):
        frame = self.env.render(
            mode="rgb_array", width=self._render_size, height=self._render_size
        ).transpose(2, 0, 1)
        self._frames.append(frame)
        return torch.from_numpy(np.concatenate(self._frames))
```
```

### tdmpc2/tdmpc2/envs/wrappers/tensor.py

```
class TensorWrapper(Wrapper)
    """Wrapper for converting numpy arrays to torch tensors."""
    def __init__(self, env)
    def rand_act(self)
    def _try_f32_tensor(self, x)
    def _obs_to_tensor(self, obs)
    def reset(self, task_idx)
    def step(self, action)
```

### tdmpc2/tdmpc2/envs/wrappers/time_limit.py

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

### tdmpc2/tdmpc2/train.py

```
def train(cfg)
```

### tdmpc2/tdmpc2/trainer/base.py

```
class Trainer()
    """Base trainer class for TD-MPC2."""
    def __init__(self, cfg, env, agent, buffer, logger)
    def eval(self)
    def train(self)
```

### tdmpc2/tdmpc2/trainer/offline_trainer.py

```
class OfflineTrainer(Trainer)
    """Trainer class for multi-task offline TD-MPC2 training."""
    def __init__(self)
    def eval(self)
    def train(self)
```

### tdmpc2/tdmpc2/trainer/online_trainer.py

```
class OnlineTrainer(Trainer)
    """Trainer class for single-task online TD-MPC2 training."""
    def __init__(self)
    def common_metrics(self)
    def eval(self)
    def to_td(self, obs, action, reward)
    def train(self)
```