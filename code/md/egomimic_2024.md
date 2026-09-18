# egomimic_2024

source: https://github.com/SimarKareer/EgoMimic


commit: 6d63e9a3cd1dcc1d24860a11d7d9c5b2d5cba645


## README

# EgoMimic: Scaling Imitation Learning through Egocentric Video
![Teaser](./assets/teaser.jpg)

This repository contains the data processing and training code for EgoMimic - Both for Human Aria and Robot teleoperated Data. To rollout policies in the real world, you'll additionally need our hardware repo [Eve](https://github.com/SimarKareer/Eve).

**Useful Links**
- [Project Website](https://egomimic.github.io/)
- [Sample Dataset Huggingface](https://huggingface.co/datasets/gatech/EgoMimic/tree/main)

---

## Structure
- [``egomimic/scripts/aloha_process``](./egomimic/scripts/aloha_process/): Process raw aloha style data into a robomimic style hdf5, compatible for training here.
- [``egomimic/scripts/aria_process``](./egomimic/scripts/aria_process/): Process human embodiment data from Aria Glasses into a robomimic style hdf5.
- [``egomimic/algo``](./egomimic/algo): Algorithm code for Egomimic, as well as ACT and mimicplay baselines
- [``egomimic/configs``](./egomimic/configs): Train configs for each algorithm
- [``egomimic/scripts/pl_train.py``](./egomimic/scripts/pl_train.py): Main training script, powered by Pytorch Lightning (DDP enabled)
- [``data_processing.md``](./data_processing.md): Instructions to process your own data, both Aria Human data and teleoperated robot data.

## Installation

```
git clone --recursive git@github.com:SimarKareer/EgoMimic.git
cd EgoMimic
conda env create -f environment.yaml
pip install projectaria-tools'[all]'
pip install -e external/robomimic
pip install -e .
python external/robomimic/robomimic/scripts/setup_macros.py
```

Set `git config --global submodule.recurse true` if you want `git pull` to automatically update the submodule as well.

Then go to  `external/robomimic/robomimic/macros_private.py` and manually add your wandb username. Make sure you have ran `wandb login` too.


**Download Sample Data**
```
mkdir datasets
cd datasets

## Groceries
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/groceries_human.hdf5
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/groceries_robot.hdf5

## Laundry
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/smallclothfold_human.hdf5
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/smallclothfold_robot.hdf5


## Bowlplace
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/bowlplace_human.hdf5
wget https://huggingface.co/datasets/gatech/EgoMimic/resolve/main/bowlplace_robot.hdf5
```



-------


## EgoMimic Quick Start (Train on Sample Data)

EgoMimic Training (Toy in Bowl Task)
```
python scripts/pl_train.py --config configs/egomimic_oboo.json --dataset /path/to/bowlplace_robot.hdf5 --dataset_2 /path/to/bowlplace_human.hdf5 --debug
```

ACT Baseline Training
```
python scripts/pl_train.py --config configs/act.json --dataset /path/to/bowlplace_robot.hdf5 --debug
```

For a detailed list of commands to run each experiment see [experiment_launch.md](./experiment_launch.md)

Use `--debug` to check that the pipeline works

Launching runs via submitit / slurm
```
python scripts/pl_submit.py --config <config> --name <name> --description <description> --gpus-per-node <gpus-per-node>`
```

Training creates a folder for each experiment
```
./trained_models_highlevel/description/name
├── videos (generated offline validation videos)
├── logs (wandb logs)
├── slurm (slurm logs if launched via slurm)
├── config.json (copy of config used to launch this run)
├── models (model ckpts)
├── ds1_norm_stats.pkl (robot dataset normalization stats)
└── ds2_norm_stats.pkl (hand data norm stats if training egomimic)
```

Offline Eval:
`python scripts/pl_train.py --dataset <dataset> --ckpt_path <ckpt> --eval`

### Processing your own data for training
![Data Streams](./assets/train_data.png)
See [``data_processing.md``](./data_processing.md)

### Rollout policies in the real world
Follow these instructions on the desktop connected to the real hardware.
1. Follow instructions in [Eve](https://github.com/SimarKareer/Eve)
2. Install the hardware package into the `emimic` conda env via
```
conda activate emimic
cd ~/interbotix_ws/src/eve
pip install -e .
```
3. Rollout policy
```
cd EgoMimic/egomimic
python scripts/evaluation/eval_real --eval-path <path to>EgoPlay/trained_models_highlevel/<your model folder>/models/<your ckpt>.ckpt
```


## File tree (depth 3, assets pruned)

```
.gitignore
.gitmodules
LICENSE
README.md
data_processing.md
egomimic/
  __init__.py
  algo/
    GPT.py
    __init__.py
    act.py
    algo.py
    egomimic.py
    mimicplay.py
  configs/
    GMMResnet.json
    GMMViT.json
    __init__.py
    act.json
    actHand.json
    act_config.py
    base_config.py
    config.py
    egomimic_clothes.json
    egomimic_groceries.json
    egomimic_oboo.json
    mimicplay_config.py
  models/
    __init__.py
    act_nets.py
    obs_nets.py
    policy_nets.py
  pl_utils/
    pl_data_utils.py
    pl_model.py
    pl_train_utils.py
  resources/
    model.urdf
  scripts/
    __init__.py
    algo_test.py
    aloha_process/
    aria_process/
    calibrate_camera/
    evaluation/
    masking/
    pl_submit.py
    pl_train.py
  utils/
    dataset.py
    egomimicUtils.py
    file_utils.py
    obs_utils.py
    train_utils.py
    val_utils.py
environment.yaml
experiment_launch.md
external/
  robomimic/
patch_notes.md
sam_env.yaml
setup.py
```

## Config files (2)


### environment.yaml

```yaml
name: emimic
channels:
  - pytorch
  - nvidia
dependencies:
  - python=3.10
  - pip=23
  - pytorch=2.3.1
  - torchvision=0.18.1
  - pytorch-cuda=12.1
  - cuda-toolkit=12.1
  - pyyaml
  - pexpect
  - matplotlib
  - packaging
  - h5py
  - ipython
  - pip:
    - wandb
    - hydra-core
    - hydra-submitit-launcher
    - black
    - gpustat
    - pynvml
    - termcolor
    - pyquaternion
    - rospkg
    - einops
    - av
    - opencv-python==4.7.0.72
    - dm-control==1.0.8
    - mujoco==2.3.1
    - mujoco-py==2.1.2.14
    - git+https://github.com/simarkareer/submitit
    - arm_pytorch_utilities
    - pytorch-kinematics
    - pytorch-lightning
    - positional-encodings[pytorch]
```

### sam_env.yaml

```yaml
name: eplay
channels:
  - pytorch
  - nvidia
dependencies:
  - python=3.11
  - scipy
  - ninja
  - pip:
    - diffusers[torch]
    - transformers
  
```

## Python signatures and reward/observation bodies (10 files)


### egomimic/configs/act_config.py

```
"""Config for BC algorithm."""
class ACTConfig(BaseConfig)
    def train_config(self)
    def algo_config(self)
class EgoMimicConfig(ACTConfig)
    def train_config(self)
    def observation_config(self)
    def algo_config(self)

```python
def observation_config(self):
        super(EgoMimicConfig, self).observation_config()
        self.observation_hand.modalities.obs.low_dim = ["joint_positions"]
        self.observation_hand.modalities.obs.rgb = ["front_img_1"]
```
```

### egomimic/configs/base_config.py

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
        self.observation.modalities.obs.low_dim = (
            [  # specify low-dim observations for agent
                "robot0_eef_pos",
                "robot0_eef_quat",
                "robot0_gripper_qpos",
                "object",
            ]
        )
        self.observation.modalities.obs.rgb = (
            []
        )  # specify rgb image observations for agent
        self.observation.modalities.obs.depth = []
        self.observation.modalities.obs.scan = []
        self.observation.modalities.goal.low_dim = (
            []
        )  # specify low-dim goal observations to condition agent on
        self.observation.modalities.goal.rgb = (
            []
        )  # specify rgb image goal observations to condition agent on
        self.observation.modalities.goal.depth = []
        self.observation.modalities.goal.scan = []
        self.observation.modalities.obs.do_not_lock_keys()
        self.observation.modalities.goal.do_not_lock_keys()

        # observation encoder architectures (per obs modality)
        # This applies to all networks that take observation dicts as input

        # =============== Low Dim default encoder (no encoder) ===============
        self.observation.encoder.low_dim.core_class = None
        self.observation.encoder.low_dim.core_kwargs = Config()  # No kwargs by default
        self.observation.encoder.low_dim.core_kwargs.do_not_lock_keys()

        # Low Dim: Obs Randomizer settings
        self.observation.encoder.low_dim.obs_randomizer_class = None
        self.observation.encoder.low_dim.obs_randomizer_kwargs = (
            Config()
        )  # No kwargs by default
        self.observation.encoder.low_dim.obs_randomizer_kwargs.do_not_lock_keys()

        # =============== RGB default encoder (ResNet backbone + linear layer output) ===============
        self.observation.encoder.rgb.core_class = "VisualCore"  # Default VisualCore class combines backbone (like ResNet-18) with pooling operation (like spatial softmax)
        self.observation.encoder.rgb.core_kwargs = (
            Config()
        )  # See models/obs_core.py for important kwargs to set and defaults used
        self.observation.encoder.rgb.core_kwargs.do_not_lock_keys()

        # RGB: Obs Randomizer settings
        self.observation.encoder.rgb.obs_randomizer_class = (
            None  # Can set to 'CropRandomizer' to use crop randomization
        )
        self.observation.encoder.rgb.obs_randomizer_kwargs = (
            Config()
        )  # See models/obs_core.py for important kwargs to set and defaults used
        self.observation.encoder.rgb.obs_randomizer_kwargs.do_not_lock_keys()

        # Allow for other custom modalities to be specified
        self.observation.encoder.do_not_lock_keys()

        # =============== Depth default encoder (same as rgb) ===============
        self.observation.encoder.depth = deepcopy(self.observation.encoder.rgb)

        # =============== Scan default encoder (Conv1d backbone + linear layer output) ===============
        self.observation.encoder.scan = deepcopy(self.observation.encoder.rgb)

        # Scan: Modify the core class + kwargs, otherwise, is same as rgb encoder
        self.observation.encoder.scan.core_class 
```
```

### egomimic/configs/config.py

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

### egomimic/configs/mimicplay_config.py

```
"""Config for MimicPlay algorithm."""
class MimicPlayConfig(BaseConfig)
    def train_config(self)
    def algo_config(self)
```

### egomimic/models/policy_nets.py

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
class GMMActorNetwork(ActorNetwork)
    """Variant of actor network that learns a multimodal Gaussian mixture distribution
over actions."""
    def __init__(self, obs_shapes, ac_dim, mlp_layer_dims, num_modes, min_std, std_activation, low_noise_eval, use_tanh, goal_shapes, encoder_kwargs)
    def _get_output_shapes(self)
    def forward_train(self, obs_dict, goal_dict, return_latent)
    def forward(self, obs_dict, goal_dict)
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
```

### egomimic/pl_utils/pl_train_utils.py

```
class PreemptionHandler(Callback)
    def __init__(self)
    def setup(self, trainer, pl_module, stage)
    def handle_preemption(self, signum, frame)
def init_dataset(config, dataset_path, type, alternate_valid_path)
def eval(config, ckpt_path, type)
def train(config, ckpt_path)
```

### egomimic/scripts/masking/hand_overlay.py

```
def show_mask(mask, ax, random_color, borders)
def show_points(coords, labels, ax, marker_size)
def show_box(box, ax)
def show_masks(image, masks, scores, point_coords, box_coords, input_labels, borders)
def get_bounds(binary_image)
def line_on_hand(images, masks, arm)
def sam_processing(dataset, debug)
def main(args)
```

### egomimic/scripts/pl_train.py

```
"""The main entry point for training policies. Adapted to use PyTorch Lightning and Optimus codebase.

Args:
    config (str): path to a config json that will be used to override the default settings.
        If omitted, default settings are used. This is the preferred way to run experiments.

    algo (str): name of the algorithm to run. Only needs to be provided if @config is not
        provided.

    name (str): if provided, override the experiment name defined in the config

    dataset (str): if provided, override the dataset path defined in the config

    debug (bool): set this flag to ru"""
def main(args)
def train_argparse()
```

### egomimic/utils/train_utils.py

```
"""This file contains several utility functions used to define the main training loop. It 
mainly consists of functions to assist with logging, rollouts, and the @run_epoch function,
which is the core training logic for models in this repository."""
def get_exp_dir(config, auto_remove_exp_dir, rank)
def load_data_for_training(config, obs_keys, type, dataset_path)
def dataset_factory(config, obs_keys, type, filter_by_attribute, dataset_path)
def run_rollout(policy, env, horizon, use_goals, render, video_writer, video_skip, terminate_on_success)
def rollout_with_stats(policy, envs, horizon, use_goals, num_episodes, render, video_dir, video_path, epoch, video_skip, terminate_on_success, verbose)
```