# **Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning** 

**Runyu Ding**<sup>1</sup><sup>_∗_</sup> **, Yuzhe Qin**<sup>2</sup><sup>_∗_</sup> **, Jiyue Zhu**<sup>2</sup><sup>_∗_</sup> **, Chengzhe Jia**<sup>2</sup> **, Shiqi Yang**<sup>2</sup> **, Ruihan Yang**<sup>2</sup> **, Xiaojuan Qi**<sup>1</sup> **, Xiaolong Wang**<sup>2</sup> 1 The University of Hong Kong, 2 University of California, San Diego 

https://dingry.github.io/projects/bunny ~~v~~ isionpro 

**Abstract:** Teleoperation is a crucial tool for collecting human demonstrations, but controlling robots with bimanual dexterous hands remains a challenge. Existing teleoperation systems struggle to handle the complexity of coordinating two hands for intricate manipulations. We introduce Bunny-VisionPro, a real-time bimanual dexterous teleoperation system that leverages a VR headset. Unlike previous vision-based teleoperation systems, we design novel low-cost devices to provide haptic feedback to the operator, enhancing immersion. Our system prioritizes safety by incorporating collision and singularity avoidance while maintaining real-time performance through innovative designs. Bunny-VisionPro outperforms prior systems on a standard task suite, achieving higher success rates and reduced task completion times. Moreover, the high-quality teleoperation demonstrations improve downstream imitation learning performance, leading to better generalizability. Notably, Bunny-VisionPro enables imitation learning with challenging multi-stage, long-horizon dexterous manipulation tasks, which have rarely been addressed in previous work. Our system’s ability to handle bimanual manipulations while prioritizing safety and real-time performance makes it a powerful tool for advancing dexterous manipulation and imitation learning. 

**Keywords:** Bimanual Dexterous Manipulation, Teleoperation, Haptics 



<!-- Start of picture text -->
Grasp toy Wipe glass<br>Finger cots with<br>Apple Vision Pro<br>vibration actuators<br>Clean pan Sweep floor<br>Robot<br>Motion Control<br>Human Uncover and pour Prepare coffee<br>Sense Feedback<br>(a) System overview (b) Teleoperation tasks for imitation learning<br><!-- End of picture text -->

Figure 1: **System Overview and Task Suits. (a)** Hand poses captured by Apple Vision Pro are converted into robot motion control commands for real-time teleoperation. The robot provides sensory feedback, including vision and touch, to operators via Vision Pro and actuator-equipped finger cots. **(b)** We design diverse short-horizon (left-column) and long-horizon tasks (right-column) to evaluate teleoperation performance and its application for imitation learning. 

Runyu Ding was an intern at UCSD during the project 

## **1 Introduction** 

Playing a Virtual Reality (VR) game is an immersive and intuitive experience where your hand and arm movements seamlessly translate into the action of a virtual character. Now, imagine controlling a bimanual robot in the real world with the same ease: operators use their own movements to guide the robot’s motion, just as they would in a VR game. This paradigm shift in robot teleoperation opens up exciting possibilities for more intuitive and accessible human-robot interaction. Recent advancements in VR technology, such as the Apple Vision Pro, have made this concept a possibility. 

Yet, translating this concept into a practical teleoperation system presents significant challenges due to the intricate motion required to perform human-like manipulations. The complexity is further amplified for high Degree-of-Freedom (DoF) hand-arm systems, where the operator must coordinate two arms and hands to execute tasks requiring spatiotemporal synchronization. Achieving responsive control is crucial, as delays can lead to imprecise robot motion [1]. Besides, ensuring safety by mitigating risks such as collision and singularity adds another layer of complexity [2]. 

In this paper, we introduce Bunny-VisionPro, a novel real-time bimanual dexterous teleoperation system. As illustrated in Fig. 1, our system utilizes Vision Pro’s tracking capabilities to capture operator hand movements and translate these movements into precise robotic commands. It addresses both arm and dexterous hand control, prioritizing safety and real-time performance. Crucially, Bunny-VisionPro features three innovative modules: (i) The arm motion control module, which can handle robot singularity and collision avoidance in real time without the need for high-end GPUs This module ensures the safe and smooth operation of robot arms, even in complex bimanual manipulation scenarios. (ii) The dexterous hand retargeting module, which accurately maps human finger movements to the robotic hand. This module features its unique ability to perform retargeting for robots with loop joints, such as four-bar linkages, in real time. (iii) The haptic feedback module, which uses low-cost Eccentric Rotating Mass (ERM) actuators ($1.2 each) to provide tactile sensations. This novel design, paired with a VR headset, offers a more immersive and realistic experience as the robot interacts with its environment, creating a sensation that the operator is the robot itself. 

The advanced capabilities of Bunny-VisionPro enable the collection of high-quality demonstrations for dexterous, bimanual, and long-horizon imitation learning tasks. By leveraging the intuitive and responsive teleoperation system, operators can perform intricate manipulations and collect diverse data for learning algorithms, enabling them to learn and generalize to new scenarios effectively. 

We evaluate our Bunny-VisionPro system on the Telekinesis [3] benchmark, achieving 11% higher success rates and reducing task completion time by 45% compared to prior systems. These enhancements are especially pronounced in multi-stage, long-horizon tasks. Imitation learning policies trained on demonstrations collected by our system show a 20% improvement in generalization on novel poses and unseen objects compared to using data from previous work [4]. These results demonstrate the system’s superior performance in executing complex bimanual manipulation tasks and its effectiveness in collecting high-quality data. 

## **2 Related Work** 

**Teleoperation with Gripper.** Classical teleoperation methods can be categorized into two main approaches based on their control objectives. The first approach, exemplified by ALOHA [5, 6, 7], uses joint-space mapping [8] within leader-follower setups. Although enabling impressive bimanual manipulation, this approach is robot-specific, requiring kinematic equivalence between the leader and follower robots [9]. It also places the burden of managing collision and singularity on the human operator. The second approach prioritizes end-effector control [10], with arm joint positions calculated using inverse kinematics. Various input devices, such as motion capture systems [11, 12], inertia sensors [13], and VR controllers [14, 15, 16, 17] have been utilized. Nevertheless, these systems often employ simple 1 or 2 DoF grippers, which limits their dexterity. In contrast, our work aims to teleoperate high-DoF hand-arm systems for complex manipulation tasks. 

**Dexterous Teleoperation.** Teleoperating dexterous hands is challenging due to their high DoF and complex kinematics. Glove-based systems [18, 19, 20, 21], like the MANUS glove [22] used by 

2 



