# **ORBIT: A Unified Simulation Framework for Interactive Robot Learning Environments** 

Mayank Mittal<sup>1</sup><sup>_,_2</sup> , Calvin Yu<sup>3</sup> , Qinxi Yu<sup>3</sup> , Jingzhou Liu<sup>3</sup> , Nikita Rudin<sup>1</sup><sup>_,_2</sup> , David Hoeller<sup>1</sup><sup>_,_2</sup> , Jia Lin Yuan<sup>3</sup> , Ritvik Singh<sup>3</sup> , Yunrong Guo<sup>2</sup> , Hammad Mazhar<sup>2</sup> , Ajay Mandlekar<sup>2</sup> , Buck Babich<sup>2</sup> , Gavriel State<sup>2</sup> , Marco Hutter<sup>1</sup> , Animesh Garg<sup>2</sup><sup>_,_3</sup> 



Fig. 1: ORBIT framework provides a large set of robots, sensors, rigid and deformable objects, motion generators, and teleoperation interfaces. Through these, we aim to simplify the process of defining new and complex environments, thereby providing a common platform for algorithmic research in robotics and robot learning. 

**_Abstract_ — We present ORBIT, a unified and modular framework for robot learning powered by NVIDIA Isaac Sim. It offers a modular design to easily and efficiently create robotic environments with photo-realistic scenes and high-fidelity rigid and deformable body simulation. With ORBIT, we provide a suite of benchmark tasks of varying difficulty– from singlestage cabinet opening and cloth folding to multi-stage tasks such as room reorganization. To support working with diverse observations and action spaces, we include fixed-arm and mobile manipulators with different physically-based sensors and motion generators. ORBIT allows training reinforcement learning policies and collecting large demonstration datasets from hand-crafted or expert solutions in a matter of minutes by leveraging GPU-based parallelization. In summary, we offer an open-sourced framework that readily comes with 16 robotic platforms, 4 sensor modalities, 10 motion generators, more than 20 benchmark tasks, and wrappers to 4 learning libraries. With this framework, we aim to support various research areas, including representation learning, reinforcement learning, imitation learning, and task and motion planning. We hope it helps establish interdisciplinary collaborations in these communities, and its modularity makes it easily extensible for more tasks and applications in the future. For videos, documentation, and code: https://isaac-orbit.github.io/.** 

## I. INTRODUCTION 

An ideal robot simulator needs to provide fast and accurate physics, high-fidelity sensor simulation, diverse asset handling, and easy-to-use interfaces for integrating new tasks and environments. However, existing platforms often need to make a trade-off between these aspects. For instance, simulators designed mainly for vision, such as Habitat [14] or ManipulaTHOR [12], offer decent rendering throughput but 

> 1 ETH Zurich, Switzerland, 2 NVIDIA, 3 University of Toronto, Canada Corresponding author: Mayank Mittal (email: mittalma@ethz.ch) 

simplify low-level interaction intricacies such as grasping. On the other hand, physics simulators for robotics, such as Isaac Gym [13] or SAPIEN [11], provide fast and reasonably accurate rigid-body contact dynamics but do not include physically-based rendering (PBR), deformable objects simulation or ROS support [15] out-of-the-box. Recently, NVIDIA released a new simulator Omniverse Isaac Sim [16] that aims to fulfill these gaps through GPU-accelerated real-time PBR and state-of-the-art physics engine. 

This work presents ORBIT, an open-source framework for robotics research that exploits the latest simulation capabilities through Isaac Sim to allow intuitive designing of tasks with photo-realistic scenes and state-of-the-art rigid and deformable body simulation. To prevent a scattering of efforts for building the necessary tooling to use the simulator for robot learning, we design a unified and modular framework that supports a wide variety of robotic platforms, sensors, and objects and allows designing tasks not only programmatically but also interactively through the GUI. We design the system bottom-up – from incorporating user-defined models for the actuator dynamics to modularizing task specifications for learning with different levels of observations and action spaces. In ORBIT, we also include a collection of features, such as different robot platforms, motion generators, and a suite of tasks that help serve not only as a benchmark but also as examples for designing a new task. Through this framework, we support various robotic applications, such as reinforcement learning (RL), learning from demonstrations (LfD), and motion planning, thereby providing a common platform for researchers in these communities to benefit from this consolidated effort. 

TABLE I: Comparison between different simulation frameworks and ORBIT. The check (✓) and cross (X) denote presence or absence of the feature. In **Robotic Platforms** column, _M_ stands for manipulator. In **Scene Authoring** column, _G_ stands for game-based designing, _M_ for mesh-scan scenes, and _P_ for procedural-generation. 

|**Name**|**PhsicsEnine**|**Renderer**|**Vectoriz**|**ation**||**Suppo**|**rted D**|**ynamics**|**PBR**|||**Sen**|**sors**||**Rob**|**otic Platfo**|**rms**|**Scene**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**y g**||**CPU**|**GPU**|**Rigid**|**Cloth**|**Soft**|**Fluid**|**Tracing**|**RGBD**|**Semantic**|**LiDAR**|**Contact**|**Acoustic**|**Fixed-M**|**Mobile-M**|**Legged**|**Authoring**|
|MetaWorld [1]|MuJoCo|OpenGL|✓|X|✓|X|X|X|X|X|X|X|X|X|✓|X|X|_P_|
|RoboSuite [2]|MuJoCo|OpenGL, OptiX|✓|X|✓|X|X|X|X|✓|✓|X|✓|X|✓|X|X|_P_|
|DoorGym [3]|MuJoCo|Unity|X|X|✓|X|X|X|✓|✓|✓|X|X|X|✓|X|X|_P, G_|
|DEDO [4]|Bullet|OpenGL|✓|X|✓|✓|✓|X|X|✓|X|X|X|X|✓|X|X|_P, G_|
|RLBench [5]|Bullet/ODE|OpenGL|X|X|✓|X|X|X|X|✓|✓|X|✓|X|✓|X|X|_P_|
|iGibson [6]|Bullet|MeshRenderer|✓|X|✓|X|X|X|✓|✓|✓|✓|X|X|X|✓|X|_M_|
|Habitat 2.0 [7]|Bullet|Magnum|X|X|✓|X|X|X|✓|✓|✓|X|X|X|✓|✓|✓|_P, M_|
|SoftGym [8]|FleX|OpenGL|✓|X|✓|✓|✓|✓|X|X|X|X|X|X|✓|X|X|_P_|
|ThreeDWorld [9]|PhysX 4/FleX/Obi|Unity3D|X|X|✓<sup>_∗_</sup>|✓<sup>_∗_</sup>|✓<sup>_∗_</sup>|✓<sup>_∗_</sup>|✓|✓|✓|X|X|✓|X|✓|X|_P_|
|ManiSkill2 [10]|PhysX 4/Warp|SAPIEN [11]|✓|X|✓|X|✓<sup>_†_</sup>|✓|✓|✓|✓|X|✓|X|✓|✓|X|_P_|
|ManipulatorThor [12]|PhysX 4|Unity|X|X|✓|X|X|X|✓|✓|✓|X|X|X|X|✓|X|_P, G_|
|IsaacGymEnvs [13]|PhysX 5|Vulkan|✓|✓|✓|X|X|X|X|✓|✓|X|✓|X|✓|X|✓|_P_|
|**ORBIT (ours)**|PhysX 5.1|Omniverse RTX|✓|✓|✓|✓|✓<sup>_†_</sup>|✓|✓|✓|✓|✓|✓|X|✓|✓|✓|_P, M, G_|



