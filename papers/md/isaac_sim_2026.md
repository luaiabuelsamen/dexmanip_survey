# **NVIDIA Isaac Sim: Enabling Scalable, GPU-Accelerated Simulation for Robotics** 

**Sicong Gao**<sup>1</sup> , **Maurice Pagnucco**<sup>1</sup> , **Tomasz Bednarz**<sup>2</sup> , **Yang Song**<sup>1</sup> 

1School of Computer Science and Engineering, The University of New South Wales 

2NVIDIA USA 

_{_ sicong.gao, morri, yang.song1 _}_ @unsw.edu.au, tbednarz@nvidia.com 

## **Abstract** 

Simulation has become a core infrastructure for robotics research. Unlike previous simulators, NVIDIA Isaac Sim leverages GPU acceleration to enable large-scale parallel training and physicsaccurate modeling. Its synthetic data generation pipeline alleviates the scarcity of high-quality training data, supporting data-driven robot learning and large-scale simulation-centric experimentation. However, existing surveys often treat it as one simulator among many, without a systematic analysis of its architectural characteristics, usage patterns, and limitations. This survey reviews Isaac Sim from system and application perspectives, outlining its architecture and comparing it with widely used simulators. We analyze representative studies across five major domains and summarize common usage patterns, particularly in data generation and high-fidelity simulation. We also outline key future directions and challenges, including physics open-world learning, simulationcentric training and practical usability constraints. 

## **1 Introduction** 

Simulation has long been a core tool in robotics and embodied AI, providing a controlled, repeatable environment for developing and evaluating algorithms before deployment in the physical world. As robotic systems increasingly integrate perception, decision-making, and physical interaction, the role of simulation has expanded beyond control and motion verification to encompass perception learning, multimodal data generation, digital twin construction, and system-level evaluation. This evolution places new demands on simulation platforms, which must support not only accurate physical dynamics but also high-fidelity sensing, scalable execution, and tight integration with learning frameworks. 

Over the past decade, simulation platforms have been adopted in the robotics community, such as Gazebo [Koenig 

_et al._ , 2004], MuJoCo [Todorov _et al._ , 2012], PyBullet [Coumans _et al._ , 2016], and Webots [Michel, 2004]. These simulators have enabled progress in areas such as motion planning, reinforcement learning, navigation, and control. However, many of them are designed with a narrow focus, often emphasizing control-oriented simulation, lightweight physics modeling, or domain-specific scenarios. Consequently, their support for photorealistic rendering, large-scale synthetic data generation, and physical interaction remains limited. As a result, researchers rely on multiple tools or custom pipelines to bridge the gap between physics simulation, sensor modeling, and data-driven learning. 

Against this backdrop, NVIDIA Isaac Sim<sup>1</sup> has emerged as a comprehensive simulation platform that addresses these limitations by unifying high-fidelity physics, photorealistic rendering, scalable assets, and native support for robotic learning frameworks. Built on the NVIDIA Omniverse ecosystem, Isaac Sim combines GPU-accelerated PhysX dynamics, RTX-based rendering, and Universal Scene Description (USD)-based scene representation, enabling large-scale simulation of complex environments, diverse sensors, and rich physical interactions. Beyond conventional robotics simulation, it provides systematic support for synthetic data generation, digital twin construction, and large-scale parallel training, making it increasingly relevant to contemporary research in robotic embodied AI. 

In recent years, Isaac Sim has been adopted across a wide range of application domains, including industrial, healthcare, and household. It is used not only as a testbed for algorithmic evaluation, but also as a data-centric simulation platform that supports the systematic generation of perception data and the analysis of long-horizon, system-level robotic behaviors that are difficult to study in real-world settings. Despite its growing impact, existing surveys on robotic simulation typically treat Isaac Sim as one platform among many, often focusing on general simulator comparisons or specific application domains [Wong _et al._ , 2025; Long _et al._ , 2025; Kargar _et al._ , 2024]. To the best of our knowledge, there has 

1https://docs.isaacsim.omniverse.nvidia.com/latest/index.html 



Figure 1: Overall pipeline of reinforcement learning training by integrating NVIDIA Isaac Sim with NVIDIA Isaac Lab. Isaac Sim is used to build high-fidelity simulation scenes and generate synthetic training data, while Isaac Lab provides vectorized environments and RL interfaces (observations, actions, rewards) for GPU-parallel policy optimization. 

been no systematic and dedicated review of Isaac Sim that covers its architecture, application patterns, and limitations. 

This survey presents the first comprehensive study of NVIDIA Isaac Sim. Rather than treating it as an isolated tool, we view Isaac Sim as an integrated simulation ecosystem and examine how its core components support the different stages of robotic research, from environment construction and data generation to learning and sim-to-real transfer. We begin by reviewing its architectural design and situating Isaac Sim in the context of other widely used simulation platforms. We then analyze its role in synthetic data generation, with particular attention to programmable scene construction and trajectory learning. On this basis, we survey representative studies across five major domains, including industrial and manufacturing, healthcare and surgical, embodied AI, foundation models, and benchmarks, to illustrate how simulation is leveraged to meet domain-specific task requirements. We also discuss future research directions and challenges. 

By synthesizing recent research, this survey aims to provide researchers and practitioners with a structured understanding of what Isaac Sim enables, how it is used in practice, and its limitations. We hope this work will serve as a reference for selecting appropriate simulation tools, designing simulation-based research pipelines, and identifying open challenges at the intersection of simulation, learning, and embodied intelligence. 

## **2 Isaac Sim Architecture** 

