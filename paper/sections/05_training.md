# 5. Training a dexterous policy

## 5.1 Sources of supervision

A dexterous policy is defined by what supervises it, and four sources are in use across the
corpus's 113 papers: a reward function supervises reinforcement learning, a human
demonstration supervises imitation, a human reference trajectory supervises a physics-based
tracker, which is imitation with a simulator in the loop, and nothing supervises a model-based
planner, which is handed a cost and a model instead.

The labels do not partition the corpus. Reinforcement learning is the largest at 54 of the 113
papers, behaviour cloning next, distillation after that, and ten further tags cover the rest. They
sum to far more than the corpus, because most methods published since 2024 sit on two branches at
once: a reinforcement-learning teacher and a behaviour-cloned student are one paper, not two.
Figure 4 draws the tree and the cross-links, and Table 7 is the paper-by-paper version of the same
thing.

What the deployed policy looks like once training is done matters more than the name a paper gives
itself, and on that axis the field has converged hard. Section 5.5 shows why.

Table 7's emptiest columns are the ones a reader most needs. Only 70 of the 113 papers state how
many real trials are behind their headline number, and fewer still state an environment count or
how many unseen objects were tested; section 7.1 takes up what that means for comparison. A mostly
empty line is not a weak method, but it is one that cannot be compared with any other here.

{{table:table7_methods}}

{{figure:fig4_taxonomy}}

## 5.2 Reinforcement learning

Sixty of the 113 papers learn from a reward, and the recipe they use is remarkably uniform. PPO
is the algorithm in nearly all of them; the next most frequent choice appears four times. Most run
in a GPU-parallel simulator, about a third distill a privileged teacher into a deployable student,
and 16 papers combine all three. That intersection is the recipe as it is actually practised, and
Table 7 gives the per-paper detail.

The hand is almost always an Allegro. It appears in 35 of them, and its hold on in-hand
reorientation is tighter still: more than half of those papers use it, against roughly a fifth
for the Shadow and an eighth for LEAP.

Privilege is handled two ways. `openai_dexterity_2018` gives the value network object and target
orientation, joint angles, joint velocities and object velocities the policy never sees, with a
footnote recording that current object orientation was left out of the policy inputs by accident,
and `dextreme_2022` uses the same asymmetric critic with a 2048-unit LSTM against the actor's
1024. `hora_2022` instead compresses nine privileged object properties into an eight-dimensional
vector regressed from 30 steps of proprioception, and `visual_dexterity_2022` distills twice, from
a state teacher to a synthetic point cloud and then to a rendered one, for a fivefold speedup.

Domain randomisation is the part of the recipe with the least discipline. The best practice in
the corpus makes it adaptive, widening each range when performance at its boundary is good enough
and narrowing it when it is not, and publishing the ranges that search discovered
(`openai_rubiks_cube_2019`, `dextreme_2022`). Below that standard, two shipped configurations
disagree with their own papers about what was randomised at all: one ships a joint-noise range
four times wider than the paper states, in a commit its own README says is not the one that
reproduces the paper, and the other ships a disturbance force of zero where the paper describes
one. Both are in Table 11 with the file and the two values.

Table 5 puts the 21 in-hand reorientation methods against nine
recurring term families and marks each cell by where the term was found: in the paper, in the
code, in both, or in the code with every shipped configuration setting its weight to zero.

{{table:table5_rewards}}

The families are not equally popular. Almost every method has a goal or rotation tracking term,
which is the task itself. After that the common families are an effort penalty, a sparse success
bonus, an object-velocity penalty and a drop penalty, each in about half of them. Only four carry
a contact or force term at all. Table 5 gives the full matrix.

Three cells an earlier draft marked *code* print *code (0)* instead, because in each the term is
in the released code with every shipped configuration setting its weight to zero:
`dextreme_2022`'s timeout reward, `dexpbt_2023`'s fall penalty, and `penspin_2024`'s action
penalty. Marking them *code* would tell a reader the code optimises something the paper does not
state, and leaving them blank would hide a term that is in the file. The repository carries the
config key and the zero beside each of the three marks.

