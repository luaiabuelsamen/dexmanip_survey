# **Scaling Cross-Embodiment World Models for Dexterous Manipulation** 

Zihao He<sup>1</sup><sup>_,_2</sup><sup>_∗_</sup> , Bo Ai<sup>1</sup><sup>_,_3</sup><sup>_∗_</sup> , Tongzhou Mu<sup>1</sup> , Yulin Liu<sup>1</sup> , Weikang Wan<sup>1</sup> , Jiawei Fu<sup>1</sup> , Yilun Du<sup>4</sup> , Henrik I. Christensen<sup>1</sup> , and Hao Su<sup>5</sup> 

> 1UC San Diego 2Shanghai Jiao Tong University 3Stanford University 

> 4Harvard University 5Sudo AI GmbH _∗_ Equal contribution 

**https://alan-heoooh.github.io/dexwm.html** 

**_Abstract_ — Cross-embodiment learning seeks to build generalist robots that learn from and operate across diverse morphologies, but differences in kinematics and action spaces hinder data sharing and control transfer. We ask: What structure can be shared across embodiments despite these differences? We argue that the physical interactions they induce can be modeled in a shared geometric space, allowing world models to provide a common interface for learning and control. To realize this idea, we represent human and robot hands as sets of 3D particles and define actions as end-effector particle displacement fields. This representation abstracts away embodiment-specific joint spaces while preserving the geometry and motion relevant to physical interaction. We train a graph-based world model on random interaction data from diverse simulated robot hands and real human hands, and integrate it with model-predictive control for deployment on new hardware. Experiments on rigid and deformable manipulation reveal three findings: increasing the diversity of training embodiments improves generalization to unseen hands; appropriately combining simulated and realworld data outperforms either source alone; and the same learned model enables effective control on robotic hands with distinct kinematics and degrees of freedom. These results position particle-based world models as a shared interface for learning from and for heterogeneous embodiments.** 

## I. INTRODUCTION 

Cross-embodiment learning seeks to build generalist robots that learn from and operate across diverse physical embodiments. Yet every embodiment expresses action through a different kinematic structure and control space, fragmenting interaction data and preventing direct transfer. This challenge is becoming increasingly important as largescale robot deployments produce heterogeneous datasets across robot platforms and hardware generations [27, 11]. Prior progress has shown embodiment-level generalization in locomotion [3] and in manipulation with parallel grippers [4, 22, 51, 28, 14, 31], whereas dexterous manipulation has largely been limited to grasping [49, 10] and in-hand reorientation [30]. Extending cross-embodiment learning to non-prehensile and deformable-object manipulation remains challenging because these tasks require both reasoning about complex object dynamics and fine-grained contact control. 

Dexterous hands offer a compelling case for crossembodiment learning. Despite the challenge of contact-rich, high-DoF control, multifingered robot hands are morphologically similar to one another and to human hands. This anthropomorphism suggests that cross-embodiment datasets, including not only robot datasets but also human–object 

interactions, can be mutually informative. This raises two central questions: what _invariant knowledge_ about the external world and contact interactions underlies purposeful action across distinct kinematics and control spaces, and how should state and action be _represented_ so that human and robot data become jointly useful? Our key insight is that joint-space actions are embodiment-specific, but the physical interactions they induce can be modeled in a shared geometric space. We argue that world models [1, 44], which predict how physical states evolve under action, can provide a common interface for learning and control in this space. The central challenge is therefore to design shared state and action representations that abstract away embodimentspecific details while preserving the geometry and motion that govern physical interaction, allowing a single predictive model to learn from heterogeneous data and enable modelbased control across diverse kinematic structures. 

To this end, we represent both human and robot hands as _particles_ (i.e., 3D point sets), with actions defined as particle displacements. A graph-based dynamics model [40, 2, 41, 42, 56] predicts particle motion while exploiting spatial locality and equivariance. We co-train the model on simulated robot–object interaction data and real human–object interaction data and study how generalization of the learned model scales with the morphological diversity in the training domain. For control, we sample robot joint actions, which are then converted to particle action representation via forward kinematics, to enable model-predictive control in the particle space. This action abstraction unifies control problems across embodiments, allowing the learned model to be deployed on hands with varied control spaces without motion retargeting or expert demonstration collection. 

We evaluate learned world models both in simulation and on real hardware. In simulation, we observe an _embodiment scaling_ trend [3]: training on more simulated hands consistently improves generalization to unseen embodiments. In the real world, we find that models trained solely on human data can already transfer to robotic hands despite the embodiment gap, and that incorporating an appropriate amount of simulation data further improves both predictive accuracy and planning performance. Our best model, cotrained on simulated robot data and real human data, enables a 6-DoF PSYONIC Ability Hand and a 12-DoF Robot Era XHand to successfully perform deformable object manipula- 

tion. These results demonstrate the promise of world models as a unifying interface for cross-embodiment learning and generalization in robot manipulation. 

## II. RELATED WORKS 

## _A. Cross-Embodiment Learning_ 

One key goal of cross-embodiment learning is to learn from diverse embodiments, with learning from human data being a special case. Most existing approaches are modelfree, which learn mappings from observations to actions endto-end via reinforcement learning (RL) or behavior cloning (BC). Prior work includes using human demonstrations to guide RL for dexterous manipulation [34, 6], crossembodiment RL training for locomotion [5], and scaling to many embodiments through a combination of RL and BC [3, 30]. When high-quality demonstrations are available, BC can provide stable learning signals [32, 20]. Human demonstrations can also be adapted to robots via motion retargeting for anthropomorphic robots [35]. These works either require extensive RL training in simulation, limited to domains where the sim-to-real gap is moderate, or require expert demonstrations in the real world. 

