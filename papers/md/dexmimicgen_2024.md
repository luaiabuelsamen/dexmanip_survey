# **DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning** 

Zhenyu Jiang<sup>_∗_1</sup><sup>_,_2</sup> Yuqi Xie<sup>_∗_1</sup><sup>_,_2</sup> Kevin Lin<sup>_∗_1</sup><sup>_,_2</sup> Zhenjia Xu<sup>1</sup> Weikang Wan<sup>3</sup> Ajay Mandlekar<sup>_†_1</sup> Linxi “Jim” Fan<sup>_†_1</sup> Yuke Zhu<sup>_†_1</sup><sup>_,_2</sup> 

**_Abstract_ — Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the high costs and human efforts involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the difficulty of simultaneously controlling the two arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for training data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for bimanual robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-tosim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at dexmimicgen.github.io.** 

## I. INTRODUCTION 

Imitation learning from human demonstrations is an effective means to teach robots manipulation skills [1,2]. One popular approach to collecting demonstrations is teleoperation, where human operators control robot arms to collect data for training the autonomous policies [3,4]. Recent efforts have scaled this approach to collect large diverse datasets through teams of human operators, and shown that robots trained on this data can achieve impressive performance and even generalize to different settings [2,5–8]. There has also been recent interest in applying this paradigm to humanoid robot embodiments [9–14]. 

Nonetheless, data acquisition has been a key bottleneck in applying this paradigm more broadly. Prior efforts for data collection in the single robot arm setting required multiple human operators, robots, and months of human effort [2,5– 8]. Unfortunately, scaling data collection for humanoids can be even more difficult, owing to the challenges of controlling the two arms and multi-fingered dexterous hands simultaneously. Enabling real-time teleoperation for humanoids has required the development of special-purpose teleoperation interfaces [9–14], but these pipelines can be costly and difficult to scale. Furthermore, the increase in operator burden due to multi-arm and multi-finger hand control makes collecting 

*Equal Contributions, _†_ Project Leads 

> 1NVIDIA Research, 2UT Austin, 3UC San Diego 



<!-- Start of picture text -->
Real-World Teleoperation Simulation Replay<br>Digital Twin<br>Real2Sim<br>DexMimicGen DataGeneration<br>Digital Twin<br>Sim2Real<br>Real-World Deployment Generated Trajectories<br><!-- End of picture text -->

Fig. 1: **DexMimicGen Overview.** DexMimicGen offers an efficient pipeline to train capable bimanual dexterous robots. (left) First, a human operator collects around five task demonstrations using a teleoperation device. (middle) Next, DexMimicGen automatically generates a large set of demonstration trajectories in simulation. (right) Finally, a policy is trained with imitation learning and deployed in the real world. 

demonstrations in this setting more challenging compared to the single-arm setting, further limiting the rate of data collection. The data acquisition burden is further compounded by the higher data requirements in the humanoid setting due to the increased degrees of freedom and task complexity. 

Leveraging automated data generation in simulation is a compelling alternative that has proved effective for the single-arm robot manipulation setting [15–17]. Inspired by prior successes, **we introduce DexMimicGen (DexMG), a large-scale automated data generation system for bimanual robots with dexterous hands, such as humanoids** . The core idea is to leverage a small set of human demonstrations and use demonstration transformation and replay in physical simulation to automatically generate large amounts of training data suitable for imitation learning in the bimanual dexterous manipulation setting. This system builds on top of MimicGen [17], which proposed a similar pipeline for the single-arm with parallel-jaw gripper setting. However, there remain several technical challenges that DexMimicGen has to overcome to operationalize the same principles. 

MimicGen relies on decomposing each task into a sequence of subtasks, to generate trajectories for each subtask separately and then stitch them together. Bimanual dexterous manipulation involves three types of subtasks where the two arms need to achieve sub-goals independently, with coordination, and following a specific order. MimicGen, which relies on a single subtask segmentation, struggles to handle the independent and interdependent actions required in 

bimanual tasks. To address these challenges, DexMimicGen incorporates a flexible per-arm subtask segmentation strategy, allowing each arm to execute its subtasks independently while still accommodating the necessary coordination phases. DexMG employs a synchronization strategy to ensure precise alignment of actions during coordination subtasks and an ordering constraint mechanism to enforce the correct order of actions during sequential subtasks. 

DexMimicGen. We show DexMimicGen plays a significant role in facilitating algorithm development for bimanual manipulation by making simulation-based manipulation datasets more widely accessible and providing easy-to-reproduce results. Recent works have leveraged offline data augmentation to increase the dataset sizes [1,55–69]. By contrast, DexMimicGen generates datasets using online simulation, ensuring the generated trajectories are physically valid. 

## **We make the following contributions:** 

_•_ We introduce DexMimicGen (DexMG), a data generation system that automatically synthesizes trajectories from a small number of human demonstrations for bimanual and dexterous robot manipulation. We introduce several key design features, including an asynchronous per-arm execution strategy, synchronization, and sequential constraints that enable handling multi-arm coordination. 

_•_ We introduce a suite of nine simulation environments across three different embodiment types requiring different coordination behaviors between the two arms. We apply DexMimicGen to generate 21K demos across these tasks from merely 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. We have released our simulations and datasets to facilitate future study into the bimanual and dexterous manipulation setting. 

_•_ We create a simulated digital twin of a real-world cansorting task, replay real-world human demonstrations in the simulation, synthesize trajectories with DexMimicGen, and then transfer the generated trajectories back into the real world, producing a visuomotor policy of 90% success rate, as opposed to 0% from just using the human demos (Fig. 1). 

## II. RELATED WORK 

**Data Collection through Teleoperation.** Teleoperation is a prevalent approach to gathering task demonstrations in robotics [3,4,18–23]. Human operators use an interface to control a robot in real time remotely, and sensor data and robot control commands are logged to a dataset. Some systems allow data collection for multiple robot arms [24– 27] and humanoids [9–14,28], and some also enable robotfree data collection using specialized hardware [29–31]. However, all these methods require significant human time and resources to collect large datasets. Some other efforts use pre-programmed experts to automate data generation in simulation [15,16,32–36], but applying these methods to challenging scenarios involving multi-arm coordination can be difficult. By contrast, DexMimicGen builds upon MimicGen [17,37,38] to automate data generation using a handful of human demonstrations, greatly reducing the human effort involved in collecting large datasets. 

**Imitation Learning and Data Augmentation.** Behavioral Cloning [39] is an established framework for learning robot control policies from demonstrations and has been used extensively in prior work [33,40–50], including for bimanual manipulators [24–26,51] and humanoid robots [10,11,28,52,53]. In this work, we apply existing imitation learning methods [1,54] to datasets generated by 

## III. PREREQUISITES 

