<!-- page 1 (ocr) -->
HumanoidBench: Simulated Humanoid Benchmark
for Whole-Body Locomotion and Manipulation
Carmelo Sferrazza1
Dun-Ming Huang1
Xingyu Lin1
Youngwoon Lee1,2
Pieter Abbeel1
1UC Berkeley
2Yonsei University
Fig. 1:
Humanoid robots equipped with dexterous hands hold immense promise for integration into real-world human
environments. Nonetheless, harnessing the full potential of humanoid robots presents numerous challenges, such as the intricate
control of robots with complex dynamics, sophisticated coordination among various body parts, and addressing long-horizon
complex tasks envisioned for these robots. We present HumanoidBench, a simulated humanoid robot benchmark consisting of
15 whole-body manipulation and 12 locomotion tasks, such as shelf rearrangement, package unloading, and maze navigation.
Abstract—Humanoid robots hold great promise in assisting
humans in diverse environments and tasks, due to their flexibility
and adaptability leveraging human-like morphology. However,
research in humanoid robots is often bottlenecked by the
costly and fragile hardware setups. To accelerate algorithmic
research in humanoid robots, we present a high-dimensional,
simulated robot learning benchmark, HumanoidBench, featuring
a humanoid robot equipped with dexterous hands and a variety
of challenging whole-body manipulation and locomotion tasks.
Our findings reveal that state-of-the-art reinforcement learning
algorithms struggle with most tasks, whereas a hierarchical
learning approach achieves superior performance when supported
by robust low-level policies, such as walking or reaching. With
HumanoidBench, we provide the robotics community with a
platform to identify the challenges arising when solving diverse
tasks with humanoid robots, facilitating prompt verification
of algorithms and ideas. The open-source code is available at
https://humanoid-bench.github.io.
I. INTRODUCTION
Humanoid robots have long held promise to be seamlessly
deployed in our daily lives. Despite the rapid progress in
humanoid robots’ hardware (e.g., Boston Dynamics Atlas, Tesla
Optimus, Unitree H1), their controllers are fully or partially
hand-designed for specific tasks, which requires significant en-
gineering efforts for each new task and environment, and often
demonstrates only limited whole-body control capabilities.
In recent years, robot learning has shown steady progress in
both robotic manipulation [12, 69, 15] and locomotion [27, 71].
However, scaling learning algorithms to humanoid robots is
still challenging and has been delayed mainly due to such
robots’ costly and unsafe real-world experimental setups.
To accelerate the progress of research for humanoid robots,
we present the first-of-its-kind humanoid robot benchmark,
HumanoidBench, with a diverse set of locomotion and
manipulation tasks, providing an accessible, fast, safe, and
inexpensive testbed to robot learning researchers. Our simulated
humanoid benchmark demonstrates a variety of challenges
in learning for autonomous humanoid robots, such as the
intricate control of robots with complex dynamics, sophisticated
coordination among various body parts, and long-horizon
complex tasks.
HumanoidBench provides (1) a simulation environment
comprising a humanoid robot with two dexterous hands, as illus-
trated in Figure 1; (2) a variety of tasks, spanning locomotion,
manipulation, and whole-body control, incorporating humans’
everyday tasks; (3) a standardized benchmark to evaluate the
progress of the community on high-dimensional humanoid
robot learning and control. In fact, HumanoidBench supports
generic controller structures, including both learning and model-
based approaches [14, 26]. In this paper, we present extensive
benchmarking results of the state-of-the-art reinforcement
learning (RL) algorithms, which do not require extensive
domain knowledge, and a hierarchical RL approach.
The simulation environment of HumanoidBench uses the
MuJoCo [60] physics engine. For the simulated humanoid robot,
arXiv:2403.10506v2  [cs.RO]  18 Jun 2024
97.Ta


<!-- page 2 (ocr) -->
Benchmark
Dexterous hands
Action dim.
DoF
Task horizon
# Tasks
Skills1
MyoHand [8]
39
23D
50-2000
9
PnP, R, Po, IR, H, Ro
Adroit [49]
24
24D
200
4
PnP, P, R, Po, IR, H, L, Ro
MyoLeg [8]
80
20D
1000
1
Lo, St
LocoMujoco [3] (Unitree-H1)
19
6D
100-500
27
L, Lo, St, BM
DMControl [58] (Humanoid)
24-56
22D
1000
6
Lo, St
FurnitureSim [22]
8
6D
2300
8
PnP, P, I, IR, H, L, Ro
robosuite [70]
6-24
6-7D
500
9
PnP, P, I, R, IR, H, L, Ro
rlbench [24]
6-7
6-7D
100-1000
106
PnP, P, I, R, Po, IR, H, L, Ro
metaworld [64]
6
7D
500
50
PnP, P, I, R, Po, IR, H, L, Ro
HumanoidBench (Ours)
61
75D
500-1000
27
PnP, P, I, R, Po, IR, H, L, Ro, Lo, BM, St
1PnP: Pick-and-place / P: Push / I: Insert / R: Reach / Po: Pose / IR: In-hand re-orientation / H: Hold / L: Lift / Ro: Rotate / Lo: Locomotion / BM: Whole-body (humanoid)
Manipulation / St: Stabilization
TABLE I: Comparison of simulated robot benchmarks. Our humanoid robot benchmark tests a variety of complex, long-
horizon task with a large action space.
we mainly opt for a Unitree H1 humanoid robot1, which is
relatively affordable and offers accurate simulation models [66],
with two dexterous Shadow Hands2 attached to its arms. Our
environment can easily incorporate any humanoid robots and
end effectors; thus, we provide other models, including Unitree
G13, Agility Robotics Digit4, the Robotiq 2F-85 gripper, and
the Unitree H1 hand.
The HumanoidBench task suite includes 15 distinct whole-
body manipulation tasks involving a variety of interactions, e.g.,
unloading packages from a truck, wiping windows using a tool,
catching and shooting a basketball. In addition, we provide 12
locomotion tasks (not requiring hands’ dexterity), which can
serve as primitive skills for whole-body manipulation tasks
and provide a set of easier tasks to verify algorithms. The
benchmarking results on this task suite show how the state-of-
the-art RL algorithms struggle with controlling the complex
humanoid robot dynamics and solving the most challenging
tasks, illustrating ample opportunities for future research.
II. RELATED WORK
Deep reinforcement learning (RL) has made rapid progress
with the advent of standardized, simulated benchmarks, such
as Atari [5] and continuous control [7, 58] benchmarks. In
robotic manipulation, most existing simulated environments
are limited to quasi-static, short-horizon skills, having focused
on tasks like picking and placing [7, 24, 70, 64, 37], in-hand
manipulation [49, 44, 8], and screwing [43].
Complex manipulation tasks, such as block stacking [13],
kitchen tasks [17], and table-top manipulation [25, 39, 34],
have been introduced but are still limited to a combination of
pushing, picking, and placing. On the other hand, the IKEA
furniture assembly environment [31], BEHAVIOR [55, 32], and
Habitat [57] present diverse long-horizon (mobile) manipulation
tasks, with their main focus being on high-level planning by
abstracting complex low-level control problems, while Furni-
tureBench [22] introduces a simulated benchmark for complex
1https://www.unitree.com/h1
2https://www.shadowrobot.com/dexterous-hand-series/
3https://www.unitree.com/g1
4https://agilityrobotics.com/robots
long-horizon furniture assembly tasks with sophisticated low-
level control.
However, most of these benchmarks use a single-arm
manipulation setup with either a parallel gripper or a dexterous
hand [9, 49], limiting the types of object interactions and not
addressing the challenges of coordinating multiple parts of a
body [30], e.g., multiple fingers, arms, and legs. Robosuite [70]
includes a handful of bimanual manipulation tasks, while more
recently Chen et al. [10] and Zakka et al. [67] have introduced
additional benchmarks that require coordinating two floating
robot hands, i.e., not attached to any arm base.
While bimanual manipulation is one of the key objectives
of humanoid robots, most benchmarks in humanoid research
have so far focused on the locomotion challenges [8, 28, 45, 3].
In this regard, such simulations have accelerated research on
control algorithms [6, 46, 47, 40], ultimately leading to achieve
robust humanoid locomotion in the real world [1, 50, 11].
Recent works have extended humanoid simulations to
different domains involving a certain degree of manipulation,
i.e., tennis [68], soccer [19], ball manipulation [61] and catching
[38], and box moving [63]. However, all these works focus
on demonstrating their approaches on specific humanoid tasks
and lack a diversity of tasks. In addition, most of the previous
work focuses on simplistic humanoid models [38, 61], leading
to inaccurate physics and collision handling. This motivates us
to implement a comprehensive simulated humanoid benchmark
based on real-world hardware and consisting of a diverse set
of whole-body control tasks with careful design choices for
diversity and usability.
In contrast to prior robotic simulation benchmarks, Hu-
manoidBench presents a broader set of challenges, featuring
high-dimensional action spaces and DoFs, resulting from
humanoid robots and dexterous hands, and a variety of long-
horizon tasks, which cover a comprehensive set of robotic
locomotion and manipulation skills, as summarized in Table I.
Finally, we note how in the literature, tasks that require
long-term planning with a high-dimensional action space
have been addressed with hierarchical reinforcement learning
(HRL), which decouples low-level and high-level planning in
a reinforcement learning paradigm [33, 4, 42, 29, 17, 30, 48].
v
v
x
x
x
x
x
x
x
v


<!-- page 3 (ocr) -->
Fig. 2: Example egocentric visual (top-left) and whole-body
tactile (right) observations when the humanoid interacts with
a package in the truck environment. In the right figure, the
two cameras on the robot head are highlighted in green, while
continuous tactile pressure readings are indicated in shades
of red (strong pressure) and yellow (mild pressure). Note that
for ease of visualization, we are not showing shear forces
and tactile readings on the back of the robot, which are also
implemented in our environment.
In the context of humanoids, we propose an HRL paradigm
to show how a specific set of low-level skills (e.g., standing,
walking) facilitates learning of higher-level tasks.
III. SIMULATED HUMANOID ROBOT ENVIRONMENT
In this section, we describe our simulated environment and
discuss relevant design choices for the simulated humanoid
robot. As illustrated in Figure 2, we use the Unitree H1
humanoid robot1 with two dexterous Shadow Hands2 as the
primary robotic agent of our benchmark. We simulate this
humanoid robot using MuJoCo [60] adapting the Unitree H1
model provided by Unitree5 and the dexterous Shadow Hand
models available through MuJoCo Menagerie.6
Humanoid Body.
We implement Unitree H11, Unitree G13,
and Agility Robotics Digit4, which are well-known humanoid
robots with their model files freely available [66, 1]. Unitree
H1 is primarily used in our benchmark as it is a full-size
humanoid compared to the smaller Unitree G1, and as we
observed faster learning compared to the Agility Robotics Digit,
which we ascribe to a simpler mechanical design compared to
Digit, which features passive joints actuated through a four-bar
linkage.
Dexterous Hands.
We use two dexterous Shadow Hands2,
which also have model files freely available6, and have shown
impressive manipulation capabilities both in simulation [67]
and in the real world [2]. To make the simulated robot have
more human-like morphology, we remove the cumbersome
5https://github.com/unitreerobotics/unitree ros
6https://github.com/google-deepmind/mujoco menagerie
Without hand
With 2 hands
Observation space
51
151
Action space
19
61
DoF (body)
25
25
DoF (two hands)
0
50
TABLE II: Humanoid robot specifications with and without
hands. Both the humanoid body (including its floating base)
and one Shadow Hand present action spaces (19 and 21,
respectively) smaller than their DoFs (25), making them under-
actuated systems. In this table, the observation spaces solely
comprise generalized positions and velocities of the robots and
do not take into account any environment observations. We
use quaternions for the robot floating base orientation, which
adds an additional position coordinate compared to the velocity
components, which match the DoFs. In the appendix, Table III
shows an exhaustive overview of all the robot configurations
available in HumanoidBench.
forearms of the dexterous Shadow Hands in HumanoidBench.
While this is not currently a realistic model, we anticipate the
trend in the industry towards developing slimmer, human-like
hands (e.g., Tesla Optimus, Figure 01) so that our design choice
aligns better with next-generation humanoid robots. In addition,
we also provide models for the Robotiq 2F-85 parallel-jaw
gripper and the 13-DoF Unitree hands available in the Unitree
collection5 (see Appendix, Section A for more details).
The observation and action spaces, and degrees of freedom
of the robot system with or without the dexterous hands are
summarized in Table II.
Observations.
Our simulated environment supports the
following observations:
• Proprioceptive robot state (i.e., joint angles and velocities)
and task-relevant environment observations (i.e., object
poses and velocities).
• Egocentric visual observations from two cameras placed
on the robot head (see Figure 2).
• Whole-body tactile sensing using the MuJoCo tactile grid
sensor (see Figure 2). We design tactile sensing at the
hands with high resolution and in other body parts with
low resolution, similar to humans, with a total of 448
taxels spread over the entire body, each providing three-
dimensional contact force readings. Similar distributed
force readings have been captured on real-world systems
both on humanoid bodies [41] and end-effectors [53]. The
implementation of such spatially distributed contact sens-
ing required non-trivial mesh adaptations and refinements,
which we detail in Appendix, Section B-D.
Although other sensory inputs are available from the envi-
ronment, to investigate challenges in whole-body control of
humanoid robots, we first focus on the state-based environment
setup, where proprioceptive robot states and object states are
used as the agent’s input in HumanoidBench. In our state-
based environment, we maintain the robot observations the
same across tasks to minimize domain knowledge, in contrast
to tailoring it to the specific tasks [59]. We leave extending
)
—
FEA ®
SB
-
To
1