<!-- Start of picture text -->
Loop Joint<br>Hand Control Retargeting<br>Finger Pose<br>Singularity<br>Arm Control Avoidance<br>Wrist Pose Collision<br>Visual Feedback<br>Avoidance<br> Vision<br>Haptic Feedback Human Haptic<br>Feedback<br>Touch<br>Operator with Vision Pro Bimanual Dexterous Robots Real-Time Capabilities<br><!-- End of picture text -->

Figure 2: **Teleoperation System.** The operator controls the robot hand and arm using finger and wrist poses, respectively. The system’s visual and haptic feedback, combined with its four real-time capabilities, provides an intuitive and immersive VR experience for the operator. 

Tesla Bot, can track the operator’s finger movements but are costly and require specific hand sizes. Recent vision-based approaches, such as AnyTeleop [4], facilitate dexterous hand-arm teleoperation using cameras [3, 23, 24, 25] or VR headsets [26, 27, 28]. However, AnyTeleop requires sophisticated GPU processing for arm motion computation and is primarily designed for a single arm. A concurrent work [29] controls the Ability hand with reduced DoF using grip buttons, sacrificing dexterous finger gaiting to avoid retargeting latency. In contrast, our retargeting modules can handle the Ability hand’s four-bar linkage structure at 300Hz with one CPU core, enabling full dexterity. Our system also integrates collision and singularity avoidance while maintaining real-time performance. 

**Imitation Learning from Demonstration.** Imitation learning enables robots to mimic human behaviors through expert guidance. Pioneering research utilizing deep learning [30, 31, 32, 33] develop policies to generate robot control commands based on image [5, 34, 35, 36, 37, 38] and point cloud data [39, 40, 41, 42], and further marking progress in bimanual systems [18, 5, 6, 43]. Additionally, recent works incorporate tactile data [44, 29] to enrich the sensory data pool for robot learning. Given that demonstration collection is labor-intensive yet highly critical for effective imitation learning, our system offers a compelling solution that streamlines the collection of high-quality bimanual dexterous data, greatly enhancing accuracy and generalization across various learning algorithms. 

## **3 Teleoperation System** 

### **3.1 Overview** 

Bunny-VisionPro is a modular teleoperation system using a VR headset’s hand and wrist tracking capabilities to control a high-DoF bimanual robot, as shown in Fig. 2. The system consists of three decoupled components: hand motion retargeting, arm motion control, and human haptic feedback. 

The hand motion retargeting module maps the operator’s finger poses to the robot’s dexterous hands, enabling intuitive dexterous manipulation. Concurrently, the arm motion control module uses the operator’s wrist poses as input to compute joint angles for the robot arms while considering collision avoidance and singularity handling. The human haptic feedback module converts the tactile readings from sensors mounted on the robot’s hands into actuation signals for the wearable Eccentric Rotating Mass (ERM) actuators on the operator’s hands. This provides the operator with real-time haptic feedback, enhancing their sense of presence and allowing for more precise manipulation. 

Coordinating bimanual robots during teleoperation also requires maintaining the distance between two robot hands to match the distance between two operators’ hands, ensuring natural, coordinated movements. However, the initial distance between the robot hands may not match that of the human hands. To address this, we design several initialization modes that align the robot’s hands with the operator’s hands on the fly when the robot starts to move. Different tasks may benefit from different initialization modes. This step creates a consistent starting point, enabling intuitive and efficient bimanual task execution throughout the teleoperation process. More details are in Appendix. 

For communication, we stream hand pose results from Vision Pro to the computer via [45]. The modular architecture allows for better extensibility and enables each module to run in a separate computation process, preventing latency accumulation in the system and ensuring real-time control. 

3 

### **3.2 Robot Hand Motion Retargeting** 

The hand motion retargeting module translates human finger poses into corresponding robot joint positions. This is achieved by minimizing the difference between the fingertip keypoint vectors [46] of the human hand and the robotic hand, formulated as an online optimization problem: 



The objective function _L_ hand consists of two terms: (i). The first term minimizes the distance between the scaled human hand keypoint vectors _αvi_ and the robot hand keypoint vectors computed by forward kinematics function FK _i_ ( _q_ ), where _vi_ represents the _i_<sup>th</sup> fingertip keypoint vector, _N_ is the total number of vectors, _|| · ||_ 2 denotes Euclidean norm, _α_ is the scaling factor to adjust for size differences between the human and robot hand and _q_ is the joint positions of the robot hand bounded by the lower and upper limit, _q_<sup>_l_</sup> and _q_<sup>_u_</sup> . (ii). The second term enforces temporal smoothness by penalizing large joint position changes ∆ _q_ between consecutive frames, with weight _β_ . The optimization variable is _q_ and the objective is solved using Sequential Quadratic Programming (SQP) [47, 48], a gradient-based method that iteratively solves quadratic approximations of the problem. 

Our work uniquely addresses the real-time handling of loop joints, common in dexterous hands, where the number of joints exceeds the actual DoF. For a robot with _n_ joints, the positions of _n − k_ passive joints depend on the other _k_ active joint, represented as: 



where the passive joint _j_ ’s position _qj_ is not independent but constrained by function _cj_ . _n_ is the total number of joint positions. Instead of adding equality constraints to the optimization problem in Eq. (1), which can lead to instability and increased computation time due to the highly non-linear forward kinematic function FK( _q_ ), we reformulate the problem into a reduced dimension where the optimization variable has _k_ dimensions (active joints) instead of _n_ (total joints). Specifically, in the forward pass of optimization, the positions of passive joints are computed as Eq. (3.2). In the backward pass, the gradients of the passive joints are backpropagated to the active joints and added to their original gradients. Thereby, the gradient for the active joint _i_ is given by: 



This approach eliminates the need for SQP to handle affine approximations of the constraints, making the problem more tractable. Experimental results in Tab. 1 show a **10.2x speedup** when using this method to solve the four-bar linkage structure (a type of loop joint) in the Ability Robot Hand. 

### **3.3 Robot Arm Motion Control** 

Arm motion control involves computing the joint trajectories of the robot arm based on the wrist pose detected by Vision Pro. Traditional approaches often rely on closed-form solutions for Inverse Kinematics (IK) and handle constraints such as singularity by exploring the null space [49]. However, for typical 7-DoF arms, the 1-DoF null space may not provide enough flexibility. Modern approaches formulate the problem as an optimization task [50], similar to retargeting. It relaxes the rigid constraints of IK to accommodate additional factors. Inspired by these works, we have developed a unified and efficient optimization objective _L_ arm in Eq.(3.3) that integrates IK, collision avoidance, and singularity management for real-time motion control. 



