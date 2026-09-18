# allegro_hand_v4_2016

source: https://github.com/simlabrobotics/allegro_hand_ros_v4


commit: b19b18ea130c4fbe343f2c178eec6cb55186a4ac


## README

# allegro_hand_ros

Allegro Hand ROS
================================

This is the official release to control Allegro Hand with ROS Kinetic.
Mostly, it is based on the old release of Allegro Hand ros package and the interfaces 
and controllers have been improved and rewritten much by Felix Duballet from EPFL. 
Thank you for the contribution.

You can find old release of the [hand ros package][1].
[1]: https://github.com/simlabrobotics/allegro_hand_ros_v4

It improves significantly upon the old release, simplifies the launch file structure,
updates the package/node names to
have a more consistent structure, improves the build process by creating a
common driver, introduces an AllegroNode C++ class that reduces the amount of
duplicated code. It also provides a python library that can control the hand
directly.

It also provides the BHand library directly in this package (including both
32-bit and 64-bit versions, though 32-bit systems will need to update the
symlink manually).

At this point no effort has been made to be backwards compatible. Some of the
non-compatible changes between the two version are:

 - Put all of the controllers into one *package* (allegro_hand_controllers) and
   made each controller a different node (allegro_node_XXXX): grasp, pd, velsat,
   and sim.
 - Single launch file with arguments instead of multiple launch files with
   repeated code.
 - Both the parameter and description files are now ROS packages, so that
   `rospack find` works with them.
 - These packages will likely not work with pre-hydro versions (only tested on
   ROS Kinetic so far, please let me know if this works on other distributions).
 - Added a torque controller (from @nisommer).
 - Added a 'simulated' pass-through hand controller that sets the joint state to
   the desired joint state.

Launch file instructions:
------------------------

There is now a single file,
[allegro_hand.launch](allegro_hand_controllers/launch/allegro_hand.launch)
that starts the hand. It takes many arguments, but at a minimum you must specify
the handedness:

    roslaunch allegro_hand_controllers allegro_hand.launch HAND:=right

Optional (recommended) arguments:

          NUM:=0|1|...
          ZEROS:=/path/to/zeros_file.yaml
          CONTROLLER:=grasp|pd|velsat|torque|sim
          RESPAWN:=true|false   Respawn controller if it dies.
          KEYBOARD:=true|false  (default is true)
          AUTO_CAN:=true|false  (default is true)
          CAN_DEVICE:=/dev/pcanusb1 | /dev/pcanusbNNN  (ls -l /dev/pcan* to see open CAN devices)
          VISUALIZE:=true|false  (Launch rviz)
          JSP_GUI:=true|false  (show the joint_state_publisher for *desired* joint angles)

Note on `AUTO_CAN`: There is a nice script `detect_pcan.py` which automatically
finds an open `/dev/pcanusb` file. If instead you specify the can device
manually (`CAN_DEVICE:=/dev/pcanusbN`), make sure you *also* specify
`AUTO_CAN:=false`. Obviously, automatic detection cannot work with two hands.

The second launch file is for visualization, it is included in
`allegro_hand.launch` if `VISUALIZE:=true`. Otherwise, it can be useful to run
it separately (with `VISUALIZE:=false`), for example if you want to start rviz separately
(and keep it running):

    roslaunch allegro_hand_controllers allegro_viz.launch HAND:=right

Note that you should also specify the hand `NUM` parameter in the viz launch if
the hand number is not zero.

Packages
--------

 * **allegro_hand** A python client that enables direct control of the hand in
                    python code.
 * **allegro_hand_driver** Driver for talking with the allegro hand.
 * **allegro_hand_controllers** Different nodes that actually control the hand.
 The AllegroNode class handles all the generic driver comms, each class then
 implements `computeDesiredTorque` differently (and can have various topic
 subscribers):
   * grasp: Apply various pre-defined grasps, including gravity compensation.
   * pd: Joint space control: save and hold positions.
   * velsat: velocity saturation joint space control (supposedly experimental)
   * torque: Direct torque control.
   * sim: Just pass desired joint states through as current joint states.
 * **allegro_hand_description** xacro descriptions for the kinematics of the
     hand, rviz configuration and meshes.
 * **allegro_hand_keyboard** Node that sends the commanded grasps. All commands
     are available with the grasp controller, only some are available with the
     other controllers.
 * **allegro_hand_parameters** All necessary parameters for loading the hand:
   * gains_pd.yaml: Controller gains for PD controller.
   * gains_velSat.yaml: Controller gains and parameters for velocity saturation
           controller.
   * initial_position.yaml: Home position for the hand.
   * zero.yaml: Offset and servo directions for each of the 16 joints, and some
           meta information about the hand.
   * zero_files/ Zero files for all hands.
 * **bhand** Library files for the predefined grasps, available in 32 and 64 bit
     versions. 64 bit by default, update symlink for 32 bit.

