# **DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation** 

**Yunchao Yao**<sup>1</sup><sup>_∗_</sup> **Zhuxiu Xu**<sup>1</sup><sup>_,_2</sup><sup>_∗_</sup> **Tianqi Zhang**<sup>1</sup> **Zixian Liu**<sup>1</sup> **Sikai Li**<sup>1</sup> **Zhenyu Wei**<sup>1</sup> **Feng Chen**<sup>2</sup> **Dihong Huang**<sup>1</sup> **Kechang Wan**<sup>1</sup> **Chenyang Ma**<sup>1</sup> **Shuqi Zhao**<sup>3</sup> **Shenghua Gao**<sup>2</sup> **Masayoshi Tomizuka**<sup>3</sup> **Yi Ma**<sup>2</sup> **Mingyu Ding**<sup>1</sup><sup>_†_</sup> 1UNC-Chapel Hill 2The University of Hong Kong 3UC Berkeley 

> _∗_ Equal contribution. _†_ Corresponding author 



Figure 1: Overview of DexVerse, a modular benchmark for multi-task, multi-embodiment dexterous manipulation with diverse tasks, visual variations, demonstration datasets, and baseline evaluations. 

**Abstract:** Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering studies of cross-task and cross-embodiment generalization. We present **DexVerse** , a large-scale and modular benchmark for dexterous manipulation. DexVerse includes 100 tasks spanning a broad range of manipulation skills, including object grasping and relocation, articulated-object interaction, functional tool use, bimanual coordination, nonprehensile control, contact-rich behaviors, multi-goal execution, and long-horizon multi-stage task completion. It supports 3 robot arms and 6 dexterous hands, and is extensible to new tasks, assets, and embodiments. To evaluate visuomotor generalization, DexVerse provides configurable visual variations in textures, background, lighting, and camera viewpoints. We further provide a VR-based teleoperation interface and 3,180 demonstrations with synchronized proprioceptive, RGB, depth, point-cloud, and state observations. We benchmark representative methods, including Diffusion Policy, DP3, OpenVLA, and _π_ 0 _._ 5, across 19 tasks. Results 

reveal substantial challenges in task generalization and visuomotor robustness, establishing DexVerse as a promising testbed for general-purpose dexterous manipulation. Project page: `https://ycyao216.github.io/DexVerse.site/` 

**Keywords:** Dexterous Manipulation, Benchmark Suite, Diverse Tasks 

## **1 Introduction** 

Dexterous manipulation is a central capability for building general-purpose robots [1, 2]. Moving beyond contact-poor, gripper-based manipulation that can often be approximated by reaching, grasping, transporting, and releasing, dexterous manipulation requires coordinated control of highDoF hands and arms under intermittent, contact-rich interactions, while grounding actions in object geometry, visual affordances, force closure, and long-horizon task structure [3, 4]. Recent generalist robot policies have advanced this frontier from several complementary directions: imageconditioned imitation learning, such as action chunking and diffusion policies [5, 6, 7]; scalable demonstration and data generation pipelines [8, 9, 10, 11]; 3D-aware policies that exploit voxel, multi-view, or point-cloud representations [12, 13, 14, 15]; and vision-language-action policies trained on increasingly heterogeneous robot data [16, 17, 18, 19, 20, 21]. Yet it remains unclear how well these methods scale from isolated skills and controlled task distributions to functionally diverse, long-horizon, contact-rich dexterous manipulation across embodiments and environments. 

A key bottleneck is the lack of benchmarks that jointly evaluate the major axes of dexterous generalization. Existing long-horizon manipulation benchmarks such as CALVIN [22], RoboTwin 2.0 [23], ManiSkill3 [24], and LIBERO [25] primarily focus on gripper-based manipulation, while dexterous benchmarks often specialize in narrower settings without expert demonstrations. DexMimicGen [10] focuses on dexterous demonstration generation, Bi-DexHands [26] emphasizes RL-based bimanual dexterous control, DexJoCo [27] studies functionally grounded dexterous tasks, and DexHoldem [28] and DexH2R [29] focus on real-world poker manipulation and dynamic human-torobot handover, respectively. These benchmarks have each advanced the field, but none jointly support broad dexterous tasks, multiple arm-hand embodiments, controllable visual variation, demonstration data, parallel simulation, and representative policy evaluation. This makes it difficult to compare policies across contact regimes, visual conditions, and embodiments. 

We present **DexVerse** , a modular benchmark suite for multi-task, multi-embodiment dexterous manipulation, unifying broad dexterous task coverage, multi-embodiment hand-arm control, modular extensibility, expert demonstrations, parallel RL, and visuomotor generalization. DexVerse includes **100 tasks** spanning a broad range of manipulation skills, including object grasping and relocation, articulated-object manipulation, functional tool use, bimanual coordination, and long-horizon multistage manipulation. The benchmark supports multiple robot arms, including Franka Research 3 [30], UR10e [31] and xArm 7 [32], and multiple dexterous hands, including Sharpa Wave [33], WUJI Hand [34], Shadow Hand [35], Inspire Hand [36], Allegro Hand [37] and LEAP Hand [38], while using reusable task templates and configuration files to add new tasks, assets, embodiments, observation modalities, and action spaces. To evaluate visuomotor generalization, DexVerse provides configurable observation-level variations, including object and scene textures, lighting conditions, and camera viewpoints. 

Together with the benchmark, we release a dataset of **3,180** demonstrations collected via VR teleoperation. Each demonstration contains synchronized proprioceptive, RGB, depth, point-cloud, and simulator state observations, enabling the evaluation of state-based, image-based, and 3D policy learning methods under a unified benchmark setting. We evaluate representative imitation learning and vision-language-action policies, including Diffusion Policy [6], DP3 [15], OpenVLA [19], and _π_ 0 _._ 5 [21], across 19 tasks. The results indicate that DexVerse remains highly challenging for current methods: even the best-performing baselines achieve only **34%** mean online success rate, and no single method consistently dominates across task categories. While some policies can solve selected lifting or articulated-object tasks, they struggle substantially on tool-use and precision tasks, with several tasks receiving zero success from all baselines. These findings demonstrate that DexVerse is 

2 

Table 1: Comparison with representative robot manipulation and dexterous manipulation benchmarks. DexVerse features broad 100 dexterous manipulation tasks, multi-embodiment support, visual variation, and demonstration datasets. ✓: supported; _△_ : partially supported; ✗: not supported. 

|Benchmark|Task Coverage|Dexterous<br>Hand|Bimanual|Multi-<br>Embodiment|Visual<br>Variation|Demo<br>Dataset|Parallel<br>RL Env.|
|---|---|---|---|---|---|---|---|
|CALVIN [22]|34 long-horizon gripper tasks|✗|✗|✗|_△_|✓|✗|
|LIBERO [25]|130 language-conditioned gripper tasks|✗|✗|✗|_△_|✓|✗|
|RoboTwin 2.0 [23]|50 bimanual gripper tasks|✗|✓|✓|✓|✓|_△_|
|ManiSkill3 [24]|diverse general tasks|_△_|_△_|✓|_△_|_△_|✓|
|DexMimicGen [10]|9 bimanual dexterous tasks|✓|✓|✓|✗|✓|✗|
|Bi-DexHands [26]|20 RL bimanual dexterous tasks|✓|✓|✗|✗|✗|✓|
|DexHoldem [28]|14 Texas Hold’em manipulation primitives|✓|✗|✗|_△_|✓|✗|
|DexJoCo [27]|11 task-oriented dexterous tasks|✓|✓|✗|✓|✓|✗|
|**DexVerse (Ours)**|100 diverse dexterous tasks|✓|✓|✓|✓|✓|✓|



not saturated by existing policy learning approaches and highlight open challenges in contact-rich dexterity, fine-grained visuomotor control, and general-purpose robotic manipulation. 

Our contributions are threefold. **1)** We introduce DexVerse, a unified large-scale dexterous manipulation benchmark with 100 tasks spanning diverse interaction patterns, object dynamics, and task horizons, with support for multiple arm-hand embodiments and controllable visual variation. **2)** We develop a VR-based teleoperation interface for collecting dexterous manipulation demonstrations and provide a multi-modal dataset of 3,180 expert demonstrations across diverse tasks and robot embodiments. **3)** We benchmark representative policies on DexVerse and analyze their success rates across different task categories, showing that current policies remain limited on many dexterous manipulation regimes. These results highlight DexVerse as a challenging testbed for developing more general dexterous manipulation policies. 

## **2 Related Works** 

**Dexterous Manipulation Benchmarks.** Robot manipulation benchmarks provide standardized testbeds for multi-task learning, imitation learning, and reinforcement learning. Generalpurpose benchmarks such as Meta-World [39], RLBench [40], ManiSkill [24], CALVIN [22], and LIBERO [25] cover diverse tabletop tasks and demonstration-based learning. However, they mostly rely on parallel-jaw grippers or simple end-effectors, and thus do not fully capture the challenges of dexterous hand-arm manipulation, such as high-dimensional control, contact-rich interactions, and functional object affordances. Recent benchmarks have explored dexterous and bimanual manipulation. DexArt [41] focuses on articulated-object dexterity, Adroit environments [3] support dexterous control and imitation learning, RoboTwin 2.0 [23] studies multi-embodiment bimanual manipulation, and DexMimicGen [10] generates bimanual dexterous demonstrations from limited human data. Most closely related, DexJoCo [27] provides task-oriented dexterous manipulation tasks with human demonstrations and policy evaluation. In contrast, DexVerse offers broader dexterous task coverage, multiple arm-hand embodiments, controllable visual variation, teleoperationcollected demonstrations, and representative policy evaluations in a unified platform. 

