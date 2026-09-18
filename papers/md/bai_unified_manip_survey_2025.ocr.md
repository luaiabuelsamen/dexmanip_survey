<!-- page 1 (ocr) -->
A Comprehensive Survey on Robot Manipulation
V2: 2026-08-15
Towards a Unified Understanding of Robot
Manipulation: A Comprehensive Survey
Shuanghao Bai1∗†
Wenxuan Song2∗
Jiayi Chen2∗
Yuheng Ji3∗
Zhide Zhong2∗
Jin Yang1∗
Han
Zhao4,5∗
Wanqi Zhou1∗
Wei Zhao4,5∗
Zhe Li6∗
Pengxiang Ding4,5
Cheng Chi7
Haoang Li2
Chang
Xu6
Xiaolong Zheng3
Donglin Wang4
Shanghang Zhang7,8
Badong Chen1
1 Xi’an Jiaotong University, 2 Hong Kong University of Science and Technology (Guangzhou), 3 Chinese Academy of Sciences,
4 Westlake University, 5 Zhejiang University, 6 University of Sydney, 7 BAAI, 8 Peking University
† Project Lead
∗Core Contributors
Corresponding Authors
chenbd@mail.xjtu.edu.cn
Awesome-Robotics-Manipulation
Abstract | Embodied intelligence has witnessed remarkable progress in recent years, driven by advances in
computer vision, natural language processing, and the rise of large-scale multimodal models. Among its core
challenges, robot manipulation stands out as a fundamental yet intricate problem, requiring the seamless
integration of perception, planning, and control to enable interaction within diverse and unstructured environ-
ments. This survey presents a comprehensive overview of robotic manipulation, encompassing foundational
background, task-organized benchmarks and datasets, and a unified taxonomy of existing methods. We extend
the classical division between high-level planning and low-level action modeling by broadening high-level
planning to include language, code, motion, affordance, and 3D representations, while introducing a new
taxonomy of low-level learning-based action modeling grounded in training paradigms such as input modeling,
latent learning, and policy learning. Furthermore, we provide the first dedicated taxonomy of key bottlenecks,
focusing on data collection, utilization, and generalization, and conclude with an extensive review of real-world
applications. Compared with prior surveys, our work offers both a broader scope and deeper insight, serving as
an accessible roadmap for newcomers and a structured reference for experienced researchers.
Task Type
§ 4
Grasping
Basic 
Manipulation
Mobile 
Manipulation
Quadrupedal 
Manipulation
Humanoid 
Manipulation
Dexterous 
Manipulation
Deformable Object 
Manipulation
Soft Robotic 
Manipulation
Language
…
Vision
Touch
Audio
Input Modeling
§ 6.2
What and how to input
How to obtain and learn latent
How to decode latent to action
Latent Learning
§ 6.3
Policy Learning
§ 6.4
𝑋𝑋
𝑍𝑍
𝐴𝐴
Learning Paradigms
§ 6.1
Reinforcement Learning
Imitation Learning
w/ Auxiliary Tasks
encode and fuse
decode
Diffusion
Autoregressive
VA, VLA, TLA, …
Pretrained Latent &
Latent Action Learning
control
Simulators, Benchmarks 
and Datasets § 3
Environment
Actor
High-level 
Planning § 5
Thinking
Low-level
Action 
Modeling
Robot Type
§ 2.1
Control Paradigms 
Application
§ 8
Industry
Agriculture
Art
Household
AI4Science
Sports
simple tasks
with more complex hands, objects
with complex mobile platforms
Datasets
Action
Learning-based
§ 6
Bottlenecks § 7
Data
§ 7.1
Generalization 
§ 7.2
Agent
§ 7.3
Human-Robot 
Collaboration § 7.4
Video
Code
Task 
Plan
3D repres-
entations
Affordance
High-level Planning § 5
Geometric
Constraint
Figure 1 | Overview of the survey. We first provide a broad introduction to existing benchmarks,
datasets, and manipulation tasks, followed by an extensive review of representative methods with a
particular focus on learning-based action modeling. We then discuss two fundamental challenges,
namely data and generalization, and conclude with an overview of their diverse applications.
arXiv:2510.10903v2  [cs.RO]  15 Aug 2026
1}
(¢]
Pa
en Cy
 — 2