Isaac Sim is designed as a unified simulation infrastructure for robotics and embodied AI, integrating high-fidelity physics, photorealistic rendering, scalable asset management, and seamless interfaces to learning and control frameworks. In this section, we position Isaac Sim in comparison with other simulators (§2.1) and review its core architectural components, including the asset system (§2.2), IsaacLab (§2.3), and digital-twin capabilities (§2.4). 

### **2.1 Simulation Platform** 

Various simulation platforms have been developed for robotics, reinforcement learning, and data-driven perception. Table 1 compares representative simulators from multiple perspectives. Among the compared platforms, Isaac Sim stands out as the most comprehensive solution. It natively supports ray tracing and parallel rendering, enabling highfidelity visual simulation through an RTX-based pipeline. 

In contrast, traditional robotics simulators such as Gazebo, MuJoCo, and PyBullet mainly focus on rigid-body dynamics and control-oriented simulation. While lightweight and efficient, they lack native support for advanced rendering, synthetic data pipelines, and complex physical dynamics, limiting their use to algorithmic evaluation rather than highfidelity perception or industrial digital twin scenarios [Wong _et al._ , 2025]. Webots and CoppeliaSim [Rohmer _et al._ , 2013] provide richer sensor support but are largely restricted to rigid-body modeling, with cloth behavior only approximated. CARLA [Dosovitskiy _et al._ , 2017] is tailored for autonomous driving, offering strong support for vehicle dynamics and sensor simulation, but its applicability is largely confined to traffic environments. Habitat [Puig _et al._ , 2023] emphasizes efficient embodied AI and navigation with parallel simulation and reinforcement learning integration, yet does not natively support advanced rendering or complex physical interactions [Long _et al._ , 2025]. Unity [Juliani _et al._ , 2018] offers flexible rendering and a mature ecosystem but requires additional engineering to achieve high physical fidelity and robotics middleware integration [Flores Gonzalez _et al._ , 2025]. In contrast, Isaac Sim provides broader support for physical dynamics and tight integration with ROS and digital twin workflows, making it well-suited for industrial robotics and vision applications. 

### **2.2 Asset System** 

Isaac Sim provides a comprehensive set of USD-based assets for constructing simulated environments and robotic systems. 

|**Simulator**|**Physics Engine**|**Ray**<br>**Tracing**|**Parallel**<br>**Rendering**|**Sensors**<br>**Stack**|**RL**<br>**Integration**|**SynData**<br>**Pipeline**|**ROS1/2**<br>**Integration**|**Digital Twin/Industry**|**Dynamics**|
|---|---|---|---|---|---|---|---|---|---|
|Isaac Sim<sup>1</sup>|PhysX (GPU)|✓|✓|✓|✓|✓|✓|✓|R;D;C;F|
|Gazebo|ODE / DART / Bullet / Simbody|✗|✗|✓|_◦_|✗|✓|_◦_|R|
|MuJoCo|MuJoCo|✗|✗|_◦_|✓|✗|_◦_|✗|R;D;C|
|PyBullet|Bullet|✗|✗|_◦_|✓|✗|_◦_|✗|R;D;C|
|Webots|ODE|✗|✗|✓|_◦_|✗|✓|_◦_|R;C<sup>_◦_</sup>|
|CoppeliaSim|Bullet / ODE / Vortex / Newton|_◦_|✗|✓|_◦_|✗|✓|_◦_|R;C<sup>_◦_</sup>|
|CARLA|PhysX|_◦_|_◦_|✓|_◦_|_◦_|_◦_|✗|R|
|Habitat|Bullet|✗|_◦_|_◦_|✓|_◦_|✗|✗|R|
|Unity|PhysX|_◦_|_◦_|_◦_|✓|✓|_◦_|_◦_|R;C|



Table 1: Functional comparison of popular simulation platforms, covering rendering, sensor simulation, reinforcement learning (RL) support, synthetic data generation, ROS/ROS 2 integration, digital-twin capabilities, and physical dynamics (R: rigid, D: deformable, C: cloth, F: fluid). ✓ denotes strong native support; _◦_ indicates partial or plugin-based support; ✗ denotes limited or no support. 

These assets include up to 50 robot models (e.g., articulated manipulators, mobile robots, and mobile manipulators), more than 20 sensor types (e.g., RGB/depth cameras, LiDAR, and IMU), and human characters (e.g., Worker, Police, Doctor). Environment assets span from simple indoor scenes to warehouse and outdoor layouts, supporting diverse testbeds for navigation, manipulation, and interaction tasks. The availability of physics-compatible assets has supported recent research efforts. For example, Orbit [Mittal _et al._ , 2023] leverages Isaac Sim assets to construct a suite of robotic environments for learning control and interaction policies, including tasks such as cloth folding and cabinet opening with articulated robots. Similarly, InteriorAgent [Team _et al._ , 2025] provides indoor scenes in USD format, which have been used to evaluate embodied AI tasks such as navigation and layout understanding with high-fidelity visual detail. 

### **2.3 IsaacLab** 

NVIDIA IsaacLab<sup>2</sup> is a reinforcement learning framework built on Isaac Sim that integrates libraries such as RL-Games, SKRL, and RSL-RL for large-scale robot learning. As shown in Fig. 1, NVIDIA Isaac Sim and Isaac Lab are combined to form an end-to-end reinforcement learning training pipeline. It provides standardized interfaces for environment and control definition, and supports GPU-based parallel execution across many environments. By coupling reinforcement learning with Isaac Sim’s physics engine, IsaacLab enables efficient training under physically consistent simulation. 

