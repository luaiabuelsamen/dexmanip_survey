Preprint 



# **DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy** 

**Haichao Liu**<sup>1</sup> **, Yuyao Jiang**<sup>1</sup> **, Hyunsun Park**<sup>2</sup> **, Yuanjiang Xue**<sup>1</sup> **, and Ziwei Wang**<sup>**†**1</sup> 

1Nanyang Technological University, Singapore 

2OOJU, USA 

†Corresponding author. 

#### **Abstract** 

Fine-grained, bimanual dexterous manipulation remains a foundational challenge in robotics. Traditional teleoperation systems often fail in contact-rich tasks because embodiment gaps hinder accurate kinematic mapping, while tactile and force feedback remain absent. Consequently, data collection efficiency for highprecision tasks remains prohibitively low. To address these limitations, we propose a tactile-driven adaptation strategy designed to enable fine-grained manipulation on top of teleoperation pipelines. Instantiated within our bimanual dexterous framework, DexTeleop-0, this strategy introduces a real-time optimization loop that bridges the embodiment gap by translating coarse human tracking intents into precise, force-compliant robotic commands with tactile sensing. By estimating accurate contact points and leveraging a tactile-enabled fingertip force-sensing profile, the system dynamically computes localized corrections using the operational space Jacobian with respect to joint angle updates. We rigorously evaluate this tactile-driven adaptation strategy across both simulated environments and real-world hardware. Compared with representative baselines, the proposed method consistently achieves higher task success rates and improved execution efficiency in robust grasping, disturbance-resilient manipulation, and complex dexterous tasks. 

**Project page:** `https://henryhcliu.github.io/dexteleop-0` **Correspondence:** ziwei.wang@ntu.edu.sg 

**Keywords:** Dexterous manipulation, shared autonomy, teleoperation, tactile feedback, optimization 

## **1 Introduction** 

The realization of human-level manual dexterity remains one of the ultimate frontiers in robotics. Multi-fingered robotic hands offer the structural versatility required to execute contact-rich, fine-grained manipulation tasks that are far beyond the capabilities of conventional parallel grippers. However, successfully executing these delicate interactions depends heavily on closing the feedback loop with high-resolution tactile profiles. Tactile sensing provides critical physical insights into localized pressure profiles, transient slip conditions, and multi-point contact dynamics [1, 2], making it indispensable for complex dexterous manipulation. To expand the functional envelope of these multi-fingered platforms, bimanual dexterous manipulation has emerged as a highly promising avenue of research. Mirroring the innate cooperative strategies of human behavior, bimanual configurations allow robots to stabilize non-prehensile objects and orchestrate highly synchronized dual-arm assemblies. Crucially, as robots 

1 



<!-- Start of picture text -->
Before Balancing After Balancing<br>Friction<br>Friction<br>𝐹tactile2 ′<br>𝐹tactile1 Tactile 𝐹tactile1′ Gravity 𝐹tactile2<br>Gravity Balancing<br>Unstable Interaction Stable Interaction<br><!-- End of picture text -->

**Figure 1.** The core principle of the proposed tactile balancing framework. **Left (Before Balancing):** Misaligned finger contact points generate asymmetric tactile forces that fail to counteract friction and gravity, yielding an unstable interaction. **Right (After Balancing):** By dynamically adjusting the dexterous hand’s posture based on real-time tactile feedback, the system rectifies the contact forces to achieve a stable force-balanced interaction. 

transition to bimanual topologies, they can better leverage vast repositories of human behavioral data, including data-driven imitation learning demonstrations, passive human videos, and egocentric tracking datasets [3–5]. 

Despite this potential, acquiring high-quality bimanual dexterous data presents a significant bottleneck. A major underlying issue is the inherent _embodiment gap_ between human hands and multi-fingered robotic topologies, which prevents completely accurate motion mapping. When compounded by the conventional absence of haptic or tactile feedback during teleoperation, operators struggle to perceive subtle contact states. This lack of physical awareness renders fine-grained, contact-rich manipulation tasks exceptionally difficult to execute, resulting in low data collection efficiency. Furthermore, existing hardware configurations fail to alleviate this issue: traditional leader-follower kinesthetic rigs [6, 7] are structurally rigid and embodiment-specific, mechanical exoskeletons [8] are physically cumbersome, and vision-only retargeting methods suffer from severe occlusions and joint tracking drift during complex hand-to-hand interactions. 

To bridge this gap, we introduce a **tactile-driven adaptation strategy** for bimanual dexterous teleoperation, implemented within our framework named **DexTeleop-0** . Rather than claiming the underlying egocentric perception hardware stack as our primary novelty, we focus on enabling high-precision, contact-rich adjustments on top of existing tracking systems. Our setup utilizes an accessible egocentric vision pipeline via a commercial VR headset to capture human tracking intents, which are then mapped onto a high-dimensional 56-Degree-of-Freedom (DoF) bimanual robot assembly through an inverse kinematics (IK) retargeting model. Critically, to overcome tracking inaccuracies stemming from the embodiment gap and the lack of force transparency, our tactile-driven adaptation strategy establishes a _force-balanced residual action optimization_ loop. As illustrated in Fig. 1, by estimating precise contact points and measuring continuous fingertip forces, the system dynamically computes force variations using the operational space Jacobian relative to individual joint angle updates. This formulation applies localized, compliant corrections to the operator’s tracking input, ensuring interactive safety and grasping stability, without requiring restrictive mechanical rigs. 

In summary, our primary contributions are as follows: 

- We propose a tactile-driven shared autonomy adaptation strategy for high-dimensional bimanual dexterous manipulation that explicitly bridges the control and interaction gap during physical contact. 

- We develop a contact-rich force sensing and predictive interaction modeling framework that systematically closes the visual-tactile feedback loop during delicate physical engagements. 

