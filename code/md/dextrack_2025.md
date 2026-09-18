# dextrack_2025

source: https://github.com/Meowuu7/DexTrack


commit: 1005fad6158c3fa0e4e8df01323de2f62d539f7a


## README

# DexTrack: Dexterous Manipulation Tracking

[Website](https://meowuu7.github.io/DexTrack/)  | [Videos](https://youtu.be/zru1Z-DaiWE)  | [OpenReview](https://openreview.net/forum?id=ajSmXqgS24&noteId=SBH6txdWH9) | [arXiv](https://arxiv.org/abs/2502.09614)


Implementation of our work [DexTrack](https://meowuu7.github.io/DexTrack/), capable of serving as an effective tool to 1) create dexterous robot hand-object manipulation demonstrations by mimicking kinematic references, and 2) develop a versatile tracking controller that can accomplish diverse manipulation tasks.
<!-- .  Track 1) can serve as an effective tool to create dexterous robot hand-object manipulation demonstrations (with actions) and 2) is also a promising way to develop a tracking controller capable of accomplishing diverse manipulation tasks.  -->
 <!-- presenting an RL-based tracking control scheme for dexterous manipulations. It is a) an effective tool to create dexterous robot hand-object manipulation data with actions and b) a promising strategy to develop a generalizable and versatile neural controller for dexterous manipulation with a unified tracking scheme. -->

<!-- https://github.com/user-attachments/assets/1222fc51-42c9-4fd2-86cf-029b9c9c24ab  -->




https://github.com/user-attachments/assets/13ddaac9-7098-435d-8b52-7517e1e95419


<!-- 

DexTrack supports the following applications:
- Converting kinematic-only human-object manipulation trajectories into dynamics-aware robot hand action trajectories, enabling the robot to interact with the object while closely mimicking the corresponding kinematic states.

- Converting kinematic-only human-object manipulation trajectories to dynamics-aware dexterous robot hand action trajectories, driving the robot hand to interact with the object with the resulting states closely mimicking the corresponding kinematic references. 
- Developing a generalizable and versatile neural controller for dexterous manipulation. Unifiying manipulaton tasks into a general *tracking control* scheme and training to track abundant trajectories with diverse *tracking commands*, DexTrack can develop a tracking controller that can solve a wide range of manipulation tasks with nice generalization ability.  -->


## Getting Started

### Installation

Create a vritual environment with python 3.8.0:
```bash
conda create -n dextrack python=3.8.0
conda activate dextrack
```