Peterson et al. [2025] propose a heterogeneous adversarial multi-agent reinforcement learning framework for scalable training under high-fidelity physics. Similarly, MARLadona. [Li _et al._ , 2025] is a multi-agent soccer environment that enables thousands of parallel simulations via GPU acceleration. This scalability is supported by IsaacLab’s vectorized environments and its tight integration with the Isaac physics engine. Wheeled Lab [Han _et al._ , 2025] integrates wheeled robots with IsaacLab to support large-scale reinforcement learning for control and perception-driven naviga- 

2https://isaac-sim.github.io/IsaacLab/main/index.html 

tion. Using IsaacLab’s realistic simulation and modular environments, policies are trained for tasks such as controlled drifting, elevation traversal, and vision-based navigation. 

### **2.4 Digital Twin** 

Digital twin technology uses virtual models to mirror realworld systems for monitoring, prediction, and optimization. By integrating sensing, data, and simulation, it synchronizes virtual and physical entities to support decision-making. Isaac Sim provides high-fidelity digital twin modules that enable rapid construction of digital twin systems, including warehouse layout builders, conveyor tools, and static warehouse assets, to create complete logistics or industrial scenarios for state monitoring, scheduling optimization, and control policy validation. 

Horsgaard et al. [2025] construct a warehouse environment and integrate a Grab™robot to enable package picking with a robotic arm and gripper. Compared to earlier Webots-based simulations, their approach addresses limitations related to unrealistic environments and slow execution speed. Building on similar warehouse sorting scenarios, Sand et al. [2023] use the built-in conveyor system together with monocular vision and reinforcement learning to achieve real-time grasping and sorting. In contrast, Nambiar et al. [2024] apply Isaac Cortex to microscopic slide sorting by transferring ROS commands to a real ABB YuMi robot. While this approach enables synchronization between the simulation and the real system, it lacks feedback from the physical environment, as perception relies on predefined spreadsheet data rather than real sensors, which limits realism and adaptability. 

## **3 Synthetic Data and Perception** 

High-quality data is essential for data-driven robotics, yet real-world collection is limited by cost, safety, and scalability. Simulation-based synthetic data generation has therefore become a key paradigm for controllable and scalable learning. This section reviews how Isaac Sim enables synthetic data generation across perception (§3.1), actor-centric simulation (§3.2), and robotic trajectory modeling (§3.3) through 

high-fidelity simulation, programmable scene construction, and large-scale randomization. 

### **3.1 Synthetic Data in Robotic Perception** 

Robotic perception models require large-scale annotated data, yet real-world collection is costly and constrained by annotation effort, limited long-tail coverage, and safety concerns. Synthetic data generation mitigates these issues by providing scalable data with accurate labels and controllable distributions that are difficult to obtain in real environments. 

In this context, Replicator<sup>3</sup> , an extension of Isaac Sim, provides a programmable framework for synthetic data generation in perception learning, supporting semantic annotation in USD-based scenes. For instance, Elia et al. [2023] built a multi-robot aerial–ground robotic platform for SLAM. Once configured, these scenes can be rendered with GPU acceleration to produce richly annotated multimodal datasets, including bounding boxes, segmentation masks, and depth maps, etc. Ng et al. [2023] proposed SynTable, which uses Replicator to generate complex 3D tabletop scenes with diverse object meshes, materials, textures, lighting conditions, and backgrounds. Their pipeline targets amodal instance segmentation for previously unseen objects and provides supervision signals that are difficult to obtain from real-world data. 

Beyond static scene generation, Replicator also supports large-scale scene and sensor randomization. Ritvik et al. [2024] leveraged Replicator’s asset library and procedural randomization to generate diverse indoor environments for object detection. By programmatically constructing room layouts, placing objects, randomizing camera trajectories, and introducing distractors to increase occlusion diversity, their approach reduces manual annotation effort and improves robustness under complex visual conditions. 

### **3.2 Synthetic Data in Actor Simulation** 

Real-world data collection is often limited by scalability, cost, and the difficulty of capturing rare or hazardous scenarios such as accidents or near-miss events. Simulation enables these long-tail events to be generated programmatically. Isaac Sim supports actor and event-oriented synthetic data workflows, enabling the generation of dynamic, richly annotated sequences by simulating in realistic environments. Maric et al. [2022] constructed a large-scale dataset for indoor fire detection and segmentation, systematically covering diverse indoor environments and challenging lighting conditions to address the difficulty of collecting real-world fire and other hazardous scenarios. OmniGibson [Li _et al._ , 2023] is a large-scale interactive indoor environment for embodied AI. Developing robot-environment interaction processes through home-based scenarios. Andreas et al. [2023] constructed a pipeline of conveyor–fish interactions in a fish factory. This 

> 3https://docs.isaacsim.omniverse.nvidia.com/latest/ replicator ~~t~~ utorials/index.html 

workflow enables systematic testing of fish sorting and grasping strategies while allowing safe, repeatable simulation of complex physical interactions that would be costly and difficult to scale in real-world settings. 

### **3.3 Synthetic Data in Robotic Trajectory** 

Real-world trajectory collection for mobile robots is costly and often constrained by safety and scalability. Simulation enables systematic synthesis of trajectory data under controlled conditions. Isaac Sim addresses this need through the MobilityGen pipeline, which captures time-series robot trajectories and multimodal sensor data during simulated navigation, enabling scalable datasets for tasks such as navigation, SLAM, and motion prediction. RoboMIND [Wu _et al._ , 2024] contains 107k manipulation trajectories across multiple robot embodiments, each annotated with multi-view RGB-D observations, robot states, and task descriptions. By aligning simulation with physical setups, Isaac Sim enables lowcost demonstration augmentation and systematic evaluation of manipulation policies across diverse tasks and robot embodiments. Salimpour et al. [2025] leveraged MobilityGen to train reinforcement-learning navigation and obstacleavoidance policies in physics-enabled simulation environments. The policies were subsequently transferred to Gazebo and to real ROS 2 robots in a zero-shot manner. KitchenR [Kachaev _et al._ , 2025] enables a large-scale collection of robotic trajectories for mobile manipulation tasks in Isaac Sim. It records navigation and manipulation trajectories while a mobile manipulator executes multi-step language instructions in a simulated kitchen, logging time-series robot states, gripper commands, and synchronized multi-view sensor observations in ROS-compatible formats. 