The first term concerns the IK objective: 



Here, _p_ ee and _p_ wrist represent the robot end effector and human wrist position, respectively, while _q_ ee and _q_ wrist are their corresponding quaternions. _⟨·, ·⟩_ means inner product. The weights _β_ pos and 

4 



<!-- Start of picture text -->
FSR sensors for ERM motors for<br>tactile reading haptic feedback<br>Grasp<br>started<br>(a) Human haptic feedback from robot tactile readings  (b) Zero-drift calibration of tactile data<br><!-- End of picture text -->

Figure 3: **Human Haptics Feedback Device.** Tactile readings from FSR sensors located in the robot’s fingertips undergo calibration and low-pass filtering. The processed tactile signals then drive ERM motors to deliver touch feedback to human. 

_β_ rot allow for balancing the errors between position and rotation. Additionally, the objectives for singularity and collision avoidance are as follows: 



In the singularity avoidance objective _L_ sin, **J** represents the spatial Jacobian matrix, _s_ 0 is the smallest singular value, _s_ low is a conditional trigger for penalizing singularity, and _λ_ acts as a temperature factor. Theoretically, both _s_ 0 and the manipulability index �det[ **JJ**<sup>**T**</sup> ] can measure singularity [51], and the robot is nearing singularity when either value is low. We opt for the manipulability index as the objective due to its suitability for gradient-based optimization while using _s_ 0 as the condition. Thus, _L_ sin only takes effect when the robot approaches singularity. 

For collision detection, the GJK algorithm [52] is often employed but can be time-intensive even with convex meshes. To efficiently compute the self-collision cost _L_ col, we model each robot link as a collection of _m_ spheres. The function dist( _·, ·_ ) calculates the Euclidean distance between spheres _ei_ and _ej_ , while 1 ( _·, ·_ ) serves as an indicator function to evaluate the necessity of collision checking, with _ϵ_ provides numerical stability. Collisions are disregarded between spheres within the same link or between spheres of a parent and its direct child. This simplification not only accelerates computation but also renders the distance function differentiable. 

### **3.4 Human Haptic Feedback Device** 

Effective human manipulation relies on the integration of both visual and tactile feedback. However, many vision-based teleoperation systems [4, 23, 26, 28, 3] neglect haptic feedback. To address this limitation, we have developed a cost-effective haptic feedback system using Eccentric Rotating Mass (ERM) actuators (Fig. 3(a)). This system first processes tactile signals from robot hands (Step I) and then drives vibration motors to simulate tactile sensations (Step II). Despite its low cost, our system enables the operator to perceive and respond to the environment more intuitively with a more immersive experience, leading to improved manipulation performance. 

**Step I: Tactile Signal Processing.** The Ability hand (Fig.3(a)) uses Force-Sensitive Resistors (FSRs) to measure finger pressure. However, FSR sensors suffer from imprecision and zero-drift problems[53, 54], which are aggravated by deformable wrapping materials. To address this, we perform zero-drift calibration by recording baseline FSR readings at various joint positions and subtracting interpolated baseline values from real-time readings during operation. This efficient calibration can be performed autonomously each time teleoperation is initiated. Furthermore, we apply a low-pass filter to reduce noise and smooth the tactile data. As shown in Fig. 3(b), these signal-processing techniques significantly improve the quality and reliability of the tactile feedback. 

**Step II: Vibration Motor Driving.** In this step, we convert the processed tactile signals to ERM actuator vibrations using an ELEGOO UNO board. Since ERM motors require constant input voltage, we employ Pulse-Width Modulation (PWM) to simulate continuous haptic strength by controlling 

5 

ERM vibration intensity through modulated pulse width. To further enhance the stability of the haptic signals and the system’s robustness, we add a Bipolar Junction Transistor (BJT) between each ERM actuator and its corresponding PWM pin. This ensures that the haptic feedback of each ERM motor is individually adjusted, only activated during the pulse width, and resistant to circuit noise. 

## **4 System Evaluation** 

We validate our Bunny-VisionPro system through profiling analysis (Sec. 4.1), comparing it with advanced teleoperation systems (Sec. 4.2) on the Telekinesis benchmark [3] and custom dexterous manipulation tasks. Note that the human haptic feedback device was not used in the teleoperation comparison experiments because all demonstration collections were completed before the haptic system was designed. We evaluate the usability of haptic feedback in a user study involving untrained operators (Sec. 4.3). 

### **4.1 Profiling Results** 

We profile the performance of different modules from Sec.3 under specific conditions (Tab.1). Our method retargets hand motion on the Ability hand, handling loop joints at a speed comparable to retargeting without loop joints. For motion control, even with singularity and collision avoidance, our modules run in real-time at _>_ 60 Hz. 

### **4.2 Real Robot Teleoperation Experiments** 

**Task Suits.** The Teleskinesis [3] benchmark consists of ten single-arm-hand manipulation tasks, as listed in Tab. 2. To further gauge our system’s capability primarily for bimanual dexterous manipulation, we designed three short-horizon tasks – _grasping toy_ , _cleaning pan_ and _uncovering and pouring_ – and three long-horizon tasks – _wiping glass_ , _sweeping floor_ and _preparing coffee_ , as shown in Fig. 1. These tasks, except for _grasping toy_ , necessitate fine-grained coordination between two hands. 

**Real-world Robot Setup.** Our bimanual dexterous system consists of two UFactory xArm-7 robotic arms, each equipped with a 6-DoF Ability hand, resulting in a 24-DoF system. Each hand incorporates 30 tactile sensors distributed across five fingertips. For demonstration collection, two RealSense L515 cameras are positioned at the front and the top of the robot’s workspace to capture adequate visual observations. 

**Baselines** . We assess our system on the Teleskinesis benchmark against Teleskinesis [3] and AnyTeleop [4], using the results reported in the original papers for comparison. For our custom tasks, to ensure a fair comparison, we integrate AnyTeleop with our Vision-Pro-based hand tracking to create AnyTeleop+ and use an identical real-robot setup as our Bunny-VisionPro. 

**Teleoperation Results** . As shown in Tab. 2, Bunny-VisionPro matches or surpasses baseline methods in 9 out of 10 tasks, evidencing its system precision and robustness for hand manipulation teleoperation. However, in the _scissor pickup_ task, our system underperforms slightly due to the limited DoF in the Ability hand, which makes it challenging to insert fingers into the scissor handles. 

