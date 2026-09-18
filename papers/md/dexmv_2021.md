# **DexMV: Imitation Learning for Dexterous Manipulation from Human Videos** 

Yuzhe Qin<sup>_∗_</sup> , Yueh-Hua Wu<sup>_∗_</sup> , Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang 

University of California San Diego, La Jolla 92093, USA 



<!-- Start of picture text -->
Relocate Pour Place Inside<br>Human  Video<br>Pose<br>Estimation<br>Task<br>Manipulation<br><!-- End of picture text -->

Fig. 1: We record human videos on manipulation tasks (1st row) and perform 3D hand-object pose estimations from the videos (2nd row) to construct the demonstrations. We have a paired simulation system providing the same dexterous manipulation tasks for the multi-finger robot (3rd row), including _relocate_ , _pour_ , and _place inside_ , which we can solve using imitation learning with the inferred demonstrations. 

**Abstract.** While significant progress has been made on understanding hand-object interactions in computer vision, it is still very challenging for robots to perform complex dexterous manipulation. In this paper, we propose a new platform and pipeline DexMV ( **Dex** terous **M** anipulation from **V** ideos) for imitation learning. We design a platform with: (i) a simulation system for complex dexterous manipulation tasks with a multifinger robot hand and (ii) a computer vision system to record large-scale demonstrations of a human hand conducting the same tasks. In our novel pipeline, we extract 3D hand and object poses from videos, and propose a novel demonstration translation method to convert human motion to robot demonstrations. We then apply and benchmark multiple imitation learning algorithms with the demonstrations. We show that the demonstrations can indeed improve robot learning by a large margin and solve the complex tasks which reinforcement learning alone cannot solve. More details can be found in the project page. 

**Keywords:** Dexterous Manipulation; Learning from Human Demonstration; Reinforcement Learning 

* Equal Contribution 

2 Y. Qin et al. 

## **1 Introduction** 

Dexterous manipulation of objects is the primary means for humans to interact with the physical world. Humans perform dexterous manipulation in everyday tasks with diverse objects. To understand these tasks, in computer vision, there is significant progress on 3D hand-object pose estimation [29,90] and affordance reasoning [13,83]. While computer vision techniques have greatly advanced, it is still very challenging to equip robots with human-like dexterity. Recently, there has been a lot of effort on using reinforcement learning (RL) for dexterous manipulation with an anthropomorphic robot hand [55]. However, given the high Degree-of-Freedom joints and nonlinear tendon-based actuation of the multi-finger robot hand, it requires a _large amount_ of training data with RL. Robot hands trained using only RL will also adopt _unnatural_ behavior. Given these challenges, can we leverage humans’ experience in the interaction with the physical world to guide robots, with the help of computer vision techniques? 

One promising avenue is imitation learning from human demonstrations [66,71]. Particularly, for dexterous manipulation, Rajeswaran _et al_ . [66] introduces a simulation environment with four different manipulation tasks and paired sets of human demonstrations collected with a Virtual Reality (VR) headset and a motion capture glove. However, data collection with VR is relatively high-cost and not scalable, and there are only 25 demonstrations collected for each task. It also limits the complexity of the task: It is shown in [64] that RL can achieve similar performance with or without the demonstrations in most tasks proposed in [66]. Instead of focusing on a small scale of data, we look into increasing the difficulty and complexity of the manipulation tasks with diverse daily objects. This requires large-scale human demonstrations which are hard to obtain with VR but are much more available from human videos. 

In this paper, we propose **a new platform and a novel imitation learning pipeline** for benchmarking complex and generalizable dexterous manipulation, namely DexMV ( **Dex** terous **M** anipulation from **V** ideos). We introduce new tasks with the multi-finger robot hand (Adroit Robotic Hand [43]) on diverse objects in simulation. We collect real human hand videos performing the same tasks as demonstrations. By using human videos instead of VR, it _largely reduces the cost_ for data collection and allows humans to perform more _complex and diverse_ tasks. While the video demonstrations might not be optimal for perfect imitation (e.g., behavior cloning) to learn successful policies, the diverse dataset is beneficial for augmenting the training data for RL, which can learn from both successful and unsuccessful trials. 

**Our DexMV platform** contains a paired systems with: (i) A computer vision system which records the videos of human performing manipulation tasks (1st row in Figure 1); (ii) A physical simulation system which provides the interactive environments for dexterous manipulation with a multi-finger robot (3rd row in Figure 1). The two systems are aligned with the same tasks. With this platform, our goal is to bridge 3D vision and robotic dexterous manipulation via a novel imitation learning pipeline. 

DexMV 3 

**Our DexMV pipeline** contains three stages. First, we extract the 3D handobject poses from the recorded videos (2nd row in Figure 1). Unlike previous imitation learning studies with 2-DoF grippers [92,81], we need the human video to guide the 30-DoF robot hand to move each finger in 3D space. Parsing the 3D structure provides critical and necessary information. Second, a **key contribution** in our pipeline is a novel demonstration translation method that connects the computer vision system and the simulation system. We propose an optimization-based approach to convert 3D human hand trajectories to robot hand demonstrations. Specifically, the innovations lie in 2 steps: (i) Hand motion retargeting approach to obtain robot hand states; and (ii) Robot action estimation to obtain the actions for learning. Third, given the robot demonstrations, we perform imitation learning in the simulation tasks. We investigate and benchmark algorithms which augment RL objectives with state-only [64] and state-action [32,66] demonstrations. 

We experiment with three types of challenging tasks with the YCB objects [15]. The first task is to _relocate_ an object to a goal position. Instead of relocating a single ball as [66], we increase the task difficulty by using diverse objects (first 5 columns in Figure 1). The second task is _pour_ , which requires the robot to pour the particles from a mug into a container (Figure 1 from column 6). The third task is _place inside_ , where the robot hand needs to place an object into a container (last 2 columns in Figure 1). In our experiments, we benchmark different imitation learning algorithms and show human demonstrations improve task performance by a large margin. More interestingly, we find the learned policy with our demonstrations can even generalize to unseen instances within the same category or outside the category. We highlight our contributions as follows: 

- DexMV platform for learning dexterous manipulation using human videos. It contains paired computer vision and simulation systems with multiple dexterous complex manipulation tasks. 

- DexMV pipeline to perform imitation learning, with a key innovation on demonstration translation to convert human videos to robot demonstrations. 

- With DexMV platform and pipeline, we largely improve the dexterous manipulation performance over multiple complex tasks, and its generalization ability to unseen object instances. 

## **2 Related Work** 

**Dexterous Manipulation.** Manipulation with multi-finger hands is one of the most challenging robotics tasks, which has been actively studied with optimization and planning [69,10,53,20,3,7]. Recently, researchers have started exploring reinforcement learning for dexterous manipulation [55,54]. However, training with only RL requires huge data samples. Different from a regular 2- DoF robot gripper, the Adroit Robotic Hand used in our experiment has 30 DoFs, which greatly increases the optimization space. 

**Imitation Learning from Human Demonstrations.** Imitation learning is a promising paradigm for robot learning. It is not limited to behavior 

4 Y. Qin et al. 

cloning [61,8,68,11,87] and inverse reinforcement learning [70,52,1,32,23,5,88,46], but also augmenting the RL training with demonstrations [60,21,89,66,64]. For example, Rajeswaran _et al_ . [66] propose to incorporate demonstrations with onpolicy RL. However, all these approaches rely on expert demonstrations collected using expert policies or VR, which is not scalable and generalizable to complex tasks. In fact, it is shown in [64] that RL can achieve similar performance and sample efficiency with or without the demonstrations in most dexterous manipulation tasks in [66] besides _relocate_ . Going beyond a VR setup, researchers have recently explored imitation learning and RL with videos [72,17,71,76,81,92]. However, all tasks are relatively simple (e.g., pushing a block) with a parallel gripper. In this paper, we propose new challenging dexterous manipulation tasks. We leverage pose estimation for providing demonstrations that largely improve imitation learning performance, while RL alone fails to solve these tasks. 

**Following Human Demonstrations.** Another line of work is to train policies to follow the expert demonstrations [48,59,56,77,79,24,91,74,78,80,58]. For example, Garcia-Hernando _et al_ . [24] propose to use RL to followed estimated human hand poses with a virtual robot hand. The robot can execute the same trajectory by following human videos. Instead of repeating one expert trajectory, we emphasize that DexMV is about learning a policy that generalized to different goals and object configurations. 