## **4 Domain Applications** 

Isaac Sim is widely used across domains where high-fidelity simulation is essential for development and evaluation. This section reviews representative applications built on Isaac Sim, including industrial and manufacturing robotics (§4.1), healthcare and surgery (§4.2), embodied AI (§4.3), foundation models (§4.4), and platform and benchmark systems (§4.5), highlighting how task-specific requirements are addressed through simulation. The categorization of application domains and representative studies is illustrated in Fig. 2. 

### **4.1 Industrial and Manufacturing** 

Industrial and manufacturing environments demand robotic systems that are safe, efficient, and robust under complex layouts and human–robot coexistence. Isaac Sim can realistically model warehouse layouts, robot kinematics, sensors, and human activities, making it well-suited for developing and evaluating automated guided vehicles (AGVs) and autonomous mobile robots (AMRs). Kagami et al. [2025] investigated multi-AGV coordination for robot-to-parts picking, analyzing shelf retrieval and task scheduling behaviors. 



<!-- Start of picture text -->
Industrial & Kagami et al. [2025], Imran et al. [2024], Haug et al. [2025], Chen et al. [2025], Koprov et<br>Manufacturing al. [2025], Nguyen et al. [2025], Monnet et al. [2024], Jeong et al. [2022]<br>Healthcare & Gao et al. [2026], Kim et al. [2025], ORBIT-Surgical [Yu  et al. , 2024], Hydock et al. [2023], dARt<br>Surgery Vinci [Liu  et al. , 2025b], SUFIA [Moghani  et al. , 2024], SUFIA-BC [Moghani  et al. , 2025]<br>Embodied AI AdaVLN [Loh  et al. , 2024], ReKep [Huang  et al. , 2024], Bonyani et al. [2025], TacEx [Nguyen  et<br>al. , 2024], GRADE [Bonetto  et al. , 2023], PR2 [Liu  et al. , 2025a], ManiSkill3 [Tao  et al. , 2024]<br>Foundation NVIDIA GR00T [Bjorck et al. , 2025], IsaacLabEvalTasks [NVIDIA, 2025], Park et al. [2025],<br>Models Cosmos [Agarwal  et al. , 2025]<br>Platform & InfiniteWorld [Ren et al. , 2024], AgentWorld [Zhang et al. , 2025], RealMirror [Tai et al. , 2025],<br>Benchmark BEHAVIOR-1K [Li et al. , 2023], Kitchen-R [Kachaev et al. , 2025], Zhou et al. [2024], Lin et<br>al. [2025]<br>Domain Applications<br><!-- End of picture text -->

Figure 2: Major domain applications of Isaac Sim and representative studies in each domain. 

Imran et al. [2024] evaluated warehouse layouts and dispatch strategies, highlighting Isaac Sim’s value for systemlevel AGV analysis. Haug et al. [2025] studied AMR safety in human–robot shared spaces. Isaac Sim also enables the industrial metaverse by linking physical assets, digital twins, and intelligent decision systems. Chen et al. [2025] view the industrial metaverse as a data-driven ecosystem supporting workflow simulation, such as sorting and production. Koprov et al. [2025] further demonstrate that integrating Isaac Sim with industrial IoT pipelines enables real-time synchronization and motion simulation for industrial metaverse applications. In addition, Isaac Sim can be applied to industrial inspection by programmatically simulating surface defects under diverse viewpoints and lighting conditions, thereby supporting robust training and evaluation of inspection models for factory components [Nguyen _et al._ , 2025; Monnet _et al._ , 2024; Jeong _et al._ , 2022]. 

### **4.2 Healthcare and Surgery** 

Due to tissue deformability and constrained workspaces, surgical robots require high perception accuracy, reliable contact-rich manipulation, and strict safety guarantees. Gao et al. [Gao _et al._ , 2026] leverage Isaac Sim to generate largescale synthetic endoscopic datasets for depth estimation and navigation. Beyond perception, Isaac Sim also supports physically accurate simulation of surgical manipulation. Kim et al. [2025] establish a robot-assisted suturing environment, where Isaac Sim’s ROS interfaces are integrated with haptic teleoperation to enable interactive training and reproducible benchmarking of suturing skills. At the system level, ORBITSurgical [Yu _et al._ , 2024] builds an open simulation benchmark on Isaac Sim for training and evaluating reinforcement learning and imitation learning policies on fundamental sur- 

gical subtasks, such as needle extraction, handover, and tissue manipulation, while supporting large-scale parallel simulation and synthetic perception data generation. 

To further reduce reliance on physical hardware and expert demonstrations, Hydock et al. [Hydock _et al._ , 2023] use Isaac Sim to render surgical instruments in randomized environments, automatically generating precisely annotated medical images for training object detection and semantic segmentation models. dARt Vinci [Liu _et al._ , 2025b] introduces an egocentric data collection pipeline that combines Isaac Sim with Augmented Reality-based interfaces, allowing users to collect surgical robot learning data using only a head-mounted display and a standard PC. Building on this paradigm, SUFIA [Moghani _et al._ , 2024] and SUFIA-BC [Moghani _et al._ , 2025] integrate language-guided planning, anatomically realistic digital twins, and large-scale synthetic demonstrations within Isaac Sim, enabling systematic evaluation of behavior cloning and language-conditioned autonomy for surgical assistants. 

