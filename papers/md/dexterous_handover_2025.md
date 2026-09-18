# **Learning Dexterous Object Handover** 

Daniel Frau-Alfaro<sup>1</sup> , Julio Casta˜no-Amoros<sup>1</sup> , Santiago Puente<sup>1</sup> , Pablo Gil<sup>1</sup> and Roberto Calandra<sup>2</sup> 

**_Abstract_ — Object handover is an important skill that we use daily when interacting with other humans. To deploy robots in collaborative setting, like houses, being able to receive and handing over objects safely and efficiently becomes a crucial skill. In this work, we demonstrate the use of Reinforcement Learning (RL) for dexterous object handover between two multi-finger hands. Key to this task is the use of a novel reward function based on dual quaternions to minimize the rotation distance, which outperforms other rotation representations such as Euler and rotation matrices. The robustness of the trained policy is experimentally evaluated by testing w.r.t. objects that are not included in the training distribution, and perturbations during the handover process. The results demonstrate that the trained policy successfully perform this task, achieving a total success rate of 94% in the best-case scenario after 100 experiments, thereby showing the robustness of our policy with novel objects. In addition, the best-case performance of the trained policy decreases by only 13.8% when the other robot moves during the handover, proving that our policy is also robust to this type of perturbation, which is common in realworld object handovers. Code and videos can be found here.** 

## I. INTRODUCTION 

With the recent focus on humanoid robots, service robots, and human-robot collaboration, several efforts have been made to teach robots how to perform dexterous manipulation tasks, such as collaborative assembly, package manipulation in logistics, and household chores. However, there are still many open questions about how to approach this type of tasks using robots, which require a variety of skills, including a high degree of dexterity, perception, coordination, collaboration, and understanding [1] [2]. In contrast, humans have an innate talent for performing tasks that require these types of skills. Therefore, it makes sense to bring humans into the loop when tackling these complex problems. 

In particular, this work addresses the task of object handover which can be very interesting in the context of humanrobot collaboration for both industrial and social applications. According to [3], the object handover collaboration can 

*This work was partially supported by the Interreg-VI Sudoe and European Regional Development Fund through the REMAIN Project under Grant S1/1.1/E0111, by the project “Genius Robot” (01IS24083) BMBF, by the DFG as part of EXC 2050/1 – Project ID 390696704 CeTI of Technische Universit¨at Dresden by BMBF, and by the DAAD in project 57616814 (SECAI School of Embedded and Composite AI) and by the Spanish Government through the Grant PID2021-122685OB-I00 and by the University of Alicante under Grant UAFPU21-26. 

*This work was conducted during Julio’s research stay at LASR Lab. 1Daniel Frau-Alfaro, 1Julio Casta˜no-Amoros, 1Santiago Puente and 1Pablo Gil are with the AUROVA Lab, Department of Physics, Systems Engineering, and Signal Theory, University of Alicante, 03690 Alicante, Spain daniel.frau@ua.es, julio.ca@ua.es, santiago.puente@ua.es, pablo.gil@ua.es 

> 2Roberto Calandra is with LASR Lab, Technische Universitat Dresden, Dresden, Germany rcalandra@lasr.org 



<!-- Start of picture text -->
Maneuver Approach Handover<br>s t s t+n<br>a t a t+n<br>r t r t+n<br><!-- End of picture text -->

Fig. 1. Overview of the different phases of the object handover process. Both robots must collaborate to successfully complete object handover, which is more complicated when employing multi-finger robotic hands. 

be classified into robot-robot collaboration, human-robot collaboration, and robot-human collaboration. The differences between them are whether humans are involved in the task or not, and which participant acts as the giver and which one as the receiver. This type of collaboration typically comprises different subtasks, from the maneuver to set the initial hand pose to the object handover and its subsequent manipulation, as illustrated in Fig. 1, that must be resolved in order to complete the task. 

In this work, we explore the object handover task based on robot-robot collaboration, as an initial step for humanrobot and robot-human collaboration. We assume that the robotic hand holding the object is already fixed in an arbitrary handover pose. Consequently, our objective is to train a single RL policy so that a robotic arm and hand can learn how to approach, grasp, and transport the object from another robotic system. The main contributions of this work are twofold. First, in contrast of using 2-finger small grippers as in [4], we use 4-finger articulated hands, which increases the DoF and consequently the difficulty of applying learningbased strategies. In addition, unlike other works such as [5] [6], we discard the use of teleoperation systems to teach robots how to perform the task. Second, [7] proposed a dual quaternion-based reward function to avoid rotation constraints in _S_ 0(3). The goal of this work is to expand that reward function to the object handover task using 4-finger robotic hands, and to compare it with other representations, such as Euler or matrix rotation, that do require these restrictions. 

## II. RELATED WORK 

Traditionally, collaboration tasks such as object handover have been addressed employing control theory algorithms, sensor fusion techniques, probabilistic methods, etc., as in [3], [8], and [9]. Although the results of such approaches are promising, they are limited for several reasons. For instance, sensor fusion techniques tend to accumulate errors when calibrating different devices. More specifically, the use of 

