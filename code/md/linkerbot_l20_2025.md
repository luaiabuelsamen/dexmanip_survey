# linkerbot_l20_2025

source: https://github.com/linkerbotai/linker_hand_sdk


commit: fdf0c26dde308296a516619879df6d6e659b7d2a


## README

# This project has been moved to the new address, please visit https://github.com/linker-bot/linkerhand-ros-sdk

-------

# 1. **Overview**

Clever Hands, Create Everything.

LinkerHand Dexterous Hand ROS SDK is a software tool developed by CHIUS INC to drive its series of dexterous hand products and provide functional examples. It supports various devices (such as laptops, desktops, Raspberry Pi, Jetson, etc.) and mainly serves fields like humanoid robotics, industrial automation, and scientific research institutions. It is suitable for scenarios such as humanoid robots, flexible automatic product lines, embodied large model training, and data collection.

**Warning**

1. Please stay away from the dexterous hand's range of motion to avoid personal injury or equipment damage.

2. Be sure to conduct a safety assessment before performing any actions to prevent collisions.

3. Please take good care of the dexterous hand.

# 2. **Version Information**

V2.1.8
1. Fix occasional frame collision issues

V1.3.4

1. The waveform graph display has been changed from single-hand to configurable single/dual-hand display, controlled by modifying the configuration file to determine whether pressure sensing is present.

2. Resolved data alignment errors in the proximity sensing waveform graph.

3. Modify the CAN port closure logic to prevent sensor data from being unreadable on the robotic hand after the second system boot..

V1.3.3

1. GUI now includes a waveform graph for pressure sensors.

2. L10 now supports setting speed and torque.

V1.3.2

1. Added support for the T24 version of the dexterous hand.

V1.3.1

1. Added acquisition of LinkerHand dexterous hand state values (radians and range) in examples

2. Added PyBullet simulation environment

3. Added GUI control interface

# 3. Preparation

## 3.1 System and hardware requirements

* Operating System: Ubuntu20.04

* ROS Version:Noetic

* Python Version: V3.8.10

* Hardware Interface: 5V standard USB interface

## 3.2 Download

```python
$ mkdir -p Linker_Hand_SDK_ROS/src    #Make directory
$ cd Linker_Hand_SDK_ROS/src    #Navigate to the directory 
$ git clone https://github.com/linkerbotai/linker_hand_sdk.git    #Get SDK
```

## 3.3 Install dependencies and compile

```python
$ sudo apt install python3-can
$ cd Linker_Hand_SDK_ROS/src/linker_hand_sdk    #Navigate to the directory 
$ pip install -r requirements.txt    #Install required dependencies
$ catkin_make    #Compile and build the ROS package
```

## 3.4 Configuring ROS Master-Slave Communication

Supports distributed computationand modularization development, effective only at this terminal; ignore if not needed. Raspberry Pi devices are pre-configured by default.

```shell
$ source /opt/ros/noetic/setup.bash
$ export ROS_MASTER_URI=http://<ROS Master IP>:11311
$ export ROS_IP=<host IP>
$ export ROS_HOSTNAME=<host IP>
```

# 4. Usage

## 4.1 Modify the setting.yaml configuration file

Whether operating on actual hardware or in a simulation, the configuration parameters must be altered beforehand.

Currently, the graphical user interface control example for ROS development is capable of independently manipulating only one LinkerHand robotic arm at a time.

```python
$ cd Linker_Hand_SDK_ROS/src/linker_hand_sdk/linker_hand_sdk_ros/config
$ sudo vim setting.yaml    #Edit the configuration file
```

Description of setting.yaml

```yaml
VERSION: 1.3.5 # Version Number, L7 O7 Supported
LINKER_HAND:  # Hand configuration information
  LEFT_HAND:
    EXISTS: True # Check if the left hand exists. If it does not, set the value to False.
    TOUCH: True  # Check if the pressure sensor exists. If it does not, set the value to False.
    JOINT: L7 # Number of joints in the left hand L7 \ L10 \ L20 \ L25
    NAME: # Regardless of l10 or l20, joint name always has 20 entries
      - joint41
      - joint42
      - joint43
      - joint44
      - joint45
      - joint46
      - joint47
      - joint48
      - joint49
      - joint50
      - joint51
      - joint52
      - joint53
      - joint54
      - joint55
      - joint56
      - joint57
      - joint58
      - joint59
      - joint60
  RIGHT_HAND:
    EXISTS: False # Check if the right hand exists.
    TOUCH: True # Check if the pressure sensor exists.
    JOINT: L10 # Number of joints in the right hand L7 \ L10 \ L20 \ L25
    NAME:  # Regardless of l10 or l20, joint name always has 20 entries
      - joint71
      - joint72
      - joint73
      - joint77
      - joint75
      - joint76
      - joint77
      - joint78
      - joint79
      - joint80
      - joint81
      - joint82
      - joint83
      - joint84
      - joint88
      - joint86
      - joint87
      - joint88
      - joint89
      - joint90
PASSWORD: "12345678" # Due to communication with CAN, the system administrator password is required to activate the communication interface.
```

## 4.2 Connect the LinkerHand Dexterous Hand hardware to your PC

### 4.2.1 Insert the USB-to-CAN device interface of the LinkerHand dexterous hand into the Ubuntu device; the blue light will turn on.

