# simpler_2024

source: https://github.com/simpler-env/SimplerEnv


commit: 06accaca93535902d408da4855f21cece12bceb7


## README

# SimplerEnv: Simulated Manipulation Policy Evaluation Environments for Real Robot Setups

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simpler-env/SimplerEnv/blob/main/example.ipynb)

![](./images/teaser.png)

Significant progress has been made in building generalist robot manipulation policies, yet their scalable and reproducible evaluation remains challenging, as real-world evaluation is operationally expensive and inefficient. We propose employing physical simulators as efficient, scalable, and informative complements to real-world evaluations. These simulation evaluations offer valuable quantitative metrics for checkpoint selection, insights into potential real-world policy behaviors or failure modes, and standardized setups to enhance reproducibility.

This repository's code is based in the [SAPIEN](https://sapien.ucsd.edu/) simulator and the CPU based [ManiSkill2](https://maniskill2.github.io/) benchmark. We have also integrated the Bridge dataset environments into ManiSkill3, which offers GPU parallelization and can run 10-15x faster than the ManiSkill2 version. For instructions on how to use the GPU parallelized environments and evaluate policies on them, see: https://github.com/simpler-env/SimplerEnv/tree/maniskill3

This repository encompasses 2 real-to-sim evaluation setups:
- `Visual Matching` evaluation: Matching real & sim visual appearances for policy evaluation by overlaying real-world images onto simulation backgrounds and adjusting foreground object and robot textures in simulation.
- `Variant Aggregation` evaluation: creating different sim environment variants (e.g., different backgrounds, lightings, distractors, table textures, etc) and averaging their results.

We hope that our work guides and inspires future real-to-sim evaluation efforts.

