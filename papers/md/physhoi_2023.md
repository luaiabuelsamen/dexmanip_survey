# **PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction** 

Yinhuai Wang<sup>1,2§</sup> Jing Lin<sup>3</sup> Ailing Zeng<sup>2</sup><sup>_†_</sup> Zhengyi Luo<sup>4</sup> Jian Zhang<sup>1</sup><sup>_†_</sup> Lei Zhang<sup>2</sup> 1Peking University 2International Digital Economy Academy 3Tsinghua University 4Carnegie Mellon University 



Figure 1. Our method controls physically simulated humanoids to perform various dynamic interaction skills. Our method can imitate human-object interaction across dynamic scenarios without task-specific rewards. **Top-to-bottom** : Fingertip spin basketball ( _left_ ), Grasp ( _right_ ); Pick up and dribble; Walk while dribbling. Project page and video demonstrations: https://wyhuai.github.io/physhoi-page/ 

## **Abstract** 

_Humans interact with objects all the time. Enabling a humanoid to learn human-object interaction (HOI) is a key step for future smart animation and intelligent robotics systems. However, recent progress in physics-based HOI requires carefully designed task-specific rewards, making the system unscalable and labor-intensive. This work focuses on dynamic HOI imitation: teaching humanoid dynamic interaction skills through imitating kinematic HOI demonstrations. It is quite challenging because of the complexity of the interaction between body parts and objects and the lack of dynamic HOI data. To handle the above issues, we present PhysHOI, the first physics-based whole-body HOI imitation approach without task-specific reward designs. Except for the kinematic HOI representations of humans and objects, we introduce the contact graph to model the contact relations between body parts and objects explicitly. A contact graph reward is also designed, which proved to be critical for precise HOI imitation. Based on the key designs, PhysHOI can imitate diverse HOI tasks simply yet effectively without prior knowledge. To make up for the lack of dynamic HOI scenarios in this area, we introduce the_ 

BallPlay _dataset that contains eight whole-body basketball skills. We validate PhysHOI on diverse HOI tasks, including whole-body grasping and basketball skills._ 

## **1. Introduction** 

Creating realistic and agile interactions between objects and humanoids is a long-standing and challenging problem in computer animation, robotics, and human-computer interaction (HCI) [22, 57, 64, 86]. Recently, due to advances in deep reinforcement learning and physics simulation, methods that learn humanoid control from demonstrations (e.g., kinematic motions from motion capture data) have been widely used in animation [53, 69–72, 102, 116] and robotics [2, 5, 17, 81]. However, most existing physics-based imitation learning methods focus on mimicking isolated human motion without considering human-object interactions, especially for whole-body (i.e., full-body with hands) motions, as involving articulated fingers and complex object dynamics can be exceedingly challenging. 

There exist HOI tasks conditioned on goals, in which the 

_§_ Work done during an internship at IDEA;<sup>_†_</sup> Corresponding authors. 

humanoid is tasked with manipulating objects to reach certain kinematic states [1, 6, 31, 116]. Although they perform well on specific tasks, e.g., playing tennis [116], these methods may find the learning paradigm difficult to generalize to new types of interaction and skills, considering each needs specially designed task rewards. For example, basketball games consist of multiple basic skills: dribbling, shooting, passing, fingertip spinning, etc. It is extremely laborious to design task-specific rewards for all skills. 

To solve diverse HOI tasks within a unified solution, we resort to the HOI imitation, i.e., recreating diverse HOI skills in simulation from kinematic demonstrations. It should be noted that the difference between HOI imitation and previous imitation methods [69, 71] is that they imitate isolated human motion, while our aim is to recreate motion for both the human and the object. During simulation, the object is passive and can only be controlled indirectly by the humanoid, making this task extremely challenging. 

Correspondingly, we introduce the first physics-based whole-body HOI imitation framework, called _PhysHOI_ , which makes HOI imitation feasible in diverse scenarios. Given a kinematic HOI demonstration sequence, _PhysHOI_ can imitate the HOI skill without task-specific knowledge and reward designs. Considering the importance of contact in describing HOI semantics, we introduce a novel generalpurpose Contact Graph (CG), where nodes are whole-body humanoid body segments and objects, and each edge denotes the binary contact information between two nodes, to enhance the commonly-used kinematic HOI representation (e.g., the human motion, object motion, and interaction graph [122]). Based on the contact-aware HOI representation, we present a task-agnostic HOI imitation reward that multiplies the kinematic rewards with the proposed contact graph reward (CGR), which effectively eliminates local optima in kinematic-only rewards. To make up for the lack of dynamic HOI data, we introduce the _BallPlay_ dataset, which contains eight diverse human-basketball interaction demonstrations with high-quality SMPL-X [68] and object motions, and contact labels. 

Our core contributions can be summarized below: 

- Aiming at learning dynamic HOI skills with the wholebody humanoids in simulation, we present _PhysHOI_ . This first whole-body HOI imitation approach learns interaction skills directly from kinematic HOI demonstrations. 

- To make the method task-agnostic towards general HOI learning, we introduce a general-purpose contact graph (CG) as a critical complement. Correspondingly, we design a novel contact graph reward (CGR), which effectively guides whole-body humanoids to manipulate objects or interact with high-dynamic objects precisely without task-specific reward designs. 

- We introduce the _BallPlay_ dataset to fill the gap in missing dynamic HOI datasets. 

|**Method**|**Year**|**High-Dynamic**<br>**HOI**|**Contact**<br>**Guidance**|**Task-Agnostic**<br>**Rewards**|**Whole-Body**<br>**Motions**|
|---|---|---|---|---|---|
|DeepMimic [69]|2018|_×_|_×_|_×_|_×_|
|AMP [71]|2021|_×_|_×_|_×_|_×_|
|Hassan_et al_. [31]|2023|_×_|_×_|_×_|_×_|
|Vid2tennis [116]|2023|✓|✓|_×_|_×_|
|PMP [1]|2023|_×_|_×_|_×_|✓|
|Zhang_et al_. [122]|2023|_×_|_×_|✓|_×_|
|Braun_et al_. [6]|2023|_×_|✓|_×_|✓|
|**_PhysHOI_ (Ours)**|2023|✓|✓|✓|✓|



Table 1. Comparisons of the most related **physics-based** methods. 

We validate the effectiveness of our proposed method comprehensively on five whole-body grasping cases and eight basketball skills, as shown in Fig. 1 and Fig. 4. Compared with previous state-of-the-art methods, _PhysHOI_ significantly improves the success rate and object trajectory errors. _PhysHOI_ is simple yet effective and easy to generalize across diverse types of HOI tasks. We hope this work could pave the path for humanoids to learn general HOI skills. 

## **2. Related Work** 

Related works on physically simulated humanoids can be divided into isolated motion imitation and human-object interaction learning. We compare the most related **physicsbased** work in Tab. 1 and present the related **kinematicsbased** methods in the Appendix. 

**Physics-Based Isolated Motion Imitation.** Physics-based methods generate motions via motor control in physics simulation [13, 62, 97], which addresses the physically implausible artifacts of kinematic methods [9, 28, 56, 96, 118, 120], _e.g_ ., penetration, sliding, and floating. Early works rely on hand-crafted [35], model-based [12], and optimization-based [94] controllers, which suffer from motion artifacts and complex parameter tuning. Recently, DeepMimic [69] proposes tracking motion capture sequences via imitation learning and deep reinforcement learning (RL). To make the generation diverse, AMP [71] uses generative adversarial imitation learning (GAIL) [33], which learns the state transition distribution of unstructured motion dataset. Except for RL-based methods, some methods use physics simulation with fully differentiable pipelines [20, 78, 112]. Some works combine kinematic methods with physics-based imitation policy [60, 80, 114, 116] to obtain physically plausible motions. However, these methods only imitate isolated human motion. 

**Physics-based Human-Object Interaction.** Humanobject interaction (HOI) faces more challenges and is less explored than isolated motion generation due to the complexity of human body parts, various objects, and diverse interactions. Compared to kinematics-based methods [75, 89, 105], physics-based methods are especially advantageous for generating human-object interaction since the physics simulator can explicitly constrain the dynamics of humanoids and objects. Using simulation, one can 



<!-- Start of picture text -->
Physics<br>a t Simulator<br>Simulated  Policy Simulated<br>MoCap HOI state HOI state<br>... g t s t Task-agnostic HOI imitation reward g t +1 s t +1 ...<br>Kinematic Rewards CG Reward<br>h t +1 × × × ... h t +2<br>Contact<br>Reference  Body Object IG Graph Reference<br>HOI state HOI state<br>HOI demonstration HOI data PhysHOI HOI skill<br><!-- End of picture text -->

Figure 2. **Framework overview** : The proposed pipeline of learning HOI skills from HOI demonstrations. We can obtain kinematic HOI data using mocap devices or estimated from monocular videos. Then, we transfer the HOI data into the reference HOI states, which is a contact-aware HOI representation _{human motion, object motion, interaction graph (IG), contact graph (CG)}_ for _PhysHOI_ to learn. **_PhysHOI_** : The training process of _PhysHOI_ consists of loops of simulation and optimization. Given the simulated HOI state **_g_** _t_ and reference HOI state **_h_** _t_ +1, the policy outputs the action **_a_** _t_ , then the simulated HOI state will be updated by the physics simulator. For each time step, we calculate the proposed task-agnostic HOI imitation reward, including kinematic rewards and the key CG reward. We train the policy until converges, where it can control simulated humanoids to reproduce the reference HOI skills. 

create realistic human-object interactions such as carrying boxes [31, 109], striking [72], climbing ropes [1], grasping [6], and even challenging sports such as skating [54], playing basketball [51], soccer [38, 108], football [55] and tennis [116]. However, these methods rely on manual task-specific reward designs, making them difficult to generalize. Besides, there are active topics on human-scene interaction [65, 105] and hand-object interaction [11, 15, 21, 66, 111, 115]. 

A highly related work is [122], where the proposed interaction graph [32] is integrated into kinematic rewards to learn the simulated multi-character interaction. Though effective in simple human-object interactions ( _e.g_ . picking up boxes), the kinematic-only rewards are prone to fall into local optimal when dealing with high-dynamic scenarios. Another closely related work is [6], a framework for physically plausible whole-body grasping. Similar to previous kinematics-based grasping synthesis methods [24, 104], they design task-specific contact rewards as guidance for learning grasp tasks. However, their method contains multiple networks and training rounds with prior learning dedicated to the grasp tasks. Our work explores whole-body object interaction with static or high-dynamic objects (e.g., grasping, playing with balls) without designing task-specific rewards. 

