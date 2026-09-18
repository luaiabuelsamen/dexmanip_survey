## **OAKINK2 : A Dataset of Bimanual Hands-Object Manipulation in Complex Task Completion** 

Xinyu Zhan<sup>1</sup><sup>_⋆_</sup> Lixin Yang<sup>1</sup><sup>_⋆_</sup> Yifei Zhao<sup>1</sup> Kangrui Mao<sup>1</sup> Hanlin Xu<sup>1</sup> Zenan Lin<sup>2,</sup><sup>_‡_</sup> Kailin Li<sup>1</sup> Cewu Lu<sup>1</sup><sup>**_†_**</sup> 

1Shanghai Jiao Tong University, 2South China University of Technology 



<!-- Start of picture text -->
������������������� ������������ ���������������<br>�������<br>�������<br>������<br>�����<br>���������<br>L0 L1 L2 L3 L9<br>��������������������������������������������� Use the knife to  cut  the apple; ����������������<br>����������������������������������������� then use the clamp to grip  the sugar cubes into the bowl; OPEN CLOSE<br>������������������������������������������ afterwards, use the microwave oven t o heat  the bowl. <heat, sth><br>������ ������������������������������������������������<br>����������������������������������������������� � OPEN CLOSE OPEN CLOSE<br>����� ���������������� ��������� ���� �������<br>�������������<br>�������������������������������<br>������������������������<br>��������������<br>���� �����<br>�������������������������������������<br>���������������������������������<br>����������������������� �������� ������������� ����� �����������<br>������������ �����������������������<br>Level1 Level2 Level3<br>��������� �������������� ������������<br><!-- End of picture text -->

Figure 1. **An overview of the data and content of our proposed OAKINK2 dataset.** OAKINK2 dataset focuses on bimanual object manipulation tasks for complex daily activities. **1) The top row shows the data collection process** , including the task setup (top-left panel), human demonstration (top-center), and annotation (top-right). **2) The second row shows the three levels of abstraction constructed by OAKINK2 for complex tasks** , including the Affordance, Primitive Task, and Complex Task. OAKINK2 dataset provides allocentric and egocentric videos of human manipulation process, as well as the corresponding 3D-pose annotation and task specification. 

### **Abstract** 

_We present_ **OAKINK2** _, a dataset of bimanual object manipulation tasks for complex daily activities. In pursuit of constructing the complex tasks into a structured representation,_ OAKINK2 _introduces three level of abstraction to organize the manipulation tasks:_ **_Affordance_** _,_ **_Primitive Task_** _, and_ **_Complex Task_** _._ OAKINK2 _features on an_ 

> _⋆_ The first two authors contributed equally. 

> _‡_ This work is done when Lin is an intern at SJTU. 

> _†_ Cewu Lu is the corresponding author. He is the member of Qing Yuan Research Institute and MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University, China. 

_object-centric perspective for decoding the complex tasks, treating them as a sequence of object affordance fulfillment. The first level, Affordance, outlines the functionalities that objects in the scene can afford, the second level, Primitive Task, describes the minimal interaction units that humans interact with the object to achieve its affordance, and the third level, Complex Task, illustrates how Primitive Tasks are composed and interdependent._ OAKINK2 _dataset provides multi-view image streams and precise pose annotations for the human body, hands and various interacting objects. This extensive collection supports applications such as interaction reconstruction and motion synthe-_ 

1 

_sis. Based on the 3-level abstraction of_ OAKINK2 _, we explore a task-oriented framework for Complex Task Completion (CTC). CTC aims to generate a sequence of bimanual manipulation to achieve task objectives. Within the CTC framework, we employ Large Language Models (LLMs) to decompose the complex task objectives into sequences of Primitive Tasks and have developed a Motion Fulfillment Model that generates bimanual hand motion for each Primitive Task._ OAKINK2 _datasets and models are available at https://oakink.net/v2._ 

### **1. Introduction** 

Learning how humans achieve specific task objectives through diverse object manipulation behaviors has been a long-standing challenge. Recent data-driven approaches have made significant progress on this topic, including hand-object pose estimation [1, 7, 14, 22, 24–26, 39, 66], interaction synthesis [12, 17, 31, 57, 62, 71], and action imitation [53, 54]. However, the gap still exists for current methods to achieve a human-level understanding on object manipulation for complex task completion. In particular, humans possess a remarkable capacity to interact with specific objects in an appropriate sequence to achieve desired outcomes [33]. This inspires us to focus on the decomposition of hands-object interaction in complex manipulation tasks into sequential units. 

Tracing prior research, the advancement in hand-object interaction understanding is inseparable from the emergence of a series of hand-object interaction datasets [3, 8, 12, 15, 21, 24, 30, 34, 40, 47, 54, 56, 67, 72] to support data-driven methods. A noteworthy example among these datasets is OakInk [67]. OakInk analyzed object affordances ( _i.e_ . functional properties of objects/objectparts [18]) and collected _human-centric_ grasping interaction driven by intents to utilize these affordances. The term: _Oak_ is for object affordance knowledge, and _Ink_ for interaction knowledge. Nevertheless, the previous OakInk has two major limitations: 1) it lacks human demonstrations that cover the process of fulfilling those affordances, and 2) it lacks complex manipulation tasks that involve multiple object affordances. 

In this paper, we present OAKINK2, extending the data and methodology of the previous OakInk. In order to manage the inherent complexity in complex manipulation tasks, OAKINK2 adopts an _object-centric_ perspective and constructs three levels of abstraction upon manipulation tasks: **1)** **_Affordance_** : object/object-part level functionalities that enable manipulation. For example, a bottle cap affords securing and unsecuring of the content in the bottle. 

- **2)** **_Primitive Task (Primitive)_** : a “minimal” sequence of hand-object interaction that fulfills a given object’s affordance. For instance, to fulfill the affordance: securing, one needs to either _screw_ or _press_ the cap onto 

the bottle’s opening to form a seal that prevents leaking. 

- **3)** **_Complex Task_** : sequential combination of _Primitives_ to address the long-horizon and multi-goals manipulation tasks. Tasks are characterized as “complex” for their goal requires more than one object affordance. _Complex Tasks_ also detail the **dependencies** among the _Primitives_ and dictate the **order** in which they are executed. To illustrate, to pour the fluid from a sealed bottle, one must first _unscrew_ the cap and then _pour_ out the liquid. 

In this way, OAKINK2 delineates _Complex Tasks_ as directed acyclic graphs, hereafter referred to as **_Primitive_ Dependency Graphs (PDG)** . Within these graphs, each node represents a _Primitive_ , serving to fulfill a specific affordance. The directed edges illustrate the sequence in which _Primitives_ must be executed to achieve task completion. 

Build upon the above methodology, OAKINK2 introduces a large-scale dataset for bimanual object manipulation. It encompasses human demonstrations for complex task completion, with multi-view image streams and paired pose annotations for human body, hands and objects. OAKINK2 contains 627 sequences of real-world bimanual manipulation sequences, where 264 of these sequences are for _Complex Tasks_ . These sequences contain 4.01M frames from four different views (one egocentric and three allocentric views). The dataset includes four manipulation scenarios, 75 objects and 9 invited subjects in total. 

The versatile and task-driven nature of OAKINK2 enables a wide range of applications. In this paper, we focus on the task and motion planning for Complex Task Completion (CTC). CTC involves two notable components: **1)** text-based _Complex Task_ decomposition using _Primitives_ and **2)** task-aware motion generation to fulfill each _Primitive_ . For the first component, we design a task interpreter with Large Language Model (LLM) that can generate the PDG and program the execution order of these _Primitives_ , based on textual descriptions of the _Complex Tasks_ . For the latter component, we propose a generalist Task-aware Motion Fulfillment model (TaMF) to generate the hand motion at _Primitive_ level, based on the task-related object trajectory. 

In summary, our contributions are as follows: 

- We build an object-centric, three-level abstraction to structure and understand complex manipulation tasks, _i.e_ . _Affordance_ , _Primitive_ to fulfill affordance, and _Complex Task_ with _Primitive_ dependencies. 

- We introduce OAKINK2, a large-scale real-world dataset for bimanual object manipulation with human demonstrations for both _Primitives_ and _Complex Tasks_ . 

- We propose a task-oriented framework, CTC, for complex task and motion planning. CTC consists of a LLMbased task interpreter for _Complex Task_ decomposition and a diffusion-based motion generator for _Primitive_ fulfillment. 

2 

### **2. Related Works** 

**Hand-Object Interaction Datasets.** The recent research community has witnessed the emergence of numerous datasets on hand-object interactions. Earlier datasets [3, 12, 24] focused on static hand-object interactions with limited diversity. More recent datasets [8, 15, 21, 34, 41, 56, 72] captured dynamic hand-object interactions, covering bimanual interactions [15, 34] and interactions with articulated bodies [15, 72]. We pay particular attention to interaction datasets related to object affordances. [12] expressed affordances in grasp type labels. [3, 15, 56] collected intention labels for interactions. [30, 67] studied object affordance-based hand-object interaction and collected object segmentations and affordance labels. [41] studied hand-object interactions in tool-action-object pairs. Our proposed OAKINK2 captures both human demonstrations for minimal interaction fulfilling object affordance as _Primitive_ , and demonstrations for _Complex Task_ where these affordances are fulfilled in specific order constrained by their dependencies. 

**Decomposition of Manipulation Tasks.** Decomposing complex manipulation tasks into multiple building blocks across different hierarchies represents a widely adopted paradigm in the research community. [10] utilize the symbolic interface of task planners to construct an abstract state space, facilitating the reuse of hierarchical skills. [27, 63] decompose task specifications into hierarchical neural programs, which feature bottom-level programs as callable subroutines interacting with the environment. [9] chain multiple dexterous policies for achieving long-horizon task goals. [2] adopt a language-based methodology for decomposing action hierarchies. In our work, we introduce an object(affordance)-centric, three-level abstraction framework within OAKINK2 for the decomposition of complex manipulation tasks into _Primitives_ . 

**Motion Synthesis.** Motion synthesis involves obtaining credible and realistic human action sequences. There are plenty of works to generate human motions [51, 52, 59], even interactions [17, 36, 37, 57, 58, 62] based on different probabilistic model backbones like cVAE or denoising diffusion. In particular, [36, 37, 58] synthesize human motion based on the object motion, delegating the latter part to preceding models serving as inputs. Inspired by these works, we propose a new task within OAKINK2: Taskaware Motion Fulfillment This task requires the model to synthesize hand motion trajectories based on given textual task descriptions and object motions. 

**Foundation Models in Manipulation Tasks.** Recent days we have seen a significant increase in the application of foundation models in completing manipulation tasks. There are significant efforts for end-to-end foundation models 

[4, 5, 11] that outputs control signals from visual and textual inputs. Existing works [6, 28, 55] also leverage the in-context learning and zero-shot generalization abilities of Large Language Models (LLMs) for action selection from an array of choices to realize an autoregressive achievement of planning. Demonstration of LLM-based program generation for task completion in [29, 37, 55] inspires us to explore the ability of LLMs to reason code for discerning interdependencies between object affordances in complex tasks, along with the sequence in which they are implemented. Our OAKINK2 introduce the decomposition of _Complex Tasks_ into interdependent affordance-based _Primitives_ , accompanied by their diverse image-textual descriptions. Based on this, we show an application of OAKINK2 in Complex Task Completion utilizing existing power of foundation models. 

### **3. Construction of OAKINK2** 

We first introduce how the three-level of abstractions are acquired in Sec. 3.1, then provide the details for data collection and annotation in Sec. 3.2. 

#### **3.1. Complex Task Acquisition** 

**Task Initialization.** Given a collected repository of objects, we first construct four manipulation scenarios. Each scenario has its unique characteristic and corresponds to a set of complex manipulation tasks. These scenarios are: 1) kitchen table; 2) study room table; 3) demo chem lab; 4) bathroom table. Then, we invite four annotators ( ) to propose _Complex Tasks_ in these scenarios and select object cluster that required for these tasks (Fig. 2’s 1st column). 

##### **3.1.1 Object Affordance Analysis** 

After the task targets are determined, we proceed to analyze the objects’ affordances in given scenarios. The expression of affordance adheres to the definitions in the previous OakInk [67]: each affordance contains a specific object part segmentation ( _e.g_ . a bottle cap) and a descriptive phrase tuple ( _e.g_ . <secure, sth>), which elucidates the function of that part. We provide examples of these affordances in Fig. 2’s 2nd column. 

##### **3.1.2 Primitive Task Design** 

In the second stage, We design _Primitives_ as the **minimal** interactions that fulfill those object affordance. Here “minimal” indicates the task are required to fully complete the functionality of a certain affordance without any redundant interaction process. Each _Primitive_ contains a starting condition, a terminal condition, and the in-between hand-object interaction process. For example, considering an affordance associated with a knife blade meant to <cut, sth>, a corresponding _Primitive_ , _cut_ , requires the subject to move 

3 



