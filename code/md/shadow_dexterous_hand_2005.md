# shadow_dexterous_hand_2005

source: https://github.com/shadow-robot/sr_common


commit: 172c3d9c3715ee75eb10dfe4ee57e26a342b4529


## README

# CI Statuses

Check | Status
---|---
Documentation|[![Documentation Status](https://readthedocs.org/projects/shadow-robots-common-packages/badge/?version=latest)](http://shadow-robots-common-packages.readthedocs.org/)
Build|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoidW96cTVPNzRvQTBpVVVaTUlwb3ZXNmRkMUFJd2NQQVpBRHNrLzZIbGk1NUU2bm55OTkzRUxFRnJDZ2ZkSWticVJITzVMUjBWQXRqeFpPQitzY0xaaFEwPSIsIml2UGFyYW1ldGVyU3BlYyI6IlIrNmg4dHZyaC9hZ0VGVGoiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=noetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_sr_common_noetic-devel_install_check/)
Style|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiMmQyRDZsQnlqMUQxRGdnK2lUdzJKT2VqR2pPTXVCbzBRa3J5OCt5WEs1dVE3N3VlOTlQUlhCRTZGUENSNDFIUVcwNlo2Y2VwRXZGdkdqQ2xCTGZuaDBZPSIsIml2UGFyYW1ldGVyU3BlYyI6Imp0Y1pMZzFXU05uUnpoczMiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=noetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_sr_common_noetic-devel_style_check/)
Code Coverage|[<img src="https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiLytJZWxiM0lKZzZyckNISTE0RE5QMjNSaElXRWhocUxzdFUvTFg3UE8wV3g4K3ZTTjFMVlI1bzRUM01SL25SYkZXUWMvaWcwWU4rN3pMVWExQkVvTW9NPSIsIml2UGFyYW1ldGVyU3BlYyI6ImNXd1o4bzFpeGplNUR3S2EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=noetic-devel"/>](https://eu-west-2.console.aws.amazon.com/codesuite/codebuild/projects/auto_sr_common_noetic-devel_code_coverage/)



# Shadow Robot Common packages
This repository contains the bare minimum for communicating with the Shadow Hand from a remote computer: urdf models, messages and services.



## File tree (depth 3, assets pruned)

```
.circleci/
  config.yml
.gitignore
CODEOWNERS
LICENSE
README.md
aws.yml
sr_common/
  CMakeLists.txt
  package.xml
sr_description/
  CMakeLists.txt
  README.md
  blender/
    BlenderHandTutoComments.png
    LICENSE
    README.md
    shadowhand_right.blend
  doc/
    HandInertia.md
  hand/
    config/
    xacro/
  loaders/
    load_hand_model.launch
  mujoco_models/
    README.md
    lh_trajectory_controller.yaml
    rh_trajectory_controller.yaml
    robot_ur10_hand_e_model.xml
    robot_ur10_hand_e_plus_model.xml
    robot_ur10_model.xml
    shared_assets.xml
    shared_assets_left.xml
    shared_assets_ur10.xml
    shared_options.xml
    shared_ur10_options.xml
    sr_hand_e_environment.xml
    sr_hand_e_environment_underactuation_test.xml
    sr_hand_e_left_environment.xml
    sr_hand_e_left_model.xml
    sr_hand_e_left_options.xml
    sr_hand_e_model.xml
    sr_hand_e_options.xml
    sr_hand_e_plus_environment.xml
    sr_hand_e_plus_environment_underactuation_test.xml
    sr_hand_e_plus_left_environment.xml
    sr_hand_e_plus_left_model.xml
    sr_hand_e_plus_model.xml
    sr_ur_environment.xml
    sr_ur_hand_e_environment.xml
    sr_ur_hand_e_plus_environment.xml
    urdfs/
  other/
    xacro/
  package.xml
  robots/
    sr_hand.urdf.xacro
    sr_hand_bimanual.urdf.xacro
  test/
    README.md
    copyright_exclusions.cfg
    test_compatibility.py
    test_hands.rviz
    test_hands.sh
    test_models.launch
    test_models.sh
    test_process_fingers_parameter.xacro
    test_process_sensor_parameters.xacro
    test_sr_description_urdf.cpp
    test_sr_description_urdf.test
sr_robot_msgs/
  CHANGELOG.rst
  CMakeLists.txt
  action/
    Grasp.action
    PlanGrasp.action
  mainpage.dox
  msg/
    ActuatorStatistics.msg
    AuxSpiData.msg
    Biotac.msg
    BiotacAll.msg
    ControlType.msg
    ControllerStatistics.msg
    EthercatDebug.msg
    FromMotorDataType.msg
    GraspArray.msg
    HybridControllerStatus.msg
    JointControllerState.msg
    JointMusclePositionControllerState.msg
    JointMuscleValveControllerCommand.msg
    JointMuscleValveControllerState.msg
    JointStatistics.msg
    MST.msg
    MSTAll.msg
    MechanismStatistics.msg
    MidProxData.msg
    MidProxDataAll.msg
    MotorSystemControls.msg
    ShadowContactStateStamped.msg
    ShadowPST.msg
    Tactile.msg
    TactileArray.msg
    UBI0.msg
    UBI0All.msg
    WrenchArray.msg
    WrenchWithModelGroupName.msg
    cartesian_data.msg
    cartesian_position.msg
    command.msg
    config.msg
    contrlr.msg
    joint.msg
    joints_data.msg
    reverseKinematics.msg
    sendupdate.msg
  package.xml
  srv/
    ChangeControlType.srv
    ChangeMotorSystemControls.srv
    ExecutePlannedTrajectory.srv
    ForceController.srv
    GetFastGraspFromBoundingBox.srv
    GetSegmentedLine.srv
    ListNamedTrajectories.srv
    ManualSelfTest.srv
    NullifyDemand.srv
    PlanNamedTrajectory.srv
    PlanTrajectoryFromList.srv
    PlanTrajectoryFromPrefix.srv
    RobotTeachMode.srv
    SetDebugData.srv
    SetEffortControllerGains.srv
    SetImuScale.srv
    SetMixedPositionVelocityPidGains.srv
    SetPidGains.srv
    SetTeachMode.srv
    SimpleMotorFlasher.srv
    is_hand_occupied.srv
    which_fingers_are_touching.srv
```

## Config files (18)


### .circleci/config.yml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

version: 2
jobs:
  build:
    working_directory: /tmp/repository
    docker:
      - image: public.ecr.aws/shadowrobot/build-tools:focal-noetic
        environment:
          toolset_branch: lint
          server_type: circle
          ros_release_name: noetic
          ubuntu_version_name: focal
          used_modules: check_cache,code_style_check
    steps:
      - checkout
      - run: echo 'export remote_shell_script="https://raw.githubusercontent.com/shadow-robot/sr-build-tools/$toolset_branch/bin/sr-run-ci-build.sh"' >> $BASH_ENV
      - run: wget -O /tmp/oneliner "$( echo "$remote_shell_script" | sed 's/#/%23/g' )"
      - run: chown -R $MY_USERNAME:$MY_USERNAME $CIRCLE_WORKING_DIRECTORY
      - run: chmod 755 /tmp/oneliner
      - run: gosu $MY_USERNAME /tmp/oneliner "$toolset_branch" $server_type $used_modules

      - store_test_results:
          path: test_results

      - store_artifacts:
          path: code_coverage_results

```

### sr_description/hand/config/hand_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_ffj0_position_controller:
  joint: FFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_ffj3_position_controller:
  joint: FFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_ffj4_position_controller:
  joint: FFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lfj0_position_controller:
  joint: LFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lfj3_position_controller:
  joint: LFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lfj4_position_controller:
  joint: LFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lfj5_position_controller:
  joint: LFJ5
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_mfj0_position_controller:
  joint: MFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_mfj3_position_controller:
  joint: MFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_mfj4_position_controller:
  joint: MFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rfj0_position_controller:
  joint: RFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rfj3_position_controller:
  joint: RFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rfj4_position_controller:
  joint: RFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_thj1_position_controller:
  joint: THJ1
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_thj2_position_controller:
  joint: THJ2
  pid:
    d: 0.0
    i: 0.7
    i_clamp: 0.4
    p: 1.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_thj3_position_controller:
  joint: THJ3
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_thj4_position_controller:
  joint: THJ4
  pid:
    d: 0.0
    i: 0.4
    i_clamp: 0.3
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 2.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_thj5_position_controller:
  joint: THJ5
  pid:
    d: 0.05
    i: 0.1
    i_clamp: 0.4
    p: 0.4
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 3.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_wrj1_position_controller:
  joint: WRJ1
  pid:
    d: 1.0
    i: 1.5
    i_clamp: 0.8
    p: 10.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 5.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_wrj2_position_controller:
  joint: WRJ2
  pid:
    d: 0.2
    i: 1.5
    i_clamp: 0.5
    p: 8.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 10.0
  type: sr_mechanism_controllers/SrhJointPositionController

```

### sr_description/hand/config/hand_effort_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

# First Finger (Index finger)
sh_ffj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: FFJ0
  max_force: 10
  friction_deadband: 0
sh_ffj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: FFJ3
  max_force: 10
  friction_deadband: 0
sh_ffj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: FFJ4
  max_force: 10
  friction_deadband: 0


# Middle Finger
sh_mfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: MFJ0
  max_force: 10
  friction_deadband: 0
sh_mfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: MFJ3
  max_force: 10
  friction_deadband: 0
sh_mfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: MFJ4
  max_force: 10
  friction_deadband: 0


# Ring Finger
sh_rfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: RFJ0
  max_force: 10
  friction_deadband: 0
sh_rfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: RFJ3
  max_force: 10
  friction_deadband: 0
sh_rfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: RFJ4
  max_force: 10
  friction_deadband: 0


# Little Finger
sh_lfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: LFJ0
  max_force: 10
  friction_deadband: 0
sh_lfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: LFJ3
  max_force: 10
  friction_deadband: 0
sh_lfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: LFJ4
  max_force: 10
  friction_deadband: 0
sh_lfj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: LFJ5
  max_force: 10
  friction_deadband: 0


# Thumb
sh_thj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: THJ1
  max_force: 10
  friction_deadband: 0
sh_thj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: THJ2
  max_force: 10
  friction_deadband: 0
sh_thj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: THJ3
  max_force: 10
  friction_deadband: 0
sh_thj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: THJ4
  max_force: 10
  friction_deadband: 0
sh_thj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: THJ5
  max_force: 10
  friction_deadband: 0


# Wrist
sh_wrj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: WRJ1
  max_force: 10
  friction_deadband: 0
sh_wrj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: WRJ2
  max_force: 10
  friction_deadband: 0



```

### sr_description/hand/config/hand_mixed_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_ffj0_mixed_position_velocity_controller:
  joint: FFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_ffj3_mixed_position_velocity_controller:
  joint: FFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_ffj4_mixed_position_velocity_controller:
  joint: FFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lfj0_mixed_position_velocity_controller:
  joint: LFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lfj3_mixed_position_velocity_controller:
  joint: LFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lfj4_mixed_position_velocity_controller:
  joint: LFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lfj5_mixed_position_velocity_controller:
  joint: LFJ5
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_mfj0_mixed_position_velocity_controller:
  joint: MFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_mfj3_mixed_position_velocity_controller:
  joint: MFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_mfj4_mixed_position_velocity_controller:
  joint: MFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rfj0_mixed_position_velocity_controller:
  joint: RFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rfj3_mixed_position_velocity_controller:
  joint: RFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rfj4_mixed_position_velocity_controller:
  joint: RFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_thj1_mixed_position_velocity_controller:
  joint: THJ1
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_thj2_mixed_position_velocity_controller:
  joint: THJ2
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_thj3_mixed_position_velocity_controller:
  joint: THJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_thj4_mixed_position_velocity_controller:
  joint: THJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechan
```

### sr_description/hand/config/lh_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_lh_ffj0_position_controller:
  joint: lh_FFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_ffj3_position_controller:
  joint: lh_FFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_ffj4_position_controller:
  joint: lh_FFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_lfj0_position_controller:
  joint: lh_LFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_lfj3_position_controller:
  joint: lh_LFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_lfj4_position_controller:
  joint: lh_LFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_lfj5_position_controller:
  joint: lh_LFJ5
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_mfj0_position_controller:
  joint: lh_MFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_mfj3_position_controller:
  joint: lh_MFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_mfj4_position_controller:
  joint: lh_MFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_rfj0_position_controller:
  joint: lh_RFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_rfj3_position_controller:
  joint: lh_RFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_rfj4_position_controller:
  joint: lh_RFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_thj1_position_controller:
  joint: lh_THJ1
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_thj2_position_controller:
  joint: lh_THJ2
  pid:
    d: 0.0
    i: 0.7
    i_clamp: 0.4
    p: 1.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_thj3_position_controller:
  joint: lh_THJ3
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_thj4_position_controller:
  joint: lh_THJ4
  pid:
    d: 0.0
    i: 0.4
    i_clamp: 0.3
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 2.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_thj5_position_controller:
  joint: lh_THJ5
  pid:
    d: 0.05
    i: 0.1
    i_clamp: 0.4
    p: 0.4
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 3.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_wrj1_position_controller:
  joint: lh_WRJ1
  pid:
    d: 1.0
    i: 1.5
    i_clamp: 0.8
    p: 10.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 5.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_lh_wrj2_position_controller:
  joint: lh_WRJ2
  pid:
    d: 0.2
    i: 1.5
    i_clamp: 0.5
    p: 8.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 10.0
  type: sr_mechanism_controllers/SrhJointPositionController


```

### sr_description/hand/config/lh_effort_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

# First Finger (Index finger)
sh_lh_ffj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_FFJ0
  max_force: 10
  friction_deadband: 0
sh_lh_ffj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_FFJ3
  max_force: 10
  friction_deadband: 0
sh_lh_ffj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_FFJ4
  max_force: 10
  friction_deadband: 0


# Middle Finger
sh_lh_mfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_MFJ0
  max_force: 10
  friction_deadband: 0
sh_lh_mfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_MFJ3
  max_force: 10
  friction_deadband: 0
sh_lh_mfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_MFJ4
  max_force: 10
  friction_deadband: 0


# Ring Finger
sh_lh_rfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_RFJ0
  max_force: 10
  friction_deadband: 0
sh_lh_rfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_RFJ3
  max_force: 10
  friction_deadband: 0
sh_lh_rfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_RFJ4
  max_force: 10
  friction_deadband: 0


# Little Finger
sh_lh_lfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_LFJ0
  max_force: 10
  friction_deadband: 0
sh_lh_lfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_LFJ3
  max_force: 10
  friction_deadband: 0
sh_lh_lfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_LFJ4
  max_force: 10
  friction_deadband: 0
sh_lh_lfj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_LFJ5
  max_force: 10
  friction_deadband: 0


# Thumb
sh_lh_thj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_THJ1
  max_force: 10
  friction_deadband: 0
sh_lh_thj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_THJ2
  max_force: 10
  friction_deadband: 0
sh_lh_thj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_THJ3
  max_force: 10
  friction_deadband: 0
sh_lh_thj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_THJ4
  max_force: 10
  friction_deadband: 0
sh_lh_thj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_THJ5
  max_force: 10
  friction_deadband: 0


# Wrist
sh_lh_wrj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_WRJ1
  max_force: 10
  friction_deadband: 0
sh_lh_wrj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: lh_WRJ2
  max_force: 10
  friction_deadband: 0



```

### sr_description/hand/config/lh_grasp_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_grasp_controller:
  gains:
    lh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ5:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ3:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    lh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
    lh_WRJ1:
      d: 1.0
      i: 1.5
      i_clamp: 0.8
      p: 10.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 5.0
    lh_WRJ2:
      d: 0.2
      i: 1.5
      i_clamp: 0.5
      p: 8.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 10.0
      
  type: sr_grasp_controllers/SrhGraspController
  joints: [lh_FFJ0, lh_FFJ3, lh_FFJ4, lh_LFJ0, lh_LFJ3, lh_LFJ4, lh_LFJ5, lh_MFJ0, lh_MFJ3, lh_MFJ4, lh_RFJ0, lh_RFJ3, lh_RFJ4, lh_THJ1, lh_THJ2, lh_THJ3, lh_THJ4, lh_THJ5, lh_WRJ1, lh_WRJ2]

```

### sr_description/hand/config/lh_hybrid_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_lh_hybrid_controller:
  gains:
    lh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_LFJ5:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ3:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    lh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
    lh_WRJ1:
      d: 1.0
      i: 1.5
      i_clamp: 0.8
      p: 10.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 5.0
    lh_WRJ2:
      d: 0.2
      i: 1.5
      i_clamp: 0.5
      p: 8.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 10.0
      
  type: sr_hybrid_controllers/SrHybridController
  joints: [lh_FFJ0, lh_FFJ3, lh_FFJ4, lh_LFJ0, lh_LFJ3, lh_LFJ4, lh_LFJ5, lh_MFJ0, lh_MFJ3, lh_MFJ4, lh_RFJ0, lh_RFJ3, lh_RFJ4, lh_THJ1, lh_THJ2, lh_THJ3, lh_THJ4, lh_THJ5, lh_WRJ1, lh_WRJ2]
  torque_to_pwm_scaling: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
```

### sr_description/hand/config/lh_lite_grasp_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_grasp_controller:
  gains:
    lh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    lh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    lh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
      
  type: sr_grasp_controllers/SrhGraspController
  joints: [lh_FFJ0, lh_FFJ3, lh_FFJ4, lh_MFJ0, lh_MFJ3, lh_MFJ4, lh_RFJ0, lh_RFJ3, lh_RFJ4, lh_THJ1, lh_THJ2, lh_THJ4, lh_THJ5]

```

### sr_description/hand/config/lh_mixed_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_lh_ffj0_mixed_position_velocity_controller:
  joint: FFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_ffj3_mixed_position_velocity_controller:
  joint: FFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_ffj4_mixed_position_velocity_controller:
  joint: FFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_lfj0_mixed_position_velocity_controller:
  joint: LFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_lfj3_mixed_position_velocity_controller:
  joint: LFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_lfj4_mixed_position_velocity_controller:
  joint: LFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_lfj5_mixed_position_velocity_controller:
  joint: LFJ5
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_mfj0_mixed_position_velocity_controller:
  joint: MFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_mfj3_mixed_position_velocity_controller:
  joint: MFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_mfj4_mixed_position_velocity_controller:
  joint: MFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_rfj0_mixed_position_velocity_controller:
  joint: RFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_rfj3_mixed_position_velocity_controller:
  joint: RFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_rfj4_mixed_position_velocity_controller:
  joint: RFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_thj1_mixed_position_velocity_controller:
  joint: THJ1
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_thj2_mixed_position_velocity_controller:
  joint: THJ2
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_thj3_mixed_position_velocity_controller:
  joint: THJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_lh_thj4_mixed_position_velocity_controller:
  joint: THJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p
```

### sr_description/hand/config/lh_variable_pid_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_lh_ffj0_variable_position_controller:
  joint: lh_FFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_ffj3_variable_position_controller:
  joint: lh_FFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_ffj4_variable_position_controller:
  joint: lh_FFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_lfj0_variable_position_controller:
  joint: lh_LFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_lfj3_variable_position_controller:
  joint: lh_LFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_lfj4_variable_position_controller:
  joint: lh_LFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_lfj5_variable_position_controller:
  joint: lh_LFJ5
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_mfj0_variable_position_controller:
  joint: lh_MFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_mfj3_variable_position_controller:
  joint: lh_MFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_mfj4_variable_position_controller:
  joint: lh_MFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_rfj0_variable_position_controller:
  joint: lh_RFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_rfj3_variable_position_controller:
  joint: lh_RFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_rfj4_variable_position_controller:
  joint: lh_RFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_thj1_variable_position_controller:
  joint: lh_THJ1
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_thj2_variable_position_controller:
  joint: lh_THJ2
  pid:
    d: 0.0
    i: 0.7
    i_clamp: 0.4
    p: 1.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_thj3_variable_position_controller:
  joint: lh_THJ3
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_thj4_variable_position_controller:
  joint: lh_THJ4
  pid:
    d: 0.0
    i: 0.4
    i_clamp: 0.3
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 2.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_thj5_variable_position_controller:
  joint: lh_THJ5
  pid:
    d: 0.05
    i: 0.1
    i_clamp: 0.4
    p: 0.4
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 3.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_wrj1_variable_position_controller:
  joint: lh_WRJ1
  pid:
    d: 1.0
    i: 1.5
    i_clamp: 0.8
    p: 10.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 5.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_lh_wrj2_variable_position_controller:
  joint: lh_WRJ2
  pid:
    d: 0.2
    i: 1.5
    i_clamp: 0.5
    p: 8.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 10.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

```

### sr_description/hand/config/rh_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_ffj0_position_controller:
  joint: rh_FFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_ffj3_position_controller:
  joint: rh_FFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_ffj4_position_controller:
  joint: rh_FFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_lfj0_position_controller:
  joint: rh_LFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_lfj3_position_controller:
  joint: rh_LFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_lfj4_position_controller:
  joint: rh_LFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_lfj5_position_controller:
  joint: rh_LFJ5
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_mfj0_position_controller:
  joint: rh_MFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_mfj3_position_controller:
  joint: rh_MFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_mfj4_position_controller:
  joint: rh_MFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_rfj0_position_controller:
  joint: rh_RFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_rfj3_position_controller:
  joint: rh_RFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_rfj4_position_controller:
  joint: rh_RFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_thj1_position_controller:
  joint: rh_THJ1
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_thj2_position_controller:
  joint: rh_THJ2
  pid:
    d: 0.0
    i: 0.7
    i_clamp: 0.4
    p: 1.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_thj3_position_controller:
  joint: rh_THJ3
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_thj4_position_controller:
  joint: rh_THJ4
  pid:
    d: 0.0
    i: 0.4
    i_clamp: 0.3
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 2.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_thj5_position_controller:
  joint: rh_THJ5
  pid:
    d: 0.05
    i: 0.1
    i_clamp: 0.4
    p: 0.4
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 3.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_wrj1_position_controller:
  joint: rh_WRJ1
  pid:
    d: 1.0
    i: 1.5
    i_clamp: 0.8
    p: 10.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 5.0
  type: sr_mechanism_controllers/SrhJointPositionController

sh_rh_wrj2_position_controller:
  joint: rh_WRJ2
  pid:
    d: 0.2
    i: 1.5
    i_clamp: 0.5
    p: 8.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 10.0
  type: sr_mechanism_controllers/SrhJointPositionController

```

### sr_description/hand/config/rh_effort_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

# First Finger (Index finger)
sh_rh_ffj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_FFJ0
  max_force: 10
  friction_deadband: 0
sh_rh_ffj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_FFJ3
  max_force: 10
  friction_deadband: 0
sh_rh_ffj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_FFJ4
  max_force: 10
  friction_deadband: 0


# Middle Finger
sh_rh_mfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_MFJ0
  max_force: 10
  friction_deadband: 0
sh_rh_mfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_MFJ3
  max_force: 10
  friction_deadband: 0
sh_rh_mfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_MFJ4
  max_force: 10
  friction_deadband: 0


# Ring Finger
sh_rh_rfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_RFJ0
  max_force: 10
  friction_deadband: 0
sh_rh_rfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_RFJ3
  max_force: 10
  friction_deadband: 0
sh_rh_rfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_RFJ4
  max_force: 10
  friction_deadband: 0


# Little Finger
sh_rh_lfj0_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_LFJ0
  max_force: 10
  friction_deadband: 0
sh_rh_lfj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_LFJ3
  max_force: 10
  friction_deadband: 0
sh_rh_lfj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_LFJ4
  max_force: 10
  friction_deadband: 0
sh_rh_lfj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_LFJ5
  max_force: 10
  friction_deadband: 0


# Thumb
sh_rh_thj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_THJ1
  max_force: 10
  friction_deadband: 0
sh_rh_thj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_THJ2
  max_force: 10
  friction_deadband: 0
sh_rh_thj3_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_THJ3
  max_force: 10
  friction_deadband: 0
sh_rh_thj4_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_THJ4
  max_force: 10
  friction_deadband: 0
sh_rh_thj5_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_THJ5
  max_force: 10
  friction_deadband: 0


# Wrist
sh_rh_wrj1_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_WRJ1
  max_force: 10
  friction_deadband: 0
sh_rh_wrj2_effort_controller:
  type: sr_mechanism_controllers/SrhEffortJointController
  joint: rh_WRJ2
  max_force: 10
  friction_deadband: 0



```

### sr_description/hand/config/rh_grasp_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_grasp_controller:
  gains:
    rh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ5:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ3:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    rh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
    rh_WRJ1:
      d: 1.0
      i: 1.5
      i_clamp: 0.8
      p: 10.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 5.0
    rh_WRJ2:
      d: 0.2
      i: 1.5
      i_clamp: 0.5
      p: 8.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 10.0
      
  type: sr_grasp_controllers/SrhGraspController
  joints: [rh_FFJ0, rh_FFJ3, rh_FFJ4, rh_LFJ0, rh_LFJ3, rh_LFJ4, rh_LFJ5, rh_MFJ0, rh_MFJ3, rh_MFJ4, rh_RFJ0, rh_RFJ3, rh_RFJ4, rh_THJ1, rh_THJ2, rh_THJ3, rh_THJ4, rh_THJ5, rh_WRJ1, rh_WRJ2]

```

### sr_description/hand/config/rh_hybrid_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_hybrid_controller:
  gains:
    rh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_LFJ5:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ3:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    rh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
    rh_WRJ1:
      d: 1.0
      i: 1.5
      i_clamp: 0.8
      p: 10.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 5.0
    rh_WRJ2:
      d: 0.2
      i: 1.5
      i_clamp: 0.5
      p: 8.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 10.0
      
  type: sr_hybrid_controllers/SrHybridController
  joints: [rh_FFJ0, rh_FFJ3, rh_FFJ4, rh_LFJ0, rh_LFJ3, rh_LFJ4, rh_LFJ5, rh_MFJ0, rh_MFJ3, rh_MFJ4, rh_RFJ0, rh_RFJ3, rh_RFJ4, rh_THJ1, rh_THJ2, rh_THJ3, rh_THJ4, rh_THJ5, rh_WRJ1, rh_WRJ2]
  torque_to_pwm_scaling: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
```

### sr_description/hand/config/rh_lite_grasp_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_grasp_controller:
  gains:
    rh_FFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_FFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_MFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ0:
      d: 0.005
      i: 0.1
      i_clamp: 0.05
      p: 0.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ3:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_RFJ4:
      d: 0.05
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ1:
      d: 0.0
      i: 0.2
      i_clamp: 0.2
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ2:
      d: 0.0
      i: 0.7
      i_clamp: 0.4
      p: 1.5
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 1.0
    rh_THJ4:
      d: 0.0
      i: 0.4
      i_clamp: 0.3
      p: 1.0
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 2.0
    rh_THJ5:
      d: 0.05
      i: 0.1
      i_clamp: 0.4
      p: 0.4
      position_deadband: 0.0
      friction_deadband: 0.0
      max_force: 3.0
      
  type: sr_grasp_controllers/SrhGraspController
  joints: [rh_FFJ0, rh_FFJ3, rh_FFJ4, rh_MFJ0, rh_MFJ3, rh_MFJ4, rh_RFJ0, rh_RFJ3, rh_RFJ4, rh_THJ1, rh_THJ2, rh_THJ4, rh_THJ5]

```

### sr_description/hand/config/rh_mixed_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_ffj0_mixed_position_velocity_controller:
  joint: FFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_ffj3_mixed_position_velocity_controller:
  joint: FFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_ffj4_mixed_position_velocity_controller:
  joint: FFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_lfj0_mixed_position_velocity_controller:
  joint: LFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_lfj3_mixed_position_velocity_controller:
  joint: LFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_lfj4_mixed_position_velocity_controller:
  joint: LFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_lfj5_mixed_position_velocity_controller:
  joint: LFJ5
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_mfj0_mixed_position_velocity_controller:
  joint: MFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_mfj3_mixed_position_velocity_controller:
  joint: MFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_mfj4_mixed_position_velocity_controller:
  joint: MFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_rfj0_mixed_position_velocity_controller:
  joint: RFJ0
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_rfj3_mixed_position_velocity_controller:
  joint: RFJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_rfj4_mixed_position_velocity_controller:
  joint: RFJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -2.3
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_thj1_mixed_position_velocity_controller:
  joint: THJ1
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_thj2_mixed_position_velocity_controller:
  joint: THJ2
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_thj3_mixed_position_velocity_controller:
  joint: THJ3
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p: -3.0
    position_deadband: 0.0
  type: sr_mechanism_controllers/SrhMixedPositionVelocityJointController
  velocity_pid:
    d: 0.0
    friction_deadband: 100.0
    i: 0.0
    i_clamp: 0.0
    max_force: 10.0
    p: -0.2

sh_rh_thj4_mixed_position_velocity_controller:
  joint: THJ4
  position_pid:
    d: 0.0
    i: 0.0
    i_clamp: 0.1
    max_velocity: 1.5
    min_velocity: -1.5
    p
```

### sr_description/hand/config/rh_variable_pid_controller_gazebo.yaml

```yaml
# Software License Agreement (BSD License)
# Copyright © 2022 belongs to Shadow Robot Company Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. Neither the name of Shadow Robot Company Ltd nor the names of its contributors
#      may be used to endorse or promote products derived from this software without
#      specific prior written permission.
#
# This software is provided by Shadow Robot Company Ltd "as is" and any express
# or implied warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed. In no event
# shall the copyright holder be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business interruption)
# however caused and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of the use of this
# software, even if advised of the possibility of such damage.

sh_rh_ffj0_variable_position_controller:
  joint: rh_FFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_ffj3_variable_position_controller:
  joint: rh_FFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_ffj4_variable_position_controller:
  joint: rh_FFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_lfj0_variable_position_controller:
  joint: rh_LFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_lfj3_variable_position_controller:
  joint: rh_LFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_lfj4_variable_position_controller:
  joint: rh_LFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_lfj5_variable_position_controller:
  joint: rh_LFJ5
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_mfj0_variable_position_controller:
  joint: rh_MFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_mfj3_variable_position_controller:
  joint: rh_MFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_mfj4_variable_position_controller:
  joint: rh_MFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_rfj0_variable_position_controller:
  joint: rh_RFJ0
  pid:
    d: 0.005
    i: 0.1
    i_clamp: 0.05
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_rfj3_variable_position_controller:
  joint: rh_RFJ3
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_rfj4_variable_position_controller:
  joint: rh_RFJ4
  pid:
    d: 0.05
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_thj1_variable_position_controller:
  joint: rh_THJ1
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_thj2_variable_position_controller:
  joint: rh_THJ2
  pid:
    d: 0.0
    i: 0.7
    i_clamp: 0.4
    p: 1.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_thj3_variable_position_controller:
  joint: rh_THJ3
  pid:
    d: 0.0
    i: 0.2
    i_clamp: 0.2
    p: 0.5
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 1.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_thj4_variable_position_controller:
  joint: rh_THJ4
  pid:
    d: 0.0
    i: 0.4
    i_clamp: 0.3
    p: 1.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 2.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_thj5_variable_position_controller:
  joint: rh_THJ5
  pid:
    d: 0.05
    i: 0.1
    i_clamp: 0.4
    p: 0.4
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 3.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_wrj1_variable_position_controller:
  joint: rh_WRJ1
  pid:
    d: 1.0
    i: 1.5
    i_clamp: 0.8
    p: 10.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 5.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController

sh_rh_wrj2_variable_position_controller:
  joint: rh_WRJ2
  pid:
    d: 0.2
    i: 1.5
    i_clamp: 0.5
    p: 8.0
    position_deadband: 0.0
    friction_deadband: 0.0
    max_force: 10.0
  type: sr_mechanism_controllers/SrhJointVariablePidPositionController


```

## Python signatures and reward/observation bodies (0 files)
