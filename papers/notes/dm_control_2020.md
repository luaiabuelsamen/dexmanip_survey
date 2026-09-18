# dm_control_2020 — dm_control: Software and Tasks for Continuous Control (Tassa, Tunyasuvunakool, Muldal, Doron, Trochim, Liu, Bohez, Merel, Erez, Lillicrap, Heess; DeepMind, Software Impacts 2020, arXiv 2020)

sources: papers/md/dm_control_2020.md [b8604601] ; code/md/dm_control_2020.md [3e9cd0bf]

## One-line contribution
A Python software stack around MuJoCo — a thin `Physics` wrapper, the PyMJCF procedural-model library, the Composer task-authoring framework, and three ready-made task suites (Control Suite, Locomotion, Manipulation) — intended as the standard RL environment layer for continuous-control research (Abstract).

## Setting
- hand(s): none — the shipped Manipulation module uses a robotic arm and a gripper with Lego-Duplo-style snap-together "studded bricks" (Sec. 8.1), not a multi-fingered dexterous hand. The only articulated end-effector referenced in the parsed code is a 3-finger Kinova Jaco gripper (`dm_control/entities/manipulators/kinova/jaco_hand.py`, code/md), which is an underactuated gripper, not a dexterous hand.
- simulator / physics: MuJoCo, accessed through a `Physics` class wrapping `mj_step`, `mj_forward`, `mj_reset`, named indexing into `model`/`data`, and an interactive viewer (Sec. 2). PyMJCF (Sec. 3) generates/attaches MJCF XML programmatically; Composer (Sec. 5) adds an observable/variation/task lifecycle on top for procedural task authoring.
- observation: Control Suite tasks are "strongly observable" by default (state recoverable from a single observation) except `point-mass:hard`; pixel observations can replace or augment feature observations (Sec. 6.1, 6.2). Manipulation tasks offer `features` (arm joint pos/vel/torque + task-specific privileged features) or `vision` (arm joint pos/vel/torque + a fixed 84×84 RGB camera view) variants (Sec. 8).
- action space: unit-box actions a ∈ [−1,1]^dim(A) for all Control Suite domains except LQR (Sec. 6.1).
- objects / data: Manipulation module ships "studded brick" models based on Lego Duplo bricks that snap together under alignment + force and hold via friction (Sec. 8.1); 13 named manipulation tasks from `reach_site` through `reassemble_5_bricks_random_order` (Sec. 8.2). Control Suite Additional domains include Quadruped (56-dim obs, 12 actuators), Dog (158/38/227), Rodent (184/38/64×64×3 pixels), and CMU Motion Capture Data (Sec. 6.3).

## Physics block
- contact model: not re-derived by this paper — it is whatever MuJoCo's own solver implements (soft/regularized rigid contact; see the `mujoco_2012`/`mujoco_convex_contact_2014` entries elsewhere in this corpus for that detail). dm_control exposes it only through `Physics.model`/`Physics.data` and `mj_step`/`mj_forward`, and through touch-sensor-style observables that "are also dependent on controls ... are functions of the previous transition" (Sec. 6.1, "Observation").
- solver and iterations: inherited from MuJoCo; not described independently in this paper.
- differentiability: not discussed — dm_control at this version is a forward-simulation/RL wrapper, with no autodiff-through-physics claim (this predates MJX).
- timestep: "Most domains use MuJoCo's default semi-implicit Euler integrator. A few domains which have smooth dynamics use 4th-order Runge Kutta" (Sec. 6.1, footnote 3). Exact numeric Δt is set per-model in MJCF and is not given as a single value in this paper.
- friction model: not described independently; inherited from MuJoCo. The studded-brick snap-together mechanism "hold[s] together using friction" (Sec. 8.1) but no coefficient or law is given.
- how penetration is resolved / is depth exposed: not discussed in physics terms in this paper; the closest statement is a general caution that "simulated physics can easily destabilise and diverge, mostly due to errors introduced by time discretisation. Smaller time-steps are more stable, but require more computation per unit of simulation time... learning agents are very good at discovering and exploiting instabilities" (Sec. 6.1, "Model and Task verification") — a design/tuning caveat, not a measured penetration number.
- GPU or CPU: not addressed as a backend choice in this paper (pre-dates MJX/GPU MuJoCo); rendering options are discussed (Sec. 2.1 "Rendering") but not a GPU-vs-CPU physics-throughput comparison.
- throughput: not reported — no FPS/steps-per-second table is given anywhere in the parsed text. Episodes are fixed at 1000 timesteps for evaluation-curve comparability (Sec. 6.1, "Evaluation"), which is an RL-protocol convention, not a speed benchmark. For quantitative Control Suite benchmarking numbers the paper explicitly defers: "Please see the original tech report for the Control Suite (Tassa et al., 2018) for detailed benchmarking results" (Sec. 6.2, "Control Suite Benchmarking") — i.e. this paper does not itself contain the numbers.