> * ThreeDWorld supports simulation of rigid bodies and deformable bodies based on whether PhysX 4 or FleX/Obi is enabled respectively. Thus, it is limited in simulating interactions between rigid and deformable bodies. 

_†_ ManiSkill2 supports a Warp-based Material Point Method (MPM) solver that helps simulate cutting and plastic deformations of soft objects. Currently, this feature is under development for ORBIT. 

Our main contributions are as follows: 

- 1) We design a unified and modular open-source framework for fast and flexible development, that leverages the latest advances in simulators for photo-realistic scenes and high-fidelity physics. 

- 2) It provides a batteries-included experience for roboticists with models readily available for different robots and sensors. This helps reduce the entry barrier to using the framework and its features. 

- 3) We include a suite of standardized tasks for benchmark purposes. These include eleven rigid object manipulation, thirteen deformable object manipulation, and two locomotion environments. Within each task, we allow switching robots, objects, and sensors easily. 

- 4) Through experiments, we demonstrate the accuracy of the simulator for rigid and soft body simulation. Compared to existing frameworks, we show that ORBIT is able to obtain up to _∼_ 10x and _∼_ 3x the throughput for rigid and deformable body manipulation tasks respectively. Additionally, we demonstrate the sim-to-real transfer of a locomotion policy for the quadruped robot, ANYmal. 

In the remainder of the paper, we describe the available simulator choices (Sec. II), the framework’s design decisions and abstractions (Sec. III), and its highlighted features (Sec. IV). We demonstrate the framework’s applicability on different robotics workflows (Sec. V), show sim-to-real experiments for locomotion and manipulation, and evaluate the obtained accuracy and simulation throughput in Sec. V-E. 

## II. RELATED WORK 

Recent years have seen several simulation frameworks, each specializing in particular robotic applications. In this section, we highlight the design choices crucial for building a unified simulation platform and how ORBIT compares to other frameworks (also summarized in Table I). 

_a) Physics Engine:_ Increasing the complexity and realism of physically simulated environments is essential for advancing robotics research. This includes improving the contact dynamics, having better collision handling for nonconvex geometries (such as threads), stable solvers for deformable bodies, and high simulation throughput. 

Prior frameworks [2], [5] using MuJoCo [17] or Bullet [18] focus mainly on rigid object manipulation tasks. Since their underlying physics engines are CPU-based, they 

need CPU clusters to achieve massive parallelization [13]. On the other hand, frameworks for deformable bodies [4], [8] mainly employ Bullet [18] or FleX [19], which use particle-based dynamics for soft bodies and cloth simulation. Recently, SofaGym [20], an RL framework specifically for soft robotics, shows the benefits of using finite-elementmethods (FEM) for deformation models. . However, limited tooling exists in these frameworks compared to those for rigid object tasks. ORBIT aims to bridge this gap by providing an integrated robotics framework that supports rigid and deformable body simulation via PhysX SDK 5 [21]. In contrast to other engines, PhysX SDK 5 features GPU-based hardware acceleration for high throughput, signed-distance field (SDF) collision checking [22], and more stable solvers based on FEM for deformable body simulation [23], [24]. 

_b) Sensor simulation:_ Various existing frameworks [2], [5], [13] use classic rasterization that limits the photo-realism in the generated images. Recent techniques [25] simulate the interaction of rays with object’s textures in a physically correct manner. These methods help capture fine visual properties such as transparency and reflection, thereby promising for bridging the sim-to-real visual domain gap. While recent frameworks [11], [7], [12] include physically-based renderers, they mainly support camera-based sensors (RGB, depth). This is insufficient for certain mobile robot applications that need range sensors, such as LiDARs. Leveraging the raytracing technology in NVIDIA Isaac Sim, ORBIT supports all these modalities and includes APIs to obtain additional information such as semantic annotations. 

_c) Scene designing and asset handling:_ Frameworks support scene creation procedurally [1], [2], [11], via mesh scans [6], [7] or through game-engine style interfaces [26], [9]. While mesh scans simplify generating large amounts of scenes, they often suffer from geometric artifacts and lighting problems. On the other hand, procedural generation allows leveraging object datasets for diverse scenes. While Isaac Sim mainly focuses on GUI-based scene designing, we choose to not be restrictive and build upon its interfaces to support all three methods for scene design. 

## III. ORBIT: ABSTRACTIONS AND INTERFACES DESIGN 

At a high level, the framework design comprises a world and an agent, similar to the real world and the software stack running on the robot. The agent receives raw observations from the world and computes the actions to apply to the embodiment (robot). Typically in learning, it is assumed 



Fig. 3: ORBIT’s abstractions comprise World, analogous to the real world, and Agent, the computation graph behind the embodied system. The nodes in the agent’s graph can perform observation-based or action-based processing. Through a graph-cut over this computation graph and specifying an extrinsic goal, it is feasible to design different tasks within the same World definition. For instance, to perform RL, this would define the task with _ot_ , _at_ , and _rt_ corresponding to the observation, action, and reward signals respectively. 

