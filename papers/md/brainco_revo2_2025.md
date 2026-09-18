# BrainCo Revo 2 dexterous hand

source entry: brainco_revo2_2025


## https://www.brainco-hz.com/docs/revolimb-hand/en/revo2/parameters.html

Skip to content

[BrainCo Hand](/docs/revolimb-hand/en/)

Search```K`

Main Navigation [Revo 1](/docs/revolimb-hand/en/revo1/getting_started.html)[Revo 2](/docs/revolimb-hand/en/revo2/getting_started.html)[Revo 3](/docs/revolimb-hand/en/revo3/sdk/quickstart.html)[Integrations](/docs/revolimb-hand/en/ecology/)

English

[简体中文](/docs/revolimb-hand/revo2/parameters.html)

English

[简体中文](/docs/revolimb-hand/revo2/parameters.html)

Menu

Return to top

Sidebar Navigation 

## Revo 2

[Getting Started](/docs/revolimb-hand/en/revo2/getting_started.html)

[Overview](/docs/revolimb-hand/en/revo2/parameters.html)

[Download](/docs/revolimb-hand/en/revo2/download.html)

[Desktop Tool Guide](/docs/revolimb-hand/en/revo2/guide.html)

## SDK

[Get SDK](/docs/revolimb-hand/en/revo2/get_sdk.html)

[Python SDK](/docs/revolimb-hand/en/revo2/python_sdk.html)

[C/C++ SDK](/docs/revolimb-hand/en/revo2/c_sdk.html)

[Adaptive Grasping Example](/docs/revolimb-hand/en/revo2/tactile_grasp.html)

## Protocol

[Overview](/docs/revolimb-hand/en/revo2/introduction.html)

[Modbus / CAN FD Basic](/docs/revolimb-hand/en/revo2/modbus_foundation.html)

[Modbus / CAN FD Pro](/docs/revolimb-hand/en/revo2/modbus_pro.html)

[Modbus / CAN FD Touch](/docs/revolimb-hand/en/revo2/modbus_touch.html)

[EtherCAT](/docs/revolimb-hand/en/revo2/ethercat.html)

[Firmware Changelog](/docs/revolimb-hand/en/revo2/changelog.html)

[FAQ](/docs/revolimb-hand/en/revo2/faq.html)

On this page




# Overview ​

BrainCo Revo 2 is a bionic dexterous hand for robot integration and research. It provides 6 active joints and 11 degrees of freedom, supports RS485, CAN FD, and EtherCAT communication interfaces, and provides SDK support for Linux, Windows, and ROS workflows. The device includes closed-loop servo control, custom gesture definitions, and protections for current, stall, high temperature, and collision conditions.

## Product size ​

## Product parameters ​

Product name| Product rendering image  
---|---  
Biomimetic dexterous hand Revo 2|   
Standard colors: Space Gray, Silver (supports bulk color customization)  
Model| BASIC| PRO| TOUCH  
Version code| XRL/XRR| XEL/XER| XTL/XTR  
**Main parameters**|  degree of freedom| 11（6 active）  
Weight | 383 g  
Height (from the base of the palm to the tip of the middle finger)| 160 mm  
Full fist grip force| ≥50N  
Pinch force| ≥15N  
Max Payload| ≥20kg  
Operating Noise (at 50cm)| ≤50dB  
Flexion/Extension Speed| ≤0.65s  
Communication interface| 485  
CANfd| 485  
CANfd  
EtherCAT| 485  
CANfd  
EtherCAT  
Supply voltage| 12-28V| 12-64V| 12-64V  
Static Current| 65 mA @24V| 115 mA @24V| 115 mA @24V  
No-load Average Current (five-finger flexion and extension)| 350mA @24V| 390mA @24V| 390mA @24V  
Maximum Current| 4.6 A @24V| 4.65A @24V| 4.65A @24V  
Repetitive control precision| 0.1°| 0.1°| 0.1°  
Maximum opening and closing distance| 100mm(from thumb to index finger)  
Operating temperature| -10 - 40℃ / 90%RH  
Tactile module| /| Multi-dimensional fingertip tactile module  
Smart Control| Position, velocity, current feedback control  
Cascaded control, compliance control| Position, velocity, current feedback control  
Cascaded control, compliance control  
Tactile Adaptive Control  
Smart Protection| Current protection, stall protection, high-temperature protection, anti-collision protection  
SDK integration| SDK supports Python/C and is compatible with Linux/Windows/ROS systems.  
Online upgrade| Support OTA online upgrades  
  
