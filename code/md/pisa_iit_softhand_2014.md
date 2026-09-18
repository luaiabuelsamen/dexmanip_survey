# pisa_iit_softhand_2014

source: https://github.com/CentroEPiaggio/pisa-iit-soft-hand


commit: 174eebc6e9e33c886cab7995f749830a436de3e8


## README

# pisa-iit-soft-hand (ROS/Gazebo packages)

This repository contains the model of the Pisa/IIT hand as described in:

* M. G. Catalano, Grioli, G., Farnioli, E., Serio, A., Piazza, C., and Bicchi, A., “Adaptive Synergies for the Design and Control of the Pisa/IIT SoftHand”, International Journal of Robotics Research, vol. 33, no. 5, pp. 768–782, 2014

[Free version of the paper](http://www.centropiaggio.unipi.it/sites/default/files/PisaIIT_SoftHand_0.pdf) and
[IJRR version (access required)](http://ijr.sagepub.com/content/33/5/768.abstract)

Unless stated otherwise, all files within the repository are released under the BSD 3-Clause License, see the [LICENSE](https://github.com/CentroEPiaggio/pisa-iit-soft-hand/blob/master/LICENSE) file for the details.

## Cloning the repository
```
git clone --recursive https://github.com/CentroEPiaggio/pisa-iit-soft-hand.git
```

## Dependencies

ToDo: Create a travis.yml file for this.

## Examples
There are several [examples](https://github.com/CentroEPiaggio/pisa-iit-soft-hand/tree/master/examples) that show how the hand can be used in different configurations.

###Push the finger (Not implemented)

Test the adaptive synergy transmission by applying a wrench to the middle fingertip (you must choose start_time and duration according to the ROS time clock)

```
rosservice call /gazebo/apply_body_wrench "body_name: 'soft_hand::soft_hand_middle_distal_link'
wrench:
  force: {x: 0.0, y: 0.0, z: 10.0}
  torque: {x: 0.0, y: 0.0, z: 0.0}
duration: {secs: -1, nsecs: 0}"
```

And clear the wrench in case you want to continue working normally

`rosservice call /gazebo/clear_body_wrenches "body_name: 'soft_hand::soft_hand_middle_distal_link'"`

## Hand configuration using QBtools (USB/Handle)

These packages assume you use qbTools to move the hand, since it is the electronics the hand is sold with.

To set-up the hand, refer to the instructions by [NMMI](https://github.com/NMMI/qbadmin).

The interface is now shared between the `SoftHand` and `qbMove` devices.


## File tree (depth 3, assets pruned)

```
.gitignore
.gitmodules
LICENSE
README.md
examples/
  adaptive_example/
    CMakeLists.txt
    config/
    launch/
    objects/
    package.xml
    robot/
    worlds/
  full_actuated_example/
    CMakeLists.txt
    config/
    launch/
    package.xml
    robot/
    worlds/
  interactive_grasping_simulatior/
    CMakeLists.txt
    README.md
    config/
    launch/
    package.xml
    src/
    world/
  kinematic_synergy_example/
    CMakeLists.txt
    config/
    launch/
    package.xml
    robot/
    worlds/
  two_hands_example/
    CMakeLists.txt
    config/
    launch/
    package.xml
    robot/
    worlds/
gazebo_ros_soft_hand/
  CMakeLists.txt
  README.md
  adaptive_transmission_plugin.xml
  doc/
    diagram.pdf
    diagram.svg
    paper.pdf
  include/
    adaptive_transmission/
    gazebo_ros_soft_hand/
  package.xml
  soft_hand_hw_sim_plugins.xml
  src/
    adaptive_synergy_transmission_loader.cpp
    default_soft_hand_hw_sim.cpp
    gazebo_ros_soft_hand_plugin.cpp
    kinematic_ctrl_soft_hand_hw_sim.cpp
  test/
    adaptive_synergy_transmission_loader_test.cpp
    adaptive_synergy_transmission_test.cpp
    random_generator_utils.h
    read_file.h
hand-tools/
  qbAPI/
  qbadmin/
soft_hand/
  CMakeLists.txt
  package.xml
soft_hand_description/
  CMakeLists.txt
  README.md
  model/
    accesories/
    materials.urdf.xacro
    soft_hand.gazebo.xacro
    soft_hand.inertia.xacro
    soft_hand.transmission.xacro
    soft_hand.urdf.xacro
  package.xml
soft_hand_ros_control/
  CMakeLists.txt
  README.md
  include/
    soft_hand_ros_control/
  launch/
    soft_hand_adaptive.launch
    soft_hand_full_control.launch
    soft_hand_hw.launch
  package.xml
  src/
    soft_hand_hw.cpp
```

## Config files (11)


### examples/adaptive_example/config/controllers.yaml

```yaml
soft_hand:
  # Publish all joint states, including mimic joints -----------------------------------
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 100

  joint_position_controller:
    type: position_controllers/JointPositionController
    joint: soft_hand_synergy_joint

  joint_trajectory_controller:
    type: position_controllers/JointTrajectoryController
    joints: 
      - soft_hand_synergy_joint
```

### examples/adaptive_example/config/joint_names.yaml

```yaml
joints:
  - soft_hand_synergy_joint
```

### examples/full_actuated_example/config/joint_names.yaml

```yaml
joints:
  - soft_hand_synergy_joint
```

### examples/full_actuated_example/config/soft_hand_full_control.yaml

```yaml
soft_hand:
  # Publish all joint states -----------------------------------
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 100

  # Position Controllers ---------------------------------------
  hand_thumb_abd_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_thumb_abd_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_thumb_inner_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_thumb_inner_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_thumb_outer_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_thumb_outer_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_abd_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_abd_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_inner_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_inner_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_middle_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_middle_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_outer_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_outer_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_abd_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_abd_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_inner_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_inner_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_middle_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_middle_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_outer_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_outer_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_abd_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_abd_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_inner_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_inner_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_middle_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_middle_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_outer_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_outer_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_abd_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_abd_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_inner_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_inner_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_middle_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_middle_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_outer_joint_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_outer_joint
    pid: {p: 1.0, i: 0.1, d: 0.5}

  # mimic joints
  hand_thumb_inner_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_thumb_inner_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_thumb_outer_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_thumb_outer_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_inner_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_inner_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_middle_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_middle_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_index_outer_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_index_outer_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_inner_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_inner_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_middle_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_middle_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_middle_outer_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_middle_outer_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_inner_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_inner_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_middle_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_middle_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_ring_outer_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_ring_outer_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_inner_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_inner_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_middle_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_middle_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}

  hand_little_outer_joint_mimic_position_controller:
    type: effort_controllers/JointPositionController
    joint: soft_hand_little_outer_joint_mimic
    pid: {p: 1.0, i: 0.1, d: 0.5}
```

### examples/interactive_grasping_simulatior/config/controllers.yaml

```yaml
soft_hand:
  # Publish all joint states, including mimic joints -----------------------------------
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 1000

  joint_trajectory_controller:
    type: position_controllers/JointTrajectoryController
    joints: 
      - soft_hand_synergy_joint
```

### examples/interactive_grasping_simulatior/config/joint_names.yaml

```yaml
joints:
  - soft_hand_synergy_joint
```

### examples/kinematic_synergy_example/config/controllers.yaml

```yaml
soft_hand:
  # Publish all joint states, including mimic joints -----------------------------------
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 100

  joint_position_controller:
    type: position_controllers/JointPositionController
    joint: soft_hand_synergy_joint

  joint_trajectory_controller:
    type: position_controllers/JointTrajectoryController
    joints: 
      - soft_hand_synergy_joint
```

### examples/kinematic_synergy_example/config/joint_names.yaml

```yaml
joints:
  - soft_hand_synergy_joint
```

### examples/two_hands_example/config/controllers.yaml

```yaml
left_hand:
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 100  
  joint_trajectory_controller:
    type: position_controllers/JointTrajectoryController
    joints: 
      - left_hand_synergy_joint

right_hand:
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 100
  joint_trajectory_controller:
    type: position_controllers/JointTrajectoryController
    joints: 
      - right_hand_synergy_joint
```

### examples/two_hands_example/config/left_hand_names.yaml

```yaml
joints:
  - left_hand_synergy_joint
```

### examples/two_hands_example/config/right_hand_names.yaml

```yaml
joints:
  - right_hand_synergy_joint
```

## Python signatures and reward/observation bodies (0 files)