**Imitation Learning.** We formalize each manipulation task as a Partially Observable Markov Decision Pro= cess (POMDP). We are given _N_ demonstrations _D {_ ( _s_<sup>_i_</sup> 0<sup>_, o_</sup> 0<sup>_i, a_</sup> 0<sup>_i, s_</sup> 1<sup>_i, o_</sup> 1<sup>_i, a_</sup> 1<sup>_i, ..., si_</sup> _Hi_<sup>)</sup><sup>_}_</sup> _i_<sup>_N_</sup> =1<sup>consistingofstates</sup><sup>_s∈_</sup> _S_ , observations _o ∈O_ , and actions _a ∈A_ . Each episode starts in a state _s_<sup>_i_</sup> 0<sup>_∼D_sampledfromtheinitialstate</sup> distribution _D ⊆S_ . The goal is to learn a policy _π_ : _O →A_ that maps observations to a distribution over the action space. We focus on Behavioral Cloning (BC) [39] methods that find a policy via the maximum likelihood objective arg max _θ_ E( _s,o,a_ ) _∼D_ [log _πθ_ ( _a | o_ )]. We train our policies with datasets generated via DexMimicGen. 

**Assumptions.** Like MimicGen [17], we make these assumptions. ( **A1** ): the action space _A_ consists of the following components for each robot arm: a pose command for an end effector controller and an actuation command for the hand (1D open/close for parallel-jaw gripper, 6-D joint commands for dexterous hand). ( **A2** ): Each task can be divided into object-centric subtasks (see Sec. IV-A). ( **A3** ): During data collection, an object’s pose can be observed or estimated prior to a robot arm making contact with that object. 

**MimicGen.** MimicGen [17] uses a small number of source human demonstrations _D_ src to generate a large dataset _D_ . It assumes that every task consists of a sequence of objectcentric subtasks ( _S_ 1( _o_ 1), _S_ 2( _o_ 2), ..., _SM_ ( _oM_ )) where the manipulation in each subtask _Si_ ( _oi_ ) is relative to a single object’s coordinate frame ( _oi ∈O_ , where _O_ is the set of objects in the task). It divides each source demo _τ ∈ Dsrc_ into contiguous object-centric manipulation segments _{τi}_<sup>_M_</sup> _i_ =1<sup>,eachofwhichcorrespondstoasubtask</sup><sup>_Si_(</sup><sup>_oi_).</sup> Each segment is a sequence of end effector control poses _τi_ = ( _TW_<sup>_C_0</sup><sup>_, T_</sup> _W_<sup>_C_1</sup><sup>_, ..., T_</sup> _W_<sup>_CK_)where</sup><sup>_W_istheworldreference</sup> frame. This segmentation can be done with human annotation or using heuristics. To generate a new demonstration in a novel scene, it observes the pose of the object for the current _i_ subtask _TW_<sup>_o′_,andtransformstheposesinasourcehuman</sup> _i_ segment (with a constant SE(3) transform _TW_<sup>_o′_(</sup><sup>_T o_</sup> _W_<sup>_i_)</sup><sup>_−_1)such</sup> that relative poses between the end effector and object frame are preserved between the source segment and the new scene. It then adds poses to the start of the segment to interpolate between the robot’s current state and the start of the transformed segment. Then, it executes the entire sequence of poses open-loop using the robot end effector controller and repeats this process for the next subtask. It checks for task success after executing all subtasks and only keeps the demonstration if it was successful. 



<!-- Start of picture text -->
Parallel subtask:  pick up concave piece and convex piece separately.<br>Coordination subtask:  place the lid with both hands.<br>Sequential subtask:  pour ball into bowl and then place bowl on green pad.<br>Pre-task Post-task<br><!-- End of picture text -->

Fig. 2: **Subtask Types.** We categorize the subtasks into parallel, coordination, and sequential subtasks, where the two arms achieve subgoals independently, with coordination, and following a specific order. 

## IV. DEXMIMICGEN METHOD 

DexMimicGen generates data for bimanual and dexterous manipulation — doing so involves handling three key challenges compared to MimicGen. First, each arm must operate independently of the other arm to achieve different goals. Next, the arms must coordinate to accomplish a shared goal. Finally, one arm’s subtask must be completed before the next one can be attempted. DexMimicGen handles these challenges by introducing a taxonomy of subtask types (Fig. 2) — parallel (Sec. IV-A), coordination (Sec. IV-B), and sequential (Sec. IV-C), and making changes to the data generation process to accommodate them. Sec. IV-D provides an overview of the entire data generation process. Note that, similar to MimicGen, we exploit the SE(3) equivariance of robot actions with respect to object poses. Specifically, when an object’s pose has an SE(3) transformation applied to it, we can similarly apply the same SE(3) transformation to robot actions to replicate the same effect of the original robot actions on the new object pose. 

..., _SM_<sup>_a_2</sup> 2<sup>(</sup><sup>_oM_</sup> 2<sup>). Each source demonstration is split into object-</sup> centric manipulation segments as in MimicGen, but now each arm has its own set of segments ( _{τi_<sup>_n}M_</sup> _i_ =1<sup>_n_,</sup><sup>_n ∈{_1</sup><sup>_,_2</sup><sup>_}_).</sup> 

However, since arm subtasks are defined independently, their execution can start and end at different times that are not aligned. To accommodate this, DexMimicGen employs an asynchronous execution strategy, where an action queue is maintained for each arm. Actions are dequeued for each arm one by one in parallel. Whenever an arm’s queue is empty, it is populated with the transformed subtask segment for the next subtask (using the same transformation from MimicGen). This approach allows for the execution of actions for both arms without requiring alignment between subtasks. 

## _B. Coordination Subtasks_ 

Some tasks require precise coordination, such as placing the lid in the Box Cleanup task (Fig. 2 middle). In these **coordination subtasks** , the relative poses between the two end-effectors during execution must be aligned with the corresponding relative poses in the source demonstration. To achieve this, we ensure that 1) both arms execute their trajectories in a synchronized manner and 2) the trajectories for both arms are generated with the same transformation. To achieve this temporal alignment, we enforce that coordination subtasks end at the same timestep during source demo segmentation. During execution, we implement a synchronization strategy in which each arm waits for the other until both have the same number of remaining steps in the coordination subtask, aligning the end of subtask execution with the subtask segmentation. 

We provide different source demonstration transformation schemes to acquire the common transformation matrix for both arms in coordination subtasks. These include the Transform and Replay schemes. The Transform scheme utilizes the _i_ transformation matrix _TW_<sup>_o′_(</sup><sup>_T o_</sup> _W_<sup>_i_)</sup><sup>_−_1computed from the object</sup> pose at the moment the first arm begins the coordination _i_ subtask _TW_<sup>_o′_andtheobjectposeinthecorrespondingsource</sup> segment _TW_<sup>_oi_.Incontrast,thereplayschemedirectlyuses</sup> the source trajectories without applying any transformation. The replay scheme can be beneficial for specific coordination subtasks like the handover phase of the Can Sorting and Transport tasks, because it ensures the trajectory remains within kinematic limits and is fully executable. 

## _C. Sequential Subtasks_ 

## _A. Parallel Subtasks_ 