Model-based approaches instead learn world models that explicitly predict action outcomes and have demonstrated strong performance on tasks requiring fine-grained control [1]. Prior work learns particle-based dynamics from human–object interactions but uses the model only to guide RL exploration [17], while concurrent PointWorld represents parallel-jaw gripper actions as 3D point flows and learns scene dynamics from large-scale robotic manipulation data [18]. In contrast, we study world-model scaling across articulated human and robotic hands, jointly leveraging simulated robot interactions and real human data to enable direct model-predictive control of hands with distinct kinematics and degrees of freedom for dexterous manipulation tasks. 

## _B. World Model Learning for Robotic Manipulation_ 

World models, predictive models that forecast the effects of actions, are central to model-based robotic control [1]. Their effectiveness depends heavily on state representation. Pixel-based models [9, 55, 8] can exploit large-scale visual data but struggle to produce physically accurate predictions in contact-rich settings with extensive training. Particlebased models are more physically grounded and incorporate stronger inductive biases. They have enabled manipulation of clothes [25, 45], ropes [57], granular object piles [48], and plasticine [41, 40], but are often trained on singleembodiment data from parallel jaw grippers. This work seeks to establish particle-based world models for complex dexterous manipulation and position them as a paradigm for cross-embodiment learning. 

## _C. Dexterous Manipulation_ 

Dexterous manipulation is a long-standing challenge in robotics [37, 26], largely due to the high degrees of freedom of multi-fingered hands and complex contact patterns. Classic control methods rely on analytical object models [36, 43, 

29], which may not capture hard-to-model factors, such as frictional contact or actuator drift, and can be hard to obtain for deformable objects. Recent learning-based approaches, including RL and BC, have shown success in rigid object manipulation, such as grasping [47, 10], in-hand reorientation [15, 33], and tool use [39, 46, 13]. However, manipulating deformable objects using multi-fingered hands remains under-explored [23, 59], due to the combined challenges of high-dimensional control and complex object dynamics. In this work, we learn a model of environment dynamics and integrate it with model-predictive control. By introducing embodiment-agnostic state and action representations, we enable learning from both robotic and human data, allowing a single model to operate over diverse dexterous hands. 

## III. METHOD 

Our goal is to enable dexterous manipulation skills from and for diverse robotic hands. We formalize the general problem as follows. At each time step _t_ , the end effector is in configuration _qt ∈_ R<sup>_ne_</sup> , where _ne_ is the number of degrees of freedom of embodiment _e_ , and the object is in state _sobj_ . The world state includes the state of both the robot and the object, _st_ = _⟨qt, sobj⟩_ . The robot takes an action _ut_ , and the world transits to a new state _st_ +1. The objective is to find an action sequence of length _H_ , _u_ 0: _H−_ 1, that minimizes a cost function _J_ : 



where _T_ ( _s_ 0 _, u_ 0: _H−_ 1) is the state reached after applying the sequence to the dynamics, and _sg_ is the target state. 

What is the shared underlying process across different embodiments for these control problems? Our key insight is that the underlying physical interaction process, captured by _T_ , is universal. However, approximating _T_ is challenging due to the varying dimensions of the robot configuration _qt ∈_ R<sup>_ne_</sup> and action _ut ∈_ R<sup>_ne_</sup> , which depend on the embodiment _e_ , as well as the differences in kinematic and geometric structures that shape the environment dynamics. Therefore, we aim to unify state and action representations to learn embodiment-agnostic world models, which hold the potential to scale with cross-embodiment datasets. 

We next discuss the high-level framework of crossembodiment model learning and planning (Section III-A), state estimation (Section III-B), world model architecture (Section III-C), and model-based control (Section III-D). 

## _A. Cross-Embodiment World Model Learning and Planning_ 

We define a **particle state and action space** that unifies cross-embodiment data format and control problems. For embodiment _e_ , we represent the end-effector at time _t_ by a set of _Ne_ particles, _Xt_<sup>(</sup><sup>_e_)</sup> = _{ x_<sup>(</sup> _i,t_<sup>_e_)</sup><sup>_∈_R3</sup><sup>_}_</sup> _i_<sup>_N_</sup> =1<sup>_e_,theobjectby</sup> _No_ particles _Xt_<sup>(</sup><sup>_o_)</sup> = _{ xi,t ∈_ R<sup>3</sup> _}_<sup>_N_</sup> _i_ =1<sup>_o_,andthustheworld</sup> state is represented as _Xt_ = ( _Xt_<sup>(</sup><sup>_e_)</sup> _, Xt_<sup>(</sup><sup>_o_)</sup> ). This is a unified particle-based representation applicable to nearly arbitrary end effector (e.g., multi-fingered hands with different DoFs) and objects (e.g., rigid and deformable objects). 



