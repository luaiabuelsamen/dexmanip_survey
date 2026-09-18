# **ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning** 

Clemens C. Christoph<sup>1†</sup> , Maximilian Eberlein<sup>1†</sup> , Filippos Katsimalis<sup>1†</sup> , Arturo Roberti<sup>1†</sup> , Aristotelis Sympetheros<sup>1†</sup> , Michel R. Vogt<sup>1†</sup> , Davide Liconti<sup>1</sup> , Chenyu Yang<sup>1</sup> , Barnabas Gavin Cangan<sup>1</sup> , Ronan J. Hinchet<sup>1</sup> , Robert K. Katzschmann<sup>1</sup><sup>_∗_</sup> 

**_Abstract_ — General-purpose robots should possess humanlike dexterity and agility to perform tasks with the same versatility as us. A human-like form factor further enables the use of vast datasets of human-hand interactions. However, the primary bottleneck in dexterous manipulation lies not only in software but arguably even more in hardware. Robotic hands that approach human capabilities are often prohibitively expensive, bulky, or require enterprise-level maintenance, limiting their accessibility for broader research and practical applications. What if the research community could get started with reliable dexterous hands within a day? We present the open-source ORCA hand, a reliable and anthropomorphic 17DoF tendon-driven robotic hand with integrated tactile sensors, fully assembled in less than eight hours and built for a material cost below 2,000 CHF. We showcase ORCA’s key design features such as popping joints, auto-calibration, and tensioning systems that significantly reduce complexity while increasing reliability, accuracy, and robustness. We benchmark the ORCA hand across a variety of tasks, ranging from teleoperation and imitation learning to zero-shot sim-to-real reinforcement learning. Furthermore, we demonstrate its durability, withstanding more than 10,000 continuous operation cycles—equivalent to approximately 20 hours—without hardware failure, the only constraint being the duration of the experiment itself. Video is here: youtu.be/kUbPSYMmOds. Design files, source code, and documentation are available at srl.ethz.ch/orcahand.** 

## I. INTRODUCTION 

Reproducing the intricate dexterity of the human hand has long been a central challenge in robotics [1], [2]. Although robotic grippers excel in industrial automation, their limited versatility makes them unsuitable for interaction with tools and objects designed for human hands [3], [4]. Consequently, extensive research has been devoted to developing anthropomorphic robotic hands and training them to solve complex manipulation tasks [5], [6]. However, compared to grippers, anthropomorphic hands require significantly more actuators, increasing the complexity of their assembly and control. In addition, good anthropomorphic hand hardware must be durable, repeatable, and versatile to be used in machine learning applications. Whether it is the sim2real gap in reinforcement learning (RL) or the accuracy of teleoperation in imitation learning (IL), bottlenecks in dexterous manipulation stem not only from software, but also, and maybe more importantly, from hardware limitations [7]–[9]. 

Tendon-driven robotic hands have been a focal point of robotics research since its early days [11]–[13]. Among 

> 1Soft Robotics Lab, IRIS, D-MAVT, ETH Zurich, Switzerland 

> † Equal contribution. 

> _∗_ Corresponding author: rkk@ethz.ch 



Fig. 1: (A) The ORCA hand closely mimics its human counterpart with the same form factor, a bony structure, and silicone-cast skin. The ORCA hand is 3D-printed but incorporates joints designed to pop before breaking, making it resistant to overload-induced failures while retaining the advantages of bearing pinhole joints, such as stability and simple kinematics. (A1) Just before the joint pops. (A2) Applying pressure pops the joint into place and keeps it secure. (A3) Depicts our spool system, which enables manual retention without unscrewing the spools or tendons. (B) We show that our hand can be deployed in real-world settings by running our self-resetting imitation learning policy for over 7 hours before we decided to end the experiment. (C) Our reliability test reveals our hand’s robustness and the high repeatability of joint movements. 

the various designs, the proprietary Shadow Hand [14] demonstrated impressive capabilities in dexterous manipulation tasks [15]. However, these hands cost over 100,000 CHF, require substantial maintenance [16] and are difficult to repair due to their proprietary and highly integrated designs. Other recent tendon-driven hand designs, such as the InMoov hand [17] and the DexHand [18], offer the advantages of being open source and low-cost. However, the 



<!-- Start of picture text -->
A C D E<br>F<br>B<br>Imitation Learning Zero-Shot Sim-To-Real RL<br><!-- End of picture text -->

Fig. 2: Versatility of the ORCA hand: (A)-(D) Teleoperation with ROKOKO [10] gloves. (A) Holding a pen (B) Using a drill, showing high dexterity. (C) Liquid pouring. (D) Grasping a cube: This picture illustrates how closely the ORCA hand resembles a human hand. (E) IL with walls and a slider for self-resetting. (F) Policies in simulation, such as rolling a ball, can be deployed zero-shot to the real world due to the ORCA hand’s low joint errors. 

InMoov hand is limited in dexterity, while the DexHand is challenging to assemble, and neither has demonstrated realworld applicability in autonomous manipulation tasks. 

Alternatives to tendon-driven hands are direct-driven hands, such as the Allegro Hand [19], priced at around 15,000 CHF, and the open-source LEAP hand [20], which is even more cost-effective under 2,000 CHF and requires only three hours of assembly for unprecedented levels of reliability. However, all direct-driven hand designs share limitations such as bulkiness, restricted form factors, and an inability to match the softness, form factor, and agility of a human hand. Embedding motors within the fingers increases inertia and limits power output, restricting the quick, dynamic, and forceful movements essential for human-like motion. 