that all the perception and motion generation occurs at the same frequency. However, in the real world, that is rarely the case: (1) sensors update at differing frequencies, (2) depending on the control architecture, actions are applied at different time-scales [27], and (3) unmodeled sources of delays and noises are present in the system. In ORBIT, we thoughtfully design its interfaces and abstractions to support these functionalities and allow the inclusion of actuator and noise models to bridge the sim-to-real gap. 

_a)_ **_World_** _:_ Analogous to the real world, we define a world where robots, sensors, objects (static or dynamic), and visualization markers exist on the same stage. The world can be designed procedurally (script-based), via scanned meshes [28], or interactively through the game-based GUI of Isaac Sim, or a combination of them. This flexibility reaps the benefits of 3D reconstructed meshes, which capture various architectural layouts, with game-based designing, that simplifies the experience of creating and verifying the scene physics properties by playing the simulation. 

Robots are a crucial component of the world since they serve as the embodiment for interaction. They consist of articulation, actuator models, and low-level joint controllers. We design these interfaces such that a single interface (such as LeggedRobot) supports a variety of robots belonging to the same category (such as ANYmal C or Unitree A1). This simplifies setting up a new robot with the simulator and using it in an existing World. The robot class loads the robot model from a USD file<sup>1</sup> . It creates and manages the necessary physics handles to set and read the simulation state. The actuator models play an important role in injecting realworld actuator characteristics into the simulation, such as 

> 1Universal Scene Description <u>(USD)</u> is a hierarchical file format, used in <u>Omniverse, that allows storing assets,</u> materials definitions, and various attributes (such as for physics, semantics, rendering) efficiently and flexibly. ORBIT includes scripts to convert assets of different formats (URDF, obj, stl) into USD from the command line and adds various physics properties to them automatically, such as colliders and friction materials. 



Fig. 4: Illustration of actuator groups for a legged mobile manipulator. This allows decomposing a complex system into sub-groups and defining of specific transmission models for each of them flexibly. The number inside ( _·_ ) is the dimension of the command vector. 

delays or torque saturation. This can help facilitate the simto-real transfer of control policies on hardware (Sec. V-D). To apply actions on the robot, the joint-level controller processes input commands through actuator models before applying the desired joint position, velocity, or torque commands to the simulator (as shown in Fig. 4). Currently, we include actuator models for Direct Control (DC) motors and Series Elastic Actuators (SEA) [29]. However, it is easy for users to integrate the actuator model for their robot into ORBIT after identifying its dynamics characteristics. 

Sensors (proprioceptive or exteroceptive) may exist both for the robot or externally (such as third-person cameras). While ORBIT relies on Isaac Sim for different physics-based (range, force, and contact sensor) and rendering-based (RGB, depth, normals) sensors, it unifies them under a common interface to simplify creating and configuring them into a scene at runtime. We diverge from the recommended USD practice in Isaac Sim where sensors are expected to be specified in a USD file and all of them are updated at every simulation step. While this practice doesn’t cause a huge issue for the traditional robotics paradigm, it leads to significant overhead when having parallelized scenes as there would exist undesired sensors updating in the scene. Through a common sensor management system 



Fig. 5: Overview of features included in ORBIT. We provide models of different sensors, robotic platforms, objects from different datasets, motion generators, and teleoperation devices. Using RTX-accelerated ray-tracing, we can obtain high-fidelity images in real-time for different modalities such as RGB, depth, surface normal, instance, and semantic segmentation (pixel-wise and bounding boxes). 

in the world, ORBIT configures the sensors required only for a given task. To simulate sensing at different frequencies, each sensor instance has its own internal timer that governs the operating frequency for reading the simulator buffers. Between the timesteps, the sensor returns the previously obtained values. 

Objects are passive entities in the world. While several objects may exist in the scene, the user can define objects of interest for a specified task and set and retrieve properties/states only for them. For any given object, we support the randomization of its textures and physics properties, such as friction material and joint parameters. Similar to the robots class, we also include interfaces to augment the simulator with models for active motion components in an object. For instance, in a refrigerator, the hinge joint is stiff initially due to a magnetic seal but becomes free once the seal is broken. Accounting for these hybrid models in the simulation allows for developing and verifying methods to deal with the varying object dynamics in the real world. 

Addition to above, the world also constitutes visualization markers. We allow programmatic additions of various primitive shapes to the simulator’s GUI, such as axes, spheres, and meshes. These are often useful for development purposes, such as displaying the goal state or visualizing different coordinate frames. We integrate these markers into different robots and controller interfaces to readily allow visualization of useful frames such as the feet or end-effector poses. _b)_ **_Agent_** _:_ An agent refers to the decision-making process (“intelligence”) guiding the embodied system. While roboticists have embraced the modularity of ROS [15], most robot learning frameworks often focus only on the environment (or MDP) definition. This practice leads to code replication and adds friction to switching between different implementations. 

Keeping modularity at its core, an agent in ORBIT comprises various nodes that formulate a computation graph exchanging information between them. Broadly, we consider nodes are of two types: 1) _perception-based i_ . _e_ ., they process inputs into another representation (such as RGB-D image to point-cloud/TSDF), or 2) _action-based i_ . _e_ ., they process inputs into action commands (such as task-level commands to joint commands). Similar to sensors, nodes also contain their own internal timers that control their update frequency. Currently, the flow of information between nodes happens synchronously via Python, which avoids the data exchange 

overhead of service-client protocols. 

_c)_ **_Learning task and agent_** _:_ Paradigms such as RL require specifying a task, a world and may include some computation nodes of the agent. The task logic helps specify the goal for the agent, compute metrics (rewards) to evaluate the agent’s performance, and manage resets. With this component as a separate module, it becomes feasible to use the same world definition for different tasks, similar to learning in the real world, where tasks are specified through extrinsic reward signals. The task definition may also contain different nodes of the agent. An intuitive way to formalize this is by considering that learning for a particular node happens through a _graph cut_ on the agent’s computation graph. 

To further concretize the design motivation, consider the example of learning over task space instead of low-level joint actions for lifting a cube [27]. In this case, the task-space controller, such as inverse kinematics (IK), would typically run at 50 Hz, while the joint controller requires commands at 1000 Hz. Although the task-space controller is a part of the agent’s and not the world’s computation, it is possible to encapsulate that into the task design. This functionality easily allows switching between motion generators, such as IK, operational space control (OSC), or reactive planners. 