Only three of those four contact terms are what they look like. `anyrotate_2024` scores good and
bad fingertip contacts, `poise_2026` rewards a friction-cone wrench margin, and
`force_grasp_sim2real_2026` tracks a commanded grasp force. The fourth penalises the *object*
touching the table, which is task shaping against using the table as a third finger rather than a
statement about hand-object contact, and the flag that enables it defaults to off. So three of the
21 reorientation methods put a hand-object contact quantity in the reward, and none puts
interpenetration in it: the one method that penalises interpenetration does so while building its
references offline, not in the policy's reward (`teledexter_2026`). The physical quality of the contact is not
something this literature optimises.

Term counts range from one to ten. `demostart_2024` gives a single binary terminal reward of 1 and
lets a curriculum over demonstration states do the shaping. `anyrotate_2024` and `viserdex_2026`
each publish ten weighted terms. `viserdex_2026` is the cleanest specification in the table, with
every term, weight and equation in one appendix table, and a statement that the same weights are
used for every object.

Weights are frequently unrecoverable. Three of the 21 papers give no numeric weight that survives
PDF conversion, because the equation blocks are images, which is a limit of this survey and is
recorded as such. `robot_synesthesia_2023` is a worse case. Its six coefficients are described
only as "tuned hyper-parameters" and no number is printed anywhere in the paper, so the reward
it reports cannot be reconstructed from the paper. `dexremoe_2025` names an angular-velocity
penalty weight in prose with no entry in its hyperparameter table, and `dextrack_2025` names an
affinity reward that is missing from its weight table.

Curricula in this literature either relax the physics or tighten the tolerance. `dexpbt_2023`
ratchets a success tolerance down once the policy starts succeeding at it; `maniptrans_2025`
starts in zero gravity with high friction and restores both while narrowing its fingertip
threshold; `dexmachina_2025` attaches virtual spring-dampers to the object, lets them do the task
at first, then decays their gains to zero. The two papers that ablate the curriculum find it
load-bearing. `rotateit_2023` has to ramp its rotation penalty in from zero, because applying it
from the start teaches the policy only to hold the object still, and `viserdex_2026` fails
completely without the regularisation leg of its curriculum.

Population-based training appears once. `dexpbt_2023` trains populations of up to 32 agents,
mutating the middle third of each population and replacing the bottom with mutated copies of
the top, and reports 0.32 trillion environment steps for its largest run. The technique is
routine outside robotics and nothing else in this corpus uses it.

A language model can write the reward outright, which removes the hand-tuning and replaces it
with a search whose objective nobody has read. `eureka_2023` has GPT-4 write the reward
function directly, constrained to return a total and a dictionary of named components, and
feeds per-component statistics back between iterations. Its appendix gives an example whose
reward correlates at −0.26 with the human-written one and still scores 1.45 on the
human-normalized metric, the strongest argument in the corpus that hand-tuned weights are not a
ceiling. `dreureka_2024` moves the safety requirement into the prompt instead of a penalty
term, asking in words for a cube rotating at about 0.25 radians per second with fingers
penalized for leaving their initial pose. Neither can be checked against a file. Eureka's
generated rewards are written at run time to a gitignored directory and never committed, so the
reward behind any reported number cannot be recovered from the repository, though its README
documents the paper's budget of five iterations and sixteen samples as the default and marks
the shipped one-iteration block a fast-test preset. DrEureka's repository contains only the
locomotion and globe-walking trees, so its LEAP-hand reward has no code at all.

Reinforcement learning stalls on objectives that are
not learnable as stated. `anyrotate_2024` found the angular-velocity objective unlearnable in
the multi-axis setting and replaced it with a moving keypoint target. `rotateit_2023` reports
that its multi-axis policy "does not converge when training with only reinforcement learning"
and adds an imitation loss against single-axis oracles. `eureka_2023` cannot spin a pen from
scratch and needs a pretrain-then-finetune split, with the from-scratch ablation failing to
complete one cycle. Section 5.3's contact-graph term exists because of the general shape of the
problem: contact moves the object off the reference, so return goes down, so the policy learns
not to touch the object.