TABLE I 

control theory algorithms require the design of the policy for each subtask, while our goal is to learn it using RL. 

In the literature of RL-based object handover, this task has been addressed in different ways. For instance, [10] formulated the object handover task by throwing and catching small objects, while our approach is based on a direct handover using longer objects due to the size of the hands. The authors employed two 6-DoF robotic arms and two Allegro hands, similarly as we do in our work. They proposed a multiagent approach and a three-phase training, while our policy comprises a single agent and trains on a single-phase process, thereby reducing the number of hyperparameters to tune. Their trained policies obtained a throw and catch success rate of 95% and 37% when testing with 11 known objects and 14 novel objects in simulation, respectively. These results showed a large gap in robustness when evaluating with objects out of the training distribution. Our policy is more robust in this type of case, although we use fewer objects to evaluate in our experiments. 

Although throwing and catching can be considered a type of object handover, it does not involve physical interaction between the robots and the object at the same time, which is what we are interested in exploring in this work. In this context, repositioning objects using two robotic systems requires transferring the object between them, resulting in a direct handover [4]. To achieve this, a single-agent policy was trained via actor-critic learning, which is similar to our approach. In this case, the authors employed two 7- DoF robotic arms equipped with two 2-finger grippers to handover objects similar to ours. However, they simplified the task by using grippers instead of multi-finger hands, which require orientation optimization in _SO_ (3), as we propose in our work. They reported an average success rate of 94% in the simulated environment, which is similar to the results obtained in our experiments, taking into account the complexity of using multi-finger hands with different objects in our approach. 

Humanoid robots equipped with multi-finger hands have also been employed to approach this task using RL recently [11]. Specifically, two 7-DoF robotic arms and two 5-finger grippers were involved in the robotic setup. Initially, they recorded demonstrations to capture the human pose of the hands at the beginning of the episode, while we let our policy learn how to maneuver to approach the object correctly, which can sometimes produce more optimal results. As visual input, they performed an ablation study to evaluate the use of the 3D object position together with the depth image. The results of this study reported that their policy was not able to learn with the depth image alone, but with the 3D object position, as we do in our work. Similar to our work, they designed a contact-based reward function. However, they generated several contact markers to guide the policy to grasp the object, while we only define a single grasping frame and let the policy learn how to grasp the object and keep it stable. The main difference of our approach is the use of dual quaternions to learn the orientation of the hands, which is not considered in any of the aforementioned works. 

BASIC OPERATIONS WITH DUAL QUATERNIONS. WE USED THESE 

OPERATIONS TO CALCULATE THE REWARD FUNCTION IN SECTION IV-B. 

|**Operation**|**Formulation**|
|---|---|
|**Primary part**|_P_(ˆ**q**1) =**qp**1|
|**Dual Part**|_D_(ˆ**q**1) =**qd**1|
|**Addition**|ˆ**q**1+ˆ**q**2=**qp**1+**qp**2+_ε_(**qd**1+**qd**2)|
|**Multiplication**|ˆ**q**1_⊗_ˆ**q**2=**qp**1_·_**qp**2+_ε_(**qp**1_·_**qd**2+**qd**1_·_**qp**2)|
|**Conjugate**|ˆ**q**<sup>_∗_</sup><br>1 <sup>=</sup><sup>**q**</sup><sup>_∗_</sup><br>**p**1 <sup>+</sup><sup>_ε_</sup><sup>**q**</sup><sup>_∗_</sup><br>**d**1|
|**Magnitude**|_||_ˆ**q**1_||_= ˆ**q**1_⊗_ˆ**q**<sup>_∗_</sup><br>1|
|**Difference**|ˆ**q**diff= ˆ**q**<sup>_∗_</sup><br>1 <sup>_⊗_ˆ</sup><sup>**q**2</sup>|
|**Identity Element**|ˆ**I**=**I**+_ε_0_,_ **I**= (1+0_i_+0_j_+0_k_) _∈_H|



## III. MATHEMATICAL FOUNDATIONS 

RL and Deep Reinforcement Learning (DRL) algorithms allow to obtain policies for a vast range of tasks with high dimensionality of actions and observations, like object handover, which are difficult to deal with classical control techniques. In this section, a brief introduction to the basics of the RL paradigm is provided. Next, we explain the dual quaternion algebra used in this work. 

## _A. RL basics_ 

The RL approach considers every problem as a Markov Decision Process (MDP) [12] [13]. Following this modeling, an agent placed in an environment captures information as a state _st_ . Then, it produces an action _at_ based on a certain policy _at ∼ π_ ( _·|st_ ). This produces a change (or step) in the environment, leading to _st_ +1. In addition, the agent receives a reward _rt_ that indicates how good the action was according to the task it is performing. With this, the final objective of the agent is to generate a policy _π_ that maximizes the expected return over time, estimated using (1). 



where _γ ∈_ [0 _,_ 1] is the discounting factor over time. 

## _B. Dual quaternion algebra_ 