<!-- Start of picture text -->
analyze   Object Affordance design  Primitive decompose  Complex Task<br><cut, sth> cut sth Given the  Scene  and the  Task  objectives:<br>Expert Pepare a bowl of hot sweet fruit tea<br>Object Repository <grip, sth> grip sth How will you accomplish this task?<br>envision  Task  OPEN unscrew cap I will first use      for cut sth<br>Prepare dishesPrepare a mug of tea <secure, sth> CLOSE screw cap Next Then hold   for  unscrew  pour grip sth st hscrew cap of Subject<br>Prepare hot sweet fruit teaClean the kitchen table <store, sth> <contain, sth> pour out sth Then,Afterwards place sth inpress buttonopen gate and of  of   close gate to start heat.,<br>Prepare fruit plattersPrepare a cup of wine ������ <contain, sth> place sth intake sth out Last, open take sth out close<br>L0 L1 L2 L3 L9<br>select  Object Cluster ������ <heat, sth> <control, sth><secure, sth> CLOSEOPEN press buttonclose gateopen gate PrimitiveDependencyGraph OPEN CLOSE OPEN <heat, sth> CLOSE OPEN CLOSE<br><!-- End of picture text -->

Figure 2. **Illustration of the complex task acquisition process.** This figure use a _Complex Task_ : ‘Prepare a bowl of hot sweet fruit tea.’ to demonstrate the process. Initially, the annotators ( ) analyze the affordances of four essential objects (a gripper, a knife, a tea bottle, and a microwave oven) and design corresponding _Primitive_ . For instance, to prepare fruit slices, the _Primitive_ : cut associated with the knife blade is required. Following this, an expert ( ) arranges the scene for the _Complex Task_ , and then the subject ( ), utilizing the designed _Primitive_ , plans the execution path of the _Complex Task_ . Later, these execution paths are structured into a _Primitive_ Dependency Graphs. 

the blade to completely pass through the object to be cut so that the separated parts could be detached. In this stage, we collect all available object affordances and their associated _Primitives_ , leading to a _Primitive_ tasks pool (Fig. 2’s 3rd column). 

##### **3.1.3 Complex Task Decomposition** 

In the third stage, we proceed to decompose the previous proposed _Complex Task_ – characterized by its long-horizon and multi-goal manipulation targets – into a series of shortterm and single-goal _Primitives_ . In emphasizing the ordering of _Primitive_ completion is important for the _Complex Task_ completion, our approach also delineates the **dependencies** between _Primitives_ . Therefore, each _Complex Task_ contains a series of _Primitives_ , along with a _Primitive_ Dependency Graph (PDG), which maps out the hierarchical execution order of these _Primitives_ . _Primitives_ at level 0 (L0) are independent, requiring no prior _Primitives_ to be completed, while the final level include those _Primitives_ that bring the _Complex Task_ to completion. 

We deploy a dedicated protocol to acquire the decomposition and dependencies. As shown in Fig. 2’s 4th column, initially, an expert ( ) instantiates the scene and target with specific description. Subsequently, a subject ( ) is instructed to describe the order of the completion using the available _Primitive_ in the pool. Then, the expert records and organizes this sequence into the PDG, concluding the _Complex Task_ acquisition process. 

#### **3.2. Data Collection and Annotation** 

After the acquisition of the three-level of abstractions, the subjects are required to complete the _Primitive_ and _Complex Task_ respectively in a data capture platform (Fig. 3). 



Figure 3. **Capture platform.** 12 MoCap cameras are circled in blue and 4 RGB cameras in red. 

##### **3.2.1 Capture Setup** 

The data capture platform contains two major components: the multi-camera system for recording the manipulation process and the optical MoCap system for pose tracking. The MoCap system uses 12 Optitrack Prime 13W infrared cameras to track the surface markers affixed to the subject’s upper body, left and right hand, and interacting objects. The multi-camera system consists of 4 commodity RGB cameras, 3 of which are from allocentric views and 1 is from the egocentric view. We synchronize all sensors at 30 fps and calibrate the transformation between these two systems. 

##### **3.2.2 Data Annotation** 

**Object Pose.** Poses of rigid bodies are directly solved via the MoCap system. For the poses of articulated bodies, the base parts of articulated bodies are handled similarly to rigid bodies, while the articulated parts are divided into two categories. If the part is large enough to attach enough mark- 

4 



<!-- Start of picture text -->
Task :  prepare a sweet pear soup in the yellow teacup.<br>Primitives: cut, uncap, scoop, pour, unscrew, place ...<br>State : The pear required for the<br>task is not cut. Use knife to cut it.<br>Action: cut  the pear with knife<br>and  place  in the teacup.<br>State : the pear has been cut.<br>The teacup lacks sugar and<br>water. Add sugar to the teacup.<br>Action: uncap  the lid of the<br>sugar can.<br>State : The lid of the sugar can<br>has been removed. Transfer the<br>sugar to the teacup<br>Action: scoop  sugar from sugar<br>can to the yellow teacup.<br>State : The sugar has been<br>placed. Teacup lacks water.<br>Add water in it<br>Action: unscrew  the lid of the<br>bottle containing water.<br>… … … …<br><!-- End of picture text -->

Figure 4. **Commentary of the task execution.** The left column shows the current state of the scene. The center column shows the narrative dialog retrieved from experts. The right column shows the upcoming _Primitive_ task to be executed. 

ers without blocking the interaction then it will be handled like rigid bodies. Otherwise, only one marker is attached to that part. The marker’s position is calibrated in the object’s canonical coordinate frame. Later, given the articulation type ( _e.g_ . revolution or prismatic), the parameter of the articulation joint is determined by minimizing the squared difference between the observed marker position and the recovered marker position in the object’s canonical frame. 

**Human Pose and Surface.** The annotation of human pose and surface relies on SMPL-X [50] body mesh. To actually acquire human pose and surface, we employ a twostage fitting approach in align with the MoSH++ [44]. In the first stage, we use the captured markers when the subject in T-pose to fit the subject’s SMPL-X shape parameter _β_<sup>¯</sup> and each marker’s location _PM_<sup>(</sup><sup>_c_)inSMPL-Xcanon-</sup> ical space. From stage one’s optimization result, we can determine the correspondence _C_ ( _·_ ) from the subject’s surface markers to the vertices of the SMPL-X model. In the second stage, we fit the per-frame subject poses parameter _θ_ throughout the task completion process. This fitting is grounded in the previously acquired shape _β_<sup>¯</sup> and marker correspondence _C_ ( _·_ ). With pose and shape parameters obtained, the subject’s body mesh is reconstructed using the SMPL-X model. Other body representations like MANO are derived from this result. Refer to Sup. Mat for details. 

**Commentary of Task Execution.** After the manipulation process is completed, we send the video recording to experts for analysis, requesting them to furnish detailed com- 

mentary on the task execution process. At each _Primitive_ step, experts are asked to provide comments on the current task state and the forthcoming action. Specifically, given the execution of the previous _Primitive_ , experts are asked to 1) summarize the tasks yet to be completed to achieve the manipulation goals, considering both the current scene and the upcoming _Primitive_ slated for execution; and 2) offer descriptions of the next action using the available _Primitives_ in the pool. This process is illustrated in Fig. 4. The narrative text provided by experts are subsequently refined using GPT-4 [48] to serve as commentary. OAKINK2 features on these commentaries as they encapsulate the expert’s chainof-thought when observing the manipulation process. These commentaries serve not only to interpret user behaviors but also to inform the generation of user actions. 

### **4. The OAKINK2 Dataset** 

#### **4.1. Data and Annotation List** 

OAKINK2 provide RGB videos that record the manipulation processes. These videos are collected from multiview (1 egocentric and 3 allocentric) setup, synchronized at 30 fps, with resolution 848 _×_ 480. The annotations contains two parts: **1) 3D motion** , including pose and shape for the human upper-body, hands, and objects (with articulation parameters) during the interaction process; and the **2) task specification** , including object affordances, _Primitives_ that correspond to these affordances, _Complex Tasks_ with task goals, initial conditions, PDGs, expert commentary, and subject’s completion sequence. Evaluations of the 3D annotation qualities are provided in Sup. Mat. Annotation on 3D hand keypoints undergo cross-dataset validation with a reconstruction model, while the 3D poses associated with grasping actions are examined for the physical property integrity. 

#### **4.2. Dataset Statistics** 

OAKINK2 sets up four scenarios of hand-object interaction with a total number of 38 long-horizon complex manipulation goals, which instantiates to 150 _Complex Tasks_ . OAKINK2 contains in total 75 objects and 39 affordance. These affordances map to 60 types of _Primitives_ . OAKINK2 contains 627 sequences of bimanual dexterous hand-object interaction in total. 363 of these are for _Primitives_ and 264 are for _Complex Tasks_ . In total, OAKINK2 contains 4.01M image frames. We compare OAKINK2 to multiple existing hand-object interaction datasets in Tab. 4. Here we highlight several notable features of OAKINK2: 1) it provides interaction grounded in object affordance ( _vs_ . HO3D, DexYCB); 2) it features long-horizon manipulation goals ( _vs_ . ARCTIC, HOI4D, GRAB); 3) it includes 3D pose and shape annotation for both hands and objects ( _vs_ . EGO4D, AssemblyHands); and 4) it offers task decomposition using _Primitives_ , which is not available in any datasets in Tab. 4. 

5 

|Dataset|image<br>mod.|resolution|#frame #|views|#subj|#obj|3D<br>gnd.|real /<br>syn.|label<br>method|hand<br>pose|obj<br>pose|afford.<br>inter.|dynamic<br>inter.|long-<br>horizon|task<br>decomp.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EGO4D [19]|✓|_∼_|_∼_|1|931|–|✗|–|–|✗|✗|✗|✗|✓|✓|
|HO3D [21]|✓|640_×_480|78K|1-5|10|10|✓|real|auto|✓|✓|✗|✓|✗|✗|
|GRAB [56]|✗|–|1.62M|–|10|51|✓|real|mocap|✓|✓|✓|✓|✗|✗|
|H2O [34]|✓|1280_×_720|571K|5|4|8|✓|real|auto|✓|✓|✓|✓|✗|✗|
|HOI4D [40]|✓|1280_×_800|3M|1|9|1000|✓|real|crowd|✓|✓|✓|✓|✗|✗|
|ARCTIC [15]|✓|2800_×_2000|2.1M|9|10|11|✓|real|mocap|✓|✓|✓|✓|✗|✗|
|AssemblyHands [47]|✓|1920_×_1080|3.03M|12|34|–|✓|real|semi-auto|✓|✗|✓|✓|✓|✓|
|Ego-Exo4D [20]|✓|_∼_|_∼_|5-6|839|–|✓|real|semi-auto|✓|✗|✗|✓|✓|✓|
|OakInk-Image [67]|✓|848_×_480|230K|4|12|100|✓|real|crowd|✓|✓|✓|✓|✗|✗|
|**OAKINK2**|✓|848_×_480|**4.01M**|4|9|75|✓|real|mocap|✓|✓|✓|✓|✓|✓|



Table 1. **A cross-comparison among various public datasets.** (Refer to Sup. Mat for the full table.) 

### **5. Selected Applications** 

geometries **_V_** _o_ = _{_ **V** _o,m}_ and their motion trajectories **_T_** _o_ = _{_ **T**<sup>(</sup> _o,m_<sup>_i_)</sup><sup>_}_during the interaction process are known.We</sup> use subscript _h_ to represent human hands, _o_ to represent the object, _m_ to index different object instances (and different parts of the same instance) and superscript ( _i_ ) to index different timestamps. The task is to generate a corresponding hands motion trajectory **_P_** _h_ = _{_ **P**<sup>(0:</sup> _h_<sup>_L_)</sup> _}_ conditioned on the textual description **text** PT, object geometries **_V_** _o_ , and motion trajectories **_T_** _o_ . 

#### **5.1. Hand Mesh Reconstruction** 

The Hand Mesh Reconstruction (HMR) task is to estimate the 3D hand pose during the interaction process from the captured images. We benchmark HMR task under both single-view settings and multi-view settings. In single-view settings, the image input only contains one view, egocentric or allocentric. In multi-view settings, the image input will contain multiple views, together with the camera calibration parameters. For both settings we partition the corresponded task-specified subsets at the sequence level, maintaining the proportion of samples in train/val/test sets at approximately 70%, 5%, and 25%. 

**Evaluation Metrics.** We evaluate contact ratio (CR) and solid intersection volume (SIV) to measure the physical plausibility of the generated motion. On sequence-level, we evaluate motion smoothness with Power Spectrum KL divergence of joints (PSKL-J) as in human motion generation, and evaluate FID to measure distances between the ground-truth motions and the generated motions. We also conduct a perceptual study to evaluate the level of realism for the generated motion. Detailed definition of these metrics can be found in Sup. Mat. 

We evaluate mean per joint position error (MPJPE), mean per vertex position error (MPVPE) in world space, wrist(root)-relative (RR) systems and systems after Procrustes analysis (PA). We also evaluate area under curve (AUC) of correct keypoints percentage within range 0 _−_ 20 mm in root-relative systems. We show HMR benchmark results under both settings in Tab. 2. 



<!-- Start of picture text -->
x T − 1 x T − 2<br>Setting Methods MPJPEPA- MPVPEPA- RR-MPJPE ( AUC ) -MPVPERR MPJPE MPVPE ������ ������ �������������<br>x ˆ 0 x ˆ 0 x 0<br>METRO [38] 6.90 6.47 17.56 (0.410) 16.44 – – x 1<br>Mono RLE [+ HandTailer [35] 42] 5.46 6.86 13.08 (0.441) 14.03 – – x T ��������� ��������� ��������� ���������<br>Multi KP-based Fit [68] 9.20 8.83 15.63 (0.349) 15.38 19.30 19.11 x ˆ 0 �������������<br>POEM [68] 6.18 6.61 12.12 (0.581) 12.15 9.17 9.52<br>��������� ���������<br>Table 2. Single- and multi-view HMR  evaluation results  in  mm . ������ ������<br>������������������� �������������������<br>�� ��<br>+ + + + + + + + + +<br>���� ���� ���� ���� ���� ����<br>5.2. Task-aware Motion Fulfillment (TaMF)<br>���� ��������� ������������������ ���� ������������������<br>To achieve task objectives in interaction scenarios, we intro- ������������������� x 0<br>duce a novel task: Task-aware Motion Fulfillment (TaMF). ���� ���� ����������������� ����������������� ������������� ���� ����������������� ����������������� ���������������<br><!-- End of picture text -->

