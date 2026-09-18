# **Bridging the Human to Robot Dexterity Gap through Object-Oriented Rewards** 

Irmak Guzey<sup>_†_</sup> Yinlong Dai Georgy Savva Raunaq Bhirangi Lerrel Pinto 

New York University 

object-rewards.github.io 



<!-- Start of picture text -->
𝒯<br>H<br>Reward  R (𝒯 R , 𝒯 H ) Policy<br>𝒯 R<br>Human Video Robot Policy<br>Human<br>Robot<br><!-- End of picture text -->

Fig. 1: HUDOR generates rewards from human videos by tracking points on the manipulable object, indicated by the rainbow-colored dots, over the trajectory. This allows for online training of multi-fingered robot hands given only a _single_ video of a human solving the task (left) without any robot teleoperation. To optimize the robot’s policy (middle), rewards are computed by matching the point movements of the robot policy _TR_ with those in the human video _TH_ . In under an hour of online fine-tuning, our Allegro robot hand (right) is able to _open the music box_ . 

**_Abstract_ — Training robots directly from human videos is an emerging area in robotics and computer vision. While there has been notable progress with two-fingered grippers, learning autonomous tasks for multi-fingered robot hands in this way remains challenging. A key reason for this difficulty is that a policy trained on human hands may not directly transfer to a robot hand due to morphology differences. In this work, we present HUDOR, a technique that enables online fine-tuning of policies by directly computing rewards from human videos. Importantly, this reward function is built using object-oriented trajectories derived from off-the-shelf point trackers, providing meaningful learning signals despite the morphology gap and visual differences between human and robot hands. Given a single video of a human solving a task, such as gently opening a music box, HUDOR enables our four-fingered Allegro hand to learn the task with just an hour of online interaction. Our experiments across four tasks show that HUDOR achieves a 4** _×_ **improvement over baselines. Code and videos are available on our website, https://object-rewards.github.io/.** 

## I. INTRODUCTION 

Humans effortlessly perform a wide range of dexterous tasks in their daily lives [1]. Achieving similar capabilities in robots is essential for their effective deployment in the real world. Towards this end, recent advances have enabled the learning of multi-modal, long-horizon, and dexterous 

> _†_ Correspondence to irmakguzey@nyu.edu. 

behaviors for two-fingered grippers [2, 3, 4, 5] using imitation learning (IL) from teleoperated robot data. However, extending such methods to complex tasks with multi-fingered hands has proven challenging. 

The challenge of using teleoperation-based learning for multi-fingered hands arises from two key issues. First, achieving even moderate robustness this way requires large amounts of data. Tasks involving two-fingered grippers [6, 7, 8, 9] often demand thousands of demonstrations to train robust policies. This data requirement is likely even greater for hands with larger action dimensions and tasks that require higher levels of precision and dexterity. Second, teleoperating multi-fingered hands presents a challenging systems problem due to the need for low-latency and continuous feedback when controlling multiple degrees of freedom [10, 11, 12]. This makes it even harder to collect the large amounts of data needed to accomplish dexterous tasks. 

An alternate approach that circumvents teleoperation is to develop policies for robots using videos of humans executing tasks [13, 14, 15]. However, most previous approaches have required either additional teleoperated robot demonstrations [16] or human-intervened learning [17] for fine-tuning. This extra information is often necessary to bridge the gap between the morphological and visual differences between human hands (as seen in human video data) and robot hands 

(as observed in robot interactions). 

In this work, we present HUDOR, a new approach to bridge the gap between human videos and robot policies through online imitation learning. Given a human video and hand pose trajectory, an initial robot replay can be generated using pose transformation and full robot inverse kinematics. However, this initial replay often fails due to morphological differences between human and robot hands. HUDOR improves this initial replay through a multi-step process: (a) We track the points of the manipulated object in both human and robot trajectory videos; (b) then compute the similarity of object motion and articulation using these tracked point sets, (c) and finally fine-tune the initial robot policy through reinforcement learning. By iteratively refining its performance based on these comparisons, the robot effectively imitates human demonstrations while adapting to its physical constraints. Our framework is shown in Fig. 1. 

We evaluate HUDOR on four dexterous tasks, including opening a small music box with one hand and slide-picking up a thin card. Our contributions can be summarized as follows: 

- 1) HUDOR introduces the first framework that enables the learning of dexterous policies on multi-fingered robot hands using only a single human video and hand pose trajectory (Section IV). 

- 2) HUDOR introduces a novel approach for objectoriented reward computation that matches human and robot trajectories. This results in 2.1 _×_ better performance on three of our tasks than common reward functions (Section IV-C). 

- 3) HUDOR outperforms state-of-the-art offline imitation learning methods for learning from human demonstrations [17, 3], achieving an average improvement of 2.64 _×_ , emphasizing the need for online corrections (Section IV-B). 

Robot videos are best viewed on our website: https: 

//object-rewards.github.io/. 

## II. RELATED WORKS 

Our work draws inspiration from extensive research in dexterous manipulation, learning from human videos, and imitation learning. In this section, we focus our discussion on the most pertinent contributions across these interrelated areas. 

_a) Robot Learning for Dexterous Manipulation:_ Learning dexterous policies for multi-fingered hands has been a long-standing challenge that has captured the interest of the robotics learning community [18, 19, 10]. Some works have addressed this problem by training policies in simulation and deploying them in the real world [20, 19]. Although this approach has produced impressive results for in-hand manipulation [21, 22], closing the sim-to-real gap becomes cumbersome when manipulating in-scene objects. 

Other works have focused on developing different teleoperation frameworks [23, 24, 11, 25] and training offline policies using robot data collected through these frameworks. While these frameworks are quite responsive, teleoperating 

dexterous hands without directly interacting with objects remains difficult for users due to the morphological mismatch between current robotic hands and the lack of tactile feedback for the teleoperator. 