For the sake of clarity, a brief introduction to dual quaternion algebra is presented [14] [15]. In the upcoming explanation, we assume some previous knowledge in the field of simple quaternions **q** _∈_ H to represent rotations in _SO_ (3). 

Dual quaternions are an extension of the group of dual numbers _q_ ˆ _∈ H_ with _q_ ˆ = ( _a_ + _εb_ ) _,_ ( _a, b_ ) _∈_ R and with _ε_ being the dual operator that fulfils that _ε_<sup>2</sup> = 0 _, ε̸_ = 0. The elements of a dual quaternion are simple quaternions instead of real numbers, therefore, considering **ˆq** as a dual quaternion, **ˆq** _∈_ <u>H</u> with **ˆq** = ( **a** + _ε_ **b** ) _,_ ( **a** _,_ **b** ) _∈_ H. This formulation allows performing the mathematical operations in Table I given **ˆq1** = **qp1** + _ε_ **qd1** and **ˆq2** = **qp2** + _ε_ **qd2** and with _≪· ≫_ being the dot operation of two vectors. 



<!-- Start of picture text -->
Hand Joint Avg.<br>size: 3<br>Object Pose<br>Euclidean Translation (size: 3) + Euler (size: 3)<br>Hand Pose<br>Euclidean Translation (size: 3) + Euler (size: 3)<br>Policy<br>Object Pose<br>Hand Pose<br>Hand Joint Avg.<br>PPO<br>Kinova GEN3 UR5e<br>Incremental Action<br>Cartesian (size: 6) + Hand Joint Avg. (size: 3)<br><!-- End of picture text -->

Fig. 2. Overview of the RL environment used in this work, comprising a single PPO agent. The observations consist of the Euclidean translations and Euler rotations of the GEN3 robot and the object, as well as the average of each joint value for the different fingers, resulting in three global joint values for the whole hand. The policy outputs increments in translation and Euler rotation as actions for the GEN3 end effector, and the three corresponding increment joint values for the hand. 

Dual quaternions are often used to represent poses in _SE_ (3) space, combining translations and rotations in a compact and short formulation. Hence, given a rotation quaternion **qr** and a translation **qt** expressed as a pure quaternion, that is, a quaternion with null real part, the dual quaternion expressing that transformation is written following (2). 



where the resulting dual quaternion meets the unitary condition as _||_ **q** ˆ _||_ = 1. The primary part of a dual quaternion represents the rotation of a pose, while the dual part contains information about the translation along that orientation. 

There are other formulations so as to represent poses in 3D space. Most of them utilize the Euclidean translation to encode translations and vary the way in which we can express orientations. An example of this issue are homogeneous transformation matrices _SO_ (3) ⋊R<sup>3</sup> . This approach employs 16 values to encode a pose in space, which is less computationally efficient to operate with, compared to the dual quaternion representation. In addition, we can compute the difference or distance between poses separately in rotation and translation, which requires normalization to combine them. Other representations use translation vectors along with Euler angles to represent positions and rotations R<sup>3</sup> ⋊R<sup>3</sup> , respectively. However, this alternative also suffers from the separation of distances and other problems, e.g. gimbal lock or singularities when interpolating. 

Summarizing, the dual quaternion allows for a unified representation of poses; both translations and rotations are expressed under the same formulation, and they do not need further processing or constraints to compute distances. 

## IV. HANDOVER SYSTEM AND REWARD FUNCTION DESIGN 

We now introduce the task modeling and the design of our reward function. We define the states and actions in the RL framework, as well as the division of the handover task into movement primitives that enable the formulation of a reward function by parts. 

## _A. Object Handover Setup_ 

In terms of modeling of the environment, we use an UR5e (6 DoF) and GEN3 (7 DoF), both equipped with Allegro Hands and touch sensors to perform the manipulation. At the start of each episode, we initialize the UR5e to an arbitrary pose chosen randomly. The UR5e robot holds the object without moving during the whole episode as shown in Fig. 2. This way, it mimics a human giver which should not be trained. Then, the GEN3 has to learn to reach the object and grasp it from the same starting pose in each episode. The policy takes as observations the Cartesian poses of the GEN3 and the object along with its hand joint values. In terms of actions, we add increments to the current pose of the GEN3 end effector and to the joint values of the hand. 

## _B. Task Modeling_ 

As for the task modeling and the reward function, it is worth mentioning that we divide the object handover task into different movement primitives or phases, as shown in Fig. 1. In each stage, we change a simple initial reward function defined in (3) using different modifiers. These provide the reward function 





Fig. 3. Example of different poses of the GEN3 hand evaluated with respect to the relative pose of the object. The different colors of the GEN3 hand indicate how adequate is the approach to grasp the object correctly. **Red** : oriented with the back of the hand toward the object, **Orange** : closer to the UR5e hand than to the object frame, **Green** : palm facing the object correctly and closer to the object frame. 

for each phase of the task, where _r_ BASE _t_ is a basic reward for approaching the object, _dt_ is the distance between the pose of the hand and the object at step _t_ and _ηt_ is the weight of the reward at step _t_ which will be defined in (6). 