<!-- page 4 (ocr) -->
push
cabinets
high_bar
door
truck
cubes
bookshelf
basketball
window
spoon
kitchen
package
powerlift
room
insert
Fig. 3: HumanoidBench manipulation task suite. We devise 15 benchmarking whole-body manipulation tasks that cover a
wide variety of interactions and difficulties. This figure illustrates an initial state for each task (left) and examples of the robot
performing such tasks (right).
our environment to benchmarking multimodal perception
capabilities [65, 54] of humanoid robots as future work.
Actions.
In HumanoidBench, the humanoid robot is con-
trolled via position control (i.e., specifying the target joint
positions). Torque-based control is also supported but we found
that position control is generally more stable and allows for
lower control frequency than torque control. For both position
and torque control, the action space is 61-dimensional including
the two hands, and controlled at 50 Hz.
IV. HUMANOIDBENCH
Humanoid robots promise to solve human-like tasks in
human-tailored environments, possibly using human tools.
However, their form factor and hardware challenges make
real-world research challenging, making simulation a crucial
tool to advance algorithmic research in the field.
To this end, we present HumanoidBench, a humanoid
benchmark for robot learning and control, which features a
SESE
Lr
A
BLL IER
“rR LIE
J, LRG of


<!-- page 5 (ocr) -->
walk
stand
run
reach
hurdle
crawl
maze
sit
balance
stairs
slides
pole
Fig. 4: HumanoidBench locomotion task suite. We devise 12 benchmarking locomotion tasks that cover a wide variety of
interactions and difficulties. This figure illustrates an initial state for each task (left) and examples of the robot performing such
tasks (right).
high-dimensional action space (up to 61 different actuators)
and enables research in complex whole-body coordination.
We benchmark 27 tasks, consisting of 12 locomotion tasks
and 15 distinct manipulation tasks, as illustrated in Figure 4
and Figure 3. A set of locomotion tasks aim to provide
interesting but simpler humanoid control scenarios, bypassing
intricate dexterous hand control. On the other hand, whole-
body manipulation tasks render a comprehensive evaluation
of the state-of-the-art algorithms on challenging tasks with
unique challenges that require coordination across the entire
robot body, ranging from toy examples (e.g., pushing a box on
a table) to practical applications (e.g., truck unloading, shelf
rearrangement).
In this section, we briefly describe the tasks in our benchmark
task suite. Further details about each of the tasks, including task
initialization, reward functions, as well as different variations
of the tasks, are provided in Appendix, Section B-E.
A. Locomotion Tasks
• walk: Keep forward velocity (in the global x-direction)
close to 1 m/s without falling to the ground.
• stand: Maintain a standing pose throughout the provided
amount of time.
• run: Run forward at a speed of 5 m/s.
• reach: Reach a randomly initialized 3D point with the
left hand.
• hurdle: Keep forward velocity close to 5 m/s while
successfully overcoming hurdles.
• crawl: Keep forward velocity close to 1 m/s while
passing inside a tunnel.
• maze: Reach the goal position in a maze by taking
multiple turns at the intersections.
• sit: Sit onto a chair situated closely behind the robot.
• balance: Stay balanced on the unstable board.
• stair: Traverse an iterating sequence of upward and
byob bf
rr BT
Qt
US


<!-- page 6 (ocr) -->
Dreamer3
PPO
SAC
TD-MPC2
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(a) walk
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(b) stand
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(c) run
0
2
4
6
8
10
Environment steps (×10⁶)
0
3500
7000
10500
14000
Return
(d) reach
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(e) hurdle
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(f) crawl
0
2
4
6
8
10
Environment steps (×10⁶)
0
375
750
1125
1500
Return
(g) maze
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(h) sit_simple
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(i) sit_hard
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(j) balance_simple
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(k) balance_hard
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(l) stair
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(m) slide
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(n) pole
Fig. 5: Learning curves of RL algorithms (locomotion). The curves are averaged over three random seeds and the shaded
regions represent the standard deviation. Returns are computed by summing the rewards at all timesteps of an episode. The
dashed lines qualitatively indicate task success. We run PPO on the walk task but it is not visible in the plot since it only
achieves very low returns.
downward stairs at 1 m/s.
• slide: Walk over an iterating sequence of upward and
downward slides at 1 m/s.
• pole: Travel in forward direction over a dense forest of
high thin poles, without colliding with them.
B. Whole-Body Manipulation Tasks
• push: Move a box to a randomly initialized 3D point on
a table.
• cabinet: Open four different types of cabinet doors
(e.g., hinge doors, sliding door, drawer).
• highbar: Athletically swing while staying attached to a
horizontal high bar until reaching a vertical upside-down
position.
• door: Pull a door and traverse it while keeping the door
open.
• truck: Unload packages from a truck by moving them
onto a platform.
• cube: Manipulate two cubes in-hand until they both reach
a randomly initialized target orientation.
• bookshelf: Pick and place several items across shelves
in a given order.
• basketball: Catch a ball coming from random direc-
tions and throw it into the basket.
• window: Grab a window wiping tool and keep its tip
parallel to a window by following a prescribed vertical
velocity.
• spoon: Grab a spoon and use it to follow a circular
pattern inside a pot.
• kitchen [17]: Execute a sequence of actions in a kitchen
environment, namely, open a microwave door, move a
kettle, and turning burner and light switches.
• package: Move a box to a randomly initialized target
position.
• powerlift: Lift a barbell shaped object of a designated
mass.


<!-- page 7 (ocr) -->
Dreamer3
PPO
SAC
TD-MPC2
0
2
4
6
8
10
Environment steps (×10⁶)
−600
−200
200
600
1000
Return
(a) push
0
2
4
6
8
10
Environment steps (×10⁶)
0
750
1500
2250
3000
Return
(b) cabinet
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(c) highbar
0
2
4
6
8
10
Environment steps (×10⁶)
0
200
400
600
800
Return
(d) door
0
2
4
6
8
10
Environment steps (×10⁶)
0
900
1800
2700
3600
Return
(e) truck
0
2
4
6
8
10
Environment steps (×10⁶)
0
125
250
375
500
Return
(f) cube
0
2
4
6
8
10
Environment steps (×10⁶)
0
625
1250
1875
2500
Return
(g) bookshelf_simple
0
2
4
6
8
10
Environment steps (×10⁶)
0
625
1250
1875
2500
Return
(h) bookshelf_hard
0
2
4
6
8
10
Environment steps (×10⁶)
0
375
750
1125
1500
Return
(i) basketball
0
2
4
6
8
10
Environment steps (×10⁶)
0
200
400
600
800
Return
(j) window
0
2
4
6
8
10
Environment steps (×10⁶)
0
200
400
600
800
Return
(k) spoon
0
2
4
6
8
10
Environment steps (×10⁶)
0
1
2
3
4
5
Return
(l) kitchen
0
2
4
6
8
10
Environment steps (×10⁶)
−12000
−8500
−5000
−1500
2000
Return
(m) package
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(n) powerlift
0
2
4
6
8
10
Environment steps (×10⁶)
0
150
300
450
600
Return
(o) room
0
2
4
6
8
10
Environment steps (×10⁶)
0
125
250
375
500
Return
(p) insert_small
0
2
4
6
8
10
Environment steps (×10⁶)
0
125
250
375
500
Return
(q) insert_normal
Fig. 6: Learning curves of RL algorithms (manipulation). The curves are averaged over three random seeds and the shaded
regions represent the standard deviation. The dashed lines qualitatively indicate task success. Note that kitchen is the only
environment with a purely discrete, sparse reward, with a maximum of 4.
• room: Organize a 5 m by 5 m space populated with
randomly scattered object to minimize the variance of
scattered objects’ locations in x, y-axis directions.
• insert: Insert the ends of a rectangular peg into two
tight target blocks.
V. BENCHMARKING RESULTS
To identify the challenges in learning with humanoid robots,
we benchmark reinforcement learning (RL) algorithms on
HumanoidBench, which promises for robots to learn from
their own experience. Remarkably, this class of algorithms
requires limited domain expertise and does not necessarily rely
on expert demonstrations, which are not only expensive but
also challenging to collect for humanoid robots.7
A. Baselines
We evaluate all tasks in our benchmark with four RL methods
(DreamerV3, TD-MPC2, SAC, PPO). Please refer to Appendix,
Section C for implementation details.
7While we do not benchmark classical model-based control approaches
[14, 26] in this work, our environments support actions obtained by using any
type of controllers.
=
—
—
—
7]
Ed
Ed
=
ni ilIR
PA=v