Given the challenges of large-scale data collection, most offline dexterous policies tend to fail due to overfitting. To mitigate this, some previous works have focused on learning policies with limited data [26, 27], either by using nearestneighbor matching for action retrieval [28, 26, 11, 23] or by initializing with a sub-optimal offline policy and finetuning that or learning a residual policy with online interactions to improve generalization [27, 29, 30]. 

_b) Learning from Human Videos:_ To scale up data collection using more accessible sources, the vision and robotics communities have worked on learning meaningful behaviors and patterns from human videos [31, 32, 33, 34]. Some efforts focus on learning simulators that closely mimic the real-world environment of the robot from human videos using generative models [32, 35, 31], using these simulators to train policies and make decisions by predicting potential future outcomes. 

Other works use internet-scale human videos to learn higher-level skills or affordances [33, 36]. However, these works either require low-level policies to learn action primitives for interacting with objects [33] or only focus on simple tasks where a single point of contact is sufficient for manipulation [36]. Yet other approaches leverage on-scene human videos to learn multi-stage planning [16, 14] but need additional robot data to learn lower-level object interactions. Notably, all of these works focused on two-gripper robots, where manipulation capabilities are limited and objects are less articulated. 

A few recent studies [17, 37, 38] address this issue for dexterous hands by using in-scene human videos collected by multiple cameras in conjunction with hand motion capture systems. These studies either focus on simple grasping tasks [38, 37] or require an online fine-tuning stage with human feedback for dexterous tasks [17]. Additionally, the offline learning process for these approaches requires extensive pre-processing to mask the human hand from the environment point cloud. 

HUDOR differs from these works by eliminating the need for cumbersome human feedback, automatically extracting a reward from a single human demonstration, and allowing the robot to learn from its mistakes to account for the morphology mismatch between the robot and the human. 

## III. LEARNING TELEOPERATION-FREE ONLINE DEXTERIOUS POLICIES 

HUDOR introduces a framework to learn dexterous policies from a single in-scene human video of task execution. Our method involves three steps: (1) A human video and corresponding hand pose trajectory are recorded using a VR headset and an RGB camera; (2) hand poses are transferred and executed on the robot using pose transformation and fullrobot inverse kinematics (IK); and (3) reinforcement learning 



<!-- Start of picture text -->
ao t<br>W<br>W aa t<br>HRW<br>aa t HOW<br><!-- End of picture text -->

Fig. 2: Illustration of the robot setup and trajectory transfer in HUDOR. ArUco markers are used for calibration. The human demonstration is collected in-scene, i.e. demonstrator is in the same scene as the robot. The VR headset is used solely for obtaining the fingertip positions with respect to the robot frame (illustrated with colored dots) and can be worn or attached to the setup as needed. World frame _W_ is visualized on the ArUco marker on the operation table. 

(RL) is used to successfully imitate the expert trajectory. In this section, we explain each component in detail. 

## _A. Robot Setup and Human Data Collection_ 

Our hardware setup includes a Kinova JACO 6-DOF robotic arm with a 16-DOF four-fingered Allegro hand [10] attached. Two RealSense RGBD cameras [39] are positioned around the operation table for calibration and visual data collection. A Meta Quest 3 VR headset is used to collect hand pose estimates. Our first step involves computing the relative transformation between the VR frame and the robot frame to directly transfer the recorded hand pose trajectory from the human video to the robot as shown in Fig. 2. We use two ArUco markers – one on the operation table and another on top of the Allegro hand – to compute relative transformations. The first marker is used to define a world frame and transform fingertip positions from the VR frame to the world frame, while the second marker is used to determine the transformation between the robot’s base and the world frame. 

_a) Relative Transformations:_ We collect human hand pose estimates using existing hand pose detectors on the Quest 3 VR Headset, and capture visual data using the RGBD cameras. Fingertip pose for the _i_<sup>th</sup> human fingertip captured in the VR frame at time _t_ , _a_<sup>_t,i_</sup> _o_<sup>, are first transformed</sup> to the world frame as _a_<sup>_t,i_</sup> _w_<sup>=</sup><sup>_HOWat,i_</sup> _o_<sup>,where</sup><sup>_HOW_isthe</sup> homogeneous transform from the VR frame to the world frame. This transform is computed by detecting the ArUco marker on the table using the cameras on the VR headset. A standard calibration procedure [40] is used to compute the transformation _HRW_ between the robot frame and the world frame by detecting the two ArUco markers using the RGB camera shown in Fig. 2. This calibration allows us to directly transfer human fingertip positions from the Oculus headset to the robot’s base using the equation: 





where, _a_<sup>_t,i_</sup> _r_ are the homogeneous coordinates of the _i_<sup>th</sup> human fingertip positions from the recorded video in the robot frame. Henceforth, we use _a_<sup>_t_</sup> _r_<sup>= [</sup><sup>_a_</sup> _r_<sup>_t,_0</sup><sup>_, a_</sup> _r_<sup>_t,_1</sup><sup>_, a_</sup> _r_<sup>_t,_2</sup><sup>_a_</sup> _r_<sup>_t,_3]to</sup> refer to the 12-dimensional vector containing concatenated locations of the four fingertips in robot frame. 

_b) Data Collection:_ Using the VR application we implemented, a user can pinch the index finger and thumb of their right hand to begin interacting with the object directly using their own hands. After collecting the demonstration, they can pinch their fingers again to signal the end of the demo. We calculate the wrist pose relative to the world frame at the start of the demo, and during deployment, we initialize the robot’s arm to that initial wrist pose. This allows the robot to begin its exploration from a suitable starting position. 

