# dexmimicgen_2024

source: https://github.com/NVlabs/dexmimicgen


commit: 940e8a1b3ad70eb1925ada6b364b197de6bb2af9


## README

# DexMimicGen

<p align="center">
  <img width="95.0%" src="images/dexmimicgen.gif">
</p>

This repository contains the official release of simulation environments and datasets for the [ICRA 2025](https://2025.ieee-icra.org) paper "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning".

Website: https://dexmimicgen.github.io

Paper: https://arxiv.org/abs/2410.24185

For business inquiries, please submit this form: [NVIDIA Research Licensing](https://www.nvidia.com/en-us/research/inquiries/)

-------

## Getting Started

To use this repository, you need to first install the latest robosuite. For more
information, please refer to [robosuite](https://github.com/ARISE-Initiative/robosuite).

```bash
git clone https://github.com/ARISE-Initiative/robosuite
pip install -e robosuite
```

Then git clone this repository and install.

```bash
git clone https://github.com/NVlabs/dexmimicgen.git
cd dexmimicgen
pip install -e .
```

After installation, you can run the following command to test the environments.

```bash
python scripts/demo_random_action.py --env TwoArmThreading --render
```

Note: If you are on a headless machine, you can run without the `--render` flag.

## Environments

For detailed information about the environments, please refer to [environments.md](environments.md).

## Datasets

You can download the datasets from [HuggingFace](https://huggingface.co/datasets/MimicGen/dexmimicgen_datasets/tree/main).

You can also run the script to download the datasets.

```bash
python scripts/download_hf_dataset.py --path /path/to/save/datasets
```

By default, the datasets will be saved to `./datasets`.

And then, you can playback one demo in the dataset by running:

```bash
python scripts/playback_datasets.py --dataset xxxxx.hdf5 --n 1
```

## Launch Training with robomimic

We provide config and training code to reproduce the BC-RNN result in our paper.

First, you need to install robomimic

```bash

git clone https://github.com/ARISE-Initiative/robomimic.git -b dexmimicgen
cd robomimic
pip install -e .
```

Then you need to generate the config file for the training.

```bash
cd dexmimicgen
python scripts/generate_training_config.py --dataset_dir /path/to/datasets --config_dir /path/to/save/config --output_dir /path/to/save/output
```

By default, it will try to find the datasets in `./datasets`, and save the config and output in `./datasets/train_configs/bcrnn_action_dict` and `./datasets/train_results/bcrnn_action_dict` respectively.

After that, you can run the training script.

```bash
cd robomimic
python scripts/train.py --config /path/to/config
```

## License

The code is released under the [NVIDIA Source Code License](https://github.com/NVlabs/mimicgen/blob/main/LICENSE) and the datasets are released under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Citation

Please cite [the DexMimicGen paper](https://arxiv.org/abs/2410.24185) if you use this code in your work:

```bibtex
@inproceedings{jiang2024dexmimicen,
      title     = {DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning},
      author    = {Jiang, Zhenyu and Xie, Yuqi and Lin, Kevin and Xu, Zhenjia and Wan, Weikang and Mandlekar, Ajay and Fan, Linxi and Zhu, Yuke},
      booktitle = {2025 IEEE International Conference on Robotics and Automation (ICRA)},
      year      = {2025}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
.pre-commit-config.yaml
LICENSE
README.md
add_license_header.py
dexmimicgen/
  __init__.py
  environments/
    __init__.py
    two_arm_box_cleanup.py
    two_arm_can_sort.py
    two_arm_coffee.py
    two_arm_dexmg_env.py
    two_arm_drawer_cleanup.py
    two_arm_lift_tray.py
    two_arm_pouring.py
    two_arm_threading.py
    two_arm_three_piece_assembly.py
    two_arm_transport.py
  models/
    __init__.py
    objects/
  utils/
    config_utils.py
    mjcf_utils.py
    transform_utils.py
environments.md
requirements.txt
scripts/
  demo_random_action.py
  download_hf_dataset.py
  generate_training_config.py
  playback_datasets.py
setup.py
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0 # Replace by any tag/version: https://github.com/psf/black/tags
    hooks:
      - id: black
        language_version: python3 # Should be a command that runs python3.6+
  - repo: https://github.com/pycqa/isort
    rev: 6.0.0
    hooks:
      - id: isort
        args: ["--profile", "black"]
  # - repo: local
  #   hooks:
  #     - id: no-github-remote-urls
  #       name: Check remote URLs for forbidden keywords
  #       entry: python check_no_github_urls.py
  #       language: python

```

## Python signatures and reward/observation bodies (15 files)


### dexmimicgen/environments/two_arm_box_cleanup.py

```
class TwoArmBoxCleanup(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config, use_translucent_lid)
    def reward(self, action)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _check_success(self)
    def visualize(self, vis_settings)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_can_sort.py

```
class TwoArmCanSortRandom(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config, red_prob, use_cylinder)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _initialize_object_states(self)
    def _check_success(self)
    def visualize(self, vis_settings)
    def reward(self, action)
class TwoArmCanSortRed(TwoArmCanSortRandom)
    def __init__(self)
class TwoArmCanSortBlue(TwoArmCanSortRandom)
    def __init__(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_coffee.py

```
class TwoArmCoffee(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config, lid_start_value, make_coffee_machine_fixture)
    def get_coffee_machine_pod_margin(self)
    def reward(self, action)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_initial_placement_bounds(self)
    def _get_placement_initializer(self)
    def _reset_internal(self)
    def _setup_references(self)
    def _check_success(self)
    def _check_lid(self)
    def _check_pod(self)
    def _get_partial_task_metrics(self)
    def _check_pod_is_grasped(self)
    def _check_pod_and_pod_holder_contact(self)
    def _check_pod_on_rim(self)
    def _check_pod_being_inserted(self)
    def _check_pod_inserted(self)
    def _check_lid_being_closed(self)
    def visualize(self, vis_settings)
class TwoArmCoffeeLidClosed(TwoArmCoffee)
    """Harder version of coffee task where lid starts closed."""
    def __init__(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_dexmg_env.py

```
class TwoArmDexMGEnv(TwoArmEnv)
    def __init__(self, translucent_robot)
    def robot_joint_names(self)
    def set_robot_state(self, init_state)
    def _load_model(self)
    def _reset_internal(self)
    def get_state(self)
    def edit_model_xml(self, xml_str)
```

### dexmimicgen/environments/two_arm_drawer_cleanup.py

```
class TwoArmDrawerCleanup(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _get_drawer_model(self)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _reset_internal(self)
    def _check_drawer_close(self)
    def _check_object(self)
    def _check_success(self)
    def visualize(self, vis_settings)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_lift_tray.py

```
class TwoArmLiftTray(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def visualize(self, vis_settings)
    def _check_success(self)
    def _handle0_xpos(self)
    def _handle1_xpos(self)
    def _pot_quat(self)
    def _gripper0_to_handle0(self)
    def _gripper1_to_handle1(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 3.0 is provided if the pot is lifted and is parallel within 30 deg to the table

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 0.5], per-arm component that is proportional to the distance between each arm and its
              respective pot handle, and exactly 0.5 when grasping the handle
              - Note that the agent only gets the lifting reward when flipping no more than 30 degrees.
            - Grasping: in {0, 0.25}, binary per-arm component awarded if the gripper is grasping its correct handle
            - Lifting: in [0, 1.5], proportional to the pot's height above the table, and capped at a certain threshold

        Note that the final reward is normalized and scaled by reward_scale / 3.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0

        # check if the pot is tilted more than 30 degrees
        mat = T.quat2mat(self._pot_quat)
        z_unit = [0, 0, 1]
        z_rotated = np.matmul(mat, z_unit)
        cos_z = np.dot(z_unit, z_rotated)
        cos_30 = np.cos(np.pi / 6)
        direction_coef = 1 if cos_z >= cos_30 else 0

        # check for goal completion: cube is higher than the table top above a margin
        if self._check_success():
            reward = 3.0 * direction_coef

        # use a shaping reward
        elif self.reward_shaping:
            # lifting reward
            pot_bottom_height = (
                self.sim.data.site_xpos[self.pot_center_id][2] - self.pot.top_offset[2]
            )
            table_height = self.sim.data.site_xpos[self.table_top_id][2]
            elevation = pot_bottom_height - table_height
            r_lift = min(max(elevation - 0.05, 0), 0.15)
            reward += 10.0 * direction_coef * r_lift

            _gripper0_to_handle0 = self._gripper0_to_handle0
            _gripper1_to_handle1 = self._gripper1_to_handle1

            # gh stands for gripper-handle
            # When grippers are far away, tell them to be closer

            # Get contacts
            (g0, g1) = (
                (self.robots[0].gripper["right"], self.robots[0].gripper["left"])
                if self.env_configuration == "single-robot"
                else (self.robots[0].gripper["right"], self.robots[1].gripper)
            )

            _g0h_dist = np.linalg.norm(_gripper0_to_handle0)
            _g1h_dist = np.linalg.norm(_gripper1_to_handle1)

            # Grasping reward
            if self._check_grasp(gripper=g0, object_geoms=self.pot.handle0_geoms):
                reward += 0.25
            # Reaching reward
            reward += 0.5 * (1 - np.tanh(10.0 * _g0h_dist))

            # Grasping reward
            if self._check_grasp(gripper=g1, object_geoms=self.pot.handle1_geoms):
                reward += 0.25
            # Reaching reward
            reward += 0.5 * (1 - np.tanh(10.0 * _g1h_dist))

        if self.reward_scale is not None:
            reward *= self.reward_scale / 3.0
        return reward
```
```

### dexmimicgen/environments/two_arm_pouring.py

```
class TwoArmPouring(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _get_objects(self)
    def _load_model(self)
    def _modify_camera_view(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _reset_internal(self)
    def _check_success(self)
    def _get_vis_target_object(self)
    def visualize(self, vis_settings)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_threading.py

```
class TwoArmThreading(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _check_success(self)
    def visualize(self, vis_settings)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Dense reward: TODO

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_three_piece_assembly.py

```
class TwoArmThreePieceAssembly(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, table_offset, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def _get_piece_densities(self)
    def reward(self, action)
    def _get_piece_patterns(self)
    def _load_model(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _check_success(self)
    def _check_first_piece_is_assembled(self, xy_thresh)
    def _check_second_piece_is_assembled(self, xy_thresh, z_thresh)
    def _get_partial_task_metrics(self)
    def visualize(self, vis_settings)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Dense reward: TODO

        The sparse reward only consists of the threading component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            pass

        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### dexmimicgen/environments/two_arm_transport.py

```
class TwoArmTransport(TwoArmDexMGEnv)
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, tables_boundary, table_friction, bin_size, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _reset_internal(self)
    def _check_success(self)
    def _check_lid_on_table(self)
    def _check_payload_lifted(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 1.0 is provided when the payload is in the target bin and the trash is in the trash
                bin

        Un-normalized max-wise components if using reward shaping:

            # TODO!

        Note that the final reward is normalized and scaled by reward_scale / 1.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        # Initialize reward
        reward = 0

        # use a shaping reward if specified
        if self.reward_shaping:
            # TODO! So we print a warning and force sparse rewards
            print(
                "\n\nWarning! No dense reward current implemented for this task. Forcing sparse rewards\n\n"
            )
            self.reward_shaping = False

        # Else this is the sparse reward setting
        else:
            # Provide reward if payload is in target bin and trash is in trash bin
            if self._check_success():
                reward = 1.0

        if self.reward_scale is not None:
            reward *= self.reward_scale / 1.0

        return reward
```
```

### dexmimicgen/models/objects/composite/pot_with_handles.py

```
class PotWithHandlesObject(CompositeObject)
    """Generates the Pot object with side handles (used in TwoArmLift)

Args:
    name (str): Name of this Pot object

    body_half_size (3-array of float): If specified, defines the (x,y,z) half-dimensions of the main pot
        body. Otherwise, defaults to [0.07, 0.07, 0.07]

    handle_radius (float):"""
    def __init__(self, name, body_half_size, handle_radius, handle_length, handle_width, handle_friction, density, use_texture, rgba_body, rgba_handle_0, rgba_handle_1, solid_handle, thickness)
    def _get_geom_attrs(self)
    def handle_distance(self)
    def handle0_geoms(self)
    def handle1_geoms(self)
    def handle_geoms(self)
    def important_sites(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### dexmimicgen/utils/config_utils.py

```
def set_learning_settings_for_bc_rnn(generator, group, seq_length, low_dim_keys, image_keys, crop_size, dataset_paths, dataset_names, horizon, output_dir)
def config_generator_to_script_lines(generator, config_dir)
```

### scripts/demo_random_action.py

```
"""Run random actions in dexmimicgen environments.

Args:
    --env (str): Name of the environment to run (default: "TwoArmThreading").
    --render (bool): Whether to render the environment.

Example usage:
    python script.py --env TwoArmPouring --render"""
```

### scripts/generate_training_config.py

```
"""Robomimic Training Configuration Generator

Args:
    --dataset_dir (str): Path to the dataset directory (default: "../datasets").
    --config_dir (str): Path to store the generated training configurations
        (default: "../datasets/train_configs/bcrnn_action_dict").
    --output_dir (str): Path to store the training results
        (default: "../datasets/training_results/bcrnn_action_dict").

Example usage:
    python script.py --dataset_dir /path/to/dataset --config_dir /path/to/configs --output_dir /path/to/results"""
def make_generators(base_config, dataset_dir, output_dir)
def make_gen(base_config, settings, output_dir)
def panda_action_config(generator)
def humanoid_action_config(generator)
def main(args)
```