Note on polling (from Wonik Robotics): The preferred sampling method is utilizing the
Hand's own real time clock running @ 333Hz by polling the CAN communication
(polling = true, default). In fact, ROS's interrupt/sleep combination might
cause instability in CAN communication resulting unstable hand motions.


Useful Links
------------

 * [Allegro Hand wiki](http://wiki.wonikrobotics/AllegroHand/wiki).
 * [ROS wiki for original package](http://www.ros.org/wiki/allegro_hand_ros).


Controlling More Than One Hand
------------------------------

When running more than one hand using ROS, you must specify the number of the
hand when launching.

    roslaunch allegro_hand.launch HAND:=right ZEROS:=parameters/zero0.yaml NUM:=0 CAN_DEVICE:=/dev/pcan0 AUTO_CAN:=false

    roslaunch allegro_hand.launch HAND:=left  ZEROS:=parameters/zero1.yaml NUM:=1 CAN_DEVICE:=/dev/pcan1 AUTO_CAN:=false


Known Issues:
-------------

While all parameters defining the hand's motor/encoder directions and offsets
fall under the enumerated "allegroHand_#" namespaces, the parameter
"robot_description" defining the kinematic structure and joint limits remains
global. When launching a second hand, this parameter is overwritten. I have yet
to find a way to have a separate enumerated "robot_decription" parameter for
each hand. If you have any info on this, please advise.


Installing the PCAN driver
--------------------------

Before using the hand, you must install the pcan drivers. This assumes you have
a peak-systems pcan to usb adapter.

1. Install these packages

    sudo apt-get install libpopt-dev ros-kinetic-libpcan

2. Download latest drivers: http://www.peak-system.com/fileadmin/media/linux/index.htm#download

Install the drivers:

    make clean; make NET=NO_NETDEV_SUPPORT
    sudo make install
    sudo /sbin/modprobe pcan

Test that the interface is installed properly with:

     cat /proc/pcan

You should see some stuff streaming.

When the hand is connected, you should see pcanusb0 or pcanusb1 in the list of
available interfaces:

    ls -l /dev/pcan*

If you do not see any available files, you may need to run:

    sudo ./driver/pcan_make_devices 2

from the downloaded pcan folder: this theoretically creates the devices files if
the system has not done it automatically.

3. Build the sources

    catkin_make
    source devel/setup.bash

4. quick start
    cd src/allegro_hand_controllers/launch
    roslaunch allegro_hand.launch HAND:=right



## File tree (depth 3, assets pruned)

```
LICENSE
README.md
src/
  CMakeLists.txt
  allegro_hand/
    CMakeLists.txt
    launch/
    package.xml
    src/
  allegro_hand_controllers/
    CMakeLists.txt
    launch/
    package.xml
    src/
  allegro_hand_description/
    CMakeLists.txt
    README.txt
    allegro_hand_config.rviz
    allegro_hand_config.vcg
    allegro_hand_description_left.urdf
    allegro_hand_description_left.xacro
    allegro_hand_description_right.urdf
    allegro_hand_description_right.xacro
    allegro_hand_description_right_.urdf
    allegro_hand_left.pdf
    allegro_hand_right.pdf
    build_desc.sh
    package.xml
    scripts/
    temp/
    worlds/
  allegro_hand_driver/
    CMakeLists.txt
    include/
    package.xml
    src/
  allegro_hand_keyboard/
    CMakeLists.txt
    package.xml
    src/
  allegro_hand_parameters/
    CMakeLists.txt
    gains_pd.yaml
    gains_velSat.yaml
    initial_position.yaml
    package.xml
    temp/
    zero.yaml
    zero_files/
  bhand/
    CMakeLists.txt
    include/
    lib/
    libBHand_32/
    libBHand_64/
    package.xml
```

## Config files (32)


### src/allegro_hand_parameters/gains_pd.yaml

```yaml
# Gains for the Proportional-Derivative Joint Space Controller
# included with the Allegro Hand ROS Package.
# P and D gains for each of the 16 joints.

# proportial
gains_pd:
 p:
  j00: 4000.0
  j01: 4000.0
  j02: 4000.0
  j03: 4000.0
  j10: 4000.0
  j11: 4000.0
  j12: 4000.0
  j13: 4000.0
  j20: 4000.0
  j21: 4000.0
  j22: 4000.0
  j23: 4000.0
  j30: 4000.0
  j31: 4000.0
  j32: 4000.0
  j33: 4000.0
#derivative
 d:
  j00: 150.0
  j01: 200.0
  j02: 150.0
  j03: 150.0
  j10: 150.0
  j11: 200.0
  j12: 150.0
  j13: 150.0
  j20: 150.0
  j21: 200.0
  j22: 150.0
  j23: 150.0
  j30: 300.0
  j31: 200.0
  j32: 200.0
  j33: 150.0

```

### src/allegro_hand_parameters/gains_velSat.yaml

```yaml
# Gains for the Velocity Saturation Joint Space Controller
# included with the Allegro Hand ROS Package.
# P and D gains and Max Velocity for each of the 16 joints.

# proportial
gains_velSat:
 p:
  j00: 1200.0
  j01: 1200.0
  j02: 1200.0
  j03: 1200.0
  j10: 1200.0
  j11: 1200.0
  j12: 1200.0
  j13: 1200.0
  j20: 1200.0
  j21: 1200.0
  j22: 1200.0
  j23: 1200.0
  j30: 1200.0
  j31: 1200.0
  j32: 1200.0
  j33: 1200.0
#derivative
 d:
  j00: 140.0
  j01: 140.0
  j02: 140.0
  j03: 140.0
  j10: 140.0
  j11: 140.0
  j12: 140.0
  j13: 140.0
  j20: 140.0
  j21: 140.0
  j22: 140.0
  j23: 140.0
  j30: 140.0
  j31: 140.0
  j32: 140.0
  j33: 140.0
#max velocity
 v_max:
  j00: 10.0
  j01: 10.0
  j02: 10.0
  j03: 10.0
  j10: 10.0
  j11: 10.0
  j12: 10.0
  j13: 10.0
  j20: 10.0
  j21: 10.0
  j22: 10.0
  j23: 10.0
  j30: 10.0
  j31: 10.0
  j32: 10.0
  j33: 10.0

```

### src/allegro_hand_parameters/initial_position.yaml

```yaml
# Initial Position used in the PD and Velocity Saturation Joint Space Controllers

# Home Position
initial_position:
 j00: 0.0
 j01: -10.0
 j02: 45.0
 j03: 45.0
 j10: 0.0
 j11: -10.0
 j12: 45.0
 j13: 45.0
 j20: 5.0
 j21: -5.0
 j22: 50.0
 j23: 45.0
 j30: 60.0
 j31: 25.0
 j32: 15.0
 j33: 45.0

```

### src/allegro_hand_parameters/temp/77R.yaml

```yaml
#SAH040A077R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH040A077R'
 version: 3.0
 input_voltage: 8

zero:
 encoder_offset:
  j00: 1406
  j01: -75
  j02: -1185
  j03: -16272
  j10: 1587
  j11: 833
  j12: -1552
  j13: -18562
  j20: 249
  j21: -618
  j22: -21
  j23: -1298
  j30: 234
  j31: -434
  j32: -349
  j33: 551

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/temp/78R.yaml

```yaml
#SAH030M078R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030M078R'
 version: 3.0
 input_voltage: 8

zero:
 encoder_offset:
  j00: 1347
  j01: -17054
  j02: -391
  j03: -17072
  j10: -1118
  j11: -15978
  j12: -17550
  j13: -17216
  j20: 1774
  j21: -18041
  j22: -13
  j23: -1391
  j30: 628
  j31: 1224
  j32: -17068
  j33: -887

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/temp/zero_hyundai.yaml

```yaml
#SAH030H061L
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Left'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030H061L'
 version: v3.0

zero:
 encoder_offset:
  j00: -7760
  j01: -6296
  j02: 2229
  j03: -5175
  j10: -9394
  j11: 4227
  j12: -4200
  j13: -6261
  j20: -7646
  j21: -10136
  j22: -3993
  j23: -10548
  j30: -14
  j31: 738
  j32: 45
  j33: -376

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/temp/zero_telexistence.yaml

```yaml
#SAH030C034R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030C034R'
 version: 3.0
 input_voltage: 8

zero:
 encoder_offset:
  j00: -12
  j01: -16798
  j02: -16135
  j03: -17314
  j10: 2193
  j11: -959
  j12: -930
  j13: -343
  j20: -782
  j21: -16616
  j22: -16170
  j23: -564
  j30: -1338
  j31: -506
  j32: -217
  j33: 798

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/temp/zero_test.yaml

```yaml
#SAH030C034R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030C034R'
 version: 3.0
 input_voltage: 8

zero:
 encoder_offset:
  j00: 867
  j01: -106
  j02: -643
  j03: 39
  j10: 146
  j11: -1797
  j12: -930
  j13: 469
  j20: 5070
  j21: 1266
  j22: -65
  j23: 616
  j30: 424
  j31: 672
  j32: -526
  j33: 424

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero.yaml

```yaml
#SAH030C034R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH040A080R'
 version: 4.0
 input_voltage: 12

```

### src/allegro_hand_parameters/zero_files/zero_SAH01010002.yaml

```yaml
#SAH01010002
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH01010002'
 version: 1.0

zero:
 encoder_offset:
  j00: -1105
  j01: -65301
  j02: -412
  j03: 832
  j10: 327
  j11: -66828
  j12: 44
  j13: -436
  j20: 758
  j21: -65920
  j22: -42
  j23: -180
  j30: 412
  j31: -266
  j32: -64487
  j33: -65882

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: +1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: -1
  j13: -1
  j20: -1
  j21: +1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH01020003.yaml

```yaml
#SAH01020003
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH01020003'
 version: 1.0

zero:
 encoder_offset:
  j00: -156
  j01: -66041
  j02: -263
  j03: 1209
  j10: 708
  j11: -65956
  j12: 88
  j13: 931
  j20: -733
  j21: -66254
  j22: 655
  j23: 419
  j30: -64973
  j31: -66524
  j32: 1265
  j33: 1187

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH01020004.yaml

```yaml
#SAH01020004
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH01020004'
 version: 2.0

zero:
 encoder_offset:
  j00: -652
  j01: 48
  j02: 85
  j03: -15
  j10: -660
  j11: -399
  j12: -634
  j13: 4
  j20: 744
  j21: 22
  j22: 463
  j23: 205
  j30: 232
  j31: 399
  j32: -273
  j33: 851

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH01020005.yaml

```yaml
#SAH01020005
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH01020005'
 version: 1.0

zero:
 encoder_offset:
  j00: 660
  j01: -67254
  j02: 931
  j03: 111
  j10: 345
  j11: -65017
  j12: 484
  j13: 920
  j20: 207
  j21: -65201
  j22: 835
  j23: 153
  j30: -64795
  j31: -64502
  j32: 707
  j33: 457

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH01020006.yaml

```yaml
#SAH01020006
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH01020006'
 version: 1.0

zero:
 encoder_offset:
  j00: 1465
  j01: -65230
  j02: 13
  j03: 697
  j10: 1251
  j11: -66019
  j12: 420
  j13: -413
  j20: 377
  j21: -63587
  j22: 1017
  j23: -50
  j30: 13
  j31: 1294
  j32: -65652
  j33: -66046

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AL011.yaml

```yaml
#SAH020AL011
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AL011'
 version: 2.0

zero:
 encoder_offset:
  j00: 438
  j01: -66996
  j02: 655
  j03: 782
  j10: 1092
  j11: -67847
  j12: 1629
  j13: 862
  j20: -491
  j21: -66084
  j22: -775
  j23: 1535
  j30: -67383
  j31: -66622
  j32: -65673
  j33: -66609

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AR007.yaml

```yaml
#SAH020AR007
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AR007'
 version: 2.0

zero:
 encoder_offset:
  j00: -105
  j01: -66036
  j02: 601
  j03: 121
  j10: 1908
  j11: -65690
  j12: 1269
  j13: 1897
  j20: 1034
  j21: -67904
  j22: 423
  j23: -240
  j30: 213
  j31: 492
  j32: -63888
  j33: -63908

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AR008.yaml

```yaml
#SAH020AR008
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AR008'
 version: 2.0

zero:
 encoder_offset:
  j00: 644
  j01: -67130
  j02: 638
  j03: -204
  j10: -145
  j11: -66826
  j12: 629
  j13: 199
  j20: 396
  j21: -65107
  j22: -330
  j23: 1171
  j30: -1025
  j31: 1663
  j32: -66697
  j33: -63593

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AR009.yaml

```yaml
#SAH020AR009
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AR009'
 version: 2.0

zero:
 encoder_offset:
  j00: 138
  j01: -65973
  j02: -780
  j03: 740
  j10: 161
  j11: -67747
  j12: 776
  j13: -60
  j20: 15
  j21: -66435
  j22: 2312
  j23: 861
  j30: 505
  j31: -65
  j32: -65716
  j33: -67160

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AR010.yaml

```yaml
#SAH020AR010
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AR010'
 version: 2.0

zero:
 encoder_offset:
  j00: 690
  j01: -66999
  j02: -207
  j03: -870
  j10: 14
  j11: -65734
  j12: 931
  j13: 1636
  j20: 63
  j21: -66921
  j22: 874
  j23: 1380
  j30: -16573
  j31: 198
  j32: -65668
  j33: -66609

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020AR011.yaml

```yaml
#SAH020AR011
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020AR011'
 version: 2.0

zero:
 encoder_offset:
  j00: 459
  j01: -66980
  j02: 506
  j03: 810
  j10: -340
  j11: -66436
  j12: -593
  j13: 1727
  j20: 1156
  j21: -67912
  j22: 1429
  j23: 625
  j30: 252
  j31: 1292
  j32: -66207
  j33: -66308

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: -1
  j01: -1
  j02: -1
  j03: -1
  j10: -1
  j11: +1
  j12: +1
  j13: -1
  j20: +1
  j21: -1
  j22: -1
  j23: -1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020BL016.yaml

```yaml
#SAH020BL016
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020BL016'
 version: 2.0

zero:
 encoder_offset:
  j00: -1367
  j01: -65420
  j02: -462
  j03: -536
  j10: 1358
  j11: -64821
  j12: 556
  j13: -191
  j20: -18
  j21: -66712
  j22: 257
  j23: 346
  j30: -67389
  j31: -65427
  j32: -65129
  j33: -66328

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: -1
  j31: -1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020BR012.yaml

```yaml
#SAH020BR012
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020BR012'
 version: 2.0

zero:
 encoder_offset:
  j00: 214
  j01: -64225
  j02: 1163
  j03: 835
  j10: -191
  j11: -65365
  j12: -1089
  j13: -737
  j20: -623
  j21: -65594
  j22: 644
  j23: -119
  j30: -218
  j31: 122
  j32: -64670
  j33: -66797

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020BR013.yaml

```yaml
#SAH020BR013
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020BR013'
 version: 2.0

zero:
 encoder_offset:
  j00: -391
  j01: -64387
  j02: -129
  j03: 532
  j10: 178
  j11: -66030
  j12: -142
  j13: 547
  j20: -234
  j21: -64916
  j22: 7317
  j23: 1923
  j30: 1124
  j31: -1319
  j32: -65983
  j33: -65566

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020BR014.yaml

```yaml
#SAH020BR014
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020BR014'
 version: 2.0

zero:
 encoder_offset:
  j00: 964
  j01: -66143
  j02: 627
  j03: -704
  j10: -1365
  j11: -67326
  j12: 1799
  j13: -1233
  j20: -611
  j21: -65663
  j22: 490
  j23: 26
  j30: 1121
  j31: -1173
  j32: -66952
  j33: -65478

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020BR015.yaml

```yaml
#SAH020BR015
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020BR015'
 version: 2.0

zero:
 encoder_offset:
  j00: 406
  j01: -65737
  j02: 880
  j03: 2095
  j10: -1223
  j11: -65918
  j12: 1678
  j13: -1341
  j20: 1302
  j21: -64773
  j22: -1601
  j23: 1600
  j30: 331
  j31: 613
  j32: -65592
  j33: -65566

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020CR017.yaml

```yaml
#SAH020CR017
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020CR017'
 version: 2.0

zero:
 encoder_offset:
  j00: -422
  j01: -65177
  j02: -265
  j03: 511
  j10: 128
  j11: -64737
  j12: 1102
  j13: 723
  j20: -1452
  j21: -66647
  j22: 1082
  j23: -886
  j30: -236
  j31: 25
  j32: -66080
  j33: -66225

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020CR018.yaml

```yaml
The contents of the file below are used by the Allegro Hand ROS Package to set zeros and offsets for your hand.

'''zero.yaml:'''
<pre>
#SAH020CR018
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020CR018'
 version: 2.0

zero:
 encoder_offset:
  j00: -460
  j01: -64503
  j02: -534
  j03: -1417
  j10: -553
  j11: -65610
  j12: 343
  j13: -1003
  j20: 1268
  j21: -65468
  j22: -322
  j23: -514
  j30: -211
  j31: 526
  j32: -66265
  j33: -64878

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1
</pre>

```

### src/allegro_hand_parameters/zero_files/zero_SAH020CR019.yaml

```yaml
#SAH020CR019
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020CR019'
 version: 2.0

zero:
 encoder_offset:
  j00: 1199
  j01: -64921
  j02: 452
  j03: -404
  j10: -915
  j11: -65016
  j12: 293
  j13: 807
  j20: -1
  j21: -65703
  j22: 318
  j23: -1415
  j30: 1326
  j31: 105
  j32: -67470
  j33: -65422

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH020CR020.yaml

```yaml
#SAH020CR020
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH020CR020'
 version: 2.0

zero:
 encoder_offset:
  j00: -611
  j01: -66016
  j02: 1161
  j03: 1377
  j10: -342
  j11: -66033
  j12: -481
  j13: 303
  j20: 30
  j21: -65620
  j22: 446
  j23: 387
  j30: -3942
  j31: -626
  j32: -65508
  j33: -66768

 encoder_direction:
  j00: +1
  j01: -1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: +1
  j13: +1
  j20: +1
  j21: -1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: -1
  j33: -1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: -1
  j12: -1
  j13: +1
  j20: -1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH030AL025.yaml

```yaml
#SAH030C033R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
# which_hand: 'left'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030AL025'
 version: 3.0
 input_voltage: 24

zero:
 encoder_offset:
  j00: -21
  j01: 617
  j02: -123
  j03: -2613
  j10: -57
  j11: 2265
  j12: -270
  j13: 284
  j20: 2055
  j21: 1763
  j22: 1683
  j23: -2427
  j30: 870
  j31: -856
  j32: 2143
  j33: 59

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH030C033R.yaml

```yaml
#SAH030C033R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
# which_hand: 'right'
 robot_name: 'Allegro Hand'
 manufacturer: 'SimLab Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030C033R'
 version: 3.0

zero:
 encoder_offset:
  j00: -1591
  j01: -277
  j02: 545
  j03: 168
  j10: -904
  j11: 53
  j12: -233
  j13: -1476
  j20: 2
  j21: -987
  j22: -230
  j23: -106
  j30: -1203
  j31: 361
  j32: 327
  j33: 565

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

### src/allegro_hand_parameters/zero_files/zero_SAH030C034R.yaml

```yaml
#SAH030C034R
#The YAML file used by the Allegro Hand Node is named "zero.yaml"

hand_info:
 control_period_s: 0.003
 DOF: 16
 which_hand: 'Right'
 robot_name: 'Allegro Hand'
 manufacturer: 'Wonikrobotics Co. Ltd.'
 origin: 'Seoul, South Korea'
 serial: 'SAH030C034R'
 version: 3.0
input_voltage: 8

zero:
 encoder_offset:
  j00: 867
  j01: -106
  j02: -643
  j03: 39
  j10: 146
  j11: -1797
  j12: -930
  j13: 469
  j20: 5070
  j21: 1266
  j22: -65
  j23: 616
  j30: 424
  j31: 672
  j32: -526
  j33: 424

 encoder_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

 motor_direction:
  j00: +1
  j01: +1
  j02: +1
  j03: +1
  j10: +1
  j11: +1
  j12: +1
  j13: +1
  j20: +1
  j21: +1
  j22: +1
  j23: +1
  j30: +1
  j31: +1
  j32: +1
  j33: +1

```

## Python signatures and reward/observation bodies (1 files)


### src/allegro_hand_description/scripts/detect_pcan.py

```
def pcan_search()
```