Table 2. Single- and multi-view HMR **evaluation results** in _mm_ . 

#### **5.2. Task-aware Motion Fulfillment (TaMF)** 

To achieve task objectives in interaction scenarios, we introduce a novel task: Task-aware Motion Fulfillment (TaMF). It targets at the generation of hand motion sequences that can fulfill given object trajectories conditioned on textual task descriptions. 

Figure 5. **Architecture of MF-MDM.** First sample random noises **_x_** _T_ ; then at each step iterating from _T_ to 1, MF-MDM G predicts the cleaned sample **_x_** ˆ0 and then diffuse it back to **_x_** _t−_ 1. After the generated sample **_x_** 0 is acquired, it is refined by MF-MDM R for better interaction details. 

**Task Formulation.** Given a textual description of the _Primitive_ task: **text** PT, we assume the involved objects 

6 



<!-- Start of picture text -->
�������������������������� ��������������������������<br>����������������� ���������������������� ��������������������� �����������������<br>��������������� ���������������<br>������������������� ����������������������������� �������������� �����������������������������<br>������������ ��������������<br>���������������������� ��������������������� ����������������������������������� ���������������������<br>�������������������<br>������������������������������������������ ������������������������ ������������������������������������ ���������������������<br><!-- End of picture text -->

Figure 6. **Qualitative Visualization** of the generated hand motion in TaMF model. 

|Physical lausibility|Motion Smoothness|
|---|---|
|CR_↑_<br>SIV(cm<sup>3</sup>)_↓_|PSKL-J(**g.t.**, **p.**) _↓_<br>(**p.**, **g.t.**) _↓_|
|0.90<br>4.17|0.0446<br>0.0460|
|FID|Perceptual Score<br>Dataset<br>Generated|
|1.369|4_._66_±_0_._48<br>3_._64_±_0_._85|



Table 3. **Evaluations** of generated hand motion in TaMF model. PSKL-J is evaluated between the training data ( **g.t.** ) and the generated hand motion trajectory ( **p.** ); both directions are included as PSKL-J is an asymmetric metric. 

**Model and Results.** We enhance a diffusion-based motion generation model: MDM [59], tailoring it to the nuanced requirements of task-aware hand motion synthesis. The model architecture is visualized in Fig. 5. Our proposed model, named as MF-MDM, consists of two components: **1) MF-MDM G** , which generates human motion trajectory conditioned on textual descriptions of tasks and object motion trajectories; and **2) MF-MDM R** , which refines generated hand motion based on spatial hand-object relationships. The sampling process is modeled as a reversed diffusion process of gradually cleaning noised samples. The key difference for MF-MDM is to incorporate multi-object related probabilistic conditions into existing transformer encoder. To achieve this, we employ an extra layer, Sequential Merging, to aggregate spatial relationships in the interaction scene at each frame. The object motion trajectories and the previously diffused hand motion trajectory are projected to the same dimension and aggregated. For the refine model MF-MDM R, we append hand-object distances as an extra spatial information for Sequential Merging layer. The aggregated embedding sequence is combined with other tokens before being fed into the main transformer encoder: the noising step token, the text embedding of the task description from the CLIP text encoder, and the aggregated 

object geometry embeddings from the PointBert encoder. We also provide the quantitative evaluations in Tab. 3 and qualitative visualization in Fig. 6. 

#### **5.3. Complex Task Completion (CTC)** 

OAKINK2 brings in a new application – breaking _Complex Task_ goals into paths of _Primitive_ motions. The Complex Task Completion (CTC) is to generate hands motion trajectories based on a textual description of the scene and the task objectives. Considering the challenge of direct translation from complex task and scene text to end-to-end motion generation, which involves a transition across multiple modalities, there is currently no adequate framework to address this problem. Therefore, we decompose CTC into three stages, tackling each one sequentially. 

The process initially begins with text-based **1)** **_Primitive_ planning** . The recent breakthroughs in foundation models [48, 69], such as Large Language Models (LLMs), allow us to utilize them as the task planner, as these models already have the capability to plan the _Primitive_ execution path, while only requiring proper guidance and context. The output of this stage is a task planning script that includes the execution order for each _Primitive_ . Subsequently, the problem is reformulated into generating the hand and object motion trajectories for each _Primitive_ , based on the target task and scene state, thus modeling _P_ ( **_P_** _h,_ **_T_** _o|_ **text** PT). We again break this down into two subtasks: **2) object trajectory retrieval** , _i.e_ . _P_ ( **_T_** _o|_ **text** PT) and **3) hand motion generation** _i.e_ . _P_ ( **_P_** _h|_ **_T_** _o,_ **text** PT). The former is solved by re-targeting<sup>1</sup> object motion from expert’s demonstration to meet the newly generated random scene. The latter is our pre-defined Task-aware Motion Fulfillment model (TaMF, Sec. 5.2). 

**_⃝_ 1 Primitive Planning by LLMs.** In this stage, we leverage the off-the-shelf GPT-4 [48] to generate program that decompose the _Complex Task_ as a sequence of _Primitive_ . We first embed the scene description **text** scene, the complex task description **text** goal and each object’s description _{_ **text** obj _}_ into the prompt based on manually designed templates. GPT-4 will respond to the prompt using the **program** . As shown in Fig. 8’s code block, this program instantiates the _Primitive_ Dependency Graph (PDG) using a sequence of code snippets, where each node of the PDG ( _Primitive_ ) is implemented as a **execute** ([primitive], ...)function, and the edge of the PDG is implemented as function’s calling order. Then we use a dependency checker built upon the PDG information in OAKINK2 to test whether the generated program completes the _Complex Task_ without violation of constraints. If a successful program is obtained, we move to the next stage. 

> 1re-target refers to the process of adjusting pre-existing motion trajectories to align with new initial and target poses of objects, ensuring compatibility with the current scene 

7 



<!-- Start of picture text -->
��������� ���������<br>cut sth ���������������������������� place sth in transition pour out sth ��������������������������������������������<br><!-- End of picture text -->

Figure 7. **Visualization of Motion Generation Outcome in Complex Task Completion.** 



<!-- Start of picture text -->
�����������<br>������������ ����� ������ ���������� ������<br>��������� ����������� ����������� ������� ���������<br>������ �������������<br>��������� � � � � �<br>��� ������ ������<br>�������� ������������ ���������<br>������������������ cut sth<br>def exec_task():<br>execute(“cut”,<br>        generator,<br>object_trajectory,<br>        src_object= knife ,<br>        tgt_object= pear )<br>pour sth<br>execute(“pour”,<br>        generator,<br>object_rajectory,<br>        src_object= bottle ,<br>        tgt_object= frying _ pan )<br><!-- End of picture text -->

Figure 8. **The diagram of Complex Task Completion.** The task input populates a predefined template to generate the prompt for planning. The _⃝_ 1 LLM (GPT-4) responds with code of the program’s execution path, delineating the DAG for _Primitive_ dependency. Within the code response block, the **orange** snippets marks the _⃝_ 2 Oracle to re-target object trajectories; the **blue** snippets indicate _⃝_ 3 motion generators for _Primitives_ . 

At this moment, the **execute()** function in Fig. 8’s code snippets remain incomplete, lacking two pivotal components: the **object** **~~t~~ rajectory** and the hand motion **generator** . We will address these components in the following two stages. 

**_⃝_ 2 Object Trajectories Retrieval from Oracle.** Accomplishing a _Primitive_ task necessitates the object’s motion trajectories within that context. In this stage, we leverage an Oracle to retrieve object motion trajectories based on a certain scene and _Primitive_ . The term “Oracle” denotes a dual-function capability: 1) pursuant to a given _Primitive_ , it fetches the object motion trajectories within the OAKINK2 dataset, and 2) it re-targets these expert-derived trajectories based on the initial, functional and post poses of the objects, thereby conforming to new scene requirements and generating the desired **object** **~~t~~ rajectory** . 

**_⃝_ 3 Hand Motion Generation with TaMF.** Once the object trajectories are obtained, the final stage is to generate hand motion trajectories for each _Primitive_ . To this end, we 

utilize our previously designed Task-aware Motion Fulfillment model (TaMF, Sec. 5.2) as a generalist **generator** (indicating that a singular TaMF model accommodates all _Primitives_ ). After populating all **execute()** functions with the determined object trajectories and generator, the program is executed in sequel and all the _Primitive_ trajectories are connected by interpolation. This interpolation ensures smooth transitions by linking the final state of a preceding trajectory with the initial state of the subsequent one. 

We show an example of the generated motions for _Complex Task_ in Fig. 7. Details of test scene generation, prompts and templates, evaluations of primitive planning, success/failure cases are referred to Sup. Mat. 

### **6. Future Works** 

OAKINK2 is a dataset packing a variety of hand-object interactions for human completion of long-horizon and multigoal complex manipulation tasks. OAKINK2 incorporates _Primitive_ demonstrations, characterized as minimal interactions that fulfill object affordance, and _Complex Tasks_ demonstrations, which also include their decomposition into interdependent _Primitives_ . 

First, we expect OAKINK2 to support large-scale language-manipulation pre-training, improving the performance of multi-modal ( _e.g_ . vision-language-action [69]) models for Complex Task Completion. In the longer term, we expect OAKINK2 can potentially support learning frameworks capable of end-to-end text-to-manipulation generation. 

Second, OAKINK2 can empower various embodied manipulation tasks by re-targeting the collected demonstrations of _Primitives_ to different embodiments, such as heterogeneous hands and platforms as [23, 53, 54, 61, 64] implied. The interaction scenarios constructed in OAKINK2 can also be transferred and integrated into existing simulation environments [45, 60] to support embodied learning on object manipulation. 

**Acknowledgments.** This work was supported by the National Key Research and Development Project of China (No. 2022ZD0160102), National Key Research and Development Project of China (No. 2021ZD0110704), Shanghai Artificial Intelligence Laboratory, XPLORER PRIZE grants, and 2023 Shanghai Pujiang X Program Project (No. 23511103104). 

8 

### **References** 

- [1] Ahmed Tawfik Aboukhadra, Jameel Malik, Ahmed Elhayek, Nadia Robertini, and Didier Stricker. THOR-Net: End-toend graformer-based realistic two hands and object reconstruction with self-supervision. In _Winter Conference on Applications of Computer Vision (WACV)_ , 2023. 2 

- [2] Suneel Belkhale, Tianli Ding, Ted Xiao, Pierre Sermanet, Quon Vuong, Jonathan Tompson, Yevgen Chebotar, Debidatta Dwibedi, and Dorsa Sadigh. RT-H: Action hierarchies using language. _arXiv preprint arXiv:2403.01823_ , 2024. 3 

- [3] Samarth Brahmbhatt, Chengcheng Tang, Christopher D Twigg, Charles C Kemp, and James Hays. ContactPose: A dataset of grasps with object contact and hand pose. In _European Conference on Computer Vision (ECCV)_ , 2020. 2, 3, 15 

- [4] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alex Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, and Brianna Zitkovich. RT-2: Vision-language-action models transfer web knowledge to robotic control. _arXiv preprint arXiv:2307.15818_ , 2023. 3 

- [5] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana Gopalakrishnan, Karol Hausman, Alex Herzog, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Tomas Jackson, Sally Jesmonth, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Kuang-Huei Lee, Sergey Levine, Yao Lu, Utsav Malla, Deeksha Manjunath, Igor Mordatch, Ofir Nachum, Carolina Parada, Jodilyn Peralta, Emily Perez, Karl Pertsch, Jornell Quiambao, Kanishka Rao, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Kevin Sayed, Jaspiar Singh, Sumedh Sontakke, Austin Stone, Clayton Tan, Huong Tran, Vincent Vanhoucke, Steve Vega, Quan Vuong, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, and Brianna Zitkovich. RT-1: Robotics transformer for realworld control at scale. _Robotics: Science and Systems (RSS)_ , 2023. 3 

- [6] Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not as i say: Grounding language in robotic affordances. In _Conference on Robot Learning (CoRL)_ , 2023. 3 

- [7] Zhe Cao, Ilija Radosavovic, Angjoo Kanazawa, and Jitendra Malik. Reconstructing hand-object interactions in the wild. 

In _International Conference on Computer Vision (ICCV)_ , 2021. 2 

- [8] Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov, Ankur Handa, Jonathan Tremblay, Yashraj S. Narang, Karl Van Wyk, Umar Iqbal, Stan Birchfield, Jan Kautz, and Dieter Fox. DexYCB: A benchmark for capturing hand grasping of objects. In _Computer Vision and Pattern Recognition (CVPR)_ , 2021. 2, 3, 15 

- [9] Yuanpei Chen, Chen Wang, Li Fei-Fei, and C Karen Liu. Sequential dexterity: Chaining dexterous policies for longhorizon manipulation. _arXiv preprint arXiv:2309.00987_ , 2023. 3 

