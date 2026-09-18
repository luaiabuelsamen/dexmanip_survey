# **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** 

**Zhi Jing**<sup>**1,2**</sup> **Siyuan Yang**<sup>**3,2**</sup> **Jicong Ao**<sup>**2**</sup> **Ting Xiao**<sup>**4**</sup> **Yu-Gang Jiang**<sup>**1**</sup> **Chenjia Bai**<sup>**† 2**</sup> 

1Fudan University‡ 2Institute of Artificial Intelligence (TeleAI), China Telecom‡ 

3University of Science and Technology of China 

4East China University of Science and Technology 

## **Abstract** 

For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is `https://openhumanoidgen.github.io` . 

## **1 Introduction** 

The long-term goal of embodied manipulation is to achieve human-like manipulation capabilities across versatile scenes and tasks [1, 2]. Humanoid robots, with their human-like morphology, offer a universal platform capable of leveraging bimanual coordination and dexterous hand manipulation [3, 4], potentially enabling more complex tasks than conventional robot arms. Bimanual dexterous manipulation is inherently intricate due to the requirement for coordinated arm movements and hand operations, which in turn makes the collection of the demonstration dataset more challenging. 

The existing data generation pipeline for humanoid robots primarily depends on teleoperation systems via Virtual Reality (VR) [5, 6] and exoskeleton devices [7, 8, 9]. However, teleoperation requires the deployment of numerous real-world objects and scenes, and also requires proficient operational skills from human operators. This makes it difficult for the dataset to cover diverse real-world tasks and scenarios. Consequently, existing real-world datasets such as Open-X [10, 11, 12, 13] consist mainly of single-arm manipulation data. To address this issue, many researchers have turned to various simulators for data acquisition, such as SAPIEN [14], IsaacSim [15], and MuJoCo [16]. In the context of bimanual manipulation, simulated benchmarks such as Aloha [17], PerAct2 [18], and RoboTwin [19] utilize dual-arm or wheeled robots for task creation and data collection. These efforts are limited in terms of task diversity and generally do not involve dexterous hands. Similarly, HumanoidBench 

> † Correspondence to: Chenjia Bai (baicj@chinatelecom.cn) ‡ Equally leading organizations 

39th Conference on Neural Information Processing Systems (NeurIPS 2025). 



<!-- Start of picture text -->
Spatial Annotation Demonstration Generation Scene Scaling<br>Hand Annotation Asset Annotation Layout Scaling Style Scaling<br>Task: Open Drawer<br>Initial<br>Initial State<br>Scene Generation<br>(3)Backpropagation<br>Executed Action<br>(1) Select<br>Current State<br>Assets Primitive Scene<br>Attributes “Create new task scene" Description Prohibited Action S (2) Expand Policy Evaluation<br>LLM TC State LR<br>LLM Exe Code R ActionJoint Data LR Point Cloud<br>Close Box Pour Cup Block Storage Constraints(p & v) DP3<br>Env Code (Asset Setup, Success Criteria) + = Succeed DP<br>Image<br><!-- End of picture text -->

Figure 1: The overview of HumanoidGen. It includes spatial annotations, scene generation, constraint generation, MCTS-enhanced reasoning, data collection, scene scaling, and policy evaluation. 

[20] and BiGym [21] use humanoid robots to perform loco-manipulation tasks but depend on VR or reinforcement learning (RL) policies for data collection, which would be costly considering that humanoid robots require coordinated control of arms and dexterous hands. Therefore, a more efficient approach is to allocate rich interactable assets in simulation for task creation and develop a fully autonomous paradigm for data collection. Taking inspiration from LLM-driven planning methods [22, 23], our goal is to generate code-form planning to complete humanoid manipulation tasks, aiming to produce high-quality demonstrations that can scale efficiently. 

In this paper, we propose **HumanoidGen** , an LLM-based framework capable of generating diverse manipulation tasks and collecting scalable demonstrations for humanoid robots. For task creation, an LLM planner is prompted to generate code for environment setup and success criteria based on language descriptions and the wealth of 3D assets.To gather demonstrations for each task, we first identify atomic operations for dexterous hands (such as pinch and grab), then we adopt LLMs to perform task decomposition for long-horizon tasks, generating spatial rational constraints for arm movements. Specifically, we give spatial annotations for assets, and the constraints are defined through geometrical relationships on contact points and the function axis for both the arm and entities. Then we conduct LLM-based code generation by translating planning into executable code-form constraints. An off-the-shelf trajectory optimizer is applied subsequently to solve the constraints to get the arm and hand movements. To further enhance reasoning efficiency in complex tasks with long constraint chains, we incorporate a variant of Monte Carlo tree search (MCTS) for better test-time reasoning. This approach strengthens the reasoning ability of LLMs, especially when the required spatial annotations are absent. 

Building on HumanoidGen, we develop a comprehensive benchmark called **HGen-Bench** for bimanual dexterous manipulation. In our setup, the Unitree H1-2 humanoid robot equipped with Inspire hands serves as the robotic platform, and SAPIEN [14] as the simulation engine for data collection. HGen-Bench consists of 20 tasks of varying difficulty levels. For each task, a chain of constraints that determines arm movements and hand operations is generated, taking into account the spatial relationship between the robot and the objects. Then the actions are obtained by solving the constrained optimization problem. We execute these actions in the simulator and record the successful trajectories as demonstrations. We evaluated the success rate in trajectory generation with randomized scene configurations. The results show that MCTS significantly improves the reasoning ability of LLMs for long-horizon tasks and insufficient annotations. We train both 2D and 3D diffusion policies on the generated data, and the results show that the performance of the policy improved continuously as more demonstrations are incorporated. 

## **2 Method** 

HumanoidGen is an automated framework for scene generation, demonstration collection, and data generalization for bimanual dexterous manipulation, aiming to provide high-quality demonstrations over diverse scenarios to facilitate data scaling and policy learning. The overview of our framework is shown in Fig. 1. (i) As preparation, the assets and dexterous hands are meticulously annotated 

2 



<!-- Start of picture text -->
Pouring<br>Axis Storage Point<br>Storage Axis<br>Pouring  Storage<br>Point Point<br>Storage Axis<br>Function  Grasp  Pinch  Press  Attach  Approach Parallel<br>Point Point Point Point Axis Axis Axis<br><!-- End of picture text -->

Figure 2: The spatial annotations, including key points and key axes for assets and hands, as well as the atomic operations of hands that include grasp, pinch, and press. 

with spatial information, allowing flexible and reliable LLM-based planning. In scene generation, the LLM planner aims to generate an environment setup with code-form configuration based on asset, scene, and task descriptions. (ii) Based on the generated scenes and pre-defined hand atomic operations, the LLM proceeds to generate the planning code of a chain of spatial constraints for subsequent data collection. (iii) For tasks with long-horizon planning and insufficient annotations, we employ MCTS with introspective exploration to enhance the reasoning ability of LLMs. (iv) Then, we collect demonstrations by executing the planning with augmented scenarios to enhance data diversity. These demonstrations are utilized to construct a humanoid manipulation benchmark for policy evaluation. 

### **2.1 Spatial Annotation and Scene Generation** 

**Spatial Annotation Preparation.** For efficient LLM planning with atomic hand operations, we conduct meticulous annotations, including key points and key axes for both assets and dexterous hands. As shown in Fig. 2, we categorize annotations into three types as follows. 

_Hand Atomic Operation._ The annotations of atomic operations indicate how the dexterous hands can interact with assets. For smooth operation execution, we perform the annotation for each atomic operation on both dexterous hands. As shown in Fig. 2, the key point and the axis vary in different atomic operations. When annotating the operation axes, we specifically categorized them into three types according to the finger movement of the atomic operation: _approach axes, attach axes_ , and _parallel axes_ . Take ‘pinch’ as an example, (i) its approach axis specifies the direction from which the dexterous hand should approach its pre-pinching pose. This ensures proper alignment for the pinching operation execution. (ii) The attach axis indicates the finger movement direction during the operation execution, pointing from the thumb tip to the index finger tip for ‘pinch’. (iii) The parallel axis, perpendicular to the first two and oriented parallel to the palm plane, typically specifies the object’s rotation axis during manipulation. This helps specify the rotation axis when manipulating an articulated object. 

_Asset Inherent Information._ Asset inherent information indicates how the asset performs its own functionality. Usually, they are the points and axes where the asset exerts its functions, which are used to indicate the interaction between objects. These points and axes vary according to the functionality of the asset. For example, in Fig. 2, the cup has two possible functions: pouring and storage, which correspond to different annotations on the point and the axis, respectively. 

_Asset Operation Annotations._ Asset operation annotations define the points and axes on an asset that indicate how various atomic operations can be applied to interact with it. Importantly, atomic operations do not have a one-to-one correspondence with assets: (i) Different operations can be performed on the same asset. For instance, both grasping and pinching can apply to a cup. (ii) The same operation can use different key points on the same asset. As shown in Fig. 2, grasping can target keypoints on both the upper and lower parts of a drawer. (iii) A single keypoint may support multiple operations, such as the endpoint of a box lid, which allows both grasping and pinching (Fig. 2). 

With annotations, we can abstract the scene information into a set of key points and key axes in the local frames of objects and hands separately. This facilitates the LLM’s spatial and relational understanding of the scene and tasks, providing the foundation for defining the constraints of various atomic operations. We also note that the recent approach [19] adopts Stable Diffusion to simplify the annotation process for similar assets, which can be integrated with our method. Implementation details and evaluation results are provided in Appendix A.1 and Appendix C.2. 

3 



<!-- Start of picture text -->
Action Frame Object Frame<br>Block Storage Point Constraints 1<br>Task Description<br>2<br>Scene Layout LLM Axis Constraints<br>3<br>Point Constraints<br>Asset Attribute<br>4<br>Axis Constraints<br>Grasp Drawer Pull Drawer<br>Left<br>Hand<br>Initial Pre-Grasp Move Grasp Move Open Hand<br>Step 0 1 2 3 4 5<br>Right<br>Hand<br>Initial Pre-Pinch Move Pinch Move Keep<br>Pinch cube<br>Handover cube<br>Move (L) Pre-Grasp (L) Storage<br>15 12 11 10 9 8 7 6<br>Open Hand (L) Move (L) Open Hand (R) Pinch (L) Move (L) Move (L)<br>14 13<br>Grasp (L) Move (L) Dynamic Collision Avoidance<br>Active Collision Avoidance<br>Collision Point Cloud<br><!-- End of picture text -->

Figure 3: An illustration of the generated plan for the task _block storage_ . The LLM is prompted with a task description, scene layout, and asset attributes to generate a step sequence. Each step is expressed using an atomic operation, along with its corresponding annotations. During plan execution, (i) from step 0 - 5, the left hand pulls out the drawer by grasping its handle, while the right hand simultaneously pinches and lifts the cube. (ii) From step 6 - 9, the left hand takes the cube from the right hand. (iii) From step 10 - 15, the left hand places the cube into the drawer and pushes the drawer back by grasping its handle. The LLM avoids collisions that would occur from directly moving to the pinching pose by planning a collision-free method during steps 6 - 7, demonstrating active collision avoidance. Additionally, the LLM proactively generates code to account for potential collisions with the drawer when performing free motion in the compact workspace, as illustrated in the bottom part. 

**Scene Generation.** Based on the annotations, an LLM planner is prompted to generate tabletoplevel task scenes and configurations according to the task description. To achieve this, we take the asset library information, scene details, and task requirements as the prompt, then the LLM planner generates task-setup code, determining the categories, quantities, placement poses, and other attributes of the selected assets. In addition, we employ LLMs to generate task success criteria to guide the execution process and determine when the task is completed. For instance, in the _cup pour_ task, the LLM must infer the size of cubes contained in the cup based on the cup’s size, and assign plausible positions for the cup, the cubes, and the target bowl. The success criterion is defined as all cubes being successfully placed inside the bowl. 

### **2.2 LLM-based Task Planning** 

We design an automated generation method to generate scripts of constraint chains, which are used to collect demonstrations with the help of trajectory optimizers. Our method significantly differs from the conventional methods, which use LLMs only for high-level task plan generation and require a wide array of predefined low-level operations [24]. Specifically, our method includes task decomposition, relational action constraints, and collision avoidance to enhance planning abilities. 

**Task Decomposition.** As shown in Fig. 3, the LLM planner decomposes the long-horizon task into an action sequence _S_ = _{S_ 1 _, S_ 2 _, ..., Sn}_ with _n_ steps according to the task description, where 

4 

each step _Si_ = ( _Si_<sup>_l, S_</sup> _i_<sup>_r_) includes left and right parts,with</sup><sup>_S_</sup> _i_<sup>_l, S_</sup> _i_<sup>_r∈{Ai, Mi}_,where</sup><sup>_Ai_and</sup><sup>_Mi_</sup> indicate hand operations and arm movements respectively. (i) For hand operation, the LLM selects _Ai_ from the atomic library _A_<sup>hand</sup> = _{A_<sup>pinch</sup> _, A_<sup>grasp</sup> _, ..., A_<sup>open</sup> _}_ at each step. (ii) For arm movements, we define two types of constraint: the goal pose constraint _Ci_<sup>goal</sup> and the path constraint _Ci_<sup>path</sup> . Using these two constraints, the motion planning problem can be transformed into a constrained optimization problem, denoted as _Mi_ = _{f_ ( _Ci_<sup>goal</sup> ) _, f_ ( _Ci_<sup>path</sup> ) _}_ , where the constraint _Ci_ is inferred by the LLM based on contextual atomic operations and functional reasoning related to movement, and _f_ ( _·_ ) is a constraints solver detailed in Appendix A.2. By employing task decomposition, the long-horizon task can be decomposed into atomic operations and constraint definition, effectively reducing the reasoning complexity while enhancing planning efficiency. 

**Relational Action Constraints.** Compared with conventional grippers, dexterous hands require more sophisticated motion constraints to accommodate diverse hand gestures and contact interactions. To systematically describe these relationships, we introduce a set of dynamic coordinate frames _F_ act that represent the contextual action space of each hand. Each frame _F_ = ( _p_ 1 _, . . . , pk_ ; _v_ 1 _, . . . , vm_ ) in _F_ act consists of key points _pi ∈_ R<sup>3</sup> and axes _vj ∈_ R<sup>3</sup> . The composition of _F_ act evolves dynamically according to the manipulation state: for instance, the left-hand action frame _F_ act<sup>_l_initially includes only</sup> _{Fl}_ , which defines the geometric properties of the hand itself, and extends to _{Fl, Fo}_ once a rigid grasp with object _o_ is established. Each constraint _c ∈{C_<sup>path</sup> _, C_<sup>goal</sup> _}_ specifies a geometric relation between an element of _F_ act and one from the global frame set _F_ all = _F_ obj _∪F_ hand _∪F_ world. These relations can take the form of point or axis correspondences, such as coincidence, parallelism, or orthogonality, allowing flexible encoding of motion intents. For example, in a grasping action (step 2 in Fig. 3), a goal constraint may enforce point coincidence and directional alignment, _p_<sup>hand</sup> grasp<sup>_≡p_handle</sup> grasp and _v_ approach<sup>hand</sup><sup>_∥v_</sup> approach<sup>handle.Duringthesubsequentpullingphase(step3),apathconstraint</sup><sup>_C_path=</sup> _{v_ grasp<sup>hand</sup><sup>_∥v_</sup> grasp<sup>handle</sup><sup>_}_is applied to ensure that the hand maintains a stable gesture throughout the motion.</sup> This formulation explicitly encodes the spatial logic underlying dexterous manipulation, enabling consistent and adaptive control across complex, multi-stage tasks. 

**Collision Avoidance.** Ensuring effective collision avoidance during atomic operations is a key challenge. We propose two solutions: (i) _Active Collision Avoidance._ The LLM planner generates atomic operation scripts that proactively incorporate collision avoidance behavior. This ensures the feasibility of the atomic operations, especially when a coordinate bimanual manipulation is necessary. For example, in _block stack_ , the left hand retracts from the stacking area to make space for the right hand. (ii) _Dynamic Collision Management._ The LLM planner dynamically manages collision checks to enable in-contact manipulation. Specifically, we maintain an object-ignoring list and let the LLM dynamically adjust it when generating scripts, thereby providing guidance for successful low-level trajectory optimization and execution. This is crucial for in-contact articulated object manipulation, whereas existing methods ignore this aspect or rely on manual processing in atomic operation programming. For example, in the _block storage_ task illustrated in Fig. 3, the LLM adds the drawer to the list to ignore the contact between the robot hand and the drawer when pulling the drawer out. After that, the drawer is removed from the list, enabling subsequent collision avoidance. This approach seamlessly integrates in-contact manipulation with free-space motion, significantly enhancing the framework’s ability to handle complex long-horizon dexterous tasks. 

### **2.3 Enhancing Reasoning with MCTS** 

When performing long-horizon tasks or encountering insufficiently annotated objects, LLMs lack sufficient prompts for reliable reasoning, which often leads to failed planning. To address this issue, we employ tree search to enhance the ability of multi-step reasoning in task planning. Specifically, we propose a novel _Segment-Truncate-Combine-Resume_ (STCR) mechanism that abstracts a planning search tree from LLMs’ outputs. By integrating MCTS exploration and exploitation strategies, the tree is iteratively expanded to derive an executable solution. 

**STCR mechanism.** Inspired by abstractions in proving problems [25, 26], STCR aims to abstract executable code into a tree to define nodes and branches, which includes four steps. (i) **_Segment._** By matching critical functions, the planning code is segmented into multiple steps according to the granularity of the execution. The segmentation is inferred by LLMs following a similar granularity as described in the task decomposition of §2.2, denoted as _S_ = _{S_ 1 _, S_ 2 _, ..., Sn}_ . (ii) **_Truncate._** The truncation is performed at the point where an error occurs. We execute the segmented steps sequentially until a code formatting error or action execution failure occurs (e.g., move or grasp 

5 

failed). We truncate the steps at the point of failure, discard the steps after the erroneous step, and retain the valid segments as _S_ remain = _{Si|_ 1 _≤ i ≤ k −_ 1 _}_ , where _Sk_ failed _._ (iii) **_Combine._** We merge atomic operations with consistent intent in _S_ remain to form a new execution sequence _S_ remain<sup>_′_=</sup><sup>_{S_</sup> 1<sup>_′, S_</sup> 2<sup>_′, . . . , S_</sup> _k_<sup>_′′} ,_</sup> where _k_<sup>_′_</sup> _< k −_ 1 _._ Operations such as _grasping_ and _pinching_ are implemented by multiple steps. These steps are abstracted into single execution units during tree search. For instance, if _S_ 1<sup>_′_representsagraspingactioncontainingtwomovesteps,then</sup> _S_ 1<sup>_′_=</sup><sup>_{A_pre</sup> 1<sup>_grasp</sup> _, M_ 2 _, M_ 3 _, A_<sup>grasp</sup> 4 _}_ denotes the combined action sequence. In the task tree, each combined action sequence _S_<sup>_′_</sup> represents an executable branch, and its terminal state serves as a new node in the tree structure. (iv) **_Resume._** For newly created nodes, the code of the executed sequence, the error code, and the scene state information are stored, which will be resumed when this node is selected in expansion. 

**Interactive Task Planning via MCTS.** Based on the tree built by STCR, we adopt MCTS as the tree search algorithm, consisting _Selection, Expansion_ , and _Backpropagation_ steps. Different from standard MCTS methods, we incorporate simulation steps into the expansion process to provide execution results of the nodes. The details are given in Appendix A.4. 

**Scene Scaling.** To enhance the data diversity, we perform room-level scene scaling that allows demonstrations to contain diverse scenes using demonstration scripts generated from table-level task scenes. We compute the transformation matrix between the coordinate systems of the original and new scenes to align the two scenes. The details are given in Appendix A.3. By harnessing diverse assets in RoboCasa [24], we can generalize demonstrations across over 120 scenes. This substantially diversifies the dataset’s task scene distribution, ensuring broad coverage of potential scenarios. 

## **3 The HumanoidGen Benchmark** 



Figure 4: HGen-Bench includes various dexterous bimanual manipulation tasks of varying difficulty. We provide different observation information and deploy the tasks in a home scene. 