In the bimanual setting, each arm must be able to operate independently of the other arm. For example, at the start of the Piece Assembly task (Fig. 2 top), each arm needs to grasp a separate object and might finish grasping the object at different points in time. This makes the single fixed sequence of subtasks from MimicGen unsuitable. To enable a flexible order of completion for **parallel subtasks** involving two arms, we consider each task to consist of a sequence of subtasks for each arm: _S_ 1<sup>_a_1(</sup><sup>_o_1),...,</sup><sup>_S_</sup> _M_<sup>_a_1</sup> 1<sup>(</sup><sup>_oM_</sup> 1<sup>)and</sup><sup>_S_</sup> 1<sup>_a_2(</sup><sup>_o_1),</sup> 

Some tasks require subtasks to be completed in a specific order. For example, in the Pouring task (Fig. 2 bottom), the robot must pour the ball into the bowl with one hand before moving the bowl to the pad with the other hand. To handle these **sequential subtasks** , we implement an ordering constraint mechanism. We specify a pre-subtask (pouring the ball) and a post-subtask (picking the bowl) based on the task requirement. This mechanism ensures that the arm executing the post-subtask waits until the pre-subtask of the other arm is completed before continuing with the post-subtask. 



<!-- Start of picture text -->
Source demo segmentation New trajectory generation and execution<br>Parallel:  pick cube  Parallel:  place cube  Coordination:  lift tray  Reference  Reference<br>Ref object:  blue cube Ref object:  tray Ref object:  tray Left arm Subtask Trajectory<br>Right arm<br>Right Two-arm coordination<br>Arm<br>Current<br>Observation<br>Full Object-Centric<br>Demo Trajectory Transformation<br>Left<br>Arm<br>Parallel:  pick cube  Parallel:  place cube  Coordination:  lift tray  Executed Generated<br>Ref object:  green cube Ref object:  tray Ref object:  tray  Trajectory Trajectory<br><!-- End of picture text -->

Fig. 3: **DexMimicGen Workflow.** Left: segment source demonstrations for each arm through manually defined heuristics or human and records the poses of the reference objects. Right: In a new simulation environment, we generate trajectories by transforming source trajectories with reference object poses and executing them. 

## _D. Data Generation for Bimanual Manipulation_ 

We outline the overall DexMimicGen data generation workflow using the Tray Lift task as an example. First, source demos are segmented into per-arm subtasks using manually defined heuristics or human annotation (Fig. 3 left). The final subtask for each arm requires coordination (they must lift the tray together), so it is annotated as a coordination subtask for synchronization during data generation (Sec. IV-B). 

At the start of data generation, the scene is randomized and a source demonstration is selected (as in MimicGen). We then iteratively generate and execute trajectories for each subtask of each arm in parallel (see Fig. 3 right). In this example, given the pose of the reference object (the tray), we compute the relative transformation between the current tray pose and the tray pose in the source segment. We use this transformation to transform the source trajectories of both arms because these are coordination subtasks. Then we use the synchronization execution strategy described in Sec. IVB to execute the generated trajectory. Note that we generate finger motion by replaying the finger joint actions in the source demo because the finger movement is always relative to the end-effector movement. Each generated demonstration is only kept if the task is successful, and this process repeats until a sufficient amount of data is generated. 

## V. SYSTEM DESIGN 

In order to instantiate DexMimicGen, we build a large collection of simulation environments and a teleoperation system allowing for source human demonstration collection in both simulation and the real world. 

**Simulation Environments.** We introduce a diverse range of setups and tasks to demonstrate the capability of DexMimicGen to generate data across different embodiments and 

manipulation behaviors. The tasks are developed in RoboSuite [70] and use MuJoCo [71] for physics simulation. We focus on three embodiments: (1) bimanual Panda arms equipped with parallel-jaw grippers, (2) bimanual Panda arms with dexterous hands, and (3) a GR-1 humanoid equipped with dexterous hands. We apply different controllers for different embodiments. For the Panda arms, we leverage the Operational Space Control (OSC) [72] framework, which converts the delta end-effector pose into joint torque commands. For the humanoid, we implemented an Inverse Kinematics (IK) controller based on mink [73,74]. We found this to be an effective approach to deal with the complexity of the humanoid kinematic tree, where both arms are linked to a single torso. The IK controller translates global target end-effector poses into robot joint positions. For finger control, we directly use joint position control. 

For each embodiment, we introduce three tasks, resulting in a total of nine tasks, as depicted in Fig. 4. These tasks involve high-precision manipulation (Threading, Piece Assembly, Box Packing, Coffee), manipulation of articulated objects (Drawer), and are long-horizon (Transport). The tasks also require overcoming key challenges in multiarm interaction. Several of these tasks contain coordination subtasks, where both arms need to cooperate to finish the subtask (Threading, Transport, Box Packing, Tray Lift, Can Sorting). Other tasks necessitate sequential subtask execution (Piece Assembly, Drawer Cleanup, Pouring, Coffee). We also introduce task variants that broaden the default reset distribution _D_ 0 for certain tasks, as in MimicGen. For instance, in the Pouring task, _D_ 1 represents a variant where objects have a larger initial reset distribution, while in _D_ 2, the reset positions of the bowl and the green pad are swapped. These simulation environments along with the datasets generated 



<!-- Start of picture text -->
Threading Piece Assembly Transport<br>Box Cleanup Drawer Cleanup Tray Lift<br>Pouring Coffee Can Sorting<br><!-- End of picture text -->

Fig. 4: **Simulation Tasks.** We deploy DexMimicGen on nine simulation tasks across three embodiments — two arms with parallel-jaw grippers (top), two arms with dexterous hands (middle), and a humanoid (bottom) 

|**Task**|**Source Demo DP**|**BC-RNN-GMM**|**BC-RNN**|**DP**|
|---|---|---|---|---|
|Piece Assembly|3_._3_±_0_._9|74_._0_±_2_._8|66_._0_±_2_._0|**80**_._**7**_±_**0**_._**9**|
|Threading|1_._3_±_0_._9|54_._0_±_4_._3|68_._0_±_1_._6|**69**_._**3**_±_**1**_._**9**|
|Transport|52_._7_±_7_._7|64_._0_±_3_._3|57_._3_±_4_._1|**83**_._**3**_±_**0**_._**9**|
|Box Cleanup|62_._0_±_1_._6|64_._0_±_10_._0|**94**_._**7**_±_**0**_._**9**|92_._0_±_4_._3|
|Drawer Cleanup|0_._7_±_0_._9|30_._7_±_5_._0|**80**_._**0**_±_**0**_._**0**|76_._0_±_0_._0|
|Tray Lift|3_._3_±_0_._9|66_._0_±_8_._2|78_._0_±_2_._0|**88**_._**7**_±_**0**_._**9**|
|Pouring|0_._7_±_0_._9|74_._0_±_8_._6|62_._0_±_7_._5|**79**_._**3**_±_**0**_._**9**|
|Coffee|14_._7_±_0_._9|12_._0_±_1_._6|**84**_._**7**_±_**4**_._**9**|77_._3_±_0_._9|
|Can Sorting|0_._7_±_0_._9|75_._3_±_1_._9|96_._0_±_4_._3|**97**_._**3**_±_**0**_._**9**|



TABLE I: Success rates (3 seeds) of image-based policies trained with BC on the source demos and DexMimicGen datasets of 1000 trajectories. 

by DexMimicGen provide a valuable platform to analyze various factors that influence the performance of imitation learning in the bimanual and dexterous manipulation setting. 