- We design a lightweight, hardware-agnostic teleoperation framework that utilizes egocentric vision perception and IK-based dexterous hand retargeting to translate human tracking intent into coordinated robotic commands. 

2 

- Our full-stack solution is comprehensively validated across an aligned simulation environment and physical robotic platform, demonstrating substantial improvements in both data-collection efficiency and task success rates compared to representative baselines. 

## **2 Related Work** 

### **2.1 Robotic Teleoperation Systems** 

Robotic teleoperation serves as the foundational mechanism for collecting high-quality demonstrations for imitation learning frameworks. Early paradigms focused on bilateral leader-follower arrangements using identical kinesthetic teaching rigs or low-cost mechanical link models such as GELLO [6] and ALOHA [7, 9]. While highly precise for parallel grippers, these setups do not naturally scale to the high-dimensional spaces required for multi-fingered hands. To capture highly expressive hand motions, researchers explored mechanical and visual-exoskeleton interfaces [8] or traditional input options like multi-axis joystick controllers [10]. However, these approaches remain ergonomically exhausting or limited in high-DoF coordination. Consequently, vision-only and spatial-tracking teleoperation have gained significant traction. Vision-based retargeting systems observe the human hand using standalone cameras to map coordinates onto robotic alternatives [11–13]. While flexible, single-camera configurations are highly susceptible to visual occlusions during bimanual interactions. To resolve this, modern setups leverage immersive spatial computing via VR/AR headsets (e.g., Apple Vision Pro, Meta Quest) to deliver real-time active visual feedback and robust egocentric hand tracking [14, 15]. DexTeleop-0 builds upon this spatial tracking paradigm but augments the visual stream with close-loop tactile force optimization to resolve the lack of physical awareness typical of pure vision systems. 

### **2.2 Dexterous Manipulation** 

Dexterous manipulation research aims to replicate human-like interaction with diverse object geometries. At the individual hand level, extensive research has addressed intricate behaviors like general grasping, turning Rubik’s cubes, or pen-spinning using complex reinforcement learning and motion planning priors [16–19]. Moving beyond single-handed operations, multi-fingered bimanual dexterous manipulation coordinates redundant, high-DoF architectures to perform complex, long-horizon tasks [20–22]. A major challenge across these methodologies is their data-hungry nature; modern vision-language-action foundation models or deep visuomotor policies require vast numbers of highly accurate human demonstrations [23, 24]. Because teleoperation stands as the primary channel for obtaining these high-quality trajectories, embedding high-fidelity modalities directly within the control loop is vital. Recent benchmarks have highlighted that integrating visual-tactile representation learning significantly improves the sample efficiency and generalizability of downstream imitation policies [25]. 

### **2.3 Tactile-Enhanced Manipulation** 

Integrating tactile information into robotic manipulation provides a direct measure of interaction forces that vision alone cannot capture. In parallel gripper frameworks, tactile arrays are commonly applied to compute fast slip-detection boundaries, gauge object compliance, or guide slow-fast visual-tactile fusion policies during contact-rich placements [26, 27]. For high-DoF dexterous hands, tactile sensors embedded across fingertips enable multi-point visual-tactile estimation and detailed geometric reconstruction during complex in-hand re-orientation [2, 28]. Furthermore, large-scale visual-tactile pretraining has shown outstanding success in yielding humanlike manipulation adaptability across multi-task regimes [25]. Rather than treating tactile feedback solely as a passive input to a neural network policy, shared autonomy architectures use tactile data to establish dynamic action correlations, adjusting operator trajectories to respect physical constraints [29, 30]. Following this insight, DexTeleop-0 uses real-time fingertip force inputs to formulate a localized optimization problem, continuously projecting the user’s tracking commands onto a physically consistent, force-compliant manifold via the operational space Jacobian. 

3 

## **3 Methodology** 



<!-- Start of picture text -->
Ego-Centric Perception Stream<br>(Quest 3)<br>TCP Port, Async Packet [26 Hand Poses, Left/Right]<br>Arm Data Module Finger Retargeting Module<br>Wrist Normalization<br>Arm Wrist Tracking Align Wrist to Neutral Robot Frame<br>Hand Robot<br>Analytical IK Solver<br>𝑞arm  (6 DoF)<br>Dexterous Hand Retargeter<br>𝑞tele (22-DoF)<br>Trajectory Aggregator<br>Combined Articulation Targets<br>[𝑞arm, 𝑞tele + ∆𝑞]<br>Force Balance Controller<br>Output:  Δ𝑞 (Corrected Action Delta)<br>Action Execution Fingertip Force<br>&<br>Isaac Sim / Real Robot Contact Points<br>with interactive objects in the environment<br><!-- End of picture text -->

**Figure 2.** System architecture of DexTeleop-0, highlighting the integration of ego-centric perception, parallel arm and finger retargeting pathways, and a closed-loop force balance controller for coordinated action execution. 

### **3.1 Problem Formulation** 

We consider a bimanual teleoperation system consisting of dual high-degree-of-freedom (DoF) robotic manipulators equipped with multi-fingered dexterous hands, driven by tracking signals from human motion capture interfaces. The central control challenge arises from the _tactile and force feedback missing problem_ . To bridge this gap, our strategy is systematically translating raw human tracking coordinates into safe, physically compliant robotic joint commands. The tracking data retrieved from the VR headset’s egocentric perception at each time step is decomposed into distinct human hand and wrist states. For each hand, the tracking input yields a set of _𝑀_ transformations in the Special Euclidean Group representing the human hand joints, defined as: 



