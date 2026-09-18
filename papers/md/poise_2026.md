# **Learning In-Hand Object Reaching to General 6D Poses** 

Junxiao Lin<sup>2</sup><sup>_,_1</sup><sup>_,_3</sup> , Tianyue Wu<sup>2</sup><sup>_,_3</sup> , Jie Yin<sup>2</sup> , Jia Pan<sup>3</sup> , Kaifeng Zhang<sup>2</sup> , Weiming Zhi<sup>1</sup><sup>_,∗_</sup> 



Fig. 1. Real-world in-hand 6D pose reaching. The Hammer (top) and Hexagonal Prism (bottom) are translated and rotated within the hand toward commanded poses. Green and red arrows indicate translational and rotational motions, respectively. 

**_Abstract_ — In-hand manipulation allows multi-fingered dexterous hands to reconfigure grasped objects without releasing and regrasping them. This improves manipulation efficiency by reducing repeated grasp acquisition and large arm motions. However, most learning-based methods focus on reorientation, continuous rotation, or translation, whereas many tasks require joint control of object position and orientation. We formulate this capability as in-hand 6D object pose reaching: starting from an existing grasp, coordinated finger motions move the object to a palm-relative target pose. We present POISE (Palm-relative Object reaching In SE** (3) **), a sim-to-real reinforcement learning framework for this task. POISE combines diverse stablegrasp initialization, goal- and geometry-conditioned control, an adaptive 6D goal curriculum, and a compact reward scheme for pose reaching and grasp preservation. In simulation, diverse initialization raises held-out-grasp success from 40.1% to 51.5% and post-drop recovery from 33.8% to 72.9%; the curriculum raises full-range success from 6.2% to 59.5%. On hardware, the grasp-maintenance reward improves three-target sequence success from 20% to 80%. In real-world experiments, POISE reaches successive 6D targets without manual reset across multiple object geometries and wrist orientations, and recovers from external disturbances. To support further research in dexterous manipulation, we will release our code at https: //junxiaolin.github.io/poise-website/.** 

## I. INTRODUCTION 

Many manipulation tasks begin, rather than end, once an object has been grasped. While parallel-jaw grippers are effective for establishing stable grasps, they have limited ability to reconfigure an object after grasp acquisition. Highdegree-of-freedom dexterous hands, in contrast, can continue 

> 1 School of Computer Science, The University of Sydney, Australia. 2 Sharpa.<sup>3</sup> School of Computing and Data Science, The University of Hong Kong, HKSAR.<sup>_∗_</sup> Corresponding author. 

to manipulate a grasped object through coordinated multifinger motions. This in-hand dexterity is crucial when a robot needs to shift the grasping region on a tool, expose a desired contact surface, or align a functional axis with the environment. 

We formulate this capability as in-hand 6D object pose reaching: given a grasped object and a random target pose defined relative to the hand in the special Euclidean group SE(3), a single multi-fingered dexterous hand must bring the object to the target using only in-hand manipulation. Unlike in-hand reorientation or translation-only tasks [1, 2], this formulation jointly constrains the object’s relative 3D translation and 3D rotation. This coupled objective significantly constrains the feasible motion space and often requires contact switching or finger gaiting while maintaining a stable grasp. Successive reaching further requires each attained object pose to be supported by a grasp that permits continued manipulation. 

Prior work has addressed aspects of this problem from two main directions. Model-based methods can achieve accurate local in-hand pose control, but they often rely on predefined contact modes, fixed contact sequences, or known and simplified object geometry [3]. As a result, they do not readily scale to random SE(3) reaching, where the hand must actively switch contacts and adapt to diverse object shapes. Reinforcement learning (RL), on the other hand, has become a powerful tool for dexterous in-hand manipulation because it can discover contact-rich behaviors without requiring high-quality demonstrations, which are difficult to acquire for such tasks. However, most learning- 

based in-hand manipulation work focuses on reorientation, continuous rotation, or constrained translation [1, 2, 4, 5]. Prior full-pose in-hand reaching methods remain confined to object-specific simulation [6, 7]. 

To bridge these gaps, we develop **POISE** ( **P** alm-relative **O** bject reaching **I** n **SE** (3)), a sim-to-real RL framework based on Proximal Policy Optimization (PPO) [8]. POISE comprises five components: diverse physics-validated stablegrasp resets for broad state coverage; a goal- and geometryconditioned policy for shape-dependent control; an adaptive 6D goal curriculum for learning large pose changes; a compact reward scheme that combines pose reaching, goal completion, grasp maintenance, and regularization; and domain randomization for robust sim-to-real transfer. Experiments demonstrate generalization across initial grasps, recovery after the original grasp is lost, and continued 6D reaching across multiple object geometries and wrist orientations. 

The main contributions of this letter are as follows: 

- 1) A diverse, physics-validated stable-grasp initialization that improves generalization to unseen grasps and recovery after the original grasp is lost. 

- 2) An RL recipe for in-hand 6D pose reaching that combines geometry-conditioned control and adaptive goal curricula with a grasp-maintenance reward based on balanced wrench coverage. 