>
=
es
~
&
[<>
Noreen:
D>
HN
a J
CC JC
J? &
o
CC JC JCC OOo cy


<!-- page 2 (ocr) -->
Contents
1
Introduction
5
1.1
Survey Scope and Key Research Questions . . . . . . . . . . . . . . . . . . . . . . . .
5
1.2
Comparison with Previous Surveys and Contributions . . . . . . . . . . . . . . . . . .
6
2
Background
7
2.1
Hardware Platforms for Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.2
Low-Level Action Modeling: Non-Learning and Learning-Based Paradigms
. . . . . .
9
2.2.1
Non-Learning-Based Action Modeling . . . . . . . . . . . . . . . . . . . . . . .
9
2.2.2
Learning-Based Action Modeling
. . . . . . . . . . . . . . . . . . . . . . . . .
10
2.3
Robotics Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
2.4
Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3
Simulators, Benchmarks and Datasets
13
3.1
Grasping Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.2
Single-Embodiment Manipulation Simulators and Benchmarks . . . . . . . . . . . . .
15
3.3
Cross-Embodiment Manipulation Simulators and Benchmarks . . . . . . . . . . . . .
16
3.4
Trajectory Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
3.5
Embodied QA and Affordance Datasets . . . . . . . . . . . . . . . . . . . . . . . . . .
18
3.6
Human Video Datasets and Video-World-Model Benchmarks . . . . . . . . . . . . . .
18
4
Manipulation Tasks
19
4.1
Grasping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
4.2
Basic Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
4.3
Dexterous Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
4.4
Soft Robotic Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
4.5
Deformable Object Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
4.6
Mobile Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
4.7
Quadrupedal Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
4.8
Humanoid Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
4.9
Aerial Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
4.10 Underwater Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
5
High-level Planning
31
5.1
LLM-Based Task Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
5.2
MLLM-based Task Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
5.3
Programmatic Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
5.4
Geometric Constraint-based Planning . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
5.5
Affordance-Based Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
5.6
3D Representation-Based Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
2


<!-- page 3 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
5.7
Video-Based Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
6
Low-level Learning-based Action Modeling
40
6.1
Learning Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
6.1.1
Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
6.1.2
Imitation Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
6.1.3
Bridging Reinforcement and Imitation Learning . . . . . . . . . . . . . . . . .
48
6.1.4
Learning with Auxiliary Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
6.2
Input Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
6.2.1
Vision-Action Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
6.2.2
Vision-Language-Action Models . . . . . . . . . . . . . . . . . . . . . . . . . .
57
6.2.3
Tactile-based Action Models . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
6.2.4
Extra Modalities as Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
6.3
Latent Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
6.3.1
Pretrained Latent Learning
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
6.3.2
Latent Action Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
6.4
Policy Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
6.4.1
MLP-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
6.4.2
Transformer-based Policy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
6.4.3
Diffusion Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
6.4.4
Flow Matching Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
6.4.5
SSM-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
6.4.6
SNN-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
6.4.7
Frequency-based Policy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
6.4.8
Action Tokenization and Structured Action Representation . . . . . . . . . . .
75
6.4.9
Drift-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
7
Approaches to the Key Bottlenecks
76
7.1
Data Collection and Utilization
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
76
7.1.1
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
76
7.1.2
Data Utilization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
7.2
Generalization
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
7.2.1
Environment Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
7.2.2
Task Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
7.2.3
Cross-Embodiment Generalization
. . . . . . . . . . . . . . . . . . . . . . . .
89
7.3
Agent
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
90
7.4
Human–Robot Interaction and Collaboration . . . . . . . . . . . . . . . . . . . . . . .
91
8
Applications
92
8.1
Household Assistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
8.2
Agriculture
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
93
3


<!-- page 4 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
8.3
Industry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
8.4
AI4Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
8.5
Art . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
8.6
Sports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
9
Prospective Future Research Directions
95
9.1
Building a General-Purpose and Self-Evolving Robot Brain . . . . . . . . . . . . . . .
95
9.2
Scaling Robot Intelligence Beyond Robot Data . . . . . . . . . . . . . . . . . . . . . .
96
9.3
Multimodal and Contact-Rich Physical Interaction . . . . . . . . . . . . . . . . . . . .
97
9.4
Safety, Recovery, and Collaborative Autonomy . . . . . . . . . . . . . . . . . . . . . .
98
10 Conclusion
99
Author Contributions
99
4


<!-- page 5 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
1. Introduction
In recent years, embodied intelligence has attracted increasing attention, largely driven by advances
in computer vision and natural language processing, particularly the success of large-scale models.
These developments have not only demonstrated remarkable machine intelligence but also offered a
glimpse into the potential of artificial general intelligence (AGI). Building on this progress, large-scale
language and multimodal models [1–3] have accelerated the development and deployment of robotic
systems by enhancing perceptual and semantic understanding, enabling operation in unstructured
environments, and supporting natural-language task specification. Their zero-shot and few-shot
generalization capabilities improve the adaptability of robotic systems, while multimodal interaction
enhances usability and reduces deployment barriers in real-world scenarios.
Robot manipulation is a core and extensively studied problem in embodied intelligence, referring
to a robot’s ability to perceive its environment, plan task execution, generate appropriate actions,
and control its effectors to physically interact with and modify the environment, such as by grasping,
moving, or using objects. Its development spans classical rule-based and non-learning methods [4–7]
from the late twentieth century through the 2010s, followed by deep learning-based approaches [8,
9], the widespread adoption of imitation learning (IL) and reinforcement learning (RL) [10, 11],
and, more recently, the integration of large language and vision-language models into IL and RL
frameworks [12, 13]. In this survey, non-learning methods are primarily introduced as methodological
background, while the main discussion focuses on data-driven and learning-based approaches.
1.1. Survey Scope and Key Research Questions
In this survey, we aim to provide newcomers with a concise roadmap to the development, tasks, and
methods of robot manipulation, while offering experienced researchers a structured reference and a
broader perspective on the field. To this end, we organize the survey around the following research
questions:
1. What benchmarks and task categories define robot manipulation today? We review the
current landscape of benchmarks in Section 3 and organize representative manipulation problems
into major task categories in Section 4.
2. What methods have been proposed to address these manipulation tasks? Beyond basic
manipulation, Section 4 reviews representative approaches for dexterous, deformable-object, mobile,
quadrupedal, and humanoid manipulation. For these categories, we briefly introduce classical
non-learning methods and place greater emphasis on learning-based approaches, including RL, IL,
VLA models, and strategy-augmented methods, while highlighting the distinct methodological and
embodiment-specific challenges of each domain.
Basic manipulation, in contrast, represents the most extensively studied setting and is supported by
a substantially richer body of literature. We therefore provide a dedicated analysis in Sections 5 and 6,
distinguishing between high-level planning methods that produce task-level plans or intermediate
planning artifacts and low-level action-modeling methods that generate executable robot actions
from observations and task specifications. Actuation-level control, which converts these actions into
joint-level position, velocity, or torque commands, is introduced separately as part of the foundational
background. Although this taxonomy is developed primarily in the context of basic manipulation, its
underlying distinction between planning, action generation, and physical execution is also applicable
to other manipulation settings.
3. What are the current bottlenecks in robot manipulation? We identify data collection and
utilization, together with generalization, as two central challenges. Section 7.1 reviews the evolution
5


<!-- page 6 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
of robot-data collection and examines strategies for improving the efficiency and effectiveness of
data utilization during training. Section 7.2 analyzes the major forms of generalization in robot
manipulation and summarizes the corresponding methodological strategies.
4. What are the practical applications of manipulation techniques beyond research? We
survey how advances in robot manipulation are being deployed across a wide range of real-world
application domains in Section 8.
1.2. Comparison with Previous Surveys and Contributions
First, compared with prior surveys that are limited in scope, our work provides a comprehen-
sive and systematic overview of robot manipulation. Existing surveys typically adopt narrower
perspectives. Some focus on particular task domains, such as dexterous manipulation [14, 15],
deformable-object manipulation [16], mobile manipulation [17], or humanoid manipulation [18].
Others emphasize methodological paradigms that recur across different tasks, including vision-
language-action models [19–22], diffusion models [23], and generative approaches [24]. A further
group concentrates on specific methodological concepts, such as language-conditioned learning [25]
or object-centric representations [26]. Several broader embodied-intelligence surveys cover a wide
range of topics but treat manipulation only as one subsection, providing insufficient depth for a
systematic understanding of the field [27, 28].
Second, our survey introduces a unified taxonomy that covers the robot-manipulation
pipeline more extensively than existing categorizations. The resulting organization provides an
accessible blueprint for newcomers while offering experienced researchers a structured perspective
on the relationships among different problem formulations and methodological paradigms.
Specifically, we provide a comprehensive background in Section 2, covering hardware embodi-
ments, actuation-level control paradigms, and foundational robotic models. We introduce benchmarks
and datasets organized by manipulation-task category in Section 3, present a systematic overview
of representative manipulation tasks, and develop a refined methodological taxonomy in Sections 5
and 6. While prior surveys often distinguish broadly between high-level planning and low-level
control, we refine this division by separating high-level planning, low-level action modeling, and
actuation-level control according to the system interface and the form of the model output. We
broaden high-level planning in Section 5 to encompass planning representations expressed through
language, code, motion, affordances, and 3D scene structures. For low-level action modeling in
Section 6, we propose a taxonomy grounded in training paradigms and further organize existing
methods according to learning strategy, input modeling, latent learning, and policy learning.
In addition, we provide a detailed analysis of current bottlenecks in robot manipulation in Section 7
and introduce a dedicated taxonomy covering data collection, data utilization, and generalization.
Finally, Section 8 presents a broader and more systematic review of real-world applications than those
provided in previous surveys.
Finally, based on these contributions and recent developments in the field, we identify
emerging research trends and outline four promising directions for future work. The first
concerns the development of a genuine robot brain, namely a general-purpose architecture that
integrates broad perception, reasoning, action-generation, and control capabilities. The second
addresses the data bottleneck, as current robot learning has not yet exhibited a reliable scaling law
comparable to those observed in language and vision, largely because of the high cost of physical
data acquisition and the limitations of simulation. The third concerns perception, particularly the
need for richer multimodal sensing and more reliable interaction with deformable, articulated, and
otherwise physically complex objects. The fourth emphasizes safe human–robot coexistence, which
6


<!-- page 7 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Hello Stretch
Franka Panda
UR5
Kinova Gen3
Google Robot
xArm
WidowX
Robotiq 2f-85
Shadow Hand
D’Kitty and D’Claw
RBO Hand 3
SpiRobs
COBOT Magic 
ALOHA
ABB YuMi
Unitree Go2
Boston Dynamics Spot
Unitree G1
Single Arm
Bimanual Arms
Soft Hands
Allegro Hand
Dexterous Hands
Parallel-Jaw Gripper
Mobile Robots
Quadruped Robots
Figure 02
Humanoid Robots
hand
+ arm
+ mobile platform
Complexity
Unitree Dex3
Inspire Hand
Linker L20 Hand
Wuji Hand
OnRobot 2FG7
Franka Hand
UMI
qb SoftHand
Galaxea R1 Lite
AgiBot A2
Galaxea R1 Pro
Tienkung3.0
PR2
Walker S2
Galbot S1
Booster K1
Alphabot2
Figure 2 | Overview of hardware platforms.
remains essential for the large-scale deployment of robotic systems in real-world environments.
2. Background
In this section, we first introduce the hardware types commonly used in robotic manipulation (Sec-
tion 2.1). We then outline the main categories of control strategies, namely non-learning-based and
learning-based approaches (Section 2.2). Next, we review the robotic models widely adopted for
learning-based control (Section 2.3) and discuss the evaluation protocols used to assess the robotic
models within these frameworks (Section 2.4).
2.1. Hardware Platforms for Manipulation
Before introducing manipulation tasks and their corresponding methodologies, it is important to
first understand the hardware systems that enable these operations. Robotic manipulation can be
achieved through various embodiments composed of fundamental components such as hands, arms,
and mobile platforms. Different combinations of these components define specific embodiments and
their functional capabilities. For example, pairing a parallel-jaw gripper with a Franka Panda arm
enables basic manipulation tasks such as pick-and-place or insertion, while integrating a Unitree G1
7
oes
nt ®


<!-- page 8 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
humanoid platform with a dexterous hand allows for humanoid-level manipulation that demands
greater dexterity and coordination. We summarize the commonly used robotic hardware types in
current research in Figure 2.
Parallel-Jaw Grippers. Parallel-jaw grippers are among the most widely adopted end-effectors in
robotic manipulation because their low-dimensional actuation, repeatable contact geometry, and
reliable force transmission simplify control, demonstration collection, and policy learning. Repre-
sentative commercial platforms include the Robotiq 2F-851, OnRobot 2FG72, and Franka Hand3.
Research-oriented designs further extend this basic morphology, including DexWrist [29], which
augments a gripper with additional wrist dexterity, and UMI [30], which integrates a portable gripper
and visual sensing interface for scalable real-world demonstration collection. Although these grippers
provide limited in-hand dexterity, their compact action spaces and robust grasping behavior make
them effective for pick-and-place, insertion, and large-scale imitation-learning experiments.
Dexterous Hands. Dexterous hands employ multiple articulated fingers and higher-dimensional
actuation to support contact-rich manipulation beyond simple opening and closing. Representative
multi-finger end-effectors include the Robotiq 3-Finger Adaptive Robot Gripper4, Allegro Hand5,
Shadow Dexterous Hand6, Unitree Dex3-17, D’Claw and D’Kitty from the ROBEL platform [31], Inspire
Hand8, Linker Hand L209, and Wuji Hand10, together with other learning-oriented designs [32, 33].
Their articulated structures enable object reorientation, in-hand manipulation, tool use, and coordi-
nated multi-contact interaction. However, the increased number of controllable joints also enlarges
the action space and places substantially greater demands on sensing, calibration, demonstration
quality, and closed-loop policy learning.
Soft Hands. Soft hands exploit material compliance, underactuated transmission, or deformable
actuation to conform passively to object geometry. Representative platforms include the RBO Hand
3 [34], Festo BionicSoftHand11, SpiRobs [35], and qb SoftHand12. In contrast to rigid dexterous hands,
these systems partially transfer the burden of contact adaptation from explicit control to mechanical
compliance, improving grasp robustness and interaction safety under geometric uncertainty. This
adaptability is obtained at the cost of less precise kinematic modeling and more difficult estimation of
contact states and deformation-dependent dynamics.
Single Arm. Fixed-base single-arm manipulators remain the predominant platforms for learning-
based manipulation because they provide accurate and repeatable motion within a well-defined
workspace. Commonly used systems include the KUKA LBR iiwa13, Franka Emika Panda [36]14,
UR5 and UR1015, Kinova Gen316, xArm6 and xArm717, and WidowX18. These platforms typically
provide six or seven degrees of freedom and are widely employed for behavior cloning, reinforcement
learning, visuomotor control, and sim-to-real evaluation. More recently, low-cost and reproducible
systems supported by open-source ecosystems such as LeRobot19 have lowered the barrier to physical
experimentation and facilitated standardized data collection across research groups.
Bimanual Arms. Bimanual systems extend the workspace and contact capabilities of single-arm
platforms by coordinating two manipulators. Representative systems include dual Franka Panda
configurations20, ALOHA [37], and ABB YuMi21. They support tasks such as bilateral assembly, object
handover, deformable-object manipulation, container opening, and coordinated tool use. Nevertheless,
bimanual manipulation introduces additional challenges associated with temporal synchronization,
inter-arm collision avoidance, assignment of complementary roles, and learning coupled actions
whose effectiveness depends on the coordinated behavior of both arms.
Mobile Manipulators. Mobile manipulators combine one or more arms with a movable base, thereby
extending manipulation beyond the bounded workspace of a fixed-base robot. Representative plat-
forms include COBOT Magic22, Hello Robot Stretch 323, the Google mobile manipulation platform24,
8


<!-- page 9 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Galaxea R1 Lite25, PR226, and TIAGo27. By coupling navigation, base positioning, torso adjustment,
and arm motion, these platforms can perform object fetching, household assistance, long-horizon
rearrangement, and human–robot interaction across extended environments. Their operational range
also introduces partial observability, accumulated localization error, dynamic obstacles, and the need
to coordinate manipulation and locomotion within a unified decision process.
Quadruped Robots. Quadruped platforms provide agile locomotion over uneven terrain and can be
equipped with articulated arms or specialized end-effectors to support mobile manipulation. Represen-
tative systems include Unitree Go2, B1, and Aliengo28, together with Boston Dynamics Spot29. Their
legged morphology enables operation in environments that are inaccessible to conventional wheeled
platforms, including stairs, rough terrain, and infrastructure-inspection settings. Manipulation on
quadrupeds nevertheless requires tight coupling among locomotion, body stabilization, arm motion,
and contact-force regulation, particularly when manipulation forces disturb the support configuration
of the robot.
Humanoid Robots. Humanoid and anthropomorphic whole-body platforms are designed to operate
in spaces, use tools, and interact with objects originally configured for humans. Representative
systems include Tesla Optimus Gen 230, Boston Dynamics Atlas31, Figure 0232, 1X NEO33, Unitree
G134, AgiBot A235, Tiangong 3.036, UBTECH Walker S237, Booster K138, AlphaBot 239, Galbot S140,
and Galaxea R1 Pro41. This category increasingly encompasses both bipedal humanoids and wheeled
anthropomorphic systems that retain a human-scale torso and manipulation workspace. Compared
with arm-centered platforms, these embodiments expand the action space to include locomotion,
balance, torso motion, whole-body contact, and coordinated use of multiple limbs. They therefore
provide a promising substrate for general-purpose embodied intelligence while introducing substantial
challenges in data efficiency, safety, state estimation, hierarchical control, and reproducible evaluation.
2.2. Low-Level Action Modeling: Non-Learning and Learning-Based Paradigms
In this survey, low-level action modeling broadly refers to methods that transform task goals, environ-
ment states, or observations into executable robot paths, trajectories, actions, or action sequences.
This definition is based on the exposed system interface rather than the internal computational mech-
anism. Accordingly, low-level actions may be constructed analytically, obtained through sampling
or optimization, or learned from data. They are subsequently translated into joint-level position,
velocity, force, or torque commands by actuation-level controllers.
Similar to how humans may follow explicit rules, such as stopping at a red light, or acquire
adaptive skills through repeated practice, such as learning to ride a bicycle, low-level robot actions
can be generated through either classical non-learning methods or data-driven learning approaches.
Non-learning methods offer interpretability, predictable behavior, and explicit constraint handling in
well-defined settings, whereas learning-based methods provide greater adaptability and generalization
in complex or uncertain environments.
2.2.1. Non-Learning-Based Action Modeling
Non-learning-based action modeling generates executable paths, trajectories, or control sequences
using analytical construction, search, optimization, and model-based control without learning the
underlying observation-to-action mapping from data. We include these methods as foundational
counterparts to learning-based action models and because they are frequently combined with learned
perception, planning, or policy modules. However, they are not the primary focus of the methodological
taxonomy developed in this survey.
9


<!-- page 10 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Interpolation-Based Planning. Classical manipulators often employ interpolation-based plan-
ning [38, 39], in which smooth joint-space trajectories are generated, typically offline, by fitting
polynomial curves, such as cubic splines, between predefined start and goal states. These methods
are computationally lightweight and straightforward to deploy, making them prevalent in repetitive
and well-structured industrial tasks. However, their dependence on predefined boundary conditions
provides limited adaptability to dynamic or uncertain environments, constraining their applicability
in unstructured settings.
Sampling-Based Planning. Sampling-based planners [40–43] construct feasible paths by sampling
configuration space and incrementally building a graph or tree of collision-free states, rather than
explicitly representing free space or solving a large global optimization problem. Canonical algorithms
include Rapidly-exploring Random Trees (RRT) [41, 43] and Probabilistic Roadmaps (PRM) [42],
together with asymptotically optimal variants such as RRT*. These methods scale effectively to
high-dimensional configuration spaces, but the resulting paths may be suboptimal or non-smooth and
therefore often require subsequent smoothing, time parameterization, and trajectory tracking.
Optimization-Based Planning. Optimization-based planners formulate low-level action generation
as a constrained optimization problem over paths, trajectories, or control sequences. They minimize
task-specific objectives while enforcing constraints related to robot kinematics, dynamics, collision
avoidance, smoothness, and task completion.
Offline optimization-based planners solve the trajectory-generation problem before execution by
optimizing the complete motion as a batch. Representative methods include CHOMP (Covariant
Hamiltonian Optimization for Motion Planning) [44], TrajOpt (Trajectory Optimization) [45], and
STOMP (Stochastic Trajectory Optimization for Motion Planning) [7]. These approaches can produce
smooth and collision-free trajectories, but they often require substantial computation and cannot
directly adapt to unexpected changes encountered during execution.
Online optimization-based planners, such as Model Predictive Control (MPC) [46, 47], repeatedly
solve a finite-horizon optimization problem using the current state as the initial condition. MPC
leverages a predictive model to estimate future states and generate executable control actions in
a receding-horizon manner. This repeated re-optimization enables adaptation to disturbances and
dynamic environments. In the taxonomy adopted here, MPC is included as a low-level action-modeling
method because its exposed output is a finite sequence of executable actions or control inputs, whereas
the downstream servo loop that realizes these commands is treated as actuation-level control.
2.2.2. Learning-Based Action Modeling
Learning-based action modeling aims to learn a policy that maps environment observations, robot
states, and optional task specifications to executable actions or action sequences. Depending on the
source of supervision and the interaction setting, representative paradigms include reinforcement
learning and imitation learning.
Sequential decision-making for learning-based action modeling is commonly formulated as a
Markov Decision Process (MDP), which provides a formal framework for modeling interactions
between a robot and its environment under uncertainty. An MDP is defined as a five-tuple:
M = ⟨S, A, P, R, 𝛾⟩,
(1)
where
• S denotes the state space containing all possible environment and robot states;
• A denotes the action space containing the executable actions available to the robot;
10


<!-- page 11 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
• P(𝑠′ | 𝑠, 𝑎) denotes the transition probability of reaching state 𝑠′ after executing action 𝑎in state
𝑠;
• R : S×A →ℝdenotes the reward function specifying the expected immediate reward obtained
by executing action 𝑎in state 𝑠;
• 𝛾∈[0, 1] denotes the discount factor that balances short-term and long-term rewards.
This formulation provides a unified basis for learning policies that map states or observations to
executable actions and underlies a wide range of robot-learning approaches, including reinforcement
learning and imitation learning.
Reinforcement Learning (RL). The objective of reinforcement learning is to learn an optimal policy
𝜋∗: S →A that maximizes the expected cumulative discounted reward, also referred to as the
return [48]:
𝜋∗= arg max
𝜋
𝔼𝜋
∞
∑︁
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡) ,
𝑎𝑡∼𝜋(· | 𝑠𝑡).
(2)
This objective provides the theoretical foundation for a broad family of algorithms, including Q-
learning [49, 50], policy-gradient methods [51, 52], and actor-critic approaches [53, 54]. According
to how interaction data are obtained, RL methods can be categorized into offline RL [55, 56], which
learns entirely from a fixed pre-collected dataset; online RL [54, 57], which continually interacts
with the environment to collect new experience; and offline-to-online RL [58, 59], which initializes
learning from offline data and subsequently improves the policy through online interaction.
Imitation Learning (IL). Imitation learning acquires action policies from expert demonstrations
and is commonly divided into Behavior Cloning (BC), Inverse Reinforcement Learning (IRL), and
Generative Adversarial Imitation Learning (GAIL).
BC formulates action modeling as supervised learning from expert state-action pairs, without
requiring an explicitly specified reward function [60, 61]. Let 𝑠𝑡denote the system state at timestep 𝑡,
which may include the robot proprioceptive state, visual observations, language instructions, and
observation histories. A policy 𝜋maps these inputs to an action or action sequence. Given an expert
demonstration dataset D𝑒, the optimization objective can be written as:
𝜋∗= arg min
𝜋𝔼(𝑠𝑡,ˆ𝑎𝑡)∼D𝑒[L (𝜋(𝑠𝑡), ˆ𝑎𝑡)] ,
(3)
where ˆ𝑎𝑡denotes the expert action label. In conventional BC, L is typically instantiated as cross-
entropy loss for discrete action spaces and as mean squared error or 𝐿1 loss for continuous action
spaces.
IRL seeks to recover a reward function that explains the expert’s behavior rather than directly
imitating expert actions. By inferring the objective underlying expert demonstrations, the learned
policy may generalize more effectively to unseen states and related tasks [62, 63]. IRL assumes that
the expert behaves approximately optimally with respect to an unknown reward function 𝑅(𝑠, 𝑎).
Given expert demonstrations D𝑒, the objective is to identify a reward function 𝑅∗under which the
expert policy 𝜋𝑒achieves a higher expected return than alternative policies:
𝑅∗= arg max
𝑅
𝔼𝜋𝑒
∞
∑︁
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡) −𝔼𝜋
∞
∑︁
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡) ,
(4)
where 𝜋denotes a policy induced by the learned reward and 𝛾∈[0, 1) is the discount factor. After
estimating 𝑅∗, a reinforcement-learning algorithm is employed to obtain a policy 𝜋∗that maximizes
the expected return under the inferred reward. This separation between reward inference and policy
11
a.
PD


<!-- page 12 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
optimization enables the model to capture objectives implicit in expert behavior rather than merely
reproducing individual demonstrated actions.
GAIL formulates imitation learning as distribution matching between the discounted state-action
occupancy measures induced by the learner and the expert, thereby avoiding explicit recovery of a
task reward. The discounted occupancy measure induced by a policy 𝜋is defined as:
𝜌𝜋(𝑠, 𝑎) = (1 −𝛾)
∞
∑︁
𝑡=0
𝛾𝑡𝑃(𝑠𝑡= 𝑠, 𝑎𝑡= 𝑎| 𝜋, P) ,
(5)
where 𝛾∈[0, 1) is the discount factor, P denotes the MDP transition kernel P(𝑠′ | 𝑠, 𝑎), and the
prefactor (1 −𝛾) normalizes the occupancy measure over the infinite horizon. A standard adversarial
objective is:
min
𝜋
max
𝐷:S×A→(0,1) 𝔼(𝑠,𝑎)∼𝜌𝐸[log 𝐷(𝑠, 𝑎)] + 𝔼(𝑠,𝑎)∼𝜌𝜋[log (1 −𝐷(𝑠, 𝑎))]
−𝜆H (𝜋),
(6)
where 𝐷is a discriminator over state-action pairs, 𝜌𝜋and 𝜌𝐸denote the learner and expert occupancy
measures, respectively, H (𝜋) = 𝔼(𝑠,𝑎)∼𝜌𝜋[−log 𝜋(𝑎| 𝑠)] is the policy entropy, and 𝜆≥0 controls
the strength of entropy regularization. At the optimal discriminator, this objective corresponds to
minimizing a divergence between 𝜌𝐸and 𝜌𝜋. In practice, the policy is updated through policy-gradient
optimization using a discriminator-induced pseudo-reward, without requiring an externally specified
task reward.
2.3. Robotics Models
Vision Models. To perceive the environment, robotic models typically incorporate vision models to
extract informative visual features. Common choices for visual encoders include models trained purely
on visual data, such as the ResNet family [64], Vision Transformers (ViT) [65], and self-supervised
models like DINO [66]. For 3D perception tasks, point cloud-based encoders such as PointNet [67]
and PointTransformer [68] are widely used. Additionally, vision-language pre-trained encoders, such
as the image encoders of CLIP [69] or SigLIP [70], are employed to obtain semantically enriched
representations that align visual observations with linguistic inputs. Some models leverage additional
visual information, including object detection results (such as bounding boxes) [71] and visual
tracking outputs [72], to improve perception and support downstream tasks more effectively.
Language Models. In recent years, especially since around 2020, language has emerged as a more
natural and human-friendly modality, leading to a growing integration of language models into
robotics. To understand human instructions, language embedding models are commonly employed
for extracting textual features, such as BERT [73] and the language encoder of CLIP. With the
leap from autoregressive models like GPT-2 [74] to GPT-3 [1], large language models (LLMs) have
demonstrated remarkable advances in text understanding and generalization. To further leverage
the powerful generalization capabilities of LLMs [2, 75], many recent robotic models adopt LLMs as
backbones, where textual inputs are processed through tokenization.
Text-conditioned Vision Models and Vision-Language Models (VLMs). Robotic models also adopt
VLMs such as LLaVA [3], PaLM-E [76], and Prism [77] as backbones, building upon their architectures
to enhance multimodal understanding and control. In addition, some works leverage text-conditioned
image editing [78] and video generation models [79] to guide action generation through visual
imagination and goal specification.
Vision-Action Models and Vision-Language-Action Models. Early approaches relied on visual
servoing for control [6] and gradually incorporated RL or IL methods that map states or images to
12
|