_c) Data alignment:_ During data collection, we record the fingertip positions _a_<sup>_t_</sup> _r_<sup>and image data</sup><sup>_ot_for all</sup><sup>_t_= 1</sup><sup>_. . . T_</sup> where _T_ is the trajectory length. Since these components are collected at different frequencies, we align them on collected timestamps to produce synchronized tuples ( _a_<sup>_t_</sup> _r_<sup>_, ot_)foreach</sup> time _t_ . The data is then subsampled to 5 Hz. 

_d) Inverse Kinematics:_ To ensure the robot’s fingertips follow the desired positions relative to its base, we implement a custom inverse kinematics (IK) module for the full robot arm-hand system. This module uses gradient descent on the joint angles, using the Jacobian of the robot fingertips with respect to the joint angles, to minimize the distance between desired fingertip positions and the current ones [41]. For the IK optimizer, we apply different learning rates for the hand and arm joints, allowing it to prioritize the hand movements. The hand learning rate is set to be 50 times higher than the arm learning rate, enabling more natural and precise control of the fingers. To summarize, the IK module takes the desired fingertip positions _a_<sup>_t_</sup> _r_<sup>andthecurrentjointpositions</sup> of both hand and arm _j_<sup>_t_</sup> as inputs, and outputs the next joint positions _j_<sup>_∗t_+1</sup> = _I_ ( _a_<sup>_t_</sup> _r_<sup>_, jt_)neededtoreachthetarget.</sup> 

Using the calibration and IK procedures outlined above, our robot arm-hand system can follow a fingertip trajectory directly from an in-scene human video. We showcase the human demonstrations used in Fig. 3. 

## _B. Residual Policy Learning_ 

Due to the morphological differences between the human and robot, as well as errors in VR hand pose estimation, naively replaying the retargeted fingertip trajectories on the robot mostly does not successfully solve the task, even when the object is in the same location. To alleviate this problem, we learn an online residual policy using reinforcement learning (RL) to augment the trajectory replay. Traditional RL algorithms for real-world robots rely on reward functions derived from straightforward methods such as image-based matching rewards [42, 30, 29] using in-domain demonstration data. However, due to the significant difference in the visual appearance of human and robot hands, these methods 



<!-- Start of picture text -->
Card Sliding Bread Picking<br>Paper Sliding<br>Music Box Opening<br><!-- End of picture text -->

Fig. 3: An illustration of the human demonstrations (top rows) and the corresponding robot policies (bottom rows) trained using HUDOR. Our method does not require teleoperated robot data and learns to imitate human demonstrations through online interactions. Note the differences in hand motions between the learned robot policy and the human videos, reflecting the morphological differences. 



<!-- Start of picture text -->
Music Box Opening Card Sliding<br>Paper Sliding Bread Picking<br><!-- End of picture text -->

Fig. 4: An illustration showing how masked objects appear in both the robot and human videos. Points on the objects represent tracking in each video. Occlusions are indicated by hollow points rather than solid ones. 

do not provide effective reward signals. To get around this domain gap, we propose a novel algorithm for object-centric trajectory-matching rewards. 

_a) Object Point Tracking and Trajectory Matching:_ Our reward computation involves using off-the-shelf computer vision models to track the motion of points on the object of interest. We compute the mean squared error between the 2D trajectories of these points in the human expert video and the robot policy rollout and use this as a reward at every timestep in our online learning framework. In this section, we explain our reward calculation in detail. 

- = 

- _• Object State Extraction_ : Given a trajectory _τ_ [ _o_<sup>1</sup> _, . . . , o_<sup>_T_</sup> ], where _T_ is the length of the trajectory and _o_<sup>_t_</sup> is an RGB image at time _t_ , we use the first frame _o_<sup>1</sup> as input to a language-grounded Segment-Anything Model [43, 44] – langSAM. langSAM uses a text prompt and GroundingDINO [45] to extract bounding boxes for the object, which are then input to the SAM 

   - [44] to generate a mask. The output of langSAM corresponding to _o_<sup>1</sup> is a segmentation mask for the initial object position, _P_<sup>1</sup> _∈_ R<sup>_N×_2</sup> , which is represented as a set of _N_ detected points on the object, where _N_ is a hyperparameter. The parameter _N_ determines the density of object tracking and is adjusted based on the object’s size in the camera view. 

- _Point Tracking_ : The mask _P_<sup>1</sup> is used to initialize the transformer-based point tracking algorithm Co-Tracker [46]. Given a trajectory of RGB images, _τ_ , and the firstframe segmentation mask, _P_<sup>1</sup> , Co-Tracker tracks points _p_<sup>_t_</sup> _i_<sup>=(</sup><sup>_xt_</sup> _i_<sup>_, y_</sup> _i_<sup>_t_)intheimagethroughoutthetrajectory</sup> _τ_ for all _t ∈{_ 1 _. . . T }_ , where _P_<sup>1</sup> = [ _p_ 1<sup>1</sup><sup>_, . . . p_1</sup> _N_<sup>].We</sup> use _τ_<sup>_p_</sup> = [ _P_<sup>1</sup> _, . . . P_<sup>_T_</sup> ] to denote the point trajectory consisting of the sets of tracked points. We illustrate what the tracking of the objects looks like for both human and robot trajectories in Fig. 4. 

- _Matching the Trajectories_ : First, we define two additional quantities: centroid of the detected points, _P_<sup>ˆ</sup><sup>_t_</sup> and mean translation, _δtrans_<sup>_t_attime</sup><sup>_t_.</sup><sup>_δ_</sup> _trans_<sup>_t_isdefinedas</sup> the mean displacement of all points in _P_<sup>_t_</sup> from _P_<sup>1</sup> . Concretely, 



We define the _object motion_ at time _t_ as _T_<sup>_t_</sup> = _δtrans_<sup>_t_.</sup> Given two separate object motions at time _t_ , one corresponding to the robot _TR_<sup>_t_andonecorrespondingtothe</sup> human _TH_<sup>_t_,therewardiscalculatedbycomputingthe</sup> negative root mean squared error between them: 