**Teleoperation System.** To collect source demonstrations for the tasks, we employ different teleoperation methods tailored to each embodiment. For bimanual Panda arms equipped with parallel-jaw grippers, we use an iPhone-based teleoperation interface, as introduced in RoboTurk [4,24], to capture human wrist and gripper actions. For robots equipped with dexterous hands, we implemented an Apple Vision Pro-based teleoperation system. Specifically, we employ the VisionProTeleop software [75] to collect wrist and finger poses via Apple Vision Pro. We first align the human and the robot to convert the raw human end effector poses to robot poses. We design a human-to-robot calibration process asking the human teleoperator to start with a fixed pose, and we automatically compute the relative transformation matrices that map the human poses to robot targets. This calibration process adapts to both bimanual Panda arms with dexterous hands and the GR-1 humanoid. We use the retargeting method provided by OmniH2O [13] to retarget human finger pose to robot finger joint positions. This teleoperation system converts human actions to robot action targets, allowing us to collect demonstrations intuitively. 

## VI. EXPERIMENTS 

In this section, we provide empirical evidence showcasing the efficacy of DexMimicGen. We discuss details on experiment setup (Sec. VI-A), highlight DexMimicGen features and applications (Sec. VI-B), then analyze how data generation and policy learning choices impact policy 



<!-- Start of picture text -->
100% Success Rate per Task Trained on Different Numbers of Demos<br>100 demos 1000 demos<br>80% 500 demos 5000 demos<br>60%<br>40%<br>20%<br>0%<br>Transport BCRNN + GMM DrawerCleanup BCRNN Coffee D1 DP<br>Success Rate<br><!-- End of picture text -->

Fig. 5: **Dataset Size Comparison.** Success rates of policies trained on datasets with different sizes. 

|**Task**|**Policy**|**D0**|**D1**|**D2**|
|---|---|---|---|---|
|Piece Assembly|BC-RNN-GMM|74_._0_±_2_._8|67_._3_±_0_._9|44_._0_±_3_._3|
|Box Cleanup|BCRNN|96_._7_±_2_._5|88_._0_±_5_._9|78_._7_±_2_._5|
|Pouring|DP|79_._3_±_0_._9|82_._0_±_2_._0|71_._3_±_2_._5|



TABLE II: Success rates of policy trained on data generated with broader initial distributions, evaluated with same broader initial distributions. 

performance (Sec. VI-C), and finally present a real-world application of the DexMimicGen system (Sec. VI-D). 

## _A. Experimental Setup_ 

We collect ten source human demonstrations for each task with parallel-jaw grippers, but only five demonstrations for those involving dexterous hands due to the additional operator burden and time cost of collecting demonstrations for dexterous hands. DexMimicGen is subsequently used to generate 1000 demonstrations per task. Each dataset was used to train visuomotor policies through Behavioral Cloning with an RNN [1], an RNN-GMM [1], and a Diffusion Policy [54]. For evaluation, we follow the procedure in prior work [1,17]: we run each experiment across 3 different seeds, and take the maximum policy success rate for each seed. 

## _B. DexMimicGen Features_ 

**DexMimicGen significantly boosts the policies’ success rates over using the source demonstrations only.** Robots trained on DexMimicGen’s datasets outperform those trained only on the small source datasets across all tasks (see Table I). Notable improvements include policy performance on Drawer Cleanup (0.7% to 76.0% success), Threading (1.3% to 69.3%), and Piece Assembly (3.3% to 80.7%). 

**DexMimicGen produces capable policies across diverse initial state distributions** . DexMimicGen generates datasets with broader initial state distributions ( _D_ 1, _D_ 2) from source demos in _D_ 0. As shown in Table II, policies trained on these datasets are performant in the evaluation with the same broader initial state distributions, showing that DexMimicGen generates valuable datasets on new initial state distributions. 

**DexMimicGen generates data across different benchmarks** . We apply DexMimicGen to BiGym [76], a new simulation benchmark for humanoid robots involving bimanual mobile manipulation tasks. We generate 1000 demonstrations for each of the three tasks, FlipCup, DishwasherLoadPlates, and CupBoardsCloseAll, and achieve data generation success rates of 29.1%, 43.6%, and 76.4%. The visualizations of generated demonstrations can be found on the project website. 

|**Task**|**Policy**|**DemoNoise**|**DexMimicGen**|
|---|---|---|---|
|Piece Assembly|BCRNN + GMM|12.7 _±_ 3.4<br>|**74.0** _±_ **2.8**<br>|
|Tray Lift|BCRNN|16.7 _±_ 2.5|**75.3** _±_ **7.5**|
|Pouring|DP|26.7 _±_ 2.5|**79.3** _±_ **0.9**|



TABLE III: Success rates of policies trained on data generated with DexMimicGen and Demo-noise baseline. 

## _C. DexMimicGen Analysis_ 

**How does DexMimicGen data generation compare to alternatives?** We compare DexMimicGen with a DemoNoise data generation baseline, which takes the same source demonstrations as DexMimicGen, but generates data by replaying the source demos with action noise during execution. In Table III, we train policies on datasets of 1000 demos generated by both DexMimicGen and the DemoNoise baseline. We can see that the policies trained using DexMimicGen outperform those trained on the Demo-Noise baseline by more than 58% across all tasks. Furthermore, unlike DexMimicGen, the Demo-Noise baseline cannot generate results on _D_ 1 and _D_ 2, as it can only replay the same initial configurations in the source demos. 

**Do larger datasets boost policy performance?** We train policies on 100, 500, 1000, and 5000 demos generated by DexMimicGen across several tasks (Fig. 5). We observe significant boosts in performance from 100 to 500 and 1000, showing that increasing dataset size boosts performance in this data regime; however, the success rate does not always increase from 1000 to 5000, suggesting that there can be diminishing returns depending on the task. 

**How do different DexMimicGen data generation strategies impact results?** First, we compare the Replay and Transform schemes in the coordination subtask (Sec. IVB). Specifically, we evaluate two tasks involving the handover subtask with two distinct policies: Transport using BCRNN+GMM, and Can Sorting using a diffusion policy. Replay demonstrates better policy performance (63.3% vs. 46.0%) in the Transport task and achieves comparable outcomes (97.3% vs. 98.6%) in the Can Sorting task. Thus, Replay is our default choice for tasks that involve handover. 

Next, we assess the effectiveness of ordering constraints in sequential subtasks (Sec. IV-C). When using the same source demonstration for both arms, subtask ordering requirements are typically satisfied automatically. In contrast, employing different source demonstrations for each arm requires an ordering constraint but also increases data diversity. We also evaluate two tasks involving the sequential subtasks with two distinct policies: Drawer Cleanup with BCRNN, and Pouring with diffusion policy. We found training on data generated with ordering constraints consistently outperforms training without them (50.7% vs. 48.0% in Drawer Cleanup and 88.7% vs. 76.7% in Pouring). Directly using the same source demo yields the policy success rates of 56.7% in the Drawer Cleanup and 79.3% in Pouring. 