- [10] Shuo Cheng and Danfei Xu. LEAGUE: Guided skill learning and abstraction for long-horizon manipulation. _IEEE Robotics and Automation Letters_ , 2023. 3 

- [11] Open X-Embodiment Collaboration, Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, Albert Tung, Alex Bewley, Alex Herzog, Alex Irpan, Alexander Khazatsky, Anant Rai, Anchit Gupta, Andrew Wang, Anikait Singh, Animesh Garg, Aniruddha Kembhavi, Annie Xie, Anthony Brohan, Antonin Raffin, Archit Sharma, Arefeh Yavary, Arhan Jain, Ashwin Balakrishna, Ayzaan Wahid, Ben Burgess-Limerick, Beomjoon Kim, Bernhard Sch¨olkopf, Blake Wulfe, Brian Ichter, Cewu Lu, Charles Xu, Charlotte Le, Chelsea Finn, Chen Wang, Chenfeng Xu, Cheng Chi, Chenguang Huang, Christine Chan, Christopher Agia, Chuer Pan, Chuyuan Fu, Coline Devin, Danfei Xu, Daniel Morton, Danny Driess, Daphne Chen, Deepak Pathak, Dhruv Shah, Dieter B¨uchler, Dinesh Jayaraman, Dmitry Kalashnikov, Dorsa Sadigh, Edward Johns, Ethan Foster, Fangchen Liu, Federico Ceola, Fei Xia, Feiyu Zhao, Freek Stulp, Gaoyue Zhou, Gaurav S. Sukhatme, Gautam Salhotra, Ge Yan, Gilbert Feng, Giulio Schiavi, Glen Berseth, Gregory Kahn, Guanzhi Wang, Hao Su, Hao-Shu Fang, Haochen Shi, Henghui Bao, Heni Ben Amor, Henrik I Christensen, Hiroki Furuta, Homer Walke, Hongjie Fang, Huy Ha, Igor Mordatch, Ilija Radosavovic, Isabel Leal, Jacky Liang, Jad Abou-Chakra, Jaehyung Kim, Jaimyn Drake, Jan Peters, Jan Schneider, Jasmine Hsu, Jeannette Bohg, Jeffrey Bingham, Jeffrey Wu, Jensen Gao, Jiaheng Hu, Jiajun Wu, Jialin Wu, Jiankai Sun, Jianlan Luo, Jiayuan Gu, Jie Tan, Jihoon Oh, Jimmy Wu, Jingpei Lu, Jingyun Yang, Jitendra Malik, Jo˜ao Silv´erio, Joey Hejna, Jonathan Booher, Jonathan Tompson, Jonathan Yang, Jordi Salvador, Joseph J. Lim, Junhyek Han, Kaiyuan Wang, Kanishka Rao, Karl Pertsch, Karol Hausman, Keegan Go, Keerthana Gopalakrishnan, Ken Goldberg, Kendra Byrne, Kenneth Oslund, Kento Kawaharazuka, Kevin Black, Kevin Lin, Kevin Zhang, Kiana Ehsani, Kiran Lekkala, Kirsty Ellis, Krishan Rana, Krishnan Srinivasan, Kuan Fang, Kunal Pratap Singh, Kuo-Hao Zeng, Kyle Hatch, Kyle Hsu, Laurent Itti, Lawrence Yunliang Chen, Lerrel Pinto, Li FeiFei, Liam Tan, Linxi ”Jim” Fan, Lionel Ott, Lisa Lee, Luca Weihs, Magnum Chen, Marion Lepert, Marius Memmel, Masayoshi Tomizuka, Masha Itkina, Mateo Guaman Castro, Max Spero, Maximilian Du, Michael Ahn, Michael C. Yip, Mingtong Zhang, Mingyu Ding, Minho Heo, Mo- 

9 

han Kumar Srirama, Mohit Sharma, Moo Jin Kim, Naoaki Kanazawa, Nicklas Hansen, Nicolas Heess, Nikhil J Joshi, Niko Suenderhauf, Ning Liu, Norman Di Palo, Nur Muhammad Mahi Shafiullah, Oier Mees, Oliver Kroemer, Osbert Bastani, Pannag R Sanketi, Patrick ”Tree” Miller, Patrick Yin, Paul Wohlhart, Peng Xu, Peter David Fagan, Peter Mitrano, Pierre Sermanet, Pieter Abbeel, Priya Sundaresan, Qiuyu Chen, Quan Vuong, Rafael Rafailov, Ran Tian, Ria Doshi, Roberto Mart’in-Mart’in, Rohan Baijal, Rosario Scalise, Rose Hendrix, Roy Lin, Runjia Qian, Ruohan Zhang, Russell Mendonca, Rutav Shah, Ryan Hoque, Ryan Julian, Samuel Bustamante, Sean Kirmani, Sergey Levine, Shan Lin, Sherry Moore, Shikhar Bahl, Shivin Dass, Shubham Sonawani, Shuran Song, Sichun Xu, Siddhant Haldar, Siddharth Karamcheti, Simeon Adebola, Simon Guist, Soroush Nasiriany, Stefan Schaal, Stefan Welker, Stephen Tian, Subramanian Ramamoorthy, Sudeep Dasari, Suneel Belkhale, Sungjae Park, Suraj Nair, Suvir Mirchandani, Takayuki Osa, Tanmay Gupta, Tatsuya Harada, Tatsuya Matsushima, Ted Xiao, Thomas Kollar, Tianhe Yu, Tianli Ding, Todor Davchev, Tony Z. Zhao, Travis Armstrong, Trevor Darrell, Trinity Chung, Vidhi Jain, Vincent Vanhoucke, Wei Zhan, Wenxuan Zhou, Wolfram Burgard, Xi Chen, Xiaolong Wang, Xinghao Zhu, Xinyang Geng, Xiyuan Liu, Xu Liangwei, Xuanlin Li, Yao Lu, Yecheng Jason Ma, Yejin Kim, Yevgen Chebotar, Yifan Zhou, Yifeng Zhu, Yilin Wu, Ying Xu, Yixuan Wang, Yonatan Bisk, Yoonyoung Cho, Youngwoon Lee, Yuchen Cui, Yue Cao, Yueh-Hua Wu, Yujin Tang, Yuke Zhu, Yunchu Zhang, Yunfan Jiang, Yunshuang Li, Yunzhu Li, Yusuke Iwasawa, Yutaka Matsuo, Zehan Ma, Zhuo Xu, Zichen Jeff Cui, Zichen Zhang, and Zipeng Lin. Open X-Embodiment: Robotic learning datasets and RT-X models. https://arxiv.org/abs/2310.08864, 2023. 

   - 3 

- [12] Enric Corona, Albert Pumarola, Guillem Alenya, Francesc Moreno-Noguer, and Gr´egory Rogez. GanHand: Predicting human grasp affordances in multi-object scenes. In _Computer Vision and Pattern Recognition (CVPR)_ , 2020. 2, 3, 15 

- [13] Dima Damen, Hazel Doughty, Giovanni Maria Farinella, Antonino Furnari, Evangelos Kazakos, Jian Ma, Davide Moltisanti, Jonathan Munro, Toby Perrett, Will Price, et al. Rescaling egocentric vision: Collection, pipeline and challenges for epic-kitchens-100. _International Journal of Computer Vision_ , 2022. 15 

- [14] Bardia Doosti, Shujon Naha, Majid Mirbagheri, and David Crandall. HOPE-Net: A graph-based model for hand-object pose estimation. In _Computer Vision and Pattern Recognition (CVPR)_ , 2020. 2 

- [15] Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J Black, and Otmar Hilliges. ARCTIC: A dataset for dexterous bimanual handobject manipulation. In _Computer Vision and Pattern Recognition (CVPR)_ , 2023. 2, 3, 6, 13, 15 

- [16] Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, and Tae-Kyun Kim. First-person hand action benchmark with rgb-d videos and 3D hand pose annotations. In _Computer Vision and Pattern Recognition (CVPR)_ , 2018. 15 

- [17] Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik, Christian Theobalt, and Philipp Slusallek. IMoS: Intent-driven full-body motion synthesis for human-object interactions. In _Computer Graphics Forum_ , 2023. 2, 3 

- [18] James J Gibson. _The ecological approach to visual perception: classic edition_ . Psychology Press, 2014. 2 

- [19] Kristen Grauman, Andrew Westbury, Eugene Byrne, Zachary Chavis, Antonino Furnari, Rohit Girdhar, Jackson Hamburger, Hao Jiang, Miao Liu, Xingyu Liu, et al. Ego4d: Around the world in 3,000 hours of egocentric video. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 6, 15 

- [20] Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote, et al. Ego-exo4d: Understanding skilled human activity from first-and third-person perspectives. _arXiv preprint arXiv:2311.18259_ , 2023. 6, 15 

- [21] Shreyas Hampali, Mahdi Rad, Markus Oberweger, and Vincent Lepetit. Honnotate: A method for 3D annotation of hand and object poses. In _Computer Vision and Pattern Recognition (CVPR)_ , 2020. 2, 3, 6, 15 

- [22] Shreyas Hampali, Sayan Deb Sarkar, Mahdi Rad, and Vincent Lepetit. Keypoint transformer: Solving joint identification in challenging hands and object interactions for accurate 3D pose estimation. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2 

- [23] Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, YuWei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, and Dieter Fox. DexPilot: Vision-based teleoperation of dexterous robotic hand-arm system. In _International Conference on Robotics and Automation (ICRA)_ , pages 9164–9170. IEEE, 2020. 8 

- [24] Yana Hasson, Gul Varol, Dimitrios Tzionas, Igor Kalevatykh, Michael J Black, Ivan Laptev, and Cordelia Schmid. Learning joint reconstruction of hands and manipulated objects. In _Computer Vision and Pattern Recognition (CVPR)_ , 2019. 2, 3, 15 

- [25] Yana Hasson, Bugra Tekin, Federica Bogo, Ivan Laptev, Marc Pollefeys, and Cordelia Schmid. Leveraging photometric consistency over time for sparsely supervised hand-object reconstruction. In _Computer Vision and Pattern Recognition (CVPR)_ , 2020. 

- [26] Yana Hasson, G¨ul Varol, Ivan Laptev, and Cordelia Schmid. Towards unconstrained joint hand-object reconstruction from rgb videos. In _International Conference on 3D Vision (3DV)_ , 2021. 2 

- [27] De-An Huang, Suraj Nair, Danfei Xu, Yuke Zhu, Animesh Garg, Li Fei-Fei, Silvio Savarese, and Juan Carlos Niebles. Neural task graphs: Generalizing to unseen tasks from a single video demonstration. In _Computer Vision and Pattern Recognition (CVPR)_ , 2019. 3 

- [28] Wenlong Huang, Pieter Abbeel, Deepak Pathak, and Igor Mordatch. Language models as zero-shot planners: Extracting actionable knowledge for embodied agents. In _International Conference on Machine Learning (ICML)_ . PMLR, 2022. 3 

10 

- [29] Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, and Li Fei-Fei. VoxPoser: Composable 3D value maps for robotic manipulation with language models. _arXiv preprint arXiv:2307.05973_ , 2023. 3 

- [30] Juntao Jian, Xiuping Liu, Manyi Li, Ruizhen Hu, and Jian Liu. AffordPose: A large-scale dataset of hand-object interactions with affordance-driven hand pose. _arXiv preprint arXiv:2309.08942_ , 2023. 2, 3, 15 

- [31] Hanwen Jiang, Shaowei Liu, Jiashun Wang, and Xiaolong Wang. Hand-object contact consistency reasoning for human grasps generation. In _International Conference on Computer Vision (ICCV)_ , 2021. 2 

- [32] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 14 

- [33] Christopher A Kurby and Jeffrey M Zacks. Segmentation in the perception and memory of events. _Trends in cognitive sciences_ , 2008. 2 

- [34] Taein Kwon, Bugra Tekin, Jan Stuhmer, Federica Bogo, and Marc Pollefeys. H2O: Two hands manipulating objects for first person interaction recognition. In _International Conference on Computer Vision (ICCV)_ , 2021. 2, 3, 6, 15 

- [35] Jiefeng Li, Siyuan Bian, Ailing Zeng, Can Wang, Bo Pang, Wentao Liu, and Cewu Lu. Human pose regression with residual log-likelihood estimation. In _International Conference on Computer Vision (ICCV)_ , 2021. 6 

- [36] Jiaman Li, Jiajun Wu, and C Karen Liu. Object motion guided human motion synthesis. _ACM Transactions on Graphics (TOG)_ , 2023. 3 

- [37] Kailin Li, Lixin Yang, Zenan Lin, Jian Xu, Xinyu Zhan, Yifei Zhao, Pengxiang Zhu, Wenxiong Kang, Kejian Wu, and Cewu Lu. FAVOR: Full-body ar-driven virtual object rearrangement guided by instruction text. In _AAAI Conference on Artificial Intelligence_ , 2024. 3, 17, 18 

- [38] Kevin Lin, Lijuan Wang, and Zicheng Liu. End-to-end human pose and mesh reconstruction with transformers. In _Computer Vision and Pattern Recognition (CVPR)_ , 2021. 6, 16 

- [39] Shaowei Liu, Hanwen Jiang, Jiarui Xu, Sifei Liu, and Xiaolong Wang. Semi-supervised 3D hand-object poses estimation with interactions in time. In _Computer Vision and Pattern Recognition (CVPR)_ , 2021. 2 

