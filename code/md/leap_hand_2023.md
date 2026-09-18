# leap_hand_2023

source: https://github.com/leap-hand/LEAP_Hand_API


commit: b0d00c881d0119077b2cab771a6de44f5aaec904


## README

## Welcome to the LEAP Hand SDK

👉 **More info:** [LEAP Hand Website](http://leaphand.com/)

---

### Software Setup
- See these folders for setup details:  
  - [Python API](https://github.com/leap-hand/LEAP_Hand_API/tree/main/python) 
  - [C++](https://github.com/leap-hand/LEAP_Hand_API/tree/main/cpp)
  - [ROS API](https://github.com/leap-hand/LEAP_Hand_API/tree/main/ros_module)  
  - [ROS2 API](https://github.com/leap-hand/LEAP_Hand_API/tree/main/ros2_module)  
  - [Useful Tools](https://github.com/leap-hand/LEAP_Hand_API/tree/main/useful_tools)

---

### 🔌 Hardware Setup
- Connect **5 V power** to the hand (Dynamixels should light up on boot).
- Connect the **Micro‑USB** cable (avoid multiple USB extensions).
- Use [Dynamixel Wizard](https://emanual.robotis.com/docs/en/software/rplus1/dynamixel_wizard/) to find the correct port.  
  ➡️ Put that port into `main.py` or `ros_example.py`.  
  ⚠️ You **cannot** have Dynamixel Wizard open while using the API (the port will be busy).
- On Ubuntu, find the hand by ID at `/dev/serial/by-id` (persistent across reboots).
- `sudo chmod 666 /dev/serial/by-id/(your_id)` to give serial port permissions.
- Official support: **Python** and **C++** and **ROS/ROS2**. 
  Other languages can use the [Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/).
- To improve latency on Ubuntu:  
  - [Adjust USB Latency Settings](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/)  
  - Tune the [Dynamixel Python SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK/issues/288)  
  - Set *Return Delay Time* (Control Table Register 9) from 250 µs to **0 µs**.
- If you are using the full hand, you can raise the current limit from 300 mA to 550 mA in the API for increased strength!
---

### 🤖 Functionality
- Leap Node allows commanding joint angles in different scalings.
- You can read **position, velocity, and current**.
- **Query limits:**  
  - Position only: ≤ 500 Hz  
  - Position + velocity + current: ≤ 500 Hz  
  (Higher rates can slow USB communication.)
- Default control: **PID** (up to current limit).  
  Velocity and current control also supported—see the [motor manual](https://emanual.robotis.com/docs/en/dxl/x/xc330-m288/).
- Current limits:  
  - Lite: ≈ 300 mA  
  - Full: up to ≈ 550 mA
  - **By default the API is at 300, you can raise it to 550mA on the Full hand!!!**
- Jittery hand? ➡️ Lower P/D values.  
  Weak hand? ➡️ Raise P/D values.

---

### 🛠️ Troubleshooting
- Motor off by 90°/180°/270° → **Remount the horn.**
- No motors show up → Check **serial port permissions**.
- Some motors missing → Verify **IDs** and **U2D2 connections**.
- Overload error (motors flashing red) → **Power cycle**. If frequent, **lower current limits**.
- Jittery motors → Lower P/D values.
- Inaccurate motors → Raise P/D values.

---

### 🔧 Useful Tools
- **MANO → LEAP** joint angle mapping.
- [Bimanual Dexterity for Complex Tasks](https://bidex-teleop.github.io/) shows how to use **Manus gloves** with LEAP Hand.
- Have a useful tool to share? **Pull requests welcome!**  
  (Or ask and I can add tools for you.)

---

### Support
- Questions/issues: **kshaw2@andrew.cmu.edu**
- **License:**  
  - Code: MIT License  
  - CAD: CC BY‑NC‑SA (non‑commercial use with attribution)
- Provided **as‑is**, without warranty.

**If you use LEAP Hand in research, please cite:**
```bibtex
@article{shaw2023leaphand,
  title={LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning},
  author={Shaw, Kenneth and Agarwal, Ananye and Pathak, Deepak},
  journal={Robotics: Science and Systems (RSS)},
  year={2023}
}


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
cpp/
  CMakeLists.txt
  dynamixel_sdk/
    build/
    example/
    include/
    keywords.txt
    library.properties
    src/
  include/
    leap_hand_utils/
  readme.md
  src/
    dynamixel_client.cpp
    leap_controller.cpp
    leap_hand_utils.cpp
    main.cpp
python/
  leap_hand_utils/
    __init__.py
    dynamixel_client.py
    leap_hand_utils.py
  main.py
  readme.md
readme.md
ros2_module/
  CMakeLists.txt
  launch/
    launch_leap.py
  package.xml
  readme.md
  scripts/
    leap_hand_utils/
    leaphand_node.py
    ros2_example.py
  srv/
    LeapEffort.srv
    LeapPosVelEff.srv
    LeapPosition.srv
    LeapVelocity.srv
ros_module/
  CMakeLists.txt
  example.launch
  leap_hand_utils/
    __init__.py
    dynamixel_client.py
    leap_hand_utils.py
  leaphand_node.py
  package.xml
  readme.md
  ros_example.py
  srv/
    leap_effort.srv
    leap_pos_vel_eff.srv
    leap_position.srv
    leap_velocity.srv
useful_tools/
  mano_to_leap_mapping.py
```

## Config files (0)


## Python signatures and reward/observation bodies (11 files)


### python/leap_hand_utils/dynamixel_client.py

```
"""Communication using the DynamixelSDK."""
def dynamixel_cleanup_handler()
def signed_to_unsigned(value, size)
def unsigned_to_signed(value, size)
class DynamixelClient()
    """Client for communicating with Dynamixel motors.

NOTE: This only supports Protocol 2."""
    def __init__(self, motor_ids, port, baudrate, lazy_connect, pos_scale, vel_scale, cur_scale)
    def is_connected(self)
    def connect(self)
    def disconnect(self)
    def set_torque_enabled(self, motor_ids, enabled, retries, retry_interval)
    def read_pos_vel_cur(self)
    def read_pos_vel(self)
    def read_pos(self)
    def read_vel(self)
    def read_cur(self)
    def write_desired_pos(self, motor_ids, positions)
    def write_byte(self, motor_ids, value, address)
    def sync_write(self, motor_ids, values, address, size)
    def check_connected(self)
    def handle_packet_result(self, comm_result, dxl_error, dxl_id, context)
    def convert_to_unsigned(self, value, size)
    def __enter__(self)
    def __exit__(self)
    def __del__(self)
class DynamixelReader()
    """Reads data from Dynamixel motors.

This wraps a GroupBulkRead from the DynamixelSDK."""
    def __init__(self, client, motor_ids, address, size)
    def read(self, retries)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelCurReader(DynamixelReader)
    """Reads positions, currents and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelCurReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
```

### python/leap_hand_utils/leap_hand_utils.py

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

### ros2_module/scripts/leap_hand_utils/dynamixel_client.py

```
"""Communication using the DynamixelSDK."""
def dynamixel_cleanup_handler()
def signed_to_unsigned(value, size)
def unsigned_to_signed(value, size)
class DynamixelClient()
    """Client for communicating with Dynamixel motors.

NOTE: This only supports Protocol 2."""
    def __init__(self, motor_ids, port, baudrate, lazy_connect, pos_scale, vel_scale, cur_scale)
    def is_connected(self)
    def connect(self)
    def disconnect(self)
    def set_torque_enabled(self, motor_ids, enabled, retries, retry_interval)
    def read_pos_vel_cur(self)
    def read_pos_vel(self)
    def read_pos(self)
    def read_vel(self)
    def read_cur(self)
    def write_desired_pos(self, motor_ids, positions)
    def write_byte(self, motor_ids, value, address)
    def sync_write(self, motor_ids, values, address, size)
    def check_connected(self)
    def handle_packet_result(self, comm_result, dxl_error, dxl_id, context)
    def convert_to_unsigned(self, value, size)
    def __enter__(self)
    def __exit__(self)
    def __del__(self)
class DynamixelReader()
    """Reads data from Dynamixel motors.

This wraps a GroupBulkRead from the DynamixelSDK."""
    def __init__(self, client, motor_ids, address, size)
    def read(self, retries)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelCurReader(DynamixelReader)
    """Reads positions, currents and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelCurReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
```

### ros2_module/scripts/leap_hand_utils/leap_hand_utils.py

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

### ros2_module/scripts/leaphand_node.py

```
class LeapNode(Node)
    def __init__(self)
    def _receive_pose(self, msg)
    def _receive_allegro(self, msg)
    def _receive_ones(self, msg)
    def pos_srv(self, request, response)
    def vel_srv(self, request, response)
    def eff_srv(self, request, response)
    def pos_vel_srv(self, request, response)
    def pos_vel_eff_srv(self, request, response)
def main(args)
```

### ros_module/leap_hand_utils/dynamixel_client.py

```
"""Communication using the DynamixelSDK."""
def dynamixel_cleanup_handler()
def signed_to_unsigned(value, size)
def unsigned_to_signed(value, size)
class DynamixelClient()
    """Client for communicating with Dynamixel motors.

NOTE: This only supports Protocol 2."""
    def __init__(self, motor_ids, port, baudrate, lazy_connect, pos_scale, vel_scale, cur_scale)
    def is_connected(self)
    def connect(self)
    def disconnect(self)
    def set_torque_enabled(self, motor_ids, enabled, retries, retry_interval)
    def read_pos_vel_cur(self)
    def read_pos_vel(self)
    def read_pos(self)
    def read_vel(self)
    def read_cur(self)
    def write_desired_pos(self, motor_ids, positions)
    def write_byte(self, motor_ids, value, address)
    def sync_write(self, motor_ids, values, address, size)
    def check_connected(self)
    def handle_packet_result(self, comm_result, dxl_error, dxl_id, context)
    def convert_to_unsigned(self, value, size)
    def __enter__(self)
    def __exit__(self)
    def __del__(self)
class DynamixelReader()
    """Reads data from Dynamixel motors.

This wraps a GroupBulkRead from the DynamixelSDK."""
    def __init__(self, client, motor_ids, address, size)
    def read(self, retries)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelCurReader(DynamixelReader)
    """Reads positions, currents and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelPosReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelVelReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
class DynamixelCurReader(DynamixelReader)
    """Reads positions and velocities."""
    def __init__(self, client, motor_ids, pos_scale, vel_scale, cur_scale)
    def _initialize_data(self)
    def _update_data(self, index, motor_id)
    def _get_data(self)
```

### ros_module/leap_hand_utils/leap_hand_utils.py

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

### ros_module/leaphand_node.py

```
class LeapNode()
    def __init__(self)
    def _receive_pose(self, pose)
    def _receive_allegro(self, pose)
    def _receive_ones(self, pose)
    def pos_srv(self, req)
    def vel_srv(self, req)
    def eff_srv(self, req)
    def pos_vel_srv(self, req)
    def pos_vel_eff_srv(self, req)
def main()
```