Based on our framework, we construct a benchmark, **HGen-Bench** , for humanoid manipulation. We designed 20 tasks performed using Inspire hands mounted on the arms of the Unitree H1-2 humanoid robot, which has 7 DoFs for each arm and 6 DoFs for each hand, resulting in a 26-dimensional action space. The examples are given in Fig. 4. In front of the robot, we place a table and construct scenes with various objects, including small items such as blocks of various shapes and colors, articulated objects such as laptops and drawers, and everyday items such as bottles, cups, and plates. 

We design atomic operations to fully exploit the dexterity of the hands and define task difficulties from easy to hard settings. We also incorporate bimanual coordination tasks to leverage the capabilities of dual dexterous hands, as well as long-horizon tasks that require geometric reasoning from the LLM planner. To enhance variability, we randomize the initial position, pose, and joint angles of articulated objects within a certain range. We provide RGB and depth images from six camera views, located on both wrists, a first-person perspective, and three third-person views. The details are given in Appendix B. 

## **4 Related Works** 

**LLM-based Data Generation.** Leveraging foundation models to automatically generate diverse tasks and scenes is promising for scaling robotic data sets with minimal human effort. RoboGen [22] 

6 

is a generative robotic agent that generates scene components and configurations with language descriptions, and the skills are learned by optimizing LLM-generated reward functions. Gensim [23] adopts LLMs to generate codes to build scenes, simulations, and expert demonstrations. Gensim2 [27] further considers long-term and articulated tasks beyond pick-and-place tasks and incorporates reasoning models for planning. However, these approaches predominantly center on single-arm robots, whereas our work addresses bimanual dexterous manipulation tasks, which are of critical importance for humanoid robots. Regarding expert data collection, LLMs have been leveraged to generate functional control programs for grasp-oriented tasks [28, 29] or articulated object manipulation [30, 31]. In contrast, our method enables code-form planning by framing the manipulation task as a sequence of constraints, thereby eliminating the need for human intervention in defining the functions. Although Rekep [32], OmniManip [33], and RoboTwin [19] utilize spatial reasoning based on key points and axes, they have limitations in handling bimanual dexterous tasks. 

**Bimanual Manipulation.** Bimanual dexterous manipulation is promising in solving complex tasks through the coordinated operation of two arms. However, this area faces several challenges, including data scarcity [34, 35], enlarged action spaces [9], diverse collaboration modalities [36, 37], and the intricacies of dexterous hand control [15]. Recent advancements have led to the development of simulation benchmarks for dual-arm systems [21, 19] and humanoid robots [20]. Nonetheless, these benchmarks exhibit limitations in task and scene diversity and typically exclude dexterous hands. These problems motivate us to develop automatic mechanisms for constructing bimanual environments and generating demonstrations, with the aim of broadening the skills and scenarios encompassed within bimanual datasets. For bimanual policy learning, previous methods rely on human-object interaction [38, 39], geometric constraints [40], and arm-movement primitives [41, 42]. In contrast, we do not consider these priors and directly train the 2D and 3D diffusion policies [43, 44], enabling a direct assessment of the effectiveness of the data collection paradigm. 

**Datasets and Benchmarks.** Collecting real-world demonstrations is promising for acquiring realistic environmental observations and encompassing the target scenarios of robots. Recent representative datasets, including RT-1 [45], RH-20T [12], DROID [46], Bridge data [13], Open X-Embodiment [10], RoboMind [11], and Agibot World [47], have collected numerous manipulation tasks on specific hardware platforms. However, as we focus on humanoid robots, the embodiment differences make most of the data unsuitable for directly training bimanual dexterous policies. Although methods such as physically interpretable action space [48] and latent action space [2, 49] have been proposed, the adaptation of cross-embodiment data remains an open research challenge. Additionally, although several data augmentation techniques have been introduced [50, 51], the collection of largescale real-world data remains costly. On the simulation front, benchmarks such as ManiSkill [52], SIMPLER [53], RoboTwin [19], RoboCasa [24], and Garmentlab [54] provide extensive assets and task configurations, while we focus on auto-create task variations and data collection for humanoid robots. 

## **5 Experiments** 

We conducted the following three groups of experiments: (1) a comprehensive evaluation of demonstration generation and execution performance of our framework compared to Robotwin; (2) an effectiveness evaluation of MCTS in enhancing the demonstration generation process; and (3) a validity evaluation of the collected demonstration data in training bimanual dexterous manipulation policies. 

In addition to these main experiments, further analyses and evaluations are provided in the Appendix C, including real-world experiments (Appendix C.1), automatic asset annotation evaluation (Appendices C.2), additional challenging dexterous manipulation tasks (Appendix C.3), resource and efficiency analysis of HumanoidGen (Appendix C.4), comparison with existing generation frameworks (Appendix C.5), and comparison across different large models (Appendix C.6). 

### **5.1 Evaluation of Data Generation and Execution** 

**Experimental Setup.** To better show the superiority of our framework, we designed 20 different tabletop manipulation tasks and conducted a quantitative evaluation of the demonstration generation and execution capability of our framework. We divide the 20 tasks into 4 groups based on the following factors: the number of arms used, the length of task horizons, and the complexity of collision scenarios. This categorization allows for a more detailed evaluation of the frameworks’ 

7 



<!-- Start of picture text -->
Single arm, Single arm, Bimanual, Bimanual,<br>free motion space complex collision scenarios free motion space long-horizon, complex collision scenarios<br><!-- End of picture text -->

Figure 5: Experiment results of demonstration generation and execution capability. The tasks are categorized into 4 groups, with names based on the number of robotic arms required and their relative difficulty levels. The features of task categories are noted in parentheses. 

performance. We compare our method to RobotTwin, where we modify the official implementation to add dexterous hands and provide additional annotations to enable dexterous atomic operations. Besides, we prompt the LLM not to perform proactive dynamical collision management during inference , which reflects the default setup in Robotwin.Using the DeepSeek-R1 [55], we generate and execute the demonstration scripts with both frameworks and compare the final success rates. 

**Experimental Results.** As shown in Fig. 5, HumanoidGen demonstrates superior performance across all dexterous manipulation tasks, achieving an average success rate of over 50%. Except for some bimanual long-horizon tasks that involve higher complexity, most task types achieve a success rate above 75%. These results highlight the effectiveness of our framework, making automatic and efficient demonstration generation feasible in bimanual dexterous tasks. In comparison, Robotwin shows comparable performance on single-arm and bimanual short-horizon tasks, indicating that the spatial annotations related to dexterous atomic operations introduced in §2.1 are effective in allowing the dexterous hand to participate in automated demonstration execution for simpler scenarios. 

Notably, we observe that HumanoidGen outperforms Robotwin in long-horizon and complex collision tasks, such as the _close & open box_ in single-arm tasks and the _blocks stack easy & hard_ in bimanual tasks. Further analysis shows that HumanoidGen dynamically manages collision avoidance during inference, handling the collision scenarios flexibly. As an example, in the task _handover and storage_ , the collisions with the drawer are appropriately ignored to facilitate trajectory planning for an incontact pulling operation, while such collisions are taken into account when planning a path around the drawer to retrieve the cube with the right hand. Another example is the _close box_ task, where the robot hand circumvents the box lid with collision-awareness to reach an intermediate pose. Subsequently, these collisions are permitted during the flipping operation to complete the closure. These examples demonstrate the potential of our dynamic collision management approach in enabling efficient data collection for long-horizon tasks involving complex collision scenarios. 

### **5.2 Effectiveness Evaluation of MCTS** 

**Experimental Setup.** To evaluate the effectiveness of MCTS in enhancing the demonstration generation process of HumanoidGen, we selected three tasks from §5.1: _blocks stack easy_ , _blocks stack hard_ , _pyramid stack_ , and added a single-arm task, _block stack single_ . In contrast to §5.1, we increased the task complexity to rigorously evaluate the performance of LLM in scenarios with insufficiently annotated objects and long-horizon tasks. Specifically, we introduced two key challenges: (i) removing all operation annotations for cubes, forcing the LLM to infer relevant constraints solely from cube poses; (ii) simplifying task descriptions to provide minimal guidance. For example, in the _blocks stack hard_ task, the LLM is instructed only to stack cubes into a pile without considering the order of operations and target positions, allowing highly uncertain execution. Building upon this setup, we compared the reasoning success rates and token consumption per execution between MCTS and non-MCTS strategies using DeepSeek-R1 [55] across these four tasks. Additionally, we analyzed the diversity of generated plans to assess the exploratory capabilities of each approach. 

8 

|Method|Success rate (%)|Token consumption (K)|
|---|---|---|
|**Block Stack Single**|||
|Non-MCTS|63.3 _±_6.24|15.3 _±_1.90|
|MCTSN=2|98.3 _±_2.36|19.3 _±_7.04|
|**Blocks Stack Easy**|||
|Non-MCTS|46.7 _±_2.36|14.8 _±_1.64|
|MCTSN=2|83.3 _±_5.56|21.6 _±_7.78|
|MCTSN=3|95.0 _±_4.08|22.8 _±_9.13|
|**Blocks Stack Hard**|||
|Non-MCTS|18.3 _±_6.24|16.0 _±_0.92|
|MCTSN=8|78.3 _±_2.36|69.9 _±_39.24|
|MCTSN=12|98.3 _±_2.36|78.3 _±_51.75|
|**Pyramid Stack**|||
|Non-MCTS|13.3 _±_6.24|16.2 _±_1.29|
|MCTSN=8|76.7 _±_4.71|80.0 _±_31.72|
|MCTSN=12|90.0 _±_4.08|89.6 _±_44.61|



Table 1: The evaluation results of applying different numbers of max MCTS exploration steps _N_ and non-MCTS in four tasks. 



<!-- Start of picture text -->
14<br>Method & Task<br>12 blocks stack hard blocks stack hard (non-MCTS)(MCTS)<br>pyramid stack (MCTS)<br>10 pyramid stack (non-MCTS)<br>8<br>6<br>4<br>2<br>0<br>0 2 4 6 8 10 12 14 16 18 20<br>the count of successful plans<br>the count of distinct successful plans<br><!-- End of picture text -->

Figure 6: The variation of the count of distinct successful plans for MCTS and non-MCTS with the count of successful plans. 

**Experimental Results.** As shown in Tab. 1, MCTS can significantly improve the reasoning ability of LLM with minimal additional token consumption. This demonstrates that during the reasoning process of MCTS, LLM can effectively utilize the information of tree nodes to infer the correct task steps. For example, in the ‘pyramid stack’ task, LLMs are prone to reasoning errors such as unreasonable selections of stacking positions and collisions of two arms in the stacking area. When exploring nodes where such errors occur, MCTS enables LLMs to analyze the causes of errors based on past experiences, correct the execution methods, and continue execution. Further, the results demonstrate that the exploration strategy of MCTS is highly cost-effective, as evidenced across all tasks. For instance, in the _block stack single_ task, a 26% increase in token consumption led to a 55% improvement in the reasoning success rate. Specifically, the average token consumption per successful execution method decreased from 24.17K to 19.63K, reducing approximately 20% token consumption. In addition, MCTS can enhance the diversity of generated plans. Fig. 6 illustrates the cumulative number of different plans generated by MCTS and non-MCTS methods as a function of successful planning counts. Among the 20 success solutions, MCTS obtains _≥_ 12 distinct plans, whereas non-MCTS only generated _≤_ 5 distinct plans. This validates that MCTS can explore diverse outcomes by correcting erroneous execution strategies inherent in the direct reasoning approach. 

### **5.3 Validity Evaluation of Collected Data** 

To validate the effectiveness of the collected dataset, we trained policies on the data and evaluated their performance, focusing on how success rates vary with different dataset sizes. We collected 100 data samples for each task using our method. Each sample includes RGB and depth images captured from six cameras, the joint states, and the action ground truth of the robot. 

**Policies used for evaluation.** The _Diffusion Policy_ (DP) [43] models vision-based robotic control as a conditional denoising process, handling multimodal action distributions and high-dimensional action spaces effectively. The _3D Diffusion Policy_ (DP3) [44] enhances DP by incorporating point cloud data, improving performance in dexterous manipulation tasks, and demonstrating strong generalization. We evaluated DP3 and DP on 14 tasks using RGB images or point clouds as input, measuring success rates across different episodes. 

**Experimental Results.** As shown in Tab. 2, for some relatively easy tasks, DP3 demonstrates few-shot learning capability. For example, in the _cup pour easy_ task, DP3 achieves a 67% success rate using only 20 demonstrations generated by our framework. This validates the diversity of our scene generation and the high quality of our collected data. Overall, DP performs worse than DP3; however, its performance improves with increased data. In the _open box hard_ task, the success rate rises from 11.1% with 20 demonstrations to 100% with 100 demonstrations, even surpassing DP3. This confirms that our data scaling approach leads to continuous policy improvement. Notably, some task policies exhibit non-stationary characteristics. Despite achieving a high success rate with 20 demonstrations, their actions exhibit instability and risk, as denoted by the ‘*’ in the table. 

For challenging tasks, such as the long-horizon task _blocks stack easy_ , both DP and DP3 exhibit a noticeable performance decline, particularly when the data is limited. The suboptimal performance of DP may be attributed to the inherent limitations of RGB information, whereas DP3, which 

9 

|**Num of Demonstrations**|**20**|**50**|**100**||**20**|**50**|**100**|
|---|---|---|---|---|---|---|---|
|**Blocks Stack Easy**||||**Close Drawer**||||
|DP3|0.0_±_0.0|0.0_±_0.0|22.8_±_16.5|DP3|83.3_±_17.6|94.4_±_7.9|92.6_±_8.3|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|95.6_±_3.7|100.0_±_0.0|100.0_±_0.0|
|**Cup Pour Easy**||||**Dual Bottles Pick Easy**||||
|DP3|67.8_±_10.8|75.6_±_9.6|72.2_±_7.9|DP3|75.9_±_17.8|96.3_±_6.9|93.9_±_7.6|
|DP|0.0_±_0.0|2.2_±_6.3|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|**Dual Bottles Pick Hard**||||**Empty Cup Place**||||
|DP3|88.9_±_13.6|90.7_±_11.4|94.4_±_7.9|DP3|25.0_±_8.2|18.3_±_4.7|33.3_±_7.1|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|6.7_±_13.3|
|**Open Box Easy**||||**Open Box Hard**||||
|DP3|85.6_±_8.0|95.6_±_4.4|95.0_±_4.1|DP3|95.6_±_5.5|96.1_±_4.6|98.3_±_3.3|
|DP|93.3_±_13.3|100.0_±_0.0|100.0_±_0.0|DP|11.1_±_19.1|93.3_±_9.4|100.0_±_0.0|
|**Open Drawer**||||**Open Laptop Hard**||||
|DP3|58.3_±_8.3|76.0_±_13.1|84.4_±_11.3|DP3|100.0_±_0.0|100.0_±_0.0|100.0_±_0.0|
|DP|17.8_±_22.0|13.3_±_18.9|48.9_±_31.4|DP|15.6_±_22.7|11.1_±_9.9|35.6_±_32.4|
|**Close Box Hard**||||**Close Laptop Easy**||||
|DP3|88.9_±_17.6|96.3_±_6.9|96.3_±_6.9|DP3|100.0_±_0.0|100.0_±_0.0|100.0_±_0.0|
|DP|*82.2_±_22.0|*51.1_±_19.1|31.1_±_28.5|DP|37.8_±_23.9|40.0_±_23.1|48.9_±_25.1|
|**Handover and Storage**||||**Blocks Stack Hard**||||
|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|



Table 2: We trained DP and DP3 using 100, 50, and 20 trajectories generated by our method, and evaluated the success rates across 14 tasks with 3 random seeds. 

requires modeling actions of high DoFs and managing complex long-horizon tasks, necessitates a larger amount of data. Our efficient data collection method enables rapid scaling of data, making it particularly effective for addressing the challenges faced by both DP and DP3 in handling complex long-horizon tasks with limited data. More evaluation details are given in Appendix B. 

## **6 Conclusion** 

This paper introduces HumanoidGen, a framework utilizing automatically generated scenes and synthetic data to facilitate the learning and execution of bimanual dexterous manipulation tasks. Spatial annotations for key points and axes of both assets and hands are given, providing sufficient information for scene generation and planning. The LLM planner generates task decomposition and relational action constraints with collision avoidance applied, enabling the following trajectory optimization of tasks. We also employ collision avoidance and MCTS-based reasoning to improve planning efficiency in complex or long-horizon tasks. We construct a benchmark that contains diverse bimanual dexterous tasks for evaluation. The experiments show that our framework has superior capabilities in demonstration script generation and execution, especially for tasks with long task horizons and complex collision scenarios. MCTS improves LLMs’ reasoning ability with insufficient annotations. The training of diffusion policies verifies the quality and scaling capacity of our method. 

## **Acknowledgments** 

This work is supported by the National Natural Science Foundation of China (Grant Nos. 62427819 and 62306242), the Young Elite Scientists Sponsorship Program by CAST (Grant No. 2024QNRC001), the Yangfan Project of the Shanghai (Grant No.23YF11462200), and the Science and Technology Commission of Shanghai Municipality (No. 24511103100). 

## **References** 

- [1] Shan An, Ziyu Meng, Chao Tang, Yuning Zhou, Tengyu Liu, Fangqiang Ding, Shufang Zhang, Yao Mu, Ran Song, Wei Zhang, et al. Dexterous manipulation through imitation learning: A survey. _arXiv preprint arXiv:2504.03515_ , 2025. 

> [2] Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Fan, Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang, et al. Gr00t n1: An open foundation model for generalist humanoid robots. _arXiv preprint arXiv:2503.14734_ , 2025. 

10 

- [3] Zhaoyuan Gu, Junheng Li, Wenlan Shen, Wenhao Yu, Zhaoming Xie, Stephen McCrory, Xianyi Cheng, Abdulaziz Shamsah, Robert Griffin, C Karen Liu, et al. Humanoid locomotion and manipulation: Current progress and challenges in control, planning, and learning. _arXiv preprint arXiv:2501.02116_ , 2025. 

- [4] Yanjie Ze, Zixuan Chen, Wenhao Wang, Tianyi Chen, Xialin He, Ying Yuan, Xue Bin Peng, and Jiajun Wu. Generalizable humanoid manipulation with improved 3d diffusion policies. _arXiv preprint arXiv:2410.10803_ , 2024. 

- [5] Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, and Xiaolong Wang. Open-television: Teleoperation with immersive active visual feedback. In _8th Annual Conference on Robot Learning_ , 2024. 

- [6] Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Shiqi Yang, Ruihan Yang, Xiaojuan Qi, and Xiaolong Wang. Bunny-visionpro: Real-time bimanual dexterous teleoperation for imitation learning. _arXiv preprint arXiv:2407.03162_ , 2024. 

- [7] Shiqi Yang, Minghuan Liu, Yuzhe Qin, Runyu Ding, Jialong Li, Xuxin Cheng, Ruihan Yang, Sha Yi, and Xiaolong Wang. Ace: A cross-platform and visual-exoskeletons system for low-cost dexterous teleoperation. In _8th Annual Conference on Robot Learning_ , 2024. 

- [8] Qingwei Ben, Feiyu Jia, Jia Zeng, Junting Dong, Dahua Lin, and Jiangmiao Pang. Homie: Humanoid loco-manipulation with isomorphic exoskeleton cockpit. In _Robotics: Science and Systems_ , 2025. 

- [9] Tony Z. Zhao, Vikash Kumar, Sergey Levine, and Chelsea Finn. Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware. In _Proceedings of Robotics: Science and Systems_ , 2023. 

- [10] Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, et al. Open x-embodiment: Robotic learning datasets and rt-x models: Open x-embodiment collaboration 0. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 6892–6903. IEEE, 2024. 

- [11] Kun Wu, Chengkai Hou, Jiaming Liu, Zhengping Che, Xiaozhu Ju, Zhuqin Yang, Meng Li, Yinuo Zhao, Zhiyuan Xu, Guang Yang, et al. Robomind: Benchmark on multi-embodiment intelligence normative data for robot manipulation. _arXiv preprint arXiv:2412.13877_ , 2024. 

- [12] Hao-Shu Fang, Hongjie Fang, Zhenyu Tang, Jirong Liu, Chenxi Wang, Junbo Wang, Haoyi Zhu, and Cewu Lu. Rh20t: A comprehensive robotic dataset for learning diverse skills in one-shot. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 653–660. IEEE, 2024. 