## Parameter description ​

### Degree of freedom distribution ​

The Revo 2 dexterous hand has 6 active joints and a total of 11 degrees of freedom. The thumb has two active degrees of freedom for abduction and adduction, as well as one passive degree of freedom for flexion and extension, while each of the remaining four fingers has one active degree of freedom for flexion and extension and one passive degree of freedom for flexion and extension.

### Range of motion ​

Active Joint| Degrees of Freedom| Minimum Angle (°)| Maximum Angle (°)  
---|---|---|---  
Thumb Flex| Flexion/Extension| 0| 59  
Thumb Aux| Adduction/Abduction| 0| 90  
Index Finger| Flexion/Extension| 0| 81  
Middle Finger| Flexion/Extension| 0| 81  
Ring Finger| Flexion/Extension| 0| 81  
Little Finger| Flexion/Extension| 0| 81  
  
### Definition of the back of hand light status ​

Light Effect| Description  
---|---  
Green light blinking| Powering on (not completed reset)  
Green light solid| Normal operation (reset completed)  
Yellow light blinking| Power supply too low  
Cyan light solid| OTA upgrading in progress  
Red light solid| Abnormal  
  
### Back of hand button function description ​

Function| Button  
---|---  
Reset| Short press  
Restore factory settings| Long press for 5 seconds  
Fist gesture| Short press 2 times  
  
### Motor ID and status ​

Motor ID| Description  
---|---  
FINGERID_THUMB| Thumb Flex  
FINGERID_THUMB_AUX| Thumb Aux  
FINGERID_INDEX| Index  
FINGERID_MIDDLE| Middle  
FINGERID_RING| Ring  
FINGERID_PINKY| Pinky  
Motor status| Description  
---|---  
MOTOR_IDLE| Joint Idle  
MOTOR_RUNNING| Joint Running  
MOTOR_STALL| Joint Stall  
MOTOR_TURBO| turbo  
  
### Control Mode Description ​

Mode Value| Control Mode| Description  
---|---|---  
1| Position + Time| Move to the target position within the specified duration time. If the time is set to 0, it operates at maximum speed.  
2| Position + Speed| Move to the target position at the specified speed limit. If the speed is set to 0, it operates at maximum speed.  
3| Speed| Move continuously at the target speed until a limit is reached or a physical stall occurs.  
4| Current| Maintain the target current continuously until a limit is reached or a physical stall occurs.  
5| PWM| Maintain the target PWM duty cycle continuously until a limit is reached or a physical stall occurs.  
  
### Turbo Mode Description ​

Turbo mode is based on stall detection. When a finger stalls against an object, it pauses for the configured stall duration and then continues gripping at 500 ms intervals. This mode can be used when the hand needs to maintain grip on soft or shifting objects.

### Device ID description ​

For Revo 2, default ID for the left hand is 126, and for the right hand, it is 127. Users can modify them within the range of 1 - 254.

### Description of the power-on auto-calibration process ​

The automatic reset upon powering on refers to the dexterous hand automatically executing a position calibration sweep after being powered on. Upon startup, the dexterous hand will search for the starting origin bounds of the fingers, during which all fingers will be set in motion.

Note 1: During the position calibration process, if the dexterous hand is currently gripping an object, it will drop the object.

Note 2: After the dexterous hand is powered on, position calibration must be completed successfully before normal control is permitted.

### Communication interface description ​

#### Revo 2 Basic ​

The basic version of the second-generation hand can communicate and control via the 485 or CAN FD communication interface. The interface is located under the wrist, and the connector model is BM05B-PASS-TFT(LF)(SN)。

#### Revo 2 Pro&Touch ​

The second generation hand advanced version and tactile version support three communication interfaces: 485/CAN FD/EtherCAT for communication and control, with the interface located below the wrist.

Interface| Connector Model  
---|---  
485| A1257WV-S-2P-6T  
CAN FD| A1257WV-S-2P-6T  
EtherCAT| A1257WV-S-5P-6T  
VCC| XT30UPB-M  
  
Last updated: 

Pager

[PreviousGetting Started](/docs/revolimb-hand/en/revo2/getting_started.html)

[NextDownload](/docs/revolimb-hand/en/revo2/download.html)

Copyright © 2018-present BrainCo Inc.

[Help](https://web.static.brainco.cn/work-order "Help")