- [40] Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, and Li Yi. HOI4D: A 4d egocentric dataset for category-level humanobject interaction. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2, 6, 15 

- [41] Yun Liu, Haolin Yang, Xu Si, Ling Liu, Zipeng Li, Yuxiang Zhang, Yebin Liu, and Li Yi. TACO: Benchmarking generalizable bimanual tool-action-object understanding. _arXiv preprint arXiv:2401.08399_ , 2024. 3, 15 

- [42] Jun Lv, Wenqiang Xu, Lixin Yang, Sucheng Qian, Chongzhao Mao, and Cewu Lu. HandTailor: Towards highprecision monocular 3D hand recovery. In _British Machine Vision Conference (BMVC)_ , 2021. 6 

- [43] Steven Macenski, Tully Foote, Brian Gerkey, Chris Lalancette, and William Woodall. Robot operating system 2: 

Design, architecture, and uses in the wild. _Science Robotics_ , 7(66):eabm6074, 2022. 13 

- [44] Naureen Mahmood, Nima Ghorbani, Nikolaus F Troje, Gerard Pons-Moll, and Michael J Black. AMASS: Archive of motion capture as surface shapes. In _Computer Vision and Pattern Recognition (CVPR)_ , 2019. 5, 13, 14 

- [45] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, Michelle Lu, Kier Storey, Miles Macklin, David Hoeller, Nikita Rudin, Arthur Allshire, Ankur Handa, et al. Isaac gym: High performance gpu-based physics simulation for robot learning. _arXiv preprint arXiv:2108.10470_ , 2021. 8 

- [46] Andrew T Miller and Peter K Allen. Graspit!: A versatile simulator for robotic grasping. _IEEE Robotics & Automation Magazine_ , 11(4):110–122, 2004. 15 

- [47] Takehiko Ohkawa, Kun He, Fadime Sener, Tomas Hodan, Luan Tran, and Cem Keskin. AssemblyHands: Towards egocentric activity understanding via 3D hand pose estimation. In _Computer Vision and Pattern Recognition (CVPR)_ , 2023. 2, 6, 15 

- [48] OpenAI. GPT-4 technical report. _arXiv preprint arXiv:2303.08774_ , 2023. 5, 7, 17 

- [49] OptiTrack. Motive: Optical motion capture software. https://optitrack.com/software/motive/. 13 

- [50] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani, Timo Bolkart, Ahmed AA Osman, Dimitrios Tzionas, and Michael J Black. Expressive Body Capture: 3D hands, face, and body from a single image. In _Computer Vision and Pattern Recognition (CVPR)_ , 2019. 5, 13 

- [51] Mathis Petrovich, Michael J Black, and G¨ul Varol. Actionconditioned 3D human motion synthesis with transformer VAE. In _International Conference on Computer Vision (ICCV)_ , 2021. 3 

- [52] Mathis Petrovich, Michael J Black, and G¨ul Varol. TEMOS: Generating diverse human motions from textual descriptions. In _European Conference on Computer Vision (ECCV)_ , 2022. 3 

- [53] Yuzhe Qin, Hao Su, and Xiaolong Wang. From one hand to multiple hands: Imitation learning for dexterous manipulation from single-camera teleoperation. _IEEE Robotics and Automation Letters_ , 2022. 2, 8 

- [54] Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong Wang. DexMV: Imitation learning for dexterous manipulation from human videos. In _European Conference on Computer Vision (ECCV)_ , 2022. 2, 8 

- [55] Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay, Dieter Fox, Jesse Thomason, and Animesh Garg. ProgPrompt: Generating situated robot task plans using large language models. In _International Conference on Robotics and Automation (ICRA)_ , 2023. 3 

- [56] Omid Taheri, Nima Ghorbani, Michael J Black, and Dimitrios Tzionas. GRAB: A dataset of whole-body human grasping of objects. In _European Conference on Computer Vision (ECCV)_ , 2020. 2, 3, 6, 13, 15 

- [57] Omid Taheri, Vasileios Choutas, Michael J Black, and Dimitrios Tzionas. GOAL: Generating 4d whole-body motion 

11 

for hand-object grasping. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2, 3, 18 

- [58] Omid Taheri, Yi Zhou, Dimitrios Tzionas, Yang Zhou, Duygu Ceylan, Soren Pirk, and Michael J Black. Grip: Generating interaction poses using spatial cues and latent consistency. In _International Conference on 3D Vision (3DV)_ , 2024. 3 

- [59] Guy Tevet, Sigal Raab, Brian Gordon, Yonatan Shafir, Daniel Cohen-Or, and Amit H Bermano. Human motion diffusion model. _International Conference on Learning Representations (ICLR)_ , 2023. 3, 7 

- [60] Emanuel Todorov, Tom Erez, and Yuval Tassa. MuJoCo: A physics engine for model-based control. _2012 IEEE/RSJ International Conference on Intelligent Robots and Systems_ , 2012. 8 

- [61] Weikang Wan, Haoran Geng, Yun Liu, Zikang Shan, Yaodong Yang, Li Yi, and He Wang. UniDexGrasp++: Improving dexterous grasping policy learning via geometryaware curriculum and iterative generalist-specialist learning. _arXiv preprint arXiv:2304.00464_ , 2023. 8 

   - [70] Hao Zheng, Regina Lee, and Yuqian Lu. HA-ViD: A human assembly video dataset for comprehensive assembly knowledge understanding. _arXiv preprint arXiv:2307.05721_ , 2023. 15 

   - [71] Juntian Zheng, Qingyuan Zheng, Lixing Fang, Yun Liu, and Li Yi. CAMS: Canonicalized manipulation spaces for category-level functional hand-object manipulation synthesis. In _Computer Vision and Pattern Recognition (CVPR)_ , 2023. 2 

   - [72] Zehao Zhu, Jiashun Wang, Yuzhe Qin, Deqing Sun, Varun Jampani, and Xiaolong Wang. ContactArt: Learning 3D interaction priors for category-level articulated object and hand poses estimation. _arXiv preprint arXiv:2305.01618_ , 2023. 2, 3, 15 

   - [73] Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan Russell, Max Argus, and Thomas Brox. FreiHAND: A dataset for markerless capture of hand pose and shape from single rgb images. In _International Conference on Computer Vision (ICCV)_ , 2019. 16 

- [62] Yan Wu, Jiahao Wang, Yan Zhang, Siwei Zhang, Otmar Hilliges, Fisher Yu, and Siyu Tang. SAGA: Stochastic whole-body grasping with contact. In _European Conference on Computer Vision (ECCV)_ , 2022. 2, 3, 17 

- [63] Danfei Xu, Suraj Nair, Yuke Zhu, Julian Gao, Animesh Garg, Li Fei-Fei, and Silvio Savarese. Neural task programming: Learning to generalize across hierarchical tasks. In _International Conference on Robotics and Automation (ICRA)_ , 2018. 3 

- [64] Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan, Hao Shen, Ruicheng Wang, Haoran Geng, Yijia Weng, Jiayi Chen, et al. Unidexgrasp: Universal robotic dexterous grasping via learning diverse proposal generation and goal-conditioned policy. In _Computer Vision and Pattern Recognition (CVPR)_ , 2023. 8 

- [65] Lixin Yang, Xinyu Zhan, Kailin Li, Wenqiang Xu, Jiefeng Li, and Cewu Lu. CPF: Learning a contact potential field to model the hand-object interaction. In _Computer Vision and Pattern Recognition (CVPR)_ , 2021. 14 

- [66] Lixin Yang, Kailin Li, Xinyu Zhan, Jun Lv, Wenqiang Xu, Jiefeng Li, and Cewu Lu. ArtiBoost: Boosting articulated 3D hand-object pose estimation via online exploration and synthesis. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2 

- [67] Lixin Yang, Kailin Li, Xinyu Zhan, Fei Wu, Anran Xu, Liu Liu, and Cewu Lu. OakInk: A large-scale knowledge repository for understanding hand-object interaction. In _Computer Vision and Pattern Recognition (CVPR)_ , 2022. 2, 3, 6, 15, 16 

- [68] Lixin Yang, Jian Xu, Licheng Zhong, Xinyu Zhan, Zhicheng Wang, Kejian Wu, and Cewu Lu. POEM: Reconstructing hand in a point embedded multi-view stereo. In _Computer Vision and Pattern Recognition (CVPR)_ , 2023. 6 

- [69] Haoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du, Yining Hong, and Chuang Gan. 3DVLA: A 3D vision-language-action generative world model. _arXiv preprint arXiv:2403.09631_ , 2024. 7, 8 

12 

# **Supplementary Materials** 

### **Table of Contents** 

- **A** Annotation Details 

   - **A.1** Platform Calibration & Synchronization 

   - **A.2** Data Cleaning 

   - **A.3** Human Pose and Surface 

- **B** Dataset Meta Information 

   - **B.1** Task-specific Subsets 

- **C** Dataset Evaluation 

   - **C.1** Cross-Dataset Validation 

   - **C.2** Physical Property Assessment 

- **D** Tasks and Benchmarks 

   - **D.1** Task-aware Motion Fulfillment 

- **E** Application: Complex Task Completion 

- **F** Dataset Inspection 

   - **F.1** Task List 

   - **F.2** Visualization 

### **A. Annotation Details** 

#### **A.1. Platform Calibration & Synchronization** 

The MoCap system is calibrated via a specialized wand provided by the vendor. The cameras in the multi-camera system are calibrated using ArUco cubes. These cameras are attached with reflective markers to be tracked by the MoCap system. These calibration tools are shown in Fig. 9. The two systems are time synchronized with software synchronization tools bundled in the ROS2 [43]. 

#### **A.2. Data Cleaning** 

In this section, we present a brief description of the process used to clean the reflective marker positions captured by the MoCap system, in preparation for subsequent object pose and human pose computations. Inherent limitations of the MoCap system inevitably lead to errors in the reflective marker positions obtained: in extreme cases of occlusion, the system may fail to detect and record some markers; ghost markers may be included due to unwanted environmental reflections; when two or more markers come into close proximity, the system may incorrectly assign their labels or falsely identify them as a single marker. These limitations lead to the introducing of a manual mechanism for cleaning and post-processing captured data. 

The data cleaning procedure is composed of two components: 1) the MoCap post-processing software; 2) a multi-view interactive editor. We invite three professional annotators for data cleaning. The annotators first sequentially check the location of the captured reflective markers in the MoCap post-processing software [49]. They then proceed to eliminate ghost points, split overlapping markers, correct mislabeled markers, and fill short gaps in the 





Figure 9. **Illustration of Platform Calibration Tools.** The top is the vender-provided calibration wand for the MoCap system. The bottom are the ArUco cubes attached with reflective markers (circled in red). The ArUco patterns are for unifying the camera in the multi-camera system, while the surface-attached reflective markers are used for unifying the cameras with the MoCap system. 

marker trajectories. The annotators, following the order from articulated parts to rigid bodies, human bodies, and both hands, systematically clean the results of the collected markers. Subsequently, the sequences are exported to the multi-view interactive editor. In the editor, annotators verify the cleaned MoCap results and recover the marker positions in extreme occlusion cases through triangulation-based annotations from 2D point locations in multiple views. The results are combined to get the cleaned captured reflective marker positions in the capture volume. 

#### **A.3. Human Pose and Surface** 

We employ a two-stage fitting approach inspired by the application of the MoSH++ algorithm in [15, 44, 56] for the SMPL-X [50] annotations. The first stage registers the subject’s SMPL-X _shape_ parameters and establishes correspondence mapping from the markerset to the surface of SMPLX model. The second stage registers SMPL-X _pose_ parameters for each frame in the sequence. The two-stage fitting pipeline is implemented on PyTorch for its automatic differentiation support and common gradient descent based algorithms are used to solve for both stages. 

**The first stage.** Let _β_<sup>¯</sup> be _shape_ parameters. Let _PM_<sup>(</sup><sup>_c_)</sup><sup>_∈_</sup> R<sup>_NM×_3</sup> be surface marker positions lying in SMPL-X canonical space, where _NM_ is the number of markers in the target markerset. Let _θ_ = _{θi}_ be SMPL-X _pose_ parameters for each frame _i_ when the subject is in T-pose. The first stage could be formulated as an optimization process to minimize the distance between the observed markers 

13 

and the reconstructed markers derived from surface marker positions lying in SMPL-X canonical space, as shown in Eq. (1). 



The main cost is _Erecon_ , which is the distance between the observed markers _PM_ and the reconstructed markers _P_<sup>ˆ</sup> _M_ derived from surface marker positions. Let **_V_**<sup>(</sup><sup>_c_)</sup> be the surface vertices in the canonical space of SMPL-X, **_V_** be the reconstructed surface vertices. The markerset correspondence function _C_ ( _·_ ) uses markerset position _PM_<sup>(</sup><sup>_c_)andsur-</sup> face vertices **_V_**<sup>(</sup><sup>_c_)</sup> in canonical space to recover the markerset positions _P_<sup>ˆ</sup> _M_ from the current reconstructed surface vertices **_V_** . It first projects the markers in canonical space _P_<sup>(</sup><sup>_c_)</sup> _M_<sup>into local frames formed by the surface vertices to get</sup> the vertex index _IM_ and coefficients in local frames _CM_ . Then it uses the index to recover frames on posed vertices **_V_** and the coefficients in local frames to recover marker positions on the posed SMPL-X bodies. _Erecon_ can then be expressed as in Eq. (2). 