### **4.3 Embodied AI** 

Embodied artificial intelligence enables perception, reasoning, and action through physical interaction. Isaac Sim integrates photorealistic rendering and multi-sensor modeling, making it well-suited for vision–language embodied learning in physically grounded environments. Recent studies leverage Isaac Sim to investigate instruction-driven embodied navigation in unstructured settings. AdaVLN [Loh _et al._ , 2024] extends vision–language navigation to continuous indoor environments with moving humans, and introduces a freezetime mechanism to ensure fair and reproducible evaluation under dynamic obstacles. ReKep [Huang _et al._ , 2024] models tasks as spatio-temporal relational keypoint constraints, 

addressing the challenge of converting free-form language instructions into executable embodied behaviors and enabling real-time robot action generation. Bonyani et al. [2025] integrate LiDAR and depth sensing into Isaac Sim to support instruction-aware planning and collision-free navigation, demonstrating Isaac Sim’s advantage in unifying realistic sensing, dynamics, and instruction grounding. 

High-fidelity physical interaction simulation is a fundamental component of embodied intelligence. Isaac Sim provides core support for complex embodied interaction by unifying physics-consistent simulation with photorealistic sensor rendering. TacEx [Nguyen _et al._ , 2024] enables highfidelity contact modeling for GelSight visuotactile sensors, GRADE [Bonetto _et al._ , 2023] supports the study of active SLAM and multi-robot perception in realistic dynamic environments, and PR2 [Liu _et al._ , 2025a] integrates accurate dynamics with indoor and outdoor scenes to study the joint embodiment of locomotion, manipulation, and perception in humanoid robots. At scale, ManiSkill3 [Tao _et al._ , 2024] extends the GPU-based physics simulation paradigm of Isaac simulators, enabling efficient large-scale embodied reinforcement and imitation learning through parallel training. 

### **4.4 Foundation Models** 

Robotic foundation models unify perception, language, and action, relying on high-fidelity simulation such as Isaac Sim for scalable training and evaluation. NVIDIA GR00T [Bjorck _et al._ , 2025] is a foundation model for generalist robots based on a unified vision–language–action formulation. It relies on Isaac Sim for large-scale, high-fidelity simulation to enable reproducible data generation and improved generalization with fewer real-world data samples. It defines two industrial manipulation tasks [NVIDIA, 2025] in Isaac Sim: nut pouring and exhaust pipe sorting, each requiring multi-step bimanual humanoid actions. In addition, Park et al. [2025] build on GR00T’s diffusion policy and use Isaac Sim simulations as well as physical interaction modeling to improve stability and generalization in grasp-and-place tasks. 

Cosmos [Agarwal _et al._ , 2025] is a world model proposed by NVIDIA for Physical AI, enabling the generation of physically consistent videos and scene trajectories for robot learning. It complements Isaac Sim, which provides high-fidelity simulation and digital twins, while Cosmos extends data coverage through generative world modeling to capture longhorizon dynamics, rare events, and complex interactions, and to generate realistic scene variations from simulation priors. 

### **4.5 Platform and Benchmark** 

Many studies regard Isaac Sim as an extensible simulation platform adaptable to task-specific scenarios. InfiniteWorld [Ren _et al._ , 2024] focuses on open-world vision–language interaction, emphasizing long-horizon interaction under partially observable environments. It aims to 

evaluate how agents explore and act in large-scale environments with continuously generated scenes. AgentWorld [Zhang _et al._ , 2025] focuses on household mobile manipulation, with its core contribution being the integration of procedural scene construction and mobile teleoperation to collect long-horizon manipulation trajectories across diverse home layouts. RealMirror [Tai _et al._ , 2025] is designed for vision–language–action learning in humanoid robots, with a particular emphasis on evaluation and sim-to-real transfer. 

Benchmarks evaluate an agent’s ability to perceive, plan, and act under physical constraints. Isaac Sim enables assessment of physical feasibility, efficiency, and robustness beyond task success rates. BEHAVIOR-1K [Li _et al._ , 2023] evaluates performance on 1,000 everyday household activities, while Kitchen-R [Kachaev _et al._ , 2025] focuses on language-guided mobile manipulation in a realistic kitchen digital twin and explicitly separates task planning and low-level control. The AI-CPS [Zhou _et al._ , 2024] benchmark evaluates industrial manipulation tasks, including peg-in-hole insertion, stacking, door opening, and cloth placement. VLNVerse [Lin _et al._ , 2025] evaluates vision–language navigation under continuous control and full embodiment. 

## **5 Future Directions and Challenges** 

**Physically Executable Open-World Learning** Recent open-world research has increasingly shifted toward generative world models that emphasize large-scale environment synthesis and semantic diversity. While these approaches can produce visually rich environments, they often lack physically consistent interaction, including reliable collision handling, contact dynamics, and long-horizon physical feasibility. Lu et al. [2024] note that robots trained in open-world settings tend to rely on case-based generalization rather than abstract physical rules, while Mao et al. [2025] show that directly applying video generation models to robot control neglects physical constraints. These limitations restrict the deployment of generative open-world models in real robotic systems. In contrast, Isaac Sim provides a physics-consistent simulation backbone that complements generative models by enforcing physical validity and executability. A promising direction is hybrid open-world systems that integrate generative scene synthesis with high-fidelity physics simulation. Generative models offer diverse and evolving environments, while Isaac Sim enforces physically grounded interaction, enabling scalable training and evaluation in executable open worlds. Its GPU-accelerated physics further enables the incorporation of physical constraints into generative model training, bridging visual diversity and physical realism. 

