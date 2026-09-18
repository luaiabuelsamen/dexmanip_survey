Preprint. 

# LEARNING DIVERSE BIMANUAL DEXTEROUS MANIPULATION SKILLS FROM HUMAN DEMONSTRATIONS 

### **Bohan Zhou** 

School of Computer Science Peking University zhoubh@stu.pku.edu.cn 

### **Haoqi Yuan** 

School of Computer Science Peking University yhq@pku.edu.cn 

### **Yuhui Fu** 

School of Computer Science Peking University fooyuhuii@gmail.com 

**Zongqing Lu**<sup>_†_</sup> School of Computer Science Peking University BAAI zongqing.lu@pku.edu.cn 

## ABSTRACT 

Bimanual dexterous manipulation is a critical yet underexplored area in robotics. Its high-dimensional action space and inherent task complexity present significant challenges for policy learning, and the limited task diversity in existing benchmarks hinders general-purpose skill development. Existing approaches largely depend on reinforcement learning, often constrained by intricately designed reward functions tailored to a narrow set of tasks. In this work, we present a novel approach for efficiently learning diverse bimanual dexterous skills from abundant human demonstrations. Specifically, we introduce **BiDexHD** , a framework that unifies task construction from existing bimanual datasets and employs teacherstudent policy learning to address all tasks. The teacher learns state-based policies using a general two-stage reward function across tasks with shared behaviors, while the student distills the learned multi-task policies into a vision-based policy. With BiDexHD, scalable learning of numerous bimanual dexterous skills from auto-constructed tasks becomes feasible, offering promising advances toward universal bimanual dexterous manipulation. Our empirical evaluation on the TACO dataset, spanning 141 tasks across six categories, demonstrates a task fulfillment rate of **74.59%** on trained tasks and **51.07%** on unseen tasks, showcasing the effectiveness and competitive zero-shot generalization capabilities of BiDexHD. For videos and more information, visit our project page. 

## 1 INTRODUCTION 

Bimanual manipulation is crucial and beneficial. Humans use both hands to do manipulations like using scissors, tying shoelaces, or operating kitchen utensils. The ability to manipulate objects with two hands is fundamental for everyday tasks, because with both hands, we can not only do some “symmetry" collaborative tasks like carrying a heavy box with two hands, but also do “asymmetry” tasks (Liu et al., 2024a) like twisting a bottle cap, which means one hand acts as an auxiliary hand for stabilizing objects and the other acts as an operator. 

With the rapid development of embodied artificial intelligence, robotic bimanual dexterous manipulation is getting more and more important in manufacturing, healthcare, agriculture, construction, and tertiary industry (Zhang et al., 2024b). This emphasizes the effective use of tools or manipulations over objects that are deformable or of irregular shapes, overcoming the limitations of low-DOF end-effectors like grippers. Moreover, it addresses complicated human-like hand-object interaction and collaboration. Despite its significance, achieving proficient bimanual manipulation remains a substantial challenge because it severely struggles with the high-dimensional action space. While a 

> _†_ Corresponding author. 

1 

Preprint. 

line of previous work (Grannen et al., 2023; Yu et al., 2024; Kataoka et al., 2022; Liu et al., 2024a) primarily focuses on bimanual manipulation with grippers, there is still much left to explore for bimanual manipulation with dexterous hands. Previous attempts to solve bimanual dexterous manipulation tasks are mainly based on reinforcement learning (RL) (Lin et al., 2024; Huang et al., 2023; Zhang et al., 2024a). However, they require intricate reward designs tailored to specific manuallydesigned tasks. Therefore, these approaches lack scalability and generalizability to a broader range of tasks. Recent research (Sindhupathiraja et al., 2024; Fu et al., 2024; He et al., 2024) has advanced robotic bimanual dexterous manipulation through teleoperation. Nevertheless, human intervention is inevitable. We would ask a question: 

### **_“Can we learn diverse bimanual dexterous manipulation skills in a unified and scalable way?”_** 

Our solution is to use human demonstrations. Compared to robotic demonstrations, human demonstrations are relatively easier to obtain with haptic gloves or MoCap devices rather than deploying a trained policy, and contain much more physically compliant and human-aligned behavior. In this paper, we propose a novel approach to learn diverse bimanual dexterous manipulation skills from human demonstrations. Upon this setting, we propose **BiDexHD** , a unified and scalable framework to automatically turn a human bimanual manipulation dataset into a series of tasks in the simulation and conduct effective policy learning. 

BiDexHD does not depend on manually-designed tasks or pre-defined tasks in existing benchmarks. Instead, it consistently constructs feasible tasks from any bimanual manipulation trajectory. Furthermore, we are not required to design specific rewards for each task but instead utilize a unified reward function for reinforcement learning followed by policy distillation. In a word, BiDexHD breaks the bottleneck of limited tasks and manual designs, which is significant to the further development of general-purpose bimanual dexterous manipulation. Though promising, several challenges must be addressed to fully realize this. It is essential to figure out how to accurately mimic fine-grained bimanual behaviors from human demonstrations and avoid collisions and disturbances while encouraging smooth trajectories and synchronous collaboration between both hands. To address this, we carefully design a general two-stage reward function to assign curricula for RL training. 

To sum up, our key contributions can be summarized as follows: 

- We formalize the problem of learning bimanual dexterous skills from human demonstrations as a preliminary attempt towards universal bimanual skills. 

- We propose **BiDexHD** , a unified and scalable reinforcement learning framework for learning diverse bimanual dexterous manipulation from human demonstrations, advancing the capabilities of robots in performing bimanual cooperative tasks. 

- We evaluate BiDexHD across 141 auto-constructed tasks over 6 categories from the TACO (Liu et al., 2024b) dataset and demonstrate the superior training performance and competitive generalization capabilities of BiDexHD. 

## 2 RELATED WORK 

### 2.1 BIMANUAL DEXTEROUS MANIPULATION 

In recent years, the robotics community has increasingly focused on dexterous manipulation due to its remarkable flexibility and human-like dexterity. Researchers have developed methods using dexterous hands for tasks such as in-hand manipulation (Arunachalam et al., 2023; Yin et al., 2023; Handa et al., 2023; Qi et al., 2023; Chen et al., 2023; 2022), grasping (Xu et al., 2023; Wan et al., 2023; Qin et al., 2023a; Ye et al., 2023; Qin et al., 2022a), and manipulating deformable objects (Bai et al., 2016; Ficuciello et al., 2018; Li et al., 2023; Hou et al., 2019). However, most existing work focuses on a single dexterous hand, revealing the potential of bimanual dexterity. In fact, for humans, bimanual collaboration takes place frequently in daily life such as riding, carrying heavy objects, and using tools. There are heterogeneous research directions towards bimanual dexterous manipulation. Some researchers attempt to settle down to specific tasks via reinforcement learning. For example, recent work (Lin et al., 2024) investigates twisting lids with two multi-fingered hands, DynamicHandover (Huang et al., 2023) explores throwing and catching, and ArtiGrasp (Zhang et al., 

2 

Preprint. 

2024a) focuses on a few grasping and articulation tasks. Gbagbe et al. (2024) leveraged large language models to design a system for bimanual robotic dexterous manipulation, while Wang et al. (2024) proposed to solve bimanual grasping via physics-aware iterative learning and prediction of saliency maps. A recent work (Gao et al., 2024) adopts keypoints-based visual imitation learning to learn bimanual coordination strategies. Unlike existing work, in this paper, we offer a general solution to learn from bimanual demonstrations by designing a unified reward function to learn a state-based policy via reinforcement learning and distilling it into a vision-based policy. 

### 2.2 LEARNING DEXTERITY FROM HUMAN DEMONSTRATIONS 

As a sample-efficient data-driven way, learning from human demonstrations has been proven successful in robot learning (Jia et al., 2024; Mandlekar et al., 2023; Odesanmi et al., 2023). Compared with learning dexterity via reinforcement learning which is notoriously challenging for policy learning due to the high degrees of freedom and the necessity of manually designing task-specific reward functions, learning complex dexterous behaviors from diverse accessible human demonstrations (Smith et al., 2019; Schmeckpeper et al., 2020; Shao et al., 2021) is a more stable and scalable approach. A line of previous studies (Arunachalam et al., 2023; Mandikal & Grauman, 2021; Sivakumar et al., 2022; Qin et al., 2022b; Mandikal & Grauman, 2022; Liu et al., 2023; Shaw et al., 2023b; Chen et al., 2024) explicitly leverages human demonstrations to facilitate the acquisition of dexterous manipulation skills mainly by human-robot-arm-hand retargeting and imitation learning. However, these studies predominantly focus on single-hand manipulation and are often limited to tasks such as in-hand manipulation (Arunachalam et al., 2023) or video-conditioned teleoperation (Sivakumar et al., 2022). With the recent advent of diverse and comprehensive human bimanual manipulation datasets (Zhan et al., 2024; Liu et al., 2024b; Fan et al., 2023; Razali & Demiris, 2023) which naturally provide a rich resource for high-quality posture sequences of dual hands and bimanual interaction with diverse real objects, a lot of bimanual manipulation tasks can be automatically defined. Thus, in this work, we aim to address more challenging and general bimanual dexterous skill learning purely based on automatically constructed tasks from human demonstrations. 

## 3 PRELIMINARIES 

### 3.1 TASK FORMULATION 

