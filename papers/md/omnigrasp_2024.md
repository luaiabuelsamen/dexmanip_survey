# **Omnigrasp: Grasping Diverse Objects with Simulated Humanoids** 

Zhengyi Luo<sup>1</sup><sup>_,_2</sup><sup>_∗_</sup> Jinkun Cao<sup>1</sup><sup>_∗_</sup> Sammy Christen<sup>2</sup><sup>_,_3</sup> Alexander Winkler<sup>2</sup> Kris Kitani<sup>1</sup><sup>_,_2</sup><sup>_†_</sup> Weipeng Xu<sup>2</sup><sup>_†_</sup> 

1Carnegie Mellon University; 2Reality Labs Research, Meta; 3ETH Zurich `https://zhengyiluo.github.io/Omnigrasp` 



Figure 1: We control a simulated humanoid to grasp diverse objects and follow complex trajectories. ( _Top_ ): picking up and holding objects. ( _Bottom_ ): green dots - reference trajectory; pink dots - object trajectory. 

### **Abstract** 

We present a method for controlling a simulated humanoid to grasp an object and move it to follow an object’s trajectory. Due to the challenges in controlling a humanoid with dexterous hands, prior methods often use a disembodied hand and only consider vertical lifts or short trajectories. This limited scope hampers their applicability for object manipulation required for animation and simulation. To close this gap, we learn a controller that can pick up a large number (>1200) of objects and carry them to follow randomly generated trajectories. Our key insight is to leverage a humanoid motion representation that provides human-like motor skills and significantly speeds up training. Using only simplistic reward, state, and object representations, our method shows favorable scalability on diverse objects and trajectories. For training, we do not need a dataset of paired full-body motion and object trajectories. At test time, we only require the object mesh and desired trajectories for grasping and transporting. To demonstrate the capabilities of our method, we show state-of-the-art success rates in following object trajectories and generalizing to unseen objects. Code and models will be released. 

_∗_ Equal Contribution _†_ Equal Advising 

38th Conference on Neural Information Processing Systems (NeurIPS 2024). 

### **1 Introduction** 

Given an object mesh, we aim to control a simulated humanoid equipped with two dexterous hands to pick up the object and follow plausible trajectories, as shown in Fig.1. This capability could be broadly applied to creating human-object interactions for animation and AV/VR, with potential extensions to humanoid robotics [27]. However, controlling a simulated humanoid with dexterous hands for precise object manipulation poses significant challenges. The bipedal humanoid must maintain balance to enable detailed movements of the arms and fingers. Moreover, interacting with objects requires forming stable grasps that accommodate diverse object shapes. Combining these demands with the inherent difficulties of controlling a humanoid with a high degree of freedom ( _e.g_ . 153 DoF) significantly complicates the learning process. 

These challenges have led previous methods of simulated grasping to employ a disembodied hand [16, 17, 60, 84] to grasp and transport. While this approach can generate physically plausible grasps, employing a floating hand compromises physical realism: the hands’ root position and orientation are controlled by invisible forces, allowing it to remain nearly perfectly stable during grasping. Moreover, studying the hand in isolation does not accurately reflect its typical use, which is when it is attached to a mobile and flexible body. A naive approach to supporting hands is to use existing full-body motion imitators [42] to provide body control and train additional hand controllers for grasping. However, the presence of a body introduces instability, limits hand movement, and requires synchronizing the entire body to facilitate finger motion. State-of-the-art (SOTA) full-body imitators also have an average 30mm tracking error for the hands, which can cause the humanoid to miss objects. Due to the above challenges, previous work that studies full-body object manipulations often limits its scope to only one sequence of object interaction [77] and encounters difficulties in trajectory following [6], even when trained with highly specialized motion priors. 

Another challenge of grasping is the diversity of the object shapes and trajectories. Each object may require a unique type of grasping, and scaling to thousands of different objects often requires training procedures such as generalist-specialist training [84] or curriculum [74, 100]. There is also infinite variability in potential object trajectories, and each trajectory may necessitate precise full-body coordination. Thus, prior work typically focuses on simple trajectories, such as vertical lifting [16, 84], or on learning a single, fixed, and pre-recorded trajectory per policy [17]. The flexibility with which humans manipulate objects to follow various trajectories while holding them remains unobtainable for current humanoids, even in simulations. 

In this work, we introduce a full-body and dexterous humanoid controller capable of picking up and following diverse object trajectories using Reinforcement Learning (RL). Our proposed method, Omnigrasp, presents a scalable approach that generalizes to unseen object shapes and trajectories. Here, “Omni” refers to following any trajectory in all directions within a reasonable range and grasping diverse objects. Our key insight lies in using a pretrained universal dexterous motion representation as the action space. Directly training a policy on the joint actuation space using RL results in unnatural motion and leads to a severe exploration problem. Exploration noise in the torso can lead to a large deviation in the location of the arm and wrist as the noise propagates through the kinematic chain. This can lead to the humanoid quickly knocking the object away, which hinders training progress. Prior work has explored using a separate body and hand latent space trained using adversarial learning [6]. However, as the adversarial latent space can only cover small-scale and curated datasets, these methods do not achieve a high grasping success rate. The separation of hands and body motion prior also adds complexity to the system. We propose using a unified _universal and dexterous_ humanoid motion latent space [41]. Learned from a large-scale human motion database [44], our motion representation provides a compact and efficient action space for RL exploration. We enhance the dexterity of this latent space by incorporating articulated hand motions into the existing body-only human motion dataset. 

Equipped with a universal motion representation, our humanoid controller does not require any specialized interaction graph [77, 101] to learn human-object interactions. Our input to the policy consists only of object and trajectory-following information and is devoid of any grasp or reference body motion. For training, we use randomly generated trajectories and do not require paired full-body human-object motion data. We also identify the importance of pre-grasps [17] (the hand pose right before grasping) and utilize it in our reward design. The resulting policy can be directly applied to transport new objects without additional processing and achieve a SOTA success rate on following object trajectories captured by Motion Capture (MoCap). 

2 

To summarize, our contributions are: (1) we design a dexterous and universal humanoid motion representation that significantly increases sample efficiency and enables learning to grasp with simple yet effective state and reward designs; (2) we show that leveraging this motion representation, one can learn grasping policies with synthetic grasp poses and trajectories, without using any paired full-body and object motion data. (3) we demonstrate the feasibility of training a humanoid controller that can achieve a high success rate in grasping objects, following complex trajectories, scaling up to diverse training objects, and generalizing to unseen objects. 

### **2 Related Works** 

**Simulated Humanoid Control** . Simulated humanoids can be used to create animations [26, 36, 53, 54, 55, 56, 79, 93, 101], estimate full-body pose from sensors [23, 30, 33, 40, 43, 78, 91, 92, 94], and transfer to real humanoid robots [20, 27, 28, 58, 59]. Since there are no ground truth data for joint actuation and physics simulators are often non-differentiable, model-based control [29], trajectory optimization [36, 82], and deep RL [13, 53] are used instead of supervised learning. Due to its flexibility and scalability, deep RL has been popular among efforts in simulated humanoids, where a policy/controller is trained via trial and error. Most of the previous work on humanoids does not consider articulated fingers, except for a few [3, 6, 36, 48]. A dexterous humanoid controller is essential for humanoids to perform meaningful tasks in simulation and in the real world. 

**Dexterous Manipulation** . Dexterous manipulation is an essential topic in robotics [7, 8, 11, 12, 15, 16, 19, 37, 61, 74, 84, 95, 96, 97] and animation [2, 6, 34, 100]. This task usually involves pick-andplace [7, 8], lifting [74, 84, 96], articulating objects [97], and following predefined object trajectories [6, 9, 17]. Most of these efforts use a disembodied hand for grasping and employ non-physical virtual forces to control the hand. Among them, D-Grasp [16] leverages the MANO [65] hand model for physically plausible grasp synthesis and 6DoF target reaching. UniDexGrasp [84] and its followup [74] use the Shadow Hand [1]. PGDM [17] trains a grasping policy for individual object trajectories and identifies pre-grasp initialization (initializing the hand in a pose right before grasping) as a crucial factor for successful grasping. For the works that consider both hands and body, PMP [3] and PhysHOI [77] train one policy for each task or object. Braun _et al_ . [6] studies a similar setting to ours but relies on MoCap human-object interaction data and only uses one hand. Compared to prior work, Omnigrasp trains one policy to transport diverse objects, supports bimanual motion, and achieves a high success rate in lifting and object trajectory following. 

**Kinematic Grasp Synthesis** . Synthesizing hand grasp can be widely applied in robotics and animation. A line of work [5, 10, 10, 18, 21, 38, 46, 50, 83, 88] focuses on reconstructing and predicting grasp from images or videos, while others [51, 89] study hand grasp generation to help image generation. Among them, Manipnet and CAMS [98] predict finger poses given a hand object trajectory. TOCH [102] and GeneOH [39] denoise dynamic hand pose predictions for object interactions. More research in this area focuses on generating static or sequential hand poses with a given object as the condition [31, 69, 87]. For synthesizing body and hand poses jointly, there are limited MoCap data available [70] due to difficulties in capturing synchronized full-body and object trajectories. Some generative methods [22, 35, 68, 71, 72, 81, 90] can create paired human-object interactions, but they require initialization from the ground truth [22, 68, 81], or only predict static full-body grasps [72]. In this work, we use GrabNet [69] trained on object shapes from OakInk [85] to generate hand poses as reward guidance for our policy training. 

**Humanoid Motion Representation** . Due to the high DoF of a humanoid and the sample inefficiency of RL training, the search space within which the policy operates during trial and error is crucial. A more structured action space such as motion primitives [24, 25, 47, 62] or motion latent space [55, 73] can significantly increase sample efficiency since the policy can sample coherent motion instead of relying on random “jittering” noise. This is especially important for humanoids with dexterous hands, where the torso motion can drastically affect the hand movement and lead to the humanoid knocking the object away. Thus, prior work in this space utilizes part-based motion priors [3, 6] trained on specialized datasets. While effective in the single task setting where the humanoid only needs to perform actions close to the ones in the specialized datasets, these motion priors can hardly scale to more free-formed motion, such as following randomly generated object trajectories. We extend the recently proposed universal humanoid motion representation, PULSE [41], to the dexterous humanoid setting and demonstrate that a 48-dimensional, full-body-and-hand motion latent space can be used to pick up and follow randomly generated trajectories. 