<!-- page 13 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
actions [80, 81], giving rise to vision–action (VA) models. Over time, VA architectures have evolved
from simple MLPs to more advanced diffusion-based frameworks [81], accompanied by diverse policy
designs. The concept of VLA models was introduced by RT-2 [12]. In the narrow sense, VLAs refer to
models that are fine-tuned from foundation VLMs using robotic trajectory data, enabling them to
take human instructions and visual observations as input and directly generate robot actions in an
end-to-end manner. In a broader sense, any model that takes both visual and language inputs and
outputs robot actions through an end-to-end pipeline can be considered a VLA model.
2.4. Evaluation
Evaluation Metrics. The most commonly used metric for evaluating robotic performance is the success
rate, which measures whether a given task is completed successfully. For long-horizon tasks [82],
this has been extended to metrics such as average success length, which captures the average number
of consecutive tasks completed within a sequence of up to 𝑛tasks. Beyond success-based measures,
efficiency metrics such as task completion time and action frequency are also employed to assess how
quickly and effectively a robot accomplishes a task. In RL settings, return is also widely used as an
overall measure of performance.
Model Selection. Evaluation strategies vary depending on the experimental setting. A common
approach is to evaluate the model every 𝑘epochs and select the checkpoint with the highest success rate.
Alternatively, for more stable comparisons, one can average the results of the top-𝑛checkpoints from
the final training phase. These strategies are frequently employed in single-task settings. In contrast,
multi-task settings often adopt a simpler approach by reporting performance at the final training
epoch or step, which enables more straightforward and consistent cross-task comparisons. Another
widely used strategy is to select the checkpoint that achieves the highest validation performance for
subsequent testing.
3. Simulators, Benchmarks and Datasets
Simulators, Benchmarks, and Datasets provide the empirical foundation for advancing robotic ma-
nipulation, enabling standardized evaluation, reproducibility, and fair comparison across methods.
They are crucial for assessing generalization, robustness, and scalability in data-driven models. This
section reviews key resources across six major areas: grasping datasets that support perception–pose
learning, single-embodiment manipulation simulators and benchmarks that focus on a specific
robotic embodiment, cross-embodiment simulators and benchmarks that evaluate generaliza-
tion across different morphologies, trajectory datasets that capture multimodal robot interaction
sequences, human video datasets and video-world-model benchmarks that provide large-scale
human interaction data and evaluate predictive visual modeling for embodied control, and embodied
QA and affordance datasets that connect perception with semantic and functional understanding.
3.1. Grasping Datasets
This subsection primarily focuses on grasp detection and generation tasks, where the goal is to predict
viable grasp configurations directly from sensory inputs. While some works explore grasping as a
downstream outcome of broader manipulation objectives, our discussion is centered on methods that
explicitly target grasp prediction rather than those that infer grasps from manipulation trajectories
or task goals. Data annotations are typically categorized into two formats: rectangle-based and
6-DoF-based. The rectangle-based format labels each grasp using a 5-dimensional grasp rectangle
representation, defined by the center position (𝑥, 𝑦), the gripper’s width and height, and the orientation
13


<!-- page 14 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Cornell
GraspNet-1Billion
Graspanything
Graspanything++
Give me the eraser.
MetaWorld1
RLbench1
CALVIN1
Robomimic1
Maniskill3
VIMA-Bench1
ARNOLD1
LIBERO1
COLOSSEUM1
SimplerEnv1
GenSim21
VLABench1
RoboEval2
SoftGym3
BEHAVIOR-1K4
HomeRobot4
BiGym5
HumanoidGen5
Robosuite
RoboCasa
Graspanything-6D
Grasping Datasets
VIKI-Bench
Cross-Embodiment Manipulation Simulators and Benchmarks
Single-Embodiment Manipulation Simulators and Benchmarks
RoboTwin2.02
Dex1B
Figure 3 | Overview of simulators and benchmarks. 1Basic Manipulation with Single Arm, 2Basic Ma-
nipulation with Bimanual Arms, 3Deformable Object Manipulation, 4Mobile Manipulation, 5Humanoid
Manipulation.
Table 1 | Summary of grasping datasets.
Dataset
Venue
Grasp Type
Scene
#Objects
Domain
Size
Visual Modality
w/ Language
Cornell [83]
ICRA 2011
rect.
single object
240
real
1035 images, 8019 grasps
RGB-D
×
Jacquard [84]
IROS 2018
rect.
single object
11k
sim
54k images, 1.1M grasps
RGB-D
×
GraspNet [85]
CVPR 2020
6-DoF
cluttered
88
real
97,280 images, ∼1.2B grasps
RGB-D
×
ACRONYM [86]
ICRA 2021
6-DoF
multi-object
8872
sim
17.7M grasps
RGB-D
×
Regrad [87]
RA-L 2022
rect. & 6-DoF
multi-object
50K
sim
1.02K images, 100M grasps
RGB-D
×
MetaGraspNet [88]
CASE 2022
6-DoF
cluttered
-
sim + real
217k (sim) + 2.3k (real) images
RGB-D
×
Dexgraspnet [89]
ICRA 2023
dexterous
single-object
5355
sim
1.32M grasps
-
×
MetaGraspNet-V2 [90]
TASE 2023
6-DoF
cluttered
-
sim + real
296k (sim) + 3.2k (real) images
RGB-D
×
Grasp-Anything [91]
ICRA 2024
rect.
multi-object
3M
syn
1M images, ∼600M grasps
RGB
✓
Grasp-Anything++ [92]
CVPR 2024
rect.
multi-object
3M
syn
1M images, 10M grasps
RGB
✓
Grasp-Anything-6D [93]
ECCV 2024
6-DoF
multi-object
3M
syn
1M images, 200M grasps
RGB-D
✓
Dex1B [94]
RSS 2025
dexterous
single object
6K
sim
1B grasps
PC
×
GraspClutter6D [95]
RA-L 2025
6-DoF
cluttered
200
real
52K images, 9.3B grasps
RGB-D
×
RealVLG-11B [96]
CVPR 2026
rect.
single to cluttered
∼800
real
165K images, 11B grasps
RGB
✓
angle relative to the horizontal axis. In contrast, the 6-DoF format directly annotates the end-effector’s
six-degree-of-freedom pose, including position (𝑥, 𝑦, 𝑧), orientation (e.g., Euler angles or quaternions),
and may also include additional information such as the approach direction and a grasp quality score.
We provide a comprehensive summary of existing grasping datasets in Table 1.
Grasping datasets have undergone significant evolution along several dimensions, each contributing
to the advancement of the field. First, annotation has shifted from manual labeling to model-based
automation, greatly reducing human effort and enabling scalable data generation. Second, the amount
of annotated data has increased from small to large-scale datasets, allowing for more robust and
data-driven learning. Third, grasp representations have evolved from simple 2D rectangles [83, 84,
87, 91, 92, 96] to full 6-DoF [85, 86, 88, 90, 93] and dexterous hand [89, 94, 97, 98] poses, enabling
a more accurate modeling of the complexity inherent in real-world grasping. Fourth, task settings
have expanded from single-object scenarios to multi-object and cluttered environments, offering more
realistic and challenging conditions. Lastly, the input modalities have progressed from purely vision-
based inputs to language-conditioned instructions, facilitating more flexible and semantically rich
manipulation. These changes collectively support the development of generalizable and intelligent
grasping systems.
14
HEAR 4 cGmmEm
I
a, FP i
+ EE


<!-- page 15 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 2 | Summary of robot manipulation simulators and benchmarks. All benchmarks provide
proprioceptive or pose observations by default, and most include additional modalities.
Name
Venue/Year
Simulator
#Objects
#Tasks
#Demos
Observation
Robot Type
Mani. Type
MetaWorld [99]
CoRL 2019
MuJoCo
80
50
-
Pose
Sawyer
Ba, Uni
Franka Kitchen [100]
CoRL 2020
MuJoCo
10
7
513
Pose
Franka Panda
Ba, Uni
RLBench [101]
RA-L 2020
CoppeliaSim
28
100
-
RGB, D, S
Franka Panda
Ba, Uni
Robomimic [102]
CoRL 2021
MuJoCo
15
8
6K
RGB, D
Franka Panda
Ba, Uni
Maniskill [103]
NeurIPS 2021
SAPIEN
100+
4
30K+
RGB, D, S
Franka Panda
Ba, Uni
CALVIN [82]
RA-L 2022
Pybullet
28
34
40M
RGB, D
Franka Panda
Ba, Uni
VLMbench [104]
NeurIPS 2022
CoppeliaSim/[101]
22
8
6K+
RGB, D, S
Franka Panda
Ba, Uni
Maniskill2 [105]
ICLR 2023
SAPIEN
2144
20
30K+
RGB, D, S
Franka Panda
Ba, Mo, Uni, Bi
VIMA-Bench [106]
ICML 2023
Pybullet/Ravens
100+
17
600K+
RGB, D, S
UR5
Ba, Uni
ARNOLD [107]
ICCV 2023
Isaac Sim
40
8
10K+
RGB, D, S
Franka Panda
Ba, Uni
LIBERO [108]
NeurIPS 2023
MuJoCo/[109]
67
130
6.5K
RGB, D
Franka Panda
Ba, Uni
COLOSSEUM [110]
RSS 2024
CoppeliaSim/[101]
-
20
2K
RGB, D
Franka Panda
Ba, Uni
SimplerEnv [111]
CoRL 2024
SAPIEN
-
10
140K+
RGB, D
Google Robot, WidowX
Ba, Uni
GenSim2 [112]
CoRL 2024
SAPIEN
200
100
-
RGB, D
Franka Panda
Ba, Uni
GemBench [113]
ICRA 2025
CoppeliaSim
20+
60
-
RGB, D
Franka Panda
Ba, Uni
RoboTwin [114]
CVPR 2025
SAPIEN/[115]
10+
-
320
RGB, D, S
Aloha-AgileX
Ba, Bi
GENMANIP [116]
CVPR 2025
Isaac Sim
10K
200
200K
RGB, D, S
Franka Panda
Ba, Uni
VLABench [117]
ICCV 2025
MuJoCo
2000+
100
5K
RGB, D
Franka Panda
Ba, Uni
AGNOSTOS [118]
NeurIPS 2025
CoppeliaSim/[101]
-
41
3.6K
RGB, D, S
Franka Panda
Ba, Uni
RoboTwin 2 [119]
2025
SAPIEN/[115]
731
50
100K
RGB, D, S
Aloha, UR5, Franka, ARX-X5
Ba, Uni, Bi
ROBOEVAL [120]
2025
-
-
8
3K+
RGB, D
Franka Panda
Ba, Bi
INT-ACT [121]
2025
SAPIEN/[111]
-
50
60K+
RGB, D
Franka Panda
Ba, Uni
RoboDojo [122]
2026
Isaac Sim
-
60
5.3K
RGB
ARX X5, Piper, Piper X
Ba, Bi
TacSL [123]
T-RO 2025
Isaac Gym
-
3
-
RGB, D, T
Franka Panda
Ba, Uni
ManiFeel [124]
2025
Isaac Gym/[123]
-
6
-
RGB, D, T
Franka Panda
Ba, Uni
[11]
RSS 2018
MuJoCo
-
4
100
RGB, D, T
ADROIT Hand
Dex, Uni
TriFinger [125]
CoRL 2021
PyBullet
-
2
-
RGB
3-DoF Hand
Dex, Uni
PlasticineLab [126]
ICLR 2021
Taichi + DiffTaichi
1
10
-
RGB, D, P
Rigid End-Effector
De
SoftGym [127]
CoRL 2021
NVIDIA FleX
4
10
-
RGB, D, P
Sawyer, Franka
De, Uni
DaXBench [128]
ICLR 2023
DaX
4
9
-
RGB, D, P
-
De
DLO-Lab [129]
ICML 2026
Genesis/Taichi
-
10
800
RGB, V
Robot Arm(s) + Parallel Gripper
De, Uni, Bi
ManipulaTHOR [130]
CVPR 2021
Unity/AI2-THOR
2.6K+
-
-
RGB, D, N
Kinova Gen3 on Mobile Base
Mo, Uni
HomeRobot [131]
CoRL 2023
AI Habitat
7892
-
-
RGB, D
Hello Robot Stretch
Mo, Uni
BEHAVIOR-1K [132]
CoRL 2023
OmniGibson
5215
1K
-
RGB, D
Mobile Manipulator
Mo, Uni
ODYSSEY [133]
AAAI 2026
Isaac Sim
100+
12
-
RGB, D, LiDAR
Unitree Go2 + ARX5
Mo, Quad, Uni
BiGym [134]
CoRL 2024
MuJoCo
10+
40
2K
RGB, D
Unitree H1
Hu, Bi
HumanoidBench [135]
RSS 2024
MuJoCo
15
27
-
RGB, LiDAR
Unitree H1 + Shadow-Hand
Hu, Bi, Dex
HumanoidGen [136]
NeurIPS 2025
SAPIEN
-
20
-
RGB, D
Unitree
Hu, Bi, Dex
SIMPLE [137]
2026
MuJoCo + Isaac Sim
1.5K+
60
6K
RGB
Unitree G1
Hu, Bi, Dex
D = depth, S = segmentation, T = tactile sensing, P = particle-based state representations, N = normals
Ba = basic, De = deformable object, Dex = dexterous, Mo = mobile, Quad = quadrupedal, Hu = humanoid manipulation
Uni = single arm, Bi = bimanual arms
3.2. Single-Embodiment Manipulation Simulators and Benchmarks
Single-embodiment manipulation benchmarks focus on a specific type of robotic platform, typically
represented by single-arm manipulators or humanoids equipped with manipulators. For consistency
in categorization, we group single-arm and dual-arm systems under the same embodiment type.
Building on the task taxonomy introduced in Section 4, we provide a comprehensive overview of
existing single-embodiment manipulation simulators and benchmarks in Table 2.
Basic Manipulation Benchmarks. These benchmarks primarily target relatively constrained tabletop
tasks performed by single- or dual-arm manipulators, including pick-and-place, sorting, pushing,
insertion, opening, closing, and pouring. Early benchmarks largely focused on learning task-specific
trajectories through reinforcement learning or imitation learning [99, 100]. More recent efforts have
progressively expanded the evaluation scope toward more demanding settings, including long-horizon
tasks that require sequential execution of multiple manipulation stages [82, 117, 138], language-
conditioned trajectory generation [104, 106, 108], generalization under visual distractions [110, 113,
139] or unseen tasks [121], and robustness to environmental or execution perturbations [140, 141].
Other benchmarks seek to establish fairer and more standardized evaluation protocols for VLA
models [111, 117], while recent platforms increasingly extend evaluation from single-arm settings to
15


<!-- page 16 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
more capable bimanual manipulation [114, 119, 142]. In parallel, growing attention has been devoted
to tactile sensing for policy learning and evaluation in contact-rich manipulation tasks [123, 124, 143].
Dexterous Manipulation Benchmarks. Dexterous manipulation benchmarks have progressed from
evaluating individual algorithms and hardware platforms toward broader assessment across tasks
and embodiments. Early work combined deep reinforcement learning with demonstrations to im-
prove high-dimensional skill acquisition [11], while TriFinger provided a reproducible hardware
testbed [125]. More recent benchmarks expand this scope: DexJoCo [144] evaluates task-oriented
dexterous manipulation under diverse settings, whereas DexVerse [145] emphasizes multi-task and
multi-embodiment generalization. Together, they support more systematic evaluation of dexterous
manipulation policies.
Deformable Object Manipulation Benchmarks. Benchmarks for deformable object manipulation
provide environments for evaluating robotic systems on non-rigid materials such as cloth, ropes, fluids,
and elastic objects [126, 127]. DaXBench [128] broadens task and object coverage through differen-
tiable physics, while DLO-Lab [129] focuses on deformable linear objects with material properties,
contact interactions, and topological complexity. RGBench [146] emphasizes physically accurate
garment simulation and systematic measurement of the sim-to-real gap, whereas MoDeSuite [147]
extends deformable-object evaluation to mobile manipulation requiring coordinated base and arm
motion. Together, these benchmarks support more systematic comparison of planning and learning
methods across physical properties, object categories, embodiments, and sim-to-real settings.
Mobile Manipulation Benchmarks. Mobile manipulation benchmarks evaluate systems that integrate
locomotion and manipulation [130–132]. Typical tasks involve coordinating a mobile base (wheeled
or legged) with an onboard manipulator to transport objects, navigate to target locations, and interact
within cluttered or spatially extended environments. These benchmarks are critical for studying
perception, planning, and control challenges faced by embodied agents operating in dynamic and
unstructured settings.
Quadrupedal Manipulation Benchmarks. Wang et al. introduced ODYSSEY [133], a benchmark and
framework for open-world quadruped robots that unifies exploration and manipulation in long-horizon
tasks. By integrating vision-language planning with whole-body control, ODYSSEY addresses key
challenges in instruction decomposition, locomotion–manipulation coordination, and generalization
across diverse open-world scenarios, with validation in both simulation and the real world.
Humanoid Manipulation Benchmarks. Humanoid manipulation benchmarks evaluate whole-body
coordination, dexterity, and stability in tasks involving upper-body manipulation and legged lo-
comotion [134–136]. Recent benchmarks further expand this scope: SIMPLE [137] provides a
scalable simulation testbed for diverse loco-manipulation tasks and policy architectures, while Hu-
manoidArena [148] emphasizes egocentric hierarchical learning and transfer across motion-tracking
controllers. Complementary frameworks such as OASIS [149] and GRAIL [150] improve scalable sim-
to-real learning through simulated teleoperation, reconstructed assets, domain randomization, and
video-generated interaction priors. Together, these efforts support more comprehensive evaluation
and data generation for generalizable humanoid loco-manipulation.
3.3. Cross-Embodiment Manipulation Simulators and Benchmarks
Cross-embodiment manipulation benchmarks support a diverse range of robotic platforms, including
single-arm, dual-arm, mobile, quadrupedal, and humanoid robots. These settings are designed to
evaluate whether a single model can consistently perform similar tasks across robots with varying
morphologies, degrees of freedom, and control constraints. Some benchmarks integrate multiple
embodiment-specific benchmarks, each with different simulator backends and without a unified
16