## IV. ORBIT: FEATURES 

While various robotic benchmarks have been proposed [4], [1], [5], the right choice of necessary and sufficient tasks to demonstrate “intelligent” behaviors remains an open question. Instead of being prescriptive about tasks, we provide ORBIT as a platform to easily design new tasks. To facilitate the same, we include a diverse set of supported robots, peripheral devices, and motion generators and a large set of tasks for rigid and soft object manipulation for essential skills such as folding cloth, opening the dishwasher, and screwing a nut into a bolt. Each task showcases aspects of physics and renderer that we believe will facilitate answering crucial research questions, such as building representations for deformable object manipulation and learning skills that generalize to different objects and robots. 

_a) Robots:_ We support 4 mobile platforms (one omnidirectional drive base and three quadrupeds), 7 robotic arms (two 6-DoF and five 7-DoF), and 6 end-effectors (four parallel-jaw grippers and two robotic hands). We provide tools to compose different combinations of these articulations into a complex robotic system such as a legged mobile 



Fig. 6: Demonstration of the designed tasks using hand-crafted state machines and task-space controllers. Leveraging recent advances in physics engines, we support high-fidelity simulation of rigid and deformable objects. We include environments that allow switching between robots, objects, observations, and action spaces through configuration files (videos). 

manipulator. This provides a large set of robot platforms, each of which can be switched in the World. 

_b) I/O Devices:_ Devices define the interface to peripheral controllers that teleoperate the robot in real-time. The interface reads the input commands from an I/O device and parses them into control commands for subsequent nodes. This helps not only in collecting demonstrations but also in debugging the task designs. Currently, we include support for Keyboard, Gamepad (Xbox controller), and Spacemouse. 

_c) Motion Generators:_ Motion generators transform high-level actions into lower-level commands by treating input actions as reference tracking signals. For instance, inverse kinematics (IK) [30] interprets commands as the desired end-effector poses and computes the desired joint positions. Employing these controllers, particularly in task space, has been shown to help sim-to-real transferability of robot manipulation policies [2], [27]. 

With ORBIT, we include GPU-based implementations for differential IK [30], operational-space control [31], and joint-level control, which compute commands for several robots efficiently. Additionally, we provide CPU implementation of state-of-the-art model-based planners such as RMPFlow [32] for fixed-arm manipulators and OCS2 [33] for whole-body control of mobile manipulators. To facilitate research in legged robot navigation, such as traversability estimation and path-planning, we also include pre-trained policies for legged locomotion [34] that track base velocity commands. 

_d) Rigid- and Deformable-body Tasks:_ ORBIT includes a suite of tasks for deformable and rigid object manipulation, as well as legged robot control and in-hand manipulation. These tasks serve not only as benchmarks for robotics research but also as examples for users to design new tasks easily. While some of these tasks have existed in prior works [1], [5], [22], [34], we enhance them using the framework’s interfaces to simplify switching between different robots, objects, motion generators, observations, and domain randomization. We also extend manipulation tasks for fixed-arm robots to mobile manipulators. Currently, the tasks mainly focus on a diverse set of skills such as grasping, screwing, stacking, pushing/pulling, pouring, folding, and walking (shown in Fig. 6). A complete and growing list of environments is available on our <u>website.</u> 

## V. EXEMPLAR WORKFLOWS WITH ORBIT 

ORBIT is a unified simulation infrastructure that provides both pre-built environments and easy-to-use interfaces that enables extendability and customization. Owing to highquality physics, sensor simulation, and rendering, ORBIT is useful for multiple robotics challenges in both perception and decision-making. We outline a subset of such use cases through exemplar workflows. 

## _A. Reinforcement Learning_ 

Since the framework primarily stores data as tensors, the data needs to be formatted and converted to data types for different learning frameworks. We provide wrappers to rlgames [35], RSL-rl [34], and stable-baselines-3 [36]. These wrappers make the underlying environment RL framework agnostic and provide users access to a larger set of algorithms for research. 

In Fig. 7, we show the training of Franka-Reach and Franka-Cabinet-Opening with PPO [37] using different RL frameworks and action spaces. Although we ensure the same parameter settings for PPO in the frameworks, we notice a difference in their performance and training time due to implementation differences. Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,00075,000 frames per second (FPS) with 2048 environments, while with stable-baselines3, we receive 6,000-18,000 FPS. 

## _B. Teleoperation and Imitation Learning_ 

Many manipulation tasks are computationally expensive or beyond the reach of current RL algorithms. In these scenarios, bootstrapping from user demonstrations provides a viable path to skill learning. ORBIT provides a data collection interface that is useful for interacting with environments using I/O devices and collecting data similar to roboturk [38]. We also support storing the data in the format desired by robomimic [39], which provides access to training various imitation learning (IL) models through it. 

As an example, we show LfD for the Franka-LiftCube task. For each of the four settings of initial and desired object positions (fixed or random start and desired positions), we collect 2000 trajectories. Using these demonstrations, we train policies using Behavior 



<!-- Start of picture text -->
10 PPO on Franka-Reach 120RSLRL PPO on Franka-Cabinet-Opening<br>100<br>9<br>80<br>60<br>8<br>Stable Baselines3 40<br>RL Games Joint, position<br>7 RSL RL 20 Joint, velocity<br>0 . 5 Steps1 . 0 1 . 5 × 10 7 0 . 5 Steps1 . 0 1 . 5 × 102 . 0 7<br>AverageReturn AverageReturn<br><!-- End of picture text -->

Fig. 7: Example showing RL integration. We include wrappers to various RL frameworks. Additionally, it is possible to easily switch action spaces for training policies with different controllers. The plot shows the mean of the average return over five seeds. 

TABLE II: Showcase of collecting demonstrations using teleoperation and performing imitation learning with them. We evaluate the trained policies for Franka-LiftCube in the same setting ( **No Change** ), changing initial states ( **I)** , goal states ( **G** ), and changing both initial and goal states ( **Both** ). The success rate and trajectory lengths are reported over 100 trials. 