_b) Exploration Strategy:_ We select a subset of action dimensions to explore and learn from. For example, we focus only on the X and Y axes of the thumb for the Card 



<!-- Start of picture text -->
8/10<br>7/10<br>6/10<br>17cm<br>Bread Picking<br>Card Sliding<br>Opening<br>Music Box<br>Paper Sliding<br><!-- End of picture text -->

Fig. 5: Rollouts of trained policies from HUDOR on four tasks are shown. For all tasks, validation is performed at various locations within the illustrated areas in the leftmost frames, while training is conducted using a single human video where the initial object configuration is in the middle of these areas. Success for each task is shown in the rightmost frames. Videos are best viewed on our website: https://object-rewards.github.io/. 

Sliding task, rather than exploring all axes of all fingers. This approach speeds up the learning process and enables quick adaptation. Exploration axes for all tasks are mentioned in Section IV-A. For the exploration strategy, we use a scheduled additive Ornstein-Uhlenbeck (OU) noise [47, 48] to ensure smooth robot actions. 

After extracting a meaningful reward function and identifying a relevant subset of the action space, we learn a residual policy _πr_ ( _·_ ) on this subset by maximizing the reward function in Eq. 5 for each episode using DrQv2 [49]. 

Inputs to the residual policy _a_<sup>_t_</sup> +<sup>=</sup><sup>_πr_()attime</sup><sup>_t_are(a)</sup> the human retargeted fingertip positions with respect to the robot’s base _a_<sup>_t_</sup> _r_<sup>, (b) change in current robot fingertip positions</sup> ∆ _s_<sup>_t_</sup> = _s_<sup>_t_</sup> _− s_<sup>_t−_1</sup> , (c) the centroid of the tracked points set on the robot trajectory _P_<sup>ˆ</sup> _R_<sup>_t_and(d)theobjectmotionattime</sup> _t_ , _TR_<sup>_t_.Finally,wecomputetheexecutedactionsasfollows:</sup> 





The action, _a_<sup>_t_</sup> , is sent to the IK module which converts it into joint commands for the robot. The policy is improved over time using DrQv2 as the robot accumulates experience interacting with the object. 

## IV. EXPERIMENTAL EVALUATION 

We evaluate our method against 6 different baselines and run multiple ablations to answer the following questions: 

- 1) How much do online corrections improve the performance of HUDOR? 

- 2) Does object-centric reward function in HUDOR improve over common reward functions? 

- 3) How well does HUDOR generalize to new objects and larger locations? 

## _A. Task Descriptions_ 

We experiment with four dexterous tasks, which are visualized in Fig. 5. Exploration axes mentioned are with respect to the base of the robot. 

_a)_ **_Bread Picking_** _:_ The robot must locate an orangecolored piece of bread, pick it up, and hold it steadily for a sustained period. During validation, the bread is positioned and oriented within a 15cm _×_ 10cm space. We explore the X axes of all fingers for this task. The text prompt used to retrieve the mask is _orange bread_ . 

_b)_ **_Card Sliding_** _:_ The robot must locate and slide a thin card with its thumb and pick it up by supporting it with the rest of its fingers. During validation, the card is positioned and oriented within a 10cm _×_ 10cm space. The text prompt used to retrieve the object mask is _orange card_ . We explore only the X and Y axes of the thumb. 

_c)_ **_Music Box Opening_** _:_ The robot must locate and open a small music box. It uses its thumb to stabilize the box while unlatching the top with its index finger. During validation, the box is positioned and oriented within a 10cm × 10cm space. We explore all axes of the thumb and index fingers, and the text prompt used is _green music box_ . 

For this task, since the rotation of the object was significant, for each time _t_ , we calculated the mean rotation vector about the centroid of all the points in _P_<sup>_t_</sup> from _P_<sup>1</sup> , <u>1</u> _δrot_<sup>_t_=</sup> _N_ � _Ni_ =1 _p_<sup>_t_</sup> _× p_<sup>1</sup> , in addition to �� _i_<sup>_−P_ˆ</sup><sup>_t_�</sup> � _i_<sup>_−P_ˆ 1��</sup> the mean translation, _δtrans_<sup>_t_.Thefinalobjectmotionis</sup> then calculated as _T_<sup>_t_</sup> = [ _δtrans_<sup>_t, δ_</sup> _rot_<sup>_t_]andusedinEq.5.</sup> Additionally, we observed that a sparse reward was better for this task, so we only used the last 5 frames of the trajectory for reward calculation for HUDOR and all of our baselines. 

_d)_ **_Paper Sliding_** _:_ The robot must slide a given piece of paper to the right. During validation, the paper is positioned and oriented within a 15cm _×_ 15cm space. The text prompt used to retrieve the mask is _blue paper with pizza patterns_ . 



<!-- Start of picture text -->
Human<br>Trajectory<br>Trajectory Visualizations<br>Robot Traj.  Robot Traj.<br>(Episode 42) (Episode 1)<br>Episode Timesteps Episode Timesteps<br>Rewards<br>Trajectories<br>X Axes of Object<br><!-- End of picture text -->

Fig. 6: Illustration of how online correction improves robot policy and moves the robot trajectory closer to the expert’s as time progresses in the Paper Sliding task. At the top, we visualize the trajectories of the paper in different episodes and the human video. At the bottom, we showcase the X-axis of the trajectory of the tracked points on the paper for different episodes and their corresponding rewards. The color of the episodes gradually changes from red in Episode 1 to green in Episode 42. 

Higher rewards are given as the paper moves further to the right. Success in this task is measured by the distance the paper moves to the right, expressed in centimeters. We explore on X and Z axes of all the fingers. 