## **3. Method** 

### **3.1. Preliminaries on Reinforcement Learning** 

Our method is based on reinforcement learning, where the agent interacts with the environment according to a policy to maximize reward. At each time step _t_ , the agent takes the system states **s** _t_ as input and outputs an action **a** _t_ by sampling the policy distribution **_π_** ( **a** _t|_ **s** _t_ ). According to the physics simulator **_f_** ( **s** _t_ +1 _|_ **a** _t,_ **s** _t_ ), the new action **a** _t_ will result in a new state **s** _t_ +1. Then a reward _rt_ = _r_ ( **s** _t,_ **a** _t,_ **s** _t_ +1) can be calculated, and the goal is to learn a policy that max- 

imizes the expected return _R_ ( **_π_** ) = E _p_ **_π_** ( **_τ_** ) �� _tT_ =0 _−_ 1<sup>_γtrt_</sup> �, where **_τ_** = _{_ **s** 0 _,_ **a** 0 _, r_ 0 _, ...,_ **s** _T −_ 1 _,_ **a** _T −_ 1 _, rT −_ 1 _,_ **s** _T }_ represents the trajectory, _p_ **_π_** ( **_τ_** ) is the probability density function (PDF) of the trajectory. _T_ denotes the time horizon of a trajectory, and _γ ∈_ [0 _,_ 1) is a discount factor. Following prior arts [71], We use PPO [79] to optimize the policy. 

### **3.2. Task Definition** 

Given a reference demonstration of Human-Object Interaction (HOI), represented by a kinematic sequence of human and object states, HOI imitation aims to train a policy to control the simulated humanoid to reproduce the given HOI. Unlike kinematics-based methods [24, 44, 89], the core challenge here is that the object is not directly controllable. Instead, we can only indirectly manipulate objects by controlling the humanoid. The whole-body humanoid follows the SMPL-X [68] kinematic tree and has a total of 52 body parts and 51 _×_ 3 DoF actuators where 30 _×_ 3 DoF is for the hands and 21 _×_ 3 DoF for the rest of the body. The object is represented as a rigid body with a simplified mesh for collision detection. Details on the HOI data preprocessing can be found in the Appendix. 

### **3.3. Overview of PhysHOI** 

In Fig. 2, we present the overview of the proposed pipeline for HOI imitation. The core of _PhysHOI_ is the generalpurpose contact graph (Sec. 3.4), introducing it into the kinematics-based HOI representation as the contact-aware HOI representation (Sec. 3.5), and the task-agnostic HOI imitation reward (Sec. 3.6). Similar to prior arts [69], policy training consists of a loop of simulation and optimization: the policy is first used for simulation and then optimized through RL (Sec. 3.1), then the updated policy continues simulation to collect more experiences and repeat this simulation-optimization loop until converges. Specifically, the state **_s_** _t_ (Sec. 3.7) consists of the simulated HOI state 

**_g_** _t_ and the reference HOI state **_h_**<sup>ˆ</sup> _t_ +1 (Sec. 3.5). The policy network (Sec. 3.8) takes the state **_s_** _t_ as input and outputs an action **_a_** _t ∈_ R<sup>51</sup><sup>_×_3</sup> . The PD controller outputs joint torques (omitted in Fig. 2 for simplicity). Then the physics simulator calculates the updated simulated HOI state **_g_** _t_ +1. 

### **3.4. General-purpose Contact Graph** 

Contact information is essential for HOI. Though contact forces are hard to acquire, binary contact labels are easy to extract from kinematic HOI data by calculating the mesh collision or distances. In addition, estimating the contact region from images is also a feasible direction [98]. We propose a general-purpose Contact Graph (CG) to enhance the HOI representation across diverse interaction imitations. **Complete CG.** As illustrated in Fig. 3 (a), the CG is a complete graph in which every pair of distinct nodes connected by a unique edge, defined as _G_ = _{V, E}_ , where _V_ is the set of _k_ nodes and _E ∈{_ 0 _,_ 1 _}_<sup>_k_(</sup><sup>_k−_1)</sup><sup>_/_2</sup> is the set of edges. The nodes consist of all the objects and humanoid body parts. Each edge stores a binary label that denotes the contact between two nodes, where 1 represents contact, and 0 means no contact. Here, we only use the edge set of CG. The edge value is calculated frame by frame. For an HOI sequence, we can calculate a corresponding CG sequence _{Et}_ , which explicitly describes the mutual contact relationship between objects and bodies at different moments. Considering the trend of hinged objects, objects here can also be broken up into finer parts [18, 23, 115]. 

**Aggregated CG.** There are three limitations in the implementation of the complete CG defined above. First, in the whole-body grasp scenario, the complete CG has 154 nodes (152 body parts, 1 table, and 1 object) and 11781 edges, which is costly in memory and computation. Second, many contact labels may be noisy due to inevitable errors from kinematic HOI estimation and annotation. Third, the contact APIs in existing physics simulation environments [62] are not yet complete. To address these challenges, we propose the aggregated CG, where the graph node can be composed of multiple aggregated parts, as illustrated in Fig. 3 (b). For example, in basketball scenarios, we can aggregate two hands as one node, the rest of the bodies as a node, and the ball as a node. As long as there is any collision between two aggregated nodes, _e.g_ ., the fingertip touches the ball; the corresponding edge value becomes one. Contact between parts belonging to the same node is not considered. The aggregated CG significantly simplifies the use of CG and proves to be critical for simulated humanoid learning accurate HOI imitation. 

### **3.5. Contact-Aware HOI Representation** 

Zhang _et al_ . [122] introduced kinematics-based representation, including human (subject) motion ˆ **_s_**<sup>_sbj_</sup> _t_ , object motion **_s_** ˆ<sup>_obj_</sup> _t_ , interaction graph (IG) **_s_** ˆ<sup>_ig_</sup> _t_<sup>.Wefurtherintroducethe</sup> 



<!-- Start of picture text -->
0<br>0 ...<br>... Aggregated Aggregated<br>Part 1 Part 2 parts 1 parts 2<br>0 0<br>0 1 0 1<br>0 1<br>...<br>0 ...<br>Obj 1 Obj 2 Obj 1 0 Obj 2<br>(a) Contact graph (b) Aggregated contact graph<br><!-- End of picture text -->

Figure 3. **Contact Graph** . ( **a** ) The nodes of the complete contact graph consist of all the objects and humanoid body parts. Each edge stores a binary contact label. ( **b** ) A node in the aggregated contact graph can contain multiple body parts. 

proposed CG ˆ **_s_**<sup>_cg_</sup> _t_<sup>to represent the reference HOI state</sup><sup>**_h_**ˆ</sup><sup>_t_:</sup> 



The human motion **_s_** ˆ<sup>_sbj_</sup> _t_ consists of the position **_s_** ˆ<sup>_p_</sup> _t ∈_ R<sup>52</sup><sup>_×_3</sup> , 6D rotation **_s_** ˆ<sup>_r_</sup> _t_<sup>_∈_R52</sup><sup>_×_6,positionvelocity</sup><sup>**_s_**ˆ</sup> _t_<sup>_pv_</sup> _∈_ R<sup>52</sup><sup>_×_3</sup> , and rotation velocity ˆ **_s_**<sup>_rv_</sup> _t ∈_ R<sup>52</sup><sup>_×_6</sup> . The object motion consists of the object position **_s_** ˆ<sup>_op_</sup> _t ∈_ R<sup>1</sup><sup>_×_3</sup> , object 6D rotation ˆ **_s_**<sup>_or_</sup> _t ∈_ R<sup>1</sup><sup>_×_6</sup> , object position velocity ˆ **_s_**<sup>_opv_</sup> _t ∈_ R<sup>1</sup><sup>_×_3</sup> , and object rotation velocity **_s_** ˆ<sup>_orv_</sup> _t ∈_ R<sup>1</sup><sup>_×_6</sup> . All velocities = here are calculated via discrete differences, _e.g_ . **_s_** ˆ<sup>_opv_</sup> _t_ **_s_** ˆ<sup>_op_</sup> _t −_ **_s_** ˆ<sup>_op_</sup> _t−_ 1<sup>.TheIGusedinthispaperisinspiredbypre-</sup> vious works [32, 122], but with a simpler definition: A set of positional vectors pointed from the objects to the contact bodies (the body parts that have been in contact with the object throughout the sequence). The IG **_s_** ˆ<sup>_ig_</sup> _t_<sup>_∈_R</sup><sup>_n×m×_3can</sup> be seen as a relative position representation of the object, where _n_ denotes the contact body numbers and _m_ denotes the object numbers. The CG ˆ **_s_**<sup>_cg_</sup> _t_<sup>_∈{_0</sup><sup>_,_1</sup><sup>_}k_(</sup><sup>_k−_1)</sup><sup>_/_2, where</sup><sup>_k_</sup> denotes the number of CG nodes. 

### **3.6. Task-agnostic HOI Imitation Reward** 

Corresponding to the reference HOI state (Sec. 3.5), the proposed task-agnostic HOI imitation reward consists of four parts: the body motion reward _rt_<sup>_b_,theobjectmotion</sup> reward _rt_<sup>_o_,theIGreward</sup><sup>_r_</sup> _t_<sup>_ig_,andtheCGreward</sup><sup>_r_</sup> _t_<sup>_cg_.To</sup> obtain balanced reward values, we _multiply_ these rewards to request that none of them be small: 



**Body Motion Reward** can be formulated as: 



where _rt_<sup>_p_,</sup><sup>_r_</sup> _t_<sup>_r_,</sup><sup>_r_</sup> _t_<sup>_pv_,</sup><sup>_r_</sup> _t_<sup>_rv_</sup> are the humanoid position reward, rotation reward, position velocity reward, and rotation velocity reward, formulated below: 





Figure 4. Our method controls simulated humanoids to perform various basketball skills. **Top-to-bottom** : 1) Rebound; 2) Single-hand toss and catch; 3) Back dribbling; 4) Cross-leg dribble. We mark red when the object has contact with the humanoid. 