|**Algorithm**|**Avg. Traj. Len**|**Succ. Rate**|**Eval. Setup**|
|---|---|---|---|
||234 _|_ 249|1.00 _|_ 1.00|**No Change**|
|**BC** _|_ **BC-RNN**|307 _|_ 251<br>|0.89 _|_ 1.00<br>|**G**|
||321 _|_ 286<br>|0.47 _|_ 0.88<br>|**I**|
||324 _|_ 293|0.43 _|_ 0.87|**Both**|



Cloning (BC) and BC with an RNN policy (BC-RNN), and show their performance in Table II. 

## _C. Motion planning_ 

Motion planning is one of the well-studied domains in robotics. The traditional Sense-Model-Plan-Act (SMPA) methodology decomposes the complex problem of reasoning and control into possible sub-components. ORBIT supports doing this both procedurally and interactively via the GUI. 

_a) Hand-crafted policies:_ We create a state machine for a given task to perform sequential planning as a separate node in the agent. It provides the goal states for reaching a target object, closing the gripper, interacting with the object, and maneuvering to the next target position. We demonstrate this paradigm for several tasks in Fig. 6. These hand-crafted policies can also be utilized for collecting expert demonstrations for challenging tasks such as cloth manipulation. 

_b) Interactive motion planning:_ We define a system of nodes for grasp generation, teleoperation, task-space control, and motion previewing (shown in Fig. 8). Through the GUI, the user can select an object to grasp and view the possible grasp poses and the robot motion sequences generated using the RMP controller. After confirming the grasp pose, the robot executes the motion and lifts the object. Following this, the user obtains teleoperation control of the robot. 

## _D. Deployment on real robot_ 

Deploying an agent on a real robot faces various challenges, such as dealing with real-time control and safety constraints. Different data transport layers, such as ROSTCP [15] or ZeroMQ (ZMQ) [40], exist for connecting a robotic stack to a real platform. We showcase how these mechanisms can be used with ORBIT to run policies on a real robot. 





<!-- Start of picture text -->
1 2<br>3 4<br><!-- End of picture text -->

Fig. 8: Interactive grasp and motion planning demonstration using ORBIT. The World comprises objects for table-top manipulation. The user can select an object from the GUI to grasp. This triggers an image-based grasp generator and allows previewing of the generated grasps and the robot motion sequence. The user can then choose the grasp and execute the motion on the robot. 







Fig. 9: Using the simulator as a digital twin to compute and apply the same commands on the simulated and real robot via ZMQ connection. We show the Franka Panda arm with an Allegro hand lifting two objects simultaneously, showcasing the realism in contact simulation. For videos, please check the website. 

_a) Using ZMQ:_ To maintain lightweight and efficient communication, we use ZMQ to send joint commands from ORBIT to a computer running the real-time kernel for Franka Emika robot. To abide by the real-time safety constraints, we use a quintic interpolator to upsample the 60 Hz joint commands from the simulator to 1000 Hz for execution on the robot (shown in Fig. 9). 

We run experiments on two configurations of the Franka robot: one with the Franka Emika hand and the other with an Allegro hand. For each configuration, we showcase three tasks: 1) teleoperation using a Spacemouse device, 2) deployment of a state machine and 3) waypoint tracking with obstacle avoidance. The modular nature of the agent makes it easy to switch between different control architectures for each task while using the same interface for the real robot. 

_b) Using ROS:_ A variety of existing robots come with their ROS software stack. In this demonstration, we focus on how policies trained using ORBIT can be exported and deployed on a robotic platform, particularly for the quadrupedal robot from ANYbotics, ANYmal-D. 

We train a locomotion policy entirely in simulation using an actuator network [29] for the legged base. To make the policy robust, we randomize the base mass (22 _±_ 5 kg) and add simulated random pushes. We use the contact reporter to 



<!-- Start of picture text -->
1 2 3<br><!-- End of picture text -->

Fig. 10: Deployment of an RL policy on ANYmal-D robot using ROS connection (video). The policy is trained in simulation and runs at 50 Hz while the actuator net functions at 200 Hz. 





Tetrahedral Mesh (Sim) 

Fig. 11: Comparison of real and simulated data for a clamped beam scenario. The real data is collected using motion markers (shown on left). The simulated data is obtained using the FEM-solver [23] in Isaac Sim over different hexahedral mesh resolutions ( _m_ ). 

obtain the contact forces and use them in reward design. The learned policy is deployed on the robot using the ANYmal ROS stack, (Fig. 10). This sim-to-real transfer indicates the viability of the simulated contact dynamics and its suitability for contact-rich tasks in ORBIT. 

## _E. Simulation Evaluation and Comparison_ 

_a) Evaluation of simulation accuracy:_ Quantitatively measuring the accuracy of physics solvers is an arduous task due to the large variations and unknown mechanics of the real world. Thus, prior frameworks resort to qualitatively comparing the simulation to the physical world by rolling out the same action sequences [8], [10]. While Sec. V-D follows a similar practice to show realism in the rigid body simulation, we discuss the accuracy of deformable body simulation through a controlled experiment. 

We consider a clamped beam made of highly deformable silicone elastomer. Following the setup used in [41], we attach motion capture markers to the beam to collect deformation data under gravity’s effect. In the simulation, we create a similar scenario by attaching a soft beam to a rigid wall and setting the same material properties (Young’s modulus, density, and incompressibility) as the physical beam. As shown in Fig. 11, we observe that the damped oscillations in the simulated data follow closely to the collected real-world data. This showcases the solver’s accuracy [23] and indicates its potential for sim-to-real deformable body manipulation. 

_b) Comparison of simulation throughput:_ We compare the throughput of the tasks in ORBIT with those in other frameworks for rigid (robosuite, Maniskill2, IsaacGymEnvs) and deformable body interactions (DEDO). To ensure a fair comparison, we adapt the environments to have the same action space, simulation frequency, and control decimation. The evaluation is performed on a workstation with a 16-core AMD Ryzen 5950X, 64 GB RAM, and NVIDIA 3090RTX. 

> 2For rigid object environments, the numbers were computed using robosuite v1.4, ManiSkill2 v0.4, Isaac Gym Preview 4, and Isaac Sim 2022.1. For the cloth environment, we used DEDO v0.1 and Isaac Sim 2022.2. 