_E_ prior(b)� _θ_ �, _E_ plau(h)� _θ_ �, and _E_ reg� _θ, β, PM_<sup>(</sup><sup>_c_)</sup> � are auxiliary cost terms. _E_ prior(b)� _θ_ � is an auxiliary term that minimizes negative log-likelihood of human body poses computed by prior from pre-existing datasets following the practice in [44]. _E_ plau(h)� _θ_ � is an implementation of anatomy loss in [65] on the SMPLX model, designed to prevent distortion in the pose of the human body during the fitting process, enhancing its physical plausibility. _E_ reg� _θ, β, PM_<sup>(</sup><sup>_c_)</sup> � is an auxiliary term that regularize the optimization variables. **The second stage.** In the second stage, we fit the subject’s pose _θ_ = _{θt}_ throughout the interaction process based on the shape _β_<sup>¯</sup> and marker correspondence _C_ ( _·_ ) obtained in the first stage. For each frame _t_ in the sequence, we optimize the subject’s SMPL-X _pose_ parameter _θt_ to minimize a combination cost composed of observed marker reconstruction error _E_ recon� _θt_ �, body pose prior _E_ prior(b)� _θt_ �, hand anatomy abnormality _E_ plau(h)� _θt_ �, hand-object intersection _E_ plau(ho)� _θt_ � and other auxiliary regularization costs. min _θt_<sup>_E_=</sup><sup>_λ_1</sup><sup>_E_recon</sup> � _θt_ � + _λ_ 2 _E_ prior(b)� _θt_ � + _λ_ 3 _E_ plau(h)� _θt_ � + _λ_ 4 _E_ plau(ho)� _θt_ � + _λ_ 5 _E_ reg� _θt_ � (3) 

_E_ plau(h)� _θt_ �, _E_ prior(b)� _θt_ �, and _E_ plau(h)� _θt_ � are the same cost terms as in the first stage. _E_ plau(ho) penalizes the penetration 

and intersection between the interacting hands and objects by sampling internal points inside hand meshes and computing the sum of their signed distance function values of the objects. _E_ reg� _θt_ � not only includes regularization terms for the optimization variables but also contains velocity regularization terms to keep the smoothness of the annotated trajectories. 

**Optimization** We implement the two-stage fitting pipeline on PyTorch for its automatic differentiation support. We adopt Adam [32] as the optimizer to solve for both stages, as it is widely applied and suitable for non-convex cost terms introduced in both stages. We propose an early stopping mechanism for better running speed of the second stage: if there is no significant reduction in the fitting cost over a number of consecutive frames that exceeds a specific threshold, the optimization process will be terminated. 

### **B. Dataset Meta Information** 

#### **B.1. Task-specific Subsets** 

Since OAKINK2 is intended for various types of tasks, we create multiple subsets with different strategies for sample selection and data organization tailored to each specific task. To obtain these subsets, we apply a few heuristics to determine whether each sample meets the requirements of the task it needs to support. For instance, the visibility of hands or objects in image samples is essential for supporting related vision tasks. We verify the individual and combined segmentation masks for hands and objects in the images. If the proportion of the combined segmentation mask to its individual counterpart exceeds a certain threshold, we consider the instance as _visible_ in the current frame. We regard the object to interact as _grasped_ if it is close enough to hands (minimal distance _≤_ 5 mm) and _lifted_ (height displacement to the initial state _≥_ 5 mm). 

We show the features and the construction methods for task-specific subsets in the following list. 

**OAKINK2-H-SV** Subset for hand reconstruction from single-view images. We select views that the subjects’ hands are _visible_ to form this subset. This subset supports task single-view Hand Mesh Recovery. 

**OAKINK2-H-MV** Subset for hand reconstruction from multi-view images. We select combined views from different cameras as a single sample in this subset if the subjects’ hands are _visible_ in a majority of camera views. This subset supports task multi-view Hand Mesh Recovery. 

**OAKINK2-HO** Subset for hand-object pose estimation or reconstruction from images. We select views that the subjects’ hands are _visible_ and the object is _grasped_ to form this subset. 

**OAKINK2-Grasp** Subset for grasps on the objects. We 

14 

|Dataset|image<br>mod.|resol|ution|#frame #|views|#subj|#obj|3D<br>gnd.|real /<br>syn.|label<br>method|hand<br>pose|obj<br>pose|afford.<br>inter.|dynamic<br>inter.|long-<br>horizon|task<br>decomp.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EPIC-KITCHEN-100 [13]|✓|_∼_<br>||20M<sup>_†_</sup><br>|1|37|–|✗|–|–|✗|✗|✗|✗|✓|✓|
|Ego4D [19]|✓|_∼_|<sup>_‡_</sup>|_∼_<sup>_†_</sup>|1|931|–|✗|–|–|✗|✗|✗|✗|✓|✓|
|HA-ViD [70]|✓|1280|_×_720|1.5M|3|30|40|✗|–|–|✗|✗|✗|✗|✓|✓|
|FPHAB [16]|✓|1920_×_|1080|105K|1|6|4|✓|real|mocap|✓|✓|✓|✓|✗|✗|
|ObMan [24]|✓|256_×_|256|154K|1|20|3K|✓|syn|simulate|✓|✓|✗|✗|✗|✗|
|YCBAfford [12]|✓|–||133K|1|1|21|✓|syn|manual|✓|✗|✗|✗|✗|✗|
|HO3D [21]|✓|640_×_|480|78K|1-5|10|10|✓|real|auto|✓|✓|✗|✓|✗|✗|
|ContactPose [3]|✓|960_×_|540|2.99M|3|50|25|✓|real|auto|✓|✓|✓|✗|✗|✗|
|GRAB [56]|✗|–||1.62M|–|10|51|✓|real|mocap|✓|✓|✓|✓|✗|✗|
|DexYCB [8]|✓|640_×_|480|582K|8|10|20|✓|real|crowd|✓|✓|✗|✓|✗|✗|
|H2O [34]|✓|1280|_×_720|571K|5|4|8|✓|real|auto|✓|✓|✓|✓|✗|✗|
|HOI4D [40]|✓|1280|_×_800|3M|1|9|1000|✓|real|crowd|✓|✓|✓|✓|✗|✗|
|ARCTIC [15]|✓|2800_×_|2000|2.1M|9|10|11|✓|real|mocap|✓|✓|✓|✓|✗|✗|
|ContactArt [72]|✓|–||332K|–|–|80|✓|real|transfer|✓|✓|✗|✓|✗|✗|
|AssemblyHands [47]|✓|1920_×_|1080|3.03M|12|34|–|✓|real|semi-auto|✓|✗|✓|✓|✓|✓|
|AffordPose [30]|✗|–<br>||–<br>|–|–|641|✓|syn|manual|✓|✓|✓|✗|✗|✗|
|TACO [41]|✓|4096_×_<br>|3000<sup>_‡_ </sup><br>|5.2M<br>|13|14|196|✓|real|auto|✓|✓|✓|✓|✗|✗|
|Ego-Exo4D [20]|✓|_∼_|<sup>_‡_</sup>|_∼_<sup>_†_</sup>|5-6|839|–|✓|real|semi-auto|✓|✗|✗|✓|✓|✓|
|OakInk-Image [67]|✓|848_×_|480|230K|4|12|100|✓|real|crowd|✓|✓|✓|✓|✗|✗|
|OakInk-Shape [67]|✗|–||–|–|–|1700|✓|real|transfer|✓|✓|✓|✗|✗|✗|
|**OAKINK2**|✓|848_×_|480|**4.01M**|4|9|75|✓|real|mocap|✓|✓|✓|✓|✓|✓|



Table 4. **A cross-comparison among various public datasets.** _∼_ : The value is either not provided on the paper or measured in a different unit. _†_ : Datasets measure in record time rather than number of captured frames. In particular, EPIC-KITCHEN-100 contains more than 100 hours of video, Ego4D 3670 hours, and Ego-Exo4D 1422 hours. They are larger in scale than any other dataset listed in the table. _‡_ : Dataset has a mixed resolution. 

**Legend** : 

**image mod.** : Image Modality. ✓ means real image captures; ✓ means synthetic (rendered) images; ✗ means no image modality provided. **3D gnd.** : 3D grounding. ✓ means the dataset contains 3D grounding annotations; ✗ means the dataset is 2D only. **real / syn.** : Interaction is real / synthetic. Here syn indicates the interactions come from certain grasp/interaction synthesizer. **label method** : Label Method of 3D grounding information. For synthetic interactions, “simulate” indicates interactions are retrieved from physical-based grasp simulators, _e.g_ . GraspIt! [46]; “manual” indicates interactions are labeled with human labor. For real interactions, “mocap” indicates the interactions are captured by MoCap systems; “crowd” indicates the interactions are derived from crowd-source keypoint annotations; “auto” indicates the interactions are retrieved from automatic annotation pipelines; “semi-auto” indicates a hybrid of “crowd” and “auto” methods. 

**afford. inter.** : Affordace-based Interaction. ✓ means the interactions captured are affordance-aware and explicitly labeled; ✓ means the interactions are afforance-aware but grouped in coarse-grained labels like intentions; ✗ means the interactions are not organized by object afforances. 

**dynamic inter.** : Dynamic Interaction. ✓ means the dataset captures dynamic sequence of hand-object interactions; ✗ means the dataset captures static grasps that do not change during the interaction process. 

**long-horizon** : Long-horizon Tasks. As in the main text, ✓ means the dataset contains captured interactions that involved more than one object afforances; ✗ vice versa. 

**task decomp.** : Task Decomposition. As in the main text, ✓ means the dataset contains annotations that decomposition a complex task into multiple segments; ✗ vice versa. 

select frames that the object is _grasped_ to form this subset. 

**OAKINK2-Motion-Approach&Retreat** Subset for the interaction process that the subjects approach and grab the object for future tasks. We select frames from the sequence in one _Primitive Task_ that cover the process of _approach_ and _grasp_ the object are collected to form this subset. This subset provides auxiliary information in Task-aware Motion Fulfillment and Object Trajectories Retrieval from Oracle Queries in Complex Task Completion. 

**OAKINK2-Motion-Task** Subset for the interaction pro- 

cess that the subjects complete a task and fulfill one object affordance. We select frames from the sequence in one _Primitive Task_ that cover the process from the _grasp_ of the object to the _completion_ of the task are collected to form this subset. This subset supports Task-aware MotionFulfillment. 

### **C. Dataset Evaluation** 

Annotation on 3D hand keypoints undergo cross-dataset validation with a reconstruction model, while the 3D poses 

15 



<!-- Start of picture text -->
To<br>tured<br>be<br>action<br>ity<br>pare<br>OAKINK2<br><!-- End of picture text -->

improvement on these metrics, verifying that OAKINK2 complements existing datasets and boosts existing models. 

|**Train**|**Test**|**PA-MPJPE**(_mm_)_↓_|**PA-MPVPE**(_mm_)_↓_|
|---|---|---|---|
|1) FreiHAND|OakInk-image (SP2)|12.07|11.96|
|2) OAKINK2-H-SV|OakInk-image (SP2)|12.60|11.04|
|**1) & 2) mixture**|OakInk-image (SP2)|**10.94**|**9.67**|



Table 5. **Cross dataset validation** for OAKINK2. 

#### **C.2. Physical Property Assessment** 

To evaluate the quality of the 3D poses associated with grasping actions in OAKINK2, we inspect several physicalbased metrics that assess the feasibility and stability of captured hand-object interactions. We restrict the samples to be evaluated based on certain rules (the objects in interaction need to be grasped and lifted), ensuring that these physics-based quality metrics accurately reflect the quality of the dataset during the interaction process. We compare OAKINK2-Grasp (-G.) with two subsets of OakInk: OakInk-Core and OakInk-Shape (Tab. 6). We observe that, despite the use of the mocap system as the primary annotation method for easily scaling up the capture process, OAKINK2 still achieved annotation quality on par with OakInk built upon the hybrid of manual and mocap annotation. More qualitative visualizations of OAKINK2 are provided in Fig. 14. 

|**Metrics**|**OAKINK2-G.**|**OakInk-Core**|**OakInk-Shape**|
|---|---|---|---|
|_Penet. Depth. cm↓_<br>|0.25|0.18|0.11|
|_Solid Intsec. Vol. cm_<sup>3</sup>_↓_|0.61|1.03|0.62|
|_Sim. Disp. Mean cm↓_|1.83|0.98|0.94|
|_Sim. Disp. Std cm↓_|1.16|1.74|1.62|



Figure 10. **Distribution of** **_Primitive Task_ demonstrations.** The sub-figure above displays the proportion of _Primitive Task_ demonstrations across various scenarios within the entire OAKINK2 dataset, with frequently occurring _Primitive Tasks_ highlighted. The sub-figure below presents a list of _Primitive Tasks_ recorded in OAKINK2, along with the illustration of their corresponding quantity distribution. A list of all recorded _Primitive Tasks_ and _Complex Tasks_ can be found at Tab. 7 and Tab. 8. 

associated with grasping actions are examined for their physical property integrity. 

#### **C.1. Cross-Dataset Validation** 

We perform cross-dataset validation to verify the consistency of 3D hand keypoint annotations in OAKINK2 with pre-existing datasets. We train a single-view hand mesh recovery model [38] separately on three different training schemes: FreiHAND [73] only, OAKINK2-H-SV only, and a mixture of these two sets. We evaluate MPJPE and MPVPE after Procrustes analysis on OakInk-image (SP2) [67], and the results shown in Tab. 5 indicates a consistent 