<!-- Start of picture text -->
(a) Cross-Embodiment World Model Learning (b) Model-Predictive Control<br>Diverse Embodiments and Action Spaces  𝑠𝑔𝑜𝑎𝑙<br>Novel  XHand<br>Ability Hand  Allegro Hand Shadow Hand Human Hand Embodiment (12-DoF)<br>(6-DoF) (16-DoF) (24-DoF) (N-DoF)<br>/ Sample Actions<br>…<br>…<br>Point Sampling<br>Fingers Thumb Palm<br>Unified Particle-Based State & Action Space<br>Pinch Pinch Press<br>… …<br>𝑠𝑡 = ⟨ Robot State Object State ⟩ 𝑎𝑡 = ⟨ Action ⟩<br>Unified World Model<br>Unified World Model<br>𝑠𝑡+1 Object State<br><!-- End of picture text -->

**Fig. 1: Overall framework** . Our key idea is to represent both embodiments and objects as 3D particles, and actions as end-effector particle displacement fields. These state–action abstractions unify data and control across embodiments. (a) We train world models on random interaction data from diverse robot hands in simulation and from human demonstrations in the real world. (b) At deployment, joint action samples are mapped into displacement fields via forward kinematics, rolled out by the world model for prediction, and the optimal trajectory is executed on the target hardware. We illustrate a planning horizon of 1 here for simplicity. 

In the particle space, the action can be defined as the endeffector particle displacement field: 



and 



For planning, we obtain particle representations from joint states via forward kinematics (FK). Let Φ _e_ : R<sup>_ne_</sup> _→_ (R<sup>3</sup> )<sup>_Ne_</sup> denote the FK mapping for embodiment _e_ . Given the current and next joint states, _qt_ and _qt_ +1 = _qt_ + _ut_ , the corresponding particle sets are 



Planning and learning therefore operate in the embodiment-agnostic state space _S_<sup>_P_</sup> = (R<sup>3</sup> )<sup>_Ne_</sup> _×_ (R<sup>3</sup> )<sup>_No_</sup> and action space _A_<sup>_P_</sup> = (R<sup>3</sup> )<sup>_Ne_</sup> _._ This abstraction enables training on data from diverse embodiments and deployment across different hardware without assumptions about the underlying kinematic structure (e.g., degrees of freedom). The only requirement is a forward kinematics model to map joint actions into the particle action space for model inference, which is standard and trivial since robot kinematics are known at deployment. We illustrate the overall framework in Figure 1. 

## _B. Perception Module_ 

The perception module performs state estimation for data collection and deployment. We use a multi-view camera setup following prior work [2, 40, 41, 45]. Cameras are placed at fixed positions around the scene for comprehensive viewpoint coverage. 

For human data collection, we reconstruct hand meshes from multi-view images using POEM-v2 [54] and sample particles with farthest point sampling (FPS). For deformable object perception, we fuse multi-view point clouds, perform Poisson surface reconstruction to obtain a smooth surface [21], and apply FPS. For rigid bodies, we estimate object poses using FoundationPose [50] and sample surface particles via FPS. Background is excluded from the scene. 

During deployment, the robot’s state is available from proprioception, and only object perception is required. We apply the same object perception procedure as in data collection. 

## _C. World Model Architecture_ 

We consider adopting graph neural networks (GNNs) as our world model architecture, as the locality and equivariance are useful inductive biases [19] that allow the learned model to generalize to objects and hands with different shapes. We use DPI-Net [24], a GNN that models local particle interactions through message passing and captures global effects via multi-step hierarchical propagation. 

Specifically, the graph state at each time step is represented as the tuple _⟨Xt, Et⟩_ with _Xt_ as vertices and _Et_ as edges constructed with a radius graph. For each particle in the graph, _ot,i_ = _⟨xi,t, c_<sup>_o_</sup> _i,t_<sup>_⟩_,where</sup><sup>_xi,t_istheparticleposition</sup> _i_ at time _t_ , and _c_<sup>_o_</sup> _i,t_<sup>istheparticle’sattributesattimet,</sup> including the group information (e.g., point belongs to robot or object). In addition, edges between particles are denoted as _ek_ = _⟨uk, vk⟩_ , where 1 _≤ uk, vk ≤|Ot|_ are the receiver and sender particle indices respectively. Given the graph, where particles are connected only within a certain radius, we can first use node encoder _fO_<sup>_enc_</sup> and edge encoder _fE_<sup>_enc_</sup> to extract node and edge features: 



where _d_<sup>_r_</sup> _k_<sup>denotesedge’sattributes(e.g.length).Then,the</sup> features are propagated through edges in multiple steps. Denote _ϵ_<sup>_l_</sup> _k,t_<sup>and</sup><sup>_h_</sup> _i,t_<sup>_l_arepropagatinginfluencefromedge</sup> _k_ and node _i_ at step _l_ , respectively. At step 0, initialize _h_<sup>0</sup> _i,t_<sup>= 0</sup><sup>_, i_= 1</sup><sup>_...|O|_.Foreachstep1</sup><sup>_≤l ≤L_:</sup> 



where _Ni_ is the neighbor index set of particle _i_ , _fO_ denotes the node propagator, and _fE_ denotes the edge propagator. Then the future state at time _t_ + 1 is predicted as 



The particle-based graph network incorporates strong inductive biases. Spatial locality is enforced by restricting message passing to local neighborhoods, analogous to shortrange force interactions between particles in physics. Equivariance is achieved through relative coordinates and shared update functions, ensuring invariance to global translations, rotations, and particle permutations. These properties support generalization across embodiments. The model is trained with a supervised objective: 

_L_ ( _Ot, O_<sup>ˆ</sup> _t_ ) = _ℓ_ ( _Ot, O_<sup>ˆ</sup> _t_ ) _,_ (3) 