Download the Isaac Gym Preview 4 release from the [website](https://developer.nvidia.com/isaac-gym). 
<!-- then -->
<!-- follow the installation instructions in the documentation. -->
```bash
cd isaacgym/python
pip install -e .
```

Install `torch_cluster`:
```bash
cd DexTrack/whls
pip install torch_cluster-1.6.3+pt24cu121-cp38-cp38-linux_x86_64.whl
```

Install other dependencies:
```bash
pip install rl_games transforms3d matplotlib omegaconf hydra-core trimesh mujoco tqdm
```

### Data

Download the retargeted data from [this link](https://1drv.ms/f/c/c746413ba7b58f04/EmTCrn1XSShNn34d3mTr7b4BBk1W4yqJxjY1y3WN0KRm3A?e=dxXnuT). Extract `.zip` files in the folder `isaacgymenvs/data`. 

Download the first part of object files from [this link](https://1drv.ms/u/c/c746413ba7b58f04/EVEQ8nNWsnROk5swNPIcqR8Bfq6eb716MFJTbkMneJEvew?e=1JbI7k). Extract this file in the folder `assets`. 

Download the second part of object files from [this link](https://1drv.ms/u/c/c746413ba7b58f04/Ed7YUar7_0lAvf9B8YQCZC0BEuaSr_5oSO65qR18RwBNvw?e=QC48Nn).  Extract this file in the folder `assets/rsc`. 

Download the third part of object files from [this link](https://1drv.ms/u/c/c746413ba7b58f04/EWEaowIuf7BMrL2NMSBXzM4BoXxjsc9HUp7wm36aLjdC5A?e=ccINfB).  Extract this file in the folder `assets`. 

(Optional) Download checkpoints from [this link](https://1drv.ms/u/c/c746413ba7b58f04/ERogbFMZSPZFs7tFY2Lz3iMBRbwt6PphW4qsqFDhhCTwuQ?e=O2Yep8). Extract it in the folder `isaacgymenvs/`. 

File structure:
```bash
isaacgymenvs/
  data/
    GRAB_Tracking_PK_reduced_300/
    GRAB_Tracking_PK_LEAP_OFFSET_0d4_0d5_warm_v2_v2urdf/
    modified_kinematics_data_leap_wfranka_v15urdf/
    TACO_Tracking_PK_reduced/
  ckpts/
    ...
assets/
  datasetv4.1/
  meshdatav3_scaled/
  rsc/
    objs/
```

### Kinematic Retargeting

Code uploaded [here](https://drive.google.com/file/d/18Zbl7mNaxV9CnLos_tM6CalyvB3sE1ce/view?usp=sharing). The retargeting pipeline used in both DexTrack and QuasiSim is based on keypoint-based retargeting. For a new robot hand, the user needs to manually define corresponding keypoints between the robot hand and the MANO hand. For Leap and Allegro, the selected keypoint indices are hardcoded in the implementation. The code is somewhat messy. The main entry script is `exp_runner_stage_1.py`.

<!-- We've also included code for kinematic retargeting in this repo. Please refer to []() for detailed usage.  -->


## Usage

<!-- Dexterous Manipulation Tracking - Usage -->


This repository includes RL environments, along with the training and evaluation procedures, for the dexterous manipulation tracking problem.
 <!-- using a simulated fly Allegro hand (6 global translational and rotational DoFs).  -->
We support 1) a fly Allegro hand (an Allegro hand with 6 global translational and rotational DoFs) and 2) a LEAP hand mounted on a Franka Panda arm.
Two control strategies (action spaces) are implemented:
- Cumulated residual positional targets with kinematic bias; 
- Relative positional targets. 
The original implementation uses the first action space. 

 <!-- with a simulated fly Allegro hand (an Allegro hand with 6 global translational and rotational DoFs). We support two types of control strategies (action spaces):
- Cumulated residual positional targets with kinematics bias; 
- Relative positional targets. 
The original DexTrack's implementation uses the first action space.  -->

DexTrack include two levels of tracking: 
- **Single trajectory tracking:** The goal is to train a trajectory-specific policy to follow a single manipulation trajectory.
- **Multiple trajectories tracking:** The goal is to train a generalizable tracking policy capable of mimicking multiple manipulation trajectories and generalizing to unseen sequences.
<!-- for a generalizable and versatile tracker. The goal is training a single tracking policy that is able to track multiple manipulation trajectories, and has the ability to generalize to unobserved sequences.  -->
<!-- In the following, we will illustrate the training and evaluation processes for these two settings. -->
Below, we will outline the training and evaluation processes for both settings.

Please ensure that you are running these commands in the `DexTrack/isaacgymenvs` folder. 

### Sincle trajectory tracking (fly Allegro hand)

**GRAB Dataset**



To train a single trajectory tracker for a sequence retargeted from the **GRAB** dataset using the `cumulative residual` action space, run the following code:
```bash
bash scripts/run_tracking_headless_grab_single.sh <GPU_ID> <SEQ_NAME>
```
Please replace `<GPU_ID>` with the index of the GPU you wish to use. Only single-GPU training is supported. For other arguments, replace `<SEQ_NAME>` with the name of the sequence you wish to track. Checkpoints will be saved in the `./logs` folder.

<!-- Please replace `<GPU_ID>` with the index of the card you wish to run the code on. We only support single gpu training. Similarly, `<SEQ_NAME>` should be replaced by the name of the sequence you wish to track. Checkpoints will be saved in the folder `./logs`.  -->

Once you have obtained a checkpoint with a satisfactory reward, run the following code to evaluate it. A display is required if `HEADLESS` is set to `False`.
<!-- After you've obtained a checkpoint with a satisfactory reward, run the following code to evaluate it. You need a display if setting `HEADLESS` to `False`.  -->
<!-- Please note that the evaluation code is not running in a headless mode (you need a display). -->
```bash
bash scripts/run_tracking_headless_grab_single_test.sh <GPU_ID> <SEQ_NAME> <CKPT> <HEADLESS>
```

<!-- To train a single trajectory tracker for a sequence retargeted from the **GRAB** dataset using the `relative positional` action space, run the following code: -->
To train a single-trajectory tracker for a sequence retargeted from the **GRAB** dataset using the `relative positional` action space, run the following code:
```bash
bash scripts/run_tracking_headless_grab_single_ctlv2.sh <GPU_ID> <SEQ_NAME>
```
Similarly, after you've obtained a good checkpoint, run the following code to evaluate it. 
```bash
bash scripts/run_tracking_headless_grab_single_test_ctlv2.sh <GPU_ID> <SEQ_NAME> <CKPT> <HEADLESS>
```


<!-- For sequences retargeted from TACO dataset, to track a trajectory with tag `<TAG>` using the `cumulative residual` action space, run the following code:
```bash
bash scripts/run_tracking_headless_taco_single.sh <GPU_ID> <TAG>
```
Similarly, after you've obtained a satisfactory checkpoint, run the following code to evaluate it. 
```bash
bash scripts/run_tracking_headless_taco_single_test.sh <GPU_ID> <TAG> <CKPT>
``` -->



Below, we provide several examples. 

The following videos illustrate their corresponding input (kinematic references retargeted from human-object manipulation trajectories) and output (tracking results) that can be achieved. 

<!-- These are their input (kinematic references retargeted from human-object manipulation trajectories) and output (tracking results) that we can achieve.  -->



|   |    Cube       |       Duck          |     Flute        |      
| :----------------------: | :----------------------: | :---------------------: | :---------------------: | 
| Kinematic References  |     ![](assets/static/cubesmall_inspect_kines.gif)        |       ![](assets/static/duck_inspect_kines.gif)         |      ![](assets/static/flute_pass_kines.gif)         |   
| Tracking Result | ![](assets/static/cubesmall_inspect_tracked.gif) | ![](assets/static/duck_inspect_tracked.gif) | ![](assets/static/flute_pass_tracked.gif) |

Please refer to the following instructions to reproduce the above tracking examples.


***Case 1: Cubesmall inspect***

To track the `cubesmall_inspect` trajectory from subject `s2` on `GPU 0`, whose corresponding sequence name is `ori_grab_s2_cubesmall_inspect_1`, please run:
```bash
bash scripts/run_tracking_headless_grab_single.sh 0 ori_grab_s2_cubesmall_inspect_1
```
This sequence can be tracked pretty well using quite short time. We can reach a reward more than `150` at epoch `50` using `22000` parallel environments. 

Our pre-trained weights can be downloaded form [](). Following instructions stated above and extract these files in the folder `./ckpts`, you can run the test code using our trained policy for this sequence using the following command:
```bash
bash scripts/run_tracking_headless_grab_single_test.sh 0 ori_grab_s2_cubesmall_inspect_1 ./ckpts/s2_cubesmall_inspect_ckpt.pth False 
```

***Case 2: Duck inspect***

To track the `duck_inspect` trajectory from subject `s2` on `GPU 0`, whose corresponding sequence name is `ori_grab_s2_duck_inspect_1`, please run:
```bash
bash scripts/run_tracking_headless_grab_single.sh 0 ori_grab_s2_duck_inspect_1
```
This sequence can also be tracked pretty well after training for a short time. We can reach a reward more than `150` at epoch `100` using `22000` parallel environments. 

Similarly, our pretrained policy for this sequence can be evaluated using the following command:
```bash
bash scripts/run_tracking_headless_grab_single_test.sh 0 ori_grab_s2_duck_inspect_1 ./ckpts/s2_duck_inspect_ckpt.pth False
```


***Case 3: Flute pass***

To track the `flute_pass` trajectory from subject `s2` on `GPU 0`, whose corresponding sequence name is `ori_grab_s2_flute_pass_1`, please run:
```bash
bash scripts/run_tracking_headless_grab_single.sh 0 ori_grab_s2_flute_pass_1
``` 
Our pretrained policy for this sequence can be evaluated using the following command:
```bash
bash scripts/run_tracking_headless_grab_single_test.sh 0 ori_grab_s2_flute_pass_1 ./ckpts/s2_flute_pass_ckpt.pth False
```




**TACO Dataset**

For sequences retargeted from **TACO** dataset, to track a trajectory with tag `<TAG>` using the `cumulative residual` action space, run the following code:
```bash
bash scripts/run_tracking_headless_taco_single.sh <GPU_ID> <TAG>
```
Similarly, after you've obtained a satisfactory checkpoint, run the following code to evaluate it. 
```bash
bash scripts/run_tracking_headless_taco_single_test.sh <GPU_ID> <TAG> <CKPT> <HEADLESS>
```



Below, we provide several examples. 

The following videos illustrate their corresponding input (kinematic references retargeted from human-object manipulation trajectories) and output (tracking results) that can be achieved. 

|   |    Shovel       |       Ladle         |     Soap        |      
| :----------------------: | :----------------------: | :---------------------: | :---------------------: | 
| Kinematic References  |     ![](assets/static/taco_1_kines.gif)        |       ![](assets/static/taco_2_kines.gif)         |      ![](assets/static/taco_3_kines.gif)         |   
| Tracking Result | ![](assets/static/taco_1_tracked.gif) | ![](assets/static/taco_2_tracked.gif) | ![](assets/static/taco_3_tracked.gif) |


***Case 1: Tool-using sequence (shovel) from TACO***

To track the tool using sequence from TACO dataset tagged with `taco_20231104_169` on `GPU 0`, run the following code
```bash
bash scripts/run_tracking_headless_taco_single.sh 0 taco_20231104_169
```
In our test, we can get nice result after 300 epochs training. To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_taco_single_test.sh 0 taco_20231104_169 ./ckpts/taco_1_ckpt.pth False 
```


***Case 2: Tool-using sequence (ladle) from TACO***

To track the tool using sequence from TACO dataset tagged with `taco_20231104_186` on `GPU 0`, run the following code
```bash
bash scripts/run_tracking_headless_taco_single.sh 0 taco_20231104_186
```
To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_taco_single_test.sh 0 taco_20231104_186 ./ckpts/taco_2_ckpt.pth False
```


***Case 3: Tool-using sequence (soap) from TACO***

To track the tool using sequence from TACO dataset tagged with `taco_20231103_073` on `GPU 0`, run the following code
```bash
bash scripts/run_tracking_headless_taco_single.sh 0 taco_20231103_073
```
To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_taco_single_test.sh 0 taco_20231103_073 ./ckpts/taco_3_ckpt.pth False
```





### Multiple trajectory tracking (fly Allegro hand)

**GRAB Dataset**


To train a multiple trajectories tracker for sequences retargeted from the **GRAB** dataset using the `cumulative residual` action space, run the following code:
```bash
bash scripts/run_tracking_headless_grab_multiple.sh <GPU_ID> <SUBJ_NM> <SEQ_TAG_LIST>
```
Please replace `<GPU_ID>` with the index of the card you wish to run the code on. `<SEQ_TAG_LIST>` is the file specifying trajectories to track. 

For instance, to train a neural controller that can track all manipulation trajectories with the object `duck`, run the following command:
```bash
bash scripts/run_tracking_headless_grab_multiple.sh 0 '' ../assets/inst_tag_list_obj_duck.npy
```

For all trajectories in the GRAB's training split (trajectories from `s2` to `s10`), run:
```bash
bash scripts/run_tracking_headless_grab_multiple.sh 0 '' ''
```

<!-- Our pretrained checkpoint is `./ckpts/grab_duck_ckpt.pth`.  -->
<!-- The pretraiend policy for all trajectories in the GRAB's training split (trajectories from `s2` to `s10`) is `./ckpts/grab_trajs_tracking_ckpt.pth`.  -->
Run the following command to evaluate a checkpoint: 
```bash
bash scripts/run_tracking_headless_grab_multiple_test.sh <GPU_ID> <SEQ_NM> <CKPT> <HEADLESS> 
```

<!-- The pretraiend policy for all trajectories in the GRAB's training split (trajectories from `s2` to `s10`) is `./ckpts/grab_trajs_tracking_ckpt.pth`.  -->


Similarly, to train a multiple trajectory tracker for a sequence retargeted from **GRAB** dataset using the `relative target` action space, run the following code:
```bash
bash scripts/run_tracking_headless_grab_multiple_ctlv2.sh <GPU_ID> <SUBJ_NM> <SEQ_TAG_LIST>
```
Running the following command for evaluation:
```bash
bash scripts/run_tracking_headless_grab_multiple_test_ctlv2.sh <GPU_ID> <TAG> <CKPT> <HEADLESS> 
```

### Single trajectory tracking (LEAP hand with Franka arm)


To train a tracking policy for a sequence retargeted from the **GRAB** dataset using the `relative positional` action space, run the following code:
```bash
bash scripts/run_tracking_headless_grab_single_wfranka.sh <GPU_ID> <TAG>
```
For testing: 
```bash
 bash scripts/run_tracking_headless_grab_single_wfranka_test.sh <GPU_ID> <TAG> <CKPT> <HEADLESS>
```

In additional to trajectories contained in the original GRAB dataset, we've synthesized more trajectories with in-hand reorientations. Please refer to `data/modified_kinematics_data_leap_wfranka_v15urdf` for their kinematic motions (the in-hand reorienntation stage contains only object motion variations with hand pose fixed). To train a tracking policy for a synthesized trajectory, run the following code:
```bash
bash scripts/run_tracking_headless_grab_single_syntraj_wfranka.sh <GPU_ID> <TAG> <SAMPLE_ID>
```
`<SAMPLE_ID>` should be replaced by a integer ranging from `0` to `99`. 
For test:
```bash
bash scripts/run_tracking_headless_grab_single_syntraj_wfranka.sh <GPU_ID> <TAG> <SAMPLE_ID> <CKPT> <HEADLESS>
```

Below, we give several examples. 

Their corresponding input and output are illustrated in the following videos: 

|   |    Elephant       |       Hammer         |     Watch        |      
| :----------------------: | :----------------------: | :---------------------: | :---------------------: | 
| Kinematic References  |     ![](assets/static/elephant_inspect_kines.gif)        |       ![](assets/static/hammer_rt_kines.gif)         |      ![](assets/static/watch_set_kines.gif)         |   
| Tracking Result | ![](assets/static/elephant_inspect_tracked.gif) | ![](assets/static/hammer_rt_tracked.gif) | ![](assets/static/watch_set_tracked.gif) |


***Case 1: Elephant***

For training, run the following code
```bash
bash scripts/run_tracking_headless_grab_single_wfranka.sh 0 ori_grab_s2_elephant_inspect_1
```
To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_grab_single_wfranka_test.sh 0 ori_grab_s2_elephant_inspect_1 ./ckpts/elephant_inspect_wfranka_ckpt.pth False
```


***Case 2: Hammer***

For training, run the following code
```bash
bash scripts/run_tracking_headless_grab_single_syntraj_wfranka.sh 0 ori_grab_s2_hammer_use_2 6
```
To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_grab_single_syntraj_wfranka.sh 0 ori_grab_s2_hammer_use_2 6 ./ckpts/hammer_reorient_sample_6_ckpt.pth False
```



***Case 3: Watch***

For training, run the following code
```bash
bash scripts/run_tracking_headless_grab_single_wfranka.sh 0 s1_watch_set_2
```
To evaluate our pretrained policy, run the following comamnd:
```bash
bash scripts/run_tracking_headless_grab_single_wfranka_test.sh 0 ori_grab_s1_watch_set_2 ./ckpts/watch_set_ckpt.pth False 
```




### Multiple trajectories tracking (LEAP with Franka arm)

Similar to the fly hand setting, run the following command to train a tracking controller for sequences retargeted from the `GRAB` dataset:
```bash
bash scripts/run_tracking_headless_grab_multiple_wfranka.sh <GPU_ID> <SEQ_TAG_LIST>
```
For evaluation:
```bash
bash scripts/run_tracking_headless_grab_multiple_wfranka_test.sh <GPU_ID> <TAG> <CKPT> <HEADLESS>
```

<!-- We've included pre-trained checkpoints for `s4` and `s6` in the `./ckpts` folder (`leap_franka_grab_s${idx}_ckpt.pth`).  -->


**Notice**: In addition to the single and multiple trajectory tracking processes included above, DexTrack incorporates two key components that make the specialist-generalist iterative training framework work: 1) homotopy optimization for enhancing single trajectory tracking (applicable only to policies using the `cumulative residual` action space), and 2) a combination of IL and RL to improve the generalist tracker. However, these components require significant human effort and cannot easily be condensed into a single script. Besides, the corresponding code and scripts are too messy to be cleaned within an acceptable time frame. As a result, we do not currently plan to release them publicly.




## Contact

Please contact xymeow7@gmail.com or create a github issue if you have any questions.

<!-- ## Bibtex

If you find this code useful in your research, please cite: -->

<!-- ```bibtex
@inproceedings{liu2025,
   title={GeneOH Diffusion: Towards Generalizable Hand-Object Interaction Denoising via Denoising Diffusion},
   author={Liu, Xueyi and Yi, Li},
   booktitle={The Twelfth International Conference on Learning Representations},
   year={2024}
}
``` -->


## Acknowledgments

This code is standing on the shoulders of giants. We want to thank the following contributors that our code is based on: [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs/tree/main) and [UniDexGrasp](https://github.com/PKU-EPIC/UniDexGrasp). 


## License

See [LICENSE](LICENSE.txt).


<!-- you can run the test code using our trained policy for this sequence using the following command: -->








## File tree (depth 3, assets pruned)

```
.gitignore
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
    a2c_dagger_continuous.py
    a2c_fromsupervised.py
    a2c_supervised.py
    a2c_supervised_deterministic.py
    a2c_supervised_player.py
    a2c_supervised_v1.py
    a2c_supervised_wplanning.py
    a2c_supervised_wplanning_player.py
    amp_continuous.py
    amp_continuous_dagger.py
    amp_datasets.py
    amp_models.py
    amp_network_builder.py
    amp_players.py
    common_agent.py
    common_player.py
    detr_vae.py
    hrl_continuous.py
    hrl_models.py
    old/
    replay_buffer.py
    storage.py
    transformer_layers.py
    visionppo_models.py
    visionppo_network_builder.py
  pbt/
    __init__.py
    experiments/
    launcher/
    mutation.py
    pbt.py
  poselib/
    README.md
    fbx_importer.py
    generate_amp_humanoid_tpose.py
    mjcf_importer.py
    poselib/
    retarget_motion.py
  scripts/
    run_tracking_headless_grab_multiple.sh
    run_tracking_headless_grab_multiple_ctlv2.sh
    run_tracking_headless_grab_multiple_test.sh
    run_tracking_headless_grab_multiple_test_ctlv2.sh
    run_tracking_headless_grab_multiple_wfranka.sh
    run_tracking_headless_grab_multiple_wfranka_test.sh
    run_tracking_headless_grab_single.sh
    run_tracking_headless_grab_single_ctlv2.sh
    run_tracking_headless_grab_single_syntraj_wfranka.sh
    run_tracking_headless_grab_single_syntraj_wfranka_test.sh
    run_tracking_headless_grab_single_test.sh
    run_tracking_headless_grab_single_test_ctlv2.sh
    run_tracking_headless_grab_single_wfranka.sh
    run_tracking_headless_grab_single_wfranka_test.sh
    run_tracking_headless_taco_single.sh
    run_tracking_headless_taco_single_test.sh
  tasks/
    __init__.py
    allegro_hand_tracking_generalist.py
    ant.py
    vec_task.py
  test_generalist_pool.py
  test_pool.py
  train.py
  train_2.py
  train_pool_2.py
  utils/
    __init__.py
    data_info.py
    dr_utils.py
    ik_utils.py
    ik_utils_1.py
    isaac_eval_utils.py
    motion_lib.py
    reformat.py
    rlgames_utils.py
    rna_util.py
    torch_jit_utils.py
    torch_utils.py
    utils.py
whls/
  torch_cluster-1.6.3+pt24cu121-cp38-cp38-linux_x86_64.whl
```

## Config files (67)


### isaacgymenvs/cfg/config.yaml

```yaml

# Task name - used to pick the class to load
task_name:  ${task.name}
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

enableCameraSensors: False

## Device config
#  'physx' or 'flex'
physics_engine: 'physx'
# whether to use cpu or gpu pipeline
pipeline: 'gpu'
# device for running physics simulation
sim_device: 'cuda:2'
# device to run RL
rl_device: 'cuda:2'

# pipeline: 'cpu'
# # device for running physics simulation
# sim_device: 'cpu'
# # device to run RL
# rl_device: 'cpu'
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

# capture_video: False
capture_video: True
capture_video_freq: 1464
# capture_video_len: 135
capture_video_len: 300
force_render: True

render_mode: 'ansi'

exp_dir: '/cephfs/xueyi/exp/IsaacGymEnvs/isaacgymenvs'
tag: 'exp'

# disables rendering
headless: False

# set default task and default training config based on task
defaults:
  - task: Ant
  - train: ${task}PPO
  - hydra/job_logging: disabled
  - pbt: no_pbt

# sv_gt_refereces_fn: /home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231105_067_spoon2_data_opt_tag_optrulesrobo.npy

# set the directory where the output files get saved
hydra:
  output_subdir: null
  run:
    dir: .


### many and mnay and a lot of things should be optimized here ###

# ###### 20231105_067 -- spoon2 (test) #########
# scaled_object_asset_file: 'taco_20231105_067_wocollision'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231105_067_spoon2_data_opt_tag_optrulesrobo.npy'
# ###### 20231105_067 -- spoon2 (test) #########


# scaled_object_asset_file: 'taco_20230927_037_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20230927_037_brush3_data_opt_tag_optrobo1.npy'

# ######## 20230930_001 ########
# scaled_object_asset_file: 'taco_20230930_001_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20230930_001_plank1_data.npy'


######## 20231031_184 ########
# scaled_object_asset_file: 'taco_20231031_184_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231031_184_hammer20231031_184_data.npy'

# ######## 20231031_171 ########
# scaled_object_asset_file: 'taco_20231031_171_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231031_171_hammer20231031_171_data.npy'



# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_067_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_067_shovel20231027_067_data.npy'

# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_066_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_066_shovel20231027_066_data.npy'



# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_068_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_068_shovel20231027_068_data.npy'


# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_087_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_087_shovel20231027_087_data.npy'


# ######## 20231027_022 ########
# scaled_object_asset_file: 'taco_20231027_022_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_022_shovel20231027_022_data.npy'


# ######## 20231027_022 ########
# scaled_object_asset_file: 'taco_20231027_027_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_027_20231027_027_data.npy'


# ######## 20231027_022 ########
# scaled_object_asset_file: 'taco_20231027_066_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_066_20231027_066_data.npy'


# ######## 20231027_022 ########
# scaled_object_asset_file: 'taco_20231027_114_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_114_20231027_114_data.npy'


######## 20231027_022 ########
# scaled_object_asset_file: 'taco_20231027_130_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_130_20231027_130_data.npy'

# ######## grab - mouse ########
# scaled_object_asset_file: 'grab_mouse_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_grab_train_split_102_mouse_data_opt.npy'


# ######## grab - mouse ########
# scaled_object_asset_file: 'grab_bunny_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_grab_train_split_85_bunny_data_opt.npy'


######## grab - mouse ########
# scaled_object_asset_file: 'taco_20231026_002_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231026_002_20231026_002_data.npy'


# scaled_object_asset_file: 'grab_stapler107_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/Data/ReferenceData/shadow_grab_train_split_107_stapler107_data_fingerretar.npy'


# two_hands: True
# scaled_object_asset_file: 'arctic_mixer_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_arctic_s05_mixer_data_v3.npy'


# two_hands: False
# scaled_object_asset_file: 'grab_mouse_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_grab_mouse_102_dgrasptracking.npy'




# two_hands: False
# scaled_object_asset_file: 'grab_bunny_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_grab_bunny_85_dgrasptracking.npy'


# two_hands: False
# scaled_object_asset_file: 'taco_20231105_067_wocollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_spoon2_idx_20231105_067_dgrasptracking.npy'


# two_hands: True
# scaled_object_asset_file: 'arctic_mixer_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_arctic_s05_mixer_data_v3_opt2.npy'



# two_hands: True
# scaled_object_asset_file: 'arctic_phone_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_arctic_s07_phone_data_v3_opt2.npy'



# two_hands: True
# scaled_object_asset_file: 'arctic_ketchup_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_arctic_s07_ketchup_data_v3_opt2.npy'

two_hands: True
scaled_object_asset_file: 'arctic_microwave_wcollision.urdf'
gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_arctic_s06_microwave_data_v3_opt2.npy'
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

### isaacgymenvs/cfg/task/AllegroHandGrasp.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandGrasp 

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandGrasp"
  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 200 # 250
  enableDebugVis: False
  aggregateMode: 1

  w_obj_ornt: False

  use_relative_bias_control: False

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0
  # glb_dof_

  rigid_obj_density: 500

  use_fingertips: False

  test: False
  exp_logging_dir: ''

  use_canonical_state: False

  random_prior: True # random prior #
  random_time: True
  repose_z: False # True
  goal_cond: False

  object_name: ''

  object_code_dict: {
    # 'sem/Headphone':[1],
    'sem/taco_20231104_016': [1]
    # 'sem/Train': [1]
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
  observationType: "full_state_nforce" #  "full_state"
  
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
  dt: 0.0166 # 1/60 s
  substeps: 2
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  up_axis: "z"
  gravity: [0.0, 0.0, -9.81]
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

### isaacgymenvs/cfg/task/AllegroHandTracking.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTracking 

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandTracking"


  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  use_hand_actions_rew: False 
  supervised_training: False 
  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
        rigid
```

### isaacgymenvs/cfg/task/AllegroHandTrackingDiff.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingDiff 

physics_engine: ${..physics_engine}



diffusion:
  resume_checkpoint_pc: ''
  statistics_info_fn: ''
  slicing_ws: 30
  history_ws: 30
  grab_inst_tag_to_opt_stat_fn: ''
  grab_inst_tag_to_optimized_res_fn: ''
  sub_task_cond_type: full
  use_deterministic: False
  predict_ws: 1
  glb_rot_use_quat: False
  use_kine_obj_pos_canonicalization: False


env:
  env_name: "AllegroHandTrackingDiff"
  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
  dt: 0.0166 # 1/60 s # 
  substeps: 2
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  up_axis: "z"
  gravity: [0.0, 0.0, -9.81]
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
    re
```

### isaacgymenvs/cfg/task/AllegroHandTrackingGeneralist.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralist 

physics_engine: ${..physics_engine}


env:
  # AllegroHandTrackingGeneralistChunking
  env_name: "AllegroHandTrackingGeneralist"


  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'


  add_global_movements: False
  add_global_movements_af_step: 369

  ##### episod length scheduling settings #####
  schedule_episod_length: False
  episod_length_low: 270 
  episod_length_high: 500
  episod_length_warming_up_steps: 130
  episod_length_increasing_steps: 200

  use_actual_traj_length: False
  randomize_reset_frame: False
  add_forece_obs: False

  teacher_model_w_vel_obs: False

  load_chunking_experiences_v2: False
  history_chunking_obs_version: 'v1'

  ##### Hierarchical model test setting #####
  switch_between_models: False
  switch_to_trans_model_frame_after: 310
  switch_to_trans_model_ckpt_fn: ''
  ##### Hierarchical model test setting #####



  hand_glb_mult_scaling_progress_before: 900

  forecasting_obs_with_original_obs: False

  use_multi_step_control: False
  nn_control_substeps: 10

  add_global_motion_penalty: False
  add_torque_penalty: False
  add_work_penalty: False

  schedule_glb_action_penalty: False
  glb_penalty_low: 0.0003
  glb_penalty_high: 1.0
  glb_penalty_warming_up_steps: 50
  glb_penalty_increasing_steps: 300

  add_hand_targets_smooth: False
  hand_targets_smooth_coef: 0.4


  action_chunking_skip_frames: 1
  multi_inst_chunking: False
  add_obj_features: False

  kine_ed_tag: '.npy'

  only_rot_axis_guidance: False

  multi_traj_use_joint_order_in_sim: False
  preset_multi_traj_index: -1

  preload_action_targets_fn: ''
  preload_action_target_env_idx: 0
  preload_action_start_frame: 190

  use_no_obj_pose: False

  use_actual_prev_targets_in_obs: False

  test_inst_base_traj_tag: ''
  distinguish_kine_with_base_traj: False

  more_allegro_stiffness: False

  train_free_hand: False
  tune_hand_pd: False

  simreal_modeling: False
  action_chunking: False
  action_chunking_frames: 1

  distill_via_bc: False

  distill_full_to_partial: False

  bc_style_training: False
  bc_relative_targets: False

  add_physical_params_in_obs: False 
  whether_randomize_obs_act: True
  whether_randomize_obs: True
  whether_randomize_act: True

  obs_rand_noise_scale: 100

  ## more about the reorientation settings 
  w_rotation_axis_rew: False
  compute_rot_axis_rew_threshold: 120

  use_vision_obs: False


  reset_obj_mass: False
  obj_mass_reset: 0.27
  recompute_inertia: False

  use_v2_leap_warm_urdf: False 
  hand_specific_randomizations: False
  action_specific_randomizations: False
  action_specific_rand_noise_scale: 0.5

  w_traj_modifications: False
  obs_simplified: False
  # w_traj_modifications

  randomize_obj_init_pos: False
  randomize_obs_more: False
  obj_init_pos_rand_sigma: 0.1
  
  estimate_vels: False # 

  train_student_model: False
  ts_teacher_model_obs_dim: 731

  arm_stiffness: 400
  arm_effort: 200
  arm_damping: 80

  closed_loop_to_real: False

  wo_fingertip_pos: False 
  wo_fingertip_rot_vel: False
  wo_fingertip_vel: False

  not_use_kine_bias: False
  disable_hand_obj_contact: False


  #### 
  wo_hand_obj_contact: False
  #### 

  #### global mult factor scaling settings ####
  hand_glb_mult_factor_scaling_coef: 1.0
  hand_glb_mult_scaling_progress_after: 900
  #### global mult factor scaling settings ####

  #### roientation reward coeficient scheduing and the corresponding parameters ####
  schedule_ornt_rew_coef: False
  lowest_ornt_rew_coef: 0.03
  highest_ornt_rew_coef: 0.33
  ornt_rew_coef_warm_starting_steps: 100
  ornt_rew_coef_increasing_steps: 200
  #### roientation reward coeficient scheduing and the corresponding parameters ####

  schedule_hodist_rew_coef: False
  lowest_rew_finger_obj_dist_coef: 0.1
  highest_rew_finger_obj_dist_coef: 0.5
  hodist_rew_coef_warm_starting_steps: 100
  hodist_rew_coef_increasing_steps: 300


  #### franka settings ###
  load_kine_info_retar_with_arm: False
  kine_info_with_arm_sv_root: ''
  #### franka settings ###

  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####
  w_finger_pos_rew: False
  hand_qpos_rew_coef: 0.0
  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####

  ##### control parameters for arm (controlled via arm ik) #####
  control_arm_via_ik: False
  warm_trans_actions_mult_coef: 0.04
  warm_rot_actions_mult_coef: 0.04
  ##### control parameters for arm (controlled via arm ik) #####

  ##### control parameters for arm (controlled via setting arm joint commands) #####
  franka_delta_delta_mult_coef: 1.0
  ##### control parameters for arm (controlled via setting arm joint commands) #####
  


  single_inst_tag: ''
  activate_forecaster: False 

  open_loop_test: False

  use_multiple_kine_source_trajs: False
  multiple_kine_source_trajs_fn: ''

  compute_hand_rew_buf_threshold: 500

  comput_reward_traj_hand_qpos: False

  use_future_ref_as_obs_goal: False

  forecasting_model_inv_freq: 1

  forecast_obj_pos: False

  
  #### History and glboal hand pose/obj pos/obj ornt features ####
  history_window_size: 60
  glb_feat_per_skip: 1
  centralize_info: False
  forecast_future_freq:  1 # forecast #
  #### History and glboal hand pose/obj pos/obj ornt features ####

  include_obj_rot_in_obs: False

  #### Conditional setting: whether to use the start and end conditional settings ####
  st_ed_state_cond: False
  #### Conditional setting: whether to use the start and end conditional settings ####

  use_clip_glb_features: False

  only_use_hand_first_frame: False

  #### Conditional information ####
  partial_hand_info: False
  partial_obj_info: False
  partial_obj_pos_info: False

  hist_cond_partial_hand_info: False
  hist_cond_partial_obj_info: False
  hist_cond_partial_obj_pos_info: False

  preset_cond_type: 0
  preset_inv_cond_freq: 1
  #### Conditional information ####


  #### Randomize conditions ####
  randomize_conditions: False
  randomize_condition_type: 'random'
  add_contact_conditions: False
  contact_info_sv_root: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced_300_contactflag"
  #### Randomize conditions ####

  #### Random shift conditions ####
  random_shift_cond: False
  random_shift_cond_freq: False
  maxx_inv_cond_freq: 30
  #### Random shift conditions ####


  #### Masked mimicing training --- for randomized conditions ####
  masked_mimic_training: False
  #### Masked mimicing training --- for randomized conditions ####

  #### forcasting model setting --- whether to add the history window ####
  w_history_window_index: False 
  #### forcasting model setting --- whether to add the history window ####


  # 


  #### Whether to use the future obs ####
  use_future_obs: False
  #### Whether to use the future obs ####

  #### History observation ferquency ####
  history_freq: 1
  #### History observation ferquency ####

  #### Spe
```

### isaacgymenvs/cfg/task/AllegroHandTrackingGeneralistChunking.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralistChunking 

physics_engine: ${..physics_engine}


env:
  # AllegroHandTrackingGeneralistChunking
  env_name: "AllegroHandTrackingGeneralistChunking"

  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'

  add_global_movements: False
  add_global_movements_af_step: 369


  ##### episod length scheduling settings #####
  schedule_episod_length: False
  episod_length_low: 270 
  episod_length_high: 500
  episod_length_warming_up_steps: 130
  episod_length_increasing_steps: 200

  use_actual_traj_length: False
  randomize_reset_frame: False
  add_forece_obs: False

  teacher_model_w_vel_obs: False


  load_chunking_experiences_v2: False
  history_chunking_obs_version: 'v1'

  ##### Hierarchical model test setting #####
  switch_between_models: False
  switch_to_trans_model_frame_after: 310
  switch_to_trans_model_ckpt_fn: ''
  ##### Hierarchical model test setting #####


  hand_glb_mult_scaling_progress_before: 900

  forecasting_obs_with_original_obs: False

  use_multi_step_control: False
  nn_control_substeps: 10

  add_global_motion_penalty: False
  add_torque_penalty: False
  add_work_penalty: False

  schedule_glb_action_penalty: False
  glb_penalty_low: 0.0003
  glb_penalty_high: 1.0
  glb_penalty_warming_up_steps: 50
  glb_penalty_increasing_steps: 300

  add_hand_targets_smooth: False
  hand_targets_smooth_coef: 0.4

  multi_traj_use_joint_order_in_sim: False
  preset_multi_traj_index: -1

  multi_inst_chunking: False
  add_obj_features: False

  kine_ed_tag: '.npy'

  only_rot_axis_guidance: False

  use_actual_prev_targets_in_obs: False

  preload_action_targets_fn: ''
  preload_action_target_env_idx: 0
  preload_action_start_frame: 190

  action_chunking_skip_frames: 1

  use_no_obj_pose: False

  train_free_hand: False
  tune_hand_pd: False
  simreal_modeling: False
  distill_full_to_partial: False

  more_allegro_stiffness: False

  action_chunking: False
  action_chunking_frames: 1
  bc_style_training: False
  bc_relative_targets: False

  distill_via_bc: False

  test_inst_base_traj_tag: ''
  distinguish_kine_with_base_traj: False

  # bc_style_training: False
  
  add_physical_params_in_obs: False 
  whether_randomize_obs_act: True
  whether_randomize_obs: True
  whether_randomize_act: True

  obs_rand_noise_scale: 100

  ## more about the reorientation settings 
  w_rotation_axis_rew: False
  compute_rot_axis_rew_threshold: 120

  use_vision_obs: False


  reset_obj_mass: False
  obj_mass_reset: 0.27
  recompute_inertia: False

  use_v2_leap_warm_urdf: False 
  hand_specific_randomizations: False
  action_specific_randomizations: False
  action_specific_rand_noise_scale: 0.5

  w_traj_modifications: False
  obs_simplified: False
  # w_traj_modifications

  randomize_obj_init_pos: False
  randomize_obs_more: False
  obj_init_pos_rand_sigma: 0.1
  
  estimate_vels: False # 

  train_student_model: False
  ts_teacher_model_obs_dim: 731

  arm_stiffness: 400
  arm_effort: 200
  arm_damping: 80

  closed_loop_to_real: False

  wo_fingertip_pos: False 
  wo_fingertip_rot_vel: False
  wo_fingertip_vel: False

  not_use_kine_bias: False
  disable_hand_obj_contact: False


  #### 
  wo_hand_obj_contact: False
  #### 

  #### global mult factor scaling settings ####
  hand_glb_mult_factor_scaling_coef: 1.0
  hand_glb_mult_scaling_progress_after: 900
  #### global mult factor scaling settings ####

  #### roientation reward coeficient scheduing and the corresponding parameters ####
  schedule_ornt_rew_coef: False
  lowest_ornt_rew_coef: 0.03
  highest_ornt_rew_coef: 0.33
  ornt_rew_coef_warm_starting_steps: 100
  ornt_rew_coef_increasing_steps: 200
  #### roientation reward coeficient scheduing and the corresponding parameters ####

  schedule_hodist_rew_coef: False
  lowest_rew_finger_obj_dist_coef: 0.1
  highest_rew_finger_obj_dist_coef: 0.5
  hodist_rew_coef_warm_starting_steps: 100
  hodist_rew_coef_increasing_steps: 300


  #### franka settings ###
  load_kine_info_retar_with_arm: False
  kine_info_with_arm_sv_root: ''
  #### franka settings ###

  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####
  w_finger_pos_rew: False
  hand_qpos_rew_coef: 0.0
  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####

  ##### control parameters for arm (controlled via arm ik) #####
  control_arm_via_ik: False
  warm_trans_actions_mult_coef: 0.04
  warm_rot_actions_mult_coef: 0.04
  ##### control parameters for arm (controlled via arm ik) #####

  ##### control parameters for arm (controlled via setting arm joint commands) #####
  franka_delta_delta_mult_coef: 1.0
  ##### control parameters for arm (controlled via setting arm joint commands) #####
  


  single_inst_tag: ''
  activate_forecaster: False 

  open_loop_test: False

  use_multiple_kine_source_trajs: False
  multiple_kine_source_trajs_fn: ''

  compute_hand_rew_buf_threshold: 500

  comput_reward_traj_hand_qpos: False

  use_future_ref_as_obs_goal: False

  forecasting_model_inv_freq: 1

  forecast_obj_pos: False

  
  #### History and glboal hand pose/obj pos/obj ornt features ####
  history_window_size: 60
  glb_feat_per_skip: 1
  centralize_info: False
  forecast_future_freq:  1 # forecast #
  #### History and glboal hand pose/obj pos/obj ornt features ####

  include_obj_rot_in_obs: False

  #### Conditional setting: whether to use the start and end conditional settings ####
  st_ed_state_cond: False
  #### Conditional setting: whether to use the start and end conditional settings ####

  use_clip_glb_features: False

  only_use_hand_first_frame: False

  #### Conditional information ####
  partial_hand_info: False
  partial_obj_info: False
  partial_obj_pos_info: False

  hist_cond_partial_hand_info: False
  hist_cond_partial_obj_info: False
  hist_cond_partial_obj_pos_info: False

  preset_cond_type: 0
  preset_inv_cond_freq: 1
  #### Conditional information ####


  #### Randomize conditions ####
  randomize_conditions: False
  randomize_condition_type: 'random'
  add_contact_conditions: False
  contact_info_sv_root: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced_300_contactflag"
  #### Randomize conditions ####

  #### Random shift conditions ####
  random_shift_cond: False
  random_shift_cond_freq: False
  maxx_inv_cond_freq: 30
  #### Random shift conditions ####


  #### Masked mimicing training --- for randomized conditions ####
  masked_mimic_training: False
  #### Masked mimicing training --- for randomized conditions ####

  #### forcasting model setting --- whether to add the history window ####
  w_history_window_index: False 
  #### forcasting model setting --- whether to add the history window ####


  # 


  #### Whether to use the future obs ####
  use_future_obs: False
  #### Whether to use the future obs ####

  #### History observation ferquency ####
  history_freq: 1
  #### History observation ferquency ####

  #### Speecify the network type ####
  net_type: 'v4'
  #### Speecify the network type ####

  #### 
```

### isaacgymenvs/cfg/task/AllegroHandTrackingGeneralistV2.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralistV2 

physics_engine: ${..physics_engine}


env:
  # AllegroHandTrackingGeneralistChunking
  env_name: "AllegroHandTrackingGeneralistV2"


  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'


  add_global_movements: False
  add_global_movements_af_step: 369

  ##### episod length scheduling settings #####
  schedule_episod_length: False
  episod_length_low: 270 
  episod_length_high: 500
  episod_length_warming_up_steps: 130
  episod_length_increasing_steps: 200

  use_actual_traj_length: False
  randomize_reset_frame: False
  add_forece_obs: False

  teacher_model_w_vel_obs: False

  load_chunking_experiences_v2: False
  history_chunking_obs_version: 'v1'

  ##### Hierarchical model test setting #####
  switch_between_models: False
  switch_to_trans_model_frame_after: 310
  switch_to_trans_model_ckpt_fn: ''
  ##### Hierarchical model test setting #####


  hand_glb_mult_scaling_progress_before: 900

  forecasting_obs_with_original_obs: False

  use_multi_step_control: False
  nn_control_substeps: 10

  add_global_motion_penalty: False
  add_torque_penalty: False
  add_work_penalty: False

  schedule_glb_action_penalty: False
  glb_penalty_low: 0.0003
  glb_penalty_high: 1.0
  glb_penalty_warming_up_steps: 50
  glb_penalty_increasing_steps: 300

  add_hand_targets_smooth: False
  hand_targets_smooth_coef: 0.4

  action_chunking_skip_frames: 1
  multi_inst_chunking: False
  add_obj_features: False

  kine_ed_tag: '.npy'

  only_rot_axis_guidance: False

  multi_traj_use_joint_order_in_sim: False
  preset_multi_traj_index: -1

  preload_action_targets_fn: ''
  preload_action_target_env_idx: 0
  preload_action_start_frame: 190

  use_no_obj_pose: False

  use_actual_prev_targets_in_obs: False

  test_inst_base_traj_tag: ''
  distinguish_kine_with_base_traj: False

  more_allegro_stiffness: False

  train_free_hand: False
  tune_hand_pd: False

  simreal_modeling: False
  action_chunking: False
  action_chunking_frames: 1

  distill_via_bc: False

  distill_full_to_partial: False

  bc_style_training: False
  bc_relative_targets: False

  add_physical_params_in_obs: False 
  whether_randomize_obs_act: True
  whether_randomize_obs: True
  whether_randomize_act: True

  obs_rand_noise_scale: 100

  ## more about the reorientation settings 
  w_rotation_axis_rew: False
  compute_rot_axis_rew_threshold: 120

  use_vision_obs: False


  reset_obj_mass: False
  obj_mass_reset: 0.27
  recompute_inertia: False

  use_v2_leap_warm_urdf: False 
  hand_specific_randomizations: False
  action_specific_randomizations: False
  action_specific_rand_noise_scale: 0.5

  w_traj_modifications: False
  obs_simplified: False
  # w_traj_modifications

  randomize_obj_init_pos: False
  randomize_obs_more: False
  obj_init_pos_rand_sigma: 0.1
  
  estimate_vels: False # 

  train_student_model: False
  ts_teacher_model_obs_dim: 731

  arm_stiffness: 400
  arm_effort: 200
  arm_damping: 80

  closed_loop_to_real: False

  wo_fingertip_pos: False 
  wo_fingertip_rot_vel: False
  wo_fingertip_vel: False

  not_use_kine_bias: False
  disable_hand_obj_contact: False


  #### 
  wo_hand_obj_contact: False
  #### 

  #### global mult factor scaling settings ####
  hand_glb_mult_factor_scaling_coef: 1.0
  hand_glb_mult_scaling_progress_after: 900
  #### global mult factor scaling settings ####

  #### roientation reward coeficient scheduing and the corresponding parameters ####
  schedule_ornt_rew_coef: False
  lowest_ornt_rew_coef: 0.03
  highest_ornt_rew_coef: 0.33
  ornt_rew_coef_warm_starting_steps: 100
  ornt_rew_coef_increasing_steps: 200
  #### roientation reward coeficient scheduing and the corresponding parameters ####

  schedule_hodist_rew_coef: False
  lowest_rew_finger_obj_dist_coef: 0.1
  highest_rew_finger_obj_dist_coef: 0.5
  hodist_rew_coef_warm_starting_steps: 100
  hodist_rew_coef_increasing_steps: 300


  #### franka settings ###
  load_kine_info_retar_with_arm: False
  kine_info_with_arm_sv_root: ''
  #### franka settings ###

  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####
  w_finger_pos_rew: False
  hand_qpos_rew_coef: 0.0
  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####

  ##### control parameters for arm (controlled via arm ik) #####
  control_arm_via_ik: False
  warm_trans_actions_mult_coef: 0.04
  warm_rot_actions_mult_coef: 0.04
  ##### control parameters for arm (controlled via arm ik) #####

  ##### control parameters for arm (controlled via setting arm joint commands) #####
  franka_delta_delta_mult_coef: 1.0
  ##### control parameters for arm (controlled via setting arm joint commands) #####
  


  single_inst_tag: ''
  activate_forecaster: False 

  open_loop_test: False

  use_multiple_kine_source_trajs: False
  multiple_kine_source_trajs_fn: ''

  compute_hand_rew_buf_threshold: 500

  comput_reward_traj_hand_qpos: False

  use_future_ref_as_obs_goal: False

  forecasting_model_inv_freq: 1

  forecast_obj_pos: False

  
  #### History and glboal hand pose/obj pos/obj ornt features ####
  history_window_size: 60
  glb_feat_per_skip: 1
  centralize_info: False
  forecast_future_freq:  1 # forecast #
  #### History and glboal hand pose/obj pos/obj ornt features ####

  include_obj_rot_in_obs: False

  #### Conditional setting: whether to use the start and end conditional settings ####
  st_ed_state_cond: False
  #### Conditional setting: whether to use the start and end conditional settings ####

  use_clip_glb_features: False

  only_use_hand_first_frame: False

  #### Conditional information ####
  partial_hand_info: False
  partial_obj_info: False
  partial_obj_pos_info: False

  hist_cond_partial_hand_info: False
  hist_cond_partial_obj_info: False
  hist_cond_partial_obj_pos_info: False

  preset_cond_type: 0
  preset_inv_cond_freq: 1
  #### Conditional information ####


  #### Randomize conditions ####
  randomize_conditions: False
  randomize_condition_type: 'random'
  add_contact_conditions: False
  contact_info_sv_root: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced_300_contactflag"
  #### Randomize conditions ####

  #### Random shift conditions ####
  random_shift_cond: False
  random_shift_cond_freq: False
  maxx_inv_cond_freq: 30
  #### Random shift conditions ####


  #### Masked mimicing training --- for randomized conditions ####
  masked_mimic_training: False
  #### Masked mimicing training --- for randomized conditions ####

  #### forcasting model setting --- whether to add the history window ####
  w_history_window_index: False 
  #### forcasting model setting --- whether to add the history window ####


  # 


  #### Whether to use the future obs ####
  use_future_obs: False
  #### Whether to use the future obs ####

  #### History observation ferquency ####
  history_freq: 1
  #### History observation ferquency ####

  #### S
```

### isaacgymenvs/cfg/task/AllegroHandTrackingGeneralistWForecasting.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralistWForecasting 

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandTrackingGeneralistWForecasting"



  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'


  add_global_movements: False
  add_global_movements_af_step: 369

  ##### episod length scheduling settings #####
  schedule_episod_length: False
  episod_length_low: 270 
  episod_length_high: 500
  episod_length_warming_up_steps: 130
  episod_length_increasing_steps: 200

  use_actual_traj_length: False
  randomize_reset_frame: False
  add_forece_obs: False

  teacher_model_w_vel_obs: False

  load_chunking_experiences_v2: False
  history_chunking_obs_version: 'v1'

  ##### Hierarchical model test setting #####
  switch_between_models: False
  switch_to_trans_model_frame_after: 310
  switch_to_trans_model_ckpt_fn: ''
  ##### Hierarchical model test setting #####

  hand_glb_mult_scaling_progress_before: 900

  forecasting_obs_with_original_obs: False

  use_multi_step_control: False
  nn_control_substeps: 10

  add_global_motion_penalty: False
  add_torque_penalty: False
  add_work_penalty: False

  schedule_glb_action_penalty: False
  glb_penalty_low: 0.0003
  glb_penalty_high: 1.0
  glb_penalty_warming_up_steps: 50
  glb_penalty_increasing_steps: 300

  add_hand_targets_smooth: False
  hand_targets_smooth_coef: 0.4

  multi_traj_use_joint_order_in_sim: False
  preset_multi_traj_index: -1

  multi_inst_chunking: False
  add_obj_features: False

  kine_ed_tag: '.npy'

  only_rot_axis_guidance: False

  use_actual_prev_targets_in_obs: False

  preload_action_targets_fn: ''
  preload_action_target_env_idx: 0
  preload_action_start_frame: 190

  use_no_obj_pose: False

  train_free_hand: False
  tune_hand_pd: False
  simreal_modeling: False
  distill_full_to_partial: False

  more_allegro_stiffness: False

  action_chunking: False
  action_chunking_frames: 1

  bc_style_training: False
  bc_relative_targets: False

  distill_via_bc: False

  test_inst_base_traj_tag: ''
  distinguish_kine_with_base_traj: False

  add_physical_params_in_obs: False 
  whether_randomize_obs_act: True
  whether_randomize_obs: True
  whether_randomize_act: True

  obs_rand_noise_scale: 100

  w_rotation_axis_rew: False
  compute_rot_axis_rew_threshold: 120


  use_vision_obs: False


  reset_obj_mass: False
  obj_mass_reset: 0.27
  recompute_inertia: False

  use_v2_leap_warm_urdf: False
  hand_specific_randomizations: False 
  action_specific_randomizations: False
  action_specific_rand_noise_scale: 0.5

  #### teacher student model training setting ####
  train_student_model: False
  ts_teacher_model_obs_dim: 731
  #### teacher student model training setting ####

  w_traj_modifications: False
  obs_simplified: False

  randomize_obj_init_pos: False
  randomize_obs_more: False
  obj_init_pos_rand_sigma: 0.1

  estimate_vels: False

  arm_stiffness: 400
  arm_effort: 200
  arm_damping: 80

  closed_loop_to_real: False

  wo_fingertip_pos: False 
  wo_fingertip_rot_vel: False 
  wo_fingertip_vel: False

  not_use_kine_bias: False
  disable_hand_obj_contact: False

  #### global mult factor scaling settings ####
  hand_glb_mult_factor_scaling_coef: 1.0
  hand_glb_mult_scaling_progress_after: 900
  #### global mult factor scaling settings ####

  #### roientation reward coeficient scheduing and the corresponding parameters ####
  schedule_ornt_rew_coef: False
  lowest_ornt_rew_coef: 0.03
  highest_ornt_rew_coef: 0.33
  ornt_rew_coef_warm_starting_steps: 100
  ornt_rew_coef_increasing_steps: 200
  #### roientation reward coeficient scheduing and the corresponding parameters ####


  schedule_hodist_rew_coef: False
  lowest_rew_finger_obj_dist_coef: 0.1
  highest_rew_finger_obj_dist_coef: 0.5
  hodist_rew_coef_warm_starting_steps: 100
  hodist_rew_coef_increasing_steps: 300

  #### franka settings ###
  load_kine_info_retar_with_arm: False
  kine_info_with_arm_sv_root: ''
  #### franka settings ###

  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####
  w_finger_pos_rew: False
  hand_qpos_rew_coef: 0.0
  ##### finger positional guidance setting -- finger pos reward and finger qpos reward #####

  ##### control parameters for arm (controlled via arm ik) #####
  control_arm_via_ik: False
  warm_trans_actions_mult_coef: 0.04
  warm_rot_actions_mult_coef: 0.04
  ##### control parameters for arm (controlled via arm ik) #####

  ##### control parameters for arm (controlled via setting arm joint commands) #####
  franka_delta_delta_mult_coef: 1.0
  ##### control parameters for arm (controlled via setting arm joint commands) #####
  



  # with forecast #
  single_inst_tag: ''
  activate_forecaster: True

  open_loop_test: False 

  comput_reward_traj_hand_qpos: False

  use_future_ref_as_obs_goal: False

  forecasting_model_inv_freq: 1

  forecast_obj_pos: False

  use_multiple_kine_source_trajs: False
  multiple_kine_source_trajs_fn: ''

  include_obj_rot_in_obs: False 

  compute_hand_rew_buf_threshold: 500

  #### History and glboal hand pose/obj pos/obj ornt features ####
  history_window_size: 60
  glb_feat_per_skip: 1
  centralize_info: False
  forecast_future_freq:  1 # forecast #
  #### History and glboal hand pose/obj pos/obj ornt features ####


  #### Conditional setting: whether to use the start and end conditional settings ####
  st_ed_state_cond: False
  #### Conditional setting: whether to use the start and end conditional settings ####

  use_clip_glb_features: False

  only_use_hand_first_frame: False

  #### Conditional information ##### conditional information #
  partial_hand_info: False
  partial_obj_info: False
  partial_obj_pos_info: False

  hist_cond_partial_hand_info: False
  hist_cond_partial_obj_info: False
  hist_cond_partial_obj_pos_info: False

  preset_cond_type: 0
  preset_inv_cond_freq: 1
  #### Conditional information ####


  #### Randomize conditions ####
  randomize_conditions: False
  randomize_condition_type: 'random'
  add_contact_conditions: False
  contact_info_sv_root: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced_300_contactflag"
  #### Randomize conditions ####

  #### Random shift conditions ####
  random_shift_cond: False
  random_shift_cond_freq: False
  maxx_inv_cond_freq: 30
  #### Random shift conditions ####


  #### Masked mimicing training --- for randomized conditions ####
  masked_mimic_training: False
  #### Masked mimicing training --- for randomized conditions ####

  #### forcasting model setting --- whether to add the history window ####
  w_history_window_index: False 
  #### forcasting model setting --- whether to add the history window ####





  #### Whether to use the future obs ####
  use_future_obs: False
  #### Whether to use the future obs ####

  #### History observation ferquency ####
  history_freq: 1
  #### History observation ferquency ####

  #### Speecify the network type ####
  net_type: 'v4'
  #### Speecify the net
```

### isaacgymenvs/cfg/task/AllegroHandTrackingPlay.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingPlay

physics_engine: ${..physics_engine}


env:
  
  env_name: "AllegroHandTrackingPlay"

  # /cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy
  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'
  
  #### Speecify the network type ####
  net_type: 'v4'
  #### Speecify the network type ####


  base_traj: ''
  
  obj_type_to_base_traj_fn: ''

  use_base_traj: False
  use_strict_maxx_nn_ts: False
  strict_maxx_nn_ts: 150
  taco_interped_data_sv_additional_tag: ''

  grab_obj_type_to_opt_res_fn: ''
  taco_obj_type_to_opt_res_fn: ''

  only_training_on_succ_samples: False

  rew_smoothness_coef: 0.0

  rew_grab_thres: 50.0
  rew_taco_thres: 200.0

  grab_train_test_setting: False
  
  maxx_inst_nn: 10000

  use_local_canonical_state: False
  
  replay_fn: ''


  object_feat_dim: 256
  tracking_save_info_fn: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced/data"
  # export tracking_info_st_tag='passive_active_info_'
  tracking_info_st_tag: 'passive_active_info_'
  use_hand_actions_rew: True
  supervised_training: False
  test_subj_nm: ''

  ### test instance tag ###
  test_inst_tag: ''
  test_optimized_res: ''
  single_instance_state_based_test: False
  sampleds_with_object_code_fn: ''

  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
  
```

### isaacgymenvs/cfg/task/AllegroHandTrackingPlayDemo.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingPlayDemo

physics_engine: ${..physics_engine}


env:
  
  env_name: "AllegroHandTrackingPlayDemo"

  # /cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy
  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'

  datanm_to_replay_fn_dict_fn: '/root/diffsim/IsaacGymEnvs2/assets/optimized_res_grab_300_demo/statistics/data_inst_tag_to_optimized_res_top50.npy'

  base_traj: ''
  
  obj_type_to_base_traj_fn: ''

  use_base_traj: False
  use_strict_maxx_nn_ts: False
  strict_maxx_nn_ts: 150
  taco_interped_data_sv_additional_tag: ''

  grab_obj_type_to_opt_res_fn: ''
  taco_obj_type_to_opt_res_fn: ''

  only_training_on_succ_samples: False

  rew_smoothness_coef: 0.0

  rew_grab_thres: 50.0
  rew_taco_thres: 200.0

  grab_train_test_setting: False
  
  maxx_inst_nn: 10000

  use_local_canonical_state: False
  
  replay_fn: ''


  object_feat_dim: 256
  tracking_save_info_fn: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced/data"
  # export tracking_info_st_tag='passive_active_info_'
  tracking_info_st_tag: 'passive_active_info_'
  use_hand_actions_rew: True
  supervised_training: False
  test_subj_nm: ''

  ### test instance tag ###
  test_inst_tag: ''
  test_optimized_res: ''
  single_instance_state_based_test: False
  sampleds_with_object_code_fn: ''

  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_s
```

### isaacgymenvs/cfg/task/AllegroHandTrackingPlayHandware.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralist 

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandTrackingGeneralist"

  # /cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy
  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'

  # generlaist training # 

  wo_vel_obs: False

  
  
  customize_damping: False
  customize_global_damping: False
  train_on_all_trajs: False 

  base_traj: ''
  
  obj_type_to_base_traj_fn: ''

  use_base_traj: False
  use_strict_maxx_nn_ts: False
  strict_maxx_nn_ts: 150
  taco_interped_data_sv_additional_tag: ''

  grab_obj_type_to_opt_res_fn: ''
  taco_obj_type_to_opt_res_fn: ''

  only_training_on_succ_samples: False

  rew_smoothness_coef: 0.0

  rew_grab_thres: 50.0
  rew_taco_thres: 200.0

  data_selection_ratio: 1.0
  
  rew_thres_with_selected_insts: False
  selected_inst_idxes_dict: ''

  grab_train_test_setting: False
  
  maxx_inst_nn: 10000

  use_local_canonical_state: False
  
  object_feat_dim: 256
  tracking_save_info_fn: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced/data"
  # export tracking_info_st_tag='passive_active_info_'
  tracking_info_st_tag: 'passive_active_info_'
  use_hand_actions_rew: True
  supervised_training: False
  test_subj_nm: ''

  ### test instance tag ###
  test_inst_tag: ''
  test_optimized_res: ''
  single_instance_state_based_test: False
  single_instance_state_based_train: False
  sampleds_with_object_code_fn: ''

  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
            distribution: "log
```

### isaacgymenvs/cfg/task/AllegroHandTrackingPlayHandwareDeploy.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingGeneralistDeploy 

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandTrackingGeneralistDeploy"

  # /cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy
  ### grab inst tag to opt stat fn ###
  # directly help us with some problems --- the policy #
  grab_inst_tag_to_opt_stat_fn: '/cephfs/xueyi/uni_manip/isaacgym_rl_exp_grab/statistics/obj_type_to_optimized_res.npy'
  # set grab_inst_tag_to_optimized_res 
  # set taco and the grab inst tag to the optimized res fn #
  grab_inst_tag_to_optimized_res_fn: '/root/diffsim/softzoo/softzoo/diffusion/assets/data_inst_tag_to_optimized_res.npy'
  # taco_inst_tag_to_optimized_res_fn: "/cephfs/xueyi/uni_manip/isaacgym_rl_exp_taco_grab_interpseq_eval_v2/statistics/data_inst_tag_to_optimized_res.npy"
  taco_inst_tag_to_optimized_res_fn: ""
  object_type_to_latent_feature_fn: "/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnew_/obj_type_to_obj_feat.npy"
  # /cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy
  inst_tag_to_latent_feature_fn: ''
  # export inst_tag_to_latent_feature_fn='/cephfs/xueyi/uni_manip/tds_diffusion_exp/allegro_tracking_kine_diff_AE_Diff_trainAE_vnewv2_v3data_sample_/inst_tag_to_obj_feat.npy'

  # generlaist training # 

  wo_vel_obs: False

  
  
  customize_damping: False
  customize_global_damping: False
  train_on_all_trajs: False 

  base_traj: ''
  
  obj_type_to_base_traj_fn: ''

  use_base_traj: False
  use_strict_maxx_nn_ts: False
  strict_maxx_nn_ts: 150
  taco_interped_data_sv_additional_tag: ''

  grab_obj_type_to_opt_res_fn: ''
  taco_obj_type_to_opt_res_fn: ''

  only_training_on_succ_samples: False

  rew_smoothness_coef: 0.0

  rew_grab_thres: 50.0
  rew_taco_thres: 200.0

  data_selection_ratio: 1.0
  
  rew_thres_with_selected_insts: False
  selected_inst_idxes_dict: ''

  grab_train_test_setting: False
  
  maxx_inst_nn: 10000

  use_local_canonical_state: False
  
  object_feat_dim: 256
  tracking_save_info_fn: "/cephfs/xueyi/data/GRAB_Tracking_PK_reduced/data"
  # export tracking_info_st_tag='passive_active_info_'
  tracking_info_st_tag: 'passive_active_info_'
  use_hand_actions_rew: True
  supervised_training: False
  test_subj_nm: ''

  ### test instance tag ###
  test_inst_tag: ''
  test_optimized_res: ''
  single_instance_state_based_test: False
  single_instance_state_based_train: False
  sampleds_with_object_code_fn: ''

  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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
            distri
```

### isaacgymenvs/cfg/task/AllegroHandTrackingVision.yaml

```yaml
# graphics_device_id: 0
name: AllegroHandTrackingVision

physics_engine: ${..physics_engine}


env:
  env_name: "AllegroHandTrackingVision"

  vision_obs: True

  enableCameraSensors: True

  vision:
    color:
      hand: [ 0.50, 0.50, 0.50 ] # gray
      # 0.6, 0.72, 0.98
      object: [ 1.00, 0.20, 0.20 ] # red
      goal: [ 0.50, 1.00, 0.35 ] # green
    pointclouds:
      numPresample: 10240 # 65536
      numDownsample: 256 # 1024
      numEachPoint: 3 # 6
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
      # z_n: 0.61
      # z_p: 1.3
      z_n: 0.0
      z_p: 0.7
      depth: 1.2



  numEnvs: 1024 #  1000
  envSpacing: 1.5
  episodeLength: 1000 # 150 # 250
  enableDebugVis: False
  aggregateMode: 1

  hand_type: 'allegro'

  test: False

  start_frame: 0

  separate_stages: False
  
  use_fingertips: False

  ground_distance: 0.0

  disable_obj_gravity: False

  right_hand_dist_thres: 0.12

  add_table: False
  table_z_dim: 0.5

  glb_trans_vel_scale: 1.0
  glb_rot_vel_scale: 1.0

  pre_optimized_traj: ''
  use_twostage_rew: False
  use_real_twostage_rew: False
  start_grasping_fr: False 

  lifting_separate_stages: False
  strict_lifting_separate_stages: False

  hand_pose_guidance_glb_trans_coef: 0.6
  hand_pose_guidance_glb_rot_coef: 0.1
  hand_pose_guidance_fingerpose_coef: 0.1

  use_kinematics_bias: False
  use_kinematics_bias_wdelta: False

  goal_dist_thres: 0.0

  use_taco_obj_traj: False

  #### reward ceofs ####
  rew_finger_obj_dist_coef: 0.5
  rew_delta_hand_pose_coef: 0.5
  rew_obj_pose_coef: 1.0
  #### reward ceofs ####
        
  tight_obs: False

  use_canonical_state: False
  use_unified_canonical_state: False

  rigid_obj_density: 500
  
  kinematics_only: False

  w_obj_ornt: False
  w_obj_vels: False

  mocap_sv_info_fn: ''
  object_name: ''

  exp_logging_dir: ''

  random_prior: True
  random_time: True
  repose_z: False #  True
  goal_cond: False

  object_code_dict: {
    'sem/Headphone':[1],
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
  observationType: "full_state_nforce" #  "full_state"
  
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

  # vision:
  #   color:
  #     hand: [ 0.50, 0.50, 0.50 ] # gray
  #     # 0.6, 0.72, 0.98
  #     object: [ 1.00, 0.20, 0.20 ] # red
  #     goal: [ 0.50, 1.00, 0.35 ] # green
  #   pointclouds:
  #     numPresample: 65536
  #     numDownsample: 1024
  #     numEachPoint: 6
  #   camera:
  #     # relative to table center
  #     eye: [
  #       [ 0.0, 0.0, 0.55 ],
  #       [ 0.5, 0.0, 0.05 ],
  #       [ -0.5, 0.0, 0.05 ],
  #       [ 0.0, 0.5, 0.05 ],
  #       [ 0.0, -0.5, 0.05 ]
  #     ]
  #     lookat: [
  #       [ 0.01, 0.0, 0.05 ], # camera cannot look at accurate -z
  #       [ 0.0, 0.0, 0.05 ],
  #       [ 0.0, 0.0, 0.05 ],
  #       [ 0.0, 0.0, 0.05 ],
  #       [ 0.0, 0.0, 0.05 ],
  #     ]
  #   #      eye: [[0.2, -0.5, 0.4], [1.0, 0.2, 0.4], [0.2, 0.2, 0.8]]
  #   #      lookat: [[0.2, 3.5, 0.4], [-3.0, 0.2, 0.4], [0.2, 0.19, -1.2]]
  #   probe:
  #     num_probes: 0 # set this to 0
  #     width: 256
  #     height: 256
  #     eye: [
  #       [ 1.6, 0.0, 2.5 ],
  #     ]
  #     forward: [
  #       [ -0.8, 0.0, -2.0 ],
  #     ]
  #   bar:
  #     x_n: -1
  #     x_p: 1
  #     y_n: -1
  #     y_p: 1
  #     z_n: 0.61
  #     z_p: 1.3
  #     depth: 1.2

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
            range: 
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

### isaacgymenvs/cfg/task/FullBody.yaml

```yaml
# used to create the object
name: FullBody 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 3
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False 
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  # stateInit: "Random"
  # hybridInitProb: 0.5
  # numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["left_hand", "right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  terminationHeight: 0.15
  enableEarlyTermination: True


  random_prior: True
  # repose_z: True
  repose_z: False
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/FullBodyAMP.yaml

```yaml
# used to create the object
name: FullBodyAMP

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 500
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  
  pdControl: False
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  stateInit: "Default"
  hybridInitProb: 0.5
  numAMPObsSteps: 10

  localRootObs: True
  contactBodies: ["right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  keyBodies: ["left_hand", "right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  AMPkeyBodies: ["left_hand", "right_foot", "left_foot" ]
  terminationHeight: 0.15
  enableEarlyTermination: True


  tarSpeed: 1.0
  tarChangeStepsMin: 100
  tarChangeStepsMax: 200
  tarDistMax: 10.0
  enableTaskObs: False


  random_prior: True
  # repose_z: True
  repose_z: False
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


  # animation files to learn from
  # these motions should use hyperparameters from HumanoidAMPPPO.yaml
  # motion_file: "amp_humanoid_walk.npy"
  motion_file: "amp_humanoid_run.npy"
  #motion_file: "amp_humanoid_dance.npy"

  # these motions should use hyperparameters from HumanoidAMPPPOLowGP.yaml
  #motion_file: "amp_humanoid_hop.npy"
  #motion_file: "amp_humanoid_backflip.npy"

  asset:
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/FullBodyStatic.yaml

```yaml
# used to create the object
name: FullBodyStatic 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 2
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False 
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  # stateInit: "Random"
  # hybridInitProb: 0.5
  # numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["left_hand", "right_foot", "left_foot", "robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  terminationHeight: 0.8
  enableEarlyTermination: True


  random_prior: True
  # repose_z: True
  repose_z: False
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/HandAMP.yaml

```yaml
# used to create the object
name: HandAMP 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  stateInit: "Random"
  hybridInitProb: 0.5
  numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  keyBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # terminationHeight: 0.5
  enableEarlyTermination: True


  random_prior: True
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

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
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/HandAMPBase.yaml

```yaml
# used to create the object
name: HandAMPBase 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False 
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  stateInit: "Random"
  hybridInitProb: 0.5
  numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  keyBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # terminationHeight: 0.5
  enableEarlyTermination: True


  random_prior: True
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

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
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/HandAMP_backup.yaml

```yaml
# used to create the object
name: HandAMP 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  stateInit: "Random"
  hybridInitProb: 0.5
  numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  keyBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # terminationHeight: 0.5
  enableEarlyTermination: True


  random_prior: True
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

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
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
```

### isaacgymenvs/cfg/task/Humanoid copy.yaml

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

### isaacgymenvs/cfg/task/Humanoid.yaml

```yaml
# used to create the object
name: Humanoid

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
enableCameraSensors: True
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 5
  episodeLength: 300
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
  terminationHeight: 0.80

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

  localRootObs: True
  contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["right_hand", "left_hand", "right_foot", "left_foot"]
  terminationHeight: 0.5
  enableEarlyTermination: True

  # animation files to learn from
  # these motions should use hyperparameters from HumanoidAMPPPO.yaml
  # motion_file: "amp_humanoid_walk.npy"
  motion_file: "amp_humanoid_run.npy"
  #motion_file: "amp_humanoid_dance.npy"

  # these motions should use hyperparameters from HumanoidAMPPPOLowGP.yaml
  #motion_file: "amp_humanoid_hop.npy"
  #motion_file: "amp_humanoid_backflip.npy"

  asset:
    assetFileName: "mjcf/amp_humanoid.xml"
    assetRoot: "../assets"

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

### isaacgymenvs/cfg/task/HumanoidAMPBase.yaml

```yaml
# used to create the object
name: HumanoidAMPBase

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

  localRootObs: True
  contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["right_hand", "left_hand", "right_foot", "left_foot"]
  terminationHeight: 0.5
  enableEarlyTermination: True

  # animation files to learn from
  # these motions should use hyperparameters from HumanoidAMPPPO.yaml
  motion_file: "amp_humanoid_walk.npy"
  # motion_file: "amp_humanoid_run.npy"
  #motion_file: "amp_humanoid_dance.npy"

  # these motions should use hyperparameters from HumanoidAMPPPOLowGP.yaml
  #motion_file: "amp_humanoid_hop.npy"
  #motion_file: "amp_humanoid_backflip.npy"

  asset:
    assetFileName: "mjcf/amp_humanoid.xml"
    assetRoot: "../assets"

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

### isaacgymenvs/cfg/task/HumanoidCALM.yaml

```yaml
# used to create the object
name: HumanoidCALM

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
  numAMPObsSteps: 10
  numAMPEncObsSteps: 60

  localRootObs: True 
  contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["right_hand", "left_hand", "right_foot", "left_foot"]
  terminationHeight: 0.15
  enableEarlyTermination: True

  # animation files to learn from
  # these motions should use hyperparameters from HumanoidAMPPPO.yaml
  # motion_file: "amp_humanoid_walk.npy"
  motion_file: "amp_humanoid_run.npy"
  #motion_file: "amp_humanoid_dance.npy"

  # these motions should use hyperparameters from HumanoidAMPPPOLowGP.yaml
  #motion_file: "amp_humanoid_hop.npy"
  #motion_file: "amp_humanoid_backflip.npy"

  asset:
    assetFileName: "mjcf/amp_humanoid.xml"
    assetRoot: "../assets"

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

### isaacgymenvs/cfg/task/MovingArm.yaml

```yaml
# used to create the object
name: MovingArm 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 3
  episodeLength: 300
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  pdControl: False 
  powerScale: 1.0
  # controlFrequencyInv: 2 # 30 Hz
  # stateInit: "Random"
  # hybridInitProb: 0.5
  # numAMPObsSteps: 2

  localRootObs: True
  contactBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  # contactBodies: ["right_foot", "left_foot"]
  keyBodies: ["robot0:ffdistal", "robot0:mfdistal", "robot0:rfdistal", "robot0:lfdistal", "robot0:thdistal"]
  terminationHeight: 0.8
  enableEarlyTermination: True


  random_prior: True
  # repose_z: True
  repose_z: False
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
    assetRoot: "../assets/hand"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameBall: "urdf/objects/ball.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"
  
  plane:
    staticFriction: 1.0
    dynamicFriction: 1.0
    restitution: 0.0

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    

sim:
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    # solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8 # 8 bottle
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 8388608 # 8*1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 2 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75
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

### isaacgymenvs/cfg/task/ShadowHandGrasp.yaml

```yaml
# used to create the object
name: ShadowHandGrasp 

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  
  
  random_time: True
  random_prior: True
  repose_z: True
  goal_cond: False

  object_name: ''
  mocap_sv_info_fn: ''

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
    assetRoot: "../assets/hand"
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
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
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

### isaacgymenvs/cfg/task/ShadowHandManip.yaml

```yaml
# used to create the object
name: ShadowHandManip

physics_engine: ${..physics_engine}

# if given, will override the device setting in gym.
env: 
  numEnvs: 1 # ${resolve_default:4096,${...num_envs}}
  envSpacing: 1.5
  episodeLength: 200
  cameraFollow: True # if the camera follows humanoid or not
  enableDebugVis: False
  aggregateMode: 1
  

  random_prior: True
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
    assetRoot: "../assets/hand"
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
  dt: 0.0166 # 1/60 s
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
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


# ######## 20230927_037 ########
# scaled_object_asset_file: 'taco_20230927_037_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20230927_037_brush3_data_opt_tag_optrobo1.npy'


# ######## 20230930_001 ########
# scaled_object_asset_file: 'taco_20230930_001_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20230930_001_plank1_data.npy'



######## 20231031_184 ########
# scaled_object_asset_file: 'taco_20231031_184_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231031_184_hammer20231031_184_data.npy'

######## 20231031_171 ########
# scaled_object_asset_file: 'taco_20231031_171_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231031_171_hammer20231031_171_data.npy'


# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_067_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_067_shovel20231027_067_data.npy'



# ######## 20231027_067 ########
# scaled_object_asset_file: 'taco_20231027_066_wcollision.urdf'
# gt_data_fn: '/home/xueyi/diffsim/Control-VAE/ReferenceData/shadow_taco_train_split_20231027_06
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

### isaacgymenvs/cfg/task/shadow_hand_grasp.yaml

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

### isaacgymenvs/cfg/train/AntPPO.yaml

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
      units: [256, 128, 64]
      activation: elu
      d2rl: False
      
      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:Ant,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: True
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 0.01
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 3e-4
    lr_schedule: adaptive
    schedule_type: legacy
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:500,${....max_iterations}}
    save_best_after: 200
    save_frequency: 50
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 4
    critic_coef: 2
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001

```

### isaacgymenvs/cfg/train/FullBodyAMP--.yaml

```yaml
params:
  seed: -1

  algo:
    name: amp

  model:
    name: amp

  network:
    name: amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: False

  config:
    name: FullBody 
    env_name: rlgpu
    multi_gpu: False
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 2e-5
    lr_schedule: constant
    score_to_win: 20000
    max_epochs: 20000
    save_best_after: 50
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 16384
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 10
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 200000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 5
    disc_logit_reg: 0.01
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: False

    task_reward_w: 0.5
    disc_reward_w: 0.5
    # task_reward_w: 0
    # disc_reward_w: 1
```

### isaacgymenvs/cfg/train/FullBodyAMPPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:FullBodyAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
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
    learning_rate: 2e-4
    lr_schedule: adaptive
    kl_threshold: 0.008
    # learning_rate: 2e-5
    # lr_schedule: constant
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 10
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 16384
    mini_epochs: 6
    critic_coef: 5
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 200000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    # disc_coef: 5
    disc_coef: 0
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: False

    task_reward_w: 1.0
    disc_reward_w: 0.0
    # task_reward_w: 0.5
    # disc_reward_w: 0.5
    # task_reward_w: 0.0
    # disc_reward_w: 1.0

```

### isaacgymenvs/cfg/train/FullBodyENCPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: encamp

  model:
    name: continuous_a2c_logstd

  network:
    name: encamp
    separate: True 

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 612]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:Humanoid,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
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
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 10
    save_frequency: 10
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

### isaacgymenvs/cfg/train/FullBodyPPO.yaml

```yaml
params:
  seed: ${...seed}

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
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:Humanoid,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
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
    learning_rate: 2e-4
    lr_schedule: adaptive
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 10
    save_frequency: 500
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

### isaacgymenvs/cfg/train/HandAMPBasePPO.yaml

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
          val: -2.9
        fixed_sigma: True

    mlp:
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:Humanoid,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

### isaacgymenvs/cfg/train/HandAMPPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    # kl_threshold: 0.016
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    # save_best_after: 100
    # ave_frequency: 50
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    # entropy_coef: 0.0
    entropy_coef: 0.01
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    # minibatch_size: 1
    mini_epochs: 6
    critic_coef: 5
    clip_value: True
    seq_len: 4
    # bounds_loss_coef: 0.0001
    bounds_loss_coef: 0.01
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    
    amp_minibatch_size: 4096
    # amp_batch_size: 1
    # amp_minibatch_size: 1
    disc_coef: 0.1
    # disc_coef: 0.00000
    disc_logit_reg: 0.05
    # disc_grad_penalty: 5
    disc_grad_penalty: 0.2
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    task_reward_w: 0.9
    disc_reward_w: 0.1
    # task_reward_w: 1.0
    # disc_reward_w: 0.0

```

### isaacgymenvs/cfg/train/HandAMPPPO_bad.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
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
    # kl_threshold: 0.016
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    # save_best_after: 100
    # ave_frequency: 50
    save_best_after: 10
    save_frequency: 5
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 0.0001
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    # disc_coef: 0.5
    disc_coef: 0.00001
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    # task_reward_w: 0.8
    # disc_reward_w: 0.2
    task_reward_w: 1.0
    disc_reward_w: 0.0

```

### isaacgymenvs/cfg/train/HandAMPPPOnew.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    # learning_rate: 5e-5
    # lr_schedule: constant
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    # disc_coef: 0.5
    disc_coef: 0.00000
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    # task_reward_w: 0.8
    # disc_reward_w: 0.2
    task_reward_w: 1.0
    disc_reward_w: 0.000

```

### isaacgymenvs/cfg/train/HandAMPPPOnew_ok.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    # learning_rate: 5e-5
    # lr_schedule: constant
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    # disc_coef: 0.5
    disc_coef: 0.00000
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    # task_reward_w: 0.8
    # disc_reward_w: 0.2
    task_reward_w: 1.0
    disc_reward_w: 0.000

```

### isaacgymenvs/cfg/train/HandAMPPPOpre.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    # kl_threshold: 0.016
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    # save_best_after: 100
    # ave_frequency: 50
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    # entropy_coef: 0.0
    entropy_coef: 0.01
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: True
    seq_len: 4
    # bounds_loss_coef: 0.0001
    bounds_loss_coef: 0.01
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 0.01
    # disc_coef: 0.00000
    disc_logit_reg: 0.05
    # disc_grad_penalty: 5
    disc_grad_penalty: 0.2
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    # task_reward_w: 0.9
    # disc_reward_w: 0.1
    task_reward_w: 1.0
    disc_reward_w: 0.0

```

### isaacgymenvs/cfg/train/HandAMPPPOpre2.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      # units: [1024, 512, 256, 128]
      units: [400, 200, 100]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    # kl_threshold: 0.016
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    # save_best_after: 100
    # ave_frequency: 50
    save_best_after: 200
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    # entropy_coef: 0.0
    entropy_coef: 0.01
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: True
    seq_len: 4
    # bounds_loss_coef: 0.0001
    bounds_loss_coef: 0.01
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    # disc_coef: 0.0001
    disc_coef: 0.0000
    # disc_coef: 0.00000
    disc_logit_reg: 0.0001
    # disc_grad_penalty: 5
    disc_grad_penalty: 0.002
    disc_reward_scale: 0.02
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: False 

    # task_reward_w: 0.999
    # disc_reward_w: 0.000
    task_reward_w: 1.0
    disc_reward_w: 0.0

```

### isaacgymenvs/cfg/train/HumanoidAMPPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_amp

  model:
    name: humanoid_amp

  network:
    name: humanoid_amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-5
    lr_schedule: constant
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 100
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 10
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 5
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    task_reward_w: 0.0
    disc_reward_w: 1.0

```

### isaacgymenvs/cfg/train/HumanoidAMPPPOLowGP.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: amp_continuous

  model:
    name: continuous_amp

  network:
    name: amp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-5
    lr_schedule: constant
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 100
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 10
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 5
    disc_logit_reg: 0.05
    disc_grad_penalty: 0.2
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True

    task_reward_w: 0.0
    disc_reward_w: 1.0

```

### isaacgymenvs/cfg/train/HumanoidCALMPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: humanoid_calm 

  model:
    name: humanoid_calm

  network:
    name: humanoid_calm
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -2.9
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 1024, 512]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 1024, 512]
      activation: relu

      initializer:
        name: default

    conditional_disc:
      units: [ 1024, 1024, 512 ]
      activation: relu

      initializer:
        name: default

    enc:
      units: [ 1024, 1024, 512 ]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-5
    lr_schedule: constant
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 100
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 10
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 5
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    conditional_disc_coef: 5
    conditional_disc_logit_reg: 0.01
    conditional_disc_grad_penalty: 5
    conditional_disc_reward_scale: 2
    conditional_disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True
    negative_disc_samples: False

    latent_dim: 64
    latent_steps_min: 10
    latent_steps_max: 150

    task_reward_w: 0.0
    disc_reward_w: 1.0

    conditional_disc_reward_w: 1.0
    enc_regularization_coeff: 0.1

```

### isaacgymenvs/cfg/train/HumanoidENCAMPPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: encamp

  model:
    name: humanoid_amp

  network:
    name: encamp
    separate: True

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: -1.0
        fixed_sigma: True
        learn_sigma: False

    mlp:
      units: [1024, 512, 128]
      activation: relu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    disc:
      units: [1024, 512]
      activation: relu

      initializer:
        name: default

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    name: ${resolve_default:HumanoidAMP,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    ppo: True
    multi_gpu: ${....multi_gpu}
    mixed_precision: False
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-5
    lr_schedule: constant
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:5000,${....max_iterations}}
    save_best_after: 100
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 16
    minibatch_size: 32768
    mini_epochs: 6
    critic_coef: 5
    clip_value: False
    seq_len: 4
    bounds_loss_coef: 10
    amp_obs_demo_buffer_size: 200000
    amp_replay_buffer_size: 1000000
    amp_replay_keep_prob: 0.01
    amp_batch_size: 512
    amp_minibatch_size: 4096
    disc_coef: 5
    disc_logit_reg: 0.05
    disc_grad_penalty: 5
    disc_reward_scale: 2
    disc_weight_decay: 0.0001
    normalize_amp_input: True
    enable_eps_greedy: True

    task_reward_w: 0.0
    disc_reward_w: 1.0

```

### isaacgymenvs/cfg/train/HumanoidPPO.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    name: a2c_continuous
    # name: a2c_fromsupervised

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
      units: [400, 200, 100]
      # units: [ 1024, 512, 256, 128]
      # units: [2048, 1024, 512, 256, 128] # largenetv3
      # units: [4096, 2048, 1024, 512, 256, 128]
      # units: [8192, 4096, 2048, 1024, 512, 256, 128]
    
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load

  config:
    train_dir: './runs'
    log_path: './runs'
    name: ${resolve_default:Humanoid,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 50
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    # minibatch_size: 32768
    minibatch_size: 1
    # minibatch_size_per_env: 32
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

### isaacgymenvs/cfg/train/HumanoidPPOSupervised.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    # name: a2c_continuous
    name: a2c_continuous_supervised

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
      # units: [400, 200, 100]
      # units: [1024, 512, 256, 128] # largenet
      # units: [1024, 2048, 1024, 512, 256, 128] # net v1 #
      # units: [2048, 1024, 512, 256, 128] # net v2 
      # units: [4096, 2048, 1024, 512, 256, 128] # net v3  # 
      units: [8192, 4096, 2048, 1024, 512, 256, 128] # net v4 
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load


  config:

    forecasting_obs_with_original_obs: False

    history_length: 5

    target_inst_tag_list_fn: ''
    teacher_subj_idx: 2

    test_inst_tag: ''
    add_obj_features: False

    traj_idx_to_experience_sv_folder: ''
    history_chunking_obs_version: 'v1'
    load_chunking_experiences_from_real: False

    use_transformer_model: False

    ##### Hierarchical model test setting #####
    switch_between_models: False
    switch_to_trans_model_frame_after: 310
    switch_to_trans_model_ckpt_fn: ''
    ##### Hierarchical model test setting #####

    ##### action chunking #####
    action_chunking: False
    action_chunking_frames: 1
    bc_relative_targets: False
    action_chunking_skip_frames: 1

    distill_via_bc: False

    load_chunking_experiences_v2: False
    ##### action chunking #####


    save_experiences_via_ts: False
    
    load_experiences_maxx_ts: 600

    simreal_modeling: False

    # demonstration tuning model #
    demonstration_tuning_model: False
    demonstration_tuning_model_freq: 1
    distill_delta_targets: False
    record_for_distill_to_ctlv2: False

    preload_all_saved_exp_buffers: False

    bc_style_training: False

    use_no_obj_pose: False

    train_student_model: False
    ts_teacher_model_obs_dim: 731
    ts_teacher_model_weights_fn: ''

    dagger_style_training: False
    rollout_student_model: True
    rollout_teacher_model: False

    maxx_inst_nn: 100000
    
    use_world_model: False
    train_controller: False
    # train_forecasting_model: False
    forecasting_model_weight_fn: ''

    train_forecasting_model: False 
    # train_controller: False

    forecasting_obs_dim: 797
    forecasting_act_dim: 29
    forecasting_nn_frames: 10


    #### Mask mimicing training ####
    masked_mimic_training: False 
    masked_mimic_teacher_model_path: ''
    #### Mask mimicing training ####

    #### teacher model settings ####
    # use_teacher_mode # 
    # teacher_index_to_weights #
    
    w_franka: False
    teacher_model_path: ''
    teacher_index_to_weights: ''

    use_teacher_model: False
    grab_obj_type_to_opt_res_fn: ''
    taco_obj_type_to_opt_res_fn: ''
    supervised_loss_coef: 0.0005
    pure_supervised_training: False
    single_instance_tag: '' # single  # single instance tag ## 
    obj_type_to_optimized_res_fn: ''
    train_dir: './runs'
    log_path: './runs'
    training_mode: 'regular'
    record_experiences: False
    name: ${resolve_default:Humanoid,${....experiment}}
    preload_experiences_tf: False
    preload_experiences_path: None

    single_instance_training: False
    single_instance_state_based_train: False 

    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 50
    save_frequency: 200 # 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    # minibatch_size: 32768
    minibatch_size: 1
    # minibatch_size_per_env: 32
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

### isaacgymenvs/cfg/train/HumanoidPPOSupervisedChunking.yaml

```yaml
params:
  seed: ${...seed}

  algo:
    # name: a2c_continuous
    name: a2c_continuous_supervised

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
      # units: [400, 200, 100]
      # units: [1024, 512, 256, 128] # largenet
      # units: [1024, 2048, 1024, 512, 256, 128] # net v1 #
      # units: [2048, 1024, 512, 256, 128] # net v2 
      # units: [4096, 2048, 1024, 512, 256, 128] # net v3  # 
      # units: [8192, 4096, 2048, 1024, 512, 256, 128] # net v4 
      units: [8192, 4096, 2048, 1024, 512] # net v4 
      # units: [8192, 4096,] # net v4 
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load


  config:

    forecasting_obs_with_original_obs: False

    test_inst_tag: ''
    add_obj_features: False

    traj_idx_to_experience_sv_folder: ''
    history_chunking_obs_version: 'v1'
    load_chunking_experiences_from_real: False

    use_transformer_model: False

    ##### Hierarchical model test setting #####
    switch_between_models: False
    switch_to_trans_model_frame_after: 310
    switch_to_trans_model_ckpt_fn: ''
    ##### Hierarchical model test setting #####

    # demonstration tuning model #
    demonstration_tuning_model: False
    demonstration_tuning_model_freq: 1
    distill_delta_targets: False
    record_for_distill_to_ctlv2: False

    preload_all_saved_exp_buffers: False

    history_length: 5

    target_inst_tag_list_fn: ''
    teacher_subj_idx: 2

    ##### action chunking #####
    action_chunking: False
    action_chunking_frames: 1
    bc_relative_targets: False
    action_chunking_skip_frames: 1

    distill_via_bc: False

    load_chunking_experiences_v2: False
    ##### action chunking #####

    save_experiences_via_ts: False

    load_experiences_maxx_ts: 600

    simreal_modeling: False

    bc_style_training: False
    use_no_obj_pose: False

    train_student_model: False
    ts_teacher_model_obs_dim: 731
    ts_teacher_model_weights_fn: ''

    dagger_style_training: False
    rollout_student_model: True
    rollout_teacher_model: False

    maxx_inst_nn: 100000
    
    use_world_model: False
    train_controller: False
    # train_forecasting_model: False
    forecasting_model_weight_fn: ''

    train_forecasting_model: False 
    # train_controller: False

    forecasting_obs_dim: 797
    forecasting_act_dim: 29
    forecasting_nn_frames: 10


    #### Mask mimicing training ####
    masked_mimic_training: False 
    masked_mimic_teacher_model_path: ''
    #### Mask mimicing training ####

    #### teacher model settings ####
    # use_teacher_mode # 
    # teacher_index_to_weights #
    
    w_franka: False
    teacher_model_path: ''
    teacher_index_to_weights: ''

    use_teacher_model: False
    grab_obj_type_to_opt_res_fn: ''
    taco_obj_type_to_opt_res_fn: ''
    supervised_loss_coef: 0.0005
    pure_supervised_training: False
    single_instance_tag: '' # single  # single instance tag ## 
    obj_type_to_optimized_res_fn: ''
    train_dir: './runs'
    log_path: './runs'
    training_mode: 'regular'
    record_experiences: False
    name: ${resolve_default:Humanoid,${....experiment}}
    preload_experiences_tf: False
    preload_experiences_path: None

    single_instance_training: False
    single_instance_state_based_train: False 

    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    mixed_precision: True
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
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: ${resolve_default:1000,${....max_iterations}}
    save_best_after: 50
    save_frequency: 200 # 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    ppo: True
    e_clip: 0.2
    horizon_length: 32
    # minibatch_size: 32768
    minibatch_size: 1
    # minibatch_size_per_env: 32
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
```

## Python signatures and reward/observation bodies (115 files)


### isaacgymenvs/__init__.py

```
def make(seed, task, num_envs, sim_device, rl_device, graphics_device_id, headless, multi_gpu, virtual_screen_capture, force_render, cfg)
```

### isaacgymenvs/learning/a2c_dagger_continuous.py

```
def swap_and_flatten01(arr)
def rescale_actions(low, high, action)
def print_statistics(print_stats, curr_frames, step_time, step_inference_time, total_time, epoch_num, max_epochs, frame, max_frames)
class A2CBase(BaseAlgorithm)
    def __init__(self, base_name, params)
    def trancate_gradients_and_step(self)
    def load_networks(self, params)
    def write_stats(self, total_time, epoch_num, step_time, play_time, update_time, a_losses, c_losses, entropies, kls, last_lr, lr_mul, frame, scaled_time, scaled_play_time, curr_frames)
    def set_eval(self)
    def set_train(self)
    def update_lr(self, lr)
    def get_action_values(self, obs)
    def get_values(self, obs)
    def device(self)
    def reset_envs(self)
    def init_tensors(self)
    def init_rnn_from_model(self, model)
    def cast_obs(self, obs)
    def obs_to_tensors(self, obs)
    def _obs_to_tensors_internal(self, obs)
    def preprocess_actions(self, actions)
    def env_step(self, actions)
    def env_reset(self)
    def discount_values(self, fdones, last_extrinsic_values, mb_fdones, mb_extrinsic_values, mb_rewards)
    def discount_values_masks(self, fdones, last_extrinsic_values, mb_fdones, mb_extrinsic_values, mb_rewards, mb_masks)
    def clear_stats(self)
    def update_epoch(self)
    def train(self)
    def prepare_dataset(self, batch_dict)
    def train_epoch(self)
    def train_actor_critic(self, obs_dict, opt_step)
    def calc_gradients(self)
    def get_central_value(self, obs_dict)
    def train_central_value(self)
    def get_full_state_weights(self)
    def set_full_state_weights(self, weights, set_epoch)
    def set_central_value_function_weights(self, weights)
    def get_weights(self)
    def get_stats_weights(self, model_stats)
    def set_stats_weights(self, weights)
    def set_weights(self, weights)
    def get_param(self, param_name)
    def set_param(self, param_name, param_value)
    def _preproc_obs(self, obs_batch)
    def play_steps(self)
    def play_steps_rnn(self)
class DiscreteA2CBase(A2CBase)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def train_epoch(self)
    def prepare_dataset(self, batch_dict)
    def train(self)
class ContinuousA2CBase(A2CBase)
    def __init__(self, base_name, params)
    def preprocess_actions(self, actions)
    def init_tensors(self)
    def train_epoch(self)
    def prepare_dataset(self, batch_dict)
    def train(self)
class ContinuousA2CBaseDAGGER(A2CBase)
    def __init__(self, base_name, params)
    def restore(self, ckpt_path)
    def restore_expert_model(self)
    def load_network_ckpt(self, args)
    def load_student_networks(self, params)
    def preprocess_actions(self, actions)
    def init_tensors(self)
    def _preproc_obs(self, obs_batch)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def train_epoch(self)
    def train(self)
```

### isaacgymenvs/learning/a2c_fromsupervised.py

```
class A2CAgentFromSupervised(ContinuousA2CBase)
    """Continuous PPO Agent

The A2CAgent class inerits from the continuous asymmetric actor-critic class and makes modifications for PPO."""
    def __init__(self, base_name, params)
    def set_full_state_weights(self, weights, set_epoch)
    def update_epoch(self)
    def save(self, fn)
    def restore(self, fn, set_epoch)
    def restore_central_value_function(self, fn)
    def get_masked_action_values(self, obs, action_masks)
    def calc_gradients(self, input_dict)
    def train_actor_critic(self, input_dict)
    def reg_loss(self, mu)
    def bound_loss(self, mu)
```

### isaacgymenvs/learning/a2c_supervised.py

```
def swap_and_flatten01(arr)
def rescale_actions(low, high, action)
def print_statistics(print_stats, curr_frames, step_time, step_inference_time, total_time, epoch_num, max_epochs, frame, max_frames)
def batched_index_select(values, indices, dim)
class A2CSupervisedAgent(A2CAgent)
    def __init__(self, base_name, params)
    def _init_teacher_models(self)
    def _init_ts_teacher_models(self)
    def _init_multiple_teacher_models(self)
    def _init_teacher_models_single(self)
    def _init_mask_mimic_teacher_model(self)
    def _init_model_transformers(self)
    def _forward_transformer_model(self, input_dict)
    def _get_teacher_action_values(self, obs, teacher_model, teacher_model_obs_dim)
    def _get_mimic_teacher_action_values(self, obs, teacher_model)
    def build_demo_experience_buffer(self)
    def preload_demonstrations(self)
    def init_tensors(self)
    def prepare_dataset(self, batch_dict)
    def get_action_values_dagger_style(self, obs)
    def get_action_values(self, obs)
    def get_values(self, obs)
    def get_ts_teacher_action_values(self, obs, is_train)
    def play_steps_gt_dataset(self)
    def play_demo_steps(self)
    def preload_saved_experiences_chunking_bc_simdemo_dict(self, tot_preload_exp)
    def preload_saved_experiences_chunking_bc_simdemo(self)
    def preload_multiple_saved_experiences_chunking_bc_simdemo(self)
    def preload_multiple_saved_experiences_realdemo(self)
    def preload_saved_experiences_simdemo(self)
    def preload_saved_experiences_chunking_bc(self)
    def preload_saved_experiences_chunking_bc_simrealseq(self)
    def preload_all_saved_experiences(self)
    def reload_experiences(self)
    def reload_experiences_inplace(self)
    def preload_saved_experiences_multitraj_via_ts(self)
    def reload_inplace_saved_experiences_multitraj_via_ts(self)
    def preload_saved_experiences(self)
    def prepare_tsr_buffer(self)
    def play_presaved_experiences(self)
    def play_steps(self)
    def actor_loss_supervised_bak(self, pred_actions, gt_actions)
    def actor_loss_supervised(self, pred_actions, gt_actions)
    def actor_loss_mimic_teacher(self, pred_actions, gt_actions)
    def trancate_gradients_and_step_transformer(self)
    def calc_gradients(self, input_dict)
    def train_epoch(self)
    def get_weights(self)
    def train(self)
    def _build_gt_act_buffers(self)
```

### isaacgymenvs/learning/a2c_supervised_deterministic.py

```
class A2CSupervisedAgent(A2CAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def prepare_dataset(self, batch_dict)
    def get_action_values(self, obs)
    def get_values(self, obs)
    def play_steps(self)
    def actor_loss_supervised(self, pred_actions, gt_actions)
    def calc_gradients(self, input_dict)
    def train_epoch(self)
    def _build_gt_act_buffers(self)
```

### isaacgymenvs/learning/a2c_supervised_player.py

```
def rescale_actions(low, high, action)
class A2CSupervisedPlayer(BasePlayer)
    def __init__(self, params)
    def _init_model_transformers(self)
    def _build_trans_model(self)
    def _build_delta_targets_buffers(self)
    def _forward_transformer_model(self, input_dict)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
    def get_action_values(self, obs)
    def run(self)
class PpoPlayerContinuous(BasePlayer)
    def __init__(self, params)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
class PpoPlayerDiscrete(BasePlayer)
    def __init__(self, params)
    def get_masked_action(self, obs, action_masks, is_deterministic)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
class SACPlayer(BasePlayer)
    def __init__(self, params)
    def restore(self, fn)
    def get_action(self, obs, is_deterministic)
    def reset(self)
```

### isaacgymenvs/learning/a2c_supervised_v1.py

```
def swap_and_flatten01(arr)
def rescale_actions(low, high, action)
def print_statistics(print_stats, curr_frames, step_time, step_inference_time, total_time, epoch_num, max_epochs, frame, max_frames)
class A2CSupervisedAgent(A2CAgent)
    def __init__(self, base_name, params)
    def _init_teacher_models(self)
    def _init_multiple_teacher_models(self)
    def _init_teacher_models_single(self)
    def _init_mask_mimic_teacher_model(self)
    def _get_teacher_action_values(self, obs, teacher_model, teacher_model_obs_dim)
    def _get_mimic_teacher_action_values(self, obs, teacher_model)
    def build_demo_experience_buffer(self)
    def preload_demonstrations(self)
    def init_tensors(self)
    def prepare_dataset(self, batch_dict)
    def get_action_values(self, obs)
    def get_values(self, obs)
    def play_steps_gt_dataset(self)
    def play_demo_steps(self)
    def preload_saved_experiences(self)
    def play_presaved_experiences(self)
    def play_steps(self)
    def actor_loss_supervised_bak(self, pred_actions, gt_actions)
    def actor_loss_supervised(self, pred_actions, gt_actions)
    def actor_loss_mimic_teacher(self, pred_actions, gt_actions)
    def calc_gradients(self, input_dict)
    def train_epoch(self)
    def train(self)
    def _build_gt_act_buffers(self)
```

### isaacgymenvs/learning/a2c_supervised_wplanning.py

```
def swap_and_flatten01(arr)
def rescale_actions(low, high, action)
def print_statistics(print_stats, curr_frames, step_time, step_inference_time, total_time, epoch_num, max_epochs, frame, max_frames)
def unscale(x, lower, upper)
class A2CSupervisedAgentWForecasting(A2CAgent)
    def __init__(self, base_name, params)
    def set_weights(self, weights)
    def set_full_state_weights(self, weights, set_epoch)
    def _init_teacher_models(self)
    def _init_multiple_teacher_models(self)
    def _init_teacher_models_single(self)
    def _init_mask_mimic_teacher_model(self)
    def _init_forecasting_model(self)
    def _init_world_model(self)
    def _init_world_model_experience_buffer(self)
    def _get_teacher_action_values(self, obs, teacher_model, teacher_model_obs_dim)
    def _get_mimic_teacher_action_values(self, obs, teacher_model)
    def init_tensors(self)
    def prepare_dataset_forecasting(self, batch_dict)
    def prepare_dataset_world_model(self, batch_dict)
    def prepare_dataset(self, batch_dict)
    def get_action_values(self, obs)
    def get_forecasting_action_values(self, obs)
    def get_values(self, obs)
    def get_forecasting_values(self, obs)
    def play_steps(self)
    def actor_loss_supervised(self, pred_actions, gt_actions)
    def actor_loss_mimic_teacher(self, pred_actions, gt_actions)
    def calc_gradients(self, input_dict)
    def trancate_gradients_and_step(self)
    def set_train(self)
    def set_eval(self)
    def train_central_value(self)
    def update_lr(self, lr)
    def train_world_model(self, world_model_dict)
    def train_epoch(self)
    def get_weights(self)
    def train(self)
    def _build_gt_act_buffers(self)
    def _build_forecasting_module_buffers(self)
```

### isaacgymenvs/learning/a2c_supervised_wplanning_player.py

```
def rescale_actions(low, high, action)
def unscale(x, lower, upper)
class A2CSupervisedWForecastingPlayer(BasePlayer)
    def __init__(self, params)
    def obs_to_torch(self, obs)
    def _init_forecasting_model(self)
    def get_forecasting_action_values(self, obs)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
    def get_action_values(self, obs)
    def run(self)
class PpoPlayerContinuous(BasePlayer)
    def __init__(self, params)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
class PpoPlayerDiscrete(BasePlayer)
    def __init__(self, params)
    def get_masked_action(self, obs, action_masks, is_deterministic)
    def get_action(self, obs, is_deterministic)
    def restore(self, fn)
    def reset(self)
class SACPlayer(BasePlayer)
    def __init__(self, params)
    def restore(self, fn)
    def get_action(self, obs, is_deterministic)
    def reset(self)
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

### isaacgymenvs/learning/amp_continuous_dagger.py

```
class AMPAgentDAGGER(CommonAgent)
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

### isaacgymenvs/learning/detr_vae.py

```
"""DETR model and criterion classes."""
def reparametrize(mu, logvar)
def get_sinusoid_encoding_table(n_position, d_hid)
class DETRVAE(Module)
    """This is the DETR module that performs object detection """
    def __init__(self, backbones, transformer, encoder, state_dim, action_dim, num_queries, camera_names)
    def forward(self, qpos, image, env_state, actions, is_pad)
class CNNMLP(Module)
    def __init__(self, backbones, state_dim, camera_names)
    def forward(self, qpos, image, env_state, actions)
def mlp(input_dim, hidden_dim, output_dim, hidden_depth)
def build_encoder(args)
def build(args)
def build_cnnmlp(args)
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

### isaacgymenvs/learning/old/amp_agent.py

```
class AMPAgent(CommonAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def set_eval(self)
    def set_train(self)
    def get_stats_weights(self)
    def set_stats_weights(self, weights)
    def play_steps(self)
    def get_action_values(self, obs_dict, rand_action_probs)
    def prepare_dataset(self, batch_dict)
    def train_epoch(self)
    def calc_gradients(self, input_dict)
    def _load_config_params(self, config)
    def _build_net_config(self)
    def _build_rand_action_probs(self)
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
    def _calc_advs(self, batch_dict)
    def _calc_amp_rewards(self, amp_obs)
    def _calc_disc_rewards(self, amp_obs)
    def _store_replay_amp_obs(self, amp_obs)
    def _record_train_batch_info(self, batch_dict, train_info)
    def _log_train_info(self, train_info, frame)
    def _log_train_info_full(self, train_info, frame)
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

### isaacgymenvs/learning/old/amp_datasets.py

```
class AMPDataset(PPODataset)
    def __init__(self, batch_size, minibatch_size, is_discrete, is_rnn, device, seq_len)
    def update_mu_sigma(self, mu, sigma)
    def _get_item(self, idx)
    def _shuffle_idx_buf(self)
```

### isaacgymenvs/learning/old/amp_models.py

```
class ModelAMPContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/old/amp_network_builder.py

```
class AMPBuilder(A2CBuilder)
    def __init__(self)
    def build(self, name)
```

### isaacgymenvs/learning/old/amp_players.py

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
            prob = 1 / (1 + torch.exp(-disc_logits)) 
            disc_r = -torch.log(torch.maximum(1 - prob, torch.tensor(0.0001, device=self.device)))
            disc_r *= self._disc_reward_scale
        return disc_r
```
```

### isaacgymenvs/learning/old/calm_agent.py

```
class CALMAgent(AMPAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def play_steps(self)
    def get_action_values(self, obs_dict, calm_latents, rand_action_probs)
    def prepare_dataset(self, batch_dict)
    def train_epoch(self)
    def calc_gradients(self, input_dict)
    def _conditional_disc_loss(self, disc_agent_logit, disc_demo_logit, obs_hrl, calm_latents)
    def _enc_reg_loss(self)
    def env_reset(self, env_ids)
    def _reset_latent_step_count(self, env_ids)
    def _load_config_params(self, config)
    def _build_net_config(self)
    def _reset_latents(self, env_ids)
    def _sample_latents(self, n)
    def _update_latents(self)
    def _eval_actor(self, obs, calm_latents)
    def _eval_enc(self, amp_obs)
    def _eval_critic(self, obs_dict, calm_latents)
    def _calc_amp_rewards(self, amp_obs, calm_latents)
    def _calc_conditional_disc_rewards(self, amp_obs, calm_latents)
    def _eval_conditional_disc(self, amp_obs_calm, calm_latents)
    def _combine_rewards(self, task_rewards, amp_rewards)
    def _record_train_batch_info(self, batch_dict, train_info)
    def _store_replay_amp_obs(self, amp_obs, enc_amp_obs)
    def _log_train_info(self, train_info, frame)
    def _change_char_color(self, env_ids)
    def _amp_debug(self, info, calm_latents)
    def _fetch_amp_obs_demo(self, num_samples)
    def _init_amp_demo_buf(self)
    def _update_amp_demos(self)
def uniform_loss(x, t)
def align_loss(x, y, alpha)

```python
def _calc_amp_rewards(self, amp_obs, calm_latents):
        cdisc_r = self._calc_conditional_disc_rewards(amp_obs, calm_latents)
        if self._disc_reward_w <= 0:
            disc_r = torch.zeros_like(cdisc_r)
        else:
            disc_r = self._calc_disc_rewards(amp_obs)
        output = {
            'disc_rewards': disc_r,
            'conditional_disc_rewards': cdisc_r
        }
        return output
```

```python
def _calc_conditional_disc_rewards(self, amp_obs, calm_latents):
        with torch.no_grad():
            disc_logits = self._eval_conditional_disc(amp_obs, calm_latents)
            prob = 1 / (1 + torch.exp(-disc_logits))
            disc_r = -torch.log(torch.maximum(1 - prob, torch.tensor(0.0001, device=self.ppo_device)))
            disc_r *= self._conditional_disc_reward_scale

        return disc_r
```

```python
def _combine_rewards(self, task_rewards, amp_rewards):
        disc_r = amp_rewards['disc_rewards']
        conditional_disc_r = amp_rewards['conditional_disc_rewards']
        combined_rewards = self._task_reward_w * task_rewards \
                         + self._disc_reward_w * disc_r \
                         + self._conditional_disc_reward_w * conditional_disc_r
        return combined_rewards
```
```

### isaacgymenvs/learning/old/calm_models.py

```
class ModelCALMContinuous(ModelAMPContinuous)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/old/calm_network_builder.py

```
class CALMBuilder(AMPBuilder)
    def __init__(self)
    def build(self, name)
class AMPMLPNet(Module)
    def __init__(self, obs_size, ase_latent_size, units, activation, initializer)
    def forward(self, obs, latent, skip_style)
    def init_params(self)
    def get_out_size(self)
class AMPStyleCatNet1(Module)
    def __init__(self, obs_size, ase_latent_size, units, activation, style_units, style_dim, initializer)
    def forward(self, obs, latent, skip_style)
    def eval_style(self, latent)
    def init_params(self)
    def get_out_size(self)
    def _build_style_mlp(self, style_units, input_size)
```

### isaacgymenvs/learning/old/calm_players.py

```
class CALMPlayer(AMPPlayerContinuous)
    def __init__(self, params)
    def run(self)
    def _fetch_amp_obs_demo(self, num_samples)
    def get_action(self, obs_dict, is_determenistic)
    def env_reset(self, env_ids)
    def _build_net_config(self)
    def _reset_latents(self, done_env_ids)
    def _sample_latents(self, n)
    def _update_latents(self)
    def _reset_latent_step_count(self)
    def _calc_amp_rewards(self, amp_obs, calm_latents)
    def _calc_conditional_disc_rewards(self, amp_obs, calm_latents)
    def _eval_conditional_disc(self, amp_obs, calm_latents)
    def _amp_debug(self, info)
    def _change_char_color(self, env_ids)

```python
def _calc_amp_rewards(self, amp_obs, calm_latents):
        disc_r = self._calc_disc_rewards(amp_obs)
        cdisc_r = self._calc_conditional_disc_rewards(amp_obs, calm_latents)
        output = {
            'disc_rewards': disc_r,
            'conditional_disc_rewards': cdisc_r
        }
        return output
```

```python
def _calc_conditional_disc_rewards(self, amp_obs, calm_latents):
        with torch.no_grad():
            disc_logits = self._eval_conditional_disc(amp_obs, calm_latents)
            prob = 1 / (1 + torch.exp(-disc_logits))
            disc_r = -torch.log(torch.maximum(1 - prob, torch.tensor(0.0001, device=self.device)))
            disc_r *= self._conditional_disc_reward_scale

        return disc_r
```
```

### isaacgymenvs/learning/old/common_agent.py

```
class CommonAgent(A2CAgent)
    def __init__(self, base_name, params)
    def init_tensors(self)
    def train(self)
    def set_full_state_weights(self, weights)
    def train_epoch(self)
    def play_steps(self)
    def prepare_dataset(self, batch_dict)
    def calc_gradients(self, input_dict)
    def discount_values(self, mb_fdones, mb_values, mb_rewards, mb_next_values)
    def env_reset(self, env_ids)
    def bound_loss(self, mu)
    def _get_mean_rewards(self)
    def _load_config_params(self, config)
    def _build_net_config(self)
    def _setup_action_space(self)
    def _init_train(self)
    def _eval_critic(self, obs_dict)
    def _actor_loss(self, old_action_log_probs_batch, action_log_probs, advantage, curr_e_clip)
    def _critic_loss(self, value_preds_batch, values, curr_e_clip, return_batch, clip_value)
    def _calc_advs(self, batch_dict)
    def _record_train_batch_info(self, batch_dict, train_info)
    def _log_train_info(self, train_info, frame)

```python
def _get_mean_rewards(self):
        return self.game_rewards.get_mean()
```
```

### isaacgymenvs/learning/old/common_player.py

```
class CommonPlayer(PpoPlayerContinuous)
    def __init__(self, params)
    def run(self)
    def obs_to_torch(self, obs)
    def get_action(self, obs_dict, is_deterministic)
    def env_step(self, env, actions)
    def _build_net(self, config)
    def env_reset(self, env_ids)
    def _post_step(self, info)
    def _build_net_config(self)
    def _setup_action_space(self)
```

### isaacgymenvs/learning/old/encamp_agent.py

```
class ENCAMPAgent(A2CAgent)
    def __init__(self, base_name, params)
    def restore_from_partial(self, fnb, fnh)
    def restore(self, fn)
```

### isaacgymenvs/learning/old/encamp_network_builder.py

```
class ENCAMPBuilder(A2CBuilder)
    def __init__(self)
    def build(self, name)
```

### isaacgymenvs/learning/old/hrl_continuous.py

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

### isaacgymenvs/learning/old/hrl_models.py

```
class ModelHRLContinuous(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/old/replay_buffer.py

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

### isaacgymenvs/learning/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, buffer_size, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, actions, rewards, dones)
    def clear(self)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### isaacgymenvs/learning/transformer_layers.py

```
class PositionalEncoding(Module)
    def __init__(self, d_model, dropout, max_len)
    def forward(self, x)
class InputProcess(Module)
    def __init__(self, nn_latents)
    def _init_models(self)
    def forward(self, in_feats, nn_history)
class InputProcessV2(Module)
    def __init__(self, nn_latents)
    def _init_models(self)
    def forward(self, in_feats, nn_history)
class OutputProcess(Module)
    def __init__(self, nn_latents)
    def _init_models(self)
    def forward(self, in_feats)
class TransformerFeatureProcessing(Module)
    def __init__(self, nn_latents, dropout)
    def forward(self, in_feats, nn_history, nn_future)
```

### isaacgymenvs/learning/visionppo_models.py

```
class ModelVisionPPO(ModelA2CContinuousLogStd)
    def __init__(self, network)
    def build(self, config)
```

### isaacgymenvs/learning/visionppo_network_builder.py

```
class PointNetModule(Module)
    def __init__(self, output_latent_dim)
    def forward(self, pc_input)
class VisionPPOBuilder(A2CBuilder)
    def __init__(self)
    def build(self, name)
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

### isaacgymenvs/poselib/poselib/core/backend/abstract.py

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

### isaacgymenvs/poselib/poselib/core/rotation3d.py

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

### isaacgymenvs/poselib/poselib/core/tensor_utils.py

```
class TensorUtils(Serializable)
    def from_dict(cls, dict_repr)
    def to_dict(self)
def tensor_to_dict(x)
```

### isaacgymenvs/poselib/poselib/skeleton/backend/fbx/fbx_backend.py

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

### isaacgymenvs/poselib/poselib/skeleton/backend/fbx/fbx_read_wrapper.py

```
"""Script that reads in fbx files from python

This requires a configs file, which contains the command necessary to switch conda
environments to run the fbx reading script from python"""
def fbx_to_array(fbx_file_path, root_joint, fps)
```

### isaacgymenvs/poselib/poselib/skeleton/skeleton3d.py

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

### isaacgymenvs/poselib/poselib/visualization/common.py

```
def plot_skeleton_state(skeleton_state, task_name)
def plot_skeleton_states(skeleton_state, skip_n, task_name)
def plot_skeleton_motion(skeleton_motion, skip_n, task_name)
def plot_skeleton_motion_interactive_base(skeleton_motion, task_name)
def plot_skeleton_motion_interactive(skeleton_motion, task_name)
def plot_skeleton_motion_interactive_multiple()
```

### isaacgymenvs/poselib/poselib/visualization/core.py

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

### isaacgymenvs/poselib/poselib/visualization/plt_plotter.py

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

### isaacgymenvs/poselib/poselib/visualization/simple_plotter_tasks.py

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

### isaacgymenvs/poselib/poselib/visualization/skeleton_plotter_tasks.py

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

### isaacgymenvs/poselib/retarget_motion.py

```
def project_joints(motion)
def main()
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
        debug = 10
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

### isaacgymenvs/tasks/vec_task.py

```
def _create_sim_once(gym)
def batched_index_select(values, indices, dim)
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
    def num_obs_w_actions(self)
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
    def step_multisubsteps(self, actions)
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

### isaacgymenvs/test_generalist_pool.py

```
def str2bool(v)
```

### isaacgymenvs/test_pool.py

```
def str2bool(v)
```

### isaacgymenvs/train.py

```
def setup_seed(seed)
def preprocess_train_config(cfg, config_dict)
def launch_rlg_hydra(cfg)
```

### isaacgymenvs/train_2.py

```
def setup_seed(seed)
def preprocess_train_config(cfg, config_dict)
def launch_rlg_hydra(cfg)
```

### isaacgymenvs/train_pool_2.py

```
def str2bool(v)
```

### isaacgymenvs/utils/data_info.py

```
def plane2pose(plane_parameters)
def plane2euler(plane_parameters, axes)
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

### isaacgymenvs/utils/ik_utils.py

```
"""This implementation of inverse kinematics is largely based on the version from dm_control. https://github.com/google-deepmind/dm_control/blob/main/dm_control/utils/inverse_kinematics.py"""
class IKWrapper()
    def __init__(self)
    def ik_trajectory_from_T_seq(self, T_seq, start_joint_positions, verbose)
    def ik_trajectory_delta_position(self, delta_pos, start_joint_positions, num_points, verbose)
    def ik_trajectory_to_target_position(self, target_pos, start_joint_positions, num_points, verbose)
    def simulate_joint_sequence(self, joint_sequence, loop, fps, render)
    def inverse_kinematics(self, model, data, target_mat, target_pos, reset_joint_positions)
    def nullspace_method(self, jac_joints, delta, regularization_strength)
    def interpolate_dense_traj(self, joint_seq, minimal_displacement)
```

### isaacgymenvs/utils/ik_utils_1.py

```
class IKWrapper()
    def __init__(self)
    def ik_trajectory_from_T_seq(self, T_seq, start_joint_positions, verbose)
    def ik_trajectory_delta_position(self, delta_pos, start_joint_positions, num_points, verbose)
    def ik_trajectory_to_target_position(self, target_pos, start_joint_positions, num_points, verbose)
    def simulate_joint_sequence(self, joint_sequence, loop, fps, render)
    def inverse_kinematics(self, model, data, target_mat, target_pos, reset_joint_positions)
    def nullspace_method(self, jac_joints, delta, regularization_strength)
    def interpolate_dense_traj(self, joint_seq, minimal_displacement)
```

### isaacgymenvs/utils/isaac_eval_utils.py

```
def parse_obj_type_fr_folder_name(folder_nm)
def find_best_rew(folder_nm)
def get_obj_type_to_optimized_res(optimized_root_folder, prev_best_res_dict)
def find_and_save_optimized_data(optimized_data_sv_root)
def parse_time_from_folder_name(folder_nm)
def find_and_save_test_files(optimized_data_sv_root)
```

### isaacgymenvs/utils/motion_lib.py

```
class DeviceCache()
    def __init__(self, obj, device)
    def __getattr__(self, string)
class LoadedMotions(Module)
    """Tuples here needed so the class can hash, which is
needed so the module can be iterated over in a parent
module's children."""
    def __init__(self, motions, motion_lengths, motion_weights, motion_fps, motion_dt, motion_num_frames, motion_files)
class MotionLib(DeviceDtypeModuleMixin)
    def __init__(self, motion_file, dof_body_ids, dof_offsets, key_body_ids, equal_motion_weights, device)
    def num_motions(self)
    def get_total_length(self)
    def get_motion(self, motion_id)
    def sample_motions(self, n)
    def sample_time(self, motion_ids, truncate_time)
    def sample_nearby_time(self, motion_ids, motion_time, time_delta, truncate_time)
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
class RLGPUEnv_old(IVecEnv)
    def __init__(self, config_name, num_actors)
    def step(self, actions)
    def reset(self)
    def reset_done(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
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
class AMPRLGPUEnv(IVecEnv)
    def __init__(self, config_name, num_actors)
    def step(self, actions)
    def reset(self, env_ids)
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

### isaacgymenvs/utils/torch_utils.py

```
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