In this paper, we present the ORCA hand: a tendondriven, dexterous, and anthropomorphic robotic hand with fully integrated tactile sensors. The ORCA hand is designed for reliability, simplicity, and versatility in a wide range of tasks. Key contributions of our integrated system include: 

- An open source, 3D-printable design with a cost of less than 2,000 CHF, which can be assembled by a single person without prior experience in less than eight hours. 

- A joint design that pops before it breaks, enhancing the durability of 3D-printed components and streamlining the assembly process. 

- Auto-calibration enabled by tendon routing through the center of rotation. This minimizes joint position errors and increases repeatability. 

- Fully integrated tactile sensors and sensor wiring, which can be produced in-house, offering a compact and modular solution. 

We demonstrate the hand’s dexterity by teleoperating it to perform complex tasks that traditional robotic grippers cannot accomplish. Through a variety of reliability tests we demonstrate the ORCA hand’s capability to offer exceptional reliability, durability, and consistent performance during tens of hours of operation. To showcase the ORCA hand’s dexterity and accuracy we implement fine motor control tasks like in-hand object orientation. Leveraging the anthropomorphic design, we are also able to implement imitation learning tasks like the picking and placement of cubes and execute these 

autonomous tasks continuously for multiple hours without any human intervention on the hand hardware. 

## II. SYSTEM DESIGN 

The ORCA hand design follows the requirements set above, namely dexterity and reliability at minimal complexity and cost. It comprises five fingers, including an opposable thumb and an actuated wrist (Figure 1-A), and is of a size similar to the average human hand [21]. The total weight of the hand is approximately 1.2 kg. The fingers are mounted on a base that resembles the human palm containing the carpal and metacarpal bones. The palm is connected to the wrist mechanism that is mounted on the _tower_ . The tower contains the motors and all auxiliary electronics, and is enclosed in a protective casing. The rest of this section describes the most important design features of the ORCA hand in detail. 

## _A. Tendon Actuation for Agility_ 

Each joint, except for the wrist joint, is actuated using two fishing lines (Nylon fibers braided into a 0.4 mm diameter rope) under tension, here referred to as tendons. One tendon is responsible for flexion (flexor) and the other for extension (extensor). This decision was made based on the observation that a smaller form factor and lower finger inertia more closely mimic the nimbleness and dexterity of human hands compared to direct-driven hands. In addition, tendon actuation makes the ORCA hand independent of the choice of actuator, enabling actuation technologies other than electric motors to be used in the future, such as contracting artificial muscles. 

Although tendon actuation offers many advantages, it also presents challenges such as friction build-up, wear, and slack over time, which can affect movement precision and longevity. We mitigate those challenges as follows: 

- We avoid direct contact of the tendons with polylactic acid (PLA) by deflecting the tendons around smooth metal pins and rods, as depicted in Figure 3-C. 

- We use Teflon tubes for nonlinear routing, _e.g._ , from the bottom of the thumb to the wrist. 

- Finally, tendons can be manually re-tensioned using a ratchet spool mechanism mounted on the motors, 



<!-- Start of picture text -->
A B<br>DIP(fixed)<br>PIP<br>IP<br>MCP<br>ABD calibrated<br>ABD<br>CMC<br>C Extensor<br>Center of<br>Rotation<br>Flexor<br>Metal Pins<br><!-- End of picture text -->

Fig. 3: (A) Naming convention of the joints. The thumb includes an additional degree of freedom. (B) Auto-calibration: The three-step process moves all joints to their respective limits and determines a mapping between motor and joint angles without any external sensors. (C) Routing of the DIP joint. The tendons are guided around metal pins, to reduce friction and eliminate wear over time. Moreover, they are always guided through the center of rotation for straightforward control at minimal slack. 

as shown in Figure 1-A3. The ratchet is attached to the top spool, allowing rotation in one direction while locking movement in the other. This design makes the ORCA hand user-friendly, as re-tensioning can be done in seconds without the need to unscrew the spool or tendon. The spool system quickly removes any slack that accumulates. In addition, tendons can be easily loosened, allowing joints to pop out for quick replacement of broken parts. 

## _B. Poppable Pin Joints_ 

Rolling contact joints [18], [22] have become a popular alternative to pinhole joints for 3D-printed hands due to their ability to dislocate instead of break. However, these mechanisms require ligaments that can potentially loosen over time and increase complexity. We introduce a pin joint design that allows the joints to "pop" out of place and dislocate instead of breaking when excessive radial and axial loads are applied (Figure 1-A1). 

This feature is achieved by placing the bearings in circular arc-shaped grooves, which hold them tightly under normal operating conditions, but allow them to dislocate in the event of a forceful collision. This mechanism combines the advantages of pinhole joints, such as axial stability and straightforward kinematics, with the robustness of ligamentbased rolling contact joints, while being extremely quick and easy to assemble. 

## _C. Finger and Palm Design_ 