where _ℓ_ denotes the loss function. In simulation, mean squared error (MSE) can be used when temporal point-level correspondence is available, while Chamfer Distance (CD) or Earth Mover’s Distance (EMD) can be applied for unpaired point sets. Thus, the learning objective is broadly applicable. 

## _D. Model-Based Planning_ 

Given learned world models, we use sampling-based model-predictive control to search for optimal trajectories 

for execution. We devise motion primitives for efficient joint action sampling, inspired by the insight that human hand motions lie in low-dimensional manifolds of the full configuration space [12]. 

For the _Object Pushing_ task, we constrain pushing actions to a fixed _x_ – _y_ plane. Global translations are sampled as random motion noise in the end-effector frame. Specifically, we first sample a straight-line trajectory in the end-effector frame and then perturb it with Gaussian noise to obtain the final action. The number of fingers making contact with the box is randomly selected. 

For the _Plasticine Reshaping_ task, we sample joint actions from the following motion primitives, which capture a useful subset of the joint action space: (i) FingersPinch, involving rotation about the _z_ -axis and relative motion between the index finger and thumb; (ii) PalmPress, characterized by rotation about the _z_ -axis and translation along the _z_ -axis; (iii) ThumbPinch, composed of rotation about the _z_ -axis and actuation of thumb-specific degrees of freedom. 

For model-based control, we map sampled joint actions _{ut}_<sup>_H_</sup> _t_ =0<sup>_−_1</sup> to particles in the shared state space through forward kinematics, rolled out with the learned world model, and evaluated using the cost function. The target is specified as a point cloud following prior work [1, 2, 40], and the cost function is defined as a combination of CD and EMD, consistent with the training objective Eqn 3, i.e., 

_J_ ( _X, G_ ) = _L_ CD( _X, G_ ) + _L_ EMD( _X, G_ ) 

where _X_ = _{xi}_<sup>_N_</sup> _i_ =1<sup>denotesthepredictedparticlepoint</sup> cloud, and _G_ = _{gi}_<sup>_N_</sup> _i_ =1<sup>denotesthetargetpointcloud.</sup> 

## IV. EXPERIMENTS 

In this section, we study the following questions: 

- **Q1.** Does cross-embodiment training of the world model improve generalization on unseen embodiments? 

- **Q2.** What is the co-training recipe to leverage simulation and real-world data? 

- **Q3.** Does the learned dynamics model enable effective planning for dexterous manipulation? 

Our study proceeds in three stages. First, we investigate cross-embodiment scaling entirely in simulation ( **Q1** ), which provides a clean and controlled environment for studying scaling behaviors. Second, to bridge the sim-to-real gap and capture realistic contact dynamics, we incorporate real human data, and study the training recipe to best leverage the simulation robot data and real human data ( **Q2** ). Finally, we evaluate the trained world models on real robot hardware to assess their quality at the system level ( **Q3** ). 

## _A. Experimental Setup_ 

**Task setup.** We consider two representative dexterous manipulation tasks: non-prehensile rigid object pushing [2, 7] and deformable object reshaping [2, 40, 41]. In _Object Pushing_ , the goal is to reorient a box to a target orientation. In _Plasticine Reshaping_ , the goal is to mold plasticine into a target shape. The targets are specified as point cloud observations, following [40, 2]. Both tasks require reasoning about object dynamics and precise contact control. 



**Fig. 2: Scaling trends in cross-embodiment world model learning.** For each target hand, models are trained on subsets of the remaining hands of varying sizes. All subset combinations at a given size are enumerated (e.g., �25� for size 2), and the mean performance with 95% confidence intervals is reported. Dashed lines indicate models directly trained on the target embodiment. “Equal data” refers to training directly on the target embodiment using the same number of samples as the total data aggregated across all source hands. Across both tasks, our model exhibits a embodiment scaling trend: increasing the number of training embodiments consistently lowers prediction error, and with five source embodiments (zero-shot) it often matches or surpasses target-only training while Point Transformer (PT) [58] shows weaker and less consistent gains, potentially due to the lack of inductive bias. 



<!-- Start of picture text -->
Allegro Hand LEAP Hand Shadow Hand … XHand Ability Hand<br>Object Pushing …<br>Object  …<br>Reshaping<br>(a) Simulation Setup (b) Real-World Setup<br><!-- End of picture text -->

**Fig. 3: Cross-embodiment setups in simulation and the real world.** We have multiple robotic hands in simulation for collecting random interaction data, and two real hardware mounted on a UFACTORY XArm 7 for system deployment. 

**Model implementation.** For _Plasticine Reshaping_ , we represent the object using 300 particles and the hand using 200 particles. We construct radius graphs with an inner radius of 0.025 m and an outer radius of 0.04 m [41]. For _Object Pushing_ , we represent the object using 100 particles and the hand using 50 particles, with both radii set to 0.04 m. We use a higher particle density for _Plasticine Reshaping_ to capture finer-grained local contact patterns. 

At each MPC iteration, we sample 500 candidate action sequences with a planning horizon of 4 steps and perform 10 optimization iterations. We execute the first 2 action steps before replanning. On a workstation equipped with an RTX 4090 GPU, each planning update takes approximately 60 s. 

