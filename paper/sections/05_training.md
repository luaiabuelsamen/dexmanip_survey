## 5. How policies are trained

### 5.1 The design space

A dexterous policy is defined by what supervises it, and four sources are in use across the
corpus's 112 method rows: a reward function supervises reinforcement learning, a human
demonstration supervises imitation, a human reference trajectory supervises a physics-based
tracker, which is imitation with a simulator in the loop, and nothing supervises a model-based
planner, which is handed a cost and a model instead.

The labels do not partition the corpus. Of the 112 method rows, 53 carry the tag `RL`, 27 `BC`, 23
`distillation`, 18 `VLA`, 14 `teleop-system`, 14 `diffusion`, 10 `data-collection`, 8 `flow`, 6
`RL+demo`, 6 `trajopt`, 5 `MPC`, 4 `grasp-synthesis` and 2 `world-model`. The tags sum to far more
than 112 because most methods published since 2024 sit on two branches at once. Figure 4 draws the
tree and the cross-links. Table 7 is the row-by-row version of the same thing, and is the table to
scan when looking for work comparable to your own.

What the deployed policy looks like once training is done matters more than the name a paper
gives itself, and on that axis the field has converged hard. Section 5.7 shows why.

{{figure:fig4_taxonomy}}

### 5.2 Reinforcement learning

#### 5.2.1 The standard recipe

Fifty-nine of the 112 method rows learn from a reward. Forty-eight name PPO as the algorithm, and
the next most frequent, DAPG, appears four times. Forty-three run their own experiments in a
GPU-parallel simulator from the Isaac family or Genesis, and 36 do both. Only 31 rows state an
environment count, with a median of 8192 and a maximum of 64000. Twenty-three rows distil a
privileged teacher into a deployable student, and 16 combine all three of PPO, a GPU simulator and
distillation. That 16-row intersection is the recipe as it is actually practised.

The hand is almost always an Allegro. It appears in 35 of the 112 method rows and in 17 of the 31
reorientation rows, ahead of Shadow at 21 and 6 and LEAP at 12 and 4.

Privilege is handled two ways. `openai_dexterity_2018` gives the value network object and target
orientation, joint angles, joint velocities and object velocities the policy never sees, with a
footnote recording that current object orientation was left out of the policy inputs by accident,
and `dextreme_2022` uses the same asymmetric critic with a 2048-unit LSTM against the actor's
1024. `hora_2022` instead compresses nine privileged object properties into an eight-dimensional
vector regressed from 30 steps of proprioception, and `visual_dexterity_2022` distils twice, from
a state teacher to a synthetic point cloud and then to a rendered one, for a fivefold speedup.

Domain randomisation is the part of the recipe with the least discipline.
`openai_rubiks_cube_2019` made it adaptive, pushing each range boundary out when performance at
that boundary exceeds 20 successes and pulling it in below 10, and `dextreme_2022` reproduced the
mechanism with a 256-sample queue and 40 percent of environments dedicated to boundary evaluation.
Both publish the discovered ranges. Below that standard, two shipped configurations disagree with
their own papers about what was randomised: `hora_2022` states a joint-noise range of U(0, 0.005)
against a shipped `jointNoiseScale` of 0.02, in a commit its own README says is not the one that
reproduces the paper, and `penspin_2024` zeroes the disturbance force its appendix describes. `dexpbt_2023`'s `randomize: False` is not a third case: it is the
IsaacGymEnvs default and agrees with the paper's statement that randomisation was not used here.

#### 5.2.2 Reward engineering

Table 5 puts the 21 in-hand reorientation methods against nine recurring term families and marks
each cell by where the term was found: in the paper, in the code, in both, or in the code with
every shipped configuration setting its weight to zero.

{{table:table5_rewards}}

The families are not equally popular. Nineteen of 21 methods have a goal or rotation tracking
term, which is the task. Thirteen penalise effort as torque, work or joint velocity, 13 pay a
sparse success bonus, 11 penalise object velocity and 10 penalise a drop. Eight penalise deviation
of the hand from a canonical grasp pose, a family the plan for this table did not anticipate and
which had to be added. Six penalise action rate or magnitude, five reward closing the distance
from fingertips to the object, and four carry a contact or force mark at all.