<!-- page 8 (ocr) -->
• DreamerV3 [20]: the state-of-the-art model-based RL
algorithm, learning from imaginary model rollouts.
• TD-MPC2 [21]: the state-of-the-art model-based RL
algorithm with online planning.
• SAC (Soft Actor-Critic [18]): the state-of-the-art off-policy
model-free RL algorithm.
• PPO (Proximal Policy Optimization [52]): the state-of-
the-art on-policy model-free RL algorithm.
B. Results
We report benchmarking results in Figure 5 and Figure 6,
where we ran each of the algorithms for approximately 48
hours, resulting in the visible differences in environment steps
(e.g., 2M steps for TD-MPC2, 10M steps for DreamerV3). We
only run PPO on a subset of tasks (walk, kitchen, door,
package), given its inferior performance without massive
parallelization. Each of the environments is evaluated with a
combination of dense rewards and sparse subtask completion
rewards, and for each of these we provide qualitative measures
of task success (see dashed lines in Figure 5 and Figure 6).
A detailed description of the reward functions used for each
environment is available in Appendix, Section B-E.
All the baseline algorithms perform below the success
threshold on most tasks, particularly struggling on tasks
that require long-horizon planning and intricate whole-body
coordination in a high-dimensional action space. Surprisingly,
these state-of-the-art RL algorithms require a large number of
steps to learn even simple locomotion tasks, such as walk,
which has been extensively studied with a simplified humanoid
agent in the DeepMind Control Suite [59].
This poor performance is mainly attributed to the high-
dimensionality of the state and action spaces of our humanoid
robot agent with dexterous hands. Although the hands of the
humanoid robot are barely used for most locomotion tasks, the
RL algorithms fail to ignore this information, which makes
policy learning challenging. In addition, these high-dimensional
state and action spaces result in a much larger exploration
space, which makes exploration slow or infeasible with simple
maximum entropy approaches. This implies the need for
incorporating behavioral priors or commonsense knowledge
about the world that can ease the exploration problem, when
it comes to learning on more complex agents, like humanoid
robots. We investigate this further in Section V-C.
This problem becomes even more severe in manipulation
tasks, resulting in particularly low rewards in all such tasks.
Before learning any manipulation skills, an agent must learn
locomotion skills to balance and move towards an object or
the world to interact. All the policies barely learn to stabilize
using the dense reward, but struggle to learn any complex
manipulation skills.
C. With Hands vs. Alternative Configurations
With Hands vs. Without Hands.
As discussed in Sec-
tion V-B, controlling humanoid robots with dexterous hands
is challenging due to their high degrees of freedom and
complex dynamics. Thus, we investigate the difficulty of RL
DreamerV3
TD-MPC2
DreamerV3 w/o Hands
TD-MPC2 w/o Hands
DreamerV3 - Reduced Action Space
TD-MPC2 - Reduced Action Space
0
2
4
6
8
10
Environment steps (×10⁶)
0
250
500
750
1000
Return
(a) walk
0
2
4
6
8
10
Environment steps (×10⁶)
−600
−200
200
600
1000
Return
(b) push
Fig. 7: Performance with and without dexterous hands. The
curves are averaged over three random seeds and the shaded
regions represent the standard deviation.
training with a large action space (i.e., additional 42 dimensions
with two dexterous Shadow Hands) on walk that does not
necessarily require to control dexterous hands. The results in
Figure 7 show that the presence of hands, with their additional
joints and actuators, leads to a large decrease in performance
compared to training the same task without the dexterous hands
(see differences in observation and action space in Table II).
Reduced Action Space.
To verify whether such difficulties
stem from the dimensionality of the action space, we benchmark
our full robot model, but fix the actuation of the hands (42D),
which we set to zero. In this way, the action dimensionality is
reduced from 61D in the original model to 19D. Note that the
observations and masses induced by the presence of the hands
are retained (i.e., observation space remains 151D). Figure 7
shows that the RL algorithms learn significantly faster in the
reduced action space setup than the ones trained with the full
action space. This confirms that most of the performance drop
is indeed due to the increased action dimensionality.
We observe similar trends in the more complex manipulation
task, push, which presents substantially different dynamics in
the task approach (e.g., pushing with and without hands).
D. Flat vs. Hierarchical Reinforcement Learning
As shown in the previous subsection, flat, end-to-end RL
approaches fail to learn most of the tasks in HumanoidBench.
Many of such tasks require long-horizon planning and necessi-
tate acquiring a diverse set of skills (e.g., balancing, walking,
reaching). These tasks can be addressed by hierarchical RL,
which introduces additional structure into the learning problem.
In HRL, one or multiple low-level skill policies are provided
to a high-level planning policy that outputs setpoints for the
lower-level policies. In practice, such setpoints comprise the
action space of the high-level policy. This framework is very
general, and there are no constraints on how to obtain both
low-level and high-level policies. However, here we focus on
training both of these through reinforcement learning [56].
Hierarchical RL Implementation.
We implement a hier-
archical RL approach on two manipulation tasks, namely, the
push and package tasks. As a low-level skill, push uses a
one-hand reaching policy, which allows the robot to reach a
3D point in space with its left hand, while package uses a
two-hand reaching policy, where both hands are commanded
aH
fi
y
f°
Nr
1;
>


<!-- page 9 (ocr) -->
(a) Hierarchical learning pipeline
(b) Low-level policy pretraining
(c) High-level policy training
Fig. 8: Our hierarchical RL pipeline (a). (b) A robust low-level reaching policy is pretrained using PPO in a MuJoCo
MJX-based reaching environment, as shown in the top snapshot in (a). (c) The high-level policy then leverages the pretrained
reaching policy to move to a desired position and learns to solve a downstream task, shown in the bottom snapshot in (a). Note
that the reaching policy weights are frozen during the high-level policy training.
to reach different 3D targets. Figure 8 illustrates the overview
of our hierarchical RL implementation.
Low-level Reaching Policy Pretraining.
We treat the low-
level reaching policy as a pretrained frozen block that can be
reused across tasks. Since this policy does not improve during
training of the high-level policy, it needs to be very robust
to cope with the continually shifting reaching targets that the
high-level policy sets during exploration. However, the results
in the previous section show that even a one-hand reaching
task is hard to learn.
On the other hand, while our experiments above confirm
that PPO exhibits poor sample efficiency compared to the off-
policy algorithms, it is worth noting that PPO has achieved
significant success in robotic locomotion by exploiting large-
scale parallelization of environments on GPUs [36]. To achieve
robust reaching policies, we exploit hardware acceleration
by pretraining the low-level reaching policies in the recently
released MuJoCo MJX8, which enables training PPO on
thousands of parallel environments.
For low-level reaching policy training, we employ a sim-
plified H1 model that only considers collisions between feet
and ground in the MuJoCo MJX environments, as in our
experience the advantages stemming from parallelization are
largely reduced when considering all numerous humanoid
geometries (hindering training of the more complex benchmark
tasks via MJX). We also remove the hands from the model
to further increase training efficiency. The simplified reaching
task environments for pretraining reset the target once reached.
To achieve robust low-level reaching policies, we apply force
perturbations at each of the links during training. We train the
one-hand reaching policy for 2 billion steps (36 hours) and
the two-hand reaching policy for 4 billion steps (60 hours) on
32,768 parallel environments. The pretrained reaching policies
successfully transfer to the original (non-simplified, simulated
in classical MuJoCo) humanoid environments.
High-level Policy Training.
Then, we use the pretrained
reaching policies (frozen) as low-level policies and only train
a high-level policy using either DreamerV3 and TD-MPC2 on
8https://mujoco.readthedocs.io/en/stable/mjx.html
DreamerV3 (flat)
DreamerV3 (hierarchical)
TD-MPC2 (flat)
TD-MPC2 (hierarchical)
0
2
4
6
8
10
Environment steps (×10⁶)
−600
−200
200
600
1000
Return
(a) push
0
2
4
6
8
10
Environment steps (×10⁶)
−12000
−8500
−5000
−1500
2000
Return
(b) package
Fig. 9: Comparison between flat policies and hierarchical
policies. The curves are averaged over three random seeds and
the shaded regions represent the standard deviation.
the push and package tasks. To facilitate exploration, we
restrict the range of reaching targets to the robot workspace.
Hierarchical RL Results.
In Figure 9, our hierarchical
architecture significantly outperforms the flat, end-to-end
baselines on the push task, achieving very high success rates
with DreamerV3. While the low-level policy has undergone
additional pretraining, this can be in principle reused across
tasks. On the other hand, we note a less pronounced per-
formance improvement in the more challenging package
task. While getting closer to picking up the package with our
hierarchical approach, the policy struggles in lifting it (having
never experienced it during training).
These results confirm that the tasks in our benchmark
present challenges that can be addressed with a more structured
approach to the learning problem, and we hope this stimulates
further directions for future research.
E. Common Failures
In this subsection, we remark on notable challenges and com-
mon failures for some representative tasks in our benchmark,
which denote the challenge in learning with high-dimensional
action spaces and limited planning horizon of the state-of-the-
art RL algorithms.
Common Failure on highbar. In the highbar task, the
Unitree H1 robot conservatively learns to maintain contact
with the bar to avoid episode termination, but experiences
Pretrain low-level policy (in MJX)
Sample new
High-level Policy
target
Reaching
target:
Reaching
targets
9
targets
Yes
Gre hand50)
+ One hand BOI
+
Two hands (6D)
* Two hands (40)
Freeze low-level policy
Reaching F] Joint actions 6101
Reaching | Joint actions 410)
Ze
:
Learn high-level policy
Robot state |Environment
LEE
Environment
(MJX)


<!-- page 10 (ocr) -->
(a) highbar
(b) door
(c) hurdle
Fig. 10: Failure Scenarios. This figure presents a selection
of common failures that occur while training our benchmark
tasks.
difficulties in performing the whole-body rotation trajectory.
This is indicative of short horizon planning and a recurrent
challenge in many of the long-horizon benchmark tasks, despite
the availability of dense rewards.
Common Failure on door. In the door task, the robot
is well-guided to turn the door hatch to unlock the door, but
it finds it challenging to learn the precise motion required
to pull the door towards its opening position. This is mainly
because pulling the door requires not only pulling its arm
but also moving the whole body backwards. The coordination
between multiple body parts and seamless interaction between
manipulation and locomotion skills are common challenges in
training humanoid robots.
Common Failure on hurdle. In the hurdle environment,
the robot learns to run forward with the expected velocity but
does not recognize the need to surpass the hurdle by jumping,
which is a hard exploration problem. Previous work has shown
that in OpenAI gym Walker2d, the forward-moving reward
is sufficient to learn this behavior [29]. On the other hand,
the humanoid robot finds conservative poses to collide with
the hurdle such that it can stabilize without terminating the
episode after hitting the obstacle, without further exploring
high-reward jumping behaviors.
VI. CONCLUSION
We presented HumanoidBench, a high-dimensional hu-
manoid robot control benchmark. Ours is the first example of
a comprehensive humanoid environment with a diversity of
locomotion and manipulation tasks, ranging from toy examples
to practical humanoid applications. We set a high bar with
our complex tasks, in the hope to stimulate the community to
accelerate the development of whole-body algorithms for such
robotic platforms.
Future work.
HumanoidBench already includes multi-
modal high-dimensional observations in the form of egocentric
vision and whole-body tactile sensing. While our experiments
only benchmarked the performance of state-based environ-
ments, studying the interplay between different modalities is a
compelling direction for future work.
Extensions of the humanoid environment will also eventually
include more realistic objects and environments with real-world
diversity and higher-quality rendering. As for dexterous manipu-
lation tasks, we envision screwing and furniture assembly tasks
being part of our framework, given that they are particularly
tailored for bimanual manipulation.
Here we have focused on reinforcement learning algorithms
because collecting physical demonstrations with humanoid
robots is particularly challenging. However, we believe that
other means could be employed to bootstrap learning (e.g.,
learning from human videos).
Finally, while this was not the focus of our work, the
impressive results obtained via domain randomization in the
newly developed MuJoCo MJX show promise to study sim-to-
real transfer in more depth, following the large success of the
field in quadrupedal locomotion [23].
ACKNOWLEDGMENTS
This work was supported in part by the SNSF Postdoc
Mobility Fellowship 211086, ONR MURI N00014-22-1-2773,
BAIR Industrial Consortium, Komatsu, InnoHK Centre for
Logistics Robotics, an ONR DURIP grant, the Institute
of Information & Communications Technology Planning &
Evaluation (IITP) grant and the National Research Foundation
of Korea (NRF) grant funded by the Korean government (MSIT)
(RS-2020-II201361, Artificial Intelligence Graduate School
Program (Yonsei University) and RS-2024-00333634). We also
thank Google TPU Research Cloud (TRC) for granting us
access to TPUs for research.
REFERENCES
[1] Alphonsus Adu-Bredu, Grant Gibson, and Jessy Grizzle.
Exploring kinodynamic fabrics for reactive whole-body
control of underactuated humanoid robots. In IEEE/RSJ
International Conference on Intelligent Robots and Sys-
tems, pages 10397–10404. IEEE, 2023.
[2] Ilge Akkaya, Marcin Andrychowicz, Maciek Chociej,
Mateusz Litwin, Bob McGrew, Arthur Petron, Alex Paino,
Matthias Plappert, Glenn Powell, Raphael Ribas, et al.
Solving rubik’s cube with a robot hand. arXiv preprint
arXiv:1910.07113, 2019.
[3] Firas Al-Hafez, Guoping Zhao, Jan Peters, and Davide
Tateo. Locomujoco: A comprehensive imitation learning
benchmark for locomotion. 6th Robot Learning Workshop
at NeurIPS, 2023.
[4] Pierre-Luc Bacon, Jean Harb, and Doina Precup. The
option-critic architecture. In Association for the Advance-
ment of Artificial Intelligence, pages 1726–1734, 2017.
[5] M. G. Bellemare, Y. Naddaf, J. Veness, and M. Bowling.
The arcade learning environment: An evaluation platform
for general agents.
Journal of Artificial Intelligence
Research, 47:253–279, jun 2013.
[6] Cameron H Berg, Vittorio Caggiano, and Vikash Kumar.
SAR: Generalization of Physiological Dexterity via Syn-
ergistic Action Representation. In Robotics: Science and
Systems, 2023.
[7] Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas
Schneider, John Schulman, Jie Tang, and Wojciech
Zaremba. Openai gym. arXiv preprint arXiv:1606.01540,
2016.