**Generalization Across Embodiments and Visual Conditions.** Generalization remains a major challenge for dexterous manipulation policies [42, 43, 44, 41, 45, 46, 47, 48, 49, 50, 51]. Visual changes in textures, lighting, camera viewpoints, backgrounds, and distractors can significantly affect visuomotor policies, motivating domain randomization, visual augmentation, and multi-modal observations [52, 53, 54, 55]. In dexterous manipulation, such visual shifts are especially important because policies must infer object geometry, contact affordances, and task-relevant regions from sensory inputs. Embodiment transfer is also challenging because different arms and hands vary in kinematics, degrees of freedom, workspace, joint limits, and contact geometry; policies or demonstrations for one embodiment may not directly transfer to another without retargeting or embodiment-aware representations [56, 57, 58, 59]. These challenges are often studied separately, but general-purpose dexterous manipulation requires robustness to both sensory changes and embodiment changes. DexVerse is designed to evaluate them in a unified setting by combining multiple 

3 

Table 2: DexVerse taxonomy with 8 categories and 100 tasks. Tasks are grouped by the dominant interaction pattern and manipulation challenge rather than only by object type. 

|Category|#|Representative tasks|Key challenge|
|---|---|---|---|
|Primitive|9|`PickCube`,`StackCube`,<br>`RelocateSphere`,`PushButton`|Direct interaction with simple goals<br>and limited action complexity.|
|Functional|11|`HammerStrike`,`RetrieveCup`,<br>`GraspKettle`,`PourCan`|Affordance-aware interaction with<br>task-relevant object regions.|
|Articulation|18|`OpenStapler`,`OpenLaptop`,<br>`SqueezeScissors`,`OpenPhone`|Controlling object parts and joints,<br>under constrained motion.|
|Non-prehensile|5|`PushT`,`TakeBook`,`PivotCuboid`,<br>`PushSphereObstacle`|Using pushing, sliding, pivoting, or<br>environmental contact.|
|Contact-rich|8|`InsertPeg`,`PlugCharger`,<br>`NutThread`,`InsertGear`|Precise alignment under sustained<br>contact and tight constraints.|
|Bimanual<br>|5|`BiLiftTray`,`BiHandover`,<br>|Coordinated stabilization, transfer, or<br>|
|Coordination||`BiLiftBox`,`BiLiftCart`|cooperative manipulation.|
|Multi-goal|39|`GraspMug + PushButton`,<br>`GraspCan + TurnOnSwitch`|Satisfying multiple goals or<br>compositional objective conditions.|
|Long-horizon|5|`MakeCoffee`,`MicrowaveFood`,<br>`CleanTable`,`OvenBake`|Completing temporally extended<br>multi-stage procedures.|





<!-- Start of picture text -->
Primitive (9)  Articulation (18) Contact-rich (8) Multi-goal (39)<br>Non-prehensile (5) Bimanual Coordination (5) Functional (11)<br><!-- End of picture text -->

Figure 2: Visualization of selected tasks from the DexVerse environments. 

robot arms and dexterous hands with controllable visual variations and synchronized proprioceptive, RGB, depth, point-cloud, and state observations. 

## **3 DexVerse Environment** 

DexVerse is a large-scale modular simulation environment with 100 dexterous manipulation tasks. The task suite covers a broad spectrum of manipulation problems, ranging from primitive and functional object manipulation to non-prehensile and contact-rich interactions, bimanual coordination, multi-goal and long-horizon tasks. Each environment specifies the scene, assets, observation interfaces, initialization distribution, success conditions, and optional visual or physical randomization. 

This design decouples task environments from robot embodiments, supporting diverse task variants and robot configurations within a unified environment framework, while keeping task objectives and evaluation conditions explicit. This section describes the main environment components of DexVerse, including task suite (Sec. 3), modular environment design (Sec. 3.1), robot embodiments (Sec. 3.2), visual variation (Sec. 3.3), and asset sources (Sec. 3.4). 

4 



<!-- Start of picture text -->
Microwave Food Oven Bake<br>Clean Table Make Coffee<br>Cook Food<br><!-- End of picture text -->

Figure 3: Visualization of task progression of the 5 long-horizon tasks in DexVerse environments. 

**Task Suite.** DexVerse contains 100 dexterous manipulation tasks organized into 8 categories: primitive, functional, articulation, non-prehensile, contact-rich, bimanual coordination, multi-goal, and long-horizon tasks. The categories are summarized in Table 2, and representative environments are shown in Figure 2. We categorize the tasks according to the dominant interaction pattern and manipulation challenge, so that the suite covers diverse forms of contact, coordination, object state change, and task temporal structure. 

Each task is specified as _T_ = (Ω _, S_ 0 _, O, A, G_ ), where Ω denotes the interactive objects in the scene, _S_ 0 denotes the initial-state distribution, _O_ and _A_ denote the task observation and action interfaces, and _G_ denotes the task-level success conditions. The success conditions specify when the intended manipulation objective is completed and are implemented as simulator predicates. Together with the observation and action interfaces, they define the concrete environment used by a policy. 

The task suite is designed to cover complementary dexterous manipulation challenges. Primitive and functional tasks evaluate basic object interaction and affordance-aware manipulation. Articulation, non-prehensile, and contact-rich tasks emphasize contact regulation, constraint exploitation, and precise interaction with object geometry or articulated structure. Bimanual coordination tasks introduce coordination requirements across two hands or arms, while multi-goal and long-horizon tasks extend the suite beyond isolated skills by requiring policies to satisfy multiple objectives or complete temporally extended procedures (Figure 3). This taxonomy supports category-level analysis across manipulation regimes, while the complete task list, initialization ranges, object assets, and success thresholds are provided in the supplementary material. 

### **3.1 Modular Environment Design** 

DexVerse uses a configuration-driven design to **Main Base Task Family Base Task** specify and instantiate manipulation environ- **Environment Environment Environment** ments. Each environment is defined by a set Defines the common tabletop structure, utilities, and interfaces. overrideInherit Specializes the shared scaffold and sets family-level defaults. overrideInherit Overrides task-specific components. of structured components, including the scene ●Table Spawn **Articulation** ●Object Type: Scissor **SqueezeScissor** ●Camera Configurations ●Object half height layout, object assets, robot embodiment, obser●Proprioceptions●Domain Randomizations ●●Object Spawn ConfigTarget Joint Name ●… vation and action interfaces, initialization rules, ●… ●Success Threshold●… **OpenLaptop** ●Object Type: Laptop success conditions, and randomization settings. ●Initial Joint Angle●… Tasks within the same family share reusable **IsaacLab Functional** templates for common logic such as asset load- **RL EnvironmentManager-Based Contact-rich HammerStrike** ing, state initialization, reset events, and success Exposes Gym API for RL integration **GraspKettle** checking, while task-specific parameters define Figure 4: Modular Environment Architecture the manipulated objects, target states, sampling ranges, and completion thresholds. This design reduces duplicated implementation across related environments and makes task variants easier to construct and maintain, as illustrated in Fig. 4. 

DexVerse builds on the manager-based environment interface of Isaac Lab, where observations, actions, events, terminations, and optional reward terms are specified through configuration classes 

5 



<!-- Start of picture text -->
Embodiment variations Visual Variations<br>(a) (b)<br><!-- End of picture text -->

Figure 5: Visual demonstration of embodiments and visual variation. 

and executed by a shared simulation loop. Most environment parameters can be adjusted through configuration overrides, enabling controlled changes to initialization ranges, camera settings, randomization options, or success thresholds without modifying the core environment code. For robot embodiments, DexVerse additionally provides a compact specification for selecting arm-hand combinations, simplifying the instantiation of feasible embodiment variants. 

### **3.2 Robot Embodiments** 

DexVerse specifies each robot embodiment through a robot configuration, which defines the arm and hand models, initial pose, action interface, controller parameters, and embodiment-specific constants. As long as a robot implements the required interface, it can be instantiated in a task without rewriting the task-specific environment logic. For physically feasible task-embodiment combinations, users can override the default robot choice, such as replacing a single-arm setup with a bimanual setup or switching to a different arm-hand pair. 

The current benchmark supports 3 robot arms (Franka Research 3, UR10e, and xArm 7) and 6 dexterous hands (Sharpa Wave, WUJI Hand, Shadow Hand, Inspire Hand, Allegro Hand, and LEAP Hand), covering diverse kinematics, degrees of freedom, joint limits, actuation ranges, and hand morphologies. Figure 5a shows the supported arm-hand combinations. Each hand also has a floating variant, where the wrist is directly controlled by prismatic and revolute joints. Detailed embodiment specifications are provided in the supplementary material. 

### **3.3 Visual Variation** 

DexVerse provides configurable visual variation as part of its environment specification. Each environment uses a fixed default appearance when visual randomization is disabled. When enabled, visual properties are sampled at reset from predefined libraries, including object materials, table materials, lighting conditions, background skyboxes, exposure, and color-temperature settings. DexVerse also supports camera-viewpoint changes, allowing the same task to appear under different observation conditions while preserving the task objective and success conditions. Fig. 5b illustrates representative visual randomizations. 

