# **Towards Human-level Dexterous Teleoperation** 

**Puhao Li**<sup>1</sup><sup>_,_2</sup><sup>_,∗_</sup> **, Zeyuan Chen**<sup>2</sup><sup>_,_3</sup><sup>_,∗_</sup> **, Yingying Wu**<sup>1</sup><sup>_,_2</sup><sup>_,∗_</sup> **, Pengkun Wei**<sup>2</sup> **, Yuyang Li**<sup>2</sup><sup>_,_3</sup> **, Tianyu Wang**<sup>2</sup><sup>_,_3</sup> **, Jiaxiao Shi**<sup>2</sup> **, Mingrui Yu**<sup>1</sup> **, Baoxiong Jia**<sup>2</sup> **, Song-Chun Zhu**<sup>1</sup><sup>_,_2</sup><sup>_,_3</sup> **, Tengyu Liu**<sup>2</sup><sup>_,†_</sup> **, Siyuan Huang**<sup>2</sup><sup>_,†_</sup> 

- 1Tsinghua University 2State Key Lab of General Artificial Intelligence, BIGAI 

   - 3Peking University _∗_ Equal Contribution _†_ Corresponding author `https://bigai-dex.github.io/blog/teledexter` 



<!-- Start of picture text -->
Diverse task configurations<br>Dexterous tele-op interface Hand target<br>Hand-object co-tracking<br>Wrist motion<br>Pick-n-place<br>In-hand re-orientation<br>TeleDexter<br>Finger gaiting<br>More potentials…<br>primitives daily objects<br>Human-level<br>Object target<br>in-hand dexterity<br>tools<br>Tighten a bolt with a screw driver<br>teleoperated<br>Sweep objects with a broom<br>teleoperated<br>Install & uninstall a lightbulb<br>teleoperated<br>Drive & draw nails with a hammer<br>teleoperated<br><!-- End of picture text -->

Fig. 1: **TELEDEXTER** learns diverse dexterous in-hand manipulation skills within a single-stage framework, marking a concrete step towards **human-level dexterous teleoperation** . 

**Abstract:** Humans routinely wield tools, swap grasps, and reposition objects within a single hand—seamlessly orchestrating contact transitions that span translation, re-orientation, and finger gaiting. Endowing robot dexterous hands with this level of in-hand dexterity through teleoperation requires precise control of object motion via dynamic hand–object contact, yet current teleoperation systems remain far from this capability. To bridge this gap, we take a major step towards human-level dexterous teleoperation by introducing **TELEDEXTER** , a hand-object co-tracking controller that maps operator intent into learned, lowlevel contact execution. The controller is trained on consecutive co-tracking subgoals derived from human reference motions, utilizing a hybrid reward that couples sparse subgoal objectives with dense tracking rewards to enable learning across diverse interaction modalities rather than frame-wise trajectory imitation. The entire pipeline requires only single-stage RL and, with random action mask- 

ing and domain randomization, transfers zero-shot to the real robot. We evaluate **TELEDEXTER** on seven challenging dexterous teleoperation tasks spanning object reorientation and long-horizon tool use across two dexterous hands, achieving a 75% average success rate where all baselines consistently fail. Furthermore, the collected demonstrations successfully train autonomous policies via behavioral cloning, marking a concrete step towards human-level dexterous teleoperation. 

**Keywords:** Robot Manipulation, Dexterous Teleoperation, Sim-to-Real Transfer 

## **1 Introduction** 

Everyday manipulation demands human-level dexterity: the ability to dynamically reorient, translate, and regrasp objects within a single hand by continuously coordinating complex finger–object contacts [1, 2]. While such agility is effortless for humans, it remains far beyond the reach of current robots. Teleoperation offers a powerful paradigm for closing this gap by enabling operators to directly teach the robot in the loop [3–5]. _However, achieving human-level in-hand dexterity through dexterous teleoperation remains an open challenge._ 

Despite recent progress, existing dexterous teleoperation systems still fall short of human-level inhand dexterity. One dominant line of work employs kinematic retargeting to map human hand motion directly onto robotic topologies, leveraging vision-based tracking [5–8] or wearable exoskeleton gloves [9–12]. While this paradigm provides an intuitive, low-latency interface that faithfully captures the operator’s kinematic intent, it completely ignores hand-object contact forces and object inertia. Consequently, high-acceleration maneuvers, non-prehensile interactions, and continuous finger-gaiting remain highly unstable, frequently resulting in object slippage or drop failures. An alternative paradigm [13] learns a dexterous action prior in simulation to map coarse teleoperation commands to contact-rich hand actions, improving local contact robustness over pure kinematics. However, these methods typically rely on synthetically generated grasp transitions as training targets, which often lack physical feasibility. Furthermore, encoding the action prior into a generative model introduces cascading trajectory drift and covariate shift during closed-loop execution, severely degrading real-world performance during long-horizon deployment. 

To overcome these limitations, we introduce **TELEDEXTER** , _a hand–object co-tracking controller designed for human-level dexterous teleoperation_ . Instead of mapping hand joints in isolation, the operator specifies explicit, synchronized geometric targets for both the fingertip positions and the object pose. A low-level controller, trained entirely in simulation with Reinforcement Learning (RL), then handles the complex multi-contact physics necessary to physically realize these dual co-tracking goals in real time. The key technical designs for **TELEDEXTER** are three-fold: 

- **Consecutive subgoal co-tracking:** Rather than forcing rigid, frame-by-frame trajectory imitation, we decompose human reference motions into a sequence of synchronized fingertip and object pose subgoals. By training the policy to reach these consecutive targets rather than blindly copying exact motion configurations, the system gains the operational flexibility needed to discover physically feasible contact-switching strategies. This framework is optimized via a single-stage RL pipeline that couples sparse subgoal rewards with dense tracking rewards, eliminating the need for complex, task-specific reward engineering. 

- **Co-tracking sequence construction:** We introduce a geometry-aware retargeting pipeline that translates unscripted human hand-object demonstrations into physically grounded reference motions. Going beyond pure kinematic mapping, our approach utilizes a two-stage optimization that incorporates object meshes to enforce contact-surface attraction and penalize mesh interpenetration. This process yields synchronized sequences of fingertip targets and object poses that serve as geometrically feasible subgoals for the low-level controller. 

- **Sim-to-real robustness:** To ensure robust zero-shot sim-to-real transfer, we introduce random action masking as a strong action-space regularizer. This technique prevents the policy from 

2 

overfitting to perfectly synchronized simulated actuation, which, when combined with systematic domain randomization, allows the controller to deploy directly onto real robots. 

We evaluate **TELEDEXTER** on seven challenging dexterous teleoperation tasks across two distinct dexterous hand embodiments. These tasks range from object rearrangement requiring continuous in-hand reorientation to long-horizon tool use with a hammer, screwdriver, brush, and light bulb. **TELEDEXTER achieves an average success rate of 75% across these tasks, whereas baseline models consistently fail.** Furthermore, we demonstrate that the high-quality teleoperation demonstrations collected via **TELEDEXTER** can be directly leveraged to train fully autonomous policies via behavioral cloning, achieving closed-loop manipulation capabilities without a human in the loop during long-term and dexterous task execution. Ablation studies confirm that our consecutive subgoal tracking and reward design are essential for learning diverse in-hand manipulation modalities in a single stage, while random action masking successfully bridges the sim-to-real gap. Broadly, this work provides a scalable foundation for collecting rich, in-hand dexterous manipulation data, unlocking a viable path toward human-level robotic dexterity. 

## **2 Related Work** 

**Dexterous Teleoperation** provides a powerful paradigm for transferring human dexterity to robotic hands [3, 14–17]. One dominant line of work is kinematic retargeting, which kinematically translates the human hand configuration to robot joint positions, via vision-based tracking [5–8, 18], wearable or exoskeleton gloves [9–11, 19], or learned neural mappings [12]. This paradigm provides an intuitive, low-latency interface but lacks a dynamics prior, making contact-rich actions such as in-hand reorientation, finger gaiting, and tool use infeasible. To address this limitation, DexGen [13] learns a generative dexterous action prior from simulation rollouts that maps coarse teleoperation commands to fine hand actions, improving contact robustness. However, its reliance on synthetically generated grasp transitions as training goals does not guarantee physical feasibility, and encoding the action prior into a generative model introduces compounding errors that degrade real-world performance. In contrast, we directly train an RL controller guided from human hand–object reference motions, providing physically grounded goals that cover diverse in-hand manipulation modalities. The learned controller directly serves as the robust but agile low-level teleoperation policy, enabling human-level in-hand dexterity including long-horizon tool use. 

**Learning Dexterous Manipulation via RL** in simulation has driven rapid progress, from grasping [20–23], in-hand reorientation [24–30] to complex finger gaiting and dynamic skills [31, 32]. However, these approaches typically learn task-specific policies with dedicated reward engineering for each skill. Recent work mitigates this by using human hand–object interaction data as reference motions to guide RL, enabling diverse manipulation skills without per-task reward design [23, 33– 35]. However, these methods primarily learn one policy per trajectory and rarely achieve in-hand dexterous skills such as reorientation or finger gaiting. We attribute this to the dense frame-wise tracking formulation, which is overly restrictive for single-stage policy learning and prevents the RL agent from exploring dynamic contact strategies beyond basic grasping and wrist motion. To address this, we introduce a consecutive subgoal tracking formulation that learns from human hand–object reference motions, enabling diverse and dynamic in-hand skills within a single RL training stage. Combined with the proposed random action masking and systematic domain randomization [28, 36], the learned policy transfers zero-shot to the real robot as a dexterous teleoperation controller. 

## **3 TELEDEXTER** 

We formulate dexterous teleoperation as hand–object co-tracking. The operator specifies hand and object pose targets, and our learned low-level controller executes the multi-contact dynamics to physically reach these goals. As shown in Fig. 2, we first formulate the co-tracking problem given a set of hand-object reference motions, then present the single-stage RL framework for training the 

3 



<!-- Start of picture text -->
HOI Data Consecutive Subgoal Co-tracking RL Training Teleoperation<br>1<br>��−�<br>1) Consecutive Goal Reach<br>SAPG<br>��<br>�� �� 2) Dense Tracking<br>��<br>3) Regularization Term<br>2 Action Mask 3 Curriculum<br>�� w/ action  86% in  GravityFailure Tolerance TELEDEXTERObject Pose<br>✅ mask real world Human Fingertip Pos Robot<br>Next Goal  57% Subgoal Step<br>In-Traj ...<br>�� Consecutive Subgoal � +30 � +20 � +10 � �−10<br>��<br>traj:031 traj:014 traj:005 traj:008 traj:  ？<br>Reached ! Goal<br>Selection Next Goal<br><!-- End of picture text -->

Fig. 2: **Method overview of TELEDEXTER.** Given human hand-object reference motions, we train a cotracking controller via single-stage RL and deploy it zero-shot to real-world dexterous teleoperation. 

co-tracking controller (Sec. 3.1). We then describe how these reference motions are constructed (Sec. 3.2) and deploy the learned policy to the real world as the teleoperation controller (Sec. 3.3). 