It stalls on geometry too. `hora_2022` fails on objects under 4 cm across because the fingers
collide with each other. What it does not stall on is publication: the real-trial counts behind
these headlines are small enough that section 7.1 treats them as the reporting problem they are.

## 5.3 Learning from human data

Table 6 lists the 30 papers in this corpus that describe a system for
getting human motion onto a robot hand, with the retargeting objective compressed to one clause
each.

{{table:table6_teleop}}

Retargeting splits four ways. The dominant family matches task-space vectors between the human
and the robot hand, weighting fingertip distances and adding a minimum separation between the
primary fingers, solved online; `dexpilot_2020` set that pattern, and `anyteleop_2023`,
`open_television_2024`, `bunny_visionpro_2024` and `ace_teleop_2024` use the same formulation. The second copies joint angles wherever the kinematics allow it and solves only
the thumb by inverse kinematics (`holo_dex_2022`). The third learns the map offline, which buys about an order of
magnitude in rate over online optimisation and, in `geometric_retargeting_2025`, raises
configuration-space coverage from 38 to 90 percent. The fourth removes retargeting from the loop
altogether, building an exoskeleton whose fingertip workspace is designed to match the target hand
and regressing encoder values straight to motor values (`dexumi_2025`).

The table's empty cells are the point. Fewer than half of the teleoperation papers state a
latency at all, and only a handful state a rig cost. Where costs are stated they are low and
falling, from a few hundred dollars for a headset or a glove (`holo_dex_2022`, `doglove_2025`) to a
few thousand for a full mocap backpack (`dexcap_2024`, `bidex_teleop_2024`). Latency is not one quantity either: some figures are end to end, others are a
single retargeting stage, and several cells hold a control rate instead, so the column's spread is
not a range. Fewer than half report how many trajectories they collected, and fewer still report
hours of data.

Where throughput is measured, human collection beats teleoperation by a wide margin.
`humanoid_policy_human_policy_2025` times a grasp demonstration at 3.79 seconds for a bare human
and 19.72 seconds through a teleoperated humanoid, and a pour at 4.81 against 37.31 seconds. It
attributes the gap to retargeting latency and to the workspace of a 7-DoF arm rather than to
anything about the hand.

Four architectures cover the corpus. Action chunking came from `aloha_act_2023`, which predicts a
chunk of joint targets with a CVAE and blends overlapping chunks, reaching high success on fine
bimanual tasks from about 50 demonstrations each. Diffusion came from `diffusion_policy_2023`,
which denoises an action sequence and reports a 46.9 percent average improvement over the previous
generation of imitation baselines; `dp3_2024` swaps the image encoder for a small point-cloud
encoder and improves on it again, most sharply on real tasks. Flow matching is the default for
large models from 2024 onward and carries eight papers. Discrete action tokens are the fourth, and
the only one of the four that needs no continuous action head at all.

Data generation is a separate lever and is underrated. `dexmimicgen_2024` turns 60 human
demonstrations into 21,000 simulated ones, and a real two-handed humanoid trained on the generated
set succeeds where the same policy trained on the source demonstrations never does. `dex1b_2025`
iterates optimisation, a proposal model and a simulator filter into roughly a billion synthetic
grasps, and beats the prior best by a wide margin on its own benchmark.

Seven papers train a dexterous-hand policy from video with no
teleoperation at any stage. `dexmv_2021` retargets 700 self-recorded demonstrations by matching
palm-to-fingertip task-space vectors and estimating actions by inverse dynamics,
`videodex_2022` mines 965 trajectories from EpicKitchens to pretrain a neural dynamic policy,
and `dexvip_2022` goes further into the reward, clustering 715 curated HowTo100M frames into
one consensus grasp pose per object category and adding it as a reward term. `okami_2024`,
`human2sim2robot_2025` and `hudor_2024` work from a single video each, and
`wm_dex_human_videos_2025` pretrains a world model on 829 hours of EgoDex.