Beyond visual variation, DexVerse also supports non-visual variations, including object initial poses, task sampling ranges, proprioceptive and object-state perturbations, and dynamics parameters. Visual and non-visual variations can be enabled independently or jointly, making appearance changes explicit while preserving standard environment variability for manipulation tasks. 

### **3.4 Asset Sources** 

DexVerse combines assets from research datasets, simulation libraries, public 3D repositories, and image-to-3D generation tools. Rigid and articulated objects are drawn from PartNet-Mobility [60], ManiTwin [61], NVIDIA Isaac Lab/Isaac Sim assets [62, 63], AutoBio [64] and publicly available 

6 

Synthesis assets [65]; when suitable objects are not available, we generate candidate meshes from reference images using Meshy [66] and manually process them for simulation. For visual variation, DexVerse uses 100 HDR skyboxes from Poly Haven [67] and table material randomization from Isaac Lab/Isaac Sim assets [63]. These assets provide diverse object geometries and scene appearances while keeping task construction consistent across the benchmark. 

## **4 Dataset and Evaluation** 

**Teleoperation Data Collection.** We develop an embodimentadaptive teleoperation pipeline to scale demonstration collection in DexVerse. The system uses Apple Vision Pro through Isaac Lab’s CloudXR-based XR teleoperation interface [62], which streams simulation feedback to the headset and returns hand-tracking inputs for robot control. The tracked human wrist pose is used as the target pose for the robot end-effector, and the robot arm follows this target through an inverse-kinematics controller. Human hand motion is converted into target joint poses for different dexterous hands using optimization-based dex-retargeting [68] (Figure 6). 



Figure 6: Teleoperation data collection system. 

The pipeline is designed to reduce embodiment-specific changes when adapting to new arm-hand platforms. Adding new robot arms typically requires updating the end-effector frame, initial poses, and low-level controller parameters, while adding dexterous hands requires configuring the hand URDF with necessary keypoints, correspondence links, and retargeting scales. 

**Dataset Statistics.** DexVerse provides teleoperation demonstrations for most of the task suites. For each of the 56 single-goal tasks, we collect 55 demonstrations: 50 with the Shadow Hand and one with each of the other five hand embodiments. For each of the 5 long-horizon tasks, we collect 20 demonstrations. This results in a total of 3,180 demonstration trajectories. 

Each demonstration is stored as a sequence of action-state pairs recorded during teleoperation. We provide the replay utility that restores the recorded simulator states and queries the environment locally to regenerate the requested observation terms. This design is important because physics simulation can diverge across machines due to differences in physics computation, hardware, and floating-point rounding. Direct state replay avoids accumulated rollout drift and makes demonstrations more portable across local setups. 

The action-state format also keeps the dataset compact. The replay mechanism also makes modifying observation presets, adding observation terms, or changing camera-based inputs more flexible without requiring a separate copy of the demonstration dataset. 

### **4.1 Imitation Learning Policy Evaluation** 

We evaluate four open-source imitation-learning policy families on the DexVerse baseline split: two vision-language-action (VLA) transformers fine-tuned from internet-scale pretrained backbones: _π_ 0 _._ 5 [21] and OpenVLA [19], and two from-scratch diffusion policies: Diffusion Policy (DP) [6] and 3D Diffusion Policy (DP3) [15]. All four methods are trained using the same set of 950 episodes (19 tasks × 50 episodes per task) of the DexVerse teleoperation corpus, and evaluated closed-loop in the same simulator under identical termination criteria. 

**Results.** For every task we roll out 50 episodes and report the mean success rate. Table 3 summarizes the per-task results. DP3 ties _π_ 0 _._ 5 for the highest overall success rate (0.34), ahead of DP (0.32) and OpenVLA (0.19). The aggregate ranking is close, but the per-skill profiles diverge: DP is strongest on simple Pick-and-Lift, DP3 on Tool Use where point-cloud inputs help disambiguate object geometry, and _π_ 0 _._ 5 on Precision Contact, the same category where OpenVLA falls behind. We highlight three findings. 

**1) Internet-scale VLA pretraining does not yet translate into a dexterous-manipulation advantage.** Despite being initialized from web-scale pretrained backbones, the stronger VLA ( _π_ 0 _._ 5, 0.34) 

7 

Table 3: Imitation learning baselines’ online success rates on DexVerse baseline tasks. 

|Task Characteristics|Task|Pi0.5|OpenVLA|3D Diffusion Policy|Diffusion Policy|
|---|---|---|---|---|---|
||BimanualLiftCarton|**1.00**|0.60|0.90|0.94|
||BimanualLiftTray|**0.84**|0.72|0.56|0.60|
||GraspBleach|0.10|0.06|**0.32**|0.10|
|Pick-and-Lift|GraspCup|0.16|0.08|0.22|**0.50**|
||GraspKettle|0.58|0.16|0.80|**0.90**|
||GraspPan|0.06|0.02|0.16|**0.52**|
||RetrieveCup|0.02|0.02|**0.06**|0.04|
||OpenFaucet|**0.84**|0.36|0.76|0.28|
||OpenFlatFolder|0.00|0.00|**0.18**|0.16|
|Aild|OpenLaptop|0.04|0.02|0.02|**0.10**|
|rtcuate|OpenStapler|0.86|**0.92**|0.84|0.86|
||SlideUtilityKnife|0.00|0.00|0.00|0.00|
||SqueezeScissors|**0.36**|0.22|0.20|0.00|
||FunctionalHammerStrike|0.22|0.18|**0.26**|0.00|
|Tool Use|FunctionalPourCan|0.04|0.10|0.14|**0.38**|
||FunctionalPourMug|0.52|0.16|**0.64**|0.26|
||InsertPen|0.06|0.00|**0.08**|0.00|
|Precision|PushSmallSphereObstacleSlope|**0.82**|0.08|0.28|0.36|
||PushT|0.00|0.00|0.00|0.00|
|Mean||**0.34**|0.19|**0.34**|0.32|



only matches the best from-scratch policy (DP3, 0.34), while OpenVLA (0.19) trails both diffusion baselines. We attribute this to the gap between the pretraining distribution and the target embodiment: the priors carried by these backbones come from web images and low-DoF action spaces, which transfer to perception but not to the high-DoF multifinger control manifold of DexVerse. 

**2) The most informative observation modality is skill-dependent, and no single representation dominates.** DP is strongest on Pick-and-Lift (0.51), where a successful grasp pose is largely a function of object appearance, and a 2D image plus low-dimensional state already suffices. 3D DP leads on Functional Tool Use (0.35), where explicit point-cloud geometry helps localize the tool tip and regulate the pour/strike pose. _π_ 0 _._ 5 leads on both Articulated-object Manipulation (0.35) and Precision Contact (0.29), where language conditioning and a flow-matching action expert help disambiguate multi-stage subgoals and contact timing. This spread, a different method wins each of the four skill families, motivates DexVerse’s multi-modal observation interface rather than committing to a single sensing paradigm. 

**3) Fine contact reasoning and sub-centimeter alignment remain unsolved across the board.** Tight-tolerance tasks collapse for every method: PushT is 0.00 for all four policies, and InsertPen, SlideUtilityKnife, and OpenLaptop stay at or near zero everywhere. These tasks demand sustained force regulation and sub-centimeter alignment that behavior cloning without explicit force feedback or closed-loop contact correction cannot yet provide, and they constitute the principal headroom that DexVerse exposes for future imitation-learning research. 

## **5 Conclusion** 

We presented DexVerse, a modular benchmark for multi-task, multi-embodiment dexterous manipulation that unifies diverse task categories, multiple arm-hand embodiments, configurable visual variation, VR-based teleoperation, multi-modal demonstrations, and representative policy evaluation. Our experiments show that current imitation-learning and vision-language-action policies remain far from solving general dexterous manipulation, particularly for precise contact, bimanual coordination, functional tool use, and robust interaction with complex objects. These findings establish DexVerse as a challenging and extensible testbed for studying contact-rich dexterous control, visuomotor robustness, and embodiment-aware robot learning. 

**Limitation and Future Work.** The current release focuses on building a broad, reproducible, and multi-task, multi-embodiment benchmark. Future extensions will study real-robot transfer, expand demonstrations across more embodiments and task families, and provide broader standardization for cross-task and cross-embodiment evaluation. These directions will further strengthen DexVerse as a foundation for developing general, robust, and transferable dexterous manipulation policies. 

8 

## **References** 

- [1] O. Kroemer, S. Niekum, and G. Konidaris. A review of robot learning for manipulation: Challenges, representations, and algorithms, 2020. URL `https://arxiv.org/abs/1907. 03146` . 

- [2] A. Billard and D. Kragic. Trends and challenges in robot manipulation. _Science_ , 364(6446): eaat8414, 2019. doi:10.1126/science.aat8414. URL `https://www.science.org/doi/abs/ 10.1126/science.aat8414` . 

- [3] A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine. Learning complex dexterous manipulation with deep reinforcement learning and demonstrations. _arXiv preprint arXiv:1709.10087_ , 2017. 

- [4] M. Suomalainen, Y. Karayiannidis, and V. Kyrki. A survey of robot manipulation in contact. _Robotics and Autonomous Systems_ , 156:104224, 2022. ISSN 0921-8890. doi:https:// doi.org/10.1016/j.robot.2022.104224. URL `https://www.sciencedirect.com/science/ article/pii/S0921889022001312` . 