Concurrently, the global spatial position and orientation of the human operator’s wrist is captured as a single transform vector **T** _𝑤_ ∈ _𝑆𝐸_ (3). The ultimate objective of our control framework is to map these tracking observations onto the joint spaces of the bimanual dexterous robotic system. The deployment configuration of each robotic arm-hand assembly is specified as follows: The robotic dexterous hand possesses _𝑁_ DoFs, characterized by its joint angle configuration vector **q** _ℎ_ ∈ R<sup>_𝑁_</sup> . The retargeting problem requires formulating a mapping function Fhand : _𝑆𝐸_ (3)<sup>_𝑀_</sup> → R<sup>_𝑁_</sup> that maps the _𝑀_ human hand joint vectors to the _𝑁_ robotic joint angles while preserving structural synergy and finger-tip positioning **q** _ℎ_ = Fhand(H) Similarly, the robotic arm possesses _𝑄_ DoFs with **q** _𝑎_ ∈ R<sup>_𝑄_</sup> . The inverse kinematics mapping Farm : _𝑆𝐸_ (3) → R<sup>_𝑄_</sup> maps the human wrist pose **T** _𝑤_ to the _𝑄_ joint angles of the robotic arm **q** _𝑎_ = Farm( **T** _𝑤_ ). 

Given the raw target joint commands **q** raw = [ **q**<sup>_𝑇_</sup> _𝑎_<sup>_,_</sup><sup>**q**</sup><sup>_𝑇_</sup> _ℎ_<sup>]</sup><sup>_𝑇_∈R</sup><sup>_𝑄_+</sup><sup>_𝑁_, the core challenge lies in modulating this</sup> 

4 

tracking intent in real time. As demonstrated in Fig. 2, we formulate this as a shared autonomy problem where **q** raw is continuously optimized to satisfy localized tactile force constraints, outputting a force-aware, stable command configuration **q**<sup>∗</sup> = **q** raw + Δ **q** that prevents slippage and object damage during physical engagement. 

### **3.2 Dexterous Hand Retargeting** 

To execute the mapping Fhand defined in Section 3.1, we transform the tracked _𝑀_ = 26 human hand joints H into target configurations for the _𝑁_ = 22 DoFs of the robotic dexterous hand. Rather than tracking absolute joint angles which suffer from significant morphology mismatches, we adopt a vector-based retargeting paradigm inspired by DexPilot. Inspired by [31], we extract a set of _𝐾_ critical inter-joint and finger-to-palm target vectors from the VR-based human hand tracking data. For the _𝑘_ -th keypoint pair, the human target vector is denoted as **v**<sup>∗</sup> _𝑘_<sup>∈R3.The corresponding structural vector on the robotic hand is</sup> dynamically computed via forward kinematics as: 



where **p** task _,𝑘,_ **p** origin _,𝑘_ ∈ R<sup>3</sup> are the operational space positions of the target and origin links on the robot hand given the joint angles **q** _ℎ_ . 

To ensure stable finger-to-finger contact closures during fine-grained grasping, we apply a "project-andescape" tracking logic to a designated subset of _𝐾 𝑝_ tip-to-tip vectors. Let _ℓ𝑘_ = ∥ **v**<sup>∗</sup> _𝑘_<sup>∥represent the scalar</sup> length of the human reference vector. The finalized reference vector **v**<sup>ref</sup> _𝑘_<sup>used for optimization is formulated</sup> as: 



where _𝑑_ project and _𝑑_ escape are hysteresis thresholds, and _𝑑𝑘_ is a predefined contact distance. When a vector is marked as _Projected_ , it signifies active intention of a close-range pinch or grasp, and its optimization weight _𝑤 𝑘_ is augmented to a high value ( _𝑤 𝑘_ = _𝑤_ high) to strictly enforce the contact geometry. Otherwise, it defaults to a nominal weight ( _𝑤 𝑘_ = _𝑤_ normal). 

We frame the real-time kinematic retargeting task as a constrained non-linear optimization problem over the robotic hand joint angles **q** _ℎ_ : 





where H _𝛿_ (·) is the robust Huber loss designed to reject measurement outliers from the VR headset perception, and **q** lb _,_ **q** ub ∈ R<sup>_𝑁_</sup> represent the physical lower and upper joint limits of the robotic hand. A quadratic regularization term weighted by _𝜆_ penalizes deviations from the joint configuration of the previous frame **q**<sup>last</sup> _ℎ_<sup>, effectively suppressing high-frequency tracking jitter and stabilizing the retargeted</sup> output. 

This optimization framework is solved in real time ( _<_ 15 ms) using SLSQP. Analytical gradients are efficiently propagated through the operational space Jacobian **J** _𝑥_ ( **q** _ℎ_ ) to ensure rapid convergence within a strict iteration budget, outputting the kinematically retargeted hand configuration **q** _ℎ_ . 

### **3.3 Contact-Rich Force-Aware Shared Autonomy** 

While the retargeting framework effectively mirrors human motion kinematics, the absence of physical haptic feedback compromises interaction safety and robustness during contact-rich tasks. To address the tactile and force feedback missing problem, we introduce a contact-rich, force-aware shared autonomy layer. This layer operates as a real-time tracking modulator that continuously overrides the nominal teleoperated joint commands **q** tele by computing a compliant residual action Δ **q** . The final command 

5 

executed by the bimanual system is formulated as: **q** final = **q** tele + Δ **q** , where Δ **q** is derived from a unified Quadratic Programming (QP) optimization framework that balances localized fingertip force regulation with global object-centric force-torque stability. 

#### **3.3.1 Tactile Sensing Processing and Contact State Estimation** 

To achieve precise force-aware control, the system continuous samples multi-contact interaction profiles at each finger tip. For each finger _𝑖_ , the tactile perception framework estimates the contact force in the world coordinate frame **f** _𝑖_<sup>_𝑤_∈R3 and the contact point location.To accurately compute object-centric load</sup> distributions without relying on complex external object models, we establish a dynamic local reference frame. We collect the world-frame contact positions **p** _𝑖_<sup>_𝑤_∈R3 across all</sup><sup>_𝑁𝑐_active contacts and estimate</sup> the instantaneous object reference center **p** obj as their mean: 