Fingers two to five (index to pinky) have three actuated joints that mimic those of the human finger: the Proximal Interphalangeal (PIP), the Metacarpophalangeal (MCP), and the Abduction (ABD) joint (Figure 3-A). The ORCA PIP joint corresponds to the human PIP joint, while the MCP and ABD joints together correspond to the human MCP joint which can perform both flexion/extension and abduction/adduction, which is necessary in various dexterous manipulation tas ~~ks [23]. The ran~~ ge of motion (RoM) for each joint is shown in Table I, based on human anatomy [21]. 

|**Joint Name**|**Fingers **|**2 to 5**|**T**|**humb**|
|---|---|---|---|---|
||**Flexion**|**Extension**|**Flexion**|**Extension**|
|**IP**|-|-|100°|20°|
|**PIP**|130°|20°|-|-|
|**MCP**|110°|20°|115°|20°|
|**ABD**|30°|30°|45°|45°|
|**CMC**|-|-|48°|53°|



TABLE I: Motion range of the joints of the ORCA hand. 

The removal of the DIP joints on digits 2 to 5 was an intentional design decision. In most cases, DIP joints are rigidly coupled with the corresponding PIP joints and do not move independently, meaning they do not contribute additional active degrees of freedom. By fixing the DIP joints, we eliminate the potential for slack buildup over time and enable direct motor control of the distal joint, resulting in improved accuracy and predictability. Furthermore, this approach simplifies assembly significantly and frees up space for additional sensing electronics. The DIP joint is not directly actuated in the human hand, and as such it is of less importance compared to the other hand joints in dexterous manipulation tasks. A positive side-effect of the removal of the DIP joint is the substantial increase in the space available for tactile sensing integration on the fingertips. 

The thumb differs from other fingers and has four instead of three DoFs, _i.e._ , the Interphalangeal (IP), MCP, ABD, and Carpometacarpal (CMC) joints. Additionally, the thumb is positioned with a supination of 15<sup>_◦_</sup> on the palm, making it opposable to the other fingers [21]. 

## _D. Wrist Design_ 

A major limitation of hands without a wrist joint is their inability to orient the palm parallel to surfaces like a table, as the robotic arm obstructs movement. This lack of a wrist joint significantly impairs grasping performance. Motivated by this, we added one rotational DoF around the transverse (radioulnar) axis of the hand. The human wrist can flex and extend about 80<sup>_◦_</sup> [21], while the ORCA wrist mechanism is capable of achieving 60<sup>_◦_</sup> in flexion and extension. Instead of using tendon actuation for the wrist, we opted for a belt drive to account for the increased loads the wrist experiences. We use a standard GT2 timing belt with fiberglass reinforcement, which exhibits negligible slack buildup over time. We decided not to add a second DoF at the wrist to represent the radial/ulnar deviation of the 

human wrist, particularly to avoid unnecessary complexity and increased cost, since the human wrist is significantly limited in this type of motion compared to flexion/extension [21]. 

## _E. Integrated tactile sensing_ 

Many previous works have enhanced the manipulation abilities of robotic hands by integrating tactile sensors, particularly on the fingertips. These sensors include force sensors [24], [25], piezoresistive pressure sensors [26], capacitive pressure sensors [27], and Hall effect sensors [28]. 

For the ORCA hand, we utilize force sensing resistors (FSR) (RP-C7.6-ST Thin-Film Pressure Sensor) mounted onto a solid FDM-printed PLA backplate, and covered by silicone-molded skin, to provide the hand with binary tactile feedback on all five fingertips. While FSR sensors can theoretically measure the magnitude of applied force, a binary interpretation was chosen due to the compliant skin and its irregular surface, which dampens external forces to varying degrees depending on the contact point on the fingertip. As such, the force magnitude cannot be estimated without additional information about the location of indentation, which the FSR sensors themselves are unable to provide. 

All sensors are connected to external electronics through thin copper wires (∅ 0.2mm), which are routed through the internal finger and palm structure through PTFE tubing, to protect them from the environment and external forces, while also providing a clean visual appearance. To read the output of the FSR sensors, each sensor forms a voltage divider with a 10 _k_ Ω resistor, the three nodes of which are connected to a 5V input, an analog input, and ground, respectively, all provided by a small microcontroller (Arduino Nano Every). 

## _F. Self-Calibration for Accurate Control_ 

Consistency across runs is essential in imitation learning, as variability between teleoperation and execution degrades policy performance [29], especially in sim-to-real settings. While proprioceptive sensors offer reliable control [14], they add cost and complexity. We propose a simpler, cost-effective alternative: automated self-calibration to estimate motor-tojoint mappings (Algorithm 1). 

Let _θj_ be the true angle and _mj_ the position of the motor for joint _j_ . The ideal goal is to perfectly control _θj_ by commanding _mj_ . However, in practice, especially with tendondriven hands without joint sensors, there is a discrepancy. A simple model would be _θj_ = _f_ ( _m_ 1 _, . . . , m_ 17) + _ϵ_ , where _f_ is a nonlinear function and _ϵ_ represents model errors arising from factors like tendon and pulley radii ( _rt, rp_ ), tendon slack _s_ , servo drift _d_ , and manual measurement errors _merr_ . These factors can introduce substantial offsets. 

Referring to the routing of the ORCA hand, as depicted in Figure 3, each tendon passes through or near the center of rotation (CoR). This design ensures that joint positions are approximately decoupled and can be actuated linearly and independently. This linearity allows us to simplify the model significantly. The self-calibration procedure detailed in 