3 



Figure 2: Omnigrasp is trained in two stages. (a) A universal and dexterous humanoid motion representation is trained via distillation. (b) Pre-grasp guided grasping training using a pretrained motion representation. 

### **3 Preliminaries** 

We define the human pose as **_q_** _t_ ≜ ( **_θ_** _t,_ **_p_** _t_ ), consisting of 3D joint rotation **_θ_** _t ∈_ R<sup>_J×_6</sup> and position **_p_** _t ∈_ R<sup>_J×_3</sup> of all _J_ links on the humanoid (hands and body), using the 6 degree-of-freedom (DOF) rotation representation [103]. To define velocities **_q_ ˙** 1: _T_ , we have **_q_ ˙** _t_ ≜ ( **_ω_** _t,_ **_v_** _t_ ) as angular **_ω_** _t ∈_ R<sup>_J×_3</sup> and linear velocities **_v_** _t ∈_ R<sup>_J×_3</sup> . For objects, we define their 3D trajectories **_q_**<sup>obj</sup> _t_ using object position **_p_**<sup>obj</sup> _t_<sup>, orientation</sup><sup>**_θ_**obj</sup> _t_<sup>, linear velocity</sup><sup>**_v_**obj</sup> _t_<sup>, and angular velocity</sup><sup>**_ω_**obj</sup> _t_<sup>.As a notation convention, we</sup> use � _·_ to denote the kinematic quantities from Motion Capture (MoCap) or trajectory generator and normal symbols without accents for values from the physics simulation. **_O_**<sup>**ˆ**</sup> refers to a dataset of diverse object meshes. 

**Goal-conditioned Reinforcement Learning for Humanoid Control** . We define the object grasping and transporting task using the general framework of goal-conditioned RL. Namely, a goalconditioned policy _π_ is trained to control a simulated humanoid to grasp an object and follow object trajectories **_q_ ˆ**<sup>obj</sup> 1: _T_<sup>usingdexteroushands.ThelearningtaskisformulatedasaMarkovDecision</sup> Process (MDP) defined by the tuple _M_ = _⟨_ **_S_** _,_ **_A_** _,_ **_T_** _,_ **_R_** _, γ⟩_ of states, actions, transition dynamics, reward function, and discount factor. The simulation determines the state **_s_** _t ∈_ **_S_** and transition dynamics **_T_** , where a policy computes the action **_a_** _t_ . The state **_s_** _t_ contains the proprioception **_s_**<sup>p</sup> _t_<sup>and</sup> the goal state **_s_**<sup>g</sup> _t_<sup>.Proprioception is defined as</sup><sup>**_s_**p</sup> _t_<sup>≜(</sup><sup>**_q_**</sup> _t_<sup>_,_</sup><sup>**_q_˙**</sup> _t_<sup>_,_</sup><sup>**_c_**</sup><sup>_t_), which contains the 3D body pose</sup><sup>**_q_**</sup> _t_<sup>,</sup> velocity **_q_ ˙** _t_ , and contact forces **_c_** _t_ on the hand. The goal state **_s_**<sup>g</sup> _t_<sup>is defined based on the states of the</sup> objects. When computing the states **_s_**<sup>g</sup> _t_<sup>and</sup><sup>**_s_**p</sup> _t_<sup>, all values are normalized with respect to the humanoid</sup> heading (yaw). Based on proprioception **_s_**<sup>p</sup> _t_<sup>and the goal state</sup><sup>**_s_**g</sup> _t_<sup>, we define a reward</sup><sup>_rt_=</sup><sup>**_R_**(</sup><sup>**_s_**p</sup> _t_<sup>_,_</sup><sup>**_s_**g</sup> _t_<sup>)</sup> for training the policy. We use proximal policy optimization (PPO) [67] to maximize discounted reward E _t_ =1<sup>_γt−_1</sup><sup>_rt_</sup> . Our humanoid follows the kinematic structure of SMPL-X [52] using the �� _T_ � mean shape. It has 52 joints, of which 51 are actuated. 21 joints are body joints, and the remaining 30 joints are for two hands. All joints have 3 DoF, resulting in an actuation space of **_a_** _t ∈_ R<sup>51</sup><sup>_×_3</sup> . Each degree of freedom is actuated by a proportional derivative (PD) controller, and the action **_a_** _t_ specifies the PD target. 

### **4 Omnigrasp: Grasping Diverse Objects and Follow Object Trajectories** 

To tackle the challenging problem of picking up objects and following diverse trajectories, we first acquire a universal dexterous humanoid motion representation in Sec.4.1. Using this motion representation, we design a hierarchical RL framework (Sec. 4.2) for grasping objects using simple<sup>‡</sup> state and reward designs guided by pre-grasps. Our architecture is visualized in Figure 2. 

> ‡ Here, the “simple reward” refers to not needing paired full-body-and-hand MoCap data when computing the reward, which increases complexity. 

4 

#### **4.1 PULSE-X: Physics-based Universal Dexterous Humanoid Motion Representation** 

We introduce PULSE-X that extends PULSE [41] to the dexterous humanoid by adding articulated fingers. We first train a humanoid motion imitator [42] that can scale to a large-scale human motion dataset with finger motion. Then, we distill the motion imitator into a motion representation using a variational information bottleneck (similar to a VAE [32]). 

**Data Augmentation** . Since full-body motion datasets that contain finger motion are rare ( _e.g_ ., 91% of the AMASS sequences do not have finger motion), we first augment existing sequences with articulated finger motion and construct a dexterous full-body motion dataset. Similarly to the process in BEDLAM [4], we randomly pair full-body motion from AMASS [44] with hand motion sampled from GRAB [70] and Re:InterHand [49] to create a dexterous AMASS dataset. Intuitively, training on this dataset increases the dexterity of the imitator and the subsequent motion representation. 

**PHC-X: Humanoid Motion Imitation with Articulated Fingers** . Inspired by PHC [42], we design PHC-X _π_ PHC-X for humanoid motion imitation with articulated fingers. For the finger joints, _we treat them similarly as the rest of the body (_ e.g _. toe or wrist)_ and find this formulation sufficient to acquire the dexterity needed for grasping. Formally, the goal state for training _π_ PHC-X with RL is **_s_**<sup>g-mimic</sup> _t_ ≜ ( **_θ_**<sup>**ˆ**</sup> _t_ +1 _⊖_ **_θ_** _t,_ **ˆ** **_p_** _t_ +1 _−_ **_p_** _t,_ **ˆ** **_v_** _t_ +1 _−_ **_v_** _t,_ **ˆ** **_ω_** _t_ +1 _−_ **_ω_** _t,_ **_θ_**<sup>**ˆ**</sup> _t_ +1 _,_ **ˆ** **_p_** _t_ +1), which contains the difference between proprioception and one frame reference pose **_q_ ˆ** _t_ +1. 

**Learning Motion Representation via Online Distillation** . In PULSE [41], an encoder **_E_** PULSE-X, decoder **_D_** PULSE-X, and prior **_P_** PULSE-X are learned to compress motor skills into a latent representation. For downstream tasks, the frozen decoder and prior will translate the latent code to joint actuation. Formally, the encoder **_E_** PULSE-X( **_z_** _t|_ **_s_**<sup>p</sup> _t_<sup>_,_</sup><sup>**_s_**g-mimic</sup> _t_ ) computes the latent code distribution based on current input states. The decoder **_D_** PULSE-X( **_a_** _t|_ **_s_**<sup>p</sup> _t_<sup>_,_</sup><sup>**_z_**</sup><sup>_t_) produces action (joint actuation) based on the latent</sup> code **_z_** _t_ . The prior **_P_** PULSE-X( **_z_** _t|_ **_s_**<sup>p</sup> _t_<sup>) defines a Gaussian distribution based on proprioception and</sup> replaces the unit Gaussian distribution used in VAEs [32]. The prior increases the expressiveness of the latent space and guides downstream task learning by forming a residual action space (see Sec.4.2). We model the encoder and prior distribution as diagonal Gaussian: 



To train the models, we use online distillation similar to DAgger [66] by rolling out the encoderdecoder in simulation and querying _π_ PHC-X for action labels **_a_**<sup>PHC-X</sup> _t_ . For more information and evaluation of PHC-X and PULSE-X, please refer to the Appendix B. 

#### **4.2 Pre-grasp Guided Object Manipulation** 

Using hierarchical RL and PULSE-X’s trained decoder **_D_** PULSE-X and prior **_P_** PULSE-X, the action space for our object manipulation policy becomes the latent motion representation **_z_** _t_ . Since the action space serves as a strong human-like motion prior, we can use simple state and reward design and do not require any paired object and human motion to learn grasping policies. We use only hand pose before grasping (pregraps), either from a generative method or MoCap, to train our policy. 

**State** . To provide the task policy _π_ Omnigrasp with information about the object and the desired object trajectory, we define the goal state as 



which contains the reference object pose and the difference between the reference object trajectory for the next _ϕ_ frames and the current object state. **_σ_**<sup>obj</sup> _∈R_<sup>512</sup> is the object shape latent code computed using the canonical object pose and Basis Point Set (BPS) [57]. **_p_**<sup>obj</sup> _t −_ **_p_**<sup>hand</sup> _t_ is the difference between the current object position and each hand joint position. All values are normalized with respect to the humanoid heading. Notice that the state **_s_**<sup>g</sup> _t_<sup>does not contain body pose, grasp, or phase variables [6],</sup> which makes our method applicable to unseen objects and reference trajectories at test time. 