- [5] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning fine-grained bimanual manipulation with low-cost hardware. _arXiv preprint arXiv:2304.13705_ , 2023. 

- [6] C. Chi, Z. Xu, S. Feng, E. Cousineau, Y. Du, B. Burchfiel, R. Tedrake, and S. Song. Diffusion policy: Visuomotor policy learning via action diffusion. _The International Journal of Robotics Research_ , 44(10-11):1684–1704, 2025. 

- [7] D. Jing, G. Wang, J. Liu, W. Tang, Z. Sun, Y. Yao, Z. Wei, Y. Liu, Z. Lu, and M. Ding. Mixture of horizons in action chunking. _arXiv preprint arXiv:2511.19433_ , 2025. 

- [8] A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Mart´ın-Mart´ın. What matters in learning from offline human demonstrations for robot manipulation. In _arXiv preprint arXiv:2108.03298_ , 2021. 

- [9] A. Mandlekar, S. Nasiriany, B. Wen, I. Akinola, Y. Narang, L. Fan, Y. Zhu, and D. Fox. Mimicgen: A data generation system for scalable robot learning using human demonstrations. In _7th Annual Conference on Robot Learning_ , 2023. 

- [10] Z. Jiang, Y. Xie, K. Lin, Z. Xu, W. Wan, A. Mandlekar, L. Fan, and Y. Zhu. Dexmimicgen: Automated data generation for bimanual dexterous manipulation via imitation learning. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025. 

- [11] Y. Wang, Z. Xian, F. Chen, T.-H. Wang, Y. Wang, K. Fragkiadaki, Z. Erickson, D. Held, and C. Gan. Robogen: Towards unleashing infinite data for automated robot learning via generative simulation, 2024. URL `https://arxiv.org/abs/2311.01455` . 

- [12] M. Shridhar, L. Manuelli, and D. Fox. Perceiver-actor: A multi-task transformer for robotic manipulation. In _Proceedings of the 6th Conference on Robot Learning (CoRL)_ , 2022. 

- [13] A. Goyal, J. Xu, Y. Guo, V. Blukis, Y.-W. Chao, and D. Fox. Rvt: Robotic view transformer for 3d object manipulation. _arXiv:2306.14896_ , 2023. 

- [14] A. Goyal, V. Blukis, J. Xu, Y. Guo, Y.-W. Chao, and D. Fox. Rvt2: Learning precise manipulation from few demonstrations. _RSS_ , 2024. 

- [15] Y. Ze, G. Zhang, K. Zhang, C. Hu, M. Wang, and H. Xu. 3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations. In _Proceedings of Robotics: Science and Systems (RSS)_ , 2024. 

9 

- [16] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, T. Jackson, S. Jesmonth, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, K.-H. Lee, S. Levine, Y. Lu, U. Malla, D. Manjunath, I. Mordatch, O. Nachum, C. Parada, J. Peralta, E. Perez, K. Pertsch, J. Quiambao, K. Rao, M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran, V. Vanhoucke, S. Vega, Q. Vuong, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. Rt1: Robotics transformer for real-world control at scale. In _arXiv preprint arXiv:2212.06817_ , 2022. 

- [17] E. Collaboration, A. O’Neill, A. Rehman, A. Gupta, A. Maddukuri, A. Gupta, A. Padalkar, A. Lee, A. Pooley, A. Gupta, A. Mandlekar, A. Jain, A. Tung, A. Bewley, A. Herzog, A. Irpan, A. Khazatsky, A. Rai, A. Gupta, A. Wang, A. Kolobov, A. Singh, A. Garg, A. Kembhavi, A. Xie, A. Brohan, A. Raffin, A. Sharma, A. Yavary, A. Jain, A. Balakrishna, A. Wahid, B. Burgess-Limerick, B. Kim, B. Sch¨olkopf, B. Wulfe, B. Ichter, C. Lu, C. Xu, C. Le, C. Finn, C. Wang, C. Xu, C. Chi, C. Huang, C. Chan, C. Agia, C. Pan, C. Fu, C. Devin, D. Xu, D. Morton, D. Driess, D. Chen, D. Pathak, D. Shah, D. B¨uchler, D. Jayaraman, D. Kalashnikov, D. Sadigh, E. Johns, E. Foster, F. Liu, F. Ceola, F. Xia, F. Zhao, F. V. Frujeri, F. Stulp, G. Zhou, G. S. Sukhatme, G. Salhotra, G. Yan, G. Feng, G. Schiavi, G. Berseth, G. Kahn, G. Yang, G. Wang, H. Su, H.-S. Fang, H. Shi, H. Bao, H. B. Amor, H. I. Christensen, H. Furuta, H. Bharadhwaj, H. Walke, H. Fang, H. Ha, I. Mordatch, I. Radosavovic, I. Leal, J. Liang, J. Abou-Chakra, J. Kim, J. Drake, J. Peters, J. Schneider, J. Hsu, J. Vakil, J. Bohg, J. Bingham, J. Wu, J. Gao, J. Hu, J. Wu, J. Wu, J. Sun, J. Luo, J. Gu, J. Tan, J. Oh, J. Wu, J. Lu, J. Yang, J. Malik, J. Silv´erio, J. Hejna, J. Booher, J. Tompson, J. Yang, J. Salvador, J. J. Lim, J. Han, K. Wang, K. Rao, K. Pertsch, K. Hausman, K. Go, K. Gopalakrishnan, K. Goldberg, K. Byrne, K. Oslund, K. Kawaharazuka, K. Black, K. Lin, K. Zhang, K. Ehsani, K. Lekkala, K. Ellis, K. Rana, K. Srinivasan, K. Fang, K. P. Singh, K.-H. Zeng, K. Hatch, K. Hsu, L. Itti, L. Y. Chen, L. Pinto, L. Fei-Fei, L. Tan, L. J. Fan, L. Ott, L. Lee, L. Weihs, M. Chen, M. Lepert, M. Memmel, M. Tomizuka, M. Itkina, M. G. Castro, M. Spero, M. Du, M. Ahn, M. C. Yip, M. Zhang, M. Ding, M. Heo, M. K. Srirama, M. Sharma, M. J. Kim, M. Z. Irshad, N. Kanazawa, N. Hansen, N. Heess, N. J. Joshi, N. Suenderhauf, N. Liu, N. D. Palo, N. M. M. Shafiullah, O. Mees, O. Kroemer, O. Bastani, P. R. Sanketi, P. T. Miller, P. Yin, P. Wohlhart, P. Xu, P. D. Fagan, P. Mitrano, P. Sermanet, P. Abbeel, P. Sundaresan, Q. Chen, Q. Vuong, R. Rafailov, R. Tian, R. Doshi, R. Mart´ın-Mart´ın, R. Baijal, R. Scalise, R. Hendrix, R. Lin, R. Qian, R. Zhang, R. Mendonca, R. Shah, R. Hoque, R. Julian, S. Bustamante, S. Kirmani, S. Levine, S. Lin, S. Moore, S. Bahl, S. Dass, S. Sonawani, S. Tulsiani, S. Song, S. Xu, S. Haldar, S. Karamcheti, S. Adebola, S. Guist, S. Nasiriany, S. Schaal, S. Welker, S. Tian, S. Ramamoorthy, S. Dasari, S. Belkhale, S. Park, S. Nair, S. Mirchandani, T. Osa, T. Gupta, T. Harada, T. Matsushima, T. Xiao, T. Kollar, T. Yu, T. Ding, T. Davchev, T. Z. Zhao, T. Armstrong, T. Darrell, T. Chung, V. Jain, V. Kumar, V. Vanhoucke, V. Guizilini, W. Zhan, W. Zhou, W. Burgard, X. Chen, X. Chen, X. Wang, X. Zhu, X. Geng, X. Liu, X. Liangwei, X. Li, Y. Pang, Y. Lu, Y. J. Ma, Y. Kim, Y. Chebotar, Y. Zhou, Y. Zhu, Y. Wu, Y. Xu, Y. Wang, Y. Bisk, Y. Dou, Y. Cho, Y. Lee, Y. Cui, Y. Cao, Y.-H. Wu, Y. Tang, Y. Zhu, Y. Zhang, Y. Jiang, Y. Li, Y. Li, Y. Iwasawa, Y. Matsuo, Z. Ma, Z. Xu, Z. J. Cui, Z. Zhang, Z. Fu, and Z. Lin. Open x-embodiment: Robotic learning datasets and rt-x models, 2025. URL `https://arxiv.org/abs/2310.08864` . 

- [18] Octo Model Team, D. Ghosh, H. Walke, K. Pertsch, K. Black, O. Mees, S. Dasari, J. Hejna, C. Xu, J. Luo, T. Kreiman, Y. Tan, L. Y. Chen, P. Sanketi, Q. Vuong, T. Xiao, D. Sadigh, C. Finn, and S. Levine. Octo: An open-source generalist robot policy. In _Proceedings of Robotics: Science and Systems_ , Delft, Netherlands, 2024. 

- [19] M. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster, G. Lam, P. Sanketi, Q. Vuong, T. Kollar, B. Burchfiel, R. Tedrake, D. Sadigh, S. Levine, P. Liang, and C. Finn. Openvla: An open-source vision-language-action model. _arXiv preprint arXiv:2406.09246_ , 2024. 

10 

- [20] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, et al. _π_ 0: A vision-language-action flow model for general robot control. _arXiv preprint arXiv:2410.24164_ , 2024. 