Table 6. **Quality assessment** of OAKINK2. 

### **D. Tasks and Benchmarks** 

#### **D.1. Task-aware Motion Fulfillment** 

**Train-Val-Test Split** Following the same practice as HMR, we partition the subsets at the sequence level, maintaining the proportion of samples in train/val/test sets at approximately 70%, 5%, and 25%, in alignment with OakInk. 

##### **Evaluation Metric Details** 

**CR, Contact Ratio.** This metric measures the ratio of the frames within the motion trajectories where the hand-object contact (minimum distance) is within a 5 mm threshold. **SIV, Solid Intersection Volume.** This metric measures how much space intersection occurs during estimation. We voxelize the object mesh into 100<sup>3</sup> voxels, and calculate the sum of the voxel volume inside the hand surface. 

##### **PSKL-J, Power Spectrum KL divergence of Joints.** 

This metric reflects the smoothness of the generated 

16 

motion. It measures the acceleration distribution variance between **predicted** and **g.t.** joint sequences, reporting results in both directions. We reference our implementation on [37, 62]. The notable difference is that we use hand joints for measurement, resulting in a distinct range of metric values compared to full-body joints. 

**FID, Fr´echet Inception Distance score.** This metric evaluates the realism of the generated motion trajectory. We develop a motion feature extractor based on the transformer encoder architecture. The embedding is obtained by appending a trailing token to hand motion trajectories. The embedding we use for each motion is of 64 dimensions. The encoder is trained by the classifying motion trajectories into their corresponding categories. We apply the encoder to both ground-truth trajectories and generated trajectories and compute Fr´echet Inception Distance between them for motion realism evaluation. 

### **E. Application: Complex Task Completion** 

**Test Scene Generation.** To evaluate the ability of the oracle-facilitated three-stage method described in the main text to accomplish complex tasks, we derive a set of test environments by perturbing the object positions within the complex scenarios contained in OAKINK2 dataset without altering the task objectives **text** goal and the descriptions of the objects’ states _{_ **text** obj _}_ . 

We utilize ground truth annotations to generate variations in the test scenes. We treat specific object sets as clusters and place them in randomized locations. Objects within the same cluster share a unified offset to ensure collective randomization. This is crucial when groups of objects must maintain coherence in their movements. The process of randomization comprises four distinct _wander_ steps. This helps prevent obstruction caused by other objects when an object ventures in a random direction. Hence, each object gains an enhanced opportunity to navigate around other structures within its environment. Each object’s final location results from the cumulative effect of these four _wander_ steps. Within each _wander_ step, a maximum of eight iterations are employed for collision prevention between objects by reducing the step length to half. 

**Prompt Generation.** We implement Primitive Planning by tweaking the Large Language Model – GPT-4 [48] in this study – so that it can generate Python code based on narrative prompts describing the current scenario and task objectives. The language model’s role is to interpret this description, identify key objects involved in the task, determine the appropriate object affordance and trajectory, and generate suitable instances of _Primitives_ execution organized into a feasible sequence. 

Our approach to overcoming these challenges involves the design of a prompt template that incorporates both scene 

and task descriptions as referenced earlier. This template not only explicates the underlying code framework but also provides a sample of scenario-independent code. We further prompt the Language Learning Model (LLM) to produce a code implementation as a response, as opposed to providing an explanatory narrative of coding procedures. 

Concerning the underlying code framework, to ensure robust and coherent code generation, we propose an EntityComponent-System (ECS) architecture. This structure encourages a decoupling of components, here referred to as data or state, from the system, representing the _Primitives_ in our context. This approach endows us with the capability of generating uniformly styled code implementations, where the layout involves instantiating object entities, loading the affordance as a component, and submitting the _Primitives_ to the execution system. 

**Evaluations of Primitive Planning.** We employ a checker based on the _Primitive_ Dependency Graph provided along with the _Complex Tasks_ to be planned to benchmark the success rate of the program that is supposed to complete the task target. We analyze the checker results and observe an overall success rate of 36% in the generation of Planning codes. Concerning the number of _Primitives_ incorporated within the _Complex Tasks_ , we observed differing success rates. Specifically, in those _Complex Tasks_ incorporating equal to or less than three _Primitives_ , a success rate of 44% was obtained Conversely, in the _Complex Tasks_ category incorporating between three and five _Primitives_ , the success rate dropped to 20%. Notably, no success was recorded in _Complex Tasks_ incorporating more than five _Primitives_ . The results demonstrate that in the current setting, the Large Language Model (LLM) is adequate to handle relatively simpler _Complex Tasks_ . However, in contexts of highly complex _Complex Tasks_ , the LLM struggles to accurately comprehend the relationships and dependencies between objects’ affordances and the corresponding _Primitives_ . 

**Demo Planning Result.** We provide a review of the results of a completed _Complex Task_ within one of the constructed test scenes. The python programs generated are listed as Listing 2. This code joins all the relevant objects and their associated affordances, proceeding to execute the _Primitives_ in the precise required order. We have also included an example of a failed case, presented as Listing 3, which highlights a failure in the execution of _Primitive_ Planning. This failure is characterized by a superfluous _Primitive_ that fulfills an unnecessary object affordance that blocks the execution path. 

**Alternative Motion Generation for Complex Task Completion.** In addition to the TaMF-based motion generation approach presented in the main text, we explore an alternative strategy that leverages keyframe generation and motion 

17 





Figure 11. **Oracle Trajectories and Motion Generation** This figure illustrates the successful _Complex Task_ completion of two Primitive Tasks. The top pair of images depict the oracle trajectories, while the bottom pair represents the sequential motion generated. 

in-betweening as motion generator for Complex Task Completion. We adopt GNet and MNet in GOAL [57] and INet in FAVOR [37]. These models follow the pattern of first generating hand-object interactions in key frames, and then generating intermediary interaction trajectories within these frames. The generation contains three stages. In the first stage, GNet generates static grasps based on the object’s initial and terminal poses. Subsequently, MNet generates motion trajectories to reach the object and retreat from the object. In the final stage, INet is fed with alternating object poses from the object motion trajectory to generate the in-between motion during the interaction process. The object oracle trajectories result in a sequence of human body movements depicted in Fig. 11. The left-hand images of Fig. 11 illustrate the sequential actions of approaching and utilizing a knife to cut a pear, representing the affordance _cut_ associated with the knife under the _Primitive Task_ category. The right-hand images illustrate the sequence of lifting a bottle and pouring its contents into a pan, indicative of the _Primitive Task_ affordance, _pour_ , as related to the bottle. 

18 

### **F. Dataset Inspection** 

#### **F.1. Task List** 

Table 7. Collected _Affordances_ and Designed _Primitive Tasks_ . 

|**Scenario**<br>kithn tbl|**Affordance**<br><bd<br>>|**Affordance Instantiation**<br>**_Primitive Task_**<br>|
|---|---|---|
|ce ae|e rearrange,<br><br><store securely, sth><br><containsth>|_rearrange_|
||, <br>|<flow in, sth><br>_pour_<br><pour, sth><br>_pour_<br><shake, sth><br>_shake_|
||<secure, sth><br><grip, sth><br><scoop, sth><br><scrape, sth><br><cut, sth><br><stir, sth><br><spread, sth><br><assemble into, sth><br><wipe, sth><br><heat with microwave, sth><br><contain, sth><br><securesth>|<screw into, sth><br>_screw_<br><unscrew from, sth><br>_unscrew_<br><cap onto, sth><br>_cap_<br><uncap from, sth><br>_uncap_<br>_grip_<br>_scoop_<br>_scrape_<br>_cut_<br>_stir_<br>_spread_<br>_assemble_<br>_wipe_<br><place inside, sth><br>_place inside_<br><take outside, sth><br>_take outside_|
||, <br><controlsth>|<shut, sth><br>_close gate_<br><open, sth><br>_open gate_|
||,|<be pressed,<br>~~>~~<br>_press button_|
||ihh|<trigger, sth><br>_trigger lever_|
||<weg, st><br>||
||<support, sth>|_place onto_|
|study room table|<be rearranged,<br>><br><store securely, sth><br><containsth>|_rearrange_|
||, <br><securesth>|<place inside, sth><br><take outside, sth>|
||,|<cover, sth><br>_put on lid_<br><uncover, sth><br>_remove lid_<br><shut, sth><br>_pull out drawer_<br><br>|
|||<open, sth><br>_push in drawer_|
||<illuminate, sth>||
||<connect to, sth>|<connect to, power socket><br>_plug in power plug_<br><deconnect from, power socket><br>_remove power plug_<br><connect to, usb><br>_insert usb_|
|||<deconnect from, usb><br>_remove usb_<br><connect to, lightbulb socket><br>_insert lightbulb_<br><br>|
||<shearpaper>|<deconnect from, lightbulb socket><br>_remove lightbulb_|
||, <br><secure, sth>|<cap, pen tip><br>_cap the pen_<br><uncaenti><br>_removetheenca_|
||<write/draw, sth>|p, p p<br>  _p p_<br>_write on paper_<br>_write on whiteboard_|
||<brush, whiteboard><br><be sharpen by, sth>|_brush whiteboard_<br>_sharpen pencil_|
||<sharpen, pencil><br><staple together, paper><br><be written/drawn by, pen/pencil>|_sharpen pencil_<br>_staple paper together_<br>_write on paper_|
|||_writeonwhiteboard_|
||<be sheared by, scissors>|<br>_shear paper_|
||<be stapled together by, stapler><br><br>|_staple paper together_<br>|
||<be turn,<br>~~>~~|_close book_<br>|
||<displaysth>|_open book_|
||, <br><protect, sth>||
|||<open, laptop lid><br>_open laptop lid_|
||<control, sth>|<close, laptop lid><br>_close laptop lid_<br>_use keyboard_<br>_use mouse_|



19 

Table 7. Collected _Affordances_ and Designed _Primitive Tasks_ . 

|**Scenario**|**Affordance**|**Affordance Instantiation**|**_Primitive Task_**<br>_mntll_|
|---|---|---|---|
||<cultivate, flowers>||_use gaecoroer_<br>_put flower into vase_|
||<be cultivated in, sth>||_put flower into vase_|
|demo chem lab|<be rearranged,<br>>||_rearrange_|
||<store securely, experiment<br>substances><br><contain, experiment substances>|||
|||<flow in, experiment substances>|_pour in lab_|
|||<pour, experiment substances>|_pour in lab_|
|||<shake, experiment substances>|_shake lab container_|
||<secure, experiment substances>|||
|||<screw into, lab container>|_screw_|
|||<unscrew from, lab container>|_unscrew_|
|||<cap onto, lab container>|_cap_|
|||<uncap from, lab container>|_uncap_|
||<contain, experiment substances>|||
|||<flow in, experiment substances>|_pour in lab_|
|||<pour, experiment substances>|_pour in lab_|
|||<shake, experiment substances>|_shake lab container_|
||<be heated by, alcohol lamp>||_heat beaker/flask_|
||||_heat test tube_|
||<stir, experiment substances>||_stir experiment_<br>_substances_|
||<be ignited,<br>>||_ignite alcohol lamp_|
||<heat, lab container>||_heat beaker/flask_|
||||_heat test tube_|
||<put off, alcohol lamp>||_put off alcohol lamp_|
||<ignite, alcohol lamp>||_ignite alcohol lamp_|
||<clamp, test tube>||_hold test tube_|
||<conduct heat to, lab container>||_place asbestos mesh_|
||<support, lab container>||_place asbestos mesh_|
|bathroom table|<be rearranged,<br>><br><contain, sth>||_rearrange_|
|||<squeeze out, sth>|_squeeze tooth paste_|
||<secure, sth>|||
|||<shut, sth>|_flip open tooth paste_|
||||_cap_|
|||<open, sth>|_flip close tooth paste_<br>_cap_|



Table 7. Collected _Affordances_ and Designed _Primitive Tasks_ . The first column records the manipulation scenarios. The second column lists collected affordances of object instances and parts. The affordances of object parts are indented below their parent instance-level affordance. The third column lists the instantiations of object affordances. These instantiations are bound to certain object attributes, _e.g_ . <screw, sth> is bound to actual screws on the bottle’s opening and cap. The fourth column lists the designed _Primitives_ corresponding to the affordances. Some _Primitives_ are set to gray for these _Primitives_ are difficult to demonstrate and capture in individual. Demonstrations of these tasks are embedded within _Complex Task_ demonstrations. 