- [13] Homer Rich Walke, Kevin Black, Tony Z Zhao, Quan Vuong, Chongyi Zheng, Philippe Hansen-Estruch, Andre Wang He, Vivek Myers, Moo Jin Kim, Max Du, et al. Bridgedata v2: A dataset for robot learning at scale. In _Conference on Robot Learning_ , pages 1723–1736. PMLR, 2023. 

- [14] Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao Zhu, Fangchen Liu, Minghua Liu, Hanxiao Jiang, Yifu Yuan, He Wang, Li Yi, Angel X. Chang, Leonidas J. Guibas, and Hao Su. SAPIEN: A simulated part-based interactive environment. In _The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , June 2020. 

- [15] Yuanpei Chen, Tianhao Wu, Shengjie Wang, Xidong Feng, Jiechuan Jiang, Zongqing Lu, Stephen McAleer, Hao Dong, Song-Chun Zhu, and Yaodong Yang. Towards human-level bimanual dexterous manipulation with reinforcement learning. _Advances in Neural Information Processing Systems_ , 35:5150–5163, 2022. 

- [16] Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, Mustafa Haiderbhai, Samuel Holt, Jing Yuan Luo, Arthur Allshire, Erik Frey, Koushil Sreenath, Lueder A Kahrs, et al. Mujoco playground. _arXiv preprint arXiv:2502.08844_ , 2025. 

- [17] Zipeng Fu, Tony Z Zhao, and Chelsea Finn. Mobile aloha: Learning bimanual mobile manipulation with low-cost whole-body teleoperation. _arXiv preprint arXiv:2401.02117_ , 2024. 

- [18] Markus Grotz, Mohit Shridhar, Yu-Wei Chao, Tamim Asfour, and Dieter Fox. Peract2: Benchmarking and learning for robotic bimanual manipulation tasks. In _CoRL 2024 Workshop on Whole-body Control and Bimanual Manipulation: Applications in Humanoids and Beyond_ , 2024. 

- [19] Yao Mu, Tianxing Chen, Shijia Peng, Zanxin Chen, Zeyu Gao, Yude Zou, Lunkai Lin, Zhiqiang Xie, and Ping Luo. Robotwin: Dual-arm robot benchmark with generative digital twins (early version). In _IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , 2025. 

- [20] Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, and Pieter Abbeel. Humanoidbench: Simulated humanoid benchmark for whole-body locomotion and manipulation. _arXiv preprint arXiv:2403.10506_ , 2024. 

11 

- [21] Nikita Chernyadev, Nicholas Backshall, Xiao Ma, Yunfan Lu, Younggyo Seo, and Stephen James. Bigym: A demo-driven mobile bi-manual manipulation benchmark. In _8th Annual Conference on Robot Learning_ , 2024. 

- [22] Yufei Wang, Zhou Xian, Feng Chen, Tsun-Hsuan Wang, Yian Wang, Katerina Fragkiadaki, Zackory Erickson, David Held, and Chuang Gan. Robogen: Towards unleashing infinite data for automated robot learning via generative simulation. In _International Conference on Machine Learning_ , 2024. 

- [23] Lirui Wang, Yiyang Ling, Zhecheng Yuan, Mohit Shridhar, Chen Bao, Yuzhe Qin, Bailin Wang, Huazhe Xu, and Xiaolong Wang. Gensim: Generating robotic simulation tasks via large language models. In _International Conference on Learning Representations_ , 2024. 

- [24] Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, and Yuke Zhu. Robocasa: Large-scale simulation of everyday tasks for generalist robots. In _RSS 2024 Workshop: Data Generation for Robotics_ , 2024. 

- [25] Huajian Xin, ZZ Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, et al. Deepseek-prover-v1. 5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. _arXiv preprint arXiv:2408.08152_ , 2024. 

- [26] ZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. _arXiv preprint arXiv:2504.21801_ , 2025. 

- [27] Pu Hua, Minghuan Liu, Annabella Macaluso, Yunfeng Lin, Weinan Zhang, Huazhe Xu, and Lirui Wang. Gensim2: Scaling robot data generation with multi-modal and reasoning LLMs. In _8th Annual Conference on Robot Learning_ , 2024. 

- [28] Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, brian ichter, Pete Florence, and Andy Zeng. Code as policies: Language model programs for embodied control. In _Workshop on Language and Robotics at CoRL 2022_ , 2022. 

- [29] Yao Mu, Junting Chen, Qinglong Zhang, Shoufa Chen, Qiaojun Yu, Chongjian GE, Runjian Chen, Zhixuan Liang, Mengkang Hu, Chaofan Tao, et al. Robocodex: multimodal code generation for robotic behavior synthesis. In _Proceedings of the 41st International Conference on Machine Learning_ , pages 36434–36454, 2024. 

- [30] Wenke Xia, Dong Wang, Xincheng Pang, Zhigang Wang, Bin Zhao, Di Hu, and Xuelong Li. Kinematicaware prompting for generalizable articulated object manipulation with llms. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 2073–2080. IEEE, 2024. 

- [31] Xi Wang, Tianxing Chen, Qiaojun Yu, Tianling Xu, Zanxin Chen, Yiting Fu, Ziqi He, Cewu Lu, Yao Mu, and Ping Luo. Articulated object manipulation using online axis estimation with sam2-based tracking. _arXiv preprint arXiv:2409.16287_ , 2024. 

- [32] Wenlong Huang, Chen Wang, Yunzhu Li, Ruohan Zhang, and Li Fei-Fei. Rekep: Spatio-temporal reasoning of relational keypoint constraints for robotic manipulation. In _8th Annual Conference on Robot Learning_ , 2024. 

- [33] Mingjie Pan, Jiyao Zhang, Tianshu Wu, Yinghao Zhao, Wenlong Gao, and Hao Dong. Omnimanip: Towards general robotic manipulation via object-centric interaction primitives as spatial constraints. _arXiv preprint arXiv:2501.03841_ , 2025. 

- [34] Rudolf Lioutikov, Oliver Kroemer, Guilherme Maeda, and Jan Peters. Learning manipulation by sequencing motor primitives with a two-armed robot. In _Intelligent Autonomous Systems 13: Proceedings of the 13th International Conference IAS-13_ , pages 1601–1611. Springer, 2016. 

- [35] Simon Stepputtis, Maryam Bandari, Stefan Schaal, and Heni Ben Amor. A system for imitation learning of contact-rich bimanual manipulation policies. In _2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 11810–11817. IEEE, 2022. 

- [36] Fan Xie, Alexander Chowdhury, M De Paolis Kaluza, Linfeng Zhao, Lawson Wong, and Rose Yu. Deep imitation learning for bimanual robotic manipulation. _Advances in neural information processing systems_ , 33:2327–2337, 2020. 

- [37] Giovanni Franzese, Leandro de Souza Rosa, Tim Verburg, Luka Peternel, and Jens Kober. Interactive imitation learning of bimanual movement primitives. _IEEE/ASME Transactions on Mechatronics_ , 2023. 

12 

- [38] Jianfeng Gao, Xiaoshu Jin, Franziska Krebs, Noémie Jaquier, and Tamim Asfour. Bi-kvil: Keypoints-based visual imitation learning of bimanual manipulation tasks. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 16850–16857. IEEE, 2024. 

- [39] Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. Taco: Benchmarking generalizable bimanual tool-action-object understanding. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 21740–21751, 2024. 

- [40] Jianfeng Gao, Xiaoshu Jin, Franziska Krebs, Noémie Jaquier, and Tamim Asfour. Bi-kvil: Keypoints-based visual imitation learning of bimanual manipulation tasks. In _2024 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 16850–16857. IEEE, 2024. 

- [41] Giovanni Franzese, Leandro de Souza Rosa, Tim Verburg, Luka Peternel, and Jens Kober. Interactive imitation learning of bimanual movement primitives. _IEEE/ASME Transactions on Mechatronics_ , 2023. 

- [42] Andrew Choong-Won Lee, Ian Chuang, Ling-Yuan Chen, and Iman Soltani. InterACT: Inter-dependency aware action chunking with hierarchical attention transformers for bimanual manipulation. In _8th Annual Conference on Robot Learning_ , 2024. 

- [43] Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion. _The International Journal of Robotics Research_ , page 02783649241273668, 2023. 

- [44] Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu, Muhan Wang, and Huazhe Xu. 3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations. In _ICRA 2024 Workshop on 3D Visual Representations for Robot Manipulation_ , 2024. 

- [45] Anthony Brohan, Noah Brown, Justice Carbajal, et al. Rt-1: Robotics transformer for real-world control at scale. In _Robotics: Science and Systems_ , 2023. 

- [46] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, et al. Droid: A large-scale in-the-wild robot manipulation dataset. In _Robotics: Science and Systems_ , 2024. 

- [47] Qingwen Bu, Jisong Cai, Li Chen, Xiuqi Cui, Yan Ding, Siyuan Feng, Shenyuan Gao, Xindong He, Xu Huang, Shu Jiang, et al. Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. _arXiv preprint arXiv:2503.06669_ , 2025. 

- [48] Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai Tan, Huayu Chen, Zhengyi Wang, Ke Xu, Hang Su, and Jun Zhu. Rdt-1b: a diffusion foundation model for bimanual manipulation. _arXiv preprint arXiv:2410.07864_ , 2024. 

- [49] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, and Minjoon Seo. Latent action pretraining from videos. In _The Thirteenth International Conference on Learning Representations_ , 2025. 

- [50] Ajay Mandlekar, Soroush Nasiriany, Bowen Wen, Iretiayo Akinola, Yashraj Narang, Linxi Fan, Yuke Zhu, and Dieter Fox. Mimicgen: A data generation system for scalable robot learning using human demonstrations. In _Conference on Robot Learning_ , pages 1820–1864. PMLR, 2023. 

- [51] Zhenyu Jiang, Yuqi Xie, Kevin Lin, Zhenjia Xu, Weikang Wan, Ajay Mandlekar, Linxi Fan, and Yuke Zhu. Dexmimicgen: Automated data generation for bimanual dexterous manipulation via imitation learning. In _2025 IEEE International Conference on Robotics and Automation (ICRA)_ , 2025. 

- [52] Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Hinrichsen, Xiaodi Yuan, Chen Bao, Xinsong Lin, Yulin Liu, Tse-kai Chan, et al. Maniskill3: Gpu parallelized robotics simulation and rendering for generalizable embodied ai. _arXiv preprint arXiv:2410.00425_ , 2024. 

- [53] Xuanlin Li, Kyle Hsu, Jiayuan Gu, Oier Mees, Karl Pertsch, Homer Rich Walke, Chuyuan Fu, Ishikaa Lunawat, Isabel Sieh, Sean Kirmani, Sergey Levine, Jiajun Wu, Chelsea Finn, Hao Su, Quan Vuong, and Ted Xiao. Evaluating real-world robot manipulation policies in simulation. In _8th Annual Conference on Robot Learning_ , 2024. 

- [54] Haoran Lu, Ruihai Wu, Yitong Li, Sijie Li, Ziyu Zhu, Chuanruo Ning, Yan Shen, Longzan Luo, Yuanpei Chen, and Hao Dong. Garmentlab: A unified simulation and benchmark for garment manipulation. In _The Thirty-eighth Annual Conference on Neural Information Processing Systems_ , 2024. 

13 

- [55] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. _arXiv preprint arXiv:2501.12948_ , 2025. 

- [56] Bowen Wen, Wei Yang, Jan Kautz, and Stan Birchfield. Foundationpose: Unified 6d pose estimation and tracking of novel objects. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 17868–17879, 2024. 

- [57] Zhengrong Xue, Shuying Deng, Zhenyang Chen, Yixuan Wang, Zhecheng Yuan, and Huazhe Xu. Demogen: Synthetic demonstration generation for data-efficient visuomotor policy learning. _arXiv preprint arXiv:2502.16932_ , 2025. 

- [58] Yiran Qin, Li Kang, Xiufeng Song, Zhenfei Yin, Xiaohong Liu, Xihui Liu, Ruimao Zhang, and Lei Bai. Robofactory: Exploring embodied agent collaboration with compositional constraints. _arXiv preprint arXiv:2503.16408_ , 2025. 

- [59] Yuheng Ji, Huajie Tan, Jiayu Shi, Xiaoshuai Hao, Yuan Zhang, Hengyuan Zhang, Pengwei Wang, Mengdi Zhao, Yao Mu, Pengju An, et al. Robobrain: A unified brain model for robotic manipulation from abstract to concrete. In _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pages 1724–1734, 2025. 

- [60] Jingshun Huang, Haitao Lin, Tianyu Wang, Yanwei Fu, Xiangyang Xue, and Yi Zhu. Cap-net: A unified network for 6d pose and size estimation of categorical articulated parts from a single rgb-d image. In _Proceedings of the Computer Vision and Pattern Recognition Conference_ , pages 11654–11664, 2025. 

- [61] Jianglong Ye, Keyi Wang, Chengjing Yuan, Ruihan Yang, Yiquan Li, Jiyue Zhu, Yuzhe Qin, Xueyan Zou, and Xiaolong Wang. Dex1b: Learning with 1b demonstrations for dexterous manipulation. _arXiv preprint arXiv:2506.17198_ , 2025. 

14 

## **Appendix Table of HumanoidGen** 

|**A Imp**|**lementation Details of HumanoidGen**|**15**|
|---|---|---|
|A.1|Automatic Asset Annotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>15|
|A.2|Constraint Solver<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
|A.3|Scene Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|A.4|MCTS-Based LLM Reasoning<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|**B**<br>**Deta**|**ils of HGen-Bench**|**18**|
|**C Exp**|**erimental Details and Additional Experiments**|**20**|
|C.1|Real-World Experiments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>20|
|C.2|Automatic Asset Annotation Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>21|
|C.3|Additional Challenging Dexterous Manipulation Tasks . . . . . . . . . . . . . . . . . .|. . .<br>22|
|C.4|Resource and Efficiency Analysis of HumanoidGen<br>. . . . . . . . . . . . . . . . . . .|. . .<br>23|
|C.5|Comparison with Existing Generation Frameworks . . . . . . . . . . . . . . . . . . . .|. . .<br>23|
|C.6|Comparison Across Different Large Models<br>. . . . . . . . . . . . . . . . . . . . . . .|. . .<br>24|
|C.7|Task Descriptions in Data Generation Experiment<br>. . . . . . . . . . . . . . . . . . . .|. . .<br>24|
|C.8|Task Descriptions in MCTS Experiment. . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>24|
|**D Mor**|**e Discussion on Limitations and Future Work**|**24**|
|**E**<br>**Pro**|**mpts and Generation Samples**|**26**|
|E.1|Prompt Template for Scene Generation . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>26|
|E.2|Sample Scene Code for Blocks Stack Hard Generated by HumanoidGen . . . . . . . . .|. . .<br>27|
|E.3|Prompt Template for Demonstration Script Generation . . . . . . . . . . . . . . . . . .|. . .<br>28|
|E.4|Sample Demonstration Code for Open Drawer Generated by HumanoidGen . . . . . . .|. . .<br>31|
|E.5|Prompt Template for MCTS-integrated Demonstration Script Generation<br>. . . . . . . .|. . .<br>32|
|E.6|Sample Demonstration Code for Block Stack Hard Generated by Applying MCTS<br>. . .|. . .<br>39|
|**F**<br>**Bro**|**ader Impacts**|**41**|



## **A Implementation Details of HumanoidGen** 

### **A.1 Automatic Asset Annotation** 



<!-- Start of picture text -->
Function  Grasp  Pinch  Press  Attach  Approach Parallel<br>Point Point Point Point Axis Axis Axis<br><!-- End of picture text -->

Figure 7: The illustration of automatic asset annotation. 

In this section, we detail how to simplify the annotation process using Stable Diffusion to automatically annotate similar assets and avoid repetitive annotation work. As shown in Fig. 7, assets of the same category have similar annotation information (points and axes), enabling direct annotation migrations across them. Specifically, we utilize the Stable Diffusion encoder for feature point matching. First, from the same viewing angle where key 

15 

points are not occluded, we obtain the image _I_<sup>_a_</sup> of the annotated asset and the image _I_<sup>non</sup> of the unannotated asset. For the annotated asset, there are _n_ key points _P_<sup>_a_</sup> = _{p_ 1<sup>_a, pa_</sup> 2<sup>_, ..., pa_</sup> _n_<sup>_}_,andourgoalistoobtainthe</sup> corresponding key points _P_<sup>non</sup> in _I_<sup>non</sup> . Following the method in [19], we extract the diffusion features of both _I_<sup>_a_</sup> and _I_<sup>non</sup> . For each _p_<sup>_a_</sup> _i_<sup>_∈P a_, which corresponds to a single pixel in</sup><sup>_Ia_, we analyze the similarity of the</sup> extracted diffusion features to obtain the corresponding pixel in _I_<sup>non</sup> . Since the images are captured without occlusion, we can obtain _pi_<sup>non</sup> _∈ P_<sup>non</sup> in sequence by back-projecting the pixels in _I_<sup>non</sup> into the 3D asset space. For axes annotation, starting from the obtained key points, the same axis directions as the original asset are extended to obtain the key axes of the unannotated asset. By applying the approach above, the key points and key axes of the new asset are automatically annotated, effectively reducing the necessary effort by manual annotation. 

### **A.2 Constraint Solver** 

As explained in §2.2, the LLM planner decomposes the long-horizon task into a sequence composed of hand atomic operations and arm movements. The arm movement solving problem is formulated as two constrained optimization problems, with the constraints _C_<sup>goal</sup> and _C_<sup>path</sup> both inferred by the LLM. We consider a movement process to consist of _T_ time steps. Here, _t ∈{_ 0 _,_ 1 _, ..., T }_ represents each time step, with _t_ = 0 and _t_ = _T_ denoting the initial and the end time step, respectively. At each _t_ , the arm joint angle is _θt_ , and the pose of the end effector is **e** _t ∈ SE_ (3). 

The motion solving process involves two steps. The first step is to (i) obtain the target end-effector pose **e** _T_ and the target arm angle _θT_ . This can be formulated as a nonlinear optimization problem as 



where _w_ denotes the weight to balance various optimization terms. _c_ ( _u_ act _, u_ all) represents a relational constraint between _F_ act and _F_ all, defined in §2.2. Here, _u ∈{p, v, l_ ( _p, v_ ) _}_ is used as a basic component for formulating the constraints, with _p_ , _v_ , and _l_ ( _p, v_ ) denoting points, vectors, and lines, respectively. Thus, _c_ ( _u_ act _, u_ all) can be further expressed as 



where _l_ ( _p, v_ ) is the line formed by the point _p_ and the axis _v_ , _d_ ( _·_ ) is the function to calculate the distance between points or between a point and a line, and _a_ ( _·_ ) is the function to calculate the angle difference between two axes. _w_ reg _∥θT − θ_ nominal _∥_ represents the regularization term, which biases the optimization toward the robot’s safe configuration. The nominal angles _θ_ nominal can generally be predefined using historical data or expert knowledge, such as _θ_ 0 and _θ_ default. The pose **e** _T_ of the end-effector must satisfy the constraints derived from the forward kinematics solution _f_ FK( _θT_ ). The interval [ _c_ lower _, c_ upper] represents the upper and lower bounds of the relational constraints. Finally, Θcollision_free denotes the set of _θ_ values that will not result in collisions. We employed the SNOPT solver from the pydrake library to solve this optimization problem. 

The second step is to (ii) calculate **e** _t_ and _θt_ , when 0 _< t < T_ . To address this problem, we utilize the constrained motion planner from the mplib library to minimize the cost function Cost( _θt_ ) while guaranteeing the satisfaction of the constraints during the movement process. The optimization problem can be formulated as 



where Cost( _θt_ ) typically incorporates objectives related to motion smoothness, energy efficiency, and trajectory optimality. 

16 



<!-- Start of picture text -->
Original Scene (tabletop-level) Scaled Scene (room-level)<br>𝑂<br>𝑂 ′<br>𝑂 ′<br><!-- End of picture text -->

Figure 8: Schematic diagram illustrating the scene scaling of the _handover and storage_ task, extending from a desktop-level scenario on the left to a room-level scenario on the right, aimed at enhancing scene diversity in the dataset. 

### **A.3 Scene Scaling** 