Three papers measure the gap directly rather than asserting it.
`okami_2024` runs the same reference-plan and warping pipeline with and without human body and
hand retargeting, and the version without it loses 75.0, 42.1, 82.0 and 74.0 points across four
task and setting pairs. That is the largest clean embodiment-gap number in the corpus.

`humanoid_policy_human_policy_2025` ablates two mitigations separately on the same vertical-grasp
task. Removing the interpolation that slows human trajectories down cuts success to a quarter of
the full method's, and removing the unified state space collapses it to zero, because the policy
is handed a shortcut for telling the two embodiments apart. `egozero_2025` reports the sharpest
version of the same effect: removing its 3D augmentation drops every one of its seven tasks to no
successes at all, and substituting monocular depth for triangulated depth does the same, because
the best metric depth models it tested carry more than 5 cm of error.

More human correspondence is not reliably better, and one paper here tested it directly.
`objdex_2024` supplies the counterexample. It retargets only the wrist and lets reinforcement
learning discover finger motion, and its ablation that adds a fingertip-matching reward "does
not yield benefits and even leads to lower performance". Richer human correspondence is not
uniformly better, and this is the one result in the corpus that says so with an ablation.

Twelve papers sit in the human-reference tracking
family. Eight track a human hand on an object and are covered here; the other four sit at the
edges, `human2sim2robot_2025` tracking only the object's trajectory, `dexman_2025` retargeting
bimanual video onto a full humanoid, and `humanplus_2024` and `omnih2o_2024` tracking
whole-body motion. A reference is retargeted onto the robot and a policy trained to make the
simulated body follow it: the reference supplies the shaping reward engineering would otherwise
have to invent, and the simulator the physical consistency pure imitation lacks.

The multiplicative reward that most human-reference methods now use has a single source.
`physhoi_2023` is the origin of the form. It multiplies a body term, an object term, an
interaction-graph term and a contact-graph term, and reaches 95.4 percent success on GRAB
against 27.0 percent for a DeepMimic baseline. The contact-graph term exists to stop the policy
learning not to touch the object. `omnigrasp_2024` replaces the action space with a pretrained
latent motion prior and reports 94.6 percent grasp success and 84.8 percent trajectory success
on GRAB, while stating outright that it omits penetration metrics.

The next step was to stop treating demonstrations as fixed and let the method generate its own.
`dextrack_2025` adds an imitation loss to PPO and mines its own demonstrations through a homotopy
search over easier neighbouring trajectories, beating the best baseline by about eight points at
either threshold. It has a penetration-depth formula and applies it only to its input references,
never to its own rollouts, and presents tolerance of "severe hand-object penetrations" as
robustness. `maniptrans_2025` freezes a generalist hand imitator and trains a per-task residual on
top, with single-hand success about half again its bimanual figure. Its stance on contact is to
raise the friction coefficient above the real value rather than model skin deformation, and its
real deployment is open-loop replay.

Two papers in this corpus ran the same curriculum and disagreed about whether it helps.
`dexmachina_2025` moves to Genesis with 12,000 environments and six hand URDFs, and drives the
object with virtual controllers that decay to zero. Its re-implementation of
`maniptrans_2025`'s curriculum does not beat no curriculum on its own setup, which is a direct
disagreement between two papers worth quoting in both directions. `dexplore_2025` drops the
explicit retargeting stage and treats the reference as soft guidance, with termination
thresholds derived from the failure rate, reaching 87.7 percent on GRAB with an Inspire hand.

`toporetarget_2026` is the only corpus method that quantifies penetration as an evaluation
quantity, reporting maximum depth and the fraction of frames past 2 mm, and constraining it during
retargeting with a 1 mm soft tolerance and a 30 mm hard bound. It reaches 87.5 percent on its own
pen-spinning set against 46.9 for the best baseline. It does not re-measure penetration after the
tracking policy runs, so the property it constrains is a property of the reference and not of the
behavior.

