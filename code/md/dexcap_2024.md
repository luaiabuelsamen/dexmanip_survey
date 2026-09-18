# dexcap_2024

source: https://github.com/j96w/DexCap


commit: 4b0bed0966c87368f3cde4476aadb7585c3b94b5


## README

# DexCap

<img src="assets/overview.gif" width=100%>

-------
## News!
2024-08: We have released new DexCap hardware updates to address known issues. Check out [latest tutorial](https://docs.google.com/document/d/1ANxSA_PctkqFf3xqAkyktgBgDWEbrFK7b1OnJe54ltw/edit#heading=h.yxlxo67jgfyx) (Hardware Setup, Software Setup, Data Collection) for more information.

-------
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Data Collection](#data-collection)
- [Data Processing](#data-processing)
- [Building Training Dataset](#building-training-dataset)
- [Training Policy](#training-policy)
- [Acknowledgements](#acknowledgements)
- [BibTeX](#bibtex)
- [License](#license)

-------
## Overview

This repository is the implementation code for "DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation" ([Paper](https://arxiv.org/abs/2403.07788), 
[Website](https://dex-cap.github.io/)) by Wang et al. at [The Movement Lab](https://tml.stanford.edu/) 
and [Stanford Vision and Learning Lab](http://svl.stanford.edu/).

In this repo, we provide our full implementation code for [Data collection](#data-collection), [Data processing](#data-processing), 
[Building dataset](#building-training-dataset), and [Training policy](#training-policy).

-------
## Installation
First, we install and build the environment on the mini-PC (NUC) for data collection. This installation is based on a Windows platform.
After installing the [software](https://www.rokoko.com/products/studio/download) for the Rokoko motion capture glove and Anaconda, create the conda environment:
```
cd DexCap/install
conda env create -n mocap -f env_nuc_windows.yml
```

The second step is to install and build environments for the Ubuntu workstation, which could also be a headless server for dataset building and training. Simply follow:
```	
conda create -n dexcap python=3.8
conda activate dexcap
cd DexCap/install
pip install -r env_ws_requirements.txt
cd STEP3_train_policy
pip install -e .
```

-------
## Data Collection
First, start the Rokoko Studio software and make sure the motion capture glove is detected. Choose the `Livestreaming` function and use the `Custom connection` with the following settings:
```	
Include connection: True
Forward IP: 192.168.0.200
Port: 14551
Data format: Json
```
Make sure the NUC has been connected to the portable Wi-Fi router and the IP address has been set to `192.168.0.200`. 
Feel free to change to another address and modify the settings correspondingly. After starting the streaming, we can now open a conda terminal and use the following script to catch the raw data of the mocap glove:
```	
conda activate mocap
cd DexCap/STEP1_collect_data
python redis_glove_server.py
```
After starting the streaming, open another conda terminal and start data collection with:
```
python data_recording.py -s --store_hand -o ./save_data_scenario_1
```
The data will first be stored in the memory. After finishing the current episode, use `Ctrl+C` to stop the recording, and the program will automatically start saving the data on the local SSD in a multi-threaded manner.
The collected raw data follows the structure of:
```
save_data_scenario_1
├── frame_0
│   ├── color_image.jpg           # Chest camera RGB image
│   ├── depth_image.png           # Chest camera depth image
│   ├── pose.txt                  # Chest camera 6-DoF pose in world frame
│   ├── pose_2.txt                # Left hand 6-DoF pose in world frame
│   ├── pose_3.txt                # Right hand 6_DoF pose in world frame
│   ├── left_hand_joint.txt       # Left hand joint positions (3D) in the palm frame
│   └── right_hand_joint.txt      # Right hand joint positions (3D) in the palm frame
├── frame_1
└── ...
```

-------
## Data Processing
First, we can visualize the collected data through:
```	
cd DexCap/STEP1_collect_data
python replay_human_traj_vis.py --directory save_data_scenario_1
```
A point cloud visualizer based on Open3D will show up, and you can see the captured hand motion as in the following

<img src="assets/replay.gif" width=100%>

(Optional) We also provide an interface for correcting initial drifts of the SLAM, if needed. Run the following script and use the numeric keypad of the keyboard to correct the drifts.
The correction will be applied to the entire video.
```	
python replay_human_traj_vis.py --directory save_data_scenario_1 --calib
python calculate_offset_vis_calib.py --directory save_data_scenario_1
```
The next step is to transform the point cloud and mocap data to the robot operation space. Run the following script and use the numeric keypad to adjust the world frame of the data to align with the robot table frame. This process usually takes < 10 seconds and only needs to be done once for each data episode.
```	
python transform_to_robot_table.py --directory save_data_scenario_1
```

<img src="assets/transfer.gif" width=100%>

Finally, cut the whole data episode into several task demos with the following script.
```	
python demo_clipping_3d.py --directory save_data_scenario_1
```
You can download our raw dataset from [Link](https://huggingface.co/datasets/chenwangj/DexCap-Data). And use `replay_human_traj_vis.py` to visualize the data.

-------
## Building Training Dataset
After collecting and processing the raw data, we can now transfer the data to the workstation and use the following script to generate a `hdf5` dataset file in [robomimic](https://github.com/ARISE-Initiative/robomimic) format for training.
```	
python demo_create_hdf5.py
```
This process will use inverse kinematics (based on PyBullet) to match the robot LEAP hand's fingertips to the human fingertips in the mocap data. When the human's hand is visible in the camera view, a point cloud mesh of the robot hand built with forward kinematics is added to the point cloud observation as shown in the following video. The redundant point clouds (background, table surface) are also removed.

<img src="assets/dataset.gif" width=100%>

You can download our processed dataset from [Link](https://huggingface.co/datasets/chenwangj/DexCap-Data).

-------
## Training Policy
After building the `hdf5` dataset, we can start policy training with the following script and config file:
```
cd DexCap/STEP3_train_policy/robomimic
python scripts/train.py --config training_config/[NAME_OF_CONFIG].json
```
The default training config will train a point cloud-based Diffusion Policy, which takes the point cloud observation from the chest camera (transformed to the fixed world frame) as input and generates a sequence (20 steps) of actions for both robot hands and arms (46 dimensions in total). For more details on the algorithm, please check out our study paper.

-------
## Acknowledgements
- Our policy training is implemented based on [robomimic](https://github.com/ARISE-Initiative/robomimic), [Diffusion Policy](https://github.com/real-stanford/diffusion_policy).
- The robot arm controller is based on [Deoxys](https://github.com/UT-Austin-RPL/deoxys_control).
- The robot LEAP hand controller is based on [LEAP_Hand_API](https://github.com/leap-hand/LEAP_Hand_API).

-------
## BibTeX
```
@article{wang2024dexcap,
  title = {DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation},
  author = {Wang, Chen and Shi, Haochen and Wang, Weizhuo and Zhang, Ruohan and Fei-Fei, Li and Liu, C. Karen},
  journal = {arXiv preprint arXiv:2403.07788},
  year = {2024}
}
```

-------
## License
Licensed under the [MIT License](LICENSE)

## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
STEP1_collect_data/
  calculate_offset_vis_calib.py
  data_recording.py
  default_offset/
    calib_offset.txt
    calib_offset_left.txt
    calib_ori_offset.txt
    calib_ori_offset_left.txt
  demo_clipping_3d.py
  hyperparameters.py
  realsense_helper.py
  redis_glove_server.py
  replay_human_traj_vis.py
  robot_table_pointcloud/
    frame_0/
  transform_to_robot_table.py
  visualizer.py
STEP1_collect_data_202408updates/
  open3d_vis_obj.py
  openxr_utils.py
  recording_utils.py
  requirements.txt
  vis_vive_realsense_glove_dataset.py
  vive_realsense_glove_datacollection.py
  vive_test.py
STEP2_build_dataset/
  config/
    alice.yml
    alice_2.yml
    control_config.yml
    example-controller.yml
    joint-impedance-controller.yml
    local-host.yml
    osc-controller.yml
    osc-position-controller.yml
    osc-yaw-controller.yml
    realrobot_left_hand_offset.yml
    realrobot_right_hand_offset.yml
  dataset_utils.py
  demo_create_hdf5.py
  hyperparameters.py
  leap_hand_mesh/
    config.json
    dip.part
    dip.stl
    fingertip.part
    fingertip.stl
    fingertip_old.stl
    mcp_joint.part
    mcp_joint.stl
    palm_lower.part
    palm_lower.stl
    palm_lower_left.stl
    palm_lower_left_old.stl
    pip.part
    pip.stl
    robot.urdf
    robot_left.urdf
    robot_left_pybullet.urdf
    robot_left_pybullet_2.urdf
    robot_pybullet.urdf
    thumb_dip.part
    thumb_dip.stl
    thumb_fingertip.part
    thumb_fingertip.stl
    thumb_fingertip_old.stl
    thumb_pip.part
    thumb_pip.stl
  pybullet_ik_bimanual.py
  utils.py
STEP3_train_policy/
  robomimic/
    __init__.py
    algo/
    config/
    envs/
    exps/
    macros.py
    macros_private.py
    models/
    scripts/
    training_config/
    utils/
  setup.py
install/
  env_nuc_windows.yml
  env_ws_requirements.txt
```

## Config files (12)


### STEP2_build_dataset/config/alice.yml

```yaml
PC:
  NAME: "rosie"
  IP: 172.16.0.4
  # PUB_PORT: 5555
  # SUB_PORT: 5556

NUC:
  NAME: "alice"
  IP: 172.16.0.3
  PUB_PORT: 5558
  SUB_PORT: 5557
  GRIPPER_PUB_PORT: 5560
  GRIPPER_SUB_PORT: 5559

ROBOT:
  IP: 172.16.0.6


control:
  x: 0.1
  y: 0.1
  z: -0.1
  ax: 0.0
  ay: 0.0
  az: 0.0
  kp:
    p: 150.0
    r: 60.0

```

### STEP2_build_dataset/config/alice_2.yml

```yaml
PC:
  NAME: "rosie"
  IP: 172.16.0.4
  # PUB_PORT: 5555
  # SUB_PORT: 5556

NUC:
  NAME: "alice"
  IP: 172.16.0.1
  PUB_PORT: 5562
  SUB_PORT: 5561
  GRIPPER_PUB_PORT: 5564
  GRIPPER_SUB_PORT: 5563

ROBOT:
  IP: 172.16.0.5


control:
  x: 0.1
  y: 0.1
  z: -0.1
  ax: 0.0
  ay: 0.0
  az: 0.0
  kp:
    p: 150.0
    r: 60.0

```

### STEP2_build_dataset/config/control_config.yml

```yaml
CONTROL:
        SAFETY:
                MAX_TORQUE: 5
                MIN_TORQUE: -5

```

### STEP2_build_dataset/config/example-controller.yml

```yaml

```

### STEP2_build_dataset/config/joint-impedance-controller.yml

```yaml
# Seems smooth enough
joint_kp: [100., 100., 100., 100., 75., 150., 50.]
joint_kd: [20., 20., 20., 20., 7.5, 15.0, 5.0]

# # A little bit shaky
# joint_kp: [600., 600., 600., 600., 75., 150., 50.]
# joint_kd: [50., 50., 50., 50., 7.5, 15.0, 5.0]

# original (with critical damping)
# joint_kp: [50., 50., 50., 50., 5., 20., 20.]
# joint_kd: null # [0., 0., 0., 0., 0., 0., 0.]
```

### STEP2_build_dataset/config/local-host.yml

```yaml
PC:
  NAME: "rosie"
  IP: localhost

NUC:
  IP: localhost
  NAME: "alice"
  PUB_PORT: 5556
  SUB_PORT: 5555
  GRIPPER_PUB_PORT: 5558
  GRIPPER_SUB_PORT: 5557

ROBOT:
  IP: 172.16.0.6

```

### STEP2_build_dataset/config/osc-controller.yml

```yaml
Kp:
  translation: 160.0
  rotation: 250.0
```

### STEP2_build_dataset/config/osc-position-controller.yml

```yaml
Kp:
  translation: 150.0
  rotation: 250.0


```

### STEP2_build_dataset/config/osc-yaw-controller.yml

```yaml
Kp:
  translation: 150.0
  rotation: 250.0


```

### STEP2_build_dataset/config/realrobot_left_hand_offset.yml

```yaml
absolute_offset:
- -0.06373723621495607
- -0.46208920357576447
- 0.20704649396348807
goal_ori_offset:
- -0.0501986409152185
- 0.019198418015565294
- 0.012741626224113348

```

### STEP2_build_dataset/config/realrobot_right_hand_offset.yml

```yaml
absolute_offset:
- -0.24834218172497126
- 0.49704745277007806
- 0.14612847752531732
goal_ori_offset:
- 0.11818597397499012
- 0.03880647837850592
- -0.005137150339164783

```

### install/env_nuc_windows.yml

```yaml
name: mocap
channels:
  - defaults
dependencies:
  - ca-certificates=2023.08.22=haa95532_0
  - openssl=1.1.1w=h2bbff1b_0
  - pip=23.2.1=py38haa95532_0
  - python=3.8.0=hff0d562_2
  - setuptools=68.0.0=py38haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py38haa95532_0
  - pip:
      - ansi2html==1.8.0
      - anyio==4.2.0
      - asttokens==2.4.1
      - async-timeout==4.0.3
      - attrs==23.1.0
      - backcall==0.2.0
      - blinker==1.7.0
      - certifi==2023.11.17
      - chardet==5.2.0
      - charset-normalizer==3.3.2
      - click==8.1.7
      - colorama==0.4.6
      - colorlog==6.8.2
      - comm==0.2.0
      - configargparse==1.7
      - dash==2.14.1
      - dash-core-components==2.0.0
      - dash-html-components==2.0.0
      - dash-table==5.0.0
      - decorator==5.1.1
      - embreex==2.17.7.post4
      - exceptiongroup==1.2.0
      - executing==2.0.1
      - fastjsonschema==2.19.0
      - flask==3.0.0
      - h11==0.14.0
      - h5py==3.10.0
      - httpcore==1.0.2
      - httpx==0.26.0
      - idna==3.4
      - importlib-metadata==6.8.0
      - importlib-resources==6.1.1
      - ipython==8.12.3
      - ipywidgets==8.1.1
      - itsdangerous==2.1.2
      - jedi==0.19.1
      - jinja2==3.1.2
      - jsonschema==4.20.0
      - jsonschema-specifications==2023.11.1
      - jupyter-core==5.5.0
      - jupyterlab-widgets==3.0.9
      - lxml==5.1.0
      - mapbox-earcut==1.0.1
      - markupsafe==2.1.3
      - matplotlib-inline==0.1.6
      - nbformat==5.7.0
      - nest-asyncio==1.5.8
      - networkx==3.1
      - numpy==1.24.4
      - open3d==0.17.0
      - opencv-python==4.8.1.78
      - packaging==23.2
      - parso==0.8.3
      - pickleshare==0.7.5
      - pillow==10.2.0
      - pkgutil-resolve-name==1.3.10
      - platformdirs==4.0.0
      - plotly==5.18.0
      - prompt-toolkit==3.0.41
      - pure-eval==0.2.2
      - pybullet==3.2.6
      - pycollada==0.8
      - pygments==2.17.1
      - pynput==1.7.6
      - pyopengl==3.1.7
      - pyqt5==5.15.9
      - pyqt5-qt5==5.15.2
      - pyqt5-sip==12.12.2
      - pyqtgraph==0.13.3
      - pyrealsense2==2.53.1.4623
      - python-dateutil==2.8.2
      - pywin32==306
      - pyzmq==25.1.2
      - redis==5.0.1
      - referencing==0.31.0
      - requests==2.31.0
      - retrying==1.3.4
      - rpds-py==0.13.1
      - rtree==1.2.0
      - scipy==1.10.1
      - shapely==2.0.2
      - six==1.16.0
      - sniffio==1.3.0
      - stack-data==0.6.3
      - svg-path==6.3
      - tenacity==8.2.3
      - traitlets==5.13.0
      - transforms3d==0.4.1
      - trimesh==4.1.3
      - typing-extensions==4.8.0
      - urllib3==2.1.0
      - vhacdx==0.0.5
      - wcwidth==0.2.10
      - werkzeug==3.0.1
      - widgetsnbextension==4.0.9
      - xxhash==3.4.1
      - yourdfpy==0.0.56
      - zipp==3.17.0
      - zmq==0.0.0
prefix: C:\Users\jeremy\anaconda3\envs\mocap

```

## Python signatures and reward/observation bodies (102 files)


### STEP3_train_policy/robomimic/__init__.py

```
def register_dataset_link(task, dataset_type, hdf5_type, link, horizon)
def register_all_links()
def register_momart_dataset_link(task, dataset_type, link, dataset_size)
def register_all_momart_links()
```

### STEP3_train_policy/robomimic/algo/algo.py

```
"""This file contains base classes that other algorithm classes subclass.
Each algorithm file also implements a algorithm factory function that
takes in an algorithm config (`config.algo`) and returns the particular
Algo subclass that should be instantiated, along with any extra kwargs.
These factory functions are registered into a global dictionary with the
@register_algo_factory_func function decorator. This makes it easy for
@algo_factory to instantiate the correct `Algo` subclass."""
def register_algo_factory_func(algo_name)
def algo_name_to_factory_func(algo_name)
def algo_factory(algo_name, config, obs_key_shapes, ac_dim, device)
class Algo(object)
    """Base algorithm class that all other algorithms subclass. Defines several
functions that should be overriden by subclasses, in order to provide
a standard API to be used by training functions such as @run_epoch in
utils/train_utils.py."""
    def __init__(self, algo_config, obs_config, global_config, obs_key_shapes, ac_dim, device)
    def _create_shapes(self, obs_keys, obs_key_shapes)
    def _create_networks(self)
    def _create_optimizers(self)
    def process_batch_for_training(self, batch)
    def postprocess_batch_for_training(self, batch, obs_normalization_stats)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def on_epoch_end(self, epoch)
    def set_eval(self)
    def set_train(self)
    def serialize(self)
    def deserialize(self, model_dict)
    def __repr__(self)
    def reset(self)
class PolicyAlgo(Algo)
    """Base class for all algorithms that can be used as policies."""
    def get_action(self, obs_dict, goal_dict)
class ValueAlgo(Algo)
    """Base class for all algorithms that can learn a value function."""
    def get_state_value(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
class PlannerAlgo(Algo)
    """Base class for all algorithms that can be used for planning subgoals
conditioned on current observations and potential goal observations."""
    def get_subgoal_predictions(self, obs_dict, goal_dict)
    def sample_subgoals(self, obs_dict, goal_dict, num_samples)
class HierarchicalAlgo(Algo)
    """Base class for all hierarchical algorithms that consist of (1) subgoal planning
and (2) subgoal-conditioned policy learning."""
    def get_action(self, obs_dict, goal_dict)
    def get_subgoal_predictions(self, obs_dict, goal_dict)
    def current_subgoal(self)
class RolloutPolicy(object)
    """Wraps @Algo object to make it easy to run policies in a rollout loop."""
    def __init__(self, policy, obs_normalization_stats, action_normalization_stats)
    def start_episode(self)
    def _prepare_observation(self, ob)
    def __repr__(self)
    def __call__(self, ob, goal)

```python
def _prepare_observation(self, ob):
        """
        Prepare raw observation dict from environment for policy.

        Args:
            ob (dict): single observation dictionary from environment (no batch dimension, 
                and np.array values for each key)
        """
        ob = TensorUtils.to_tensor(ob)
        ob = TensorUtils.to_batch(ob)
        ob = TensorUtils.to_device(ob, self.policy.device)
        ob = TensorUtils.to_float(ob)
        if self.obs_normalization_stats is not None:
            # ensure obs_normalization_stats are torch Tensors on proper device
            obs_normalization_stats = TensorUtils.to_float(TensorUtils.to_device(TensorUtils.to_tensor(self.obs_normalization_stats), self.policy.device))
            # limit normalization to obs keys being used, in case environment includes extra keys
            ob = { k : ob[k] for k in self.policy.global_config.all_obs_keys }
            ob = ObsUtils.normalize_dict(ob, normalization_stats=obs_normalization_stats)
        return ob
```
```

### STEP3_train_policy/robomimic/algo/bc.py

```
"""Implementation of Behavioral Cloning (BC)."""
def algo_config_to_class(algo_config)
class BC(PolicyAlgo)
    """Normal BC training."""
    def _create_networks(self)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def _forward_training(self, batch)
    def _compute_losses(self, predictions, batch)
    def _train_step(self, losses)
    def log_info(self, info)
    def get_action(self, obs_dict, goal_dict)
class BC_Gaussian(BC)
    """BC training with a Gaussian policy."""
    def _create_networks(self)
    def _forward_training(self, batch)
    def _compute_losses(self, predictions, batch)
    def log_info(self, info)
class BC_GMM(BC_Gaussian)
    """BC training with a Gaussian Mixture Model policy."""
    def _create_networks(self)
class BC_VAE(BC)
    """BC training with a VAE policy."""
    def _create_networks(self)
    def train_on_batch(self, batch, epoch, validate)
    def _forward_training(self, batch)
    def _compute_losses(self, predictions, batch)
    def log_info(self, info)
class BC_RNN(BC)
    """BC training with an RNN policy."""
    def _create_networks(self)
    def process_batch_for_training(self, batch)
    def get_action(self, obs_dict, goal_dict)
    def _compute_losses(self, predictions, batch)
    def reset(self)
class BC_RNN_GMM(BC_RNN)
    """BC training with an RNN GMM policy."""
    def _create_networks(self)
    def _forward_training(self, batch)
    def _compute_losses(self, predictions, batch)
    def log_info(self, info)
class BC_Transformer(BC)
    """BC training with a Transformer policy."""
    def _create_networks(self)
    def _set_params_from_config(self)
    def process_batch_for_training(self, batch)
    def _forward_training(self, batch, epoch)
    def get_action(self, obs_dict, goal_dict)
class BC_Transformer_GMM(BC_Transformer)
    """BC training with a Transformer GMM policy."""
    def _create_networks(self)
    def _forward_training(self, batch, epoch)
    def _compute_losses(self, predictions, batch)
    def log_info(self, info)
```

### STEP3_train_policy/robomimic/algo/bcq.py

```
"""Batch-Constrained Q-Learning (BCQ), with support for more general
generative action models (the original paper uses a cVAE).
(Paper - https://arxiv.org/abs/1812.02900)."""
def algo_config_to_class(algo_config)
class BCQ(PolicyAlgo, ValueAlgo)
    """Default BCQ training, based on https://arxiv.org/abs/1812.02900 and
https://github.com/sfujim/BCQ"""
    def __init__(self)
    def _create_networks(self)
    def _create_critics(self)
    def _create_action_sampler(self)
    def _create_actor(self)
    def _check_epoch(self, net_name, epoch)
    def set_discount(self, discount)
    def process_batch_for_training(self, batch)
    def _train_action_sampler_on_batch(self, batch, epoch, no_backprop)
    def _train_critic_on_batch(self, batch, action_sampler_outputs, epoch, no_backprop)
    def _train_actor_on_batch(self, batch, action_sampler_outputs, critic_outputs, epoch, no_backprop)
    def _get_target_values(self, next_states, goal_states, rewards, dones, action_sampler_outputs)
    def _sample_actions_for_value_maximization(self, states_tiled, goal_states_tiled, for_target_update)
    def _get_target_values_from_sampled_actions(self, next_states_tiled, next_sampled_actions, goal_states_tiled, rewards, dones)
    def _compute_critic_loss(self, critic, states, actions, goal_states, q_targets)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def _log_action_sampler_info(self, info)
    def _log_critic_info(self, info)
    def _log_actor_info(self, info)
    def set_train(self)
    def on_epoch_end(self, epoch)
    def _get_best_value(self, obs_dict, goal_dict)
    def get_action(self, obs_dict, goal_dict)
    def get_state_value(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
class BCQ_GMM(BCQ)
    """A simple modification to BCQ that replaces the VAE used to sample action proposals from the
batch with a GMM."""
    def _create_action_sampler(self)
    def _train_action_sampler_on_batch(self, batch, epoch, no_backprop)
    def _log_action_sampler_info(self, info)
class BCQ_Distributional(BCQ)
    """BCQ with distributional critics. Distributional critics output categorical
distributions over a discrete set of values instead of expected returns.
Some parts of this implementation were adapted from ACME (https://github.com/deepmind/acme)."""
    def _create_critics(self)
    def _get_target_values_from_sampled_actions(self, next_states_tiled, next_sampled_actions, goal_states_tiled, rewards, dones)
    def _compute_critic_loss(self, critic, states, actions, goal_states, q_targets)
```

### STEP3_train_policy/robomimic/algo/cql.py

```
"""Implementation of Conservative Q-Learning (CQL).
Based off of https://github.com/aviralkumar2907/CQL.
(Paper - https://arxiv.org/abs/2006.04779)."""
def algo_config_to_class(algo_config)
class CQL(PolicyAlgo, ValueAlgo)
    """CQL-extension of SAC for the off-policy, offline setting. See https://arxiv.org/abs/2006.04779"""
    def __init__(self)
    def log_entropy_weight(self)
    def log_cql_weight(self)
    def _create_networks(self)
    def _create_optimizers(self)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def _train_policy_on_batch(self, batch, epoch, validate)
    def _train_critic_on_batch(self, batch, epoch, validate)
    def _get_actions_and_log_prob(self, dist, sample_shape)
    def _get_qs_from_actions(obs_dict, actions, goal_dict, q_net)
    def log_info(self, info)
    def _log_critic_info(self, info)
    def _log_actor_info(self, info)
    def set_train(self)
    def on_epoch_end(self, epoch)
    def get_action(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
```

### STEP3_train_policy/robomimic/algo/diffusion_policy.py

```
"""Implementation of Diffusion Policy https://diffusion-policy.cs.columbia.edu/ by Cheng Chi"""
def algo_config_to_class(algo_config)
class DiffusionPolicyUNetDex(PolicyAlgo)
    def _create_networks(self)
    def _adjust_brightness(self, tensor)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def reset(self)
    def get_action(self, obs_dict, goal_dict)
    def _get_action_trajectory(self, obs_dict, goal_dict)
    def serialize(self)
    def deserialize(self, model_dict)
class DiffusionPolicyUNet(PolicyAlgo)
    def _create_networks(self)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def reset(self)
    def get_action(self, obs_dict, goal_dict)
    def _get_action_trajectory(self, obs_dict, goal_dict)
    def serialize(self)
    def deserialize(self, model_dict)
def replace_submodules(root_module, predicate, func)
def replace_bn_with_gn(root_module, features_per_group)
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

### STEP3_train_policy/robomimic/algo/gl.py

```
"""Subgoal prediction models, used in HBC / IRIS."""
def algo_config_to_class(algo_config)
class GL(PlannerAlgo)
    """Implements goal prediction component for HBC and IRIS."""
    def __init__(self, algo_config, obs_config, global_config, obs_key_shapes, ac_dim, device)
    def _create_networks(self)
    def process_batch_for_training(self, batch)
    def get_actor_goal_for_training_from_processed_batch(self, processed_batch)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def get_subgoal_predictions(self, obs_dict, goal_dict)
    def sample_subgoals(self, obs_dict, goal_dict, num_samples)
    def get_action(self, obs_dict, goal_dict)
class GL_VAE(GL)
    """Implements goal prediction via VAE."""
    def _create_networks(self)
    def get_actor_goal_for_training_from_processed_batch(self, processed_batch, use_latent_subgoals, use_prior_correction, num_prior_samples)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def get_subgoal_predictions(self, obs_dict, goal_dict)
    def sample_subgoals(self, obs_dict, goal_dict, num_samples)
class ValuePlanner(PlannerAlgo, ValueAlgo)
    """Base class for all algorithms that are used for planning subgoals
based on (1) a @PlannerAlgo that is used to sample candidate subgoals
and (2) a @ValueAlgo that is used to select one of the subgoals."""
    def __init__(self, planner_algo_class, value_algo_class, algo_config, obs_config, global_config, obs_key_shapes, ac_dim, device)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def on_epoch_end(self, epoch)
    def set_eval(self)
    def set_train(self)
    def serialize(self)
    def deserialize(self, model_dict)
    def reset(self)
    def __repr__(self)
    def get_subgoal_predictions(self, obs_dict, goal_dict)
    def sample_subgoals(self, obs_dict, goal_dict, num_samples)
    def get_state_value(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
```

### STEP3_train_policy/robomimic/algo/hbc.py

```
"""Implementation of Hierarchical Behavioral Cloning, where
a planner model outputs subgoals (future observations), and
an actor model is conditioned on the subgoals to try and
reach them. Largely based on the Generalization Through Imitation (GTI)
paper (see https://arxiv.org/abs/2003.06085)."""
def algo_config_to_class(algo_config)
class HBC(HierarchicalAlgo)
    """Default HBC training, largely based on https://arxiv.org/abs/2003.06085"""
    def __init__(self, planner_algo_class, policy_algo_class, algo_config, obs_config, global_config, obs_key_shapes, ac_dim, device)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def on_epoch_end(self, epoch)
    def set_eval(self)
    def set_train(self)
    def serialize(self)
    def deserialize(self, model_dict)
    def current_subgoal(self)
    def current_subgoal(self, sg)
    def get_action(self, obs_dict, goal_dict)
    def reset(self)
    def __repr__(self)
```

### STEP3_train_policy/robomimic/algo/iql.py

```
"""Implementation of Implicit Q-Learning (IQL).
Based off of https://github.com/rail-berkeley/rlkit/blob/master/rlkit/torch/sac/iql_trainer.py.
(Paper - https://arxiv.org/abs/2110.06169)."""
def algo_config_to_class(algo_config)
class IQL(PolicyAlgo, ValueAlgo)
    def _create_networks(self)
    def process_batch_for_training(self, batch)
    def train_on_batch(self, batch, epoch, validate)
    def _compute_critic_loss(self, batch)
    def _update_critic(self, critic_losses, vf_loss)
    def _compute_actor_loss(self, batch, critic_info)
    def _update_actor(self, actor_loss)
    def _get_adv_weights(self, adv)
    def log_info(self, info)
    def _log_data_attributes(self, log, info, key)
    def on_epoch_end(self, epoch)
    def get_action(self, obs_dict, goal_dict)
```

### STEP3_train_policy/robomimic/algo/iris.py

```
"""Implementation of IRIS (https://arxiv.org/abs/1911.05321)."""
def algo_config_to_class(algo_config)
class IRIS(HBC, ValueAlgo)
    """Implementation of IRIS (https://arxiv.org/abs/1911.05321)."""
    def __init__(self, planner_algo_class, value_algo_class, policy_algo_class, algo_config, obs_config, global_config, obs_key_shapes, ac_dim, device)
    def process_batch_for_training(self, batch)
    def get_state_value(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
```

### STEP3_train_policy/robomimic/algo/td3_bc.py

```
"""Implementation of TD3-BC. 
Based on https://github.com/sfujim/TD3_BC
(Paper - https://arxiv.org/abs/1812.02900).

Note that several parts are exactly the same as the BCQ implementation,
such as @_create_critics, @process_batch_for_training, and 
@_train_critic_on_batch. They are replicated here (instead of subclassing 
from the BCQ algo class) to be explicit and have implementation details 
self-contained in this file."""
def algo_config_to_class(algo_config)
class TD3_BC(PolicyAlgo, ValueAlgo)
    """Default TD3_BC training, based on https://arxiv.org/abs/2106.06860 and
https://github.com/sfujim/TD3_BC."""
    def __init__(self)
    def _create_networks(self)
    def _create_critics(self)
    def _create_actor(self)
    def _check_epoch(self, net_name, epoch)
    def set_discount(self, discount)
    def process_batch_for_training(self, batch)
    def _train_critic_on_batch(self, batch, epoch, no_backprop)
    def _train_actor_on_batch(self, batch, epoch, no_backprop)
    def _get_target_values(self, next_states, goal_states, rewards, dones)
    def _compute_critic_loss(self, critic, states, actions, goal_states, q_targets)
    def train_on_batch(self, batch, epoch, validate)
    def log_info(self, info)
    def _log_critic_info(self, info)
    def _log_actor_info(self, info)
    def set_train(self)
    def on_epoch_end(self, epoch)
    def get_action(self, obs_dict, goal_dict)
    def get_state_value(self, obs_dict, goal_dict)
    def get_state_action_value(self, obs_dict, actions, goal_dict)
```

### STEP3_train_policy/robomimic/config/base_config.py

```
"""The base config class that is used for all algorithm configs in this repository.
Subclasses get registered into a global dictionary, making it easy to instantiate
the correct config class given the algorithm name."""
def get_all_registered_configs()
def config_factory(algo_name, dic)
class ConfigMeta(type)
    """Define a metaclass for constructing a config class.
It registers configs into the global registry."""
    def __new__(meta, name, bases, class_dict)
class BaseConfig(Config)
    def __init__(self, dict_to_load)
    def ALGO_NAME(cls)
    def experiment_config(self)
    def train_config(self)
    def algo_config(self)
    def observation_config(self)
    def meta_config(self)
    def use_goals(self)
    def all_obs_keys(self)

```python
def observation_config(self):
        """
        This function populates the `config.observation` attribute of the config, and is given 
        to the `Algo` subclass (see `algo/algo.py`) for each algorithm through the `obs_config` 
        argument to the constructor. This portion of the config is used to specify what 
        observation modalities should be used by the networks for training, and how the 
        observation modalities should be encoded by the networks. While this class has a 
        default implementation that usually doesn't need to be overriden, certain algorithm 
        configs may choose to, in order to have seperate configs for different networks 
        in the algorithm. 
        """

        # observation modalities
        self.observation.modalities.obs.low_dim = [             # specify low-dim observations for agent
            "robot0_eef_pos", 
            "robot0_eef_quat", 
            "robot0_gripper_qpos", 
            "object",
        ]
        self.observation.modalities.obs.rgb = []              # specify rgb image observations for agent
        self.observation.modalities.obs.depth = []
        self.observation.modalities.obs.scan = []
        self.observation.modalities.goal.low_dim = []           # specify low-dim goal observations to condition agent on
        self.observation.modalities.goal.rgb = []             # specify rgb image goal observations to condition agent on
        self.observation.modalities.goal.depth = []
        self.observation.modalities.goal.scan = []
        self.observation.modalities.obs.do_not_lock_keys()
        self.observation.modalities.goal.do_not_lock_keys()

        # observation encoder architectures (per obs modality)
        # This applies to all networks that take observation dicts as input

        # =============== Low Dim default encoder (no encoder) ===============
        self.observation.encoder.low_dim.core_class = None
        self.observation.encoder.low_dim.core_kwargs = Config()                 # No kwargs by default
        self.observation.encoder.low_dim.core_kwargs.do_not_lock_keys()

        # Low Dim: Obs Randomizer settings
        self.observation.encoder.low_dim.obs_randomizer_class = None
        self.observation.encoder.low_dim.obs_randomizer_kwargs = Config()       # No kwargs by default
        self.observation.encoder.low_dim.obs_randomizer_kwargs.do_not_lock_keys()

        # =============== RGB default encoder (ResNet backbone + linear layer output) ===============
        self.observation.encoder.rgb.core_class = "VisualCore"                  # Default VisualCore class combines backbone (like ResNet-18) with pooling operation (like spatial softmax)
        self.observation.encoder.rgb.core_kwargs = Config()                     # See models/obs_core.py for important kwargs to set and defaults used
        self.observation.encoder.rgb.core_kwargs.do_not_lock_keys()

        # RGB: Obs Randomizer settings
        self.observation.encoder.rgb.obs_randomizer_class = None                # Can set to 'CropRandomizer' to use crop randomization
        self.observation.encoder.rgb.obs_randomizer_kwargs = Config()           # See models/obs_core.py for important kwargs to set and defaults used
        self.observation.encoder.rgb.obs_randomizer_kwargs.do_not_lock_keys()

        # Allow for other custom modalities to be specified
        self.observation.encoder.do_not_lock_keys()

        # =============== Depth default encoder (same as rgb) ===============
        self.observation.encoder.depth = deepcopy(self.observation.encoder.rgb)

        # =============== Scan default encoder (Conv1d backbone + linear layer output) ===============
        self.observation.encoder.scan = deepcopy(self.observation.encoder.rgb)

        # Scan: Modify the core class + kwargs, otherwise, is same as rgb encoder
        self.observation.encoder.scan.core_class = "ScanCore"                   # Default ScanCore class uses Conv1D to process t
```
```

### STEP3_train_policy/robomimic/config/bc_config.py

```
"""Config for BC algorithm."""
class BCConfig(BaseConfig)
    def train_config(self)
    def algo_config(self)
```

### STEP3_train_policy/robomimic/config/bcq_config.py

```
"""Config for BCQ algorithm."""
class BCQConfig(BaseConfig)
    def algo_config(self)
```

### STEP3_train_policy/robomimic/config/config.py

```
"""Basic config class - provides a convenient way to work with nested
dictionaries (by exposing keys as attributes) and to save / load from jsons.

Based on addict: https://github.com/mewwts/addict"""
class Config(dict)
    def __init__(__self)
    def lock(self)
    def unlock(self)
    def _get_lock_state_recursive(self)
    def _set_lock_state_recursive(self, lock_state)
    def _get_lock_state(self)
    def _set_lock_state(self, lock_state)
    def unlocked(self)
    def values_unlocked(self)
    def lock_keys(self)
    def unlock_keys(self)
    def is_locked(self)
    def is_key_locked(self)
    def do_not_lock_keys(self)
    def key_lockable(self)
    def __setattr__(self, name, value)
    def __setitem__(self, name, value)
    def __add__(self, other)
    def _hook(cls, item)
    def __getattr__(self, item)
    def __repr__(self)
    def __getitem__(self, name)
    def __delattr__(self, name)
    def to_dict(self)
    def copy(self)
    def deepcopy(self)
    def __deepcopy__(self, memo)
    def update(self)
    def __getnewargs__(self)
    def __getstate__(self)
    def __setstate__(self, state)
    def setdefault(self, key, default)
    def dump(self, filename)
```

### STEP3_train_policy/robomimic/config/cql_config.py

```
"""Config for CQL algorithm."""
class CQLConfig(BaseConfig)
    def train_config(self)
    def algo_config(self)
```

### STEP3_train_policy/robomimic/config/diffusion_policy_config.py

```
"""Config for Diffusion Policy algorithm."""
class DiffusionPolicyConfig(BaseConfig)
    def algo_config(self)
```

### STEP3_train_policy/robomimic/config/gl_config.py

```
"""Config for Goal Learning (sub-algorithm used by hierarchical models like HBC and IRIS).
This class of model predicts (or samples) subgoal observations given a current observation."""
class GLConfig(BaseConfig)
    def algo_config(self)
    def observation_config(self)
    def all_obs_keys(self)

```python
def observation_config(self):
        """
        Update from superclass to specify subgoal modalities.
        """
        super(GLConfig, self).observation_config()
        self.observation.modalities.subgoal.low_dim = [                     # specify low-dim subgoal observations for agent to predict
            "robot0_eef_pos", 
            "robot0_eef_quat", 
            "robot0_gripper_qpos", 
            "object",
        ]
        self.observation.modalities.subgoal.rgb = []                      # specify rgb image subgoal observations for agent to predict
        self.observation.modalities.subgoal.depth = []
        self.observation.modalities.subgoal.scan = []
        self.observation.modalities.subgoal.do_not_lock_keys()
```
```

### STEP3_train_policy/robomimic/config/hbc_config.py

```
"""Config for HBC algorithm."""
class HBCConfig(BaseConfig)
    def train_config(self)
    def algo_config(self)
    def observation_config(self)
    def use_goals(self)
    def all_obs_keys(self)

```python
def observation_config(self):
        """
        Update from superclass so that planner and actor each get their own observation config.
        """
        self.observation.planner = GLConfig().observation
        self.observation.actor = BCConfig().observation
```
```

### STEP3_train_policy/robomimic/config/iql_config.py

```
"""Config for IQL algorithm."""
class IQLConfig(BaseConfig)
    def algo_config(self)
```

### STEP3_train_policy/robomimic/config/iris_config.py

```
"""Config for IRIS algorithm."""
class IRISConfig(HBCConfig)
    def algo_config(self)
    def observation_config(self)
    def use_goals(self)
    def all_obs_keys(self)

```python
def observation_config(self):
        """
        Update from superclass so that value planner and actor each get their own obs config.
        """
        self.observation.value_planner.planner = GLConfig().observation
        self.observation.value_planner.value = BCQConfig().observation
        self.observation.actor = BCConfig().observation
```
```

### STEP3_train_policy/robomimic/config/td3_bc_config.py

```
"""Config for TD3_BC."""
class TD3_BCConfig(BaseConfig)
    def experiment_config(self)
    def train_config(self)
    def algo_config(self)
    def observation_config(self)

```python
def observation_config(self):
        """
        Update from superclass to use flat observations from gym envs.
        """
        super(TD3_BCConfig, self).observation_config()
        self.observation.modalities.obs.low_dim = ["flat"]
```
```

### STEP3_train_policy/robomimic/envs/env_base.py

```
"""This file contains the base class for environment wrappers that are used
to provide a standardized environment API for training policies and interacting
with metadata present in datasets."""
class EnvType()
    """Holds environment types - one per environment class.
These act as identifiers for different environments."""
class EnvBase(ABC)
    """A base class method for environments used by this repo."""
    def __init__(self, env_name, render, render_offscreen, use_image_obs, use_depth_obs, postprocess_visual_obs)
    def step(self, action)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, height, width, camera_name)
    def get_observation(self)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def action_dimension(self)
    def name(self)
    def type(self)
    def version(self)
    def serialize(self)
    def create_for_data_processing(cls, camera_names, camera_height, camera_width, reward_shaping, render, render_offscreen, use_image_obs, use_depth_obs)
    def rollout_exceptions(self)
    def base_env(self)

```python
def get_observation(self):
        """Get environment observation"""
        return
```

```python
def get_reward(self):
        """
        Get current reward.
        """
        return
```
```

### STEP3_train_policy/robomimic/envs/env_gym.py

```
"""This file contains the gym environment wrapper that is used
to provide a standardized environment API for training policies and interacting
with metadata present in datasets."""
class EnvGym(EnvBase)
    """Wrapper class for gym"""
    def __init__(self, env_name, render, render_offscreen, use_image_obs, use_depth_obs, postprocess_visual_obs)
    def step(self, action)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, height, width, camera_name)
    def get_observation(self, obs)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def action_dimension(self)
    def name(self)
    def type(self)
    def serialize(self)
    def create_for_data_processing(cls, env_name, camera_names, camera_height, camera_width, reward_shaping, render, render_offscreen, use_image_obs, use_depth_obs)
    def rollout_exceptions(self)
    def base_env(self)
    def __repr__(self)

```python
def get_observation(self, obs=None):
        """
        Get current environment observation dictionary.

        Args:
            ob (np.array): current flat observation vector to wrap and provide as a dictionary.
                If not provided, uses self._current_obs.
        """
        if obs is None:
            assert self._current_obs is not None
            obs = self._current_obs
        return { "flat" : np.copy(obs) }
```

```python
def get_reward(self):
        """
        Get current reward.
        """
        assert self._current_reward is not None
        return self._current_reward
```
```

### STEP3_train_policy/robomimic/envs/env_ig_momart.py

```
"""Wrapper environment class to enable using iGibson-based environments used in the MOMART paper"""
class EnvGibsonMOMART(EnvBase)
    """Wrapper class for gibson environments (https://github.com/StanfordVL/iGibson) specifically compatible with
MoMaRT datasets"""
    def __init__(self, env_name, ig_config, postprocess_visual_obs, render, render_offscreen, use_image_obs, use_depth_obs, image_height, image_width, physics_timestep, action_timestep)
    def step(self, action)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, camera_name, height, width)
    def resize_obs_frame(self, frame)
    def get_observation(self, di)
    def sync_task(self)
    def set_task_conditions(self, task_conditions)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def create_for_data_processing(cls, env_name, camera_names, camera_height, camera_width, reward_shaping, render, render_offscreen, use_image_obs, use_depth_obs)
    def action_dimension(self)
    def name(self)
    def type(self)
    def serialize(self)
    def deserialize(cls, info, postprocess_visual_obs)
    def rollout_exceptions(self)
    def base_env(self)
    def __repr__(self)

```python
def get_observation(self, di=None):
        """Get environment observation"""
        if di is None:
            di = self.env.get_state()
        ret = {}
        for k in di:
            # RGB Images
            if "rgb" in k:
                ret[k] = di[k]
                # ret[k] = np.transpose(di[k], (2, 0, 1))
                if self.postprocess_visual_obs:
                    ret[k] = ObsUtils.process_obs(obs=self.resize_obs_frame(ret[k]), obs_key=k)

            # Depth images
            elif "depth" in k:
                # ret[k] = np.transpose(di[k], (2, 0, 1))
                # Values can be corrupted (negative or > 1.0, so we clip values)
                ret[k] = np.clip(di[k], 0.0, 1.0)
                if self.postprocess_visual_obs:
                    ret[k] = ObsUtils.process_obs(obs=self.resize_obs_frame(ret[k])[..., None], obs_key=k)

            # Segmentation Images
            elif "seg" in k:
                ret[k] = di[k][..., None]
                if self.postprocess_visual_obs:
                    ret[k] = ObsUtils.process_obs(obs=self.resize_obs_frame(ret[k]), obs_key=k)

            # Scans
            elif "scan" in k:
                ret[k] = np.transpose(np.array(di[k]), axes=(1, 0))

        # Compose proprio obs
        proprio_obs = di["proprio"]

        # Compute intermediate values
        lin_vel = np.linalg.norm(proprio_obs["base_lin_vel"][:2])
        ang_vel = proprio_obs["base_ang_vel"][2]

        ret["proprio"] = np.concatenate([
            proprio_obs["head_joint_pos"],
            proprio_obs["grasped"],
            proprio_obs["eef_pos"],
            proprio_obs["eef_quat"],
        ])

        # Proprio info that's only relevant for navigation
        ret["proprio_nav"] = np.concatenate([
            [lin_vel],
            [ang_vel],
        ])

        # Compose task obs
        ret["object"] = np.concatenate([
            np.array(di["task_obs"]["object-state"]),
        ])

        # Add ground truth navigational state
        ret["gt_nav"] = np.concatenate([
            proprio_obs["base_pos"][:2],
            [np.sin(proprio_obs["base_rpy"][2])],
            [np.cos(proprio_obs["base_rpy"][2])],
        ])

        return ret
```

```python
def get_reward(self):
        return self.env.task.get_reward(self.env)[0]
```
```

### STEP3_train_policy/robomimic/envs/env_real_panda.py

```
"""This file contains the base class for environment wrappers that are used
to provide a standardized environment API for training policies and interacting
with metadata present in datasets."""
class EnvRealPanda(EnvBase)
    """Wrapper class for real panda environment"""
    def __init__(self, env_name, render, render_offscreen, use_image_obs, use_depth_obs, postprocess_visual_obs, control_freq, action_scale, camera_names_to_sizes, init_ros_node, publish_target_pose, fake_controller, use_moveit)
    def _compile_jit_functions(self)
    def step(self, action, need_obs)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, height, width, camera_name)
    def get_observation(self, obs)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def action_dimension(self)
    def name(self)
    def type(self)
    def serialize(self)
    def create_for_data_processing(cls, env_name, camera_names, camera_height, camera_width, reward_shaping)
    def rollout_exceptions(self)
    def base_env(self)
    def __repr__(self)

```python
def get_observation(self, obs=None):
        """
        Get current environment observation dictionary.

        Args:
            ob (np.array): current observation dictionary.
        """
        self.timers.tic("get_observation")
        observation = {}
        observation["ee_pose"] = np.concatenate(self.robot_interface.ee_pose)
        observation["joint_positions"] = self.robot_interface.joint_position
        observation["joint_velocities"] = self.robot_interface.joint_velocity
        observation["gripper_position"] = self.robot_interface.gripper_position
        observation["gripper_velocity"] = self.robot_interface.gripper_velocity
        for cam_name in self.camera_names_to_sizes:
            im = self.robot_interface.get_camera_frame(camera_name=cam_name)
            if self.postprocess_visual_obs:
                im = ObsUtils.process_image(im)
            observation[cam_name] = im
        self.timers.toc("get_observation")
        return observation
```

```python
def get_reward(self):
        """
        Get current reward.
        """
        return 0.
```
```

### STEP3_train_policy/robomimic/envs/env_real_panda_gprs.py

```
"""Real robot env wrapper for Yifeng's GPRS control stack."""
def center_crop(im, t_h, t_w)
def get_depth_scale(camera_name)
class EnvRealPandaGPRS(EnvBase)
    """Wrapper class for real panda environment"""
    def __init__(self, env_name, render, render_offscreen, use_image_obs, postprocess_visual_obs, control_freq, camera_names_to_sizes, center_crop_images, general_cfg_file, controller_type, controller_cfg_file, controller_cfg_dict, use_depth_obs, absolute_actions, state_freq, control_timeout, has_gripper, use_visualizer, debug)
    def _compile_jit_functions(self)
    def _get_unified_getter(self)
    def switch_controllers(self, controller_dict)
    def step(self, action, need_obs)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, height, width, camera_name)
    def get_observation(self, obs)
    def _get_image(self, camera_name)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def action_dimension(self)
    def action_dim(self)
    def name(self)
    def type(self)
    def serialize(self)
    def create_for_data_processing(cls, env_name, camera_names, camera_height, camera_width, reward_shaping, render, render_offscreen, use_image_obs, use_depth_obs)
    def rollout_exceptions(self)
    def base_env(self)
    def __repr__(self)
    def close(self)

```python
def get_observation(self, obs=None):
        """
        Get current environment observation dictionary.

        Args:
            ob (np.array): current observation dictionary.
        """
        self.timers.tic("get_observation")
        observation = {}
        last_robot_state = self.robot_interface._state_buffer[-1]
        last_gripper_state = self.robot_interface._gripper_state_buffer[-1]
        ee_pose = np.array(last_robot_state.O_T_EE).reshape((4, 4)).T
        if np.count_nonzero(ee_pose.reshape(-1)) == 0:
            raise Exception("GOT ZERO EE POSE")
        ee_pos = ee_pose[:3, 3]
        ee_quat = U.mat2quat(ee_pose[:3, :3])
        observation["ee_pose"] = np.concatenate([ee_pos, ee_quat])
        observation["joint_positions"] = np.array(last_robot_state.q)
        observation["joint_velocities"] = np.array(last_robot_state.dq)
        observation["gripper_position"] = np.array(last_gripper_state.width)
        # observation["gripper_velocity"] = self.robot_interface.gripper_velocity
        for cam_name in self.camera_names_to_sizes:
            im = self._get_image(camera_name=cam_name)
            if self.use_depth_obs:
                im, depth_im = im
                # im, depth_im, depth_im_unaligned = im
                # observation[cam_name + "_depth"] = depth_im
                # observation[cam_name + "_unaligned_depth"] = depth_im_unaligned
                if (not self._exclude_depth_from_obs):
                    depth_im_mod = cam_name + "_depth"
                    if self.postprocess_visual_obs and (depth_im_mod in ObsUtils.OBS_KEYS_TO_MODALITIES) and ObsUtils.key_is_obs_modality(key=depth_im_mod, obs_modality="depth"):
                        depth_im = ObsUtils.process_obs(obs=depth_im, obs_key=depth_im_mod)
                    observation[depth_im_mod] = depth_im
            im = im[..., ::-1]
            if self.postprocess_visual_obs:
                # NOTE: commented out for now, since run-trained-agent was running into issues with unneeded agent modalities that were present in @self.camera_names_to_sizes
                # assert (cam_name in ObsUtils.OBS_KEYS_TO_MODALITIES) and ObsUtils.key_is_obs_modality(key=cam_name, obs_modality="rgb")
                im = ObsUtils.process_obs(obs=im, obs_key=cam_name)
            observation[cam_name] = im
        self.timers.toc("get_observation")
        return observation
```

```python
def get_reward(self):
        """
        Get current reward.
        """
        return 0.
```
```

### STEP3_train_policy/robomimic/envs/env_robosuite.py

```
"""This file contains the robosuite environment wrapper that is used
to provide a standardized environment API for training policies and interacting
with metadata present in datasets."""
class EnvRobosuite(EnvBase)
    """Wrapper class for robosuite environments (https://github.com/ARISE-Initiative/robosuite)"""
    def __init__(self, env_name, render, render_offscreen, use_image_obs, use_depth_obs, postprocess_visual_obs)
    def step(self, action)
    def reset(self)
    def reset_to(self, state)
    def render(self, mode, height, width, camera_name)
    def get_observation(self, di)
    def get_real_depth_map(self, depth_map)
    def get_camera_intrinsic_matrix(self, camera_name, camera_height, camera_width)
    def get_camera_extrinsic_matrix(self, camera_name)
    def get_camera_transform_matrix(self, camera_name, camera_height, camera_width)
    def get_state(self)
    def get_reward(self)
    def get_goal(self)
    def set_goal(self)
    def is_done(self)
    def is_success(self)
    def action_dimension(self)
    def name(self)
    def type(self)
    def version(self)
    def serialize(self)
    def create_for_data_processing(cls, env_name, camera_names, camera_height, camera_width, reward_shaping, render, render_offscreen, use_image_obs, use_depth_obs)
    def rollout_exceptions(self)
    def base_env(self)
    def __repr__(self)

```python
def get_observation(self, di=None):
        """
        Get current environment observation dictionary.

        Args:
            di (dict): current raw observation dictionary from robosuite to wrap and provide 
                as a dictionary. If not provided, will be queried from robosuite.
        """
        if di is None:
            di = self.env._get_observations(force_update=True) if self._is_v1 else self.env._get_observation()
        ret = {}
        for k in di:
            if (k in ObsUtils.OBS_KEYS_TO_MODALITIES) and ObsUtils.key_is_obs_modality(key=k, obs_modality="rgb"):
                ret[k] = di[k][::-1]
                if self.postprocess_visual_obs:
                    ret[k] = ObsUtils.process_obs(obs=ret[k], obs_key=k)
            elif (k in ObsUtils.OBS_KEYS_TO_MODALITIES) and ObsUtils.key_is_obs_modality(key=k, obs_modality="depth"):
                ret[k] = di[k][::-1]
                if len(ret[k].shape) == 2:
                    ret[k] = ret[k][..., None] # (H, W, 1)
                assert len(ret[k].shape) == 3 
                # scale entries in depth map to correspond to real distance.
                ret[k] = self.get_real_depth_map(ret[k])
                if self.postprocess_visual_obs:
                    ret[k] = ObsUtils.process_obs(obs=ret[k], obs_key=k)

        # "object" key contains object information
        ret["object"] = np.array(di["object-state"])

        if self._is_v1:
            for robot in self.env.robots:
                # add all robot-arm-specific observations. Note the (k not in ret) check
                # ensures that we don't accidentally add robot wrist images a second time
                pf = robot.robot_model.naming_prefix
                for k in di:
                    if k.startswith(pf) and (k not in ret) and (not k.endswith("proprio-state")):
                        ret[k] = np.array(di[k])
        else:
            # minimal proprioception for older versions of robosuite
            ret["proprio"] = np.array(di["robot-state"])
            ret["eef_pos"] = np.array(di["eef_pos"])
            ret["eef_quat"] = np.array(di["eef_quat"])
            ret["gripper_qpos"] = np.array(di["gripper_qpos"])
        return ret
```

```python
def get_reward(self):
        """
        Get current reward.
        """
        return self.env.reward()
```
```

### STEP3_train_policy/robomimic/envs/wrappers.py

```
"""A collection of useful environment wrappers."""
class EnvWrapper(object)
    """Base class for all environment wrappers in robomimic."""
    def __init__(self, env)
    def class_name(cls)
    def _warn_double_wrap(self)
    def unwrapped(self)
    def _to_string(self)
    def __repr__(self)
    def __getattr__(self, attr)
class FrameStackWrapper(EnvWrapper)
    """Wrapper for frame stacking observations during rollouts. The agent
receives a sequence of past observations instead of a single observation
when it calls @env.reset, @env.reset_to, or @env.step in the rollout loop."""
    def __init__(self, env, num_frames)
    def _get_initial_obs_history(self, init_obs)
    def _get_stacked_obs_from_history(self)
    def cache_obs_history(self)
    def uncache_obs_history(self)
    def reset(self)
    def reset_to(self, state)
    def step(self, action)
    def update_obs(self, obs, action, reset)
    def _to_string(self)
```

### STEP3_train_policy/robomimic/macros.py

```
"""Set of global variables shared across robomimic"""
```

### STEP3_train_policy/robomimic/macros_private.py

```
"""Set of global variables shared across robomimic"""
```

### STEP3_train_policy/robomimic/models/base_nets.py

```
"""Contains torch Modules that correspond to basic network building blocks, like 
MLP, RNN, and CNN backbones."""
def rnn_args_from_config(rnn_config)
def transformer_args_from_config(transformer_config)
class Module(Module)
    """Base class for networks. The only difference from torch.nn.Module is that it
requires implementing @output_shape."""
    def output_shape(self, input_shape)
class Sequential(Sequential, Module)
    """Compose multiple Modules together (defined above)."""
    def __init__(self)
    def output_shape(self, input_shape)
    def freeze(self)
    def train(self, mode)
class Parameter(Module)
    """A class that is a thin wrapper around a torch.nn.Parameter to make for easy saving
and optimization."""
    def __init__(self, init_tensor)
    def output_shape(self, input_shape)
    def forward(self, inputs)
class Unsqueeze(Module)
    """Trivial class that unsqueezes the input. Useful for including in a nn.Sequential network"""
    def __init__(self, dim)
    def output_shape(self, input_shape)
    def forward(self, x)
class Squeeze(Module)
    """Trivial class that squeezes the input. Useful for including in a nn.Sequential network"""
    def __init__(self, dim)
    def output_shape(self, input_shape)
    def forward(self, x)
class MLP(Module)
    """Base class for simple Multi-Layer Perceptrons."""
    def __init__(self, input_dim, output_dim, layer_dims, layer_func, layer_func_kwargs, activation, dropouts, normalization, output_activation)
    def output_shape(self, input_shape)
    def forward(self, inputs)
    def __repr__(self)
class PointNet(Module)
    """PointNet class for processing point clouds."""
    def __init__(self, input_dim, output_dim, layer_dims, activation, normalization, global_feature, output_activation)
    def forward(self, x)
    def output_shape(self, input_shape)
    def __repr__(self)
class SetTransformer(Module)
    """PointNet class for processing point clouds."""
    def __init__(self, dim_input, num_outputs, dim_output, num_inds, dim_hidden, num_heads, ln, dropout_rate)
    def forward(self, X)
    def output_shape(self, input_shape)
    def __repr__(self)
class SetXFPCDEncoder(Module)
    def __init__(self, n_coordinates, add_ee_embd, ee_embd_dim, hidden_dim, output_dim, set_xf_num_heads, set_xf_num_queries, set_xf_layer_norm)
    def forward(self, x)
    def output_shape(self, input_shape)
    def __repr__(self)
class RNN_Base(Module)
    """A wrapper class for a multi-step RNN and a per-step network."""
    def __init__(self, input_dim, rnn_hidden_dim, rnn_num_layers, rnn_type, rnn_kwargs, per_step_net)
    def rnn_type(self)
    def get_rnn_init_state(self, batch_size, device)
    def output_shape(self, input_shape)
    def forward(self, inputs, rnn_init_state, return_state)
    def forward_step(self, inputs, rnn_state)
class ConvBase(Module)
    """Base class for ConvNets."""
    def __init__(self)
    def output_shape(self, input_shape)
    def forward(self, inputs)
class ResNet18Conv(ConvBase)
    """A ResNet18 block that can be used to process input images."""
    def __init__(self, input_channel, pretrained, input_coord_conv)
    def output_shape(self, input_shape)
    def __repr__(self)
class R3MConv(ConvBase)
    """Base class for ConvNets pretrained with R3M (https://arxiv.org/abs/2203.12601)"""
    def __init__(self, input_channel, r3m_model_class, freeze)
    def output_shape(self, input_shape)
    def __repr__(self)
class MVPConv(ConvBase)
    """Base class for ConvNets pretrained with MVP (https://arxiv.org/abs/2203.06173)"""
    def __init__(self, input_channel, mvp_model_class, freeze)
    def forward(self, inputs)
    def output_shape(self, input_shape)
    def __repr__(self)
class CoordConv2d(Conv2d, Module)
    """2D Coordinate Convolution

Source: An Intriguing Failing of Convolutional Neural Networks and the CoordConv Solution
https://arxiv.org/abs/1807.03247
(e.g. adds 2 channels per input feature map corresponding to (x, y) location on map)"""
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode, coord_encoding)
    def output_shape(self, input_shape)
    def forward(self, input)
class ShallowConv(ConvBase)
    """A shallow convolutional encoder from https://rll.berkeley.edu/dsae/dsae.pdf"""
    def __init__(self, input_channel, output_channel)
    def output_shape(self, input_shape)
class Conv1dBase(Module)
    """Base class for stacked Conv1d layers.

Args:
    input_channel (int): Number of channels for inputs to this network
    activation (None or str): Per-layer activation to use. Defaults to "relu". Valid options are
        currently {relu, None} for no activation
    out_channels (list of int): Output"""
    def __init__(self, input_channel, activation, out_channels, kernel_size, stride)
    def output_shape(self, input_shape)
    def forward(self, inputs)
class SpatialSoftmax(ConvBase)
    """Spatial Softmax Layer.

Based on Deep Spatial Autoencoders for Visuomotor Learning by Finn et al.
https://rll.berkeley.edu/dsae/dsae.pdf"""
    def __init__(self, input_shape, num_kp, temperature, learnable_temperature, output_variance, noise_std)
    def __repr__(self)
    def output_shape(self, input_shape)
    def forward(self, feature)
class SpatialMeanPool(Module)
    """Module that averages inputs across all spatial dimensions (dimension 2 and after),
leaving only the batch and channel dimensions."""
    def __init__(self, input_shape)
    def output_shape(self, input_shape)
    def forward(self, inputs)
class FeatureAggregator(Module)
    """Helpful class for aggregating features across a dimension. This is useful in 
practice when training models that break an input image up into several patches
since features can be extraced per-patch using the same encoder and then 
aggregated using this module."""
    def __init__(self, dim, agg_type)
    def set_weight(self, w)
    def clear_weight(self)
    def output_shape(self, input_shape)
    def forward(self, x)
```

### STEP3_train_policy/robomimic/models/distributions.py

```
"""Contains distribution models used as parts of other networks. These
classes usually inherit or emulate torch distributions."""
class TanhWrappedDistribution(Distribution)
    """Class that wraps another valid torch distribution, such that sampled values from the base distribution are
passed through a tanh layer. The corresponding (log) probabilities are also modified accordingly.
Tanh Normal distribution - adapted from rlkit and CQL codebase
(https://github.com/aviralkumar2"""
    def __init__(self, base_dist, scale, epsilon)
    def log_prob(self, value, pre_tanh_value)
    def sample(self, sample_shape, return_pretanh_value)
    def rsample(self, sample_shape, return_pretanh_value)
    def mean(self)
    def stddev(self)
class DiscreteValueDistribution(object)
    """Extension to torch categorical probability distribution in order to keep track
of the support (categorical values, or in this case, value atoms). This is
used for distributional value networks."""
    def __init__(self, values, probs, logits)
    def values(self)
    def probs(self)
    def logits(self)
    def mean(self)
    def variance(self)
    def sample(self, sample_shape)
```

### STEP3_train_policy/robomimic/models/obs_core.py

```
"""Contains torch Modules for core observation processing blocks
such as encoders (e.g. EncoderCore, VisualCore, ScanCore, ...)
and randomizers (e.g. Randomizer, CropRandomizer)."""
class EncoderCore(Module)
    """Abstract class used to categorize all cores used to encode observations"""
    def __init__(self, input_shape)
    def __init_subclass__(cls)
class VisualCore(EncoderCore, ConvBase)
    """A network block that combines a visual backbone network with optional pooling
and linear layers."""
    def __init__(self, input_shape, backbone_class, pool_class, backbone_kwargs, pool_kwargs, flatten, feature_dimension)
    def output_shape(self, input_shape)
    def forward(self, inputs)
    def __repr__(self)
class ScanCore(EncoderCore, ConvBase)
    """A network block that combines a Conv1D backbone network with optional pooling
and linear layers."""
    def __init__(self, input_shape, conv_kwargs, conv_activation, pool_class, pool_kwargs, flatten, feature_dimension)
    def output_shape(self, input_shape)
    def forward(self, inputs)
    def __repr__(self)
class Randomizer(Module)
    """Base class for randomizer networks. Each randomizer should implement the @output_shape_in,
@output_shape_out, @forward_in, and @forward_out methods. The randomizer's @forward_in
method is invoked on raw inputs, and @forward_out is invoked on processed inputs
(usually processed by a @VisualCore insta"""
    def __init__(self)
    def __init_subclass__(cls)
    def output_shape(self, input_shape)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def forward_in(self, inputs)
    def forward_out(self, inputs)
    def _forward_in(self, inputs)
    def _forward_in_eval(self, inputs)
    def _forward_out(self, inputs)
    def _forward_out_eval(self, inputs)
    def _visualize(self, pre_random_input, randomized_input, num_samples_to_visualize)
class CropRandomizer(Randomizer)
    """Randomly sample crops at input, and then average across crop features at output."""
    def __init__(self, input_shape, crop_height, crop_width, num_crops, pos_enc)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def _forward_in(self, inputs)
    def _forward_in_eval(self, inputs)
    def _forward_out(self, inputs)
    def _visualize(self, pre_random_input, randomized_input, num_samples_to_visualize)
    def __repr__(self)
class ColorRandomizer(Randomizer)
    """Randomly sample color jitter at input, and then average across color jtters at output."""
    def __init__(self, input_shape, brightness, contrast, saturation, hue, num_samples)
    def get_transform(self)
    def get_batch_transform(self, N)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def _forward_in(self, inputs)
    def _forward_out(self, inputs)
    def _visualize(self, pre_random_input, randomized_input, num_samples_to_visualize)
    def __repr__(self)
class GaussianNoiseRandomizer(Randomizer)
    """Randomly sample gaussian noise at input, and then average across noises at output."""
    def __init__(self, input_shape, noise_mean, noise_std, limits, num_samples)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def _forward_in(self, inputs)
    def _forward_out(self, inputs)
    def _visualize(self, pre_random_input, randomized_input, num_samples_to_visualize)
    def __repr__(self)
```

### STEP3_train_policy/robomimic/models/obs_nets.py

```
"""Contains torch Modules that help deal with inputs consisting of multiple
modalities. This is extremely common when networks must deal with one or 
more observation dictionaries, where each input dictionary can have
observation keys of a certain modality and shape.

As an example, an observation could consist of a flat "robot0_eef_pos" observation key,
and a 3-channel RGB "agentview_image" observation key."""
def obs_encoder_factory(obs_shapes, feature_activation, encoder_kwargs)
class ObservationEncoder(Module)
    """Module that processes inputs by observation key and then concatenates the processed
observation keys together. Each key is processed with an encoder head network.
Call @register_obs_key to register observation keys with the encoder and then
finally call @make to create the encoder networks. """
    def __init__(self, feature_activation)
    def register_obs_key(self, name, shape, net_class, net_kwargs, net, randomizer, share_net_from)
    def make(self)
    def _create_layers(self)
    def forward(self, obs_dict)
    def output_shape(self, input_shape)
    def __repr__(self)
class ObservationDecoder(Module)
    """Module that can generate observation outputs by modality. Inputs are assumed
to be flat (usually outputs from some hidden layer). Each observation output
is generated with a linear layer from these flat inputs. Subclass this
module in order to implement more complex schemes for generating each
modal"""
    def __init__(self, decode_shapes, input_feat_dim)
    def _create_layers(self)
    def output_shape(self, input_shape)
    def forward(self, feats)
    def __repr__(self)
class ObservationGroupEncoder(Module)
    """This class allows networks to encode multiple observation dictionaries into a single
flat, concatenated vector representation. It does this by assigning each observation
dictionary (observation group) an @ObservationEncoder object.

The class takes a dictionary of dictionaries, @observation_group_sh"""
    def __init__(self, observation_group_shapes, feature_activation, encoder_kwargs)
    def forward(self)
    def output_shape(self)
    def __repr__(self)
class MIMO_MLP(Module)
    """Extension to MLP to accept multiple observation dictionaries as input and
to output dictionaries of tensors. Inputs are specified as a dictionary of 
observation dictionaries, with each key corresponding to an observation group.

This module utilizes @ObservationGroupEncoder to process the multiple """
    def __init__(self, input_obs_group_shapes, output_shapes, layer_dims, layer_func, activation, encoder_kwargs)
    def output_shape(self, input_shape)
    def forward(self)
    def _to_string(self)
    def __repr__(self)
class RNN_MIMO_MLP(Module)
    """A wrapper class for a multi-step RNN and a per-step MLP and a decoder.

Structure: [encoder -> rnn -> mlp -> decoder]

All temporal inputs are processed by a shared @ObservationGroupEncoder,
followed by an RNN, and then a per-step multi-output MLP. """
    def __init__(self, input_obs_group_shapes, output_shapes, mlp_layer_dims, rnn_hidden_dim, rnn_num_layers, rnn_type, rnn_kwargs, mlp_activation, mlp_layer_func, per_step, encoder_kwargs)
    def get_rnn_init_state(self, batch_size, device)
    def output_shape(self, input_shape)
    def forward(self, rnn_init_state, return_state)
    def forward_step(self, rnn_state)
    def _to_string(self)
    def __repr__(self)
class MIMO_Transformer(Module)
    """Extension to Transformer (based on GPT architecture) to accept multiple observation 
dictionaries as input and to output dictionaries of tensors. Inputs are specified as 
a dictionary of observation dictionaries, with each key corresponding to an observation group.
This module utilizes @ObservationG"""
    def __init__(self, input_obs_group_shapes, output_shapes, transformer_embed_dim, transformer_num_layers, transformer_num_heads, transformer_context_length, transformer_emb_dropout, transformer_attn_dropout, transformer_block_output_dropout, transformer_sinusoidal_embedding, transformer_activation, transformer_nn_parameter_for_timesteps, encoder_kwargs)
    def output_shape(self, input_shape)
    def embed_timesteps(self, embeddings)
    def input_embedding(self, inputs)
    def forward(self)
    def _to_string(self)
    def __repr__(self)
```

### STEP3_train_policy/robomimic/models/perceiverio.py

```
"""https://github.com/juho-lee/set_transformer
Paper: Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks"""
class SetAttention(Module)
    """"MAB" in the original paper"""
    def __init__(self, dim_Q, dim_K, dim_V, num_heads, layer_norm)
    def forward(self, Q, K, mask)
class SelfSetAttention(SetAttention)
    """"SAB" in the original paper"""
    def forward(self, X)
class InducedSetAttention(Module)
    """"ISAB" in the original paper"""
    def __init__(self, dim_in, dim_out, num_heads, num_queries, layer_norm)
    def forward(self, X)
class PoolingSetAttention(Module)
    """"PMA" in the original paper"""
    def __init__(self, dim, num_heads, num_queries, pool_type, layer_norm)
    def forward(self, X, mask)
class IdentityKeyValuePoolingAttention(Module)
    """The key/value are identity functions as the original features, and only
the query (external inducing point) is learned.
See CoCa paper: https://arxiv.org/abs/2205.01917"""
    def __init__(self, dim, num_heads, num_queries)
    def forward(self, V)
    def extra_repr(self)
```

### STEP3_train_policy/robomimic/models/policy_nets.py

```
"""Contains torch Modules for policy networks. These networks take an
observation dictionary as input (and possibly additional conditioning,
such as subgoal or goal dictionaries) and produce action predictions,
samples, or distributions as outputs. Note that actions
are assumed to lie in [-1, 1], and most networks will have a final
tanh activation to help ensure this range."""
class ActorNetwork(MIMO_MLP)
    """A basic policy network that predicts actions from observations.
Can optionally be goal conditioned on future observations."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def output_shape(self, input_shape)
    def forward(self, obs_dict, goal_dict)
    def _to_string(self)
class PerturbationActorNetwork(ActorNetwork)
    """An action perturbation network - primarily used in BCQ.
It takes states and actions and returns action perturbations."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, perturbation_scale, goal_shapes, encoder_kwargs)
    def forward(self, obs_dict, acts, goal_dict)
    def _to_string(self)
class GaussianActorNetwork(ActorNetwork)
    """Variant of actor network that learns a diagonal unimodal Gaussian distribution
over actions."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, fixed_std, std_activation, init_last_fc_weight, init_std, mean_limits, std_limits, low_noise_eval, use_tanh, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, goal_dict)
    def forward(self, obs_dict, goal_dict)
    def _to_string(self)
class GMMActorNetwork(ActorNetwork)
    """Variant of actor network that learns a multimodal Gaussian mixture distribution
over actions."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, num_modes, min_std, std_activation, low_noise_eval, use_tanh, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, goal_dict)
    def forward(self, obs_dict, goal_dict)
    def _to_string(self)
class RNNActorNetwork(RNN_MIMO_MLP)
    """An RNN policy network that predicts actions from observations."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, rnn_hidden_dim, rnn_num_layers, rnn_type, rnn_kwargs, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def output_shape(self, input_shape)
    def forward(self, obs_dict, goal_dict, rnn_init_state, return_state)
    def forward_step(self, obs_dict, goal_dict, rnn_state)
    def _to_string(self)
class RNNGMMActorNetwork(RNNActorNetwork)
    """An RNN GMM policy network that predicts sequences of action distributions from observation sequences."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, rnn_hidden_dim, rnn_num_layers, rnn_type, rnn_kwargs, num_modes, min_std, std_activation, low_noise_eval, use_tanh, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, goal_dict, rnn_init_state, return_state)
    def forward(self, obs_dict, goal_dict, rnn_init_state, return_state)
    def forward_train_step(self, obs_dict, goal_dict, rnn_state)
    def forward_step(self, obs_dict, goal_dict, rnn_state)
    def _to_string(self)
class TransformerActorNetwork(MIMO_Transformer)
    """An Transformer policy network that predicts actions from observation sequences (assumed to be frame stacked
from previous observations) and possible from previous actions as well (in an autoregressive manner)."""
    def __init__(self, obs_shapes, ac_dim, transformer_embed_dim, transformer_num_layers, transformer_num_heads, transformer_context_length, transformer_emb_dropout, transformer_attn_dropout, transformer_block_output_dropout, transformer_sinusoidal_embedding, transformer_activation, transformer_nn_parameter_for_timesteps, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def output_shape(self, input_shape)
    def forward(self, obs_dict, actions, goal_dict)
    def _to_string(self)
class TransformerGMMActorNetwork(TransformerActorNetwork)
    """A Transformer GMM policy network that predicts sequences of action distributions from observation 
sequences (assumed to be frame stacked from previous observations)."""
    def __init__(self, obs_shapes, ac_dim, transformer_embed_dim, transformer_num_layers, transformer_num_heads, transformer_context_length, transformer_emb_dropout, transformer_attn_dropout, transformer_block_output_dropout, transformer_sinusoidal_embedding, transformer_activation, transformer_nn_parameter_for_timesteps, num_modes, min_std, std_activation, low_noise_eval, use_tanh, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, actions, goal_dict, low_noise_eval)
    def forward(self, obs_dict, actions, goal_dict)
    def _to_string(self)
class VAEActor(Module)
    """A VAE that models a distribution of actions conditioned on observations.
The VAE prior and decoder are used at test-time as the policy."""
    def __init__(self, obs_shapes, ac_dim, encoder_layer_dims, decoder_layer_dims, latent_dim, device, decoder_is_conditioned, decoder_reconstruction_sum_across_elements, latent_clip, prior_learn, prior_is_conditioned, prior_layer_dims, prior_use_gmm, prior_gmm_num_modes, prior_gmm_learn_weights, prior_use_categorical, prior_categorical_dim, prior_categorical_gumbel_softmax_hard, goal_shapes, encoder_kwargs)
    def encode(self, actions, obs_dict, goal_dict)
    def decode(self, obs_dict, goal_dict, z, n)
    def sample_prior(self, obs_dict, goal_dict, n)
    def set_gumbel_temperature(self, temperature)
    def get_gumbel_temperature(self)
    def output_shape(self, input_shape)
    def forward_train(self, actions, obs_dict, goal_dict, freeze_encoder)
    def forward(self, obs_dict, goal_dict, z)
```

### STEP3_train_policy/robomimic/models/set_transformer/data_modelnet40.py

```
def rotate_z(theta, x)
def augment(x)
def standardize(x)
class ModelFetcher(object)
    def __init__(self, fname, batch_size, down_sample, do_standardize, do_augmentation)
    def train_data(self)
    def next_train_batch(self)
    def test_data(self)
    def next_test_batch(self)
```

### STEP3_train_policy/robomimic/models/set_transformer/main_pointcloud.py

```
class SetTransformer(Module)
    def __init__(self, dim_input, num_outputs, dim_output, num_inds, dim_hidden, num_heads, ln)
    def forward(self, X)
```

### STEP3_train_policy/robomimic/models/set_transformer/mixture_of_mvns.py

```
class MultivariateNormal(object)
    def __init__(self, dim)
    def sample(self, B, K, labels)
    def log_prob(self, X, params)
    def stats(self)
    def parse(self, raw)
class MixtureOfMVNs(object)
    def __init__(self, mvn)
    def sample(self, B, N, K, return_gt)
    def log_prob(self, X, pi, params, return_labels)
    def plot(self, X, labels, params, axes)
    def parse(self, raw)
```

### STEP3_train_policy/robomimic/models/set_transformer/models.py

```
class DeepSet(Module)
    def __init__(self, dim_input, num_outputs, dim_output, dim_hidden)
    def forward(self, X)
class SetTransformer(Module)
    def __init__(self, dim_input, num_outputs, dim_output, num_inds, dim_hidden, num_heads, ln)
    def forward(self, X)
```

### STEP3_train_policy/robomimic/models/set_transformer/modules.py

```
class MAB(Module)
    def __init__(self, dim_Q, dim_K, dim_V, num_heads, ln)
    def forward(self, Q, K)
class SAB(Module)
    def __init__(self, dim_in, dim_out, num_heads, ln)
    def forward(self, X)
class ISAB(Module)
    def __init__(self, dim_in, dim_out, num_heads, num_inds, ln)
    def forward(self, X)
class PMA(Module)
    def __init__(self, dim, num_heads, num_seeds, ln)
    def forward(self, X)
```

### STEP3_train_policy/robomimic/models/set_transformer/mvn_diag.py

```
class MultivariateNormalDiag(MultivariateNormal)
    def __init__(self, dim)
    def sample(self, B, K, labels)
    def log_prob(self, X, params)
    def stats(self, params)
    def parse(self, raw)
```

### STEP3_train_policy/robomimic/models/set_transformer/plots.py

```
def scatter(X, labels, ax, colors)
def draw_ellipse(pos, cov, ax)
def scatter_mog(X, labels, mu, cov, ax, colors)
```

### STEP3_train_policy/robomimic/models/set_transformer/run.py

```
def generate_benchmark()
def train()
def test(bench, verbose)
def plot()
```

### STEP3_train_policy/robomimic/models/transformers.py

```
"""Implementation of transformers, mostly based on Andrej's minGPT model.
See https://github.com/karpathy/minGPT/blob/master/mingpt/model.py
for more details."""
class GEGLU(Module)
    """References:
    Shazeer et al., "GLU Variants Improve Transformer," 2020.
    https://arxiv.org/abs/2002.05202
Implementation: https://github.com/pfnet-research/deep-table/blob/237c8be8a405349ce6ab78075234c60d9bfe60b7/deep_table/nn/layers/activation.py"""
    def geglu(self, x)
    def forward(self, x)
class PositionalEncoding(Module)
    """Taken from https://pytorch.org/tutorials/beginner/transformer_tutorial.html."""
    def __init__(self, embed_dim)
    def forward(self, x)
class CausalSelfAttention(Module)
    def __init__(self, embed_dim, num_heads, context_length, attn_dropout, output_dropout)
    def forward(self, x)
    def output_shape(self, input_shape)
class SelfAttentionBlock(Module)
    """A single Transformer Block, that can be chained together repeatedly.
It consists of a @CausalSelfAttention module and a small MLP, along with
layer normalization and residual connections on each input."""
    def __init__(self, embed_dim, num_heads, context_length, attn_dropout, output_dropout, activation)
    def forward(self, x)
    def output_shape(self, input_shape)
class GPT_Backbone(Module)
    """the GPT model, with a context size of block_size"""
    def __init__(self, embed_dim, context_length, attn_dropout, block_output_dropout, num_layers, num_heads, activation)
    def _create_networks(self)
    def _init_weights(self, module)
    def output_shape(self, input_shape)
    def forward(self, inputs)
```

### STEP3_train_policy/robomimic/models/vae_nets.py

```
"""Contains an implementation of Variational Autoencoder (VAE) and other
variants, including other priors, and RNN-VAEs."""
def vae_args_from_config(vae_config)
class Prior(Module)
    """Base class for VAE priors. It's basically the same as a @MIMO_MLP network (it
instantiates one) but it supports additional methods such as KL loss computation 
and sampling, and also may learn prior parameters as observation-independent 
torch Parameters instead of observation-dependent mappings."""
    def __init__(self, param_shapes, param_obs_dependent, obs_shapes, mlp_layer_dims, goal_shapes, encoder_kwargs)
    def _create_layers(self, net_kwargs)
    def sample(self, n, obs_dict, goal_dict)
    def kl_loss(self, posterior_params, z, obs_dict, goal_dict)
    def output_shape(self, input_shape)
    def forward(self, batch_size, obs_dict, goal_dict)
class GaussianPrior(Prior)
    """A class that holds functionality for learning both unimodal Gaussian priors and
multimodal Gaussian Mixture Model priors for use in VAEs."""
    def __init__(self, latent_dim, device, latent_clip, learnable, use_gmm, gmm_num_modes, gmm_learn_weights, obs_shapes, mlp_layer_dims, goal_shapes, encoder_kwargs)
    def _create_layers(self, net_kwargs)
    def sample(self, n, obs_dict, goal_dict)
    def kl_loss(self, posterior_params, z, obs_dict, goal_dict)
    def forward(self, batch_size, obs_dict, goal_dict)
    def __repr__(self)
class CategoricalPrior(Prior)
    """A class that holds functionality for learning categorical priors for use
in VAEs."""
    def __init__(self, latent_dim, categorical_dim, device, learnable, obs_shapes, mlp_layer_dims, goal_shapes, encoder_kwargs)
    def _create_layers(self, net_kwargs)
    def sample(self, n, obs_dict, goal_dict)
    def kl_loss(self, posterior_params, z, obs_dict, goal_dict)
    def forward(self, batch_size, obs_dict, goal_dict)
    def __repr__(self)
class VAE(Module)
    """A Variational Autoencoder (VAE), as described in https://arxiv.org/abs/1312.6114.

Models a distribution p(X) or a conditional distribution p(X | Y), where each
variable can consist of multiple modalities. The target variable X, whose
distribution is modeled, is specified through the @input_shapes a"""
    def __init__(self, input_shapes, output_shapes, encoder_layer_dims, decoder_layer_dims, latent_dim, device, condition_shapes, decoder_is_conditioned, decoder_reconstruction_sum_across_elements, latent_clip, output_squash, output_scales, output_ranges, prior_learn, prior_is_conditioned, prior_layer_dims, prior_use_gmm, prior_gmm_num_modes, prior_gmm_learn_weights, prior_use_categorical, prior_categorical_dim, prior_categorical_gumbel_softmax_hard, goal_shapes, encoder_kwargs)
    def _create_layers(self)
    def _create_encoder(self)
    def _create_decoder(self)
    def _create_prior(self)
    def encode(self, inputs, conditions, goals)
    def reparameterize(self, posterior_params)
    def decode(self, conditions, goals, z, n)
    def sample_prior(self, n, conditions, goals)
    def kl_loss(self, posterior_params, encoder_z, conditions, goals)
    def reconstruction_loss(self, reconstructions, targets)
    def forward(self, inputs, outputs, conditions, goals, freeze_encoder)
    def set_gumbel_temperature(self, temperature)
    def get_gumbel_temperature(self)
```

### STEP3_train_policy/robomimic/models/value_nets.py

```
"""Contains torch Modules for value networks. These networks take an 
observation dictionary as input (and possibly additional conditioning, 
such as subgoal or goal dictionaries) and produce value or 
action-value estimates or distributions."""
class ValueNetwork(MIMO_MLP)
    """A basic value network that predicts values from observations.
Can optionally be goal conditioned on future observations."""
    def __init__(self, obs_shapes, mlp_layer_dims, value_bounds, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def output_shape(self, input_shape)
    def forward(self, obs_dict, goal_dict)
    def _to_string(self)
class ActionValueNetwork(ValueNetwork)
    """A basic Q (action-value) network that predicts values from observations
and actions. Can optionally be goal conditioned on future observations."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, value_bounds, goal_shapes, encoder_kwargs)
    def forward(self, obs_dict, acts, goal_dict)
    def _to_string(self)
class DistributionalActionValueNetwork(ActionValueNetwork)
    """Distributional Q (action-value) network that outputs a categorical distribution over
a discrete grid of value atoms. See https://arxiv.org/pdf/1707.06887.pdf for 
more details."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, value_bounds, num_atoms, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, acts, goal_dict)
    def forward(self, obs_dict, acts, goal_dict)
    def _to_string(self)
```

### STEP3_train_policy/robomimic/scripts/config_gen/bc_xfmr_gen.py

```
def make_generator_helper(args)
```

### STEP3_train_policy/robomimic/scripts/config_gen/diffusion_gen.py

```
def make_generator_helper(args)
```

### STEP3_train_policy/robomimic/scripts/config_gen/helper.py

```
def scan_datasets(folder, postfix)
def get_generator(algo_name, config_file, args, algo_name_short, pt)
def set_env_settings(generator, args)
def set_mod_settings(generator, args)
def set_debug_mode(generator, args)
def get_argparser()
def make_generator(args, make_generator_helper)
```

### STEP3_train_policy/robomimic/scripts/conversion/convert_d4rl.py

```
"""Helper script to convert D4RL data into an hdf5 compatible with this repository.
Takes a folder path and a D4RL env name. This script downloads the corresponding
raw D4RL dataset into a "d4rl" subfolder, and then makes a converted dataset 
in the "d4rl/converted" subfolder.

This script has been tested on the follwing commits:

    https://github.com/rail-berkeley/d4rl/tree/9b68f31bab6a8546edfb28ff0bd9d5916c62fd1f
    https://github.com/rail-berkeley/d4rl/tree/26adf732efafdad864b3df2287e7b778ee4f7f63

Args:
    env (str): d4rl env name, which specifies the dataset to download and convert
    f"""
```

### STEP3_train_policy/robomimic/scripts/conversion/convert_r2d2.py

```
"""Add image information to existing r2d2 hdf5 file"""
def convert_dataset(path, args)
```

### STEP3_train_policy/robomimic/scripts/conversion/convert_robosuite.py

```
"""Helper script to convert a dataset collected using robosuite into an hdf5 compatible with
this repository. Takes a dataset path corresponding to the demo.hdf5 file containing the
demonstrations. It modifies the dataset in-place. By default, the script also creates a
90-10 train-validation split.

For more information on collecting datasets with robosuite, see the code link and documentation
link below.

Code: https://github.com/ARISE-Initiative/robosuite/blob/offline_study/robosuite/scripts/collect_human_demonstrations.py

Documentation: https://robosuite.ai/docs/algorithms/demonstrations.html"""
```

### STEP3_train_policy/robomimic/scripts/conversion/convert_roboturk_pilot.py

```
"""Helper script to convert the RoboTurk Pilot datasets (https://roboturk.stanford.edu/dataset_sim.html)
into a format compatible with this repository. It will also create some useful filter keys
in the file (e.g. training, validation, and fastest n trajectories). Prior work
(https://arxiv.org/abs/1911.05321) has found this useful (for example, training on the 
fastest 225 demonstrations for bins-Can).

Direct download link for dataset: http://cvgl.stanford.edu/projects/roboturk/RoboTurkPilot.zip

Args:
    folder (str): path to a folder containing a demo.hdf5 and a models directory containing
  """
def convert_rt_pilot_hdf5(ref_folder)
def split_fastest_from_hdf5(hdf5_path, n)
```

### STEP3_train_policy/robomimic/scripts/conversion/convert_to_robosuite_v141.py

```
def replace_elem(parent, old_elem, new_elem)
def convert_xml(old_xml_str, env_name, env)
```

### STEP3_train_policy/robomimic/scripts/conversion/extract_action_dict.py

```
def extract_action_dict(args)
```

### STEP3_train_policy/robomimic/scripts/conversion/robosuite_add_absolute_actions.py

```
class RobomimicAbsoluteActionConverter()
    def __init__(self, dataset_path, algo_name)
    def __len__(self)
    def convert_actions(self, states, actions)
    def convert_idx(self, idx)
    def convert_and_eval_idx(self, idx)
    def evaluate_rollout_error(env, states, actions, robot0_eef_pos, robot0_eef_quat, metric_skip_steps)
def worker(x)
def main(input, output, eval_dir, num_workers)
```

### STEP3_train_policy/robomimic/scripts/conversion/set_dataset_attr.py

```
"""Example:
python robomimic/scripts/set_dataset_attr.py --glob 'datasets/**/*_abs.hdf5' --env_args env_kwargs.controller_configs.control_delta=false absolute_actions=true """
def update_env_args_dict(env_args_dict, key, value)
def main()
```

### STEP3_train_policy/robomimic/scripts/convert_actions.py

```
"""Helper script to prepare datasets for diffusion policy training by (1) adding absolute actions and (2) 
writing the absolute actions to action dictionaries."""
def convert_actions_in_dataset(dataset_path, output_name, absolute_mg)
```

### STEP3_train_policy/robomimic/scripts/dataset_states_to_obs.py

```
"""Script to extract observations from low-dimensional simulation states in a robosuite dataset.

Args:
    dataset (str): path to input hdf5 dataset

    output_name (str): name of output hdf5 dataset

    n (int): if provided, stop after n trajectories are processed

    shaped (bool): if flag is set, use dense rewards

    camera_names (str or [str]): camera name(s) to use for image observations. 
        Leave out to not use image observations.

    camera_height (int): height of image observation.

    camera_width (int): width of image observation

    done_mode (int): how to write done sig"""
def extract_trajectory(env, initial_state, states, actions, done_mode)
def dataset_states_to_obs(args)
```

### STEP3_train_policy/robomimic/scripts/download_datasets.py

```
"""Script to download datasets packaged with the repository. By default, all
datasets will be stored at robomimic/datasets, unless the @download_dir
argument is supplied. We recommend using the default, as most examples that
use these datasets assume that they can be found there.

The @tasks, @dataset_types, and @hdf5_types arguments can all be supplied
to choose which datasets to download. 

Args:
    download_dir (str): Base download directory. Created if it doesn't exist. 
        Defaults to datasets folder in repository - only pass in if you would
        like to override the location.

    """
```

### STEP3_train_policy/robomimic/scripts/download_momart_datasets.py

```
"""Script to download datasets used in MoMaRT paper (https://arxiv.org/abs/2112.05251). By default, all
datasets will be stored at robomimic/datasets, unless the @download_dir
argument is supplied. We recommend using the default, as most examples that
use these datasets assume that they can be found there.

The @tasks and @dataset_types arguments can all be supplied
to choose which datasets to download. 

Args:
    download_dir (str): Base download directory. Created if it doesn't exist. 
        Defaults to datasets folder in repository - only pass in if you would
        like to override the lo"""
```

### STEP3_train_policy/robomimic/scripts/generate_config_templates.py

```
"""Helpful script to generate example config files for each algorithm. These should be re-generated
when new config options are added, or when default settings in the config classes are modified."""
def main()
```

### STEP3_train_policy/robomimic/scripts/generate_paper_configs.py

```
"""Helper script to generate jsons for reproducing paper experiments.

Args:
    config_dir (str): Directory where generated configs will be placed. 
        Defaults to 'paper' subfolder in exps folder of repository

    dataset_dir (str): Base dataset directory where released datasets can be
        found on disk. Defaults to datasets folder in repository.

    output_dir (str): Base output directory for all training runs that will be 
        written to generated configs.

Example usage:
    # Assume datasets alredy exist in robomimic/../datasets folder. Configs will be generated under robomim"""
def modify_config_for_default_low_dim_exp(config)
def modify_config_for_default_image_exp(config)
def modify_config_for_dataset(config, task_name, dataset_type, hdf5_type, base_dataset_dir, filter_key)
def modify_bc_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def modify_bc_rnn_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def modify_bcq_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def modify_cql_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def modify_hbc_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def modify_iris_config_for_dataset(config, task_name, dataset_type, hdf5_type)
def generate_experiment_config(base_exp_name, base_config_dir, base_dataset_dir, base_output_dir, algo_name, algo_config_modifier, task_name, dataset_type, hdf5_type, filter_key, additional_name, additional_config_modifier)
def generate_core_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
def generate_subopt_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
def generate_dataset_size_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
def generate_obs_ablation_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
def generate_hyper_ablation_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
def generate_d4rl_configs(base_config_dir, base_dataset_dir, base_output_dir, algo_to_config_modifier)
```

### STEP3_train_policy/robomimic/scripts/get_dataset_info.py

```
"""Helper script to report dataset information. By default, will print trajectory length statistics,
the maximum and minimum action element in the dataset, filter keys present, environment
metadata, and the structure of the first demonstration. If --verbose is passed, it will
report the exact demo keys under each filter key, and the structure of all demonstrations
(not just the first one).

Args:
    dataset (str): path to hdf5 dataset

    filter_key (str): if provided, report statistics on the subset of trajectories
        in the file that correspond to this filter key

    verbose (bool): if """
```

### STEP3_train_policy/robomimic/scripts/give_slack_notification.py

```
"""Script to send a slack message for notifications on completed training runs.
Super extra, but gotta love it."""
def give_slack_notif(msg)
```

### STEP3_train_policy/robomimic/scripts/hyperparam_helper.py

```
"""A useful script for generating json files and shell scripts for conducting parameter scans.
The script takes a path to a base json file as an argument and a shell file name.
It generates a set of new json files in the same folder as the base json file, and 
a shell file script that contains commands to run for each experiment.

Instructions:

(1) Start with a base json that specifies a complete set of parameters for a single 
    run. This only needs to include parameters you want to sweep over, and parameters
    that are different from the defaults. You can set this file path by either
    p"""
def make_generator(config_file, script_file)
def main(args)
```

### STEP3_train_policy/robomimic/scripts/hyperparam_helper_diffusion.py

```
"""Version of hyperparam helper to easily spin up runs with different base configs and diffusion policy."""
def make_generators(base_configs)
def make_gen(base_config, settings)
def main(args)
```

### STEP3_train_policy/robomimic/scripts/playback_dataset.py

```
"""A script to visualize dataset trajectories by loading the simulation states
one by one or loading the first state and playing actions back open-loop.
The script can generate videos as well, by rendering simulation frames
during playback. The videos can also be generated using the image observations
in the dataset (this is useful for real-robot datasets) by using the
--use-obs argument.

Args:
    dataset (str): path to hdf5 dataset

    filter_key (str): if provided, use the subset of trajectories
        in the file that correspond to this filter key

    n (int): if provided, stop after n tr"""
def add_red_border(frame)
def depth_to_rgb(depth_map, depth_min, depth_max)
def playback_trajectory_with_env(env, initial_state, states, actions, render, video_writer, video_skip, camera_names, first, interventions, real)
def playback_trajectory_with_obs(traj_grp, video_writer, video_skip, image_names, depth_names, first, intervention)
def playback_dataset(args, env)
```

### STEP3_train_policy/robomimic/scripts/postprocess_dataset_intervention_segments.py

```
"""Script to postprocess a dataset by splitting each trajectory up into new trajectories 
that only consists of continuous intervention segments."""
def write_intervention_segments_as_trajectories(src_ep_grp, dst_grp, start_ep_write_ind, same)
def postprocess_dataset_intervention_segments(args)
```

### STEP3_train_policy/robomimic/scripts/remove_idle_segments.py

```
"""Script to remove idle segments from a real robot hdf5."""
def get_idle_segments_in_trajectory(ep_grp, obs_pos_key, min_segment_length, threshold, verbose)
def write_non_idle_segments_as_interventions(hdf5_path, n, min_segment_length, threshold)
def combine_intervention_segments(hdf5_path, output_name, n)
def remove_idle_segments(args)
```

### STEP3_train_policy/robomimic/scripts/run_trained_agent.py

```
"""The main script for evaluating a policy in an environment.

Args:
    agent (str): path to saved checkpoint pth file

    horizon (int): if provided, override maximum horizon of rollout from the one 
        in the checkpoint

    env (str): if provided, override name of env from the one in the checkpoint,
        and use it for rollouts

    render (bool): if flag is provided, use on-screen rendering during rollouts

    video_path (str): if provided, render trajectories to this video file path

    video_skip (int): render frames to a video every @video_skip steps

    camera_names (str or ["""
def rollout(policy, env, horizon, render, video_writer, video_skip, return_obs, camera_names, real, rate_measure)
def run_trained_agent(args)
```

### STEP3_train_policy/robomimic/scripts/run_trained_agent_real_withmodel.py

```
class RedisReceiver()
    def __init__(self, host, port, db)
    def start_stream(self)
```

### STEP3_train_policy/robomimic/scripts/run_trained_agent_utils.py

```
def resize_image(image_path)
def translate_wrist_to_origin(joint_positions)
def apply_pose_matrix(joint_positions, pose_matrix)
def inverse_transformation(matrix)
def calculate_rotation_deltas(quaternions, frame_step)
def reconstruct_quaternions(original_quaternions, delta_euler_rotations)
def calculate_translation_deltas(translations, frame_step)
def _back_project_point(point, intrinsics)
```

### STEP3_train_policy/robomimic/scripts/run_trained_agent_vis.py

```
class VisOnlyEnv()
    def __init__(self, hdf5_file)
    def load_hdf5_data(self)
    def _load_demo(self, demo_name)
    def get_state(self)
    def reset(self)
    def _visualize(self)
    def _draw_ee_hand(self, image, robot0_eef, corrected_pose)
    def _draw_action(self, image, robot0_eef, corrected_pose, action)
    def start_visualization(self)
    def stop_visualization(self)
def run_trained_agent(args)
```

### STEP3_train_policy/robomimic/scripts/run_trained_agent_vis_withmodel.py

```
class VisOnlyEnv()
    def __init__(self, hdf5_file, obs_horizon)
    def load_hdf5_data(self)
    def _load_demo(self, demo_name)
    def get_state(self)
    def vis_model_action(self, action)
    def vis_gt_action(self)
    def save_current_frame(self)
    def reset(self)
    def _visualize(self)
    def _draw_ee_hand(self, image, robot0_eef, corrected_pose)
    def _draw_action(self, image, robot0_eef, corrected_pose, action, gt)
    def start_visualization(self)
    def stop_visualization(self)
def run_trained_agent(args)
```

### STEP3_train_policy/robomimic/scripts/setup_macros.py

```
"""This script sets up a private macros file.

The private macros file (macros_private.py) is not tracked by git,
allowing user-specific settings that are not tracked by git.

This script checks if macros_private.py exists.
If applicable, it creates the private macros at robomimic/macros_private.py"""
```

### STEP3_train_policy/robomimic/scripts/split_train_val.py

```
"""Script for splitting a dataset hdf5 file into training and validation trajectories.

Args:
    dataset (str): path to hdf5 dataset

    filter_key (str): if provided, split the subset of trajectories
        in the file that correspond to this filter key into a training
        and validation set of trajectories, instead of splitting the
        full set of trajectories

    ratio (float): validation ratio, in (0, 1). Defaults to 0.1, which is 10%.

Example usage:
    python split_train_val.py --dataset /path/to/demo.hdf5 --ratio 0.1"""
def split_train_val_from_hdf5(hdf5_path, val_ratio, filter_key)
```

### STEP3_train_policy/robomimic/scripts/train.py

```
"""The main entry point for training policies.

Args:
    config (str): path to a config json that will be used to override the default settings.
        If omitted, default settings are used. This is the preferred way to run experiments.

    algo (str): name of the algorithm to run. Only needs to be provided if @config is not
        provided.

    name (str): if provided, override the experiment name defined in the config

    dataset (str): if provided, override the dataset path defined in the config

    debug (bool): set this flag to run a quick training run for debugging purposes    """
def load_dict_from_checkpoint(ckpt_path)
def maybe_dict_from_checkpoint(ckpt_path, ckpt_dict)
def train(config, device, auto_remove_exp, resume)
def main(args)
```

### STEP3_train_policy/robomimic/scripts/valid.py

```
"""The main entry point for training policies.

Args:
    config (str): path to a config json that will be used to override the default settings.
        If omitted, default settings are used. This is the preferred way to run experiments.

    algo (str): name of the algorithm to run. Only needs to be provided if @config is not
        provided.

    name (str): if provided, override the experiment name defined in the config

    dataset (str): if provided, override the dataset path defined in the config

    debug (bool): set this flag to run a quick training run for debugging purposes"""
def load_dict_from_checkpoint(ckpt_path)
def maybe_dict_from_checkpoint(ckpt_path, ckpt_dict)
def valid(config, device, auto_remove_exp, resume)
def main(args)
```

### STEP3_train_policy/robomimic/utils/action_utils.py

```
def action_dict_to_vector(action_dict, action_keys)
def vector_to_action_dict(action, action_shapes, action_keys)
```

### STEP3_train_policy/robomimic/utils/dataset.py

```
"""This file contains Dataset classes that are used by torch dataloaders
to fetch batches from hdf5 files."""
class SequenceDataset(Dataset)
    def __init__(self, hdf5_path, obs_keys, action_keys, dataset_keys, action_config, frame_stack, seq_length, pad_frame_stack, pad_seq_length, get_pad_mask, goal_mode, hdf5_cache_mode, hdf5_use_swmr, hdf5_normalize_obs, filter_by_attribute, load_next_obs)
    def load_demo_info(self, filter_by_attribute, demos)
    def hdf5_file(self)
    def close_and_delete_hdf5_handle(self)
    def hdf5_file_opened(self)
    def __del__(self)
    def __repr__(self)
    def __len__(self)
    def load_dataset_in_memory(self, demo_list, hdf5_file, obs_keys, dataset_keys, load_next_obs)
    def normalize_obs(self)
    def get_obs_normalization_stats(self)
    def get_action_traj(self, ep)
    def get_action_stats(self)
    def set_action_normalization_stats(self, action_normalization_stats)
    def get_action_normalization_stats(self)
    def get_dataset_for_ep(self, ep, key)
    def __getitem__(self, index)
    def get_item(self, index)
    def get_sequence_from_demo(self, demo_id, index_in_demo, keys, num_frames_to_stack, seq_length)
    def get_obs_sequence_from_demo(self, demo_id, index_in_demo, keys, num_frames_to_stack, seq_length, prefix)
    def get_dataset_sequence_from_demo(self, demo_id, index_in_demo, keys, num_frames_to_stack, seq_length)
    def get_trajectory_at_index(self, index)
    def get_dataset_sampler(self)
class R2D2Dataset(SequenceDataset)
    def get_action_traj(self, ep)
    def load_demo_info(self, filter_by_attribute, demos, n_demos)
    def load_dataset_in_memory(self, demo_list, hdf5_file, obs_keys, dataset_keys, load_next_obs)
    def get_dataset_for_ep(self, ep, key, try_to_use_cache)
    def get_sequence_from_demo(self, demo_id, index_in_demo, keys, num_frames_to_stack, seq_length)
    def get_item(self, index)
class MetaDataset(Dataset)
    def __init__(self, datasets, ds_weights, normalize_weights_by_ds_size, ds_labels)
    def __len__(self)
    def __getitem__(self, idx)
    def get_ds_label(self, idx)
    def get_ds_id(self, idx)
    def __repr__(self)
    def get_dataset_sampler(self)
    def get_action_stats(self)
    def set_action_normalization_stats(self, action_normalization_stats)
    def get_action_normalization_stats(self)
def _compute_traj_stats(traj_obs_dict)
def _aggregate_traj_stats(traj_stats_a, traj_stats_b)
def action_stats_to_normalization_stats(action_stats, action_config)
```

### STEP3_train_policy/robomimic/utils/env_utils.py

```
"""This file contains several utility functions for working with environment
wrappers provided by the repository, and with environment metadata saved
in dataset files."""
def get_env_class(env_meta, env_type, env)
def get_env_type(env_meta, env_type, env)
def check_env_type(type_to_check, env_meta, env_type, env)
def check_env_version(env, env_meta)
def is_robosuite_env(env_meta, env_type, env)
def is_simpler_env(env_meta, env_type, env)
def is_simpler_ov_env(env_meta, env_type, env)
def is_factory_env(env_meta, env_type, env)
def is_furniture_sim_env(env_meta, env_type, env)
def is_real_robot_env(env_meta, env_type, env)
def is_real_robot_gprs_env(env_meta, env_type, env)
def create_env(env_type, env_name, env_class, render, render_offscreen, use_image_obs, use_depth_obs)
def create_env_from_metadata(env_meta, env_name, env_class, render, render_offscreen, use_image_obs, use_depth_obs)
def create_env_for_data_processing(env_meta, camera_names, camera_height, camera_width, reward_shaping, env_class, render, render_offscreen, use_image_obs, use_depth_obs)
def set_env_specific_obs_processing(env_meta, env_type, env)
def wrap_env_from_config(env, config)
```

### STEP3_train_policy/robomimic/utils/file_utils.py

```
"""A collection of utility functions for working with files, such as reading metadata from
demonstration datasets, loading model checkpoints, or downloading dataset files."""
def create_hdf5_filter_key(hdf5_path, demo_keys, key_name)
def get_demos_for_filter_key(hdf5_path, filter_key)
def get_env_metadata_from_dataset(dataset_path, ds_format, set_env_specific_obs_processors)
def get_shape_metadata_from_dataset(dataset_path, action_keys, all_obs_keys, ds_format, verbose)
def get_intervention_segments(interventions)
def load_dict_from_checkpoint(ckpt_path)
def maybe_dict_from_checkpoint(ckpt_path, ckpt_dict)
def algo_name_from_checkpoint(ckpt_path, ckpt_dict)
def update_config(cfg)
def config_from_checkpoint(algo_name, ckpt_path, ckpt_dict, verbose)
def policy_from_checkpoint(device, ckpt_path, ckpt_dict, verbose)
def env_from_checkpoint(ckpt_path, ckpt_dict, env_name, render, render_offscreen, verbose)
class DownloadProgressBar(tqdm)
    def update_to(self, b, bsize, tsize)
def url_is_alive(url)
def download_url(url, download_dir, check_overwrite)
def find_and_replace_path_prefix(org_path, replace_prefixes, new_prefix, assert_replace)
```

### STEP3_train_policy/robomimic/utils/hyperparam_utils.py

```
"""A collection of utility functions and classes for generating config jsons for hyperparameter sweeps."""
class ConfigGenerator(object)
    """Useful class to keep track of hyperparameters to sweep, and to generate
the json configs for each experiment run."""
    def __init__(self, base_config_file, wandb_proj_name, script_file, generated_config_dir)
    def add_param(self, key, name, group, values, value_names, hidename)
    def generate(self)
    def _name_for_experiment(self, base_name, parameter_values, parameter_value_names)
    def _get_parameter_ranges(self)
    def _generate_jsons(self)
    def _script_from_jsons(self, json_paths)
def load_json(json_file, verbose)
def save_json(config, json_file)
def get_value_for_key(dic, k)
def set_value_for_key(dic, k, v)
```

### STEP3_train_policy/robomimic/utils/log_utils.py

```
"""This file contains utility classes and functions for logging to stdout, stderr,
and to tensorboard."""
class PrintLogger(object)
    """This class redirects print statements to both console and a file."""
    def __init__(self, log_file)
    def fileno(self)
    def write(self, message)
    def flush(self)
class DataLogger(object)
    """Logging class to log metrics to tensorboard and/or retrieve running statistics about logged data."""
    def __init__(self, log_dir, config, log_tb, log_wandb)
    def record(self, k, v, epoch, data_type, log_stats)
    def get_stats(self, k)
    def close(self)
class custom_tqdm(tqdm)
    """Small extension to tqdm to make a few changes from default behavior.
By default tqdm writes to stderr. Instead, we change it to write
to stdout."""
    def __init__(self)
def silence_stdout()
def log_warning(message, color, print_now)
def flush_warnings()
```

### STEP3_train_policy/robomimic/utils/loss_utils.py

```
"""This file contains a collection of useful loss functions for use with torch tensors."""
def cosine_loss(preds, labels)
def KLD_0_1_loss(mu, logvar)
def KLD_gaussian_loss(mu_1, logvar_1, mu_2, logvar_2)
def log_normal(x, m, v)
def log_normal_mixture(x, m, v, w, log_w)
def log_mean_exp(x, dim)
def log_sum_exp(x, dim)
def project_values_onto_atoms(values, probabilities, atoms)
```

### STEP3_train_policy/robomimic/utils/obs_utils.py

```
"""A collection of utilities for working with observation dictionaries and
different kinds of modalities such as images."""
def register_obs_key(target_class)
def register_encoder_core(target_class)
def register_randomizer(target_class)
class ObservationKeyToModalityDict(dict)
    """Custom dictionary class with the sole additional purpose of automatically registering new "keys" at runtime
without breaking. This is mainly for backwards compatibility, where certain keys such as "latent", "actions", etc.
are used automatically by certain models (e.g.: VAEs) but were never specifie"""
    def __getitem__(self, item)
def obs_encoder_kwargs_from_config(obs_encoder_config)
def initialize_obs_modality_mapping_from_dict(modality_mapping)
def initialize_obs_utils_with_obs_specs(obs_modality_specs)
def initialize_default_obs_encoder(obs_encoder_config)
def initialize_obs_utils_with_config(config)
def key_is_obs_modality(key, obs_modality)
def center_crop(im, t_h, t_w)
def batch_image_hwc_to_chw(im)
def batch_image_chw_to_hwc(im)
def process_obs(obs, obs_modality, obs_key)
def process_obs_dict(obs_dict)
def process_frame(frame, channel_dim, scale)
def unprocess_obs(obs, obs_modality, obs_key)
def unprocess_obs_dict(obs_dict)
def unprocess_frame(frame, channel_dim, scale)
def get_processed_shape(obs_modality, input_shape)
def normalize_dict(dict, normalization_stats)
def unnormalize_dict(dict, normalization_stats)
def has_modality(modality, obs_keys)
def repeat_and_stack_observation(obs_dict, n)
def crop_image_from_indices(images, crop_indices, crop_height, crop_width)
def sample_random_image_crops(images, crop_height, crop_width, num_crops, pos_enc)
class Modality()
    """Observation Modality class to encapsulate necessary functions needed to
process observations of this modality"""
    def __init_subclass__(cls)
    def set_keys(cls, keys)
    def add_keys(cls, keys)
    def set_obs_processor(cls, processor)
    def set_obs_unprocessor(cls, unprocessor)
    def _default_obs_processor(cls, obs)
    def _default_obs_unprocessor(cls, obs)
    def process_obs(cls, obs)
    def unprocess_obs(cls, obs)
    def process_obs_from_dict(cls, obs_dict, inplace)
class ImageModality(Modality)
    """Modality for RGB image observations"""
    def _default_obs_processor(cls, obs)
    def _default_obs_unprocessor(cls, obs)
class DepthModality(Modality)
    """Modality for depth observations"""
    def _default_obs_processor(cls, obs)
    def _default_obs_unprocessor(cls, obs)
class ScanModality(Modality)
    """Modality for scan observations"""
    def _default_obs_processor(cls, obs)
    def _default_obs_unprocessor(cls, obs)
class LowDimModality(Modality)
    """Modality for low dimensional observations"""
    def _default_obs_processor(cls, obs)
    def _default_obs_unprocessor(cls, obs)

```python
def repeat_and_stack_observation(obs_dict, n):
    """
    Given an observation dictionary and a desired repeat value @n,
    this function will return a new observation dictionary where
    each modality is repeated @n times and the copies are
    stacked in the first dimension. 

    For example, if a batch of 3 observations comes in, and n is 2,
    the output will look like [ob1; ob1; ob2; ob2; ob3; ob3] in
    each modality.

    Args:
        obs_dict (dict): dictionary mapping observation key to np.array or
            torch.Tensor. Leading batch dimensions are optional.

        n (int): number to repeat by

    Returns:
        repeat_obs_dict (dict): repeated obs dict
    """
    return TU.repeat_by_expand_at(obs_dict, repeats=n, dim=0)
```
```

### STEP3_train_policy/robomimic/utils/python_utils.py

```
"""Set of general purpose utility functions for easier interfacing with Python API"""
def get_class_init_kwargs(cls)
def extract_subset_dict(dic, keys, copy)
def extract_class_init_kwargs_from_dict(cls, dic, copy, verbose)
```

### STEP3_train_policy/robomimic/utils/script_utils.py

```
"""Collection of miscellaneous utility tools"""
def deep_update(d, u)
```

### STEP3_train_policy/robomimic/utils/tensor_utils.py

```
"""A collection of utilities for working with nested tensor structures consisting
of numpy arrays and torch tensors."""
def recursive_dict_list_tuple_apply(x, type_func_dict, error_on_missing_type)
def map_tensor(x, func, error_on_missing_type)
def map_ndarray(x, func, error_on_missing_type)
def map_tensor_ndarray(x, tensor_func, ndarray_func, error_on_missing_type)
def clone(x)
def detach(x)
def to_batch(x)
def to_sequence(x)
def index_at_time(x, ind)
def unsqueeze(x, dim)
def contiguous(x)
def to_device(x, device)
def to_tensor(x)
def to_numpy(x)
def to_list(x)
def to_float(x)
def to_uint8(x)
def to_uint16(x)
def to_torch(x, device)
def to_one_hot_single(tensor, num_class)
def to_one_hot(tensor, num_class)
def flatten_single(x, begin_axis)
def flatten(x, begin_axis)
def reshape_dimensions_single(x, begin_axis, end_axis, target_dims)
def reshape_dimensions(x, begin_axis, end_axis, target_dims)
def join_dimensions(x, begin_axis, end_axis)
def expand_at_single(x, size, dim)
def expand_at(x, size, dim)
def unsqueeze_expand_at(x, size, dim)
def repeat_by_expand_at(x, repeats, dim)
def named_reduce_single(x, reduction, dim)
def named_reduce(x, reduction, dim)
def gather_along_dim_with_dim_single(x, target_dim, source_dim, indices)
def gather_along_dim_with_dim(x, target_dim, source_dim, indices)
def gather_sequence_single(seq, indices)
def gather_sequence(seq, indices)
def pad_sequence_single(seq, padding, batched, pad_same, pad_values)
def pad_sequence(seq, padding, batched, pad_same, pad_values)
def assert_size_at_dim_single(x, size, dim, msg)
def assert_size_at_dim(x, size, dim, msg)
def get_shape(x)
def list_of_flat_dict_to_dict_of_list(list_of_dict)
def flatten_nested_dict_list(d, parent_key, sep, item_key)
def time_distributed(inputs, op, activation, inputs_as_kwargs, inputs_as_args)
```

### STEP3_train_policy/robomimic/utils/test_utils.py

```
"""Utilities for testing algorithm implementations - used mainly by scripts in tests directory."""
def maybe_remove_dir(dir_to_remove)
def maybe_remove_file(file_to_remove)
def example_dataset_path()
def example_momart_dataset_path()
def temp_model_dir_path()
def temp_dataset_path()
def temp_video_path()
def get_base_config(algo_name)
def config_from_modifier(base_config, config_modifier)
def checkpoint_path_from_test_run()
def test_eval_agent_from_checkpoint(ckpt_path, device)
def test_run(base_config, config_modifier)
```

### STEP3_train_policy/robomimic/utils/torch_utils.py

```
"""This file contains some PyTorch utilities."""
def soft_update(source, target, tau)
def hard_update(source, target)
def get_torch_device(try_to_use_cuda)
def reparameterize(mu, logvar)
def optimizer_from_optim_params(net_optim_params, net)
def lr_scheduler_from_optim_params(net_optim_params, net, optimizer)
def backprop_for_loss(net, optim, loss, max_grad_norm, retain_graph)
def rot_6d_to_axis_angle(rot_6d)
def axis_angle_to_rot_6d(axis_angle)
class dummy_context_mgr()
    """A dummy context manager - useful for having conditional scopes (such
as @maybe_no_grad). Nothing happens in this scope."""
    def __enter__(self)
    def __exit__(self, exc_type, exc_value, traceback)
def maybe_no_grad(no_grad)
def _sqrt_positive_part(x)
def quaternion_to_matrix(quaternions)
def matrix_to_quaternion(matrix)
def axis_angle_to_matrix(axis_angle)
def matrix_to_axis_angle(matrix)
def axis_angle_to_quaternion(axis_angle)
def quaternion_to_axis_angle(quaternions)
def rotation_6d_to_matrix(d6)
def matrix_to_rotation_6d(matrix)
```

### STEP3_train_policy/robomimic/utils/train_utils.py

```
"""This file contains several utility functions used to define the main training loop. It 
mainly consists of functions to assist with logging, rollouts, and the @run_epoch function,
which is the core training logic for models in this repository."""
def get_exp_dir(config, auto_remove_exp_dir)
def set_absolute_sync_path(output_dir, exp_name, time_str)
def load_data_for_training(config, obs_keys)
def dataset_factory(config, obs_keys, filter_by_attribute, dataset_path)
def get_dataset(ds_class, ds_kwargs, ds_weights, ds_labels, normalize_weights_by_ds_size, meta_ds_class, meta_ds_kwargs)
def run_rollout(policy, env, horizon, use_goals, render, video_writer, video_skip, terminate_on_success)
def rollout_with_stats(policy, envs, horizon, use_goals, num_episodes, render, video_dir, video_path, epoch, video_skip, terminate_on_success, verbose)
def should_save_from_rollout_logs(all_rollout_logs, best_return, best_success_rate, epoch_ckpt_name, save_on_best_rollout_return, save_on_best_rollout_success_rate)
def save_model(model, config, env_meta, shape_meta, ckpt_path, obs_normalization_stats, action_normalization_stats)
def run_epoch(model, data_loader, epoch, validate, num_steps, obs_normalization_stats)
def is_every_n_steps(interval, current_step, skip_zero)
def get_model_from_output_folder(models_path, videos_path, epoch, best, last)
```

### STEP3_train_policy/robomimic/utils/vis_utils.py

```
"""This file contains utility functions for visualizing image observations in the training pipeline.
These functions can be a useful debugging tool."""
def image_tensor_to_numpy(image)
def image_to_disk(image, fname)
def image_tensor_to_disk(image, fname)
def visualize_image_randomizer(original_image, randomized_image, randomizer_name)
```