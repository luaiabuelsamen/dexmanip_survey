# bidexhand_2025

source: https://github.com/wengmister/BiDexHand


commit: 6cd2c754f53393cad13f752c16c3ea51cfce3b21


## README

# BiDexHand: Open-Source 16-DoF Biomimetic Dexterous Hand
Author: [Zhengyang Kris Weng](https://wengmister.github.io/)   
[arXiv](https://arxiv.org/abs/2504.14712) | [OnShape](https://cad.onshape.com/documents/01cd86c3e9db901b13d9f00a/w/85362aa967854376c1ce3eaf/e/cdd4272996feef8877266f8c?renderMode=0&uiState=68e7603e87a047038d7ce8cc) | [Blogpost](https://wengmister.github.io/#dexterous-hand)

Open source release of BiDexHand. This guide will help you build your own hand and get your started on the setup.

[![Biomimetic Dexterous Hand Demonstration](https://img.youtube.com/vi/X8zVKlZNorc/0.jpg)](https://youtu.be/X8zVKlZNorc?si=lmVslFvECZyih0Kd)

# Overview

This is the open source release of the BiDexHand V4, a robotic hand featuring 16 degrees of freedom. It utilizes a cable-and-pulley system, with 15 servos arranged in `N configuration` to drive its 15 joints with tenden, and a 4-bar linkage driven 16th joint.

Each finger provides three degrees of freedom: metacarpal (MCP) adduction/abduction, MCP flexion/extension, and proximal interphalangeal (PIP) flexion/extension. A custom four-bar linkage at the distal end of each phalanx converts the PIP motion into a coupled movement at the distal interphalangeal (DIP) joint. The thumb is designed with four degrees of freedom, including carpometacarpal (CMC) adduction/abduction and flexion/extension, as well as MCP adduction/abduction and flexion/extension.

The hand is controlled through provided `ROS2` packages found in `/src`. It provides several modes to interface with the robot - `motion shadowing` and `servo input` streaming through `ROS2` topic, or direct `servo input` control through CLI. See packages in `/src` for more details.

**V4 Updates in a nutshell:**
- Updated single shear phalanx
- Added servo calibration modules
- Now using unified FeeTech servos (see [BOM](/BOM.md) update)
- Now using servo2040 for PWM builds
- Franka whole arm VR teleoperation (see [this repo](https://github.com/wengmister/franka-vr-teleop) for more details)

# Hardware Setup

STEP file for the cad asset can be found under `/cad_asset/_stp`, and individual STL file under `/cad_asset/_stl`. Additionally, you can find CAD hosted online on [OnShape](https://cad.onshape.com/documents/01cd86c3e9db901b13d9f00a/w/85362aa967854376c1ce3eaf/e/cdd4272996feef8877266f8c?renderMode=0&uiState=68e7603e87a047038d7ce8cc).

See [BOM.md](/BOM.md) for more details.

For `V4`, build, flash and deploy `/scripts/Servo2040/servo2040_controller` to controller for the PWM version. Alternatively, use script from `V3` fork for SCS bus builds.
- You'll need `pico-sdk` and `pimoroni-pico` modules to build the PWM project.

# Environment Setup

This project is primarily tested on `ROS2-JAZZY`. To build locally, run:

    git clone https://github.com/wengmister/BiDexHand.git
    cd BiDexHand
    rosdep install --from-paths src -y --ignore-src

Finally, 

    colcon build
    . install/setup.bash

# VR Setup

If you plan to use Meta Quest for the motion shadowing demo, you can follow the build and deployment steps in [this repo](https://github.com/NU-MECH-ENG-495/vr-hand-tracking).


# Quickstart
### Hand Control

For motion shadowing:

    ros2 launch hand_motion_shadowing shadowing.launch.xml usb:=/dev/ttyACM0

For direct servo control:

    ros2 launch hand_servo_control multi_servo_control.launch.xml usb:=/dev/ttyACM0

Change usb port based on your device setting.

For Franka `MoveIT!` config demo:

    ros2 launch combined_fer_moveit_config demo.launch.py

### Franka Integration

For deploying on real Franka Fer, copy and build the following packages to your robot `station`:
- hand_rviz
- combined_fer_moveit_config

On station, run:

    ros2 launch combined_fer_moveit_config real.launch.py use_rviz:=false robot_ip:=[YOUR_ROBOT_IP]

On your laptop, run:

    ros2 launch combined_fer_moveit_config moveit_rviz.launch.py robot_ip:=[YOUR_ROBOT_IP]

See [this repo](https://github.com/wengmister/franka-vr-teleop) on details about whole arm teleoperation!

# Demo

### Mixed Reality Motion Shadowing      
<img src="images/vr_control_exp.gif" alt="MR" width="500px">

### Calibration
<img src="images/calibration.gif" alt="Calibration" width="500px">

### Franka FER Integration    
<img src="images/franka_integration.gif" alt="Franka" width="500px">

### Franka VR Teleoperation    
<img src="images/franka_teleop.gif" alt="Franka Teleop" width="500px">

# Citation
If you find this work helpful for your work or research, please consider citing as:

    @misc{weng2025bidexhand,
        title={BiDexHand: Design and Evaluation of an Open-Source 16-DoF Biomimetic Dexterous Hand}, 
        author={Zhengyang Kris Weng},
        year={2025},
        eprint={2504.14712},
        archivePrefix={arXiv},
        primaryClass={cs.RO},
        url={https://arxiv.org/abs/2504.14712}, 
    }

# License
MIT

# Related Repo
[Franka VR Teleop](https://github.com/wengmister/franka-vr-teleop)  
[VR Tracking App](https://github.com/wengmister/quest-wrist-tracker)  
[VR dex-retargeting](https://github.com/wengmister/vr-dex-retargeting)  

## File tree (depth 3, assets pruned)

```
.gitattributes
.gitignore
BOM.md
CITATION.cff
LICENSE
README.md
cad_asset/
  _stl/
    palm, base.STL
    palm, coupler.STL
    palm, guard 2.STL
    plx, base.STL
    plx, cover.STL
    plx, distal.STL
    plx, knuckle.STL
    plx, middle.STL
    plx, proximal.STL
    plx, support.STL
    pulley, scs0009.STL
    sleeve, base.STL
    sleeve, servo carriage.STL
    sleeve, servo rack back.STL
    sleeve, servo rack top.STL
    sleeve, servo rack.STL
    sleeve, servo single rack back.STL
    sleeve, servo single rack top.STL
    sleeve, servo single rack.STL
    thumb, arm.STL
    thumb, base.STL
    thumb, bridge.STL
    thumb, cmc.STL
    thumb, cover.STL
    thumb, mcp.STL
    thumb, proximal.STL
  _stp/
    bidexhand v4.STEP
scripts/
  ESP32_multi_servo_control/
    ESP32_multi_servo_control.ino
  ESP32_multi_servo_feather/
    ESP32_multi_servo_feather.ino
  ESP32_multi_servo_with_linear/
    ESP32_multi_servo_with_linear.ino
  ESP32_multi_servo_with_linear_feather/
    ESP32_multi_servo_with_linear_feather.ino
  Servo2040/
    CMakeLists.txt
    servo2040_controller.cpp
src/
  combined_fer_moveit_config/
    .setup_assistant
    CMakeLists.txt
    LICENSE
    config/
    launch/
    package.xml
    srdf/
  hand_calibration/
    LICENSE
    config/
    hand_calibration/
    launch/
    package.xml
    resource/
    setup.cfg
    setup.py
    test/
  hand_calibration_interfaces/
    CMakeLists.txt
    LICENSE
    package.xml
    srv/
  hand_kinematics/
    CMakeLists.txt
    LICENSE
    README.md
    launch/
    package.xml
    src/
    srv/
  hand_motion_shadowing/
    LICENSE
    config/
    hand_motion_shadowing/
    launch/
    package.xml
    resource/
    setup.cfg
    setup.py
    test/
  hand_rviz/
    LICENSE
    config/
    hand_rviz/
    launch/
    package.xml
    resource/
    setup.cfg
    setup.py
    test/
  hand_servo_control/
    LICENSE
    config/
    hand_servo_control/
    launch/
    package.xml
    resource/
    setup.cfg
    setup.py
    test/
  hand_servo_interfaces/
    CMakeLists.txt
    LICENSE
    package.xml
    srv/
  hand_vision/
    LICENSE
    hand_vision/
    launch/
    package.xml
    resource/
    setup.cfg
    setup.py
    test/
```

## Config files (18)


### src/combined_fer_moveit_config/config/fer_real_controllers.yaml

```yaml
controller_manager:
  ros__parameters:
    update_rate: 1000  # Hz

    fer_arm_controller:
      type: joint_trajectory_controller/JointTrajectoryController

    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster

    franka_robot_state_broadcaster:
      type: franka_robot_state_broadcaster/FrankaRobotStateBroadcaster

franka_robot_state_broadcaster:
  ros__parameters:
    arm_id: fer

fer_arm_controller:
  ros__parameters:
    command_interfaces:
      - effort
    state_interfaces:
      - position
      - velocity
    joints:
      - fer_joint1
      - fer_joint2
      - fer_joint3
      - fer_joint4
      - fer_joint5
      - fer_joint6
      - fer_joint7
    gains:
      fer_joint1: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint2: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint3: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint4: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint5: { p: 250., d: 10., i: 0., i_clamp: 1. }
      fer_joint6: { p: 150., d: 10., i: 0., i_clamp: 1. }
      fer_joint7: { p: 50., d: 5., i: 0., i_clamp: 1. }

joint_state_broadcaster:
    ros__parameters:
        use_local_topics: true
```

### src/combined_fer_moveit_config/config/joint_limits.yaml

```yaml
# joint_limits.yaml allows the dynamics properties specified in the URDF to be overwritten or augmented as needed
# Specific joint properties can be changed with the keys [max_position, min_position, max_velocity, max_acceleration]
# Joint limits can be turned off with [has_velocity_limits, has_acceleration_limits]
# These limits are taken from https://support.franka.de/docs/control_parameters.html

default_velocity_scaling_factor: 0.1
default_acceleration_scaling_factor: 0.1

joint_limits:
  fer_joint1:
    max_position: 2.8973
    min_position: -2.8973
    has_velocity_limits: true
    max_velocity: 2.1750
    has_acceleration_limits: true
    max_acceleration: 15.0
  fer_joint2:
    max_position: 1.7628
    min_position: -1.7628
    has_velocity_limits: true
    max_velocity: 2.1750
    has_acceleration_limits: true
    max_acceleration: 7.5
  fer_joint3:
    max_position: 2.8973
    min_position: -2.8973
    has_velocity_limits: true
    max_velocity: 2.1750
    has_acceleration_limits: true
    max_acceleration: 10.0
  fer_joint4:
    max_position: -0.0698
    min_position: -3.0718
    has_velocity_limits: true
    max_velocity: 12.5
    has_acceleration_limits: true
    max_acceleration: 12.5
  fer_joint5:
    max_position: 2.8973
    min_position: -2.8973
    has_velocity_limits: true
    max_velocity: 2.6100
    has_acceleration_limits: true
    max_acceleration: 15.0
  fer_joint6:
    max_position: 3.7525
    min_position: -0.0175
    has_velocity_limits: true
    max_velocity: 2.6100
    has_acceleration_limits: true
    max_acceleration: 20.0
  fer_joint7:
    max_position: 1.750
    min_position: -0.350
    has_velocity_limits: true
    max_velocity: 2.6100
    has_acceleration_limits: true
    max_acceleration: 20.0
  fer_finger_joint1:
    max_position: 0.04
    min_position: 0.00
    has_velocity_limits: true
    max_velocity: 0.2
    has_acceleration_limits: true
    max_acceleration: 20.0
  fer_finger_joint2:
    max_position: 0.04
    min_position: 0.00
    has_velocity_limits: true
    max_velocity: 0.2
    has_acceleration_limits: true
    max_acceleration: 20.0

```

### src/combined_fer_moveit_config/config/kinematics.yaml

```yaml
fer_manipulator:
    kinematics_solver: kdl_kinematics_plugin/KDLKinematicsPlugin
    kinematics_solver_search_resolution: 0.0050000000000000001
    kinematics_solver_timeout: 0.0050000000000000001
fer_arm:
    kinematics_solver: kdl_kinematics_plugin/KDLKinematicsPlugin
    kinematics_solver_search_resolution: 0.0050000000000000001
    kinematics_solver_timeout: 0.0050000000000000001

```

### src/combined_fer_moveit_config/config/moveit_controllers.yaml

```yaml
# MoveIt uses this configuration for controller management

moveit_controller_manager: moveit_simple_controller_manager/MoveItSimpleControllerManager

moveit_simple_controller_manager:
  controller_names:
    - fer_arm_controller
    - fer_gripper

  fer_arm_controller:
    action_ns: follow_joint_trajectory
    type: FollowJointTrajectory
    default: true
    joints:
      - fer_joint1
      - fer_joint2
      - fer_joint3
      - fer_joint4
      - fer_joint5
      - fer_joint6
      - fer_joint7

  fer_gripper:
      action_ns: gripper_action
      type: GripperCommand
      default: true
      joints:
        - fer_finger_joint1
        - fer_finger_joint2

```

### src/combined_fer_moveit_config/config/moveit_cpp.yaml

```yaml
planning_pipelines:
  pipeline_names: ["ompl"]

plan_request_params:
  planning_attempts: 1
  planning_pipeline: ompl
  max_velocity_scaling_factor: 1.0
  max_acceleration_scaling_factor: 1.0
```

### src/combined_fer_moveit_config/config/ompl_planning copy.yaml

```yaml
planning_plugins:
  - ompl_interface/OMPLPlanner
# The order of the elements in the adapter corresponds to the order they are processed by the motion planning pipeline.
request_adapters:
  - default_planning_request_adapters/ResolveConstraintFrames
  - default_planning_request_adapters/ValidateWorkspaceBounds
  - default_planning_request_adapters/CheckStartStateBounds
  - default_planning_request_adapters/CheckStartStateCollision
response_adapters:
  - default_planning_response_adapters/AddTimeOptimalParameterization
  - default_planning_response_adapters/ValidateSolution
  - default_planning_response_adapters/DisplayMotionPath
planner_configs:
  SBLkConfigDefault:
    type: geometric::SBL
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  ESTkConfigDefault:
    type: geometric::EST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0 setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
  LBKPIECEkConfigDefault:
    type: geometric::LBKPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  BKPIECEkConfigDefault:
    type: geometric::BKPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9
    failed_expansion_score_factor: 0.5  # When extending motion fails, scale score by factor. default: 0.5
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  KPIECEkConfigDefault:
    type: geometric::KPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9 (0.0,1.]
    failed_expansion_score_factor: 0.5  # When extending motion fails, scale score by factor. default: 0.5
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  RRTkConfigDefault:
    type: geometric::RRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
  RRTConnectkConfigDefault:
    type: geometric::RRTConnect
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  RRTstarkConfigDefault:
    type: geometric::RRTstar
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
    delay_collision_checking: 1  # Stop collision checking as soon as C-free parent found. default 1
  TRRTkConfigDefault:
    type: geometric::TRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
    max_states_failed: 10  # when to start increasing temp. default: 10
    temp_change_factor: 2.0  # how much to increase or decrease temp. default: 2.0
    min_temperature: 10e-10  # lower limit of temp change. default: 10e-10
    init_temperature: 10e-6  # initial temperature. default: 10e-6
    frountier_threshold: 0.0  # dist new state to nearest neighbor to disqualify as frontier. default: 0.0 set in setup()
    frountierNodeRatio: 0.1  # 1/10, or 1 nonfrontier for every 10 frontier. default: 0.1
    k_constant: 0.0  # value used to normalize expresssion. default: 0.0 set in setup()
  PRMkConfigDefault:
    type: geometric::PRM
    max_nearest_neighbors: 10  # use k nearest neighbors. default: 10
  PRMstarkConfigDefault:
    type: geometric::PRMstar
  FMTkConfigDefault:
    type: geometric::FMT
    num_samples: 1000  # number of states that the planner should sample. default: 1000
    radius_multiplier: 1.1  # multiplier used for the nearest neighbors search radius. default: 1.1
    nearest_k: 1  # use Knearest strategy. default: 1
    cache_cc: 1  # use collision checking cache. default: 1
    heuristics: 0  # activate cost to go heuristics. default: 0
    extended_fmt: 1  # activate the extended FMT*: adding new samples if planner does not finish successfully. default: 1
  BFMTkConfigDefault:
    type: geometric::BFMT
    num_samples: 1000  # number of states that the planner should sample. default: 1000
    radius_multiplier: 1.0  # multiplier used for the nearest neighbors search radius. default: 1.0
    nearest_k: 1  # use the Knearest strategy. default: 1
    balanced: 0  # exploration strategy: balanced true expands one tree every iteration. False will select the tree with lowest maximum cost to go. default: 1
    optimality: 1  # termination strategy: optimality true finishes when the best possible path is found. Otherwise, the algorithm will finish when the first feasible path is found. default: 1
    heuristics: 1  # activates cost to go heuristics. default: 1
    cache_cc: 1  # use the collision checking cache. default: 1
    extended_fmt: 1  # Activates the extended FMT*: adding new samples if planner does not finish successfully. default: 1
  PDSTkConfigDefault:
    type: geometric::PDST
  STRIDEkConfigDefault:
    type: geometric::STRIDE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    use_projected_distance: 0  # whether nearest neighbors are computed based on distances in a projection of the state rather distances in the state space itself. default: 0
    degree: 16  # desired degree of a node in the Geometric Near-neightbor Access Tree (GNAT). default: 16
    max_degree: 18  # max degree of a node in the GNAT. default: 12
    min_degree: 12  # min degree of a node in the GNAT. default: 12
    max_pts_per_leaf: 6  # max points per leaf in the GNAT. default: 6
    estimated_dimension: 0.0  # estimated dimension of the free space. default: 0.0
    min_valid_path_fraction: 0.2  # Accept partially valid moves above fraction. default: 0.2
  BiTRRTkConfigDefault:
    type: geometric::BiTRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    temp_change_factor: 0.1  # how much to increase or decrease temp. default: 0.1
    init_temperature: 100  # initial temperature. default: 100
    frountier_threshold: 0.0  # dist new state to nearest neighbor to disqualify as frontier. default: 0.0 set in setup()
    frountier_node_ratio: 0.1  # 1/10, or 1 nonfrontier for every 10 frontier. default: 0.1
    cost_threshold: 1e300  # the cost threshold. Any motion cost that is not better will not be expanded. default: inf
  LBTRRTkConfigDefault:
    type: geometric::LBTRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    epsilon: 0.4  # optimality approximation factor. default: 0.4
  BiESTkConfigDefault:
    type: geometric::BiEST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  ProjESTkConfigDefault:
    type: geometric::ProjEST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
  LazyPRMkConfigDefault:
    type: geometric::LazyPRM
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  LazyPRMstarkConfigDefault:
    type: geometric::LazyPRMstar
  SPARSkConfigD
```

### src/combined_fer_moveit_config/config/ompl_planning.yaml

```yaml
planning_plugins:
  - ompl_interface/OMPLPlanner
# The order of the elements in the adapter corresponds to the order they are processed by the motion planning pipeline.
request_adapters:
  - default_planning_request_adapters/ResolveConstraintFrames
  - default_planning_request_adapters/ValidateWorkspaceBounds
  - default_planning_request_adapters/CheckStartStateBounds
  - default_planning_request_adapters/CheckStartStateCollision
response_adapters:
  - default_planning_response_adapters/AddTimeOptimalParameterization
  - default_planning_response_adapters/ValidateSolution
  - default_planning_response_adapters/DisplayMotionPath
planner_configs:
  SBLkConfigDefault:
    type: geometric::SBL
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  ESTkConfigDefault:
    type: geometric::EST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0 setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
  LBKPIECEkConfigDefault:
    type: geometric::LBKPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  BKPIECEkConfigDefault:
    type: geometric::BKPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9
    failed_expansion_score_factor: 0.5  # When extending motion fails, scale score by factor. default: 0.5
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  KPIECEkConfigDefault:
    type: geometric::KPIECE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    border_fraction: 0.9  # Fraction of time focused on boarder default: 0.9 (0.0,1.]
    failed_expansion_score_factor: 0.5  # When extending motion fails, scale score by factor. default: 0.5
    min_valid_path_fraction: 0.5  # Accept partially valid moves above fraction. default: 0.5
  RRTkConfigDefault:
    type: geometric::RRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
  RRTConnectkConfigDefault:
    type: geometric::RRTConnect
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  RRTstarkConfigDefault:
    type: geometric::RRTstar
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
    delay_collision_checking: 1  # Stop collision checking as soon as C-free parent found. default 1
  TRRTkConfigDefault:
    type: geometric::TRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability? default: 0.05
    max_states_failed: 10  # when to start increasing temp. default: 10
    temp_change_factor: 2.0  # how much to increase or decrease temp. default: 2.0
    min_temperature: 10e-10  # lower limit of temp change. default: 10e-10
    init_temperature: 10e-6  # initial temperature. default: 10e-6
    frountier_threshold: 0.0  # dist new state to nearest neighbor to disqualify as frontier. default: 0.0 set in setup()
    frountierNodeRatio: 0.1  # 1/10, or 1 nonfrontier for every 10 frontier. default: 0.1
    k_constant: 0.0  # value used to normalize expresssion. default: 0.0 set in setup()
  PRMkConfigDefault:
    type: geometric::PRM
    max_nearest_neighbors: 10  # use k nearest neighbors. default: 10
  PRMstarkConfigDefault:
    type: geometric::PRMstar
  FMTkConfigDefault:
    type: geometric::FMT
    num_samples: 1000  # number of states that the planner should sample. default: 1000
    radius_multiplier: 1.1  # multiplier used for the nearest neighbors search radius. default: 1.1
    nearest_k: 1  # use Knearest strategy. default: 1
    cache_cc: 1  # use collision checking cache. default: 1
    heuristics: 0  # activate cost to go heuristics. default: 0
    extended_fmt: 1  # activate the extended FMT*: adding new samples if planner does not finish successfully. default: 1
  BFMTkConfigDefault:
    type: geometric::BFMT
    num_samples: 1000  # number of states that the planner should sample. default: 1000
    radius_multiplier: 1.0  # multiplier used for the nearest neighbors search radius. default: 1.0
    nearest_k: 1  # use the Knearest strategy. default: 1
    balanced: 0  # exploration strategy: balanced true expands one tree every iteration. False will select the tree with lowest maximum cost to go. default: 1
    optimality: 1  # termination strategy: optimality true finishes when the best possible path is found. Otherwise, the algorithm will finish when the first feasible path is found. default: 1
    heuristics: 1  # activates cost to go heuristics. default: 1
    cache_cc: 1  # use the collision checking cache. default: 1
    extended_fmt: 1  # Activates the extended FMT*: adding new samples if planner does not finish successfully. default: 1
  PDSTkConfigDefault:
    type: geometric::PDST
  STRIDEkConfigDefault:
    type: geometric::STRIDE
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    use_projected_distance: 0  # whether nearest neighbors are computed based on distances in a projection of the state rather distances in the state space itself. default: 0
    degree: 16  # desired degree of a node in the Geometric Near-neightbor Access Tree (GNAT). default: 16
    max_degree: 18  # max degree of a node in the GNAT. default: 12
    min_degree: 12  # min degree of a node in the GNAT. default: 12
    max_pts_per_leaf: 6  # max points per leaf in the GNAT. default: 6
    estimated_dimension: 0.0  # estimated dimension of the free space. default: 0.0
    min_valid_path_fraction: 0.2  # Accept partially valid moves above fraction. default: 0.2
  BiTRRTkConfigDefault:
    type: geometric::BiTRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    temp_change_factor: 0.1  # how much to increase or decrease temp. default: 0.1
    init_temperature: 100  # initial temperature. default: 100
    frountier_threshold: 0.0  # dist new state to nearest neighbor to disqualify as frontier. default: 0.0 set in setup()
    frountier_node_ratio: 0.1  # 1/10, or 1 nonfrontier for every 10 frontier. default: 0.1
    cost_threshold: 1e300  # the cost threshold. Any motion cost that is not better will not be expanded. default: inf
  LBTRRTkConfigDefault:
    type: geometric::LBTRRT
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
    epsilon: 0.4  # optimality approximation factor. default: 0.4
  BiESTkConfigDefault:
    type: geometric::BiEST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  ProjESTkConfigDefault:
    type: geometric::ProjEST
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
    goal_bias: 0.05  # When close to goal select goal, with this probability. default: 0.05
  LazyPRMkConfigDefault:
    type: geometric::LazyPRM
    range: 0.0  # Max motion added to tree. ==> maxDistance_ default: 0.0, if 0.0, set on setup()
  LazyPRMstarkConfigDefault:
    type: geometric::LazyPRMstar
  SPARSkConfigD
```

### src/combined_fer_moveit_config/config/pilz_cartesian_limits.yaml

```yaml
# Limits for the Pilz planner
# Warning: These limits have not been verified. Package not tested with Pilz
cartesian_limits:
  max_trans_vel: 1.0
  max_trans_acc: 2.25
  max_trans_dec: -5.0
  max_rot_vel: 1.57

```

### src/combined_fer_moveit_config/config/ros2_controllers.yaml

```yaml
controller_manager:
  ros__parameters:
    update_rate: 1000  # Hz

    fer_arm_controller:
      type: joint_trajectory_controller/JointTrajectoryController

    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster

fer_arm_controller:
  ros__parameters:
    command_interfaces:
      - position
    state_interfaces:
      - position
      - velocity
    joints:
      - fer_joint1
      - fer_joint2
      - fer_joint3
      - fer_joint4
      - fer_joint5
      - fer_joint6
      - fer_joint7
    gains:
      fer_joint1: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint2: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint3: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint4: { p: 600., d: 30., i: 0., i_clamp: 1. }
      fer_joint5: { p: 250., d: 10., i: 0., i_clamp: 1. }
      fer_joint6: { p: 150., d: 10., i: 0., i_clamp: 1. }
      fer_joint7: { p: 50., d: 5., i: 0., i_clamp: 1. }

joint_state_broadcaster:
    ros__parameters:
        use_local_topics: true
```

### src/hand_calibration/config/atag_calibration.yaml

```yaml
/**:
    ros__parameters:
        image_transport: raw    # image format
        family: 16h5           # tag family name
        size: 0.0105             # tag edge size in meter tag36: size/10*8, tag25: size/9*7, tag16: size/8*6
        max_hamming: 0          # maximum allowed hamming distance (corrected bits)

        # see "apriltag.h" 'struct apriltag_detector' for more documentation on these optional parameters
        detector:
            threads: 4          # number of threads
            decimate: 1.0       # decimate resolution for quad detection
            blur: 0.0           # sigma of Gaussian blur for quad detection
            refine: True        # snap to strong gradientss
            sharpening: 0.25    # sharpening of decoded images
            debug: False        # write additional debugging images to current working directory

        # optional list of tags
        tag:
            ids: [0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 29]            # tag ID
            frames: [tag_0, tag_1, tag_2, tag_3, tag_4, tag_5, tag_6, tag_10, tag_11, tag_12, tag_13, tag_14, piano]  # optional frame name
            sizes: [0.0061875, 0.0061875, 0.0061875, 0.0061875, 0.0061875, 0.0061875, 0.0061875, 0.008625, 0.008625, 0.008625, 0.008625, 0.008625, 0.01950]   # optional tag-specific edge size
```

### src/hand_calibration/config/atag_piano.yaml

```yaml
/**:
    ros__parameters:
        image_transport: raw    # image format
        family: 16h5           # tag family name
        size: 0.0105             # tag edge size in meter tag36: size/10*8, tag25: size/9*7, tag16: size/8*6
        max_hamming: 0          # maximum allowed hamming distance (corrected bits)

        # see "apriltag.h" 'struct apriltag_detector' for more documentation on these optional parameters
        detector:
            threads: 4          # number of threads
            decimate: 1.0       # decimate resolution for quad detection
            blur: 0.0           # sigma of Gaussian blur for quad detection
            refine: True        # snap to strong gradientss
            sharpening: 0.25    # sharpening of decoded images
            debug: False        # write additional debugging images to current working directory

        # optional list of tags
        tag:
            ids: [29]            # tag ID
            frames: [piano]  # optional frame name
            sizes: [0.01950]   # optional tag-specific edge size
```

### src/hand_calibration/config/calibration_params.yaml

```yaml
motor_calibrator:
  ros__parameters:
    mcp_abduction:
      motor_index: 4
      tag_frame: "tag_10"
      min_angle: -25.0
      max_angle: 25.0
    mcp_flexion:
      motor_index: 9
      tag_frame: "tag_10"
      hysteresis_clearance: -15.0
    pip_flexion:
      motor_index: 14
      tag_frame: "tag_0"
      hysteresis_clearance: -10.0
```

### src/hand_motion_shadowing/config/v1mp.yaml

```yaml
# hand_shadowing_params.yaml
hand_shadowing_node:
  ros__parameters:
    # General parameters
    scale_factor: 2.0
    smoothing_factor: 0.3
    
    # Scaling parameters by joint index
    scaling:
      thumb_mcp_abd: -2.0        # index 0
      finger_mcp_abd: 2.0         # indices 1-4
      index_mcp_flex: -5.0        # index 5
      finger_mcp_flex: -5.0       # indices 6-8
      thumb_pip: 5.0              # index 9
      finger_pip: 1.0             # indices 10-13
      thumb_cmc_flex: 10.0        # index 15
    
    # Compensation parameters by joint index
    compensation:
      thumb_mcp_abd: -30.0        # index 0
      finger_mcp_abd: 0.0         # indices 1-4
      finger_mcp_flex: 8.0        # indices 5-8
      thumb_pip: 30.0             # index 9
      finger_pip: 90.0            # indices 10-13
      thumb_cmc_flex: 35.0        # index 15
    
    # Clamping parameters by joint index (min, max)
    clamping:
      thumb_mcp_abd: [-40.0, 40.0]      # index 0
      finger_mcp_abd: [-25.0, 25.0]     # indices 1-4
      finger_mcp_flex: [-90.0, 90.0]    # indices 5-8
      thumb_pip: [-50.0, 90.0]          # index 9
      finger_pip: [-50.0, 90.0]         # indices 10-13
      default: [-90.0, 90.0]            # default (including index 15)
```

### src/hand_motion_shadowing/config/v1quest.yaml

```yaml
# hand_shadowing_params.yaml
hand_shadowing_node:
  ros__parameters:
    # General parameters
    scale_factor: 2.0
    smoothing_factor: 0.3
    
    # Scaling parameters by joint index
    scaling:
      thumb_mcp_abd: -2.0        # index 0
      finger_mcp_abd: -2.0         # indices 1-4
      index_mcp_flex: -5.0        # index 5
      finger_mcp_flex: -5.0       # indices 6-8
      thumb_pip: 5.0              # index 9
      finger_pip: -2.0             # indices 10-13
      thumb_cmc_flex: 5.0        # index 15
    
    # Compensation parameters by joint index
    compensation:
      thumb_mcp_abd: -50.0        # index 0
      finger_mcp_abd: 0.0         # indices 1-4
      finger_mcp_flex: 0.0        # indices 5-8
      thumb_pip: 0.0             # index 9
      finger_pip: -53.0            # indices 10-13
      thumb_cmc_flex: -15.0        # index 15
    
    # Clamping parameters by joint index (min, max)
    clamping:
      thumb_mcp_abd: [-40.0, 40.0]      # index 0
      finger_mcp_abd: [-25.0, 25.0]     # indices 1-4
      finger_mcp_flex: [-90.0, 90.0]    # indices 5-8
      thumb_pip: [-50.0, 90.0]          # index 9
      finger_pip: [-50.0, 90.0]         # indices 10-13
      default: [-90.0, 90.0]            # default (including index 15)
```

### src/hand_motion_shadowing/config/v2mp.yaml

```yaml
# hand_shadowing_params.yaml
hand_shadowing_node:
  ros__parameters:
    # General parameters
    scale_factor: 2.0
    smoothing_factor: 0.3
    
    # Scaling parameters by joint index
    scaling:
      thumb_cmc_abd: 2.0      # index 0
      thumb_mcp_abd: 5.0        # index 1
      finger_mcp_abd: -2.5         # indices 2-5
      finger_mcp_flex: 1.0       # indices 6-10
      thumb_mcp_flex: -5.0              # index 11
      finger_pip: -2.0           # indices 12-15 
      thumb_cmc_flex: 5.0        # index 16
    
    # Compensation parameters by joint index
    compensation:
      thumb_cmc_abd: -25.0      # index 0
      thumb_mcp_abd: 20.0        # index 1
      index_mcp_abd: 0.0          # index 2
      middle_mcp_abd: 0.0        # index 3
      ring_mcp_abd: 0.0          # index 4
      pinky_mcp_abd: 0.0        # index 5
      finger_mcp_flex: 8.0        # indices 6-10
      thumb_mcp_flex: 0.0             # index 11
      finger_pip: 30.0            # indices 12-15
      thumb_cmc_flex: 35.0        # index 16
    
    # Clamping parameters by joint index (min, max)
    clamping:
      thumb_cmc_abd: [-25.0, 60.0]      # index 0
      thumb_mcp_abd: [-60.0, 40.0]      # index 1
      finger_mcp_abd: [-25.0, 25.0]     # indices 2-4
      pinky_mcp_abd: [-40.0, 25.0]        # index 5
      finger_mcp_flex: [-90.0, 90.0]    # indices 6-10
      thumb_mcp_flex: [-50.0, 90.0]          # index 11
      finger_pip: [-50.0, 90.0]         # indices 12-15
      thumb_cmc_flex: [-85.0, 90.0]     # index 16
      default: [-90.0, 90.0]            # default
```

### src/hand_motion_shadowing/config/v2quest.yaml

```yaml
# hand_shadowing_params.yaml
hand_shadowing_node:
  ros__parameters:
    # General parameters
    scale_factor: 2.0
    smoothing_factor: 0.3
    
    # Scaling parameters by joint index
    scaling:
      thumb_cmc_abd: -3.5      # index 0
      thumb_mcp_abd: 4.5        # index 5
      finger_mcp_abd: -2.5         # indices 1-4
      finger_mcp_flex: 1.4       # indices 6-9
      thumb_mcp_flex: 1.0              # index 10
      finger_pip: 1.5            # indices 11-14 
      thumb_cmc_flex: 2.0        # index 15
    
    # Compensation parameters by joint index
    compensation:
      thumb_cmc_abd: 35.0      # index 0
      thumb_mcp_abd: -40.0        # index 5
      index_mcp_abd: -2.0          # index 1
      middle_mcp_abd: -8.0        # index 2
      ring_mcp_abd: -10.0          # index 3
      pinky_mcp_abd: 20.0        # index 4
      finger_mcp_flex: 0.0        # indices 6-9
      thumb_mcp_flex: 0.0             # index 10
      finger_pip: -50.0            # indices 11-14
      thumb_cmc_flex: -25.0        # index 15
    
    # Clamping parameters by joint index (min, max)
    clamping:
      thumb_cmc_abd: [-25.0, 60.0]      # index 0
      thumb_mcp_abd: [-70.0, 40.0]      # index 5
      finger_mcp_abd: [-25.0, 25.0]     # indices 1-3
      pinky_mcp_abd: [-40.0, 25.0]        # index 4
      finger_mcp_flex: [-90.0, 90.0]    # indices 6-9
      thumb_mcp_flex: [-50.0, 90.0]          # index 10
      finger_pip: [-50.0, 90.0]         # indices 11-14
      thumb_cmc_flex: [-75.0, 75.0]     # index 15
      default: [-90.0, 90.0]            # default
```

### src/hand_motion_shadowing/config/v3quest.yaml

```yaml
# hand_shadowing_params.yaml
hand_shadowing_node:
  ros__parameters:
    # General parameters
    scale_factor: 2.0
    smoothing_factor: 0.3
    
    # Scaling parameters by joint index
    scaling:
      thumb_cmc_flex: -3.0        # index 15
      thumb_cmc_abd: 3.5      # index 0
      thumb_mcp_abd: 2.5        # index 5
      thumb_mcp_flex: -3.0              # index 10
      finger_mcp_abd: -2.5         # indices 1-4
      finger_mcp_flex: 1.4       # indices 6-9
      finger_pip: 1.5            # indices 11-14 

    
    # Compensation parameters by joint index
    compensation:
      thumb_cmc_flex: -20.0        # index 15
      thumb_cmc_abd: 35.0      # index 0
      thumb_mcp_abd: -28.0        # index 5
      thumb_mcp_flex: 30.0             # index 10
      index_mcp_abd: -2.0          # index 1
      middle_mcp_abd: -8.0        # index 2
      ring_mcp_abd: -10.0          # index 3
      pinky_mcp_abd: 20.0        # index 4
      finger_mcp_flex: 0.0        # indices 6-9
      finger_pip: -50.0            # indices 11-14

    
    # Clamping parameters by joint index (min, max)
    clamping:
      thumb_cmc_flex: [-90.0, 10.0]     # index 15
      thumb_cmc_abd: [-90.0, 60.0]      # index 0
      thumb_mcp_abd: [-40.0, 50.0]      # index 5
      thumb_mcp_flex: [-50.0, 90.0]          # index 10
      finger_mcp_abd: [-25.0, 25.0]     # indices 1-3
      pinky_mcp_abd: [-40.0, 25.0]        # index 4
      finger_mcp_flex: [-90.0, 90.0]    # indices 6-9
      finger_pip: [-50.0, 90.0]         # indices 11-14

      default: [-90.0, 90.0]            # default
```

### src/hand_servo_control/config/servo_calibration.yaml

```yaml
channel_0: #TCA
  gain: 0.550
  offset: -5.3
channel_1: #IMA
  gain: 0.601
  offset: -2.8
channel_2: #MMA
  gain: 0.601
  offset: -0.91
channel_3: #RMA
  gain: 0.601
  offset: -2.16
channel_4: #PMA
  gain: 0.601
  offset: 3.0
channel_5: #TMA
  gain: -1.0
  offset: 0.0
channel_6:  #IMF
  gain: 0.783
  offset: -5.6
channel_7:  #MMF
  gain: 0.783
  offset: -7.43
channel_8:  #RMF
  gain: 0.783
  offset: 2.42
channel_9:  #PMF
  gain: 0.783
  offset: -7.2
channel_10:  #TMF
  gain: 0.7868
  offset: -5.4
channel_11:  #IPF
  gain: 0.7868
  offset: -7.7
channel_12:  #MPF
  gain: 0.7868
  offset: 1.3
channel_13:  #RPF
  gain: 0.7868
  offset: 2.0
channel_14: #PPF
  gain: 0.7868
  offset: 1.0
channel_15: #TCF
  gain: 1.0
  offset: -6.0
```

## Python signatures and reward/observation bodies (51 files)


### src/combined_fer_moveit_config/launch/demo.launch.py

```
def generate_launch_description()
```

### src/combined_fer_moveit_config/launch/move_group.launch.py

```
def generate_launch_description()
```

### src/combined_fer_moveit_config/launch/moveit_rviz.launch.py

```
def generate_launch_description()
```

### src/combined_fer_moveit_config/launch/real.launch.py

```
"""Launchfile for the real robot. Does not start Rviz by default."""
def generate_launch_description()
```

### src/combined_fer_moveit_config/launch/rsp.launch.py

```
def generate_launch_description()
```

### src/combined_fer_moveit_config/launch/spawn_controllers.launch.py

```
def generate_launch_description()
```

### src/hand_calibration/hand_calibration/data_collector.py

```
class AprilTagRotationAnalyzer(Node)
    """ROS2 Node to analyze rotation of multiple AprilTags simultaneously.
Takes measurement when /collect_data service is called and computes the
results when /compute service is called."""
    def __init__(self)
    def collect_data_callback(self, request, response)
    def compute_callback(self, request, response)
    def clear_data_callback(self, request, response)
    def _compute_rotation(self, tag_frame)
    def _estimate_rotation_origin(self, tag_frame)
def main(args)
```

### src/hand_calibration/hand_calibration/motor_calibrator.py

```
class MotorCalibrator(Node)
    """ROS2 Node for motor calibration using AprilTag measurements.

This node provides services for different calibration sequences
and stores calibration results for each motor.

Now supports tracking multiple AprilTags simultaneously."""
    def __init__(self)
    def calibrate_phalanx_mcp_abduction_callback(self, request, response)
    def calibrate_phalanx_mcp_flexion_callback(self, request, response)
    def calibrate_phalanx_pip_flexion_callback(self, request, response)
    def calibrate_phalanx_mcp_flexion_with_multi_tags_callback(self, request, response)
    def run_calibration_sequence(self, motor_index, min_angle, max_angle, num_steps, settle_time, sequence_name, tag_frame, additional_motors, hysteresis_clearance, additional_tags)
    def _call_service_with_timeout(self, client, service_name, tag_frames)
    def _set_motor_angle(self, motor_index, angle, additional_motors)
    def _extract_angles(self, message)
    def _create_output_folder(self, sequence_name, motor_index, timestamp)
    def _compute_calibration(self, commanded_angles, measured_angles, motor_index, sequence_name)
    def _plot_calibration(self, gain, offset, inverse_gain, inverse_offset, commanded_angles, commanded_relative, measured_angles, motor_index, sequence_name, output_folder)
    def _save_calibration_data(self, calibration_data, motor_index, sequence_name, output_folder)
def main(args)
```

### src/hand_calibration/test/test_copyright.py

```
def test_copyright()
```

### src/hand_calibration/test/test_flake8.py

```
def test_flake8()
```

### src/hand_calibration/test/test_pep257.py

```
def test_pep257()
```

### src/hand_kinematics/launch/hand_kinematics.launch.py

```
def generate_launch_description()
```

### src/hand_motion_shadowing/hand_motion_shadowing/hand_shadowing_node.py

```
class HandShadowingNode(Node)
    def __init__(self)
    def joint_angles_callback(self, msg)
    def scale_angle_by_index(self, angle, index)
    def compensate_angle_by_index(self, angle, index)
    def clamp_angle_by_index(self, angle, index)
    def convert_rel_to_abs(self, angle, index)
def main(args)
```

### src/hand_motion_shadowing/test/test_copyright.py

```
def test_copyright()
```

### src/hand_motion_shadowing/test/test_flake8.py

```
def test_flake8()
```

### src/hand_motion_shadowing/test/test_pep257.py

```
def test_pep257()
```

### src/hand_rviz/hand_rviz/joint_state_forwarding_node.py

```
class JointStateForwardingNode(Node)
    def __init__(self)
    def dip_from_pip(self, pip_angle)
    def hand_callback(self, msg)
    def publish_joint_state(self)
def main(args)
```

### src/hand_rviz/launch/combined_rviz.launch.py

```
def generate_launch_description()
```

### src/hand_rviz/launch/hand_rviz.launch.py

```
def generate_launch_description()
```

### src/hand_rviz/test/test_copyright.py

```
def test_copyright()
```

### src/hand_rviz/test/test_flake8.py

```
def test_flake8()
```

### src/hand_rviz/test/test_pep257.py

```
def test_pep257()
```

### src/hand_servo_control/hand_servo_control/calibrated_control_gui.py

```
class CalibratedServoControlGUI(Node)
    def __init__(self)
    def load_calibration(self, filename)
    def update_raw_value(self, index)
    def update_calibrated_value(self, index)
    def send_positions(self)
    def reset_raw_sliders(self)
    def reset_calibrated_sliders(self)
    def on_closing(self)
    def spin(self)
def main(args)
```

### src/hand_servo_control/hand_servo_control/calibrated_control_node.py

```
class CalibratedControlNode(Node)
    def __init__(self)
    def load_calibration(self, filename)
    def calibrated_input_callback(self, msg)
def main(args)
```

### src/hand_servo_control/hand_servo_control/calibrated_ik_verification_node.py

```
class CalibratedIKVerificationNode(Node)
    def __init__(self)
    def call_ik_service_async(self, ik_request)
    def handle_reach_service_async(self, request)
    def handle_reach_service(self, request, response)
def main(args)
```

### src/hand_servo_control/hand_servo_control/demo_motion_node.py

```
class DemoMotionNode(Node)
    def __init__(self)
    def home_callback(self, request, response)
    def flex_extend_callback(self, request, response)
    def thumb_up_callback(self, request, response)
    def v_sign_callback(self, request, response)
    def ok_callback(self, request, response)
    def all_extend_callback(self, request, response)
    def all_flex_callback(self, request, response)
    def grip_callback(self, request, response)
    def thumb_sequence_callback(self, request, response)
    def thumb_kapandji_callback(self, request, response)
def main(args)
```

### src/hand_servo_control/hand_servo_control/servo_control_gui.py

```
class ServoControlGUI(Node)
    def __init__(self)
    def update_value(self, index)
    def send_positions(self)
    def reset_sliders(self)
    def on_closing(self)
    def spin(self)
def main(args)
```

### src/hand_servo_control/hand_servo_control/servo_control_node.py

```
class ServoControlNode(Node)
    def __init__(self)
    def handle_set_servo_positions(self, request, response)
    def servo_input_callback(self, msg)
def main(args)
```

### src/hand_servo_control/hand_servo_control/single_servo_control.py

```
class SingleServoNode(Node)
    def __init__(self)
    def handle_set_servo_position(self, request, response)
def main(args)
```

### src/hand_servo_control/test/test_copyright.py

```
def test_copyright()
```

### src/hand_servo_control/test/test_flake8.py

```
def test_flake8()
```

### src/hand_servo_control/test/test_pep257.py

```
def test_pep257()
```

### src/hand_vision/hand_vision/hand_angle_node.py

```
def calculate_angle(a, b, c)
def neutralize_angle(angle)
def project_vector_onto_plane(v, normal)
def calculate_mcp_felxion(origin, joint, distal, palm_normal)
def calculate_abduction_generic(origin, joint, reference, distal)
class HandAngleNode(Node)
    def __init__(self)
    def image_callback(self, msg)
def main(args)
```

### src/hand_vision/hand_vision/hand_angle_quest.py

```
class HandAnglePublisher(Node)
    def __init__(self)
    def timer_callback(self)
    def process_message(self, message)
    def map_received_data_to_order(self, hand_data)
    def publish_hand_angles(self)
def main(args)
```

### src/hand_vision/hand_vision/hand_joint_gui_node.py

```
class JointAngleGUI(Node)
    def __init__(self)
    def joint_angle_callback(self, msg)
    def servo_angle_callback(self, msg)
    def update_gui(self)
    def run(self)
def ros_spin(node)
def main(args)
```

### src/hand_vision/hand_vision/wrist_camera_node.py

```
class WristCameraNode(Node)
    def __init__(self)
    def broadcast_wrist_tf(self)
    def timer_callback(self)
def main(args)
```

### src/hand_vision/hand_vision/wrist_tracker_node.py

```
class WristTrackerNode(Node)
    def __init__(self)
    def get_orientation(self, hand_landmarks)
    def image_callback(self, msg)
    def reset_callback(self, request, response)
def main(args)
```

### src/hand_vision/hand_vision/yolo_node.py

```
class YoloNode(Node)
    """Use Yolo to identify objects in the scene"""
    def __init__(self)
    def yolo_callback(self, image)
def main()
```

### src/hand_vision/test/test_copyright.py

```
def test_copyright()
```

### src/hand_vision/test/test_flake8.py

```
def test_flake8()
```

### src/hand_vision/test/test_pep257.py

```
def test_pep257()
```