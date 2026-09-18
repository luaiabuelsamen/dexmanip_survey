# omnih2o_2024

source: https://github.com/LeCAR-Lab/human2humanoid


commit: 750f1fa052641f0fde43669d50cb4e407dabe6c8


## README

<h1 align="center">Human to Humanoid</h1>

Official Implementation for [H2O](https://human2humanoid.com/) and [OmniH2O](https://omni.human2humanoid.com/):
- [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://human2humanoid.com/), IROS 2024.
- [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](https://omni.human2humanoid.com/), CoRL 2024.


<div style="display: flex; align-items: center;">
    <img src="./images/H2O.gif" alt="H2O" style="margin-right: 10px;">
    <img src="./images/OmniH2O.gif" alt="OmniH2O">
</div>




This codebase is under [CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/deed.en), with inherited license in [Legged Gym](training/legged_gym) and [RSL RL](training/rsl_rl) from *ETH Zurich, Nikita Rudin* and *NVIDIA CORPORATION & AFFILIATES*. You **may not use the material for commercial purposes**, e.g., to make demos to advertise your commercial products.

Please read through the whole README.md before cloning the repo.

# Installation

**Note**: Before running our code, it's highly recommended to first play with [RSL's Legged Gym version](https://github.com/leggedrobotics/legged_gym) to get a basic understanding of the Isaac-LeggedGym-RslRL framework.
   <!-- <br/><br/> -->

1. Create environment and install torch

   ```text
   conda create -n omnih2o python=3.8 
   conda activate omnih2o
   pip3 install torch torchvision torchaudio 
   ```

   

2. Install Isaac Gym preview 4 release https://developer.nvidia.com/isaac-gym

   unzip files to a folder, then install with pip:

   `cd isaacgym/python && pip install -e .`

   check it is correctly installed by playing: 

   ```cmd
   cd examples && python 1080_balls_of_solitude.py
   ```

   

3. Clone this codebase and install our `rsl_rl` in the training folder

   ```cmd
   pip install -e rsl_rl
   ```



4. Install our `legged_gym`

   ```cmd
   pip install -e legged_gym
   ```

   Ensure you have installed the following packages:
    + pip install numpy==1.20 (must < 1.24)
    + pip install tensorboard
    + pip install setuptools==59.5.0

5. Install our `phc`

   ```cmd
   pip install -e phc
   ```

6. Install additional packages `requirements.txt`

   ```cmd
   pip install -r requirements.txt
   ```


# Training and Playing

1. Try training and playing **privileged teacher policy**.

   can use "--headless" to disable gui, press "v" to pause/resume gui play.

    ```text
   # OmniH2O Training and Playing Teacher Policy 
   python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_TEACHER env.num_observations=913 env.num_privileged_obs=990 motion.teleop_obs_version=v-teleop-extend-max-full motion=motion_full motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5

   # OmniH2O Play Teacher Policy
    python  legged_gym/scripts/play_hydra.py --config-name=config_teleop task=h1:teleop env.num_observations=913 env.num_privileged_obs=990 motion.future_tracks=True motion.teleop_obs_version=v-teleop-extend-max-full motion=motion_full  motion.extend_head=True asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0  sim_device=cuda:0 load_run=OmniH2O_TEACHER checkpoint=XXXX num_envs=1 headless=False
   ```
2. Try training and playing **sim2real deploy policy**.
   ```text
   # OmniH2O Distill Student Policy
   python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT env.num_observations=1665 env.num_privileged_obs=1742 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=25 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True

   # OmniH2O Play Student Policy
   python legged_gym/scripts/play_hydra.py --config-name=config_teleop task=h1:teleop env.num_observations=1665 env.num_privileged_obs=1742 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=1 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0 sim_device=cuda:0 load_run=OmniH2O_STUDENT checkpoint=XXXX env.add_short_history=True env.short_history_length=25 headless=False 

   ```

3. Different Configurations on **Hisotry Steps**

    **0-step MLP**
    ```text
    # OmniH2O Distill 0-step MLP Student Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT_0stepMLP env.num_observations=90 env.num_privileged_obs=167 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=False noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True

    # OmniH2O Play 0-step MLP Student Policy 
    python legged_gym/scripts/play_hydra.py --config-name=config_teleop task=h1:teleop env.num_observations=90 env.num_privileged_obs=167 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=1 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0 sim_device=cuda:0 load_run=OmniH2O_STUDENT checkpoint=XXXX env.add_short_history=False headless=False 
    ```

    **5-step MLP**
    ```text
    # OmniH2O Distill 5-step MLP Student Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT_50stepMLP env.num_observations=405 env.num_privileged_obs=482 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=5 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True

    # OmniH2O Play 5-step MLP Student Policy 
    python legged_gym/scripts/play_hydra.py --config-name=config_teleop task=h1:teleop env.env.env.num_observations=405 env.num_privileged_obs=482 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=1 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0 sim_device=cuda:0 load_run=OmniH2O_STUDENT checkpoint=XXXX env.add_short_history=True env.short_history_length=5 headless=False 
    ```

    **50-step MLP**
    ```text
    # OmniH2O Distill 50-step MLP Student Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT_50stepMLP env.num_observations=3240 env.num_privileged_obs=3317 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=50 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True

    # OmniH2O Play 50-step MLP Student Policy 
    python legged_gym/scripts/play_hydra.py --config-name=config_teleop task=h1:teleop env.env.num_observations=3240 env.num_privileged_obs=3317 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=1 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0 sim_device=cuda:0 load_run=OmniH2O_STUDENT checkpoint=XXXX env.add_short_history=True env.short_history_length=50 headless=False 
    ```
   

    

4. Different Configurations on **Hisotry Architectures**

    **LSTM**
    ```text
    # OmniH2O Distill LSTM Student Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=LSTM_STUDENT env.num_observations=90 env.num_privileged_obs=167 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=False rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=False env.short_history_length=0 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=55500 train.dagger.dagger_only=True train.runner.policy_class_name=ActorCriticRecurrent train.policy.rnn_type=lstm
    ```

    **GRU**
    ```text
    # OmniH2O Distill GRU Student Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=LSTM_STUDENT env.num_observations=90 env.num_privileged_obs=167 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=False rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=False env.short_history_length=0 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=55500 train.dagger.dagger_only=True train.runner.policy_class_name=ActorCriticRecurrent train.policy.rnn_type=gru
    ```




5. Different Configurations on **Observation Type (tracking points)**

    ```text
    # OmniH2O Distill 8-point Tracking Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT_8point env.num_observations=1719 env.num_privileged_obs=1796 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[left_ankle_link,right_ankle_link,left_shoulder_pitch_link,right_shoulder_pitch_link,left_elbow_link,right_elbow_link] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=25 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True

    # OmniH2O Distill 23-point Tracking Policy 
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT_23point env.num_observations=1845 env.num_privileged_obs=1922 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[pelvis,left_hip_yaw_link,left_hip_roll_link,left_hip_pitch_link,left_knee_link,left_ankle_link,right_hip_yaw_link,right_hip_roll_link,right_hip_pitch_link,right_knee_link,right_ankle_link,torso_link,left_shoulder_pitch_link,left_shoulder_roll_link,left_shoulder_yaw_link,left_elbow_link,right_shoulder_pitch_link,right_shoulder_roll_link,right_shoulder_yaw_link,right_elbow_link] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:1 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=25 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True
    ```

6. Different Configurations on **Observation Type (with linear velocity)**

    ```text
    # OmniH2O Distill Student Policy with Linear Velocity
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_STUDENT env.num_observations=1743 env.num_privileged_obs=1820 motion.teleop_obs_version=v-teleop-extend-vr-max motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 train.distill=True train.policy.init_noise_std=0.001 env.add_short_history=True env.short_history_length=25 noise.add_noise=False noise.noise_level=0 train.dagger.load_run_dagger=TEACHER_RUN_NAME train.dagger.checkpoint_dagger=XXX train.dagger.dagger_only=True
    ```


7. Different Configurations on **Training Pipeline (without DAgger)**

    ```text
    # OmniH2O Train Sim2Real Policy with RL directly
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=OmniH2O_wo_DAgger env.num_observations=1665 env.num_privileged_obs=1742 motion.teleop_obs_version=v-teleop-extend-vr-max-nolinvel motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 noise.add_noise=False noise.noise_level=0 env.add_short_history=True env.short_history_length=25
    ```

8. Train **H2O Policy** (8point tracking, no history, MLP, with linear velocity in the state space)

    ```text
    # H2O Train Sim2Real Policy (8point tracking, no history, MLP, with linear velocity) with RL directly
    python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=H2O_Policy env.num_observations=138 env.num_privileged_obs=215 motion.teleop_obs_version=v-teleop-extend-max motion.teleop_selected_keypoints_names=[left_ankle_link,right_ankle_link,left_shoulder_pitch_link,right_shoulder_pitch_link,left_elbow_link,right_elbow_link] motion.extend_head=False num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=1.5 sim_device=cuda:0 motion.motion_file=resources/motions/h1/stable_punch.pkl rewards=rewards_teleop_omnih2o_teacher rewards.penalty_curriculum=True rewards.penalty_scale=0.5 env.add_short_history=False
    ```



# Motion Retargeting


## AMASS Dataset Preparation
Download [AMASS Dataset](https://amass.is.tue.mpg.de/index.html) with `SMPL + H G` format and put it under `human2humanoid/data/AMASS/AMASS_Complete/`:
```
|-- human2humanoid
   |-- data
      |-- AMASS
         |-- AMASS_Complete 
               |-- ACCAD.tar.bz2
               |-- BMLhandball.tar.bz2
               |-- BMLmovi.tar.bz2
               |-- BMLrub.tar
               |-- CMU.tar.bz2
               |-- ...
               |-- Transitions.tar.bz2

```

And then `cd human2humanoid/data/AMASS/AMASS_Complete` extract all the motion files by running:
```
for file in *.tar.bz2; do
    tar -xvjf "$file"
done
```

Then you should have:
```
|-- human2humanoid
   |-- data
      |-- AMASS
         |-- AMASS_Complete 
               |-- ACCAD
               |-- BioMotionLab_NTroje
               |-- BMLhandball
               |-- BMLmovi
               |-- CMU
               |-- ...
               |-- Transitions

```

## SMPL Model Preparation

Download [SMPL](https://smpl.is.tue.mpg.de/download.php) with `pkl` format and put it under `human2humanoid/data/smpl/`, and you should have:
```
|-- human2humanoid
   |-- data
      |-- smpl
         |-- SMPL_python_v.1.1.0.zip
```

Then `cd human2humanoid/data/smpl` and  `unzip SMPL_python_v.1.1.0.zip`, you should have 
```
|-- human2humanoid
   |-- data
      |-- smpl
         |-- SMPL_python_v.1.1.0
            |-- models
               |-- basicmodel_f_lbs_10_207_0_v1.1.0.pkl
               |-- basicmodel_m_lbs_10_207_0_v1.1.0.pkl
               |-- basicmodel_neutral_lbs_10_207_0_v1.1.0.pkl
            |-- smpl_webuser
            |-- ...
```
Rename these three pkl files and move it under smpl like this:
```
|-- human2humanoid
   |-- data
      |-- smpl
         |-- SMPL_FEMALE.pkl
         |-- SMPL_MALE.pkl
         |-- SMPL_NEUTRAL.pkl
```

## Retargeting AMASS to specific humanoid robot

We use an 3-step process to retarget the AMASS dataset to specific humanoid embodiments. Taking `H1` as an example here
1. Write forward kinematics of `H1` in `human2humanoid/phc/phc/utils/torch_h1_humanoid_batch.py`
2. Fit the SMPL shape that matches the `H1` kinematics in `human2humanoid/scripts/data_process/grad_fit_h1_shape.py`
3. Retarget the AMASS dataset based on the corresponding keypoints between fitted SMLP shape and `H1` using `human2humanoid/scripts/data_process/grad_fit_h1.py`

```
cd human2humanoid
python scripts/data_process/grad_fit_h1_shape.py
```

And you should have 
```
|-- human2humanoid
   |-- data
      |-- h1
         |-- shape_optimized_v1.pkl 
```

### Retargetting
   

```
cd human2humanoid
python scripts/data_process/grad_fit_h1.py
```
You should have:
```
(h2o) tairanhe@tairanhe-PRO-WS-WRX80E-SAGE-SE:~/Workspace/human2humanoid$ python scripts/data_process/grad_fit_h1.py
Importing module 'gym_38' (/home/tairanhe/Workspace/isaacgym/isaacgym/python/isaacgym/_bindings/linux-x86_64/gym_38.so)
Setting GYM_USD_PLUG_INFO_PATH to /home/tairanhe/Workspace/isaacgym/isaacgym/python/isaacgym/_bindings/linux-x86_64/usd/plugInfo.json
2024-07-11 18:35:43,587 - INFO - logger - logger initialized
  0%|                                                                                                                                                                                                                              | 0/15886 [00:00<?, ?it/s]15886 Motions to process
0-AMASS_Complete_MPI_Limits_03101_ulr1b_poses Iter: 0    256.983:   0%|                                                                                                                                                             | 0/15886 [00:01<?, ?it/s
```
After this retargeting loop done, you should have your embodiment-specific dataset ready.

To visualize the retargeted motion, you can run:

```
python scripts/vis/vis_motion.py
```


### Downloading Full retargeted motion dataset after feasibility filter: 
Download motion file `amass_phc_filtered.pkl` [here](https://cmu.box.com/s/vfi619ox7lwf2hzzi710p3g2l59aeczv), and put it under `human2humanoid/legged_gym/resources/motions/h1/amass_phc_filtered.pkl`. Make sure your running command overwrites the default motion file by `motion.motion_file=resources/motions/h1/amass_phc_filtered.pkl`


# Real-World Deployment

## System Overview
<p align="center">
  <img src="images/hardware.png" width="80%"/>
</p>

- **Robot**: [Unitree H1 EDU](https://shop.unitree.com/)
- **Perception**: [ZED mini Camera](https://store.stereolabs.com/products/zed-mini)
- **Onboard Compute**: [Orin NX (16GB)](https://www.seeedstudio.com/reComputer-J4012-p-5586.html)
- **Dexterous Hand**: [Inspire Hand](https://inspire-robots.store/collections/the-dexterous-hands?srsltid=AfmBOooJTL25MrQzRKIq5WQHDwr8ozIdlNQOdckJesxYqxeZ4uqj4Z4C)
- **Wrist Motor**: [DM-J4310-2EC](https://github.com/dmBots/DM-J4310-2EC)

## Deployment Code 

- **Unitree H1**: [Unitree H1 SDK](https://github.com/unitreerobotics/unitree_sdk2)
- **Inspire Hand**: [Inspire Hand (Unitree SDK)](hardware_code/inspire_hand.cpp)
- **Wrist Motor**: [Damiao c++ controller](hardware_code/damiao_wrist.cpp)
- **Vision Pro**: Please refer to [VisionProTeleop](https://github.com/Improbable-AI/VisionProTeleop) and [OpenTelevision](https://github.com/OpenTeleVision/TeleVision)
- **RGB Pose Estimation**: Please refer to [HybrIK](https://github.com/Jeff-sjtu/HybrIK)
- **Diffusion Policy**: Please refer to [Diffusion Policy](https://github.com/real-stanford/diffusion_policy) and [HATO](https://github.com/toruowo/hato)
- **Odometry**: [ZED mini SDK](hardware_code/zed_odometry.py)


# Trouble Shooting

## Contact
+ Deployment and Policy Learning in Sim: Tairan He, tairanh@andrew.cmu.edu
+ Motion Retargeting: Zhengyi Luo, zluo2@cs.cmu.edu

## Issues
You can create an issue if you meet any bugs, except:
+ If you cannot run the [vanilla RSL's Legged Gym](https://github.com/leggedrobotics/legged_gym), it is expected that you first go to the vanilla Legged Gym repo for help.
+ There can be CUDA-related errors when there are too many parallel environments on certain PC+GPU+driver combination: we cannot solve thiss, you can try to reduce num_envs.
+ Our codebase is only for our hardware system showcased above. We are happy to make it serve as a reference for the community, but we won't tune it for your own robots.


# Citation

This codebase builds upon prior work. Please adhere to the relevant licensing in the respective repositories.
If you use this code in your work, please consider citing our works:

```bibtex
@inproceedings{he2024learning,
  title={Learning human-to-humanoid real-time whole-body teleoperation},
  author={He, Tairan and Luo, Zhengyi and Xiao, Wenli and Zhang, Chong and Kitani, Kris and Liu, Changliu and Shi, Guanya},
  journal={arXiv preprint arXiv:2403.04436},
  year={2024}
}

@inproceedings{he2024omnih2o,
  title={OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning},
  author={He, Tairan and Luo, Zhengyi and He, Xialin and Xiao, Wenli and Zhang, Chong and Zhang, Weinan and Kitani, Kris and Liu, Changliu and Shi, Guanya},
  journal={arXiv preprint arXiv:2406.08858},
  year={2024}
}
```

Also consider citing these prior works that helped contribute to this project:

```bibtex
@inproceedings{luo2023perpetual,
  title={Perpetual humanoid control for real-time simulated avatars},
  author={Luo, Zhengyi and Cao, Jinkun and Kitani, Kris and Xu, Weipeng and others},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={10895--10904},
  year={2023}
}

@inproceedings{rudin2022learning,
  title={Learning to walk in minutes using massively parallel deep reinforcement learning},
  author={Rudin, Nikita and Hoeller, David and Reist, Philipp and Hutter, Marco},
  booktitle={Conference on Robot Learning},
  pages={91--100},
  year={2022},
  organization={PMLR}
}

@inproceedings{cheng2024open,
  title={Open-TeleVision: teleoperation with immersive active visual feedback},
  author={Cheng, Xuxin and Li, Jialong and Yang, Shiqi and Yang, Ge and Wang, Xiaolong},
  journal={arXiv preprint arXiv:2407.01512},
  year={2024}
}

@software{Park_Teleopeation_System_using,
author = {Park, Younghyo},
title = {{Teleopeation System using Apple Vision Pro}},
url = {https://github.com/Improbable-AI/VisionProTeleop},
version = {0.1.0}
}

@article{peng2018deepmimic,
  title={Deepmimic: Example-guided deep reinforcement learning of physics-based character skills},
  author={Peng, Xue Bin and Abbeel, Pieter and Levine, Sergey and Van de Panne, Michiel},
  journal={ACM Transactions On Graphics (TOG)},
  volume={37},
  number={4},
  pages={1--14},
  year={2018},
  publisher={ACM New York, NY, USA}
}


@article{lin2024learning,
   author={Lin, Toru and Zhang, Yu and Li, Qiyang and Qi, Haozhi and Yi, Brent and Levine, Sergey and Malik, Jitendra},
   title={Learning Visuotactile Skills with Two Multifingered Hands},
   journal={arXiv:2404.16823},
   year={2024}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE-CC-BY-NC-4.0.md
README.md
hardware_code/
  damiao_mvp/
    SerialPort.h
    damiao.h
    test_damiao
    test_damiao.cpp
  damiao_wrist.cpp
  inspire_hand.cpp
  zed_odometry.py
legged_gym/
  legged_gym/
    LICENSE
    __init__.py
    cfg/
    envs/
    scripts/
    utils/
  resources/
    actuator_nets/
    motions/
    objects/
    robots/
  setup.py
phc/
  phc/
    __init__.py
    env/
    learning/
    run.py
    smpllib/
    utils/
  setup.py
requirements.txt
resources/
  actuator_nets/
    anydrive_v3_lstm.pt
  objects/
    Cone/
    DiningChair/
    FoldChair/
    Human/
    Oaktree/
    OfficeChair/
    Vase/
    cylindar.urdf
    cylindar_35.urdf
  robots/
    h1/
rsl_rl/
  .gitignore
  LICENSE
  README.md
  licenses/
    dependencies/
  rsl_rl/
    __init__.py
    algorithms/
    env/
    modules/
    runners/
    storage/
    utils/
  setup.py
scripts/
  .ipynb_checkpoints/
    render_smpl_o3d-checkpoint.py
  data_process/
    convert_amass_isaac.py
    convert_data_mdm.py
    convert_data_smpl.py
    grad_fit_h1.py
    grad_fit_h1_shape.py
    process_amass_db.py
    process_amass_raw.py
  joint_monkey_h1.py
  joint_monkey_smpl.py
  mdm_test.py
  mjcf_to_urdf.py
  pmcp/
    forward_pmcp.py
  quest_camera.py
  render_smpl_o3d.py
  vis/
    joint_monkey.py
    vis_motion.py
    vis_motion_dir.py
    vis_smpl_o3d.py
    vis_smpl_o3d_ego.py
    vis_smpl_o3d_multi.py
    vis_smpl_o3d_single.py
  ws_client.py
```

## Config files (31)


### legged_gym/legged_gym/cfg/asset/asset_base.yaml

```yaml
file : ""
name : "legged_robot"  # actor name
foot_name : "None" # name of the feet bodies, used to index body state and contact force tensors
penalize_contacts_on : []
terminate_after_contacts_on : []
disable_gravity : False
collapse_fixed_joints : True # merge bodies connected by fixed joints. Specific fixed joints can be kept by adding " <... dont_collapse:"true">
fix_base_link : False # fixe the base of the robot
# default_dof_drive_mode : 3 # see GymDofDriveModeFlags (0 is none, 1 is pos tgt, 2 is vel tgt, 3 effort)
default_dof_drive_mode : 1 # see GymDofDriveModeFlags (0 is none, 1 is pos tgt, 2 is vel tgt, 3 effort)
self_collisions : 1 # 1 to disable, 0 to enable...bitwise filter
replace_cylinder_with_capsule : True # replace collision cylinders with capsules, leads to faster/more stable simulation
flip_visual_attachments : True # Some .obj meshes must be flipped from y-up to z-up

density : 0.001
angular_damping : 0.
linear_damping : 0.
max_angular_velocity : 1000.
max_linear_velocity : 1000.
armature : 0.
thickness : 0.01

terminate_by_knee_distance : False
terminate_by_lin_vel : False
terminate_by_ang_vel : False
terminate_by_gravity : False
terminate_by_low_height : False

terminate_by_ref_motion_distance : False
terminate_by_1time_motion : False

termination_scales:
  base_height : 0.3
  base_vel : 10.0
  base_ang_vel : 5.0
  gravity_x : 0.7
  gravity_y : 0.7
  min_knee_distance : 0.
```

### legged_gym/legged_gym/cfg/asset/asset_teleop.yaml

```yaml
defaults:
  - asset_base

file : 'resources/robots/h1/urdf/h1.urdf'
name : "h1"
foot_name : "ankle"
penalize_contacts_on : []
terminate_after_contacts_on : ["pelvis", "shoulder", "hip", "knee"]
self_collisions : 1 # 1 to disable, 0 to enable...bitwise filter
replace_cylinder_with_capsule : True
flip_visual_attachments : False

density : 0.001
angular_damping : 0.
linear_damping : 0.
set_dof_properties : True
default_dof_prop_damping : [5,5,5,6,2, 5,5,5,6,2, 6, 2,2,2,2, 2,2,2,2]
# default_dof_prop_stiffness : [200,200,200,300,40, 200,200,200,300,40, 300, 100,100,100,100, 100,100,100,100]
default_dof_prop_stiffness : [0,0,0,0,0, 0,0,0,0,0, 0, 0,0,0,0, 0,0,0,0]
default_dof_prop_friction : [0,0,0,0,0, 0,0,0,0,0, 0, 0,0,0,0, 0,0,0,0]
max_angular_velocity : 1000.
max_linear_velocity : 1000.
armature : 0.
thickness : 0.01

terminate_by_knee_distance : False
terminate_by_lin_vel : False
terminate_by_ang_vel : False
terminate_by_gravity : True
terminate_by_low_height : False

terminate_by_ref_motion_distance : True
terminate_by_1time_motion : True

local_upper_reward : False
zero_out_far: False # Zero out far termination
zero_out_far_change_obs: False
close_distance : 1.0
far_distance : 1.0

termination_scales:
    base_height : 0.3
    base_vel : 10.0
    base_ang_vel : 5.0
    gravity_x : 0.7
    gravity_y : 0.7
    min_knee_distance : 0.
    max_ref_motion_distance : 5.0

clip_motion_goal: True
clip_motion_goal_distance: 1.0
```

### legged_gym/legged_gym/cfg/commands/commands_base.yaml

```yaml
curriculum : False
max_curriculum : 1.
num_commands : 4 # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
resampling_time : 10. # time before command are changed[s]
heading_command : True # if true: compute ang vel command from heading error
ranges:
    lin_vel_x : [-1.0, 1.0] # min max [m/s]
    lin_vel_y : [-1.0, 1.0]   # min max [m/s]
    ang_vel_yaw : [-1, 1]    # min max [rad/s]
    heading : [-3.14, 3.14]
```

### legged_gym/legged_gym/cfg/commands/commands_teleop.yaml

```yaml
defaults:
  - commands_base

curriculum : False
max_curriculum : 0.
num_commands : 4 # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
resampling_time : 10. # time before command are changed[s]
heading_command : False # if true: compute ang vel command from heading error
ranges:
    lin_vel_x : [.0, .0] # min max [m/s]
    lin_vel_y : [.0, .0]   # min max [m/s]
    ang_vel_yaw : [.0, .0]    # min max [rad/s]
    heading : [.0, .0]
```

### legged_gym/legged_gym/cfg/config_base.yaml

```yaml
defaults:
  - _self_
  - asset: asset_base
  - commands: commands_base
  - control: control_base
  - domain_rand: domain_rand_base
  - env: env_base
  - init_state: init_state_base
  - motion: motion_base
  - noise: noise_base
  - normalization: normalization_base
  - train: ppo_base
  - rewards: rewards_base
  - sim: sim_base
  - terrain: terrain_base
  - viewer: viewer_base


project_name: "H1"
notes: "Default Notes"
exp_name: &exp_name humanoid_smpl
headless: True
seed: 0
no_log: False
test: False 
sim_device: "cuda:0"
rl_device: "cuda:0"
sim_device_id: 0
metadata: false
play: ${test}
train: True
im_dump: False
task: "h1:teleop"
load_run: ""
num_envs: 1024
checkpoint: 0

joystick: False
tmp_freeze_upper: False
max_iterations: 1000000
horovod: False
resume: False
experiment_name: null
run_name: null
compute_device_id: 0
graphics_device_id: 0
flex: False

use_gpu: True
use_gpu_pipeline: True
subscenes: 0
slices: 0
num_threads: 0


####### Testing Configs. ########
server_mode: False
no_virtual_display: False
render_o3d: False
debug: False
follow: False
add_proj: False
real_traj: False

hydra:
  job:
    name: ${exp_name}
    env_set:
      OMP_NUM_THREADS: 1
  run:
    dir: output/h1/${exp_name}


```

### legged_gym/legged_gym/cfg/config_teleop.yaml

```yaml
defaults:
  - _self_
  - asset: asset_teleop
  - commands: commands_teleop
  - control: control_teleop
  - domain_rand: domain_rand_teleop
  - env: env_teleop
  - init_state: init_state_teleop
  - motion: motion_teleop
  - noise: noise_teleop
  - normalization: normalization_teleop
  - train: ppo_teleop
  - rewards: rewards_teleop
  - sim: sim_teleop
  - terrain: terrain_teleop
  - viewer: viewer_base


project_name: "H1"
notes: "Default Notes"
exp_name: &exp_name humanoid_smpl
headless: True
seed: 1
no_log: False
test: False 
sim_device: "cuda:0"
rl_device: "cuda:0"
sim_device_id: 0
metadata: false
play: ${test}
train: True
im_dump: False
task: "h1:teleop"
load_run: ""
num_envs: 4096
checkpoint: 0

joystick: False
tmp_freeze_upper: False
max_iterations: 1000000
horovod: False
resume: False
experiment_name: null
run_name: null
compute_device_id: 0
graphics_device_id: 0
flex: False

use_gpu: True
use_gpu_pipeline: True
subscenes: 0
slices: 0
num_threads: 0


####### Testing Configs. ########
server_mode: False
no_virtual_display: False
render_o3d: False
debug: False
follow: False
add_proj: False
real_traj: False

hydra:
  job:
    name: ${exp_name}
    env_set:
      OMP_NUM_THREADS: 1
  run:
    dir: output/h1/${exp_name}

use_wandb: True


###### velocity estimation ########
train_velocity_estimation: False
use_velocity_estimation: False



```

### legged_gym/legged_gym/cfg/control/control_base.yaml

```yaml
control_type : 'P' # P: position, V: velocity, T: torques
# PD Drive parameters:
stiffness : 
  joint_a: 10.0
  joint_b: 15.  # [N*m/rad]
damping : 
  joint_a: 1.0
  joint_b: 1.5     # [N*m*s/rad]
# action scale: target angle : actionScale * action + defaultAngle
action_scale : 0.5
# decimation: Number of control action updates @ sim DT per policy DT
decimation : 4
```

### legged_gym/legged_gym/cfg/control/control_teleop.yaml

```yaml

control_type : 'P'
  # PD Drive parameters:
stiffness : 
  hip_yaw: 200
  hip_roll: 200
  hip_pitch: 200
  knee: 300
  ankle: 40
  torso: 300
  shoulder: 100
  elbow : 100 # [N*m/rad]

damping : 
  hip_yaw: 5
  hip_roll: 5
  hip_pitch: 5
  knee: 6
  ankle: 2
  torso: 6
  shoulder: 2
  elbow: 2 # [N*m/rad]  # [N*m*s/rad]

action_scale : 0.25
# decimation: Number of control action updates @ sim DT per policy DT
decimation : 4 # 4

# action_filt : False
action_filt : False
action_cutfreq : 4.0
```

### legged_gym/legged_gym/cfg/domain_rand/domain_rand_base.yaml

```yaml
randomize_base_com : False
base_com_range:
  x : [-0.1, 0.1]
  y : [-0.1, 0.1]
  z : [-0.2, 0.2]
randomize_link_mass : False
randomize_link_body_names : [
    'world', 'pelvis', 'left_hip_yaw_link', 'left_hip_roll_link', 'left_hip_pitch_link', 'left_knee_link', 
    'left_ankle_link', 'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link', 'right_knee_link', 
    'right_ankle_link', 'torso_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_shoulder_yaw_link', 
    'left_elbow_link', 'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_shoulder_yaw_link', 'right_elbow_link'
]
link_mass_range : [0.75, 1.25]
randomize_pd_gain : False
kp_range : [0.75, 1.25]
kd_range : [0.75, 1.25]
randomize_friction : False
friction_range : [0.5, 1.25]
randomize_base_mass : False
push_robots : False
push_interval_s : 15
max_push_vel_xy : 1.
randomize_torque_rfi : False
rfi_lim : 0.1

randomize_rfi_lim : True
rfi_lim_range : [0.5, 1.5]

randomize_ctrl_delay : False
ctrl_delay_step_range : [0, 4] # integer max real delay is 90ms
```

### legged_gym/legged_gym/cfg/domain_rand/domain_rand_teleop.yaml

```yaml
defaults:
  - domain_rand_base

push_robots : True
push_interval_s : 5
max_push_vel_xy : 1.0

randomize_friction : True
# randomize_friction : False
friction_range : [-0.6, 1.2]

randomize_base_mass : False # replaced by randomize_link_mass
added_mass_range : [-5., 10.]


randomize_base_com : True
base_com_range: #kg
    x : [-0.1, 0.1]
    y : [-0.1, 0.1]
    z : [-0.1, 0.1]

randomize_link_mass : True
link_mass_range : [0.7, 1.3] # *factor
randomize_link_body_names : [
    'pelvis', 'left_hip_yaw_link', 'left_hip_roll_link', 'left_hip_pitch_link', 
    'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link',  'torso_link',
]

randomize_pd_gain : True
kp_range : [0.75, 1.25]
kd_range : [0.75, 1.25]


randomize_torque_rfi : True
rfi_lim : 0.1
randomize_rfi_lim : True
rfi_lim_range : [0.5, 1.5]

randomize_ctrl_delay : True
ctrl_delay_step_range : [0, 3] # integer max real delay is 90ms

randomize_motion_ref_xyz: True # head only for now
motion_ref_xyz_range : [[-0.02, 0.02],[-0.02, 0.02],[-0.1, 0.1]]

motion_package_loss: False
package_loss_range: [1, 10] # dt = 0.02s, delay for 0.02s - 0.2s
package_loss_interval_s : 2


born_offset : False
born_offset_curriculum: False
born_offset_level_down_threshold: 50
born_offset_level_up_threshold: 120
level_degree: 0.00005
born_distance : 0.25
born_offset_range: [0.0, 1]
born_offset_possibility : 1.0

born_heading_curriculum: False
born_heading_randomization : False
born_heading_level_down_threshold: 50
born_heading_level_up_threshold: 120
born_heading_degree: 10
born_heading_range: [0, 180]
born_heading_level_degree: 0.00005
# defaults:
#   - domain_rand_base

# push_robots : False
# push_interval_s : 5
# max_push_vel_xy : 1.0

# randomize_friction : False
# # randomize_friction : False
# friction_range : [-0.6, 1.2]

# randomize_base_mass : False # replaced by randomize_link_mass
# added_mass_range : [-5., 10.]


# randomize_base_com : False
# base_com_range: #kg
#     x : [-0.1, 0.1]
#     y : [-0.1, 0.1]
#     z : [-0.1, 0.1]

# randomize_link_mass : False
# link_mass_range : [0.7, 1.3] # *factor
# randomize_link_body_names : [
#     'pelvis', 'left_hip_yaw_link', 'left_hip_roll_link', 'left_hip_pitch_link', 
#     'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link',  'torso_link',
# ]

# randomize_pd_gain : False
# kp_range : [0.75, 1.25]
# kd_range : [0.75, 1.25]


# randomize_torque_rfi : False
# rfi_lim : 0.1
# randomize_rfi_lim : False
# rfi_lim_range : [0.5, 1.5]

# randomize_ctrl_delay : False
# ctrl_delay_step_range : [1, 3] # integer max real delay is 90ms

# randomize_motion_ref_xyz: False
# motion_ref_xyz_range : [[-0.02, 0.02],[-0.02, 0.02],[-0.05, 0.05]]

# motion_package_loss: False
# package_loss_range: [1, 10] # dt = 0.02s, delay for 0.02s - 0.2s
# package_loss_interval_s : 2


# born_offset : False
# born_offset_range: [-5, 5]
# born_offset_possibility : 0.3

```

### legged_gym/legged_gym/cfg/env/env_base.yaml

```yaml
num_envs : 4096
num_observations : 48
num_privileged_obs : null # if not None a priviledge_obs_buf will be returned by step() (critic obs for assymetric training). None is returned otherwise 
num_actions : 12
env_spacing : 2.  # not used with heightfields/trimeshes 
send_timeouts : True # send time out information to the algorithm
episode_length_s : 20 # episode length in seconds
test : False

add_short_history: False
short_history_length: 5
```

### legged_gym/legged_gym/cfg/env/env_teleop.yaml

```yaml
defaults:
  - env_base

num_envs : 4096
# num_observations : 88 # v-min2
# num_privileged_obs : 164 # v-min2
# num_observations : 624
# num_observations : 87 # v-teleop
# num_privileged_obs : 163 # v-teleop
# num_observations : 84 # v-teleop-clean
# num_privileged_obs : 160 # v-teleop-clean
# num_observations : 75 # v-teleop-superclean
# num_privileged_obs : 151 # v-teleop-superclean
# num_observations : 65 # v-teleop-clean-nolastaction
# num_privileged_obs : 141 # v-teleop-clean-nolastaction
# num_observations : 90 # v-teleop_extend
# num_privileged_obs : 166 # v-teleop_extend
# num_observations : 87 # v-teleop_extend_nolinvel
# num_privileged_obs : 163 # v-teleop_extend_nolinvel

num_observations : 138 # v-teleop-extend-max
num_privileged_obs : 215 #214 # v-teleop-extend-max




# num_observations : 93 # v-teleop-extend-vr-max
# num_privileged_obs : 170 #214 # v-teleop-extend-vr-max

# num_observations : 135 # v-teleop-extend-max-nolinvel
# num_privileged_obs : 211 # v-teleop-extend-max-nolinvel

num_actions : 19
im_eval : False

add_short_history: False
short_history_length: 5
```

### legged_gym/legged_gym/cfg/init_state/init_state_base.yaml

```yaml
pos : [0.0, 0.0, 1.] # x,y,z [m]
rot : [0.0, 0.0, 0.0, 1.0] # x,y,z,w [quat]
lin_vel : [0.0, 0.0, 0.0]  # x,y,z [m/s]
ang_vel : [0.0, 0.0, 0.0]  # x,y,z [rad/s]
default_joint_angles :
  joint_a: 0. 
  joint_b: 0.
```

### legged_gym/legged_gym/cfg/init_state/init_state_teleop.yaml

```yaml
pos : [0.0, 0.0, 1.0] # xyz [m]
rot : [0.0, 0.0, 0.0, 1.0] # x,y,z,w [quat]
lin_vel : [0.0, 0.0, 0.0]  # x,y,z [m/s]
ang_vel : [0.0, 0.0, 0.0]  # x,y,z [rad/s]
max_linvel : 0.5
max_angvel : 0.5
default_joint_angles :  # : target angles [rad] when action : 0.0
    left_hip_yaw_joint : 0. 
    left_hip_roll_joint : 0            
    left_hip_pitch_joint : -0.4      
    left_knee_joint : 0.8    
    left_ankle_joint : -0.4  
    right_hip_yaw_joint : 0. 
    right_hip_roll_joint : 0 
    right_hip_pitch_joint : -0.4                                    
    right_knee_joint : 0.8                                          
    right_ankle_joint : -0.4                                  
    torso_joint : 0. 
    left_shoulder_pitch_joint : 0. 
    left_shoulder_roll_joint : 0 
    left_shoulder_yaw_joint : 0.
    left_elbow_joint  : 0.
    right_shoulder_pitch_joint : 0.
    right_shoulder_roll_joint : 0.0
    right_shoulder_yaw_joint : 0.
    right_elbow_joint : 0.

```

### legged_gym/legged_gym/cfg/motion/motion_base.yaml

```yaml
teleop : False
visualize : False
reset_at_start : False
num_markers : 0
motion_file : ''
skeleton_file : ''
marker_file : ''
num_dof_pos_reference : 0
num_dof_vel_reference : 0
num_ef_pos_reference : 0
num_ef_vel_reference : 0

curriculum : False
teleop_level_up_episode_length : 100
teleop_level_down_episode_length : 50

visualize_config:
    customize_color : True
    marker_joint_colors : 
    - [0.157, 0.231, 0.361] # pelvis
    - [0.157, 0.231, 0.361] # left_hip_yaw_joint
    - [0.157, 0.231, 0.361] # left_hip_roll_joint
    - [0.157, 0.231, 0.361] # left_hip_pitch_joint
    - [0.157, 0.231, 0.361] # left_knee_joint
    - [0.157, 0.231, 0.361] # left_ankle_joint
    - [0.157, 0.231, 0.361] # right_hip_yaw_joint
    - [0.157, 0.231, 0.361] # right_hip_roll_joint
    - [0.157, 0.231, 0.361] # right_hip_pitch_joint
    - [0.157, 0.231, 0.361] # right_knee_joint
    - [0.157, 0.231, 0.361] # right_ankle_joint
    - [0.765, 0.298, 0.498] # torso_joint
    - [1, 0.651, 0] # left_shoulder_pitch_joint
    - [1, 0.651, 0] # left_shoulder_roll_joint
    - [1, 0.651, 0] # left_shoulder_yaw_joint
    - [1, 0.651, 0] # left_elbow_joint
    - [1, 0.651, 0] # right_shoulder_pitch_joint
    - [1, 0.651, 0] # right_shoulder_roll_joint
    - [1, 0.651, 0] # right_shoulder_yaw_joint
    - [1, 0.651, 0] # right_elbow_joint
    - [1, 0.651, 0] # right_elbow_joint_extend
    - [1, 0.651, 0] # left_elbow_joint_extend
```

### legged_gym/legged_gym/cfg/motion/motion_full.yaml

```yaml
teleop : True
visualize : False
recycle_motion : True
terrain_level_down_distance : 0.5
num_markers : 19
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walking_gesture.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/standing_one_gesture.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/standing.pkl'\
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/standing_20s_fpaa30.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/stable_wave_short.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/stable_wave_short_fpaa30.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/standing_20s_fpaa30.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/wave_and_walk_unfiltered.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_run.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/gestures_3.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walking_gesture_filered_12_fix.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walking_gesture_filtered_fix.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walking_gesture_filered_4.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/stable_punch.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/stable_amass.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walk_fitted.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/bent_slowalk.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/walking_gesture_17.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_and_stable_phc_filtered.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_phc_filtered.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_phc_filtered_shrinked800.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_full.pkl'
# motion_file = "/hdd/zen/dev/copycat/h1_phc/data/h1/v2/singles/test.pkl"
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_phc_clean.pkl'
# motion_file = '{LEGGED_GYM_ROOT_DIR}/resources/motions/h1/amass_phc_clean_smooth.pkl'

motion_file : 'resources/motions/h1/amass_phc_filtered.pkl'

# motion_file : 'resources/motions/h1/walking_gesture_filered_12_fix.pkl'
skeleton_file : 'resources/robots/h1/xml/h1.xml'
marker_file : 'resources/objects/Marker/traj_marker.urdf'
num_dof_pos_reference : 19
num_dof_vel_reference : 19

extend_hand: True
extend_head: False

future_tracks: False
num_traj_samples: 1
traj_sample_timestep_inv: 50

curriculum : False
obs_noise_by_curriculum: False
push_robot_by_curriculum: False
kpkd_by_curriculum: False
rfi_by_curriculum: False


teleop_level_up_episode_length : 100
teleop_level_down_episode_length : 30


# eleop_obs_version : 'v-teleop'
# teleop_obs_version : 'v-teleop-clean'
# teleop_obs_version : 'v-teleop-superclean'
# teleop_obs_version : 'v-teleop-clean-nolastaction'
# teleop_obs_version : 'v-teleop-extend'
# teleop_obs_version : 'v-teleop-extend-nolinvel'
teleop_obs_version : 'v-teleop-extend-max'
# teleop_obs_version : 'v-teleop-extend-max-nolinvel'
# teleop_obs_version : 'v-min2'
teleop_selected_keypoints_names : [ 'pelvis',  'left_hip_yaw_link', 'left_hip_roll_link','left_hip_pitch_link', 'left_knee_link', 'left_ankle_link', 'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link', 'right_knee_link', 'right_ankle_link', 'torso_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_shoulder_yaw_link', 'left_elbow_link',  'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_shoulder_yaw_link', 'right_elbow_link']


resample_motions_for_envs : True
resample_motions_for_envs_interval_s : 1000


visualize_config:
    customize_color : True
    marker_joint_colors : 
    - [0.157, 0.231, 0.361] # pelvis
    - [0.157, 0.231, 0.361] # left_hip_yaw_joint
    - [0.157, 0.231, 0.361] # left_hip_roll_joint
    - [0.157, 0.231, 0.361] # left_hip_pitch_joint
    - [0.157, 0.231, 0.361] # left_knee_joint
    - [0.157, 0.231, 0.361] # left_ankle_joint
    - [0.157, 0.231, 0.361] # right_hip_yaw_joint
    - [0.157, 0.231, 0.361] # right_hip_roll_joint
    - [0.157, 0.231, 0.361] # right_hip_pitch_joint
    - [0.157, 0.231, 0.361] # right_knee_joint
    - [0.157, 0.231, 0.361] # right_ankle_joint
    - [0.765, 0.298, 0.498] # torso_joint
    - [1, 0.651, 0] # left_shoulder_pitch_joint
    - [1, 0.651, 0] # left_shoulder_roll_joint
    - [1, 0.651, 0] # left_shoulder_yaw_joint
    - [1, 0.651, 0] # left_elbow_joint
    - [1, 0.651, 0] # right_shoulder_pitch_joint
    - [1, 0.651, 0] # right_shoulder_roll_joint
    - [1, 0.651, 0] # right_shoulder_yaw_joint
    - [1, 0.651, 0] # right_elbow_joint
    - [1, 0.651, 0] # right_elbow_joint_extend
    - [1, 0.651, 0] # left_elbow_joint_extend
    - [1, 0.651, 0] # head_link

realtime_vr_keypoints : False
```

### legged_gym/legged_gym/cfg/motion/motion_teleop.yaml

```yaml
teleop : True
visualize : False
recycle_motion : True
terrain_level_down_distance : 0.5
num_markers : 19


# motion_file : 'resources/motions/h1/amass_phc_filtered.pkl'
motion_file : 'resources/motions/h1/stable_punch.pkl'
skeleton_file : 'resources/robots/h1/xml/h1.xml'
marker_file : 'resources/objects/Marker/traj_marker.urdf'
num_dof_pos_reference : 19
num_dof_vel_reference : 19

extend_hand: True
extend_head: False

future_tracks: False
num_traj_samples: 1
traj_sample_timestep_inv: 50

curriculum : False
obs_noise_by_curriculum: False
push_robot_by_curriculum: False
kpkd_by_curriculum: False
rfi_by_curriculum: False


teleop_level_up_episode_length : 100
teleop_level_down_episode_length : 30


# eleop_obs_version : 'v-teleop'
# teleop_obs_version : 'v-teleop-clean'
# teleop_obs_version : 'v-teleop-superclean'
# teleop_obs_version : 'v-teleop-clean-nolastaction'
# teleop_obs_version : 'v-teleop-extend'
# teleop_obs_version : 'v-teleop-extend-nolinvel'
teleop_obs_version : 'v-teleop-extend-max'
# teleop_obs_version : 'v-teleop-extend-max-nolinvel'
# teleop_obs_version : 'v-min2'
teleop_selected_keypoints_names : ['left_ankle_link', 'right_ankle_link', 'left_shoulder_pitch_link','right_shoulder_pitch_link', 'left_elbow_link', 'right_elbow_link']


resample_motions_for_envs : True
resample_motions_for_envs_interval_s : 1000


visualize_config:
    customize_color : True
    marker_joint_colors : 
    - [0.157, 0.231, 0.361] # pelvis
    - [0.157, 0.231, 0.361] # left_hip_yaw_joint
    - [0.157, 0.231, 0.361] # left_hip_roll_joint
    - [0.157, 0.231, 0.361] # left_hip_pitch_joint
    - [0.157, 0.231, 0.361] # left_knee_joint
    - [0.157, 0.231, 0.361] # left_ankle_joint
    - [0.157, 0.231, 0.361] # right_hip_yaw_joint
    - [0.157, 0.231, 0.361] # right_hip_roll_joint
    - [0.157, 0.231, 0.361] # right_hip_pitch_joint
    - [0.157, 0.231, 0.361] # right_knee_joint
    - [0.157, 0.231, 0.361] # right_ankle_joint
    - [0.765, 0.298, 0.498] # torso_joint
    - [1, 0.651, 0] # left_shoulder_pitch_joint
    - [1, 0.651, 0] # left_shoulder_roll_joint
    - [1, 0.651, 0] # left_shoulder_yaw_joint
    - [1, 0.651, 0] # left_elbow_joint
    - [1, 0.651, 0] # right_shoulder_pitch_joint
    - [1, 0.651, 0] # right_shoulder_roll_joint
    - [1, 0.651, 0] # right_shoulder_yaw_joint
    - [1, 0.651, 0] # right_elbow_joint
    - [1, 0.651, 0] # right_elbow_joint_extend
    - [1, 0.651, 0] # left_elbow_joint_extend
    - [1, 0.651, 0] # head_link

realtime_vr_keypoints : False
```

### legged_gym/legged_gym/cfg/noise/noise_base.yaml

```yaml
add_noise : False
noise_level : 1.0 # scales other values
noise_scales:
    dof_pos : 0.01 # joint angle
    dof_vel : 0.02 # joint angle velocity 
    lin_vel : 0.1 # root linear velocity
    ang_vel : 0.2  # root angular velocity
    gravity : 0.05 # gravity
    height_measurements : 0.1 # height measurements
    body_pos : 0.01 # body pos in cartesian space: 19x3
    body_lin_vel : 0.01 # body velocity in cartesian space: 19x3
    body_rot : 0.01 # 6D body rotation 
    ref_body_pos : 0
    ref_body_rot : 0
    ref_lin_vel : 0
    ref_ang_vel : 0
    ref_dof_pos : 0
    ref_dof_vel : 0
    ref_gravity : 0
    delta_base_pos : 0.05
    delta_heading : 0.1
```

### legged_gym/legged_gym/cfg/noise/noise_teleop.yaml

```yaml
### For noise, do not use the defaults from noise_base.yaml. 
add_noise : True # False for teleop sim right now
noise_level : 1.0 # scales other values
noise_scales:
    base_z : 0.05
    dof_pos : 0.01
    dof_vel : 0.1
    lin_vel : 0.2
    lin_acc : 0.2 # ???????????????
    ang_vel : 0.5
    gravity : 0.1
    in_contact : 0.1
    height_measurements : 0.05
    body_pos : 0.01 # body pos in cartesian space: 19x3
    body_rot : 0.01 # body pos in cartesian space: 19x3
    body_lin_vel : 0.01 # body velocity in cartesian space: 19x3
    body_ang_vel : 0.01 # body velocity in cartesian space: 19x3
    delta_base_pos : 0.05
    delta_heading : 0.1
    last_action : 0.0
    
    ref_body_pos : 0.05
    ref_body_rot : 0.01
    ref_body_vel : 0.01
    ref_lin_vel : 0.01
    ref_ang_vel : 0.01
    ref_dof_pos : 0.01
    ref_dof_vel : 0.01
    ref_gravity : 0.01
```

### legged_gym/legged_gym/cfg/normalization/normalization_base.yaml

```yaml
obs_scales:
    lin_vel : 2.0
    ang_vel : 0.25
    dof_pos : 1.0
    dof_vel : 0.05
    height_measurements : 5.0
    body_pos : 1.0
    body_lin_vel : 1.0
    body_rot : 1.0
    delta_base_pos : 1.0
    delta_heading : 1.0
clip_observations : 100.
clip_actions : 100.
```

### legged_gym/legged_gym/cfg/normalization/normalization_teleop.yaml

```yaml
obs_scales:
  lin_vel : 1.0 # 2.0
  lin_acc : 1.0 # ????????????
  ang_vel : 1.0 # 0.25
  dof_pos : 1.0 # 1.0
  dof_vel : 1.0 # 0.05
  height_measurements : 1.0 # 5.0
  body_pos : 1.0
  body_lin_vel : 1.0
  body_rot : 1.0
  delta_base_pos : 1.0
  delta_heading : 1.0
clip_actions : 100.
clip_observations : 100.
```

### legged_gym/legged_gym/cfg/rewards/rewards_base.yaml

```yaml
scales:
  termination : -0.0
  tracking_lin_vel : 1.0
  tracking_ang_vel : 0.5
  lin_vel_z : -2.0
  ang_vel_xy : -0.05
  orientation : -0.
  torques : -0.00001
  dof_vel : -0.
  dof_acc : -2.5e-7
  base_height : -0. 
  feet_air_time :  1.0
  collision : -1.
  feet_stumble : -0.0 
  action_rate : -0.01
  stand_still : -0.
  joint_position : 0.
  joint_vel : 0.
  body_position : 0.
  body_rotation : 0.
  body_vel : 0.
  body_ang_vel : 0.
feet_max_height_for_this_air : 0.25
max_penalty_compared_to_positive : False
max_penalty_compared_to_positive_coef : 0.5
scaling_down_body_pos_sigma : True
teleop_body_pos_sigma_scaling_down_coef : 0.999
only_positive_rewards : True # if true negative total rewards are clipped at zero (avoids early termination problems)
tracking_sigma : 0.25 # tracking reward : exp(-error^2/sigma)
soft_dof_pos_limit : 1. # percentage of urdf limits, values above this limit are penalized
soft_dof_vel_limit : 1.
soft_torque_limit : 1.
base_height_target : 1.
max_contact_force : 100. # forces above this value are penalized
joint_pos_sigma : 1.
joint_vel_sigma : 1.
body_pos_sigma : 1.
body_rot_sigma : 1.
body_vel_sigma : 1.
body_ang_vel_sigma : 1.
teleop_body_rot_selection : ['pelvis']
teleop_body_vel_selection : ['pelvis']
teleop_body_pos_selection : ['pelvis']
teleop_body_ang_vel_selection : ['pelvis']

```

### legged_gym/legged_gym/cfg/rewards/rewards_teleop_omnih2o_teacher.yaml

```yaml
scales:
  # regularization penalty
  torques : -0.0001
  torque_limits : -2.
  dof_acc : -0.000011 #-8.4e-6   -4.2e-7 #-3.5e-8
  dof_vel : -0.004 # -0.003
  # action_rate : -0.6 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  lower_action_rate : -3.0 # -1.35 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  upper_action_rate : -0.625 # 0.0625 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  dof_pos_limits : -100.0*1.25
  dof_vel_limits : -50.
  termination : -200*1.25
  feet_contact_forces : -0.75 # 0.125
  stumble : -1000.0*1.25
  feet_air_time_teleop : 1000
  slippage : -30.0*1.25
  feet_ori : -50.0*1.25
  in_the_air: -200 # -150 # < -1
  stable_lower_when_vrclose: 0 #-500.0
  stable_lower_when_vrclose_positive: 0 #-500.0
  orientation : -200.0
  feet_height : -0
  feet_max_height_for_this_air : -2500
  


  # torques : 0
  # torque_limits : 0
  # dof_acc : 0 #-8.4e-6   -4.2e-7 #-3.5e-8
  # dof_vel : 0 # -0.003
  # # action_rate : -0.6 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  # lower_action_rate : 0 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  # upper_action_rate : 0 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  # dof_pos_limits : 0
  # termination : -200*1.25
  # feet_contact_forces : 0
  # stumble : 0
  # feet_air_time_teleop : 0
  # slippage : -0
  # feet_ori : 0 = python legged_gym/scripts/train_hydra.py --config-name=config_teleop task=h1:teleop run_name=3pointvr_upperrewardonly_sigma_curriculum0.01-1penalty_curriculum0.25-1 env.num_observations=93 env.num_privileged_obs=170 motion.teleop_obs_version=v-teleop-extend-vr-max motion.teleop_selected_keypoints_names=[] motion.extend_head=True num_envs=4096 asset.zero_out_far=False asset.termination_scales.max_ref_motion_distance=10.0 sim_device=cuda:0 rewards.sigma_curriculum=True rewards.penalty_curriculum=Truereward
  # orientation : -0.0


  # # teleop task rewards
  # teleop_joint_position_lower : 32 # 5.0
  # teleop_joint_position_upper : 32 # 5.0
  # teleop_joint_vel_lower : 16  # 5.
  # teleop_joint_vel_upper : 16  # 5.
  # teleop_body_position_extend_lower : 40 * 1.4 # 8 keypoint
  # teleop_body_position_extend_upper : 40 * 1.4 # 8 keypoint
  # teleop_body_position_vr_3keypoints : 60 * 1.4 # 8 keypoint
  # teleop_body_rotation_lower : 20
  # teleop_body_rotation_upper : 20
  # teleop_body_vel_lower : 8
  # teleop_body_vel_upper : 8 
  # teleop_body_ang_vel_lower: 8 
  # teleop_body_ang_vel_upper: 8 

  # ============================= 0421 version rewards
  closing: 0
  # teleop upper only
  # teleop_joint_position_lower : 0 # 5.0
  # teleop_joint_position_upper : 32  # 5.0
  # teleop_joint_vel_lower : 0  # 5.
  # teleop_joint_vel_upper : 16  # 5.
  # teleop_body_position_extend_lower : 0 # 8 keypoint
  # teleop_body_position_extend_upper : 0 # 8 keypoint
  # teleop_body_position_extend_upper_0dot5sigma : 40 # 8 keypoint
  # teleop_body_position_vr_3keypoints : 0 # 8 keypoint
  # teleop_body_rotation_lower : 0
  # teleop_body_rotation_upper : 20
  # teleop_body_vel_lower : 0
  # teleop_body_vel_upper : 8
  # teleop_body_ang_vel_lower: 0 
  # teleop_body_ang_vel_upper: 8 

  # ============================= 0406 version rewards (all whole body rewards)
  teleop_selected_joint_position : 32 # 5.0
  teleop_selected_joint_vel : 16 # 5.
  teleop_body_position : 0.0 # 6 keypoint
  teleop_body_position_extend :  30 # wholebody
  teleop_body_position_extend_small_sigma : 0.0 # wholebody
  teleop_body_position_extend_upper: 0
  teleop_body_position_vr_3keypoints : 50 # 8 keypoint
  teleop_body_rotation : 20.0
  teleop_body_vel : 8.0
  teleop_body_ang_vel : 8.0
  

  # teleop_selected_joint_position : 32 # 5.0
  # teleop_selected_joint_vel : 16 # 5.
  # teleop_body_position : 0.0 # 6 keypoint
  # teleop_body_position_extend :  40 # 8 keypoint
  # teleop_body_position_extend_small_sigma : 0.0 # 8 keypoint
  # teleop_body_rotation : 0
  # teleop_body_vel : 8
  # teleop_body_ang_vel : 8

desired_feet_max_height_for_this_air : 0.25
feet_height_target: 0.2
vrclose_threshold: 0.10
ref_stable_velocity_threshold: 0.05
only_positive_rewards : False # if true negative total rewards are clipped at zero (avoids early termination problems)
tracking_sigma : 0.25 # tracking reward : exp(-error^2/sigma)
soft_dof_pos_limit : 0.85 # percentage of urdf limits values above this limit are penalized
soft_dof_vel_limit : 0.85
soft_torque_limit : 0.85

max_contact_force : 500.

base_height_target : 1.
body_pos_sigma : 0.5
body_rot_sigma : 1.
body_vel_sigma : 1.
body_ang_vel_sigma : 1.
joint_pos_sigma : 1.
joint_vel_sigma : 1.

max_penalty_compared_to_positive : False
max_penalty_compared_to_positive_coef : 0.5
scaling_down_body_pos_sigma : True
teleop_body_pos_sigma_scaling_down_coef : 0.999

# teleop_joint_pos_small_sigma : 0.1 # 0.5 -> 0.1 lower body
teleop_joint_pos_sigma : 0.5 
teleop_joint_vel_sigma : 10 # 10 -> 5
teleop_body_pos_lowerbody_sigma : 0.5 # 0.01
teleop_body_pos_0dot5sigma : 0.5 # 0.01
teleop_body_pos_upperbody_sigma : 0.03 # -> 0.03
teleop_body_pos_vr_3keypoints_sigma : 0.03 # 0.002->0.03

teleop_body_pos_lowerbody_weight : 0.5
teleop_body_pos_upperbody_weight : 1.0
teleop_body_rot_sigma : 0.1
teleop_body_vel_sigma : 10 # 10 -> 5
teleop_body_ang_vel_sigma : 10 # 10 -> 5


teleop_body_rot_selection : ['pelvis']
teleop_body_vel_selection : ['pelvis']
teleop_body_pos_selection : ['pelvis']
teleop_body_ang_vel_selection : ['pelvis']
teleop_joint_pos_selection : 
  # upper body
  torso_joint: 2.0
  left_shoulder_pitch_joint: 2.0
  left_shoulder_roll_joint: 2.0
  left_shoulder_yaw_joint: 2.0
  left_elbow_joint: 2.0
  right_shoulder_pitch_joint: 2.0
  right_shoulder_roll_joint: 2.0
  right_shoulder_yaw_joint: 2.0
  right_elbow_joint: 2.0
  # lower body
  left_hip_pitch_joint: 2.0
  left_hip_roll_joint: 0.5
  left_hip_yaw_joint: 0.5
  left_knee_joint: 0.5
  left_ankle_joint: 0.5
  right_hip_pitch_joint: 2.0
  right_hip_roll_joint: 0.5
  right_hip_yaw_joint: 0.5
  right_knee_joint: 0.5
  right_ankle_joint: 0.5

# curriculum: False
sigma_curriculum: False
num_compute_average_epl : 10000
teleop_body_pos_upperbody_sigma_range: [0.02, 1.0]
reward_position_sigma_level_up_threshold: 50
reward_position_sigma_level_down_threshold: 120

penalty_curriculum: False
penalty_scale : 1.0
penalty_scale_range: [0.25, 1.0]
penalty_level_down_threshold: 50
penalty_level_up_threshold: 120

level_degree: 0.00001

penalty_reward_names : [  "torques",
  "torque_limits",
  "dof_acc",
  "dof_vel",
  # action_rate : -0.6 # -0.6  # -0.3 # -0.3 -0.12 -0.01
  "lower_action_rate",
  "upper_action_rate",
  "dof_pos_limits",
  "termination",
  "feet_contact_forces",
  "stumble",
  "feet_air_time_teleop",
  "slippage",
  "feet_ori",
  "orientation",
  "in_the_air",
  "stable_lower_when_vrclose"]
```

### legged_gym/legged_gym/cfg/sim/sim_base.yaml

```yaml
dt :  0.005
substeps : 1
gravity : [0., 0. ,-9.81]  # [m/s^2]
up_axis : 1  # 0 is y, 1 is z

physx:
    num_threads : 4
    solver_type : 1  # 0: pgs, 1: tgs
    num_position_iterations : 4
    num_velocity_iterations : 0
    contact_offset : 0.02  # [m]
    rest_offset : 0.0   # [m]
    bounce_threshold_velocity : 0.2 #0.5 [m/s]
    max_depenetration_velocity : 10
    max_gpu_contact_pairs : 16777216 #  -> needed for 8000 envs and more
    default_buffer_size_multiplier : 10
    contact_collection : 2 # 0: never, 1: last sub-step, 2: all sub-steps (default:2)
```

### legged_gym/legged_gym/cfg/sim/sim_teleop.yaml

```yaml
defaults:
  - sim_base

dt : 0.005  #   1/60.
```

### legged_gym/legged_gym/cfg/terrain/terrain_base.yaml

```yaml
mesh_type : 'plane' # "heightfield" # none, plane, heightfield or trimesh
# mesh_type : 'trimesh' # "heightfield" # none, plane, heightfield or trimesh
horizontal_scale : 0.1 # [m]
vertical_scale : 0.005 # [m]
border_size : 25 # [m]
# curriculum : True
curriculum : False
static_friction : 1.0
dynamic_friction : 1.0
restitution : 0.
# rough terrain only:
measure_heights : False # keep it False
measured_points_x : [-0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] # 1mx1.6m rectangle (without center line)
measured_points_y : [-0.5, -0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3, 0.4, 0.5]
selected : False # select a unique terrain type and pass all arguments
terrain_kwargs : None # Dict of arguments for selected terrain
max_init_terrain_level : 9 # starting curriculum state
terrain_length : 8.
terrain_width : 8.
num_rows: 10 # number of terrain rows (levels)
num_cols : 20 # number of terrain cols (types)
# terrain types: [smooth slope, rough slope, stairs up, stairs down, discrete]
terrain_proportions : [0.5, 0.5]
# trimesh only:
slope_treshold : 0.75 # slopes above this threshold will be corrected to vertical surfaces
```

### legged_gym/legged_gym/cfg/terrain/terrain_teleop.yaml

```yaml
defaults:
  - terrain_base

# mesh_type : 'plane' # "heightfield" # none, plane, heightfield or trimesh
# mesh_type : 'plane' # "heightfield" # none, plane, heightfield or trimesh
mesh_type : 'trimesh' # "heightfield" # none, plane, heightfield or trimesh
horizontal_scale : 0.1 # [m]
vertical_scale : 0.005 # [m]
border_size : 25 # [m]
curriculum : False
# curriculum : False
static_friction : 1.0
dynamic_friction : 1.0
restitution : 0.
# rough terrain only:
measure_heights : True # keep it False
measured_points_x : [ 0.] # 1mx1.6m rectangle (without center line)
measured_points_y : [ 0.]
selected : False # select a unique terrain type and pass all arguments
terrain_kwargs : null # Dict of arguments for selected terrain
max_init_terrain_level : 9 # starting curriculum state
terrain_length : 8.
terrain_width : 8.
num_rows: 10 # number of terrain rows (levels)
num_cols : 20 # number of terrain cols (types)
terrain_types : ['flat', 'rough', 'low_obst', 'smooth_slope', 'rough_slope']  # do not duplicate!
# terrain_proportions : [0.2, 0.2, 0.2, 0.2, 0.2]
terrain_proportions : [0.2, 0.6, 0.2, 0.0, 0.0]
# trimesh only:
slope_treshold : 0.75 # slopes above this threshold will be corrected to vertical surfaces
```

### legged_gym/legged_gym/cfg/train/ppo_base.yaml

```yaml
seed : 1
runner_class_name : 'OnPolicyRunner'
policy:
    init_noise_std : 1.0
    actor_hidden_dims : [512, 256, 128]
    critic_hidden_dims : [512, 256, 128]
    activation : 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
    # only for 'ActorCriticRecurrent':
    # rnn_type : 'lstm'
    # rnn_hidden_size : 512
    # rnn_num_layers : 1

add_short_history: False
short_history_length: 5

algorithm:
    # training params
    value_loss_coef : 1.0
    use_clipped_value_loss : True
    clip_param : 0.2
    entropy_coef : 0.01
    num_learning_epochs : 5
    num_mini_batches : 4 # mini batch size : num_envs*nsteps / nminibatches
    learning_rate : 1.e-3 #5.e-4
    schedule : 'adaptive' # could be adaptive, fixed
    gamma : 0.99
    lam : 0.95
    desired_kl : 0.01
    max_grad_norm : 1.
    action_smoothness_coef : 0.0

runner:
    policy_class_name : 'ActorCritic'
    # policy_calss_name : 'ActorCriticRecurrent'
    algorithm_class_name : 'PPO'
    num_steps_per_env : 24 # per iteration
    max_iterations : 100000 # number of policy updates

    # logging
    save_interval : 500 # check for potential saves every this many iterations
    experiment_name : 'test'
    run_name : ''
    # load and resume
    resume : False
    load_run : -1 # -1 : last run
    checkpoint : -1 # -1 : last saved model
    resume_path : None # updated from load_run and chkpt
    

```

### legged_gym/legged_gym/cfg/train/ppo_pulse.yaml

```yaml
defaults:
  - ppo_base

distill: False
distill_model_config: 
  obs_v: v-teleop-extend-max-full
  extend_head: True
  future_tracks: True
  num_traj_samples: 1
  teleop_selected_keypoints_names : [ 'pelvis',  'left_hip_yaw_link', 'left_hip_roll_link','left_hip_pitch_link', 'left_knee_link', 'left_ankle_link', 'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link', 'right_knee_link', 'right_ankle_link', 'torso_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_shoulder_yaw_link', 'left_elbow_link',  'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_shoulder_yaw_link', 'right_elbow_link']
  num_observations: 913
  num_privileged_obs: 990

add_short_history: False
short_history_length: 5


algorithm:
    # training params
    value_loss_coef : 1.0
    use_clipped_value_loss : True
    clip_param : 0.2
    entropy_coef : 0.005
    num_learning_epochs : 5
    num_mini_batches : 4 # mini batch size : num_envs*nsteps / nminibatches
    learning_rate : 1.e-3 #5.e-4
    schedule : 'adaptive' # could be adaptive, fixed
    gamma : 0.99
    lam : 0.95
    desired_kl : 0.01
    max_grad_norm : 0.2
    action_smoothness_coef : 0.000 # 0.003
    kin_only: True
    save_z_noise: True
    z_type: "vae"
    
runner:
    run_name : ''
    policy_class_name : 'ActorCriticPULSE'
    experiment_name : 'h1:teleop'
    max_iterations : 10000000
    has_eval : False
    eval_interval: 2500
    auto_negative_samping: False
policy:
    init_noise_std : 1.0
    actor_hidden_dims : [512, 256, 128]
    # actor_hidden_dims : [512*4, 256*4, 128*4]
    critic_hidden_dims : [512, 256, 128]
    # critic_hidden_dims : [512*4, 256*4, 128*4]

    embedding_size: 8
    use_vae_prior: True
    use_ar1_prior: True
    use_vae_clamped_prior: True
    vae_var_clamp_max: 2
    kld_coefficient_max: 0.01
    kld_coefficient_min: 0.001
    kld_anneal: True
    kld_reverse_anneal: False
    ar1_coefficient: 0.005



```

### legged_gym/legged_gym/cfg/train/ppo_teleop.yaml

```yaml
defaults:
  - ppo_base

distill: False
distill_model_config: 
  obs_v: v-teleop-extend-max-full
  extend_head: True
  future_tracks: True
  num_traj_samples: 1
  teleop_selected_keypoints_names : [ 'pelvis',  'left_hip_yaw_link', 'left_hip_roll_link','left_hip_pitch_link', 'left_knee_link', 'left_ankle_link', 'right_hip_yaw_link', 'right_hip_roll_link', 'right_hip_pitch_link', 'right_knee_link', 'right_ankle_link', 'torso_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_shoulder_yaw_link', 'left_elbow_link',  'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_shoulder_yaw_link', 'right_elbow_link']
  num_observations: 913
  num_privileged_obs: 990

add_short_history: False
short_history_length: 5

algorithm:
    # training params
    value_loss_coef : 1.0
    use_clipped_value_loss : True
    clip_param : 0.2
    entropy_coef : 0.005
    num_learning_epochs : 5
    num_mini_batches : 4 # mini batch size : num_envs*nsteps / nminibatches
    learning_rate : 1.e-3 #5.e-4
    schedule : 'adaptive' # could be adaptive, fixed
    gamma : 0.99
    lam : 0.95
    desired_kl : 0.01
    max_grad_norm : 0.2
    action_smoothness_coef : 0.000 # 0.003
    
runner:
    policy_class_name : 'ActorCritic'
    run_name : ''
    experiment_name : 'h1:teleop'
    max_iterations : 10000000
    has_eval : False
    eval_interval: 2500
    auto_negative_samping: False
policy:
    rnn_type : 'lstm'
    init_noise_std : 1.0
    actor_hidden_dims : [512, 256, 128]
    # actor_hidden_dims : [512*4, 256*4, 128*4]
    critic_hidden_dims : [512, 256, 128]
    # critic_hidden_dims : [512*4, 256*4, 128*4]
dagger:
  ###### Dagger ########
  load_run_dagger: ""
  checkpoint_dagger: 0
  dagger_only: False
  dagger_anneal: False

```

### legged_gym/legged_gym/cfg/viewer/viewer_base.yaml

```yaml
debug_viz : False
ref_env : 0
pos : [10, 0, 6]  # [m]
lookat : [11., 5, 3.]  # [m]
```

## Python signatures and reward/observation bodies (34 files)


### legged_gym/legged_gym/envs/base/base_config.py

```
class BaseConfig()
    def __init__(self)
    def init_member_classes(obj)
```

### legged_gym/legged_gym/envs/base/base_task.py

```
class BaseTask()
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def get_observations(self)
    def get_privileged_observations(self)
    def reset_idx(self, env_ids)
    def reset(self)
    def step(self, actions)
    def next_task(self)
    def render(self, sync_frame_time)

```python
def get_observations(self):
        return self.obs_buf
```

```python
def get_privileged_observations(self):
        return self.privileged_obs_buf
```
```

### legged_gym/legged_gym/envs/base/legged_robot.py

```
class LeggedRobot(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, sim_device, headless)
    def setup_kin_info(self)
    def load_expert(self)
    def step(self, actions)
    def _refresh_sim_tensors(self)
    def post_physics_step(self)
    def begin_seq_motion_samples(self)
    def check_termination(self)
    def reset_idx(self, env_ids)
    def compute_reward(self)
    def update_freeze_ref(self, motion_res, index)
    def compute_observations(self)
    def compute_self_and_task_obs(self)
    def create_sim(self)
    def _create_trimesh(self)
    def _init_height_points(self)
    def _get_heights(self, position, env_ids)
    def set_camera(self, position, lookat)
    def _update_realtime_vr_keypoints(self, keypoints_pos, keypoints_vel)
    def _draw_debug_vis(self)
    def _process_rigid_shape_props(self, props, env_id)
    def _process_dof_props(self, props, env_id)
    def _process_rigid_body_props(self, props, env_id)
    def _post_physics_step_callback(self)
    def _resample_commands(self, env_ids)
    def _compute_torques(self, actions)
    def _reset_dofs(self, env_ids)
    def _reset_root_states(self, env_ids)
    def _push_robots(self)
    def _freeze_ref_motion(self)
    def _update_terrain_curriculum(self, env_ids)
    def update_command_curriculum(self, env_ids)
    def update_average_episode_length(self, env_ids)
    def _update_sigma_curriculum(self)
    def _update_penalty_curriculum(self)
    def _update_born_offset_curriculum(self)
    def _update_born_heading_curriculum(self)
    def _update_teleop_curriculum(self, env_ids)
    def _get_noise_scale_vec(self, cfg)
    def _episodic_domain_randomization(self, env_ids)
    def _init_buffers(self)
    def _init_domain_params(self)
    def _prepare_reward_function(self)
    def _create_ground_plane(self)
    def _create_envs(self)
    def _get_env_origins(self)
    def _parse_cfg(self, cfg)
    def _load_motion(self)
    def resample_motion(self)
    def forward_motion_samples(self)
    def _resample_motion_times(self, env_ids)
    def _get_state_from_motionlib_cache(self, motion_ids, motion_times, offset)
    def _get_state_from_motionlib_cache_trimesh(self, motion_ids, motion_times, offset)
    def _load_marker_asset(self)
    def _get_rigid_body_pos(self, body_name)
    def knee_distance(self)
    def feet_distance(self)
    def _reward_closing(self)
    def _reward_in_the_air(self)
    def _reward_stable_lower_when_vrclose(self)
    def _reward_stable_lower_when_vrclose_positive(self)
    def _reward_lin_vel_z(self)
    def _reward_ang_vel_xy(self)
    def _reward_orientation(self)
    def _reward_feet_ori(self)
    def _reward_base_height(self)
    def _reward_feet_height(self)
    def _reward_torques(self)
    def _reward_dof_vel(self)
    def _reward_dof_acc(self)
    def _reward_action_rate(self)
    def _reward_lower_action_rate(self)
    def _reward_upper_action_rate(self)
    def _reward_collision(self)
    def _reward_termination(self)
    def _reward_dof_pos_limits(self)
    def _reward_dof_vel_limits(self)
    def _reward_torque_limits(self)
    def _reward_close_feet(self)
    def _reward_tracking_lin_vel(self)
    def _reward_tracking_ang_vel(self)
    def _reward_freeze_upper_body(self)
    def _reward_tracking_dof_vel(self)
    def _reward_teleop_joint_position_lower(self)
    def _reward_teleop_joint_position_upper(self)
    def _reward_teleop_selected_joint_position(self)
    def _reward_teleop_joint_vel_lower(self)
    def _reward_teleop_joint_vel_upper(self)
    def _reward_teleop_selected_joint_vel(self)
    def _reward_teleop_body_position(self)
    def _reward_teleop_body_position_extend_small_sigma(self)
    def _reward_teleop_body_position_extend(self)
    def _reward_teleop_body_position_extend_lower(self)
    def _reward_teleop_body_position_extend_upper(self)
    def _reward_teleop_body_position_extend_upper_0dot5sigma(self)
    def _reward_teleop_body_position_vr_3keypoints(self)
    def _reward_teleop_body_position_extend_small_sigma(self)
    def _reward_teleop_body_rotation(self)
    def _reward_teleop_body_rotation_lower(self)
    def _reward_teleop_body_rotation_upper(self)
    def _reward_teleop_selected_body_rotation(self)
    def _reward_teleop_body_vel(self)
    def _reward_teleop_body_vel_lower(self)
    def _reward_teleop_body_vel_upper(self)
    def _reward_teleop_selected_body_vel(self)
    def _reward_teleop_body_ang_vel(self)
    def _reward_teleop_body_ang_vel_lower(self)
    def _reward_teleop_body_ang_vel_upper(self)
    def _reward_teleop_selected_body_ang_vel(self)
    def _reward_feet_max_height_for_this_air(self)
    def _reward_feet_air_time_teleop(self)
    def _reward_slippage(self)
    def _reward_alive(self)
    def _reward_stumble(self)
    def _reward_stand_still(self)
    def _reward_move_or_not(self)
    def _reward_feet_contact_forces(self)
    def _reward_no_fly(self)
    def _reward_freeze_arms(self)
    def render(self, sync_frame_time)
    def _init_camera(self)
    def _update_camera(self)
    def next_task(self)
    def _update_recovery_count(self)
    def _update_package_loss_count(self)
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, root_vel, root_ang_vel, dof_pos, dof_vel, ref_body_pos, ref_body_rot, ref_root_vel, ref_root_ang_vel, ref_dof_pos, ref_dof_vel, time_steps)
def compute_imitation_observations_teleop(root_pos, root_rot, root_vel, body_pos, ref_body_pos, time_steps)
def compute_imitation_observations_teleop_max(root_pos, root_rot, body_pos, ref_body_pos, ref_body_vel, time_steps, ref_episodic_offset, ref_vel_in_task_obs)
def compute_imitation_observations_teleop_max_heading(root_pos, root_rot, body_pos, head_rot, ref_body_pos, ref_head_rot, ref_body_vel, time_steps, ref_episodic_offset, ref_vel_in_task_obs)
def compute_humanoid_observations(body_pos, body_rot, root_vel, root_ang_vel, dof_pos, dof_vel, local_root_obs, root_height_obs)
def compute_humanoid_observations_max_full(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs)
def compute_imitation_observations_max_full(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, ref_episodic_offset, ref_vel_in_task_obs)

```python
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, root_vel, root_ang_vel, dof_pos, dof_vel, ref_body_pos, ref_body_rot, ref_root_vel, ref_root_ang_vel, ref_dof_pos, ref_dof_vel, time_steps):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor,Tensor,Tensor,Tensor, Tensor, int) -> Tensor
    # V7 with the addition of head position. 
    obs = []
    B, J, _ = body_pos.shape

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot[:, None].repeat_interleave(time_steps, 1)))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences for root
    diff_global_root_vel = ref_root_vel.view(B, time_steps,3) - root_vel.view(B, 1, 3)
    diff_local_root_vel = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), diff_global_root_vel.view(-1, 3))
    
    diff_global_root_ang_vel = ref_root_ang_vel.view(B, time_steps, 3) - root_ang_vel.view(B, 1, 3)
    diff_local_root_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot.view(-1, 4), diff_global_root_ang_vel.view(-1, 3))
    

    ##### body pos + Dof_pos This part will have proper futuers.
    local_ref_body_pos = ref_body_pos.view(B, time_steps, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_ref_body_pos = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), local_ref_body_pos.view(-1, 3))

    local_ref_body_rot = torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), ref_body_rot.view(-1, 4))
    local_ref_body_rot = torch_utils.quat_to_tan_norm(local_ref_body_rot)

    ###### Dof difference
    dof_diff = ref_dof_pos.view(B, time_steps, -1) - dof_pos.view(B, 1, -1)
    dof_vel_diff = ref_dof_vel.view(B, time_steps, -1) - dof_vel.view(B, 1, -1)


    # make some changes to how futures are appended.
    obs.append(diff_local_body_pos_flat.view(B, time_steps, -1))  # 1 * timestep * J * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, time_steps, -1))  #  1 * timestep * J * 6
    obs.append(diff_local_root_vel.view(B, time_steps, -1))  # timestep  * J * 3
    obs.append(diff_local_root_ang_vel.view(B, time_steps, -1))  # timestep  * J * 3
    obs.append(local_ref_body_pos.view(B, time_steps, -1))  # timestep  * J * 3
    obs.append(local_ref_body_rot.view(B, time_steps, -1))  # timestep  * J * 6
    obs.append(dof_diff.view(B, time_steps, -1))  # timestep  * J * 3
    obs.append(dof_vel_diff.view(B, time_steps, -1))  # timestep  * J * 3

    
    # print(obs[0].shape, obs[1].shape, obs[2].shape, obs[3].shape, obs[4].shape, obs[5].shape, obs[6].shape, obs[7].shape)
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_imitation_observations_teleop(root_pos, root_rot, root_vel, body_pos, ref_body_pos, time_steps):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, int) -> Tensor
    # V7 with the addition of head position. 
    obs = []
    B, J, _ = body_pos.shape

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    


    # ##### body pos + Dof_pos This part will have proper futuers.
    local_ref_body_pos = ref_body_pos.view(B, time_steps, J, 3) - root_pos.view(B, 1, 1, 3)  # preserves the body position
    local_ref_body_pos = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), local_ref_body_pos.view(-1, 3))
    # local_ref_body_vel = ref_body_vel.view(B, time_steps, J, 3) 
    # local_ref_body_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), local_ref_body_vel.view(-1, 3))


    obs.append(local_ref_body_pos.view(B, time_steps, -1))  # timestep  * J * 3

    # print(obs[0].shape, obs[1].shape, obs[2].shape, obs[3].shape, obs[4].shape, obs[5].shape, obs[6].shape, obs[7].shape)
    obs = torch.cat(obs, dim=-1).view(B, -1)
    return obs
```

```python
def compute_imitation_observations_teleop_max(root_pos, root_rot, body_pos,   ref_body_pos, ref_body_vel, time_steps,  ref_episodic_offset = None, ref_vel_in_task_obs = True):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor,  int, bool, bool) -> Tensor
    #  Teleop version
    obs = []
    B, J, _ = body_pos.shape

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    
    ##### Body posi
```

### legged_gym/legged_gym/envs/base/legged_robot_config.py

```
class LeggedRobotCfg(BaseConfig)
class LeggedRobotCfgPPO(BaseConfig)
```

### legged_gym/legged_gym/envs/base/lpf.py

```
"""Two types of filters which can be applied to policy output sequences.

1. Simple exponential filter
2. Butterworth filter - lowpass or bandpass

The implementation of the butterworth filter follows scipy's lfilter
https://github.com/scipy/scipy/blob/v1.2.1/scipy/signal/signaltools.py

We re-implement the logic in order to explicitly manage the y states

The filter implements::
       a[0]*y[n] = b[0]*x[n] + b[1]*x[n-1] + ... + b[M]*x[n-M]
                             - a[1]*y[n-1] - ... - a[N]*y[n-N]

We assume M == N."""
class ActionFilter(object)
    """Implements a generic lowpass or bandpass action filter."""
    def __init__(self, a, b, order, num_joints, ftype)
    def reset(self)
    def filter(self, x)
    def init_history(self, x)
class ActionFilterButter(ActionFilter)
    """Butterworth filter."""
    def __init__(self, lowcut, highcut, sampling_rate, order, num_joints)
    def butter_filter(self, lowcut, highcut, fs, order)
    def reset_by_ids(self, action_ids)
class ActionFilterButterTorch(ActionFilterButter)
    """Utilizes pytorch for filtering. """
    def __init__(self, lowcut, highcut, sampling_rate, order, num_joints, device)
    def filter_old(self, x)
    def reset_old(self, action_ids)
    def filter(self, x)
    def reset_hist(self, action_ids)
class ActionFilterExp(ActionFilter)
    """Filter by way of simple exponential smoothing.

y = alpha * x + (1 - alpha) * previous_y"""
    def __init__(self, alpha, num_joints)
```

### legged_gym/legged_gym/envs/h1/h1_teleop_config.py

```
class H1TeleopCfg(LeggedRobotCfg)
class H1TeleopCfgPPO(LeggedRobotCfgPPO)
```

### legged_gym/legged_gym/scripts/train.py

```
def train(args)
```

### legged_gym/legged_gym/scripts/train_hydra.py

```
def train(cfg_hydra)
```

### legged_gym/legged_gym/utils/task_registry.py

```
class TaskRegistry()
    def __init__(self)
    def register(self, name, task_class, env_cfg, train_cfg)
    def get_task_class(self, name)
    def get_cfgs(self, name)
    def make_env(self, name, args, env_cfg)
    def make_env_hydra(self, name, hydra_cfg, env_cfg)
    def make_alg_runner(self, env, name, args, train_cfg, log_root)
```

### phc/phc/env/tasks/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors)
    def create_viewer(self)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions)
    def get_states(self)
    def _clear_recorded_states(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def setup_video_client(self)
    def setup_talk_client(self)
    def talk(self)
    def video_stream(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def _physics_step(self)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### phc/phc/env/tasks/humanoid.py

```
class Humanoid(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _load_proj_asset(self)
    def _build_proj(self, env_id, env_ptr)
    def _setup_tensors(self)
    def load_humanoid_configs(self, cfg)
    def load_common_humanoid_configs(self, cfg)
    def load_smpl_configs(self, cfg)
    def load_h1_configs(self, cfg)
    def _clear_recorded_states(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def get_obs_size(self)
    def get_running_mean_size(self)
    def get_self_obs_size(self)
    def get_action_size(self)
    def get_dof_action_size(self)
    def get_num_actors_per_env(self)
    def create_sim(self)
    def reset(self, env_ids)
    def change_char_color(self)
    def sample_char_color(self, cols, env_ids)
    def set_char_color(self, col, env_ids)
    def _reset_envs(self, env_ids)
    def _reset_env_tensors(self, env_ids)
    def _create_ground_plane(self)
    def _setup_character_props(self, key_bodies)
    def _build_termination_heights(self)
    def _create_smpl_humanoid_xml(self, num_humanoids, smpl_robot, queue, pid)
    def _load_amass_gender_betas(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_pd_action_offset_scale(self)
    def _compute_reward(self, actions)
    def _compute_reset(self)
    def _refresh_sim_tensors(self)
    def _compute_observations(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _reset_actors(self, env_ids)
    def pre_physics_step(self, actions)
    def _init_tensor_history(self, env_ids)
    def _update_tensor_history(self)
    def post_physics_step(self)
    def render(self, sync_frame_time)
    def _build_key_body_ids_tensor(self, key_body_names)
    def _build_key_body_ids_orig_tensor(self, key_body_names)
    def _build_contact_body_ids_tensor(self, contact_body_names)
    def _action_to_pd_targets(self, action)
    def _init_camera(self)
    def _update_camera(self)
    def _update_debug_viz(self)
def dof_to_obs_smpl(pose)
def dof_to_obs(pose, dof_obs_size, dof_offsets)
def compute_humanoid_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets)
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs)
def compute_humanoid_reward(obs_buf)
def compute_humanoid_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, max_episode_length, enable_early_termination, termination_heights)
def remove_base_rot(quat)
def compute_humanoid_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, dof_obs_size, dof_offsets, smpl_params, local_root_obs, root_height_obs, upright, has_smpl_params)
def compute_humanoid_observations_smpl_max(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params)
def compute_humanoid_observations_smpl_max_v2(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params, time_steps)
def compute_humanoid_observations_smpl_v3(body_pos, body_rot, root_vel, root_ang_vel, dof_pos, dof_vel, local_root_obs, root_height_obs)

```python
def compute_humanoid_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, int, List[int]) -> Tensor
    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)

    obs = torch.cat((root_h_obs, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def compute_humanoid_observations_max(body_pos, body_rot, body_vel, body_ang_vel, local_root_obs, root_height_obs):
    # type: (Tensor, Tensor, Tensor, Tensor, bool, bool) -> Tensor
    root_pos = body_pos[:, 0, :]
    root_rot = body_rot[:, 0, :]

    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, body_pos.shape[1], 1))
    flat_heading_rot = heading_rot_expand.reshape(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])

    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:]  # remove root pos

    flat_body_rot = body_rot.reshape(body_rot.shape[0] * body_rot.shape[1], body_rot.shape[2])  # global body rotation
    flat_local_body_rot = quat_mul(flat_heading_rot, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_rot_obs = flat_local_body_rot_obs.reshape(body_rot.shape[0], body_rot.shape[1] * flat_local_body_rot_obs.shape[1])

    if (local_root_obs):
        root_rot_obs = torch_utils.quat_to_tan_norm(root_rot)
        local_body_rot_obs[..., 0:6] = root_rot_obs

    flat_body_vel = body_vel.reshape(body_vel.shape[0] * body_vel.shape[1], body_vel.shape[2])
    flat_local_body_vel = torch_utils.my_quat_rotate(flat_heading_rot, flat_body_vel)
    local_body_vel = flat_local_body_vel.reshape(body_vel.shape[0], body_vel.shape[1] * body_vel.shape[2])

    flat_body_ang_vel = body_ang_vel.reshape(body_ang_vel.shape[0] * body_ang_vel.shape[1], body_ang_vel.shape[2])
    flat_local_body_ang_vel = torch_utils.my_quat_rotate(flat_heading_rot, flat_body_ang_vel)
    local_body_ang_vel = flat_local_body_ang_vel.reshape(body_ang_vel.shape[0], body_ang_vel.shape[1] * body_ang_vel.shape[2])

    obs = torch.cat((root_h_obs, local_body_pos, local_body_rot_obs, local_body_vel, local_body_ang_vel), dim=-1)
    return obs
```

```python
def compute_humanoid_reward(obs_buf):
    # type: (Tensor) -> Tensor
    reward = torch.ones_like(obs_buf[:, 0])
    return reward
```

```python
def compute_humanoid_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, dof_obs_size, dof_offsets, smpl_params, local_root_obs, root_height_obs, upright, has_smpl_params):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, int, List[int], Tensor, bool, bool,bool, bool) -> Tensor
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)

    obs_list = []
    if root_height_obs:
        obs_list.append(root_h_obs)
    obs_list += [
        root_rot_obs,
        local_root_vel,
        local_root_ang_vel,
        dof_obs,
        dof_vel,
        flat_local_key_pos,
    ]
    if has_smpl_params:
        obs_list.append(smpl_params)
    obs = torch.cat(obs_list, dim=-1)

    return obs
```

```python
def compute_humanoid_observations_smpl_max(body_pos, body_rot, body_vel, body_ang_vel, smpl_params, limb_weight_params, local_root_obs, root_height_obs, upright, has_smpl_params, has_limb_weight_params):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool) -> Tensor
    root_pos = body_pos[:, 0, :]
    root_rot = body_rot[:, 0, :]

    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    heading_rot_inv_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_inv_expand = heading_rot_inv_expand.repeat((1, body_pos.shape[1], 1))
    flat_heading_rot_inv = heading_rot_inv_expand.reshape(heading_rot_inv_expand.shape[0] * heading_rot_inv_expand.shape[1], heading_rot_inv_expand.shape[2])

    root_pos_expand = root_pos.unsqueeze(-2)
    local_body_pos = body_pos - root_pos_expand
    flat_local_body_pos = local_body_pos.reshape(local_body_pos.shape[0] * local_body_pos.shape[1], local_body_pos.shape[2])
    flat_local_body_pos = torch_utils.my_quat_rotate(flat_heading_rot_inv, flat_local_body_pos)
    local_body_pos = flat_local_body_pos.reshape(local_body_pos.shape[0], local_body_pos.shape[1] * local_body_pos.shape[2])
    local_body_pos = local_body_pos[..., 3:]  # remove root pos

    flat_body_rot = body_rot.reshape(body_rot.shape[0] * body_rot.shape[1], body_rot.shape[2])  # This is global rotation of the body
    flat_local_body_rot = quat_mul(flat_heading_rot_inv, flat_body_rot)
    flat_local_body_rot_obs = torch_utils.quat_to_tan_norm(flat_local_body_rot)
    local_body_rot_obs = flat_local_body_rot_obs.reshape(body_rot.shape[0], body_rot.shape[1] * flat_local_body_rot_obs.shape[1])

    if not (local_root_obs):
        root_rot_obs = torch_utils.quat_to_tan_norm(root_rot) # If not local root obs, you override it
```

### phc/phc/env/tasks/humanoid_amp.py

```
class HumanoidAMP(Humanoid)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _compute_observations(self, env_ids)
    def resample_motions(self)
    def pre_physics_step(self, actions)
    def get_task_obs_size_detail(self)
    def post_physics_step(self)
    def get_num_amp_obs(self)
    def fetch_amp_obs_demo(self, num_samples)
    def build_amp_obs_demo_steps(self, motion_ids, motion_times0, num_steps)
    def build_amp_obs_demo(self, motion_ids, motion_times0)
    def _build_amp_obs_demo_buf(self, num_samples)
    def _setup_character_props(self, key_bodies)
    def _load_motion(self, motion_file)
    def _reset_envs(self, env_ids)
    def _reset_actors(self, env_ids)
    def _reset_default(self, env_ids)
    def _sample_time(self, motion_ids)
    def _get_fixed_smpl_state_from_motionlib(self, motion_ids, motion_times, curr_gender_betas)
    def _get_state_from_motionlib_cache(self, motion_ids, motion_times, offset)
    def _sample_ref_state(self, env_ids)
    def _reset_ref_state_init(self, env_ids)
    def _reset_hybrid_state_init(self, env_ids)
    def _compute_humanoid_obs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _init_amp_obs_default(self, env_ids)
    def _init_amp_obs_ref(self, env_ids, motion_ids, motion_times)
    def _set_env_state(self, env_ids, root_pos, root_rot, dof_pos, root_vel, root_ang_vel, dof_vel, rigid_body_pos, rigid_body_rot, rigid_body_vel, rigid_body_ang_vel)
    def _refresh_sim_tensors(self)
    def _update_hist_amp_obs(self, env_ids)
    def _compute_amp_observations(self, env_ids)
    def _compute_amp_observations_from_state(self, root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vels, smpl_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)
    def _hack_motion_sync(self)
    def _update_camera(self)
    def _hack_consistency_test(self)
    def _hack_output_motion(self)
    def get_num_enc_amp_obs(self)
    def fetch_amp_obs_demo_enc_pair(self, num_samples)
    def fetch_amp_obs_demo_pair(self, num_samples)
def build_amp_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets)
def build_amp_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)
def build_amp_observations_h1(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)
def build_amp_observations_smpl_v2(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vel, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright)

```python
def build_amp_observations(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, local_root_obs, root_height_obs, dof_obs_size, dof_offsets):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, int, List[int]) -> Tensor
    root_h = root_pos[:, 2:3]
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot, root_rot)
    else:
        root_rot_obs = root_rot
    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    if (not root_height_obs):
        root_h_obs = torch.zeros_like(root_h)
    else:
        root_h_obs = root_h

    local_root_vel = torch_utils.my_quat_rotate(heading_rot, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_to_obs(dof_pos, dof_obs_size, dof_offsets)
    obs = torch.cat((root_h_obs, root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos), dim=-1)
    return obs
```

```python
def build_amp_observations_smpl(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool, bool) -> Tensor
    B, N = root_pos.shape
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot_inv, root_rot)
    else:
        root_rot_obs = root_rot

    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    local_root_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    if has_dof_subset:
        dof_vel = dof_vel[:, dof_subset]
        dof_pos = dof_pos[:, dof_subset]
        
    dof_obs = dof_to_obs_smpl(dof_pos)
        
    obs_list = []
    if root_height_obs:
        obs_list.append(root_h)
    obs_list += [root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos]
    # 1? + 6 + 3 + 3 + 114 + 57 + 12
    if has_shape_obs_disc:
        obs_list.append(shape_params)
    if has_limb_weight_obs:
        obs_list.append(limb_weight_params)
    obs = torch.cat(obs_list, dim=-1)
    
    return obs