The localized contact point position vector relative to this object center is then defined as: 



To handle transient contact phase transitions and guard against high-frequency signal noise, we pass the magnitude of the raw contact force ∥ **f** _𝑖_ ∥ through a continuous logistic activation weight function governed by a hysteresis state machine: 



where _𝜎_ (·) represents the standard logistic function, _𝑘_ denotes the activation slope parameter, and <u>1</u> _𝑚_ = 2<sup>(</sup><sup>_𝑓_release+</sup><sup>_𝑓_contact)characterizestheoperationalmidpointofthehysteresisdeadband.</sup> This continuous formulation yields a smooth activation weight _𝑤𝑖_ ∈[0 _,_ 1] that scales the participation of each individual finger in the subsequent optimization steps based on its current contact reliability. 

#### **3.3.2 Localized Force Feedback Tracking** 

For active fingers, the optimization loop aims to modulate joint velocities such that fingertip interaction forces remain bounded within a desired operational window [ _𝑓_ min _, 𝑓_ max]. We relate joint parameter variations to spatial displacement profiles using the operational space contact Jacobian **J** _𝑖_ ( **q** ). The linear contribution of the joint angle increments to force dampening is captured via the interaction matrix **A** _𝐹_ : 



where the negative sign ensures that the calculated joint modifications actively counteract the accumulation of destructive contact forces. Let **r** _𝑖_<sup>_𝐹_define the raw scalar force error indicating the magnitude by which</sup> the contact force exceeds the specified safety boundaries. We project this force domain error into a corresponding displacement domain residual vector _𝝆𝑖_<sup>_𝐹_through a virtual force residual stiffness scaling</sup> parameter _𝐾𝐹_ : 



The localized force tracking objective is then formulated as a quadratic error minimization cost: 



6 

where _𝜆𝐹_ serves as a prioritized penalty weight scaled proportionally by the instantaneous contact activation parameter _𝑤𝑖_ , and _𝝆𝐹_ represents the consolidated residual vector across all active fingertips. 

#### **3.3.3 Multi-Contact Force-Torque Balance Evaluation** 

Crucially, localized force corrections alone can introduce destabilizing torques that induce object slippage or rotation during fine-grained bimanual tasks. To enforce cooperative grasp stability, we introduce a shared-autonomy multi-contact balance penalty. We evaluate the instantaneous net force **F** ∈ R<sup>3</sup> and net torque _𝝉_ ∈ R<sup>3</sup> acting upon the object reference center: 



Given the target structural load specifications **F**<sup>∗</sup> and _𝝉_<sup>∗</sup> , the system computes the global force and torque domain discrepancies: 



To prevent the collaborative balance items from competing with the localized primary safety tracking commands during minor tracking fluctuations, a filtering deadband parameter _𝜖_ is applied to the raw residuals: 



To map the object-level force-torque deviations into the joint space optimization variables, we linearize the multi-contact equations. While the net force variation maps directly using the interaction matrix Δ **F** ≈ **A** _𝐹_ Δ **q** , the torque variation relies on a skew-symmetric cross-product formulation: 



where [ **p** _𝑖_ ] × ∈ R<sup>3×3</sup> is the skew-symmetric matrix representation of the contact arm vector **p** _𝑖_ . The resulting multi-contact balance optimization penalty _ℓ𝐵_ (Δ **q** ) is represented as a secondary soft quadratic task: 



where _𝝆𝐹_ = **r** _𝐹_ / _𝐾𝐹_ and _𝝆 𝜏_ = **r** _𝜏_ / _𝐾𝜏_ correspond to the standardized displacement-equivalent tracking residuals, and _𝜆_ fb _, 𝜆_ tb define the force and torque balance prioritization hyper-parameters, respectively. 

#### **3.3.4 Unified Force Balance Optimization** 

We unify the localized safety constraints and cooperative balance requirements into a single box-constrained QP solved at every control cycle at 30 Hz: 







where **H** 0 and **g** 0 constitute the nominal stabilization Hessian and linear cost arrays that govern smooth joint tracking transitions. The optimization is subject to dual structural boundaries: physical hardware joint constraints ( **q** min _,_ **q** max) and a strict slew-rate saturation limit _𝜹_ (derived from maximum permissible joint velocity configurations **v** max). 

The problem is resolved using an efficient projected gradient box-QP solver. This shared autonomy loop ensures that while the main tracking intent is preserved from the VR headset perception, the execution commands are projected onto a force-compliant, physically stable manifold. This capability enables robust grasping and anti-disturbance object handling in complex bimanual environments. 

7 

## **4 Experimental Results and Analysis** 

### **4.1 Experimental Setup and Metrics** 



**Figure 3.** Comparison of physical and simulated bimanual systems. **Left:** The real-world hardware setup with twin UR7e arms and Sharpa Wave dexterous hands. **Right:** The digital twin in IsaacSim for evaluation and validation. Both configurations support Meta Quest 3 teleoperation. 

#### **4.1.1 System Architecture and Hardware Configuration** 

Our framework aligns virtual and physical environments to facilitate a seamless sim-to-real transfer pipeline as shown in Fig. 3. The simulation domain is hosted within NVIDIA IsaacSim 4.5, whereas the real-world deployment leverages an identical twin physical platform. Each manipulator branch integrates a 6-DoF Universal Robots UR7e arm with a 22-DoF Sharpa Wave dexterous hand, establishing a high-dimensional control loop managing 56 DoFs simultaneously across the bimanual system. Human movement perception and tracking commands are extracted entirely from an egocentric Meta Quest 3 VR headset without requiring external motion-capture hardware. 

