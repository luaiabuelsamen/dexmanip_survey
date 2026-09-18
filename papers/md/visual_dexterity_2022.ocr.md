<!-- page 1 (ocr) -->
Visual Dexterity: In-Hand Reorientation of Novel and
Complex Object Shapes
Tao Chen1,2, Megha Tippur2, Siyang Wu3, Vikash Kumar4,
Edward Adelson2, Pulkit Agrawal∗1,2,5
1Improbable AI Laboratory, Massachusetts Institute of Technology
Cambridge, MA 02139, USA
2Computer Science and Artificial Intelligence Laboratory (CSAIL),
Massachusetts Institute of Technology,
Cambridge, MA 02139, USA
3Institute for Interdisciplinary Information Sciences,
Tsinghua University, Beijing, 100084, China
4Meta AI, Pittsburgh, PA 15213, USA
5Institute of Artificial Intelligence and Advanced Interactions (IAIFI)
Massachusetts Institute of Technology,
Cambridge, MA 02139, USA
∗To whom correspondence should be addressed; E-mail: pulkitag@mit.edu.
In-hand object reorientation is necessary for performing many dexterous ma-
nipulation tasks, such as tool use in less structured environments that remain
beyond the reach of current robots. Prior works built reorientation systems
assuming one or many of the following: reorienting only specific objects with
simple shapes, limited range of reorientation, slow or quasistatic manipula-
tion, simulation-only results, the need for specialized and costly sensor suites,
and other constraints which make the system infeasible for real-world deploy-
ment. We present a general object reorientation controller that does not make
1
arXiv:2211.11744v3  [cs.RO]  24 Nov 2023


<!-- page 2 (ocr) -->
these assumptions. It uses readings from a single commodity depth camera to
dynamically reorient complex and new object shapes by any rotation in real-
time, with the median reorientation time being close to seven seconds. The
controller is trained using reinforcement learning in simulation and evaluated
in the real world on new object shapes not used for training, including the most
challenging scenario of reorienting objects held in the air by a downward-
facing hand that must counteract gravity during reorientation. Our hardware
platform only uses open-source components that cost less than five thousand
dollars. Although we demonstrate the ability to overcome assumptions in prior
work, there is ample scope for improving absolute performance. For instance,
the challenging duck-shaped object not used for training was dropped in 56
percent of the trials. When it was not dropped, our controller reoriented the
object within 0.4 radians (23 degrees) 75 percent of the time.
Summary
A real-time controller that dynamically reorients complex and new objects by any amount using
a single depth camera.
Introduction
The human hand’s dexterity is vital to a wide range of daily tasks such as re-arranging objects,
loading dishes in a dishwasher, fastening bolts, cutting vegetables, and other forms of tool use
both inside and outside households. Despite a long-standing interest in creating similarly capa-
ble robotic systems, current robots are far behind in their versatility, dexterity, and robustness.
In-hand object reorientation, illustrated in Figure 1, is a specific dexterous manipulation prob-
lem where the goal is to manipulate a hand-held object from an arbitrary initial orientation to an
2


<!-- page 3 (ocr) -->
arbitrary target orientation (1–7). Object reorientation occupies a special place in manipulation
because it is a pre-cursor to flexible tool use. After picking a tool, the robot must orient the tool
in an appropriate configuration to use it. For example, a screwdriver can only be used if its head
is aligned with the top of the screw. Object reorientation is, therefore, not only a litmus test for
dexterity but also an enabler for many downstream manipulation tasks.
A reorientation system ready for the real world should satisfy multiple criteria: it should
be able to reorient objects into any orientation, generalize to new objects, and operate in real-
time using data from commodity sensors. Some seemingly benign setup choices can make the
system impractical for real-world deployment. For instance, consider the choice of placing
multiple cameras around the workspace to reduce occlusion in viewing the object being ma-
nipulated (8,9). For a mobile manipulator, such camera placements are impractical. Similarly,
performing reorientation under the assumption that the hand is below the object (upwards fac-
ing hand configuration) (8–10) instead of the hand holding the object from the top (downwards
facing hand configuration) is much easier. With a downward-facing hand, the hand must ma-
nipulate the object while simultaneously counteracting gravity. Small errors in finger motion
can result in the object falling down. The upward-facing hand assumption makes control easier,
but it limits the downstream use of the reorientation skill in many tool-use applications.
Even without real-world setup constraints, object reorientation is challenging because it re-
quires coordinated movement between multiple fingers resulting in a high-dimensional control
space. The robot must control the amount of applied force, when to apply it, and where the
fingers should make and break contact with the object. The combination of continuous and
discrete decisions leads to a challenging continuous-discrete optimization problem that is often
computationally intractable. For computational feasibility, a majority of prior works constrain
manipulation to simple convex shapes such as polygons or cylinders (6,8,11–22). Other simpli-
fying assumptions include designing specific movement patterns of fingers (18, 23), assuming
3


<!-- page 4 (ocr) -->
fingers never make and break contact with the object (15,24), hand being in an upward-facing
configuration (5, 8, 10) or the manipulation being quasi-static (23, 25). Such assumptions re-
strict the applicability of reorientation to a limited set of objects, scenarios, or orientations (for
example, along only a single axis).
Complementary to the control problem is the issue of measuring the state information the
controller requires, such as the object’s pose, surface friction, whether the finger is in contact
with the object, etc. Touch sensors provide local contact information but are not widely avail-
able as a plug-and-play module. The difficulty in using visual sensing is that fingers occlude
the object during reorientation. Recent works employed RGBD (RGB and depth) cameras to
estimate object pose but require a separate pose estimator to be trained per object, which limits
their generalization to new object shapes (8,9,23,26).
Due to challenges in perception and control, no prior work has demonstrated a real-world
ready reorientation system. Although controlling directly from perception is hard, given the
full low-dimensional representation of relevant state information such as the object’s position,
velocity, pose, and manipulator’s proprioceptive state, it is possible to build a controller using
deep reinforcement learning (RL) that successfully reorients diverse objects in simulation (7).
RL effectively leverages large amounts of interaction data to find an approximate solution to the
computationally challenging optimization problem of solving for reorientation. However, as a
result of requiring large amounts of data and full state information, today, such RL controllers
can only be trained in simulation. This leaves at least two open questions: how to train con-
trollers with sensors available in the real world such as visual inputs and whether controllers
trained in simulation transfer to the real world (sim-to-real transfer problem).
The difficulty in training RL controllers from visual inputs stems from the learner’s need to
simultaneously solve the problem of inferring the relevant state information (feature learning)
and determining the optimal actions. If the optimal actions were known in advance, it would
4


<!-- page 5 (ocr) -->
be simpler to train a model that predicts these actions from visual inputs (supervised learning).
Such a two-stage teacher-student training paradigm, where first a control policy is trained via
RL with full state information (teacher) and then a second student policy trained via supervised
learning to mimic the teacher has been successfully used for several applications (7, 27–30).
We found the major roadblock in learning a visual policy that works across diverse objects is
the slow speed of rendering in simulation which resulted in training times of over 20 days with
our compute resources. Such slow training makes experimentation infeasible. We devised a
two-stage approach for training the vision policy that first uses a synthetic point cloud without
the need for rendering and is then finetuned with rendered point cloud to reduce the sim-to-real
gap. Our pipeline makes training 5× times faster. The second consideration was the use of a
sparse convolution neural network to represent the policy to process point clouds at the speed
required for real-time feedback control (12Hz in our case). By directly predicting actions from
point clouds, our approach bypasses the problem of consistently defining pose/keypoints across
different objects, allowing for generalization to new shapes.
The next challenge is in overcoming the sim-to-real gap. In dynamic in-hand object reori-
entation, both the robot and the object move quickly. Achieving precise control in a system
with fast-changing dynamics is challenging. It becomes even more challenging when using a
downward-facing hand as control failures are irreversible. Therefore, dynamic in-hand object
reorientation poses a substantial sim-to-real transfer challenge. Some reasons for the sim-to-real
gap are differences in motor/object dynamics, perception noise, and modeling approximations
made by the simulator. For instance, contact models in fast simulators tend to be a crude ap-
proximation of reality, especially for non-convex objects (31). Whether sim-to-real transfer of
reorientation controller is even possible for these complex object shapes remained unclear.
The systematic choices of identifying the manipulator dynamics (details in Method sec-
tion), domain randomization (32), the design of reward function, and the hardware considera-
5