**Algorithm 1** Self-Calibration Algorithm 

- 1: **Input:** Set of joints _J_ = _{_ 1 _, . . . , N }_ , joint ROMs [ _θj_<sup>min</sup> _, θj_<sup>max</sup> ] for each joint _j_ 

- 2: **Output:** Motor limits [ _m_<sup>min</sup> _j , m_<sup>max</sup> _j_ ], motor-to-joint ratios _ρj_ for each joint _j_ 

- 3: **for** each joint _j ∈J_ **do** 

- 4: Move joint _j_ towards its flexion limit until stall is detected 

- 5: _m_<sup>min</sup> _j ←_ current motor position 6: 

- 7: Move joint _j_ towards its extension limit until stall is detected 

- 8: _m_<sup>max</sup> _j ←_ current motor position 9: 

- 10: Compute motor travel: ∆ _mj_ = _m_<sup>max</sup> _j − m_<sup>min</sup> _j_ 11: Compute joint ROM: ∆ _θj_ = _θj_<sup>max</sup> _− θj_<sup>min</sup> 12: Compute motor-to-joint ratio: _ρj_ =<sup>∆</sup> ∆<sup>_m_</sup> _θj_<sup>_<u>j</u>_</sup> 13: **end for** 

Algorithm 1 leverages this by empirically finding the linear relationship for each joint. The process works as follows: 

- 1) **Determine Joint ROM (Line 11):** The absolute range of motion (ROM) for each joint, ∆ _θj_ , is precisely determined from the robot’s CAD models. This provides an accurate ground truth for the joint’s angular travel between its physical stops, [ _θj_<sup>min</sup> _, θj_<sup>max</sup> ]. 

- 2) **Find Motor Limits (Lines 4-8):** During calibration, each joint _j_ is programmatically moved to its extreme mechanical limits (e.g., fully flexed and fully extended). The corresponding motor positions, _m_<sup>min</sup> _j_ and _m_<sup>max</sup> _j_ , are recorded when the joint stalls. 

- 3) **Calculate Transmission Ratio (Lines 10-12):** The total motor travel, ∆ _mj_ , is computed from the recorded limits. The motor-to-joint transmission ratio _ρj_ is then calculated via linear interpolation as the ratio of the motor travel to the joint’s known ROM: 



This autocalibration largely eliminates the complex error terms related to physical modeling and manual measurements, _ϵ_ ( _rt, rp, s, d, merr_ ), leaving a much smaller residual error, _ϵ_ (∆ _θj, s, d_ ). With the calibrated parameters, the motor position _mj_ required to achieve a desired joint angle _θj_ is computed using a linear mapping: 



This method ensures a consistent and accurate mapping from desired joint angles to motor commands across different operational sessions. 

III. HARDWARE PERFORMANCE TESTS 

## _A. Reliability and Robustness_ 

To evaluate the reliability and robustness of the ORCA hand in long-duration tasks, we conducted an experiment 



<!-- Start of picture text -->
Commanded Angle Ground Truth Angle (ORCA) Ground Truth Angle (LEAP) B LEAP  ORCA<br>A 0.2 Hz Sine 0.5 Hz Sine Hand Hand<br>60 !!"! !#$!<br>40<br>20<br>0<br>60<br>ROS<br>Camera<br>40 @60 fps<br>20<br>0<br>0 2 4 6 8 100 2 4 6 8 10<br>Time (s) Time (s)<br>C Wrist Motor Middle-MCP Motor Middle-PIP Motor Motor Average<br>220 39<br>38<br>200<br>0 50 100 150 0 50 100 150<br>Time (min) Time (min)<br>(deg) µMCP<br>(deg) µPIP<br>(mA)Curr. (C)°Temp.<br><!-- End of picture text -->

Fig. 4: (A) Joint response comparison at 0.2 Hz and 0.5 Hz: ORCA achieves accuracy and latency comparable to the LEAP hand despite its tendon-driven design. (B) Accuracy benchmarking setup using AprilTags to infer groundtruth joint angles synchronized with commands. (C) Reliability test: 2.5 hours of continuous grasping (2200+ cycles) and wrist motion (550+ cycles) without failure, overheating, or performance drop, as shown by stable motor current and temperature. 

in which we actuate the hand joints continuously for 2.5 hours (Figure 1-C). We attach a plush animal to the palm of the hand and have it grasp it with all fingers every four seconds. This setup, using a compliant object, is similar to the repeatability test performed by [20] and allows us to assess behavior under increased stress over a greater range of motion. Moreover, to test the durability of the wrist joint, we flex and extend the wrist to 40<sup>_◦_</sup> at one fourth of the frequency of the finger, that is, every 16 seconds. 

The hand successfully completed 2,250 grasping cycles without breakage, motor shutdown, or excessive tendon slack. Figure 4-C shows the maximum current per cycle for the middle finger’s MCP and PIP motors, and the wrist joint motor during wrist extension-flexion. Motor current reflects the torque and friction the system must overcome. The stable maximum current over 2.5 hours of continuous operation demonstrates the hand’s robustness, high repeatability, and long-duration capability. Side-mounted fans (Figure 4-C) prevent motor overheating, enabling near-continuous use. The experiment was ended voluntarily after 2.5 hours, not due to failure. 