<!-- Start of picture text -->
× 10 5 Franka-LiftCube × 10 5 ANYmal-Locomotion<br>RoboSuite 3 IsaacGym<br>ManiSkill2 Ours<br>1 . 5<br>IsaacGym<br>Ours 2<br>1 . 0<br>0 . 5 1<br>0 . 0 0<br>256 512 1024 2048 4096 256 512 1024 2048 4096<br>Number of environments Number of environments<br>Throughput (FPS)<br><!-- End of picture text -->

Fig. 12: Simulation throughput for rigid body tasks<sup>2</sup> . CPU-based vectorization is limited to the available memory and scales poorly compared to GPU-accelerated simulation. ORBIT performs at par with IsaacGym since they use the same physics engine. 



<!-- Start of picture text -->
a. Franka-HangCloth b. Effect of cloth mesh resolution<br>4000 4000<br>3000 3000<br>2000 DEDO (574 pts) 2000 294 pts<br>DEDO (294 pts) 574 pts<br>1000 Ours (574 pts) 1000 2203 pts<br>Ours (294 pts) 8623 pts<br>0 0<br>0 100 200 300 400 0 250 500 750 1000<br>Number of environments Number of environments<br>Throughput (FPS)<br><!-- End of picture text -->

Fig. 13: Simulation throughput for cloth hanging task<sup>2</sup> . ORBIT obtains 3 _×_ the throughput than DEDO while using PBD solver [42]. However, increasing the number of nodes or points ( _pts_ ) in the cloth mesh adversely affects its performance. The dotted line shows where the system ran out of memory. 

Frameworks that rely on CPU-vectorization ([2], [4], [10]) show an increase in throughput with the number of environments. However, at around 200-300 environments, their programs crash due to insufficient memory. In contrast, GPU-based parallelization scales better to a larger number of environments and achieves a throughput of _∼_ 10x faster for rigid body environments (Fig. 12) and _∼_ 3x faster for deformable body environments (Fig. 13). For the cloth task, we also examine the impact of using meshes of different resolutions on the throughput. We observe that a higher mesh resolution produces more accurate simulation but requires more computation time. To address this challenge, we intend to provide best practices for tuning the simulation and various sim-ready assets. 

## VI. DISCUSSION 

In this paper, we proposed ORBIT: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier into robotics and robot learning. ORBIT exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the simulation, and advance sensors, actuators, and motion generators at varying operating frequencies. It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for roboticists. The breadth of environments and robotic paradigms possible, as demonstrated in part in Sec. IV and Sec. V, make ORBIT useful for a broad set 

of research questions in robotics. Through experiments, we show a significant throughput improvement on tasks designed in ORBIT with respect to those in other frameworks, and its potential to facilitate sim-to-real transfer. 

By open-sourcing this framework<sup>3</sup> , we aim to reduce the overhead for developing new applications and provide a unified platform for robot learning research. As we continue to enhance and incorporate more features into the framework, we encourage researchers to contribute to transforming it into a comprehensive solution for robotics research. 

## VII. FUTURE WORK 

ORBIT can notably simulate physics at up to 125,000 FPS; however, camera rendering is currently bottlenecked to a total of 270 FPS for ten cameras rendering 640 _×_ 480 images on an RTX 3090. While this number is comparable to other frameworks, we are actively improving the rendering speed through GPU-based acceleration. 

While our experiments demonstrate the effectiveness of rigid-contact modeling and FEM for soft bodies, quantitatively studying the fidelity of the entire simulator (such as rendering, sensors, and physics) remains an area for future exploration. It is important to note that robotics research, particularly in deformable-body manipulation, has infrequently used sim-to-real due to difficulties in achieving fast and accurate simulation and realistic rendering. We believe that ORBIT can help address these challenges and facilitate answering open research questions in these fields. 

Further enhancements to the framework include integrating tactile sensors and 6-axis force-torque sensors. Additionally, we plan to add support for loading assets directly in their native formats (such as URDF and OBJ) instead of USDs to make the framework more versatile and user-friendly. 

## ACKNOWLEDGMENT 

We thank the NVIDIA PhysX and Omniverse teams for their assistance with the simulator, as well as Farbod Farshidian and Mike Y. Michelis for their contributions to OCS2 and data collection of the deformable beam, respectively. 

## REFERENCES 

- [1] T. Yu, D. Quillen, Z. He, R. Julian, K. Hausman, C. Finn, and S. Levine, “Meta-world: A benchmark and evaluation for multi-task and meta reinforcement learning,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2020. 

- [2] Y. Zhu, J. Wong, A. Mandlekar, and R. Martín-Martín, “robosuite: A modular simulation framework and benchmark for robot learning,” in _arXiv preprint arXiv:2009.12293_ , 2020. 

- [3] Y. Urakami, A. Hodgkinson, C. Carlin, R. Leu, L. Rigazio, and P. Abbeel, “Doorgym: A scalable door opening environment and baseline agent,” _CoRR_ , vol. abs/1908.01887, 2019. 

- [4] R. Antonova, p. shi, H. Yin, Z. Weng, and D. Kragic, “Dynamic environments with deformable objects,” in _Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks_ , J. Vanschoren and S. Yeung, Eds., vol. 1. Curran, 2021. 

- [5] S. James, Z. Ma, D. Rovick Arrojo, and A. J. Davison, “Rlbench: The robot learning benchmark & learning environment,” _IEEE Robotics and Automation Letters_ , 2020. 

- [6] C. Li, F. Xia, R. Martín-Martín, M. Lingelbach, S. Srivastava, B. Shen, K. E. Vainio, C. Gokmen, G. Dharan, T. Jain, A. Kurenkov, K. Liu, H. Gweon, J. Wu, L. Fei-Fei, and S. Savarese, “igibson 2.0: Object-centric simulation for robot learning of everyday household tasks,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2021. 

> 3NVIDIA Isaac Sim is free with an individual license. ORBIT is opensourced on GitHub and available at https://isaac-orbit.github.io. 

- [7] A. Szot, A. Clegg, E. Undersander, E. Wijmans, Y. Zhao, J. Turner, N. Maestre, M. Mukadam, D. Chaplot, O. Maksymets, A. Gokaslan, V. Vondrus, S. Dharur, F. Meier, W. Galuba, A. Chang, Z. Kira, V. Koltun, J. Malik, M. Savva, and D. Batra, “Habitat 2.0: Training home assistants to rearrange their habitat,” in _Advances in Neural Information Processing Systems (NeurIPS)_ , 2021. 