**Dec-POMDP** . We formulate each bimanual manipulation task as a decentralized partially observable Markov decision process (Dec-POMDP). The Dec-POMDP can be represented by the tuple _Z_ = ( _N , M, S,_ **_O_** _,_ **_A_** _, P, R, ρ, γ_ ). Dual hands with arms are separated as _N_ agents, which is represented by set _M_ . The proprioception of robots and the information about objects are initialized at _s_ 0 _∈ S_ according to the initial state distribution _ρ_ ( _s_ 0). At each time step _t_ , the state is represented by _st_ , and the _i_ -th agent receives an observation _o_<sup>_i_</sup> _t_<sup>_∈_</sup><sup>**_O_**based on</sup><sup>_st_.Subsequently, the policy of the</sup> _i_ -th agent, _πi ∈_ **Π** , takes _o_<sup>_i_</sup> _t_<sup>as input and outputs an action</sup><sup>_ai_</sup> _t_<sup>_∈Ai_.The joint action of all agents is</sup> denoted by **_a_** _t ∈_ **_A_** , where **_A_** = _A_<sup>1</sup> _× A_<sup>2</sup> _× · · · A_<sup>_N_</sup> . The state transits to the next state according to the transition function _st_ +1 _∼ P_ ( _st_ +1 _|st,_ **_a_** _t_ ). After this, the _i_ -th agent receives a reward _rt_<sup>_i_based</sup> on the reward function _R_ ( _st,_ **_a_** _t_ ). The objective is to find the optimal policy **_π_** that maximizes the expected sum of rewards E **_π_** [<sup>�</sup><sup>_T_</sup> _t_ =0<sup>_−_1</sup><sup>_γt_�</sup> _i_<sup>_N_</sup> =1<sup>_r_</sup> _t_<sup>_i_] over an episode with</sup><sup>_T_time steps, where</sup><sup>_γ_is the</sup> discount factor. 

**Environment Setups** . The leftmost subgraph in Figure 2 illustrates the setups for each bimanual manipulation task in IsaacGym (Makoviychuk et al., 2021). In general, there are a tool and a target object initialized on a table. _N_ = 2 robotic arms are installed in front of the table, with left LEAP Hand (Shaw et al., 2023a) mounted on the left arm and right hand on the right arm. The right hand reaches for the tool, and the left hand targets the object. Both hands coordinate to simultaneously move, pick up, and manipulate the objects above the table. Note that our method applies to all dexterous hand embodiments. The observation space **_O_** contains robot proprioception and object information. The left and right policies both output 22 joint angles normalized to [ _−_ 1 _,_ 1], and the robots are controlled via position control. See more details in Appendix B.4. 

**Dataset Preparation** . A human bimanual manipulation dataset consists of _M_ trajectories _D_ = _{τ_<sup>1</sup> _, τ_<sup>2</sup> _, . . . , τ_<sup>_M_</sup> _}_ , each of which describes a human using a tool with his right hand to manipulate a target object with his left hand. The behavior of each trajectory can be recapped with 

3 

Preprint. 



<!-- Start of picture text -->
Phase 1: Task Construction Phase 2: State-Based Multi-Task Reinforcement Learning Phase 3: Vision-Based Policy Distillation<br>TACO Dataset Isaac Gym<br>① ② Robotic Proprioception<br>Dust<br>③ ④ K-step Future Positions<br>Pose SequencesHuman-Object Demonstration<br>Put out<br>Object-Tool Point Clouds<br>① ② Supervise Bimanual<br>Tool-ObjectMesh Pairs Bimanual TasksConstructed  Pour in Simulation ③ ④ Expert PoliciesMulti-task  ManipulationDexterous<br>DAgger<br>Trajectory Tracking  Stage 2:<br>Simulation Alignment  Stage 1:<br><!-- End of picture text -->

**Figure 1:** The three-phase framework, BiDexHD, unifies constructing and solving tasks from human bimanual datasets instead of existing benchmarks. In phase one, BiDexHD constructs each bimanual task from a human demonstration. In phase two, BiDexHD learns diverse state-based policies from a generally designed two-stage reward function via multi-task reinforcement learning. A group of learned policies are then distilled into a vision-based policy for inference in phase three. 

a triplet (action, tool, object). Any triplet belongs to a union _U_ = _V ×_ Ω _×_ Ω, where Ω denotes the set of all objects and tools, and _V_ denotes the set of all human actions. According to different behaviors depicted in _V_ , we can split all the tasks into _|V|_ categories. Each trajectory _τ_<sup>_i_</sup> = _{_ **h**<sup>tool</sup> _,_ **h**<sup>object</sup> _,_ ˆ **x**<sup>tool</sup> _t ,_ ˆ **q**<sup>tool</sup> _t ,_ ˆ **x**<sup>object</sup> _t ,_ ˆ **q**<sup>object</sup> _t ,_ Θ<sup>left</sup> _t_<sup>_,_Θ</sup> _t_<sup>right</sup> _}_<sup>_i_</sup> _t_ :1 _..N_<sup>involves a pair of meshes of the tool</sup> and object from a object mesh set **h**<sup>tool</sup> _,_ **h**<sup>object</sup> _∈H_ , _N_ -step position **x** _∈_ R<sup>3</sup> and orientation **q** _∈_ R<sup>4</sup> sequence of the tool and the object, and the pose sequence of hands described in MANO (Romero et al., 2017) parameters Θ. 

### 3.2 TEACHER-STUDENT LEARNING 

It is well known (Chen et al., 2022; 2023) that directly learning a multi-task vision-based policy for dexterous hands is extremely challenging. A more popular and scalable approach is teacher-student learning (Wan et al., 2023), which not only simplifies the complexity of multi-DoF robot multitask learning but also enhances the efficiency of point cloud-based policy learning. In the teacher learning phase, a single state-based policy is first trained via reinforcement learning, leveraging privileged information to solve multiple similar tasks. Once trained, multiple teacher policies can effectively tackle all tasks. In the student learning phase, a vision-based student policy is distilled from the teacher policies. A key distinction between teacher and student observations is how object information is represented. While the teacher’s observation space includes precise details about an object’s position, orientation, and linear and angular velocities, the student’s observation relies on point clouds consisting of _P_ sampled points from the object’s surface mesh. In this way, the learned student policy is promising to be deployed in real world to deal with multiple tasks provided that the real point clouds can be constructed from real-time multi-view RGB-D camera system. 

## 4 LEARNING BIMANUAL DEXTERITY FROM HUMAN DEMONSTRATIONS 

### 4.1 OVERVIEW 

As illustrated in Figure 1, we propose a scalable three-phase framework. In the first phase, we parallelize the construction of Dec-POMDP bimanual tasks from a human bimanual manipulation dataset within IsaacGym (Makoviychuk et al., 2021). After task initialization, the subsequent two phases adopt a teacher-student policy learning framework. Following the approach of Chen et al. (2022; 2023); Wan et al. (2023), we utilize Independent Proximal Policy Optimization (IPPO) (De Witt et al., 2020) during the second phase to independently train state-based teacher policies for constructed bimanual dexterous tasks in parallel. Each expert focuses on a subset of tasks that require similar behaviors. In the final phase, the teacher policies are distilled into a vision-based student policy, integrating skills across related tasks. 

4 

Preprint. 

### 4.2 TASK CONSTRUCTION FROM BIMANUAL DATASET 

In this work, we primarily focus on bimanual tool using tasks. Recent datasets (Liu et al., 2024b; Zhan et al., 2024; Fan et al., 2023; Razali & Demiris, 2023) capture a wide range of bimanual cooperative behaviors, involving the use of tools to manipulate objects via motion capture and 3D scanning. The rich data, including object pose trajectories and hand-object interaction postures, provides sufficient information to construct feasible bimanual tasks. The task construction process from the bimanual dataset involves data preprocessing and simulation initialization. 

**Data Preprocessing** . We extract the wrist and fingertip pose of dual hands at each timestep _{Vt_<sup>side</sup> _, Jt_<sup>side</sup> _}_ = MANO(Θ<sup>side</sup> _t_ ) _,_ side _∈{_ left, right} with MANO (Romero et al., 2017) parameters Θ = _{α, β,_ ˆ **x**<sup>w</sup> _}_ , where _α ∈_ R<sup>48</sup> _, β ∈_ R<sup>10</sup> _,_ and **x** ˆ<sup>w</sup> _∈_ R<sup>3</sup> represent hand pose, hand shape parameters, and wrist position respectively. _V ∈_ R<sup>778</sup><sup>_×_3</sup> and _J ∈_ R<sup>21</sup><sup>_×_3</sup> represent vertices and joints on a hand respectively. The quaternion of the wrist **q** ˆ<sup>w</sup> _∈_ R<sup>4</sup> is translated from axis-angle _β_ 0:3. Given that single LEAP Hand (Shaw et al., 2023a) has only four fingers, we can easily filter the corresponding positions of these _m_ = 4 fingers in _J_ , denoting them as **x**<sup>ft</sup> _∈_ R<sup>_m×_3</sup> . In the following sections, _τ_<sup>_i_</sup> is denoted as: 



**Simulation Initialization** . After data preprocessing, we can construct bimanual manipulation tasks _Γ_ = _{T_<sup>1</sup> _, ..., T_<sup>_M_</sup> _}_ in Issac Gym in parallel. For each task _T_<sup>_i_</sup> , the mesh of a tool **h**<sup>tool</sup> and a target object **h**<sup>object</sup> , along with two arms with hands are initialized with a fixed initial observation vector: 



The robot proprioception includes arm-hand joint angles and velocities, wrist poses, and fingertip positions, and object information includes object positions, orientations, linear and angular velocities, and a unique object identifier for multi-task learning. For all tasks, ( **j** _,_ **v** )0 are all reset to zero. The initial states of wrist and fingertips are calculated with forward kinematics accordingly. Except identifiers, the initial observations for all tools and target objects keep unchanged. It is worth noting that we assume the robot to be right-handed by default, _i.e._ , the left hand handles the target object and the right hand handles the tool. For brevity, the repeated notation side, obj _∈{_ (left, object),(right, tool)} is omitted in subsequent sections. 