- 3) Real-world validation of successive 6D reaching across object geometries and wrist orientations, including disturbance recovery and a quantitative evaluation of the grasp-maintenance reward. 

## II. RELATED WORK 

Dexterous in-hand manipulation has been extensively studied, from early analyses of rolling and finger gaiting [9] to modern model-based and learning-based approaches. Modelbased methods compute manipulation motions from explicit models of hand kinematics, fingertip contacts, and object motion. Motion-cone planning derives feasible object motions from contact constraints [10], while trajectory optimization and multi-modal planning coordinate in-grasp motion, finger gaiting, and compliant contact transitions [3, 11]. Model predictive control instead plans over locally identified or contact-implicit dynamics [12]–[14]. These approaches can enforce physical and kinematic constraints directly, but often depend on accurate models, predefined contact modes, or time-consuming online optimization. Extending them to a broad range of 6D goals and object geometries remains challenging. 

Learning-based methods instead discover contact-rich multi-finger coordination through trial-and-error interaction [15]–[18]. RL has enabled real-world reorientation, continuous rotation, and constrained translation [1, 2, 4, 19]– [27]. Recent work further improves generalization across object geometry through visual or explicit shape conditioning [5, 28, 29]. Nevertheless, most of these methods control orientation or a constrained translational motion rather than a general 6D target pose. 

Closest to our setting, Plappert et al. [6] introduced goal-pose-conditioned RL simulation environments for inhand manipulation of block, egg, and pen objects. Initial solutions to these challenging tasks achieved only low success rates; Charlesworth and Montana [7] later improved performance using offline trajectory optimization, but still only in simulation. More recent systems learn 6D object pose reaching through joint arm–hand control toward world-frame goals [30]–[32]. Other controllers track human or synthetic hand–object reference motions [33]–[36]. In contrast, POISE reaches palm-relative SE(3) object goals through finger motions alone, without hand-motion references. 

## III. PROBLEM FORMULATION 

We consider a fixed-wrist hand moving an already-grasped object to commanded poses using only finger motions. Let _H_ and _O_ denote the palm- and object-fixed frames. The current and target palm-relative poses are<sup>_H_</sup> **T** _O,t_ = (<sup>_H_</sup> **p** _t,_<sup>_H_</sup> **R** _t_ ) and<sup>_H_</sup> **T** _O,g_ = (<sup>_H_</sup> **p** _g,_<sup>_H_</sup> **R** _g_ ) _∈_ SE(3). Their position and orientation errors are 



Here, Log( _·_ ) denotes the matrix logarithm and _∥· ∥_ F denotes the Frobenius norm; thus, _eR ∈_ [0 _, π_ ] is the geodesic rotation angle between the two orientations. 

We formulate the task as a goal-conditioned partially observable Markov decision process (POMDP). An MLP actor receives three-frame histories of the current and commanded finger-joint positions, estimated palm-frame object pose and velocity, the gravity direction expressed in the palm frame, a confidence score for the visual pose estimate, the target pose, the current-to-target translation and rotation, and an objectgeometry descriptor **z** _O_ (Sec. IV-B). The critic additionally receives noise-free simulator states, fingertip states, applied joint torques, and contact forces. The normalized action incrementally updates the commanded finger joints, 



A target is reached when both errors remain within their tolerances for a prescribed number of control steps. A new target is then sampled without resetting the hand–object state during training, requiring successive 6D reaches within one continuous rollout. 

## IV. METHOD 

In-hand 6D pose reaching requires the policy to handle varied grasps and object geometries, explore a broad range of 6D poses, and preserve a stable grasp after reaching. POISE addresses these challenges through diverse stablegrasp initialization, geometry-conditioned control, an adaptive 6D goal curriculum, a grasp-preserving reward, and domain randomization, as summarized in Fig. 2. 

## _A. Diverse Stable-Grasp Initialization_ 

Because the task starts after grasp acquisition, each episode must begin from a stable hand–object state. With 



Fig. 2. Overview of POISE. Diverse stable grasps initialize simulation training, while FoundationPose supplies object-pose feedback during realworld deployment. 

only one reset grasp, rollout exploration is largely restricted to states that the current policy can reach from that configuration, leaving alternative object–palm poses and contact arrangements underrepresented. We therefore initialize training from a diverse set of stable grasps. 

Following the optimization-based grasp synthesis paradigm [37], we generate these grasps using a procedure adapted from [38]. Object poses are first sampled over a feasible in-hand workspace. For each pose, we optimize stable contacts and solve for the corresponding joint configuration **q** ; the optimized contact forces are then converted into an executable position-control command **q**<sup>cmd</sup> . Randomized contact search produces multiple postures for each object pose. We then perturb the object pose, **q** , and **q**<sup>cmd</sup> , and simulate each candidate for 2 s under gravity and position control. Only candidates that retain the object are stored in the reset cache _G_ . 

Sampling reset states from _G_ makes grasp diversity an explicit part of the training distribution, rather than leaving it to be discovered through rollout exploration. We evaluate its effect on held-out grasps and recovery in Sec. V-B.1. 