|CPU|i7-12700KF|Task|Telekinesis [3]|AnyTeleop [4]|Ours|
|---|---|---|---|---|---|
|Module|Time (ms)|Pickup Box Object|9/10|**10/10**|**10/10**|
||<br>|Pickup Fabric Toy|9/10|**10/10**|**10/10**|
|Retargeting (w/o loop joints)<br>|2_._54<br>|Box Rotation|6/10|6/10|**9/10**|
|Retargeting (loop joints as Cons.)<br>|34_._98<br>|Scissor Pickup|7/10|**8/10**|7/10|
|Retargeting (loop joints ours)<br>|3_._43<br>|Cup Stack|6/10|9/10|**10/10**|
|Motion Control (IK only)<br>|0_._74<br>|<br>Two Cup Stacking|3/10|7/10|**9/10**|
|Motion Control (+ Coll.)<br>|7_._85<br>|Pouring Cubes onto Plate|7/10|7/10|**10/10**|
|Motion Control (+ Sing.)<br>|10_._42<br>|Cup Into Plate|8/10|**10/10**|**10/10**|
|Motion Control (+ Coll. + Sing.)<br>|15_._93<br>|Open Drawer|9/10|**10/10**|**10/10**|
|Haptic Feedback (PWM)|0_._04|Open Drawer & Pickup Object|6/10|9/10|**10/10**|



Table 1: **Profiling Results.** We profile different modules at certain conditions. 

Table 2: **Teleoperation Results in Telekinesis Benchmark.** 10 single-arm tasks are evaluated. 

6 

|Task|Description|Arm|System|Success (_↑_)|Time (_↓_)|EpLen (_↓_)|∆Qpos (_↓_)|
|---|---|---|---|---|---|---|---|
|||**_Short-h_**|**_orizon Tasks_**|||||
|Grasp Toy|Grasp toy and place in box.|single|<sup>AnyTeleop+</sup><br>Ours|**50 / 54**<br>50 / 55|28.9<br>**24.3**|145_±_24<br>**142**_±_**21**|0.77<br>**0.35**|
|Clean Pan|Grasp panhandle and sponge|dual|AnyTeleop+|50 / 78|74.6|282_±_23|0.98|
||to clean the pan.||Ours|**50 / 58**|**30.4**|**186**_±_**17**|**0.58**|
|Uncover & Pour|<sup>Grasp container, remove lid,</sup><br>and pour into bowl.|dual|AnyTeleop+<br>Ours|50 / 77<br>**50 / 63**|63.2<br>**41.5**|189_±_21<br>**183**_±_**15**|1.26<br>**0.86**|
|||**_Long-h_**|**_orizon Tasks_**|||||
|Wipe Glass|Pull out wipes to cleanglass|dual|AnyTeleop+<br>Ours|30 / 53<br>**30 / 41**|69.0<br>**32.2**|517_±_51<br>**360**_±_**35**|1.44<br>**0.68**|
|S Fl|Sweep and dump trash|dl|AnyTeleop+|30 / 61|129.4|786_±_118|1.99|
|weep oor|using dustpan and broom|ua|Ours|**30 / 40**|**45.4**|**570**_±_**77**|**1.30**|
|PCff|Pour coffee into bottle, stir|dl|AnyTeleop+|30 / 52|95.3|705_±_42|1.87|
|repare oee|and hand it over to human|ua|Ours|**30 / 44**|**55.2**|**576**_±_**33**|**1.05**|



Table 3: **Teleoperation System Evaluation.** We measure collection success rate (Success), episode length (EpLen), collection time in minutes (Time), and joint position changes of the arms(∆Qpos). 

In self-designed manipulation tasks (Tab. 3), our system outperforms AnyTeleop+ [4], achieving 11% higher success rate with 45% task completion time. This performance confirms its precision in replicating human actions and its responsiveness and efficiency. Additionally, Bunny-VisionPro demonstrates enhanced stability and robustness, reducing episode lengths by 19% with lower variability. In contrast, AnyTeleop+ struggles with complex trajectories and large end-effector pose changes, often leading to aggressive joint movements and unpredictable, potentially unsafe robot control, as evidenced by a 43% increase in arm joint position changes during tasks. Besides, our system’s advantages are particularly pronounced in bimanual long-horizon tasks, where it excels in real-time, fine-grained coordination between two hands, leading to a better teleoperation experience. 

### **4.3 User Study of Haptic Feedback** 

We invite five untrained operators for a user study on human haptic feedback involving two tasks: (i) _toy handover_ and (ii) _ball moving_ (see Appendix for task figures). Each operator performs five trials per task, and we measure task success rates and average completion time. As shown in Fig. 4, haptic feedback maintains or improves success rates in 9 out of 10 comparisons. This boost is attributed to enhanced interaction awareness between the robot and the object, which prevents abnormal current generation in robot arms due to excessive pressure, thus promoting safer operations. Moreover, 



<!-- Start of picture text -->
w/o haptics w/ haptics<br><!-- End of picture text -->

Figure 4: **User Study.** It evaluates the impact of haptic feedback on success rates and time efficiency. 

haptic feedback allows for quicker completion of the _ball moving_ task, which requires precise control due to the ball’s low deformability. Operators report that the haptic feedback expedites object localization when their vision is partially obstructed and enhances their confidence in teleoperation. 

## **5 Imitation Learning** 

To evaluate the quality of demonstrations collected by AnyTeleop+ and our system from an imitation learning perspective, we train several popular methods: ACT [5], Diffusion Policy [34], and DP3 [40] and test their generalization performance of unseen scenarios. Besides, we investigate the effectiveness of tactile data in imitation learning. Although proven effective, the haptic feedback system is not used in the demonstration collection because it was designed after the data gathering was completed. Demonstration details are provided in Appendix. 

7 

|Task|System||ACT [5]||Diffu|sion Polic|y [34]||DP3 [40]||
|---|---|---|---|---|---|---|---|---|---|---|
|||SR|SR-SG|SR-U|SR|SR-SG|SR-U|SR|SR-SG|SR-U|
|G t|AnyTeleop+|**8/10**|**6/10**|**7/10**|4/10|3/10|3/10|**10/10**|5/10|5/10|
|rasp oy|Ours|**8/10**|4/10|5/10|**7/10**|**6/10**|**4/10**|**10/10**|**6/10**|**7/10**|
|Cl|AnyTeleop+|7/10|3/10|2/10|5/10|**4/10**|1/10|6/10|1/10|4/10|
|eanpan|Ours|**9/10**|**6/10**|**5/10**|**7/10**|**4/10**|**7/10**|**8/10**|**4/10**|**5/10**|
|U &|AnyTeleop+|2/10|0/10|1/10|3/10|**2/10**|2/10|5/10|4/10|3/10|
|ncover  pour|Ours|**8/10**|**4/10**|**8/10**|**6/10**|**2/10**|**3/10**|**7/10**|**5/10**|**7/10**|