To ensure the feasibility of each task, after initialization, we use retargeting optimizers (Qin et al., 2023b) to map human hand motions to robot hand joint angles and solve inverse kinematics (IK) to determine the robot arm joint angles based on the robot’s palm base pose. By replaying all objecthand trajectories in the simulator, we can easily identify and remove invalid tasks to build up a complete task set _Γ_ . 

### 4.3 MULTI-TASK STATE-BASED POLICY LEARNING 

In the second phase, we focus on learning a multi-task state-based policy for tasks that require similar behaviors. Broadly, these tasks can generally be divided into two stages: first, aligning the simulation state with initial _τ_ 0<sup>_i_ofatrajectory,andsecond,followingeachstepofthetrajectory.</sup> During the alignment stage, both hands should prioritize approaching their objects as quickly as possible. The left hand learns to grasp or stabilize the target object, while the right hand learns to grasp the tool. Once simulation alignment is achieved, both hands are expected to maintain their hold and follow the pre-defined trajectory derived from the human demonstration dataset to perform the manipulations in sync. The pipeline is illustrated in Figure 2. We initialize objects and robots at stage zero, finish simulation alignment at stage one, and conduct trajectory tracking at stage two via IPPO to learn state-based policies _πθ_<sup>side</sup> ( **a**<sup>side</sup> _t |o_<sup>side</sup> _t ,_ **a**<sup>side</sup> _t−_ 1<sup>) conditioning on the current observation</sup> _o_<sup>side</sup> _t_ = _{_ ( **j** _,_ **v** )<sup>side</sup> _,_ ( **x** _,_ **q** )<sup>side,w</sup> _,_ **x**<sup>side,ft</sup> _,_ ( **x** _,_ **q** _,_ **v** _,_ **w** _,_ id)<sup>obj</sup> _}_<sup>side</sup> _t_ and previously executed action **a**<sup>side</sup> _t−_ 1<sup>for</sup> dual hands. 

**Stage 1: Simulation Alignment** . The central goal of stage one is to align the state of simulation to the first step in a trajectory by moving the tool and target object from the fixed initial pose to _τ_ 0, which serves as an essential yet challenging prerequisite for subsequent trajectory tracking in stage two. Through experiments in Section 5.4, we find that it is not feasible to directly acquire 

5 

Preprint. 



<!-- Start of picture text -->
left  right<br>hand hand Approaching Reward<br>tool<br>target<br>object Lifting Reward<br>table<br>Bonus Reward Track Reward<br>Simulation Initialization Stage 0:  Simulation Alignment  Stage 1:  Trajectory Tracking  Stage 2:<br><!-- End of picture text -->

**Figure 2:** General two-stage teacher learning. For each task _T_<sup>_i_</sup> , all joint poses are initialized at zero pose and a pair of tool-object are initialized at a fixed pose at stage zero. At stage one, approaching reward _r_ appro encourages both hands to get close to their grasping centers ˆ **x** gc, and lifting reward _r_ lift along with extra bonus _r_ bonus incentivizes moving both objects to thier reference poses respectively. After simulation alignment, dual hands will manipulate objects under the guidance of tracking reward _r_ track. 

dynamic skills from static poses through imitation. Instead, we adopt reinforcement learning to develop skills like grasping, twisting and pushing. Some previous work (Luo et al., 2024; Xu et al., 2023) on grasping prefers introducing additional pre-grasp poses by estimating grasping pose upon manipulated objects. We adopt a simpler but more generalizable approach by learning skills directly from the object poses provided in the dataset. Specifically, we anchor the first timestep in the dataset as the reference timestep to establish a tool-object reference pose pair for each manipulation task. Stage one is considered complete once both the tool and the object reach the specified pose for a sustained _u_ -step duration. Rewards are carefully designed to encourage the object to be lifted above the table in reference to the filtered reference poses. The total reward consists of an approaching reward, a lifting reward, and a bonus reward. 

The approaching reward, _r_ appro, encourages both dexterous hands to approach and remain close to the object. In other words, the goal is to minimize the distance between the robot’s palm, fingertips, and the grasp center. Since functional grasping is critical for tool using, we do not simply select the geometric center of the object. Instead, we pre-compute the grasping center **x** ˆgc for each tool and object based on the dataset. Specifically, for each task, we use the human-demonstrated wrist and fingertip positions at the reference timestep– **x** ˆ<sup>lw</sup> 0<sup>_,_ˆ</sup><sup>**x**rw</sup> 0<sup>_,_ˆ</sup><sup>**x**lft</sup> 0<sup>_,_ˆ</sup><sup>**x**rft</sup> 0<sup>–as anchor points.We then uniformly</sup> sample 1024 points from the surface of the object mesh **h**<sup>tool</sup> _,_ **h**<sup>object</sup> to form a representative point set _P_ and compute the average grasp center based on the top _L_ = 50 nearest points. _r_ appro penalizes the distance between the wrist, fingertips, and the grasp center, and is defined as 



The lifting reward _r_ lift encourages holding objects tightly in hands and lifting to desired reference poses. As long as the lifting conditions are satisfied, the robots receive a lifting reward _r_ lift composed of a non-negative linear position reward and a negative quaternion distance reward, 



Here, **x**<sup>object</sup> 0 and **x**<sup>tool</sup> 0 respectively represent the initial positions of the target object and tool in the simulator, while **x** ˆ0 denotes the first reference position in a human demonstration. 

The bonus reward _r_ bonus incentivizes the target object or the tool to reach and finally stay at their reference poses, which lays a foundation for the second manipulation stage. _r_ bonus becomes positive only when the distance between an object’s current position and its reference position becomes lower than _ε_ succ. Stage one is considered successful only if both _r_ bonus<sup>leftand</sup><sup>_r_</sup> bonus<sup>rightare positive for at least</sup><sup>_u_</sup> 

6 

Preprint. 

consecutive steps. Thus, the bonus reward _r_ bonus is defined as 



The total alignment reward is the linear weighted sum of the three components. 

**Stage 2: Trajectory Tracking** . Once stage one is completed, the left hand is securely holding the target object, and the right hand keeps grasping the tool at its desired reference pose. The next step is to maintain the grasp and follow a trajectory to perform the manipulation. To achieve this, we design a more fine-grained exponential reward, _r_ track, which encourages the dexterous hands to precisely track the desired positions at each timestep in a trajectory starting from the reference timestep. Assuming that human hands are more flexible than robotic hands, we introduce a constant tracking frequency _f_ , where _f_ simulation steps correspond to one step in the dataset. Let **ˆx**<sup>obj</sup> _i_ represent the position of a object at _i_ -th step in a _l_ -step human-demonstrated trajectory and **x**<sup>obj</sup> _ti_<sup>representthe</sup> object’s position at the corresponding simulation step in IsaacGym. We have _i_ = _⌈ti/f ⌉∈_ [0 _, l_ ), and the tracking reward is defined as 



We adopt IPPO to learn a unified policy from the combination of all rewards for the two stages, 



_r_ total unifies two stages of bimanual dexterous manipulation, enabling scaling up to multi-task policy learning for a wide range of constructed bimanual tasks. 

### 4.4 VISION-BASED POLICY DISTILLATION 

We employ DAgger (Ross et al., 2011), an on-policy imitation learning algorithm, to develop a vision-based policy for each task category _ν ∈V_ , under the supervision of a group of state-based teacher policies. To enhance generalization capabilities for new objects or unseen tasks, we propose transforming the student policy into a trajectory-conditioned in-context policy, denoted as _πϕ_<sup>side(</sup><sup>**a**</sup> _t_<sup>side</sup> _|_ **o**<sup>side</sup> _t ,_ **p**<sup>side</sup> _t ,_ **a**<sup>side</sup> _t−_ 1<sup>),where</sup><sup>**o**</sup><sup>_t_=</sup><sup>_{_(</sup><sup>**j**</sup><sup>_,_</sup><sup>**v**)side</sup><sup>_,_(</sup><sup>**x**</sup><sup>_,_</sup><sup>**q**)side,w</sup><sup>_,_</sup><sup>**x**side,ft</sup><sup>_,_pcobj</sup><sup>_}t_,</sup><sup>_K_-stepfuturepose</sup> **p**<sup>side</sup> _t ∈_ R<sup>_K×_3</sup> , and pc<sup>obj</sup> _t ∈_ R<sup>_P ×_3</sup> . Specifically, to get point clouds pc<sup>tool</sup> _t_ and pc<sup>object</sup> _t_ , we pre-sample 4096 points from the surface of **h**<sup>tool</sup> and **h**<sup>object</sup> for each task during initialization. At each timestep _t_ , a subset of points are sampled from the pre-sampled point clouds, transformed according to current object pose and added with Gaussian noise for robustness. Besides, it is important to note that during DAgger distillation, we augment traditional vision-based policy _πϕ_<sup>side(</sup><sup>**a**</sup> _t_<sup>side</sup> _|_ **o**<sup>side</sup> _t ,_ **a**<sup>side</sup> _t−_ 1<sup>) with</sup> next _K_ positions along the object’s trajectory as additional inputs. This design allows the learned policy to utilize more information about the motion of objects, such as movement direction and speed in the near future, facilitating zero-shot transfer to unfamiliar tasks or objects. Notably, we can easily mask this additional input by setting _K_ = 0. We further investigate the influence of _K_ future steps in Section 5.4. The whole teacher-student training process is summarized in Appendix A. More implementation details can be found in Appendix B. 

## 5 EXPERIMENTS 

### 5.1 SETUPS 

