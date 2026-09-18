# eureka_2023

source: https://github.com/eureka-research/Eureka


commit: 9eee42808b52d8abc14845d1547bfde886403ccc


## README

# Eureka: Human-Level Reward Design via Coding Large Language Models (ICLR 2024)

<div align="center">

[[Website]](https://eureka-research.github.io)
[[arXiv]](https://arxiv.org/abs/2310.12931)
[[PDF]](https://eureka-research.github.io/assets/eureka_paper.pdf)

[![Python Version](https://img.shields.io/badge/Python-3.8-blue.svg)](https://github.com/eureka-research/Eureka)
[<img src="https://img.shields.io/badge/Framework-PyTorch-red.svg"/>](https://pytorch.org/)
[![GitHub license](https://img.shields.io/github/license/eureka-research/Eureka)](https://github.com/eureka-research/Eureka/blob/main/LICENSE)
______________________________________________________________________

https://github.com/eureka-research/Eureka/assets/21993118/1abb960d-321a-4de9-b311-113b5fc53d4a



![](images/eureka.png)
</div>

Large Language Models (LLMs) have excelled as high-level semantic planners for sequential decision-making tasks. However, harnessing them to learn complex low-level manipulation tasks, such as dexterous pen spinning, remains an open problem. We bridge this fundamental gap and present Eureka, a **human-level** reward design algorithm powered by LLMs. Eureka exploits the remarkable zero-shot generation, code-writing, and in-context improvement capabilities of state-of-the-art LLMs, such as GPT-4, to perform in-context evolutionary optimization over reward code. The resulting rewards can then be used to acquire complex skills via reinforcement learning. Eureka generates reward functions that outperform expert human-engineered rewards without any task-specific prompting or pre-defined reward templates. In a diverse suite of 29 open-source RL environments that include 10 distinct robot morphologies, Eureka outperforms human expert on **83\%** of the tasks leading to an average normalized improvement of **52\%**. The generality of Eureka also enables a new gradient-free approach to reinforcement learning from human feedback (RLHF), readily incorporating human oversight to improve the quality and the safety of the generated rewards in context. Finally, using Eureka rewards in a curriculum learning setting, we demonstrate for the first time a simulated five-finger Shadow Hand capable of performing pen spinning tricks, adeptly manipulating a pen in circles at human speed. 

# Installation
Eureka requires Python ≥ 3.8. We have tested on Ubuntu 20.04 and 22.04.

1. Create a new conda environment with:
    ```
    conda create -n eureka python=3.8
    conda activate eureka
    ```

2. Install IsaacGym (tested with `Preview Release 4/4`). Follow the [instruction](https://developer.nvidia.com/isaac-gym) to download the package.
```	
tar -xvf IsaacGym_Preview_4_Package.tar.gz
cd isaacgym/python
pip install -e .
(test installation) python examples/joint_monkey.py
```

3. Install Eureka
```
git clone https://github.com/eureka-research/Eureka.git
cd Eureka; pip install -e .
cd isaacgymenvs; pip install -e .
cd ../rl_games; pip install -e .
```

4. Eureka currently uses OpenAI API for language model queries. You need to have an OpenAI API key to use Eureka [here](https://platform.openai.com/account/api-keys)/. Then, set the environment variable in your terminal
```
export OPENAI_API_KEY= "YOUR_API_KEY"
```

# Getting Started

Navigate to the `eureka` directory and run:
```
python eureka.py env={environment} iteration={num_iterations} sample={num_samples}
```
- `{environment}` is the task to perform. Options are listed in `eureka/cfg/env`.
- `{num_samples}` is the number of reward samples to generate per iteration. Default value is `16`.
- `{num_iterations}` is the number of Eureka iterations to run. Default value is `5`.


Below are some example commands to try out Eureka:
```
python eureka.py env=shadow_hand sample=4 iteration=2 model=gpt-4-0314
```
```
python eureka.py env=humanoid sample=16 iteration=5 model=gpt-3.5-turbo-16k-0613
```
Each run will create a timestamp folder in `eureka/outputs` that saves the Eureka log as well as all intermediate reward functions and associated policies.

Other command line parameters can be found in `eureka/cfg/config.yaml`. The list of supported environments can be found in `eureka/cfg/env`.

# Eureka Pen Spinning Demo
We have released Eureka pen spinning policy in `isaacgymenvs/isaacgymenvs/checkpoints`. Try visualizing it with the following command:
```
cd isaacgymenvs/isaacgymenvs
python train.py test=True headless=False force_render=True task=ShadowHandSpin checkpoint=checkpoints/EurekaPenSpinning.pth
```
Note that this script use the default Isaac Gym renderer and not the Omniverse rendering in the paper videos.

# Running Eureka on a New Environment
1. Create a new IsaacGym environment; instructions can be found in [here](isaacgymenvs/docs/framework.md).
2. Verify that standard RL works for your new environment.
```
cd isaacgymenvs/isaacgymenvs
python train.py task=YOUR_NEW_TASK
```
3. Create a new yaml file `your_new_task.yaml` in `eureka/cfg/env`:
```
env_name: your_new_task
task: YOUR_NEW_TASK 
description: ...
```
4. Construct the raw environment code that will serve as context for Eureka as well as the skeleton environment code on which the Eureka reward will be appended to:
```
cd eureka/utils
python prune_env.py your_new_task
```

5. Try out Eureka!
```
python eureka.py env=your_new_task
```

# Acknowledgement
We thank the following open-sourced projects:
- Our environments are from [IsaacGym](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs) and [DexterousHands](https://github.com/PKU-MARL/DexterousHands/).
- Our RL training code is based on [rl_games](https://github.com/Denys88/rl_games).


# License
This codebase is released under [MIT License](LICENSE).

# Citation
If you find our work useful, please consider citing us!

```bibtex
@article{ma2023eureka,
  title   = {Eureka: Human-Level Reward Design via Coding Large Language Models},
  author  = {Yecheng Jason Ma and William Liang and Guanzhi Wang and De-An Huang and Osbert Bastani and Dinesh Jayaraman and Yuke Zhu and Linxi Fan and Anima Anandkumar},
  year    = {2023},
  journal = {arXiv preprint arXiv: Arxiv-2310.12931}
}
```

Disclaimer: This project is strictly for research purposes, and not an official product from NVIDIA.



## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
eureka/
  cfg/
    config.yaml
    env/
    hydra/
  envs/
    bidex/
    isaac/
  eureka.py
  utils/
    create_task.py
    extract_task_code.py
    file_utils.py
    misc.py
    prompts/
    prune_env.py
    prune_env_dexterity.py
    prune_env_isaac.py
isaacgymenvs/
  .gitattributes
  .gitignore
  .gitlab/
    issue_templates/
  .pre-commit-config.yaml
  LICENSE.txt
  README.md
  isaacgymenvs/
    __init__.py
    cfg/
    learning/
    tasks/
    train.py
    utils/
  setup.py
rl_games/
  .github/
    workflows/
  .gitignore
  LICENSE
  README.md
  notebooks/
    brax_training.ipynb
    brax_visualization.ipynb
    mujoco_envpool_training.ipynb
    train_and_export_onnx_example_continuous.ipynb
    train_and_export_onnx_example_discrete.ipynb
    train_and_export_onnx_example_lstm_continuous.ipynb
  poetry.lock
  pyproject.toml
  rl_games/
    __init__.py
    algos_torch/
    common/
    configs/
    distributed/
    envs/
    interfaces/
    networks/
    torch_runner.py
  runner.py
  setup.py
  tests/
    __init__.py
    simple_test.py
setup.py
```

## Config files (352)


### eureka/cfg/config.yaml

```yaml
defaults:
  - _self_
  - env: shadow_hand
  - override hydra/launcher: local
  - override hydra/output: local

hydra:
  job:
    chdir: True

# LLM parameters
model: gpt-4-0314  # LLM model (other options are gpt-4, gpt-4-0613, gpt-3.5-turbo-16k-0613)
temperature: 1.0
suffix: GPT  # suffix for generated files (indicates LLM model)

# Eureka parameters
iteration: 1 # how many iterations of Eureka to run
sample: 3 # number of Eureka samples to generate per iteration
max_iterations: 3000 # RL Policy training iterations (decrease this to make the feedback loop faster)
num_eval: 5 # number of evaluation episodes to run for the final reward
capture_video: False # whether to capture policy rollout videos

# Weights and Biases
use_wandb: False # whether to use wandb for logging
wandb_username: "" # wandb username if logging with wandb
wandb_project: "" # wandb project if logging with wandb
```

### eureka/cfg/env/allegro_hand.yaml

```yaml
task: AllegroHand
env_name: allegro_hand
description: to make the hand spin the object to a target orientation 
max_iterations: 5000
```

### eureka/cfg/env/ant.yaml

```yaml
task: Ant
env_name: ant
description: to make the ant run forward as fast as possible
```

### eureka/cfg/env/anymal.yaml

```yaml
task: Anymal
env_name: anymal
description: to make the quadruped follow randomly chosen x,y, and yaw target velocities
max_iterations: 1000
```

### eureka/cfg/env/ballbalance.yaml

```yaml
task: BallBalance
env_name: ball_balance
description: to keep the ball on the table top without falling
```

### eureka/cfg/env/cartpole.yaml

```yaml
task: Cartpole
env_name: cartpole
description: to balance a pole on a cart so that the pole stays upright
```

### eureka/cfg/env/franka_cabinet.yaml

```yaml
task: FrankaCabinet
env_name: franka_cabinet
description: to open the cabinet door
max_iterations: 1500
```

### eureka/cfg/env/franka_cube_stack.yaml

```yaml
task: FrankaCubeStack
env_name: franka_cube_stack
description: to stack a cube on top of an other cube
max_iterations: 10000
```

### eureka/cfg/env/humanoid.yaml

```yaml
task: Humanoid # Environment class Name in the environment file
env_name: humanoid # Environment file name
description: to make the humanoid run as fast as possible

```

### eureka/cfg/env/humanoidamp.yaml

```yaml
task: HumanoidAMP
env_name: amp/humanoid_amp_base
description: to make the humanoid do a moon walk with feet sliding off the ground alternatingly to move backward
```

### eureka/cfg/env/ingenuity.yaml

```yaml
task: Ingenuity
env_name: ingenuity
description: to NASA's Ingenuity helicopter to navigate to a moving target
```

### eureka/cfg/env/quadcopter.yaml

```yaml
task: Quadcopter
env_name: quadcopter
description: to make the quadcopter reach and hover near a fixed position
```

### eureka/cfg/env/shadow_hand.yaml

```yaml
task: ShadowHand
env_name: shadow_hand
description: to make the shadow hand spin the object to a target orientation 
```

### eureka/cfg/env/shadow_hand_block_stack.yaml

```yaml
description: This class corresponds to the Block Stack task. This environment involves
  dual hands and two blocks, and we need to stack the block as a tower.
env_name: shadow_hand_block_stack
task: ShadowHandBlockStack

```

### eureka/cfg/env/shadow_hand_bottle_cap.yaml

```yaml
description: This class corresponds to the Bottle Cap task. This environment involves
  two hands and a bottle, we  need to hold the bottle with one hand and open the bottle
  cap with the other hand. This skill requires  the cooperation of two hands to ensure
  that the cap does not fall.
env_name: shadow_hand_bottle_cap
task: ShadowHandBottleCap

```

### eureka/cfg/env/shadow_hand_catch_abreast.yaml

```yaml
description: This class corresponds to the Catch Abreast task. This environment consists
  of two shadow hands placed  side by side in the same direction and an object that
  needs to be passed. Compared with the previous  environment which is more like passing
  objects between the hands of two people, this environment is  designed to simulate
  the two hands of the same person passing objects, so different catch techniques  are
  also required and require more hand translation and rotation techniques.
env_name: shadow_hand_catch_abreast
task: ShadowHandCatchAbreast

```

### eureka/cfg/env/shadow_hand_catch_over2underarm.yaml

```yaml
description: This class corresponds to the Over2Underarm task. This environment is
  similar to Catch Underarm,  but with an object in each hand and the corresponding
  goal on the other hand. Therefore, the environment  requires two objects to be thrown
  into the other hand at the same time, which requires a higher  manipulation technique
  than the environment of a single object.
env_name: shadow_hand_catch_over2underarm
task: ShadowHandCatchOver2Underarm

```

### eureka/cfg/env/shadow_hand_catch_underarm.yaml

```yaml
description: This class corresponds to the Catch Underarm task. In this task, two
  shadow hands with palms facing upwards are controlled to pass an object from one
  palm to the other. What makes it more difficult  than the Hand over task is that
  the hands' translation and rotation degrees of freedom are no longer  frozen but
  are added into the action space
env_name: shadow_hand_catch_underarm
task: ShadowHandCatchUnderarm

```

### eureka/cfg/env/shadow_hand_door_close_inward.yaml

```yaml
description: This class corresponds to the DoorCloseInward task. This environment
  require a closed door  to be opened and the door can only be pushed outward or initially
  open inward. Both these two  environments only need to do the push behavior, so
  it is relatively simple
env_name: shadow_hand_door_close_inward
task: ShadowHandDoorCloseInward

```

### eureka/cfg/env/shadow_hand_door_close_outward.yaml

```yaml
description: This class corresponds to the DoorCloseOutward task. This environment
  also require a closed door  to be opened and the door can only be pushed inward
  or initially open outward, but because they  can't complete the task by simply pushing,
  which need to catch the handle by hand and then open  or close it, so it is relatively
  difficult.
env_name: shadow_hand_door_close_outward
task: ShadowHandDoorCloseOutward

```

### eureka/cfg/env/shadow_hand_door_open_inward.yaml

```yaml
description: This class corresponds to the DoorOpenInward task. This environment also
  require a opened door  to be closed and the door can only be pushed inward or initially
  open outward, but because they  can't complete the task by simply pushing, which
  need to catch the handle by hand and then open  or close it, so it is relatively
  difficult.
env_name: shadow_hand_door_open_inward
task: ShadowHandDoorOpenInward

```

### eureka/cfg/env/shadow_hand_door_open_outward.yaml

```yaml
description: This class corresponds to the DoorOpenOutward task. This environment
  require a opened door  to be closed and the door can only be pushed outward or initially
  open inward. Both these two  environments only need to do the push behavior, so
  it is relatively simple
env_name: shadow_hand_door_open_outward
task: ShadowHandDoorOpenOutward

```

### eureka/cfg/env/shadow_hand_free_arm.yaml

```yaml
task: ShadowHandFreeArm
env_name: shadow_hand_free_arm
description: to make the shadow hand, whose arm is not fixed, spin the object to a target orientation; 
```

### eureka/cfg/env/shadow_hand_grasp_and_place.yaml

```yaml
description: This class corresponds to the GraspAndPlace task. This environment consists
  of dual-hands, an object and a bucket that requires us to pick up the object and
  put it into the bucket.
env_name: shadow_hand_grasp_and_place
task: ShadowHandGraspAndPlace

```

### eureka/cfg/env/shadow_hand_kettle.yaml

```yaml
description: This class corresponds to the PourWater task. This environment involves
  two hands, a kettle, and a bucket, we need to hold the kettle with one hand and the bucket
  with the other hand, and pour the water from the kettle into the bucket. In the
  practice task in Isaac Gym, we use many small balls to simulate the water
env_name: shadow_hand_kettle
task: ShadowHandKettle

```

### eureka/cfg/env/shadow_hand_lift_underarm.yaml

```yaml
description: This class corresponds to the LiftUnderarm task. This environment requires
  grasping the pot handle  with two hands and lifting the pot to the designated position.
  This environment is designed to  simulate the scene of lift in daily life and is
  a practical skill.
env_name: shadow_hand_lift_underarm
task: ShadowHandLiftUnderarm

```

### eureka/cfg/env/shadow_hand_over.yaml

```yaml
description: This class corresponds to the HandOver task. This environment consists
  of two shadow hands with palms facing up, opposite each other, and an object that
  needs to be passed. In the beginning,  the object will fall randomly in the area
  of the shadow hand on the right side. Then the hand  holds the object and passes
  the object to the other hand. Note that the base of the hand is  fixed. More importantly,
  the hand which holds the object initially can not directly touch the  target, nor
  can it directly roll the object to the other hand, so the object must be thrown
  up  and stays in the air in the process
env_name: shadow_hand_over
task: ShadowHandOver

```

### eureka/cfg/env/shadow_hand_pen.yaml

```yaml
description: This class corresponds to the Open Pen Cap task. This environment involves
  two hands and a pen, we need to use two hands to open the pen cap.
env_name: shadow_hand_pen
task: ShadowHandPen

```

### eureka/cfg/env/shadow_hand_push_block.yaml

```yaml
description: This class corresponds to the PushBlock task. This environment involves
  two hands and two blocks,  we need to use both hands to reach and push the block
  to the desired goal separately. This is a  relatively simple task
env_name: shadow_hand_push_block
task: ShadowHandPushBlock

```

### eureka/cfg/env/shadow_hand_re_orientation.yaml

```yaml
description: This class corresponds to the ReOrientation task. This environment involves
  two hands and two objects.  Each hand holds an object and we need to reorient the
  object to the target orientation
env_name: shadow_hand_re_orientation
task: ShadowHandReOrientation

```

### eureka/cfg/env/shadow_hand_scissors.yaml

```yaml
description: This class corresponds to the Scissors task. This environment involves
  two hands and scissors,  we need to use two hands to open the scissors
env_name: shadow_hand_scissors
task: ShadowHandScissors

```

### eureka/cfg/env/shadow_hand_spin.yaml

```yaml
task: ShadowHandSpin
env_name: shadow_hand_spin
description: to make the shadow hand spin the pen to a target orientation
```

### eureka/cfg/env/shadow_hand_swing_cup.yaml

```yaml
description: This class corresponds to the SwingCup task. This environment involves
  two hands and a dual handle  cup, we need to use two hands to hold and swing the
  cup together
env_name: shadow_hand_swing_cup
task: ShadowHandSwingCup

```

### eureka/cfg/env/shadow_hand_switch.yaml

```yaml
description: This class corresponds to the Switch task. This environment involves
  dual hands and a bottle, we  need to use dual hand fingers to press the desired
  button
env_name: shadow_hand_switch
task: ShadowHandSwitch

```

### eureka/cfg/env/shadow_hand_two_catch_underarm.yaml

```yaml
description: This class corresponds to the TwoCatchUnderarm task. This environment
  is similar to Catch Underarm,  but with an object in each hand and the corresponding
  goal on the other hand. Therefore, the  environment requires two objects to be thrown
  into the other hand at the same time, which requires  a higher manipulation technique
  than the environment of a single object
env_name: shadow_hand_two_catch_underarm
task: ShadowHandTwoCatchUnderarm

```

### eureka/cfg/env/shadow_hand_upside_down.yaml

```yaml
task: ShadowHandUpsideDown
env_name: shadow_hand_upside_down
description: to make the shadow hand, whose palm faces down, spin the object to a target orientation; 
```

### eureka/cfg/env/trifinger.yaml

```yaml
task: Trifinger
env_name: trifinger
description: to move the cube to the desired target location
```

### eureka/cfg/hydra/launcher/local.yaml

```yaml
# @package _global_
hydra:
    launcher:
        cpus_per_task: 20
        gpus_per_node: 8
        tasks_per_node: 1
        timeout_min: 1600
        mem_gb: 512
        name: ${hydra.job.name}
        _target_: hydra_plugins.hydra_submitit_launcher.submitit_launcher.LocalLauncher
        submitit_folder: ${hydra.sweep.dir}/.submitit/%j

```

### eureka/cfg/hydra/output/local.yaml

```yaml
# @package _global_
hydra:
  run:
    dir: ./outputs/${hydra.job.name}/${now:%Y-%m-%d}_${now:%H-%M-%S}
    subdir: ${hydra.job.num}_${hydra.job.override_dirname}
  sweep:
    dir: ./outputs/${hydra.job.name}/${now:%Y-%m-%d}_${now:%H-%M-%S}
    subdir: ${hydra.job.num}_${hydra.job.override_dirname}
```

### isaacgymenvs/.pre-commit-config.yaml

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

### isaacgymenvs/isaacgymenvs/cfg/config.yaml

```yaml
defaults:
  - _self_
  - task: Ant
  - train: ${task}PPO
  - hydra/job_logging: disabled
  - override hydra/launcher:  local
  - override hydra/output:  local

# Task name - used to pick the class to load
task_name: ${task.name}
# experiment name. defaults to name of training config
experiment: ''

# env_path for custom environment
env_path: ''

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
# set to True to use multi-gpu horovod training
multi_gpu: False

wandb_activate: False
wandb_group: ''
wandb_name: ${train.params.config.name}
# wandb_entity: ''
# wandb_project: 'isaacgymenvs'
wandb_entity: 'jma2020'
wandb_project: 'isaac_gpt'
wandb_tags: []
wandb_logcode_dir: '' 

capture_video: False
capture_video_freq: 5000
capture_video_len: 200
force_render: False

# disables rendering
# headless: False
headless: True 

# set default task and default training config based on task
# defaults:
#   - task: Ant
#   - train: ${task}PPO
#   - hydra/job_logging: disabled

# set the directory where the output files get saved
# hydra:
#   output_subdir: null
#   run:
#     dir: .


```

### isaacgymenvs/isaacgymenvs/cfg/hydra/launcher/local.yaml

```yaml
# @package _global_
hydra:
    launcher:
        cpus_per_task: 20
        gpus_per_node: 2
        tasks_per_node: 1
        timeout_min: 600
        mem_gb: 256
        name: ${hydra.job.name}
        _target_: hydra_plugins.hydra_submitit_launcher.submitit_launcher.LocalLauncher
        submitit_folder: ${hydra.sweep.dir}/.submitit/%j

```

### isaacgymenvs/isaacgymenvs/cfg/hydra/output/local.yaml

```yaml
# @package _global_
hydra:
  run:
    dir: ./outputs/${hydra.job.name}/${now:%Y-%m-%d}_${now:%H-%M-%S}
    subdir: ${hydra.job.num}_${hydra.job.override_dirname}
  sweep:
    dir: ./outputs/${hydra.job.name}/${now:%Y-%m-%d}_${now:%H-%M-%S}
    subdir: ${hydra.job.num}_${hydra.job.override_dirname}
```

### isaacgymenvs/isaacgymenvs/cfg/hydra/output/subprocess.yaml

```yaml
# @package _global_
hydra:
  output_subdir: null
  run:
    dir: ./policy-${now:%Y-%m-%d}_${now:%H-%M-%S}
```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHand.yaml

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
    assetFileName: "urdf/kuka_allegro_description/allegro.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

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

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandDextremeADR.yaml

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
    assetFileName: "urdf/kuka_allegro_description/allegro.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

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

    worker_adr_boundary_fraction: 0.4 # fraction of workers dedicated to measuring perf of ends of ADR ranges to update the ranges

    adr_queue_threshold_length: 256

    adr_objective_threshold_low: 5
    
```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandDextremeManualDR.yaml

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
    assetFileName: "urdf/kuka_allegro_description/allegro.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor_allegro.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

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
          # schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          # schedule_steps: 30000
        rigid_body_properties:
   
```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandFF.yaml

```yaml
defaults:
  - AllegroHandLSTM
  - _self_
```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandGPT.yaml

```yaml
env:
  actionPenaltyScale: -0.0002
  actionsMovingAverage: 1.0
  aggregateMode: 1
  asset:
    assetFileName: urdf/kuka_allegro_description/allegro.urdf
    assetFileNameBlock: urdf/objects/cube_multicolor_allegro.urdf
    assetFileNameEgg: mjcf/open_ai_assets/hand/egg.xml
    assetFileNamePen: mjcf/open_ai_assets/hand/pen.xml
  asymmetric_observations: false
  clipActions: 1.0
  clipObservations: 5.0
  controlFrequencyInv: 2
  distRewardScale: -10.0
  dofSpeedScale: 20.0
  enableDebugVis: false
  envSpacing: 0.75
  env_name: allegro_handGPT
  episodeLength: 600
  fallDistance: 0.24
  fallPenalty: 0.0
  forceDecay: 0.99
  forceDecayInterval: 0.08
  forceLimitScale: 1.0
  forceProbRange:
  - 0.001
  - 0.1
  forceScale: 0.0
  maxConsecutiveSuccesses: 0
  numEnvs: ${resolve_default:16384,${...num_envs}}
  objectType: block
  observationType: full_state
  printNumSuccesses: false
  reachGoalBonus: 250
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0
  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  rotEps: 0.1
  rotRewardScale: 1.0
  startObjectPoseDY: -0.19
  startObjectPoseDZ: 0.06
  startPositionNoise: 0.01
  startRotationNoise: 0.0
  stiffnessScale: 1.0
  successTolerance: 0.1
  useRelativeControl: false
name: AllegroHandGPT
physics_engine: ${..physics_engine}
sim:
  dt: 0.01667
  gravity:
  - 0.0
  - 0.0
  - -9.81
  physx:
    bounce_threshold_velocity: 0.2
    contact_collection: 0
    contact_offset: 0.002
    default_buffer_size_multiplier: 5.0
    max_depenetration_velocity: 1000.0
    max_gpu_contact_pairs: 8388608
    num_position_iterations: 8
    num_subscenes: ${....num_subscenes}
    num_threads: ${....num_threads}
    num_velocity_iterations: 0
    rest_offset: 0.0
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}}
  substeps: 2
  up_axis: z
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
task:
  enableCameraSensors: false
  randomization_params:
    actions:
      distribution: gaussian
      operation: additive
      range:
      - 0.0
      - 0.05
      range_correlated:
      - 0
      - 0.015
    actor_params:
      hand:
        color: true
        dof_properties:
          damping:
            distribution: loguniform
            operation: scaling
            range:
            - 0.3
            - 3.0
          lower:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
          stiffness:
            distribution: loguniform
            operation: scaling
            range:
            - 0.75
            - 1.5
          upper:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
        rigid_body_properties:
          mass:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            setup_only: true
        rigid_shape_properties:
          friction:
            distribution: uniform
            num_buckets: 250
            operation: scaling
            range:
            - 0.7
            - 1.3
      object:
        rigid_body_properties:
          mass:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            setup_only: true
        rigid_shape_properties:
          friction:
            distribution: uniform
            num_buckets: 250
            operation: scaling
            range:
            - 0.7
            - 1.3
        scale:
          distribution: uniform
          operation: scaling
          range:
          - 0.95
          - 1.05
          setup_only: true
    frequency: 720
    observations:
      distribution: gaussian
      operation: additive
      range:
      - 0
      - 0.002
      range_correlated:
      - 0
      - 0.001
    sim_params:
      gravity:
        distribution: gaussian
        operation: additive
        range:
        - 0
        - 0.4
  randomize: false

```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandLSTM.yaml

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

  #clipObservations: 5.0
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
            num_buckets: 100
            range: [0.0, 0.4]
        
```

### isaacgymenvs/isaacgymenvs/cfg/task/AllegroHandLSTM_Big.yaml

```yaml
defaults:
  - AllegroHandLSTM
  - _self_


```

### isaacgymenvs/isaacgymenvs/cfg/task/Ant.yaml

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

### isaacgymenvs/isaacgymenvs/cfg/task/AntGPT.yaml

```yaml
env:
  actionsCost: 0.005
  asset:
    assetFileName: mjcf/nv_ant.xml
  clipActions: 1.0
  contactForceScale: 0.1
  controlFrequencyInv: 1
  deathCost: -2.0
  dofVelocityScale: 0.2
  enableCameraSensors: false
  enableDebugVis: false
  energyCost: 0.05
  envSpacing: 5
  env_name: antGPT
  episodeLength: 1000
  headingWeight: 0.5
  jointsAtLimitCost: 0.1
  numEnvs: ${resolve_default:4096,${...num_envs}}
  plane:
    dynamicFriction: 1.0
    restitution: 0.0
    staticFriction: 1.0
  powerScale: 1.0
  terminationHeight: 0.31
  upWeight: 0.1
name: AntGPT
physics_engine: ${..physics_engine}
sim:
  dt: 0.0166
  gravity:
  - 0.0
  - 0.0
  - -9.81
  physx:
    bounce_threshold_velocity: 0.2
    contact_collection: 0
    contact_offset: 0.02
    default_buffer_size_multiplier: 5.0
    max_depenetration_velocity: 10.0
    max_gpu_contact_pairs: 8388608
    num_position_iterations: 4
    num_subscenes: ${....num_subscenes}
    num_threads: ${....num_threads}
    num_velocity_iterations: 0
    rest_offset: 0.0
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}}
  substeps: 2
  up_axis: z
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
task:
  randomization_params:
    actions:
      distribution: gaussian
      operation: additive
      range:
      - 0.0
      - 0.02
    actor_params:
      ant:
        color: true
        dof_properties:
          damping:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
          lower:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
          stiffness:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
          upper:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
        rigid_body_properties:
          mass:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            setup_only: true
    frequency: 600
    observations:
      distribution: gaussian
      operation: additive
      range:
      - 0
      - 0.002
  randomize: false

```

### isaacgymenvs/isaacgymenvs/cfg/task/AntSAC.yaml

```yaml
# used to create the object
defaults:
  - Ant
  - _self_

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:64,${...num_envs}}
```

### isaacgymenvs/isaacgymenvs/cfg/task/Anymal.yaml

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

### isaacgymenvs/isaacgymenvs/cfg/task/AnymalGPT.yaml

```yaml
env:
  baseInitState:
    pos:
    - 0.0
    - 0.0
    - 0.62
    rot:
    - 0.0
    - 0.0
    - 0.0
    - 1.0
    vAngular:
    - 0.0
    - 0.0
    - 0.0
    vLinear:
    - 0.0
    - 0.0
    - 0.0
  clipActions: 1.0
  clipObservations: 5.0
  control:
    actionScale: 0.5
    controlFrequencyInv: 1
    damping: 2.0
    stiffness: 85.0
  defaultJointAngles:
    LF_HAA: 0.03
    LF_HFE: 0.4
    LF_KFE: -0.8
    LH_HAA: 0.03
    LH_HFE: -0.4
    LH_KFE: 0.8
    RF_HAA: -0.03
    RF_HFE: 0.4
    RF_KFE: -0.8
    RH_HAA: -0.03
    RH_HFE: -0.4
    RH_KFE: 0.8
  enableCameraSensors: false
  envSpacing: 4.0
  env_name: anymalGPT
  learn:
    angularVelocityScale: 0.25
    angularVelocityZRewardScale: 0.5
    dofPositionScale: 1.0
    dofVelocityScale: 0.05
    episodeLength_s: 50
    linearVelocityScale: 2.0
    linearVelocityXYRewardScale: 1.0
    torqueRewardScale: -2.5e-05
  numEnvs: ${resolve_default:4096,${...num_envs}}
  plane:
    dynamicFriction: 1.0
    restitution: 0.0
    staticFriction: 1.0
  randomCommandVelocityRanges:
    linear_x:
    - -2.0
    - 2.0
    linear_y:
    - -1.0
    - 1.0
    yaw:
    - -1.0
    - 1.0
  urdfAsset:
    collapseFixedJoints: true
    defaultDofDriveMode: 4
    fixBaseLink: false
  viewer:
    lookat:
    - 1.0
    - 1
    - 3.3
    pos:
    - 0
    - 0
    - 4
    refEnv: 0
name: AnymalGPT
physics_engine: ${..physics_engine}
sim:
  dt: 0.02
  gravity:
  - 0.0
  - 0.0
  - -9.81
  physx:
    bounce_threshold_velocity: 0.2
    contact_collection: 1
    contact_offset: 0.02
    default_buffer_size_multiplier: 5.0
    max_depenetration_velocity: 100.0
    max_gpu_contact_pairs: 8388608
    num_position_iterations: 4
    num_subscenes: ${....num_subscenes}
    num_threads: ${....num_threads}
    num_velocity_iterations: 1
    rest_offset: 0.0
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}}
  substeps: 2
  up_axis: z
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
task:
  randomization_params:
    actions:
      distribution: gaussian
      operation: additive
      range:
      - 0.0
      - 0.02
    actor_params:
      anymal:
        color: true
        dof_properties:
          damping:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            schedule: linear
            schedule_steps: 3000
          lower:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
            schedule: linear
            schedule_steps: 3000
          stiffness:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            schedule: linear
            schedule_steps: 3000
          upper:
            distribution: gaussian
            operation: additive
            range:
            - 0
            - 0.01
            schedule: linear
            schedule_steps: 3000
        rigid_body_properties:
          mass:
            distribution: uniform
            operation: scaling
            range:
            - 0.5
            - 1.5
            schedule: linear
            schedule_steps: 3000
            setup_only: true
        rigid_shape_properties:
          friction:
            distribution: uniform
            num_buckets: 500
            operation: scaling
            range:
            - 0.7
            - 1.3
            schedule: linear
            schedule_steps: 3000
          restitution:
            distribution: uniform
            operation: scaling
            range:
            - 0.0
            - 0.7
            schedule: linear
            schedule_steps: 3000
    frequency: 600
    observations:
      distribution: gaussian
      operation: additive
      range:
      - 0
      - 0.002
    sim_params:
      gravity:
        distribution: gaussian
        operation: additive
        range:
        - 0
        - 0.4
        schedule: linear
        schedule_steps: 3000
  randomize: false

```

### isaacgymenvs/isaacgymenvs/cfg/task/AnymalTerrain.yaml

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

### isaacgymenvs/isaacgymenvs/cfg/task/BallBalance.yaml

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

### isaacgymenvs/isaacgymenvs/cfg/task/BallBalanceGPT.yaml

```yaml
env:
  actionSpeedScale: 20
  clipActions: 1.0
  clipObservations: 5.0
  enableCameraSensors: false
  enableDebugVis: false
  envSpacing: 2.0
  env_name: ball_balanceGPT
  maxEpisodeLength: 500
  numEnvs: ${resolve_default:4096,${...num_envs}}
name: BallBalanceGPT
physics_engine: ${..physics_engine}
sim:
  dt: 0.01
  gravity:
  - 0.0
  - 0.0
  - -9.81
  physx:
    bounce_threshold_velocity: 0.2
    contact_collection: 0
    contact_offset: 0.02
    default_buffer_size_multiplier: 5.0
    max_depenetration_velocity: 1000.0
    max_gpu_contact_pairs: 8388608
    num_position_iterations: 8
    num_subscenes: ${....num_subscenes}
    num_threads: ${....num_threads}
    num_velocity_iterations: 0
    rest_offset: 0.001
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}}
  substeps: 1
  up_axis: z
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
task:
  randomize: false

```

### isaacgymenvs/isaacgymenvs/cfg/task/Cartpole.yaml

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

## Python signatures and reward/observation bodies (211 files)


### eureka/envs/bidex/shadow_hand_block_stack.py

```
class ShadowHandBlockStack(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_pose = self.root_state_tensor[self.block_indices, 0:7]
        self.block_pos = self.root_state_tensor[self.block_indices, 0:3]
        self.block_rot = self.root_state_tensor[self.block_indices, 3:7]
        self.block_linvel = self.root_state_tensor[self.block_indices, 7:10]
        self.block_angvel = self.root_state_tensor[self.block_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):

        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_s
```
```

### eureka/envs/bidex/shadow_hand_block_stack_obs.py

```
class ShadowHandBlockStack(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_pose = self.root_state_tensor[self.block_indices, 0:7]
        self.block_pos = self.root_state_tensor[self.block_indices, 0:3]
        self.block_rot = self.root_state_tensor[self.block_indices, 3:7]
        self.block_linvel = self.root_state_tensor[self.block_indices, 7:10]
        self.block_angvel = self.root_state_tensor[self.block_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos
```
```

### eureka/envs/bidex/shadow_hand_bottle_cap.py

```
class ShadowHandBottleCap(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_lf_pos = self.rigid_body_states[:, 20, 0:3]
        self.right_hand_lf_rot = self.rigid_body_states[:, 20, 3:7]
        self.right_hand_lf_pos = self.right_hand_lf_pos + quat_apply(self.right_hand_lf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_th_pos = self.rigid_body_states[:, 25, 0:3]
        self.right_hand_th_rot = self.rigid_body_states[:, 25, 3:7]
        self.right_hand_th_pos = self.right_hand_th_pos + quat_apply(self.right_hand_th_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)


        self.goal_pose = self.goal_states[:, 0:7]
        self.
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_bottle_cap_obs.py

```
class ShadowHandBottleCap(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_lf_pos = self.rigid_body_states[:, 20, 0:3]
        self.right_hand_lf_rot = self.rigid_body_states[:, 20, 3:7]
        self.right_hand_lf_pos = self.right_hand_lf_pos + quat_apply(self.right_hand_lf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_th_pos = self.rigid_body_states[:, 25, 0:3]
        self.right_hand_th_rot = self.rigid_body_states[:, 25, 3:7]
        self.right_hand_th_pos = self.right_hand_th_pos + quat_apply(self.right_hand_th_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)


        self.goal_pose = self.goal_states[:, 0:7]
        self.
```
```

### eureka/envs/bidex/shadow_hand_catch_abreast.py

```
class ShadowHandCatchAbreast(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, left_hand_pos, right_hand_pos, left_hand_base_pos, right_hand_base_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot, device)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.left_hand_pos, self.right_hand_pos,
            self.rigid_body_states[:, 3 + 26, 0:3], self.rigid_body_states[:, 3, 0:3],
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen"), self.device
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.hand_positions[self.hand_indices, :]
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.hand_positions[self.another_hand_indices, :]
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = 
```
```

### eureka/envs/bidex/shadow_hand_catch_abreast_obs.py

```
class ShadowHandCatchAbreast(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)
        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_catch_over2underarm.py

```
class ShadowHandCatchOver2Underarm(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, left_hand_base_pos, right_hand_base_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot, device)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.hand_positions[self.another_hand_indices, :], self.hand_positions[self.hand_indices, :], 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen"), self.device
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)
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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]

        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.hand_positions[self.hand_indices, :]
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.hand_positions[self.another_hand_indices, :]
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.obj
```
```

### eureka/envs/bidex/shadow_hand_catch_over2underarm_obs.py

```
class ShadowHandCatchOver2Underarm(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)
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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_catch_underarm.py

```
class ShadowHandCatchUnderarm(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):

        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):

        num_ft_states = 13 * int(self.num_fingertips / 2)
        num_ft_force_torques = 6 * int(self.num_fingertips / 2) 

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.hand_positions[self.hand_indices, :]
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.hand_positions[self.another_hand_indices, :]
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs
```
```

### eureka/envs/bidex/shadow_hand_catch_underarm_obs.py

```
class ShadowHandCatchUnderarm(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):

        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_door_close_inward.py

```
class ShadowHandDoorCloseInward(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)


        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).r
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):

        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_s
```
```

### eureka/envs/bidex/shadow_hand_door_close_inward_obs.py

```
class ShadowHandDoorCloseInward(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)


        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).r
```
```

### eureka/envs/bidex/shadow_hand_door_close_outward.py

```
class ShadowHandDoorCloseOutward(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_door_close_outward_obs.py

```
class ShadowHandDoorCloseOutward(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).
```
```

### eureka/envs/bidex/shadow_hand_door_open_inward.py

```
class ShadowHandDoorOpenInward(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).re
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_door_open_inward_obs.py

```
class ShadowHandDoorOpenInward(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).re
```
```

### eureka/envs/bidex/shadow_hand_door_open_outward.py

```
class ShadowHandDoorOpenOutward(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_door_open_outward_obs.py

```
class ShadowHandDoorOpenOutward(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.door_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.door_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.door_left_handle_pos = self.door_left_handle_pos + quat_apply(self.door_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.door_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.door_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.door_right_handle_pos = self.door_right_handle_pos + quat_apply(self.door_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).
```
```

### eureka/envs/bidex/shadow_hand_grasp_and_place.py

```
class ShadowHandGraspAndPlace(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=s
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_grasp_and_place_obs.py

```
class ShadowHandGraspAndPlace(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=s
```
```

### eureka/envs/bidex/shadow_hand_kettle.py

```
class ShadowHandKettle(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, kettle_handle_pos, bucket_handle_pos, kettle_spout_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):

        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.kettle_handle_pos, self.bucket_handle_pos, self.kettle_spout_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.kettle_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.kettle_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pos = self.rigid_body_states[:, 26 * 2, 0:3].clone()
        self.kettle_spout_rot = self.rigid_body_states[:, 26 * 2, 3:7].clone()
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.2)
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.07)

        self.bucket_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.bucket_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.1)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.rig
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):

        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_s
```
```

### eureka/envs/bidex/shadow_hand_kettle_obs.py

```
class ShadowHandKettle(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.kettle_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.kettle_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.kettle_handle_pos = self.kettle_handle_pos + quat_apply(self.kettle_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pos = self.rigid_body_states[:, 26 * 2, 0:3].clone()
        self.kettle_spout_rot = self.rigid_body_states[:, 26 * 2, 3:7].clone()
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.2)
        self.kettle_spout_pos = self.kettle_spout_pos + quat_apply(self.kettle_spout_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.07)

        self.bucket_handle_pos = self.rigid_body_states[:, 26 * 2 + 3, 0:3]
        self.bucket_handle_rot = self.rigid_body_states[:, 26 * 2 + 3, 3:7]
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.1)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.rig
```
```

### eureka/envs/bidex/shadow_hand_lift_underarm.py

```
class ShadowHandLiftUnderarm(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, pot_left_handle_pos, pot_right_handle_pos, left_hand_pos, right_hand_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pot_left_handle_pos, self.pot_right_handle_pos,
            self.left_hand_pos, self.right_hand_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)


        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.pot_right_handle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.pot_right_handle_pos = self.pot_right_handle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)
        self.pot_left_handle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.15)
        self.pot_left_handle_pos = self.pot_left_handle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_lift_underarm_obs.py

```
class ShadowHandLiftUnderarm(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)


        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.pot_right_handle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.pot_right_handle_pos = self.pot_right_handle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)
        self.pot_left_handle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.15)
        self.pot_left_handle_pos = self.pot_left_handle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_over.py

```
class ShadowHandOver(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]
        
        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]

        action_obs_start = fingertip_obs_start + 95
        self.obs_buf[:, action_obs_start:action_obs_start + 20] = self.actions[:, :20]

        another_hand_start = action_obs_start + 20
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        action_another_obs_start = fingertip_another_obs_start + 95
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 20] = self.actions[:, 20:]

        obj_obs_start = action_another_obs_start + 20  # 144
        if collect_demonstration:
            self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
            self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
            self.obs_buf[:, obj_obs_start + 10:obj_obs_start + 13] = self.vel_obs_scale * self.object_angvel

        goal_obs_start = obj_obs_start + 13  # 157 = 144 + 13
        self.obs_buf[:, goal_obs_start:goal_obs_start + 7] = self.goal_pose
        self.obs_buf[:, goal_obs_start + 7:goal_obs_start + 11] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

        point_clouds = torch.zeros((self.num_envs, self.pointCloudDownsampleNum, 3), device=self.device)
        
        if self.camera_debug:
            import matplotlib.pyplot as plt
            self.camera_rgba_debug_fig = plt.figure("CAMERA_RGBD_DEBUG")
            camera_rgba_image = self.camera_visulization(is_depth_image=False)

        for i in range(self.num_envs):
            points = depth_image_to_point_cloud_GPU(self.camera_tensors[i], self.camera_view_matrixs[i], self.camera_proj_matrixs[i], self.camera_u2, self.camera_v2, self.camera_props.width, self.camera_props.height, 10, self.device)
            
            if points.shape[0] > 0:
                selected_points = self.sample_points(points, sample_num=self.pointCloudDownsampleNum, sample_mathed='random')
            else:
                selected
```
```

### eureka/envs/bidex/shadow_hand_over_obs.py

```
class ShadowHandOver(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]
        
        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_pen.py

```
class ShadowHandPen(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, pen_right_handle_pos, pen_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pen_right_handle_pos, self.pen_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.pen_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.pen_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.1)
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.pen_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.pen_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.07)
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_pen_obs.py

```
class ShadowHandPen(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.pen_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.pen_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.1)
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.pen_right_handle_pos = self.pen_right_handle_pos + quat_apply(self.pen_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.pen_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.pen_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.07)
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.pen_left_handle_pos = self.pen_left_handle_pos + quat_apply(self.pen_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.
```
```

### eureka/envs/bidex/shadow_hand_push_block.py

```
class ShadowHandPushBlock(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, left_target_pos, left_target_rot, right_target_pos, right_target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.left_goal_pos, self.left_goal_rot, self.left_goal_pos, self.left_goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.devi
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_push_block_obs.py

```
class ShadowHandPushBlock(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.devi
```
```

### eureka/envs/bidex/shadow_hand_re_orientation.py

```
class ShadowHandReOrientation(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.object_another_pose = self.root_state_tensor[self.object_another_indices, 0:7]
        self.object_another_pos = self.root_state_tensor[self.object_another_indices, 0:3]
        self.object_another_rot = self.root_state_tensor[self.object_another_indices, 3:7]
        self.object_another_linvel = self.root_state_tensor[self.object_another_indices, 7:10]
        self.object_another_angvel = self.root_state_tensor[self.object_another_indices, 10:13]

        self.goal_another_pose = self.goal_another_states[:, 0:7]
        self.goal_another_pos = self.goal_another_states[:, 0:3]
        self.goal_another_rot = self.goal_another_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]

        action_obs_start = fingertip_obs_start + 95
        self.obs_buf[:, action_obs_start:action_obs_start + 20] = self.actions[:, :20]

        another_hand_start = action_obs_start + 20
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        action_another_obs_start = fingertip_another_obs_start + 95
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 20] = self.actions[:, 20:]

        obj_obs_start = action_another_obs_start + 20  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_start + 10:obj_obs_start + 13] = self.vel_obs_scale * self.object_angvel

        goal_obs_start = obj_obs_start + 13  # 157 = 144 + 13
        self.obs_buf[:, goal_obs_start:goal_obs_start + 7] = self.goal_pose
        self.obs_buf[:, goal_obs_start + 7:goal_obs_start + 11] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

        another_obj_obs_start = goal_obs_start + 11  # 144
        self.obs_buf[:, another_obj_obs_start:another_obj_obs_start + 7] = self.object_another_pose
        self.obs_buf[:, another_obj_obs_start + 7:another_obj_obs_start + 10] = self.object_another_linvel
        self.obs_buf[:, another_obj_obs_start + 10:another_obj_obs_start + 13] = self.vel_obs_scale * self.object_another_angvel

        another_goal_obs_start = another_obj_obs_start + 13  # 157 = 144 + 13
        self.obs_buf[:, another_goal_obs_start:another_goal_obs_start + 7] = self.goal_another_pose
        self.obs_buf[:, another_goal_obs_start + 7:another_goal_obs_start + 11] = quat_mul(self.object_another_rot, quat_conjugate(self.goal_another_rot))
        point_clouds = torch.zeros((self.num_envs, self.pointCloudDownsampleNum, 3), device=self.device)
        
        if self.camera_debug:
    
```
```

### eureka/envs/bidex/shadow_hand_re_orientation_obs.py

```
class ShadowHandReOrientation(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.object_another_pose = self.root_state_tensor[self.object_another_indices, 0:7]
        self.object_another_pos = self.root_state_tensor[self.object_another_indices, 0:3]
        self.object_another_rot = self.root_state_tensor[self.object_another_indices, 3:7]
        self.object_another_linvel = self.root_state_tensor[self.object_another_indices, 7:10]
        self.object_another_angvel = self.root_state_tensor[self.object_another_indices, 10:13]

        self.goal_another_pose = self.goal_another_states[:, 0:7]
        self.goal_another_pos = self.goal_another_states[:, 0:3]
        self.goal_another_rot = self.goal_another_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_scissors.py

```
class ShadowHandScissors(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, scissors_right_handle_pos, scissors_left_handle_pos, object_dof_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.scissors_right_handle_pos, self.scissors_left_handle_pos, self.object_dof_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.scissors_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.scissors_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.)
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.2)
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.1)

        self.scissors_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.scissors_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_scissors_obs.py

```
class ShadowHandScissors(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.scissors_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.scissors_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.)
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.2)
        self.scissors_right_handle_pos = self.scissors_right_handle_pos + quat_apply(self.scissors_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.1)

        self.scissors_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.scissors_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.scissors_left_handle_pos = self.scissors_left_handle_pos + quat_apply(self.scissors_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_
```
```

### eureka/envs/bidex/shadow_hand_swing_cup.py

```
class ShadowHandSwingCup(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, cup_right_handle_pos, cup_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.cup_right_handle_pos, self.cup_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.cup_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3].clone()
        self.cup_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7].clone()
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.062)
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0)

        self.cup_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3].clone()
        self.cup_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7].clone()
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_swing_cup_obs.py

```
class ShadowHandSwingCup(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):

        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)


        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.cup_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3].clone()
        self.cup_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7].clone()
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.062)
        self.cup_right_handle_pos = self.cup_right_handle_pos + quat_apply(self.cup_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0)

        self.cup_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3].clone()
        self.cup_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7].clone()
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0)
        self.cup_left_handle_pos = self.cup_left_handle_pos + quat_apply(self.cup_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.06)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(sel
```
```

### eureka/envs/bidex/shadow_hand_switch.py

```
class ShadowHandSwitch(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, switch_right_handle_pos, switch_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.switch_right_handle_pos, self.switch_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.switch_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.switch_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.05)
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.switch_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 5, 0:3]
        self.switch_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 5, 3:7]
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.05)
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_ro
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]
        
        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.right_hand_pos
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.left_hand_pos
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.object_linvel
        self.obs_buf[:, obj_obs_st
```
```

### eureka/envs/bidex/shadow_hand_switch_obs.py

```
class ShadowHandSwitch(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.switch_right_handle_pos = self.rigid_body_states[:, 26 * 2 + 2, 0:3]
        self.switch_right_handle_rot = self.rigid_body_states[:, 26 * 2 + 2, 3:7]
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.05)
        self.switch_right_handle_pos = self.switch_right_handle_pos + quat_apply(self.switch_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.switch_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 5, 0:3]
        self.switch_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 5, 3:7]
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.05)
        self.switch_left_handle_pos = self.switch_left_handle_pos + quat_apply(self.switch_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_ro
```
```

### eureka/envs/bidex/shadow_hand_two_ball_juggle.py

```
class ShadowHandTwoBallJuggle(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object1_pose = self.root_state_tensor[self.object1_indices, 0:7]
        self.object1_pos = self.root_state_tensor[self.object1_indices, 0:3]
        self.object1_rot = self.root_state_tensor[self.object1_indices, 3:7]
        self.object1_linvel = self.root_state_tensor[self.object1_indices, 7:10]
        self.object1_angvel = self.root_state_tensor[self.object1_indices, 10:13]

        self.object2_pose = self.root_state_tensor[self.object2_indices, 0:7]
        self.object2_pos = self.root_state_tensor[self.object2_indices, 0:3]
        self.object2_rot = self.root_state_tensor[self.object2_indices, 3:7]
        self.object2_linvel = self.root_state_tensor[self.object2_indices, 7:10]
        self.object2_angvel = self.root_state_tensor[self.object2_indices, 10:13]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]

        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.hand_positions[self.hand_indices, :]
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.hand_positions[self.another_hand_indices, :]
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj1_obs_start = action_another_obs_start + 26
        self.obs_buf[:, obj1_obs_start:obj1_obs_start + 7] = self.object1_pose
        self.obs_buf[:, obj1_obs_start + 7:obj1_obs_start + 10] = self.obje
```
```

### eureka/envs/bidex/shadow_hand_two_ball_juggle_obs.py

```
class ShadowHandTwoBallJuggle(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object1_pose = self.root_state_tensor[self.object1_indices, 0:7]
        self.object1_pos = self.root_state_tensor[self.object1_indices, 0:3]
        self.object1_rot = self.root_state_tensor[self.object1_indices, 3:7]
        self.object1_linvel = self.root_state_tensor[self.object1_indices, 7:10]
        self.object1_angvel = self.root_state_tensor[self.object1_indices, 10:13]

        self.object2_pose = self.root_state_tensor[self.object2_indices, 0:7]
        self.object2_pos = self.root_state_tensor[self.object2_indices, 0:3]
        self.object2_rot = self.root_state_tensor[self.object2_indices, 3:7]
        self.object2_linvel = self.root_state_tensor[self.object2_indices, 7:10]
        self.object2_angvel = self.root_state_tensor[self.object2_indices, 10:13]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/bidex/shadow_hand_two_catch_underarm.py

```
class ShadowHandTwoCatchUnderarm(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset_idx(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.object_another_pose = self.root_state_tensor[self.object_another_indices, 0:7]
        self.object_another_pos = self.root_state_tensor[self.object_another_indices, 0:3]
        self.object_another_rot = self.root_state_tensor[self.object_another_indices, 3:7]
        self.object_another_linvel = self.root_state_tensor[self.object_another_indices, 7:10]
        self.object_another_angvel = self.root_state_tensor[self.object_another_indices, 10:13]

        self.goal_another_pose = self.goal_another_states[:, 0:7]
        self.goal_another_pos = self.goal_another_states[:, 0:3]
        self.goal_another_rot = self.goal_another_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```

```python
def compute_point_cloud_observation(self, collect_demonstration=False):
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs:2*self.num_shadow_hand_dofs] = self.vel_obs_scale * self.shadow_hand_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs:3*self.num_shadow_hand_dofs] = self.force_torque_obs_scale * self.dof_force_tensor[:, :24]

        fingertip_obs_start = 72  # 168 = 157 + 11
        self.obs_buf[:, fingertip_obs_start:fingertip_obs_start + num_ft_states] = self.fingertip_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_obs_start + num_ft_states:fingertip_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, :30]

        hand_pose_start = fingertip_obs_start + 95
        self.obs_buf[:, hand_pose_start:hand_pose_start + 3] = self.hand_positions[self.hand_indices, :]
        self.obs_buf[:, hand_pose_start+3:hand_pose_start+4] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+4:hand_pose_start+5] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_pose_start+5:hand_pose_start+6] = get_euler_xyz(self.hand_orientations[self.hand_indices, :])[2].unsqueeze(-1)

        action_obs_start = hand_pose_start + 6
        self.obs_buf[:, action_obs_start:action_obs_start + 26] = self.actions[:, :26]

        another_hand_start = action_obs_start + 26
        self.obs_buf[:, another_hand_start:self.num_shadow_hand_dofs + another_hand_start] = unscale(self.shadow_hand_another_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_dof_upper_limits)
        self.obs_buf[:, self.num_shadow_hand_dofs + another_hand_start:2*self.num_shadow_hand_dofs + another_hand_start] = self.vel_obs_scale * self.shadow_hand_another_dof_vel
        self.obs_buf[:, 2*self.num_shadow_hand_dofs + another_hand_start:3*self.num_shadow_hand_dofs + another_hand_start] = self.force_torque_obs_scale * self.dof_force_tensor[:, 24:48]

        fingertip_another_obs_start = another_hand_start + 72
        self.obs_buf[:, fingertip_another_obs_start:fingertip_another_obs_start + num_ft_states] = self.fingertip_another_state.reshape(self.num_envs, num_ft_states)
        self.obs_buf[:, fingertip_another_obs_start + num_ft_states:fingertip_another_obs_start + num_ft_states +
                    num_ft_force_torques] = self.force_torque_obs_scale * self.vec_sensor_tensor[:, 30:]

        hand_another_pose_start = fingertip_another_obs_start + 95
        self.obs_buf[:, hand_another_pose_start:hand_another_pose_start + 3] = self.hand_positions[self.another_hand_indices, :]
        self.obs_buf[:, hand_another_pose_start+3:hand_another_pose_start+4] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[0].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+4:hand_another_pose_start+5] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[1].unsqueeze(-1)
        self.obs_buf[:, hand_another_pose_start+5:hand_another_pose_start+6] = get_euler_xyz(self.hand_orientations[self.another_hand_indices, :])[2].unsqueeze(-1)

        action_another_obs_start = hand_another_pose_start + 6
        self.obs_buf[:, action_another_obs_start:action_another_obs_start + 26] = self.actions[:, 26:]

        obj_obs_start = action_another_obs_start + 26  # 144
        self.obs_buf[:, obj_obs_start:obj_obs_start + 7] = self.object_pose
        self.obs_buf[:, obj_obs_start + 7:obj_obs_start + 10] = self.obj
```
```

### eureka/envs/bidex/shadow_hand_two_catch_underarm_obs.py

```
class ShadowHandTwoCatchUnderarm(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        self.object_another_pose = self.root_state_tensor[self.object_another_indices, 0:7]
        self.object_another_pos = self.root_state_tensor[self.object_another_indices, 0:3]
        self.object_another_rot = self.root_state_tensor[self.object_another_indices, 3:7]
        self.object_another_linvel = self.root_state_tensor[self.object_another_indices, 7:10]
        self.object_another_angvel = self.root_state_tensor[self.object_another_indices, 10:13]

        self.goal_another_pose = self.goal_another_states[:, 0:7]
        self.goal_another_pos = self.goal_another_states[:, 0:3]
        self.goal_another_rot = self.goal_another_states[:, 3:7]

        self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        if self.obs_type == "full_state":
            self.compute_full_state()
        elif self.obs_type == "point_cloud":
            self.compute_point_cloud_observation()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### eureka/envs/isaac/allegro_hand.py

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
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def compute_bonus(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.rew_buf[:] = compute_bonus(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

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

            self.obs_buf[:, 32:39] = self.object_pose
            self.obs_buf[:, 39:42] = self.object_linvel
            self.obs_buf[:, 42:45] = self.vel_obs_scale * self.object_angvel

            self.obs_buf[:, 45:52] = self.goal_pose
            self.obs_buf[:, 52:56] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))


            self.obs_buf[:, 56:72] = self.actions
```
```

### eureka/envs/isaac/allegro_hand_obs.py

```
class AllegroHand(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)

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
```

### eureka/envs/isaac/ant.py

```
class Ant(VecTask)
    def __init__(self, cfg, rl_device, sim_device, graphics_device_id, headless, virtual_screen_capture, force_render)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def reset_idx(self, env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_ant_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, basis_vec0, basis_vec1, up_axis_idx)
def compute_success(obs_buf, reset_buf, consecutive_successes, progress_buf, actions, up_weight, heading_weight, potentials, prev_potentials, actions_cost_scale, energy_cost_scale, joints_at_limit_cost_scale, termination_height, death_cost, max_episode_length)

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

    obs = torch.cat((torso_position[:, up_axis_idx].view(-1, 1), vel_loc, angvel_loc,
                     yaw.unsqueeze(-1), roll.unsqueeze(-1), angle_to_target.unsqueeze(-1),
                     up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1), dof_pos_scaled,
                     dof_vel * dof_vel_scale, sensor_force_torques.view(-1, 24) * contact_force_scale,
                     actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
```

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.consecutive_successes[:] = compute_success(
            self.obs_buf,
            self.reset_buf,
            self.consecutive_successes,
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
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
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

### eureka/envs/isaac/ant_obs.py

```
class Ant(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
def compute_ant_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, basis_vec0, basis_vec1, up_axis_idx)

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

    obs = torch.cat((torso_position[:, up_axis_idx].view(-1, 1), vel_loc, angvel_loc,
                     yaw.unsqueeze(-1), roll.unsqueeze(-1), angle_to_target.unsqueeze(-1),
                     up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1), dof_pos_scaled,
                     dof_vel * dof_vel_scale, sensor_force_torques.view(-1, 24) * contact_force_scale,
                     actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
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

### eureka/envs/isaac/anymal.py

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
def compute_anymal_observations(root_states, commands, dof_pos, default_dof_pos, dof_vel, gravity_vec, actions, lin_vel_scale, ang_vel_scale, dof_pos_scale, dof_vel_scale)
def compute_success(root_states, commands, torques, contact_forces, knee_indices, consecutive_successes, episode_lengths, rew_scales, base_index, max_episode_length)

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
        self.gt_rew_buf, self.reset_buf[:], self.consecutive_successes[:] = compute_success(
            self.root_states,
            self.commands,
            self.torques,
            self.contact_forces,
            self.knee_indices,
            self.consecutive_successes,
            self.progress_buf,
            self.rew_scales,
            self.base_index,
            self.max_episode_length,
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
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
                                                        self.lin_vel_scale,
                                                        self.ang_vel_scale,
                                                        self.dof_pos_scale,
                                                        self.dof_vel_scale
        )
```
```

### eureka/envs/isaac/anymal_obs.py

```
class Anymal(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
def compute_anymal_observations(root_states, commands, dof_pos, default_dof_pos, dof_vel, gravity_vec, actions, lin_vel_scale, ang_vel_scale, dof_pos_scale, dof_vel_scale)

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
                                                        self.lin_vel_scale,
                                                        self.ang_vel_scale,
                                                        self.dof_pos_scale,
                                                        self.dof_vel_scale
        )
```
```

### eureka/envs/isaac/ball_balance.py

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
def compute_success(tray_positions, ball_positions, ball_velocities, ball_radius, reset_buf, consecutive_successes, progress_buf, max_episode_length)

```python
def compute_observations(self):

        actuated_dof_indices = torch.tensor([1, 3, 5], device=self.device)

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
        self.gt_rew_buf, self.reset_buf[:], self.consecutive_successes[:] = compute_success(
            self.tray_positions,
            self.ball_positions,
            self.ball_linvels,
            self.ball_radius,
            self.reset_buf, self.consecutive_successes, 
            self.progress_buf, self.max_episode_length
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
```
```

### eureka/envs/isaac/ball_balance_obs.py

```
class BallBalance(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

```python
def compute_observations(self):

        actuated_dof_indices = torch.tensor([1, 3, 5], device=self.device)

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
```

### eureka/envs/isaac/cartpole.py

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
def compute_success(pole_angle, pole_vel, cart_vel, cart_pos, reset_dist, reset_buf, consecutive_successes, progress_buf, max_episode_length)

```python
def compute_reward(self):
        pole_angle = self.obs_buf[:, 2]
        pole_vel = self.obs_buf[:, 3]
        cart_vel = self.obs_buf[:, 1]
        cart_pos = self.obs_buf[:, 0]

        self.gt_rew_buf, self.reset_buf[:], self.consecutive_successes[:] = compute_success(
            pole_angle, pole_vel, cart_vel, cart_pos,
            self.reset_dist, self.reset_buf, self.consecutive_successes, self.progress_buf, self.max_episode_length
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
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

### eureka/envs/isaac/cartpole_obs.py

```
class Cartpole(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self, env_ids)

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

### eureka/envs/isaac/franka_cabinet.py

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
def compute_grasp_transforms(hand_rot, hand_pos, franka_local_grasp_rot, franka_local_grasp_pos, drawer_rot, drawer_pos, drawer_local_grasp_rot, drawer_local_grasp_pos)
def compute_success(reset_buf, progress_buf, successes, consecutive_successes, actions, cabinet_dof_pos, franka_grasp_pos, drawer_grasp_pos, franka_grasp_rot, drawer_grasp_rot, franka_lfinger_pos, franka_rfinger_pos, gripper_forward_axis, drawer_inward_axis, gripper_up_axis, drawer_up_axis, num_envs, dist_reward_scale, rot_reward_scale, around_handle_reward_scale, open_reward_scale, finger_dist_reward_scale, action_penalty_scale, distX_offset, max_episode_length)

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.reset_buf, self.progress_buf, self.successes, self.consecutive_successes, self.actions, self.cabinet_dof_pos,
            self.franka_grasp_pos, self.drawer_grasp_pos, self.franka_grasp_rot, self.drawer_grasp_rot,
            self.franka_lfinger_pos, self.franka_rfinger_pos,
            self.gripper_forward_axis, self.drawer_inward_axis, self.gripper_up_axis, self.drawer_up_axis,
            self.num_envs, self.dist_reward_scale, self.rot_reward_scale, self.around_handle_reward_scale, self.open_reward_scale,
            self.finger_dist_reward_scale, self.action_penalty_scale, self.distX_offset, self.max_episode_length
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
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

### eureka/envs/isaac/franka_cabinet_obs.py

```
class FrankaCabinet(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

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

### eureka/envs/isaac/humanoid.py

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
def compute_humanoid_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_force, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, angular_velocity_scale, basis_vec0, basis_vec1)
def compute_success(obs_buf, reset_buf, consecutive_successes, progress_buf, actions, up_weight, heading_weight, potentials, prev_potentials, actions_cost_scale, energy_cost_scale, joints_at_limit_cost_scale, max_motor_effort, motor_efforts, termination_height, death_cost, max_episode_length)

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

    obs = torch.cat((torso_position[:, 2].view(-1, 1), vel_loc, angvel_loc * angular_velocity_scale,
                     yaw, roll, angle_to_target, up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1),
                     dof_pos_scaled, dof_vel * dof_vel_scale, dof_force * contact_force_scale,
                     sensor_force_torques.view(-1, 12) * contact_force_scale, actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
```

```python
def compute_reward(self, actions):
        self.gt_rew_buf, self.reset_buf, self.consecutive_successes[:] = compute_success(
            self.obs_buf,
            self.reset_buf,
            self.consecutive_successes,
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
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
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

### eureka/envs/isaac/humanoid_obs.py

```
class Humanoid(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
def compute_humanoid_observations(obs_buf, root_states, targets, potentials, inv_start_rot, dof_pos, dof_vel, dof_force, dof_limits_lower, dof_limits_upper, dof_vel_scale, sensor_force_torques, actions, dt, contact_force_scale, angular_velocity_scale, basis_vec0, basis_vec1)

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

    obs = torch.cat((torso_position[:, 2].view(-1, 1), vel_loc, angvel_loc * angular_velocity_scale,
                     yaw, roll, angle_to_target, up_proj.unsqueeze(-1), heading_proj.unsqueeze(-1),
                     dof_pos_scaled, dof_vel * dof_vel_scale, dof_force * contact_force_scale,
                     sensor_force_torques.view(-1, 12) * contact_force_scale, actions), dim=-1)

    return obs, potentials, prev_potentials_new, up_vec, heading_vec
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

### eureka/envs/isaac/quadcopter.py

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
def compute_success(root_positions, root_quats, root_linvels, root_angvels, reset_buf, consecutive_successes, progress_buf, max_episode_length)

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
        self.gt_rew_buf, self.reset_buf[:], self.consecutive_successes[:] = compute_success(
            self.root_positions,
            self.root_quats,
            self.root_linvels,
            self.root_angvels,
            self.reset_buf, self.consecutive_successes, self.progress_buf, self.max_episode_length
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()
```
```

### eureka/envs/isaac/quadcopter_obs.py

```
class Quadcopter(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)

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
```

### eureka/envs/isaac/shadow_hand.py

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
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def compute_bonus(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.rew_buf[:] = compute_bonus(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

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

            self.obs_buf[:, 0:15] = self.fingertip_pos.reshape(self.num_envs, 15)
            self.obs_buf[:, 15:18] = self.object_pose[:, 0:3]
            self.obs_buf[:, 18:22] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 22:42] = self.actions
        else:
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

            self.obs_buf[:, 72:137] = self.fingertip_state.reshape(self.num_envs, 65)

            self.obs_buf[:, 137:157] = self.actions
```
```

### eureka/envs/isaac/shadow_hand_obs.py

```
class ShadowHand(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)

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
```

### eureka/envs/isaac/shadow_hand_spin.py

```
class ShadowHandSpin(VecTask)
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
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_bonus(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.rew_buf[:] = compute_bonus(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        
        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

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

            self.obs_buf[:, 0:15] = self.fingertip_pos.reshape(self.num_envs, 15)
            self.obs_buf[:, 15:18] = self.object_pose[:, 0:3]
            self.obs_buf[:, 18:22] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 22:42] = self.actions
        else:
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

            self.obs_buf[:, 72:137] = self.fingertip_state.reshape(self.num_envs, 65)

            self.obs_buf[:, 137:157] = self.actions
```
```

### eureka/envs/isaac/shadow_hand_spin_obs.py

```
class ShadowHandSpin(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)

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
```

### eureka/envs/isaac/shadow_hand_upside_down.py

```
class ShadowHandUpsideDown(VecTask)
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
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_bonus(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def compute_success(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

```python
def compute_reward(self, actions):
        self.rew_buf[:] = compute_bonus(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.gt_rew_buf, self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_success(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        self.extras['gt_reward'] = self.gt_rew_buf.mean()
        self.extras['consecutive_successes'] = self.consecutive_successes.mean()

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

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

            self.obs_buf[:, 0:15] = self.fingertip_pos.reshape(self.num_envs, 15)
            self.obs_buf[:, 15:18] = self.object_pose[:, 0:3]
            self.obs_buf[:, 18:22] = quat_mul(self.object_rot, quat_conjugate(self.goal_rot))

            self.obs_buf[:, 22:42] = self.actions
        else:
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

            self.obs_buf[:, 72:137] = self.fingertip_state.reshape(self.num_envs, 65)

            self.obs_buf[:, 137:157] = self.actions
```
```

### eureka/envs/isaac/shadow_hand_upside_down_obs.py

```
class ShadowHandUpsideDown(VecTask)
    """Rest of the environment definition omitted."""
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)

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
```

### eureka/utils/create_task.py

```
def create_task(root_dir, task, env_name, suffix)
```

### eureka/utils/extract_task_code.py

```
def file_to_string(filename)
def extract_task_code(filename)
def extract_observation_code(filename)
def extract_observation_functions(filename, task)
def get_function_signature(code_string)

```python
def extract_observation_code(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    function_code = ''
    function_started = False

    for line in lines:
        if re.match(r'def .+observations.+\(.*\):', line):
            function_started = True
            print(line)
        if function_started:
            function_code += line

            if line.strip() == '':
                function_started = False

    return function_code
```

```python
def extract_observation_functions(filename, task='ant'):
    with open(filename, 'r') as f:
        lines = f.readlines()

    functions = []
    function_lines = []
    indent = 0

    for line in lines:
        stripped_line = line.lstrip()
        current_indent = len(line) - len(stripped_line)

        if current_indent < indent:  # if the indent decreases, we've left the function
            if function_lines:  # if there are lines saved, we save the function
                functions.append(''.join(function_lines))
                function_lines = []  # clear function lines

        if re.match(r'def .+ant_observations.+\(.*\):', stripped_line):
            indent = current_indent
            function_lines.append(line)  # save function line
        elif function_lines:  # if we're in the function, save lines
            function_lines.append(line)

    # handle case where the file ends but we're still in a function
    if function_lines:
        functions.append(''.join(function_lines))

    return '\n'.join(functions)
```
```

### eureka/utils/prune_env.py

```
def modify_python_file(task, filename, output)
def prune_python_class(filename, output, methods_to_keep, new_docstring, methods_to_prune_docstring)
def prune_reward(filename, output, method_to_keep)
def extract_class_info(file_path)
def create_yaml(file_path, yaml_path)

```python
def prune_reward(filename, output, method_to_keep):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove methods not in methods_to_keep
    pruned_lines = []
    inside_method_to_keep = False
    seen_jit = False
    prev_line = None
    for line in lines:
        stripped = line.strip()
        if method_to_keep in line:
            if "@torch.jit.script" in prev_line:
                pruned_lines.append(prev_line)
                pruned_lines.append(line)
                inside_method_to_keep = True
                continue
        else: 
            if inside_method_to_keep == True:
                if stripped == '"""':
                    break
                pruned_lines.append(line)
                if stripped == '"""':
                    break
        prev_line = line

    # Write the pruned lines back to the file
    with open(output, 'w') as file:
        file.writelines(pruned_lines)
```
```

### eureka/utils/prune_env_dexterity.py

```
def modify_python_file(filename, output)
def prune_python_class(filename, output, methods_to_keep, new_docstring, methods_to_prune_docstring)
def prune_reward(filename, output, method_to_keep)
def extract_class_info(file_path)
def create_yaml(file_path, yaml_path)

```python
def prune_reward(filename, output, method_to_keep):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove methods not in methods_to_keep
    pruned_lines = []
    inside_method_to_keep = False
    seen_jit = False
    prev_line = None
    for line in lines:
        stripped = line.strip()
        if method_to_keep in line:
            if "@torch.jit.script" in prev_line:
                pruned_lines.append(prev_line)
                pruned_lines.append(line)
                inside_method_to_keep = True
                continue
        else: 
            if inside_method_to_keep == True:
                if stripped == '"""':
                    break
                pruned_lines.append(line)
                if stripped == '"""':
                    break
        prev_line = line

    # Write the pruned lines back to the file
    with open(output, 'w') as file:
        file.writelines(pruned_lines)
```
```

### eureka/utils/prune_env_isaac.py

```
def modify_python_file(task, filename, output)
def prune_python_class(filename, output, methods_to_keep, new_docstring, methods_to_prune_docstring)
def prune_reward(filename, output, method_to_keep)
def extract_class_info(file_path)
def create_yaml(file_path, yaml_path)

```python
def prune_reward(filename, output, method_to_keep):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove methods not in methods_to_keep
    pruned_lines = []
    inside_method_to_keep = False
    seen_jit = False
    prev_line = None
    for line in lines:
        stripped = line.strip()
        if method_to_keep in line:
            if "@torch.jit.script" in prev_line:
                pruned_lines.append(prev_line)
                pruned_lines.append(line)
                inside_method_to_keep = True
                continue
        else: 
            if inside_method_to_keep == True:
                if stripped == '"""':
                    break
                pruned_lines.append(line)
                if stripped == '"""':
                    break
        prev_line = line

    # Write the pruned lines back to the file
    with open(output, 'w') as file:
        file.writelines(pruned_lines)
```
```

### isaacgymenvs/isaacgymenvs/__init__.py

```
def make(seed, task, num_envs, sim_device, rl_device, graphics_device_id, headless, multi_gpu, virtual_screen_capture, force_render, cfg)
```

### isaacgymenvs/isaacgymenvs/learning/amp_continuous.py

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

### isaacgymenvs/isaacgymenvs/learning/amp_datasets.py

```
class AMPDataset(PPODataset)
    def __init__(self, batch_size, minibatch_size, is_discrete, is_rnn, device, seq_len)
    def update_mu_sigma(self, mu, sigma)
    def _get_item(self, idx)
    def _shuffle_idx_buf(self)
```

### isaacgymenvs/isaacgymenvs/learning/amp_models.py

```
class ModelAMPContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/isaacgymenvs/learning/amp_network_builder.py

```
class AMPBuilder(A2CBuilder)
    def __init__(self)
    def build(self, name)
```

### isaacgymenvs/isaacgymenvs/learning/amp_players.py

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

### isaacgymenvs/isaacgymenvs/learning/common_agent.py

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

### isaacgymenvs/isaacgymenvs/learning/common_player.py

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

### isaacgymenvs/isaacgymenvs/learning/hrl_continuous.py

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

### isaacgymenvs/isaacgymenvs/learning/hrl_models.py

```
class ModelHRLContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/isaacgymenvs/learning/replay_buffer.py

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

### isaacgymenvs/isaacgymenvs/tasks/allegro_hand.py

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
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)

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

    # reward = cons_successes
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

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]

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

            # 3*self.num_fingertips = 15
            #self.obs_buf[:, 42:57] = self.fingertip_pos.reshape(self.num_envs, 15)

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

            # 13*self.num_fingertips = 65 4*13 = 52
            # self.obs_buf[:, 72:137] = self.fingertip_state.reshape(self.num_envs, 65)

            self.obs_buf[:, 56:72] = self.actions
```
```

### isaacgymenvs/isaacgymenvs/tasks/amp/humanoid_amp_base.py

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
    def render(self, mode)
    def _build_key_body_ids_tensor(self, env_ptr, actor_handle)
    def _build_contact_body_ids_tensor(self, env_ptr, actor_handle)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
def dof_to_obs(pose)
def compute_humanoid_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, max_episode_length, enable_early_termination, termination_height)
def compute_humanoid_reward(obs_buf)

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

### isaacgymenvs/isaacgymenvs/tasks/amp/humanoid_amp_basegpt.py

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
    def render(self, mode)
    def _build_key_body_ids_tensor(self, env_ptr, actor_handle)
    def _build_contact_body_ids_tensor(self, env_ptr, actor_handle)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
def dof_to_obs(pose)
def compute_humanoid_observations(root_states, dof_pos, dof_vel, key_body_pos, local_root_obs)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, max_episode_length, enable_early_termination, termination_height)
def compute_humanoid_reward(obs_buf)

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
    root_h = obs_buf[:, 0]
    root_rot_obs = obs_buf[:, 1:5]
    local_root_vel = obs_buf[:, 5:8]
    local_root_ang_vel = obs_buf[:, 8:11]
    dof_obs = obs_buf[:, 11:63]
    dof_vel = obs_buf[:, 63:115]
    flat_local_key_pos = obs_buf[:, 115:]
    # Encourage low root height
    height_reward = -torch.abs(root_h - 0.5)

    # Encourage diverse joint movements
    joint_vel_reward = torch.sum(torch.abs(dof_vel), dim=-1)

    # Penalize large angular velocities of the root to maintain balance
    balance_penalty = -torch.sum(torch.abs(local_root_ang_vel), dim=-1)

    # Combine the rewards and penalties
    reward = height_reward + joint_vel_reward + balance_penalty

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

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/core/backend/abstract.py

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

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/core/rotation3d.py

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

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/core/tensor_utils.py

```
class TensorUtils(Serializable)
    def from_dict(cls, dict_repr)
    def to_dict(self)
def tensor_to_dict(x)
```

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/skeleton/backend/fbx/fbx_backend.py

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

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/skeleton/backend/fbx/fbx_read_wrapper.py

```
"""Script that reads in fbx files from python

This requires a configs file, which contains the command necessary to switch conda
environments to run the fbx reading script from python"""
def fbx_to_array(fbx_file_path, root_joint, fps)
```

### isaacgymenvs/isaacgymenvs/tasks/amp/poselib/poselib/skeleton/skeleton3d.py

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