```

```python
def build_amp_observations_h1(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool, bool) -> Tensor
    B, N = root_pos.shape
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot_inv, root_rot)
    else:
        root_rot_obs = root_rot

    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    local_root_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_end_pos = local_key_body_pos.view(local_key_body_pos.shape[0] * local_key_body_pos.shape[1], local_key_body_pos.shape[2])
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, flat_end_pos)
    flat_local_key_pos = local_end_pos.view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])

    dof_obs = dof_pos
        
    obs_list = []
    if root_height_obs:
        obs_list.append(root_h)
    obs_list += [root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, flat_local_key_pos]
    # 1? + 6 + 3 + 3 + 114 + 57 + 12
    if has_shape_obs_disc:
        obs_list.append(shape_params)
    if has_limb_weight_obs:
        obs_list.append(limb_weight_params)
    obs = torch.cat(obs_list, dim=-1)
    
    return obs
```

```python
def build_amp_observations_smpl_v2(root_pos, root_rot, root_vel, root_ang_vel, dof_pos, dof_vel, key_body_pos, key_body_vel,  shape_params, limb_weight_params, dof_subset, local_root_obs, root_height_obs, has_dof_subset, has_shape_obs_disc, has_limb_weight_obs, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, bool, bool, bool, bool, bool, bool) -> Tensor
    B, N = root_pos.shape
    root_h = root_pos[:, 2:3]
    if not upright:
        root_rot = remove_base_rot(root_rot)
    heading_rot_inv = torch_utils.calc_heading_quat_inv(root_rot)

    if (local_root_obs):
        root_rot_obs = quat_mul(heading_rot_inv, root_rot)
    else:
        root_rot_obs = root_rot

    root_rot_obs = torch_utils.quat_to_tan_norm(root_rot_obs)

    local_root_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_vel)
    local_root_ang_vel = torch_utils.my_quat_rotate(heading_rot_inv, root_ang_vel)

    root_pos_expand = root_pos.unsqueeze(-2)
    local_key_body_pos = key_body_pos - root_pos_expand

    heading_rot_expand = heading_rot_inv.unsqueeze(-2)
    heading_rot_expand = heading_rot_expand.repeat((1, local_key_body_pos.shape[1], 1))
    flat_heading_rot = heading_rot_expand.view(heading_rot_expand.shape[0] * heading_rot_expand.shape[1], heading_rot_expand.shape[2])
    local_end_pos = torch_utils.my_quat_rotate(flat_heading_rot, local_key_body_pos.view(-1, 3)).view(local_key_body_pos.shape[0], local_key_body_pos.shape[1] * local_key_body_pos.shape[2])
    
    local_vel = torch_utils.my_quat_rotate(flat_heading_rot, key_body_vel.view(-1, 3)).view(key_body_vel.shape[0], key_body_vel.shape[1] * key_body_vel.shape[2])

    if has_dof_subset:
        dof_vel = dof_vel[:, dof_subset]
        dof_pos = dof_pos[:, dof_subset]

    dof_obs = dof_to_obs_smpl(dof_pos)
    obs_list = []
    if root_height_obs:
        obs_list.append(root_h)
    obs_list += [root_rot_obs, local_root_vel, local_root_ang_vel, dof_obs, dof_vel, local_end_pos, local_vel]
    # 1 + 6 + 3 + 3 + 114 + 57 + 12
    if has_shape_obs_disc:
        obs_list.append(shape_params)
    if has_limb_weight_obs:
        obs_list.append(limb_weight_params)
    obs = torch.cat(obs_list, dim=-1)
    
    return obs
