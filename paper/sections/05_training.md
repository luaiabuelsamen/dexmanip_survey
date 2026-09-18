## 5. How policies are trained

### 5.1 The design space

A dexterous policy is defined by what supervises it. Four sources are in use across the corpus's
110 method rows. A reward function supervises reinforcement learning. A human demonstration
supervises imitation. A human reference trajectory supervises a physics-based tracker, which is
imitation with a simulator in the loop. And nothing supervises a model-based planner, which is
handed a cost and a model instead.

The labels do not partition the corpus. Of the 110 method rows, 53 carry the tag `RL`, 27 `BC`, 23
`distillation`, 16 `VLA`, 14 `teleop-system`, 14 `diffusion`, 10 `data-collection`, 8 `flow`, 6
`RL+demo`, 6 `trajopt`, 5 `MPC`, 4 `grasp-synthesis` and 2 `world-model`. The tags sum to far more
than 110 because most methods published since 2024 sit on two branches at once. Figure 4 draws the
tree and the cross-links. Table 7 is the row-by-row version of the same thing, and is the table to
scan when looking for work comparable to your own.

Three axes matter more than the name a paper gives itself: where the supervision comes from,
whether it is optimised in a simulator or on hardware, and what the deployed policy looks like
once training is done. On the last axis the field has converged hard, and section 5.7 shows why.

{{figure:fig4_taxonomy}}

### 5.2 Reinforcement learning

#### 5.2.1 The standard recipe

Fifty-nine of the 110 method rows learn from a reward. Forty-eight name PPO as the algorithm, and
the next most frequent, DAPG, appears four times. Forty-three run their own experiments in a
GPU-parallel simulator from the Isaac family or Genesis, and 36 do both. Only 31 rows state an
environment count, with a median of 8192 and a maximum of 64000. Twenty-three rows distil a
privileged teacher into a deployable student, and 16 combine all three of PPO, a GPU simulator and
distillation. That 16-row intersection is the recipe as it is actually practised.

The hand is almost always an Allegro. It appears in 35 of the 110 method rows and in 17 of the 31
reorientation rows, ahead of Shadow at 21 and 6 and LEAP at 12 and 4.

Privilege is handled two ways. `openai_dexterity_2018` gives the value network object and target
orientation, joint angles, joint velocities and object velocities that the policy never sees, and
its footnote records that current object orientation was left out of the policy inputs by
accident. `dextreme_2022` uses the same asymmetric critic with a 2048-unit LSTM against the
actor's 1024. `hora_2022` instead compresses nine privileged object properties into an
eight-dimensional vector and regresses that vector from 30 steps of proprioception.
`visual_dexterity_2022` distils twice, from a state teacher to a synthetic point cloud and then to
a rendered one, for a stated fivefold training speedup.

Domain randomisation is the part of the recipe with the least discipline.
`openai_rubiks_cube_2019` made it adaptive, pushing each range boundary out when performance at
that boundary exceeds 20 successes and pulling it in below 10, and `dextreme_2022` reproduced the
mechanism with a 256-sample queue and 40 percent of environments dedicated to boundary evaluation.
Both publish the discovered ranges. Below that standard, three shipped configurations disagree
with their own papers about what was randomised. `hora_2022` states a joint-noise range of U(0,
0.005) against a shipped `jointNoiseScale` of 0.02, `penspin_2024` zeroes the disturbance force
its appendix describes, and `dexpbt_2023` reports no randomisation experiments while shipping a
full schedule behind a `randomize: False` switch.

#### 5.2.2 Reward engineering

Table 5 puts the 21 in-hand reorientation methods against nine recurring term families and marks
each cell by where the term was found, in the paper, in the code, or in both.

{{table:table5_rewards}}

The families are not equally popular. Nineteen of 21 methods have a goal or rotation tracking
term, which is the task. Thirteen penalise effort as torque, work or joint velocity, 13 pay a
sparse success bonus, 12 penalise a drop and 11 penalise object velocity. Eight penalise deviation
of the hand from a canonical grasp pose, a family the plan for this table did not anticipate and
which had to be added. Only five reward closing the distance from fingertips to the object, and
only four mention contact or force at all.