**Toward Simulation-Centric Training of Robotic Foundation Models** Robotic foundation models require largescale, multimodal, and physically realistic data to jointly learn perception, language, and action; however, real-world data collection is costly, slow, and constrained by safety 

and scalability. Isaac Sim provides a cost-effective alternative as a unified simulation-based training platform, where high-fidelity physical modeling helps reduce the sim-to-real gap and enables more transferable representations and policies. Its native support for GPU acceleration and large-scale parallel simulation further improves training efficiency, allowing foundation models to scale across diverse tasks, instances, and scenarios, and to explore large architectures and long-horizon behaviors within practical time budgets [Ahmed _et al._ , 2024]. Moreover, the Replicator pipeline enables a data-centric training paradigm by generating largescale, richly annotated datasets covering visual perception, robot trajectories, human–robot interaction, and multimodal sensor streams, effectively capturing diversity and long-tail scenarios [Salimpour _et al._ , 2025]. Beyond training, foundation models can be deployed within Isaac Sim for planning, decision-making, and interaction studies, supporting controlled system-level evaluation and safety analysis. This bidirectional integration positions Isaac Sim as both a training platform and a testbed for studying foundation model behavior under physically grounded interaction conditions. 

**Generation–Simulation Hybrid Approaches for Sim-toReal Transfer** One long-standing challenge in robotics is the sim-to-real gap, particularly caused by visual discrepancies between simulated environments and the real world, which hinder reliable policy transfer. Looking ahead, integrating generative world models, such as Cosmos [Agarwal _et al._ , 2025], into physics-based simulation pipelines enabled by Isaac Sim represents a promising approach to address this issue. By converting simulated scenes into realistic digital twins, Isaac Sim can help reduce visual distribution mismatches while preserving consistent physical interaction. For example, DSR [Pareja _et al._ , 2025] uses Isaac Sim for largescale interaction learning in simulation, while Cosmos enriches visual and semantic diversity through generative modeling. Such hybrid simulation–generation approaches may significantly reduce dependence on real-world data collection and alleviate sim-to-real performance degradation caused by visual inconsistencies, particularly in complex robotic navigation scenarios. 

**Cloud-Native Collaborative Simulation Worlds** Another promising direction is to extend Isaac Sim toward cloudnative, persistent, and collaborative simulation worlds. In such environments, simulations remain continuously online and are jointly constructed and interacted with by multiple users, robots, and learning agents. These shared simulation worlds resemble small virtual ecosystems, where changes introduced by one participant can affect others in real time, enabling collective experimentation, long-horizon interaction, and continual data accumulation. Isaac Sim is well positioned to support this direction due to its system-level design. Built on NVIDIA Omniverse, it natively supports distributed rendering, asset streaming, and real-time synchronization, en- 

abling multi-user and multi-agent interaction within shared virtual spaces. In addition, its GPU-accelerated physics engine allows simulation to scale across many environments and agents, making persistent worlds practical on cloud infrastructure with dynamic resource allocation. The use of standardized scene representations and modular simulation components enables environments to be updated, versioned, and shared incrementally across users without requiring entire scenes to be rebuilt. 

**Challenge: Usability and Learning Curve of Isaac Sim** Despite its strong performance in physics fidelity and largescale simulation, the usability and learning curve of Isaac Sim remain practical challenges for broader adoption. Compared with lighter alternatives such as Webots or CoppeliaSim, Isaac Sim incurs substantially higher computational and memory overhead, which increases setup complexity and development costs, particularly for users with limited resources or experience [Wong _et al._ , 2025]. In addition, its reliance on high-end hardware and complex configuration pipelines may pose barriers for smaller research teams, even though it offers advanced GPU acceleration and photorealistic rendering [Flores Gonzalez _et al._ , 2025]. More broadly, highfidelity simulation platforms such as Isaac Sim often require nontrivial configuration and specialized expertise to fully exploit their capabilities, highlighting a trade-off between realism and ease of use [Zafra-Navarro _et al._ , 2025]. Addressing these usability challenges through improved abstractions, streamlined workflows, and clearer configuration standards will be critical for enabling wider and more effective use of Isaac Sim in both research and practice. 

## **6 Conclusions** 

This survey reviews recent studies that adopt NVIDIA Isaac Sim across different research domains. The literature indicates that Isaac Sim is used not only as a simulation tool, but more importantly as an integrated platform for data generation and for jointly modeling physical dynamics and perception learning. Its design enables researchers to study embodied decision-making and data-driven robotic foundation models under physically grounded conditions, while leveraging GPU-accelerated rendering and large-scale parallel simulation capabilities that are difficult to achieve with many other simulators. The surveyed works suggest a shift from taskspecific simulation toward system-level evaluation. Rather than focusing on isolated scenarios, many studies use Isaac Sim to analyze interaction-rich behaviors, long-horizon execution, and other complex settings, aiming to reduce the simto-real gap through more realistic simulation environments. At the same time, the high computational cost and steep learning curve remain practical obstacles to its broader adoption. 

## **References** 

- [Agarwal _et al._ , 2025] Agarwal et al. Cosmos world foundation model platform for physical AI. _arXiv:2501_ , 2025. 

- [Ahmed _et al._ , 2024] Ahmed et al. A systemic survey of the Omniverse platform and its applications in data generation, simulation and metaverse. _Frontiers in Computer Science_ , 6:1423129, 2024. 

- [Andreas, 2023] Andreas. Deformable body based salmon model-for iterative development and testing of equipment within Isaac Sim. Master’s thesis, NTNU, 2023. 

- [Bjorck _et al._ , 2025] Bjorck et al. GR00T n1: An open foundation model for generalist humanoid robots. _arXiv:2503.14734_ , 2025. 