<!-- page 11 (ocr) -->
[8] Vittorio Caggiano, Huawei Wang, Guillaume Durandau,
Massimo Sartori, and Vikash Kumar. Myosuite: A contact-
rich simulation suite for musculoskeletal motor control.
In Learning for Dynamics and Control, pages 492–507.
PMLR, 2022.
[9] Vittorio Caggiano, Sudeep Dasari, and Vikash Kumar.
Myodex: a generalizable prior for dexterous manipulation.
In International Conference on Machine Learning, pages
3327–3346. PMLR, 2023.
[10] Yuanpei Chen, Yiran Geng, Fangwei Zhong, Jiaming Ji,
Jiechuang Jiang, Zongqing Lu, Hao Dong, and Yaodong
Yang.
Bi-dexhands: Towards human-level bimanual
dexterous manipulation. IEEE Transactions on Pattern
Analysis and Machine Intelligence, 2023.
[11] Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang,
Ge Yang, and Xiaolong Wang.
Expressive whole-
body control for humanoid robots.
arXiv preprint
arXiv:2402.16796, 2024.
[12] Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric
Cousineau, Benjamin Burchfiel, and Shuran Song. Dif-
fusion policy: Visuomotor policy learning via action
diffusion. In Robotics: Science and Systems, 2023.
[13] Yan Duan, Marcin Andrychowicz, Bradly Stadie, Jonathan
Ho, Jonas Schneider, Ilya Sutskever, Pieter Abbeel, and
Wojciech Zaremba.
One-shot imitation learning.
In
Advances in Neural Information Processing Systems,
pages 1087–1098, 2017.
[14] Siyuan Feng, Eric Whitman, X Xinjilefu, and Christo-
pher G Atkeson. Optimization based full body control
for the atlas robot.
In 2014 IEEE-RAS International
Conference on Humanoid Robots, pages 120–127. IEEE,
2014.
[15] Zipeng Fu, Tony Z Zhao, and Chelsea Finn. Mobile
aloha: Learning bimanual mobile manipulation with
low-cost whole-body teleoperation.
arXiv preprint
arXiv:2401.02117, 2024.
[16] Dibya Ghosh. dibyaghosh/jaxrl m, 2023. URL https:
//github.com/dibyaghosh/jaxrl m.
[17] Abhishek Gupta, Vikash Kumar, Corey Lynch, Sergey
Levine, and Karol Hausman. Relay policy learning: Solv-
ing long-horizon tasks via imitation and reinforcement
learning. Conference on Robot Learning, 2019.
[18] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey
Levine. Soft actor-critic: Off-policy maximum entropy
deep reinforcement learning with a stochastic actor. In
International Conference on Machine Learning, pages
1856–1865, 2018.
[19] Tuomas Haarnoja, Ben Moran, Guy Lever, Sandy H
Huang, Dhruva Tirumala, Markus Wulfmeier, Jan Hump-
lik, Saran Tunyasuvunakool, Noah Y Siegel, Roland
Hafner, Michael Bloesch, Kristian Hartikainen, Arunk-
umar Byravan, Leonard Hasenclever, Yuval Tassa,
Fereshteh Sadeghi, Nathan Batchelor, Federico Casarini,
Stefano Saliceti, Charles Game, Neil Sreendra, Kushal
Patel, Marlon Gwira, Andrea Huber, Nicole Hurley,
Francesco Nori, Raia Hadsell, and Nicolas Heess. Learn-
ing agile soccer skills for a bipedal robot with deep
reinforcement learning. arXiv preprint arXiv:2304.13653,
2023.
[20] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy
Lillicrap.
Mastering diverse domains through world
models. arXiv preprint arXiv:2301.04104, 2023.
[21] Nicklas Hansen, Hao Su, and Xiaolong Wang. Td-mpc2:
Scalable, robust world models for continuous control. In
International Conference on Learning Representations,
2024.
[22] Minho Heo, Youngwoon Lee, Doohyun Lee, and Joseph J.
Lim. Furniturebench: Reproducible real-world benchmark
for long-horizon complex manipulation.
In Robotics:
Science and Systems, 2023.
[23] Jemin Hwangbo, Joonho Lee, Alexey Dosovitskiy, Dario
Bellicoso, Vassilios Tsounis, Vladlen Koltun, and Marco
Hutter.
Learning agile and dynamic motor skills for
legged robots. Science Robotics, 4(26):eaau5872, 2019.
[24] Stephen James, Zicong Ma, David Rovick Arrojo, and An-
drew J. Davison. Rlbench: The robot learning benchmark
& learning environment. IEEE Robotics and Automation
Letters, 2020.
[25] Harini Kannan, Danijar Hafner, Chelsea Finn, and Du-
mitru Erhan.
Robodesk: A multi-task reinforcement
learning benchmark. https://github.com/google-research/
robodesk, 2021.
[26] Scott Kuindersma, Robin Deits, Maurice Fallon, Andr´es
Valenzuela, Hongkai Dai, Frank Permenter, Twan Koolen,
Pat Marion, and Russ Tedrake.
Optimization-based
locomotion planning, estimation, and control design for
the atlas humanoid robot. Autonomous robots, 40:429–
455, 2016.
[27] Ashish Kumar, Zipeng Fu, Deepak Pathak, and Jitendra
Malik. Rma: Rapid motor adaptation for legged robots.
In Robotics: Science and Systems, 2021.
[28] Seunghwan Lee, Moonseok Park, Kyoungmin Lee, and
Jehee Lee. Scalable muscle-actuated human simulation
and control. ACM Transactions on Graphics, 38(4):1–13,
2019.
[29] Youngwoon Lee, Shao-Hua Sun, Sriram Somasundaram,
Edward S. Hu, and Joseph J. Lim. Composing complex
skills by learning transition policies. In International
Conference on Learning Representations, 2019. URL
https://openreview.net/forum?id=rygrBhC5tQ.
[30] Youngwoon Lee, Jingyun Yang, and Joseph J. Lim.
Learning to coordinate manipulation skills via skill
behavior diversification. In International Conference on
Learning Representations, 2020.
[31] Youngwoon Lee, Edward S Hu, and Joseph J Lim. IKEA
furniture assembly environment for long-horizon complex
manipulation tasks. In IEEE International Conference on
Robotics and Automation, 2021. URL https://clvrai.com/
furniture.
[32] Chengshu Li, Ruohan Zhang, Josiah Wong, Cem Gok-
men, Sanjana Srivastava, Roberto Mart´ın-Mart´ın, Chen
Wang, Gabrael Levine, Michael Lingelbach, Jiankai