## _B. Geometry-Conditioned Policy_ 

Object shape determines which surfaces and edges can support contact and how finger motion is transferred to the object. Thus, identical current and target poses can require different finger coordination for different geometries. We expose this information through an explicit shape descriptor. 

We use the basis point set (BPS) representation [29, 39]. A fixed set of query points is shared by all objects in their canonical frames, and each entry records the normalized distance from one query point to the nearest object surface. The resulting ordered vector **z** _O_ has the same dimension and spatial structure across objects. 

The actor receives **z** _O_ together with its observation and goal. During multi-object training, one actor is optimized jointly across objects without a categorical identity input; it must therefore use geometry to adapt its finger coordination. The BPS dimension is given in Sec. V-A. 

## _C. Adaptive 6D Goal Curriculum_ 

Sampling the full range of 6D goals from the outset makes early exploration difficult. We therefore use separate curricula that expand the maximum rotation and translation magnitudes from 5<sup>_◦_</sup> and 10 mm to 180<sup>_◦_</sup> and 30 mm, respectively. Only the magnitudes are scheduled; axes and directions remain randomized, with the same limits applied to all targets in a rollout. Targets outside the palm-frame workspace or intersecting the fixed hand base are resampled. 

At each stage, magnitudes are sampled near the frontier, from the exposed range, or at the current limit in a 0 _._ 6 _/_ 0 _._ 3 _/_ 0 _._ 1 ratio. When frontier success reaches 0.4, the rotation or translation limit increases by 10<sup>_◦_</sup> or 10 mm. Each object maintains independent curriculum progress. 

## _D. Grasp-Preserving Reward Design_ 

Reaching the target pose does not guarantee a useful terminal grasp: the object may be loosely supported or held by too few contacts to continue manipulation. Our reward therefore combines pose reaching, verified goal completion, grasp maintenance, and actuation regularization. **Pose reaching.** Using the errors in Eq. (1), the dense pose reward is 





where _α_ and _σ_ vary with _eR_ as 



When the orientation error is large, the position term is broad and downweighted, allowing translation needed for contact rearrangement. As the object becomes rotationally aligned, the reward increasingly emphasizes accurate positioning. **Goal completion.** Let _st ∈{_ 0 _,_ 1 _}_ indicate that the object is retained and lies within both pose tolerances. A goal is verified only after this condition holds for _N_ = 20 consecutive steps; _ct ∈{_ 0 _,_ 1 _}_ marks the first step on which verification occurs. We use 



The per-step term encourages the policy to remain inside the target region, while the one-time bonus rewards verified completion. 

**Grasp maintenance.** We approximate each active contact by four friction-cone wrench rays, with moments normalized by object size. For each force and torque axis, _mt,k ∈_ [0 _,_ 1] is the smaller of the maximum ray projections in its positive and negative directions. We aggregate the six margins as 



This generalized mean emphasizes the weakest of the six bidirectional projection margins, encouraging balanced wrench coverage along the three force and three torque 

axes. Contact contributions saturate with force, preventing the policy from increasing the score merely by squeezing harder. 

Since attainable quality depends on the object and initial grasp, the reward preserves quality relative to the episode’s stable reset rather than using one absolute threshold. Let _Q_<sup>_⋆_</sup> be the mean quality over the first four control steps, clipped to [0 _._ 08 _,_ 0 _._ 35]. We define 



The reward remains maximal while the initial wrench coverage is retained and decreases smoothly as the grasp becomes less secure. 

**Drop and actuation regularization.** Let _dt ∈{_ 0 _,_ 1 _}_ indicate a drop. To discourage object loss and unnecessarily aggressive control, the complete reward penalizes drops, joint torque, and instantaneous mechanical power: 



## _E. Domain Randomization_ 

Real deployment introduces both dynamics mismatch and imperfect visual pose feedback. We randomize object properties, friction, controller gains, and external disturbances to improve robustness to the former. For the latter, the actor receives joint and object-pose noise, pose delay, and hold-last dropouts; object velocities are estimated from the corrupted pose history. Table I summarizes the ranges. 

TABLE I 

SIM-TO-REAL RANDOMIZATION USED DURING TRAINING. _U_ AND LogU DENOTE UNIFORM AND LOG-UNIFORM SAMPLING. 



Fig. 3. First-target success of the diverse policy across independently generated held-out initial grasps under paired 30-mm/180<sup>_◦_</sup> targets. Sphere positions indicate the initial object positions in the palm frame, and color indicates success rate. 



Fig. 4. First-target success of the narrow and diverse policies, marginalized along each palm-frame position axis. Palm-frame _X_ is approximately normal to the palm, while _Y_ and _Z_ lie in the palm plane. 

## _A. Experimental Setup_ 