To scale tasks from tabletop-level scenes to room-level scenes, as introduced in §2.3, coordinate transformations are applied to align the scene configurations. Specifically, in the original scene, a point is selected on the table edge near the robot as the origin _o_ to construct a Cartesian coordinate system _O_ –xyz. The x-axis of _O_ points in the direction the robot faces toward the table, the y-axis extends from _o_ along the table’s edge toward the robot’s left-hand direction, and the z-axis extends vertically upward from _o_ . Correspondingly, in the new scene, an edge point in an open desktop area is selected as the origin _o_<sup>_′_</sup> to construct another Cartesian coordinate system _O_<sup>_′_</sup> –xyz, with x, y, and z directions consistent with those in _O_ –xyz. Thus, for a point _p_ , vector _v_ , and pose _P ∈ SE_ (3) in the world coordinate system of the original scene, and their counterparts _p_<sup>_′_</sup> , _v_<sup>_′_</sup> , and _P_<sup>_′_</sup> _∈ SE_ (3) in world coordinate system of the scaled scene, the following relationship holds: 



Based on the coordinate transformation defined in Eq. (4), the spatial relationships of objects, robots, key points, and axes in the original system _O_ can be directly mapped to the target system _O_<sup>_′_</sup> . This allows reconstructed poses (e.g., object configurations, relational action constraints) to inherit geometric consistency from the source scene, enabling seamless task execution in the scaled environment. By leveraging this lightweight approach, our dataset diversity is enhanced without requiring additional annotations or complex geometric reasoning. 

### **A.4 MCTS-Based LLM Reasoning** 

**Selection.** In each iterative loop, the step begins with a selection to find the node to expand. In the selection step, it starts from the root node and explores downwards. When a node is explored, the algorithm decides whether to continue exploring one of its children or to end the exploration and select the node for expansion. To define the action to expand from the explored node, we introduce a special branch _S_<sup>_′_</sup> = _∅_ as proposed in [25]. Here, _S_<sup>_′_</sup> is the branch defined in §2.3, which consists of multiple operation steps _S_ with consistent intents. The choice of continuing exploration and expansion is decided by 



where we use _Q_ DUCB as the value estimation method to balance the values of exploration and exploitation, as referenced in [25]. _Q_ DUCB uses a discount _γ ∈_ (0 _,_ 1) to smoothly drop those outdated feedback records and give greater weights to the feedback from the latest backpropagation during value estimation. The process can be described as 









17 

where _τt_ = _{_ ( _n_ root _, n_<sup>(1)</sup> ) _,_ ( _n_<sup>(1)</sup> _, n_<sup>(2)</sup> ) _, ...,_ ( _n_<sup>(</sup><sup>_|τ|−_1)</sup> = _nt,_ ∅) _}_ denotes the selection trajectory of t-th iteration that ends with _nt_ as the expanding node. Γ( _n, S_<sup>_′_</sup> ) = _{τ |_ ( _n, S_<sup>_′_</sup> ) _∈ τ }_ denotes the set of _τ_ that contains ( _n, S_<sup>_′_</sup> ). _R_ ( _τ_ ) represents the value of the trajectory _τ_ , which is determined in the backpropagation stage. _N_ ( _n, S_<sup>_′_</sup> ) denotes the number of trajectories _τ_ that contain ( _n, S_<sup>_′_</sup> ). _W_ ( _n, S_<sup>_′_</sup> ) denotes the total value of trajectories _τ_ that contain ( _n, S_<sup>_′_</sup> ). _Nγ_ ( _n, S_<sup>_′_</sup> ) and _Wγ_ ( _n, S_<sup>_′_</sup> ) are both results decayed by _γ_ . 

**Expansion.** Using the information stored in the exploration node, such as executed code, non-executable code, and the node’s runtime scene information, a prompt is constructed and fed into the reasoning LLM. Then the LLM infers new executable code. Following the STCR mechanism proposed in §2.3, a subtree is built with the selected expansion node as the root. When expanding, if the next execution branch _S_ new<sup>_′_under the current</sup> expansion node _n_ now already exists, i.e., _S_ new<sup>_′∈_Children(</sup><sup>_n_</sup> now<sup>),anewnodewillnotbegenerated,andthe</sup> expansion will continue along the existing branch. If the task is successfully completed, the MCTS process ends, and the executed code is concatenated to the generated code to form the final successfully executed code. If the task remains incomplete, the iterative loop continues. 

**Backpropagation.** Backpropagation is the final step of the iteration. It aims to update the reward _R_ ( _τ_ ), where _τ_ is the selected trajectory in this iteration. Since iteration ends once a successful task plan is discovered, the extrinsic reward contains _R_ extrinsic = 0 during the iteration process and cannot be used as a reward. Therefore, we propose an intrinsic exploration value _R_ intrinsic based on ‘valuable moment’, which refers to the occurrence of a valuable event, such as ‘successfully grasp a cup’, ‘pinch a cube’, ‘the object does not fall off when the hand is opened’, etc. If the generated code contains at least one ‘valuable moment’ during execution, then we set _R_ intrinsic = 1 for backpropagation to incentivize the expansion of the LLM. 

## **B Details of HGen-Bench** 

**Benchmark Task Design.** Our benchmark builds on ManiSkill3 [52] physics engine. In the simulation, the maximum control frequency can be set to 100 Hz, and the maximum camera capture frequency is 100 Hz. Our tasks span various scenarios. The details are given as follows. (i) _Atom operations_ . To fully leverage the dexterity of the hands, we design interaction modes such as pinching and grasping. For example, stacking small blocks requires pinching them with the index finger and thumb, whereas picking up a bottle requires a firm grasp. (ii) _Task difficulties_ . To reflect varying levels of task difficulty, we define difficulty settings and name the tasks with ‘easy’ and ‘hard’ to distinguish. For instance, in the _dual bottles pick_ task, the ’easy’ setting involves picking upright bottles, while the ’hard’ setting involves picking fallen ones. (iii) _Collaboration modes_ . We also design bimanual coordination tasks that exploit the capabilities of dual dexterous hands. For example, the _block handover_ task involves picking up a block, handing it over from hand to hand, and placing it. (iv) _Long-horizon and geometric reasoning._ We design a set of challenging tasks to evaluate these capabilities. For example, the long-horizon task _handover and storage_ involves a sequence of five steps: the right hand grasps a block and positions it for transfer, the left hand opens a drawer, then takes over the block, and finally places it into the drawer. We also design tasks requiring geometric reasoning. In _blocks stack hard_ , the robot must stack three blocks vertically. In _pyramid stack_ , two blocks must be placed on the first layer, with a third block stacked on top to form the second layer. To introduce variability, we randomize the initial position, pose, and joint angles of articulated objects within a certain range. This allows us to collect more diverse data and test the generalization ability of learned policies. 

**Policy Training Examples.** We provide example code for deploying and evaluating different types of policies. In our experiments, we present the training and evaluation results of these policies. The dataset we collected includes first-person RGB images captured by an Intel RealSense D435 camera, aligned depth maps, and point clouds generated using Open3D, as well as joint angles as part of the observation data. We use first-person RGB images and joint angles as inputs to DP. For DP3, we crop the point cloud to retain only the workspace, i.e., the hand, arm, and the object to be manipulated. The point cloud is then downsampled to 1024 points. This sparse point cloud, together with the joint angles, is used as the input to DP3. 

We train both DP and DP3 using 100, 50, and 20 trajectories generated by our method. During each training session, we record results from three checkpoints. For DP, we evaluate checkpoints at epochs 150, 200, and 250, while for DP3, we evaluate at epochs 1500, 2000, and 2500. For evaluation, we test each of the three checkpoints using seeds 0, 1, and 2, and report the mean and standard deviation of the success rates. 

The full success rate results across 20 tasks are shown in Tab. 3. For relatively simple tasks, DP3 exhibits few-shot learning capabilities when trained with data collected using our method, achieving high success rates with as few as 20 trajectories. For moderately difficult tasks where 20 trajectories yield insufficient performance, increasing the number of trajectories consistently improves success rates, indicating the effectiveness of our data scaling strategy. However, for several extremely challenging tasks, although our data generation method demonstrates high-quality demonstrations, neither DP nor DP3 is able to accurately learn each step. These tasks often involve long-horizon sequences and fine-grained object manipulation. We anticipate that future methods 

18 

Table 3: We present the DP and DP3 results for all 20 tasks using 100, 50, and 20 trajectories <u>generated by our method, and evaluate the success rates across 14 tasks using 3 random seeds.</u> 

|**Num of Demonstrations**|**20**|**50**|**100**||**20**|**50**|**100**|
|---|---|---|---|---|---|---|---|
|**Blocks Stack Easy**||||**Close Drawer**||||
|DP3|0.0_±_0.0|0.0_±_0.0|22.8_±_16.5|DP3|83.3_±_17.6|94.4_±_7.9|92.6_±_8.3|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|95.6_±_3.7|100.0_±_0.0|100.0_±_0.0|
|**Cup Pour Easy**<br>||||**Dual Bottles Pick Easy**<br>||||
|DP3|67.8_±_10.8|75.6_±_9.6|72.2_±_7.9|DP3|75.9_±_17.8|96.3_±_6.9|93.9_±_7.6|
|DP|0.0_±_0.0|2.2_±_6.3|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|**Dual Bottles Pick Hard**||||**Empty Cup Place**||||
|DP3|88.9_±_13.6|90.7_±_11.4|94.4_±_7.9|DP3|25.0_±_8.2|18.3_±_4.7|33.3_±_7.1|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|6.7_±_13.3|
|**Open Box Easy**||||**Open Box Hard**||||
|DP3|85.6_±_8.0|95.6_±_4.4|95.0_±_4.1|DP3|95.6_±_5.5|96.1_±_4.6|98.3_±_3.3|
|DP|93.3_±_13.3|100.0_±_0.0|100.0_±_0.0|DP|11.1_±_19.1|93.3_±_9.4|100.0_±_0.0|
|**Open Drawer**||||**Open Laptop Hard**||||
|DP3|58.3_±_8.3|76.0_±_13.1|84.4_±_11.3|DP3|100.0_±_0.0|100.0_±_0.0|100.0_±_0.0|
|DP|17.8_±_22.0|13.3_±_18.9|48.9_±_31.4|DP|15.6_±_22.7|11.1_±_9.9|35.6_±_32.4|
|**Close Box Hard**||||**Close Laptop Easy**||||
|DP3|88.9_±_17.6|96.3_±_6.9|96.3_±_6.9|DP3|100.0_±_0.0|100.0_±_0.0|100.0_±_0.0|
|DP|*82.2_±_22.0|*51.1_±_19.1|31.1_±_28.5|DP|37.8_±_23.9|40.0_±_23.1|48.9_±_25.1|
|**Handover and Storage**||||**Blocks Stack Hard**||||
|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|**Block Handover**||||**Close Box Easy**||||
|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP3|100.0_±_0.0|98.3_±_3.3|99.4_±_1.6|
|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|DP|97.8_±_6.3|100.0_±_0.0|91.1_±_13.7|
|**Close Laptop Hard**||||**Handover and Storage Cooperation**||||
|DP3|92.6_±_8.3|94.4_±_7.9|96.3_±_6.9|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|DP|*46.7_±_13.3|*42.2_±_34.6|33.3_±_26.7|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|**Open Laptop Easy**||||**Pyramid Stack**||||
|DP3|71.1_±_5.7|77.2_±_7.5|81.1_±_9.4|DP3|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|
|DP|*75.6_±_18.3|*71.1_±_16.6|60.0_±_16.3|DP|0.0_±_0.0|0.0_±_0.0|0.0_±_0.0|



that are capable of learning long-horizon behaviors will help address these challenges. As discussed in the main text, during DP training, some tasks show abnormally high success rates even when the policy has not learned a valid strategy. We mark such results with ‘*’ in the table. For example, in the task _Close Box Hard_ , with only 20 demonstrations, the arm tends to make rapid and random movements, occasionally closing the box lid by chance, which results in a deceptively high success rate. However, this behavior is unstable and unsafe. As the number of demonstrations increases (e.g., at 100 demonstrations), the arm no longer moves randomly and instead attempts to perform a deliberate closing motion. In this case, the hand needs to approach the lid from behind. Due to DP’s lack of spatial understanding and perception, the hand often collides with the lid, failing to maneuver behind it and ultimately leading to lower success rates. 

**Decision.** We adopt a diffusion policy framework for both DP and DP3, which predicts a future sequence of _H_ actions conditioned on _n_ obs steps of past observations. At inference time, the last _N_ act = _H − n_ obs + 1 predicted actions are executed to form the final control trajectory. In our experiments, we set _H_ = 8 and _n_ obs = 3 for both DP3 and DP. While both DP and DP3 share the core principle of conditional denoising diffusion, they differ in input modalities and policy architectures. 

DP3 processes 3D point cloud inputs using a DP3 encoder, where each frame consists of 1024 points with 3D coordinates. The encoded feature has a dimension of 128. The architecture incorporates Feature-wise Linear Modulation (FiLM) at the down, mid, and up layers of the convolutional UNet to improve conditional representation learning. In contrast, DP operates on image-based observations alongside low-dimensional proprioceptive inputs. The visual encoder is implemented using the `MultiImageObsEncoder` module, which supports multiple RGB observation keys, each associated with its own ResNet18 backbone (without pre-trained weights) or a shared model depending on configuration. 

Both methods adopt a noise schedule with _β_ start = 0 _._ 0001, _β_ end = 0 _._ 02, and a squared cosine schedule ( `squaredcos_cap_v2` ) over 100 diffusion training steps. However, the sampling strategies differ: DP3 employs DDIM ( `prediction_type=sample` ), while DP uses DDPM with _ϵ_ -prediction ( `prediction_type=epsilon` ) and enables `clip_sample` to stabilize training. 

**Training Setting.** For both DP and DP3, we adopt an exponential moving average (EMA) to stabilize the training process. The EMA parameters are updated with `inv_gamma` = 1 _._ 0, `power` = 0 _._ 75, and `max_value` = 0 _._ 9999. Since BatchNorm is not compatible with EMA, all normalization layers are replaced with GroupNorm to ensure training stability, particularly for DP with image inputs. Both policies use the AdamW optimizer with a learning rate of 1 _×_ 10<sup>_−_4</sup> , _β_ = [0 _._ 95 _,_ 0 _._ 999], and a weight decay of 1 _×_ 10<sup>_−_6</sup> . A cosine learning rate scheduler with a linear warm-up of 500 steps is applied to improve convergence during the initial training phase. 

19 

Table 4: Randomization Settings 

||**Position Randomization**|**Angle Randomization**||**Position Randomization**|**Angle Randomization**|
|---|---|---|---|---|---|
|**Blocks Stack Easy**|[-0.005, 0.005, -0.02, 0.02]|[-15, 15]|**Close Drawer**|[-0.05, 0.05, 0.18, -0.18]|[-25, 25]|
|**Cup Pour Easy**|[-0.02, 0.02, -0.04, 0.04]|[-30, 30]|**Dual Bottles Pick Easy**|[-0.005, 0.035, -0.025, 0.035]|[0, 0]|
|**Dual Bottles Pick Hard**|[-0.005, 0.035, -0.025, 0.035]|[0, 0]|**Empty Cup Place**|[-0.02, 0.02, -0.04, 0.04]|[-30, 30]|
|**Open Box Easy**|[-0.02, 0.02, -0.04, 0.04]|[30, 30]|**Open Box Hard**|[-0.02, 0.02, -0.04, 0.04]|[30, 30]|
|**Open Drawer**|[-0.05, 0.05, -0.18, 0.18]|[-25, 25]|**Open Laptop Hard**|[-0.02, 0.02, -0.04, 0.04]|[30, 30]|
|**Close Box Hard**|[-0.05, 0.05, -0.18, 0.18]|[-25, 25]|**Close Laptop Easy**|[-0.05, 0.05, -0.18, 0.18]|[-25, 25]|
|**Handover and Storage**|[-0.01, 0.01, 0, 0]|[0, 0]|**Blocks Stack Hard**|[-0.005, 0.005, -0.02, 0.02]|[-15, 15]|
|**Block Handover**|[-0.005, 0.005, -0.005, 0.005]|[0, 0]|**Close Box Easy**|[-0.05, 0.05, -0.18, 0.18]|[-25, 25]|
|**Close Laptop Hard**|[-0.05, 0.05, -0.18, 0.18]|[-25, 25]|**Handover and Storage Cooperation**|[-0.01, 0.01, 0, 0]|[0, 0]|
|**Open Laptop Easy**|[-0.01, 0.01, 0.04, -0.04]|[-30, 10]|**Pyramid Stack**|[-0.02, 0.02, -0.04, 0.04]|[-30, 30]|



DP3 is trained for 3000 epochs with checkpoints saved every 500 epochs. In contrast, DP is trained for 300 epochs with checkpoints saved every 50 epochs. The batch size is set to 256 for DP3 and 64 for DP, reflecting the difference in memory requirements between point cloud and image inputs. Data loading includes shuffling for training and deterministic ordering for validation, with `pin_memory=True` to improve performance. 

**Randomization Setting.** In the data collection and policy performance evaluation, We defined the randomization ranges for object positions and orientations, as shown in Tab. 4. Specifically, _Position Randomization_ [ _x_ 1 _, x_ 2 _, y_ 1 _, y_ 2] (in meters) denotes the range of randomized positions, where _x_ 1 and _x_ 2 represent the bounds for the _x_ -coordinate, and _y_ 1 and _y_ 2 represent the bounds for the _y_ -coordinate. _Angle Randomization_ [ _θ_ 1 _, θ_ 2] (in degrees) indicates the range for orientation randomization. To accommodate the capabilities of different algorithms, a small subset of tasks (DP3 vs. DP) adopts slightly different randomization ranges. 

## **C Experimental Details and Additional Experiments** 

### **C.1 Real-World Experiments** 

To further explore the application of HumanoidGen in real-world settings, we conducted experiments focusing on both data generation and sim2real transfer. 



Figure 9: Visualization of real scene and simulation scene. 

**Experiment Setup.** As shown in Fig. 9, we set up a real-world environment that closely mirrors the simulation environment. This includes a white table and a humanoid robot performing bimanual dexterous manipulation tasks. The robot used is the Unitree H1-2, equipped with a D435i depth camera mounted on its head, with a resolution of 640×480. The robot’s dexterous hands are the same Inspire hands used in the simulation environment. For the tasks, we selected the _dual bottles pick easy_ and _close laptop hard_ from the HGen-Bench for real-world transfer, using physical assets that match their simulated counterparts. The object poses in each trial were randomized to test robustness. Specifically, for the _dual bottles pick easy_ , the placement was randomized within a range of 6 cm × 6 cm and ±15° in orientation, while for the _close laptop hard_ , the randomization range was 6 cm × 6 cm and +10° to +20° in orientation. 

**Experimental Procedure.** The experiment consists of three main steps: **(i) Real2Sim Pose Estimation.** Using the existing digital assets, we first estimate the current poses of objects in the camera coordinate system with FoundationPose [56]. The estimated 6D poses are then transformed into the world coordinate system, allowing the corresponding digital assets to be placed at the same poses in the simulation environment. **(ii) Trajectory Collection.** We leverage LLM reasoning and the trajectory generation module of our framework to automatically generate execution trajectories in simulation, which are then executed on the real robot to collect real-world data. For each task, we collected 25 real-world trajectories. **(iii) Policy Training and Sim2Real Transfer.** To evaluate the effectiveness of the collected real-world data, we train diffusion policy models using 5 and 25 real-world trajectories, respectively. In addition, to investigate the contribution of simulation data to real-world policy performance, we augment the real-world dataset with additional simulated trajectories. Specifically, for each task, we train and evaluate policies using 5 real-world trajectories combined with 100 simulated trajectories, aiming to analyze how simulation data improves real-world performance. 

20 

Table 5: **Experiment Results.** DP represents the diffusion policy success rate under different training settings: 5 real trajectories (5R), 25 real trajectories (25R), and 100 simulated + 5 real trajectories <u>(100S+5R).</u> 

|**Task**|**Collection Success Rate (%)**|**Collection Time (s)**|**DP (5R)**|**DP (25R)**|**DP (100S+5R)**|
|---|---|---|---|---|---|
|**Dual Bottles Pick Easy**|85|16|0% (0/20)|**60% (12/20)**|**65% (13/20)**|
|**Close Laptop Hard**|90|13|20% (4/20)|**70% (14/20)**|**70% (14/20)**|



