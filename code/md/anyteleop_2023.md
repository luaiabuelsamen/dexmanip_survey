# anyteleop_2023

source: https://github.com/dexsuite/dex-retargeting


commit: 3f56141bc8bd2760d5e452e382937269554ebb21


## README

<div align="center">
  <h1 align="center"> Dex Retargeting </h1>
  <h3 align="center">
    Various retargeting optimizers to translate human hand motion to robot hand motion.
  </h3>
</div>
<p align="center">
  <!-- code check badges -->
  <a href='https://github.com/dexsuite/dex-retargeting/blob/main/.github/workflows/test.yml'>
      <img src='https://github.com/dexsuite/dex-retargeting/actions/workflows/test.yml/badge.svg' alt='Test Status' />
  </a>
  <!-- issue badge -->
  <a href="https://github.com/dexsuite/dex-retargeting/issues">
  <img src="https://img.shields.io/github/issues-closed/dexsuite/dex-retargeting.svg" alt="Issues Closed">
  </a>
  <a href="https://github.com/dexsuite/dex-retargeting/issues?q=is%3Aissue+is%3Aclosed">
  <img src="https://img.shields.io/github/issues/dexsuite/dex-retargeting.svg" alt="Issues">
  </a>
  <!-- release badge -->
  <a href="https://github.com/dexsuite/dex-retargeting/tags">
  <img src="https://img.shields.io/github/v/release/dexsuite/dex-retargeting.svg?include_prereleases&sort=semver" alt="Releases">
  </a>
  <!-- pypi badge -->
  <a href="https://github.com/dexsuite/dex-retargeting/tags">
  <img src="https://static.pepy.tech/badge/dex_retargeting/month" alt="pypi">
  </a>
  <!-- license badge -->
  <a href="https://github.com/dexsuite/dex-retargeting/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
  </a>
</p>
<div align="center">
  <h4>This repo originates from <a href="https://yzqin.github.io/anyteleop/">AnyTeleop Project</a></h4>
  <img src="example/vector_retargeting/teaser.webp" alt="Retargeting with different hands.">
</div>

## Installation

```shell
pip install dex_retargeting
```

To run the example, you may need additional dependencies for rendering and hand pose detection.

```shell
git clone https://github.com/dexsuite/dex-retargeting
cd dex-retargeting
pip install -e ".[example]"
```

## Changelog

### v0.5.0

- **Numpy Support Update**: Starting from this version, `dex-retargeting` supports `numpy >= 2.0.0`. If you need to use `numpy < 2.0.0`, you can install an earlier version of `dex-retargeting` using:
  ```bash
  pip install "dex-retargeting<0.5.0"
  ```

- **Mediapipe Compatibility**: Although `mediapipe` lists `numpy 1.x` as a dependency, it is compatible with `numpy >= 2.0.0`. You can safely ignore any warnings related to this and continue using `numpy 2.0.0` or higher.

- **Dependency Cleanup**: Removed `trimesh` as a dependency to simplify installation and reduce potential conflicts. The core functionality of `dex-retargeting` no longer requires mesh processing capabilities.

## Examples

### Retargeting from human hand video