<!-- page 6 (ocr) -->
tions, including the number of fingers and the fingertip material, reduced the sim-to-real gap.
We conducted experiments in the challenging downward-facing hand configuration. We tested
the controller’s ability to make use of an external support surface for reorientation (extrinsic
dexterity (33)) and the harder condition when the object is in the air without any supporting
surface. The results show progress towards developing a real-time controller capable of dy-
namically reorienting new objects with complex shapes and diverse materials by any amount in
the full space of rotations (SO(3), special orthogonal group in three dimensions) using inputs
from just a single commodity depth camera and joint encoders. While there is substantial room
for improvement, especially in achieving precise reorientation, our results provide evidence
that sim-to-real transfer is possible for challenging tasks involving dynamic and contact-rich
manipulation in less-structured settings than previously demonstrated.
Finally, many prior efforts used custom or expensive manipulators (such as the Shadow
Hand (8–10) costing over $100, 000) and often relied on sophisticated sensing equipments such
as a motion capture system. Such a hardware stack is hard to replicate due to its cost and
complexity. In contrast, our hardware setup costs less than $5, 000 and uses only open-source
components, making it easier to replicate. Furthermore, our platform is not specific to object
reorientation and can be used for other dexterous manipulation tasks. Due to the low barrier
to entry, and the evidence that such a system can tackle a challenging manipulation task, our
platform can democratize research in dexterous manipulation.
Results
We trained a single controller to reorient 150 objects from an arbitrary initial to a target config-
uration in simulation. The learned controllers are deployed in the real world on the open-source
three-fingered D’Claw manipulator (34) and a modified four-fingered version with nine and
twelve degrees of freedom (DoFs), respectively. The robot’s observation is a depth image cap-
6


<!-- page 7 (ocr) -->
joint positions
point cloud
Controller
joint commands
side view
A
B
Fig. 1 Illustration of the robot system. (A): the front and side views of our real-world setup.
The controller is a neural network that uses depth recordings from a single camera along with
the joint positions of the manipulator to predict the change in joint positions. (B): Visualization
of the same controller reorienting three different objects. The rightmost column shows the target
orientation. The first two rows are instances of a four-fingered hand reorienting objects in the
air. The last row shows reorientation with the help of a supporting surface (extrinsic dexterity).
tured from a single Intel RealSense camera and the proprioceptive state of the fingers. The goal
is provided as the point cloud of the object in a target configuration in the SO(3) space. The
initial configuration of the object is a random transformation in SE(3)(special Euclidean group
in three dimensions) space within the range of the robot’s fingers – either the object is set on a
table or handed over by a human to the robot.
We experimented with the hand in the downward-facing configuration in two settings: with
and without a supporting table. Our system runs in real-time at a control frequency of 12
7
il aly
EE
eller
Ld
|
|
i
FASE NEI
CE


<!-- page 8 (ocr) -->
Hz using a commodity workstation. Figure 1 shows the intermediate steps of manipulating
three objects to target orientations depicted in the rightmost column. The proposed controller
reorients a diverse set of new objects with complex geometries not used for training. The main
text movie provides a short summary of our results with audio. Movie S1 shows our system
reorienting many objects and provides a more detailed summary of our major findings. Movie
S2 visualizes the setting where the robot is tasked with a sequence of target orientations. In
such a scenario, it has to stop when it reaches the current target orientation and then restart to
achieve the next target.
For quantitative evaluation, we use seven objects from the training dataset (B), which we
refer to as in-distribution, and five objects from the held-out test dataset (S), which we refer
to as out-of-distribution (OOD). Objects are shown in Figure 2A. We test each object 20 times
with random initial and goal orientation in each testing condition. We 3D print these objects
to ensure the shape of objects in simulation and the real world is identical, which is helpful in
evaluating the extent of sim-to-real transfer. While the shape of these seven objects is included
in the training set, the surface properties such as friction of the real-world objects, may not
correspond to any object used for training in simulation. Evaluation on five OOD objects tests
generalization to shapes. To further showcase generalization to shapes and different material
properties, we also present results on some rigid objects from daily life. The orientation errors
are measured using an OptiTrack motion capture system that tracks object pose. We define error
as the distance between the goal and the object’s orientation when the controller predicts it has
reached the goal and stops. The motion capture is only used for evaluation and is not required
by our controller otherwise.
8


<!-- page 9 (ocr) -->
1
2
3
4
6
7
8
5
9
10
11
12
12
1
2
3
4
5
6
7
8
9
10
11
12
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Object ID
Error (rad)
1
2
3
4
5
6
7
8
9
10
11
12
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Object ID
Error (rad)
M1
M2
M3
M4
M5
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Material ID
Error (rad)
M1
M2
M3
M4
M5
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Material ID
Error (rad)
1
2
3
4
5
6
7
8
9
10
11
12
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Object ID
Error (rad)
M1
M2
M3
M4
M5
A
B
C
D
E
F
G
Fig. 2 Experimental results of reorientation. (A): twelve objects with their IDs. The first
seven objects are from the training dataset B, and the last five are from the testing dataset S. (B),
(C) show the real-world error distribution when using rigid and soft fingertips, respectively, on
material M1. (D) shows the error distribution in simulation for each object as a violin plot (35).
The violet rectangle shows the errors within [25%, 75%] percentile and the horizontal bar in
the rectangle depicts the median error. Train objects can mostly be reoriented within an error
of 0.4 radians, with similar performance for rigid and soft fingertips. The error on test objects
is higher, and soft fingertips exhibit better generalization. (E): five table materials. (F) and (G)
show the error distribution on different materials for object #5 and #10, respectively.
9
|
||
}
||
||
|
||