**Experimental Results.** We evaluated two tasks, _dual bottles pick easy_ and _close laptop hard_ , in real-world experiments. The metrics include the data collection success rate, the average collection time per trajectory, and the performance of DP [43] models trained under different data settings. As shown in Tab. 5, the average time to collect a single real-world trajectory is only about 14 seconds, and the data collection success rate exceeds 85% for both tasks. The results of DP model training demonstrate that policies trained with 25 real-world trajectories significantly outperform those trained with only 5. This indicates that the success rate increases with the amount of real-world data. Furthermore, pretraining with 100 simulated trajectories followed by fine-tuning on 5 real-world trajectories achieves comparable or even better performance than using 25 real-world trajectories alone, particularly in the _dual bottles pick easy_ task. 

### **C.2 Automatic Asset Annotation Evaluation** 

To assess the effectiveness of our automatic annotation method based on annotation migration, we conducted quantitative analyses. 



<!-- Start of picture text -->
Cup<br> (rim)<br>Cup<br>(handle)<br>Bowl<br>Drawer<br>Laptop<br><!-- End of picture text -->

Figure 10: Visualization of annotation migration. 

**Experimental Setup.** As illustrated in Fig. 10, we selected five parts from four commonly used object types for automatic annotation. The cup contains two parts: the rim and the handle. For each object category, 20 assets were randomly selected from [14, 24, 19]. The rendering and reprojection processes for automatic annotation were implemented using ManiSkill3 [52], the same simulation environment as our data generation framework. 

21 

Table 6: Evaluation of annotation time and success rate. 

|**Evaluation Metric**|**Cup (rim)**|**Cup (handle)**|**Bowl**|**Drawer**|**Laptop**|
|---|---|---|---|---|---|
|**Manual Annotation Time (s)**|4.00|4.00|4.00|6.00|6.00|
|**Automated Migration Time (s)**|0.72|0.72|0.79|0.80|0.81|
|**Migration Success Rate (%)**|100.0% (20/20)|90.0% (18/20)|100.0% (20/20)|90.0% (18/20)|100.0% (20/20)|



**Experimental Results.** We compared the annotation time between manual and automatic annotation and evaluated the success rate of automatic annotation, as summarized in Tab. 6. For manual annotation, simple rigid objects such as cups and bowls required about 4 seconds per part, while articulated objects like laptops and drawers took around 6 seconds. In contrast, our automatic annotation required only about 0.7 seconds per asset on average, achieving a substantial acceleration. The success rate of automatic annotation was also high, reaching 100% for the cup rim, bowl, and laptop, and over 90% for other parts. The few failures, such as those for the cup handle and drawer, were primarily caused by significant geometric variations, such as differences in handle shapes between circular and rectangular designs. 

### **C.3 Additional Challenging Dexterous Manipulation Tasks** 

To further evaluate the scalability and robustness of our framework beyond the 20 main tabletop manipulation tasks, we design five additional challenging tasks focusing on bimanual coordination, dexterous contact-rich operations, and complex tabletop environments, as illustrated in Fig. 11. 





**Rotate Safe Knob Press Toaster** 



**Open Safe Door** 



**Dual Lift Pot** 



**Blocks Stack Hard With Barrier** 

Figure 11: Illustration of the five additional challenging bimanual dexterous manipulation tasks used for supplementary evaluation: _rotate safe knob_ , _press toaster_ , _open safe door_ , _dual lift pot_ , and _blocks stack hard With barrier_ . These tasks involve coordinated bimanual motions, contact-rich dexterous operations, and complex tabletop environments, highlighting the scalability of our framework. 

**Experimental Setup.** The five additional tasks include _rotate safe knob_ , _press toaster_ , _open safe door_ , _dual lift pot_ , and _blocks stack hard with barrier_ . In _rotate safe knob_ , the robot precisely pinches and rotates a knob, requiring accurate fingertip control to prevent slippage. In _press toaster_ , the robot presses a switch using a single finger, demonstrating fine dexterous motion beyond grasping or pinching. The _open safe door_ task involves pulling open a door with a vertically oriented hinge, testing manipulation of articulated mechanisms. In _dual lift pot_ , the robot must grasp both handles of a pot simultaneously and lift it, testing coordinated bimanual manipulation. Finally, _blocks stack hard with barrier_ requires stacking blocks in an environment where more than 60% of the workspace is occupied by barriers, posing severe spatial constraints. 

Table 7: Evaluation of additional challenging dexterous manipulation tasks. Each task is tested under randomized initial positions and orientations. 

|**Metric**|**Rotate Safe Knob**|**Press Toaster**|**Open Safe Door**|**Dual Lift Pot**|**Blocks Stack Hard With Barrier**|
|---|---|---|---|---|---|
|**Randomization**|5 cm_×_5 cm,_±_15°|5 cm_×_5 cm,_±_15°|5 cm_×_5 cm,_±_15°|12 cm_×_6 cm,_±_15°|6 cm_×_8 cm,_±_10°|
|**Success Rate(%)**|91.09|87.72|95.24|93.00|73.00|



**Experimental Results.** As shown in Tab. 7, our framework achieves high success rates across all five tasks, with three exceeding 90%. These results further validate the scalability of our method in handling bimanual coordination and contact-rich dexterous manipulation. Even in the most challenging case, _blocks stack hard with barrier_ , where over 60% of the workspace is blocked by obstacles, the framework still achieves a 73% success rate, outperforming existing baselines under comparable conditions. 

22 

### **C.4 Resource and Efficiency Analysis of HumanoidGen** 

We analyze average computational and token consumption across all 20 tasks in HGen-Bench, including both time cost and LLM resource usage. The detailed statistics are summarized in Tab. 8. 

Table 8: Average time and resource consumption for each stage in the HumanoidGen data generation pipeline, computed over all 20 tasks in HGen-Bench. Manual annotation requires limited human effort, while all other stages are fully automated. 

|**Metric**|**Manual Annotation Automatic Annotation**|**Scene Generation**|**Script Generation**|**Data Collection Execution**|
|---|---|---|---|---|
|**Time (s)**|4-6<br>1.17|12.64|18.31|14.40|
|**Resource Cost**|Human Operator<br>Automated Process<br>|LLM (2,958 tokens avg.)|LLM (3,745 tokens avg.)|Motion Planner (0.53 s)|



It is important to note that generating a new trajectory does not always require executing all stages of the pipeline. Depending on the scenario, certain steps can be skipped or reused, significantly improving efficiency: (i) For pose randomization of manipulated objects, tabletop obstacles, or room-level scene extensions, the system can directly execute the previously generated running scripts to collect new trajectories. The randomization operations are executed at the millisecond level and thus have negligible time cost. (ii) For tasks sharing identical tabletop setups but differing in manipulation procedures, such as _handover and storage_ and _handover and storage cooperation_ . For these tasks, scene initialization can be reused, requiring only the generation of new execution scripts. (iii) When different objects are used but all exist in the asset library, no manual intervention is required; automated scene generation and code synthesis are sufficient to produce new executable scripts for data collection. Only when introducing new object categories absent from the asset library is manual annotation needed, which takes merely 4–6 seconds per asset class. 

These results demonstrate that HumanoidGen achieves high efficiency in both automated data generation and resource utilization, enabling scalable and reproducible large-scale evaluations in HGen-Bench. 

### **C.5 Comparison with Existing Generation Frameworks** 

To demonstrate the advantages of our proposed framework, we conduct a comparison with several state-of-the-art robot manipulation data generation frameworks, including both augmentation-based and zero-shot generation approaches. 

**Augmentation-Based Frameworks.** These methods [51, 57] require an existing expert trajectory as the basis for data expansion, which typically involves teleoperation-based data collection. Moreover, manual annotation is needed to segment long-horizon demonstrations into multiple sub-stages before augmentation can be applied. When the task execution mode changes, such as switching from _left-to-right_ to _right-to-left_ handover, or modifying the stacking order in a block stacking task, new expert data collection and segmentation are needed. In contrast, our framework achieves object-level reusability and full automation without human intervention, enabling flexible and scalable task generation under varied manipulation settings. 

Table 9: Comparison of different robot manipulation data generation frameworks. Only our proposed HumanoidGen provides a unified and fully automated pipeline that supports bimanual dexterous hands, scene generation, room-level synthesis, and dynamic collision management. 

|**Framework**|**Bimanual**|**Dexterous**<br>**Hand**|**Tabletop Scene**<br>**Generation**|**Room-level**<br>**Scene Synthesis**|**Dynamic Collision**<br>**Management**|
|---|---|---|---|---|---|
|RoboGen [22]|Yes|No|Yes|Yes|No|
|Gensim [23]|No|No|Yes|No|No|
|Gensim2 [27]|No|No|Yes|Yes|No|
|RoboTwin [19]|Yes|No|No|No|No|
|RoboFactory [58]|Yes|No|No|No|No|
|HumanoidGen(Ours)|Yes|Yes|Yes|Yes|Yes|



**Zero-Shot Generation Frameworks.** For frameworks that support zero-shot data generation without relying on expert demonstrations, a comparison with HumanoidGen is summarized in Tab. 9. It can be clearly observed that HumanoidGen is the first framework to provide a systematic solution for bimanual dexterous hand manipulation problems. Other frameworks do not incorporate dexterous hands as end-effectors. RoboTwin [19] and RoboFactory [58] lack table-top scene generation and room-level scene scaling, both of which are included in HumanoidGen, demonstrating the comprehensiveness of our work. Additionally, only our framework includes dynamic collision management by LLMs, enhancing the flexibility and effectiveness of our framework in handling collisions during long-horizon tasks. 

23 

### **C.6 Comparison Across Different Large Models** 

To further investigate the impact of different large models serving as the planner within our framework, we conduct a comparative study involving a reasoning model, a chat model, and a multimodal model, both with and without visual input. Specifically, we evaluate _DeepSeek-R1_ (reasoning model), _DeepSeek-Chat-v3_ (chat model), and _GPT-4o_ in both its language-only and multimodal configurations. Four representative tasks, each from a distinct category in Fig. 5, are selected for this experiment. 



<!-- Start of picture text -->
Open Drawer, Close Laptop Hard, Block Handover, Handover and Storage,<br>single arm, single arm, bimanual, bimanual,<br>free motion space complex collision scenarios free motion space long-horizon,<br>complex collision scenarios<br><!-- End of picture text -->

Figure 12: Comparison of different large models used as the planning module in our framework: a reasoning model (DeepSeek-R1), a chat model (DeepSeek-Chat-v3), and a multimodal model with and without visual input (GPT-4o language-only and GPT-4o multimodal). 

As shown in Fig. 12, all four models achieve high success rates in generating valid constraints and executable planning code. Specifically, GPT-4o (with and without image inputs) shows a consistently good performance across all four tasks, whereas the Deepseek reasoning model and the Deepseek chat model have a slight performance decline when generating plans for bimanual and long-horizon tasks. The consistent high performance of these different models across various tasks demonstrates the effectiveness of our framework and its compatibility with diverse models. 

### **C.7 Task Descriptions in Data Generation Experiment** 

We describe our 20 tabletop-level tasks in detail in Tab. 10. The initial positions of target objects in all tasks are randomized. The tasks include 12 single-arm tasks and 8 bimanual tasks. Dexterous hands are used as end-effectors in all tasks. For bimanual tasks, the appropriate arms to manipulate target objects are selected according to the distance between the arms and the objects. Some tasks involve object handoffs between two hands, like _block handover_ and _handover and storage_ . Furthermore, _handover and storage cooperation_ requires the coordination between both arms to complete the task. 

### **C.8 Task Descriptions in MCTS Experiment** 

As mentioned in §5.2, to evaluate the effectiveness of MCTS in enhancing the demonstration generation process of HumanoidGen, we simplified task descriptions to provide minimal guidance in the experiments. As shown in Tab. 11, we did not notice the operation order or the operation executor, both of which were inferred by the reasoning LLM. 

## **D More Discussion on Limitations and Future Work** 

Despite the promising results achieved by our framework, several limitations remain. First, human intervention has not been completely eliminated. For asset categories and atomic manipulation types that have not been previously annotated, automatic labeling through annotation transfer is not possible, requiring manual annotation instead. Consequently, generating a task that involves a novel asset category still demands prior human annotation of its manipulation primitives. However, we note that several recent works have proposed learning-based methods for predicting contact points, axes, or grasp poses [59, 60, 61]. Although these approaches are not yet fully mature and still face generalization challenges, they demonstrate certain zero-shot capabilities that could be integrated into our annotation pipeline. Combining these advances with our generative framework holds promise for fully automated data generation, which we plan to explore in future work. 

Second, our current framework cannot yet generate all types of dexterous manipulation tasks. On one hand, due to the limitations of the ManiSkill3 [52] physics engine, tasks involving deformable or fluid objects cannot be simulated. On the other hand, our arm control currently relies on a low-level motion planner, making it difficult to handle manipulation tasks with ambiguous or dynamic objectives, such as push-T or cloth flattening. These 

24 

Table 10: The descriptions of our 20 tasks. 

|**Task**|**Description**|
|---|---|
|**Block Handover**|A rectangular cube is placed on the right side of the table. The right hand pinches the cube and moves it to hand over to<br>the left hand. The left hand then pinches the cube and moves the cube above the target cube to release it.|
|**Blocks Stack Easy**|Two cubes, cube0 and cube1, are placed on the table. Initially, both the left and right hands simultaneously pinch cube0<br>and cube1, respectively. The left hand then put cube0 to a specified position. Following this, the right hand moves cube1<br>to put it above cube0.|
|**Blocks Stack Hard**|Three cubes, cube0, cube1, and cube2, are placed on the table. Initially, the left hand pinches cube0 and the right hand<br>pinches cube1 simultaneously. The left hand puts cube0 at the target place. Then the right hand puts cube1 above cube0.<br>Finally, the right hand picks up cube2, puts it above cube1.|
|**Close Box Easy**|A box is placed on the table. Initially, the right hand approaches the box lid from above. Then, the right hand moves to<br>flip the box lid down.|
|**Close Box Hard**|A box is placed on the table. Initially, the right hand grasps the box lid. While maintaining its grasp, the right hand<br>adjusts the box lid’s openness to 0.3 and releases it.|
|**Close Drawer**|A drawer is placed on the table. Initially, the left hand moves to grasp the drawer handle. With the left hand attached to<br>the drawer handle, the left hand pushes the drawer back to an openness of 0. Finally, the left hand releases the drawer<br>handle.|
|**Close Laptop Easy**|A laptop is placed on the table. First, the right hand approaches the laptop screen from above. Then, the right hand<br>moves to flip the laptop screen down.|
|**Close Laptop Hard**|A laptop is placed on the table. First, the right hand grasps the laptop screen from above. While maintaining its grasp,<br>the right hand adjusts the laptop screen’s openness to 0.3. Then, the right hand releases the laptop screen and moves<br>above it. Finally, the right hand moves to flip the laptop screen fully down.|
|**Cup Pour Easy**|A cup and a bowl are placed on the table. First, the right hand grasps the cup and moves it above and in front of the<br>bowl. Finally, the right hand tilts the cup to pour its contents into the bowl.|
|**Dual Bottles Pick Easy**|Two bottles, bottle0 and bottle1, are placed on the table. The left and right hands simultaneously grasp the two bottles<br>and lift them to the target position.|
|**Dual Bottles Pick Hard**|Two bottles, bottle0 and bottle1, are placed on the table. The left and right hands simultaneously grasp the two bottles<br>and lift them to the target position.|
|**Empty Cup Place**|A cup and a plate are placed on the table. The task is to use one hand to grasp the cup and place it directly over the plate.|
|**Handover and Storage**|A drawer and a rectangular cube0 are placed on the table. First, the left hand grasps the drawer handle and pulls it out to<br>an openness of 0.9. Then the left hand releases the drawer handle. Next, the right hand pinches the cube and moves it to<br>hand it over to the left hand. The left hand then moves to pitch the cube, taking it from the right hand. The left hand<br>moves the cube above the open drawer and releases it to put it into the drawer. Afterwards, the left hand moves to grasp<br>the drawer handle again, pushes it back to an openness of 0, and finally releases the drawer handle.|
|**Handover and Storage**<br>**Cooperation**|A drawer and a rectangular cube0 are placed on the table. First, the left hand grasps the drawer handle, and the right<br>hand pinches cube0 simultaneously. Then, the right hand moves the cube to an intermediate position while the left hand<br>pulls the drawer out to an openness of 0.9 at the same time. The left hand then releases the drawer handle. Next, the<br>left hand moves to pinch the cube, taking it from the right hand. The left hand moves the cube above the drawer and<br>releases it to put it into the drawer. Afterwards, the left hand moves to grasp the drawer handle again, pushes it back to<br>an openness of 0, and finally releases the drawer handle.|
|**Open Box Easy**|A box is placed on the table. First, the right hand moves to be under the box lid. Then the right hand moves to flip the<br>box lid up.|
|**Open Box Hard**|A box is placed on the table. First, the right hand moves to grasp the box lid. While maintaining its grasp, the right hand<br>adjusts the box lid’s openness to 0.8 and releases it. After this, the right hand releases the box lid and moves to be under<br>it. Finally, the right hand moves to flip the box lid up.|
|**Open Drawer**|A drawer is placed on the table. First, the left hand moves to grasp the drawer handle. With the left hand grasping the<br>drawer handle, it pulls the drawer out to an openness of 1. Finally, the left hand releases the drawer handle.|
|**Open Laptop Easy**|A laptop is placed on the table. First, the right hand moves to be under the laptop screen. Then, the right hand moves to<br>flip the laptop screen up.|
|**Open Laptop Hard**|A laptop is placed on the table. First, the right hand grasps the laptop and flips it up to an openness of 0.55. Then, the<br>right hand releases the initial grasp and moves to be under the laptop screen. Finally, it moves to flip the laptop screen to<br>be fully up.|
|**Pyramid Stack**|Three cubes, cube0, cube1, and cube2, are placed on the table. First, the left hand and the right hand simultaneously<br>pinch cube0 and cube1, respectively. The left hand then moves cube0 to put it at the target position. After this, the right<br>hand moves cube1 to put it on the right side of cube0. Then, the right hand pinches cube2 and moves it to put it in the<br>middle and above cube0 and cube1.|



tasks involve continuous state adjustments rather than planning toward a single target pose, which cannot be realized solely through motion planning. In the future, we plan to extend our framework to support more diverse physics engines, such as IsaacSim [15] and MuJoCo [16], enabling richer simulation scenarios. Moreover, leveraging the extensibility of our framework, we will explore combining goal-conditioned motion planning with goal-agnostic pre-trained atomic operation models, forming a unified library of atomic operations to support a wider range of dexterous manipulation tasks. 

Finally, we plan to expand HGen-Bench with additional assets, scenes, tasks, and evaluation policies to enable more comprehensive benchmarking and broader applicability. 

25 

Table 11: The descriptions of 4 tasks in the MCTS experiment. 

|**Task**|**Description**|
|---|---|
|**Block Stack Single**|Stack cube1 on top of cube0.|
|**Blocks Stack Easy**|Stack the two cubes on the table into a single pile.|
|**Blocks Stack Hard**|Stack the three cubes on the table into a single pile.|
|**Pyramid Stack**|Stack the three cubes into a pyramid shape in the center area, with two cubes at the bottom and one cube stacked on top<br>of them.|



## **E Prompts and Generation Samples** 

We show the prompt templates and the sample code generated by LLMs in scene generation and demonstration script generation (with and without integrating MCTS). The meanings of the placeholders in the prompt templates are explained in Table 12. 

Table 12: The placeholders in the prompt templates and their meanings. 

|**Placeholder**|**Meaning**|
|---|---|
|**ASSET_INFO**|The information of the assets in the asset library.|
|**ASSETS_ATTRIBUTES**|The default attributes of the assets.|
|**INITIAL_ASSET_STATE**|The asset states when the scene is initialized, before any actions<br>are executed.|
|**CURRENT_ASSET_STATE**|The current states of the assets on the tabletop.|
|**EXECUTED_CODE**|Code for actions executed by the robot to transform the asset state<br>on the tabletop from the initial state to the current state.|
|**PROHIBITED_ACTION**|The actions prohibited for the next step.|
|**ASSETS_STATUS**|The current states of the assets in the task scene.|
|**ROBOT_END_EFFECTOR**|The current state of the robot end-effector.|



### **E.1 Prompt Template for Scene Generation** 