Table 4: **Imitation Learning for Real-World Tasks.** The Success Rate (SR) is based on 10 trials, with SR-SG indicating success rates for spatial generalization and SR-U for unseen objects. 

### **5.1 Main Results.** 

As shown in Tab. 4, Bunny-VisoinPro significantly outperforms AnyTeleop+ by an average of 22% success rate across three tasks using three different policies. This showcases the superior quality of the demonstrations collected by our system. Our system’s effectiveness is particularly evident in bimanual tasks, _i.e. cleaning pan_ and _uncovering and pouring_ . One possible reason for this improvement is that our system handles the alignment of bimanual robots delicately, enabling the collection of demonstrations with more natural robot motions. 

**Generalization.** We assess the generalizability of policies learned on AnyTeleop+ and our demonstrations. It evaluates spatial generalization (SR-SG) with random object poses, and the ability to manipulate unseen objects (SR-U) varying in shape, size, and color. As shown in Tab. 4, BunnyVisionPro exceeds by 14% SR-SG and 26% SR-U, suggesting that high-quality, trajectory-consistent demonstrations significantly improve generalization in imitation learning. Details are in Appendix. 

**Long-horizon Tasks.** For complicated, multi-stage tasks, the policy achieves notable success rates – 73% for sub-tasks and 38% for entire tasks – with only 30 demonstrations. This manifests the reliability of long-horizon data collection of our system to serve advanced manipulation task learning. 

### **5.2 Tactile Data as Policy Input** 

**Tactile Data Processing.** FSR sensors capture the pressure on the robot during object gripping. These signals can also be processed to calculate impulse by differentiating force over time. For tactile learning, touch signals are represented as vectors, encoded using MLPs, or visualized as point sets for visual embedding learning, akin to DexPoint [55] (see Appendix for details). 

**Results and Discussion.** As shown in Tab. 6, utilizing tactile data does not necessarily enhance outcomes, potentially because vision alone suffice for these tasks. Tactile feedback only activates upon the contact between hands and objects, thus not aiding in the object’s identification or localization. Moreover, using force data delivers slightly inferior performance compared to impulse data, possibly due to the zero-point drift in tactile readings over time. This drift, likely caused by the deformation of viscous materials used in sensor embedding, can persistently alter force reading during tasks, leading to unstable performance. Impulse, by contrast, is more robust against such variations. 

|Task|DP3 [|40]|Signal|Representation|Clean pan|Uncover & pour|
|---|---|---|---|---|---|---|
|Wipe glass|SR-subtask<br>7/10|SR<br>7/10|/<br>force<br>impulse|/<br>vector<br>vector|**8/10**<br>7/10<br>**8/10**|7/10<br>4/10<br>7/10|
|Sweep floor|8/10|4/10|force|point cloud|7/10|6/10|
|Prepare coffee|7/10|4/10|impulse|<br>point cloud|7/10|**8/10**|



Table 5: **DP3 Results for Long-Horizon Tasks.** SR-subtask is subtask success rate. 

Table 6: **Ablation of Touch as DP3 Policy Input.** Success rates are reported for two bimanual tasks. 

## **6 Conclusion and Limitation** 

**Limitation.** Our system has two main limitations: (i) Vision Pro’s hand tracking is inaccurate when fingers are self-occluded, causing jerky control commands. This issue could be mitigated by fusing data from wearable devices with Vision Pro. (ii) Subtle changes in haptic feedback are difficult to 

8 

sense when the robot touches an object lightly. In future work, we will consider using actuators with larger contact areas and better sensitivity, such as piezoelectric actuators, to address this problem. 

**Conclusion.** In this paper, we introduce Bunny-VisionPro, a bimanual dexterous teleoperation system for real-time robotic control. Our system utilizes Vision Pro to track hand poses and convert them into control commands, addressing critical challenges including loop joint hand retargeting, collision avoidance, and singularity to ensure accurate, safe, and responsive operations. Moreover, we develop a haptic feedback device that delivers tactile sensations to the operator, thus enhancing control accuracy and fostering a more immersive experience. 

### **Acknowledgments** 

We extend our sincere thanks to An-Chieh Cheng, Luobin Wang, Jiarui Xu, and Xinyu Zhang for their efforts in testing and evaluating the teleoperation system. 

9 

## **References** 

- [1] K. Hauser. Recognition, prediction, and planning for assisted teleoperation of freeform tasks. _Autonomous Robots_ , 35:241–254, 2013. 

- [2] N. Zhong and K. Hauser. Attentiveness map estimation for haptic teleoperation of mobile robot obstacle avoidance and approach. _IEEE Robotics and Automation Letters_ , 2024. 

- [3] A. Sivakumar, K. Shaw, and D. Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2022. 

- [4] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 

- [5] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning fine-grained bimanual manipulation with low-cost hardware. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 

- [6] Z. Fu, T. Z. Zhao, and C. Finn. Mobile aloha: Learning bimanual mobile manipulation with low-cost whole-body teleoperation. _arXiv preprint arXiv:2401.02117_ , 2024. 

- [7] H. Fang, H.-S. Fang, Y. Wang, J. Ren, J. Chen, R. Zhang, W. Wang, and C. Lu. Low-cost exoskeletons for learning whole-arm manipulation in the wild. _arXiv preprint arXiv:2309.14975_ , 2023. 

- [8] A. Toedtheide, X. Chen, H. Sadeghian, A. Naceri, and S. Haddadin. A force-sensitive exoskeleton for teleoperation: An application in elderly care robotics. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 12624–12630. IEEE, 2023. 

- [9] P. Wu, Y. Shentu, Z. Yi, X. Lin, and P. Abbeel. Gello: A general, low-cost, and intuitive teleoperation framework for robot manipulators. _arXiv preprint arXiv:2309.13037_ , 2023. 

- [10] A. Tung, J. Wong, A. Mandlekar, R. Mart´ın-Mart´ın, Y. Zhu, L. Fei-Fei, and S. Savarese. Learning multi-arm manipulation through collaborative teleoperation. In _2021 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9212–9219. IEEE, 2021. 

- [11] W. Zhao, J. Chai, and Y.-Q. Xu. Combining marker-based mocap and rgb-d camera for acquiring high-fidelity hand motion data. In _Proceedings of the ACM SIGGRAPH/eurographics symposium on computer animation_ , pages 33–42, 2012. 

- [12] S. Liu, H. Jiang, J. Xu, S. Liu, and X. Wang. Semi-supervised 3d hand-object poses estimation with interactions in time. In _CVPR_ , 2021. 