_1) Maneuver phase:_ The reward in (3) incentivizes the agent to approach the object along a straight trajectory, although it can be troublesome because the robots may collide or the GEN3 hand might be oriented with its back facing the object, as shown in Fig. 3. For this reason, we restrict the reward to take the GEN3’s end effector closer to the object than to the UR5e. Moreover, we propose a double frame system for the agent to maneuver into a suitable position for manipulation, with the GEN3 palm toward the target. If both conditions are satisfied, the agent is in a correct zone for approaching. First, we calculate the distance between the palm of each robot _d_ ROBOTS _t_ . Then, we define a frame for the back of the GEN3 hand, computing the distance between it and the object _d_ BACK _t_ . In this way, we define a condition for the approach phase in (4), which we will use in (5). 



where _m_ MAN _t ∈{_ 0 _,_ 1 _}_ is a modifier for (3) which we will use in the following equations. 

_2) Approach phase:_ Once the GEN3 palm is located in a suitable zone for approaching the object, the action taken at _t_ must bring the agent closer than it was at step _t −_ 1. Hence, in (5) we extend the maneuver modifier _m_ MAN _t_ to restrict the distance at _t_ and so to be lower than the one in the previous step. 



where ( _dt < dt−_ 1) _∈{_ 0 _,_ 1 _}_ and _mt ∈{−_ 1 _,_ 1 _}_ . 

_3) Handover phase:_ For the handover phase, we place tactile sensors on the phalanges of the fingers and the palm of the GEN3 hand, as shown in Fig. 4. In this way, we can detect the contacts between each finger and other elements of 



<!-- Start of picture text -->
Contact Sensors<br><!-- End of picture text -->

Fig. 4. Placement of the contact sensors on the Allegro hand. Each green area represents a boolean contact sensor. It is important to note that contact sensing beyond the fingertips is necessary to successfully complete the object handover task as the object is mainly grasped with the palm and the proximal phalanges. 

the simulation. We define the contacts as a vector of Boolean values _⃗ c_ and we weight them using _⃗ wc_ according to their relevance in the task; the lower phalanges are of greater importance than the tips. In this work, it is worth mentioning that we only consider the contacts between the GEN3 hand and the object. In (6) we modify the original weight _η_ 0 = 1 according to the contacts. Therefore, the more touches, the lower that value will be. 



In addition, we add the weighed sum of contacts _⃗ c ·⃗ wc_ to the reward _r_ BASE _t_ . Thus, when the agent touches the object, the reward encourages it to close the hand rather than to continue advancing towards the target. 

_4) Manipulation phase:_ In the previous phases, the object is not grasped yet and the UR5e hand remains closed. This stage is changed when the thumb and another finger of the GEN3 hand touch the object. At this point, we consider the object susceptible to be grasped, so the UR5e hand opens. The reward also changes to take into account the distance between the object and the starting pose of the GEN3 _d_ TGT following (7). Hence, the objective of this phase is to take the object to the starting pose of the GEN3. 



where _α_ = 12 is the weight for the manipulation phase. Moreover, when the agent changes to this phase or reaches the target, it receives a bonus. 

The final reward function remain as (8), involving all phases and modifiers. 



where **1** G _∈{_ 0 _,_ 1 _}_ indicates whether the agent has already grasped the object or not. 

## _C. Distance calculation methods_ 

We need to calculate the distances between poses in the environment to compute the rewards. When dealing with 

poses, it is important to define precise metrics that reflect not only translational distances but also orientation ones. For this reason, we use and compare several representations according to their formulation: dual quaternion, translation along with Euler angles, and homogeneous transformation matrices. 

_1) Dual Quaternions:_ Given two dual quaternions **ˆq1** and **ˆq2** , we compute the difference transformation between them, noted as **ˆq** diff, using the corresponding formula in Table I. This difference **ˆq** diff is the identity element **I**<sup>**ˆ**</sup> when they represent the same pose. Then, **ˆq** diff _−_ **I**<sup>**ˆ**</sup> _≈_ 01 _×_ 8 if both transformations are the same. In this regard, we calculate the distance between frames using dual quaternions using (9) as presented in [16]. In this work, we propose this reward function to perform the object handover task. 



where _||·||_ 2 is the second norm of all elements of **ˆq** diff _−_ **I**<sup>**ˆ**</sup> . _2) Euler Angles:_ Considering two sets of Euler angles _e_ 1 and _⃗ e_ 2 in the _XYZ_ convention with their corresponding Euclidean translations _⃗ t_ 1 and _⃗ t_ 2, we calculate the distance using this representation applying (10), extended from [17]. 



where _ψ_ = 2 _._ 1 and _µ_ = 0 _._ 32 are scaling factors, so the magnitude of the distance in translation and rotation is similar due to differences in units. 

