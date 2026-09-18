# articulated_tools_inhand_2025 — In-Hand Manipulation of Articulated Tools with Dexterous Robot Hands with Sim-to-Real Transfer (Atar, Huang, Richter, Yip; arXiv 2025)

sources: papers/md/articulated_tools_inhand_2025.md [acba413a] ; no code

## One-line contribution
A privileged-oracle-to-proprioceptive-student sim-to-real pipeline for in-hand articulation of tools with a single internal revolute joint (scissors, pliers, tongs, laparoscopic tool, stapler), refined online on hardware by a cross-attention module (CATFA) that fuses whole-hand tactile and motor-torque feedback into the frozen student's action intent (Abstract; Sec. III).

## Setting
- hand(s): Inspire Hand, 6 active DoF (one per finger, two for the thumb) + 6 mimic joints, "approximately 1.4× the size of an average human hand"; covered with a nitrile glove (Sec. IV, "Hardware"). Arm: mounted on a Franka arm for the perturbation study (Tab. III). Single-handed, single-arm.
- simulator / physics: IsaacLab (Sec. IV, "Simulation"). Sim runs at 120 Hz with control decimation of 3 (effective 40 Hz control); joint targets on hardware issued at 30 Hz tracked by a 120 Hz low-level PD. Episodes: 2000 steps (≈50 s), terminate on object drop, workspace exit, or horizon. Contact: "convex decomposition for complex geometries and convex hulls for simpler ones." 8192 parallel headless envs on a single RTX 4090; training per tool 4-12 hours (more complex collision models cost more).
- observation: oracle (privileged) o_t = joint positions/velocities of the 6 active DoF (q_t, q̇_t), previous joint target u_{t-1}, articulation angle and rate (θ_art_t, θ̇_art_t), tool-frame pose and linear velocity (x_obj_t, ẋ_obj_t, frame attached to the articulation joint axis per the URDF, not COM or tip), raw simulated joint force τ_raw_t, and a one-hot articulation command s_t ∈ {0,1}² (Sec. III-A). Distilled student drops u_{t-1} and privileged terms, keeping (q_t, s_t) plus proprioception. Hardware adds tactile f_tact_t ∈ R^{36×44} (resistive skin) and motor torque τ_motor_t ∈ R^6 (current sensing), fed only to CATFA, not the frozen base policy (Sec. III-C).
- action space: absolute joint targets u_t ∈ R^6, smoothed with an exponential moving average before execution (Sec. III-A, "Actions").
- objects / data: 5 articulated tools, each with one revolute joint, real + simulated counterparts (Fig. 5): surgical clamp, tong, plier, laparoscopic tool, stapler. Mechanical fixtures scale tools to the oversized Inspire hand. Sim randomizes object mass, surface friction, material properties (Sec. IV). Initial grasps for oracle rollouts collected via Manus MetaGloves Pro teleoperation when autonomous grasping fails (Sec. III-A).