**Baseline.** We adapt the Point Transformer (PT) [58] as an alternative architecture for modeling particle dynamics. Unlike DPI-Net, which uses structured message passing, PT models interactions among particles using an attention mechanism. PT and DPI-Net share the same input and output formats and are trained on the same data using the same loss functions to ensure a fair comparison. Because we collect only random interaction data, we exclude approaches that require expert demonstrations [7, 31, 16]. 

**Simulation setup.** We simulate six dexterous hands representative of commonly used multi-fingered designs: Ability Hand (6-DoF), Allegro Hand (16-DoF), XHand (12DoF), Leap Hand (16-DoF) [38], Shadow Hand (24-DoF), and a URDF variant of the Shadow Hand without its forearm (24-DoF). For the rigid-body task ( _Object Pushing_ ), we use SAPIEN [52] for data collection. For deformable object manipulation, we use the Rewarped simulation platform [53], a differentiable multiphysics simulator. We collect 100 trajectories per task for each robots, where the robots perform random actions in the predefined action space. 

**Real-world setup.** Our hardware platform consists of a 7-DoF XArm robot equipped with an Ability Hand and an XHand. Four Intel RealSense cameras provide multi-view perception, following prior work [40, 41, 2]. The system is controlled via a workstation with an NVIDIA RTX 4090 GPU. For human demonstration data, we collect 30 minutes of demonstrations for ThumbPinch, FingersPinch, and PalmPress each. The simulation and real-world hardware setup are illustrated in Figure 3. 

## _B. Evaluating Cross-Embodiment World Model Learning_ 

We systematically evaluate how the number of training embodiments influences generalization to unseen embodiments. For each target hand, we hold it out and train on _x_ other hands, enumerating all � _Nx_ � subsets from _N_ = 6 total hands. The mean squared error (MSE) on the unseen hand serves as the generalization metric. We report results for both our method and a Point Transformer (PT) [58] baseline trained under the same subset protocol and data budget. In addition, the case _x_ = 6 corresponds to training on all hands, including the target, and provides a reference for the upper bound of cross-embodiment learning in the current data regime. Results are shown in Figure 2. 



<!-- Start of picture text -->
time Result Target<br>(a)<br>(b)<br><!-- End of picture text -->

**Fig. 4: Qualitative results of cross-embodiment deployment** . (a) Ability Hand (6-DoF) and (b) XHand (12-DoF) utilize the same particle-space dynamics model learned from human demonstration. For each trial, the hand successfully reshapes the deformable clay toward the target shape using a combination of FingersPinch, PalmPress, and ThumbPinch skills. 



**Fig. 5: Evaluating training recipes for bridging simulation and real.** We compare co-training with different mixtures of simulation and real-world data. Legend values indicate the amount of simulation data relative to a fixed quantity of real human data. The y-axis shows prediction error on held-out human interactions, with error bars denoting 95% confidence intervals. Here, “CD+EMD” denotes an equally weighted sum (CD+EMD, 1:1). We adopt CD/EMD since the real-world data lacks temporal point-level correspondence. 

**Key observations.** We make the following observations: 

- _Embodiment scaling law [3]:_ Prediction error decreases as more embodiments are included, and variance across subsets shrinks, indicating more stable models with broader embodiment diversity for our GNN. In contrast, PT [58] shows weaker and less consistent improvements as _x_ increases, suggesting that the inductive bias in GNN contributes to the cross-embodiment transfer. 

- _Zero-shot strength at x_ =5 _:_ With five training embodiments (no target data), the performance of GNN often approaches or surpasses training directly on the target hand. This shows that diverse cross-embodiment data can substitute for target-specific data when deploying to a new hand. This opens up the possibility of building cross-embodiment generalist world models that can broadly zero-shot transfer to novel ones via large-scale cross-embodiment training. 

- _Benefit of co-training at x_ =6<sup>_∗_</sup> _:_ Even when target data is available, adding the other embodiments yields fur- 

ther gains over target-only training. Our proposed state and action representations unify data from heterogeneous embodiments and make such co-training possible; PT [58] benefits less from co-training, consistent with its higher sensitivity to which training subset is used. 

**Task-specific differences.** Errors are generally lower for deformable reshaping, as deformations are spatially localized, whereas rigid-body rotations move particles over a much larger scale. At the same time, the scaling effect is more pronounced in deformable manipulation. We hypothesize this is because deformable tasks involve larger contact surfaces, making end-effector geometry more influential. Exposure to diverse embodiments therefore provides richer coverage of contact geometries and interaction patterns, which aids generalization. By contrast, rigid pushing often depends on a small number of contact points, where crossembodiment differences are less critical. These results suggest that our approach is particularly beneficial for tasks with complex contact dynamics, as in _Plasticine Reshaping_ . 

**Embodiment-specific trends.** Certain hands (e.g., Shadow Hand, Leap Hand) show sharp improvements when scaling from 4 to 5 training embodiments, whereas smaller hands (e.g., Ability Hand) achieve competitive performance earlier. We hypothesize that this effect is linked to graph density in the particle–graph representation used by our GNN-based world model. Smaller hands have fewer degrees of freedom but a more compact geometry, which results in denser particle connections under the radius-graph construction. This denser connectivity provides richer local message passing and allows the GNN to propagate interaction information more effectively, even when trained on fewer embodiments. By contrast, larger hands span a larger spatial extent, yielding sparser graphs where local neighborhoods capture fewer interactions. In such cases, broader embodiment diversity is needed to expose the model to sufficient variations in contact patterns and fill in the missing structural information. This suggests that the scaling benefits of adding more training embodiments 

