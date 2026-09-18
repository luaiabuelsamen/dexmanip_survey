# bidexhands_2022

source: https://github.com/PKU-MARL/DexterousHands


commit: dc41afd134cebfe4d80a5b861f0b8c15d734320a


## README

# Bi-DexHands: Bimanual Dexterous Manipulation via Reinforcement Learning
<img src="assets/image_folder/coverv3.jpg" width="1000" border="1"/>

****
[![PyPI](https://img.shields.io/pypi/v/bidexhands)](https://pypi.org/project/bidexhands/)
[![Organization](https://img.shields.io/badge/Organization-PKU_MARL-blue.svg "Organization")](https://github.com/PKU-MARL "Organization")
[![Unittest](https://img.shields.io/badge/Unittest-passing-green.svg "Unittest")](https://github.com/PKU-MARL "Unittest")
[![Docs](https://img.shields.io/badge/Docs-In_development-red.svg "Author")](https://github.com/PKU-MARL "Docs")
[![GitHub license](https://img.shields.io/github/license/PKU-MARL/DexterousHands)](https://github.com/PKU-MARL/DexterousHands/blob/main/LICENSE)

### Update

[2023/02/09] We re-package the Bi-DexHands. Now you can call the Bi-DexHands' environments not only on the command line, but also in your Python script. check our README [Use Bi-DexHands in Python scripts](#Use-Bi-DexHands-in-Python-scripts) below.

[2022/11/24] Now we support visual observation for all the tasks, check this [document for visual input](#./docs/visual-in.md).

[2022/10/02] Now we support for the default IsaacGymEnvs RL library [rl-games](https://github.com/Denys88/rl_games), check our README [below](#Use-rl_games-to-train-our-tasks).

**Bi-DexHands** ([click bi-dexhands.ai](https://pku-marl.github.io/DexterousHands/)) provides a collection of bimanual dexterous manipulations tasks and reinforcement learning algorithms. 
Reaching human-level sophistication of hand dexterity and bimanual coordination remains an open challenge for modern robotics researchers. To better help the community study this problem, Bi-DexHands are developed with the following key features:
- **Isaac Efficiency**: Bi-DexHands is built within [Isaac Gym](https://developer.nvidia.com/isaac-gym); it supports running thousands of environments simultaneously. For example, on one NVIDIA RTX 3090 GPU, Bi-DexHands can reach **40,000+ mean FPS** by running  2,048  environments in parallel. 
- **Comprehensive RL Benchmark**: we provide the first bimanual manipulation task environment for RL, MARL, Multi-task RL, Meta RL, and Offline RL practitioners, along with a comprehensive benchmark for SOTA continuous control model-free RL/MARL methods. See [example](./bidexhands/algorithms/marl/)
- **Heterogeneous-agents Cooperation**: Agents in Bi-DexHands (i.e., joints, fingers, hands,...) are genuinely heterogeneous; this is very different from common multi-agent environments such as [SMAC](https://github.com/oxwhirl/smac)  where agents can simply share parameters to solve the task. 
- **Task Generalization**: we introduce a variety of dexterous manipulation tasks (e.g., handover, lift up, throw, place, put...) as well as enormous target objects from the [YCB](https://rse-lab.cs.washington.edu/projects/posecnn/) and [SAPIEN](https://sapien.ucsd.edu/) dataset (>2,000 objects); this allows meta-RL and multi-task RL algorithms to be tested on the task generalization front. 
- **Point Cloud**: We provide the ability to use point clouds as observations. We used the depth camera in Isaacc Gym to get the depth image and then convert it to partial point cloud. We can customize the pose and numbers of depth cameras to get point cloud from difference angles. The density of generated point cloud depends on the number of the camera pixels. See the [visual input docs](./docs/point-cloud.md). 
- **Quick Demos**

<div align=center>
<img src="assets/image_folder/quick_demo3.gif" align="center" width="600"/>
</div> 
 

Contents of this repo are as follows:

- [Installation](#Installation)
  - [Pre-requisites](#Installation)
  <!-- - [Install from PyPI](#Install-from-PyPI) -->
  - [Install from source code](#Install-from-source-code)
- [Introduction to Bi-DexHands](#Introduction-to-Bi-DexHands)
- [Overview of Environments](./docs/environments.md)
- [Overview of Algorithms](./docs/algorithms.md)
- [Getting Started](#Getting-Started)
  - [Tasks](#Tasks)
  - [Training](#Training)
  - [Testing](#Testing)
  - [Plotting](#Plotting)
  - [Use Bi-DexHands in Python scripts](#Use-Bi-DexHands-in-Python-scripts)
- [Enviroments Performance](#Enviroments-Performance)
  - [Figures](#Figures)
- [Offline RL Datasets](#Offline-RL-Datasets)
- [Use rl_games to train our tasks](#Use-rl_games-to-train-our-tasks)
- [Future Plan](#Future-Plan)
- [Customizing your Environments](docs/customize-the-environment.md)
- [How to change the type of dexterous hand](docs/Change-the-type-of-dexterous-hand.md)
- [How to add a robotic arm drive to the dexterous hand](docs/Add-a-robotic-arm-drive-to-the-dexterous-hand.md)
- [The Team](#The-Team)
- [License](#License)
<br></br>

For more information about this work, please check [our paper.](https://arxiv.org/abs/2206.08686)

****
## Installation

Details regarding installation of IsaacGym can be found [here](https://developer.nvidia.com/isaac-gym). **We currently support the `Preview Release 3/4` version of IsaacGym.**

### Pre-requisites

The code has been tested on Ubuntu 18.04/20.04 with Python 3.7/3.8. The minimum recommended NVIDIA driver
version for Linux is `470.74` (dictated by support of IsaacGym).

It uses [Anaconda](https://www.anaconda.com/) to create virtual environments.
To install Anaconda, follow instructions [here](https://docs.anaconda.com/anaconda/install/linux/).

Ensure that Isaac Gym works on your system by running one of the examples from the `python/examples` 
directory, like `joint_monkey.py`. Please follow troubleshooting steps described in the Isaac Gym Preview Release 3/4
install instructions if you have any trouble running the samples.

Once Isaac Gym is installed and samples work within your current python environment, install this repo:

<!-- #### Install from PyPI
Bi-DexHands is hosted on PyPI. It requires Python >= 3.7.
You can simply install Bi-DexHands from PyPI with the following command:

```bash
pip install bidexhands
``` -->

#### Install from source code
You can also install this repo from the source code:

```bash
pip install -e .
```

## Introduction

This repository contains complex dexterous hands control tasks. Bi-DexHands is built in the NVIDIA Isaac Gym with high performance guarantee for training RL algorithms. Our environments focus on applying model-free RL/MARL algorithms for bimanual dexterous manipulation, which are considered as a challenging task for traditional control methods. 

## Getting Started

### <span id="task">Tasks</span>

Source code for tasks can be found in `envs/tasks`. The detailed settings of state/action/reward are in [here](./docs/environments.md).

So far, we release the following tasks (with many more to come):

| Environments | Description | Demo     |
|  :----:  | :----:  | :----:  |
|ShadowHand Over| These environments involve two fixed-position hands. The hand which starts with the object must find a way to hand it over to the second hand. | <img src="assets/image_folder/0v2.gif" width="250"/>    |
|ShadowHandCatch Underarm|These environments again have two hands, however now they have some additional degrees of freedom that allows them to translate/rotate their centre of masses within some constrained region. | <img src="assets/image_folder/hand_catch_underarmv2.gif" align="middle" width="250"/>    |
|ShadowHandCatch Over2Underarm| This environment is made up of half ShadowHandCatchUnderarm and half ShadowHandCatchOverarm, the object needs to be thrown from the vertical hand to the palm-up hand | <img src="assets/image_folder/2v2.gif" align="middle" width="250"/>    |
|ShadowHandCatch Abreast| This environment is similar to ShadowHandCatchUnderarm, the difference is that the two hands are changed from relative to side-by-side posture. | <img src="assets/image_folder/1v2.gif" align="middle" width="250"/>    |
|ShadowHandCatch TwoCatchUnderarm| These environments involve coordination between the two hands so as to throw the two objects between hands (i.e. swapping them). | <img src="assets/image_folder/two_catchv2.gif" align="middle" width="250"/>    |
|ShadowHandLift Underarm | This environment requires grasping the pot handle with two hands and lifting the pot to the designated position  | <img src="assets/image_folder/3v2.gif" align="middle" width="250"/>    |
|ShadowHandDoor OpenInward | This environment requires the closed door to be opened, and the door can only be pulled inwards | <img src="assets/image_folder/door_open_inwardv2.gif" align="middle" width="250"/>    |
|ShadowHandDoor OpenOutward | This environment requires a closed door to be opened and the door can only be pushed outwards  | <img src="assets/image_folder/open_outwardv2.gif" align="middle" width="250"/>    |
|ShadowHandDoor CloseInward | This environment requires the open door to be closed, and the door is initially open inwards | <img src="assets/image_folder/close_inwardv2.gif" align="middle" width="250"/>    |
|ShadowHand BottleCap | This environment involves two hands and a bottle, we need to hold the bottle with one hand and open the bottle cap with the other hand  | <img src="assets/image_folder/bottle_capv2.gif" align="middle" width="250"/>    |
|ShadowHandPush Block | This environment requires both hands to touch the block and push it forward | <img src="assets/image_folder/push_block.gif" align="middle" width="250"/>    |
|ShadowHandOpen Scissors | This environment requires both hands to cooperate to open the scissors | <img src="assets/image_folder/scissors.gif" align="middle" width="250"/>    |
|ShadowHandOpen PenCap | This environment requires both hands to cooperate to open the pen cap  | <img src="assets/image_folder/pen.gif" align="middle" width="250"/>    |
|ShadowHandSwing Cup | This environment requires two hands to hold the cup handle and rotate it 90 degrees | <img src="assets/image_folder/swing_cup.gif" align="middle" width="250"/>    |
|ShadowHandTurn Botton | This environment requires both hands to press the button | <img src="assets/image_folder/switch.gif" align="middle" width="250"/>    |
|ShadowHandGrasp AndPlace | This environment has a bucket and an object, we need to put the object into the bucket  | <img src="assets/image_folder/g&p.gif" align="middle" width="250"/>    |


### Training

#### Training Examples

##### RL/MARL Examples
For example, if you want to train a policy for the ShadowHandOver task by the PPO algorithm, run this line in `bidexhands` folder:

```bash
python train.py --task=ShadowHandOver --algo=ppo
```

To select an algorithm, pass `--algo=ppo/mappo/happo/hatrpo/...` 
as an argument. For example, if you want to use happo algorithm, run this line in `bidexhands` folder:

```bash
python train.py --task=ShadowHandOver --algo=happo
``` 

Supported Single-Agent RL algorithms are listed below:

- [Proximal Policy Optimization (PPO)](https://arxiv.org/pdf/1707.06347.pdf)
- [Trust Region Policy Optimization (TRPO)](https://arxiv.org/pdf/1502.05477.pdf)
- [Twin Delayed DDPG (TD3)](https://arxiv.org/pdf/1802.09477.pdf)
- [Soft Actor-Critic (SAC)](https://arxiv.org/pdf/1812.05905.pdf)
- [Deep Deterministic Policy Gradient (DDPG)](https://arxiv.org/pdf/1509.02971.pdf)

Supported Multi-Agent RL algorithms are listed below:

- [Heterogeneous-Agent Proximal Policy Optimization (HAPPO)](https://arxiv.org/pdf/2109.11251.pdf)
- [Heterogeneous-Agent Trust Region Policy Optimization (HATRPO)](https://arxiv.org/pdf/2109.11251.pdf)
- [Multi-Agent Proximal Policy Optimization (MAPPO)](https://arxiv.org/pdf/2103.01955.pdf)
- [Independent Proximal Policy Optimization (IPPO)](https://arxiv.org/pdf/2011.09533.pdf)
- [Multi-Agent Deep Deterministic Policy Gradient  (MADDPG)](https://arxiv.org/pdf/1706.02275.pdf)

##### Multi-task/Meta RL Examples

The training method of multi-task/meta RL is similar to the RL/MARL, it is only need to select the multi-task/meta categories and the corresponding algorithm. For example, if you want to train a policy for the ShadowHandMT4 categories by the MTPPO algorithm, run this line in `bidexhands` folder:

```bash
python train.py --task=ShadowHandMetaMT4 --algo=mtppo
```

Supported Multi-task RL algorithms are listed below:

- [Multi-task Proximal Policy Optimization (MTPPO)](https://arxiv.org/pdf/1707.06347.pdf)
- [Multi-task Trust Region Policy Optimization (MTTRPO)](https://arxiv.org/pdf/1502.05477.pdf)
- [Multi-task Soft Actor-Critic (MTSAC)](https://arxiv.org/pdf/1812.05905.pdf)

Supported Meta RL algorithms are listed below:

- [ProMP: Proximal Meta-Policy Search (ProMP)](https://arxiv.org/pdf/1810.06784.pdf)



#### Gym-Like API

We provide a Gym-Like API that allows us to get information from the Isaac Gym environment. Our single-agent Gym-Like wrapper is the code of the Isaac Gym team used, and we have developed a multi-agent Gym-Like wrapper based on it:

```python
class MultiVecTaskPython(MultiVecTask):
    # Get environment state information
    def get_state(self):
        return torch.clamp(self.task.states_buf, -self.clip_obs, self.clip_obs).to(self.rl_device)

    def step(self, actions):
        # Stack all agent actions in order and enter them into the environment
        a_hand_actions = actions[0]
        for i in range(1, len(actions)):
            a_hand_actions = torch.hstack((a_hand_actions, actions[i]))
        actions = a_hand_actions
        # Clip the actions
        actions_tensor = torch.clamp(actions, -self.clip_actions, self.clip_actions)
        self.task.step(actions_tensor)
        # Obtain information in the environment and distinguish the observation of different agents by hand
        obs_buf = torch.clamp(self.task.obs_buf, -self.clip_obs, self.clip_obs).to(self.rl_device)
        hand_obs = []
        hand_obs.append(torch.cat([obs_buf[:, :self.num_hand_obs], obs_buf[:, 2*self.num_hand_obs:]], dim=1))
        hand_obs.append(torch.cat([obs_buf[:, self.num_hand_obs:2*self.num_hand_obs], obs_buf[:, 2*self.num_hand_obs:]], dim=1))
        rewards = self.task.rew_buf.unsqueeze(-1).to(self.rl_device)
        dones = self.task.reset_buf.to(self.rl_device)
        # Organize information into Multi-Agent RL format
        # Refer to https://github.com/tinyzqh/light_mappo/blob/HEAD/envs/env.py
        sub_agent_obs = []
        ...
        sub_agent_done = []
        for i in range(len(self.agent_index[0] + self.agent_index[1])):
            ...
            sub_agent_done.append(dones)
        # Transpose dim-0 and dim-1 values
        obs_all = torch.transpose(torch.stack(sub_agent_obs), 1, 0)
        ...
        done_all = torch.transpose(torch.stack(sub_agent_done), 1, 0)
        return obs_all, state_all, reward_all, done_all, info_all, None

    def reset(self):
        # Use a random action as the first action after the environment reset
        actions = 0.01 * (1 - 2 * torch.rand([self.task.num_envs, self.task.num_actions * 2], dtype=torch.float32, device=self.rl_device))
        # step the simulator
        self.task.step(actions)
        # Get the observation and state buffer in the environment, the detailed are the same as step(self, actions)
        obs_buf = torch.clamp(self.task.obs_buf, -self.clip_obs, self.clip_obs)
        ...
        obs = torch.transpose(torch.stack(sub_agent_obs), 1, 0)
        state_all = torch.transpose(torch.stack(agent_state), 1, 0)
        return obs, state_all, None
```
#### RL/Multi-Agent RL API

We also provide single-agent and multi-agent RL interfaces. In order to adapt to Isaac Gym and speed up the running efficiency, all operations are implemented on GPUs using tensor. Therefore, there is no need to transfer data between the CPU and GPU.

We give an example using ***HATRPO (the SOTA MARL algorithm for cooperative tasks)*** to illustrate multi-agent RL APIs, please refer to [https://github.com/cyanrain7/TRPO-in-MARL](https://github.com/cyanrain7/TRPO-in-MARL):

```python
from algorithms.marl.hatrpo_trainer import HATRPO as TrainAlgo
from algorithms.marl.hatrpo_policy import HATRPO_Policy as Policy
...
# warmup before the main loop starts
self.warmup()
# log data
start = time.time()
episodes = int(self.num_env_steps) // self.episode_length // self.n_rollout_threads
train_episode_rewards = torch.zeros(1, self.n_rollout_threads, device=self.device)
# main loop
for episode in range(episodes):
    if self.use_linear_lr_decay:
        self.trainer.policy.lr_decay(episode, episodes)
    done_episodes_rewards = []
    for step in range(self.episode_length):
        # Sample actions
        values, actions, action_log_probs, rnn_states, rnn_states_critic = self.collect(step)
        # Obser reward and next obs
        obs, share_obs, rewards, dones, infos, _ = self.envs.step(actions)
        dones_env = torch.all(dones, dim=1)
        reward_env = torch.mean(rewards, dim=1).flatten()
        train_episode_rewards += reward_env
        # Record reward at the end of each episode
        for t in range(self.n_rollout_threads):
            if dones_env[t]:
                done_episodes_rewards.append(train_episode_rewards[:, t].clone())
                train_episode_rewards[:, t] = 0

        data = obs, share_obs, rewards, dones, infos, \
                values, actions, action_log_probs, \
                rnn_states, rnn_states_critic
        # insert data into buffer
        self.insert(data)

    # compute return and update network
    self.compute()
    train_infos = self.train()
    # post process
    total_num_steps = (episode + 1) * self.episode_length * self.n_rollout_threads
    # save model
    if (episode % self.save_interval == 0 or episode == episodes - 1):
        self.save()
```

### Testing

The trained model will be saved to `logs/${Task Name}/${Algorithm Name}`folder.

To load a trained model and only perform inference (no training), pass `--test` 
as an argument, and pass `--model_dir` to specify the trained models which you want to load.
For single-agent reinforcement learning, you need to pass `--model_dir` to specify exactly what .pt model you want to load. An example of PPO algorithm is as follows:

```bash
python train.py --task=ShadowHandOver --algo=ppo --model_dir=logs/shadow_hand_over/ppo/ppo_seed0/model_5000.pt --test
```

For multi-agent reinforcement learning, pass `--model_dir` to specify the path to the folder where all your agent model files are saved. An example of HAPPO algorithm is as follows:

```bash
python train.py --task=ShadowHandOver --algo=happo --model_dir=logs/shadow_hand_over/happo/models_seed0 --test
```

### Plotting

Users can convert all tfevent files into csv files and then try plotting the results. Note that you should verify `env-num` and `env-step` same as your experimental setting. For the details, please refer to the `./utils/logger/tools.py`.

```bash
# geenrate csv for sarl and marl algorithms
$ python ./utils/logger/tools.py --alg-name <sarl algorithm> --alg-type sarl --env-num 2048 --env-step 8 --root-dir ./logs/shadow_hand_over --refresh 
$ python ./utils/logger/tools.py --alg-name <marl algorithm> --alg-type marl --env-num 2048 --env-step 8 --root-dir ./logs/shadow_hand_over --refresh 
# generate figures
$ python ./utils/logger/plotter.py --root-dir ./logs/shadow_hand_over --shaded-std --legend-pattern "\\w+"  --output-path=./logs/shadow_hand_over/figure.png
```

### Use Bi-DexHands in Python scripts

```python
import bidexhands as bi
import torch

env_name = 'ShadowHandOver'
algo = "ppo"
env = bi.make(env_name, algo)

obs = env.reset()
terminated = False

while not terminated:
    act = torch.tensor(env.action_space.sample()).repeat((env.num_envs, 1))
    obs, reward, done, info = env.step(act)
```

## Enviroment Performance

### Figures

We provide stable and reproducible baselins run by **PPO, HAPPO, MAPPO, SAC** algorithms. All baselines are run under the parameters of `2048 num_env` and `100M total_step`. The `dataset` folder contains the raw csv files. 

<table>
    <tr>
        <th colspan="2">ShadowHandOver</th>
        <th colspan="2">ShadowHandLiftUnderarm</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/hand_over.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/over.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/lift_underarm.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/lift_underarm.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandCatchUnderarm</th>
        <th colspan="2">ShadowHandDoorOpenInward</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/catch_underarm.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/catch_underarm.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/open_inward.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/door_open_inward.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandOver2Underarm</th>
        <th colspan="2">ShadowHandDoorOpenOutward</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/catch_over2underarm.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/catch_over2underarm.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/open_outward.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/door_open_outward.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandCatchAbreast</th>
        <th colspan="2">ShadowHandDoorCloseInward</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/catch_abreast.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/catch_abreast.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/close_inward.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/door_close_inward.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandTwoCatchUnderarm</th>
        <th colspan="2">ShadowHandDoorCloseOutward</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/two_catch.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/two_catch_underarm.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/close_outward.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/door_close_outward.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandPushBlock</th>
        <th colspan="2">ShadowHandPen</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/push_block.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/push_block.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/pen_cap.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/pen.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandScissors</th>
        <th colspan="2">ShadowHandSwingCup</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/scissors.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/scissors.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/swing_cup.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/swing_cup.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandBlockStack</th>
        <th colspan="2">ShadowHandReOrientation</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/stack_block.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/block_stack.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/re_orientation.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/re_orientation.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandPourWater</th>
        <th colspan="2">ShadowHandSwitch</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/pour_water.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/pour_water.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/switch.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/switch.png" align="middle" width="750"/></td>
    <tr>
    <tr>
        <th colspan="2">ShadowHandGraspAndPlace</th>
        <th colspan="2">ShadowHandBottleCap</th>
    <tr>
    <tr>
        <td><img src="assets/image_folder/static_image/grasp_and_place.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/grasp_and_place.png" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/static_image/bottle_cap.jpg" align="middle" width="750"/></td>
        <td><img src="assets/image_folder/figures/bottle_cap.png" align="middle" width="750"/></td>
    <tr>
</table>

<!-- ## Building the Documentation

To build documentation in various formats, you will need [Sphinx](http://www.sphinx-doc.org) and the
readthedocs theme.

```bash
cd docs/
pip install -r requirements.txt
```
You can then build the documentation by running `make <format>` from the
`docs/` folder. Run `make` to get a list of all available output formats.

If you get a katex error run `npm install katex`.  If it persists, try
`npm install -g katex` -->

## Offline RL Datasets

### Data Collection

`ppo_collect` is the algo that collects offline data, which is basically the same as the mujoco data collection in d4rl. Firstly train the PPO for 5000 iterations, and collect and save the demonstration data in the first 2500 iterations:

```bash
python train.py --task=ShadowHandOver --algo=ppo_collection --num_envs=2048 --headless
```

Select model_5000.pt as the export policy to collect the expert dataset:

```bash
python3	train.py --task=ShadowHandOver --algo=ppo_collect --model_dir=./logs/shadow_hand_over/ppo_collect/ppo_collect_seed-1/model_5000.pt --test --num_envs=200 --headless
```

Similarly, select model.pt as the random policy, select a model as the medium policy, collect random data and medium data as above, and evenly sample the replay data set from the demonstration data before training to the medium policy. The size of each dataset is 10e6. Run merge.py to get the medium-expert dataset.

### Offline Data

The originally collected data in our paper is available at: 
[Shadow Hand Over](https://disk.pku.edu.cn:443/link/74F68A12FFE4A12048604CFC37A54F9C), 
[Shadow Hand Door Open Outward](https://disk.pku.edu.cn:443/link/A696D1FF69D60AC2E3E033C4567C108E).

### Use rl_games to train our tasks

**Please note that we have only test to support rl-games==1.5.2. Higher or lower version may cause an error.**

For example, if you want to train a policy for the ShadowHandOver task by the PPO algorithm, run this line in `bidexhands` folder:

```bash
python train_rlgames.py --task=ShadowHandOver --algo=ppo
```

Currently we only support PPO and PPO with LSTM methods in rl_games. If you want to use PPO with LSTM, run this line in `bidexhands` folder:

```bash
python train_rlgames.py --task=ShadowHandOver --algo=ppo_lstm
``` 

The log files using rl_games can be found in `bidexhands/runs` folder.

## Known issue

It must be pointed out that Bi-DexHands is still under development, and there are some known issue: 
- Some environments may report errors due to PhysX's collision calculation bugs in the later stage of program runtime.
```
RuntimeError: CUDA error: an illegal memory access was encountered
CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
```
- Although we provide the implementation, we did not tested **DDPG**, **TD3**, and **MADDPG** algorithms, they may still have bugs.

## Future Plan
 - [x] Success Metric for all tasks
 - [ ] Add fatory environment (see [this](https://sites.google.com/nvidia.com/factory))
 - [x] Add support for the default IsaacGymEnvs RL library [rl-games](https://github.com/Denys88/rl_games)

## Citation
Please cite as following if you think this work is helpful for you:
```
@inproceedings{
chen2022towards,
title={Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning},
author={Yuanpei Chen and Yaodong Yang and Tianhao Wu and Shengjie Wang and Xidong Feng and Jiechuan Jiang and Zongqing Lu and Stephen Marcus McAleer and Hao Dong and Song-Chun Zhu},
booktitle={Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
year={2022},
url={https://openreview.net/forum?id=D29JbExncTP}
}
```

## The Team

Bi-DexHands is a project contributed by [Yuanpei Chen](https://github.com/cypypccpy), [Yaodong Yang](https://www.yangyaodong.com/), [Tianhao Wu](https://tianhaowuhz.github.io/), [Shengjie Wang](https://github.com/Shengjie-bob), [Xidong Feng](https://github.com/waterhorse1), [Jiechuang Jiang](https://github.com/jiechuanjiang), [Hao Dong](https://zsdonghao.github.io), [Zongqing Lu](https://z0ngqing.github.io), [Song-chun Zhu](http://www.stat.ucla.edu/~sczhu/) at Peking University, please contact yaodong.yang@pku.edu.cn if you are interested to collaborate.


We also thank the list of contributors from the following two open source repositories: 
[Isaac Gym](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs), [HATRPO](https://github.com/cyanrain7/TRPO-in-MARL).

We also recommend users to read [the early work](htt

## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
bidexhands/
  __init__.py
  algorithms/
    __init__.py
    marl/
    metarl/
    mtrl/
    offrl/
    rl/
    utils/
  cfg/
    AllegroHandCatchUnderarm.yaml
    AllegroHandOver.yaml
    ShadowHandBlockStack.yaml
    ShadowHandBottleCap.yaml
    ShadowHandCatchAbreast.yaml
    ShadowHandCatchOver2Underarm.yaml
    ShadowHandCatchUnderarm.yaml
    ShadowHandDoorCloseInward.yaml
    ShadowHandDoorCloseOutward.yaml
    ShadowHandDoorOpenInward.yaml
    ShadowHandDoorOpenOutward.yaml
    ShadowHandGraspAndPlace.yaml
    ShadowHandKettle.yaml
    ShadowHandLiftUnderarm.yaml
    ShadowHandOver.yaml
    ShadowHandPen.yaml
    ShadowHandPushBlock.yaml
    ShadowHandReOrientation.yaml
    ShadowHandScissors.yaml
    ShadowHandSwingCup.yaml
    ShadowHandSwitch.yaml
    ShadowHandTwoCatchUnderarm.yaml
    bcq/
    ddpg/
    happo/
    hatrpo/
    ippo/
    iql/
    maddpg/
    mamlppo/
    mappo/
    meta_env_cfg/
    mtppo/
    mtsac/
    mttrpo/
    ppo/
    ppo_collect/
    random/
    sac/
    td3/
    td3_bc/
    trpo/
  scripts/
    run_experiments.sh
  tasks/
    __init__.py
    allegro_hand_catch_underarm.py
    allegro_hand_over.py
    hand_base/
    shadow_hand_block_stack.py
    shadow_hand_bottle_cap.py
    shadow_hand_catch_abreast.py
    shadow_hand_catch_over2underarm.py
    shadow_hand_catch_underarm.py
    shadow_hand_door_close_inward.py
    shadow_hand_door_close_outward.py
    shadow_hand_door_open_inward.py
    shadow_hand_door_open_outward.py
    shadow_hand_grasp_and_place.py
    shadow_hand_kettle.py
    shadow_hand_lift_underarm.py
    shadow_hand_meta/
    shadow_hand_over.py
    shadow_hand_pen.py
    shadow_hand_point_cloud.py
    shadow_hand_push_block.py
    shadow_hand_re_orientation.py
    shadow_hand_scissors.py
    shadow_hand_swing_cup.py
    shadow_hand_switch.py
    shadow_hand_two_catch_underarm.py
  train.py
  train_customize.py
  train_rlgames.py
  utils/
    __init__.py
    config.py
    logger/
    o3dviewer.py
    package_utils.py
    parse_task.py
    process_marl.py
    process_metarl.py
    process_mtrl.py
    process_offrl.py
    process_sarl.py
    torch_jit_utils.py
    util.py
dataset/
  shadow_hand_catch_abreast/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_catch_over2underarm/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_catch_underarm/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_door_close_inward/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_door_close_outward/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_door_open_inward/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_door_open_outward/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_over/
    figure.png
    happo/
    mappo/
    ppo/
  shadow_hand_two_catch_underarm/
    figure.png
    happo/
    mappo/
    ppo/
requirements.txt
setup.py
```

## Config files (57)


### bidexhands/cfg/AllegroHandCatchUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_catch_underarm"
  numEnvs: 8
  envSpacing: 1.25
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/AllegroHandOver.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_over"
  numEnvs: 8
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandBlockStack.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_block_stack"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  transition_scale: 0.2
  orientation_scale: 0.02
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandBottleCap.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 125
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/ShadowHandCatchAbreast.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_abreast"
  numEnvs: 256
  envSpacing: 0.75
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  resetDofPosRandomInterval: 0.
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  transition_scale: 0.5
  orientation_scale: 1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.65
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandCatchOver2Underarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_over2underarm"
  numEnvs: 256
  envSpacing: 1
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  resetDofPosRandomInterval: 0.
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 2
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 2
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandCatchUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_underarm"
  numEnvs: 256
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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

  distRewardScale: 50
  transition_scale: 0.05
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.65
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandDoorCloseInward.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_door_close_inward"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandDoorCloseOutward.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_door_close_outward"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandDoorOpenInward.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_door_open_inward"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandDoorOpenOutward.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_door_open_outward"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandGraspAndPlace.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_grasp_and_place"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 500
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandKettle.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_kettle"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 125
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/ShadowHandLiftUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_lift_underarm"
  numEnvs: 128
  envSpacing: 0.75
  episodeLength: 500
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  transition_scale: 0.25
  orientation_scale: 1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/ShadowHandOver.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_over"
  numEnvs: 128
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandPen.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_pen"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 125
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/ShadowHandPushBlock.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_push_block"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 125
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandReOrientation.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_re_orientation"
  numEnvs: 128
  envSpacing: 0.75
  episodeLength: 600
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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

  distRewardScale: -10
  transition_scale: 0.05
  orientation_scale: 0.5

  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 500
  fallDistance: 0.24
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandScissors.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_scissors"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandSwingCup.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_swing_cup"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 300
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 5.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/ShadowHandSwitch.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_switch"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 125
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/ShadowHandTwoCatchUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_two_catch_underarm"
  numEnvs: 128
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

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

  distRewardScale: 50.0
  transition_scale: 0.05
  orientation_scale: 0.5

  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.65
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # full_state or point_cloud
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/bcq/config.yaml

```yaml
seed: -1

learn:
  agent_name: shadow_hand
  max_timesteps: 1000000
  batch_size: 100
  phi: 0.05
  lmbda: 0.75
  discount: 0.99
  tau: 0.005
  iterations: 10000
  test : False
  max_iterations: 10000
  save_interval : 10000
```

### bidexhands/cfg/ddpg/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0


learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 2500

  # training params
  hidden_nodes: 256
  hidden_layer: 3

  cliprange: 0.2
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent #TODO: too small
  replay_size: 10000
  polyak: 0.995
  learning_rate: 0.0001
  max_grad_norm: 1
  gamma: 0.99
  act_noise: 0.1
  target_noise: 0.2
  noise_clip: 0.5
  reward_scale: 1
  batch_size: 64

  log_interval: 1
  asymmetric: False

```

### bidexhands/cfg/happo/config.yaml

```yaml
env_name: happo
algorithm_name: happo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False

num_env_steps: 50000000

episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: True
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/happo/lift_config.yaml

```yaml
env_name: happo
algorithm_name: happo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False

num_env_steps: 30000000

episode_length: 20
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: True
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/happo/stack_block_config.yaml

```yaml
env_name: happo
algorithm_name: happo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False

num_env_steps: 50000000

episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: True
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/hatrpo/config.yaml

```yaml
env_name: hatrpo
algorithm_name: hatrpo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False
num_env_steps: 100000000
episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: True
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/ippo/config.yaml

```yaml
env_name: ippo
algorithm_name: ippo
experiment_name: check
run_dir: ./logs
use_centralized_V: False # false in IPPO
use_obs_instead_of_state: False
num_env_steps: 100000000
episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: False  # false in IPPO
use_valuenorm: True
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length:
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False  # false in IPPO
use_policy_active_masks: False  # false in IPPO

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/iql/config.yaml

```yaml
seed: -1

learn:
  agent_name: shadow_hand
  max_timesteps: 1000000
  batch_size: 256
  expectile: 0.7
  beta: 3.0
  scale: 25.0
  discount: 0.99
  tau: 0.005
  iterations: 10000
  test : False
  max_iterations: 10000
  save_interval : 10000
```

### bidexhands/cfg/maddpg/config.yaml

```yaml
env_name: maddpg
algorithm_name: maddpg
experiment_name: check
run_dir: ./logs
num_env_steps: 50000000
episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: [1024, 1024, 512]
activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
use_render: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000


# rollout params
max_iterations: 1000000

# ddpg 参数
cliprange: 0.2
nsteps: 8
noptepochs: 5
num_mini_batch: 1 # this is per agent #TODO: too small
num_learning_epochs: 50
replay_size: 100
batch_size: 16
polyak: 0.995
learning_rate: 0.001
max_grad_norm: 1
gamma: 0.99
act_noise: 0.1
target_noise: 0.2
noise_clip: 0.5
sampler: random
```

### bidexhands/cfg/mamlppo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [2048, 1024, 512]
  vf_hid_sizes: [2048, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 2000

  # training params
  cliprange: 0.2
  ent_coef: 0
  nsteps: 8
  noptepochs: 1
  nminibatches: 1 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: fixed # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.9
  lam: 0.95
  init_noise_std: 1

  log_interval: 1
  asymmetric: False
```

### bidexhands/cfg/mappo/config.yaml

```yaml
env_name: mappo
algorithm_name: mappo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False
num_env_steps: 100000000
episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: False
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/mappo/lift_config.yaml

```yaml
env_name: mappo
algorithm_name: mappo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False

num_env_steps: 30000000

episode_length: 20
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: False
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5

```

### bidexhands/cfg/mappo/stack_block_config.yaml

```yaml
env_name: mappo
algorithm_name: mappo
experiment_name: check
run_dir: ./logs
use_centralized_V: True
use_obs_instead_of_state: False
num_env_steps: 100000000
episode_length: 8
n_rollout_threads: 80
n_eval_rollout_threads: 1
use_linear_lr_decay: False
hidden_size: 512
use_render: False
recurrent_N: 1
use_single_network: False

save_interval: 1
use_eval: False
eval_interval: 25
log_interval: 25
eval_episodes: 10000

gamma: 0.96
gae_lambda: 0.95
use_gae: True
use_popart: True
use_valuenorm: False
use_proper_time_limits: False

kl_threshold: 0.016
ls_step: 10
accept_ratio: 0.5
clip_param: 0.2
ppo_epoch: 5
num_mini_batch: 1
data_chunk_length: 
value_loss_coef: 1
entropy_coef: 0.0
max_grad_norm: 10
huber_delta: 10.0
use_recurrent_policy: False
use_naive_recurrent_policy: False
use_max_grad_norm: True
use_clipped_value_loss: True
use_huber_loss: True
use_value_active_masks: False
use_policy_active_masks: False

lr: 5.e-4
critic_lr: 5.e-4
opti_eps: 1.e-5
weight_decay: 0.0

gain: 0.01
actor_gain: 0.01
use_orthogonal: True

use_feature_normalization: True
use_ReLU: True
stacked_frames: 1
layer_N: 2

std_x_coef: 1
std_y_coef: 0.5
```

### bidexhands/cfg/meta_env_cfg/ShadowHandMetaML1.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_meta_ml1"
  numEnvs: 64
  envSpacing: 1.
  episodeLength: 75
  enableDebugVis: False
  aggregateMode: 0

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

  distRewardScale: 50
  transition_scale: 0.05
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 0
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/meta_env_cfg/ShadowHandMetaMT1.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_meta_mt1"
  numEnvs: 128
  envSpacing: 1.
  episodeLength: 75
  enableDebugVis: False
  aggregateMode: 0

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

  distRewardScale: 50
  transition_scale: 0.05
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 0
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/meta_env_cfg/ShadowHandMetaMT20.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_meta_mt20"
  numEnvs: 2
  envSpacing: 1.
  episodeLength: 100
  enableDebugVis: True
  aggregateMode: 0

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.00
  startRotationNoise: 0.0

  resetPositionNoise: 0.00
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  transition_scale: 0.1
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 0
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
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

### bidexhands/cfg/meta_env_cfg/ShadowHandMetaMT4.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_meta_mt4"
  numEnvs: 64
  envSpacing: 1.
  episodeLength: 75
  enableDebugVis: False
  aggregateMode: 0

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

  distRewardScale: 50
  transition_scale: 0.05
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 0
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/meta_env_cfg/shadow_hand_meta.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_meta"
  numEnvs: 16
  envSpacing: 1.
  episodeLength: 75
  enableDebugVis: False
  aggregateMode: 0

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.00
  startRotationNoise: 0.0

  resetPositionNoise: 0.00
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  transition_scale: 0.25
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
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
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
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
      hand:
        color: True
        tendon_properties:
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
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
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
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
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

### bidexhands/cfg/mtppo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [2048, 1024, 512]
  vf_hid_sizes: [2048, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
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

### bidexhands/cfg/mtsac/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

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

### bidexhands/cfg/mttrpo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

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

### bidexhands/cfg/ppo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

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

### bidexhands/cfg/ppo/humanoid_config.yaml

```yaml
seed: -1
policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024,1024]
  vf_hid_sizes: [1024, 1024,1024]
  activation: selu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: humanoid_ppo
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 5000

  # training params
  cliprange: 0.1
  ent_coef: 0
  nsteps: 32
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1.0
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.01
  gamma: 0.99
  lam: 0.95
  init_noise_std: 1.0

  log_interval: 1
```

### bidexhands/cfg/ppo/lift_config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 512, 512]
  vf_hid_sizes: [1024, 512, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6501

  # training params
  cliprange: 0.2
  ent_coef: 0
  nsteps: 20
  noptepochs: 10
  nminibatches: 4 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.998
  lam: 0.95
  init_noise_std: 1.0

  log_interval: 1
  asymmetric: False
```

### bidexhands/cfg/ppo/ppo_continuous.yaml

```yaml
params:  
  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: True
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
          scale: 0.02
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [512, 256, 128]
      activation: elu
      initializer:
        name: default
      regularizer:
        name: None #'l2_regularizer'
        #scale: 0.001

  load_checkpoint: False
  load_path: path

  config:
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.96
    tau: 0.95

    learning_rate: 3e-4
    name: allegro
    score_to_win: 100000

    grad_norm: 1
    entropy_coef: 0.0
    truncate_grads: True
    env_name: openai_gym
    e_clip: 0.2
    clip_value: True
    num_agent: 1
    horizon_length: 8
    minibatch_size: 4
    mini_epochs: 5
    critic_coef: 1
    lr_schedule:  adaptive
    kl_threshold: 0.016

    max_epochs: 6104
    save_frequency: 200
    save_best_after: 1000
    games_to_track: 8
    
    normalize_input: False
    seq_length: 4
    bounds_loss_coef: 0.001
    env_config:
      seed: 42


```

### bidexhands/cfg/ppo/ppo_continuous_lstm.yaml

```yaml
params:  
  seed: 8
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
      units: [1024, 1024]
      d2rl: False
      activation: elu
      initializer:
        name: default
    rnn:
      name: 'lstm'
      units: 512
      layers: 1
      before_mlp: False
      concat_input: True
      #layer_norm: True

  config:
    env_name: BipedalWalker-v3
    name: walker_rnn
    reward_shaper:
      min_val: -1
      scale_value: 1

    normalize_advantage: True
    gamma: 0.96
    tau: 0.95
    learning_rate: 3e-4
    lr_schedule: adaptive
    kl_threshold: 0.016
    save_best_after: 10
    score_to_win: 300
    grad_norm: 1
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    clip_value: True
    num_agent: 1
    horizon_length: 8
    minibatch_size: 4
    mini_epochs: 5
    critic_coef: 1
    normalize_input: True
    bound_loss_type: regularisation
    bounds_loss_coef: 0.001
    max_epochs: 6104
    seq_length: 4
    normalize_value: True
    use_diagnostics: True
    value_bootstrap: True
    weight_decay: 0.0001
    use_smooth_clamp: True

    env_config:
      name: BipedalWalker-v3
```

### bidexhands/cfg/ppo/re_orientation_config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512, 256]
  vf_hid_sizes: [1024, 1024, 512, 256]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

  # training params
  cliprange: 0.2
  ent_coef: 0
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 5.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.99
  lam: 0.95
  init_noise_std: 1.0

  log_interval: 1
  asymmetric: False
```

### bidexhands/cfg/ppo/stack_block_config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

  # training params
  cliprange: 0.2
  ent_coef: 0
  nsteps: 8
  noptepochs: 2
  nminibatches: 8 # this is per agent
  max_grad_norm: 1
  optim_stepsize: 3.e-4 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  desired_kl: 0.016
  gamma: 0.9
  lam: 0.95
  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False
```

### bidexhands/cfg/ppo_collect/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 5000

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
  gamma: 0.99
  lam: 0.95
  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False

  data_size: 1000000
```

### bidexhands/cfg/random/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [2048, 1024, 512]
  vf_hid_sizes: [2048, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
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

### bidexhands/cfg/sac/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0


learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6500

  # training params
  hidden_nodes: 1024
  hidden_layer: 3

  cliprange: 0.2
  nsteps: 8
  noptepochs: 1
  nminibatches: 4 # this is per agent
  replay_size: 5000
  polyak: 0.99
  learning_rate: 0.0003
  max_grad_norm: 1
  ent_coef: 0.2
  reward_scale: 1
  batch_size: 32
#  optim_stepsize: 1.e-3 # 3e-4 is default for single agent training with constant schedule
#  schedule: adaptive # could be adaptive or linear or fixed
#  desired_kl: 0.016
  gamma: 0.99
#  lam: 0.95
#  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False

```

### bidexhands/cfg/sac/humanoid_config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0


learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 5000

  # training params
  hidden_nodes: 1024
  hidden_layer: 3

  cliprange: 0.2
  nsteps: 32
  noptepochs: 1
  nminibatches: 1 # this is per agent
  replay_size: 40000
  polyak: 0.995
  learning_rate: 0.001
  max_grad_norm: 1
  ent_coef: 0.2
  reward_scale: 1
  batch_size: 64
#  optim_stepsize: 1.e-3 # 3e-4 is default for single agent training with constant schedule
#  schedule: adaptive # could be adaptive or linear or fixed
#  desired_kl: 0.016
  gamma: 0.99
#  lam: 0.95
#  init_noise_std: 0.8

  log_interval: 1
  asymmetric: False

```

### bidexhands/cfg/td3/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0


learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 200 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 2500

  # training params
  hidden_nodes: 256
  hidden_layer: 3

  cliprange: 0.2
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  replay_size: 100
  polyak: 0.995
  learning_rate: 0.0001
  max_grad_norm: 1
  policy_delay: 2
  gamma: 0.99
  act_noise: 0.1
  target_noise: 0.2
  noise_clip: 0.5
  reward_scale: 1
  batch_size: 64
  
  log_interval: 1
  asymmetric: False

```

### bidexhands/cfg/td3_bc/config.yaml

```yaml
seed: -1

learn:
  agent_name: shadow_hand
  max_timesteps: 1000000
  batch_size: 256
  policy_freq: 2
  alpha: 0.2 #2.5
  discount: 0.99
  tau: 0.005
  iterations: 10000
  test : False
  max_iterations: 10000
  save_interval : 10000
```

### bidexhands/cfg/trpo/config.yaml

```yaml
seed: -1

clip_observations: 5.0
clip_actions: 1.0

policy: # only works for MlpPolicy right now
  pi_hid_sizes: [1024, 1024, 512]
  vf_hid_sizes: [1024, 1024, 512]
  activation: elu # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
learn:
  agent_name: shadow_hand
  test: False
  resume: 0
  save_interval: 1000 # check for potential saves every this many iterations
  print_log: True

  # rollout params
  max_iterations: 6104

  # training params
  cliprange: 0.2
  nsteps: 8
  noptepochs: 5
  nminibatches: 4 # this is per agent
  max_grad_norm: 10
  optim_stepsize: 1.e-3 # 3e-4 is default for single agent training with constant schedule
  schedule: adaptive # could be adaptive or linear or fixed
  gamma: 0.99
  lam: 0.95
  init_noise_std: 0.8
  value_loss_coef: 2.0

  # optimize the actor
  damping: 0.1
  cg_nsteps: 3
  max_kl: 0.1
  max_num_backtrack: 10
  accept_ratio: 0.01
  step_fraction: 0.1

  log_interval: 1
  asymmetric: False


```

## Python signatures and reward/observation bodies (137 files)


### bidexhands/algorithms/marl/actor_critic.py

```
class Actor(Module)
    """Actor network class for HAPPO. Outputs actions given observations.
:param args: (argparse.Namespace) arguments containing relevant model information.
:param obs_space: (gym.Space) observation space.
:param action_space: (gym.Space) action space.
:param device: (torch.device) specifies the device to """
    def __init__(self, config, obs_space, action_space, device)
    def forward(self, obs, rnn_states, masks, available_actions, deterministic)
    def evaluate_actions(self, obs, rnn_states, action, masks, available_actions, active_masks)
class Critic(Module)
    """Critic network class for HAPPO. Outputs value function predictions given centralized input (HAPPO) or local observations (IPPO).
:param args: (argparse.Namespace) arguments containing relevant model information.
:param cent_obs_space: (gym.Space) (centralized) observation space.
:param device: (torc"""
    def __init__(self, config, cent_obs_space, device)
    def forward(self, cent_obs, rnn_states, masks)
```

### bidexhands/algorithms/marl/happo_policy.py

```
class HAPPO_Policy()
    """HAPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function in"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/happo_trainer.py

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

### bidexhands/algorithms/marl/hatrpo_policy.py

```
class HATRPO_Policy()
    """HATRPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function i"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/hatrpo_trainer.py

```
class HATRPO()
    """Trainer class for MATRPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (HATRPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def flat_grad(self, grads)
    def flat_hessian(self, hessians)
    def flat_params(self, model)
    def update_model(self, model, new_params)
    def kl_approx(self, q, p)
    def kl_divergence(self, obs, rnn_states, action, masks, available_actions, active_masks, new_actor, old_actor)
    def conjugate_gradient(self, actor, obs, rnn_states, action, masks, available_actions, active_masks, b, nsteps, residual_tol)
    def fisher_vector_product(self, actor, obs, rnn_states, action, masks, available_actions, active_masks, p)
    def trpo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/ippo_policy.py

```
"""# @Time    : 2021/7/1 6:53 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : rMAPPOPolicy.py
refer to ....."""
class IPPO_Policy()
    """IPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function inp"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/ippo_trainer.py

```
"""# @Time    : 2021/7/1 6:52 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : r_mappo.py"""
class IPPO()
    """Trainer class for IPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (IPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/maddpg/module.py

```
def get_activation(act_name)
def mlp(sizes, activation, output_activation)
class MLPActLayer(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class Actor(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation, device)
    def act(self, obs)
class Critic(Module)
    def __init__(self, share_observation_space, share_action_space, hidden_sizes, activation, device)
    def get_value(self, share_obs, share_acts)
class MADDPG_policy()
    def __init__(self, config, obs_space, cent_obs_space, act_space, cent_act_space, device)
    def get_actions(self, obs, deterministic)
    def get_values(self, cent_obs, cent_acts)
    def act(self, obs, deterministic)
class MADDPG()
    def __init__(self, config, policy, num_agents, device)
    def cal_value_loss(self, data, nid)
    def cal_pi_loss(self, data, id)
    def ddpg_update(self, samples)
    def train(self, buffer)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/maddpg/runner.py

```
def _t2n(x)
class Runner()
    def __init__(self, vec_env, config, model_dir)
    def run(self)
    def collect(self, step)
    def insert(self, data)
    def log_train(self, train_infos, total_num_steps)
    def train(self)
    def save(self)
    def restore(self)
    def log_train(self, train_infos, total_num_steps)
    def log_env(self, env_infos, total_num_steps)
    def eval(self, total_num_steps)
```

### bidexhands/algorithms/marl/maddpg/storage.py

```
class ReplayBuffer()
    def __init__(self, config, obs_shape, share_obs_shape, actions_shape, joint_actions_shape, device)
    def add_transitions(self, observations, share_obs, actions, joint_actions, rewards, next_obs, next_state, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/marl/mappo_policy.py

```
"""# @Time    : 2021/7/1 6:53 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : rMAPPOPolicy.py"""
class MAPPO_Policy()
    """MAPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function in"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/mappo_trainer.py

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

### bidexhands/algorithms/marl/runner.py

```
def _t2n(x)
class Runner()
    def __init__(self, vec_env, config, model_dir)
    def run(self)
    def warmup(self)
    def collect(self, step)
    def insert(self, data)
    def log_train(self, train_infos, total_num_steps)
    def train(self)
    def save(self)
    def restore(self)
    def log_train(self, train_infos, total_num_steps)
    def log_env(self, env_infos, total_num_steps)
    def eval(self, total_num_steps)
    def compute(self)
```

### bidexhands/algorithms/marl/utils/multi_discrete.py

```
class MultiDiscrete(Space)
    """- The multi-discrete action space consists of a series of discrete action spaces with different parameters
- It can be adapted to both a Discrete action space or a continuous (Box) action space
- It is useful to represent game controllers or keyboards where each key can be represented as a discrete """
    def __init__(self, array_of_param_array)
    def sample(self)
    def contains(self, x)
    def shape(self)
    def __repr__(self)
    def __eq__(self, other)
```

### bidexhands/algorithms/marl/utils/popart.py

```
class PopArt(Module)
    """Normalize a vector of observations - across the first norm_axes dimensions"""
    def __init__(self, input_shape, norm_axes, beta, per_element_update, epsilon, device)
    def reset_parameters(self)
    def running_mean_var(self)
    def forward(self, input_vector, train)
    def denormalize(self, input_vector)
```

### bidexhands/algorithms/marl/utils/separated_buffer.py

```
def _flatten(T, N, x)
def _cast(x)
class SeparatedReplayBuffer(object)
    def __init__(self, config, obs_space, share_obs_space, act_space, device)
    def update_factor(self, factor)
    def insert(self, share_obs, obs, rnn_states, rnn_states_critic, actions, action_log_probs, value_preds, rewards, masks, bad_masks, active_masks, available_actions)
    def chooseinsert(self, share_obs, obs, rnn_states, rnn_states_critic, actions, action_log_probs, value_preds, rewards, masks, bad_masks, active_masks, available_actions)
    def after_update(self)
    def chooseafter_update(self)
    def compute_returns(self, next_value, value_normalizer)
    def feed_forward_generator(self, advantages, num_mini_batch, mini_batch_size)
    def naive_recurrent_generator(self, advantages, num_mini_batch)
    def recurrent_generator(self, advantages, num_mini_batch, data_chunk_length)
```

### bidexhands/algorithms/marl/utils/util.py

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

### bidexhands/algorithms/marl/utils/valuenorm.py

```
class ValueNorm(Module)
    """Normalize a vector of observations - across the first norm_axes dimensions"""
    def __init__(self, input_shape, norm_axes, beta, per_element_update, epsilon, device)
    def reset_parameters(self)
    def running_mean_var(self)
    def update(self, input_vector)
    def normalize(self, input_vector)
    def denormalize(self, input_vector)
```

### bidexhands/algorithms/metarl/maml/maml.py

```
class Trainer()
    def __init__(self, inner_algo, meta_actor_critic, vec_env, learning_rate, sampler, asymmetric)
    def train(self, train_epoch)
    def sample_batch_task(self, task_size)
    def meta_update(self, support_storage_list, query_storage_list)
    def inner_update(self, support_storage, i)
```

### bidexhands/algorithms/metarl/maml/mamlppo.py

```
class MAMLPPO()
    def __init__(self, vec_env, pseudo_actor_critic, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def sample_support_trajectory(self, support_set_size, log_interval)
    def sample_query_trajectory(self, query_set_size, meta_storage)
    def log(self, locs, width, pad, query)
    def update(self)
```

### bidexhands/algorithms/metarl/maml/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/metarl/maml/storage.py

```
class RolloutStorage(object)
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mtppo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/mtrl/mtppo/mtppo.py

```
class PPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, random)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/mtrl/mtppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mtsac/module.py

```
def mlp(sizes, activation, output_activation)
class SquashedGaussianMLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs, deterministic, with_logprob, epsilon)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/mtrl/mtsac/mtsac.py

```
def count_vars(module)
class SAC()
    def __init__(self, vec_env, actor_critic, ac_kwargs, num_transitions_per_env, num_learning_epochs, num_mini_batches, replay_size, gamma, polyak, learning_rate, max_grad_norm, entropy_coef, use_clipped_value_loss, reward_scale, batch_size, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/mtrl/mtsac/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mttrpo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/mtrl/mttrpo/mttrpo.py

```
class TRPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, damping, cg_nsteps, max_kl, max_num_backtrack, accept_ratio, step_fraction, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def conjugate_gradient(self, Av, b, nsteps, residual_tol)
    def line_search(self, evaluate_policy, full_step, old_actions_log_prob_batch, grad, max_num_backtrack, accept_ratio, step_fraction)
    def kl_hessian_times_vector(self, v, kl)
    def set_pi_flat_params(self, flat_params)
    def get_pi_flat_params(self)
    def get_aloss_logp(self, obs_batch, states_batch, actions_batch, advantages_batch, old_actions_log_prob_batch)
```

### bidexhands/algorithms/mtrl/mttrpo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/offrl/bcq/bcq.py

```
class BCQ()
    def __init__(self, vec_env, device, discount, tau, lmbda, phi, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/offrl/bcq/module.py

```
class Actor(Module)
    def __init__(self, state_dim, action_dim, max_action, phi)
    def forward(self, state, action)
class Critic(Module)
    def __init__(self, state_dim, action_dim)
    def forward(self, state, action)
    def q1(self, state, action)
class VAE(Module)
    def __init__(self, state_dim, action_dim, latent_dim, max_action, device)
    def forward(self, state, action)
    def decode(self, state, z)
class BCQ_Model(object)
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, lmbda, phi)
    def select_action(self, state)
    def train(self, replay_buffer, iterations, batch_size)
```

### bidexhands/algorithms/offrl/bcq/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/iql/iql.py

```
class IQL()
    def __init__(self, vec_env, device, discount, tau, expectile, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/offrl/iql/module.py

```
class TDNetwork(Module)
    def __init__(self, state_dim, action_dim, net_type)
    def forward(self, x)
class Policy(Module)
    def __init__(self, state_dim, action_dim, max_action)
    def forward_dist(self, states)
class IQL_Model()
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, expectile, beta)
    def expectile_loss(self, value, expectile_prediction)
    def square_loss(self, value, mean_prediction)
    def L_V(self, states, actions)
    def L_Q(self, q_net, states, actions, rewards, next_states, terminals)
    def target_update(self)
    def TD_networks_update(self, states, actions, rewards, next_states, terminals)
    def L_pi(self, states, actions)
    def policy_update(self, states, actions)
    def select_action(self, state)
    def train(self, replay_buffer, interaction, batch_size)
```

### bidexhands/algorithms/offrl/iql/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/ppo_collect/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/offrl/ppo_collect/ppo_collect.py

```
class PPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, data_size)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/offrl/ppo_collect/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/offrl/td3_bc/module.py

```
class Actor(Module)
    def __init__(self, state_dim, action_dim, max_action)
    def forward(self, state)
class Critic(Module)
    def __init__(self, state_dim, action_dim)
    def forward(self, state, action)
    def Q1(self, state, action)
class TD3_BC_Model(object)
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, policy_noise, noise_clip, policy_freq, alpha)
    def select_action(self, state)
    def train(self, replay_buffer, interaction, batch_size)
```

### bidexhands/algorithms/offrl/td3_bc/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/td3_bc/td3_bc.py

```
class TD3_BC()
    def __init__(self, vec_env, device, discount, tau, alpha, policy_freq, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/rl/ddpg/ddpg.py

```
def count_vars(module)
class DDPG()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/ddpg/module.py

```
def mlp(sizes, activation, output_activation)
class MLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, act_noise, device, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/ddpg/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/ppo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/rl/ppo/ppo.py

```
class PPO()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/rl/ppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/sac/module.py

```
def mlp(sizes, activation, output_activation)
class SquashedGaussianMLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs, deterministic, with_logprob, epsilon)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/sac/sac.py

```
def count_vars(module)
class SAC()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/sac/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/td3/module.py

```
def mlp(sizes, activation, output_activation)
class MLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, act_noise, device, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/td3/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/td3/td3.py

```
def count_vars(module)
class TD3()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/trpo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/rl/trpo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/trpo/trpo.py

```
class TRPO()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def conjugate_gradient(self, Av, b, nsteps, residual_tol)
    def line_search(self, evaluate_policy, full_step, old_actions_log_prob_batch, grad, max_num_backtrack, accept_ratio, step_fraction)
    def kl_hessian_times_vector(self, v, kl)
    def set_pi_flat_params(self, flat_params)
    def get_pi_flat_params(self)
    def get_aloss_logp(self, obs_batch, states_batch, actions_batch, advantages_batch, old_actions_log_prob_batch)
```

### bidexhands/algorithms/utils/act.py

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

### bidexhands/algorithms/utils/cnn.py

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

### bidexhands/algorithms/utils/distributions.py

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

### bidexhands/algorithms/utils/mlp.py

```
class MLPLayer(Module)
    def __init__(self, input_dim, hidden_size, layer_N, use_orthogonal, use_ReLU)
    def forward(self, x)
class MLPBase(Module)
    def __init__(self, config, obs_shape, cat_self, attn_internal)
    def forward(self, x)
```

### bidexhands/algorithms/utils/rnn.py

```
class RNNLayer(Module)
    def __init__(self, inputs_dim, outputs_dim, recurrent_N, use_orthogonal)
    def forward(self, x, hxs, masks)
```

### bidexhands/algorithms/utils/util.py

```
def init(module, weight_init, bias_init, gain)
def get_clones(module, N)
def check(input)
```

### bidexhands/tasks/allegro_hand_catch_underarm.py

```
class AllegroHandCatchUnderarm(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, allegro_left_hand_pos, allegro_right_hand_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, allegro_left_hand_pos, allegro_right_hand_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.1, torch.ones_like(reset_buf), reset_buf)
    resets = torch.where(allegro_right_hand_pos[:, 1] <= -0.8, torch.ones_like(resets), resets)

    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, successes, cons_successes
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.allegro_left_hand_pos, self.allegro_right_hand_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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

        self.allegro_right_hand_pos = self.rigid_body_states[:, 6, 0:3]
        self.allegro_right_hand_rot = self.rigid_body_states[:, 6, 3:7]

        self.allegro_left_hand_pos = self.rigid_body_states[:, 6 + 23, 0:3]
        self.allegro_left_hand_rot = self.rigid_body_states[:, 6 + 23, 3:7]

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
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_over.py

```
class AllegroHandOver(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
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
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

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

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/hand_base/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors, is_meta, task_num)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions)
    def get_states(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### bidexhands/tasks/hand_base/meta_vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def uniform_random_strategy(self, num_tasks, _)
    def round_robin_strategy(self, num_tasks, last_task)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MetaVecTaskPython(VecTask)
    def set_task(self, task)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _active_task_one_hot(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/multi_task_vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def uniform_random_strategy(self, num_tasks, _)
    def round_robin_strategy(self, num_tasks, last_task)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MultiTaskVecTaskPython(VecTask)
    def set_task(self, task)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _active_task_one_hot(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/multi_vec_task.py

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

### bidexhands/tasks/hand_base/vec_task.py

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
    def step(self, actions)
    def reset(self)
class VecTaskPythonArm(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/vec_task_rlgames.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def has_action_masks(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def seed(self, seed)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
    def get_env_info(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class RLgamesVecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _to_device(self, inp)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/shadow_hand_block_stack.py

```
class ShadowHandBlockStack(BaseTask)
    """This class corresponds to the Block Stack task. This environment involves dual hands and two blocks, and we need to stack the block
as a tower.

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg folder

    sim_params"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        block_right_handle_pos (tensor): The position of the right block

        block_left_handle_pos (tensor): The position of the left block

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    
    # Distance from the hand to the object
    stack_pos1 = target_pos.clone()
    stack_pos2 = target_pos.clone()

    stack_pos1[:, 1] -= 0.1
    stack_pos2[:, 1] -= 0.1
    # stack_pos1[:, 2] += 0.025
    stack_pos1[:, 2] += 0.05

    goal_dist1 = torch.norm(stack_pos1 - block_left_handle_pos, p=2, dim=-1)
    goal_dist2 = torch.norm(stack_pos2 - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(block_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - r
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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

   
```

### bidexhands/tasks/shadow_hand_bottle_cap.py

```
class ShadowHandBottleCap(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    # quat_diff = 
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_
```

### bidexhands/tasks/shadow_hand_catch_abreast.py

```
class ShadowHandCatchAbreast(BaseTask)
    """This class corresponds to the Catch Abreast task. This environment consists of two shadow hands placed 
side by side in the same direction and an object that needs to be passed. Compared with the previous 
environment which is more like passing objects between the hands of two people, this environme"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, left_hand_pos, right_hand_pos, left_hand_base_pos, right_hand_base_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, left_hand_pos, right_hand_pos, left_hand_base_pos, right_hand_base_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool, device: str
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        left_hand_pos (tensor): The position of the left hand
        
        right_hand_pos (tensor): The position of the right hand
        
        left_hand_base_pos (tensor): The position of the base body of the left hand
        
        right_hand_base_pos (tensor): The position of the base body of the right hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_x_dist = torch.norm(target_pos[:, 0] - object_pos[:, 0], p=2, dim=-1, keepdim=True)

    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))
    # reward = torch.exp(-0.2 * (dist_rew + rot_dist * rot_reward_scale))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)

    successes = torch.where(successes == 0, 
                    torch.where(goal_dist < 0.03, torch.ones_like(
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment.

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.left_hand_pos, self.right_hand_pos,
            self.rigid_body_states[:, 3 + 26, 0:3], self.rigid_body_states[:, 3, 0:3],
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen"), self.device
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 422-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow hand actions
        199 - 222	left shadow hand dof position
        223 - 246	left shadow hand dof velocity
        247 - 270	left shadow hand dof force
        271 - 335	left shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        336 - 365	left shadow hand fingertip force, torque (5 x 6)
        366 - 368	left shadow hand base position
        369 - 371	left shadow hand base rotation
        372 - 397	left shadow hand actions
        398 - 404	object pose
        405 -
```

### bidexhands/tasks/shadow_hand_catch_over2underarm.py

```
class ShadowHandCatchOver2Underarm(BaseTask)
    """This class corresponds to the Over2Underarm task. This environment is similar to Catch Underarm, 
but with an object in each hand and the corresponding goal on the other hand. Therefore, the environment 
requires two objects to be thrown into the other hand at the same time, which requires a higher """
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, left_hand_base_pos, right_hand_base_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot, device)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, left_hand_base_pos, right_hand_base_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool, device: str
):    
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        left_hand_base_pos (tensor): The position of the base body of the left hand
        
        right_hand_base_pos (tensor): The position of the base body of the right hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = torch.where(successes == 0, 
                    torch.where(goal_dist < 0.03, torch.ones_like(successes), successes), successes)

    # Check env termination conditions, including maximum success number
    right_hand_base_dist = torch.norm(right_hand_base_pos - torch.tensor([0.0, 0.0, 0.5], dtype=torch.float, device=device), p=2, dim=-1)
    left_hand_base_dist = torch.norm(left_hand_base_pos - torch.tensor([0.0, -0.8, 0.5], dtype=
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.hand_positions[self.another_hand_indices, :], self.hand_positions[self.hand_indices, :], 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.hand_positions[self.another_hand_indices, :], self.hand_positions[self.hand_indices, :], 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen"), self.device
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 422-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow hand actions
        199 - 222	left shadow hand dof position
        223 - 246	left shadow hand dof velocity
        247 - 270	left shadow hand dof force
        271 - 335	left shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        336 - 365	left shadow hand fingertip force, torque (5 x 6)
        366 - 368	left shadow hand base position
        369 - 371	left shadow hand base rotation
        372 - 397	left shadow hand actions
        398 - 404	object pose
        405 - 407	object linear velocity
        408 - 410	object angle velocity
        411 - 417	goal pose
        418 - 421	goal rot - object rot
        """
        # fingertip observations, state(pose and vel) + force-torque sensors
   
```

### bidexhands/tasks/shadow_hand_catch_underarm.py

```
class ShadowHandCatchUnderarm(BaseTask)
    """This class corresponds to the Catch Underarm task. In this task, two shadow hands with palms
facing upwards are controlled to pass an object from one palm to the other. What makes it more difficult 
than the Hand over task is that the hands' translation and rotation degrees of freedom are no longer """
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
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
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """

    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)

    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = torch.where(successes == 0, 
                    torch.where(goal_dist < 0.03, torch.ones_like(successes), successes), successes)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.1, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.1, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_suc
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """

        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        # Whether to print out success information
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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """

        # Refreash gym GPU state tensors and specify the state we need
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 422-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow hand actions
        199 - 222	left shadow hand dof position
        223 - 246	left shadow hand dof velocity
        247 - 270	left shadow hand dof force
        271 - 335	left shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        336 - 365	left shadow hand fingertip force, torque (5 x 6)
        366 - 368	left shadow hand base position
        369 - 371	left shadow hand base rotation
        372 - 397	left shadow hand actions
        398 - 404	object pose
        405 - 407	object linear velocity
        408 - 410	object angle velocity
        411 - 417	goal pose
        418 - 421	goal rot - object rot
        """

        # Fingertip observations, state(pose and vel) + force-torque sensors
        num_ft_states = 13 * int(self.num_fingertips / 2)
        num_ft_force_torques = 6 * int(self.num_fingertips / 2) 

        se
```

### bidexhands/tasks/shadow_hand_door_close_inward.py

```
class ShadowHandDoorCloseInward(BaseTask)
    """This class corresponds to the DoorCloseInward task. This environment require a closed door 
to be opened and the door can only be pushed outward or initially open inward. Both these two 
environments only need to do the push behavior, so it is relatively simple

Args:
    cfg (dict): The configurati"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        door_right_handle_pos (tensor): The position of the right door handle

        door_left_handle_pos (tensor): The position of the left door handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(door_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(door_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(door_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(door_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(door_right_handle_pos - right_hand_th_pos, 
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1
```

### bidexhands/tasks/shadow_hand_door_close_outward.py

```
class ShadowHandDoorCloseOutward(BaseTask)
    """This class corresponds to the DoorCloseOutward task. This environment also require a closed door 
to be opened and the door can only be pushed inward or initially open outward, but because they 
can't complete the task by simply pushing, which need to catch the handle by hand and then open 
or close"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        door_right_handle_pos (tensor): The position of the right door handle

        door_left_handle_pos (tensor): The position of the left door handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(door_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(door_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(door_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(door_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(door_right_handle_pos - right_hand_th_pos, 
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0,
```

### bidexhands/tasks/shadow_hand_door_open_inward.py

```
class ShadowHandDoorOpenInward(BaseTask)
    """This class corresponds to the DoorOpenInward task. This environment also require a opened door 
to be closed and the door can only be pushed inward or initially open outward, but because they 
can't complete the task by simply pushing, which need to catch the handle by hand and then open 
or close i"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        door_right_handle_pos (tensor): The position of the right door handle

        door_left_handle_pos (tensor): The position of the left door handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(door_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(door_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(door_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(door_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(door_right_handle_pos - right_hand_th_pos, 
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 
```

### bidexhands/tasks/shadow_hand_door_open_outward.py

```
class ShadowHandDoorOpenOutward(BaseTask)
    """This class corresponds to the DoorOpenOutward task. This environment require a opened door 
to be closed and the door can only be pushed outward or initially open inward. Both these two 
environments only need to do the push behavior, so it is relatively simple

Args:
    cfg (dict): The configurati"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, door_left_handle_pos, door_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        door_right_handle_pos (tensor): The position of the right door handle

        door_left_handle_pos (tensor): The position of the left door handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(door_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(door_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(door_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(door_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(door_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(door_right_handle_pos - right_hand_th_pos, 
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.door_left_handle_pos, self.door_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 
```

### bidexhands/tasks/shadow_hand_grasp_and_place.py

```
class ShadowHandGraspAndPlace(BaseTask)
    """This class corresponds to the GraspAndPlace task. This environment consists of dual-hands, an
object and a bucket that requires us to pick up the object and put it into the bucket.

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dextero"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        block_right_handle_pos (tensor): The position of the right block handle

        block_left_handle_pos (tensor): The position of the left block handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(block_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_ro
```

### bidexhands/tasks/shadow_hand_kettle.py

```
class ShadowHandKettle(BaseTask)
    """This class corresponds to the PourWater task. This environment involves two hands and a bottle, 
we need to Hold the kettle with one hand and the bucket with the other hand, and pour the water 
from the kettle into the bucket. In the practice task in Isaac Gym, we use many small balls to 
simulate t"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, kettle_handle_pos, bucket_handle_pos, kettle_spout_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, kettle_handle_pos, bucket_handle_pos, kettle_spout_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        kettle_handle_pos (tensor): The position of the kettle

        bucket_handle_pos (tensor): The position of the bucket

        kettle_spout_pos (tensor): The position of the kettle's spout

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(kettle_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bucket_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(kettle_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(kettle_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(kettle_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(kettle_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(kettle_handl
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.kettle_handle_pos, self.bucket_handle_pos, self.kettle_spout_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """

        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.kettle_handle_pos, self.bucket_handle_pos, self.kettle_spout_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.bucket_handle_pos = self.bucket_handle_pos + quat_apply(self.bucket_handle_rot, to_torch([1, 0, 0], device=self.de
```

### bidexhands/tasks/shadow_hand_lift_underarm.py

```
class ShadowHandLiftUnderarm(BaseTask)
    """This class corresponds to the LiftUnderarm task. This environment requires grasping the pot handle 
with two hands and lifting the pot to the designated position. This environment is designed to 
simulate the scene of lift in daily life and is a practical skill.

Args:
    cfg (dict): The configurat"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, pot_left_handle_pos, pot_right_handle_pos, left_hand_pos, right_hand_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, pot_left_handle_pos, pot_right_handle_pos, 
    left_hand_pos, right_hand_pos, 
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        pot_left_handle_pos (tensor): The position of the left handle of the pot

        pot_right_handle_pos (tensor): The position of the right handle of the pot

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]
    right_hand_dist = torch.norm(pot_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(pot_left_handle_pos - left_hand_pos, p=2, dim=-1)
    # Orientation alignment for the cube in hand and goal cube
    # quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    # rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = right_hand_dist
    left_hand_dist_rew = left_hand_dist

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.where(right_hand_dist < 0.08,
                        torch.where(left_hand_dist < 0.08,
                                        3*(0.385 - goal
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pot_left_handle_pos, self.pot_right_handle_pos,
            self.left_hand_pos, self.right_hand_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pot_left_handle_pos, self.pot_right_handle_pos,
            self.left_hand_pos, self.right_hand_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is compo
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_ml1.py

```
class ShadowHandMetaML1(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,self.object_left_handle_pos, self.object_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, self.this_task
        )

        self.extras['total_successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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

        self.object_left_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_left_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.object_right_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_right_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num
```
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_ml1_task_info.py

```
def obtrain_task_info(task_name)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_left_handle_pos, object_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, this_task)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, object_left_handle_pos, object_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, this_task: str
):
    # Distance from the hand to the object
    if this_task in ["catch_underarm", "hand_over", "catch_abreast", "catch_over2underarm"]:
        goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)

        # Orientation alignment for the cube in hand and goal cube
        quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
        rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

        dist_rew = goal_dist
        # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

        action_penalty = torch.sum(actions ** 2, dim=-1)

        # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
        reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

        # Find out which envs hit the goal and update successes count
        goal_resets = torch.where(torch.abs(goal_dist) <= 0.03, torch.ones_like(reset_goal_buf), reset_goal_buf)
        successes = successes + goal_resets

        # Success bonus: orientation is within `success_tolerance` of goal orientation
        reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

        # Fall penalty: distance to the goal is larger than a threashold
        reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

        # Check env termination conditions, including maximum success number
        resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
        if max_consecutive_successes > 0:
            # Reset progress buffer on goal envs if max_consecutive_successes > 0
            progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
            resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
        resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

        # Apply penalty for not reaching the goal
        if max_consecutive_successes > 0:
            reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

        num_resets = torch.sum(resets)
        finished_cons_successes = torch.sum(successes * resets.float())

        cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

        return reward, resets, goal_resets, progress_buf, successes, cons_successes

    if this_task in ["door_open_outward"]:
        # Distance from the hand to the object
        goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
        # goal_dist = target_pos[:, 2] - object_pos[:, 2]

        right_hand_dist = torch.norm(object_right_handle_pos - right_hand_pos, p=2, dim=-1)
        left_hand_dist = torch.norm(object_left_handle_pos - left_hand_pos, p=2, dim=-1)

        right_hand_finger_dist = (torch.norm(object_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(object_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                                + torch.norm(object_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(object_right_h
```
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_mt1.py

```
class ShadowHandMetaMT1(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,self.object_left_handle_pos, self.object_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, self.this_task
        )

        self.extras['total_successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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

        self.object_left_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_left_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.object_right_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_right_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_mf_rot = self.rigid_body_states[:, 11, 3:7]
        self.right_hand_mf_pos = self.right_hand_mf_pos + quat_apply(self.right_hand_mf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_rf_pos = self.rigid_body_states[:, 15, 0:3]
        self.right_hand_rf_rot = self.rigid_body_states[:, 15, 3:7]
        self.right_hand_rf_pos = self.right_hand_rf_pos + quat_apply(self.right_hand_rf_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num
```
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_mt1_task_info.py

```
def obtrain_task_info(task_name)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_left_handle_pos, object_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, this_task)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, object_left_handle_pos, object_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, this_task: str
):
    # Distance from the hand to the object
    if this_task in ["catch_underarm", "hand_over", "catch_abreast", "catch_over2underarm"]:
        goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)

        # Orientation alignment for the cube in hand and goal cube
        quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
        rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

        dist_rew = goal_dist
        # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

        action_penalty = torch.sum(actions ** 2, dim=-1)

        # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
        reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

        # Find out which envs hit the goal and update successes count
        goal_resets = torch.where(torch.abs(goal_dist) <= 0.03, torch.ones_like(reset_goal_buf), reset_goal_buf)
        successes = successes + goal_resets

        # Success bonus: orientation is within `success_tolerance` of goal orientation
        reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

        # Fall penalty: distance to the goal is larger than a threashold
        reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

        # Check env termination conditions, including maximum success number
        resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
        if max_consecutive_successes > 0:
            # Reset progress buffer on goal envs if max_consecutive_successes > 0
            progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
            resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
        resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

        # Apply penalty for not reaching the goal
        if max_consecutive_successes > 0:
            reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

        num_resets = torch.sum(resets)
        finished_cons_successes = torch.sum(successes * resets.float())

        cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

        return reward, resets, goal_resets, progress_buf, successes, cons_successes

    if this_task in ["door_open_outward"]:
        # Distance from the hand to the object
        goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
        # goal_dist = target_pos[:, 2] - object_pos[:, 2]

        right_hand_dist = torch.norm(object_right_handle_pos - right_hand_pos, p=2, dim=-1)
        left_hand_dist = torch.norm(object_left_handle_pos - left_hand_pos, p=2, dim=-1)

        right_hand_finger_dist = (torch.norm(object_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(object_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                                + torch.norm(object_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(object_right_h
```
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_mt4.py

```
class ShadowHandMetaMT4(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.another_object_pos, self.another_object_rot, self.another_goal_pos, self.another_goal_rot, self.object_left_handle_pos, self.object_right_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, self.this_task
        )

        self.extras['total_successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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

        # refresh
        tem_shadow_hand_dof = torch.zeros((self.num_envs, 48, 2), dtype=torch.float, device=self.device)
        pointer = 0
        for i in range(self.num_envs):
            tem_shadow_hand_dof[i, :, :] = self.dof_state[pointer:pointer+48, :]
            pointer += 48 + self.object_dof[i] * 2

        self.shadow_hand_dof_state = tem_shadow_hand_dof[:, :self.num_shadow_hand_dofs]
        self.shadow_hand_dof_pos = self.shadow_hand_dof_state[..., 0]
        self.shadow_hand_dof_vel = self.shadow_hand_dof_state[..., 1]

        self.shadow_hand_another_dof_state = tem_shadow_hand_dof[:, self.num_shadow_hand_dofs:self.num_shadow_hand_dofs*2]
        self.shadow_hand_another_dof_pos = self.shadow_hand_another_dof_state[..., 0]
        self.shadow_hand_another_dof_vel = self.shadow_hand_another_dof_state[..., 1]

        self.num_total_rigid_body = self.total_rigid_body_tensor.shape[0]
        self.rigid_body_states = torch.zeros((self.num_envs, 52, 13), dtype=torch.float, device=self.device)
        pointer = 0
        for i in range(self.num_envs):
            self.rigid_body_states[i, :, :] = self.total_rigid_body_tensor[pointer:pointer+52, :]
            pointer += 52 + self.object_rigid_body[i] * 2 + 1

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.another_object_pose = self.root_state_tensor[self.another_object_indices, 0:7]
        self.another_object_pos = self.root_state_tensor[self.another_object_indices, 0:3]
        self.another_object_rot = self.root_state_tensor[self.another_object_indices, 3:7]
        self.another_object_linvel = self.root_state_tensor[self.another_object_indices, 7:10]
        self.another_object_angvel = self.root_state_tensor[self.another_object_indices, 10:13]

        self.object_left_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_left_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.39)
        self.object_left_handle_pos = self.object_left_handle_pos + quat_apply(self.object_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.object_right_handle_pos = self.rigid_body_states[:, 26 * 2 - 1, 0:3]
        self.object_right_handle_rot = self.rigid_body_states[:, 26 * 2 - 1, 3:7]
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.5)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.39)
        self.object_right_handle_pos = self.object_right_handle_pos + quat_apply(self.object_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.04)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot 
```
```

### bidexhands/tasks/shadow_hand_meta/shadow_hand_meta_mt4_task_info.py

```
def obtain_task_info(task_name)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, another_object_pos, another_object_rot, another_target_pos, another_target_rot, object_left_handle_pos, object_right_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, this_task)
def obtain_task_dof_info(this_task, env_ids, num_each_envs, device)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, another_object_pos, another_object_rot, another_target_pos, another_target_rot, object_left_handle_pos, object_right_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, this_task: str
):
    # Distance from the hand to the object
    if this_task in ["catch_underarm", "two_catch_underarm", "catch_abreast", "catch_over2underarm"]:
        goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
        another_goal_dist = torch.norm(another_target_pos - another_object_pos, p=2, dim=-1)

        # Orientation alignment for the cube in hand and goal cube
        quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
        rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))
        another_quat_diff = quat_mul(another_object_rot, quat_conjugate(another_target_rot))
        another_rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(another_quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

        dist_rew = goal_dist
        # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

        action_penalty = torch.sum(actions ** 2, dim=-1)

        # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
        reward = torch.exp(-0.2*((dist_rew * dist_reward_scale + rot_dist) + (another_goal_dist * dist_reward_scale)))

        # Find out which envs hit the goal and update successes count
        goal_resets = torch.where(torch.abs(goal_dist) <= 0.03, torch.ones_like(reset_goal_buf), reset_goal_buf)
        successes = successes + goal_resets

        # Success bonus: orientation is within `success_tolerance` of goal orientation
        reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

        # Fall penalty: distance to the goal is larger than a threashold
        reward = torch.where(object_pos[:, 2] <= 0.1, reward + fall_penalty, reward)
        reward = torch.where(another_object_pos[:, 2] <= 0.1, reward + fall_penalty, reward)

        # Check env termination conditions, including maximum success number
        resets = torch.where(object_pos[:, 2] <= 0.1, torch.ones_like(reset_buf), reset_buf)
        resets = torch.where(another_object_pos[:, 2] <= 0.1, torch.ones_like(resets), resets)        
        
        if max_consecutive_successes > 0:
            # Reset progress buffer on goal envs if max_consecutive_successes > 0
            progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
            resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
        resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

        # Apply penalty for not reaching the goal
        if max_consecutive_successes > 0:
            reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

        num_resets = torch.sum(resets)
        finished_cons_successes = torch.sum(successes * resets.float())

        cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

        return reward, resets, goal_resets, progress_buf, successes, cons_successes

    if this_task in ["door_open_inward"]:
        # Distance f
```
```

### bidexhands/tasks/shadow_hand_over.py

```
class ShadowHandOver(BaseTask)
    """This class corresponds to the HandOver task. This environment consists of two shadow hands with 
palms facing up, opposite each other, and an object that needs to be passed. In the beginning, 
the object will fall randomly in the area of the shadow hand on the right side. Then the hand 
holds the ob"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
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
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = torch.where(successes == 0, 
                    torch.where(goal_dist < 0.03, torch.ones_like(successes), successes), successes)

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 422-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow hand actions
        199 - 222	left shadow hand dof position
        223 - 246	left shadow hand dof velocity
        247 - 270	left shadow hand dof force
        271 - 335	left shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        336 - 365	left shadow hand fingertip force, torque (5 x 6)
        366 - 368	left shadow hand base position
        369 - 371	left shadow hand base rotation
        372 - 397	left shadow hand actions
        398 - 404	object pose
        405 - 407	object linear velocity
        408 - 410	object angle velocity
        411 - 417	goal pose
        418 - 421	goal rot - object rot
        """
        num_ft_states = 13 * int(self.num_fingertips / 2)  # 65
        num_ft_force_torques = 6 * int(self.num_fingertips / 2)  # 30

        self.obs_buf[:, 0:self.num_shadow_hand_dofs] = unscale(self.shadow_hand_dof_pos,
                                                            self.shadow_hand_dof_lower_limits, self.shadow_hand_d
```

### bidexhands/tasks/shadow_hand_pen.py

```
class ShadowHandPen(BaseTask)
    """This class corresponds to the Open Pen Cap task. This environment involves two hands and a pen, we need to use two hands
to open the pen cap.


Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg folder

    sim_params """
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, pen_right_handle_pos, pen_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, pen_right_handle_pos, pen_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        pen_left_handle_pos (tensor): The position of the left handle of the pen

        pen_right_handle_pos (tensor): The position of the right handle of the pen

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(pen_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(pen_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(pen_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(pen_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(pen_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(pen_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(pen_right_handle_pos - right_hand_th_pos, p=2, di
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pen_right_handle_pos, self.pen_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.pen_right_handle_pos, self.pen_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs
```

### bidexhands/tasks/shadow_hand_point_cloud.py

```
class ShadowHandPointCloud(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def camera_visulization(self, is_depth_image)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
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
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

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

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        self.gym.render_all_camera_sensors(self.sim)
        self.gym.start_access_image_tensors(self.sim)

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
        self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/shadow_hand_push_block.py

```
class ShadowHandPushBlock(BaseTask)
    """This class corresponds to the PushBlock task. This environment involves two hands and two blocks, 
we need to use both hands to reach and push the block to the desired goal separately. This is a 
relatively simple task

Args:
    cfg (dict): The configuration file of the environment, which is the pa"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, left_target_pos, left_target_rot, right_target_pos, right_target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, left_target_pos, left_target_rot, right_target_pos, right_target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        block_left_handle_pos (tensor): The position of the left handle of the block

        block_right_handle_pos (tensor): The position of the right handle of the block

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    left_goal_dist = torch.norm(left_target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(right_target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(block_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(block_right_handle_pos - right_hand_rf
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.left_goal_pos, self.left_goal_rot, self.left_goal_pos, self.left_goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 
```

### bidexhands/tasks/shadow_hand_re_orientation.py

```
class ShadowHandReOrientation(BaseTask)
    """This class corresponds to the ReOrientation task. This environment involves two hands and two objects. 
Each hand holds an object and we need to reorient the object to the target orientation

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
     """
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        object_another_pos (tensor): The position of the another object

        object_another_rot (tensor): The rotation of the another object

        target_another_pos (tensor): The position of the another target

        target_another_rot (tensor): The rotate of the another target

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    goal_another_dist = torch.norm(target_another_pos - object_another_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    quat_another_diff = quat_mul(object_another_rot, quat_conjugate(target_another_rot))
    rot_another_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_another_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist * dist_reward_scale + goal_another_dist * dist_reward_scale
    rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale + 1.0/(torch.abs(rot_another_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = dist_rew + rot_rew + action_penalty * action_penalty_scale

  
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 446-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow h
```

### bidexhands/tasks/shadow_hand_scissors.py

```
class ShadowHandScissors(BaseTask)
    """This class corresponds to the Scissors task. This environment involves two hands and scissors, 
we need to use two hands to open the scissors

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg folder

    sim_params ("""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, scissors_right_handle_pos, scissors_left_handle_pos, object_dof_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, scissors_right_handle_pos, scissors_left_handle_pos, object_dof_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        scissors_left_handle_pos (tensor): The position of the left handle of the scissors

        scissors_right_handle_pos (tensor): The position of the right handle of the scissors

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(scissors_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(scissors_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(scissors_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(scissors_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(scissors_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(scissors_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
              
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.scissors_right_handle_pos, self.scissors_left_handle_pos, self.object_dof_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.scissors_right_handle_pos, self.scissors_left_handle_pos, self.object_dof_pos,
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 
```

### bidexhands/tasks/shadow_hand_swing_cup.py

```
class ShadowHandSwingCup(BaseTask)
    """This class corresponds to the SwingCup task. This environment involves two hands and a dual handle 
cup, we need to use two hands to hold and swing the cup together

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg f"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, cup_right_handle_pos, cup_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, cup_right_handle_pos, cup_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        cup_left_handle_pos (tensor): The position of the left handle of the cup

        cup_right_handle_pos (tensor): The position of the right handle of the cup

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(cup_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(cup_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(cup_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(cup_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(cup_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(cup_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(cup_right_handle_pos - right_hand_th_pos, p=2, di
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.cup_right_handle_pos, self.cup_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.cup_right_handle_pos, self.cup_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """

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
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.devi
```

### bidexhands/tasks/shadow_hand_switch.py

```
class ShadowHandSwitch(BaseTask)
    """This class corresponds to the Switch task. This environment involves dual hands and a bottle, we 
need to use dual hand fingers to press the desired button

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg folder

  """
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, switch_right_handle_pos, switch_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, switch_right_handle_pos, switch_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        switch_left_handle_pos (tensor): The position of the left handle of the switch

        switch_right_handle_pos (tensor): The position of the right handle of the switch

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands

        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(switch_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(switch_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(switch_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(switch_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
                            + torch.norm(switch_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(switch_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
                            + torch.norm(switch_right_
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.switch_right_handle_pos, self.switch_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.switch_right_handle_pos, self.switch_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        self.left_hand_pos = self.left_hand_pos 
```

### bidexhands/tasks/shadow_hand_two_catch_underarm.py

```
class ShadowHandTwoCatchUnderarm(BaseTask)
    """This class corresponds to the TwoCatchUnderarm task. This environment is similar to Catch Underarm, 
but with an object in each hand and the corresponding goal on the other hand. Therefore, the 
environment requires two objects to be thrown into the other hand at the same time, which requires 
a hig"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, object_another_pos, object_another_rot, target_another_pos, target_another_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        object_another_pos (tensor): The position of the another object

        object_another_rot (tensor): The rotation of the another object

        target_another_pos (tensor): The position of the another target

        target_another_rot (tensor): The rotate of the another target

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    goal_another_dist = torch.norm(target_another_pos - object_another_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    quat_another_diff = quat_mul(object_another_rot, quat_conjugate(target_another_rot))
    rot_another_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_another_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist)) + torch.exp(-0.2*(goal_another_dist * dist_reward_scale + rot_another_dist))

    # Find out which envs hit the goal and update
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.object_another_pos, self.object_another_rot, self.goal_another_pos, self.goal_another_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

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
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
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
        """
        Compute the observations of all environment. The observation is composed of three parts: 
        the state values of the left and right hands, and the information of objects and target. 
        The state values of the left and right hands were the same for each task, including hand 
        joint and finger positions, velocity, and force information. The detail 446-dimensional 
        observational space as shown in below:

        Index       Description
        0 - 23	    right shadow hand dof position
        24 - 47	    right shadow hand dof velocity
        48 - 71	    right shadow hand dof force
        72 - 136	right shadow hand fingertip pose, linear velocity, angle velocity (5 x 13)
        137 - 166	right shadow hand fingertip force, torque (5 x 6)
        167 - 169	right shadow hand base position
        170 - 172	right shadow hand base rotation
        173 - 198	right shadow hand actions
        199 - 222	left shadow 
```

### bidexhands/train.py

```
def train()
```

### bidexhands/utils/config.py

```
def set_np_formatting()
def warn_task_name()
def warn_algorithm_name()
def set_seed(seed, torch_deterministic)
def retrieve_cfg(args, use_rlg_config)
def load_cfg(args, use_rlg_config)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark, use_rlg_config, task_name, algo)
```

### bidexhands/utils/logger/plotter.py

```
def smooth(y, radius, mode, valid_only)
def plot_ax(ax, file_lists, legend_pattern, xlabel, ylabel, title, xlim, xkey, ykey, smooth_radius, shaded_std, legend_outside)
def plot_figure(file_lists, group_pattern, fig_length, fig_width, sharex, sharey, title)
```

### bidexhands/utils/logger/tools.py

```
def find_all_files(root_dir, pattern)
def group_files(file_list, pattern)
def csv2numpy(csv_file)
def convert_tfevents_to_csv(root_dir, alg_type, env_num, env_step, refresh)
def merge_csv(csv_files, root_dir, remove_zero)
```

### bidexhands/utils/o3dviewer.py

```
class PointcloudVisualizer()
    def __init__(self)
    def add_geometry(self, cloud)
    def update(self, cloud)
```

### bidexhands/utils/package_utils.py

```
def make(task_name, algo)
```

### bidexhands/utils/parse_task.py

```
def parse_task(args, cfg, cfg_train, sim_params, agent_index)
```

### bidexhands/utils/process_marl.py

```
def get_AgentIndex(config)
def process_MultiAgentRL(args, env, config, model_dir)
```

### bidexhands/utils/process_metarl.py

```
def process_mamlppo(args, env, cfg_train, logdir)
```

### bidexhands/utils/process_mtrl.py

```
def process_mtppo(args, env, cfg_train, logdir)
def process_random(args, env, cfg_train, logdir)
```

### bidexhands/utils/process_offrl.py

```
def process_td3_bc(args, env, cfg_train, logdir)
def process_bcq(args, env, cfg_train, logdir)
def process_iql(args, env, cfg_train, logdir)
def process_ppo_collect(args, env, cfg_train, logdir)
```

### bidexhands/utils/process_sarl.py

```
def process_sarl(args, env, cfg_train, logdir)
```

### bidexhands/utils/torch_jit_utils.py

```
def compute_heading_and_up(torso_rotation, inv_start_rot, to_target, vec0, vec1, up_idx)
def compute_rot(torso_quat, velocity, ang_velocity, targets, torso_positions)
def quat_axis(q, axis)
```

### bidexhands/utils/util.py

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