- [21] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, et al. _π_ 0 _._ 5: a vision-language-action model with open-world generalization. _arXiv preprint arXiv:2504.16054_ , 2025. 

- [22] O. Mees, L. Hermann, E. Rosete-Beas, and W. Burgard. Calvin: A benchmark for languageconditioned policy learning for long-horizon robot manipulation tasks. _IEEE Robotics and Automation Letters (RA-L)_ , 7(3):7327–7334, 2022. 

- [23] T. Chen, Z. Chen, B. Chen, Z. Cai, Y. Liu, Z. Li, Q. Liang, X. Lin, Y. Ge, Z. Gu, et al. Robotwin 2.0: A scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation. _arXiv preprint arXiv:2506.18088_ , 2025. 

- [24] S. Tao, F. Xiang, A. Shukla, Y. Qin, X. Hinrichsen, X. Yuan, C. Bao, X. Lin, Y. Liu, T. kai Chan, Y. Gao, X. Li, T. Mu, N. Xiao, A. Gurha, V. N. Rajesh, Y. W. Choi, Y.-R. Chen, Z. Huang, R. Calandra, R. Chen, S. Luo, and H. Su. Maniskill3: Gpu parallelized robotics simulation and rendering for generalizable embodied ai. _Robotics: Science and Systems_ , 2025. 

- [25] B. Liu, Y. Zhu, C. Gao, Y. Feng, Q. Liu, Y. Zhu, and P. Stone. Libero: Benchmarking knowledge transfer for lifelong robot learning. _arXiv preprint arXiv:2306.03310_ , 2023. 

- [26] Y. Chen, Y. Yang, T. Wu, S. Wang, X. Feng, J. Jiang, Z. Lu, S. M. McAleer, H. Dong, and S.-C. Zhu. Towards human-level bimanual dexterous manipulation with reinforcement learning. In _Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track_ , 2022. URL `https://openreview.net/forum?id=D29JbExncTP` . 

- [27] H. Wang, W. Zhao, X. Wang, S. Huang, H. Lin, B. Zheng, R. Xu, G. Wang, Y. Mu, H. Wang, L. Fan, H. Li, Z. Zhang, and T. Tan. Dexjoco: A benchmark and toolkit for task-oriented dexterous manipulation on mujoco, 2026. URL `https://arxiv.org/abs/2605.16257` . 

- [28] F. Chen, T. Chu, L. Sun, P. Zhou, Z. Xu, S. Gao, Y. Zhai, Y. Yang, and Y. Ma. Dexholdem: Playing texas hold’em with dexterous embodied system, 2026. URL `https://arxiv.org/ abs/2605.18727` . 

- [29] Y. Wang, J. Ye, C. Xiao, Y. Zhong, H. Tao, H. Yu, Y. Liu, J. Yu, and Y. Ma. Dexh2r: A benchmark for dynamic dexterous grasping in human-to-robot handover, 2025. URL `https: //arxiv.org/abs/2506.23152` . 

- [30] Franka Robotics. Franka research 3. `https://franka.de/franka-research-3` , 2026. Accessed: 2026-05-22. 

- [31] Universal Robots. _UR10e Technical Specification_ , 2024. Accessed: 2026-05-22. 

- [32] UFACTORY. _xArm User Manual_ , 2023. Accessed: 2026-05-22. 

- [33] Sharpa Robotics. Sharpa wave. `https://www.sharpa.com/pages/wave` , 2026. Accessed: 2026-05-22. 

- [34] WUJI TECH. _WUJI Hand Product Introduction_ , 2026. Accessed: 2026-05-22. 

- [35] Shadow Robot Company. Shadow dexterous hand series. `https://shadowrobot.com/ dexterous-hand-series/` , 2026. Accessed: 2026-05-22. 

- [36] Inspire Robots. The dexterous hands. `https://en.inspire-robots.com/ product-category/the-dexterous-hands` , 2026. Accessed: 2026-05-22. 

11 

- [37] Allegro Hand. Allegro hand. `https://www.allegrohand.com/` , 2026. Accessed: 2026-0522. 

- [38] K. Shaw, A. Agarwal, and D. Pathak. Leap hand: Low-cost, efficient, and anthropomorphic hand for robot learning. _arXiv preprint arXiv:2309.06440_ , 2023. 

- [39] R. McLean, E. Chatzaroulas, L. McCutcheon, F. R¨oder, T. Yu, Z. He, K. Zentner, R. Julian, J. K. Terry, I. Woungang, N. Farsad, and P. S. Castro. Meta-world+: An improved, standardized, RL benchmark. In _The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track_ , 2025. URL `https://openreview.net/ forum?id=1de3azE606` . 

- [40] S. James, Z. Ma, D. Rovick Arrojo, and A. J. Davison. Rlbench: The robot learning benchmark & learning environment. _IEEE Robotics and Automation Letters_ , 2020. 

- [41] C. Bao, H. Xu, Y. Qin, and X. Wang. DexArt: Benchmarking generalizable dexterous manipulation with articulated objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21190–21200, 2023. 

- [42] D. Huang, Z. Wei, Z. Xu, Y. Yao, S. Li, and M. Ding. Dexcompose: Reusing dexterous policies for multi-task manipulation with a single hand. _arXiv preprint arXiv:2606.28323_ , 2026. 

- [43] S. Li, S. Li, Z. Wei, Y. Yao, C. Li, and M. Ding. Coordex: Coordinating body and hand priors for continuous dexterous humanoid loco-manipulation. _arXiv preprint arXiv:2606.23680_ , 2026. 

- [44] Z. Liang, Y. Mu, Y. Wang, T. Chen, W. Shao, W. Zhan, M. Tomizuka, P. Luo, and M. Ding. Dexhanddiff: Interaction-aware diffusion planning for adaptive dexterous manipulation. In _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pages 1745–1755, 2025. 

- [45] R. Wang, J. Zhang, J. Chen, Y. Xu, P. Li, T. Liu, and H. Wang. Dexgraspnet: A large-scale robotic dexterous grasp dataset for general objects based on simulation. In _2023 IEEE International Conference on Robotics and Automation_ , pages 11359–11366, 2023. 

- [46] Y. Xu, W. Wan, J. Zhang, H. Liu, Z. Shan, H. Shen, R. Wang, H. Geng, Y. Weng, J. Chen, T. Liu, L. Yi, and H. Wang. UniDexGrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 4737–4746, 2023. 

- [47] W. Wan, H. Geng, Y. Liu, Z. Shan, Y. Yang, L. Yi, and H. Wang. UniDexGrasp++: Improving dexterous grasping policy learning via geometry-aware curriculum and iterative generalistspecialist learning. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ , pages 3891–3902, 2023. 

- [48] J. Zhang, H. Liu, D. Li, X. Yu, H. Geng, Y. Ding, J. Chen, and H. Wang. Dexgraspnet 2.0: Learning generative dexterous grasping in large-scale synthetic cluttered scenes. In _Proceedings of the 8th Conference on Robot Learning_ , volume 270 of _Proceedings of Machine Learning Research_ . PMLR, 2025. 

- [49] G. Zhang, Q. Xu, H. Zhang, J. Ma, L. He, Y. Bao, Z. Ping, Z. Yuan, C. Lu, C. Yuan, et al. Unidex: A robot foundation suite for universal dexterous hand control from egocentric human videos. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 1841–1852, 2026. 

- [50] S. Zhao, X. Zhu, Y. Chen, C. Li, Y. Xie, X. Zhang, M. Ding, and M. Tomizuka. Dexh2r: Task-oriented dexterous manipulation from human to robots. _IEEE/ASME Transactions on Mechatronics_ , 2025. 

12 

- [51] C. Ma, Y. Yao, Z. Wei, R. Li, D. Szafir, and M. Ding. Current as touch: Proprioceptive contact feedback for compliant dexterous manipulation. _arXiv preprint arXiv:2607.03529_ , 2026. 

- [52] K. Lei, H. Li, D. Yu, Z. Wei, L. Guo, Z. Jiang, Z. Wang, S. Liang, and H. Xu. Rl100: Performant robotic manipulation with real-world reinforcement learning. _arXiv preprint arXiv:2510.14830_ , 2025. 

- [53] J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. In _2017 IEEE/RSJ international conference on intelligent robots and systems (IROS)_ , pages 23–30. IEEE, 2017. 

- [54] Y. Zhu, Z. Jiang, P. Stone, and Y. Zhu. Learning generalizable manipulation policies with object-centric 3d representations. _arXiv preprint arXiv:2310.14386_ , 2023. 

- [55] O. M. Andrychowicz, B. Baker, M. Chociej, R. Jozefowicz, B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell, A. Ray, et al. Learning dexterous in-hand manipulation. _The International Journal of Robotics Research_ , 39(1):3–20, 2020. 

- [56] Z. Wei, Z. Xu, J. Guo, Y. Hou, C. Gao, Z. Cai, J. Luo, and L. Shao. _D_ ( _R, O_ ) grasp: A unified representation of robot and object interaction for cross-embodiment dexterous grasping. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 4982–4988, 2025. doi:10.1109/ICRA55743.2025.11127754. 

- [57] R. Doshi, H. Walke, O. Mees, S. Dasari, and S. Levine. Scaling cross-embodied learning: One policy for manipulation, navigation, locomotion and aviation. _arXiv preprint arXiv:2408.11812_ , 2024. 