**Dataset** . We evaluate the effectiveness of BiDexHD on the TACO (Liu et al., 2024b) dataset, a large-scale bimanual manipulation dataset that encompasses diverse human demonstrations using tools to manipulate target objects in real-world scenarios. BiDextHD converts 6 categories _V_ = _{_ Dust, Empty, Pour in some, Put out, Skim off, Smear _}_ of total 141 human demonstrations in the TACO dataset to Dec-POMDP tasks (See Appendix D for task examples). Task diversity and 

7 

Preprint. 

abundance make BiDexHD easy to scale up. All tasks can be separated into 16 semantic groups, each of which gathers a number of similar demonstrations with the same action, the same toolobject category but different tool and object instances. BiDextHD constructs a task from single demonstration, and thus each semantic group correspond to a semantic subtask. We adopt teacherstudent learning to train 16 semantic sub-tasks and distill teacher policies with similar skills into 6 vision-based policies for each category eventually. 

To evaluate the effectiveness of the framework as well as the generalizability of the learned policies, we split 80% tasks for training ( **Train** ) and the rest 20% unseen tasks for testing. Detailed descriptions of dataset split are provided in Appendix B.2. For each task in the testing set, if the object and tool both occur in the training set it is labeled as a kind of combinational task ( **Test Comb** ), and otherwise it is labeled as a new task ( **Test New** ). 

**Metrics** . To measure the quality of our constructed tasks, we introduce two metrics _r_ 1 and _r_ 2. 



- The second is the average tracking rate _r_ 2 of stage two. Each task corresponds to _l_ -step human-demonstrated trajectory. For each episode, calculate the proportion of steps where two objects both effectively follows their desired poses. _r_ 2 is the average tracking rate over _n_ episodes. 



It is important to note that _r_ 2 serves as the primary metric for indicating task completion while _r_ 1 is an intermediate metric for assessing task progression. Considering the choice of _ε_ succ and _ε_ track has a non-legligible impact for the reported results, we will discuss the sensitivity of these thresholds in Section 5.4. By default, we choose _ε_ succ = _ε_ track = 0 _._ 1 for evaluation. 

### 5.2 TEACHER LEARNING 

Upon the framework of BiDexHD, different base RL algorithms can be incorporated. We mainly compare the performance of independent PPO ( **BiDexHD-IPPO** ) and centralized PPO ( **BiDexHDPPO** ). For BiDexHD-IPPO, two agents possess their own observations and execute their own actions. For BiDexHD-PPO, a single policy takes as input both observations and is trained to output all actions that maximize the sum of all total rewards in an episode, which essentially transforms a Dec-POMDP task into a POMDP task. 

**Table 1:** The average success rate of stage 1 and tracking rate of stage 2 during training and evaluation across all tasks constructed from the TACO dataset under _ε_ succ = _ε_ track = 0 _._ 1. 

|Method|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|BiDexHD-PPO|90.55|53.88|78.74|36.99|**81.42**|**26.24**|
|BiDexHD-IPPO (w/o stage-1)|25.00|17.52|24.80|18.10|19.85|08.51|
|BiDexHD-IPPO (w/o gc)|90.53|66.39|91.47|52.11|77.03|22.63|
|BiDexHD-IPPO (w/o bonus)|97.67|66.65|98.01|59.76|77.96|17.52|
|**BiDexHD-IPPO**|**98.71**|**78.18**|**98.37**|**59.94**|75.48|21.34|
|BC|00.00|00.00|00.00|00.00|00.00|00.00|
|BiDexHD-PPO+DAgger|95.35|55.82|76.75|30.42|86.34|30.00|
|**BiDexHD-IPPO+DAgger**|**99.38**|**74.59**|**92.85**|**48.43**|**94.79**|**53.71**|



**RL Results** . The first and last rows in the green section of Table 1 present the average performance across all auto-constructed bimanual tasks. For tasks with seen objects (Train and Test Comb), 

8 

Preprint. 

BiDexHD-IPPO nearly completes stage 1 by successfully reaching the reference poses and maintaining high-quality tracking during stage 2, which demonstrates its impressive scalability across diverse tasks in the TACO dataset. In contrast, BiDexHD-PPO underperforms compared to BiDexHDIPPO, particularly on tasks with seen objects. This discrepancy arises because BiDexHD-IPPO is more efficient at acquiring robust skills within limited updates by independently learning left and right policies across a wide range of tasks with smaller observation and action spaces. Furthermore, two independent expert policies focusing solely on specific groups of target objects or tools adapt more easily to similar combinational tasks than a single policy that must attend to both. Consequently, we select IPPO as our base RL algorithm. See Appendix C.1 for detailed evaluation results. 

When applied to tasks with new objects (Test New), both BiDexHD-IPPO and BiDexHD-PPO experience a noticeable performance decline. The primary reason for this drop is that these approaches incorporate one-hot object labels in observations during state-based training, leading the policy to heavily rely on this information. As a result, during evaluation, the introduction of new labels disrupts decision-making. Therefore, we remove one-hot object labels during policy distillation to enhance generalization. 

### 5.3 ABLATIONS ON TEACHER LEARNING 

We conduct ablation studies focusing on the key designs at stage one during teacher learning. 

**Alignment Stage** . To demonstrate the necessity of the design of dataset-simulation alignment stage, we compare BiDexHD-IPPO with a more naive version, denoted as **(w/o stage-1)** , which retains only _r_ track in RL training at stage 2 and maintains a fixed number of free exploration steps at stage 1. The second line in the green section of Table 1 reveals a significant performance decline. We observe that only 30.5% of relatively easy tasks (See Appendix C.1 for details) achieve positive _r_ 1 and _r_ 2, while for the remaining tasks, the success rate of stage 1 and the tracking rate of stage 2 remain at zero. This emphasizes the importance of _r_ align during stage 1. 

**Functional Grasping Center** . In BiDexHD, we pre-compute the grasping center **x** ˆgc to calculate _r_ appro in Equation 3. In this section, we explore replacing the grasping center with the geometric center of an object, denoted as **(w/o gc)** . The results presented in the third line of Table 1 show a decrease in _r_ 1 and _r_ 2, particularly on tasks involving seen objects compared to BiDexHDIPPO. To further figure out their discrepancy in behavior, we deploy both policies for inference and visualize their grasping poses for a typical task (dust, brush, pan) in Figure 3. BiDexHDIPPO tends to align more closely with the calculated grasping centers (red points), exhibiting human-like grasping behavior. In contrast, BiDexHD-IPPO (w/o gc) with geometric centers (green points) struggles to find proper poses for using the brush or holding the pan. In fact, the geometric center of an object does not often fall within areas suitable for manipulation. These findings highlight the significance of incorporating a functional grasping center, particularly for objects that are thin, flat, or equipped with handles. 



<!-- Start of picture text -->
Geometric<br>Center<br>Grasping<br>Center<br><!-- End of picture text -->

**Figure 3:** A comparison of grasping pose during policy deployment between BiDexHDIPPO (w/o gc) and BiDexHDIPPO. 

**Success Bonus** . The fourth line in the green section of Table 1 investigates whether removing reward _r_ bonus defined in Equation 5 will affect performance. We observe a decline in _r_ 2 on both the training set and unseen tasks involving new objects. We analyze the additional bonus in Equation 5 effectively signals the transition between the two stages, enhancing the policy’s awareness of task progression. 

### 5.4 STUDENT LEARNING 

For the BiDexHD variants, several trained multi-task state-based teacher policies from one task category are distilled into a single vision-based policy, which is then tested on all tasks. We also introduce behavior cloning (BC) as our baseline. To directly learn bimanual skills from a dataset, we employ Dexpilot (Handa et al., 2020) to retarget human hand motions in the TACO dataset to joint angles for dexterous hands, solving inverse kinematics (IK) for arm joint angles. All joint 

9 

Preprint. 

angles are collected and replayed in IsaacGym (Makoviychuk et al., 2021) to gather observations. BC learns purely from this static observation-action dataset and is ultimately tested under the same configuration as BiDexHD. 

**DAgger Results** . The blue section of Table 1 displays the performance of the vision-based policies. Our **BiDexHD-IPPO+DAgger** significantly outperforms both PPO variant and BC, achieving a high task completion rate on the training set and an average _r_ 2 = 51 _._ 07% across all unseen tasks (Test Comb and Test New). This evidence indicates the scalability and competitive generalization ability of BiDexHD framework. Among unseen tasks, we observe a slight decline in _r_ 2 for combinational tasks, while tasks involving new objects show a sharp increase in _r_ 2. This suggests that the visionbased policy relies more on information from the point clouds, such as shape and local features, rather than specific one-hot identifiers, enabling effective zero-shot generalization. Conversely, BC performs poorly due to the loss of true dynamics in the simulation, often getting confused by unfamiliar observations and stuck in stationary states. This also reflects the challenges associated with our constructed bimanual tasks. Our framework unifies bimanual skill learning through a combination of trial-and-error and distillation, providing a robust and scalable solution to diverse challenging bimanual manipulation tasks. See Appendix C.2 for detailed evaluation results. 

**Table 2:** The metrics of different _K_ future steps under _ε_ succ = _ε_ track = 0 _._ 1. 

**Table 3:** The sensitivity analysis of metrics of BiDexHD-IPPO+DAgger to different _ε_ . 