_Evaluating robot performance_ : To compare the robot’s performance, we evaluate HUDOR against various online and offline algorithms. For all online algorithms, we train the policies until the reward converges, up to one hour of online interactions. We evaluate the methods by running rollouts on 10 varying initial object configurations for every task. 

## _B. How important are online corrections?_ 

Fig. 6 demonstrates how online learning improves the policy in the Paper Sliding task. As can be seen, HUDOR enables the robot policy trajectory to move progressively closer to that of the human expert. To showcase the importance of online corrections, we implement and run the state-ofthe-art transformer-based behavior cloning (BC) algorithm VQ-BeT [3], as the base architecture for all of our offline baselines. Similar to the residual policy, the centroid of the tracked points set _P_<sup>ˆ</sup><sup>_t_</sup> , the rotation and translation of the object _TR_<sup>_t_,andtherobot’sfingertippositions</sup><sup>_st_aregiven</sup> as inputs to each BC baseline. We ablate the input and the amount of demonstrations used to experiment on different aspects, and compare HUDOR against the following offline baselines: 



<!-- Start of picture text -->
Success & Failure Modes of Offline Algorithms<br>Success<br>Failure<br><!-- End of picture text -->

Fig. 7: Illustration of failure modes in the Point Cloud BC algorithm. Red borders indicate frames, where the data goes out of distribution (OOD) and the algorithm, fails to recover. Note how, in the Bread Picking and Paper Sliding tasks, the hand progressively lowers, while in the Card Sliding task, once the card is slid to the edge, the algorithm fails to recover. In contrast, HUDOR combines an open-loop base policy with a learned residual policy, providing more robust behavior against OOD cases. 

- 1) **BC - 1 Demo** [3]: HUDOR enables training robust policies with only a single human demonstration. For fairness, we compare its offline counterpart and train VQ-BeT end-to-end using only a single demonstration per task. 

- 2) **BC** [3]: We run VQ-BeT similar to the previous baseline, but we use 30 demonstrations for each task. 

- 3) **Point Cloud BC** : Similar to DexCap [17], we include point cloud in our input space and modify the input of the BC algorithm by concatenating the point cloud representations received from PointNet [50] encoder. We uniformly sample 5000 points from the point cloud and pass them to PointNet without any further preprocessing. Gradients are backpropagated through the entire system, including the point cloud encoder. 

TABLE I: Comparison of HUDOR to different offline algorithms. Paper sliding success is measured in cm of rightward motion; other tasks show success rates out of 10 robot rollouts. 

|Method|Bread|Card|Music|Paper|
|---|---|---|---|---|
||(./10)|(./10)|(./10)|(cm)|
|BC - 1 Demo [3]|0|0|0|3.5 _±_ 1.1<br>|
|BC [3]|3|0|0|4.1 _±_ 1.3|
|Point Cloud BC [17]|3|0|0|12 _±_ 1.3|
|HUDOR (ours)|**8**|**7**|**6**|**17.3** _±_ **1.5**|





<!-- Start of picture text -->
Bread Picking Card Sliding<br>5/10 5/10 5/10 2/10<br>4/10 0/10 4/10 2/10<br>Dobby<br>Brown Tissue<br>Brown Music Box Green Gum Pack<br>Red Peg<br>Small Plate<br>Medicine Bottle Yellow Tea Bag<br><!-- End of picture text -->

Fig. 8: Generalization experiments on the Bread Picking and Card Sliding tasks. We use the text prompts shown on the left side of each image as input to the language-grounded SAM model to generate the initial mask for each object. 

Table I shows the comparison results. As expected, the BC-1 Demo baseline quickly overfits and fails across all tasks. The BC baseline performs relatively well on the Bread Picking task, where precision is less critical. However, on tasks like Card Sliding and Music Box Opening, which require more dexterity, it also overfits quickly—reaching the objects but failing to maintain the necessary consistency. Both BC baselines manage to reach the paper but do little beyond that for Paper Sliding. Our strongest baseline, Point Cloud BC, performs relatively well on Paper Sliding and Bread Picking. We observed that with this baseline, when the robot hand occupies too much of the scene, the data goes out of distribution, causing the model to fail. It moves the paper to the middle but doesn’t move it further, grasps the bread but fails to lift it, and reaches for the card but fails to consistently slide it with the thumb. We showcase the failure modes of our most successful offline baseline Point Cloud BC algorithm in Fig. 7 for three of our tasks. Videos of these failure cases can be seen on our project website. 

These results indicate that the dexterous skills learned using this human data collected with HUDOR can scale better with more data for some tasks. However, for highly precise tasks such as Music Box Opening and Card Sliding, all offline methods fail, highlighting the importance of online corrections for tasks requiring high dexterity. 

## _C. Does_ HUDOR _improve over other reward functions?_ 

In HUDOR to compensate for the visual differences between the human and robot videos, we use object-oriented point tracking-based reward functions to guide the learning. We ablate over our design decision, and train online policies for our tasks with the following reward functions: 

- 1) **Image OT** [30]: We pass RGB images from both the robot and the human videos through pretrained Resnet18 [51] image encoders to get image representations and apply optimal transport (OT) based matching on them to get the reward, similar to FISH [30]. 

- 2) **Point OT** : Instead of direct images we apply OT matching on the points that are tracked throughout both the trajectories of tracked sets of points _τr_<sup>_p_and</sup><sup>_τ p_</sup> _h_<sup>.</sup> 

TABLE II: Comparison of success of HUDOR to different reward extraction algorithms. Success is shown as similar to Table I 

|Method|HUDOR(ours)|Image OT [30]|Point OT|
|---|---|---|---|
|Bread Picking|**8**|6|6|
|Music Box Opening|**6**|1|2|
|Paper Sliding (cm)|**17.25** _±_ **1.47**|16.1 _±_ 1.37|16.5 _±_ 1.23|