**Action** . Similar to downstream task policies in PULSE, we form the action space of _π_ Omnigrasp as the residual action with respect to prior’s mean **_µ_**<sup>_p_</sup> _t_<sup>and compute the PD target</sup><sup>**_a_**</sup><sup>_t_:</sup> 



5 

**Algo 1:** Learn Omnigrasp 



<!-- Start of picture text -->
1 Function  TrainOmnigrasp( D PULSE-X,  P PULSE-X, πOmnigrasp, O ˆ , T 3D ) :<br>2 Input: Pretrained PULSE-X’s decoder  D PULSE-X and prior  P PULSE-X, Object mesh dataset O ˆ , 3D trajectory Generator  T 3D ;<br>3 while  not converged  do<br>4 M ←∅ initialize sampling memory ;<br>5 while  M not full  do<br>6 q obj 0 , p ˆ pre-grasp ,  s t p ∼ randomly sample initial object state, pre-grasp, and humanoid state ;<br>7 q ˆ obj 1: T ∼ sample reference object trajectory using  T 3D ;<br>8 for  t ← 1 ...T do<br>9 z omnigrasp t ∼ π Omnigrasp( z t omnigrasp | s p t ,  s g t ) // use pretrained latent space as action space  ;<br>10 µ p t ,  σ p t ← P PULSE-X( z t| s t p ) // compute prior latent code  ;<br>11 a t ← D PULSE-X( a t| s p t ,  z omnigrasp t +  µ p t ) // decode action using pretrained decoder  ;<br>12 s t +1 ←T  ( s t +1 | s t,  a t ) // simulation  ;<br>13 r t ← R ( s p t ,  s t g ) // compute reward  ;<br>14 store ( s t,  z omnigrasp t ,  r t,  s t +1) into memory  M ;<br>1615 O π ˆ Omnigrasphard ← Eval and pick hard object subset to train on. ← PPO update using experiences collected in  M ;<br>17 return  π Omnigrasp ;<br><!-- End of picture text -->

where **_µ_**<sup>_p_</sup> _t_<sup>is computed by the prior</sup><sup>**_P_**PULSE-X(</sup><sup>**_z_**</sup><sup>_t|_</sup><sup>**_s_**p</sup> _t_<sup>).The policy</sup><sup>_π_Omnigraspcomputes</sup><sup>**_z_**</sup> _t_<sup>omnigrasp</sup> _∈R_<sup>48</sup> instead of the target **_a_** _t ∈R_<sup>51</sup><sup>_×_3</sup> directly, and leverages the latent motion representation of PULSE-X to produce human-like motion. **Reward** . While our policy does not take any grasp guidance or reference body trajectory _as input_ , we utilize pre-grasp guidance in the _reward_ . We refer to pre-grasp **_q_ ˆ**<sup>pre-grasp</sup> ≜ ( **_p_ ˆ**<sup>pre-grasp</sup> _,_ **_θ_**<sup>**ˆ**</sup> pre-grasp) as a single frame of hand pose consisting of hand translation **_p_ ˆ**<sup>pre-grasp</sup> and rotation **_θ_**<sup>**ˆ**</sup> pre-grasp. PGDM [17] shows that initializing a floating hand to pre-grasps can help the policy better reach objects and initiate manipulation. As we do not initialize the humanoid with the pre-grasp pose as in PGDM, we design a stepwise pre-grasp reward: 



based on time and the distance between the object and hands. Here, _λ_ = 1 _._ 5 _s_ indicates the frame in which grasping should occur, and **_p_**<sup>hand</sup> _t_ indicates the hand position. When the object is far away from the hands ( _∥_ **_p_ ˆ**<sup>pre-grasp</sup> _−_ **_p_**<sup>hand</sup> _t ∥_ 2 _>_ 0 _._ 2), we use an approach reward _rt_<sup>approach</sup> similar to a point-goal [42, 80] reward _rt_<sup>approach</sup> = _∥_ **_p_ ˆ**<sup>pre-grasp</sup> _−_ **_p_**<sup>hand</sup> _t ∥_ 2 _−∥_ **_p_ ˆ**<sup>pre-grasp</sup> _−_ **_p_**<sup>hand</sup> _t−_ 1<sup>_∥_2</sup><sup>_,_,wherethepolicyisencouragedtogetclosetothe</sup> = pre-grasp. After the hands are close enough ( _≤_ 0.2m), we use a more precise hand imitation reward: _rt_<sup>pre-grasp</sup> _w_ hp _e_<sup>_−_100</sup><sup>_∥_</sup> **_p_**<sup>**ˆ**pre-grasp</sup> _−_ **_p_**<sup>hand</sup> _t ∥_ 2 _×_ 1 _{∥_ **_p_ ˆ**<sup>pre-grasp</sup> _−_ **_p_ ˆ**<sup>obj</sup> _t_<sup>_∥_2</sup><sup>_≤_0</sup><sup>_._2</sup><sup>_}_</sup> + _w_ hr _e_<sup>_−_100</sup><sup>_∥_</sup> **_θ_**<sup>**ˆ**pre-grasp</sup> _−_ **_θ_**<sup>hand</sup> _t ∥_ 2 _,_ to encourage the hands to be close to pre-grasps. For grasps that involve only one hand, we use an indicator variable 1 _{∥_ **_p_ ˆ**<sup>pre-grasp</sup> _−_ **_p_ ˆ**<sup>obj</sup> _t_<sup>_∥_2</sup><sup>_≤_0</sup><sup>_._2</sup><sup>_}_</sup> to filter out hands that are too far away from the object. After timestep _λ_ , we use only the object trajectory following reward: 



_rt_<sup>obj</sup> computes the difference between the current and reference object pose, which is filtered by an indicator variable 1 _{_ C _}_ that is set to true if the object is in contact with the humanoid hands. The reward 1 _{_ C _} · w_ c encourages the humanoid’s hand to have contact with the object. Hyperparameters can be found in Appendix C. 

**Object 3D Trajectory Generator** . As there is a limited number of ground-truth object trajectories [17], either collected from MoCap or animators, we design a 3D object trajectory generator that can create trajectories with varying speed and direction. Using the trajectory generator, our policy can be trained without any ground-truth object trajectories. This strategy provides better coverage of potential object trajectories, and the resulting policy achieves higher success in following unseen trajectories (see Table 1). Specifically, we extend the 2D trajectory generator used in PACER [64, 75] to 3D, and create our trajectory generator _T_<sup>3D</sup> ( **_q_**<sup>obj</sup> 0<sup>) =</sup><sup>**_q_ˆ**obj</sup> 1: _T_<sup>.Given initial</sup> object pose **_q_**<sup>obj</sup> 0<sup>,</sup><sup>_T_3D can generate a sequence of plausible reference object motion</sup><sup>**_q_ˆ**obj</sup> 1: _T_<sup>.We limit the z-direction</sup> trajectory to between 0.03m and 1.8m and leave the xy direction unbounded. For more information and sampled trajectories, please refer to Appendix C. 

6 

Table 1: Quantitative results on object grasp and trajectory following on the GRAB dataset. 

|||GRAB-Go|al-Test (Cro|ss-Object,|140 seque|nces, 5|unseen ob|jects)|GRAB-|IMoS-Test (|Cross-Sub|ject, 92 s|equences|, 44 obje|cts)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|Traj|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|PPO-10B|Gen|98.4%|55.9%|97.5%|36.4|**0.4**|21.0|14.5|96.8%|53.2%|97.9%|35.6|**0.5**|19.6|13.9|
|PHC [42]|MoCap|3.6%|11.4%|81.1%|66.3|0.8|1.5|3.8|0%|3.3%|97.4%|56.5|0.3|1.4|2.9|
|AMP [56]|Gen|90.4%|46.6%|94.0 %|40.7|0.6|5.3|5.3|95.8 %|49.2%|96.5%|34.9|0.5|6.2|6.0|
|Braun_et al_. [6]|MoCap|79%|-|85%|-|-|-|-|64%|-|65%|-|-|-|-|
|Omnigrasp|MoCap|94.6%|84.8%|98.7%|**28.0**|**0.5**|**4.2**|**4.3**|95.8%|85.4%|99.8%|**27.5**|**0.6**|**5.0**|**5.0**|
|Omnigrasp|Gen|**100**%|**94.1%**|**99.6%**|30.2|0.93|5.4|4.7|**98.9%**|**90.5%**|**99.8%**|27.9|0.97|6.3|5.4|



**Training** . Our training process is depicted in Algo 1. One of the main sources of performance improvement for motion imitation is hard-negative mining [42, 43], where the policy is evaluated regularly to find the failure sequences to train on. Thus, instead of using object curriculum [74, 84, 100], we use a simple hard-negative mining process to pick hard objects **_O_**<sup>**ˆ**</sup> hard to train on. Specifically, let _sj_ be the number of failed lifts for object _j_ over all previous runs. The probability of choosing object _j_ among all objects is _P_ ( _j_ ) = _sj_ <u>�</u> _Ji_<sup>_si_.</sup> 

**Object and Humanoid Initial State Randomization** . Since objects can have diverse initial positions and orientations with respect to the humanoid, it is crucial to have the policy exposed to diverse initial object states. Given the object dataset **_O_**<sup>**ˆ**</sup> and the provided initial states (either from MoCap or by dropping the object in simulation) **_q_**<sup>obj</sup> 0<sup>, we perturb</sup><sup>**_q_**obj</sup> 0<sup>by adding randomly sampled yaw-direction rotation and adjusting the position</sup> component **_q_**<sup>obj</sup> 0<sup>.We do not change the pitch and yaw of the object’s initial pose as some poses are invalid in</sup> simulation. For the humanoid, we use the initial state from the dataset if provided ( _e.g_ . GRAB dataset [70]), and a standing T-pose if there is no paired data. 

**Inference** . During inference, the object latent code **_p_**<sup>obj</sup> _t_<sup>, a random object starting pose</sup><sup>**_q_**obj</sup> 0<sup>, and desired object</sup> trajectory **_q_ ˆ**<sup>obj</sup> 1: _T_<sup>is all that is required, without any dependency on pre-grasps or paired kinematic human pose.</sup> 