1 <mark>`You are a professional AI simulation environment code generation assistant capable of generating logical reasoning and accurate code. You need to generate reasoning monologues for the initial scene of the task based on the user ’s given task , i.e., what kind of initial scene to generate and why the initial scene is designed this way. Afterward , provide an answer that includes the code to construct the scene.`</mark> 2 <mark>`======`</mark> 3 <mark>`Scene information (all coordinates are in the world coordinate system):`</mark> 4 <mark>`Dual -arm robot , pose.p=[ -0.85 ,0 ,0] , pose.q=[1 ,0 ,0 ,0]`</mark> 5 <mark>`Table surface , "x from -0.42 to -0.19, y from -1.1 to 1.16 , z=0"`</mark> 6 <mark>`======`</mark> 7 <mark>`Available assets:`</mark> 8 <mark>`ASSETS_INFO`</mark> 9 <mark>`======`</mark> 10 <mark>`Code Example: Task to place two cubes side by side.`</mark> 11 <mark>`‘‘‘python`</mark> 12 <mark>`from humanoidgen.envs.example.task_env import * # Import necessary libraries`</mark> 13 <mark>`@register_env (" place_cubes_side_by_side ", max_episode_steps =200) # Register the environment , name can be set based on the task`</mark> 14 <mark>`class PutTwoCubeAdjacentEnv ( TableSetting ): # Must inherit from TableSetting`</mark> 15 <mark>`env_name= " place_cubes_side_by_side "`</mark> 16 <mark>`def _load_scene (self , options: Dict): # Load objects`</mark> 17 <mark>`super ()._load_scene (options)`</mark> 18 <mark>`self. _add_object(type_name =" cube", type_id =1) # name =" cube", obj_id =0, yellow cube`</mark> 19 <mark>`self. _add_object(type_name =" cube", type_id =0) # name =" cube", obj_id =1, green cube`</mark> 20 21 <mark>`def _initialize_episode (self , env_idx: torch.Tensor , options: Dict): # Set object positions`</mark> 

26 

22 <mark>`super (). _initialize_episode (env_idx , options)`</mark> 23 <mark>`self. _set_object_pose (type_name =" cube", obj_id =0, pose=sapien.Pose(`</mark> 24 <mark>`p=[ -0.38 , 0.28 , 0.02] ,`</mark> 25 <mark>`q=[1, 0, 0, 0]`</mark> 26 <mark>`))`</mark> 27 <mark>`self. _set_object_pose (type_name =" cube", obj_id =1, pose=sapien.Pose(`</mark> 28 <mark>`p=[ -0.32 , -0.32, 0.02] ,`</mark> 29 <mark>`q=[1, 0, 0, 0]`</mark> 30 <mark>`))`</mark> 31 32 <mark>`def check_success (self):`</mark> 33 <mark>`print ("=========== check_success ===========")`</mark> 34 <mark>`p0 = self.cube [0]. pose.p.numpy () [0]`</mark> 35 <mark>`p1 = self.cube [1]. pose.p.numpy () [0]`</mark> 36 <mark>`target_position_0 =[-0.3, 0.02 ,0.02]`</mark> 37 <mark>`target_position_1 =[-0.3, -0.02 ,0.02]`</mark> 38 <mark>`eps = [0.03 , 0.03]`</mark> 39 <mark>`success_0 = all(abs(p0[i] - target_position_0 [i]) <= eps[i] for i in range (2))`</mark> 40 <mark>`success_1 = all(abs(p1[i] - target_position_1 [i]) <= eps[i] for i in range (2))`</mark> 41 <mark>`print (" cube [0] position :", p0)`</mark> 42 <mark>`print (" cube [0] target position :", target_position_0 )`</mark> 43 <mark>`print (" cube [1] position :", p1)`</mark> 44 <mark>`print (" cube [1] target position :", target_position_1 )`</mark> 45 <mark>`print (" success_0 :", success_0)`</mark> 46 <mark>`print (" success_1 :", success_1)`</mark> 47 <mark>`return success_0 and success_1`</mark> 48 <mark>`‘‘‘`</mark> 49 <mark>`======`</mark> 50 <mark>`Notes:`</mark> 51 <mark>`- ‘type_id ‘ represents different models of the same type of object , while ‘obj_id ‘ indicates the order in which objects of the same type are added.`</mark> 52 <mark>`- The left hand ’s operable range is x in [-0.42, -0.19], y in [-0.07, 0.36]; the right hand ’s range is x in [-0.42, -0.19], y in [-0.36, 0.07]. Objects must be placed within these intervals (note: meeting the range is a necessary but not sufficient condition. Successful grasping may still fail due to object orientation , collisions , or gripper constraints ).`</mark> 53 <mark>`- The robot ’s coordinate system aligns with the world frame: +X (front of robot), +Y (left of robot), +Z (up of robot).`</mark> 54 <mark>`- The object ’s bounding box (BBX) represents its dimensions in its own coordinate system (axis -aligned when the orientation quaternion is q=[1 ,0 ,0 ,0]). For example , a can with BBX [0.054 , 0.1, 0.054] has lengths of 0.054 units along X/Z-axes and 0.1 units along the Y-axis.`</mark> 55 <mark>`======`</mark> 56 <mark>`Now please generate the initial scene of task "TASKNAME ".`</mark> 

### **E.2 Sample Scene Code for Blocks Stack Hard Generated by HumanoidGen** 

1 <mark>`from humanoidgen .envs.example.task_env import *`</mark> 2 3 <mark>`@register_env (" blocks_stack_hard ", max_episode_steps =200)`</mark> 4 <mark>`class BlocksStackHardMctsEnv ( TableSetting ):`</mark> 5 <mark>`env_name= " blocks_stack_hard "`</mark> 6 7 <mark>`def _load_scene (self , options: Dict):`</mark> 8 <mark>`super (). _load_scene(options)`</mark> 9 <mark>`self. _add_object(type_name="cube", type_id =0)`</mark> 10 <mark>`self. _add_object(type_name="cube", type_id =1)`</mark> 11 <mark>`self. _add_object(type_name="cube", type_id =2)`</mark> 12 13 <mark>`def _initialize_episode (self , env_idx: torch.Tensor , options: Dict):`</mark> 14 <mark>`super (). _initialize_episode (env_idx , options)`</mark> 15 <mark>`default_pose = [`</mark> 16 <mark>`sapien.Pose(p=[ -0.32 , 0.32 , 0.05] , q=[1,0, 0, 0]) ,`</mark> 17 <mark>`sapien.Pose(p=[ -0.32 , -0.32, 0.05] , q=[1, 0, 0, 0]) ,`</mark> 18 <mark>`sapien.Pose(p=[ -0.45 , -0.32, 0.05] , q=[1, 0, 0, 0]) ,`</mark> 19 <mark>`]`</mark> 20 <mark>`if self. random_scene :`</mark> 21 <mark>`default_pose =self. get_random_pose ( default_pose = default_pose )`</mark> 22 <mark>`if not self.random_once or (self. random_once and not hasattr(self , " random_pose ")):`</mark> 23 <mark>`self. random_pose = default_pose`</mark> 24 <mark>`self. _set_object_pose (`</mark> 

27 

25 <mark>`type_name="cube",`</mark> 26 <mark>`obj_id =0,`</mark> 27 <mark>`pose=self.random_pose [0]`</mark> 28 <mark>`)`</mark> 29 30 <mark>`self. _set_object_pose (`</mark> 31 <mark>`type_name="cube",`</mark> 32 <mark>`obj_id =1,`</mark> 33 <mark>`pose=self.random_pose [1]`</mark> 34 <mark>`)`</mark> 35 36 <mark>`self. _set_object_pose (`</mark> 37 <mark>`type_name="cube",`</mark> 38 <mark>`obj_id =2,`</mark> 39 <mark>`pose=self.random_pose [2]`</mark> 40 <mark>`)`</mark> 41 42 <mark>`def check_success (self):`</mark> 43 <mark>`print("=========== check_success =========== ")`</mark> 44 <mark>`positions = [`</mark> 45 <mark>`self.cube [0]. pose.p.numpy ()[0],`</mark> 46 <mark>`self.cube [1]. pose.p.numpy ()[0],`</mark> 47 <mark>`self.cube [2]. pose.p.numpy () [0]`</mark> 48 <mark>`]`</mark> 49 <mark>`positions.sort(key=lambda p: p[2])`</mark> 50 <mark>`eps_xy = 0.03`</mark> 51 <mark>`eps_z = 0.005`</mark> 52 <mark>`height_diff = 0.04`</mark> 53 <mark>`xy_aligned = (`</mark> 54 <mark>`abs(positions [0][0] - positions [1][0]) <= eps_xy and abs(positions [0][1] - positions [1][1]) <= eps_xy and`</mark> 55 <mark>`abs(positions [1][0] - positions [2][0]) <= eps_xy and abs(positions [1][1] - positions [2][1]) <= eps_xy`</mark> 56 <mark>`)`</mark> 57 <mark>`z_aligned = (`</mark> 58 <mark>`abs(positions [1][2] - positions [0][2] - height_diff ) <= eps_z and`</mark> 59 <mark>`abs(positions [2][2] - positions [1][2] - height_diff ) <= eps_z`</mark> 60 <mark>`)`</mark> 61 <mark>`return xy_aligned and z_aligned`</mark> 

### **E.3 Prompt Template for Demonstration Script Generation** 

1 <mark>`You are a professional assistant for generating code that enables dual -arm robots to perform tabletop tasks. Please generate logically structured code to execute the user -specified tasks based on the provided context.`</mark> 2 <mark>`======`</mark> 3 <mark>`Scene information :`</mark> 4 <mark>`Dual -arm robot , pose.p=[ -0.85 ,0 ,0] , pose.q=[1,0,0,0], " robot_base_link " is the connection between the "torso_link" and the "pelvis".`</mark> 5 <mark>`Table surface , x in [-0.42, -0.19], y in [-1.1, 1.16] , z=0`</mark> 6 <mark>`======`</mark> 7 <mark>`Assets attributes (The default state of the assets , not the current state):`</mark> 8 <mark>`ASSETS_ATTRIBUTES`</mark> 9 <mark>`======`</mark> 10 <mark>`Assets status (The current state of the assets):`</mark> 11 <mark>`ASSETS_STATUS`</mark> 12 <mark>`======`</mark> 13 <mark>`Robot end -effector (wrist) current status:`</mark> 14 <mark>`ROBOT_END_EFFECTOR`</mark> 15 <mark>`======`</mark> 16 <mark>`Available functions:`</mark> 17 <mark>`def hand_pre_grasp (hand_name):`</mark> 18 <mark>`Function: Adjusts the thumb movement of the specified hand to position it opposite the index finger , preparing for subsequent grasping operations. This should typically be called before executing ’move_to_pose_with_screw ’ to reach the pre -grasp pose.`</mark> 19 <mark>`Return: None`</mark> 20 <mark>`Args:`</mark> 21 <mark>`- hand_name (str , optional): "all" (both), "right", or "left". Default: "all".`</mark> 22 <mark>`Example:`</mark> 23 <mark>`planner. hand_pre_grasp ("left") # Control the left hand fingers to assume the pre -grasp pose`</mark> 24 <mark>`planner. hand_pre_grasp ("right") # Control the right hand fingers to assume the pre -grasp pose`</mark> 

28 

25 <mark>`planner. hand_pre_grasp ("all")`</mark> 26 27 <mark>`def hand_grasp(hand_name , grasp_object , obj_id):`</mark> 28 <mark>`Function: Control the hand to close.`</mark> 29 <mark>`Return: None`</mark> 30 <mark>`Args:`</mark> 31 <mark>`- hand_name (str , Mandatory): "right" or "left".`</mark> 32 <mark>`- grasp_object (str , Mandatory): The type of the grasped object.`</mark> 33 <mark>`- obj_id (int , Mandatory): The object id of the grasped object.`</mark> 34 <mark>`Example:`</mark> 35 <mark>`planner.hand_grasp("left",grasp_object ="can",obj_id =0) # Control the left hand close to grasp the bottle 0`</mark> 36 <mark>`planner.hand_grasp("right",grasp_object ="can",obj_id =1) # Control the right hand close to grasp the bottle 0`</mark> 37 38 <mark>`def hand_pre_pinch (hand_name):`</mark> 39 <mark>`Usage: Similar to the usage of the hand_pre_grasp function.`</mark> 40 41 <mark>`def hand_pinch(hand_name , pinch_object , obj_id):`</mark> 42 <mark>`Usage: Similar to the usage of the hand_grasp function.`</mark> 43 44 <mark>`def open_hand(self , hand_name):`</mark> 45 <mark>`Function: Control the hand to open the fingers.`</mark> 46 <mark>`Return: None`</mark> 47 <mark>`Args:`</mark> 48 <mark>`- hand_name (str , Mandatory): "right" or "left".`</mark> 49 50 <mark>`def generate_constraints (self ,obj_name ,obj_id ,action ,hand_name):`</mark> 51 <mark>`Function: Generate the constraints for the end -effector pose when performing a specific action.`</mark> 52 <mark>`Return: constraints`</mark> 53 <mark>`Args:`</mark> 54 <mark>`- obj_name (str , Mandatory): The object to be operated.`</mark> 55 <mark>`- obj_id (int , Mandatory): The object id of the operated object.`</mark> 56 <mark>`- action (str , Mandatory): The action name corresponding to the constraints . Can be "pinch", "grasp", "target", "move", "target1", "target2"`</mark> 57 <mark>`- "pinch": Move to the pose for pinching the object.`</mark> 58 <mark>`- "grasp": Move to the pose for grasping the object.`</mark> 59 <mark>`- "target": Move the "target" pose`</mark> 60 <mark>`- "target1": Move the "target1" pose`</mark> 61 <mark>`- "target2": Move the "target2" pose`</mark> 62 <mark>`- "move": Move to a specific pose relative to an object.`</mark> 63 <mark>`- hand_name (str , Mandatory): "right" or "left".`</mark> 64 <mark>`- openness (float , Optional): [necessary for openness constraint generation] the openness of the manipulated object after being manipulated . The value should be between 0 or 1. This argment is only used when the action is " grasp" or "pinch".`</mark> 65 <mark>`- relative_obj_name (str , Optional): [necessary for relative pose constraint generation] the name of the object to be used as a reference for defining the relative pose.`</mark> 66 <mark>`- relative_obj_id (int , Optional): [necessary for relative pose constraint generation] the id of the object to be used as a reference for defining the relative pose.`</mark> 67 <mark>`- relative_p (np.array , Optional): [necessary for relative pose constraint generation] the relative position of the end -effector to the reference object.`</mark> 68 <mark>`Example:`</mark> 69 <mark>`constraint_l =planner. generate_constraints (obj_name="can", obj_id =0, action ="pinch", hand_name="left") # Generate the constraints for the left hand end -effector to move to the pre -pinch pose for pinching can0`</mark> 70 <mark>`constraint_l =planner. generate_constraints (obj_name="can", obj_id =0, action ="grasp", hand_name="left") # Generate the constraints for the left hand end -effector to move to the pre -grasp pose for grasping can0`</mark> 71 <mark>`constraint_l =planner. generate_constraints (obj_name="can", obj_id =0, action ="target", hand_name="left") # Generate the constraints for the left hand end -effector to move to the target pose after grasping can0`</mark> 72 <mark>`constraint_r =planner. generate_constraints (obj_name="can", obj_id =1, action ="move", hand_name="right",relative_obj_name ="can",relative_obj_id =0, relative_p=np.array ([0 ,0 ,0.06])) # Generate the end -effector pose for the right hand after grasping can1 to place it 6cm above can0 along the world coordinate system ’s z-axis`</mark> 73 <mark>`constraint_l =planner. generate_constraints (obj_name=" some_articulated_object ", obj_id =0, action="target1", hand_name=" left") # Generate the constraints for the left hand end -effector to move to the target1 pose with the left hand pushing the object " some_articulated_object " to move along its articulation axis`</mark> 74 <mark>`constraint_r =planner. generate_constraints (obj_name=" some_articulated_object ", obj_id =0, action="target2", hand_name="`</mark> 

29 

<mark>`right") # Generate the constraints for the right hand end -effector to move to the target2 pose with the right hand pushing the object " some_articulated_object " to move along its articulation axis`</mark> 75 <mark>`constraint_l =planner. generate_constraints (obj_name=" some_articulated_object ", obj_id =0, action="grasp", hand_name="left" ) # Generate the constraints for the left hand end -effector to move to the pre -grasp pose for grasping the object " some_articulated_object "`</mark> 76 <mark>`constraint_l =planner. generate_constraints (obj_name=" some_articulated_object ", obj_id =0, action="grasp", hand_name="left" , openness =0.7) # Generate the constraints for the left end -effector pose after grasping the articulated_obj . This constraint is used for planning a motion to turn the " some_articulated_object " to an openness of 0.7.`</mark> 77 78 <mark>`def generate_end_effector_pose (constraints ,hand_name):`</mark> 79 <mark>`Function: Calculate the end -effector pose that satisfies the given constraints .`</mark> 80 <mark>`Return: _, target_effector_pose`</mark> 81 <mark>`Args:`</mark> 82 <mark>`- constraints (list , Mandatory)`</mark> 83 <mark>`- hand_name (str , Mandatory): "left" or "right"`</mark> 84 <mark>`Example:`</mark> 85 <mark>`_, target_effector_pose_l = planner. generate_end_effector_pose ( constraint_l ,hand_name="left")`</mark> 86 87 <mark>`def move_to_pose_with_screw (pose: sapien.Pose , hand_name , attach_obj =False , object_name=None , object_id =0):`</mark> 88 <mark>`Function: Control the robotic arm to move the end -effector of ’hand_name ’ to the ’pose ’.`</mark> 89 <mark>`Return: None`</mark> 90 <mark>`Args:`</mark> 91 <mark>`- pose (sapien.Pose or list , Mandatory): The target pose for the movement of ’ hand_name ’.`</mark> 92 <mark>`- hand_name (str , Mandatory): "all", "left" or "right".`</mark> 93 <mark>`- attach_obj (bool or list , Mandatory): Whether there is an attached object in the hand during the movement.`</mark> 94 <mark>`- object_name (str or list): [Required when ’attach_obj ’ is True] The type of the attached object.`</mark> 95 <mark>`- object_id (int or list , Mandatory): [Required when ’attach_obj ’ is True] The object id of the attached object.`</mark> 96 <mark>`Example:`</mark> 97 <mark>`# If ’hand_name ’ is ’all ’, ensure that other parameters are of list type , where index [0] and [1] correspond to the parameters for the left and right hands , respectively .`</mark> 98 <mark>`# you need to indicate the objects that are currently in hand (grasped or pinched) with args attach_obj , object_name , and object_id. If both hands are holding objects , set these args with list.`</mark> 99 <mark>`planner. move_to_pose_with_screw ( target_effector_pose ,"all",attach_obj =[ False ,False ])`</mark> 100 <mark>`planner. move_to_pose_with_screw (planner. right_hand_init_pose ,hand_name=" right") # The right hand returns to the initial pose.`</mark> 101 102 <mark>`======`</mark> 103 <mark>`Code example:`</mark> 104 <mark>`1. The right hand grasps the can. Initial conditions: Not yet performed any action`</mark> 105 106 <mark>`step 0: Set the right hand fingers to a pre -grasp pose`</mark> 107 <mark>`‘‘‘python`</mark> 108 <mark>`# Set the right hand fingers to a pre -grasp pose`</mark> 109 <mark>`planner. hand_pre_grasp ("right")`</mark> 110 <mark>`‘‘‘`</mark> 111 112 <mark>`step 1: Move the right hand to grasp pose`</mark> 113 <mark>`‘‘‘python`</mark> 114 <mark>`constraint_r =planner. generate_constraints (obj_name="can", obj_id =0, action=" grasp", hand_name="right")`</mark> 115 <mark>`# Generate the target pose for the end -effector and move the right hand to the target pose`</mark> 116 <mark>`_, target_effector_pose = planner. generate_end_effector_pose (constraint_r , hand_name="right")`</mark> 117 <mark>`planner. move_to_pose_with_screw (target_effector_pose ,"right",attach_obj =False)`</mark> 118 <mark>`‘‘‘`</mark> 119 120 <mark>`step 2: Close the right hand to grasp the can`</mark> 121 <mark>`‘‘‘python`</mark> 122 <mark>`# Close the right hand to grasp the can`</mark> 123 <mark>`planner.hand_grasp("right",grasp_object ="can",obj_id =0)`</mark> 

30 