|Quantity|Range or distribution|
|---|---|
|Object scale|_U_[0_._975_,_1_._025]|
|Object mass|10–100 g|
|Inertia multiplier|LogU[1_,_4]|
|CoM offset|Up to 5 mm per axis|
|Friction multiplier|_U_[0_._5_,_2_._0]|
|PD-gain multipliers|_U_[0_._5_,_2_._0]|
|Wrist orientation|Random over the full orientation range|
|External disturbances|_σa_ = 6_._67 m/s<sup>2</sup>; _σα_ = 133_._33 rad/s<sup>2</sup>|
|Disturbance probability|LogU[1_/_3000_,_1_/_30] per step|
|Joint-position noise|_U_[_−_0_._02_,_0_._02] rad|
|Object-pose noise|_σp_ = 10 mm/axis; _σR_ = 5<sup>_◦_</sup>(clip 15<sup>_◦_</sup>)|
|Pose delay|0–3 steps (0–150 ms)|
|Pose dropout|3% per step; hold last pose|



## V. EXPERIMENTS 

We use simulation and hardware experiments for complementary purposes. Simulation provides controlled, quantitative evidence for the three main design choices: diverse stable-grasp initialization, the adaptive goal curriculum, and the grasp-maintenance reward. Hardware experiments instead focus on system-level capabilities, including reaching across object geometries and wrist orientations, recovery from external disturbances, and continued operation after reaching. 

**Simulation.** We train the policies with asymmetric PPO in Isaac Lab [40]. Physics is simulated at 120 Hz, and the policy produces incremental joint-position commands at 20 Hz. Both actor and critic are [512 _,_ 256 _,_ 128] ELU MLPs, and object geometry is represented by a 64-dimensional BPS descriptor. Unless noted otherwise, ablations use a 40mm Hexagonal Prism and fixed palm-up wrist, changing only the component under study. A target is considered reached when the position and orientation errors remain below 10 mm and 10<sup>_◦_</sup> , respectively, for 20 consecutive policy steps. After reaching, a new target is issued without resetting the hand–object state. Each episode lasts 400 policy steps and terminates early if the object is dropped. 

**Hardware.** The real system consists of a 22-DoF Sharpa Wave hand [41] and a RealSense D435 camera [42]. FoundationPose [43] estimates the object pose from the RGB-D stream and a known object mesh. A calibrated camera-tohand transform expresses the estimate in the palm frame, and the policy runs in closed loop at 20 Hz. The same observation and action interfaces are used in simulation and on hardware; only deployable proprioceptive and visual estimates are provided to the actor. The domain randomization used for transfer is summarized in Table I. 



Fig. 5. Simulation recovery from the same post-drop state and target. The diverse policy (top) rebuilds contact, lifts the object from the palm, and reaches the target. The narrow policy (bottom) attempts to regrasp the object but stalls before reaching the target. 

## _B. Quantitative Simulation Studies_ 

_1) Generalization Across Initial Grasps:_ To isolate the effect of diversity in grasp initialization, we compare the proposed method with a narrow variant whose reset cache is obtained by perturbing the joint state and object pose of a single grasp seed. Each cache contains 6,842 stable reset states; the conditions differ only in their reset-state distributions. We test whether this coverage supports reaching from unseen stable grasps and recovery after the original grasp is lost. 

On independently generated held-out stable grasps, both policies receive the same initial states and 30-mm/180<sup>_◦_</sup> first targets. Diverse initialization increases first-target success from 40.1% to 51.5% and the mean number of completed goals per episode from 0.69 to 1.00. Figs. 3 and 4 further characterize this gain over the initial object position. Smaller _Z_ coordinates and the boundaries of the _Y_ range are more difficult for both policies, while success varies less along _X_ . The diverse policy has higher observed success in every marginalized position bin shown, suggesting that the gain is distributed across the held-out grasp workspace. 

The recovery test then examines whether this broader state coverage also improves recovery after a grasp is broken. Both policies are evaluated on the same 720 trials, with the object resting on the palm and no established grasp. For 30mm/180<sup>_◦_</sup> targets that require lifting the object away from the palm, diverse initialization increases first-target success from 33.8% to 72.9%. Among successful trials, the mean time to recover and reach the target decreases from 11.63 s to 9.45 s. Figure 5 contrasts representative rollouts from the same post-drop state and target: the diverse policy rebuilds multi-finger contact, lifts the object, and reaches the target, 

TABLE II 

ABLATION OF THE ADAPTIVE GOAL CURRICULUM ON THE HEXAGONAL PRISM. STRICT AND NEAR DENOTE FIRST-TARGET SUCCESS UNDER THE 10<sup>_◦_</sup> /10-MM AND 20<sup>_◦_</sup> /20-MM CRITERIA, RESPECTIVELY. 

|||Full ran|ge|Max|imum c|hange|
|---|---|---|---|---|---|---|
|Training|Strict|Near|Goals/ep.|Strict|Near|Goals/ep.|
|Without curriculum|6.2%|18.8%|0.08|3.4%|13.9%|0.04|
|**Curriculum**|**59.5% **|**77.0%**|**1.55**|**55.3% **|**72.8%**|**1.08**|



whereas the narrow policy stalls without reaching the target. Together, the two tests indicate that broader coverage during training improves both generalization across grasp poses and recovery after a drop. 