**_s_** ˆ<sup>_p_</sup> _t_<sup>,</sup><sup>**_s_**ˆ</sup><sup>_r_</sup> _t_<sup>,</sup><sup>**_s_**ˆ</sup> _t_<sup>_pv_,</sup><sup>**_s_**ˆ</sup><sup>_rv_</sup> _t_ are the components of the reference HOI state: the humanoid position, rotation, velocity, and rotation velocity. **_s_**<sup>_p_</sup> _t_<sup>,</sup><sup>**_s_**</sup><sup>_r_</sup> _t_<sup>,</sup><sup>**_s_**</sup> _t_<sup>_pv_,</sup><sup>**_s_**</sup><sup>_rv_</sup> _t_<sup>are calculated from simulation and</sup> is aligned with the reference HOI state in format. _λ_<sup>_p_</sup> , _λ_<sup>_r_</sup> , _λ_<sup>_pv_</sup> , _λ_<sup>_rv_</sup> are hyperparameters that conditions the sensitivity. **Object Motion Reward.** Similar to the human motion reward, the object motion reward is: 



where _rt_<sup>_op_,</sup><sup>_r_</sup> _t_<sup>_or_,</sup><sup>_r_</sup> _t_<sup>_opv_</sup> , _rt_<sup>_orv_</sup> are the object position reward, rotation reward, position velocity reward, and rotation velocity reward, respectively. The calculation of these rewards is similar to the Eq. 4, with _λ_<sup>_op_</sup> , _λ_<sup>_or_</sup> , _λ_<sup>_opv_</sup> , _λ_<sup>_orv_</sup> denotes the hyperparameters that condition the reward sensitivity. **Interaction Graph Reward.** The reward for the IG is: 



where ˆ **_s_**<sup>_ig_</sup> _t_<sup>is the reference and</sup><sup>**_s_**</sup><sup>_ig_</sup> _t_<sup>is calculated from current</sup> simulation. Note that the body motion reward _rt_<sup>_b_,object</sup> motion reward _rt_<sup>_o_, and IG reward</sup><sup>_r_</sup> _t_<sup>_ig_are all measurements</sup> of kinematic properties. We call them kinematic rewards. **Contact Graph Reward.** Though kinematic rewards can handle simple interactions, they usually do not handle dynamic scenarios and are not robust to noisy data, _e.g_ ., dur- 

ing the training of grasp tasks, the contact between the humanoid and the object will, in most cases, cause the object to move away from the desired trajectory and the expected return becomes smaller. In this case, the policy may learn not to touch the object and falls into a local optimal, as demonstrated in Fig. 7 (8). We observe that these issues are highly related to unwanted contacts. To encourage accurate contact with the object, we design the contact graph (Sec. 3.4) and a corresponding contact graph reward (CGR) to guide the humanoid to learn correct contact. The CG error is defined as 



where _| · |_ represent element wise absolute value. The CGR is measured by CG error, with independent weights on different edges: 



where _J_ = _k_ ( _k−_ 1) _/_ 2 is the CG edge numbers; **_e_**<sup>_cg_</sup> _t_<sup>[</sup><sup>_j_] is the</sup> _j_ th element of **_e_**<sup>_cg_</sup> _t ∈{_ 0 _,_ 1 _}_<sup>_J_</sup> , a binary label representing a CG edge error; **_λ_**<sup>_cg_</sup> [ _j_ ] is the _j_ th element of **_λ_**<sup>_cg_</sup> _∈_ R<sup>_J_</sup> , a hyperparameter controls the sensitivity of a CG edge. We multiply the CGR with the previous kinematic rewards. With the guidance of CGR, the humanoid learns the correct contact and avoids the local optimal of kinematic rewards. The ablation study in Fig. 7 and Tab. 2 justifies our design. 

### **3.7. State** 

The state **_s_** _t_ is the input of the policy, consisting of two parts: the simulated HOI state **_g_** _t_ and the reference HOI state **_h_**<sup>ˆ</sup> _t_ +1 (Sec. 3.5): 



where the reference HOI state **_h_**<sup>ˆ</sup> _t_ +1 is the target that we expect the humanoid and objects to reach in the next time step. The simulated HOI state represents the current humanoid and object state under simulation and is necessary for the policy to sense the current environment. Similar to previous works [69], we transform all coordinates into the root local coordinate of the humanoid, simplifying data distribution and making it more conducive to learning. For the humanoid, we observe its global root height, local body position, rotation, position velocity, and rotation velocity. These representations form the humanoid (subject) observation **_o_**<sup>_sbj_</sup> _t_ . In addition, we detect net contact forces **_o_**<sup>_f_</sup> _t_ for the contact bodies (e.g., fingers), which helps to identify contact and accelerate training. For objects, we observe their local position, rotation, velocity, and rotation velocity, which form the object observation **_o_**<sup>_obj_</sup> _t_ . The simulated HOI state can be formulated as: 



### **3.8. Policy and Action** 

We follow the actor-critic framework widely used by prior arts [71, 72]. The policy output is modeled as a Gaussian distribution of dimensions 51 _×_ 3 with constant variance, and the mean is modeled by a two-layer MLP of [1024, 512] units and ReLU activations. The action **_a_** _t ∈_ R<sup>51</sup><sup>_×_3</sup> sampled from the policy is the target joint rotations for the PD controller. The PD controller adjusts and outputs the joint torques to reach the target rotations. 

### **3.9. Simulation Setting** 

The simulation and the PD controller run at 60 Hz. The policy is sampled at 30Hz. The humanoid and objects need initialization when the simulation starts. We use fixed initialization by default; that is, we extract the rotations and root positions from the first reference frame to initialize the humanoids and objects. We do not use random initialization since the HOI data may have severe collisions that eject the object. We use early termination depending on the time and kinematic state errors. See the Appendix for details. 

## **4. The BallPlay Dataset** 

To compensate for the lack of dynamic HOI scenarios, we introduce the _BallPlay_ dataset containing **eight** whole-body basketball skills, including _back dribble, cross leg, hold, fingertip spin, pass, backspin, cross, and rebound_ , as shown 

in Fig. 5. Instead of using MoCap devices that are costly and hard to scale up, we apply a monocular annotation solution to estimate the high-quality human SMPL-X parameters and object translations from RGB videos. However, annotating these videos with high-speed and dynamic movements and complex interactions in the 3D camera coordinate is quite challenging. Inspired by the whole-body annotation pipeline of Motion-X [52], our automatic annotation additionally introduces depth estimation [3], semantic segmentation [26], and CAD model selection to obtain high-quality whole-body human motions and object motions. Besides, we manually annotate three key contact frames for each video to help the object depth estimation. The dataset contains videos, estimated HOI sequences, contact labels, and physically rectified HOI sequences using _PhysHOI_ . Annotation details can be found in the Appendix. 



<!-- Start of picture text -->
Back dribble Cross leg<br>Hold Fingertip spin<br>Pass Back spin<br>Cross Rebound<br><!-- End of picture text -->

Figure 5. **The** **_BallPlay_ dataset.** We show the eight HOI demonstrations of high-dynamic basketball skills. For each skill, the **upper** rows show the real-life videos, and the **lower** rows give the estimated whole-body SMPL-X human model and object mesh. 



<!-- Start of picture text -->
Reference<br>DeepMimic*<br>AMP*<br>Zhang  et al .*<br>PhysHOI<br><!-- End of picture text -->

Figure 6. **Qualitative results on HOI imitation.** *means re-implemented methods. Previous methods that use kinematic-only rewards fail to reproduce the interaction accurately, e.g., the ball falls or the grasp fails. Guided by the contact graph, our method yields successful HOI imitation. We mark the object red when it has contact with the humanoid. We outline in red the frame where the failure begins. 

## **5. Experiment** 

### **5.1. Evaluation on HOI Imitation** 

**Datasets.** We evaluate _PhysHOI_ on two types of HOI datasets: GRAB [92] and our proposed BallPlay (Sec. 4). We chose 5 cases from the GRAB S8 subset, including _grasping cube, cylinder, flashlight, flute, and bottle_ . 

**Metrics.** We report three types of metrics: 1) the success rate (Succ) of HOI imitation, where the success is defined per frame, deeming imitation successful when the object position and body position errors are both under the thresholds and the contact graph edge value is correct. The Succ is calculated by averaging the success values of all frames. The object threshold is defined as 0.2 _m_ . The body threshold is defined as 0.1 _m_ . The Succ reflects whether the humanoid can accurately imitate the reference body motion to interact with the object correctly. 2) the mean per-joint position error (MPJPE) of the humanoid ( _E_ b-mpjpe) and object ( _E_ o-mpjpe) to evaluate the positional tracking performance (in _mm_ ) following [60]. 3) the contact accuracy _E_ cg, ranging from 0 to 1, defined as _N_ <u>1</u> � _Nt_ =1<sup>MSE(</sup><sup>**_s_**</sup> _t_<sup>_cg,_ˆ</sup><sup>**_s_**</sup><sup>_cg_</sup> _t_<sup>)where</sup> N is the total frames of the reference HOI data. 

**Baseline Methods.** To the best of our knowledge, our proposed _PhysHOI_ is the first whole-body HOI imitation method. For fair comparisons, we make proper adaptations for previous human motion imitation methods to experiment on HOI imitation tasks: (1) DeepMimic [69] is a motion imitation method using additive motion rewards; 

we add the object motion reward to it; (2) AMP [71] is an unaligned motion imitation method, we modify its reference state as our proposed contact-aware HOI representation from Sec.3.5; (3) We implement a simplified version of Zhang’s method [122] via our interaction graph (Sec. 3.5) since the code is not available yet. 

**Implementation Details.** We use Isaac Gym [62] as the physics simulation platform. All experiments are trained on a single Nvidia A100 GPU, with 2048 parallel environments and fixed simulation initialization. We train 5000 epochs for all experiments on the GRAB dataset, and 15000 epochs for all experiments on the BallPlay dataset. Each epoch contains 10 frames of sequential simulation. We use the aggregated contact graph (CG) for experiments. For GRAB, the CG contains 3 nodes: the table, the object, and the aggregated whole body. For BallPlay, the CG contains 3 nodes: the object, aggregated hands, and the aggregated rest body parts. We do not consider the basketball rotation since it is not provided, _i.e_ ., we set _λ_<sup>_or_</sup> and _λ_<sup>_orv_</sup> as zero for experiments on BallPlay. The setting of hyperparameters can be found in the Appendix. 