**How do different policy architecture choices affect success rates?** In Table I, we also compare the performance of different policy architectures (Diffusion Policy [54], BCRNN-GMM [1], BC-RNN [1] with no GMM action head) 



Fig. 6: **Real-World DexMimicGen Deployment.** Rollouts of real-world visuomotor policy trained with DexMimicGen data and digital twin. 

on the datasets generated by DexMimicGen. We found that Diffusion Policy [54] generally outperforms the other architectures. Interestingly, we also found that BC-RNNGMM generally underperformed BC-RNN and Diffusion Policy, especially on tasks that involve dexterous hands, in contrast to the RoboMimic study [1] which found the use of a GMM head to be beneficial. We believe DexMimicGen datasets will make it easier for future work to study further how imitation learning choices might differ in the bimanual dexterous manipulation setting. 

## _D. Real-World Evaluation_ 

We showcase how DexMimicGen enables real-world deployment using the pipeline illustrated in Fig. 1. We generate real-world demonstrations by running DexMimicGen with a digital twin [77] in simulation. 

**Hardware Setup.** We use a Fourier GR1 robot equipped with two 6-DoF Inspire dexterous hands. For vision, we use two Intel RealSense D435i cameras: one head-mounted camera provides a first-person view and one camera in front of the robot as a third-person view. 

**Digital Twin Setup.** We perform our experiment on the Can Sorting task (Fig. 6), with digital twin assets in simulation that align with the real-world setup. To ensure accurate alignment between the real-world and simulated environments, we perform pose estimation on the objects prior to data collection. Using the head-mounted camera, we capture an initial RGB-D frame and apply GroundingDINO [78] to segment an RGB mask of the object. We use the real world object’s center point (determined by averaging the depth values within the RGB mask) to initialize the object’s _x−_ and _y−_ coordinates in simulation. 

**Data Collection Pipeline.** Using the teleoperation pipeline described in Sec. V, we collect four source human demonstrations for the Can Sorting task. These demonstrations are replayed in simulation, and are used as source demonstrations for DexMimicGen in the digital twin. Next, new real-world demonstrations are collected by synchronizing the initial object state from real to sim, and then attempting to generate a new demonstration in sim with DexMimicGen. If the demonstration is successful in simulation, the sequence of robot control actions is sent to the real-world for execution. In this way, the digital twin functions to ensure safety during 

real-world data generation, while DexMimicGen mitigates human effort for data collection, which is autonomous apart from the environment resets. We generate 40 successful demonstrations with the approach described above. 

**Results.** We compare visuomotor policies trained using Diffusion Policy [54] on the 40 DexMimicGen demos with one trained on the 4 source demos. We evaluated both models by running 10 trials each for the red and blue cups. The policy trained on DexMimicGen data achieves 90% success, while the model trained on the source data achieves 0%; DexMimicGen thus offers an efficient pipeline for training real-world robots through the use of a digital twin. 

## VII. CONCLUSION 

We introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a small number of human demonstrations for bimanual and dexterous robots, and a collection of nine simulation environments across three embodiments requiring different coordination behaviors. Our findings from applying DexMimicGen to these tasks show that there is great value in further investigating policy learning in this setting. We also deploy DexMimicGen on a real humanoid robot through a real2sim2real pipeline. We hope the release of our DexMimicGen datasets and environments will facilitate future research. 

## ACKNOWLEDGMENT 

We appreciate Fourier Intelligence for hardware support. We also thank Yifeng Zhu, Abhiram Maddukuri, Soroush Nasiriany, and Yu Fang for their help with robosuite, and Akul Santhosh and Abhishek Joshi for their help with rendering, and Toru Lin and Tairan He for valuable discussions. 

REFERENCES 

- [1] A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Mart´ın-Mart´ın, “What matters in learning from offline human demonstrations for robot manipulation,” in _Conference on Robot Learning (CoRL)_ , 2021. 

- [2] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, _et al._ , “Rt-1: Robotics transformer for real-world control at scale,” _arXiv preprint arXiv:2212.06817_ , 2022. 

- [3] T. Zhang, Z. McCarthy, O. Jow, D. Lee, X. Chen, K. Goldberg, and P. Abbeel, “Deep imitation learning for complex manipulation tasks from virtual reality teleoperation,” in _2018 IEEE international conference on robotics and automation (ICRA)_ . IEEE, 2018, pp. 5628–5635. 

- [4] A. Mandlekar, Y. Zhu, A. Garg, J. Booher, M. Spero, A. Tung, J. Gao, J. Emmons, A. Gupta, E. Orbay, S. Savarese, and L. Fei-Fei, “RoboTurk: A Crowdsourcing Platform for Robotic Skill Learning through Imitation,” in _Conference on Robot Learning_ , 2018. 

- [5] F. Ebert, Y. Yang, K. Schmeckpeper, B. Bucher, G. Georgakis, K. Daniilidis, C. Finn, and S. Levine, “Bridge Data: Boosting Generalization of Robotic Skills with Cross-Domain Datasets,” in _Proceedings of Robotics: Science and Systems_ , New York City, NY, USA, 6 2022. 

- [6] A. Brohan, Y. Chebotar, C. Finn, K. Hausman, A. Herzog, D. Ho, J. Ibarz, A. Irpan, E. Jang, R. Julian, _et al._ , “Do as i can, not as i say: Grounding language in robotic affordances,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 287–318. 

- [7] E. Jang, A. Irpan, M. Khansari, D. Kappler, F. Ebert, C. Lynch, S. Levine, and C. Finn, “Bc-z: Zero-shot task generalization with robotic imitation learning,” in _Conference on Robot Learning_ . PMLR, 2022, pp. 991–1002. 

- [8] C. Lynch, A. Wahid, J. Tompson, T. Ding, J. Betker, R. Baruch, T. Armstrong, and P. Florence, “Interactive language: Talking to robots in real time,” _IEEE Robotics and Automation Letters_ , 2023. 

- [9] K. Darvish, L. Penco, J. Ramos, R. Cisneros, J. Pratt, E. Yoshida, S. Ivaldi, and D. Pucci, “Teleoperation of humanoid robots: A survey,” _IEEE Transactions on Robotics_ , vol. 39, no. 3, pp. 1706–1727, 2023. 

- [10] R. Ding, Y. Qin, J. Zhu, C. Jia, S. Yang, R. Yang, X. Qi, and X. Wang, “Bunny-visionpro: Real-time bimanual dexterous teleoperation for imitation learning,” _arXiv preprint arXiv:2407.03162_ , 2024. 

- [11] X. Cheng, J. Li, S. Yang, G. Yang, and X. Wang, “Open-television: teleoperation with immersive active visual feedback,” _arXiv preprint arXiv:2407.01512_ , 2024. 

- [12] T. He, Z. Luo, W. Xiao, C. Zhang, K. Kitani, C. Liu, and G. Shi, “Learning human-to-humanoid real-time whole-body teleoperation,” _arXiv preprint arXiv:2403.04436_ , 2024. 

- [13] T. He, Z. Luo, X. He, W. Xiao, C. Zhang, W. Zhang, K. Kitani, C. Liu, and G. Shi, “Omnih2o: Universal and dexterous humanto-humanoid whole-body teleoperation and learning,” _arXiv preprint arXiv:2406.08858_ , 2024. 