We present the success rates in Table II. We observe that in tasks where the object occupies a large area in the image and the visual differences between the hand and the robot do not significantly affect the image, the Image OT baseline performs similarly to HUDOR, as seen in the Paper Sliding task. However, in tasks where the camera needs to be closer to the object to detect its trajectory—such as Music Box Opening—the visual differences between the hand and the robot significantly hinder training, causing image-based reward calculations to fail. On the other hand, direct matching on the predicted points fails because the points tracked for two separate trajectories do not correspond to each other; the same indexed point in one trajectory may correspond to a different location on the object in another trajectory. These differences cause matching to give inconsistent rewards emphasizing the importance of matching _trajectories_ rather than points or images. 

## _D. How well does_ HUDOR _generalize to new objects?_ 

We test the generalization capabilities of policies trained with HUDOR on new objects for two tasks, with the results shown in Fig. 8. In these experiments, we apply the policies directly to new objects without retraining, using different text prompts for each inference to obtain object segmentation. We observe that HUDOR can generalize with varying success to new objects, provided their shape and texture do not differ significantly from the original. In the Card Sliding task, factors like weight and thickness affect success; for instance, lightweight objects, such as the Yellow Tea Bag, may not fall onto the supporting fingers after sliding, while thin objects, like the Brown Tissue, cannot be slid properly by the thumb. In Bread Picking, HUDOR performs well with the Dobby 



<!-- Start of picture text -->
Music Box Opening Bread Picking<br>HRC<br>oc Original object position Reached the lid / semi opened it Original object position Picked the bread but dropped it<br>Reached the box but not the lid Success Couldn’t pick up the bread Success<br>(a) Decoupling (b) Spatial Generalization Results<br><!-- End of picture text -->

Fig. 9: Illustration of how we conduct spatial generalization experiments and their results. First, (a) we decouple the hand and arm generalization by identifying the object location with respect to the robot base and using this location to extract a larger offset to be added to the trained policies with HUDOR. Next, (b) we present spatial generalization experiments for the _Bread Picking_ and _Music Box Opening_ tasks. We illustrate the evaluation locations and report their success below. Note that while policies learned with HUDOR generalize successfully in the majority of locations for Bread Picking, they fail to perform similarly in the more dexterous task, Music Box Opening. Videos of evaluation runs can be found on our website. 

sculpture, despite its different shape from the bread, but fails with slippery objects, like the Red Peg. 

These experiments demonstrate that while point-tracking can enable some degree of policy generalization, it is insufficient to overcome substantial differences in shape and texture. 

## _E. How effectively does_ HUDOR _generalize to larger areas?_ 

We evaluated how well policies trained with HUDOR generalize spatially to larger areas. Here, we did not train any new policies from scratch for broader spatial generalization due to the extensive online training time required. Instead, we decouple the spatial generalization component from policy learning as follows: we first calculate the object’s location in pixel space from the camera using a similar object detection pipeline as described in Section III-B. Then, combined with the depth image, we reproject this to a 3D translation relative to the camera, _oc_ . We transform this translation to the robot’s base frame by _or_ = _HRC_<sup>_−_1</sup><sup>_oc_where</sup><sup>_HRC_is the homogeneous</sup> transform from the robot’s base to the camera frame as shown in Fig. 9. Next, we calculate the offset of this location from the original object location in the demonstration _o_ ˆ _r_ , as _or − o_ ˆ _r_ . Finally, at inference time, we load the weights for each task trained with HUDOR and apply this offset to all the fingers. 

We present the results in both Fig. 9 and Table III. While this approach enables fairly effective spatial generalization for the bread-picking task, it fails to generalize for music box opening due to the dexterity and sensitivity required. We observe a trend where the fingers move too high, missing the lid on the leftmost edges of the evaluation area, and too low, lifting the box instead of opening the lid on the rightmost edges. We believe this issue arises both from residual policy predictions and noise in the depth received from the camera. 

## V. LIMITATIONS AND DISCUSSION 

In this paper, we introduced HUDOR, a point-tracking, object-oriented reward mechanism designed to close the 

TABLE III: The success of spatial generalization. The first column lists the total evaluations for each task, the second describes the behavior, and the third shows successful completions for the given behavior. Note that behaviors are sequential; for example, stabilizing the music box lid can only follow opening it. 

|**Task**|**Behavior**|**Successful**<br>**Evaluations**|
|---|---|---|
|Bread Picking (./20)|Reached the bread<br>Picked the bread up<br>Held it firmly|20<br>17<br>15|
||Reached the music box|18|
|Music Box Opening|Reached the lid|14|
|(./18)|Opened the lid|10|
||Stabilized the lid|7|



gap in human-to-robot policy transfer for dexterous hands. HUDOR improves upon both offline methods and online counterparts with different reward functions. We also demonstrate HUDOR’s generalization to new objects and locations. 

Despite its strengths, we identify three limitations. First, our framework only works with in-scene human videos. We believe integrating in-the-wild data collection would significantly enhance its generalization potential. Second, the exploration mechanism requires prior knowledge of which subset of action dimensions is suitable for exploration. Finally, there is no retry mechanism during an episode; when the robot makes a mistake, it can only retry in the next episode. This makes training for long-term tasks challenging. Incorporating a multi-stage learning framework could address this issue. These represent interesting opportunities for future improvements to HUDOR. 

## ACKNOWLEDGEMENTS 

We thank Siddhant Haldar, Mara Levy, Jeff Cui, Gaoyue Zhou, Aadhithya Iyer and Venkatesh Pattabiraman for valuable feedback and discussions. This work is supported by grants from Honda, Hyundai, NSF award 2339096 and ONR awards N00014-21-1-2758 and N00014-22-1-2773. LP is supported by the Packard Fellowship. 

REFERENCES 