#### **4.1.2 Algorithmic Baselines** 

We compare our approach against three algorithmic benchmarks to isolate the benefits of our shared autonomy optimization. The **No-Residual** baseline performs exact kinematic position mapping directly from the VR headset tracking data without applying any residual trajectory adjustments. The **Joint-Level PD Control** baseline introduces localized proportional-derivative loops at the finger joints to dynamically damp excessive physical forces based on raw tactile threshold inputs. The **Single-Force Tracking** ablation model implements only the localized fingertip force feedback tracking module ( _ℓ𝐹_ ) and removes the multi-finger cooperative balance component ( _ℓ𝐵_ ). **DexTeleop-0** represents our full optimization method incorporating both local contact compliance and global object force-torque balance. 

#### **4.1.3 Task Specifications and Performance Evaluation** 

The evaluation tasks span single-arm fine dexterity and dual-arm coordination. To maintain brevity, the benchmark tasks are structurally summarized in Table 1. To mathematically analyze baseline performance, we utilize two principal metrics. The **Multi-Stage Success Rate** evaluates operational proficiency by decomposing long-horizon actions into distinct operational segments. For 

**Table 1.** Summary of Simulation and Real-World Evaluation Tasks 

|**Domain**|**Configuration**|**Task Name**|
|---|---|---|
|Simulation|Single-Arm<br>Dual-Arm|Ball Assembly<br>Stir in Cup|
||Single-Arm|Gear Assembly|
|Real-World|Single-Arm<br>Dual-Arm|Insert Peg into Tube<br>Fruit and Vegetable Sorting|
||Dual-Arm|ChemistryExperiment|



tasks with non-sequential phases (e.g., initial grasp stages in bimanual routines), failures in one sector do not propagate to penalize adjacent validation steps. The **Force Statistical Data** assesses grasp compliance and physical safety by computing the continuous mathematical mean and variance of the thumb contact force profile throughout task execution. Unlike traditional error metrics, this index does not exhibit a 

8 

monotonic correlation with performance. Our objective is to minimize interaction forces while ensuring robust interaction stability. Simulation evaluations are conducted via strict teleoperated trajectory replay across different residual control approaches. During replay, the nominal trajectory remains identical, while object physical parameters, specifically mass and friction coefficients, are subjected to random variance. To ensure evaluation fairness, these physical parameters are kept identical across different methods within the same trial index. For real-world evaluation, teleoperation trajectories are collected from a diverse pool of operators, consisting of five inexperienced and two professional operators. Each operator conducts five trials per task for each method evaluated. 

### **4.2 Comparison Results** 

We evaluate the performance of DexTeleop-0 against the baseline methods across both simulation and real-world setups. To ensure an insightful evaluation, the following analysis isolates the physical safety, tracking compliance, and manipulation efficacy of our framework by comparing it directly with the No Residual and Joint-Level PD control benchmarks. 

#### **4.2.1 Simulation Performance Analysis** 





<!-- Start of picture text -->
(a)  Ball Assembly<br>(b)  Stir in Cup<br><!-- End of picture text -->

**Figure 4.** Evaluation of the DexTeleop-0 pipeline via simulation. The same teleoperation trajectory is replayed within IsaacSim with two distinct tasks: (a) Ball Assembly, which requires dynamic grasping and relocation, and (b) Stir in Cup, which demonstrates delicate tool use and precise bimanual trajectories. 

**Table 2.** Simulation Results on Challenging Dexterous Manipulation Tasks 

|**Scene**|**Method**|**Stage 1**|**Stage 2**|**Stage 3**|**Tactile Force**↓**(N)**|
|---|---|---|---|---|---|
||No Residual|99%|10%|4%|31_._58±10_._48|
|Bll A|PD|100%|6%|1%|29_._96±9_._75|
|a ssem.|Force Tracking|84%|78%|78%|11_._03±5_._01|
||DexTeleop-0|100%|98%|97%|11_._15±5_._01|
||No Residual|100%|100%|60%|15_._56±6_._59|
|Stir in Cu|PD|100%|100%|6%|12_._45±5_._28|
|p|Force Tracking|100%|100%|49%|8_._01±2_._50|
||DexTeleop-0|100%|100%|59%|7_._93±2_._67|



As presented in Table 2, DexTeleop-0 exhibits a significant performance advantage in multi-stage execution rates and force regulation. In the contact-rich _Ball Assembly_ task shown in Fig. 4a, 

9 

**Table 3.** Comparison on real robot through challenging dexterous manipulation tasks: Gear Mesh and Peg Insertion 

|**Scene**|**Method**|**Stage 1**|**Stage 2**|**Tactile Force**↓**(N)**|
|---|---|---|---|---|
||No Residual|62.86%|11.43%|2_._12±1_._60|
|G Mh|PD|77.14%|37.14%|2_._20±0_._95|
|ear es|Force Tracking|94.29%|42.86%|2_._42±1_._44|
||DexTeleop-0|97.14%|57.14%|2_._47±1_._07|
||No Residual|74.29%|25.71%|3_._98±2_._12|
|Pe Ins|PD|80.00%|34.29%|3_._68±1_._17|
|g .|Force Tracking|91.43%|62.86%|3_._72±0_._98|
||DexTeleop-0|97.14%|60.00%|5_._17±3_._13|