Three cells an earlier draft marked `code` are blank in it, because in each the term is in the
released code with every shipped configuration setting its weight to zero: `dextreme_2022`'s
`timeout_rew` and `dexpbt_2023`'s fall penalty through `fallPenalty: 0.0`, and `penspin_2024`'s
`action_penalty_scale: 0.0`. Marking them `code` would tell a reader the code optimises something
the paper does not state. They carry the mark `code (0)` in `corpus/reward_matrix.json`, with the
config key and value; section 5.8 says why the distinction matters.

Three of the four contact marks are the finding, not four. `anyrotate_2024` scores good and bad
fingertip contacts, `poise_2026` rewards a friction-cone wrench margin, and
`force_grasp_sim2real_2026` tracks a commanded grasp force. The fourth, `visual_dexterity_2022`,
penalises the *object* touching the table, a task-shaping term against using the table as a third
finger rather than a hand-object term, and its `pen_tb_contact` flag defaults to `False` with no
shipped config setting it true. Three of 21 in-hand reorientation methods, then, put a hand-object
contact or force quantity in the reward, and none puts interpenetration in it. `teledexter_2026`
penalises interpenetration with a differentiable signed-distance term, but during offline
reference construction, not in the policy's reward. Across all 112 method rows, 85 do not address
penetration at all, 5 constrain it, 3 measure it, 3 penalise it and 16 say nothing either way. The
physical quality of the contact is not something this literature optimises.

Term counts range from one to ten. `demostart_2024` gives a single binary terminal reward of 1 and
lets a curriculum over demonstration states do the shaping. `anyrotate_2024` and `viserdex_2026`
each publish ten weighted terms. `viserdex_2026` is the cleanest specification in the table, with
every term, weight and equation in one appendix table, and a statement that the same weights are
used for every object.

Weights are frequently unrecoverable. Three of the 21 rows give no numeric weight that survives
PDF conversion, because the equation blocks are images, which is a limit of this survey and is
recorded as such. `robot_synesthesia_2023` is a worse case. Its six coefficients are described
only as "tuned hyper-parameters" and no number is printed anywhere in the paper, so the reward it
reports cannot be reconstructed by anyone. `dexremoe_2025` names an angular-velocity penalty
weight in prose with no entry in its hyperparameter table, and `dextrack_2025` names an affinity
reward that is missing from its weight table.

#### 5.2.3 Curricula, populations and machine-written rewards

Curricula in this literature relax physics or tighten tolerances. `dexpbt_2023` tightens a success
tolerance from 0.075 to 0.01 by a factor of 0.9 every 3000 environment steps once three successes
are logged, and `maniptrans_2025` starts at zero gravity and high friction and restores both while
narrowing a fingertip threshold from 6 cm to 4 cm. `dexmachina_2025` attaches virtual
spring-damper controllers to the object, lets them do the task at first, then decays their gains
to zero. The two that ablate the curriculum report it is load-bearing: `rotateit_2023` sets its
rotation-penalty weight to zero and ramps it to −0.1, because applying it from the start makes the
policy learn only to hold the object still, and `viserdex_2026`, whose performance-based
curriculum runs over regularisation weight, action latency and time between successes, fails
completely without the regularisation component.

Population-based training appears once. `dexpbt_2023` runs populations of 8, 16 and 32 agents,
splits them 30/40/30, mutates the middle and replaces the bottom with mutated copies of the top,
each float hyperparameter multiplied or divided by a factor drawn from U(1.1, 1.5) with
probability 0.2. It reports 30 hours on a single V100 for a five-billion-transition single-arm
run, and 0.32 trillion environment steps for its largest population.