- [58] P. Li, T. Liu, Y. Li, Y. Zhu, Y. Yang, and S. Huang. Gendexgrasp: Generalizable dexterous grasping. _arXiv preprint arXiv:2210.00722_ , 2022. 

- [59] Z. Wei, Y. Yao, and M. Ding. One hand to rule them all: Canonical representations for unified dexterous manipulation. _arXiv preprint arXiv:2602.16712_ , 2026. 

- [60] F. Xiang, Y. Qin, K. Mo, Y. Xia, H. Zhu, F. Liu, M. Liu, H. Jiang, Y. Yuan, H. Wang, L. Yi, A. X. Chang, L. J. Guibas, and H. Su. SAPIEN: A simulated part-based interactive environment. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2020. 

- [61] K. Wang, T. Chen, J. Liu, H. Su, S. Zhu, M. Wang, Z. Li, Y. Chen, H.-a. Gao, Y. Qin, J. Wang, Q. Zhang, L. Xu, J. Yu, Y. Mu, and P. Luo. ManiTwin: Scaling data-generation-ready digital object dataset to 100k. _arXiv preprint arXiv:2603.16866_ , 2026. 

- [62] M. Mittal, P. Roth, J. Tigue, et al. Isaac Lab: A gpu-accelerated simulation framework for multi-modal robot learning. _arXiv preprint arXiv:2511.04831_ , 2025. 

- [63] NVIDIA. Isaac Sim Assets. `https://docs.isaacsim.omniverse.nvidia.com/latest/ assets/usd_assets_overview.html` , 2026. Accessed: 2026-05-28. 

- [64] Z. Lan, Y. Jiang, R. Wang, X. Xie, R. Zhang, Y. Zhu, P. Li, T. Yang, T. Chen, H. Gao, X. Yang, X. Li, H. Zhang, Y. Mu, and P. Luo. Autobio: A simulation and benchmark for robotic automation in digital biology laboratory, 2025. URL `https://arxiv.org/abs/2505.14030` . 

- [65] Extwin. Synthesis Sim-Ready Assets. `https://huggingface.co/datasets/Extwin/ Synthesis-Sim-Ready-Assets` , 2025. Accessed: 2026-05-28. 

- [66] Meshy. Meshy Image to 3D API. `https://docs.meshy.ai/en/api/image-to-3d` , 2026. Accessed: 2026-05-28. 

- [67] Poly Haven. Poly Haven HDRIs. `https://polyhaven.com/hdris` , 2026. Accessed: 202605-28. 

13 

- [68] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system. _arXiv preprint arXiv:2307.04577_ , 2023. 

- [69] M. J. Kim, C. Finn, and P. Liang. Fine-tuning vision-language-action models: Optimizing speed and success. _arXiv preprint arXiv:2502.19645_ , 2025. 

14 

## **Appendix** 

## **A Task List and Visualization** 

Table 4: Task list with category, task name, task description, success condition, and environment rendering. 

|Category|`task`<br>~~`n`~~`ame`|Description|Success condition|rendering|
|---|---|---|---|---|
|**ITIVE**|`PickCube`|Grasp a cube on the<br>tabletop and lift it away<br>from the surface.|The cube is lifted at least 0.20 m above its<br>resetting height.||
|**PRIM**|`StackCube`|Pick and place one cube<br>on top of another cube to<br>form a stable stack.|The moving cube is stabilized within 0.035<br>m horizontally and 0.025 m vertically of<br>resting directly on top of the base cube.||
||`RelocateSphere`|Move a sphere from its<br>initial tabletop position<br>to the commanded target<br>location.|The sphere comes within 0.03 m of a goal<br>point sampled once per episode.||
||`PickUpStick`|Grasp a stick on the<br>tabletop and lift it while<br>maintaining an upright<br>orientation.|The stick is lifted at least 0.20 m above its<br>reset height and stays within 30<sup>_◦_</sup>of vertical.||
||`RelocateObject`|Move a rigid object from<br>the tabletop reset region<br>to a sampled 3D goal<br>position above the table.|The object is moved to within 0.03 m of a<br>sampled goal point, roughly within 0.2 m of<br>table center and 0.15-0.25 m above the table.||
||`TurnOnSwitch`|Flip an articulated switch<br>from the off state toward<br>the on state.|The switch moves at least 80% of its<br>reachable travel from its reset position.||
||`PushButton`|Move the fingertip or<br>hand into an articulated<br>button and press it down.|The button is pressed at least 80% of its<br>roughly 0.015 m travel.||
||`OpenFaucet`|Turn an articulated faucet<br>handle from its initial<br>pose toward the target<br>turned state.|The handle is turned at least 80<sup>_◦_</sup>from its<br>reset angle.||
||`GraspTwo`<br>`Items`|Randomly select two<br>primitive objects from<br>the candidate set and lift<br>both selected objects.|Both of the two randomly selected primitive<br>shapes, out of 5 candidates, are lifted at least<br>0.20 m above the tabletop at the same time.||
|**ATION**|`OpenCabinet`|Open the cabinet by<br>actuating target joint<br>`joint`<br>~~`1`~~`1`from its reset<br>pose.|The target cabinet joint moves at least 80% of<br>the way toward its limit from its reset pose.||
|**RTICUL**|`LiftLid`|Interact with an<br>articulated object and lift<br>its lid to the open state.|The lid hinge reaches at least 80% of its full<br>opening range.||
|**A**|`OpenDoor`|Grasp the handle, then<br>rotate to unblock the<br>door. Then pull the<br>articulated door until it<br>reaches the open state.|The door hinge reaches at least 80% of its<br>full swing range.||



Continued on next page 

15 

|Category|`task`<br>~~`n`~~`ame`|Description|Success condition|rendering|
|---|---|---|---|---|
||`RotateKnob`|Grasp or contact an<br>articulated knob and<br>rotate it to the target<br>setting.|The knob is turned to either end of its 180<sup>_◦_</sup><br>joint limits.||
||`OpenMicrowave`|Grasp and pull an<br>articulated microwave<br>door until it reaches the<br>open state.|The door hinge reaches at least 80% of its<br>full opening range.||
||`OpenDrawer`|Grasp and pull an<br>articulated drawer<br>outward from the<br>cabinet.|The drawer slides out at least 80% of its full<br>travel.||
||`GraspBucket`|Reach for an articulated<br>bucket and raise its<br>handle from the resting<br>pose.|The handle hinge rotates at least 40% of its<br>reachable range from its near-limit reset<br>pose.||
||`GraspPot`|Manipulate the<br>articulated pot lid until<br>its lid joint reaches the<br>intended state.|The lid hinge reaches at least 80% of its full<br>opening range.||
||`OpenLaptop`|Hold the laptop base and<br>open the laptop lid<br>around its hinge.|The lid swings at least 70% of the way from<br>its slightly-open reset angle near_−_15<sup>_◦_</sup><br>toward the fully open limit near_−_110<sup>_◦_</sup>.||
||`SqueezeScissors`|Hold and squeeze a pair<br>of scissors so the hinge<br>moves toward the closed<br>state.|Either blade hinge closes at least 50% of the<br>way from its reset position.||
||`SlideUtility`<br>`Knife`|Hold a utility knife body<br>and slide its blade out<br>from the handle.|The blade slides out at least 40% of its travel<br>from the retracted reset pose, and the whole<br>knife is lifted at least 0.2 m off its support.||
||`LiftBasket`<br>`Handle`|Hold a shopping basket<br>body and raise one of its<br>articulated handles.|Either handle hinge swings at least 50% of<br>the way from its folded reset position.||
||`OpenStapler`|Hold a stapler body and<br>open the upper arm<br>around its hinge.|The shell hinge opens at least 20% of the<br>way from its closed reset position.||
||`OpenFlatFolder`|Hold a flat folder and<br>open its top flap around<br>the hinge.|The flap hinge opens at least 60% of the way<br>from its near-closed reset position.||
||`Open`<br>`Phone`|Lift and unfold a foldable<br>phone until its hinges<br>open to the target state.|Both screen hinges independently open at<br>least 50% of the way from their folded reset<br>position, and the phone is lifted at least 0.1 m<br>above its spawn height.||
||`OpenDouble`<br>`Door`|Open both target cabinet<br>doors in a coordinated<br>manner.|Both doors reach at least 80% of their full<br>swing range at the same time, and the gap<br>between when each door first stays past that<br>point is no more than 1.0s.||
||`UnscrewCap`|Hold the tube and rotate<br>the cap until it reaches<br>the unscrewed state.|The cap is rotated at least 98% of the way<br>through its reachable unscrewing range from<br>its screwed-in start.||



Continued on next page 

16 