```

```python
def _compute_observations(self, env_ids=None):
        if env_ids is None:
            env_ids = torch.arange(self.num_envs).to(self.device)
        obs = self._compute_humanoid_obs(env_ids)

                
        if self.obs_v == 2:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:self.past_track_steps].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            ob
```

### phc/phc/env/tasks/humanoid_amp_getup.py

```
class HumanoidAMPGetup(HumanoidAMP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def pre_physics_step(self, actions)
    def _generate_fall_states(self)
    def _reset_actors(self, env_ids)
    def _reset_recovery_episode(self, env_ids)
    def _reset_fall_episode(self, env_ids)
    def _reset_envs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _update_recovery_count(self)
    def _compute_reset(self)
```

### phc/phc/env/tasks/humanoid_amp_task.py

```
class HumanoidAMPTask(HumanoidAMP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def get_obs_size(self)
    def get_task_obs_size(self)
    def pre_physics_step(self, actions)
    def render(self, sync_frame_time)
    def _update_task(self)
    def _reset_envs(self, env_ids)
    def _reset_task(self, env_ids)
    def _compute_observations(self, env_ids)
    def _compute_task_obs(self, env_ids)
    def _compute_reward(self, actions)
    def _draw_task(self)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = torch.arange(self.num_envs).to(self.device)
        humanoid_obs = self._compute_humanoid_obs(env_ids)

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs(env_ids)
            obs = torch.cat([humanoid_obs, task_obs], dim=-1)
        else:
            obs = humanoid_obs
        
                
        if self.obs_v == 2:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:self.past_track_steps].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            obs_slice[zeros] = torch.tile(obs[zeros], (1, self.past_track_steps))
            obs_slice[nonzero] = torch.cat([obs_slice[nonzero, N:], obs[nonzero]], dim=-1)
            self.obs_buf[env_ids] = obs_slice
        else:
            self.obs_buf[env_ids] = obs

        return
```

```python
def _compute_reward(self, actions):
        return NotImplemented
```
```

### phc/phc/env/tasks/humanoid_im.py

```
class HumanoidIm(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def pause_func(self, action)
    def next_func(self, action)
    def reset_func(self, action)
    def record_func(self, action)
    def hide_ref(self, action)
    def create_o3d_viewer(self)
    def _physics_step(self)
    def render(self, sync_frame_time, i)
    def _load_motion(self, motion_train_file, motion_test_file)
    def resample_motions(self)
    def get_motion_lengths(self)
    def _record_states(self)
    def _write_states_to_file(self, file_name)
    def begin_seq_motion_samples(self)
    def forward_motion_samples(self)
    def get_task_obs_size(self)
    def get_task_obs_size_detail(self)
    def _build_termination_heights(self)
    def init_root_points(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _load_marker_asset(self)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _update_marker(self)
    def _build_marker(self, env_id, env_ptr)
    def _build_marker_state_tensors(self)
    def _sample_time(self, motion_ids)
    def _reset_task(self, env_ids)
    def post_physics_step(self)
    def _compute_observations(self, env_ids)
    def _compute_task_obs(self, env_ids, save_buffer)
    def _compute_reward(self, actions)
    def _reset_ref_state_init(self, env_ids)
    def _get_state_from_motionlib_cache(self, motion_ids, motion_times, offset)
    def _sample_ref_state(self, env_ids)
    def _hack_motion_sync(self)
    def _update_cycle_count(self)
    def _update_occl_training(self)
    def _action_to_pd_targets(self, action)
    def pre_physics_step(self, actions)
    def _compute_reset(self)
    def _draw_task(self)
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v2(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, dof_pos, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, ref_dof_pos, time_steps, upright)
def compute_imitation_observations_v3(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v6(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v7(root_pos, root_rot, body_pos, body_vel, ref_body_pos, ref_body_vel, time_steps, upright)
def compute_imitation_observations_v8(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright)
def compute_imitation_observations_v9(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_root_vel, ref_body_root_ang_vel, time_steps, upright)
def compute_imitation_observations_v10(root_pos, root_rot, body_pos, body_rot, root_vel, root_ang_vel, dof_pos, dof_vel, ref_body_pos, ref_body_rot, ref_root_vel, ref_root_ang_vel, ref_dof_pos, ref_dof_vel, time_steps)
def compute_imitation_reward(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, rwd_specs)
def compute_point_goal_reward(prev_dist, curr_dist)
def compute_location_reward(root_pos, tar_pos)
def compute_humanoid_im_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, ref_body_pos, pass_time, enable_early_termination, termination_distance, disableCollision, use_mean)
def compute_location_observations(root_pos, root_rot, target_pos, upright)
def compute_humanoid_traj_reset(reset_buf, progress_buf, contact_buf, contact_body_ids, rigid_body_pos, pass_time, enable_early_termination, termination_heights, disableCollision)

```python
def compute_imitation_observations(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, int, bool) -> Tensor
    # We do not use any dof in observation.
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))

    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis

    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    ##### Velocities
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_vel.view(B, 1, J, 3)
    diff_global_ang_vel = ref_body_ang_vel.view(B, time_steps, J, 3) - body_ang_vel.view(B, 1, J, 3)

    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    obs.append(diff_local_vel.view(B, -1))  # 3 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # 3 * 3

    obs = torch.cat(obs, dim=-1)
    return obs