|Hand Type|Method|Metric|Letter X|Letter R|Letter T|Letter A|Aggregated|
|---|---|---|---|---|---|---|---|
|||CD _×_10<sup>_−_3</sup> _↓_<br>|6.85 _±_ 0.21|6.92 _±_ 0.10|6.88 _±_ 0.19|7.14 _±_ 0.14|**6.95** _±_ **0.10**|
||**Co-train**|EMD _×_10<sup>_−_3</sup> _↓_|4.76 _±_ 0.17|4.90 _±_ 0.35|4.94 _±_ 0.27|5.10 _±_ 0.18|**4.92** _±_ **0.13**|
|Ability Hand||Success Rate _↑_|5 / 5|4 / 5|5 / 5|4 / 5|**18 / 20**|
|||CD _×_10<sup>_−_3</sup> _↓_<br>|7.21 _±_ 0.55|7.20 _±_ 0.15|6.94 _±_ 0.14|7.26 _±_ 0.14|7.15 _±_ 0.16|
||Human-only|EMD _×_10<sup>_−_3</sup> _↓_|5.07 _±_ 0.67|5.38 _±_ 0.39|5.08 _±_ 0.25|5.40 _±_ 0.36|5.23 _±_ 0.23|
|||Success Rate _↑_|3 / 5|2 / 5|4 / 5|1 / 5|10 / 20|
|||CD _×_10<sup>_−_3</sup> _↓_|6.65 _±_ 0.26|6.70 _±_ 0.11|6.99 _±_ 0.17|7.05 _±_ 0.20|**6.85** _±_ **0.12**|
||**Co-train**|EMD _×_10<sup>_−_3</sup> _↓_|4.52 _±_ 0.29|4.65 _±_ 0.17|4.90 _±_ 0.21|5.07 _±_ 0.23|**4.78** _±_ **0.14**|
|XHand||Success Rate _↑_|5 / 5|5 / 5|4 / 5|3 / 5|**17 / 20**|
|||CD _×_10<sup>_−_3</sup> _↓_|6.82 _±_ 0.30|7.22 _±_ 0.27|7.32 _±_ 0.31|7.53 _±_ 0.32|7.22 _±_ 0.18|
||Human-only|EMD _×_10<sup>_−_3</sup> _↓_|4.66 _±_ 0.44|5.26 _±_ 0.31|5.37 _±_ 0.29|5.43 _±_ 0.33|5.18 _±_ 0.21|
|||Success Rate _↑_|4 / 5|2 / 5|2 / 5|1 / 5|9 / 20|



**TABLE I: Quantitative results of cross-embodiment deployment on Plasticine Reshaping task.** Real-world performance comparison of co-training (human + 6 simulated robot hands) vs. training on only human data, evaluated on Ability Hand and XHand. Columns correspond to target letter X/R/T/A settings. Reported values are mean _±_ 95% confidence interval. 

are not uniform across morphologies, but depend on the intrinsic graph density of each hand’s particle representation. We believe developing model architectures that are less sensitive to graph densities is an interesting future direction. 

## _C. Co-Training Recipe_ 

Having established positive embodiment scaling in simulation, we next study how to leverage simulation data for real-world learning. Simulation offers uniform sensing and abundant interactions, but models trained purely in simulation can overfit to simulator-specific artifacts such as contact or material mismatches. Conversely, real-world human data avoids the reality gap but introduces an embodiment gap relative to robot hands. We hypothesize that co-training on both domains may combine their complementary strengths, when the signals from each are balanced appropriately. 

We train models with different mixtures of simulation and real-world data, and evaluate them on held-out real human data (Figure 5). Simulation-only training yields the highest prediction error, highlighting the sim-to-real gap. Humanonly training provides a stronger baseline, and mixing simulation with human data further reduces error when the ratio is well balanced. Notably, a 1:1 ratio performs best across tasks, suggesting that simulation data can act as a useful regularizer for human data rather than a substitute. 

## _D. Evaluating Model-Based Control_ 

For real-world deployment, we focus on the more challenging task _Plasticine Reshaping_ , which has complex contact dynamics. We compare two models: one trained on human data only and the best-performing co-training model. Each model is evaluated across four target shapes (“X”, “R”, “T”, “A”), with five trials per shape, for a total of 20 runs. We report CD, EMD, and success rates, where success is defined as achieving an error lower than 0.0125 for CD + EMD loss. Quantitative results are reported in Table I. The human-only model achieves zero-shot transfer to novel robot hands by leveraging the unified state and action space, but its performance is lower than that of the co-training model due to the lack of embodiment diversity in the training data. On Ability Hand, co-training achieves 

18 _/_ 20 successes, while the human-only model reaches only 10 _/_ 20 successes. The improvement is especially visible on letters A and R where human-only struggles. On XHand, cotraining similarly attains 17 _/_ 20 successes, compared to 9 _/_ 20 for human-only. Co-training is robust across targets (notably R and X at 5 _/_ 5 each), whereas human-only is much more target-dependent. 

Qualitative results of the co-training model are shown in Figure 4. Both the _(a)_ Ability Hand and _(b)_ XHand successfully reshape clay into target letters by composing the three predefined motion skills, ThumbPinch, FingersPinch, and PalmPress, to carve, spread, and compress. Despite their kinematic differences, the same particle-based dynamics model enables model-predictive planning on both hands without fine-tuning, demonstrating effective crossembodiment deployment. 

