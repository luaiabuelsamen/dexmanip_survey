# psyonic_ability_hand_2021

source: https://github.com/psyonicinc/ability-hand-api


commit: 34c9a9324d3739d976e6de441e56ccefafd0000b


## README

## Ability Hand API

This repository contains the [PSYONIC Ability Hand API documentation](https://github.com/psyonicinc/ability-hand-api/blob/master/Documentation/ABILITY-HAND-ICD.pdf) and examples/wrappers using the API. 

 - [Python](https://github.com/psyonicinc/ability-hand-api/tree/master/python) (Linux, Windows, MacOS)
 - Simulation ([Mujoco](https://github.com/psyonicinc/ability-hand-api/tree/master/python/ah_simulators#mujoco), [Isaac](https://github.com/psyonicinc/ability-hand-api/tree/master/python/ah_simulators#isaac-simulator-45))
 - [ROS2](https://github.com/psyonicinc/ability-hand-ros2/tree/main)
 - [C++](https://github.com/psyonicinc/ability-hand-api/tree/master/cpp) (Linux, Windows) 
 - [MATLAB](https://github.com/psyonicinc/ability-hand-api/tree/master/MATLAB) (Legacy I2C API Only)


See the README.md in individual folders for more information.  

# Quickstart Guide

### Connect Ability Hand and serial adapter

Ensure you connect the ABILITY HAND, POWER SWITCH and BREAKOUT BOARD correctly.
Windows users will first need to [install drivers](https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip)
for the USB serial adapter.

<img src="python/images/ah_wiring_guide.png" alt="isolated" width="600"/>

1. Connect PWR (POWER SWITCH) ➡️ PWR CONNECTOR (BREAKOUT BOARD) 
2. 6 PIN (ABILITY HAND) ➡️ 6 PIN (BREAKOUT BOARD)  
3. GND (SERIAL ADAPTER) ➡️ GND (BREAKOUT BOARD)
4. RXD (SERIAL ADAPTER) ➡️ SCL (BREAKOUT BOARD) 
5. TXD (SERIAL ADAPTER) ➡️ SDA (BREAKOUT BOARD)
6. SERIAL ADAPTER ➡️ COMPUTER
7. Connect Lipo Battery ➡️ BAT (POWER SWITCH)
8. Power on Ability Hand (hold power button for 1 second then release when you see the white LED)
9. You will see the LED flash red then go solid red

#### Connect to Power Supply (Optional)

If you choose you can strip the wires going to the Ability Hand Power Switch
and connect them directly to a power supply providing 8-12 volts.

<img src="python/images/ah_wiring_guide_ps.png" alt="isolated" width="600"/>

Linux users will need to issue the following command after plugging in USB 
serial adapter.

`sudo chmod a+rw /dev/ttyUSB*` 

To avoid having to issue the above command every time you can issue:

`sudo usermod -aG dialout $USER`

And restart your computer.

### Enable UART Using App

The hand ships in I2C mode but UART is recommended, to enable UART using the 
PSYONIC mobile app:

Scan ➡️ SELECT HAND ➡️ Gear Icon ⚙️
(Top Right) ➡️ Troubleshoot ➡️ Developer Mode

and issue the following command

```We16```

#### Enabling RS-485

If using an RS-485 serial adapter, you will additionally need to issue the following command

```We35```

And connect as follows:

1. GND (SERIAL ADAPTER) ➡️ GND (BREAKOUT BOARD)
2. A (SERIAL ADAPTER) ➡️ SCL (BREAKOUT BOARD) 
3. B (SERIAL ADAPTER) ➡️ SDA (BREAKOUT BOARD)

### Run Examples

You are now ready to run examples using [Python](https://github.com/psyonicinc/ability-hand-api/tree/master/python)
(*recommended for new users*) or [C++](https://github.com/psyonicinc/ability-hand-api/tree/master/cpp).  
See their respective README's for instructions on getting started.

### Power off Ability Hand

To power off the hand hold the power button for 1 second, the white LED will 
pulse, then go out, indicating that the power is off.

### Charging The Battery

You can charge the Lipo battery by plugging the provided USB-C charger to the 
ABILITY HAND POWER SWITCH.  You can leave everything connected, but you cannot 
operate the Ability Hand while it is charging.


## File tree (depth 3, assets pruned)

```
.gitignore
Arduino/
  examplecode.ino
Documentation/
  ABILITY-HAND-ICD.pdf
LICENSE
MATLAB/
  bluetooth/
    ble_fctl.m
    ble_finger_control_example.m
    ble_plot_cost_cooled.m
    ble_plot_fingerpos.m
    ble_plot_float.m
    ble_plot_fsr.m
    ble_plot_imu.m
    ble_plot_peus.m
    ble_plot_qdot.m
    ble_plot_qprog.m
    textChanged.m
    unpack_8bit_into_12bit.m
  get_abh_4bar_driven_angle.m
  get_intersection_circles.m
README.md
URDF/
  README.md
  ability_hand_left_large.urdf
  ability_hand_left_small.urdf
  ability_hand_right_large.urdf
  ability_hand_right_large_no_fsr.urdf
  ability_hand_right_small.urdf
  models/
    FB_palm_ref.STL
    FB_palm_ref_MIR.STL
    WRISTADAPTER.STEP
    WRISTADAPTER_MIR.STL
    full_model_fused_no_wrist.stl
    full_model_fused_with__wrist.stl
    idx-F1-hull.STL
    idx-F1.STL
    idx-F2-Lg-hull.STL
    idx-F2-Lg.STL
    idx-F2-hull.STL
    idx-F2.STL
    palm_hull.STL
    palm_hull_mir.STL
    thumb-F1-MIR-hull.STL
    thumb-F1-MIR.STL
    thumb-F1-hull.STL
    thumb-F1.STL
    thumb-F2-hull.STL
    thumb-F2-left.STL
    thumb-F2-right.STL
    wristmesh.STL
cpp/
  .gitignore
  .reformat.sh
  CMakeLists.txt
  LICENSE
  README.md
  ah_wrapper/
    CMakeLists.txt
    include/
    src/
  hand_wave.cpp
  main.cpp
python/
  .gitignore
  .reformat.sh
  CHANGELOG.md
  README.md
  ah_examples/
    README.md
    __init__.py
    hand_wave.py
    observer_example.py
    plot_motors.py
    plot_motors_and_touch.py
    plot_read_only.py
    plot_touch_sensors.py
    send_misc_msg.py
    simulated_hand_wave.py
    speed_tests.py
    validate_hand.py
    write_registers.py
  ah_plotting/
    __init__.py
    plots.py
    touch_sensor_legend_sml.png
  ah_simulators/
    README.md
    __init__.py
    ah_mujoco.py
    mujoco_xml/
    requirements.txt
  ah_wrapper/
    __init__.py
    ah_api.py
    ah_parser.py
    ah_serial_client.py
    functions.py
    hand.py
    observer.py
    ppp_stuffing.py
    serial_connection.py
    sim_functions.py
    sim_serial.py
    sim_serial_connection.py
  config.py
  finger_4bar/
    abh_finger_4bar.py
    linfit_4bar.py
  requirements.txt
  setup.py
  tests/
    __init__.py
    config.py
    test_mock_data.py
    test_observer.py
    test_ppp_stuffing.py
    test_serial_connection_simulated.py
    test_state_machine.py
```

## Config files (0)


## Python signatures and reward/observation bodies (16 files)


### python/ah_examples/hand_wave.py

```
def main()
```

### python/ah_examples/observer_example.py

```
class MyObserver(Observer)
    def __init__(self)
    def update_fsr(self, fsr)
    def update_pos(self, position)
    def update_vel(self, velocity)
    def update_hot_cold(self, hot_cold)
    def update_cur(self, current)
def main()
```

### python/ah_examples/simulated_hand_wave.py

```
def main()
```

### python/ah_examples/validate_hand.py

```
def get_average_finger_positions(positions)
def validate_velocity()
def validate_position()
def validate_torque()
def validate_fsr()
def validate_grips()
def main()
```

### python/ah_simulators/ah_mujoco.py

```
class Controller()
    def __init__(self, hand, model, left_hand)
    def actuate(self, data)
    def mimic_joints(self, data)
class AHMujocoSim()
    def __init__(self, scene, hand, left_hand)
    def mujoco_loop(self)
```

### python/ah_wrapper/hand.py

```
class Hand(Observable)
    def __init__(self, addr, fsr_offset)
    def _update_cur(self, positions, velocity, current, fsr)
    def update_tar(self, positions, velocities, currents, duties)
    def update_hot_cold(self, hot_cold_status)
    def get_hot_cold(self)
    def get_current(self)
    def get_position(self)
    def get_velocity(self)
    def get_fsr(self)
    def get_tar_position(self)
    def get_tar_velocity(self)
    def get_tar_current(self)
    def get_tar_duty(self)
    def __repr__(self)
```

### python/ah_wrapper/observer.py

```
class Observable()
    def __init__(self)
    def add_observer(self, observer)
    def remove_observer(self, observer)
    def notify_observers(self)
    def notify_pos(self, position)
    def notify_vel(self, velocity)
    def notify_cur(self, current)
    def notify_fsr(self, fsr)
    def notify_hot_cold(self, hot_cold)
class Observer(ABC)
    def update(self, observable)
    def update_pos(self, position)
    def update_vel(self, velocity)
    def update_cur(self, current)
    def update_fsr(self, fsr)
    def update_hot_cold(self, hot_cold)
```

### python/ah_wrapper/sim_functions.py

```
class GeneratedPacket()
    def __init__(self, pos, cur, vel, fsr, reply_mode, mode)
    def generate_packet(self)
```

### python/ah_wrapper/sim_serial.py

```
class Serial()
    """Simulated version of the python serial.Serial library with"""
    def __init__(self, port, baud_rate, read_size)
    def read(self, read_size)
    def write(self, msg)
```

### python/ah_wrapper/sim_serial_connection.py

```
class SimSerialConnection(SerialConnectionBase)
    def __init__(self, port, baud_rate, read_size)
    def _connect(self, port, baud_rate)
    def close(self)
```

### python/tests/test_observer.py

```
class Foo(Observer)
    def update_pos(self, position)
    def update_vel(self, velocity)
    def update_cur(self, current)
    def update_fsr(self, fsr)
    def update_hot_cold(self, hot_cold)
def test_observer()
```