Extra fields required for a METHOD paper note (RL / IL / VLA / MPC), on top of TEMPLATE.md.
Record these explicitly; write "not stated" when the source is silent. Never infer a number.

A. Embodiment block (one line each)
  hand model + DoF + vendor; arm/floating base; bimanual?; simulator + version; physics engine;
  sim timestep and control rate; number of parallel envs; GPU used and wall-clock training time.
B. Learning block
  paradigm (RL / BC / RL+demo / distillation / diffusion / autoregressive VLA / MPC / optimisation);
  algorithm and its implementation (PPO from which repo? DDPG? flow-matching?);
  teacher-student or privileged->vision distillation? what is privileged exactly?
  observation vector, item by item, as the code builds it (cite the file);
  action space and whether it is position targets, torques or residual;
  domain randomisation: list every randomised quantity and its range, from the code if possible.
C. Reward / objective block
  every reward term with its weight, quoted from the paper AND from the code config or reward
  function; note any term present in one and not the other. For IL: the loss and the action
  chunking / horizon. This block is the core of the survey's method comparison; do not summarise it,
  quote it.
D. Contact / penetration handling
  does the method penalise, measure or ignore hand-object interpenetration? quote the term or say
  "not addressed". Note the contact solver settings if given.
E. Evaluation block
  the exact success criterion (threshold in metres / radians / seconds); number of eval episodes or
  seeds; whether numbers are sim or real; real-robot trial counts; what the baselines are and
  whether they were re-run or quoted.
F. Reproducibility
  code released? checkpoints? assets? which of the paper's tables can be reproduced from the repo as
  parsed in code/md/<key>.md?