<!-- Start of picture text -->
124 ‘‘‘<br>125<br>126 ======<br>127 Notes:<br>128 - All coordinate information , unless otherwise specified , is in the world<br>coordinate system.<br>129 - The robot ’s coordinate system aligns with the world frame: +X (front of robot),<br>+Y (left of robot), +Z (up of robot).<br>130 - ‘type_id ‘ represents different models of the same type of object , while ‘obj_id ‘<br>indicates the order in which objects of the same type are added.<br>131 - The object ’s bounding box (bbox) represents its dimensions in its own coordinate<br>system (axis -aligned when the orientation quaternion is q=[1 ,0 ,0 ,0]). For<br>example , a can with bbox :{"min": [ -0.08 , -0.08 , -0.02] ,"max": [0.08 ,0.08 ,0.02]}<br>has lengths of 0.16 units along X/Y-axes and 0.04 units along the Z-axis.<br>132 - Please place each step in a separate code block , enclosed within ‘‘‘python ‘‘‘<br>tags. The number of steps should correspond exactly to the number of ‘‘‘<br>python ‘‘‘ blocks in your response , with no extra or missing blocks.<br>133 - The parameters in the code block corresponding to each step are not shared.<br>Please do not carry over the parameters set in the previous step to the next<br>step.<br>134 - When selecting the hand to operate on an object , please choose the hand that is<br>closer to the object.<br>135 - Each line of code must have at least one level of indentation .<br>136 - - The left hand ’s operable range is x in [-0.42, -0.19], y in [-0.07, 0.36]; the<br>right hand ’s range is x in [-0.42, -0.19], y in [-0.36, 0.07]. Objects must<br>be placed within these intervals (note: meeting the range is a necessary but<br>not sufficient condition. Successful grasping may still fail due to object<br>orientation , collisions , or gripper constraints ).<br>137 ======<br>138 Please generate the code to execute ’TASK_DESCRIPTION ’.<br><!-- End of picture text -->

### **E.4 Sample Demonstration Code for Open Drawer Generated by HumanoidGen** 

1 <mark>`from humanoidgen . motion_planning .h1_2.solution.generated.solver_env import *`</mark> 2 <mark>`def step(planner: HumanoidMotionPlanner ):`</mark> 3 <mark>`# Step 1: Left hand grasps the drawer`</mark> 4 <mark>`planner. hand_pre_grasp ("left")`</mark> 5 <mark>`constraint_r = planner. generate_constraints (`</mark> 6 <mark>`obj_name="drawer",`</mark> 7 <mark>`obj_id =0,`</mark> 8 <mark>`action="grasp",`</mark> 9 <mark>`hand_name="left"`</mark> 10 <mark>`)`</mark> 11 <mark>`_, target_effector_pose = planner. generate_end_effector_pose (constraint_r , " left")`</mark> 12 <mark>`planner. move_to_pose_with_screw (`</mark> 13 <mark>`target_effector_pose ,`</mark> 14 <mark>`"left",`</mark> 15 <mark>`attach_obj=False`</mark> 16 <mark>`)`</mark> 17 <mark>`planner.hand_grasp("left", grasp_object ="drawer", obj_id =0)`</mark> 18 <mark>`# Step 2: Left hand opens the drawer to an openness of 1`</mark> 19 <mark>`constraint_open = planner. generate_constraints (`</mark> 20 <mark>`obj_name="drawer",`</mark> 21 <mark>`obj_id =0,`</mark> 22 <mark>`action="grasp",`</mark> 23 <mark>`hand_name="left",`</mark> 24 <mark>`openness =1`</mark> 25 <mark>`)`</mark> 26 <mark>`_, target_open_pose = planner. generate_end_effector_pose (constraint_open , " left")`</mark> 27 <mark>`planner. move_to_pose_with_screw (`</mark> 28 <mark>`target_open_pose ,`</mark> 29 <mark>`"left",`</mark> 30 <mark>`attach_obj=True ,`</mark> 31 <mark>`object_name ="drawer",`</mark> 32 <mark>`object_id =0`</mark> 33 <mark>`)`</mark> 34 <mark>`# Step 3: Left hand releases the drawer`</mark> 35 <mark>`planner.open_hand("left")`</mark> 

31 

### **E.5 Prompt Template for MCTS-integrated Demonstration Script Generation** 



<!-- Start of picture text -->
1 You are a professional assistant for generating code that enables dual -arm robots<br>to perform tabletop tasks. Please generate logically structured code to<br>execute the user -specified tasks based on the provided context.<br>2 ======<br>3 Static Scene Elements:<br>4 The static scene elements include a robot and a table. The robot ’s base_link (<br>position between torso_link and pelvis) has a pose of pose.p = [-0.85, 0, 0],<br>pose.q = [1, 0, 0, 0]. The table surface spans x in [-0.42, -0.19], y in<br>[-1.1, 1.16] , z = 0.<br>5 ======<br>6 World Coordinate System Information :<br>7 Since the robot ’s base coordinate frame has pose.q = [1, 0, 0, 0], its xyz<br>directions align with the world coordinate system: x points forward , y points<br>to the robot ’s left , and z points upward.<br>8 ======<br>9 Intrinsic Asset Attributes:<br>10 ASSETS_ATTRIBUTES<br>11 Note: The ’orientation ’ in ’status ’ represents the rotation in the world<br>coordinate system under its corresponding ’description ’.<br>12 ======<br>13 Initial Asset State:<br>14 INITIAL_ASSET_STATE<br>15 Note: The asset(object) state(pose) when the scene is just initialized , before any<br>actions are executed. Pose consists of Cartesian coordinates and a<br>quaternion in the world coordinate system: [x, y, z, w, x, y, z]( The<br>following 7- dimensional poses all follow this format).<br>16 ======<br>17 Current Asset State:<br>18 CURRENT_ASSET_STATE<br>19 Note: Current states(poses) of assets(objects) on the tabletop<br>20 ======<br>21 Executed Action Code:<br>22 EXECUTED_CODE<br>23 Note:<br>24 - Code for actions executed by the robot to transform the asset state on the<br>tabletop from the initial state to the current state.<br>25 ======<br>26 Prohibited Next Actions:<br>27 PROHIBITED_ACTION<br>28 Note: The next step cannot execute the prohibited actions listed above. ’Same ’<br>means completely identical. For ’move ’, any addition , removal , or<br>modification of constraints is considered a different action. Applies only to<br>the next step; subsequent steps can still choose those actions.<br>29 ======<br>30 Robot Attributes:<br>31 hand_key_point :{<br>32 "left_hand ":[" base_left_hand "," grasp_point_base_left_hand ","<br>pinch_point_base_left_hand "],<br>33 "right_hand ":[" base_right_hand "," grasp_point_base_right_hand ","<br>pinch_point_base_right_hand "]<br>34 }<br>35 hand_key_axis :{<br>36 "left_hand ":[" left_pinch_axis "," left_pinch_wrist_2_palm_axis ","<br>left_ring_2_index "," left_grasp_axis "," left_grasp_wrist_2_palm_axis "],<br>37 "right_hand ":[" right_pinch_axis "," right_pinch_wrist_2_palm_axis ","<br>right_ring_2_index "," right_grasp_axis "," right_grasp_wrist_2_palm_axis "]<br>38 }<br>39 default_pose :{<br>40 "left_hand ":[ left_hand_init_pose ],<br>41 "right_hand ":[ right_hand_init_pose ]<br>42 }<br>43 ======<br>44 Available Class:<br>45 Constraint(env ,type ,end_effector_frame ,hand_key_point ,object_key_point ,hand_axis ,<br>object_axis):<br>46 Function:<br>47 "Constraint" defines hard constraints that must be strictly satisfied.<br>48 Establishes spatial equivalence constraints between:<br>49 - ( point2point) Specified end -effector point to target point.<br>50 - (parallel) Specified end -effector axis direction to target axis<br>direction.<br>51 Args:<br>52 - env (Environment , Mandatory): The planner ’s bound operating environment .<br>Must reference the planner ’s environment instance through ‘planner.env ‘<br>property.<br><!-- End of picture text -->

32 

53 <mark>`- type (str , Mandatory): " point2point " or "parallel ".`</mark> 54 <mark>`- end_effector_frame (str , Mandatory): " l_hand_base_link " or " r_hand_base_link ".`</mark> 55 <mark>`- hand_key_point (np.ndarray): [Required when ’type ’ is ’point2point ’] Pre - motion end -effector anchor point in world coordinates .`</mark> 56 <mark>`- object_key_point (np.ndarray): [Required when ’type ’ is ’point2point ’] Target ’s corresponding point in world coordinates .`</mark> 57 <mark>`- hand_axis (np.ndarray): [Required when ’type ’ is ’parallel ’] Pre -motion end - effector alignment axis in world coordinates .`</mark> 58 <mark>`- object_axis (np.ndarray): [Required when ’type ’ is ’parallel ’] Target ’s reference axis in world coordinates .`</mark> 59 <mark>`Example:`</mark> 60 <mark>`# Right palm facing down to grasp(Top -down grasping of the object)`</mark> 61 <mark>`Constraint(`</mark> 62 <mark>`env=planner.env ,`</mark> 63 <mark>`type =" parallel",`</mark> 64 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 65 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name =" right_grasp_axis "), # The back of the palm points toward the front of the palm. Pinch action is similar.`</mark> 66 <mark>`object_axis=np.array ([0 ,0 , -1]), # World frame ,`</mark> 67 <mark>`)`</mark> 68 69 <mark>`# Right palm facing up to grasp(Down -Top grasping of the object). If there is a table or other objects below the target , it often causes collisions and makes it unreachable .`</mark> 70 <mark>`Constraint(`</mark> 71 <mark>`env=planner.env ,`</mark> 72 <mark>`type =" parallel",`</mark> 73 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 74 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name =" right_grasp_axis "), # The back of the palm points toward the front of the palm. Pinch action is similar.`</mark> 75 <mark>`object_axis=np.array ([0 ,0 ,1]) , # World frame ,`</mark> 76 <mark>`)`</mark> 77 78 <mark>`# The direction from the right wrist to the palm center is facing forward.`</mark> 79 <mark>`Constraint(`</mark> 80 <mark>`env=planner.env ,`</mark> 81 <mark>`type =" parallel",`</mark> 82 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 83 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name =" right_grasp_wrist_2_palm_axis "), # The direction from the wrist to the palm center`</mark> 84 <mark>`object_axis=np.array ([1 ,0 ,0]) , # World frame`</mark> 85 <mark>`)`</mark> 86 87 <mark>`# The direction from the right pinky finger to the index finger is parallel to the x-axis of object0.`</mark> 88 <mark>`Constraint(`</mark> 89 <mark>`env=planner.env ,`</mark> 90 <mark>`type =" parallel",`</mark> 91 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 92 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name =" right_ring_2_index "), # The direction from the right pinky finger to the index finger`</mark> 93 <mark>`object_axis= get_axis_in_env (planner.env , "x", obj_type =" object", obj_id =0), # The coordinates of object0 ’s x-axis in the world coordinate system.`</mark> 94 <mark>`)`</mark> 95 96 <mark>`# After object0 is in hand , align its x-axis parallel to the world coordinate system ’s z-axis , making its x-axis point upward.`</mark> 97 <mark>`Constraint(`</mark> 98 <mark>`env=planner.env ,`</mark> 99 <mark>`type="point2point ",`</mark> 100 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 101 <mark>`hand_key_point = get_axis_in_env (planner.env , "x", obj_type="object", obj_id =0),`</mark> 102 <mark>`object_key_point =object_axis =np.array ([0 ,0 ,1]) , # np.array ([0, 0.1, 0.1]) in the object0 ’s coordinate system.`</mark> 103 <mark>`)`</mark> 104 105 <mark>`# The right -hand grasp point coincides with [0, 0.1, 0.1] in the object0 ’s coordinate system.`</mark> 106 <mark>`Constraint(`</mark> 107 <mark>`env=planner.env ,`</mark> 108 <mark>`type="point2point ",`</mark> 109 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 

33 

110 <mark>`hand_key_point = get_point_in_env (planner.env , point_name=" grasp_point_base_right_hand "),`</mark> 111 <mark>`object_key_point = get_point_in_env (planner.env ,type_name="object", obj_id =0, related_point =np.array ([0, 0.1, 0.1])), # np.array ([0, 0.1, 0.1]) in the object0 ’s coordinate system.`</mark> 112 <mark>`)`</mark> 113 114 <mark>`# After object0 is in hand , position it 0.1m above object1.`</mark> 115 <mark>`Constraint(`</mark> 116 <mark>`env=planner.env ,`</mark> 117 <mark>`type="point2point ",`</mark> 118 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 119 <mark>`hand_key_point = get_point_in_env (planner.env ,type_name="object",obj_id =0) ,`</mark> 120 <mark>`object_key_point = get_point_in_env (planner.env ,type_name="object", obj_id =1)+np.array ([0, 0, 0.1]) , # np.array ([0, 0, 0.1]) in the world(robot) coordinate system.`</mark> 121 <mark>`)`</mark> 122 <mark>`Note:`</mark> 123 <mark>`’hand_key_point ’ and ’object_key_point ’ represent two points in the world coordinate system. ’hand_key_point ’ moves with the corresponding end - effector , and type=’point2point ’ indicates the intention for the two points to coincide.`</mark> 124 <mark>`’hand_axis ’ and ’object_axis ’ have similar meanings to ’point ’.`</mark> 125 <mark>`’right_grasp_axis ’ or ’right_pinch_axis ’ parallel [0,0,-1] means executing with the palm facing downward.`</mark> 126 <mark>`’right_grasp_axis ’ or ’right_pinch_axis ’ parallel [1,0,0] means executing with the palm facing forward.`</mark> 127 <mark>`’right_grasp_axis ’ or ’right_pinch_axis ’ parallel [0,1,0] means executing with the palm facing left.`</mark> 128 <mark>`’left_grasp_axis ’ or ’left_pinch_axis ’ parallel [0,-1,0] means executing with the palm facing right.`</mark> 129 130 131 <mark>`Const(env ,type ,end_effector_frame ,hand_key_point ,object_key_point ,hand_axis , object_axis):`</mark> 132 <mark>`The usage is similar to the Constraint class , but it is not a strict constraint; it is an optimization objective.`</mark> 133 <mark>`======`</mark> 134 <mark>`Available functions:`</mark> 135 136 <mark>`def get_point_in_env (env , point_name ,type_name , obj_id ,related_point ,openness):`</mark> 137 <mark>`Function: Get specified point position in world frame.`</mark> 138 <mark>`Return: point_position (np.ndarray)`</mark> 139 <mark>`Args:`</mark> 140 <mark>`- env (Environment , Mandatory): The planner ’s bound operating environment . Must reference the planner ’s environment instance through ‘planner.env ‘ property.`</mark> 141 <mark>`- point_name (str , optional): The point name. Example: " grasp_point_base_left_hand ".`</mark> 142 <mark>`- type_name (str , optional): The reference object relative to the target point .`</mark> 143 <mark>`- obj_id (int , optional): The reference object id.`</mark> 144 <mark>`- related_point (np.ndarray , optional): The coordinates of the target point relative to the object center in the object coordinate system. Default: np.array ([0 ,0 ,0])`</mark> 145 <mark>`- openness (int , optional): Represents the openness degree of the articulated object. If type_name is an articulated object , this value can be set to obtain the coordinates corresponding to point_name at a specific openness degree.`</mark> 146 <mark>`Example:`</mark> 147 <mark>`# Get the current coordinates of the right -hand pinch point in the world coordinate system.`</mark> 148 <mark>`get_point_in_env (planner.env , point_name =" grasp_point_base_pinch_hand ")`</mark> 149 150 <mark>`def get_axis_in_env (env , axis_name , obj_type , obj_id):`</mark> 151 <mark>`Function: Get specified direction vector in world frame.`</mark> 152 <mark>`Return: direction_vector (np.ndarray)`</mark> 153 <mark>`Args:`</mark> 154 <mark>`- env (Environment , Mandatory): The planner ’s bound operating environment . Must reference the planner ’s environment instance through ‘planner.env ‘ property.`</mark> 155 <mark>`- axis_name (str , Mandatory): The axis name. Example: " right_pinch_axis ".`</mark> 156 <mark>`- obj_type (str , optional): The reference object relative to the target axis.`</mark> 157 <mark>`- obj_id (int , optional): The reference object ID.`</mark> 158 159 <mark>`def open_hand(self , hand_name):`</mark> 160 <mark>`Function: Control the hand to open.`</mark> 

34 



<!-- Start of picture text -->
161 Return: None<br>162 Args:<br>163 - hand_name (str , Mandatory): "all", "right", or "left".<br>164<br>165 def hand_pre_grasp (hand_name):<br>166 Function: Adjusts the thumb movement of the specified hand to position it<br>opposite the index finger , preparing for subsequent grasping operations.<br>This should typically be called before executing ’move_to_pose_with_screw<br>’ to reach the pre -grasp pose.<br>167 Return: None<br>168 Args:<br>169 - hand_name (str , Mandatory): "all", "right", or "left". Default: "all".<br>170<br>171 def hand_grasp(hand_name , grasp_object , obj_id):<br>172 Function: Control the hand to close.<br>173 Return: None<br>174 Args:<br>175 - hand_name (str , Mandatory): "right", or "left".<br>176 - grasp_object (str , Mandatory): The type of the grasped object. Example: "can<br>".<br>177 - obj_id (int , Mandatory): The object ID of the grasped object. Example: If<br>grasp_object ="can" and obj_id =0, it indicates the first can object added<br>to the environment .<br>178<br>179 def hand_pre_pinch (hand_name):<br>180 Function: Adjusts the thumb movement of the specified hand to position it<br>opposite the index finger , preparing for subsequent pinching operations.<br>This should typically be called before executing ’move_to_pose_with_screw<br>’ to reach the pre -pinch pose.<br>181 Return: None<br>182 Args:<br>183 - hand_name (str , optional): "all", "right", or "left". Default: "all".<br>184<br>185 def hand_pinch(hand_name , pinch_object , obj_id):<br>186 Function: Only control the closing operation of the thumb and index finger.<br>Typically used for small and hard -to -grasp objects.<br>187 Return: None<br>188 Args:<br>189 - hand_name (str , Mandatory): "right", or "left".<br>190 - pinch_object (str , Mandatory): The type of the pinched object. Example: "can<br>".<br>191 - obj_id (int , Mandatory): The object ID of the pinched object. Example: If<br>pinch_object ="can" and obj_id =0, it indicates the first can object added<br>to the environment .<br>192<br>193 def generate_end_effector_pose (constraints ,hand_name):<br>194 Function: Calculate the target pose that the robotic arm needs to move to in<br>this step based on the constraint and cost.<br>195 Return: _, target_effector_pose<br>196 Args:<br>197 - constraints (list , Mandatory): A list of Constraint objects , with the number<br>of Constraints determined by specific requirements .<br>198 - hand_name (str , Mandatory): "left" or "right"<br>199<br>200 def move_to_pose_with_screw (pose: sapien.Pose , hand_name , attach_obj =False ,<br>object_name=None , object_id =0):<br>201 Function: Control the robotic arm to move the end -effector of ’hand_name ’ to<br>the ’pose ’.<br>202 Return: None<br>203 Args:<br>204 - pose (sapien.Pose , Mandatory): The target pose for the movement of ’<br>hand_name ’.<br>205 - hand_name (str , Mandatory): The specified robotic arm for the movement.<br>206 - attach_obj (bool , Mandatory): Whether there is an attached object in the<br>hand during the movement.<br>207 - object_name (str): [Required when ’attach_obj ’ is True] The type of the<br>attached object.<br>208 - obj_id (int , Mandatory): [Required when ’attach_obj ’ is True] The object id<br>of the attached object.<br>209<br>210 ======<br>211 Incorrect example code:<br>212 1. The right hand grasps the can when cthe an is on the table:<br>213 step 1: Grasp can0<br>214 ‘‘‘python<br>215 # Set the right -hand fingers to a pre -grasp pose<br>216 planner. hand_pre_grasp ("right")<br>217<br><!-- End of picture text -->

35 