**Hand-Object Interaction.** Hand-object interaction is a widely studied topic. One line of work focus on object pose estimation [40,63,90,84,57,34,30] and hand pose estimation [93,35,82,26,6,12,29,42,47]. For example, Berk _et al_ . [15] propose YCB dataset with real objects and their 3D scans. Beyond object poses, datasets and methods for joint estimation of the hand-object poses are also proposed [25,27,47,18]. Another line of work focus on hand-object contact reasoning [13,83], which can be used for functional grasps [36,14,50]. Recently, researchers explored to use hand pose estimation to control a robot hand [28,4,45]. They require motion retargeting to map the hand pose into robot motion. These work focus on teleoperation where no objects are involved. In DexMV, we consider the demonstration translation setting, which converts a sequence of handobject poses into robot demonstrations. We show that the translated demonstration is beneficial for imitation learning for dexterous manipulation. 

## **3 Overview** 

We propose DexMV for **Dex** terous **M** anipulation with imitation learning from human **V** ideos including: 

**(i) DexMV platform** , which offers a paired computer vision system recording human manipulation videos and physical simulators conducting the same tasks. We design three challenging tasks in the simulator and use computer vision system to collect human demonstrations for these tasks in real world. The videos can be efficiently collected with around _100 demonstrations per hour_ . 

**(ii) DexMV pipeline** , a new pipeline for imitation learning from human videos. Given the recorded videos from the computer vision system, we perform pose estimation and motion retargeting to translate human video to robot hand 

DexMV 5 



<!-- Start of picture text -->
DexMV Platform DexMV Pipeline<br>Raw Video 3D Pose<br>... ... ...<br>... ... ...<br>RL Interaction Data Translated Demonstration<br>Train Test ...<br>RL<br>Algorithm<br>...<br>Translation<br>Computer Vision Demonstration<br>Simulation<br><!-- End of picture text -->

Fig. 2: **DexMV platform and pipeline overview.** Our platform is composed of a computer vision system (yellow), a simulation system (blue), and a demonstration translation module (colored with green). In computer vision system, we collect human manipulation videos. In simulation, we design the same tasks for the robot hand. We apply 3D hand-object pose estimation from videos, followed by demonstration translation to generate robot demonstrations, which are then used for imitation learning. 

demonstrations. These demonstrations are then used for policy learning where multiple imitation learning and RL algorithms are investigated. By learning from demonstrations, our policy can be deployed in environments with _different goals and object configurations_ , instead of just following one trajectory. We show that given the complex manipulation tasks, 3D pose estimation provides _necessary signals_ for imitation learning to learn natural policies. 

## **4 DexMV Platform** 

Our DexMV platform is shown in Figure 2. It is composed of a computer vision system and a simulation system. 

**Computer Vision System.** The computer vision system is used to collect human demonstration videos on manipulating diverse real objects. In this system, we build a cubic frame (35 inch<sup>3</sup> ) and attach two RealSense D435 cameras (RGBD cameras) on the top front and top left, as shown on the top row of Figure 2. During data collection, a human will perform manipulation tasks inside the frame, e.g., relocate sugar box. The manipulation videos will be recorded using the two cameras (from a front view and a side view). 

**Simulation System.** Our simulation system is built on MuJoCo [85] with the Adroit Hand [43]. We design multiple dexterous manipulation tasks aligned with human demonstrations. As shown in the bottom row of Figure 2, we perform imitation learning by augmenting the Reinforcement Learning with the collected demonstrations. Once the policy is trained, it can be tested on the same tasks with different goals and object configurations. 

**Task Description.** We propose 3 types of manipulation tasks with different objects. We select the YCB objects [15] with a reasonable size for human to manipulate. We collect 100 demonstrations per object for _relocate_ and 100 demonstrations for _pour_ and _place inside_ . For all tasks, the state is composed of 

6 Y. Qin et al. 

robot joint readings, object pose. For _relocate_ , we also include target position. The action is 30-d control command of the position actuator for each joint. 

_Relocate._ It requires the robot hand to pick up an object on the table to a target location. It is inspired by the hardest task in [66] where the robot hand needs to grasp a sphere and move it to the target position. We further increase the task difficulty by using 5 complex objects as shown in the table above and visualized in the first 5 columns of Figure 1. The transparent green shape represents the goal, which can change during training and testing (goal-conditioned). The task is successfully solved if the object reaches the goal, without the need for a specific orientation. We train one policy for relocating each object. 

_Pour._ It requires the robot hand to reach the mug and pour the particles inside into a container (Figure 1 column 6). The robot needs to grasp the mug and then manipulate it precisely. The evaluation criteria is based on the percentage of particles poured inside the container. 

_Place Inside._ It requires the robot to pick up an object (e.g., a banana) and place it into a container. The robot needs to rotate the object to a suitable orientation and approach the container carefully to avoid collisions. 

The evaluation is based on how much percentage of the object mesh volume is inside the container. 

Besides testing on the trained objects, we also evaluate the generalization ability of the trained policies on unseen object instances, within the training categories like can, bottle, mug, and also outside the training categories such as camera from ShapeNet dataset [16]. 

## **5 Pose Estimation** 

### **5.1 Object Pose Estimation** 

We use the 6-DoF pose to represent the location and orientation of objects, which contains translation _T ∈_ **R**<sup>3</sup> and rotation _R ∈_ **SO** ( **3** ). For each frame _t_ in the video, we use the PVN3D [30] model trained on the YCB dataset [15] to detect objects and estimate 6-DoF poses. By taking both the RGB image and the point clouds as inputs, the model first estimates the instance segmentation mask. With dense voting on the segmented point clouds, the model then predicts the 3D location of object key points. The 6-DoF object pose is optimized by minimizing the PnP matching error. 

### **5.2 Hand Pose Estimation** 

We utilize the MANO model [67] to represent the hand that consists of hand pose parameter _θt_ for 3D rotations of 15 joints and root global pose _rt_ , and shape parameters _βt_ for each frame _t_ . The 3D hand joints can be computed using hand kinematics function _jt_<sup>3</sup><sup>_d_</sup> = **J** ( _θt, βt, rt_ ). 

Given a video, we use the off-the-shelf skin segmentation [41] and hand detection [75] models to obtain a hand mask _Mt_ . We use the trained hand pose estimation models in [47] to predict the 2D hand joints _jt_<sup>2</sup><sup>_d_</sup> and the MANO parameters _θt_ and _βt_ for every frame _t_ using RGB image. We estimate the root 

DexMV 7 

joint _rt_ using the center of the depth image masked by _Mt_ . Given the initial estimation _θt, βt, rt_ of each frame _t_ and the camera pose _Π_ , we formulate the 3D hand joint estimation as an optimization problem, 



where _λ_ = 0 _._ 001 and **R** is a depth rendering function [39] and _Dt_ is the corresponding depth map in frame _t_ . We minimize the re-projection error in 2D and optimize the hand 3D locations from the depth map. Equation 1 can be further extended to a multi-camera setting by minimizing the objective from different cameras with calibrated extrinsics. We use two cameras by default to handle occlusion. Additionally, we deploy a post-processing procedure with minimizing the difference of _jt_<sup>3</sup><sup>_d_</sup> and _βt_ between frames. 

## **6 Demonstration Translation** 

Common imitation learning algorithm consumes state-action pairs from expert demonstrations. It requires the state of the robot and the action of the motor as training data but not directly using the human hand pose. As shown in the kinematics chains in the blue box of Figure 3, although both robot and human hands share a similar five-finger morphology, their kinematics chains are different. The human hand MANO model [67] is parameterized by 15 rotation vector, leading to 15 ball joint with 15 _∗_ 3 = 45 DoF. The Adroit Robotic Hand [43] used in simulation has 24 revolute joint and 1 free joint, which leads to 24+1 _∗_ 6 = 30 DoF. The finger length of each knuckle is also different. 

In this paper, we propose a novel method to translate demonstrations from _human-centric pose estimation_ result into _robot-centric imitation data_ . Specifically, there are two steps in demonstration translation (as shown in the red box of Figure 3): (i) **Hand motion retargeting** to align the human hand motion to robot hand motion, which are with different DoF and geometry; (ii) **Predicting robot action** , i.e. torque of robot motor: Without any wired sensors, we need to recover the action from only pose estimation results. We will introduce our approach for these two challenges as follows. 

### **6.1 Hand Motion Retargeting** 

In computer graphics and animation, motion retargeting is used to retarget a performer’s motion to a virtual character for applications such as movies and cartons [2,31]. While the animation community emphasizes realistic visual appearance, we consider more on the physical effect of the retargeted motion in the context of robotics manipulation. That is, the robot motion should be executable, respecting the physical limit of motors, e.g. acceleration and torque. 

