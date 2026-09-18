# robohive_2023

source: https://github.com/vikashplus/robohive


commit: 6c14798e48b9904dd8c9151837a1d2468b87bcf3


## README

<!-- =================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
================================================= -->

<!-- # RoboHive -->

[![report](https://img.shields.io/badge/Project-Page-blue)](https://sites.google.com/view/robohive/)
[![report](https://img.shields.io/badge/ArXiv-Paper-green)](https://arxiv.org/abs/2310.06828)
[![Documentation](https://img.shields.io/static/v1?label=Wiki&message=Documentation&color=<green)](https://github.com/vikashplus/robohive/wiki) ![PyPI](https://img.shields.io/pypi/v/robohive)
![PyPI - License](https://img.shields.io/pypi/l/robohive)
[![Downloads](https://pepy.tech/badge/robohive)](https://pepy.tech/project/robohive)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rdSgnsfUaE-eFLjAkFHeqfUWzAK8ruTs?usp=sharing)
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://robohiveworkspace.slack.com)

![RoboHive Social Preview](https://github.com/vikashplus/robohive/assets/12837145/04aff6da-f9fa-4f5f-abc6-cfcd70c6cd90)
`RoboHive` is a collection of environments/tasks simulated with the [MuJoCo](http://www.mujoco.org/) physics engine exposed using the OpenAI-Gym API. Its compatible with any gym-compatible agents training framework ([Stable Baselines](https://stable-baselines3.readthedocs.io/en/master), [RLlib](https://docs.ray.io/en/latest/rllib/index.html), [TorchRL](https://pytorch.org/rl/), [AgentHive](https://sites.google.com/view/robohive/baseline), etc)

# Getting Started
   Getting started with RoboHive is as simple as -
   ``` bash
   # Install RoboHive
   pip install robohive
   # Initialize RoboHive
   robohive_init
   # Demo an environment
   python -m robohive.utils.examine_env -e FrankaReachRandom-v0
   ```

   or, alternatively for editable installation -

   ``` bash
   # Clone RoboHive
   git clone --recursive https://github.com/vikashplus/robohive.git; cd robohive
   # Install (editable) RoboHive
   pip install -e .
   # Demo an environment
   python -m robohive.utils.examine_env -e FrankaReachRandom-v0
   ```

   See [detailed installation instructions](./setup/README.md) for options on mujoco-python-bindings and  visual-encoders ([R3M](https://sites.google.com/view/robot-r3m/), [RRL](https://sites.google.com/view/abstractions4rl), [VC](https://eai-vc.github.io/)), and [frequently asked questions](https://github.com/vikashplus/robohive/wiki/6.-Tutorials-&-FAQs#installation) for more details.

# Suites
*RoboHive* contains a variety of environments, which are organized as suites. Each suite is a collection of loosely related environments. The following suites are provided at the moment with plans to improve the diversity of the collection.

**Hand-Manipulation-Suite** [(video)](https://youtu.be/jJtBll8l_OM)
:-------------------------:
![Alt text](https://raw.githubusercontent.com/vikashplus/robohive/f786982204e85b79bd921aa54ffebf3a7887de3d/mj_envs/hand_manipulation_suite/assets/tasks.jpg?raw=false "Hand Manipulation Suite") A collection of environments centered around dexterous manipulation. Standard ADROIT benchmarks introduced in [Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations, RSS2018](https://sites.google.com/corp/view/deeprl-dexterous-manipulation).) are a part of this suite


Arm-Manipulation-Suite
:-------------------------:
![Alt text](https://github.com/vikashplus/robohive/assets/12837145/ef072b90-42e7-414b-9da0-45c87c31443a?raw=false "Arm Manipulation Suite") A collection of environments centered around Arm manipulation.


Myo-Suite [(website)](https://sites.google.com/view/myosuite)
:-------------------------:
![Alt text](https://github.com/vikashplus/robohive/assets/12837145/0db70854-cb90-4360-8bd9-42cd1b5446c1?raw=false "Myo_Suite") A collection of environments centered around Musculoskeletal control.


Myo/MyoDM-Suite [(Website)](https://sites.google.com/view/myodex)
:-------------------------:
![myodm_task_suite](https://github.com/vikashplus/robohive/assets/12837145/2ca62e77-6827-4029-930e-b95ab86ae0f4) A collection of musculoskeletal environments for dexterous manipulation introduced as MyoDM in [MyoDeX](https://sites.google.com/view/myodex).


MultiTask Suite
:-------------------------:
![Alt text](https://github.com/vikashplus/robohive/assets/12837145/b7f314b9-8d4e-4e58-b791-6df774b91d21?raw=false "Myo_Suite") A collection of environments centered around multi-task. Standard [RelayKitchen benchmarks](https://relay-policy-learning.github.io/) are a part of this suite.

## - TCDM Suite (WIP)
   This suite contains a collection of environments centered around dexterous manipulation. Standard [TCDM benchmarks](https://pregrasps.github.io/) are a part of this suite

## - ROBEL Suite (Coming soon)
   This suite contains a collection of environments centered around real-world locomotion and manipulation. Standard [ROBEL benchmarks](http://roboticsbenchmarks.org/) are a part of this suite

# Citation
If you find `RoboHive` useful in your research,
- please consider supporting the project by providing a [star ⭐](https://github.com/vikashplus/robohive/stargazers)
- please consider citing our project by using the following BibTeX entry:



```bibtex
@Misc{RoboHive2020,
  title = {RoboHive -- A Unified Framework for Robot Learning},
  howpublished = {\url{https://sites.google.com/view/robohive}},
  year = {2020},
  url = {https://sites.google.com/view/robohive},
}


## File tree (depth 3, assets pruned)

```
.gitattributes
.github/
  workflows/
    python-app.yml
.gitignore
.gitmodules
LICENSE
README.md
robohive/
  __init__.py
  envs/
    __init__.py
    arms/
    claws/
    env_base.py
    env_variants.py
    fm/
    hands/
    multi_task/
    myo/
    obs_vec_dict.py
    quadrupeds/
    tcdm/
  logger/
    README.md
    examine_logs.py
    examine_reference.py
    grouped_datasets.py
    reference_motion.py
    roboset_logger.py
  physics/
    __init__.py
    mj_sim_scene.py
    mjpy_sim_scene.py
    randomize.py
    sim_scene.py
    sim_scene_test.py
  renderer/
    __init__.py
    mj_renderer.py
    mjpy_renderer.py
    renderer.py
  robot/
    README.md
    __init__.py
    capnp/
    hardware_base.py
    hardware_dynamixel.py
    hardware_franka.py
    hardware_optitrack.py
    hardware_realsense.py
    hardware_realsense_single.py
    hardware_robotiq.py
    robohive_robot_overview.png
    robot.py
    robot_viz.py
    serdes.py
  sandbox/
    dmanus_pickplace_script.py
  simhive/
    Adroit/
    YCB_sim/
    dmanus_sim/
    fetch_sim/
    franka_sim/
    furniture_sim/
    myo_sim/
    object_sim/
    robel_sim/
    robotiq_sim/
    sawyer_sim/
    scene_sim/
    trifinger_sim/
  tests/
    __init__.py
    test_all.py
    test_arms.py
    test_claws.py
    test_envs.py
    test_examine_env.py
    test_examine_robot.py
    test_fm.py
    test_hands.py
    test_logger.py
    test_multitask.py
    test_myo.py
    test_quads.py
    test_robot.py
    test_sb.py
    test_tcdm.py
    test_versions.sh
  tutorials/
    1_env_registration_and_customization.ipynb
    2_env_interactions.ipynb
    3_get_obs_proprio_extero.ipynb
    __init__.py
    ee_teleop.py
    ee_teleop_oculus.py
    examine_robot.py
    ik_minjerk_trajectory.py
    render_cams.py
  utils/
    __init__.py
    curriculum_utils.py
    dict_utils.py
    examine_env.py
    examine_sim.py
    implement_for.py
    import_utils.py
    inverse_kinematics.py
    min_jerk.py
    paths_utils.py
    prompt_utils.py
    quat_math.py
    tensor_utils.py
    vector_math.py
    xml_utils.py
robohive_init.py
setup/
  README.md
  env.yaml
setup.py
```

## Config files (2)


### robohive/envs/tcdm/myodex_selection.yaml

```yaml

grab_myo:
- s1/airplane_lift_myo.npz
- s1/airplane_pass_1_myo.npz
- s1/alarmclock_lift_myo.npz
- s1/alarmclock_pass_1_myo.npz
- s1/apple_lift_myo.npz
- s1/apple_pass_1_myo.npz
- s1/bowl_pass_1_myo.npz
- s1/camera_pass_1_myo.npz
- s1/cubelarge_pass_1_myo.npz
- s1/cubemedium_inspect_1_myo.npz
- s1/cubesmall_lift_myo.npz
- s1/cubesmall_pass_1_myo.npz
- s1/cup_pass_1_myo.npz
- s1/cylindermedium_lift_myo.npz
- s1/cylindermedium_pass_1_myo.npz
- s1/cylindersmall_inspect_1_myo.npz
- s1/cylindersmall_lift_myo.npz
- s1/cylindersmall_pass_1_myo.npz
- s1/duck_inspect_1_myo.npz
- s1/duck_lift_myo.npz
- s1/duck_pass_1_myo.npz
- s1/elephant_lift_myo.npz
- s1/elephant_pass_1_myo.npz
- s1/eyeglasses_pass_1_myo.npz
- s1/flashlight_lift_myo.npz
- s1/fryingpan_cook_2_myo.npz
- s1/hammer_pass_1_myo.npz
- s1/hammer_use_1_myo.npz
- s1/hand_pass_1_myo.npz
- s1/headphones_pass_1_myo.npz
- s1/knife_lift_myo.npz
- s1/mouse_lift_myo.npz
- s1/mouse_pass_1_myo.npz
- s1/mug_lift_myo.npz
- s1/mug_pass_1_myo.npz
- s1/phone_lift_myo.npz
- s1/pyramidlarge_pass_1_myo.npz
- s1/pyramidmedium_pass_1_myo.npz
- s1/pyramidsmall_inspect_1_myo.npz
- s1/spherelarge_pass_1_myo.npz
- s1/spheremedium_inspect_1_myo.npz
- s1/spheremedium_lift_myo.npz
- s1/spheresmall_inspect_1_myo.npz
- s1/spheresmall_lift_myo.npz
- s1/spheresmall_pass_1_myo.npz
- s1/stamp_lift_myo.npz
- s1/stamp_stamp_1_myo.npz
- s1/stanfordbunny_pass_1_myo.npz
- s1/stapler_lift_myo.npz
- s1/stapler_staple_1_myo.npz
- s1/stapler_staple_2_myo.npz
- s1/toothbrush_lift_myo.npz
- s1/toothpaste_lift_myo.npz
- s1/toruslarge_lift_myo.npz
- s1/torusmedium_lift_myo.npz
- s1/torusmedium_pass_1_myo.npz
- s1/torussmall_lift_myo.npz
- s1/torussmall_pass_1_myo.npz
- s1/train_play_1_myo.npz
- s1/watch_lift_myo.npz
- s1/waterbottle_lift_myo.npz
- s1/waterbottle_pass_1_myo.npz
- s1/wineglass_lift_myo.npz
- s1/wineglass_pass_1_myo.npz
- s2/banana_pass_1_myo.npz
- s5/hand_inspect_1_myo.npz
- s5/piggybank_pass_1_myo.npz
- s6/stanfordbunny_inspect_1_myo.npz
- s6/toruslarge_inspect_1_myo.npz
- s2/airplane_fly_1_myo.npz
- s2/cup_drink_1_myo.npz
- s2/flashlight_on_1_myo.npz
- s2/scissors_use_1_myo.npz
- s2/teapot_pour_2_myo.npz
- s3/cup_pour_1_myo.npz
- s3/toothpaste_squeeze_1_myo.npz
- s3/toothbrush_brush_1_myo.npz
- s3/mug_drink_3_myo.npz
- s5/flashlight_on_2_myo.npz
- s6/wineglass_toast_1_myo.npz
- s7/waterbottle_shake_1_myo.npz
- s8/alarmclock_see_1_myo.npz
- s8/piggybank_use_1_myo.npz
- s8/bowl_drink_2_myo.npz
- s9/wineglass_drink_2_myo.npz
- s9/binoculars_pass_1_myo.npz
- s9/flashlight_pass_1_myo.npz
- s10/wineglass_drink_1_myo.npz
- s10/flute_pass_1_myo.npz
- s10/lightbulb_pass_1_myo.npz
- s10/mouse_use_1_myo.npz
- s10/knife_chop_1_myo.npz
- s10/watch_pass_1_myo.npz

```

### setup/env.yaml

```yaml
name: robohive_base
channels:
  - pytorch
  - fair-robotics
  - aihabitat
  - conda-forge
  - defaults
dependencies:
  - cudatoolkit=11.3
  - gdown
  - hydra-core
  - polymetis
  - pytorch=1.10.0
  - torchvision
  - pillow
  - pip
  - pip:
    - click
    - gym==0.13
    - mujoco==2.3.3
    - mujoco-py<2.2,>=2.1
    - termcolor
    - sk-video
    - flatten_dict
    - matplotlib
    - ffmpeg
    - absl-py
    - pycapnp==1.1.0
    - r3m @ git+https://github.com/facebookresearch/r3m.git
    - h5py==3.7.0
    - alephzero # real_sense subscribers dependency

```

## Python signatures and reward/observation bodies (72 files)


### robohive/envs/arms/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def register_visual_envs(encoder_type)
```

### robohive/envs/arms/pick_place_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class PickPlaceV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, robot_ndof, robot_site_name, object_site_name, target_site_name, target_xyz_range, frame_skip, reward_mode, obs_keys, weighted_reward_keys, randomize, geom_sizes)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        object_dist = np.linalg.norm(obs_dict['object_err'], axis=-1)
        target_dist = np.linalg.norm(obs_dict['target_err'], axis=-1)
        far_th = 1.25

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('object_dist',   object_dist),
            ('target_dist',   target_dist),
            ('bonus',   (object_dist<.1) + (target_dist<.1) + (target_dist<.05)),
            ('penalty', (object_dist>far_th)),
            # Must keys
            ('sparse',  -1.0*target_dist),
            ('solved',  target_dist<.050),
            ('done',    object_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/arms/push_base_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class PushBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, robot_ndof, robot_site_name, object_site_name, target_site_name, target_xyz_range, frame_skip, reward_mode, obs_keys, proprio_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        object_dist = np.linalg.norm(obs_dict['object_err'], axis=-1)
        target_dist = np.linalg.norm(obs_dict['target_err'], axis=-1)
        far_th = 1.25

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('object_dist',   object_dist),
            ('target_dist',   target_dist),
            ('bonus',   (object_dist<.1) + (target_dist<.1) + (target_dist<.05)),
            ('penalty', (object_dist>far_th)),
            # Must keys
            ('sparse',  -1.0*target_dist),
            ('solved',  target_dist<.050),
            ('done',    object_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/arms/reach_base_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class ReachBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, robot_site_name, target_site_name, target_xyz_range, frame_skip, reward_mode, obs_keys, proprio_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.linalg.norm(obs_dict['reach_err'], axis=-1)
        far_th = 1.0

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach',   reach_dist),
            ('bonus',   (reach_dist<.1) + (reach_dist<.05)),
            ('penalty', (reach_dist>far_th)),
            # Must keys
            ('sparse',  -1.0*reach_dist),
            ('solved',  reach_dist<.050),
            ('done',    reach_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/claws/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def register_visual_envs(env_id, encoder_type)
```

### robohive/envs/claws/reorient_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class ReorientBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, object_site_name, target_site_name, target_xyz_range, target_euler_range, frame_skip, reward_mode, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        reach_pos_dist = np.linalg.norm(obs_dict['reach_pos_err'], axis=-1)
        reach_rot_dist = np.linalg.norm(obs_dict['reach_rot_err'], axis=-1)
        far_th = 1.0

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach_pos',   reach_pos_dist),
            ('reach_rot',   reach_rot_dist),
            ('bonus',   (reach_pos_dist<.1) + (reach_pos_dist<.05) + (reach_rot_dist<.3) + (reach_rot_dist<.1)),
            ('penalty', (reach_pos_dist>far_th)),
            # Must keys
            ('sparse',  -1.0*reach_pos_dist-1.0*reach_rot_dist),
            ('solved',  (reach_pos_dist<.050) and (reach_rot_dist<.1)),
            ('done',    reach_pos_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/env_base.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class MujocoEnv(Env, EzPickle, ObsVecDict)
    """Superclass for all MuJoCo environments."""
    def __init__(self, model_path, obsd_model_path, seed, env_credits)
    def _setup(self, obs_keys, weighted_reward_keys, proprio_keys, visual_keys, reward_mode, frame_skip, normalize_act, obs_range, rwd_viz, device_id)
    def _setup_rgb_encoders(self, visual_keys, device)
    def step(self, a)
    def forward(self)
    def forward(self)
    def forward(self)
    def _forward(self)
    def get_obs(self, update_proprioception, update_exteroception)
    def get_visuals(self, sim, visual_keys, device_id)
    def get_proprioception(self, obs_dict)
    def get_exteroception(self)
    def get_env_infos(self)
    def seed(self, seed)
    def get_input_seed(self)
    def _reset(self, reset_qpos, reset_qvel, seed)
    def reset(self, reset_qpos, reset_qvel)
    def reset(self, reset_qpos, reset_qvel)
    def reset(self, reset_qpos, reset_qvel, seed)
    def dt(self)
    def time(self)
    def id(self)
    def _horizon(self)
    def _horizon(self)
    def horizon(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)
    def compute_path_rewards(self, paths)
    def truncate_paths(self, paths)
    def evaluate_success(self, paths, logger, successful_steps)
    def mj_render(self)
    def viewer_setup(self, distance, azimuth, elevation, lookat, render_actuator, render_tendon)
    def examine_policy(self, policy, horizon, num_episodes, mode, render, camera_name, frame_size, output_dir, filename, device_id)
    def examine_policy_new(self, policy, horizon, num_episodes, mode, render, camera_name, frame_size, output_dir, filename, device_id)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)

```python
def compute_path_rewards(self, paths):
        """
        Compute vectorized rewards for paths and check for done conditions
        path has two keys: observations and actions
        path["observations"] : (num_traj, horizon, obs_dim)
        path["rewards"] should have shape (num_traj, horizon)
        """
        obs_dict = self.obsvec2obsdict(paths["observations"])
        rwd_dict = self.get_reward_dict(obs_dict)

        rewards = rwd_dict[self.rwd_mode]
        done = rwd_dict['done']
        # time align rewards. last step is redundant
        done[...,:-1] = done[...,1:]
        rewards[...,:-1] = rewards[...,1:]
        paths["done"] = done if done.shape[0] > 1 else done.ravel()
        paths["rewards"] = rewards if rewards.shape[0] > 1 else rewards.ravel()
        return paths
```

```python
def get_reward_dict(self, obs_dict):
        """
        Compute rewards dictionary
        Implement this in each subclass.
        """
        raise NotImplementedError
```
```

### robohive/envs/env_variants.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def gym_registry_specs()
def gym_registry_specs()
def gym_registry_specs()
def _update_env_spec_kwarg(env_variant_specs, variants, override_keys)
def _update_env_spec_kwarg(env_variant_specs, variants, override_keys)
def _update_env_spec_kwarg(env_variant_specs, variants, override_keys)
def _entry_point(env_variant_specs)
def _entry_point(env_variant_specs)
def _entry_point(env_variant_specs)
def _kwargs(env_variant_specs)
def _kwargs(env_variant_specs)
def _kwargs(env_variant_specs)
def update_dict(base_dict, update_dict, override_keys)
def register_env_variant(env_id, variants, variant_id, silent, override_keys)
```

### robohive/envs/fm/franka_ee_pose_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class FrankaEEPose(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, target_pose, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_target_pose(self)
    def reset(self, reset_qpos, reset_qvel)
class FrankaRobotiqPose(FrankaEEPose)
    def __init__(self, model_path, obsd_model_path, seed)
    def get_obs_dict(self, sim)
    def get_target_pose(self)

```python
def get_reward_dict(self, obs_dict):
        pose_dist = np.linalg.norm(obs_dict['pose_err'], axis=-1)
        far_th = 10

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pose',   pose_dist),
            ('bonus',   (pose_dist<1) + (pose_dist<2)),
            ('penalty', (pose_dist>far_th)),
            # Must keys
            ('sparse',  -1.0*pose_dist),
            ('solved',  pose_dist<.5),
            ('done',    pose_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/fm/franka_robotiq_data_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class FrankaRobotiqData(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, nq_arm, nq_ee, name_ee, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)

```python
def get_reward_dict(self, obs_dict):
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('none',   0.0),
            # Must keys
            ('sparse',  0.0),
            ('solved',  False),
            ('done',    False),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/hands/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def register_visual_envs(env_name, encoder_type)
```

### robohive/envs/hands/baoding_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class Task(Enum)
class BaodingFixedEnvV1(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, n_shifts_per_period, obs_keys, weighted_reward_keys)
    def step(self, a)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_pose, reset_vel, reset_goal, time_period)
    def create_goal_trajectory(self, time_step, time_period)
class BaodingRandomEnvV1(BaodingFixedEnvV1)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        # tracking error
        target1_dist = np.linalg.norm(obs_dict['target1_err'], axis=-1)
        target2_dist = np.linalg.norm(obs_dict['target2_err'], axis=-1)
        target_dist = target1_dist if self.which_task==Task.MOVE_TO_LOCATION else (target1_dist+target2_dist)
        if self.sim.model.na ==0:
            act_mag = np.array([[0]]) if obs_dict['hand_pos'].ndim==3 else 0
        else:
            act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na

        # wrist pose err (New in V1)
        hand_pos = obs_dict['hand_pos'][:,:,:3] if obs_dict['hand_pos'].ndim==3 else obs_dict['hand_pos'][:3]
        wrist_pose_err = np.linalg.norm(hand_pos*np.array([5,0.5,1]), axis=-1)
        # V0: penalize wrist angle for lifting up (positive) too much
        # wrist_threshold = 0.15
        # wrist_too_high = zeros
        # wrist_too_high[wrist_angle>wrist_threshold] = 1
        # self.reward_dict['wrist_angle'] = -10 * wrist_too_high

        # detect fall
        object1_pos = obs_dict['object1_pos'][:,:,2] if obs_dict['object1_pos'].ndim==3 else obs_dict['object1_pos'][2]
        object2_pos = obs_dict['object2_pos'][:,:,2] if obs_dict['object2_pos'].ndim==3 else obs_dict['object2_pos'][2]
        is_fall_1 = object1_pos < self.drop_height_threshold
        is_fall_2 = object2_pos < self.drop_height_threshold
        is_fall = is_fall_1 if self.which_task==Task.MOVE_TO_LOCATION else np.logical_or(is_fall_1, is_fall_2) # keep single/ both balls up

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_dist_1',      -1.*target1_dist), # V0 had only xy, V1 has xyz
            ('pos_dist_2',      -1.*target2_dist), # V0 had only xy, V1 has xyz
            ('drop_penalty',    -1.*is_fall),
            ('wrist_angle',     -1.*wrist_pose_err),    # V0 had -10 if wrist>0.15
            ('act_reg',         -1.*act_mag),
            ('bonus',           1.*(target1_dist < self.proximity_threshold)+1.*(target2_dist < self.proximity_threshold)+4.*(target1_dist < self.proximity_threshold)*(target2_dist < self.proximity_threshold)),
            # Must keys
            ('sparse',          -target_dist), # V0 had only xy, V1 has xyz
            ('solved',          (target1_dist < self.proximity_threshold)*(target2_dist < self.proximity_threshold)*(~is_fall)),
            ('done',            is_fall),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/hands/door_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class DoorEnvV0(MujocoEnv, EzPickle, ObsVecDict)
    def __init__(self)
    def step(self, a)
    def get_obs_dict(self, sim)
    def get_obs(self)
    def get_reward_dict(self, obs_dict)
    def get_env_infos(self)
    def compute_path_rewards(self, paths)
    def truncate_paths(self, paths)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)
    def mj_viewer_setup(self)
    def evaluate_success(self, paths, logger)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.linalg.norm(self.obs_dict['reach_err'], axis=-1)
        door_pos = obs_dict['door_pos'][:,:,0]
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach',   -0.1* reach_dist),
            ('open',    -0.1*(door_pos - 1.57)*(door_pos - 1.57)),
            ('bonus',   2*(door_pos > 0.2) + 8*(door_pos > 1.0) + 10*(door_pos > 1.35)),
            # Must keys
            ('sparse',  door_pos),
            ('solved',  door_pos > 1.35),
            ('done',    reach_dist > 1.0),
        ))
        rwd_dict['dense'] = np.sum([rwd_dict[key] for key in RWD_KEYS], axis=0)
        return rwd_dict
```

```python
def compute_path_rewards(self, paths):
        # path has two keys: observations and actions
        # path["observations"] : (num_traj, horizon, obs_dim)
        # path["rewards"] should have shape (num_traj, horizon)
        obs_dict = self.obsvec2obsdict(paths["observations"])
        rwd_dict = self.get_reward_dict(obs_dict)

        rewards = rwd_dict[RWD_MODE]
        done = rwd_dict['done']
        # time align rewards. last step is redundant
        done[...,:-1] = done[...,1:]
        rewards[...,:-1] = rewards[...,1:]
        paths["done"] = done if done.shape[0] > 1 else done.ravel()
        paths["rewards"] = rewards if rewards.shape[0] > 1 else rewards.ravel()
        return paths
```
```

### robohive/envs/hands/door_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class DoorEnvV1(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, reward_mode, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.linalg.norm(self.obs_dict['reach_err'], axis=-1)
        door_pos = obs_dict['door_pos'][:,:,0] if obs_dict['door_pos'].ndim==3 else obs_dict['door_pos'][0]
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach',   -0.1* reach_dist),
            ('open',    -0.1*(door_pos - 1.57)*(door_pos - 1.57)),
            ('bonus',   2*(door_pos > 0.2) + 8*(door_pos > 1.0) + 10*(door_pos > 1.35)),
            # Must keys
            ('sparse',  door_pos),
            ('solved',  door_pos > 1.35),
            ('done',    reach_dist > 1.0),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/hands/hammer_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class HammerEnvV0(MujocoEnv, EzPickle, ObsVecDict)
    def __init__(self)
    def step(self, a)
    def get_reward_dict(self, obs_dict)
    def get_obs_dict(self, sim)
    def get_obs(self)
    def get_env_infos(self)
    def compute_path_rewards(self, paths)
    def truncate_paths(self, paths)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)
    def mj_viewer_setup(self)
    def evaluate_success(self, paths, logger)

```python
def get_reward_dict(self, obs_dict):
        # get to hammer
        palm_obj_dist = np.linalg.norm(obs_dict['palm_pos'] - obs_dict['obj_pos'], axis=-1)
        # take hammer head to nail
        tool_target_dist = np.linalg.norm(obs_dict['tool_pos'] - obs_dict['target_pos'], axis=-1)
        # make nail go inside
        target_goal_dist = np.linalg.norm(obs_dict['target_pos'] - obs_dict['goal_pos'], axis=-1)
        # vel magnitude (handled differently in DAPG)
        hand_vel_mag = np.linalg.norm(obs_dict['hand_vel'], axis=-1)
        obj_vel_mag = np.linalg.norm(obs_dict['obj_vel'], axis=-1)
        # lifting tool
        lifted = (obs_dict['obj_pos'][:,:,2] > 0.04) * (obs_dict['tool_pos'][:,:,2] > 0.04)

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('palm_obj', - 0.1 * palm_obj_dist),
            ('tool_target', -1.0 * tool_target_dist),
            ('target_goal', -10.0 * target_goal_dist),
            ('smooth', -1e-2 * (hand_vel_mag + obj_vel_mag)),
            ('bonus', 2.0*lifted + 25.0*(target_goal_dist<0.020) + 75.0*(target_goal_dist<0.010)),
            # Must keys
            ('sparse',  -1.0*target_goal_dist),
            ('solved',  target_goal_dist<0.010),
            ('done',    palm_obj_dist > 1.0),
        ))
        rwd_dict['dense'] = np.sum([rwd_dict[key] for key in RWD_KEYS], axis=0)
        return rwd_dict
```

```python
def compute_path_rewards(self, paths):
        # path has two keys: observations and actions
        # path["observations"] : (num_traj, horizon, obs_dim)
        # path["rewards"] should have shape (num_traj, horizon)
        obs_dict = self.obsvec2obsdict(paths["observations"])
        rwd_dict = self.get_reward_dict(obs_dict)

        rewards = rwd_dict[RWD_MODE]
        done = rwd_dict['done']
        # time align rewards. last step is redundant
        done[...,:-1] = done[...,1:]
        rewards[...,:-1] = rewards[...,1:]
        paths["done"] = done if done.shape[0] > 1 else done.ravel()
        paths["rewards"] = rewards if rewards.shape[0] > 1 else rewards.ravel()
        return paths
```
```

### robohive/envs/hands/hammer_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class HammerEnvV1(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, reward_mode, obs_keys, weighted_reward_keys)
    def get_reward_dict(self, obs_dict)
    def get_obs_dict(self, sim)
    def reset(self, reset_qpos, reset_qvel)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def get_reward_dict(self, obs_dict):
        # get to hammer
        palm_obj_dist = np.linalg.norm(obs_dict['palm_pos'] - obs_dict['obj_pos'], axis=-1)
        # take hammer head to nail
        tool_target_dist = np.linalg.norm(obs_dict['tool_pos'] - obs_dict['target_pos'], axis=-1)
        # make nail go inside
        target_goal_dist = np.linalg.norm(obs_dict['target_pos'] - obs_dict['goal_pos'], axis=-1)
        # vel magnitude (handled differently in DAPG)
        hand_vel_mag = np.linalg.norm(obs_dict['hand_vel'], axis=-1)
        obj_vel_mag = np.linalg.norm(obs_dict['obj_vel'], axis=-1)
        # lifting tool
        obj_pos = obs_dict['obj_pos'][:,:,2] if obs_dict['obj_pos'].ndim==3 else obs_dict['obj_pos'][2]
        lifted = (obj_pos > 0.04) * (obj_pos > 0.04)

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('palm_obj', - 0.1 * palm_obj_dist),
            ('tool_target', -1.0 * tool_target_dist),
            ('target_goal', -10.0 * target_goal_dist),
            ('smooth', -1e-2 * (hand_vel_mag + obj_vel_mag)),
            ('bonus', 2.0*lifted + 25.0*(target_goal_dist<0.020) + 75.0*(target_goal_dist<0.010)),
            # Must keys
            ('sparse',  -1.0*target_goal_dist),
            ('solved',  target_goal_dist<0.010),
            ('done',    palm_obj_dist > 1.0),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/hands/pen_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class PenEnvV0(MujocoEnv, EzPickle, ObsVecDict)
    def __init__(self)
    def step(self, a)
    def get_obs_dict(self, sim)
    def get_obs(self)
    def calculate_cosine(self, vec1, vec2)
    def get_reward_dict(self, obs_dict)
    def get_env_infos(self)
    def compute_path_rewards(self, paths)
    def truncate_paths(self, paths)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)
    def mj_viewer_setup(self)
    def evaluate_success(self, paths, logger)

```python
def get_reward_dict(self, obs_dict):
        pos_err = obs_dict['obj_err_pos']
        pos_align = np.linalg.norm(pos_err, axis=-1)
        rot_align = self.calculate_cosine(obs_dict['obj_rot'], obs_dict['obj_des_rot'])
        # dropped = obs_dict['obj_pos'][:,:,2] < 0.075
        dropped = obs_dict['obj_pos'][:,:,2] < 0.075 if obs_dict['obj_pos'].ndim==3 else obs_dict['obj_pos'][2] < 0.075

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_align',   -1.0*pos_align),
            ('rot_align',   1.0*rot_align),
            ('drop',        -5.0*dropped),
            ('bonus',       10.0*(rot_align > 0.9)*(pos_align<0.075) + 50.0*(rot_align > 0.95)*(pos_align<0.075) ),
            # Must keys
            ('sparse',      -1.0*pos_align+rot_align),
            ('solved',      (rot_align > 0.95)*(~dropped)),
            ('done',        dropped),
        ))
        rwd_dict['dense'] = np.sum([rwd_dict[key] for key in RWD_KEYS], axis=0)
        return rwd_dict
```

```python
def compute_path_rewards(self, paths):
        # path has two keys: observations and actions
        # path["observations"] : (num_traj, horizon, obs_dim)
        # path["rewards"] should have shape (num_traj, horizon)
        obs_dict = self.obsvec2obsdict(paths["observations"])

        rwd_dict = self.get_reward_dict(obs_dict)

        rewards = rwd_dict[RWD_MODE]
        done = rwd_dict['done']
        # time align rewards. last step is redundant
        done[...,:-1] = done[...,1:]
        rewards[...,:-1] = rewards[...,1:]
        paths["done"] = done if done.shape[0] > 1 else done.ravel()
        paths["rewards"] = rewards if rewards.shape[0] > 1 else rewards.ravel()
        return paths
```
```

### robohive/envs/hands/pen_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class PenEnvV1(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, reward_mode, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def get_reward_dict(self, obs_dict):
        pos_err = obs_dict['obj_err_pos']
        pos_align = np.linalg.norm(pos_err, axis=-1)
        rot_align = calculate_cosine(obs_dict['obj_rot'], obs_dict['obj_des_rot'])
        # dropped = obs_dict['obj_pos'][:,:,2] < 0.075
        obj_pos = obs_dict['obj_pos'][:,:,2] if obs_dict['obj_pos'].ndim==3 else obs_dict['obj_pos'][2]
        dropped = obj_pos < 0.075

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_align',   -1.0*pos_align),
            ('rot_align',   1.0*rot_align),
            ('drop',        -5.0*dropped),
            ('bonus',       10.0*(rot_align > 0.9)*(pos_align<0.075) + 50.0*(rot_align > 0.95)*(pos_align<0.075) ),
            # Must keys
            ('sparse',      -1.0*pos_align+rot_align),
            ('solved',      (rot_align > 0.95)*(~dropped)),
            ('done',        dropped),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/hands/relocate_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class RelocateEnvV0(MujocoEnv, EzPickle, ObsVecDict)
    def __init__(self)
    def step(self, a)
    def get_rewards_old(self)
    def get_reward_dict(self, obs_dict)
    def get_obs_old(self)
    def get_obs_dict(self, sim)
    def get_obs(self)
    def get_env_infos(self)
    def compute_path_rewards(self, paths)
    def truncate_paths(self, paths)
    def reset_model(self)
    def get_env_state(self)
    def set_env_state(self, state_dict)
    def mj_viewer_setup(self)
    def evaluate_success(self, paths, logger)

```python
def get_rewards_old(self):
        obj_pos  = self.data.body_xpos[self.obj_bid].ravel()
        palm_pos = self.data.site_xpos[self.S_grasp_sid].ravel()
        target_pos = self.data.site_xpos[self.target_obj_sid].ravel()

        reward = -0.1*np.linalg.norm(palm_pos-obj_pos)              # take hand to object
        if obj_pos[2] > 0.04:                                       # if object off the table
            reward += 1.0                                           # bonus for lifting the object
            reward += -0.5*np.linalg.norm(palm_pos-target_pos)      # make hand go to target
            reward += -0.5*np.linalg.norm(obj_pos-target_pos)       # make object go to target

        if ADD_BONUS_REWARDS:
            if np.linalg.norm(obj_pos-target_pos) < 0.1:
                reward += 10.0                                          # bonus for object close to target
            if np.linalg.norm(obj_pos-target_pos) < 0.05:
                reward += 20.0                                          # bonus for object "very" close to target

        goal_achieved = True if np.linalg.norm(obj_pos-target_pos) < 0.1 else False
        return reward, goal_achieved
```

```python
def get_reward_dict(self, obs_dict):
        palm_obj_dist = np.linalg.norm(obs_dict['palm_obj_err'], axis=-1)
        palm_tar_dist = np.linalg.norm(obs_dict['palm_tar_err'], axis=-1)
        obj_tar_dist = np.linalg.norm(obs_dict['obj_tar_err'], axis=-1)
        obj_lifted = obs_dict['obj_pos'][:,:,2] > 0.04

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('palm_obj', - 0.1 * palm_obj_dist),            # take hand to object
            ('palm_tar', -0.5 * palm_tar_dist * obj_lifted),# make hand go to target
            ('obj_tar', -0.5 * obj_tar_dist * obj_lifted),  # make obj go to target
            ('bonus', 1.0*obj_lifted + 10.0*(obj_tar_dist<0.1) + 20.0*(obj_tar_dist<0.05)),
            # Must keys
            ('sparse',  -1.0*obj_tar_dist),
            ('solved',  obj_tar_dist<0.1),
            ('done',    palm_obj_dist > 0.7),
        ))
        rwd_dict['dense'] = np.sum([rwd_dict[key] for key in RWD_KEYS], axis=0)
        return rwd_dict
```

```python
def compute_path_rewards(self, paths):
        # path has two keys: observations and actions
        # path["observations"] : (num_traj, horizon, obs_dim)
        # path["rewards"] should have shape (num_traj, horizon)
        obs_dict = self.obsvec2obsdict(paths["observations"])
        rwd_dict = self.get_reward_dict(obs_dict)

        rewards = rwd_dict[RWD_MODE]
        done = rwd_dict['done']
        # time align rewards. last step is redundant
        done[...,:-1] = done[...,1:]
        rewards[...,:-1] = rewards[...,1:]
        paths["done"] = done if done.shape[0] > 1 else done.ravel()
        paths["rewards"] = rewards if rewards.shape[0] > 1 else rewards.ravel()
        return paths
```
```

### robohive/envs/hands/relocate_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class RelocateEnvV1(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, reward_mode, obs_keys, weighted_reward_keys)
    def get_rewards_old(self)
    def get_reward_dict(self, obs_dict)
    def get_obs_old(self)
    def get_obs_dict(self, sim)
    def reset(self, reset_qpos, reset_qvel)
    def get_env_state(self)
    def set_env_state(self, state_dict)

```python
def get_rewards_old(self):
        obj_pos  = self.sim.data.body_xpos[self.obj_bid].ravel()
        palm_pos = self.sim.data.site_xpos[self.S_grasp_sid].ravel()
        target_pos = self.sim.data.site_xpos[self.target_obj_sid].ravel()

        reward = -0.1*np.linalg.norm(palm_pos-obj_pos)              # take hand to object
        if obj_pos[2] > 0.04:                                       # if object off the table
            reward += 1.0                                           # bonus for lifting the object
            reward += -0.5*np.linalg.norm(palm_pos-target_pos)      # make hand go to target
            reward += -0.5*np.linalg.norm(obj_pos-target_pos)       # make object go to target

        if ADD_BONUS_REWARDS:
            if np.linalg.norm(obj_pos-target_pos) < 0.1:
                reward += 10.0                                          # bonus for object close to target
            if np.linalg.norm(obj_pos-target_pos) < 0.05:
                reward += 20.0                                          # bonus for object "very" close to target

        goal_achieved = True if np.linalg.norm(obj_pos-target_pos) < 0.1 else False
        return reward, goal_achieved
```

```python
def get_reward_dict(self, obs_dict):
        palm_obj_dist = np.linalg.norm(obs_dict['palm_obj_err'], axis=-1)
        palm_tar_dist = np.linalg.norm(obs_dict['palm_tar_err'], axis=-1)
        obj_tar_dist = np.linalg.norm(obs_dict['obj_tar_err'], axis=-1)
        obj_pos = obs_dict['obj_pos'][:,:,2] if obs_dict['obj_pos'].ndim==3 else obs_dict['obj_pos'][2]
        obj_lifted = obj_pos > 0.04

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('palm_obj', - 0.1 * palm_obj_dist),            # take hand to object
            ('palm_tar', -0.5 * palm_tar_dist * obj_lifted),# make hand go to target
            ('obj_tar', -0.5 * obj_tar_dist * obj_lifted),  # make obj go to target
            ('bonus', 1.0*obj_lifted + 10.0*(obj_tar_dist<0.1) + 20.0*(obj_tar_dist<0.05)),
            # Must keys
            ('sparse',  -1.0*obj_tar_dist),
            ('solved',  obj_tar_dist<0.1),
            ('done',    palm_obj_dist > 0.7),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/multi_task/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
```

### robohive/envs/multi_task/common/franka_appliance_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class FrankaAppliance(KitchenBase)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obj_body_randomize, robot_jnt_names)
    def reset(self, reset_qpos, reset_qvel)
```

### robohive/envs/multi_task/common/franka_kitchen_v2.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class FrankaKitchen(KitchenBase)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys_wt, robot_jnt_reset_noise_scale, robot_base_reset_range, robot_jnt_names, obj_jnt_names, obj_interaction_site)
    def reset(self, reset_qpos, reset_qvel)
```

### robohive/envs/multi_task/multi_task_base_v1.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class KitchenBase(MujocoEnv)
    def _setup(self, robot_jnt_names, obj_jnt_names, obj_interaction_site, obj_goal, robot_base_name, interact_site, obj_init, obs_keys_wt, proprio_keys_wt, weighted_reward_keys, frame_skip, obs_range, act_mode, robot_name)
    def get_dof_proximity(self, obj_dof_ranges, obj_dof_type)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def set_obj_init(self, obj_init)
    def set_obj_goal(self, obj_goal, interact_site)

```python
def get_reward_dict(self, obs_dict):
        goal_dist = np.abs(obs_dict["goal_err"])

        rwd_dict = collections.OrderedDict(
            (
                # Optional Keys
                ("obj_goal", -np.sum(goal_dist, axis=-1)),
                ("bonus",
                    1.0*np.product(goal_dist < 5 * self.obj["dof_proximity"], axis=-1)
                    # np.product(goal_dist < 0.75 * self.obj["dof_ranges"], axis=-1)
                    + 1.0*np.product(goal_dist < 1.67 * self.obj["dof_proximity"], axis=-1),
                    # + np.product(goal_dist < 0.25 * self.obj["dof_ranges"], axis=-1),
                ),
                ("pose", -np.sum(np.abs(obs_dict["pose_err"]), axis=-1)),
                ("approach", -np.linalg.norm(obs_dict["approach_err"], axis=-1)),
                # Must keys
                ("sparse", -np.sum(goal_dist, axis=-1)),
                ("solved", np.all(goal_dist < self.obj["dof_proximity"])),
                ("done", False),
            )
        )
        rwd_dict["dense"] = np.sum(
            [wt * rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0
        )

        if self.mujoco_render_frames and VIZ:
            self.dict_plot.append(rwd_dict, self.rwd_keys_wt)
            # self.dict_plot.append(rwd_dict)

        return rwd_dict
```
```

### robohive/envs/multi_task/substeps1/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
```

### robohive/envs/multi_task/substeps1/franka_kitchen.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def register_all_env_variants(task_id, task_configs, max_episode_steps, random_configs)
```

### robohive/envs/multi_task/substeps2/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
```

### robohive/envs/multi_task/substeps9/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
```

### robohive/envs/multi_task/utils/parse_demos.py

```
def viewer(env, mode, filename, frame_size, camera_id, render)
def render_demos(env, data, filename, render)
def gather_training_data(env, data, filename, render)
def main(env, demo_dir, skip, graph, save_logs, view, render)
```

### robohive/envs/myo/base_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class BaseV0(MujocoEnv)
    def _setup(self, obs_keys, weighted_reward_keys, sites, frame_skip, muscle_condition)
    def initializeConditions(self)
    def step(self, a)
```

### robohive/envs/myo/myobase/__init__.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
def register_env_with_variants(id, entry_point, max_episode_steps, kwargs)
```

### robohive/envs/myo/myobase/baoding_v1.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class Task(Enum)
class BaodingEnvV1(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, n_shifts_per_period, drop_th, proximity_th, goal_time_period, goal_xrange, goal_yrange, obs_keys, weighted_reward_keys)
    def step(self, a)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def evaluate_success(self, paths, logger, successful_steps)
    def reset(self, reset_pose, reset_vel, reset_goal, time_period)
    def create_goal_trajectory(self, time_step, time_period)

```python
def get_reward_dict(self, obs_dict):
        # tracking error
        target1_dist = np.linalg.norm(obs_dict['target1_err'], axis=-1)
        target2_dist = np.linalg.norm(obs_dict['target2_err'], axis=-1)
        target_dist = target1_dist if self.which_task==Task.MOVE_TO_LOCATION else (target1_dist+target2_dist)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0

        # wrist pose err (New in V1)
        hand_pos = obs_dict['hand_pos'][:,:,:3] if obs_dict['hand_pos'].ndim==3 else obs_dict['hand_pos'][:3]
        wrist_pose_err = np.linalg.norm(hand_pos*np.array([5,0.5,1]), axis=-1)
        # V0: penalize wrist angle for lifting up (positive) too much
        # wrist_threshold = 0.15
        # wrist_too_high = zeros
        # wrist_too_high[wrist_angle>wrist_threshold] = 1
        # self.reward_dict['wrist_angle'] = -10 * wrist_too_high

        # detect fall
        object1_pos = obs_dict['object1_pos'][:,:,2] if obs_dict['object1_pos'].ndim==3 else obs_dict['object1_pos'][2]
        object2_pos = obs_dict['object2_pos'][:,:,2] if obs_dict['object2_pos'].ndim==3 else obs_dict['object2_pos'][2]
        is_fall_1 = object1_pos < self.drop_th
        is_fall_2 = object2_pos < self.drop_th
        is_fall = is_fall_1 if self.which_task==Task.MOVE_TO_LOCATION else np.logical_or(is_fall_1, is_fall_2) # keep single/ both balls up

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_dist_1',      -1.*target1_dist), # V0 had only xy, V1 has xyz
            ('pos_dist_2',      -1.*target2_dist), # V0 had only xy, V1 has xyz
            ('drop_penalty',    -1.*is_fall),
            ('wrist_angle',     -1.*wrist_pose_err),    # V0 had -10 if wrist>0.15
            ('act_mag',         -1.*act_mag),
            ('bonus',           1.*(target1_dist < self.proximity_th)+1.*(target2_dist < self.proximity_th)+4.*(target1_dist < self.proximity_th)*(target2_dist < self.proximity_th)),
            # Must keys
            ('sparse',          -target_dist), # V0 had only xy, V1 has xyz
            ('solved',          (target1_dist < self.proximity_th)*(target2_dist < self.proximity_th)*(~is_fall)),
            ('done',            is_fall),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # Sucess Indicator
        self.sim.model.geom_rgba[self.object1_gid, :2] = np.array([1, 1]) if target1_dist < self.proximity_th else np.array([0.5, 0.5])
        self.sim.model.geom_rgba[self.object2_gid, :2] = np.array([0.9, .7]) if target1_dist < self.proximity_th else np.array([0.5, 0.5])

        return rwd_dict
```
```

### robohive/envs/myo/myobase/key_turn_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class KeyTurnEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, goal_th, obs_keys, weighted_reward_keys, key_init_range)
    def get_obs_vec(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        IF_approach_dist = np.abs(np.linalg.norm(self.obs_dict['IFtip_approach'], axis=-1)-0.030)
        TH_approach_dist = np.abs(np.linalg.norm(self.obs_dict['THtip_approach'], axis=-1)-0.030)
        key_pos = obs_dict['key_qpos'][:,:,0] if obs_dict['key_qpos'].ndim==3 else obs_dict['key_qpos'][0]
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        far_th = 0.1
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('key_turn', key_pos),
            ('IFtip_approach', -1.*IF_approach_dist),
            ('THtip_approach', -1.*TH_approach_dist),
            ('act_reg', -1.*act_mag),
            ('bonus', 1.*(key_pos>np.pi/2) + 1.*(key_pos>np.pi)),
            ('penalty', -1.*(IF_approach_dist>far_th/2)-1.*(TH_approach_dist>far_th/2) ),
            # Must keys
            ('sparse', key_pos),
            ('solved', obs_dict['key_qpos']>self.goal_th),
            ('done', (IF_approach_dist>far_th) or (TH_approach_dist>far_th)),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/myo/myobase/obj_hold_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class ObjHoldFixedEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys)
    def get_obs_vec(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
class ObjHoldRandomEnvV0(ObjHoldFixedEnvV0)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        goal_dist = np.abs(np.linalg.norm(self.obs_dict['obj_err'], axis=-1)) #-0.040)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        gaol_th = .010
        drop = goal_dist > 0.300

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('goal_dist', -1.*goal_dist),
            ('bonus', 1.*(goal_dist<2*gaol_th) + 1.*(goal_dist<gaol_th)),
            ('act_reg', -1.*act_mag),
            ('penalty', -1.*drop),
            # Must keys
            ('sparse', -goal_dist),
            ('solved', goal_dist<gaol_th),
            ('done', drop),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/myo/myobase/pen_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class PenTwirlFixedEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys)
    def get_obs_vec(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
class PenTwirlRandomEnvV0(PenTwirlFixedEnvV0)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        pos_err = obs_dict['obj_err_pos']
        pos_align = np.linalg.norm(pos_err, axis=-1)
        rot_align = calculate_cosine(obs_dict['obj_rot'], obs_dict['obj_des_rot'])
        # dropped = obs_dict['obj_pos'][:,:,2] < 0.075 if obs_dict['obj_pos'].ndim==3 else obs_dict['obj_pos'][2] < 0.075
        dropped = (pos_align > 0.075)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_align',   -1.*pos_align),
            ('rot_align',   rot_align),
            ('act_reg',     -1.*act_mag),
            ('drop',        -1.*dropped),
            ('bonus',       1.*(rot_align > 0.9)*(pos_align<0.075) + 5.0*(rot_align > 0.95)*(pos_align<0.075) ),
            # Must keys
            ('sparse',      -1.0*pos_align+rot_align),
            ('solved',      (rot_align > 0.95)*(~dropped)),
            ('done',        dropped),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/myo/myobase/pose_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class PoseEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, viz_site_targets, target_jnt_range, target_jnt_value, reset_type, target_type, obs_keys, weighted_reward_keys, pose_thd, weight_bodyname, weight_range)
    def get_obs_vec(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_target_pose(self)
    def update_target(self, restore_sim)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        pose_dist = np.linalg.norm(obs_dict['pose_err'], axis=-1)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)
        if self.sim.model.na !=0: act_mag= act_mag/self.sim.model.na
        far_th = 4*np.pi/2

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pose',    -1.*pose_dist),
            ('bonus',   1.*(pose_dist<self.pose_thd) + 1.*(pose_dist<1.5*self.pose_thd)),
            ('penalty', -1.*(pose_dist>far_th)),
            ('act_reg', -1.*act_mag),
            # Must keys
            ('sparse',  -1.0*pose_dist),
            ('solved',  pose_dist<self.pose_thd),
            ('done',    pose_dist>far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/myo/myobase/reach_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class ReachEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, target_reach_range, far_th, obs_keys, weighted_reward_keys)
    def get_obs_vec(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def generate_target_pose(self)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.linalg.norm(obs_dict['reach_err'], axis=-1)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        far_th = self.far_th*len(self.tip_sids) if np.squeeze(obs_dict['time'])>2*self.dt else np.inf
        near_th = len(self.tip_sids)*.0125
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach',   -1.*reach_dist),
            ('bonus',   1.*(reach_dist<2*near_th) + 1.*(reach_dist<near_th)),
            ('act_reg', -1.*act_mag),
            ('penalty', -1.*(reach_dist>far_th)),
            # Must keys
            ('sparse',  -1.*reach_dist),
            ('solved',  reach_dist<near_th),
            ('done',    reach_dist > far_th),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/myo/myobase/reorient_sar_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Cameron Berg (cameronberg@meta.com), Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class ProprioceptiveEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
class Geometries8EnvV0(ProprioceptiveEnvV0)
    def reset(self)
class Geometries100EnvV0(ProprioceptiveEnvV0)
    def reset(self)
class InDistribution(ProprioceptiveEnvV0)
    def reset(self)
class OutofDistribution(ProprioceptiveEnvV0)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):
        pos_err = obs_dict['obj_err_pos']
        pos_align = np.linalg.norm(pos_err, axis=-1)
        rot_align = calculate_cosine(obs_dict['obj_rot'], obs_dict['obj_des_rot'])
        dropped = (pos_align > 0.075)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pos_align',   -1.*pos_align),
            ('rot_align',   rot_align),
            ('act_reg',     -1.*act_mag),
            ('drop',        -1.*dropped),
            ('bonus',       1.*(rot_align > 0.9)*(pos_align<0.075) + 5.0*(rot_align > 0.95)*(pos_align<0.075) ),
            # Must keys
            ('sparse',      -1.0*pos_align+rot_align),
            ('solved',      (rot_align > 0.95)*(~dropped)),
            ('done',        dropped),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        if list(self.sim.model.site_rgba[self.success_indicator_sid, :2]) != [0.0, 2.0]:
            self.sim.model.site_rgba[self.success_indicator_sid, :2] = np.array([0, 2]) if rwd_dict['solved'] else np.array([2, 0])
        return rwd_dict
```
```

### robohive/envs/myo/myobase/walk_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com), Pierre Schumacher (schumacherpier@gmail.com), Cameron Berg (cam.h.berg@gmail.com)
================================================= """
class ReachEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, target_reach_range, joint_random_range, far_th, obs_keys, weighted_reward_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def generate_targets(self)
    def generate_qpos(self)
    def reset(self)
class WalkEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys, min_height, max_rot, hip_period, reset_type, target_x_vel, target_y_vel, target_rot)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_randomized_initial_state(self)
    def step(self)
    def reset(self)
    def muscle_lengths(self)
    def muscle_forces(self)
    def muscle_velocities(self)
    def _get_done(self)
    def _get_joint_angle_rew(self, joint_names)
    def _get_feet_heights(self)
    def _get_feet_relative_position(self)
    def _get_vel_reward(self)
    def _get_cyclic_rew(self)
    def _get_ref_rotation_rew(self)
    def _get_torso_angle(self)
    def _get_com_velocity(self)
    def _get_height(self)
    def _get_rot_condition(self)
    def _get_com(self)
    def _get_angle(self, names)
class TerrainEnvV0(WalkEnvV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys, min_height, max_rot, hip_period, reset_type, target_x_vel, target_y_vel, target_rot, terrain, variant)
    def reset(self)
    def _get_done(self)
    def _get_knee_condition(self)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.linalg.norm(obs_dict['reach_err'], axis=-1)
        vel_dist = np.linalg.norm(obs_dict['qvel'], axis=-1)
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        far_th = self.far_th*len(self.tip_sids) if np.squeeze(obs_dict['time'])>2*self.dt else np.inf
        # near_th = len(self.tip_sids)*.0125
        near_th = len(self.tip_sids)*.050
        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('reach',   10.-1.*reach_dist -10.*vel_dist),
            ('bonus',   1.*(reach_dist<2*near_th) + 1.*(reach_dist<near_th)),
            ('act_reg', -100.*act_mag),
            ('penalty', -1.*(reach_dist>far_th)),
            # Must keys
            ('sparse',  -1.*reach_dist),
            ('solved',  reach_dist<near_th),
            ('done',    reach_dist > far_th),
        ))
        # print(f"reach_dist:{reach_dist}, far_th:{far_th}")
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```

```python
def get_reward_dict(self, obs_dict):
        vel_reward = self._get_vel_reward()
        cyclic_hip = self._get_cyclic_rew()
        ref_rot = self._get_ref_rotation_rew()
        joint_angle_rew = self._get_joint_angle_rew(['hip_adduction_l', 'hip_adduction_r', 'hip_rotation_l',
                                                       'hip_rotation_r'])
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('vel_reward', vel_reward),
            ('cyclic_hip',  cyclic_hip),
            ('ref_rot',  ref_rot),
            ('joint_angle_rew', joint_angle_rew),
            ('act_mag', act_mag),
            # Must keys
            ('sparse',  vel_reward),
            ('solved',    vel_reward >= 1.0),
            ('done',  self._get_done()),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```

```python
def _get_vel_reward(self):
        """
        Gaussian that incentivizes a walking velocity. Going
        over only achieves flat rewards.
        """
        vel = self._get_com_velocity()
        return np.exp(-np.square(self.target_y_vel - vel[1])) + np.exp(-np.square(self.target_x_vel - vel[0]))
```
```

### robohive/envs/myo/myochallenge/baoding_v1.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class Task(Enum)
class BaodingEnvV1(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, frame_skip, drop_th, proximity_th, goal_time_period, goal_xrange, goal_yrange, obj_size_range, obj_mass_range, obj_friction_change, task_choice, obs_keys, weighted_reward_keys)
    def step(self, a)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def evaluate_success(self, paths, logger, successful_steps)
    def get_metrics(self, paths)
    def reset(self, reset_pose, reset_vel, reset_goal, time_period)
    def create_goal_trajectory(self, time_step, time_period)

```python
def get_reward_dict(self, obs_dict):
        # tracking error
        target1_dist = np.linalg.norm(obs_dict['target1_err'], axis=-1)
        target2_dist = np.linalg.norm(obs_dict['target2_err'], axis=-1)
        target_dist = target1_dist+target2_dist
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)
        if self.sim.model.na !=0: act_mag= act_mag/self.sim.model.na


        # detect fall
        object1_pos = obs_dict['object1_pos'][:,:,2] if obs_dict['object1_pos'].ndim==3 else obs_dict['object1_pos'][2]
        object2_pos = obs_dict['object2_pos'][:,:,2] if obs_dict['object2_pos'].ndim==3 else obs_dict['object2_pos'][2]
        is_fall_1 = object1_pos < self.drop_th
        is_fall_2 = object2_pos < self.drop_th
        is_fall = np.logical_or(is_fall_1, is_fall_2) # keep both balls up

        rwd_dict = collections.OrderedDict((
            # Perform reward tuning here --
            # Update Optional Keys section below
            # Update reward keys (DEFAULT_RWD_KEYS_AND_WEIGHTS) accordingly to update final rewards
            # Examples: Env comes pre-packaged with two keys pos_dist_1 and pos_dist_2

            # Optional Keys
            ('pos_dist_1',      -1.*target1_dist),
            ('pos_dist_2',      -1.*target2_dist),
            # Must keys
            ('act_reg',         -1.*act_mag),
            ('sparse',          -target_dist),
            ('solved',          (target1_dist < self.proximity_th)*(target2_dist < self.proximity_th)*(~is_fall)),
            ('done',            is_fall),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # Sucess Indicator
        self.sim.model.geom_rgba[self.object1_gid, :2] = np.array([1, 1]) if target1_dist < self.proximity_th else np.array([0.5, 0.5])
        self.sim.model.geom_rgba[self.object2_gid, :2] = np.array([0.9, .7]) if target1_dist < self.proximity_th else np.array([0.5, 0.5])

        return rwd_dict
```
```

### robohive/envs/myo/myochallenge/chasetag_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com), Pierre Schumacher (schumacherpier@gmail.com), Chun Kwang Tan (cktan.neumove@gmail.com)
================================================= """
class TerrainTypes(Enum)
class SpecialTerrains(Enum)
class Task(Enum)
class ChallengeOpponent()
    """Training Opponent for the Locomotion Track of the MyoChallenge 2023.
Contains several different policies. For the final evaluation, an additional
non-disclosed policy will be used."""
    def __init__(self, sim, rng, probabilities, min_spawn_distance, chase_vel_range, random_vel_range, dt)
    def reset_noise_process(self)
    def get_opponent_pose(self)
    def set_opponent_pose(self, pose)
    def move_opponent(self, vel)
    def random_movement(self)
    def sample_opponent_policy(self)
    def update_opponent_state(self)
    def reset_opponent(self, player_task, rng)
    def chase_player(self)
class HeightField()
    def __init__(self, sim, rng, hills_range, rough_range, relief_range, patches_per_side, real_length, view_distance)
    def flatten_agent_patch(self, qpos)
    def _compute_patch_data(self, terrain_type)
    def _populate_patches(self)
    def _fill_patch(self, i, j, terrain_type)
    def get_heightmap_obs(self)
    def cart2map(self, points_1, points_2)
    def sample(self, rng)
    def _compute_rough_terrain(self)
    def _compute_relief_terrain(self)
    def _compute_hilly_terrain(self)
    def _init_height_points(self)
    def _measure_height(self)
    def size(self)
    def nrow(self)
    def ncol(self)
class RepellerChallengeOpponent(ChallengeOpponent)
    def __init__(self, sim, rng, probabilities, min_spawn_distance, chase_vel_range, random_vel_range, repeller_vel_range, dt)
    def get_agent_pos(self)
    def get_wall_pos(self)
    def get_repellers(self)
    def repeller_stochastic(self)
    def _calc_angular_vel(self, current_pos, desired_pos)
    def repeller_policy(self)
    def sample_opponent_policy(self)
    def update_opponent_state(self)
class ChaseTagEnvV0(WalkEnvV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys, reset_type, win_distance, min_spawn_distance, task_choice, terrain, hills_range, rough_range, relief_range, repeller_opponent, chase_vel_range, random_vel_range, repeller_vel_range, opponent_probabilities)
    def assert_settings(self)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_metrics(self, paths)
    def step(self)
    def reset(self)
    def _maybe_flatten_agent_patch(self, qpos)
    def _sample_task(self)
    def _maybe_sample_terrain(self)
    def _randomize_position_orientation(self, qpos, qvel)
    def _get_reset_state(self)
    def _maybe_adjust_height(self, qpos, qvel)
    def viewer_setup(self)
    def _get_randomized_initial_state(self)
    def _setup_convenience_vars(self)
    def _get_done(self)
    def _win_condition(self)
    def _lose_condition(self)
    def _chase_lose_condition(self)
    def _evade_lose_condition(self)
    def _chase_win_condition(self)
    def _evade_win_condition(self)
    def _get_body_mass(self)
    def _get_score(self, time)
    def _get_muscle_lengthRange(self)
    def _get_tendon_lengthspring(self)
    def _get_muscle_operating_length(self)
    def _get_muscle_fmax(self)
    def _get_grf(self)
    def _get_pelvis_angle(self)
    def _get_joint_names(self)
    def _get_actuator_names(self)
    def _get_fallen_condition(self)

```python
def get_reward_dict(self, obs_dict):
        """
        Rewards are computed from here, using the <self.weighted_reward_keys>.
        These weights can either be set in this file in the
        DEFAULT_RWD_KEYS_AND_WEIGHTS dict, or when registering the environment
        with gym.register in myochallenge/__init__.py
        """
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0

        # The task is entirely defined by these 3 lines
        win_cdt = self._win_condition()
        lose_cdt = self._lose_condition()
        if self.current_task.name == 'CHASE':
            score = self._get_score(float(self.obs_dict['time'])) if win_cdt else 0
            self.obs_dict['time'] = self.maxTime if lose_cdt else self.obs_dict['time']
        elif self.current_task.name == 'EVADE':
            score = self._get_score(float(self.obs_dict['time'])) if (win_cdt or lose_cdt) else 0
        # ----------------------

        # Example reward, you should change this!
        distance = np.linalg.norm(obs_dict['model_root_pos'][...,:2] - obs_dict['opponent_pose'][...,:2])

        rwd_dict = collections.OrderedDict((
            # Perform reward tuning here --
            # Update Optional Keys section below
            # Update reward keys (DEFAULT_RWD_KEYS_AND_WEIGHTS) accordingly to update final rewards

            # Example: simple distance function

                # Optional Keys
                ('act_reg', act_mag),
                ('distance', distance),
                ('lose', lose_cdt),
                # Must keys
                ('sparse',  score),
                ('solved',  win_cdt),
                ('done',  self._get_done()),
            ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # Success Indicator
        self.sim.model.site_rgba[self.success_indicator_sid, :] = np.array([0, 2, 0, 0.2]) if rwd_dict['solved'] else np.array([2, 0, 0, 0])
        return rwd_dict
```
```

### robohive/envs/myo/myochallenge/relocate_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class RelocateEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, target_xyz_range, target_rxryrz_range, obj_xyz_range, obj_geom_range, obj_mass_range, obj_friction_range, qpos_noise_range, obs_keys, weighted_reward_keys, pos_th, rot_th, drop_th)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_metrics(self, paths, successful_steps)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        reach_dist = np.abs(np.linalg.norm(self.obs_dict['reach_err'], axis=-1))
        pos_dist = np.abs(np.linalg.norm(self.obs_dict['pos_err'], axis=-1))
        rot_dist = np.abs(np.linalg.norm(self.obs_dict['rot_err'], axis=-1))
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        drop = reach_dist > self.drop_th
        rwd_dict = collections.OrderedDict((
            # Perform reward tuning here --
            # Update Optional Keys section below
            # Update reward keys (DEFAULT_RWD_KEYS_AND_WEIGHTS) accordingly to update final rewards
            # Examples: Env comes pre-packaged with two keys pos_dist and rot_dist
            # Optional Keys
            ('pos_dist', -1.*pos_dist),
            ('rot_dist', -1.*rot_dist),
            # Must keys
            ('act_reg', -1.*act_mag),
            ('sparse', -rot_dist-10.0*pos_dist),
            ('solved', (pos_dist<self.pos_th) and (rot_dist<self.rot_th) and (not drop) ),
            ('done', drop),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # Success Indicator
        self.sim.model.site_rgba[self.success_indicator_sid, :2] = np.array([0, 2]) if rwd_dict['solved'] else np.array([2, 0])
        self.sim.model.site_size[self.success_indicator_sid, :] = np.array([.25,]) if rwd_dict['solved'] else np.array([0.1,])
        return rwd_dict
```
```

### robohive/envs/myo/myochallenge/reorient_v0.py

```
"""=================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """
class ReorientEnvV0(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, obs_keys, weighted_reward_keys, goal_pos, goal_rot, obj_size_change, obj_mass_range, obj_friction_change, pos_th, rot_th, drop_th)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def get_metrics(self, paths, successful_steps)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        pos_dist = np.abs(np.linalg.norm(self.obs_dict['pos_err'], axis=-1))
        rot_dist = np.abs(np.linalg.norm(self.obs_dict['rot_err'], axis=-1))
        act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        drop = pos_dist > self.drop_th

        rwd_dict = collections.OrderedDict((
            # Perform reward tuning here --
            # Update Optional Keys section below
            # Update reward keys (DEFAULT_RWD_KEYS_AND_WEIGHTS) accordingly to update final rewards
            # Examples: Env comes pre-packaged with two keys pos_dist and rot_dist

            # Optional Keys
            ('pos_dist', -1.*pos_dist),
            ('rot_dist', -1.*rot_dist),
            ('bonus', 1.*(pos_dist<2*self.pos_th) + 1.*(pos_dist<self.pos_th)),
            ('act_reg', -1.*act_mag),
            ('penalty', -1.*drop),
            # Must keys
            ('sparse', -rot_dist-10.0*pos_dist),
            ('solved', (pos_dist<self.pos_th) and (rot_dist<self.rot_th) and (not drop) ),
            ('done', drop),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # Sucess Indicator
        self.sim.model.site_rgba[self.success_indicator_sid, :2] = np.array([0, 2]) if rwd_dict['solved'] else np.array([2, 0])
        return rwd_dict
```
```

### robohive/envs/myo/myodm/__init__.py

```
def register_myohand_object_trackref(task_name, object_name, motion_path)
def register_MyoHand_object(object_name)
```

### robohive/envs/myo/myodm/myodm_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com), Sudeep Dasari (sdasari@andrew.cmu.edu), Vittorio Caggiano (caggiano@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASI"""
class TrackEnv(BaseV0)
    def __init__(self, object_name, model_path, obsd_model_path, seed)
    def _setup(self, reference, motion_start_time, motion_extrapolation, obs_keys, weighted_reward_keys, Termimate_obj_fail, Termimate_pose_fail)
    def rotation_distance(self, q1, q2, euler)
    def update_reference_insim(self, curr_ref)
    def norm2(self, x)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def qpos_from_robot_object(self, qpos, robot, object)
    def playback(self)
    def reset(self)
    def check_termination(self, obs_dict)

```python
def get_reward_dict(self, obs_dict):
        # get targets from reference object
        tgt_obj_com = obs_dict['targ_obj_com'].flatten()
        tgt_obj_rot = obs_dict['targ_obj_rot'].flatten()

        # get real values from physics object
        obj_com = obs_dict['curr_obj_com'].flatten()
        obj_rot = obs_dict['curr_obj_rot'].flatten()

        # calculate both object "matching"
        obj_com_err = np.sqrt(self.norm2(tgt_obj_com - obj_com))
        obj_rot_err = self.rotation_distance(obj_rot, tgt_obj_rot, False) / np.pi
        obj_reward = np.exp(-self.obj_err_scale * (obj_com_err + 0.1 * obj_rot_err))

        # calculate lift bonus
        lift_bonus = (tgt_obj_com[2] >= self._lift_z) and (obj_com[2] >= self._lift_z)

        # reward = obj_reward + self.lift_bonus_mag * float(lift_bonus)

        # calculate reward terms
        qpos_reward = np.exp(-self.qpos_err_scale * self.norm2(obs_dict['hand_qpos_err']))
        qvel_reward = np.array([0]) if obs_dict['hand_qvel_err'] is None else np.exp(-self.qvel_err_scale * self.norm2(obs_dict['hand_qvel_err']))


        # weight and sum individual reward terms
        pose_reward  = self.qpos_reward_weight * qpos_reward
        vel_reward   = self.qvel_reward_weight * qvel_reward

        # print(f"Time: {obs_dict['time']} Error Pose: {self.norm2(obs_dict['hand_qpos_err'])} {obs_dict['hand_qpos_err']}    Error Obj:{obs_dict['obj_com_err']}")

        base_error = np.sqrt(self.norm2(obs_dict['base_error'] ))
        base_reward = np.exp(-self.base_err_scale * base_error)

        # print(base_error, base_reward)

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pose',   float(pose_reward+vel_reward)),
            ('object' , float(obj_reward+base_reward)),
            ('bonus',  self.lift_bonus_mag * float(lift_bonus)),
            ('penalty', float(self.check_termination(obs_dict))),
            # Must keys
            ('sparse',  0),
            ('solved',  0),
            ('done',    self.initialized_pos and self.check_termination(obs_dict)),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # print(rwd_dict['dense'], obj_com_err,rwd_dict['done'],rwd_dict['sparse'])
        return rwd_dict
```
```

### robohive/envs/myo/myomimic/__init__.py

```
def register_myoleg_trackref(task_name, robot_name, object_name, motion_path)
```

### robohive/envs/myo/myomimic/myomimic_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com), Sudeep Dasari (sdasari@andrew.cmu.edu), Vittorio Caggiano (caggiano@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASI"""
class TrackEnv(BaseV0)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, reference, motion_start_time, motion_extrapolation, obs_keys, weighted_reward_keys, Termimate_obj_fail, Termimate_pose_fail)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def qpos_from_robot_object(self, qpos, robot)
    def playback(self)
    def reset(self)

```python
def get_reward_dict(self, obs_dict):

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pose',   1.0),
            ('bonus',  1.0),
            ('penalty', 1.0),
            # Must keys
            ('sparse',  0),
            ('solved',  0),
            ('done',    False),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # print(rwd_dict['dense'], obj_com_err,rwd_dict['done'],rwd_dict['sparse'])
        return rwd_dict
```
```

### robohive/envs/obs_vec_dict.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class ObsVecDict()
    """Class to help with conversion between obs_dict <> obs_vector
Requirements:
    - obs_dict must have key 'time' with observation timestamp
    - initialize() must be called if 'ordered_obs_keys' changes post initialization"""
    def __init__(self, obsvec_cachesize)
    def add_obsvec_to_cache(self, t, obsvec, check_timeStamps)
    def get_obsvec_from_cache(self, index)
    def obsvec_cache_flush(self, t, obsvec)
    def initialize(self, obs_dict, ordered_obs_keys)
    def squeeze_dims(self, obs_dict)
    def expand_dims(self, obs_dict)
    def obsdict2obsvec(self, obs_dict, ordered_obs_keys)
    def obsvec2obsdict(self, obsvec)
```

### robohive/envs/quadrupeds/orient_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class OrientBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, dof_range_names, act_range_names, upright_threshold, torso_site_name, target_site_name, heading_site_name, target_distance_range, target_angle_range, target_height_range, frame_skip, obs_keys, weighted_reward_keys, proprio_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        """Returns the reward for the given action and observation."""
        target_xy_dist = np.linalg.norm(obs_dict['target_error'], axis=-1)
        heading = obs_dict['heading'][:,:,0] if obs_dict['heading'].ndim==3 else obs_dict['heading'][0]
        upright = obs_dict['upright'][:,:,0] if obs_dict['upright'].ndim==3 else obs_dict['upright'][0]
        quad_height = obs_dict['root_pos'][:,:,2] if obs_dict['root_pos'].ndim==3 else obs_dict['root_pos'][2]

        target_height_th = np.mean(self.target_height_range)

        rwd_dict = collections.OrderedDict((
            # Reward for proximity to the target.
            ('target_dist_cost', -1.0 * target_xy_dist),
            # staying upright
            ('upright', (upright - self._upright_threshold)),
            # not falling
            ('falling', -1.0* (upright < self._upright_threshold)),
            # Heading - 1 @ cos(0) to 0 @ cos(25deg).
            # ('heading', (heading - 0.9) / 0.1),
            ('heading', (heading + 1.0)),
            # height
            ('height', -1.*abs(quad_height-target_height_th)),
            # Bonus when mean error < 15deg or upright within 15deg.
            ('bonus_small', 1.0*(upright > self._upright_threshold) + 1.0*(heading > 0.9)),
            # Bonus when mean error < 5deg or upright within 5deg.
            ('bonus_big', 1.0 * (upright > self._upright_threshold) * (heading > 0.996)),
            # Must keys
            ('sparse',  heading),
            ('solved',  (upright > self._upright_threshold) * (heading > 0.996)),
            ('done',    upright < self._upright_threshold),
        ))

        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/quadrupeds/stand_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class StandBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, dof_range_names, act_range_names, upright_threshold, torso_site_name, target_site_name, heading_site_name, target_distance_range, target_angle_range, target_height_range, frame_skip, obs_keys, weighted_reward_keys, reset_type, proprio_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        """Returns the reward for the given action and observation."""

        pose_mean_error = np.abs(obs_dict['pose_error']).mean(axis=-1)
        upright = obs_dict['upright'][:,:,0] if obs_dict['upright'].ndim==3 else obs_dict['upright'][0]
        center_dist = np.linalg.norm(obs_dict['root_pos'][:2], axis=-1)

        rwd_dict = collections.OrderedDict((
            # staying upright
            ('upright', (upright - self._upright_threshold)/(1 - self._upright_threshold)),
            # not falling
            ('falling', -1.0* (upright < self._upright_threshold)),
            # Reward for closeness to desired pose.
            ('pose_error_cost', -1 * pose_mean_error),
            # Reward for closeness to center; i.e. being stationary.
            ('center_distance_cost', -1 * center_dist),
            # Bonus when mean error < 30deg, scaled by uprightedness.
            ('bonus_small', 1.0 * (pose_mean_error < (np.pi / 6)) * upright),
            # Bonus when mean error < 15deg and upright within 30deg.
            ('bonus_big', 1.0 * (pose_mean_error < (np.pi / 12)) * (upright > 0.9)),
            # Must keys
            ('sparse', (1 - np.maximum(pose_mean_error / (np.pi / 3), 1))),  # Normalized pose error by 60deg.
            ('solved', (pose_mean_error < (np.pi / 12)) * (upright > 0.9)),
            ('done', upright < self._upright_threshold),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/quadrupeds/walk_v0.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class WalkBaseV0(MujocoEnv)
    def __init__(self, model_path, obsd_model_path, seed)
    def _setup(self, dof_range_names, act_range_names, upright_threshold, torso_site_name, target_site_name, heading_site_name, target_distance_range, target_angle_range, target_height_range, frame_skip, obs_keys, weighted_reward_keys, proprio_keys)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def reset(self, reset_qpos, reset_qvel)

```python
def get_reward_dict(self, obs_dict):
        """Returns the reward for the given action and observation."""
        target_xy_dist = np.linalg.norm(obs_dict['target_error'], axis=-1)
        heading = obs_dict['heading'][:,:,0] if obs_dict['heading'].ndim==3 else obs_dict['heading'][0]
        upright = obs_dict['upright'][:,:,0] if obs_dict['upright'].ndim==3 else obs_dict['upright'][0]
        quad_height = obs_dict['root_pos'][:,:,2] if obs_dict['root_pos'].ndim==3 else obs_dict['root_pos'][2]

        target_distance_th = np.mean(self.target_distance_range)
        target_height_th = np.mean(self.target_height_range)

        rwd_dict = collections.OrderedDict((
            # Reward for proximity to the target.
            ('target_dist_cost', -1.0 * target_xy_dist),
            # staying upright
            ('upright', (upright - self._upright_threshold)),
            # not falling
            ('falling', -1.0* (upright < self._upright_threshold)),
            # Heading - 1 @ cos(0) to 0 @ cos(25deg).
            ('heading', (heading - 0.9) / 0.1),
            # height
            ('height', -1.*abs(quad_height-target_height_th)),
            # Bonus
            ('bonus_small', 1.0*(target_xy_dist < 0.75*target_distance_th) + 1.0*(heading > 0.9)),
            ('bonus_big', 1.0 * (target_xy_dist < 0.5*target_distance_th) * (heading > 0.9)),
            # Must keys
            ('sparse',  -1.0*target_xy_dist),
            ('solved',  (target_xy_dist < 0.5)),
            ('done',    upright < self._upright_threshold),
        ))

        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        return rwd_dict
```
```

### robohive/envs/tcdm/__init__.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com), Sudeep Dasari (sdasari@andrew.cmu.edu )
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF """
def register_adroit_object_trackref(task_name, object_name, motion_path)
def register_Adroit_object(object_name)
def register_Franka_object(object_name, data_path)
```

### robohive/envs/tcdm/mocap_utils.py

```
def _lerp(l, v1, v2)
def _affine(X, old_origin, new_origin, R)
def _obj_axis_to_quat(axis, global_rot)
def _calc_start_pos(physics, object_name, rot_0, global_rot)
def interpolate_traj(pos, ori, substeps)
class MoCapTask(Task)
    def __init__(self, mocap_controller, save_filename, length, input_name)
    def action_spec(self, _)
    def initialize_episode(self, physics)
    def before_step(self, action, physics)
    def after_step(self, physics)
    def get_observation(self, physics)
    def get_reward(self, _)
    def get_frame(self)
    def get_termination(self, _)
    def get_info_from_physics(self, physics)
def get_body_poses(physics)
class MoCapController(object)
    def __init__(self, human_motion_file, physics, object_name, start_t, end_t, out_len)
    def _init_base_robot_pose(self, physics, hand_joints)
    def _fk(self, base_translation, joint_angles)
    def set_mocap(self, physics, time)
    def T(self)
    def q0(self)
    def object_name(self)
def to_quat(arr)
def rotation_distance(q1, q2)
def root_to_point(root_pos, root_rotation, point)
def to_transform_mat(R, t)
def axis_angle_to_rot(axis_angle)

```python
def get_observation(self, physics):
        """Returns dummy obs and appends state vector to saver"""
        # self._saver.append_from_physics(physics)
        self._saver.append(self.get_info_from_physics(physics))
        obs = collections.OrderedDict()
        obs['position'] = physics.data.qpos.astype(np.float32).copy()
        obs['velocity'] = physics.data.qvel.astype(np.float32).copy()
        return obs
```

```python
def get_reward(self, _):
        # return a dummy reward
        return 0
```
```

### robohive/envs/tcdm/track.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com), Sudeep Dasari (sdasari@andrew.cmu.edu )
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF """
class TrackEnv(MujocoEnv)
    def __init__(self, object_name, model_path, obsd_model_path, seed)
    def _setup(self, reference, motion_start_time, motion_extrapolation, obs_keys, weighted_reward_keys, Termimate_obj_fail, Termimate_pose_fail)
    def rotation_distance(self, q1, q2, euler)
    def update_reference_insim(self, curr_ref)
    def norm2(self, x)
    def get_obs_dict(self, sim)
    def get_reward_dict(self, obs_dict)
    def qpos_from_robot_object(self, qpos, robot, object)
    def playback(self)
    def reset(self)
    def check_termination(self, obs_dict)

```python
def get_reward_dict(self, obs_dict):
        # get targets from reference object
        tgt_obj_com = obs_dict['targ_obj_com'].flatten()
        tgt_obj_rot = obs_dict['targ_obj_rot'].flatten()

        # get real values from physics object
        obj_com = obs_dict['curr_obj_com'].flatten()
        obj_rot = obs_dict['curr_obj_rot'].flatten()

        # calculate both object "matching"
        obj_com_err = np.sqrt(self.norm2(tgt_obj_com - obj_com))
        obj_rot_err = self.rotation_distance(obj_rot, tgt_obj_rot, False) / np.pi
        obj_reward = np.exp(-self.obj_err_scale * (obj_com_err + 0.1 * obj_rot_err))

        # calculate lift bonus
        lift_bonus = (tgt_obj_com[2] >= self._lift_z) and (obj_com[2] >= self._lift_z)

        # reward = obj_reward + self.lift_bonus_mag * float(lift_bonus)

        # calculate reward terms
        qpos_reward = np.exp(-self.qpos_err_scale * self.norm2(obs_dict['hand_qpos_err']))
        qvel_reward = np.array([0]) if obs_dict['hand_qvel_err'] is None else np.exp(-self.qvel_err_scale * self.norm2(obs_dict['hand_qvel_err']))


        # weight and sum individual reward terms
        pose_reward  = self.qpos_reward_weight * qpos_reward
        vel_reward   = self.qvel_reward_weight * qvel_reward

        # print(f"Time: {obs_dict['time']} Error Pose: {self.norm2(obs_dict['hand_qpos_err'])} {obs_dict['hand_qpos_err']}    Error Obj:{obs_dict['obj_com_err']}")

        base_error = np.sqrt(self.norm2(obs_dict['base_error'] ))
        base_reward = np.exp(-self.base_err_scale * base_error)

        # print(base_error, base_reward)

        rwd_dict = collections.OrderedDict((
            # Optional Keys
            ('pose',   float(pose_reward+vel_reward)),
            ('object' , float(obj_reward+base_reward)),
            ('bonus',  self.lift_bonus_mag * float(lift_bonus)),
            ('penalty', float(self.check_termination(obs_dict))),
            # Must keys
            ('sparse',  0),
            ('solved',  0),
            ('done',    self.initialized_pos and self.check_termination(obs_dict)),
        ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)

        # print(rwd_dict['dense'], obj_com_err,rwd_dict['done'],rwd_dict['sparse'])
        return rwd_dict
```
```

### robohive/physics/mj_sim_scene.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar, Copyright (C) 2019 The ROBEL Authors
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY"""
class DMSimScene(SimScene)
    """Encapsulates a MuJoCo robotics simulation using dm_control."""
    def _load_simulation(self, model_handle)
    def advance(self, substeps, render)
    def _create_renderer(self, sim)
    def copy_model(self)
    def save_binary(self, path)
    def upload_height_field(self, hfield_id)
    def get_mjlib(self)
    def get_handle(self, value)
    def _patch_mjmodel_accessors(self, model)
    def _patch_mjdata_accessors(self, data)
```

### robohive/physics/mjpy_sim_scene.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar, Copyright (C) 2019 The ROBEL Authors
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY"""
def _mj_warning_fn(warn_data)
class MjPySimScene(SimScene)
    """Encapsulates a MuJoCo robotics simulation using mujoco_py."""
    def _load_simulation(self, model_handle)
    def _create_renderer(self, sim)
    def copy_model(self)
    def save_binary(self, path)
    def upload_height_field(self, hfield_id)
    def _patch_mjlib_accessors(self, lib)
    def get_mjlib(self)
    def get_handle(self, value)
    def advance(self, substeps, render)
class _MjlibWrapper()
    """Wrapper that forwards mjlib calls."""
    def __init__(self, lib)
    def __getattr__(self, name)
```

### robohive/physics/sim_scene.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar, Copyright (C) 2019 The ROBEL Authors
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY"""
class SimBackend(Enum)
    """Simulation library types."""
    def get_sim_backend()
class SimScene()
    """Encapsulates a MuJoCo robotics simulation."""
    def create()
    def get_sim(model_handle)
    def __init__(self, model_handle)
    def step_duration(self)
    def close(self)
    def forward(self)
    def reset(self)
    def disable_option(self, constraint_solver, limits, contact, gravity, clamp_ctrl, actuation)
    def get_state(self)
    def set_state(self, time, qpos, qvel, act)
    def disable_option_context(self)
    def copy_model(self)
    def save_binary(self, path)
    def upload_height_field(self, hfield_id)
    def get_handle(self, value)
    def get_mjlib(self)
    def _load_simulation(self, model_handle)
    def _create_renderer(self, sim)
    def advance(self, substeps, render)
```

### robohive/physics/sim_scene_test.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar, Copyright (C) 2019 The ROBEL Authors
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY"""
def test_model_file()
def mjpy_and_dm(fn)
class SimSceneTest(TestCase)
    """Unit test class for SimScene."""
    def test_load(self, robot)
    def test_step(self, robot)
    def test_accessors(self, robot)
    def test_copy_model(self, robot)
```

### robohive/tests/test_envs.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
def assert_close(prm1, prm2, atol, rtol)
class TestEnvs(TestCase)
    def check_envs(self, module_name, env_names, lite, input_seed)
    def check_env(self, environment_id, input_seed)
    def check_old_envs(self, module_name, env_names, lite, seed)
```

### robohive/tests/test_examine_env.py

```
class TestExamineEnv(TestCase)
    def delete_recent_file(self, filename_pattern, directory, age)
    def test_main(self)
    def test_offscreen_rendering(self)
    def test_paths_plotting(self)
    def no_test_scripted_policy_loading(self)
```

### robohive/tests/test_hands.py

```
class TestHMS(TestEnvs)
    def test_hand_manipulation_suite(self)
```

### robohive/tests/test_multitask.py

```
class TestKitchen(TestEnvs)
    def test_envs(self)
```

### robohive/utils/examine_env.py

```
"""=================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See """
class rand_policy()
    def __init__(self, env, seed)
    def get_action(self, obs)
def load_class_from_str(module_name, class_name)
def main(env_name, policy_path, mode, seed, num_episodes, render, camera_name, output_dir, output_name, save_paths, plot_paths, render_visuals, env_args)
```

### robohive/utils/examine_sim.py

```
def main(sim_path, qpos, ctrl, horizon)
```