|**Scenario**|**_Complex Task_**|
|---|---|
|kitchen table|heat with microwave oven; weigh with scale; scoop and pour; scoop and grip; scoop and wipe; scoop and scrape; pour and<br>stir; grip and pour; pour and arrange; weigh with scale and pour; pour and scrape; grip and arrange; weigh with scale and<br>grip; grip and wipe; pour and grip; clean the kitchen table; prepare a cup of hot sweet drink; prepare a bowl of hot soup with<br>salt; prepare a cup of hot sweet fruit tea; prepare a chilled apple platter; prepare a savory fruit salad; prepare a baked sweet<br>donut with sauce; prepare a baked sweet donut with apple slices and jam; prepare a savory baked sweet donut; prepare a<br>cheese-baked sweet donut with tomato sauce; prepare savory baked apple slices with cheese; prepare a chilled fruit platter;<br>make a baked sandwich with a filling of donut and salt; make a sandwich with a filling of tomato sauce and sugar; make a<br>sandwich with a filling of apple slices and donut, adding tomato sauce, mustard sauce, salt, and sugar; make a baked sandwich<br>with a filling of cheese and donut, adding tomato sauce; scoop, unscrew, pour, and screw; grip and scoop; scoop and scoop;<br>scoop and arrange; weigh with scale and scoop; cut and scoop; cut and pour; grip and stir; grip and scrape; cut and grip; grip<br>and assemble; stir and arrange; stir and scrape; scrape and arrange; weigh with scale and assemble; unscrew and pour; pour<br>and screw; uncap and scrape; scrape and cap; uncap, scrape, and cap; scrape and assemble; assemble and arrange; unscrew<br>and heat with microwave; pour and heat with microwave; heat with microwave and pour; heat with microwave and stir; heat<br>with microwave and assemble; cut and heat with microwave; uncap, pour, and cap; prepare a cup of chilled green tea; prepare<br>a cup of apple green tea; prepare a cup of mixed flavor fruit juice; prepare a cup of savory fruit juice milk tea; prepare a cup<br>of pear milk tea with fruit jam; prepare a cup of savory honey fruit juice milk tea; prepare a cup of savory strawberry orange<br>juice mixed with milk; uncap and scoop; prepare a cup of wine; prepare a cup of milk tea; prepare a cup of chilled fruit tea;<br>prepare a cupof honeycoffee; prepare a cupof chilledjuice milk withjam; prepare a cupof chilled sweet milk tea;|



20 

|**Scenario**|**_Complex Task_**|
|---|---|
|study room table|put into box; take out of box; put into drawer; take out of drawer; ready the laptop on the desktop for work; tidy up the<br>desktop with the laptop after work; ready the laptop on the desktop for entertainment; illuminate the desktop; sharpen the<br>pencil and write; tidy up the desktop with the laptop after entertainment; tidy up the desktop after paper-cutting; write and<br>bind the paper; design and cut out rectangle shape on the paper; press button and open laptop; press button and close laptop;<br>press button and put into box; press button and take out of box; press button and remove power plug; insert usb and plug<br>in power plug; tidy up the desktop after writing; plug in power plug and press button; design and cut out flower shape on<br>the paper; design and draw on the paper; ready the laptop and the lamp on the desktop for work; design, write and bind the<br>paper; ready the desktop for drawing; take out of drawer, insert usb, and open laptop; put into drawer and put into box; put<br>into drawer, put into box, and close laptop; remove usb, close laptop, and put into drawer; tidy up the desktop after drawing;<br>cut and bind paper; ready the laptop and the lamp on the desktop for entertainment; design, draw and cut out flower shape on<br>thepaper;design,draw and bind thepaper;tidyupthe desktopafter binding paper;|
|demo chem lab|transfer and heat liquid in beaker; transfer and heat liquid in conical flask; heat liquid in beaker and transfer liquid; heat<br>liquid in conical flask and transfer liquid; transfer and heat liquid in beaker and transfer liquid out; heat liquid in test tube and<br>transfer liquid; prepare solution through heating; mix liquid; pour in lab and shake in lab; pour in lab and pour in lab; pour in<br>lab and heat test tube; pour in lab and light lamp; stir in lab and pour in lab; stir in lab and heat beaker; shake in lab and pour<br>in lab; shake in lab and heat test tube; shake in lab and heat beaker; heat beaker and put off lamp; heat test tube and put off<br>lamp; light lamp and put off lamp; put off lamp and pour in lab; put off lamp and stir in lab; put off lamp and shake in lab;<br>heat beaker and stir in lab; stack mesh and heat beaker; light lamp and heat beaker; light lamp and heat test tube; pour in lab,<br>shake in lab, and heat test tube; stir in lab, pour in lab, and shake in lab; light lamp, heat beaker, and put off lamp; light lamp,<br>heat test tube, and put off lamp; stack mesh, light lamp, and heat beaker; light lamp, heat beaker, and stir in lab; light lamp,<br>heat test tube, and shake in lab; pour in lab, pour in lab, and pour in lab; pour in lab, shake in lab, and pour in lab; stir in lab,<br>stack mesh, and heat beaker; shake in lab, pour in lab, and heat test tube; shake in lab, heat test tube, and pour in lab; heat<br>beaker, stir in lab, and pour in lab; heat beaker, put off lamp, and pour in lab; heat beaker, put off lamp, and stir in lab; heat<br>test tube, put off lamp, and shake in lab; pour in lab, stir in lab, and pour in lab; pour in lab, pour in lab, pour in lab, pour in<br>lab, and pour in lab; stir and transfer liquid; heat liquid in beaker; heat liquid in test tube; put off lamp, pour in lab, and shake<br>in lab; put off lamp,stir in lab,andpour in lab; prepare solution in beaker;|
|bathroom table|squeeze toothpaste tube to tooth brush;squeeze toothpaste and stack tooth brush; prepare for teeth brushing.|



Table 8. Recorded _Complex Tasks_ . We list the names of the recorded _Complex Tasks_ here. 

#### **F.2. Visualization** 

21 



<!-- Start of picture text -->
���� ���� ��� ���� ������ �������� �����<br>����� ��� ������� ����� ���� ������ ������������<br>������������ ������������ ��������� ���������� ������������ �������������� ���������������<br>���������� ���������� ������������ ������������ ������������ ������������ ������������<br>������������������� ��������������������� ��������������� ���������������� ���������������� �����������<br>������������������ ����������� �������������� ������������������� �������������� ��������������<br>����������������� ������������������ ���������� ���������� ���������������� ����������������<br>�������������������������� ������������������� ������������������� ������������������� ��������������������������<br>������������������� ���������������� �������������� ������������������������ ������������������������� �������������������<br>Figure 12. Primitives  visualization.<br>22<br><!-- End of picture text -->























































































































Figure 13. **Object visualization.** 

23 



Figure 14. **Dataset visualization.** Human bodies and objects within the scene are rendered onto the captured raw images for visualization. 

24 

1 You are a python programming expert and you are asked to finish a certain bimanual robotics task. 2 3 Scene Description: 4 {scene_desc} 5 6 Task Description: 7 {task_desc} 8 9 The Structure of the code is a ECS architecture defined as 10 ECS File 11 12 The **entities** are defined as 13 **Entity** File 14 15 The **components** are defined as 16 **Component** File 17 18 The **systems** are defined as 19 **System** File 20 21 The task is to finish the methods called "exec_task" in this class {read_from_file(scene_path)} 22 23 You need to query the raw 3d object from the scene which contains object name as keys in scene description and you can use them to query different type of information from the scene. Build them into Objects and instantiate PrimitiveTasks to finish the job. 24 Leave the objects not mentioned in the task description as they are. 25 Avoid using any methods with underscore prefix. Explicitly specify the keyword arguments instead of using **kwargs. 26 For example: 27 28 an_object = Object(’object_name’, 29 geometry=self.query_geometry_info(’object_name’), 30 ... 31 ) 32 33 a_primitive_task = PrimitiveTask(an_object.affordance.get_primitive_task_info(’primitive_task_name’)) 34 35 a_primitive_task.execute(src_object=an_object, tgt_object=another_object, trajectory= **oracle** . **generate** (a_primitive_task) ) 36 37 Explanation of the code is unnecessary. Putting everything in method implementation would be admired. Respond with exec_task(self) itself. 

Listing 1. Prompt Template. **Entity** marks object instances present in the scene. **Component** accommodates information of objects’ initial status and affordances. **System** accommodates the interface of motion generators for _Primitives_ . The example code incorporated in the prompt demonstrates the interface of **oracle queries** for object motion trajectories. 



<!-- Start of picture text -->
1 # Task<br>2 # The task is to cut the pear into pieces which to be put in the pan and add some season.<br>3<br>4 # Scene<br>5 # In a kitchen, on a table, these objects are placed: [knife, pear, bottle, pan]<br>6 def exec_task(self):<br>7 # making an object for knife<br>8 knife = Object(’knife’,<br>9 geometry=self.query_geometry_info(’knife’),<br>10 state=self.query_state_info(’knife’),<br>11 affordance=self.query_affordance_info(’knife’)<br>12 )<br>13<br>14 # making an object for pear<br>15 pear = Object(’pear’,<br>16 geometry=self.query_geometry_info(’pear’),<br>17 state=self.query_state_info(’pear’),<br>18 affordance=self.query_affordance_info(’pear’)<br>19 )<br>20<br>21 # making an object for pan<br>22 pan = Object(’pan’,<br>23 geometry=self.query_geometry_info(’pan’),<br>24 state=self.query_state_info(’pan’),<br>25 affordance=self.query_affordance_info(’pan’)<br>26 )<br>27<br>28 # making an object for bottle<br>29 bottle = Object(’bottle’,<br>30 geometry=self.query_geometry_info(’bottle’),<br>31 state=self.query_state_info(’bottle’),<br>32 affordance=self.query_affordance_info(’bottle’)<br>33 )<br>34<br>35 # creating primitive task for cutting<br>36 cut_pear = PrimitiveTask(knife.affordance.get_primitive_task_info(’cut’))<br>37 cut_pear.execute(src_object=knife, tgt_object=pear, trajectory=oracle.generate(cut_pear))<br>38<br>39 # creating primitive task for placing pear inside the pan<br>40 put_task = PrimitiveTask(pear.affordance.get_primitive_task_info(’put_inside’))<br>41 put_task.execute(src_object=pear, tgt_object=pan)<br>42<br>43 # create primitive task for adding season<br>44 add_season = PrimitiveTask(bottle.affordance.get_primitive_task_info(’pour’))<br>45 add_season.execute(src_object=bottle, tgt_object=pan, trajectory=oracle.generate(add_season))<br><!-- End of picture text -->

Listing 2. Primitive Task Planning Success Example. 

25 



<!-- Start of picture text -->
1 # Task<br>2 # The task is to light the alcohol lamp to heat the compound in the beaker. The lamp is capped at the beginning. Put<br>the beaker on the support with mesh when heating<br>3<br>4 # Scene<br>5 # In a chemistry laboratory, on a table, these objects are placed: [lighter, alcohol_lamp, beaker, heat_support, mesh]<br>6 def exec_task(self):<br>7 # Uncap<br>8 alcohol_lamp = Object(’alcohol_lamp’,<br>9 geometry=self.query_geometry_info(’alcohol_lamp’),<br>10 affordance=self.query_affordance_info(’alcohol_lamp’),<br>11 state=self.query_state_info(’alcohol_lamp’)<br>12 )<br>13 uncap_alcohol_lamp_task = PrimitiveTask(alcohol_lamp.affordance.get_primitive_task_info(’uncap’))<br>14 uncap_alcohol_lamp_task.execute(src_object=alcohol_lamp, trajectory=oracle.generate(uncap_alcohol_lamp_task))<br>15<br>16 # Light<br>17 lighter = Object(’lighter’,<br>18 geometry=self.query_geometry_info(’lighter’),<br>19 affordance=self.query_affordance_info(’lighter’),<br>20 state=self.query_state_info(’lighter’)<br>21 )<br>22 light_alcohol_lamp_task = PrimitiveTask(lighter.affordance.get_primitive_task_info(’light_lamp’))<br>23 light_alcohol_lamp_task.execute(src_object=lighter, tgt_object=alcohol_lamp, trajectory=oracle.generate(<br>light_alcohol_lamp_task))<br>24<br>25 # Arrange (put on the mesh support)<br>26 beaker = Object(’beaker’,<br>27 geometry=self.query_geometry_info(’beaker’),<br>28 affordance=self.query_affordance_info(’beaker’),<br>29 state=self.query_state_info(’beaker’)<br>30 )<br>31 heat_support = Object(’heat_support’,<br>32 geometry=self.query_geometry_info(’heat_support’),<br>33 affordance=self.query_affordance_info(’heat_support’),<br>34 state=self.query_state_info(’heat_support’)<br>35 )<br>36 mesh = Object(’mesh’,<br>37 geometry=self.query_geometry_info(’mesh’),<br>38 affordance=self.query_affordance_info(’mesh’),<br>39 state=self.query_state_info(’mesh’)<br>40 )<br>41 put_beaker_on_mesh_task = PrimitiveTask(beaker.affordance.get_primitive_task_info(’arrange’))<br>42 put_beaker_on_mesh_task.execute(src_object=beaker, tgt_object=heat_support, trajectory=oracle.generate(<br>put_beaker_on_mesh_task))<br>43<br>44 # Stack mesh to heat<br>45 stack_mesh_task = PrimitiveTask(mesh.affordance.get_primitive_task_info(’stack_mesh’))<br>46 stack_mesh_task.execute(src_object=mesh, tgt_object=beaker, trajectory=oracle.generate(stack_mesh_task))<br>47<br>48 # Heat<br>49 heat_beaker = PrimitiveTask(alcohol_lamp.affordance.get_primitive_task_info(’heat_beaker’))<br>50 heat_beaker.execute(src_object=alcohol_lamp, tgt_object=beaker, trajectory=oracle.generate(heat_beaker))<br><!-- End of picture text -->

Listing 3. Primitive Task Planning Fail Example. One violation of dependency occurs (line 41): the extra _place onto_ primitive erroneously positions the beaker upon the support prior to the asbestos mesh’s placement on the support. This blocks the correct execution path that requires placing the asbestos mesh before heating the beaker. 

26 