**Problem Formulation** All quantities below are expressed in the wrist frame. The robot arm tracks the human wrist pose independently via inverse kinematics (IK). Given a set of hand-object reference motions (Sec. 3.2), our goal is to learn a co-tracking policy **_a_** _t_ = _πθ_ ( **_o_** _t, gt_ ) that drives the robot hand and the manipulated object toward target poses prescribed by a co-tracking goal _gt_ . Here **_o_** _t_ encodes the current robot hand-object state, **_a_** _t ∈_ R<sup>_n_dof</sup> are target joint positions, and the co-tracking goal specifies both target fingertip positions and target object pose: _gt_ = � **_p_** ˆ _t_ tip<sup>_,T_ˆ</sup><sup>_o_</sup> _t_ �, where **_p_** ˆ<sup>tip</sup> _t ∈_ R<sup>_Nf ×_3</sup> and _T_<sup>ˆ</sup> _t_<sup>_o_=</sup> � **_x_** ˆ _to_<sup>_,R_ˆ</sup> _t_<sup>_o_</sup> � _∈ SE_ (3). During teleoperation, _gt_ is constructed from real-time captured hand-object poses, casting dexterous teleoperation as a co-tracking problem. This formulation prescribes _what_ the hand and object should achieve, while leaving the contact strategy, i.e. _how_ , to the learned controller. 

### **3.1 Learning a Co-tracking Controller** 

Given the reference motions for the manipulated object, we train a hand-object co-tracking controller _πθ_ in simulation via RL. The co-tracking goals guide the controller to learn a dynamic hand-object action prior through simulated contact, moving beyond kinematic trajectory imitation. The controller input consists of the observation **_o_** _t_ and the co-tracking goal _gt_ . The observation **_o_** _t_ contains the current hand joint positions **_q_** _t_ , the object pose ( **_x_**<sup>_o_</sup> _t_<sup>_, R_</sup> _t_<sup>_o_)andthegravitydirectioninthewrist</sup> frame, and the previous action **_a_** _t−_ 1. **Consecutive Subgoal Co-tracking** Each reference trajectory is converted into a sequence of cotracking subgoals sampled at varying intervals. We term this formulation _consecutive subgoal cotracking_ : the policy must reach each hand-object subgoal in order before advancing to the next, while freely discovering its own contact strategy between subgoals. For a subgoal _gk_ = (ˆ **_p_**<sup>tip</sup> _k_<sup>_,T_ˆ</sup><sup>_o_</sup> _k_<sup>),</sup> the per-finger, object position, and object rotation tracking errors are 



4 

_reaching reward_ with _dense tracking reward_ : 



The indicator 1 reach( _t_ ) fires when the active subgoal is reached, and _w_ step weights the reward by the inter-subgoal step size. The score _r_ score measures how well the hand and object match the active subgoal: 



The dense tracking reward _r_ dense uses the same per-finger and object tracking terms at every timestep, scaled by _α_ dense, providing a small dense signal during early training. 

**Curriculum Learning** We progressively increase three dimensions of difficulty during training. (i) Gravity is reduced initially and annealed to full gravity, easing initial contact establishment. (ii) The subgoal tracking tolerances ( _ϵ_ tip _, ϵ_ pos _, ϵ_ rot) start permissive and are progressively tightened, enforcing stricter tracking precision over training. (iii) The inter-subgoal step size grows from small to large, so the policy first masters fine-grained local tracking and later handles longer-horizon goal jumps. Episodes are initialized at random frames across the reference motions, and successful traversal of one trajectory resets the environment to another (cross-trajectory reset), enabling continuous learning across the full reference-motion set. 

**Sim-to-Real Robustness** For sim-to-real transfer, we apply domain randomization to tolerate dynamics, sensing, and actuation mismatch between simulation and the real world. Following [28], we randomize the shape and dynamics properties of both the object and the dexterous hand, apply random external forces to the object, and inject observation noise and latency. In addition, we introduce _random action masking_ as a strong action-space regularization. Given the policy action **_a_** _t_ , we sample a binary mask **_m_** _t ∈{_ 0 _,_ 1 _}_<sup>_n_dof</sup> and apply ˜ **_a_** _t_ = **_m_** _t ⊙_ **_a_** _t_ + (1 _−_ **_m_** _t_ ) _⊙_ **_a_** ˜ _t−_ 1, where masked dimensions are frozen at the previous command for a randomly sampled duration. By forcing the policy to succeed even when subsets of joints retain stale commands, this regularization prevents the policy from overfitting to simulation dynamics, which inevitably differ from those of the real world. 

**Single-stage RL Training** Each controller is trained in a single RL stage using large-scale parallel simulation, without staged skill decomposition or task-specific reward engineering. We use Isaac Gym [37], and all reference motions for one object ( _∼_ 50 minutes in our setting) are loaded simultaneously. We use SAPG [38] to optimize the policy with 4 NVIDIA RTX 5090 GPUs, running _∼_ 62,000 parallel environments. Training converges within _∼_ 10<sup>10</sup> environment steps. Being reference-driven, the framework scales directly to new objects, hands and more interaction patterns. 

### **3.2 Hand-Object Reference Motion Construction** 

We now describe how the hand-object reference motions used in training are constructed. Starting from human hand-object interaction trajectories recorded by a motion-capture system, we convert them into robot hand-object reference motions through geometry-aware retargeting. The recorded interactions span three categories: _(i) in-hand translation_ , _(ii) in-hand rotation_ , and _(iii) free-play_ combining arbitrary grasps, finger gaiting, and tool-use motion sequences. 

**Geometry-aware Retargeting** The retargeting proceeds in two stages. The first stage follows vector-based retargeting [5, 6], optimizing robot joint angles **_q_** 1: _T_ to match human hand geometry via directional and inter-finger vector alignment. Kinematic retargeting alone does not account for object geometry or contact feasibility. The second stage refines the result with a geometry-aware optimization that incorporates the object mesh. The final trajectory is obtained by 



5 

where _L_<sup>_t_</sup> vec<sup>isthevector-retargetingloss[5,6].</sup> Let _Ht_ and _Ot_ denote the hand and object meshes at frame _t_ , with sdf _Ot_ ( _·_ ) the differentiable signed distance [39]. The surface term _L_<sup>_t_</sup> surf<sup>=</sup> _|S_ <u>1</u> _t|_ � _p∈St_<sup>ReLU(sdf</sup><sup>_O_</sup> _t_<sup>(</sup><sup>_p_)) pulls near-contact hand points (</sup><sup>_St_=</sup><sup>_{p_: sdf</sup><sup>_O_</sup> _t_<sup>(</sup><sup>_p_)</sup><sup>_< τ_surf</sup><sup>_}_) onto the</sup> object surface. The penetration term _L_<sup>_t_</sup> pen<sup>= �</sup> _p∈Ht_<sup>ReLU</sup> � _−_ sdf _Ot_ ( _p_ )� penalizes interpenetration. The self-collision term _L_<sup>_t_</sup> col<sup>=</sup><sup><u>1</u></sup> 2 � _f_ ( _i_ ) _̸_ = _f_ ( _j_ )<sup>ReLU</sup> �( _ri_ + _rj_ ) _−∥_ **_c_** _i −_ **_c_** _j∥_ 2� prevents inter-finger overlap via collision spheres with radii _ri, rj_ and centers **_c_** _i,_ **_c_** _j_ . _L_ smooth applies the Curobo [40] temporal smoothness energy on **_q_** 1: _T_ to suppress capture jitter. The output is a set of robot handobject reference trajectories _{_ ( **_q_**<sup>_∗_</sup> _t_<sup>_, T_</sup> _t_<sup>_o_)</sup><sup>_}T_</sup> _t_ =1<sup>in the wrist frame, from which the co-tracking goals used</sup> in Sec. 3.1 are constructed as fingertip targets **_p_** ˆ<sup>tip</sup> _t_ = FKtip( **_q_** _t_<sup>_∗_) and object targets</sup><sup>_T_ˆ</sup><sup>_o_</sup> _t_<sup>=</sup><sup>_T_</sup> _t_<sup>_o_.</sup> 

### **3.3 Real-world Teleoperation Deployment** 

The learned co-tracking controller deploys zero-shot as the teleoperation controller. A real-time system captures the operator’s wrist, fingertip, and object poses; the arm tracks the wrist via IK, while the fingertip and object poses form the co-tracking goal for the policy. For contact initialization, kinematic retargeting [6] handles pre-grasp positioning; once stable contact is established, the operator switches to the co-tracking controller for dexterous manipulation. 

## **4 Experiments** 

We conduct a systematic real-world evaluation of **TELEDEXTER** for dexterous hand teleoperation. In experiments, we describe the experimental setup (Sec. 4.1), compare **TELEDEXTER** against representative baselines on seven dexterous tasks across two hand embodiments (Sec. 4.2), demonstrate autonomous policy learning from collected teleoperation data (Sec. 4.3), and conduct ablation studies on consecutive subgoal tracking and random action masking (Sec. 4.4). 

### **4.1 Experimental Setup** 

**Robot Platforms** All real-world experiments are conducted on a Franka FR3 arm equipped with a dexterous robot hand. We evaluate two hand embodiments: LeapHand [41], a four-finger hand with 16 DoFs, and SharpaWave, a five-finger human-like hand with 22 DoFs, to validate that our framework can generalize across different robotic hand morphologies and actuation spaces. 

**Teleoperation Interface** We use a NOKOV MoCap system to track the operator’s hand pose and the manipulated object’s 6D pose in real time. For all methods, the operator’s wrist pose is converted into Franka arm commands via IK. The methods differ in how they map the captured hand and object references to dexterous hand actions. All teleoperation evaluations run at 30 Hz. 

**Baselines** _DexRT_ [5, 6] directly maps the operator’s hand motion to the robot hand through kinematic retargeting. _GeoRT_ [12] learns a neural retargeting function using geometric objectives. _DexGen_ [13] uses a learned generative action prior to convert teleoperation commands into contact-rich hand actions. _SimToolReal_ [42] is an object-centric sim-to-real tool manipulation method that requires human reference motions at inference time to guide execution. Although not a teleoperation approach, it provides a strong reference for learned dexterous tool use. 

### **4.2 Dexterous Teleoperation Evaluation** 

**Overview** As shown in Fig. 3, we evaluate **TELEDEXTER** on seven real-world dexterous tasks spanning two categories. The three reorientation tasks ( `CylinderReorient` , `CuboidReorient` , `BunnyReorient` ) test precise in-hand pose control over symmetric, edge/corner, and irregular geometries. The four tool-use tasks ( `HammerUse` , `BrushSweep` , `ScrewdriverUse` , `BulbReplace` ) require long-horizon multi-stage manipulation involving in-hand reorientation to transition between functional grasps, finger gaiting, and tool application. Together, these tasks provide a comprehensive evaluation of whether a teleoperation system can robustly execute diverse dexterous manipulation. 

6 



<!-- Start of picture text -->
CylinderReorient CuboidReorient BunnyReorient<br>1) Pick up 2) Reorient to the target pose 3) Place 1) Pick up 2) Reorient to the target pose 3) Place 1) Pick up 2) Reorient to the target pose 3) Place<br>HammerUse<br>1) Pick up 2) Rotate face-down 3) Drive two nails 4) Rotate claw-down 5) Pull out two nails 6) Rotate parallel to the table 7) Place<br>BrushSweep<br>1) Pick up 2) Rotate 3) Sweep forward 4) Rotate bristles-right 5) Sweep trash rightward into target area 6) Rotate parallel to the table 7) Place<br>ScrewdriverUse BulbReplace<br>1) Pick up 2) Rotate 3) Tighten the screw 4) Rotate  5) Place 1) Pick up 2) Rotate 3) Screw the bulb 4) Unscrew the bulb 5) Rotate 6) Place<br><!-- End of picture text -->