`eureka_2023` has GPT-4 write the reward function directly, constrained to return a total and a
dictionary of named components, and feeds per-component statistics back between iterations. Its
appendix gives an example whose reward correlates at −0.26 with the human-written one and still
scores 1.45 on the human-normalised metric, the strongest argument in the corpus that hand-tuned
weights are not a ceiling. `dreureka_2024` moves the safety requirement into the prompt instead of
a penalty term, asking in words for a cube rotating at about 0.25 radians per second with fingers
penalised for leaving their initial pose. Neither can be checked against a file. Eureka's
generated rewards are written at run time to a gitignored directory and never committed, so the
reward behind any reported number cannot be recovered from the repository, though its README
documents the paper's budget of five iterations and sixteen samples as the default and marks the
shipped one-iteration block a fast-test preset. DrEureka's repository contains only the locomotion
and globe-walking trees, so its LEAP-hand reward has no code at all.

#### 5.2.4 Where reinforcement learning stalls

Reinforcement learning stalls on objectives that are not learnable as stated. `anyrotate_2024`
found the angular-velocity objective unlearnable in the multi-axis setting and replaced it with a
moving keypoint target. `rotateit_2023` reports that its multi-axis policy "does not converge when
training with only reinforcement learning" and adds an imitation loss against single-axis oracles.
`eureka_2023` cannot spin a pen from scratch and needs a pretrain-then-finetune split, with the
from-scratch ablation failing to complete one cycle. Section 5.4's contact-graph term exists
because of the general shape of the problem: contact moves the object off the reference, so return
goes down, so the policy learns not to touch the object.

It stalls on geometry too. `hora_2022` fails on objects under 4 cm across because the fingers
collide with each other. What it does not stall on is publication: the real-trial counts behind
these headlines are small enough that section 7.1 treats them as the reporting problem they are.

### 5.3 Learning from human data

#### 5.3.1 Teleoperation and retargeting

Table 6 lists the 30 corpus rows that describe a system for getting human motion onto a robot
hand, with the retargeting objective compressed to one clause each.

{{table:table6_teleop}}

Retargeting splits four ways. The dominant family matches task-space vectors between the human and
robot hands. `dexpilot_2020` set the pattern with a weighted squared distance between fingertip
vectors, switching weights of 1, 200 and 400 by whether a pair is within threshold, a
minimum-separation constant of 3 cm between primary fingers, and a regulariser toward the open
hand, solved online with SLSQP; `anyteleop_2023`, `open_television_2024`, `bunny_visionpro_2024`
and `ace_teleop_2024` all use the same formulation. The second copies joint angles where the
kinematics allow it, as `holo_dex_2022` does for index, middle and ring while solving the thumb by
inverse kinematics and discarding the pinky the Allegro does not have. The third learns the map
offline: `geometric_retargeting_2025` trains a per-finger network in three to five minutes against
motion-direction, coverage, flatness, pinch and collision criteria, then runs at 1 kHz against the
60 to 100 Hz of online optimisation, raising configuration-space coverage from 38 to 90 percent
and one-time grasp success from 55 to 87.5 percent. The fourth removes retargeting from the loop:
`dexumi_2025` builds an exoskeleton whose fingertip workspace is optimised to match the target
hand, then regresses encoder values straight to motor values.

The table's empty cells are the point. Only 12 of the 30 rows carry a latency cell at all, three
of those give no number, and only 7 state a rig cost. Where costs are stated they are low and
falling, from `holo_dex_2022`'s $399 headset through the $600 exoskeleton of `ace_teleop_2024` and
the $600 haptic glove of `doglove_2025` to the $4,000 backpack of `dexcap_2024` and the $6,000 rig
of `bidex_teleop_2024`. Latency is not one quantity: `dexpilot_2020`'s "about one second" and
`holo_dex_2022`'s "under 100 milliseconds" are end to end, while `geometric_retargeting_2025`'s 1
kHz and `anyteleop_2023`'s 9 to 10 ms retargeting are single stages and several cells give a
control rate. The column mixes the two, so its spread is not a range. Only 13 rows report how many
trajectories were collected, and only 7 report hours.

Where throughput is measured, human collection beats teleoperation by a wide margin.
`humanoid_policy_human_policy_2025` times a grasp demonstration at 3.79 seconds for a bare human
and 19.72 seconds through a teleoperated humanoid, and a pour at 4.81 against 37.31 seconds. It
attributes the gap to retargeting latency and to the workspace of a 7-DoF arm rather than to
anything about the hand.

#### 5.3.2 Imitation architectures