- [1] V. Kumar, E. Todorov, and S. Levine, “Optimal control with learned local models: Application to dexterous manipulation,” _2016 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 378–383, 2016. 

- [2] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning FineGrained Bimanual Manipulation with Low-Cost Hardware,” _arXiv e-prints arXiv:2304.13705_ , Apr. 2023. 

- [3] S. Lee, Y. Wang, H. Etukuru, H. J. Kim, N. M. Mahi Shafiullah, and L. Pinto, “Behavior Generation with Latent Actions,” _arXiv e-prints arXiv:2403.03181_ , Mar. 2024. 

- [4] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song, “Diffusion policy: Visuomotor policy learning via action diffusion,” _The International Journal of Robotics Research_ , 2024. 

- [5] Z. J. Cui, Y. Wang, N. M. M. Shafiullah, and L. Pinto, “From play to policy: Conditional behavior generation from uncurated robot data,” _arXiv preprint arXiv:2210.10047_ , 2022. 

- [6] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, _et al._ , “RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control,” _arXiv e-prints arXiv:2307.15818_ , p. arXiv:2307.15818, July 2023. 

- [7] Open X-Embodiment Collaboration, A. O’Neill, A. Rehman, A. Gupta, A. Maddukuri, A. Gupta, A. Padalkar, A. Lee, _et al._ , “Open X-Embodiment: Robotic Learning Datasets and RT-X Models,” _arXiv e-prints arXiv:2310.08864_ , Oct. 2023. 

- [8] H. Etukuru, N. Naka, Z. Hu, S. Lee, J. Mehu, A. Edsinger, C. Paxton, S. Chintala, L. Pinto, and N. M. Mahi Shafiullah, “Robot Utility Models: General Policies for ZeroShot Deployment in New Environments,” _arXiv e-prints arXiv:2409.05865_ , Sept. 2024. 

- [9] S. Haldar, Z. Peng, and L. Pinto, “Baku: An efficient transformer for multi-task policy learning,” _arXiv preprint arXiv:2406.07539_ , 2024. 

- [10] S. Pandian Arunachalam, I. G¨uzey, S. Chintala, and L. Pinto, “Holo-Dex: Teaching Dexterity with Immersive Mixed Reality,” _arXiv e-prints arXiv:2210.06463_ , Oct. 2022. 

- [11] A. Iyer, Z. Peng, Y. Dai, I. Guzey, S. Haldar, S. Chintala, and L. Pinto, “OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation,” _arXiv e-prints arXiv:2403.07870_ , Mar. 2024. 

- [12] R. Ding, Y. Qin, J. Zhu, C. Jia, S. Yang, R. Yang, X. Qi, and X. Wang, “Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning,” _arXiv e-prints arXiv:2407.03162_ , July 2024. 

- [13] S. Kumar, J. Zamora, N. Hansen, R. Jangir, and X. Wang, “Graph inverse reinforcement learning from diverse videos,” _arXiv preprint arXiv:2207.14299_ , 2022. 

- [14] L. Smith, N. Dhawan, M. Zhang, P. Abbeel, and S. Levine, “AVID: Learning Multi-Stage Tasks via Pixel-Level Translation of Human Videos,” _arXiv e-prints arXiv:1912.04443_ , Dec. 2019. 

- [15] C. Eze and C. Crick, “Learning by Watching: A Review of Video-based Learning Approaches for Robot Manipulation,” _arXiv e-prints arXiv:2402.07127_ , Feb. 2024. 

- [16] C. Wang, L. Fan, J. Sun, R. Zhang, L. Fei-Fei, D. Xu, Y. Zhu, and A. Anandkumar, “MimicPlay: Long-Horizon Imitation Learning by Watching Human Play,” _arXiv e-prints arXiv:2302.12422_ , Feb. 2023. 

- [17] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu, “DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation,” _arXiv e- prints arXiv:2403.07788_ , Mar. 2024. 

- [18] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam, Y. Narang, J.-F. Lafleche, D. Fox, and 

G. State, “DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality,” _arXiv e-prints arXiv:2210.13702_ , Oct. 2022. 

- [19] OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, J. Schneider, N. Tezak, J. Tworek, P. Welinder, L. Weng, Q. Yuan, W. Zaremba, and L. Zhang, “Solving Rubik’s Cube with a Robot Hand,” _arXiv e-prints arXiv:1910.07113_ , Oct. 2019. 

- [20] K. Shaw, A. Agarwal, and D. Pathak, “LEAP Hand: LowCost, Efficient, and Anthropomorphic Hand for Robot Learning,” _arXiv e-prints arXiv:2309.06440_ , Sept. 2023. 

- [21] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang, “Rotating without Seeing: Towards In-hand Dexterity through Touch,” _arXiv e-prints arXiv:2303.10880_ , Mar. 2023. 

- [22] Y. J. Ma, W. Liang, G. Wang, D.-A. Huang, O. Bastani, D. Jayaraman, Y. Zhu, L. Fan, and A. Anandkumar, “Eureka: Human-Level Reward Design via Coding Large Language Models,” _arXiv e-prints arXiv:2310.12931_ , Oct. 2023. 

- [23] S. P. Arunachalam, I. G¨uzey, S. Chintala, and L. Pinto, “Holodex: Teaching dexterity with immersive mixed reality,” _arXiv preprint arXiv:2210.06463_ , 2022. 

- [24] S. Yang, M. Liu, Y. Qin, R. Ding, J. Li, X. Cheng, R. Yang, S. Yi, and X. Wang, “ACE: A Cross-Platform VisualExoskeletons System for Low-Cost Dexterous Teleoperation,” _arXiv e-prints arXiv:2408.11805_ , Aug. 2024. 

- [25] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox, “Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system,” in _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , 2020, pp. 9164–9170. 