<!-- page 12 (ocr) -->
Sun, Mona Anvari, Minjune Hwang, Manasi Sharma,
Arman Aydin, Dhruva Bansal, Samuel Hunter, Kyu-Young
Kim, Alan Lou, Caleb R Matthews, Ivan Villa-Renteria,
Jerry Huayang Tang, Claire Tang, Fei Xia, Silvio Savarese,
Hyowon Gweon, Karen Liu, Jiajun Wu, and Li Fei-Fei.
Behavior-1k: A benchmark for embodied ai with 1,000
everyday activities and realistic simulation. In Conference
on Robot Learning, 2022.
[33] L-J Lin. Hierarchical learning of robot skills by rein-
forcement. In IEEE International Conference on Neural
Networks, pages 181–186. IEEE, 1993.
[34] Xingyu Lin, Yufei Wang, Jake Olkin, and David Held.
Softgym: Benchmarking deep reinforcement learning for
deformable object manipulation. In Conference on Robot
Learning, 2020.
[35] Chris Lu, Jakub Kuba, Alistair Letcher, Luke Metz, Chris-
tian Schroeder de Witt, and Jakob Foerster. Discovered
policy optimisation.
Advances in Neural Information
Processing Systems, 35:16455–16468, 2022.
[36] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo,
Michelle Lu, Kier Storey, Miles Macklin, David Hoeller,
Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel
State. Isaac gym: High performance gpu based physics
simulation for robot learning.
In Neural Information
Processing Systems Datasets and Benchmarks Track,
2021.
[37] Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush
Nasiriany, Chen Wang, Rohun Kulkarni, Li Fei-Fei, Silvio
Savarese, Yuke Zhu, and Roberto Mart´ın-Mart´ın. What
matters in learning from offline human demonstrations
for robot manipulation. In Conference on Robot Learning,
2021.
[38] Dominik Mattern, Pierre Schumacher, Francisco M L´opez,
Marcel C Raabe, Markus R Ernst, Arthur Aubret, and
Jochen Triesch. Mimo: A multi-modal infant model for
studying cognitive development. IEEE Transactions on
Cognitive and Developmental Systems, 2024.
[39] Oier Mees, Lukas Hermann, Erick Rosete-Beas, and
Wolfram Burgard. Calvin: A benchmark for language-
conditioned policy learning for long-horizon robot ma-
nipulation tasks. IEEE Robotics and Automation Letters,
2022.
[40] Josh Merel, Saran Tunyasuvunakool, Arun Ahuja, Yuval
Tassa, Leonard Hasenclever, Vu Pham, Tom Erez, Greg
Wayne, and Nicolas Heess.
Catch & carry: reusable
neural controllers for vision-guided whole-body tasks.
ACM Transactions on Graphics, 39(4):39–1, 2020.
[41] Philipp Mittendorfer and Gordon Cheng.
Humanoid
multimodal tactile-sensing modules. IEEE Transactions
on robotics, 27(3):401–410, 2011.
[42] Ofir Nachum, Shixiang Shane Gu, Honglak Lee, and
Sergey Levine. Data-efficient hierarchical reinforcement
learning. In Advances in Neural Information Processing
Systems, pages 3303–3313, 2018.
[43] Yashraj Narang, Kier Storey, Iretiayo Akinola, Miles
Macklin, Philipp Reist, Lukasz Wawrzyniak, Yunrong
Guo, Adam Moravanszky, Gavriel State, Michelle Lu,
Ankur Handa, and Dieter Fox. Factory: Fast contact for
robotic assembly. In Robotics: Science and Systems, 2022.
[44] OpenAI, Marcin Andrychowicz, Bowen Baker, Maciek
Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki,
Arthur Petron, Matthias Plappert, Glenn Powell, Alex
Ray, Jonas Schneider, Szymon Sidor, Josh Tobin, Peter
Welinder, Lilian Weng, and Wojciech Zaremba. Learn-
ing dexterous in-hand manipulation. The International
Journal of Robotics Research, 39(1):3–20, 2020.
[45] Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel
Van de Panne. Deepmimic: Example-guided deep rein-
forcement learning of physics-based character skills. ACM
Transactions on Graphics, 37(4):1–14, 2018.
[46] Xue Bin Peng, Angjoo Kanazawa, Jitendra Malik, Pieter
Abbeel, and Sergey Levine. Sfv: Reinforcement learning
of physical skills from videos. ACM Transactions on
Graphics, 37(6):1–14, 2018.
[47] Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine,
and Angjoo Kanazawa. Amp: Adversarial motion priors
for stylized physics-based character control.
ACM
Transactions on Graphics, 40(4):1–20, 2021.
[48] Karl Pertsch, Youngwoon Lee, and Joseph J. Lim. Accel-
erating reinforcement learning with learned skill priors.
In Conference on Robot Learning, 2020.
[49] Matthias Plappert, Marcin Andrychowicz, Alex Ray, Bob
McGrew, Bowen Baker, Glenn Powell, Jonas Schneider,
Josh Tobin, Maciek Chociej, Peter Welinder, Vikash
Kumar, and Wojciech Zaremba. Multi-goal reinforcement
learning: Challenging robotics environments and request
for research. arXiv preprint arXiv:1802.09464, 2018.
[50] Ilija Radosavovic, Tete Xiao, Bike Zhang, Trevor Dar-
rell, Jitendra Malik, and Koushil Sreenath.
Learning
humanoid locomotion with transformers. arXiv preprint
arXiv:2303.03381, 2023.
[51] Antonin Raffin, Ashley Hill, Maximilian Ernestus, Adam
Gleave, Anssi Kanervisto, and Noah Dormann. Stable
baselines3, 2019.
[52] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec
Radford, and Oleg Klimov. Proximal policy optimization
algorithms. arXiv preprint arXiv:1707.06347, 2017.
[53] Carmelo Sferrazza and Raffaello D’Andrea. Sim-to-real
for high-resolution optical tactile sensing: From images
to three-dimensional contact force distributions.
Soft
Robotics, 9(5):926–937, 2022.
[54] Carmelo Sferrazza, Younggyo Seo, Hao Liu, Young-
woon Lee, and Pieter Abbeel.
The power of the
senses: Generalizable manipulation from vision and touch
through masked multimodal learning.
arXiv preprint
arXiv:2311.00924, 2023.
[55] Sanjana Srivastava, Chengshu Li, Michael Lingelbach,
Roberto Mart´ın-Mart´ın, Fei Xia, Kent Elliott Vainio,
Zheng Lian, Cem Gokmen, Shyamal Buch, Karen Liu, Sil-
vio Savarese, Hyowon Gweon, Jiajun Wu, and Li Fei-Fei.
Behavior: Benchmark for everyday household activities
in virtual, interactive, and ecological environments. In


<!-- page 13 (ocr) -->
Conference on Robot Learning, 2021.
[56] Richard S Sutton, Doina Precup, and Satinder Singh.
Between mdps and semi-mdps: A framework for tem-
poral abstraction in reinforcement learning.
Artificial
intelligence, 112(1-2):181–211, 1999.
[57] Andrew Szot, Alex Clegg, Eric Undersander, Erik Wij-
mans, Yili Zhao, John Turner, Noah Maestre, Mustafa
Mukadam, Devendra Chaplot, Oleksandr Maksymets,
Aaron Gokaslan, Vladimir Vondrus, Sameer Dharur,
Franziska Meier, Wojciech Galuba, Angel Chang, Zsolt
Kira, Vladlen Koltun, Jitendra Malik, Manolis Savva, and
Dhruv Batra. Habitat 2.0: Training home assistants to
rearrange their habitat. In Neural Information Processing
Systems, 2021.
[58] Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez,
Yazhe Li, Diego de Las Casas, David Budden, Abbas
Abdolmaleki, Josh Merel, Andrew Lefrancq, Timothy P.
Lillicrap, and Martin A. Riedmiller. Deepmind control
suite. arXiv preprint arXiv:1801.00690, 2018.
[59] Yuval Tassa, Saran Tunyasuvunakool, Alistair Muldal,
Yotam Doron, Siqi Liu, Steven Bohez, Josh Merel, Tom
Erez, Timothy Lillicrap, and Nicolas Heess. dm control:
Software and tasks for continuous control. arXiv preprint
arXiv:2006.12983, 2020.
[60] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A
physics engine for model-based control. In IEEE/RSJ In-
ternational Conference on Intelligent Robots and Systems,
pages 5026–5033, 2012.
[61] Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian
Zhang, and Lei Zhang. Physhoi: Physics-based imitation
of dynamic human-object interaction.
arXiv preprint
arXiv:2312.04393, 2023.
[62] Xinyue Wei, Minghua Liu, Zhan Ling, and Hao Su.
Approximate convex decomposition for 3d meshes with
collision-aware concavity and tree search. ACM Transac-
tions on Graphics (TOG), 41(4):1–18, 2022.
[63] Zhaoming Xie, Jonathan Tseng, Sebastian Starke, Michiel
van de Panne, and C Karen Liu. Hierarchical planning
and control for box loco-manipulation. Symposium on
Computer Animation, 2023.
[64] Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian,
Karol Hausman, Chelsea Finn, and Sergey Levine. Meta-
world: A benchmark and evaluation for multi-task and
meta reinforcement learning. In Conference on Robot
Learning, 2019.
[65] Ying Yuan, Haichuan Che, Yuzhe Qin, Binghao Huang,
Zhao-Heng Yin, Kang-Won Lee, Yi Wu, Soo-Chul
Lim, and Xiaolong Wang. Robot synesthesia: In-hand
manipulation with visuotactile sensing. arXiv preprint
arXiv:2312.01853, 2023.
[66] Kevin Zakka, Yuval Tassa, and MuJoCo Menagerie
Contributors. MuJoCo Menagerie: A collection of high-
quality simulation models for MuJoCo, 2022.
URL
http://github.com/google-deepmind/mujoco menagerie.
[67] Kevin Zakka, Philipp Wu, Laura Smith, Nimrod Gileadi,
Taylor Howell, Xue Bin Peng, Sumeet Singh, Yuval Tassa,
Pete Florence, Andy Zeng, and Pieter Abbeel. Robopi-
anist: Dexterous piano playing with deep reinforcement
learning. In Conference on Robot Learning, pages 2975–
2994. PMLR, 2023.
[68] Haotian Zhang, Ye Yuan, Viktor Makoviychuk, Yunrong
Guo, Sanja Fidler, Xue Bin Peng, and Kayvon Fatahalian.
Learning physically simulated tennis skills from broadcast
videos. ACM Transactions on Graphics, 42(4):1–14, 2023.
[69] Tony Z Zhao, Vikash Kumar, Sergey Levine, and Chelsea
Finn. Learning fine-grained bimanual manipulation with
low-cost hardware. In Robotics: Science and Systems,
2023.
[70] Yuke Zhu, Josiah Wong, Ajay Mandlekar, and Roberto
Mart´ın-Mart´ın. robosuite: A modular simulation frame-
work and benchmark for robot learning. arXiv preprint
arXiv:2009.12293, 2020.
[71] Ziwen Zhuang, Zipeng Fu, Jianren Wang, Christopher G
Atkeson, S¨oren Schwertfeger, Chelsea Finn, and Hang
Zhao. Robot parkour learning. In Conference on Robot
Learning, 2023.


<!-- page 14 (ocr) -->
(a) Digit w/ Shadow Hands
(b) Unitree G1
(c) H1 w/ Robotiq grippers
(d) H1 w/ Unitree hands
Fig. 11: Additional configurations available in HumanoidBench.
Appendix
Table of Contents
Appendix A: Additional Components
14
Appendix B: Simulated Environment Details
14
B-A
Observation Space . . . . . . . . . . . .
14
B-B
Action Space . . . . . . . . . . . . . . .
14
B-C
Simulation Performance . . . . . . . . .
14
B-D
Whole-body Tactile Sensing
. . . . . .
14
B-E
Task Specification . . . . . . . . . . . .
14
Appendix C: Training Details
24
C-A
Baseline Implementation Details . . . .
24
C-B
Reaching Policy Implementation Details
24
C-C
Benchmarking Results . . . . . . . . . .
24
APPENDIX A
ADDITIONAL COMPONENTS
In addition to the Unitree H1 robot, we also include model
files for the Agility Robotics Digit humanoid (see Figure 11).
We add a custom head, together with egocentric vision and
whole-body tactile sensing, similarly to the H1. We provide a
torque controlled version of this robot. We also provide a torque
controlled version of the more recent Unitree G1 humanoid.
For the broader use of HumanoidBench, we also provide
two simple end-effector options for the Unitree H1 robot: a
2-DoF Robotiq 2F-45 parallel-jaw gripper (with a rotational
wrist joint), and a 13-DoF dexterous Unitree hand available in
the Unitree model collection.5
Specifications for all these variants are detailed in Table III.
APPENDIX B
SIMULATED ENVIRONMENT DETAILS
A. Observation Space
The observation space for the benchmarked H1 robot state
(joint positions and velocities) comprises 151 dimensions, with
51 dimensions representing the humanoid robot body and
50 dimensions representing each hand. Table III summarizes
observation spaces for other robotic configurations supported
in HumanoidBench. The observation space can also include
environment states for tasks interacting with objects, as
described in detail in Section B-E.
B. Action Space
The action space is the same across all environments. We
normalize the action space to be [−1, 1]∥A∥, where ∥A∥= 61
(19 for the humanoid body and 21 for each hand). We use
position control for the benchmarking results in this paper.
C. Simulation Performance
HumanoidBench is based on MuJoCo [60], which provides
fast and accurate physics simulation. We provide a diverse set
of configurations, such as the full humanoid model with two
hands, the humanoid model without hands, and the humanoid
model with collision meshes only on its feet. We use the fastest
model (i.e., collision meshes only on feet) to train the low-level
reaching policies, described in Section C-B.
We benchmark our HumanoidBench simulation using the
Unitree H1 model and report its performance in Table IV.
Even with complex humanoid body and dexterous hands,
HumanoidBench can run 1000+ FPS on a single CPU with a
simulation timestep of 0.002 s.
D. Whole-body Tactile Sensing
We implement whole-body tactile sensing by employing
MuJoCo touch grid, which aggregates pressure and shear
contact forces into discrete bins. Similar distributed force
readings have been captured on real-world systems both on
humanoid bodies [41] and end-effectors [53]. To increase
the number of contact point candidates and fully exploit the
spatial resolution of the touch grid, we subdivide the original
meshes into many smaller meshes. Specifically, we build on
top of CoACD [62], which in addition makes sure that the
resulting meshes are all convex. This procedure results in finer
contact resolution when the MuJoCo physics engine computes
collisions. An example is depicted in Figure 12, with a larger
number of contact points generally resulting in a considerably
better discretization of the tactile readings. The full model with
refined meshes and tactile readings runs at 550 FPS.
E. Task Specification
Before enumerating the environment details below, let us
define auxiliary functions and variables that are employed in
the reward functions of multiple environments:
• tol (x, (xlower, xupper), m) is a function provided in the
DeepMind Control Suite package [59]. This is denoted
LB)