<!-- page 17 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 3 | Summary of cross-embodiment robotic manipulation benchmarks. S denotes segmentation,
T tactile sensing, A audio, L LiDAR, and F force/contact information.
Name
Venue/Year
Simulator
#Objects
#Tasks
#Demos
Observation
#Robots
Manip. Type
RoboSuite [109]
2020
MuJoCo
20
9 tasks
-
RGB, D
10
Ba, Mo, Hu, Quad, Uni, Bi, Dex
CortexBench [151]
NeurIPS 2023
Multiple
-
17 tasks
850+
RGB, D
6
Ba, Mo, Uni
RoboHive [152]
NeurIPS 2023
Multiple
-
17 tasks
850+
RGB, D
10+
Ba, Mo, Quad, Hu, Uni, Bi, Dex
ORBIT/Isaac Lab [154]
RA-L 2023
Isaac Sim
-
5 types
-
RGB, D, S
16
Ba, Mo, Hu, Uni, Bi, Dex
RoboCasa [155]
RSS 2024
MuJoCo/[109]
2509
100 tasks
100K+
RGB, D
4+
Ba, Mo, Hu, Quad, Uni, Bi, Dex
Genesis [156]
2024
Genesis Engine
-
-
-
RGB, D, T, A
6
Ba, Mo, Hu, Uni, Bi, Dex
ManiSkill3 [115]
RSS 2025
SAPIEN
10K+
12 types
1M frames
RGB, D, S
20+
Ba, Mo, Hu, Uni, Bi, Dex
RoboVerse [153]
RSS 2025
MetaSim
5.5K
276 tasks
500K
RGB, D
5
Ba, Mo, Hu, Uni, Bi, Dex
AgentWorld [157]
CoRL 2025
Isaac Sim
9K
-
1000+
RGB, D
4
Mo, Hu, Uni, Bi, Dex
VIKI-Bench [158]
NeurIPS 2025
[115, 155]
-
23,737 tasks
-
RGB, D
6
Ba, Mo, Hu, Uni, Bi, Dex
GS-Playground [159]
RSS 2026
GS-Playground
-
3 types
-
RGB, D, L, F
5+
Ba, Mo, Hu, Quad, Uni
Table 4 | Summary of trajectory datasets.
Dataset
Venue/Year
Domain
#Demos
#Verbs
Robot Type
Observation
MIME [160]
CoRL 2018
real
8.3k
20
Baxter Robot
RGB, D
BridgeData [161]
2021
real
7.2k
4
WidowX250
RGB, D
BC-Z [162]
CoRL 2021
real
26k
3
Google Robot
RGB
RT-1 [163]
RSS 2023
real
130k
2
Google Robot
RGB, D
RH20T [164]
RSSW 2023
real
110k
33
Flexiv, UR5, Franka
RGB, D, T
BridgeData V2 [165]
CoRL 2023
real
60.1k
24
WidowX 250
RGB, D
RoboSet [166]
ICRA 2024
real
98.5k
11
Franka Panda
RGB, D
Open X-Embodiment [167]
ICRA 2024
real
1.4M
217
22 Embodiments
RGB, D
DROID [168]
RSS 2024
real
76k
86
Franka Panda
RGB, D
AgiBot World Dataset [169]
IROS 2025
real
1M+
87
Agibot
RGB, D, T
ARIO [170]
2024
real + sim
3M
20
AgileX, UR5, Cloud Ginger XR-1
RGB, D, T, A
RoboMind [171]
RSS 2025
real
107k
38
Franka Panda, Tien Kung, AgileX, UR5
RGB, D
RoboFAC [172]
2025
sim (SAPIEN/ManiSkill)
9.44k
12
Franka Panda
RGB, D
RoboCOIN [173]
2025
real
180K+
39
15 Dual-Arm/Humanoid Embodiments
RGB, D
Humanoid Everyday [174]
ICRA 2026
real
10.3k
221
Unitree G1, H1
RGB, D, L, T
interface [151]. Others consolidate various simulator backends and provide a unified API for consistent
interaction [152, 153]. Additionally, there are benchmarks that rely on a single simulator backend,
within which different embodiments are supported through carefully designed environments [109,
115, 154–157]. We present a comprehensive overview of existing cross-embodiment simulators and
benchmarks in Table 3.
3.4. Trajectory Datasets
Trajectory datasets are structured collections of time-ordered data that capture the sequential states,
actions, and sensory observations of an agent interacting with an environment. In the context of
robotics and embodied AI, these datasets typically include robot joint states, end-effector poses, control
inputs, and multimodal observations (e.g., RGB images, depth maps, force-torque readings) collected
during the execution of specific tasks. In addition to trajectory datasets included in benchmarks, some
works focus on building dedicated datasets that vary in scale, quality, and diversity. These datasets
range from small collections to large-scale repositories with millions of samples, and from low-fidelity
teleoperated data to high-quality expert demonstrations. They also differ in embodiment types,
control modes, and data sources such as human teleoperation, scripted agents, or learned policies.
Many high-quality datasets include semantic labels, task definitions, and multimodal observations,
making them valuable for learning general manipulation policies across tasks and robot types. We
provide a comprehensive summary of existing trajectory datasets in Table 4.
17


<!-- page 18 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 5 | Summary of embodied QA and affordance datasets.
Dataset
Venue
Domain
Size
Visual Perception
Tasks
Spatial Reasoning
Tasks
Functional and
Commonsense
Reasoning Tasks
OpenEQA [175]
CVPR 2024
real
1.6K
Object, Attribute and
Object State
Recognition
Object Localization,
Spatial Reasoning
Functional Reasoning,
World Knowledge
ManipVQA [176]
IROS 2024
real + sim
84K
Physically Grounded
Understanding
Object Detection
–
ManipBench [177]
CoRL 2025
real + sim
12K+
Keypoint Selection,
Trajectory
Understanding
Fabric Manipulation,
Tool & Drawer Contact
–
RefSpatial [178]
NeurIPS 2025
real
20M
-
Object Location,
Orientation and
Topological Reasoning
–
Robo2VLM [179]
NeurIPS 2025
real
684K+
Scene Understanding,
Multiple View
Object State, Spatial
Relationship
Goal-conditioned
Reasoning, Interaction
Reasoning
PAC Bench [180]
NeurIPS 2025
real + sim
30K+
Properties
Constraints
Affordance
PointArena [181]
2025
real
982
Pointing
Pointing
–
3.5. Embodied QA and Affordance Datasets
While EQA and affordance understanding both require visual-semantic and spatial reasoning, EQA
emphasizes high-level question answering based on environmental context, whereas affordance
understanding targets low-level functional interaction with objects, such as grasping or tool use.
These datasets empower robotic models with the ability to perceive and understand the physical
world, and we categorize their capabilities into three core task types. First, Visual Perception
Tasks focus on the static recognition of visual information, enabling robots to identify what an
object is, what color or material it has, and what state it is in (e.g., open or closed). This includes
object recognition, attribute recognition, object state recognition [175], and keypoint selection to
determine actionable locations for manipulation [177]. Second, Spatial Reasoning Tasks involve
understanding object positions, spatial relationships, and reachability. They encompass 2D/3D object
detection [176], object localization [175], and reasoning about spatial relations between the robot and
its environment [178, 179], such as determining the relative direction between a gripper and a target
object. Finally, Functional and Commonsense Reasoning Tasks address the robot’s understanding of
affordances [180] and functional uses [175] of objects—for instance, recognizing that a dish wand
is used for cleaning utensils or that a knife should be grasped by its handle. These tasks bridge
perception with actionable, context-aware behavior grounded in physical interaction knowledge.
Table 5 offers detailed descriptions of representative datasets.
3.6. Human Video Datasets and Video-World-Model Benchmarks
Given the scarcity of robot trajectories, increasing attention has turned to human egocentric videos
as a scalable complementary data source that captures diverse hand-object interactions and offers
valuable priors for learning robot manipulation. Ego4D [182] established a large-scale founda-
tion for first-person activity understanding, while Ego-Exo4D [183] extended this setting with
synchronized egocentric and exocentric views and rich multimodal annotations. More manipulation-
oriented datasets have increasingly incorporated supervision that is directly relevant to robot learning.
EgoDex [184] provides large-scale dexterous manipulation videos with detailed 3D hand trajectories,
and EgoVerse [185] emphasizes diverse human demonstrations and systematic human-to-robot trans-
fer across tasks, scenes, and robot embodiments. Hoi! [186] further connects human and robotic
interaction data through cross-view visual observations, force, torque, and tactile sensing. Collectively,
18


<!-- page 19 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 6 | Comparison between non-learning and learning-based methods for grasping and manipula-
tion. Here, grasping specifically refers to grasp detection and generation.
Mani. Type
Control Type
Pose Generation
Trajectory Generation
Generalization
Interpretability
& Stability
Grasping
Non-learning
Analytical: geometric rules,
force-closure analysis
IK + motion planning
Low
High
Learning
Learned from data
IK + motion planning
High
Low
Manipulation
Non-learning
Task-specific or predefined
goal pose
IK + motion planning
Low
High
Learning
Learned implicitly via RL
or IL
Learned policies via RL or
IL
High
Low
these datasets shift human video from generic activity understanding toward scalable supervision for
manipulation, although embodiment mismatch, incomplete action labels, and uncertain recovery of
contact dynamics remain important limitations.
In parallel, recent benchmarks have begun evaluating whether video world models capture
interaction dynamics that can support robot execution, rather than assessing generated videos
solely through perceptual quality. Dream.exe [187] converts generated manipulation videos into
robot trajectories and evaluates their execution in simulation, while RoboWM-Bench [188] extends
embodiment-grounded evaluation to both human-hand and robotic manipulation videos. WoW-
World-Eval [189] further introduces an embodied Turing test that evaluates perception, planning,
prediction, generalization, and execution through complementary automatic, human-preference,
and action-execution metrics. Together, these benchmarks shift world-model evaluation from visual
realism toward physical consistency, long-horizon reasoning, and embodied executability.
4. Manipulation Tasks
Early grasping methods primarily focused on identifying stable grasp configurations through geometric
analysis, force closure conditions, or task-specific heuristics. Candidate grasp poses were analytically
generated from object geometry, contact normals, or predefined grasp templates, and then executed
using inverse kinematics (IK) and motion planning. Building on such established grasps, early
approaches to dexterous, deformable, mobile, quadrupedal, and humanoid manipulation typically
assumed a known target pose or a task-specific goal. The emphasis was on optimizing motion
trajectories or control commands to achieve these goals under physical and kinematic constraints,
rather than learning end-to-end action generation from raw sensory input as in modern RL or IL
methods. The comparison is summarized in Table 6.
Among these, basic manipulation is by far the most extensively studied, supported by a rich body
of literature that enables fine-grained categorization of methods. We therefore dedicate Sections 5
and 6 to a detailed discussion of high-level planning and low-level learning-based action modeling
in the context of basic manipulation, while for other task categories we summarize representative
methods within their respective subsections.
4.1. Grasping
In the narrow sense considered in this work, grasping specifically refers to the tasks of grasp detection
and grasp generation. These tasks involve identifying feasible grasp configurations from sensor inputs
such as images or point clouds, allowing robotic end-effectors to securely pick up objects. The primary
focus is on predicting the position and orientation of the gripper to ensure stable and reliable grasps,
19