Four architectures cover the corpus. Action chunking came from `aloha_act_2023`, which predicts a
chunk of joint targets with a CVAE and combines overlapping chunks by exponentially weighted
ensembling, reaching 80 to 90 percent on fine bimanual tasks from about 50 demonstrations each.
Diffusion came from `diffusion_policy_2023`, which denoises an action sequence and reports a 46.9
percent average success improvement over LSTM-GMM, IBC and BET across 15 tasks. `dp3_2024` swaps
the image encoder for a small point-cloud encoder and reports 74.4 percent against 59.8 percent
across 72 simulated tasks, and 85.0 against 35.0 percent on four real tasks from 40 demonstrations
each. Flow matching is the 2024-onward default for large models and carries 8 of the 112 rows.
Discrete action tokens are the fourth, used by `openvla_2024` and `metis_2025`, and are the only
one of the four that needs no continuous head at all.

Data generation is a separate lever and is underrated. `dexmimicgen_2024` turns 60 human source
demonstrations into 21,000 simulated ones across 9 tasks and 3 embodiments, and a real Fourier GR1
with two Inspire hands reaches 90 percent from 40 generated demonstrations against 0 percent from
the 4 source ones. `dex1b_2025` iterates optimisation, a CVAE proposal model and a simulator
filter into roughly a billion synthetic grasps, and its CVAE baseline beats the prior best by 22
points.

#### 5.3.3 Human video without a robot