the No Residual and PD control methods drop drastically after Stage 1, achieving a final Stage 3 completion rate of only 4% and 1%, respectively. This failure stems directly from the tactile and force feedback missing problem; without tracking adjustments, rigid kinematic overrides induce extreme interaction pressures (31 _._ 58 ± 10 _._ 48 N for No Residual), causing the slippery spherical object to blast out of the multi-fingered grasp. In contrast, DexTeleop-0 regulates localized contact pressures to a safe distribution (11 _._ 15 ± 5 _._ 01 N), maintaining a 97% success rate through Stage 3. Fig. 5 illustrates the tactile force profiles and corresponding joint response analysis during the manipulation task. As demonstrated in Fig. 5b, the real-time adjustment of joint position deviations Δ _𝑞_ significantly alleviates contact forces at the fingertip. This active mechanism regulates and balances excessive loading, thereby ensuring safe object interaction and high-quality tactile data collection. In the bimanual _Stir in Cup_ instance illustrated in Fig. 4b, our framework demonstrates a crucial trade-off between absolute tracking precision and physical compliance. While the No Residual approach yields a Stage 3 completion rate that is marginally higher than ours (60% vs. 59%), it achieves this at the expense of severe structural interaction. The No Residual method registers a mean tactile 



<!-- Start of picture text -->
58.7 Tangential Force Normal Force<br>45.9<br>33.0<br>20.1<br>7.2<br>-5.7<br>0.0 1.8 3.6 5.4 7.2 8.9 10.7<br>Time (s)<br>(a)  Thumb Fingertip Tactile Force (No Residual Baseline)<br>29.9 Fx Fy Fz<br>23.3<br>16.7<br>10.1<br>3.5<br>-3.0<br>0.0 1.8 3.6 5.4 7.2 8.9 10.7<br>Time (s)<br>1.2 CMC-AA CMC-FE MCP-AA MCP-FE IP<br>-1.7<br>-4.5<br>-7.4<br>-10.2<br>-13.0<br>0.0 1.8 3.6 5.4 7.2 8.9 10.7<br>Time (s)<br>Force Value<br>Force (N)<br>Delta q (deg)<br><!-- End of picture text -->



<!-- Start of picture text -->
(b)  Tactile Force Components and Joint Angle Adjustments (Ours)<br><!-- End of picture text -->

**Figure 5.** Tactile force profile and joint response analysis during ball assembly dexterous manipulation. (a) Illustrates the normal and tangential force components at the right thumb fingertip under the no residual control scheme. (b) Demonstrates the force values within the identical manipulation task, aligned with the corresponding joint angle adjustment curves displayed below to validate the shared autonomy framework’s active compliance. 

force of 15 _._ 56 ± 6 _._ 59 N, which is twice the pressure exerted by DexTeleop-0 (7 _._ 93 ± 2 _._ 67 N). In physical environments, such high unmitigated interaction forces would result in collision damage, highlighting that DexTeleop-0 prioritizes force-safe compliance while maintaining a highly comparable operational success 

10 

rate. 

#### **4.2.2 Real-Robot Experimental Verification** 





<!-- Start of picture text -->
(a)  Gear Mesh<br>(b)  Peg Insertion<br>(c)  Food Sorting<br>(d)  Tube Operation<br><!-- End of picture text -->

**Figure 6.** Real-world evaluation of dexterous manipulation using DexTeleop-0. Time-series snapshots demonstrate high-precision coordination and robust execution under egocentric vision across four distinct tasks: (a) Gear Mesh, involving tight-tolerance alignment; (b) Peg Insertion, requiring precise peg-to-hole clearance; (c) Food Sorting, demonstrating hemispherical object handling; and (d) Tube Operation, highlighting bimanual coordination. 

The physical hardware experiments validate the real-to-sim generalization capability of our shared autonomy layer during high-precision and long-horizon tasks. For the precision single-arm manipulations documented in Table 3, DexTeleop-0 mitigates tracking errors that typically cause mechanical binding. In the sub-centimeter _Gear Mesh_ task shown in Fig. 6a, our method achieves a Stage 2 assembly success rate of 57.14%, vastly outperforming the No Residual (11.43%) and PD control (37.14%) models. During the _Peg Insertion_ routine demonstrated in Fig. 6b, our system preserves an exceptional Stage 1 capture success rate of 97.14% and a Stage 2 insertion completion rate of 60.00%. While the rigid tracking profiles of the baselines frequently result in parts slipping out of the fingertips due to uncompensated contact vectors, DexTeleop-0 utilizes the operational space Jacobian to modulate the user’s intent into compliant alignment trajectories. Notably, our method does not yield the absolute lowest tactile force across these two tasks. 

11 

This variance is primarily attributed to operator caution, as users adopted conservative manipulation strategies to safeguard the dexterous hand against potential damage. In the coordinated bimanual 

**Table 4.** Comparison on real robot through challenging dexterous manipulation tasks: Food Sorting 

|**Method**|**Stage 1**|**Stage 2**|**Stage 3**|**Stage 4**|**Tactile Force**↓**(N)**|
|---|---|---|---|---|---|
|No Residual|71.43%|51.43%|54.29%|48.57%|6_._92±1_._48|
|PD|65.71%|68.57%|62.86%|51.43%|5_._13±0_._83|
|Force Tracking|82.86%|94.29%|85.71%|57.14%|5_._21±0_._87|
|DexTeleop-0|91.43%|97.14%|82.86%|74.29%|4_._94±1_._80|



**Table 5.** Comparison on real robot through challenging dexterous manipulation tasks: Tube Operation 

|**Method**|**Stage 1**|**Stage 2**|**Stage 3**|**Tactile Force**↓**(N)**|
|---|---|---|---|---|
|No Residual|60.00%|71.43%|34.29%|7_._80±3_._50|
|PD|82.86%|60.00%|25.71%|5_._07±1_._05|
|Force Tracking|91.43%|91.43%|57.14%|4_._72±1_._87|
|DexTeleop-0|94.29%|100.00%|77.14%|6_._87±1_._91|