Fig. 3: **Task descriptions.** Seven dexterous tasks across two categories: three reorientation tasks over diverse geometries and four long-horizon tool-use tasks. Each task is decomposed into well-defined stages. 

Tab. 1: **Dexterous teleoperation results on SharpaWave.** Each cell: **SR** / **TP** (%; higher is better). _SimToolReal_ is not a teleoperation method ( _†_ = category-specific, _‡_ = all categories) averaged over three tasks only. 

|**Task**|_DexRT_|_GeoRT_|_DexGen_|_SimToolReal_<sup>_†_</sup>|_SimToolReal_<sup>_‡_</sup>|**TELEDEXTER**|
|---|---|---|---|---|---|---|
|`CylinderReorient`|6.7 / 37.8|0.0 / 24.4|0.0 / 31.1|—|—|**80.0**/**86.7**|
|`CuboidReorient`|26.7 / 51.1|0.0 / 33.3|0.0 / 28.9|—|—|**80.0**/**86.7**|
|`BunnyReorient`|0.0 / 35.6|0.0 / 31.1|0.0 / 26.7|—|—|**66.7**/**77.8**|
|`HammerUse`|0.0 / 26.7|0.0 / 30.5|0.0 / 26.7|0.0 / 27.6|20.0 / 36.2|**66.7**/**86.7**|
|`BrushSweep`|0.0 / 39.0|0.0 / 29.5|0.0 / 8.6|26.7 / 41.9|0.0 / 5.7|**73.3**/**89.5**|
|`ScrewdriverUse`|6.7 / 37.3|0.0 / 25.3|0.0 / 33.3|0.0 / 17.3|0.0 / 20.0|**73.3**/**86.7**|
|`BulbReplace`|0.0 / 35.6|0.0 / 25.6|0.0 / 20.0|—|—|**86.7**/**95.6**|
|**Average**|5.7 / 37.6|0.0 / 28.5|0.0 / 25.0|8.9 / 28.9|6.7 / 20.6|**75.2**/**87.1**|



**Protocol and Metrics** For each task, we conduct 15 trials Tab. 2: **Teleoperation on LeapHand.** per method. Each task is decomposed into a sequence of **Task TELEDEXTER** well-defined stages (shown in Fig. 3). We report two met- `CylinderReorient` 60.0 / 73.3 rics. Success rate ( **SR** ) is the percentage of trials complet- `CuboidReorient` 73.3 / 82.2 ing all stages. Task progress ( **TP** ) is the average percentage of stages completed per trial, where each stage contributes equally. A trial is terminated when an unrecoverable grasp loss or object drop occurs during execution. 

**Results and Analysis** As shown in Tab. 1, **TELEDEXTER** achieves 75.2% average **SR** and 87.1% average **TP** across all seven tasks, while all baselines near-uniformly fail. On the reorientation tasks, **TELEDEXTER** achieves 66.7–80.0% **SR** by executing dynamic in-hand reorientation through learned contact strategies. In contrast, kinematic retargeting methods ( _DexRT_ , _GeoRT_ ) rarely progress beyond the initial pick-up stage, as they lack the dynamics prior needed for contactrich in-hand manipulation. _DexGen_ , despite its learned action prior, similarly fails due to compounding errors in its generative model that degrade real-world contact execution. The gap widens on tool-use tasks, which demand long-horizon coordination of functional grasp transitions, finger gaiting, and tool application. **TELEDEXTER** achieves 66.7–86.7% **SR** on these tasks, while all teleoperation baselines achieve near-zero **SR** . The **TP** metric reveals where failures occur: **TELEDEXTER** ’s narrow **SR** -to- **TP** gap (75.2% vs. 87.1%) indicates that most failures happen at late task stages, whereas baselines consistently collapse at the first stage requiring in-hand reorientation or finger gaiting. On `BulbReplace` , **TELEDEXTER** completes both the screw-in and unscrew rotation stages without losing a single trial (15 _/_ 15 through stage 4 of 6), with the only failures at final placement (13 _/_ 15). Similarly, on `ScrewdriverUse` , 13 of 15 trials sustain continuous finger gaiting through the tightening stage, a contact mode that no baseline can execute. _SimToolReal_ , an object-centric policy trained specifically for tool manipulation, achieves at most 

7 

Tab. 3: **Autonomous policy stage-wise success.** `BulbInstall` : pick up _→_ reorient _→_ align _→_ install; `HammerDriver` : pick up _→_ rotate _→_ drive nails; `BrushForward` : pick up _→_ rotate _→_ sweep forward. 

|**Task**|Stage 1|Stage 2|Stage 3|Stage 4|**SR**|
|---|---|---|---|---|---|
|`BulbInstall`|13/15|12/13|8/12|7/8|46.7%|
|`HammerDriver`|15/15|15/15|11/15|—|73.3%|
|`BrushForward`|7/15|7/7|6/7|—|40.0%|



26.7% **SR** on a single task and fails on the others, indicating that even dedicated tool-use policies struggle to generalize across the diverse contact transitions required for long-horizon manipulation. As shown in Tab. 2, applying the same training pipeline to LeapHand yields a strong controller with minimal embodiment-specific tuning. Notably, both controllers are trained from the same human hand-object interaction reference motions; only the geometry-aware retargeting stage adapts to the target morphology (4-finger, 16-DoF LeapHand vs. 5-finger, 22-DoF SharpaWave). Despite this substantial morphological gap, LeapHand achieves 60 _._ 0–73 _._ 3% **SR** on the reorientation tasks, confirming that the framework generalizes across embodiments without re-collecting human reference motions. 

### **4.3 From Teleoperation to Autonomy** 

**Overview** A key advantage of **TELEDEXTER** is its ability to collect dexterous manipulation data beyond the reach of existing teleoperation systems. While the teleoperation evaluation (Sec. 4.2) demonstrates that **TELEDEXTER** enables human-level in-hand dexterity, the collected trajectories also serve as high-quality expert demonstrations for training autonomous policies. To validate this, we train Diffusion Policies [43] on three dexterous tasks: `BulbInstall` , `HammerDriver` , and `BrushForward` . Each task retains the most contact-intensive stages of its teleoperation counterpart while removing the return-andplace phases, isolating the core dexterous manipulation skills. 



<!-- Start of picture text -->
Sharpa Wave<br>Third-person ViewRealsense D455 - RGB Dexterous Hand<br>Wrist-cam view<br>Realsense D405 - RGB<br>Autonomous policy rollout  →<br>Wrist-cam view (D405 RGB)<br><!-- End of picture text -->

Fig. 4: **Autonomous policy setup and rollout.** 

**Protocol and Metrics** We adopt the Conv-UNet Diffusion Policy architecture [43], conditioned on RGB observations from third-person and wrist-mounted cameras, as shown in Fig. 4. For each task, we collect 50 expert demonstrations and evaluate each policy over 15 real-world trials. Each task is decomposed into well-defined stages following the same protocol as the teleoperation evaluation; we report stage-wise success (the number of trials surviving past each stage) and overall **SR** . 

**Results and Analysis** As shown in Tab. 3, all three tasks achieve non-trivial success rates from only 50 demonstrations, confirming that **TELEDEXTER** captures sufficiently rich contact-mode coverage for behavioral cloning across diverse dexterous manipulation skills. The stage-wise breakdown reveals a distinct bottleneck per task. `HammerDriver` achieves the highest **SR** (73 _._ 3%) with perfect grasping and reorientation (15 _/_ 15 through stage 2). The only failures occur at the nail-driving stage, where the policy must sustain repeated contact force against the foam target. `BulbInstall` (46 _._ 7% **SR** ) shows a similar pattern: grasping and reorientation succeed reliably, but the precision alignment stage (8 _/_ 12) is the primary bottleneck. Once aligned, installation succeeds in 7 _/_ 8 trials, indicating that the screw-in skill transfers well from demonstrations. `BrushForward` (40 _._ 0% **SR** ) presents the opposite profile: grasping is the dominant failure point (7 _/_ 15), due to the thin and irregular brush handle requiring precise finger placement that is difficult to resolve from RGB alone. Trials that survive the grasp nearly all complete the subsequent rotation and sweep (6 _/_ 7). 

8 

Tab. 4: **Sparse subgoal vs. dense tracking** (sim). EpLen: episode length ( _↑_ ). Goals: consecutive subgoals reach ( _↑_ ). 

Tab. 5: **Random action masking** (real). Each cell reports **SR** / **TP** (%). 