Formally, given a sequence of human hand pose estimated _{_ ( _θt, βt, rt_ ) _}_<sup>_T_</sup> _t_ =0 from a video, the hand pose retargeting can be defined as computing the sequence of robot joint angles _{qt}_<sup>_T_</sup> _t_ =0<sup>,where</sup><sup>_t_isthestepnumberinasequenceoflength</sup> _T_ + 1. We formulate the hand pose retargeting as an optimization problem. 

Y. Qin et al. 

8 



<!-- Start of picture text -->
Kinematics Chains  Task Space Vectors<br>Demonstration Translation<br>Hand Motion  Robot Action<br>Retargeting Estimation<br>Human Hand Pose Robot Joint  Robot Motor<br>(from Vision) Angles Command<br>Human<br>Hand Pose<br>Retargeting FingerTip  Mapping<br>Retargeting Our Method<br><!-- End of picture text -->

Fig. 3: **Top row** : Kinematic Chains and Task Space Vectors (TSV). The TSV (dash arrows) are ten vectors to be matched between both hands. **Bottom row** : (i) Hand motion retargeting; (ii) Action Estimation. 

Fig. 4: Visualization of hand motion retargeting results. **Top row:** 3D hand-object poses. **Mid row:** Retargeting results using Finger Tip Mapping as optimization objective. **Bottom row:** Retargeting results using the proposed optimization objective. 

**Optimization with Task Space Vectors.** In most manipulation tasks, human and multi-finger robot hand contacts the object using finger tips. Thus in fingertip-based mapping [4,28], retargeting is solved by preserving the Task Space Vectors (TSV) defined from finger tips position to the hand palm position (green arrow) as shown in the green box of Figure 3, so that the human and robot hands will have same finger tip position relative to the palm. However, only considering finger tip may results in unexpected optimization result as shown in Figure 4. Although the tip position is preserved, the bending information of hand fingers are lost, leading to penetrating the object after retargeting. It becomes more severe when the joint angles are closed to the robot singularity [51]. To solve this issue, we include the TSV from palm to middle phalanx (blue arrow) as shown in the green box of Figure 3. The optimization objective is, 



where the forward kinematics function for human **vi**<sup>**H**(</sup><sup>_θ, β, r_)computesthe</sup> _i_ -th TSV for human hand and the robot forward kinematics function **vi**<sup>**R**(</sup><sup>_q_)</sup> computes _i_ -th TSV for the robot. The first term in Equation 2 is to find the best _{qt}_<sup>_T_</sup> _t_ =0<sup>thatmatchesthefingertip-palmTSVandfingertip-phalanxTSVfrom</sup> both hands. Note the human hand TSV _{vi_<sup>_H_(</sup><sup>_θ_0</sup><sup>_, β_0</sup><sup>_, r_0)</sup><sup>_}_</sup> _t_<sup>_T_</sup> =0<sup>isfirstprocessedby</sup> a low pass filter before optimization for better smoothness. We also add an L2 normalization (second term in Equation 2) to improve the temporal consistency. For optimization, we use Sequential Least-Squares Quadratic Programming in NLopt [37], where _α_ = 8 _e −_ 3 in implementation. 

When retargeting hand pose, the objective in Equation 2 is optimized for each _t_ from _t_ = 0 to _t_ = _T_ . For _t ≥_ 1, we initialize _qt_ using the optimization results _qt−_ 1 from last step to further improve the temporal smoothness. 

DexMV 9 

### **6.2 Robot Action Estimation** 

Hand motion retargeting provides temporal-consistent translation from human hand poses to robot joint angles _{qt}_<sup>_T_</sup> _t_ =0<sup>indifferenttimesteps.Butthe</sup> action, i.e. joint torque or control command, is unknown. In robotics, the joint torque _τ_ can be computed via robot inverse dynamics function _τ_ = _finv_ ( _q, q_<sup>_′_</sup> _, q_<sup>_′′_</sup> ). To use this function, we first fit the sequence of joint angles into a continuous joint trajectory function **q** ( _t_ ). Then, the first and second order derivative **q**<sup>_′_</sup> ( _t_ ) and **q**<sup>_′′_</sup> ( _t_ ) can be used to compute the torque _τ_ ( _t_ ) = _finv_ ( _q_ ( _t_ ) _, q_<sup>_′_</sup> ( _t_ ) _, q_<sup>_′′_</sup> ( _t_ )). 

**One important property of q** ( _t_ ) **is:** The absolute value of third-order derivative **q**<sup>_′′′_</sup> ( _t_ ), which also refers as jerk, should be as small as possible. We call it minimum-jerk requirement. The reason is two-fold: (i) First, physiological study [22] shows that the motion of human hand is a minimum jerk trajectory, where the lowest effort is required during the movement. This requirement will resemble the behavior of human, which in turn leads to more natural robot motion. (ii) Second, minimizing jerk can ensure low joint position errors for motors [44] and limit excessive wear on the physical robot [19]. Thus we also expect the fitted trajectory function _{qt}_<sup>_T_</sup> _t_ =0<sup>tobeminimum-jerk.Inimplementation,</sup> we use the model proposed in [86] to achieve this. 

**Time Alignment.** The recorded video is with around 30 _Hz_ frequency and the simulation runs at 120 _Hz_ . We need to align the demonstrations with the simulated environment before we apply for training. We sample the continuous function **q** ( _t_ ) with simulation frequency and compute the corresponding action. 

## **7 Imitation Learning** 

We perform imitation learning using the translated demonstrations. Instead of using behavior cloning, we adopt imitation learning algorithms that incorporate the demonstrations into RL. 

**Background.** We consider the Markov Decision Process (MDP) represented by _⟨S, A, P, R, γ⟩_ , where _S_ and _A_ are state and action space, _P_ ( _st_ +1 _|st, at_ ) is the transition density of state _st_ +1 at step _t_ +1 given action _at_ . _R_ ( _s, a_ ) is the reward function, and _γ_ is the discount factor. The goal of RL is to maximize the expected reward under policy _π_ ( _a|s_ ). We incorporate RL with imitation learning. Given trajectories _{_ ( _si, ai_ ) _}_<sup>_n_</sup> _i_ =1<sup>fromdemonstrations</sup><sup>_π_D,weoptimizetheagentpolicy</sup> _πθ_ with _{_ ( _si, ai_ ) _}_<sup>_n_</sup> _i_ =1<sup>andreward</sup><sup>_R_.Weevaluateimitationlearningundertwo</sup> settings: state-action imitation and state-only imitation. All methods utilize both demonstrations and reward to learn the dexterous manipulation tasks. 

### **7.1 State-action imitation learning** 

We will introduce two algorithms. The first one is the Generative Adversarial Imitation Learning (GAIL) [33], which is the SOTA IL method that performs occupancy measure matching to learn policy. Occupancy measure _ρπ_ [62] is a density measure of the state-action tuple on policy _π_ . GAIL aims to minimize 

10 Y. Qin et al. 

the objective _d_ ( _ρπ_ E _, ρπθ_ ), where _d_ is a distance function, _πθ_ is the policy parameterized by _θ_ . GAIL use generative adversarial training to estimate the distance and minimize it with the objective as, 



where _Dw_ is a discriminator. To equip GAIL with reward function, we adopt the approach proposed by [38], denoted as GAIL+ in this paper. 

The second algorithm is Demo Augmented Policy Gradient (DAPG) [65]. The objective function for policy optimization at each iteration _k_ is as follow. 



where _A_<sup>_πθ_</sup> is the advantage function [9] of policy _πθ_ , and _λ_ 0 and _λ_ 1 are hyperparameters to determine the advantage of state-action pair in demonstrations. 

### **7.2 State-only imitation learning** 

Besides state-action imitation, we also evaluate the State-Only Imitation Learning (SOIL) [64] algorithm which does using action information from demonstrations. SOIL extends DAPG to the state-only imitation setting by learning an inverse model _hϕ_ with the collected trajectories when running the policy. The inverse model predicts the missing actions in demonstrations and the policy is trained as DAPG. The policy and inverse model are optimized simultaneously. 

## **8 Experiment** 

We conduct experiments on the proposed tasks including _Relocate_ , _Pour_ and _Place Inside_ defined in Section 3. We benchmark different imitation learning algorithms on two aspects: (i) First, we benchmark the different methods by testing on the trained objects but with different configurations. We report the training curves and success rates for all tasks. We also ablate how different ways for hand pose estimation, number of demonstrations, and different environmental parameters can affect imitation learning. (ii) Second, we benchmark how well different imitation learning algorithms can generalize to unseen object instances. We evaluate on both object instances that are taken from the same category as the trained object, and from a different category. 