- [Bonetto _et al._ , 2023] Bonetto et al. GRADE: Generating realistic and dynamic environments for robotics research with isaac sim. _IJRR_ , page 02783649251346211, 2023. 

- [Bonyani _et al._ , 2025] Bonyani et al. Embodied AI in unstructured 3d spaces: Fusing mid and long-range sensing for instruction-aware construction robotics. 2025. 

- [Chen _et al._ , 2025] Chen et al. Task-oriented edge-assisted cross-system design for real-time human-robot interaction in industrial metaverse. _arXiv:2508.20664_ , 2025. 

- [Coumans _et al._ , 2016] Coumans et al. Pybullet, a Python module for physics simulation for games, robotics and machine learning, 2016. 

- [Dosovitskiy _et al._ , 2017] Dosovitskiy et al. CARLA: An open urban driving simulator. In _Conference on robot learning_ , pages 1–16. PMLR, 2017. 

- [Flores Gonzalez _et al._ , 2025] Flores Gonzalez et al. ROScompatible robotics simulators for Industry 4.0 and Industry 5.0: A systematic review of trends and technologies. _Applied Sciences_ , 15(15):8637, 2025. 

- [Gao _et al._ , 2026] Gao et al. Reinforcement learning for follow-the-leader robotic endoscopic navigation via synthetic data. _arXiv:2601.02798_ , 2026. 

- [Han _et al._ , 2025] Han et al. Wheeled Lab: Modern sim2real for low-cost, open-source wheeled robotics. In _RSS_ , 2025. 

- [Haug _et al._ , 2025] Haug et al. Vision-based human awareness estimation for enhanced safety and efficiency of AMRs in industrial warehouses. In _ETFA_ , pages 1–4. IEEE, 2025. 

- [Horsgaard _et al._ , 2025] Horsgaard et al. Exploring real-time robot simulation in Isaac Sim with a digital twin of a warehouse picking robot. B.S. thesis, NTNU, 2025. 

- [Huang _et al._ , 2024] Huang et al. ReKep: Spatio-temporal reasoning of relational keypoint constraints for robotic manipulation. _arXiv:2409.01652_ , 2024. 

- [Hydock _et al._ , 2023] Hydock et al. Generation of synthetic data for medical decision support applications. In _AIPR_ , pages 1–7. IEEE, 2023. 

- [Imran _et al._ , 2024] Imran et al. Decentralized multi-robot shared perception for worker action inference in industrial facilities. In _ICRA_ , 2024. 

- [Jeong _et al._ , 2022] Jeong et al. Digital twin-based cutting tool breakage detection model using synthetic depth map and deep learning. In _ASPEN_ , 2022. 

- [Juliani _et al._ , 2018] Juliani et al. Unity: A general platform for intelligent agents. _arXiv:1809.02627_ , 2018. 

- [Kachaev _et al._ , 2025] Kachaev et al. Mind and motion aligned: a joint evaluation IsaacSim benchmark for task planning and low-level policies in mobile manipulation. _arXiv:2508.15663_ , 2025. 

- [Kagami _et al._ , 2025] Kagami et al. Multi-AGV assisted OPS in warehouse using digital twins and layout comparison. In _MetaCom_ , pages 205–212. IEEE, 2025. 

- [Kang _et al._ , 2024] Kang et al. How far is video generation from world model: A physical law perspective. _arXiv:2411.02385_ , 2024. 

- [Kargar _et al._ , 2024] Kargar et al. Emerging trends in realistic robotic simulations: A comprehensive systematic literature review. _IEEE Access_ , 12:191264–191287, 2024. 

- [Kim _et al._ , 2025] Kim et al. Surgical robotics environment in NVIDIA Isaac Sim for robot-assisted suturing. In _ISMR_ , pages 192–198. IEEE, 2025. 

- [Koenig _et al._ , 2004] Koenig et al. Design and use paradigms for Gazebo, an open-source multi-robot simulator. In _IROS_ , volume 3, pages 2149–2154. IEEE, 2004. 

- [Koprov _et al._ , 2025] Koprov et al. Industrial metaverse meets iiot: Low-code platforms for machine-to-machine and human-to-machine integration. _Manufacturing Letters_ , 44:1254–1265, 2025. 

- [Li _et al._ , 2023] Li et al. Behavior-1K: A benchmark for embodied AI with 1,000 everyday activities and realistic simulation. In _CoRL_ , pages 80–93. PMLR, 2023. 

- [Li _et al._ , 2025] Li et al. Marladona-towards cooperative team play using multi-agent reinforcement learning. In _ICRA_ , pages 15014–15020. IEEE, 2025. 

- [Lin _et al._ , 2025] Lin et al. VLNVerse: A benchmark for vision-language navigation with versatile, embodied, realistic simulation and evaluation. _arXiv:2512.19021_ , 2025. 

- [Liu _et al._ , 2025a] Liu et al. PR2: A physics-and photorealistic humanoid testbed with pilot study in competition. _Journal of Field Robotics_ , 2025. 

- [Liu _et al._ , 2025b] Liu et al. dARt Vinci: Egocentric data collection for surgical robot learning at scale. _arXiv:2503.05646_ , 2025. 

- [Loh _et al._ , 2024] Loh et al. AdaVLN: Towards visual language navigation in continuous indoor environments with moving humans. _arXiv:2411.18539_ , 2024. 

- [Long _et al._ , 2025] Long et al. A survey: Learning embodied intelligence from physical simulators and world models. _arXiv:2507.00917_ , 2025. 

- [Mao _et al._ , 2025] Mao et al. Robot learning from a physical world model. _arXiv:2511.07416_ , 2025. 