## Method
- paradigm: RL (oracle) → behavior-cloning distillation (student) → behavior-cloning online adaptation (CATFA), sim-to-real, no vision.
- algorithm: PPO [37] for the oracle in simulation with a force-torque perturbation curriculum (Sec. III-A). Distillation trains the student from "stable oracle rollouts," explicitly not DAgger ("Standard distillation methods such as DAgger are ineffective ... partially informed students frequently drop objects early and fail to explore," Sec. III-B) — exact distillation loss not printed in the parse. CATFA is trained by behavior cloning on <50 human-labeled successful real rollouts: "the student minimizes" a loss over demonstrations D = {(q_t, s_t, u_t)} with oracle actions u_t (equation itself not rendered in the parse; Sec. III-C, "Training Adaptation").
- teacher-student: yes — oracle (privileged) → proprioceptive student (behavior-cloned from oracle rollouts) → CATFA (behavior-cloned residual on top of the frozen student, using real tactile+torque). Privileged signal removed at distillation is specifically u_{t-1} plus the full privileged o_t; CATFA is explicitly framed as compensating for the resulting partial observability (Sec. III-C derivation, "Reducing Partial Observability via Tactile-Force Feedback").
- reward or loss — oracle reward, quoted from TABLE I (paper's own equation table, terms transcribed as printed):
  - r_pos_t = −‖x_obj_t − x_obj_0‖²₂, scale 500.0
  - r_quat_t = −‖q_obj_t − q_obj_0‖²₂, scale 5.0
  - r_goal_t = −|θ_art_t − θ_target_st|, scale 10.0
  - r_timer_t = T_open_{t-1}+1 if s_t=1 ∧ θ_art_t ≥ θ_open; T_close_{t-1}+1 if s_t=0 ∧ θ_art_t ≤ θ_close; −1 otherwise, scale 0.05
  - r_inc_t = Σ_{ϑ∈Θ_st} w(ϑ)·1{θ_art_t crosses ϑ}, scale 1.0
  - r_contact_t = n* − n_t (deviation of finger-link contact count from a desired count n*), scale −0.1
  - r_slip_t = 1{h_obj_t < h_min}, scale −1.0
  - r_act_t = −‖u_t‖²₂, scale −0.001
  Prose gloss (Sec. III-A): pose terms "penalize deviation from the initial pose," r_goal minimizes error to θ_target, r_timer "rewards sustained achievement of articulation state," r_inc gives crossing bonuses, r_contact/r_slip "enforce stability," r_act "regularizes joint motion to prevent excessive excursions and over-tightening." No aggregate weighted-sum formula is printed beyond the per-term scale column; CATFA's BC loss equation is present in prose reference only, not rendered as a formula in the parse.
- key trick(s): random-walk external force/torque perturbations during oracle and student training (ΔF_ext_t, Δτ_ext_t sampled uniformly, clipped, accumulated as a random walk — "allows directional accumulation over time, covering disturbances that emulate gravity, acceleration, and external contact," Sec. III-A "Policy optimization with random walk perturbations"); cross-attention (not concatenation) fusion of tactile/force features as keys/values against the policy's intent embedding as query, 8 heads, embed dim 64, argued to give "targeted correction rather than symmetric feature aggregation" (Sec. III-C, "Model Architecture" and "Cross-Attention vs Concatenation").

## Evaluation
- metrics (Sec. IV-A): success = "maintaining the commanded open or closed configuration (joint angle above or below a predefined threshold) throughout the episode"; Opening Displacement = max tip separation in the open state (higher better); Closure Residual = remaining tip gap in the closed state (lower better), averaged per trial. Second study: pose deviation e_pose(t) = ‖x_t − x_0‖₂ + λ‖q_t − q_0‖₂ (quaternion L2 as a small-angle proxy for geodesic distance), tracked via ArUco markers.
- headline numbers, TABLE II (≈10 real-world rollouts per tool per policy, per Sec. IV-A text): CATFA success = 100% on all 5 tools (Surgical Clamp, Tong, Plier, Laparoscopic Tool, Stapler); best or tied-best Opening Disp. and Closure Residual on 4/5 tools (Laparoscopic Tool opening disp. slightly below the raw sim-to-real student: 109.31±1.05 vs 109.45±9.98 mm). Sim-to-Real student alone drops to 20% (Surgical Clamp) and 30% (Plier) success; Proprioceptive BC (no tactile/force) reaches 90%/70% on those two. TABLE III (n=10 real rollouts per tool, Franka-mounted perturbation study): CATFA has lowest or near-lowest pose-deviation error on Clamp and Laparoscopic Tool in both open/close phases; on Plier-Close, Proprio-Tactile-Force BC (concatenation, no attention) is marginally lower (0.031 vs 0.033 m).
- baselines beaten: raw distilled Sim-to-Real student (open-loop, no sensing); Proprioceptive BC (proprioception only, no tactile/force); Proprio-Force BC, Proprio-Tactile BC, Proprio-Tactile-Force BC (direct concatenation of the same sensor features CATFA uses, added only in the Tab. III study).
- real robot? Inspire Hand on a Franka arm; "approximately 10 real-world rollouts" per tool per policy for Tab. II, and explicitly n=10 real-world rollouts per tool for Tab. III. Not video-only — trial counts and per-trial mean±std are reported for both tables.

## Reproducibility
- code released? No. Abstract references a "Website" (URL not given in the parse); bib `github` field is null; no code/md exists for this key.
- checkpoints / assets? Not mentioned.
- reproducible tables? None of Tab. II or Tab. III numbers can be checked against a repo; they stand only as reported.

## Limitations stated by the authors (Discussion & Conclusion)
- Formulation assumes binary articulation commands s_t ∈ {0,1}, limited to discrete open/close tools; continuous articulation targets and multi-DOF mechanisms are future work.
- "Hardware fine-tuning is sensitive to motor torque scaling and control-frequency discrepancies between simulation and the geared, spring-assisted hand."
- "minor joint micro-oscillations are occasionally observed in the Inspire hand due to backlash in the geared transmission and spring compliance not modeled in the simulation" (reduced, not eliminated, by CATFA).
- Simulated joints "do not fully reproduce real-world mechanics, introducing a domain gap" even though intended kinematics are captured (Sec. IV).

## Quotable claims (verbatim, with section)
- "Standard distillation methods such as DAgger are ineffective for articulated in-hand manipulation, as partially informed students π_student frequently drop objects early and fail to explore." (Sec. III-B)
- "This intent-conditioned design enables targeted correction rather than symmetric feature aggregation, effectively serving as a learned impedance adaptation layer that injects feedback only when contact discrepancies arise." (Sec. III-C)
- "we introduce structured disturbance augmentation during training... A random walk in force–torque space allows directional accumulation over time, covering disturbances that emulate gravity, acceleration, and external contact within a bounded domain." (Sec. III-A)
- "we directly incorporate f_tact and τ_motor into CATFA" rather than modeling gear ratio/friction/backlash/compliance transmission effects via system identification (Sec. III-C, "Hardware Sensing")
- "The current formulation assumes binary articulation commands st ∈ {0, 1}, limiting applicability to tools with discrete open–close behaviors." (Limitations)

## Notes for the survey
- Feeds: sim-to-real distillation architecture comparisons (oracle→student→adaptor is a 3-stage pipeline, distinct from single-stage teacher-student in most 2022-2023 in-hand RL); tactile-fusion architecture comparison (cross-attention vs. concatenation, with an ablation, Tab. III, that is the paper's only controlled evidence CATFA's attention mechanism beats naive fusion — margins are small and one cell (Plier-Close) favors concatenation).
- What's genuinely new vs. 2022-2023 rigid-object reorientation baselines (OpenAI-style / penspin-style): the task itself has a second internal DoF (tool articulation) that must be driven to a target while a stable grasp is separately maintained under injected disturbances — reward table adds r_goal/r_timer/r_inc specifically for articulation-state progress and a contact-count term (r_contact) rather than the position/orientation-only reward typical of cube/pen reorientation. The paper frames this explicitly as new relative to prior work that "treat[s] the articulated object as part of the static world" (door/drawer/cabinet manipulation) rather than held in-hand (Sec. II).
- Contact/penetration: not addressed as a measured quantity anywhere in the parse — "contact" appears only as a reward term counting finger-link contacts (r_contact) and as tactile-sensor readings; no interpenetration metric, contact-force distribution, or penetration-depth number is reported. Contact solver detail is limited to "convex decomposition for complex geometries and convex hulls for simpler ones" (Sec. IV).
- See Reproducibility block above: no code, tables stand only as reported.