## V. CONCLUSION & DISCUSSION 

This work positions world models as a shared interface for learning and control across embodiments. By representing heterogeneous hands and their actions in a unified particle space, we train a single dynamics model from simulated robot interactions and real human interactions and deploy it for model-predictive control on distinct robotic hands. Our experiments show that prediction and control improve as the diversity of training embodiments increases, and that appropriately combining simulation and real-world data outperforms either source alone. Together, these results suggest that the transferable structure across embodiments lies not in their joint spaces, but in the physical interactions they induce in the world. World models that capture this shared structure therefore offer a promising path toward generalist systems that learn from heterogeneous embodiments and control new ones without embodiment-specific policy training. 

## REFERENCES 

> [1] Bo Ai et al. “A Review of Learning-Based Dynamics Models for Robotic Manipulation”. In: _Science Robotics_ (2025). 

> [2] Bo Ai et al. “RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing”. In: _Robotics: Science and Systems_ . 2024. 

- [3] Bo Ai et al. “Towards Embodiment Scaling Laws in Robot Locomotion”. In: _CoRL_ (2025). 

- [4] Kevin Black et al. “ _π_ 0: A Vision-Language-Action Flow Model for General Robot Control”. In: _arXiv preprint arXiv:2410.24164_ (2024). 

- [5] Nico Bohlinger et al. “One Policy to Run Them All: an Endto-end Learning Approach to Multi-Embodiment Locomotion”. In: _Conference on Robot Learning_ (2024). 

- [6] Zerui Chen et al. “Vividex: Learning vision-based dexterous manipulation from human videos”. In: _arXiv preprint arXiv:2404.15709_ (2024). 

- [7] Cheng Chi et al. “Diffusion policy: Visuomotor policy learning via action diffusion”. In: _The International Journal of Robotics Research_ (2024). 

- [8] Yilun Du et al. “Learning universal policies via text-guided video generation”. In: _NeurIPS_ (2023). 

- [9] Frederik Ebert et al. “Visual foresight: Model-based deep reinforcement learning for vision-based robotic control”. In: _arXiv:1812.00568_ (2018). 

- [10] Hao-Shu Fang et al. “AnyDexGrasp: General Dexterous Grasping for Different Hands with Human-level Learning Efficiency”. In: _arXiv preprint arXiv:2502.16420_ (2025). 

- [11] Hao-Shu Fang et al. “RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot”. In: _ICRA_ . 2024, pp. 653–660. 

- [12] Thomas Feix et al. “The GRASP Taxonomy of Human Grasp Types”. In: _IEEE Trans. Hum. Mach. Syst._ 46.1 (2016), pp. 66–77. 

- [13] Ying Feng et al. “Learning Dexterous Manipulation with Quantized Hand State”. In: _arXiv preprint arXiv:2509.17450_ (2025). 

- [14] Shresth Grover et al. “Enhancing generalization in vision-languageaction models by preserving pretrained representations”. In: _arXiv preprint arXiv:2509.11417_ (2025). 

- [15] Ankur Handa et al. “Dextreme: Transfer of agile in-hand manipulation from simulation to reality”. In: _ICRA_ . 2023, pp. 5977–5984. 

- [16] Zihao He et al. “FoAR: Force-Aware Reactive Policy for ContactRich Robotic Manipulation”. In: _IEEE Robotics and Automation Letters_ 10.6 (2025), pp. 5625–5632. 

- [17] Zhengdong Hong et al. “Learning Particle-Based World Model from Human for Robot Dexterous Manipulation”. In: _3rd RSS Workshop on Dexterous Manipulation: Learning and Control with Diverse Data_ . 2025. 

- [18] Wenlong Huang et al. “PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation”. In: _arXiv preprint arXiv:2601.03782_ (2026). 

- [19] Leslie Pack Kaelbling. “The foundation of efficient robot learning”. In: _Science_ 369.6506 (2020), pp. 915–916. 

- [20] Simar Kareer et al. “Emergence of Human to Robot Transfer in Vision-Language-Action Models”. In: _arXiv preprint arXiv:2512.22414_ (2025). 

- [21] Michael Kazhdan, Matthew Bolitho, and Hugues Hoppe. “Poisson surface reconstruction”. In: _Proceedings of the fourth Eurographics symposium on Geometry processing_ . Vol. 7. 4. 2006. 

- [22] Moo Jin Kim et al. “OpenVLA: An Open-Source Vision-LanguageAction Model”. In: _CoRL_ . Vol. 270. 2024, pp. 2679–2713. 

- [23] Sizhe Li et al. “DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics”. In: _ICLR_ . OpenReview.net, 2023. 

- [24] Yunzhu Li et al. “Learning Particle Dynamics for Manipulating Rigid Bodies, Deformable Objects, and Fluids”. In: _ICLR_ . OpenReview.net, 2019. 

- [25] Xingyu Lin et al. “Learning Visible Connectivity Dynamics for Cloth Smoothing”. In: _CoRL_ . 2021. 

- [26] Igor Mordatch, Zoran Popovi´c, and Emanuel Todorov. “Contactinvariant optimization for hand manipulation”. In: _Proceedings of the ACM SIGGRAPH/Eurographics symposium on computer animation_ . 2012, pp. 137–144. 

