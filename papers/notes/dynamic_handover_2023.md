# dynamic_handover_2023 — Dynamic Handover: Throw and Catch with Bimanual Hands (Huang et al., CoRL 2023)

sources: papers/md/dynamic_handover_2023.md [sha c4be81a0] ; no code

## One-line contribution
A three-stage MARL pipeline (base MAPPO policy -> supervised goal estimator -> end-to-end joint fine-tune) trains a thrower and a catcher Allegro-hand-on-xArm system to throw and catch objects, transferred sim2real (Sec. 4, Sec. 3).

## Setting
- hand(s): Allegro Hand, 16 DoF each, two of them (one per arm); vendor not stated beyond "Allegro Hands" (Sec. 3, "System Setup")
- arm: 6-DoF XArm-6 per hand, giving a "44-DoF system" per arm-hand subsystem pair; bimanual: yes, two arm-hand subsystems facing each other (Sec. 3)
- simulator / physics: IsaacGym [52]; "simulation frequency is set at 120Hz while the control frequency is 20Hz" (Sec. 3, "Simulation Setup")
- observation: thrower — proprioception + pre-defined target position (padded with zeros to match catcher's obs dimension for MAPPO); catcher — proprioception + pre-defined goal + object's current position; both include past k=2 frames for temporal info (Sec. 4.1). Real-robot catcher additionally gets object position from a RealSense D435 camera (Sec. 3, "Real-world Setup")
- action space: "The policy outputs a 22-dimensional PD control target, with the first six dimensions corresponding to XArm-6 and the remaining 16 dimensions corresponding to Allegro hand" — XArm-6 uses delta joint positions, Allegro uses absolute joint positions; only arm joints 2 and 3 are actually controlled (others fixed), giving "an 18-dimensional target for the thrower and a 22-dimensional target for the catcher" (Sec. 3, "Action Space")
- objects / data: training objects = "a ball, a cube, and a rod" (one randomly selected per episode); sim evaluation expands to "11 trained objects and 14 novel objects" (Table 1 caption); real world uses "sandbags in three different shapes... a ball, a cylinder, and a triangle prism" (Sec. 5, "Training and Dataset")

## Method
- paradigm: Multi-Agent RL (MARL), each hand-arm system is one agent, plus a supervised-learned goal estimator, combined in a 3-stage pipeline (Sec. 4)
- algorithm: "Multi-Agent Proximal Policy Optimization (MAPPO) [9]... in a non-parameter sharing way" — "leverages centralized training with decentralized execution" (Sec. 4.1). Goal estimator trained with "Adam to optimize the L2 distance between the position of the predicted goal and the thrower's goal" (Sec. 4.2)
- reward or loss: see block C below
- key trick(s): three-stage pipeline separating base-policy MARL from goal-estimator learning from end-to-end joint fine-tuning (Sec. 4); a rod object added to the training set specifically because "if the policy wants to throw the rod stably, it must learn to use all of its fingers" (Sec. 5, Appendix C)

## Evaluation
- metrics (exact definitions): "Success Rate(SR): ... the ratio of successful throws and catches to the total attempts" and "Hit Rate(HR): ... the proportion of objects that successfully hit the hand palm of catcher" (Sec. 5, "Evaluation Criterion"; repeated verbatim in Table 3 caption). No numeric distance/time threshold for what counts as a "successful" catch is given anywhere in the parsed text — not stated.
- headline numbers: Table 1 (sim, ablation) — Ours 0.95±0.07 (known obj.), 0.37±0.04 (novel obj.), vs. "w/o Multi-Agent" 0.89±0.07 / 0.24±0.05, "w/o Goal Estimation" 0.88±0.04 / 0.22±0.04, "w/o Both" 0.93±0.07 / 0.12±0.06. Table 3 (real world) — Ours: Ball HR 0.93±0.12 / SR 0.60±0.20; Cylinder HR 0.80±0.20 / SR 0.53±0.12; Triangle HR 0.86±0.12 / SR 0.33±0.12, vs. Open-Loop (worst: Ball SR 0.13±0.12, Triangle SR 0.07±0.12) and the "w/o Multi-Agent" / "w/o Goal Estimation" / "w/o Both" ablations.
- baselines beaten: Open-Loop (kinesthetic-taught trajectory replay), w/o Multi-Agent (PPO instead of MAPPO, shared full observation), w/o Goal Estimation (stage-1-only MAPPO), w/o Both (stage-1-only PPO) (Sec. 5, "Baselines")
- real robot? Yes — two Allegro Hands on two XArm-6 arms; Table 3, "averaged on 3 seeds with 5 trails for each" per object per method (i.e. N=15 trials per cell); 3 sandbag shapes (ball, cylinder, triangle prism)

## A. Embodiment
- hand: Allegro Hand x2, 16 DoF each; arm: XArm-6, 6 DoF each, giving "a 44-DoF system" per subsystem (Sec. 3); bimanual: yes, facing configuration (Fig. 1, Fig. 2)
- simulator: IsaacGym [52]; physics engine not named beyond "IsaacGym physical simulator" (Sec. 3)
- sim timestep / control rate: "simulation frequency is set at 120Hz while the control frequency is 20Hz" (Sec. 3); real-robot "ROS-based pipeline that operates at a control frequency of 20Hz" (Appendix A)
- number of parallel envs: not stated
- GPU used / wall-clock training time: not stated

## B. Learning
- paradigm: MARL (MAPPO) for stage 1 and stage 3, supervised regression for stage 2 goal estimator (Sec. 4)
- algorithm: "Multi-Agent Proximal Policy Optimization (MAPPO) [9]... in a non-parameter sharing way" (Sec. 4.1); PPO used as the single-agent ablation baseline ("Without Multi-Agent," Sec. 5, "Baselines"); hyperparameters for both in Appendix D, Tables 6-7 (values garbled in the parsed markdown table — flagged, not fully re-derivable; e.g. MAPPO: hidden size [1024,1024,512], clip range 0.2, discount γ=0.96, GAE λ=0.95; PPO: num mini-batches 4, learning rate 3.e-4, discount γ=0.96, GAE λ=0.95)
- teacher-student / distillation: not used; this is not a privileged->vision distillation setup. The goal estimator is a separate supervised module (Sec. 4.2), not a policy distillation
- observation vector: thrower = proprioception + pre-defined target position (zero-padded to match catcher dim); catcher = proprioception + pre-defined goal position + object's current position (camera-derived on real robot); past k=2 frames stacked (Sec. 4.1, Sec. 3). Exact per-dimension breakdown (joint angles, velocities, etc.) not stated — code absent.
- action space: 22-dim PD target overall, arm uses delta joint position on joints 2-3 only, hand uses absolute joint position target; effective 18-dim thrower / 22-dim catcher action (Sec. 3, "Action Space")
- domain randomisation (Appendix A, Table 4, "Domain Randomization"): Robot — Mass scaling uniform [0.5,1.5]; Friction scaling uniform [0.7,1.3]; Joint Lower/Upper Limit scaling loguniform [0.0,0.01] each; Joint Stiffness/Damping scaling loguniform [0.0,0.01] each. Object — Mass scaling uniform [0.5,1.5]; Friction scaling uniform [0.5,1.5]; Scale scaling uniform [0.95,1.05]. Observation — Correlated noise additive gaussian [0.0,0.001]; Uncorrelated noise additive gaussian [0.0,0.002]. Action — Correlated noise additive gaussian [0.0,0.015]; Uncorrelated noise additive gaussian [0.0,0.05]. Environment — Gravity additive normal [0,0.4]. "We generate new randomizations every 1000 simulation steps."

## C. Reward / objective
Paper only — no code/md file exists for this key (confirmed: `code/md/dynamic_handover_2023.md` absent).

Stage 1 (MAPPO base policy), quoted verbatim (Sec. 4.1):
> "we design the reward function using three components: (i) distance between object and throwing goal; (ii) object velocity projected in the direction from thrower to catcher; (iii) robot joint torque. The final reward r can be computed as r = rdis + rlinvel + rtorque, where rdis = exp(−20 ∗ (pt −Gt)) represents the distance, rlinvel = clamp(v · û, −0.1, 0.1) denotes the object's velocity towards the catcher, and rtorque = −0.003 ∗ ∥τ∥² corresponds to the torque penalty."

Appendix E ("Reward design") repeats the same formula and glosses each term verbatim:
> "The reward of our system r can be computed as r = rdis + rlinvel + rtorque. In the design of our reward, rdis is the reward that mainly responds to throwing objects to the target position. rlinvel is a reward that encourages throwers to release the ball from hand. rtorque is a penalty item for robots that torque is too big."
> "if rdis is missing, the object will not be thrown to the exact position, but will only be thrown forward vigorously. Without rlinvel, it would often fall into a sub-optimal where the thrower holds the ball in its hand and doesn't release. rtorque is a common reward term that allows robots to avoid jitter and large dangerous movements."

Important gap for the giver-vs-catcher comparison this note was written for: **the paper gives a single combined reward formula (r = rdis + rlinvel + rtorque) and does not state separate, differently-weighted reward functions for the thrower ("giver") policy π0 versus the catcher ("catcher") policy π1.** It is not stated whether rtorque is summed over both robots' joints or computed per-agent, nor whether each agent receives the full r or a per-agent decomposition. Not stated = leave as stated, do not infer.

Stage 2 (goal estimator) loss, paraphrased-only text (no verbatim loss equation rendered — the LaTeX expression did not survive PDF->markdown extraction), described as: "Adam to optimize the L2 distance between the position of the predicted goal and the thrower's goal until convergence" (Sec. 4.2). Input is "the historical positions of the object over a span of k frames"; Fig. 3's caption instead says "past 20 frames of the object's positions" — the two values (k=2 used for policy observations in Sec. 4.1 vs. 20 frames in the Fig. 3 caption for the goal estimator) are not reconciled in the text; flagged as an internal inconsistency, not resolved by this note.

Stage 3 (end-to-end joint fine-tune): no new reward term stated; "we jointly fine-tune the goal estimator and the policy network... allowing the catcher to adapt to the goal estimator," with the catcher's observation goal replaced by the predicted goal from stage 2 (Sec. 4.3). No loss/reward formula given for the joint objective beyond continuing to use the stage-1 RL reward plus (implicitly) the stage-2 regression loss — not stated explicitly as a combined objective.

## D. Contact / penetration handling
Not addressed. No interpenetration penalty, contact-force reward term, or contact solver setting is mentioned anywhere in the parsed text. The only contact-adjacent randomization is "contact force" listed in the Introduction as one of the randomized physical properties ("randomization in friction, inertia, the object's center of mass, and contact force," Sec. 1) — but this does not reappear in the Appendix A domain-randomization table (Table 4), which lists Mass/Friction/Joint limits/Stiffness/Damping/Scale/Observation noise/Action noise/Gravity only, with no explicit "contact force" row. This paper->appendix mismatch is noted, not resolved.

## E. Evaluation
- success criterion: SR = "ratio of successful throws and catches to the total attempts"; HR = "proportion of objects that successfully hit the hand palm of catcher" (Sec. 5, "Evaluation Criterion"). No metric threshold (distance/time/contact force) operationalizing "successful" is given in the parsed text — not stated.
- handover/catch-event trigger: not stated as an explicit contact-detection or timing trigger in the pipeline description. The catcher instead acts continuously in closed loop on the goal estimator's predicted destination ("the catch policy will take the predicted object's destination position as input in a close-loop manner," Sec. 1); there is no described discrete "handover moment" detector (e.g., no stated contact sensor, no stated time-to-impact trigger).
- number of eval episodes/seeds: sim (Table 1) — "averaged on 5 seeds, each seed has 100 trails" over 11 trained + 14 novel objects; real world (Table 3, Table 2) — "averaged on 3 seeds with 5 trails for each" (Table 3), and Table 2's pre-throw-condition test uses "10 trials" per pose.
- sim vs real: Table 1/Fig. 4 are simulation; Table 2/Table 3/Sec. 5.4 are real-robot ("real-world evaluation," Sec. 5.4).
- baselines re-run or quoted: all four baselines (Open-Loop, w/o Multi-Agent, w/o Goal Estimation, w/o Both) are the authors' own re-implementations/ablations, not numbers quoted from other papers (Sec. 5, "Baselines").

## F. Reproducibility
"We are committed to releasing the code for our system" (Sec. 6, Conclusion) — stated as a future commitment, not a release; the bib record for this key has `github: null` and there is no `code/md/dynamic_handover_2023.md`, i.e. no code was available to parse at the time of this note. No table in this paper can currently be reproduced from a repo, since none is linked; checkpoints/assets: not stated.

## Limitations stated by the authors
"the use of objects with low restitution may not fully capture the challenges faced in real-life scenarios where objects often have higher restitution... making it more difficult to catch them smoothly without collisions" (Sec. 6, "Limitation").

## Quotable claims (verbatim, with section)
- "we propose to tackle this problem as a multi-agent problem, with each hand being one agent. This helps improve the coordination of two hands during manipulation which allows better Sim2Real transfer." (Sec. 1)
- "MAPPO is an application of the PPO algorithm to multi-agent settings. It leverages centralized training with decentralized execution, allowing each robot agents to efficiently accomplish the cooperative task using partial observations." (Sec. 4.1)
- "we introduce a novel three-stage training pipeline for learning bimanual throwing and catching." (Sec. 4)
- "we also notice that the success rates achieved in real-world experiments are lower than the hit rate. This is primarily attributed to occasional challenges encountered during the grasping phase of the catcher." (Sec. 5.4)

## Notes for the survey (which sections this feeds; contradictions with other notes)
Feeds the survey's bimanual-handover / multi-agent-RL comparison table: this is a MARL (MAPPO, centralized-training/decentralized-execution, non-parameter-sharing between the two agents) approach with a single shared 3-term reward formula, not independently-trained single-agent giver/catcher policies and not a per-agent reward decomposition — contrast with any note describing fully independent thrower/catcher training. No contact/penetration handling is present, unlike notes on grasping-focused dexterous-hand papers that do report a penetration term — useful as a "not addressed" data point in the survey's contact-handling column. Flag two internal inconsistencies found while reading (goal-estimator history window k=2 vs. Fig. 3's "past 20 frames"; Sec. 1's "contact force" randomization vs. its absence from the Appendix A randomization table) for anyone comparing exact hyperparameters against this note.