- [8] X. Lin, Y. Wang, J. Olkin, and D. Held, “Softgym: Benchmarking deep reinforcement learning for deformable object manipulation,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2020. 

- [9] C. Gan, J. Schwartz, S. Alter, D. Mrowca, M. Schrimpf, J. Traer, J. De Freitas, J. Kubilius, A. Bhandwaldar, N. Haber, M. Sano, K. Kim, E. Wang, M. Lingelbach, A. Curtis, K. Feigelis, D. Bear, D. Gutfreund, D. Cox, A. Torralba, J. J. DiCarlo, J. Tenenbaum, J. McDermott, and D. Yamins, “Threedworld: A platform for interactive multi-modal physical simulation,” in _Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks_ , vol. 1. Curran, 2021. 

- [10] J. Gu, F. Xiang, X. Li, Z. Ling, X. Liu, T. Mu, Y. Tang, S. Tao, X. Wei, Y. Yao, X. Yuan, P. Xie, Z. Huang, R. Chen, and H. Su, “Maniskill2: A unified benchmark for generalizable manipulation skills,” in _International Conference on Learning Representations (ICLR)_ , 2023. 

- [11] F. Xiang, Y. Qin, K. Mo, Y. Xia, H. Zhu, F. Liu, M. Liu, H. Jiang, Y. Yuan, H. Wang, _et al._ , “Sapien: A simulated part-based interactive environment,” in _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2020. 

- [12] K. Ehsani, W. Han, A. Herrasti, E. VanderBilt, L. Weihs, E. Kolve, A. Kembhavi, and R. Mottaghi, “Manipulathor: A framework for visual object manipulation,” in _IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2021. 

- [13] V. Makoviychuk, L. Wawrzyniak, Y. Guo, M. Lu, K. Storey, M. Macklin, D. Hoeller, N. Rudin, A. Allshire, A. Handa, and G. State, “Isaac gym: High performance gpu based physics simulation for robot learning,” in _Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks_ , J. Vanschoren and S. Yeung, Eds., vol. 1. Curran, 2021. 

- [14] M. Savva, A. Kadian, O. Maksymets, Y. Zhao, E. Wijmans, B. Jain, J. Straub, J. Liu, V. Koltun, J. Malik, D. Parikh, and D. Batra, “Habitat: A Platform for Embodied AI Research,” in _IEEE/CVF International Conference on Computer Vision (ICCV)_ , 2019. 

- [15] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs, R. Wheeler, A. Y. Ng, _et al._ , “Ros: an open-source robot operating system,” in _ICRA workshop on open source software_ , vol. 3, 2009. 

- [16] NVIDIA, “Isaac sim - robotics simulation and synthetic data generation,” https://developer.nvidia.com/isaac-sim, 2023, (accessed on May 2, 2023). 

- [17] E. Todorov, T. Erez, and Y. Tassa, “Mujoco: A physics engine for model-based control,” in _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2012. 

- [18] E. Coumans, , and Y. Bai, “Pybullet, a python module for physics simulation for games, robotics and machine learning,” https://pybullet. org/wordpress/, 2023, (accessed on May 2, 2023). 

- [19] M. Macklin, M. Müller, N. Chentanez, and T.-Y. Kim, “Unified particle physics for real-time applications,” _ACM Trans. Graph._ , vol. 33, no. 4, jul 2014. 

- [20] E. Ménager, P. Schegg, E. Khairallah, D. Marchal, J. Dequidt, P. Preux, and C. Duriez, “SofaGym: An open platform for Reinforcement Learning based on Soft Robot simulations,” _Soft Robotics_ , 2022. 

- [21] NVIDIA, “Physx sdk,” https://developer.nvidia.com/physx-sdk, 2023, (accessed on May 2, 2023). 

- [22] Y. Narang, K. Storey, I. Akinola, M. Macklin, P. Reist, L. Wawrzyniak, Y. Guo, A. Moravanszky, G. State, M. Lu, _et al._ , “Factory: Fast contact for robotic assembly,” _Robotics: Science and Systems (RSS)_ , 2022. 

- [23] M. Macklin and M. Muller, “A constraint-based formulation of stable neo-hookean materials,” in _ACM SIGGRAPH Conference on Motion, Interaction and Games_ , New York, NY, USA, 2021. 

- [24] M. Macklin, K. Storey, M. Lu, P. Terdiman, N. Chentanez, S. Jeschke, and M. Müller, “Small steps in physics simulation,” in _ACM SIGGRAPH/Eurographics Symposium on Computer Animation_ , 2019. 

- [25] S. G. Parker, J. Bigler, A. Dietrich, H. Friedrich, J. Hoberock, D. Luebke, D. McAllister, M. McGuire, K. Morley, A. Robison, and M. Stich, “Optix: A general purpose ray tracing engine,” _ACM Transactions On Graphics_ , vol. 29, no. 4, 2010. 

- [26] S. Shah, D. Dey, C. Lovett, and A. Kapoor, “Airsim: High-fidelity visual and physical simulation for autonomous vehicles,” in _Field and Service Robotics_ , 2017. 

- [27] R. Martín-Martín, M. Lee, R. Gardner, S. Savarese, J. Bohg, and A. Garg, “Variable impedance control in end-effector space. an action space for reinforcement learning in contact rich tasks,” in _IEEE/RSJ_ 

_International Conference of Intelligent Robots and Systems (IROS)_ , 2019. 

- [28] J. Straub, T. Whelan, L. Ma, Y. Chen, E. Wijmans, S. Green, J. J. Engel, R. Mur-Artal, C. Ren, S. Verma, _et al._ , “The replica dataset: A digital replica of indoor spaces,” _arXiv preprint arXiv:1906.05797_ , 2019. 

- [29] J. Hwangbo, J. Lee, A. Dosovitskiy, D. Bellicoso, V. Tsounis, V. Koltun, and M. Hutter, “Learning agile and dynamic motor skills for legged robots,” _Science Robotics_ , vol. 4, no. 26, 2019. 

