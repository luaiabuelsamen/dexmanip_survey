# dreureka_2024

source: https://github.com/eureka-research/DrEureka


commit: 1d4e00700423170717654516f4ef4b24cb0f3a84


## README

# DrEureka: Language Model Guided Sim-to-Real Transfer

<div align="center">

[[Website]](https://eureka-research.github.io/dr-eureka/)
[[arXiv]](https://arxiv.org/abs/2406.01967)
[[PDF]](https://eureka-research.github.io/dr-eureka/assets/dreureka-paper.pdf)

[Yecheng Jason Ma<sup>1*</sup>](https://jasonma2016.github.io/), [William Liang<sup>1*</sup>](https://willjhliang.github.io), [Hung-Ju Wang<sup>1</sup>](https://www.linkedin.com/in/hungju-wang), [Sam Wang<sup>1</sup>](https://www.linkedin.com/in/sam-wang-penn),<br>
[Yuke Zhu<sup>2,3</sup>](https://www.cs.utexas.edu/~yukez/), [Linxi "Jim" Fan<sup>2</sup>](https://jimfan.me/), [Osbert Bastani<sup>1</sup>](https://obastani.github.io/), [Dinesh Jayaraman<sup>1</sup>](https://www.seas.upenn.edu/~dineshj/)

<sup>1</sup>University of Pennsylvania, <sup>2</sup>NVIDIA, <sup>3</sup>University of Texas, Austin

<sup>*</sup>Equal Contribution

[![Python Version](https://img.shields.io/badge/Python-3.8-blue.svg)](https://github.com/eureka-research/Eureka)
[<img src="https://img.shields.io/badge/Framework-PyTorch-red.svg"/>](https://pytorch.org/)
[![GitHub license](https://img.shields.io/github/license/eureka-research/Eureka)](https://github.com/eureka-research/Eureka/blob/main/LICENSE)
______________________________________________________________________



https://github.com/eureka-research/DrEureka/assets/21993118/d0fd772c-bfbd-4796-8f89-b0553ffb7b80


https://github.com/eureka-research/DrEureka/assets/21993118/0a9825b2-101b-4fb9-878d-4563c6a14090

</div>

Transferring policies learned in simulation to the real world is a promising strategy for acquiring robot skills at scale. However, sim-to-real approaches typically rely on manual design and tuning of the task reward function as well as the simulation physics parameters, rendering the process slow and human-labor intensive. In this paper, we investigate using Large Language Models (LLMs) to automate and accelerate sim-to-real design. Our LLM-guided sim-to-real approach requires only the physics simulation for the target task and automatically constructs suitable reward functions and domain randomization distributions to support real-world transfer. We first demonstrate our approach can discover sim-to-real configurations that are competitive with existing human-designed ones on quadruped locomotion and dexterous manipulation tasks. Then, we showcase that our approach is capable of solving novel robot tasks, such as quadruped balancing and walking atop a yoga ball, without iterative manual design.

## Installation
This repository contains code for DrEureka's reward generation, RAPP, and domain randomization generation pipelines as well as the forward locomotion and globe walking environments. The two environments are modified from [Rapid Locomotion](https://github.com/Improbable-AI/rapid-locomotion-rl) and [Dribblebot](https://github.com/Improbable-AI/dribblebot), respectively.

The following instructions will install everything under one Conda environment. We have tested on Ubuntu 20.04.

1. Create a new Conda environment with:
    ```
    conda create -n dr_eureka python=3.8
    conda activate dr_eureka
    ```
2. Install Pytorch with CUDA:
    ```
    pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
    ```
3. Install IsaacGym, the simulator for forward locomotion and globe walking:
    1. Download and install IsaacGym from NVIDIA: https://developer.nvidia.com/isaac-gym.
    2. Unzip the file:
        ```
        tar -xf IsaacGym_Preview_4_Package.tar.gz
        ```
    3. Install the python package:
        ```
        cd isaacgym/python
        pip install -e .
        ```
4. Install DrEureka:
    ```
    cd dr_eureka
    pip install -e .
    ```
5. Install the forward locomotion and globe walking environments:
    ```
    cd forward_locomotion
    pip install -e .
    cd ../globe_walking
    pip install -e .
    ```

## Usage
We'll use forward locomotion (`forward_locomotion`) as an example. The following steps can also be done for globe walking (`globe_walking`).

First, run reward generation (Eureka):
```
cd ../eureka
python eureka.py env=forward_locomotion
```
At the end, the final best reward will be saved in `forward_locomotion/go1_gym/rewards/eureka_reward.py` and used for subsequent training runs. The Eureka logs will be stored in `eureka/outputs/[TIMESTAMP]`, and the run directory of the best-performing policy will be printed to terminal.

Second, copy the run directory and run RAPP:
```
cd ../dr_eureka
python rapp.py env=forward_locomotion run_path=[YOUR_RUN_DIRECTORY]
```

This will update the prompt in `dr_eureka/prompts/initial_users/forward_locomotion.txt` with the computed RAPP bounds.

Third, run DR generation with the new reward and RAPP bounds:
```
python dr_eureka.py env=forward_locomotion
```

The trained policies are ready for deployment, see the section below.

## Deployment
Our deployment infrastructure is based on [Walk These Ways](https://github.com/Improbable-AI/walk-these-ways). We'll use forward locomotion as an example, though the deployment setup for both environments are essentially the same.
1. Add the (relative) path to your checkpoint to `forward_locomotion/go1_gym_deploy/scripts/deploy_policy.py`. Note that you can have multiple policies at once and switch between them.
2. Start up the Go1, and connect to it on your machine via Ethernet. Make sure you can ssh onto the NX (`192.168.123.15`).
3. Put the robot into damping mode with the controller: L2+A, L2+B, L1+L2+START. The robot should be lying on the ground afterwards.
4. Run the following to send the checkpoint and code to the Go1:
    ```
    cd forward_locomotion/go1_gym_deploy/scripts
    ./send_to_unitree.sh
    ```
4. Now, ssh onto the Go1 and run the following:
    ```
    chmod +x installer/install_deployment_code.sh
    cd ~/go1_gym/go1_gym_deploy/scripts
    sudo ../installer/install_deployment_code.sh
    ```
5. Make sure your Go1 is in a safe location and hung up. Start up two prompts in the Go1. In the first, run:
    ```
    cd ~/go1_gym/go1_gym_deploy/autostart
    ./start_unitree_sdk.sh
    ```
6. In the second, run:
    ```
    cd ~/go1_gym/go1_gym_deploy/docker
    sudo make autostart && sudo docker exec -it foxy_controller bash
    ```
7. The previous command should enter a Docker image. Within it, run:
    ```
    cd /home/isaac/go1_gym && rm -r build && python3 setup.py install && cd go1_gym_deploy/scripts && python3 deploy_policy.py
    ```
8. Now, you can press R2 on the controller, and the robot should extend its legs (calibrate).
9. Pressing R2 again will start the policy.
10. To switch policies, press L1 or R1 to switch between policies in the list in `deploy_policy.py`.

## Code Structure
DrEureka manipulates pre-defined environments by inserting generated reward functions and domain randomization configurations. To do so, we have designed the environment code to be modular and easily configurable. Below, we explain how the components of our code interact with each other, using forward locomotion as an example:

`eureka/eureka.py` runs the reward generation process. It uses:
1. **Environment source code** as input to the LLM, which is at `eureka/envs/forward_locomotion.py`. This is a shortened version of the actual environment code to save token usage.
2. **Reward signature definition** as input to the LLM, which is at `eureka/prompts/reward_signatures/forward_locomotion.txt`. This file should contain a simple format for the LLM to follow. It may also contain additional instructions or explanations for the format, if necessary.
3. **Location of training script**, which is defined as `train_script: scripts/train.py` in `eureka/cfg/env/forward_locomotion.yaml`.
4. **Location of the reward template and output files**, which are defined as `reward_template_file: go1_gym/rewards/eureka_reward_template.py` and `reward_output_file: go1_gym/rewards/eureka_reward.py` in `eureka/cfg/env/forward_locomotion.yaml`. Eureka reads the template file's boilerplate code, fills in the reward function, and writes to the output file for use during training.
5. **Function to extract training metrics**, which is defined in `eureka/utils/misc.py` as `construct_run_log(stdout_str)`. This function parses the training script's standard output into a dictionary. Alternatively, it can be used to load a file containing metrics saved during training (for example, tensorboard logs).

`dr_eureka/rapp.py` computes the RAPP bounds. It uses:
1. **Location of the play (evaluation) script**, which is defined as `play_script: scripts/play.py` in `dr_eureka/cfg/env/forward_locomotion.yaml`.
2. **Location of the DR template and output files**, which are defined as `dr_template_file: go1_gym/envs/base/legged_robot_config_template.py` and `dr_output_file: go1_gym/envs/base/legged_robot_config.py` in `dr_eureka/cfg/env/forward_locomotion.yaml`. Like the reward template/output setup, DrEureka fills in the boilerplate code and writes to the output file for use during evaluation.
3. **List of randomizable DR parameters**, defined in the variable `parameter_test_vals` in `dr_eureka/rapp.py`.
4. **Simple success criteria** for the task, defined as the function `forward_locomotion_success()` in `dr_eureka/rapp.py`.

`dr_eureka/dr_eureka.py` runs the DR generation process. It uses:
1. **RAPP bounds** as input to the LLM, defined in `dr_eureka/prompts/initial_users/forward_locomotion.txt`. This uses the direct output of `dr_eureka/rapp.py`.
2. **Best reward function**, the output of reward generation. This should be in the file defined in `reward_output_file: go1_gym/rewards/eureka_reward.py`.
3. **Location of the training script**, same as reward generation. This is defined in `dr_eureka/cfg/env/forward_locomotion.yaml`.
4. **Location of the DR template and output files**, same as RAPP.
5. **Function to extract training metrics**, same as reward generation. Note that this is used only for a general idea of the policy's performance in simulation, and unlike reward generation, is not used for iterative feedback.

## Acknowledgements
We thank the following open-sourced projects:
* Our simulation runs in [IsaacGym](https://developer.nvidia.com/isaac-gym).
* Our LLM-generation algorithm builds on [Eureka](https://github.com/eureka-research/Eureka).
* Our environments are adapted from [Rapid Locomotion](https://github.com/Improbable-AI/rapid-locomotion-rl) and [Dribblebot](https://github.com/Improbable-AI/dribblebot).
* The environment structure and training code build on [Legged Gym](https://github.com/leggedrobotics/legged_gym) and [RSL_RL](https://github.com/leggedrobotics/rsl_rl).

## License
This codebase is released under [MIT License](LICENSE).

## Citation
If you find our work useful, please consider citing us!
```bibtex
@inproceedings{ma2024dreureka,
    title   = {DrEureka: Language Model Guided Sim-To-Real Transfer},
    author  = {Yecheng Jason Ma and William Liang and Hungju Wang and Sam Wang and Yuke Zhu and Linxi Fan and Osbert Bastani and Dinesh Jayaraman}
    year    = {2024},
  booktitle = {Robotics: Science and Systems (RSS)}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
dr_eureka/
  cfg/
    config.yaml
    config_rapp.yaml
    env/
    hydra/
  dr_eureka.py
  prompts/
    initial_system.txt
    initial_users/
  rapp.py
  utils/
    create_task.py
    extract_task_code.py
    file_utils.py
    misc.py
eureka/
  cfg/
    config.yaml
    env/
    hydra/
  envs/
    forward_locomotion.py
    globe_walking.py
  eureka.py
  prompts/
    code_feedback.txt
    code_output_tip.txt
    code_output_tip_temp.txt
    execution_error_feedback.txt
    initial_system.txt
    initial_user.txt
    policy_feedback.txt
    reward_signatures/
  utils/
    extract_task_code.py
    file_utils.py
    misc.py
forward_locomotion/
  LICENSE
  LICENSES/
    legged_gym/
    rsl_rl/
  go1_gym/
    __init__.py
    envs/
    rewards/
    utils/
  go1_gym_deploy/
    __init__.py
    autostart/
    docker/
    envs/
    installer/
    lcm_types/
    scripts/
    setup.py
    tests/
    unitree_legged_sdk_bin/
    utils/
  go1_gym_learn/
    __init__.py
    env/
    eval_metrics/
    ppo/
    utils/
  resources/
    robots/
  runs/
    forward_locomotion/
  scripts/
    __init__.py
    play.py
    train.py
  setup.py
globe_walking/
  LICENSE
  LICENSES/
    legged_gym/
    rsl_rl/
  go1_gym/
    __init__.py
    envs/
    rewards/
    robots/
    sensors/
    terrains/
    utils/
  go1_gym_deploy/
    __init__.py
    autostart/
    docker/
    envs/
    installer/
    lcm_types/
    scripts/
    setup.py
    tests/
    unitree_legged_sdk_bin/
    utils/
  go1_gym_learn/
    __init__.py
    env/
    eval_metrics/
    ppo_cse/
    ppo_cse_teacher_student/
    utils/
  resources/
    actuator_nets/
    objects/
    robots/
    textures/
  runs/
    globe_walking/
  scripts/
    __init__.py
    actuator_net/
    play.py
    train.py
  setup.py
setup.py
```

## Config files (11)


### dr_eureka/cfg/config.yaml

```yaml
defaults:
  - _self_
  - env: forward_locomotion
  - override hydra/launcher: local
  - override hydra/output: local

hydra:
  job:
    chdir: True

# LLM parameters
model: gpt-4-0125-preview
temperature: 1.0

# Eureka parameters
sample: 16                  # number of Eureka samples to generate per iteration

# Weights and Biases
use_wandb: False            # whether to use wandb for logging
wandb_username: ""          # wandb username if logging with wandb
wandb_project: ""           # wandb project if logging with wandb
```

### dr_eureka/cfg/config_rapp.yaml

```yaml
defaults:
  - _self_
  - env: forward_locomotion
  - override hydra/launcher: local
  - override hydra/output: local

hydra:
  output_subdir: null

run_path: ""
```

### dr_eureka/cfg/env/forward_locomotion.yaml

```yaml
task: Forward Locomotion
env_name: forward_locomotion
description: To train a quadruped robot to run on a variety of terrains indoor and outdoor. The goal of the robot is to run forward at 2.0 m/s while remaining steady and safe in the real world.

train_script: scripts/train.py
dr_template_file: go1_gym/envs/base/legged_robot_config_template.py
dr_output_file: go1_gym/envs/base/legged_robot_config.py

train_iterations: 1000
success_keyword: running
failure_keyword: Traceback

play_script: scripts/play.py
play_iterations: 100
```

### dr_eureka/cfg/env/globe_walking.yaml

```yaml
task: Globe Walking
env_name: globe_walking
description: To train a quadruped robot to balance on a yoga ball for as long as possible. Please note that our simulation environment models the ball as a solid rigid object, so the robot will not be able to deform the ball in any way. However, our real yoga ball is hollow, bouncy, and deformable, so the robot will need to adapt to this difference. Please keep this in mind when designing your domain randomization.

train_script: scripts/train.py
dr_template_file: go1_gym/envs/base/legged_robot_config_template.py
dr_output_file: go1_gym/envs/base/legged_robot_config.py

train_iterations: 1000
success_keyword: running
failure_keyword: Traceback

play_script: scripts/play.py
play_iterations: 200
```

### dr_eureka/cfg/hydra/launcher/local.yaml

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

### dr_eureka/cfg/hydra/output/local.yaml

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

### eureka/cfg/config.yaml

```yaml
defaults:
  - _self_
  - env: forward_locomotion
  - override hydra/launcher: local
  - override hydra/output: local

hydra:
  job:
    chdir: True

# LLM parameters
model: gpt-4-0125-preview
temperature: 1.0

# Eureka parameters
iteration: 5                # how many iterations of Eureka to run
sample: 16                  # number of Eureka samples to generate per iteration

# Weights and Biases
use_wandb: False            # whether to use wandb for logging
wandb_username: ""          # wandb username if logging with wandb
wandb_project: ""           # wandb project if logging with wandb
```

### eureka/cfg/env/forward_locomotion.yaml

```yaml
task: Forward Locomotion
env_name: forward_locomotion
description: To make the go1 quadruped run forward with a velocity of exactly 2.0 m/s in the positive x direction of the global coordinate frame. The policy will be trained in simulation and deployed in the real world, so the policy should be as steady and stable as possible with minimal action rate. Specifically, as it's running, the torso should remain near a z position of 0.34, and the orientation should be perpendicular to gravity. Also, the legs should move smoothly and avoid the DOF limits.
# Note: 0.34 is from go1_config.py (base_height_target)

train_script: scripts/train.py
reward_template_file: go1_gym/rewards/eureka_reward_template.py
reward_output_file: go1_gym/rewards/eureka_reward.py

train_iterations: 1000
success_keyword: running
failure_keyword: Traceback
```

### eureka/cfg/env/globe_walking.yaml

```yaml
task: Globe Walking
env_name: globe_walking
description: To make the go1 quadruped balance on the top of the ball. The quadruped should maintain a z-position of 2 * ball_radius or higher. Please keep in mind that the policy learned using your reward terms will be deployed on a robot in the real world. As such, you should prioritize safety, robustness, and feasibility over performance. Please generate reward terms that penalize actions that are unsafe or infeasible. Please also penalize jittery or fast actions that may burn out the motors. Also, remember to keep the scaling of your regularization terms small. If you choose to use env.torques, please keep in mind that this value will be large, so your scaling for this term should be near 0.00001.

train_script: scripts/train.py
reward_template_file: go1_gym/rewards/eureka_reward_template.py
reward_output_file: go1_gym/rewards/eureka_reward.py

train_iterations: 1000
success_keyword: running
failure_keyword: Traceback
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

## Python signatures and reward/observation bodies (55 files)


### dr_eureka/utils/create_task.py

```
def create_task(root_dir, task, env_name, suffix)
```

### dr_eureka/utils/extract_task_code.py

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

### eureka/envs/forward_locomotion.py

```
class LeggedRobot(BaseTask)
    """Rest of environment ommitted"""
    def _init_buffers(self)
def _process_dof_props(self, props, env_id)
```

### eureka/envs/globe_walking.py

```
class LeggedRobot(BaseTask)
    """Rest of environment ommitted"""
    def _init_buffers(self)
    def _init_custom_buffers__(self)
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

### forward_locomotion/go1_gym/envs/base/base_task.py

```
class BaseTask(Env)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless, eval_cfg)
    def get_observations(self)
    def get_privileged_observations(self, horizon)
    def reset_idx(self, env_ids)
    def reset(self)
    def step(self, actions)
    def render_gui(self, sync_frame_time)
    def close(self)

```python
def get_observations(self):
        return self.obs_buf
```

```python
def get_privileged_observations(self, horizon=0):
        if horizon == 0:
            return self.privileged_obs_buf
        else:
            env_timesteps_remaining_until_rand = int(self.cfg.domain_rand.rand_interval) - self.episode_length_buf % int(self.cfg.domain_rand.rand_interval)
            switched_env_ids = torch.arange(self.num_envs, device=self.device)[env_timesteps_remaining_until_rand>=horizon]
            privileged_obs_buf = self.privileged_obs_buf
            privileged_obs_buf[switched_env_ids] = self.next_privileged_obs_buf[switched_env_ids]
            return privileged_obs_buf
```
```

### forward_locomotion/go1_gym/envs/base/curriculum.py

```
def is_met(scale, l2_err, threshold)
def key_is_met(metric_cache, config, ep_len, target_key, env_id, threshold)
class Curriculum()
    def set_to(self, low, high, value)
    def __init__(self, seed)
    def __len__(self)
    def __getitem__(self)
    def update(self)
    def sample_bins(self, batch_size)
    def sample_uniform_from_cell(self, centroids)
    def sample(self, batch_size)
class SumCurriculum(Curriculum)
    def __init__(self, seed)
    def update(self, bin_inds, l1_error, threshold)
    def success_rates(self)
class RewardThresholdCurriculum(Curriculum)
    def __init__(self, seed)
    def get_local_bins(self, bin_inds, range)
    def update(self, bin_inds, lin_vel_rewards, ang_vel_rewards, lin_vel_threshold, ang_vel_threshold, local_range)
    def log(self, bin_inds, lin_vel_raw, ang_vel_raw, episode_duration)
```

### forward_locomotion/go1_gym/envs/base/legged_robot.py

```
class LeggedRobot(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless, eval_cfg, initial_dynamics_dict)
    def load_cfg(self, cfg, headless, eval_cfg, deploy, prone, num_envs)
    def step(self, actions)
    def post_physics_step(self)
    def check_termination(self)
    def reset_evaluation_envs(self)
    def reset_idx(self, env_ids)
    def set_idx_pose(self, env_ids, dof_pos, base_state)
    def compute_reward(self)
    def compute_observations(self)
    def create_sim(self)
    def set_camera(self, position, lookat)
    def set_main_agent_pose(self, loc, quat)
    def _call_train_eval(self, func, env_ids)
    def _randomize_gravity(self, external_force)
    def _process_rigid_shape_props(self, props, env_id)
    def _process_dof_props(self, props, env_id)
    def _randomize_rigid_body_props(self, env_ids, cfg)
    def _randomize_dof_props(self, env_ids, cfg)
    def _process_rigid_body_props(self, props, env_id)
    def _post_physics_step_callback(self)
    def _resample_commands(self, env_ids)
    def _resample_commands_uniform(self, env_ids, cfg)
    def _compute_torques(self, actions)
    def _reset_dofs(self, env_ids, cfg)
    def _reset_root_states(self, env_ids, cfg)
    def _push_robots(self, env_ids, cfg)
    def _teleport_robots(self, env_ids, cfg)
    def _update_terrain_curriculum(self, env_ids, cfg)
    def update_command_curriculum(self, env_ids, cfg, episode_sums)
    def _update_command_curriculum_uniform(self, env_ids, cfg, episode_sums)
    def _get_noise_scale_vec(self, cfg)
    def _init_buffers(self)
    def _init_custom_buffers__(self)
    def _init_command_distribution(self, env_ids)
    def _prepare_reward_function(self)
    def _create_ground_plane(self)
    def _create_heightfield(self)
    def _create_trimesh(self)
    def _create_envs(self)
    def render(self, mode)
    def _render_headless(self)
    def start_recording(self)
    def start_recording_eval(self)
    def pause_recording(self)
    def pause_recording_eval(self)
    def get_complete_frames(self)
    def get_complete_frames_eval(self)
    def _get_env_origins(self, env_ids, cfg)
    def _parse_cfg(self, cfg)
    def _draw_debug_vis(self)
    def _init_height_points(self, env_ids, cfg)
    def _get_heights(self, env_ids, cfg)

```python
def compute_reward(self):
        """ Compute rewards
            Calls each reward function which had a non-zero scale (processed in self._prepare_reward_function())
            adds each terms to the episode sums and to the total reward
        """
        self.rew_buf[:] = 0.
        if self.cfg.rewards.reward_container_name == "OriginalReward":
            for i in range(len(self.reward_functions)):
                name = self.reward_names[i]
                rew = self.reward_functions[i]() * self.reward_scales[name]
                self.rew_buf += rew
                self.episode_sums[name] += rew
                self.command_sums[name] += rew
            if self.cfg.rewards.only_positive_rewards:
                self.rew_buf[:] = torch.clip(self.rew_buf[:], min=0.)
        else:
            rew, rew_components = self.reward_container.compute_reward()
            self.rew_buf += rew
            for name, rew_term in rew_components.items():
                self.episode_sums[name] += rew_term
                self.command_sums[name] += rew_term
            self.episode_sums["success"] += self.reward_container.compute_success()

        self.episode_sums["total"] += self.rew_buf

        if self.cfg.rewards.reward_container_name == "OriginalReward" and "termination" in self.reward_scales:
            rew = self.reward_container._reward_termination() * self.reward_scales["termination"]
            self.rew_buf += rew
            self.episode_sums["termination"] += rew
            self.command_sums["termination"] += rew

        self.command_sums["lin_vel_raw"] += self.base_lin_vel[:, 0]
        self.command_sums["ang_vel_raw"] += self.base_ang_vel[:, 2]
        self.command_sums["lin_vel_residual"] += (self.base_lin_vel[:, 0] - self.commands[:, 0]) ** 2
        self.command_sums["ang_vel_residual"] += (self.base_ang_vel[:, 2] - self.commands[:, 2]) ** 2
        self.command_sums["ep_timesteps"] += 1
```

```python
def compute_observations(self):
        """ Computes observations
        """
        self.obs_buf = torch.cat((self.projected_gravity,
                                  (self.dof_pos - self.default_dof_pos) * self.obs_scales.dof_pos,
                                  self.dof_vel * self.obs_scales.dof_vel,
                                  self.actions
                                  ), dim=-1)
        if self.cfg.env.observe_command:
            self.obs_buf = torch.cat((self.projected_gravity,
                                      self.commands[:, :3] * self.commands_scale,
                                      (self.dof_pos - self.default_dof_pos) * self.obs_scales.dof_pos,
                                      self.dof_vel * self.obs_scales.dof_vel,
                                      self.actions
                                      ), dim=-1)


        if self.cfg.env.observe_vel:
            if self.cfg.commands.global_reference:
                self.obs_buf = torch.cat((self.root_states[:, 7:10] * self.obs_scales.lin_vel,
                                          self.base_ang_vel * self.obs_scales.ang_vel,
                                          self.obs_buf), dim=-1)
            else:
                self.obs_buf = torch.cat((self.base_lin_vel * self.obs_scales.lin_vel,
                                          self.base_ang_vel * self.obs_scales.ang_vel,
                                          self.obs_buf), dim=-1)

        if self.cfg.env.observe_only_ang_vel:
            self.obs_buf = torch.cat((self.base_ang_vel * self.obs_scales.ang_vel,
                                      self.obs_buf), dim=-1)

        if self.cfg.env.observe_only_lin_vel:
            self.obs_buf = torch.cat((self.base_lin_vel * self.obs_scales.lin_vel,
                                      self.obs_buf), dim=-1)

        if self.cfg.env.observe_yaw:
            forward = quat_apply(self.base_quat, self.forward_vec)
            heading = torch.atan2(forward[:, 1], forward[:, 0])
            heading_error = torch.clip(0.5 * wrap_to_pi(heading), -1., 1.).unsqueeze(1)
            self.obs_buf = torch.cat((self.obs_buf,
                                      heading_error), dim=-1)

        # add perceptive inputs if not blind
        if self.cfg.terrain.measure_heights:
            heights = torch.clip(self.root_states[:, 2].unsqueeze(1) - 0.5 - self.measured_heights, -1,
                                 1.) * self.obs_scales.height_measurements
            self.obs_buf = torch.cat((self.obs_buf, heights), dim=-1)
        # add noise if needed
        if self.add_noise:
            self.obs_buf += (2 * torch.rand_like(self.obs_buf) - 1) * self.noise_scale_vec

        # build privileged obs
        # in RLvRL: Friction, Restitution, Payload, CoM displacement, Motor Strength

        # scale all the randomization from -1 to 1
        friction_coeffs_scale, friction_coeffs_shift = get_scale_shift(self.cfg.domain_rand.friction_range)
        restitutions_scale, restitutions_shift = get_scale_shift(self.cfg.domain_rand.restitution_range)
        payloads_scale, payloads_shift = get_scale_shift(self.cfg.domain_rand.added_mass_range)
        com_displacements_scale, com_displacements_shift = get_scale_shift(
            self.cfg.domain_rand.com_displacement_range)
        motor_strengths_scale, motor_strengths_shift = get_scale_shift(self.cfg.domain_rand.motor_strength_range)

        if not self.cfg.env.priv_observe_friction: friction_coeffs_scale = 0
        if not self.cfg.env.priv_observe_restitution: restitutions_scale = 0
        if not self.cfg.env.priv_observe_base_mass: payloads_scale = 0
        if not self.cfg.env.priv_observe_com_displacement: com_displacements_scale = 0
        if not self.cfg.env.priv_observe_motor_strength: motor_strengths_scale = 0

        self.privileged_obs_buf = torch.cat(
            ((self.friction_coeffs.unsqueeze(1) - friction_coeffs_shift) * friction_coeffs_scale,  # friction coeff
             (s
```

```python
def _prepare_reward_function(self):
        """ Prepares a list of reward functions, whcih will be called to compute the total reward.
            Looks for self._reward_<REWARD_NAME>, where <REWARD_NAME> are names of all non zero reward scales in the cfg.
        """
        # reward containers
        reward_container_name = self.cfg.rewards.reward_container_name
        from forward_locomotion.go1_gym.rewards.original_reward import OriginalReward
        from forward_locomotion.go1_gym.rewards.eureka_reward import EurekaReward
        if reward_container_name == "OriginalReward":
            self.reward_container = OriginalReward(self)
        elif reward_container_name == "EurekaReward":
            self.reward_container = EurekaReward(self)
        else:
            raise NameError(f"Unknown reward container: {reward_container_name}")

        if reward_container_name == "OriginalReward":
            # remove zero scales + multiply non-zero ones by dt
            for key in list(self.reward_scales.keys()):
                scale = self.reward_scales[key]
                if scale == 0:
                    self.reward_scales.pop(key)
                else:
                    self.reward_scales[key] *= self.dt
            # prepare list of functions
            self.reward_functions = []
            self.reward_names = []
            for name, scale in self.reward_scales.items():
                if name == "termination":
                    continue
                if not hasattr(self.reward_container, '_reward_' + name):
                    print(f"Warning: reward {'_reward_' + name} has nonzero coefficient but was not found!")
                else:
                    self.reward_names.append(name)
                    self.reward_functions.append(getattr(self.reward_container, '_reward_' + name))
        else:
            _, reward_components = self.reward_container.compute_reward()
            self.reward_names = list(reward_components.keys())

        # reward episode sums
        self.episode_sums = {
            name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
            for name in self.reward_names}
        self.episode_sums["total"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                 requires_grad=False)
        self.episode_sums["success"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                    requires_grad=False)
        self.episode_sums_eval = {
            name: -1 * torch.ones(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
            for name in self.reward_names}
        self.episode_sums_eval["total"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                      requires_grad=False)
        self.episode_sums_eval["success"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                            requires_grad=False)
        self.command_sums = {
            name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
            for name in
            list(self.reward_names) + ["lin_vel_raw", "ang_vel_raw", "lin_vel_residual", "ang_vel_residual",
                                               "ep_timesteps"]}
```
```

### forward_locomotion/go1_gym/envs/base/legged_robot_config.py

```
class Cfg(PrefixProto)
def set_seed(seed, torch_deterministic, rank)
```

### forward_locomotion/go1_gym/envs/base/legged_robot_config_template.py

```
class Cfg(PrefixProto)
def set_seed(seed, torch_deterministic, rank)
```

### forward_locomotion/go1_gym/envs/go1/go1_config.py

```
def config_go1(Cnfg)
```

### forward_locomotion/go1_gym/envs/mini_cheetah/mini_cheetah_config.py

```
def config_mini_cheetah(Cnfg)
```

### forward_locomotion/go1_gym/envs/mini_cheetah/velocity_tracking/velocity_tracking_easy_env.py

```
class VelocityTrackingEasyEnv(LeggedRobot)
    def __init__(self, sim_device, headless, num_envs, prone, deploy, cfg, eval_cfg, initial_dynamics_dict, physics_engine)
    def step(self, actions)
    def reset(self)
```

### forward_locomotion/go1_gym/envs/wrappers/history_wrapper.py

```
class HistoryWrapper(Wrapper)
    def __init__(self, env)
    def step(self, action)
    def get_observations(self)
    def reset_idx(self, env_ids)
    def reset(self)

```python
def get_observations(self):
        obs = self.env.get_observations()
        privileged_obs = self.env.get_privileged_observations()
        self.obs_history = torch.cat((self.obs_history[:, self.env.num_obs:], obs), dim=-1)
        return {'obs': obs, 'privileged_obs': privileged_obs, 'obs_history': self.obs_history}
```
```

### forward_locomotion/go1_gym/rewards/eureka_reward.py

```
class EurekaReward()
    def __init__(self, env)
    def load_env(self, env)
    def compute_reward(self, using_curriculum)
    def compute_success(self)

```python
def compute_reward(self, using_curriculum=False):
        env = self.env  # Do not skip this line. Afterwards, use env.{parameter_name} to access parameters of the environment.
    
        # Ideal forward velocity in the x direction
        # target_velocity_x = 2.0
        target_velocity_x = self.env.cfg.rewards.target_velocity
        # Ideal height of the robot's torso
        target_height_z = 0.34
    
        # Compute the velocity reward component
        current_velocity_x = env.root_states[:, 7]  # Linear velocity in x from the root_states tensor
        velocity_error = torch.abs(current_velocity_x - target_velocity_x)
        velocity_reward = torch.exp(-velocity_error)
    
        # Compute the height reward component
        current_height = env.root_states[:, 2]  # Position in z from the root_states tensor
        height_error = torch.abs(current_height - target_height_z)
        height_reward = torch.exp(-5.0 * height_error)  # More weight to maintain height
    
        # Compute the orientation reward component
        # Ideal orientation is perpendicular to gravity, i.e., the projected gravity vector should be [0, 0, -1] in the robot's frame
        ideal_projected_gravity = torch.tensor([0., 0., -1.], device=env.device).repeat((env.num_envs, 1))
        orientation_error = torch.norm(env.projected_gravity - ideal_projected_gravity, dim=1)
        orientation_reward = torch.exp(-5.0 * orientation_error)  # More weight to maintain orientation
    
        # Legs movement within DOF limits reward component
        dof_limit_violations = torch.any(
            (env.dof_pos < env.dof_pos_limits[:, 0]) | (env.dof_pos > env.dof_pos_limits[:, 1]),
            dim=-1)
        dof_limit_violations_reward = 1.0 - dof_limit_violations.float()  # Penalize if any DOF limit is violated
    
        # Smoothness reward component (penalize the change in actions to encourage smooth movements)
        action_difference = torch.norm(env.actions - env.last_actions, dim=1)
        smoothness_reward = torch.exp(-0.1 * action_difference)
    
        # Combine reward components
        total_reward = velocity_reward * height_reward * orientation_reward * dof_limit_violations_reward * smoothness_reward
    
        # Debug information
        reward_components = {"velocity_reward": velocity_reward,
                             "height_reward": height_reward,
                             "orientation_reward": orientation_reward,
                             "dof_limit_violations_reward": dof_limit_violations_reward,
                             "smoothness_reward": smoothness_reward}

        if using_curriculum:
            # Additional terms, only used when training with curriculum
            def _reward_tracking_lin_vel(env):
                # Tracking of linear velocity commands (xy axes)
                if env.cfg.commands.global_reference:
                    lin_vel_error = torch.sum(torch.square(env.commands[:, :2] - env.root_states[:, 7:9]), dim=1)
                else:
                    lin_vel_error = torch.sum(torch.square(env.commands[:, :2] - env.base_lin_vel[:, :2]), dim=1)
                return torch.exp(-lin_vel_error / env.cfg.rewards.tracking_sigma)
            def _reward_tracking_ang_vel(env):
                # Tracking of angular velocity commands (yaw) 
                ang_vel_error = torch.square(env.commands[:, 2] - env.base_ang_vel[:, 2])
                return torch.exp(-ang_vel_error / env.cfg.rewards.tracking_sigma_yaw)
            reward_components["tracking_lin_vel"] = _reward_tracking_lin_vel(env)
            reward_components["tracking_ang_vel"] = _reward_tracking_ang_vel(env)
                             
        return total_reward, reward_components
```

```python
def _reward_tracking_lin_vel(env):
                # Tracking of linear velocity commands (xy axes)
                if env.cfg.commands.global_reference:
                    lin_vel_error = torch.sum(torch.square(env.commands[:, :2] - env.root_states[:, 7:9]), dim=1)
                else:
                    lin_vel_error = torch.sum(torch.square(env.commands[:, :2] - env.base_lin_vel[:, :2]), dim=1)
                return torch.exp(-lin_vel_error / env.cfg.rewards.tracking_sigma)
```

```python
def _reward_tracking_ang_vel(env):
                # Tracking of angular velocity commands (yaw) 
                ang_vel_error = torch.square(env.commands[:, 2] - env.base_ang_vel[:, 2])
                return torch.exp(-ang_vel_error / env.cfg.rewards.tracking_sigma_yaw)
```
```

### forward_locomotion/go1_gym/rewards/eureka_reward_template.py

```
class EurekaReward()
    def __init__(self, env)
    def load_env(self, env)
    def compute_success(self)
```

### forward_locomotion/go1_gym/rewards/original_reward.py

```
class OriginalReward()
    def __init__(self, env)
    def load_env(self, env)
    def _reward_lin_vel_z(self)
    def _reward_ang_vel_xy(self)
    def _reward_orientation(self)
    def _reward_base_height(self)
    def _reward_torques(self)
    def _reward_energy(self)
    def _reward_energy_expenditure(self)
    def _reward_dof_vel(self)
    def _reward_dof_acc(self)
    def _reward_action_rate(self)
    def _reward_collision(self)
    def _reward_termination(self)
    def _reward_survival(self)
    def _reward_dof_pos_limits(self)
    def _reward_dof_vel_limits(self)
    def _reward_torque_limits(self)
    def _reward_tracking_lin_vel(self)
    def _reward_tracking_ang_vel(self)
    def _reward_feet_air_time(self)
    def _reward_stumble(self)
    def _reward_stand_still(self)
    def _reward_feet_contact_forces(self)

```python
def _reward_lin_vel_z(self):
        # Penalize z axis base linear velocity
        return torch.square(self.env.base_lin_vel[:, 2])
```

```python
def _reward_ang_vel_xy(self):
        # Penalize xy axes base angular velocity
        return torch.sum(torch.square(self.env.base_ang_vel[:, :2]), dim=1)
```

```python
def _reward_orientation(self):
        # Penalize non flat base orientation
        return torch.sum(torch.square(self.env.projected_gravity[:, :2]), dim=1)
```

```python
def _reward_base_height(self):
        # Penalize base height away from target
        base_height = torch.mean(self.env.root_states[:, 2].unsqueeze(1) - self.env.measured_heights, dim=1)
        return torch.square(base_height - self.env.cfg.rewards.base_height_target)
```

```python
def _reward_torques(self):
        # Penalize torques
        return torch.sum(torch.square(self.env.torques), dim=1)
```

```python
def _reward_energy(self):
        # Penalize torques
        return torch.sum(torch.multiply(self.env.torques, self.env.dof_vel), dim=1)
```

```python
def _reward_energy_expenditure(self):
        # Penalize torques
        return torch.sum(torch.clip(torch.multiply(self.env.torques, self.env.dof_vel), 0, 1e30), dim=1)
```

```python
def _reward_dof_vel(self):
        # Penalize dof velocities
        return torch.sum(torch.square(self.env.dof_vel), dim=1)
```

```python
def _reward_dof_acc(self):
        # Penalize dof accelerations
        return torch.sum(torch.square((self.env.last_dof_vel - self.env.dof_vel) / self.env.dt), dim=1)
```

```python
def _reward_action_rate(self):
        # Penalize changes in actions
        return torch.sum(torch.square(self.env.last_actions - self.env.actions), dim=1)
```

```python
def _reward_collision(self):
        # Penalize collisions on selected bodies
        return torch.sum(1. * (torch.norm(self.env.contact_forces[:, self.env.penalised_contact_indices, :], dim=-1) > 0.1),
                         dim=1)
```

```python
def _reward_termination(self):
        # Terminal reward / penalty
        return self.env.reset_buf * ~self.env.time_out_buf
```

```python
def _reward_survival(self):
        # Survival reward / penalty
        return ~(self.env.reset_buf * ~self.env.time_out_buf)
```

```python
def _reward_dof_pos_limits(self):
        # Penalize dof positions too close to the limit
        out_of_limits = -(self.env.dof_pos - self.env.dof_pos_limits[:, 0]).clip(max=0.)  # lower limit
        out_of_limits += (self.env.dof_pos - self.env.dof_pos_limits[:, 1]).clip(min=0.)
        return torch.sum(out_of_limits, dim=1)
```

```python
def _reward_dof_vel_limits(self):
        # Penalize dof velocities too close to the limit
        # clip to max error = 1 rad/s per joint to avoid huge penalties
        return torch.sum(
            (torch.abs(self.env.dof_vel) - self.env.dof_vel_limits * self.env.cfg.rewards.soft_dof_vel_limit).clip(min=0., max=1.),
            dim=1)
```

```python
def _reward_torque_limits(self):
        # penalize torques too close to the limit
        return torch.sum(
            (torch.abs(self.env.torques) - self.env.torque_limits * self.env.cfg.rewards.soft_torque_limit).clip(min=0.), dim=1)
```

```python
def _reward_tracking_lin_vel(self):
        # Tracking of linear velocity commands (xy axes)
        if self.env.cfg.commands.global_reference:
            lin_vel_error = torch.sum(torch.square(self.env.commands[:, :2] - self.env.root_states[:, 7:9]), dim=1)
        else:
            lin_vel_error = torch.sum(torch.square(self.env.commands[:, :2] - self.env.base_lin_vel[:, :2]), dim=1)
        return torch.exp(-lin_vel_error / self.env.cfg.rewards.tracking_sigma)
```

```python
def _reward_tracking_ang_vel(self):
        # Tracking of angular velocity commands (yaw) 
        ang_vel_error = torch.square(self.env.commands[:, 2] - self.env.base_ang_vel[:, 2])
        return torch.exp(-ang_vel_error / self.env.cfg.rewards.tracking_sigma_yaw)
```

```python
def _reward_feet_air_time(self):
        # Reward long steps
        # Need to filter the contacts because the contact reporting of PhysX is unreliable on meshes
        contact = self.env.contact_forces[:, self.env.feet_indices, 2] > 1.
        contact_filt = torch.logical_or(contact, self.env.last_contacts)
        self.env.last_contacts = contact
        first_contact = (self.env.feet_air_time > 0.) * contact_filt
        self.env.feet_air_time += self.env.dt
        rew_airTime = torch.sum((self.env.feet_air_time - 0.5) * first_contact,
                                dim=1)  # reward only on first contact with the ground
        rew_airTime *= torch.norm(self.env.commands[:, :2], dim=1) > 0.1  # no reward for zero command
        # rew_airTime *= torch.norm(self.env.base_lin_vel[:, :2], dim=1) > 0.1  # no reward for zero movement
        self.env.feet_air_time *= ~contact_filt
        return rew_airTime
```

```python
def _reward_stumble(self):
        # Penalize feet hitting vertical surfaces
        return torch.any(torch.norm(self.env.contact_forces[:, self.env.feet_indices, :2], dim=2) > \
                         5 * torch.abs(self.env.contact_forces[:, self.env.feet_indices, 2]), dim=1)
```

```python
def _reward_stand_still(self):
        # Penalize motion at zero commands
        return torch.sum(torch.abs(self.env.dof_pos - self.env.default_dof_pos), dim=1) * (
                torch.norm(self.env.commands[:, :2], dim=1) < 0.1)
```

```python
def _reward_feet_contact_forces(self):
        # penalize high contact forces
        return torch.sum((torch.norm(self.env.contact_forces[:, self.env.feet_indices, :],
                                     dim=-1) - self.env.cfg.rewards.max_contact_force).clip(min=0.), dim=1)
```
```

### forward_locomotion/go1_gym_deploy/envs/history_wrapper.py

```
class HistoryWrapper()
    def __init__(self, env)
    def step(self, action)
    def get_observations(self)
    def get_obs(self)
    def reset_idx(self, env_ids)
    def reset(self)
    def __getattr__(self, name)

```python
def get_observations(self):
        obs = self.env.get_observations()
        privileged_obs = self.env.get_privileged_observations()
        self.obs_history = torch.cat((self.obs_history[:, self.env.num_obs:], obs), dim=-1)
        return {'obs': obs, 'privileged_obs': privileged_obs, 'obs_history': self.obs_history}
```
```

### forward_locomotion/go1_gym_deploy/envs/lcm_agent.py

```
def class_to_dict(obj)
class LCMAgent()
    def __init__(self, cfg, se, command_profile)
    def set_probing(self, is_currently_probing)
    def get_obs(self)
    def get_privileged_observations(self)
    def publish_action(self, action, hard_reset)
    def reset(self)
    def reset_gait_indices(self)
    def step(self, actions, hard_reset)

```python
def get_privileged_observations(self):
        return None
```
```

### forward_locomotion/go1_gym_deploy/scripts/deploy_policy.py

```
def run_policy(label, se, max_vel, max_yaw_vel)
def run(labels, experiment_name, max_vel, max_yaw_vel)
def load_policy(logdir)
```

### forward_locomotion/go1_gym_deploy/utils/network_config_unitree.py

```
def get_saved_interface_name()
def get_likely_iface()
def main()
```

### forward_locomotion/go1_gym_learn/env/vec_env.py

```
class VecEnv(ABC)
    def step(self, actions)
    def reset(self, env_ids)
    def get_observations(self)
    def get_privileged_observations(self)

```python
def get_observations(self) -> torch.Tensor:
        pass
```

```python
def get_privileged_observations(self) -> Union[torch.Tensor, None]:
        pass
```
```

### forward_locomotion/scripts/train.py

```
def train_mc(iterations, command_config, reward_config, dr_config, eureka_target_velocity, headless, no_wandb, wandb_group, wandb_prefix, seed)
```

### globe_walking/go1_gym/envs/base/base_task.py

```
class BaseTask(Env)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def get_observations(self)
    def get_privileged_observations(self)
    def reset_idx(self, env_ids)
    def reset(self)
    def step(self, actions)
    def render_gui(self, sync_frame_time)
    def close(self)

```python
def get_observations(self):
        return self.obs_buf
```

```python
def get_privileged_observations(self):
        return self.privileged_obs_buf
```
```

### globe_walking/go1_gym/envs/base/curriculum.py

```
def is_met(scale, l2_err, threshold)
def key_is_met(metric_cache, config, ep_len, target_key, env_id, threshold)
class Curriculum()
    def set_to(self, low, high, value)
    def __init__(self, seed)
    def __len__(self)
    def __getitem__(self)
    def update(self)
    def sample_bins(self, batch_size, low, high)
    def sample_uniform_from_cell(self, centroids)
    def sample(self, batch_size, low, high)
class SumCurriculum(Curriculum)
    def __init__(self, seed)
    def update(self, bin_inds, l1_error, threshold)
    def success_rates(self)
class RewardThresholdCurriculum(Curriculum)
    def __init__(self, seed)
    def get_local_bins(self, bin_inds, ranges)
    def update(self, bin_inds, task_rewards, success_thresholds, local_range)
    def log(self, bin_inds, lin_vel_raw, ang_vel_raw, episode_duration)
```

### globe_walking/go1_gym/envs/base/legged_robot.py

```
class LeggedRobot(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless, initial_dynamics_dict, terrain_props, custom_heightmap)
    def pre_physics_step(self)
    def step(self, actions)
    def post_physics_step(self)
    def simulate_ball_pos_delay(self, new_ball_pos, last_ball_pos)
    def check_termination(self)
    def reset_idx(self, env_ids)
    def set_idx_pose(self, env_ids, dof_pos, base_state)
    def compute_reward(self)
    def initialize_sensors(self)
    def compute_observations(self)
    def create_sim(self)
    def _randomize_gravity(self, external_force)
    def _randomize_ball_drag(self)
    def _randomize_lag_timesteps(self)
    def _process_rigid_shape_props(self, props, env_id)
    def _process_ball_rigid_shape_props(self, props, env_id)
    def _process_dof_props(self, props, env_id)
    def _randomize_rigid_body_props(self, env_ids, cfg)
    def refresh_actor_rigid_shape_props(self, env_ids, cfg)
    def _randomize_dof_props(self, env_ids, cfg)
    def _process_robot_rigid_body_props(self, props, env_id)
    def _process_ball_rigid_body_props(self, props, env_id)
    def _post_physics_step_callback(self)
    def _resample_commands(self, env_ids)
    def _step_contact_targets(self)
    def _compute_torques(self, actions)
    def _reset_dofs(self, env_ids, cfg)
    def _reset_root_states(self, env_ids, cfg)
    def _push_robots(self, env_ids, cfg)
    def _push_balls(self, env_ids, cfg)
    def _update_terrain_curriculum(self, env_ids)
    def _update_command_ranges(self, env_ids)
    def _teleport_robots(self, env_ids, cfg)
    def _init_buffers(self)
    def _init_custom_buffers__(self)
    def _init_command_distribution(self, env_ids)
    def _prepare_reward_function(self)
    def _create_envs(self)
    def render(self, mode, target_loc, cam_distance)
    def _render_headless(self)
    def start_recording(self)
    def pause_recording(self)
    def get_complete_frames(self)
    def _get_env_origins(self, env_ids, cfg)
    def _parse_cfg(self, cfg)
    def get_segmentation_images(self, env_ids)
    def get_rgb_images(self, env_ids)
    def get_depth_images(self, env_ids)
    def initialize_cameras(self, env_ids)
    def set_lighting(self)
    def set_camera(self, position, lookat)

```python
def compute_reward(self):
        """ Compute rewards
            Calls each reward function which had a non-zero scale (processed in self._prepare_reward_function())
            adds each terms to the episode sums and to the total reward
        """
        self.rew_buf[:] = 0.
        self.rew_buf_pos[:] = 0.
        self.rew_buf_neg[:] = 0.
        if self.reward_functions is not None:
            for i in range(len(self.reward_functions)):
                name = self.reward_names[i]
                rew = self.reward_functions[i]()
                if "success" not in name:
                    self.rew_buf += rew
                    if torch.sum(rew) >= 0:
                        self.rew_buf_pos += rew
                    elif torch.sum(rew) <= 0:
                        self.rew_buf_neg += rew
                self.episode_sums[name] += rew
        else:
            rew, rew_components = self.reward_container.compute_reward()
            self.rew_buf += rew
            for name, rew_term in rew_components.items():
                self.episode_sums[name] += rew_term
                if torch.sum(rew_term) >= 0:
                    self.rew_buf_pos += rew_term
                elif torch.sum(rew_term) <= 0:
                    self.rew_buf_neg += rew_term
            self.episode_sums["success"] += self.reward_container.compute_success()
        self.episode_sums["total"] += self.rew_buf

        if self.cfg.commands.num_commands > 0:
            self.command_sums["lin_vel_raw"] += self.base_lin_vel[:, 0]
            self.command_sums["ang_vel_raw"] += self.base_ang_vel[:, 2]
            self.command_sums["lin_vel_residual"] += (self.base_lin_vel[:, 0] - self.commands[:, 0]) ** 2
            self.command_sums["ang_vel_residual"] += (self.base_ang_vel[:, 2] - self.commands[:, 2]) ** 2
            self.command_sums["ep_timesteps"] += 1
```

```python
def compute_observations(self):
        """ Computes observations
        """
        # aggregate the sensor data
        self.pre_obs_buf = []
        for sensor in self.sensors:
            self.pre_obs_buf += [sensor.get_observation()]

        self.pre_obs_buf = torch.reshape(torch.cat(self.pre_obs_buf, dim=-1), (self.num_envs, -1))
        self.obs_buf[:] = self.pre_obs_buf

        self.privileged_obs_buf = []
        # aggregate the privileged observations
        for sensor in self.privileged_sensors:
            self.privileged_obs_buf += [sensor.get_observation()]
        self.privileged_obs_buf = torch.reshape(torch.cat(self.privileged_obs_buf, dim=-1), (self.num_envs, -1))
        # add noise if needed
        if self.cfg.noise.add_noise:
            self.obs_buf += (2 * torch.rand_like(self.obs_buf) - 1) * self.noise_scale_vec
```

```python
def _prepare_reward_function(self):
        """ Prepares a list of reward functions, whcih will be called to compute the total reward.
            Looks for self._reward_<REWARD_NAME>, where <REWARD_NAME> are names of all non zero reward scales in the cfg.
        """
        # reward containers
        from globe_walking.go1_gym.rewards.eureka_reward import EurekaReward
        reward_containers = {"EurekaReward": EurekaReward}
        self.reward_container = reward_containers[self.cfg.rewards.reward_container_name](self)

        if "compute_reward" in dir(self.reward_container):
            exit()
            _, reward_components = self.reward_container.compute_reward()
            self.reward_names = list(reward_components.keys())
            self.reward_functions = None
        else:
            # prepare list of functions
            self.reward_functions = []
            self.reward_names = []
            for name in dir(self.reward_container):
                if not name.startswith("_reward_"):
                    continue
                name = name.replace("_reward_", "")
                self.reward_names.append(name)
                self.reward_functions.append(getattr(self.reward_container, '_reward_' + name))

        # reward episode sums
        self.episode_sums = {
            name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
            for name in self.reward_names}
        self.episode_sums["total"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                 requires_grad=False)
        self.episode_sums["success"] = torch.zeros(self.num_envs, dtype=torch.float, device=self.device,
                                                 requires_grad=False)
        self.command_sums = {
            name: torch.zeros(self.num_envs, dtype=torch.float, device=self.device, requires_grad=False)
            for name in
            list(self.reward_names) + ["lin_vel_raw", "ang_vel_raw", "lin_vel_residual", "ang_vel_residual",
                                               "ep_timesteps"]}
```
```

### globe_walking/go1_gym/envs/base/legged_robot_config.py

```
class Cfg(PrefixProto)
def set_seed(seed, torch_deterministic, rank)
```

### globe_walking/go1_gym/envs/base/legged_robot_config_template.py

```
class Cfg(PrefixProto)
def set_seed(seed, torch_deterministic, rank)
```

### globe_walking/go1_gym/envs/base/vec_task.py

```
def _create_sim_once(gym)
class Env(ABC)
    def __init__(self, config, sim_params, physics_engine, sim_device, headless)
    def allocate_buffers(self)
    def step(self, actions)
    def reset(self)
    def reset_idx(self, env_ids)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTask(Env)
    def __init__(self, config, sim_params, physics_engine, sim_device, headless)
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
    def apply_randomizations(self, dr_params, dr_params_target)
    def apply_randomizations_to_envs(self, env_ids, do_nonenv_randomize, dr_params, dr_params_target)
    def get_observations(self)
    def get_privileged_observations(self)
    def render_gui(self, sync_frame_time)

```python
def observation_space(self) -> gym.Space:
        """Get the environment's observation space."""
        return self.obs_space
```

```python
def get_observations(self):
        return self.obs_buf
```

```python
def get_privileged_observations(self):
        return self.privileged_obs_buf
```
```

### globe_walking/go1_gym/envs/go1/go1_config.py

```
def config_go1(Cnfg)
```

### globe_walking/go1_gym/envs/go1/velocity_tracking/__init__.py

```
class VelocityTrackingEasyEnv(LeggedRobot)
    def __init__(self, sim_device, headless, num_envs, prone, deploy, cfg, eval_cfg, initial_dynamics_dict, physics_engine)
    def step(self, actions)
    def reset(self)
```

### globe_walking/go1_gym/envs/wrappers/history_wrapper.py

```
class HistoryWrapper(Wrapper)
    def __init__(self, env)
    def step(self, action)
    def get_observations(self)
    def reset_idx(self, env_ids)
    def reset(self)

```python
def get_observations(self):
        obs = self.env.get_observations()
        privileged_obs = self.env.get_privileged_observations()
        self.obs_history = torch.cat((self.obs_history[:, self.env.num_obs:], obs), dim=-1)
        return {'obs': obs, 'privileged_obs': privileged_obs, 'obs_history': self.obs_history}
```
```

### globe_walking/go1_gym/rewards/eureka_reward.py

```
class EurekaReward()
    def __init__(self, env)
    def load_env(self, env)
    def _reward_height(self)
    def _reward_balance(self)
    def _reward_smooth_actions(self)
    def _reward_penalize_large_actions(self)
    def compute_success(self)

```python
def _reward_height(self):
        env = self.env
        height_threshold = 2.0 * env.ball_radius
        height_temperature = 7.0  # Fine-tuned temperature parameter
        height_exp = torch.exp((env.base_pos[:, 2] - height_threshold) / height_temperature)
        height_reward = torch.where(env.base_pos[:, 2] >= height_threshold, height_exp, torch.zeros_like(env.base_pos[:, 2]))
        return 1.5 * height_reward
```

```python
def _reward_balance(self):
        env = self.env
        balance_temperature = 5.0  # Fine-tuned temperature parameter
        # ball_top = env.object_pos_world_frame + torch.tensor([0.0, 0.0, env.ball_radius], device=env.device).unsqueeze(0)
        ball_top = env.object_pos_world_frame.clone()
        ball_top[:, 2] += env.ball_radius

        feet_dist_to_ball_top = torch.norm(env.foot_positions - ball_top.unsqueeze(1), dim=-1)
        balance_exp = torch.exp(-feet_dist_to_ball_top / balance_temperature)
        balance_reward = torch.mean(balance_exp, dim=-1)
        return 2.0 * balance_reward
```

```python
def _reward_smooth_actions(self):
        env = self.env
        action_diff = env.actions - env.last_actions
        smooth_actions_reward = -torch.mean(torch.abs(action_diff), dim=-1)
        return 1.0 * smooth_actions_reward
```

```python
def _reward_penalize_large_actions(self):
        env = self.env
        large_action_penalty = -torch.mean(torch.abs(env.actions), dim=-1)
        return 0.3 * large_action_penalty
```
```

### globe_walking/go1_gym/rewards/eureka_reward_template.py

```
class EurekaReward()
    def __init__(self, env)
    def load_env(self, env)
    def compute_success(self)
```

### globe_walking/go1_gym/sensors/action_sensor.py

```
class ActionSensor(Sensor)
    def __init__(self, env, attached_robot_asset, delay)
    def get_observation(self, env_ids)
    def get_noise_vec(self)
    def get_dim(self)

```python
def get_observation(self, env_ids = None):
        if self.delay == 0:
            return self.env.actions
        elif self.delay == 1:
            return self.env.last_actions
        else:
            raise NotImplementedError("Action delay of {} not implemented".format(self.delay))
```
```

### globe_walking/go1_gym/sensors/last_action_sensor.py

```
class LastActionSensor(Sensor)
    def __init__(self, env, attached_robot_asset, delay)
    def get_observation(self, env_ids)
    def get_noise_vec(self)
    def get_dim(self)

```python
def get_observation(self, env_ids = None):
        if self.delay == 0:
            return self.env.actions
        elif self.delay == 1:
            return self.env.last_actions
        else:
            raise NotImplementedError("Action delay of {} not implemented".format(self.delay))
```
```

### globe_walking/go1_gym_deploy/envs/history_wrapper.py

```
class HistoryWrapper()
    def __init__(self, env)
    def step(self, action)
    def get_observations(self)
    def get_obs(self)
    def reset_idx(self, env_ids)
    def reset(self)
    def __getattr__(self, name)

```python
def get_observations(self):
        obs = self.env.get_observations()
        privileged_obs = self.env.get_privileged_observations()
        self.obs_history = torch.cat((self.obs_history[:, self.env.num_obs:], obs), dim=-1)
        return {'obs': obs, 'privileged_obs': privileged_obs, 'obs_history': self.obs_history}
```
```

### globe_walking/go1_gym_deploy/envs/lcm_agent.py

```
def class_to_dict(obj)
class LCMAgent()
    def __init__(self, cfg, se, command_profile)
    def set_probing(self, is_currently_probing)
    def get_obs(self)
    def get_privileged_observations(self)
    def publish_action(self, action, hard_reset)
    def reset(self)
    def reset_gait_indices(self)
    def step(self, actions, hard_reset)

```python
def get_privileged_observations(self):
        return None
```
```

### globe_walking/go1_gym_deploy/scripts/deploy_policy.py

```
def run_policy(label, se, max_vel, max_yaw_vel)
def run(labels, experiment_name, max_vel, max_yaw_vel)
def load_policy(logdir)
```

### globe_walking/go1_gym_deploy/utils/network_config_unitree.py

```
def get_saved_interface_name()
def get_likely_iface()
def main()
```

### globe_walking/go1_gym_learn/env/vec_env.py

```
class VecEnv(ABC)
    def step(self, actions)
    def reset(self, env_ids)
    def get_observations(self)
    def get_privileged_observations(self)

```python
def get_observations(self) -> torch.Tensor:
        pass
```

```python
def get_privileged_observations(self) -> Union[torch.Tensor, None]:
        pass
```
```

### globe_walking/scripts/train.py

```
def train_go1(iterations, dr_config, headless, resume_path, no_wandb, wandb_group)
```