```

```python
def compute_imitation_observations_v2(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, dof_pos, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, ref_dof_pos, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding dof
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))

    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis

    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    ##### Velocities
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_vel.view(B, 1, J, 3)
    diff_global_ang_vel = ref_body_ang_vel.view(B, time_steps, J, 3) - body_ang_vel.view(B, 1, J, 3)

    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_vel.view(-1, 3))
    diff_local_ang_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_ang_vel.view(-1, 3))
    obs.append(diff_local_vel.view(B, -1))  # 3 * 3
    obs.append(diff_local_ang_vel.view(B, -1))  # 3 * 3

    ##### Dof_pos diff
    diff_dof_pos = ref_dof_pos.view(B, time_steps, -1) - dof_pos.view(B, time_steps, -1)
    obs.append(diff_dof_pos.view(B, -1))  # 23 * 3

    obs = torch.cat(obs, dim=-1)
    return obs
```

```python
def compute_imitation_observations_v3(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor, int, bool) -> Tensor
    # No velocities
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)

    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))
    obs.append(diff_local_body_pos_flat.view(B, -1))  # 1 * 10 * 3 * 3

    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot).repeat_interleave(time_steps, 0).view(B, time_steps, J, 4))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    obs.append(torch_utils.quat_to_tan_norm(diff_local_body_rot_flat).view(B, -1))  #  1 * 10 * 3 * 6

    obs = torch.cat(obs, dim=-1)

    return obs