Seven rows train a dexterous-hand policy from video with no teleoperation at any stage.
`dexmv_2021` retargets 700 self-recorded demonstrations by matching palm-to-fingertip task-space
vectors and estimating actions by inverse dynamics, `videodex_2022` mines 965 trajectories from
EpicKitchens to pretrain a neural dynamic policy, and `dexvip_2022` goes further into the reward,
clustering 715 curated HowTo100M frames into one consensus grasp pose per object category and
adding it as a reward term. `okami_2024`, `human2sim2robot_2025` and `hudor_2024` work from a
single video each, and `wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

#### 5.3.4 The embodiment gap, and what closing it is worth

Three papers measure the gap directly rather than asserting it. `okami_2024` runs the same
reference-plan and warping pipeline with and without human body and hand retargeting, and the
version without it loses 75.0, 42.1, 82.0 and 74.0 points across four task and setting pairs. That
is the largest clean embodiment-gap number in the corpus.

`humanoid_policy_human_policy_2025` ablates two mitigations separately on the same vertical-grasp
task over 10 trials. The full method scores 4 out of 10. Removing the interpolation that slows
human trajectories by a factor of four drops it to 1 out of 10. Removing the unified
54-dimensional state space while keeping the slowdown drops it to 0 out of 10, because the policy
is handed a shortcut for telling the two embodiments apart. `egozero_2025` reports the sharpest
version of the same effect. Removing 3D augmentation drops every one of its seven tasks to 0 out
of 15, and substituting monocular depth for triangulated depth does the same, because the best
metric depth models it tested carry more than 5 cm of error. It also quantifies what its hand-pose
pipeline costs, at 1 to 2 cm of action-label error.

`objdex_2024` supplies the counterexample. It retargets only the wrist and lets reinforcement
learning discover finger motion, and its ablation that adds a fingertip-matching reward "does not
yield benefits and even leads to lower performance". Richer human correspondence is not uniformly
better, and this is the one result in the corpus that says so with an ablation.

### 5.4 Tracking a human reference with physics

Twelve method rows carry the `track-human-ref` task family. Eight track a human hand on an object
and are covered here; the other four sit at the edges, `human2sim2robot_2025` tracking only the
object's trajectory, `dexman_2025` retargeting bimanual video onto a full humanoid, and
`humanplus_2024` and `omnih2o_2024` tracking whole-body motion. A reference is retargeted onto the
robot and a policy trained to make the simulated body follow it: the reference supplies the
shaping reward engineering would otherwise have to invent, and the simulator the physical
consistency pure imitation lacks.

`physhoi_2023` is the origin of the reward form. It multiplies a body term, an object term, an
interaction-graph term and a contact-graph term, and reaches 95.4 percent success on GRAB against
27.0 percent for a DeepMimic baseline. The contact-graph term exists to stop the policy learning
not to touch the object. `omnigrasp_2024` replaces the action space with a pretrained latent
motion prior and reports 94.6 percent grasp success and 84.8 percent trajectory success on GRAB,
while stating outright that it omits penetration metrics.

`dextrack_2025` adds an imitation loss to PPO and mines its own demonstrations through a homotopy
search over easier neighbouring trajectories, reaching 46.70 and 65.48 percent on GRAB at loose
and strict thresholds against 38.58 and 54.82 for the best baseline. It has a penetration-depth
formula and applies it only to input references, never to its own rollouts, and presents tolerance
of "severe hand-object penetrations" as robustness. `maniptrans_2025` freezes a generalist hand
imitator and trains a per-task residual on top, reaching 58.1 percent single-hand and 39.5 percent
bimanual success on OakInk-V2. Its stance on contact is to raise the friction coefficient above
the real value rather than model skin deformation, and its real deployment is open-loop replay.

`dexmachina_2025` moves to Genesis with 12,000 environments and six hand URDFs, and drives the
object with virtual controllers that decay to zero. Its re-implementation of `maniptrans_2025`'s
curriculum does not beat no curriculum on its own setup, which is a direct disagreement between
two papers worth quoting in both directions. `dexplore_2025` drops the explicit retargeting stage
and treats the reference as soft guidance, with termination thresholds derived from the failure
rate, reaching 87.7 percent on GRAB with an Inspire hand.

`toporetarget_2026` is the only corpus method that quantifies penetration as an evaluation
quantity, reporting maximum depth and the fraction of frames past 2 mm, and constraining it during
retargeting with a 1 mm soft tolerance and a 30 mm hard bound. It reaches 87.5 percent on its own
pen-spinning set against 46.9 for the best baseline. It does not re-measure penetration after the
tracking policy runs, so the property it constrains is a property of the reference and not of the
behaviour.

That is the pattern across all eight. Penetration is handled at the reference, if at all, and
never at the rollout. `objdex_2024` completes the set with the only real-robot numbers among them,
from 100 percent on a microwave and a laptop down to 41.2 percent on a ketchup bottle over 20
trials each.

### 5.5 Generalist and vision-language-action policies

The finding is the size of the hand. Eighteen method rows carry the `VLA` tag. Eleven evaluate on
a multi-fingered hand and six report no hand result at all, `groot_n16_2025` naming no end
effector anywhere on its page. Seven of the eleven state a hand size, and that comparison has to
be made in actuated degrees of freedom rather than joints, for the reason section 3 opens with:
four are six, the Inspire RH56DFX among them actuating six of its twelve joints; one is twelve,
`dexora_2026`'s XHAND; and two are 21 and 22, `gr_dexter_2025`'s ByteDexter V2 and
`egoscale_2026`'s Sharpa Wave. Their median is 6. Of the 59 reward-learning rows, 48 state a
count, 38 of those are 16 or above, and their median is 16: an Allegro and a LEAP actuate 16, and
a Shadow actuates 20 of its 24 joints. Two generalist rows reach the band the
reinforcement-learning literature of section 5.2 works in, and the rest sit a factor of two or
three below it. An earlier version of this claim said that none reached it, which was true of the
eight rows scored on the hand-evaluation field and false of the two that were not scored.

The six with no hand result are parallel-jaw throughout (`pi0_2024`, whose released code encodes
each ALOHA gripper as one scalar, `pi05_2025`, `pistar06_2025`, `openvla_2024`, `helix_2025`,
which claims individual-finger control of a 35-DoF upper body with no success rate or trial count
for any task, and `gemini_robotics_2025`, whose Apollo hand appears in a figure caption with no
number attached). Its successor `gemini_robotics_15_2025` closed that gap with Apollo progress
scores, not success rates, of 0.74 down to 0.62 across five generalisation axes. `dexvla_2025` is
the borderline case the other way: a hand in one real-robot task family, grippers in the other
five and in all 91 pretraining tasks.

The released code also drifts. `groot_n1_2025`'s repository is a later N1.7 generation with a
different backbone, a different action horizon and embodiments the paper does not describe, and
`pi05_2025`'s supports only the flow-matching head, not the hybrid recipe the paper describes.

### 5.6 Model-based control as the non-learning baseline

Three corpus methods solve dexterous tasks without learning a policy, and they are the control
group the rest of this section lacks.

`pddm_2019` learns an ensemble of dynamics models and plans through it with an MPPI-style
optimiser, replanning every step. It needs 1 to 2 hours of data in simulation and 2 to 4 hours on
a real 24-DoF Shadow Hand. `mjpc_2022` removes the learned model too and samples ten rollouts per
step through MuJoCo itself, planning in 1 to 20 milliseconds. It reorients a cube with a Shadow
Hand in real time from scratch, and reports no success criterion, no trial count and no real-robot
result.

`pang_global_planning_2022` is the most substantial of the three. It proves that the randomised
smoothing implicit in reinforcement learning and an analytic log-barrier relaxation compute the
same local linear model of contact, then uses the analytic version inside a trajectory optimiser
and an RRT. Allegro in-hand rotation takes 19.59 seconds to optimise and its plate-pickup task
117.16 seconds of planning on a 16-core CPU, against the GPU-days of section 5.2, and it is the
only method here that imposes non-penetration as a hard constraint. Its own limitation is the
honest part: its 3D systems transfer to hardware far worse than its 2D ones, because the
quasi-dynamic assumption breaks and planned grasps miss contacts under a second-order solver.

### 5.7 Hybrids, and where the field has converged

The recurring shape is reinforcement learning in simulation distilled into a policy that looks
like an imitation policy, and it appears in four variants. The first distils a privileged teacher
into a vision student inside one paper, which is `hora_2022`, `visual_dexterity_2022`,
`rotateit_2023`, `robot_synesthesia_2023` and `viserdex_2026`. The second uses reinforcement
learning as a demonstration factory: `dextrack_2025` mines demonstrations with per-trajectory RL
and trains a generalist on them, `maniptrans_2025` does the same to build a 3.3K-episode dataset,
and `dexteritygen_2025` trains a diffusion controller on ten billion simulated grasp-to-grasp
transitions and projects a human teleoperator's coarse command onto it, taking four reorientation
tasks from 0 out of 20 under raw teleoperation to 12, 13, 10 and 9 out of 20. The third generates
data without reinforcement learning at all, which is `dexmimicgen_2024`, `dex1b_2025` and
`deximit_2026`; `dex1b_2025`'s row is classed as a dataset, so figure 4's leaf, which counts
method rows, holds the other two. The fourth wraps an RL policy in a residual, which is
`resdex_2024` at 88.8 percent over 3,200 objects in 12 GPU-hours.

The consequence is worth stating plainly. In the variants that dominate 2025 and 2026 work, the
reward is no longer the objective of the deployed policy. It is the objective of the process that
produced the deployed policy's training data. Reward engineering has moved upstream into data
curation, and every reward-shaping pathology in section 5.2 now reaches the shipped policy through
a dataset rather than a gradient.

### 5.8 What the released code says

Thirty-seven of the 112 method rows record a discrepancy between a paper and the code it released,
and all 37 released code, so they sit inside the 62 rows that released anything. They are not one
kind of thing. Ten are contradictions, where paper and code state different values or different
terms. Thirteen are limits of this survey's own parse, where the body or config that would settle
the question was never recovered and the row says so. Eight released code without the described
component in it, three are version skew against a later repository, and three are a paper
disagreeing with itself. An unclassified thirty-eighth, `groot_n16_2025`, ships a main branch one
generation later than the checkpoint its page describes.

Ten is the number to quote, eight at high confidence and two, `penspin_2024` and `omnih2o_2024`,
held at medium pending a direct read of the code. Ten of 62 is 16 percent, bounded on both sides:
a floor, because the census covers method rows only and `robopianist_2023`, whose row is a
benchmark, sums five reward terms against the three its Table 2 documents; a ceiling, because
seven accusations an earlier draft of this section made were withdrawn under adversarial review,
each with its reason recorded in the accused row's `mismatch_review` field. Among the 21
reorientation methods of Table 5, seven released a repository: four disagree with their paper, one
(`dreureka_2024`) ships no cube-rotation environment at all, one (`hora_2022`) is a later
generation its own README flags, and one (`eureka_2023`) was a default-value question the same
README settles.

The most consequential case is `physhoi_2023`. Its `compute_humanoid_reward` hardcodes the body
position-velocity error and both object rotation errors to zero, with the real computation
commented out beside them, and does so unconditionally rather than per dataset, while its Table 4
lists non-zero weights of 0.1 and 0.01 for those rotation terms on GRAB. The reward that produced
the paper's numbers never tracked object orientation: a method presented as tracking a 6-DoF
reference was, in the code that ran, tracking the object in position only, with body rotation and
body rotation-velocity still live. `omnigrasp_2024`, in the same file family, keeps its object
rotation term live and fails the other way, internally: `compute_pregrasp_reward_time` takes
weights as arguments and then hardcodes `w_pos, w_rot = 0.9, 0.1`.

Zeroed terms recur, and are not the same failure. A term present and zeroed is worse than a term
missing, because it survives a reader's check of the file, but only when the paper claims it.
`dexpbt_2023` sums eight components against the paper's four and multiplies `hand_delta_penalty`
by zero with the comment "currently disabled", a term the paper never claims, and its five named
weights are present at their stated values. `pianomime_2024`'s Table 3 states two weighted terms
while its environment sums roughly five unweighted ones, two of them inherited stubs returning
zero and a third, forearm collision, the paper never lists. `penspin_2024` ships `forceScale: 0.0`
against the disturbance force in its appendix, and its 96-dimensional observation carries no
tactile channel, which is also what its proprioception-only student should carry, hence the
medium confidence.

Weights drift. `dextreme_2022` states an action-delta penalty of −0.25 in Table 2 and ships −0.2
and −0.01 in its two DR yamls, neither matching. `visual_dexterity_2022`'s Eq. 8 penultimate-joint
penalty is absent from `dexenv/envs/rewards.py`, and its two configs disagree about the fall
distance. `unidexgrasp_2023` and `dexpoint_2022` ship rewards structured differently from their
equations, and `pddm_2019`'s Baoding reward carries a −10 wrist-height term Table 2 omits.

In 13 rows the repository does not settle the question, which is this survey's limit and not an
accusation. The reward code is C++ and outside the parse in `graspxl_2024`, whose configs expose
four velocity coefficients where the paper prints two, and in `artigrasp_2023`, whose two weight
sets are the two phases of a curriculum the paper documents. `dextrack_2025` ships several
unreconciled coefficient sets and which produced its headline table cannot be identified, and
`maniptrans_2025`'s learning rate and environment count match its own config, the differing values
being a README example's override and an unused fallback. `hora_2022` is the one repository that
discloses its own gap, telling the reader to check out tag v0.0.1. Elsewhere a paper disagrees
with itself: `aloha_act_2023`'s Algorithm 1 says MSE and its Section IV.C says L1, `dp3_2024`'s
prose says the network predicts noise while its config sets `prediction_type: sample`, and
`dexmachina_2025`'s multiplicative task reward, charged to its code in an earlier draft, is
printed in the paper.

A reward table is a claim about a training run and the code is a claim about a repository. Here
the two contradict each other in ten cases, in the other 27 the released artefacts do not settle
the question, and in exactly one, `hora_2022`, the repository says so itself. Read the reward
function before the reward table, and treat a printed weight as a hypothesis about the code.


### 5.9 The master table

Table 7's emptiest columns are the ones a reader most needs: only 31 rows state an environment
count, only 55 state how many real trials are behind the headline number, and only 32 state how
many unseen objects were tested. A mostly empty row is not a weak method, but it is one that
cannot be compared with any other row here.

{{table:table7_methods}}

<!--
FIGURE 4. Taxonomy of training paradigms. Drawn by tools/make_flow_tree.py from corpus/rows at
generation time; paper/figures/fig4_taxonomy.svg. This comment is the specification the drawn
figure should satisfy.

THE RULE, after the R3 review: a leaf label may assert only what its predicate tests. Three leaves
previously read a paradigm tag and then claimed an algorithm, a simulator or a student modality
the tag does not carry. They are now either re-predicated or renamed:
  - "PPO in a GPU-parallel simulator, no distillation stage" reads `algorithm` and `sim`, not the
    RL tag, so it no longer prints `pistar06_2025` (no simulator, parallel-jaw grippers) or claims
    privileged state of `physhoi_2023`, which has none. There is no privileged-observation field
    in the schema, so no leaf claims privileged state at all.
  - "plus teacher-student distillation" no longer says "to vision"; the five papers whose student
    really is a vision policy hang off it as an annotation, from the same list Sec. 5.7 names.
  - "synthetic demonstration generation" takes its membership from Sec. 5.7 rather than from the
    `data-collection` tag, which is mostly real human-capture rigs; those rigs are now their own
    leaf. Membership lists the prose also states are defined once, in the figure code.
  - The demonstration branch counts the union of `BC`, `diffusion` and `flow` (44), not their sum.
  - The reward branch counts `RL` and `RL+demo` together (59), so the "seeded by demonstrations"
    leaf is inside the branch it hangs from.
  - "no learned policy" counts the three papers that learn no policy, not the 11 rows carrying a
    trajopt or MPC tag; the other 8 use those methods inside a learned pipeline and the footer
    says so. Where a branch's leaves do not cover it, the branch prints "N of M in a leaf", and a
    truncated key list prints "and N more".
  - The human-reference branch's six leaves now partition its 12 rows exactly: `pgdm_2023`, whose
    task family is grasp and functional/tool, is out, and `dexman_2025`, `humanplus_2024` and
    `omnih2o_2024` are in a "whole-body humanoid" leaf matching Sec. 5.4's four edge cases.
    `physhoi_2023` and `omnigrasp_2024` stay under "no retargeting, reference already on the
    embodiment", which is what their notes support; the earlier plan to move them under "whole
    reference including fingers" and "object trajectory only" is superseded.

STILL TO DO.
1. THE CROSS-LINKS ARE MISSING AND THEY ARE THE POINT. The footer says the branches are not
   exclusive, then a strict tree is drawn. Draw the overlaps as dashed curves behind the nodes, in
   the muted accent colour, each labelled with one word:
     reward-branch distillation leaf  ->  demonstration-branch architecture tags   "distil"
     reward-branch PPO leaf           ->  synthetic demonstration generation       "generate"
     egocentric video leaf            ->  human-reference branch                   "retarget"
     human-reference branch           ->  demonstration-branch architecture tags   "distil"
     no-learned-policy branch         ->  reward-branch PPO leaf                   "smooth"
     teleoperated-on-robot leaf       ->  seeded by demonstrations                 "seed"
   The fifth carries `pang_global_planning_2022`'s proof that randomised smoothing, which is what
   a policy gradient does implicitly, and analytic log-barrier smoothing compute the same local
   model of contact. It is the only edge that is a theorem rather than a pipeline; draw it
   differently, for instance with a double dash.
2. THE ARCHITECTURE AXIS IS ABSENT. Under the human-demonstration branch, what supervises the
   policy and what shape the policy has are independent choices. Add four small tags, not full
   nodes: action chunking `aloha_act_2023`; diffusion `diffusion_policy_2023`, `dp3_2024`; flow
   matching `pi0_2024`, `groot_n1_2025`, `h_rdt_2025`, `unidex_2026`, `egoscale_2026`;
   autoregressive action tokens `openvla_2024`, `metis_2025`. Tag counts are 1, 14 and 8 for the
   first three from the `diffusion` and `flow` labels.
3. SCARCITY MUST BE LEGIBLE. Population-based training over hyperparameters holds one paper,
   `dexpbt_2023`, which the figure does not show; add it as an annotation off the PPO leaf with
   the count 1. Size or shade every leaf by its count so a reader sees without reading a number
   that the demonstration branch is wide, the non-learning branch is three single papers, and
   automated reward design is two.

Palette, dark-mode handling and font stack follow the other figures in paper/figures/. All counts
are recomputed from corpus/rows/*.json at generation time and never hardcoded, so the figure
cannot drift from the corpus.
-->