**Qualitative Results.** From Fig. 6, DeepMimic [69] and AMP [71] achieve reasonable humanoid motion but fail to control the object. Zhang _et al_ . [122] is effective on some interactions but is also prone to local optima due to the lack of contact guidance. We highlight the failure beginning frames in red outlines. In contrast, the proposed _PhysHOI_ introduces the contact graph that makes it able to handle 



<!-- Start of picture text -->
(1) Ref (2) w/o CGR (3) w/ CGR (4) Ref (5) w/o CGR (6) w/ CGR (7) Ref (8) w/o CGR (9) w/ CGR (10) Ref (11) w/o CGR on table (12) w/ CGR<br><!-- End of picture text -->

Figure 7. **Ablation on Contact Graph Reward (CGR).** Without CGR, the humanoid is easy to fall into local optimal, e.g., ( **2** ) using the head to help control the ball, ( **5** ) using the wrist to touch the ball, ( **8** ) being afraid of catching objects, ( **11** ) supporting the table to keep balance. In comparison, the use of CGR effectively guides the humanoid toward correct interaction, as shown in ( **3** ), ( **6** ), ( **9** ), and ( **12** ). 

|||DeepM|imic*|||Zhang|_et al_. *|||**_PhysHO_**|**_I_ (Ours)**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Dataset|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|
|_GRAB_|27.0%|**44.7**|180.2|0.7240|38.6%|91.0|180.1|0.3370|**95.4%**|71.1|**78.0**|**0.0260**|
|_BallPlay_|7.5%|**40.1**|1662.5|0.3063|13.6%|88.5|155.3|0.4124|**82.4%**|56.8|**82.9**|**0.0877**|



Table 2. **Quantitative results on HOI imitation.** Our method yields superior object control and success rate on HOI imitation. *means re-implemented methods. We repeat all sequences 10 times, report the average values, and **bold** the best score. 

|||_r_<sup>_b_</sup><br>_t _<sup>_∗_</sup>|<sup>_ro_</sup><br>_t_|||_r_<sup>_b_</sup><br>_t _<sup>_∗r_</sup><br>_t_|<sup>_o_</sup><br> <sup>_∗rig_</sup><br>_t_|||_r_<sup>_b_</sup><br>_t _<sup>_∗ro_</sup><br>_t _<sup>_∗_</sup>|<sup>_rig_</sup><br>_t _<sup>_∗rcg_</sup><br>_t_||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|HOI Data|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|Succ_↑_|_E_b-mpjpe _↓_|_E_o-mpjpe _↓_|_E_cg _↓_|
|_Toss_|20.7%|79.9|**31.9**|0.3837|7.7%|86.9|154.3|0.4396|**84.8%**|**45.7**|77.9|**0.0767**|
|_Cross leg_|6.7%|292.4|246.2|0.5189|8.2%|**42.0**|**51.6**|0.5394|**88.2%**|54.1|92.3|**0.0843**|
|_Backspin_|0.2%|1247.8|7105.6|0.5460|21.7%|**50.4**|74.9|0.3908|**70.3%**|60.2|**65.2**|**0.1302**|
|_Pass_|4.8%|616.5|1047.7|0.5118|16.2%|203.8|418.0|0.2909|**71.2%**|**72.5**|**110.6**|**0.1135**|



Table 3. **Ablation on rewards.** The interaction graph reward _rt_<sup>_ig_can refine the interaction and motion imitation quality.The contact graph</sup> reward _rt_<sup>_cg_</sup> significantly improves the overall performance, especially the success rate, on HOI imitation. 

#### various complex interactions. 

**Quantitative Results.** Tab. 2 shows the average metrics on the GRAB subset and the BallPlay dataset. DeepMimic [69] achieves the best score in body motion metrics, _i.e_ ., _E_ b-mpjpe, since it only learns human motions. It fails to control the object and results in low interaction success rates. Zhang _et al_ . [122] achieves better interaction than DeepMimic, but still yields low success rates because only learning kinematic information. Interestingly, their body imitation errors increase severely, and the contact accuracy worsens for dynamic HOI. In contrast, _PhysHOI_ with CG provides effective contact guidance on HOI learning and yields superior success rates. 

### **5.2. Ablation on Contact Graph Reward** 

Tab. 3 and Fig. 7 study the effectiveness of CGR. Overall, the use of CGR significantly improves success rates. If it only applies kinematic reward, the humanoid is prone to fall into local optimal. For instance, the kinematic rewards result in decent kinematic metrics on the _Cross leg_ data, but it uses false body parts to control the ball, resulting in inferior HOI imitation in Fig. 7 (5). Similarly, in Fig. 7 (2), on the _Toss_ data, the humanoid wrongly learns to use its head to control the ball. On the contrary, by applying the contact graph reward in Fig. 7 (3) and (6), the humanoid learns correct contact and avoids incorrect collisions. Another interesting phenomenon is that the HOI generated by our methods is more accurate than the reference. From Fig. 7 (1), 

there is a slight floating between the hand and the ball in the reference, while our result fits perfectly. 

Considering contact with multiple objects is also necessary. In the grasp tasks, the humanoid sometimes learns to use its hands to support the table to maintain balance if the table is not considered in the contact graph, as shown in Fig. 7 (11). By involving the table in the contact graph, this local optimal can be well addressed (Fig. 7 (12)). In summary, comprehensive studies have validated the essence and effectiveness of the proposed CGR. 

## **6. Conclusion** 

We present a framework for learning Human-Object Interaction (HOI) skills from HOI demonstrations. Our method is able to imitate a diverse set of highly dynamic basketball skills. We involve the contact graph (CG) to guide the humanoid toward precise object control, which is proven to be critical for HOI imitation and is effective even when the reference HOI data is highly biased. The proposed taskagnostic HOI imitation reward is effective on diverse HOI types without the need to design task-specific rewards. We also introduce an HOI dataset called BallPlay is provided to support research on dynamic HOI. We believe this work opens up many exciting directions for future exploration toward general HOI learning. See the Appendix for more discussions about limitations and future work. 

## **References** 

- [1] Jinseok Bae, Jungdam Won, Donggeun Lim, Cheol-Hui Min, and Young Min Kim. Pmp: Learning to physically interact with environments using part-wise motion priors. _arXiv preprint arXiv:2305.03249_ , 2023. 2, 3 

- [2] Shikhar Bahl, Abhinav Gupta, and Deepak Pathak. Humanto-robot imitation in the wild. In _RSS_ , 2022. 1 

- [3] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka, and Matthias M¨uller. Zoedepth: Zero-shot transfer by combining relative and metric depth. _arXiv preprint arXiv:2302.12288_ , 2023. 6, 2 

- [4] Bharat Lal Bhatnagar, Xianghui Xie, Ilya Petrov, Cristian Sminchisescu, Christian Theobalt, and Gerard Pons-Moll. BEHAVE: Dataset and method for tracking human object interactions. In _CVPR_ , 2022. 3 

- [5] Steven Bohez, Saran Tunyasuvunakool, Philemon Brakel, Fereshteh Sadeghi, Leonard Hasenclever, Yuval Tassa, Emilio Parisotto, Jan Humplik, Tuomas Haarnoja, Roland Hafner, et al. Imitate and repurpose: Learning reusable robot movement skills from human and animal behaviors. _arXiv preprint arXiv:2203.17138_ , 2022. 1 

- [6] Jona Braun, Sammy Christen, Muhammed Kocabas, Emre Aksan, and Otmar Hilliges. Physically plausible full-body hand-object interaction synthesis. In _International Conference on 3D Vision (3DV)_ , 2024. 2, 3 

- [7] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. 2020. 3 

- [8] Angel X Chang, Thomas Funkhouser, Leonidas Guibas, Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese, Manolis Savva, Shuran Song, Hao Su, et al. Shapenet: An information-rich 3d model repository. _arXiv preprint arXiv:1512.03012_ , 2015. 2 

- [9] Xin Chen, Biao Jiang, Wen Liu, Zilong Huang, Bin Fu, Tao Chen, and Gang Yu. Executing your commands via motion diffusion in latent space. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 18000–18010, 2023. 2, 3 

- [10] Yixin Chen, Sai Kumar Dwivedi, Michael J Black, and Dimitrios Tzionas. Detecting human-object contact in images. In _CVPR_ , 2023. 3 

- [11] Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, and Otmar Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for handobject interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 20577–20586, 2022. 3 

- [12] Stelian Coros, Philippe Beaudoin, and Michiel van de Panne. Generalized biped walking control. _ACM Transactions on Graphics_ , 29(4):1–9, 2010. 2 

- [13] Erwin Coumans and Yunfei Bai. Pybullet, a python module for physics simulation for games, robotics and machine learning. 2016. 2 

- [14] Rishabh Dabral, Muhammad Hamza Mughal, Vladislav Golyanik, and Christian Theobalt. Mofusion: A framework for denoising-diffusion-based motion synthesis. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9760–9770, 2023. 3 

- [15] Sudeep Dasari, Abhinav Gupta, and Vikash Kumar. Learning dexterous manipulation from exemplar object trajectories and pre-grasps. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3889– 3896. IEEE, 2023. 3 

- [16] Dawson-Haggerty et al. trimesh. 2 

- [17] Alejandro Escontrela, Xue Bin Peng, Wenhao Yu, Tingnan Zhang, Atil Iscen, Ken Goldberg, and Pieter Abbeel. Adversarial motion priors make good substitutes for complex reward functions. In _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 25– 32. IEEE, 2022. 1 

- [18] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. Arctic: A dataset for dexterous bimanual handobject manipulation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 12943–12954, 2023. 4, 3 

- [19] Katerina Fragkiadaki, Sergey Levine, Panna Felsen, and Jitendra Malik. Recurrent network models for human dynamics. In _2015 IEEE International Conference on Computer Vision (ICCV)_ , 2015. 3 

- [20] Levi Fussell, Kevin Bergamin, and Daniel Holden. Supertrack: Motion tracking for physically simulated characters using supervised learning. _ACM Transactions on Graphics (TOG)_ , 40(6):1–13, 2021. 2 