### **5 Experiments** 

**Datasets** . We use the GRAB [70], OakInk [85], and OMOMO [34] to study grasping small and large objects. The GRAB dataset contains 1.3k paired full-body motion and object trajectories of 50 objects (we remove the doorknob as it is not movable). Since the GRAB dataset provides reference body and object motion, we use them to extract initial humanoid positions and pre-grasps. We follow prior art [6] in constructing cross-object (45 for training and 5 for testing) and cross-subject (9 subjects for training and 1 for testing) train-test sets. On GRAB, we evaluate on following MoCap object trajectories using the mean body shape humanoid. The OakInk dataset contains 1700 diverse objects of 32 categories with real-world scanned and generated object meshes. We split them into 1330 objects for training, 185 for validation, and 185 for testing. Train-test splits are conducted within categories, with train and test splits containing objects from all categories. Since no paired MoCap human motion or grasps exists for the OakInk dataset, we use an off-the-shelf grasp generator [85] to create pre-grasps. The OMOMO dataset contains 15 large objects (table lamps, monitors, _etc_ .) with reconstructed mesh, and we pick 7 of them that have cleaner meshes. Due to the limited number of objects from OMOMO, we only test lifting on the objects used for training to verify that our pipeline can learn to move larger objects. On OMOMO and OakInk, we study vertical lifting (30cm) and holding (3s) as the trajectory for quantitative results. 

**Implementation Details** . Simulation is conducted in Isaac Gym [45], where the policy is run at 30 Hz and the simulation at 60 Hz. For PULSE-X and PHC-X, each policy is a 6-layer MLP. For the grasping task, we employ a GRU [14] based recurrent policy and use a GRU with a latent dimension of 512, followed by a 3-layer MLP. We train Omnigrasp for three days collecting around 10<sup>9</sup> samples on a Nvidia A100 GPU. PHC-X and PULSE-X are trained once and frozen, which takes around 1.5 weeks and 3 days. Object density is 1000 kg/m<sup>3</sup> . The static and dynamic friction coefficients of the object and humanoid fingers are set to 1. For reference object trajectory, we use _ϕ_ = 20 future frames sampled at 15Hz. For more details, please refer to Appendix C. 

**Metrics** . For the object trajectory following, we report the position error _E_ pos (mm), rotation error _E_ rot (radian), and physics-based metrics such as acceleration error _E_ acc (mm/frame<sup>2</sup> ) and velocity error _E_ vel (mm/frame). Following prior art in full-body simulated humanoid grasping [6], we report the grasp success rate Succgrasp and Trajectory Targets Reached (TTR). The grasp success rate Succgrasp deems a grasp successful when the object is held for at least 0.5s in the physics simulation without dropping. TTR measures the ratio of the target position (< 12cm away from the target position) reached over all the time steps in the trajectory and is only measured on successful trajectories. To measure the complete trajectory success rate, we also report Succtraj, where a trajectory following is unsuccessful if, at any point in time, the object is > 25cm away from the reference. 

7 



Figure 3: Qualitative results. Unseen objects are tested for GRAB and OakInk. Green dots: reference trajectories. Best seen in videos on our `supplement site` . 

#### **5.1 Grasping and Trajectory Following** 

As motion is best seen in videos, please refer to `supplement site` for extended evaluation on trajectory following, unseen objects, and robustness. Unless otherwise specified, all policies are trained on their respective dataset training split, and we conduct cross-dataset experiments on GRAB and OakInk. All experiments are run 10 times and averaged as the simulator yields slightly different results for each run due to _e.g_ . floating-point error. As full-body simulated humanoid grasping is a relatively new task with a limited number of baselines, we use Braun et [6] as our main comparison. We also implement AMP [56] and PHC [42] as baselines. We train AMP with a similar state and reward design (without using PULSE-X’s latent space) and a task and discriminator reward weighting of 0.5 and 0.5. PHC refers to using an imitator for grasping, where we directly feed ground-truth kinematic body and finger motion to a pretrained imitator to grasp objects. Since PHC and PULSE-X require pre-training, we also include PPO-10B, which is trained using RL without PULSE-X for a month ( _∼_ 10 billion samples). 

**GRAB Dataset (50 objects)** . Since Braun _et al_ . do not use randomly generated trajectories, we train Omnigrasp using two different settings for a fair comparison: one trained with MoCap object trajectories only, and one trained using synthetic trajectories only. From Table 1, we can see that our method outperforms prior SOTA and baselines on all metrics, especially on success rate and trajectory following. Since all methods are simulationbased, we omit penetration/foot sliding metrics and report the precise trajectory tracking errors instead. Training directly using PPO without PULSE-X leads to a performance that significantly lags behind Omnigrasp, even though it has used similar aggregate samples (counting PHC-X and PULSE-X training). Compared to Braun _et al_ ., Omnigrasp achieves a high success rate on both object lifting and trajectory following. Directly using the motion imitator, PHC, yields a low success rate even when the ground-truth kinematic pose is provided, showing that the imitator’s error (on average 30mm) is too large to overcome for precise object grasping. The body shape mismatch between MoCap and our simulated humanoid also contributes to this error. AMP leads to a low trajectory success rate, showing the importance of using a motion prior in the _actions space_ . Omnigrasp can track the MoCap trajectory precisely with an average error of 28mm. Comparing training on MoCap trajectories and randomly generated ones, we can see that training on generated trajectories achieves better performance on success rate and position error, though worse on rotation error. This is due to our 3D trajectory generator offering good coverage on physically plausible 3D trajectories, but there is a gap between the randomly generated rotations and MoCap object rotation. This can be improved by introducing more rotation variation on the trajectory generator. The gap between trajectory Succtraj and grasp success Succgrasp shows that following the full trajectory is a much harder task than just grasping, and the object can be dropped during trajectory following. Qualitative results can be found in Fig. 3. 

**OakInk Dataset (1700 objects)** . On the OakInk dataset, we scale our grasping policy to >1000 objects and test our generalization to unseen objects. We also conduct cross-dataset experiments, where we train on the GRAB dataset and test on the OakInk dataset. Results are shown in Table 3. We can see that 1272 out of the 1330 objects are trained to be picked up, and the whole lifting process also has a high success rate. We observe similar results on the test split. Upon inspection, the failed objects are usually either too large or too small for the humanoid to establish a grasp. The large number of objects also places a strain on the hard-negative mining process. The policy trained on both GRAB and OakInk shows the highest success rate, as on GRAB, there are bi-manual pre-grasps, and the policy learned to use both hands. 

8 

Table 3: Quantitative results on OakInk with our method. We also test Omnigrasp cross-dataset, where a policy trained on GRAB is tested on the OakInk dataset. 

|||OakInk-|Train (133|0 objects)||||OakI|nk-Test (18|5 objects)|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Training Data|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|OakInk|93.7%|86.2%|**100%**|21.3|**0.4**|7.7|6.0|**94.3%**|87.5%|**100%**|**21.2**|**0.4**|7.6|5.9|
|GRAB|84.5%|75.2%|99.9%|22.4|**0.4**|6.8|5.7|81.9%|72.1%|99.9%|22.7|**0.4**|7.1|5.8|
|GRAB + OakInk|**95.6%**|**92.0%**|**100%**|**21.0**|0.6|**5.4**|**4.8**|93.5%|**89.0%**|**100%**|21.3|0.6|**5.4**|**4.8**|



Table 4: Ablation on various strategies of training Omnigrasp. PULSE-X: whether to use the latent motion representation. pre-grasp: pre-grasp guidance reward. Dex-AMASS: whether to train PULSE-X on the dexterous AMASS dataset. Rand-pose: randomizing the object initial pose. Hard-neg: hard-negative mining. 

|||GRAB-G|oal-Test (Cros|s-Object, 140|sequences, 5 u|nseen objects)||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|idx<br>PULSE-X|pre-grasp|Dex-AMASS|Rand-pose|Hard-neg|Succgrasp _↑_|Succtraj _↑_|TTR _↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|1<br>✗|✓|✓|✓|✓|97.0%|33.6%|92.8%|43.5|**0.5**|10.6|8.3|
|2<br>✓|✗|✓|✓|✓|77.1%|57.9%|97.4%|54.9|1.0|5.5|5.2|
|3<br>✓|✓|✗|✓|✓|94.4%|77.3%|99.3%|30.5|0.9|4.8|**4.4**|
|4<br>✓|✓|✓|✗|✓|92.9%|79.9%|99.2%|31.4|1.1|**4.5**|**4.4**|
|5<br>✓|✓|✓|✓|✗|94.0%|71.6%|98.4%|32.3|1.3|6.2|5.7|
|6<br>✓|✓|✓|✓|✓|**100**%|**94.1%**|**99.6%**|**30.2**|0.9|5.4|4.7|



Using both hands significantly improves the success rate on some larger objects, where the humanoid can scoop up the object with one hand and carry it with both. As OakInk only has pre-grasps using one hand, it cannot learn such a strategy. Surprisingly, training on only GRAB achieves a high success rate on OakInk, picking up more than 1000 objects without training on the dataset, showcasing the robustness of our grasping policy on unseen objects. 

Table 2: Quantitative results on the OMOMO dataset. 

||OM|OMO (7|objects)||||
|---|---|---|---|---|---|---|
|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|7/7|7/7|100%|22.8|0.2|3.1|3.3|



**OMOMO Dataset (7 objects)** . On the OMOMO dataset, we train a policy to show that our method can learn to pick up large objects. Table 2 shows that our method can successfully learn to pick up all the objects, including chairs and lamps. For larger objects, the pre-grasp guidance is essential for guiding the policy to learn bi-manual manipulation skills (as is shown in Fig 3) 

#### **5.2 Ablation and Analysis** 