- [Maric _et al._ , 2022] Maric et al. A large scale dataset for fire detection and segmentation in indoor spaces. In _ICECCME_ , pages 1–8. IEEE, 2022. 

- [Michel, 2004] Michel. Cyberbotics ltd. webots™: professional mobile robot simulation. _IJARS_ , 1(1):5, 2004. 

- [Mittal _et al._ , 2023] Mittal et al. Orbit: A unified simulation framework for interactive robot learning environments. _IEEE RA-L_ , 8(6):3740–3747, 2023. 

- [Moghani _et al._ , 2024] Moghani et al. SuFIA: languageguided augmented dexterity for robotic surgical assistants. In _IROS_ , pages 6969–6976. IEEE, 2024. 

- [Moghani _et al._ , 2025] Moghani et al. SuFIA-BC: Generating high quality demonstration data for visuomotor policy learning in surgical subtasks. _arXiv:2504.14857_ , 2025. 

- [Monnet _et al._ , 2024] Monnet et al. Investigating the generation of synthetic data for surface defect detection: A comparative analysis. _Procedia CIRP_ , 130:767–773, 2024. 

- [Nambiar _et al._ , 2024] Nambiar et al. Automation in unstructured production environments using Isaac Sim: A flexible framework for dynamic robot adaptability. _Procedia CIRP_ , 130:837–846, 2024. 

- [Ng _et al._ , 2023] Ng et al. Syntable: A synthetic data generation pipeline for unseen object amodal instance segmentation of cluttered tabletop scenes. _arXiv:2307.07333_ , 2023. 

- [Nguyen _et al._ , 2024] Nguyen et al. TacEx: Gelsight tactile simulation in isaac sim–combining soft-body and visuotactile simulators. _arXiv:2411.04776_ , 2024. 

- [Nguyen _et al._ , 2025] Nguyen et al. Efficient synthetic defect on 3d object reconstruction and generation pipeline for digital twins smart factory. _Sensors_ , 2025. 

- [NVIDIA, 2025] NVIDIA. IsaacLabEvalTasks: Benchmarking GR00T n1 policy in isaac lab. https://github.com/ isaac-sim/IsaacLabEvalTasks, 2025. 

- [Pareja _et al._ , 2025] Pareja et al. DSR framework: A hybrid approach for accelerated training of AI models in mobile robotics. In _WEA_ , pages 150–161. Springer, 2025. 

- [Park _et al._ , 2025] Park et al. Modality-augmented finetuning of foundation robot policies for cross-embodiment manipulation on gr1 and g1. _arXiv:2512.01358_ , 2025. 

- [Peterson _et al._ , 2025] Peterson et al. A framework for scalable heterogeneous multi-agent adversarial reinforcement learning in IsaacLab. _arXiv:2510.01264_ , 2025. 

- [Puig _et al._ , 2023] Puig et al. Habitat 3.0: A co-habitat for humans, avatars and robots. _arXiv:2310.13724_ , 2023. 

- [Ren _et al._ , 2024] Ren et al. InfiniteWorld: A unified scalable simulation framework for general visual-language robot interaction. _arXiv:2412.05789_ , 2024. 

- [Rohmer _et al._ , 2013] Rohmer et al. V-REP: A versatile and scalable robot simulation framework. In _IROS_ , pages 1321–1326. IEEE, 2013. 

- [Salimpour _et al._ , 2025] Salimpour et al. Sim-to-Real transfer for mobile robots with reinforcement learning: from NVIDIA Isaac Sim to Gazebo and real ROS 2 robots. _arXiv:2501.02902_ , 2025. 

- [SAND _et al._ , 2023] SAND et al. Utilizing reinforcement learning and computer vision in a Pick-And-Place operation for sorting objects in motion. 2023. 

- [Singh _et al._ , 2024] Singh et al. Synthetica: Large scale synthetic data for robot perception. _arXiv:2410.21153_ , 2024. 

- [Tai _et al._ , 2025] Tai et al. RealMirror: A comprehensive, open-source vision-language-action platform for embodied ai. _arXiv:2509.14687_ , 2025. 

- [Tao _et al._ , 2024] Tao et al. Maniskill3: Gpu parallelized robotics simulation and rendering for generalizable embodied AI. _arXiv:2410.00425_ , 2024. 

- [Team _et al._ , 2025] Team and Inc. Interioragent: Interactive USD interior scenes for Isaac Sim-based simulation, 2025. 

- [Todorov _et al._ , 2012] Todorov et al. Mujoco: A physics engine for model-based control. In _IROS_ . IEEE, 2012. 

- [Wong _et al._ , 2025] Wong et al. A survey of robotic navigation and manipulation with physics simulators in the era of embodied AI. _arXiv:2505.01458_ , 2025. 

- [Wu _et al._ , 2024] Wu et al. Robomind: Benchmark on multiembodiment intelligence normative data for robot manipulation. _arXiv:2412.13877_ , 2024. 

- [Yu _et al._ , 2024] Yu et al. Orbit-surgical: An opensimulation framework for learning surgical augmented dexterity. In _ICRA_ , pages 15509–15516. IEEE, 2024. 

- [Zafra-Navarro _et al._ , 2025] Zafra-Navarro et al. Survey of simulators for deformable objects in robotics. _Jornadas de Autom´atica_ , (46), 2025. 

- [Zhang _et al._ , 2025] Zhang et al. AgentWorld: An interactive simulation platform for scene construction and mobile robotic manipulation. _arXiv:2508.07770_ , 2025. 

- [Zhou _et al._ , 2024] Zhou et al. Towards building AI-CPS with NVIDIA Isaac Sim: An industrial benchmark and case study for robotics manipulation. In _ICSE_ , pages 263– 274, 2024. 