<!-- page 20 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
(b) Multimodal Feature Fusion
(c) High-level Planner-Guided 
Modular Pipeline
(d) End-to-end Foundation Model
(a) Vision-only-based Methods
Pick up the
lemon/pan
Grasp Foundation Model
…
…
…
or
Mapping or 
Generative Model
or
Image 
Encoder
Text 
Encoder
Fusion
Decoder
or
Grasp 
Model
High-level 
Planner
Planning & Grounding
filter
or
or
Figure 4 | Comparison of different grasping methods. (a) Vision-only approaches, which map visual
inputs to grasp poses using CNNs or spatial transformers, or generate poses via VAEs or diffusion
models. With the introduction of language, three main categories emerge: (b) fusion of language
and visual features through mechanisms such as cross-attention; (c) generation of multiple grasp
candidates using pretrained grasp models, followed by selection with high-level planners (e.g., LLMs,
VLMs, or 3D representations); and (d) end-to-end fine-tuning of grasp foundation models on large-
scale grasping datasets. Figure adapted from [199].
even in the presence of diverse object shapes, varying poses, and cluttered environments.
Non-Learning-Based Grasp. Early methods generate grasp poses by explicitly analyzing object
geometry [190], performing contact-driven force analysis [191], or applying task-specific rules [192],
in combination with the gripper model. However, due to their limited generalization ability in handling
complex shapes, occlusions, and unseen objects, these approaches have gradually been replaced by
data-driven, learning-based methods, as discussed below. The taxonomy of learning-based grasping
approaches is illustrated in Figure 4.
Rectangle-based Grasp. Grasping rectangles were first introduced by Jiang et al. [83]. While they are
visually similar to bounding boxes, their representational semantics are fundamentally different. A
grasping rectangle is defined as a 5-dimensional representation, as previously described in Section 3.1.
Subsequent methods have progressively incorporated deep learning techniques, ranging from basic
convolutional neural networks (CNNs) [193–195] to more advanced architectures such as ResNet [71],
GR-ConvNet [196] and Transformer [197], and further to CLIP-based models that integrate textual
information through feature fusion methods [198]. More recently, diffusion models have also been
employed [92]. Over time, the models have evolved from simple to complex, and the modalities have
shifted from unimodal to increasingly multimodal.
6-DoF Grasp. Two-dimensional rectangle-based representations, which typically assume parallel-jaw
grippers executing top-down grasps, are limited to 2 or 3 degrees of freedom (DoF). This restricts the
gripper’s orientation and reduces applicability in unstructured or complex environments. To address
these limitations, researchers have proposed 6-DoF grasp representations [200] that define a grasp as
a 6-dimensional pose in 3D space. This formulation enables the robot to grasp objects from arbitrary
orientations, improving flexibility and robustness. The 6-DoF representation is especially beneficial in
cluttered scenes, non-planar object poses, and scenarios involving complex geometries.
20
—
KEE
Z-
=
7 oY
B=
Ba
=
|=
—
2
SEE
Co
=
&
g
© OEE
oo
Ga
=e
=
%
Zs L——1
00. 0
N
B=
=a [2
00 O-


<!-- page 21 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Apart from a few early 2D-based approaches [201], the majority of recent methods adopt 3D
representations. In particular, methods based on point cloud inputs have explored a wide range
of architectures, ranging from mapping convolutional networks [202] and transformer-based mod-
els [203], to generative autoencoders [200], variational autoencoders [204, 205], and UNet-style
frameworks [206]. To improve efficiency, various methods have been proposed, including applying in-
stance segmentation or heatmap to focus on task-relevant manipulation regions [207, 208], reducing
the grasp search space by representing grasp poses with contact points on the object surface [209],
incorporating graph neural networks for geometric reasoning on point cloud data [210], and adopting
an economic supervision paradigm that selects key annotations and leverages focal representation
to reduce training cost and improve performance [211]. Some works further address structural
distortions commonly found in real-world point cloud data by introducing completion or denoising
modules to convert the input into a clean and consistent style [212, 213]. Several methods also
address the SE(3)-equivariance problem [214, 215] by modeling grasp generation as a continuous
normalizing flow over SE(3) with equivariant vector fields, or by predicting per-point grasp quality
over the orientation sphere using spherical harmonic basis functions. Meanwhile, several methods
also leverage 3D representations such as SDF [216–218], NeRF [219, 220], and 3DGS [221–223] to
extract geometric features or to sample grasp points for downstream prediction.
Language-driven Grasp. In recent years, language-driven grasping has gained increasing attention,
aiming to achieve object-specific and instruction-guided manipulation. Existing approaches can be
broadly categorized into three groups. The first adopts multimodal feature fusion [224, 225], where
textual and visual modalities are jointly encoded, often via cross-attention mechanisms. The second
leverages existing grasp models to generate large numbers of grasp candidates, followed by ranking or
scoring with LLMs or VLMs to select the most confident grasps. For instance, LLMs can generate task-
specific descriptions [226], while VLMs are used for visual grounding to compute grasp confidence
scores [227, 228]. Representative methods include VL-Grasp, which employs VLMs to attend to
the target object and generate grasps [229]; OWG, which leverages VLM-based semantic priors for
planning under occlusion [230]; and Reasoning-Grasping, which integrates visual-linguistic inference
for improved object-level understanding [231]. Other efforts adapt MLLMs for environment-aware
error correction [232], or learn object-centric attributes to enable rapid grasp adaptation across
tasks [233]. Affordance-driven approaches also ground grasp generation in language and vision
cues [234–236]. The third line of work directly fine-tunes MLLMs on grasp foundation models with
large-scale grasp datasets [199, 237].
Challenges. Firstly, the aforementioned grasp detection and generation methods were originally de-
signed for 2-DoF parallel-jaw grippers. However, with the increasing use of dexterous hands, research
has shifted toward dexterous grasping, which requires complex annotations such as hand joint angles
and contact force maps. To handle the high dimensionality of this task, various generative approaches,
including diffusion-based models, have been proposed [238–240]. Some approaches represent grasp
configurations via contact points or maps [241], or leverage interaction-based representations such
as D(R, O) [242] to infer grasps from geometric relationships. Second, traditional grasping strategies
typically rely on a single end-effector, such as suction or parallel grippers, which limits adaptability
to diverse object geometries. To address this, several works have explored bimanual grasping using
dual-arm or dual-gripper configurations [243, 244]. Lastly, grasping transparent objects remains a
significant challenge, as depth sensors often fail to detect or localize such materials accurately. Recent
efforts address this limitation by incorporating alternative modalities, such as LiDAR [245] or 3D
reconstruction [246–248], to infer the geometry of transparent or reflective objects.
21


<!-- page 22 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 7 | Representative methods across manipulation types and learning paradigms.
Mani. Type
RL
IL
RL+IL
VLA
Basic
See Table 8
See Figure 15
See Table 9
See Figure 17
Dexterous
PDDM [249],
[11], [250]
DexHandDiff [251],
CordViP [252]
REBOOT [253],
ViViDex [254]
OFA [255], LBM [256]
Soft Robotics
[257], [258]
Soft DAgger [259],
KineSoft [260]
SS-ILKC [261]
–
Deformable Object
[262]
DeformerNet [263],
DexDeform [264]
DMfD [265]
𝜒0 [266]
Mobile
[267],
MoMa [268]
MOMA-Force [269], Skill
Transformer [270]
[271]
MoManipVLA [272]
Quadrupedal
VBC [273],
GAMMA [274]
Human2LocoMan [275]
[276], WildLMa [277]
QUAR-VLA [278],
GeRM [279]
Humanoid
[280],
FLAM [281]
OmniH2O [282], iDP3 [283]
[284]
GR00T N1 [285],
Humanoid-VLA [286]
4.2. Basic Manipulation
Basic manipulation refers to relatively simple tabletop tasks performed by single- or dual-arm ma-
nipulators, such as pick-and-place, sorting, pushing, inserting, opening, closing, and pouring. Most
current research remains focused on this category, as illustrated in Figure 12 and further discussed in
Sections 5–6, where the majority of methods and benchmarks are developed around object-centric
interactions in structured environments. While these sections classify approaches within the scope of
basic manipulation, the proposed taxonomy is general in nature and can be readily extended to other
categories of manipulation tasks.
4.3. Dexterous Manipulation
Dexterous manipulation refers to the capability of robotic systems equipped with multi-fingered or
anthropomorphic hands to achieve precise and coordinated object control through complex contact
interactions. It involves in-hand reorientation, fine force modulation, and multi-point contact, enabling
actions such as twisting, grasping, and rotating, as illustrated in Figure 5. This capability is critical for
tasks requiring high precision and adaptability, such as tool use, assembly, and manipulation of small
or irregular objects. Human hand models typically include 20–25 DoF, with each finger modeled by 4
DoF, the thumb by 4–5 DoF, and additional DoF from the palm and wrist for enhanced realism [287].
Rotate
Spin & Roll
Pour
Open
Grasp
Insert
Figure 5 | Tasks in dexterous manipulation, fig-
ure adapted from [249, 250, 288–290].
Non-Learning-Based Methods. Early work on
dexterous manipulation predominantly employed
non-learning approaches, including optimization-
and control-based techniques such as heuristic
search and constrained optimization [291]. These
methods typically assume access to known dy-
namics and object models, and focus on trajectory
planning under physical constraints.
Learning-Based Methods. With the advent of
RL, both model-based and model-free paradigms
have been applied to dexterous manipulation.
Model-based methods such as PDDM [249] ex-
ploit learned dynamics for efficient planning and
control, while model-free approaches directly op-
timize policies through interaction [11], sometimes combined with few-shot imitation to accelerate
adaptation to real hands [250]. More recently, human-in-the-loop frameworks such as HIL-SERL [292]
22
Lar
i
Pe
yw
=
Se
~@ TR
[@
1g:
-
NX
gq"
Be
L
~
ke
u
NG


<!-- page 23 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
integrate demonstrations, online corrections, and reinforcement learning for sample-efficient acquisi-
tion of precise skills on physical robots. DexScrew [293] further addresses imperfect simulation by
first learning transferable finger-motion primitives with RL in simplified environments, then using
these primitives to collect real multisensory demonstrations for tactile-conditioned behavior cloning.
IL has gained attention for its data efficiency, exemplified by DexMV [294], which employs
kinematic retargeting from human videos to robot hands. Extensions incorporate auxiliary supervision
such as contact prediction [251, 252] and inverse dynamics modeling [295], improving generalization
and action consistency. SAT [296] instead represents an action chunk as a variable-length sequence
of joint-wise trajectories and incorporates joint-level functional and kinematic priors, enabling 3D
dexterous policy learning across heterogeneous hand embodiments. Hybrid IL–RL approaches combine
these strengths, typically using IL for policy initialization followed by RL refinement [297, 298].
DexMV [294] instead translates human videos into robot demonstrations for imitation learning,
whereas ViViDex [254] first performs RL in a privileged state space and subsequently distills the
resulting policy through IL.
Recent VLA models expand task and embodiment generalization. DexGraspVLA [299] integrates
semantic reasoning with diffusion-based policies for grasping in cluttered scenes, while OFA [255],
LBM [256], and Being-H0 [300] leverage multimodal prompts or human videos to generate dexterous
motions and follow language instructions. UniDex [301] transforms egocentric human videos into
robot-centric trajectories and introduces a function-aligned action space to support unified control
across heterogeneous dexterous hands. Dexora [302] extends VLA modeling to high-dimensional dual-
arm and dual-hand manipulation, combining embodiment-matched simulated and real demonstrations
with quality-aware training to reduce the influence of noisy teleoperation data.
Human guidance provides another supervision source: Chen et al. [303] use object and wrist
trajectories from videos to guide RL, and Mandi et al. [304] introduce functional retargeting to
transition from demonstrations to autonomous control. Affordance reasoning further supports grasp-
specific strategies [305, 306], guiding object selection under semantic constraints. Finally, recent
works emphasize robustness and autonomy. Task decomposition reduces complexity by structuring
subtasks [307], while recovery mechanisms such as REBOOT [253] introduce IL-trained reset policies
to handle failures in long-horizon settings.
Challenges. Beyond high-dimensional control and contact dynamics, dexterous manipulation faces
broader challenges. First, many real-world tasks are long-horizon and compositional, requiring
sequential execution of fine-grained skills. Chen et al. [289] address this by decomposing tasks into
discrete skills trained with RL and linking them via a high-level policy. Second, sim-to-real transfer
remains a bottleneck due to discrepancies in perception, dynamics, and actuation. CyberDemo [290]
mitigates this through data augmentation, improving robustness under domain shift. Third, accurate
perception is difficult in cluttered or partially observed scenes, where occlusion hampers object
tracking. DexPoint [288] leverages point cloud completion to recover missing geometry and enhance
spatial awareness.
4.4. Soft Robotic Manipulation
Soft manipulators, built with compliant materials or structures, are well-suited for human–robot
collaboration, operation in uncertain environments, and safe, adaptive grasping, as illustrated in
Figure 6. They overcome the limitations of rigid manipulators when handling delicate or deformable
objects [308]. To this end, a wide range of designs have been developed to support diverse applica-
tions [34, 35, 309–311].
Non-Learning-Based Methods. For soft manipulator control, analytical kinematic models based on
23


<!-- page 24 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
the constant-curvature assumption map shape parameters to end-effector poses via virtual rigid-link
chains and Denavit–Hartenberg transformations [312]. Similarly, three-dimensional continuum
manipulators can be approximated as rigid-jointed robots, with computed-torque control achieving
closed-loop dynamics [313]. Other approaches employ model predictive control with Koopman
operators [314, 315], or rely on accurate Lagrangian models combined with adaptive dynamic sliding
mode control to enhance robustness [316]. Hybrid schemes also integrate learning into non-learning
frameworks: forward dynamics can be approximated with machine learning and combined with
trajectory optimization for open-loop control [317], while feedback-driven strategies exploit learned
models to stabilize and restore system states [310].
Pick & Insert
Unscrew
Move
Grasp
Flick Lid
Grasp Fabric
Figure 6 | Tasks in soft robotic manipulation,
figure adapted from [35, 260, 318].
Learning-based Methods. RL and IL have
been widely applied to soft manipulator control.
Model-free RL avoids explicit physical modeling by
training policies in simulation for closed-loop end-
point control [318]. Forward dynamics learned
with recurrent networks can be integrated into
trajectory optimization to generate samples and
train predictive controllers [257], while LSTM-
based dynamics models enable feedback policy
learning [319]. Domain randomization combined
with incremental offline training has improved
task-space accuracy and adaptability [258], and
wavelet-based dynamics approximations paired
with LSTM and TD3 controllers further enhance
generalization under variability [320]. IL approaches include Soft DAgger [259], which employs
dynamic behavior mapping for online expert-like action generation, and KineSoft [260], which inte-
grates kinesthetic teaching with diffusion-based policy learning. Hybrid methods also emerge, such as
SS-ILKC [261], which combines multi-objective RL with adversarial IL to learn goal-directed control
strategies in sensor space, supported by sim-to-real pre-calibration for zero-shot transfer.
Challenges. Soft-hand-based manipulation faces several challenges, including modeling highly
nonlinear and underactuated dynamics, achieving precise force and pose control with deformable or
fragile objects, ensuring robustness under environmental uncertainty and sensor noise, and lowering
the cost and complexity of data collection and teleoperation for policy training. To improve sample
efficiency, Soft DAgger [259] enables online imitation learning from limited demonstrations through
dynamic behavior mapping. To reduce hardware complexity in teleoperation, Liu et al. [311] propose
a flexible bimodal sensory interface that combines vision-based perception with wearable sensors,
enabling intuitive and low-cost control without bulky equipment.
4.5. Deformable Object Manipulation
Deformable object manipulation (DOM) requires robots to perceive and control non-rigid objects
whose shapes vary under applied forces. Unlike rigid-body manipulation, it demands reasoning
over high-dimensional, continuous state spaces, coping with uncertain deformation dynamics, and
interpreting subtle visual or tactile cues. As illustrated in Figure 7, tasks such as cloth folding, rope
and cable tying, and food handling involve diverse deformations—including tension, compression,
and bending—making DOM a complex yet crucial challenge in robotic manipulation [16, 321, 322].
Non-Learning-Based Methods. Traditional approaches to DOM, such as path planning [323]
and model-based control [324], often rely on simplified physical models or analytical solutions.
However, these methods typically struggle with generalization and real-time adaptability in complex
24


<!-- page 25 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
environments, leading to a shift toward data-driven techniques such as RL, IL, and hybrid learning-
control frameworks.
Shape the Plasticine
Open the Bag
Folding Clothes
Untie the 
Knotted Cable
Figure 7 | Tasks in deformable object manipula-
tion, figure adapted from [325–328].
Learning-based Methods. Jan et al. [262] pro-
pose a deep RL method based on a modified DDPG
algorithm that learns from visual and robot state
inputs and achieves zero-shot sim-to-real transfer
via domain randomization. In contrast, IL meth-
ods exploit demonstrations: DexDeform [264] ex-
tracts latent skills from human demonstrations
and fine-tunes them with limited robot data, De-
fGoalNet [329] predicts goal configurations from
few-shot demonstrations conditioned on state and
context, and MPD [330] generates movement
primitives with diffusion models. To combine both
paradigms, DMfD [265] incorporates expert data
into RL through advantage-weighted BC loss, expert-initialized replay buffers, and reset-to-state
initialization, achieving efficient policy optimization.
Beyond learning paradigms, DOM has explored diverse strategies spanning geometric modeling,
affordance prediction, and structure-aware perception. DeformGS [331] represents deformable objects
with canonical Gaussians and learns a time-conditioned deformation field for temporally consistent 3D
pose tracking. Affordance-based approaches include DeformerNet [263], which predicts end-effector
displacements from partial point clouds, Foresightful Affordance [332], which integrates dense per-
pixel affordances with long-horizon value estimation, and APS-Net [328], which ranks standardized
folding and flattening trajectories guided by affordance heatmaps. Language-conditioned affordance
prediction has also been explored [333]. Finally, estimating object-specific physical properties has
emerged as a complementary direction [334, 335]. GenDOM [335] learns a parameter-conditioned
policy and leverages a single human demonstration with differentiable simulation to infer unseen
object properties, enabling generalization to novel deformable instances.
Challenges. Deformable objects lack a fixed pose, and key deformation regions are often occluded
during manipulation. To improve visibility and perception, recent work jointly optimizes camera and
manipulator motion, guided by structure-of-interest cues [327]. Deformation dynamics also exhibit
delayed responses, complicating real-time control; this is addressed by encoding states into latent
spaces and predicting their dynamics. For example, DeformNet [336] encodes object geometry with
PointNet and a conditional NeRF, and models temporal evolution with a recurrent state-space model
for latent-level MPC. An even greater challenge is modeling topological changes. DoughNet [337]
extends latent-space modeling to jointly capture geometric and topological variations from point
clouds, enabling long-horizon planning with CEM for tool selection and manipulation.
4.6. Mobile Manipulation
Mobile manipulation is a robotic paradigm that combines navigation and manipulation capabilities
within a single system. It allows robots to physically interact with objects beyond a fixed workspace
by actively navigating the environment. This integration poses significant challenges in perception,
planning, and control, as it requires coordinating whole-body motion, handling long-horizon tasks, and
dealing with dynamic, partially observable scenes. Several studies have focused on designing robots
specifically for mobile manipulation [37, 338, 339]. As illustrated in Figure 8, mobile manipulation is
critical for real-world applications such as household assistance, warehouse automation, and service
robotics [17].
25
“= oe
q Bn
us
h


<!-- page 26 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Non-Learning-Based Methods. Traditionally, mobile manipulation is decomposed into two separate
problems: navigation and manipulation. Navigation is typically handled by classic path planners, such
as grid-based methods (e.g., Dijkstra) and sampling-based planners (e.g., RRT). Manipulation is often
addressed using grasp models, motion primitives, or trajectory planning based on point clouds. Some
control methods perform joint optimization of navigation and manipulation. For example, Berenson
et al. [340] optimize full-body configurations and grasp poses simultaneously, then plan motions via
sampling. Chitta et al. [341] coordinate base-arm planning with ROS-based navigation and point
cloud grasping. Others embed manipulation goals directly into MPC cost functions [342].
Load Laundry
Open Fridge
Cook Shrimp
Wipe Countertop
Take out Trash
Clean the room
Push Chairs
Open Cabinet 
Drawer
Rotate Tap
Open washer
Figure 8 | Tasks in mobile manipulation, figure
adapted from [37, 269, 343, 344].
Learning-based Methods. These methods have
emerged to learn policies for whole-body control.
For RL, Wang et al. [345] use RGB-D inputs to
estimate object pose and train a policy that jointly
predicts base velocity, arm trajectories, and grip-
per actions. HarmonicMM [346] extends this by
integrating visual and pose information into a
unified RL framework, while Wu et al. [267] pro-
pose spatial Q-value learning at the map level for
navigation guidance. To improve reward signals,
Honerkamp et al. [347] design dense rewards
based on end-effector reachability, and Causal
MoMa [268] introduces causality-aware model-
ing of control–reward relations to stabilize policy
optimization. For IL, MOMA-Force [269] learns
motion and force policies from visual-force demonstrations, while HoMeR [344] decomposes tasks
into global keypose prediction and local refinement to map end-effector targets to whole-body actions.
Wang et al. [348] leverage SAM2-based perception for object-centric IL, and Skill Transformer [270]
treats manipulation as a skill prediction problem, learning both skill categories and corresponding
low-level actions. Hybrid methods combine IL with RL to enhance generalization. For example, Xiong
et al. [271] initialize policies via behavior cloning and refine them through online RL to handle unseen
articulated objects.
Beyond learning paradigms, recent work integrates high-level reasoning and multimodal rep-
resentations. VLA-based methods such as MoManipVLA [272] process multimodal instructions to
predict end-effector waypoints while delegating base motion to a trajectory optimizer. LLM-driven
frameworks, including MoMa-LLM [349] and SayPlan [350], combine open-vocabulary language,
scene graphs, and reasoning for object search and high-level task planning. Complementary efforts in
3D scene modeling guide manipulation through active perception: ActPerMoMa [351] optimizes view-
point selection and grasp reachability via incremental TSDF mapping, while TaMMa [352] employs
sparse Gaussian localization and depth completion to generate accurate target poses.
Challenges. In addition to perception–action coordination, dynamic obstacles, and long-horizon
decision-making, mobile manipulation faces several additional challenges. A first challenge is enabling
effective human–robot collaboration. Ciocarlie et al. [353] developed an assistive system that combines
user interfaces, shared control, and autonomy to transform a PR2 robot into an in-home assistant.
Extending this line of work, Robi Butler [354] introduces a closed-loop household control framework
that supports multimodal interaction, where high-level planners such as LLMs and VLMs enable
natural language and gesture-based commands for intuitive and remote collaboration. A second
challenge is real-time manipulation during navigation, where robots must coordinate mobility and
manipulation under environmental constraints. Whole-body motion control frameworks [355, 356]
address this problem by enabling reactive planning and execution for on-the-move manipulation.
26
rm
P
Lil
mi [=
==
S T@UCN
S
=~
~)
=
A
y
E>
*~
pp
UT]
Na———
BL
.
ue
b
fo
28
|
—
—
=


<!-- page 27 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
4.7. Quadrupedal Manipulation
Quadrupedal manipulation is an emerging paradigm that combines the agile mobility of quadruped
robots with the ability to physically interact with objects. Unlike traditional manipulators or mobile
bases, quadrupeds can traverse complex and unstructured terrains while maintaining dynamic stability,
making them particularly suitable for applications such as search and rescue, field robotics, and
autonomous exploration. Representative tasks are illustrated in Figure 9. Manipulation can be
realized through several embodiments: whole-body loco-manipulation [278, 279, 357–360]; leg-as-
manipulator designs that repurpose one or more legs for interaction [276, 361, 362]; back-mounted
arms [273, 274, 363–374]; and grippers integrated into front legs for simultaneous locomotion and
manipulation [375]. Each embodiment introduces unique challenges in whole-body coordination,
dynamic control, and perception-driven planning.
Pick & Place
Write
Press Button
Press Switch
Push
Wave Ribbon
Figure 9 | Tasks in quadrupedal manipulation,
figure adapted from [133, 362, 370, 371, 374].
Non-Learning-Based Methods.
Recent ad-
vances in quadrupedal manipulation have ex-
plored diverse control strategies, ranging from
model-based optimization to learning-based ap-
proaches. Optimization-based methods provide
interpretable and physically grounded control
with strong task generalization.
For example,
Arcari et al. [365] combine MPC with Bayesian
multi-task error learning for real-time dynamics
adaptation. Wolfslag et al. [363] incorporate SUF
stability metrics and contact constraints into a
quadratic programming framework for robust,
support-leg-aware planning, a concept further extended by RoLoMa [366] to improve trajectory robust-
ness. LocoMan [375] demonstrates a hardware–control co-design approach, equipping quadrupeds
with lightweight front-leg manipulators and employing unified WBC to achieve agile locomotion and
precise manipulation.
Learning-based Methods. In the realm of RL, recent research has focused on developing structured
and informative control representations. Jeon et al. [357] introduce a hierarchical RL framework that
encodes interaction experience, robot morphology, and action history into latent representations to
facilitate effective policy learning. Fu et al. [364] decouple leg and arm rewards in the policy-gradient
formulation to enhance coordination between locomotion and manipulation, while Zhi et al. [373]
present a unified force-position controller that estimates forces from perception instead of sensors. Hou
et al. [374] incorporate explicit arm kinematics and feasibility-based rewards to promote physically
plausible behaviors. Two-stage training schemes have also been explored: RoboDuet [372] sequen-
tially trains locomotion and arm policies with reward adaptation for coordination. GAMMA [274]
improves grasp precision by conditioning policies on grasp poses, while Wang et al. [371] propose
GORM, a metric for grasp reachability under varying base poses, to guide base movement for effective
grasping. Teacher-student frameworks further advance base-arm coordination, as in VBC [273] and
Jiang et al. [370], where visual or pose-tracking guidance is distilled into student policies. SLIM [376]
extends this paradigm to long-horizon pick-and-place by progressively expanding a privileged teacher
across task stages and distilling it into an egocentric visuomotor policy through RL. Other works
combine hierarchical and hybrid designs, such as HiLMa-Res [358], which uses high-level RL to
control Bézier parameters and base motion while relying on hybrid CPG-Bézier controllers for leg
movements, and Pedipulate [362], which demonstrates end-to-end RL for single-foot manipulation.
HeLoM [377] further develops hierarchical whole-body RL for hexapod robots, using a high-level
planner to specify pushing commands and foreleg targets and a low-level controller to coordinate
locomotion, balance, and forceful object interaction.
27
3 7 ?
a)
pO
Lo
“se!
|
as)
—
~~
ad
175
Ss
=
wo
al
=
A
/
| i
Cs
v
dy