- [21] Guillermo Garcia-Hernando, Edward Johns, and Tae-Kyun Kim. Physics-based dexterous manipulations with estimated hand poses and residual reinforcement learning. In _2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 9561–9568. IEEE, 2020. 

   - 3 

- [22] Thomas Geijtenbeek and Nicolas Pronost. Interactive character animation using simulated physics: A state-of-the-art review. In _Computer graphics forum_ , pages 2492–2515. Wiley Online Library, 2012. 1 

- [23] Haoran Geng, Helin Xu, Chengyang Zhao, Chao Xu, Li Yi, Siyuan Huang, and He Wang. Gapartnet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 7081–7091, 2023. 4 

- [24] Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik, Christian Theobalt, and Philipp Slusallek. Imos: Intentdriven full-body motion synthesis for human-object interactions. In _Eurographics_ , 2023. 3 

- [25] Georgia Gkioxari, Ross Girshick, Piotr Doll´ar, and Kaiming He. Detecting and recognizing human-object interactions. In _CVPR_ , 2018. 3 

- [26] Grounded-SAM Contributors. Grounded-SegmentAnything: https://github.com/IDEA-Research/GroundedSegment-Anything, 2023. 6, 2 

- [27] Chuan Guo, Xinxin Zuo, Sen Wang, Shihao Zou, Qingyao Sun, Annan Deng, Minglun Gong, and Li Cheng. Action2motion: Conditioned generation of 3d human motions. In _Proceedings of the 28th ACM International Conference on Multimedia_ , 2020. 3 

- [28] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, and Li Cheng. Generating diverse and natural 3d human motions from text. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 5152–5161, 2022. 2, 3 

- [29] F´elix G. Harvey, Mike Yurick, Derek Nowrouzezahrai, and Christopher Pal. Robust motion in-betweening. _ACM Transactions on Graphics_ , 2020. 3 

- [30] Mohamed Hassan, Duygu Ceylan, Ruben Villegas, Jun Saito, Jimei Yang, Yi Zhou, and Michael Black. Stochastic scene-aware motion prediction. In _ICCV_ , 2021. 3 

- [31] Mohamed Hassan, Yunrong Guo, Tingwu Wang, Michael Black, Sanja Fidler, and Xue Bin Peng. Synthesizing physical character-scene interactions. In _ACM SIGGRAPH 2022 Conference Proceedings_ , 2023. 2, 3 

- [32] Edmond SL Ho, Taku Komura, and Chiew-Lan Tai. Spatial relationship preserving character motion adaptation. In _ACM SIGGRAPH 2010 papers_ , pages 1–8, 2010. 3, 4 

- [33] Jonathan Ho and Stefano Ermon. Generative adversarial imitation learning. _Advances in neural information processing systems_ , 29, 2016. 2 

- [34] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. _Advances in Neural Information Processing Systems (NeurIPS)_ , 33, 2020. 3 

- [35] Jessica K. Hodgins, Wayne L. Wooten, David C. Brogan, and James F. O’Brien. Animating human athletics. In _Proceedings of the 22nd annual conference on Computer graphics and interactive techniques - SIGGRAPH ’95_ , 1995. 2 

- [36] Daniel Holden, Jun Saito, and Taku Komura. A deep learning framework for character motion synthesis and editing. _ACM Transactions on Graphics_ , page 1–11, 2016. 3 

- [37] Daniel Holden, Taku Komura, and Jun Saito. Phasefunctioned neural networks for character control. _ACM Transactions on Graphics_ , page 1–13, 2017. 3 

- [38] Seokpyo Hong, Daseong Han, Kyungmin Cho, Joseph S Shin, and Junyong Noh. Physics-based full-body soccer motion control for dribbling and shooting. _ACM Transactions on Graphics (TOG)_ , 38(4):1–12, 2019. 3 

- [39] Zhi Hou, Baosheng Yu, and Dacheng Tao. Compositional 3d human-object neural animation. _arXiv preprint arXiv:2304.14070_ , 2023. 3 

- [40] Yinghao Huang, Omid Taheri, Michael J. Black, and Dimitrios Tzionas. InterCap: Joint markerless 3D tracking of humans and objects in interaction. In _GCPR_ , 2022. 3 

- [41] Jingwei Ji, Rishi Desai, and Juan Carlos Niebles. Detecting human-object relationships in videos. In _ICCV_ , 2021. 3 

- [42] Nan Jiang, Tengyu Liu, Zhexuan Cao, Jieming Cui, Yixin Chen, He Wang, Yixin Zhu, and Siyuan Huang. CHAIRS: 

Towards full-body articulated human-object interaction. _arXiv preprint arXiv:2212.10621_ , 2022. 3 

- [43] Peng Jin, Yang Wu, Yanbo Fan, Zhongqian Sun, Yang Wei, and Li Yuan. Act as you wish: Fine-grained control of motion diffusion model with hierarchical semantic graphs. In _NeurIPS_ , 2023. 3 

- [44] Roy Kapon, Guy Tevet, Daniel Cohen-Or, and Amit H Bermano. Mas: Multi-view ancestral sampling for 3d motion generation using 2d diffusion. _arXiv preprint arXiv:2310.14729_ , 2023. 3 

- [45] Bahjat Kawar, Michael Elad, Stefano Ermon, and Jiaming Song. Denoising diffusion restoration models. In _ICLR Workshop on Deep Generative Models for Highly Structured Data (ICLRW)_ , 2022. 3 

- [46] Taeksoo Kim, Shunsuke Saito, and Hanbyul Joo. NCHO: Unsupervised learning for neural 3d composition of humans and objects. In _ICCV_ , 2023. 3 

- [47] Jiye Lee and Hanbyul Joo. Locomotion-actionmanipulation: Synthesizing human-scene interactions in complex 3d environments. _arXiv preprint arXiv:2301.02667_ , 2023. 3 

- [48] Jiaman Li, Jiajun Wu, and C Karen Liu. Object motion guided human motion synthesis. _arXiv preprint arXiv:2309.16237_ , 2023. 3 

- [49] Ruilong Li, Shan Yang, David A. Ross, and Angjoo Kanazawa. Learn to dance with aist++: Music conditioned 3d dance generation, 2021. 3 

- [50] Yuanzhi Liang, Qianyu Feng, Linchao Zhu, Li Hu, Pan Pan, and Yi Yang. Seeg: Semantic energized co-speech gesture generation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 10473– 10482, 2022. 3 

- [51] Jessica Hodgins Libin Liu. Learning basketball dribbling skills using trajectory optimization and deep reinforcement learning. _ACM Transactions on Graphics_ , 37(4), August 2018. 3 

- [52] Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, Ruimao Zhang, Haoqian Wang, and Lei Zhang. Motion-x: A largescale 3d expressive whole-body human motion dataset. _Advances in Neural Information Processing Systems_ , 2023. 6, 2, 3 

- [53] Hung Yu Ling, Fabio Zinno, George Cheng, and Michiel Van De Panne. Character controllers using motion vaes. _ACM Transactions on Graphics_ , 2020. 1, 3, 4 

- [54] Libin Liu and Jessica Hodgins. Learning to schedule control fragments for physics-based characters using deep q- learning. _ACM Transactions on Graphics_ , 36(3), 2017. 3 

- [55] Siqi Liu, Guy Lever, Zhe Wang, Josh Merel, SM Ali Eslami, Daniel Hennes, Wojciech M Czarnecki, Yuval Tassa, Shayegan Omidshafiei, Abbas Abdolmaleki, et al. From motor control to team play in simulated humanoid football. _Science Robotics_ , 7(69):eabo0235, 2022. 3 

- [56] Shunlin Lu, Ling-Hao Chen, Ailing Zeng, Jing Lin, Ruimao Zhang, Lei Zhang, and Heung-Yeung Shum. Humantomato: Text-aligned whole-body motion generation. _arxiv:2310.12978_ , 2023. 2, 3 

- [57] Michael Luck and Ruth Aylett. Applying artificial intelligence to virtual reality: Intelligent virtual environments. _Applied artificial intelligence_ , 14(1):3–32, 2000. 1 

- [58] Zhengyi Luo, Ryo Hachiuma, Ye Yuan, and Kris Kitani. Dynamics-regulated kinematic policy for egocentric pose estimation. In _Advances in Neural Information Processing Systems_ , 2021. 1 

- [59] Zhengyi Luo, Shun Iwase, Ye Yuan, and Kris Kitani. Embodied scene-aware human pose estimation. In _Advances in Neural Information Processing Systems_ , 2022. 1 

- [60] Zhengyi Luo, Jinkun Cao, Alexander Winkler, Kris Kitani, and Weipeng Xu. Perpetual humanoid control for real-time simulated avatars, 2023. 2, 7 

- [61] Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard Pons-Moll, and Michael J. Black. AMASS: Archive of motion capture as surface shapes. In _International Conference on Computer Vision_ , pages 5442–5451, 2019. 3 

- [62] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel State. Isaac gym: High performance GPU based physics simulation for robot learning. In _Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)_ , 2021. 2, 4, 7 

- [63] Julieta Martinez, Michael J. Black, and Javier Romero. On human motion prediction using recurrent neural networks. In _2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2017. 3 

- [64] Lucas Mourot, Ludovic Hoyet, Franc¸ois Le Clerc, Franc¸ois Schnitzler, and Pierre Hellier. A survey on deep learning for skeleton-based human animation. In _Computer Graphics Forum_ , pages 122–157. Wiley Online Library, 2022. 1 

- [65] Liang Pan, Jingbo Wang, Buzhen Huang, Junyu Zhang, Haofan Wang, Xu Tang, and Yangang Wang. Synthesizing physically plausible human motions in 3d scenes. _arXiv preprint arXiv:2308.09036_ , 2023. 3 

- [66] Austin Patel, Andrew Wang, Ilija Radosavovic, and Jitendra Malik. Learning to imitate object interactions from internet videos. _arXiv preprint arXiv:2211.13225_ , 2022. 3 

- [67] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani, Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas, and Michael J. Black. Expressive body capture: 3D hands, face, and body from a single image. In _Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)_ , pages 10975–10985, 2019. 1 