The pattern holds across all eight, and it is the reference-versus-rollout split in its sharpest
form. Penetration is handled at the reference, if at all, and never at the rollout. `objdex_2024`
completes the set with the only real-robot numbers among them, from 100 percent on a microwave and
a laptop down to 41.2 percent on a ketchup bottle over 20 trials each.

Human data does not port across hands, and
the map is usually left unstated. Fifty-four papers use human data and name 45 distinct hand
strings between them; twenty of those appear in Table 6 with a stated retargeting objective.
The other 33 never say how the human motion reached the hand, and the objectives that are
stated do not converge, running from a fingertip keypoint-vector energy in `anyteleop_2023`
through a per-joint regression from exoskeleton encoders in `dexumi_2025` to no retargeting at
all in `egozero_2025`. What would close it is a retargeting benchmark in TopoRetarget's form
`toporetarget_2026`, reporting contact precision, contact alignment, maximum penetration and
the share of frames past 2 mm, per hand and per dataset.

## 5.4 Generalist and vision-language-action policies

The finding is the size of the hand. Eighteen papers carry the generalist tag. Fourteen of them
settle whether the reported evaluation ran on a multi-fingered hand. Eight of those fourteen did,
six report no hand result at all, and the remaining four never say, `groot_n16_2025` naming no end
effector anywhere on its page.

Five of the eight state a hand size, and that comparison has to be made in actuated degrees of
freedom rather than joints, for the reason section 3 opens with. Four of the five use a
six-actuator hand and one a twelve, so their median is six. The reinforcement-learning literature
of section 5.2 works an order of magnitude above that: its median hand actuates 16 joints. No
generalist policy here that settles the question evaluates on a hand in that band, and the two that
would reach it on paper are the two that never say whether the hand was in the evaluation at all.

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

The gap is size rather than absence. A
generalist policy that does touch a hand runs it at roughly a third of the actuation the
reinforcement-learning literature assumes, and the papers that never settle the question are the
smaller half of the same gap. What would close it is one dexterous-hand task inside the
standard generalist suite, with the hand's actuated degrees of freedom and its vendor printed
beside the number.

## 5.5 Model-based baselines and hybrids

Three corpus methods solve dexterous tasks without learning a policy, and they are the control
group the rest of this section lacks.

Not every method here learns a policy. A smaller line plans through a model instead, and it
reaches dexterous tasks on a fraction of the data. `pddm_2019` learns an ensemble of dynamics
models and plans through it with an MPPI-style optimiser, replanning every step, on a few hours of
data in simulation and a few more on a real Shadow Hand. `mjpc_2022` removes the learned model
too, sampling rollouts through MuJoCo itself at millisecond latency, and reorients a cube in real
time from scratch. It also reports no success criterion, no trial count and no real-robot
result.

One of the three does more than plan: it explains why the learned and analytic routes arrive at
the same place. `pang_global_planning_2022` is the most substantial. It proves that the
randomised smoothing implicit in reinforcement learning and an analytic log-barrier relaxation
compute the same local linear model of contact, then uses the analytic version inside a
trajectory optimiser and an RRT. Allegro in-hand rotation takes 19.59 seconds to optimize and
its plate-pickup task 117.16 seconds of planning on a 16-core CPU, against the GPU-days of
section 5.2, and it is the only method here that imposes non-penetration as a hard constraint.
Its own limitation is the honest part: its 3D systems transfer to hardware far worse than its
2D ones, because the quasi-dynamic assumption breaks and planned grasps miss contacts under a
second-order solver.