```

```python
def compute_imitation_observations_v6(root_pos, root_rot, body_pos, body_rot, body_vel, body_ang_vel, ref_body_pos, ref_body_rot, ref_body_vel, ref_body_ang_vel, time_steps, upright):
    # type: (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor,Tensor, Tensor,Tensor,Tensor, int, bool) -> Tensor
    # Adding pose information at the back
    # Future tracks in this obs will not contain future diffs.
    obs = []
    B, J, _ = body_pos.shape

    if not upright:
        root_rot = remove_base_rot(root_rot)

    heading_inv_rot = torch_utils.calc_heading_quat_inv(root_rot)
    heading_rot = torch_utils.calc_heading_quat(root_rot)
    heading_inv_rot_expand = heading_inv_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    heading_rot_expand = heading_rot.unsqueeze(-2).repeat((1, body_pos.shape[1], 1)).repeat_interleave(time_steps, 0)
    

    ##### Body position and rotation differences
    diff_global_body_pos = ref_body_pos.view(B, time_steps, J, 3) - body_pos.view(B, 1, J, 3)
    diff_local_body_pos_flat = torch_utils.my_quat_rotate(heading_inv_rot_expand.view(-1, 4), diff_global_body_pos.view(-1, 3))

    body_rot[:, None].repeat_interleave(time_steps, 1)
    diff_global_body_rot = torch_utils.quat_mul(ref_body_rot.view(B, time_steps, J, 4), torch_utils.quat_conjugate(body_rot[:, None].repeat_interleave(time_steps, 1)))
    diff_local_body_rot_flat = torch_utils.quat_mul(torch_utils.quat_mul(heading_inv_rot_expand.view(-1, 4), diff_global_body_rot.view(-1, 4)), heading_rot_expand.view(-1, 4))  # Need to be change of basis
    
    ##### linear and angular  Velocity differences
    diff_global_vel = ref_body_vel.view(B, time_steps, J, 3) - body_vel.view(B, 1, J, 3)
    diff_local_vel = torch_utils.my_quat_rotate(heading_inv_rot_expand.view
```

### phc/phc/env/tasks/humanoid_im_demo.py

```
class HumanoidImDemo(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def talk(self)
    def _update_marker(self)
    def _reset_ref_state_init(self, env_ids)
    def _compute_observations(self, env_ids)
    def _compute_task_obs_demo(self, env_ids)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = torch.arange(self.num_envs).to(self.device)

        self_obs = self._compute_humanoid_obs(env_ids)
        self.self_obs_buf[env_ids] = self_obs

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs_demo(env_ids)
            obs = torch.cat([self_obs, task_obs], dim=-1)
        else:
            obs = self_obs

        if self.obs_v == 4:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:10].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            obs_slice[zeros] = torch.tile(obs[zeros], (1, 5))
            obs_slice[nonzero] = torch.cat([obs_slice[nonzero, N:], obs[nonzero]], dim=-1)
            self.obs_buf[env_ids] = obs_slice
        else:
            self.obs_buf[env_ids] = obs
        return obs
```
```

### phc/phc/env/tasks/humanoid_im_getup.py

```
class HumanoidImGetup(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def update_getup_schedule(self, epoch_num, getup_udpate_epoch)
    def pre_physics_step(self, actions)
    def _generate_fall_states(self)
    def resample_motions(self)
    def _reset_actors(self, env_ids)
    def _reset_recovery_episode(self, env_ids)
    def _reset_fall_episode(self, env_ids)
    def _reset_envs(self, env_ids)
    def _init_amp_obs(self, env_ids)
    def _update_recovery_count(self)
    def _compute_reset(self)
```

### phc/phc/env/tasks/humanoid_im_mcp.py

```
class HumanoidImMCP(HumanoidIm)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def _setup_character_props(self, key_bodies)
    def get_task_obs_size_detail(self)
    def step(self, weights)
```

### phc/phc/env/tasks/humanoid_im_mcp_demo.py

```
class HumanoidImMCPDemo(HumanoidImMCP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def talk(self)
    def _update_marker(self)
    def _compute_observations(self, env_ids)
    def _compute_task_obs_demo(self, env_ids)
    def _compute_reset(self)

```python
def _compute_observations(self, env_ids=None):
        # env_ids is used for resetting
        if env_ids is None:
            env_ids = torch.arange(self.num_envs).to(self.device)

        self_obs = self._compute_humanoid_obs(env_ids)
        self.self_obs_buf[env_ids] = self_obs

        if (self._enable_task_obs):
            task_obs = self._compute_task_obs_demo(env_ids)
            obs = torch.cat([self_obs, task_obs], dim=-1)
        else:
            obs = self_obs

        if self.obs_v == 4:
            # Double sub will return a copy.
            B, N = obs.shape
            sums = self.obs_buf[env_ids, 0:10].abs().sum(dim=1)
            zeros = sums == 0
            nonzero = ~zeros
            obs_slice = self.obs_buf[env_ids]
            obs_slice[zeros] = torch.tile(obs[zeros], (1, 5))
            obs_slice[nonzero] = torch.cat([obs_slice[nonzero, N:], obs[nonzero]], dim=-1)
            self.obs_buf[env_ids] = obs_slice
        else:
            self.obs_buf[env_ids] = obs
        return obs
```
```

### phc/phc/env/tasks/humanoid_im_mcp_getup.py

```
class HumanoidImMCPGetup(HumanoidImGetup, HumanoidImMCP)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
```

### phc/phc/env/tasks/humanoid_speed.py

```
class HumanoidSpeed(HumanoidAMPTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless)
    def get_task_obs_size(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def _update_marker(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def _load_marker_asset(self)
    def _build_env(self, env_id, env_ptr, humanoid_asset)
    def _build_marker(self, env_id, env_ptr)
    def _build_marker_state_tensors(self)
    def _update_task(self)
    def _reset_task(self, env_ids)
    def _compute_flip_task_obs(self, normal_task_obs, env_ids)
    def _compute_task_obs(self, env_ids)
    def _compute_reward(self, actions)
    def _draw_task(self)
    def _reset_ref_state_init(self, env_ids)
    def _sample_ref_state(self, env_ids)
    def _hack_output_motion_target(self)
def compute_speed_observations(root_states, tar_speed)
def compute_speed_reward(root_pos, prev_root_pos, root_rot, tar_speed, dt)

```python
def compute_speed_observations(root_states, tar_speed):
    # type: (Tensor, Tensor) -> Tensor
    root_rot = root_states[:, 3:7]

    tar_dir3d = torch.zeros_like(root_states[..., 0:3])
    tar_dir3d[..., 0] = 1
    heading_rot = torch_utils.calc_heading_quat_inv(root_rot)
    
    local_tar_dir = torch_utils.my_quat_rotate(heading_rot, tar_dir3d)
    local_tar_dir = local_tar_dir[..., 0:2]
    tar_speed = tar_speed.unsqueeze(-1)
    
    obs = torch.cat([local_tar_dir, tar_speed], dim=-1)

    return obs
```

```python
def compute_speed_reward(root_pos, prev_root_pos, root_rot, tar_speed, dt):
    # type: (Tensor, Tensor, Tensor, Tensor, float) -> Tensor
    vel_err_scale = 0.25
    tangent_err_w = 0.1

    delta_root_pos = root_pos - prev_root_pos
    root_vel = delta_root_pos / dt
    tar_dir_speed = root_vel[..., 0]
    tangent_speed = root_vel[..., 1]

    tar_vel_err = tar_speed - tar_dir_speed
    tangent_vel_err = tangent_speed
    dir_reward = torch.exp(-vel_err_scale * (tar_vel_err * tar_vel_err +  tangent_err_w * tangent_vel_err * tangent_vel_err))

    reward = dir_reward

    return reward
```

```python
def _compute_reward(self, actions):
        root_pos = self._humanoid_root_states[..., 0:3]
        root_rot = self._humanoid_root_states[..., 3:7]
        
        # if False:
        if flags.test:
            root_pos = self._humanoid_root_states[..., 0:3]
            delta_root_pos = root_pos - self._prev_root_pos
            root_vel = delta_root_pos / self.dt
            tar_dir_speed = root_vel[..., 0]
            # print(self._tar_speed, tar_dir_speed)
        
        self.rew_buf[:] = self.reward_raw = compute_speed_reward(root_pos, self._prev_root_pos,  root_rot, self._tar_speed, self.dt)
        self.reward_raw = self.reward_raw[:, None]

        # if True:
        if self.power_reward:
            power_all = torch.abs(torch.multiply(self.dof_force_tensor, self._dof_vel))
            power = power_all.sum(dim=-1)
            power_reward = -self.power_coefficient * power
            power_reward[self.progress_buf <= 3] = 0 # First 3 frame power reward should not be counted. since they could be dropped.

            self.rew_buf[:] += power_reward
            self.reward_raw = torch.cat([self.reward_raw, power_reward[:, None]], dim=-1)

        # if True:
        if self.power_usage_reward: 
            power_all = torch.abs(torch.multiply(self.dof_force_tensor, self._dof_vel))
            power_all = power_all.reshape(-1, 23, 3)
            left_power = power_all[:, self.left_indexes].reshape(self.num_envs, -1).sum(dim = -1)
            right_power = power_all[:, self.right_indexes].reshape(self.num_envs, -1).sum(dim = -1)
            self.power_acc[:, 0] += left_power
            self.power_acc[:, 1] += right_power
            power_usage_reward = self.power_acc/(self.progress_buf + 1)[:, None]
            # print((power_usage_reward[:, 0] - power_usage_reward[:, 1]).abs())
            power_usage_reward = - self.power_usage_coefficient * (power_usage_reward[:, 0] - power_usage_reward[:, 1]).abs()
            power_usage_reward[self.progress_buf <= 3] = 0 # First 3 frame power reward should not be counted. since they could be dropped. on the ground to balance.
            
            self.rew_buf[:] += power_usage_reward
            self.reward_raw = torch.cat([self.reward_raw, power_usage_reward[:, None]], dim=-1)
            

        return
```
```

### phc/phc/env/tasks/vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations)
    def step(self, actions)
    def reset(self)
class VecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### phc/phc/env/tasks/vec_task_wrappers.py

```
class VecTaskCPUWrapper(VecTaskCPU)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations)
class VecTaskGPUWrapper(VecTaskGPU)
    def __init__(self, task, rl_device, clip_observations)
class VecTaskPythonWrapper(VecTaskPython)
    def __init__(self, task, rl_device, clip_observations)
    def reset(self, env_ids)
    def amp_observation_space(self)
    def enc_amp_observation_space(self)
    def fetch_amp_obs_demo(self, num_samples)
    def enc_amp_observation_space(self)
    def fetch_amp_obs_demo_pair(self, num_samples)
    def fetch_amp_obs_demo_enc_pair(self, num_samples)
    def fetch_amp_obs_demo_per_id(self, num_samples, motion_ids)

```python
def amp_observation_space(self):
        return self._amp_obs_space
```

```python
def enc_amp_observation_space(self):
        return self._enc_amp_obs_space
```

```python
def enc_amp_observation_space(self):
        return self._enc_amp_obs_space
```
```

### phc/phc/env/util/gym_util.py

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

### phc/phc/env/util/traj_generator.py

```
class TrajGenerator()
    def __init__(self, num_envs, episode_dur, num_verts, device, dtheta_max, speed_min, speed_max, accel_max, sharp_turn_prob)
    def reset(self, env_ids, init_pos)
    def input_new_trajs(self, env_ids)
    def get_num_verts(self)
    def get_num_segs(self)
    def get_num_envs(self)
    def get_traj_duration(self)
    def get_traj_verts(self, traj_id)
    def calc_pos(self, traj_ids, times)
    def mock_calc_pos(self, env_ids, traj_ids, times, query_value_gradient)
```

### phc/phc/utils/config.py

```
def set_np_formatting()
def warn_task_name()
def set_seed(seed, torch_deterministic)
def load_cfg(args)
def parse_sim_params(args, cfg, cfg_train)
def get_args(benchmark)
```

### phc/phc/utils/parse_task.py

```
def warn_task_name()
def parse_task(args, cfg, cfg_train, sim_params)
```

### rsl_rl/rsl_rl/env/vec_env.py

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

### rsl_rl/rsl_rl/runners/on_policy_runner.py

```
class OnPolicyRunner()
    def __init__(self, env, train_cfg, log_dir, device)
    def learn(self, num_learning_iterations, init_at_random_ep_len)
    def update_training_data(self, failed_keys)
    def eval(self)
    def run_eval_loop(self)
    def _post_step_eval(self, info, done)
    def log(self, locs, width, pad)
    def save(self, path, infos)
    def load(self, path, load_optimizer)
    def get_inference_policy(self, device)
```

### rsl_rl/rsl_rl/runners/on_policy_runner_cost.py

```
class OnPolicyRunnerCost()
    def __init__(self, env, train_cfg, log_dir, device)
    def learn(self, num_learning_iterations, init_at_random_ep_len)
    def log(self, locs, width, pad)
    def save(self, path, infos)
    def load(self, path, load_optimizer)
    def get_inference_policy(self, device)
```