

## **Shadow Dexterous Hand** 

**Technical Specification December 2024** 



> © Shadow Robot Company 2024. All rights reserved 



# **Table of Contents** 

|**1 Overview**|**4**|
|---|---|
|**2 Mechanical Profile**|**5**|
|2.1 Dimensions|5|
|2.2 Kinematic Diagram|6|
|2.3 Kinematic Structure|7|
|2.4 Weight and Payload|7|
|2.5 Speed|7|
|2.6 Material|8|
|**3 Communications**|**8**|
|3.1 Motor Hand Features|8|
|3.2 Control|8|
|3.3 Micro-controllers|8|
|**4 Sensing**|**9**|
|4.1 Position|9|
|4.2 Tactile Sensing|9|
|4.3 Force|9|
|4.4 Temperature and Current|10|
|4.5 Hand Sensor Node|10|
|**5 Actuation**|**10**|
|**6 PC and Software**|**10**|
|6.1 Open Platform|10|
|6.2 ROS|10|
|**7 Power**|**11**|
|**8 Options**|**11**|
|8.1 Left Hand|11|
|8.2 Universal Robot Arm Integration|11|



**Shadow Dexterous Hand - Technical Specifications** 

**1** 



### **1 Overview** 

The Shadow Dexterous Hand is an advanced humanoid robot hand system that provides 24 movements to reproduce the human hand's kinematics and dexterity as closely as possible. It has been designed to provide comparable force output and movement precision to the human hand. 

Shadow Hand systems have been used for research in grasping, manipulation, neural control, brain-computer interface, industrial quality control, and hazardous material handling. 

The Shadow Dexterous Hand is a self-contained system - all actuation and sensing are built into the hand and forearm. The Shadow Dexterous Hand development kit includes: 

- Control systems 

- Software (provided under GNU GPL or BSD as appropriate) 

- ROS compliant 

- PC 

- Power supplies 

- Tactile sensing 

- Auxiliary equipment (if required) 

- Documentation and training 

All versions of the Hand use an EtherCAT bus (Ethernet for Control Automation Technology), providing a 100Mbps Ethernet-based communications field bus and full integration into ROS (Robot Operating System). 

The Hands use Shadow's electric “Smart Motor” actuation system and integrates force and position control electronics, motor drive electronics, motor, gearbox, force sensing and communications into a compact module, 20 of which are packed into the Hand base. 

**Shadow Dexterous Hand - Technical Specifications** 

**2** 



### **2 Mechanical Profile** 

#### **2.1 Dimensions** 

The Hand has been designed to be similar in shape and size to a typical male hand and reproduce as closely as possible the kinematics and dexterity of the human hand. The fingers are all the same length, with the knuckles staggered to give comparable fingertip locations to the human hand. 



**Shadow Dexterous Hand - Technical Specifications** 

**3** 



#### **2.2 Kinematic Diagram** 



**Shadow Dexterous Hand - Technical Specifications** 

**4** 



#### **2.3 Kinematic structure** 

The Dexterous Hand kinematics are optimized to be as close as possible (within engineering constraints) to the kinematics of the human hand. 

|**Joint(s)**|**Deg**<br>**Min**|**rees**<br>**Max**|**Radi**<br>**Min**|**ans**<br>**Max**|**Notes**|
|---|---|---|---|---|---|
|FF1, MF1, RF1, LF1|0|90|0|1.571|ld|
|FF2, MF2, RF2, LF2|0|90|0|1.571|Coupe|
|FF3, MF3, RF3, LF3|-15|90|-0.262|1.571||
|FF4, MF4, RF4, LF4|-20|20|-0.349|0.349||
|LF5|0|45|0|0.785||
|TH1|-15|90|-0.262|1.571||
|TH2|-40|40|-0.698|0.698||
|TH3|-12|12|-0.209|0.209||
|TH4|0|70|0|1.222||
|TH5|-60|60|-1.047|1.047||
|WR1|-40|28|-0.698|0.489||
|WR2|-28|8|-0.489|0.140||



The thumb has 5 degrees of freedom and 5 joints. Each finger has 3 degrees of freedom and 4 joints. 

The distal joints of the fingers are coupled in a manner similar to a human finger, such that the angle of the middle joint is always greater than or equal to the angle of the distal joint. This allows the middle phalange to bend while the distal phalange is straight. The little finger has an extra joint in the palm provided to allow opposition to the thumb. 

All joints except the finger distal joints are controllable to +/- 1° across the full range of movement. 

#### **2.4 Weight and Payload** 

The Hand and forearm have a total weight of 4.3 kg. The Hand, while in a power grasp, can hold up to 4 kg. 

**Shadow Dexterous Hand - Technical Specifications** 

**5** 



#### **2.5 Speed** 

Movement speed is dependent on safety settings in the control system. Typical parameters allow a full-range joint movement in free space to operate at a frequency of 1.0 Hz. 

#### **2.6 Material** 

The entire system is built with a combination of metals and plastics, including aluminium, brass, acetyl, polycarbonate and polyurethane flesh. 

### **3 Communications** 

All versions of the Hand use an EtherCAT bus. EtherCAT (Ethernet for Control Automation Technology) is a 100Mbps ethernet-based fieldbus. It is currently used in a number of systems, such as Willow Garage's PR2 robot, making these versions of the Hand compatible with the PR2 and any other research or industrial control systems that are EtherCAT/ROS compatible. The EtherCAT bus plus ROS requires a powerful multi-core PC (supplied) with a standard Ethernet port. The EtherCAT protocol used by the hand is simple since the position control loop happens in the host. 

#### **3.1 Motor Hand Features** 

- Enable and disable torque control 

- Change torque control PID values 

- Change operational limits such as force and temperature cut-outs 

- Reset motors 