**Experiment settings.** We adopt TRPO [73] as our RL baseline. We benchmark imitation learning algorithms SOIL, GAIL+, and DAPG. All these algorithms incorporate demonstrations with TRPO of same hyper-parameters. Thus all the algorithms are comparable. All policies are evaluated with the same three random seeds. By default, the hand pose is estimated using two cameras. 

### **8.1 Experiments with Relocate** 

**Main comparisons.** We benchmark four methods: SOIL, GAIL+, DAPG, and RL on the _relocate_ tasks. The _success rate_ is shown in Table 1 and training 

DexMV 

11 



<!-- Start of picture text -->
SOIL GAIL+ DAPG RL<br>1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0<br>0 500 1000 1500 2000 0 500 1000 1500 2000 0 500 1000 1500 2000 0 500 1000 1500 2000 0 500 1000 1500 2000<br>MustardBottle SugarBox TomatoSoupCan LargeClamp Mug<br>Average Return<br><!-- End of picture text -->

Fig. 5: Learning curves of the four methods on the relocate task with respect to five different objects. The x-axis is training iterations. The shaded area indicates standard error and the performance is evaluated with three individual random seeds. 

||||Task - Relocate|||
|---|---|---|---|---|---|
|Model|Mustard|Sugar Box|Tomato Can|Clamp|Mug|
|SOIL|0_._33_±_0_._42|**0.67**_±_**0.47**|0_._98_±_0_._02|0_._89_±_0_._15|0_._71_±_0_._35|
|GAIL+|0_._06_±_0_._01|0_._00_±_0_._00|0_._66_±_0_._47|0_._52_±_0_._39|0_._53_±_0_._37|
|DAPG|**0.93**_±_**0.05**|0_._00_±_0_._00|**1.00**_±_**0.00**|**1.00**_±_**0.00**|**1.00**_±_**0.00**|
|RL|0_._06_±_0_._01|0_._00_±_0_._00|0_._67_±_0_._47|0_._51_±_0_._37|0_._49_±_0_._36|



Table 1: Success rate of the evaluated methods on _Relocate_ with five different objects. Success is defined based on the distance between object and target, evaluated via 100 trials for three seeds. 

curves are in Figure 5. A trial is counted as success only when the final position of the object (after 200 steps) is within 0.1 unit length to the target. The initial object position and target position are randomized. In figure 5, the x-axis is training iterations and the y-axis is normalized average-return over three seeds. 

Both Table 1 and Figure 5 show that the imitation learning methods outperform RL baseline for all five tasks. For mustard bottle and sugar box, a pure RL agent is not able to learn anything. SOIL performs the best for sugar box while DAPG achieves comparable or better performance on mug, mustard bottle, and tomato soup can. _Relocate_ with sugar box is most challenging since it is tall and thin with a flat surface. Once it drops on the table, it is hard to grasp again. We conjecture training the inverse dynamics model online in SOIL helps obtain more accurate action for _Relocate_ . 

**Ablation on motion retargeting method.** Figure 6 (a) illustrates the performance of SOIL with respect to demonstrations generated by different retargeting method, on relocating a tomato soup can. It shows that our retargeting design (blue curve) can improve the imitation learning performance over fingertip mapping (red curve) based retargeting baseline. Besides, without L2 norms in Equation 2 (green curve), the performance shows a huge drop. It indicates the importance of smooth robot motion when used as demonstrations. 

**Ablation on the number of demonstrations.** Figure 6 (b) shows the performance of SOIL with respect to different number of demonstrations, on relocating a tomato soup can. SOIL can achieve better sample efficiency, performance and the variance is reduced when more demonstrations are given. Table 2 illustrates the success rate of the different policies trained with a different num- 

12 Y. Qin et al. 



<!-- Start of picture text -->
1.0 Retargeting Ours 1.0 SOIL (100) 1.0 SOIL (size x0.75) 1.0 SOIL (fric x0.8)<br>0.80.6 Retargeting Without L2 NormRetargeting Finger TipRL 0.80.6 SOIL (50)SOIL (10)RL 0.80.6 SOIL (size x1.0)SOIL (size x1.125)RL (size x0.75)RL (size x1.0) 0.80.6 SOIL (fric x1.0)SOIL (fric x1.2)RL (fric x0.8)RL (fric x1.0)<br>0.4 0.4 0.4 RL (size x1.125) 0.4 RL (fric x1.2)<br>0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0<br>0 250 500 750 1000 1250 1500 1750 2000 0 250 500 750 1000 1250 1500 1750 2000 0 250 500 750 1000 1250 1500 1750 2000 0 250 500 750 1000 1250 1500 1750 2000<br>(a) Retargeting (b) Num of Demo. (c) Object Size (d) Object Friction<br>Average Return Average Return Average Return Average Return<br><!-- End of picture text -->

Fig. 6: **Ablation Study** : Learning curves of SOIL on _Relocate_ with tomato soup can. The x-axis is training iterations. We ablate: (a) hand pose estimation methods; (b) number of demonstrations used to train SOIL; (c) scaling of object size; (d) friction of the relocated object. The demonstrations are kept the same for all conditions. 

|#Demo|400 Iter.|600 Iter.|800 Iter.|Setting|MPJPE|Success (%)|
|---|---|---|---|---|---|---|
|SOIL (100)|**0.36**_±_**0.13**|**0.70**_±_**0.25**|**1.00**_±_**0.00**|1 Cam|41_._7|66_._7_±_57_._7|
|SOIL (50)|0_._19_±_0_._23|0_._40_±_0_._43|0_._59_±_0_._39|1 Cam Post|36_._2|69_._7_±_33_._3|
|SOIL (10)|0_._04_±_0_._05|0_._17_±_0_._11|0_._36_±_0_._21|2 Cam|36_._6|84_._7_±_25_._7|
|RL (0)|0_._00_±_0_._00|0_._00_±_0_._00|0_._13_±_0_._19|2 Cam Post|**32.5**|**93.3**_±_**11.5**|



Table 2: Success rate with different number of demonstrations on _Relocate_ task with a tomato soup can, evaluated via 100 trials for three random seeds at 400, 600, and 800 training iterations. 

Table 3: Hand pose error and the success rate of learned policy for 4 hand pose estimation settings. Smaller MPJPE means better hand pose estimation performance. 

ber of demonstrations. _This shows the importance of our efficient platform to scale up the number and diversity of demonstrations._ 

**Ablation on environmental conditions.** Figure 6 (c) and (d) illustrates that our demonstrations can transfer to different physical environments. Given the same demonstrations on _Relocate_ the tomato soup can, we train policies with objects scaling into different size from _×_ 0 _._ 75 to _×_ 1 _._ 125 (Figure 6 (c)) and applying different frictions (Figure 6 (d)) from _×_ 0 _._ 8 to _×_ 1 _._ 2. With same demonstrations, we can still perform imitation learning in different environments and achieve consistent results. All policies achieve much better performance than pure RL. _This experiment shows the robustness of our pipeline against the gap between simulation (environment) and real (demonstration)._ 

**Ablation on hand pose estimation.** We choose 4 different settings for hand pose estimation from video captured by: (i) single camera; (ii) single camera plus post-processing (iii) dual camera; (iv) dual cameras plus the post-processing (mentioned in Section 5.2) Since we have no ground-truth pose annotation in our dataset, we evaluate the performance of hand pose estimation approaches on the DexYCB [18] dataset, which provides the pose ground-truths. We follow DexYCB to use Mean Per Joint Position Error (MPJPE, smaller the better). We experiment with SOIL on relocating a tomato soup can. The object pose remains the same for all four settings. Table 3 shows better pose estimation in general corresponds to better imitation, except the comparison on 1-Cam Post and 2- Cam. It seems 2-Cam are better than 1-Cam in imitation, even pose estimation result is close. We conjecture 2-Cam can provide more smooth trajectories. 

DexMV 13 



<!-- Start of picture text -->
1.00.8 SOILGAIL+DAPG Model Success (%) 1.501.25 SOILGAIL+DAPG Model Inside Score<br>0.6 RL SOIL 3 . 5  ±  3 . 3 1.00 RL SOIL 27 . 9  ±  26 . 5<br>0.4 GAIL+ 3 . 4  ±  2 . 5 0.75 GAIL+ 16 . 0  ±  14 . 2<br>0.20.0 DAPGRL 27.2 1 . 3  ± ±  18.4  0 . 7 0.500.250.00 DAPGRL 31.3 3 . 2  ± ±  30.0  5 . 6<br>0 250 500 750 1000 1250 1500 1750 2000 0 500 1000 1500 2000 2500 3000<br>(a) Pour (b) Pour (c) Place Inside (d) Place Inside<br>Average Return Average Return<br><!-- End of picture text -->