This type of retargeting can be used for applications like teleoperation,
e.g. [AnyTeleop](https://yzqin.github.io/anyteleop/).

[Tutorial on retargeting from human hand video](example/vector_retargeting/README.md)

### Retarget from hand object pose dataset

![teaser](example/position_retargeting/hand_object.webp)

This type of retargeting can be used post-process human data for robot imitation,
e.g. [DexMV](https://yzqin.github.io/dexmv/).

[Tutorial on retargeting from hand-object pose dataset](example/position_retargeting/README.md)

## FAQ and Troubleshooting

### Joint Orders for Retargeting

URDF parsers, such as ROS, physical simulators, real robot driver, and this repository, may parse URDF files with
different joint orders. To use `dex-retargeting` results with other libraries, handle joint ordering explicitly **using
joint names**, which are unique within a URDF file.

Example: Using `dex-retargeting` with the SAPIEN simulator

```python
from dex_retargeting.seq_retarget import SeqRetargeting

retargeting: SeqRetargeting
sapien_joint_names = [joint.get_name() for joint in robot.get_active_joints()]
retargeting_joint_names = retargeting.joint_names
retargeting_to_sapien = np.array([retargeting_joint_names.index(name) for name in sapien_joint_names]).astype(int)

# Use the index map to handle joint order differences
sapien_robot.set_qpos(retarget_qpos[retargeting_to_sapien])
```

This example retrieves joint names from the SAPIEN robot and `SeqRetargeting` object, creates a mapping
array (`retargeting_to_sapien`) to map joint indices, and sets the SAPIEN robot's joint positions using the retargeted
joint positions.

## Citation

This repository is derived from the [AnyTeleop Project](https://yzqin.github.io/anyteleop/) and is subject to ongoing
enhancements. If you utilize this work, please cite it as follows:

```shell
@inproceedings{qin2023anyteleop,
  title     = {AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System},
  author    = {Qin, Yuzhe and Yang, Wei and Huang, Binghao and Van Wyk, Karl and Su, Hao and Wang, Xiaolong and Chao, Yu-Wei and Fox, Dieter},
  booktitle = {Robotics: Science and Systems},
  year      = {2023}
}
```

## Acknowledgments

The robot hand models in this repository are sourced directly from [dex-urdf](https://github.com/dexsuite/dex-urdf).
The robot kinematics in this repo are based on [pinocchio](https://github.com/stack-of-tasks/pinocchio).
Examples use [SAPIEN](https://github.com/haosulab/SAPIEN) for rendering and visualization.

The `PositionOptimizer` leverages methodologies from our earlier
project, [From One Hand to Multiple Hands](https://yzqin.github.io/dex-teleop-imitation/).
Additionally, the `DexPilotOptimizer`is crafted using insights from [DexPilot](https://sites.google.com/view/dex-pilot).


## File tree (depth 3, assets pruned)

```
.editorconfig
.github/
  workflows/
    build_nightly.yml
    build_stable.yml
    test.yml
.gitignore
.gitmodules
CITATION.cff
LICENSE
README.md
example/
  position_retargeting/
    .gitignore
    README.md
    dataset.py
    hand_object.webp
    hand_robot_viewer.py
    hand_viewer.py
    mano_layer.py
    render_hand_object.py
    visualize_hand_object.py
  profiling/
    generate_human_data_from_video.py
    human_joint_right.pkl
    profile_online_retargeting.py
  vector_retargeting/
    .gitignore
    README.md
    capture_webcam.py
    detect_from_video.py
    render_robot_hand.py
    show_realtime_retargeting.py
    single_hand_detector.py
    teaser.webp
pyproject.toml
src/
  dex_retargeting/
    __init__.py
    configs/
    constants.py
    kinematics_adaptor.py
    optimizer.py
    optimizer_utils.py
    retargeting_config.py
    robot_wrapper.py
    seq_retarget.py
    yourdfpy.py
tests/
  test_optimizer.py
  test_retargeting_config.py
```

## Config files (39)


### src/dex_retargeting/configs/offline/ability_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: ability_hand/ability_hand_left.urdf

  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False

```

### src/dex_retargeting/configs/offline/ability_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: ability_hand/ability_hand_right.urdf

  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False

```

### src/dex_retargeting/configs/offline/allegro_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: allegro_hand/allegro_hand_left.urdf

  target_joint_names: null
  target_link_names: [ "link_15.0_tip", "link_11.0_tip", "link_7.0_tip", "link_3.0_tip", "link_14.0",
                       "link_10.0", "link_6.0", "link_2.0" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/allegro_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: allegro_hand/allegro_hand_right.urdf

  target_joint_names: null
  target_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip", "link_14.0",
                       "link_2.0", "link_6.0", "link_10.0" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/inspire_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: inspire_hand/inspire_hand_left.urdf

  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  target_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False

```

### src/dex_retargeting/configs/offline/inspire_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: inspire_hand/inspire_hand_right.urdf

  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  target_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False

```

### src/dex_retargeting/configs/offline/leap_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: leap_hand/leap_hand_left.urdf

  target_joint_names: null
  target_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head", "thumb_dip", "dip", "dip_2", "dip_3" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/leap_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: leap_hand/leap_hand_right.urdf

  target_joint_names: null
  target_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head", "thumb_dip", "dip", "dip_2", "dip_3" ]

  target_link_human_indices: [ 4, 8, 12, 16, 2, 6, 10, 14 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/panda_gripper.yml

```yaml
retargeting:
  type: position
  urdf_path: panda_gripper/panda_gripper_glb.urdf

  target_joint_names: [ "panda_finger_joint1" ]
  target_link_names: [ "panda_leftfinger", "panda_rightfinger"]

  target_link_human_indices: [ 4, 8 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

  # To ignore the mimic joint tags in the URDF, set it to True
  ignore_mimic_joint: False

```

### src/dex_retargeting/configs/offline/schunk_svh_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: schunk_hand/schunk_svh_hand_left.urdf

  target_joint_names: [ 'left_hand_Thumb_Opposition', 'left_hand_Thumb_Flexion', 'left_hand_Index_Finger_Proximal',
                        'left_hand_Index_Finger_Distal', 'left_hand_Finger_Spread', 'left_hand_Pinky',
                        'left_hand_Ring_Finger', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal' ]
  target_link_names: [ "left_hand_c", "left_hand_t", "left_hand_s", "left_hand_r",
                        "left_hand_q", "left_hand_b", "left_hand_p", "left_hand_o", "left_hand_n", "left_hand_i"]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/schunk_svh_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: schunk_hand/schunk_svh_hand_right.urdf

  target_joint_names: [ 'right_hand_Thumb_Opposition', 'right_hand_Thumb_Flexion', 'right_hand_Index_Finger_Proximal',
                        'right_hand_Index_Finger_Distal', 'right_hand_Finger_Spread', 'right_hand_Pinky',
                        'right_hand_Ring_Finger', 'right_hand_Middle_Finger_Proximal', 'right_hand_Middle_Finger_Distal' ]
  target_link_names: [ "right_hand_c", "right_hand_t", "right_hand_s", "right_hand_r",
                        "right_hand_q", "right_hand_b", "right_hand_p", "right_hand_o", "right_hand_n", "right_hand_i"]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/shadow_hand_left.yml

```yaml
retargeting:
  type: position
  urdf_path: shadow_hand/shadow_hand_left.urdf

  target_joint_names: null
  target_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",
                       "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/offline/shadow_hand_right.yml

```yaml
retargeting:
  type: position
  urdf_path: shadow_hand/shadow_hand_right.urdf

  target_joint_names: null
  target_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",
                       "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]

  target_link_human_indices: [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ]
  add_dummy_free_joint: True

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  # 1 means no filter while 0 means not moving
  low_pass_alpha: 1

```

### src/dex_retargeting/configs/teleop/ability_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: ability_hand/ability_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_origin_link_names: [ "base_link", "base_link", "base_link", "base_link", "base_link" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip", ]
  scaling_factor: 1.0

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/ability_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ability_hand/ability_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  wrist_link_name: "base_link"
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.0

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/ability_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: ability_hand/ability_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  target_origin_link_names: [ "base_link", "base_link", "base_link", "base_link", "base_link" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip", ]
  scaling_factor: 1.0

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/ability_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: ability_hand/ability_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'thumb_q1', 'thumb_q2', 'index_q1', 'middle_q1', 'pinky_q1', 'ring_q1' ]
  wrist_link_name: "base_link"
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.0

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/allegro_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: allegro_hand/allegro_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "wrist", "wrist", "wrist", "wrist" ]
  target_task_link_names: [ "link_15.0_tip", "link_11.0_tip", "link_7.0_tip", "link_3.0_tip" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/allegro_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: allegro_hand/allegro_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "wrist"
  finger_tip_link_names: [ "link_15.0_tip", "link_11.0_tip", "link_7.0_tip", "link_3.0_tip" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/allegro_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: allegro_hand/allegro_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "wrist", "wrist", "wrist", "wrist" ]
  target_task_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/allegro_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: allegro_hand/allegro_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "wrist"
  finger_tip_link_names: [ "link_15.0_tip", "link_3.0_tip", "link_7.0_tip", "link_11.0_tip" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/inspire_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: inspire_hand/inspire_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  target_origin_link_names: [ "base", "base", "base", "base", "base" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.15

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/inspire_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: inspire_hand/inspire_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  wrist_link_name: "base"
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.15

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/inspire_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: inspire_hand/inspire_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  target_origin_link_names: [ "base", "base", "base", "base", "base" ]
  target_task_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.15

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/inspire_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: inspire_hand/inspire_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'pinky_proximal_joint', 'ring_proximal_joint', 'middle_proximal_joint', 'index_proximal_joint',
                        'thumb_proximal_pitch_joint', 'thumb_proximal_yaw_joint' ]
  wrist_link_name: "base"
  finger_tip_link_names: [ "thumb_tip",  "index_tip", "middle_tip", "ring_tip", "pinky_tip" ]
  scaling_factor: 1.15

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/leap_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: leap_hand/leap_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "base", "base", "base", "base" ]
  target_task_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/leap_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: leap_hand/leap_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "base"
  finger_tip_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/leap_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: leap_hand/leap_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "base", "base", "base", "base" ]
  target_task_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0 ], [ 4, 8, 12, 16 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/leap_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: leap_hand/leap_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "base"
  finger_tip_link_names: [ "thumb_tip_head", "index_tip_head", "middle_tip_head", "ring_tip_head" ]
  scaling_factor: 1.6

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/panda_gripper.yml

```yaml
retargeting:
  type: vector
  urdf_path: panda_gripper/panda_gripper_glb.urdf 

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ "panda_finger_joint1" ]
  target_origin_link_names: [ "panda_leftfinger" ]
  target_task_link_names: [ "panda_rightfinger" ]
  scaling_factor: 1.5

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 4 ], [ 8 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/panda_gripper_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: panda_gripper/panda_gripper_glb.urdf 

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ "panda_finger_joint1" ]
  wrist_link_name: "panda_hand"
  finger_tip_link_names: [ "panda_leftfinger", "panda_rightfinger" ]
  scaling_factor: 1.5

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/schunk_svh_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: schunk_hand/schunk_svh_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'left_hand_Thumb_Opposition', 'left_hand_Thumb_Flexion', 'left_hand_Index_Finger_Proximal',
                        'left_hand_Index_Finger_Distal', 'left_hand_Finger_Spread', 'left_hand_Pinky',
                        'left_hand_Ring_Finger', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal' ]
  target_origin_link_names: [ "left_hand_base_link","left_hand_base_link", "left_hand_base_link", "left_hand_base_link", "left_hand_base_link", ]
  target_task_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2


  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20, ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/schunk_svh_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: schunk_hand/schunk_svh_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'left_hand_Thumb_Opposition', 'left_hand_Thumb_Flexion', 'left_hand_Index_Finger_Proximal',
                        'left_hand_Index_Finger_Distal', 'left_hand_Finger_Spread', 'left_hand_Pinky',
                        'left_hand_Ring_Finger', 'left_hand_Middle_Finger_Proximal', 'left_hand_Middle_Finger_Distal' ]
  wrist_link_name: "left_hand_base_link"
  finger_tip_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/schunk_svh_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: schunk_hand/schunk_svh_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'right_hand_Thumb_Opposition', 'right_hand_Thumb_Flexion', 'right_hand_Index_Finger_Proximal',
                        'right_hand_Index_Finger_Distal', 'right_hand_Finger_Spread', 'right_hand_Pinky',
                        'right_hand_Ring_Finger', 'right_hand_Middle_Finger_Proximal', 'right_hand_Middle_Finger_Distal' ]
  target_origin_link_names: [ "right_hand_base_link","right_hand_base_link", "right_hand_base_link", "right_hand_base_link", "right_hand_base_link", ]
  target_task_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2


  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20, ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/schunk_svh_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: schunk_hand/schunk_svh_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: [ 'right_hand_Thumb_Opposition', 'right_hand_Thumb_Flexion', 'right_hand_Index_Finger_Proximal',
                        'right_hand_Index_Finger_Distal', 'right_hand_Finger_Spread', 'right_hand_Pinky',
                        'right_hand_Ring_Finger', 'right_hand_Middle_Finger_Proximal', 'right_hand_Middle_Finger_Distal' ]
  wrist_link_name: "right_hand_base_link"
  finger_tip_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/shadow_hand_left.yml

```yaml
retargeting:
  type: vector
  urdf_path: shadow_hand/shadow_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm" ]
  target_task_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",  "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]
  scaling_factor: 1.2

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/shadow_hand_left_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: shadow_hand/shadow_hand_left.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "ee_link"
  finger_tip_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/shadow_hand_right.yml

```yaml
retargeting:
  type: vector
  urdf_path: shadow_hand/shadow_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  target_origin_link_names: [ "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm", "palm" ]
  target_task_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip",  "thmiddle", "ffmiddle", "mfmiddle", "rfmiddle", "lfmiddle" ]
  scaling_factor: 1.2

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 4, 8, 12, 16, 20, 2, 6, 10, 14, 18 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

### src/dex_retargeting/configs/teleop/shadow_hand_right_dexpilot.yml

```yaml
retargeting:
  type: DexPilot
  urdf_path: shadow_hand/shadow_hand_right.urdf

  # Target refers to the retargeting target, which is the robot hand
  wrist_link_name: "ee_link"
  finger_tip_link_names: [ "thtip", "fftip", "mftip", "rftip", "lftip" ]
  scaling_factor: 1.2

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.2

```

## Python signatures and reward/observation bodies (22 files)


### example/position_retargeting/dataset.py

```
"""DexYCB dataset."""
class DexYCBVideoDataset()
    def __init__(self, data_dir, hand_type, filter_objects)
    def __len__(self)
    def __getitem__(self, item)
    def _filter_object_motion_frame(self, capture_filter, object_pose, frame_margin)
    def is_object_move(single_object_pose)
    def _object_mesh_file(self, object_id)
    def _load_camera_parameters(self)
    def _load_mano(self)
def main(dexycb_dir)
```

### example/position_retargeting/hand_robot_viewer.py

```
class RobotHandDatasetSAPIENViewer(HandDatasetSAPIENViewer)
    def __init__(self, robot_names, hand_type, headless, use_ray_tracing)
    def load_object_hand(self, data)
    def render_dexycb_data(self, data, fps, y_offset)
```

### example/position_retargeting/hand_viewer.py

```
def compute_smooth_shading_normal_np(vertices, indices)
class HandDatasetSAPIENViewer()
    def __init__(self, headless, use_ray_tracing)
    def clear_all(self)
    def clear_node(self)
    def load_object_hand(self, data)
    def _load_ycb_object(self, ycb_id, ycb_mesh_file)
    def _compute_hand_geometry(self, hand_pose_frame, use_camera_frame)
    def _update_hand(self, vertex)
    def render_dexycb_data(self, data, fps)
```

### example/position_retargeting/mano_layer.py

```
"""Wrapper layer for manopth ManoLayer."""
class MANOLayer(Module)
    """Wrapper layer for manopth ManoLayer."""
    def __init__(self, side, betas)
    def forward(self, p, t)
```

### example/position_retargeting/render_hand_object.py

```
def viz_hand_object(robots, data_root, fps)
def main(dexycb_dir, robots, fps)
```

### example/position_retargeting/visualize_hand_object.py

```
def viz_hand_object(robots, data_root, fps)
def main(dexycb_dir, robots, fps)
```

### example/profiling/profile_online_retargeting.py

```
def profile_retargeting(retargeting, data)
def main()
```

### example/vector_retargeting/capture_webcam.py

```
def main(video_path, video_capture_device)
```

### example/vector_retargeting/detect_from_video.py

```
def retarget_video(retargeting, video_path, output_path, config_path)
def main(robot_name, video_path, output_path, retargeting_type, hand_type)
```

### example/vector_retargeting/render_robot_hand.py

```
def render_by_sapien(meta_data, data, output_video_path, headless)
def main(pickle_path, output_video_path, headless)
```

### example/vector_retargeting/show_realtime_retargeting.py

```
def start_retargeting(queue, robot_dir, config_path)
def produce_frame(queue, camera_path)
def main(robot_name, retargeting_type, hand_type, camera_path)
```

### example/vector_retargeting/single_hand_detector.py

```
class SingleHandDetector()
    def __init__(self, hand_type, min_detection_confidence, min_tracking_confidence, selfie)
    def draw_skeleton_on_image(image, keypoint_2d, style)
    def detect(self, rgb)
    def parse_keypoint_3d(keypoint_3d)
    def parse_keypoint_2d(keypoint_2d, img_size)
    def estimate_frame_from_hand_points(keypoint_3d_array)
```

### src/dex_retargeting/constants.py

```
class RobotName(Enum)
class RetargetingType(Enum)
class HandType(Enum)
def get_default_config_path(robot_name, retargeting_type, hand_type)
```

### src/dex_retargeting/kinematics_adaptor.py

```
class KinematicAdaptor()
    def __init__(self, robot, target_joint_names)
    def forward_qpos(self, qpos)
    def backward_jacobian(self, jacobian)
class MimicJointKinematicAdaptor(KinematicAdaptor)
    def __init__(self, robot, target_joint_names, source_joint_names, mimic_joint_names, multipliers, offsets)
    def forward_qpos(self, pin_qpos)
    def backward_jacobian(self, jacobian)
```

### src/dex_retargeting/optimizer.py

```
class Optimizer()
    def __init__(self, robot, target_joint_names, target_link_human_indices)
    def set_joint_limit(self, joint_limits, epsilon)
    def get_link_indices(self, target_link_names)
    def set_kinematic_adaptor(self, adaptor)
    def retarget(self, ref_value, fixed_qpos, last_qpos)
    def get_objective_function(self, ref_value, fixed_qpos, last_qpos)
    def fixed_joint_names(self)
class PositionOptimizer(Optimizer)
    def __init__(self, robot, target_joint_names, target_link_names, target_link_human_indices, huber_delta, norm_delta)
    def get_objective_function(self, target_pos, fixed_qpos, last_qpos)
class VectorOptimizer(Optimizer)
    def __init__(self, robot, target_joint_names, target_origin_link_names, target_task_link_names, target_link_human_indices, huber_delta, norm_delta, scaling)
    def get_objective_function(self, target_vector, fixed_qpos, last_qpos)
class DexPilotOptimizer(Optimizer)
    """Retargeting optimizer using the method proposed in DexPilot

This is a broader adaptation of the original optimizer delineated in the DexPilot paper.
While the initial DexPilot study focused solely on the four-fingered Allegro Hand, this version of the optimizer
embraces the same principles for both"""
    def __init__(self, robot, target_joint_names, finger_tip_link_names, wrist_link_name, target_link_human_indices, huber_delta, norm_delta, project_dist, escape_dist, eta1, eta2, scaling)
    def generate_link_indices(num_fingers)
    def set_dexpilot_cache(num_fingers, eta1, eta2)
    def get_objective_function(self, target_vector, fixed_qpos, last_qpos)
```

### src/dex_retargeting/optimizer_utils.py

```
class LPFilter()
    def __init__(self, alpha)
    def next(self, x)
    def reset(self)
```

### src/dex_retargeting/retargeting_config.py

```
class RetargetingConfig()
    def __post_init__(self)
    def set_default_urdf_dir(cls, urdf_dir)
    def load_from_file(cls, config_path, override)
    def from_dict(cls, cfg, override)
    def build(self)
def get_retargeting_config(config_path)
def parse_mimic_joint(robot_urdf)
```

### src/dex_retargeting/robot_wrapper.py

```
class RobotWrapper()
    """This class does not take mimic joint into consideration"""
    def __init__(self, urdf_path, use_collision, use_visual)
    def joint_names(self)
    def dof_joint_names(self)
    def dof(self)
    def link_names(self)
    def joint_limits(self)
    def get_joint_index(self, name)
    def get_link_index(self, name)
    def get_joint_parent_child_frames(self, joint_name)
    def compute_forward_kinematics(self, qpos)
    def get_link_pose(self, link_id)
    def get_link_pose_inv(self, link_id)
    def compute_single_link_local_jacobian(self, qpos, link_id)
```

### src/dex_retargeting/seq_retarget.py

```
class SeqRetargeting()
    def __init__(self, optimizer, has_joint_limits, lp_filter)
    def warm_start(self, wrist_pos, wrist_quat, hand_type, is_mano_convention)
    def retarget(self, ref_value, fixed_qpos)
    def set_qpos(self, robot_qpos)
    def get_qpos(self, fixed_qpos)
    def verbose(self)
    def reset(self)
    def joint_names(self)
```

### src/dex_retargeting/yourdfpy.py

```
def _array_eq(arr1, arr2)
class TransmissionJoint()
    def __eq__(self, other)
class Actuator()
    def __eq__(self, other)
class Transmission()
    def __eq__(self, other)
class Calibration()
class Mimic()
class SafetyController()
class Sphere()
class Cylinder()
class Box()
    def __eq__(self, other)
class Mesh()
    def __eq__(self, other)
class Geometry()
class Color()
    def __eq__(self, other)
class Texture()
class Material()
class Visual()
    def __eq__(self, other)
class Collision()
    def __eq__(self, other)
class Inertial()
    def __eq__(self, other)
class Link()
    def __eq__(self, other)
class Dynamics()
class Limit()
class Joint()
    def __eq__(self, other)
class Robot()
    def __eq__(self, other)
class URDFError(Exception)
    """General URDF exception."""
    def __init__(self, msg)
    def __str__(self)
    def __repr__(self)
class URDFIncompleteError(URDFError)
    """Raised when needed data for an object isn't there."""
class URDFAttributeValueError(URDFError)
    """Raised when attribute value is not contained in the set of allowed values."""
class URDFBrokenRefError(URDFError)
    """Raised when a referenced object is not found in the scope."""
class URDFMalformedError(URDFError)
    """Raised when data is found to be corrupted in some way."""
class URDFUnsupportedError(URDFError)
    """Raised when some unexpectedly unsupported feature is found."""
class URDFSaveValidationError(URDFError)
    """Raised when XML validation fails when saving."""
def _str2float(s)
def filename_handler_null(fname)
def filename_handler_ignore_directive(fname)
def filename_handler_ignore_directive_package(fname)
def filename_handler_add_prefix(fname, prefix)
def filename_handler_absolute2relative(fname, dir)
def filename_handler_relative(fname, dir)
def filename_handler_relative_to_urdf_file(fname, urdf_fname)
def filename_handler_relative_to_urdf_file_recursive(fname, urdf_fname, level)
def _create_filename_handlers_to_urdf_file_recursive(urdf_fname)
def filename_handler_meta(fname, filename_handlers)
def filename_handler_magic(fname, dir)
def validation_handler_strict(errors)
class URDF()
    def __init__(self, robot, build_scene_graph, build_collision_scene_graph, load_meshes, load_collision_meshes, filename_handler, mesh_dir, force_mesh, force_collision_mesh, build_tree)
    def link_map(self)
    def joint_map(self)
    def joint_names(self)
    def actuated_joints(self)
    def actuated_dof_indices(self)
    def actuated_joint_indices(self)
    def actuated_joint_names(self)
    def num_actuated_joints(self)
    def num_dofs(self)
    def zero_cfg(self)
    def center_cfg(self)
    def cfg(self)
    def base_link(self)
    def errors(self)
    def clear_errors(self)
    def show(self, collision_geometry, callback)
    def validate(self, validation_fn)
    def _create_maps(self)
    def _update_actuated_joints(self)
    def _validate_required_attribute(self, attribute, error_msg, allowed_values)
    def load(fname_or_file, add_dummy_free_joints)
    def contains(self, key, value, element)
    def _determine_base_link(self)
    def _forward_kinematics_joint(self, joint, q)
    def _create_subrobot(self, robot_name, root_link_name)
    def validate_filenames(self)
    def write_xml(self)
    def write_xml_string(self)
    def write_xml_file(self, fname)
    def _parse_mimic(xml_element)
    def _write_mimic(self, xml_parent, mimic)
    def _parse_safety_controller(xml_element)
    def _write_safety_controller(self, xml_parent, safety_controller)
    def _parse_transmission_joint(xml_element)
    def _write_transmission_joint(self, xml_parent, transmission_joint)
    def _parse_actuator(xml_element)
    def _write_actuator(self, xml_parent, actuator)
    def _parse_transmission(xml_element)
    def _write_transmission(self, xml_parent, transmission)
    def _parse_calibration(xml_element)
    def _write_calibration(self, xml_parent, calibration)
    def _parse_box(xml_element)
    def _write_box(self, xml_parent, box)
    def _parse_cylinder(xml_element)
    def _write_cylinder(self, xml_parent, cylinder)
    def _parse_sphere(xml_element)
    def _write_sphere(self, xml_parent, sphere)
    def _parse_scale(xml_element)
    def _write_scale(self, xml_parent, scale)
    def _parse_mesh(xml_element)
    def _write_mesh(self, xml_parent, mesh)
    def _parse_geometry(xml_element)
    def _validate_geometry(self, geometry)
    def _write_geometry(self, xml_parent, geometry)
    def _parse_origin(xml_element)
    def _write_origin(self, xml_parent, origin)
    def _parse_color(xml_element)
    def _write_color(self, xml_parent, color)
    def _parse_texture(xml_element)
    def _write_texture(self, xml_parent, texture)
    def _parse_material(xml_element)
    def _write_material(self, xml_parent, material)
    def _parse_visual(xml_element)
    def _validate_visual(self, visual)
    def _write_visual(self, xml_parent, visual)
    def _parse_collision(xml_element)
    def _validate_collision(self, collision)
    def _write_collision(self, xml_parent, collision)
    def _parse_inertia(xml_element)
    def _write_inertia(self, xml_parent, inertia)
    def _parse_mass(xml_element)
    def _write_mass(self, xml_parent, mass)
    def _parse_inertial(xml_element)
    def _write_inertial(self, xml_parent, inertial)
    def _parse_link(xml_element)
    def _validate_link(self, link)
    def _write_link(self, xml_parent, link)
    def _parse_axis(xml_element)
    def _write_axis(self, xml_parent, axis)
    def _parse_limit(xml_element)
    def _validate_limit(self, limit, type)
    def _write_limit(self, xml_parent, limit)
    def _parse_dynamics(xml_element)
    def _write_dynamics(self, xml_parent, dynamics)
    def _parse_joint(xml_element)
    def _validate_joint(self, joint)
    def _write_joint(self, xml_parent, joint)
    def _parse_robot(xml_element, add_dummy_free_joints)
    def _validate_robot(self, robot)
    def _write_robot(self, robot)
    def __eq__(self, other)
    def filename_handler(self)
    def build_tree(self)
    def update_kinematics(self, configuration)
    def get_link_global_transform(self, link_name)
def _add_dummy_joints(robot, root_link_name)
```

### tests/test_retargeting_config.py

```
class TestRetargetingConfig()
    def test_path_config_parsing(self, config_path)
    def test_dict_config_parsing(self)
    def test_multi_dict_config_parsing(self)
    def test_add_dummy_joint(self, config_path)
```