_2) Effect of the Adaptive Goal Curriculum:_ We compare our curriculum with a variant that samples target magnitudes uniformly over the full range throughout training. Each training run uses 64,000 parallel simulation environments. We evaluate the policies from the same stable grasps and with the same first targets in two suites: full-range targets with rotations in [5<sup>_◦_</sup> _,_ 180<sup>_◦_</sup> ] and translations in [10 _,_ 30] mm, and maximum-change targets of 180<sup>_◦_</sup> and 30 mm. 

We report strict first-target success under the standard 10<sup>_◦_</sup> /10-mm criterion and near success under a relaxed 20<sup>_◦_</sup> /20-mm criterion. The goals-per-episode metric counts targets completed under the strict criterion before reset. 

As shown in Table II, directly training on the full goal range rarely produces successful 6D reaching. The curriculum raises strict success from 6.2% to 59.5% on full-range targets and from 3.4% to 55.3% on maximum-change targets. Near success and the number of completed goals improve consistently as well. Thus, progressively expanding the goal range is important for learning large coupled translations and rotations. 

TABLE III 

GRASP-MAINTENANCE REWARD ABLATION. 

|Metric|Without grasp reward|**With grasp reward**|
|---|---|---|
|Grasp-wrench quality _Q_|0_._032_±_0_._002|**0**_._**045**_±_**0**_._**005**|
|Minimum force margin|0_._077_±_0_._003|**0**_._**107**_±_**0**_._**010**|
|Minimum torque margin|0_._036_±_0_._002|**0**_._**047**_±_**0**_._**004**|
|Episode success rate (%)|53_._7_±_2_._5|**59**_._**1**_±_**2**_._**5**|



_3) Effect of the Grasp-Maintenance Reward:_ We isolate the grasp-maintenance reward by setting only the weight of _rt_<sup>grasp</sup> to zero. We independently train each configuration three times. For each paired comparison, we average the metrics over equal-length training windows after both policies have reached the full 30-mm/180<sup>_◦_</sup> goal range, and report the mean and sample standard deviation across the three runs. 

We focus on four complementary metrics. Grasp-wrench quality _Q_ is the smooth minimum over the six bidirectional force and torque margins defined in Eq. (8). The minimum force and torque margins are the weakest bidirectional coverage values over the three force axes and three torque axes, respectively. Episode success rate is the fraction of completed training episodes in which at least one target is reached. Higher values are better for all four metrics. 

As summarized in Table III, the grasp-maintenance reward increases quality by approximately 41%, the minimum force margin by 39%, and the minimum torque margin by 31% on average. All three grasp metrics improve in every run. Episode success rate also rises from 53.7% to 59.1%, a mean gain of 5.4 percentage points. Thus, encouraging the policy to preserve balanced wrench resistance improves the resulting grasp without sacrificing pose-reaching performance. 

## _C. Real-World Capability Evaluation_ 

We evaluate the complete visual-feedback system on hardware across object geometries and wrist orientations, under external disturbances, and during continued reaching without resets. 

_1) Reaching Across Object Geometries:_ We evaluate the real-world system on four objects with distinct manipulation geometries: Cube, Hexagonal Prism, Square Bifrustum, and Hammer. The first three are drawn from the three training shape families and sizes and share one geometryconditioned policy jointly trained on all nine shape–size combinations. They differ in symmetry and surface structure while having comparable scales. The Hammer, measuring 215 _×_ 50 _×_ 33 _._ 6 mm, further tests the framework on an object with a substantially larger aspect ratio, moment arm, and translational workspace. Owing to its elongated geometry, the Hammer uses an extended translation curriculum of up to 100 mm, while the maximum rotation remains 180<sup>_◦_</sup> . **Continuous random goal reaching.** For each object, we conduct uninterrupted rollouts in which 6D targets are sampled randomly from its feasible workspace. Once the position and orientation errors remain within their tolerances for the required dwell time, a new target is issued without resetting the hand–object system. In each rollout, POISE completed at least five successive goals without resetting the hand–object system. The experiment therefore evaluates not only whether 



Fig. 6. Representative snapshots after successful 6D pose reaching for the Hexagonal Prism, Cube, Square Bifrustum, and Hammer. The cyan outline denotes the commanded object pose, and the coordinate frames indicate the current and target poses. 

the policy can reach an individual pose, but also whether it retains sufficient control of the object for subsequent reaching. Figure 6 shows one representative reached pose for each object geometry. 

**Reaching user-specified targets.** We further test whether the system can follow explicitly specified goals rather than only targets drawn from the random sampler. For the Hexagonal Prism, the commanded sequence moves the object to different in-hand positions while successively orienting different prism faces upward. For the Hammer, we prescribe full 6D targets involving substantial translation and changes in its principal-axis direction. In the representative sequences, POISE reaches four Hexagonal Prism targets with changes of up to 35 mm and 100<sup>_◦_</sup> , and seven Hammer targets with changes of up to 93 mm and 180<sup>_◦_</sup> . The corresponding mean times to reach a target are 3.0 s and 2.7 s. In both cases, each new target is issued from the attained state without resetting the hand or object. Representative reaching sequences are shown in Fig. 1. 

