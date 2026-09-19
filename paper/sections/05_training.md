# 5. Training a dexterous policy

## 5.1 Sources of supervision

A dexterous policy is defined by what supervises it, and four sources are in use across the
corpus's 112 method rows: a reward function supervises reinforcement learning, a human
demonstration supervises imitation, a human reference trajectory supervises a physics-based
tracker, which is imitation with a simulator in the loop, and nothing supervises a model-based
planner, which is handed a cost and a model instead.

The labels do not partition the corpus. Of the 112 method rows, 53 are tagged reinforcement
learning, 27 behaviour cloning, 23 distillation, 18 generalist or vision-language-action, 14
teleoperation systems, 14 diffusion, 10 data collection, 8 flow matching, 6 reinforcement learning
from demonstrations, 6 trajectory optimisation, 5 model-predictive control, 4 grasp synthesis and
2 world models. The tags sum to far more than 112 because most methods published since 2024 sit on
two branches at once. Figure 4 draws the tree and the cross-links. Table 7 is the row-by-row
version of the same thing, and is the table to scan when looking for work comparable to your own.

What the deployed policy looks like once training is done matters more than the name a paper gives
itself, and on that axis the field has converged hard. Section 5.5 shows why.

**What the tabulation does not record.** Table 7's emptiest columns are the ones a reader most needs:
only 31 rows state an environment count, only 70 state how many real trials are behind the headline
number, and only 39 state how many unseen objects were tested. The trial and unseen-object figures
are the audited ones, after section 7.1 recovered 15 trial counts and 7 unseen-object counts that the
notes carried and the extraction had dropped. A mostly empty row is not a weak method, but it is one
that cannot be compared with any other row here.

{{table:table7_methods}}

{{figure:fig4_taxonomy}}

## 5.2 Reinforcement learning

**The standard recipe.** Fifty-nine of the 112 method rows learn from a reward. Forty-eight name PPO as the algorithm, and
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
reproduces the paper, and `penspin_2024` zeroes the disturbance force its appendix describes.
`dexpbt_2023`'s `randomize: False` is not a third case: it is the IsaacGymEnvs default and agrees
with the paper's statement that randomisation was not used here.

**Reward engineering.** Table 5 puts the 21 in-hand reorientation methods against nine recurring term families and marks
each cell by where the term was found: in the paper, in the code, in both, or in the code with
every shipped configuration setting its weight to zero.

{{table:table5_rewards}}

The families are not equally popular. Nineteen of 21 methods have a goal or rotation tracking
term, which is the task. Thirteen penalise effort as torque, work or joint velocity, 13 pay a
sparse success bonus, 11 penalise object velocity and 10 penalise a drop. Eight penalise deviation
of the hand from a canonical grasp pose, a family the plan for this table did not anticipate and
which had to be added. Six penalise action rate or magnitude, five reward closing the distance
from fingertips to the object, and four carry a contact or force mark at all.

Three cells an earlier draft marked *code* print *code (0)* instead, because in each the term is
in the released code with every shipped configuration setting its weight to zero:
`dextreme_2022`'s timeout reward, `dexpbt_2023`'s fall penalty, and `penspin_2024`'s action
penalty. Marking them *code* would tell a reader the code optimises something the paper does not
state, and leaving them blank would hide a term that is in the file. The repository carries the
config key and the zero beside each of the three marks.

Only three of the four contact marks are the finding. `anyrotate_2024` scores good and bad
fingertip contacts, `poise_2026` rewards a friction-cone wrench margin, and
`force_grasp_sim2real_2026` tracks a commanded grasp force. The fourth, `visual_dexterity_2022`,
penalises the *object* touching the table, a task-shaping term against using the table as a third
finger rather than a hand-object term, and its table-contact flag defaults to off, with no shipped
config setting it true. Three of 21 in-hand reorientation methods, then, put a hand-object contact
or force quantity in the reward, and none puts interpenetration in it. `teledexter_2026` penalises
interpenetration with a differentiable signed-distance term, but during offline reference
construction, not in the policy's reward. Across all 112 method rows, 85 do not address
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

**Curricula, populations and machine-written rewards.** Curricula in this literature relax physics or tighten tolerances. `dexpbt_2023` tightens a success
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