Fig. 7: _Pour and Place Inside_ . (a) learning curves of _Pour_ ; (b) success rate of _Pour_ ; (c) learning rate of _Place Inside_ ; (d) Inside score of _Place Inside_ . 



|Setting|SOIL|GAIL+|DAPG|RL|
|---|---|---|---|---|
|**Novel O**|**bject Inst**|**ances, Sa**|**me Catego**|**ry**|
|tomato._→_can|62.0_±_27.3|30.7_±_23.5|**83.6**_±_**4.7**|15.9_±_16.7|
|mustard._→_bottle|0.0_±_0.0|0.0_±_0.0|**68.5**_±_**7.0**|0.0_±_0.0|
|mug._→_mug|51.4_±_33.2|33.8_±_36.1|**79.4**_±_**11.9**|27.7_±_38.8|
||**Novel **|**Category**|||
|tomato._→_cam.|27.1_±_13.5|5.9_±_6.3|**47.2**_±_**2.5**|3.8_±_2.1|
|mustard._→_cam.|2.6_±_2.8|0.0_±_0.0|**49.9**_±_**8.5**|0.1_±_0.1|
|mug._→_cam.|25.8_±_18.8|17.3_±_23.1|**33.4**_±_**3.9**|7.5_±_9.5|



Fig. 8: _Relocate_ generalization. Left: visualization of _Relocate_ with unseen ShapeNet objects from 4 categories. Right: success rate of _Relocate_ . A _→_ B denotes using the policy trained on YCB object A to evaluate the performance on ShapeNet category B. 

### **8.2 Experiments with Pour** 

The _Pour_ task involves a sequence of dexterous manipulations: reaching the mug, holding and stably moving the mug, and pouring water into the container. We benchmark four imitation learning algorithms in Figure 7 (a) and (b). We observe that DAPG converges to a good policy with much fewer iterations: 27 _._ 2% of the particles are poured into the container on average. Without the demonstrations, pure RL will only have a very small chance to pour a few particles into the container. State-action method DAPG performs better than state-only method SOIL. It is challenging to learn inverse model with water particles in this task for SOIL, while the analytical inverse dynamics function still provides reasonable actions for DAPG. See our videos and website for visualization. 

### **8.3 Experiments with Place Inside** 

The _Place Inside_ task requires the robot hand to first pick up a banana, rotate it to the appropriate orientation, and place it inside the mug. We define a metric _Inside Score_ , which is computed based on the volume percentage of the banana inside of the mug. We benchmark the imitation learning algorithms in Figure 7 (c) and (d). We find that DAPG outperforms other approaches whereas RL hardly learns to manipulate the object. Between state-only method (SOIL) and state-action method (DAPG), we again observe that computing action offline analytically achieves better results, due to the complexity of the task. 

14 Y. Qin et al. 





<!-- Start of picture text -->
(a) Visualization of Two Tasks<br><!-- End of picture text -->

|Model|Success (%)|Category|Inside Score|
|---|---|---|---|
|SOIL|3_._8_±_3_._2|SOIL|21_._6_±_16_._1|
|GAIL+|2_._1_±_0_._8|GAIL+|10_._9_±_4_._6|
|DAPG|**23.3**_±_**10.4**|DAPG|**26.9**_±_**17.3**|
|RL|0_._5_±_0_._3|RL|1_._8_±_1_._5|
|(b|) Pour|(c) Pl|ace Inside|



Fig. 9: Generalization with _Pour_ and _Place Inside_ . (a) visualization of _Pour_ (top row) with ShapeNet mug, and _Place Inside_ with ShapeNet cellphone; (b) success rate of _Pour_ with ShapeNet Mug; (c) inside score of _Place Inside_ with ShapeNet cellphone. 

### **8.4 Generalization on Novel Objects and Category** 

**Generalization with Relocate.** We benchmark the generalization ability of the trained policy with different imitation learning algorithms. We directly deployed the trained policies for the _Relocate_ task using our demonstrations on: (i) novel unseen objects within the same category; (ii) object instances from a new category. For evaluation on unseen object instances within the same category, we choose the can, bottle, and mug categories from ShapeNet [16] dataset, which corresponds to the tomato soup can, mustard bottle, and mug in our demonstrations. We omit evaluation on the clamp and sugar box policies since there are no corresponding categories in ShapeNet. For the evaluation on new category, we choose the camera category from ShapeNet. We select 100 object instances for each category and pre-process the objects to fit the size of robot hand. More details about data pre-processing can be found in supplementary. We report the results in Figure 8. The success rate is computed as a mean accuracy over all object instances within a category. We find DAPG generalizes well on unseen objects in both same category and novel category experiments, significantly outperforming other approaches. We can also observe generalization to novel categories brings a larger challenge. 

**Generalization with Pour.** We benchmark the generalization performance of the trained policies from all four methods on new mug instances for _Pour_ task. We choose 100 object instances from the ShapeNet mug category for deployment. The top row of Figure 9 (a) visualizes the task with different mugs and Figure 9 (b) shows the success rate. In this benchmark, DAPG still performs the best across all methods. Interestingly, the performance is not much worse than _Pour_ with the trained object (by comparing Fig. 7 (b)). This shows the robustness of imitation learning using our pipeline. 

**Generalization with Place Inside.** For _Place Inside_ , we replace the YCB banana using the objects from cellphone category in ShapeNet as visualized in the bottom row of Figure 9 (a). Figure 9 (c) shows the generalization performance when directly deploying the policy trained with banana. We find the policy performance is also close to Place Inside with banana (by comparing Fig. 7 (d)). This indicates the robustness of policy against small shape variations and human demonstration on single object can also benefit the tasks on new objects. 

DexMV 15 

## **9 Conclusion** 

To the best of our knowledge, DexMV is the first work to provide a platform on computer vision/simulation systems and a pipeline on learning dexterous manipulation from human videos. We propose a novel demonstration translation module to bridge the gap between these two systems. We hope DexMV opens new research opportunities for benchmarking imitation learning algorithms for dexterous manipulation. 

## **References** 

1. Abbeel, P., Ng, A.Y.: Apprenticeship learning via inverse reinforcement learning (2004) 4 

2. Aberman, K., Wu, R., Lischinski, D., Chen, B., Cohen-Or, D.: Learning characteragnostic motion for motion retargeting in 2d. arXiv preprint arXiv:1905.01680 (2019) 7 

3. Andrews, S., Kry, P.G.: Goal directed multi-finger manipulation: Control policies and analysis. Computers & Graphics (2013) 3 

4. Antotsiou, D., Garcia-Hernando, G., Kim, T.K.: Task-oriented hand motion retargeting for dexterous manipulation imitation. In: ECCV Workshops (2018) 4, 8 

5. Aytar, Y., Pfaff, T., Budden, D., Paine, T., Wang, Z., de Freitas, N.: Playing hard exploration games by watching youtube. In: NeurIPS (2018) 4 

6. Baek, S., Kim, K.I., Kim, T.K.: Pushing the envelope for rgb-based dense 3d hand pose estimation via neural rendering. In: CVPR (2019) 4 

7. Bai, Y., Liu, C.K.: Dexterous manipulation using both palm and fingers (2014) 3 

8. Bain, M., Sammut, C.: A framework for behavioural cloning. In: Machine Intelligence (1995) 4 

9. Baird III, L.C.: Advantage updating. Tech. rep. (1993) 10 

10. Bicchi, A.: Hands for dexterous manipulation and robust grasping: A difficult road toward simplicity. IEEE Transactions on robotics and automation (2000) 3 

11. Bojarski, M., Del Testa, D., Dworakowski, D., Firner, B., Flepp, B., Goyal, P., Jackel, L.D., Monfort, M., Muller, U., Zhang, J., et al.: End to end learning for self-driving cars. arXiv (2016) 4 

12. Boukhayma, A., Bem, R.d., Torr, P.H.: 3d hand shape and pose from images in the wild. In: CVPR (2019) 4 

13. Brahmbhatt, S., Ham, C., Kemp, C.C., Hays, J.: Contactdb: Analyzing and predicting grasp contact via thermal imaging. In: CVPR (2019) 2, 4 

14. Brahmbhatt, S., Handa, A., Hays, J., Fox, D.: Contactgrasp: Functional multifinger grasp synthesis from contact. arXiv (2019) 4 