<!-- page 10 (ocr) -->
Extrinsic dexterity: object reorientation with a supporting surface
We first report results on the easier problem of reorienting objects when the table is present
below the hand to support the object. Using an external surface to aid reorientation has been
referred to as extrinsic dexterity (33) and is necessary in many real-world use cases. Visualiza-
tion of the proposed controller reorienting a diverse set of objects is provided in Figure 3. To
demonstrate the versatility of our system, we present results of the robot manipulating objects
of different shapes, materials, surfaces, fingertip materials, and varying numbers of fingers.
Reorientation using a three-fingered manipulator with rigid and soft fingertips
With table support, we found three fingers to suffice for the reorientation task. The error distri-
bution for different objects, when tested on a table surface covered with a white cloth (material
M1 in Figure 2E), is shown in Figure 2B using a violin plot (35). Although the overall er-
ror distribution is more informative, for ease of comparison, in Table 1, following the success
threshold used in previous work (8), we report summary statistics of success rate measured as
the percentage of tests with error within 0.4 or 0.8 radians. The seven train objects can be reori-
ented within an error of 0.4 radians 81% of the time. On the five OOD test objects, the success
rate is lower at 45%. As expected, the performance is better with a relaxed error threshold of
0.8 radians and worse at stricter thresholds.
Qualitatively observing the robot behavior revealed that some causes of failure were the
object overshooting the target orientation or the finger slipping across the object, especially
for OOD objects. One explanation is that rigid hemispherical fingertips contact the object in
a very small area (close to making a point contact), which makes small errors in the action
commands more pronounced. Further, we found that the fingertip material had low friction
resulting in slips which made manipulation harder. To mitigate these issues, we designed and
fabricated soft fingertips that cover the rigid 3D-printed skeleton with a soft elastomer (see
10


<!-- page 11 (ocr) -->
A
B
C
D
E
F
G
Fig. 3 Different testing scenarios. We test our controller on objects with diverse shapes and
reorientation conditions such as using different supporting surfaces such as a tablecloth, an
uneven door mat, a slippery acrylic sheet, and a perforated bath mat. We also evaluate perfor-
mance using fingertips with different softness: rigid 3D-printed (row (A)), and soft elastomer
fingertips (rows (B) to (G)). Row (A) to (E) use a three-fingered robot hand. And row (F) to
(G) use a four-fingered robot hand. Our policy can reorient real household objects (rows (E,G))
and can operate without the need for a supporting surface (in the air) as shown in row (G).
11
JRC JR EC JR pre pe
ECR RRR


<!-- page 12 (ocr) -->
Table 1: Statistics of the orientation error when the hand reorients objects on a table. CI
stands for bias-corrected and accelerated (BCa) bootstrap confidence interval. Train stands for
testing on the seven objects (Figure 2A) from the training dataset B. Test stands for testing on
the five objects from the testing dataset S.
with rigid fingertips
(real)
with soft fingertips
(real)
in simulation
Train
Test
Train
Test
Train
Test
≤0.4 radians (22.9◦)
81%
45%
79%
55%
96%
85%
95% CI
[73%, 90%]
[32%, 58%]
[71%, 86%]
[44%, 62%]
[94%, 97%]
[82%, 88%]
≤0.8 radians (45.8◦)
95%
75%
98%
86%
98%
87%
95% CI
[88%, 98%]
[46%, 91%]
[96%, 99%]
[58%, 96%]
[97%, 99%]
[84%, 90%]
95% CI of the median
of orientation errors (radian)
[0.20, 0.27]
[0.29, 0.46]
[0.21, 0.28]
[0.33, 0.42]
[0.12, 0.13]
[0.15, 0.18]
Figure S2c in the supplementary material). Soft fingertips provide higher friction and deform
when contact happens (compliance), increasing the contact area between the finger and the
object. The error distribution in Figure 2C shows using soft fingers doesn’t affect performance
on train objects but improves generalization to OOD objects. Results in Table 1 confirm the
findings – success rate on OOD objects increases from 45% to 55% when switching from rigid
to soft fingertips. Qualitatively, we noticed that soft fingertips behave less aggressively than
rigid fingertips resulting in smoother object motion. We, therefore, use soft fingertips in the rest
of the experiments. It’s worth noting that although the controller was trained using a rigid-body
simulator, its performance does not degrade when applied to soft fingertips.
The reorientation error can result from imperfect training, sim-to-real gap, generalization
gap, or failures at detecting if the object is at the target orientation, which triggers the controller
to stop. In Figure 2D, we report the error distribution in simulation. Although the trained
controller is not perfect in simulation, the errors in simulation follow the same trend as in the
real world (Figure 2C) but are lower, indicating some sim-to-real gap. As shown in Table 1,
the performance gap between the simulation and the real world is smaller with a relaxed error
threshold of 0.8 radians than with a threshold of 0.4 radians, illustrating the difficulty in precise
reorientation. For some objects (#1, #12), the error distribution is bi-modal both in simulation
12
—————


<!-- page 13 (ocr) -->
and the real world. The test runs with high errors largely result from incorrect detection of when
to stop. For instance, object #12 appears nearly symmetric in the point cloud representation,
which often leads to errors close to 180◦. Although it is hard to quantitatively disentangle errors
originating from incorrect action prediction and the stopping criterion, based on our experience
with the system, we hypothesize that the latter contributes more which is supported by the
analysis in Supplementary Discussion (see Discussion on precise manipulation).
Object reorientation on different supporting materials
Changing the table surface changes the dynamics of object motion. We tested if our controller
is robust to a diverse set of materials: a rough cloth (M1), a smooth cloth (M2), a slippery
acrylic sheet (M3), a bathtub mat with perforations resulting in non-stationary object dynamics
depending on the object’s position on the mat (M4), and a door mat with uneven texture (M5).
The materials have different surface structures, roughness, and friction, leading to different
system dynamics. We evaluate with one in-distribution object (object #5) and one out-of-
distribution object (object #10). Figure 2F and Figure 2G show that our controller performs
similarly on different supporting materials, demonstrating its robustness.
Towards object reorientation in air
As the controllers discussed above were trained with a supporting surface, when the supporting
surface was removed, the manipulator consistently dropped the object resulting in failures. Prior
work used a specialized training procedure of configuring the object in a good pose at the start
of each training episode and a manually designed gravity curriculum (7) to learn in-air (without
supporting surface) reorientation controllers. Consequently, it was necessary to train separate
controllers for reorientation with a supporting surface and in the air. It is preferable to have
a single controller capable of in-air reorientation and use the supporting surface, if available,
13


<!-- page 14 (ocr) -->
to recover from any dropping failures. We achieved this desideratum by employing a four-
fingered hand and designing a reward function that penalizes contact between the object and the
supporting surface to discourage the controller from using external support for reorientation.
When the controller is trained on a supporting surface with the proposed reward function, in-air
reorientation emerges.
Although both three and four-fingered hands can reorient objects on a supporting surface
(Figure 4A), only the four-fingered hand was capable of in-air reorientation (Figure 4B). We
hypothesize this to be the case because, with four fingers, more finger configurations can re-
orient the object, making it easier for policy optimization to find one solution. Furthermore,
we hypothesize that the redundancy in the number of fingers makes the system more robust to
errors in action prediction.
SO(3) object reorientation in air
Figure 1B shows how our controller trained in simulation reorients different real-world objects
in the air. In-air reorientation can fail if the object is not accurately reoriented or if the robot
drops the object. Because in-air reorientation is more challenging, it is possible that the con-
troller is less accurate at reorienting objects. On evaluation with two objects, we found the
distribution of orientation error in trials where the objects are not dropped (Figure 4C) to be
similar to reorientation with the supporting surface, indicating that the controller doesn’t lose
reorientation precision in the more challenging in-air scenario. In simulation analysis, we did
not notice any notable correlation between orientation error and the distance between the initial
and target orientations (Figure S12b in the supplementary material), indicating that the con-
troller performs similarly in the full SO(3) space.
Our controller performs dynamic reorientation. The median time for manipulation across
objects and randomly sampled orientation distances in the full SO(3) space is less than 7s (Fig-
14


<!-- page 15 (ocr) -->
0
2B
4B
6B
8B
10B
12B
0
0.2
0.4
0.6
0.8
1
Four fingers
Three fingers
Number of steps
Success rate
0
1B
2B
3B
4B
5B
6B
7B
8B
0
0.2
0.4
0.6
0.8
1
Four fingers
Three fingers
Number of steps
Success rate
1
2
3
4
5
6
7
8
9
10
11
12
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Object ID
Error (rad)
Rectangular cuboid
Cube
0
0.4
0.8
1.2
1.6
2
2.4
2.8
Object ID
Error (rad)
A
B
C
D
E
F
Fig. 4 Benefit and performance of reorientation with a four-fingered hand.(A): When
training a controller to reorient objects with a supporting surface, the three-fingered and four-
fingered hands achieve similar learning performance. (B): However, when we incentivize the
hands to lift the object during reorientation, the four-fingered hand outperforms the three-
fingered hand substantially. (C): We tested the controller performance with a four-fingered
hand in the air. We collected 20 non-dropping testing cases for one in-distribution object and
one out-of-distribution object. The error distribution is similar to that in the case of table-top
reorientation. (D) shows the distribution of the episode time both in simulation and the real
world. (E): We show the same controller’s performance on twelve objects with a supporting
surface. (F): We tested the controller on symmetric objects with a supporting surface. The con-
troller behaves reasonably well even though it was never trained with symmetric objects.
15
|_|
| |
rE
tS 2
2
*
9
I”
J
Ara
*
++
/
rr
¥
.
apr
.
J
+
rd
+
| |
|
28
0 On a supporting surface
35
-
© Simulation
B
@ In the air
= Real
52
pe
|
> =A
“
Eg
“
5
.
C16
©
o
.
5
Esl
.
.
:
G12
=
.
PB
0.8 BE
EHH
01.
.
Ki
oat 3A
E
5A
°
2)
i
i
oN HED $B
ia
bb
2
5
5
10
10
5
5
10
10
Object ID
Object ID
|_|
||
!
©


<!-- page 16 (ocr) -->
ure 4D), which makes it a fast in-air reorientation controller operating in the full SO(3) space.
Figure 4D also shows that the reorientation times in the real world are longer than in simulation,
which we believe is due to real-world contact dynamics being different from simulation.
Simulation analysis reveals that object dropping is the most notable source of errors (Figure
S12c). Dropping rates vary substantially across objects. Real-world results follow the same
trend. The dropping rate of a shape used in training, the truck (object #5), was 23%, much
lower than the dropping rate of 56% for an out-of-distribution duck-shaped object (#10). The
dropping rate for the duck object shape in the simulation was around 20% showing a sim-to-
real gap. However, it remains unclear if the difference in performance can be attributed to
the simulator being an approximate model of the real world or whether the object in the real
world is much harder to manipulate. This is because, even though the simulation and real-
world experiments used the object with the same shape, properties such as surface friction that
are critical in reorientation can be different. If an object is curved and has a smooth surface,
which is the case with the duck, small differences in friction can substantially change the task
difficulty. We chose to report results on the duck as it was used in prior work (23) and is among
the harder objects to reorient and thus also highlights the limitations of our controller.
If a table is present below the hand (for example, the setup shown in the third row of Figure
1B) and the object is dropped, we notice that our controller picks up the object and continues
reorienting – an instance of recovery from failures. It is possible that the reward term encour-
aging in-air reorientation might hurt on-table reorientation. However, the error distribution for
on-table reorientation with the updated reward function (Equation 6)(Figure 4E) is similar to
earlier on-table experiments. Moreover, although our controller is trained using objects with
asymmetry or reflective symmetry, which makes learning much easier, we noticed some gener-
alization to symmetric objects (Figure 4F, more discussion in Supplementary Discussion). The
in-air, on-table, and dropping recovery results demonstrate that it is possible to build a single
16


<!-- page 17 (ocr) -->
controller that works across different scenarios.
Qualitatively looking at the reorientation behavior, it might appear that the object is not
always moving toward the target orientation. One possibility is that the manipulator randomly
moves the object until it gets close to the target orientation by chance and then stops. To
rule out this possibility, we provide videos in Movie S1 showing that for the same initial but
different target orientation, the object motions are different. And for the same initial and target
orientation, object motions across trials are similar, which would not be the case if the object
was randomly being reoriented.
Generalization to objects in daily life
In previous experiments, we used 3D-printed objects for quantitative evaluation. However,
real-world objects have varying object dynamics due to differences in material properties, non-
uniform mass distribution, and other factors that can vary across the object surface. To test
the generalization ability of our controller on such objects, we conducted a qualitative evalu-
ation on a few household objects. Since we did not have the CAD (Computer Aided Design)
model of these objects to generate point clouds in target orientations, we used a free iPad App
called Scaniverse to scan the objects. Note that the scan was only required to specify the tar-
get orientation, and the scanned object cloud was imperfect (see Figure 5), resulting in noisy
goal specification. Figures 1B and 5 illustrate examples of reorienting such objects. The re-
sults illustrate that the controller exhibits a certain degree of robustness against noise in the goal
specification and some ability to generalize to new materials and shapes.
Comparison to prior works
Unfortunately, a strictly fair comparison with prior work is not possible as we make fewer as-
sumptions (such as no object-specific pose trackers, reorientation in full SO(3) space, and not
17


<!-- page 18 (ocr) -->
Fig. 5 Reorientation of real objects. Examples of reorienting real objects that were not 3D
printed using a four-fingered and a three-fingered manipulator.
being quasi-static), and there are substantial differences in hardware/sensing. Nevertheless, to
contextualize our research within the existing literature, we present an approximate comparison
to the closest work that reported reorientation results on a duck-shaped object with a downward-
facing but under-actuated hand of different morphology and mechanical properties (23). They
reported a success rate of 60% (3 out of 5 tests) for reorienting the duck quasi-statically (reori-
entation time of more than 70s compared to ∼7s for our controller) to within 0.1 radians, but
only in a subset of the SO(3) space (rotation only along two axes). Further, they used a precise
18
2
A
A
A
a
LAA
LY
1 AA-
1611881
84 Lb Gh 681
PEE
1EE
A111 5811
VED
558 BOB


<!-- page 19 (ocr) -->
object-specific pose tracker (error < 2 degrees or 0.034 radians). If we assume perfect stopping
criteria (the agent stops reorientation if the object is within 0.1 radians of the target), then for
the duck-shaped object, we achieve a success rate of 71% when dynamically reorienting in the
full SO(3) space in simulation. Due to challenges in setting up precise stopping in the real
world, we could not run these evaluations in the real world. Even if we did, the differences in
material properties between the duck used by us and prior research (23) would make the com-
parison unfair. Comparing our simulation and their real-world results is also unfair. However,
the results indicate that with more assumptions, such as the precise stopping criterion, the per-
formance of our system improves. Improving the precision of our system without any additional
assumptions is an exciting avenue for future research.
The differences in experimental setups with other prior works (8, 9, 17, 25) and concurrent
work (36) are even larger. For instance, OpenAI’s work (8) reported results on reorientation
with a single object (no generalization), with a simple shape (cube), an upward-facing hand,
and an extensive sensing system consisting of three RGB cameras, a motion capture system,
and a different hand. Moreover, their success criterion was the number of times an object passes
through a target pose, and they never trained their controller to stop the object at the target pose,
which we experimentally found harder to learn. In the broader context of manipulation, the
ability to stop at the target pose is vital: If the robot uses a tool, it must reorient it to the desired
pose and hold the tool in that pose.
The focus of our work is not to increase the reorientation performance on a single object;
rather, our work expands the scope of object reorientation to operate in more general and prag-
matic settings. The result is a single controller for reorienting multiple objects, evidence of some
generalization to new objects, and dynamic reorientation in the air without a highly specialized
perception system. At the same time, there remains ample scope for improving performance,
and we hope that our conscious use of open-source hardware, commodity sensing, computing,
19


<!-- page 20 (ocr) -->
and fast-learning framework (Figure 6 and Figure 7) will facilitate future research in enhancing
performance and comparing results.
Discussion
Solving contact-rich tasks typically requires optimizing the location at which the robotic ma-
nipulator contacts the object (4, 37, 38). One would assume predicting the contact location
requires knowledge of the object’s shape. However, inputs to the teacher policy have no infor-
mation about object shape, yet it could reorient diverse and new objects. One possibility is that
the agent gathers shape information by integrating information across the sequence of touches
made by the fingers. However, the teacher policy is not recurrent, ruling out this possibility. The
surprising observation of reorientation without knowledge of shape was made by earlier work
in the context of a reorientation system in simulation (7). However, because real-world results
were not demonstrated, it remained unclear if such an observation was an artifact of the sim-
ulator or the property of the reorientation problem. With real-world evaluation, we have more
confidence that shape information may not be as critical to object reorientation as one might
apriori think. However, this is not to suggest that shape is not useful at all. The results show
that one can go quite far without shape information, but the performance, especially on pre-
cise manipulation and in generalization to new shapes, can likely be improved by incorporating
shape features into the teacher policy, an exciting direction for future research.
Typically, having more fingers introduces more optimization variables, making the opti-
mization problem harder in the conventional view. However, we have some evidence to the
contrary (Figure 4B). Having more fingers can make it easier for deep reinforcement learning
to find a solution, especially in challenging manipulation scenarios such as in the air, similar to
how over-parameterized deep networks find better solutions (a conjecture). We conjecture that
over-parameterized hardware results in a larger pool of good solutions (more ways to reorient
20


<!-- page 21 (ocr) -->
an object with more fingers), making it easier for current optimizers in deep learning to find a
good solution.
In designing the proposed system, we either devised or made several technical choices: two-
stage student training, representing both the camera recordings and proprioceptive readings as
a point cloud, sparse convolution neural network for real-time control, limited range of domain
randomization due to system identification, system identification using parallel GPU simulation,
use of soft material on fingertips, using a larger number of fingers instead of the conventional
wisdom of using fewer fingers. These choices, however, are not specific to in-hand reorientation
but can be applied to a broad spectrum of vision-based manipulation tasks involving rigid bod-
ies. We hope that the knowledge of these choices, along with a low-cost platform, can further
the goal of democratizing research in dexterous manipulation.
Limitations and Possible Extensions
Object reorientation with a downward-facing hand has
notable room for improving precision and reducing the drop rate. We hypothesize that one
possible cause for dropping objects is that the control frequency of 12Hz is not fast enough. The
robot dynamically manipulates the object, and it takes a fraction of a second to lose control. It
might be challenging to determine when the object is slipping from the fingers in real-time using
visual feedback at 12Hz. Feedback control at a higher frequency may mitigate such failures but
either requires more efficient neural network architectures or more processing power.
Another hypothesis for object dropping is missing information regarding whether the finger
is in contact with the object, if the object is slipping, or how much force is being applied. We
conjecture that explicit knowledge of contact, contact force, and other signals such as slip can
substantially improve performance. Currently, the robot relies purely on occluded vision obser-
vations to infer contacts. Augmenting the robot’s observation with touch sensors is therefore an
exciting direction for future investigation.
21


<!-- page 22 (ocr) -->
We also found that inaccurate prediction of rotational distance is another cause for impre-
cise object reorientation. The prediction of rotational distance is less accurate when the actual
rotational distance is less than 0.4 radians (see Discussion on precise manipulation in Supple-
mentary Discussion).
We hypothesize that generalization and precision can be improved by training on a larger ob-
ject dataset, investigating RGB sensing to complement depth sensing to capture fine geometric
structures and reduce noise, and integrating visual and tactile sensing to obtain more complete
point clouds. Further, there remains a sim-to-real gap that future research should investigate.
We used D’Claw manipulators in this work as it is open-source and low-cost. However,
many aspects of the D’Claw, such as the finger design and the number of fingers, are sub-
optimal. For instance, although we observed some robustness to the softness of fingertips,
different softness and skeleton designs can notably affect the longevity of fingertips. We man-
ually iterated over many soft fingertip designs, which was time-consuming. Similarly, the fin-
gertips have a hemispherical shape, quite different from humans and presumably not optimal.
The performance of the task can be improved by better hardware design: the shape of fingers,
the degrees of actuation on each finger, the placement of fingers, and the choice of materials.
Manually iterating over these choices is infeasible. A promising future direction is to utilize a
computational approach for automatically designing the hand for specific tasks (39).
In summary, we presented a real-time controller that can dynamically reorient complex and
new objects by any desired amount using a single depth camera. The system is both simple
and affordable, which aligns with the objective of making dexterous manipulation research
accessible to a wider audience.
22


<!-- page 23 (ocr) -->
Materials and Method
Given a random object in a random initial pose, the robot is tasked to reorient the object to a
user-provided target orientation in SO(3) space. We train a single vision-based object reorien-
tation controller (or policy) in simulation to reorient hundreds of objects. The controller trained
in simulation is directly deployed in the real world (zero-shot transfer). The choices in our
experimental setup have been made to support future deployment of reorientation in service of
tool use and on a mobile manipulator.
Object datasets
We use two object datasets in this work: Big dataset (B) and Small dataset
(S). B contains 150 objects from internet sources. S contains 12 objects from the ContactDB
(40) dataset. These two datasets do not have overlapped shapes. More details on the object
dataset are in Supplementary Methods.
Simulation setup
We use Isaac Gym (41) as the rigid body physics simulator. We train all
the policies on a table-top setup: hands face downward with a supporting table.
Success criteria
During training, the success criterion for reorienting an object acts as both a
reward signal and a criterion for success to end the episode. A straightforward success criterion
is judging whether an object’s orientation is close to the target orientation (orientation criterion).
However, a controller trained using this criterion tends to cause the object to oscillate around the
target orientation. To address this issue, the success criterion is expanded to explicitly penalize
finger and object movements. For further details on how we designed the success criteria for
training, please refer to Supplementary Methods.
23


<!-- page 24 (ocr) -->
Training the visuomotor policy
We model the problem of learning the controller, π, as a finite-horizon discrete-time decision
process with horizon length T. The policy π takes as input sensory observations (ot) and out-
puts action commands (at) at every time step t. Learning π using RL is data inefficient when
the observation (ot) is high-dimensional (for example, point clouds). The reason is that the
policy needs to simultaneously learn which features to extract from visual observations and
what are the high-rewarding actions. The problem would be simplified if one of these factors
were known: learning a policy via RL from sufficient state information would be much easier
than direct learning from sensory observations. Similarly, apriori knowledge of high-rewarding
actions would reduce the data requirements of learning from visual observations.
Prior work has employed this intuition to ease policy learning by decomposing the learning
process into two steps (7, 27, 28, 30). In the first step, a teacher policy is trained in simulation
with RL using low-dimensional state space that includes privileged information. In the case of
in-hand object reorientation, privileged information includes quantities such as fingertip veloc-
ity, object pose, and object velocity that can be directly accessed from the simulator but can
be challenging to measure in the real world. Because the teacher policy operates from a low-
dimensional state space, it can be more efficiently trained using RL. Next, to enable operation
in the real world, one can either train a perception system to predict the privileged informa-
tion (8,26) or train a second student policy to predict high-rewarding teacher actions from raw
sensory observations via supervised learning (7,27,28,30).
An underlying assumption of the two-stage training paradigm is that a low-dimensional
state for learning a teacher policy can be identified. Because there are no tools available to the-
oretically analyze if a particular choice of state space is sufficient for policy learning, selecting
the state inputs for the teacher policy is a manual process based on human intuition. At first,
object reorientation might seem to require knowledge of object shape since the controller must
24


<!-- page 25 (ocr) -->
reason about where to make contact. If object shape is necessary, then it will not be possible
to reduce depth observations into a low-dimensional state. However, past work found that even
without any shape information, it is possible to train RL policies to achieve good reorientation
performance on a diverse set of objects in simulation (7). Therefore, teacher-student training
can be leveraged to simplify the learning of object reorientation.
To deploy the policy in the real world, some prior works train a perception system to predict
the object pose (8,9). However, object pose is only defined with respect to a particular reference
frame. Choosing a common frame of reference across different objects is not possible. As a
consequence, pose estimators cannot generalize across objects. Therefore, we choose to train
an end-to-end student policy that takes as input the raw sensory observations and is optimized
to match the actions predicted by the teacher policy via supervised learning (42). Because
supervised learning is considerably more data efficient than RL, such an approach solves the
hard problem of learning a policy from raw sensory observations.
The teacher-student training paradigm has been used to learn object reorientation policy in
simulation from visual and proprioceptive observations (7). However, a separate policy was
trained per object. Secondly, it required more than a week to train the student vision policy for
a single object on an NVIDIA V100 GPU. We developed a two-stage student training (Teacher-
student2) framework (Figure 6) that substantially speeds up the vision student policy learning.
Using this framework, we were able to learn a vision policy that operates across a diverse set of
objects and generalizes to objects with different shapes and physical parameters.
Teacher policy: reinforcement learning with privileged information
The learning of teacher policy (πE) is formulated as a reinforcement learning problem where
the robot observes the current observation (oE
t ), takes an action (at), and receives a reward
(rt) afterward. A single policy (πE) is trained across multiple objects using proximal pol-
25


<!-- page 26 (ocr) -->
Teacher Policy
Student Policy
Action
+
Action
Student Policy
Physics Simulation
Rendering
Physics Simulation
Physics Simulation
Imitation Learning
Reinforcement Learning
Finetune
+
Action
Student Policy
Real World
robot state (position)
object pose
goal orientation
robot state (velocity)
object velocity
1. Teacher Policy Training
2.2 Student Policy Training - Stage 2
3. Real-world Deployment
2.1 Student Policy Training - Stage 1
SE(3) 
Transformation
SE(3) 
Transformation
SE(3) 
Transformation
Imitation Learning
Fig. 6 Teacher and two-stage student training framework. First, a teacher policy is trained
using reinforcement learning with privileged state information. Then, a student policy is trained
to imitate the teacher using synthetic and complete point clouds as input. The student policy is
further fine-tuned using rendered point clouds. During deployment, the student policy can be
directly used to control real robots.
26
[4
®
S
4
-
[3
gr
a B—
—I
~~,
Ad
a
®
Ad 3,2 —°
|
LLERE
TLIT
Ea
TLITE


<!-- page 27 (ocr) -->
icy optimization (PPO) (43) to maximize the expected discounted episodic return: πE∗=
arg maxπE E
T−1
t=0 γtrt . Since the observation ot at a single time step t does not convey
the full state information such as the geometric shape of an object, our setup is an instance of
Partially Observable Markov Decision Process (POMDP). However, for the sake of simplicity
and based on the finding that knowledge of object shape may not be critical as discussed above,
we chose to model the policy as a Markov Decision Process (MDP): at = πE∗(ot; at−1). The
policy also takes as input the previous action (at−1) to encourage smooth control.
Observation space
The inputs to the teacher policy, ot, include proprioceptive state informa-
tion, object state, and target orientation. Details are shown in Supplementary Methods.
Action space
We use position controllers to actuate the robot joints at a frequency of 12Hz.
The policy outputs the relative joint position changes at ∈R3G. Instead of directly using at,
we use the exponential moving average of actions ¯at = αat + (1 −α)¯at−1 for smooth control,
where α ∈[0, 1] is a smoothing coefficient. In our experiments, we set α = 0.8. Given the
smoothed action ¯at, the target joint position at the next time step is: qtgt
t+1 = qt + ¯at.
Reward
We first describe the reward function for the hand to reorient objects on a table. The
first term in the reward function (Equation 1) is the success criteria for the task. However, since
this only provides sparse reward supervision, the criteria by itself is insufficient for successful
learning. Therefore we add additional reward shaping (44) terms to encourage reorientation.
We use a dense reward term that encourages minimization of the distance (∆θt) between the
agent’s current and target orientation (Equation 2). We penalize the agent for moving fingertips
far away from the object (Equation 3). Without this term, fingers barely made any contact with
the object during training. We also penalize the agent for expending energy (Equation 4) and
for pushing the object too far from the robot’s hand (Equation 5) in which case the episode is
27
[=


<!-- page 28 (ocr) -->
also terminated. The reward terms are mathematically expressed as:
r1t =c11(Task successful)
sparse task reward
(1)
+c2
1
|∆θt| + ϵθ
dense task reward
(2)
+c3
G
i=1
pfi
t −po
t
2
2
keep fingertip close to the object
(3)
+c4| ˙qt|T|τt|
energy reward
(4)
+c51(∥po
t∥2
2 > ¯p)
penalty for pushing the object away
(5)
where c1, c2 > 0, and c3, c4, c5 < 0 are coefficients, 1 is an indicator function, ϵθ and ¯p are
constants, pfi
t is the fingertip position of ith finger, po
t is the object center position, τt is the
vector of the joint torques.
Using the aforementioned reward function, we were able to train reorientation policies that
used the support of the table. Next, to enable the more challenging behavior of reorienting
objects in the air, we added a penalty for the contact between the object and table (Equation 7)
and a penalty for using the penultimate joint instead of the fingertip for reorientation (Equation
8). Although the term in Equation 8 is not critical, it results in more natural-looking behaviors.
The overall reward function is:
r2t =r1t
(6)
+c61(object contacts with the table)
(7)
+c7
N
i=1
1(pfi
t,z > ¯pz)
(8)
where c6, c7 < 0 are coefficients.
28
I
2


<!-- page 29 (ocr) -->
Student policy - imitation learning from depth observations
The student policy (πS) is trained in simulation with the purpose of being deployed in the real
world. Since the sim-to-real gap for depth data is less pronounced than RGB data, we only
use the depth images provided by the camera along with readings from joint encoders. We
represent the depth data as a point cloud in the robot’s base link frame. To enable the neural
network representing πS to model the spatial relationship between the fingers and the object,
we express the robot’s current configuration by showing the policy a point cloud representing
points sampled on the surface of the fingers. We concatenate the point cloud obtained from the
camera along with the generated point cloud of the hand. We denote this scene point cloud as
P s
t .
Goal representation
Instead of providing the goal orientation as a pose which has general-
ization issues discussed above, the goal is represented as the object’s point cloud in the target
orientation P g. In other words, the policy sees how the object should look in the end (see the
top left of Figure 7A).
Observation space
The input to πS is the point cloud Pt = P s
t ∪P g (see Figure 7A). We
also did an ablation study on different ways to process the goal point cloud in Supplementary
Discussion S5.4. The results show that merging P s
t and P g before they are input to the network
leads to faster learning.
Architecture
The critical requirement for the vision policy is to run at a high enough fre-
quency to enable real-time control. For fast computation, we designed a sparse convolutional
neural network to process point cloud (Pt) using the Minkowski Engine (45) (see Figure 7A).
Compared to the architecture used in (7), our convolutional network has a higher capacity to
29


<!-- page 30 (ocr) -->
GRU
Linear
Linear
Linear
GELU
Linear
Linear
Linear
Linear
GELU
N=32
N=128
N=256
N=256
N=256
N=1
Sparse 3D CNN
Linear
GELU
Linear
Linear
Conv
BN
Max Pooling
Residual Block
Residual Block
{
Conv
BN
Residual Block
Residual Block
Linear
Linear
ReLU
K=3
S=2
C=3
K=2
S=2
Residual Block
Conv
BN
ReLU
Conv
BN
ReLU
K=3, S=1
K=3, S=1
K=3
S=2
C=3
C=3
x3, C=[64, 128, 256]
N=256
Sparse 3D CNN
Max Pool
Avg Pool
0
100
200
300
400
0
0.2
0.4
0.6
0.8
1
Two-stage student learning
Single-stage student learning
Wall clock time (h)
Success rate
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Teacher
Student, Stage 1
Student, Stage 2
Error (rad)
Percentage
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Teacher (Big dataset)
Teacher (Small dataset)
Error (rad)
Percentage
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Student, Stage 1 (Big dataset)
Student, Stage 1 (Small dataset)
Error (rad)
Percentage
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Student, Stage 2 (Big dataset)
Student, Stage 2 (Small dataset)
Error (rad)
Percentage
A
B
C
D
E
F
G
Fig. 7 Student policy learning. (A): Student vision policy network architecture. (B): Sparse 3D
CNN (Convolutional Neural Network) component of the policy network. (C): Proposed two-
stage student learning learns faster than single-stage student learning. The dashed vertical line
denotes the transition from the first to the second stage of student learning. The performance
dip happens due to a change in the distribution of point cloud inputs from being unoccluded
in the first stage to being occluded in the second. (D): Post-training evaluation of teacher and
student policies on the training dataset B. For each object, the initial and target orientations are
randomly sampled 50 times, resulting in 7500 samples. The empirical cumulative distribution
function (ECDF) of the orientation error is plotted. The results show that the students are
close to the teacher’s performance. (E), (F), (G): Comparing the ECDFs of the policies being
evaluated on dataset B and dataset S reveals small generalization gap for all the policies.
make it possible to learn the reorientation of multiple objects. Without direct access to object
velocity, it is necessary to integrate temporal information in πS, for which we use the gated
30
Rvs
AB;
he
—
Kd
JS
2s B08, --<
—
EY
SRR
g
>
ER
SRE
—
{
:
.
—
"
!
—- — <
at
v
||
14
a
=
,a
h
yo
=
|
yy
ll
:
A=
/
1
:
AN
/
1
|
I
/
1
:
a
/
|
y
/
'
:
/
/
1
H
I
/
[]
—
1
J
1
.
-
]
'
ET
]
le
H
~~
i
|
|
'
|
|
|
'
\
'
|
|
H
|
|
|
|
:
|
H
_
H
i.
H
-
|
|
|


<!-- page 31 (ocr) -->
recurrent unit (46) in the network.
Optimization
The student policy πS is trained using DAGGER (42) to imitate the teacher
policy πE.
Need for two-stage student learning
We found training a vision policy in simulation to be
slow, consuming 20+ days on an NVIDIA V100 GPU (Figure 7C). The main reason for slow
training is that the simulator performs rendering to generate a point cloud which consumes a
substantial amount of time and GPU memory. To reduce training time, we generated synthetic
point clouds by uniformly sampling points on the object and robot meshes used by the simulator.
The synthetic point cloud is also complete (no occlusions), which makes training easier. The
vision policy (πS
1 ) can be trained with synthetic point cloud in less than three days, which is
a 7× speedup (stage 1; see Figure 7C). However, the policy, πS
1 , cannot be deployed in the
real world because it operates on an idealized point cloud (no occlusions). Therefore, once the
student reaches high performance, we initiate stage 2, where the policy is finetuned with the
rendered point cloud. Such finetuning is quick in wall-clock time (around one day), and the
resulting policy (πS
2 ) performs better than training from scratch with rendered point clouds (see
Figure 7C). It is possible to further reduce the training time of the student policy by employing
visual pre-training with passive data that we discuss in Supplementary Discussion S5.5. An
additional benefit of the two-stage student policy training is that πS
1 is agnostic to the camera
pose. Therefore a policy from a new viewpoint (πS
2 ) can be quickly obtained by finetuning
using rendered point clouds from that camera pose. Training the vision policy from scratch is
not necessary.
Stage 1: details of synthetic point cloud
In stage 1, the simulation is not used for rendering
but only for physics simulation. We generate the point cloud for each link on the manipulator
31


<!-- page 32 (ocr) -->
and object by sampling K points on their meshes in the following way: let the point cloud of link
lj in the local coordinate frame of the link be denoted as P lj ∈RK×3. Given link orientation
(R
lj
t ∈R3×3) and position (p
lj
t ∈R3×1) at time step t, the point cloud can be computed in the
global frame, P
lj
t = P lj(R
lj
t )T + (p
lj
t )T. The point cloud representation of the entire scene is
the union of point clouds of all the links, the object being manipulated, and the object in the goal
orientation: P s
t =
j=M
j=1 P
lj
t where M is the total number of links (bodies) in the environment.
The point cloud P s
t can be efficiently generated using matrix multiplication.
Stage 2: details of rendered point cloud
In stage 2, at each time step, we acquire depth
images from the simulator and convert them into point clouds (which we call exteroceptive
point cloud) using the camera’s intrinsic and extrinsic matrices. Note that such a point cloud
is incomplete due to occlusions. We also convert the joint angle information into poses of the
links on the robot hand via forward kinematics and then generate the complete point cloud of
the robot (which we call proprioceptive point cloud). Note that such a proprioceptive point
cloud of a robot can be easily obtained in the real world in real-time from the joint position
readings. The policy input is the union of the exteroceptive and the proprioceptive point cloud.
Reducing the simulation to reality gap
There are two main sources of the gap between simulation and reality. The first one is dynamics
gap that arises from differences in the robot dynamics, the approximation in the simulator’s
contact model, and differences in object dynamics that depends on material properties such as
friction. The other source is perception gap caused by differences in statistics of sensor readings
and/or noise. One way to reduce these gaps is to train a single policy across many different
settings of the simulation parameters (domain randomization (32)). The success of domain
randomization hinges on the hope that the real world is well approximated by one of the many
32
U


<!-- page 33 (ocr) -->
simulation parameter settings used during training. The chances of such a match increase by
randomizing parameters over a larger range. However, excessive randomization may result in
an overly conservative policy with low performance (47). Therefore, we make design choices
that reduce the need for domain randomization and use it only when needed.
The perception gap is reduced by using only depth readings, which is more similar between
simulation and reality than RGB. To account for noisy depth sensing, we add noise to the sim-
ulated point cloud. The dynamics gap can be reduced by identifying simulation parameters
closest to the real world. While such identification is possible for the robotic manipulator, it
is infeasible for object dynamics that vary in material and mass distribution. Therefore, we
perform system identification on the robot dynamics and use only small randomization to ac-
count for unmodeled errors. We use a larger range of domain randomization on the object and
environment dynamics. To make the policy more robust to unmodeled real-world physics, we
apply random forces on the object during training which pressures the policy to reorient objects
while being robust to external disturbance. Lastly, to increase compliance and friction between
the object and the manipulator, we use soft fingertips. Such a choice makes the system more
tolerant of errors in control commands. Empirically we noticed that soft fingertips make the
robot less aggressive and reduce overshoot.
Identification of robot dynamics
We build the Unified Robot Description Format (URDF) model for the manipulator using its
CAD model, which provides accurate kinematics parameters, but the dynamics parameters,
such as joint damping and stiffness, must be estimated. One way of identifying dynamics
parameters is to leverage the equations of motion (or the dynamics model) and solve for the
unknown variables using a dataset of motion trajectories. The Isaac Gym simulator has a built-
in dynamics model. But because the simulator’s code is not open-source, we do not have access
33


<!-- page 34 (ocr) -->
to the precise dynamics model nor the gradients of dynamics parameters. We, therefore, used
a black-box approach that leverages the ability of Isaac Gym to perform massively parallel
simulations. We spawn many simulations with different dynamics parameters and use the one
that has the closest match to the real robot’s motion.
Let λi ∈Λ denote the dynamics parameter of the ith simulated robot (Cλi), where Λ de-
notes the entire set of dynamics parameter values over which search is performed. To evaluate
the similarity between the motion of Cλi and the real robot (Creal), we compute the score:
h(qCreal
A
(·), qCλi
A
(·)) = −qCreal
A
(·) −qCλi
A
(·)
2
2, where qC
A(·) represents the joint position tra-
jectories of a robot C given action commands A(·) which are detailed in Supplementary Meth-
ods. The closer the motion of the simulated robot is to that of the real world, the higher the score
will be. We use the black-box optimization method of Covariance Matrix Adaptation Evolu-
tion Strategy (CMA-ES) (48), an instance of evolutionary search algorithms, to determine the
optimal dynamics parameter: λ∗= arg maxλ∈Λ h(qCreal
A
(·), qCλ
A (·)). Note that it might be im-
possible to find a simulated robot that exactly matches the real robot due to the approximate
parameterization of real-world dynamics in simulation and the stochasticity in the real-world
resulting from actuation/sensing noise. More details on the identification are in Supplementary
Methods.
Real-world deployment
Real-world observation
It includes the joint positions of each motor in the manipulator and
the depth image from a RealSense camera. Details how the joint positions and depth image are
converted into a unified point cloud input can be found in Supplementary Methods.
Stopping criteria
To automatically stop the robot, we train a predictor that re-uses features
from the policy network to predict |∆θt| (see Figure 7A). The robot is stopped when ∆θpred
t
< ¯θ
34


<!-- page 35 (ocr) -->
and ||at|| < ¯a.
More details on the stopping criteria, the real-world experimental setup, and the procedure
for quantitative evaluation are in Supplementary Methods.
35


<!-- page 36 (ocr) -->
List of Supplementary Materials
The supplementary PDF file includes:
Supplementary Methods
Supplementary Discussion
Figs. S1 to S14
Tables S1 to S3
Other Supplementary Materials for this manuscript include the following:
Movies S1 to S2
36


<!-- page 37 (ocr) -->
References
1. M. T. Mason, J. K. Salisbury, and J. K. Parker, Robot hands and the mechanics of manipu-
lation.
The MIT Press, 1989.
2. J. K. Salisbury and J. J. Craig, “Articulated hands: Force control and kinematic issues,” The
International journal of Robotics research, vol. 1, no. 1, pp. 4–17, 1982.
3. D. Rus, “In-hand dexterous manipulation of piecewise-smooth 3-d objects,” The Interna-
tional Journal of Robotics Research, vol. 18, no. 4, pp. 355–381, 1999.
4. I. Mordatch, Z. Popovi´c, and E. Todorov, “Contact-invariant optimization for hand manip-
ulation,” in Proceedings of the ACM SIGGRAPH/Eurographics symposium on computer
animation, 2012, pp. 137–144.
5. Y. Bai and C. K. Liu, “Dexterous manipulation using both palm and fingers,” in 2014 IEEE
International Conference on Robotics and Automation (ICRA).
IEEE, 2014, pp. 1560–
1565.
6. V. Kumar, Y. Tassa, T. Erez, and E. Todorov, “Real-time behaviour synthesis for dynamic
hand-manipulation,” in 2014 IEEE International Conference on Robotics and Automation
(ICRA).
IEEE, 2014, pp. 6808–6815.
7. T. Chen, J. Xu, and P. Agrawal, “A system for general in-hand object reorientation,” in
Conference on Robot Learning.
PMLR, 2022, pp. 297–307.
8. O. M. Andrychowicz, B. Baker, M. Chociej, R. J´ozefowicz, B. McGrew, J. Pachocki,
A. Petron, M. Plappert, G. Powell, A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder,
L. Weng, and W. Zaremba, “Learning dexterous in-hand manipulation,” The International
Journal of Robotics Research, vol. 39, no. 1, pp. 3–20, 2020.
37


<!-- page 38 (ocr) -->
9. OpenAI, I. Akkaya, M. Andrychowicz, M. Chociej, M. Litwin, B. McGrew, A. Petron,
A. Paino, M. Plappert, G. Powell, R. Ribas et al., “Solving rubik’s cube with a robot hand,”
arXiv preprint arXiv:1910.07113, 2019.
10. A. Nagabandi, K. Konolige, S. Levine, and V. Kumar, “Deep dynamics models for learning
dexterous manipulation,” in Conference on Robot Learning. PMLR, 2020, pp. 1101–1112.
11. N. Furukawa, A. Namiki, S. Taku, and M. Ishikawa, “Dynamic regrasping using a high-
speed multifingered hand and a high-speed vision system,” in Proceedings 2006 IEEE In-
ternational Conference on Robotics and Automation, 2006. ICRA 2006.
IEEE, 2006, pp.
181–187.
12. T. Ishihara, A. Namiki, M. Ishikawa, and M. Shimojo, “Dynamic pen spinning using a high-
speed multifingered hand with high-speed tactile sensor,” in 6th IEEE-RAS International
Conference on Humanoid Robots.
IEEE, 2006, pp. 258–263.
13. V. Kumar, A. Gupta, E. Todorov, and S. Levine, “Learning dexterous manipulation policies
from experience and imitation,” arXiv preprint arXiv:1611.05095, 2016.
14. B. Calli and A. M. Dollar, “Vision-based model predictive control for within-hand preci-
sion manipulation with underactuated grippers,” in 2017 IEEE International Conference on
Robotics and Automation (ICRA).
IEEE, 2017, pp. 2839–2845.
15. B. Sundaralingam and T. Hermans, “Relaxed-rigidity constraints: kinematic trajectory op-
timization and collision avoidance for in-grasp manipulation,” Autonomous Robots, vol. 43,
no. 2, pp. 469–483, 2019.
16. H. Van Hoof, T. Hermans, G. Neumann, and J. Peters, “Learning robot in-hand manipula-
tion with tactile features,” in 2015 IEEE-RAS 15th International Conference on Humanoid
Robots (Humanoids).
IEEE, 2015, pp. 121–127.
38


<!-- page 39 (ocr) -->
17. S. Abondance, C. B. Teeple, and R. J. Wood, “A dexterous soft robotic hand for delicate in-
hand manipulation,” IEEE Robotics and Automation Letters, vol. 5, no. 4, pp. 5502–5509,
2020.
18. A. Bhatt, A. Sieler, S. Puhlmann, and O. Brock, “Surprisingly robust in-hand manipulation:
An empirical study,” Robotics: Science and Systems (RSS), 2021.
19. B. Calli, A. Kimmel, K. Hang, K. Bekris, and A. Dollar, “Path planning for within-hand
manipulation over learned representations of safe states,” in International Symposium on
Experimental Robotics.
Springer, 2018, pp. 437–447.
20. H. Zhu, A. Gupta, A. Rajeswaran, S. Levine, and V. Kumar, “Dexterous manipulation
with deep reinforcement learning: Efficient, general, and low-cost,” in 2019 International
Conference on Robotics and Automation (ICRA).
IEEE, 2019, pp. 3651–3657.
21. A. Rajeswaran, V. Kumar, A. Gupta, G. Vezzani, J. Schulman, E. Todorov, and S. Levine,
“Learning complex dexterous manipulation with deep reinforcement learning and demon-
strations,” Robotics: Science and Systems (RSS), 2017.
22. G. Khandate, M. Haas-Heger, and M. Ciocarlie, “On the feasibility of learning finger-
gaiting in-hand manipulation with intrinsic sensing,” in 2022 International Conference on
Robotics and Automation (ICRA).
IEEE, 2022, pp. 2752–2758.
23. A. S. Morgan, K. Hang, B. Wen, K. Bekris, and A. M. Dollar, “Complex in-hand manip-
ulation via compliance-enabled finger gaiting and multi-modal planning,” IEEE Robotics
and Automation Letters, vol. 7, no. 2, pp. 4821–4828, 2022.
24. R. Jeong, J. T. Springenberg, J. Kay, D. Zheng, Y. Zhou, A. Galashov, N. Heess, and
F. Nori, “Learning dexterous manipulation from suboptimal experts,” in Conference on
Robot Learning.
PMLR, 2020, pp. 915–934.
39


<!-- page 40 (ocr) -->
25. L. Sievers, J. Pitz, and B. B¨auml, “Learning purely tactile in-hand manipulation with a
torque-controlled hand,” in 2022 International Conference on Robotics and Automation
(ICRA), 2022, pp. 2745–2751.
26. A. Allshire, M. MittaI, V. Lodaya, V. Makoviychuk, D. Makoviichuk, F. Widmaier,
M. W¨uthrich, S. Bauer, A. Handa, and A. Garg, “Transferring dexterous manipulation from
gpu simulation to a remote real-world trifinger,” in 2022 IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems (IROS).
IEEE, 2022, pp. 11 802–11 809.
27. D. Chen, B. Zhou, V. Koltun, and P. Kr¨ahenb¨uhl, “Learning by cheating,” in Conference on
Robot Learning.
PMLR, 2020, pp. 66–75.
28. G. B. Margolis, T. Chen, K. Paigwar, X. Fu, D. Kim, S. Kim, and P. Agrawal, “Learning to
jump from pixels,” in Conference on Robot Learning.
PMLR, 2022, pp. 1025–1034.
29. A. Kumar, Z. Fu, D. Pathak, and J. Malik, “Rma: Rapid motor adaptation for legged
robots,” Robotics: Science and Systems (RSS), 2021.
30. J. Lee, J. Hwangbo, L. Wellhausen, V. Koltun, and M. Hutter, “Learning quadrupedal loco-
motion over challenging terrain,” Science robotics, vol. 5, no. 47, p. eabc5986, 2020.
31. J. Xu, T. Aykut, D. Ma, and E. Steinbach, “6dls: Modeling nonplanar frictional surface
contacts for grasping using 6-d limit surfaces,” IEEE Transactions on Robotics, vol. 37,
no. 6, pp. 2099–2116, 2021.
32. J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel, “Domain random-
ization for transferring deep neural networks from simulation to the real world,” in 2017
IEEE/RSJ international conference on intelligent robots and systems (IROS).
IEEE, 2017,
pp. 23–30.
40