- [14] Z. Fu, Q. Zhao, Q. Wu, G. Wetzstein, and C. Finn, “Humanplus: Humanoid shadowing and imitation from humans,” _arXiv preprint arXiv:2406.10454_ , 2024. 

- [15] M. Dalal, A. Mandlekar, C. R. Garrett, A. Handa, R. Salakhutdinov, and D. Fox, “Imitating task and motion planning with visuomotor transformers,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 2565–2593. 

- [16] Y. Wang, Z. Xian, F. Chen, T.-H. Wang, Y. Wang, K. Fragkiadaki, Z. Erickson, D. Held, and C. Gan, “Robogen: Towards unleashing infinite data for automated robot learning via generative simulation,” in _Forty-first International Conference on Machine Learning_ , 2023. 

- [17] A. Mandlekar, S. Nasiriany, B. Wen, I. Akinola, Y. Narang, L. Fan, Y. Zhu, and D. Fox, “Mimicgen: A data generation system for scalable robot learning using human demonstrations,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 1820–1864. 

- [18] A. Mandlekar, J. Booher, M. Spero, A. Tung, A. Gupta, Y. Zhu, A. Garg, S. Savarese, and L. Fei-Fei, “Scaling robot supervision to hundreds of hours with roboturk: Robotic manipulation dataset through human reasoning and dexterity,” in _2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2019, pp. 1048–1055. 

- [19] A. Mandlekar, D. Xu, R. Mart´ın-Mart´ın, Y. Zhu, L. Fei-Fei, and S. Savarese, “Human-in-the-loop imitation learning using remote teleoperation,” _arXiv preprint arXiv:2012.06733_ , 2020. 

- [20] J. Wong, A. Tung, A. Kurenkov, A. Mandlekar, L. Fei-Fei, S. Savarese, and R. Mart´ın-Mart´ın, “Error-aware imitation learning from teleoperation data for mobile manipulation,” in _Conference on Robot Learning_ . PMLR, 2022, pp. 1367–1378. 

- [21] P. Wu, Y. Shentu, Z. Yi, X. Lin, and P. Abbeel, “Gello: A general, lowcost, and intuitive teleoperation framework for robot manipulators,” 2023. 

- [22] A. Iyer, Z. Peng, Y. Dai, I. Guzey, S. Haldar, S. Chintala, and L. Pinto, “Open teach: A versatile teleoperation system for robotic manipulation,” _arXiv preprint arXiv:2403.07870_ , 2024. 

- [23] S. Dass, W. Ai, Y. Jiang, S. Singh, J. Hu, R. Zhang, P. Stone, B. Abbatematteo, and R. Mart´ın-Mart´ın, “Telemoma: A modular and versatile teleoperation system for mobile manipulation,” in _2nd Workshop on Mobile Manipulation and Embodied Intelligence at ICRA 2024_ , 2024. 

- [24] A. Tung, J. Wong, A. Mandlekar, R. Mart´ın-Mart´ın, Y. Zhu, L. FeiFei, and S. Savarese, “Learning multi-arm manipulation through collaborative teleoperation,” in _2021 IEEE International Conference on Robotics and Automation (ICRA)_ . IEEE, 2021, pp. 9212–9219. 

- [25] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware,” in _Proceedings of Robotics: Science and Systems_ , Daegu, Republic of Korea, 7 2023. 

- [26] J. Aldaco, T. Armstrong, R. Baruch, J. Bingham, S. Chan, K. Draper, D. Dwibedi, C. Finn, P. Florence, S. Goodrich, _et al._ , “Aloha 2: An enhanced low-cost hardware for bimanual teleoperation,” _arXiv preprint arXiv:2405.02292_ , 2024. 

- [27] T. Lin, Y. Zhang, Q. Li, H. Qi, B. Yi, S. Levine, and J. Malik, “Learning visuotactile skills with two multifingered hands,” _arXiv preprint arXiv:2404.16823_ , 2024. 

- [28] S. Schaal, “Is imitation learning the route to humanoid robots?” _Trends in cognitive sciences_ , vol. 3, no. 6, pp. 233–242, 1999. 

- [29] H. Fang, H.-S. Fang, Y. Wang, J. Ren, J. Chen, R. Zhang, W. Wang, and C. Lu, “Low-cost exoskeletons for learning whole-arm manipulation in the wild,” in _Towards Generalist Robots: Learning Paradigms for Scalable Skill Acquisition@ CoRL2023_ , 2023. 

- [30] C. Chi, Z. Xu, C. Pan, E. Cousineau, B. Burchfiel, S. Feng, R. Tedrake, and S. Song, “Universal manipulation interface: In-the-wild robot teaching without in-the-wild robots,” in _Proceedings of Robotics: Science and Systems (RSS)_ , 2024. 

- [31] H. Etukuru, N. Naka, Z. Hu, S. Lee, J. Mehu, A. Edsinger, C. Paxton, S. Chintala, L. Pinto, and N. M. M. Shafiullah, “Robot utility models: General policies for zero-shot deployment in new environments,” 2024. 

- [32] S. James, Z. Ma, D. R. Arrojo, and A. J. Davison, “Rlbench: The robot learning benchmark & learning environment,” _IEEE Robotics and Automation Letters_ , vol. 5, no. 2, pp. 3019–3026, 2020. 

- [33] A. Zeng, P. Florence, J. Tompson, S. Welker, J. Chien, M. Attarian, T. Armstrong, I. Krasin, D. Duong, V. Sindhwani, _et al._ , “Transporter networks: Rearranging the visual world for robotic manipulation,” in _Conference on Robot Learning_ . PMLR, 2021, pp. 726–747. 

- [34] Y. Jiang, A. Gupta, Z. Zhang, G. Wang, Y. Dou, Y. Chen, L. FeiFei, A. Anandkumar, Y. Zhu, and L. Fan, “Vima: General robot manipulation with multimodal prompts,” in _Fortieth International Conference on Machine Learning_ , 2023. 

- [35] J. Gu, F. Xiang, X. Li, Z. Ling, X. Liu, T. Mu, Y. Tang, S. Tao, X. Wei, Y. Yao, _et al._ , “Maniskill2: A unified benchmark for generalizable manipulation skills,” in _The Eleventh International Conference on Learning Representations_ , 2023. 

- [36] H. Ha, P. Florence, and S. Song, “Scaling up and distilling down: Language-guided robot skill acquisition,” in _Conference on Robot Learning_ . PMLR, 2023, pp. 3766–3777. 

- [37] R. Hoque, A. Mandlekar, C. R. Garrett, K. Goldberg, and D. Fox, “Interventional data generation for robust and data-efficient robot imitation learning,” in _First Workshop on Out-of-Distribution Generalization in Robotics at CoRL 2023_ , 2023. [Online]. Available: https://openreview.net/forum?id=ckFRoOaA3n 

- [38] S. Nasiriany, A. Maddukuri, L. Zhang, A. Parikh, A. Lo, A. Joshi, A. Mandlekar, and Y. Zhu, “Robocasa: Large-scale simulation of everyday tasks for generalist robots,” in _Robotics: Science and Systems (RSS)_ , 2024. 