- [27] Abby O’Neill et al. “Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration”. In: _ICRA_ . 2024, pp. 6892–6903. 

- [28] Octo Model Team et al. “Octo: An Open-Source Generalist Robot Policy”. In: _RSS_ . 2024. 

- [29] Tao Pang et al. “Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models”. In: _IEEE Transactions on Robotics_ 39.6 (2023), pp. 4691–4711. 

- [30] Austin Patel and Shuran Song. “GET-Zero: Graph Embodiment Transformer for Zero-shot Embodiment Generalization”. In: _ICRA_ . 2025. 

- [31] Physical Intelligence et al. “ _π_ 0 _._ 7: A Steerable Generalist Robotic Foundation Model with Emergent Capabilities”. In: _arXiv preprint arXiv:2604.15483_ (2026). 

- [32] Ryan Punamiya et al. “EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World”. In: _CoRR_ abs/2604.07607 (2026). DOI: 10.48550/ARXIV.2604.07607. arXiv: 2604. 07607. URL: https://doi.org/10.48550/arXiv.2604. 07607. 

- [33] Haozhi Qi et al. “From Simple to Complex Skills: The Case of InHand Object Reorientation”. In: _ICRA_ (2025). 

- [34] Yuzhe Qin et al. “DexMV: Imitation Learning for Dexterous Manipulation from Human Videos”. In: _ECCV (39)_ . Vol. 13699. Lecture Notes in Computer Science. Springer, 2022, pp. 570–587. 

- [35] Ri-Zhao Qiu et al. “Humanoid Policy ˜ Human Policy”. In: _arXiv preprint arXiv:2503.13441_ (2025). 

- [36] Daniela Rus. “In-hand dexterous manipulation of piecewise-smooth 3-d objects”. In: _IJRR_ 18.4 (1999), pp. 355–381. 

- [37] J Kenneth Salisbury and John J Craig. “Articulated hands: Force control and kinematic issues”. In: _IJRR_ 1.1 (1982), pp. 4–17. 

- [38] Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. “LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning”. In: _RSS_ (2023). 

- [39] Kenneth Shaw et al. “Bimanual dexterity for complex tasks”. In: _arXiv preprint arXiv:2411.13677_ (2024). 

- [40] Haochen Shi et al. “RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools”. In: _CoRL_ . Vol. 229. Proceedings of Machine Learning Research. PMLR, 2023, pp. 642–660. 

- [41] Haochen Shi et al. “RoboCraft: Learning to see, simulate, and shape elasto-plastic objects in 3D with graph networks”. In: _Int. J. Robotics Res._ 43.4 (2024), pp. 533–549. 

- [42] Haochen Shi et al. “RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks”. In: _RSS_ . 2022. 

- [43] HJ Suh et al. “Dexterous contact-rich manipulation via the contact trust region”. In: _arXiv preprint arXiv:2505.02291_ (2025). 

- [44] Joshua B. Tenenbaum et al. “How to Grow a Mind: Statistics, Structure, and Abstraction”. In: _Science_ 331.6022 (2011), pp. 1279–1285. 

- [45] Tongxuan Tian et al. “Diffusion Dynamics Models with Generative State Estimation for Cloth Manipulation”. In: _CoRL_ (2025). 

- [46] Weikang Wan et al. “LodeStar: Long-horizon Dexterity via Synthetic Data Augmentation from Human Demonstrations”. In: _CoRL_ (2025). 

- [47] Weikang Wan et al. “Unidexgrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalist-specialist learning”. In: _ICCV_ . 2023, pp. 3891–3902. 

- [48] Yixuan Wang et al. “Dynamic-Resolution Model Learning for Object Pile Manipulation”. In: _Robotics: Science and Systems_ . 2023. 

- [49] Zhenyu Wei et al. “D(R,O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping”. In: _arXiv preprint arXiv:2410.01702_ (2024). 

- [50] Bowen Wen et al. “FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects”. In: _CVPR_ . 2024. 

- [51] Shangning Xia et al. “CAGE: Causal Attention Enables DataEfficient Generalizable Robotic Manipulation”. In: _ICRA_ (2025). 

- [52] Fanbo Xiang et al. “SAPIEN: A SimulAted Part-based Interactive ENvironment”. In: _CVPR_ . June 2020. 

- [53] Eliot Xing, Vernon Luk, and Jean Oh. “Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation”. In: _International Conference on Learning Representations (ICLR)_ (2025). 

- [54] Lixin Yang et al. _Multi-view Hand Reconstruction with a PointEmbedded Transformer_ . 2024. 

- [55] Mengjiao Yang et al. “Learning interactive real-world simulators”. In: _ICLR_ . 2024. 

- [56] Kaifeng Zhang et al. “AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation”. In: _Robotics: Science and Systems_ . 2024. 

- [57] Mingtong Zhang, Kaifeng Zhang, and Yunzhu Li. “Dynamic 3D Gaussian Tracking for Graph-Based Neural Dynamics Modeling”. In: _CoRL_ . 2024. 

- [58] Hengshuang Zhao et al. “Point transformer”. In: _ICCV_ . 2021, pp. 16259–16268. 

- [59] Sun Zhaole, Jihong Zhu, and Robert B Fisher. “Dexdlo: Learning goal-conditioned dexterous policy for dynamic manipulation of deformable linear objects”. In: _ICRA_ . IEEE. 2024, pp. 16009–16015. 