- [13] H. Zhang, Z. Zhao, Y. Yu, K. Gui, X. Sheng, and X. Zhu. A feasibility study on an intuitive teleoperation system combining imu with semg sensors. In _Intelligent Robotics and Applications: 11th International Conference, ICIRA 2018, Newcastle, NSW, Australia, August 9–11, 2018, Proceedings, Part I 11_ , pages 465–474. Springer, 2018. 

- [14] T. Zhang, Z. McCarthy, O. Jow, D. Lee, X. Chen, K. Goldberg, and P. Abbeel. Deep imitation learning for complex manipulation tasks from virtual reality teleoperation. In _ICRA_ , 2018. 

- [15] J. DelPreto, J. I. Lipton, L. Sanneman, A. J. Fay, C. Fourie, C. Choi, and D. Rus. Helping robots learn: A human-robot master-apprentice model using demonstrations via virtual reality teleoperation. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 10226–10233, 2020. doi:10.1109/ICRA40945.2020.9196754. 

- [16] Y. Pan, C. Chen, D. Li, Z. Zhao, and J. Hong. Augmented reality-based robot teleoperation system using rgb-d imaging and attitude teaching device. _Robotics and Computer-Integrated Manufacturing_ , 71:102167, 2021. 

10 

- [17] A. Iyer, Z. Peng, Y. Dai, I. Guzey, S. Haldar, S. Chintala, and L. Pinto. Open teach: A versatile teleoperation system for robotic manipulation. _arXiv preprint arXiv:2403.07870_ , 2024. 

- [18] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. _arXiv preprint arXiv:2403.07788_ , 2024. 

- [19] H. Liu, Z. Zhang, X. Xie, Y. Zhu, Y. Liu, Y. Wang, and S.-C. Zhu. High-fidelity grasping in virtual reality using a glove-based system. In _2019 international conference on robotics and automation (icra)_ , pages 5180–5186. IEEE, 2019. 

- [20] M. Mosbach, K. Moraw, and S. Behnke. Accelerating interactive human-like manipulation learning with GPU-based simulation and high-quality demonstrations. In _Humanoids_ , 2022. 

- [21] M. Schwarz, C. Lenz, A. Rochow, M. Schreiber, and S. Behnke. Nimbro avatar: Interactive immersive telepresence with force-feedback telemanipulation. In _2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 5312–5319. IEEE, 2021. 

- [22] M. Meta. Manus meta quantum mocap metagloves. `https://www.ufactory.cc/pages/ xarm` . 

- [23] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _ICRA_ , 2020. 

- [24] S. Li, N. Hendrich, H. Liang, P. Ruppel, C. Zhang, and J. Zhang. A dexterous hand-arm teleoperation system based on hand pose estimation and active vision. _IEEE Transactions on Cybernetics_ , 2022. 

- [25] Y. Qin, H. Su, and X. Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _RA-L_ , 7(4):10873–10881, 2022. 

- [26] S. P. Arunachalam, I. G¨uzey, S. Chintala, and L. Pinto. Holo-dex: Teaching dexterity with immersive mixed reality. _arXiv preprint arXiv:2210.06463_ , 2022. 

- [27] L. S. Yim, Q. T. Vo, C.-I. Huang, C.-R. Wang, W. McQueary, H.-C. Wang, H. Huang, and L.-F. Yu. Wfh-vr: Teleoperating a robot arm to set a dining table across the globe via virtual reality. In _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 4927–4934. IEEE, 2022. 

- [28] P. Ponomareva, D. Trinitatova, A. Fedoseev, I. Kalinov, and D. Tsetserukou. Grasplook: a vrbased telemanipulation system with r-cnn-driven augmentation of virtual environment. In _2021 20th International Conference on Advanced Robotics (ICAR)_ , pages 166–171. IEEE, 2021. 

- [29] T. Lin, Y. Zhang, Q. Li, H. Qi, B. Yi, S. Levine, and J. Malik. Learning visuotactile skills with two multifingered hands. _arXiv preprint arXiv:2404.16823_ , 2024. 

- [30] E. Jang, A. Irpan, M. Khansari, D. Kappler, F. Ebert, C. Lynch, S. Levine, and C. Finn. Bc-z: Zero-shot task generalization with robotic imitation learning. In _Conference on Robot Learning_ , pages 991–1002. PMLR, 2022. 

- [31] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, T. Jackson, S. Jesmonth, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, K.-H. Lee, S. Levine, Y. Lu, U. Malla, D. Manjunath, I. Mordatch, O. Nachum, C. Parada, J. Peralta, E. Perez, K. Pertsch, J. Quiambao, K. Rao, M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran, V. Vanhoucke, S. Vega, Q. Vuong, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. Rt-1: Robotics transformer for real-world control at scale. _arXiv preprint arXiv:2212.06817_ , 2022. 

11 

- [32] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, P. Florence, C. Fu, M. G. Arenas, K. Gopalakrishnan, K. Han, K. Hausman, A. Herzog, J. Hsu, B. Ichter, A. Irpan, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, L. Lee, T.-W. E. Lee, S. Levine, Y. Lu, H. Michalewski, I. Mordatch, K. Pertsch, K. Rao, K. Reymann, M. Ryoo, G. Salazar, P. Sanketi, P. Sermanet, J. Singh, A. Singh, R. Soricut, H. Tran, V. Vanhoucke, Q. Vuong, A. Wahid, S. Welker, P. Wohlhart, J. Wu, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. Rt-2: Vision-language-action models transfer web knowledge to robotic control. _arXiv preprint arXiv:2307.15818_ , 2023. 

- [33] S. Reed, K. Zolna, E. Parisotto, S. G. Colmenarejo, A. Novikov, G. Barth-maron, M. Gim´enez, Y. Sulsky, J. Kay, J. T. Springenberg, T. Eccles, J. Bruce, A. Razavi, A. Edwards, N. Heess, Y. Chen, R. Hadsell, O. Vinyals, M. Bordbar, and N. de Freitas. A generalist agent. _Transactions on Machine Learning Research_ , 2022. ISSN 2835-8856. URL `https://openreview. net/forum?id=1ikK0kHjvj` . Featured Certification, Outstanding Certification. 

- [34] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. Burchfiel, and S. Song. Diffusion policy: Visuomotor policy learning via action diffusion. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 

- [35] J. Pari, N. M. Shafiullah, S. P. Arunachalam, and L. Pinto. The surprising effectiveness of representation learning for visual imitation. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2022. 