- [SimplerEnv: Simulated Manipulation Policy Evaluation Environments for Real Robot Setups](#simplerenv-simulated-manipulation-policy-evaluation-environments-for-real-robot-setups)
  - [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Examples](#examples)
  - [Current Environments](#current-environments)
  - [Compare Your Policy Evaluation Approach to SIMPLER](#compare-your-policy-evaluation-approach-to-simpler)
  - [Code Structure](#code-structure)
  - [Adding New Policies](#adding-new-policies)
  - [Adding New Real-to-Sim Evaluation Environments and Robots](#adding-new-real-to-sim-evaluation-environments-and-robots)
  - [Full Installation (RT-1 and Octo Inference, Env Building)](#full-installation-rt-1-and-octo-inference-env-building)
    - [RT-1 Inference Setup](#rt-1-inference-setup)
    - [Octo Inference Setup](#octo-inference-setup)
  - [Troubleshooting](#troubleshooting)
  - [Citation](#citation)


## Getting Started

Follow the [Installation](#installation) section to install the minimal requirements for our environments. Then you can run the following minimal inference script with interactive python. The scripts creates prepackaged environments for our `visual matching` evaluation setup.

```python
import simpler_env
from simpler_env.utils.env.observation_utils import get_image_from_maniskill2_obs_dict

env = simpler_env.make('google_robot_pick_coke_can')
obs, reset_info = env.reset()
instruction = env.get_language_instruction()
print("Reset info", reset_info)
print("Instruction", instruction)

done, truncated = False, False
while not (done or truncated):
   # action[:3]: delta xyz; action[3:6]: delta rotation in axis-angle representation;
   # action[6:7]: gripper (the meaning of open / close depends on robot URDF)
   image = get_image_from_maniskill2_obs_dict(env, obs)
   action = env.action_space.sample() # replace this with your policy inference
   obs, reward, done, truncated, info = env.step(action) # for long horizon tasks, you can call env.advance_to_next_subtask() to advance to the next subtask; the environment might also autoadvance if env._elapsed_steps is larger than a threshold
   new_instruction = env.get_language_instruction()
   if new_instruction != instruction:
      # for long horizon tasks, we get a new instruction when robot proceeds to the next subtask
      instruction = new_instruction
      print("New Instruction", instruction)

episode_stats = info.get('episode_stats', {})
print("Episode stats", episode_stats)
```

Additionally, you can play with our environments in an interactive manner through [`ManiSkill2_real2sim/mani_skill2_real2sim/examples/demo_manual_control_custom_envs.py`](https://github.com/simpler-env/ManiSkill2_real2sim/blob/main/mani_skill2_real2sim/examples/demo_manual_control_custom_envs.py). See the script for more details and commands.

## Installation

Prerequisites:
- CUDA version >=11.8 and < 13 (this is required if you want to perform a full installation of this repo and perform RT-1 or Octo inference)
- An NVIDIA GPU (ideally RTX; for non-RTX GPUs, such as 1080Ti and A100, environments that involve ray tracing will be slow). Currently TPU is not supported as SAPIEN requires a GPU to run.

Create an anaconda environment:
```
conda create -n simpler_env python=3.10 (3.10 or 3.11)
conda activate simpler_env
```

Clone this repo:
```
git clone https://github.com/simpler-env/SimplerEnv --recurse-submodules
```

Install numpy<2.0 (otherwise errors in IK might occur in pinocchio):
```
pip install numpy==1.24.4
```

Install ManiSkill2 real-to-sim environments and their dependencies:
```
cd {this_repo}/ManiSkill2_real2sim
pip install -e .
```

Install this package:
```
cd {this_repo}
pip install -e .
```

**If you'd like to perform evaluations on our provided agents (e.g., RT-1, Octo), or add new robots and environments, please additionally follow the full installation instructions [here](#full-installation-rt-1-and-octo-inference-env-building).**


## Examples

- Simple RT-1 and Octo evaluation script on prepackaged environments with visual matching evaluation setup: see [`simpler_env/simple_inference_visual_matching_prepackaged_envs.py`](https://github.com/simpler-env/SimplerEnv/blob/main/simpler_env/simple_inference_visual_matching_prepackaged_envs.py).
- Colab notebook for RT-1 and Octo inference: see [this link](https://colab.research.google.com/github/simpler-env/SimplerEnv/blob/main/example.ipynb).
- Environment interactive visualization and manual control: see [`ManiSkill2_real2sim/mani_skill2_real2sim/examples/demo_manual_control_custom_envs.py`](https://github.com/simpler-env/ManiSkill2_real2sim/blob/main/mani_skill2_real2sim/examples/demo_manual_control_custom_envs.py)
- Policy inference scripts to reproduce our Google Robot and WidowX real-to-sim evaluation results with sweeps over object / robot poses and advanced loggings. These contain both visual matching and variant aggregation evaluation setups along with RT-1, RT-1-X, and Octo policies. See [`scripts/`](https://github.com/simpler-env/SimplerEnv/tree/main/scripts).
- Real-to-sim evaluation videos from running `scripts/*.sh`: see [this link](https://huggingface.co/datasets/xuanlinli17/simpler-env-eval-example-videos/tree/main).

## Current Environments

To get a list of all available environments, run:
```
import simpler_env
print(simpler_env.ENVIRONMENTS)
```

| Task Name | ManiSkill2 Env Name | Image (Visual Matching) |
| ----------- | ----- | ----- |
| google_robot_pick_coke_can | GraspSingleOpenedCokeCanInScene-v0 | <img src="./images/example_visualization/google_robot_coke_can_visual_matching.png" width="128" height="128" > |
| google_robot_pick_object | GraspSingleRandomObjectInScene-v0 | <img src="./images/example_visualization/google_robot_pick_random_object.png" width="128" height="128" > |
| google_robot_move_near | MoveNearGoogleBakedTexInScene-v1 | <img src="./images/example_visualization/google_robot_move_near_visual_matching.png" width="128" height="128" > |
| google_robot_open_drawer | OpenDrawerCustomInScene-v0 | <img src="./images/example_visualization/google_robot_open_drawer_visual_matching.png" width="128" height="128" > |
| google_robot_close_drawer | CloseDrawerCustomInScene-v0 | <img src="./images/example_visualization/google_robot_close_drawer_visual_matching.png" width="128" height="128" > |
| google_robot_place_in_closed_drawer | PlaceIntoClosedDrawerCustomInScene-v0 | <img src="./images/example_visualization/google_robot_put_apple_in_closed_top_drawer.png" width="128" height="128" > |
| widowx_spoon_on_towel    | PutSpoonOnTableClothInScene-v0                | <img src="./images/example_visualization/widowx_spoon_on_towel_visual_matching.png" width="128" height="128" > |
| widowx_carrot_on_plate   | PutCarrotOnPlateInScene-v0                    | <img src="./images/example_visualization/widowx_carrot_on_plate_visual_matching.png" width="128" height="128" > |
| widowx_stack_cube        | StackGreenCubeOnYellowCubeBakedTexInScene-v0  | <img src="./images/example_visualization/widowx_stack_cube_visual_matching.png" width="128" height="128" > |
| widowx_put_eggplant_in_basket        | PutEggplantInBasketScene-v0  | <img src="./images/example_visualization/widowx_put_eggplant_in_basket_visual_matching.png" width="128" height="128" > |

We also support creating sub-tasks variations such as `google_robot_pick_{horizontal/vertical/standing}_coke_can`, `google_robot_open_{top/middle/bottom}_drawer`, and `google_robot_close_{top/middle/bottom}_drawer`. For the `google_robot_place_in_closed_drawer` task, we use the `google_robot_place_apple_in_closed_top_drawer` subtask for paper evaluations.

By default, Google Robot environments use a control frequency of 3hz, and Bridge environments use a control frequency of 5hz. Simulation frequency is ~500hz.


## Compare Your Policy Evaluation Approach to SIMPLER

We make it easy to compare your offline robot policy evaluation approach to SIMPLER. In [our paper](https://simpler-env.github.io/), we use two metrics to measure the quality of simulated evaluation pipelines: Mean Maximum Rank Violation (MMRV) and the Pearson Correlation Coefficient. Both capture how well the offline evaluations reflect the policy's real-world performance and behaviors during robot rollouts.

To make comparisons easy, we provide our real and SIMPLER evaluation performance for all policies on all tasks. We also provide the corresponding functions for computing the aforementioned metrics we report in the paper.

To compute the corresponding metrics for *your* offline policy evaluation approach `your_sim_eval(task, policy)`, you can use the following snippet:
```
from simpler_env.utils.metrics import mean_maximum_rank_violation, pearson_correlation, REAL_PERF

sim_eval_perf = [
    your_sim_eval(task="google_robot_move_near", policy=p) 
    for p in ["rt-1-x", "octo", ...]
]
real_eval_perf = [
    REAL_PERF["google_robot_move_near"][p] for p in ["rt-1-x", "octo", ...]
]
mmrv = mean_maximum_rank_violation(real_eval_perf, sim_eval_perf)
pearson = pearson_correlation(real_eval_perf, sim_eval_perf)
```

To reproduce the key numbers from our paper for SIMPLER, you can run the [`tools/calc_metrics.py`](tools/calc_metrics.py) script:
```
python3 tools/calc_metrics.py
```

## Code Structure

```
ManiSkill2_real2sim/: the ManiSkill2 real-to-sim environment codebase, which contains the environments, robots, and objects for real-to-sim evaluation.
   data/
      custom/: custom object assets (e.g., coke can, cabinet) and their infos
      hab2_bench_assets/: custom scene assets
      real_inpainting/: real-world inpainting images for visual matching evaluation
      debug/: debugging assets
   mani_skill2_real2sim/
      agents/: robot agents, configs, and controller implementations
      assets/: robot assets such as URDF and meshes
      envs/: environments
      examples/demo_manual_control_custom_envs.py: interactive script for environment visualization and manual
      utils/
   ...
simpler_env/
   evaluation/: real-to-sim evaluator with advanced environment building and logging
      argparse.py: argument parser supporting custom policy and environment building
      maniskill2_evaluator.py: evaluator that supports environment parameter sweeps and advanced logging
   policies/: policy implementations
      rt1/: RT-1 policy implementation
      octo/: Octo policy implementation
   utils/:
      env/: environment building and observation utilities
      debug/: debugging tools for policies and robots
      ...
   main_inference.py: main inference script, taking in args from evaluation.argparse and calling evaluation.maniskill2_evaluator
   simple_inference_visual_matching_prepackaged_envs.py: an independent simple inference script on prepackaged environments, doesn't depend on evaluation/*
tools/
   robot_object_visualization/: tools for visualizing robots and objects when creating new environments
   sysid/: tools for system identification when adding new robots
   calc_metrics.py: tools for summarizing eval results and calculating metrics, such as Mean Maximum Rank Violation (MMRV) and Pearson Correlation
   coacd_process_mesh.py: tools for generating convex collision meshes through CoACD when adding new assets
   merge_videos.py: tools for merging videos into one
   ...
scripts/: example bash scripts for policy inference under our variant aggregation / visual matching evaluation setup,
          with custom environment building and advanced logging; also useful for reproducing our evaluation results
...
```

## Adding New Policies

If you want to use existing environments for evaluating new policies, you can keep `./ManiSkill2_real2sim` as is.

1. Implement new policy inference scripts in `simpler_env/policies/{your_new_policy}`, following the examples for RT-1 (`simpler_env/policies/rt1`) and Octo (`simpler_env/policies/octo`) policies.
2. You can now use `simpler_env/simple_inference_visual_matching_prepackaged_envs.py` to perform policy evaluations in simulation.
   - If the policy behaviors deviate a lot from those in the real-world, you can write similar scripts as in `simpler_env/utils/debug/{policy_name}_inference_real_video.py` to debug the policy behaviors. The debugging script performs policy inference by feeding real eval video frames into the policy. If the policy behavior still deviates significantly from real, this may suggest that policy actions are processed incorrectly into the simulation environments. Please double check action orderings and action spaces.
3. If you'd like to perform customized evaluations,
   - Modify a few lines in `simpler_env/main_inference.py` to support your new policies.
   - Add policy inference scripts in `scripts/` with customized configs.
   - Optionally, modify the scripts in `tools/calc_metrics.py` to calculate the real-to-sim evaluation metrics for your new policies.


## Adding New Real-to-Sim Evaluation Environments and Robots

We provide a step-by-step guide to add new real-to-sim evaluation environments and robots in [this README](ADDING_NEW_ENVS_ROBOTS.md)


## Full Installation (RT-1 and Octo Inference, Env Building)

If you'd like to perform evaluations on our provided agents (e.g., RT-1, Octo), or add new robots and environments, please follow the full installation instructions below.

```
sudo apt install ffmpeg
```

```
pip install tensorflow==2.15.0
pip install -r requirements_full_install.txt
pip install tensorflow[and-cuda]==2.15.1 # tensorflow gpu support
```

Install simulated annealing utils for system identification:
```
pip install git+https://github.com/nathanrooy/simulated-annealing
```

### RT-1 Inference Setup

Download RT-1 Checkpoint:
```
# First, install gsutil following https://cloud.google.com/storage/docs/gsutil_install

# Make a checkpoint dir:
mkdir {this_repo}/checkpoints

# RT-1-X
cd {this_repo}
gsutil -m cp -r gs://gdm-robotics-open-x-embodiment/open_x_embodiment_and_rt_x_oss/rt_1_x_tf_trained_for_002272480_step.zip .
unzip rt_1_x_tf_trained_for_002272480_step.zip
mv rt_1_x_tf_trained_for_002272480_step checkpoints
rm rt_1_x_tf_trained_for_002272480_step.zip

# RT-1-Converged
cd {this_repo}
gsutil -m cp -r gs://gdm-robotics-open-x-embodiment/open_x_embodiment_and_rt_x_oss/rt_1_tf_trained_for_000400120 .
mv rt_1_tf_trained_for_000400120 checkpoints

# RT-1-15%
cd {this_repo}
gsutil -m cp -r gs://gdm-robotics-open-x-embodiment/open_x_embodiment_and_rt_x_oss/rt_1_tf_trained_for_000058240 .
mv rt_1_tf_trained_for_000058240 checkpoints

# RT-1-Begin
cd {this_repo}
gsutil -m cp -r gs://gdm-robotics-open-x-embodiment/open_x_embodiment_and_rt_x_oss/rt_1_tf_trained_for_000001120 .
mv rt_1_tf_trained_for_000001120 checkpoints      
```

### Octo Inference Setup

Install Octo:
```
pip install --upgrade "jax[cuda11_pip]==0.4.20" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html # or jax[cuda12_pip] if you have CUDA 12

cd {this_repo}
git clone https://github.com/octo-models/octo/
cd octo
git checkout 653c54acde686fde619855f2eac0dd6edad7116b  # we use octo-1.0
pip install -e .
# You don't need to run "pip install -r requirements.txt" inside the octo repo; the package dependencies are already handled in the simpler_env repo
# Octo checkpoints are managed by huggingface, so you don't need to download them manually.
```

If you are using CUDA 12, then to use GPU for Octo inference, you need CUDA version >= 12.2 to satisfy the requirement of Jax; in this case, you can perform a runfile install of the corresponding CUDA (e.g., version 12.3), then set the environment variables whenever you run Octo inference scripts:

`PATH=/usr/local/cuda-12.3/bin:$PATH   LD_LIBRARY_PATH=/usr/local/cuda-12.3/lib64:$LD_LIBRARY_PATH   bash scripts/octo_xxx_script.sh`

## Troubleshooting

1. If you encounter issues such as

```
RuntimeError: vk::Instance::enumeratePhysicalDevices: ErrorInitializationFailed
Some required Vulkan extension is not present. You may not use the renderer to render, however, CPU resources will be still available.
Segmentation fault (core dumped)
```

Follow [this link](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html#vulkan) to troubleshoot the issue. (Even though the doc points to SAPIEN 3 and ManiSkill3, the troubleshooting section still applies to the current environments that use SAPIEN 2.2 and ManiSkill2).

2. You can ignore the following error if it is caused by tensorflow's internal code. Sometimes this error will occur when running the inference or debugging scripts.

```
TypeError: 'NoneType' object is not subscriptable
```


## Citation

If you find our ideas / environments helpful, please cite our work at
```
@article{li24simpler,
         title={Evaluating Real-World Robot Manipulation Policies in Simulation},
         author={Xuanlin Li and Kyle Hsu and Jiayuan Gu and Karl Pertsch and Oier Mees and Homer Rich Walke and Chuyuan Fu and Ishikaa Lunawat and Isabel Sieh and Sean Kirmani and Sergey Levine and Jiajun Wu and Chelsea Finn and Hao Su and Quan Vuong and Ted Xiao},
         journal = {arXiv preprint arXiv:2405.05941},
         year={2024}
}
```


## File tree (depth 3, assets pruned)

```
.flake8
.gitignore
.gitmodules
.pre-commit-config.yaml
ADDING_NEW_ENVS_ROBOTS.md
LICENSE
ManiSkill2_real2sim/
README.md
example.ipynb
pyproject.toml
requirements_full_install.txt
scripts/
  misc/
    octo_drawer_variant_agg_alt_urdf.sh
    octo_move_near_variant_agg_alt_urdf.sh
    octo_pick_coke_can_variant_agg_alt_urdf.sh
  octo_bridge.sh
  octo_drawer_variant_agg.sh
  octo_drawer_visual_matching.sh
  octo_move_near_variant_agg.sh
  octo_move_near_visual_matching.sh
  octo_pick_coke_can_variant_agg.sh
  octo_pick_coke_can_visual_matching.sh
  octo_put_in_drawer_variant_agg.sh
  octo_put_in_drawer_visual_matching.sh
  rt1_drawer_variant_agg.sh
  rt1_drawer_visual_matching.sh
  rt1_move_near_variant_agg.sh
  rt1_move_near_visual_matching.sh
  rt1_pick_coke_can_variant_agg.sh
  rt1_pick_coke_can_visual_matching.sh
  rt1_put_in_drawer_variant_agg.sh
  rt1_put_in_drawer_visual_matching.sh
  rt1x_bridge.sh
setup.py
simpler_env/
  __init__.py
  evaluation/
    __init__.py
    argparse.py
    maniskill2_evaluator.py
  main_inference.py
  policies/
    __init__.py
    octo/
    rt1/
  simple_inference_visual_matching_prepackaged_envs.py
  utils/
    __init__.py
    action/
    debug/
    env/
    fonts/
    io.py
    metrics.py
    visualization.py
tools/
  calc_metrics.py
  calc_metrics_evaluation_videos.py
  coacd_process_mesh.py
  merge_videos.py
  robot_object_visualization/
    test_googlerobot.py
    test_object.py
    test_widowx.py
  save_video_frame.py
  sysid/
    analyze_sysid_results.py
    prepare_sysid_dataset.py
    sysid.py
  visualize_dataset.py
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
default_language_version:
    python: python3.10
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-yaml
      - id: check-ast
      - id: check-added-large-files
        exclude: ^examples/
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: detect-private-key
      - id: debug-statements
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]
  - repo: https://github.com/srstevenson/nb-clean
    rev: 3.1.0
    hooks:
      - id: nb-clean
        args:
          - --remove-empty-cells
          - --preserve-cell-outputs

```

## Python signatures and reward/observation bodies (27 files)


### simpler_env/__init__.py

```
def make(task_name)
```

### simpler_env/evaluation/argparse.py

```
def parse_range_tuple(t)
def get_args()
```

### simpler_env/evaluation/maniskill2_evaluator.py

```
"""Evaluate a model on ManiSkill2 environment."""
def run_maniskill2_eval_single_episode(model, ckpt_path, robot_name, env_name, scene_name, robot_init_x, robot_init_y, robot_init_quat, control_mode, obj_init_x, obj_init_y, obj_episode_id, additional_env_build_kwargs, rgb_overlay_path, obs_camera_name, control_freq, sim_freq, max_episode_steps, instruction, enable_raytracing, additional_env_save_tags, logging_dir)
def maniskill2_evaluator(model, args)
```

### simpler_env/policies/octo/octo_model.py

```
class OctoInference()
    def __init__(self, model, dataset_id, model_type, policy_setup, horizon, pred_action_horizon, exec_horizon, image_size, action_scale, init_rng)
    def _resize_image(self, image)
    def _add_image_to_history(self, image)
    def _obtain_image_history_and_mask(self)
    def reset(self, task_description)
    def step(self, image, task_description)
    def visualize_epoch(self, predicted_raw_actions, images, save_path)
```

### simpler_env/policies/octo/octo_server_model.py

```
def default(obj)
def object_hook(dct)
def dumps()
def loads()
def dump()
def load()
def patch()
class OctoServerInference()
    def __init__(self, model_type, policy_setup, image_size, action_scale)
    def _resize_image(self, image)
    def reset(self, task_description)
    def _get_fake_pay_load(self, image_primary, text, modality)
    def _query_for_action(self, image_primary, text, goal, modality)
    def step(self, image, task_description)
    def visualize_epoch(self, predicted_raw_actions, images, save_path)
```

### simpler_env/policies/rt1/rt1_model.py

```
class RT1Inference()
    def __init__(self, saved_model_path, lang_embed_model_path, image_width, image_height, action_scale, policy_setup)
    def _rescale_action_with_bound(actions, low, high, safety_margin, post_scaling_max, post_scaling_min)
    def _unnormalize_action_widowx_bridge(self, action)
    def _initialize_model(self)
    def _resize_image(self, image)
    def _initialize_task_description(self, task_description)
    def reset(self, task_description)
    def _small_action_filter_google_robot(raw_action, arm_movement, gripper)
    def step(self, image, task_description)
    def visualize_epoch(self, predicted_raw_actions, images, save_path)
```

### simpler_env/simple_inference_visual_matching_prepackaged_envs.py

```
"""Simple script for real-to-sim eval using the prepackaged visual matching setup in ManiSkill2.
Example:
    cd {path_to_simpler_env_repo_root}
    python simpler_env/simple_inference_visual_matching_prepackaged_envs.py --policy rt1         --ckpt-path ./checkpoints/rt_1_tf_trained_for_000400120  --task google_robot_pick_coke_can  --logging-root ./results_simple_eval/  --n-trajs 10
    python simpler_env/simple_inference_visual_matching_prepackaged_envs.py --policy octo-small         --ckpt-path None --task widowx_spoon_on_towel  --logging-root ./results_simple_eval/  --n-trajs 10"""
```

### simpler_env/utils/action/action_ensemble.py

```
class ActionEnsembler()
    def __init__(self, pred_action_horizon, action_ensemble_temp)
    def reset(self)
    def ensemble_action(self, cur_action)
```

### simpler_env/utils/debug/google_robot_test_dataset_inference_rollout_gt_traj_in_sim.py

```
"""Step ground-truth actions in a dataset in an open-loop manner and record the resulting observation video and robot qpos."""
def dataset2path(dataset_name)
def main(dset_iter, iter_num, episode_id, control_mode, save_root, step_action)
```

### simpler_env/utils/debug/octo_inference_real_video.py

```
"""Uses:
1. Given a static (inpainting) image (with robot arm removed), query the Octo model to predict actions and visualize them in the environment,
    where the policy input is the inpainting image plus the robot arm rendered in it.
2. Given a video, feed the video frames as input to the Octo model, and visualize the resulting actions in the environment."""
def main(input_video, inpainting_img_path, instruction, gt_tcp_pose_at_robot_base, camera, model_type, policy_setup, robot, control_freq, max_episode_steps, control_mode, save_root, save_name)
```

### simpler_env/utils/debug/rt1_inference_real_video.py

```
"""Uses:
1. Given a static (inpainting) image (with robot arm removed), query the RT-1 model to predict actions and visualize them in the environment,
    where the policy input is the inpainting image plus the robot arm rendered in it.
2. Given a video, feed the video frames as input to the RT-1 model, and visualize the resulting actions in the environment."""
def main(input_video, inpainting_img_path, instruction, ckpt_path, control_freq, control_mode, policy_setup, robot, init_tcp_pose_at_robot_base, init_robot_base_pos, overlay_camera, save_root, save_name)
```

### simpler_env/utils/debug/rt1_plot_dataset_inference_trajectory.py

```
"""Run RT-1 model on a dataset and plot the predicted and ground truth action trajectory."""
def dataset2path(dataset_name)
def main(episode, model, model_type)
```

### simpler_env/utils/debug/widowx_test_dataset_inference_rollout_gt_traj_in_sim.py

```
"""Step ground-truth actions in a dataset in an open-loop manner and record the resulting observation video and robot qpos."""
def dataset2path(dataset_name)
def main(dset_iter, iter_num, episode_id, control_mode, save_root, overlay_camera)
```

### simpler_env/utils/env/env_builder.py

```
def build_maniskill2_env(env_name)
def get_robot_control_mode(robot_name, policy_name)
```

### simpler_env/utils/env/observation_utils.py

```
def get_image_from_maniskill2_obs_dict(env, obs, camera_name)
```

### simpler_env/utils/io.py

```
def is_path(path)
def load_image_pils(image_paths)
def load_image_arrays(image_paths)
class DictAction(Action)
    """argparse action to split an argument into KEY=VALUE form
on the first = and append to a dictionary. List options can
be passed as comma separated values, i.e 'KEY=V1,V2,V3', or with explicit
brackets, i.e. 'KEY=[V1,V2,V3]'. It also support nested brackets to build
list/tuple values. e.g. 'KEY=[(V1,V"""
    def _parse_int_float_bool(val)
    def _parse_iterable(val)
    def __call__(self, parser, namespace, values, option_string)
```

### simpler_env/utils/metrics.py

```
def pearson_correlation(perf_sim, perf_real)
def mean_maximum_rank_violation(perf_sim, perf_real)
def print_all_kruskal_results(sim, real, title)
def construct_unordered_trial_results(n_trials_per_ckpt, success)
def get_dir_stats(dir_name, extra_pattern_require, succ_fail_pattern)
```

### simpler_env/utils/visualization.py

```
def write_video(path, images, fps)
def plot_pred_and_gt_action_trajectory(predicted_actions, gt_actions, stacked_images)
```