_2) Reaching Under Different Wrist Orientations:_ We deploy the same policy with the wrist fixed in three orientations, thereby changing gravity in the palm frame and reducing the passive support available from the palm. Nevertheless, the policy sustains continued reaching in every configuration. In the representative rollouts shown from left to right in Fig. 8, it completes 7, 5, and 6 successive goals without reset, with mean reaching times of 5.1, 5.5, and 7.1 s. Across the three conditions, the per-target minimum error averages 5.3– 7.4 mm in position and 3 _._ 2<sup>_◦_</sup> –4 _._ 4<sup>_◦_</sup> in orientation, based on the 



Fig. 7. Closed-loop recovery from two consecutive disturbances on hardware. After reaching the target, the object is first perturbed in orientation and then displaced more substantially, changing its contacts. The policy returns it to the unchanged target after each disturbance. 



Fig. 8. Representative real-world reaches under three wrist orientations with different gravity directions in the palm frame. TABLE IV 

REAL-WORLD REACHING SUCCESS WITH AND WITHOUT THE GRASP REWARD. 

|Metric|Without grasp reward|**With grasp reward**|
|---|---|---|
|Complete sequences|2_/_10|**8**_/_**10**|
|Planned targets completed|8_/_30|**27**_/_**30**|
|Mean targets reached|0_._8|**2**_._**7**|
|Reach time (s)|6_._8|**4**_._**9**|
|Position error (mm)|4_._8|**6**_._**4**|
|Orientation error (<sup>_◦_</sup>)|4_._7|**5**_._**9**|



online pose estimates. These results demonstrate continued reaching under different gravity directions using one policy. 

_3) Closed-Loop Recovery from Disturbances:_ We further evaluate whether the policy can recover from unexpected disturbances during real-world operation. After the object reaches the commanded pose, an experimenter perturbs it twice while keeping the target unchanged. As shown in Fig. 7, the first perturbation primarily changes the object orientation, whereas the second produces a larger displacement and a change in the contact configuration. In both cases, the policy responds to the updated visual pose estimate, reorganizes the contacts, and returns the object to the commanded pose. This sequence demonstrates closed-loop recovery from externally induced pose and contact deviations. 

_4) Hardware Ablation of the Grasp-Maintenance Reward:_ We deploy the two policies from Sec. V-B.3 in 10 trials each. Starting from the same grasp, each policy attempts the same sequence of three targets without reset; completing all three defines sequence success. Reach time and steady-state errors are reported as medians over reached targets, with errors averaged over the final 20 policy steps. 

As shown in Table IV, the reward raises sequence success 

from 2 _/_ 10 to 8 _/_ 10 and target success from 26.7% to 90.0%, while maintaining comparable pose accuracy. Without the reward, progressive contact loss often led to object drops. The full policy instead tended to retain more distributed multi-finger contacts, improving the reliability of continued reaching. 

## VI. CONCLUSION AND FUTURE WORK 

We presented POISE, a sim-to-real RL framework for reaching palm-relative 6D object poses through finger motions alone. Our results show that diverse stable-grasp initialization improves generalization to unseen grasp configurations and recovery after contact loss, while the adaptive goal curriculum and grasp-preserving reward enable stable, largerange pose reaching. Together, these findings establish palmrelative SE(3) reaching as a useful primitive for functional in-hand reconfiguration, with the potential to support tool use and other downstream tasks as a step toward general-purpose dexterous manipulation. 

**Limitations and future work.** Two limitations remain. First, POISE specifies the object target pose but not a desired hand or contact configuration. The policy may therefore use effective but unnatural hand postures. Conditioning on both object and grasp targets could produce more natural, taskappropriate motions. Second, real-world performance still lags that in simulation because of imperfect contact modeling and errors in 6D pose tracking. Future work will reduce this gap by incorporating online point-cloud observations through observation distillation, adding tactile feedback, and adapting from real interactions, for example by learning residual dynamics. 

## REFERENCES 

- [1] M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and W. Zaremba, “Learning dexterous in-hand manipulation,” _The International Journal of Robotics Research_ , vol. 39, no. 1, pp. 3–20, 2020. 

- [2] J. Yin, H. Qi, J. Malik, J. Pikul, M. Yim, and T. Hellebrekers, “Learning in-hand translation using tactile skin with shear and normal force sensing,” in _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025, pp. 5850–5856. 

- [3] A. S. Morgan, K. Hang, B. Wen, K. Bekris, and A. M. Dollar, “Complex in-hand manipulation via compliance-enabled finger gaiting and multi-modal planning,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 4821–4828, 2022. 

- [4] H. Qi, A. Kumar, R. Calandra, Y. Ma, and J. Malik, “In-hand object rotation via rapid motor adaptation,” in _Proceedings of the 6th Conference on Robot Learning_ , ser. Proceedings of Machine Learning Research, vol. 205. PMLR, 2023, pp. 1722–1732. 