15. Calli, B., Walsman, A., Singh, A., Srinivasa, S., Abbeel, P., Dollar, A.M.: Benchmarking in manipulation research: The ycb object and model set and benchmarking protocols. arXiv (2015) 3, 4, 5, 6, 20, 22 

16. Chang, A.X., Funkhouser, T., Guibas, L., Hanrahan, P., Huang, Q., Li, Z., Savarese, S., Savva, M., Song, S., Su, H., et al.: Shapenet: An information-rich 3d model repository. arXiv preprint arXiv:1512.03012 (2015) 6, 14, 22 

17. Chang, M., Gupta, A., Gupta, S.: Semantic visual navigation by watching youtube videos. In: NIPS (2020) 4 

16 Y. Qin et al. 

18. Chao, Y.W., Yang, W., Xiang, Y., Molchanov, P., Handa, A., Tremblay, J., Narang, Y.S., Van Wyk, K., Iqbal, U., Birchfield, S., et al.: Dexycb: A benchmark for capturing hand grasping of objects. In: CVPR (2021) 4, 12 

19. Craig, J.J.: Introduction to robotics: mechanics and control, 3/E. Pearson Education India (2009) 9 

20. Dogar, M.R., Srinivasa, S.S.: Push-grasping with dexterous hands: Mechanics and a method (2010) 3 

21. Duan, Y., Chen, X., Houthooft, R., Schulman, J., Abbeel, P.: Benchmarking deep reinforcement learning for continuous control (2016) 4 

22. Flash, T., Hogan, N.: The coordination of arm movements: an experimentally confirmed mathematical model. Journal of neuroscience **5** (7), 1688–1703 (1985) 9 

23. Fu, J., Luo, K., Levine, S.: Learning robust rewards with adversarial inverse reinforcement learning. arXiv (2017) 4 

24. Garcia-Hernando, G., Johns, E., Kim, T.K.: Physics-based dexterous manipulations with estimated hand poses and residual reinforcement learning. arXiv (2020) 4 

25. Garcia-Hernando, G., Yuan, S., Baek, S., Kim, T.K.: First-person hand action benchmark with rgb-d videos and 3d hand pose annotations. CVPR (2018) 4 

26. Ge, L., Ren, Z., Li, Y., Xue, Z., Wang, Y., Cai, J., Yuan, J.: 3d hand shape and pose estimation from a single rgb image. In: CVPR (2019) 4 

27. Hampali, S., Rad, M., Oberweger, M., Lepetit, V.: Honnotate: A method for 3d annotation of hand and object poses. In: CVPR (2020) 4 

28. Handa, A., Van Wyk, K., Yang, W., Liang, J., Chao, Y.W., Wan, Q., Birchfield, S., Ratliff, N., Fox, D.: Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In: ICRA (2020) 4, 8, 23 

29. Hasson, Y., Varol, G., Tzionas, D., Kalevatykh, I., Black, M.J., Laptev, I., Schmid, C.: Learning joint reconstruction of hands and manipulated objects. In: CVPR (2019) 2, 4 

30. He, Y., Sun, W., Huang, H., Liu, J., Fan, H., Sun, J.: Pvn3d: A deep point-wise 3d keypoints voting network for 6dof pose estimation. CVPR (2020) 4, 6 

31. Hecker, C., Raabe, B., Enslow, R.W., DeWeese, J., Maynard, J., van Prooijen, K.: Real-time motion retargeting to highly varied user-created morphologies. ACM Transactions on Graphics (TOG) **27** (3), 1–11 (2008) 7 

32. Ho, J., Ermon, S.: Generative adversarial imitation learning. In: NeurIPS (2016) 3, 4 

33. Ho, J., Ermon, S.: Generative adversarial imitation learning. In: NeurIPS (2016) 9 

34. Hu, Y., Hugonot, J., Fua, P., Salzmann, M.: Segmentation-driven 6d object pose estimation. CVPR (2019) 4 

35. Iqbal, U., Molchanov, P., Breuel Juergen Gall, T., Kautz, J.: Hand pose estimation via latent 2.5 d heatmap regression. In: ECCV (2018) 4 

36. Jiang, H., Liu, S., Wang, J., Wang, X.: Hand-object contact consistency reasoning for human grasps generation. arXiv (2021) 4 

37. Johnson, S.G.: The nlopt nonlinear-optimization package (2014) 8 

38. Kang, B., Jie, Z., Feng, J.: Policy optimization with demonstrations. In: ICML (2018) 10 

39. Kato, H., Ushiku, Y., Harada, T.: Neural 3d mesh renderer. In: CVPR (2018) 7 

40. Kehl, W., Manhardt, F., Tombari, F., Ilic, S., Navab, N.: Ssd-6d: Making rgb-based 3d detection and 6d pose estimation great again. ICCV (2017) 4 

41. Khaled, S.M., Islam, M.S., Rabbani, M.G., Tabassum, M.R., Gias, A.U., Kamal, M.M., Muctadir, H.M., Shakir, A.K., Imran, A., Islam, S.: Combinatorial color 

DexMV 17 

space models for skin detection in sub-continental human images. In: IVIC (2009) 6 

42. Kulon, D., Guler, R.A., Kokkinos, I., Bronstein, M.M., Zafeiriou, S.: Weaklysupervised mesh-convolutional hand reconstruction in the wild. In: CVPR (2020) 4 

43. Kumar, V., Xu, Z., Todorov, E.: Fast, strong and compliant pneumatic actuation for dexterous tendon-driven hands. In: ICRA (2013) 2, 5, 7 

44. Kyriakopoulos, K.J., Saridis, G.N.: Minimum jerk path generation. In: Proceedings. 1988 IEEE international conference on robotics and automation. pp. 364–369. IEEE (1988) 9 

45. Li, S., Ma, X., Liang, H., G¨orner, M., Ruppel, P., Fang, B., Sun, F., Zhang, J.: Vision-based teleoperation of shadow dexterous hand using end-to-end deep neural network. In: ICRA (2019) 4 

46. Liu, F., Ling, Z., Mu, T., Su, H.: State alignment-based imitation learning. In: ICLR (2020) 4 

47. Liu, S., Jiang, H., Xu, J., Liu, S., Wang, X.: Semi-supervised 3d hand-object poses estimation with interactions in time. In: CVPR (2021) 4, 6 

48. Liu, Y., Gupta, A., Abbeel, P., Levine, S.: Imitation from observation: Learning to imitate behaviors from raw video via context translation. In: ICRA (2018) 4 

49. Mamou, K., Ghorbel, F.: A simple and efficient approach for 3d mesh approximate convex decomposition. In: 2009 16th IEEE international conference on image processing (ICIP). pp. 3501–3504. IEEE (2009) 23 

50. Mandikal, P., Grauman, K.: Dexterous robotic grasping with object-centric visual affordances. arXiv (2020) 4 

51. Nakamura, Y., Hanafusa, H.: Inverse kinematic solutions with singularity robustness for robot manipulator control (1986) 8 

52. Ng, A.Y., Russell, S.J., et al.: Algorithms for inverse reinforcement learning. (2000) 4 

53. Okamura, A.M., Smaby, N., Cutkosky, M.R.: An overview of dexterous manipulation. In: ICRA (2000) 3 

54. OpenAI, Akkaya, I., Andrychowicz, M., Chociej, M., Litwin, M., McGrew, B., Petron, A., Paino, A., Plappert, M., Powell, G., Ribas, R., Schneider, J., Tezak, N., Tworek, J., Welinder, P., Weng, L., Yuan, Q., Zaremba, W., Zhang, L.: Solving rubik’s cube with a robot hand. arXiv (2019) 3 

55. OpenAI, Andrychowicz, M., Baker, B., Chociej, M., J´ozefowicz, R., McGrew, B., Pachocki, J., Petron, A., Plappert, M., Powell, G., Ray, A., Schneider, J., Sidor, S., Tobin, J., Welinder, P., Weng, L., Zaremba, W.: Learning dexterous in-hand manipulation. arXiv (2018) 2, 3 

56. Pathak, D., Mahmoudieh, P., Luo, G., Agrawal, P., Chen, D., Shentu, Y., Shelhamer, E., Malik, J., Efros, A.A., Darrell, T.: Zero-shot visual imitation. In: ICLR (2018) 4 

57. Peng, S., Liu, Y., Huang, Q.X., Bao, H., Zhou, X.: Pvnet: Pixel-wise voting network for 6dof pose estimation. CVPR (2019) 4 

58. Peng, X.B., Coumans, E., Zhang, T., Lee, T.W., Tan, J., Levine, S.: Learning agile robotic locomotion skills by imitating animals. arXiv (2020) 4 