That last number is the finding. Four of 21 in-hand reorientation methods put any contact or force
quantity in the reward. None puts interpenetration in it. `teledexter_2026` penalises
interpenetration with a differentiable signed-distance term, but during offline reference
construction, not in the policy's reward. Across all 110 method rows, 83 do not address
penetration at all, 5 constrain it, 3 measure it and 3 penalise it. The physical quality of the
contact is not something this literature optimises.

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
are logged. `maniptrans_2025` starts at zero gravity and high friction and restores both, while
narrowing a fingertip threshold from 6 cm to 4 cm. `dexmachina_2025` attaches virtual
spring-damper controllers to the object, lets them do the task at first, then decays their gains
to zero. `rotateit_2023` sets its rotation-penalty weight to zero and ramps it to −0.1, reporting
that applying it from the start makes the policy learn only to hold the object still.
`viserdex_2026` replaces adaptive domain randomisation with a performance-based curriculum over
regularisation weight, action latency and time between successes, and reports that removing the
regularisation component causes complete failure.

Population-based training appears once. `dexpbt_2023` runs populations of 8, 16 and 32 agents,
splits them 30/40/30, mutates the middle and replaces the bottom with mutated copies of the top,
with each float hyperparameter multiplied or divided by a factor drawn from U(1.1, 1.5) with
probability 0.2. It reports 30 hours on a single V100 for a five-billion-transition single-arm
run, and 0.32 trillion environment steps for its largest population.

`eureka_2023` has GPT-4 write the reward function directly, constrained to return a total and a
dictionary of named components, and feeds per-component statistics back to the model between
iterations. Its own appendix gives an example whose reward correlates at −0.26 with the
human-written one and still scores 1.45 on the human-normalised metric, which is the strongest
argument in the corpus that hand-tuned weights are not a ceiling. `dreureka_2024` moves the safety
requirement into the prompt instead of a penalty term, asking in words for a cube rotating at
about 0.25 radians per second with fingers penalised for leaving their initial pose. Neither can
be checked. Eureka's config ships one iteration and three samples against the paper's five
iterations and sixteen samples, and writes generated rewards to a gitignored directory. DrEureka's
repository contains only the locomotion and globe-walking trees, so its LEAP-hand reward has no
code at all.

#### 5.2.4 Where reinforcement learning stalls

Reinforcement learning stalls on objectives that are not learnable as stated. `anyrotate_2024`
found the angular-velocity objective unlearnable in the multi-axis setting and replaced it with a
moving keypoint target. `rotateit_2023` reports that its multi-axis policy "does not converge when
training with only reinforcement learning" and adds an imitation loss against single-axis oracles.
`eureka_2023` cannot spin a pen from scratch and needs a pretrain-then-finetune split, with the
from-scratch ablation failing to complete one cycle. `physhoi_2023` documents the general shape of
the problem: contact moves the object off the reference, so return goes down, so the policy learns
not to touch the object.

It stalls on geometry too, and on evidence. `hora_2022` fails on objects under 4 cm across because
the fingers collide with each other. Real-robot trial counts stay small: `openai_dexterity_2018`,
`openai_rubiks_cube_2019`, `dextreme_2022` and `poise_2026` each report 10 trials for their
headline, and `robot_synesthesia_2023` reports 5. `hora_2022` at 240 is the outlier, not the norm.

### 5.3 Learning from human data

#### 5.3.1 Teleoperation and retargeting

Table 6 lists the 30 corpus rows that describe a system for getting human motion onto a robot
hand, with the retargeting objective compressed to one clause each.

{{table:table6_teleop}}