- Adjust data transmission rates for motors and tactile sensors 

- Track error and status indicators from the components 

- Download new firmware into the Smart Motor modules 

#### **3.2 Control** 

As standard, the EtherCAT Hand implements a position control strategy in the host PC. Other control algorithms can be used as much more complex control strategies can be implemented, fusing information from joint and tactile sensors and even visual signals via ROS. 

The torque loop is closed inside the motor unit at 5kHz. The PID settings for this loop can be changed in real-time. Alternatively, new firmware can be downloaded into the motor 

**Shadow Dexterous Hand - Technical Specifications** 

**6** 



units if you require a different control strategy, or a new version is available from Shadow. All other control loops run at 1kHz through the host. 

The PID controllers are set up in the configuration or boot phase of the system, can be changed on the fly, and can be configured to operate from sensor data, permitting control of joint position, force, or user-supplied parameters. 

#### **3.3 Micro-controllers** 

Microchip PIC18Fxx80 microcontrollers are used for embedded control throughout the robot system, except on the palm, where a PIC32 is used, and on the tactile sensors, where PSoCs are used. The firmware is available upon request by the customer under a Non-Disclosure Agreement (NDA). All microcontrollers are connected to the internal bus and can be accessed via the EtherCAT interface. 

### **4 Sensing** 

All sensor data are presented to the PC at various rates depending on the rate-setting for that sensor. Typical rates are: 

||**Update Rate**|**Bits**|
|---|---|---|
|**Position**|1000 Hz|12|
|**Tactile**|1000 Hz|12|
|**Force**|500 Hz|12|
|**Temperature**|100 Hz|12|
|**Current**|100 Hz|12|
|**Voltage**|100 Hz|12|



#### **4.1 Position** 

A Hall effect sensor senses the rotation of each joint locally with a typical resolution of 0.2 degrees. This data is sampled in the Hand by 12-bit ADCs. Data is provided to the communication bus in raw form and calibrated at the host. 

#### **4.2 Tactile Sensing** 

All Shadow Hands come with two Shadow Tactile Fingertips (STFs) fitted on the thumb and index finger as standard. Additional sensors can be purchased. 

**Shadow Dexterous Hand - Technical Specifications** 

**7** 



The STF has 17 x 3 DoF taxels. Each taxel consists of a magnet and an accompanying 3-axis Hall effect sensor. The data is uncalibrated and sampled by a 12-bit ADC. 

#### **4.3 Force** 

A separate force sensor measures the load in each of the pairs of tendons driven by the Smart Motor unit. This data is captured by 12-bit ADCs and used locally for torque control. The data are also transmitted back to the PC. The sensors have a resolution of about 30mN. They are zeroed but not calibrated. I.e. a reading of zero means zero difference between the tendons. 

#### **4.4 Temperature and Current** 

The current flow through the motor unit and the temperature of the motor unit are measured internally by the Smart Motor unit and are used to ensure safety and reliability. 

#### **4.5 Hand Sensor Node** 

The Hand Sensor Node, which is made up of a number of PCBs throughout the palm, fingers and thumb, reads joint position data and tactile sensing data, provides this to the communication bus in raw form, and is calibrated at the host. Other sensors can be attached to the Hand sensor node by request and arrangement. 

### **5 Actuation** 

Each of the twenty Smart Motor nodes drives a Maxon motor using PWM. The Smart Motor node implements a PID controller, which can be set to do force control on the tendons at the motor end or position control on the joints. 

### **6 PC and Software** 

All Hands are supplied with a standard multi-core laptop running Ubuntu with an EtherCAT-compatible network port (more optional). The drivers and other useful packages are installed by default on the computer. The software is based on the ROS meta-operating system. 

Software in the host PC provides sensor calibration and scaling, mappings from sensor names to hardware, and permits easy access to all robot facilities from Python and/or C++. 

**Shadow Dexterous Hand - Technical Specifications** 

**8** 



#### **6.1 Open platform** 

- All source codes for the micro-controllers and schematics for the electronics subsystems are available on request under the Non-Disclosure Agreement (NDA). 

- Example code along with documentation is provided, along with access to e-mail support from Shadow. 

- Solid models (VRML) and kinematic data are supplied via ROS. 

- An open software layer supports easy interfacing between this and other systems, as well as quick prototyping of algorithms and tools. 

#### **6.2 ROS** 

The Shadow Dexterous Hand is fully compatible with ROS (Robot Operating System www.ros.org), providing a full range of capabilities, including: 

- Control 

- Visualisation 

- Simulation 

A repository provides a simulated model of the Hand running in the Gazebo simulator. It integrates a full physics model for grasping and manipulation development. The shadow_robot_ethercat stack provides the drivers for the Hand. 

All the back-ends (simulated or real) present the same interface to your software - the selection is simply made depending on which launch file is used, be it the real Hand or the simulated Hand - making it easy to test software away from the hardware and then run on the real hardware. 

### **7 Power** 

Power supplies are provided with the Hand: 

- 48 V @ 2.5 A 

**Shadow Dexterous Hand - Technical Specifications** 

**9** 



### **8 Options** 

The following options may be selected at the time of ordering. 

#### **8.1 Left Hand** 

The Left Hand is functionally identical to the standard Hand but mirrored for use in a bi-manual system. 

#### **8.2 Universal Robot Arm Integration** 

The Dexterous Hand system can be supplied and integrated with a **UR10e robot arm.** 



#### **Shadow Robot Company** 

Unit 31, Spectrum House 32-34 Gordon House Rd London NW5 1LP United Kingdom +44 (0)20 7700 2487 

**<u>www.shadowrobot.com hand@shadowrobot.com</u>** 

**Shadow Dexterous Hand - Technical Specifications** 

**10** 