|Category|`task`<br>~~`n`~~`ame`|Description|Success condition|rendering|
|---|---|---|---|---|
||`OpenGlasses`|Hold a pair of glasses<br>and unfold both temple<br>arms.|Both temple hinges independently open at<br>least 80% of the way from their slightly-open<br>reset position.||
|**AL**|`GraspBleach`|Grasp a bleach bottle, lift<br>it, and rotate it into a<br>pouring posture while<br>avoiding the nozzle.|The bottle is lifted at least 0.3 m, tilted at<br>least 100<sup>_◦_</sup>from vertical, and its nozzle<br>brought within 0.02 m of the goal, all while<br>not touching a small region around the<br>nozzle.||
|**UNCTION**|`GraspPan`|Manipulate a frying pan<br>into a controlled flat pose<br>while avoiding contact<br>with the cooking surface.|The pan face is brought within 10<sup>_◦_</sup>of flat<br>and its center within 0.025 m of the burner<br>target, all while not touching the cooking<br>surface.||
|**F**|`GraspKettle`|Grasp a kettle, lift it from<br>the table, and rotate it<br>into a pouring posture<br>while avoiding the spout.|The kettle is lifted at least 0.15 m, tilted at<br>least 45<sup>_◦_</sup>, and its spout brought within 0.05<br>m of the goal, all while not touching the<br>spout.||
||`GraspCup`|Grasp a cup, lift it from<br>the table, and rotate it<br>into a pouring posture<br>while avoiding the rim.|The cup is lifted at least 0.3 m, tilted at least<br>100<sup>_◦_</sup>, and its rim brought within 0.10 m of<br>the goal, all while not touching the rim<br>region.||
||`RetrieveCup`|Remove a cup from a<br>rack and place it upright<br>at the commanded goal.|The cup comes within 0.04 m of the goal on<br>the table and stays within 15<sup>_◦_</sup>of upright.||
||`LiftBucket`|Grasp an articulated<br>bucket and lift the bucket<br>body away from the<br>tabletop.|The bucket is lifted at least 0.12 m above its<br>spawn height.||
||`Functional`<br>`PourCan`|Grasp a soup can, lift it<br>from the table, and rotate<br>it into a pouring posture.|The can is lifted at least 0.2 m, tilted at least<br>100<sup>_◦_</sup>, and its lip brought within 0.10 m of<br>the goal, all while not touching the lip.||
||`Functional`<br>`PourMug`|Grasp a mug, lift it from<br>the table, and rotate it<br>into a pouring posture.|The mug is lifted at least 0.2 m, tilted at least<br>100<sup>_◦_</sup>, and its rim brought within 0.10 m of<br>the goal, all while not touching the rim.||
||`Functional`<br>`HammerStrike`|Use a hammer to strike<br>or press a nail into a<br>board while avoiding<br>unsafe fingertip contact.|The nail is pressed in at least 0.06 m, and the<br>hand does not touch the nail head directly.||
||`Functional`<br>`DrillApply`|Pick up a drill and bring<br>its bit onto a marked<br>target point on the work<br>surface.|The bit tip is brought within 0.025 m of the<br>target while the drill is held near-vertical, all<br>while not touching the chuck or bit.||
||`PourWineGlass`|Lift the wine glass and<br>tilt it into a pouring<br>orientation.|The glass is lifted at least 0.20 m above its<br>spawn height and tilted at least 100<sup>_◦_</sup>from<br>vertical, all while not touching the opening<br>of the glass.||



Continued on next page 

17 

|Category|`task`<br>~~`n`~~`ame`|Description<br>Alin a nut with a fixed|Success condition<br>The nut is centered within about 0.0025 m of|rendering|
|---|---|---|---|---|
|**-RICH**|`NutThread`|g     i<br>bolt and thread it down<br>onto the bolt.|the bolt axis and threaded down to within<br>roughly 0.002 m of the target depth, about<br>1.5 turns down the bolt.||
|**ONTACT**|`InsertPipette`|Pick up a pipette and<br>guide its tip into the neck<br>of the target glassware.|The tip is centered within 0.02 m of the<br>glassware opening and pushed at least 0.01<br>m below the rim.||
|**C**|`PlugCharger`|Align a charger plug with<br>a fixed receptacle and<br>insert the plug into the<br>socket.|The plug tip is inserted into the receptacle<br>with less than 0.0025 m of lateral and<br>vertical misalignment.||
||`InsertPen`|Pick up a pen and guide<br>either tip into the<br>opening of a pen holder.|Either pen tip is centered within about 0.038<br>m of the holder opening and pushed at least<br>0.03 m below its rim.||
||`InsertGear`|Pick and place a gear<br>onto the fixed gear base<br>so that it seats into the<br>mesh position.|The gear’s shaft point is centered within<br>0.0025 m of the base’s shaft and seated to<br>within 0.003 m of full depth.||
||`InsertPeg`|Align a side peg with a<br>fixed tabletop hole and<br>insert it into the opening.|The peg head is inserted to within 0.015 m<br>along the axis and stays within the hole’s<br>0.023 m bore radius laterally.||
||`PickFrom`<br>`Clutter`|Pick the green target<br>object out of a cluttered<br>corral containing<br>distractor objects.|The target object is lifted at least 0.20 m<br>above its default reset height; the 19<br>distractor objects are not checked.||
||`PickThinObject`<br>`FromContainer`|Extract a thin object<br>from a small container<br>and move it to the<br>commanded goal.|The object comes within 0.04 m of the<br>extraction goal, which sits roughly 0.125 m<br>above the object’s start, clear of the<br>container’s 0.11 m walls and pulled forward<br>out of the container.||
|**NSILE**|`PushSphere`<br>`UpSlope`|Push a sphere up a sloped<br>ramp and guide it to the<br>commanded goal region.|The sphere comes within 0.08 m of a goal<br>near the top of the 15<sup>_◦_</sup>slope, sampled within<br>about 0.30 m across the slope’s width.||
|**-PREHE**|`PushSmallSphere`<br>`ObstacleSlope`|Push a small sphere<br>uphill through randomly<br>spawn obstacles until it<br>crosses the target line.|The sphere crosses the target line, reaching<br>or passing both the target’s forward position<br>and height.||
|**NON**|`PushT`|Push a T-shaped object<br>across the plane until it<br>aligns with the target<br>pose.|The pushed T-shape overlaps at least 90% of<br>the goal T’s footprint.||
||`PivotLargeCuboid`<br>`AgainstWall`|Use the hand and wall<br>support to pivot a large<br>thin cuboid into an<br>upright pose.|The cuboid is lifted at least 0.20 m above its<br>reset height and tilted to within 20<sup>_◦_</sup>of<br>vertical.||
||`TakeBook`<br>`OffShelf`|Extract a target book<br>from a shelf and move it<br>to the commanded pose.|The book’s position is within 0.05 m and its<br>orientation within about 26<sup>_◦_</sup>of a goal that<br>sits 0.18 m out and 0.05 m up from the shelf<br>slot, tilted downward by 65<sup>_◦_</sup>.||



Continued on next page 

18 

|Category|`task`<br>~~`n`~~`ame`|Description|Success condition|rendering|
|---|---|---|---|---|
|**TION**|`BimanualLift`<br>`Tray`|Use both hands to lift a<br>tray while keeping the<br>carried surface level.|The tray is lifted at least 0.20 m above reset<br>height and kept within 10<sup>_◦_</sup>of level.||
|**OORDINA**|`BimanualLift`<br>`Basket`|Use both hands to grasp<br>and lift a basket while<br>maintaining a level<br>carrying pose.|The basket is lifted at least 0.20 m above<br>reset height and kept within 10<sup>_◦_</sup>of level.||
|**ANUAL C**|`BimanualLift`<br>`Carton`|Use both hands to grasp<br>a carton and lift it clear<br>of the tabletop.|The carton is lifted at least 0.20 m above its<br>spawn height.||
|**BIM**|`BimanualLift`<br>`DutchOven`|Use both hands to grasp<br>a Dutch oven and lift the<br>cookware from the table.|The Dutch oven is lifted at least 0.30 m<br>above its spawn height.||
||`Bimanual`<br>`Handover`|Transfer a cube so that<br>the left hand holds it<br>while the right hand<br>releases it and the object<br>remains stable.|The left hand grips firmly the cube with a<br>contact force of at least 1.6 N on at least one<br>link, while the right hand having no active<br>contact with the cube.||
|**ORIZON**|`CookFood`|Pour ingredients into a<br>pot, keep the food<br>contained, move the pot<br>to the stove, and turn the<br>stove on.|First, in any order: the bottle and the can are<br>each lifted at least 0.10 m, tilted at least<br>100<sup>_◦_</sup>, and their spout brought within 0.10 m<br>of the pot. Then, all at once: the stove knob<br>is turned at least 45<sup>_◦_</sup>, the pot is centered<br>within 0.08 m of the burner and stays within<br>15<sup>_◦_</sup>of flat, and all active ingredients remain<br>inside the pot.||
|**LONG-H**|`MakeCoffee`|Pour milk into a mug,<br>place the mug under the<br>coffee machine, and<br>activate the machine<br>switch.|In order: pour the milk into the mug by<br>tilting the bottle at least 70<sup>_◦_</sup>and bringing its<br>spout close to the mug, place the mug under<br>the coffee machine within about 0.09 m<br>horizontally and 0.07 m vertically of its<br>target spot, then rotate the switch lever at<br>least 35<sup>_◦_</sup>from rest.||
||`MicrowaveFood`|Open the fridge, retrieve<br>food, place it into the<br>microwave, close the<br>appliance, and turn the<br>dial.|In order: open the fridge at least a quarter of<br>the way, close it back down, open the<br>microwave door at least halfway, place the<br>food within 0.15 m of its goal, close the<br>microwave door, then turn either dial at least<br>18<sup>_◦_</sup>from rest.||
||OvenBake|Season salmon with<br>condiments, load it into<br>the oven, close the oven<br>door, and start the oven.|First, in any order, the salmon is seasoned<br>with both salt and pepper by lifting, tilting,<br>and pouring each jar near the salmon. Then,<br>in order: the salmon is placed inside the oven<br>cavity, the door is closed while the salmon<br>stays inside, and the oven knob is turned<br>about 40<sup>_◦_</sup>while the salmon still stays inside.||
|||Sort active objects into|In any order: the drawer is fully closed with||
|||the drawer or trash can,|every active drawer-assigned object||
||`CleanTable`|then close the<br>corresponding<br>receptacles.|contained inside it, and the trash lid is closed<br>and latched with every active trash-assigned<br>object contained inside it.||



