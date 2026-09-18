# dexwild_2025

source: https://github.com/DexWild/dexwild


commit: 5fa34af5115bb6f54320d0071c3b1d4864cd224a


## README

<h1 align="center"> DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies </h1>


<div align="center">

#### [Tony Tao](https://tony-tao.com/)<sup>\*</sup>, [Mohan Kumar Srirama](https://www.mohansrirama.com/)<sup>\*</sup>, [Jason Jingzhou Liu](https://jasonjzliu.com/), [Kenneth Shaw](https://kennyshaw.net/), [Deepak Pathak](https://www.cs.cmu.edu/~dpathak/)

#### Robotics: Science and Systems (RSS) 2025

<p align="center">
    <img src="website_assets/imgs/teaser.gif" width="25%"> 
</p>

[[Project page]](https://dexwild.github.io/) [[Video]](https://youtu.be/oMaamSkcl5E) [[ArXiv]](https://arxiv.org/abs/2505.07813) 


[[Hardware Guide]](https://resisted-salad-9e6.notion.site/DexWild-Hardware-Setup-Guide-20eee3f68d27801b8eb8dfde3a5bb7c4?source=copy_link) [[Data Collection Guide]](https://resisted-salad-9e6.notion.site/DexWild-Data-Collection-Guide-20fee3f68d27803b9a88ef9847e292d4?source=copy_link) [[Policy Training]](https://github.com/dexwild/dexwild-training)


[![Linux platform](https://img.shields.io/badge/Platform-linux--64-orange.svg)](https://ubuntu.com/blog/tag/22-04-lts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()


</div>

---

# Overview of Repository

Folder Structure:
```Bash
├── _hardware           # 3D files
├── _MANUS_SDK          # Manus Glove SDK
├── data_preprocessing  # Used for data preprocessing
├── dexwild_ros2        # ROS2 workspace
├── dexwild_utils       # Miscellaneous Utilities
├── misc_scripts        # Miscellaneous Scripts
├── model_checkpoints   # Model Checkpoints
├── shell_scripts       # Shell Scripts
├── training            # Training Code
└── website_assets      # Assets for Website
```

# Data Collection

## 🛠️ Hardware Guide

Setup hardware components following this [Hardware Guide](https://resisted-salad-9e6.notion.site/DexWild-Hardware-Setup-Guide-20eee3f68d27801b8eb8dfde3a5bb7c4?source=copy_link)

## ⚙️ Environment Setup (Main Computer)
Only tested on Ubuntu 22.04.

Core Dependencies:
1. Install [ROS2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) on your machine.
2. Install [ZED SDK 4.2](https://www.stereolabs.com/docs/installation/linux) on your machine. Make sure it is the correct version (4.2).

    You can download the ZED SDK using this command.
    ```bash
    wget -O ZED_SDK_Ubuntu22_cuda12.1_v4.2.5.zstd.run "https://download.stereolabs.com/zedsdk/4.2/cu12/ubuntu22?_gl=1*1m7mgu9*_gcl_au*NDQ4NjIzMzIzLjE3NDk5NTE2NjE."
    ```

Since ROS2 has common compatibility issues with conda, we recommend installing everything into the **base system python**.

3. Clone this repository and cd into the directory:
    ```bash
    git clone git@github.com:dexwild/dexwild.git
    cd dexwild
    ```

4. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

5. Install DexWild Utils
    ```bash
    cd dexwild_utils
    pip install -e .
    ```

5. Build ROS Packages
    ```bash
    cd dexwild_ros2
    source /opt/ros/humble/setup.bash

    colcon build --symlink-install
    ```

    This should create `build`, `install`, and `log`, folders.

For robot data collection, install:
1. Install [GELLO](https://github.com/wuphilipp/gello_software) following this guide. 
2. Install [XARM Python SDK](https://github.com/xArm-Developer/xArm-Python-SDK) following this guide.

## 🖥️ Environment Setup (Mini-PC)
Only tested on Nvidia [Jetpack 5.1.1](https://developer.nvidia.com/embedded/jetpack-sdk-511), but later versions should still work.

Core Dependencies:
1. Install [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html) on your machine. If using later version of Jetpack, [ROS2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) will also work.
2. Install [ZED SDK 4.2](https://www.stereolabs.com/docs/installation/linux) on your machine. Make sure it is the correct version (4.2).

    You can download the ZED SDK using this command.
    ```bash
    wget -O ZED_SDK_Ubuntu22_cuda12.1_v4.2.5.zstd.run "https://download.stereolabs.com/zedsdk/4.2/cu12/ubuntu22?_gl=1*1m7mgu9*_gcl_au*NDQ4NjIzMzIzLjE3NDk5NTE2NjE."
    ```

3. Docker Image For Manus SDK
    Pull the docker image from docker hub
    ```bash
    docker pull boardd/manussdk:v0
    ```

    Setup for Docker:
    ```bash
    sudo apt update
    sudo apt install -y qemu qemu-user-static

    sudo update-binfmts --install qemu-x86_64 /usr/bin/qemu-x86_64-static
    sudo update-binfmts --enable qemu-x86_64
    sudo update-binfmts --display qemu-x86_64

    # Check that QEMU configuration is registered
    cat /proc/sys/fs/binfmt_misc/qemu-x86_64

    sudo docker run --rm --platform linux/amd64 debian uname -m
    # expected output: x86_64

    ```

4. Clone this repository and cd into the directory:
    ```bash
    git clone git@github.com:dexwild/dexwild.git
    cd ~/dexwild
    ```
5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

6. Install DexWild Utils
    ```bash
    cd dexwild_utils
    pip install -e .
    ```

7. Build ROS Packages
    ```bash
    cd ..
    cd dexwild_ros2
    source /opt/ros/foxy/setup.bash
    # alternatively
    source /opt/ros/humble/setup.bash

    colcon build --symlink-install
    ```

    This should create `build`, `install`, and `log`, folders.

8. Misc Installs
    ```bash
    sudo apt update
    sudo apt install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
    ```

8. Update Desktop File Paths and put on desktop.
    ```bash
    cd ~/dexwild
    cd shell_scripts/desktop_apps
    ```
    First go to `launch_collect.desktop`. This is a one click app that launches all of the data collection code. 

    Edit the two lines such that the paths match your username.
    ```bash
    Exec=/home/$USERNAME/dexwild/shell_scripts/kill_tmux.sh
    Icon=/home/$USERNAME/dexwild/shell_scripts/imgs/stop.png
    ```

    Then go to `kill_collect.desktop`. This is one click app that shuts down all data collection cleanly.
    
    Similarly, update the paths such that the paths have your username.
    
    Copy the desktop files to your applications folder

    ```bash
    mkdir -p ~/.local/share/applications
    cp launch_collect.desktop kill_collect.desktop ~/.local/share/applications/

    # make executable
    chmod +x ~/.local/share/applications/launch_collect.desktop
    chmod +x ~/.local/share/applications/kill_collect.desktop

    update-desktop-database ~/.local/share/applications/
    ```

    Lastly, some shell scripts need sudo access. Give them sudo access by using `visudo`

    ```bash
    sudo visudo

    # In visudo paste the following lines. Take care to update your username and path to the shell scripts (under shell_scripts in ~/dexwild)
    USERNAME ALL=(ALL) NOPASSWD: /path/to/run_glove.sh, /path/to/launch_docker.sh
    ```

    Note: It helps to favorite the apps so that they appear in the sidebar for easy access.

## 📈 Data Collection Instructions

Follow [Data Collection Instruction](https://resisted-salad-9e6.notion.site/DexWild-Data-Collection-Guide-20fee3f68d27803b9a88ef9847e292d4?source=copy_link) to collect data.

Data is saved in the following structure:
```bash
data
├── ep_0
│   ├── intergripper
│   │   └── intergripper.pkl
│   ├── left_leapv2
│   │   └── left_leapv2.pkl
│   ├── left_manus
│   │   └── left_manus_full.pkl, left_manus.pkl
│   ├── left_pinky_cam
│   │   └── timestamp1.jpg, timestamp2.jpg, ...
│   ├── left_thumb_cam
│   │   └── timestamp1.jpg, timestamp2.jpg, ...
│   ├── left_tracker
│   │   └── left_tracker_cam_frame_abs.pkl, ...
│   ├── right_leapv2
│   │   └── right_leapv2.pkl
│   ├── right_manus
│   │   └── right_manus_full.pkl, right_manus.pkl
│   ├── right_pinky_cam
│   │   └── timestamp1.jpg, timestamp2.jpg, ...
│   ├── right_thumb_cam
│   │   └── timestamp1.jpg, timestamp2.jpg, ...
│   ├── right_tracker
│   │   └── right_tracker_cam_frame_abs.pkl, ...
│   ├── timesteps
│   │   └── timesteps.txt
│   ├── zed
│   │   └── zed_ts.pkl  
│   └── zed_obs
│       └── timestamp1.jpg, timestamp2.jpg, ...
├── ep_1
├── ep_2
├── ...
└── zed_recordings
    ├── output_0_4.svo2
    ├── output_5_9.svo2
    └── ...
```

# Data Processing

There are two main scripts for data processing. One preprocesses the data and the other turns the processed data into a robobuf buffer

## 🧮 Preprocessing

In `data_preprocessing/process_data.sh` there are a few parameters that must be changed.

```bash
# Basic settings
IS_ROBOT=false        # Set True if this is robot data
PARALLELIZE=true      # Set True if you want to process in parallel (usually yes)
LEFT_HAND=true        # Set True to process left hand
RIGHT_HAND=true       # Set True to process right hand

# Data Directory
DATA_DIR="/path/to/data_folder"  # SET to your input dataset directory

# Processing options
PROCESS_SVO=true       # Process zed data
SKIP_SLAM=false        # Skip SLAM (set True if camera is static)
PROCESS_HAND=false     # Retarget hand to robot joint angles
PROCESS_TRACKER=false  # Clean up tracker wrist trajectories
CLIP_ACTIONS=false     # Clip action outliers
INTERGRIPPER=false     # Process intergripper poses (for bimanual tasks)

# Optional arguments
GENERATE_VIDEOS=false  # Generate videos of processed results
HAND_TYPE="v2"         # Choose the hand type: "v1" or "v2"
LANG=false             # Add a natural language description
```

After checking that the parameters are what you want, run the script. It may take up to 30 minutes depending on how much data you have and how powerful your computer is.

```bash
chmod +x process_data.sh
./process_data.sh
```

## 💾 Buffer Creation

First make sure you have the `robobuf` package
```bash
pip install git+https://github.com/AGI-Labs/robobuf.git
```

Now, we must convert the data from our format to one that is consumable by the training. 

In `data_preprocessing/dataset_to_robobuf.sh` there are a also few parameters that must be changed.

```bash
RETAIN_PCT=1.0           # Percentage of original data to retain (1.0 = keep all data), always removes from the end of trajectories

UPSAMPLE_PCTS=("0.60" "1.0")    # List of upsample intervals (e.g., upsample between 60% and 100% of each trajectory)
UPSAMPLE_MULTIPLIER=0           # 0 = no upsampling; n = replicate samples to increase dataset size by n×
SUBSAMPLE_RATE=1.0              # 1.0 = no subsampling; <1.0 = keep only a fraction of the data.

MODE="abs"                      # Action mode: "abs" = absolute actions, "rel" = relative actions
ROT_REPR="rot6d"                # Rotation representation: choose from "quat", "euler", "rot6d"

HUMAN=True                      # True = process human demonstration data?
LEFT_HAND=True                  # True = include left hand data
RIGHT_HAND=True                 # True = include right hand data
LANGUAGE=False                  # True = include language annotations

DATA="/path/to/data"            # Root directory containing data folders
BUF_NAME="buffer name"          # Name/tag of the buffer
```

Usually, all parameters can just be kept constant, except a few:

1. Change the path to the task data folder containing all the data for the particular task
    ```bash
    data_buffers/
    task_data/
    ├── data_1/
    │   ├── ep_0/
    │   ├── ep_1/
    │   └── ...
    ├── data_2/
    │   ├── ep_0/
    │   └── ...
    └── ...
    ```
2. Choose a name for the buffer. This will be saved in `data_buffers` folder as `BUF_NAME`
3. Choose if the data is human demonstration or robot
4. Choose which hands are present in dataset

When you're ready
```bash
chmod +x dataset_to_robobuf.sh
./dataset_to_robobuf.sh
```

# Training

To train the policy, all data must be in robobuf format.

First clone the repository used for training.

```bash
git clone https://github.com/dexwild/dexwild-training
cd ~/dexwild-training
```

Follow the install and training instructions in the [training repository](https://github.com/dexwild/dexwild-training).

# Deployment

There are two launch files for deployment, one for single arm and single hand, and the other for bimanual. Within each launch file, the main parameters to change are as listed below:

```bash
"checkpoint_path":  # Path to the trained policy checkpoint
"replay_path":  # Path to the input Robobuf replay data
"replay_id":  # Index of the episode in the replay buffer to play
"id":  # Identifier for setup type (e.g., "bimanual", "left_mobile")
"observation_keys":  # List of sensor keys used as inputs to the policy

"openloop_length":  # Number of steps to run before running inference again
"skip_first_actions":  # Number of initial actions to skip (to account for delay)

"freq":  # Control loop frequency in Hz
"rot_repr":  # Rotation representation used for actions ("euler", "quat", "rot6d")

"buffer_size":  # Number of past steps to keep for input to model. Must be at least max length of history for policy.

"ema_amount":  # Exponential moving average weight for action smoothing
"use_rmp":  # If True, uses Riemannian Motion Policy (RMP) controller

"start_poses":  # Initial arm poses at start of episode (flattened list)
"start_hand_poses":  # Initial hand poses at start of episode (flattened list)

"pred_horizon":  # How many future steps the model predicts for ensembling
"exp_weight":  # Weight for blending old vs new predictions (0 = only latest) for ensembling

"mode":  # Action interpretation mode ("rel", "abs", "hybrid", etc.)
```

## Single Arm Deployment
```bash
cd ~/dexwild
cd dexwild_ros2
ros2 launch launch/deploy_policy.launch.py
```

## Bimanual Deployment
```bash
cd ~/dexwild
cd dexwild_ros2
ros2 launch launch/bimanual_deploy_policy.launch.py
```

# Citation
If you find this project useful, please cite our work:
```
@article{tao2025dexwild,
      title={DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies},
      author={Tao, Tony and Srirama, Mohan Kumar and Liu, Jason Jingzhou and Shaw, Kenneth and Pathak, Deepak},
      journal={Robotics: Science and Systems (RSS)},
      year={2025}}

```



## File tree (depth 3, assets pruned)

```
.gitignore
.gitmodules
LICENSE
README.md
_MANUS_SDK/
  SDKClient.sln
  SDKClient_Linux/
    ClientLogging.hpp
    ClientPlatformSpecific.cpp
    ClientPlatformSpecific.hpp
    ClientPlatformSpecificTypes.hpp
    Dockerfile
    Dockerfile.Integrated
    Main.cpp
    Makefile
    ManusSDK/
    Readme.md
    SDKClient.cpp
    SDKClient.hpp
    SDKClient_Linux.code-workspace
    SDKClient_Linux.out
    SDKClient_Linux.vcxproj
    SDKClient_Linux.vcxproj.filters
    objects/
  SDKClient_Windows/
    .editorconfig
    .gitignore
    Main.cpp
    PlatformSpecific/
    Readme.md
    SDKClient.cpp
    SDKClient.hpp
    SDKClient.vcxproj
    SDKClient.vcxproj.filters
    SDKClient.vcxproj.user
    log.txt
  SDKMinimalClient_Linux/
    .gitignore
    ClientPlatformSpecific.cpp
    ClientPlatformSpecific.hpp
    ClientPlatformSpecificTypes.hpp
    Dockerfile
    Dockerfile.Integrated
    Makefile
    Readme.md
    SDKMinimalClient.cpp
    SDKMinimalClient.hpp
    SDKMinimalClient_Linux.code-workspace
    SDKMinimalClient_Linux.vcxproj
    SDKMinimalClient_Linux.vcxproj.filters
  SDKMinimalClient_Windows/
    .gitignore
    Readme.md
    SDKMinimalClient.cpp
    SDKMinimalClient.hpp
    SDKMinimalClient.vcxproj
    SDKMinimalClient.vcxproj.bak
    SDKMinimalClient.vcxproj.filters
_hardware/
  step_files/
    aruco_cube.STEP
    left_leapv1_palm_cam_mount.STEP
    left_leapv2_palm_pinky_mount.STEP
    left_leapv2_palm_thumb_mount.STEP
    manus_mount_left.STEP
    manus_mount_right.STEP
    minipc_box.STEP
    minipc_lid.STEP
    right_leapv1_palm_cam_mount.STEP
    right_leapv2_palm_pinky_mount.STEP
    right_leapv2_palm_thumb_mount.STEP
    zed_camera_mount.STEP
  stl_files/
    aruco_cube.STL
    left_leapv1_palm_cam_mount.STL
    left_leapv2_palm_pinky_mount.STL
    left_leapv2_palm_thumb_mount.STL
    manus_mount_left.STL
    manus_mount_right.STL
    minipc_box.STL
    minipc_lid.STL
    right_leapv1_palm_cam_mount.STL
    right_leapv2_palm_pinky_mount.STL
    right_leapv2_palm_thumb_mount.STL
    zed_camera_mount.STL
data_preprocessing/
  dataset_to_robobuf.sh
  mass_generate_videos.py
  mass_process_data.py
  process_data.sh
  processing_config.yaml
  processing_helpers/
    clip_actions.py
    debugging.py
    process_hands.py
    process_intergripper.py
    process_svo.py
    process_tracker.py
    text_generation.py
    video_generation.py
  robobuf/
    check_buffer.py
    compute_dataset_statistics.py
    dataset_to_robobuf.py
    subsample_buffer.py
dexwild_ros2/
  configs/
    human/
    robot/
  launch/
    bimanual_collect_data_leapv2.launch.py
    bimanual_deploy_policy.launch.py
    collect_data_leapv1.launch.py
    collect_data_leapv2.launch.py
    deploy_policy.launch.py
    hand_collect_data.launch.py
    synchronize_hand_data.py
  src/
    dexwild_cameras/
    dexwild_data_collection/
    dexwild_deploy/
    dexwild_gello/
    dexwild_interfaces/
    franka_control/
    glove/
    leap_v1/
    leap_v2/
    retargeting/
    xarm_control/
dexwild_utils/
  dexwild_utils/
    PolicyInference.py
    RecordUI.py
    TrackerProcessor.py
    ZedProcessor.py
    __init__.py
    aruco_utils.py
    cv_viewer/
    data_processing.py
    dynamixel_client.py
    leap_hand_utils.py
    leap_v2_utils.py
    ogl_viewer/
    pose_utils.py
    zmq_utils.py
  setup.py
misc_scripts/
  aruco_generator.py
  camera_calibration/
    april_6x6_80x80cm.yaml
    april_6x6_80x80cm_A0.pdf
    calibrate_camera.py
    generate_checkerboard.py
    imgs/
    see_overlap.py
  list_cameras.py
  markers/
    dexwild_aruco_left_A4.pdf
    dexwild_aruco_left_letter.pdf
    dexwild_aruco_right_A4.pdf
    dexwild_aruco_right_letter.pdf
    individual_pngs/
  read_pkl.py
  test_cameras.py
  view_video.py
model_checkpoints/
  obs_config.yaml
requirements.txt
requirements_minipc.txt
shell_scripts/
  desktop_apps/
    kill_collect.desktop
    launch_collect.desktop
  imgs/
    record.png
    stop.png
  kill_tmux.sh
  launch_docker.sh
  launch_tmux.sh
  run_glove.sh
  start_manus_sdk_desktop.sh
  tmuxp.yaml
website_assets/
  imgs/
    teaser.gif
```

## Config files (11)


### data_preprocessing/processing_config.yaml

```yaml
hands:
  left_hand:
    cube_size: 8
    marker_size: 6.4
    transformation: [0, 0, 0.10, 0, 0, 0]
    marker_ids: [null, 46, 44, 45, 47, 43]
    corner_faces: left

  right_hand:
    cube_size: 8
    marker_size: 6.4
    transformation: [0, 0, 0.10, 0, 0, 0]
    marker_ids: [null, 3, 0, 4, 5, 2]
    corner_faces: right
```

### dexwild_ros2/configs/human/human_bimanual_minipc.yaml

```yaml
glove_node:
  ros__parameters:
    left_glove_sn: "45a7fc8f"
    right_glove_sn: "8569617b"

palm_camera_node:
  ros__parameters:
    cameras: [left_thumb, left_pinky, right_thumb, right_pinky]
    serials: ["00006", "00009", "00011", "00012"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

head_camera_node:
  ros__parameters:
    serial: "00002"
    fourcc: MJPG
    width: 1280
    height: 720
    fps: 30

zed_node:
  ros__parameters:
    serial: 16352271 #13909734
    visualize: True

data_sync_node:
  ros__parameters:
    topics: [
        "/left/thumb_camera_im",
        "/left/pinky_camera_im",
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        # "/head/camera_im",
        # "/head/gray_camera_im",
        # '/zed/im',
        "/zed_ts",
        "/glove/r_short",
        "/glove/l_short",
        "/glove/r_full",
        "/glove/l_full",
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/human/human_left_hand_minipc.yaml

```yaml
glove_node:
  ros__parameters:
    left_glove_sn: "45a7fc8f"
    right_glove_sn: "8569617b"

palm_camera_node:
  ros__parameters:
    cameras: [left_thumb, left_pinky]
    serials: ["00011", "00012"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

zed_node:
  ros__parameters:
    serial: 13909734
    visualize: True

data_sync_node:
  ros__parameters:
    topics: [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        # "/head/camera_im",
        # "/head/gray_camera_im",
        # '/zed/im',
        "/zed_ts",
        "/glove/r_short",
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/human/human_right_hand_minipc.yaml

```yaml
glove_node:
  ros__parameters:
    left_glove_sn: "45a7fc8f"
    right_glove_sn: "8569617b"

palm_camera_node:
  ros__parameters:
    cameras: [right_thumb, right_pinky]
    serials: ["00011", "00012"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

head_camera_node:
  ros__parameters:
    serial: "00002"
    fourcc: MJPG
    width: 1280
    height: 720
    fps: 30

zed_node:
  ros__parameters:
    serial: 13909734
    visualize: True

data_sync_node:
  ros__parameters:
    topics: [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        # "/head/camera_im",
        # "/head/gray_camera_im",
        # '/zed/im',
        "/zed_ts",
        "/glove/r_short",
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/robot/bimanual_robot_xarm6_leapv2.yaml

```yaml
left_mobile_gello_node:
  ros__parameters:
    id: left_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT7WBGG1-if00-port0 # Set to a specific port if needed

right_mobile_gello_node:
  ros__parameters:
    id: right_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISEQG-if00-port0 # Set to a specific port if needed

left_xarm_node:
  ros__parameters:
    xARM_IP: "192.168.1.224"
    id: left_mobile
    teleop: True
    use_rmp: False

right_xarm_node:
  ros__parameters:
    xarm_ip: "192.168.1.228"
    arm_id: right_mobile
    teleop: True
    use_rmp: False

leap_v2_node_left:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISVLF-if00-port0
    isLeft: True

leap_v2_node_right:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT78LTIG-if00-port0
    isLeft: False

leap_v2_ik_left:
  ros__parameters:
    isLeft: True

leap_v2_ik_right:
  ros__parameters:
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [left_thumb, left_pinky, right_thumb, right_pinky]
    serials: ["00002", "00008", "00010", "00001"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

glove_node:
  ros__parameters:
    left_glove_sn: "45a7fc8f"
    right_glove_sn: "8569617b"

zed_node:
  ros__parameters:
    serial: 13909734 # 16352271
    which_hands: [""]
    visualize: True

ticker_node:
  ros__parameters:
    rate: 30.0

data_sync_node:
  ros__parameters:
    topics: [
        /left/thumb_camera_im,
        /left/pinky_camera_im,
        /right/thumb_camera_im,
        /right/pinky_camera_im,

        /ticker,
        /glove/l_short,
        /glove/r_short,
        /glove/l_full,
        /glove/r_full,

        /arm/left_mobile/obs_eef_pose,
        /arm/right_mobile/obs_eef_pose,
        /leapv2_node/cmd_raw_leap_l,
        /leapv2_node/cmd_raw_leap_r,
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/robot/bimanual_robot_xarm6_leapv2_deploy.yaml

```yaml
left_xarm_node:
  ros__parameters:
    xARM_IP: "192.168.1.224"
    id: left_mobile
    teleop: True
    use_rmp: False

right_xarm_node:
  ros__parameters:
    xarm_ip: "192.168.1.228"
    arm_id: right_mobile
    teleop: True
    use_rmp: False

leap_v2_node_left:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISVLF-if00-port0
    isLeft: True

leap_v2_node_right:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT78LTIG-if00-port0
    isLeft: False

leap_v2_ik_left:
  ros__parameters:
    isLeft: True

leap_v2_ik_right:
  ros__parameters:
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [left_thumb, left_pinky, right_thumb, right_pinky]
    serials: ["00002", "00008", "00010", "00001"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

zed_node:
  ros__parameters:
    serial: 13909734 # 16352271
    which_hands: [""]
    visualize: True

ticker_node:
  ros__parameters:
    rate: 30.0

data_sync_node:
  ros__parameters:
    topics: [
        /left/thumb_camera_im,
        /left/pinky_camera_im,
        /right/thumb_camera_im,
        /right/pinky_camera_im,

        /arm/left_mobile/obs_eef_pose,
        /arm/right_mobile/obs_eef_pose,
        /ticker,
      ]
    rosbag_collect: False
    collect_data_mode: False

```

### dexwild_ros2/configs/robot/right_robot_xarm6_leapv1.yaml

```yaml
right_mobile_gello_node:
  ros__parameters:
    id: right_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISEQG-if00-port0 # Set to a specific port if needed

right_xarm_node:
  ros__parameters:
    xarm_ip: "192.168.1.228"
    arm_id: right_mobile
    teleop: True
    use_rmp: False

leap_v1_node_right:
  ros__parameters:
    port: "/dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FTA2U2IO-if00-port0"
    isLeft: False

leap_v1_ik_right:
  ros__parameters:
    isLeft: False
    useViewer: True

leap_v2_ik_right:
  ros__parameters:
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [
        # left_thumb,
        # left_pinky,
        right_thumb,
        right_pinky,
      ]
    serials: ["00010", "00001"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

glove_node:
  ros__parameters:
    left_glove_sn: "60f3738b"
    right_glove_sn: "431ea0a1"

ticker_node:
  ros__parameters:
    rate: 30.0

data_sync_node:
  ros__parameters:
    topics:
      [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        "/glove/r_short",
        "/glove/r_full",
        /arm/right_mobile/obs_eef_pose,
        /leaphand_node/cmd_allegro_right,
        "/ticker",
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/robot/right_robot_xarm6_leapv1_deploy.yaml

```yaml
right_mobile_gello_node:
  ros__parameters:
    id: right_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISEQG-if00-port0 # Set to a specific port if needed
    type: single
    mirror': False

right_xarm_node:
  ros__parameters:
    xARM_IP: "192.168.1.228"
    id: right_mobile
    testing: True

leap_v1_node_right:
  ros__parameters:
    port: "/dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FTA2U2IO-if00-port0"
    isLeft: False

leap_v1_ik_right:
  ros__parameters:
    isLeft: False
    useViewer: True

leap_v2_ik_right:
  ros__parameters:
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [
        # left_thumb,
        # left_pinky,
        right_thumb,
        right_pinky,
      ]
    serials: ["00020", "00021"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

glove_node:
  ros__parameters:
    left_glove_sn: "45a7fc8f"
    right_glove_sn: "8569617b"

data_sync_node:
  ros__parameters:
    topics: [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        # "/zed/im",
        # "/glove/r_short",
        # "/glove/r_full",
        /arm/right_mobile/obs_eef_pose,
        # /leaphand_node/cmd_allegro_right,
        # /leapv2_node/cmd_raw_leap_r,
      ]
    rosbag_collect: False
    collect_data_mode: False

```

### dexwild_ros2/configs/robot/right_robot_xarm6_leapv2.yaml

```yaml
right_mobile_gello_node:
  ros__parameters:
    id: right_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISEQG-if00-port0 # Set to a specific port if needed

right_xarm_node:
  ros__parameters:
    xarm_ip: "192.168.1.228"
    arm_id: right_mobile
    teleop: True
    use_rmp: False

leap_v2_node_right:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT78LTIG-if00-port0
    isLeft: False

leap_v2_ik_right:
  ros__parameters:
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [
        # left_thumb,
        # left_pinky,
        right_thumb,
        right_pinky,
      ]
    serials: ["00010", "00001"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

glove_node:
  ros__parameters:
    left_glove_sn: "60f3738b"
    right_glove_sn: "431ea0a1"

zed_node:
  ros__parameters:
    serial: 16352271 #13909734
    which_hands: [""]
    visualize: False
    zed_live: True # run when running on the robot

ticker_node:
  ros__parameters:
    rate: 30.0

data_sync_node:
  ros__parameters:
    topics:
      [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        "/glove/r_short",
        /arm/right_mobile/obs_eef_pose,
        /leapv2_node/cmd_raw_leap_r,
        "/ticker",
      ]
    rosbag_collect: False
    collect_data_mode: True

```

### dexwild_ros2/configs/robot/right_robot_xarm6_leapv2_deploy.yaml

```yaml
right_mobile_gello_node:
  ros__parameters:
    id: right_mobile
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT8ISEQG-if00-port0 # Set to a specific port if needed

right_xarm_node:
  ros__parameters:
    xarm_ip: "192.168.1.228"
    arm_id: right_mobile
    teleop: False
    use_rmp: False

right_franka_node:
  ros__parameters:
    franka_IP: "172.26.9.131"
    id: right_franka

leap_v2_node_right:
  ros__parameters:
    port: /dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT78LTIG-if00-port0
    isLeft: False

palm_camera_node:
  ros__parameters:
    cameras: [right_thumb, right_pinky]
    serials: ["00010", "00001"] # left_thumb, left_pinky, right_thumb, right_pinky
    fourcc: MJPG
    width: 320
    height: 240
    fps: 60
    superwide: True

zed_node:
  ros__parameters:
    serial: 16352271 #13909734
    which_hands: [""]
    visualize: False
    zed_live: True # run when running on the robot

ticker_node:
  ros__parameters:
    rate: 30.0

data_sync_node:
  ros__parameters:
    topics:
      [
        "/right/thumb_camera_im",
        "/right/pinky_camera_im",
        /arm/right_mobile/obs_eef_pose,
        "/ticker",
      ]
    rosbag_collect: False
    collect_data_mode: False

```

### model_checkpoints/obs_config.yaml

```yaml
transform:
  _target_: data4robotics.transforms.get_transform_by_name
  name: preproc
```

## Python signatures and reward/observation bodies (16 files)


### data_preprocessing/processing_helpers/clip_actions.py

```
def clip_eef_actions(data_dir, all_episodes, left_arm, right_arm)
```

### data_preprocessing/processing_helpers/process_hands.py

```
def process_leapv2_to_v1_wrapper(all_episodes, data_dir, left_hand, right_hand)
def process_hand_wrapper(all_episodes, data_dir, left_hand, right_hand, parallelize, hand_type)
```

### dexwild_ros2/launch/bimanual_deploy_policy.launch.py

```
def generate_launch_description()
```

### dexwild_ros2/launch/deploy_policy.launch.py

```
def generate_launch_description()
```

### dexwild_ros2/launch/hand_collect_data.launch.py

```
def generate_launch_description()
```

### dexwild_ros2/launch/synchronize_hand_data.py

```
def generate_launch_description()
```

### dexwild_ros2/src/dexwild_deploy/dexwild_deploy/deploy_policy.py

```
"""deploy_policy_node.py

This script defines the `DeployPolicy` ROS 2 node, responsible for executing
learned robot manipulation policies in real-time using visual and proprioceptive inputs.

Key Features:
- Supports single-arm and bimanual robotic setups with modular sensor configurations.
- Performs observation buffering, preprocessing, and policy inference at a configurable frequency.
- Interfaces with both standard ROS publishers and RMP (Riemannian Motion Policies) controllers for trajectory execution.
- Handles action smoothing (EMA), policy modes (absolute, relative, hybrid), and warm-sta"""
class DeployPolicy(Node)
    def __init__(self)
    def _declare_parameters(self)
    def _load_parameters(self)
    def _init_state_fields(self)
    def _process_nominal_poses(self)
    def _init_prev_action(self)
    def _setup_publishers_and_subscribers(self, myIP)
    def _setup_bimanual(self, myIP)
    def _setup_single_arm(self, side, myIP)
    def _init_policy(self)
    def model_forward(self, obs)
    def get_obs(self)
    def inference_step(self)
    def pub_messages(self)
    def zed_callback(self, msg)
    def left_thumb_cam_callback(self, msg)
    def right_thumb_cam_callback(self, msg)
    def left_pinky_cam_callback(self, msg)
    def right_pinky_cam_callback(self, msg)
    def left_hand_callback(self)
    def right_hand_callback(self)
    def curr_right_pose_callback(self, msg)
    def curr_left_pose_callback(self, msg)
    def left_pose_callback(self, msg)
    def right_pose_callback(self, msg)
    def destroy_node(self)
def main(args)
```

### dexwild_ros2/src/retargeting/retargeting/leap_ik.py

```
"""Leapv1PybulletIK simulates inverse kinematics (IK) for a Leap V1 robotic hand using PyBullet.
Supports both headless (DIRECT) and GUI modes, ROS2 integration for live control,
and offline batch processing for glove demonstration data."""
class Leapv1PybulletIKNoROS()
    """Standalone PyBullet IK solver for Leap V1 hand."""
    def __init__(self, process, is_left, use_viewer)
    def create_target_vis(self)
    def update_target_vis(self, hand_pos)
    def get_glove_data(self, pose)
    def compute_IK(self, hand_pos)
    def disconnect(self)
class LeapPybulletIK(Node)
    """ROS2 Node wrapper for real-time Leap V1 IK."""
    def __init__(self, is_left, use_viewer)
    def get_glove_data(self, pose)
    def destroy_node(self)
def main(args)
def process_glove_data_v1(glove_path, leap_v1_path, is_left, use_viewer)
def ray_process_glove_data_v1(glove_path, leap_v1_path, is_left, use_viewer)
```

### dexwild_ros2/src/retargeting/retargeting/leap_v2_ik.py

```
"""Leapv2PybulletIK simulates inverse kinematics (IK) for a LeapV2 robotic hand using PyBullet.
This code supports both GUI and headless (DIRECT) simulation, ROS integration for real-time operation,
and offline data processing for human glove demonstrations."""
class Leapv2PybulletIKNoROS()
    """Standalone PyBullet-based LeapV2 inverse kinematics solver.
This class does not depend on ROS and is used for both real-time and batch processing."""
    def __init__(self, process, is_left, use_viewer)
    def create_target_vis(self)
    def update_target_vis(self, hand_pos)
    def get_glove_data(self, pose)
    def compute_IK(self, hand_pos)
    def disconnect(self)
class Leapv2PybulletIK(Node)
    """ROS2 Node wrapper for real-time inference and command publishing using PyBullet-based IK."""
    def __init__(self, is_left, use_viewer)
    def timer_callback(self)
    def get_glove_data(self, pose)
    def destroy_node(self)
def main(args)
def process_glove_data(glove_path, leap_v2_path, is_left, use_viewer)
def ray_process_glove_data(glove_path, leap_v2_path, is_left, use_viewer)
```

### dexwild_ros2/src/retargeting/test/test_copyright.py

```
def test_copyright()
```

### dexwild_ros2/src/retargeting/test/test_flake8.py

```
def test_flake8()
```

### dexwild_ros2/src/retargeting/test/test_pep257.py

```
def test_pep257()
```

### dexwild_utils/dexwild_utils/PolicyInference.py

```
"""Replay and Diffusion Policy Inference for Dexterous Manipulation
=================================================================

This script defines two main classes for running action inference on demonstration data:
1. `ReplayPolicy` – A simple policy that replays pre-recorded demonstration actions.
2. `DiTInference` – A learned policy interface using a Diffusion Transformer (DiT) model 
   for action generation based on multi-view images, state history, and optional language inputs.

Key Features:
-------------
- Handles both single-arm and bimanual setups, with support for Leap hand inp"""
class ReplayPolicy()
    def __init__(self, buffer_path, id, mode, normalized, isensemble, replay_id, rot_repr)
    def update_pose(self, curr_pose)
    def forward(self, obs, lang)
    def threshold_hands(self, actions)
class DiTInference()
    def __init__(self, agent_path, model_name, isensemble, id, mode, openloop_length, pred_horizon, exp_weight, rot_repr, buffer_size, skip_first_actions)
    def preprocess_image(self, bgr_img, size)
    def _proc_image(self, imgs, size)
    def _proc_state(self, obs)
    def update_pose(self, curr_pose)
    def forward(self, obs, lang)
    def average_actions(self, weights, curr_act_preds, use_median)
    def threshold_hands(self, actions)
```

### dexwild_utils/dexwild_utils/leap_hand_utils.py

```
"""Some utilities for LEAP Hand that help with converting joint angles between each convention."""
def angle_safety_clip(joints)
def LEAPsim_limits(type)
def scale(x, lower, upper)
def unscale(x, lower, upper)
def sim_ones_to_LEAPhand(joints, hack_thumb)
def LEAPhand_to_sim_ones(joints, hack_thumb)
def LEAPsim_to_LEAPhand(joints)
def LEAPhand_to_LEAPsim(joints)
def allegro_to_LEAPhand(joints, teleop, zeros)
def LEAPhand_to_allegro(joints, teleop, zeros)
```