<!-- page 28 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
In the IL domain, Human2LocoMan [275] enables cross-embodiment transfer from XR-driven
human demonstrations using a modular Transformer policy, effectively transferring human manipula-
tion skills to quadrupeds. Hybrid IL–RL frameworks further improve efficiency and generalization.
He et al. [276] employ BC to train a high-level planner for grasp trajectories, while a low-level RL
controller coordinates locomotion and single-leg manipulation. WildLMa [277] builds an IL-based
skill library from VR demonstrations and sequences these skills under LLM guidance.
VLA-based frameworks have also emerged for high-level semantic reasoning. QUAR-VLA [278]
pioneers the application of VLA models to quadrupeds, while GeRM [279] and MoRE [360] inte-
grate mixture-of-experts architectures with offline RL to learn generalist visuomotor policies and
Q-functions with enhanced generalization and decision quality. QUART-Online [378] advances this
line by introducing action-chunk discretization and semantic alignment training, enabling latency-free
inference for quadrupedal VLA tasks.
Finally, advances in 3D semantic perception and high-level planning extend quadrupedal capabil-
ities. GeFF [368] performs real-time NeRF-based reconstruction with semantic relevance fields to
guide locomotion, while manipulation is executed via learned grasp models. At the task level, LLMs
have been combined with policy libraries: Ouyang et al. [359] propose a hierarchical framework
where LLMs parse long-horizon, multi-skill instructions into structured subgoals executed by RL-based
skills, bridging symbolic reasoning and continuous control.
Challenges. In addition to common challenges such as balance–manipulation coupling, terrain
adaptability, and perception delays, real-world deployment remains difficult due to the sim-to-real gap
caused by modeling inaccuracies and sensor noise. To mitigate this, fully autonomous RL pipelines
have been developed. Mendonca et al. [369] propose a framework that integrates on-policy data
collection with continuous training, while ASC [367] addresses long-horizon tasks by decomposing
them into modular skills trained via RL, coordinating them through a skill-switching policy jointly
trained with IL and RL, and introducing a corrective policy to improve robustness during deployment.
Long-horizon task execution itself poses another significant challenge. Cheng et al. [361] propose a
stage-wise RL framework that independently learns locomotion and single-leg manipulation skills,
which are later composed via a behavior tree to accomplish temporally extended tasks.
4.8. Humanoid Manipulation
(a) Manipulation
(b) Navi-Manipulation
Pick
Pick & Place
Play Piano
Water Plants
(c) Loco-Manipulation
Box Loco-
Manipulation
Play Ping Pong
Squat & Pick
 & Place
Figure
10
|
Tasks in humanoid manipu-
lation, categorized into manipulation [280,
283, 379], navi-manipulation [380], and loco-
manipulation [379, 381, 382].
Humanoid manipulation involves robotic plat-
forms with human-like morphology, typically com-
prising a torso, two arms, and either simplified
2-DoF grippers or fully dexterous hands, with loco-
motion provided by a mobile base or bipedal legs.
Designed for object interaction in human-centered
environments, these systems aim to replicate or
extend human manipulation capabilities through
tasks such as grasping, lifting, tool use, and co-
ordinated bimanual operation, as illustrated in
Figure 10. Although humanoid morphology of-
fers natural compatibility with tools, workspaces,
and infrastructures designed for humans, it also
introduces substantial challenges in balance main-
tenance, whole-body coordination, and fine motor
control, making humanoid manipulation a central
topic in robotics and embodied intelligence.
28
4
x5
aw.g
Sz a
BENS
£
>
iT
Peat
®
i
4
-—
Th Ea
oN
nr
»
Wola
Pu
C
we [20 g
u
®-
o
A
\\\
oe
TEs
&
v lB
Cav
(= LOIN YoriRR
4 nd |
3 us
i
\
)
-4
»
hE —
=
:


<!-- page 29 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Non-Learning-Based Methods. Early humanoid
control primarily relied on traditional approaches such as rule-based and analytical controllers [383,
384]. Some works also explored the integration of learning-based models into control frameworks.
For example, OKAMI [385] leverages 3D human pose estimation from a single human video to infer
joint positions and derive executable actions for humanoid robots via inverse kinematics.
Learning-Based Methods. Recent humanoid manipulation research has shifted from hand-engineered
control stacks toward learning-based systems spanning RL, IL, hybrid RL–IL, VLA, and world-action-
model paradigms [18]. In RL, FLAM [281] uses a pretrained human-motion model to score pose
stability as an auxiliary reward, while Xie et al. [280] combine diffusion-based motion generation
with RL for whole-body manipulation. OmniRetarget [386] further preserves robot–object and
robot–environment interactions when retargeting human demonstrations into kinematic references
for RL. In IL, TRILL [387] maps RGB observations to pose commands, OmniH2O [282] unifies
goals from language, vision, motion capture, and VR, and iDP3 [283] adapts diffusion policies to
egocentric whole-body control. Other methods leverage large-scale egocentric demonstrations [381],
tactile feedback [388], or data augmentation from a single demonstration [389]. MimicDroid [390]
meta-trains an in-context policy from human play videos for few-shot adaptation. Hybrid RL–IL
methods combine efficient supervision with feasible execution, as in André et al. [284], who train a
mid-level trajectory generator with IL and a low-level whole-body tracker with RL.
VLA methods jointly ground language and visual observations in coordinated locomotion and
manipulation. HumanVLA [391] separately encodes images and language, while GR00T N1 [285]
fuses visual and tokenized language features through a VLM and predicts actions with a diffusion
head. Humanoid-VLA [286] aligns language and action representations via cross-attention. Traj-
Booster [382] uses dual-arm end-effector trajectories to transfer wheeled-humanoid demonstrations to
bipedal whole-body control. WholeBodyVLA [392] learns latent representations from action-free ego-
centric videos and decodes them into arm and locomotion commands. Ψ0 [393] adopts staged training
with egocentric videos and humanoid trajectories, while HEX [394] leverages humanoid-aligned
states and expert-routed proprioceptive prediction for cross-embodiment learning. OpenHLM [395]
further studies teleoperation interfaces, action-space design, and heterogeneous co-training for
whole-body-native VLAs. Beyond conventional VLAs, MotionWAM [396] incorporates intermediate
denoising features from a video world model and predicts unified whole-body motion tokens spanning
locomotion, torso motion, height regulation, foot interaction, and hand manipulation. This direction
seeks to combine visual dynamics priors with real-time whole-body action generation.
Challenges. In addition to challenges such as multimodal perception, balance–manipulation coupling,
and high degrees of freedom, humanoid manipulation also struggles with enabling multi-agent
collaboration. For instance, CooHOI [397] exploits object dynamics as an implicit communication
channel to achieve coordinated manipulation across multiple agents. To further address the sim-to-real
gap, Lin et al. [398] introduce a generalizable reward formulation and a decoupled RL architecture,
which improve sample efficiency through staged training.
4.9. Aerial Manipulation
Aerial manipulation combines the mobility of unmanned aerial vehicles with robotic end-effectors,
such as grippers or articulated arms, to enable physical interaction beyond the reach of ground-based
platforms. Representative tasks include aerial grasping, object transportation, pick-and-place, tool
use, surface interaction, and infrastructure maintenance. Unlike fixed-base manipulation, aerial
manipulation must coordinate flight and manipulation while maintaining stability under arm motion,
contact forces, and payload changes. Its floating-base dynamics, limited onboard sensing and
computation, and strict payload constraints therefore create distinctive challenges for perception,
29


<!-- page 30 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
planning, and action modeling.
Pick and Place
Writing
Pick
Figure 11 | Tasks in aerial manipulation, figure
adapted from [399–401].
Non-Learning-Based Methods. Early aerial ma-
nipulation systems primarily relied on analytical
modeling, motion planning, and model-based con-
trol. Pounds et al. [402] studied hovering capture
and load stability during aerial grasping, while
Kim et al. [403] modeled a quadrotor and a 2-DoF
arm as a coupled system and designed an adap-
tive sliding-mode controller for autonomous object
transportation. Orsag et al. [404] further orga-
nized aerial manipulation according to momen-
tary, loose, and strong environmental coupling,
demonstrating tasks such as pick-and-place, inser-
tion, and valve operation. More recent systems extend these foundations toward greater workspace
and robustness. Lee et al. [405] combine geometric robust control with optimization-based whole-
body planning, allowing an omnidirectional aerial manipulator to operate at arbitrary poses in SE(3).
FlyAware [406] instead addresses payload-dependent dynamics through vision-based pre-grasp inertia
estimation and post-grasp adaptive control.
Learning-Based Methods. Learning-based aerial manipulation has gradually expanded from task-
specific RL and demonstration-based learning toward general-purpose VLA systems. In RL, Dimmig
and Kobilarov [407] jointly learn a world model and interaction policy for non-prehensile aerial
manipulation under unknown object dynamics. Swooper [408] adopts a two-stage deep RL strategy
that first learns flight control and subsequently coordinates high-speed flight with active gripper
control using a unified lightweight policy. Demonstration-based approaches reduce the cost and risk
of direct interaction during policy acquisition. Zito and Ferrante [409] learn transferable contact
distributions from a single demonstration to identify attachment points on unseen payloads. Flying
Hand [401] introduces an end-effector-centric interface that combines whole-body model predictive
control with intuitive teleoperation, enabling imitation policies to learn diverse tasks including writing,
insertion, pick-and-place, and tool interaction.
VLA models seek to unify semantic understanding, long-horizon reasoning, flight, and manip-
ulation. AIR-VLA [400] establishes an aerial-manipulation benchmark and multimodal dataset
covering spatial understanding, base motion, manipulator control, and multi-stage task execution.
AirVLA [399] investigates the transfer of a manipulation-pretrained 𝜋0 model to aerial pick-and-place,
using synthetic navigation data and payload-aware guidance to address data scarcity and the mis-
match between fixed-base and aerial dynamics. AIR-VLA+ [410] separates UAV movement from arm
manipulation through cascaded action decoders and an asymmetric mixture-of-experts architecture,
reducing interference between coarse platform motion and precise end-effector control.
Challenges. Aerial manipulation remains constrained by strong coupling between flight and arm mo-
tion, time-varying payload dynamics, limited sensing and onboard computation, and the destabilizing
effects of physical contact. Learning-based methods additionally face scarce demonstrations, costly and
potentially unsafe exploration, and substantial sim-to-real discrepancies in aerodynamics and contact
behavior. For VLA systems, a central challenge is coordinating semantically driven platform movement
with precise manipulation despite their different action scales and dynamics. Future progress will re-
quire safer data collection, more accurate payload and contact estimation, embodiment-aware action
representations, and tighter integration of high-level reasoning with real-time stability guarantees.
30
|.


<!-- page 31 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
4.10. Underwater Manipulation
Underwater manipulation involves robotic platforms equipped with one or more arms or grippers
to physically interact with submerged objects, structures, and environments. Representative tasks
include object retrieval, valve operation, sampling, inspection, maintenance, and archaeological
intervention. Compared with terrestrial manipulation, underwater systems must account for coupled
vehicle–manipulator dynamics, buoyancy, hydrodynamic drag, external currents, degraded visibility,
and limited communication bandwidth. These factors complicate perception, contact regulation, and
coordinated motion while placing stringent requirements on operational reliability and safety.
Non-Learning-Based Methods. Traditional underwater manipulation primarily relies on model-
based control, task-priority optimization, and human teleoperation. The TRIDENT framework [411]
coordinates a floating vehicle and redundant manipulator through an extended task-priority controller,
enabling dexterous grasping while satisfying operational constraints such as joint limits and target
visibility. Ocean One [412, 413] combines a whole-body controller for manipulation, posture, and
constraint regulation with visual and haptic interfaces, allowing a human operator to supervise
deep-sea dexterous manipulation without directly controlling every joint. DexROV [414] addresses
long-distance underwater teleoperation under communication latency through predictive simulation,
force-feedback interfaces, and shared autonomy. More recently, MR-UBi [415] integrates bilateral
control with a mixed-reality reaction-torque indicator, providing visual and haptic feedback to improve
contact-force regulation during underwater grasping and pick-and-place operations.
Learning-Based Methods. Learning-based underwater manipulation remains less explored than
its terrestrial counterpart, but recent work has begun to address model uncertainty, demonstration
scarcity, and challenging visual conditions. In RL, Carlucho et al. [416] introduce an actor–critic con-
troller that directly predicts joint torques for an underwater manipulator while respecting position and
torque constraints, reducing dependence on an accurate hydrodynamic model. In IL, AquaBot [417]
first learns from human teleoperation through behavior cloning and subsequently improves the policy
using autonomous real-world trials, supporting tasks such as grasping, sorting, and object retrieval.
Bi-AQUA [418] learns from bilateral-control demonstrations and introduces lighting-aware feature
modulation and transformer conditioning to maintain manipulation performance under varying under-
water illumination. UMI-Underwater [419] further reduces reliance on underwater teleoperation by
autonomously collecting underwater grasp demonstrations and transferring knowledge from on-land
human demonstrations through a depth-based affordance representation. An affordance-conditioned
diffusion policy then generates robot actions that remain robust to changes in lighting, color, and
background appearance. Together, these methods indicate a shift from manually operated systems
toward autonomous and data-scalable underwater manipulation.
Challenges. Underwater manipulation remains constrained by uncertain hydrodynamics, strong
coupling between vehicle and manipulator motion, limited visibility, communication latency, and
the difficulty of regulating contact forces in moving fluids. Learning-based approaches additionally
face scarce real-world demonstrations, costly and risky data collection, limited simulation fidelity,
and substantial distribution shifts across water conditions, lighting, payloads, and deployment sites.
Future progress will require tighter integration of model-based control with learned policies, scalable
self-supervised data collection, robust multimodal perception using vision, sonar, proprioception, and
force sensing, and safety-aware adaptation under changing environmental dynamics.
5. High-level Planning
High-level planning in robot manipulation provides structured guidance for low-level execution by
determining what actions to perform, in which order, and which aspects of the environment are
31


<!-- page 32 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Decision 
Layer
Motion 
Generation Layer
Actuation 
Control Layer
High-level Planning (§5)
• Task Plan (§5.1 & §5.2)
• Code (§5.3)
• Geometric Objective and Constraint (§5.4)
• Affordance (§5.5)
• 3D Representations (§5.6)
Output: Structured Artifacts (e.g., symbolic plan, program, 
constraint set, affordance prior, structured 3D world, video)
Low-Level Action Modeling
Classical Non-Learning
• Sampling-based Planning
• Trajectory Optimization
• Model Predictive Control …
Output: Trajectory
Actuation-Level Control
• Joint-space Control (Position, Velocity, Torque)
• Interaction Control (Impedance, Admittance)
Output: Motor torques
Learning-Based (§6)
• Input Modeling (§6.2)
• Latent Learning (§6.3)
• Policy Learning (§6.4)
Output: Actions
Language / Perception
(or other modalities)
Instantiated as target 
pose / constraint
Instantiated as 
input/latent
Robot Dynamics
• Video (§5.7)
Figure 12 | Method taxonomy for basic manipulation, extensible to other manipulation tasks. It
comprises High-Level Planning, Low-Level Action Modeling, and Actuation-Level Control. High-level
modules produce planning artifacts that guide downstream action generation, while low-level methods
operate on these artifacts or raw multimodal observations. Solid arrows indicate the survey’s primary
focus: High-Level Planning and Learning-Based Low-Level Action Modeling.
relevant. LLMs and MLLMs are increasingly used for task planning, programmatic planning, and
geometric constraint-based planning, supporting task decomposition, skill sequencing, executable
program generation, and spatially grounded reasoning. In parallel, affordance-based planning
and 3D representation-based planning provide actionable intermediate representations, such as
functional regions, contact cues, geometric relations, and structured scene states. More recently,
video-based planning extends this paradigm by representing future task evolution through generated
visual trajectories or predictive world models, enabling prospective reasoning over action outcomes and
plan refinement. Together, these approaches establish high-level planning as a flexible guidance layer
that integrates semantic reasoning, spatial grounding, scene understanding, and future prediction
to support reliable execution across diverse manipulation tasks. We summarize this taxonomy in
Figure 13 and provide a visualization in Figure 14.
32
CJ CC]