The recurring shape in recent work is reinforcement learning in simulation distilled into
something that looks like an imitation policy, and it appears in four variants. The first distills
a privileged teacher into a vision student inside one paper, as `hora_2022` and four others do.
The second uses reinforcement learning as a demonstration factory: `dextrack_2025` mines
demonstrations with per-trajectory RL and trains a generalist on them, and `maniptrans_2025` does
the same at dataset scale. `dexteritygen_2025` goes furthest, training a diffusion controller on
billions of simulated grasp-to-grasp transitions and projecting a human teleoperator's coarse
command onto it, which takes four reorientation tasks from no successes at all under raw
teleoperation to roughly half. The third generates data without reinforcement learning at all. The
fourth wraps an RL policy in a residual, as `resdex_2024` does across thousands of objects in
hours of GPU time.

In the variants that dominate 2025 and 2026 work, the reward is no longer the objective of the
deployed policy. It is the objective of the process that produced the deployed policy's training
data. Reward engineering has moved upstream into data curation, and every reward-shaping pathology
in section 5.2 now reaches the shipped policy through a dataset rather than a gradient.

## 5.6 Paper against released code

A paper that states its reward and also ships the code that trained it can be read twice, and
the two readings sometimes disagree. In eight of the papers here they state different things.
The sharpest case is `physhoi_2023`: its Table 4 gives the object's rotation error a weight for
the GRAB dataset, and in the released reward function that error is set to zero with the
computation that would produce it commented out on the same line, so no weight on it could move
the reward. Table 11 states all eight the same way, each as a repository, a commit, a file, the
value the paper prints and the value the file contains, so a reader with a browser can confirm
or refute any line of it without this survey and without anyone's agreement. What the comparison
does not do is name a cause. A repository at some commit is not the code that produced a paper's
numbers, and nothing here is a claim about intent or about work that released nothing to read.

The authors of every paper named in the table were written to on 19 September 2026, before this
survey was posted, with the claim, its evidence and the sentences the survey would print, and were
given until 10 October 2026 to answer. One reply changed a comparison and removed it from the
count. A second confirmed one: the first author of `pianomime_2024` states that the released code
is the implementation behind that paper's results and that its description of the reward "might be
imprecise" (personal communication, C. Qian, Oct 2026), which settles the direction of the
comparison in the code's favour. The rest are
recorded as they came, and silence is recorded as silence rather than as agreement. The letters as they went out are in `outreach/`, so a reader can see exactly what every
author was asked, and `outreach/RECIPIENTS.md` records who each one went to and how the address was
found. A disputed line is corrected the same way it was made, in public: the route is the address in
the author block, and Appendix C prints every comparison beside the review note that revised it.

The practical lesson for a reader of this literature is small and worth keeping: read the reward
function before the reward table, and treat a printed weight as a hypothesis about the code.

{{table:table11_codegap}}

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
papers that learn no policy, not the 11 papers carrying a trajopt or MPC tag; the other 8 use those
methods inside a learned pipeline and the footer says so. Where a branch's leaves do not cover it,
the branch prints "N of M in a leaf", and a truncated key list prints "and N more". - The
human-reference branch's six leaves now partition its 12 papers exactly: `pgdm_2023`, whose task
family is grasp and functional/tool, is out, and `dexman_2025`, `humanplus_2024` and
`omnih2o_2024` are in a "whole-body humanoid" leaf matching Sec. 5.4's four edge cases.
`physhoi_2023` and `omnigrasp_2024` stay under "no retargeting, reference already on the
embodiment", which is what their notes support; the earlier plan to move them under "whole
reference including fingers" and "object trajectory only" is superseded.

SUPERSEDED. An earlier version of this note listed the cross-links, the architecture axis and
three small annotations as outstanding. All three are drawn now by tools/make_flow_tree.py: six
dashed overlap curves in a right-hand gutter, the architecture tags under the demonstration
branch, and the double-dashed smoothing edge for pang_global_planning_2022's result that
randomised smoothing and analytic log-barrier smoothing compute the same local model of contact.
The list is replaced rather than kept, because a note that says work is missing when it is done
sends the next reader looking for nothing.

Palette, dark-mode handling and font stack follow the other figures in paper/figures/. All counts
are recomputed from corpus/rows/*.json at generation time and never hardcoded, so the figure
cannot drift from the corpus. -->