arenas, the integration of object-centric force-torque balances is paramount. As indicated in the _Food Sorting_ benchmark (Table 4), which requires handling irregular geometries shown in Fig. 6c, DexTeleop-0 maintains the highest end-to-end operational mastery, executing Stage 4 sorting with a 74.29% success rate. Furthermore, our framework archives the lowest overall contact profile (4 _._ 94 ± 1 _._ 80 N), preventing damage to delicate surfaces. Finally, as shown in Table 5, for the long-horizon _Tube Operation_ task outlined in Fig. 6d, DexTeleop-0 displays robust stability during fluid transfer, securing a 100.00% success rate in Stage 2 and a dominant 77.14% completion rate in Stage 3, whereas the position-bound No Residual method drops to 34.29% due to continuous multi-contact distribution mismatching. 

## **5 Conclusion** 

In this work, we introduced a tactile-driven adaptation strategy for bimanual dexterous teleoperation, explicitly designed to mitigate the inherent embodiment gap and low data collection efficiency that plague traditional vision-only tracking pipelines. Instantiated within our full-stack framework, DexTeleop-0, this strategy integrates accessible egocentric tracking from a commercial VR headset with a real-time force-balanced residual optimization loop, coordinating 56 concurrent DoFs across dual arm-hand assemblies. By leveraging a tactile-enabled fingertip force-sensing profile, the closed-loop optimization framework maps coarse human tracking intentions onto a physically compliant manifold. Extensive validation across high-fidelity simulations and physical hardware experiments demonstrates that our tactile-driven adaptation strategy achieves outstanding grasp stability, anti-disturbance compliance, and significantly enhanced task execution efficiency during contact-rich, long-horizon manipulation. The proposed approach drastically reduces destructive physical interaction forces compared to conventional position-bound or decentralized joint-level baselines, all while maintaining precise kinematic fidelity. These findings yield a fundamental insight for high-dimensional embodied manipulation: incorporating localized tactile corrections and physical force-balancing directly into a tracking optimization loop is more critical for closing the embodiment gap and ensuring interaction safety than merely increasing baseline tracking resolution. Future work will focus on integrating predictive slip-detection algorithms to adapt dynamically to unexpected object physical properties. Furthermore, we intend to leverage the high-quality, visual-tactile demonstration trajectories natively collected through DexTeleop-0 to train generalizable imitation learning policies for complex industrial and laboratory assembly tasks. 

12 

## **References** 

- [1] W. Yuan, S. Dong, and E. H. Adelson, “GelSight: High-resolution robot tactile sensors for estimating geometry and force,” _Sensors_ , vol. 17, no. 12, p. 2762, 2017. 

- [2] S. Suresh, H. Qi, T. Wu, T. Fan, L. Pineda, M. Lambeta, J. Malik, M. Kalakrishnan, R. Calandra, M. Kaess, J. Ortiz, and M. Mukadam, “NeuralFeels with neural fields: Visuotactile perception for in-hand manipulation,” _Science Robotics_ , vol. 9, no. 96, p. eadl0628, 2024. 

- [3] Y. Qin, Y.-H. Wu, S. Liu, H. Jiang, R. Yang, Y. Fu, and X. Wang, “DexMV: Imitation learning for dexterous manipulation from human videos,” in _Computer Vision – ECCV 2022_ , vol. 13699 of _Lecture Notes in Computer Science_ , pp. 570–587, Springer, 2022. 

- [4] C. Chi, Z. Xu, C. Pan, E. Cousineau, B. Burchfiel, S. Feng, R. Tedrake, and S. Song, “Universal manipulation interface: In-the-wild robot teaching without in-the-wild robots,” in _Proceedings of Robotics: Science and Systems_ , (Delft, Netherlands), July 2024. 

- [5] C. S. Wang, H. Shi, W. Wang, R. Zhang, L. Fei-Fei, and K. Liu, “Dexcap: Scalable and portable mocap data collection system for dexterous manipulation,” in _Proceedings of Robotics: Science and Systems_ , (Delft, Netherlands), July 2024. 

- [6] P. Wu, Y. Shentu, Z. Yi, X. Lin, and P. Abbeel, “GELLO: A general, low-cost, and intuitive teleoperation framework for robot manipulators,” _arXiv preprint arXiv:2309.13037_ , 2023. 

- [7] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning fine-grained bimanual manipulation with low-cost hardware,” in _Proceedings of Robotics: Science and Systems_ , (Daegu, Republic of Korea), July 2023. 

- [8] S. Yang, M. Liu, Y. Qin, R. Ding, J. Li, X. Cheng, R. Yang, S. Yi, and X. Wang, “Ace: A cross-platform and visual-exoskeletons system for low-cost dexterous teleoperation,” in _Proceedings of The 8th Conference on Robot Learning_ , vol. 270 of _Proceedings of Machine Learning Research_ , pp. 4895–4911, PMLR, 2025. 

- [9] ALOHA 2 Team, J. Aldaco, T. Armstrong, R. Baruch, J. Bingham, S. Chan, K. Draper, D. Dwibedi, C. Finn, P. Florence, S. Goodrich, W. Gramlich, T. Hage, A. Herzog, J. Hoech, T. Nguyen, I. Storz, B. Tabanpour, L. Takayama, J. Tompson, A. Wahid, T. Wahrburg, S. Xu, S. Yaroshenko, K. Zakka, and T. Z. Zhao, “ALOHA 2: An enhanced low-cost hardware for bimanual teleoperation,” _arXiv preprint arXiv:2405.02292_ , 2024. 

- [10] V. Dhat, N. Walker, and M. Cakmak, “Using 3D mice to control robot manipulators,” in _Proceedings of the 2024 ACM/IEEE International Conference on Human-Robot Interaction_ , (New York, NY, USA), pp. 896–900, Association for Computing Machinery, 2024. 

- [11] A. Sivakumar, K. Shaw, and D. Pathak, “Robotic telekinesis: Learning a robotic hand imitator by watching humans on YouTube,” in _Proceedings of Robotics: Science and Systems_ , (New York City, NY, USA), June 2022. 