<!-- page 15 (ocr) -->
H1 w/o hands
H1 w/ ShadowHand
H1 w/ Robotiq gripper
H1 w/ Unitree hand
Digit w/ ShadowHand
Unitree G1
Observation space
51
151
55
103
221
87
Action space
19
61
23
45
65
37
DoF (body)
25
25
25
25
57
29
DoF (2 end-effectors)
0
50
4
26
50
14
TABLE III: All supported robot specifications. Note that the observation space in this table does not take into account any
observations of the surrounding environment and solely comprises generalized positions and velocities. We use quaternions for
the robot floating base orientation, as well as for ball joints, which add additional position coordinates compared to the velocity
components (which match the DoFs).
Configuration
FPS
Without hands
2450
Simplified body collisions
3600
Collisions only for feet
5100
Default
1050
TABLE IV: HumanoidBench Simulation Performance.
there as a tolerance function that returns 1 when the eval-
uated value is within the bounds, i.e., x ∈(xlower, xupper),
and between 0 and 1 otherwise. The margin m regulates
the slope of the function, i.e., how far from the bounds
the function approaches 0.
• height ((xlower, xupper), m)
is
a
variable
defined
as
tol (zhead, (xlower, xupper), m) that rewards the head height,
where zhead is the vertical coordinate of the robot head
position. Whenever the arguments are not indicated, we
assume xlower = 1.65, xupper = +∞, and m = 0.4125.
• d(objectA, objectB) is the distance between object A and
object B.
• upright ((xlower, xupper), m) is a variable defined as
tol (zproj, (xlower, xupper), m), which rewards the alignment
of the robot torso with respect to the vertical axis, where
zproj is the unit projection of the z-axis in the robot body
frame onto the z-axis in the global frame. Whenever the
arguments are not indicated, we assume xlower = 0.9,
xupper = +∞, and m = 1.9.
• stand := height×upright represents a standing posture
reward.
• e := 0.2 · 4 +
1
|u|
i tol(ui, (0, 0), 10)
rewards small
control effort, where u is the vector of actuation inputs.
• stable = stand × e, densely rewards stable standing
configurations.
• vx is the robot velocity in the x direction (positive forward)
of the robot body coordinate frame.
• vy is the robot velocity in the y direction (positive left)
of the robot body coordinate frame.
• zitem is the vertical z coordinate of the indicated ‘item’ in
the global frame.
• positem is the 3D position of the indicated ‘item’ in the
global frame.
1) walk:
Objective. Keep forward velocity close to 1 m/s without
falling to the ground.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.2.
Reward Implementation.
R(s, a) = stable × tol(vx, (1, +∞), 1).
2) stand:
Objective. Maintain a standing pose.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let:
• stillx = tol(vx, (0, 0), 2)
• stilly = tol(vy, (0, 0), 2),
Then:
R(s, a) = stable × mean(stillx, stilly)
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.2.
—%
]


<!-- page 16 (ocr) -->
(a) Refined meshes
(b) Contact before refinement
(c) Contact after refinement
Fig. 12: Refinement of collision meshes. As a result of the
mesh refinement (see (a), where each colored section indicates
a different collision mesh), our model can detect a higher
number of contact points, as shown by the yellow disks in
the figure. This results in a better spatial discretization of the
tactile readings.
3) run:
Objective. Keep forward velocity close to 5 m/s without
falling to the ground.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation.
R(s, a) = stable × tol(vx, (5, ∞), 5)
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.2.
4) sit:
Objective. Sit onto a chair situated closely behind the robot.
Observation. In sit_simple, the observation is a vector
containing all joint positions on the robot unit. In sit_hard,
we allow the chair to be moved, and the robot initial position is
randomized, so the observation includes position and orientation
of the chair as well.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset. Note that in sit_hard, the robot is rotated at a
random angle α ∈[−1.8 rad, 1.8 rad] with position initialized
at random values x ∈[0.2, 0.4], y ∈[−0.15, 0.15]
Reward Implementation. Let
• sittingx = tol(xrobot −xchair, (−0.19, 0.19), 0.2
• sittingy = tol(yrobot −ychair, (0, 0), 0.1
• sittingz = tol(zrobot, (0.68, 0.72), 0.2)
• posture = tol(zhead −zIMU, (0.35, 0.45), 0.3)
• stillx = tol(vx, (0, 0), 2)
• stilly = tol(vy, (0, 0), 2)
then, the reward of this task is
R(s, a) = ((0.5 · sittingz + 0.5 · sittingx × sittingy)
× upright × posture)
× e × mean(stillx, stilly)
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.5.
5) balance:
Objective. Balance on the unstable board. There are two
variants to this environment: the balance_simple variant’s
(}
*
w
>
|
7,
4
5
Fo
<
=
Y
[-
)


<!-- page 17 (ocr) -->
spherical pivot beneath the board does not move, while the
balance_hard variant’s pivot does.
Observation. The observation comprises the joint positions
and velocities of the robot and those of the board.
Initialization. The robot is initialized to a standing position
on the unstable board, with random noise added to all joint
positions during each episode reset.
Reward Implementation. Let
• stillx = tol(vx, (0, 0), 2)
• stilly = tol(vy, (0, 0), 2)
• still = 1
2(stillx + stilly)
• heightrobot = height((2.15, +∞))
Then:
R(s, a) = (e × still) × (heightrobot × upright)
Termination. The episode terminates after 1000 steps, or
when one of the following condition satisfies:
• zrobot < 0.8
• The sphere collides with anything other than the floor and
the standing board.
• The standing board collides with the floor.
6) stair:
Objective. Traverse an iterating sequence of upward and
downward stairs at 1 m/s.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let
• verticalfoot,left = tol(zhead −zfoot,left, (1.2, +∞), 0.45)
• verticalfoot,right = tol(zhead −zfoot,right, (1.2, +∞), 0.45)
Then:
R(s, a) = e × tol(vx, (1, +∞), 1) × upright((0.5, 1), 1.9)
× (verticalfoot,left × verticalfoot,right)
Termination. The episode terminates after 1000 steps, or
when zproj < 0.1.
7) slide:
Objective. Walk over an iterating sequence of upward and
downward slides at 1 m/s.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let
• verticalfoot,left = tol(zhead −zfoot,left, (1.2, +∞), 0.45)
• verticalfoot,right = tol(zhead −zfoot,right, (1.2, +∞), 0.45)
Then:
R(s, a) = e × tol(vx, (1, +∞), 1) × upright((0.5, 1), 1.9)
× (verticalfoot,left × verticalfoot,right)
Termination. The episode terminates after 1000 steps, or
when zproj < 0.6.
8) pole:
Objective. Travel in forward direction over a dense forest
of high thin poles, without colliding with them.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let
• γcollision =
0.1,
, robot collides with pole
1,
otherwise
Then,
R(s, a) = γcollision × (0.5 · stable + 0.5 · tol(vx, (1, +∞), 1)).
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.6.
9) reach:
Ct
©
WY


<!-- page 18 (ocr) -->
Objective. Reach a randomly initialized 3D point with the
left hand.
Observation. Joint positions and velocities of the robot, left
hand position of robot, and reaching target position.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let
• dhand = d(handleft, goal)
• health = 5 · zpelvis,proj
• penaltymotion = ∥vrobot∥2
• close =
5,
dhand < 1
0,
otherwise
• success =
10,
dhand < 0.05
0,
otherwise
Then,
R(s, a) = −10−4 · penaltymotion + health + close + success
Termination. The episode terminates after 1000 steps.
10) hurdle:
Objective. Keep forward velocity close to 5 m/s without
falling to the ground.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let
γcollision =
0.1
, robot is colliding with wall
1
, otherwise
Then, we formulate the reward of this task as:
R(s, a) = stable × tol(vx, (5, ∞), 5) × γcollision
Termination. The episode terminates after 1000 steps.
11) crawl:
Objective. Keep forward velocity close to 1 m/s while
passing inside a tunnel.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. Let:
• heightcrawl = height((0.6, 1), 1)
• heightIMU = tol(zIMU, (0.6, 1), 1)
• quatcrawl = 0.75
0
0.65
0 is the expected quater-
nion expected when the robot is crawling.
• orientation = tol(∥quatpelvis −quatcrawl∥, (0, 0), 1) re-
wards correct robot body orientation.
• tunnel = tol(yIMU, (−1, 1), 0) rewards the robot when
its y coordinate is inside the tunnel.
• speed = tol(vx, (1, +∞), 1)
Then, the reward is formulated as:
R = tunnel × (0.1 · e + 0.25 · min(heightcrawl, heightIMU)
+ 0.25 · orientation + 0.4 · speed)
Termination. The episode terminates after 1000 steps.
12) maze:
Objective. Reach the goal position in a maze by taking
multiple turns at the intersections.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. For each checkpoint in the maze,
we assign vtarget to be the velocity prescribed to travel from
the previous checkpoint towards next one. Then, let
• move =
tol(vx −vtargetx, (0, 0), vtargetx)
× tol(vy −vtargety, (0, 0), vtargety)
3
2
to


<!-- page 19 (ocr) -->
• γcollision =
0.1
, robot is colliding with wall
1
, otherwise
• proximity = tol(d(checkpoint, posrobot), (0, 0), 1)
We formulate the reward as
R(s, a) = (0.2 · stable + 0.4 · move
+ 0.4 · proximity) × γcollision
We also provide a sparse reward of i × 100 for arriving at the
ith checkpoint.
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.2.
13) push:
Objective. Move a box to a randomly initialized 3D point
on a table.
Observation. Joint positions and velocities of the robot, left
hand position of the robot, box destination, box position, and
box velocity.
Initialization. The robot is initialized to a standing position.
The box and its destination are initialized at a random location
on the table. Random noise is added to all joint positions
during each episode reset.
Reward Implementation. Let:
• dgoal = d(box, destination)
• success = 1dgoal<0.05
• dhand = d(box, handleft)
Then the reward is
R(s, a) = αs · success −αt · dgoal −αh · dhand
where by default αs = 1000, αt = 1, αh = 0.1.
Termination. The episode terminates after 500 steps, or
when dgoal < 0.05.
14) cabinets:
Objective. Open four different types of cabinet doors
(e.g., hinge door, sliding door, drawer) and perform different
manipulations (see subtasks below) for objects inside the
cabinet.
Observation. Positions and velocities of the robot’s joints,
the cabinets’ joints, and the objects situated inside the cabinets.
Initialization. The robot is initialized to a standing position,
with random noise added to all joint positions during each
episode reset.
Reward Implementation. The reward of this task changes
based on the occurring subtask.
Subtask 1 is to open the sliding door (second highest one),
with reward
R1 = 0.2 · stable + 0.8 · |lcabinet/0.4|
where the cabinet joint position lcabinet is a value in [0, 0.4].
Subtask 2 is to open the drawer (the lowest one), with reward
R2 = 0.2 · stable + 0.8 · |ldrawer/0.45|
where the drawer joint position ldrawer is a value in [0, 0.45].
Subtask 3 is to put the cube from the drawer into the hinge-
based cabinet (the third highest one). Both the left and right
hinge-based cabinet doors’ joint positions αdoor,left, αdoor,right are
values in [0, 1.57]. Let
• opendoor,left = min(1, |αdoor,left|)
• opendoor,right = min(1, |αdoor,right|)
• ddestination,x = tol(xcube −0.9, (−0.3, 0.3), 0.3)
• ddestination,y = tol(ycube, (−0.6, 0.6), 0.3)
• ddestination,z = tol(zcube −0.94, (−0.15, 0.15), 0.3)
• rdestination = 0.3 · mean(ddestination,x, ddestination,y) + 0.7 ·
ddestination,z
Then the reward of this subtask, R3, is formulated as follows
r3 = 0.5 · max(opendoor,left, opendoor,right) + 0.5 · rdestination
R3 = 0.2 · stable + 0.8 · r3
Subtask 4 is to put the original cube from the hinge-based left-
right cabinet (third highest) into the pull-up cabinet (highest).
The pull-up door has a joint position αpull in [0, 1.57]. Let
• openpull = min(1, |αpull|)
• ddestination,x = tol(xcube −0.9, (−0.3, 0.3), 0.3)
• ddestination,y = tol(ycube, (−0.6, 0.6), 0.3)
• ddestination,z = tol(zcube −1.54, (−0.15, 0.15), 0.3)
• rdestination = 0.3 · mean(ddestination,x, ddestination,y) + 0.7 ·
ddestination,z
Then the reward of this subtask, R4, is formulated as follows
r4 =0.5 · openpull + 0.5 · rdestination
R4 =0.2 · stable + 0.8 · r4
The reward during the occurrence of subtask i is Ri. Upon
the completion of subtask i, a sparse reward of i ∗100 is
offered. At the timestep where all subtasks are completed, a
sparse reward of 1000 is added to the total reward.
Termination. The episode terminates after 1000 steps or
whenever all subtasks are complete.
%,
PJ