**Ablation** . In this section, we study the effects of different components of our framework using the cross-object split of the GRAB dataset. Results are shown in Table 4. First, we compare our method trained with (Row 6) or without (R1) PULSE-X’s action space. Using the same reward and state design, we can see that using the universal motion prior significantly improves success rates. Upon inspection, using PULSE-X also yields human-like motion, while not using it leads to unnatural motion (see in `supplement site` ). R2 vs. R6 shows that the pre-grasp guidance is essential in learning grasps that are stable for grasping objects, but without it, some objects can still be grasped successfully. The difference between R3 and R6 is whether to train using the dexterous AMASS dataset. R3 vs R6 shows that without training on a dataset that has diverse hand motion and full-body motion, the policy can learn to pick up objects (high grasp success rate), but struggles in trajectory following. This is expected as the motion prior probably lacks the motion of “holding the object while moving”. R4 and R5 show that object position randomization and hard-negativing mining are crucial for learning robust and successful policies. Ablations on the object latent code, RNN policy, _etc_ . can be found in the Appendix C. 

**Analysis: Diverse Grasps** . In Fig. 4, we visualize the grasping strategy used by our method. We can see that based on the object shape, our policy uses a diverse set of grasping strategies to hold the object during the trajectory following. Based on the trajectory and object initial pose, Omnigrasp discovers different grasping poses for the _same_ object, showcasing the advantage of using simulation and laws of physics for grasp generation. We also notice that for larger objects, our policy will resort to using two hands and a non-prehensile transport strategy. This behavior is learned from pre-grasps in GRAB, which utilize both hands for object manipulation. 

**Analysis: Robustness and Potential for Sim-to-real Transfer** . In Table 5, we add uniform random noise [-0.01, 0.01] to both task observation (positions, object latent codes, etc.) and proprioception. A similar scale (0.01) of random noise is used in sim-to-real RL to tackle noisy input in real-world humanoids [28]. We see that Omnigrasp is relatively robust to input noise, even though it has not been trained with noisy input. Performance drop is more prominent in the acceleration and velocity metrics. Adding noise during training can further improve robustness. We do not claim that Omnigrasp is currently ready for real-world deployment, but we 

9 



Figure 4: _(Top rows)_ : grasping different objects using both hands. _(Bottom)_ diverse grasps on the same object. 

Table 5: Study on how noise affects pretrained Omnigrasp Policy 

|||GRAB-Go|al-Test (Cro|ss-Object,|140 seque|nces, 5|unseen o|bjects)|GRAB-|IMoS-Test (|Cross-Sub|ject, 92 s|equences,|44 obje|cts)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|Noise Scale|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|Omnigrasp|0|**100**%|**94.1%**|**99.6%**|**30.2**|**0.93**|**5.4**|**4.7**|98.9%|**90.5%**|**99.8%**|**27.9**|**0.97**|**6.3**|**5.4**|
|Omnigrasp|0.01|**100**%|91.4%|99.2%|34.8|1.1|15.6|11.5|**99.5%**|86.2%|99.6%|32.5|1.0|17.9|13.2|



believe that a similar system design plus sim-to-real modifications (e.g. domain randomization, distilling into a vision-based policy) has the potential. We conduct more analysis on the robustness of our method with respect to initial object position, object weight, and object trajectories on our `supplement site` . 

### **6 Limitations, Conclusions, and Future Work** 

**Limitations** . While Omnigrasp demonstrates the feasibility of controlling a simulated humanoid to grasp diverse objects and hold them to follow diverse trajectories, many limitations remain. For example, though the 6DoF input is provided in the input and reward, the rotation error remains to be further improved. Omnigrasp has yet to support precise in-hand manipulations. The success rate on trajectory following can be improved, as objects can be dropped or not picked up. Another area of improvement is to achieve _specific_ types of grasps on the object, which may require additional input such as desired contact points and grasp. Human-level dexterity, even in simulation, remains challenging. For visualization of failure cases, see `supplement site` . 

**Conclusion and Future Work** . In conclusion, we present Omnigrasp, a humanoid controller capable of grasping _>_ 1200 objects and following trajectories while holding the object. It generalizes to unseen objects of similar sizes, utilizes bi-manual skills, and supports picking up larger objects. We demonstrate that by using a pretrained universal humanoid motion representation, grasping can be learned using simplistic reward and state designs. Future work includes improving trajectory following success rate, improving grasping diversity, and supporting more object categories. Also, improving upon the humanoid motion representation is a promising direction. While we utilize a simple yet effective unified motion latent space, separating the motion representation for hands and body [3, 6] could lead to further improvements. Effective object representation is also an important future direction. How to formulate an object representation that does not rely on canonical object pose and generalizes to vision-based systems will be valuable to help the model generalize to more objects. 

**Acknowledgement** . Zhengyi Luo is supported by the Meta AI Mentorship (AIM) program. 

10 

### **References** 

- [1] Dexterous hand series. `https://www.shadowrobot.com/dexterous-hand-series/` , 19 Sept. 2023. Accessed: 2024-5-13. 

- [2] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [3] J. Bae, J. Won, D. Lim, C.-H. Min, and Y. M. Kim. Pmp: Learning to physically interact with environments using part-wise motion priors. In _ACM SIGGRAPH 2023 Conference Proceedings_ , pages 1–10, 2023. 

- [4] M. J. Black, P. Patel, J. Tesch, and J. Yang. Bedlam: A synthetic dataset of bodies exhibiting detailed lifelike animated motion. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 8726–8737, 2023. 

- [5] S. Brahmbhatt, C. Ham, C. C. Kemp, and J. Hays. ContactDB: Analyzing and predicting grasp contact via thermal imaging. In _The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2019. 

- [6] J. Braun, S. Christen, M. Kocabas, E. Aksan, and O. Hilliges. Physically plausible full-body hand-object interaction synthesis. _International Conference on 3D Vision (3DV)_ , 2024. 

- [7] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, et al. Rt-2: Vision-language-action models transfer web knowledge to robotic control. _arXiv preprint arXiv:2307.15818_ , 2023. 

- [8] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, et al. Rt-1: Robotics transformer for real-world control at scale. _arXiv preprint arXiv:2212.06817_ , 2022. 

- [9] V. Caggiano, S. Dasari, and V. Kumar. Myodex: Generalizable representations for dexterous physiological manipulation. 2022. 

- [10] Z. Cao, I. Radosavovic, A. Kanazawa, and J. Malik. Reconstructing hand-object interactions in the wild. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 12417–12426, 2021. 

- [11] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal. Visual dexterity: In-hand reorientation of novel and complex object shapes. _Science Robotics_ , 8(84):eadc9244, 2023. 

- [12] T. Chen, J. Xu, and P. Agrawal. A system for general in-hand object re-orientation. _Conference on Robot Learning_ , 2021. 

- [13] N. Chentanez, M. Müller, M. Macklin, V. Makoviychuk, and S. Jeschke. Physics-based motion capture imitation with deep reinforcement learning. In _Proceedings of the 11th ACM SIGGRAPH Conference on Motion, Interaction and Games_ , pages 1–10, 2018. 

- [14] K. Cho, B. van Merrienboer, Çaglar Gülçehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio. Learning phrase representations using rnn encoder–decoder for statistical machine translation. In _Conference on Empirical Methods in Natural Language Processing_ , 2014. 

- [15] S. Christen, L. Feng, W. Yang, Y.-W. Chao, O. Hilliges, and J. Song. Synh2r: Synthesizing hand-object motions for learning human-to-robot handovers. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3168–3175. IEEE, 2024. 

- [16] S. Christen, M. Kocabas, E. Aksan, J. Hwangbo, J. Song, and O. Hilliges. D-grasp: Physically plausible dynamic grasp synthesis for hand-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 20577–20586, 2022. 

- [17] S. Dasari, A. Gupta, and V. Kumar. Learning dexterous manipulation from exemplar object trajectories and pre-grasps. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 3889–3896. IEEE, 2023. 

- [18] Z. Fan, M. Parelli, M. E. Kadoglou, M. Kocabas, X. Chen, M. J. Black, and O. Hilliges. Hold: Categoryagnostic 3d reconstruction of interacting hands and objects from video. _arXiv preprint arXiv:2311.18448_ , 2023. 

- [19] H.-S. Fang, C. Wang, H. Fang, M. Gou, J. Liu, H. Yan, W. Liu, Y. Xie, and C. Lu. Anygrasp: Robust and efficient grasp perception in spatial and temporal domains. _IEEE Transactions on Robotics_ , 2023. 

- [20] Z. Fu, X. Cheng, and D. Pathak. Deep whole-body control: Learning a unified policy for manipulation and locomotion. _arXiv preprint arXiv:2210.10044_ , 2022. 

- [21] G. Garcia-Hernando, S. Yuan, S. Baek, and T.-K. Kim. First-person hand action benchmark with rgb-d videos and 3d hand pose annotations. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 409–419, 2018. 

- [22] A. Ghosh, R. Dabral, V. Golyanik, C. Theobalt, and P. Slusallek. Imos: Intent-driven full-body motion synthesis for human-object interactions. In _Eurographics_ , 2023. 

- [23] K. Gong, B. Li, J. Zhang, T. Wang, J. Huang, M. B. Mi, J. Feng, and X. Wang. Posetriplet: Co-evolving 3d human pose estimation, imitation, and hallucination under self-supervision. _CVPR_ , 2022. 

- [24] T. Haarnoja, K. Hartikainen, P. Abbeel, and S. Levine. Latent space policies for hierarchical reinforcement learning. _arXiv preprint arXiv:1804.02808_ , 2018. 

- [25] L. Hasenclever, F. Pardo, R. Hadsell, N. Heess, and J. Merel. CoMic: Complementary task learning & mimicry for reusable skills. In H. D. Iii and A. Singh, editors, _Proceedings of the 37th International Conference on Machine Learning_ , volume 119 of _Proceedings of Machine Learning Research_ , pages 4105–4115. PMLR, 2020. 

11 

- [26] M. Hassan, Y. Guo, T. Wang, M. Black, S. Fidler, and X. B. Peng. Synthesizing physical character-scene interactions. In _ACM SIGGRAPH 2023 Conference Proceedings_ , pages 1–9, 2023. 