- [36] A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Mart´ın-Mart´ın. What matters in learning from offline human demonstrations for robot manipulation. _arXiv preprint arXiv:2108.03298_ , 2021. 

- [37] S. Haldar, J. Pari, A. Rai, and L. Pinto. Teach a robot to fish: Versatile imitation from one minute of demonstrations. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 

- [38] C. Wang, L. Fan, J. Sun, R. Zhang, L. Fei-Fei, D. Xu, Y. Zhu, and A. Anandkumar. Mimicplay: Long-horizon imitation learning by watching human play. In _Proceedings of the 7th Conference on Robot Learning (CoRL)_ , 2023. 

- [39] M. Shridhar, L. Manuelli, and D. Fox. Perceiver-actor: A multi-task transformer for robotic manipulation. In _Proceedings of the 6th Conference on Robot Learning (CoRL)_ , 2022. 

- [40] Y. Ze, G. Zhang, K. Zhang, C. Hu, M. Wang, and H. Xu. 3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2024. 

- [41] A. Goyal, J. Xu, Y. Guo, V. Blukis, Y.-W. Chao, and D. Fox. Rvt: Robotic view transformer for 3d object manipulation. _arXiv:2306.14896_ , 2023. 

- [42] T. Gervet, Z. Xian, N. Gkanatsios, and K. Fragkiadaki. Act3d: 3d feature field transformers for multi-task robotic manipulation. In _7th Annual Conference on Robot Learning_ , 2023. URL `https://openreview.net/forum?id=-HFJuX1uqs` . 

- [43] J. Grannen, Y. Wu, B. Vu, and D. Sadigh. Stabilize to act: Learning to coordinate for bimanual manipulation. In _Conference on Robotic Learning (CoRL)_ , 2023. 

- [44] W. Yang, A. Angleraud, R. S. Pieters, J. Pajarinen, and J.-K. K¨am¨ar¨ainen. Seq2seq imitation learning for tactile feedback-based manipulation. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 5829–5836. IEEE, 2023. 

- [45] Y. Park. Teleopeation system using apple vision pro. URL `https://github.com/ Improbable-AI/VisionProTeleop` . 

12 

- [46] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pages 570–587. Springer, 2022. 

- [47] P. T. Boggs and J. W. Tolle. Sequential quadratic programming. _Acta numerica_ , 4:1–51, 1995. 

- [48] S. G. Johnson and J. Schueller. Nlopt: Nonlinear optimization library. _Astrophysics Source Code Library_ , pages ascl–2111, 2021. 

- [49] A. Dietrich, T. Wimbock, A. Albu-Schaffer, and G. Hirzinger. Reactive whole-body control: Dynamic mobile manipulation using a large number of actuated degrees of freedom. _IEEE Robotics & Automation Magazine_ , 19(2):20–33, 2012. 

- [50] M. Bhardwaj, B. Sundaralingam, A. Mousavian, N. D. Ratliff, D. Fox, F. Ramos, and B. Boots. Storm: An integrated framework for fast joint-space model-predictive control for reactive manipulation. In _Conference on Robot Learning_ , pages 750–759. PMLR, 2022. 

- [51] T. Yoshikawa. Manipulability of robotic mechanisms. _The international journal of Robotics Research_ , 4(2):3–9, 1985. 

- [52] E. G. Gilbert, D. W. Johnson, and S. S. Keerthi. A fast procedure for computing the distance between complex objects in three-dimensional space. _IEEE Journal on Robotics and Automation_ , 4(2):193–203, 1988. 

- [53] A. Barnea, C. Oprisan, and D. Olaru. Force sensitive resistors calibration for use in gripping devices. _Mechanical testing and diagnosis_ , 2(3):18–27, 2012. 

- [54] G. S. Lakshmi and R. Hemavathi. Calibration of force sensitive resistor used in force controlled grippers. _Int. J. Eng. Res. Technol_ , 9:356–358, 2020. 

- [55] Y. Qin, B. Huang, Z.-H. Yin, H. Su, and X. Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In _Conference on Robot Learning_ , pages 594–605. PMLR, 2023. 

13 

## **Appendix Outline** 

In these supplementary materials, we provide additional details for our Bunny-VisionPro teleoperation system, including: 

Sec. A Bimanual teleoperation initialization modes. 

Sec. B Sphere Modeling of Robot Links in Collision Checking. 

Sec. C Task suits design and demonstration details. 

Sec. D Haptic feedback implementation. 

Sec. E Tactile data processing for Imitation Learning. 

Sec. F Imitation learning implementation. 

## **A Bimanual Teleoperation Initialization** 

Teleoperation systems facilitate the mapping of human movements to robotic actions. For example, moving the right hand forward by 0.1 meters should result in an equivalent movement of the robot’s right end effector. To ensure precise translation of human motions into robotic actions in a three-dimensional space, it is essential to define and synchronize coordinate systems for both the human operator and the robot during an initialization step. This phase involves establishing a three-dimensional framework, known as the initial human frame and the initial robot frame, for both systems. Movements made by the human operator are then measured relative to the initial human frame, and the robot replicates these movements within its own initial robot frame. 

Bimanual teleoperation requires careful consideration of the relative positioning of the operator’s two hands, which is critical for tasks that demand intricate dual-hand coordination. Given that the spacing between a robot’s hands can differ from that of a human due to the specific hardware configuration, designing adaptable initialization modes that can dynamically align the robot’s hands with those of the operator is vital. To address diverse operational requirements, we have developed several alignment modes: 

- `ALIGN` ~~`S`~~ `EPARATELY` : Each arm is treated as an independent unit, which is ideal for tasks that require distinct arm movements. 

- `ALIGN` ~~`C`~~ `ENTER` : This mode calculates a midpoint between the two robot end effectors and aligns it with the central point between the human operator’s hands. 

- `ALIGN` ~~`L`~~ `EFT` and `ALIGN` ~~`R`~~ `IGHT` : These modes focus on aligning the robot’s movements with either the left or the right hand of the human operator, which is beneficial for tasks that prioritize activity on one side. 

Our system provides users with the flexibility to select from these modes, offering a range of options to suit specific task demands. 

## **B Sphere Modeling in Collision Checking** 

To enable fast and differentiable collision avoidance during real-time teleoperation, we represent each link of the robot arm with multiple spheres of varying sizes, as detailed in Sec. 3.3 of the main paper. Fig. 5 depicts these modeled spheres. We expedite the collision detection process by ignoring collisions between spheres within the same link or between a parent link and its direct child. This approach allows us to efficiently compute the gradient necessary for optimizing motion control in collision avoidance scenarios. 

14 