||Dense e|val: EpLen|Sparse e|val: Goals|Task|w/ AM|w/o AM|
|---|---|---|---|---|---|---|---|
|Object|Ours|Dense|Ours|Dense|`HammerUse`|**66.7**/**86.7**|33.3 / 57.1|
|Cuboid|**378.6**|115.8|**32.6**|2.6|`ScrewdriverUse`|**73.3**/**86.7**|0.0 / 36.0|
|Hammer|**376.9**|131.2|**186.6**|2.7|`CuboidReorient`|**80.0**/**86.7**|26.7 / 51.1|
|Screwdriver|**373.2**|88.7|**178.5**|2.7||||



Notably, no baseline teleoperation system evaluated in Tab. 1 can reliably complete any of these three tasks, making it infeasible to collect comparable demonstration data with existing methods. These results validate **TELEDEXTER** as both a teleoperation interface and a scalable data collection pipeline for autonomous dexterous manipulation. 

### **4.4 Ablation Studies** 

**Consecutive Subgoal Tracking vs. Dense Tracking** We compare our consecutive subgoal tracking formulation against standard dense frame-wise tracking in simulation on held-out reference motions for three objects (Tab. 4). We evaluate in two modes: dense, where the reference advances every control step, and sparse, where the target advances only after the current subgoal is reached. Even under dense evaluation, which favors the dense tracking baseline, sparse subgoal tracking achieves significantly longer episode lengths. Dense frame-wise tracking forces the policy to replicate reference trajectories step by step, leaving insufficient tolerance to discover physically feasible contact strategies and causing early termination. In contrast, sparse subgoal tracking only requires stable goal completion, allowing the policy to find feasible contact sequences through simulation rollout. This advantage is amplified in sparse evaluation, where dense tracking policies stall after only a few subgoals while sparse subgoal tracking reaches orders of magnitude more. 

**Random Action Masking** We ablate random action masking on three real-world teleoperation tasks (Tab. 5). Removing action masking causes substantial degradation across all evaluated tasks. Random action masking serves as a strong action-space regularization that prevents the policy from overfitting to simulation dynamics, which inevitably differ from real-world dynamics. Without this regularization, the policy exploits simulation-specific dynamics patterns that do not transfer, confirming that random action masking is critical for zero-shot sim-to-real deployment. 

## **5 Conclusion** 

We introduce **TELEDEXTER** , a hand-object co-tracking controller that takes a concrete step toward human-level dexterous teleoperation. Built on our proposed _consecutive subgoal tracking_ with _hybrid reward design_ , and _random action masking_ , **TELEDEXTER** learns diverse in-hand skills in single-stage RL with no task-specific reward, and transfers to real robots. Across seven long-horizon and challenging dexterous tasks, **TELEDEXTER** achieves a strong success rate where baselines uniformly fail. Furthermore, the collected demonstrations successfully train policies to autonomously execute long-horizon dexterous tasks, establishing **a scalable foundation for collecting rich inhand dexterous manipulation data and a viable path toward human-level robotic dexterity** . 

## **6 Limitations** 

**TELEDEXTER** currently learns an object-specific controller. Adapting to a new object requires collecting human hand-object interaction data and training a dedicated policy. Scaling to a unified, object-conditioned controller that generalizes across object categories without per-object data collection and training is a promising direction for future work. 

Our real-world deployment relies on a motion-capture system for real-time hand and object pose estimation. Replacing this with a markerless, vision-based tracking system would significantly lower the barrier to deployment and broaden the practical applicability of the framework. 

9 

## **References** 

- [1] A. Billard and D. Kragic. Trends and challenges in robot manipulation. _Science_ , 364(6446): eaat8414, 2019. 

- [2] I. M. Bullock, R. R. Ma, and A. M. Dollar. A hand-centric classification of human and robot dexterous manipulation. _IEEE Transactions on Haptics_ , 6(2):129–144, 2013. doi:10.1109/ TOH.2012.53. 

- [3] T. Zhang, Z. McCarthy, O. Jow, D. Lee, X. Chen, K. Goldberg, and P. Abbeel. Deep imitation learning for complex manipulation tasks from virtual reality teleoperation. In _2018 IEEE international conference on robotics and automation (ICRA)_ , pages 5628–5635. IEEE, 2018. 

- [4] A. Mandlekar, D. Xu, R. Mart´ın-Mart´ın, Y. Zhu, L. Fei-Fei, and S. Savarese. Human-in-theloop imitation learning using remote teleoperation. _arXiv preprint arXiv:2012.06733_ , 2020. 

- [5] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. _arXiv preprint arXiv:2307.04577_ , 2023. 

- [6] A. Handa, K. Van Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. Ratliff, and D. Fox. Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 

- [7] R. Ding, Y. Qin, J. Zhu, C. Jia, S. Yang, R. Yang, X. Qi, and X. Wang. Bunny-visionpro: Realtime bimanual dexterous teleoperation for imitation learning. In _2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 12248–12255. IEEE, 2025. 

- [8] X. Cheng, J. Li, S. Yang, G. Yang, and X. Wang. Open-television: Teleoperation with immersive active visual feedback. In _8th Annual Conference on Robot Learning_ , 2024. 

- [9] H. Zhang, S. Hu, Z. Yuan, and H. Xu. Doglove: Dexterous manipulation with a low-cost open-source haptic force feedback glove. _arXiv preprint arXiv:2502.07730_ , 2025. 

- [10] H.-S. Fang, B. Romero, Y. Xie, A. Hu, B.-R. Huang, J. Alvarez, M. Kim, G. Margolis, K. Anbarasu, M. Tomizuka, et al. Dexop: A device for robotic transfer of dexterous human manipulation. _arXiv preprint arXiv:2509.04441_ , 2025. 

- [11] A. Zhu, M. Zhu, B. J. Kim, J. V. S. Ramos, Y. Shi, Y. Wu, R. Dhar, F. Yang, R. Hou, H. Fang, et al. Dexexo: A wearability-first dexterous exoskeleton for operator-agnostic demonstration and learning. _arXiv preprint arXiv:2603.17323_ , 2026. 

- [12] Z.-H. Yin, C. Wang, L. Pineda, K. Bodduluri, T. Wu, P. Abbeel, and M. Mukadam. Geometric retargeting: A principled, ultrafast neural hand retargeting algorithm. In _2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 17376–17382. IEEE, 2025. 

- [13] Z.-H. Yin, C. Wang, L. Pineda, F. Hogan, K. Bodduluri, A. Sharma, P. Lancaster, I. Prasad, M. Kalakrishnan, J. Malik, et al. Dexteritygen: Foundation controller for unprecedented dexterity. _arXiv preprint arXiv:2502.04307_ , 2025. 

- [14] G. Niemeyer, C. Preusche, S. Stramigioli, and D. Lee. Telerobotics. In _Springer handbook of robotics_ , pages 1085–1108. Springer, 2016. 

- [15] H. Hedayati, M. Walker, and D. Szafir. Improving collocated robot teleoperation with augmented reality. In _Proceedings of the 2018 ACM/IEEE international conference on humanrobot interaction_ , pages 78–86, 2018. 

10 

- [16] G. Du, P. Zhang, J. Mai, and Z. Li. Markerless kinect-based hand tracking for robot teleoperation. _International Journal of Advanced Robotic Systems_ , 9(2):36, 2012. 

- [17] J. Kofman, S. Verma, and X. Wu. Robot-manipulator teleoperation by markerless vision-based hand-arm tracking. _International Journal of Optomechatronics_ , 1(3):331–357, 2007. 

- [18] S. Yang, M. Liu, Y. Qin, R. Ding, J. Li, X. Cheng, R. Yang, S. Yi, and X. Wang. Ace: A crossplatform and visual-exoskeletons system for low-cost dexterous teleoperation. In _8th Annual Conference on Robot Learning_ , 2024. 

- [19] C. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and C. K. Liu. Dexcap: Scalable and portable mocap data collection system for dexterous manipulation. _arXiv preprint arXiv:2403.07788_ , 2024. 

- [20] P. Li, T. Liu, Y. Li, Y. Geng, Y. Zhu, Y. Yang, and S. Huang. Gendexgrasp: Generalizable dexterous grasping. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 8068–8074. IEEE, 2023. 

- [21] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4737–4746, 2023. 

- [22] Y. Li, B. Liu, Y. Geng, P. Li, Y. Yang, Y. Zhu, T. Liu, and S. Huang. Grasp multiple objects with one hand. _IEEE Robotics and Automation Letters_ , 9(5):4027–4034, 2024. 

- [23] K. Li, P. Li, T. Liu, Y. Li, and S. Huang. Maniptrans: Efficient dexterous bimanual manipulation transfer via residual learning. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 6991–7003, 2025. 

- [24] M. Andrychowicz, B. Baker, M. Chociej, R. J´ozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and W. Zaremba. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39(1), 2020. doi:10.1177/0278364919887447. 

- [25] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, et al. Solving rubik’s cube with a robot hand. _arXiv preprint arXiv:1910.07113_ , 2019. 

- [26] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam, et al. Dextreme: Transfer of agile in-hand manipulation from simulation to reality. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 5977–5984. IEEE, 2023. 

- [27] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik. In-hand object rotation via rapid motor adaptation. In _Proceedings of The 6th Conference on Robot Learning_ , volume 205 of _Proceedings of Machine Learning Research_ , pages 1722–1732. PMLR, 2023. URL `https: //proceedings.mlr.press/v205/qi23a.html` . 

- [28] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal. Visual dexterity: In-hand reorientation of novel and complex object shapes. _Science Robotics_ , 8(84):eadc9244, 2023. 

- [29] M. Yang, A. Church, Y. Lin, C. J. Ford, H. Li, E. Psomopoulou, D. A. Barton, N. F. Lepora, et al. Anyrotate: Gravity-invariant in-hand object rotation with sim-to-real touch. In _8th Annual Conference on Robot Learning_ , 2024. 

- [30] X. Liu, H. Wang, and L. Yi. Dexndm: Closing the reality gap for dexterous in-hand rotation via joint-wise neural dynamics model. _arXiv preprint arXiv:2510.08556_ , 2025. 

11 

- [31] H. Qi, B. Yi, M. Lambeta, Y. Ma, R. Calandra, and J. Malik. From simple to complex skills: The case of in-hand object reorientation. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 14291–14298. IEEE, 2025. 

- [32] J. Wang, Y. Yuan, H. Che, H. Qi, Y. Ma, J. Malik, and X. Wang. Lessons from learning to spin” pens”. _arXiv preprint arXiv:2407.18902_ , 2024. 

- [33] X. Liu, K. Lyu, J. Zhang, T. Du, and L. Yi. Parameterized quasi-physical simulators for dexterous manipulations transfer. In _European Conference on Computer Vision_ , pages 164– 182. Springer, 2024. 

- [34] Y. Chen, C. Wang, Y. Yang, and K. Liu. Object-centric dexterous manipulation from human motion data. In _8th Annual Conference on Robot Learning_ , 2024. 

- [35] X. Liu, J. Adalibieke, Q. Han, Y. Qin, and L. Yi. Dextrack: Towards generalizable neural tracking control for dexterous manipulation from human references. _arXiv preprint arXiv:2502.09614_ , 2025. 

- [36] X. B. Peng, M. Andrychowicz, W. Zaremba, and P. Abbeel. Sim-to-real transfer of robotic control with dynamics randomization. In _2018 IEEE international conference on robotics and automation (ICRA)_ , pages 3803–3810. IEEE, 2018. 

- [37] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 

- [38] J. Singla, A. Agarwal, and D. Pathak. Sapg: split and aggregate policy gradients. In _Proceedings of the 41st International Conference on Machine Learning_ , pages 45759–45772, 2024. 

- [39] C. Fuji Tsang, M. Shugrina, J. F. Lafleche, O. Perel, C. Loop, T. Takikawa, V. Modi, A. Zook, J. Wang, W. Chen, T. Shen, J. Gao, K. M. Jatavallabhula, E. Smith, A. Rozantsev, S. Fidler, G. State, J. Gorski, T. Xiang, J. Li, M. Li, and R. Lebaredian. Kaolin: A pytorch library for accelerating 3d deep learning research, 2024. URL `https://github.com/ NVIDIAGameWorks/kaolin` . 

- [40] B. Sundaralingam, A. Murali, and S. Birchfield. curobov2: Dynamics-aware motion generation with depth-fused distance fields for high-dof robots, 2026. 

- [41] K. Shaw, A. Agarwal, and D. Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _arXiv preprint arXiv:2309.06440_ , 2023. 

- [42] K. Kedia, T. G. W. Lum, J. Bohg, and C. K. Liu. Simtoolreal: An object-centric policy for zero-shot dexterous tool manipulation. _arXiv preprint arXiv:2602.16863_ , 2026. 

- [43] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song. Diffusion policy: Visuomotor policy learning via action diffusion. _The International Journal of Robotics Research_ , 44(10-11):1684–1704, 2025. 

12 

## **Supplementary Materials of Towards Human-level Dexterous Teleoperation** 

This appendix complements the main paper with extended results and full implementation details. Sec. A provides extended results and analysis, including any-to-any reposition tests, additional ablation studies, stage-wise teleoperation analysis, and failure modes. Sec. B details the task definitions, hardware setup, and teleoperation interface. Sec. C details the complete implementation of **TELEDEXTER** . Sec. D details each baseline implementation, and Sec. E details the autonomous policy architecture and training. 

## **A Extended Results and Analysis** 

### **A.1 Any-to-Any Reposition Evaluation** 

**Overview** This evaluation directly tests whether our co-tracking controller, deployed zero-shot to the real robot, can handle arbitrary in-hand hand-object tracking goal transitions. During teleoperation the operator’s goal can jump to any feasible hand-object configuration at any time; the any-toany reposition test isolates this capability by streaming a sequence of randomly sampled targets and measuring how many the controller reaches consecutively before failure. 

**Protocol and Metrics** We evaluate the co-tracking controller on `Cylinder` and `Cuboid` on LeapHand. We choose LeapHand for this stress test. Despite LeapHand’s more limited dexterity (4 fingers, 16 DoFs vs. 5 fingers, 22 DoFs), the controller trained by our framework still demonstrates non-trivial in-hand repositioning capability and robustness, as shown below. 

For each object, we construct a hand-object targets pool consisting of all frames from our HOI reference set (Sec. C.6), which covers the full feasible workspace of in-hand configurations. We run 15 trials per object. Each trial begins by sampling an initial grasp pose from the pool; the tester places the object into the hand accordingly and starts the controller. The controller is then queried with a stream of targets, each freshly sampled from the same pool as soon as the previous one is reached. A target is counted as reached when the object position error falls below 2 cm and the object rotation error falls below 20<sup>_◦_</sup> simultaneously. A trial terminates when (i) the object slips out of the hand, or (ii) the active target has not been reached for 20 s. We report two metrics: consecutive successes, the number of targets reached in sequence before failure (averaged over trials), and pertarget success rate, the fraction of all attempted targets that are successfully reached. 

**Results and Analysis** As shown in Tab. 6, the controller sustains long sequences of arbitrary goal transitions on both objects, confirming that it generalizes well beyond the training reference trajectories. On `Cylinder` the controller reaches 41 _._ 1 consecutive targets on average with a per-target success rate of 97 _._ 6%, substantially outperforming `Cuboid` (12 _._ 1 consecutive successes, 92 _._ 3%). We attribute this gap to object geometry: the cylinder’s continuous surface allows fingers to slide and roll the object fluidly during transitions without encountering abrupt geometric changes, and its rotational symmetry reduces the effective distance between arbitrary target poses. The cuboid’s edges and corners, by contrast, can obstruct finger motion during rapid regrasps — fingers must navigate around these features to reach certain target orientations, increasing the chance of contact transition jams and failed repositioning attempts. 

Tab. 6: **Any-to-any results on LeapHand.** Each object is evaluated over 15 trials. 

|**Object**|Consecutive Successes (_↑_)|Per-target SR (_↑_)|
|---|---|---|
|`Cylinder`|41_._1|97_._6%|
|`Cuboid`|12_._1|92_._3%|



13 

### **A.2 Additional Ablation Studies** 

We ablate two training recipe choices on `Hammer` : the curriculum schedule (Sec. C.3) and the policy optimizer (SAPG vs. PPO). All other training settings and reference motions are shared. We report training curves of reward and consecutive subgoals reached in Fig. 5. 



<!-- Start of picture text -->
Ours Ours<br>1.4 w/o curriculum 50 w/o curriculum<br>PPO PPO<br>1.2<br>40<br>1.0<br>0.8 30<br>0.6<br>20<br>0.4<br>10<br>0.2<br>0.0 0<br>0 3 6 9 12 15 18 0 3 6 9 12 15 18<br>Number of envsteps (×10 9 ) Number of envsteps (×10 9 )<br>(a) Reward. (b) Consecutive successes.<br>4Reward (×10)<br>Consecutive Successes<br><!-- End of picture text -->

Fig. 5: **Training-recipe ablation curves on** `Hammer` **.** (a) Reward and (b) consecutive subgoals reached vs. environment steps for the full method, without curriculum, and with PPO replacing SAPG. 

**Curriculum Schedule** As shown in Fig. 5, disabling the curriculum (training at full deployment difficulty throughout) produces faster initial progress but plateaus at a lower final performance. The curriculum completes its annealing within the first 2 _×_ 10<sup>9</sup> environment steps, yet the advantage it provides continues to grow well beyond that point. We attribute this to the quality of the earlytraining foundation: the curriculum first exposes the policy to small subgoal steps, permissive tolerances, and reduced gravity, allowing it to discover a diverse repertoire of stable contact primitives before difficulty ramps up. Without this scaffolding, the policy must simultaneously learn basic contact strategies and cope with full-difficulty dynamics, converging to a narrower set of behaviors that limits its ability to compose longer manipulation sequences later in training. 

**PPO vs. SAPG** As shown in Fig. 5, replacing SAPG [38] with vanilla PPO causes a substantial drop in both reward and consecutive successes. SAPG maintains multiple independently exploring policy blocks whose gradients are aggregated, promoting diverse strategy discovery within a single training run. This exploration diversity is critical for co-tracking, where the policy must master qualitatively different contact modes — translation, continuous rotation, finger gaiting, and regrasping — within a single network. PPO’s unimodal gradient updates tend to commit early to a limited strategy set, under-covering the full spectrum of in-hand manipulation modalities in our reference motions. 

### **A.3 Stage-Wise Teleoperation Success Analysis** 

For each of the four long-horizon tool-use tasks, we plot the number of trials (out of 15) that survive past each task stage for **TELEDEXTER** and all baselines (Fig. 6). The main paper highlights key stage-wise numbers for **TELEDEXTER** ; here we provide the complete per-stage breakdown across all methods and analyze where each baseline breaks down. We additionally include _SimToolReal_ [42], an object-centric sim-to-real tool-use policy that is not a teleoperation method but provides a strong reference for learned dexterous tool manipulation. 

Across all four tasks, a consistent pattern emerges. **TELEDEXTER** retains 13–15 out of 15 trials through the demanding mid-task stages and only drops modestly at the final placement stages, whereas every baseline suffers a sharp collapse at or shortly after the first stage that requires in-hand reorientation or functional grasp transition. 

In `HammerUse` , all methods pick up the hammer (stage 1), but baselines diverge sharply at stage 2 (rotate face-down): _DexRT_ drops from 15 to 6 and _DexGen_ from 14 to 10. By stage 4 (rotate claw-down), no teleoperation baseline retains any trial. _SimToolReal_<sup>_†_</sup> (category-specific) leverages task-specific training to reach 14 _/_ 15 at stage 2 but collapses entirely at stage 3 (drive nails), unable 

14 



<!-- Start of picture text -->
HammerUse BrushSweep<br>15<br>12<br>9<br>6<br>3<br>0<br>0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7<br>ScrewdriverUse BulbReplace<br>15<br>12<br>9<br>6<br>3<br>0<br>0 1 2 3 4 5 0 1 2 3 4 5 6<br>Stage<br>Ours DexRT GeoRT DexGen SimToolReal† SimToolReal‡<br>Trials Reached  (/15)<br><!-- End of picture text -->

Fig. 6: **Stage-wise success on four long-horizon tool-use tasks.** For each task, the horizontal axis indexes the task stage and the vertical axis is the number of trials (out of 15) that reach that stage. Each curve corresponds to one method ( **TELEDEXTER** and baselines from Tab. 1 in the main paper). _SimToolReal_ is not a teleoperation method but is included as a strong baseline for learned tool manipulation. 

to sustain the repeated contact force required for hammering. _SimToolReal_<sup>_‡_</sup> (all-category) maintains 3 _/_ 15 through completion at the cost of weaker early-stage performance. **TELEDEXTER** retains all 15 trials through stage 3 and 10 through final placement. 

In `BrushSweep` , a similar bottleneck emerges at grasp-transition stages. _DexGen_ collapses earliest, losing most trials at pick-up (5 _/_ 15) due to compounding generative-model errors. _DexRT_ and _GeoRT_ survive the initial sweep (stage 3, 8 _/_ 15 each) but fail at stage 4 (rotate bristles-right), which demands controlled in-hand reorientation while maintaining grasp. _SimToolReal_<sup>_†_</sup> is the strongest baseline on this task with 4 _/_ 15 completions, while **TELEDEXTER** reaches 11 _/_ 15. 

In `ScrewdriverUse` , _DexGen_ maintains 10 _/_ 15 through stage 2 (rotate to align) but drops to 0 at stage 3 (tighten the screw), as its action prior cannot sustain continuous axial rotation. Both _SimToolReal_ variants also fail entirely at stage 3. _DexRT_ retains 1 _/_ 15 to completion, the only teleoperation baseline trial to finish this task. **TELEDEXTER** maintains 13 _/_ 15 through tightening and finishes with 11 _/_ 15. 

In `BulbReplace` , evaluated without _SimToolReal_ as the task falls outside its object-centric formulation, all methods pick up the bulb (15 _/_ 15), but the critical drop occurs at stage 3 (screw in), where _DexRT_ falls from 12 to 2 and both _GeoRT_ and _DexGen_ reach 0. These stages require precise bidirectional rotation about the bulb axis under sustained contact, which kinematic retargeting cannot achieve. **TELEDEXTER** completes both rotational stages without trial loss (15 _/_ 15 through stage 4) and finishes with 13 _/_ 15. 

Taken together, these results show that all baselines fail not at grasping or gross positioning, but at contact-rich in-hand manipulation: reorientation, finger gaiting, and sustained tool application. Kinematic methods ( _DexRT_ , _GeoRT_ ) lack a dynamics prior and collapse at the first contact-intensive stage. _DexGen_ suffers compounding trajectory drift that causes abrupt failure at contact transitions. _SimToolReal_ achieves partial success on trained tool categories but cannot generalize across the diverse contact modes within a single long-horizon task. **TELEDEXTER** sustains high trial survival precisely at these stages, confirming that the co-tracking controller provides the in-hand dexterity needed for long-horizon tool use. 

15 



<!-- Start of picture text -->
(a) Interaction perturbation.<br><!-- End of picture text -->



























<!-- Start of picture text -->
(b) Contact transition jam.<br><!-- End of picture text -->















<!-- Start of picture text -->
(c) Tracking stall.<br><!-- End of picture text -->

















Fig. 7: **Real-world failure cases.** Each panel shows a snapshot at the point of failure together with the representative failure mode: (a) interaction perturbation, (b) contact transition jam, (c) tracking stall. 

### **A.4 TELEDEXTER Failure Analysis** 

We identify three dominant failure modes of our teleoperation controller, illustrated in Fig. 7. 

- **Interaction perturbation (Fig. 7a).** Forceful tool–environment contact, such as striking a nail during `HammerUse` , generates impulsive reaction forces that shift the object’s in-hand pose by a large, instantaneous amount. The controller, trained exclusively on free-space hand–object interaction, has never encountered such impact dynamics and cannot recover from the resulting out-of-distribution grasp configuration. This mode does not appear in reorientation-only tasks. 

- **Contact transition jam (Fig. 7b).** During finger gaiting or in-hand reorientation, a finger that should lift away occasionally remains wedged against the object due to actuator compliance or geometric interlocking. As the remaining fingers continue to move, the jam generates unbalanced forces that eject the object from the hand. This failure is most frequent on irregular objects ( `BunnyReorient` ) where concavities increase the chance of interlocking. 

- **Tracking stall (Fig. 7c).** The controller attempts a regrasp but fails to establish contacts that can move the object toward the target pose. Unlike the contact transition jam, the object is not lost—the hand simply cannot make progress. We attribute this to the absence of tactile observations (Tab. 7): the policy cannot distinguish between a finger pressing against the object and one sliding past it, and thus cannot adapt when a regrasp attempt fails. 

16 

The three modes point to distinct limitation of our current system. Interaction perturbation reflects a _training distribution_ gap, as tool–environment impact dynamics are absent from the simulation training. Contact transition jams reveal an _actuation compliance_ mismatch between rigid-body simulation and real direct-drive fingers with passive compliance. Tracking stalls expose the lack of _tactile observation_ , without which the policy cannot close the loop on contact state during regrasping. Addressing these limits through interaction-aware training, compliant-contact simulation, and tactile-rich observation spaces is a promising direction for future work. 

## **B Experimental Setup Details** 

### **B.1 Teleoperation Task Definitions** 

We provide detailed descriptions of the seven real-world tasks introduced in the main paper (Fig. 3), together with their stage decompositions. Each task is decomposed into _N_ well-defined stages that the trial must reach in order. The task progress ( **TP** ) reported in the main paper is the average _k/N_ of the furthest stage _k_ reached across trials, and the success rate ( **SR** ) is the fraction of trials that reach all _N_ stages. For all tasks, stage 0 _/N_ denotes failure to pick up the object. We wrap the tested objects with medical bandage tape to increase surface friction. 

`CylinderReorient` **/** `CuboidReorient` **/** `BunnyReorient` **(** 3 **stages each).** The three reorientation tasks share an identical stage decomposition and differ only in object geometry, testing continuous in-hand pose control on rotationally symmetric ( `CylinderReorient` ), corner-rich ( `CuboidReorient` ), and irregular freeform ( `BunnyReorient` ) geometries. _Stages:_ 

- 1 _/_ 3: picked up the object. 

- 2 _/_ 3: reoriented to the target pose in-hand. 

- 3 _/_ 3: placed back on the table. 

`HammerUse` **(** 7 **stages).** A long-horizon task that exercises bidirectional functional grasp transitions (face-down vs. claw-down) and repeated striking and pulling. _Stages:_ 

- 1 _/_ 7: picked up the hammer. 

- 2 _/_ 7: rotated face-down for hammering. 

- 3 _/_ 7: drove the two nails into the board. 

- 4 _/_ 7: rotated claw-down. 

- 5 _/_ 7: pulled out the two nails with the claw. 

- 6 _/_ 7: rotated parallel to the table. 

- 7 _/_ 7: placed back on the table. 

`BrushSweep` **(** 7 **stages).** A long-horizon task requiring transitions between two functional brush orientations while sweeping across an extended workspace. _Stages:_ 

- 1 _/_ 7: picked up the brush. 

- 2 _/_ 7: rotated for forward sweeping. 

- 3 _/_ 7: swept the debris forward. 

- 4 _/_ 7: rotated so the bristles face rightward. 

- 5 _/_ 7: swept the debris rightward into the target area. 

- 6 _/_ 7: rotated parallel to the table. 

- 7 _/_ 7: placed back on the table. 

`ScrewdriverUse` **(** 5 **stages).** A precision task that tests axial alignment with the screw and sustained in-hand rotation about the tool axis. _Stages:_ 

- 1 _/_ 5: picked up the screwdriver. 

- 2 _/_ 5: rotate the screwdriver tip downward.. 

- 3 _/_ 5: tightened the screw until fully seated. 

- 4 _/_ 5: rotated the screwdriver for placement. 

- 5 _/_ 5: placed back on the table. 

17 

`BulbReplace` **(** 6 **stages).** A precision insertion task that combines functional in-hand reorientation with bidirectional rotation about the bulb axis. _Stages:_ 

- 1 _/_ 6: picked up the bulb. 

- 2 _/_ 6: rotated to align with the socket. 

- 3 _/_ 6: screwed the bulb in until it lit up. 

- 4 _/_ 6: unscrewed it until fully removed. 

- 5 _/_ 6: rotated for placement. 

- 6 _/_ 6: placed back on the table. 

### **B.2 Autonomous Policy Task Definitions** 

The autonomous Diffusion Policies are evaluated on simplified subsets of three teleoperation tasks, each retaining the most dexterous stages while removing the return-and-place phases. Stage decompositions follow the same protocol as the teleoperation tasks (Sec. B.1); a trial is terminated when an unrecoverable failure occurs. 

`BulbInstall` **(** 4 **stages).** A subset of `BulbReplace` that covers bulb installation only (no unscrewing or return). _Stages:_ 

- 1 _/_ 4: picked up the bulb. 

- 2 _/_ 4: reoriented to the installation pose. 

- 3 _/_ 4: aligned with the socket. 

- 4 _/_ 4: screwed in until the bulb lit up. 

`HammerDriver` **(** 3 **stages).** A simplified variant of `HammerUse` with larger nails and a foam target, retaining the core in-hand rotation to a functional hammering grasp. _Stages:_ 

- 1 _/_ 3: picked up the hammer. 

- 2 _/_ 3: rotated face-down for hammering. 

- 3 _/_ 3: drove the nails into foam. 

`BrushForward` **(** 3 **stages).** A subset of `BrushSweep` that covers a single forward sweep only (no bristle-reorientation or return sweep). _Stages:_ 

- 1 _/_ 3: picked up the brush. 

- 2 _/_ 3: rotated for forward sweeping. 

- 3 _/_ 3: swept forward across the workspace. 

### **B.3 Hardware and Teleoperation System** 

### **B.3.1 Motion Capture System** 

We use a NOKOV optical motion capture system for both offline reference-motion collection and real-time teleoperation, with a different glove configuration for each setting. For offline collection (Fig. 8a), the operator stands in a dedicated capture volume equipped with tripod-mounted infrared cameras and wears a full-coverage glove instrumented with retro-reflective markers on the wrist, palm, and all finger joints (Fig. 8b, left). This dense marker layout enables the system to output, per frame, (i) 24 hand joint 3-D positions, (ii) 21 joint pose matrices, (iii) the wrist SE(3) pose, and (iv) the object’s 6-D pose. For real-time teleoperation, the operator wears a compact glove with markers placed only on the wrist and fingertips (Fig. 8b, right) at the deployment workstation. This lightweight configuration provides the wrist pose and fingertip positions needed by the control loop. The MoCap stream is fed directly into the teleoperation loop at 30 Hz. In both settings, each rigid object is tagged with a marker rigid body that yields its 6-D pose. 

18 





<!-- Start of picture text -->
(a) Motion capture setup.<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) Marker-instrumented gloves.<br><!-- End of picture text -->

Fig. 8: **Hand–object motion capture setup.** (a) The dedicated capture volume equipped with tripod-mounted NOKOV infrared cameras. (b) Two glove configurations: the left glove, used for offline reference-motion collection, has dense markers on the wrist, palm, and all finger joints; the right glove, used for real-time teleoperation, has markers only on the wrist and fingertips. 

### **B.3.2 Teleoperation Interface** 

At runtime, the NOKOV system (Sec. B.3.1) streams the operator’s wrist pose and fingertip positions together with the manipulated object’s 6-D pose at 30 Hz. Each frame triggers two parallel control paths that together close the teleoperation loop at the same rate: 

- **Arm.** The operator’s wrist pose (world frame) is mapped to a 7-DoF Franka FR3 joint target via inverse kinematics. 

- **Hand.** The operator’s fingertip positions and the object’s 6-D pose are converted to the wrist frame and assembled into the co-tracking goal _gt_ . The learned policy then maps the current hand–object state and _gt_ to joint position targets sent to the dexterous-hand SDK via position control. 

The co-tracking policy is trained on in-hand HOI references (Sec. C.6) and does not cover the pregrasp approach. We therefore split each trial into two phases. In the _reaching and grasping phase_ , the hand is driven by kinematic vector retargeting [5, 6], which maps the operator’s fingertip positions to robot joints via vector alignment and handles the pre-grasp approach and initial contact acquisition. Once the hand reaches an approximate grasp pose near the object, the operator switches to the _in-hand phase_ , where the co-tracking policy drives all subsequent in-hand reorientation, regrasping, and finger gaiting. 

## **C TELEDEXTER Implementation Details** 

This section provides the full implementation details of **TELEDEXTER** . We follow the same notation as Sec. 3 unless stated otherwise. 

### **C.1 Observation & Action Space** 

**Observation Space** The observation **_o_** _t_ concatenates the elements listed in Tab. 7 (SharpaWave: _Nf_ = 5, _n_ dof = 22; LeapHand: _Nf_ = 4, _n_ dof = 16). Two design choices are worth highlighting: (i) since every other entry is expressed in _F_ wrist, the gravity direction **_g_** ˆwrist is the _only_ signal that anchors the policy to the world frame and tells it the absolute orientation of the wrist; and (ii) we deliberately exclude joint velocities and contact forces, since both are noisy or unavailable on hardware and the policy can implicitly recover them from the kinematic state, previous action, and gravity cue. 

**Action Space** Extending the residual joint-target parameterization of HORA [27] with a soft deadzone, the policy output **_a_** _t ∈_ [ _−_ 1 _,_ 1]<sup>_n_dof</sup> is converted into a joint command by 



19 

Tab. 7: **Observation** **_o_** _t_ **:** **<u>per-element dimensions.</u>** ˆ _·_ denotes a target quantity; ∆ denotes target _−_ current. 

|Element|Description|Formula|SharpaWave|LeapHand|
|---|---|---|---|---|
|**_q_**_t_|joint positions|_n_dof|22|16|
|cos**_q_**_t_|cosine of joint positions|_n_dof|22|16|
|sin**_q_**_t_|sine of joint positions|_n_dof|22|16|
|**_x_**<sup>_o_</sup><br>_t_|object position in_F_wrist|3|3|3|
|**_q_**<sup>_o_</sup><br>_t_|object quaternion in_F_wrist|4|4|4|
|ˆ**_g_**wrist|gravity direction in_F_wrist|3|3|3|
|ˆ**_p_**<sup>tip</sup><br>_t_|target fingertip positions|3_Nf_|15|12|
|∆ˆ**_p_**<sup>tip</sup><br>_t_|fingertip target_−_current|3_Nf_|15|12|
|ˆ**_x_**<sup>_o_</sup><br>_t_|target object position|3|3|3|
|∆ˆ**_x_**<sup>_o_</sup><br>_t_|object-position target_−_current|3|3|3|
|ˆ**_q_**<sup>_o_</sup><br>_t_|target object quaternion|4|4|4|
|∆ˆ**_q_**<sup>_o_</sup><br>_t_|object-quaternion target_−_current|4|4|4|
|˜**_a_**_t−_1|previous low-level command|_n_dof|22|16|
|**Total**_|_**_o_**_t|_|||**142**|**112**|



with action scale _αa_ = 0 _._ 1, deadzone threshold _τ_ = 0 _._ 1. Under this residual formulation, exactly outputting zero is hard for a Gaussian policy; the deadzone gives an explicit “hold-still” region in action space (any **_a_** _t_ within _±τ_ produces zero delta), letting the policy actively choose to keep the current command rather than having to emit exactly zero. 

### **C.2 Complete Reward Design** 

We give the complete form of the reward used to train the co-tracking controller. The reward couples a sparse _consecutive subgoal-reaching_ term, a dense _tracking_ term, and a small time penalty: 



**Subgoal Indicator** 1 reach( _t_ ) At each step, the active subgoal _gk_ is considered _instantaneously reached_ when all tracking errors fall below their tolerances simultaneously: _e_<sup>pos</sup> _t,k_<sup>_< ϵ_pos,</sup><sup>_ef_</sup> _t,k_<sup>_< ϵ_tip</sup> for every fingertip _f ∈{_ thumb _,_ index _,_ middle _,_ ring _,_ pinky _}_ , and _e_<sup>rot</sup> _t,k_<sup>_< ϵ_rot.The indicator1reach(</sup><sup>_t_)</sup> fires only when this condition is held for _N_ stay consecutive frames, where _N_ stay is resampled after every successful subgoal hit. 

**Step Weighting** _w_ step( _t_ ) After a subgoal _gk_ is hit, the next subgoal is drawn from the same reference trajectory at index _k_<sup>_′_</sup> = _k_ + ∆ _k_ , where the jump ∆ _k ∈_ Z is drawn from a uniform distribution whose range expands over training according to the curriculum (Sec. C.3); _|_ ∆ _k|_ is the number of reference frames skipped between two consecutive subgoals. The step-weighting factor _w_ step scales the sparse bonus by this temporal gap so that larger jumps yield proportionally larger rewards and the policy is not biased toward exploiting trivially close subgoals. When the environment performs a cross-trajectory switch (Sec. C.4), _w_ step is set to a much larger fixed value for the reward computation at that step instead. Both values are listed in Tab. 8. 

**Subgoal Score** _r_ score( _t_ ) The score blends per-fingertip and object tracking terms with fixed weights: 



where the fingertip set _F_ consists of thumb, index, middle, ring, and pinky for SharpaWave, with the ring finger omitted for LeapHand. Each _ρ·_ is an exponential kernel applied to the corresponding tracking error—the per-fingertip distance _e_<sup>_f_</sup> _t,k_<sup>, the object position error</sup><sup>_e_pos</sup> _t,k_<sup>, and the object rotation</sup> error _e_<sup>rot</sup> _t,k_<sup>in radians:</sup> 



20 

Outer scale _αs_ = 1 _._ 5. The remaining blend weights and decay rates _β_ (following Li et al. [23]) are listed in Tab. 8. 

**Dense Tracking** _r_ dense( _t_ ) Following Li et al. [23], a small dense signal shapes early exploration before any subgoal is reached: 



where _I_ = _{_ thumb, index, middle, ring, pinky, lvl1, lvl2 _}_ , with _lvl1_ the MCP (root) knuckles and _lvl2_ the medial (proximal) knuckles, each averaged across fingers, sharing the same exponential kernel form as the per-finger _ρf_ . The (1 _− σt_ ) factor turns the dense object signal off early in training and ramps it in as the curriculum hardens (Sec. C.3). Weight values _wi_<sup>_d_and decay rates</sup><sup>_β_</sup> are listed in Tab. 8; the overall dense-reward scale in Eq. (5) is _α_ dense = 0 _._ 1. 

Tab. 8: **Reward parameters.** Full set of constants used in the reward function (Eq. (5)), grouped by reward component. 

|Parameter|Value|
|---|---|
|_Subgoal indicator_||
|_ϵ_pos (object pos. tolerance)|1cm|
|_ϵ_tip (fingertip tolerance)|3cm|
|_ϵ_rot (object rot. tolerance)|10<sup>_◦_</sup>|
|_N_stay (dwell duration)|_U{_5_,_ 15_}_|
|_Step weighting w_step||
|in-traj|_|_∆_k|_+ 5|
|cross-traj|100|
|_Subgoal score r_score||
|_αs_ (outer scale)<br>_w_<sup>_s_</sup><br>tip <sup>(per-fingertip)</sup><br>_w_<sup>_s_</sup><br>obj <sup>(pos / rot)</sup>|1_._5<br>0_._5<br>2_._0|
|_Time penalty_||
|_c_time|0_._1|



|Parameter||Value|
|---|---|---|
|_Kernel decay rates β_|||
|_β_thumb||100|
|_β_index =_β_middle =_β_ring =|_β_pinky|90|
|_β_lvl1||50|
|_β_lvl2||40|
|_β_pos||80|
|_β_rot (rad)||3|
|_Dense tracking r_dense|||
|_w_<sup>_d_</sup><br>thumb<br>_w_<sup>_d_</sup><br>index <sup>=</sup><sup>_wd_</sup><br>middle <sup>=</sup><sup>_wd_</sup><br>ring|<sup>=</sup><sup>_wd_</sup><br>pinky|1_._0<br>0_._8|
|_w_<sup>_d_</sup><br>lvl1<br>||0_._6|
|_w_<sup>_d_</sup><br>lvl2||0_._4|
|_w_<sup>_d_</sup><br>pos <sup>=</sup><sup>_wd_</sup><br>rot||1_._5|
|_α_dense (outer scale)||0_._1|



**Time Penalty** A constant per-step cost _c_ time = 0 _._ 1 pressures the policy to complete subgoals quickly and prevents it from lingering in locally stable but unproductive configurations. 

### **C.3 Curriculum Schedule** 

Following the curriculum design of Li et al. [23], we progressively harden four difficulty knobs over training. Three of them are jointly controlled by a scalar progress factor _σt_ that decays from 1 to _σ_ min = 0 _._ 7, and simulator gravity follows its own schedule. The four knobs are: 

- **Inter-subgoal step size** (driven by _σt_ ). After each successful subgoal hit (Sec. C.4), the next subgoal is drawn _|_ ∆ _k|_ reference frames ahead, with the upper bound on _|_ ∆ _k|_ growing from 40 frames ( _∼_ 0 _._ 67 s at the 60 Hz reference rate) to _∼_ 80 frames ( _∼_ 1 _._ 33 s) over training. Closer subgoals are easier to reach, so the policy first learns to reach nearby subgoals and only later is asked to reach farther ones. 

- **Action-masking duration** (driven by _σt_ ). The freeze duration of the random action mask (Sec. C.8) is sampled uniformly from _{_ 1 _, . . . , d_<sup>max</sup> _t }_ , with the upper bound _d_<sup>max</sup> _t_ growing from 1 to 10 frames over training. Shorter freezes are easier to tolerate, so the policy first faces brief freezes and only later is exposed to longer ones. 

- **Dense object reward** (driven by _σt_ ). The object-tracking term ( _ρ_ pos + _ρ_ rot) in _r_ dense (Eq. (8)) is scaled by (1 _− σt_ ), growing from zero early on to its full value late, so the policy first learns to track the fingertips and only later learns to track the object pose. 

21 

- **Simulator gravity** (independent schedule). Gravity is annealed linearly from 0 to _−_ 9 _._ 8 m/s<sup>2</sup> over the first 32 K environment frames, so the policy first learns to manipulate under reduced object weight and only later has to support the full deployment load. 

**Schedules** The progress factor _σt_ decays linearly over an annealing window of _Tσ_ = 25 _,_ 600 environment frames (counted per env), where _t_ is the per-env frame counter: 



Each _σt_ -driven upper bound expands cubically toward its saturation value _u_ max from its initial value _u_ min, 



instantiated with ( _u_ min _, u_ max) = (40 _,_ 80) for the inter-subgoal step bound _kt_<sup>max</sup> and (1 _,_ 10) for the action-mask duration bound _d_<sup>max</sup> _t_ . 

### **C.4 Reset Conditions** 

**Goal Reset** Whenever a subgoal _gk_ is hit, the next reference trajectory _τ_ next and subgoal index _k_ next are sampled as 



where _τ_ is the current trajectory, _Do_ is the reference set for the current object _o_ , and ∆ _k_ is drawn from a uniform distribution whose range expands over training according to the curriculum (Sec. C.3). The next subgoal is then read as the _k_ next-th frame of _τ_ next. A cross-trajectory switch swaps the trajectory while preserving the frame index. Its purpose is to train the policy to handle transitions between different demonstrations rather than overfitting to any single one. This generality is required at deployment, where the operator’s motion will not stay within any recorded trajectory. 

**Episode Reset** An episode ends if (i) any joint velocity or object linear or angular velocity exceeds its safety bound, (ii) the object position error exceeds 15 cm, or (iii) the policy accumulates too many out-of-tolerance frames before reaching the next subgoal: 



where “out of tolerance” means _any_ of the five fingertip, object position, or object rotation errors is above threshold, and _η_ fail is the failure-tolerance scale, meaning the policy is allowed _η_ fail outof-tolerance frames per unit of subgoal step before the episode terminates. We use _η_ fail = 1 _._ 5. Immediately after a cross-trajectory switch, _n_<sup>max</sup> fail<sup>is overridden by a flat 300 frames to accommodate</sup> the longer regrasp transition. On termination, the environment is re-initialized via _reference state initialization_ (RSI) [23]: a random frame in the first 90% of the assigned trajectory sets hand DoFs from the retargeted **_q_**<sup>_∗_</sup> and the object pose from the reference. 

### **C.5 Geometry-Aware Retargeting Details** 

We define each loss term in Eq. (4) and specify the two-stage optimization procedure and loss weights below. The main paper provides compact inline definitions of each loss term; here we give the full formulation together with the optimization procedure and hyperparameters. Let _Ht_ denote the robot hand model at frame _t_ with joint configuration **_q_** _t_ and wrist pose ( **_p_**<sup>_w_</sup> _t_<sup>_, R_</sup> _t_<sup>_w_),and</sup><sup>_Ot_the</sup> manipulated object mesh transformed by the recorded object pose _Tt_<sup>_o_.Eachlinkof</sup><sup>_Ht_carriesa</sup> precomputed surface point cloud and, for self-collision, a set of body-attached collision spheres. All signed distances sdf _Ot_ ( _·_ ) from a point on the hand surface to the object (positive outside) are computed with NVIDIA Kaolin [39], which provides a differentiable point-to-mesh SDF used by both _L_<sup>_t_</sup> surf<sup>and</sup><sup>_Lt_</sup> pen<sup>below.</sup> 

22 

**Vector Alignment** _L_<sup>_t_</sup> vec<sup>We use the standard vector-retargeting loss of Qin et al. [5], Handa et al.</sup> [6] without modification: a weighted Huber on per-vector errors between the captured operator hand keypoints (Sec. C.6) and the corresponding robot vectors. We refer readers to the original papers for the exact loss form, keypoint vector set, and per-vector weights. 

**Surface Attraction** _L_<sup>_t_</sup> surf<sup>In the second stage we incorporate the object mesh:points on the hand</sup> surface that fall within a threshold _τ_ surf of the object are pulled onto the surface, 



This glues the contact-side of the hand to the object without forcing non-contacting links onto it. 

**Mesh Interpenetration** _L_<sup>_t_</sup> pen<sup>Asymmetricpenetrationpenaltypullsanyhandsurfacepointthat</sup> has entered the object back out: 



The weights _λ_ pen and _λ_ surf are listed in the optimization paragraph below. 

**Self-Collision** _L_<sup>_t_</sup> col<sup>Self-collisioniscomputedbetweencollisionsphereson</sup><sup>_different_fingers:for</sup> every pair of spheres ( _i, j_ ) with finger indices _f_ ( _i_ ) _̸_ = _f_ ( _j_ ), radii _ri, rj_ and centers **_c_** _i,_ **_c_** _j_ , 



Intra-finger sphere pairs are ignored because adjacent links are designed to touch. 

**Trajectory Smoothness** _L_ smooth We adopt the temporal smoothness energy of Curobo [40] without modification: a log-cosh penalty on the velocity, a squared _ℓ_ 2 penalty on the acceleration, and a squared _ℓ_ 2 penalty on the jerk of the per-frame joint configuration **_q_** _t_ , summed across the trajectory with internal coefficients fixed to the Curobo defaults. 

**Optimization** The two stages are run sequentially per trajectory: 

- **Stage 1 (vector retargeting).** We minimize<sup>�</sup> _t_<sup>_L_</sup> vec<sup>_t_jointlyoverallframes</sup><sup>**_q_**</sup> 1: _T_<sup>withAdam,</sup> using a GPU-batched FK implementation that follows the dex-retargeting design [5]. The learning rate is 10<sup>_−_3</sup> and we run 6 _,_ 000 iterations. This gives a strong but contact-blind initialization. 

- **Stage 2 (geometry-aware post-optimization).** From the Stage 1 solution we minimize the remaining loss terms of Eq. (4) with Adam. The learning rate is 3 _×_ 10<sup>_−_3</sup> , we run 160 iterations, and the gradient norm is clipped to 1 _._ 0. The surface-attraction mask _St_ is built once at the start of Stage 2 with _τ_ surf = 2 and frozen for all iterations. 

We set _λ_ surf = 10, _λ_ pen = 2, _λ_ col = 10, _λ_ smooth = 0 _._ 1 for both SharpaWave and LeapHand. The final per-frame robot configuration **_q_**<sup>_∗_</sup> _t_<sup>,togetherwiththerecordedobjectpose</sup><sup>_T o_</sup> _t_<sup>,formsthe</sup> reference motion consumed by RL. 

### **C.6 Hand–Object Reference Motion Construction** 

For each object, we record 150 reference trajectories of unscripted hand–object interactions using the NOKOV MoCap system (Sec. B.3.1) at 30 Hz. Each trajectory lasts 20 s (600 frames), giving a total of _∼_ 50 minutes of interaction data per object. The interactions span three categories: (1) inhand translation, (2) in-hand rotation, and (3) free-play combining arbitrary grasps, finger gaiting, and tool-use sequences. This diversity ensures the reference set covers the full range of contact modes the controller may encounter at deployment. 

Fig. 9 visualizes short reference-motion clips for `Cylinder` and `Cuboid` , each showing the source MANO hand alongside the retargeted LeapHand and SharpaWave configurations. The retargeted robot hands accurately reproduce the operator’s grasp poses and contact transitions across both embodiments, confirming that the two-stage retargeting pipeline (Sec. C.5) transfers contact-rich interaction structure despite the significant kinematic differences between the human hand and the two robot platforms. 

23 



<!-- Start of picture text -->
Mano Hand<br>Leap Hand<br>Sharpa Wave<br>Mano Hand<br>Leap Hand<br>Sharpa Wave<br><!-- End of picture text -->

### **(a)** _Cylinder_ 



<!-- Start of picture text -->
(b)  Cuboid<br><!-- End of picture text -->

Fig. 9: **Hand–object reference motion visualization.** Retargeted motion clips for (a) `Cylinder` and (b) `Cuboid` . Each clip shows the source MANO hand and the corresponding retargeted LeapHand and SharpaWave sequences. Coordinate axes indicate the object 6-D pose. 

### **C.7 Domain Randomization** 

We randomize hand and object dynamics, external perturbations, sensing noise, and observation latency to tolerate the sim-to-real gap. Each parameter is sampled independently at the start of every episode and held fixed throughout. The implementation of random force perturbation follows VisualDexterity [28]. The full set of ranges is listed in Tab. 9. 

### **C.8 Random Action Masking Details** 

Random action masking is the strong action-space regularizer introduced in Sec. 3.1. It prevents the policy from overfitting to the perfectly synchronized actuation of simulation, which is unrealistic on hardware where actuator compliance, backlash, and PD response vary across DoFs. 

24 

Tab. 9: **Domain randomization ranges.** 

|Group|Parameter|Operation|Range|
|---|---|---|---|
|Hand dynamics|body mass<br>shape friction<br>DoF stiffness_Kp_<br>DoF damping_Kd_|scaling<br>absolute<br>scaling<br>scaling|_U_[0_._9_,_ 1_._2]<br>_U_[1_._0_,_ 4_._0]<br>_U_[0_._8_,_ 1_._2]<br>_U_[0_._8_,_ 1_._2]|
|Object physics|body mass<br>surface friction<br>rolling / torsional friction<br>restitution<br>mesh scale|scaling<br>absolute<br>absolute<br>additive<br>scaling|_U_[0_._5_,_ 2_._0]<br>_U_[0_._5_,_ 4_._0]<br>_U_[0_,_ 0_._05]<br>_U_[0_,_ 1_._0]<br>_U_[0_._95_,_ 1_._05]|
|External force on object|trigger probability per step<br>force scale<br>exponential decay|—<br>constant<br>constant|_U_[0_._01_,_ 0_._25]<br>1_._0<br>0_._99|
|Sensing noise|joint position**_q_**_t_<br>fingertip position<br>object position<br>object orientation|additive Gaussian<br>additive uniform<br>additive uniform<br>additive uniform|_σ_ = 0_._1<br>_±_5mm<br>_±_5mm<br>_±_2<sup>_◦_</sup>|
|Observation latency|queue size<br>queue sampling probability|constant<br>constant|2frames<br>0_._5|
|Initial state|wrist orientation<br>reference frame index|additive<br>uniform|_±_30<sup>_◦_</sup><br>first90%of clip|



**Mechanism** At each environment step, with probability _p_ mask = 0 _._ 15 _and only when no mask is currently active_ , we sample a fresh mask: _nm_ = 3 DoF indices are drawn uniformly without replacement, and a freeze duration _d ∼_ Uniform _{_ 1 _, d_<sup>max</sup> _t }_ is drawn (where _d_<sup>max</sup> _t_ ramps from 1 to 10 following the curriculum schedule in Sec. C.3). For the next _d_ control steps, the executed action **_a_** ˜ _t_ on the masked DoFs is overwritten with the previously commanded action, while the unmasked DoFs receive the current policy output: 



After _d_ steps the mask deactivates, and a new mask can be sampled on the next step. Because the mask refreshes asynchronously across the _∼_ 62 K parallel environments, training sees a wide spectrum of partially-stale joint commands. 

**Sim-to-Real Effect** Random action masking effectively augments the training distribution with desynchronized, partially stale joint commands. The policy is therefore forced to recover useful contact configurations even when some joints respond late or not at all, which closely matches the dominant failure modes we observe on the real hardware (motor lag, backlash, occasional missed commands on the SharpaWave SDK). Empirically, masking is the single most impactful sim-to-real intervention we tested (Tab. 5 in the main paper; further analysis in Sec. A.4). 

### **C.9 RL Training Hyperparameters and Compute** 

Tab. 10 provides the full set of network, PPO, and SAPG-specific hyperparameters used to train the controller. All our controllers are trained on 4 NVIDIA RTX 5090 GPUs running 15 _,_ 600 parallel environments per GPU (62 _,_ 400 environments in total). Each controller is trained for _∼_ 10<sup>10</sup> environment steps in a single RL stage, which takes approximately 1 day on this setup. 

25 

Tab. 10: **Hyperparameters of SAPG.** 

|Hyperparameter|Value|
|---|---|
|_Network_||
|LSTM hidden units|512|
|LSTM Layer Normalization|enabled|
|<br>LSTM sequence length|4|
|<br>MLP hidden sizes|[512_,_ 1024_,_ 1024_,_ 512_,_ 512]|
|Activation|ELU|
|_PPO_||
|Learning rate|2_×_10<sup>_−_4</sup>|
|LR schedule|adaptive|
|KL threshold|0_._008|
|Num opt-epochs|4|
|Minibatch size (per GPU)|31_,_200|
|Horizon length|32|
|Discount (_γ_)|0_._99|
|GAE_λ_|0_._95|
|Clip range (_ϵ_)|0_._2|
|Max grad norm|1_._0|
|Bounds-loss coef.|10<sup>_−_4</sup>|
|Parallel envs (per GPU)|15_,_600|
|_SAPG_||
|Num blocks|6|
|Entropy Bonus Scale|0_._005|
|Off-policy ratio|1_._0|
|Mix ratio|0_._5|



## **D Baseline Implementation Details** 

This section describes how each baseline in Tab. 1 is implemented and what we change relative to the original release. All baselines are deployed on the same hardware platform and share the same teleoperation interface (Sec. B.3). 

**DexRT [5, 6]** We use the open-source dex-retargeting codebase<sup>1</sup> with vector-alignment retargeting. The key parameter is the fingertip scaling factor, set to 1 _._ 0 for SharpaWave and 1 _._ 2 for LeapHand. 

**GeoRT [12]** We follow the original paper and official implementation<sup>2</sup> to train and deploy the neural retargeter. The fingertip workspace data used for training is collected with our own inference glove to match the operator’s hand kinematics at deployment. 

**DexGen [13]** No official implementation is available for DexGen. We re-implement its foundation dexterity controller following the training and deployment recipe described in the original paper. Because the key intermediate step (the AnyGrasp-to-AnyGrasp RL policy) lacks sufficient detail for faithful reproduction, we substitute it with our co-tracking controller to generate the simulation rollouts, matching the data scale reported in the original paper. All subsequent stages (diffusionbased action prior training and deployment) follow the original design. 

**SimToolReal [42]** SimToolReal is not a teleoperation method but an object-centric sim-to-real tooluse policy; we include it as a strong reference for learned dexterous manipulation. We follow the official implementation<sup>3</sup> and re-train on our hardware (Franka FR3 + SharpaWave right hand), adapting the simulation workspace and robot embodiment to match our deployment setup. The three tool categories (hammer, brush, screwdriver) and all other training details follow the original paper. We 

> 1 `https://github.com/dexsuite/dex-retargeting` 

> 2 `https://github.com/facebookresearch/GeoRT` 

> 3 `https://github.com/tylerlum/simtoolreal` 

26 

evaluate both the category-specific variant (SimToolReal<sup>_†_</sup> , one policy per tool) and the all-categories variant (SimToolReal<sup>_‡_</sup> , a single policy across tools), as reported in Tab. 1. 

## **E Autonomous Policy Details** 

We adopt the Conv-UNet Diffusion Policy of Chi et al. [43] (DDPM noise predictor with 1-D temporal convolutions). The policy is conditioned on RGB observations from one third-person and one wrist-mounted camera, each encoded by a separate frozen DINOv2 ViT-S/14 encoder. At each step the policy observes the last _To_ = 2 frames and predicts an action chunk of length _Tp_ = 16. Architecture and training hyperparameters are summarised in Tab. 11. 

Tab. 11: **Diffusion Policy hyperparameters.** 

|Hyperparameter|Value|
|---|---|
|Visual encoder|DINOv2 ViT-S/14, pretrained, frozen|
|Encoder sharing|Separate encoders per camera|
|Image resolution|240_×_320; random crop210_×_280|
|Observation horizon_To_|2|
|Action horizon_Tp_|16<br>|
|Conv-UNet channels|[512_,_ 1024_,_ 2048]|
|Diffusion embedding dim|128|
|Diffusion steps (train)|100|
|Diffusion steps (inference)|16(DDIM)<br>|
|Optimizer|AdamW (_β_1=0_._95,_β_2=0_._999, wd10<sup>_−_6</sup>)<br>|
|Learning rate|10<sup>_−_4</sup>, cosine schedule,500-step warmup|
|Batch size|16|
|Training epochs|300|



27 