- [12] Y. Qin, H. Su, and X. Wang, “From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 4, pp. 10873–10881, 2022. 

- [13] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox, “Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system,” in _Proceedings of Robotics: Science and Systems_ , (Daegu, Republic of Korea), July 2023. 

- [14] R. Ding, Y. Qin, J. Zhu, C. Jia, S. Yang, R. Yang, X. Qi, and X. Wang, “Bunny-visionpro: Real-time bimanual dexterous teleoperation for imitation learning,” _arXiv preprint arXiv:2407.03162_ , 2024. 

13 

- [15] X. Cheng, J. Li, S. Yang, G. Yang, and X. Wang, “Open-television: Teleoperation with immersive active visual feedback,” in _Proceedings of The 8th Conference on Robot Learning_ (P. Agrawal, O. Kroemer, and W. Burgard, eds.), vol. 270 of _Proceedings of Machine Learning Research_ , pp. 2729–2749, PMLR, 2025. 

- [16] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, T. Liu, L. Yi, and H. Wang, “UniDexGrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pp. 4737–4746, 2023. 

- [17] H.-S. Fang, H. Yan, Z. Tang, H. Fang, C. Wang, and C. Lu, “Anydexgrasp: General dexterous grasping for different hands with human-level learning efficiency,” _arXiv preprint arXiv:2502.16420_ , 2025. 

- [18] H. Liu, S. Guo, P. Mai, J. Cao, H. Li, and J. Ma, “RoboDexVLM: Visual language model-enabled task planning and motion control for dexterous robot manipulation,” in _Proceedings of the IEEE/RSJ 2025 International Conference on Intelligent Robots and Systems (IROS)_ , pp. 1–8, IEEE, 2025. 

- [19] Z.-H. Yin, C. Wang, L. Pineda, F. Hogan, K. Bodduluri, A. Sharma, P. Lancaster, I. Prasad, M. Kalakrishnan, J. Malik, M. Lambeta, T. Wu, P. Abbeel, and M. Mukadam, “Dexteritygen: Foundation controller for unprecedented dexterity,” _arXiv preprint arXiv:2502.04307_ , 2025. 

- [20] V. Caggiano, S. Dasari, and V. Kumar, “MyoDex: A generalizable prior for dexterous manipulation,” in _Proceedings of the 40th International Conference on Machine Learning_ , vol. 202 of _Proceedings of Machine Learning Research_ , pp. 3327–3346, PMLR, 2023. 

- [21] J. Wang, Y. Qin, K. Kuang, Y. Korkmaz, A. Gurumoorthy, H. Su, and X. Wang, “Cyberdemo: Augmenting simulated human demonstration for real-world dexterous manipulation,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 17952–17963, 2024. 

- [22] Y. Zhong, X. Huang, R. Li, C. Zhang, Z. Chen, T. Guan, F. Zeng, K. N. Lui, Y. Ye, Y. Liang, Y. Yang, and Y. Chen, “DexGraspVLA: A vision-language-action framework towards general dexterous grasping,” in _Proceedings of the AAAI Conference on Artificial Intelligence_ , vol. 40, pp. 18836–18844, 2026. 

- [23] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. C. M. Burchfiel, and S. Song, “Diffusion policy: Visuomotor policy learning via action diffusion,” in _Proceedings of Robotics: Science and Systems_ , (Daegu, Republic of Korea), July 2023. 

- [24] Y. Ze, G. Zhang, K. Zhang, C. Hu, M. Wang, and H. Xu, “3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations,” in _Proceedings of Robotics: Science and Systems_ , (Delft, Netherlands), July 2024. 

- [25] Q. Ye, Q. Liu, S. Wang, J. Chen, Y. Cui, K. Jin, H. Chen, X. Cai, G. Li, and J. Chen, “Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity,” _Science Robotics_ , vol. 11, no. 110, p. eady2869, 2026. 

- [26] H. Xue, J. Ren, W. Chen, G. Zhang, Y. Fang, G. Gu, H. Xu, and C. Lu, “Reactive diffusion policy: Slow-fast visual-tactile policy learning for contact-rich manipulation,” in _Proceedings of Robotics: Science and Systems_ , 2025. 

- [27] Y. Wu, Z. Chen, F. Wu, L. Chen, L. Zhang, Z. Bing, A. Swikir, A. Knoll, and S. Haddadin, “Tacdiffusion: Force-domain diffusion policy for precise tactile manipulation,” _arXiv preprint arXiv:2409.11047_ , 2024. 

14 

- [28] Y. Yuan, H. Che, Y. Qin, B. Huang, Z.-H. Yin, K.-W. Lee, Y. Wu, S.-C. Lim, and X. Wang, “Robot synesthesia: In-hand manipulation with visuotactile sensing,” in _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 6558–6565, 2024. 

- [29] S. Sujit, L. Nunziante, D. O. Lillrank, R. F. J. Dossa, and K. Arulkumaran, “Improving low-cost teleoperation: Augmenting GELLO with force,” _arXiv preprint arXiv:2507.13602_ , 2025. 

- [30] C. Chen, Z. Yu, H. Choi, M. Cutkosky, and J. Bohg, “DexForce: Extracting force-informed actions from kinesthetic demonstrations for dexterous manipulation,” _IEEE Robotics and Automation Letters_ , vol. 10, no. 6, pp. 6416–6423, 2025. 

- [31] A. Handa, K. V. Wyk, W. Yang, J. Liang, Y.-W. Chao, Q. Wan, S. Birchfield, N. D. Ratliff, and D. Fox, “Dexpilot: Vision-based teleoperation of dexterous robotic hand-arm system,” in _2020 IEEE International Conference on Robotics and Automation (ICRA)_ , pp. 9164–9170, IEEE, 2020. 

15 

