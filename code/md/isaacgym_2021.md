# isaacgym_2021

source: https://github.com/isaac-sim/IsaacGymEnvs


commit: aeed298638a1f7b5421b38f5f3cc2d1079b6d9c3


## README

# Isaac Gym Benchmark Environments

[Website](https://developer.nvidia.com/isaac-gym) | [Technical Paper](https://arxiv.org/abs/2108.10470) | [Videos](https://sites.google.com/view/isaacgym-nvidia)


### About this repository

This repository contains example RL environments for the NVIDIA Isaac Gym high performance environments described [in our NeurIPS 2021 Datasets and Benchmarks paper](https://openreview.net/forum?id=fgFBtYgJQX_)


### Installation

Download the Isaac Gym Preview 4 release from the [website](https://developer.nvidia.com/isaac-gym), then
follow the installation instructions in the documentation. We highly recommend using a conda environment 
to simplify set up.

Ensure that Isaac Gym works on your system by running one of the examples from the `python/examples` 
directory, like `joint_monkey.py`. Follow troubleshooting steps described in the Isaac Gym Preview 4
install instructions if you have any trouble running the samples.

Once Isaac Gym is installed and samples work within your current python environment, install this repo:

```bash
pip install -e .
```


### Creating an environment

We offer an easy-to-use API for creating preset vectorized environments. For more info on what a vectorized environment is and its usage, please refer to the Gym library [documentation](https://www.gymlibrary.dev/content/vectorising/#vectorized-environments).

```python
import isaacgym
import isaacgymenvs
import torch

num_envs = 2000

envs = isaacgymenvs.make(
	seed=0, 
	task="Ant", 
	num_envs=num_envs, 
	sim_device="cuda:0",
	rl_device="cuda:0",
)
print("Observation space is", envs.observation_space)
print("Action space is", envs.action_space)
obs = envs.reset()
for _ in range(20):
	random_actions = 2.0 * torch.rand((num_envs,) + envs.action_space.shape, device = 'cuda:0') - 1.0
	envs.step(random_actions)
```


### Running the benchmarks

To train your first policy, run this line:

```bash
python train.py task=Cartpole
```

Cartpole should train to the point that the pole stays upright within a few seconds of starting.

Here's another example - Ant locomotion:

```bash
python train.py task=Ant
```

Note that by default we show a preview window, which will usually slow down training. You 
can use the `v` key while running to disable viewer updates and allow training to proceed 
faster. Hit the `v` key again to resume viewing after a few seconds of training, once the 
ants have learned to run a bit better.

Use the `esc` key or close the viewer window to stop training early.

Alternatively, you can train headlessly, as follows:

```bash
python train.py task=Ant headless=True
```

Ant may take a minute or two to train a policy you can run. When running headlessly, you 
can stop it early using Control-C in the command line window.

### Loading trained models // Checkpoints

Checkpoints are saved in the folder `runs/EXPERIMENT_NAME/nn` where `EXPERIMENT_NAME` 
defaults to the task name, but can also be overridden via the `experiment` argument.

To load a trained checkpoint and continue training, use the `checkpoint` argument:

```bash
python train.py task=Ant checkpoint=runs/Ant/nn/Ant.pth
```

To load a trained checkpoint and only perform inference (no training), pass `test=True` 
as an argument, along with the checkpoint name. To avoid rendering overhead, you may 
also want to run with fewer environments using `num_envs=64`:

```bash
python train.py task=Ant checkpoint=runs/Ant/nn/Ant.pth test=True num_envs=64
```

Note that If there are special characters such as `[` or `=` in the checkpoint names, 
you will need to escape them and put quotes around the string. For example,
`checkpoint="./runs/Ant/nn/last_Antep\=501rew\[5981.31\].pth"`


### Configuration and command line arguments

We use [Hydra](https://hydra.cc/docs/intro/) to manage the config. Note that this has some 
differences from previous incarnations in older versions of Isaac Gym.
 
Key arguments to the `train.py` script are:

* `task=TASK` - selects which task to use. Any of `AllegroHand`, `AllegroHandDextremeADR`, `AllegroHandDextremeManualDR`, `AllegroKukaLSTM`, `AllegroKukaTwoArmsLSTM`, `Ant`, `Anymal`, `AnymalTerrain`, `BallBalance`, `Cartpole`, `FrankaCabinet`, `Humanoid`, `Ingenuity` `Quadcopter`, `ShadowHand`, `ShadowHandOpenAI_FF`, `ShadowHandOpenAI_LSTM`, and `Trifinger` (these correspond to the config for each environment in the folder `isaacgymenvs/config/task`)
* `train=TRAIN` - selects which training config to use. Will automatically default to the correct config for the environment (ie. `<TASK>PPO`).
* `num_envs=NUM_ENVS` - selects the number of environments to use (overriding the default number of environments set in the task config).
* `seed=SEED` - sets a seed value for randomizations, and overrides the default seed set up in the task config
* `sim_device=SIM_DEVICE_TYPE` - Device used for physics simulation. Set to `cuda:0` (default) to use GPU and to `cpu` for CPU. Follows PyTorch-like device syntax.
* `rl_device=RL_DEVICE` - Which device / ID to use for the RL algorithm. Defaults to `cuda:0`, and also follows PyTorch-like device syntax.
* `graphics_device_id=GRAPHICS_DEVICE_ID` - Which Vulkan graphics device ID to use for rendering. Defaults to 0. **Note** - this may be different from CUDA device ID, and does **not** follow PyTorch-like device syntax.
* `pipeline=PIPELINE` - Which API pipeline to use. Defaults to `gpu`, can also set to `cpu`. When using the `gpu` pipeline, all data stays on the GPU and everything runs as fast as possible. When using the `cpu` pipeline, simulation can run on either CPU or GPU, depending on the `sim_device` setting, but a copy of the data is always made on the CPU at every step.
* `test=TEST`- If set to `True`, only runs inference on the policy and does not do any training.
* `checkpoint=CHECKPOINT_PATH` - Set to path to the checkpoint to load for training or testing.
* `headless=HEADLESS` - Whether to run in headless mode.
* `experiment=EXPERIMENT` - Sets the name of the experiment.
* `max_iterations=MAX_ITERATIONS` - Sets how many iterations to run for. Reasonable defaults are provided for the provided environments.

Hydra also allows setting variables inside config files directly as command line arguments. As an example, to set the discount rate for a rl_games training run, you can use `train.params.config.gamma=0.999`. Similarly, variables in task configs can also be set. For example, `task.env.enableDebugVis=True`.

#### Hydra Notes

Default values for each of these are found in the `isaacgymenvs/config/config.yaml` file.

The way that the `task` and `train` portions of the config works are through the use of config groups. 
You can learn more about how these work [here](https://hydra.cc/docs/tutorials/structured_config/config_groups/)
The actual configs for `task` are in `isaacgymenvs/config/task/<TASK>.yaml` and for train in `isaacgymenvs/config/train/<TASK>PPO.yaml`. 

In some places in the config you will find other variables referenced (for example,
 `num_actors: ${....task.env.numEnvs}`). Each `.` represents going one level up in the config hierarchy.
 This is documented fully [here](https://omegaconf.readthedocs.io/en/latest/usage.html#variable-interpolation).

## Tasks

Source code for tasks can be found in `isaacgymenvs/tasks`. 

Each task subclasses the `VecEnv` base class in `isaacgymenvs/base/vec_task.py`.

Refer to [docs/framework.md](docs/framework.md) for how to create your own tasks.

Full details on each of the tasks available can be found in the [RL examples documentation](docs/rl_examples.md).

## Domain Randomization

IsaacGymEnvs includes a framework for Domain Randomization to improve Sim-to-Real transfer of trained
RL policies. You can read more about it [here](docs/domain_randomization.md).

## Reproducibility and Determinism

If deterministic training of RL policies is important for your work, you may wish to review our [Reproducibility and Determinism Documentation](docs/reproducibility.md).

## Multi-GPU Training

You can run multi-GPU training using `torchrun` (i.e., `torch.distributed`) using this repository.

Here is an example command for how to run in this way -
`torchrun --standalone --nnodes=1 --nproc_per_node=2 train.py multi_gpu=True task=Ant <OTHER_ARGS>`

Where the `--nproc_per_node=` flag specifies how many processes to run and note the `multi_gpu=True` flag must be set on the train script in order for multi-GPU training to run.

## Population Based Training

You can run population based training to help find good hyperparameters or to train on very difficult environments which would otherwise
be hard to learn anything on without it. See [the readme](docs/pbt.md) for details.

## WandB support

You can run [WandB](https://wandb.ai/) with Isaac Gym Envs by setting `wandb_activate=True` flag from the command line. You can set the group, name, entity, and project for the run by setting the `wandb_group`, `wandb_name`, `wandb_entity` and `wandb_project` set. Make sure you have WandB installed with `pip install wandb` before activating.


## Capture videos


We implement the standard `env.render(mode='rgb_rray')` `gym` API to provide an image of the simulator viewer. Additionally, we can leverage `gym.wrappers.RecordVideo` to help record videos that shows agent's gameplay. Consider running the following file which should produce a video in the `videos` folder.

```python
import gym
import isaacgym
import isaacgymenvs
import torch

num_envs = 64

envs = isaacgymenvs.make(
	seed=0, 
	task="Ant", 
	num_envs=num_envs, 
	sim_device="cuda:0",
	rl_device="cuda:0",
	graphics_device_id=0,
	headless=False,
	multi_gpu=False,
	virtual_screen_capture=True,
	force_render=False,
)
envs.is_vector_env = True
envs = gym.wrappers.RecordVideo(
	envs,
	"./videos",
	step_trigger=lambda step: step % 10000 == 0, # record the videos every 10000 steps
	video_length=100  # for each video record up to 100 steps
)
envs.reset()
print("the image of Isaac Gym viewer is an array of shape", envs.render(mode="rgb_array").shape)
for _ in range(100):
	actions = 2.0 * torch.rand((num_envs,) + envs.action_space.shape, device = 'cuda:0') - 1.0
	envs.step(actions)
```

## Capture videos during training

You can automatically capture the videos of the agents gameplay by toggling the `capture_video=True` flag and tune the capture frequency `capture_video_freq=1500` and video length via `capture_video_len=100`. You can set `force_render=False` to disable rendering when the videos are not captured.

```
python train.py capture_video=True capture_video_freq=1500 capture_video_len=100 force_render=False
```

You can also automatically upload the videos to Weights and Biases:

```
python train.py task=Ant wandb_activate=True wandb_entity=nvidia wandb_project=rl_games capture_video=True force_render=False
```

## Pre-commit

We use [pre-commit](https://pre-commit.com/) to helps us automate short tasks that improve code quality. Before making a commit to the repository, please ensure `pre-commit run --all-files` runs without error.


## Troubleshooting

Please review the Isaac Gym installation instructions first if you run into any issues.

You can either submit issues through GitHub or through the [Isaac Gym forum here](https://forums.developer.nvidia.com/c/agx-autonomous-machines/isaac/isaac-gym/322).

## Citing

Please cite this work as:
```
@misc{makoviychuk2021isaac,
      title={Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning}, 
      author={Viktor Makoviychuk and Lukasz Wawrzyniak and Yunrong Guo and Michelle Lu and Kier Storey and Miles Macklin and David Hoeller and Nikita Rudin and Arthur Allshire and Ankur Handa and Gavriel State},
      year={2021},
      journal={arXiv preprint arXiv:2108.10470}
}
```

**Note** if you use the DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with Population Based Training work or the code related to Population Based Training, please cite the following paper:

```
@inproceedings{
	petrenko2023dexpbt,
	author = {Aleksei Petrenko, Arthur Allshire, Gavriel State, Ankur Handa, Viktor Makoviychuk},
	title = {DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with Population Based Training},
	booktitle = {RSS},
	year = {2023}
}
```

**Note** if you use the DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality work or the code related to Automatic Domain Randomisation, please cite the following paper:

```
@inproceedings{
	handa2023dextreme,
	author = {Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar Sundaralingam, Yashraj Narang, Jean-Francois Lafleche, Dieter Fox, Gavriel State},
	title = {DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality},
	booktitle = {ICRA},
	year = {2023}
} 
```

**Note** if you use the ANYmal rough terrain environment in your work, please ensure you cite the following work:
```
@misc{rudin2021learning,
      title={Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning}, 
      author={Nikita Rudin and David Hoeller and Philipp Reist and Marco Hutter},
      year={2021},
      journal = {arXiv preprint arXiv:2109.11978}
}
```

**Note** if you use the Trifinger environment in your work, please ensure you cite the following work:
```
@misc{isaacgym-trifinger,
  title     = {{Transferring Dexterous Manipulation from GPU Simulation to a Remote Real-World TriFinger}},
  author    = {Allshire, Arthur and Mittal, Mayank and Lodaya, Varun and Makoviychuk, Viktor and Makoviichuk, Denys and Widmaier, Felix and Wuthrich, Manuel and Bauer, Stefan and Handa, Ankur and Garg, Animesh},
  year      = {2021},
  journal = {arXiv preprint arXiv:2108.09779}
}
```

**Note** if you use the AMP: Adversarial Motion Priors environment in your work, please ensure you cite the following work:
```
@article{
	2021-TOG-AMP,
	author = {Peng, Xue Bin and Ma, Ze and Abbeel, Pieter and Levine, Sergey and Kanazawa, Angjoo},
	title = {AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control},
	journal = {ACM Trans. Graph.},
	issue_date = {August 2021},
	volume = {40},
	number = {4},
	month = jul,
	year = {2021},
	articleno = {1},
	numpages = {15},
	url = {http://doi.acm.org/10.1145/3450626.3459670},
	doi = {10.1145/3450626.3459670},
	publisher = {ACM},
	address = {New York, NY, USA},
	keywords = {motion control, physics-based character animation, reinforcement learning},
} 
```

**Note** if you use the Factory simulation methods (e.g., SDF collisions, contact reduction) or Factory learning tools (e.g., assets, environments, or controllers) in your work, please cite the following paper:
```
@inproceedings{
	narang2022factory,
	author = {Yashraj Narang and Kier Storey and Iretiayo Akinola and Miles Macklin and Philipp Reist and Lukasz Wawrzyniak and Yunrong Guo and Adam Moravanszky and Gavriel State and Michelle Lu and Ankur Handa and Dieter Fox},
	title = {Factory: Fast contact for robotic assembly},
	booktitle = {Robotics: Science and Systems},
	year = {2022}
} 
```

**Note** if you use the IndustReal training environments or algorithms in your work, please cite the following paper:
```
@inproceedings{
	tang2023industreal,
	author = {Bingjie Tang and Michael A Lin and Iretiayo Akinola and Ankur Handa and Gaurav S Sukhatme and Fabio Ramos and Dieter Fox and Yashraj Narang},
	title = {IndustReal: Transferring contact-rich assembly tasks from simulation to reality},
	booktitle = {Robotics: Science and Systems},
	year = {2023}
}
```

## File tree (depth 3, assets pruned)

```
.gitattributes
.gitignore
.gitlab/
  issue_templates/
    Default.md
.pre-commit-config.yaml
LICENSE.txt
README.md
isaacgymenvs/
  __init__.py
  cfg/
    config.yaml
    pbt/
    task/
    train/
  learning/
    __init__.py
    amp_continuous.py
    amp_datasets.py
    amp_models.py
    amp_network_builder.py
    amp_players.py
    common_agent.py
    common_player.py
    hrl_continuous.py
    hrl_models.py
    replay_buffer.py
  pbt/
    __init__.py
    experiments/
    launcher/
    mutation.py
    pbt.py
  tasks/
    __init__.py
    allegro_hand.py
    allegro_kuka/
    amp/
    ant.py
    anymal.py
    anymal_terrain.py
    ball_balance.py
    base/
    cartpole.py
    dextreme/
    factory/
    franka_cabinet.py
    franka_cube_stack.py
    humanoid.py
    humanoid_amp.py
    industreal/
    ingenuity.py
    quadcopter.py
    shadow_hand.py
    trifinger.py
    utils/
  train.py
  utils/
    __init__.py
    dr_utils.py
    reformat.py
    rlgames_utils.py
    rna_util.py
    torch_jit_utils.py
    utils.py
    wandb_utils.py
setup.py
```

## Config files (92)


### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/codespell-project/codespell
    rev: v2.1.0
    hooks:
      - id: codespell
        args:
          - --ignore-words-list=nd,reacher,thist,ths,magent
          - --skip=assets/**/*

```

### isaacgymenvs/cfg/config.yaml

```yaml

# Task name - used to pick the class to load
task_name: ${task.name}
# experiment name. defaults to name of training config
experiment: ''

# if set to positive integer, overrides the default number of environments
num_envs: ''

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

# RLGames Arguments
# test - if set, run policy in inference mode (requires setting checkpoint to load)
test: False
# used to set checkpoint path
checkpoint: ''
# set sigma when restoring network
sigma: ''
# set to True to use multi-gpu training
multi_gpu: False

wandb_activate: False
wandb_group: ''
wandb_name: ${train.params.config.name}
wandb_entity: ''
wandb_project: 'isaacgymenvs'
wandb_tags: []
wandb_logcode_dir: '' 

capture_video: False
capture_video_freq: 1464
capture_video_len: 100
force_render: True

# disables rendering
headless: False

# set default task and default training config based on task
defaults:
  - task: Ant
  - train: ${task}PPO
  - pbt: no_pbt
  - override hydra/job_logging: disabled
  - _self_

# set the directory where the output files get saved
hydra:
  output_subdir: null
  run:
    dir: .


```

### isaacgymenvs/cfg/pbt/mutation/allegro_hand_mutation.yaml

```yaml
task.env.dist_reward_scale: "mutate_float"
task.env.rot_reward_scale: "mutate_float"
task.env.rot_eps: "mutate_float"
task.env.reach_goal_bonus: "mutate_float"

# Could be additionally mutated
#task.env.actionPenaltyScale: "mutate_float"
#task.env.actionDeltaPenaltyScale: "mutate_float"

#task.env.startObjectPoseDY: "mutate_float"
#task.env.startObjectPoseDZ: "mutate_float"
#task.env.fallDistance: "mutate_float"

train.params.config.learning_rate: "mutate_float"
train.params.config.grad_norm: "mutate_float"
train.params.config.entropy_coef: "mutate_float"
train.params.config.critic_coef: "mutate_float"
train.params.config.bounds_loss_coef: "mutate_float"
train.params.config.kl_threshold: "mutate_float"

train.params.config.e_clip: "mutate_eps_clip"

train.params.config.mini_epochs: "mutate_mini_epochs"

train.params.config.gamma: "mutate_discount"

# These would require special mutation rules
# 'train.params.config.steps_num': 8
# 'train.params.config.minibatch_size': 256

```

### isaacgymenvs/cfg/pbt/mutation/allegro_kuka_mutation.yaml

```yaml
task.env.distRewardScale: "mutate_float"
task.env.rotRewardScale: "mutate_float"
task.env.actionPenaltyScale: "mutate_float"
task.env.liftingRewScale: "mutate_float"
task.env.liftingBonus: "mutate_float"
task.env.liftingBonusThreshold: "mutate_float"
task.env.keypointRewScale: "mutate_float"
task.env.distanceDeltaRewScale: "mutate_float"
task.env.reachGoalBonus: "mutate_float"
task.env.kukaActionsPenaltyScale: "mutate_float"
task.env.allegroActionsPenaltyScale: "mutate_float"
task.env.fallDistance: "mutate_float"

# Could be additionally mutated
#train.params.config.learning_rate: "mutate_float"
#train.params.config.entropy_coef: "mutate_float"  # this is 0, no reason to mutate

train.params.config.grad_norm: "mutate_float"
train.params.config.critic_coef: "mutate_float"
train.params.config.bounds_loss_coef: "mutate_float"
train.params.config.kl_threshold: "mutate_float"

train.params.config.e_clip: "mutate_eps_clip"

train.params.config.mini_epochs: "mutate_mini_epochs"

train.params.config.gamma: "mutate_discount"

# These would require special mutation rules
# 'train.params.config.steps_num': 8
# 'train.params.config.minibatch_size': 256

```

### isaacgymenvs/cfg/pbt/mutation/ant_mutation.yaml

```yaml
task.env.headingWeight: "mutate_float"
task.env.upWeight: "mutate_float"

train.params.config.grad_norm: "mutate_float"
train.params.config.entropy_coef: "mutate_float"
train.params.config.critic_coef: "mutate_float"
train.params.config.bounds_loss_coef: "mutate_float"
train.params.config.kl_threshold: "mutate_float"

train.params.config.e_clip: "mutate_eps_clip"

train.params.config.mini_epochs: "mutate_mini_epochs"

train.params.config.gamma: "mutate_discount"
train.params.config.tau: "mutate_discount"
```

### isaacgymenvs/cfg/pbt/mutation/default_mutation.yaml

```yaml
train.params.config.reward_shaper.scale_value: "mutate_float"
train.params.config.learning_rate: "mutate_float"
train.params.config.grad_norm: "mutate_float"
train.params.config.entropy_coef: "mutate_float"
train.params.config.critic_coef: "mutate_float"
train.params.config.bounds_loss_coef: "mutate_float"

train.params.config.e_clip: "mutate_eps_clip"

train.params.config.mini_epochs: "mutate_mini_epochs"

train.params.config.gamma: "mutate_discount"

```

### isaacgymenvs/cfg/pbt/mutation/humanoid_mutation.yaml

```yaml
task.env.headingWeight: "mutate_float"
task.env.upWeight: "mutate_float"

task.env.fingertipDeltaRewScale: "mutate_float"
task.env.liftingRewScale: "mutate_float"
task.env.liftingBonus: "mutate_float"
task.env.keypointRewScale: "mutate_float"
task.env.reachGoalBonus: "mutate_float"
task.env.kukaActionsPenaltyScale: "mutate_float"
task.env.allegroActionsPenaltyScale: "mutate_float"

train.params.config.reward_shaper.scale_value: "mutate_float"
train.params.config.learning_rate: "mutate_float"
train.params.config.grad_norm: "mutate_float"
train.params.config.entropy_coef: "mutate_float"
train.params.config.critic_coef: "mutate_float"
train.params.config.bounds_loss_coef: "mutate_float"

train.params.config.e_clip: "mutate_eps_clip"

train.params.config.mini_epochs: "mutate_mini_epochs"

train.params.config.gamma: "mutate_discount"

```

### isaacgymenvs/cfg/pbt/no_pbt.yaml

```yaml
enabled: False
```

### isaacgymenvs/cfg/pbt/pbt_default.yaml

```yaml
defaults:
  - mutation: default_mutation

enabled: True

policy_idx: 0  # policy index in a population: should always be specified explicitly! Each run in a population should have a unique idx from [0..N-1]
num_policies: 8  # total number of policies in the population, the total number of learners. Override through CLI!
workspace: "pbt_workspace"  # suffix of the workspace dir name inside train_dir, used to distinguish different PBT runs with the same experiment name. Recommended to specify a unique name

# special mode that enables PBT features for debugging even if only one policy is present. Never enable in actual experiments
dbg_mode: False

# PBT hyperparams
interval_steps: 10000000  # Interval in env steps between PBT iterations (checkpointing, mutation, etc.)
start_after: 10000000  # Start PBT after this many env frames are collected, this applies to all experiment restarts, i.e. when we resume training after the weights are mutated
initial_delay: 20000000  # This is a separate delay for when we're just starting the training session. It makes sense to give policies a bit more time to develop different behaviors

# Fraction of the underperforming policies whose weights are to be replaced by better performing policies
# This is rounded up, i.e. for 8 policies and fraction 0.3 we replace ceil(0.3*8)=3 worst policies
replace_fraction_worst: 0.125

# Fraction of agents used to sample weights from when we replace an underperforming agent
# This is also rounded up
replace_fraction_best: 0.3

# Replace an underperforming policy only if its reward is lower by at least this fraction of standard deviation
# within the population.
replace_threshold_frac_std: 0.5

# Replace an underperforming policy only if its reward is lower by at least this fraction of the absolute value
# of the objective of a better policy
replace_threshold_frac_absolute: 0.05

# Probability to mutate a certain parameter
mutation_rate: 0.15

# min and max values for the mutation of a parameter
# The mutation is performed by multiplying or dividing (randomly) the parameter value by a value sampled from [change_min, change_max]
change_min: 1.1
change_max: 1.5

```

### isaacgymenvs/cfg/task/AllegroHand.yaml

```yaml
# used to create the object
name: AllegroHand

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 600
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 2 # 30 Hz

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  startObjectPoseDY: -0.19
  startObjectPoseDZ: 0.06

  # Random forces applied to the object
  forceScale: 0.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # reward -> dictionary
  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # can be "no_vel", "full_state"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetFileName: "urdf/kuka_allegro_description/allegro_touch_sensor.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: False
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
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

### isaacgymenvs/cfg/task/AllegroHandDextremeADR.yaml

```yaml
# used to create the object
name: AllegroHandADR

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 320 # Not used, but would be 8 sec if resetTime is not set
  resetTime: 8 # Max time till reset, in seconds, if a goal wasn't achieved. Will overwrite the episodeLength if is > 0.
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 50.0
  clipActions: 1.0
  discreteActions: False

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  dofSpeedScale: 20.0

  use_capped_dof_control: False 
  max_dof_radians_per_second: 6.2832 

  max_effort: 0.5

  num_success_hold_steps: 0

  actionsMovingAverage: 
    range: [0.15, 0.2]
    schedule_steps: 1000_000
    #schedule_steps: 300_000
    schedule_freq: 500 # schedule every 500 steps for stability

  controlFrequencyInv: 2 #2 # 30 Hz #3 # 20 Hz

  cubeObsDelayProb: 0.3
  maxObjectSkipObs: 2

  # Action Delay related 
  actionDelayProbMax: 0.3
  actionLatencyMax: 15
  actionLatencyScheduledSteps: 2_000_000

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.03
  resetPositionNoiseZ: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  startObjectPoseDY: -0.15
  startObjectPoseDZ: 0.06

  # Random forces applied to the object
  forceScale: 2.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # Random Adversarial Perturbations
  random_network_adversary:
    enable: True
    # prob: 0.30
    weight_sample_freq: 1000 # steps 

  random_cube_observation:
    enable: True 
    prob: 0.3

  # reward -> dictionary
  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.001
  actionDeltaPenaltyScale: -0.2 #-0.01
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "no_vel" #"full_state" # can be "no_vel", "full_state"
  asymmetric_observations: True
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 50

  asset:
    assetFileName: "urdf/kuka_allegro_description/allegro_touch_sensor.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: True
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations

    sim_params:
      gravity:
        range: [0, 0.6]
        operation: "additive"
        distribution: "gaussian"

    actor_params:
      hand:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        color: True
        dof_properties:
          damping: 
            range: [0.01, 20.0]
            operation: "scaling"
            distribution: "loguniform"
          stiffness:
            range: [0.01, 20.0]
            operation: "scaling"
            distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          effort:
            range: [0.4, 10.0]
            operation: "scaling"
            distribution: "uniform"
          friction:
            range: [0.0, 10.0]
            operation: "scaling"
            distribution: "uniform"
          armature:
            range: [0.0, 10.0]
            operation: "scaling"
            distribution: "uniform"
          lower:
            # range: [0, 0.01]
            # operation: "additive"
            # distribution: "gaussian"
            range: [-5.0, 5.0]
            operation: "additive"
            distribution: "uniform"
          upper:
            # range: [0, 0.01]
            # operation: "additive"
            # distribution: "gaussian"
            range: [-5.0, 5.0]
            operation: "additive"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

        rigid_body_properties:
          mass:
            # range: [0.5, 2.0]
            # range: [0.5, 1.5]
            range: [0.4, 1.6] # change when runtime API is available
            operation: "scaling"
            distribution: "uniform"
            setup_only: False # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

        rigid_shape_properties:
          friction:
            num_buckets: 250
            # range: [0.2, 1.2] #[0.7, 1.3]
            range: [0.01, 2.0]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          restitution:
            num_buckets: 100
            range: [0.0, 0.5]
            operation: "additive"
            distribution: "uniform"

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
            # range: [0.5, 1.5]
            range: [0.3, 1.7] # after fixing the API expand it even more
            operation: "scaling"
            distribution: "uniform"
            setup_only: False # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

        rigid_shape_properties:
          friction:
            # num_buckets: 250
            # range: [0.2, 1.2] #[0.7, 1.3]
            # operation: "scaling"
            # distribution: "uniform"
            num_buckets: 250
            range: [0.01, 2.0]
            operation: "scaling"
            distribution: "uniform"
            # distribution: "loguniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          restitution:
            num_buckets: 100
            range: [0.0, 0.5]
            operation: "additive"
            distribution: "uniform"

  adr:

    use_adr: True

    # set to false to not do update ADR ranges. useful for evaluation or training a base policy
    update_adr_ranges: True 
    clear_other_queues: False

    # if set, boundary sampling and performance eval will occur at (bound + delta) instead of at bound.
    adr_extended_boundary_sample: False

    worker_adr_boundary_fraction: 0.4 # fraction of workers dedicated to measuring perf of ends of ADR r
```

### isaacgymenvs/cfg/task/AllegroHandDextremeManualDR.yaml

```yaml
# used to create the object
name: AllegroHandManualDR

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 320 # Not used, but would be 8 sec if resetTime is not set
  resetTime: 8 # Max time till reset, in seconds, if a goal wasn't achieved. Will overwrite the episodeLength if is > 0.
  enableDebugVis: False
  aggregateMode: 1

  #clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  dofSpeedScale: 20.0

  use_capped_dof_control: False 
  max_dof_radians_per_second: 3.1415


  # This is to generate correct random goals 
  apply_random_quat: True 

  actionsMovingAverage: 
    range: [0.15, 0.35]
    schedule_steps: 1000_000
    schedule_freq: 500 # schedule every 500 steps for stability

  controlFrequencyInv: 2 #2 # 30 Hz #3 # 20 Hz

  cubeObsDelayProb: 0.3
  maxObjectSkipObs: 2

  # Action Delay related 
  # right now the schedule steps are so big that
  # it virtually never changes the latency
  # our best seed came out of this config file 
  # so for now keeping it as it is, will look into it in future
  actionDelayProbMax: 0.3
  actionLatencyMax: 15
  actionLatencyScheduledSteps: 10_000_000


  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.03
  resetPositionNoiseZ: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.5
  resetDofVelRandomInterval: 0.0

  startObjectPoseDY: -0.19
  startObjectPoseDZ: 0.06

  # Random forces applied to the object
  forceScale: 2.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # Random Adversarial Perturbations
  random_network_adversary:
    enable: True
    prob: 0.15
    weight_sample_freq: 1000 # steps 

  # Provide random cube observations to model pose jumps in the real
  random_cube_observation:
    enable: True 
    prob: 0.3

  # reward -> dictionary
  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0001
  actionDeltaPenaltyScale: -0.01
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "no_vel" #"full_state" # can be "no_vel", "full_state"
  asymmetric_observations: True
  successTolerance: 0.4
  printNumSuccesses: False
  maxConsecutiveSuccesses: 50

  asset:
    assetFileName: "urdf/kuka_allegro_description/allegro_touch_sensor.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: True
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
    # There is a hidden variable `apply_white_noise_prob` which is set to 0.5
    # so that the observation noise is added only 50% of the time.
      dof_pos:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      object_pose_cam:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      goal_pose:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      goal_relative_rot_cam:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      last_actions:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .02] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params:
      gravity:
        range: [0, 0.5]
        operation: "additive"
        distribution: "gaussian"

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
            range: [0.5, 2.0]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:

          friction:
            num_buckets: 250
            range: [0.2, 1.2] #[0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000

          restitution:
            num_buckets: 100
            range: [0.0, 0.4]
            operation: "additive"
            distribution: "uniform"

          
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps
```

### isaacgymenvs/cfg/task/AllegroHandFF.yaml

```yaml
defaults:
  - AllegroHandLSTM
  - _self_
```

### isaacgymenvs/cfg/task/AllegroHandLSTM.yaml

```yaml
# used to create the object
name: AllegroHand

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 320 # Not used, but would be 8 sec if resetTime is not set
  resetTime: 16 # Max time till reset, in seconds, if a goal wasn't achieved. Will overwrite the episodeLength if is > 0.
  enableDebugVis: False
  aggregateMode: 1

  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
  dofSpeedScale: 20.0

  use_capped_dof_control: False 
  max_dof_radians_per_second: 3.1415

  # This is to generate correct random goals 
  apply_random_quat: False 

  actionsMovingAverage: 
    range: [0.15, 0.35]
    schedule_steps: 1000_000
    #schedule_steps: 300_000
    schedule_freq: 500 # schedule every 500 steps for stability

  controlFrequencyInv: 2 #2 # 30 Hz #3 # 20 Hz

  cubeObsDelayProb: 0.3
  maxObjectSkipObs: 2

  # Action Delay related 
  # right now the schedule steps are so big that
  # it virtually never changes the latency
  # our best seed came out of this config file 
  # so for now keeping it as it is, will look into it in future
  actionDelayProbMax: 0.3
  actionLatencyMax: 15
  actionLatencyScheduledSteps: 10_000_000

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.03
  resetPositionNoiseZ: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.5
  resetDofVelRandomInterval: 0.0

  startObjectPoseDY: -0.19
  startObjectPoseDZ: 0.06

  # Random forces applied to the object
  forceScale: 2.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  # Random Adversarial Perturbations
  random_network_adversary:
    enable: True
    prob: 0.15
    weight_sample_freq: 1000 # steps 

  # Provide random cube observations to model pose jumps in the real
  random_cube_observation:
    enable: True 
    prob: 0.3

  # reward -> dictionary
  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0001
  actionDeltaPenaltyScale: -0.01
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "no_vel" #"full_state" # can be "no_vel", "full_state"
  asymmetric_observations: True
  successTolerance: 0.4
  printNumSuccesses: False
  maxConsecutiveSuccesses: 50

  asset:
    assetFileName: "urdf/kuka_allegro_description/allegro.urdf"
    # assetFileNameBlock: "urdf/objects/cube_multicolor_dextreme.urdf"
    # assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: True
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
    # There is a hidden variable `apply_white_noise_prob` which is set to 0.5
    # so that the observation noise is added only 50% of the time.
      dof_pos:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      object_pose_cam:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      goal_pose:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      goal_relative_rot_cam:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
      last_actions:
        range: [0, .005] # range for the white noise
        range_correlated: [0, .01 ] # range for correlated noise, refreshed with freq `frequency`
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
        # schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .02] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      # schedule_steps: 40000
    sim_params:
      gravity:
        range: [0, 0.5]
        operation: "additive"
        distribution: "gaussian"
        # schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        # schedule_steps: 40000
        #rest_offset:
        #range: [0, 0.007]
        #operation: "additive"
        #distribution: "uniform"
        #schedule: "linear"
        #schedule_steps: 6000
    actor_params:
      hand:
        # scale:
        #   range: [0.95, 1.05]
        #   operation: "scaling"
        #   distribution: "uniform"
        #   setup_only: True         

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
            range: [0.5, 2.0]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.2, 1.2] #[0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            # schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            # schedule_steps: 30000
          restitution:
            n
```

### isaacgymenvs/cfg/task/AllegroHandLSTM_Big.yaml

```yaml
defaults:
  - AllegroHandLSTM
  - _self_


```

### isaacgymenvs/cfg/task/AllegroKuka.yaml

```yaml
defaults:
  - _self_
  - env: reorientation

name: AllegroKuka

physics_engine: ${..physics_engine}

env:
  subtask: ""

  # if given, will override the device setting in gym.
  numEnvs: ${resolve_default:8192,${...num_envs}}

  envSpacing: 1.2
  episodeLength: 600
  enableDebugVis: False
  evalStats: False  # extra evaluation-time statistics

  clampAbsObservations: 10.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 10.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  resetPositionNoiseX: 0.1
  resetPositionNoiseY: 0.1
  resetPositionNoiseZ: 0.02
  resetRotationNoise: 1.0
  resetDofPosRandomIntervalFingers: 0.1
  resetDofPosRandomIntervalArm: 0.1
  resetDofVelRandomInterval: 0.5

  # Random forces applied to the object
  forceScale: 2.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  liftingRewScale: 20.0
  liftingBonus: 300.0
  liftingBonusThreshold: 0.15  # when the object is lifted this distance (in meters) above the table, the agent gets the lifting bonus
  keypointRewScale: 200.0
  distanceDeltaRewScale: 50.0
  reachGoalBonus: 1000.0
  kukaActionsPenaltyScale: 0.003
  allegroActionsPenaltyScale: 0.0003
  fallDistance: 0.24
  fallPenalty: 0.0

  privilegedActions: False
  privilegedActionsTorque: 0.02

  # Physics v1, pretty much default settings we used from the start of the project
  dofFriction: -1.0  # negative values are ignored and the default friction from URDF file is used

  # gain of PD controller (?)
  allegroStiffness: 40.0
  kukaStiffness: 40.0

  allegroEffort: 0.35  # this is what was used in sim-to-real experiment. Motor torque in Newton*meters
  kukaEffort: [300, 300, 300, 300, 300, 300, 300]  # see Physics v2

  allegroDamping: 5.0
  kukaDamping: 5.0

  allegroArmature: 0
  kukaArmature: 0

  keypointScale: 1.5
  objectBaseSize: 0.05

  randomizeObjectDimensions: True
  withSmallCuboids: True
  withBigCuboids: True
  withSticks: True

  objectType: "block"
  observationType: "full_state"
  successTolerance: 0.075
  targetSuccessTolerance: 0.01
  toleranceCurriculumIncrement: 0.9  # multiplicative
  toleranceCurriculumInterval: 3000  # in env steps across all agents, with 8192 this is 3000 * 8192 = 24.6M env steps
  maxConsecutiveSuccesses: 50
  successSteps: 1  # how many steps we should be within the tolerance before we declare a success

  saveStates: False
  saveStatesFile: "rootTensorsDofStates.bin"

  loadInitialStates: False
  loadStatesFile: "rootTensorsDofStates.bin"

  asset:
    # Whis was the original kuka_allegro asset.
    # This URDF has some issues, i.e. weights of fingers are too high and the mass of the Allegro hand is too
    # high in general. But in turn this leads to smoother movements and better looking behaviors.
    # Additionally, collision shapes of fingertips are more primitive (just rough convex hulls), which
    # gives a bit more FPS.
    kukaAllegro: "urdf/kuka_allegro_description/kuka_allegro_touch_sensor.urdf"

    # This is the URDF which has more accurate collision shapes and weights.
    # I believe since the hand is much lighter, the policy has more control over the movement of both arm and
    # fingers which leads to faster training (better sample efficiency). But overall the resulting
    # behaviors look too fast and a bit unrealistic.
    # For sim-to-real experiments this needs to be addressed. Overall, v2 is a "Better" URDF, and it should not
    # lead to behaviors that would be worse for sim-to-real experiments. Most likely the problem is elsewhere,
    # for example the max torques might be too high, or the armature of the motors is too low.
    # The exercise of finding the right URDF and other parameters is left for the sim-to-real part of the project.
    # kukaAllegro: "urdf/kuka_allegro_description/kuka_allegro_v2.urdf"

    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"

task:
  randomize: False
  randomization_params:
    frequency: 480   # Define how many simulation steps between generating new randomizations

    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000

    sim_params:
    gravity:
      range: [0, 0.4]
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000

    actor_params:
      allegro:
        color: True
        dof_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.5, 2.0]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 1
        rigid_body_properties:
          mass:
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  dt: 0.01667 # 1/60
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  num_client_threads: 8

  gravity: [0.0, 0.0, 
```

### isaacgymenvs/cfg/task/AllegroKukaLSTM.yaml

```yaml
defaults:
  - AllegroKuka
  - _self_
```

### isaacgymenvs/cfg/task/AllegroKukaTwoArmsLSTM.yaml

```yaml
defaults:
  - AllegroKukaLSTM
  - _self_

name: AllegroKukaTwoArms

env:
  numArms: 2

  envSpacing: 1.75

  # two arms essentially need to throw the object to each other
  # training is much harder with random forces, so we disable it here as we do for the throw task
  # forceScale: 0.0

  armXOfs: 1.1  # distance from the center of the table, distance between arms is 2x this
  armYOfs: 0.0

```

### isaacgymenvs/cfg/task/Ant.yaml

```yaml
# used to create the object
name: Ant

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 1000
  enableDebugVis: False

  clipActions: 1.0

  powerScale: 1.0
  controlFrequencyInv: 1 # 60 Hz

  # reward parameters
  headingWeight: 0.5
  upWeight: 0.1

  # cost parameters
  actionsCost: 0.005
  energyCost: 0.05
  dofVelocityScale: 0.2
  contactForceScale: 0.1
  jointsAtLimitCost: 0.1
  deathCost: -2.0
  terminationHeight: 0.31

  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

  asset:
    assetFileName: "mjcf/nv_ant.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 10.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    # specify which attributes to randomize for each actor type and property
    frequency: 600   # Define how many environment steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      operation: "additive"
      distribution: "gaussian"
    actions:
      range: [0., .02]
      operation: "additive"
      distribution: "gaussian"
    actor_params:
      ant:
        color: True
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
        dof_properties:
          damping: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
          stiffness: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"

```

### isaacgymenvs/cfg/task/AntSAC.yaml

```yaml
# used to create the object
defaults:
  - Ant
  - _self_

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:64,${...num_envs}}
```

### isaacgymenvs/cfg/task/Anymal.yaml

```yaml
# used to create the object
name: Anymal

physics_engine: ${..physics_engine}

env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 4.  # [m]

  clipObservations: 5.0
  clipActions: 1.0

  plane:
    staticFriction: 1.0  # [-]
    dynamicFriction: 1.0  # [-]
    restitution: 0.        # [-]

  baseInitState:
    pos: [0.0, 0.0, 0.62] # x,y,z [m]
    rot: [0.0, 0.0, 0.0, 1.0] # x,y,z,w [quat]
    vLinear: [0.0, 0.0, 0.0]  # x,y,z [m/s]
    vAngular: [0.0, 0.0, 0.0]  # x,y,z [rad/s]

  randomCommandVelocityRanges:
    linear_x: [-2., 2.] # min max [m/s]
    linear_y: [-1., 1.]   # min max [m/s]
    yaw: [-1., 1.]          # min max [rad/s]

  control:
    # PD Drive parameters:
    stiffness: 85.0  # [N*m/rad]
    damping: 2.0     # [N*m*s/rad]
    actionScale: 0.5
    controlFrequencyInv: 1 # 60 Hz

  defaultJointAngles:  # = target angles when action = 0.0
    LF_HAA: 0.03    # [rad]
    LH_HAA: 0.03    # [rad]
    RF_HAA: -0.03   # [rad]
    RH_HAA: -0.03   # [rad]

    LF_HFE: 0.4     # [rad]
    LH_HFE: -0.4    # [rad]
    RF_HFE: 0.4     # [rad]
    RH_HFE: -0.4    # [rad]

    LF_KFE: -0.8    # [rad]
    LH_KFE: 0.8     # [rad]
    RF_KFE: -0.8    # [rad]
    RH_KFE: 0.8     # [rad]

  urdfAsset:
    collapseFixedJoints: True
    fixBaseLink: False
    defaultDofDriveMode: 4 # see GymDofDriveModeFlags (0 is none, 1 is pos tgt, 2 is vel tgt, 4 effort)

  learn:
    # rewards
    linearVelocityXYRewardScale: 1.0
    angularVelocityZRewardScale: 0.5
    torqueRewardScale: -0.000025 

    # normalization
    linearVelocityScale: 2.0
    angularVelocityScale: 0.25
    dofPositionScale: 1.0
    dofVelocityScale: 0.05

    # episode length in seconds
    episodeLength_s: 50

  # viewer cam:
  viewer:
    refEnv: 0
    pos: [0, 0, 4]  # [m]
    lookat: [1., 1, 3.3]  # [m]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.02
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 1
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 100.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many environment steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      operation: "additive"
      distribution: "gaussian"
    actions:
      range: [0., .02]
      operation: "additive"
      distribution: "gaussian"
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 3000
    actor_params:
      anymal:
        color: True
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
            schedule_steps: 3000
        rigid_shape_properties:
          friction:
            num_buckets: 500
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          restitution:
            range: [0., 0.7]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
        dof_properties:
          damping: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          stiffness: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000

```

### isaacgymenvs/cfg/task/AnymalTerrain.yaml

```yaml
# used to create the object
name: AnymalTerrain

physics_engine: 'physx'

env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  numObservations: 188
  numActions: 12
  envSpacing: 3.  # [m]
  enableDebugVis: False

  terrain:
    terrainType: trimesh # none, plane, or trimesh
    staticFriction: 1.0  # [-]
    dynamicFriction: 1.0  # [-]
    restitution: 0.        # [-]
    # rough terrain only:
    curriculum: true
    maxInitMapLevel: 0
    mapLength: 8.
    mapWidth: 8.
    numLevels: 10
    numTerrains: 20
    # terrain types: [smooth slope, rough slope, stairs up, stairs down, discrete]
    terrainProportions: [0.1, 0.1, 0.35, 0.25, 0.2]
    # tri mesh only:
    slopeTreshold: 0.5

  baseInitState:
    pos: [0.0, 0.0, 0.62] # x,y,z [m]
    rot: [0.0, 0.0, 0.0, 1.0] # x,y,z,w [quat]
    vLinear: [0.0, 0.0, 0.0]  # x,y,z [m/s]
    vAngular: [0.0, 0.0, 0.0]  # x,y,z [rad/s]

  randomCommandVelocityRanges:
    # train
    linear_x: [-1., 1.] # min max [m/s]
    linear_y: [-1., 1.]   # min max [m/s]
    yaw: [-3.14, 3.14]    # min max [rad/s]

  control:
    # PD Drive parameters:
    stiffness: 80.0  # [N*m/rad]
    damping: 2.0     # [N*m*s/rad]
    # action scale: target angle = actionScale * action + defaultAngle
    actionScale: 0.5
    # decimation: Number of control action updates @ sim DT per policy DT
    decimation: 4

  defaultJointAngles:  # = target angles when action = 0.0
    LF_HAA: 0.03    # [rad]
    LH_HAA: 0.03    # [rad]
    RF_HAA: -0.03   # [rad]
    RH_HAA: -0.03   # [rad]

    LF_HFE: 0.4     # [rad]
    LH_HFE: -0.4    # [rad]
    RF_HFE: 0.4     # [rad]
    RH_HFE: -0.4    # [rad]

    LF_KFE: -0.8    # [rad]
    LH_KFE: 0.8     # [rad]
    RF_KFE: -0.8    # [rad]
    RH_KFE: 0.8     # [rad]

  urdfAsset:
    file: "urdf/anymal_c/urdf/anymal_minimal.urdf"
    footName: SHANK # SHANK if collapsing fixed joint, FOOT otherwise
    kneeName: THIGH
    collapseFixedJoints: True
    fixBaseLink: false
    defaultDofDriveMode: 4 # see GymDofDriveModeFlags (0 is none, 1 is pos tgt, 2 is vel tgt, 4 effort)

  learn:
    allowKneeContacts: true
    # rewards
    terminalReward: 0.0
    linearVelocityXYRewardScale: 1.0
    linearVelocityZRewardScale: -4.0
    angularVelocityXYRewardScale: -0.05
    angularVelocityZRewardScale: 0.5
    orientationRewardScale: -0. #-1.
    torqueRewardScale: -0.00002 # -0.000025
    jointAccRewardScale: -0.0005 # -0.0025
    baseHeightRewardScale: -0.0 #5
    feetAirTimeRewardScale:  1.0
    kneeCollisionRewardScale: -0.25 
    feetStumbleRewardScale: -0. #-2.0
    actionRateRewardScale: -0.01
    # cosmetics
    hipRewardScale: -0. #25

    # normalization
    linearVelocityScale: 2.0
    angularVelocityScale: 0.25
    dofPositionScale: 1.0
    dofVelocityScale: 0.05
    heightMeasurementScale: 5.0

    # noise 
    addNoise: true
    noiseLevel: 1.0 # scales other values
    dofPositionNoise: 0.01
    dofVelocityNoise: 1.5
    linearVelocityNoise: 0.1
    angularVelocityNoise: 0.2
    gravityNoise: 0.05
    heightMeasurementNoise: 0.06

    #randomization
    randomizeFriction: true
    frictionRange: [0.5, 1.25]
    pushRobots: true
    pushInterval_s: 15

    # episode length in seconds
    episodeLength_s: 20

  # viewer cam:
  viewer:
    refEnv: 0
    pos: [0, 0, 10]  # [m]
    lookat: [1., 1, 9]  # [m]

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.005
  substeps: 1
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 1
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 100.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False

```

### isaacgymenvs/cfg/task/BallBalance.yaml

```yaml
# used to create the object
name: BallBalance

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 2.0
  maxEpisodeLength: 500
  actionSpeedScale: 20
  enableDebugVis: False

  clipObservations: 5.0
  clipActions: 1.0

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.01
  substeps: 1
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.001
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)
task:
  randomize: False

```

### isaacgymenvs/cfg/task/Cartpole.yaml

```yaml
# used to create the object
name: Cartpole

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym. 
env:
  numEnvs: ${resolve_default:512,${...num_envs}}
  envSpacing: 4.0
  resetDist: 3.0
  maxEffort: 400.0

  clipObservations: 5.0
  clipActions: 1.0

  asset:
    assetRoot: "../../assets"
    assetFileName: "urdf/cartpole.urdf"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.001
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 100.0
    default_buffer_size_multiplier: 2.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False

```

### isaacgymenvs/cfg/task/FactoryBase.yaml

```yaml
# See schema in factory_schema_config_base.py for descriptions of parameters.

defaults:
    - _self_
    #- /factory_schema_config_base

mode:
    export_scene: False
    export_states: False

sim:
    dt: 0.016667
    substeps: 2
    up_axis: "z"
    use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
    gravity: [0.0, 0.0, -9.81]
    add_damping: True

    physx:
        solver_type: ${....solver_type}
        num_threads: ${....num_threads}
        num_subscenes: ${....num_subscenes}
        use_gpu: ${contains:"cuda",${....sim_device}}

        num_position_iterations: 16
        num_velocity_iterations: 0
        contact_offset: 0.005
        rest_offset: 0.0
        bounce_threshold_velocity: 0.2
        max_depenetration_velocity: 5.0
        friction_offset_threshold: 0.01
        friction_correlation_distance: 0.00625

        max_gpu_contact_pairs: 1048576  # 1024 * 1024
        default_buffer_size_multiplier: 8.0
        contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

env:
    env_spacing: 0.5
    franka_depth: 0.5
    table_height: 0.4
    franka_friction: 1.0
    table_friction: 0.3

```

### isaacgymenvs/cfg/task/FactoryEnvGears.yaml

```yaml
# See schema in factory_schema_config_env.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    - /factory_schema_config_env

sim:
    disable_franka_collisions: False

env:
    env_name: 'FactoryEnvGears'

    tight_or_loose: loose  # use assets with loose (maximal clearance) or tight (minimal clearance) shafts
    gears_lateral_offset: 0.1  # Y-axis offset of gears before initial reset to prevent initial interpenetration with base plate
    gears_density: 1000.0  # density of gears
    base_density: 2700.0  # density of base plate
    gears_friction: 0.3  # coefficient of friction associated with gears
    base_friction: 0.3  # coefficient of friction associated with base plate

```

### isaacgymenvs/cfg/task/FactoryEnvInsertion.yaml

```yaml
# See schema in factory_schema_config_env.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    - /factory_schema_config_env

sim:
    disable_franka_collisions: False

env:
    env_name: 'FactoryEnvInsertion'

    desired_subassemblies: ['round_peg_hole_4mm_loose', 
                            'round_peg_hole_8mm_loose', 
                            'round_peg_hole_12mm_loose', 
                            'round_peg_hole_16mm_loose',
                            'rectangular_peg_hole_4mm_loose', 
                            'rectangular_peg_hole_8mm_loose', 
                            'rectangular_peg_hole_12mm_loose', 
                            'rectangular_peg_hole_16mm_loose']
    plug_lateral_offset: 0.1  # Y-axis offset of plug before initial reset to prevent initial interpenetration with socket

    # Subassembly options:
    # {round_peg_hole_4mm_tight, round_peg_hole_4mm_loose,
    # round_peg_hole_8mm_tight, round_peg_hole_8mm_loose,
    # round_peg_hole_12mm_tight, round_peg_hole_12mm_loose,
    # round_peg_hole_16mm_tight, round_peg_hole_16mm_loose,
    # rectangular_peg_hole_4mm_tight, rectangular_peg_hole_4mm_loose,
    # rectangular_peg_hole_8mm_tight, rectangular_peg_hole_8mm_loose,
    # rectangular_peg_hole_12mm_tight, rectangular_peg_hole_12mm_loose,
    # rectangular_peg_hole_16mm_tight, rectangular_peg_hole_16mm_loose,
    # bnc, dsub, usb}
    #
    # NOTE: BNC, D-sub, and USB are currently unavailable while we await approval from manufacturers.

```

### isaacgymenvs/cfg/task/FactoryEnvNutBolt.yaml

```yaml
# See schema in factory_schema_config_env.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    - /factory_schema_config_env

sim:
    disable_franka_collisions: False

    disable_nut_collisions: False
    disable_bolt_collisions: False

env:
    env_name: 'FactoryEnvNutBolt'

    desired_subassemblies: ['nut_bolt_m16_tight', 'nut_bolt_m16_loose']
    nut_lateral_offset: 0.1  # Y-axis offset of nut before initial reset to prevent initial interpenetration with bolt
    nut_bolt_density: 7850.0
    nut_bolt_friction: 0.3

    # Subassembly options:
    # {nut_bolt_m4_tight, nut_bolt_m4_loose,
    # nut_bolt_m8_tight, nut_bolt_m8_loose,
    # nut_bolt_m12_tight, nut_bolt_m12_loose,
    # nut_bolt_m16_tight, nut_bolt_m16_loose,
    # nut_bolt_m20_tight, nut_bolt_m20_loose}
```

### isaacgymenvs/cfg/task/FactoryTaskGears.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    # - /factory_schema_config_task

name: FactoryTaskGears
physics_engine: ${..physics_engine}

env:
    numEnvs: ${resolve_default:128,${...num_envs}}
    numObservations: 32
    numActions: 12

randomize:
    joint_noise: 0.0  # noise on Franka DOF positions [deg]
    initial_state: random  # initialize gears in random state or goal state {random, goal}
    gears_bias_y: -0.1  # if random, Y-axis offset of gears during each reset to prevent initial interpenetration with base plate
    gears_bias_z: 0.0  # if random, Z-axis offset of gears during each reset to prevent initial interpenetration with ground plane
    gears_noise_xy: 0.05  # if random, XY-axis noise on gears during each reset

rl:
    max_episode_length: 1024

```

### isaacgymenvs/cfg/task/FactoryTaskInsertion.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    # - /factory_schema_config_task

name: FactoryTaskInsertion
physics_engine: ${..physics_engine}

env:
    numEnvs: ${resolve_default:128,${...num_envs}}
    numObservations: 32
    numActions: 12

randomize:
    joint_noise: 0.0  # noise on Franka DOF positions [deg]
    initial_state: random  # initialize plugs in random state or goal state {random, goal}
    plug_bias_y: -0.1  # if random, Y-axis offset of plug during each reset to prevent initial interpenetration with socket
    plug_bias_z: 0.0  # if random, Z-axis offset of plug during each reset to prevent initial interpenetration with ground plane
    plug_noise_xy: 0.05  # if random, XY-axis noise on plug position during each reset

rl:
    max_episode_length: 1024

```

### isaacgymenvs/cfg/task/FactoryTaskNutBoltPick.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    # - /factory_schema_config_task

name: FactoryTaskNutBoltPick
physics_engine: ${..physics_engine}

sim:
    disable_gravity: False

env:
    numEnvs: ${resolve_default:128,${...num_envs}}
    numObservations: 20
    numActions: 12

    close_and_lift: True  # close gripper and lift after last step of episode
    num_gripper_move_sim_steps: 20  # number of timesteps to reserve for moving gripper before first step of episode
    num_gripper_close_sim_steps: 25  # number of timesteps to reserve for closing gripper after last step of episode
    num_gripper_lift_sim_steps: 25  # number of timesteps to reserve for lift after last step of episode

randomize:
    franka_arm_initial_dof_pos: [0.3413, -0.8011, -0.0670, -1.8299,  0.0266,  1.0185,  1.0927]
    fingertip_midpoint_pos_initial: [0.0, -0.2, 0.2]  # initial position of hand above table
    fingertip_midpoint_pos_noise: [0.2, 0.2, 0.1]  # noise on hand position
    fingertip_midpoint_rot_initial: [3.1416, 0, 3.1416]  # initial rotation of fingertips (Euler)
    fingertip_midpoint_rot_noise: [0.3, 0.3, 1]  # noise on rotation
    nut_pos_xy_initial: [0.0, -0.3]  # initial XY position of nut on table
    nut_pos_xy_initial_noise: [0.1, 0.1]  # noise on nut position
    bolt_pos_xy_initial: [0.0, 0.0]  # initial position of bolt on table
    bolt_pos_xy_noise: [0.1, 0.1]  # noise on bolt position

rl:
    pos_action_scale: [0.1, 0.1, 0.1]
    rot_action_scale: [0.1, 0.1, 0.1]
    force_action_scale: [1.0, 1.0, 1.0]
    torque_action_scale: [1.0, 1.0, 1.0]

    clamp_rot: True
    clamp_rot_thresh: 1.0e-6

    num_keypoints: 4  # number of keypoints used in reward
    keypoint_scale: 0.5  # length of line of keypoints

    keypoint_reward_scale: 1.0  # scale on keypoint-based reward
    action_penalty_scale: 0.0  # scale on action penalty

    max_episode_length: 100

    success_bonus: 0.0  # bonus if nut has been lifted

ctrl:
    ctrl_type: joint_space_id  # {gym_default,
                               #  joint_space_ik, joint_space_id, 
                               #  task_space_impedance, operational_space_motion, 
                               #  open_loop_force, closed_loop_force,
                               #  hybrid_force_motion}
    all:
        jacobian_type: geometric
        gripper_prop_gains: [50, 50]
        gripper_deriv_gains: [2, 2]
    gym_default:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [20, 20]
    joint_space_ik:
        ik_method: dls
        joint_prop_gains: [1, 1, 1, 1, 1, 1, 1]
        joint_deriv_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    joint_space_id:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
    task_space_impedance:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
    operational_space_motion:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [1, 1, 1, 1, 1, 1]
        task_deriv_gains: [1, 1, 1, 1, 1, 1]
    open_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
    closed_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    hybrid_force_motion:
        motion_ctrl_axes: [1, 1, 0, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
```

### isaacgymenvs/cfg/task/FactoryTaskNutBoltPlace.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    # - /factory_schema_config_task

name: FactoryTaskNutBoltPlace
physics_engine: ${..physics_engine}

sim:
    disable_gravity: True

env:
    numEnvs: ${resolve_default:128,${...num_envs}}
    numObservations: 27
    numActions: 12

    num_gripper_move_sim_steps: 40  # number of timesteps to reserve for moving gripper before first step of episode
    num_gripper_close_sim_steps: 50  # number of timesteps to reserve for closing gripper onto nut during each reset

randomize:
    franka_arm_initial_dof_pos: [0.00871, -0.10368, -0.00794, -1.49139, -0.00083,  1.38774,  0.7861]
    fingertip_midpoint_pos_initial: [0.0, 0.0, 0.2]  # initial position of midpoint between fingertips above table
    fingertip_midpoint_pos_noise: [0.2, 0.2, 0.1]  # noise on fingertip pos
    fingertip_midpoint_rot_initial: [3.1416, 0, 3.1416]  # initial rotation of fingertips (Euler)
    fingertip_midpoint_rot_noise: [0.3, 0.3, 1]  # noise on rotation
    nut_noise_pos_in_gripper: [0.0, 0.0, 0.01]  # noise on nut position within gripper
    nut_noise_rot_in_gripper: 0.0  # noise on nut rotation within gripper
    bolt_pos_xy_initial: [0.0, 0.0]  # initial XY position of nut on table
    bolt_pos_xy_noise: [0.1, 0.1]  # noise on nut position

rl:
    pos_action_scale: [0.1, 0.1, 0.1]
    rot_action_scale: [0.1, 0.1, 0.1]
    force_action_scale: [1.0, 1.0, 1.0]
    torque_action_scale: [1.0, 1.0, 1.0]

    clamp_rot: True
    clamp_rot_thresh: 1.0e-6

    add_obs_bolt_tip_pos: False  # add observation of bolt tip position

    num_keypoints: 4  # number of keypoints used in reward
    keypoint_scale: 0.5  # length of line of keypoints

    keypoint_reward_scale: 1.0  # scale on keypoint-based reward
    action_penalty_scale: 0.0  # scale on action penalty

    max_episode_length: 200

    close_error_thresh: 0.1  # threshold below which nut is considered close enough to bolt
    success_bonus: 0.0  # bonus if nut is close enough to bolt

ctrl:
    ctrl_type: joint_space_id  # {gym_default,
                               #  joint_space_ik, joint_space_id, 
                               #  task_space_impedance, operational_space_motion, 
                               #  open_loop_force, closed_loop_force,
                               #  hybrid_force_motion}
    all:
        jacobian_type: geometric
        gripper_prop_gains: [100, 100]
        gripper_deriv_gains: [2, 2]
    gym_default:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [20, 20]
    joint_space_ik:
        ik_method: dls
        joint_prop_gains: [1, 1, 1, 1, 1, 1, 1]
        joint_deriv_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    joint_space_id:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
    task_space_impedance:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
    operational_space_motion:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [1, 1, 1, 1, 1, 1]
        task_deriv_gains: [1, 1, 1, 1, 1, 1]
    open_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
    closed_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    hybrid_force_motion:
        motion_ctrl_axes: [1, 1, 0, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


```

### isaacgymenvs/cfg/task/FactoryTaskNutBoltScrew.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - FactoryBase
    - _self_
    # - /factory_schema_config_task

name: FactoryTaskNutBoltScrew
physics_engine: ${..physics_engine}

sim:
    disable_gravity: False

env:
    numEnvs: ${resolve_default:128,${...num_envs}}
    numObservations: 32
    numActions: 12

randomize:
    franka_arm_initial_dof_pos: [1.5178e-03, -1.9651e-01, -1.4364e-03, -1.9761e+00, -2.7717e-04, 1.7796e+00, 7.8556e-01]
    nut_rot_initial: 30.0  # initial rotation of nut from configuration in CAD [deg]; default = 30.0 (gripper aligns with flat surfaces of nut)

rl:
    pos_action_scale: [0.1, 0.1, 0.1]
    rot_action_scale: [0.1, 0.1, 0.1]
    force_action_scale: [1.0, 1.0, 1.0]
    torque_action_scale: [1.0, 1.0, 1.0]

    unidirectional_rot: True  # constrain Franka Z-rot to be unidirectional
    unidirectional_force: False  # constrain Franka Z-force to be unidirectional (useful for debugging)

    clamp_rot: True
    clamp_rot_thresh: 1.0e-6

    add_obs_finger_force: False  # add observations of force on left and right fingers

    keypoint_reward_scale: 1.0  # scale on keypoint-based reward
    action_penalty_scale: 0.0  # scale on action penalty

    max_episode_length: 8192  # terminate episode after this number of timesteps (failure)

    far_error_thresh: 0.100  # threshold above which nut is considered too far from bolt
    success_bonus: 0.0  # bonus if nut is close enough to base of bolt shank

ctrl:
    ctrl_type: operational_space_motion  # {gym_default,
                                         #  joint_space_ik, joint_space_id, 
                                         #  task_space_impedance, operational_space_motion, 
                                         #  open_loop_force, closed_loop_force,
                                         #  hybrid_force_motion}
    all:
        jacobian_type: geometric
        gripper_prop_gains: [100, 100]
        gripper_deriv_gains: [1, 1]
    gym_default:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [20, 20]
    joint_space_ik:
        ik_method: dls
        joint_prop_gains: [1, 1, 1, 1, 1, 1, 1]
        joint_deriv_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    joint_space_id:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
    task_space_impedance:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
    operational_space_motion:
        motion_ctrl_axes: [0, 0, 1, 0, 0, 1]
        task_prop_gains: [1, 1, 1, 1, 1, 200]
        task_deriv_gains: [1, 1, 1, 1, 1, 1]
    open_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
    closed_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    hybrid_force_motion:
        motion_ctrl_axes: [1, 1, 0, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
```

### isaacgymenvs/cfg/task/FrankaCabinet.yaml

```yaml
# used to create the object
name: FrankaCabinet

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym. 
env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 500
  enableDebugVis: False

  clipObservations: 5.0
  clipActions: 1.0

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  numProps: 16
  aggregateMode: 3

  actionScale: 7.5
  dofVelocityScale: 0.1
  distRewardScale: 2.0
  rotRewardScale: 0.5
  aroundHandleRewardScale: 0.25
  openRewardScale: 7.5
  fingerDistRewardScale: 5.0
  actionPenaltyScale: 0.01

  asset:
    assetRoot: "../../assets"
    assetFileNameFranka: "urdf/franka_description/robots/franka_panda.urdf"
    assetFileNameCabinet: "urdf/sektion_cabinet_model/urdf/sektion_cabinet_2.urdf"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166 # 1/60
  substeps: 1
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 12
    num_velocity_iterations: 1
    contact_offset: 0.005
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False

```

### isaacgymenvs/cfg/task/FrankaCubeStack.yaml

```yaml
# used to create the object
name: FrankaCubeStack

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym. 
env:
  numEnvs: ${resolve_default:8192,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 300
  enableDebugVis: False

  clipObservations: 5.0
  clipActions: 1.0

  startPositionNoise: 0.25
  startRotationNoise: 0.785
  frankaPositionNoise: 0.0
  frankaRotationNoise: 0.0
  frankaDofNoise: 0.25

  aggregateMode: 3

  actionScale: 1.0
  distRewardScale: 0.1
  liftRewardScale: 1.5
  alignRewardScale: 2.0
  stackRewardScale: 16.0

  controlType: osc  # options are {joint_tor, osc}

  asset:
    assetRoot: "../../assets"
    assetFileNameFranka: "urdf/franka_description/robots/franka_panda_gripper.urdf"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

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
    num_velocity_iterations: 1
    contact_offset: 0.005
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False

```

### isaacgymenvs/cfg/task/Humanoid.yaml

```yaml
# used to create the object
name: Humanoid

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 1000
  enableDebugVis: False

  clipActions: 1.0

  powerScale: 1.0

  # reward parameters
  headingWeight: 0.5
  upWeight: 0.1

  # cost parameters
  actionsCost: 0.01
  energyCost: 0.05
  dofVelocityScale: 0.1
  angularVelocityScale: 0.25
  contactForceScale: 0.01
  jointsAtLimitCost: 0.25
  deathCost: -1.0
  terminationHeight: 0.8

  asset:
    assetFileName: "mjcf/nv_humanoid.xml"

  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 10.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    # specify which attributes to randomize for each actor type and property
    frequency: 600   # Define how many environment steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      operation: "additive"
      distribution: "gaussian"
    actions:
      range: [0., .02]
      operation: "additive"
      distribution: "gaussian"
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 3000
    actor_params:
      humanoid:
        color: True
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
            schedule_steps: 3000
        rigid_shape_properties:
          friction:
            num_buckets: 500
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          restitution:
            range: [0., 0.7]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
        dof_properties:
          damping: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          stiffness: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000

```

### isaacgymenvs/cfg/task/HumanoidAMP.yaml

```yaml
# used to create the object
name: HumanoidAMP

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 300
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  
  pdControl: True
  powerScale: 1.0
  controlFrequencyInv: 2 # 30 Hz
  stateInit: "Random"
  hybridInitProb: 0.5
  numAMPObsSteps: 2

  localRootObs: False
  contactBodies: ["right_foot", "left_foot"]
  terminationHeight: 0.5
  enableEarlyTermination: True

  # animation files to learn from
  # these motions should use hyperparameters from HumanoidAMPPPO.yaml
  #motion_file: "amp_humanoid_walk.npy"
  motion_file: "amp_humanoid_run.npy"
  #motion_file: "amp_humanoid_dance.npy"

  # these motions should use hyperparameters from HumanoidAMPPPOLowGP.yaml
  #motion_file: "amp_humanoid_hop.npy"
  #motion_file: "amp_humanoid_backflip.npy"

  asset:
    assetFileName: "mjcf/amp_humanoid.xml"

  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 10.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    # specify which attributes to randomize for each actor type and property
    frequency: 600   # Define how many environment steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      operation: "additive"
      distribution: "gaussian"
    actions:
      range: [0., .02]
      operation: "additive"
      distribution: "gaussian"
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 3000
    actor_params:
      humanoid:
        color: True
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
            schedule_steps: 3000
        rigid_shape_properties:
          friction:
            num_buckets: 500
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          restitution:
            range: [0., 0.7]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
        dof_properties:
          damping: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          stiffness: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000


```

### isaacgymenvs/cfg/task/HumanoidAMPHands.yaml

```yaml
# used to create the object
name: HumanoidAMP

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 300
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  
  pdControl: True
  powerScale: 1.0
  controlFrequencyInv: 2 # 30 Hz
  stateInit: "Random"
  hybridInitProb: 0.5
  numAMPObsSteps: 2

  localRootObs: False
  contactBodies: ["right_foot", "left_foot", "right_hand", "left_hand"]
  terminationHeight: 0.5
  enableEarlyTermination: True

  # animation files to learn from
  motion_file: "amp_humanoid_cartwheel.npy"

  asset:
    assetFileName: "mjcf/amp_humanoid.xml"

  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 10.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    # specify which attributes to randomize for each actor type and property
    frequency: 600   # Define how many environment steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      operation: "additive"
      distribution: "gaussian"
    actions:
      range: [0., .02]
      operation: "additive"
      distribution: "gaussian"
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 3000
    actor_params:
      humanoid:
        color: True
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
            schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
            schedule_steps: 3000
        rigid_shape_properties:
          friction:
            num_buckets: 500
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          restitution:
            range: [0., 0.7]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
        dof_properties:
          damping: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          stiffness: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 3000


```

### isaacgymenvs/cfg/task/HumanoidSAC.yaml

```yaml
# used to create the object
defaults:
  - Humanoid
  - _self_

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:64,${...num_envs}}
```

### isaacgymenvs/cfg/task/IndustRealBase.yaml

```yaml
# See schema in factory_schema_config_base.py for descriptions of parameters.

defaults:
    - _self_

mode:
    export_scene: False
    export_states: False

sim:
    dt: 0.016667 
    substeps: 2
    up_axis: "z"
    use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
    gravity: [0.0, 0.0, -9.81]
    add_damping: True
    disable_franka_collisions: False

    physx:
        solver_type: ${....solver_type}
        num_threads: ${....num_threads}
        num_subscenes: ${....num_subscenes}
        use_gpu: ${contains:"cuda",${....sim_device}}

        num_position_iterations: 16
        num_velocity_iterations: 0
        contact_offset: 0.01
        rest_offset: 0.0
        bounce_threshold_velocity: 0.2
        max_depenetration_velocity: 5.0
        friction_offset_threshold: 0.01
        friction_correlation_distance: 0.00625

        max_gpu_contact_pairs: 6553600  # 50 * 1024 * 1024
        default_buffer_size_multiplier: 8.0
        contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)
    
env:
    env_spacing: 0.7
    franka_depth: 0.37  # Franka origin 37 cm behind table midpoint
    table_height: 1.04
    franka_friction: 4.0
    table_friction: 0.3
```

### isaacgymenvs/cfg/task/IndustRealEnvGears.yaml

```yaml
# See schema in factory_schema_config_env.py for descriptions of common parameters.

defaults:
    - IndustRealBase
    - _self_
    - /factory_schema_config_env

env:
    env_name: 'IndustRealEnvGears'
    
    gears_lateral_offset: 0.1  # Y-axis offset of gears before initial reset to prevent initial interpenetration with base plate
    gears_friction: 0.5  # coefficient of friction associated with gears
    base_friction: 0.5  # coefficient of friction associated with base plate

```

### isaacgymenvs/cfg/task/IndustRealEnvPegs.yaml

```yaml
# See schema in factory_schema_config_env.py for descriptions of common parameters.

defaults:
    - IndustRealBase
    - _self_
    - /factory_schema_config_env

env:
    env_name: 'IndustRealEnvPegs'

    desired_subassemblies: ['round_peg_hole_8mm', 
                            'round_peg_hole_12mm', 
                            'round_peg_hole_16mm',
                            'rectangular_peg_hole_8mm', 
                            'rectangular_peg_hole_12mm', 
                            'rectangular_peg_hole_16mm']

    plug_lateral_offset: 0.1  # Y-axis offset of plug before initial reset to prevent initial interpenetration with socket
    # Density and friction values are specified in industreal_asset_info_pegs.yaml

```

### isaacgymenvs/cfg/task/IndustRealTaskGearsInsert.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - IndustRealBase
    - _self_
    # - /factory_schema_config_task

name: IndustRealTaskGearsInsert
physics_engine: ${..physics_engine}

env:
    numEnvs: 128
    numObservations: 24
    numStates: 47
    numActions: 6
    
    gear_medium_pos_offset: [-0.05, -0.02, 0.03]
    num_gripper_move_sim_steps: 120  # number of timesteps to reserve for moving gripper before first step of episode
    num_gripper_close_sim_steps: 60  # number of timesteps to reserve for closing gripper onto gear during each reset

    base_pos_obs_noise: [0.001, 0.001, 0.0]
    base_rot_obs_noise: [0.0, 0.0, 0.0] 

randomize:
    franka_arm_initial_dof_pos: [-1.7574766278484677, 0.8403247702305783, 2.015877580177467, -2.0924931236718334, -0.7379389376686856, 1.6256438760537268, 1.2689337870766628]
    fingertip_centered_pos_initial: [0.0, 0.0, 0.2]  # initial position of midpoint between fingertips above table
    fingertip_centered_pos_noise: [0.0, 0.0, 0.0]  # noise on fingertip pos
    fingertip_centered_rot_initial: [3.141593, 0.0, 0.0]  # initial rotation of fingertips (Euler)
    fingertip_centered_rot_noise: [0.0, 0.0, 0.0]  # noise on fingertip rotation
    
    base_pos_xy_initial: [0.5, 0.0, 1.0781]  # initial position of gear base on table
    base_pos_xy_noise: [0.1, 0.1, 0.0381]  # noise on gear base position
    base_pos_z_noise_bounds: [0.0, 0.05]  # noise on gear base offset from table

    gear_pos_xyz_noise: [0.01, 0.01, 0.0]  # noise on gear position
    gear_rot_noise: 0.0872665  # noise on gear rotation

rl:
    pos_action_scale: [0.01, 0.01, 0.01]
    rot_action_scale: [0.01, 0.01, 0.01]
    force_action_scale: [1.0, 1.0, 1.0]
    torque_action_scale: [1.0, 1.0, 1.0]

    unidirectional_rot: True  # constrain Franka Z-rot to be unidirectional
    unidirectional_force: False  # constrain Franka Z-force to be unidirectional (useful for debugging)

    clamp_rot: True
    clamp_rot_thresh: 1.0e-6

    num_keypoints: 4  # number of keypoints used in reward
    keypoint_scale: 0.5  # length of line of keypoints

    max_episode_length: 128

    # SAPU
    interpen_thresh: 0.001  # max allowed interpenetration between gear and shaft

    # SDF-Based Reward
    sdf_reward_scale: 10.0
    sdf_reward_num_samples: 5000

    # SBC
    initial_max_disp: 0.01  # max initial downward displacement of gear at beginning of curriculum
    curriculum_success_thresh: 0.6  # success rate threshold for increasing curriculum difficulty
    curriculum_failure_thresh: 0.3  # success rate threshold for decreasing curriculum difficulty
    curriculum_height_step: [-0.005, 0.002]  # how much to increase max initial downward displacement after hitting success or failure thresh
    curriculum_height_bound: [-0.005, 0.015]  # max initial downward displacement of gear at hardest and easiest stages of curriculum

    # Success bonus
    close_error_thresh: 0.1  # threshold distance below which gear is considered close to shaft
    success_height_thresh: 0.01  # threshold distance below which gear is considered successfully inserted
    engagement_bonus: 10.0  # bonus if gear is engaged (partially inserted) with shaft

ctrl:
    ctrl_type: task_space_impedance  # {gym_default,
                                     #  joint_space_ik, joint_space_id, 
                                     #  task_space_impedance, operational_space_motion, 
                                     #  open_loop_force, closed_loop_force,
                                     #  hybrid_force_motion}
    all:
        jacobian_type: geometric
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [2, 2]
    gym_default:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [20, 20]
    joint_space_ik:
        ik_method: dls
        joint_prop_gains: [1, 1, 1, 1, 1, 1, 1]
        joint_deriv_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    joint_space_id:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
    task_space_impedance:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [300, 300, 600, 50, 50, 50]
        task_deriv_gains: [34, 34, 34, 1.4, 1.4, 1.4]
    operational_space_motion:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [20, 20, 100, 0, 0, 100]
        task_deriv_gains: [1, 1, 1, 1, 1, 1]
    open_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
    closed_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    hybrid_force_motion:
        motion_ctrl_axes: [1, 1, 0, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

```

### isaacgymenvs/cfg/task/IndustRealTaskPegsInsert.yaml

```yaml
# See schema in factory_schema_config_task.py for descriptions of common parameters.

defaults:
    - IndustRealBase
    - _self_
    # - /factory_schema_config_task

name: IndustRealTaskPegsInsert
physics_engine: ${..physics_engine}

env:
    numEnvs: 128
    numObservations: 24
    numStates: 47
    numActions: 6

    socket_base_height: 0.003

    num_gripper_move_sim_steps: 120  # number of timesteps to reserve for moving gripper before first step of episode
    num_gripper_close_sim_steps: 60  # number of timesteps to reserve for closing gripper onto plug during each reset

    socket_pos_obs_noise: [0.001, 0.001, 0.0]
    socket_rot_obs_noise: [0.0, 0.0, 0.0]  

randomize:
    franka_arm_initial_dof_pos: [-1.7574766278484677, 0.8403247702305783, 2.015877580177467, -2.0924931236718334, -0.7379389376686856, 1.6256438760537268, 1.2689337870766628]  # initial joint angles after reset; FrankX home pose
    fingertip_centered_pos_initial: [0.0, 0.0, 0.2]  # initial position of midpoint between fingertips above table
    fingertip_centered_pos_noise: [0.0, 0.0, 0.0]  # noise on fingertip pos
    fingertip_centered_rot_initial: [3.141593, 0.0, 0.0]  # initial rotation of fingertips (Euler)
    fingertip_centered_rot_noise: [0.0, 0.0, 0.0]  # noise on fingertip rotation

    socket_pos_xy_initial: [0.5, 0.0]  # initial position of socket on table
    socket_pos_xy_noise: [0.1, 0.1]  # noise on socket position
    socket_pos_z_noise_bounds: [0.0, 0.05]  # noise on socket offset from table
    socket_rot_noise: [0.0, 0.0, 0.0872665]  # noise on socket rotation

    plug_pos_xy_noise: [0.01, 0.01]  # noise on plug position

rl:
    pos_action_scale: [0.01, 0.01, 0.01]
    rot_action_scale: [0.01, 0.01, 0.01]
    force_action_scale: [1.0, 1.0, 1.0]
    torque_action_scale: [1.0, 1.0, 1.0]

    unidirectional_rot: True  # constrain Franka Z-rot to be unidirectional
    unidirectional_force: False  # constrain Franka Z-force to be unidirectional (useful for debugging)

    clamp_rot: True
    clamp_rot_thresh: 1.0e-6

    num_keypoints: 4  # number of keypoints used in reward
    keypoint_scale: 0.5  # length of line of keypoints

    max_episode_length: 256

    # SAPU
    interpen_thresh: 0.001  # SAPU: max allowed interpenetration between plug and socket

    # SDF-Based Reward
    sdf_reward_scale: 10.0
    sdf_reward_num_samples: 1000

    # SBC
    initial_max_disp: 0.01  # max initial downward displacement of plug at beginning of curriculum
    curriculum_success_thresh: 0.75  # success rate threshold for increasing curriculum difficulty
    curriculum_failure_thresh: 0.5  # success rate threshold for decreasing curriculum difficulty
    curriculum_height_step: [-0.005, 0.003]  # how much to increase max initial downward displacement after hitting success or failure thresh
    curriculum_height_bound: [-0.01, 0.01]  # max initial downward displacement of plug at hardest and easiest stages of curriculum

    # Success bonus
    close_error_thresh: 0.15  # threshold below which plug is considered close to socket
    success_height_thresh: 0.003  # threshold distance below which plug is considered successfully inserted
    engagement_bonus: 10.0  # bonus if plug is engaged (partially inserted) with socket

ctrl:
    ctrl_type: task_space_impedance  # {gym_default,
                                     #  joint_space_ik, joint_space_id, 
                                     #  task_space_impedance, operational_space_motion, 
                                     #  open_loop_force, closed_loop_force,
                                     #  hybrid_force_motion}
    all:
        jacobian_type: geometric
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [2, 2]
    gym_default:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
        gripper_prop_gains: [500, 500]
        gripper_deriv_gains: [20, 20]
    joint_space_ik:
        ik_method: dls
        joint_prop_gains: [1, 1, 1, 1, 1, 1, 1]
        joint_deriv_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    joint_space_id:
        ik_method: dls
        joint_prop_gains: [40, 40, 40, 40, 40, 40, 40]
        joint_deriv_gains: [8, 8, 8, 8, 8, 8, 8]
    task_space_impedance:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [300, 300, 300, 50, 50, 50]
        task_deriv_gains: [34, 34, 34, 1.4, 1.4, 1.4]
    operational_space_motion:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [60, 60, 60, 5, 5, 5]
        task_deriv_gains: [15.5, 15.5, 15.5, 4.5, 4.5, 4.5]
    open_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
    closed_loop_force:
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    hybrid_force_motion:
        motion_ctrl_axes: [1, 1, 1, 1, 1, 1]
        task_prop_gains: [40, 40, 40, 40, 40, 40]
        task_deriv_gains: [8, 8, 8, 8, 8, 8]
        force_ctrl_axes: [0, 0, 1, 0, 0, 0]
        wrench_prop_gains: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

```

### isaacgymenvs/cfg/task/Ingenuity.yaml

```yaml
# used to create the object
name: Ingenuity

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 2.5
  maxEpisodeLength: 2000
  enableDebugVis: False

  clipObservations: 5.0
  clipActions: 1.0

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.01
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 6
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.001
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False


```

### isaacgymenvs/cfg/task/Quadcopter.yaml

```yaml
# used to create the object
name: Quadcopter

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym. 
env:
  numEnvs: ${resolve_default:8192,${...num_envs}}
  envSpacing: 1.25
  maxEpisodeLength: 500
  enableDebugVis: False

  clipObservations: 5.0
  clipActions: 1.0

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.01
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.02
    rest_offset: 0.001
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)
    
task:
  randomize: False

```

### isaacgymenvs/cfg/task/ShadowHand.yaml

```yaml
# used to create the object
name: ShadowHand

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 600
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0

  useRelativeControl: False
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
  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # can be "openai", "full_no_vel", "full", "full_state"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

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
        tendon_properties:
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

### isaacgymenvs/cfg/task/ShadowHandOpenAI_FF.yaml

```yaml
# used to create the object
name: ShadowHand

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:16384,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 160 # Not used, but would be 8 sec if resetTime is not set
  resetTime: 8 # Max time till reset, in seconds, if a goal wasn't achieved. Will overwrite the episodeLength if is > 0.
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.3
  controlFrequencyInv: 3 # 20 Hz

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  # Random forces applied to the object
  forceScale: 1.0
  forceProbRange: [0.001, 0.1]
  forceDecay: 0.99
  forceDecayInterval: 0.08

  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: -50.0

  objectType: "block" # can be block, egg or pen
  observationType: "openai" # can be "openai", "full_no_vel", "full","full_state"
  asymmetric_observations: True
  successTolerance: 0.4
  printNumSuccesses: False
  maxConsecutiveSuccesses: 50
  averFactor: 0.1 # running mean factor for consecutive successes calculation

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: True
  randomization_params:
    frequency: 720   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
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
        tendon_properties:
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

### isaacgymenvs/cfg/task/ShadowHandOpenAI_LSTM.yaml

```yaml
# specifies what the config is when running `ShadowHandOpenAI` in LSTM mode

defaults:
  - ShadowHandOpenAI_FF
  - _self_

env:
  numEnvs: ${resolve_default:8192,${...num_envs}}

```

### isaacgymenvs/cfg/task/ShadowHandTest.yaml

```yaml
# used to create the object
name: ShadowHand

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:256,${...num_envs}}
  envSpacing: 0.75
  episodeLength: 1600 # 80 sec
  resetTime: 80 # Max time till reset, if goal wasn't achieved. In sec, if >0 will overwrite the episodeLength
  enableDebugVis: False
  aggregateMode: 1

  clipObservations: 5.0
  clipActions: 1.0

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.3
  controlFrequencyInv: 3 # 20 Hz

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

  distRewardScale: -10.0
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.24
  fallPenalty: -50.0

  objectType: "block" # can be block, egg or pen
  observationType: "openai" # can be "openai", "full_no_vel", "full", "full_state"
  asymmetric_observations: True
  successTolerance: 0.4
  printNumSuccesses: True
  maxConsecutiveSuccesses: 50
  averFactor: 0.1 # running mean factor for consecutive successes calculation

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

task:
  randomize: True
  randomization_params:
    frequency: 480000   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "constant"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 1
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "constant"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 1
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "constant"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 1
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"

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
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    num_subscenes: ${....num_subscenes}
    default_buffer_size_multiplier: 5.0
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

```

### isaacgymenvs/cfg/task/Trifinger.yaml

```yaml
name: Trifinger

physics_engine: ${..physics_engine}

env:
  aggregate_mode: True

  control_decimation: 1
  envSpacing: 1.0

  numEnvs: ${resolve_default:16384,${...num_envs}}

  episodeLength: 750

  clipObservations: 5.0
  clipActions: 1.0

  task_difficulty: 4
  enable_ft_sensors: false
  asymmetric_obs: true
  normalize_obs: true

  apply_safety_damping: true
  command_mode: torque
  normalize_action: true
  cube_obs_keypoints: true
  reset_distribution:
    object_initial_state:
      type: random
    robot_initial_state:
      dof_pos_stddev: 0.4
      dof_vel_stddev: 0.2
      type: default

  reward_terms:
    finger_move_penalty:
      activate: true
      weight: -0.5
    finger_reach_object_rate:
      activate: true
      norm_p: 2
      weight: -250
    object_dist:
      activate: false
      weight: 2000
    object_rot:
      activate: false
      weight: 2000
    keypoints_dist:
      activate: true
      weight: 2000
  termination_conditions:
    success:
      orientation_tolerance: 0.4
      position_tolerance: 0.02

  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.02
  substeps: 4
  up_axis: z
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity:
  - 0.0
  - 0.0
  - -9.81
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.5
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 0 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: True
  randomization_params:
    frequency: 750   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .000 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      # schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      # schedule_steps: 40000
    actions:
      range: [0., .02]
      range_correlated: [0, .01] # range for correlated noise, refreshed with freq `frequency`
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
      robot:
        color: True
        dof_properties:
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
      object:
        scale:
          range: [0.97, 1.03]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True # Property will only be randomized once before simulation is started. See Domain Randomization Documentation for more info.
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
          mass:
            range: [0.7, 1.3]
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
      table:
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"

```

### isaacgymenvs/cfg/task/env/regrasping.yaml

```yaml
subtask: "regrasping"

episodeLength: 300

# requires holding a grasp for a whole second, thus trained policies develop a robust grasp
successSteps: 30

```

### isaacgymenvs/cfg/task/env/reorientation.yaml

```yaml
# reorientation is a default task
subtask: "reorientation"

```

### isaacgymenvs/cfg/task/env/throw.yaml

```yaml
subtask: "throw"

episodeLength: 300

forceScale: 0.0  # random forces don't allow us to throw precisely so we turn them off

# curriculum not needed - if we hit a bin, that's good!
successTolerance: 0.075
targetSuccessTolerance: 0.075

# adds a small pause every time we hit a target
successSteps: 5

# throwing big objects is hard and they don't fit in the bin, so focus on randomized but smaller objects
withSmallCuboids: True
withBigCuboids: False
withSticks: False

```

### isaacgymenvs/cfg/train/AllegroHandDextremeADRPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True

    inputs:
      dof_pos_randomized: {}
      object_pose_cam_randomized: { }
      goal_pose: { }
      goal_relative_rot_cam_randomized: { }
      last_actions: { }

    mlp:
      units: [512, 512]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None
    rnn:
        name: lstm
        units: 1024
        layers: 1
        before_mlp: True
        layer_norm: True

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:AllegroHandADRAsymmLSTM,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: False  
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.998
    tau: 0.95
    learning_rate: 1e-4
    lr_schedule: linear #adaptive
    schedule_type: standard
    kl_threshold: 0.01
    score_to_win: 1000000
    max_epochs: ${resolve_default:1000_000,${....max_iterations}}
    save_best_after: 10000
    save_frequency: 500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.002
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 16384
    mini_epochs: 4
    critic_coef: 4
    clip_value: True
    seq_length: 16
    bound_loss_type: regularization
    bounds_loss_coef: 0.005
    zero_rnn_on_done: False

    # optimize summaries to prevent tf.event files from growing to gigabytes
    force_interval_writer: True

    central_value_config:
      minibatch_size: 16384 
      mini_epochs: 4
      learning_rate: 5e-5
      kl_threshold: 0.016
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        inputs:
          dof_pos: { }
          dof_vel: { }
          dof_force: { }

          object_pose: { }
          object_pose_cam_randomized: { }
          object_vels: { }

          goal_pose: { }
          goal_relative_rot: {}

          last_actions: { }

          stochastic_delay_params: { }
          affine_params: { }

          cube_random_params: {}
          hand_random_params: {}
          ft_force_torques: {}
          gravity_vec: {}
          ft_states: {}
          rot_dist: {}
          rb_forces: {}

        mlp:
          units: [1024, 512] 
          activation: elu
          d2rl: False
          initializer:
            name: default
          regularizer:
            name: None
        rnn:
          name: lstm
          units: 2048 
          layers: 1
          before_mlp: True
          layer_norm: True

    player:
      deterministic: True
      use_vecenv: True
      games_num: 1000000
      print_stats: False

```

### isaacgymenvs/cfg/train/AllegroHandDextremeManualDRPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True

    inputs:

      dof_pos_randomized: { }
      object_pose_cam_randomized: { }
      goal_pose_randomized: { }
      goal_relative_rot_cam_randomized: { }
      last_actions_randomized: { }

    mlp:
      units: [256]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None
    rnn:
        name: lstm
        units: 512
        layers: 1
        before_mlp: True
        layer_norm: True

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:AllegroHandManualDRAsymmLSTM,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: False  
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.998
    tau: 0.95
    learning_rate: 1e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.016
    score_to_win: 100000
    max_epochs: ${resolve_default:50000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 16384
    mini_epochs: 4
    critic_coef: 4
    clip_value: True
    seq_length: 16
    bounds_loss_coef: 0.0001
    zero_rnn_on_done: False

    central_value_config:
      minibatch_size: 16384 
      mini_epochs: 4
      learning_rate: 1e-4
      kl_threshold: 0.016
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        inputs:
          dof_pos: { }
          dof_vel: { }
          dof_force: { }

          object_pose: { }
          object_pose_cam_randomized: { }
          object_vels: { }

          goal_pose: { }
          goal_relative_rot: {}

          last_actions: { }

          ft_force_torques: {}
          gravity_vec: {}
          ft_states: {}


        mlp:
          units: [512, 256, 128] 
          activation: elu
          d2rl: False
          initializer:
            name: default
          regularizer:
            name: None

    player:
      deterministic: True
      use_vecenv: True
      games_num: 1000000
      print_stats: False

```

### isaacgymenvs/cfg/train/AllegroHandLSTMPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
      
    
    inputs:

      dof_pos_randomized: { }
      object_pose_cam_randomized: { }
      goal_pose_randomized: { }
      goal_relative_rot_cam_randomized: { }
      last_actions_randomized: { }

    mlp:
      units: [256]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None
    rnn:
        name: lstm
        units: 512
        layers: 1
        before_mlp: True
        layer_norm: True

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:AllegroHandAsymmLSTM,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: False  # TODO: enable bootstrap?
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.998
    tau: 0.95
    learning_rate: 1e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.016
    score_to_win: 100000
    max_epochs: ${resolve_default:50000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 16384
    mini_epochs: 4
    critic_coef: 4
    clip_value: True
    seq_length: 16
    bounds_loss_coef: 0.0001

    # optimize summaries to prevent tf.event files from growing to gigabytes
    defer_summaries_sec: ${if:${....pbt},150,5}
    summaries_interval_sec_min: ${if:${....pbt},20,5}
    summaries_interval_sec_max: 100

    central_value_config:
      minibatch_size: 16384 #32768
      mini_epochs: 4
      learning_rate: 1e-4
      kl_threshold: 0.016
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        inputs:
          dof_pos: { }
          dof_vel: { }
          dof_force: { }

          object_pose: { }
          object_pose_cam_randomized: { }
          object_vels: { }

          goal_pose: { }
          goal_relative_rot: {}

          last_actions: { }

          ft_force_torques: {}
          gravity_vec: {}
          ft_states: {}


        mlp:
          units: [512, 256, 128] #[256] # 
          activation: elu
          d2rl: False
          initializer:
            name: default
          regularizer:
            name: None
        rnn:
          name: lstm
          units: 512
          layers: 1
          before_mlp: True
          layer_norm: True

    player:
      deterministic: True
      use_vecenv: True
      games_num: 1000000
      print_stats: False

```

### isaacgymenvs/cfg/train/AllegroHandLSTM_BigPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: complex_net
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
      
    inputs:
      dof_pos_offset_randomized: {}
      object_pose_delayed_randomized: {}
      goal_pose: {}
      goal_relative_rot_delayed_randomized: {}
      last_actions: {}

    mlp:
      units: [512]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None
    rnn:
        name: lstm
        units: 1024
        layers: 1
        before_mlp: True
        layer_norm: True

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:AllegroHandAsymmLSTM,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    use_smooth_clamp: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.998
    tau: 0.95
    learning_rate: 1e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.016
    score_to_win: 100000
    max_epochs: ${resolve_default:1000000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 16384
    mini_epochs: 4
    critic_coef: 4
    clip_value: True
    seq_length: 16
    bounds_loss_coef: 0.0001

    central_value_config:
      minibatch_size: 16384 #32768
      mini_epochs: 4
      learning_rate: 1e-4
      kl_threshold: 0.016
      clip_value: True
      normalize_input: True
      truncate_grads: True
      use_smooth_clamp: True

      network:
        name: complex_net
        central_value: True
        inputs:
          dof_pos: {}
          dof_pos_offset_randomized: {}
          dof_vel: {}
          dof_torque: {}
          object_pose: {}
          object_vels: {}
          goal_pose: {}
          goal_relative_rot: {}
          object_pose_delayed_randomized: {}
          goal_relative_rot_delayed_randomized: {}
          object_obs_delayed_age: {}
          # ft_states: {}
          # ft_force_torques: {}
          last_actions: {}
        mlp:
          units: [512, 512, 256, 128] #[256] # 
          activation: elu
          d2rl: False
          initializer:
            name: default
          regularizer:
            name: None
        # rnn:
        #   name: lstm
        #   units: 512
        #   layers: 1
        #   before_mlp: True
        #   layer_norm: True

    player:
      deterministic: True
      use_vecenv: True
      games_num: 1000000
      print_stats: False


```

### isaacgymenvs/cfg/train/AllegroHandPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True

    mlp:
      units: [512, 256, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:AllegroHand,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 0.01
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.016
    score_to_win: 100000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 500
    save_frequency: 200
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 8
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001

    player:
      #render: True
      deterministic: True
      games_num: 100000
      print_stats: True
```

### isaacgymenvs/cfg/train/AllegroKukaLSTMPPO.yaml

```yaml
defaults:
  - AllegroKukaPPO
  - _self_

params:
  network:
    mlp:
      units: [768, 512, 256]
      activation: elu
      d2rl: False
      initializer:
        name: default
      regularizer:
        name: None
    rnn:
      name: lstm
      units: 768
      layers: 1
      before_mlp: True
      layer_norm: True

  config:
    name: ${resolve_default:AllegroKukaLSTMPPO,${....experiment}}
    minibatch_size: 32768
    mini_epochs: 2

```

## Python signatures and reward/observation bodies (133 files)


### isaacgymenvs/__init__.py

```
def make(seed, task, num_envs, sim_device, rl_device, graphics_device_id, headless, multi_gpu, virtual_screen_capture, force_render, cfg)
```

### isaacgymenvs/learning/amp_continuous.py

```
class AMPAgent(CommonAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def set_eval(self)
    def set_train(self)
    def get_stats_weights(self)
    def set_stats_weights(self, weights)
    def play_steps(self)
    def prepare_dataset(self, batch_dict)
    def train_epoch(self)
    def calc_gradients(self, input_dict)
    def _load_config_params(self, config)
    def _build_net_config(self)
    def _init_train(self)
    def _disc_loss(self, disc_agent_logit, disc_demo_logit, obs_demo)
    def _disc_loss_neg(self, disc_logits)
    def _disc_loss_pos(self, disc_logits)
    def _compute_disc_acc(self, disc_agent_logit, disc_demo_logit)
    def _fetch_amp_obs_demo(self, num_samples)
    def _build_amp_buffers(self)
    def _init_amp_demo_buf(self)
    def _update_amp_demos(self)
    def _preproc_amp_obs(self, amp_obs)
    def _combine_rewards(self, task_rewards, amp_rewards)
    def _eval_disc(self, amp_obs)
    def _calc_amp_rewards(self, amp_obs)
    def _calc_disc_rewards(self, amp_obs)
    def _store_replay_amp_obs(self, amp_obs)
    def _record_train_batch_info(self, batch_dict, train_info)
    def _log_train_info(self, train_info, frame)
    def _amp_debug(self, info)

```python
def _combine_rewards(self, task_rewards, amp_rewards):
        disc_r = amp_rewards['disc_rewards']
        combined_rewards = self._task_reward_w * task_rewards + \
                         + self._disc_reward_w * disc_r
        return combined_rewards
```

```python
def _calc_amp_rewards(self, amp_obs):
        disc_r = self._calc_disc_rewards(amp_obs)
        output = {
            'disc_rewards': disc_r
        }
        return output
```

```python
def _calc_disc_rewards(self, amp_obs):
        with torch.no_grad():
            disc_logits = self._eval_disc(amp_obs)
            prob = 1 / (1 + torch.exp(-disc_logits)) 
            disc_r = -torch.log(torch.maximum(1 - prob, torch.tensor(0.0001, device=self.ppo_device)))
            disc_r *= self._disc_reward_scale
        return disc_r
```
```

### isaacgymenvs/learning/amp_datasets.py

```
class AMPDataset(PPODataset)
    def __init__(self, batch_size, minibatch_size, is_discrete, is_rnn, device, seq_len)
    def update_mu_sigma(self, mu, sigma)
    def _get_item(self, idx)
    def _shuffle_idx_buf(self)
```

### isaacgymenvs/learning/amp_models.py

```
class ModelAMPContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/amp_network_builder.py

```
class AMPBuilder(A2CBuilder)
    def __init__(self)
    def build(self, name)
```

### isaacgymenvs/learning/amp_players.py

```
class AMPPlayerContinuous(CommonPlayer)
    def __init__(self, params)
    def restore(self, fn)
    def _build_net(self, config)
    def _post_step(self, info)
    def _build_net_config(self)
    def _amp_debug(self, info)
    def _preproc_amp_obs(self, amp_obs)
    def _eval_disc(self, amp_obs)
    def _calc_amp_rewards(self, amp_obs)
    def _calc_disc_rewards(self, amp_obs)

```python
def _calc_amp_rewards(self, amp_obs):
        disc_r = self._calc_disc_rewards(amp_obs)
        output = {
            'disc_rewards': disc_r
        }
        return output
```

```python
def _calc_disc_rewards(self, amp_obs):
        with torch.no_grad():
            disc_logits = self._eval_disc(amp_obs)
            prob = 1.0 / (1.0 + torch.exp(-disc_logits)) 
            disc_r = -torch.log(torch.maximum(1 - prob, torch.tensor(0.0001, device=self.device)))
            disc_r *= self._disc_reward_scale
        return disc_r
```
```

### isaacgymenvs/learning/common_agent.py

```
class CommonAgent(A2CAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def train(self)
    def train_epoch(self)
    def play_steps(self)
    def calc_gradients(self, input_dict)
    def discount_values(self, mb_fdones, mb_values, mb_rewards, mb_next_values)
    def bound_loss(self, mu)
    def _load_config_params(self, config)
    def _build_net_config(self)
    def _setup_action_space(self)
    def _init_train(self)
    def _env_reset_done(self)
    def _eval_critic(self, obs_dict)
    def _actor_loss(self, old_action_log_probs_batch, action_log_probs, advantage, curr_e_clip)
    def _critic_loss(self, value_preds_batch, values, curr_e_clip, return_batch, clip_value)
    def _record_train_batch_info(self, batch_dict, train_info)
    def _log_train_info(self, train_info, frame)
```

### isaacgymenvs/learning/common_player.py

```
class CommonPlayer(PpoPlayerContinuous)
    def __init__(self, params)
    def run(self)
    def obs_to_torch(self, obs)
    def get_action(self, obs_dict, is_determenistic)
    def _build_net(self, config)
    def _env_reset_done(self)
    def _post_step(self, info)
    def _build_net_config(self)
    def _setup_action_space(self)
```

### isaacgymenvs/learning/hrl_continuous.py

```
class HRLAgent(CommonAgent)
    def __init__(self, base_name, config)
    def env_step(self, actions)
    def cast_obs(self, obs)
    def preprocess_actions(self, actions)
    def _setup_action_space(self)
    def _build_llc(self, config_params, checkpoint_file)
    def _build_llc_agent_config(self, config_params, network)
    def _compute_llc_action(self, obs, actions)
    def _extract_llc_obs(self, obs)
```

### isaacgymenvs/learning/hrl_models.py

```
class ModelHRLContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/replay_buffer.py

```
class ReplayBuffer()
    def __init__(self, buffer_size, device)
    def reset(self)
    def get_buffer_size(self)
    def get_total_count(self)
    def store(self, data_dict)
    def sample(self, n)
    def _reset_sample_idx(self)
    def _init_data_buf(self, data_dict)
```

### isaacgymenvs/pbt/experiments/run_utils.py

```
def seeds(num_seeds)
```

### isaacgymenvs/pbt/launcher/run.py

```
def launcher_argparser(args)
def parse_args()
def main()
```

### isaacgymenvs/pbt/launcher/run_description.py

```
class ParamGenerator()
    def __init__(self)
    def generate_params(self, randomize)
class ParamList(ParamGenerator)
    """The most simple kind of generator, represents just the list of parameter combinations."""
    def __init__(self, combinations)
    def generate_params(self, randomize)
class ParamGrid(ParamGenerator)
    """Parameter generator for grid search."""
    def __init__(self, grid_tuples)
    def _generate_combinations(self, param_idx, params)
    def generate_params(self, randomize)
class Experiment()
    def __init__(self, name, cmd, param_generator, env_vars)
    def generate_experiments(self, experiment_arg_name, customize_experiment_name, param_prefix)
class RunDescription()
    def __init__(self, run_name, experiments, experiment_arg_name, experiment_dir_arg_name, customize_experiment_name, param_prefix)
    def generate_experiments(self, train_dir, makedirs)
```

### isaacgymenvs/pbt/launcher/run_ngc.py

```
"""Run many experiments with NGC: hyperparameter sweeps, etc.
This isn't production code, but feel free to use as an example for your NGC setup."""
def add_ngc_args(parser)
def run_ngc(run_description, args)
```

### isaacgymenvs/pbt/launcher/run_processes.py

```
"""Run groups of experiments, hyperparameter sweeps, etc."""
def add_os_parallelism_args(parser)
def ensure_dir_exists(path)
def run(run_description, args)
```

### isaacgymenvs/pbt/launcher/run_slurm.py

```
def str2bool(v)
def add_slurm_args(parser)
def run_slurm(run_description, args)
```

### isaacgymenvs/pbt/mutation.py

```
def mutate_float(x, change_min, change_max)
def mutate_float_min_1(x)
def mutate_eps_clip(x)
def mutate_mini_epochs(x)
def mutate_discount(x)
def get_mutation_func(mutation_func_name)
def mutate(params, mutations, mutation_rate, pbt_change_min, pbt_change_max)
```

### isaacgymenvs/pbt/pbt.py

```
def _checkpnt_name(iteration)
def _model_checkpnt_name(iteration)
def _flatten_params(params, prefix, separator)
def _filter_params(params, params_to_mutate)
class PbtParams()
    def __init__(self, cfg)
def _restart_process_with_new_params(policy_idx, new_params, restart_from_checkpoint, experiment_name, algo, with_wandb)
def initial_pbt_check(cfg)
class PbtAlgoObserver(AlgoObserver)
    def __init__(self, cfg)
    def after_init(self, algo)
    def process_infos(self, infos, done_indices)
    def after_steps(self)
    def _rewrite_checkpoint(self, restart_checkpoint_tmp, env_frames)
    def _save_pbt_checkpoint(self)
    def _policy_workspace_dir(self, policy_idx)
    def _load_population_checkpoints(self)
    def _maybe_save_best_policy(self, best_objective, best_policy_idx, best_policy_checkpoint)
    def _pbt_summaries(self, params, best_objective)
    def _cleanup(self, checkpoints)
    def _delete_old_checkpoint(self, pbt_checkpoint_files)
```

### isaacgymenvs/tasks/__init__.py

```
def resolve_allegro_kuka(cfg)
def resolve_allegro_kuka_two_arms(cfg)
```

### isaacgymenvs/tasks/allegro_hand.py

```
class AllegroHand(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(object_pos - target_pos, p=2, dim=-1)

    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist * dist_reward_scale
    rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = dist_rew + rot_rew + action_penalty * action_penalty_scale

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threshold
    reward = torch.where(goal_dist >= fall_dist, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(goal_dist >= fall_dist, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)

    timed_out = progress_buf >= max_episode_length - 1
    resets = torch.where(timed_out, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(timed_out, reward + 0.5 * fall_penalty, reward)

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, successes, cons_successes
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
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
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        if self.obs_type == "full_no_vel":
            self.compute_full_observations(True)
        elif self.obs_type == "full":
            self.compute_full_observations()
        elif self.obs_type == "full_state":
             self.compute_full_state()
        else:
            print("Unknown observations type!")

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_full_observations(self, no_vel=False):
        if no_vel:
            self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                                   self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)

            self.obs_buf[:, 16:23] = self.object_pose
            self.obs_buf[:, 23:30] = self.goal_pose
            self.obs_buf[:, 30:34] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 34:50] = self.actions
        else:
            self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                                   self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
            self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel

            # 2*16 = 32 -16
            self.obs_buf[:, 32:39] = self.object_pose
            self.obs_buf[:, 39:42] = self.object_linvel
            self.obs_buf[:, 42:45] = self.vel_obs_scale * self.object_angvel

            self.obs_buf[:, 45:52] = self.goal_pose
            self.obs_buf[:, 52:56] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 56:72] = self.actions
```
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_base.py

```
class AllegroKukaBase(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _object_start_pose(self, allegro_pose, table_pose_dy, table_pose_dz)
    def _main_object_assets_and_scales(self, object_asset_root, tmp_assets_dir)
    def _load_main_object_asset(self)
    def _load_additional_assets(self, object_asset_root, arm_pose)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _extra_reset_rules(self, resets)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def _extra_curriculum(self)
    def get_env_state(self)
    def set_env_state(self, env_state)
    def create_sim(self)
    def _create_ground_plane(self)
    def _box_asset_files_and_scales(self, object_assets_root, generated_assets_dir)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _distance_delta_rewards(self, lifted_object)
    def _lifting_reward(self)
    def _keypoint_reward(self, lifted_object)
    def _action_penalties(self)
    def _compute_resets(self, is_success)
    def _true_objective(self)
    def compute_kuka_reward(self)
    def _eval_stats(self, is_success)
    def compute_observations(self)
    def compute_full_state(self, buf)
    def clamp_obs(self, obs_buf)
    def get_random_quat(self, env_ids)
    def reset_target_pose(self, env_ids)
    def reset_object_pose(self, env_ids)
    def deferred_set_actor_root_state_tensor_indexed(self, obj_indices)
    def set_actor_root_state_tensor_indexed(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def accumulate_env_states(self)
    def dump_env_states(self, env_ids)
    def load_initial_states(self)

```python
def _distance_delta_rewards(self, lifted_object: Tensor) -> Tuple[Tensor, Tensor]:
        """Rewards for fingertips approaching the object or penalty for hand getting further away from the object."""
        # this is positive if we got closer, negative if we're further away than the closest we've gotten
        fingertip_deltas_closest = self.closest_fingertip_dist - self.curr_fingertip_distances
        # update the values if finger tips got closer to the object
        self.closest_fingertip_dist = torch.minimum(self.closest_fingertip_dist, self.curr_fingertip_distances)

        # again, positive is closer, negative is further away
        # here we use index of the 1st finger, when the distance is large it doesn't matter which one we use
        hand_deltas_furthest = self.furthest_hand_dist - self.curr_fingertip_distances[:, 0]
        # update the values if finger tips got further away from the object
        self.furthest_hand_dist = torch.maximum(self.furthest_hand_dist, self.curr_fingertip_distances[:, 0])

        # clip between zero and +inf to turn deltas into rewards
        fingertip_deltas = torch.clip(fingertip_deltas_closest, 0, 10)
        fingertip_deltas *= self.finger_rew_coeffs
        fingertip_delta_rew = torch.sum(fingertip_deltas, dim=-1)
        # add this reward only before the object is lifted off the table
        # after this, we should be guided only by keypoint and bonus rewards
        fingertip_delta_rew *= ~lifted_object

        # clip between zero and -inf to turn deltas into penalties
        hand_delta_penalty = torch.clip(hand_deltas_furthest, -10, 0)
        hand_delta_penalty *= ~lifted_object
        # multiply by the number of fingers so two rewards are on the same scale
        hand_delta_penalty *= self.num_allegro_fingertips

        return fingertip_delta_rew, hand_delta_penalty
```

```python
def _lifting_reward(self) -> Tuple[Tensor, Tensor, Tensor]:
        """Reward for lifting the object off the table."""

        z_lift = 0.05 + self.object_pos[:, 2] - self.object_init_state[:, 2]
        lifting_rew = torch.clip(z_lift, 0, 0.5)

        # this flag tells us if we lifted an object above a certain height compared to the initial position
        lifted_object = (z_lift > self.lifting_bonus_threshold) | self.lifted_object

        # Since we stop rewarding the agent for height after the object is lifted, we should give it large positive reward
        # to compensate for "lost" opportunity to get more lifting reward for sitting just below the threshold.
        # This bonus depends on the max lifting reward (lifting reward coeff * threshold) and the discount factor
        # (i.e. the effective future horizon for the agent)
        # For threshold 0.15, lifting reward coeff = 3 and gamma 0.995 (effective horizon ~500 steps)
        # a value of 300 for the bonus reward seems reasonable
        just_lifted_above_threshold = lifted_object & ~self.lifted_object
        lift_bonus_rew = self.lifting_bonus * just_lifted_above_threshold

        # stop giving lifting reward once we crossed the threshold - now the agent can focus entirely on the
        # keypoint reward
        lifting_rew *= ~lifted_object

        # update the flag that describes whether we lifted an object above the table or not
        self.lifted_object = lifted_object
        return lifting_rew, lift_bonus_rew, lifted_object
```

```python
def _keypoint_reward(self, lifted_object: Tensor) -> Tensor:
        # this is positive if we got closer, negative if we're further away
        max_keypoint_deltas = self.closest_keypoint_max_dist - self.keypoints_max_dist

        # update the values if we got closer to the target
        self.closest_keypoint_max_dist = torch.minimum(self.closest_keypoint_max_dist, self.keypoints_max_dist)

        # clip between zero and +inf to turn deltas into rewards
        max_keypoint_deltas = torch.clip(max_keypoint_deltas, 0, 100)

        # administer reward only when we already lifted an object from the table
        # to prevent the situation where the agent just rolls it around the table
        keypoint_rew = max_keypoint_deltas * lifted_object

        return keypoint_rew
```

```python
def compute_kuka_reward(self) -> Tuple[Tensor, Tensor]:
        lifting_rew, lift_bonus_rew, lifted_object = self._lifting_reward()
        fingertip_delta_rew, hand_delta_penalty = self._distance_delta_rewards(lifted_object)
        keypoint_rew = self._keypoint_reward(lifted_object)

        keypoint_success_tolerance = self.success_tolerance * self.keypoint_scale

        # noinspection PyTypeChecker
        near_goal: Tensor = self.keypoints_max_dist <= keypoint_success_tolerance
        self.near_goal_steps += near_goal

        is_success = self.near_goal_steps >= self.success_steps
        goal_resets = is_success
        self.successes += is_success

        self.reset_goal_buf[:] = goal_resets

        self.rewards_episode["raw_fingertip_delta_rew"] += fingertip_delta_rew
        self.rewards_episode["raw_hand_delta_penalty"] += hand_delta_penalty
        self.rewards_episode["raw_lifting_rew"] += lifting_rew
        self.rewards_episode["raw_keypoint_rew"] += keypoint_rew

        fingertip_delta_rew *= self.distance_delta_rew_scale
        hand_delta_penalty *= self.distance_delta_rew_scale * 0  # currently disabled
        lifting_rew *= self.lifting_rew_scale
        keypoint_rew *= self.keypoint_rew_scale

        kuka_actions_penalty, allegro_actions_penalty = self._action_penalties()

        # Success bonus: orientation is within `success_tolerance` of goal orientation
        # We spread out the reward over "success_steps"
        bonus_rew = near_goal * (self.reach_goal_bonus / self.success_steps)

        reward = (
            fingertip_delta_rew
            + hand_delta_penalty  # + sign here because hand_delta_penalty is negative
            + lifting_rew
            + lift_bonus_rew
            + keypoint_rew
            + kuka_actions_penalty
            + allegro_actions_penalty
            + bonus_rew
        )

        self.rew_buf[:] = reward

        resets = self._compute_resets(is_success)
        self.reset_buf[:] = resets

        self.extras["successes"] = self.prev_episode_successes.mean()
        self.true_objective = self._true_objective()
        self.extras["true_objective"] = self.true_objective

        # scalars for logging
        self.extras["true_objective_mean"] = self.true_objective.mean()
        self.extras["true_objective_min"] = self.true_objective.min()
        self.extras["true_objective_max"] = self.true_objective.max()

        rewards = [
            (fingertip_delta_rew, "fingertip_delta_rew"),
            (hand_delta_penalty, "hand_delta_penalty"),
            (lifting_rew, "lifting_rew"),
            (lift_bonus_rew, "lift_bonus_rew"),
            (keypoint_rew, "keypoint_rew"),
            (kuka_actions_penalty, "kuka_actions_penalty"),
            (allegro_actions_penalty, "allegro_actions_penalty"),
            (bonus_rew, "bonus_rew"),
        ]

        episode_cumulative = dict()
        for rew_value, rew_name in rewards:
            self.rewards_episode[rew_name] += rew_value
            episode_cumulative[rew_name] = rew_value
        self.extras["rewards_episode"] = self.rewards_episode
        self.extras["episode_cumulative"] = episode_cumulative

        return self.rew_buf, is_success
```

```python
def compute_observations(self) -> Tuple[Tensor, int]:
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state":
            if self.with_fingertip_force_sensors:
                self.gym.refresh_force_sensor_tensor(self.sim)
            if self.with_dof_force_sensors:
                self.gym.refresh_dof_force_tensor(self.sim)

        self.object_state = self.root_state_tensor[self.object_indices, 0:13]
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.palm_center_offset = torch.from_numpy(self.palm_offset).to(self.device).repeat((self.num_envs, 1))
        self._palm_state = self.rigid_body_states[:, self.allegro_palm_handle][:, 0:13]
        self._palm_pos = self.rigid_body_states[:, self.allegro_palm_handle][:, 0:3]
        self._palm_rot = self.rigid_body_states[:, self.allegro_palm_handle][:, 3:7]
        self.palm_center_pos = self._palm_pos + quat_rotate(self._palm_rot, self.palm_center_offset)

        self.fingertip_state = self.rigid_body_states[:, self.allegro_fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.allegro_fingertip_handles][:, :, 0:3]
        self.fingertip_rot = self.rigid_body_states[:, self.allegro_fingertip_handles][:, :, 3:7]

        if not isinstance(self.fingertip_offsets, torch.Tensor):
            self.fingertip_offsets = (
                torch.from_numpy(self.fingertip_offsets).to(self.device).repeat((self.num_envs, 1, 1))
            )

        if hasattr(self, "fingertip_pos_rel_object"):
            self.fingertip_pos_rel_object_prev[:, :, :] = self.fingertip_pos_rel_object
        else:
            self.fingertip_pos_rel_object_prev = None

        self.fingertip_pos_offset = torch.zeros_like(self.fingertip_pos).to(self.device)
        for i in range(self.num_allegro_fingertips):
            self.fingertip_pos_offset[:, i] = self.fingertip_pos[:, i] + quat_rotate(
                self.fingertip_rot[:, i], self.fingertip_offsets[:, i]
            )

        obj_pos_repeat = self.object_pos.unsqueeze(1).repeat(1, sel
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_regrasping.py

```
class AllegroKukaRegrasping(AllegroKukaBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _load_additional_assets(self, object_asset_root, arm_pose)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def compute_kuka_reward(self)
    def _true_objective(self)
    def _extra_curriculum(self)

```python
def compute_kuka_reward(self) -> Tuple[Tensor, Tensor]:
        rew_buf, is_success = super().compute_kuka_reward()  # TODO: customize reward?
        return rew_buf, is_success
```
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_reorientation.py

```
class AllegroKukaReorientation(AllegroKukaBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _load_additional_assets(self, object_asset_root, arm_pose)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _extra_reset_rules(self, resets)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def _extra_curriculum(self)
    def _true_objective(self)
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_throw.py

```
class AllegroKukaThrow(AllegroKukaBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _load_additional_assets(self, object_asset_root, arm_pose)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def _true_objective(self)
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_two_arms.py

```
class AllegroKukaTwoArmsBase(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _object_start_pose(self, arms_y_ofs, table_pose_dy, table_pose_dz)
    def _main_object_assets_and_scales(self, object_asset_root, tmp_assets_dir)
    def _load_main_object_asset(self)
    def _load_additional_assets(self, object_asset_root, arm_y_offset)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _extra_reset_rules(self, resets)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def _extra_curriculum(self)
    def get_env_state(self)
    def set_env_state(self, env_state)
    def create_sim(self)
    def _create_ground_plane(self)
    def _box_asset_files_and_scales(self, object_assets_root, generated_assets_dir)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _distance_delta_rewards(self, lifted_object)
    def _lifting_reward(self)
    def _keypoint_reward(self, lifted_object)
    def _compute_resets(self, is_success)
    def _true_objective(self)
    def compute_kuka_reward(self)
    def _eval_stats(self, is_success)
    def compute_observations(self)
    def compute_full_state(self, buf)
    def clamp_obs(self, obs_buf)
    def get_random_quat(self, env_ids)
    def reset_target_pose(self, env_ids)
    def reset_object_pose(self, env_ids)
    def deferred_set_actor_root_state_tensor_indexed(self, obj_indices)
    def set_actor_root_state_tensor_indexed(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)

```python
def _distance_delta_rewards(self, lifted_object: Tensor) -> Tensor:
        """Rewards for fingertips approaching the object or penalty for hand getting further away from the object."""
        # this is positive if we got closer, negative if we're further away than the closest we've gotten
        fingertip_deltas_closest = self.closest_fingertip_dist - self.curr_fingertip_distances
        # update the values if finger tips got closer to the object
        self.closest_fingertip_dist = torch.minimum(self.closest_fingertip_dist, self.curr_fingertip_distances)

        # clip between zero and +inf to turn deltas into rewards
        fingertip_deltas = torch.clip(fingertip_deltas_closest, 0, 10)
        fingertip_delta_rew = torch.sum(fingertip_deltas, dim=-1)
        fingertip_delta_rew = torch.sum(fingertip_delta_rew, dim=-1)  # sum over all arms

        # vvvv this is commented out for 2 arms: we want the 2nd arm to be relatively close at all times

        # add this reward only before the object is lifted off the table
        # after this, we should be guided only by keypoint and bonus rewards
        # fingertip_delta_rew *= ~lifted_object

        return fingertip_delta_rew
```

```python
def _lifting_reward(self) -> Tuple[Tensor, Tensor, Tensor]:
        """Reward for lifting the object off the table."""

        z_lift = 0.05 + self.object_pos[:, 2] - self.object_init_state[:, 2]
        lifting_rew = torch.clip(z_lift, 0, 0.5)

        # this flag tells us if we lifted an object above a certain height compared to the initial position
        lifted_object = (z_lift > self.lifting_bonus_threshold) | self.lifted_object

        # Since we stop rewarding the agent for height after the object is lifted, we should give it large positive reward
        # to compensate for "lost" opportunity to get more lifting reward for sitting just below the threshold.
        # This bonus depends on the max lifting reward (lifting reward coeff * threshold) and the discount factor
        # (i.e. the effective future horizon for the agent)
        # For threshold 0.15, lifting reward coeff = 3 and gamma 0.995 (effective horizon ~500 steps)
        # a value of 300 for the bonus reward seems reasonable
        just_lifted_above_threshold = lifted_object & ~self.lifted_object
        lift_bonus_rew = self.lifting_bonus * just_lifted_above_threshold

        # stop giving lifting reward once we crossed the threshold - now the agent can focus entirely on the
        # keypoint reward
        lifting_rew *= ~lifted_object

        # update the flag that describes whether we lifted an object above the table or not
        self.lifted_object = lifted_object
        return lifting_rew, lift_bonus_rew, lifted_object
```

```python
def _keypoint_reward(self, lifted_object: Tensor) -> Tensor:
        # this is positive if we got closer, negative if we're further away
        max_keypoint_deltas = self.closest_keypoint_max_dist - self.keypoints_max_dist

        # update the values if we got closer to the target
        self.closest_keypoint_max_dist = torch.minimum(self.closest_keypoint_max_dist, self.keypoints_max_dist)

        # clip between zero and +inf to turn deltas into rewards
        max_keypoint_deltas = torch.clip(max_keypoint_deltas, 0, 100)

        # administer reward only when we already lifted an object from the table
        # to prevent the situation where the agent just rolls it around the table
        keypoint_rew = max_keypoint_deltas * lifted_object

        return keypoint_rew
```

```python
def compute_kuka_reward(self) -> Tuple[Tensor, Tensor]:
        lifting_rew, lift_bonus_rew, lifted_object = self._lifting_reward()
        fingertip_delta_rew = self._distance_delta_rewards(lifted_object)
        keypoint_rew = self._keypoint_reward(lifted_object)

        keypoint_success_tolerance = self.success_tolerance * self.keypoint_scale

        # noinspection PyTypeChecker
        near_goal: Tensor = self.keypoints_max_dist <= keypoint_success_tolerance
        self.near_goal_steps += near_goal

        is_success = self.near_goal_steps >= self.success_steps
        goal_resets = is_success
        self.successes += is_success

        self.reset_goal_buf[:] = goal_resets

        self.rewards_episode["raw_fingertip_delta_rew"] += fingertip_delta_rew
        self.rewards_episode["raw_lifting_rew"] += lifting_rew
        self.rewards_episode["raw_keypoint_rew"] += keypoint_rew

        fingertip_delta_rew *= self.distance_delta_rew_scale
        lifting_rew *= self.lifting_rew_scale
        keypoint_rew *= self.keypoint_rew_scale

        # Success bonus: orientation is within `success_tolerance` of goal orientation
        # We spread out the reward over "success_steps"
        bonus_rew = near_goal * (self.reach_goal_bonus / self.success_steps)

        reward = fingertip_delta_rew + lifting_rew + lift_bonus_rew + keypoint_rew + bonus_rew

        self.rew_buf[:] = reward

        resets = self._compute_resets(is_success)
        self.reset_buf[:] = resets

        self.extras["successes"] = self.prev_episode_successes.mean()
        self.true_objective = self._true_objective()
        self.extras["true_objective"] = self.true_objective

        # scalars for logging
        self.extras["true_objective_mean"] = self.true_objective.mean()
        self.extras["true_objective_min"] = self.true_objective.min()
        self.extras["true_objective_max"] = self.true_objective.max()

        rewards = [
            (fingertip_delta_rew, "fingertip_delta_rew"),
            (lifting_rew, "lifting_rew"),
            (lift_bonus_rew, "lift_bonus_rew"),
            (keypoint_rew, "keypoint_rew"),
            (bonus_rew, "bonus_rew"),
        ]

        episode_cumulative = dict()
        for rew_value, rew_name in rewards:
            self.rewards_episode[rew_name] += rew_value
            episode_cumulative[rew_name] = rew_value
        self.extras["rewards_episode"] = self.rewards_episode
        self.extras["episode_cumulative"] = episode_cumulative

        return self.rew_buf, is_success
```

```python
def compute_observations(self) -> Tuple[Tensor, int]:
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        self.object_state = self.root_state_tensor[self.object_indices, 0:13]
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self._palm_state = self.rigid_body_states[:, self.allegro_palm_handles]
        palm_pos = self._palm_state[..., 0:3]  # [num_envs, num_arms, 3]
        self._palm_rot = self._palm_state[..., 3:7]  # [num_envs, num_arms, 4]
        for arm_idx in range(self.num_arms):
            self.palm_center_pos[:, arm_idx] = palm_pos[:, arm_idx] + quat_rotate(
                self._palm_rot[:, arm_idx], self.palm_center_offset
            )

        self.fingertip_state = self.rigid_body_states[:, self.allegro_fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.fingertip_state[:, :, 0:3]
        self.fingertip_rot = self.fingertip_state[:, :, 3:7]

        if hasattr(self, "fingertip_pos_rel_object"):
            self.fingertip_pos_rel_object_prev[:, :, :] = self.fingertip_pos_rel_object
        else:
            self.fingertip_pos_rel_object_prev = None

        self.fingertip_pos_offset = torch.zeros_like(self.fingertip_pos).to(self.device)
        for arm_idx in range(self.num_arms):
            for i in range(self.num_fingertips):
                finger_idx = arm_idx * self.num_fingertips + i
                self.fingertip_pos_offset[:, finger_idx] = self.fingertip_pos[:, finger_idx] + quat_rotate(
                    self.fingertip_rot[:, finger_idx], self.fingertip_offsets[:, i]
                )

        obj_pos_repeat = self.object_pos.unsqueeze(1).repeat(1, self.num_arms * self.num_fingertips, 1)
        self.fingertip_pos_rel_object = self.fingertip_pos_offset - obj_pos_repeat
        self.curr_fingertip_distances = torch.norm(
            self.fingertip_pos_rel_object.view(self.num_envs, self.num_arms, self.num_fingertips, -1), dim=-1
        )

        # when episode ends or target changes we reset this to -1, this will initialize it to the actual distance on the 1st frame of the episode
        self.closest_fingertip_dist = torch.where(
            self.closest_fingertip_dist < 0.0, self.curr_fingertip_distances, self.closest_fingertip_dist
        )

        palm_center_repeat = self.palm_center_pos.unsqueeze(2).repeat(
            1, 1, self.num_fingertips, 1
        )  # [num_envs, num_arms, num_fingertips, 3] == [num_envs, 2, 4, 3]
        self.fingertip_pos_rel_palm = self.fingertip_pos_offset - palm_center_repeat.view(
            self.num_envs, self.num_arms * self.num_fingertips, 3
        )  # [num_envs, num_arms * num_fingertips, 3] == [num_envs, 8, 3]

        if self.fingertip_pos_rel_object_prev is None:
            self.fingertip_pos_rel_object_prev = self.fingertip_pos_rel_object.clone()

        for i in range(self.num_keypoints):
            self.obj_keypoint_pos[:, i] = self.object_pos + quat_rotate(
                self.object_rot, self.object_keypoint_offsets[:, i]
            )
            self.goal_keypoint_pos[:, i] = self.goal_pos + quat_rotate(
                self.goal_rot, self.object_keypoint_offsets[:, i]
            )

        self.keypoints_rel_goal = self.obj_keypoint_pos - self.goal_keypoint_pos

        palm_center_repeat = self.palm_center_pos.unsqueeze(2).repeat(1, 1, self.num_keypoints, 1)
        obj_kp_pos_repeat = self.obj_keypoint_pos.unsquee
```
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_two_arms_regrasping.py

```
class AllegroKukaTwoArmsRegrasping(AllegroKukaTwoArmsBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _load_additional_assets(self, object_asset_root, arm_y_offset)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def compute_kuka_reward(self)
    def _true_objective(self)
    def _extra_curriculum(self)

```python
def compute_kuka_reward(self) -> Tuple[Tensor, Tensor]:
        rew_buf, is_success = super().compute_kuka_reward()
        return rew_buf, is_success
```
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_two_arms_reorientation.py

```
class AllegroKukaTwoArmsReorientation(AllegroKukaTwoArmsBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _object_keypoint_offsets(self)
    def _load_additional_assets(self, object_asset_root, arm_pose)
    def _create_additional_objects(self, env_ptr, env_idx, object_asset_idx)
    def _after_envs_created(self)
    def _reset_target(self, env_ids)
    def _extra_object_indices(self, env_ids)
    def _extra_curriculum(self)
    def _true_objective(self)
```

### isaacgymenvs/tasks/allegro_kuka/allegro_kuka_utils.py

```
class DofParameters()
    """Joint/dof parameters."""
    def from_cfg(cfg)
def populate_dof_properties(hand_arm_dof_props, params, arm_dofs, hand_dofs)
def tolerance_curriculum(last_curriculum_update, frames_since_restart, curriculum_interval, prev_episode_successes, success_tolerance, initial_tolerance, target_tolerance, tolerance_curriculum_increment)
def interp_0_1(x_curr, x_initial, x_target)
def tolerance_successes_objective(success_tolerance, initial_tolerance, target_tolerance, successes)
```

### isaacgymenvs/tasks/allegro_kuka/generate_cuboids.py

```
def generate_assets(scales, min_volume, max_volume, generated_assets_dir, base_mesh, base_cube_size_m, filter_funcs)
def filter_thin_plates(scales)
def generate_default_cube(assets_dir, base_mesh, base_cube_size_m)
def generate_small_cuboids(assets_dir, base_mesh, base_cube_size_m)
def generate_big_cuboids(assets_dir, base_mesh, base_cube_size_m)
def filter_non_elongated(scales)
def generate_sticks(assets_dir, base_mesh, base_cube_size_m)
```

### isaacgymenvs/tasks/amp/humanoid_amp_base.py

```
class HumanoidAMPBase(VecTask)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def get_obs_size(self)
    def get_action_size(self)
    def create_sim(self)
    def reset_idx(self, env_ids)
    def set_char_color(self, col)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_pd_action_offset_scale(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _refresh_sim_tensors(self)
    def _compute_observations(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _reset_actors(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def render(self)
    def _build_key_body_ids_tensor(self, env_ptr, actor_handle)
    def _build_contact_body_ids_tensor(self, env_ptr, actor_handle)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
def dof_to_obs(pose)
def compute_humanoid_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs)
def compute_humanoid_reward(obs_buf)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, max_episode_length, enable_early_termination, termination_height)

```python
def compute_humanoid_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs):
    # type: (Tensor, Tensor, Tensor, Tensor, bool) -> Tensor
    root_pos = root_states[:, 0:3]
    root_rot = root_states[:, 3:7]
    root_vel = root_states[:, 7:10]
    root_ang_vel = root_states[:, 10:13]

    root_h = root_pos[:, 2:3]
    heading_rot = calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = quat_to_tan_norm(root_rot_obs)

    local_root_vel = my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand
    
    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], 
                                               heading_rot_expand.shape[2])
    local_end_pos = my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos)

    obs = torch.cat((root_h, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def compute_humanoid_reward(obs_buf):
    # type: (Tensor) -> Tensor
    reward = torch.ones_like(obs_buf[:, 0])
    return reward
```

```python
def _compute_reward(self, actions):
        self.rew_buf[:] = compute_humanoid_reward(self.obs_buf)
        return
```

```python
def _compute_observations(self, env_ids=None):
        obs = self._compute_humanoid_obs(env_ids)

        if (env_ids is None):
            self.obs_buf[:] = obs
        else:
            self.obs_buf[env_ids] = obs

        return
```
```

### isaacgymenvs/tasks/amp/poselib/poselib/core/backend/abstract.py

```
def register(name)
def _get_cls(name)
class NumpyEncoder(JSONEncoder)
    """Special json encoder for numpy types """
    def default(self, obj)
def json_numpy_obj_hook(dct)
class Serializable()
    """Implementation to read/write to file.
All class the is inherited from this class needs to implement to_dict() and 
from_dict()"""
    def from_dict(cls, dict_repr)
    def to_dict(self)
    def from_file(cls, path)
    def to_file(self, path)
```

### isaacgymenvs/tasks/amp/poselib/poselib/core/rotation3d.py

```
def quat_mul(a, b)
def quat_pos(x)
def quat_abs(x)
def quat_unit(x)
def quat_conjugate(x)
def quat_real(x)
def quat_imaginary(x)
def quat_norm_check(x)
def quat_normalize(q)
def quat_from_xyz(xyz)
def quat_identity(shape)
def quat_from_angle_axis(angle, axis, degree)
def quat_from_rotation_matrix(m)
def quat_mul_norm(x, y)
def quat_rotate(rot, vec)
def quat_inverse(x)
def quat_identity_like(x)
def quat_angle_axis(x)
def quat_yaw_rotation(x, z_up)
def transform_from_rotation_translation(r, t)
def transform_identity(shape)
def transform_rotation(x)
def transform_translation(x)
def transform_inverse(x)
def transform_identity_like(x)
def transform_mul(x, y)
def transform_apply(rot, vec)
def rot_matrix_det(x)
def rot_matrix_integrity_check(x)
def rot_matrix_from_quaternion(q)
def euclidean_to_rotation_matrix(x)
def euclidean_integrity_check(x)
def euclidean_translation(x)
def euclidean_inverse(x)
def euclidean_to_transform(transformation_matrix)
```

### isaacgymenvs/tasks/amp/poselib/poselib/core/tensor_utils.py

```
class TensorUtils(Serializable)
    def from_dict(cls, dict_repr)
    def to_dict(self)
def tensor_to_dict(x)
```

### isaacgymenvs/tasks/amp/poselib/poselib/skeleton/backend/fbx/fbx_backend.py

```
"""This script reads an fbx file and returns the joint names, parents, and transforms.

NOTE: It requires the Python FBX package to be installed."""
def fbx_to_npy(file_name_in, root_joint_name, fps)
def _get_frame_count(fbx_scene)
def _get_animation_curve(joint, fbx_scene)
def _get_skeleton(root_joint)
def _recursive_to_list(array)
def parse_fbx(file_name_in, root_joint_name, fps)
```

### isaacgymenvs/tasks/amp/poselib/poselib/skeleton/backend/fbx/fbx_read_wrapper.py

```
"""Script that reads in fbx files from python

This requires a configs file, which contains the command necessary to switch conda
environments to run the fbx reading script from python"""
def fbx_to_array(fbx_file_path, root_joint, fps)
```

### isaacgymenvs/tasks/amp/poselib/poselib/skeleton/skeleton3d.py

```
class SkeletonTree(Serializable)
    """A skeleton tree gives a complete description of a rigid skeleton. It describes a tree structure
over a list of nodes with their names indicated by strings. Each edge in the tree has a local
translation associated with it which describes the distance between the two nodes that it
connects. 

Basic Us"""
    def __init__(self, node_names, parent_indices, local_translation)
    def __len__(self)
    def __iter__(self)
    def __getitem__(self, item)
    def __repr__(self)
    def _indent(self, s)
    def node_names(self)
    def parent_indices(self)
    def local_translation(self)
    def num_joints(self)
    def from_dict(cls, dict_repr)
    def to_dict(self)
    def from_mjcf(cls, path)
    def parent_of(self, node_name)
    def index(self, node_name)
    def drop_nodes_by_names(self, node_names, pairwise_translation)
    def keep_nodes_by_names(self, node_names, pairwise_translation)
class SkeletonState(Serializable)
    """A skeleton state contains all the information needed to describe a static state of a skeleton.
It requires a skeleton tree, local/global rotation at each joint and the root translation.

Example:
    >>> t = SkeletonTree.from_mjcf(SkeletonTree.__example_mjcf_path__)
    >>> zero_pose = SkeletonState"""
    def __init__(self, tensor_backend, skeleton_tree, is_local)
    def __len__(self)
    def rotation(self)
    def _local_rotation(self)
    def _global_rotation(self)
    def is_local(self)
    def invariant_property(self)
    def num_joints(self)
    def skeleton_tree(self)
    def root_translation(self)
    def global_transformation(self)
    def global_rotation(self)
    def global_translation(self)
    def global_translation_xy(self)
    def global_translation_xz(self)
    def local_rotation(self)
    def local_transformation(self)
    def local_translation(self)
    def root_translation_xy(self)
    def global_root_rotation(self)
    def global_root_yaw_rotation(self)
    def local_translation_to_root(self)
    def local_rotation_to_root(self)
    def compute_forward_vector(self, left_shoulder_index, right_shoulder_index, left_hip_index, right_hip_index, gaussian_filter_width)
    def _to_state_vector(rot, rt)
    def from_dict(cls, dict_repr)
    def to_dict(self)
    def from_rotation_and_root_translation(cls, skeleton_tree, r, t, is_local)
    def zero_pose(cls, skeleton_tree)
    def local_repr(self)
    def global_repr(self)
    def _get_pairwise_average_translation(self)
    def _transfer_to(self, new_skeleton_tree)
    def drop_nodes_by_names(self, node_names, estimate_local_translation_from_states)
    def keep_nodes_by_names(self, node_names, estimate_local_translation_from_states)
    def _remapped_to(self, joint_mapping, target_skeleton_tree)
    def retarget_to(self, joint_mapping, source_tpose_local_rotation, source_tpose_root_translation, target_skeleton_tree, target_tpose_local_rotation, target_tpose_root_translation, rotation_to_target_skeleton, scale_to_target_skeleton, z_up)
    def retarget_to_by_tpose(self, joint_mapping, source_tpose, target_tpose, rotation_to_target_skeleton, scale_to_target_skeleton)
class SkeletonMotion(SkeletonState)
    def __init__(self, tensor_backend, skeleton_tree, is_local, fps)
    def clone(self)
    def invariant_property(self)
    def global_velocity(self)
    def global_angular_velocity(self)
    def fps(self)
    def time_delta(self)
    def global_root_velocity(self)
    def global_root_angular_velocity(self)
    def from_state_vector_and_velocity(cls, skeleton_tree, state_vector, global_velocity, global_angular_velocity, is_local, fps)
    def from_skeleton_state(cls, skeleton_state, fps)
    def _to_state_vector(rot, rt, vel, avel)
    def from_dict(cls, dict_repr)
    def to_dict(self)
    def from_fbx(cls, fbx_file_path, skeleton_tree, is_local, fps, root_joint, root_trans_index)
    def _compute_velocity(p, time_delta, guassian_filter)
    def _compute_angular_velocity(r, time_delta, guassian_filter)
    def crop(self, start, end, fps)
    def retarget_to(self, joint_mapping, source_tpose_local_rotation, source_tpose_root_translation, target_skeleton_tree, target_tpose_local_rotation, target_tpose_root_translation, rotation_to_target_skeleton, scale_to_target_skeleton, z_up)
    def retarget_to_by_tpose(self, joint_mapping, source_tpose, target_tpose, rotation_to_target_skeleton, scale_to_target_skeleton, z_up)
```

### isaacgymenvs/tasks/amp/poselib/poselib/visualization/common.py

```
def plot_skeleton_state(skeleton_state, task_name)
def plot_skeleton_states(skeleton_state, skip_n, task_name)
def plot_skeleton_motion(skeleton_motion, skip_n, task_name)
def plot_skeleton_motion_interactive_base(skeleton_motion, task_name)
def plot_skeleton_motion_interactive(skeleton_motion, task_name)
def plot_skeleton_motion_interactive_multiple()
```

### isaacgymenvs/tasks/amp/poselib/poselib/visualization/core.py

```
"""The base abstract classes for plotter and the plotting tasks. It describes how the plotter
deals with the tasks in the general cases"""
class BasePlotterTask(object)
    def __init__(self, task_name, task_type)
    def task_name(self)
    def task_type(self)
    def get_scoped_name(self, name)
    def __iter__(self)
class BasePlotterTasks(object)
    def __init__(self, tasks)
    def __iter__(self)
class BasePlotter(object)
    """An abstract plotter which deals with a plotting task. The children class needs to implement
the functions to create/update the objects according to the task given"""
    def __init__(self, task)
    def task_primitives(self)
    def create(self, task)
    def update(self)
    def _update_impl(self, task_list)
    def _create_impl(self, task_list)
```

### isaacgymenvs/tasks/amp/poselib/poselib/visualization/plt_plotter.py

```
"""The matplotlib plotter implementation for all the primitive tasks (in our case: lines and
dots)"""
class Matplotlib2DPlotter(BasePlotter)
    def __init__(self, task)
    def ax(self)
    def fig(self)
    def show(self)
    def _min(self, x, y)
    def _max(self, x, y)
    def _init_lim(self)
    def _update_lim(self, xs, ys)
    def _set_lim(self)
    def _lines_extract_xy_impl(index, lines_task)
    def _trail_extract_xy_impl(index, trail_task)
    def _lines_create_impl(self, lines_task)
    def _lines_update_impl(self, lines_task)
    def _dots_create_impl(self, dots_task)
    def _dots_update_impl(self, dots_task)
    def _trail_create_impl(self, trail_task)
    def _trail_update_impl(self, trail_task)
    def _create_impl(self, task_list)
    def _update_impl(self, task_list)
    def _set_aspect_equal_2d(self, zero_centered)
    def _draw(self)
class Matplotlib3DPlotter(BasePlotter)
    def __init__(self, task)
    def ax(self)
    def fig(self)
    def show(self)
    def _min(self, x, y)
    def _max(self, x, y)
    def _init_lim(self)
    def _update_lim(self, xs, ys, zs)
    def _set_lim(self)
    def _lines_extract_xyz_impl(index, lines_task)
    def _trail_extract_xyz_impl(index, trail_task)
    def _lines_create_impl(self, lines_task)
    def _lines_update_impl(self, lines_task)
    def _dots_create_impl(self, dots_task)
    def _dots_update_impl(self, dots_task)
    def _trail_create_impl(self, trail_task)
    def _trail_update_impl(self, trail_task)
    def _create_impl(self, task_list)
    def _update_impl(self, task_list)
    def _set_aspect_equal_3d(self)
    def _draw(self)
```

### isaacgymenvs/tasks/amp/poselib/poselib/visualization/simple_plotter_tasks.py

```
"""This is where all the task primitives are defined"""
class DrawXDLines(BasePlotterTask)
    def __init__(self, task_name, lines, color, line_width, alpha, influence_lim)
    def influence_lim(self)
    def raw_data(self)
    def color(self)
    def line_width(self)
    def alpha(self)
    def dim(self)
    def name(self)
    def update(self, lines)
    def __getitem__(self, index)
    def __len__(self)
    def __iter__(self)
class DrawXDDots(BasePlotterTask)
    def __init__(self, task_name, dots, color, marker_size, alpha, influence_lim)
    def update(self, dots)
    def __getitem__(self, index)
    def __len__(self)
    def __iter__(self)
    def influence_lim(self)
    def raw_data(self)
    def color(self)
    def marker_size(self)
    def alpha(self)
    def dim(self)
    def name(self)
class DrawXDTrail(DrawXDDots)
    def line_width(self)
    def name(self)
class Draw2DLines(DrawXDLines)
    def dim(self)
class Draw3DLines(DrawXDLines)
    def dim(self)
class Draw2DDots(DrawXDDots)
    def dim(self)
class Draw3DDots(DrawXDDots)
    def dim(self)
class Draw2DTrail(DrawXDTrail)
    def dim(self)
class Draw3DTrail(DrawXDTrail)
    def dim(self)
```

### isaacgymenvs/tasks/amp/poselib/poselib/visualization/skeleton_plotter_tasks.py

```
"""This is where all skeleton related complex tasks are defined (skeleton state and skeleton
motion)"""
class Draw3DSkeletonState(BasePlotterTask)
    def __init__(self, task_name, skeleton_state, joints_color, lines_color, alpha)
    def name(self)
    def update(self, skeleton_state)
    def _get_lines_and_dots(skeleton_state)
    def _update(self, lines, dots)
    def __iter__(self)
class Draw3DSkeletonMotion(BasePlotterTask)
    def __init__(self, task_name, skeleton_motion, frame_index, joints_color, lines_color, velocity_color, angular_velocity_color, trail_color, trail_length, alpha)
    def name(self)
    def update(self, frame_index, reset_trail, skeleton_motion)
    def _get_vel_and_avel(skeleton_motion)
    def _update(self, vel_lines, avel_lines)
    def __iter__(self)
class Draw3DSkeletonMotions(BasePlotterTask)
    def __init__(self, skeleton_motion_tasks)
    def name(self)
    def update(self, frame_index)
    def __iter__(self)
```

### isaacgymenvs/tasks/amp/poselib/retarget_motion.py

```
def project_joints(motion)
def main()
```

### isaacgymenvs/tasks/amp/utils_amp/amp_torch_utils.py

```
def my_quat_rotate(q, v)
def quat_to_angle_axis(q)
def angle_axis_to_exp_map(angle, axis)
def quat_to_exp_map(q)
def quat_to_tan_norm(q)
def euler_xyz_to_exp_map(roll, pitch, yaw)
def exp_map_to_angle_axis(exp_map)
def exp_map_to_quat(exp_map)
def slerp(q0, q1, t)
def calc_heading(q)
def calc_heading_quat(q)
def calc_heading_quat_inv(q)
```

### isaacgymenvs/tasks/amp/utils_amp/data_tree.py

```
class data_tree(object)
    def __init__(self, name)
    def add_node(self, dict_hierachy, mocap_data)
    def summarize_length(self)
    def to_dict(self, verbose)
    def name(self)
    def picked(self)
    def total_length(self)
    def water_floating_algorithm(self)
    def assign_probability(self, total_prob)
def parse_dataset(env, args)
def save_tsv_files(base_dir, name, data_dict)
```

### isaacgymenvs/tasks/amp/utils_amp/gym_util.py

```
def setup_gym_viewer(config)
def initialize_gym(config)
def configure_gym(gym, config)
def parse_states_from_reference_states(reference_states, progress)
def parse_states_from_reference_states_with_motion_id(precomputed_state, progress, motion_id)
def parse_dof_state_with_motion_id(precomputed_state, dof_state, progress, motion_id)
def get_flatten_ids(precomputed_state)
def parse_states_from_reference_states_with_global_id(precomputed_state, global_id)
def get_robot_states_from_torch_tensor(config, ts, global_quats, vels, avels, init_rot, progress, motion_length, actions, relative_rot, motion_id, num_motion, motion_onehot_matrix)
def get_xyzoffset(start_ts, end_ts, root_yaw_inv)
```

### isaacgymenvs/tasks/amp/utils_amp/logger.py

```
def colored(text, color)
class _MyFormatter(Formatter)
    """@brief:
    a class to make sure the format could be used"""
    def format(self, record)
class GLOBAL_PATH(object)
    def __init__(self, path)
    def _set_path(self, path)
    def _get_path(self)
def set_file_handler(path, prefix, time_str)
def _get_path()
```

### isaacgymenvs/tasks/amp/utils_amp/motion_lib.py

```
class MotionLib()
    def __init__(self, motion_file, num_dofs, key_body_ids, device)
    def num_motions(self)
    def get_total_length(self)
    def get_motion(self, motion_id)
    def sample_motions(self, n)
    def sample_time(self, motion_ids, truncate_time)
    def get_motion_length(self, motion_ids)
    def get_motion_state(self, motion_ids, motion_times)
    def _load_motions(self, motion_file)
    def _fetch_motion_files(self, motion_file)
    def _calc_frame_blend(self, time, len, num_frames, dt)
    def _get_num_bodies(self)
    def _compute_motion_dof_vels(self, motion)
    def _local_rotation_to_dof(self, local_rot)
    def _local_rotation_to_dof_vel(self, local_rot0, local_rot1, dt)
```

### isaacgymenvs/tasks/ant.py

```
class Ant(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_true_objective(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_ant_reward(obs_buf, reset_buf, progress_buf, actions, up_weight, heading_weight, potentials, prev_potentials, actions_cost_scale, energy_cost_scale, joints_at_limit_cost_scale, termination_height, death_cost, max_episode_length)
def compute_ant_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, basis_vec0, basis_vec1, up_axis_idx)

```python
def compute_ant_reward(
    obs_buf,
    reset_buf,
    progress_buf,
    actions,
    up_weight,
    heading_weight,
    potentials,
    prev_potentials,
    actions_cost_scale,
    energy_cost_scale,
    joints_at_limit_cost_scale,
    termination_height,
    death_cost,
    max_episode_length
):
    # type: (Tensor, Tensor, Tensor, Tensor, float, float, Tensor, Tensor, float, float, float, float, float, float) -> Tuple[Tensor, Tensor]

    # reward from direction headed
    heading_weight_tensor = torch.ones_like(obs_buf[:, 11]) * heading_weight
    heading_reward = torch.where(obs_buf[:, 11] > 0.8, heading_weight_tensor, heading_weight * obs_buf[:, 11] / 0.8)

    # aligning up axis of ant and environment
    up_reward = torch.zeros_like(heading_reward)
    up_reward = torch.where(obs_buf[:, 10] > 0.93, up_reward + up_weight, up_reward)

    # energy penalty for movement
    actions_cost = torch.sum(actions ** 2, dim=-1)
    electricity_cost = torch.sum(torch.abs(actions * obs_buf[:, 20:28]), dim=-1)
    dof_at_limit_cost = torch.sum(obs_buf[:, 12:20] > 0.99, dim=-1)

    # reward for duration of staying alive
    alive_reward = torch.ones_like(potentials) * 0.5
    progress_reward = potentials - prev_potentials

    total_reward = progress_reward + alive_reward + up_reward + heading_reward - \
        actions_cost_scale * actions_cost - energy_cost_scale * electricity_cost - dof_at_limit_cost * joints_at_limit_cost_scale

    # adjust reward for fallen agents
    total_reward = torch.where(obs_buf[:, 0] < termination_height, torch.ones_like(total_reward) * death_cost, total_reward)

    # reset agents
    reset = torch.where(obs_buf[:, 0] < termination_height, torch.ones_like(reset_buf), reset_buf)
    reset = torch.where(progress_buf >= max_episode_length - 1, torch.ones_like(reset_buf), reset)

    return total_reward, reset
```

```python
def compute_ant_observations(obs_buf, root_states, targets, potentials,
                             inv_start_rot, dof_pos, dof_vel,
                             dof_limits_lower, dof_limits_upper, dof_vel_scale,
                             sensor_force_torques, actions, dt, contact_force_scale,
                             basis_vec0, basis_vec1, up_axis_idx):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, float, Tensor, Tensor, float, float, Tensor, Tensor, int) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor]

    torso_position = root_states[:, 0:3]
    torso_rotation = root_states[:, 3:7]
    velocity = root_states[:, 7:10]
    ang_velocity = root_states[:, 10:13]

    to_target = targets - torso_position
    to_target[:, 2] = 0.0

    prev_potentials_new = potentials.clone()
    potentials = -torch.norm(to_target, p=2, dim=-1) / dt

    torso_quat, up_proj, heading_proj, up_vec, heading_vec = compute_heading_and_up(
        torso_rotation, inv_start_rot, to_target, basis_vec0, basis_vec1, 2)

    vel_loc, angvel_loc, roll, pitch, yaw, angle_to_target = compute_rot(
        torso_quat, velocity, ang_velocity, targets, torso_position)

    dof_pos_scaled = unscale(dof_pos, dof_limits_lower, dof_limits_upper)

    # obs_buf shapes: 1, 3, 3, 1, 1, 1, 1, 1, num_dofs(8), num_dofs(8), 24, num_dofs(8)
    obs = torch.cat((torso_position[:, up_axis_idx].view(-1, 1), vel_loc, angvel_loc,
                     yaw.unsqueeze(-1), roll.unsqueeze(-1), angle_to_target.unsqueeze(-1),
                     up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1), dof_pos_scaled,
                     dof_vel * dof_vel_scale, sensor_force_torques.view(-1, 24) * contact_force_scale,
                     actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:] = compute_ant_reward(
            self.obs_buf,
            self.reset_buf,
            self.progress_buf,
            self.actions,
            self.up_weight,
            self.heading_weight,
            self.potentials,
            self.prev_potentials,
            self.actions_cost_scale,
            self.energy_cost_scale,
            self.joints_at_limit_cost_scale,
            self.termination_height,
            self.death_cost,
            self.max_episode_length
        )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)

        self.obs_buf[:], self.potentials[:], self.prev_potentials[:], self.up_vec[:], self.heading_vec[:] = compute_ant_observations(
            self.obs_buf, self.root_states, self.targets, self.potentials,
            self.inv_start_rot, self.dof_pos, self.dof_vel,
            self.dof_limits_lower, self.dof_limits_upper, self.dof_vel_scale,
            self.vec_sensor_tensor, self.actions, self.dt, self.contact_force_scale,
            self.basis_vec0, self.basis_vec1, self.up_axis_idx)
```
```

### isaacgymenvs/tasks/anymal.py

```
class Anymal(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
def compute_anymal_reward(root_states, commands, torques, contact_forces, knee_indices, episode_lengths, rew_scales, base_index, max_episode_length)
def compute_anymal_observations(root_states, commands, dof_pos, default_dof_pos, dof_vel, gravity_vec, actions, lin_vel_scale, ang_vel_scale, dof_pos_scale, dof_vel_scale)

```python
def compute_anymal_reward(
    # tensors
    root_states,
    commands,
    torques,
    contact_forces,
    knee_indices,
    episode_lengths,
    # Dict
    rew_scales,
    # other
    base_index,
    max_episode_length
):
    # (reward, reset, feet_in air, feet_air_time, episode sums)
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Dict[str, float], int, int) -> Tuple[Tensor, Tensor]

    # prepare quantities (TODO: return from obs ?)
    base_quat = root_states[:, 3:7]
    base_lin_vel = quat_rotate_inverse(base_quat, root_states[:, 7:10])
    base_ang_vel = quat_rotate_inverse(base_quat, root_states[:, 10:13])

    # velocity tracking reward
    lin_vel_error = torch.sum(torch.square(commands[:, :2] - base_lin_vel[:, :2]), dim=1)
    ang_vel_error = torch.square(commands[:, 2] - base_ang_vel[:, 2])
    rew_lin_vel_xy = torch.exp(-lin_vel_error/0.25) * rew_scales["lin_vel_xy"]
    rew_ang_vel_z = torch.exp(-ang_vel_error/0.25) * rew_scales["ang_vel_z"]

    # torque penalty
    rew_torque = torch.sum(torch.square(torques), dim=1) * rew_scales["torque"]

    total_reward = rew_lin_vel_xy + rew_ang_vel_z + rew_torque
    total_reward = torch.clip(total_reward, 0., None)
    # reset agents
    reset = torch.norm(contact_forces[:, base_index, :], dim=1) > 1.
    reset = reset | torch.any(torch.norm(contact_forces[:, knee_indices, :], dim=2) > 1., dim=1)
    time_out = episode_lengths >= max_episode_length - 1  # no terminal reward for time-outs
    reset = reset | time_out

    return total_reward.detach(), reset
```

```python
def compute_anymal_observations(root_states,
                                commands,
                                dof_pos,
                                default_dof_pos,
                                dof_vel,
                                gravity_vec,
                                actions,
                                lin_vel_scale,
                                ang_vel_scale,
                                dof_pos_scale,
                                dof_vel_scale
                                ):

    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, float, float, float, float) -> Tensor
    base_quat = root_states[:, 3:7]
    base_lin_vel = quat_rotate_inverse(base_quat, root_states[:, 7:10]) * lin_vel_scale
    base_ang_vel = quat_rotate_inverse(base_quat, root_states[:, 10:13]) * ang_vel_scale
    projected_gravity = quat_rotate(base_quat, gravity_vec)
    dof_pos_scaled = (dof_pos - default_dof_pos) * dof_pos_scale

    commands_scaled = commands*torch.tensor([lin_vel_scale, lin_vel_scale, ang_vel_scale], requires_grad=False, device=commands.device)

    obs = torch.cat((base_lin_vel,
                     base_ang_vel,
                     projected_gravity,
                     commands_scaled,
                     dof_pos_scaled,
                     dof_vel*dof_vel_scale,
                     actions
                     ), dim=-1)

    return obs
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:] = compute_anymal_reward(
            # tensors
            self.root_states,
            self.commands,
            self.torques,
            self.contact_forces,
            self.knee_indices,
            self.progress_buf,
            # Dict
            self.rew_scales,
            # other
            self.base_index,
            self.max_episode_length,
        )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)  # done in step
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        self.obs_buf[:] = compute_anymal_observations(  # tensors
                                                        self.root_states,
                                                        self.commands,
                                                        self.dof_pos,
                                                        self.default_dof_pos,
                                                        self.dof_vel,
                                                        self.gravity_vec,
                                                        self.actions,
                                                        # scales
                                                        self.lin_vel_scale,
                                                        self.ang_vel_scale,
                                                        self.dof_pos_scale,
                                                        self.dof_vel_scale
        )
```
```

### isaacgymenvs/tasks/anymal_terrain.py

```
class AnymalTerrain(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _get_noise_scale_vec(self, cfg)
    def _create_ground_plane(self)
    def _create_trimesh(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def check_termination(self)
    def compute_observations(self)
    def compute_reward(self)
    def reset_idx(self, env_ids)
    def update_terrain_level(self, env_ids)
    def push_robots(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def init_height_points(self)
    def get_heights(self, env_ids)
class Terrain()
    def __init__(self, cfg, num_robots)
    def randomized_terrain(self)
    def curiculum(self, num_robots, num_terrains, num_levels)
def quat_apply_yaw(quat, vec)
def wrap_to_pi(angles)

```python
def compute_observations(self):
        self.measured_heights = self.get_heights()
        heights = torch.clip(self.root_states[:, 2].unsqueeze(1) - 0.5 - self.measured_heights, -1, 1.) * self.height_meas_scale
        self.obs_buf = torch.cat((  self.base_lin_vel * self.lin_vel_scale,
                                    self.base_ang_vel  * self.ang_vel_scale,
                                    self.projected_gravity,
                                    self.commands[:, :3] * self.commands_scale,
                                    self.dof_pos * self.dof_pos_scale,
                                    self.dof_vel * self.dof_vel_scale,
                                    heights,
                                    self.actions
                                    ), dim=-1)
```

```python
def compute_reward(self):
        # velocity tracking reward
        lin_vel_error = torch.sum(torch.square(self.commands[:, :2] - self.base_lin_vel[:, :2]), dim=1)
        ang_vel_error = torch.square(self.commands[:, 2] - self.base_ang_vel[:, 2])
        rew_lin_vel_xy = torch.exp(-lin_vel_error/0.25) * self.rew_scales["lin_vel_xy"]
        rew_ang_vel_z = torch.exp(-ang_vel_error/0.25) * self.rew_scales["ang_vel_z"]

        # other base velocity penalties
        rew_lin_vel_z = torch.square(self.base_lin_vel[:, 2]) * self.rew_scales["lin_vel_z"]
        rew_ang_vel_xy = torch.sum(torch.square(self.base_ang_vel[:, :2]), dim=1) * self.rew_scales["ang_vel_xy"]

        # orientation penalty
        rew_orient = torch.sum(torch.square(self.projected_gravity[:, :2]), dim=1) * self.rew_scales["orient"]

        # base height penalty
        rew_base_height = torch.square(self.root_states[:, 2] - 0.52) * self.rew_scales["base_height"] # TODO add target base height to cfg

        # torque penalty
        rew_torque = torch.sum(torch.square(self.torques), dim=1) * self.rew_scales["torque"]

        # joint acc penalty
        rew_joint_acc = torch.sum(torch.square(self.last_dof_vel - self.dof_vel), dim=1) * self.rew_scales["joint_acc"]

        # collision penalty
        knee_contact = torch.norm(self.contact_forces[:, self.knee_indices, :], dim=2) > 1.
        rew_collision = torch.sum(knee_contact, dim=1) * self.rew_scales["collision"] # sum vs any ?

        # stumbling penalty
        stumble = (torch.norm(self.contact_forces[:, self.feet_indices, :2], dim=2) > 5.) * (torch.abs(self.contact_forces[:, self.feet_indices, 2]) < 1.)
        rew_stumble = torch.sum(stumble, dim=1) * self.rew_scales["stumble"]

        # action rate penalty
        rew_action_rate = torch.sum(torch.square(self.last_actions - self.actions), dim=1) * self.rew_scales["action_rate"]

        # air time reward
        # contact = torch.norm(contact_forces[:, feet_indices, :], dim=2) > 1.
        contact = self.contact_forces[:, self.feet_indices, 2] > 1.
        first_contact = (self.feet_air_time > 0.) * contact
        self.feet_air_time += self.dt
        rew_airTime = torch.sum((self.feet_air_time - 0.5) * first_contact, dim=1) * self.rew_scales["air_time"] # reward only on first contact with the ground
        rew_airTime *= torch.norm(self.commands[:, :2], dim=1) > 0.1 #no reward for zero command
        self.feet_air_time *= ~contact

        # cosmetic penalty for hip motion
        rew_hip = torch.sum(torch.abs(self.dof_pos[:, [0, 3, 6, 9]] - self.default_dof_pos[:, [0, 3, 6, 9]]), dim=1)* self.rew_scales["hip"]

        # total reward
        self.rew_buf = rew_lin_vel_xy + rew_ang_vel_z + rew_lin_vel_z + rew_ang_vel_xy + rew_orient + rew_base_height +\
                    rew_torque + rew_joint_acc + rew_collision + rew_action_rate + rew_airTime + rew_hip + rew_stumble
        self.rew_buf = torch.clip(self.rew_buf, min=0., max=None)

        # add termination reward
        self.rew_buf += self.rew_scales["termination"] * self.reset_buf * ~self.timeout_buf

        # log episode reward sums
        self.episode_sums["lin_vel_xy"] += rew_lin_vel_xy
        self.episode_sums["ang_vel_z"] += rew_ang_vel_z
        self.episode_sums["lin_vel_z"] += rew_lin_vel_z
        self.episode_sums["ang_vel_xy"] += rew_ang_vel_xy
        self.episode_sums["orient"] += rew_orient
        self.episode_sums["torques"] += rew_torque
        self.episode_sums["joint_acc"] += rew_joint_acc
        self.episode_sums["collision"] += rew_collision
        self.episode_sums["stumble"] += rew_stumble
        self.episode_sums["action_rate"] += rew_action_rate
        self.episode_sums["air_time"] += rew_airTime
        self.episode_sums["base_height"] += rew_base_height
        self.episode_sums["hip"] += rew_hip
```
```

### isaacgymenvs/tasks/ball_balance.py

```
def _indent_xml(elem, level)
class BallBalance(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_balance_bot_asset(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_observations(self)
    def compute_reward(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, _actions)
    def post_physics_step(self)
def compute_bbot_reward(tray_positions, ball_positions, ball_velocities, ball_radius, reset_buf, progress_buf, max_episode_length)

```python
def compute_bbot_reward(tray_positions, ball_positions, ball_velocities, ball_radius, reset_buf, progress_buf, max_episode_length):
    # type: (Tensor, Tensor, Tensor, float, Tensor, Tensor, float) -> Tuple[Tensor, Tensor]
    # calculating the norm for ball distance to desired height above the ground plane (i.e. 0.7)
    ball_dist = torch.sqrt(ball_positions[..., 0] * ball_positions[..., 0] +
                           (ball_positions[..., 2] - 0.7) * (ball_positions[..., 2] - 0.7) +
                           (ball_positions[..., 1]) * ball_positions[..., 1])
    ball_speed = torch.sqrt(ball_velocities[..., 0] * ball_velocities[..., 0] +
                            ball_velocities[..., 1] * ball_velocities[..., 1] +
                            ball_velocities[..., 2] * ball_velocities[..., 2])
    pos_reward = 1.0 / (1.0 + ball_dist)
    speed_reward = 1.0 / (1.0 + ball_speed)
    reward = pos_reward * speed_reward

    reset = torch.where(progress_buf >= max_episode_length - 1, torch.ones_like(reset_buf), reset_buf)
    reset = torch.where(ball_positions[..., 2] < ball_radius * 1.5, torch.ones_like(reset_buf), reset)

    return reward, reset
```

```python
def compute_observations(self):
        #print("~!~!~!~! Computing obs")

        actuated_dof_indices = torch.tensor([1, 3, 5], device=self.device)
        #print(self.dof_states[:, actuated_dof_indices, :])

        self.obs_buf[..., 0:3] = self.dof_positions[..., actuated_dof_indices]
        self.obs_buf[..., 3:6] = self.dof_velocities[..., actuated_dof_indices]
        self.obs_buf[..., 6:9] = self.ball_positions
        self.obs_buf[..., 9:12] = self.ball_linvels
        self.obs_buf[..., 12:15] = self.sensor_forces[..., 0] / 20  # !!! lousy normalization
        self.obs_buf[..., 15:18] = self.sensor_torques[..., 0] / 20  # !!! lousy normalization
        self.obs_buf[..., 18:21] = self.sensor_torques[..., 1] / 20  # !!! lousy normalization
        self.obs_buf[..., 21:24] = self.sensor_torques[..., 2] / 20  # !!! lousy normalization

        return self.obs_buf
```

```python
def compute_reward(self):
        self.rew_buf[:], self.reset_buf[:] = compute_bbot_reward(
            self.tray_positions,
            self.ball_positions,
            self.ball_linvels,
            self.ball_radius,
            self.reset_buf, self.progress_buf, self.max_episode_length
        )
```
```

### isaacgymenvs/tasks/base/vec_task.py

```
def _create_sim_once(gym)
class Env(ABC)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless)
    def allocate_buffers(self)
    def step(self, actions)
    def reset(self)
    def reset_idx(self, env_ids)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
class VecTask(Env)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def set_viewer(self)
    def allocate_buffers(self)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def get_state(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def step(self, actions)
    def zero_actions(self)
    def reset_idx(self, env_idx)
    def reset(self)
    def reset_done(self)
    def render(self, mode)
    def __parse_sim_params(self, physics_engine, config_sim)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)

```python
def observation_space(self) -> gym.Space:
        """Get the environment's observation space."""
        return self.obs_space
```
```

### isaacgymenvs/tasks/cartpole.py

```
class Cartpole(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self)
    def compute_observations(self, env_ids)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_cartpole_reward(pole_angle, pole_vel, cart_vel, cart_pos, reset_dist, reset_buf, progress_buf, max_episode_length)

```python
def compute_cartpole_reward(pole_angle, pole_vel, cart_vel, cart_pos,
                            reset_dist, reset_buf, progress_buf, max_episode_length):
    # type: (Tensor, Tensor, Tensor, Tensor, float, Tensor, Tensor, float) -> Tuple[Tensor, Tensor]

    # reward is combo of angle deviated from upright, velocity of cart, and velocity of pole moving
    reward = 1.0 - pole_angle * pole_angle - 0.01 * torch.abs(cart_vel) - 0.005 * torch.abs(pole_vel)

    # adjust reward for reset agents
    reward = torch.where(torch.abs(cart_pos) > reset_dist, torch.ones_like(reward) * -2.0, reward)
    reward = torch.where(torch.abs(pole_angle) > np.pi / 2, torch.ones_like(reward) * -2.0, reward)

    reset = torch.where(torch.abs(cart_pos) > reset_dist, torch.ones_like(reset_buf), reset_buf)
    reset = torch.where(torch.abs(pole_angle) > np.pi / 2, torch.ones_like(reset_buf), reset)
    reset = torch.where(progress_buf >= max_episode_length - 1, torch.ones_like(reset_buf), reset)

    return reward, reset
```

```python
def compute_reward(self):
        # retrieve environment observations from buffer
        pole_angle = self.obs_buf[:, 2]
        pole_vel = self.obs_buf[:, 3]
        cart_vel = self.obs_buf[:, 1]
        cart_pos = self.obs_buf[:, 0]

        self.rew_buf[:], self.reset_buf[:] = compute_cartpole_reward(
            pole_angle, pole_vel, cart_vel, cart_pos,
            self.reset_dist, self.reset_buf, self.progress_buf, self.max_episode_length
        )
```

```python
def compute_observations(self, env_ids=None):
        if env_ids is None:
            env_ids = np.arange(self.num_envs)

        self.gym.refresh_dof_state_tensor(self.sim)

        self.obs_buf[env_ids, 0] = self.dof_pos[env_ids, 0].squeeze()
        self.obs_buf[env_ids, 1] = self.dof_vel[env_ids, 0].squeeze()
        self.obs_buf[env_ids, 2] = self.dof_pos[env_ids, 1].squeeze()
        self.obs_buf[env_ids, 3] = self.dof_vel[env_ids, 1].squeeze()

        return self.obs_buf
```
```

### isaacgymenvs/tasks/dextreme/adr_vec_task.py

```
class RolloutWorkerModes()
class EnvDextreme(Env)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless, use_dict_obs)
    def get_env_state(self)
    def set_env_state(self, env_state)
class VecTaskDextreme(EnvDextreme, VecTask)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless, use_dict_obs)
    def allocate_buffers(self)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def get_state(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def step(self, actions)
    def reset(self)
    def get_env_state(self)
    def set_env_state(self, env_state)
    def get_randomization_dict(self, dr_params, obs_shape)
class ADRVecTask(VecTaskDextreme)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, headless, use_dict_obs)
    def get_current_adr_params(self, dr_params)
    def get_dr_params_by_env_id(self, env_id, default_dr_params, current_adr_params)
    def modify_adr_param(self, param, direction, adr_param_dict, param_limit)
    def env_ids_from_mask(mask)
    def sample_adr_tensor(self, param_name, env_ids)
    def get_adr_tensor(self, param_name, env_ids)
    def recycle_envs(self, recycle_envs)
    def adr_update(self, rand_envs, adr_objective)
    def apply_randomizations(self, dr_params, randomize_buf, adr_objective, randomisation_callback)
```

### isaacgymenvs/tasks/dextreme/allegro_hand_dextreme.py

```
class AllegroHandDextreme(ADRVecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def get_env_state(self)
    def get_save_tensors(self)
    def save_step(self)
    def get_num_obs_dict(self, num_dofs)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_poses_wrt_wrist(self, object_pose, palm_link_pose, goal_pose)
    def convert_pos_quat_to_mat(self, obj_pose_pos_quat)
    def compute_observations(self)
    def get_random_quat(self, env_ids)
    def reset_target_pose(self, env_ids, apply_reset)
    def get_relative_rot(self, obj_rot, goal_rot)
    def get_random_cube_observation(self, current_cube_pose)
    def reset_idx(self, env_ids, goal_env_ids)
    def get_rna_alpha(self)
    def get_random_network_adversary_action(self, canonical_action)
    def update_action_moving_average(self)
    def pre_physics_step(self, actions)
    def apply_action_noise_latency(self)
    def apply_actions(self, actions)
    def apply_random_forces(self)
    def post_physics_step(self)
    def track_dr_params(self)
    def _read_cfg(self)
    def _init_pre_sim_buffers(self)
    def _init_post_sim_buffers(self)
    def randomisation_callback(self, param_name, param_val, env_id, actor)
class AllegroHandDextremeADR(AllegroHandDextreme)
    def _init_pre_sim_buffers(self)
    def sample_discrete_adr(self, param_name, env_ids)
    def sample_gaussian_adr(self, param_name, env_ids, trailing_dim)
    def get_rna_alpha(self)
    def apply_randomizations(self, dr_params, randomize_buf, adr_objective, randomisation_callback)
    def create_sim(self)
    def apply_action_noise_latency(self)
    def compute_observations(self)
    def _read_cfg(self)
class AllegroHandDextremeManualDR(AllegroHandDextreme)
    def _init_post_sim_buffers(self)
    def get_num_obs_dict(self, num_dofs)
    def get_rna_alpha(self)
    def create_sim(self)
    def apply_randomizations(self, dr_params, randomize_buf, adr_objective, randomisation_callback)
    def apply_action_noise_latency(self)
    def compute_observations(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, hold_count_buf, cur_targets, prev_targets, hand_dof_vel, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, action_delta_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, num_success_hold_steps)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def unique_cube_rotations_3d()

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, hold_count_buf, cur_targets, prev_targets, hand_dof_vel, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float, action_delta_penalty_scale: float, #max_velocity: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, num_success_hold_steps: int
) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor]:
    # Distance from the hand to the object
    goal_dist = torch.norm(object_pos - target_pos, p=2, dim=-1)

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist * dist_reward_scale
    rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty =  action_penalty_scale * torch.sum(actions ** 2, dim=-1)
    action_delta_penalty = action_delta_penalty_scale * torch.sum((cur_targets - prev_targets) ** 2, dim=-1)
  
    max_velocity = 5.0 #rad/s
    vel_tolerance = 1.0
    velocity_penalty_coef = -0.05

    # todo add actions regularization

    velocity_penalty = velocity_penalty_coef * torch.sum((hand_dof_vel/(max_velocity - vel_tolerance)) ** 2, dim=-1)

    # Find out which envs hit the goal and update successes count
    goal_reached = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.ones_like(reset_goal_buf), reset_goal_buf)
    hold_count_buf = torch.where(goal_reached, hold_count_buf + 1, torch.zeros_like(goal_reached))

    goal_resets = torch.where(hold_count_buf > num_success_hold_steps, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reach_goal_rew = (goal_resets == 1) * reach_goal_bonus

    # Fall penalty: distance to the goal is larger than a threashold
    fall_rew = (goal_dist >= fall_dist) * fall_penalty

    # Check env termination conditions, including maximum success number
    resets = torch.where(goal_dist >= fall_dist, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)

    timed_out = progress_buf >= max_episode_length - 1
    resets = torch.where(timed_out, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    timeout_rew = timed_out * 0.5 * fall_penalty

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = dist_rew + rot_rew + action_penalty + action_delta_penalty + velocity_penalty + reach_goal_rew + fall_rew + timeout_rew

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, hold_count_buf, successes, cons_successes, \
        dist_rew, rot_rew, action_penalty, action_delta_penalty, velocity_penalty, reach_goal_rew, fall_rew, timeout_rew
```

```python
def compute_reward(self, actions):

        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], \
        self.hold_count_buf[:], self.successes[:], self.consecutive_successes[:], \
        dist_rew, rot_rew, action_penalty, action_delta_penalty, velocity_penalty, reach_goal_rew, fall_rew, timeout_rew = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.hold_count_buf, self.cur_targets, self.prev_targets,
            self.dof_vel, self.successes, self.consecutive_successes, self.max_episode_length,
            self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.dist_reward_scale, self.rot_reward_scale, self.rot_eps,
            self.actions, self.action_penalty_scale, self.action_delta_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, self.num_success_hold_steps
        )

        # update best rotation distance in the current episode
        self.best_rotation_dist = torch.minimum(self.best_rotation_dist, self.curr_rotation_dist)
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
        self.extras['true_objective'] = self.successes

        episode_cumulative = dict()
        episode_cumulative['dist_rew'] = dist_rew
        episode_cumulative['rot_rew'] = rot_rew
        episode_cumulative['action_penalty'] = action_penalty
        episode_cumulative['action_delta_penalty'] = action_delta_penalty
        episode_cumulative['velocity_penalty'] = velocity_penalty
        episode_cumulative['reach_goal_rew'] = reach_goal_rew
        episode_cumulative['fall_rew'] = fall_rew
        episode_cumulative['timeout_rew'] = timeout_rew
        self.extras['episode_cumulative'] = episode_cumulative

        if self.print_success_stat:
            is_success = self.reset_goal_buf.to(torch.bool)

            frame_ = torch.empty_like(self.last_success_step).fill_(self.frame)
            self.success_time = torch.where(is_success, frame_ - self.last_success_step, self.success_time)
            self.last_success_step = torch.where(is_success, frame_, self.last_success_step)
            mask_ = self.success_time > 0
            if any(mask_):
                avg_time_mean = ((self.success_time * mask_).sum(dim=0) / mask_.sum(dim=0)).item()
            else:
                avg_time_mean = math.nan
            
            envs_reset = self.reset_buf 
            if self.use_adr:
                envs_reset = self.reset_buf & ~self.apply_reset_buf
            
            self.total_resets = self.total_resets + envs_reset.sum() 
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * envs_reset).sum() 

            self.total_num_resets += envs_reset

            self.last_ep_successes = torch.where(envs_reset > 0, self.successes, self.last_ep_successes)
            reset_ids = envs_reset.nonzero().squeeze()
            last_successes = self.successes[reset_ids].long()
            self.successes_count[last_successes] += 1

            if self.frame % 100 == 0:
                # The direct average shows the overall result more quickly, but slightly undershoots long term
                # policy performance.
                print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
                if self.total_resets > 0:
                    print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
                print(f"Max num successes: {self.successes.max().item()}")
                print(f"Average consecutive successes: {self.consecutive_successes.mean().item():.2f}")
                print(f"Total num resets: {self.total_num_resets.sum().item()} --> {self.total_num_resets}")

```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]

        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # Need to update the pose of the cube so that it is represented wrt wrist 
        self.palm_link_pose = self.rigid_body_states[:, self.palm_link_handle, 0:7].view(-1, 7)

        self.object_pose_wrt_wrist, self.goal_pose_wrt_wrist = self.compute_poses_wrt_wrist(self.object_pose,
                                                                                            self.palm_link_pose,
                                                                                            self.goal_pose)

        self.goal_wrt_wrist_rot = sel
```

### isaacgymenvs/tasks/factory/factory_base.py

```
"""Factory: base class.

Inherits Gym's VecTask class and abstract base class. Inherited by environment classes. Not directly executed.

Configuration defined in FactoryBase.yaml. Asset info defined in factory_asset_info_franka_table.yaml."""
class FactoryBase(VecTask, FactoryABCBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_base_yaml_params(self)
    def create_sim(self)
    def _create_ground_plane(self)
    def import_franka_assets(self)
    def acquire_base_tensors(self)
    def refresh_base_tensors(self)
    def parse_controller_spec(self)
    def generate_ctrl_signals(self)
    def _set_dof_pos_target(self)
    def _set_dof_torque(self)
    def print_sdf_warning(self)
    def enable_gravity(self, gravity_mag)
    def disable_gravity(self)
    def export_scene(self, label)
    def extract_poses(self)
```

### isaacgymenvs/tasks/factory/factory_control.py

```
"""Factory: control module.

Imported by base, environment, and task classes. Not directly executed."""
def compute_dof_pos_target(cfg_ctrl, arm_dof_pos, fingertip_midpoint_pos, fingertip_midpoint_quat, jacobian, ctrl_target_fingertip_midpoint_pos, ctrl_target_fingertip_midpoint_quat, ctrl_target_gripper_dof_pos, device)
def compute_dof_torque(cfg_ctrl, dof_pos, dof_vel, fingertip_midpoint_pos, fingertip_midpoint_quat, fingertip_midpoint_linvel, fingertip_midpoint_angvel, left_finger_force, right_finger_force, jacobian, arm_mass_matrix, ctrl_target_gripper_dof_pos, ctrl_target_fingertip_midpoint_pos, ctrl_target_fingertip_midpoint_quat, ctrl_target_fingertip_contact_wrench, device)
def get_pose_error(fingertip_midpoint_pos, fingertip_midpoint_quat, ctrl_target_fingertip_midpoint_pos, ctrl_target_fingertip_midpoint_quat, jacobian_type, rot_error_type)
def _get_wrench_error(left_finger_force, right_finger_force, ctrl_target_fingertip_contact_wrench, num_envs, device)
def _get_delta_dof_pos(delta_pose, ik_method, jacobian, device)
def _apply_task_space_gains(delta_fingertip_pose, fingertip_midpoint_linvel, fingertip_midpoint_angvel, task_prop_gains, task_deriv_gains)
def get_analytic_jacobian(fingertip_quat, fingertip_jacobian, num_envs, device)
def get_skew_symm_matrix(vec, device)
def translate_along_local_z(pos, quat, offset, device)
def axis_angle_from_euler(euler)
def axis_angle_from_quat(quat, eps)
def axis_angle_from_quat_naive(quat)
def get_rand_quat(num_quats, device)
def get_nonrand_quat(num_quats, rot_perturbation, device)
```

### isaacgymenvs/tasks/factory/factory_env_gears.py

```
"""Factory: class for gears env.

Inherits base class and abstract environment class. Inherited by gear task class. Not directly executed.

Configuration defined in FactoryEnvGears.yaml. Asset info defined in factory_asset_info_gears.yaml."""
class FactoryEnvGears(FactoryBase, FactoryABCEnv)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self, lower, upper, num_per_row, franka_asset, gear_small_asset, gear_medium_asset, gear_large_asset, base_asset, table_asset)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/factory/factory_env_insertion.py

```
"""Factory: class for insertion env.

Inherits base class and abstract environment class. Inherited by insertion task class. Not directly executed.

Configuration defined in FactoryEnvInsertion.yaml. Asset info defined in factory_asset_info_insertion.yaml."""
class FactoryEnvInsertion(FactoryBase, FactoryABCEnv)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self, lower, upper, num_per_row, franka_asset, plug_assets, socket_assets, table_asset)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/factory/factory_env_nut_bolt.py

```
"""Factory: class for nut-bolt env.

Inherits base class and abstract environment class. Inherited by nut-bolt task classes. Not directly executed.

Configuration defined in FactoryEnvNutBolt.yaml. Asset info defined in factory_asset_info_nut_bolt.yaml."""
class FactoryEnvNutBolt(FactoryBase, FactoryABCEnv)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self, lower, upper, num_per_row, franka_asset, nut_assets, bolt_assets, table_asset)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/factory/factory_schema_class_base.py

```
"""Factory: abstract base class for base class.

Inherits ABC class. Inherited by base class. Defines template for base class."""
class FactoryABCBase(ABC)
    def __init__(self)
    def _get_base_yaml_params(self)
    def create_sim(self)
    def _create_ground_plane(self)
    def import_franka_assets(self)
    def acquire_base_tensors(self)
    def refresh_base_tensors(self)
    def parse_controller_spec(self)
    def generate_ctrl_signals(self)
    def enable_gravity(self)
    def disable_gravity(self)
    def export_scene(self)
    def extract_poses(self)
```

### isaacgymenvs/tasks/factory/factory_schema_class_env.py

```
"""Factory: abstract base class for environment classes.

Inherits ABC class. Inherited by environment classes. Defines template for environment classes."""
class FactoryABCEnv(ABC)
    def __init__(self)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/factory/factory_schema_class_task.py

```
"""Factory: abstract base class for task classes.

Inherits ABC class. Inherited by task classes. Defines template for task classes."""
class FactoryABCTask(ABC)
    def __init__(self)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_rew_buf(self)
    def _update_reset_buf(self)
    def reset_idx(self)
    def _reset_franka(self)
    def _reset_object(self)
    def _reset_buffers(self)
    def _set_viewer_params(self)

```python
def compute_observations(self):
        """Compute observations."""
        pass
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""
        pass
```
```

### isaacgymenvs/tasks/factory/factory_schema_config_base.py

```
"""Factory: schema for base class configuration.

Used by Hydra. Defines template for base class YAML file."""
class Mode()
class PhysX()
class Sim()
class Env()
class FactorySchemaConfigBase()
```

### isaacgymenvs/tasks/factory/factory_schema_config_env.py

```
"""Factory: schema for environment class configurations.

Used by Hydra. Defines template for environment class YAML files."""
class Sim()
class Env()
class FactorySchemaConfigEnv()
```

### isaacgymenvs/tasks/factory/factory_schema_config_task.py

```
"""Factory: schema for task class configurations.

Used by Hydra. Defines template for task class YAML files. Not enforced."""
class Sim()
class Env()
class Randomize()
class RL()
class All()
class GymDefault()
class JointSpaceIK()
class JointSpaceID()
class TaskSpaceImpedance()
class OperationalSpaceMotion()
class OpenLoopForce()
class ClosedLoopForce()
class HybridForceMotion()
class Ctrl()
class FactorySchemaConfigTask()
```

### isaacgymenvs/tasks/factory/factory_task_gears.py

```
"""Factory: Class for gears task.

Inherits gears environment class and abstract task class (not inforced). Can be executed with 
python train.py task=FactoryTaskGears

Only the environment is provided; training a successful RL policy is an open research problem left to the user."""
class FactoryTaskGears(FactoryEnvGears, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_rew_buf(self)
    def _update_reset_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self, env_ids)
    def _reset_object(self, env_ids)
    def _reset_buffers(self, env_ids)
    def _set_viewer_params(self)

```python
def compute_observations(self):
        """Compute observations."""

        return self.obs_buf
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""

        self._update_rew_buf()
        self._update_reset_buf()
```
```

### isaacgymenvs/tasks/factory/factory_task_insertion.py

```
"""Factory: Class for insertion task.

Inherits insertion environment class and abstract task class (not enforced). Can be executed with
python train.py task=FactoryTaskInsertion

Only the environment is provided; training a successful RL policy is an open research problem left to the user."""
class FactoryTaskInsertion(FactoryEnvInsertion, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_rew_buf(self)
    def _update_reset_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self, env_ids)
    def _reset_object(self, env_ids)
    def _reset_buffers(self, env_ids)
    def _set_viewer_params(self)

```python
def compute_observations(self):
        """Compute observations."""

        return self.obs_buf
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""

        self._update_rew_buf()
        self._update_reset_buf()
```
```

### isaacgymenvs/tasks/factory/factory_task_nut_bolt_pick.py

```
"""Factory: Class for nut-bolt pick task.

Inherits nut-bolt environment class and abstract task class (not enforced). Can be executed with
python train.py task=FactoryTaskNutBoltPick"""
class FactoryTaskNutBoltPick(FactoryEnvNutBolt, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_reset_buf(self)
    def _update_rew_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self, env_ids)
    def _reset_object(self, env_ids)
    def _reset_buffers(self, env_ids)
    def _set_viewer_params(self)
    def _apply_actions_as_ctrl_targets(self, actions, ctrl_target_gripper_dof_pos, do_scale)
    def _get_keypoint_offsets(self, num_keypoints)
    def _get_keypoint_dist(self)
    def _close_gripper(self, sim_steps)
    def _move_gripper_to_dof_pos(self, gripper_dof_pos, sim_steps)
    def _lift_gripper(self, franka_gripper_width, lift_distance, sim_steps)
    def _check_lift_success(self, height_multiple)
    def _randomize_gripper_pose(self, env_ids, sim_steps)

```python
def compute_observations(self):
        """Compute observations."""

        # Shallow copies of tensors
        obs_tensors = [self.fingertip_midpoint_pos,
                       self.fingertip_midpoint_quat,
                       self.fingertip_midpoint_linvel,
                       self.fingertip_midpoint_angvel,
                       self.nut_grasp_pos,
                       self.nut_grasp_quat]

        self.obs_buf = torch.cat(obs_tensors, dim=-1)  # shape = (num_envs, num_observations)

        return self.obs_buf
```

```python
def compute_reward(self):
        """Update reward and reset buffers."""

        self._update_reset_buf()
        self._update_rew_buf()
```
```

### isaacgymenvs/tasks/factory/factory_task_nut_bolt_place.py

```
"""Factory: Class for nut-bolt place task.

Inherits nut-bolt environment class and abstract task class (not enforced). Can be executed with
python train.py task=FactoryTaskNutBoltPlace"""
class FactoryTaskNutBoltPlace(FactoryEnvNutBolt, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_reset_buf(self)
    def _update_rew_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self, env_ids)
    def _reset_object(self, env_ids)
    def _reset_buffers(self, env_ids)
    def _set_viewer_params(self)
    def _apply_actions_as_ctrl_targets(self, actions, ctrl_target_gripper_dof_pos, do_scale)
    def _open_gripper(self, sim_steps)
    def _move_gripper_to_dof_pos(self, gripper_dof_pos, sim_steps)
    def _lift_gripper(self, gripper_dof_pos, lift_distance, sim_steps)
    def _get_keypoint_offsets(self, num_keypoints)
    def _get_keypoint_dist(self)
    def _check_nut_close_to_bolt(self)
    def _randomize_gripper_pose(self, env_ids, sim_steps)

```python
def compute_observations(self):
        """Compute observations."""

        # Shallow copies of tensors
        obs_tensors = [self.fingertip_midpoint_pos,
                       self.fingertip_midpoint_quat,
                       self.fingertip_midpoint_linvel,
                       self.fingertip_midpoint_angvel,
                       self.nut_pos,
                       self.nut_quat,
                       self.bolt_pos,
                       self.bolt_quat]

        if self.cfg_task.rl.add_obs_bolt_tip_pos:
            obs_tensors += [self.bolt_tip_pos_local]

        self.obs_buf = torch.cat(obs_tensors, dim=-1)  # shape = (num_envs, num_observations)

        return self.obs_buf
```

```python
def compute_reward(self):
        """Update reward and reset buffers."""

        self._update_reset_buf()
        self._update_rew_buf()
```
```

### isaacgymenvs/tasks/factory/factory_task_nut_bolt_screw.py

```
"""Factory: Class for nut-bolt screw task.

Inherits nut-bolt environment class and abstract task class (not enforced). Can be executed with
python train.py task=FactoryTaskNutBoltScrew

Initial Franka/nut states are ideal for M16 nut-and-bolt.
In this example, initial state randomization is not applied; thus, policy should succeed almost instantly."""
class FactoryTaskNutBoltScrew(FactoryEnvNutBolt, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_reset_buf(self, curr_successes, curr_failures)
    def _update_rew_buf(self, curr_successes)
    def reset_idx(self, env_ids)
    def _reset_franka(self, env_ids)
    def _reset_object(self, env_ids)
    def _reset_buffers(self, env_ids)
    def _set_viewer_params(self)
    def _apply_actions_as_ctrl_targets(self, actions, ctrl_target_gripper_dof_pos, do_scale)
    def _get_keypoint_dist(self, body)
    def _get_curr_successes(self)
    def _get_curr_failures(self, curr_successes)

```python
def compute_observations(self):
        """Compute observations."""

        # Shallow copies of tensors
        obs_tensors = [self.fingertip_midpoint_pos,
                       self.fingertip_midpoint_quat,
                       self.fingertip_midpoint_linvel,
                       self.fingertip_midpoint_angvel,
                       self.nut_com_pos,
                       self.nut_com_quat,
                       self.nut_com_linvel,
                       self.nut_com_angvel]

        if self.cfg_task.rl.add_obs_finger_force:
            obs_tensors += [self.left_finger_force, self.right_finger_force]

        obs_tensors = torch.cat(obs_tensors, dim=-1)
        self.obs_buf[:, :obs_tensors.shape[-1]] = obs_tensors  # shape = (num_envs, num_observations)

        return self.obs_buf
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""

        # Get successful and failed envs at current timestep
        curr_successes = self._get_curr_successes()
        curr_failures = self._get_curr_failures(curr_successes)

        self._update_reset_buf(curr_successes, curr_failures)
        self._update_rew_buf(curr_successes)
```
```

### isaacgymenvs/tasks/franka_cabinet.py

```
class FrankaCabinet(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def init_data(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_franka_reward(reset_buf, progress_buf, actions, cabinet_dof_pos, franka_grasp_pos, drawer_grasp_pos, franka_grasp_rot, drawer_grasp_rot, franka_lfinger_pos, franka_rfinger_pos, gripper_forward_axis, drawer_inward_axis, gripper_up_axis, drawer_up_axis, num_envs, dist_reward_scale, rot_reward_scale, around_handle_reward_scale, open_reward_scale, finger_dist_reward_scale, action_penalty_scale, distX_offset, max_episode_length)
def compute_grasp_transforms(hand_rot, hand_pos, franka_local_grasp_rot, franka_local_grasp_pos, drawer_rot, drawer_pos, drawer_local_grasp_rot, drawer_local_grasp_pos)

```python
def compute_franka_reward(
    reset_buf, progress_buf, actions, cabinet_dof_pos,
    franka_grasp_pos, drawer_grasp_pos, franka_grasp_rot, drawer_grasp_rot,
    franka_lfinger_pos, franka_rfinger_pos,
    gripper_forward_axis, drawer_inward_axis, gripper_up_axis, drawer_up_axis,
    num_envs, dist_reward_scale, rot_reward_scale, around_handle_reward_scale, open_reward_scale,
    finger_dist_reward_scale, action_penalty_scale, distX_offset, max_episode_length
):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, int, float, float, float, float, float, float, float, float) -> Tuple[Tensor, Tensor]

    # distance from hand to the drawer
    d = torch.norm(franka_grasp_pos - drawer_grasp_pos, p=2, dim=-1)
    dist_reward = 1.0 / (1.0 + d ** 2)
    dist_reward *= dist_reward
    dist_reward = torch.where(d <= 0.02, dist_reward * 2, dist_reward)

    axis1 = tf_vector(franka_grasp_rot, gripper_forward_axis)
    axis2 = tf_vector(drawer_grasp_rot, drawer_inward_axis)
    axis3 = tf_vector(franka_grasp_rot, gripper_up_axis)
    axis4 = tf_vector(drawer_grasp_rot, drawer_up_axis)

    dot1 = torch.bmm(axis1.view(num_envs, 1, 3), axis2.view(num_envs, 3, 1)).squeeze(-1).squeeze(-1)  # alignment of forward axis for gripper
    dot2 = torch.bmm(axis3.view(num_envs, 1, 3), axis4.view(num_envs, 3, 1)).squeeze(-1).squeeze(-1)  # alignment of up axis for gripper
    # reward for matching the orientation of the hand to the drawer (fingers wrapped)
    rot_reward = 0.5 * (torch.sign(dot1) * dot1 ** 2 + torch.sign(dot2) * dot2 ** 2)

    # bonus if left finger is above the drawer handle and right below
    around_handle_reward = torch.zeros_like(rot_reward)
    around_handle_reward = torch.where(franka_lfinger_pos[:, 2] > drawer_grasp_pos[:, 2],
                                       torch.where(franka_rfinger_pos[:, 2] < drawer_grasp_pos[:, 2],
                                                   around_handle_reward + 0.5, around_handle_reward), around_handle_reward)
    # reward for distance of each finger from the drawer
    finger_dist_reward = torch.zeros_like(rot_reward)
    lfinger_dist = torch.abs(franka_lfinger_pos[:, 2] - drawer_grasp_pos[:, 2])
    rfinger_dist = torch.abs(franka_rfinger_pos[:, 2] - drawer_grasp_pos[:, 2])
    finger_dist_reward = torch.where(franka_lfinger_pos[:, 2] > drawer_grasp_pos[:, 2],
                                     torch.where(franka_rfinger_pos[:, 2] < drawer_grasp_pos[:, 2],
                                                 (0.04 - lfinger_dist) + (0.04 - rfinger_dist), finger_dist_reward), finger_dist_reward)

    # regularization on the actions (summed for each environment)
    action_penalty = torch.sum(actions ** 2, dim=-1)

    # how far the cabinet has been opened out
    open_reward = cabinet_dof_pos[:, 3] * around_handle_reward + cabinet_dof_pos[:, 3]  # drawer_top_joint

    rewards = dist_reward_scale * dist_reward + rot_reward_scale * rot_reward \
        + around_handle_reward_scale * around_handle_reward + open_reward_scale * open_reward \
        + finger_dist_reward_scale * finger_dist_reward - action_penalty_scale * action_penalty

    # bonus for opening drawer properly
    rewards = torch.where(cabinet_dof_pos[:, 3] > 0.01, rewards + 0.5, rewards)
    rewards = torch.where(cabinet_dof_pos[:, 3] > 0.2, rewards + around_handle_reward, rewards)
    rewards = torch.where(cabinet_dof_pos[:, 3] > 0.39, rewards + (2.0 * around_handle_reward), rewards)

    # prevent bad style in opening drawer
    rewards = torch.where(franka_lfinger_pos[:, 0] < drawer_grasp_pos[:, 0] - distX_offset,
                          torch.ones_like(rewards) * -1, rewards)
    rewards = torch.where(franka_rfinger_pos[:, 0] < drawer_grasp_pos[:, 0] - distX_offset,
                          torch.ones_like(rewards) * -1, rewards)
    
    # reset if drawer is open or max length reached
    reset_buf = torch.where(cabinet_dof_pos[:, 3] > 0.39, tor
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:] = compute_franka_reward(
            self.reset_buf, self.progress_buf, self.actions, self.cabinet_dof_pos,
            self.franka_grasp_pos, self.drawer_grasp_pos, self.franka_grasp_rot, self.drawer_grasp_rot,
            self.franka_lfinger_pos, self.franka_rfinger_pos,
            self.gripper_forward_axis, self.drawer_inward_axis, self.gripper_up_axis, self.drawer_up_axis,
            self.num_envs, self.dist_reward_scale, self.rot_reward_scale, self.around_handle_reward_scale, self.open_reward_scale,
            self.finger_dist_reward_scale, self.action_penalty_scale, self.distX_offset, self.max_episode_length
        )
```

```python
def compute_observations(self):

        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        hand_pos = self.rigid_body_states[:, self.hand_handle][:, 0:3]
        hand_rot = self.rigid_body_states[:, self.hand_handle][:, 3:7]
        drawer_pos = self.rigid_body_states[:, self.drawer_handle][:, 0:3]
        drawer_rot = self.rigid_body_states[:, self.drawer_handle][:, 3:7]

        self.franka_grasp_rot[:], self.franka_grasp_pos[:], self.drawer_grasp_rot[:], self.drawer_grasp_pos[:] = \
            compute_grasp_transforms(hand_rot, hand_pos, self.franka_local_grasp_rot, self.franka_local_grasp_pos,
                                     drawer_rot, drawer_pos, self.drawer_local_grasp_rot, self.drawer_local_grasp_pos
                                     )

        self.franka_lfinger_pos = self.rigid_body_states[:, self.lfinger_handle][:, 0:3]
        self.franka_rfinger_pos = self.rigid_body_states[:, self.rfinger_handle][:, 0:3]
        self.franka_lfinger_rot = self.rigid_body_states[:, self.lfinger_handle][:, 3:7]
        self.franka_rfinger_rot = self.rigid_body_states[:, self.rfinger_handle][:, 3:7]

        dof_pos_scaled = (2.0 * (self.franka_dof_pos - self.franka_dof_lower_limits)
                          / (self.franka_dof_upper_limits - self.franka_dof_lower_limits) - 1.0)
        to_target = self.drawer_grasp_pos - self.franka_grasp_pos
        self.obs_buf = torch.cat((dof_pos_scaled, self.franka_dof_vel * self.dof_vel_scale, to_target,
                                  self.cabinet_dof_pos[:, 3].unsqueeze(-1), self.cabinet_dof_vel[:, 3].unsqueeze(-1)), dim=-1)

        return self.obs_buf
```
```

### isaacgymenvs/tasks/franka_cube_stack.py

```
def axisangle2quat(vec, eps)
class FrankaCubeStack(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def init_data(self)
    def _update_states(self)
    def _refresh(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
    def _reset_init_cube_state(self, cube, env_ids, check_valid)
    def _compute_osc_torques(self, dpose)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_franka_reward(reset_buf, progress_buf, actions, states, reward_settings, max_episode_length)

```python
def compute_franka_reward(
    reset_buf, progress_buf, actions, states, reward_settings, max_episode_length
):
    # type: (Tensor, Tensor, Tensor, Dict[str, Tensor], Dict[str, float], float) -> Tuple[Tensor, Tensor]

    # Compute per-env physical parameters
    target_height = states["cubeB_size"] + states["cubeA_size"] / 2.0
    cubeA_size = states["cubeA_size"]
    cubeB_size = states["cubeB_size"]

    # distance from hand to the cubeA
    d = torch.norm(states["cubeA_pos_relative"], dim=-1)
    d_lf = torch.norm(states["cubeA_pos"] - states["eef_lf_pos"], dim=-1)
    d_rf = torch.norm(states["cubeA_pos"] - states["eef_rf_pos"], dim=-1)
    dist_reward = 1 - torch.tanh(10.0 * (d + d_lf + d_rf) / 3)

    # reward for lifting cubeA
    cubeA_height = states["cubeA_pos"][:, 2] - reward_settings["table_height"]
    cubeA_lifted = (cubeA_height - cubeA_size) > 0.04
    lift_reward = cubeA_lifted

    # how closely aligned cubeA is to cubeB (only provided if cubeA is lifted)
    offset = torch.zeros_like(states["cubeA_to_cubeB_pos"])
    offset[:, 2] = (cubeA_size + cubeB_size) / 2
    d_ab = torch.norm(states["cubeA_to_cubeB_pos"] + offset, dim=-1)
    align_reward = (1 - torch.tanh(10.0 * d_ab)) * cubeA_lifted

    # Dist reward is maximum of dist and align reward
    dist_reward = torch.max(dist_reward, align_reward)

    # final reward for stacking successfully (only if cubeA is close to target height and corresponding location, and gripper is not grasping)
    cubeA_align_cubeB = (torch.norm(states["cubeA_to_cubeB_pos"][:, :2], dim=-1) < 0.02)
    cubeA_on_cubeB = torch.abs(cubeA_height - target_height) < 0.02
    gripper_away_from_cubeA = (d > 0.04)
    stack_reward = cubeA_align_cubeB & cubeA_on_cubeB & gripper_away_from_cubeA

    # Compose rewards

    # We either provide the stack reward or the align + dist reward
    rewards = torch.where(
        stack_reward,
        reward_settings["r_stack_scale"] * stack_reward,
        reward_settings["r_dist_scale"] * dist_reward + reward_settings["r_lift_scale"] * lift_reward + reward_settings[
            "r_align_scale"] * align_reward,
    )

    # Compute resets
    reset_buf = torch.where((progress_buf >= max_episode_length - 1) | (stack_reward > 0), torch.ones_like(reset_buf), reset_buf)

    return rewards, reset_buf
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:] = compute_franka_reward(
            self.reset_buf, self.progress_buf, self.actions, self.states, self.reward_settings, self.max_episode_length
        )
```

```python
def compute_observations(self):
        self._refresh()
        obs = ["cubeA_quat", "cubeA_pos", "cubeA_to_cubeB_pos", "eef_pos", "eef_quat"]
        obs += ["q_gripper"] if self.control_type == "osc" else ["q"]
        self.obs_buf = torch.cat([self.states[ob] for ob in obs], dim=-1)

        maxs = {ob: torch.max(self.states[ob]).item() for ob in obs}

        return self.obs_buf
```
```

### isaacgymenvs/tasks/humanoid.py

```
class Humanoid(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_humanoid_reward(obs_buf, reset_buf, progress_buf, actions, up_weight, heading_weight, potentials, prev_potentials, actions_cost_scale, energy_cost_scale, joints_at_limit_cost_scale, max_motor_effort, motor_efforts, termination_height, death_cost, max_episode_length)
def compute_humanoid_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_force, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, angular_velocity_scale, basis_vec0, basis_vec1)

```python
def compute_humanoid_reward(
    obs_buf,
    reset_buf,
    progress_buf,
    actions,
    up_weight,
    heading_weight,
    potentials,
    prev_potentials,
    actions_cost_scale,
    energy_cost_scale,
    joints_at_limit_cost_scale,
    max_motor_effort,
    motor_efforts,
    termination_height,
    death_cost,
    max_episode_length
):
    # type: (Tensor, Tensor, Tensor, Tensor, float, float, Tensor, Tensor, float, float, float, float, Tensor, float, float, float) -> Tuple[Tensor, Tensor]

    # reward from the direction headed
    heading_weight_tensor = torch.ones_like(obs_buf[:, 11]) * heading_weight
    heading_reward = torch.where(obs_buf[:, 11] > 0.8, heading_weight_tensor, heading_weight * obs_buf[:, 11] / 0.8)

    # reward for being upright
    up_reward = torch.zeros_like(heading_reward)
    up_reward = torch.where(obs_buf[:, 10] > 0.93, up_reward + up_weight, up_reward)

    actions_cost = torch.sum(actions ** 2, dim=-1)

    # energy cost reward
    motor_effort_ratio = motor_efforts / max_motor_effort
    scaled_cost = joints_at_limit_cost_scale * (torch.abs(obs_buf[:, 12:33]) - 0.98) / 0.02
    dof_at_limit_cost = torch.sum((torch.abs(obs_buf[:, 12:33]) > 0.98) * scaled_cost * motor_effort_ratio.unsqueeze(0), dim=-1)

    electricity_cost = torch.sum(torch.abs(actions * obs_buf[:, 33:54]) * motor_effort_ratio.unsqueeze(0), dim=-1)

    # reward for duration of being alive
    alive_reward = torch.ones_like(potentials) * 2.0
    progress_reward = potentials - prev_potentials

    total_reward = progress_reward + alive_reward + up_reward + heading_reward - \
        actions_cost_scale * actions_cost - energy_cost_scale * electricity_cost - dof_at_limit_cost

    # adjust reward for fallen agents
    total_reward = torch.where(obs_buf[:, 0] < termination_height, torch.ones_like(total_reward) * death_cost, total_reward)

    # reset agents
    reset = torch.where(obs_buf[:, 0] < termination_height, torch.ones_like(reset_buf), reset_buf)
    reset = torch.where(progress_buf >= max_episode_length - 1, torch.ones_like(reset_buf), reset)

    return total_reward, reset
```

```python
def compute_humanoid_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel,
                                  dof_force, dof_limits_lower, dof_limits_upper, dof_vel_scale,
                                  sensor_force_torques, actions, dt, contact_force_scale, angular_velocity_scale,
                                  basis_vec0, basis_vec1):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, float, Tensor, Tensor, float, float, float, Tensor, Tensor) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor]

    torso_position = root_states[:, 0:3]
    torso_rotation = root_states[:, 3:7]
    velocity = root_states[:, 7:10]
    ang_velocity = root_states[:, 10:13]

    to_target = targets - torso_position
    to_target[:, 2] = 0

    prev_potentials_new = potentials.clone()
    potentials = -torch.norm(to_target, p=2, dim=-1) / dt

    torso_quat, up_proj, heading_proj, up_vec, heading_vec = compute_heading_and_up(
        torso_rotation, inv_start_rot, to_target, basis_vec0, basis_vec1, 2)

    vel_loc, angvel_loc, roll, pitch, yaw, angle_to_target = compute_rot(
        torso_quat, velocity, ang_velocity, targets, torso_position)

    roll = normalize_angle(roll).unsqueeze(-1)
    yaw = normalize_angle(yaw).unsqueeze(-1)
    angle_to_target = normalize_angle(angle_to_target).unsqueeze(-1)
    dof_pos_scaled = unscale(dof_pos, dof_limits_lower, dof_limits_upper)

    # obs_buf shapes: 1, 3, 3, 1, 1, 1, 1, 1, num_dofs (21), num_dofs (21), 6, num_acts (21)
    obs = torch.cat((torso_position[:, 2].view(-1, 1), vel_loc, angvel_loc * angular_velocity_scale,
                     yaw, roll, angle_to_target, up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1),
                     dof_pos_scaled, dof_vel * dof_vel_scale, dof_force * contact_force_scale,
                     sensor_force_torques.view(-1, 12) * contact_force_scale, actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf = compute_humanoid_reward(
            self.obs_buf,
            self.reset_buf,
            self.progress_buf,
            self.actions,
            self.up_weight,
            self.heading_weight,
            self.potentials,
            self.prev_potentials,
            self.actions_cost_scale,
            self.energy_cost_scale,
            self.joints_at_limit_cost_scale,
            self.max_motor_effort,
            self.motor_efforts,
            self.termination_height,
            self.death_cost,
            self.max_episode_length
        )
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)

        self.gym.refresh_force_sensor_tensor(self.sim)

        self.gym.refresh_dof_force_tensor(self.sim)
        self.obs_buf[:], self.potentials[:], self.prev_potentials[:], self.up_vec[:], self.heading_vec[:] = compute_humanoid_observations(
            self.obs_buf, self.root_states, self.targets, self.potentials,
            self.inv_start_rot, self.dof_pos, self.dof_vel, self.dof_force_tensor,
            self.dof_limits_lower, self.dof_limits_upper, self.dof_vel_scale,
            self.vec_sensor_tensor, self.actions, self.dt, self.contact_force_scale, self.angular_velocity_scale,
            self.basis_vec0, self.basis_vec1)
```
```

### isaacgymenvs/tasks/humanoid_amp.py

```
class HumanoidAMP(HumanoidAMPBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def post_physics_step(self)
    def get_num_amp_obs(self)
    def amp_observation_space(self)
    def fetch_amp_obs_demo(self, num_samples)
    def fetch_amp_obs_demo(self, num_samples)
    def _build_amp_obs_demo_buf(self, num_samples)
    def _load_motion(self, motion_file)
    def reset_idx(self, env_ids)
    def _reset_actors(self, env_ids)
    def _reset_default(self, env_ids)
    def _reset_ref_state_init(self, env_ids)
    def _reset_hybrid_state_init(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _init_amp_obs_default(self, env_ids)
    def _init_amp_obs_ref(self, env_ids, motion_ids, motion_times)
    def _set_env_state(self, env_ids, root_pos, root_rot, dof_pos, root_vel, root_ang_vel, dof_vel)
    def _update_hist_amp_obs(self, env_ids)
    def _compute_amp_observations(self, env_ids)
def build_amp_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs)

```python
def build_amp_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs):
    # type: (Tensor, Tensor, Tensor, Tensor, bool) -> Tensor
    root_pos = root_states[:, 0:3]
    root_rot = root_states[:, 3:7]
    root_vel = root_states[:, 7:10]
    root_ang_vel = root_states[:, 10:13]

    root_h = root_pos[:, 2:3]
    heading_rot = calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = quat_to_tan_norm(root_rot_obs)

    local_root_vel = my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand
    
    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], 
                                               heading_rot_expand.shape[2])
    local_end_pos = my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])
    
    dof_obs = dof_to_obs(dof_pos)

    obs = torch.cat((root_h, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def amp_observation_space(self):
        return self._amp_obs_space
```

```python
def _compute_amp_observations(self, env_ids=None):
        key_body_pos = self._rigid_body_pos[:, self._key_body_ids, :]
        if (env_ids is None):
            self._curr_amp_obs_buf[:] = build_amp_observations(self._root_states, self._dof_pos, self._dof_vel, key_body_pos,
                                                                self._local_root_obs)
        else:
            self._curr_amp_obs_buf[env_ids] = build_amp_observations(self._root_states[env_ids], self._dof_pos[env_ids], 
                                                                    self._dof_vel[env_ids], key_body_pos[env_ids],
                                                                    self._local_root_obs)
        return
```
```

### isaacgymenvs/tasks/industreal/industreal_algo_utils.py

```
"""IndustReal: algorithms module.

Contains functions that implement Simulation-Aware Policy Update (SAPU), SDF-Based Reward, and Sampling-Based Curriculum (SBC).

Not intended to be executed as a standalone script."""
def load_asset_mesh_in_warp(urdf_path, sample_points, num_samples, device)
def load_asset_meshes_in_warp(plug_files, socket_files, num_samples, device)
def get_max_interpen_dists(asset_indices, plug_pos, plug_quat, socket_pos, socket_quat, wp_plug_meshes_sampled_points, wp_socket_meshes, wp_device, device)
def get_sapu_reward_scale(asset_indices, plug_pos, plug_quat, socket_pos, socket_quat, wp_plug_meshes_sampled_points, wp_socket_meshes, interpen_thresh, wp_device, device)
def get_plug_goal_sdfs(wp_plug_meshes, asset_indices, socket_pos, socket_quat, wp_device)
def get_sdf_reward(wp_plug_meshes_sampled_points, asset_indices, plug_pos, plug_quat, plug_goal_sdfs, wp_device, device)
def get_curriculum_reward_scale(cfg_task, curr_max_disp)
def get_new_max_disp(curr_success, cfg_task, curr_max_disp)
def get_keypoint_offsets(num_keypoints, device)
def check_plug_close_to_socket(keypoints_plug, keypoints_socket, dist_threshold, progress_buf)
def check_plug_engaged_w_socket(plug_pos, socket_top_pos, keypoints_plug, keypoints_socket, cfg_task, progress_buf)
def check_plug_inserted_in_socket(plug_pos, socket_pos, keypoints_plug, keypoints_socket, cfg_task, progress_buf)
def check_gear_engaged_w_shaft(keypoints_gear, keypoints_shaft, gear_pos, shaft_pos, asset_info_gears, cfg_task, progress_buf)
def check_gear_inserted_on_shaft(gear_pos, shaft_pos, keypoints_gear, keypoints_shaft, cfg_task, progress_buf)
def get_engagement_reward_scale(plug_pos, socket_pos, is_plug_engaged_w_socket, success_height_thresh, device)
def transform_points(src, dest, xform)
def get_interpen_dist(queries, mesh, interpen_dists)

```python
def get_sapu_reward_scale(
    asset_indices,
    plug_pos,
    plug_quat,
    socket_pos,
    socket_quat,
    wp_plug_meshes_sampled_points,
    wp_socket_meshes,
    interpen_thresh,
    wp_device,
    device,
):
    """Compute reward scale for SAPU."""

    # Get max interpenetration distances
    max_interpen_dists = get_max_interpen_dists(
        asset_indices=asset_indices,
        plug_pos=plug_pos,
        plug_quat=plug_quat,
        socket_pos=socket_pos,
        socket_quat=socket_quat,
        wp_plug_meshes_sampled_points=wp_plug_meshes_sampled_points,
        wp_socket_meshes=wp_socket_meshes,
        wp_device=wp_device,
        device=device,
    )

    # Determine if envs have low interpenetration or high interpenetration
    low_interpen_envs = torch.nonzero(max_interpen_dists <= interpen_thresh)
    high_interpen_envs = torch.nonzero(max_interpen_dists > interpen_thresh)

    # Compute reward scale
    reward_scale = 1 - torch.tanh(
        max_interpen_dists[low_interpen_envs] / interpen_thresh
    )

    return low_interpen_envs, high_interpen_envs, reward_scale
```

```python
def get_sdf_reward(
    wp_plug_meshes_sampled_points,
    asset_indices,
    plug_pos,
    plug_quat,
    plug_goal_sdfs,
    wp_device,
    device,
):
    """Calculate SDF-based reward."""

    num_envs = len(plug_pos)
    sdf_reward = torch.zeros((num_envs,), dtype=torch.float32, device=device)

    for i in range(num_envs):
        # Create copy of sampled points
        sampled_points = wp.clone(wp_plug_meshes_sampled_points[asset_indices[i]])

        # Transform sampled points from original plug pose to current plug pose
        curr_transform = wp.transform(plug_pos[i], plug_quat[i])
        wp.launch(
            kernel=transform_points,
            dim=len(sampled_points),
            inputs=[sampled_points, sampled_points, curr_transform],
            device=wp_device,
        )

        # Get SDF values at transformed points
        sdf_dists = torch.from_numpy(plug_goal_sdfs[i](sampled_points.numpy())).double()

        # Clamp values outside isosurface and take absolute value
        sdf_dists = torch.abs(torch.where(sdf_dists > 0.0, 0.0, sdf_dists))

        sdf_reward[i] = torch.mean(sdf_dists)

    sdf_reward = -torch.log(sdf_reward)

    return sdf_reward
```

```python
def get_curriculum_reward_scale(cfg_task, curr_max_disp):
    """Compute reward scale for SBC."""

    # Compute difference between max downward displacement at beginning of training (easiest condition)
    # and current max downward displacement (based on current curriculum stage)
    # NOTE: This number increases as curriculum gets harder
    curr_stage_diff = cfg_task.rl.curriculum_height_bound[1] - curr_max_disp

    # Compute difference between max downward displacement at beginning of training (easiest condition)
    # and min downward displacement (hardest condition)
    final_stage_diff = (
        cfg_task.rl.curriculum_height_bound[1] - cfg_task.rl.curriculum_height_bound[0]
    )

    # Compute reward scale
    reward_scale = curr_stage_diff / final_stage_diff + 1.0

    return reward_scale
```

```python
def get_engagement_reward_scale(
    plug_pos, socket_pos, is_plug_engaged_w_socket, success_height_thresh, device
):
    """Compute scale on reward. If plug is not engaged with socket, scale is zero.
    If plug is engaged, scale is proportional to distance between plug and bottom of socket."""

    # Set default value of scale to zero
    num_envs = len(plug_pos)
    reward_scale = torch.zeros((num_envs,), dtype=torch.float32, device=device)

    # For envs in which plug and socket are engaged, compute positive scale
    engaged_idx = np.argwhere(is_plug_engaged_w_socket.cpu().numpy().copy()).squeeze()
    height_dist = plug_pos[engaged_idx, 2] - socket_pos[engaged_idx, 2]
    # NOTE: Edge case: if success_height_thresh is greater than 0.1,
    # denominator could be negative
    reward_scale[engaged_idx] = 1.0 / ((height_dist - success_height_thresh) + 0.1)

    return reward_scale
```
```

### isaacgymenvs/tasks/industreal/industreal_base.py

```
"""IndustReal: base class.

Inherits Factory base class and Factory abstract base class. Inherited by IndustReal environment classes. Not directly executed.

Configuration defined in IndustRealBase.yaml. Asset info defined in industreal_asset_info_franka_table.yaml."""
class IndustRealBase(FactoryBase, FactoryABCBase)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_base_yaml_params(self)
    def import_franka_assets(self)
    def acquire_base_tensors(self)
    def generate_ctrl_signals(self)
    def _set_dof_pos_target(self)
    def _set_dof_torque(self)
    def simulate_and_refresh(self)
    def enable_gravity(self)
    def open_gripper(self, sim_steps)
    def close_gripper(self, sim_steps)
    def move_gripper_to_target_pose(self, gripper_dof_pos, sim_steps)
    def pose_world_to_robot_base(self, pos, quat)
```

### isaacgymenvs/tasks/industreal/industreal_env_gears.py

```
"""IndustReal: class for gears environment.

Inherits IndustReal base class and Factory abstract environment class. Inherited by IndustReal gear insertion task class. Not directly executed.

Configuration defined in IndustRealEnvGears.yaml. Asset info defined in industreal_asset_info_gears.yaml."""
class IndustRealEnvGears(IndustRealBase, FactoryABCEnv)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self, lower, upper, num_per_row, franka_asset, gear_small_asset, gear_medium_asset, gear_large_asset, base_asset, table_asset)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/industreal/industreal_env_pegs.py

```
"""IndustReal: class for pegs environment.

Inherits IndustReal base class and Factory abstract environment class. Inherited by IndustReal peg insertion task class. Not directly executed.

Configuration defined in IndustRealEnvPegs.yaml. Asset info defined in industreal_asset_info_pegs.yaml."""
class IndustRealEnvPegs(IndustRealBase, FactoryABCEnv)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_env_yaml_params(self)
    def create_envs(self)
    def _import_env_assets(self)
    def _create_actors(self, lower, upper, num_per_row, franka_asset, plug_assets, socket_assets, table_asset)
    def _acquire_env_tensors(self)
    def refresh_env_tensors(self)
```

### isaacgymenvs/tasks/industreal/industreal_task_gears_insert.py

```
"""IndustReal: class for gear insertion task.

Inherits IndustReal gears environment class and Factory abstract task class (not enforced).

Trains a gear insertion policy with Simulation-Aware Policy Update (SAPU), SDF-Based Reward, and Sampling-Based Curriculum (SBC).

Can be executed with python train.py task=IndustRealTaskGearsInsert."""
class IndustRealTaskGearsInsert(IndustRealEnvGears, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_rew_buf(self)
    def _update_reset_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self)
    def _reset_object(self)
    def _reset_base(self)
    def _reset_small_large_gears(self)
    def _reset_medium_gear(self, before_move_to_grasp)
    def _reset_buffers(self)
    def _set_viewer_params(self)
    def _apply_actions_as_ctrl_targets(self, actions, ctrl_target_gripper_dof_pos, do_scale)
    def _move_gripper_to_grasp_pose(self, sim_steps)

```python
def compute_observations(self):
        """Compute observations."""

        delta_pos = self.gripper_goal_pos - self.fingertip_centered_pos
        noisy_delta_pos = self.noisy_gripper_goal_pos - self.fingertip_centered_pos

        # Define observations (for actor)
        obs_tensors = [
            self.arm_dof_pos,  # 7
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                1
            ],  # 4
            self.pose_world_to_robot_base(
                self.noisy_gripper_goal_pos, self.noisy_gripper_goal_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.noisy_gripper_goal_pos, self.noisy_gripper_goal_quat
            )[
                1
            ],  # 4
            noisy_delta_pos,
        ]

        # Define state (for critic)
        state_tensors = [
            self.arm_dof_pos,  # 7
            self.arm_dof_vel,  # 7
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                1
            ],  # 4
            self.fingertip_centered_linvel,  # 3
            self.fingertip_centered_angvel,  # 3
            self.pose_world_to_robot_base(
                self.gripper_goal_pos, self.gripper_goal_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.gripper_goal_pos, self.gripper_goal_quat
            )[
                1
            ],  # 4
            delta_pos,  # 3
            self.pose_world_to_robot_base(self.gear_medium_pos, self.gear_medium_quat)[
                0
            ],  # 3
            self.pose_world_to_robot_base(self.gear_medium_pos, self.gear_medium_quat)[
                1
            ],  # 4
            noisy_delta_pos - delta_pos,
        ]  # 3

        self.obs_buf = torch.cat(
            obs_tensors, dim=-1
        )  # shape = (num_envs, num_observations)
        self.states_buf = torch.cat(state_tensors, dim=-1)

        return self.obs_buf
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""

        self._update_rew_buf()
        self._update_reset_buf()
```
```

### isaacgymenvs/tasks/industreal/industreal_task_pegs_insert.py

```
"""IndustReal: class for peg insertion task.

Inherits IndustReal pegs environment class and Factory abstract task class (not enforced).

Trains a peg insertion policy with Simulation-Aware Policy Update (SAPU), SDF-Based Reward, and Sampling-Based Curriculum (SBC).

Can be executed with python train.py task=IndustRealTaskPegsInsert."""
class IndustRealTaskPegsInsert(IndustRealEnvPegs, FactoryABCTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def _get_task_yaml_params(self)
    def _acquire_task_tensors(self)
    def _refresh_task_tensors(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
    def _update_rew_buf(self)
    def _update_reset_buf(self)
    def reset_idx(self, env_ids)
    def _reset_franka(self)
    def _reset_object(self)
    def _reset_socket(self)
    def _reset_plug(self, before_move_to_grasp)
    def _reset_buffers(self)
    def _set_viewer_params(self)
    def _apply_actions_as_ctrl_targets(self, actions, ctrl_target_gripper_dof_pos, do_scale)
    def _move_gripper_to_grasp_pose(self, sim_steps)

```python
def compute_observations(self):
        """Compute observations."""

        delta_pos = self.gripper_goal_pos - self.fingertip_centered_pos
        noisy_delta_pos = self.noisy_gripper_goal_pos - self.fingertip_centered_pos

        # Define observations (for actor)
        obs_tensors = [
            self.arm_dof_pos,  # 7
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                1
            ],  # 4
            self.pose_world_to_robot_base(
                self.noisy_gripper_goal_pos, self.noisy_gripper_goal_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.noisy_gripper_goal_pos, self.noisy_gripper_goal_quat
            )[
                1
            ],  # 4
            noisy_delta_pos,
        ]  # 3

        # Define state (for critic)
        state_tensors = [
            self.arm_dof_pos,  # 7
            self.arm_dof_vel,  # 7
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.fingertip_centered_pos, self.fingertip_centered_quat
            )[
                1
            ],  # 4
            self.fingertip_centered_linvel,  # 3
            self.fingertip_centered_angvel,  # 3
            self.pose_world_to_robot_base(
                self.gripper_goal_pos, self.gripper_goal_quat
            )[
                0
            ],  # 3
            self.pose_world_to_robot_base(
                self.gripper_goal_pos, self.gripper_goal_quat
            )[
                1
            ],  # 4
            delta_pos,  # 3
            self.pose_world_to_robot_base(self.plug_pos, self.plug_quat)[0],  # 3
            self.pose_world_to_robot_base(self.plug_pos, self.plug_quat)[1],  # 4
            noisy_delta_pos - delta_pos,
        ]  # 3

        self.obs_buf = torch.cat(
            obs_tensors, dim=-1
        )  # shape = (num_envs, num_observations)
        self.states_buf = torch.cat(state_tensors, dim=-1)

        return self.obs_buf
```

```python
def compute_reward(self):
        """Detect successes and failures. Update reward and reset buffers."""

        self._update_rew_buf()
        self._update_reset_buf()
```
```

### isaacgymenvs/tasks/ingenuity.py

```
class Ingenuity(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ingenuity_asset(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def set_targets(self, env_ids)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, _actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
def compute_ingenuity_reward(root_positions, target_root_positions, root_quats, root_linvels, root_angvels, reset_buf, progress_buf, max_episode_length)

```python
def compute_ingenuity_reward(root_positions, target_root_positions, root_quats, root_linvels, root_angvels, reset_buf, progress_buf, max_episode_length):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, float) -> Tuple[Tensor, Tensor]

    # distance to target
    target_dist = torch.sqrt(torch.square(target_root_positions - root_positions).sum(-1))
    pos_reward = 1.0 / (1.0 + target_dist * target_dist)

    # uprightness
    ups = quat_axis(root_quats, 2)
    tiltage = torch.abs(1 - ups[..., 2])
    up_reward = 5.0 / (1.0 + tiltage * tiltage)

    # spinning
    spinnage = torch.abs(root_angvels[..., 2])
    spinnage_reward = 1.0 / (1.0 + spinnage * spinnage)

    # combined reward
    # uprigness and spinning only matter when close to the target
    reward = pos_reward + pos_reward * (up_reward + spinnage_reward)

    # resets due to misbehavior
    ones = torch.ones_like(reset_buf)
    die = torch.zeros_like(reset_buf)
    die = torch.where(target_dist > 8.0, ones, die)
    die = torch.where(root_positions[..., 2] < 0.5, ones, die)

    # resets due to episode length
    reset = torch.where(progress_buf >= max_episode_length - 1, ones, die)

    return reward, reset
```

```python
def compute_observations(self):
        self.obs_buf[..., 0:3] = (self.target_root_positions - self.root_positions) / 3
        self.obs_buf[..., 3:7] = self.root_quats
        self.obs_buf[..., 7:10] = self.root_linvels / 2
        self.obs_buf[..., 10:13] = self.root_angvels / math.pi
        return self.obs_buf
```

```python
def compute_reward(self):
        self.rew_buf[:], self.reset_buf[:] = compute_ingenuity_reward(
            self.root_positions,
            self.target_root_positions,
            self.root_quats,
            self.root_linvels,
            self.root_angvels,
            self.reset_buf, self.progress_buf, self.max_episode_length
        )
```
```

### isaacgymenvs/tasks/quadcopter.py

```
class Quadcopter(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_quadcopter_asset(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, _actions)
    def post_physics_step(self)
    def compute_observations(self)
    def compute_reward(self)
def compute_quadcopter_reward(root_positions, root_quats, root_linvels, root_angvels, reset_buf, progress_buf, max_episode_length)

```python
def compute_quadcopter_reward(root_positions, root_quats, root_linvels, root_angvels, reset_buf, progress_buf, max_episode_length):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, float) -> Tuple[Tensor, Tensor]

    # distance to target
    target_dist = torch.sqrt(root_positions[..., 0] * root_positions[..., 0] +
                             root_positions[..., 1] * root_positions[..., 1] +
                             (1 - root_positions[..., 2]) * (1 - root_positions[..., 2]))
    pos_reward = 1.0 / (1.0 + target_dist * target_dist)

    # uprightness
    ups = quat_axis(root_quats, 2)
    tiltage = torch.abs(1 - ups[..., 2])
    up_reward = 1.0 / (1.0 + tiltage * tiltage)

    # spinning
    spinnage = torch.abs(root_angvels[..., 2])
    spinnage_reward = 1.0 / (1.0 + spinnage * spinnage)

    # combined reward
    # uprigness and spinning only matter when close to the target
    reward = pos_reward + pos_reward * (up_reward + spinnage_reward)

    # resets due to misbehavior
    ones = torch.ones_like(reset_buf)
    die = torch.zeros_like(reset_buf)
    die = torch.where(target_dist > 3.0, ones, die)
    die = torch.where(root_positions[..., 2] < 0.3, ones, die)

    # resets due to episode length
    reset = torch.where(progress_buf >= max_episode_length - 1, ones, die)

    return reward, reset
```

```python
def compute_observations(self):
        target_x = 0.0
        target_y = 0.0
        target_z = 1.0
        self.obs_buf[..., 0] = (target_x - self.root_positions[..., 0]) / 3
        self.obs_buf[..., 1] = (target_y - self.root_positions[..., 1]) / 3
        self.obs_buf[..., 2] = (target_z - self.root_positions[..., 2]) / 3
        self.obs_buf[..., 3:7] = self.root_quats
        self.obs_buf[..., 7:10] = self.root_linvels / 2
        self.obs_buf[..., 10:13] = self.root_angvels / math.pi
        self.obs_buf[..., 13:21] = self.dof_positions
        return self.obs_buf
```

```python
def compute_reward(self):
        self.rew_buf[:], self.reset_buf[:] = compute_quadcopter_reward(
            self.root_positions,
            self.root_quats,
            self.root_linvels,
            self.root_angvels,
            self.reset_buf, self.progress_buf, self.max_episode_length
        )
```
```

### isaacgymenvs/tasks/shadow_hand.py

```
class ShadowHand(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_fingertip_observations(self, no_vel)
    def compute_full_observations(self, no_vel)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(object_pos - target_pos, p=2, dim=-1)

    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist * dist_reward_scale
    rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = dist_rew + rot_rew + action_penalty * action_penalty_scale

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threshold
    reward = torch.where(goal_dist >= fall_dist, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(goal_dist >= fall_dist, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length - 1, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length - 1, reward + 0.5 * fall_penalty, reward)

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, successes, cons_successes
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
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
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]

        if self.obs_type == "openai":
            self.compute_fingertip_observations(True)
        elif self.obs_type == "full_no_vel":
            self.compute_full_observations(True)
        elif self.obs_type == "full":
            self.compute_full_observations()
        elif self.obs_type == "full_state":
            self.compute_full_state()
        else:
            print("Unknown observations type!")

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_fingertip_observations(self, no_vel=False):
        if no_vel:
            # Per https://arxiv.org/pdf/1808.00177.pdf Table 2
            #   Fingertip positions
            #   Object Position, but not orientation
            #   Relative target orientation

            # 3*self.num_fingertips = 15
            self.obs_buf[:, 0:15] = self.fingertip_pos.reshape(self.num_envs, 15)
            self.obs_buf[:, 15:18] = self.object_pose[:, 0:3]
            self.obs_buf[:, 18:22] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 22:42] = self.actions
        else:
            # 13*self.num_fingertips = 65
            self.obs_buf[:, 0:65] = self.fingertip_state.reshape(self.num_envs, 65)
            self.obs_buf[:, 65:72] = self.object_pose
            self.obs_buf[:, 72:75] = self.object_linvel
            self.obs_buf[:, 75:78] = self.vel_obs_scale * self.object_angvel

            self.obs_buf[:, 78:85] = self.goal_pose
            self.obs_buf[:, 85:89] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 89:109] = self.actions
```

```python
def compute_full_observations(self, no_vel=False):
        if no_vel:
            self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                                   self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)

            self.obs_buf[:, 24:31] = self.object_pose
            self.obs_buf[:, 31:38] = self.goal_pose
            self.obs_buf[:, 38:42] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            # 3*self.num_fingertips = 15
            self.obs_buf[:, 42:57] = self.fingertip_pos.reshape(self.num_envs, 15)

            self.obs_buf[:, 57:77] = self.actions
        else:
            self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                                   self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
            self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel

            self.obs_buf[:, 48:55] = self.object_pose
            self.obs_buf[:, 55:58] = self.object_linvel
            self.obs_buf[:, 58:61] = self.vel_obs_scale * self.object_angvel

            self.obs_buf[:, 61:68] = self.goal_pose
            self.obs_buf[:, 68:72] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            # 13*self.num_fingertips = 65
            self.obs_buf[:, 72:137] = self.fingertip_state.reshape(self.num_envs, 65)

            self.obs_buf[:, 137:157] = self.actions
```
```

### isaacgymenvs/tasks/trifinger.py

```
class TrifingerDimensions(Enum)
    """Dimensions of the tri-finger robot.

Note: While it may not seem necessary for tri-finger robot since it is fixed base, for floating
base systems having this dimensions class is useful."""
class CuboidalObject()
    """Fields for a cuboidal object.

@note Motivation for this class is that if domain randomization is performed over the
      size of the cuboid, then its attributes are automatically updated as well."""
    def __init__(self, size)
    def size(self)
    def size(self, size)
    def __compute(self)
class Trifinger(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_scene_assets(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def __configure_mdp_spaces(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
    def _sample_robot_state(self, instances, distribution, dof_pos_stddev, dof_vel_stddev)
    def _sample_object_poses(self, instances, distribution)
    def _sample_object_goal_poses(self, instances, difficulty)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _check_termination(self)
    def __define_robot_asset(self)
    def __define_table_asset(self)
    def __define_boundary_asset(self)
    def __define_object_asset(self)
    def __define_goal_object_asset(self)
    def env_steps_count(self)
def lgsk_kernel(x, scale, eps)
def gen_keypoints(pose, num_keypoints, size)
def compute_trifinger_reward(obs_buf, reset_buf, progress_buf, episode_length, dt, finger_move_penalty_weight, finger_reach_object_weight, object_dist_weight, object_rot_weight, env_steps_count, object_goal_poses_buf, object_state, last_object_state, fingertip_state, last_fingertip_state, use_keypoints)
def compute_trifinger_observations_states(asymmetric_obs, dof_position, dof_velocity, object_state, object_goal_poses, actions, fingertip_state, joint_torques, tip_wrenches)
def random_xy(num, max_com_distance_to_center, device)
def random_z(num, min_height, max_height, device)
def default_orientation(num, device)
def random_orientation(num, device)
def random_orientation_within_angle(num, device, base, max_angle)
def random_angular_vel(num, device, magnitude_stdev)
def random_yaw_orientation(num, device)

```python
def compute_trifinger_reward(
        obs_buf: torch.Tensor,
        reset_buf: torch.Tensor,
        progress_buf: torch.Tensor,
        episode_length: int,
        dt: float,
        finger_move_penalty_weight: float,
        finger_reach_object_weight: float,
        object_dist_weight: float,
        object_rot_weight: float,
        env_steps_count: int,
        object_goal_poses_buf: torch.Tensor,
        object_state: torch.Tensor,
        last_object_state: torch.Tensor,
        fingertip_state: torch.Tensor,
        last_fingertip_state: torch.Tensor,
        use_keypoints: bool
) -> Tuple[torch.Tensor, torch.Tensor, Dict[str, torch.Tensor]]:

    ft_sched_start = 0
    ft_sched_end = 5e7

    # Reward penalising finger movement

    fingertip_vel = (fingertip_state[:, :, 0:3] - last_fingertip_state[:, :, 0:3]) / dt

    finger_movement_penalty = finger_move_penalty_weight * fingertip_vel.pow(2).view(-1, 9).sum(dim=-1)

    # Reward for finger reaching the object

    # distance from each finger to the centroid of the object, shape (N, 3).
    curr_norms = torch.stack([
        torch.norm(fingertip_state[:, i, 0:3] - object_state[:, 0:3], p=2, dim=-1)
        for i in range(3)
    ], dim=-1)
    # distance from each finger to the centroid of the object in the last timestep, shape (N, 3).
    prev_norms = torch.stack([
        torch.norm(last_fingertip_state[:, i, 0:3] - last_object_state[:, 0:3], p=2, dim=-1)
        for i in range(3)
    ], dim=-1)

    ft_sched_val = 1.0 if ft_sched_start <= env_steps_count <= ft_sched_end else 0.0
    finger_reach_object_reward = finger_reach_object_weight * ft_sched_val * (curr_norms - prev_norms).sum(dim=-1)

    if use_keypoints:
        object_keypoints = gen_keypoints(object_state[:, 0:7])
        goal_keypoints = gen_keypoints(object_goal_poses_buf[:, 0:7])

        delta = object_keypoints - goal_keypoints

        dist_l2 = torch.norm(delta, p=2, dim=-1)

        keypoints_kernel_sum = lgsk_kernel(dist_l2, scale=30., eps=2.).mean(dim=-1)

        pose_reward = object_dist_weight * dt * keypoints_kernel_sum

    else:

        # Reward for object distance
        object_dist = torch.norm(object_state[:, 0:3] - object_goal_poses_buf[:, 0:3], p=2, dim=-1)
        object_dist_reward = object_dist_weight * dt * lgsk_kernel(object_dist, scale=50., eps=2.)

        # Reward for object rotation

        # extract quaternion orientation
        quat_a = object_state[:, 3:7]
        quat_b = object_goal_poses_buf[:, 3:7]

        angles = quat_diff_rad(quat_a, quat_b)
        object_rot_reward =  object_rot_weight * dt / (3. * torch.abs(angles) + 0.01)

        pose_reward = object_dist_reward + object_rot_reward

    total_reward = (
            finger_movement_penalty
            + finger_reach_object_reward
            + pose_reward
    )

    # reset agents
    reset = torch.zeros_like(reset_buf)
    reset = torch.where(progress_buf >= episode_length - 1, torch.ones_like(reset_buf), reset)

    info: Dict[str, torch.Tensor] = {
        'finger_movement_penalty': finger_movement_penalty,
        'finger_reach_object_reward': finger_reach_object_reward,
        'pose_reward': finger_reach_object_reward,
        'reward': total_reward,
    }

    return total_reward, reset, info
```

```python
def compute_trifinger_observations_states(
        asymmetric_obs: bool,
        dof_position: torch.Tensor,
        dof_velocity: torch.Tensor,
        object_state: torch.Tensor,
        object_goal_poses: torch.Tensor,
        actions: torch.Tensor,
        fingertip_state: torch.Tensor,
        joint_torques: torch.Tensor,
        tip_wrenches: torch.Tensor
):

    num_envs = dof_position.shape[0]

    obs_buf = torch.cat([
        dof_position,
        dof_velocity,
        object_state[:, 0:7], # pose
        object_goal_poses,
        actions
    ], dim=-1)

    if asymmetric_obs:
        states_buf = torch.cat([
            obs_buf,
            object_state[:, 7:13], # linear / angular velocity
            fingertip_state.reshape(num_envs, -1),
            joint_torques,
            tip_wrenches
        ], dim=-1)
    else:
        states_buf = obs_buf

    return obs_buf, states_buf
```

```python
def compute_reward(self, actions):
        self.rew_buf[:] = 0.
        self.reset_buf[:] = 0.

        self.rew_buf[:], self.reset_buf[:], log_dict = compute_trifinger_reward(
            self.obs_buf,
            self.reset_buf,
            self.progress_buf,
            self.max_episode_length,
            self.cfg["sim"]["dt"],
            self.cfg["env"]["reward_terms"]["finger_move_penalty"]["weight"],
            self.cfg["env"]["reward_terms"]["finger_reach_object_rate"]["weight"],
            self.cfg["env"]["reward_terms"]["object_dist"]["weight"],
            self.cfg["env"]["reward_terms"]["object_rot"]["weight"],
            self.env_steps_count,
            self._object_goal_poses_buf,
            self._object_state_history[0],
            self._object_state_history[1],
            self._fingertips_frames_state_history[0],
            self._fingertips_frames_state_history[1],
            self.cfg["env"]["reward_terms"]["keypoints_dist"]["activate"]
        )

        self.extras.update({"env/rewards/"+k: v.mean() for k, v in log_dict.items()})
```

```python
def compute_observations(self):
        # refresh memory buffers
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.cfg["env"]["enable_ft_sensors"] or self.cfg["env"]["asymmetric_obs"]:
            self.gym.refresh_dof_force_tensor(self.sim)
            self.gym.refresh_force_sensor_tensor(self.sim)
            joint_torques = self._dof_torque
            tip_wrenches = self._ft_sensors_values

        else:
            joint_torques = torch.zeros(self.num_envs, self._dims.JointTorqueDim.value, dtype=torch.float32, device=self.device)
            tip_wrenches = torch.zeros(self.num_envs, self._dims.NumFingers.value * self._dims.WrenchDim.value, dtype=torch.float32, device=self.device)

        # extract frame handles
        fingertip_handles_indices = list(self._fingertips_handles.values())
        object_indices = self.gym_indices["object"]
        # update state histories
        self._fingertips_frames_state_history.appendleft(self._rigid_body_state[:, fingertip_handles_indices])
        self._object_state_history.appendleft(self._actors_root_state[object_indices])
        # fill the observations and states buffer

        self.obs_buf[:], self.states_buf[:] = compute_trifinger_observations_states(
            self.cfg["env"]["asymmetric_obs"],
            self._dof_position,
            self._dof_velocity,
            self._object_state_history[0],
            self._object_goal_poses_buf,
            self.actions,
            self._fingertips_frames_state_history[0],
            joint_torques,
            tip_wrenches,
        )

        # normalize observations if flag is enabled
        if self.cfg["env"]["normalize_obs"]:
            # for normal obs
            self.obs_buf = scale_transform(
                self.obs_buf,
                lower=self._observations_scale.low,
                upper=self._observations_scale.high
            )
```
```

### isaacgymenvs/tasks/utils/generate_cuboids.py

```
def generate_assets(scales, min_volume, max_volume, generated_assets_dir, base_mesh)
def generate_small_cuboids(assets_dir, base_mesh)
def generate_big_cuboids(assets_dir, base_mesh)
```

### isaacgymenvs/train.py

```
def preprocess_train_config(cfg, config_dict)
def launch_rlg_hydra(cfg)
```

### isaacgymenvs/utils/dr_utils.py

```
def get_property_setter_map(gym)
def get_property_getter_map(gym)
def get_default_setter_args(gym)
def generate_random_samples(attr_randomization_params, shape, curr_gym_step_count, extern_sample)
def get_bucketed_val(new_prop_val, attr_randomization_params)
def apply_random_samples(prop, og_prop, attr, attr_randomization_params, curr_gym_step_count, extern_sample, bucketing_randomization_params)
def check_buckets(gym, envs, dr_params)
```

### isaacgymenvs/utils/reformat.py

```
def omegaconf_to_dict(d)
def print_dict(val, nesting, start)
```

### isaacgymenvs/utils/rlgames_utils.py

```
def multi_gpu_get_rank(multi_gpu)
def get_rlgames_env_creator(seed, task_config, task_name, sim_device, rl_device, graphics_device_id, headless, multi_gpu, post_create_hook, virtual_screen_capture, force_render)
class RLGPUAlgoObserver(AlgoObserver)
    """Allows us to log stats from the env along with the algorithm running stats. """
    def __init__(self)
    def after_init(self, algo)
    def process_infos(self, infos, done_indices)
    def after_print_stats(self, frame, epoch_num, total_time)
class MultiObserver(AlgoObserver)
    """Meta-observer that allows the user to add several observers."""
    def __init__(self, observers_)
    def _call_multi(self, method)
    def before_init(self, base_name, config, experiment_name)
    def after_init(self, algo)
    def process_infos(self, infos, done_indices)
    def after_steps(self)
    def after_clear_stats(self)
    def after_print_stats(self, frame, epoch_num, total_time)
class RLGPUEnv(IVecEnv)
    def __init__(self, config_name, num_actors)
    def step(self, actions)
    def reset(self)
    def reset_done(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
class ComplexObsRLGPUEnv(IVecEnv)
    def __init__(self, config_name, num_actors, obs_spec)
    def _generate_obs(self, env_obs)
    def step(self, action)
    def reset(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def gen_obs_dict(self, obs_dict, obs_names, concat)
    def gen_obs_space(self, obs_names, concat)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
```

### isaacgymenvs/utils/rna_util.py

```
class RandomNetworkAdversary(Module)
    def __init__(self, num_envs, in_dims, out_dims, softmax_bins, device)
    def _refresh(self)
    def _init_weights(self)
    def refresh_dropout_masks(self)
    def forward(self, x)
```

### isaacgymenvs/utils/torch_jit_utils.py

```
def to_torch(x, dtype, device, requires_grad)
def quat_mul(a, b)
def normalize(x, eps)
def quat_apply(a, b)
def quat_rotate(q, v)
def quat_rotate_inverse(q, v)
def quat_conjugate(a)
def quat_unit(a)
def quat_from_angle_axis(angle, axis)
def normalize_angle(x)
def tf_inverse(q, t)
def tf_apply(q, t, v)
def tf_vector(q, v)
def tf_combine(q1, t1, q2, t2)
def get_basis_vector(q, v)
def get_axis_params(value, axis_idx, x_value, dtype, n_dims)
def copysign(a, b)
def get_euler_xyz(q)
def quat_from_euler_xyz(roll, pitch, yaw)
def torch_rand_float(lower, upper, shape, device)
def torch_random_dir_2(shape, device)
def tensor_clamp(t, min_t, max_t)
def scale(x, lower, upper)
def unscale(x, lower, upper)
def unscale_np(x, lower, upper)
def compute_heading_and_up(torso_rotation, inv_start_rot, to_target, vec0, vec1, up_idx)
def compute_rot(torso_quat, velocity, ang_velocity, targets, torso_positions)
def quat_axis(q, axis)
def scale_transform(x, lower, upper)
def unscale_transform(x, lower, upper)
def saturate(x, lower, upper)
def quat_diff_rad(a, b)
def local_to_world_space(pos_offset_local, pose_global)
def normalise_quat_in_pose(pose)
def my_quat_rotate(q, v)
def quat_to_angle_axis(q)
def angle_axis_to_exp_map(angle, axis)
def quat_to_exp_map(q)
def quaternion_to_matrix(quaternions)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def quat_to_tan_norm(q)
def euler_xyz_to_exp_map(roll, pitch, yaw)
def exp_map_to_angle_axis(exp_map)
def exp_map_to_quat(exp_map)
def slerp(q0, q1, t)
def calc_heading(q)
def calc_heading_quat(q)
def calc_heading_quat_inv(q)
```

### isaacgymenvs/utils/utils.py

```
def retry(times, exceptions)
def flatten_dict(d, prefix, separator)
def set_np_formatting()
def set_seed(seed, torch_deterministic, rank)
def nested_dict_set_attr(d, key, val)
def nested_dict_get_attr(d, key)
def ensure_dir_exists(path)
def safe_ensure_dir_exists(path)
def get_username()
def project_tmp_dir()
```

### isaacgymenvs/utils/wandb_utils.py

```
class WandbAlgoObserver(AlgoObserver)
    """Need this to propagate the correct experiment name after initialization."""
    def __init__(self, cfg)
    def before_init(self, base_name, config, experiment_name)
```