- [26] I. Guzey, B. Evans, S. Chintala, and L. Pinto, “Dexterity from touch: Self-supervised pre-training of tactile representations with robotic play,” 2023. 

- [27] S. Haldar, V. Mathur, D. Yarats, and L. Pinto, “Watch and match: Supercharging imitation with regularized optimal transport,” _arXiv preprint arXiv:2206.15469_ , 2022. 

- [28] J. Pari, N. M. Shafiullah, S. P. Arunachalam, and L. Pinto, “The surprising effectiveness of representation learning for visual imitation,” 2021. 

- [29] I. Guzey, Y. Dai, B. Evans, S. Chintala, and L. Pinto, “See to Touch: Learning Tactile Dexterity through Visual Incentives,” _arXiv e-prints arXiv:2309.12300_ , Sept. 2023. 

- [30] S. Haldar, J. Pari, A. Rai, and L. Pinto, “Teach a Robot to FISH: Versatile Imitation from One Minute of Demonstrations,” _arXiv e-prints arXiv:2303.01497_ , Mar. 2023. 

- [31] J. Liang, R. Liu, E. Ozguroglu, S. Sudhakar, A. Dave, P. Tokmakov, S. Song, and C. Vondrick, “Dreamitate: Real-World Visuomotor Policy Learning via Video Generation,” _arXiv e- prints arXiv:2406.16862_ , June 2024. 

- [32] M. Yang, Y. Du, K. Ghasemipour, J. Tompson, D. Schuurmans, and P. Abbeel, “Learning interactive real-world simulators,” _arXiv preprint arXiv:2310.06114_ , 2023. 

- [33] K. Pertsch, R. Desai, V. Kumar, F. Meier, J. J. Lim, D. Batra, and A. Rai, “Cross-Domain Transfer via Semantic Skill Imitation,” _arXiv e-prints arXiv:2212.07407_ , Dec. 2022. 

- [34] K. Grauman, A. Westbury, L. Torresani, K. Kitani, J. Malik, T. Afouras, K. Ashutosh, V. Baiyya, _et al._ , “Ego-Exo4D: Understanding Skilled Human Activity from First- and ThirdPerson Perspectives,” _arXiv e-prints arXiv:2311.18259_ , Nov. 2023. 

- [35] J. Urain, A. Mandlekar, Y. Du, M. Shafiullah, D. Xu, K. Fragkiadaki, G. Chalvatzaki, and J. Peters, “Deep Generative Models in Robotics: A Survey on Learning from Multimodal Demonstrations,” _arXiv e-prints_ , p. arXiv:2408.04380, Aug. 2024. 

- [36] S. Bahl, R. Mendonca, L. Chen, U. Jain, and D. Pathak, “Affordances from Human Videos as a Versatile Representation 

   - for Robotics,” _arXiv e-prints arXiv:2304.08488_ , Apr. 2023. 

- [37] S. Chen, C. Wang, K. Nguyen, L. Fei-Fei, and C. K. Liu, “Arcap: Collecting high-quality human demonstrations for robot learning with augmented reality feedback,” _arXiv preprint arXiv:2410.08464_ , 2024. 

- [38] J. Li, Y. Zhu, Y. Xie, Z. Jiang, M. Seo, G. Pavlakos, and Y. Zhu, “Okami: Teaching humanoid robots manipulation skills through single video imitation,” _arXiv preprint arXiv:2410.11792_ , 2024. 

- [39] L. Keselman, J. Iselin Woodfill, A. Grunnet-Jepsen, and A. Bhowmik, “Intel RealSense Stereoscopic Depth Cameras,” _arXiv e-prints arXiv:1705.05548_ , May 2017. 

- [40] R. Hartley and A. Zisserman, _Multiple View Geometry in Computer Vision_ . Academic Press, 2002. 

- [41] T. Yenamandra, F. Bernard, J. Wang, F. Mueller, and C. Theobalt, “Convex Optimisation for Inverse Kinematics,” _arXiv e-prints arXiv:1910.11016_ , Oct. 2019. 

- [42] S. Haldar, V. Mathur, D. Yarats, and L. Pinto, “Watch and match: Supercharging imitation with regularized optimal transport,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 32–43. 

- [43] L. Medeiros _et al._ , “Lang-segment-anything,” https://github. com/luca-medeiros/lang-segment-anything, 2023, accessed: 2024-09-15. 

- [44] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo, P. Doll´ar, and R. Girshick, “Segment Anything,” _arXiv e-prints arXiv:2304.02643_ , Apr. 2023. 

- [45] M. Caron, H. Touvron, I. Misra, H. J´egou, J. Mairal, P. Bojanowski, and A. Joulin, “Emerging Properties in Self-Supervised Vision Transformers,” _arXiv e-prints arXiv:2104.14294_ , Apr. 2021. 

- [46] N. Karaev, I. Rocco, B. Graham, N. Neverova, A. Vedaldi, and C. Rupprecht, “Cotracker: It is better to track together,” _arXiv preprint arXiv:2307.07635_ , 2023. 

- [47] G. E. Uhlenbeck and L. S. Ornstein, “On the theory of the brownian motion,” _Phys. Rev._ , vol. 36, pp. 823–841, Sep 1930. [Online]. Available: https://link.aps.org/doi/10.1103/ PhysRev.36.823 

- [48] T. Lillicrap, “Continuous control with deep reinforcement learning,” _arXiv preprint arXiv:1509.02971_ , 2015. 

- [49] D. Yarats, R. Fergus, A. Lazaric, and L. Pinto, “Mastering visual continuous control: Improved data-augmented reinforcement learning,” _arXiv preprint arXiv:2107.09645_ , 2021. 

- [50] C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “Pointnet: Deep learning on point sets for 3d classification and segmentation,” in _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 2017, pp. 652–660. 

- [51] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 2016, pp. 770– 778. 