218 <mark>`constraints =[]`</mark> 219 220 <mark>`constraints .append(`</mark> 221 <mark>`Constraint(`</mark> 222 <mark>`env=planner.env ,`</mark> 223 <mark>`type="parallel",`</mark> 224 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 225 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" right_grasp_axis "),`</mark> 226 <mark>`object_axis=np.array ([0, 0, 1])`</mark> 227 <mark>`)`</mark> 228 <mark>`)`</mark> 229 <mark>`# Generate the target pose for the end -effector and move the right hand to the target pose`</mark> 230 <mark>`_, target_effector_pose = planner. generate_end_effector_pose (constraints , hand_name="right")`</mark> 231 <mark>`planner. move_to_pose_with_screw (target_effector_pose ,"right",attach_obj =False)`</mark> 232 233 <mark>`# Close the right hand to grasp the can`</mark> 234 <mark>`planner.hand_grasp("right",grasp_object ="can",obj_id =0)`</mark> 235 <mark>`‘‘‘`</mark> 236 <mark>`Reason for the error: ‘object_axis =np.array ([0, 0, 1]) ‘ represents the positive z- axis in the world coordinate system. If it is parallel to the grasp axis , it indicates a bottom -up grasping direction. For an object on a table , the hand cannot reach below the object. To perform a top -down grasp along the -z direction , use ‘object_axis =np.array ([0, 0, -1]) ‘.`</mark> 237 238 <mark>`======`</mark> 239 <mark>`Correct example code:`</mark> 240 <mark>`1. The right hand grasps the can from right to left , then lifts it by 0.1m, and then releases it.`</mark> 241 <mark>`step 1: Grasp can0`</mark> 242 <mark>`‘‘‘python`</mark> 243 <mark>`# Set the right -hand fingers to a pre -grasp pose`</mark> 244 <mark>`planner. hand_pre_grasp ("right")`</mark> 245 246 <mark>`constraints =[]`</mark> 247 <mark>`# Add a point -to -point constraint to align the grasp point of the right hand with the can ’s center point`</mark> 248 <mark>`constraints .append(`</mark> 249 <mark>`Constraint(`</mark> 250 <mark>`env=planner.env ,`</mark> 251 <mark>`type="point2point ",`</mark> 252 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 253 <mark>`hand_key_point = get_point_in_env (planner.env , point_name=" grasp_point_base_right_hand "), # Grasp point on the right hand`</mark> 254 <mark>`object_key_point = get_point_in_env (planner.env ,type_name="can",obj_id =0) , # Center point of the can`</mark> 255 <mark>`)`</mark> 256 <mark>`)`</mark> 257 <mark>`# Add a Constraint to align the pinky -to -index axis of the right hand with the world z-axis`</mark> 258 <mark>`constraints .append(`</mark> 259 <mark>`Constraint(`</mark> 260 <mark>`env=planner.env ,`</mark> 261 <mark>`type="parallel",`</mark> 262 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 263 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name=" right_ring_2_index "), # The direction from the pinky finger to the index finger`</mark> 264 <mark>`object_axis=np.array ([0 ,0 ,1]) , # World frame. Or the specific axis of the object , such as ‘get_axis_in_env (planner.env , axis_name ="z", obj_type =" can", obj_id =0) ‘.`</mark> 265 <mark>`)`</mark> 266 <mark>`)`</mark> 267 <mark>`# Generate the target pose for the end -effector and move the right hand to the target pose`</mark> 268 <mark>`_, target_effector_pose = planner. generate_end_effector_pose (constraints , hand_name="right")`</mark> 269 <mark>`planner. move_to_pose_with_screw (target_effector_pose ,"right",attach_obj =False)`</mark> 270 271 <mark>`# Close the right hand to grasp the can`</mark> 272 <mark>`planner.hand_grasp("right",grasp_object ="can",obj_id =0)`</mark> 273 <mark>`‘‘‘`</mark> 274 <mark>`step 2: Lift the can by 0.1m while keeping its pose unchanged`</mark> 275 <mark>`‘‘‘python`</mark> 276 <mark>`constraints =[]`</mark> 277 <mark>`# Add a point -to -point constraint to lift the can by 0.1m`</mark> 278 <mark>`constraints .append(`</mark> 279 <mark>`Constraint(`</mark> 

36 

280 <mark>`env=planner.env ,`</mark> 281 <mark>`type="point2point ",`</mark> 282 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 283 <mark>`hand_key_point = get_point_in_env (planner.env ,type_name="can",obj_id =0) , # can center point now`</mark> 284 <mark>`object_key_point = get_point_in_env (planner.env ,type_name="can",obj_id =0)+np.array ([0 ,0 ,0.1]) , # can center point after being lifted by 0.1m`</mark> 285 <mark>`)`</mark> 286 <mark>`)`</mark> 287 <mark>`# Add a parallel constraint to keep the x-axis of the can unchanged`</mark> 288 <mark>`constraints .append(`</mark> 289 <mark>`Constraint(`</mark> 290 <mark>`env=planner.env ,`</mark> 291 <mark>`type="parallel",`</mark> 292 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 293 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name="x",obj_type="can", obj_id =0), # The x-axis of the can`</mark> 294 <mark>`object_axis= get_axis_in_env (planner.env ,axis_name="x",obj_type="can", obj_id =0), # Keep the x-axis unchanged`</mark> 295 <mark>`)`</mark> 296 <mark>`)`</mark> 297 <mark>`# Add a parallel constraint to keep the y-axis of the can unchanged`</mark> 298 <mark>`constraints .append(`</mark> 299 <mark>`Constraint(`</mark> 300 <mark>`env=planner.env ,`</mark> 301 <mark>`type="parallel",`</mark> 302 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 303 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name="y",obj_type="can", obj_id =0), # The y-axis of the can`</mark> 304 <mark>`object_axis= get_axis_in_env (planner.env ,axis_name="y",obj_type="can", obj_id =0), # Keep the y-axis unchanged`</mark> 305 <mark>`)`</mark> 306 <mark>`)`</mark> 307 <mark>`# Generate the target pose for the end -effector and move the right hand to the target pose`</mark> 308 <mark>`_, target_effector_pose = planner. generate_end_effector_pose (constraints , hand_name="right")`</mark> 309 <mark>`planner. move_to_pose_with_screw (target_effector_pose ,"right",attach_obj =True , object_name ="can",object_id =0)`</mark> 310 311 <mark>`# Open the right hand to release the can`</mark> 312 <mark>`planner.open_hand("right")`</mark> 313 <mark>`‘‘‘`</mark> 314 <mark>`step3: Move the right hand back to its initial pose`</mark> 315 <mark>`‘‘‘python`</mark> 316 <mark>`# Move the right hand back to its initial pose`</mark> 317 <mark>`planner. move_to_pose_with_screw (planner.right_hand_init_pose , "right", attach_obj=False)`</mark> 318 <mark>`‘‘‘`</mark> 319 320 <mark>`2. Based on step 1 of Example 1, place the can into the bowl after grasping it.`</mark> 321 322 <mark>`step 2: Move the can above the bowl and ensure the palm is facing downward.`</mark> 323 <mark>`‘‘‘python`</mark> 324 <mark>`constraints =[]`</mark> 325 <mark>`# Add a point -to -point constraint to lift the can by 0.1m`</mark> 326 <mark>`constraints .append(`</mark> 327 <mark>`Constraint(`</mark> 328 <mark>`env=planner.env ,`</mark> 329 <mark>`type="point2point ",`</mark> 330 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 331 <mark>`hand_key_point = get_point_in_env (planner.env ,type_name="can",obj_id =0) , # can center point now`</mark> 332 <mark>`object_key_point = get_point_in_env (planner.env ,type_name="bowl",obj_id =0)+np.array ([0 ,0 ,0.1]) , # can center point over the bowl`</mark> 333 <mark>`)`</mark> 334 <mark>`)`</mark> 335 <mark>`# Palm facing down`</mark> 336 <mark>`constraints .append(`</mark> 337 <mark>`Constraint(`</mark> 338 <mark>`env=planner.env ,`</mark> 339 <mark>`type="parallel",`</mark> 340 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 341 <mark>`hand_axis= get_axis_in_env (planner.env ,axis_name=" right_grasp_axis "), # The back of the palm points toward the front of the palm.`</mark> 342 <mark>`object_axis=np.array ([0 ,0 , -1]), # World frame ,`</mark> 343 <mark>`)`</mark> 

37 



<!-- Start of picture text -->
344 )<br>345<br>346 # Generate the target pose for the end -effector and move the right hand to the<br>target pose<br>347 _, target_effector_pose = planner. generate_end_effector_pose (constraints ,<br>hand_name="right")<br>348 planner. move_to_pose_with_screw (target_effector_pose ,"right",attach_obj =True ,<br>object_name ="can",object_id =0)<br>349<br>350 # Open the right hand to release the can<br>351 planner.open_hand("right")<br>352 ‘‘‘<br>353 step3: Move the right hand back to its initial pose<br>354 ‘‘‘python<br>355 # Move the right hand back to its initial pose<br>356 planner. move_to_pose_with_screw (planner.right_hand_init_pose , "right",<br>attach_obj=False)<br>357 ‘‘‘<br>358<br>359 ======<br>360 Notes:<br>361 - ‘type_id ‘ represents different models of the same type of object , while ‘obj_id ‘<br>indicates the order in which objects of the same type are added.<br>362 - The left hand ’s operable range is x in [-0.42, -0.19], y in [-0.07, 0.36]; the<br>right hand ’s range is x in [-0.42, -0.19], y in [-0.36, 0.07]. It must be<br>ensured that the hand moves within this range. For actions such as grasping ,<br>pinching , or placing an object , it must be ensured that they are all within<br>the operational range of the corresponding hand.<br>363 - The object ’s bounding box (bbox) represents its dimensions in its own coordinate<br>system (axis -aligned when the orientation quaternion is q =[1 ,0 ,0 ,0]). For<br>example , a can with bbox: {" min ": [ -0.08 , -0.08 , -0.02] , "max ":<br>[0.08 ,0.08 ,0.02]} has lengths of 0.16 units along X/Y-axes and 0.04 units<br>along the Z-axis.<br>364 - Please place each step in a separate code block , enclosed within ‘‘‘python ‘‘‘<br>tags. The number of steps should correspond exactly to the number of ‘‘‘<br>python ‘‘‘ blocks in your response , with no extra or missing blocks.<br>365 - Variables in different code blocks are not shared , meaning variables from<br>previous code blocks cannot be used in subsequent ones.<br>366 - When placing an object , release it slightly above the target position.<br>367 - To avoid collisions , consider splitting a move action into multiple moves. For<br>example , when placing a can into a bowl , first move the can to a height above<br>the bowl , then lower it to just above the bowl before releasing it. However ,<br>ensure the height is neither too high nor too low to avoid inverse<br>kinematics issues or collisions . Typically , an additional height of 0.03 cm<br>is added.<br>368 - When planning , please take collision issues into account. For example , if the<br>height of an object relative to the table is z=0.03 <0.08 , do not use the<br>right hand to grasp from right to left , as it will cause a collision between<br>the hand and the table. Similarly , when placing the object somewhere , it is<br>acceptable to release it slightly above the target position.<br>369 - If ’Executed Action Code ’ is empty , it means no code has been executed. If not<br>empty , generate only the subsequent actions to be executed.<br>370 - If ’Prohibited Next Actions ’ is empty , there are no restrictions on the next<br>action. If not empty , avoid executing any action identical to the listed ones<br>in the first subsequent step.<br>371 - When performing operations such as moving an object to a specific location for<br>placement , various factors should be fully considered . For example , when<br>placing an object on a table , it is acceptable to suspend it slightly above<br>the table.<br>372 - Before executing grasp or pinch actions , pre -grasp and pre -pinch actions must be<br>performed , respectively . Before executing another grasp or pinch action , the<br>corresponding pre -action must be performed again.<br>373 - When calling ‘Constraint ‘, parameter names must be explicitly specified using<br>the ‘name=value ‘ format.<br>374 - Each line of code must have at least one level of indentation .<br>375 - " right_hand_init_pose " and " left_hand_init_pose " are non -collision poses , which<br>can avoid collisions with other hands or objects.<br>376 ======<br>377 Please generate the code to continue executing the task ’TASK_DESCRIPTION ’.<br>378 TASK_NOTE<br><!-- End of picture text -->

38 

### **E.6 Sample Demonstration Code for Block Stack Hard Generated by Applying MCTS** 

1 <mark>`from humanoidgen . motion_planning .h1_2.solution.generated.solver_env import *`</mark> 2 <mark>`def step(planner: HumanoidMotionPlanner ):`</mark> 3 4 <mark>`# Step 1: Right hand picks cube1 and places it at the stacking base position`</mark> 5 <mark>`planner. hand_pre_pinch ("right")`</mark> 6 7 <mark>`constraints = [`</mark> 8 <mark>`Constraint(`</mark> 9 <mark>`env=planner.env ,`</mark> 10 <mark>`type="point2point ",`</mark> 11 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 12 <mark>`hand_key_point = get_point_in_env (planner.env , point_name =" pinch_point_base_right_hand "),`</mark> 13 <mark>`object_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =1)`</mark> 14 <mark>`),`</mark> 15 <mark>`Constraint(`</mark> 16 <mark>`env=planner.env ,`</mark> 17 <mark>`type="parallel",`</mark> 18 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 19 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" right_pinch_axis "),`</mark> 20 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 21 <mark>`)`</mark> 22 <mark>`]`</mark> 23 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "right")`</mark> 24 <mark>`planner. move_to_pose_with_screw (target_pose , "right", attach_obj =False)`</mark> 25 26 <mark>`planner.hand_pinch("right", pinch_object ="cube", obj_id =1)`</mark> 27 28 <mark>`constraints = [`</mark> 29 <mark>`Constraint(`</mark> 30 <mark>`env=planner.env ,`</mark> 31 <mark>`type="point2point ",`</mark> 32 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 33 <mark>`hand_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =1) ,`</mark> 34 <mark>`object_key_point =np.array ([-0.3, 0.0, 0.05])`</mark> 35 <mark>`),`</mark> 36 <mark>`Constraint(`</mark> 37 <mark>`env=planner.env ,`</mark> 38 <mark>`type="parallel",`</mark> 39 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 40 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" right_pinch_axis "),`</mark> 41 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 42 <mark>`)`</mark> 43 <mark>`]`</mark> 44 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "right")`</mark> 45 <mark>`planner. move_to_pose_with_screw (target_pose , "right", attach_obj =True , object_name ="cube", object_id =1)`</mark> 46 47 <mark>`planner.open_hand("right")`</mark> 48 49 <mark>`planner. move_to_pose_with_screw (planner.right_hand_init_pose , "right", attach_obj=False)`</mark> 50 51 <mark>`# Step 2: Left hand picks cube0 and stacks it on cube1`</mark> 52 <mark>`planner. hand_pre_pinch ("left")`</mark> 53 54 <mark>`constraints = [`</mark> 55 <mark>`Constraint(`</mark> 56 <mark>`env=planner.env ,`</mark> 57 <mark>`type="point2point ",`</mark> 58 <mark>`end_effector_frame =" l_hand_base_link ",`</mark> 59 <mark>`hand_key_point = get_point_in_env (planner.env , point_name =" pinch_point_base_left_hand "),`</mark> 60 <mark>`object_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =0)`</mark> 61 <mark>`),`</mark> 62 <mark>`Constraint(`</mark> 63 <mark>`env=planner.env ,`</mark> 64 <mark>`type="parallel",`</mark> 65 <mark>`end_effector_frame =" l_hand_base_link ",`</mark> 66 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" left_pinch_axis "),`</mark> 67 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 68 <mark>`)`</mark> 

39 

69 <mark>`]`</mark> 70 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "left")`</mark> 71 <mark>`planner. move_to_pose_with_screw (target_pose , "left", attach_obj =False)`</mark> 72 73 <mark>`planner.hand_pinch("left", pinch_object ="cube", obj_id =0)`</mark> 74 75 <mark>`constraints = [`</mark> 76 <mark>`Constraint(`</mark> 77 <mark>`env=planner.env ,`</mark> 78 <mark>`type="point2point ",`</mark> 79 <mark>`end_effector_frame =" l_hand_base_link ",`</mark> 80 <mark>`hand_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =0) ,`</mark> 81 <mark>`object_key_point =np.array ([-0.3, 0.0, 0.09])`</mark> 82 <mark>`),`</mark> 83 <mark>`Constraint(`</mark> 84 <mark>`env=planner.env ,`</mark> 85 <mark>`type="parallel",`</mark> 86 <mark>`end_effector_frame =" l_hand_base_link ",`</mark> 87 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" left_pinch_axis "),`</mark> 88 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 89 <mark>`)`</mark> 90 <mark>`]`</mark> 91 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "left")`</mark> 92 <mark>`planner. move_to_pose_with_screw (target_pose , "left", attach_obj =True , object_name ="cube", object_id =0)`</mark> 93 94 <mark>`planner.open_hand("left")`</mark> 95 96 <mark>`planner. move_to_pose_with_screw (planner.left_hand_init_pose , "left", attach_obj=False)`</mark> 97 98 <mark>`# Step 3: Right hand picks cube2 and completes the stack`</mark> 99 <mark>`planner. hand_pre_pinch ("right")`</mark> 100 101 <mark>`constraints = [`</mark> 102 <mark>`Constraint(`</mark> 103 <mark>`env=planner.env ,`</mark> 104 <mark>`type="point2point ",`</mark> 105 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 106 <mark>`hand_key_point = get_point_in_env (planner.env , point_name =" pinch_point_base_right_hand "),`</mark> 107 <mark>`object_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =2)`</mark> 108 <mark>`),`</mark> 109 <mark>`Constraint(`</mark> 110 <mark>`env=planner.env ,`</mark> 111 <mark>`type="parallel",`</mark> 112 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 113 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" right_pinch_axis "),`</mark> 114 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 115 <mark>`)`</mark> 116 <mark>`]`</mark> 117 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "right")`</mark> 118 <mark>`planner. move_to_pose_with_screw (target_pose , "right", attach_obj =False)`</mark> 119 <mark>`planner.hand_pinch("right", pinch_object ="cube", obj_id =2)`</mark> 120 121 <mark>`constraints = [`</mark> 122 <mark>`Constraint(`</mark> 123 <mark>`env=planner.env ,`</mark> 124 <mark>`type="point2point ",`</mark> 125 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 126 <mark>`hand_key_point = get_point_in_env (planner.env , type_name="cube", obj_id =2) ,`</mark> 127 <mark>`object_key_point =np.array ([-0.3, 0.0, 0.13])`</mark> 128 <mark>`),`</mark> 129 <mark>`Constraint(`</mark> 130 <mark>`env=planner.env ,`</mark> 131 <mark>`type="parallel",`</mark> 132 <mark>`end_effector_frame =" r_hand_base_link ",`</mark> 133 <mark>`hand_axis= get_axis_in_env (planner.env , axis_name=" right_pinch_axis "),`</mark> 134 <mark>`object_axis=np.array ([0, 0, -1])`</mark> 135 <mark>`)`</mark> 136 <mark>`]`</mark> 137 <mark>`_, target_pose = planner. generate_end_effector_pose (constraints , "right")`</mark> 138 <mark>`planner. move_to_pose_with_screw (target_pose , "right", attach_obj =True , object_name ="cube", object_id =2)`</mark> 139 <mark>`planner.open_hand("right")`</mark> 

40 

## **F Broader Impacts** 

This work advances the field of robotic manipulation by enabling automated task creation and demonstration collection for bimanual dexterous systems, which can significantly reduce the cost and complexity of data acquisition in humanoid robotics. Traditional methods often rely on manual demonstration design, expert supervision, or extensive environment resets—processes that are time-consuming, labor-intensive, and difficult to scale. By contrast, our framework automates these processes through an LLM-driven planning framework that generates semantically meaningful and physically feasible tasks without human intervention. This not only simplifies the pipeline from task specification to execution but also ensures consistency and diversity in the collected demonstrations. 

The proposed framework has the potential to accelerate research on autonomous humanoid agents, particularly in domains such as assistive robotics, disaster response, and intelligent automation, where bimanual coordination and fine-grained hand manipulation are critical. For instance, in assistive robotics, precise bimanual operations, such as opening a pill bottle or pouring liquid from one container to another, require both high-level task reasoning and low-level motion control. Similarly, in disaster response scenarios, robots may need to manipulate tools, open doors, or handle irregularly shaped objects in constrained environments. These tasks demand robust and adaptive manipulation capabilities that go beyond simple pick-and-place actions. Our framework enables the generation of such complex interaction sequences, allowing researchers to train and evaluate policies on long-horizon, multi-step tasks at ease. 

41 