Retargeting splits four ways. The dominant family matches task-space vectors between the human and
robot hands. `dexpilot_2020` set the pattern with a weighted squared distance between fingertip
vectors, switching weights of 1, 200 and 400 by whether a pair is within threshold, a
minimum-separation constant of 3 cm between primary fingers, and a regulariser toward the open
hand, solved online with SLSQP. `anyteleop_2023`, `open_television_2024`, `bunny_visionpro_2024`
and `ace_teleop_2024` all use the same formulation. The second family copies joint angles where
the kinematics allow it, as `holo_dex_2022` does for index, middle and ring while solving the
thumb by inverse kinematics and discarding the pinky the Allegro does not have. The third family
learns the map offline. `geometric_retargeting_2025` trains a per-finger network in three to five
minutes against motion-direction, coverage, flatness, pinch and collision criteria, then runs at 1
kHz against the 60 to 100 Hz of online optimisation, raising configuration-space coverage from 38
to 90 percent and one-time grasp success from 55 to 87.5 percent. The fourth family removes
retargeting from the loop. `dexumi_2025` builds an exoskeleton whose fingertip workspace is
optimised to match the target hand, then regresses encoder values straight to motor values.

The table's empty cells are the point. Only 12 of the 30 rows state a latency of any kind, and
only 7 state a rig cost. Where costs are stated they are low and falling, from the $399 headset of
`holo_dex_2022` through the $600 exoskeleton of `ace_teleop_2024` and the $600 haptic glove of
`doglove_2025` to the $4,000 backpack of `dexcap_2024` and the roughly $6,000
glove-and-teacher-arm rig of `bidex_teleop_2024`. Latency, where reported, spans four orders of
magnitude, from `dexpilot_2020`'s "about one second" to `holo_dex_2022`'s "under 100 milliseconds"
to `geometric_retargeting_2025`'s 1 kHz retargeting step. Only 13 rows report how many
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
each. Flow matching is the 2024-onward default for large models and carries 8 of the 110 rows.
Discrete action tokens are the fourth, used by `openvla_2024` and `metis_2025`, and are the only
one of the four that needs no continuous head at all.

Data generation is a separate lever and is underrated. `dexmimicgen_2024` turns 60 human source
demonstrations into 21,000 simulated ones across 9 tasks and 3 embodiments, and a real Fourier GR1
with two Inspire hands reaches 90 percent from 40 generated demonstrations against 0 percent from
the 4 source demonstrations. `dex1b_2025` iterates optimisation, a CVAE proposal model and a
simulator filter to produce roughly a billion synthetic grasps, and its CVAE baseline beats the
prior best by 22 points.

#### 5.3.3 Human video without a robot