- [68] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani, Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas, and Michael J. Black. Expressive body capture: 3d hands, face, and body from a single image. In _Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)_ , 2019. 2, 3 

- [69] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel van de Panne. Deepmimic. _ACM Transactions on Graphics_ , page 1–14, 2018. 1, 2, 3, 6, 7, 8 

- [70] Xue Bin Peng, Erwin Coumans, Tingnan Zhang, TsangWei Edward Lee, Jie Tan, and Sergey Levine. Learning agile robotic locomotion skills by imitating animals. In _Robotics: Science and Systems_ , 2020. 

- [71] Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, and Angjoo Kanazawa. Amp: Adversarial motion priors for stylized physics-based character control. _ACM Transactions on Graphics_ , page 1–20, 2021. 2, 3, 6, 7 

- [72] Xue Bin Peng, Yunrong Guo, Lina Halper, Sergexuey Levine, and Sanja Fidler. Ase: Large-scale reusable adversarial skill embeddings for physically simulated characters. _ACM Trans. Graph._ , 41(4), 2022. 1, 3, 6, 2 

- [73] Ilya A Petrov, Riccardo Marin, Julian Chibane, and Gerard Pons-Moll. Object pop-up: Can we infer 3d objects and their poses from human interactions alone? In _CVPR_ , 2023. 3 

- [74] Mathis Petrovich, Michael J. Black, and Gul Varol. Actionconditioned 3d human motion synthesis with transformer vae. In _2021 IEEE/CVF International Conference on Computer Vision (ICCV)_ , 2021. 3 

- [75] Huaijin Pi, Sida Peng, Minghui Yang, Xiaowei Zhou, and Hujun Bao. Hierarchical generation of human-object interactions with diffusion probabilistic models. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 15061–15073, 2023. 2, 3 

- [76] Matthias Plappert, Christian Mandery, and Tamim Asfour. The KIT motion-language dataset. _Big Data_ , 4(4):236–252, 2016. 3 

- [77] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019. 3 

- [78] Jiawei Ren, Cunjun Yu, Siwei Chen, Xiao Ma, Liang Pan, and Ziwei Liu. Diffmimic: Efficient motion mimicking with differentiable physics. In _The Eleventh International Conference on Learning Representations_ , 2023. 2 

- [79] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_ , 2017. 3 

- [80] Yi Shi, Jingbo Wang, Xuekun Jiang, and Bo Dai. Controllable motion diffusion model. _arXiv preprint arXiv:2306.00416_ , 2023. 2 

- [81] Laura M. Smith, J. Chase Kew, Tianyu Li, Linda Luu, Xue Bin Peng, Sehoon Ha, Jie Tan, and Sergey Levine. Learning and adapting agile locomotion skills by transferring experience. In _Robotics: Science and Systems XIX, Daegu, Republic of Korea, July 10-14, 2023_ , 2023. 1 

- [82] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. _arXiv preprint arXiv:2010.02502_ , 2020. 3 

- [83] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. In _International Conference on Learning Representations (ICLR)_ , 2021. 

- [84] Yang Song and Stefano Ermon. Generative modeling by estimating gradients of the data distribution. _Advances in Neural Information Processing Systems (NeurIPS)_ , 32, 2019. 

- [85] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Scorebased generative modeling through stochastic differential equations. In _International Conference on Learning Representations (ICLR)_ , 2020. 3 

- [86] Jackie Stacey and Lucy Suchman. Animation and automation–the liveliness and labours of bodies and machines. _Body & Society_ , 18(1):1–46, 2012. 1 

- [87] Sebastian Starke, He Zhang, Taku Komura, and Jun Saito. Neural state machine for character-scene interactions. _ACM Trans. Graph._ , 38(6):209–1, 2019. 3 

- [88] Sebastian Starke, Yiwei Zhao, Taku Komura, and Kazi Zaman. Local motion phases for learning multi-contact character movements. _ACM Transactions on Graphics_ , 2020. 3 

- [89] Sebastian Starke, Yiwei Zhao, Taku Komura, and Kazi Zaman. Local motion phases for learning multi-contact character movements. _ACM Transactions on Graphics (TOG)_ , 39(4):54–1, 2020. 2, 3 

- [90] Sebastian Starke, Yiwei Zhao, Fabio Zinno, and Taku Komura. Neural animation layering for synthesizing martial arts movements. _ACM Transactions on Graphics_ , page 1–16, 2021. 

- [91] Sebastian Starke, Ian Mason, and Taku Komura. Deepphase. _ACM Transactions on Graphics_ , 41(4):1–13, 2022. 3 

- [92] Omid Taheri, Nima Ghorbani, Michael J. Black, and Dimitrios Tzionas. GRAB: A dataset of whole-body human grasping of objects. In _European Conference on Computer Vision (ECCV)_ , 2020. 7, 3 

- [93] Omid Taheri, Vasileios Choutas, Michael J. Black, and Dimitrios Tzionas. Goal: Generating 4d whole-body motion for hand-object grasping. In _2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2022. 3 

- [94] Jie Tan, Yuting Gu, C. Karen Liu, and Greg Turk. Learning bicycle stunts. _ACM Transactions on Graphics_ , 33(4):1–12, 2014. 2 

- [95] Purva Tendulkar, D´ıdac Sur´ıs, and Carl Vondrick. Flex: Full-body grasping without full-body grasps. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21179–21189, 2023. 3 

- [96] Guy Tevet, Sigal Raab, Brian Gordon, Yoni Shafir, Daniel Cohen-or, and Amit Haim Bermano. Human motion diffusion model. In _The Eleventh International Conference on Learning Representations_ , 2023. 2, 3 

- [97] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In _2012 IEEE/RSJ international conference on intelligent robots and systems_ , pages 5026–5033. IEEE, 2012. 2 

- [98] Shashank Tripathi, Agniv Chatterjee, Jean-Claude Passy, Hongwei Yi, Dimitrios Tzionas, and Michael J. Black. DECO: Dense estimation of 3D human-scene contact in the wild. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ , pages 8001–8013, 2023. 4 

- [99] Jonathan Tseng, Rodrigo Castellon, and Karen Liu. Edge: Editable dance generation from music. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 448–458, 2023. 3 

- [100] Xi Wang, Gen Li, Yen-Ling Kuo, Muhammed Kocabas, Emre Aksan, and Otmar Hilliges. Reconstructing action- 

conditioned human-object interactions using commonsense knowledge priors. In _3DV_ , 2022. 3 

- [101] Yinhuai Wang, Jiwen Yu, and Jian Zhang. Zero-shot image restoration using denoising diffusion null-space model. In _The Eleventh International Conference on Learning Representations_ , 2023. 3 

- [102] Jungdam Won, Deepak Gopinath, and Jessica Hodgins. Physics-based character controllers using conditional vaes. _ACM Transactions on Graphics (TOG)_ , 41(4):1–12, 2022. 1 

- [103] Xiaoqian Wu, Yong-Lu Li, Xinpeng Liu, Junyi Zhang, Yuzhe Wu, and Cewu Lu. Mining cross-person cues for body-part interactiveness learning in hoi detection. In _ECCV_ , 2022. 3 

- [104] Yan Wu, Jiahao Wang, Yan Zhang, Siwei Zhang, Otmar Hilliges, Fisher Yu, and Siyu Tang. Saga: Stochastic wholebody grasping with contact. In _Proceedings of the European Conference on Computer Vision (ECCV)_ , 2022. 3 

- [105] Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei Zhang, Bo Dai, Dahua Lin, and Jiangmiao Pang. Unified human-scene interaction via prompted chain-of-contacts. _arXiv preprint arXiv:2309.07918_ , 2023. 2, 3 

- [106] Xianghui Xie, Bharat Lal Bhatnagar, and Gerard PonsMoll. Chore: Contact, human and object reconstruction from a single rgb image. In _ECCV_ , 2022. 3 

- [107] Xianghui Xie, Bharat Lal Bhatnagar, and Gerard PonsMoll. Visibility aware human-object interaction tracking from single rgb camera. In _CVPR_ , 2023. 3 

- [108] Zhaoming Xie, Sebastian Starke, Hung Yu Ling, and Michiel van de Panne. Learning soccer juggling skills with layer-wise mixture-of-experts. In _ACM SIGGRAPH 2022 Conference Proceedings_ , pages 1–9, 2022. 3 

- [109] Zhaoming Xie, Jonathan Tseng, Sebastian Starke, Michiel van de Panne, and C. Karen Liu. Hierarchical planning and control for box loco-manipulation, 2023. 3 

- [110] Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, and Liang-Yan Gui. Interdiff: Generating 3d human-object interactions with physics-informed diffusion. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 14928–14940, 2023. 3 

- [111] Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4737–4746, 2023. 3 

- [112] Heyuan Yao, Zhenhua Song, Baoquan Chen, and Libin Liu. Controlvae: Model-based learning of generative controllers for physics-based characters. _ACM Transactions on Graphics (TOG)_ , 41(6):1–16, 2022. 2 

- [113] Youngwoo Yoon, Woo-Ri Ko, Minsu Jang, Jaeyeon Lee, Jaehong Kim, and Geehyuk Lee. Robots learn social skills: End-to-end learning of co-speech gesture generation for humanoid robots. In _2019 International Conference on Robotics and Automation (ICRA)_ , pages 4303–4309. IEEE, 2019. 3 

- [114] Ye Yuan, Jiaming Song, Umar Iqbal, Arash Vahdat, and Jan Kautz. Physdiff: Physics-guided human motion diffusion model, 2022. 2 

- [115] Hui Zhang, Sammy Christen, Zicong Fan, Luocheng Zheng, Jemin Hwangbo, Jie Song, and Otmar Hilliges. Artigrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. _arXiv preprint arXiv:2309.03891_ , 2023. 3, 4 

- [116] Haotian Zhang, Ye Yuan, Viktor Makoviychuk, Yunrong Guo, Sanja Fidler, Xue Bin Peng, and Kayvon Fatahalian. Learning physically simulated tennis skills from broadcast videos. _ACM Trans. Graph._ , 2023. 1, 2, 3 

- [117] Juze Zhang, Haimin Luo, Hongdi Yang, Xinru Xu, Qianyang Wu, Ye Shi, Jingyi Yu, Lan Xu, and Jingya Wang. NeuralDome: A neural modeling pipeline on multi-view human-object interactions. In _CVPR_ , 2023. 3 