_3) Homogeneous Transformation Matrices:_ The poses are represented in homogeneous transformation matrices as _<u>T</u>_ 1 and _<u>T</u>_ ~~2~~<sup>being</sup><sup>_<u>T</u>_</sup> = [ _R_ 3 _×_ 3 _t_ ; 01 _×_ 3 1], with _R_ 3 _×_ 3 _∈ SO_ (3) as the rotation matrix and _⃗ t ∈_ R<sup>3</sup> as the Euclidean translation vector. Consequently, we obtain the distance by separating the translation and rotation parts from the elements as shown in (10). Therefore, we compute the orientation component using (11), which corresponds to the relative angle between the two rotation matrices. 



As a result, the final distance consists of the addition of the rotation and translation components, as shown in (12). 



where _ψ_ = 2 _._ 1 and _β_ = 0 _._ 32 are scaling factors to normalize the distances so the magnitudes are similar. 

## V. EXPERIMENTS 

We now present several experiments to evaluate the performance of the agents produced by all the proposed reward functions, as well as to test the robustness of the system to novel objects. Specifically, we investigate the following questions: 

- Can we use RL to train an object handover policy using two robotic arms equipped with multi-finger hands? 



Fig. 5. Average reward for all the agents trained for the object handover task using different reward functions: DQ (blue), EULER (red), MATRIX (green). The DQ agent shows the higher reward values, followed by the EULER and MATRIX agents. 

- How accurate and robust is the trained policy to seen and novel objects in simulation? 

- Are dual quaternions more adequate to compute reward distances in _SE_ (3) than Euler or rotation matrices? 

- Is the trained policy robust enough to handle motion perturbations during the object handover? 

## _A. Simulation_ 

We performed the entire training process along with experiments on the IsaacLab simulator [18] using the Stable Baselines 3 (SB3) framework [19]. In addition, we used Proximal Policy Optimization (PPO) [20] with three different seeds, using 1024 environments on a single NVIDIA A40 GPU. For each episode, we randomly reset the object position inside a cube of _±_ 0 _._ 15 m of side, as well as the orientation with a variation of _±_ 0 _._ 3 rad in roll and yaw, and _±_ 0 _._ 6 rad in pitch. 

## _B. Learning to handover an object_ 

We chose an elongated quadrangular prism as the original training object of (0 _._ 035 _×_ 0 _._ 035 _×_ 0 _._ 45) m, as shown in Fig. 2. The single object training aims to reduce computational resources and to assess how the policy performs under unseen objects in this setup. The training results in terms of the average reward are shown in Fig. 5. 

The MATRIX agent was unable to learn the task correctly, collapsing with a constant reward near zero. A possible reason for this issue may be the angle representation of the angle-vector to compute rotational distances. During training, there might be cases in which the observations were similar but the _θ_ diff for each observation was not. In these cases, the rotation vector was different as the angle remained the same. This can generate ambiguity when the policy obtained the actions. Thus, we did not consider this agent for the next experiments. 

In contrast, the EULER agent learned faster to perform the task successfully compared to the DQ agent, but the reward became constant while the DQ agent continued to learn. Specifically, the EULER agent exploited the reward bonuses for grasping the object, thereby trying to reach those stages of the task quickly to increase the reward. However, 









<!-- Start of picture text -->
(a) Success. (b) Indetermination. (c) Failure.<br><!-- End of picture text -->

Fig. 6. Graphical description of the different cases contemplated during the experiments to evaluate the object handover. The success case is a correct handover without collision or falling. During the indetermination case, the object is clipped through the UR5e hand. The failure case happens when the object falls during handover. 

this behavior led to an incorrect learning of the task during simulation, as explained in the following Section V-C. 

The DQ agent achieved the highest reward during the training process without stabilizing, indicating that the agent would collect an even higher reward if the training continued. The best results obtained by the DQ agent may be due to the ability of the proposed reward function to calculate the rotation differences or distances more accurately. 

Finally, we can answer the first question by saying that RL can be used to learn the dexterous object handover task. However, we observed that the results are highly dependent on the representation used to compute the rotation distances in the reward function, with Euler angles and dual quaternions being able to solve the task. 

## _C. Success rate with seen and novel objects_ 

We used the following metrics to measure the success rate during the experimentation (see Fig. 6). 

- **Success** (Succ.): the robot grasped and manipulated the object correctly. 

- **Indetermination** (Ind.): indicates that, although the robot manipulated the object correctly, there are bugs during the episode because of failures of the simulator to resolve collisions. Therefore, in a real environment, we would not consider the grasp an absolute success. 

- **Total Success** (Total Succ.): the combination of indetermination and success cases. 

- **Fail** : indicates object falling during the episode. 

We selected the best agents for each case to evaluate the trained policies using the same object as during training. The results in Table II show the performance for a total of 100 episodes in each case. The DQ agent achieved a total success rate of 91%, while the EULER agent obtained 83%. These results are an improvement of nearly 10% from the DQ agent with respect to the EULER agent, although both have a considerable number of indeterminate cases. During tests, inconsistencies in the simulation may be causing movements that made the object clip through the UR5e hand, snatching the object out of its hand instead of grasping and taking it with subtlety. Furthermore, the EULER agent collided with the UR5e robot frequently, causing imprecisions during the episode that led to cases of indetermination. 