<!-- page 20 (ocr) -->
15) highbar:
Objective. Athletically swing while staying attached to a
horizontal high bar until reaching a vertical upside-down
position.
Observation. Joint positions and velocities of the robot.
Initialization. The robot is initialized such that its hand is
gripping the high bar, and its body is hanging from it.
Reward Implementation. Let
• uprighthighbar = upright((−∞, −0.9), 1.9)
• feet = tol((zfoot,left + zfoot,right)/2, (4.8, +∞), 2)
Then,
R(s, a) = uprighthighbar × feet × e
Termination. The episode terminates after 1000 steps, or
when zhead < 2.
16) door:
Objective. Pull a door open using its doorknob, and traverse
through the doorpath while keeping the door open.
Observation. Joint positions and velocities of the robot, door
hinge, and door hatch.
Initialization. The robot is initialized to a standing position.
The door hinge joint and door latch are initialized such that the
door is completely closed. For the current implementation, the
door can only be pulled towards the robot, limiting its hinge
joint position to be within [0, 1.4]. The door latch has a joint
range of [0, 2] (being pulled downwards until 2 radians from
positive x-axis, clockwise). Random noise is added to all joint
positions during each episode reset.
Reward Implementation. Let
• opendoor = min(1, q2
door)
• openhatch = tol(qhatch, (0.75, 2), 0.75)
• proximitydoor =
tol( min(d(handleft, door), d(handright, door)),
(0, 0.25), 1)
• passage = tol(xIMU, (1.2, +∞), 1)
Then, the reward of this task is:
R = 0.1 · stable + 0.45 · opendoor + 0.05 · openhatch
+ 0.05 · proximitydoor + 0.35 · passage
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.58.
17) truck:
Objective. Unload packages from a truck by moving them
onto a platform.
Observation. Joint positions and velocities of the robot, and
positions and velocities of packages.
Initialization. The robot is initialized to a standing position.
Packages are initialized to be on the truck. Random noise is
added to all joint positions during each episode reset.
Reward Implementation. The reward of this task relies on
the subsets of packages based on three categories: (1) being
on truck (ptruck), (2) being picked up (ppicked), and (3) being
on table (ptable). Let
• truck = tol(minp∈ptruck ∥posp −pospelvis∥, (0, 0.2), 4)
• picked = tol(minp∈ppicked ∥posp −pospelvis∥, (0, 0.2), 4)
• table = tol(minp∈ptable ∥posp −postable∥, (0, 0.2), 4)
• rlocation = 100 · (ptable + ppicked −ptruck)
Then, the reward is:
R(s, a) = rlocation + upright × (1 + truck + picked + table)
If all packages are picked up, an additional sparse reward of
1000 is provided, and the episode terminates thereafter.
Termination. The episode terminates after 1000 steps, or
when all packages are delivered onto the table.
18) cube:
Objective. Manipulate two cubes, each cube in one hand,
until they both correspond with a specific, randomly initialized
target orientation.
Observation. Joint positions and velocities of the robot and
the two cubes to be manipulated on hand. The transparent cube
=
”,
x |


<!-- page 21 (ocr) -->
in front of the robot is an indication of the target orientation
for in-hand cubes, and its orientation is also in the state.
Initialization. The robot is initialized to a standing position.
The cubes are initialized at a random orientation right above
the robot hands. Random noise is added to all joint positions
during each episode reset.
Reward Implementation. Let
• stillx = tol(vx, (0, 0), 2)
• stilly = tol(vy, (0, 0), 2)
• still = mean(stillx, stilly)
• quattarget denotes the target orientation for both in-hand
cubes.
• orientation =
1
2[(quatcube,left −quattarget)2 +(quatcube,right −quattarget)2]
• proximitycube =
1
2[tol(d(cubeleft, handleft), (0, 0), 0.5)
+ tol(d(cuberight, handright), (0, 0), 0.5)]
Then the reward of this task is:
R =0.2 · (stable × still)
+ 0.5 · orientation + 0.3 · proximitycube
Termination. The episode terminates after 500 steps, or
when zpelvis < 0.5, zcube,left < 0.5, or zcube,right < 0.5.
19) bookshelf:
Objective. The bookshelf environment mainly concerns
relocating five objects across the various shelves. There are
five designated subtasks, resembling five different relocations
(each for a different item and destination location). The items
involved in the subtasks are colored from brightest to darkest
in a red shade, where the brighter shade of red shows that
the object’s relocation is an earlier subtask to complete. The
subtasks must be completed in order. The order is always
the same in bookshelf_simple, while it is randomized at
every episode in bookshelf_hard.
Observation. Positions and velocities of the robot’s joints
and all objects on the bookshelf, including those that are not
associated with any subtasks, as well as an index representing
the next object to be relocated.
Initialization. The robot is initialized to a standing position.
All objects on the bookshelf are currently initialized at a default
position. Random noise is added to all joint positions during
each episode reset. In the simple version of this environment,
the objects to move on the bookshelf and their destinations are
fixed; in the hard version, both of them are randomized at the
beginning of every episode instead.
Reward Implementation. For each subtask ti where i ∈
{1, 2, . . . , 5}, its reward ri is formulated as follows. First, let
• proximitydestination =
tol(d(object, destination), (0, 0.15), 1)
• dhand =
min(d(object, handleft), d(object, handright))
• proximityhand = exp(−dhand).
Then, the subtask reward is
ri =0.4 · proximityhand
+ 0.2 · stable + 0.4 · proximitydestination
and the reward for that step is the subtask reward per se.
The current subtask is considered complete when the distance
between the destination and object of current subtask is less
than 0.15.
An additional sparse reward of 100∗i is added to the timestep
of subtask i’s completion.
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.58, zobject < 0.5, or all subtasks succceeded.
20) basketball:
Objective. Catch a ball coming from random direction and
throw it into the basket.
Observation. Positions and velocities of the robot’s joints
and the basketball.
Initialization. The robot is initialized to a standing position.
The basketball is initialized such that it will be randomly
spawned at a radius of 1.5 m from the robot, at a random angle
ω ∈[−1.45 rad, 1.45 rad] from positive x-axis, and arrive
right in front of the robot after 0.2 s. Random noise is added
to all joint positions during each episode reset.
Reward Implementation. The task is divided into two stages:
catch :
before the basketball collides with anything
throw :
after the basketball experiences one collision
The rewards at different stages are formulated differently. Let
• proximityhand =
tol( max(d(ball, handleft), d(ball, handright)),
(0, 0.2), 1)
• aim = tol(d(ball, basket), (0, 0), 7).


<!-- page 22 (ocr) -->
Then, the reward at each stage of the task is formulated as
follows:
Rcatch(x, u) = 0.5 · proximityhand + 0.5 · stable
Rthrow(x, u) = 0.05 · proximityhand
+ 0.15 · stable + 0.8 · aim
At the earliest timestep where d(ball, basket) ≤0.05, the
episode terminates, and a large sparse reward of 1000 is given.
Termination. The episode terminates after 500 steps, or when
zpelvis < 0.5, zball < 0.5, or when success has been achieved.
21) window:
Objective. Grab a window wiping tool and keep its tip
parallel to a window by following a prescribed vertical speed
(in absolute value).
Observation. Joint positions and velocities of the robot and
the window wiping tool (position and velocities of the entire
tool, in addition to those of the rotational joint attached between
the wipe and the rod of the tool).
Initialization. The robot is initialized to a standing position.
The window wiping tool is initialized above the robot unit’s
hand in a parallel direction to the window frames. Random
noise is added to all joint positions during each episode reset.
Reward Implementation. Let
• proximitytool =
1
2[tol(d(tool, handleft), (0, 0), 0.5)
+ tol(d(tool, handright), (0, 0), 0.5)]
• dwindow = tol(d(head, window), (0.4, 0.4), 0.1)
• movewipe = tol(|vwipe,z|, (0.5, 0.5), 0.5)
The manipulation reward is defined as:
rmanipulation =0.4 · movewipe + 0.4 · proximitytool
+ 0.2 · (stable × dwindow)
Meanwhile, five sites are put on the four corners and center
of the wipe to detect coverage of contact. Let these sites be
s1, s2, . . . , s5, then the reward for contact between the tool
and window is defined as:
rcontact = 1
5
si
tol(xsi, (0.92, 0.92), 0.4)
Then, the reward of this task is:
R = 0.5 · rmanipulation + 0.5 · rcontact
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.58 or ztool < 0.58.
22) spoon:
Objective. Grab a spoon and use it to follow a circular pattern
inside a pot.
Observation. Joint positions and velocities of the robot and
the position and velocity of the spoon, as well as the target
position that the spoon should be at the current timestep.
Initialization. The robot is initialized to a standing position.
The spoon is initialized at a specified position on the table,
leftwards of the pot. Random noise is added to all joint positions
during each episode reset.
Reward Implementation. Let
• t := current timestep
• proximitytool =
1
2[tol(d(tool, handleft), (0, 0), 0.5)
+ tol((tool, handright), (0, 0), 0.5)]
• destination =


xpot + 0.06 cos( tπ
20)
ypot + 0.06 sin( tπ
20)
zpot


• rtrajectory = tol(d(spoon, destination), (0, 0), 0.15)
• rdestination =
1
3 i∈{x,y,z}
1ispoonin the pot
Then:
R(s, a) = 0.15 · stable + 0.25 · proximitytool
+ 0.25 · rdestination + 0.35 · rtrajectory
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.58.
23) kitchen:
Objective. Execute a sequence of actions in a kitchen
environment, namely, open a microwave door, move a kettle,
and turn burner and light switches.
Observation. Joint positions and velocities of the robot, and
positions and velocities of kitchenware.
.
N
CE