- [118] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Shaoli Huang, Yong Zhang, Hongwei Zhao, Hongtao Lu, and Xi Shen. T2m-gpt: Generating human motion from textual descriptions with discrete representations. _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2023. 2, 3 

- [119] Jason Y Zhang, Sam Pepose, Hanbyul Joo, Deva Ramanan, Jitendra Malik, and Angjoo Kanazawa. Perceiving 3d human-object spatial arrangements from a single image in the wild. In _ECCV_ , 2020. 3 

- [120] Mingyuan Zhang, Zhongang Cai, Liang Pan, Fangzhou Hong, Xinying Guo, Lei Yang, and Ziwei Liu. Motiondiffuse: Text-driven human motion generation with diffusion model. _arXiv preprint arXiv:2208.15001_ , 2022. 2, 3 

- [121] Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Vladimir Guzov, and Gerard Pons-Moll. COUCH: Towards controllable human-chair interactions. In _ECCV_ , 2022. 3 

- [122] Yunbo Zhang, Deepak Gopinath, Yuting Ye, Jessica Hodgins, Greg Turk, and Jungdam Won. Simulation and retargeting of complex multi-character interactions. In _ACM SIGGRAPH 2023 Conference Proceedings_ , 2023. 2, 3, 4, 7, 8 

- [123] Desen Zhou, Zhichao Liu, Jian Wang, Leshan Wang, Tao Hu, Errui Ding, and Jingdong Wang. Human-object interaction detection via disentangled transformer. In _CVPR_ , 2022. 3 

- [124] Fangrui Zhu, Yiming Xie, Weidi Xie, and Huaizu Jiang. Diagnosing human-object interaction detectors. _arXiv preprint arXiv:2308.08529_ , 2023. 3 

- [125] Lingting Zhu, Xian Liu, Xuanyu Liu, Rui Qian, Ziwei Liu, and Lequan Yu. Taming diffusion models for audiodriven co-speech gesture generation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 10544–10553, 2023. 3 

# **PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction** 

# Supplementary Material 

In the following document, we provide additional information to supplement the main paper. Video demonstrations can be found on our project page. We will release the BallPlay dataset and open source the code. 

## **Contents** 

#### **A. Technical Details** 

|**A. Technical Details**|**1**|
|---|---|
|A.1. HOI Data Preprocessing . . . . . . . . . . .|1|
|A.2. Details on Simulation Setting<br>. . . . . . . .|1|
|A.3. Experiment Details . . . . . . . . . . . . . .|2|
|**B. The BallPlay Dataset**|**2**|
|B.1. HOI Data Annotation . . . . . . . . . . . . .|2|
|B.2. Refine The HOI Data Using PhysHOI . . . .|2|
|**C. Additional Experiments**|**3**|
|C.1. Varying Ball Sizes . . . . . . . . . . . . . .|3|
|C.2. Ablation on Contact Graph Reward . . . . .|3|
|**D. Related Work on Kinematic-Based Methods**|**3**|
|D.1. Human Motion Generation . . . . . . . . . .|3|
|D.2. Human-Object Interaction Generation . . . .|3|



#### **E. Discussions** 

|**iscussions**|||**4**|
|---|---|---|---|
|E.1. Failure Cases . .|. . . . . .|. .|. . . . . . .<br>4|
|E.2. Limitations . . .|. . . . . .|. .|. . . . . . .<br>4|
|E.3. Future Work<br>. .|. . . . . .|. .|. . . . . . .<br>4|





Figure 8. The original human and object shape ( **bottom** ) and their approximated simulation model ( **up** ). 

simplify collision calculation, bodies are simplified as simple geometries like capsules or boxes. For general objects, we use convex decomposition to approximate the object mesh as convex hulls, which is necessary for collision detection. For the basketball, we simply use a sphere as an approximation. Fig. 8 shows the original human and object shape and the approximated simulation model. 

**HOI Data Calibration.** We transfer the original HOI data to the simulation environment and perform coordinate calibration to obtain preliminary data samples. To accurately model interaction information, we extract and save the body positions and the binary contact labels per frame, which can be easily acquired by reading the simulator’s API after loading the calibrated HOI data into the simulation. This data calibration process is effective in resolving hand-object penetration in the data, because the simulator will automatically adjust the body position to avoid collision. 

## **A. Technical Details** 

### **A.1. HOI Data Preprocessing** 

Since the shapes of humans and objects in HOI data are represented by mesh and cannot be directly used for the simulation environment, we build the simulation models of robots and objects to match their meshes and make necessary calibrations for the HOI data. 

**Raw HOI Data Format.** The raw HOI data consists of frames at 30 fps. Each frame contains the human joint rotation, human root rotation, human root position, object position, and object rotation. We use the SMPL-X model [67] to parameterize the whole-body shape as _β ∈_ R<sup>10</sup> and wholebody pose as _θ ∈_ R<sup>51</sup><sup>_×_3</sup> . The object is represented as mesh. **Simulation Models for Human and Object.** Given an SMPL-X shape parameter _β_ , we generate a corresponding whole-body humanoid robot following UHC [58, 59]. To drive the poses, we use SMPL-X pose parameter _θ_ . Accordingly, the robot has a total of 51 _×_ 3 DoF actuators where 21 _×_ 3 DoF for the body and 30 _×_ 3 DoF for the hands. To 

### **A.2. Details on Simulation Setting** 

**Simulation Initialization.** We use first-frame initialization by default; that is, we extract the rotations and root positions from the first reference state to initialize the robot and objects. 

**Early Termination.** Since our imitation learning is strictly aligned with the reference frame, the maximum duration of the simulation is the length of the reference HOI sequence. In general, during training, the simulation is reset only when the maximum time is reached. However, during the training process, the robot often fails before reaching the maximum time, such as falling down or the object significantly deviating from the reference trajectory. In these cases, we reset the simulation to improve the simulation sample efficiency. Specifically, in three cases we reset the simulation: (1) the maximum time is reached; (2) the object deviates far from the reference trajectory; (3) the robot positions deviate from the reference. The threshold of position error is set to 0.5m. 

|||b|ody|||ob|ject||IG||CG|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Dataset|_λ_<sup>_p_</sup>|_λ_<sup>_r_</sup>|_λ_<sup>_pv_</sup>|_λ_<sup>_rv_</sup>|_λ_<sup>_op_</sup>|_λ_<sup>_or_</sup>|_λ_<sup>_opv_</sup>|_λ_<sup>_orv_</sup>|_λ_<sup>_ig_</sup>|**_λ_**<sup>_cg_</sup>[0]|**_λ_**<sup>_cg_</sup>[1]|**_λ_**<sup>_c_</sup>|<sup>_g_</sup>[2]|
|_BallPlay_|50|20|0.01|0.01|1|0|0.01|0|20|5|5|5||
|_GRAB_|50|20|0.01|0.01|1|0.1|0.01|0.01|20|50|5|5||



Table 4. **Reward weights for PhysHOI.** Note that for the _fingertip spin_ case, we set **_λ_**<sup>_cg_</sup> [0]=0.01 to weak restrictions on contact between hands and the ball, as explained in Fig. 14. 

|||||body|||ob|ject||IG|CG|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Methods|+ or_×_|_r_<sup>_p_</sup>|_r_<sup>_r_</sup>|_r_<sup>_pv_</sup>|_r_<sup>_rv_</sup>|_r_<sup>_op_</sup>|_r_<sup>_or_</sup>|_r_<sup>_opv_</sup>|_r_<sup>_orv_</sup>|_r_<sup>_ig_</sup>|_r_<sup>_cg_</sup>|
|DeepMimic|+|✓|✓|✓|✓|✓|✓|✓|✓|_×_|_×_|
|Zhang_et al_.|_×_|✓|✓|✓|✓|✓|✓|✓|✓|✓|_×_|



Table 5. Reward design for re-implemented methods. 

### **A.3. Experiment Details** 

**Hyperparameters.** We use the aggregated contact graph (CG) for experiments. For GRAB, the CG contains 3 nodes: the table, the object, and the aggregated whole body. For BallPlay, the CG contains 3 nodes: the object, the aggregated hands, and the aggregated rest body parts. We provide the setting of reward weights in Tab. 4. For _BallPlay_ , **_λ_**<sup>_cg_</sup> [0] corresponding to the CG edge connecting the hands and the ball, **_λ_**<sup>_cg_</sup> [1] corresponding to the CG edge connecting the hands and the rest body, **_λ_**<sup>_cg_</sup> [2] corresponding to the CG edge connecting the rest body and the ball. For _GRAB_ , **_λ_**<sup>_cg_</sup> [0] corresponding to the CG edge connecting the body and the object, **_λ_**<sup>_cg_</sup> [1] corresponding to the CG edge connecting the body and the table, **_λ_**<sup>_cg_</sup> [2] corresponding to the CG edge connecting the table and the object. 

**Details on Re-Implemented Methods.** For fair comparisons, we re-implement related state-of-the-art methods: DeepMimic [69], AMP [71], and Zhang’s method [122]. The main difference is the reward design, which is presented in Tab. 5. Note that our code is based on the ASE project [72], which contains the implementation of AMP. We change the original AMP observation as our HOI representation for HOI imitation. 

**Contact Detection.** Since Isaac Gym does not yet provide contact detection APIs for the GPU pipeline, we use force detections as approximations for contact detections. For example, if the net contact force of the ball on either of the x and y axes is above a threshold and the net contact force of the hands-excluded body parts is under a threshold, we deem that the ball has contact with the hands. 

## **B. The BallPlay Dataset** 

### **B.1. HOI Data Annotation** 

To construct the BallPlay dataset, we propose a semiautomatic annotation pipeline to estimate 3D human-object interaction motion from monocular RGB videos. As depicted in Fig. 9, our annotation pipeline mainly involved 

three stages: whole-body human motion annotation, object annotation, and contact-based manual correction. **Whole-Body Human Motion Annotation.** Initially, we adopt an optimization-based approach, as introduced in Motion-X [52], to annotate high-quality 3D whole-body human motion from RGB videos. This optimization process also includes the estimation of camera parameters. 

