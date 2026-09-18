# unitree_dex5_2025

source: https://github.com/unitreerobotics/unitree_sdk2


commit: c753829882fba461ed07ba25aaabee0a25d83663


## README

# unitree_sdk2
Unitree robot sdk version 2.

### Prebuild environment
* OS  (Ubuntu 20.04 LTS)  
* CPU  (aarch64 and x86_64)   
* Compiler  (gcc version 9.4.0) 

### Environment Setup

Before building or running the SDK, ensure the following dependencies are installed:

- CMake (version 3.10 or higher)
- GCC (version 9.4.0)
- Make

You can install the required packages on Ubuntu 20.04 with:

```bash
apt-get update
apt-get install -y cmake g++ build-essential libyaml-cpp-dev libeigen3-dev libboost-all-dev libfmt-dev
```

### Build examples

To build the examples inside this repository:

```bash
mkdir build
cd build
cmake ..
make
```

### Installation

To build your own application with the SDK, you can install the unitree_sdk2 to your system directory:

```bash
mkdir build
cd build
cmake ..
sudo make install
```

Or install unitree_sdk2 to a specified directory:

```bash
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/unitree_robotics
sudo make install
```

You can refer to `example/cmake_sample` on how to import the unitree_sdk2 into your CMake project. 

Note that if you install the library to other places other than `/opt/unitree_robotics`, you need to make sure the path is added to "${CMAKE_PREFIX_PATH}" so that cmake can find it with "find_package()".

### Notice
For more reference information, please go to [Unitree Document Center](https://support.unitree.com/home/zh/developer).


## File tree (depth 3, assets pruned)

```
.devcontainer/
  Dockerfile.devcontainer
  devcontainer.json
  docker-compose.yml
.github/
  workflows/
    c-cpp.yml
.gitignore
CMakeLists.txt
LICENSE
README.md
cmake/
  unitree_sdk2Config.cmake.in
  unitree_sdk2Targets.cmake
example/
  CMakeLists.txt
  a2/
    CMakeLists.txt
    audio/
    sport/
  as2/
    CMakeLists.txt
    sport/
  b2/
    CMakeLists.txt
    b2_sport_client.cpp
    b2_stand_example.cpp
  b2w/
    CMakeLists.txt
    b2w_sport_client.cpp
    b2w_stand_example.cpp
  g1/
    CMakeLists.txt
    audio/
    dex3/
    g1d/
    high_level/
    low_level/
  go2/
    CMakeLists.txt
    go2_low_level.cpp
    go2_robot_state_client.cpp
    go2_sport_client.cpp
    go2_stand_example.cpp
    go2_trajectory_follow.cpp
    go2_video_client.cpp
    go2_vui_client.cpp
  go2w/
    CMakeLists.txt
    go2w_sport_client.cpp
    go2w_stand_example.cpp
  h1/
    CMakeLists.txt
    README.md
    README_zh.md
    doc/
    high_level/
    low_level/
  h2/
    CMakeLists.txt
    high_level/
    low_level/
  helloworld/
    CMakeLists.txt
    HelloWorldData.cpp
    HelloWorldData.hpp
    publisher.cpp
    subscriber.cpp
  jsonize/
    CMakeLists.txt
    test_jsonize.cpp
  r1/
    CMakeLists.txt
    audio/
    high_level/
    low_level/
  state_machine/
    CMakeLists.txt
    cfg.hpp
    comm.h
    conversion.hpp
    gamepad.hpp
    main.cpp
    params/
    robot_controller.hpp
    robot_interface.hpp
    state_machine.hpp
    user_controller.hpp
  wireless_controller/
    CMakeLists.txt
    advanced_gamepad.hpp
    main.cpp
include/
  unitree/
    common/
    dds_wrapper/
    idl/
    robot/
lib/
  aarch64/
    libunitree_sdk2.a
  x86_64/
    libunitree_sdk2.a
licenses/
  Tencent/
    rapidjson/
  eclipse-cyclonedds/
    cyclonedds/
    cyclonedds-cxx/
  eclipse-iceoryx/
    iceoryx/
thirdparty/
  CMakeLists.txt
  include/
    dds/
    ddsc/
    ddscxx/
  lib/
    aarch64/
    x86_64/
```

## Config files (0)


## Python signatures and reward/observation bodies (0 files)