To evaluate payload capacity, we used a hand force sensor (electronic grip strength tester) with constant 600 mA motor current in position control mode. The hand was tested in various grasps, showing it can hold up to 10 _._ 5 kg (103 N) using all four fingers, and up to 2 kg (19 _._ 6 N) using only the index finger. 

## _B. Accuracy and Latency_ 

Accurate control of joint motion is crucial for reliable performance across any dexterous manipulation task. Additionally, excessive latency between action commands and their execution in the real world can severely hinder the implementation of closed-loop behaviors. Incorporating latency into the hand’s model for training in simulation can be 

helpful to bridge the sim2real gap. To further demonstrate the reliability of the ORCA hand, we, therefore, benchmark the accuracy and latency with which the hand’s joints can follow diverse action commands. We propose the following experimental setup to benchmark the accuracy and latency of robotic hands: 

By attaching distinct AprilTags along one finger and measuring their relative orientations to each other, each joint angle on the finger can be calculated with relatively low error ( _σ_ = 0 _._ 08<sup>_◦_</sup> for our experimental setup). We place three tag36h11 AprilTags across the MCP and PIP joints of the ORCA hand’s index finger and align them in a single plane (Fig. 4B). We then position a RealSense D435i camera in front of the AprilTags, using a custom script to ensure that the camera faces the tags at an angle of 90<sup>_◦_</sup> _±_ 5<sup>_◦_</sup> for more precise angle measurements. We record image frames at 60 fps and save them to a ROS2 bag file. Simultaneously, we publish commanded angles that actuate the index finger’s MCP and PIP joints in a sine wave pattern and log them into the same ROS2 bag file. This allows us to synchronize the commanded angles with the real angles obtained from the image frames and evaluate the system’s latency and accuracy offline. 

We compare the accuracy and latency of the ORCA hand with the LEAP [20] hand to benchmark our system’s tendondriven dynamics against the dynamics of a direct-driven robot hand (Figure 4-A). We actuate the MCP and PIP joints of both hands’ index fingers with 0.2 Hz and 0.5 Hz sine wave patterns. Before each test, we leverage the auto-calibration mechanism of the ORCA hand to account for any changes in tendon length or slack that might have accumulated beforehand. We demonstrate that, through autocalibration, the finger joints of the ORCA hand accurately follow the commanded sine input. In fact, we achieve similar accuracy to the LEAP hand while being far less bulky thanks to our tendon-driven actuation design. Additionally, we observe that the ORCA hand’s joints rotate more smoothly than those of the LEAP hand, which exhibit more jerks, presumably due to the cables and possibly increased inertia interfering with the LEAP hand’s finger joint motion. Both hands exhibit average latencies of less than 0.2 seconds, most of which comes from the software process. However, slack in the ORCA hand may introduce additional latency, which is why re-tensioning the spools periodically is important for robust performance. 

One limitation of our benchmarking experiment is that we cannot evaluate the accuracy and latency of the hands for faster movements, as the AprilTags can not be tracked at sine wave frequencies above 0.5 Hz or for step signals due to motion blur at 60 fps. Recording the finger joints with a ROS2-compatible camera capable of 240 fps could enable more thorough system identification in the future. 

## _C. Reinforcement Learning_ 

Reinforcement learning (RL) is commonly used to learn dexterous tasks that are challenging to demonstrate or require fine motor control, such as object reorientation in the hand 

[30]. A key challenge in applying RL to dexterous manipulation tasks is that the policies learned in simulation often perform poorly when transferred to the real robotic hand. We use the IsaacGymEnvs wrapper from [22] to train 4096 ORCA hand models in parallel with an advantage actor-critic (A2C) architecture to learn in-hand ball reorientation. We do not use tactile sensors in our RL experiments, primarily due to the additional complexity involved in accurately modeling them. We demonstrate that after one hour of training with domain randomization, we can deploy a robust policy on the physical ORCA hand (Figure 6-B), that can successfully reorient a tennis ball along a given rotation axis. 

## _D. Imitation Learning_ 

Imitation learning has become another predominant approach in the manipulation community, as it enables learning tasks from a set of demonstrations without requiring taskspecific rewards or simulation environments. Various architectures have been proposed to extract meaningful representations of observations and map them to the correct actions [31]–[33]. However, the application of imitation learning to dexterous platforms presents additional challenges mainly due to their higher-dimensional action spaces [34], [35]. 

To demonstrate autonomous task execution with the Orca Hand, we employed a state-of-the-art robotic diffusion transformer [31]. Our setup consists of the hand mounted on a robotic arm (Franka Emika Panda), equipped with two external cameras and one wrist-mounted camera. 

Demonstrations were collected using motion capture gloves [10], which provided absolute wrist tracking and finger pose estimation. We retargeted these demonstrations into the robot’s state space using an energy-based minimization objective, similar to [36]. The wrist pose was used to control the robotic arm in cartesian end-effector space. This teleoperation method allowed us to showcase the versatility of the hand in a wide range of tasks (Figure 2) and facilitated the rapid and intuitive collection of demonstrations, even from non-trained operators. 

The policy takes as input three camera images along with proprioceptive data from both the robotic arm’s end-effector and the hand. The output consists of an action chunk that predicts future actions. 

Over approximately 2h30m, 214 recordings (videos, proprioceptive data, actions) were collected to train the policy on an _NVIDIA GeForce RTX 4090_ GPU for 500 epochs, which took approximately 4h. 