**Where reinforcement learning stalls.** Reinforcement learning stalls on objectives that are not learnable as stated. `anyrotate_2024`
found the angular-velocity objective unlearnable in the multi-axis setting and replaced it with a
moving keypoint target. `rotateit_2023` reports that its multi-axis policy "does not converge when
training with only reinforcement learning" and adds an imitation loss against single-axis oracles.
`eureka_2023` cannot spin a pen from scratch and needs a pretrain-then-finetune split, with the
from-scratch ablation failing to complete one cycle. Section 5.3's contact-graph term exists
because of the general shape of the problem: contact moves the object off the reference, so return
goes down, so the policy learns not to touch the object.

It stalls on geometry too. `hora_2022` fails on objects under 4 cm across because the fingers
collide with each other. What it does not stall on is publication: the real-trial counts behind
these headlines are small enough that section 7.1 treats them as the reporting problem they are.

## 5.3 Learning from human data

**Teleoperation and retargeting.** Table 6 lists the 30 corpus rows that describe a system for getting human motion onto a robot
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

**Imitation architectures.** Four architectures cover the corpus. Action chunking came from `aloha_act_2023`, which predicts a
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

**Human video without a robot.** Seven rows train a dexterous-hand policy from video with no teleoperation at any stage.
`dexmv_2021` retargets 700 self-recorded demonstrations by matching palm-to-fingertip task-space
vectors and estimating actions by inverse dynamics, `videodex_2022` mines 965 trajectories from
EpicKitchens to pretrain a neural dynamic policy, and `dexvip_2022` goes further into the reward,
clustering 715 curated HowTo100M frames into one consensus grasp pose per object category and
adding it as a reward term. `okami_2024`, `human2sim2robot_2025` and `hudor_2024` work from a
single video each, and `wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

**The embodiment gap.** Three papers measure the gap directly rather than asserting it. `okami_2024` runs the same
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

**Tracking a human reference with physics.** Twelve method rows sit in the human-reference tracking family. Eight track a human hand on an
object and are covered here; the other four sit at the edges, `human2sim2robot_2025` tracking only
the object's trajectory, `dexman_2025` retargeting bimanual video onto a full humanoid, and
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

That is the pattern across all eight, and it is the reference-versus-rollout split in its sharpest
form. Penetration is handled at the reference, if at all, and never at the rollout. `objdex_2024`
completes the set with the only real-robot numbers among them, from 100 percent on a microwave and
a laptop down to 41.2 percent on a ketchup bottle over 20 trials each.

**The retargeting map, and what would close it.** Human data does not port across hands, and the map
is usually left unstated. Fifty-three method rows use human data and name 44 distinct hand strings
between them; twenty of those appear in Table 6 with a stated retargeting objective. The other 33
never say how the human motion reached the hand, and the objectives that are stated do not converge,
running from a fingertip keypoint-vector energy in `anyteleop_2023` through a per-joint regression
from exoskeleton encoders in `dexumi_2025` to no retargeting at all in `egozero_2025`. What would
close it is a retargeting benchmark in TopoRetarget's form `toporetarget_2026`, reporting contact
precision, contact alignment, maximum penetration and the share of frames past 2 mm, per hand and per
dataset.

## 5.4 Generalist and vision-language-action policies

The finding is the size of the hand. Eighteen rows carry the generalist tag. Fourteen of them
settle whether the reported evaluation ran on a multi-fingered hand. Eight of those fourteen did,
six report no hand result at all, and the remaining four never say, `groot_n16_2025` naming no end
effector anywhere on its page.

Five of the eight state a hand size, and that comparison has to be made in actuated degrees of
freedom rather than joints, for the reason section 3 opens with. Four are six, the Inspire RH56DFX
among them actuating six of its twelve joints, and one is twelve, `dexora_2026`'s XHAND. Their
median is 6. Two of the four rows that never settle the hand question do state a size, and both
are large: 21 for `gr_dexter_2025`'s ByteDexter V2 and 22 for `egoscale_2026`'s Sharpa Wave. Of
the 59 reward-learning rows, 48 state a count, 38 of those are 16 or above, and their median is
16: an Allegro and a LEAP actuate 16, and a Shadow actuates 20 of its 24 joints. So no row that
settles the question reaches the band the reinforcement-learning literature of section 5.2 works
in, and the two rows that reach it on paper are the two that never say whether the hand was in the
evaluation. An earlier version of this claim counted eleven rows as evaluating on a hand, which
mixed the settled eight with rows the notes leave open.

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

**The size of the gap, and what would close it.** The gap is size rather than absence. A generalist
policy that does touch a hand runs it at roughly a third of the actuation the reinforcement-learning
literature assumes, and the rows that never settle the question are the smaller half of the same gap.
What would close it is one dexterous-hand task inside the standard generalist suite, with the hand's
actuated degrees of freedom and its vendor printed beside the number.

## 5.5 Model-based baselines and hybrids

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

**Hybrids, and where the field has converged.** The recurring shape is reinforcement learning in simulation distilled into a policy that looks
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

In the variants that dominate 2025 and 2026 work, the reward is no longer the objective of the
deployed policy. It is the objective of the process that produced the deployed policy's training
data. Reward engineering has moved upstream into data curation, and every reward-shaping pathology
in section 5.2 now reaches the shipped policy through a dataset rather than a gradient.

## 5.6 Paper against released code

Thirty-eight of the 112 method rows record a disagreement between a paper and the code it
released, and all 38 released code, so they sit inside the 62 rows that released anything. They
are not one kind of thing. Nine are contradictions, where paper and code state different values or
different terms. Thirteen are limits of this survey's own parse, where the body or config that
would settle the question was never recovered and the row says so. Eight released code without the
described component in it, four are version skew against a later repository, and four are a paper
disagreeing with itself. The fourth version skew is `groot_n16_2025`, which ships a main branch
one generation later than the checkpoint its page describes.

Nine is the number to quote, eight at high confidence and one, `penspin_2024`, held at medium.
Nine of 62 is 15 percent, bounded on both sides: a floor, because the census covers method rows
only and `robopianist_2023`, whose row is a benchmark, sums five reward terms against the three its
Table 2 documents; a ceiling, because eight accusations an earlier draft of this section made were
withdrawn, seven of them under adversarial review and an eighth, `omnih2o_2024`, once writing to
its authors sent someone back to the evidence, each with its reason recorded in the accused row
beside the charge. Among the 21 reorientation methods of Table 5, seven released a repository and
four of those state something different from their paper, the other three being a missing
environment, a later generation and a default-value question their own READMEs settle.

Table 11 is the whole of the finding, in the form the finding is made: a public repository, the
commit `tools/fetch_code.py` cloned, the file inside it, and the two values. The repository and
the commit are the ones `corpus/code_manifest.json` records; the file is in the parsed copy under
`code/md/`, which is the same snapshot every other claim in this survey about that repository is
made from; `what the paper prints` names the table or equation the value was read from. No cell
states a cause, and none is a claim about what the work's authors did.

{{table:table11_codegap}}

The case with the most at stake is `physhoi_2023`, and it is four items. The repository is
`wyhuai/PhysHOI`, the commit is `6095c605e2`, the file is `physhoi/env/tasks/physhoi.py`, and
inside `compute_humanoid_reward` the object rotation error and the object rotation-velocity error
are set to `torch.zeros_like(ep)`, with the computation that would produce them commented out on
the same two lines. The paper's Table 4 gives those two terms weights of 0.1 and 0.01 for GRAB.
The paper does say that both are zero for BallPlay, which supplies no ball rotation; the zeroing
in the file is not conditioned on the dataset. In that file the object's orientation error is the
constant zero and its weight cannot change the reward, and the success criterion the paper scores
its 95.4 percent with is itself position-only, so a run of that file would not report the
difference either. Two documents say different things, and that is the whole of the claim.

Two more read the same way and are quicker. `dextreme_2022`'s Table 2 prints an action-delta
penalty weight of -0.25; at commit `aeed298638` of `isaac-sim/IsaacGymEnvs`,
`AllegroHandDextremeADR.yaml` sets `actionDeltaPenaltyScale: -0.2` and the ManualDR yaml beside it
sets -0.01. `pianomime_2024`'s Table 3 prints two weighted terms, at two thirds and one third; at
commit `c4abefac8d` of `sNiper-Qian/pianomime`, `_set_rewards` in
`single_task/piano_with_shadow_hands_res.py` sums five, and two of the five,
`_compute_energy_reward` and `_compute_fingering_reward`, compute a value and then end `return 0`
and `return 0.0`. The remaining six are in Table 11 in the same four parts, and every one of the
nine can be checked by opening the repository at the commit in that table.

**Nobody was written to first.** The authors of these nine works were not contacted before this
survey was posted. Ten letters were drafted, one per method, each quoting the claim, its evidence
and the sentences the survey would print, and each asking whether the reading was right; they are
in `outreach/` in the repository, unsent, so a reader can see exactly what every author would have
been asked. Publishing without them narrows what this section may say, and what it says is written
to the narrower form: a repository, a commit, a file, and two values. It attributes nothing to
intent, and a reader with a browser can confirm or refute any line of Table 11 without anyone's
agreement. Two limits come with that, and neither is a hedge. A repository at a fetched commit is
not the code that produced a paper's numbers: it may postdate that code, precede it, or have
diverged from it on a branch nobody tagged, and a snapshot cannot say which, so each line compares
a published document with one public artefact and claims nothing beyond the two. One work in this
corpus says exactly that about itself. `hora_2022`'s README sends a reader to tag `v0.0.1` rather
than to the default branch to reproduce the paper's numbers, which is why its row is classed
version skew and is not one of the nine: told which commit to read, this survey read it, and
nobody else was in a position to tell us, because nobody else was asked. The other limit is the
remedy. Every one of the nine is correctable in public, and an author who shows that the file says
something other than what Table 11 prints, or that the fetched commit is not the one behind their
numbers, changes the row: `mismatch_class` and `mismatch_review` in `corpus/rows/`, the counts that
follow from them, and the sentence in the next version, with the correction printed beside the
original charge as the eight withdrawals already are. The routes are the corresponding author's
address on this paper and the issue tracker of the deposited corpus, and a correction asked for
either way is a commit and a replacement version rather than a negotiation. Eight of the sixteen
charges an earlier draft made have already gone that way on this survey's own evidence; a ninth
would cost it nothing.

Zeroed terms recur, and they are not the same thing as a term that is missing. A term present and
zeroed survives a reader's check of the file, which is why Table 5 marks it separately, and it is
only worth marking where the paper claims the term. Weights differ as well: a penalty printed at
one value in a table and set to another in a config, an equation's term that is not in the released
reward file, a term in the file that the table does not list. And in 13 rows the repository does
not settle the question at all, which is this survey's limit and not an accusation. Appendix C
prints all 38 row by row in their five classes, each with the file, the value on both sides, and
the review note where a charge was narrowed or withdrawn.

A reward table is a claim about a training run and the code is a claim about a repository. Here
the two state different things in nine cases, in the other 29 the released artefacts do not settle
the question, and in exactly one, `hora_2022`, the repository says so itself. Read the reward
function before the reward table, and treat a printed weight as a hypothesis about the code.

**The withdrawals, and what would close it.** This is a result about publishing practice in robot
learning more than about dexterous manipulation: the dexterous corpus is its sample, not its subject.
Nine is also a floor, since 46 method rows released nothing to check and four more are unsettled. The
first count was sixteen. An adversarial re-reading withdrew six outright, `maniptrans_2025`,
`eureka_2023`, `open_television_2024`, `dexmachina_2025`, `artigrasp_2023` and `graspxl_2024`: two
refuted by the accused repository's own README, two resting on reward code that was never in the
parse, one charging the code with structure the paper prints, one against a paper with no reward
function. A seventh, `dexpbt_2023`, was narrowed rather than dropped, its domain-randomisation half
withdrawn and its zeroed reward term left standing, so that row is still a contradiction and the
narrowing takes nothing off the count. That left ten, and ten held until the letters to the authors
were drafted. Writing to `omnih2o_2024` meant reading its accusation again before it went out, and
reading it again is what broke it: four of its five reward-weight comparisons match the paper's own
table to the digit once a systematic x1.25 curriculum factor is applied, and only the stumble weight
differs, by a factor of about a million, which reads as a typo signature in a table rather than a
policy trained on a different objective. Its hands are driven open-loop from a VR pose as well,
outside the policy and outside the reward, which made the work a poor fit for a reward census in a
dexterous-manipulation survey whatever the weight said. The charge is withdrawn and the row moves to
an internal inconsistency, which is where the count above sits it. `penspin_2024` was narrowed the
same way and before the same deadline: half of its charge, that the released code turns off the
paper's tactile channel, is withdrawn, because the config that was read carries 96 observation
dimensions and `enable_tactile: False`, which is what the paper's proprioception-only student should
carry and not a claim the paper makes about that stage. What is left is the line in Table 11, and it
is held at medium because this survey could not establish from the parse whether a second task config
exists elsewhere in that repository.

**The survey has now withdrawn eight accusations in total: seven of them under adversarial review,
and the eighth at the point of writing to the authors, because someone sat down to write the letter
and looked at the evidence again.** Each retraction and narrowing is recorded in its row beside the
charge: a survey that names people should carry its corrections beside its accusations, in public and
not just in the corpus. What would close the finding itself is a reward table generated from the
released config at a named commit, so a reviewer diffs two artefacts instead of reading two
documents.


<!-- FIGURE 4. Taxonomy of training paradigms. Drawn by tools/make_flow_tree.py from corpus/rows
at generation time; paper/figures/fig4_taxonomy.svg. This comment is the specification the drawn
figure should satisfy.

THE RULE, after the R3 review: a leaf label may assert only what its predicate tests. Three leaves
previously read a paradigm tag and then claimed an algorithm, a simulator or a student modality
the tag does not carry. They are now either re-predicated or renamed: - "PPO in a GPU-parallel
simulator, no distillation stage" reads `algorithm` and `sim`, not the RL tag, so it no longer
prints `pistar06_2025` (no simulator, parallel-jaw grippers) or claims privileged state of
`physhoi_2023`, which has none. There is no privileged-observation field in the schema, so no leaf
claims privileged state at all. - "plus teacher-student distillation" no longer says "to vision";
the five papers whose student really is a vision policy hang off it as an annotation, from the
same list Sec. 5.7 names. - "synthetic demonstration generation" takes its membership from Sec.
5.7 rather than from the `data-collection` tag, which is mostly real human-capture rigs; those
rigs are now their own leaf. Membership lists the prose also states are defined once, in the
figure code. - The demonstration branch counts the union of `BC`, `diffusion` and `flow` (44), not
their sum. - The reward branch counts `RL` and `RL+demo` together (59), so the "seeded by
demonstrations" leaf is inside the branch it hangs from. - "no learned policy" counts the three
papers that learn no policy, not the 11 rows carrying a trajopt or MPC tag; the other 8 use those
methods inside a learned pipeline and the footer says so. Where a branch's leaves do not cover it,
the branch prints "N of M in a leaf", and a truncated key list prints "and N more". - The
human-reference branch's six leaves now partition its 12 rows exactly: `pgdm_2023`, whose task
family is grasp and functional/tool, is out, and `dexman_2025`, `humanplus_2024` and
`omnih2o_2024` are in a "whole-body humanoid" leaf matching Sec. 5.4's four edge cases.
`physhoi_2023` and `omnigrasp_2024` stay under "no retargeting, reference already on the
embodiment", which is what their notes support; the earlier plan to move them under "whole
reference including fingers" and "object trajectory only" is superseded.

STILL TO DO. 1. THE CROSS-LINKS ARE MISSING AND THEY ARE THE POINT. The footer says the branches
are not exclusive, then a strict tree is drawn. Draw the overlaps as dashed curves behind the
nodes, in the muted accent colour, each labelled with one word: reward-branch distillation leaf ->
demonstration-branch architecture tags   "distil" reward-branch PPO leaf           -> synthetic
demonstration generation       "generate" egocentric video leaf            -> human-reference
branch                   "retarget" human-reference branch           -> demonstration-branch
architecture tags   "distil" no-learned-policy branch         -> reward-branch PPO leaf "smooth"
teleoperated-on-robot leaf       ->  seeded by demonstrations                 "seed" The fifth
carries `pang_global_planning_2022`'s proof that randomised smoothing, which is what a policy
gradient does implicitly, and analytic log-barrier smoothing compute the same local model of
contact. It is the only edge that is a theorem rather than a pipeline; draw it differently, for
instance with a double dash. 2. THE ARCHITECTURE AXIS IS ABSENT. Under the human-demonstration
branch, what supervises the policy and what shape the policy has are independent choices. Add four
small tags, not full nodes: action chunking `aloha_act_2023`; diffusion `diffusion_policy_2023`,
`dp3_2024`; flow matching `pi0_2024`, `groot_n1_2025`, `h_rdt_2025`, `unidex_2026`,
`egoscale_2026`; autoregressive action tokens `openvla_2024`, `metis_2025`. Tag counts are 1, 14
and 8 for the first three from the `diffusion` and `flow` labels. 3. SCARCITY MUST BE LEGIBLE.
Population-based training over hyperparameters holds one paper, `dexpbt_2023`, which the figure
does not show; add it as an annotation off the PPO leaf with the count 1. Size or shade every leaf
by its count so a reader sees without reading a number that the demonstration branch is wide, the
non-learning branch is three single papers, and automated reward design is two.

Palette, dark-mode handling and font stack follow the other figures in paper/figures/. All counts
are recomputed from corpus/rows/*.json at generation time and never hardcoded, so the figure
cannot drift from the corpus. -->