Figure 5: **Sphere Modeling of Robot Arm Links** for efficient and differentiable collision checking and avoidance. 

## **C Task Suits Design** 

**Task Suits Design.** In our main paper, teleoperation and imitation learning tasks are illustrated in Figure 1. Here, we provide the detailed task pipeline, depicted in Figure 6. For the user study of haptics, we design _toy handover_ and _ball moving_ tasks, which are illustrated in Fig. 7. 

**Demonstration Details.** On the camera side, we collect images and processed point cloud data at approximately 30 Hz. Concurrently, the robots’ proprioceptive data is recorded at over 100 Hz. These two data streams are timestamp-aligned via interpolation and downsampled to 10 Hz for imitation training. For short-horizon tasks, we gather 50 demonstrations per task; for long-horizon tasks, 30 demonstrations per task are collected. 

## **D Haptic Feedback Implementation** 

Our implementation of haptic feedback can be divided into two aspects: server-side signal processing and Arduino-side motor control. 

**Server-side signal processing.** As outlined in Algorithm 1, the server side involves several stages of signal manipulation. Initially, tactile readings are calibrated, filtered, and normalized (refer to Section 3.4 for details). Subsequently, these processed signals are converted into valid PWM values and transmitted to the ELEGOO UNO board. This ensures that the tactile data are accurately prepared for motor activation, facilitating precise control over haptic feedback. 

**Arduino-side motor control.** Algorithm 2 details the pseudo-code for motor control on the Arduino side. This component of the system is responsible for parsing the PWM values received via serial communication from the server. Once parsed, these values are directly mapped to the PWM pins on the board, which in turn control the ERM motors. This arrangement enables the Arduino to dynamically adjust the intensity of the haptic feedback based on the input from the server, ensuring that the haptic responses are both timely and contextually appropriate. 

15 



Figure 6: **Task Pipeline for Teleoperation and Imitation Learning.** We design six tasks including three short-horizon ones (top three rows) – _grasping toy_ , _uncovering and pouring_ and _cleaning pan_ – and three long-horizon ones (bottom three rows) – _wiping glass_ , _sweeping floor_ and _preparing coffee_ . 



Figure 7: **Task Pipeline for Haptic User Study.** We design two tasks: _ball moving_ and _toy handover_ . The former requires precise and careful control due to the minimal deformability of the balls, while the latter involves manipulating soft and deformable toys. 

16 

### **Algorithm 1** Server-side tactile signal processing 

1: **Initialize** serial connection with a specified baud rate 2: **while** True **do** _▷_ Until manually stopped 3: _V ←_ Get tactile sensor values from robot hand 4: _V_ � _←_ Calibrate and smoothen the tactile readings 5: _T ←_ Set ERM activation threshold based on _V_<sup>�</sup> <u>(</u> _V_<sup>�</sup> _−T_ <u>)</u> _×_ <u>(255</u> _−_ 0) 6: _V_ norm _←_ clip( , 0, 255) _▷_ Normalize _V_ and clip _V_ to [0, 255] � max( _V_<sup>�</sup> ) _−T_ � 7: Send _V_ norm to serial port as PWM values 8: **end while** 

### **Algorithm 2** Arduino-side motor controlling 

1: **Define** _numMotors ▷_ Total number of motors 2: **Define** _motorPins_ [1 _. . . numMotors_ ] _▷_ Array of PWM pins for each motor 3: **function** SETUP 4: **for** _i ←_ 1 **to** _numMotors_ **do** 5: _pinMode_ ( _motorPins_ [ _i_ ] _,_ OUTPUT) _▷_ Set each motor pin as an output 6: **end for** 7: **Initialize** serial communication with a specified baud rate 8: **end function** 9: **function** LOOP 10: **if** Serial.available() _≥ numMotors ×_ sizeof( _PWM_ value) **then** 11: _pwmV alues_ [1 _. . . numMotors_ ] _←_ Parse PWM values from Serial 12: **for** _i ←_ 1 **to** _numMotors_ **do** 13: analogWrite( _motorPins_ [ _i_ ] _, pwmV alues_ [ _i_ ]) _▷_ Write PWM values to motor pins 14: **end for** 15: **end if** 16: **end function** 

## **E Tactile Data Processing** 

We integrate tactile signals from the fingertips of the Ability hand into our imitation learning framework to evaluate its effectiveness across various conditions. On the **data acquisition** side, raw data from FSR sensors, which measure the pressure exerted on the robot during object manipulation, undergo zero-drift calibration and low-pass filtering similar to haptic feedback processing. Additionally, these signals can be processed to calculate force impulse by differentiating force over time. For tactile **data representation** , touch signals are effectively expressed as vectors, treated as components of the robot’s state, and encoded using Multi-layer Perceptrons (MLPs). Furthermore, since touch indicates contact points between the robot and an object, these points are visualized as imaginary point sets. These are then concatenated with point cloud data from cameras to enhance visual embedding in the visual observation space for the imitation learning policy. To highlight active signals, we append a boolean dimension to indicate when tactile signals exceed predefined thresholds: 500 for force data and 50 for impulse data. This representation is inspired and adapted from DexPoint [55]. 

## **F Imitation Learning Implementation** 

We implement ACT [5], Diffusion Policy [34] and 3D Diffusion Policy [40] to rigorously evaluate the demonstration quality collected by our system. To enhance performance assessment, we design generalization experiments focusing on the spatial locations of objects and interaction with unseen objects for each task. Details are further elaborated below. 

17 



<!-- Start of picture text -->
grasp toy uncover & pour clean pan<br>spatial<br>generalization<br>unseen object<br>generalization<br><!-- End of picture text -->

Figure 8: **Generalization Design of Imitation Learning.** Blue boxes represent the spatial generalization range for objects, whereas green boxes identify unseen objects that were not present during the collection of demonstrations. 

**Learning Algorithms.** For Diffusion Policy, we employ multi-view images as visual inputs and establish a horizon of 8, consisting of 2 observation steps and 6 action steps. The model is trained for 300 epochs with a batch size of 64. For 3D Diffusion Policy, we utilize multi-view point clouds as inputs and maintain the same horizon settings as the Diffusion Policy. This model is trained for 500 epochs with a batch size of 64. For ACT, multi-view images are used, the chunk size is set as 20, and the training extends 3000 epochs. 

**Generalization Evaluation Design.** For generalization experiments involving different spatial locations and novel objects not present in the demonstrations, we detail the design for each task in Fig. 8. The spatial range encompasses a large working space, while the unseen objects vary in size, color, and shape, providing a comprehensive evaluation of the robustness of policies learned from our demonstrations. 

18 