|Metrics (%)||_K_|||Metrics (%)||_ε_||
|---|---|---|---|---|---|---|---|---|
||0|1|2|5||0.05|0.075|0.1|
|Train_r_1|98.01|98.81|98.71|**99.38**|Train_r_1|96.87|98.27|99.38|
|Train_r_2|72.09|**75.40**|75.01|74.59|Train_r_2|52.58|66.19|74.59|
|Test Comb_r_1|**94.36**|92.11|93.26|92.85|Test Comb_r_1|49.30|77.74|92.85|
|Test Comb_r_2|46.64|**49.02**|48.60|48.43|Test Comb_r_2|13.02|24.56|48.43|
|Test New_r_1|93.96|94.67|94.38|**94.79**|Test New_r_1|79.56|88.11|94.79|
|Test New_r_2|49.27|51.00|50.39|**53.71**|Test New_r_2|17.19|37.62|53.71|



**Future Conditioned Steps** . We further examine the selection of _K ∈{_ 0 _,_ 1 _,_ 2 _,_ 5 _}_ for future object positions. Specifically, when _K_ = 0, the vision-based policy relies exclusively on 3D information from object point clouds and the robot’s proprioception. As shown in Table 2, the performance across different values of _K_ does not vary significantly. Even when future conditioned steps are masked ( _K_ = 0), _r_ 2 only exhibits slight declines of 2.5% on trained tasks and an average of 3.1% on all unseen tasks compared to _K_ = 5. This evidence suggests that after the multi-task RL training phase, the teachers have acquired diverse and robust skills, making pure imitation sufficient for a student to achieve acceptable performance. Nonetheless, _K_ future steps provide additional informative and fine-grained, albeit implicit, clues such as motion and intention for more precise tracking. 

**Discussion** . To investigate the impact of different thresholds on the metrics, we re-evaluate all tasks and report the performance of our BiDexHD-IPPO+DAgger under varying thresholds, _ε_ succ = _ε_ track = _ε ∈{_ 0 _._ 05 _,_ 0 _._ 075 _,_ 0 _._ 1 _}_ in Table 3. Notably, stricter metrics have a more pronounced impact on the performance of unseen tasks compared to trained ones, underscoring the challenges of continuous spatial-temporal trajectory tracking in bimanual manipulation tasks. We will focus on addressing more precise behavior tracking in future work. 

## 6 CONCLUSION & LIMITATIONS 

In this paper, we introduce a novel approach to learning diverse bimanual dexterous manipulation skills that utilizes human demonstrations. Our framework, BiDexHD, automatically constructs bimanual manipulation tasks from existing datasets and employs a teacher-student learning approach for a vision-based policy that can tackle similar tasks. Our main technical contributions include designing a unified two-stage reward function for multi-task RL training and an in-context vision-based policy that enhances generalization capabilities. Experimental results demonstrate that BiDexHD facilitates robust RL training and policy distillation, successfully solves six categories of bimanual dexterous manipulation tasks, and effectively transfers to unseen tasks through zero-shot generalization. 

10 

Preprint. 

Our work forwards a step toward universal bimanual manipulation skills, and some limitations need to be addressed in future research. Exploring strategies for achieving more precise spatial and temporal tracking is a valuable direction for future work. Additionally, incorporating a wider variety of real-world tasks–such as deformable object manipulation and bimanual handover–could reveal further potential in dynamic collaborative manipulation scenarios with bimanual dexterous hands. 

## REFERENCES 

- Sridhar Pandian Arunachalam, Sneha Silwal, Ben Evans, and Lerrel Pinto. Dexterous imitation made easy: A learning-based framework for efficient dexterous manipulation. In _2023 ieee international conference on robotics and automation (icra)_ , pp. 5954–5961. IEEE, 2023. 

- Yunfei Bai, Wenhao Yu, and C Karen Liu. Dexterous manipulation of cloth. In _Computer Graphics Forum_ , 2016. 

- Tao Chen, Jie Xu, and Pulkit Agrawal. A system for general in-hand object re-orientation. In _Conference on Robot Learning_ , pp. 297–307. PMLR, 2022. 

- Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, and Pulkit Agrawal. Visual dexterity: In-hand dexterous manipulation from depth. In _Icml workshop on new frontiers in learning, control, and dynamical systems_ , 2023. 

- Zerui Chen, Shizhe Chen, Cordelia Schmid, and Ivan Laptev. Vividex: Learning vision-based dexterous manipulation from human videos. _arXiv preprint arXiv:2404.15709_ , 2024. 

- Christian Schroeder De Witt, Tarun Gupta, Denys Makoviichuk, Viktor Makoviychuk, Philip HS Torr, Mingfei Sun, and Shimon Whiteson. Is independent learning all you need in the starcraft multi-agent challenge? _arXiv preprint arXiv:2011.09533_ , 2020. 

- Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. Arctic: A dataset for dexterous bimanual hand-object manipulation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 12943–12954, 2023. 

- Fanny Ficuciello, Alessandro Migliozzi, Eulalie Coevoet, Antoine Petit, and Christian Duriez. Fembased deformation control for dexterous manipulation of 3d soft objects. In _2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 4007–4013. IEEE, 2018. 

- Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, and Chelsea Finn. Humanplus: Humanoid shadowing and imitation from humans. _arXiv preprint arXiv:2406.10454_ , 2024. 

- Jianfeng Gao, Zhi Tao, Noémie Jaquier, and Tamim Asfour. Bi-kvil: Keypoints-based visual imitation learning of bimanual manipulation tasks. _arXiv preprint arXiv:2403.03270_ , 2024. 

- Koffivi Fidèle Gbagbe, Miguel Altamirano Cabrera, Ali Alabbas, Oussama Alyunes, Artem Lykov, and Dzmitry Tsetserukou. Bi-vla: Vision-language-action model-based system for bimanual robotic dexterous manipulations. _arXiv preprint arXiv:2405.06039_ , 2024. 

- Jennifer Grannen, Yilin Wu, Brandon Vu, and Dorsa Sadigh. Stabilize to act: Learning to coordinate for bimanual manipulation. In _Conference on Robot Learning_ , pp. 563–576. PMLR, 2023. 

- Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, and Dieter Fox. Dexpilot: Vision-based teleoperation of dexterous robotic handarm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 9164–9170. IEEE, 2020. 

- Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 5977–5984. IEEE, 2023. 

- Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, and Guanya Shi. Omnih2o: Universal and dexterous human-to-humanoid wholebody teleoperation and learning. _arXiv preprint arXiv:2406.08858_ , 2024. 

11 

Preprint. 

- Yew Cheong Hou, Khairul Salleh Mohamed Sahari, and Dickson Neoh Tze How. A review on modeling of flexible deformable object for dexterous robotic manipulation. _International Journal of Advanced Robotic Systems_ , 16(3):1729881419848894, 2019. 

- Binghao Huang, Yuanpei Chen, Tianyu Wang, Yuzhe Qin, Yaodong Yang, Nikolay Atanasov, and Xiaolong Wang. Dynamic handover: Throw and catch with bimanual hands. _arXiv preprint arXiv:2309.05655_ , 2023. 

- Xiaogang Jia, Denis Blessing, Xinkai Jiang, Moritz Reuss, Atalay Donat, Rudolf Lioutikov, and Gerhard Neumann. Towards diverse behaviors: A benchmark for imitation learning with human demonstrations. _arXiv preprint arXiv:2402.14606_ , 2024. 

- Satoshi Kataoka, Seyed Kamyar Seyed Ghasemipour, Daniel Freeman, and Igor Mordatch. Bimanual manipulation and attachment via sim-to-real reinforcement learning. _arXiv preprint arXiv:2203.08277_ , 2022. 

- Sizhe Li, Zhiao Huang, Tao Chen, Tao Du, Hao Su, Joshua B Tenenbaum, and Chuang Gan. Dexdeform: Dexterous deformable object manipulation with human demonstrations and differentiable physics. _arXiv preprint arXiv:2304.03223_ , 2023. 

- Toru Lin, Zhao-Heng Yin, Haozhi Qi, Pieter Abbeel, and Jitendra Malik. Twisting lids off with two hands. _arXiv preprint arXiv:2403.02338_ , 2024. 

- I Liu, Chun Arthur, Sicheng He, Daniel Seita, and Gaurav Sukhatme. Voxact-b: Voxel-based acting and stabilizing policy for bimanual manipulation. _arXiv preprint arXiv:2407.04152_ , 2024a. 

- Qingtao Liu, Yu Cui, Qi Ye, Zhengnan Sun, Haoming Li, Gaofeng Li, Lin Shao, and Jiming Chen. Dexrepnet: Learning dexterous robotic grasping network with geometric and spatial hand-object representations. In _2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pp. 3153–3160. IEEE, 2023. 

- Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking generalizable bimanual tool-action-object understanding. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 21740–21751, 2024b. 

- Zhengyi Luo, Jinkun Cao, Sammy Christen, Alexander Winkler, Kris Kitani, and Weipeng Xu. Grasping diverse objects with simulated humanoids. _arXiv preprint arXiv:2407.11385_ , 2024. 

- Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- Priyanka Mandikal and Kristen Grauman. Learning dexterous grasping with object-centric visual affordances. In _2021 IEEE international conference on robotics and automation (ICRA)_ , pp. 6169–6176. IEEE, 2021. 

- Priyanka Mandikal and Kristen Grauman. Dexvip: Learning dexterous grasping with human hand pose priors from video. In _Conference on Robot Learning_ , pp. 651–661. PMLR, 2022. 

- Ajay Mandlekar, Soroush Nasiriany, Bowen Wen, Iretiayo Akinola, Yashraj Narang, Linxi Fan, Yuke Zhu, and Dieter Fox. Mimicgen: A data generation system for scalable robot learning using human demonstrations. _arXiv preprint arXiv:2310.17596_ , 2023. 

- Gbenga Abiodun Odesanmi, Qining Wang, and Jingeng Mai. Skill learning framework for human– robot interaction and manipulation tasks. _Robotics and Computer-Integrated Manufacturing_ , 79: 102444, 2023. 

- Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pp. 652–660, 2017. 

- Haozhi Qi, Ashish Kumar, Roberto Calandra, Yi Ma, and Jitendra Malik. In-hand object rotation via rapid motor adaptation. In _Conference on Robot Learning_ , pp. 1722–1732. PMLR, 2023. 

12 

Preprint. 

- Yuzhe Qin, Hao Su, and Xiaolong Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _IEEE Robotics and Automation Letters_ , 7(4):10873–10881, 2022a. 

- Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision_ , pp. 570–587. Springer, 2022b. 

- Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Generalizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In _Conference on Robot Learning_ , pp. 594–605. PMLR, 2023a. 

- Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su, Xiaolong Wang, Yu-Wei Chao, and Dieter Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. In _Robotics: Science and Systems_ , 2023b. 

- Haziq Razali and Yiannis Demiris. Action-conditioned generation of bimanual object manipulation sequences. In _Proceedings of the AAAI conference on artificial intelligence_ , 2023. 

- Javier Romero, Dimitrios Tzionas, and Michael J. Black. Embodied hands: Modeling and capturing hands and bodies together. _ACM Transactions on Graphics, (Proc. SIGGRAPH Asia)_ , 36(6), November 2017. 

- Stéphane Ross, Geoffrey Gordon, and Drew Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. In _Proceedings of the fourteenth international conference on artificial intelligence and statistics_ , pp. 627–635. JMLR Workshop and Conference Proceedings, 2011. 

- Karl Schmeckpeper, Oleh Rybkin, Kostas Daniilidis, Sergey Levine, and Chelsea Finn. Reinforcement learning with videos: Combining offline observations with interaction. _arXiv preprint arXiv:2011.06507_ , 2020. 

- Lin Shao, Toki Migimatsu, Qiang Zhang, Karen Yang, and Jeannette Bohg. Concept2robot: Learning manipulation concepts from instructions and human demonstrations. _The International Journal of Robotics Research_ , 40(12-14):1419–1434, 2021. 

- Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _arXiv preprint arXiv:2309.06440_ , 2023a. 

- Kenneth Shaw, Shikhar Bahl, and Deepak Pathak. Videodex: Learning dexterity from internet videos. In _Conference on Robot Learning_ , pp. 654–665. PMLR, 2023b. 

- Siddhanth Raja Sindhupathiraja, AKM Amanat Ullah, William Delamare, and Khalad Hasan. Exploring bi-manual teleportation in virtual reality. In _2024 IEEE Conference Virtual Reality and 3D User Interfaces (VR)_ , pp. 754–764. IEEE, 2024. 

- Aravind Sivakumar, Kenneth Shaw, and Deepak Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. _arXiv preprint arXiv:2202.10448_ , 2022. 

- Laura Smith, Nikita Dhawan, Marvin Zhang, Pieter Abbeel, and Sergey Levine. Avid: Learning multi-stage tasks via pixel-level translation of human videos. _arXiv preprint arXiv:1912.04443_ , 2019. 

- Weikang Wan, Haoran Geng, Yun Liu, Zikang Shan, Yaodong Yang, Li Yi, and He Wang. Unidexgrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalist-specialist learning. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pp. 3891–3902, 2023. 

- Shiyao Wang, Xiuping Liu, Charlie CL Wang, and Jian Liu. Physics-aware iterative learning and prediction of saliency map for bimanual grasp planning. _Computer Aided Geometric Design_ , 111: 102298, 2024. 

13 

Preprint. 

- Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 4737–4746, 2023. 

- Jianglong Ye, Jiashun Wang, Binghao Huang, Yuzhe Qin, and Xiaolong Wang. Learning continuous grasping function with a dexterous hand from human demonstrations. _IEEE Robotics and Automation Letters_ , 8(5):2882–2889, 2023. 

- Zhao-Heng Yin, Binghao Huang, Yuzhe Qin, Qifeng Chen, and Xiaolong Wang. Rotating without seeing: Towards in-hand dexterity through touch. _arXiv preprint arXiv:2303.10880_ , 2023. 

- Dongjie Yu, Hang Xu, Yizhou Chen, Yi Ren, and Jia Pan. Bikc: Keypose-conditioned consistency policy for bimanual robotic manipulation. _arXiv preprint arXiv:2406.10093_ , 2024. 

- Xinyu Zhan, Lixin Yang, Yifei Zhao, Kangrui Mao, Hanlin Xu, Zenan Lin, Kailin Li, and Cewu Lu. Oakink2: A dataset of bimanual hands-object manipulation in complex task completion. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 445–456, 2024. 

- Hui Zhang, Sammy Christen, Zicong Fan, Luocheng Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges. Artigrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. In _2024 International Conference on 3D Vision (3DV)_ , pp. 235–246. IEEE, 2024a. 

- Tianle Zhang, Dongjiang Li, Yihang Li, Zecui Zeng, Lin Zhao, Lei Sun, Yue Chen, Xuelong Wei, Yibing Zhan, Lusong Li, et al. Empowering embodied manipulation: A bimanual-mobile robot manipulation dataset for household tasks. _arXiv preprint arXiv:2405.18860_ , 2024b. 

14 

Preprint. 

## A ALGORITHM 

**Algorithm 1:** BiDexHD framework. 

**Input:** Human demonstration dataset _D_ = _{τ_<sup>1</sup> _, τ_<sup>2</sup> _, . . . , τ_<sup>_M_</sup> _}_ ; Object mesh set Ω; State-based policies _πθ_<sup>side</sup> ; Vision-based policy _πϕ_<sup>side</sup> (side _∈{_ left,right}). **Output:** The learned vision-based policy _πϕ_<sup>side.</sup> 

### **<u>Task Construction:</u>** 

**for** _τ_<sup>_i_</sup> _∈D_ **do** 

Preprocess each _τ_<sup>_i_</sup> by translating MANO parameters to pose sequence in Equation 1 ; Construct task _T_<sup>_i_</sup> with corresponding _τ_<sup>_i_</sup> _,_ **h**<sup>tool</sup> and **h**<sup>object</sup> . 

### **Teacher learning:** 

Sample a subset of similar tasks Λ _⊆ Γ_ = _{T_<sup>1</sup> _, ..., T_<sup>_M_</sup> _}_ ; Parallelly initialize _T_<sup>_i_:1</sup><sup>_...|_Λ</sup><sup>_|_</sup> in IsaacGym simulation with _o_<sup>left</sup> 0 and _o_<sup>right</sup> 0 in Equation 2; **while** _not converge_ **do** Get state-based observations _o_<sup>left</sup> _t_<sup>_, o_</sup> _t_<sup>right</sup> ; Sample action **a**<sup>left</sup> _t ∼ πθ_<sup>left(</sup><sup>**a**</sup> _t_<sup>left</sup><sup>_|o_left</sup> _t_<sup>_,_</sup><sup>**a**left</sup> _t−_ 1<sup>)</sup><sup>_,_</sup><sup>**a**</sup> _t_<sup>right</sup> _∼ πθ_<sup>right</sup> ( **a**<sup>right</sup> _t |o_<sup>right</sup> _t ,_ **a**<sup>right</sup> _t−_ 1<sup>);</sup> Step the environments to observe _o_<sup>left</sup> _t_ +1<sup>_, o_right</sup> _t_ +1<sup>and calculate total reward</sup><sup>_r_</sup> total<sup>left</sup><sup>_, r_</sup> total<sup>right;</sup> Save ( _o_<sup>left</sup> _t_<sup>_,_</sup><sup>**a**left</sup> _t_<sup>_, o_left</sup> _t_ +1<sup>_, r_</sup> total<sup>left) and (</sup><sup>_o_</sup> _t_<sup>right</sup> _,_ **a**<sup>right</sup> _t , o_<sup>right</sup> _t_ +1<sup>_, r_</sup> total<sup>right) into IPPO buffer;</sup> Update _πθ_<sup>left</sup> and _πθ_<sup>right</sup> using IPPO with the IPPO buffer. 

### **Policy Distillation:** 

Index _{τ_<sup>1</sup> _, . . . , τ_<sup>_|_Λ</sup><sup>_|_</sup> _}_ and pre-sample 4096 points for the tool and target object in each _T_<sup>_i_</sup> ; Parallelly initialize _T_<sup>_i_:1</sup><sup>_...|_Λ</sup><sup>_|_</sup> in IsaacGym simulation; 

**while** _not converge_ **do** 

The students get vision-based observations **o**<sup>left</sup> _t_<sup>_,_</sup><sup>**o**</sup> _t_<sup>right</sup> with sampled point clouds and _K_ -step future trajectories and sample action **a**<sup>left</sup> _t ∼ πϕ_<sup>left(</sup><sup>**a**</sup> _t_<sup>left</sup><sup>_|_</sup><sup>**o**left</sup> _t_<sup>_,_</sup><sup>**a**left</sup> _t−_ 1<sup>)</sup><sup>_,_</sup><sup>**a**</sup> _t_<sup>right</sup> _∼ πϕ_<sup>right</sup> ( **a**<sup>right</sup> _t |_ **o**<sup>right</sup> _t ,_ **a**<sup>right</sup> _t−_ 1<sup>);</sup> The experts _πθ_<sup>left</sup><sup>_, π_</sup> _θ_<sup>right</sup> observe the corresponding _o_<sup>left</sup> _t_<sup>_, o_</sup> _t_<sup>right</sup> and labels **ˆa**<sup>left</sup> _t_<sup>_,_</sup><sup>**ˆa**</sup> _t_<sup>right</sup> ; Step the environments; Save ( **o**<sup>left</sup> _t_<sup>_,_</sup><sup>**ˆa**left</sup> _t_<sup>) and (</sup><sup>**o**</sup> _t_<sup>right</sup> _,_ **ˆa**<sup>left</sup> _t_<sup>) into DAgger buffer;</sup> Update _πϕ_<sup>right</sup> and _πϕ_<sup>right</sup> by minimizing MSE loss with the DAgger buffer. 