## Evaluation
- metrics: Control Suite rewards are bounded r(s,a) ∈ [0,1], some "sparse" (r ∈ {0,1}) via the `tolerance()` helper (Sec. 6.1); return is measured over fixed 1000-step episodes so all learning curves share y-axis limits of [0,1000], with "[800,1000]" as the practically-achievable near-optimal band (Sec. 6.1); Manipulation-task reward is likewise r(s,a) ∈ [0,1] per timestep with a 10-second episode time limit (Sec. 8).
- headline numbers: none reported in this paper — it is a software/infrastructure paper, not an experimental results paper; task verification was done qualitatively by running "a variety of learning agents ... against all tasks" and iterating on task design "until we were satisfied that the physics was stable and non-exploitable, and that the task is solved correctly by at least one agent" (Sec. 6.1). Solvable tasks became the `benchmarking` set; unsolved ones became the `extra` set (Sec. 6.1).
- baselines beaten: not applicable (no comparative results in this paper).
- real robot? none.

## Limitations stated by the authors
- Time-discretisation instability is a persistent risk that trades off against compute cost, and "learning agents are very good at discovering and exploiting instabilities" (Sec. 6.1).
- Designing tasks that are neither trivially easy, unintendedly hard, unsolvable, nor solvable by unintended "cheat" strategies is called out as "surprisingly easy" to get wrong, especially since "many continuous control domains cannot be solved by humans with standard input devices" (unlike Atari, which had ALE's decade of human playtesting) so a different validation approach (multi-agent iterative testing) was used instead (Sec. 6.1).

## Quotable claims (verbatim, with section)
- "`dm_control` is a starting place for the testing and performance comparison of reinforcement learning algorithms for physics-based control." (Sec. 9, Conclusion)
- "Most domains use MuJoCo's default semi-implicit Euler integrator. A few domains which have smooth dynamics use 4th-order Runge Kutta." (Sec. 6.1, footnote 3)
- "Simulated physics can easily destabilise and diverge, mostly due to errors introduced by time discretisation." (Sec. 6.1)
- "Please see the original tech report for the Control Suite (Tassa et al., 2018) for detailed benchmarking results of the BENCHMARKING tasks." (Sec. 6.2)

## Notes for the survey
- dm_control ships no dexterous hand in the parsed sources — the only manipulator model referenced is a 3-finger Kinova Jaco gripper (`dm_control/entities/manipulators/kinova/jaco_hand.py`) plus a generic arm+gripper for the brick-manipulation tasks; this note should not be cited as a source of any dexterous-hand physics or benchmark numbers.
- No throughput, contact-model, or penetration numbers are contained anywhere in this paper; every physics-fidelity question routes back to MuJoCo itself (documented elsewhere in the corpus) or to the original 2018 Control Suite tech report, which is not one of the parsed sources.
- The paper's main survey-relevant content is infrastructural: PyMJCF/Composer as a pattern for procedural task/asset generation, and the Control-Suite convention of unit-interval, often-sparse rewards over fixed-length episodes — useful for the survey's "task-authoring tooling" section, not for the physics-comparison table.
- Code md provenance: `code/md/dm_control_2020.md` (79,944 chars) confirms `jaco_hand.py` under `dm_control/entities/manipulators/kinova/` and gives the versioning policy (semantic versioning from 1.0.0; prior to that, an incrementing `0.0.N` build number) but contains no MuJoCo solver source (that lives in the separate `mujoco` package, not in `dm_control`).