The objective of the following experiments is to test the robustness of the agents to different types of unseen 

### TABLE II 

SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%) WHEN EVALUATING WITH THE PRISM USED DURING TRAINING. THE DQ AGENT ACHIEVED THE HIGHEST TOTAL SUCCESS VALUE COMPARED TO THE EULER AGENT. THE BEST RESULTS ARE IN BOLD. 

|Agent|Suc. (%)|Ind. (%)|Total<br>Succ. (%)|Fail (%)|
|---|---|---|---|---|
|**DQ**|59|32|**91**|9|
|**EULER**|17|66|83|17|



object morphologies. The new objects are a short prism of dimension (0 _._ 035 _×_ 0 _._ 035 _×_ 0 _._ 35) m, a cylinder of radius 0 _._ 019 m and length of 0 _._ 45 m, and a short cylinder with the same radius and a length of 0 _._ 35 m. In Table III the success rates for each agent with each object are shown. 

When testing with the short prism, the DQ and EULER agents obtained a total success rate of 94% and 92%, respectively, which are higher rates with respect to the previous experiment. The smaller size of the object may be causing a more precise and stable grasp because the robot is approaching better the grasp frame. Although they have similar total success rates, the EULER agent obtained many more cases of indetermination owing to the same reasons as when testing with the original prism. Regarding the results with respect to the cylinder objects in Table III, the circular shape of its surface can cause the orientation of the object to slightly vary inside the UR5e hand. This rotates the target frame to unseen poses, leading to a lower success rate for all agents with 87% and 84% for the DQ and EULER. When testing with the shorter version of the cylinder, a success rate of 90% and 86% is obtained for the DQ and EULER agent, respectively. It is relevant to consider that both agents obtained around 20% less indetermination cases with the shorter version of the cylinder. 

Therefore, to respond to the second question, we can confirm that the trained policy is accurate when evaluating with objects from the training distribution and is also robust to objects from another distribution. Specifically, the best results are achieved when manipulating short rectangular objects. 

## _D. Distance minimization with dual quaternions_ 

The objective of these experiments is to test how precise the trajectory followed by the agent is from the starting point to the target frame of the object. We conducted a total of 10 successful experiments for each agent with the different objects proposed. During those, we collected how the distance to the object frame is minimized. In Fig. 7, all three minimization cases are shown for both agents, confirming the results in Tables II and III. 

For the DQ agent, we calculated the mean distances following (9) in each step until the target pose is reached. Given two frames in space, we obtained the translation distance by applying _||t⃗_ 1 _−⃗t_ 2 _||_ 2, which represents the Euclidean distance between two poses. On the other hand, we calculated the rotational distance using _||P_ ( **ˆq** diff _−_ **I**<sup>**ˆ**</sup> ) _||_ 2, which represents the rotation term of the dual quaternion difference of both 

### TABLE III 

SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%) WHEN EVALUATING WITH THE OBJECTS OUT OF THE TRAINING DISTRIBUTION. NOTE THAT THE DQ AGENT ACHIEVED THE HIGHER TOTAL SUCESS VALUE COMPARED TO THE EULER AGENT. THE BEST RESULTS ARE IN BOLD. 

|**Short**<br>**Prism**<br>|**Cylinder**<br>**Short**<br>**Cylinder**<br><br>|
|---|---|
|Ttl|Ttl<br>Ttl|
|Agent<br>Succ. (%)<br>Ind. (%)<br>oa<br>Succ. (%)<br>|Fail (%)<br>Succ. (%)<br>Ind. (%)<br>oa<br>Succ. (%)<br>Fail (%)<br>Succ. (%)<br>Ind. (%)<br>oa<br>Succ. (%)<br>Fail (%)|
|**DQ**<br>69<br>25<br>**94**|6<br>41<br>46<br>**87**<br>13<br>55<br>35<br>**90**<br>10|
|**EULER**<br>32<br>60<br>92|8<br>8<br>76<br>84<br>16<br>25<br>61<br>86<br>14|
|(a) Global distance in Dual Quaternions for the<br>DQ agent.|(b) Euclidean Translation for the DQ agent.<br>(c) Rotation Distance in Dual Quaternions for the<br>DQ agent.|
|(d) Global distance in Translation + Euler for the<br>EULER agent.|(e) Euclidean Translation for the EULER agent.<br>(f) Rotation Distance for the EULER agent.|



Fig. 7. Distance minimization of the agents for all selected objects. The DQ agent showed a greater minimization of the rotation distance than the EULER agent, which maximized it in most cases. 

poses. Alternatively, we computed the global distance for the EULER agent using (10), while we extracted the translational and rotational distances from the respective terms of the addition in that equation. 

Both policies minimized the global distance from the target (Fig. 7a and 7d). However, the DQ one made it smoother than the EULER. Even though both agents were able to minimize the translational distance (Fig. 7b and 7e), the EULER one failed to orient the end effector to the target rotation as shown in Fig. 7f. The DQ agent minimized the rotational poses from the starting pose around 43% on average. Far from reducing it, the EULER one increased it. This fact may be one of the reasons why the latter obtains more indetermination cases during the tests. 