<!-- page 23 (ocr) -->
Initialization. The robot is initialized to a standing position.
Kitchenware is initialized at specified positions. Random noise
is added to all joint positions during each episode reset.
Reward Implementation. A subtask in kitchen is consid-
ered complete if the distance between an object and its goal
position is lower than a specified threshold. The sparse reward
is the number of subtasks completed.
Termination. The episode terminates after 500 steps.
24) package:
Objective. Move a box to a randomly initialized target
position, also tested in the ablation in Figure 9.
Observation. Joint positions and velocities of the robot,
both hand positions of the robot, package destination, package
position, and package velocity.
Initialization. The robot is initialized to a standing position.
The package position and its destination are randomly initial-
ized within a specific area. Random noise is added to all joint
positions during each episode reset.
Reward Implementation. Let
• heightpackage = min(1, zpackage)
• success = 1d(package,destination)<0.1
• dhand = d(package, handleft) + d(package, handright).
Then, the reward is:
R(s, a) = −3 · d(package, destination) −0.1 · dhand
+ stable + heightpackage + 1000 · success
Termination. The episode terminates after 1000 steps, or
when d(package, destination) < 0.1.
25) powerlift:
Objective. Lift a barbell of a designated mass.
Observation. Joint positions and velocities of the robot and
barbell.
Initialization. The robot is initialized to a standing position.
The barbell is initialized on the ground. Random noise is added
to all joint positions during each episode reset.
Reward Implementation. Let
• heightbarbell = tol(zbarbell, (1.9, 2.1), 2).
Then,
R(s, a) = 0.2 · stable + 0.8 · heightbarbell.
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.2.
26) room:
Objective. Organize a 5 m by 5 m space populated with
randomly scattered object to minimize the variance of scattered
objects’ locations in x, y-axis directions.
Observation. Joint positions and velocities of the robot and
scattered objects.
Initialization. The robot is initialized to a standing position.
The scattered objects’ positions are randomly initialized within
a specific area. Random noise is added to all joint positions
during each episode reset.
Reward Implementation. Let
• X be a matrix containing the location of all scattered
objects in 3D coordinates.
• cleanness = tol(max(V ar(X:,0), V ar(X:,1)), (0, 0), 3),
where V ar(X:,0) is the variance of x-coordinates of all
objects’ locations, and V ar(X:,1) is such variance for
y-coordinates.
Then,
R(s, a) = 0.2 · stable + 0.8 · cleanness
Termination. The episode terminates after 1000 steps, or
when zpelvis < 0.3.
27) insert:
Objective. Insert the ends of a rectangular block into
two
small
pegs.
Two
versions,
insert_small
and
insert_normal present different object sizes.
Observation. Joint positions and velocities of the robot,
rectangular block to insert, and two provided small pegs.
Initialization. The robot is initialized to a standing position.
The rectangular block and two pegs are initialized on the table
at specific orientation and position.
y
7
rT
dl


<!-- page 24 (ocr) -->
Reward Implementation. Let the rectangular blocks be
formualted to have two ends enda, endb, which must be
respectively inserted to the pegs pega, pegb.
• proximitypeg,site = tol(d(peg, site), (0, 0), 0.5)
• proximityblock =
mean(proximity(pega, enda), proximity(pegb, endb))
• height(peg) = tol(zpeg −1.1, (0, 0), 0.15)
• heightpegs = mean(height(pega), height(pegb))
• proximityhands =
mean(proximity(pega, handleft),
proximity(pegb, handright))
The reward of this task is phrased as:
R(s, a) =(0.5 · stable + 0.5 · proximityblock)
× (0.5 · heightpegs + 0.5 · proximityhands)
Termination. The episode terminates after 1000 steps, or
when any of the blocks or pegs are at a height lower than 0.5
from floor.
APPENDIX C
TRAINING DETAILS
A. Baseline Implementation Details
For SAC, we use the implementation from JaxRL Mini-
mal [16]. For PPO, we use the Stable-Baselines3 [51] imple-
mentation with 4 parallel environments. For DreamerV3 and
TD-MPC2, we use their official code. For DreamerV3, we use
the ‘medium’ configuration, with an update-to-data ratio of 64.
For TD-MPC2, we use the 5M configuration. Unless specified,
we use their default hyperparameters.
B. Reaching Policy Implementation Details
We train the low-level reaching policies described in Sec-
tion V-D using PPO, largely parallelized on GPU using MuJoCo
MJX. We employ the PureJaxRL [35] implementation, using
their default parameters, except a higher number of environ-
ments as detailed in Section V-D, 16 steps per environment,
and an entropy coefficient of 0.001.
C. Benchmarking Results
We summarize our benchmarking results in Table V and
Table VI. We report the mean and standard deviation of
maximum episode returns over three seeds. DreamerV3 and
SAC are trained for 10M, while TD-MPC2 is trained for 2M
environment steps, which roughly corresponds to 48 h.
DreamerV3
TD-MPC2
SAC
Target
walk
800.2 ± 158.7
782.0 ± 109.2
31.7 ± 24.0
700.0
stand
622.7 ± 404.8
809.0 ± 137.1
208.3 ± 105.6
800.0
run
633.8 ± 222.4
93.3 ± 14.3
5.0 ± 2.1
700.0
reach
7580.9 ± 1951.0
7316.1 ± 2112.1
4565.1 ± 212.8
12000.0
hurdle
126.2 ± 59.4
46.4 ± 10.8
13.2 ± 8.8
700.0
crawl
878.8 ± 122.7
957.4 ± 17.5
330.0 ± 111.9
700.0
maze
272.3 ± 116.6
244.3 ± 97.7
144.8 ± 17.8
1200.0
sit_simple
891.4 ± 38.4
411.1 ± 368.0
148.3 ± 103.8
750.0
sit_hard
433.4 ± 355.9
343.0 ± 381.7
55.0 ± 18.2
750.0
balance_simple
19.8 ± 7.0
40.5 ± 23.9
61.5 ± 1.1
800.0
balance_hard
45.9 ± 27.4
48.2 ± 28.5
42.5 ± 22.6
800.0
stair
131.1 ± 43.6
70.4 ± 7.1
14.1 ± 6.8
700.0
slide
436.5 ± 200.1
119.0 ± 35.9
6.3 ± 2.8
700.0
pole
658.3 ± 343.3
226.3 ± 116.1
46.3 ± 26.4
700.0
push
−1251.9 ± 659.8
−258.7 ± 66.5
−97.9 ± 147.0
700.0
cabinet
57.3 ± 66.3
112.8 ± 142.9
211.8 ± 33.8
2500.0
highbar
8.9 ± 5.8
0.3 ± 0.0
9.4 ± 3.7
750.0
door
213.0 ± 149.3
274.7 ± 12.5
39.4 ± 25.2
600.0
truck
1103.8 ± 232.9
1132.6 ± 72.1
1077.5 ± 95.0
3000.0
cube
111.2 ± 59.9
54.7 ± 33.1
130.7 ± 30.5
370.0
bookshelf_simple
840.4 ± 5.6
136.2 ± 71.6
346.9 ± 231.5
2000.0
bookshelf_hard
530.2 ± 302.5
37.0 ± 1.3
293.9 ± 121.6
2000.0
basketball
19.3 ± 2.5
42.0 ± 14.8
22.1 ± 3.2
1200.0
window
461.0 ± 252.8
87.1 ± 37.5
62.9 ± 83.8
650.0
spoon
349.7 ± 46.2
77.9 ± 80.6
87.7 ± 80.5
650.0
kitchen
0.0 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
4.0
package
−18015.2 ± 9477.7
−3655.6 ± 1055.0
−6718.3 ± 607.0
1500.0
powerlift
315.9 ± 16.9
99.1 ± 47.3
81.8 ± 46.7
800.0
room
120.5 ± 71.4
131.4 ± 56.7
12.0 ± 4.9
400.0
insert_small
184.8 ± 26.3
129.8 ± 51.9
10.8 ± 13.4
350.0
insert_normal
171.5 ± 33.2
237.6 ± 9.1
46.3 ± 63.1
350.0
TABLE V: Average returns for HumanoidBench. Each
number represents average return@10M (return@2M) with
the standard deviation for DreamerV3 and SAC (TD-MPC2).
DreamerV3
TD-MPC2
SAC
Target
walk
932.4 ± 0.3
900.3 ± 47.6
68.7 ± 27.0
700.0
stand
932.9 ± 1.1
925.7 ± 2.5
809.9 ± 194.5
800.0
run
895.9 ± 6.0
226.7 ± 23.3
104.8 ± 7.4
700.0
reach
9831.6 ± 115.9
9727.6 ± 48.9
7169.9 ± 874.1
12000.0
hurdle
396.8 ± 39.7
196.7 ± 30.5
78.6 ± 32.8
700.0
crawl
985.3 ± 0.6
985.2 ± 0.4
626.5 ± 29.1
700.0
maze
592.5 ± 49.0
444.9 ± 22.1
269.9 ± 37.8
1200.0
sit_simple
935.7 ± 5.5
928.4 ± 1.5
842.7 ± 50.8
750.0
sit_hard
914.6 ± 1.5
906.3 ± 6.0
214.0 ± 47.9
750.0
balance_simple
95.4 ± 8.3
95.3 ± 3.1
80.7 ± 3.7
800.0
balance_hard
114.0 ± 12.3
122.2 ± 13.1
71.0 ± 7.9
800.0
stair
411.4 ± 9.7
251.9 ± 9.1
42.8 ± 0.7
700.0
slide
928.4 ± 2.0
311.9 ± 15.1
41.4 ± 2.4
700.0
pole
952.2 ± 10.3
644.9 ± 21.2
440.0 ± 88.4
700.0
push
1000.0 ± 0.0
1000.0 ± 0.0
352.8 ± 31.5
700.0
cabinet
722.6 ± 7.3
721.6 ± 25.9
485.9 ± 137.2
2500.0
highbar
83.1 ± 4.6
0.9 ± 0.4
40.8 ± 41.7
750.0
door
335.7 ± 14.8
310.6 ± 10.6
251.2 ± 9.0
600.0
truck
1674.3 ± 52.6
1457.2 ± 24.3
1387.5 ± 10.0
3000.0
cube
237.9 ± 3.4
241.1 ± 1.2
203.5 ± 27.2
370.0
bookshelf_simple
849.6 ± 0.3
825.0 ± 9.6
766.5 ± 10.3
2000.0
bookshelf_hard
867.8 ± 8.4
320.4 ± 58.9
681.5 ± 10.3
2000.0
basketball
808.8 ± 340.5
1055.3 ± 4.1
192.3 ± 45.6
1200.0
window
765.6 ± 38.4
201.1 ± 91.5
128.6 ± 170.8
650.0
spoon
421.5 ± 2.5
403.5 ± 3.2
297.5 ± 26.5
650.0
kitchen
0.0 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
4.0
package
1009.2 ± 4.1
1003.3 ± 3.4
−3552.8 ± 361.3
1500.0
powerlift
338.6 ± 0.1
264.7 ± 23.9
171.2 ± 3.6
800.0
room
420.8 ± 51.1
353.3 ± 41.5
52.2 ± 3.9
400.0
insert_small
239.8 ± 4.6
226.4 ± 10.8
72.7 ± 21.9
350.0
insert_normal
279.9 ± 9.9
273.0 ± 5.7
135.3 ± 51.5
350.0
TABLE VI: Maximum returns for HumanoidBench. Each
number represents maximum return@10M (return@2M) with
the standard deviation for DreamerV3 and SAC (TD-MPC2).