- [30] S. R. Buss and J.-S. Kim, “Selectively damped least squares for inverse kinematics,” _Journal of Graphics Tools_ , vol. 10, 2005. 

- [31] O. Khatib, “Inertial properties in robotic manipulation: An objectlevel framework,” _The International Journal of Robotics Research_ , vol. 14, no. 1, 1995. 

- [32] C.-A. Cheng, M. Mukadam, J. Issac, S. Birchfield, D. Fox, B. Boots, and N. Ratliff, “Rmpflow: A geometric framework for generation of multitask motion policies,” _IEEE Transactions on Automation Science and Engineering_ , vol. 18, no. 3, 2021. 

- [33] M. Mittal, D. Hoeller, F. Farshidian, M. Hutter, and A. Garg, “Articulated object interaction in unknown scenes with whole-body mobile manipulation,” _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2022. 

- [34] N. Rudin, D. Hoeller, P. Reist, and M. Hutter, “Learning to walk in minutes using massively parallel deep reinforcement learning,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2022. 

- [35] D. Makoviichuk and V. Makoviychuk, “rl-games: A high-performance framework for reinforcement learning,” https://github.com/Denys88/rl_ games, May 2022. 

- [36] A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and N. Dormann, “Stable-baselines3: Reliable reinforcement learning implementations,” _Journal of Machine Learning Research_ , 2021. 

- [37] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” _arXiv preprint arXiv:1707.06347_ , 2017. 

- [38] A. Mandlekar, Y. Zhu, A. Garg, J. Booher, M. Spero, A. Tung, J. Gao, J. Emmons, A. Gupta, E. Orbay, _et al._ , “Roboturk: A crowdsourcing platform for robotic skill learning through imitation,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2018. 

- [39] A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni, L. Fei-Fei, S. Savarese, Y. Zhu, and R. Martin-Martin, “What matters in learning from offline human demonstrations for robot manipulation,” in _Conference on Robot Learning (CoRL)_ . PMLR, 2022. 

- [40] P. Hintjens, _ZeroMQ: messaging for many applications_ . " O’Reilly Media, Inc.", 2013. 

- [41] M. Dubied, M. Y. Michelis, A. Spielberg, and R. K. Katzschmann, “Sim-to-real for soft robots using differentiable fem: Recipes for meshing, damping, and actuation,” _IEEE Robotics and Automation Letters_ , vol. 7, no. 2, 2022. 

- [42] M. Macklin and M. Müller, “Position based fluids,” _ACM Transactions on Graphics_ , vol. 32, no. 4, 2013. 

- [43] A. Allshire, M. Mittal, V. Lodaya, V. Makoviychuk, D. Makoviichuk, F. Widmaier, M. Wüthrich, S. Bauer, A. Handa, and A. Garg, “Transferring dexterous manipulation from gpu simulation to a remote real-world trifinger,” _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , 2022. 

## APPENDIX A: AUTHOR CONTRIBUTIONS 

The following lists author contributions by the type: 

- _Designed and built the core infrastructure:_ M. Mittal, D. Hoeller, N. Rudin 

- _Integrated robots into the simulator:_ M. Mittal, J. Liu 

- _Implemented motion generators:_ M. Mittal, J. Liu 

- _Added environments for locomotion:_ M. Mittal, D. Hoeller, N. Rudin 

- _Added environments for rigid object manipulation:_ M. Mittal, J. Liu, A. Yuan 

- _Added environments for deformable object manipulation:_ C. Yu, Q. Yu 

- _Ran workflows evaluations:_ J. Liu, C. Yu, Q. Yu 

- _Conducted sim-to-real experiments on ANYmal robot:_ M. Mittal, D. Hoeller 

- _Provided NVIDIA Isaac Sim support:_ Y. Guo, H. Mazhar, B. Babich, G. State 

- _Managed or advised on the project:_ A. Mandlekar, M. Hutter, A. Garg 

- _Wrote the paper:_ M. Mittal, A. Garg 

## APPENDIX B: MOTIVATION BEHIND ORBIT 

Over the years, NVIDIA has developed a number of tools for robotics and AI. These tools leverage the power of GPUs to accelerate the simulation both in terms of speed and realism. They show great promise in the field of simulation technology and are being used by many researchers and companies worldwide. 

**Isaac Gym** [13] provides a high-performance GPU-based physics simulation for robot learning. It is built on top of PhysX which supports GPU-accelerated simulation of rigid bodies and a Python API to directly access physics simulation data. Through an end-to-end GPU pipeline, it is possible to achieve high frame rates compared to CPU-based physics engines. The tool has been used successfully in a number of research projects, including legged locomotion [34], in-hand manipulation [43], and industrial assembly [22]. 

Despite Isaac Gym’s success and adoption, it is not designed to be a general-purpose simulator for robotics. For instace, it does not include interaction between deformable and rigid objects, high-fidelity rendering, and support for ROS. The tool has been primarily designed as a preview release to showcase the capabilities of the underlying physics engine. With the release of Isaac Sim, NVIDIA is building a general-purpose simulator for robotics and has integrated the functionalities of Isaac Gym into Isaac Sim. 

**Isaac Sim** is a robot simulation toolkit built on top of Omniverse, which is a general-purpose platform that aims to unite complex 3D workflows. Isaac Sim leverages the latest advances in graphics and physics simulation to provide a high-fidelity simulation environment for robotics. It supports ROS/ROS2, various sensor simulations, tools for domain randomization, and synthetic data creation. Overall, it is a powerful tool for roboticists and is a huge step forward in the field of robotics simulation. 

With the release of the above two tools, NVIDIA also released an open-sourced set of RL environments called IsaacGymEnvs and OmniIsaacGymEnvs, which use Isaac Gym and Isaac Sim respectively. These environments have been designed to display the capabilities of the underlying simulators and provide a great starting point to understand what is possible with the simulators for robot learning. However, these repositories are constrained by their limited integration with different RL libraries (beyond RL-Games), lack of modularity for scalable environment design, and inadequate support for paradigms beyond RL. It is these deficiencies that sparked the development of the ORBIT framework, aiming to bridge this gap and empower researchers and developers alike. 

- _Performed throughput comparisons:_ C. Yu, M. Mittal 

- _Conducted sim-to-real experiments on Franka arm:_ R. Singh, J. Liu 