Answering the third question, we state that dual quaternions are more adequate to calculate the rewards on _SE_ (3) for approach trajectories. The distance minimized by the agents trained with this representation is lower and smoother than the obtained using the EULER representation. 

handover. The objective of these is to test the robustness of the policy to unseen states where there is movement of the target. In these experiments, the UR5e is moving in a random direction within the limits where the agent was trained. The velocity is set to be 40% lower than GEN3 so it can reach it. Specifically, at 0 _._ 03 m/s for the linear velocity and 0 _._ 16 rad/s for the angular velocity. The results are shown in Table IV. All the total success rates decreased around 13.68% on average due to movement during the task in our setup. The best results are still achieved by the DQ agent when manipulating the original or short prism with 81% success compared to a 78% from the EULER. The DQ agent performed better with all objects except the cylinder, where the EULER obtained 77% compared to a 71% of total success from the DQ. The movement of the UR5e caused the agent to lose precision in the task, although it still tried to perform the handover even taking advantage of the simulation problems. 

## _E. Success rate under perturbations_ 

When dealing with object handover in the real world, it is common to have perturbations on the object pose from the giver agent. For this reason, we conducted some experiments where the handing robot (UR5e) is moving during the object 

As a result and answering the fourth question, our policies are robust to movement of the object during the handover. In particular, the DQ agent obtained a higher success rate with almost all proposed objects. 

TABLE IV 

SUCCESS RATE OF THE AGENTS EXPRESSED AS A PERCENTAGE (%) WHEN EVALUATING THE TRAINED POLICIES UNDER PERTURBATIONS. THE DQ AGENT SHOWED HIGHER TOTAL SUCCESS VALUES FOR 3 OUT OF THE 4 OBJECTS COMPARED TO THE EULER ONE. THE BEST RESULTS ARE IN BOLD. 

||**Prism**|**Short**<br>**Prism**|**Cylinder**||**C**|**Short**<br>**ylinder**||
|---|---|---|---|---|---|---|---|
|Agent|Succ. (%) Ind. (%)<br>Total<br>Succ. (%) <sup>Fail (%)</sup>|Succ. (%) Ind. (%)<br>Total<br>Succ. (%) <sup>Fail (%)</sup>|Succ. (%) Ind. (%)<br>Total<br>Succ. (%|) <sup>Fail (%</sup>|<sup>)</sup><br>Succ. (%) Ind. (|%)<br>Total<br>Succ. (%|) <sup>Fail (%)</sup>|
|**DQ**|46<br>35<br>**81**<br>19|55<br>26<br>**81**<br>19|37<br>34<br>71|29|12<br>65|**77**|23|
|**EULER**|11<br>67<br>78<br>22|21<br>51<br>72<br>28|12<br>65<br>**77**|23|13<br>59|72|28|



## VI. CONCLUSIONS 

In this work, we evaluate in simulation an RL policy to perform dexterous object handover with a multi-finger hand. We trained the policy by using the PPO algorithm, a single quadrangular prism as the handover object, and a variety of random poses to reset the object differently at the beginning of each episode. Experimental results demonstrate that the policy trained with the quadrangular prism object is robust to other objects with similar geometric shapes and also with different sizes. Furthermore, it is shown that the dual quaternion representation can minimize the orientation of the hand with respect to the target orientation of the object, while other representations failed. Finally, the trained policy was evaluated under perturbations during the object handover, showing only minimal decrease in performance after the same number of experiments. 

While this work is a promising first step towards dexterous object handover, it is limited by several factors: First, a single object is employed for the training process, thereby diminishing the generalization capabilities of the policy. Second, the proposed policy does not incorporate any kind of visual perception; it is only extracting the object pose from the simulator. This is very important to transfer the trained policy from simulation to the real-world setup. Finally, imperfections in the physics engine limit the training of the policy by enabling undesired grasping behaviors that may not occur in the real-world setup. Future work will look into training not only the receiving robot, but also the handing robot within the RL framework used, as well as looking into the generalization of the policy to a wider set of objects. 

Moreover, it is planned to transfer the policy to realworld scenarios. In this way, it could be assessed how the policy behaves under noisy observations provided by sensors in real environments. By doing so, it will remove the indetermination cases present during the simulation and test the trained policies with humans as givers. 

## REFERENCES 

- [1] V. Ortenzi, A. Cosgun, T. Pardi, W. P. Chan, E. Croft, and D. Kuli´c, “Object handovers: A review for robotics,” _IEEE Transactions on Robotics_ , vol. 37, no. 6, pp. 1855–1873, 2021. doi: 10.1109/TRO.2021.3075365 

- [2] D. Haonan, Y. Yifan, L. Daheng, and W. Peng, “Human–robot object handover: Recent progress and future direction,” _Biomimetic Intelligence and Robotics_ , vol. 4, no. 1, p. 100145, 2024. doi: 10.1016/j.birob.2024.100145 