59. Peng, X.B., Kanazawa, A., Malik, J., Abbeel, P., Levine, S.: Sfv: Reinforcement learning of physical skills from videos. TOG (2018) 4 

60. Peters, J., Schaal, S.: Reinforcement learning of motor skills with policy gradients. Neural networks (2008) 4 

61. Pomerleau, D.A.: Alvinn: An autonomous land vehicle in a neural network. In: NeurIPS (1989) 4 

Y. Qin et al. 

18 

62. Puterman, M.L.: Markov Decision Processes: Discrete Stochastic Dynamic Programming. John Wiley & Sons, Inc. (1994) 9 

63. Rad, M., Lepetit, V.: Bb8: A scalable, accurate, robust to partial occlusion method for predicting the 3d poses of challenging objects without using depth. ICCV (2017) 4 

64. Radosavovic, I., Wang, X., Pinto, L., Malik, J.: State-only imitation learning for dexterous manipulation. IROS (2021) 2, 3, 4, 10 

65. Rajeswaran, A., Kumar, V., Gupta, A., Vezzani, G., Schulman, J., Todorov, E., Levine, S.: Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. arXiv (2017) 10, 20 

66. Rajeswaran, A., Kumar, V., Gupta, A., Vezzani, G., Schulman, J., Todorov, E., Levine, S.: Learning complex dexterous manipulation with deep reinforcement learning and demonstrations (2018) 2, 3, 4, 6 

67. Romero, J., Tzionas, D., Black, M.J.: Embodied hands: Modeling and capturing hands and bodies together. ToG (2017) 6, 7 

68. Ross, S., Bagnell, D.: Efficient reductions for imitation learning. In: AISTATS (2010) 4 

69. Rus, D.: In-hand dexterous manipulation of piecewise-smooth 3-d objects. The International Journal of Robotics Research (1999) 3 

70. Russell, S.: Learning agents for uncertain environments (1998) 4 

71. Schmeckpeper, K., Rybkin, O., Daniilidis, K., Levine, S., Finn, C.: Reinforcement learning with videos: Combining offline observations with interaction. arXiv (2020) 2, 4 

72. Schmeckpeper, K., Xie, A., Rybkin, O., Tian, S., Daniilidis, K., Levine, S., Finn, C.: Learning predictive models from observation and interaction. arXiv (2019) 4 

73. Schulman, J., Levine, S., Abbeel, P., Jordan, M., Moritz, P.: Trust region policy optimization. In: ICML (2015) 10 

74. Sermanet, P., Lynch, C., Chebotar, Y., Hsu, J., Jang, E., Schaal, S., Levine, S., Brain, G.: Time-contrastive networks: Self-supervised learning from video (2018) 4 

75. Shan, D., Geng, J., Shu, M., Fouhey, D.: Understanding human hands in contact at internet scale. In: CVPR (2020) 6 

76. Shao, L., Migimatsu, T., Zhang, Q., Yang, K., Bohg, J.: Concept2robot: Learning manipulation concepts from instructions and human demonstrations. In: RSS (2020) 4 

77. Sharma, P., Mohan, L., Pinto, L., Gupta, A.: Multiple interactions made easy (mime): Large scale demonstrations data for imitation. arXiv (2018) 4 

78. Sharma, P., Pathak, D., Gupta, A.: Third-person visual imitation learning via decoupled hierarchical controller. In: NIPS (2019) 4 

79. Sieb, M., Xian, Z., Huang, A., Kroemer, O., Fragkiadaki, K.: Graph-structured visual imitation. In: CoRL (2020) 4 

80. Smith, L., Dhawan, N., Zhang, M., Abbeel, P., Levine, S.: Avid: Learning multistage tasks via pixel-level translation of human videos. arXiv (2019) 4 

81. Song, S., Zeng, A., Lee, J., Funkhouser, T.: Grasping in the wild: Learning 6dof closed-loop grasping from low-cost demonstrations. Robotics and Automation Letters (2020) 3, 4 

82. Spurr, A., Song, J., Park, S., Hilliges, O.: Cross-modal deep variational hand pose estimation. In: CVPR (2018) 4 

83. Taheri, O., Ghorbani, N., Black, M.J., Tzionas, D.: Grab: A dataset of whole-body human grasping of objects. In: ECCV (2020) 2, 4 

DexMV 19 

84. Tekin, B., Sinha, S.N., Fua, P.: Real-time seamless single shot 6d object pose prediction. CVPR (2018) 4 

85. Todorov, E., Erez, T., Tassa, Y.: Mujoco: A physics engine for model-based control. In: IROS (2012) 5, 20 

86. Todorov, E., Jordan, M.I.: Smoothness maximization along a predefined path accurately predicts the speed profiles of complex arm movements. Journal of Neurophysiology (1998) 9 

87. Torabi, F., Warnell, G., Stone, P.: Behavioral cloning from observation. arXiv (2018) 4 

88. Torabi, F., Warnell, G., Stone, P.: Generative adversarial imitation from observation. arXiv (2018) 4 

89. Veˇcer´ık, M., Hester, T., Scholz, J., Wang, F., Pietquin, O., Piot, B., Heess, N., Roth¨orl, T., Lampe, T., Riedmiller, M.: Leveraging demonstrations for deep reinforcement learning on robotics problems with sparse rewards. arXiv (2017) 4 

90. Xiang, Y., Schmidt, T., Narayanan, V., Fox, D.: Posecnn: A convolutional neural network for 6d object pose estimation in cluttered scenes. arXiv (2018) 2, 4 

91. Xiong, H., Li, Q., Chen, Y.C., Bharadhwaj, H., Sinha, S., Garg, A.: Learning by watching: Physical imitation of manipulation skills from human videos. arXiv (2021) 4 

92. Young, S., Gandhi, D., Tulsiani, S., Gupta, A., Abbeel, P., Pinto, L.: Visual imitation made easy. arXiv (2020) 3, 4 

93. Zimmermann, C., Brox, T.: Learning to estimate 3d hand pose from single rgb images. In: CVPR (2017) 4 

20 Y. Qin et al. 

## **A Appendix Overview** 

This supplementary material provides more details, results and visualizations accompanying the main paper. In summary, we include 

- More details about video data collection; 

- More details about the _Relocate_ , _Pour_ , and _Place inside_ environments 

- More details about demonstration translation; 

- More visualization of hand-object pose estimation and hand motion retargeting results. 

## **B Video Data Collection** 

We use Intel RealSense D435 cameras to collect human demonstrations of manipulating different objects for finishing diverse tasks on the table. In detail, each captured demonstration is about 10 seconds. Moreover, after the demonstration is captured, only the pour task is in need to reset the particles back into the mug, which tasks about 6 seconds. Thus, the time cost for data collection is not high, and the procedure tends to be scalable on different objects and tasks. In practice, it takes about 60 minutes to capture all 100 sequences for a task. 

## **C Environments** 

We propose three types of manipulation tasks along with the DexMV Platform: _Relocate_ , _Pour_ , and _Place Inside_ . The manipulated objects come from YCB Dataset [15]. Environments use the MuJoCo simulator [85] with timestep set to 0 _._ 002 and frame skip set to 5. We adopt the same contact friction parameters following the setting in the literature [65]. We use the open-source MuJoCo model of Adroit Hand<sup>1</sup> . Figure 10 shows the seven different task used in DexMV: _Relocate_ with five different objects, _Pour_ , and _Place Inside_ . 

**Action.** The action space is the same for all tasks, which is the motor command of 30 actuators on the robotic hand. The first 6 motors control the global position and orientation of the robot while the last 24 motors control the fingers of the hand. We normalize the action range to ( _−_ 1 _,_ 1) based on actuator specification. 

### **C.1 Relocate** 

**Observation.** The observation of _Relocate_ is composed of four components: (i) joint angles of adroit robotic hand; (ii) global position of adroit hands root; (iii) object position; (iv) target position. The overall observation space is 39-dim. **Reward.** The reward is defined based on three distances: (i) the distance between the robot hand and the object; (ii) the distance between the robot hand 

> 1 https://github.com/vikashplus/Adroit 

DexMV 

21 



<!-- Start of picture text -->
Clamp<br>Relocate<br>Mug<br>Relocate<br>Relocate  Mustard<br>Relocate  Sugar Box<br>Relocate  Soup Can<br>Pour<br>Place  Inside<br><!-- End of picture text -->