<!-- page 33 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
High-level Planner (§ 5)
LLM-based Task
Planning 5.1
Grounded & Closed-Loop
Planning
SayCan [420], Grounded Decoding [421], Inner
Monologue [422], LLM-Planner [423], Polaris [424]
Feasibility-Aware Planning
LLM+P [425], LLM3 [426], REFLECT [427]
Preference & Collaborative
Planning
APRICOT [428], MALMM [429], RoCo [430]
MLLM-based Task
Planning 5.2
General-Purpose MLLM
Reasoning
PaLM-E [76], VILA [431], PG-InstructBLIP [432], EVLP [433],
EmbodiedGPT [434]
Spatial Reasoning &
Grounding
SpatialVLM [435], SpatialBot [436], RoboSpatial [437],
EmbodiedVSR [438], SoFar [439], RoboRefer [178]
Reward & Progress Reasoning
Robo-Dopamine [440], RoboReward [441], Robometer [442],
ProcVLM [443]
Failure Reasoning & Recovery
AHA [444], Code-as-Monitor [445], I-FailSense [446],
Rewind-IL [447], AgentChord [448]
Robot-Specialized Embodied
Reasoning
RoboBrain [449], RoboBrain 2.0 [450], RynnBrain [451],
FSD [452], Embodied-R1 [453], Gemini Robotics [454]
Programmatic
Planning 5.3
Language-to-Program
Code as Policies [455], ProgPrompt [456], ChatGPT for
Robotics [457]
Demonstration-to-Program
Instruct2Act [458], Demo2Code [459], SHOWTELL [460],
Statler [461]
Grounded & Verifiable
Programs
InterPreT [462], Reliable CaP [463], HyCodePolicy [464]
Geometric
Constraint-Based
Planning 5.4
Spatial Objectives
VoxPoser [465], IKER [466]
Relational & Keypoint
Constraints
CoPa [467], ReKep [468], GeoManip [469]
Functional Constraints
CoDex [470]
Affordance-Based
Planning 5.5
Geometric Affordance
Ditto [471], GAPartNet [472], CPM [473], RoboPCA [474]
Visual Affordance
Transporter Networks [475], VAPO [476], RAAP [477]
Semantic Affordance
Affordance-Based Imitation Learning [478], SAGE [479]
Multimodal Affordance
CLIPort [480], ManipLLM [481], MOKA [482], A3VLM [483],
RoboPoint [484], UniAff [485], BiPreManip [486]
3D Representation-
Based Planning 5.6
Point-Cloud Representations
Point-Cloud Planning [487], PA3FF [488]
Implicit & Descriptor Fields
NDF [489], R-NDF [490], F3RM [491], 𝐷3Fields [492],
PA3FF [488]
Gaussian-Splatting
Representations
Splat-MOVER [493], Physically Embodied GS [494],
MSGField [495], RoboSplat [496]
Generative & Structured 3D
Representations
Imagination Policy [497], RoboEXP [498]
Figure 13 | Taxonomy of high-level planning approaches, organized into major planning paradigms,
including LLM- and MLLM-based task planning, programmatic planning, and geometric constraint-
based planning, together with supporting capabilities in affordance learning and 3D representations.
5.1. LLM-Based Task Planning
Early work followed a symbolic planning and grounding paradigm, in which neural networks mapped
demonstrations and observations to symbolic states and goals represented by predicate truth val-
ues [499]. LLMs have subsequently extended this paradigm by providing semantic knowledge,
instruction decomposition, and open-vocabulary reasoning, while frequently retaining symbolic repre-
sentations or predefined robot skills for grounding and execution. SayCan [420] is an early influential
example that combines language-model-based task relevance with learned affordance scores estimat-
33


<!-- page 34 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
ing skill executability, thereby selecting actions that are both semantically appropriate and physically
feasible. Grounded Decoding [421] further integrates language and grounded model likelihoods
during sequence decoding. However, these methods primarily perform planning without incorporating
execution feedback. Inner Monologue [422] addresses this limitation by feeding task-success signals,
scene descriptions, and human feedback back into the LLM reasoning process, enabling closed-loop
plan revision in unstructured environments. Related feedback-driven replanning is also explored in
LLM-Planner [423].
Another line of work improves the logical and physical feasibility of LLM-generated plans. LLM+P
[425] translates natural-language problems into PDDL representations and delegates plan search to
a classical planner, combining the semantic flexibility of LLMs with the correctness guarantees of
symbolic planning. LLM3 [426] more directly connects task and motion planning by using motion-
planning failures to revise action sequences and continuous parameters, reducing repeated exploration
of geometrically infeasible plans. REFLECT [427] similarly diagnoses unsuccessful interactions and
uses the resulting failure information to generate corrective plans. These methods shift LLM-based
planning from unconstrained language generation toward iterative planning grounded in symbolic
validity, motion feasibility, and execution outcomes.
Recent studies further incorporate user preferences, safety requirements, and broader interaction
structures. APRICOT [428] combines LLM-based active preference learning with constraint-aware
task planning, querying users to resolve ambiguous preferences while adapting plans to geometric
limitations. MALMM [429] employs multiple LLM agents to improve planning and decision-making,
while Polaris [424] combines LLM reasoning with Syn2Real visual grounding for open-ended tabletop
manipulation. RoCo [430] extends LLM-based planning to multi-robot collaboration and introduces
RoCoBench for evaluating collaborative manipulation tasks.
5.2. MLLM-based Task Planning
Text-only LLMs require visual observations and other sensory inputs to be processed by separate
perception modules before reasoning. In contrast, MLLMs [3, 77, 500] jointly process visual and
linguistic information, enabling tighter integration of perception, reasoning, planning, and execution
monitoring. We therefore view MLLM-based task planning as a closed-loop process that encompasses
plan generation, spatial grounding, progress evaluation, failure diagnosis, and corrective reasoning.
General-Purpose MLLM Reasoning. Early studies adapt general-purpose MLLMs to robotic decision-
making. PaLM-E [76] incorporates continuous embodied observations into a pretrained language
model, enabling visually grounded sequential decision-making, while VILA [431] directly lever-
ages GPT-4V for visual grounding and manipulation planning without task-specific fine-tuning. PG-
InstructBLIP [432] instead fine-tunes InstructBLIP [501] on physical concepts to strengthen physical
reasoning. EmbodiedGPT [434] introduces embodied chain-of-thought reasoning [502], and Zhang
et al. [503] further incorporate fine-grained reward guidance. Matcha [504] enables interactive
multimodal perception, whereas EVLP [433] jointly generates linguistic subplans and visual sub-
goals. Socratic Models [505] and Socratic Planner [506] further coordinate specialized perception,
reasoning, and control modules through language.
Spatial Reasoning and Grounding. Spatial reasoning supplies the geometric and relational in-
formation required to ground high-level instructions into manipulation plans. SpatialVLM [435],
SpatialBot [436], and RoboSpatial [437] improve metric, directional, and 3D scene understand-
ing, while EmbodiedVSR [438] organizes evolving relations through dynamic scene graphs. For
manipulation-specific grounding, SoFar [439] represents object poses and action directions using
language-grounded functional orientations, and RoboRefer [178] combines depth-aware perception
34


<!-- page 35 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
with multi-step spatial referring. These methods provide intermediate representations, including
orientations, referring regions, scene graphs, affordances, and geometric relations, that constrain
downstream action generation.
Reward and Progress Reasoning. MLLMs can also serve as critics that evaluate execution progress
and provide feedback for replanning or policy improvement. Robo-Dopamine [440] models fine-
grained manipulation progress, RoboReward [441] learns general-purpose vision–language rewards
from diverse robot trajectories, and Robometer [442] combines within-trajectory progress estimation
with cross-trajectory comparison. ProcVLM [443] further grounds dense rewards in procedural
stages and visual state transitions. Together, these methods extend multimodal reasoning from plan
generation to execution evaluation.
Failure Reasoning and Recovery. Failure reasoning closes the planning loop by detecting deviations,
diagnosing their causes, and selecting corrective actions. AHA [444] detects manipulation failures and
produces natural-language explanations for plan revision, while Code-as-Monitor [445] translates task
constraints into executable visual programs for reactive and proactive monitoring. I-FailSense [446]
targets failure detection across robots and tasks, and self-refining VLMs [507] improve failure
recognition and reasoning through iterative feedback. Rewind-IL [447] leverages detected failures
for recovery learning, whereas AgentChord [448] incorporates anticipated failure branches and
corrective transitions into task graphs. These approaches extend one-shot planning toward closed-
loop monitoring, diagnosis, recovery, and replanning.
Robot-Specialized Embodied Reasoning. Recent work increasingly trains MLLMs specifically for
robotic perception and reasoning. RoboBrain [449] learns from robot-centric annotations spanning
task plans, affordances, and end-effector trajectories, while RoboBrain 2.0 [450] extends these
capabilities to spatial–temporal reasoning and closed-loop interaction. RynnEC [508] emphasizes
region-centric visual representations, and RynnBrain [451] further integrates embodied reasoning
within a unified foundation model. FSD [452] connects spatial reasoning to manipulation through
affordance regions and visual traces, whereas Embodied-R1 [453] uses pointing as an intermediate
interface between multimodal reasoning and action generation. Other embodied models, including
ERA [509], GenieReasoner [510], PhysBrain [511], HY-Embodied [512], and ACE-Brain [513], further
integrate task reasoning, spatial grounding, affordance prediction, and action-related representations.
Overall, this trend shifts MLLMs from external planners toward embodied foundation models that
support planning, grounding, evaluation, and closed-loop adaptation within a unified framework.
5.3. Programmatic Planning
Programmatic planning represents robot plans as executable programs that connect high-level seman-
tic reasoning with perception, motion primitives, and control APIs. Early work maps natural-language
instructions to robot programs [514], while Code as Policies [455] prompts LLMs with perception and
control APIs to synthesize executable policies. ProgPrompt [456] similarly generates situated robot
programs with explicit action and state structures, and Vemprala et al. [457] establish a reusable
framework for integrating ChatGPT with robotic APIs. Subsequent methods broaden the available
supervision and program representations. Instruct2Act [458] integrates visual foundation models
for multimodal instruction following, Demo2Code [459] abstracts demonstrations into reusable pro-
grammatic skills, and SHOWTELL [460] generates policy code directly from visual demonstrations.
Statler [461] further maintains an explicit world state to support longer-horizon reasoning.
Recent work increasingly focuses on grounding, verification, and adaptation of generated pro-
grams. InterPreT [462] learns executable predicates from language feedback and compiles them
with learned symbolic operators into PDDL domains for generalizable planning. Towards Reliable
35