### **Multi-goal composite tasks (** `multigraspenvs` **)** 

The `multigraspenvs` benchmark composes 39 environment variants by pairing one of nine articulated-object tasks drawn from the primitive and articulation categories with one of four rigid-object addon tasks. The primary set is _{_ OpenMicrowave, OpenDoor, OpenDrawer, LiftLid, GraspPot, PushButton, RotateKnob, TurnOnSwitch, GraspBucket _}_ , and the addon set is _{_ PourCan, PickUpStick, PourMug, RelocateSphere _}_ . Every primary task is paired with every addon, giving 

19 

9 _×_ 4 = 36 variants, and PourMug additionally serves as a primary task paired with the remaining three addons _{_ PourCan, PickUpStick, RelocateSphere _}_ , giving 3 more variants, for 39 total. Each variant places both the primary task’s asset and the addon object in the same scene, and the agent must interact with both. 

An environment is marked successful when both of the following hold at the same time: 

- The addon object is lifted at least _h_ addon above its reset height, regardless of which addon task it originally comes from. 

- The primary task’s articulated joint also reaches its own single-task success threshold _τ_ primary. For when the primary object is the mug, the same lift-then-pour procedure apply. 

Both conditions must hold simultaneously for the task to count as a success. _h_ addon is a single fixed lift threshold shared across all 39 variants, while _τ_ primary is task-specific and matches each primary task’s own standalone threshold. 

## **B Imitation Learning Baseline & Implementation Details** 

_π_ 0 _._ 5 **.** We fine-tune the official 3.3B-parameter _π_ 0 _._ 5 checkpoint. At each control step the observation comprises (i) two 256 _×_ 256 RGB images from a fixed third-person camera and a wrist-mounted camera (three cameras – third-person, left wrist, and right wrist – for the bimanual variant) and (ii) the per-task natural-language instruction; the policy is conditioned on vision and language only, as the proprioceptive-state input is disabled. The Gemma action expert predicts a 10-step chunk of absolute 28-/56-dimensional joint targets via flow matching. We fully fine-tune all model parameters on 32 H20 GPUs for 2K steps, using AdamW ( _β_ = (0 _._ 9 _,_ 0 _._ 95), weight decay 10<sup>_−_10</sup> , gradient-norm clipping at 1 _._ 0), a global batch size of 512, and a cosine learning-rate schedule (100-step warmup, peak 10<sup>_−_4</sup> decaying to 10<sup>_−_6</sup> ). 

**OpenVLA.** We fine-tune `openvla-7b` [19] with the OFT recipe [69], replacing the discrete 7- token action head with a continuous _L_ 1-regression head that emits an 8-step chunk of absolute joint targets. The observation comprises the same RGB camera set as _π_ 0 _._ 5 (two views single-hand, three views bimanual), the current 28-/56-dimensional joint position encoded by a learned proprioceptive projector, and the per-task language instruction. Fine-tuning attaches LoRA (rank 32) adapters to every linear layer of the base VLA, while the regression head and the proprioceptive projector are trained from scratch; the underlying base weights remain frozen. We train on 8 H20 GPUs for 3K steps with AdamW at a learning rate of 10<sup>_−_4</sup> (decayed by 10 _×_ via a multi-step schedule), a per-GPU batch size of 8, and random-crop image augmentation. 

**Diffusion Policy.** Following the state-based variant of diffusion policy [6], we train a separate policy per task on the normalized proprioceptive state, with no visual input. The denoiser is the standard 1D conditional U-Net with FiLM conditioning, channel widths (256 _,_ 512 _,_ 1024) and two residual blocks per stage. Observations are passed through a 256-d encoder and projected to a 128-d conditioning vector. We use an observation horizon of _To_ =2 and predict action chunks of length _Ta_ =16 at stride 1, re-planning from fresh observations after each chunk. The denoiser is trained with the DDPM objective over 100 timesteps under a squared-cosine _β_ schedule, and 20 denoising steps are taken at inference. We optimize with AdamW (lr=1 _×_ 10<sup>_−_4</sup> , weight decay 1 _×_ 10<sup>_−_4</sup> ), batch size 256, gradient-norm clipping at 1 _._ 0, and an EMA of decay 0 _._ 995 on the policy weights. Each policy is trained for up to 300 epochs with early stopping on the held-out validation loss. Following the state-based variant of Diffusion Policy [6], we train a per-task U-Net denoiser on normalized proprioceptive state with no visual input. It uses an observation horizon of _To_ =2 and predicts action chunks of length _Ta_ =16, re-planning after each chunk. 

**3D Diffusion Policy.** Following DP3 [15], we train a separate policy per task that conditions on a point cloud plus proprioception and has no RGB or language input. Each observation is a workspacecropped point cloud back-projected from a single front-view depth camera (two views are fused for 

20 

bimanual tasks), expressed in world frame and farthest-point-downsampled to _N_ =512 points; the proprioceptive input is the current 28-/56-dimensional joint position. A lightweight PointNet encoder (per-point MLP with LayerNorm, max-pooled, projected to 64-d) summarizes the cloud, and the proprio history is flattened and concatenated to form the global conditioning vector. The denoiser is the same 1D conditional U-Net with FiLM conditioning as in the state-based variant, but widened to channel widths (512 _,_ 1024 _,_ 2048) with two residual blocks per stage (kernel size 5, GroupNorm with 8 groups). It uses an observation horizon of _To_ =2 and predicts action chunks of length _Ta_ =16, executing the first 8 steps before re-planning. The denoiser is trained with the DDIM objective over 100 timesteps under a squared-cosine _β_ schedule, and 10 denoising steps are taken at inference. Pertask statistics over the training split normalize point clouds, proprioception, and actions to [ _−_ 1 _,_ 1]. We optimize with AdamW (lr=1 _×_ 10<sup>_−_4</sup> , weight decay 1 _×_ 10<sup>_−_6</sup> , _β_ =(0 _._ 95 _,_ 0 _._ 999)), batch size 128, gradient-norm clipping at 1 _._ 0, and an EMA of max-decay 0 _._ 9999 on the policy weights. Each policy is trained for 100 epochs. 

## **C Observation Modes** 

DexVerse organizes observations into nine groups: `policy` , `proprio` , `contact` , `state` , `privileged` , `goal` , `rgb` , `depth` , and `pointcloud` . Each group holds observation terms with a single semantic role, so a consumer (policy, asymmetric critic, or perception backbone) can subscribe to exactly the groups it needs. 

- `policy` **:** Contains the previous action. 

- `proprio` **:** Contains the joint positions of every joint of the robots. 

- `contact` **:** Contains a per-fingertip 3D contact-force vector for each configured contact sensor, expressed in the robot base frame. This group is `None` when contact sensors are disabled for a task. 

- `state` **:** Contains observable task state such as object poses, articulated-object poses, joint positions. Also contains derived geometry such as functional-point positions and functional-axis directions, and, for the long-horizon tasks, stage progress. The exact terms are task-specific; this group is `None` for tasks that do not populate it. 

- `privileged` **:** Contains simulation-only quantities that are withheld from the policy, such as robot joint velocities, full body state (position, orientation, linear velocity, and angular velocity) for the robot’s hand links, and, where applicable, object linear and angular velocities. 

- `goal` **:** Contains the commanded task target, such as a target object pose or position that the object should reach for task success. This group is `None` for tasks with no separate goal, such as PickCube. 

- `rgb` **:** Contains an RGB image from each configured camera, kept as separate per-camera tensors. 

- `depth` **:** Contains a distance-to-image-plane depth image from each configured camera, kept as separate per-camera tensors. 

- `pointcloud` **:** Contains a point cloud from a single camera, or merged from multiple camera views when multiview is enabled. 

Task configurations select the observation groups and terms required by each environment, giving downstream policies a unified interface across state-based, image-based, point-cloud-based, and privileged observations. 

### **Observation-mode presets** 

While the user is free to select the observation groups to use, DexVerse also defines some observation-mode presets, each of which enables a fixed set of groups and disables every other 

21 

managed group. A preset is applied to an environment’s `ObservationsCfg` through a config field. The `privileged` group is never enabled by any preset since it contains information that is hardly observable in the real world and should only be intentionally enabled by the user. 

|Preset|Groups enabled|History length|Multiview|
|---|---|---|---|
|`state`|policy, proprio, contact, state, goal|0|no|
|`rgb`|policy, proprio, goal, rgb|3|no|
|`rgb`<br>~~`d`~~`epth`|policy, proprio, goal, rgb, depth|3|no|
|`pointcloud`|policy, proprio, goal, pointcloud|3|no|
|`3view`<br>~~`r`~~`gb`|policy, proprio, goal, rgb|3|yes|
|`3view`<br>~~`r`~~`gb`<br>`depth`|policy, proprio, goal, rgb, depth|3|yes|
|`3view`<br>~~`p`~~`ointcloud`|policy, proprio, goal, pointcloud|3|yes|



Table 5: Observation-mode presets. Each preset enables only the listed groups and sets history length to the given length 

22 