- [27] T. He, Z. Luo, X. He, W. Xiao, C. Zhang, W. Zhang, K. Kitani, C. Liu, and G. Shi. Omnih2o: Universal and dexterous human-to-humanoid whole-body teleoperation and learning. In _arXiv_ , 2024. 

- [28] T. He, Z. Luo, W. Xiao, C. Zhang, K. Kitani, C. Liu, and G. Shi. Learning human-to-humanoid real-time whole-body teleoperation, 2024. 

- [29] T. Howell, N. Gileadi, S. Tunyasuvunakool, K. Zakka, T. Erez, and Y. Tassa. Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo. dec 2022. 

- [30] B. Huang, L. Pan, Y. Yang, J. Ju, and Y. Wang. Neural mocon: Neural motion control for physically plausible human motion capture. _arXiv preprint arXiv:2203.14065_ , 2022. 

- [31] H. Jiang, S. Liu, J. Wang, and X. Wang. Hand-object contact consistency reasoning for human grasps generation. In _ICCV_ , 2021. 

- [32] D. P. Kingma and M. Welling. Auto-encoding variational bayes. _2nd International Conference on Learning Representations, ICLR 2014 - Conference Track Proceedings_ , pages 1–14, 2014. 

- [33] S. Lee, S. Starke, Y. Ye, J. Won, and A. Winkler. Questenvsim: Environment-aware simulated motion tracking from sparse sensors. _arXiv preprint arXiv:2306.05666_ , 2023. 

- [34] J. Li, J. Wu, and C. K. Liu. Object motion guided human motion synthesis. _ACM Transactions on Graphics (TOG)_ , 42(6):1–11, 2023. 

- [35] Q. Li, J. Wang, C. C. Loy, and B. Dai. Task-oriented human-object interactions generation with implicit neural representations. In _Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision_ , pages 3035–3044, 2024. 

- [36] L. Liu and J. Hodgins. Learning basketball dribbling skills using trajectory optimization and deep reinforcement learning. _ACM Transactions on Graphics (TOG)_ , 37(4):1–14, 2018. 

- [37] P. Liu, Y. Orru, C. Paxton, N. M. M. Shafiullah, and L. Pinto. Ok-robot: What really matters in integrating open-knowledge models for robotics. _arXiv preprint arXiv:2401.12202_ , 2024. 

- [38] S. Liu, S. Tripathi, S. Majumdar, and X. Wang. Joint hand motion and interaction hotspots prediction from egocentric videos. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 3282–3292, 2022. 

- [39] X. Liu and L. Yi. Geneoh diffusion: Towards generalizable hand-object interaction denoising via denoising diffusion. In _ICLR_ , 2024. 

- [40] Z. Luo, J. Cao, R. Khirodkar, A. Winkler, K. Kitani, and W. Xu. Real-time simulated avatar from head-mounted sensors. _arXiv preprint arXiv:2403.06862_ , 2024. 

- [41] Z. Luo, J. Cao, J. Merel, A. Winkler, J. Huang, K. Kitani, and W. Xu. Universal humanoid motion representations for physics-based control. _arXiv preprint arXiv:2310.04582_ , 2023. 

- [42] Z. Luo, J. Cao, A. W. Winkler, K. Kitani, and W. Xu. Perpetual humanoid control for real-time simulated avatars. In _International Conference on Computer Vision (ICCV)_ , 2023. 

- [43] Z. Luo, R. Hachiuma, Y. Yuan, and K. Kitani. Dynamics-regulated kinematic policy for egocentric pose estimation. _NeurIPS_ , 34:25019–25032, 2021. 

- [44] N. Mahmood, N. Ghorbani, N. F. Troje, G. Pons-Moll, and M. J. Black. Amass: Archive of motion capture as surface shapes. _Proceedings of the IEEE International Conference on Computer Vision_ , 2019-Octob:5441–5450, 2019. 

- [45] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, and Gavriel State. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- [46] P. Mandikal and K. Grauman. Dexvip: Learning dexterous grasping with human hand pose priors from video. In _Conference on Robot Learning_ , pages 651–661. PMLR, 2022. 

- [47] J. Merel, L. Hasenclever, A. Galashov, A. Ahuja, V. Pham, G. Wayne, Y. W. Teh, and N. Heess. Neural probabilistic motor primitives for humanoid control, 2018. 

- [48] J. Merel, S. Tunyasuvunakool, A. Ahuja, Y. Tassa, L. Hasenclever, V. Pham, T. Erez, G. Wayne, and N. Heess. Catch and carry: Reusable neural controllers for vision-guided whole-body tasks. _ACM Trans. Graph._ , 39, 2020. 

- [49] G. Moon, S. Saito, W. Xu, R. Joshi, J. Buffalini, H. Bellan, N. Rosen, J. Richardson, M. Mallorie, P. Bree, T. Simon, B. Peng, S. Garg, K. McPhail, and T. Shiratori. A dataset of relighted 3D interacting hands. In _NeurIPS Track on Datasets and Benchmarks_ , 2023. 

- [50] T. Nagarajan, C. Feichtenhofer, and K. Grauman. Grounded human-object interaction hotspots from video. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 8688–8697, 2019. 

- [51] S. Narasimhaswamy, U. Bhattacharya, X. Chen, I. Dasgupta, S. Mitra, and M. Hoai. Handiffuser: Text-to-image generation with realistic hand appearances. _arXiv preprint arXiv:2403.01693_ , 2024. 

- [52] G. Pavlakos, V. Choutas, N. Ghorbani, T. Bolkart, A. A. A. Osman, D. Tzionas, and M. J. Black. Expressive body capture: 3d hands, face, and body from a single image. _Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition_ , 2019-June:10967–10977, 2019. 

- [53] X. B. Peng, P. Abbeel, S. Levine, and M. van de Panne. Deepmimic: Example-guided deep reinforcement learning of physics-based character skills. _ACM Trans. Graph._ , 37:143:1–143:14, 2018. 

- [54] X. B. Peng, M. Chang, G. Zhang, P. Abbeel, and S. Levine. Mcp: Learning composable hierarchical control with multiplicative compositional policies. _arXiv preprint arXiv:1905.09808_ , 2019. 

12 

- [55] X. B. Peng, Y. Guo, L. Halper, S. Levine, and S. Fidler. Ase: Large-scale reusable adversarial skill embeddings for physically simulated characters. _arXiv preprint arXiv:2205.01906_ , 2022. 

- [56] X. B. Peng, Z. Ma, P. Abbeel, S. Levine, and A. Kanazawa. Amp: Adversarial motion priors for stylized physics-based character control. _ACM Trans. Graph._ , pages 1–20, 2021. 

- [57] S. Prokudin, C. Lassner, and J. Romero. Efficient learning on point clouds with basis point sets. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pages 4332–4341, 2019. 

- [58] I. Radosavovic, T. Xiao, B. Zhang, T. Darrell, J. Malik, and K. Sreenath. Real-world humanoid locomotion with reinforcement learning. _Science Robotics_ , 9(89):eadi9579, 2024. 

- [59] I. Radosavovic, B. Zhang, B. Shi, J. Rajasegaran, S. Kamat, T. Darrell, K. Sreenath, and J. Malik. Humanoid locomotion as next token prediction. _arXiv preprint arXiv:2402.19469_ , 2024. 

- [60] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- [61] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- [62] D. Rao, F. Sadeghi, L. Hasenclever, M. Wulfmeier, M. Zambelli, G. Vezzani, D. Tirumala, Y. Aytar, J. Merel, N. Heess, and R. Hadsell. Learning transferable motor skills with hierarchical latent mixture policies. _arXiv preprint arXiv:2112.05062_ , 2021. 

- [63] D. Rempe, T. Birdal, A. Hertzmann, J. Yang, S. Sridhar, and L. J. Guibas. Humor: 3d human motion model for robust pose estimation. _arXiv preprint arXiv:2105.04668_ , 2021. 

- [64] D. Rempe, Z. Luo, X. B. Peng, Y. Yuan, K. Kitani, K. Kreis, S. Fidler, and O. Litany. Trace and pace: Controllable pedestrian animation via guided trajectory diffusion. _arXiv preprint arXiv:2304.01893_ , 2023. 

- [65] J. Romero, D. Tzionas, and M. J. Black. Embodied hands: Modeling and capturing hands and bodies together. _arXiv preprint arXiv:2201.02610_ , 2022. 

- [66] S. Ross, G. J. Gordon, and J. A. Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. _arXiv preprint arXiv:1011.0686_ , 2010. 

- [67] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization algorithms, 2017. 

- [68] O. Taheri, V. Choutas, M. J. Black, and D. Tzionas. GOAL: Generating 4D whole-body motion for hand-object grasping. In _CVPR_ , 2022. 

- [69] O. Taheri, N. Ghorbani, M. J. Black, and D. Tzionas. GRAB: A dataset of whole-body human grasping of objects. In _ECCV_ , 2020. 

- [70] O. Taheri, N. Ghorbani, M. J. Black, and D. Tzionas. Grab: A dataset of whole-body human grasping of objects. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IV 16_ , pages 581–600. Springer, 2020. 

- [71] O. Taheri, Y. Zhou, D. Tzionas, Y. Zhou, D. Ceylan, S. Pirk, and M. J. Black. GRIP: Generating interaction poses using latent consistency and spatial cues. In _International Conference on 3D Vision (3DV)_ , 2024. 

- [72] P. Tendulkar, D. Surís, and C. Vondrick. Flex: Full-body grasping without full-body grasps. In _CVPR_ , 2023. 

- [73] C. Tessler, I. Yoni Kasten, I. Y. Guo, and C. Nvidia. Calm: Conditional adversarial latent models for directable virtual characters. 

- [74] W. Wan, H. Geng, Y. Liu, Z. Shan, Y. Yang, L. Yi, and H. Wang. Unidexgrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalist-specialist learning. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 3891–3902, 2023. 

- [75] J. Wang, Z. Luo, Y. Yuan, Y. Li, and B. Dai. Pacer+: On-demand pedestrian animation controller in driving scenarios. _arXiv preprint arXiv:2404.19722_ , 2024. 