- [5] T. Chen, M. Tippur, S. Wu, V. Kumar, E. Adelson, and P. Agrawal, “Visual dexterity: In-hand reorientation of novel and complex object shapes,” _Science Robotics_ , vol. 8, no. 84, p. eadc9244, 2023. 

- [6] M. Plappert, M. Andrychowicz, A. Ray, B. McGrew, B. Baker, G. Powell, J. Schneider, J. Tobin, M. Chociej, P. Welinder, V. Kumar, and W. Zaremba, “Multi-goal reinforcement learning: Challenging robotics environments and request for research,” _arXiv preprint arXiv:1802.09464_ , 2018. 

- [7] H. J. Charlesworth and G. Montana, “Solving challenging dexterous manipulation tasks with trajectory optimisation and reinforcement learning,” in _Proceedings of the 38th International Conference on Machine Learning_ , ser. Proceedings of Machine Learning Research, vol. 139. PMLR, 2021, pp. 1496–1506. 

- [8] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017. [Online]. Available: https://arxiv.org/abs/1707.06347 

- [9] L. Han and J. C. Trinkle, “Dextrous manipulation by rolling and finger gaiting,” in _Proceedings of the 1998 IEEE International Conference on Robotics and Automation_ , vol. 1, 1998, pp. 730–735. 

- [10] N. C. Dafle, R. Holladay, and A. Rodriguez, “In-hand manipulation via motion cones,” in _Proceedings of Robotics: Science and Systems_ , Pittsburgh, Pennsylvania, June 2018. 

- [11] B. Sundaralingam and T. Hermans, “Relaxed-rigidity constraints: Kinematic trajectory optimization and collision avoidance for in-grasp manipulation,” _Autonomous Robots_ , vol. 43, no. 2, pp. 469–483, 2019. 

- [12] P. Chanrungmaneekul, K. Ren, J. T. Grace, A. M. Dollar, and K. Hang, “Non-parametric self-identification and model predictive control of dexterous in-hand manipulation,” in _2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2023, pp. 8743–8750. 

- [13] Y. Jiang, M. Yu, X. Zhu, M. Tomizuka, and X. Li, “Contact-implicit model predictive control for dexterous in-hand manipulation: A longhorizon and robust approach,” in _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2024, pp. 5260–5266. 

- [14] H. J. T. Suh, T. Pang, T. Zhao, and R. Tedrake, “Dexterous contact-rich manipulation via the contact trust region,” _The International Journal of Robotics Research_ , vol. 45, no. 9, pp. 1418–1454, 2026. 

- [15] G. Khandate, S. Shang, E. T. Chang, T. L. Saidi, J. Adams, and M. Ciocarlie, “Sampling-based exploration for reinforcement learning of dexterous manipulation,” in _Proceedings of Robotics: Science and Systems_ , 2023. 

- [16] Z.-H. Yin, C. Wang, L. Pineda, F. Hogan, K. Bodduluri, A. Sharma, P. Lancaster, I. Prasad, M. Kalakrishnan, J. Malik, M. Lambeta, T. Wu, P. Abbeel, and M. Mukadam, “DexterityGen: Foundation controller for unprecedented dexterity,” 2025. [Online]. Available: https://arxiv.org/abs/2502.04307 

- [17] H. Zhang, J. Ferchow, J. Song, and M. Meboldt, “UniCross: Unified cross-skill dexterous manipulation synthesis,” _arXiv preprint arXiv:2607.28198_ , 2026. 

- [18] L. Pei, T. Wu, H. Zhang, P. Luo, and J. Song, “Assembling two parts in one hand,” in _Conference on Robot Learning_ , 2026, to appear. 

- [19] I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron, A. Paino, M. Plappert, G. Powell, R. Ribas, _et al._ , “Solving Rubik’s cube with a robot hand,” _arXiv preprint arXiv:1910.07113_ , 2019. 

- [20] T. Chen, J. Xu, and P. Agrawal, “A system for general in-hand object re-orientation,” in _Proceedings of the 5th Conference on Robot Learning_ , ser. Proceedings of Machine Learning Research, vol. 164. PMLR, 2022, pp. 297–307. 

- [21] A. Handa, A. Allshire, V. Makoviychuk, A. Petrenko, R. Singh, J. Liu, D. Makoviichuk, K. Van Wyk, A. Zhurkevich, B. Sundaralingam, _et al._ , “DeXtreme: Transfer of agile in-hand manipulation from simulation to reality,” in _2023 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2023, pp. 5977–5984. 

- [22] H. Qi, B. Yi, S. Suresh, M. Lambeta, Y. Ma, R. Calandra, and J. Malik, 

   - “General in-hand object rotation with vision and touch,” in _Proceed-_ 

   - _ings of the 7th Conference on Robot Learning_ , ser. Proceedings of Machine Learning Research, vol. 229. PMLR, 2023, pp. 2549–2564. 

- [23] Z.-H. Yin, B. Huang, Y. Qin, Q. Chen, and X. Wang, “Rotating without seeing: Towards in-hand dexterity through touch,” in _Proceedings of Robotics: Science and Systems_ , 2023. 