For the proposed task, we performed ablation studies on image pre-processing. Specifically, we compared three policy variations: (1) a baseline policy trained on raw RGB inputs, (2) a policy incorporating segmentation of the cube’s color, and (3) a hybrid approach trained on both data sets (Figure 7). 

For (2) and (3), a binary mask was generated using the CIELAB [37] color space, with parameters tuned to isolate the red cube. From the RGB image, a three-channel grayscale image is created, and non-zero pixels of the binary mask are 



<!-- Start of picture text -->
Franka Panda External<br>Cameras<br>ORCA<br>Hand<br>Sliding Surface<br>Wrist<br>Camera<br>Random Cube Position<br><!-- End of picture text -->

Fig. 5: Experimental setup for repeated pick & place: The cardboard serves as a fence, preventing the cube from rolling out of the testing area and enabling uninterrupted, long-duration policy deployment. 

set to 255 in the first channel (arbitrarily chosen), effectively highlighting the cube. 

## _E. Tactile Sensing_ 

We also evaluated the fingertip sensors. To determine the absolute threshold (AT) of the tactile sensors, a controlled orthogonal force was applied to the front surface of a fingertip using a cylindrical indenter with a diameter of 2 _cm_ and a flat contact surface. The applied force was varied by placing calibrated weights on top of the indenter. The registered touch was classified as any output reading above 0 _._ 01 _V_ on the respective analog input on the Arduino. 

Although the FSR sensors used are rated for a minimum trigger force of 0 _._ 29 _N_ , the fingertip was able to register forces as low as 0 _._ 05 _N_ with perfect accuracy over 10 cycles. It is unknown if this is due to a lower than rated minimum trigger force of the commercial FSR sensors, or if the silicone skin had an unintentional preloading effect on the sensor. 

However, wear and tear on the silicone skin can drastically affect the AT of the sensors. Although the sensor mounted on the ring finger of the hand showed no degradation after thousands of grasp cycles as part of the experiments described in Section III-A, the AT for the sensor mounted on the pinkie finger increased to 6 _._ 38 _N_ due to the degradation of the silicone skin creating an air gap between the silicone skin and the mounted FSR sensor. 

Furthermore, after around 4,500 to 7,000 grasp cycles, the thin copper wires connecting the sensors to the external electronics snapped on the thumb, index, and middle finger. The snapping points occurred at different heights but were all concentrated in the area of the MCP and ABD joints. 

IV. ADDITIONAL RESULTS AND DISCUSSION 

In this section, we show the results of human teleoperation and imitation learning with the ORCA hand. We also discuss additional hardware-related findings. 

## _A. Teleoperation - Dexterous Manipulation_ 

The dexterity and stability of the ORCA hand were successfully evaluated by picking up, interacting with, and placing a variety of objects: 



<!-- Start of picture text -->
A<br>~2k graps<br>…<br>7 hours later<br>still running<br>B<br>…<br><!-- End of picture text -->

Fig. 6: (A) Prolonged imitation learning experiments over several hours. Walls and a sliding surface allow for self-resetting of the experiment. (B) Policies built in simulation are easily deployed zero-shot to the real world since the ORCA hand has autocalibration and only minimal joint control errors. 

|||**RGB**|**Masked **|**Mixed**|
|---|---|---|---|---|
|1<br>2|**Area **|**1**<br>50%|80%|80%|
||**Area **|**2**<br>10%|60%|20%|
|4<br>3|**Area **|**3**<br>80%|100%|100%|
||**Area **|**4**<br>60%|100%|80%|
||**Area **|**5**<br>60%|100%|80%|
|6<br>5|**Area **|**6**<br>40%|80%|60%|
|Slide|**Total**|50%|86_._<br>_<br>6%|70%|



Fig. 7: Testing area with respective policy success rates (% out of 10) 

- Stack 3 small and large cubes (the same as for IL experiment). The cubes were first placed separately on the table. 

- Grab a plush toy (about the size of 3 large cubes) from the table top. 

- Grab a tennis ball lying on the table 

- Twist open the cap of a _Nutella_ jar (�8 _cm_ ). The jar itself is fully screwed on. 

- Spin a fidget toy for 2 _s_ . The fidget spinner is placed on a finger by hand, but the grasping and spinning are done purely by teleoperation. 

- Pick up a pen and write "Hello" on a fastened piece of paper (font size _∼_ 200). 

- Pick up a piece of paper lying on a shut box. 

- Pick up a cup and pour its contents (50 _ml_ water) into another cup. 

## _B. Imitation Learning - Repeated Pick & Place_ 

To highlight the reliability of both the hardware platform and the trained IL policy, we designed a continuous pick-andplace evaluation task. The robotic hand is required to pick up a cube (6 cm in side length) from a table and place it on a sliding surface, which then causes the cube to fall back onto a random location on the table (Figure 5, Figure 6-A). 

To evaluate different policies, we collected the ratio of failure positions to success positions (regarding picking up the cube) within a testing area for 60 iterations (10 per subarea), as shown in Figure 7. The most successful policy, using only masked images of the cube, is deployed for 7h 17min (approx. 2,000 grasping cycles) with no human intervention on the ORCA hand’s hardware and minimal 