**Object Annotation.** Subsequently, we employ GroundedSAM [26] to annotate the object category and the segmentation mask, along with utilizing ZoeDepth [3] for depth estimation. We then project the object mask into a point cloud in the world coordinate system based on the depth map and camera parameters. The central point of the resulting point cloud serves as the initialized object center. Meanwhile, based on the object category, we retrieve the object mesh from a CAD model library. The meshes of the CAD model library are collected from ShapeNet [8] and some geometries built by ourselves with Trimesh [16] tool. 

**Contact-based Manual Correction.** Due to the inherent depth ambiguity of monocular video, the object center obtained from the previous steps can be noisy. To address this issue, we propose a contact-based manual correction procedure. Specifically, we manually annotate the human-object contact labels of three keyframes within each video, and then compute the average depth of the contact body parts to update the object center position. This manual correction can greatly mitigate depth ambiguity and enhance overall data quality. Ultimately, our refined object mesh and human mesh constitute the final human-object interaction dataset. 



<!-- Start of picture text -->
Human  BBox Pose Human<br>Detection Optimization Mesh<br>Depth  Depth Camera<br>Estimation Contact Label<br>Grounded - Mask Camera Object<br>SAM Projection Center<br>RGB Image Category CAD Models Object Mesh Output Meshes<br><!-- End of picture text -->

Figure 9. Annotation pipeline of _BallPlay_ . 

**Contact Graph Annotation.** We focus on basketball skills that involve only hands to interact with the ball. In this scenario, we aggregate all elements as 3 Contact Graph (CG) nodes: the ball, the hands, and the rest of body parts. For all sequences, the rest body parts do not come into contact with the ball and the hands, so we only need to manually label the CG edge between the hands and the ball, which is easy to obtain through observation. 

### **B.2. Refine The HOI Data Using PhysHOI** 

Though some HOI data in BallPlay may be biased, we may resort to PhysHOI to eliminate errors and yield physically plausible HOI data. As shown in Fig. 10, we can see that the reference HOI data suffer inaccuracies, while the results 



Figure 10. **PhysHOI can rectify the error of reference HOI data** . We can see that the reference HOI data suffers inaccuracies more or less, while the result generated by PhysHOI can be much better than the reference. 

generated by PhysHOI are much better than the reference, in terms of physical plausibility and smoothness. Specifically, we first train PhysHOI to imitate an HOI sequence. After convergence, we do the inference under physics simulation and record the HOI data as well as the CG through the API of the environment. Physically rectified HOI data is also provided in the BallPlay dataset. 

## **C. Additional Experiments** 

### **C.1. Varying Ball Sizes** 

During the inference time, we change the radius of the ball to different values and surprisingly find that the humanoids can still perform plausible interaction, even if they are not trained on these ball sizes. Fig. 13 shows the result in three cases. Interestingly, we still get reasonable results without additional training for different ball sizes, which shows the robustness of PhysHOI. Note that the humanoid may fail if the ball size changes too drastically. 

### **C.2. Ablation on Contact Graph Reward** 

In addition to the ablation in the main paper, we provide more visual comparisons in Fig. 12 for an intuitive understanding. In the _cross leg_ case, the humanoid trained w/o CGR tends to hold the ball between its left hand and leg (we provide another view in red boxes for better observation), which causes unnatural interaction. In the _pass_ case, the ball drops without the CGR. In the _fingertip spin_ case, the humanoid trained w/o CGR tends to hold the ball with its hands and head. In comparison, applying CGR addresses these problems well. In Fig. 11 we visualize multiple environments to intuitively demonstrate the success rate w/ or w/o CGR. Each environment applies different random 

seeds. We can see that the ball falling w/o CGR is not accidental, but common. Instead, our method applies CGR and achieves steady success in ball holding. 

## **D. Related Work on Kinematic-Based Methods** 

### **D.1. Human Motion Generation** 

Kinematic motion generation methods are usually learned from motion capture datasets [28, 52, 61, 76]. Early attempts generate motions from the prefix [19, 63] and keyframes [29]. [36] generate motions using an autoencoder, and further apply motion phases to generate consistent motions [37, 89–91]. Beyond action-conditioned motion generation [27, 53, 74], recent advances make it possible to control motions with text description [9, 28, 43, 56, 96, 118, 120], music [14, 49, 99], and speech [50, 113, 125], based on recent progress in autoregressive models [7, 77] and diffusion models [34, 45, 82–85, 101]. 

### **D.2. Human-Object Interaction Generation** 

There are many research topics surrounding HOI, especially detection [10, 25, 41, 103, 107, 123, 124] and reconstruction [39, 46, 73, 100, 106, 119]. Based on recent development of 3D HOI datasets [4, 18, 30, 40, 42, 87, 92, 117, 121], there emerges a branch of research focuses on generating human motion that interacts with objects [24, 44, 47, 48, 75, 88, 93, 95, 104, 110]. However, all the methods mentioned learn directly from kinematic datasets without strict modeling of dynamics and contacts, causing artifacts that harm the motion quality, _e.g_ ., penetration, shaking, sliding, and floating. Besides, kinematic HOI generation can not be used for robot control yet. 



Figure 11. **Ablation on Contact Graph Reward (CGR)** . We visualize multiple environments to intuitively demonstrate the success rate w/ or w/o CGR. We can see that if w/o CGR, the ball falling is not accidental, but common. Instead, our method applies CGR and achieves steady success in ball holding. 

## **E. Discussions** 

### **E.1. Failure Cases** 

The failure cases of our method are mainly due to inaccurate data or incomplete contact graphs. For example, in the _rebound_ case in Fig. 14, the ball in the reference data is always under the hand, which, combined with the fact that the ball bounces back to the hand very quickly, results in a local optimum: the ball is not firmly grasped during the learning process. This problem can be solved with precise HOI data. 

High CGR weight may lead to unpleasant interactions if the CG node is not detailed enough. As shown in the _fingertip spin_ case in Fig. 14, when we set a high CGR weight on the CG edge between hands and the ball, the trained humanoid tends to use multiple fingers to maintain steady contact. The reasons can be twofold: (1) The CG is not detailed enough, e.g., we simply take two hands as one CG node, but it is necessary to take fingers as separate CG nodes in this case. (2) The frame rate of simulation and reference data is low, which yields frequent bouncing, i.e., less contact. While reducing the corresponding CG edge weights can improve this problem, as shown in the _fingertip spin_ case in Fig. 13 and Fig. 12, a more general solution requires richer CGs and higher frame rates, which is also the solution we expect. 

### **E.2. Limitations** 

Though our method is able to mimic diverse dynamic HOI skills, it still faces several limitations, which we list here: 

- Our method may fail when the reference HOI data suffers severe biases, _e.g_ ., the false reference data can result in a ball drop, as shown in the _rebound_ case in Fig. 14. 

- When CG nodes are not detailed enough, some subtle operations can still easily fall into local optimality. For example, fingers should be independent CG nodes when 

learning complex in-hand manipulations. 

- Due to the low frame rate of HOI data and simulation frequency, some minor penetrations may appear. 

- Informing the policy with a single reference object state may not be sufficient for long-term hands-off object control. For example, when learning diverse jump shot sequences, it is difficult for the policy to determine how to control the ball through a single frame of HOI reference state because the ball is out of control after being shot out. One potential solution is to provide the policy with multi-frame reference states of the ball. 

- Our method can not generalize to HOIs that are not trained on, _e.g_ ., the policy trained on _back dribble_ can not handle _fingertip spin_ . 

### **E.3. Future Work** 

We believe this work opens up many exciting directions for future exploration, which we list here: 

- Our work demonstrates the potential to learn generic human skills from diverse HOI data. The way of acquiring HOI data accurately and conveniently is worth studying. 

- When large HOI data is available, studying generalization and generation based on HOI imitation will be an attractive direction toward future humanoid autonomy, considering no need for designing task-specific rewards. For example, train an MVAE [53] using HOI imitation based on a large HOI dataset. 

- Although building a real humanoid with 153 DOF seems far away, it is promising to explore retargeting-based HOI Imitation, _e.g_ ., teaching a robot arm with a dextrous hand to play basketball via HOI Imitation. 

- Multi-human dynamic interactions are also worth studying, such as multi-player basketball games. 



<!-- Start of picture text -->
Cross leg<br>Pass<br>Fingertip spin<br>Ref<br>w/o CGR<br>Ours<br>Ref<br>w/o CGR<br>Ours<br>Ref<br>w/o CGR<br>Ours<br><!-- End of picture text -->

Figure 12. **Ablation on Contact Graph Reward (CGR)** . The humanoid trained w/o CGR tends to fall into the local optimal of kinematic rewards, e.g., using its left leg and left hand to hold the ball. We provide the _cross leg_ case another view in boxes for better observation. 



<!-- Start of picture text -->
Fingertip spin<br>Jump shoot<br>Crossover dribble<br>R = 12 +4  cm<br>R = 12 -2  cm<br>R = 12 +1  cm<br>R = 12 -2  cm<br>R = 12 +8  cm<br>R = 12 -6  cm<br><!-- End of picture text -->

Figure 13. **Varying Ball Sizes** . During inference, we change the ball radius to different values. Interestingly, we still get reasonable results, which show the robustness of PhysHOI. The default ball radius is 12cm. R denotes the changed ball radius. 



<!-- Start of picture text -->
Rebound<br>Fingertip spin<br>Ref<br>Ours<br>Ref<br>Ours<br><!-- End of picture text -->

Figure 14. **Failure cases** . The failure cases of our method are mainly due to inaccurate data or incomplete contact graphs. In the _rebound_ case, the biased ball position results in a local optimum: the ball not being firmly grasped during the learning process. High CGR weight may lead to unpleasant interactions if the CG node is not detailed enough. In the _fingertip spin_ case, when we set a high CGR weight on the CG edge between hands and the ball, the trained humanoid tends to use multiple fingers to maintain steady contact. The reasons can be twofold: (1) The CG is not detailed enough, e.g., we simply take two hands as one CG node, but it is necessary to take fingers as separate CG nodes in this case. (2) The frame rate of simulation and reference data is low, which yields frequent bouncing, i.e., less contact. While reducing the corresponding CG edge weights can improve this problem, as shown in the _fingertip spin_ case in Fig. 13 and Fig. 12, a more general solution requires richer CGs and higher frame rates, which is also the solution we expect. 