- [24] M. Yang, C. Lu, A. Church, Y. Lin, C. Ford, H. Li, E. Psomopoulou, D. A. W. Barton, and N. F. Lepora, “AnyRotate: Gravity-invariant in-hand object rotation with sim-to-real touch,” 2024. [Online]. Available: https://arxiv.org/abs/2405.07391 

- [25] X. Liu, H. Wang, and L. Yi, “DexNDM: Closing the reality gap for dexterous in-hand rotation via joint-wise neural dynamics model,” in _International Conference on Learning Representations_ , 2026. [Online]. Available: https://openreview.net/forum?id=80vjyj5o7l 

- [26] A. Bhardwaj, M. Wilder-Smith, M. Mittal, V. Patil, and M. Hutter, “ViserDex: Visual sim-to-real for robust dexterous in-hand reorientation,” in _Proceedings of Robotics: Science and Systems_ , 2026. 

- [27] J. Yin, Z. Zhao, X. Tan, Y. Liu, C. Wang, and X. Gu, “WM-Craftnet: World synesthesia model for generalizable and robust dexterous inhand manipulation,” in _Conference on Robot Learning_ , 2026. 

- [28] W. Huang, I. Mordatch, P. Abbeel, and D. Pathak, “Generalization in dexterous manipulation via geometry-aware multi-task learning,” arXiv preprint arXiv:2111.03062, 2021. 

- [29] J. Pitz, L. R¨ostel, L. Sievers, D. Burschka, and B. B¨auml, “Learning a shape-conditioned agent for purely tactile in-hand manipulation of various objects,” in _2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2024, pp. 13 112– 13 119. 

- [30] K. Kedia, T. G. W. Lum, J. Bohg, and C. K. Liu, “SimToolReal: An object-centric policy for zero-shot dexterous tool manipulation,” arXiv preprint arXiv:2602.16863, 2026. 

- [31] T. G. W. Lum, K. Kedia, C. K. Liu, and J. Bohg, “Play2Perfect: What matters in dexterous play pretraining for precise assembly?” arXiv preprint arXiv:2606.26428, 2026. 

- [32] Y. Kuang, S. Park, K. Fragkiadaki, and S. Tulsiani, “Dex4D: Taskagnostic point track policy for sim-to-real dexterous manipulation,” 2026. [Online]. Available: https://arxiv.org/abs/2602.15828 

- [33] X. Liu, J. Adalibieke, Q. Han, Y. Qin, and L. Yi, “DexTrack: Towards generalizable neural tracking control for dexterous manipulation from human references,” in _International Conference on Learning Representations_ , 2025. 

- [34] K. Li, P. Li, T. Liu, Y. Li, and S. Huang, “ManipTrans: Efficient dexterous bimanual manipulation transfer via residual learning,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2025, pp. 6991–7003. 

- [35] Y. Wang, R. Yu, H. W. Tsui, X. Lin, H. Zhang, Q. Zhao, K. Fan, M. Li, J. Song, J. Wang, Q. Chen, and P. Tan, “Learning generalizable hand-object tracking from synthetic demonstrations,” _arXiv preprint arXiv:2512.19583_ , 2025. 

- [36] P. Li, Z. Chen, Y. Wu, P. Wei, Y. Li, T. Wang, J. Shi, M. Yu, B. Jia, S.-C. Zhu, T. Liu, and S. Huang, “Towards human-level dexterous teleoperation,” _arXiv preprint arXiv:2607.11481_ , 2026. 

- [37] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang, “DexGraspNet: A large-scale robotic dexterous grasp dataset for general objects based on simulation,” in _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , 2023, pp. 11 359– 11 366. 

- [38] Z.-H. Yin and P. Abbeel, “Lightning Grasp: High performance procedural grasp synthesis with contact fields,” _arXiv preprint arXiv:2511.07418_ , 2025. 

- [39] S. Prokudin, C. Lassner, and J. Romero, “Efficient learning on point clouds with basis point sets,” in _2019 IEEE/CVF International Conference on Computer Vision (ICCV)_ . IEEE, 2019, pp. 4331–4340. 

- [40] M. Mittal, P. Roth, J. Tigue, A. Richard, O. Zhang, P. Du, A. SerranoMunoz, X. Yao, R. Zurbr¨ugg, N. Rudin, _et al._ , “Isaac Lab: A GPUaccelerated simulation framework for multi-modal robot learning,” _arXiv preprint arXiv:2511.04831_ , 2025. 

- [41] Sharpa, “Sharpa Wave,” accessed: Aug. 27, 2026. [Online]. Available: https://www.sharpa.com/pages/wave 

- [42] RealSense, “RealSense D435,” accessed: Aug. 27, 2026. [Online]. Available: https://www.realsenseai.com/cn/products/ stereo-depth-camera-d435/ 

- [43] B. Wen, W. Yang, J. Kautz, and S. Birchfield, “FoundationPose: Unified 6D pose estimation and tracking of novel objects,” in _2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2024, pp. 17 868–17 879. 