- [76] J. Wang, Y. Yuan, Z. Luo, K. Xie, D. Lin, U. Iqbal, S. Fidler, S. Khamis, H. Kong, and Mellon University, Carnegie. Learning human dynamics in autonomous driving scenarios. International Conference on Computer Vision, 2023, 2023. 

- [77] Y. Wang, J. Lin, A. Zeng, Z. Luo, J. Zhang, and L. Zhang. Physhoi: Physics-based imitation of dynamic human-object interaction. _arXiv preprint arXiv:2312.04393_ , 2023. 

- [78] A. Winkler, J. Won, and Y. Ye. Questsim: Human motion tracking from sparse sensors with simulated avatars. _arXiv preprint arXiv:2209.09391_ , 2022. 

- [79] J. Won, D. Gopinath, and J. Hodgins. A scalable approach to control diverse behaviors for physically simulated characters. _ACM Trans. Graph._ , 39, 2020. 

- [80] J. Won, D. Gopinath, and J. Hodgins. Physics-based character controllers using conditional vaes. _ACM Trans. Graph._ , 41:1–12, 2022. 

- [81] Y. Wu, J. Wang, Y. Zhang, S. Zhang, O. Hilliges, F. Yu, and S. Tang. Saga: Stochastic whole-body grasping with contact. In _Proceedings of the European Conference on Computer Vision (ECCV)_ , 2022. 

- [82] K. Xie, T. Wang, U. Iqbal, Y. Guo, S. Fidler, and F. Shkurti. Physics-based human motion estimation and synthesis from videos. _arXiv preprint arXiv:2109.09913_ , 2021. 

- [83] X. Xie, B. L. Bhatnagar, and G. Pons-Moll. Visibility aware human-object interaction tracking from single rgb camera. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4757–4768, 2023. 

13 

- [84] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goalconditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4737–4746, 2023. 

- [85] L. Yang, K. Li, X. Zhan, F. Wu, A. Xu, L. Liu, and C. Lu. OakInk: A large-scale knowledge repository for understanding hand-object interaction. In _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2022. 

- [86] L. Yang, K. Li, X. Zhan, F. Wu, A. Xu, L. Liu, and C. Lu. Oakink: A large-scale knowledge repository for understanding hand-object interaction. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 20953–20962, 2022. 

- [87] Y. Ye, A. Gupta, K. Kitani, and S. Tulsiani. G-hop: Generative hand-object prior for interaction reconstruction and grasp synthesis. In _CVPR_ , 2024. 

- [88] Y. Ye, A. Gupta, and S. Tulsiani. What’s in your hands? 3d reconstruction of generic objects in hands. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 3895–3905, 2022. 

- [89] Y. Ye, X. Li, A. Gupta, S. De Mello, S. Birchfield, J. Song, S. Tulsiani, and S. Liu. Affordance diffusion: Synthesizing hand-object interactions. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 22479–22489, 2023. 

- [90] Y. Ye and C. K. Liu. Synthesis of detailed hand manipulations using contact sampling. _ACM TOG_ , 31(4):1–10, 2012. 

- [91] Y. Yuan and K. Kitani. 3d ego-pose estimation via imitation learning. In _Computer Vision – ECCV 2018_ , volume 11220 LNCS, pages 763–778. Springer International Publishing, 2018. 

- [92] Y. Yuan and K. Kitani. Ego-pose estimation and forecasting as real-time pd control. _Proceedings of the IEEE International Conference on Computer Vision_ , 2019-Octob:10081–10091, 2019. 

- [93] Y. Yuan, J. Song, U. Iqbal, A. Vahdat, and J. Kautz. Physdiff: Physics-guided human motion diffusion model. _arXiv preprint arXiv:2212.02500_ , 2022. 

- [94] Y. Yuan, S.-E. Wei, T. Simon, K. Kitani, and J. Saragih. Simpoe: Simulated character control for 3d human pose estimation. _CVPR_ , 2021. 

- [95] A. Zeng, S. Song, K.-T. Yu, E. Donlon, F. R. Hogan, M. Bauza, D. Ma, O. Taylor, M. Liu, E. Romo, et al. Robotic pick-and-place of novel objects in clutter with multi-affordance grasping and cross-domain image matching. _The International Journal of Robotics Research_ , 41(7):690–705, 2022. 

- [96] H. Zhang, S. Christen, Z. Fan, O. Hilliges, and J. Song. GraspXL: Generating grasping motions for diverse objects at scale. _arXiv preprint arXiv:2403.19649_ , 2024. 

- [97] H. Zhang, S. Christen, Z. Fan, L. Zheng, J. Hwangbo, J. Song, and O. Hilliges. ArtiGrasp: Physically plausible synthesis of bi-manual dexterous grasping and articulation. In _International Conference on 3D Vision (3DV)_ , 2024. 

- [98] H. Zhang, Y. Ye, T. Shiratori, and T. Komura. Manipnet: neural manipulation synthesis with a hand-object spatial representation. _ACM TOG_ , 40(4):1–14, 2021. 

- [99] H. Zhang, Y. Yuan, V. Makoviychuk, Y. Guo, S. Fidler, X. B. Peng, and K. Fatahalian. Learning physically simulated tennis skills from broadcast videos. _ACM Trans. Graph._ , 42:1–14, 2023. 

- [100] Y. Zhang, A. Clegg, S. Ha, G. Turk, and Y. Ye. Learning to transfer in-hand manipulations using a greedy shape curriculum. In _Computer Graphics Forum_ , volume 42, pages 25–36. Wiley Online Library, 2023. 

- [101] Y. Zhang, D. Gopinath, Y. Ye, J. Hodgins, G. Turk, and J. Won. Simulation and retargeting of complex multi-character interactions. In _ACM SIGGRAPH 2023 Conference Proceedings_ , pages 1–11, 2023. 

- [102] K. Zhou, B. L. Bhatnagar, J. E. Lenssen, and G. Pons-Moll. Toch: Spatio-temporal object-to-hand correspondence for motion refinement. In _ECCV_ . Springer, October 2022. 

- [103] Y. Zhou, C. Barnes, J. Lu, J. Yang, and H. Li. On the continuity of rotation representations in neural networks. _Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition_ , 2019-June:5738–5746, 2019. 

14 

## **Appendix** 

|**A **|**Intr**|**oduction**|**15**|
|---|---|---|---|
|**B**|**Deta**|**ils about PHC-X and PULSE-X**|**15**|
||B.1|Training and Architecture . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>15|
||B.2|Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>16|
|**C **|**Deta**|**ils about Omnigrasp**|**16**|
||C.1|Object Processing . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>16|
||C.2|Training Details . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>16|
||C.3|Additional Ablations . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>17|
||C.4|Per-object Successrate breakdown . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>17|
|**D **|**Add**|**itional Discussions**|**17**|
||D.1|Alternatives to PULSE-X . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . .<br>17|
|**E**|**Bro**|**ader social impact.**|**18**|



### **A Introduction** 

In this document, we include additional details about Omnigrasp that are omitted from the main paper due to the page limit. In Sec.B, we include additional information about training and evaluating the performance of our humanoid motion representation, PULSE-X. In Sec. C, we include details about Omnigrasp, such as the trajectory generator and training procedures. 

Extensive qualitative results are provided at the project page as well as the supplementary zip files (which contain lower-resolution videos due to file size limitations). As motion is best seen in videos, we highly encourage our readers to view them to judge the capabilities of our method better. Specifically, we visualize using our controller to trace the characters “Omnigrasp” in the air while holding unseen objects during training. This complex trajectory is never seen during training. We also visualize the policy on GRAB [70], OakInk [86], and OMOMO [34] datasets, both for training and testing objects. On the GRAB dataset, we follow MoCap trajectories, while for the OakInk and OMOMO datasets, we showcase randomly generated trajectories for training. To demonstrate robustness to different object poses, weights, and directions, we also test our method by varying these variables and show that it can still pick up objects. Interestingly, we notice that our method prefers to use both hands to pick and hold the object as the weight of the object increases. We also include motion imitation and random motion sampling for PHC-X and PULSE-X. Further, we visualize our constructed dexterous AMASS dataset and the motion imitation result. Last, we include failure cases for grasping and trajectory following. 

### **B Details about PHC-X and PULSE-X** 

**Data Cleaning** . To train both PHC-X and PULSE-X, we follow PULSE’s [41] procedure in filtering on implausible motion. This process yields 14889 motion sequences from the AMASS dataset for training our humanoid motion representation. Out of all 14889 sequences, only 9% of the sequences contain hand motion, and training on it will bias the motion imitator to have limited dexterity. Thus, we construct the dexterous AMASS dataset by pairing hand-only motion with body-only motion and demonstrate its effectiveness in learning a motion representation that enables object grasping. 

#### **B.1 Training and Architecture** 

The state, action, and rewards for PHC-X and PULSE-X follow the implementation choices of PULSE with the only modifications on the training data (dexterous AMASS) and humanoid (SMPL-X). PHC-X is trained for 1.5 week while PULSE-X takes 3 days. We use the same-sized networks: 6-layer MLP of units [2048, 1536, 1024, 1024, 512, 512] for PHC-X and 3-layer MLP of units [3096, 2048, 1024] for PULSE-X’s encoder and decoders. We notice that due to the increase in DoF from SMPL (69) to SMPL-X (153), simulation is _∼_ 2 times slower. 

15 

Table 7: Hyperparameters for Omnigrasp, PHC-X, and PULSE-X. _σ_ : fixed variance for policy. _γ_ : discount factor. _ϵ_ : clip range for PPO. 