## B IMPLEMENTATION DETAILS 

B.1 DATASET PREPROCESSING 

**Reference Timestep** . Considering there are a number of useless preparation timesteps before grasping, the reference timestep in Section 4.2 is actually chosen based on the first sudden change of the distance between an object and a tool, because the distance between the tool and object almost stays unchanged before grasping. 

**More Details** . We further align the coordinates of human wrist to the coordinates of robot palm base to ensure the same dual-hand manipulation behavior. Besides, due to the geometric discrepancy of objects, we found that the initial height of objects differ a lot in different tasks. Therefore, a translation offset in z-axis is added to all poses in the dataset to keep all the object at the same initial height on the same table. 

### B.2 CONSTRUCTED TASKS 

**Task Composition** . Table 4 describes the detailed task categories, sub-task names, the split of training and testing set and the diversity of tools and target objects. 

15 

Preprint. 

**Table 4:** 141 constructed tasks across 6 categories for BiDexHD. “All” refers to the total number of a kind of sub-task. “Train” refers to the number of tasks in the training set. “Test Comb” and “Test New” refer to the number of tasks in two types of testing sets. “Tool” and “Object” refer to number of objects in the corresponding sub-tasks. 

|Action|Sub-Task Name|All|Train|Test Comb|Test New|Tool|Object|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)|10|7|1|2|5|5|
||(empty, bowl, plate)|34|26|1|7|8|9|
||(empty, cup, plate)|1|1|0|0|1|1|
||(empty, teapot, plate)|12|8|1|3|2|6|
||(empty, teapot, teapot)|3|3|0|0|2|2|
|Pour in some|(pour in some, cup, cup)|1|1|0|0|1|1|
||(pour in some, cup, plate)|2|2|0|0|2|2|
||(pour in some, cup, teapot)|1|1|0|0|1|1|
||(pour in some, teapot, bowl)|1|1|0|0|1|1|
||(pour in some, teapot, cup)|2|1|0|1|2|2|
|Dust|(dust, brush, bowl)|20|5|0|15|5|9|
||(dust, brush, pan)|9|6|3|0|4|3|
|Put out|(put out, bowl, bowl)|10|7|2|1|5|5|
||(put out, bowl, plate)|16|11|1|4|3|8|
|Skim off|(skim off, bowl, plate)|17|12|0|5|5|8|
|Smear|(smear, glue gun, plate)|2|2|0|0|1|2|
|**Total**|–|**141**|94|9|38|–|–|



### B.3 DEXTEROUS HANDS 

Currently we use LEAP Hands (Shaw et al., 2023a). In future work we will introduce more kinds of dexterous hands. 

### B.4 SIMULATION SETUP 

Two 6-DOF RealMan arms, spaced 0.68 meters apart, are placed in front of a 0.7m table. 16DOF LEAP Hands are Shaw et al. (2023a) mounted on both the left and right arms, with an initial stretching pose. The tool and target object are spaced 0.4m apart horizontally, 0.5m distant from the robotic arm base. 

### B.5 TRAINING DETAILS 

**DAgger Details** . To make the student policy learn more efficiently especially at the early training stage, we mix a few imitation samples to DAgger buffer. Specifically, we choose to use the actions labelled by the experts with probability _p_ = 0 _._ 05 and otherwise actions output by the policy itself. This is often proven desirable in practice, as the naive policy may make more mistakes and visit states that are irrelevant at the early training stage with relatively few datapoints (Ross et al., 2011). 

**Hyperparameters** . Table 5 and 6 outlines the hyperparameters for IPPO and DAgger in BiDexHD respectively. 

### B.6 MODEL ARCHITECTURE 

Our codebase for RL and DAgger is built upon UniDexGrasp++ (Wan et al., 2023). For each statebased policy, we employ five-layer multi-layer perceptrons (MLPs) for both the actor and the critic, featuring hidden layers with dimensions [1024, 1024, 512, 512] and using ELU activation functions. For the vision-based policy, we utilize a simplified PointNet (Qi et al., 2017) backbone that incorporates two 1D convolutional layers, a mixture of maximum and average pooling operations, and two MLP layers to process the object point cloud, resulting in an output dimension of 128. Both the actor and the critic share the output of this backbone. 

16 

Preprint. 

**Table 5:** Hyperparameters of IPPO 

|**Hyperparameter**|**Value**|
|---|---|
|_wr_|2.0|
|_wt_|15.0|
|_w_1|0.5|
|_w_2|1.0|
|_w_3|1.0|
|_w_4|1.0|
|_λ_w|0.12|
|_λ_ft|0.48|
|Episode Length|1000|
|Parallel rollout steps per iteration|8|
|Training epochs per iteration|5|
|Discount factor|0.96|
|GAE lambda|0.95|
|Clip range|0.2|
|Optimizer|AdamW|
|Learning Rate|3e-4|
|Number of Environments|15000|
|Type of GPUs|A100, or Nvidia RTX 4090 Ti|



**Table 6:** Hyperparameters of DAgger 

|**Hyperparameter**|**Value**|
|---|---|
|_P_|512|
|_K_|5|
|Parallel rollout steps per iteration|8|
|Training epochs per iteration|5|
|Optimizer|AdamW|
|Learning Rate|3e-4|
|Number of Environments|5000|
|Type of GPUs|A100, or Nvidia RTX 4090 Ti|



17 

Preprint. 

### B.7 COMPUTATION RESOURCES 

we train a state-based IPPO policy for single sub-tasks for around two days, and distill teacher policies into a vision-based policy for each action category for around one day on single 40G A100 GPUs. All the evaluations are done on a 24G Nvidia RTX 4090 Ti GPU for about half an hour. 

## C EVALUATION RESULTS 

### C.1 RESULTS OF TEACHER LEARNING 

Tables below record the detailed evaluation results for each sub-task. ‘–’ represents the absence of testing tasks. The last row of each table shows the average results over all sub-tasks. 

**Table 7:** Detailed Metrics of BiDexHD-PPO for each sub-task under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Sub-Task Name|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)<br>|99.38<br>|69.28<br>|99.30<br>|62.24<br>|93.64<br>|53.13<br>|
||(empty, bowl, plate)<br>|97.88<br>|50.38<br>|100.00|35.93|65.91|8.95|
||(empty, cup, plate)|77.03|33.41|–|–|–|–|
||(empty, teapot, plate)|100.00|82.09|71.83|23.62|96.84|28.04|
||(empty, teapot, teapot)|100.00|27.89|42.42|7.63|–|–|
|Pour in some|(pour in some, cup, cup)|25.50|22.71|–|–|–|–|
||(pour in some, cup, plate)|99.88|82.16|–|–|–|–|
||(pour in some, cup, teapot)|100.00|69.69|–|–|–|–|
||(pour in some, teapot, bowl)<br>|99.56<br>|5.85<br>|–|–|–|–|
||(pour in some, teapot, cup)|85.48|31.26|–|–|–|–|
|Dust|(dust, brush, bowl)|99.61|77.70|–|–|78.57|17.54|
||(dust, brush, pan)|73.68|48.22|41.58|15.69|–|–|
|Put out|(put out, bowl, bowl)|91.54|39.80|100.00|46.25|67.74|5.48|
||(put out, bowl, plate)|99.57|69.75|96.08|67.54|81.51|34.51|
|Skim off|(skim off, bowl, plate)|99.68|74.59|–|–|85.76|36.01|
|Smear|(smear, glue gun, plate)|100.00|77.26|–|–|–|–|
|**Average**|–|90.55|53.88|78.74|36.99|81.42|26.24|



**Table 8:** Detailed Metrics of BiDexHD-IPPO for each sub-task under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Sub-Task Name|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)|99.74|79.02|97.67|37.55|98.34|48.72|
||(empty, bowl, plate)|97.90|75.76|100.00|62.13|85.00|9.10|
||(empty, cup, plate)|99.84|79.47|–|–|–|–|
||(empty, teapot, plate)|100.00|84.29|90.91|16.84|100.00|25.80|
||(empty, teapot, teapot)|100.00|84.87|100.00|87.06|–|–|
|Pour in some|(pour in some, cup, cup)|100.00|99.70|–|–|–|–|
||(pour in some, cup, plate)|89.78|55.95|–|–|–|–|
||(pour in some, cup, teapot)|99.47|74.43|–|–|–|–|
||(pour in some, teapot, bowl)|100.00|75.48|–|–|–|–|
||(pour in some, teapot, cup)|95.76|57.23|–|–|–|–|
|Dust|(dust, brush, bowl)|100.00|91.24|–|–|84.34|32.10|
||(dust, brush, pan)|100.00|86.08|100.00|58.09|–|–|
|Put out|(put out, bowl, bowl)|100.00|75.09|100.00|72.92|81.25|17.87|
||(put out, bowl, plate)|96.98|77.97|100.00|84.97|29.41|7.03|
|Skim off|(skim off, bowl, plate)|100.00|73.11|–|–|50.00|8.74|
|Smear|(smear, glue gun, plate)|99.88|81.24|–|–|–|–|
|**Average**|–|98.71|78.18|98.37|59.94|75.48|21.34|



18 

Preprint. 