Fig. 10: **DexMV Tasks.** There are three types of tasks in the figure. The first five columns: _relocate_ with mug, mustard bottle, clamp, sugar box, tomato soup can. _Relocate_ task means that the agent needs to move the object from the initial position to the target position. The sixth and seventh columns: _Pour_ and _Place Inside_ . In _Pour_ task, the agent needs to pour the water particles inside a mug into the yellow container. In _Place Inside_ task, the agent needs to manipulate the orientation of the banana to place it inside a mug. Both of the last two tasks require delicate manipulation. 

and the target; (iii) the distance between the object and the target. Lower distance corresponds to higher reward. 

**Reset.** For each episode, the xy position of both object and target is randomized within a ( _−_ 0 _._ 3 _,_ 0 _._ 3) square on the table. The height of target is randomized between (0 _._ 15 _,_ 0 _._ 25). 

22 Y. Qin et al. 

### **C.2 Pour** 

**Observation.** Similar to _Relocate_ , we include the robot joint angles, root position of robot hand, and object position in the observation. In _Pour_ , we replace the target position with the container position. Besides, since the agent needs orientation information of the mug to pour the water particles, we add a quaternion to represent object orientation. 

**Reward.** The main reward is based on the final number of particles that fell within the container. Additionally, similar to _Relocate_ , we use the distance between the robot hand and the object as well as the distance between the object and the container to provide part of the rewards. Lower distance leads to higher reward. The coefficient of the main reward is 10 _×_ larger than the reward computed based on the distance. 

**Reset.** For each episode, the xy position of the mug is randomized between ( _−_ 0 _._ 1 _,_ 0 _._ 1) on the table. The water particles are inside the mug at the beginning of each episode. The container is always at the center of the tabletop. 

### **C.3 Place Inside** 

**Observation.** The observation space of the _Place Inside_ task is the same as the observation space of _Pour_ as described in Section C.2. 

**Reward.** The main reward is based on the position and orientation of the manipulated object. If the object is placed inside of the mug, the agent will get a large portion of the reward. Similar to _Relocate_ , we also add a lifting reward to encourage the robot to first lift the object before moving it towards the container. **Reset.** For each episode, the xy position of the object is randomized between ( _−_ 0 _._ 15 _,_ 0 _._ 15) on the table. The container, i.e. mug, is always placed at the center of tabletop. 

### **C.4 ShapeNet Objects** 

In the _Generalization on Novel Objects and Category_ experiments (Section 8.4) of the main paper, we use objects from ShapeNet [16] dataset. We preprocess the ShapeNet geometry by scaling the mesh so that it can be used in our simulated environment. The YCB objects [15] are captured from the real scan, so the scale of object mesh from YCB dataset aligns with the real counterpart and can be used for robot manipulation directly. Different from the YCB dataset, the ShapeNet dataset does not contain any scale information, e.g. the mug in ShapeNet can be larger than the robot. So we need to scale the object to a reasonable size in which it can be manipulated by the robot. We scale the object based on the diagonal length of the object bounding box. For each category, we manually select a diagonal length so that all object instances from the category will have the same bounding-box diagonal length after scaling. Besides, we will not use objects with non-manifold geometry to avoid instability 

DexMV 23 

in physical simulation. For the _Place Inside_ task, the object mesh should be watertight for volume computation. We use the convex meshes processed by VHACD [49] for both simulation and volume computation. 

## **D Demonstration Translation** 

### **D.1 Kinematics Model** 

In Table 4, we compare the difference of kinematics model between the human hand and robot hand. The overall Degree-of-Freedom(DoF) of the human hand is higher than the DoF of the robot hand. Thus hand motion retargeting from human to robot is projecting a pose from a higher dimension to a lower dimension, which will lose information inevitably. The motion retargeting module try to maintain the task space vectors between these two different kinematics model. 

||**H**-Joints|**H**-DoF|**R**-Joints|**R**-DoF|
|---|---|---|---|---|
|Thumb|3x Ball|9|5x Revolute|5|
|Index|3x Ball|9|4x Revolute|4|
|Middle|3x Ball|9|4x Revolute|4|
|Ring|3x Ball|9|4x Revolute|4|
|Pinkie|3x Ball|9|5x Revolute|5|
|Wrist|Null|0|2x Revolute|2|
|Root|1x Free|6|1x Free|6|
|Overall|N/A|51|N/A|30|



Table 4: **Comparison of Kinematics** We compare the kinematic model between MANO human hand and the robot hand we used in simulator. **H** is the abbr for Human while **R** stands for robot. For example, the **H** -Joints column shows the number and type of joints for a specific sub-part in the kinematics model. Each ball joint has 3 Degree-of-Freedom(DoF), each revolute joint has 1 DoF, and each free joint has 6 DoF 

### **D.2 Initialization in Hand Motion Retargeting** 

As mentioned in the Demonstration Translation section of the main paper, the robot joint angles are solved using optimization. A good initialization is essential for optimization. For _t ≥_ 1, _qt_ is initialized using the optimization results _qt−_ 1. Here we will discuss how to initialize _qt_ for _t_ = 0. Previous work [28] initializes _qt_ with zero vectors. The optimization cannot provide reasonable outputs when the goal is far from zeros. To tackle this issue, we use a heuristic function _ϕ_ ( _θ_ 0) to initialize _q_ 0. The heuristic function takes the MANO hand pose parameters _θ_ 0 and outputs an estimation of the robot joint angles. The heuristic function _ϕ_ ( _θ_ 0) can be regarded as a coarse hand motion retargeting function 

24 Y. Qin et al. 

which does not consider the shape difference between human and robot hands. It is only used to provide a reasonable initialization for further optimization. 

Given the axis-angle representation _θ_ 0 from hand pose estimation, we first convert it to 15 rotation matrices. Then we compute the projection of each rotation matrix on the joint axis direction of each robot hand joint. Then we use a manually-designed vector _w_ to map the projection to the robot joint angle. The overall function can be formulated as below, 



where **R** ( _·_ ) is the Rodrigues’ formula that maps axis-angle to rotation matrix, **Prot** ( _·_ ) is the projection function to compute the nearest rotation along with the robot joint direction for each joint, i.e. projection. **Prot** ( **R** ( _θ_ 0)) _∈_ R<sup>24</sup><sup>_×_15</sup> and _w ∈_ R<sup>15</sup> is a manually designed vector. Thus the dimension of _ϕ_ ( _θ_ 0) is 24, which corresponds to the joint angles for finger and wrist. As mentioned in Table 4, the overall DoF of the robot hand is 24 + 6 = 30, which includes 6 DoF hand root pose. We directly use the root position plus root orientation from human hand pose estimation as the root pose for the robot hand. 

### **D.3 Post Processing** 

**Filter Estimated Pose:** When human is manipulating the object, either hand or object is in heavy occlusion, which may cause inconsistent estimation results. To improve the temporal consistency of the estimated hand and object poses, we apply a digital low-pass filter to remove the high-frequency noise. The sampling frequency of the filter is 100 while the cutoff frequency is 5 for the position of both object and hand. Filtering the rotation is not as straightforward as filtering the position. To get a smooth orientation sequence, we first convert the rotation into _so_ (3) lie algebra. Then, we apply the filter in _so_ (3) space and convert it back to rotation matrix _SO_ (3) after filtering. 

**Hindsight Goal Position for Relocate.** As mentioned in the Task Section of the main paper, _relocate_ is a goal-conditioned task. The goal information should also be included in the state representation. To provide goal information from human demonstration, we use the position of the object in the last step as the hindsight goal. 

**Frame Alignment.** Spatial quantities like object pose are dependent on the frame in which it is observed. The natural frame for pose estimation results is the camera frame. In the simulated environment, such a camera frame does not exist and the pose is represented in the world coordinate fixed on the table. Thus we also align the frame in demonstrations to match the simulated environment. 

## **E More Visualization of Hand-Object Pose Estimation and Hand Motion Retargeting** 

In this section, we provide more visualization on hand-object pose estimation and hand motion retargeting in Figure 11. The four tasks in the first three rows 

DexMV 25 



<!-- Start of picture text -->
Raw<br> Image<br>Human<br>Hand Pose<br>Pose<br>Robot Hand<br>Raw<br> Image<br>Human<br>Hand Pose<br>Pose<br>Robot Hand<br><!-- End of picture text -->

Fig. 11: **3D hand-object pose estimation results and hand motion retargeting results.** Visualization on relocate tomato soup can, sugar box, mustard bottle, mug, clamp, pour, and place inside. 

are _Relocate_ with tomato soup can, sugar box, a mustard bottle, and mug. The three tasks in the last three rows are: _Relocate_ with clamp, _Pour_ , and _Place Inside_ . 