intervention in aiding in the pick-and-place task (Figure 1-B). Throughout the test, the policy maintained consistent performance, with no tendon slack or rupture, and the experiment was concluded not due to failure but because it sufficiently demonstrated the system’s reliability and effectiveness. For extended videos and time-lapses of the reliability test, please refer to the ORCA project website. 

## _C. Tactile Sensing_ 

While integrated tactile sensing provides a cost-effective and low barrier-of-entry approach to providing tactile feedback at the fingertips, the current design still shows a variety of limitations regarding reliability over thousands of grasp cycles. These limitations are namely the degradation of the silicone skin that is vital to reliably transmit the contact forces to the sensors (occurrence in 2 fingertips after approx. 2,000 to 4,000 grasp cycles) as well as the snapping of the thin copper wires used for signal transmission (occurrence in 3 fingertips after approx. 4,500 to 7,000 grasp cycles). Both limitations will be addressed in future work to allow for reliable tactile sensing integration into autonomous tasks. 

## V. CONCLUSION 

The ORCA hand provides an accessible platform for advancing robotic manipulation, aiming to support real-world tasks and cutting-edge research. It is designed to be humanlike, compliant, robust, versatile, easy to control, and costeffective. 

Despite these strengths, limitations remain. Prolonged use requires manual re-tensioning to maintain performance. To overcome this, we plan to develop an autonomous retensioning mechanism to reduce tendon slack without human intervention, enabling longer operation and supporting realworld RL applications. Future work also includes integrating sensors directly into the learning pipeline and applying more advanced deep learning methods to handle complex environmental interactions. 

## ACKNOWLEDGMENT 

We thank Robert Jomar Malate and the Real World Robotics course team at ETH Zurich for initiating and enabling this project, and Carlo Sferrazza and the Berkeley Robot Learning Lab for access to their LEAP Hand. This 

work was funded through a research collaboration with armasuisse. Filippos Katsimalis acknowledges support from the Bodossaki Foundation, SYN-ENOSIS, and the Onassis Foundation. Aristotelis Sympetheros acknowledges support from the John S. Latsis Public Benefit Foundation and SYNENOSIS. 

## REFERENCES 

- [1] A. Bicchi and V. Kumar, “Robotic grasping and contact: a review,” in _Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No.00CH37065)_ , vol. 1, 2000, pp. 348–353 vol.1. 

- [2] A. Okamura, N. Smaby, and M. Cutkosky, “An overview of dexterous manipulation,” in _Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No.00CH37065)_ , vol. 1, 2000, pp. 255–262 vol.1. 

- [3] C. Yu and P. Wang, “Dexterous manipulation for multifingered robotic hands with reinforcement learning: A review,” _Frontiers in Neurorobotics_ , vol. 16, 2022. [Online]. Available: https://www.frontiersin.org/journals/neurorobotics/articles/ 10.3389/fnbot.2022.861825 

- [4] P. Seguin, C. Preault, P. Bidaud, and J.-P. Gazeau, “From specialized industrial grippers to flexible grippers: Issues for grasping and dexterous manipulation,” _Foundations and Trends® in Robotics_ , vol. 11, no. 1, pp. 1–89, 2023. [Online]. Available: http://dx.doi.org/10.1561/2300000074 

- [5] S. Kadalagere Sampath, N. Wang, H. Wu, and C. Yang, “Review on human-like robot manipulation using dexterous hands,” _Cognitive Computation and Systems_ , vol. 5, no. 1, pp. 14–29, 2023. [Online]. Available: https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/ ccs2.12073 

- [6] Y. Huang, D. Fan, H. Duan, D. Yan, W. Qi, J. Sun, Q. Liu, and P. Wang, “Human-like dexterous manipulation for anthropomorphic five-fingered hands: A review,” _Biomimetic Intelligence and Robotics_ , p. 100212, 2025. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S2667379725000038 

- [7] T. Feix, J. Romero, C. H. Ek, H.-B. Schmiedmayer, and D. Kragic, “A metric for comparing the anthropomorphic motion capability of artificial hands,” _IEEE Transactions on Robotics_ , vol. 29, no. 1, pp. 82–93, 2013. 

- [8] A. Billard and D. Kragic, “Trends and challenges in robot manipulation,” _Science_ , vol. 364, no. 6446, p. eaat8414, 2019. [Online]. Available: https://www.science.org/doi/abs/10.1126/science. aat8414 

- [9] J. Zhu, A. Cherubini, C. Dune, D. Navarro-Alarcon, F. Alambeigi, D. Berenson, F. Ficuciello, K. Harada, J. Kober, X. Li, _et al._ , “Challenges and outlook in robotic manipulation of deformable objects,” _IEEE Robotics & Automation Magazine_ , vol. 29, no. 3, pp. 67–77, 2022. 

- [10] Rokoko, “Rokoko official website,” 2025, accessed: 2025-01-16. [Online]. Available: https://www.rokoko.com 

- [11] G. A. Bekey, R. Tomovic, and I. Zeljkovic, “Control architecture for the belgrade/usc hand,” _Dextrous robot hands_ , pp. 136–149, 1990. 

- [12] J. K. Salisbury and J. J. Craig, “Articulated hands: Force control and kinematic issues,” _The International journal of Robotics research_ , vol. 1, no. 1, pp. 4–17, 1982. 