**Table 9:** Detailed Metrics of BiDexHD-IPPO(w.o. stage-1) for each sub-task under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Sub-Task Name|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)|100.00|73.94|64.63|49.10|58.08|45.91|
||(empty, bowl, plate)|0.00|0.00|0.00|0.00|0.00|0.00|
||(empty, cup, plate)|0.00|0.00|–|–|–|–|
||(empty, teapot, plate)|0.00|0.00|0.00|0.00|0.00|0.00|
||(empty, teapot, teapot)|100.00|83.77|61.32|45.78|–|–|
|Pour in some|(pour in some, cup, cup)|0.00|0.00|–|–|–|–|
||(pour in some, cup, plate)|0.00|0.00|–|–|–|–|
||(pour in some, cup, teapot)|0.00|0.00|–|–|–|–|
||(pour in some, teapot, bowl)|0.00|0.00|–|–|–|–|
||(pour in some, teapot, cup)|0.00|0.00|–|–|–|–|
|Dust|(dust, brush, bowl)|0.00|0.00|–|–|0.00|0.00|
||(dust, brush, pan)|0.00|0.00|0.00|0.00|–|–|
|Put out|(put out, bowl, bowl)|100.00|71.32|47.65|31.80|11.02|6.79|
||(put out, bowl, plate)|0.00|0.00|0.00|0.00|0.00|0.00|
|Skim off|(skim off, bowl, plate)|100.00|51.37|–|–|69.88|6.86|
|Smear|(smear, glue gun, plate)|0.00|0.00|–|–|–|–|
|**Average**|–|25.00|17.52|24.80|18.10|19.85|8.51|



**Table 10:** Detailed Metrics of BiDexHD-IPPO(w.o. gc) for each sub-task under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Sub-Task Name|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)|100.00|75.66|100.00|49.28|100.00|50.27|
||(empty, bowl, plate)|78.68|45.56|65.00|16.44|56.67|10.62|
||(empty, cup, plate)|52.53|19.67|–|–|–|–|
||(empty, teapot, plate)|69.73|47.65|91.23|14.89|83.00|35.43|
||(empty, teapot, teapot)|100.00|83.56|100.00|86.58|–|–|
|Pour in some|(pour in some, cup, cup)|100.00|99.71|–|–|–|–|
||(pour in some, cup, plate)|98.06|44.36|–|–|–|–|
||(pour in some, cup, teapot)|99.90|91.03|–|–|–|–|
||(pour in some, teapot, bowl)|100.00|74.71|–|–|–|–|
||(pour in some, teapot, cup)|94.41|56.88|–|–|–|–|
|Dust|(dust, brush, bowl)|99.78|88.39|–|–|80.15|27.45|
||(dust, brush, pan)|94.03|74.31|84.03|55.75|–|–|
|Put out|(put out, bowl, bowl)|99.95|62.07|100.00|61.41|84.51|11.88|
||(put out, bowl, plate)|84.15|66.27|100.00|80.39|79.59|18.73|
|Skim off|(skim off, bowl, plate)|91.40|70.22|–|–|55.26|4.06|
|Smear|(smear, glue gun, plate)|85.93|62.13|–|–|–|–|
|**Average**|–|90.53|66.39|91.47|52.11|77.03|22.63|



19 

Preprint. 

**Table 11:** Detailed Metrics of BiDexHD-IPPO(w.o. bonus) for each sub-task under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Sub-Task Name|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|---|
|Empty|(empty, bowl, bowl)|100.00|52.77|98.91|44.44|96.49|24.22|
||(empty, bowl, plate)|98.95|66.06|99.51|63.93|84.87|8.59|
||(empty, cup, plate)|99.77|43.87|–|–|–|–|
||(empty, teapot, plate)|100.00|83.39|92.66|24.63|86.70|26.44|
||(empty, teapot, teapot)|100.00|84.03|99.61|85.76|–|–|
|Pour in some|(pour in some, cup, cup)|100.00|98.99|–|–|–|–|
||(pour in some, cup, plate)|89.91|31.76|–|–|–|–|
||(pour in some, cup, teapot)|100.00|86.55|–|–|–|–|
||(pour in some, teapot, bowl)|76.43|11.27|–|–|–|–|
||(pour in some, teapot, cup)|100.00|67.22|–|–|–|–|
|Dust|(dust, brush, bowl)|99.77|86.93|–|–|88.34|35.45|
||(dust, brush, pan)|99.44|72.85|95.41|46.95|–|–|
|Put out|(put out, bowl, bowl)|100.00|62.52|100.00|68.21|95.45|16.13|
||(put out, bowl, plate)|98.80|75.67|100.00|84.37|48.82|5.16|
|Skim off|(skim off, bowl, plate)|100.00|58.47|–|–|45.03|6.66|
|Smear|(smear, glue gun, plate)|99.70|84.10|–|–|–|–|
|**Average**|–|97.67|66.65|98.01|59.76|77.96|17.52|



### C.2 RESULTS OF STUDENT LEARNING 

Tables below record the detailed evaluation results for each task category. The last row of each table shows the average results over all sub-tasks in all task categories. ‘–’ in the table represents the absence of testing tasks. 

**Table 12:** Detailed Metrics of BiDexHD-PPO+DAgger for each task category under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|95.42|72.49|72.41|19.13|94.92|40.79|
|Empty (5)|96.61|56.95|70.18|24.58|90.91|27.63|
|Put out (2)|98.04|52.33|97.52|56.31|88.41|29.75|
|Pour in some (5)|91.73|42.96|–|–|–|–|
|Skim off (1)|97.60|71.54|–|–|42.19|20.79|
|Smear (1)|99.40|72.46|–|–|–|–|
|**Average**|95.35|55.82|76.75|30.42|86.34|30.00|



**Table 13:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=5) for task category under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|100.00|86.91|100.00|49.94|100.00|48.37|
|Empty (5)|99.04|73.20|87.13|36.62|96.61|61.96|
|Put out (2)|98.22|71.89|100.00|76.43|93.63|42.40|
|Pour in some (5)|100.00|72.31|–|–|–|–|
|Skim off (1)|98.78|71.59|–|–|77.58|45.71|
|Smear (1)|99.70|76.69|–|–|–|–|
|**Average**|99.38|74.59|92.85|48.43|94.79|53.71|



20 

Preprint. 

**Table 14:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=5) for each task category under _ε_ succ = _ε_ track = 0 _._ 075. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|99.64|75.79|97.06|22.34|96.97|28.81|
|Empty (5)|97.26|63.39|61.11|10.62|96.59|48.16|
|Put out (2)|94.44|60.38|100.00|61.64|62.50|20.29|
|Pour in some (5)|100.00|68.38|–|–|–|–|
|Skim off (1)|98.53|60.74|–|–|79.17|37.23|
|Smear (1)|99.40|67.15|–|–|–|–|
|**Average**|98.27|66.19|77.74|24.56|88.11|37.62|



**Table 15:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=5) for each task category under _ε_ succ = _ε_ track = 0 _._ 05. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|97.51|58.09|52.38|5.22|84.62|14.20|
|Empty (5)|94.52|50.47|27.78|6.65|88.89|21.71|
|Put out (2)|93.05|41.78|100.00|36.75|56.25|10.49|
|Pour in some (5)|100.00|59.37|–|–|–|–|
|Skim off (1)|98.75|42.11|–|–|69.39|13.94|
|Smear (1)|97.44|50.18|–|–|–|–|
|**Average**|96.87|52.58|49.30|13.02|79.56|17.19|



**Table 16:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=2) for each task category under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|99.81|86.47|98.33|48.19|99.79|52.57|
|Empty (5)|98.42|73.13|88.54|36.51|97.30|55.76|
|Put out (2)|98.37|70.56|100.00|79.25|91.41|39.62|
|Pour in some (5)|98.47|74.59|–|–|–|–|
|Skim off (1)|98.55|70.32|–|–|74.87|40.77|
|Smear (1)|100.00|77.14|–|–|–|–|
|**Average**|98.71|75.01|93.26|48.60|94.38|50.39|



21 

Preprint. 

**Table 17:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=1) for each task category under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|99.89|85.90|99.19|45.88|100.00|47.51|
|Empty (5)|98.55|73.04|86.13|39.56|98.44|59.65|
|Put out (2)|97.90|72.42|100.00|75.80|90.91|38.03|
|Pour in some (5)|98.78|74.90|–|–|–|–|
|Skim off (1)|98.94|71.45|–|–|72.65|40.66|
|Smear (1)|99.87|78.54|–|–|–|–|
|**Average**|98.81|75.40|92.11|49.02|94.67|51.00|



**Table 18:** Detailed Metrics of BiDexHD-IPPO+DAgger(K=0) for each task category under _ε_ succ = _ε_ track = 0 _._ 1. 

|Action|Train<br>_r_1(%)|Train<br>_r_2(%)|Test Comb<br>_r_1(%)|Test Comb<br>_r_2(%)|Test New<br>_r_1(%)|Test New<br>_r_2(%)|
|---|---|---|---|---|---|---|
|Dust (2)|100.00|86.27|98.21|44.53|98.72|42.01|
|Empty (5)|95.77|64.37|90.57|35.44|96.20|59.15|
|Put out (2)|98.08|72.92|100.00|76.74|90.84|39.50|
|Pour in some (5)|99.01|73.35|–|–|–|–|
|Skim off (1)|98.39|69.76|–|–|79.44|33.94|
|Smear (1)|99.70|76.63|–|–|–|–|
|**Average**|98.01|72.09|94.36|46.64|93.96|49.27|



## D ADDITIONAL VISUALIZATIONS 

Figures below visualize samples of bimanual human demonstrations and policy deployment of constructed bimanual dexterous manipulation tasks. 



**Figure 4:** Task visualization of (pour in some, cup, teapot). 

22 

Preprint. 



**Figure 5:** Task visualization of (empty, bowl, bowl). 

23 