![](https://lkaeimso7m.feishu.cn/space/api/box/stream/download/asynccode/?code=ODI5Zjk4NzhiN2U4ZWNhNjIzMTdmOTE1ZWI5ODRlNjFfbjhEaEQ2dlVBN2J1WlpaWFFYSUdmMmtzd2FteldWZDFfVG9rZW46UGVWQmI3b2gwb1ZJbEN4N3ZuQWN5c0g4bmdjXzE3NDM1ODU1NTU6MTc0MzU4OTE1NV9WNA)

Light indicator: Flashing blue signifies a successful connection.

## 4.3 Launch SDK

Launch the LinkerHand L10, L20 dexterous hand SDK. Upon successful startup, there will be prompts for SDK version, CAN interface status, dexterous hand configuration information, and current joint speed of the dexterous hand.

```python
# Enable CAN port
$ sudo /usr/sbin/ip link set can0 up type can bitrate 1000000 #USB-to-CAN device with blue light constantly on
$ cd ~/Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

Launch the LinkerHand O7 dexterous hand SDK.

```python
# Enable CAN port
$ sudo /usr/sbin/ip link set can0 up type can bitrate 1000000 #USB-to-CAN device with blue light constantly on
$ cd ~/Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand_l7.launch # Launch L07 dexterous hand
```

Launch the LinkerHand L25 dexterous hand SDK.

```python
# Enable CAN port
$ sudo /usr/sbin/ip link set can0 up type can bitrate 1000000 #USB-to-CAN device with blue light constantly on
$ cd ~/Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand_l25.launch # Launch L07 dexterous hand
```

# 5. **ROS Package Overview**

## 5.1 linker\_hand\_sdk\_ros

Actuate joint angles of the LinkerHand and retrieve its real-time state values (angle in radians, angular range).

## 5.2 range\_to\_arc

Retrieve radian measurements from L10 and L20.

Get and send the radians for L10 or L20  through the topic:/cb_left_hand_state_arc and /cb_right_hand_state_arc 

Get the position status of the LinkerHand in radians through the topic topic:/cb_left_hand_control_cmd_arc and /cb_right_hand_control_cmd_arc.  Publish the position in radians to control the finger movement of the LinkerHand.

## 5.3 examples

Includes application examples for each product.

## 5.4 doc

Appendix: Document Attachments

# 6. **ROS Development Examples**

## 6.1 PyBullet Simulation

Supported LinkerHand products: L10、L20、L25

1. Open a new terminal and launch ROS

```css
$ roscore
```

* Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and launch PyBullet Simulation

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun linker_hand_pybullet linker_hand_pybullet.py _hand_type:=L20
```

**Parameter Description**

The value of ‘\_hand\_type‘ can be selected based on the product model, for example: \_hand\_type:=L20

**Output Result Example**

None.

## 6.2 **Graphical User Interface Control**

Supported LinkerHand products: L10、L20

Graphical user interface control allows the independent movement of each joint of the LinkerHand dexterous hand L10 and L20 via sliders. Buttons can also be added to record the current values of all sliders and save the current movement state of each joint of the LinkerHand dexterous hand. Functional buttons can be used to replay the action.

Use gui\_control to control the LinkerHand Dexterous Hand: To operate the LinkerHand Dexterous Hand via the gui\_control interface, you need to launch the linker\_hand\_sdk\_ros package and communicate via topics.

1. Open a new terminal and launch ROS

```python
$ roscore
```

* Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and launch the graphical user interface control.

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun gui_control gui_control.py
```

After opening, a UI interface appears. Users can control the joints of the LinkerHand dexterous hand using sliding bars. They can also save the current sliding bar data by clicking the add button on the right, facilitating the replay of the settings in the future.

**Parameter Description**

None.

**Output Result Example**

None.

## 6.3 Get Robot Status Information

### 6.3.1 **Get Current Status**

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and get the current status

  1. For L20, open a new terminal to get the current status.

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ rosrun L20_get_linker_hand_state L20_get_linker_hand_state.py _loop:=True
```

**Parameter Description**&#x20;

Status values include: range value and radian value.

The “\_loop“ parameter must be specified. If set to True, the terminal will continuously display the current status values of the LinkerHand dexterous hand. If set to False, the terminal will display the status once. For example: \_loop:=True .

**Output Result Example**

稍后更新

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ rosrun L10_get_linker_hand_state L10_get_linker_hand_state.py _loop:=True
```

**Parameter Description&#x20;**

Status values include: range value and radian value.

The “\_loop“ parameter must be specified. If set to True, the terminal will continuously display the current status values of the LinkerHand dexterous hand. If set to False, the terminal will display the status once. For example: \_loop:=True.

**Output Result Example**

```bash
header:
  seq: 83
  stamp:
    secs: 1743409242
    nsecs: 193927526
  frame_id: ''
name: []
position: [1.03, -1.57, 1.3, 1.3, 1.3, 1.3, 0.26, -0.26, -0.26, 1.57]
velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
effort: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

### 6.3.2 **Get force sensor data**

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and get force sensor data

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun get_linker_hand_force get_linker_hand_force.py _loop:=False
```

**Parameter Description&#x20;**

The “\_loop“ parameter must be specified. If set to True, the terminal will continuously display the current status values of the LinkerHand dexterous hand. If set to False, the terminal will display the status once. For example: \_loop:=True.

**Output Result Example**

* Right hand five-finger normal force readings: \[0.0, 0.0, 0.0, 0.0, 0.0], with a range of 0 to 255, where greater pressure results in higher values.

* Right hand five-finger tangential force readings: \[0.0, 0.0, 0.0, 0.0, 0.0], with a range of 0 to 255, where greater pressure results in higher values.

* Right hand five-finger tangential force direction readings: \[255.0, 255.0, 255.0, 255.0, 255.0], with a range of 255 to 0, where greater pressure results in smaller values.

* Right hand five-finger proximity sensing readings: \[0.0, 0.0, 0.0, 0.0, 0.0], with a range of 0 to 255, where greater pressure results in higher values.

### 6.3.3 **Get the Current Velocity**

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and get force sensor data

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ rosrun get_linker_hand_speed get_linker_hand_speed.py _loop:=False
```

**Parameter Description**

The “\_loop“ parameter must be specified. If set to True, the terminal will continuously display the current status values of the LinkerHand dexterous hand. If set to False, the terminal will display the status once. For example: \_loop:=True.

**Output Result Example**

The velocity of the right hand’s five fingers is: \[180, 250, 250, 250, 250], in the order of thumb, index finger, middle finger, ring finger, and little finger.

### 6.3.4 **Get the Current**

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and get the current

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun get_linker_hand_current get_linker_hand_current.py _loop:=False
```

**Parameter Description**

The “\_loop“ parameter must be specified. If set to True, the terminal will continuously display the current status values of the LinkerHand dexterous hand. If set to False, the terminal will display the status once. For example: \_loop:=True.

**Output Result Example**

The current of the right hand’s five fingers is: \[180, 250, 250, 250, 250], in the order of thumb, index finger, middle finger, ring finger, and little finger.

### 6.3.5 **Get Error Code**

```python
rostopic pub /cb_hand_setting_cmd std_msgs/String '{data: "{\"setting_cmd\":\"get_faults\",\"params\":{\"hand_type\":\"left\"}}"}'
```

**Parameter Description**

setting\_cmd : Command Parameter

get\_faults : Command Type String

**Output Result Example**

Current of the right hand’s five fingers is: \[0, 1, 0, 0, 0], where 0 represents normal and 1 represents a fault.

## 6.4 Settings

### 6.4.1 Set Speed

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and set speed

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun set_linker_hand_speed set_linker_hand_speed.py _hand_type:=left _speed:=[180,250,250,250,250] # L7为7个值，其他为5个值
```

**Parameter Description**

L10, L20: Consistent speed of five fingers

speed:=\[180,250,250,250,250]

L7：Speed of seven motors

speed:=\[180,250,250,250,250,250,250]&#x20;

**Output Result Example**

speed:\[180,250,250,250,250]

### 6.4.2 Set Current

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and set the current

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun set_linker_hand_current set_linker_hand_current.py _hand_type:=left _current:=42 #暂不支持L7
```

**Parameter Description**

Parameters: hand\_type: left | right (left or right hand) current:0\~255 (set maximum current value)

**Output Result Example**

current:\[180,250,250,250,250]

### 6.4.3 Set Torque

Supported LinkerHand products: L10、L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal and set torque

```python
$ cd Linker_Hand_SDK_ROS
$ source ./devel/setup.bash
$ rosrun set_linker_hand_torque set_linker_hand_torque.py _hand_type:=left _torque:=[180,250,250,250,250] # L7为7个值，其他为5个值
```

**Parameter Description**

Parameters: hand\_type: left | right (left or right hand) torque:=\[180,250,250,250,250]  0\~255. L7 represents the maximum torque for 7 motors, while the other values represent the maximum torque for 5 fingers.&#x20;

**Output Result Example**

torque:\[180,250,250,250,250]

### 6.4.4 **Set to disabled mode**

Supported LinkerHand products: L25

Disables the motor of the dexterous hand, allowing free movement of all joints.

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L25 dexterous hand
```

* Open a new terminal and set to disabled mode

```python
$ Linker_Hand_SDK_ROS/src/linker_hand_sdk/examples/L25
$ python set_disability.py
```

**Parameter Description**

None

**Output Result Example**

None

### 6.4.5 **Set to enabled mode**

Supported LinkerHand products: L25

Enable the dexterous hand motor, which can then be controlled by the control program.

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L25 dexterous hand
```

* Open a new terminal and set to enabled mode

```python
$ Linker_Hand_SDK_ROS/src/linker_hand_sdk/examples/L25
$ python set_enable.py
```

**Parameter Description**

None

**Output Result Example**

None

### 6.4.6 **Set to remote operation mode**

Supported LinkerHand products: L25

If you possess multiple L25 dexterous hands of the same version, this example demonstrates how to have a disabled hand control an enabled one.

First, start the LinkerHand SDK ROS. Below is the configuration method for the controlled L25 dexterous hand, using the right hand as an example. Ensure that both Ubuntu machines are on the same network and that the master and slave configurations are set up, allowing both machines to communicate via ROS simultaneously. For further guidance, please refer to the [Documentation - ROS Wiki](https://wiki.ros.org/).

**Control Party A Dexterous Hand Configuration**

1. Open a new terminal and launch ROS

```css
$ roscore
```

* Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L25 dexterous hand
```

* Open a new terminal and start executing remote control

```python
$ Linker_Hand_SDK_ROS/src/linker_hand_sdk/examples/L25
$ python set_remote_control.py
```

**Controlled Party B Dexterous Hand Configuration**

1. Open a new terminal and launch ROS

```python
# Open a new terminal and launch ROS
$ roscore
```

* Open a new terminal

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch
```

At this time, manually dragging the disabled L25 dexterous hand of Machine A can control the enabled L25 dexterous hand of Machine B.

## 6.5 **Application Demonstration**

### 6.5.1 **Rock-Paper-Scissors Game**

Supported LinkerHand products: L10、L20

Note: Requires an RGB camera

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L10 or L20 dexterous hand
```

* Open a new terminal, start Rock-Paper-Scissors game

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ rosrun finger_guessing finger_guessing.py
```

**Parameter Description**

None

**Output Result Example**

None

### 6.5.2 **Pinch Operation**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal , start Pinch Demonstration

```python
python ./<Your path>/lipcontroller.py
```

If the terminal prints ‘**Start Demonstration**’, it indicates normal operation. At this point, if the hand settings are correct, it should begin performing a pinch motion using the index finger and middle finger. The motion will stop when an object is pinched, and after removing the object, it will continue attempting to pinch until it successfully grabs the item or reaches its motion limit.

**lipcontroller.py&#x20;**&#x69;s a demonstration demo developed based on version 7 of product O7. When used in demonstrations of other versions, you need to adjust the closing posture of the thumb and index finger. Otherwise, the action of ‘**pinching together with the index finger and thumb’** cannot be achieved.

**Parameter Description**

None

**Output Result Example**

None

## 6.6 **Imitation Learning**

### 6.6.1 **Imitation Learning Training**

The hardware used in this example is the LinkerRobot humanoid robot, but other robotic arms or robots can also be used for imitation learning training, as long as the corresponding data topics are modified. For detailed instructions, please refer to the [human-dex project README.md](https://github.com/linkerbotai/human-dex)&#x20;

1. Configure environment

```css
cd human-dex
conda create -n human-dex python=3.8.10
conda activate human-dex
pip install torchvision
pip install torch
pip install -r requirements.txt
```

* Installation

```css
mkdir -p your_ws/src
cd your_ws/src
git clone https://github.com/linkerbotai/human-dex.git
cd ..
catkin_make
source ./devel/setup.bash
```

* Run

```solidity
# Data Collection
 roslaunch record_hdf5 record_hdf5.launch
# Open a new terminal to send the collection command
rostopic pub /record_hdf5 std_msgs/String "data: '{\"method\":\"start\",\"type\":\"humanplus\"}'"
```

* Train

```solidity
cd humanplus/scripts/utils/HIT
python3 imitate_episodes_h1_train.py --task_name data_cb_grasp --ckpt_dir cb_grasp/ --policy_class HIT --chunk_size 50 --hidden_dim 512 --batch_size 48 --dim_feedforward 512 --lr 1e-5 --seed 0 --num_steps 100000 --eval_every 1000 --validate_every 1000 --save_every 1000 --no_encoder --backbone resnet18 --same_backbones --use_pos_embd_image 1 --use_pos_embd_action 1 --dec_layers 6 --gpu_id 0 --feature_loss_weight 0.005 --use_mask --data_aug
```

* Reproduction/Evaluation

```css
cd humanplus/scripts
python3 cb.py
```

**Parameter Description**

None

**Output Result Example**

None

### 6.6.2 **Unidexgrasp Grasping Algorithm**

The original Unidexgrasp algorithm uses the shadowhand. Below is the relevant code for developing the Unidexgrasp algorithm on the linkerhand. For the detailed process, refer to the [linker\_unidexgrasp project](https://github.com/linkerbotai/linker_unidexgrasp).

**Grasping Pose Generation Section**

The grasping pose module maps the shadowhand pose output by the model to the linkerHand L20 pose, facilitating its use in subsequent development.

1. Configure environment

```bash
conda create -n unidexgrasp python=3.8
conda activate unidexgrasp
conda install -y pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge
conda install -y https://mirrors.bfsu.edu.cn/anaconda/cloud/pytorch3d/linux-64/pytorch3d-0.6.2-py38_cu113_pyt1100.tar.bz2
pip install -r requirements.txt
cd thirdparty/pytorch_kinematics
pip install -e .
cd ../nflows
pip install -e .
cd ../
git clone https://github.com/wrc042/CSDF.git
cd CSDF
pip install -e .
cd ../../
```

* Train&#x20;

  1. GraspIPDF

  ```bash
  python ./network/train.py --config-name ipdf_config \
                            --exp-dir ./ipdf_train
  ```

  * GraspGlow

  ```bash
  python ./network/train.py --config-name glow_config \
                            --exp-dir ./glow_train
  python ./network/train.py --config-name glow_joint_config \
                            --exp-dir ./glow_train
  ```

  * ContactNet

  ```bash
  python ./network/train.py --config-name cm_net_config \
                            --exp-dir ./cm_net_train
  ```

* Verification

```bash
python ./network/eval.py  --config-name eval_config \
                          --exp-dir=./eval
```

* Mapping, result visualization

```bash
python ./tests/visualize_result_l20_shadow.py --exp_dir 'eval' --num 3
```

* Save the results for subsequent reinforcement learning algorithm development use.

```bash
python ./tests/data_for_RL.py
```

# 7. Python Development Example

### 7.1 **Make an OK gesture&#x20;**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal and make an OK gesture

```python
python ./<Your path>/gesture-Show-OK.py
```

After starting, the terminal will print “Testing in progress”, and at the same time, the hand will begin to make an OK gesture, bending the middle, ring, and little fingers while extending them.

**Parameter Description**

None

**Output Result Example**

None

### 7.2&#x20;**&#x20;Hand performs index finger rotation movement**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal and start the index finger rotation movement

```python
python ./<Your path>/gesture-Show-Surround-Index-Finger.py
```

After starting, the terminal will print "Testing in progress". At this time, the hand will start to clench into a fist and extend the index finger, which will continuously rotate.

**Parameter Description**

None

**Output Result Example**

None

### 7.3&#x20;**&#x20;Hand wave motion**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal and start the wave motion

```python
python ./<Your path>/gesture-Show-Wave.p
```

After starting, the terminal will print "Testing in progress". At this time, the thumb extends outward and remains still, while the other four fingers begin the wave motion.

**Parameter Description**

None

**Output Result Example**

None

### 7.4 **Hand Performs a Set of Complex Movements**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal and start a set of complex movements

```python
python ./<Your path>/gesture-Show-Ye.py
```

After starting, the terminal will print "Testing in progress". At this time, the hand will begin to perform a set of complex movements to demonstrate the flexibility of the hand.

This example is a demonstration demo developed based on version 7 of product O7. When used in demonstrations of other versions, you need to adjust the closing posture of the thumb and index finger. Otherwise, the action of ‘**pinching together with the index finger and thumb’** cannot be achieved.

**Parameter Description**

None

**Output Result Example**

None

### 7.5&#x20;**&#x20;Manual Loop Grasping Action**

Supported LinkerHand products: L20

1. Open a new terminal and launch ROS

```css
$ roscore
```

* 2\. Open a new terminal and launch Linker Hand ROS SDK

```python
$ cd Linker_Hand_SDK_ROS/
$ source ./devel/setup.bash
$ roslaunch linker_hand_sdk_ros linker_hand.launch # Launch L20 dexterous hand
```

* Open a new terminal and start the loop grasp action

```python
$ cd Linker_Hand_SDK_ROS/src/linker_hand_sdk/examples/gesture-show
$ python gesture-Loop.py 
```

**Parameter Description**

None

**Output Result Example**

None

### 7.6 Finger Dance

Supported LinkerHand products: L25

**Parameter Description**

None

**Output Result Example**

None

# 8. Related GitHub Resources

Human-Dex：https://github.com/linkerbotai/human-dex

Linker\_UniDexGrasp：https://github.com/linkerbotai/linker\_unidexgrasp

LinkerHand-Python-SDK：https://github.com/linkerbotai/linker\_hand\_python\_sdk

linker\_serl：https://githu

## File tree (depth 3, assets pruned)

```
CMakeLists.txt
README.md
README_CN.md
__init__.py
doc/
  20250221-135706.jpeg
  20250221-135722.jpeg
  Topic-Reference.md
  gui_control.png
  hardware_settings.md
  pybullet.png
  setting.png
  start_sdk.png
  state.png
  开始演示.png
  极限位置.jpg
examples/
  L10/
    action-group-show-new.py
    action-group-show-normal.py
  L20/
    L20_get_linker_hand_state/
    gesture-show/
    l20_isaacgym/
    set_linker_hand_current/
  L25/
    be_manipulated/
    gesture/
    linker_L25_pybullet/
    set_disability.py
    set_enable.py
    set_remote_control.py
  L7/
    gesture/
  README_CN.md
  __init__.py
  finger_guessing/
    CMakeLists.txt
    package.xml
    scripts/
  get_linker_hand_current/
    CMakeLists.txt
    package.xml
    scripts/
  get_linker_hand_fault/
    CMakeLists.txt
    package.xml
    scripts/
  get_linker_hand_force/
    CMakeLists.txt
    package.xml
    scripts/
  get_linker_hand_speed/
    CMakeLists.txt
    package.xml
    scripts/
  graphic_display_status/
    CMakeLists.txt
    launch/
    package.xml
    scripts/
  gui_control/
    CMakeLists.txt
    README_CN.md
    config/
    launch/
    package.xml
    scripts/
  set_linker_hand_speed/
    CMakeLists.txt
    package.xml
    scripts/
  set_linker_hand_torque/
    CMakeLists.txt
    package.xml
    scripts/
find_can.sh
linker_hand_sdk_ros/
  CMakeLists.txt
  __init__.py
  launch/
    linker_hand.launch
    linker_hand_double.launch
    linkerf_hand.launch.bak
  package.xml
  scripts/
    LinkerHand/
    __init__.py
    common/
    linker_hand.py
range_to_arc/
  CMakeLists.txt
  launch/
    range_to_arc.launch
  package.xml
  scripts/
    range_to_arc.py
    utils/
release_2.1.9.txt
requirements.txt
```

## Config files (17)


### examples/gui_control/config/L10_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 205
  - 255
  - 255
  - 255
  - 255
  - 180
  - 179
  - 181
  - 41
- ACTION_NAME: 握拳
  ACTION_POS:
  - 116.0
  - 208.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 0.0
- ACTION_NAME: '66'
  ACTION_POS:
  - 155
  - 162
  - 176
  - 125
  - 255
  - 255
  - 180
  - 179
  - 181
  - 68
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 104
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 71
- ACTION_NAME: 握拳
  ACTION_POS:
  - 101.0
  - 60.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 51.0
- ACTION_NAME: 食指弯曲
  ACTION_POS:
  - 255.0
  - 255.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 中指弯曲
  ACTION_POS:
  - 255.0
  - 255.0
  - 255.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 无名指弯曲
  ACTION_POS:
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 小拇指弯曲
  ACTION_POS:
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 拇指侧摆内
  ACTION_POS:
  - 255.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 中指无名指弯曲
  ACTION_POS:
  - 255.0
  - 255.0
  - 255.0
  - 0.0
  - 0.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0

```

### examples/gui_control/config/L20_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 10
  - 100
  - 180
  - 240
  - 245
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  ACTION_POS:
  - 69.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 151.0
  - 10.0
  - 100.0
  - 180.0
  - 240.0
  - 14.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 109.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 10.0
  - 100.0
  - 180.0
  - 240.0
  - 245.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: 握拳
  ACTION_POS:
  - 69.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 151.0
  - 10.0
  - 100.0
  - 180.0
  - 240.0
  - 14.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 109.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
- ACTION_NAME: '666'
  ACTION_POS:
  - 255.0
  - 255.0
  - 33.0
  - 255.0
  - 255.0
  - 255.0
  - 10.0
  - 100.0
  - 180.0
  - 240.0
  - 245.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0
  - 255.0

```

### examples/gui_control/config/L21_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  ACTION_POS:
  - 177
  - 0
  - 0
  - 0
  - 0
  - 51
  - 114
  - 151
  - 189
  - 255
  - 79
  - 255
  - 255
  - 255
  - 255
  - 131
  - 222
  - 244
  - 255
  - 255
  - 0
  - 0
  - 0
  - 0
  - 0

RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  ACTION_POS:
  - 177
  - 0
  - 0
  - 0
  - 0
  - 51
  - 114
  - 151
  - 189
  - 255
  - 79
  - 255
  - 255
  - 255
  - 255
  - 131
  - 222
  - 244
  - 255
  - 255
  - 0
  - 0
  - 0
  - 0
  - 0


```

### examples/gui_control/config/L25_V2_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 51
  - 51
  - 72
  - 202
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 矿泉水
  ACTION_POS:
  - 248
  - 2
  - 40
  - 16
  - 100
  - 49
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 109
  - 151
  - 151
  - 169
  - 88
  - 62
  - 78
  - 133
  - 80
  - 43
- ACTION_NAME: 两指抓奶瓶
  ACTION_POS:
  - 81.0
  - 82.0
  - 253.0
  - 254.0
  - 253.0
  - 30.0
  - 86.0
  - 0.0
  - 18.0
  - 66.0
  - 138.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 148.0
  - 20.0
  - 240.0
  - 249.0
  - 228.0
  - 12.0
  - 2.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: '66'
  ACTION_POS:
  - 248
  - 0
  - 49
  - 16
  - 4
  - 25
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 0
  - 39
  - 32
  - 5
  - 72
  - 0
  - 109
  - 0
  - 0
- ACTION_NAME: '77'
  ACTION_POS:
  - 248
  - 255
  - 255
  - 16
  - 4
  - 64
  - 255
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 255
  - 255
  - 32
  - 5
  - 72
  - 255
  - 255
  - 0
  - 0
- ACTION_NAME: 拇指中指捏合
  ACTION_POS:
  - 248
  - 0
  - 28
  - 16
  - 4
  - 49
  - 0
  - 0
  - 91
  - 103
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 16
  - 159
  - 30
  - 20
  - 230
  - 135
  - 201
  - 0
  - 0
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 51
  - 51
  - 72
  - 202
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 矿泉水
  ACTION_POS:
  - 248
  - 2
  - 40
  - 16
  - 100
  - 49
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 109
  - 151
  - 151
  - 169
  - 88
  - 62
  - 78
  - 50
  - 137
  - 43
- ACTION_NAME: 两指抓奶瓶
  ACTION_POS:
  - 81.0
  - 82.0
  - 253.0
  - 254.0
  - 253.0
  - 30.0
  - 86.0
  - 0.0
  - 18.0
  - 66.0
  - 138.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 148.0
  - 20.0
  - 240.0
  - 249.0
  - 228.0
  - 12.0
  - 2.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: '999'
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 97
  - 81
  - 114
  - 147
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: '777'
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 97
  - 81
  - 114
  - 147
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255

```

### examples/gui_control/config/L25_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 51
  - 51
  - 72
  - 202
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 矿泉水
  ACTION_POS:
  - 248
  - 2
  - 40
  - 16
  - 100
  - 49
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 109
  - 151
  - 151
  - 169
  - 88
  - 62
  - 78
  - 133
  - 80
  - 43
- ACTION_NAME: 两指抓奶瓶
  ACTION_POS:
  - 81.0
  - 82.0
  - 253.0
  - 254.0
  - 253.0
  - 30.0
  - 86.0
  - 0.0
  - 18.0
  - 66.0
  - 138.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 148.0
  - 20.0
  - 240.0
  - 249.0
  - 228.0
  - 12.0
  - 2.0
  - 255.0
  - 255.0
  - 255.0
- ACTION_NAME: '66'
  ACTION_POS:
  - 248
  - 0
  - 49
  - 16
  - 4
  - 25
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 0
  - 39
  - 32
  - 5
  - 72
  - 0
  - 109
  - 0
  - 0
- ACTION_NAME: '77'
  ACTION_POS:
  - 248
  - 255
  - 255
  - 16
  - 4
  - 64
  - 255
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 255
  - 255
  - 32
  - 5
  - 72
  - 255
  - 255
  - 0
  - 0
- ACTION_NAME: 拇指中指捏合
  ACTION_POS:
  - 248
  - 0
  - 28
  - 16
  - 4
  - 49
  - 0
  - 0
  - 91
  - 103
  - 84
  - 0
  - 0
  - 0
  - 0
  - 83
  - 16
  - 159
  - 30
  - 20
  - 230
  - 135
  - 201
  - 0
  - 0
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 75
  - 255
  - 255
  - 255
  - 255
  - 176
  - 51
  - 51
  - 72
  - 202
  - 202
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 矿泉水
  ACTION_POS:
  - 248
  - 2
  - 40
  - 16
  - 100
  - 49
  - 56
  - 0
  - 77
  - 96
  - 84
  - 0
  - 0
  - 0
  - 0
  - 109
  - 151
  - 151
  - 169
  - 88
  - 62
  - 78
  - 50
  - 137
  - 43
- ACTION_NAME: 两指抓奶瓶
  ACTION_POS:
  - 81.0
  - 82.0
  - 253.0
  - 254.0
  - 253.0
  - 30.0
  - 86.0
  - 0.0
  - 18.0
  - 66.0
  - 138.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 148.0
  - 20.0
  - 240.0
  - 249.0
  - 228.0
  - 12.0
  - 2.0
  - 255.0
  - 255.0
  - 255.0

```

### examples/gui_control/config/L7_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 175
  - 255
  - 255
  - 255
  - 255
  - 72
- ACTION_NAME: 握拳
  ACTION_POS:
  - 70
  - 116
  - 0
  - 0
  - 0
  - 0
  - 46
- ACTION_NAME: 食指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 255
  - 255
  - 255
  - 72
- ACTION_NAME: 中指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 255
  - 255
  - 72
- ACTION_NAME: 无名指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 0
  - 255
  - 72
- ACTION_NAME: 小拇指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 0
  - 0
  - 72
- ACTION_NAME: 大拇指弯曲
  ACTION_POS:
  - 13
  - 125
  - 250
  - 250
  - 250
  - 250
  - 32
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 175
  - 255
  - 255
  - 255
  - 255
  - 72
- ACTION_NAME: 握拳
  ACTION_POS:
  - 70.0
  - 116.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 46.0
- ACTION_NAME: 食指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 255
  - 255
  - 255
  - 72
- ACTION_NAME: 中指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 255
  - 255
  - 72
- ACTION_NAME: 无名指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 0
  - 255
  - 72
- ACTION_NAME: 小拇指弯曲
  ACTION_POS:
  - 255
  - 175
  - 0
  - 0
  - 0
  - 0
  - 72
- ACTION_NAME: 大拇指弯曲
  ACTION_POS:
  - 13
  - 125
  - 250
  - 250
  - 250
  - 250
  - 32
```

### examples/gui_control/scripts/config/L10_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  POSITION:
  - 116
  - 208
  - 0
  - 0
  - 0
  - 0
  - 255
  - 255
  - 255
  - 0
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  POSITION:
  - 101
  - 60
  - 0
  - 0
  - 0
  - 0
  - 255
  - 255
  - 255
  - 51
- ACTION_NAME: 食指弯曲
  POSITION:
  - 255
  - 255
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 中指弯曲
  POSITION:
  - 255
  - 255
  - 255
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 无名指弯曲
  POSITION:
  - 255
  - 255
  - 255
  - 255
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 小拇指弯曲
  POSITION:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 0
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 拇指侧摆内
  POSITION:
  - 255
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 中指无名指弯曲
  POSITION:
  - 255
  - 255
  - 255
  - 0
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255

```

### examples/gui_control/scripts/config/L20_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 10
  - 100
  - 180
  - 240
  - 245
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
RIGHT_HAND:
- ACTION_NAME: 张开
  ACTION_POS:
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 10
  - 100
  - 180
  - 240
  - 245
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  ACTION_POS:
  - 69
  - 0
  - 0
  - 0
  - 0
  - 151
  - 10
  - 100
  - 180
  - 240
  - 14
  - 255
  - 255
  - 255
  - 255
  - 109
  - 0
  - 0
  - 0
  - 0
- ACTION_NAME: '666'
  ACTION_POS:
  - 255
  - 255
  - 33
  - 255
  - 255
  - 255
  - 10
  - 100
  - 180
  - 240
  - 245
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255

```

### examples/gui_control/scripts/config/T24_action.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 半握拳
  ACTION_POS:
  - 248
  - 127
  - 107
  - 180
  - 214
  - 42
  - 137
  - 0
  - 30
  - 20
  - 189
  - 0
  - 0
  - 0
  - 0
  - 59
  - 47
  - 32
  - 11
  - 17
  - 170
  - 43
  - 84
  - 76
  - 81
- ACTION_NAME: 张开
  ACTION_POS:
  - 205
  - 255
  - 255
  - 255
  - 255
  - 183
  - 133
  - 255
  - 74
  - 104
  - 98
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
RIGHT_HAND:
- ACTION_NAME: 半握拳
  ACTION_POS:
  - 248
  - 127
  - 107
  - 180
  - 214
  - 42
  - 137
  - 0
  - 30
  - 20
  - 189
  - 0
  - 0
  - 0
  - 0
  - 59
  - 47
  - 32
  - 11
  - 17
  - 170
  - 43
  - 84
  - 76
  - 81
- ACTION_NAME: 张开
  ACTION_POS:
  - 74
  - 255
  - 255
  - 255
  - 255
  - 183
  - 133
  - 255
  - 74
  - 104
  - 98
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L10_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 捏合5CM
  POSITION:
  - 165
  - 70
  - 165
  - 165
  - 255
  - 255
  - 113
  - 255
  - 255
  - 88
- ACTION_NAME: 捏合1CM
  POSITION:
  - 150
  - 70
  - 155
  - 155
  - 255
  - 255
  - 113
  - 255
  - 255
  - 88
- ACTION_NAME: 握3CM物品
  POSITION:
  - 113
  - 70
  - 85
  - 85
  - 85
  - 85
  - 85
  - 255
  - 255
  - 88
- ACTION_NAME: 准备抓握
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 121
- ACTION_NAME: 拇指弯曲
  POSITION:
  - 35
  - 140
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 30
- ACTION_NAME: 食指弯曲
  POSITION:
  - 255
  - 70
  - 0
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: shishi
  POSITION:
  - 85
  - 30
  - 255
  - 0
  - 0
  - 255
  - 0
  - 0
  - 0
  - 66
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 捏合5CM
  POSITION:
  - 165
  - 70
  - 165
  - 165
  - 255
  - 255
  - 113
  - 255
  - 255
  - 88
- ACTION_NAME: 捏合1CM
  POSITION:
  - 150
  - 70
  - 155
  - 155
  - 255
  - 255
  - 113
  - 255
  - 255
  - 88
- ACTION_NAME: 准备抓握
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 121

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L20_positions.yaml

```yaml

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L21_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  POSITION:
  - 177
  - 0
  - 0
  - 0
  - 0
  - 51
  - 114
  - 151
  - 189
  - 255
  - 79
  - 255
  - 255
  - 255
  - 255
  - 131
  - 222
  - 244
  - 255
  - 255
  - 0
  - 0
  - 0
  - 0
  - 0
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  POSITION:
  - 230
  - 80
  - 51
  - 42
  - 7
  - 35
  - 114
  - 151
  - 189
  - 255
  - 58
  - 255
  - 255
  - 255
  - 255
  - 133
  - 5
  - 0
  - 0
  - 0
  - 30
  - 0
  - 0
  - 0
  - 0

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L25_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 96
  - 255
  - 255
  - 255
  - 255
  - 150
  - 114
  - 151
  - 189
  - 255
  - 180
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
  - 255
- ACTION_NAME: 握拳
  POSITION:
  - 230
  - 80
  - 51
  - 42
  - 7
  - 35
  - 114
  - 151
  - 189
  - 255
  - 58
  - 255
  - 255
  - 255
  - 255
  - 133
  - 5
  - 0
  - 0
  - 0
  - 30
  - 0
  - 0
  - 0
  - 0

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L6_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 握拳
  POSITION:
  - 67
  - 151
  - 0
  - 0
  - 0
  - 0
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 179
  - 255
  - 255
  - 255
  - 255
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/L7_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 握拳
  POSITION:
  - 67
  - 151
  - 0
  - 0
  - 0
  - 0
  - 37
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 179
  - 255
  - 255
  - 255
  - 255
  - 83
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255
  - 255

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/O6_positions.yaml

```yaml
LEFT_HAND:
- ACTION_NAME: 握拳
  POSITION:
  - 67
  - 151
  - 0
  - 0
  - 0
  - 0
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 179
  - 255
  - 255
  - 255
  - 255
RIGHT_HAND:
- ACTION_NAME: 张开
  POSITION:
  - 255
  - 70
  - 255
  - 255
  - 255
  - 255

```

### linker_hand_sdk_ros/scripts/LinkerHand/config/setting.yaml

```yaml
VERSION: 2.1.9 # 修复撞帧
LINKER_HAND:  # 手部配置信息
  LEFT_HAND:
    EXISTS: False # 是否存在左手
    TOUCH: True # 是否有压力传感器
    MODBUS: "None" # 通讯协议是否为485 默认None 当前支持RML(睿尔曼API2)
    JOINT: L10 # 左手关节数 L7/L10/L20/L21/L25
    NAME: # 无论l10还是l20 joint name都是20个
      - joint41
      - joint42
      - joint43
      - joint44
      - joint45
      - joint46
      - joint47
      - joint48
      - joint49
      - joint50
      - joint51
      - joint52
      - joint53
      - joint54
      - joint55
      - joint56
      - joint57
      - joint58
      - joint59
      - joint60
    
  RIGHT_HAND:
    EXISTS: True # 是否存在右手
    TOUCH: True # 是否有压力传感器
    MODBUS: "None" # 通讯协议是否为485 默认None 当前支持RML(睿尔曼API2)
    JOINT: L10 # 右手关节数量
    NAME:  # 无论l10还是l20 joint name都是20个
      - joint71
      - joint72
      - joint73
      - joint77
      - joint75
      - joint76
      - joint77
      - joint78
      - joint79
      - joint80
      - joint81
      - joint82
      - joint83
      - joint84
      - joint88
      - joint86
      - joint87
      - joint88
      - joint89
      - joint90
PASSWORD: "12345678" # 由于与can通讯，需要激活通讯接口用到系统管理员密码。只有Linux系统需要，windows系统不需要

```

## Python signatures and reward/observation bodies (145 files)


### examples/L10/action-group-show-new.py

```
def send_messages()
def show_left()
def signal_handler(sig, frame)
```

### examples/L10/action-group-show-normal.py

```
def send_messages()
def show_left()
def signal_handler(sig, frame)
```

### examples/L20/L20_get_linker_hand_state/scripts/L20_get_linker_hand_state.py

```
class L20GetLinkerHandState()
    def __init__(self, loop)
    def left_hand_state_cb(self, msg)
    def left_hand_state_arc_cb(self, msg)
    def right_hand_state_cb(self, msg)
    def right_hand_state_arc_cb(self, msg)
    def single_smg(self)
```

### examples/L20/L20_get_linker_hand_state/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/L20/set_linker_hand_current/scripts/set_linker_hand_current.py

```
"""Author: HJX
Date: 2025-04-08 13:28:18
LastEditors: Please set LastEditors
LastEditTime: 2025-04-09 11:38:23
FilePath: /Linker_Hand_SDK_ROS/src/examples/set_linker_hand_current/scripts/set_linker_hand_current.py
Description: 
symbol_custom_string_obkorol_copyright: """
class SetLinkerHandCurrent()
    def __init__(self, hand_type, current)
    def set_hand_current(self)
```

### examples/L25/be_manipulated/scripts/utils/linker_hand_l10_can.py

```
class FrameProperty(Enum)
class LinkerHandL10Can()
    def __init__(self, config, can_id, can_channel, baudrate)
    def init_can_bus(self, channel, baudrate)
    def send_frame(self, frame_property, data_list)
    def set_joint_positions(self, joint_angles)
    def set_max_torque_limits(self, pressures, type)
    def set_torque(self, torque)
    def set_joint_speed_l10(self, speed)
    def request_all_status(self)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def receive_response(self)
    def process_response(self, msg)
    def get_current_status(self)
    def get_speed(self)
    def get_press(self)
    def get_force(self)
    def close_can_interface(self)
```

### examples/L25/be_manipulated/scripts/utils/linker_hand_l20_can.py

```
class LinkerHandL20Can()
    def __init__(self, config, can_channel, baudrate, can_id)
    def send_command(self, frame_property, data_list)
    def receive_response(self)
    def set_finger_base(self, angles)
    def set_finger_tip(self, angles)
    def set_finger_middle(self, angles)
    def set_thumb_roll(self, angle)
    def send_command(self, frame_property, data_list)
    def set_joint_pitch(self, frame, angles)
    def set_joint_yaw(self, angles)
    def set_joint_roll(self, thumb_roll)
    def set_joint_speed(self, speed)
    def set_electric_current(self, e_c)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_electric_current(self, e_c)
    def clear_faults(self)
    def get_faults(self)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def get_current_status(self)
    def get_force(self)
    def get_speed(self)
    def get_current(self)
    def get_fault(self)
    def close_can_interface(self)
```

### examples/L25/be_manipulated/scripts/utils/linker_hand_l25_can.py

```
class FrameProperty(Enum)
class LinkerHandL25Can()
    def __init__(self, config, can_channel, baudrate, can_id)
    def send_command(self, frame_property, data_list)
    def receive_response(self)
    def set_joint_positions(self, joint_ranges)
    def set_roll_positions(self, joint_ranges)
    def set_yaw_positions(self, joint_ranges)
    def set_root1_positions(self, joint_ranges)
    def set_root2_positions(self, joint_ranges)
    def set_root3_positions(self, joint_ranges)
    def set_tip_positions(self, joint_ranges)
    def get_thumb_positions(self, j)
    def get_index_positions(self, j)
    def get_middle_positions(self, j)
    def get_ring_positions(self, j)
    def get_little_positions(self, j)
    def set_disability_mode(self, j)
    def set_enable_mode(self, j)
    def set_speed(self, speed)
    def set_finger_torque(self, torque)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def joint_map(self, pose)
    def state_to_cmd(self, l24_state)
    def get_current_status(self, j)
    def get_speed(self, j)
    def get_finger_torque(self)
    def close_can_interface(self)
    def joint_map_2(self, pose)
```

### examples/L25/gesture/action_group_l25.py

```
def send_messages()
def show_left()
def signal_handler(sig, frame)
```

### examples/L7/gesture/action-group-show-ti.py

```
def set_speed(speed)
def send_messages()
def show_left()
def signal_handler(sig, frame)
```

### examples/get_linker_hand_current/scripts/get_linker_hand_current.py

```
class GetLinkerHandCurrent()
    def __init__(self, loop)
    def loop_acquisition(self)
    def left_hand_cb(self, msg)
    def right_hand_cb(self, msg)
    def single_acquisition(self)
```

### examples/get_linker_hand_current/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/get_linker_hand_fault/scripts/get_linker_hand_fault.py

```
class GetLinkerHandFault()
    def __init__(self, loop)
    def loop_acquisition(self)
    def left_hand_cb(self, msg)
    def right_hand_cb(self, msg)
    def single_acquisition(self)
    def decimal_to_bits(self, decimal_value, bit_length)
    def get_active_bits(self, decimal_value, bit_length)
```

### examples/get_linker_hand_fault/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/get_linker_hand_force/scripts/get_linker_hand_force.py

```
class GetLinkerHandPressure()
    def __init__(self, loop)
    def loop_acquisition(self)
    def left_hand_cb(self, msg)
    def right_hand_cb(self, msg)
    def single_acquisition(self)
    def list_slice(self, data, n)
```

### examples/get_linker_hand_force/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/get_linker_hand_speed/scripts/get_linker_hand_speed.py

```
class GetLinkerHandSpeed()
    def __init__(self, loop)
    def loop_acquisition(self)
    def left_hand_cb(self, msg)
    def right_hand_cb(self, msg)
    def single_acquisition(self)
```

### examples/get_linker_hand_speed/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/gui_control/scripts/utils/ros_handler.py

```
class RosHandler()
    def __init__(self, hand_joint, hand_type)
    def pub_msg(self, pos)
    def pub_msg_once(self, pos)
    def joint_msg(self, data)
```

### examples/set_linker_hand_speed/scripts/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### examples/set_linker_hand_torque/scripts/set_linker_hand_torque.py

```
"""Author: HJX
Date: 2025-04-08 13:28:18
LastEditors: Please set LastEditors
LastEditTime: 2025-04-09 11:41:59
FilePath: /Linker_Hand_SDK_ROS/src/examples/set_linker_hand_torque/scripts/set_linker_hand_torque.py
Description: 
symbol_custom_string_obkorol_copyright: """
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l10_can.py

```
class FrameProperty(Enum)
class LinkerHandL10Can()
    def __init__(self, can_id, can_channel, baudrate, yaml)
    def init_can_bus(self, channel, baudrate)
    def send_frame(self, frame_property, data_list, sleep)
    def set_joint_positions(self, joint_angles)
    def set_max_torque_limits(self, pressures, type)
    def set_joint_speed_l10(self, speed)
    def set_speed(self, speed)
    def request_all_status(self)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_motor_temperature(self)
    def get_motor_fault_code(self)
    def receive_response(self)
    def process_response(self, msg)
    def set_torque(self, torque)
    def get_version(self)
    def get_current_status(self)
    def get_current_pub_status(self)
    def get_speed(self)
    def get_force(self)
    def get_temperature(self)
    def get_touch_type(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_matrix_touch_v2(self)
    def get_torque(self)
    def get_fault(self)
    def get_current(self)
    def show_fun_table(self)
    def close_can_interface(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l20_can.py

```
class FrameProperty(Enum)
class LinkerHandL20Can()
    def __init__(self, can_channel, baudrate, can_id, yaml)
    def receive_response(self)
    def set_finger_base(self, angles)
    def set_finger_tip(self, angles)
    def set_finger_middle(self, angles)
    def set_thumb_roll(self, angle)
    def send_command(self, frame_property, data_list, sleep)
    def set_joint_pitch(self, frame, angles)
    def set_joint_yaw(self, angles)
    def set_joint_roll(self, thumb_roll)
    def set_joint_speed(self, speed)
    def set_electric_current(self, e_c)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_electric_current(self, e_c)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def pose_slice(self, p)
    def set_joint_positions(self, position)
    def set_speed(self, speed)
    def set_torque(self, torque)
    def set_current(self, current)
    def get_version(self)
    def get_current_status(self)
    def get_current_pub_status(self)
    def get_speed(self)
    def get_current(self)
    def get_torque(self)
    def get_fault(self)
    def get_temperature(self)
    def clear_faults(self)
    def get_touch_type(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_faults(self)
    def get_force(self)
    def show_fun_table(self)
    def close_can_interface(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l21_can.py

```
class FrameProperty(Enum)
class LinkerHandL21Can()
    def __init__(self, can_channel, baudrate, can_id, yaml)
    def send_command(self, frame_property, data_list, sleep_time)
    def receive_response(self)
    def set_joint_positions(self, joint_ranges)
    def set_joint_positions_by_topic(self, joint_ranges)
    def slice_list(self, input_list, slice_size)
    def _list_d_value(self, list1, list2)
    def set_roll_positions(self, joint_ranges)
    def set_yaw_positions(self, joint_ranges)
    def set_root1_positions(self, joint_ranges)
    def set_root2_positions(self, joint_ranges)
    def set_root3_positions(self, joint_ranges)
    def set_tip_positions(self, joint_ranges)
    def set_thumb_torque(self, j)
    def set_index_torque(self, j)
    def set_middle_torque(self, j)
    def set_ring_torque(self, j)
    def set_little_torque(self, j)
    def get_thumb_positions(self, j)
    def get_index_positions(self, j)
    def get_middle_positions(self, j)
    def get_ring_positions(self, j)
    def get_little_positions(self, j)
    def get_thumbn_fault(self, j)
    def get_index_fault(self, j)
    def get_middle_fault(self, j)
    def get_ring_fault(self, j)
    def get_little_fault(self, j)
    def get_thumb_threshold(self, j)
    def get_index_threshold(self, j)
    def get_middle_threshold(self, j)
    def get_ring_threshold(self, j)
    def get_little_threshold(self, j)
    def set_disability_mode(self, j)
    def set_enable_mode(self, j)
    def set_torque(self, torque)
    def set_speed(self, speed)
    def set_finger_torque(self, torque)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def joint_map(self, pose)
    def state_to_cmd(self, l21_state)
    def action_play(self)
    def get_current_status(self, j)
    def get_current_pub_status(self)
    def get_current_state_topic(self)
    def get_speed(self, j)
    def get_finger_torque(self)
    def get_fault(self)
    def get_threshold(self)
    def get_version(self)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_touch_type(self)
    def get_finger_torque(self)
    def get_torque(self)
    def get_thumb_touch(self)
    def get_index_touch(self)
    def get_middle_touch(self)
    def get_ring_touch(self)
    def get_little_touch(self)
    def get_palm_touch(self)
    def get_force(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_current(self)
    def get_temperature(self)
    def get_finger_order(self)
    def clear_faults(self)
    def close_can_interface(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l24_can.py

```
class FrameProperty(Enum)
class LinkerHandL24Can()
    def __init__(self, config, can_channel, baudrate, can_id)
    def send_command(self, frame_property, data_list)
    def receive_response(self)
    def set_joint_positions(self, joint_ranges)
    def set_roll_positions(self, joint_ranges)
    def set_yaw_positions(self, joint_ranges)
    def set_root1_positions(self, joint_ranges)
    def set_root2_positions(self, joint_ranges)
    def set_root3_positions(self, joint_ranges)
    def set_tip_positions(self, joint_ranges)
    def get_thumb_positions(self, j)
    def get_index_positions(self, j)
    def get_middle_positions(self, j)
    def get_ring_positions(self, j)
    def get_little_positions(self, j)
    def set_disability_mode(self, j)
    def set_enable_mode(self, j)
    def set_speed(self, speed)
    def set_finger_torque(self, torque)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def joint_map(self, pose)
    def state_to_cmd(self, l24_state)
    def get_current_status(self, j)
    def get_speed(self, j)
    def get_finger_torque(self)
    def close_can_interface(self)
    def joint_map_2(self, pose)
    def show_fun_table(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l25_can.py

```
class FrameProperty(Enum)
class LinkerHandL25Can()
    def __init__(self, can_channel, baudrate, can_id, yaml)
    def send_command(self, frame_property, data_list)
    def receive_response(self)
    def set_joint_positions(self, joint_ranges)
    def set_joint_positions_by_topic(self, joint_ranges)
    def slice_list(self, input_list, slice_size)
    def _list_d_value(self, list1, list2)
    def set_roll_positions(self, joint_ranges)
    def set_yaw_positions(self, joint_ranges)
    def set_root1_positions(self, joint_ranges)
    def set_root2_positions(self, joint_ranges)
    def set_root3_positions(self, joint_ranges)
    def set_tip_positions(self, joint_ranges)
    def set_thumb_torque(self, j)
    def set_index_torque(self, j)
    def set_middle_torque(self, j)
    def set_ring_torque(self, j)
    def set_little_torque(self, j)
    def get_thumb_positions(self, j)
    def get_index_positions(self, j)
    def get_middle_positions(self, j)
    def get_ring_positions(self, j)
    def get_little_positions(self, j)
    def get_thumbn_fault(self, j)
    def get_index_fault(self, j)
    def get_middle_fault(self, j)
    def get_ring_fault(self, j)
    def get_little_fault(self, j)
    def get_thumb_threshold(self, j)
    def get_index_threshold(self, j)
    def get_middle_threshold(self, j)
    def get_ring_threshold(self, j)
    def get_little_threshold(self, j)
    def set_disability_mode(self, j)
    def set_enable_mode(self, j)
    def set_torque(self, torque)
    def set_speed(self, speed)
    def set_finger_torque(self, torque)
    def request_device_info(self)
    def save_parameters(self)
    def process_response(self, msg)
    def joint_map(self, pose)
    def state_to_cmd(self, l25_state)
    def action_play(self)
    def get_current_status(self, j)
    def get_current_pub_status(self)
    def get_current_state_topic(self)
    def get_speed(self, j)
    def get_finger_torque(self)
    def get_torque(self)
    def get_fault(self)
    def get_threshold(self)
    def get_version(self)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_force(self)
    def get_matrix_touch(self)
    def get_touch_type(self)
    def get_touch(self)
    def get_current(self)
    def get_temperature(self)
    def get_finger_order(self)
    def close_can_interface(self)
    def joint_map_2(self, pose)
    def show_fun_table(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_l7_can.py

```
class LinkerHandL7Can()
    def __init__(self, can_id, can_channel, baudrate, yaml)
    def init_can_bus(self, channel, baudrate)
    def send_frame(self, frame_property, data_list, sleep)
    def set_joint_positions(self, joint_angles)
    def set_max_torque_limits(self, pressures, type)
    def set_torque(self, torque)
    def set_speed(self, speed)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_motor_temperature(self)
    def get_motor_fault_code(self)
    def receive_response(self)
    def process_response(self, msg)
    def get_version(self)
    def get_current_status(self)
    def get_current_pub_status(self)
    def get_speed(self)
    def get_current(self)
    def get_torque(self)
    def get_touch_type(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_matrix_touch_v2(self)
    def get_force(self)
    def get_temperature(self)
    def get_fault(self)
    def show_fun_table(self)
    def close_can_interface(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/can/linker_hand_o6_can.py

```
class LinkerHandO6Can()
    def __init__(self, can_id, can_channel, baudrate, yaml)
    def init_can_bus(self, channel, baudrate)
    def send_frame(self, frame_property, data_list, sleep)
    def set_joint_positions(self, joint_angles)
    def set_max_torque_limits(self, pressures, type)
    def set_torque(self, torque)
    def set_speed(self, speed)
    def get_normal_force(self)
    def get_tangential_force(self)
    def get_tangential_force_dir(self)
    def get_approach_inc(self)
    def get_motor_temperature(self)
    def get_motor_fault_code(self)
    def receive_response(self)
    def process_response(self, msg)
    def get_version(self)
    def get_current_status(self)
    def get_current_pub_status(self)
    def get_speed(self)
    def get_current(self)
    def get_torque(self)
    def get_touch_type(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_matrix_touch_v2(self)
    def get_force(self)
    def get_temperature(self)
    def get_fault(self)
    def show_fun_table(self)
    def close_can_interface(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/core/rml485/linker_hand_l10_485.py

```
class LinkerHandL10For485()
    def __init__(self, ip, linkerhand_id, modbus_port, modbus_baudrate, modbus_timeout)
    def set_speed(self, speed)
    def set_torque(self, force)
    def set_joint_positions(self, pose)
    def get_version(self)
    def get_current(self)
    def get_current_status(self)
    def get_touch_type(self)
    def get_force(self)
    def get_touch(self)
    def get_torque(self)
    def get_temperature(self)
    def get_fault(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/linker_hand_api.py

```
class LinkerHandApi()
    def __init__(self, hand_type, hand_joint, modbus, can)
    def finger_move(self, pose)
    def _get_normal_force(self)
    def _get_tangential_force(self)
    def _get_tangential_force_dir(self)
    def _get_approach_inc(self)
    def set_speed(self, speed)
    def set_joint_speed(self, speed)
    def set_torque(self, torque)
    def set_current(self, current)
    def get_embedded_version(self)
    def get_current(self)
    def get_state(self)
    def get_state_for_pub(self)
    def get_speed(self)
    def get_joint_speed(self)
    def get_touch_type(self)
    def get_force(self)
    def get_touch(self)
    def get_matrix_touch(self)
    def get_matrix_touch_v2(self)
    def get_torque(self)
    def get_temperature(self)
    def get_fault(self)
    def clear_faults(self)
    def set_enable(self)
    def set_disable(self)
    def get_finger_order(self)
    def range_to_arc_left(self, state, hand_joint)
    def range_to_arc_right(self, state, hand_joint)
    def arc_to_range_left(self, state, hand_joint)
    def arc_to_range_right(self, state, hand_joint)
    def show_fun_table(self)
    def close_can(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_AlgoInterface/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_AlgoInterface/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_AlgoInterface/src/core/demo_algo_interface.py

```
class AlgoController()
    def __init__(self, arm_model, force_type)
    def get_arm_model(self)
    def set_angle(self, x, y, z)
    def set_workframe(self, pose)
    def set_toolframe(self, pose, payload, x, y, z)
    def forward_kinematics(self, joint_angles, flag)
    def inverse_kinematics(self, q_in, q_pose, flag)
    def euler2quaternion(self, euler_angle)
    def quaternion2euler(self, quaternion)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_CoordinateSystem/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_CoordinateSystem/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_CoordinateSystem/src/core/demo_coordinate_system.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def set_manual_work_frame(self, name, pose)
    def delete_work_frame(self, name)
    def update_work_frame(self, name, pose)
    def get_given_work_frame(self, name)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_DoubleRoboticArm/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_DoubleRoboticArm/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_DoubleRoboticArm/src/core/demo_double_robotic_arm.py

```
def demo_movej(robot, joint, v, r, connect, block)
def demo_movel(robot, pose, v, r, connect, block)
def demo_movec(robot, pose_via, pose_to, v, r, loop, connect, block)
def demo_movej_p(robot, pose, v, r, connect, block)
def connect_robot(ip, port, level, mode)
def disconnect_robot(robot)
def robot_motion_1()
def robot_motion_2()
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ForceControl/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ForceControl/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ForceControl/src/core/demo_force_control.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def set_force_position(self, sensor, mode, direction, force)
    def stop_force_position(self)
    def movel(self, pose, v, r, connect, block)
    def movej_p(self, pose, v, r, connect, block)
    def movej(self, joint, v, r, connect, block)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Gripper/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Gripper/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Gripper/src/core/demo_gripper.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def movej(self, joint, v, r, connect, block)
    def set_gripper_pick_on(self, speed, force, block, timeout)
    def set_gripper_release(self, speed, block, timeout)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_IOControl/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_IOControl/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_IOControl/src/core/demo_io_control.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def drag_teach(self, trajectory_record)
    def save_trajectory(self, file_path)
    def add_lines_to_file(self, file_path, degree_of_freedom, type_value)
    def demo_send_project(self, file_path, plan_speed, only_save, save_id, step_flag, auto_start, project_type)
    def get_program_run_state(self, time_sleep, max_retries)
    def set_io_mode(self, io_num, io_mode)
    def set_do_state(self, io_num, io_state)
    def get_io_input(self, io_num)
    def set_default_run_program(self, tra_id)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Lift/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Lift/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Lift/src/core/demo_lift.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def movel(self, pose, v, r, connect, block)
    def movej_p(self, pose, v, r, connect, block)
    def set_gripper_pick_on(self, speed, force, block, timeout)
    def set_gripper_release(self, speed, block, timeout)
    def set_lift_height(self, speed, height, block)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ModbusRTU/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ModbusRTU/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_ModbusRTU/src/core/demo_modbus_rtu.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def set_modbus_mode(self, port, baudrate, timeout)
    def close_modbus_mode(self, port)
    def read_coils(self, port, address, device, num)
    def write_single_coil(self, data, port, address, device, num)
    def write_single_register(self, data, port, address, device)
    def read_holding_registers(self, port, address, device)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_MovejCANFD/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_MovejCANFD/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_MovejCANFD/src/core/demo_movej_canfd.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def arm_state_callback(data)
    def demo_movej_canfd(self)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Moves/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Moves/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_Moves/src/core/demo_moves.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def get_arm_model(self)
    def disconnect(self)
    def movej(self, joint, v, r, connect, block)
    def movej_p(self, pose, v, r, connect, block)
    def moves(self, move_positions, speed, blending_radius, block)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_OnlineProgram/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_OnlineProgram/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_OnlineProgram/src/core/demo_online_program.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def disconnect(self)
    def demo_drag_teach(self, trajectory_record)
    def demo_save_trajectory(self, file_path)
    def add_lines_to_file(self, file_path, type_value)
    def demo_send_project(self, file_path, plan_speed, only_save, save_id, step_flag, auto_start, project_type)
    def demo_get_program_run_state(self, time_sleep, max_retries)
    def demo_set_arm_pause(self)
    def demo_set_arm_continue(self)
    def demo_set_arm_stop(self)
    def demo_set_arm_slow_stop(self)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_SimpleProcess/src/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_SimpleProcess/src/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Demo/RMDemo_Python/RMDemo_SimpleProcess/src/core/demo_simple_process.py

```
class RobotArmController()
    def __init__(self, ip, port, level, mode)
    def get_arm_model(self)
    def disconnect(self)
    def get_arm_software_info(self)
    def movej(self, joint, v, r, connect, block)
    def movel(self, pose, v, r, connect, block)
    def movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def movej_p(self, pose, v, r, connect, block)
def main()
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Python/Robotic_Arm/rm_ctypes_wrap.py

```
"""封装C库接口与结构体  
@author Realman-Aisha  
@date 2024-04-28  
  
@details
此模块通过ctypes库封装了对C库接口的调用，简化了Python与C库之间的交互过程。它会自动加载对应环境的C库，  
封装了设置参数类型、返回值类型等复杂步骤，并创建了与C库中定义的结构体相对应的Python类。  
 
**重要提示**  
- 在使用此模块前，请确保已经根据当前操作系统和Python环境正确安装了C版本的API库，并且库文件的路径正确配置。   
- 请勿直接修改此文件，除非您了解其内部实现并清楚修改可能带来的后果。  """
class UserString()
    def __init__(self, seq)
    def __bytes__(self)
    def __str__(self)
    def __repr__(self)
    def __int__(self)
    def __long__(self)
    def __float__(self)
    def __complex__(self)
    def __hash__(self)
    def __le__(self, string)
    def __lt__(self, string)
    def __ge__(self, string)
    def __gt__(self, string)
    def __eq__(self, string)
    def __ne__(self, string)
    def __contains__(self, char)
    def __len__(self)
    def __getitem__(self, index)
    def __getslice__(self, start, end)
    def __add__(self, other)
    def __radd__(self, other)
    def __mul__(self, n)
    def __mod__(self, args)
    def capitalize(self)
    def center(self, width)
    def count(self, sub, start, end)
    def decode(self, encoding, errors)
    def encode(self, encoding, errors)
    def endswith(self, suffix, start, end)
    def expandtabs(self, tabsize)
    def find(self, sub, start, end)
    def index(self, sub, start, end)
    def isalpha(self)
    def isalnum(self)
    def isdecimal(self)
    def isdigit(self)
    def islower(self)
    def isnumeric(self)
    def isspace(self)
    def istitle(self)
    def isupper(self)
    def join(self, seq)
    def ljust(self, width)
    def lower(self)
    def lstrip(self, chars)
    def partition(self, sep)
    def replace(self, old, new, maxsplit)
    def rfind(self, sub, start, end)
    def rindex(self, sub, start, end)
    def rjust(self, width)
    def rpartition(self, sep)
    def rstrip(self, chars)
    def split(self, sep, maxsplit)
    def rsplit(self, sep, maxsplit)
    def splitlines(self, keepends)
    def startswith(self, prefix, start, end)
    def strip(self, chars)
    def swapcase(self)
    def title(self)
    def translate(self)
    def upper(self)
    def zfill(self, width)
class MutableString(UserString)
    """mutable string objects

Python strings are immutable objects.  This has the advantage, that
strings may be used as dictionary keys.  If this property isn't needed
and you insist on changing string values in place instead, you may cheat
and use MutableString.

But the purpose of this class is an educ"""
    def __init__(self, string)
    def __hash__(self)
    def __setitem__(self, index, sub)
    def __delitem__(self, index)
    def __setslice__(self, start, end, sub)
    def __delslice__(self, start, end)
    def immutable(self)
    def __iadd__(self, other)
    def __imul__(self, n)
class String(MutableString, Union)
    def __init__(self, obj)
    def __len__(self)
    def from_param(cls, obj)
def ReturnString(obj, func, arguments)
def UNCHECKED(type)
class _variadic_function(object)
    def __init__(self, func, restype, argtypes, errcheck)
    def _as_parameter_(self)
    def __call__(self)
def ord_if_char(value)
def _environ_path(name)
class LibraryLoader()
    """A base class For loading of libraries ;-)
Subclasses load libraries for specific platforms."""
    def __init__(self)
    def __call__(self, libname)
    def getpaths(self, libname)
    def getplatformpaths(self, _libname)
class DarwinLibraryLoader(LibraryLoader)
    """Library loader for MacOS"""
    def getplatformpaths(self, libname)
    def getdirs(libname)
class PosixLibraryLoader(LibraryLoader)
    """Library loader for POSIX-like systems (including Linux)"""
    def _get_ld_so_conf_dirs(self, conf, dirs)
    def _create_ld_so_cache(self)
    def getplatformpaths(self, libname)
class WindowsLibraryLoader(LibraryLoader)
    """Library loader for Microsoft Windows"""
def add_library_search_dirs(other_dirs)
def RM_MOVE_SINGLE_BLOCK(timeout)
class rm_thread_mode_e(IntEnum)
    """线程模式枚举
    """
class rm_robot_arm_model_e(IntEnum)
    """机械臂型号枚举  

此枚举类定义了不同型号的机械臂型号。  

Attributes:  
    RM_MODEL_RM_65_E (int): RM_65型号  
    RM_MODEL_RM_75_E (int): RM_75型号  
    RM_MODEL_RM_63_I_E (int): RML_63I型号（已弃用）  
    RM_MODEL_RM_63_II_E (int): RML_63II型号  
    RM_MODEL_RM_63_III_E (int): RML_63III型号
    RM_MODEL_ECO_65_E (int): ECO_65型号  
  """
class rm_force_type_e(IntEnum)
    """机械臂末端版本枚举 
    """
class rm_event_type_e(IntEnum)
    """机械臂事件类型枚举 
    """
class rm_force_position_sensor_e(IntEnum)
    """力位混合控制传感器类型枚举
    """
class rm_force_position_mode_e(IntEnum)
    """力位混合控制模式枚举
    """
class rm_force_position_dir_e(IntEnum)
    """力位混合控制模式（单方向）力控方向枚举
    """
class rm_event_push_data_t(Structure)
    """表示机械臂到位等事件信息的结构体  
@details 此结构体用于接收关于机械臂的各类事件信息，如规划轨迹到位、在线编程到位等。  
通过rm_get_arm_event_call_back接口注册回调函数处理本结构体数据。  
**Attributes**: 
    - handle_id (int) 机械臂连接id，用于标识特定的机械臂连接。
    - event_type (rm_event_type_e) 事件类型枚举，表示具体的事件类型。  
        - 0：无事件  
        - 1：当前规划轨迹到位  
        - 2：当前在线编程到位  
    """
class rm_arm_current_trajectory_e(IntEnum)
    """机械臂当前规划类型枚举 
    """
class rm_udp_custom_config_t(Structure)
    """自定义UDP上报项  

**Attributes**:  
    - joint_speed (int): 关节速度。 
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - lift_state (int): 升降关节信息。
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - expand_state (int): 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）
            1：上报；   0：关闭上报；   -1：不设置，保持之前的状态
    - hand_st"""
    def __init__(self, joint_speed, lift_state, expand_state, arm_current_status, hand_state, aloha_state, plus_base, plus_state)
    def to_dict(self, recurse)
class rm_realtime_push_config_t(Structure)
    """UDP机械臂状态主动上报接口配置  

**Attributes**:  
    - cycle (int): 广播周期，5ms的倍数
    - enable (bool): 使能，是否主动上报
    - port (int): 广播的端口号
    - force_coordinate (int): 系统外受力数据的坐标系（力传感器版本支持）
        - -1：不支持力传感器
        -  0：传感器坐标系 
        -  1：当前工作坐标系
        -  2：当前工具坐标系
    - ip (bytes): 自定义的上报目标IP地址
    - cu"""
    def __init__(self, cycle, enable, port, force_coordinate, ip, custom_config)
    def to_dict(self, recurse)
class rm_io_real_time_config_t(Structure)
    def __init__(self, speed, mode)
    def to_dict(self, recurse)
class rm_io_config_t(Structure)
    """数字IO配置结构体

io_mode:模式，0-通用输入模式
            1-通用输出模式
            2-输入开始功能复用模式
            3-输入暂停功能复用模式
            4-输入继续功能复用模式
            5-输入急停功能复用模式
            6-输入进入电流环拖动复用模式
            7-输入进入力只动位置拖动模式（六维力版本可配置）
            8-输入进入力只动姿态拖动模式（六维力版本可配置）
            9-输入进入力位姿结合拖动复用模式（六维力版本可配置）
    """
    def __init__(self, io_mode, io_real_time_config_t)
    def to_dict(self, recurse)
class rm_io_get_t(Structure)
    """数字IO状态获取结构体
**Attributes**
    - io_state:数字io状态（0低 1高）
    - io_config:io配置结构体"""
    def __init__(self, io_state, io_config)
    def to_dict(self, recurse)
class rm_quat_t(Structure)
    """表示四元数的结构体  

**Attributes**:  
    - w (float): 四元数的实部（scalar part），通常用于表示旋转的角度和方向。  
    - x (float): 四元数的虚部中的第一个分量（vector part）。  
    - y (float): 四元数的虚部中的第二个分量。  
    - z (float): 四元数的虚部中的第三个分量。    """
    def to_dict(self, recurse)
class rm_position_t(Structure)
    """位置结构体  

**Attributes**:  
    - x (float): X轴坐标值，单位：m。  
    - y (float): Y轴坐标值，单位：m。  
    - z (float): Z轴坐标值，单位：m。  

这个结构体通常用于表示机器人、物体或其他任何可以在三维空间中定位的点的位置。  """
    def to_dict(self, recurse)
class rm_euler_t(Structure)
    """表示欧拉角（Euler angles）的结构体  

**Attributes**:  
    - rx (float): 绕X轴旋转的角度，单位：rad。  
    - ry (float): 绕Y轴旋转的角度，单位：rad。  
    - rz (float): 绕Z轴旋转的角度，单位：rad。   """
    def to_dict(self, recurse)
class rm_pose_t(Structure)
    """表示机械臂位置姿态的结构体  

**Attributes**:  
    - position (rm_position_t): 位置，单位：m
    - quaternion (rm_quat_t): 四元数
    - euler (rm_euler_t): 欧拉角，单位：rad"""
    def to_dict(self, recurse)
class rm_frame_name_t(Structure)
    """坐标系名称结构体  

**Attributes**:  
    - name (str): 不超过10个字符"""
class rm_frame_t(Structure)
    """表示一个坐标系的结构体  

**Attributes**:  
    - frame_name (bytes): 坐标系名称，不超过10个字符（包括结尾的null字节）。  
    - pose (rm_pose_t): 坐标系位姿，包含位置和姿态信息。  
    - payload (float): 坐标系末端负载重量，单位：kg。  
    - x (float), y (float), z (float): 坐标系末端负载质心位置坐标。  """
    def __init__(self, frame_name, pose, payload, x, y, z)
    def to_dictionary(self)
class rm_ctrl_version_t(Structure)
    """表示控制器ctrl 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self, recurse)
class rm_dynamic_version_t(Structure)
    """表示动力学版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - model_version (bytes): 动力学模型版本号。"""
    def to_dict(self)
class rm_planinfo_t(Structure)
    """表示控制器plan 层软件信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_algorithm_version_t(Structure)
    """表示算法库信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_software_build_info_t(Structure)
    """表示软件版本信息的结构体  

**Args:**  
    - 无（此结构体通常为调用接口获取数据填充）。  

**Attributes:**  
    - build_time (bytes): 编译时间。
    - version (bytes): 版本号。"""
    def to_dict(self)
class rm_arm_software_version_t(Structure)
    """表示机械臂软件版本信息的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


Attributes:  
    product_version (bytes): 机械臂型号
    robot_controller_version (bytes): 机械臂控制器版本，若为四代控制器，则该字段为"4.0"
    algorithm_info (rm_algorithm_version_t): 算法库信息
    ctrl_info (rm_software_build_info_t): ctrl 层软件信"""
    def to_dict(self, robot_controller_version)
class rm_err_t(Structure)
    """错误码结构体
**Args**:  
无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    err_len (uint8_t):   机械臂错误代码个数
    err     (list[int]): 错误代码"""
    def to_dict(self, recurse)
class rm_current_arm_state_t(Structure)
    """表示机械臂当前状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes:**  
    pose    (rm_pose_t): 机械臂的当前位姿信息。  
    joint   (list[float]): 机械臂当前关节角度，单位：°。  
    err     (rm_err_t): 机械臂错误代码。

注意：  
- 这些字段通常由外部系统或硬件提供，并通过适当的接口填充。  
- 在处理错误代码时，请参考相关的错误代码文档或枚举。  """
    def to_dictionary(self, arm_dof)
class rm_joint_status_t(Structure)
    """表示机械臂关节状态的结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  


**Attributes**:  
    joint_current (list[float]): 关节电流，单位mA，精度：0.001mA
    joint_en_flag (list[bool]): 当前关节使能状态 ，1为上使能，0为掉使能
    joint_err_code (list[int]): 当前关节错误码
    joint_position (list[float]): 关节角度，单位°，精度：0.001°
"""
    def to_dict(self, recurse)
class rm_pos_teach_type_e(IntEnum)
    """位置示教方向枚举 
    """
class rm_ort_teach_type_e(IntEnum)
    """姿态示教方向枚举 
    """
class rm_wifi_net_t(Structure)
    """无线网络信息结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - channel (int): 如果是 AP 模式，则存在此字段，标识 wifi 热点的物理信道号  
    - ip (str): IP 地址  
    - mac (str): MAC 地址  
    - mask (str): 子网掩码  
    - mode (str): 'ap' 代表热点模式，'sta' 代表联网模式，'off' 代表未开启无线模式  
    - passwor"""
    def to_dict(self, recurse)
class rm_arm_all_state_t(Structure)
    """机械臂所有状态参数  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - joint_current (list[float]): 关节电流，单位mA
    - joint_en_flag (list[int]): 关节使能状态
    - joint_temperature (list[float]): 关节温度,单位℃
    - joint_voltage (list[float]): 关节电压，单位V
    - joint_err_code (list[in"""
    def to_dictionary(self)
class rm_gripper_state_t(Structure)
    """夹爪状态结构体

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - enable_state (int): 夹爪使能标志，0 表示未使能，1 表示使能
    - status (int): 夹爪在线状态，0 表示离线， 1表示在线
    - error (int): 夹爪错误信息，低8位表示夹爪内部的错误信息bit5-7 保留bit4 内部通bit3 驱动器bit2 过流 bit1 过温bit0 堵转
    - mode (int): 当前工作状态：1 夹爪张开到最"""
    def to_dict(self, recurse)
class rm_force_data_t(Structure)
    """六维力传感器数据结构体  

**Args**:  
    无（无直接构造参数，此结构体通常由机械臂提供数据并填充，通过访问对应的属性读取信息）。  

**Attributes**:  
    - force_data (list[float]): 当前力传感器原始数据，力的单位为N；力矩单位为Nm。
    - zero_force_data (list[float]): 当前力传感器系统外受力数据，力的单位为N；力矩单位为Nm。
  
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/RM_API2/Python/Robotic_Arm/rm_robot_interface.py

```
"""@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-"""
class JointConfigSettings()
    """关节配置"""
    def rm_set_joint_max_speed(self, joint_num, speed)
    def rm_set_joint_max_acc(self, joint_num, acc)
    def rm_set_joint_min_pos(self, joint_num, min_pos)
    def rm_set_joint_max_pos(self, joint_num, max_pos)
    def rm_set_joint_drive_max_speed(self, joint_num, speed)
    def rm_set_joint_drive_max_acc(self, joint_num, acc)
    def rm_set_joint_drive_min_pos(self, joint_num, min_pos)
    def rm_set_joint_drive_max_pos(self, joint_num, max_pos)
    def rm_set_joint_en_state(self, joint_num, en_state)
    def rm_set_joint_zero_pos(self, joint_num)
    def rm_set_joint_clear_err(self, joint_num)
    def rm_auto_set_joint_limit(self, mode)
class JointConfigReader()
    """关节配置查询"""
    def rm_get_joint_max_speed(self)
    def rm_get_joint_max_acc(self)
    def rm_get_joint_min_pos(self)
    def rm_get_joint_max_pos(self)
    def rm_get_joint_drive_max_speed(self)
    def rm_get_joint_drive_max_acc(self)
    def rm_get_joint_drive_min_pos(self)
    def rm_get_joint_drive_max_pos(self)
    def rm_get_joint_en_state(self)
    def rm_get_joint_err_flag(self)
class ArmTipVelocityParameters()
    """机械臂运动参数"""
    def rm_set_arm_max_line_speed(self, speed)
    def rm_set_arm_max_line_acc(self, acc)
    def rm_set_arm_max_angular_speed(self, speed)
    def rm_set_arm_max_angular_acc(self, acc)
    def rm_set_arm_tcp_init(self)
    def rm_set_collision_state(self, stage)
    def rm_get_collision_stage(self)
    def rm_get_arm_max_line_speed(self)
    def rm_get_arm_max_line_acc(self)
    def rm_get_arm_max_angular_speed(self)
    def rm_get_arm_max_angular_acc(self)
    def rm_set_DH_data_default(self)
    def rm_set_DH_data(self, DH_data)
    def rm_get_DH_data(self)
class ToolCoordinateConfig()
    """工具坐标系"""
    def rm_set_auto_tool_frame(self, point_num)
    def rm_generate_auto_tool_frame(self, tool_name, payload, x, y, z)
    def rm_set_manual_tool_frame(self, frame)
    def rm_change_tool_frame(self, tool_name)
    def rm_delete_tool_frame(self, tool_name)
    def rm_update_tool_frame(self, frame)
    def rm_get_total_tool_frame(self)
    def rm_get_given_tool_frame(self, tool_name)
    def rm_get_current_tool_frame(self)
    def rm_set_tool_envelope(self, envelope)
    def rm_get_tool_envelope(self, tool_name)
class WorkCoordinateConfig()
    """工作坐标系"""
    def rm_set_auto_work_frame(self, name, point_num)
    def rm_set_manual_work_frame(self, name, pose)
    def rm_change_work_frame(self, tool_name)
    def rm_delete_work_frame(self, tool_name)
    def rm_update_work_frame(self, name, pose)
    def rm_get_total_work_frame(self)
    def rm_get_given_work_frame(self, name)
    def rm_get_current_work_frame(self)
class ArmState()
    """机械臂状态获取"""
    def rm_get_current_arm_state(self)
    def rm_get_current_joint_temperature(self)
    def rm_get_current_joint_current(self)
    def rm_get_current_joint_voltage(self)
    def rm_set_init_pose(self, joint)
    def rm_get_init_pose(self)
    def rm_get_joint_degree(self)
    def rm_get_arm_all_state(self)
    def rm_get_controller_rs485_mode(self)
    def rm_get_tool_rs485_mode(self)
class MovePlan()
    """机械臂轨迹规划指令"""
    def rm_movej(self, joint, v, r, connect, block)
    def rm_movel(self, pose, v, r, connect, block)
    def rm_movel_offset(self, pose, v, r, connect, frame_type, block)
    def rm_moves(self, pose, v, r, connect, block)
    def rm_movec(self, pose_via, pose_to, v, r, loop, connect, block)
    def rm_movej_p(self, pose, v, r, connect, block)
    def rm_movej_canfd(self, joint, follow, expand, trajectory_mode, radio)
    def rm_movep_canfd(self, pose, follow, trajectory_mode, radio)
    def rm_movej_follow(self, joint)
    def rm_movep_follow(self, pose)
class ArmTeachMove()
    """机械臂示教及步进运动"""
    def rm_set_joint_step(self, num, step, v, block)
    def rm_set_pos_step(self, teach_type, step, v, block)
    def rm_set_ort_step(self, teach_type, step, v, block)
    def rm_set_joint_teach(self, num, direction, v)
    def rm_set_pos_teach(self, teach_type, direction, v)
    def rm_set_ort_teach(self, teach_type, direction, v)
    def rm_set_stop_teach(self)
    def rm_set_teach_frame(self, frame_type)
    def rm_get_teach_frame(self)
class ArmMotionControl()
    """机械臂运动的急停、暂停、继续等控制"""
    def rm_set_arm_slow_stop(self)
    def rm_set_arm_stop(self)
    def rm_set_arm_pause(self)
    def rm_set_arm_continue(self)
    def rm_set_delete_current_trajectory(self)
    def rm_set_arm_delete_trajectory(self)
    def rm_get_arm_current_trajectory(self)
class ControllerConfig()
    """系统配置"""
    def rm_get_controller_state(self)
    def rm_set_arm_power(self, power)
    def rm_get_arm_power_state(self)
    def rm_get_system_runtime(self)
    def rm_clear_system_runtime(self)
    def rm_get_joint_odom(self)
    def rm_clear_joint_odom(self)
    def rm_get_arm_software_info(self)
    def rm_set_netip(self, ip)
    def rm_clear_system_err(self)
class CommunicationConfig()
    """配置通讯内容

@details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。"""
    def rm_set_wifi_ap(self, wifi_name, password)
    def rm_set_wifi_sta(self, router_name, password)
    def rm_set_RS485(self, baudrate)
    def rm_get_wired_net(self)
    def rm_get_wifi_net(self)
    def rm_set_net_default(self)
    def rm_set_wifi_close(self)
class ControllerIOConfig()
    """控制器端IO
机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。"""
    def rm_set_io_mode(self, io_num, io_mode, io_speed, io_speed_mode)
    def rm_set_do_state(self, io_num, state)
    def rm_get_io_state(self, io_num)
    def rm_get_io_input(self)
    def rm_get_io_output(self)
    def rm_set_voltage(self, voltage_type)
    def rm_get_voltage(self)
class EffectorIOConfig()
    """末端工具IO
 机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
 """
    def rm_set_tool_do_state(self, io_num, state)
    def rm_set_tool_IO_mode(self, io_num, state)
    def rm_get_tool_io_state(self)
    def rm_set_tool_voltage(self, voltage_type)
    def rm_get_tool_voltage(self)
class GripperControl()
    """夹爪控制及状态获取
@details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）"""
    def rm_set_rm_plus_mode(self, mode)
    def rm_get_rm_plus_mode(self)
    def rm_set_rm_plus_touch(self, mode)
    def rm_get_rm_plus_touch(self)
    def rm_get_rm_plus_base_info(self)
    def rm_get_rm_plus_state_info(self)
    def rm_set_gripper_route(self, min_route, max_route)
    def rm_set_gripper_release(self, speed, block, timeout)
    def rm_set_gripper_pick(self, speed, force, block, timeout)
    def rm_set_gripper_pick_on(self, speed, force, block, timeout)
    def rm_set_gripper_position(self, position, block, timeout)
    def rm_get_gripper_state(self)
class Force()
    """末端力传感器
@details
**六维力**
睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
注意使用要求，防止损坏六维力传感器。
@image html force.png "六维力坐标系"
**一维力**
睿尔曼机械臂一维力版末端接口板集成了一维力传"""
    def rm_get_force_data(self)
    def rm_clear_force_data(self)
    def rm_set_force_sensor(self, block)
    def rm_manual_set_force(self, point_num, joint, block)
    def rm_stop_set_force_sensor(self)
    def rm_get_fz(self)
    def rm_clear_fz(self)
    def rm_auto_set_fz(self, block)
    def rm_manual_set_fz(self, joint1, joint2, block)
class DragTeach()
    """拖动示教

@details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。"""
    def rm_start_drag_teach(self, trajectory_record)
    def rm_stop_drag_teach(self)
    def rm_start_multi_drag_teach(self, mode, singular_wall)
    def rm_start_multi_drag_teach_new(self, param)
    def rm_set_drag_teach_sensitivity(self, grade)
    def rm_get_drag_teach_sensitivity(self)
    def rm_drag_trajectory_origin(self, block)
    def rm_run_drag_trajectory(self, timeout)
    def rm_pause_drag_trajectory(self)
    def rm_continue_drag_trajectory(self)
    def rm_stop_drag_trajectory(self)
    def rm_set_force_position(self, sensor, mode, direction, force)
    def rm_set_force_position_new(self, param)
    def rm_stop_force_position(self)
    def rm_save_trajectory(self, file_path)
    def rm_set_force_drag_mode(self, mode)
    def rm_get_force_drag_mode(self)
class HandControl()
    """五指灵巧手控制"""
    def rm_set_hand_posture(self, posture_num, block, timeout)
    def rm_set_hand_seq(self, seq_num, block, timeout)
    def rm_set_hand_angle(self, hand_angle)
    def rm_set_hand_follow_angle(self, hand_angle, block)
    def rm_set_hand_follow_pos(self, hand_pos, block)
    def rm_set_hand_speed(self, speed)
    def rm_set_hand_force(self, force)
class ModbusConfig()
    """Modbus 配置

@details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

@attention
    - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
    - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
    - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS"""
    def rm_set_modbus_mode(self, port, baudrate, timeout)
    def rm_close_modbus_mode(self, port)
    def rm_set_modbustcp_mode(self, ip, port, timeout)
    def rm_close_modbustcp_mode(self)
    def rm_read_coils(self, read_params)
    def rm_read_input_status(self, read_params)
    def rm_read_holding_registers(self, read_params)
    def rm_read_input_registers(self, read_params)
    def rm_write_single_coil(self, write_params, data)
    def rm_write_single_register(self, write_params, data)
    def rm_write_registers(self, write_params, data)
    def rm_write_coils(self, write_params, data)
    def rm_read_multiple_coils(self, read_params)
    def rm_read_multiple_holding_registers(self, read_params)
    def rm_read_multiple_input_registers(self, read_params)
class InstallPos()
    """安装方式及关节、末端软件版本号查询
@details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。"""
    def rm_set_install_pose(self, x, y, z)
    def rm_get_install_pose(self)
    def rm_get_joint_software_version(self)
    def rm_get_tool_software_version(self)
class ForcePositionControl()
    """透传力位混合控制补偿
    """
    def rm_start_force_position_move(self)
    def rm_stop_force_position_move(self)
    def rm_force_position_move_joint(self, joint, sensor, mode, dir, force, follow)
    def rm_force_position_move_pose(self, pose, sensor, mode, dir, force, follow)
    def rm_force_position_move(self, param)
class LiftControl()
    """升降机构控制
    """
    def rm_set_lift_speed(self, speed)
    def rm_set_lift_height(self, speed, height, block)
    def rm_get_lift_state(self)
class ExpandControl()
    """扩展关节控制
    """
    def rm_set_expand_speed(self, speed)
    def rm_set_expand_pos(self, speed, height, block)
    def rm_get_expand_state(self)
class ProjectManagement()
    """在线编程文件下发、管理"""
    def rm_send_project(self, send_project)
    def rm_get_program_trajectory_list(self, page_num, page_size, vague_search)
    def rm_set_program_id_run(self, tra_id, speed, timeout)
    def rm_get_program_run_state(self)
    def rm_get_flowchart_program_run_state(self)
    def rm_delete_program_trajectory(self, tra_id)
    def rm_update_program_trajectory(self, tra_id, speed, name)
    def rm_set_default_run_program(self, tra_id)
    def rm_get_default_run_program(self)
class GlobalWaypointManage()
    """全局路点管理"""
    def rm_add_global_waypoint(self, waypoint)
    def rm_update_global_waypoint(self, waypoint)
    def rm_delete_global_waypoint(self, point_name)
    def rm_get_given_global_waypoint(self, point_name)
    def rm_get_global_waypoints_list(self, page_num, page_size, vague_search)
class ElectronicFenceConfig()
    """电子围栏和虚拟墙

@details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
用户可以通过这些接口，实现
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/color_msg.py

```
class ColorMsg()
    def __init__(self, msg, color, timestamp)
    def colorMsg(self, msg, color, timestamp)
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/init_linker_hand.py

```
"""Author: HJX
Date: 2025-04-01 14:09:21
LastEditors: Please set LastEditors
LastEditTime: 2025-04-08 11:18:23
FilePath: /Linker_Hand_SDK_ROS/src/linker_hand_sdk_ros/scripts/LinkerHand/utils/init_linker_hand.py
Description: 
symbol_custom_string_obkorol_copyright: """
class InitLinkerHand()
    def __init__(self)
    def current_hand(self)
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/load_write_yaml.py

```
"""Author: HJX
Date: 2025-04-01 14:09:21
LastEditors: Please set LastEditors
LastEditTime: 2025-04-11 10:19:01
FilePath: /LinkerHand_Python_SDK/LinkerHand/utils/load_write_yaml.py
Description: 
symbol_custom_string_obkorol_copyright: """
class LoadWriteYaml()
    def __init__(self)
    def load_setting_yaml(self)
    def load_action_yaml(self, hand_joint, hand_type)
    def write_to_yaml(self, action_name, action_pos, hand_joint, hand_type)
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/mapping.py

```
def range_to_arc_left(left_range, hand_joint)
def range_to_arc_right(right_range, hand_joint)
def arc_to_range_left(hand_arc_l, hand_joint)
def arc_to_range_right(right_arc, hand_joint)
def range_to_arc_right_l20(hand_range_r)
def range_to_arc_left_l20(hand_range_l)
def arc_to_range_right_l20(hand_arc_r)
def arc_to_range_left_l20(hand_arc_l)
def range_to_arc_right_10(hand_range_r)
def range_to_arc_left_10(hand_range_l)
def arc_to_range_right_10(hand_arc_r)
def arc_to_range_left_10(hand_arc_l)
def scale_value(original_value, a_min, a_max, b_min, b_max)
def is_within_range(value, min_value, max_value)
```

### linker_hand_sdk_ros/scripts/LinkerHand/utils/open_can.py

```
"""Author: HJX
Date: 2025-04-01 14:09:21
LastEditors: Please set LastEditors
LastEditTime: 2025-04-11 09:15:31
FilePath: /Linker_Hand_SDK_ROS/src/linker_hand_sdk_ros/scripts/LinkerHand/utils/open_can.py
Description: 
symbol_custom_string_obkorol_copyright: """
class OpenCan()
    def __init__(self, load_yaml)
    def open_can0(self)
    def open_can(self, can)
    def is_can_up_sysfs(self, interface)
    def close_can0(self)
    def close_can(self, can)
```

### linker_hand_sdk_ros/scripts/common/mapping.py

```
def range_to_arc_left(left_range, hand_joint)
def range_to_arc_right(right_range, hand_joint)
def arc_to_range_left(hand_arc_l, hand_joint)
def arc_to_range_right(right_arc, hand_joint)
def range_to_arc_right_l20(hand_range_r)
def range_to_arc_left_l20(hand_range_l)
def arc_to_range_right_l20(hand_arc_r)
def arc_to_range_left_l20(hand_arc_l)
def range_to_arc_right_10(hand_range_r)
def range_to_arc_left_10(hand_range_l)
def arc_to_range_right_10(hand_arc_r)
def arc_to_range_left_10(hand_arc_l)
def scale_value(original_value, a_min, a_max, b_min, b_max)
def is_within_range(value, min_value, max_value)
```

### linker_hand_sdk_ros/scripts/linker_hand.py

```
class LinkerHand()
    def __init__(self)
    def _init_hand(self, hand_type)
    def _hand_setting_cb(self, msg)
    def run(self)
    def run_v2(self)
    def action_hand(self)
    def get_all_state_v2(self)
    def get_pub_state_v2(self)
    def _get_hand_state(self)
    def _get_hand_state_v2(self)
    def pub_hand_state(self, hand_state)
    def _get_hand_touch(self)
    def _get_matrix_touch(self)
    def _get_matrix_touch_v2(self)
    def _get_hand_info(self)
    def _get_hand_info_v2(self)
    def pub_hand_info(self, dic)
    def left_hand_cb(self, msg)
    def action_left_hand(self, position, velocity)
    def left_hand_arc_cb(self, msg)
    def action_left_hand_arc(self, position, velocity)
    def right_hand_cb(self, msg)
    def action_right_hand(self, position, velocity)
    def right_hand_arc_cb(self, msg)
    def action_right_hand_arc(self, position, velocity)
    def joint_state_msg(self, pose, vel)
    def signal_handler(self, sig, frame)
```