- [13] S. Jacobsen, E. Iversen, D. Knutti, R. Johnson, and K. Biggers, “Design of the utah/mit dextrous hand,” in _Proceedings. 1986 IEEE International Conference on Robotics and Automation_ , vol. 3. IEEE, 1986, pp. 1520–1532. 

- [14] Shadow Robot Company, “Dexterous hand series,” 2024, accessed: 2024-12-26. [Online]. Available: https://www.shadowrobot.com/ dexterous-hand-series/ 

- [15] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, _et al._ , “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [16] OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, J. Schneider, N. Tezak, J. Tworek, P. Welinder, L. Weng, Q. Yuan, W. Zaremba, and L. Zhang, “Solving rubik’s cube with a robot hand,” 2019. [Online]. Available: https://arxiv.org/abs/1910.07113 

- [17] Inmoov, “Inmoov Hand,” 2024, accessed: 2024-12-26. [Online]. Available: https://inmoov.fr/ 

- [18] DexHand Project, “DexHand,” 2024, accessed: 2024-12-26. [Online]. Available: https://www.dexhand.org 

- [19] SimLab Co., Ltd., “Allegro Hand,” 2024, accessed: 2024-12-26. [Online]. Available: https://www.allegrohand.com 

- [20] K. Shaw, A. Agarwal, and D. Pathak, “Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning,” 2023. [Online]. Available: https://arxiv.org/abs/2309.06440 

- [21] B. Hirt, H. Seyhan, M. Wagner, and R. Zumhasch, _Hand and Wrist Anatomy and Biomechanics_ , 2017th ed. Thieme Verlag, 2017, publication Title: Hand and Wrist Anatomy and Biomechanics. [Online]. Available: https://www.thieme-connect.de/products/ebooks/ lookinside/10.1055/b-0036-140288 

- [22] Y. Toshimitsu, B. Forrai, B. G. Cangan, U. Steger, M. Knecht, S. Weirich, and R. K. Katzschmann, “Getting the ball rolling: Learning a dexterous policy for a biomimetic tendon-driven hand with rolling contact joints,” in _2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids)_ , 2023, pp. 1–7. 

- [23] T. C. Pataky, M. L. Latash, and V. M. Zatsiorsky, “Multifinger aband adduction strength and coordination,” _Journal of Hand Therapy_ , vol. 21, no. 4, pp. 377–385, 2008. [Online]. Available: https: //www.sciencedirect.com/science/article/pii/S0894113008000239 

- [24] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang, “Rotating without seeing: Towards in-hand dexterity through touch,” 2023. [Online]. Available: https://arxiv.org/abs/2303.10880 

- [25] P. Weiner, C. Neef, Y. Shibata, Y. Nakamura, and T. Asfour, “An embedded, multi-modal sensor system for scalable robotic and prosthetic hand fingers,” _Sensors_ , vol. 20, no. 1, 2020. [Online]. Available: https://www.mdpi.com/1424-8220/20/1/101 

- [26] J. Egli, B. Forrai, T. Buchner, J. Su, X. Chen, and R. K. Katzschmann, “Sensorized soft skin for dexterous robotic hands,” 2024. [Online]. Available: https://arxiv.org/abs/2404.19448 

- [27] A. Schmitz, M. Maggiali, L. Natale, B. Bonino, and G. Metta, “A tactile sensor for the fingertips of the humanoid robot icub,” in _2010 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , 2010, pp. 2212–2217. 

- [28] M.-J. Seo and J. C. Yoo, “Omnidirectional fingertip pressure sensor using hall effect,” _Sensors_ , vol. 21, p. 7072, 10 2021. 

- [29] S. Belkhale, Y. Cui, and D. Sadigh, “Data quality in imitation learning,” 2023. [Online]. Available: https://arxiv.org/abs/2306.02437 

- [30] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. V. Wyk, A. Zhurkevich, B. Sundaralingam, Y. Narang, J.-F. Lafleche, D. Fox, and G. State, “Dextreme: Transfer of agile in-hand manipulation from simulation to reality,” 2024. [Online]. Available: https://arxiv.org/abs/2210.13702 

- [31] S. Dasari, O. Mees, S. Zhao, M. K. Srirama, and S. Levine, “The ingredients for robotic diffusion transformers,” 2024. [Online]. Available: https://arxiv.org/abs/2410.10088 

- [32] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song, “Diffusion policy: Visuomotor policy learning via action diffusion,” 2024. [Online]. Available: https://arxiv.org/abs/2303.04137 

- [33] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning fine-grained bimanual manipulation with low-cost hardware,” 2023. [Online]. Available: https://arxiv.org/abs/2304.13705 

- [34] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang, “Dexmv: Imitation learning for dexterous manipulation from human videos,” 2022. [Online]. Available: https://arxiv.org/abs/2108.05877 

- [35] D. Liconti, Y. Toshimitsu, and R. Katzschmann, “Leveraging pretrained latent representations for few-shot imitation learning on an anthropomorphic robotic hand,” in _2024 IEEE-RAS 23rd International Conference on Humanoid Robots (Humanoids)_ , 2024, pp. 181–188. 

- [36] A. Sivakumar, K. Shaw, and D. Pathak, “Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube,” 2022. [Online]. Available: https://arxiv.org/abs/2202.10448 

- [37] C. Standard _et al._ , “Colorimetry-part 4: Cie 1976 l* a* b* colour space,” _International Standard_ , pp. 2019–06, 2007. 