- [3] M. Costanzo, G. D. Maria, and C. Natale, “Handover control for human-robot and robot-robot collaboration,” _Frontiers in Robotics and AI_ , vol. 8, 2021. doi: 10.3389/frobt.2021.672995 

- [4] Y. Li, C. Pan, H. Xu, X. Wang, and Y. Wu, “Efficient bimanual handover and rearrangement via symmetry-aware actor-critic learning,” in _IEEE International Conference on Robotics and Automation (ICRA)_ , 2023. doi: 10.1109/ICRA48891.2023.10160739 

- [5] B. Huang, Y. Wang, X. Yang, Y. Luo, and Y. Li, “3d-vitac: Learning fine-grained manipulation with visuo-tactile sensing,” in _8th Annual Conference on Robot Learning_ , 2024. doi: 10.48550/arXiv.2410.24091 

- [6] Z. Wang, J. Chen, Z. Chen, P. Xie, R. Chen, and L. Yi, “Genh2r: Learning generalizable human-to-robot handover via scalable simulation, demonstration, and imitation,” in _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2024, pp. 16 362–16 372. doi: 10.1109/CVPR52733.2024.01548 

- [7] D. Frau-Alfaro, S. T. Puente, I. De Loyola P´aez-Ubieta, and E. Velasco-S´anchez, “Robotic approach trajectory using reinforcement learning with dual quaternions,” in _7th Iberian Robotics Conference (ROBOT)_ , 2024. doi: 10.1109/ROBOT61475.2024.10796878 

- [8] W. He, J. Li, Z. Yan, and F. Chen, “Bidirectional human–robot bimanual handover of big planar object with vertical posture,” _IEEE Transactions on Automation Science and Engineering_ , pp. 1180–1191, 2022. doi: 10.1109/TASE.2020.3043480 

- [9] S. E. Ovur and Y. Demiris, “Naturalistic robot-to-human bimanual handover in complex environments through multi-sensor fusion,” _IEEE Transactions on Automation Science and Engineering_ , pp. 3730–3741, 2024. doi: 10.1109/TASE.2023.3284668 

- [10] B. Huang, Y. Chen, T. Wang, Y. Qin, Y. Yang, N. Atanasov, and X. Wang, “Dynamic handover: Throw and catch with bimanual hands,” in _7th Annual Conference on Robot Learning_ , 2023. doi: 10.48550/arXiv.2309.05655 

- [11] T. Lin, K. Sachdev, L. Fan, J. Malik, and Y. Zhu, “Sim-toreal reinforcement learning for vision-based dexterous manipulation on humanoids,” _arXiv preprint arXiv:2502.20396_ , 2025. doi: 10.48550/arXiv.2502.20396 

- [12] Y. Li, “Deep reinforcement learning: An overview,” _arXiv preprint arXiv:1701.07274_ , 2017. doi: 10.48550/arXiv.2412.05265 

- [13] M. A. Wiering and M. Van Otterlo, “Reinforcement learning,” _Adaptation, learning, and optimization_ , vol. 12, no. 3, p. 729, 2012. 

- [14] Y.-B. Jia, “Dual quaternions,” _Iowa State University: Ames, IA, USA_ , 2013. [Online]. Available: https://faculty.sites.iastate.edu/jia/ files/inline-files/dual-quaternion.pdf 

- [15] F. Thomas, “Approaching dual quaternions from matrix algebra,” _IEEE Transactions on Robotics_ , 2014. doi: 10.1109/TRO.2014.2341312 

- [16] E. P. Velasco-S´anchez, L. F. Recalde, G. Li, F. A. Candelas-Herias, S. T. Puente-Mendez, and F. Torres-Medina, “Dualquat-loam: Lidar odometry and mapping parameterized on dual quaternions,” _Robotics and Autonomous Systems_ , 2025. doi: 10.1016/j.robot.2025.105009 

- [17] A. Iriondo, E. Lazkano, A. Ansuategi, A. Rivera, I. Lluvia, and C. Tub´ıo, “Learning positioning policies for mobile manipulation operations with deep reinforcement learning,” _International journal of machine learning and cybernetics_ , 2023. doi: 10.1007/s13042-02301815-8 

- [18] M. Mittal, C. Yu, Q. Yu, J. Liu, N. Rudin, D. Hoeller, J. L. Yuan, R. Singh, Y. Guo, H. Mazhar, A. Mandlekar, B. Babich, G. State, M. Hutter, and A. Garg, “Orbit: A unified simulation framework for interactive robot learning environments,” _IEEE Robotics and Automation Letters_ , 2023. doi: 10.1109/LRA.2023.3270034 

- [19] A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and N. Dormann, “Stable-baselines3: Reliable reinforcement learning implementations,” _Journal of Machine Learning Research_ . [Online]. Available: http://jmlr.org/papers/v22/20-1364.html 

- [20] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” _arXiv preprint arXiv:1707.06347_ , 2017. doi: 10.48550/arXiv.1707.06347 