- [39] D. A. Pomerleau, “Alvinn: An autonomous land vehicle in a neural network,” in _Advances in neural information processing systems_ , 1989, pp. 305–313. 

- [40] C. Finn, T. Yu, T. Zhang, P. Abbeel, and S. Levine, “One-shot visual imitation learning via meta-learning,” in _Conference on robot learning_ . PMLR, 2017, pp. 357–368. 

- [41] A. Billard, S. Calinon, R. Dillmann, and S. Schaal, “Robot programming by demonstration,” in _Springer Handbook of Robotics_ , 2008. 

- [42] S. Calinon, F. D’halluin, E. L. Sauser, D. G. Caldwell, and A. Billard, “Learning and reproduction of gestures by imitation,” _IEEE Robotics and Automation Magazine_ , vol. 17, pp. 44–54, 2010. 

- [43] A. Mandlekar, D. Xu, R. Mart´ın-Mart´ın, S. Savarese, and L. Fei-Fei, “GTI: Learning to Generalize across Long-Horizon Tasks from Human Demonstrations,” in _Proceedings of Robotics: Science and Systems_ , Corvalis, Oregon, USA, 7 2020. 

- [44] C. Wang, R. Wang, A. Mandlekar, L. Fei-Fei, S. Savarese, and D. Xu, “Generalization through hand-eye coordination: An action space for learning spatially-invariant visuomotor control,” in _2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ . IEEE, 2021, pp. 8913–8920. 

- [45] C. Lynch, M. Khansari, T. Xiao, V. Kumar, J. Tompson, S. Levine, and P. Sermanet, “Learning latent plans from play,” in _Conference on Robot Learning_ , 2019. 

- [46] K. Pertsch, Y. Lee, Y. Wu, and J. J. Lim, “Demonstration-guided reinforcement learning with learned skills,” in _Conference on Robot Learning_ , 2021. 

- [47] A. Ajay, A. Kumar, P. Agrawal, S. Levine, and O. Nachum, “Opal: Offline primitive discovery for accelerating offline reinforcement learning,” in _International Conference on Learning Representations_ , 2021. 

- [48] K. Hakhamaneshi, R. Zhao, A. Zhan, P. Abbeel, and M. Laskin, “Hierarchical few-shot imitation with skill transition models,” in _International Conference on Learning Representations_ , 2021. 

- [49] Y. Zhu, P. Stone, and Y. Zhu, “Bottom-up skill discovery from unsegmented demonstrations for long-horizon robot manipulation,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, pp. 4126–4133, 2022. 

- [50] S. Nasiriany, T. Gao, A. Mandlekar, and Y. Zhu, “Learning and retrieval from prior data for skill-based imitation learning,” in _Conference on Robot Learning (CoRL)_ , 2022. 

- [51] M. Drolet, S. Stepputtis, S. Kailas, A. Jain, J. Peters, S. Schaal, and H. Ben Amor, “A comparison of imitation learning algorithms for bimanual manipulation,” _IEEE Robotics and Automation Letters (RAL)_ , 2024. 

- [52] A. J. Ijspeert, J. Nakanishi, and S. Schaal, “Movement imitation with nonlinear dynamical systems in humanoid robots,” _Proceedings 2002 IEEE International Conference on Robotics and Automation_ , vol. 2, pp. 1398–1403 vol.2, 2002. 

- [53] M. Seo, S. Han, K. Sim, S. H. Bang, C. Gonzalez, L. Sentis, and Y. Zhu, “Deep imitation learning for humanoid loco-manipulation through human teleoperation,” in _2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids)_ . IEEE, 2023, pp. 1–8. 

- [54] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. Burchfiel, and S. Song, “Diffusion policy: Visuomotor policy learning via action diffusion,” in _Proceedings of Robotics: Science and Systems (RSS)_ , 2023. 

- [55] P. Mitrano and D. Berenson, “Data Augmentation for Manipulation,” in _Proceedings of Robotics: Science and Systems_ , New York City, NY, USA, 6 2022. 

- [56] M. Laskin, K. Lee, A. Stooke, L. Pinto, P. Abbeel, and A. Srinivas, “Reinforcement learning with augmented data,” _Advances in neural information processing systems_ , vol. 33, pp. 19 884–19 895, 2020. 

- [57] D. Yarats, I. Kostrikov, and R. Fergus, “Image augmentation is all you need: Regularizing deep reinforcement learning from pixels,” in _International conference on learning representations_ , 2021. 

visual imitation learning,” in _CoRL 2022 Workshop on Pre-training Robot Learning_ , 2022. 

   - [64] T. Yu, T. Xiao, A. Stone, J. Tompson, A. Brohan, S. Wang, J. Singh, C. Tan, J. Peralta, B. Ichter, _et al._ , “Scaling robot learning with semantically imagined experience,” _arXiv preprint arXiv:2302.11550_ , 2023. 

   - [65] Z. Chen, S. Kiami, A. Gupta, and V. Kumar, “Genaug: Retargeting behaviors to unseen situations via generative augmentation,” _arXiv preprint arXiv:2302.06671_ , 2023. 

   - [66] H. Bharadhwaj, J. Vakil, M. Sharma, A. Gupta, S. Tulsiani, and V. Kumar, “Roboagent: Generalization and efficiency in robot manipulation via semantic augmentations and action chunking,” in _First Workshop on Out-of-Distribution Generalization in Robotics at CoRL 2023_ , 2023. 

   - [67] X. Zhang, M. Chang, P. Kumar, and S. Gupta, “Diffusion meets dagger: Supercharging eye-in-hand imitation learning,” _arXiv preprint arXiv:2402.17768_ , 2024. 

   - [68] S. Tian, B. Wulfe, K. Sargent, K. Liu, S. Zakharov, V. Guizilini, and J. Wu, “View-invariant policy learning via zero-shot novel view synthesis,” in _Conference on Robot Learning (CoRL)_ , Munich, Germany, 2024. 

   - [69] L. Y. Chen, C. Xu, K. Dharmarajan, M. Z. Irshad, R. Cheng, K. Keutzer, M. Tomizuka, Q. Vuong, and K. Goldberg, “Rovi-aug: Robot and viewpoint augmentation for cross-embodiment robot learning,” in _Conference on Robot Learning (CoRL)_ , Munich, Germany, 2024. 

   - [70] Y. Zhu, J. Wong, A. Mandlekar, and R. Mart´ın-Mart´ın, “robosuite: A modular simulation framework and benchmark for robot learning,” in _arXiv preprint arXiv:2009.12293_ , 2020. 

   - [71] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for model-based control,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems_ , 2012, pp. 5026–5033. 

   - [72] O. Khatib, “A unified approach for motion and force control of robot manipulators: The operational space formulation,” _IEEE Journal on Robotics and Automation_ , vol. 3, no. 1, pp. 43–53, 1987. 

   - [73] K. Zakka, “mink,” 2024. [Online]. Available: https://github.com/ kevinzakka/mink 

   - [74] S. Caron, Y. De Mont-Marin, R. Budhiraja, S. H. Bang, I. Domrachev, and S. Nedelchev, “Pink: Python inverse kinematics based on Pinocchio,” 2024. [Online]. Available: https://github.com/ stephane-caron/pink 

   - [75] Y. Park and P. Agrawal, “Using apple vision pro to train and control robots,” 2024. [Online]. Available: https://github.com/Improbable-AI/ VisionProTeleop 

   - [76] N. Chernyadev, N. Backshall, X. Ma, Y. Lu, Y. Seo, and S. James, “Bigym: A demo-driven mobile bi-manual manipulation benchmark,” _arXiv preprint arXiv:2407.07788_ , 2024. 

   - [77] Z. Jiang, C.-C. Hsu, and Y. Zhu, “Ditto: Building digital twins of articulated objects from interaction,” in _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2022, pp. 5616–5626. 

   - [78] S. Liu, Z. Zeng, T. Ren, F. Li, H. Zhang, J. Yang, C. Li, J. Yang, H. Su, J. Zhu, _et al._ , “Grounding dino: Marrying dino with grounded pre-training for open-set object detection,” _arXiv preprint arXiv:2303.05499_ , 2023. 

   - [79] C. Garrett, A. Mandlekar, B. Wen, and D. Fox, “Skillmimicgen: Automated demonstration generation for efficient skill learning and deployment,” _arXiv preprint arXiv:2410.18907_ , 2024. 

