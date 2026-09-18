# diffusion_policy_2023

source: https://github.com/real-stanford/diffusion_policy


commit: 5ba07ac6661db573af695b419a7947ecb704690f


## README

# Diffusion Policy

[[Project page]](https://diffusion-policy.cs.columbia.edu/)
[[Paper]](https://diffusion-policy.cs.columbia.edu/#paper)
[[Data]](https://diffusion-policy.cs.columbia.edu/data/)
[[Colab (state)]](https://colab.research.google.com/drive/1gxdkgRVfM55zihY9TFLja97cSVZOZq2B?usp=sharing)
[[Colab (vision)]](https://colab.research.google.com/drive/18GIHeOQ5DyjMN8iIRZL2EKZ0745NLIpg?usp=sharing)


[Cheng Chi](http://cheng-chi.github.io/)<sup>1</sup>,
[Siyuan Feng](https://www.cs.cmu.edu/~sfeng/)<sup>2</sup>,
[Yilun Du](https://yilundu.github.io/)<sup>3</sup>,
[Zhenjia Xu](https://www.zhenjiaxu.com/)<sup>1</sup>,
[Eric Cousineau](https://www.eacousineau.com/)<sup>2</sup>,
[Benjamin Burchfiel](http://www.benburchfiel.com/)<sup>2</sup>,
[Shuran Song](https://www.cs.columbia.edu/~shurans/)<sup>1</sup>

<sup>1</sup>Columbia University,
<sup>2</sup>Toyota Research Institute,
<sup>3</sup>MIT

<img src="media/teaser.png" alt="drawing" width="100%"/>
<img src="media/multimodal_sim.png" alt="drawing" width="100%"/>

## 🛝 Try it out!
Our self-contained Google Colab notebooks is the easiest way to play with Diffusion Policy. We provide separate notebooks for  [state-based environment](https://colab.research.google.com/drive/1gxdkgRVfM55zihY9TFLja97cSVZOZq2B?usp=sharing) and [vision-based environment](https://colab.research.google.com/drive/18GIHeOQ5DyjMN8iIRZL2EKZ0745NLIpg?usp=sharing).

## 🧾 Checkout our experiment logs!
For each experiment used to generate Table I,II and IV in the [paper](https://diffusion-policy.cs.columbia.edu/#paper), we provide:
1. A `config.yaml` that contains all parameters needed to reproduce the experiment.
2. Detailed training/eval `logs.json.txt` for every training step.
3. Checkpoints for the best `epoch=*-test_mean_score=*.ckpt` and last `latest.ckpt` epoch of each run.

Experiment logs are hosted on our website as nested directories in format:
`https://diffusion-policy.cs.columbia.edu/data/experiments/<image|low_dim>/<task>/<method>/`

Within each experiment directory you may find:
```
.
├── config.yaml
├── metrics
│   └── logs.json.txt
├── train_0
│   ├── checkpoints
│   │   ├── epoch=0300-test_mean_score=1.000.ckpt
│   │   └── latest.ckpt
│   └── logs.json.txt
├── train_1
│   ├── checkpoints
│   │   ├── epoch=0250-test_mean_score=1.000.ckpt
│   │   └── latest.ckpt
│   └── logs.json.txt
└── train_2
    ├── checkpoints
    │   ├── epoch=0250-test_mean_score=1.000.ckpt
    │   └── latest.ckpt
    └── logs.json.txt
```
The `metrics/logs.json.txt` file aggregates evaluation metrics from all 3 training runs every 50 epochs using `multirun_metrics.py`. The numbers reported in the paper correspond to `max` and `k_min_train_loss` aggregation keys.

To download all files in a subdirectory, use:

```console
$ wget --recursive --no-parent --no-host-directories --relative --reject="index.html*" https://diffusion-policy.cs.columbia.edu/data/experiments/low_dim/square_ph/diffusion_policy_cnn/
```

## 🛠️ Installation
### 🖥️ Simulation
To reproduce our simulation benchmark results, install our conda environment on a Linux machine with Nvidia GPU. On Ubuntu 20.04 you need to install the following apt packages for mujoco:
```console
$ sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
```

We recommend [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) instead of the standard anaconda distribution for faster installation: 
```console
$ mamba env create -f conda_environment.yaml
```

but you can use conda as well: 
```console
$ conda env create -f conda_environment.yaml
```

The `conda_environment_macos.yaml` file is only for development on MacOS and does not have full support for benchmarks.

### 🦾 Real Robot
Hardware (for Push-T):
* 1x [UR5-CB3](https://www.universal-robots.com/cb3) or [UR5e](https://www.universal-robots.com/products/ur5-robot/) ([RTDE Interface](https://www.universal-robots.com/articles/ur/interface-communication/real-time-data-exchange-rtde-guide/) is required)
* 2x [RealSense D415](https://www.intelrealsense.com/depth-camera-d415/)
* 1x [3Dconnexion SpaceMouse](https://3dconnexion.com/us/product/spacemouse-wireless/) (for teleop)
* 1x [Millibar Robotics Manual Tool Changer](https://www.millibar.com/manual-tool-changer/) (only need robot side)
* 1x 3D printed [End effector](https://cad.onshape.com/documents/a818888644a15afa6cc68ee5/w/2885b48b018cda84f425beca/e/3e8771c2124cee024edd2fed?renderMode=0&uiState=63ffcba6631ca919895e64e5)
* 1x 3D printed [T-block](https://cad.onshape.com/documents/f1140134e38f6ed6902648d5/w/a78cf81827600e4ff4058d03/e/f35f57fb7589f72e05c76caf?renderMode=0&uiState=63ffcbc9af4a881b344898ee)
* USB-C cables and screws for RealSense

Software:
* Ubuntu 20.04.3 (tested)
* Mujoco dependencies: 
`sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf`
* [RealSense SDK](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)
* Spacemouse dependencies: 
`sudo apt install libspnav-dev spacenavd; sudo systemctl start spacenavd`
* Conda environment `mamba env create -f conda_environment_real.yaml`

## 🖥️ Reproducing Simulation Benchmark Results 
### Download Training Data
Under the repo root, create data subdirectory:
```console
[diffusion_policy]$ mkdir data && cd data
```

Download the corresponding zip file from [https://diffusion-policy.cs.columbia.edu/data/training/](https://diffusion-policy.cs.columbia.edu/data/training/)
```console
[data]$ wget https://diffusion-policy.cs.columbia.edu/data/training/pusht.zip
```

Extract training data:
```console
[data]$ unzip pusht.zip && rm -f pusht.zip && cd ..
```

Grab config file for the corresponding experiment:
```console
[diffusion_policy]$ wget -O image_pusht_diffusion_policy_cnn.yaml https://diffusion-policy.cs.columbia.edu/data/experiments/image/pusht/diffusion_policy_cnn/config.yaml
```

### Running for a single seed
Activate conda environment and login to [wandb](https://wandb.ai) (if you haven't already).
```console
[diffusion_policy]$ conda activate robodiff
(robodiff)[diffusion_policy]$ wandb login
```

Launch training with seed 42 on GPU 0.
```console
(robodiff)[diffusion_policy]$ python train.py --config-dir=. --config-name=image_pusht_diffusion_policy_cnn.yaml training.seed=42 training.device=cuda:0 hydra.run.dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}'
```

This will create a directory in format `data/outputs/yyyy.mm.dd/hh.mm.ss_<method_name>_<task_name>` where configs, logs and checkpoints are written to. The policy will be evaluated every 50 epochs with the success rate logged as `test/mean_score` on wandb, as well as videos for some rollouts.
```console
(robodiff)[diffusion_policy]$ tree data/outputs/2023.03.01/20.02.03_train_diffusion_unet_hybrid_pusht_image -I wandb
data/outputs/2023.03.01/20.02.03_train_diffusion_unet_hybrid_pusht_image
├── checkpoints
│   ├── epoch=0000-test_mean_score=0.134.ckpt
│   └── latest.ckpt
├── .hydra
│   ├── config.yaml
│   ├── hydra.yaml
│   └── overrides.yaml
├── logs.json.txt
├── media
│   ├── 2k5u6wli.mp4
│   ├── 2kvovxms.mp4
│   ├── 2pxd9f6b.mp4
│   ├── 2q5gjt5f.mp4
│   ├── 2sawbf6m.mp4
│   └── 538ubl79.mp4
└── train.log

3 directories, 13 files
```

### Running for multiple seeds
Launch local ray cluster. For large scale experiments, you might want to setup an [AWS cluster with autoscaling](https://docs.ray.io/en/master/cluster/vms/user-guides/launching-clusters/aws.html). All other commands remain the same.
```console
(robodiff)[diffusion_policy]$ export CUDA_VISIBLE_DEVICES=0,1,2  # select GPUs to be managed by the ray cluster
(robodiff)[diffusion_policy]$ ray start --head --num-gpus=3
```

Launch a ray client which will start 3 training workers (3 seeds) and 1 metrics monitor worker.
```console
(robodiff)[diffusion_policy]$ python ray_train_multirun.py --config-dir=. --config-name=image_pusht_diffusion_policy_cnn.yaml --seeds=42,43,44 --monitor_key=test/mean_score -- multi_run.run_dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}' multi_run.wandb_name_base='${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}'
```

In addition to the wandb log written by each training worker individually, the metrics monitor worker will log to wandb project `diffusion_policy_metrics` for the metrics aggregated from all 3 training runs. Local config, logs and checkpoints will be written to `data/outputs/yyyy.mm.dd/hh.mm.ss_<method_name>_<task_name>` in a directory structure identical to our [training logs](https://diffusion-policy.cs.columbia.edu/data/experiments/):
```console
(robodiff)[diffusion_policy]$ tree data/outputs/2023.03.01/22.13.58_train_diffusion_unet_hybrid_pusht_image -I 'wandb|media'
data/outputs/2023.03.01/22.13.58_train_diffusion_unet_hybrid_pusht_image
├── config.yaml
├── metrics
│   ├── logs.json.txt
│   ├── metrics.json
│   └── metrics.log
├── train_0
│   ├── checkpoints
│   │   ├── epoch=0000-test_mean_score=0.174.ckpt
│   │   └── latest.ckpt
│   ├── logs.json.txt
│   └── train.log
├── train_1
│   ├── checkpoints
│   │   ├── epoch=0000-test_mean_score=0.131.ckpt
│   │   └── latest.ckpt
│   ├── logs.json.txt
│   └── train.log
└── train_2
    ├── checkpoints
    │   ├── epoch=0000-test_mean_score=0.105.ckpt
    │   └── latest.ckpt
    ├── logs.json.txt
    └── train.log

7 directories, 16 files
```
### 🆕 Evaluate Pre-trained Checkpoints
Download a checkpoint from the published training log folders, such as [https://diffusion-policy.cs.columbia.edu/data/experiments/low_dim/pusht/diffusion_policy_cnn/train_0/checkpoints/epoch=0550-test_mean_score=0.969.ckpt](https://diffusion-policy.cs.columbia.edu/data/experiments/low_dim/pusht/diffusion_policy_cnn/train_0/checkpoints/epoch=0550-test_mean_score=0.969.ckpt).

Run the evaluation script:
```console
(robodiff)[diffusion_policy]$ python eval.py --checkpoint data/0550-test_mean_score=0.969.ckpt --output_dir data/pusht_eval_output --device cuda:0
```

This will generate the following directory structure:
```console
(robodiff)[diffusion_policy]$ tree data/pusht_eval_output
data/pusht_eval_output
├── eval_log.json
└── media
    ├── 1fxtno84.mp4
    ├── 224l7jqd.mp4
    ├── 2fo4btlf.mp4
    ├── 2in4cn7a.mp4
    ├── 34b3o2qq.mp4
    └── 3p7jqn32.mp4

1 directory, 7 files
```

`eval_log.json` contains metrics that is logged to wandb during training:
```console
(robodiff)[diffusion_policy]$ cat data/pusht_eval_output/eval_log.json
{
  "test/mean_score": 0.9150393806777066,
  "test/sim_max_reward_4300000": 1.0,
  "test/sim_max_reward_4300001": 0.9872969750774386,
...
  "train/sim_video_1": "data/pusht_eval_output//media/2fo4btlf.mp4"
}
```

## 🦾 Demo, Training and Eval on a Real Robot
Make sure your UR5 robot is running and accepting command from its network interface (emergency stop button within reach at all time), your RealSense cameras plugged in to your workstation (tested with `realsense-viewer`) and your SpaceMouse connected with the `spacenavd` daemon running (verify with `systemctl status spacenavd`).

Start the demonstration collection script. Press "C" to start recording. Use SpaceMouse to move the robot. Press "S" to stop recording. 
```console
(robodiff)[diffusion_policy]$ python demo_real_robot.py -o data/demo_pusht_real --robot_ip 192.168.0.204
```

This should result in a demonstration dataset in `data/demo_pusht_real` with in the same structure as our example [real Push-T training dataset](https://diffusion-policy.cs.columbia.edu/data/training/pusht_real.zip).

To train a Diffusion Policy, launch training with config:
```console
(robodiff)[diffusion_policy]$ python train.py --config-name=train_diffusion_unet_real_image_workspace task.dataset_path=data/demo_pusht_real
```
Edit [`diffusion_policy/config/task/real_pusht_image.yaml`](./diffusion_policy/config/task/real_pusht_image.yaml) if your camera setup is different.

Assuming the training has finished and you have a checkpoint at `data/outputs/blah/checkpoints/latest.ckpt`, launch the evaluation script with:
```console
python eval_real_robot.py -i data/outputs/blah/checkpoints/latest.ckpt -o data/eval_pusht_real --robot_ip 192.168.0.204
```
Press "C" to start evaluation (handing control over to the policy). Press "S" to stop the current episode.

## 🗺️ Codebase Tutorial
This codebase is structured under the requirement that:
1. implementing `N` tasks and `M` methods will only require `O(N+M)` amount of code instead of `O(N*M)`
2. while retaining maximum flexibility.

To achieve this requirement, we 
1. maintained a simple unified interface between tasks and methods and 
2. made the implementation of the tasks and the methods independent of each other. 

These design decisions come at the cost of code repetition between the tasks and the methods. However, we believe that the benefit of being able to add/modify task/methods without affecting the remainder and being able understand a task/method by reading the code linearly outweighs the cost of copying and pasting 😊.

### The Split
On the task side, we have:
* `Dataset`: adapts a (third-party) dataset to the interface.
* `EnvRunner`: executes a `Policy` that accepts the interface and produce logs and metrics.
* `config/task/<task_name>.yaml`: contains all information needed to construct `Dataset` and `EnvRunner`.
* (optional) `Env`: an `gym==0.21.0` compatible class that encapsulates the task environment.

On the policy side, we have:
* `Policy`: implements inference according to the interface and part of the training process.
* `Workspace`: manages the life-cycle of training and evaluation (interleaved) of a method. 
* `config/<workspace_name>.yaml`: contains all information needed to construct `Policy` and `Workspace`.

### The Interface
#### Low Dim
A [`LowdimPolicy`](./diffusion_policy/policy/base_lowdim_policy.py) takes observation dictionary:
- `"obs":` Tensor of shape `(B,To,Do)`

and predicts action dictionary:
- `"action": ` Tensor of shape `(B,Ta,Da)`

A [`LowdimDataset`](./diffusion_policy/dataset/base_dataset.py) returns a sample of dictionary:
- `"obs":` Tensor of shape `(To, Do)`
- `"action":` Tensor of shape `(Ta, Da)`

Its `get_normalizer` method returns a [`LinearNormalizer`](./diffusion_policy/model/common/normalizer.py) with keys `"obs","action"`.

The `Policy` handles normalization on GPU with its copy of the `LinearNormalizer`. The parameters of the `LinearNormalizer` is saved as part of the `Policy`'s weights checkpoint.

#### Image
A [`ImagePolicy`](./diffusion_policy/policy/base_image_policy.py) takes observation dictionary:
- `"key0":` Tensor of shape `(B,To,*)`
- `"key1":` Tensor of shape e.g. `(B,To,H,W,3)` ([0,1] float32)

and predicts action dictionary:
- `"action": ` Tensor of shape `(B,Ta,Da)`

A [`ImageDataset`](./diffusion_policy/dataset/base_dataset.py) returns a sample of dictionary:
- `"obs":` Dict of
    - `"key0":` Tensor of shape `(To, *)`
    - `"key1":` Tensor fo shape `(To,H,W,3)`
- `"action":` Tensor of shape `(Ta, Da)`

Its `get_normalizer` method returns a [`LinearNormalizer`](./diffusion_policy/model/common/normalizer.py) with keys `"key0","key1","action"`.

#### Example
```
To = 3
Ta = 4
T = 6
|o|o|o|
| | |a|a|a|a|
|o|o|
| |a|a|a|a|a|
| | | | |a|a|
```
Terminology in the paper: `varname` in the codebase
- Observation Horizon: `To|n_obs_steps`
- Action Horizon: `Ta|n_action_steps`
- Prediction Horizon: `T|horizon`

The classical (e.g. MDP) single step observation/action formulation is included as a special case where `To=1` and `Ta=1`.

## 🔩 Key Components
### `Workspace`
A `Workspace` object encapsulates all states and code needed to run an experiment. 
* Inherits from [`BaseWorkspace`](./diffusion_policy/workspace/base_workspace.py).
* A single `OmegaConf` config object generated by `hydra` should contain all information needed to construct the Workspace object and running experiments. This config correspond to `config/<workspace_name>.yaml` + hydra overrides.
* The `run` method contains the entire pipeline for the experiment.
* Checkpoints happen at the `Workspace` level. All training states implemented as object attributes are automatically saved by the `save_checkpoint` method.
* All other states for the experiment should be implemented as local variables in the `run` method.

The entrypoint for training is `train.py` which uses `@hydra.main` decorator. Read [hydra](https://hydra.cc/)'s official documentation for command line arguments and config overrides. For example, the argument `task=<task_name>` will replace the `task` subtree of the config with the content of `config/task/<task_name>.yaml`, thereby selecting the task to run for this experiment.

### `Dataset`
A `Dataset` object:
* Inherits from `torch.utils.data.Dataset`.
* Returns a sample conforming to [the interface](#the-interface) depending on whether the task has Low Dim or Image observations.
* Has a method `get_normalizer` that returns a `LinearNormalizer` conforming to [the interface](#the-interface).

Normalization is a very common source of bugs during project development. It is sometimes helpful to print out the specific `scale` and `bias` vectors used for each key in the `LinearNormalizer`.

Most of our implementations of `Dataset` uses a combination of [`ReplayBuffer`](#replaybuffer) and [`SequenceSampler`](./diffusion_policy/common/sampler.py) to generate samples. Correctly handling padding at the beginning and the end of each demonstration episode according to `To` and `Ta` is important for good performance. Please read our [`SequenceSampler`](./diffusion_policy/common/sampler.py) before implementing your own sampling method.

### `Policy`
A `Policy` object:
* Inherits from `BaseLowdimPolicy` or `BaseImagePolicy`.
* Has a method `predict_action` that given observation dict, predicts actions conforming to [the interface](#the-interface).
* Has a method `set_normalizer` that takes in a `LinearNormalizer` and handles observation/action normalization internally in the policy.
* (optional) Might has a method `compute_loss` that takes in a batch and returns the loss to be optimized.
* (optional) Usually each `Policy` class correspond to a `Workspace` class due to the differences of training and evaluation process between methods.

### `EnvRunner`
A `EnvRunner` object abstracts away the subtle differences between different task environments.
* Has a method `run` that takes a `Policy` object for evaluation, and returns a dict of logs and metrics. Each value should be compatible with `wandb.log`. 

To maximize evaluation speed, we usually vectorize environments using our modification of [`gym.vector.AsyncVectorEnv`](./diffusion_policy/gym_util/async_vector_env.py) which runs each individual environment in a separate process (workaround python GIL). 

⚠️ Since subprocesses are launched using `fork` on linux, you need to be specially careful for environments that creates its OpenGL context during initialization (e.g. robosuite) which, once inherited by the child process memory space, often causes obscure bugs like segmentation fault. As a workaround, you can provide a `dummy_env_fn` that constructs an environment without initializing OpenGL.

### `ReplayBuffer`
The [`ReplayBuffer`](./diffusion_policy/common/replay_buffer.py) is a key data structure for storing a demonstration dataset both in-memory and on-disk with chunking and compression. It makes heavy use of the [`zarr`](https://zarr.readthedocs.io/en/stable/index.html) format but also has a `numpy` backend for lower access overhead.

On disk, it can be stored as a nested directory (e.g. `data/pusht_cchi_v7_replay.zarr`) or a zip file (e.g. `data/robomimic/datasets/square/mh/image_abs.hdf5.zarr.zip`).

Due to the relative small size of our datasets, it's often possible to store the entire image-based dataset in RAM with [`Jpeg2000` compression](./diffusion_policy/codecs/imagecodecs_numcodecs.py) which eliminates disk IO during training at the expense increasing of CPU workload.

Example:
```
data/pusht_cchi_v7_replay.zarr
 ├── data
 │   ├── action (25650, 2) float32
 │   ├── img (25650, 96, 96, 3) float32
 │   ├── keypoint (25650, 9, 2) float32
 │   ├── n_contacts (25650, 1) float32
 │   └── state (25650, 5) float32
 └── meta
     └── episode_ends (206,) int64
```

Each array in `data` stores one data field from all episodes concatenated along the first dimension (time). The `meta/episode_ends` array stores the end index for each episode along the fist dimension.

### `SharedMemoryRingBuffer`
The [`SharedMemoryRingBuffer`](./diffusion_policy/shared_memory/shared_memory_ring_buffer.py) is a lock-free FILO data structure used extensively in our [real robot implementation](./diffusion_policy/real_world) to utilize multiple CPU cores while avoiding pickle serialization and locking overhead for `multiprocessing.Queue`. 

As an example, we would like to get the most recent `To` frames from 5 RealSense cameras. We launch 1 realsense SDK/pipeline per process using [`SingleRealsense`](./diffusion_policy/real_world/single_realsense.py), each continuously writes the captured images into a `SharedMemoryRingBuffer` shared with the main process. We can very quickly get the last `To` frames in the main process due to the FILO nature of `SharedMemoryRingBuffer`.

We also implemented [`SharedMemoryQueue`](./diffusion_policy/shared_memory/shared_memory_queue.py) for FIFO, which is used in [`RTDEInterpolationController`](./diffusion_policy/real_world/rtde_interpolation_controller.py).

### `RealEnv`
In contrast to [OpenAI Gym](https://gymnasium.farama.org/), our polices interact with the environment asynchronously. In [`RealEnv`](./diffusion_policy/real_world/real_env.py), the `step` method in `gym` is split into two methods: `get_obs` and `exec_actions`. 

The `get_obs` method returns the latest observation from `SharedMemoryRingBuffer` as well as their corresponding timestamps. This method can be call at any time during an evaluation episode.

The `exec_actions` method accepts a sequence of actions and timestamps for the expected time of execution for each step. Once called, the actions are simply enqueued to the `RTDEInterpolationController`, and the method returns without blocking for execution.

## 🩹 Adding a Task
Read and imitate:
* `diffusion_policy/dataset/pusht_image_dataset.py`
* `diffusion_policy/env_runner/pusht_image_runner.py`
* `diffusion_policy/config/task/pusht_image.yaml`

Make sure that `shape_meta` correspond to input and output shapes for your task. Make sure `env_runner._target_` and `dataset._target_` point to the new classes you have added. When training, add `task=<your_task_name>` to `train.py`'s arguments.

## 🩹 Adding a Method
Read and imitate:
* `diffusion_policy/workspace/train_diffusion_unet_image_workspace.py`
* `diffusion_policy/policy/diffusion_unet_image_policy.py`
* `diffusion_policy/config/train_diffusion_unet_image_workspace.yaml`

Make sure your workspace yaml's `_target_` points to the new workspace class you created.

## 🏷️ License
This repository is released under the MIT license. See [LICENSE](LICENSE) for additional details.

## 🙏 Acknowledgement
* Our [`ConditionalUnet1D`](./diffusion_policy/model/diffusion/conditional_unet1d.py) implementation is adapted from [Planning with Diffusion](https://github.com/jannerm/diffuser).
* Our [`TransformerForDiffusion`](./diffusion_policy/model/diffusion/transformer_for_diffusion.py) implementation is adapted from [MinGPT](https://github.com/karpathy/minGPT).
* The [BET](./diffusion_policy/model/bet) baseline is adapted from [its original repo](https://github.com/notmahi/bet).
* The [IBC](./diffusion_policy/policy/ibc_dfo_lowdim_policy.py) baseline is adapted from [Kevin Zakka's reimplementation](https://github.com/kevinzakka/ibc).
* The [Robomimic](https://github.com/ARISE-Initiative/robomimic) tasks and [`ObservationEncoder`](https://github.com/ARISE-Initiative/robomimic/blob/master/robomimic/models/obs_nets.py) are used extensively in this project.
* The [Push-T](./diffusion_policy/env/pusht) task is adapted from [IBC](https://github.com/google-research/ibc).
* The [Block Pushing](./diffusion_policy/env/block_pushing) task is adapted from [BET](https://github.com/notmahi/bet) and [IBC](https://github.com/google-research/ibc).
* The [Kitchen](./diffusion_policy/env/kitchen) task is adapted from [BET](https://github.com/notmahi/bet) and [Relay Policy Learning](https://github.com/google-research/relay-policy-learning).
* Our [shared_memory](./diffusion_policy/shared_memory) data structures are heavily inspired by [shared-ndarray2](https://gitlab.com/osu-nrsg/shared-ndarray2).


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
conda_environment.yaml
conda_environment_macos.yaml
conda_environment_real.yaml
demo_pusht.py
demo_real_robot.py
diffusion_policy/
  codecs/
    imagecodecs_numcodecs.py
  common/
    checkpoint_util.py
    cv2_util.py
    env_util.py
    json_logger.py
    nested_dict_util.py
    normalize_util.py
    pose_trajectory_interpolator.py
    precise_sleep.py
    pymunk_override.py
    pymunk_util.py
    pytorch_util.py
    replay_buffer.py
    robomimic_config_util.py
    robomimic_util.py
    sampler.py
    timestamp_accumulator.py
  config/
    task/
    train_bet_lowdim_workspace.yaml
    train_diffusion_transformer_hybrid_workspace.yaml
    train_diffusion_transformer_lowdim_kitchen_workspace.yaml
    train_diffusion_transformer_lowdim_pusht_workspace.yaml
    train_diffusion_transformer_lowdim_workspace.yaml
    train_diffusion_transformer_real_hybrid_workspace.yaml
    train_diffusion_unet_ddim_hybrid_workspace.yaml
    train_diffusion_unet_ddim_lowdim_workspace.yaml
    train_diffusion_unet_hybrid_workspace.yaml
    train_diffusion_unet_image_pretrained_workspace.yaml
    train_diffusion_unet_image_workspace.yaml
    train_diffusion_unet_lowdim_workspace.yaml
    train_diffusion_unet_real_hybrid_workspace.yaml
    train_diffusion_unet_real_image_workspace.yaml
    train_diffusion_unet_real_pretrained_workspace.yaml
    train_diffusion_unet_video_workspace.yaml
    train_ibc_dfo_hybrid_workspace.yaml
    train_ibc_dfo_lowdim_workspace.yaml
    train_ibc_dfo_real_hybrid_workspace.yaml
    train_robomimic_image_workspace.yaml
    train_robomimic_lowdim_workspace.yaml
    train_robomimic_real_image_workspace.yaml
  dataset/
    base_dataset.py
    blockpush_lowdim_dataset.py
    kitchen_lowdim_dataset.py
    kitchen_mjl_lowdim_dataset.py
    mujoco_image_dataset.py
    pusht_dataset.py
    pusht_image_dataset.py
    real_pusht_image_dataset.py
    robomimic_replay_image_dataset.py
    robomimic_replay_lowdim_dataset.py
  env/
    block_pushing/
    kitchen/
    pusht/
    robomimic/
  env_runner/
    base_image_runner.py
    base_lowdim_runner.py
    blockpush_lowdim_runner.py
    kitchen_lowdim_runner.py
    pusht_image_runner.py
    pusht_keypoints_runner.py
    real_pusht_image_runner.py
    robomimic_image_runner.py
    robomimic_lowdim_runner.py
  gym_util/
    async_vector_env.py
    multistep_wrapper.py
    sync_vector_env.py
    video_recording_wrapper.py
    video_wrapper.py
  model/
    bet/
    common/
    diffusion/
    vision/
  policy/
    base_image_policy.py
    base_lowdim_policy.py
    bet_lowdim_policy.py
    diffusion_transformer_hybrid_image_policy.py
    diffusion_transformer_lowdim_policy.py
    diffusion_unet_hybrid_image_policy.py
    diffusion_unet_image_policy.py
    diffusion_unet_lowdim_policy.py
    diffusion_unet_video_policy.py
    ibc_dfo_hybrid_image_policy.py
    ibc_dfo_lowdim_policy.py
    robomimic_image_policy.py
    robomimic_lowdim_policy.py
  real_world/
    keystroke_counter.py
    multi_camera_visualizer.py
    multi_realsense.py
    real_data_conversion.py
    real_env.py
    real_inference_util.py
    realsense_config/
    rtde_interpolation_controller.py
    single_realsense.py
    spacemouse.py
    spacemouse_shared_memory.py
    video_recorder.py
  scripts/
    bet_blockpush_conversion.py
    blockpush_abs_conversion.py
    episode_lengths.py
    generate_bet_blockpush.py
    real_dataset_conversion.py
    real_pusht_metrics.py
    real_pusht_successrate.py
    robomimic_dataset_action_comparison.py
    robomimic_dataset_conversion.py
  shared_memory/
    shared_memory_queue.py
    shared_memory_ring_buffer.py
    shared_memory_util.py
    shared_ndarray.py
  workspace/
    base_workspace.py
    train_bet_lowdim_workspace.py
    train_diffusion_transformer_hybrid_workspace.py
    train_diffusion_transformer_lowdim_workspace.py
    train_diffusion_unet_hybrid_workspace.py
    train_diffusion_unet_image_workspace.py
    train_diffusion_unet_lowdim_workspace.py
    train_diffusion_unet_video_workspace.py
    train_ibc_dfo_hybrid_workspace.py
    train_ibc_dfo_lowdim_workspace.py
    train_robomimic_image_workspace.py
    train_robomimic_lowdim_workspace.py
eval.py
eval_real_robot.py
image_pusht_diffusion_policy_cnn.yaml
multirun_metrics.py
pyrightconfig.json
ray_exec.py
ray_train_multirun.py
setup.py
tests/
  test_block_pushing.py
  test_cv2_util.py
  test_multi_realsense.py
  test_pose_trajectory_interpolator.py
  test_precise_sleep.py
  test_replay_buffer.py
  test_ring_buffer.py
  test_robomimic_image_runner.py
  test_robomimic_lowdim_runner.py
  test_shared_queue.py
  test_single_realsense.py
  test_timestamp_accumulator.py
train.py
```

## Config files (53)


### conda_environment.yaml

```yaml
name: robodiff
channels:
  - pytorch
  - pytorch3d
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - pip=22.2.2
  - cudatoolkit=11.6
  - pytorch=1.12.1
  - torchvision=0.13.1
  - pytorch3d=0.7.0
  - numpy=1.23.3
  - numba==0.56.4
  - scipy==1.9.1
  - py-opencv=4.6.0
  - cffi=1.15.1
  - ipykernel=6.16
  - matplotlib=3.6.1
  - zarr=2.12.0
  - numcodecs=0.10.2
  - h5py=3.7.0
  - hydra-core=1.2.0
  - einops=0.4.1
  - tqdm=4.64.1
  - dill=0.3.5.1
  - scikit-video=1.1.11
  - scikit-image=0.19.3
  - gym=0.21.0
  - pymunk=6.2.1
  - wandb=0.13.3
  - threadpoolctl=3.1.0
  - shapely=1.8.4
  - cython=0.29.32
  - imageio=2.22.0
  - imageio-ffmpeg=0.4.7
  - termcolor=2.0.1
  - tensorboard=2.10.1
  - tensorboardx=2.5.1
  - psutil=5.9.2
  - click=8.0.4
  - boto3=1.24.96
  - accelerate=0.13.2
  - datasets=2.6.1
  - diffusers=0.11.1
  - av=10.0.0
  - cmake=3.24.3
  # trick to avoid cpu affinity issue described in https://github.com/pytorch/pytorch/issues/99625
  - llvm-openmp=14
  # trick to force reinstall imagecodecs via pip
  - imagecodecs==2022.8.8
  - pip:
    - ray[default,tune]==2.2.0
    # requires mujoco py dependencies libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
    - free-mujoco-py==2.1.6
    - pygame==2.1.2
    - pybullet-svl==3.1.6.4
    - robosuite @ https://github.com/cheng-chi/robosuite/archive/277ab9588ad7a4f4b55cf75508b44aa67ec171f0.tar.gz
    - robomimic==0.2.0
    - pytorchvideo==0.1.5
    # pip package required for jpeg-xl
    - imagecodecs==2022.9.26
    - r3m @ https://github.com/facebookresearch/r3m/archive/b2334e726887fa0206962d7984c69c5fb09cceab.tar.gz
    - dm-control==1.0.9

```

### conda_environment_macos.yaml

```yaml
name: robodiff
channels:
  - pytorch
  - conda-forge
dependencies:
  - python=3.9
  - pip=22.2.2
  - pytorch=1.12.1
  - torchvision=0.13.1
  - numpy=1.23.3
  - numba==0.56.4
  - scipy==1.9.1
  - py-opencv=4.6.0
  - cffi=1.15.1
  - ipykernel=6.16
  - matplotlib=3.6.1
  - zarr=2.12.0
  - numcodecs=0.10.2
  - h5py=3.7.0
  - hydra-core=1.2.0
  - einops=0.4.1
  - tqdm=4.64.1
  - dill=0.3.5.1
  - scikit-video=1.1.11
  - scikit-image=0.19.3
  - gym=0.21.0
  - pymunk=6.2.1
  - wandb=0.13.3
  - threadpoolctl=3.1.0
  - shapely=1.8.4
  - cython=0.29.32
  - imageio=2.22.0
  - imageio-ffmpeg=0.4.7
  - termcolor=2.0.1
  - tensorboard=2.10.1
  - tensorboardx=2.5.1
  - psutil=5.9.2
  - click=8.0.4
  - boto3=1.24.96
  - accelerate=0.13.2
  - datasets=2.6.1
  - diffusers=0.11.1
  - av=10.0.0
  - cmake=3.24.3
  # trick to force reinstall imagecodecs via pip
  - imagecodecs==2022.8.8
  - pip:
    - ray[default,tune]==2.2.0
    - pygame==2.1.2
    - robomimic==0.2.0
    - pytorchvideo==0.1.5
    - atomics==1.0.2
    # No support for jpeg-xl for MacOS
    - imagecodecs==2022.9.26
    - r3m @ https://github.com/facebookresearch/r3m/archive/b2334e726887fa0206962d7984c69c5fb09cceab.tar.gz

```

### conda_environment_real.yaml

```yaml
name: robodiff
channels:
  - pytorch
  - pytorch3d
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - pip=22.2.2
  - cudatoolkit=11.6
  - pytorch=1.12.1
  - torchvision=0.13.1
  - pytorch3d=0.7.0
  - numpy=1.23.3
  - numba==0.56.4
  - scipy==1.9.1
  - py-opencv=4.6.0
  - cffi=1.15.1
  - ipykernel=6.16
  - matplotlib=3.6.1
  - zarr=2.12.0
  - numcodecs=0.10.2
  - h5py=3.7.0
  - hydra-core=1.2.0
  - einops=0.4.1
  - tqdm=4.64.1
  - dill=0.3.5.1
  - scikit-video=1.1.11
  - scikit-image=0.19.3
  - gym=0.21.0
  - pymunk=6.2.1
  - wandb=0.13.3
  - threadpoolctl=3.1.0
  - shapely=1.8.4
  - cython=0.29.32
  - imageio=2.22.0
  - imageio-ffmpeg=0.4.7
  - termcolor=2.0.1
  - tensorboard=2.10.1
  - tensorboardx=2.5.1
  - psutil=5.9.2
  - click=8.0.4
  - boto3=1.24.96
  - accelerate=0.13.2
  - datasets=2.6.1
  - diffusers=0.11.1
  - av=10.0.0
  - cmake=3.24.3
  # trick to avoid cpu affinity issue described in https://github.com/pytorch/pytorch/issues/99625
  - llvm-openmp=14
  # trick to force reinstall imagecodecs via pip
  - imagecodecs==2022.8.8
  - pip:
    - ray[default,tune]==2.2.0
    # requires mujoco py dependencies libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
    - free-mujoco-py==2.1.6
    - pygame==2.1.2
    - pybullet-svl==3.1.6.4
    - robosuite @ https://github.com/cheng-chi/robosuite/archive/277ab9588ad7a4f4b55cf75508b44aa67ec171f0.tar.gz
    - robomimic==0.2.0
    - pytorchvideo==0.1.5
    # requires librealsense https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md
    - pyrealsense2==2.51.1.4348
    # requires apt install libspnav-dev spacenavd; systemctl start spacenavd
    - spnav @ https://github.com/cheng-chi/spnav/archive/c1c938ebe3cc542db4685e0d13850ff1abfdb943.tar.gz
    - ur-rtde==1.5.5
    - atomics==1.0.2
    # pip package required for jpeg-xl
    - imagecodecs==2022.9.26
    - r3m @ https://github.com/facebookresearch/r3m/archive/b2334e726887fa0206962d7984c69c5fb09cceab.tar.gz
    - dm-control==1.0.9
    - pynput==1.7.6
  
```

### diffusion_policy/config/task/blockpush_lowdim_seed.yaml

```yaml
name: blockpush_lowdim_seed

obs_dim: 16
action_dim: 2
keypoint_dim: 2
obs_eef_target: True

env_runner:
  _target_: diffusion_policy.env_runner.blockpush_lowdim_runner.BlockPushLowdimRunner
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 350
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  fps: 5
  past_action: ${past_action_visible}
  abs_action: False
  obs_eef_target: ${task.obs_eef_target}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.blockpush_lowdim_dataset.BlockPushLowdimDataset
  zarr_path: data/block_pushing/multimodal_push_seed.zarr
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_eef_target: ${task.obs_eef_target}
  use_manual_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/blockpush_lowdim_seed_abs.yaml

```yaml
name: blockpush_lowdim_seed_abs

obs_dim: 16
action_dim: 2
keypoint_dim: 2
obs_eef_target: True

env_runner:
  _target_: diffusion_policy.env_runner.blockpush_lowdim_runner.BlockPushLowdimRunner
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 350
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  fps: 5
  past_action: ${past_action_visible}
  abs_action: True
  obs_eef_target: ${task.obs_eef_target}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.blockpush_lowdim_dataset.BlockPushLowdimDataset
  zarr_path: data/block_pushing/multimodal_push_seed_abs.zarr
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_eef_target: ${task.obs_eef_target}
  use_manual_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/can_image.yaml

```yaml
name: can_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [7]

task_name: &task_name can
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/can_image_abs.yaml

```yaml
name: can_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [10]

task_name: &task_name can
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/can_lowdim.yaml

```yaml
name: can_lowdim

obs_dim: 23
action_dim: 7
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name can
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/can_lowdim_abs.yaml

```yaml
name: can_lowdim

obs_dim: 23
action_dim: 10
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name can
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  rotation_rep: rotation_6d
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/kitchen_lowdim.yaml

```yaml
name: kitchen_lowdim

obs_dim: 60
action_dim: 9
keypoint_dim: 3

dataset_dir: &dataset_dir data/kitchen

env_runner:
  _target_: diffusion_policy.env_runner.kitchen_lowdim_runner.KitchenLowdimRunner
  dataset_dir: *dataset_dir
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 280
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_hw: [240, 360]
  fps: 12.5
  past_action: ${past_action_visible}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.kitchen_lowdim_dataset.KitchenLowdimDataset
  dataset_dir: *dataset_dir
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1'}
  pad_after: ${eval:'${n_action_steps}-1'}
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/kitchen_lowdim_abs.yaml

```yaml
name: kitchen_lowdim

obs_dim: 60
action_dim: 9
keypoint_dim: 3

abs_action: True
robot_noise_ratio: 0.1

env_runner:
  _target_: diffusion_policy.env_runner.kitchen_lowdim_runner.KitchenLowdimRunner
  dataset_dir: data/kitchen
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 280
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_hw: [240, 360]
  fps: 12.5
  past_action: ${past_action_visible}
  abs_action: ${task.abs_action}
  robot_noise_ratio: ${task.robot_noise_ratio}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.kitchen_mjl_lowdim_dataset.KitchenMjlLowdimDataset
  dataset_dir: data/kitchen/kitchen_demos_multitask
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1'}
  pad_after: ${eval:'${n_action_steps}-1'}
  abs_action: ${task.abs_action}
  robot_noise_ratio: ${task.robot_noise_ratio}
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/lift_image.yaml

```yaml
name: lift_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [7]

task_name: &task_name lift
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 1
  train_start_idx: 0
  n_test: 50
  n_test_vis: 3
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/lift_image_abs.yaml

```yaml
name: lift_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [10]

task_name: &task_name lift
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/lift_lowdim.yaml

```yaml
name: lift_lowdim

obs_dim: 19
action_dim: 7
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name lift
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/lift_lowdim_abs.yaml

```yaml
name: lift_lowdim

obs_dim: 19
action_dim: 10
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name lift
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 3
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  rotation_rep: rotation_6d
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/pusht_image.yaml

```yaml
name: pusht_image

image_shape: &image_shape [3, 96, 96]
shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    image:
      shape: *image_shape
      type: rgb
    agent_pos:
      shape: [2]
      type: low_dim
  action:
    shape: [2]

env_runner:
  _target_: diffusion_policy.env_runner.pusht_image_runner.PushTImageRunner
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  legacy_test: True
  test_start_seed: 100000
  max_steps: 300
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  fps: 10
  past_action: ${past_action_visible}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.pusht_image_dataset.PushTImageDataset
  zarr_path: data/pusht/pusht_cchi_v7_replay.zarr
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1'}
  pad_after: ${eval:'${n_action_steps}-1'}
  seed: 42
  val_ratio: 0.02
  max_train_episodes: 90

```

### diffusion_policy/config/task/pusht_lowdim.yaml

```yaml
name: pusht_lowdim

obs_dim: 20 # 9*2 keypoints + 2 state
action_dim: 2
keypoint_dim: 2

env_runner:
  _target_: diffusion_policy.env_runner.pusht_keypoints_runner.PushTKeypointsRunner
  keypoint_visible_rate: ${keypoint_visible_rate}
  n_train: 6
  n_train_vis: 2
  train_start_seed: 0
  n_test: 50
  n_test_vis: 4
  legacy_test: True
  test_start_seed: 100000
  max_steps: 300
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  fps: 10
  agent_keypoints: False
  past_action: ${past_action_visible}
  n_envs: null

dataset:
  _target_: diffusion_policy.dataset.pusht_dataset.PushTLowdimDataset
  zarr_path: data/pusht/pusht_cchi_v7_replay.zarr
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  seed: 42
  val_ratio: 0.02
  max_train_episodes: 90

```

### diffusion_policy/config/task/real_pusht_image.yaml

```yaml
name: real_image

image_shape: [3, 240, 320]
dataset_path: data/pusht_real/real_pusht_20230105

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    # camera_0:
    #   shape: ${task.image_shape}
    #   type: rgb
    camera_1:
      shape: ${task.image_shape}
      type: rgb
    # camera_2:
    #   shape: ${task.image_shape}
    #   type: rgb
    camera_3:
      shape: ${task.image_shape}
      type: rgb
    # camera_4:
    #   shape: ${task.image_shape}
    #   type: rgb
    robot_eef_pose:
      shape: [2]
      type: low_dim
  action: 
    shape: [2]

env_runner:
  _target_: diffusion_policy.env_runner.real_pusht_image_runner.RealPushTImageRunner

dataset:
  _target_: diffusion_policy.dataset.real_pusht_image_dataset.RealPushTImageDataset
  shape_meta: *shape_meta
  dataset_path: ${task.dataset_path}
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  n_latency_steps: ${n_latency_steps}
  use_cache: True
  seed: 42
  val_ratio: 0.00
  max_train_episodes: null
  delta_action: False


```

### diffusion_policy/config/task/square_image.yaml

```yaml
name: square_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [7]

task_name: &task_name square
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/square_image_abs.yaml

```yaml
name: square_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    agentview_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [10]

task_name: &task_name square
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'agentview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/square_lowdim.yaml

```yaml
name: square_lowdim

obs_dim: 23
action_dim: 7
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name square
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02
  max_train_episodes: null

```

### diffusion_policy/config/task/square_lowdim_abs.yaml

```yaml
name: square_lowdim

obs_dim: 23
action_dim: 10
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name square
dataset_type: &dataset_type ph
abs_action: &abs_action True
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim_abs.hdf5


env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  # use python's eval function as resolver, single-quoted string as argument
  max_steps: ${eval:'500 if "${task.dataset_type}" == "mh" else 400'}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02
  max_train_episodes: null

```

### diffusion_policy/config/task/tool_hang_image.yaml

```yaml
name: tool_hang_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    sideview_image:
      shape: [3, 240, 240]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 240, 240]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [7]

task_name: &task_name tool_hang
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'sideview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/tool_hang_image_abs.yaml

```yaml
name: tool_hang_image_abs

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    sideview_image:
      shape: [3, 240, 240]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 240, 240]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
  action: 
    shape: [10]

task_name: &task_name tool_hang
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  # costs 1GB per env
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'sideview_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/tool_hang_lowdim.yaml

```yaml
name: tool_hang_lowdim

obs_dim: 53
action_dim: 7
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name tool_hang
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28
# seed 42 will crash MuJoCo for some reason.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/tool_hang_lowdim_abs.yaml

```yaml
name: tool_hang_lowdim

obs_dim: 53
action_dim: 10
keypoint_dim: 3

obs_keys: &obs_keys ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos']
task_name: &task_name tool_hang
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28
# seed 42 will crash MuJoCo for some reason.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  rotation_rep: rotation_6d
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/transport_image.yaml

```yaml
name: transport_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    shouldercamera0_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
    shouldercamera1_image:
      shape: [3, 84, 84]
      type: rgb
    robot1_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot1_eef_pos:
      shape: [3]
      # type default: low_dim
    robot1_eef_quat:
      shape: [4]
    robot1_gripper_qpos:
      shape: [2]
  action: 
    shape: [14]

task_name: &task_name transport
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'shouldercamera0_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/transport_image_abs.yaml

```yaml
name: transport_image

shape_meta: &shape_meta
  # acceptable types: rgb, low_dim
  obs:
    shouldercamera0_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot0_eef_pos:
      shape: [3]
      # type default: low_dim
    robot0_eef_quat:
      shape: [4]
    robot0_gripper_qpos:
      shape: [2]
    shouldercamera1_image:
      shape: [3, 84, 84]
      type: rgb
    robot1_eye_in_hand_image:
      shape: [3, 84, 84]
      type: rgb
    robot1_eef_pos:
      shape: [3]
      # type default: low_dim
    robot1_eef_quat:
      shape: [4]
    robot1_gripper_qpos:
      shape: [2]
  action: 
    shape: [20]

task_name: &task_name transport
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/image_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_image_runner.RobomimicImageRunner
  dataset_path: *dataset_path
  shape_meta: *shape_meta
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  render_obs_key: 'shouldercamera0_image'
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  tqdm_interval_sec: 1.0
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_image_dataset.RobomimicReplayImageDataset
  shape_meta: *shape_meta
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  n_obs_steps: ${dataset_obs_steps}
  abs_action: *abs_action
  rotation_rep: 'rotation_6d'
  use_legacy_normalizer: False
  use_cache: True
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/transport_lowdim.yaml

```yaml
name: transport_lowdim

obs_dim: 59 # 41+(3+4+2)*2
action_dim: 14 # 7*2
keypoint_dim: 3

obs_keys: &obs_keys [
  'object', 
  'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 
  'robot1_eef_pos', 'robot1_eef_quat', 'robot1_gripper_qpos'
]
task_name: &task_name transport
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim.hdf5
abs_action: &abs_action False

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 5
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/task/transport_lowdim_abs.yaml

```yaml
name: transport_lowdim

obs_dim: 59 # 41+(3+4+2)*2
action_dim: 20 # 10*2
keypoint_dim: 3

obs_keys: &obs_keys [
  'object', 
  'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 
  'robot1_eef_pos', 'robot1_eef_quat', 'robot1_gripper_qpos'
]
task_name: &task_name transport
dataset_type: &dataset_type ph
dataset_path: &dataset_path data/robomimic/datasets/${task.task_name}/${task.dataset_type}/low_dim_abs.hdf5
abs_action: &abs_action True

env_runner:
  _target_: diffusion_policy.env_runner.robomimic_lowdim_runner.RobomimicLowdimRunner
  dataset_path: *dataset_path
  obs_keys: *obs_keys
  n_train: 6
  n_train_vis: 2
  train_start_idx: 0
  n_test: 50
  n_test_vis: 4
  test_start_seed: 100000
  max_steps: 700
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  n_latency_steps: ${n_latency_steps}
  render_hw: [128,128]
  fps: 10
  crf: 22
  past_action: ${past_action_visible}
  abs_action: *abs_action
  n_envs: 28
# evaluation at this config requires a 16 core 64GB instance.

dataset:
  _target_: diffusion_policy.dataset.robomimic_replay_lowdim_dataset.RobomimicReplayLowdimDataset
  dataset_path: *dataset_path
  horizon: ${horizon}
  pad_before: ${eval:'${n_obs_steps}-1+${n_latency_steps}'}
  pad_after: ${eval:'${n_action_steps}-1'}
  obs_keys: *obs_keys
  abs_action: *abs_action
  use_legacy_normalizer: False
  seed: 42
  val_ratio: 0.02

```

### diffusion_policy/config/train_bet_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: blockpush_lowdim_seed

name: train_bet_lowdim
_target_: diffusion_policy.workspace.train_bet_lowdim_workspace.TrainBETLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
keypoint_dim: ${task.keypoint_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 3
n_obs_steps: 3
n_action_steps: 1
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_local_cond: False
obs_as_global_cond: False
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.bet_lowdim_policy.BETLowdimPolicy

  action_ae:
    _target_: diffusion_policy.model.bet.action_ae.discretizers.k_means.KMeansDiscretizer
    num_bins: 24
    action_dim: ${action_dim}
    predict_offsets: True
  
  obs_encoding_net:
    _target_: torch.nn.Identity
    output_dim: ${obs_dim}
  
  state_prior:
    _target_: diffusion_policy.model.bet.latent_generators.mingpt.MinGPT

    discrete_input: false
    input_dim: ${obs_dim}

    vocab_size: ${policy.action_ae.num_bins}

    # Architecture details
    n_layer: 4
    n_head: 4
    n_embd: 72

    block_size: ${horizon}  # Length of history/context
    predict_offsets: True
    offset_loss_scale: 1000.0  # actions are very small
    focal_loss_gamma: 2.0
    action_dim: ${action_dim}

  horizon: ${horizon}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  learning_rate: 0.0001 # 1e-4
  weight_decay: 0.1
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 5000
  gradient_accumulate_every: 1
  grad_norm_clip: 1.0
  enable_normalizer: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_transformer_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_transformer_hybrid
_target_: diffusion_policy.workspace.train_diffusion_transformer_hybrid_workspace.TrainDiffusionTransformerHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 10
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_transformer_hybrid_image_policy.DiffusionTransformerHybridImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100

  crop_shape: [76, 76]
  obs_encoder_group_norm: True
  eval_fixed_crop: True

  n_layer: 8
  n_cond_layers: 0  # >0: use transformer encoder for cond, otherwise use MLP
  n_head: 4
  n_emb: 256
  p_drop_emb: 0.0
  p_drop_attn: 0.3
  causal_attn: True
  time_as_cond: True # if false, use BERT like encoder only arch, time as input
  obs_as_cond: ${obs_as_cond}

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  transformer_weight_decay: 1.0e-3
  obs_encoder_weight_decay: 1.0e-6
  learning_rate: 1.0e-4
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  # Transformer needs LR warmup
  lr_warmup_steps: 1000
  num_epochs: 3050
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_transformer_lowdim_kitchen_workspace.yaml

```yaml
defaults:
  - _self_
  - task: kitchen_lowdim_abs

name: train_diffusion_transformer_lowdim
_target_: diffusion_policy.workspace.train_diffusion_transformer_lowdim_workspace.TrainDiffusionTransformerLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 16
n_obs_steps: 4
n_action_steps: 8
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.diffusion_transformer_lowdim_policy.DiffusionTransformerLowdimPolicy

  model:
    _target_: diffusion_policy.model.diffusion.transformer_for_diffusion.TransformerForDiffusion
    input_dim: ${eval:'${action_dim} if ${obs_as_cond} else ${obs_dim} + ${action_dim}'}
    output_dim: ${policy.model.input_dim}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    cond_dim: ${eval:'${obs_dim} if ${obs_as_cond} else 0'}

    n_layer: 8
    n_head: 4
    n_emb: 768
    p_drop_emb: 0.0
    p_drop_attn: 0.1

    causal_attn: True
    time_as_cond: True # if false, use BERT like encoder only arch, time as input
    obs_as_cond: ${obs_as_cond}
    n_cond_layers: 0 # >0: use transformer encoder for cond, otherwise use MLP
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${n_action_steps}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_cond: ${obs_as_cond}
  pred_action_steps_only: ${pred_action_steps_only}

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  learning_rate: 1.0e-4
  weight_decay: 1.0e-3
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  # Transformer needs LR warmup
  lr_warmup_steps: 1000
  num_epochs: 5000
  gradient_accumulate_every: 1
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_transformer_lowdim_pusht_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_lowdim

name: train_diffusion_transformer_lowdim
_target_: diffusion_policy.workspace.train_diffusion_transformer_lowdim_workspace.TrainDiffusionTransformerLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.diffusion_transformer_lowdim_policy.DiffusionTransformerLowdimPolicy

  model:
    _target_: diffusion_policy.model.diffusion.transformer_for_diffusion.TransformerForDiffusion
    input_dim: ${eval:'${action_dim} if ${obs_as_cond} else ${obs_dim} + ${action_dim}'}
    output_dim: ${policy.model.input_dim}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    cond_dim: ${eval:'${obs_dim} if ${obs_as_cond} else 0'}

    n_layer: 8
    n_head: 4
    n_emb: 256
    p_drop_emb: 0.0
    p_drop_attn: 0.01

    causal_attn: True
    time_as_cond: True # if false, use BERT like encoder only arch, time as input
    obs_as_cond: ${obs_as_cond}
    n_cond_layers: 0 # >0: use transformer encoder for cond, otherwise use MLP
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${n_action_steps}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_cond: ${obs_as_cond}
  pred_action_steps_only: ${pred_action_steps_only}

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  learning_rate: 1.0e-4
  weight_decay: 1.0e-1
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  # Transformer needs LR warmup
  lr_warmup_steps: 1000
  num_epochs: 8000
  gradient_accumulate_every: 1
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_transformer_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: blockpush_lowdim_seed

name: train_diffusion_transformer_lowdim
_target_: diffusion_policy.workspace.train_diffusion_transformer_lowdim_workspace.TrainDiffusionTransformerLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 5
n_obs_steps: 3
n_action_steps: 1
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.diffusion_transformer_lowdim_policy.DiffusionTransformerLowdimPolicy

  model:
    _target_: diffusion_policy.model.diffusion.transformer_for_diffusion.TransformerForDiffusion
    input_dim: ${eval:'${action_dim} if ${obs_as_cond} else ${obs_dim} + ${action_dim}'}
    output_dim: ${policy.model.input_dim}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    cond_dim: ${eval:'${obs_dim} if ${obs_as_cond} else 0'}

    n_layer: 8
    n_head: 4
    n_emb: 256
    p_drop_emb: 0.0
    p_drop_attn: 0.3

    causal_attn: True
    time_as_cond: True # if false, use BERT like encoder only arch, time as input
    obs_as_cond: ${obs_as_cond}
    n_cond_layers: 0 # >0: use transformer encoder for cond, otherwise use MLP
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${n_action_steps}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_cond: ${obs_as_cond}
  pred_action_steps_only: ${pred_action_steps_only}

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  learning_rate: 1.0e-4
  weight_decay: 1.0e-3
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  # Transformer needs LR warmup
  lr_warmup_steps: 1000
  num_epochs: 5000
  gradient_accumulate_every: 1
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_transformer_real_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_diffusion_transformer_hybrid
_target_: diffusion_policy.workspace.train_diffusion_transformer_hybrid_workspace.TrainDiffusionTransformerHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_transformer_hybrid_image_policy.DiffusionTransformerHybridImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 8

  crop_shape: [216, 288] # ch, cw 320x240 90%
  obs_encoder_group_norm: True
  eval_fixed_crop: True

  n_layer: 8
  n_cond_layers: 0  # >0: use transformer encoder for cond, otherwise use MLP
  n_head: 4
  n_emb: 256
  p_drop_emb: 0.0
  p_drop_attn: 0.3
  causal_attn: True
  time_as_cond: True # if false, use BERT like encoder only arch, time as input
  obs_as_cond: ${obs_as_cond}

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: True

optimizer:
  transformer_weight_decay: 1.0e-3
  obs_encoder_weight_decay: 1.0e-6
  learning_rate: 1.0e-4
  betas: [0.9, 0.95]

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  # Transformer needs LR warmup
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_ddim_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_unet_hybrid
_target_: diffusion_policy.workspace.train_diffusion_unet_hybrid_workspace.TrainDiffusionUnetHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_hybrid_image_policy.DiffusionUnetHybridImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 8
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: [76, 76]
  crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [256,512,1024]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True
  obs_encoder_group_norm: True
  eval_fixed_crop: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 3000
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_ddim_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_lowdim

name: train_diffusion_unet_lowdim
_target_: diffusion_policy.workspace.train_diffusion_unet_lowdim_workspace.TrainDiffusionUnetLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
keypoint_dim: ${task.keypoint_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_local_cond: False
obs_as_global_cond: False
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.diffusion_unet_lowdim_policy.DiffusionUnetLowdimPolicy

  model:
    _target_: diffusion_policy.model.diffusion.conditional_unet1d.ConditionalUnet1D
    input_dim: "${eval: ${task.action_dim} if ${obs_as_local_cond} or ${obs_as_global_cond} else ${task.obs_dim} + ${task.action_dim}}"
    local_cond_dim: "${eval: ${task.obs_dim} if ${obs_as_local_cond} else None}"
    global_cond_dim: "${eval: ${task.obs_dim}*${n_obs_steps} if ${obs_as_global_cond} else None}"
    diffusion_step_embed_dim: 256
    down_dims: [256, 512, 1024]
    kernel_size: 5
    n_groups: 8
    cond_predict_scale: True
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 8
  obs_as_local_cond: ${obs_as_local_cond}
  obs_as_global_cond: ${obs_as_global_cond}
  pred_action_steps_only: ${pred_action_steps_only}
  oa_step_convention: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 8000
  gradient_accumulate_every: 1
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_unet_hybrid
_target_: diffusion_policy.workspace.train_diffusion_unet_hybrid_workspace.TrainDiffusionUnetHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_hybrid_image_policy.DiffusionUnetHybridImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  crop_shape: [76, 76]
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True
  obs_encoder_group_norm: True
  eval_fixed_crop: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 3050
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_image_pretrained_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_unet_image
_target_: diffusion_policy.workspace.train_diffusion_unet_image_workspace.TrainDiffusionUnetImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: IMAGENET1K_V1 # or r3m
    resize_shape: [256, 256]
    crop_shape: [224, 224]
    random_crop: False
    use_group_norm: False
    share_rgb_model: True
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 4
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 4
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 8000
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  freeze_encoder: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_image_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_unet_image
_target_: diffusion_policy.workspace.train_diffusion_unet_image_workspace.TrainDiffusionUnetImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: null
    resize_shape: null
    crop_shape: [76, 76]
    # constant center crop
    random_crop: True
    use_group_norm: True
    share_rgb_model: False
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 4
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 4
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 8000
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  freeze_encoder: False
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_lowdim

name: train_diffusion_unet_lowdim
_target_: diffusion_policy.workspace.train_diffusion_unet_lowdim_workspace.TrainDiffusionUnetLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
keypoint_dim: ${task.keypoint_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_local_cond: False
obs_as_global_cond: True
pred_action_steps_only: False

policy:
  _target_: diffusion_policy.policy.diffusion_unet_lowdim_policy.DiffusionUnetLowdimPolicy

  model:
    _target_: diffusion_policy.model.diffusion.conditional_unet1d.ConditionalUnet1D
    input_dim: "${eval: ${task.action_dim} if ${obs_as_local_cond} or ${obs_as_global_cond} else ${task.obs_dim} + ${task.action_dim}}"
    local_cond_dim: "${eval: ${task.obs_dim} if ${obs_as_local_cond} else None}"
    global_cond_dim: "${eval: ${task.obs_dim}*${n_obs_steps} if ${obs_as_global_cond} else None}"
    diffusion_step_embed_dim: 256
    down_dims: [256, 512, 1024]
    kernel_size: 5
    n_groups: 8
    cond_predict_scale: True
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_local_cond: ${obs_as_local_cond}
  obs_as_global_cond: ${obs_as_global_cond}
  pred_action_steps_only: ${pred_action_steps_only}
  oa_step_convention: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 5000
  gradient_accumulate_every: 1
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_real_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_diffusion_unet_hybrid
_target_: diffusion_policy.workspace.train_diffusion_unet_hybrid_workspace.TrainDiffusionUnetHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_hybrid_image_policy.DiffusionUnetHybridImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 8
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: [76, 76] # 84x84 90%
  crop_shape: [216, 288] # ch, cw 320x240 90%
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [256,512,1024]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True
  obs_encoder_group_norm: True
  eval_fixed_crop: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: True

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_real_image_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_diffusion_unet_image
_target_: diffusion_policy.workspace.train_diffusion_unet_image_workspace.TrainDiffusionUnetImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: null
    resize_shape: [240, 320]
    crop_shape: [216, 288] # ch, cw 240x320 90%
    random_crop: True
    use_group_norm: True
    share_rgb_model: False
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: True

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  freeze_encoder: False
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_real_pretrained_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_diffusion_unet_image
_target_: diffusion_policy.workspace.train_diffusion_unet_image_workspace.TrainDiffusionUnetImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 2
n_action_steps: 8
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    # beta_schedule is important
    # this is the best we found
    beta_schedule: squaredcos_cap_v2
    clip_sample: True
    set_alpha_to_one: True
    steps_offset: 0
    prediction_type: epsilon # or sample

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: IMAGENET1K_V1 # or r3m
    resize_shape: [224,224]
    crop_shape: null
    random_crop: False
    use_group_norm: False
    share_rgb_model: True
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  # crop_shape: null
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 64
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: True

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  # EMA destroys performance when used with BatchNorm
  # replace BatchNorm with GroupNorm.
  use_ema: True
  freeze_encoder: True
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_diffusion_unet_video_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image_abs

name: train_diffusion_unet_video
_target_: diffusion_policy.workspace.train_diffusion_unet_video_workspace.TrainDiffusionUnetVideoWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 16
n_obs_steps: 4
n_action_steps: 8
past_action_visible: False
keypoint_visible_rate: 1.0
lowdim_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_video_policy.DiffusionUnetVideoPolicy

  shape_meta: ${shape_meta}
  
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small # Yilun's paper uses fixed_small_log instead, but easy to cause Nan
    clip_sample: True # required when predict_epsilon=False
    prediction_type: epsilon # or sample

  rgb_net:
    _target_: diffusion_policy.model.obs_encoder.video_core.VideoCore

    backbone:
      _target_: diffusion_policy.model.obs_encoder.video_core.VideoResNet

      norm_groups: 8
      input_channel: 3
      model_depth: 50 # ResNet 50 (18,34 not yet available)
    
    pool:
      _target_: diffusion_policy.model.ibc.global_avgpool.GlobalAvgpool

      dim: [2,3,4]

  horizon: ${horizon}
  n_action_steps: ${n_action_steps}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  lowdim_as_global_cond: ${lowdim_as_global_cond}
  diffusion_step_embed_dim: 128
  down_dims: [512, 1024, 2048]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

  # TemporalAggregator Parameters
  channel_mults: [1,1]
  n_blocks_per_level: 1
  ta_kernel_size: 3
  ta_n_groups: 1

  # scheduler.step params
  # predict_epsilon: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 32
  num_workers: 1
  shuffle: True
  pin_memory: True

optimizer:
  _target_: torch.optim.AdamW
  lr: 0.0001 # 1e-4
  betas: [0.95, 0.999]
  eps: 0.00000001 # 1e-8
  weight_decay: 0.000001 # 1e-6

training:
  device: "cuda:0"
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 1500
  gradient_accumulate_every: 1
  eval_every: 5000
  eval_first: False
  val_every: 300
  use_ema: False
  tqdm_interval_sec: 1.0
  seed: 42

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:03d}-test_score={test_score:.3f}.ckpt'
  save_last_ckpt: False
  save_last_snapshot: False

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_ibc_dfo_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_image

name: train_ibc_dfo_hybrid
_target_: diffusion_policy.workspace.train_ibc_dfo_hybrid_workspace.TrainIbcDfoHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 2
n_obs_steps: 2
n_action_steps: 1
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.ibc_dfo_hybrid_image_policy.IbcDfoHybridImagePolicy

  shape_meta: ${shape_meta}

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  dropout: 0.1
  train_n_neg: 1024
  pred_n_iter: 5
  pred_n_samples: 1024
  kevin_inference: False
  andy_train: False
  obs_encoder_group_norm: True
  eval_fixed_crop: True
  crop_shape: [84, 84]

dataloader:
  batch_size: 128
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 128
  num_workers: 8
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 3050
  gradient_accumulate_every: 1
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  sample_max_batch: 128
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_ibc_dfo_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_lowdim

name: train_ibc_dfo_lowdim
_target_: diffusion_policy.workspace.train_ibc_dfo_lowdim_workspace.TrainIbcDfoLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
keypoint_dim: ${task.keypoint_dim}
task_name: ${task.name}
exp_name: "default"

horizon: 2
n_obs_steps: 2
n_action_steps: 1
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.ibc_dfo_lowdim_policy.IbcDfoLowdimPolicy

  horizon: ${horizon}
  obs_dim: ${obs_dim}
  action_dim: ${action_dim}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  dropout: 0.1
  train_n_neg: 1024
  pred_n_iter: 5
  pred_n_samples: 1024
  kevin_inference: False
  andy_train: False

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 5000
  gradient_accumulate_every: 1
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  sample_max_batch: 128
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_ibc_dfo_real_hybrid_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_ibc_dfo_hybrid
_target_: diffusion_policy.workspace.train_ibc_dfo_hybrid_workspace.TrainIbcDfoHybridWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: 2
n_obs_steps: 2
n_action_steps: 1
n_latency_steps: 1
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.ibc_dfo_hybrid_image_policy.IbcDfoHybridImagePolicy

  shape_meta: ${shape_meta}

  horizon: ${horizon}
  n_action_steps: ${n_action_steps}
  n_obs_steps: ${n_obs_steps}
  dropout: 0.1
  train_n_neg: 256
  pred_n_iter: 3
  pred_n_samples: 1024
  kevin_inference: False
  andy_train: False
  obs_encoder_group_norm: True
  eval_fixed_crop: True
  crop_shape: [216, 288] # ch, cw 320x240 90%

dataloader:
  batch_size: 128
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 128
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 1000
  gradient_accumulate_every: 1
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 5
  val_every: 1
  sample_every: 5
  sample_max_batch: 128
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_action_mse_error
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_action_mse_error={train_action_mse_error:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_robomimic_image_workspace.yaml

```yaml
defaults:
  - _self_
  - task: lift_image

name: train_robomimic_image
_target_: diffusion_policy.workspace.train_robomimic_image_workspace.TrainRobomimicImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: &horizon 10
n_obs_steps: 1
n_action_steps: 1
n_latency_steps: 0
dataset_obs_steps: *horizon
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.robomimic_image_policy.RobomimicImagePolicy
  shape_meta: ${shape_meta}
  algo_name: bc_rnn
  obs_type: image
  # oc.select resolver: key, default
  task_name: ${oc.select:task.task_name,lift}
  dataset_type: ${oc.select:task.dataset_type,ph}
  crop_shape: [76,76]

dataloader:
  batch_size: 64
  num_workers: 16
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 64
  num_workers: 16
  shuffle: False
  pin_memory: True
  persistent_workers: False

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  num_epochs: 3050
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_robomimic_lowdim_workspace.yaml

```yaml
defaults:
  - _self_
  - task: pusht_lowdim

name: train_robomimic_lowdim
_target_: diffusion_policy.workspace.train_robomimic_lowdim_workspace.TrainRobomimicLowdimWorkspace

obs_dim: ${task.obs_dim}
action_dim: ${task.action_dim}
transition_dim: "${eval: ${task.obs_dim} + ${task.action_dim}}"
task_name: ${task.name}
exp_name: "default"

horizon: 10
n_obs_steps: 1
n_action_steps: 1
n_latency_steps: 0
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.robomimic_lowdim_policy.RobomimicLowdimPolicy
  action_dim: ${action_dim}
  obs_dim: ${obs_dim}
  algo_name: bc_rnn
  obs_type: low_dim
  # oc.select resolver: key, default
  task_name: ${oc.select:task.task_name,lift}
  dataset_type: ${oc.select:task.dataset_type,ph}

dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 256
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  num_epochs: 5000
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### diffusion_policy/config/train_robomimic_real_image_workspace.yaml

```yaml
defaults:
  - _self_
  - task: real_pusht_image

name: train_robomimic_image
_target_: diffusion_policy.workspace.train_robomimic_image_workspace.TrainRobomimicImageWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "default"

horizon: &horizon 10
n_obs_steps: 1
n_action_steps: 1
n_latency_steps: 1
dataset_obs_steps: *horizon
past_action_visible: False
keypoint_visible_rate: 1.0

policy:
  _target_: diffusion_policy.policy.robomimic_image_policy.RobomimicImagePolicy
  shape_meta: ${shape_meta}
  algo_name: bc_rnn
  obs_type: image
  # oc.select resolver: key, default
  task_name: ${oc.select:task.task_name,tool_hang}
  dataset_type: ${oc.select:task.dataset_type,ph}
  crop_shape: [216, 288] # ch, cw 320x240 90%

dataloader:
  batch_size: 32
  num_workers: 8
  shuffle: True
  pin_memory: True
  persistent_workers: True

val_dataloader:
  batch_size: 32
  num_workers: 1
  shuffle: False
  pin_memory: True
  persistent_workers: False

training:
  device: "cuda:0"
  seed: 42
  debug: False
  resume: True
  # optimization
  num_epochs: 1000
  # training loop control
  # in epochs
  rollout_every: 50
  checkpoint_every: 50
  val_every: 1
  sample_every: 5
  # steps per epoch
  max_train_steps: null
  max_val_steps: null
  # misc
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: train_loss
    mode: min
    k: 5
    format_str: 'epoch={epoch:04d}-train_loss={train_loss:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

```

### image_pusht_diffusion_policy_cnn.yaml

```yaml
_target_: diffusion_policy.workspace.train_diffusion_unet_hybrid_workspace.TrainDiffusionUnetHybridWorkspace
checkpoint:
  save_last_ckpt: true
  save_last_snapshot: false
  topk:
    format_str: epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt
    k: 5
    mode: max
    monitor_key: test_mean_score
dataloader:
  batch_size: 64
  num_workers: 8
  persistent_workers: false
  pin_memory: true
  shuffle: true
dataset_obs_steps: 2
ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  inv_gamma: 1.0
  max_value: 0.9999
  min_value: 0.0
  power: 0.75
  update_after_step: 0
exp_name: default
horizon: 16
keypoint_visible_rate: 1.0
logging:
  group: null
  id: null
  mode: online
  name: 2023.01.16-20.20.06_train_diffusion_unet_hybrid_pusht_image
  project: diffusion_policy_debug
  resume: true
  tags:
  - train_diffusion_unet_hybrid
  - pusht_image
  - default
multi_run:
  run_dir: data/outputs/2023.01.16/20.20.06_train_diffusion_unet_hybrid_pusht_image
  wandb_name_base: 2023.01.16-20.20.06_train_diffusion_unet_hybrid_pusht_image
n_action_steps: 8
n_latency_steps: 0
n_obs_steps: 2
name: train_diffusion_unet_hybrid
obs_as_global_cond: true
optimizer:
  _target_: torch.optim.AdamW
  betas:
  - 0.95
  - 0.999
  eps: 1.0e-08
  lr: 0.0001
  weight_decay: 1.0e-06
past_action_visible: false
policy:
  _target_: diffusion_policy.policy.diffusion_unet_hybrid_image_policy.DiffusionUnetHybridImagePolicy
  cond_predict_scale: true
  crop_shape:
  - 84
  - 84
  diffusion_step_embed_dim: 128
  down_dims:
  - 512
  - 1024
  - 2048
  eval_fixed_crop: true
  horizon: 16
  kernel_size: 5
  n_action_steps: 8
  n_groups: 8
  n_obs_steps: 2
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    beta_start: 0.0001
    clip_sample: true
    num_train_timesteps: 100
    prediction_type: epsilon
    variance_type: fixed_small
  num_inference_steps: 100
  obs_as_global_cond: true
  obs_encoder_group_norm: true
  shape_meta:
    action:
      shape:
      - 2
    obs:
      agent_pos:
        shape:
        - 2
        type: low_dim
      image:
        shape:
        - 3
        - 96
        - 96
        type: rgb
shape_meta:
  action:
    shape:
    - 2
  obs:
    agent_pos:
      shape:
      - 2
      type: low_dim
    image:
      shape:
      - 3
      - 96
      - 96
      type: rgb
task:
  dataset:
    _target_: diffusion_policy.dataset.pusht_image_dataset.PushTImageDataset
    horizon: 16
    max_train_episodes: 90
    pad_after: 7
    pad_before: 1
    seed: 42
    val_ratio: 0.02
    zarr_path: data/pusht/pusht_cchi_v7_replay.zarr
  env_runner:
    _target_: diffusion_policy.env_runner.pusht_image_runner.PushTImageRunner
    fps: 10
    legacy_test: true
    max_steps: 300
    n_action_steps: 8
    n_envs: null
    n_obs_steps: 2
    n_test: 50
    n_test_vis: 4
    n_train: 6
    n_train_vis: 2
    past_action: false
    test_start_seed: 100000
    train_start_seed: 0
  image_shape:
  - 3
  - 96
  - 96
  name: pusht_image
  shape_meta:
    action:
      shape:
      - 2
    obs:
      agent_pos:
        shape:
        - 2
        type: low_dim
      image:
        shape:
        - 3
        - 96
        - 96
        type: rgb
task_name: pusht_image
training:
  checkpoint_every: 50
  debug: false
  device: cuda:0
  gradient_accumulate_every: 1
  lr_scheduler: cosine
  lr_warmup_steps: 500
  max_train_steps: null
  max_val_steps: null
  num_epochs: 3050
  resume: true
  rollout_every: 50
  sample_every: 5
  seed: 42
  tqdm_interval_sec: 1.0
  use_ema: true
  val_every: 1
val_dataloader:
  batch_size: 64
  num_workers: 8
  persistent_workers: false
  pin_memory: true
  shuffle: false

```

## Python signatures and reward/observation bodies (159 files)


### diffusion_policy/codecs/imagecodecs_numcodecs.py

```
"""Additional numcodecs implemented using imagecodecs."""
def protective_squeeze(x)
def get_default_image_compressor()
class Aec(Codec)
    """AEC codec for numcodecs."""
    def __init__(self, bitspersample, flags, blocksize, rsi)
    def encode(self, buf)
    def decode(self, buf, out)
class Apng(Codec)
    """APNG codec for numcodecs."""
    def __init__(self, level, photometric, delay)
    def encode(self, buf)
    def decode(self, buf, out)
class Avif(Codec)
    """AVIF codec for numcodecs."""
    def __init__(self, level, speed, tilelog2, bitspersample, pixelformat, numthreads, index)
    def encode(self, buf)
    def decode(self, buf, out)
class Bitorder(Codec)
    """Bitorder codec for numcodecs."""
    def encode(self, buf)
    def decode(self, buf, out)
class Bitshuffle(Codec)
    """Bitshuffle codec for numcodecs."""
    def __init__(self, itemsize, blocksize)
    def encode(self, buf)
    def decode(self, buf, out)
class Blosc(Codec)
    """Blosc codec for numcodecs."""
    def __init__(self, level, compressor, typesize, blocksize, shuffle, numthreads)
    def encode(self, buf)
    def decode(self, buf, out)
class Blosc2(Codec)
    """Blosc2 codec for numcodecs."""
    def __init__(self, level, compressor, typesize, blocksize, shuffle, numthreads)
    def encode(self, buf)
    def decode(self, buf, out)
class Brotli(Codec)
    """Brotli codec for numcodecs."""
    def __init__(self, level, mode, lgwin)
    def encode(self, buf)
    def decode(self, buf, out)
class ByteShuffle(Codec)
    """ByteShuffle codec for numcodecs."""
    def __init__(self, shape, dtype, axis, dist, delta, reorder)
    def encode(self, buf)
    def decode(self, buf, out)
class Bz2(Codec)
    """Bz2 codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Cms(Codec)
    """CMS codec for numcodecs."""
    def __init__(self)
    def encode(self, buf, out)
    def decode(self, buf, out)
class Deflate(Codec)
    """Deflate codec for numcodecs."""
    def __init__(self, level, raw)
    def encode(self, buf)
    def decode(self, buf, out)
class Delta(Codec)
    """Delta codec for numcodecs."""
    def __init__(self, shape, dtype, axis, dist)
    def encode(self, buf)
    def decode(self, buf, out)
class Float24(Codec)
    """Float24 codec for numcodecs."""
    def __init__(self, byteorder, rounding)
    def encode(self, buf)
    def decode(self, buf, out)
class FloatPred(Codec)
    """Floating Point Predictor codec for numcodecs."""
    def __init__(self, shape, dtype, axis, dist)
    def encode(self, buf)
    def decode(self, buf, out)
class Gif(Codec)
    """GIF codec for numcodecs."""
    def encode(self, buf)
    def decode(self, buf, out)
class Heif(Codec)
    """HEIF codec for numcodecs."""
    def __init__(self, level, bitspersample, photometric, compression, numthreads, index)
    def encode(self, buf)
    def decode(self, buf, out)
class Jetraw(Codec)
    """Jetraw codec for numcodecs."""
    def __init__(self, shape, identifier, parameters, verbosity, errorbound)
    def encode(self, buf)
    def decode(self, buf, out)
class Jpeg(Codec)
    """JPEG codec for numcodecs."""
    def __init__(self, bitspersample, tables, header, colorspace_data, colorspace_jpeg, level, subsampling, optimize, smoothing)
    def encode(self, buf)
    def decode(self, buf, out)
    def get_config(self)
    def from_config(cls, config)
class Jpeg2k(Codec)
    """JPEG 2000 codec for numcodecs."""
    def __init__(self, level, codecformat, colorspace, tile, reversible, bitspersample, resolutions, numthreads, verbose)
    def encode(self, buf)
    def decode(self, buf, out)
class JpegLs(Codec)
    """JPEG LS codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class JpegXl(Codec)
    """JPEG XL codec for numcodecs."""
    def __init__(self, level, effort, distance, lossless, decodingspeed, photometric, planar, usecontainer, index, keeporientation, numthreads)
    def encode(self, buf)
    def decode(self, buf, out)
class JpegXr(Codec)
    """JPEG XR codec for numcodecs."""
    def __init__(self, level, photometric, hasalpha, resolution, fp2int)
    def encode(self, buf)
    def decode(self, buf, out)
class Lerc(Codec)
    """LERC codec for numcodecs."""
    def __init__(self, level, version, planar)
    def encode(self, buf)
    def decode(self, buf, out)
class Ljpeg(Codec)
    """LJPEG codec for numcodecs."""
    def __init__(self, bitspersample)
    def encode(self, buf)
    def decode(self, buf, out)
class Lz4(Codec)
    """LZ4 codec for numcodecs."""
    def __init__(self, level, hc, header)
    def encode(self, buf)
    def decode(self, buf, out)
class Lz4f(Codec)
    """LZ4F codec for numcodecs."""
    def __init__(self, level, blocksizeid, contentchecksum, blockchecksum)
    def encode(self, buf)
    def decode(self, buf, out)
class Lzf(Codec)
    """LZF codec for numcodecs."""
    def __init__(self, header)
    def encode(self, buf)
    def decode(self, buf, out)
class Lzma(Codec)
    """LZMA codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Lzw(Codec)
    """LZW codec for numcodecs."""
    def encode(self, buf)
    def decode(self, buf, out)
class PackBits(Codec)
    """PackBits codec for numcodecs."""
    def __init__(self, axis)
    def encode(self, buf)
    def decode(self, buf, out)
class Pglz(Codec)
    """PGLZ codec for numcodecs."""
    def __init__(self, header, strategy)
    def encode(self, buf)
    def decode(self, buf, out)
class Png(Codec)
    """PNG codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Qoi(Codec)
    """QOI codec for numcodecs."""
    def __init__(self)
    def encode(self, buf)
    def decode(self, buf, out)
class Rgbe(Codec)
    """RGBE codec for numcodecs."""
    def __init__(self, header, shape, rle)
    def encode(self, buf)
    def decode(self, buf, out)
class Rcomp(Codec)
    """Rcomp codec for numcodecs."""
    def __init__(self, shape, dtype, nblock)
    def encode(self, buf)
    def decode(self, buf, out)
class Snappy(Codec)
    """Snappy codec for numcodecs."""
    def encode(self, buf)
    def decode(self, buf, out)
class Spng(Codec)
    """SPNG codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Tiff(Codec)
    """TIFF codec for numcodecs."""
    def __init__(self, index, asrgb, verbose)
    def encode(self, buf)
    def decode(self, buf, out)
class Webp(Codec)
    """WebP codec for numcodecs."""
    def __init__(self, level, lossless, method, hasalpha)
    def encode(self, buf)
    def decode(self, buf, out)
class Xor(Codec)
    """XOR codec for numcodecs."""
    def __init__(self, shape, dtype, axis)
    def encode(self, buf)
    def decode(self, buf, out)
class Zfp(Codec)
    """ZFP codec for numcodecs."""
    def __init__(self, shape, dtype, strides, level, mode, execution, numthreads, chunksize, header)
    def encode(self, buf)
    def decode(self, buf, out)
class Zlib(Codec)
    """Zlib codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Zlibng(Codec)
    """Zlibng codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
class Zopfli(Codec)
    """Zopfli codec for numcodecs."""
    def encode(self, buf)
    def decode(self, buf, out)
class Zstd(Codec)
    """ZStandard codec for numcodecs."""
    def __init__(self, level)
    def encode(self, buf)
    def decode(self, buf, out)
def _flat(out)
def register_codecs(codecs, force, verbose)
def log_warning(msg)
```

### diffusion_policy/common/checkpoint_util.py

```
class TopKCheckpointManager()
    def __init__(self, save_dir, monitor_key, mode, k, format_str)
    def get_ckpt_path(self, data)
```

### diffusion_policy/common/cv2_util.py

```
def draw_reticle(img, u, v, label_color)
def draw_text(img)
def get_image_transform(input_res, output_res, bgr_to_rgb)
def optimal_row_cols(n_cameras, in_wh_ratio, max_resolution)
```

### diffusion_policy/common/env_util.py

```
def render_env_video(env, states, actions)
```

### diffusion_policy/common/json_logger.py

```
def read_json_log(path, required_keys)
class JsonLogger()
    def __init__(self, path, filter_fn)
    def start(self)
    def stop(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def log(self, data)
    def get_last_log(self)
```

### diffusion_policy/common/nested_dict_util.py

```
def nested_dict_map(f, x)
def nested_dict_reduce(f, x)
def nested_dict_check(f, x)
```

### diffusion_policy/common/normalize_util.py

```
def get_range_normalizer_from_stat(stat, output_max, output_min, range_eps)
def get_image_range_normalizer()
def get_identity_normalizer_from_stat(stat)
def robomimic_abs_action_normalizer_from_stat(stat, rotation_transformer)
def robomimic_abs_action_only_normalizer_from_stat(stat)
def robomimic_abs_action_only_dual_arm_normalizer_from_stat(stat)
def array_to_stats(arr)
```

### diffusion_policy/common/pose_trajectory_interpolator.py

```
def rotation_distance(a, b)
def pose_distance(start_pose, end_pose)
class PoseTrajectoryInterpolator()
    def __init__(self, times, poses)
    def times(self)
    def poses(self)
    def trim(self, start_t, end_t)
    def drive_to_waypoint(self, pose, time, curr_time, max_pos_speed, max_rot_speed)
    def schedule_waypoint(self, pose, time, max_pos_speed, max_rot_speed, curr_time, last_waypoint_time)
    def __call__(self, t)
```

### diffusion_policy/common/precise_sleep.py

```
def precise_sleep(dt, slack_time, time_func)
def precise_wait(t_end, slack_time, time_func)
```

### diffusion_policy/common/pymunk_override.py

```
"""This submodule contains helper functions to help with quick prototyping 
using pymunk together with pygame.

Intended to help with debugging and prototyping, not for actual production use
in a full application. The methods contained in this module is opinionated 
about your coordinate system and not in any way optimized. """
class DrawOptions(SpaceDebugDrawOptions)
    def __init__(self, surface)
    def draw_circle(self, pos, angle, radius, outline_color, fill_color)
    def draw_segment(self, a, b, color)
    def draw_fat_segment(self, a, b, radius, outline_color, fill_color)
    def draw_polygon(self, verts, radius, outline_color, fill_color)
    def draw_dot(self, size, pos, color)
def get_mouse_pos(surface)
def to_pygame(p, surface)
def from_pygame(p, surface)
def light_color(color)
```

### diffusion_policy/common/pymunk_util.py

```
def get_body_type(static)
def create_rectangle(space, pos_x, pos_y, width, height, density, static)
def create_rectangle_bb(space, left, bottom, right, top)
def create_circle(space, pos_x, pos_y, radius, density, static)
def get_body_state(body)
```

### diffusion_policy/common/pytorch_util.py

```
def dict_apply(x, func)
def pad_remaining_dims(x, target)
def dict_apply_split(x, split_func)
def dict_apply_reduce(x, reduce_func)
def replace_submodules(root_module, predicate, func)
def optimizer_to(optimizer, device)
```

### diffusion_policy/common/replay_buffer.py

```
def check_chunks_compatible(chunks, shape)
def rechunk_recompress_array(group, name, chunks, chunk_length, compressor, tmp_key)
def get_optimal_chunks(shape, dtype, target_chunk_bytes, max_chunk_length)
class ReplayBuffer()
    """Zarr-based temporal datastructure.
Assumes first dimension to be time. Only chunk in time dimension."""
    def __init__(self, root)
    def create_empty_zarr(cls, storage, root)
    def create_empty_numpy(cls)
    def create_from_group(cls, group)
    def create_from_path(cls, zarr_path, mode)
    def copy_from_store(cls, src_store, store, keys, chunks, compressors, if_exists)
    def copy_from_path(cls, zarr_path, backend, store, keys, chunks, compressors, if_exists)
    def save_to_store(self, store, chunks, compressors, if_exists)
    def save_to_path(self, zarr_path, chunks, compressors, if_exists)
    def resolve_compressor(compressor)
    def _resolve_array_compressor(cls, compressors, key, array)
    def _resolve_array_chunks(cls, chunks, key, array)
    def data(self)
    def meta(self)
    def update_meta(self, data)
    def episode_ends(self)
    def get_episode_idxs(self)
    def backend(self)
    def __repr__(self)
    def keys(self)
    def values(self)
    def items(self)
    def __getitem__(self, key)
    def __contains__(self, key)
    def n_steps(self)
    def n_episodes(self)
    def chunk_size(self)
    def episode_lengths(self)
    def add_episode(self, data, chunks, compressors)
    def drop_episode(self)
    def pop_episode(self)
    def extend(self, data)
    def get_episode(self, idx, copy)
    def get_episode_slice(self, idx)
    def get_steps_slice(self, start, stop, step, copy)
    def get_chunks(self)
    def set_chunks(self, chunks)
    def get_compressors(self)
    def set_compressors(self, compressors)
```

### diffusion_policy/common/robomimic_config_util.py

```
def get_robomimic_config(algo_name, hdf5_type, task_name, dataset_type)
```

### diffusion_policy/common/robomimic_util.py

```
class RobomimicAbsoluteActionConverter()
    def __init__(self, dataset_path, algo_name)
    def __len__(self)
    def convert_actions(self, states, actions)
    def convert_idx(self, idx)
    def convert_and_eval_idx(self, idx)
    def evaluate_rollout_error(env, states, actions, robot0_eef_pos, robot0_eef_quat, metric_skip_steps)
```

### diffusion_policy/common/sampler.py

```
def create_indices(episode_ends, sequence_length, episode_mask, pad_before, pad_after, debug)
def get_val_mask(n_episodes, val_ratio, seed)
def downsample_mask(mask, max_n, seed)
class SequenceSampler()
    def __init__(self, replay_buffer, sequence_length, pad_before, pad_after, keys, key_first_k, episode_mask)
    def __len__(self)
    def sample_sequence(self, idx)
```

### diffusion_policy/common/timestamp_accumulator.py

```
def get_accumulate_timestamp_idxs(timestamps, start_time, dt, eps, next_global_idx, allow_negative)
def align_timestamps(timestamps, target_global_idxs, start_time, dt, eps)
class TimestampObsAccumulator()
    def __init__(self, start_time, dt, eps)
    def __len__(self)
    def data(self)
    def actual_timestamps(self)
    def timestamps(self)
    def put(self, data, timestamps)
class TimestampActionAccumulator()
    def __init__(self, start_time, dt, eps)
    def __len__(self)
    def actions(self)
    def actual_timestamps(self)
    def timestamps(self)
    def put(self, actions, timestamps)
```

### diffusion_policy/dataset/base_dataset.py

```
class BaseLowdimDataset(Dataset)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
class BaseImageDataset(Dataset)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### diffusion_policy/dataset/blockpush_lowdim_dataset.py

```
class BlockPushLowdimDataset(BaseLowdimDataset)
    def __init__(self, zarr_path, horizon, pad_before, pad_after, obs_key, action_key, obs_eef_target, use_manual_normalizer, seed, val_ratio)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def get_all_actions(self)
    def __len__(self)
    def _sample_to_data(self, sample)
    def __getitem__(self, idx)
```

### diffusion_policy/dataset/kitchen_lowdim_dataset.py

```
class KitchenLowdimDataset(BaseLowdimDataset)
    def __init__(self, dataset_dir, horizon, pad_before, pad_after, seed, val_ratio)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### diffusion_policy/dataset/kitchen_mjl_lowdim_dataset.py

```
class KitchenMjlLowdimDataset(BaseLowdimDataset)
    def __init__(self, dataset_dir, horizon, pad_before, pad_after, abs_action, robot_noise_ratio, seed, val_ratio)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### diffusion_policy/dataset/mujoco_image_dataset.py

```
class MujocoImageDataset(BaseImageDataset)
    def __init__(self, zarr_path, horizon, pad_before, pad_after, seed, val_ratio, max_train_episodes)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def __len__(self)
    def _sample_to_data(self, sample)
    def __getitem__(self, idx)
def test()
```

### diffusion_policy/dataset/pusht_dataset.py

```
class PushTLowdimDataset(BaseLowdimDataset)
    def __init__(self, zarr_path, horizon, pad_before, pad_after, obs_key, state_key, action_key, seed, val_ratio, max_train_episodes)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def get_all_actions(self)
    def __len__(self)
    def _sample_to_data(self, sample)
    def __getitem__(self, idx)
```

### diffusion_policy/dataset/pusht_image_dataset.py

```
class PushTImageDataset(BaseImageDataset)
    def __init__(self, zarr_path, horizon, pad_before, pad_after, seed, val_ratio, max_train_episodes)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def __len__(self)
    def _sample_to_data(self, sample)
    def __getitem__(self, idx)
def test()
```

### diffusion_policy/dataset/real_pusht_image_dataset.py

```
class RealPushTImageDataset(BaseImageDataset)
    def __init__(self, shape_meta, dataset_path, horizon, pad_before, pad_after, n_obs_steps, n_latency_steps, use_cache, seed, val_ratio, max_train_episodes, delta_action)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
def zarr_resize_index_last_dim(zarr_arr, idxs)
def _get_replay_buffer(dataset_path, shape_meta, store)
def test()
```

### diffusion_policy/dataset/robomimic_replay_image_dataset.py

```
class RobomimicReplayImageDataset(BaseImageDataset)
    def __init__(self, shape_meta, dataset_path, horizon, pad_before, pad_after, n_obs_steps, abs_action, rotation_rep, use_legacy_normalizer, use_cache, seed, val_ratio)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
def _convert_actions(raw_actions, abs_action, rotation_transformer)
def _convert_robomimic_to_replay(store, shape_meta, dataset_path, abs_action, rotation_transformer, n_workers, max_inflight_tasks)
def normalizer_from_stat(stat)
```

### diffusion_policy/dataset/robomimic_replay_lowdim_dataset.py

```
class RobomimicReplayLowdimDataset(BaseLowdimDataset)
    def __init__(self, dataset_path, horizon, pad_before, pad_after, obs_keys, abs_action, rotation_rep, use_legacy_normalizer, seed, val_ratio, max_train_episodes)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
def normalizer_from_stat(stat)
def _data_to_obs(raw_obs, raw_actions, obs_keys, abs_action, rotation_transformer)
```

### diffusion_policy/env/block_pushing/block_pushing.py

```
"""Simple block environments for the XArm."""
def build_env_name(task, shared_memory, use_image_obs, use_normalized_env)
class BlockTaskVariant(Enum)
def sleep_spin(sleep_time_sec)
class BlockPush(Env)
    """Simple XArm environment for block pushing."""
    def __init__(self, control_frequency, task, image_size, shared_memory, seed, goal_dist_tolerance, effector_height, visuals_mode, abs_action)
    def pybullet_client(self)
    def robot(self)
    def workspace_uid(self)
    def target_effector_pose(self)
    def target_pose(self)
    def control_frequency(self)
    def connection_mode(self)
    def save_state(self)
    def set_goal_dist_tolerance(self, val)
    def get_control_frequency(self)
    def compute_state(self)
    def get_goal_translation(self)
    def get_obj_ids(self)
    def _setup_workspace_and_robot(self, end_effector)
    def _setup_pybullet_scene(self)
    def step_simulation_to_stabilize(self, nsteps)
    def seed(self, seed)
    def _set_robot_target_effector_pose(self, pose)
    def reset(self, reset_poses)
    def _compute_goal_distance(self, state)
    def _compute_reach_target(self, state)
    def _compute_state(self)
    def _step_robot_and_sim(self, action)
    def step(self, action)
    def succeeded(self)
    def goal_distance(self)
    def render(self, mode)
    def close(self)
    def calc_camera_params(self, image_size)
    def _render_camera(self, image_size)
    def _create_observation_space(self, image_size)
    def get_pybullet_state(self)
    def set_pybullet_state(self, state)
class BlockPushNormalized(Env)
    """Simple XArm environment for block pushing, normalized state and actions."""
    def __init__(self, control_frequency, task, image_size, shared_memory, seed)
    def get_control_frequency(self)
    def reach_target_translation(self)
    def seed(self, seed)
    def reset(self)
    def step(self, action)
    def render(self, mode)
    def close(self)
    def _normalize(values, values_min, values_max)
    def _unnormalize(values, values_min, values_max)
    def calc_normalized_action(cls, action)
    def calc_unnormalized_action(cls, norm_action)
    def calc_normalized_state(cls, state)
    def calc_unnormalized_state(cls, norm_state)
    def get_pybullet_state(self)
    def set_pybullet_state(self, state)
    def pybullet_client(self)
    def calc_camera_params(self, image_size)
    def _compute_state(self)

```python
def _create_observation_space(self, image_size):
        pi2 = math.pi * 2

        obs_dict = collections.OrderedDict(
            block_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            block_orientation=spaces.Box(low=-pi2, high=pi2, shape=(1,)),  # phi
            effector_translation=spaces.Box(
                low=self.workspace_bounds[0] - 0.1,  # Small buffer for to IK noise.
                high=self.workspace_bounds[1] + 0.1,
            ),  # x,y
            effector_target_translation=spaces.Box(
                low=self.workspace_bounds[0] - 0.1,  # Small buffer for to IK noise.
                high=self.workspace_bounds[1] + 0.1,
            ),  # x,y
            target_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            target_orientation=spaces.Box(
                low=-pi2,
                high=pi2,
                shape=(1,),
            ),  # theta
        )
        if image_size is not None:
            obs_dict["rgb"] = spaces.Box(
                low=0, high=255, shape=(image_size[0], image_size[1], 3), dtype=np.uint8
            )
        return spaces.Dict(obs_dict)
```
```

### diffusion_policy/env/block_pushing/block_pushing_discontinuous.py

```
"""Discontinuous block pushing."""
def build_env_name(task, shared_memory, use_image_obs)
class BlockTaskVariant(Enum)
class BlockPushDiscontinuous(BlockPush)
    """Discontinuous block pushing."""
    def __init__(self, control_frequency, task, image_size, shared_memory, seed, goal_dist_tolerance)
    def target_poses(self)
    def get_goal_translation(self)
    def _setup_pybullet_scene(self)
    def _reset_target_poses(self, workspace_center_x)
    def reset(self)
    def _compute_goal_distance(self, state)
    def _compute_state(self)
    def step(self, action)
    def dist(self, state, target)
    def _get_reward(self, state)
    def succeeded(self)
    def _create_observation_space(self, image_size)

```python
def _get_reward(self, state):
        """Reward is 1.0 if agent hits both goals and stays at second."""
        # This also statefully updates these values.
        self.min_dist_to_first_goal = min(
            self.dist(state, "target"), self.min_dist_to_first_goal
        )
        self.min_dist_to_second_goal = min(
            self.dist(state, "target2"), self.min_dist_to_second_goal
        )

        def _reward(thresh):
            reward_first = True if self.min_dist_to_first_goal < thresh else False
            reward_second = True if self.min_dist_to_second_goal < thresh else False
            return 1.0 if (reward_first and reward_second) else 0.0

        reward = _reward(self.goal_dist_tolerance)
        return reward
```

```python
def _create_observation_space(self, image_size):
        pi2 = math.pi * 2

        obs_dict = collections.OrderedDict(
            block_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            block_orientation=spaces.Box(low=-pi2, high=pi2, shape=(1,)),  # phi
            effector_translation=spaces.Box(
                # Small buffer for to IK noise.
                low=block_pushing.WORKSPACE_BOUNDS[0] - 0.1,
                high=block_pushing.WORKSPACE_BOUNDS[1] + 0.1,
            ),  # x,y
            effector_target_translation=spaces.Box(
                # Small buffer for to IK noise.
                low=block_pushing.WORKSPACE_BOUNDS[0] - 0.1,
                high=block_pushing.WORKSPACE_BOUNDS[1] + 0.1,
            ),  # x,y
            target_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            target_orientation=spaces.Box(
                low=-pi2,
                high=pi2,
                shape=(1,),
            ),  # theta
            target2_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            target2_orientation=spaces.Box(
                low=-pi2,
                high=pi2,
                shape=(1,),
            ),  # theta
        )
        if image_size is not None:
            obs_dict["rgb"] = spaces.Box(
                low=0, high=255, shape=(image_size[0], image_size[1], 3), dtype=np.uint8
            )
        return spaces.Dict(obs_dict)
```

```python
def _reward(thresh):
            reward_first = True if self.min_dist_to_first_goal < thresh else False
            reward_second = True if self.min_dist_to_second_goal < thresh else False
            return 1.0 if (reward_first and reward_second) else 0.0
```
```

### diffusion_policy/env/block_pushing/block_pushing_multimodal.py

```
"""Multimodal block environments for the XArm."""
def build_env_name(task, shared_memory, use_image_obs)
class BlockPushEventManager()
    def __init__(self)
    def reach(self, step, block_id)
    def target(self, step, block_id, target_id)
    def reset(self)
    def get_info(self)
class BlockPushMultimodal(BlockPush)
    """2 blocks, 2 targets."""
    def __init__(self, control_frequency, task, image_size, shared_memory, seed, goal_dist_tolerance, abs_action)
    def target_poses(self)
    def get_goal_translation(self)
    def _setup_pybullet_scene(self)
    def _reset_block_poses(self, workspace_center_x)
    def _reset_target_poses(self, workspace_center_x)
    def _reset_object_poses(self, workspace_center_x, workspace_center_y)
    def reset(self, reset_poses)
    def _get_target_pose(self, idx)
    def _compute_reach_target(self, state)
    def _compute_state(self)
    def step(self, action)
    def _step_robot_and_sim(self, action)
    def _get_reward(self, state)
    def _compute_goal_distance(self, state)
    def succeeded(self)
    def _create_observation_space(self, image_size)
    def get_pybullet_state(self)
    def set_pybullet_state(self, state)
class BlockPushHorizontalMultimodal(BlockPushMultimodal)
    def _reset_object_poses(self, workspace_center_x, workspace_center_y)
    def _reset_block_poses(self, workspace_center_y)
    def _reset_target_poses(self, workspace_center_y)

```python
def _get_reward(self, state):
        # Reward is 1. if both blocks are inside targets, but not the same target.
        targets = ["target", "target2"]

        def _block_target_dist(block, target):
            return np.linalg.norm(
                state["%s_translation" % block] - state["%s_translation" % target]
            )

        def _closest_target(block):
            # Distances to all targets.
            dists = [_block_target_dist(block, t) for t in targets]
            # Which is closest.
            closest_target = targets[np.argmin(dists)]
            closest_dist = np.min(dists)
            # Is it in the closest target?
            in_target = closest_dist < self.goal_dist_tolerance
            return closest_target, in_target

        blocks = ["block", "block2"]

        reward = 0.0

        for t_i, t in enumerate(targets):
            for b_i, b in enumerate(blocks):
                if self._in_target[t_i][b_i] == -1:
                    dist = _block_target_dist(b, t)
                    if dist < self.goal_dist_tolerance:
                        self._in_target[t_i][b_i] = 0
                        logger.info(
                            f"Block {b_i} entered target {t_i} on step {self._step_num}"
                        )
                        self._event_manager.target(step=self._step_num, block_id=b_i, target_id=t_i)
                        reward += 0.49

        b0_closest_target, b0_in_target = _closest_target("block")
        b1_closest_target, b1_in_target = _closest_target("block2")
        # reward = 0.0
        if b0_in_target and b1_in_target and (b0_closest_target != b1_closest_target):
            reward = 0.51
        return reward
```

```python
def _create_observation_space(self, image_size):
        pi2 = math.pi * 2

        obs_dict = collections.OrderedDict(
            block_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            block_orientation=spaces.Box(low=-pi2, high=pi2, shape=(1,)),  # phi
            block2_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            block2_orientation=spaces.Box(low=-pi2, high=pi2, shape=(1,)),  # phi
            effector_translation=spaces.Box(
                low=block_pushing.WORKSPACE_BOUNDS[0] - 0.1,
                high=block_pushing.WORKSPACE_BOUNDS[1] + 0.1,
            ),  # x,y
            effector_target_translation=spaces.Box(
                low=block_pushing.WORKSPACE_BOUNDS[0] - 0.1,
                high=block_pushing.WORKSPACE_BOUNDS[1] + 0.1,
            ),  # x,y
            target_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            target_orientation=spaces.Box(
                low=-pi2,
                high=pi2,
                shape=(1,),
            ),  # theta
            target2_translation=spaces.Box(low=-5, high=5, shape=(2,)),  # x,y
            target2_orientation=spaces.Box(
                low=-pi2,
                high=pi2,
                shape=(1,),
            ),  # theta
        )
        if image_size is not None:
            obs_dict["rgb"] = spaces.Box(
                low=0, high=255, shape=(image_size[0], image_size[1], 3), dtype=np.uint8
            )
        return spaces.Dict(obs_dict)
```
```

### diffusion_policy/env/block_pushing/oracles/discontinuous_push_oracle.py

```
"""Pushes to first target, waits, then pushes to second target."""
class DiscontinuousOrientedPushOracle(OrientedPushOracle)
    """Pushes to first target, waits, then pushes to second target."""
    def __init__(self, env, goal_tolerance, wait)
    def reset(self)
    def _action(self, time_step, policy_state)
```

### diffusion_policy/env/block_pushing/oracles/multimodal_push_oracle.py

```
"""Oracle for multimodal pushing task."""
class MultimodalOrientedPushOracle(OrientedPushOracle)
    """Oracle for multimodal pushing task."""
    def __init__(self, env, goal_dist_tolerance, action_noise_std)
    def reset(self)
    def _get_move_to_preblock(self, xy_pre_block, xy_ee)
    def _get_action_for_block_target(self, time_step, block, target)
    def _choose_goal_order(self)
    def _action(self, time_step, policy_state)
```

### diffusion_policy/env/block_pushing/oracles/oriented_push_oracle.py

```
"""Oracle for pushing task which orients the block then pushes it."""
class OrientedPushOracle(PyPolicy)
    """Oracle for pushing task which orients the block then pushes it."""
    def __init__(self, env, action_noise_std)
    def reset(self)
    def get_theta_from_vector(self, vector)
    def theta_to_rotation2d(self, theta)
    def rotate(self, theta, xy_dir_block_to_ee)
    def _get_action_info(self, time_step, block, target)
    def _get_move_to_preblock(self, xy_pre_block, xy_ee)
    def _get_move_to_block(self, xy_delta_to_nexttoblock, theta_threshold_to_orient, theta_error)
    def _get_push_block(self, theta_error, theta_threshold_to_orient, xy_delta_to_touchingblock)
    def _get_orient_block_left(self, xy_dir_block_to_ee, orient_circle_diameter, xy_block, xy_ee, theta_error, theta_threshold_flat_enough)
    def _get_orient_block_right(self, xy_dir_block_to_ee, orient_circle_diameter, xy_block, xy_ee, theta_error, theta_threshold_flat_enough)
    def _get_action_for_block_target(self, time_step, block, target)
    def _action(self, time_step, policy_state)
class OrientedPushNormalizedOracle(PyPolicy)
    """Oracle for pushing task which orients the block then pushes it."""
    def __init__(self, env)
    def reset(self)
    def _action(self, time_step, policy_state)
```

### diffusion_policy/env/block_pushing/oracles/pushing_info.py

```
"""Dataclass holding info needed for pushing oracles."""
class PushingInfo()
    """Holds onto info necessary for pushing state machine."""
```

### diffusion_policy/env/block_pushing/oracles/reach_oracle.py

```
"""Reach oracle."""
class ReachOracle(PyPolicy)
    """Oracle for moving to a specific spot relative to the block and target."""
    def __init__(self, env, block_pushing_oracles_action_std)
    def _action(self, time_step, policy_state)
```

### diffusion_policy/env/block_pushing/utils/pose3d.py

```
"""A simple 6DOF pose container."""
class NoCopyAsDict(object)
    """Base class for dataclasses. Avoids a copy in the asdict() call."""
    def asdict(self)
class Pose3d(NoCopyAsDict)
    """Simple container for translation and rotation."""
    def vec7(self)
    def serialize(self)
    def deserialize(data)
    def __eq__(self, other)
    def __ne__(self, other)
```

### diffusion_policy/env/block_pushing/utils/utils_pybullet.py

```
"""Assortment of utilities to interact with bullet within g3."""
def rotation_to_matrix(rotation)
def matrix_to_rotation(matrix)
def load_urdf(pybullet_client, file_path)
def add_visual_sphere(client, center, radius, rgba)
def pybullet_mat_to_numpy_4x4(pybullet_matrix)
def decompose_view_matrix(pybullet_view_matrix)
def world_obj_to_view(world_xyz_obj, world_quat_obj, camera_view, client)
def image_xy_to_view_ray(xy, cam_width, cam_height, proj_mat_inv)
def view_ray_to_world_ray(origin, vec, view_mat_inv)
def ray_to_plane_test(ray_origin, ray_vec, plane_origin, plane_normal)
def get_workspace(env)
def reset_camera_pose(env, view_type)
def _lists_to_tuple(obj)
class ObjState()
    """A container for storing pybullet object state."""
    def get_bullet_state(client, obj_id)
    def _get_joint_info(client, obj_id, joint_index)
    def set_bullet_state(self, client, obj_id)
    def serialize(self)
    def deserialize(data)
class XarmState(ObjState)
    """A container for storing pybullet robot state."""
    def get_bullet_state(client, obj_id, target_effector_pose, goal_translation)
    def serialize(self)
    def deserialize(data)
def _serialize_pybullet_state(pybullet_state)
def _deserialize_pybullet_state(state)
def write_pybullet_state(filename, pybullet_state, task, actions)
def read_pybullet_state(filename)
```

### diffusion_policy/env/block_pushing/utils/xarm_sim_robot.py

```
"""XArm Robot Kinematics."""
class XArmSimRobot()
    """A simulated PyBullet XArm robot, mostly for forward/inverse kinematics."""
    def __init__(self, pybullet_client, initial_joint_positions, end_effector, color)
    def _setup_end_effector(self, end_effector)
    def reset_joints(self, joint_values)
    def get_joints_measured(self)
    def get_joint_positions(self)
    def forward_kinematics(self)
    def inverse_kinematics(self, world_effector_pose, max_iterations, residual_threshold)
    def set_target_effector_pose(self, world_effector_pose)
    def set_target_joint_velocities(self, target_joint_velocities)
    def set_target_joint_positions(self, target_joint_positions)
    def set_alpha_transparency(self, alpha)
```

### diffusion_policy/env/kitchen/__init__.py

```
"""Environments using kitchen and Franka robot."""
```

### diffusion_policy/env/kitchen/base.py

```
class KitchenBase(KitchenTaskRelaxV1)
    def __init__(self, dataset_url, ref_max_score, ref_min_score, use_abs_action)
    def set_goal_masking(self, goal_masking)
    def _get_task_goal(self, task, actually_return_goal)
    def reset_model(self)
    def _get_reward_n_score(self, obs_dict)
    def step(self, a, b)
    def get_goal(self)
    def _split_data_into_seqs(self, data)

```python
def _get_reward_n_score(self, obs_dict):
        reward_dict, score = super(KitchenBase, self)._get_reward_n_score(obs_dict)
        reward = 0.0
        next_q_obs = obs_dict["qp"]
        next_obj_obs = obs_dict["obj_qp"]
        next_goal = self._get_task_goal(
            task=self.TASK_ELEMENTS, actually_return_goal=True
        )  # obs_dict['goal']
        idx_offset = len(next_q_obs)
        completions = []
        all_completed_so_far = True
        for element in self.tasks_to_complete:
            element_idx = OBS_ELEMENT_INDICES[element]
            distance = np.linalg.norm(
                next_obj_obs[..., element_idx - idx_offset] - next_goal[element_idx]
            )
            complete = distance < BONUS_THRESH
            condition = (
                complete and all_completed_so_far
                if not self.COMPLETE_IN_ANY_ORDER
                else complete
            )
            if condition:  # element == self.tasks_to_complete[0]:
                print("Task {} completed!".format(element))
                completions.append(element)
            all_completed_so_far = all_completed_so_far and complete
        if self.REMOVE_TASKS_WHEN_COMPLETE:
            [self.tasks_to_complete.remove(element) for element in completions]
        bonus = float(len(completions))
        reward_dict["bonus"] = bonus
        reward_dict["r_total"] = bonus
        score = bonus
        return reward_dict, score
```
```

### diffusion_policy/env/kitchen/kitchen_lowdim_wrapper.py

```
class KitchenLowdimWrapper(Env)
    def __init__(self, env, init_qpos, init_qvel, render_hw)
    def action_space(self)
    def observation_space(self)
    def seed(self, seed)
    def reset(self)
    def render(self, mode)
    def step(self, a)

```python
def observation_space(self):
        return self.env.observation_space
```
```

### diffusion_policy/env/kitchen/kitchen_util.py

```
def parse_mjl_logs(read_filename, skipamount)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/base_robot.py

```
class BaseRobot(object)
    """Base class for all robot classes."""
    def __init__(self, n_jnt, n_obj, pos_bounds, vel_bounds, calibration_path, is_hardware, device_name, overlay, calibration_mode, observation_cache_maxsize)
    def n_jnt(self)
    def n_obj(self)
    def n_dofs(self)
    def pos_bounds(self)
    def vel_bounds(self)
    def is_hardware(self)
    def device_name(self)
    def calibration_path(self)
    def overlay(self)
    def has_obj(self)
    def calibration_mode(self)
    def observation_cache_maxsize(self)
    def observation_cache(self)
    def clip_positions(self, positions)

```python
def observation_cache_maxsize(self):
        return self._observation_cache_maxsize
```

```python
def observation_cache(self):
        return self._observation_cache
```
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/franka/kitchen_multitask_v0.py

```
"""Kitchen environment for long horizon manipulation """
class KitchenV0(RobotEnv)
    def __init__(self, robot_params, frame_skip, use_abs_action)
    def _get_reward_n_score(self, obs_dict)
    def step(self, a, b)
    def _get_obs(self)
    def reset_model(self)
    def evaluate_success(self, paths)
    def close_env(self)
    def set_goal(self, goal)
    def _get_task_goal(self)
    def goal_space(self)
    def convert_to_active_observation(self, observation)
class KitchenTaskRelaxV1(KitchenV0)
    """Kitchen environment with proper camera and goal setup"""
    def __init__(self, use_abs_action)
    def _get_reward_n_score(self, obs_dict)
    def render(self, mode, width, height, custom)

```python
def _get_reward_n_score(self, obs_dict):
        raise NotImplementedError()
```

```python
def _get_obs(self):
        t, qp, qv, obj_qp, obj_qv = self.robot.get_obs(
            self, robot_noise_ratio=self.robot_noise_ratio)

        self.obs_dict = {}
        self.obs_dict['t'] = t
        self.obs_dict['qp'] = qp
        self.obs_dict['qv'] = qv
        self.obs_dict['obj_qp'] = obj_qp
        self.obs_dict['obj_qv'] = obj_qv
        self.obs_dict['goal'] = self.goal
        if self.goal_concat:
            return np.concatenate([self.obs_dict['qp'], self.obs_dict['obj_qp'], self.obs_dict['goal']])
```

```python
def convert_to_active_observation(self, observation):
        return observation
```

```python
def _get_reward_n_score(self, obs_dict):
        reward_dict = {}
        reward_dict['true_reward'] = 0.
        reward_dict['bonus'] = 0.
        reward_dict['r_total'] = 0.
        score = 0.
        return reward_dict, score
```
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/franka/robot/franka_robot.py

```
class Robot(BaseRobot)
    """Abstracts away the differences between the robot_simulation and robot_hardware"""
    def __init__(self)
    def _read_specs_from_config(self, robot_configs)
    def _de_calib(self, qp_mj, qv_mj)
    def _calib(self, qp_ad, qv_ad)
    def _observation_cache_refresh(self, env)
    def get_obs_from_cache(self, env, index)
    def get_obs(self, env, robot_noise_ratio, object_noise_ratio, sim_mimic_hardware)
    def ctrl_position_limits(self, ctrl_position)
    def step(self, env, ctrl_desired, step_duration, sim_override)
    def reset(self, env, reset_pose, reset_vel, overlay_mimic_reset_pose, sim_override)
    def close(self)
class Robot_PosAct(Robot)
    def ctrl_velocity_limits(self, ctrl_position, step_duration)
class Robot_VelAct(Robot)
    def ctrl_velocity_limits(self, ctrl_velocity, step_duration)

```python
def _observation_cache_refresh(self, env):
        for _ in range(self.observation_cache_maxsize):
            self.get_obs(env, sim_mimic_hardware=False)
```
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/mujoco_env.py

```
"""Base environment for MuJoCo-based environments."""
class MujocoEnv(Env)
    """Superclass for all MuJoCo environments."""
    def __init__(self, model_path, frame_skip, camera_settings, use_dm_backend)
    def seed(self, seed)
    def _seed(self, seed)
    def reset_model(self)
    def reset(self)
    def _reset(self)
    def set_state(self, qpos, qvel)
    def dt(self)
    def do_simulation(self, ctrl, n_frames)
    def render(self, mode, width, height, camera_id)
    def close(self)
    def mj_render(self)
    def state_vector(self)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/robot_env.py

```
"""Base class for robotics environments."""
class RobotEnv(MujocoEnv)
    """Base environment for all adept robots."""
    def __init__(self, model_path, robot, frame_skip, camera_settings)
    def robot(self)
    def n_jnt(self)
    def n_obj(self)
    def skip(self)
    def initializing(self)
    def close_env(self)
    def make_robot(self, n_jnt, n_obj, is_hardware, device_name, legacy)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/simulation/module.py

```
"""Module for caching Python modules related to simulation."""
def get_mujoco_py()
def get_mujoco_py_mjlib()
def get_dm_mujoco()
def get_dm_viewer()
def get_dm_render()
def _mj_warning_fn(warn_data)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/simulation/renderer.py

```
"""Module for viewing Physics objects in the DM Control viewer."""
class RenderMode(Enum)
    """Rendering modes for offscreen rendering."""
class Renderer(ABC)
    """Base interface for rendering simulations."""
    def __init__(self, camera_settings)
    def close(self)
    def render_to_window(self)
    def render_offscreen(self, width, height, mode, camera_id)
    def _update_camera(self, camera)
class MjPyRenderer(Renderer)
    """Class for rendering mujoco_py simulations."""
    def __init__(self, sim)
    def render_to_window(self)
    def render_offscreen(self, width, height, mode, camera_id)
    def close(self)
class DMRenderer(Renderer)
    """Class for rendering DM Control Physics objects."""
    def __init__(self, physics)
    def render_to_window(self)
    def render_offscreen(self, width, height, mode, camera_id)
    def close(self)
class DMRenderWindow()
    """Class that encapsulates a graphical window."""
    def __init__(self, width, height, title)
    def camera(self)
    def close(self)
    def load_model(self, physics)
    def run_frame(self)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/simulation/sim_robot.py

```
"""Module for loading MuJoCo models."""
class MujocoSimRobot()
    """Class that encapsulates a MuJoCo simulation.

This class exposes methods that are agnostic to the simulation backend.
Two backends are supported:
1. mujoco_py - MuJoCo v1.50
2. dm_control - MuJoCo v2.00"""
    def __init__(self, model_file, use_dm_backend, camera_settings)
    def close(self)
    def save_binary(self, path)
    def get_mjlib(self)
    def _patch_mjlib_accessors(self, model, data)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/utils/config.py

```
def read_config_from_node(root_node, parent_name, child_name, dtype)
def get_config_root_node(config_file_name, config_file_data)
def read_config_from_xml(config_file_name, parent_name, child_name, dtype)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/utils/configurable.py

```
def import_class_from_path(class_path)
class ConfigCache(object)
    """Configuration class to store constructor arguments.

This is used to store parameters to pass to Gym environments at init time."""
    def __init__(self)
    def set_default_config(self, config)
    def set_config(self, cls_or_env_id, config)
    def get_config(self, cls_or_env_id)
    def clear_config(self, cls_or_env_id)
    def _get_config_key(self, cls_or_env_id)
def configurable(config_id, pickleable, config_cache)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/utils/parse_demos.py

```
def viewer(env, mode, filename, frame_size, camera_id, render)
def render_demos(env, data, filename, render)
def gather_training_data(env, data, filename, render)
def main(env, demo_dir, skip, graph, save_logs, view, render)
```

### diffusion_policy/env/kitchen/relay_policy_learning/adept_envs/adept_envs/utils/quatmath.py

```
def mulQuat(qa, qb)
def negQuat(quat)
def quat2Vel(quat, dt)
def quatDiff2Vel(quat1, quat2, dt)
def axis_angle2quat(axis, angle)
def euler2mat(euler)
def euler2quat(euler)
def mat2euler(mat)
def mat2quat(mat)
def quat2euler(quat)
def quat2mat(quat)
```

### diffusion_policy/env/kitchen/v0.py

```
class KitchenMicrowaveKettleBottomBurnerLightV0(KitchenBase)
class KitchenMicrowaveKettleLightSliderV0(KitchenBase)
class KitchenKettleMicrowaveLightSliderV0(KitchenBase)
class KitchenAllV0(KitchenBase)
```

### diffusion_policy/env/pusht/pusht_env.py

```
def pymunk_to_shapely(body, shapes)
class PushTEnv(Env)
    def __init__(self, legacy, block_cog, damping, render_action, render_size, reset_to_state)
    def reset(self)
    def step(self, action)
    def render(self, mode)
    def teleop_agent(self)
    def _get_obs(self)
    def _get_goal_pose_body(self, pose)
    def _get_info(self)
    def _render_frame(self, mode)
    def close(self)
    def seed(self, seed)
    def _handle_collision(self, arbiter, space, data)
    def _set_state(self, state)
    def _set_state_local(self, state_local)
    def _setup(self)
    def _add_segment(self, a, b, radius)
    def add_circle(self, position, radius)
    def add_box(self, position, height, width)
    def add_tee(self, position, angle, scale, color, mask)

```python
def _get_obs(self):
        obs = np.array(
            tuple(self.agent.position) \
            + tuple(self.block.position) \
            + (self.block.angle % (2 * np.pi),))
        return obs
```
```

### diffusion_policy/env/pusht/pusht_image_env.py

```
class PushTImageEnv(PushTEnv)
    def __init__(self, legacy, block_cog, damping, render_size)
    def _get_obs(self)
    def render(self, mode)

```python
def _get_obs(self):
        img = super()._render_frame(mode='rgb_array')

        agent_pos = np.array(self.agent.position)
        img_obs = np.moveaxis(img.astype(np.float32) / 255, -1, 0)
        obs = {
            'image': img_obs,
            'agent_pos': agent_pos
        }

        # draw action
        if self.latest_action is not None:
            action = np.array(self.latest_action)
            coord = (action / 512 * 96).astype(np.int32)
            marker_size = int(8/96*self.render_size)
            thickness = int(1/96*self.render_size)
            cv2.drawMarker(img, coord,
                color=(255,0,0), markerType=cv2.MARKER_CROSS,
                markerSize=marker_size, thickness=thickness)
        self.render_cache = img

        return obs
```
```

### diffusion_policy/env/pusht/pusht_keypoints_env.py

```
class PushTKeypointsEnv(PushTEnv)
    def __init__(self, legacy, block_cog, damping, render_size, keypoint_visible_rate, agent_keypoints, draw_keypoints, reset_to_state, render_action, local_keypoint_map, color_map)
    def genenerate_keypoint_manager_params(cls)
    def _get_obs(self)
    def _render_frame(self, mode)

```python
def _get_obs(self):
        # get keypoints
        obj_map = {
            'block': self.block
        }
        if self.agent_keypoints:
            obj_map['agent'] = self.agent

        kp_map = self.kp_manager.get_keypoints_global(
            pose_map=obj_map, is_obj=True)
        # python dict guerentee order of keys and values
        kps = np.concatenate(list(kp_map.values()), axis=0)

        # select keypoints to drop
        n_kps = kps.shape[0]
        visible_kps = self.np_random.random(size=(n_kps,)) < self.keypoint_visible_rate
        kps_mask = np.repeat(visible_kps[:,None], 2, axis=1)

        # save keypoints for rendering
        vis_kps = kps.copy()
        vis_kps[~visible_kps] = 0
        draw_kp_map = {
            'block': vis_kps[:len(kp_map['block'])]
        }
        if self.agent_keypoints:
            draw_kp_map['agent'] = vis_kps[len(kp_map['block']):]
        self.draw_kp_map = draw_kp_map
        
        # construct obs
        obs = kps.flatten()
        obs_mask = kps_mask.flatten()
        if not self.agent_keypoints:
            # passing agent position when keypoints are not available
            agent_pos = np.array(self.agent.position)
            obs = np.concatenate([
                obs, agent_pos
            ])
            obs_mask = np.concatenate([
                obs_mask, np.ones((2,), dtype=bool)
            ])

        # obs, obs_mask
        obs = np.concatenate([
            obs, obs_mask.astype(obs.dtype)
        ], axis=0)
        return obs
```
```

### diffusion_policy/env/pusht/pymunk_keypoint_manager.py

```
def farthest_point_sampling(points, n_points, init_idx)
class PymunkKeypointManager()
    def __init__(self, local_keypoint_map, color_map)
    def kwargs(self)
    def create_from_pusht_env(cls, env, n_block_kps, n_agent_kps, seed)
    def get_tf_img(pose)
    def get_tf_img_obj(cls, obj)
    def get_keypoints_global(self, pose_map, is_obj)
    def draw_keypoints(self, img, kps_map, radius)
    def draw_keypoints_pose(self, img, pose_map, is_obj)
def test()
```

### diffusion_policy/env/pusht/pymunk_override.py

```
"""This submodule contains helper functions to help with quick prototyping 
using pymunk together with pygame.

Intended to help with debugging and prototyping, not for actual production use
in a full application. The methods contained in this module is opinionated 
about your coordinate system and not in any way optimized. """
class DrawOptions(SpaceDebugDrawOptions)
    def __init__(self, surface)
    def draw_circle(self, pos, angle, radius, outline_color, fill_color)
    def draw_segment(self, a, b, color)
    def draw_fat_segment(self, a, b, radius, outline_color, fill_color)
    def draw_polygon(self, verts, radius, outline_color, fill_color)
    def draw_dot(self, size, pos, color)
def get_mouse_pos(surface)
def to_pygame(p, surface)
def from_pygame(p, surface)
def light_color(color)
```

### diffusion_policy/env/robomimic/robomimic_image_wrapper.py

```
class RobomimicImageWrapper(Env)
    def __init__(self, env, shape_meta, init_state, render_obs_key)
    def get_observation(self, raw_obs)
    def seed(self, seed)
    def reset(self)
    def step(self, action)
    def render(self, mode)
def test()

```python
def get_observation(self, raw_obs=None):
        if raw_obs is None:
            raw_obs = self.env.get_observation()
        
        self.render_cache = raw_obs[self.render_obs_key]

        obs = dict()
        for key in self.observation_space.keys():
            obs[key] = raw_obs[key]
        return obs
```
```

### diffusion_policy/env/robomimic/robomimic_lowdim_wrapper.py

```
class RobomimicLowdimWrapper(Env)
    def __init__(self, env, obs_keys, init_state, render_hw, render_camera_name)
    def get_observation(self)
    def seed(self, seed)
    def reset(self)
    def step(self, action)
    def render(self, mode)
def test()

```python
def get_observation(self):
        raw_obs = self.env.get_observation()
        obs = np.concatenate([
            raw_obs[key] for key in self.obs_keys
        ], axis=0)
        return obs
```
```

### diffusion_policy/env_runner/base_image_runner.py

```
class BaseImageRunner()
    def __init__(self, output_dir)
    def run(self, policy)
```

### diffusion_policy/env_runner/base_lowdim_runner.py

```
class BaseLowdimRunner()
    def __init__(self, output_dir)
    def run(self, policy)
```

### diffusion_policy/env_runner/blockpush_lowdim_runner.py

```
class BlockPushLowdimRunner(BaseLowdimRunner)
    def __init__(self, output_dir, n_train, n_train_vis, train_start_seed, n_test, n_test_vis, test_start_seed, max_steps, n_obs_steps, n_action_steps, fps, crf, past_action, abs_action, obs_eef_target, tqdm_interval_sec, n_envs)
    def run(self, policy)
```

### diffusion_policy/env_runner/kitchen_lowdim_runner.py

```
class KitchenLowdimRunner(BaseLowdimRunner)
    def __init__(self, output_dir, dataset_dir, n_train, n_train_vis, train_start_seed, n_test, n_test_vis, test_start_seed, max_steps, n_obs_steps, n_action_steps, render_hw, fps, crf, past_action, tqdm_interval_sec, abs_action, robot_noise_ratio, n_envs)
    def run(self, policy)
```

### diffusion_policy/env_runner/pusht_image_runner.py

```
class PushTImageRunner(BaseImageRunner)
    def __init__(self, output_dir, n_train, n_train_vis, train_start_seed, n_test, n_test_vis, legacy_test, test_start_seed, max_steps, n_obs_steps, n_action_steps, fps, crf, render_size, past_action, tqdm_interval_sec, n_envs)
    def run(self, policy)
```

### diffusion_policy/env_runner/pusht_keypoints_runner.py

```
class PushTKeypointsRunner(BaseLowdimRunner)
    def __init__(self, output_dir, keypoint_visible_rate, n_train, n_train_vis, train_start_seed, n_test, n_test_vis, legacy_test, test_start_seed, max_steps, n_obs_steps, n_action_steps, n_latency_steps, fps, crf, agent_keypoints, past_action, tqdm_interval_sec, n_envs)
    def run(self, policy)
```

### diffusion_policy/env_runner/real_pusht_image_runner.py

```
class RealPushTImageRunner(BaseImageRunner)
    def __init__(self, output_dir)
    def run(self, policy)
```

### diffusion_policy/env_runner/robomimic_image_runner.py

```
def create_env(env_meta, shape_meta, enable_render)
class RobomimicImageRunner(BaseImageRunner)
    """Robomimic envs already enforces number of steps."""
    def __init__(self, output_dir, dataset_path, shape_meta, n_train, n_train_vis, train_start_idx, n_test, n_test_vis, test_start_seed, max_steps, n_obs_steps, n_action_steps, render_obs_key, fps, crf, past_action, abs_action, tqdm_interval_sec, n_envs)
    def run(self, policy)
    def undo_transform_action(self, action)
```

### diffusion_policy/env_runner/robomimic_lowdim_runner.py

```
def create_env(env_meta, obs_keys)
class RobomimicLowdimRunner(BaseLowdimRunner)
    """Robomimic envs already enforces number of steps."""
    def __init__(self, output_dir, dataset_path, obs_keys, n_train, n_train_vis, train_start_idx, n_test, n_test_vis, test_start_seed, max_steps, n_obs_steps, n_action_steps, n_latency_steps, render_hw, render_camera_name, fps, crf, past_action, abs_action, tqdm_interval_sec, n_envs)
    def run(self, policy)
    def undo_transform_action(self, action)
```

### diffusion_policy/gym_util/async_vector_env.py

```
"""Back ported methods: call, set_attr from v0.26
Disabled auto-reset after done
Added render method."""
class AsyncState(Enum)
class AsyncVectorEnv(VectorEnv)
    """Vectorized environment that runs multiple environments in parallel. It
uses `multiprocessing` processes, and pipes for communication.
Parameters
----------
env_fns : iterable of callable
    Functions that create the environments.
observation_space : `gym.spaces.Space` instance, optional
    Observa"""
    def __init__(self, env_fns, dummy_env_fn, observation_space, action_space, shared_memory, copy, context, daemon, worker)
    def seed(self, seeds)
    def reset_async(self)
    def reset_wait(self, timeout)
    def step_async(self, actions)
    def step_wait(self, timeout)
    def close_extras(self, timeout, terminate)
    def _poll(self, timeout)
    def _check_observation_spaces(self)
    def _assert_is_running(self)
    def _raise_if_errors(self, successes)
    def call_async(self, name)
    def call_wait(self, timeout)
    def call(self, name)
    def call_each(self, name, args_list, kwargs_list, timeout)
    def set_attr(self, name, values)
    def render(self)
def _worker(index, env_fn, pipe, parent_pipe, shared_memory, error_queue)
def _worker_shared_memory(index, env_fn, pipe, parent_pipe, shared_memory, error_queue)

```python
def _check_observation_spaces(self):
        self._assert_is_running()
        for pipe in self.parent_pipes:
            pipe.send(("_check_observation_space", self.single_observation_space))
        same_spaces, successes = zip(*[pipe.recv() for pipe in self.parent_pipes])
        self._raise_if_errors(successes)
        if not all(same_spaces):
            raise RuntimeError(
                "Some environments have an observation space "
                "different from `{0}`. In order to batch observations, the "
                "observation spaces from all environments must be "
                "equal.".format(self.single_observation_space)
            )
```
```

### diffusion_policy/gym_util/multistep_wrapper.py

```
def stack_repeated(x, n)
def repeated_box(box_space, n)
def repeated_space(space, n)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def aggregate(data, method)
def stack_last_n_obs(all_obs, n_steps)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, n_obs_steps, n_action_steps, max_episode_steps, reward_agg_method)
    def reset(self)
    def step(self, action)
    def _get_obs(self, n_steps)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def run_dill_function(self, dill_fn)
    def get_infos(self)

```python
def _get_obs(self, n_steps=1):
        """
        Output (n_steps,) + obs_shape
        """
        assert(len(self.obs) > 0)
        if isinstance(self.observation_space, spaces.Box):
            return stack_last_n_obs(self.obs, n_steps)
        elif isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                result[key] = stack_last_n_obs(
                    [obs[key] for obs in self.obs],
                    n_steps
                )
            return result
        else:
            raise RuntimeError('Unsupported space type')
```

```python
def get_rewards(self):
        return self.reward
```
```

### diffusion_policy/gym_util/sync_vector_env.py

```
class SyncVectorEnv(VectorEnv)
    """Vectorized environment that serially runs multiple environments.
Parameters
----------
env_fns : iterable of callable
    Functions that create the environments.
observation_space : `gym.spaces.Space` instance, optional
    Observation space of a single environment. If `None`, then the
    observati"""
    def __init__(self, env_fns, observation_space, action_space, copy)
    def seed(self, seeds)
    def reset_wait(self)
    def step_async(self, actions)
    def step_wait(self)
    def close_extras(self)
    def _check_observation_spaces(self)
    def call(self, name)
    def call_each(self, name, args_list, kwargs_list)
    def render(self)
    def set_attr(self, name, values)

```python
def _check_observation_spaces(self):
        for env in self.envs:
            if not (env.observation_space == self.single_observation_space):
                break
        else:
            return True
        raise RuntimeError(
            "Some environments have an observation space "
            "different from `{0}`. In order to batch observations, the "
            "observation spaces from all environments must be "
            "equal.".format(self.single_observation_space)
        )
```
```

### diffusion_policy/gym_util/video_recording_wrapper.py

```
class VideoRecordingWrapper(Wrapper)
    def __init__(self, env, video_recoder, mode, file_path, steps_per_render)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### diffusion_policy/gym_util/video_wrapper.py

```
class VideoWrapper(Wrapper)
    def __init__(self, env, mode, enabled, steps_per_render)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### diffusion_policy/model/bet/action_ae/__init__.py

```
class AbstractActionAE(SaveModule, ABC)
    def fit_model(self, input_dataloader, eval_dataloader, obs_encoding_net)
    def encode_into_latent(self, input_action, input_rep)
    def decode_actions(self, latent_action_batch, input_rep_batch)
    def num_latents(self)
```

### diffusion_policy/model/bet/action_ae/discretizers/k_means.py

```
class KMeansDiscretizer(DictOfTensorMixin)
    """Simplified and modified version of KMeans algorithm  from sklearn."""
    def __init__(self, action_dim, num_bins, predict_offsets)
    def fit_discretizer(self, input_actions)
    def suggested_actions(self)
    def _kmeans(cls, x, ncluster, niter)
    def encode_into_latent(self, input_action, input_rep)
    def decode_actions(self, latent_action_batch, input_rep_batch)
    def discretized_space(self)
    def latent_dim(self)
    def num_latents(self)
```

### diffusion_policy/model/bet/latent_generators/latent_generator.py

```
class AbstractLatentGenerator(ABC, SaveModule)
    """Abstract class for a generative model that can generate latents given observation representations.

In the probabilisitc sense, this model fits and samples from P(latent|observation) given some observation."""
    def get_latent_and_loss(self, obs_rep, target_latents, seq_masks)
    def generate_latents(self, seq_obses, seq_masks)
    def get_optimizer(self, weight_decay, learning_rate, betas)
class LatentGeneratorDataParallel(DataParallel)
    def get_latent_and_loss(self)
    def generate_latents(self)
    def get_optimizer(self)
```

### diffusion_policy/model/bet/latent_generators/mingpt.py

```
class MinGPT(AbstractLatentGenerator)
    def __init__(self, input_dim, n_layer, n_head, n_embd, embd_pdrop, resid_pdrop, attn_pdrop, block_size, vocab_size, latent_dim, action_dim, discrete_input, predict_offsets, offset_loss_scale, focal_loss_gamma)
    def get_latent_and_loss(self, obs_rep, target_latents, seq_masks, return_loss_components)
    def generate_latents(self, obs_rep)
    def get_optimizer(self, weight_decay, learning_rate, betas)
```

### diffusion_policy/model/bet/latent_generators/transformer.py

```
class Transformer(AbstractLatentGenerator)
    def __init__(self, input_dim, num_bins, action_dim, horizon, focal_loss_gamma, offset_loss_scale)
    def get_optimizer(self)
    def get_latent_and_loss(self, obs_rep, target_latents, return_loss_components)
    def generate_latents(self, obs_rep)
```

### diffusion_policy/model/bet/libraries/loss_fn.py

```
def soft_cross_entropy(input, target)
class FocalLoss(Module)
    """Focal Loss, as described in https://arxiv.org/abs/1708.02002.
It is essentially an enhancement to cross entropy loss and is
useful for classification tasks when there is a large class imbalance.
x is expected to contain raw, unnormalized scores for each class.
y is expected to contain class labels.
"""
    def __init__(self, alpha, gamma, reduction, ignore_index)
    def __repr__(self)
    def forward(self, x, y)
def focal_loss(alpha, gamma, reduction, ignore_index, device, dtype)
```

### diffusion_policy/model/bet/libraries/mingpt/model.py

```
"""GPT model:
- the initial stem consists of a combination of token encoding and a positional encoding
- the meat of it is a uniform sequence of Transformer blocks
    - each Transformer is a sequential combination of a 1-hidden-layer MLP block and a self-attention block
    - all blocks feed into a central residual pathway similar to resnets
- the final decoder is a linear projection into a vanilla Softmax classifier"""
class GPTConfig()
    """base GPT config, params common to all GPT versions"""
    def __init__(self, vocab_size, block_size)
class GPT1Config(GPTConfig)
    """GPT-1 like network roughly 125M params"""
class CausalSelfAttention(Module)
    """A vanilla multi-head masked self-attention layer with a projection at the end.
It is possible to use torch.nn.MultiheadAttention here but I am including an
explicit implementation here to show that there is nothing too scary here."""
    def __init__(self, config)
    def forward(self, x)
class Block(Module)
    """an unassuming Transformer block"""
    def __init__(self, config)
    def forward(self, x)
class GPT(Module)
    """the full GPT language model, with a context size of block_size"""
    def __init__(self, config)
    def get_block_size(self)
    def _init_weights(self, module)
    def configure_optimizers(self, train_config)
    def forward(self, idx, targets)
```

### diffusion_policy/model/bet/libraries/mingpt/trainer.py

```
"""Simple training loop; Boilerplate that could apply to any arbitrary neural network,
so nothing in this file really has anything to do with GPT specifically."""
class TrainerConfig()
    def __init__(self)
class Trainer()
    def __init__(self, model, train_dataset, test_dataset, config)
    def save_checkpoint(self)
    def train(self)
```

### diffusion_policy/model/bet/libraries/mingpt/utils.py

```
def set_seed(seed)
def top_k_logits(logits, k)
def sample(model, x, steps, temperature, sample, top_k)
```

### diffusion_policy/model/bet/utils.py

```
def mlp(input_dim, hidden_dim, output_dim, hidden_depth, output_mod)
class eval_mode()
    def __init__(self)
    def __enter__(self)
    def __exit__(self)
def freeze_module(module)
def set_seed_everywhere(seed)
def shuffle_along_axis(a, axis)
def transpose_batch_timestep()
class TrainWithLogger()
    def reset_log(self)
    def log_append(self, log_key, length, loss_components)
    def flush_log(self, epoch, iterator)
class SaveModule(Module)
    def set_snapshot_path(self, path)
    def save_snapshot(self)
    def load_snapshot(self)
def split_datasets(dataset, train_fraction, random_seed)
```

### diffusion_policy/model/common/dict_of_tensor_mixin.py

```
class DictOfTensorMixin(Module)
    def __init__(self, params_dict)
    def device(self)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
```

### diffusion_policy/model/common/lr_scheduler.py

```
def get_scheduler(name, optimizer, num_warmup_steps, num_training_steps)
```

### diffusion_policy/model/common/module_attr_mixin.py

```
class ModuleAttrMixin(Module)
    def __init__(self)
    def device(self)
    def dtype(self)
```

### diffusion_policy/model/common/normalizer.py

```
class LinearNormalizer(DictOfTensorMixin)
    def fit(self, data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
    def __call__(self, x)
    def __getitem__(self, key)
    def __setitem__(self, key, value)
    def _normalize_impl(self, x, forward)
    def normalize(self, x)
    def unnormalize(self, x)
    def get_input_stats(self)
    def get_output_stats(self, key)
class SingleFieldLinearNormalizer(DictOfTensorMixin)
    def fit(self, data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
    def create_fit(cls, data)
    def create_manual(cls, scale, offset, input_stats_dict)
    def create_identity(cls, dtype)
    def normalize(self, x)
    def unnormalize(self, x)
    def get_input_stats(self)
    def get_output_stats(self)
    def __call__(self, x)
def _fit(data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
def _normalize(x, params, forward)
def test()
```

### diffusion_policy/model/common/rotation_transformer.py

```
class RotationTransformer()
    def __init__(self, from_rep, to_rep, from_convention, to_convention)
    def _apply_funcs(x, funcs)
    def forward(self, x)
    def inverse(self, x)
def test()
```

### diffusion_policy/model/common/shape_util.py

```
def get_module_device(m)
def get_output_shape(input_shape, net)
```

### diffusion_policy/model/common/tensor_util.py

```
"""A collection of utilities for working with nested tensor structures consisting
of numpy arrays and torch tensors."""
def recursive_dict_list_tuple_apply(x, type_func_dict)
def map_tensor(x, func)
def map_ndarray(x, func)
def map_tensor_ndarray(x, tensor_func, ndarray_func)
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

### diffusion_policy/model/diffusion/conditional_unet1d.py

```
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups, cond_predict_scale)
    def forward(self, x, cond)
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, local_cond_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale)
    def forward(self, sample, timestep, local_cond, global_cond)
```

### diffusion_policy/model/diffusion/conv1d_components.py

```
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
def test()
```

### diffusion_policy/model/diffusion/ema_model.py

```
class EMAModel()
    """Exponential Moving Average of models weights"""
    def __init__(self, model, update_after_step, inv_gamma, power, min_value, max_value)
    def get_decay(self, optimization_step)
    def step(self, new_model)
```

### diffusion_policy/model/diffusion/mask_generator.py

```
def get_intersection_slice_mask(shape, dim_slices, device)
def get_union_slice_mask(shape, dim_slices, device)
class DummyMaskGenerator(ModuleAttrMixin)
    def __init__(self)
    def forward(self, shape)
class LowdimMaskGenerator(ModuleAttrMixin)
    def __init__(self, action_dim, obs_dim, max_n_obs_steps, fix_obs_steps, action_visible)
    def forward(self, shape, seed)
class KeypointMaskGenerator(ModuleAttrMixin)
    def __init__(self, action_dim, keypoint_dim, max_n_obs_steps, fix_obs_steps, keypoint_visible_rate, time_independent, action_visible, context_dim, n_context_steps)
    def forward(self, shape, seed)
def test()
```

### diffusion_policy/model/diffusion/positional_embedding.py

```
class SinusoidalPosEmb(Module)
    def __init__(self, dim)
    def forward(self, x)
```

### diffusion_policy/model/diffusion/transformer_for_diffusion.py

```
class TransformerForDiffusion(ModuleAttrMixin)
    def __init__(self, input_dim, output_dim, horizon, n_obs_steps, cond_dim, n_layer, n_head, n_emb, p_drop_emb, p_drop_attn, causal_attn, time_as_cond, obs_as_cond, n_cond_layers)
    def _init_weights(self, module)
    def get_optim_groups(self, weight_decay)
    def configure_optimizers(self, learning_rate, weight_decay, betas)
    def forward(self, sample, timestep, cond)
def test()
```

### diffusion_policy/model/vision/crop_randomizer.py

```
class CropRandomizer(Module)
    """Randomly sample crops at input, and then average across crop features at output."""
    def __init__(self, input_shape, crop_height, crop_width, num_crops, pos_enc)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def forward_in(self, inputs)
    def forward_out(self, inputs)
    def forward(self, inputs)
    def __repr__(self)
def crop_image_from_indices(images, crop_indices, crop_height, crop_width)
def sample_random_image_crops(images, crop_height, crop_width, num_crops, pos_enc)
```

### diffusion_policy/model/vision/model_getter.py

```
def get_resnet(name, weights)
def get_r3m(name)
```

### diffusion_policy/model/vision/multi_image_obs_encoder.py

```
class MultiImageObsEncoder(ModuleAttrMixin)
    def __init__(self, shape_meta, rgb_model, resize_shape, crop_shape, random_crop, use_group_norm, share_rgb_model, imagenet_norm)
    def forward(self, obs_dict)
    def output_shape(self)
```

### diffusion_policy/policy/base_image_policy.py

```
class BaseImagePolicy(ModuleAttrMixin)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
```

### diffusion_policy/policy/base_lowdim_policy.py

```
class BaseLowdimPolicy(ModuleAttrMixin)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
```

### diffusion_policy/policy/bet_lowdim_policy.py

```
class BETLowdimPolicy(BaseLowdimPolicy)
    def __init__(self, action_ae, obs_encoding_net, state_prior, horizon, n_action_steps, n_obs_steps)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def fit_action_ae(self, input_actions)
    def get_latents(self, latent_collection_loader)
    def get_optimizer(self, weight_decay, learning_rate, betas)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_transformer_hybrid_image_policy.py

```
class DiffusionTransformerHybridImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, horizon, n_action_steps, n_obs_steps, num_inference_steps, crop_shape, obs_encoder_group_norm, eval_fixed_crop, n_layer, n_cond_layers, n_head, n_emb, p_drop_emb, p_drop_attn, causal_attn, time_as_cond, obs_as_cond, pred_action_steps_only)
    def conditional_sample(self, condition_data, condition_mask, cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def get_optimizer(self, transformer_weight_decay, obs_encoder_weight_decay, learning_rate, betas)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_transformer_lowdim_policy.py

```
class DiffusionTransformerLowdimPolicy(BaseLowdimPolicy)
    def __init__(self, model, noise_scheduler, horizon, obs_dim, action_dim, n_action_steps, n_obs_steps, num_inference_steps, obs_as_cond, pred_action_steps_only)
    def conditional_sample(self, condition_data, condition_mask, cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def get_optimizer(self, weight_decay, learning_rate, betas)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_unet_hybrid_image_policy.py

```
class DiffusionUnetHybridImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, horizon, n_action_steps, n_obs_steps, num_inference_steps, obs_as_global_cond, crop_shape, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale, obs_encoder_group_norm, eval_fixed_crop)
    def conditional_sample(self, condition_data, condition_mask, local_cond, global_cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_unet_image_policy.py

```
class DiffusionUnetImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, obs_encoder, horizon, n_action_steps, n_obs_steps, num_inference_steps, obs_as_global_cond, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale)
    def conditional_sample(self, condition_data, condition_mask, local_cond, global_cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_unet_lowdim_policy.py

```
class DiffusionUnetLowdimPolicy(BaseLowdimPolicy)
    def __init__(self, model, noise_scheduler, horizon, obs_dim, action_dim, n_action_steps, n_obs_steps, num_inference_steps, obs_as_local_cond, obs_as_global_cond, pred_action_steps_only, oa_step_convention)
    def conditional_sample(self, condition_data, condition_mask, local_cond, global_cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/diffusion_unet_video_policy.py

```
class DiffusionUnetVideoPolicy(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, rgb_net, horizon, n_action_steps, n_obs_steps, num_inference_steps, lowdim_as_global_cond, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale, channel_mults, n_blocks_per_level, ta_kernel_size, ta_n_groups)
    def conditional_sample(self, condition_data, condition_mask, local_cond, global_cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
```

### diffusion_policy/policy/ibc_dfo_hybrid_image_policy.py

```
class IbcDfoHybridImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, horizon, n_action_steps, n_obs_steps, dropout, train_n_neg, pred_n_iter, pred_n_samples, kevin_inference, andy_train, obs_encoder_group_norm, eval_fixed_crop, crop_shape)
    def forward(self, obs, action)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
    def get_naction_stats(self)
```

### diffusion_policy/policy/ibc_dfo_lowdim_policy.py

```
class IbcDfoLowdimPolicy(BaseLowdimPolicy)
    def __init__(self, horizon, obs_dim, action_dim, n_action_steps, n_obs_steps, dropout, train_n_neg, pred_n_iter, pred_n_samples, kevin_inference, andy_train)
    def forward(self, obs, action)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
    def get_naction_stats(self)
```

### diffusion_policy/policy/robomimic_image_policy.py

```
class RobomimicImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, algo_name, obs_type, task_name, dataset_type, crop_shape)
    def to(self)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
    def train_on_batch(self, batch, epoch, validate)
    def on_epoch_end(self, epoch)
    def get_optimizer(self)
def test()
```

### diffusion_policy/policy/robomimic_lowdim_policy.py

```
class RobomimicLowdimPolicy(BaseLowdimPolicy)
    def __init__(self, action_dim, obs_dim, algo_name, obs_type, task_name, dataset_type)
    def to(self)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
    def train_on_batch(self, batch, epoch, validate)
    def get_optimizer(self)
```

### diffusion_policy/real_world/keystroke_counter.py

```
class KeystrokeCounter(Listener)
    def __init__(self)
    def on_press(self, key)
    def on_release(self, key)
    def clear(self)
    def __getitem__(self, key)
    def get_press_events(self)
```

### diffusion_policy/real_world/multi_camera_visualizer.py

```
class MultiCameraVisualizer(Process)
    def __init__(self, realsense, row, col, window_name, vis_fps, fill_value, rgb_to_bgr)
    def start(self, wait)
    def stop(self, wait)
    def start_wait(self)
    def stop_wait(self)
    def run(self)
```

### diffusion_policy/real_world/multi_realsense.py

```
class MultiRealsense()
    def __init__(self, serial_numbers, shm_manager, resolution, capture_fps, put_fps, put_downsample, record_fps, enable_color, enable_depth, enable_infrared, get_max_k, advanced_mode_config, transform, vis_transform, recording_transform, video_recorder, verbose)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def n_cameras(self)
    def is_ready(self)
    def start(self, wait, put_start_time)
    def stop(self, wait)
    def start_wait(self)
    def stop_wait(self)
    def get(self, k, out)
    def get_vis(self, out)
    def set_color_option(self, option, value)
    def set_exposure(self, exposure, gain)
    def set_white_balance(self, white_balance)
    def get_intrinsics(self)
    def get_depth_scale(self)
    def start_recording(self, video_path, start_time)
    def stop_recording(self)
    def restart_put(self, start_time)
def repeat_to_list(x, n, cls)
```

### diffusion_policy/real_world/real_data_conversion.py

```
def real_data_to_replay_buffer(dataset_path, out_store, out_resolutions, lowdim_keys, image_keys, lowdim_compressor, image_compressor, n_decoding_threads, n_encoding_threads, max_inflight_tasks, verify_read)
```

### diffusion_policy/real_world/real_env.py

```
class RealEnv()
    def __init__(self, output_dir, robot_ip, frequency, n_obs_steps, obs_image_resolution, max_obs_buffer_size, camera_serial_numbers, obs_key_map, obs_float32, max_pos_speed, max_rot_speed, tcp_offset, init_joints, video_capture_fps, video_capture_resolution, record_raw_video, thread_per_video, video_crf, enable_multi_cam_vis, multi_cam_vis_resolution, shm_manager)
    def is_ready(self)
    def start(self, wait)
    def stop(self, wait)
    def start_wait(self)
    def stop_wait(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def get_obs(self)
    def exec_actions(self, actions, timestamps, stages)
    def get_robot_state(self)
    def start_episode(self, start_time)
    def end_episode(self)
    def drop_episode(self)
```

### diffusion_policy/real_world/real_inference_util.py

```
def get_real_obs_dict(env_obs, shape_meta)
def get_real_obs_resolution(shape_meta)
```

### diffusion_policy/real_world/rtde_interpolation_controller.py

```
class Command(Enum)
class RTDEInterpolationController(Process)
    """To ensure sending command to the robot with predictable latency
this controller need its separate process (due to python GIL)"""
    def __init__(self, shm_manager, robot_ip, frequency, lookahead_time, gain, max_pos_speed, max_rot_speed, launch_timeout, tcp_offset_pose, payload_mass, payload_cog, joints_init, joints_init_speed, soft_real_time, verbose, receive_keys, get_max_k)
    def start(self, wait)
    def stop(self, wait)
    def start_wait(self)
    def stop_wait(self)
    def is_ready(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def servoL(self, pose, duration)
    def schedule_waypoint(self, pose, target_time)
    def get_state(self, k, out)
    def get_all_state(self)
    def run(self)
```

### diffusion_policy/real_world/single_realsense.py

```
class Command(Enum)
class SingleRealsense(Process)
    def __init__(self, shm_manager, serial_number, resolution, capture_fps, put_fps, put_downsample, record_fps, enable_color, enable_depth, enable_infrared, get_max_k, advanced_mode_config, transform, vis_transform, recording_transform, video_recorder, verbose)
    def get_connected_devices_serial()
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def start(self, wait, put_start_time)
    def stop(self, wait)
    def start_wait(self)
    def end_wait(self)
    def is_ready(self)
    def get(self, k, out)
    def get_vis(self, out)
    def set_color_option(self, option, value)
    def set_exposure(self, exposure, gain)
    def set_white_balance(self, white_balance)
    def get_intrinsics(self)
    def get_depth_scale(self)
    def start_recording(self, video_path, start_time)
    def stop_recording(self)
    def restart_put(self, start_time)
    def run(self)
```

### diffusion_policy/real_world/spacemouse.py

```
class Spacemouse(Thread)
    def __init__(self, max_value, deadzone, dtype)
    def get_motion_state(self)
    def get_motion_state_transformed(self)
    def is_button_pressed(self, button_id)
    def stop(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def run(self)
def test()
```

### diffusion_policy/real_world/spacemouse_shared_memory.py

```
class Spacemouse(Process)
    def __init__(self, shm_manager, get_max_k, frequency, max_value, deadzone, dtype, n_buttons)
    def get_motion_state(self)
    def get_motion_state_transformed(self)
    def get_button_state(self)
    def is_button_pressed(self, button_id)
    def start(self, wait)
    def stop(self, wait)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def run(self)
```

### diffusion_policy/real_world/video_recorder.py

```
def read_video(video_path, dt, video_start_time, start_time, img_transform, thread_type, thread_count, max_pad_frames)
class VideoRecorder()
    def __init__(self, fps, codec, input_pix_fmt)
    def _reset_state(self)
    def create_h264(cls, fps, codec, input_pix_fmt, output_pix_fmt, crf, profile)
    def __del__(self)
    def is_ready(self)
    def start(self, file_path, start_time)
    def write_frame(self, img, frame_time)
    def stop(self)
```

### diffusion_policy/scripts/bet_blockpush_conversion.py

```
def main(input, output, abs_action)
```

### diffusion_policy/scripts/blockpush_abs_conversion.py

```
def main(input, output, target_eef_idx)
```

### diffusion_policy/scripts/episode_lengths.py

```
def main(input, dt)
```

### diffusion_policy/scripts/generate_bet_blockpush.py

```
def main(output, n_episodes, chunk_length)
```

### diffusion_policy/scripts/real_dataset_conversion.py

```
def main(input, output, resolution, n_decoding_threads, n_encoding_threads)
```

### diffusion_policy/scripts/real_pusht_metrics.py

```
def get_t_mask(img, hsv_ranges)
def get_mask_metrics(target_mask, mask)
def get_video_metrics(video_path, target_mask, use_tqdm)
def worker(x)
def main(reference, input, camera_idx, n_workers)
```

### diffusion_policy/scripts/real_pusht_successrate.py

```
def main(reference, input)
```

### diffusion_policy/scripts/robomimic_dataset_action_comparison.py

```
def read_all_actions(hdf5_file, metric_skip_steps)
def main(input, output)
```

### diffusion_policy/scripts/robomimic_dataset_conversion.py

```
def worker(x)
def main(input, output, eval_dir, num_workers)
```

### diffusion_policy/shared_memory/shared_memory_queue.py

```
class SharedMemoryQueue()
    """A Lock-Free FIFO Shared Memory Data Structure.
Stores a sequence of dict of numpy arrays."""
    def __init__(self, shm_manager, array_specs, buffer_size)
    def create_from_examples(cls, shm_manager, examples, buffer_size)
    def qsize(self)
    def empty(self)
    def clear(self)
    def put(self, data)
    def get(self, out)
    def get_k(self, k, out)
    def get_all(self, out)
    def _get_k_impl(self, k, read_count, out)
    def _allocate_empty(self, k)
```

### diffusion_policy/shared_memory/shared_memory_ring_buffer.py

```
class SharedMemoryRingBuffer()
    """A Lock-Free FILO Shared Memory Data Structure.
Stores a sequence of dict of numpy arrays."""
    def __init__(self, shm_manager, array_specs, get_max_k, get_time_budget, put_desired_frequency, safety_margin)
    def count(self)
    def create_from_examples(cls, shm_manager, examples, get_max_k, get_time_budget, put_desired_frequency)
    def clear(self)
    def put(self, data, wait)
    def _allocate_empty(self, k)
    def get(self, out)
    def get_last_k(self, k, out)
    def get_all(self)
```

### diffusion_policy/shared_memory/shared_memory_util.py

```
class ArraySpec()
class SharedAtomicCounter()
    def __init__(self, shm_manager, size)
    def buf(self)
    def load(self)
    def store(self, value)
    def add(self, value)
```

### diffusion_policy/shared_memory/shared_ndarray.py

```
class SharedNDArray(?)
    """Class to keep track of and retrieve the data in a shared array
Attributes
----------
shm
    SharedMemory object containing the data of the array
shape
    Shape of the NumPy array
dtype
    Type of the NumPy array. Anything that may be passed to the `dtype=` argument in `np.ndarray`.
lock
    (Opti"""
    def __init__(self, shm, shape, dtype)
    def __repr__(self)
    def create_from_array(cls, mem_mgr, arr)
    def create_from_shape(cls, mem_mgr, shape, dtype)
    def shape(self)
    def get(self)
    def __del__(self)
```

### diffusion_policy/workspace/base_workspace.py

```
class BaseWorkspace()
    def __init__(self, cfg, output_dir)
    def output_dir(self)
    def run(self)
    def save_checkpoint(self, path, tag, exclude_keys, include_keys, use_thread)
    def get_checkpoint_path(self, tag)
    def load_payload(self, payload, exclude_keys, include_keys)
    def load_checkpoint(self, path, tag, exclude_keys, include_keys)
    def create_from_checkpoint(cls, path, exclude_keys, include_keys)
    def save_snapshot(self, tag)
    def create_from_snapshot(cls, path)
def _copy_to_cpu(x)
```

### diffusion_policy/workspace/train_bet_lowdim_workspace.py

```
class TrainBETLowdimWorkspace(BaseWorkspace)
    def __init__(self, cfg)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_transformer_hybrid_workspace.py

```
class TrainDiffusionTransformerHybridWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_transformer_lowdim_workspace.py

```
class TrainDiffusionTransformerLowdimWorkspace(BaseWorkspace)
    def __init__(self, cfg)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_unet_hybrid_workspace.py

```
class TrainDiffusionUnetHybridWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_unet_image_workspace.py

```
class TrainDiffusionUnetImageWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_unet_lowdim_workspace.py

```
class TrainDiffusionUnetLowdimWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_diffusion_unet_video_workspace.py

```
class TrainDiffusionUnetVideoWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_ibc_dfo_hybrid_workspace.py

```
class TrainIbcDfoHybridWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_ibc_dfo_lowdim_workspace.py

```
class TrainIbcDfoLowdimWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_robomimic_image_workspace.py

```
class TrainRobomimicImageWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def run(self)
def main(cfg)
```

### diffusion_policy/workspace/train_robomimic_lowdim_workspace.py

```
class TrainRobomimicLowdimWorkspace(BaseWorkspace)
    def __init__(self, cfg)
    def run(self)
def main(cfg)
```

### ray_train_multirun.py

```
"""Start local ray cluster
(robodiff)$ export CUDA_VISIBLE_DEVICES=0,1,2 # select GPUs to be managed by the ray cluster
(robodiff)$ ray start --head --num-gpus=3

Training:
python ray_train_multirun.py --config-name=train_diffusion_unet_lowdim_workspace --seeds=42,43,44 --monitor_key=test/mean_score -- logger.mode=online training.eval_first=True"""
def main(config_name, config_dir, seeds, monitor_key, ray_address, num_cpus, num_gpus, max_retries, monitor_max_retires, data_src, unbuffer_python, single_node, command_args)
```

### train.py

```
"""Usage:
Training:
python train.py --config-name=train_diffusion_lowdim_workspace"""
def main(cfg)
```