Seven rows train a dexterous-hand policy from video with no teleoperation at any stage.
`dexmv_2021` retargets 700 self-recorded demonstrations by matching palm-to-fingertip task-space
vectors and estimating actions by inverse dynamics. `videodex_2022` mines 965 trajectories from
EpicKitchens to pretrain a neural dynamic policy. `dexvip_2022` goes further into the reward,
clustering 715 curated HowTo100M frames into one consensus grasp pose per object category and
adding it as a reward term. `okami_2024`, `human2sim2robot_2025` and `hudor_2024` work from a
single video each. `wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

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

Twelve method rows carry the `track-human-ref` task family. Eight of them track a human hand on an
object and are covered here. The other four sit at the edges of the family: `human2sim2robot_2025`
tracks only the object's trajectory, `dexman_2025` retargets bimanual video onto a full humanoid,
and `humanplus_2024` and `omnih2o_2024` track whole-body human motion. In all of them a reference
is retargeted onto the robot and a policy is trained to make the simulated body follow it. The
reference supplies the shaping that reward engineering would otherwise have to invent, and the
simulator supplies the physical consistency that pure imitation lacks.

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

The corpus scores 13 generalist policies on whether their own experiments report a result on a
multi-fingered hand. Eight do and five do not. The evidence is one sentence in each case.

Five are gripper-only. `pi0_2024` writes "UR5e. An arm with a parallel jaw gripper", and its
released code encodes each ALOHA gripper as a single scalar. `pi05_2025` writes "Both platforms
are equipped with two 6 DoF arms with parallel jaw grippers". `pistar06_2025` writes "we use a
static bimanual system with two 6 DoF arms with parallel jaw grippers". `openvla_2024` evaluates
on a WidowX, a Google robot, a Franka tabletop and DROID, all parallel-jaw, with the gripper as
one action dimension. `gemini_robotics_2025` puts a five-fingered Apollo hand in a figure caption
and reports no success rate, trial count or table for it anywhere.

Eight do evaluate on a hand. `gemini_robotics_15_2025` is the successor that fixed the gap, and
reports Apollo progress scores of 0.74, 0.73, 0.66, 0.62 and 0.63 by generalisation axis.
`groot_n1_2025` writes "This benchmark focuses on dexterous hand control using the GR-1 humanoid
robot equipped with Fourier dexterous hands", without stating the hand's degrees of freedom.
`being_h0_2025` uses "a 7-DoF Franka Research 3 arm, a 6-DoF Inspire hand" over 20 trials per
task, and `being_h05_2026` adds a LinkerBot O6 and two further hands, all tagged as six degrees of
freedom. `dexgraspvla_2025` uses "a 7-DoF RealMan RM75-6F arm and a 6-DoF PsiBot G0-R hand" over
1,287 trials, `metis_2025` uses "a pair of Inspire 6-DoF dexterous hands" on a Unitree G1, and
`dexora_2026` uses two XHAND hands with 12 actuated joints each. `dexvla_2025` is the borderline
case: the hand appears in one real-robot task family, while shirt folding, bussing, sorting, bin
picking and laundry all run on parallel-jaw grippers, and its 91-task pretraining mixture is
entirely gripper-based.

The hands that do appear are small. Four of the eight report six actuated degrees of freedom, one
reports twelve, and three do not state the number. None of the eight evaluates on the 16 to 24
actuated degrees of freedom that the reinforcement learning literature of section 5.2 runs on.
Three further rows, `gr_dexter_2025`, `unidex_2026` and `egoscale_2026`, evaluate on hands but
were not scored on this field, and the first of them reports a 21-DoF ByteDexter V2.

The released code also drifts. `groot_n1_2025`'s repository is a later N1.7 generation with a
different backbone, a different action horizon and embodiments the paper does not describe.
`pi05_2025`'s repository states that it supports only the flow-matching head, not the hybrid
recipe the paper describes.

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
takes 117.16 seconds of planning on a 16-core CPU, against the GPU-days of section 5.2. It is also
the only method here that imposes non-penetration as a hard constraint. Its own limitation is the
honest part: its 3D systems transfer to hardware far worse than its 2D ones, because the
quasi-dynamic assumption breaks and planned grasps miss contacts under a second-order solver.

### 5.7 Hybrids, and where the field has converged

The recurring shape is reinforcement learning in simulation distilled into a policy that looks
like an imitation policy. Twenty-three rows label the distillation step, and 16 combine PPO, a GPU
simulator and distillation in one pipeline.

The shape appears in four variants. The first distils a privileged teacher into a vision student
inside one paper, which is `hora_2022`, `visual_dexterity_2022`, `rotateit_2023`,
`robot_synesthesia_2023` and `viserdex_2026`. The second uses reinforcement learning as a
demonstration factory. `dextrack_2025` mines demonstrations with per-trajectory RL and trains a
generalist on them, and `maniptrans_2025` does the same to build a 3.3K-episode dataset.
`dexteritygen_2025` trains a diffusion controller on ten billion simulated grasp-to-grasp
transitions and then projects a human teleoperator's coarse command onto it, taking four
reorientation tasks from 0 out of 20 under raw teleoperation to 12, 13, 10 and 9 out of 20. The
third generates data without reinforcement learning at all, which is `dexmimicgen_2024`,
`dex1b_2025` and `deximit_2026`. The fourth wraps an RL policy in a residual, which is
`resdex_2024` at 88.8 percent over 3,200 objects in 12 GPU-hours.

The consequence is worth stating plainly. In the variants that dominate 2025 and 2026 work, the
reward is no longer the objective of the deployed policy. It is the objective of the process that
produced the deployed policy's training data. Reward engineering has moved upstream into data
curation, and every reward-shaping pathology in section 5.2 now reaches the shipped policy through
a dataset rather than a gradient.

### 5.8 What the released code says

Thirty-seven of the 110 method rows record a disagreement between the paper and the released code,
and all 37 released code, so the rate among the 61 methods that released anything is 61 percent.
Not all 37 are the same kind of thing. Sixteen are contradictions, where paper and code state
different values or different terms. Nine are limitations of this survey's own parsing, where the
relevant function body or config was not recovered and the survey says so. Seven released code
that does not contain the described component at all, three are version skew between the paper and
a later repository, and two are inconsistencies inside the paper. The 16 contradictions are the
number to quote. Among the 21 reorientation methods in Table 5, seven released code, five of those
seven contradict their paper outright, one is version skew and one released a repository without
the reward in it.

The most consequential case is `physhoi_2023`. Its `compute_humanoid_reward` hardcodes the body
position-velocity error and both object rotation errors to zero, with the real computation
commented out beside them. Its Table 4 lists non-zero weights of 0.1 and 0.01 for those object
rotation terms on GRAB. The reward that produced the paper's numbers therefore never tracked
object orientation. A method presented as tracking a 6-DoF reference was, in the code that ran,
tracking position only. The same file family shows the opposite outcome in `omnigrasp_2024`, whose
object rotation term is live. Its `compute_pregrasp_reward_time` has a problem of its own, and it
is internal to the code rather than a paper disagreement. The function accepts weights as
arguments and then hardcodes `w_pos, w_rot = 0.9, 0.1` inside its body.

Zeroed terms recur. `dexpbt_2023`'s `allegro_kuka_base.py` sums eight reward components against
the paper's four, and multiplies one of them, `hand_delta_penalty`, by zero with the comment
"currently disabled". `pianomime_2024` hardcodes its energy and fingering reward terms to return
zero. `penspin_2024` zeroes the disturbance force its appendix describes and disables the tactile
observation channel. A term that is present and zeroed is worse than a term that is missing,
because it survives a reader's check of the file.

Weights drift. `dextreme_2022` states an action-delta penalty of −0.25 in Table 2, ships −0.2 in
`AllegroHandDextremeADR.yaml` and −0.01 in `AllegroHandDextremeManualDR.yaml`, and adds a
`timeout_rew` term that appears in no table. `visual_dexterity_2022`'s Eq. 8 penultimate-joint
penalty does not exist in `dexenv/envs/rewards.py`. `graspxl_2024` ships an object-velocity
coefficient of −1.5 against a stated 0.1, and `unidexgrasp_2023` and `dexpoint_2022` both ship
reward functions structured differently from the paper's equation. `hora_2022`'s own README says
to check out tag v0.0.1 rather than the current commit to reproduce the paper's numbers, which is
version skew rather than contradiction. `dextrack_2025` ships several unreconciled
reward-coefficient sets, and which one produced its headline table could not be determined from
what this survey parsed.

The pattern is not confined to reinforcement learning, and some of it is internal to the papers.
`aloha_act_2023`'s Algorithm 1 says the reconstruction loss is MSE and its Section IV.C says L1.
`dp3_2024`'s prose says the network predicts noise while its shipped config sets `prediction_type:
sample`. `eureka_2023` ships a one-iteration, three-sample default against a reported five
iterations and sixteen samples. `maniptrans_2025`'s stated learning rate and environment count
differ from its own README.

A reward table in a paper is a claim about a training run, and the code is a claim about a
repository. In this corpus the two contradict each other in 16 cases, and in the other 21 the
released artefacts do not settle the question. In none of the 37 does the paper say so. Read the
reward function before the reward table, and treat a printed weight as a hypothesis about the
code.

### 5.9 The master table

Table 7 is every method row on one set of axes, and its footer is worth reading before its rows.
Two hundred and thirty-seven of its 1540 cells are values no source stated. The emptiest columns
are the ones a reader most needs: only 31 rows state an environment count, only 55 state how many
real trials are behind the headline number, and only 32 state how many unseen objects were tested.
A mostly empty row is not a weak method, but it is one that cannot be compared with any other row
here.

{{table:table7_methods}}

<!--
FIGURE 4. Taxonomy of training paradigms. A draft exists at paper/figures/fig4_taxonomy.svg,
generated by tools/make_figures.py with counts recomputed from corpus/rows. This comment is the
specification the drawn figure should satisfy. The draft already gets the frame right: four
first-level branches off "supervision for a dexterous policy", 110 method papers at the root,
branch counts of 53 for a reward function, 49 for a human demonstration, 12 for a human reference
tracked with physics and 11 for no learned policy, and a footer saying the branches are not
exclusive. Five things still need to be true of it.

1. LEAF KEYS MUST BE EXHAUSTIVE OR MARKED. The draft prints five example keys per leaf with no
   indication that the list is truncated. A reader cannot tell whether "egocentric video, no robot
   at all, 7" lists all seven. Either print every key at a leaf or append "and N more" so the
   truncation is visible. This matters most at the two largest leaves, "PPO in a GPU simulator,
   privileged state" at 32 and "synthetic demonstration generation" at 10.

2. THE CROSS-LINKS ARE MISSING AND THEY ARE THE POINT. The draft states in its footer that the
   branches are not exclusive, then draws a strict tree. Draw the overlaps as dashed curves behind
   the nodes, in the muted accent colour, each labelled with one word:
     reward-branch distillation leaf  ->  demonstration-branch architecture tags   "distil"
     reward-branch PPO leaf           ->  synthetic demonstration generation        "generate"
     egocentric video leaf            ->  human-reference branch                    "retarget"
     human-reference branch           ->  demonstration-branch architecture tags    "distil"
     no-learned-policy branch         ->  reward-branch PPO leaf                    "smooth"
     teleoperated-on-robot leaf       ->  seeded by demonstrations                  "seed"
   The fifth link carries `pang_global_planning_2022`'s proof that randomised smoothing, which is
   what a policy gradient does implicitly, and analytic log-barrier smoothing compute the same
   local model of contact. It is the only edge in the figure that is a theorem rather than a
   pipeline, and it should be drawn differently, for instance with a double dash.

3. THE ARCHITECTURE AXIS IS ABSENT. Under the human-demonstration branch, what supervises the
   policy and what shape the policy has are independent choices. Add four small tags, not full
   nodes, hanging under the branch: action chunking `aloha_act_2023`; diffusion
   `diffusion_policy_2023`, `dp3_2024`; flow matching `pi0_2024`, `groot_n1_2025`, `h_rdt_2025`,
   `unidex_2026`, `egoscale_2026`; autoregressive action tokens `openvla_2024`, `metis_2025`.
   Tag counts are 1, 14 and 8 for the first three from the `diffusion` and `flow` paradigm labels.

4. TWO LEAF ASSIGNMENTS IN THE DRAFT ARE WRONG AGAINST THE NOTES. `physhoi_2023` is placed under
   "reference as soft guidance". It is not soft guidance. It tracks a fixed reference with a
   multiplicative kinematic and contact-graph reward, and it does not randomise initialisation
   because "the HOI data may have severe collisions that eject the object". Move it to "whole
   reference including fingers", which then holds five. `omnigrasp_2024` is likewise not soft
   guidance. It tracks a generated object trajectory from a single pre-grasp pose, so it belongs
   under "object trajectory only", which then holds three. "Reference as soft guidance" should
   hold `dexplore_2025` alone, and its count of one is itself informative.

5. SCARCITY MUST BE LEGIBLE. The three leaves under "no learned policy" hold one paper each, and
   population-based training over hyperparameters holds one, `dexpbt_2023`, which the draft does
   not show at all. Add it as an annotation hanging off the PPO leaf with the count 1. Size or
   shade every leaf by its count so that a reader sees, without reading a number, that the
   demonstration branch is wide, the non-learning branch is three single papers, and automated
   reward design is two.

Palette, dark-mode handling and font stack follow the other figures in paper/figures/. All counts
are recomputed from corpus/rows/*.json at generation time and never hardcoded, so the figure
cannot drift from the corpus.
-->