<!-- page 36 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Programmatic Planning
Geometric Constraint-
based Planning
3D 
Representations
(t = 0) Instruction: Cook a potato and put it into the recycle bin.
LLM Planner: Plan → navigate to potato → pick up → … → place in recycle bin.
(t = 5) Observation: Potato not found; fridge observed.
LLM Planner: Replan → navigate to fridge → open → pick up potato → close → … → 
place in recycle bin.
(t = 20) Observation: Recycle bin not found; garbage can observed.
LLM Planner: Replan → navigate to
garbage can → place potato.
Visual Planning
Affordance
MLLM-based Task Planning
Text / Code Planning
Video: 
LLM-based Task Planning
Figure 14 | Overview of the taxonomy of high-level planners, highlighting six core components:
LLM-based task planning, MLLM-based task planning, code generation, motion planning, affordance
learning, and 3D scene representations. Figure adapted from [423, 434, 455, 465, 471, 491].
Code-as-Policies [463] combines symbolic verification with interactive environment exploration to
validate task-relevant conditions before execution. HyCodePolicy [464] closes the programming loop
by integrating geometric grounding, visual monitoring, failure diagnosis, and iterative code repair.
More recently, Functional Cache Grafting [515] retrieves and composes validated function-level code
structures, reducing redundant generation while improving policy robustness. Overall, program-
matic planning is evolving from one-shot language-to-code generation toward grounded, verifiable,
self-correcting, and reusable executable representations.
5.4. Geometric Constraint-based Planning
Geometric objectives and constraints provide an intermediate representation between semantic task
reasoning and motion execution. Rather than directly mapping observations to robot actions, these
36
yin
my
EB
=
L-
Large
<+—--- Stack the blocks on the empty bowl. ®
Language
Model
APIs
APIs
l Policy Code
id
For Bowname. in bowl names:
em med eis
MT
Assistant.
i
bail
|
)
=
‘The video displays a red robotic arm, a red cylinder, and a ring, The cylinder is positioned on a flat surfice, and
chfeto,stack
= Tempty bowl] + block names
ED
¢
| he
the ing is positioned next to it, with their centers aligned. The robotic am is then sed (0 pick up the ing.
=
EX
-“
§
=
|
Carefully, the center of the ring is aligned withthe center of the cylinder, and the ring is slowly lowered onto the
if
def is_copty(nane):
/ $
{
“cylinder, joining the two together. The final step is to inspect thejoin using the robotic arm, ensuring that it is
def stack_objects(obj_names):
I.
-
secure and without gaps.
rate
ho
hs
for Lin roneeCoobis
- 1:
=!
Human: can you write a detailed plan
a1 = ovmametiy
{
-
for the task the robot is performing?
Pik
15ctTonse, ob31
|
Assistant:
1. Position the first object, a cylinder, on a flat surface.
2. Position the second object, a
ring, next to the red cylinder, with their centers aligned
=2
13. Use the robotic arm to pick up the ring.
~~
4 Carefully align the centerof the ring with the center of the cylinder.
15. Slowly lower the ring onto the cylinder, joining the two objects together.
P|Cam##l ,
Y
def affordance_nap():
i
i
pe
A
a
msize = (100,100,100)
i
i
i.
J
Vision
map = np.zeros(msize)
H
H
iW
L
handles = dezect(’handle') |_}
i
—
5
—>
Language |
k= lambda x: x.posf2]
H
H
a
~
fe
handles. sort(key=k)
i
H
LY
4
er
Model
top_handle = handles[-1]
H
cE
i
}
}’
Re:
X,¥,Z = top_handle.pos
i
View
IH
gas
Wr
5
Cam#2 [7°
return skootap)
Affordance Maps
ER
msize = (100,100,100)
H
iB
NP
a
map = np.zeros(msize)
H
H
LE
Openthe top drawer.
Large
vases ~ detect(vase’)
i
|
0
en
g
vase = vases[0.
lH
i
il
@ Please alsowatch
—» Language —»
ots vase occupancy. grid =>
i
a]
yz]
= -
i
i
out for that vase!
Model
Be] erties
1
i


<!-- page 37 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
approaches translate language and perception into spatial costs, keypoint relations, target poses, or
geometric constraints that can be optimized by downstream planners. VoxPoser [465] composes
language-conditioned 3D value maps as spatial objectives for model-based trajectory generation.
CoPa [467] identifies task-relevant object parts and their spatial relations to derive target end-effector
poses, while ReKep [468] represents manipulation tasks as sequences of optimizable relational
constraints over semantic 3D keypoints. GeoManip [469] further treats stage-specific geometric
constraints as a general interface between semantic reasoning and trajectory optimization.
Recent work extends this paradigm toward adaptive objectives and more complex physical inter-
actions. IKER [466] uses VLMs to generate and iteratively refine keypoint-based reward functions
from language and RGB-D observations, enabling geometric task specification for downstream policy
learning. CoDex [470] similarly infers semantic constraints for dexterous functional manipulation
and uses constrained optimization to generate physically feasible grasp candidates before policy
refinement. Collectively, these methods separate semantic task interpretation from numerical motion
generation through explicit, optimizable geometric representations, improving the modularity and
physical grounding of manipulation planning.
5.5. Affordance-Based Planning
Affordance-based planning represents manipulation tasks through action-oriented properties that
specify where and how an agent can interact with objects or environments. Originating from
Gibson’s notion of affordance [516], this perspective provides an intermediate abstraction between
semantic understanding and motion generation. Rather than directly predicting complete trajectories,
affordance-based methods identify functional parts, interaction regions, keypoints, contact poses,
action directions, or kinematic constraints that guide downstream execution. We organize these
methods by their dominant information source and representation into geometric, visual, semantic,
and multimodal affordances, while noting that recent approaches increasingly combine these cues.
Geometric Affordance. Geometric affordances derive interaction possibilities primarily from object
shape, articulation, and kinematic structure. Early methods infer parts, joints, and motion constraints
directly from 3D observations [471, 472, 517]. Ditto [471], for example, reconstructs articulation
models from physical interaction, while GAPartNet [472] introduces cross-category generalizable
actionable parts that support skill transfer across object instances. CPM [473] further represents
manipulation through compositional geometric relations between functional parts. For articulated ob-
jects, Kinematic-aware Prompting [518] converts joints and contact locations into a unified kinematic
description and prompts an LLM to generate 3D manipulation waypoints, explicitly connecting object
kinematics with low-level action generation. ScrewSplat [519] instead reconstructs object geometry,
movable parts, and screw axes directly from RGB observations, providing an explicit kinematic model
that can subsequently support text-guided manipulation. More recently, RoboPCA [474] jointly
predicts task-conditioned contact regions and end-effector poses from RGB-D observations, coupling
where to interact with how the interaction should be geometrically realized.
Visual Affordance. Visual affordances infer interaction opportunities directly from images, commonly
representing them as pixels, regions, keypoints, or action-conditioned heatmaps. Transporter Net-
works [475] establish a spatially equivariant formulation for pick-and-place by predicting image-space
action locations, while VAPO [476] learns visual affordances from unstructured interaction data.
KITE [520] grounds language instructions into 2D image keypoints and conditions downstream
manipulation skills on these keypoints, enabling fine-grained object- and part-level interaction across
scene variations. UAD [521] reduces the dependence on manually annotated affordances by distilling
complementary knowledge from pretrained vision and vision–language models into a lightweight
task-conditioned affordance predictor. Recent work further improves transfer beyond fixed training
37


<!-- page 38 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
categories. RAAP [477] combines retrieval with cross-image alignment, decoupling contact localiza-
tion from post-contact action direction to transfer affordances across unseen objects. Together, these
methods turn visual grounding and correspondence into actionable intermediate representations for
manipulation.
Semantic Affordance. Semantic affordances associate object identity, functional parts, and task
concepts with possible interactions. Early affordance-based imitation learning [478] showed that
semantic properties can provide transferable priors for mapping observations to manipulation be-
haviors. More recent methods shift from category-level semantics toward functional and part-level
representations. SAGE [479] bridges semantic parts with Generalizable Actionable Parts, combining
instruction interpretation with part-level motion knowledge to construct executable policies. PartIn-
struct [522] further highlights the importance of such fine-grained grounding through a benchmark
in which instructions explicitly refer to object parts and their task-dependent roles, exposing the
difficulty of jointly grounding part semantics and predicting manipulation actions in 3D space. This
distinction between semantic identity and physical functionality is especially important for articulated
and multi-part objects, where similarly named parts may exhibit different kinematics and afford
different interactions.
Multimodal Affordance. Foundation models increasingly combine language, vision, geometry, demon-
strations, and interaction feedback to infer richer affordance representations. CLIPort [480] couples
a semantic “what” pathway with a spatial “where” pathway for language-conditioned manipulation.
ManipLLM [481] further reasons about object categories, affordance priors, contact points, and
end-effector directions within an embodied MLLM. MOKA [482] uses marked visual prompts to elicit
point-based affordances from pretrained VLMs, providing a compact interface between semantic
reasoning and robot motion, while RoboPoint [484] predicts spatial affordance points from language
and images. PIVOT [523] similarly turns continuous spatial decisions into iterative visual selection by
overlaying candidate actions, locations, or trajectories onto images and repeatedly querying a VLM to
refine them, enabling actionable spatial reasoning without task-specific fine-tuning.
Retrieval provides another route to generalizable affordance reasoning. RAM [524] constructs an
affordance memory from heterogeneous robot, human–object interaction, and custom demonstrations,
retrieves task-relevant examples from language instructions, and transfers the retrieved 2D affordance
into an executable 3D affordance in the target scene. For articulated manipulation, A3VLM [483]
learns robot-agnostic articulation and action affordances that can be instantiated through downstream
motion primitives, whereas UniAff [485] jointly models affordance understanding and object-centric
3D motion constraints for both articulated objects and tools. AIC MLLM [525] further closes the
interaction loop by using visual and textual feedback from failed interactions to correct predicted
SE(3) contact poses, showing how affordance-related geometric decisions can be refined through
physical experience. BiPreManip [486] uses affordance prediction prospectively, reasoning about
the desired final interaction to plan preparatory actions for coordinated bimanual manipulation.
These developments shift affordances from passive interaction descriptors toward explicit planning
interfaces that connect multimodal task reasoning, geometric grounding, interaction feedback, and
executable robot behavior.
5.6. 3D Representation-Based Planning
3D representation-based planning uses structured scene representations to bridge perception and ac-
tion by exposing planning-relevant geometry, semantics, relations, or goal states. Rather than directly
mapping observations to control signals, these methods support manipulation through intermediate
representations such as point-cloud transformations, continuous descriptor fields, editable Gaussian
scenes, imagined goal geometries, or action-conditioned scene graphs. We focus on representations
38


<!-- page 39 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
that explicitly support goal specification, correspondence, search, or downstream motion generation.
Point-Cloud Representations. Point clouds provide an explicit geometric state space for manipulation
planning. Saha et al. [487] formulate multi-object rearrangement as A* search directly over point-
cloud transformations, avoiding discrete symbolic state and action representations. Related methods
use point clouds to encode functional parts or geometric targets for manipulation. For example,
PA3FF [488] learns a continuous part-aware 3D feature field from point-cloud inputs, providing
functional-part representations that support correspondence and downstream policy learning.
Implicit and Descriptor Fields. Implicit fields provide continuous, geometry-aware representa-
tions for pose correspondence and language-conditioned manipulation. NDF [489] learns SE(3)-
equivariant descriptors for pose transfer, while R-NDF [490] extends them to relational rearrangement.
F3RM [491] distills 2D foundation-model features into 3D fields for few-shot language-guided grasp-
ing and placing. 𝐷3Fields [492] further models dynamic semantic and instance-aware descriptors for
zero-shot rearrangement, while PA3FF [488] incorporates functional part structure to improve robust
articulated-object generalization.
Gaussian-Splatting Scene Representations. Gaussian Splatting provides an explicit and editable
3D scene representation combining geometry, appearance, and semantics. Splat-MOVER [493]
embeds semantic and affordance features into 3DGS and generates grasp candidates for multi-
stage open-vocabulary manipulation. Physically Embodied Gaussian Splatting [494] couples visual
Gaussians with particle-based physical states for predictive and correctable scene modeling, while
MSGField [495] augments Gaussian primitives with semantic and motion attributes for dynamic
manipulation. RoboSplat [496] instead exploits scene editability to synthesize diverse demonstrations
and improve downstream policy generalization.
Generative and Structured 3D Representations. Beyond reconstructing the current scene, 3D rep-
resentations can encode desired future states and action-relevant structure. Imagination Policy [497]
generates target point clouds and recovers keyframe actions through rigid registration, formulating
action inference as goal-state generation. RoboEXP [498] incrementally builds action-conditioned
scene graphs through interaction, combining geometry, semantics, and relational structure for down-
stream manipulation. These approaches extend 3D representations from static perception toward
explicit goal and interaction representations for planning.
5.7. Video-Based Planning
Video-based planning represents task evolution through predicted visual futures, providing a temporal
interface between task understanding and robot execution. Unlike static goals or geometric constraints,
videos encode object motion, interaction outcomes, and intermediate task states. Recent world models
further condition future prediction on language or robot actions, enabling visual rollouts to support
action extraction, model-based planning, and planner optimization. We focus on methods where
predicted futures directly contribute to plan representation, action selection, or planner learning.
Generative Video Planning. One line of work treats generated future observations as visual plans.
Large Video Planner [526] learns from large-scale human and task videos to produce zero-shot
video plans that are converted into robot actions. RIGVid [527] generates manipulation videos
from language and initial observations, filters them with a VLM, and recovers object trajectories
through 6-DoF pose tracking. Geometry-aware 4D Video Generation [528] improves cross-view
geometric consistency in generated RGB-D videos, while GEM-4D [529] adds dense 4D correspondence
supervision and inverse dynamics for trajectory recovery. These methods use video as an explicit
spatiotemporal plan that can be translated into robot motion.
39


<!-- page 40 (ocr) -->
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Predictive World-Model Planning. A second direction predicts the consequences of candidate actions
for action selection. SAMPO [530] performs action-conditioned video prediction for model-based
control. Grounded World Model [531] predicts outcomes in a vision–language-aligned latent space
and scores them against task instructions, enabling language-conditioned model-predictive control.
Here, the world model functions as a predictive dynamics model within the planning loop.
World-Model-Guided Planner Learning. World models can also provide simulated interaction for
improving planners with fewer physical rollouts. DreamPlan [532] uses imagined rollouts from an
action-conditioned video world model to construct preferences for reinforcement fine-tuning of a VLM
planner. RoboEvolve [533] co-evolves a VLM planner and video simulator using simulated successes
and near-miss failures. GE-Sim 2.0 [534] further supports closed-loop simulation by predicting
visual and proprioceptive evolution and providing rollout-level supervision for policy learning. These
approaches position world models as learned environments for planner refinement.
6. Low-level Learning-based Action Modeling
Low-level action modeling focuses on how robots transform perception and task context into executable
actions, trajectories, or action sequences, providing the interface between high-level planning and
physical execution. While high-level planning determines what to do and in what order, such as task
decomposition, skill sequencing, or goal reasoning, low-level action modeling determines how planned
intent is instantiated into concrete manipulation behaviors through learned visuomotor mappings.
The two are complementary: high-level planners provide structured intent and semantic constraints,
whereas low-level action models translate them, or directly map multimodal observations, into action
representations that can be executed by controllers. Within this framework, learning paradigms
such as imitation learning and reinforcement learning define how action models are optimized. We
further decompose learning-based low-level action modeling into three interdependent components:
input modeling, which determines what sensory and contextual information is used and how it is
encoded; latent learning, which studies compact and transferable internal representations; and policy
learning, which determines how these representations are decoded into executable actions. Together,
this taxonomy provides a unified view of learning-based action generation by connecting perception,
representation, and policy optimization between high-level reasoning and actuation-level control.
6.1. Learning Strategy
6.1.1. Reinforcement Learning
In robotic manipulation, reinforcement learning (RL) has emerged as a central paradigm for acquiring
complex skills. By leveraging high-dimensional perceptual inputs (e.g., vision or proprioception)
and reward signals as feedback, RL enables agents to learn control policies through trial-and-error
interaction with the environment. This section reviews RL methods for robotic manipulation from
both theoretical and application perspectives. We categorize existing approaches into two main
classes: model-free and model-based algorithms, depending on whether the agent exploits an explicit
or learned dynamics model to guide the learning process. Representative methods across these
categories are summarized in Table 8.
i) Model-Free Methods
In robotic manipulation, model-free RL learns policies or value functions directly from interaction
data without explicitly modeling environment dynamics. Its flexibility makes it suitable for high-
dimensional and contact-rich manipulation, but typically at the cost of substantial interaction data
and limited sample efficiency. Recent work therefore increasingly combines RL with offline data,
40