|Method|Batch Size|Learning Rate|_σ_|_γ_|_ϵ_||||||# of samples|
|---|---|---|---|---|---|---|---|---|---|---|---|
|PHC-X|3072|2_×_10<sup>_−_5</sup>|0.05|0.99|0.2||||||_∼_10<sup>10</sup>|
||Batch Size|Learning Rate|Latent size||||||||# of samples|
|PULSE-X|3072|5_×_10<sup>_−_4</sup>|48||||||||_∼_10<sup>9</sup>|
||Batch Size|Learning Rate|_σ_|_γ_|_ϵ_|_w_op|_w_or|_w_ov|_w_oav|_w_c|# of samples|
|Omnigrasp|3072|5_×_10<sup>_−_4</sup>|0.36|0.99|0.2|0.5|0.3|0.05|0.05|0.1|_∼_10<sup>9</sup>|



#### **B.2 Evaluation** 

Table 6: Imitation result on dexterous AMASS (14889 sequences). 

|We evaluate PULSE-X and PHC-X on<br>our constructed dexterous AMASS dataset.|Table 6: Imitat|ion result|on dextero|us AMASS|(14889|seque|
|---|---|---|---|---|---|---|
|The metrics we use are the mean per-|||Dexterou|s AMASS-Tra|in||
|joint position error (mm) for both global<br>_E_and local_E_(root-relative) set-|Method|Succ _↑_|_E_g-mpjpe _↓_|_E_mpjpe _↓_|Eacc _↓_|Evel _↓_|
|g-mhpe  mpjpe <br>tings.<br>We also report acceleration and<br>velocity errors, similar to the object tra-|PHC-X<br>PULSE-X|99.9 %<br>99.5 %|29.4<br>42.9|31.0<br>46.4|4.1<br>4.6|5.1<br>6.7|
|jectory following the setting but averaged|||||||



across all body joints. From Table 6, we can see that PHC-X and PULSE-X achieve a high success rate on training data while maintaining a low per-joint error. Distilling from PHC-X to PULSE-X, we observe similar degradation in imitation performance as in PULSE, akin to the reconstruction error in training VAEs [32]. 

### **C Details about Omnigrasp** 

#### **C.1 Object Processing** 

Since the simulator requires convex objects for simulation, we use the built-in v-hacd function to decompose the meshes into convex geometries. The parameters we use for decomposition can be found in Table 7. To compute object latent code, we use 512-d BPS [57] by randomly sampling 512 points on a unit sphere and calculating their distances to points on the object mesh. As some object meshes have a large number of vertices, we also perform quadratic decimation on the mesh if it contains more than 50000 vertices. 

#### **C.2 Training Details** 

**Early Termination** . During training, we terminate the episode whenever the object is more than 12cm away from its desired reference trajectory at time step t: _∥_ **_p_ ˆ** _t_<sup>obj</sup> _−_ **_p_**<sup>obj</sup> _t_<sup>_∥_2</sup><sup>_>_0</sup><sup>_._12.</sup> 

**Table Removal** . Since the GRAB and OakInk datasets are table-top objects, we use a table at the beginning of the episode to support the object. However, since our randomly generated trajectory can collide with the table and the humanoid has no environmental awareness except for the object, we remove the table after certain timestamps (1.5s) during training. 

**Contact Detection** . As IsaacGym does not provide easy access to contact labels and only provides contact forces, there is no way of differentiating between contact with the table, humanoid body, or objects. Thus, we resort to a heuristic-based way to detect contact. Specifically, if the object is within 0.2m from the hands, has non-zero contact forces, and has a non-zero velocity, we deem it to have contact with the hands. 

**Trajectory Generator** . Randomly generated trajectories can be seen on our `supplement site` on the OakInk and OMOMO dataset, as there is no paired MoCap object motion for these datasets. We sample a random velocity and delta angle at each time step and aggregate the velocities to produce full trajectories. We bound the velocity of our randomly generated trajectories to be between [0, 2] m/s and bound the angles to be between [0, 1] radian. With a probability of 0.2, a sharp turn could happen where the angle is between [0, 2 _π_ ]. As the trajectories can not be too high or low, we bound the z-direction translation to be between [0.1, 2.0]. For orientation, we sample a random ending orientation at the end of the trajectory and interpolate it between the object’s initial trajectory to obtain a sequence of target rotations. 

16 

Table 8: Additional ablations: Object-latent refers to whether to provide the object shape latent code **_σ_**<sup>obj</sup> to the policy. RNN refers to either using an RNN-based policy or an MLP-based policy. Im-obs refers to whether to <u>provide the policy with ground truth full-body pose</u> **_<u>q</u>_ ˆ** _<u>t</u>_ <u>+1</u> as input. 

||||GRAB|-Goal-Test (Cro|ss-Object, 14|0 sequences|, 5 unseen|objects)|||
|---|---|---|---|---|---|---|---|---|---|---|
|idx|Object Latent|RNN|Im-obs|Succgrasp _↑_|Succtraj _↑_|TTR _↑_|_E_pos _↓_|_E_rot _↓_|Eacc _↓_|Evel _↓_|
|1|✗|✓|✗|**100%**|93.2%|**99.8%**|**28.7**|1.3|6.1|5.1|
|2|✓|✗|✗|99.9%|89.6%|99.0%|33.4|1.2|4.5|4.4|
|3|✓|✓|✓|95.2|77.8%|97.9%|32.2|0.9|**3.2**|**3.9**|
|4|✓|✓|✗|**100**%|**94.1%**|99.6%|30.2|**0.9**|5.4|4.7|



#### **C.3 Additional Ablations** 

In Table 8, we provide additional ablations left out due to space limitations. Comparing Row 1 (R1) and R4, we can see that on the GRAB dataset cross-object test set, a policy trained without the object shape latent code **_σ_**<sup>obj</sup> can be on par with a policy with access to it. This is because the humanoid learned a general "grasping" for small objects, and the 5 testing objects do not deviate too much from these strategies. Also, upon inspection, R1 learns to rely on bi-manual manipulation and using two hands when it cannot pick it up with one hand, at which point the object shape no longer affects the grasping pose as much. As a result, R1 suffers a higher rotation error _E_ rot. On the GRAB cross-subject test (44 objects), R1 has a trajectory success rate of Succtraj 84.2%, worse than R4’s 90.5%. R2 vs. R4 shows that the RNN policy is more effective than the MLP-based policy, confirming our intuition that some form of memory is beneficial for a sequential task, such as grasping and omnidirectional trajectory following. R3 studies the scenario where we provide ground truth full-body pose **_q_ ˆ** _t_ to the policy at all times, similar to the setting in PhysHOI [77] (though without the contact graph). Results show that this strategy leads to worse performance, and also prevents us from training on objects that do not have paired MoCap full-body motion. This indicates that the contact graph is needed to imitate human-object interaction precisely. Omnigrasp provides a flexible interface to support learning and testing on novel objects without needing paired ground-truth full-body motion. 

#### **C.4 Per-object Successrate breakdown** 

In Table 9, we break down the per-object success rate on the cross-object split of the GRAB dataset. Of the 5 novel objects, our model finds it hardest to pick up the toothpaste, which has an elongated surface. Upon inspection, we find that Omnigrasp will slip on the round edges of the toothpaste surface and fail to grasp the object. Compared to previous SOTA [6], Omnigrasp outperforms in all metrics and objects. 

Table 9: Per-object breakdown on the GRAB-Goal (cross-object) split. 

|Object|Bra|un_et al_.|[6]||O|mnigrasp||
|---|---|---|---|---|---|---|---|
||Succgrasp _↑_|Succtraj|_↑_|TTR_↑_|Succgrasp _↑_|Succtraj _↑_|TTR_↑_|
|Apple|95%||-|91%|**100%**|99.6%|**99.9%**|
|Binoculars|54%||-|83%|**100%**|90.5%|**99.6%**|
|Camera|95%||-|85%|**100%**|97.7%|**99.7%**|
|Mug|89%||-|74%|**100%**|97.3%|**99.8%**|
|Toothpaste|64%||-|94%|**100%**|80.9%|**99.0%**|



### **D Additional Discussions** 

#### **D.1 Alternatives to PULSE-X** 

One alternative way for reusing the motor skills from a motion imitator like PHC-X is to train a kinematic motion latent space to provide reference motion to drive PHC-X. Such a general-purpose kinematic latent space has been used in physics-based control for pose estimation [76] and animation [99]. However, few have been extended to include dexterous hands. These latent spaces, like HuMoR [63], model motion transition using an encoder **_q_** _ϕ_ ( **_z_** _t|_ **_q_ ˆ** _t,_ **ˆ** **_q_** _t−_ 1) and decoder _pθ_ ( **_q_ ˆ** _t|_ **_z_** _t,_ **ˆ** **_q_** _t−_ 1) where **_q_ ˆ** _t_ is the pose at time step t and **_z_** _t_ is the latent code. **_q_** _ϕ_ and **_p_** _θ_ are trained using supervised learning. The issue with applying such a latent space to simulated humanoid control is twofold: 

> • The output **_q_ ˆ** _t_ of the VAE model, while representing natural human motion, does not model the PD-target (action) space required to maintain balance. This is shown in prior art [76, 99], where an additional motion imitator is still needed to actuate the humanoid by imitating **_q_ ˆ** _t_ instead of using **_q_ ˆ** _t_ as policy output (PD-target). 

- **_q_** _ϕ_ and **_p_** _θ_ are optimized using MoCap data, whose **_q_ ˆ** _t_ values are computed using ground truth motion and finite difference (for velocities). As a result, **_q_** _ϕ_ and **_p_** _θ_ handle noisy humanoid states from simulation poorly. Thus, [76] runs the kinematic latent space in an open-loop auto-regressive fashion without feedback from physics simulation ( _e.g_ . using **_q_ ˆ** _t−_ 1 from the previous time step’s output rather 

17 

than from simulation). The lack of feedback from physics simulation leads to floating and unnatural artifacts [76], and the imitator heavily relies on residual force control to maintain stability. 

### **E Broader social impact.** 

Our method can be used to create a realistic grasping policy for humanoids, generate animation, or synthesize stable grasps. While the state designs have access to privileged information, the overall system design methodology (plus sim-to-real transfer techniques such as domain randomization) has the potential to be transferred to a real humanoid robot. Thus, it has a potential positive social impact, as it can create content or help build the next generation of home robots. 

18 