- [58] S. Young, D. Gandhi, S. Tulsiani, A. Gupta, P. Abbeel, and L. Pinto, “Visual imitation made easy,” _arXiv e-prints_ , pp. arXiv–2008, 2020. 

- [59] A. Zhan, R. Zhao, L. Pinto, P. Abbeel, and M. Laskin, “A framework for efficient robotic manipulation,” in _Deep RL Workshop NeurIPS 2021_ , 2021. 

- [60] S. Sinha, A. Mandlekar, and A. Garg, “S4rl: Surprisingly simple self-supervision for offline reinforcement learning in robotics,” in _Conference on Robot Learning_ . PMLR, 2022, pp. 907–917. 

- [61] S. Pitis, E. Creager, and A. Garg, “Counterfactual data augmentation using locally factored dynamics,” _Advances in Neural Information Processing Systems_ , vol. 33, pp. 3976–3990, 2020. 

- [62] S. Pitis, E. Creager, A. Mandlekar, and A. Garg, “Mocoda: modelbased counterfactual data augmentation,” in _Proceedings of the 36th International Conference on Neural Information Processing Systems_ , 2022, pp. 18 143–18 156. 

- [63] Z. Mandi, H. Bharadhwaj, V. Moens, S. Song, A. Rajeswaran, and V. Kumar, “Cacti: A framework for scalable multi-task multi-scene 

## VIII. APPENDIX OVERVIEW 

The Appendix contains the following content. 

- **Implementation Details** (Appendix IX): more details of DexMimicGen implementation. 

- **Result Analysis** (Appendix X): analysis of DexMimicGen results. 

- **Author Contributions** (Appendix XI): list of each author’s contributions to the paper. 

## IX. IMPLEMENTATION DETAILS 

**Which parts of the DexMimicGen process rely on human input versus automation?** 

- The source demonstration collection requires human teleoperation. 

- Similar to MimicGen, we have two options for segmenting the source demonstrations. The first option relies on manually defined heuristics, where we implement subtask terminal signals — e.g., detecting when the hand makes contact with the target object in simulation — and automatically segment the source demonstrations by checking the corresponding simulation states. The second option involves manually segmenting each demonstration, which requires more human effort but offers greater flexibility, especially when subtask terminal signals are difficult to define. 

- By default all subtasks are parallel subtasks. We need to manually specify which pairs of subtasks are coordination subtasks or sequential subtasks if required. 

Once the source demonstrations are collected and segmented, and the subtask structure is specified, the data generation process is fully automated. 

**How does DexMimicGen determine the success condition** 

**of a task?** We implement a success check function for each task. Typically, success is determined based on the final simulation state, such as whether the object of interest is placed in the target container. The success check is used for filtering out failed demonstrations during the data generation phase. 

**How does DexMimicGen handle collisions between the robots and objects?** DexMimicGen does not explicitly handle collisions. Some failure cases during the data generation phase result from collisions between the generated trajectory and objects in the workspace. To mitigate this issue, we plan to extend DexMimicGen with motion planning modules from SkillMimicGen [79] for future work. 

## X. RESULT ANALYSIS 

**What factors contributed to the low success rate of certain tasks?** For instance, the threading task has a success rate below 70%. We hypothesize that in this task, both the threading object and the hole are occluded from the thirdperson camera, making it challenging for the vision-based policy to complete the task successfully. To address this issue, we could incorporate visual reinforcement learning to enable active perception and improve dexterous control. We 



<!-- Start of picture text -->
End-Effector Position Finger Joints<br>0.15 1.0 GeneratedSource<br>0.10<br>0.05 0.5<br>0.00<br>0.0<br>0.05<br>0.10 0.5<br>0.15<br>Generated 1.0<br>0.20 Source<br>0.3 0.2 0.1 0.0 0.1 0.2 0.3 2 1 0 1 2<br><!-- End of picture text -->

Fig. 7: **Visualization of generated and source action distributions.** We run PCA to project actions into 2D and visualize them. 

believe it will facilitate the policies to accomplish the tasks under high occlusions. 

**How does the DexMimicGen process augment the data distribution?** To further analyze the data generation process of DexMimicGen, we visualize the PCA projections of endeffector poses and finger joint actions for both generated and source demonstrations in the TwoArmCoffee task (Fig. 7). The results show that DexMimicGen significantly expands the distribution coverage of end-effector actions. In contrast, for finger joint actions, DexMimicGen primarily performs local interpolation rather than broad expansion. 

## XI. AUTHOR CONTRIBUTIONS 

**Zhenyu Jiang.** Co-led project ideation and development. Implemented the data generation code and simulation environments. Oversaw the development of the teleoperation and control infrastructure. Ran most of the experiments in the paper, and wrote the paper. 

**Yuqi Xie.** Core developer of the project. Developed the simulation environments, teleoperation infrastructure for simulation, and rendering pipeline. Ran part of the experiments for humanoids, and the real robot experiments. 

**Kevin Lin.** Core developer of the project. Developed the control infrastructure for the simulation experiments, including whole-body IK controllers. Ran part of the experiments for humanoids. 

**Zhenjia Xu.** Implemented the real robot teleoperation and policy deployment infrastructure and helped oversee the real robot experiments. 

**Weikang Wan.** Implemented the initial prototype of the data generation code and ran the BiGym [76] experiments. 

**Ajay Mandlekar.** Co-led project ideation and development. Implemented simulation environments. Oversaw the development of the main algorithm for data generation, the simulation environments, and the experiments presented in the paper. Advised on the project and wrote the paper. 

**Linxi Fan.** Co-led project ideation and development. Led resource acquisition for the project, including robot hardware and cluster compute. Provided feedback on paper writing. 

**Yuke Zhu.** Co-led project ideation and development. Provided feedback on experiments and presentation, and wrote the paper. 

