# tactile_genesis_2026

source: https://github.com/neuroagents-lab/tactile-genesis


commit: 3023bcd2d43fe947327713ddce3c2123d475735d


## README

# Tactile Genesis

> !! Please note, this is not the final version of the paper. We plan to update ALL experiments with latest version of Genesis World. !!

https://github.com/user-attachments/assets/9d8bb278-fbc8-41f4-b1b2-ab9ce572c294

This repository reflects the self-contained code snapshot to reproduce the paper, [Tactile Genesis](https://arxiv.org/abs/2606.22332).
**Please note**, if you wish to use tactile sensors for your own project, use the latest [Genesis World](https://github.com/Genesis-Embodied-AI/genesis-world) physics engine which includes our tactile sensors,
and optionally, the official [Eden](https://github.com/embodied-ai-nexus/Eden) (not yet available, but will be released before end of 2026) if you require a managed learning framework.

## Structure

| Directory | Package | Role |
|---|---|---|
| [`dexterous-hands/`](dexterous-hands/) | `tactile_genesis` | Tactile dexterous-hand RL tasks, robots, sensors, training/eval entrypoints. |
| [`Eden/`](Eden/) | `eden` | RL environment framework built on Genesis + rsl_rl. Declarative Pydantic configs, manager/term registries. |
| [`Genesis/`](Genesis/) | `genesis-world` | The physics-simulation backend (rigid/MPM/SPH/FEM/PBD). |
| [`rsl_rl/`](rsl_rl/) | `rsl-rl-lib` | PPO + student/teacher distillation training loop. |

Dependency topology: `dexterous-hands` → `Eden` → `Genesis`, with `rsl_rl` as the training loop.

## How the packages are wired

`dexterous-hands/pyproject.toml` resolves the three dependencies from the sibling
checkouts via `[tool.uv.sources]` (editable path installs). These sources override the
package origin across the whole resolution graph, so Eden's own transitive
`genesis-world` / `rsl-rl-lib` requirements also point at the local checkouts:

```toml
[tool.uv.sources]
eden          = { path = "../Eden",    editable = true }
genesis-world = { path = "../Genesis", editable = true }
rsl-rl-lib    = { path = "../rsl_rl",  editable = true }
```

## Quickstart

Everything is run from `dexterous-hands/`:

```bash
cd dexterous-hands
uv sync  # installs eden, genesis-world, rsl-rl-lib from local
uv run python main.py --task=in_hand_repose --robot=xhand1 --cpu
```

See [`dexterous-hands/README.md`](dexterous-hands/README.md) for the full task/robot list, run modes, and tooling scripts.

## Citation

If you use or reference our simulated tactile sensors in any way, please cite:

```bibtex
@article{chung2026tactilegenesis,
  title   = {Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks},
  author  = {Chung, Trinity and Yamazaki, Kashu and Patel, Dhruv and Duburcq, Alexis and Qiao, Yiling and Fragkiadaki, Katerina and Nayebi, Aran},
  journal = {arXiv preprint arXiv:2606.22332},
  year    = {2026},
  url     = {https://arxiv.org/abs/2606.22332}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
Eden/
  .gitignore
  .pre-commit-config.yaml
  LICENSE
  README.md
  eden/
    __init__.py
    __main__.py
    _logging.py
    constants.py
    entities/
    envs/
    extensions/
    managers/
    options/
    tasks/
    terms.py
    types.py
    utils/
  pyproject.toml
Genesis/
  .gitattributes
  .gitignore
  .pre-commit-config.yaml
  AGENTS.md
  LICENSE
  MANIFEST.in
  README.md
  examples/
    sensors/
  genesis/
    __init__.py
    _main.py
    constants.py
    datatypes.py
    engine/
    ext/
    grad/
    logging/
    options/
    recorders/
    repr_base.py
    styles.py
    typing.py
    utils/
    version.py
    vis/
  pyproject.toml
  tests/
    __init__.py
    benchmark_tactile_sensors.py
    conftest.py
    monitor_test_mem.py
    run_benchmarks.py
    scaling_repro.py
    test_audio_sensors.py
    test_backend_switching.py
    test_bvh.py
    test_deformable_physics.py
    test_examples.py
    test_fem.py
    test_grad.py
    test_hybrid.py
    test_imgui_overlay.py
    test_integration.py
    test_ipc.py
    test_kinematic.py
    test_mesh.py
    test_misc.py
    test_pbd.py
    test_quadrants.py
    test_recorders.py
    test_render.py
    test_rigid_benchmarks.py
    test_rigid_physics.py
    test_rigid_physics_analytical_vs_gjk.py
    test_rigid_physics_sparse.py
    test_sensor_camera.py
    test_sensors.py
    test_sph.py
    test_usd.py
    test_utils.py
    test_viewer.py
    upload_benchmarks_table_to_wandb.py
    utils.py
README.md
dexterous-hands/
  .env.example
  .gitattributes
  .gitignore
  .python-version
  LICENSE
  README.md
  conf/
    distill_configs.yaml
    experiments/
    sample_grasps/
    sensor/
  main.py
  pyproject.toml
  scripts/
    expand_distill_config.py
    grasps_generator.py
    imgui_panels.py
    manual_calibration_gui.py
    robot_dofs_viewer.py
    sensor_probes_selector.py
    sensors_viewer.py
    slurm/
    submit_distill.sh
    task_viewer.py
  src/
    __init__.py
    calibration/
    deploy.py
    entities/
    model_config.py
    models/
    optimization.py
    registry.py
    shared_terms.py
    tactile_compare.py
    tactile_record.py
    tactile_sensors.py
    task_mods.py
    tasks/
    utils.py
rsl_rl/
  .gitignore
  .pre-commit-config.yaml
  CITATION.cff
  CONTRIBUTING.md
  CONTRIBUTORS.md
  LICENSE
  README.md
  licenses/
    dependencies/
  pyproject.toml
  rsl_rl/
    __init__.py
    algorithms/
    env/
    extensions/
    models/
    modules/
    runners/
    storage/
    utils/
  ruff.toml
  setup.py
  uv.lock
```

## Config files (9)


### Eden/.pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.10
    hooks:
      - id: ruff-check
      - id: ruff-format
  - repo: https://github.com/google/yamlfmt
    rev: v0.16.0
    hooks:
      - id: yamlfmt
  - repo: https://github.com/pappasam/toml-sort
    rev: v0.24.2
    hooks:
      - id: toml-sort-fix

```

### Genesis/.pre-commit-config.yaml

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.14.11
  hooks:
    # Run the formatter.
    - id: ruff-check
    # Run the formatter.
    - id: ruff-format

```

### dexterous-hands/conf/distill_configs.yaml

```yaml
# Distillation sweeps consumed by scripts/submit_distill.sh.
#
# Each entry under `configs:` is one (task, robot, teacher) sweep, selected by
# name on the command line, e.g.
#   `bash scripts/submit_distill.sh types screwdriver-xhand1`.
# `defaults:` is the menu of options shared by every entry; per-entry fields
# (task/robot/teacher/placements/extra_flags/...) override or extend it.
#
# The submit script picks a *subset* of this menu based on its first arg
# `<mode>`:
#   - <mode>=types   -> sweep sensor_types at the pinned baseline
#                       (sensor_types x [pinned_resolution] x [pinned_noisy]),
#                       prefixed with `none`. tactile_encoder is auto-picked
#                       per sensor (grid sensors -> tactile_convrnn,
#                       gridless/`none` -> rnn).
#   - <mode>=models  -> sweep tactile_encoders at the pinned baseline against
#                       models_sensor_types (models_sensor_types x
#                       [pinned_resolution] x [pinned_noisy] x tactile_encoders).
#                       No `none` (baseline doesn't depend on encoder).
#   - <mode>=<type>  -> focused sweep on one sensor type
#                       ([type] x sensor_resolutions x noisy_modes), prefixed
#                       with `none`. tactile_encoder auto-picked per sensor.
#
# `sensor_placements` x the chosen resolutions form placements; placements then
# cross-product with the chosen sensor_types x noisy_modes.

defaults:
  # --- Menus (focused sweeps iterate over the full list) ---
  sensor_resolutions: [low, med, high]
  sensor_types: [bool, depth, proximity, agg_force, force, force_torque, elastomer]
  noisy_modes: [false, true]
  tactile_encoders: [tactile_cnn, tactile_convrnn, rnn, mlp, tactile_canvas_cnn, tactile_canvas_convrnn]

  # --- Pinned baseline (used by `types` and `models` modes) ---
  pinned_resolution: med
  pinned_noisy: false

  # --- `models` mode subset: which sensor types to cross with tactile_encoders ---
  # models_sensor_types: [bool, force_torque, elastomer]
  models_sensor_types: [force_torque]

  # How TactileSensorRead reduces the within-step substep history (DECIMATION=5).
  # none   -- keep all 5 substeps as extra features per probe (5x wider obs)
  # median -- per-element median across substeps (old default; noise-robust)
  # last   -- keep only the final substep
  temporal_reduction: none

  # Total training iterations per student job. Overrides the task's
  # RUNNER_CFG['max_iterations']. Leave unset (or null) to keep the task default.
  # Per-config entries below can also set this individually.
  max_iters: null

configs:
  in_palm_rotate-xhand1:
    task: in_palm_rotate
    robot: xhand1
    teacher_checkpoint: checkpoints/teachers/in_palm_rotate-xhand1.pt
    extra_flags: [--obj=primitives]
    sensor_placements: [tips, hand]
    max_iters: 6000


  in_palm_rotate-xhand1-models:
    task: in_palm_rotate
    robot: xhand1
    teacher_checkpoint: checkpoints/teachers/in_palm_rotate-xhand1.pt
    extra_flags: [--obj=primitives]
    sensor_placements: [hand]
    tactile_encoders: [tactile_cnn, tactile_convrnn, tactile_convrnn_lstm, tactile_convrnn_big, rnn, mlp, tactile_canvas_cnn, tactile_canvas_convrnn]
    pinned_resolution: med
    max_iters: 6000

  screwdriver-xhand1:
    task: screwdriver
    robot: xhand1
    teacher_checkpoint: checkpoints/teachers/screwdriver-xhand1.pt
    # Block form: commas inside a value would otherwise split flow lists.
    extra_flags:
      - --no-include_ext_force
    sensor_placements: [fingers] # [tips, fingers]
    max_iters: 2000

  in_hand_repose-xhand1:
    task: in_hand_repose
    robot: xhand1
    teacher_checkpoint: checkpoints/teachers/in_hand_repose-xhand1.pt
    extra_flags: [--obj=primitives]
    sensor_placements: [hand]
    max_iters: 6000

  in_hand_repose-sharpa:
    task: in_hand_repose
    robot: sharpa
    teacher_checkpoint: checkpoints/teachers/in_hand_repose-sharpa.pt
    extra_flags: [--obj=primitives]
    sensor_placements: [hand]
    max_iters: 6000

  # screwdriver-sharpa:
  #   task: screwdriver
  #   robot: sharpa
  #   teacher_checkpoint: checkpoints/teachers/screwdriver-sharpa.pt
  #   extra_flags:
  #     - --no-include_ext_force
  #   sensor_placements: [fingers] # [tips, fingers]

```

### dexterous-hands/conf/experiments/tiny.yaml

```yaml
# Tiny smoke-test config: 4 envs, 10 iterations, TensorBoard logging (no W&B
# login needed). Used by the README's local CPU smoke test:
#   uv run python main.py --task=<task> --robot=<robot> --cpu --config=conf/experiments/tiny.yaml
env_options:
  num_envs: 4
runner_options:
  max_iterations: 10
  num_steps_per_env: 24
  logger: tensorboard

```

### dexterous-hands/conf/sample_grasps/screwdrivers_sharpa.yaml

```yaml
# Grasp sampling config for Sharpa + plug_insertion task.
# The hand grasps the plug body (prongs pointing down) so it can be pushed into
# the socket. Seed pose adapted from the screwdriver XHand1 grasp config.
grasp_generation:
  num_envs: 1024
  num_grasps: 64
  perturb_range: 0.2
  # Require enough configured surface-distance sensors below threshold.
  required_num_surface_distance_fingers: 3
  surface_distance_threshold: 0.01
  max_penetration: 0.003
  max_displacement: 0.01
  # Keep the object near the seeded hand-relative pose while bootstrapping grasps.
  obj_pos_shift: "-0.01,0.01,-0.01,0.01,0.0,0.0"
  obj_euler_range: "0,0,0,0,-180,180"
  bottom_aligned: true
  output_file: src/assets/grasps/screwdrivers_sharpa_grasps_64.pt

scene_options:
  robot:
    default_root_pos: [-0.055000, -0.020000, 0.290000]
    default_root_quat: [0.500000, 0.000000, 0.866025, 0.000000]
    default_dofs_pos:
      right_thumb_CMC_FE: 1.490000
      right_thumb_CMC_AA: -0.190000
      right_thumb_MCP_FE: 0.200000
      right_thumb_MCP_AA: -0.020000
      right_thumb_IP: 0.350000
      right_index_MCP_FE: 0.860000
      right_index_MCP_AA: 0.000000
      right_index_PIP: 0.340000
      right_index_DIP: 0.610000
      right_middle_MCP_FE: 0.770000
      right_middle_MCP_AA: 0.020000
      right_middle_PIP: 0.680000
      right_middle_DIP: 0.340000
      right_ring_MCP_FE: 0.000000
      right_ring_MCP_AA: 0.000000
      right_ring_PIP: 0.000000
      right_ring_DIP: 0.000000
      right_pinky_CMC: 0.000000
      right_pinky_MCP_FE: 0.000000
      right_pinky_MCP_AA: 0.000000
      right_pinky_PIP: 0.000000
      right_pinky_DIP: 0.000000
  obj:
    default_root_pos: [0.000000, 0.000000, 0.0]
    default_root_quat: [0.707107, 0.707107, 0.000000, 0.000000]

```

### dexterous-hands/conf/sample_grasps/screwdrivers_xhand1.yaml

```yaml
# Grasp sampling config for XHand1 + screwdriver task (right-hand, link2 runtime links).
# Joint seed mapped from DexScrew screwdriver_inclined and adapted for right-hand XHand1.
grasp_generation:
  num_envs: 1024
  num_grasps: 64
  # Broaden joint exploration around the seed so sampler can escape
  # the local penetrating basin.
  perturb_range: 0.2
  # Condition 1: require enough configured surface-distance sensors below threshold.
  required_num_surface_distance_fingers: 3
  surface_distance_threshold: 0.02
  # Tighten penetration acceptance so retained grasps are cleaner.
  max_penetration: 0.003
  max_displacement: 0.01
  # Keep the object near the seeded hand-relative pose while bootstrapping grasps.
  obj_pos_shift: "-0.01,0.01,-0.01,0.01,0.0,0.0"
  obj_euler_range: "0,0,0,0,-180,180"
  bottom_aligned: true
  output_file: src/assets/grasps/screwdrivers_xhand1_grasps_64.pt

scene_options:
  robot:
    default_root_pos: [0.015, -0.055, 0.25]
    default_root_quat: [0.405580, -0.579228, 0.579228, 0.405580]
    default_dofs_pos:
      right_hand_thumb_bend_joint: 1.440000
      right_hand_index_bend_joint: 0.000000
      right_hand_mid_joint1: 1.250000
      right_hand_ring_joint1: 0.000000
      right_hand_pinky_joint1: 0.000000
      right_hand_thumb_rota_joint1: 0.340000
      right_hand_index_joint1: 1.270000
      right_hand_mid_joint2: 0.590000
      right_hand_ring_joint2: 0.000000
      right_hand_pinky_joint2: 0.000000
      right_hand_thumb_rota_joint2: 0.500000
      right_hand_index_joint2: 0.550000
  obj:
    default_root_pos: [0.000000, 0.000000, 0.0]
    default_root_quat: [0.707107, 0.707107, 0.000000, 0.000000]

```

### dexterous-hands/conf/sensor/tactile_params.yaml

```yaml
# Tactile sensor construction kwargs, keyed by sensor type (see
# TACTILE_SENSORS in src/tactile_sensors.py). Each block has two parts:
#
#   params:       base kwargs forwarded to the matching `gs.sensors` class.
#   noise_params: extra kwargs layered on top of `params` when a sensor is
#                 requested with a trailing `/noisy` flag (see
#                 `TactileSensorsMod`). Empty (or missing) makes `/noisy` a
#                 no-op for that sensor type.
#
# noise knobs come from `genesis/options/sensors/{options,tactile}.py`:
#   noise                     - std of additive white noise (sensor output units)
#   bias                      - constant additive offset
#   random_walk               - std of slow bias drift
#   resolution                - quantization step
#   probe_radius_noise        - sensing-radius uncertainty (m)
#   dead_taxel_probability    - per-reset Bernoulli chance a taxel goes dead
#   probe_gain_resample_range - per-reset uniform multiplicative gain scatter
#   hysteresis_strength / hysteresis_tau - viscoelastic loading/unloading loop
#
# Noise magnitudes are tuned to be plausible for low-cost tactile hardware --
# enough to make a distilled student robust to the sim-to-real gap without
# drowning the signal. Crosstalk (`crosstalk_strength`) is intentionally
# omitted from contact-depth probes: it needs a regular-grid `probe_local_pos`
# layout the flat probe configs do not have.
#
# Top-level keys starting with `_` are anchor holders, ignored by the loader.

_anchors:
  # Shared kinematic-taxel base params (force, force_torque).
  kin_taxel: &kin_taxel
    normal_stiffness: 500.0
    normal_damping: 1.0
    normal_exponent: 1.2
    shear_scalar: 2.0
    twist_scalar: 2.0
    debug_probe_color: [0.4, 0.7, 1.0]
    debug_contact_color: [1.0, 0.4, 0.4]

  # Shared noise model for ContactDepthProbe-based sensors (depth, agg_force).
  contact_depth_noise: &contact_depth_noise
    noise: 2.0e-4                       # m, ~20 um white noise on contact depth
    resolution: 1.0e-4                  # m, depth quantization step
    probe_radius_noise: 3.0e-4          # m, sensing-radius uncertainty
    dead_taxel_probability: 0.05
    probe_gain_resample_range: [0.85, 1.15]   # per-reset calibration scatter
    hysteresis_strength: 0.5            # viscoelastic loading/unloading loop
    hysteresis_tau: 0.05                 # s, hysteresis relaxation time constant

  # Shared noise model for KinematicTaxel-based sensors (force, force_torque).
  kin_taxel_noise: &kin_taxel_noise
    noise: 0.005                 # N, white-noise std
    random_walk: 0.0001          # N, slow bias drift
    resolution: 0.01
    probe_radius_noise: 3.0e-4  # m, sensing-radius uncertainty
    dead_taxel_probability: 0.05
    probe_gain_resample_range: [0.85, 1.15]
    # crosstalk_strength: 0.1
    # crosstalk_sigma: 0.1
    hysteresis_strength: 0.5
    hysteresis_tau: 0.05

# --- boolean contact -------------------------------------------------------
# A thresholded bit, so the realistic imperfection is white noise near the
# threshold (Contact) or intermittently dead taxels (ContactProbe).

link_bool:
  params: {}
  noise_params:
    noise: 0.03   # white-noise std on the pre-threshold contact magnitude

bool:
  params:
    contact_threshold: 0.0005
  noise_params:
    release_threshold: 0.0002   # schmitt trigger hysteresis
    dead_taxel_probability: 0.05   # per-reset Bernoulli chance a taxel goes dead

# Same ContactProbe as `bool`; the postprocess collapses the per-link taxel
# bits into a single bit (true iff > AGG_BOOL_TAXEL_COUNT_THRESHOLD taxels
# read true).
agg_bool:
  params:
    contact_threshold: 0.0005
  noise_params:
    release_threshold: 0.0002
    dead_taxel_probability: 0.05

# --- aggregate per-link contact force (ContactForce), in Newtons -----------
link_force:
  params:
    min_force: 0.0001   # minimum detectable force
    max_force: 10.0     # maximum force to clip at
  noise_params:
    noise: 0.08         # N, white-noise std per axis
    random_walk: 0.01   # N, slow bias drift
    resolution: 0.005   # N, ADC quantization step

# --- per-probe contact depth (ContactDepthProbe), in meters ----------------
# `agg_force` shares the depth noise model since it is a ContactDepthProbe
# scaled inside the postprocess func.
depth:
  params: {}
  noise_params: *contact_depth_noise

agg_force:
  params: {}
  noise_params: *contact_depth_noise

# --- per-probe force estimate (KinematicTaxel), in Newtons -----------------
force:
  params: *kin_taxel
  noise_params: *kin_taxel_noise

force_torque:
  params: *kin_taxel
  noise_params: *kin_taxel_noise

# --- per-probe proximity force estimate (ProximityTaxel), in Newtons -------
# R_eff is resampled every step when `probe_radius_noise` is non-zero.
proximity:
  params:
    probe_radius: 0.01
    n_sample_points: 1000
    stiffness: 300.0
    shear_coupling: 10.0
    debug_point_cloud_radius: 0.001
    debug_point_cloud_color: [1.0, 0.8, 0.0, 0.3]
    debug_probe_color: [0.4, 0.7, 1.0]
    debug_probe_sphere_opacity: 0.1
    debug_contact_color: [1.0, 0.4, 0.4]
  noise_params:
    noise: 0.01
    random_walk: 0.001
    resolution: 0.01
    probe_radius_noise: 6.0e-4   # m, per-step sensing-radius noise
    dead_taxel_probability: 0.05
    probe_gain_resample_range: [0.85, 1.15]
    hysteresis_strength: 0.5
    hysteresis_tau: 0.05

# --- per-marker displacement (ElastomerTaxel), in meters -------------------
elastomer:
  params:
    n_sample_points: 1000
    lambda_d: 8000.0
    lambda_s: 2000.0
    dilate_scale: 100.0
    shear_scale: 200.0
    normal_exponent: 1.2
    debug_point_cloud_radius: 0.001
    debug_point_cloud_color: [1.0, 0.8, 0.0, 0.3]
    debug_probe_color: [0.4, 0.7, 1.0]
    debug_contact_color: [1.0, 0.4, 0.4]
  noise_params:
    noise: 0.0001                # m, white-noise std on marker displacement
    random_walk: 0.00001
    resolution: 0.0001
    probe_radius_noise: 3.0e-4   # m, sensing-radius uncertainty
    dead_taxel_probability: 0.05
    probe_gain_resample_range: [0.85, 1.15]
    hysteresis_strength: 0.5
    hysteresis_tau: 0.05

```

### dexterous-hands/conf/sensor/xhand1_deploy_sensor_params.yaml

```yaml
# Calibration parameters for the real xhand1 fingertip tactile sensors.
#
# `scale` multiplies the real fingertip force reading (`calc_pressure`, the
# [fx, fy, fz] vector) during deployment so it matches the simulated
# `agg_force` magnitude. The scaled value feeds both the policy observation
# and the real-vs-sim recording/plot.
#
# Tune it: run `python main.py --mode deploy --robot xhand1 --sensors agg_force
# ... --record_tactile`, compare the real vs sim traces, and adjust until they
# line up. `per_finger` overrides `scale` for individual fingers
# (thumb/index/mid/ring/pinky); omit a finger to use the global `scale`.

scale: 1000.0
per_finger: {
  # thumb: 1000.0,
  # index: 1000.0,
  # mid: 1000.0,
  # ring: 1000.0,
  # pinky: 1000.0,
}

# Per-axis multiplier on `calc_pressure` [fx, fy, fz], applied together with
# `scale`. The real xhand1 sensor reports fx and fy with the opposite sign to
# sim, so flip them; fz keeps its sign.
axis_scale: [-1.0, -1.0, 1.0]

```

### rsl_rl/.pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.0
    hooks:
      - id: ruff-check
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-symlinks
      - id: destroyed-symlinks
      - id: check-yaml
      - id: check-toml
      - id: check-merge-conflict
      - id: check-case-conflict
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: detect-private-key
  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.6
    hooks:
      - id: codespell
        additional_dependencies:
        - tomli
  - repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.5.1
    hooks:
      - id: insert-license
        files: \.py$
        args:
          # - --remove-header    # Remove existing license headers. Useful when updating license.
          - --license-filepath
          - .github/LICENSE_HEADER.txt

```

## Python signatures and reward/observation bodies (103 files)


### Eden/eden/envs/__init__.py

```
"""Vectorized environment base classes and wrappers."""
```

### Eden/eden/envs/base.py

```
"""Core vectorized environment base classes: EnvBase and RLEnvBase.

The class hierarchy mirrors the config hierarchy in :mod:`eden.utils.configs`:

- :class:`EnvBase` — scene, entities, sensors, and the action/observation/event managers.
- :class:`RLEnvBase` — adds reward, termination, command, and curriculum managers plus the RL ``step``.

Build environments with ``RLEnvBase.from_config(cfg)`` (not ``from_cfg``); the ``config``
property reconstructs the config object. In :meth:`RLEnvBase.step`, auto-reset happens
**after** reward/termination but **before** observation, so the returned observati"""
def _entity_class_for_options(options)
class EnvBase(DrawDebugMixin, RBC)
    """Base class for all environments.

Parameters
----------
env_options: EnvOptions
    Environment options.
scene_options: SceneOptions
    Scene options.
observation_options: ObservationManagerOptions
    Observation manager options.
event_options: EventManagerOptions
    Event manager options.
action"""
    def __init__(self, env_options, scene_options, observation_options, event_options, action_options, metric_options, recorder_options, cameras_options, sensors_options, renderer_options)
    def from_config(cls, cfg)
    def _setup_cameras(self)
    def _setup_sensors(self)
    def register_pre_build_hook(self, hook)
    def register_post_build_hook(self, hook)
    def build(self, env_spacing, center_envs_at_origin)
    def pre_build_setup(self)
    def post_build_setup(self)
    def _verify_build(self)
    def destroy(self)
    def _load_managers(self)
    def summary(self)
    def seed(seed)
    def _all_indices(self)
    def is_built(self)
    def coupler(self)
    def _has_ipc_coupler(self)
    def rigid_solver(self)
    def segmentation_idx_dict(self)
    def device(self)
    def config(self)
    def gravity(self)
    def set_global_sol_params(self, sol_params)
    def set_sol_params(self, sol_params, geoms_idx, envs_idx)
    def get_entity(self, name)
    def get_entities(self, names)
    def get_camera(self, name)
    def reset(self, envs_idx)
    def step(self, action)
    def _scene_step_with_sensor_gating(self, is_last_substep)
    def _compute_sensor_substep_skip_safe(self)
    def _reset_idx(self, envs_idx)
class RLEnvBase(EnvBase)
    """Base class for all RL environments.

Parameters
----------
env_options: EnvOptions
    Environment options.
observation_options: ObservationManagerOptions
    Observation manager options.
reward_options: RewardManagerOptions
    Reward manager options.
termination_options: TerminationManagerOptions
"""
    def __init__(self, env_options, scene_options, observation_options, reward_options, termination_options, event_options, curriculum_options, command_options, action_options, metric_options, recorder_options, cameras_options, sensors_options, renderer_options)
    def from_config(cls, cfg)
    def _load_managers(self)
    def summary(self)
    def config(self)
    def unwrapped(self)
    def step(self, action)
    def _compute_final_observations(self)
    def _record_final_observations(self)
    def _copy_into_final_obs_cache(cls, source, cache, mask)
    def _reset_idx(self, envs_idx)

```python
def _compute_final_observations(self) -> dict[str, torch.Tensor | dict[str, torch.Tensor]]:
        """Return the pre-reset observation dict for snapshotting (hook).

        Default: full-batch ``observation_manager.compute(update_history=False)``.
        ``update_history=False`` is critical — the post-reset compute at the
        end of ``step()`` advances the history buffer once with
        ``update_history=True``; advancing here too would skip a frame on
        non-done envs. For history-bearing groups the manager still computes
        the fresh post-physics frame and exposes it in the most-recent slot of
        the returned tensor (via ``CircularBuffer.peek_buffer``), without
        mutating the underlying buffer. Subclass to swap in motion-frame
        indices or skip groups whose terms are unsafe to evaluate against the
        post-physics state.
        """
        return self.observation_manager.compute(update_history=False)
```

```python
def _record_final_observations(self) -> dict[str, torch.Tensor | dict[str, torch.Tensor]]:
        """Snapshot ``_compute_final_observations`` into the cached ``_final_obs_cache``.

        Only the rows for ``self.reset_buf`` are kept.

        Allocates the cache lazily; rebuilds the cache when the source
        tensor's shape or dtype changes (e.g. when the env is rebuilt at a
        different ``num_envs``). The slice-copy from ``snapshot[reset_buf]``
        is required, not just an allocation optimization — for
        history-bearing groups ``compute(update_history=False)`` returns a
        view into ``CircularBuffer.buffer`` that the post-reset
        ``compute(update_history=True)`` mutates.
        """
        snapshot = self._compute_final_observations()
        return self._copy_into_final_obs_cache(snapshot, self._final_obs_cache, self.reset_buf)
```
```

### Eden/eden/envs/draw_debug_mixin.py

```
"""Mixin adding debug-draw helpers (points, arrows, frames) to environments."""
class DrawDebugMixin()
    """Mixin providing debug drawing pass-throughs to the Genesis scene."""
    def draw_debug_line(self, start, end, radius, color)
    def draw_debug_arrow(self, pos, vec, radius, color)
    def draw_debug_frame(self, T, axis_length, origin_size, axis_radius)
    def draw_debug_frames(self, Ts, axis_length, origin_size, axis_radius)
    def draw_debug_mesh(self, mesh, pos, T)
    def draw_debug_sphere(self, pos, radius, color)
    def draw_debug_spheres(self, poss, radius, color)
    def draw_debug_box(self, bounds, color, wireframe, wireframe_radius)
    def draw_debug_points(self, poss, colors)
    def draw_debug_path(self, qposs, entity, link_idx, density, frame_scaling)
    def clear_debug_object(self, node)
    def clear_debug_objects(self)
```

### Eden/eden/envs/wrappers/rsl_rl_env.py

```
"""RSL RL environment wrapper for Eden.

Auto-detects the installed ``rsl_rl`` version and translates the runner
config dict accordingly.

Usage::

    from eden.envs.wrappers.rsl_rl_env import RslRlVecEnvWrapper, make_rsl_rl_runner

    env = RslRlVecEnvWrapper.from_config(config)
    runner = make_rsl_rl_runner(env)"""
class RslRlVecEnvWrapper(VecEnv, Env)
    """Wrapper for RSL RL environments.

Works with rsl_rl v3 / v4 / v5 — the ``VecEnv`` interface is identical
across all versions.  The ``runner_dict`` property automatically
translates the Eden config to whatever format the installed version
expects.

Parameters
----------
env: RLEnvBase
    The environ"""
    def __init__(self, env, options)
    def from_config(cls, cfg)
    def runner_dict(self)
    def config(self)
    def class_name(cls)
    def unwrapped(self)
    def dt(self)
    def episode_length_buf(self)
    def episode_length_buf(self, value)
    def seed(self, seed)
    def get_observations(self)
    def reset(self)
    def step(self, actions)
    def close(self)
    def _configure_gym_env_spaces(self)
class DDPRunnerMixin()
    def __init__(self)
    def _configure_multi_gpu(self)
class DDPOnPolicyRunner(DDPRunnerMixin, OnPolicyRunner)
    """Drop-in replacement for :class:`OnPolicyRunner` for Eden's single-GPU-per-process setup.

Expects the NCCL process group to be **already initialized** by
``eden.init()``.  The device is always ``cuda:0`` because
``CUDA_VISIBLE_DEVICES`` restricts each process to one physical GPU.

Usage
-----
``torc"""
class DDPDistillationRunner(DDPRunnerMixin, DistillationRunner)
    """Drop-in replacement for :class:`DistillationRunner` for Eden's single-GPU-per-process setup.

Expects the NCCL process group to be **already initialized** by
``eden.init()``.  The device is always ``cuda:0`` because
``CUDA_VISIBLE_DEVICES`` restricts each process to one physical GPU.

Usage
-----
``"""
def _detect_std_type(runner_dict)
def _maybe_convert_legacy_checkpoint(path)
def _audit_rsl_rl_checkpoint_keys(runner, checkpoint_path, device)
def make_rsl_rl_runner(env, checkpoint, log_dir)

```python
def get_observations(self) -> TensorDict:
        obs_dict = self.unwrapped.observation_manager.compute()
        return TensorDict(cast(dict[str, Any], obs_dict), batch_size=[self.num_envs])
```
```

### Eden/eden/extensions/deployment/robotera_xhand.py

```
"""RobotEra XHand real-robot deployment backend."""
class RoboTeraXHandDeployment(DeploymentBase)
    """Deployment backend for the RoboTera XHand1 dexterous hand.

Supports both EtherCAT and RS485 communication protocols.  For RS485 you
must also set ``serial_port`` and ``baud_rate`` to match your hardware.

The hand is treated as a fixed-base robot: ``read_state`` returns an
identity quaternion and z"""
    def __init__(self, env, options)
    def connect(self)
    def close(self)
    def init_sequence(self)
    def read_state(self)
    def send_payload(self, payload)
    def _set_finger_mode(self, mode)
    def reset_sensor(self, sensor_id)
    def set_hand_id(self, new_id)
    def _sdk_version(self)
    def _serial_number(self)
    def _hand_type(self)
```

### Eden/eden/managers/action_manager.py

```
"""Action manager and ActionTerm base: map policy actions to actuator commands.

The manager slices the policy action vector across its active :class:`ActionTerm`
instances and applies them every control step (re-applied across ``decimation``
physics sub-steps). ``ActionManager.dofs_order`` maps dof-name -> action index; mind
the DOF-ordering caveat in :mod:`eden.entities.rigid` when wiring actions to joints."""
class ActionTerm(ManagerTermBase, ?)
    """Base class for action terms."""
    def __init__(self, env, options)
    def build(self)
    def entity(self)
    def action(self)
    def prev_action(self)
    def dofs_order(self)
    def action_dim(self)
    def num_dofs(self)
    def apply_actions(self)
class ActionManager(?)
    """Action manager for processing actions sent to the environment."""
    def __init__(self, env, options)
    def summary(self)
    def total_action_dim(self)
    def action_term_dim(self)
    def total_dofs_dim(self)
    def dofs_term_dim(self)
    def action(self)
    def prev_action(self)
    def reset(self, envs_idx)
    def compute(self, action)
    def apply_actions(self)
    def _prepare_terms(self)
```

### Eden/eden/managers/modifiers/actions/__init__.py

```
"""Action-term modifiers."""
```

### Eden/eden/managers/modifiers/actions/actuators.py

```
"""Composable action modifiers for action terms.

Action modifiers sit between action terms and the physics engine. They
intercept and transform processed actions (target positions/velocities)
and/or control torques via composable operations like clipping, delay,
friction, and motor strength scaling.

Modifiers are designed to be composed together using :class:`Compose`,
similar to ``torchvision.transforms.Compose``::

    modifiers = Compose.configure(
        modifiers=[
            ActionDelay.configure(min_delay=1, max_delay=3),
            FrictionModel.configure(),
            EffortClip.co"""
def _per_dof_float_row(values, n_dof, device)
def _get_param_tensor_from_entity(param_value)
def _explicit_lax_to_tensor(values)
def _get_entity_spec(entity, dofs_idx_local, attr)
def _tanh_friction(ctrl_torque, dofs_vel, dofs_static_friction, dofs_dynamic_friction, friction_activation_vel, friction_offset)
def _clip_effort(dofs_torque, dofs_vel, driving_torque_limit, braking_torque_limit, full_torque_speed, no_load_speed)
def _compute_effort_limit(max_effort, dofs_vel, full_torque_speed, no_load_speed)
class Compose(ActionModifier)
    """Chains multiple action modifiers in sequence.

Parameters
----------
modifiers : tuple[ActionModifierOptions, ...] | list[ActionModifierOptions]
    Ordered sequence of modifier configurations. Each modifier's
    ``modify_processed_action`` and ``modify_ctrl_torque`` are called
    in sequence.

Ex"""
    def __init__(self, env, options)
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_processed_action(self, processed_action)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
    def get(self, cls)
class ActionDelay(ActionModifier)
    """Delays processed actions by a stochastic number of physics steps.

At each reset, a new random delay is sampled uniformly from
``[min_delay, max_delay]`` for the reset environments.

Parameters
----------
min_delay : int
    Minimum command delay in physics steps (inclusive).
max_delay : int
    Max"""
    def __init__(self, env, options)
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_processed_action(self, processed_action)
class FrictionModel(ActionModifier)
    """Applies tanh-based static + viscous dynamic friction to torques.

By default, friction parameters are read from the entity's actuator
spec (``dofs_spec``).  Explicit values override the entity defaults.

Parameters
----------
static_friction : LaxFArrayType | None
    Static friction coefficient per"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class EffortClip(ActionModifier)
    """Clips torques to motor torque-speed (T-N) curve limits.

By default, T-N curve parameters are read from the entity's actuator
spec (``dofs_spec``).  Explicit values override the entity defaults.

Parameters
----------
driving_torque_limit : LaxFArrayType | None
    Maximum torque when torque and vel"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class MotorStrength(ActionModifier)
    """Scales control torques by a motor strength multiplier.

Parameters
----------
motor_strength : LaxFArrayType
    Per-DOF multiplier, or a scalar broadcast to every controlled DOF.

Note
----
This modifier provides a deterministic motor strength multiplier.
If you want to randomize the motor strength"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class TorqueOffset(ActionModifier)
    """Adds a constant offset to the control torques.

Parameters
----------
torque_offset : LaxFArrayType
    Per-DOF offset, or a scalar broadcast to every controlled DOF."""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class ConstantTorqueKick(ActionModifier)
    """Adds a flat directional torque on top of computed control torque.

This acts like a minimum drive effort: when the joint has a nonzero position
error, the modifier adds ``torque_kick`` in the direction of that error. It
is useful for matching actuators that move sharply through small errors or
have """
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class Deadband(ActionModifier)
    """Zeroes PD control torque inside a position-error deadband.

No torque is applied when the instantaneous position error ``|pos_err|``
is smaller than ``deadband_epsilon``. Only applicable to PD-position controllers that pass
``pos_err`` into :meth:`modify_ctrl_torque` — velocity-only controllers do
n"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_ctrl_torque(self, ctrl_torque, dofs_vel, pos_err)
class GearBacklash(ActionModifier)
    """Adds direction-dependent gear slop to position targets before PD control.

This models lost motion in the drivetrain, where the load settles on the
side of the gear gap selected by the latest commanded motion. After a
positive target move the effective motor-side target becomes
``target + backlash``"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_processed_action(self, processed_action)
class EnvelopeClip(ActionModifier)
    """Clips target positions so PD torques stay within the motor torque-speed envelope.

Back-solves the motor torque-speed curve to find the range of target positions
that yield feasible torques, then clips targets into that range. This ensures
the PD controller never commands torques outside the motor's"""
    def build(self, num_envs, device, entity, dofs_idx_local)
    def reset(self, envs_idx)
    def modify_processed_action(self, processed_action)
```

### Eden/eden/managers/modifiers/observations/__init__.py

```
"""Observation-term modifiers."""
```

### Eden/eden/managers/modifiers/observations/noise.py

```
"""Observation noise modifiers (constant, uniform, Gaussian)."""
def ensure_tensor_on_device(value, device)
class ConstantNoise(NoiseModel)
    def __init__(self, env, options)
    def compute(self, data)
class UniformNoise(NoiseModel)
    def __init__(self, env, options)
    def compute(self, data)
class GaussianNoise(NoiseModel)
    def __init__(self, env, options)
    def compute(self, data)
```

### Eden/eden/managers/observation_manager.py

```
"""Observation manager for computing observations."""
def _init_obs_term_shared(term, env)
class ObservationTerm(ManagerTermBase, ?)
    """Base class for observation terms.

The post-compute modifiers (noise/clip/scale/history) are options-only fields (see
``ObservationTermOptions.POST_COMPUTE_FIELDS``): ``configure()`` accepts them and stores them on the
options, but they are NOT mirrored as term attributes — the manager reads them fr"""
    def __init__(self, env, options)
class ObservationTermFuncWrapper(ManagerTermFuncWrapperBase, ?)
    """Base class for observation terms defined as function. See :class:`ObservationTerm` for the modifier
fields (options-only, not mirrored as attributes)."""
    def __init__(self, func, env, options)
class ObservationManager(?)
    def __init__(self, env, options)
    def _assign_concat_caches(self)
    def _freeze(value)
    def _raw_term_signature(term)
    def _build_dup_signatures(self)
    def _term_raw(self, term)
    def summary(self)
    def active_terms(self)
    def get_term(self, name)
    def group_obs_dim(self)
    def group_obs_term_dim(self)
    def reset(self, envs_idx)
    def compute(self, update_history)
    def compute_group(self, group_name, update_history)
    def _cat_into(self, key, tensors, dim)
    def _prepare_terms(self)
```

### Eden/eden/managers/reward_manager.py

```
"""Reward manager for computing reward signals."""
class RewardTerm(ManagerTermBase, ?)
    """Base class for reward terms."""
    def __init__(self, env, options)
    def reset(self, envs_idx)
class RewardTermFuncWrapper(ManagerTermFuncWrapperBase, ?)
    """Base class for reward terms defined as a function."""
    def __init__(self, func, env, options)
class RewardManager(?)
    def __init__(self, env, options)
    def summary(self)
    def iter_terms(self)
    def get_episode_sum(self, name, raw)
    def is_timestep_in_range(timestep, range_s)
    def reset(self, envs_idx)
    def compute(self, dt)
    def _prepare_terms(self)
```

### Eden/eden/managers/terms/actions/__init__.py

```
"""Built-in action terms."""
```

### Eden/eden/managers/terms/actions/binary_actions.py

```
"""Binary (open/close) gripper action term."""
class BinaryJointController(ActionTerm)
    """A binary joint controller for a parallel-jaw gripper.

When the action is applied, the joints are opened or closed.

Parameters
----------
entity_name: str
    The name of the entity to control.
dofs_name: list[str]
    The names of the DOFs to control.
open_action: float | dict[str, float]
    The """
    def __init__(self, env, options)
    def build(self)
    def action_dim(self)
    def compute(self, actions)
    def reset(self, envs_idx)
    def apply_actions(self)
```

### Eden/eden/managers/terms/actions/joint_actions.py

```
"""Joint-space PD and velocity action terms (implicit/explicit controllers)."""
class _JointPDControllerBase(ActionTerm)
    """Base class for joint PD controllers.

The processed target is built additively as::

    target = raw_action * scale + offset + reference_offset

where ``reference_offset`` is selected by ``reference_source`` (see
:class:`eden.constants.ReferenceSource`):

- ``ReferenceSource.ZERO``: no reference of"""
    def __init__(self, env, options)
    def build(self)
    def _has_nonzero_offset(self)
    def _build_scale_and_offset(self)
    def _compute_pos_target(self, raw_pos)
    def compute(self, actions)
    def reset(self, envs_idx)
class ImplicitPDController(_JointPDControllerBase)
    """Implicit joint PD controller using Genesis's built-in position control.

Uses ``control_dofs_pos`` which leverages Genesis's implicit integration scheme:
the PD target is recomputed at every physics substep and an implicit damping term
(kd * substep_dt) is added to the mass matrix for numerical stab"""
    def apply_actions(self)
class ExplicitPDController(_JointPDControllerBase)
    """Explicit joint PD controller using manual torque computation.

Computes PD torques explicitly and applies them via ``control_dofs_force``.
This is more physically accurate as it matches real-world motor control where
only torque commands are valid. Better suited for sim2real transfer and easier
to e"""
    def build(self)
    def reset(self, envs_idx)
    def apply_actions(self)
class VelocityFeedforwardPDController(_JointPDControllerBase)
    """Explicit joint PD controller with velocity feedforward.

Extends the explicit PD controller by accepting both target joint positions
and target joint velocities as actions. The torque is computed as:

.. math::
    \\tau = k_p (q_{target} + q_{offset} - q_{current} + q_{motor\\_offset})
          + """
    def action_dim(self)
    def build(self)
    def reset(self, envs_idx)
    def compute(self, actions)
    def apply_actions(self)
class ImplicitVelocityController(_JointPDControllerBase)
    """Implicit joint velocity controller using Genesis's built-in velocity control."""
    def build(self)
    def apply_actions(self)
class ExplicitVelocityController(_JointPDControllerBase)
    """Explicit joint velocity controller using manual torque computation.

The policy action is interpreted as a target joint velocity. Torque is computed
as a proportional law on the velocity error:

.. math::
    \\tau = k_p (\\dot{q}_{target} - \\dot{q})

This matches the behavior of MuJoCo's ``velocit"""
    def _compute_gain(self, envs_idx)
    def build(self)
    def reset(self, envs_idx)
    def apply_actions(self)
class NullJointAction(ActionTerm)
    """Virtually fix the DoFs to the default positions.

Parameters
----------
entity_name: str
    The name of the entity to control.
dofs_name: list[str]
    The names of the DOFs to control."""
    def __init__(self, env, options)
    def build(self)
    def compute(self, actions)
    def apply_actions(self)
```

### Eden/eden/managers/terms/actions/task_space_actions.py

```
"""Task-space action terms: differential IK and operational-space control."""
class DifferentialIKController(ActionTerm)
    """Action term that maps task-space commands to joint targets via differential IK.

Parameters
----------
entity_name: str
    The name of the entity to control.
dofs_name: list[str]
    The names of the DOFs to control.
ee_link_name: str
    The name of the end-effector link.
scale: float | list[float"""
    def __init__(self, env, options)
    def build(self)
    def action_dim(self)
    def diag(self)
    def compute(self, actions)
    def reset(self, envs_idx)
    def apply_actions(self)
class OperationalSpaceController(ActionTerm)
    """Operational Space Control (OSC) for either position only or position and orientation.

Reference:
----------
[1] http://khatib.stanford.edu/publications/pdfs/Khatib_1987_RA.pdf"""
    def __init__(self, env, options)
    def build(self)
    def action_dim(self)
    def compute(self, actions)
    def reset(self, envs_idx)
    def apply_actions(self)
    def compute_ops_kinetics_cholesky(mass_mat_U, mass_mat_D_inv_vec, J, is_U_unitriangular)
    def nullspace_torques(mass_matrix, nullspace_matrix, initial_joint, joint_pos, joint_vel, joint_kp)
```

### Eden/eden/managers/terms/actions/welding_actions.py

```
"""Welding action terms for suction-cup and parallel-jaw attach/detach."""
class _WeldingBase(ActionTerm)
    """A special ActionTerm that does not require any dofs for control."""
    def __init__(self, env, options)
    def build(self)
    def compute(self, actions)
    def reset(self, envs_idx)
class SuctionCupWelding(_WeldingBase)
    """Perform collision-aware welding between the end-effector link (suction cup) and an object link.

When the action is applied and the end-effector link is in contact with an object link,
the end-effector link and the object link are welded together.

Parameters
----------
entity_name: str
    The name"""
    def action_dim(self)
    def apply_actions(self)
class ParallelJawWelding(_WeldingBase)
    """Perform collision-aware welding between the end-effector link and an object link.

When the action is applied and the end-effector link is in contact with an object link,
the end-effector link and the object link are welded together.

Parameters
----------
entity_name: str
    The name of the entity"""
    def __init__(self, env, options)
    def build(self)
    def action_dim(self)
    def apply_actions(self)
```

### Eden/eden/managers/terms/curricula/rewards.py

```
"""Reward-weight curricula (staged ramp-up, penalty scheduling)."""
class StageRewardWeightCurriculum(CurriculumTerm)
    """Curriculum that modifies a reward weight a given number of training steps.

Parameters
----------
reward_term_name: str
    The name of the reward term.
weight_stages: list[tuple[int, float]]
    The list of stages with the training step and weight."""
    def __init__(self, env, options)
    def compute(self)
class PenaltyCurriculum(CurriculumTerm)
    """Curriculum that gradually scales reward weights for a set of reward terms.

Monitors average episode length and adjusts a scale factor applied to all
targeted reward terms. When episodes are short (agent struggling), the scale
decreases to ease penalties. When episodes are long (agent succeeding), t"""
    def __init__(self, env, options)
    def _resolve_terms(self)
    def reset(self, envs_idx)
    def _read_tracker_state(self)
    def compute(self)
    def _apply_scale(self)
```

### Eden/eden/managers/terms/observations/__init__.py

```
"""Built-in observation terms."""
```

### Eden/eden/managers/terms/observations/camera.py

```
"""Camera observation terms (RGB, depth, segmentation, normals, point cloud)."""
def rgb_image(env)
def depth_image(env)
def segmentation_image(env)
def normal_image(env)
def pointcloud_image(env)
```

### Eden/eden/managers/terms/observations/common.py

```
"""Common observation terms (commands, last action, episode phase)."""
def generated_commands(env)
def last_action(env)
def episode_phase(env)
```

### Eden/eden/managers/terms/observations/contact.py

```
"""Per-link contact-force-norm observation.

Reads :meth:`RigidEntity.get_links_net_contact_force` (Genesis-aggregated
per-link net force; ``(num_envs, n_links, 3)`` in world frame), slices to
the configured link set, and returns the per-link force magnitude.

Trade-off vs. ``gs.sensors.ContactForce``: the Genesis sensor binds to
**one** link per ``SensorOptions`` declaration, so a 14-link hand needs
14 sensor entries plus 14 obs-term entries to do what
:class:`ContactForceNorm` does in a single declaration. The cost is no
``NoisySensorMixin`` noise / delay / decimation modeling; that path is
rea"""
class ContactForceNorm(ObservationTerm)
    """Per-link contact-force magnitude (Euclidean, world frame).

Returns ``(num_envs, K)`` where ``K = len(matched links)``, each
entry being ``‖f_link‖`` at the most recent ``scene.step()``.

Parameters
----------
entity_name:
    Entity to read forces from (must be a ``RigidEntity``).
links_name:
    :"""
    def build(self)
    def compute(self)
```

### Eden/eden/managers/terms/observations/manipulation.py

```
"""Manipulation observation terms (end-effector / object distances)."""
class EndEffectorToObjectDistance(ObservationTerm)
    """Observation term for the distance between the end effector and the object."""
    def __init__(self, env, options)
    def build(self)
    def compute(self)
class ObjectToOracleDistance(ObservationTerm)
    """Observation term for the distance between the object and the oracle."""
    def __init__(self, env, options)
    def build(self)
    def compute(self)
```

### Eden/eden/managers/terms/observations/proprio.py

```
"""Proprioceptive observation terms (base pose/velocity, joint pos/vel)."""
def base_pos(env)
def base_quat(env)
def base_rpy(env)
def base_lin_vel(env)
def base_ang_vel(env)
def dofs_pos(env)
def dofs_vel(env)
def dofs_force(env)
def dofs_control_force(env)
def links_pos(env)
def links_quat(env)
def links_vel(env)
def links_ang(env)
```

### Eden/eden/managers/terms/observations/sensors.py

```
"""Observation term that concatenates configured sensor readings."""
class SensorRead(ObservationTerm)
    """Concatenate selected sensor readings into a single observation tensor.

Sensors return a tensor or NamedTuple of tensors. The tensors are concatenated if needed.

Parameters
----------
sensor_names : list[str], optional
    A list of sensor names to include in the observation. If None, all sensors a"""
    def build(self)
    def compute(self)
```

### Eden/eden/managers/terms/recorders/actions.py

```
"""Recorder term capturing per-step actions."""
class ActionRecorder(RecorderTerm)
    def record_pre_step(self)
```

### Eden/eden/managers/terms/rewards/__init__.py

```
"""Built-in reward terms."""
```

### Eden/eden/managers/terms/rewards/common.py

```
"""Common reward/penalty terms (action rate/magnitude, joint-limit penalties)."""
def _compute_action_rate_l2(action, prev_action)
def action_rate_l2(env)
def _compute_action_l2(action)
def action_l2(env)
def _compute_dofs_pos_limits(dofs_pos, soft_limits)
def dofs_pos_limits(env)
def _compute_dofs_vel_limits(dofs_vel, max_vel)
def dofs_vel_limits(env)
def self_collision_cost(env)
class UndesiredContacts(RewardTerm)
    """Penalty count of links whose net contact-force magnitude exceeds ``threshold``.

``links_name`` accepts the same regex / glob patterns as
:func:`eden.utils.string.resolve_matching_names`. Use a negative reward
weight to penalise (e.g. -0.1 per offending link)."""
    def build(self)
    def compute(self, envs_idx)
def _compute_action_rate_l2_smooth(action, prev_action, prev_prev_action)
def action_rate_l2_smooth(env)
def _compute_dofs_torques(torques)
def dofs_torques(env)
def _compute_dofs_acc_l2(dvel)
def dofs_acc_l2(env)
def similar_to_default(env, entity_name)
```

### Eden/eden/options/envs.py

```
"""Top-level environment configuration options (sim, solvers, batching)."""
class EnvOptions(ConfigurableOptions)
    """Top-level environment configuration (sim, solvers, batching).

Parameters
----------
num_envs: int
    Number of environments to run in parallel.
num_eval_envs: int
    Number of environments to run in evaluation mode.
sim_dt: float
    Simulation time step.
sim_substeps: int
    Number of simulatio"""
    def model_post_init(self, context)
```

### Eden/eden/options/file_handler.py

```
"""Configuration options for dataset file handlers."""
class FileHandlerOptions(ConfigurableOptions)
```

### Eden/eden/options/managers/actions.py

```
"""Action manager and action-term configuration options."""
class ActionTermOptions(ConfigurableOptions)
    """Action term specification.

Parameters
----------
entity_name: str
    The name of the entity to control.
dofs_name: str | list[str]
    The names of the DOFs to control."""
class ActionManagerOptions(?)
    """Action manager options.

Parameters
----------
<action_term_name>: ActionTermOptions
    The action terms configuration to be used."""
```

### Eden/eden/options/managers/observations.py

```
"""Observation manager, group, and term configuration options."""
class ObservationTermOptions(ConfigurableOptions)
    """Observation term specification.

Parameters
----------
noise: float, optional
    Standard deviation of Gaussian noise added to the observation (default=0.0).
clip: array-like[float, float] or None, optional
    Range to clip the observation values (default=None, no clipping).
scale: float, optional"""
class ObservationGroupOptions(ConfigurableOptions)
    """Observation group options.

Parameters
----------
concatenate_terms: bool, optional
    Whether to concatenate the terms (default=True).
concatenate_dim: int, optional
    The dimension to concatenate the terms (default=-1).
terms_order: list[str] | None, optional
    The order of the terms in the g"""
    def model_post_init(self, context)
    def disable_term(self, name)
class ObservationManagerOptions(?)
    """Observation manager options.

Parameters
----------
<group_name>: ObservationGroupOptions
    The observation terms configuration to be used for the given group."""
```

### Eden/eden/options/managers/rewards.py

```
"""Reward manager and reward-term configuration options."""
class RewardTermOptions(ConfigurableOptions)
    """Reward term specification.

Parameters
----------
range_s: tuple[float, float] | None
    The temporal range in seconds where the reward is active given as (start_s, end_s) or a list of such tuples.
    The both ends are inclusive. If None, the reward is active for the entire episode. Default is Non"""
    def _wrap_single_range(cls, v)
class RewardManagerOptions(?)
    """Reward manager options.

Parameters
----------
<reward_term_name>: RewardTermOptions
    The reward terms configuration to be used."""
```

### Eden/eden/options/robots/franka_hand.py

```
"""Franka Hand parallel-jaw gripper configuration."""
class FrankaHand(RobotOptions)
```

### Eden/eden/options/robots/leap_hand.py

```
"""LEAP hand configurations (left/right)."""
class _LeapHand(RobotOptions)
class LeapHand_R(_LeapHand)
class LeapHand_L(_LeapHand)
```

### Eden/eden/options/robots/mano_hand.py

```
"""MANO hand model configurations (left/right)."""
class _ManoHand(RobotOptions)
    """Base class for MANO Hand model from https://mano.is.tue.mpg.de/."""
class ManoHand_R(_ManoHand)
class ManoHand_L(_ManoHand)
```

### Eden/eden/options/robots/robotera_xhand.py

```
"""RobotEra XHand1 dexterous hand configurations (left/right)."""
class _XHand1(RobotOptions)
class XHand1_R(_XHand1)
class XHand1_L(_XHand1)
```

### Eden/eden/tasks/__init__.py

```
"""Eden task configurations.

Tasks self-register via ``@TASK_REGISTRY.register()`` on the config class.
The registry AST-scans ``eden/tasks/**/*.py`` on first lookup and finds the
decorator without importing the module — so writing a new task is a single
file change with no central index to update. See
``eden/tasks/benchmark/reacher/config.py`` for the canonical example.

Use ``TASK_REGISTRY.get("task_name")`` to load a config class on demand,
or ``TASK_REGISTRY.build("task_name", **modifier_kwargs)`` to construct an
instance with applied modifiers."""
```

### Eden/eden/tasks/parser.py

```
"""CLI helpers for building task configs from argparse.

This module wires :class:`~eden.tasks.registry.TaskMod` parameters into a
standard ``argparse.ArgumentParser`` so that user-facing scripts can accept
flat flags (``--difficulty hard``, ``--robot g1``) that are translated into
typed mod kwargs and applied via :meth:`TaskRegistry.build`."""
def _peek_task_name(argv, default)
def _add_mod_field_to_parser(parser, mod, field_name, annotation, help_text)
def get_task_argparser(description, default_task_name, argv)
def _collect_modifier_kwargs(args, task_name)
def _apply_run_name(config, run_name)
def get_task_config(task_name)
def get_task_config_from_args(args, run_name)
```

### Eden/eden/tasks/registry.py

```
"""Task registry: lazy task lookup and CLI field derivation.

:data:`TASK_REGISTRY` resolves task config classes by name, importing the owning module
lazily on first access. Built-in tasks are registered in :mod:`eden.tasks`
(``eden/tasks/__init__.py``); register your own with ``@TASK_REGISTRY.register()`` (or
``register(name=..., override=True)`` to shadow a built-in). This module also derives
argparse CLI fields from a task config's keyword-only fields."""
def _default_task_name(class_name)
class TaskMod()
    """Tool that modifies an EdenConfig instance.

TaskMod is a plain Python class (not a Pydantic model) because it is
*logic* with a few parameters, not user-facing data. ``EdenConfig`` is the
Pydantic data model; ``TaskMod`` operates on it.

To define one: subclass, declare CLI-tunable parameters as
**p"""
    def prefix(self)
    def with_prefix(self, prefix)
    def flag_for(self, field_name)
    def apply(self, config)
def _unwrap_annotated(annotation)
def cli_fields(mod_cls)
def _keyword_only_fields(mod_cls)
def _check_cli_value(field_name, annotation, value)
class TaskRegistry()
    """Task registry with two lookup paths, tried in order.

1. Eager registry — populated by ``@TASK_REGISTRY.register()`` decorators
   or explicit ``register(cls, ...)`` calls.
2. Auto-discovery — an AST scan of the configured search packages (default
   ``["eden.tasks"]``) finds ``@TASK_REGISTRY.regist"""
    def __init__(self)
    def register(self, obj)
    def add_search_path(self, package)
    def get(self, name)
    def get_modifiers(self, name)
    def build(self, name)
    def list_tasks(self)
    def __contains__(self, name)
    def __repr__(self)
    def _do_register(self, name, obj)
    def _ensure_discovered(self)
    def _invalidate_discovery_cache(self)
def _task_registry_aliases(tree)
def _scan_packages_for_tasks(packages)
def _iter_package_py_files(package)
def _task_name_from_decorators(cls_def)
def _normalize_modifier_entries(entries)
def literal_choices(annotation)
```

### Eden/eden/utils/configs.py

```
"""Eden config hierarchy (EdenConfig/EdenRLConfig) and serialization.

- :class:`EdenConfig` — base config for all environments (``EnvBase``).
- :class:`EdenRLConfig` — adds reward, termination, command, curriculum, and runner options.

Root config classes use Pydantic ``extra="forbid"`` (so misspelled fields raise), while
inner ``ManagerOptions`` / ``SceneOptions`` keep ``extra="allow"`` to hold dynamic
term/entity children. Saved configs use a ``_meta``/``config`` envelope; nested Options
recover their type from ``_option_module_`` / ``_option_class_`` keys."""
def _is_namedtuple_class(cls)
class EdenConfig(ConfigurableOptions)
    """Base configuration for all Eden environments (EnvBase).

Parameters
----------
env_options: EnvOptions
    Environment options (sim dt, num_envs, etc.).
scene_options: SceneOptions
    Scene options (entities, attachments).
observation_options: ObservationManagerOptions
    Observation manager optio"""
    def _serialize(self)
    def save_as_file(self, path, lock_config)
    def save_as_json(self, path, lock_config)
    def save_as_yaml(self, path, lock_config)
    def load_from_file(cls, path)
    def with_overrides_from_file(self, path)
    def with_overrides_from_dict(self, data_dict)
    def _to_dict(self)
class EdenRLConfig(EdenConfig)
    """Configuration for RL environments (RLEnvBase).

Extends EdenConfig with reward, termination, command, curriculum,
and runner options needed for reinforcement learning.

Parameters
----------
reward_options: RewardManagerOptions
    Reward manager options.
termination_options: TerminationManagerOptio"""
def _deep_merge(base, override)
def serialize_obj_with_metadata(obj)
def get_options_class_from_qualname(qualname)
def to_options(config, base_options)
def _safe_model_construct(cls, data)
def load_json(path)
```

### Eden/eden/utils/file_handler/__init__.py

```
"""Dataset file handlers (HDF5, NPZ) and registry."""
```

### Eden/eden/utils/file_handler/base.py

```
"""Base class and registry for dataset file handlers."""
class FileHandlerBase(?)
    """Abstract class for handling dataset files."""
    def resolve_path(self, file_path)
    def open(self, file_path, mode, env_cfg)
    def create(self, file_path, env_cfg)
    def write_episode(self, episode)
    def flush(self)
    def close(self)
    def load_episode(self, episode_name, device)
    def get_num_episodes(self)
```

### Eden/eden/utils/file_handler/episode_data.py

```
"""EpisodeData container for recorded trajectories."""
def _stack_recursive(data, in_place)
class EpisodeData()
    """Class to store episode data."""
    def __init__(self)
    def is_empty(self)
    def _resolve_key(self, key)
    def add(self, key, value)
    def _append_owned(self, key, value)
    def get(self, key, index, sequential)
    def size(self, key)
    def reset(self, clear_data)
    def pre_export(self)
    def pre_export_copy(self)
```

### Eden/eden/utils/file_handler/hdf5_file_handler.py

```
"""HDF5 dataset file handler."""
class HDF5FileHandler(FileHandlerBase)
    """HDF5 dataset file handler for storing and loading episode data.

The format of the stored structure
dataset_file.hdf5
└── data/                     # _hdf5_data_group
    ├── demo_0/               # Episode group
    │   ├── actions           # Dataset (Tensor saved as NumPy array)
    │   ├── state"""
    def __init__(self)
    def resolve_path(self, file_path)
    def open(self, file_path, mode, env_cfg)
    def create(self, file_path, env_cfg)
    def __del__(self)
    def get_episode_names(self)
    def get_num_episodes(self)
    def demo_count(self)
    def load_episode(self, episode_name, device)
    def write_episode(self, episode)
    def flush(self)
    def close(self)
    def _raise_if_not_initialized(self)
```

### Eden/eden/utils/file_handler/npz_file_handler.py

```
"""NPZ dataset file handler."""
def _encode_json_to_bytes(obj)
def _decode_bytes_to_json(arr)
def _flatten_dict(d, parent_key)
def _unflatten_dict(flat, device)
class NPZFileHandler(FileHandlerBase)
    """NPZ dataset file handler for storing and loading episode data.

Since NPZ files are flat key-value stores of numpy arrays, we use a
naming convention to represent the hierarchical episode structure:

    dataset_file.npz
    ├── __meta__env_cfg              # JSON string stored as bytes array
    ├─"""
    def __init__(self)
    def resolve_path(self, file_path)
    def open(self, file_path, mode, env_cfg)
    def create(self, file_path, env_cfg)
    def _collect_episode_names(self)
    def __del__(self)
    def get_episode_names(self)
    def get_num_episodes(self)
    def demo_count(self)
    def load_episode(self, episode_name, device)
    def write_episode(self, episode)
    def flush(self)
    def close(self)
    def _raise_if_not_initialized(self)
```

### Genesis/examples/sensors/surface_distance_shadowhand.py

```
"""Interactive SurfaceDistanceProbe demo with Shadow Hand and keyboard teleop.

Surface distance probes on the hand measure distance to a rubber duck (mesh) and a box.
Use keyboard controls to move the hand via IK; the hand tracks target positions
for the wrist and fingertips."""
def main()
```

### Genesis/genesis/engine/simulator.py

```
class Simulator(RBC)
    """A simulator is a scene-level simulation manager, which manages all simulation-related operations in the scene, including multiple solvers and the inter-solver coupler.

Parameters
----------
scene : gs.Scene
    The scene object that the simulator is associated with.
options : gs.SimOptions
    A Si"""
    def __init__(self, scene, options, coupler_options, tool_options, rigid_options, kinematic_options, mpm_options, sph_options, fem_options, sf_options, pbd_options)
    def _add_entity(self, morph, material, surface, visualize_contact, name)
    def _add_force_field(self, force_field)
    def build(self)
    def destroy(self)
    def reset(self, state, envs_idx)
    def reset_grad(self)
    def f_global_to_f_local(self, f_global)
    def f_local_to_s_local(self, f_local)
    def f_global_to_s_local(self, f_global)
    def f_global_to_s_global(self, f_global)
    def step(self, in_backward)
    def _step_grad(self)
    def process_input(self, in_backward)
    def process_input_grad(self)
    def substep(self, f)
    def sub_step_grad(self, f)
    def substep_pre_coupling(self, f)
    def substep_pre_coupling_grad(self, f)
    def substep_post_coupling(self, f)
    def substep_post_coupling_grad(self, f)
    def add_grad_from_state(self, state)
    def collect_output_grads(self)
    def save_ckpt(self)
    def load_ckpt(self)
    def get_state(self)
    def set_gravity(self, gravity, envs_idx)
    def dt(self)
    def substeps(self)
    def scene(self)
    def gravity(self)
    def requires_grad(self)
    def n_entities(self)
    def entities(self)
    def substeps_local(self)
    def cur_substep_global(self)
    def cur_substep_local(self)
    def cur_step_local(self)
    def cur_step_global(self)
    def cur_t(self)
    def coupler(self)
    def solvers(self)
    def active_solvers(self)
```

### Genesis/genesis/engine/solvers/rigid/constraint/__init__.py

```
"""Constraint solver submodule for rigid body simulation.

Contains constraint solving, island detection, and backward pass."""
```

### Genesis/genesis/engine/solvers/rigid/constraint/backward.py

```
def func_matvec_Ap(entities_info, constraint_state, rigid_global_info, static_rigid_sim_config, i_b)
def kernel_solve_adjoint_u(entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
def kernel_compute_gradients(entities_info, constraint_state, static_rigid_sim_config)
```

### Genesis/genesis/engine/solvers/rigid/constraint/noslip.py

```
def func_build_efc_AR_b_batch(i_b, dofs_state, entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
def func_solve_mass_entity_row(i_row, i_e, i_b, buf, entities_info, rigid_global_info)
def func_noslip_batch(i_b, collider_state, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_dual_finish_batch(i_b, dofs_state, entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
def kernel_noslip_fused(collider_state, dofs_state, entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
def kernel_noslip_decomposed(collider_state, dofs_state, entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
def func_extract_block_matrix_from_AR(Ac, i_b, start, n, constraint_state, static_rigid_sim_config)
def func_residual_constraint_force(res, i_b, i_efc, dim, constraint_state, static_rigid_sim_config)
def func_cost_change(i_b, Ac, force, force_start, old_force, res, dim, eps)
def compute_A_diag(entities_info, rigid_global_info, constraint_state, static_rigid_sim_config)
```

### Genesis/genesis/engine/solvers/rigid/constraint/solver.py

```
def _sort_relevant_dofs_descending(constraint_state, i_con, n, i_b)
class ConstraintSolver()
    def __init__(self, rigid_solver)
    def reset(self, envs_idx)
    def clear(self, envs_idx)
    def add_equality_constraints(self)
    def add_inequality_constraints(self)
    def resolve(self, entities_info, rigid_global_info)
    def noslip(self)
    def get_equality_constraints(self, as_tensor, to_torch)
    def get_weld_constraints(self, as_tensor, to_torch)
    def add_weld_constraint(self, link1_idx, link2_idx, envs_idx)
    def delete_weld_constraint(self, link1_idx, link2_idx, envs_idx)
    def backward(self, dL_dqacc)
def kernel_get_equality_constraints(is_padded, iout, fout, constraint_state, equalities_info, static_rigid_sim_config)
def constraint_solver_kernel_reset(envs_idx, constraint_state, static_rigid_sim_config)
def func_clear_constraint_at_env(i_b, n_dofs, len_constraints, constraint_state, rigid_global_info, static_rigid_sim_config)
def constraint_solver_kernel_clear(envs_idx, constraint_state, rigid_global_info, static_rigid_sim_config)
def constraint_solver_kernel_masked_clear(envs_mask, constraint_state, rigid_global_info, static_rigid_sim_config)
def _add_friction_constraint(i_b, i_col_, i_friction, links_info, links_state, dofs_state, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def _add_collision_constraints_per_friction(links_info, links_state, dofs_state, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def _add_collision_constraints_per_contact(links_info, links_state, dofs_state, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def add_collision_constraints(links_info, links_state, dofs_state, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def func_equality_connect(i_b, i_e, links_info, links_state, dofs_state, equalities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_equality_joint(i_b, i_e, joints_info, dofs_state, dofs_info, equalities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def add_equality_constraints(links_info, links_state, dofs_state, dofs_info, joints_info, equalities_info, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def add_inequality_constraints(links_info, links_state, dofs_state, dofs_info, joints_info, constraint_state, collider_state, rigid_global_info, static_rigid_sim_config)
def func_equality_weld(i_b, i_e, links_info, links_state, dofs_state, equalities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def add_joint_limit_constraints(links_info, joints_info, dofs_info, dofs_state, rigid_global_info, constraint_state, static_rigid_sim_config)
def add_frictionloss_constraints(links_info, joints_info, dofs_info, dofs_state, rigid_global_info, constraint_state, static_rigid_sim_config)
def kernel_add_weld_constraint(link1_idx, link2_idx, envs_idx, equalities_info, constraint_state, links_state, rigid_global_info, static_rigid_sim_config)
def kernel_delete_weld_constraint(link1_idx, link2_idx, envs_idx, equalities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def linear_to_lower_tri(i_pair)
def func_compute_dof_perm(dofs_info, entities_info, links_state, constraint_state, static_rigid_sim_config)
def func_compute_sparsity_pattern(i_b, constraint_state, rigid_global_info)
def func_hessian_direct_batch(i_b, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_hessian_direct_tiled(constraint_state, rigid_global_info, check_full_hessian)
def func_cholesky_factor_direct_batch(i_b, constraint_state, rigid_global_info, static_rigid_sim_config)
def _cholesky_factor_direct_tiled_impl(constraint_state, rigid_global_info, static_rigid_sim_config, TileCls)
def _cholesky_and_solve_fused_tiled_impl(constraint_state, rigid_global_info, static_rigid_sim_config, TileCls, write_L_to_nt_H)
def func_cholesky_factor_direct_tiled(constraint_state, rigid_global_info, static_rigid_sim_config)
def func_cholesky_and_solve_fused_tiled(constraint_state, rigid_global_info, static_rigid_sim_config, write_L_to_nt_H)
def func_hessian_and_cholesky_factor_direct_batch(i_b, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_hessian_and_cholesky_factor_direct(entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_build_changed_constraint_list(i_b, constraint_state)
def func_hessian_and_cholesky_factor_incremental_dense_batch(i_b, constraint_state, rigid_global_info)
def func_hessian_and_cholesky_factor_incremental_sparse_batch(i_b, constraint_state, rigid_global_info)
def func_hessian_and_cholesky_factor_incremental_batch(i_b, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_cholesky_solve_batch(i_b, constraint_state, static_rigid_sim_config)
def func_cholesky_solve_tiled(constraint_state, static_rigid_sim_config)
def func_ls_init_and_eval_p0(i_b, entities_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_linesearch_eval_constraints_at_n_alphas_serial(i_b, alphas, constraint_state, n_alphas)
def _func_linesearch_eval_quadratic_at_alpha(i_b, tid, alpha, t, constraint_state, rigid_global_info, coop)
def _func_linesearch_eval_at_alpha(i_b, tid, alpha, constraint_state, rigid_global_info, coop)
def _func_linesearch_eval_constraints_at_n_alphas_coop(i_b, tid, alphas, constraint_state, n_alphas)
def _func_linesearch_eval_quadratic_at_3_alphas(i_b, tid, alphas, t0, t1, t2, constraint_state, rigid_global_info, coop)
def _func_linesearch_eval_at_3_alphas(i_b, tid, alphas, constraint_state, rigid_global_info, coop)
def update_bracket_no_eval_local(p_alpha, p_cost, p_grad, p_hess, alphas, costs, grads, hess)
def func_linesearch_and_apply_alpha(i_b, entities_info, dofs_state, rigid_global_info, constraint_state, static_rigid_sim_config)
def func_linesearch_refine(i_b, tid, p1_alpha, p1_cost, p1_deriv_0, p1_deriv_1, p0_cost, gtol, constraint_state, rigid_global_info, coop)
def func_linesearch_batch(i_b, entities_info, dofs_state, rigid_global_info, constraint_state, static_rigid_sim_config)
def func_save_prev_grad(i_b, constraint_state)
def func_update_constraint_batch(i_b, qacc, Ma, cost, dofs_state, constraint_state, static_rigid_sim_config)
def _func_update_efc_force_body(i_c, i_b, constraint_state, static_rigid_sim_config)
def _func_update_efc_force(constraint_state, static_rigid_sim_config)
def _func_update_qfrc_constraint_coop(constraint_state, static_rigid_sim_config)
def _func_update_cost_coop(qacc, Ma, cost, dofs_state, constraint_state, static_rigid_sim_config)
def func_update_constraint(qacc, Ma, cost, dofs_state, constraint_state, static_rigid_sim_config)
def func_update_gradient_batch(i_b, dofs_state, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_update_gradient_tiled(dofs_state, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_update_gradient(dofs_state, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_terminate_or_update_descent_batch(i_b, constraint_state, rigid_global_info, static_rigid_sim_config)
def initialize_Jaref(qacc, constraint_state, static_rigid_sim_config)
def _initialize_Jaref_body(i_c, i_b, n_dofs, qacc, constraint_state, static_rigid_sim_config)
def _initialize_Jaref_per_env(qacc, constraint_state, static_rigid_sim_config)
def _initialize_Jaref_parallel(qacc, constraint_state, static_rigid_sim_config)
def initialize_Ma(Ma, qacc, dofs_info, entities_info, rigid_global_info, static_rigid_sim_config)
def func_solve_init(dofs_info, dofs_state, entities_info, constraint_state, rigid_global_info, static_rigid_sim_config)
def func_solve_iter(i_b, entities_info, dofs_state, rigid_global_info, constraint_state, static_rigid_sim_config)
def _get_static_config()
def func_solve_body(entities_info, dofs_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config, _n_iterations)
def func_solve_body_monolith(entities_info, dofs_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config, _n_iterations)
def func_update_contact_force(links_state, collider_state, constraint_state, static_rigid_sim_config)
def func_update_qacc(dofs_state, constraint_state, static_rigid_sim_config, errno)
```

### Genesis/genesis/engine/solvers/rigid/constraint/solver_breakdown.py

```
def _ls_eval_cost_grad(alpha, i_b, constraint_state)
def _func_decomp_linesearch_p0(dofs_info, entities_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_decomp_linesearch_refine_coop(i_b, tid, alpha_newton, p0_cost, gtol, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_decomp_linesearch_refine_serial(i_b, tid, alpha_newton, p0_cost, gtol, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_decomp_linesearch_refine(i_b, tid, alpha_newton, p0_cost, gtol, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_decomp_linesearch_refine_and_apply(constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_cg_only_save_prev_grad(constraint_state, static_rigid_sim_config)
def _func_update_constraint_forces_body(i_c, i_b, constraint_state, static_rigid_sim_config)
def _func_update_constraint_forces(constraint_state, static_rigid_sim_config)
def _func_update_qfrc_constraint_per_dof(constraint_state, static_rigid_sim_config)
def _func_update_constraint_cost_coop(dofs_state, constraint_state, static_rigid_sim_config)
def _func_update_constraint_cost_serial(dofs_state, constraint_state, static_rigid_sim_config)
def _func_update_constraint_cost(dofs_state, constraint_state, static_rigid_sim_config)
def _func_build_changed_and_decide_hessian_mode(constraint_state, static_rigid_sim_config)
def _func_patch_hessian_delta(constraint_state, rigid_global_info)
def _func_newton_only_nt_hessian(constraint_state, rigid_global_info)
def _func_newton_only_nt_hessian_and_cholesky(constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_update_gradient(entities_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_update_gradient_no_solve(entities_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_cholesky_and_solve_fused(constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_update_search_direction(constraint_state, rigid_global_info, static_rigid_sim_config)
def _func_check_early_exit(constraint_state, graph_counter)
def _kernel_solve_graph(dofs_info, entities_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config, graph_counter)
def func_solve_decomposed(entities_info, dofs_info, dofs_state, constraint_state, rigid_global_info, static_rigid_sim_config, _n_iterations)
```

### Genesis/genesis/engine/solvers/rigid/constraint/solver_island.py

```
class ConstraintSolverIsland()
    def __init__(self, rigid_solver)
    def clear(self, envs_idx)
    def _kernel_clear(self, envs_idx)
    def resolve(self, entities_state, entities_info, dofs_state, links_state, geoms_state, rigid_global_info, contact_island_state)
    def add_constraints(self)
    def add_collision_constraints_and_wakeup_entities(self, i_island, i_b, entities_state, entities_info, dofs_state, links_state, geoms_state, rigid_global_info, contact_island_state)
    def add_joint_limit_constraints(self, i_island, i_b)
    def _func_nt_hessian_incremental(self, island, i_b)
    def _func_nt_hessian_direct(self, island, i_b)
    def _func_nt_chol_factor(self, island, i_b)
    def _func_nt_chol_solve(self, island, i_b)
    def reset(self, envs_idx)
    def _kernel_reset(self, envs_idx)
    def _func_update_contact_force(self, i_island, i_b)
    def _func_update_qacc(self, i_island, i_b)
    def _func_solve(self, i_island, i_b, entities_info, rigid_global_info)
    def _func_ls_init(self, island, i_b)
    def _func_ls_point_fn(self, i_b, alpha)
    def _func_linesearch(self, island, i_b)
    def update_bracket(self, p_alpha, p_cost, p_deriv_0, p_deriv_1, i_b)
    def _func_solve_body(self, island, i_b, entities_info, rigid_global_info)
    def _func_update_constraint(self, island, i_b, qacc, Ma, cost)
    def _func_update_gradient(self, island, i_b, entities_info, rigid_global_info)
    def initialize_Jaref(self, qacc, i_b)
    def initialize_Ma(self, Ma, qacc, island, i_b)
    def _func_init_solver(self, i_island, i_b, entities_info, rigid_global_info)
```

### Genesis/genesis/utils/generate_env_sphere.py

```
def compute_uv_from_vertex(vertex)
def main()
```

### Genesis/genesis/vis/viewer_plugins/plugins/mouse_interaction.py

```
class MouseInteractionPlugin(RaycasterViewerPlugin)
    """Basic interactive viewer plugin that enables using mouse to apply spring force on rigid entities."""
    def __init__(self, use_force, spring_const, color)
    def build(self, viewer, camera, scene)
    def on_mouse_motion(self, x, y, dx, dy)
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y)
    def on_mouse_press(self, x, y, button, modifiers)
    def on_mouse_release(self, x, y, button, modifiers)
    def update_on_sim_step(self)
    def on_draw(self)
    def on_close(self)
    def _compute_line_T(self, start, end)
    def _update_drag_plane(self)
    def _get_last_raycast_env_idx(self)
    def _apply_spring_force(self, control_point, dt)
```

### dexterous-hands/main.py

```
"""Main training script for dexterous manipulation tasks using Eden + RSL-RL."""
def _wipe_stale_log_dir(log_dir)
def train(config, args)
def play(config, args)
def rollout_benchmark(config, args)
def optimize(config, args)
def deploy(config, args)
def main()
```

### dexterous-hands/scripts/expand_distill_config.py

```
"""Expand one entry from conf/distill_configs.yaml into bash exports.

The YAML carries shared ``defaults`` (the menu of available
resolutions/types/noisy modes/tactile encoders, plus a pinned baseline) and a
``configs:`` map keyed by sweep name (e.g. ``screwdriver-xhand1``). This
script merges defaults with the selected entry, then picks a subset of the
menu based on ``<mode>``:

* ``mode == "types"``: every type at the pinned baseline (clean / pinned
  resolution), prefixed with ``none``. The tactile encoder is auto-picked
  per sensor (grid sensors -> ``tactile_convrnn``; gridless/``none`` ->
"""
def auto_tactile_encoder(sensor)
def expand_baseline_sensors(placements, sensor_types, pinned_resolution, pinned_noisy, include_none)
def expand_focused_sensors(placements, resolutions, noisy_modes, sensor_type)
def jobs_for_mode(cfg, mode)
def main(path, name, mode)
```

### dexterous-hands/scripts/grasps_generator.py

```
"""What this script does:
- Randomly perturbs robot DOFs (and object pose if not fixed-base), then keeps only grasps
  that pass 3 checks: surface distance, penetration, and stability checks.
- Runs in parallel over many envs until `num_grasps` valid samples are collected.

Fast start:
- `python scripts/grasps_generator.py --task=<task> --config=<yaml> --num_grasps=<N> [--num_envs=<M>]`
- Typical config path: `conf/sample_grasps/<task>_<robot>.yaml`

Config precedence (important):
- CLI args are parsed first.
- Then `grasp_generation` in YAML overrides matching CLI/default values.
- Keep grasp-ge"""
def parse_numeric_sequence(value, expected_len)
def expand_root_pose_override(value, expected_len, num_envs, device)
def resolve_surface_distance_sensors(env, pattern)
def _sensor_min_distance_per_env(sensor, num_envs)
def check_surface_distance(num_envs, surface_distance_sensors, surface_distance_threshold, required_num_surface_distance_fingers)
def build_link_index_tensor(link_names, hand, device)
def membership_mask(values, allowed_values)
def get_max_penetration_per_env(num_envs, contacts, device, extra_mask)
def check_object_stable(obj, initial_pos, max_displacement)
def check_penetration(num_envs, hand, obj, max_penetration, device)
def check_finger_self_penetration(num_envs, hand, finger_link_indices, max_penetration, device)
def main()
```

### dexterous-hands/scripts/imgui_panels.py

```
"""Shared ImGui sub-panels for the viewer scripts.

Reused by:
- ``scripts/sensor_probes_selector.py`` (``ProbeControlPanel`` embeds ``DofSliderPanel``)
- ``scripts/hand_tactile_sandbox.py`` (manual DOF sliders + YAML sequence pause / load)

Each helper is designed to be composed inside a larger ImGui panel: it renders into
the caller's ``imgui`` context and (where applicable) returns whether anything changed
so the host can react (e.g. apply targets to the entity)."""
def get_dof_info(entity)
def format_dofs_as_yaml_pose(names, targets)
def format_camera_pose(viewer)
def render_camera_pose_button(imgui, viewer)
class DofSliderPanel()
    """ImGui sub-panel: a per-DOF slider for every actuated joint of an articulated entity.

The panel mutates a caller-owned ``targets`` numpy array in place via ``render()``;
the host script reads that array and drives the entity. With ``readonly=True``
the sliders are replaced by static text so a differ"""
    def __init__(self, get_entity)
    def dof_names(self)
    def dof_lower(self)
    def dof_upper(self)
    def sync(self, entity)
    def current_targets(self)
    def render(self, imgui, targets)
class DofSequencePanel()
    """ImGui sub-panel: pause / play + YAML file loader for a cycling DOF target sequence.

Owns the full cycling state:

- ``paused`` (bool): toggled by a checkbox; the host script consults it to decide
  whether to follow the cycle or let the slider panel drive.
- ``sequence`` ((n_steps, n_dofs) ndarray """
    def __init__(self, load_callback)
    def _refresh_files(self)
    def set_sequence(self, path, seq)
    def advance(self, dt)
    def current_pose_index(self)
    def current_step_target(self)
    def render(self, imgui)
```

### dexterous-hands/scripts/manual_calibration_gui.py

```
"""Manual dexterous-hand calibration GUI.

Replay a recorded sysid trajectory while interactively tuning the sim
twin's per-joint gains and passive parameters. Works for any registered
hand via ``--robot``; ``--deploy`` (mirroring commands to the real hand)
is XHand1-only because that is the only hand with a deployment class so
far. Without ``--deploy`` the GUI runs the sim twin alone, for any hand.

Example
-------
python scripts/manual_calibration_gui.py --robot xhand1     --trajectory data/xhand_sysid/trajectories/prbs_range20.npz"""
def _to_1d_numpy(value)
class PendingCommand()
class CalibrationState()
    def __post_init__(self)
    def queue(self, name, payload)
    def pop_commands(self)
    def selected_dof_name(self)
    def replay_mode(self)
class NPZFileBrowser()
    def __init__(self, start_dir, extension)
    def request(self, target, start_path)
    def draw(self, imgui, state)
    def _accept(self, path, state)
class ManualCalibrationPanel()
    def __init__(self, state)
    def __call__(self, imgui)
def _load_trajectory(path, dof_names, sim_step_dt)
def _apply_property_values(env, state, names, selected_idx)
def _read_current_values(env, state, dof_indices)
def _deploy_send(deployer, dofs_pos)
def _reset_views(env, state, deployer)
def _reset_replay(env, state, deployer)
def _read_deploy_state(deployer)
def _update_plot_values(env, state, deploy_state)
def _plot_data_func(state)
def _set_plot_colors(plotter)
def _process_commands(env, state, sim_step_dt, deployer)
def _update_tactile(env, state, deploy_state)
def _first_env_flag(flag)
def _env_step_terminated(step_out)
def _step(env, action_np, state, deployer)
def _replay_step(env, state, deployer)
def _target_step(env, state, deployer)
def _resize_state_dofs(state, dof_names)
def _build_deployer(env, args)
def build_env(args)
def main()
```

### dexterous-hands/scripts/robot_dofs_viewer.py

```
"""Interactive visualizer for controlling robot joints, base pose, and (optionally) object pose.
Exports a YAML snippet suitable for use as a grasp-generator config override.

Usage:
    python scripts/robot_dofs_viewer.py --task screwdriver --robot xhand1 --cpu
    python scripts/robot_dofs_viewer.py --task in_hand_repose --cpu
    python scripts/robot_dofs_viewer.py --task="$TASK" --robot="$ROBOT" --grasp-path "$GRASPS_OUTPUT" --grasp-index 0 --cpu"""
def _format_vec(values)
def _to_dofs_idx_list(dofs_idx_local)
def _load_grasp_target_metadata_from_yaml(config_path)
def _apply_precomputed_grasp(robot, obj)
class RobotDofsViewer(ViserViewer)
    def __init__(self, env, robot, obj, grasp_target_metadata, host, port, enable_gui)
    def _add_grasp_target_controls(self)
    def _add_pose_controls(self, folder_name, init_pos, init_euler, current_pos, current_euler, pos_sliders, rot_sliders)
    def _setup_gui(self)
    def update_robot_state(self)
    def _update_grasp_target_markers(self)
    def get_yaml_snippet(self)
    def update(self)
def main()
```

### dexterous-hands/scripts/sensor_probes_selector.py

```
def _gl_camera_pose_from_eye_target(eye, target)
def _snap_viewer_camera_neg_world_axis(pyrender_viewer, axis)
def _make_axis_snap_callback(pyrender_viewer, axis)
def _axis_rotation_matrix(axis, angle)
def _rotate_viewer_camera_world_axis(pyrender_viewer, axis, angle)
def _make_axis_rotate_callback(pyrender_viewer, axis, angle)
class SingleProbeAction(NamedTuple)
class ProbeLayoutAction(NamedTuple)
class DebugPreview(NamedTuple)
class ProbePointsSelectorPlugin(RaycasterViewerPlugin)
    """Interactive viewer plugin: **left-click** adds a single probe on the mesh (no click-to-delete; use **U** undo).

Grid/line selection samples on the **plane through the anchor** whose normal is the **camera view direction**
at anchor time — parallel to the image plane:

- **L** toggles right-click pl"""
    def __init__(self, radius, color, grid_snap, output_file, default_grid_num_points, save_on_close)
    def _log(self, message)
    def _draw_probe_spheres(self, positions, color, radius)
    def _clear_probe_debug(self, debug_object)
    def _entry_flat_probes(entry)
    def _build_link_by_name(self)
    def _probes_world_by_radius(self, probes, link)
    def _draw_probes_for_link(self, probes, link, color)
    def _draw_entry_debug(self, entry, link_by_name, color)
    def set_probe_color(self, rgb)
    def _reset_probe_state(self)
    def build(self, viewer, camera, scene)
    def _probe_layout_message(self)
    def _toggle_probe_layout_mode(self)
    def _adjust_grid_resolution(self, axis, delta)
    def _keybind_undo(self)
    def _clear_all_probes(self)
    def _keybind_clear_all(self)
    def _undo_single_action(self, action)
    def _undo_probe_layout_action(self, action)
    def _next_layout_color(self)
    def _probe_dict_payload(self, local_pos, local_normal, radius)
    def _zero_probe()
    def _entry_for_output(self, entry)
    def _clear_grid_preview_debug(self)
    def _append_single_probe_session(self, link_name, payload, debug_object)
    def _raycast_from_camera_to_plane_target(self, cam_pos, target)
    def _grid_plane_hits_matrix(self, corner_b_world)
    def _line_plane_hits(self, end_world)
    def _layout_endpoint_at(self, x, y)
    def _commit_probe_layout_at(self, x, y)
    def _commit_grid_at(self, x, y)
    def _commit_line_at(self, x, y)
    def _snap_to_grid(self, point)
    def _clamp_grid_axis(self, n)
    def _project_point_on_grid_plane(self, p)
    def _hit_to_probe_data(self, ray_hit)
    def _exit_grid_mode(self)
    def on_mouse_motion(self, x, y, dx, dy)
    def on_mouse_press(self, x, y, button, modifiers)
    def on_mouse_scroll(self, x, y, dx, dy)
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)
    def on_draw(self)
    def load_probes_from_file(self, file_path)
    def load_probes_replace(self, file_path)
    def save_probes(self)
    def on_close(self)
class SelectorApp()
    """Shared control state between the ImGui panel (viewer thread) and the main loop (main thread)."""
    def __init__(self)
    def stop(self)
    def request_robot_switch(self, robot_name)
def make_robot_entity_kwargs(robot_name)
def save_viewer_screenshot(pyrender_viewer, out_dir)
def find_probe_files(robot_name)
class ProbeControlPanel()
    """ImGui side panel: switch the hand (in-place rebuild), load probe-layout files, recolor probes,
pose the hand's DOFs, and take screenshots.

The panel holds no scene-specific objects — it reads the live entity/viewer from the
``InteractiveScene`` each frame, so it transparently survives a robot-switc"""
    def __init__(self, selector, interactive, app, robot_names, current_robot)
    def _hand_entity(self)
    def _sync(self, entity)
    def __call__(self, imgui)
```

### dexterous-hands/scripts/sensors_viewer.py

```
"""Load task environment and visualize the sensor placements and sensor readings.

Usage:
    python sensor_viewer.py --task in_hand_repose"""
def _plot_rotation_quat(plot_normal)
def _align_normal_quat(from_vec, to_vec)
def _read_sensor_vectors(sensor_type, sensor)
def _plot_all_sensors(scene, sensor_type, sensors, plot_normal)
def _debug_print_tactile_sensor(sensor_type, sensor, t)
def _lookup_obs_value(obs, key)
def _to_printable_obs(obs)
def _debug_print_sensor_obs(obs, t)
def main()
```

### dexterous-hands/scripts/task_viewer.py

```
"""Task environment viewer and debugger.
Provides a GUI to manually control actions and step through the simulation.

Usage:
    python task_viewer.py --task in_hand_repose"""
class TaskViewerViser(ViserViewer)
    def __init__(self, env, num_actions, policy, control_env, sample_policy_actions, host, port, enable_gui)
    def _format_vec3(values)
    def _get_active_client_camera(self)
    def print_current_camera_yaml(self)
    def _reward_series_labels(self)
    def _setup_reward_plot(self)
    def _clear_reward_plot_history(self)
    def _append_reward_plot_sample(self, rewards)
    def _setup_gui(self)
    def _set_action_sliders_disabled(self, disabled)
    def update_action(self, idx, val)
    def zero_actions(self)
    def randomize_actions(self)
    def _compute_actions(self, obs)
    def step_env(self)
    def reset_env(self)
    def update_info_display(self)
    def update(self)
def main()

```python
def _reward_series_labels(self) -> list[str]:
        rm = getattr(self.env, "reward_manager", None)
        if rm is not None and rm.active_terms:
            return list(rm.active_terms)
        return ["total"]
```

```python
def _setup_reward_plot(self) -> None:
        data = (
            np.array([0.0]),
            *[np.array([0.0]) for _ in range(self._num_reward_series)],
        )
        colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow"]
        self._reward_plot_handle = self.server.gui.add_uplot(
            data=data,
            series=(
                uplot.Series(label="Time (s)"),
                *[
                    uplot.Series(
                        label=self._reward_plot_names[i],
                        stroke=colors[i % len(colors)],
                        width=2,
                    )
                    for i in range(self._num_reward_series)
                ],
            ),
            title="Rewards (env 0)",
            scales={
                "x": uplot.Scale(time=False, auto=True),
                "y": uplot.Scale(auto=True),
            },
            legend=uplot.Legend(show=True),
            aspect=2.5,
        )
```

```python
def _clear_reward_plot_history(self) -> None:
        self.time_history.clear()
        for dq in self.reward_history_per_series:
            dq.clear()
        self.start_time = time.time()
        if self._reward_plot_handle is not None:
            self._reward_plot_handle.data = (
                np.array([0.0]),
                *[np.array([0.0]) for _ in range(self._num_reward_series)],
            )
```

```python
def _append_reward_plot_sample(self, rewards: torch.Tensor) -> None:
        if self._reward_plot_handle is None:
            return
        dt = float(self.env.dt)
        current_time = time.time() - self.start_time
        self.time_history.append(current_time)

        rm = getattr(self.env, "reward_manager", None)
        if rm is not None and rm.active_terms:
            step_contrib = rm._step_reward[0] * dt
            for i in range(self._num_reward_series):
                self.reward_history_per_series[i].append(float(step_contrib[i].item()))
        else:
            self.reward_history_per_series[0].append(float(rewards[0].item()))

        self._reward_plot_handle.data = (
            np.array(list(self.time_history)),
            *[np.array(list(self.reward_history_per_series[i])) for i in range(self._num_reward_series)],
        )
```
```

### dexterous-hands/src/calibration/action_mod_sysid.py

```
"""Bridge PD ``Compose`` action modifiers to Eden sysid ``Parameter`` application.

``apply_parameters`` only writes entity solver fields. We monkeypatch
``eden.extensions.sysid.modifier._apply_one`` so synthetic ``property``
strings update tensors on ``Deadband``, ``GearBacklash``, ``ConstantTorqueKick``,
``MotorStrength``, ``EffortClip``, ``EnvelopeClip``, and ``FrictionModel`` (matching
``HAND_CONTROLLER`` in ``shared_terms.py``).

T-N curve scalars (``driving_torque_limit``, …) are written to both
``EffortClip`` and ``EnvelopeClip`` so they stay consistent."""
def get_dofs_pos_controller(env)
def resolve_compose(term)
def resolve_deadband(term)
def resolve_gear_backlash(term)
def resolve_constant_torque_kick(term)
def _local_indices_for_param(term, dof_names)
def _values_for_columns(env, param, local_idx, per_env_values)
def _assign_modifier_slice(modifier, attr, env, param, term, per_env_values, row_attr)
def write_deadband_epsilon(env, param)
def write_gear_backlash(env, param)
def write_gear_reversal_threshold(env, param)
def write_gear_takeup_rate(env, param)
def write_gear_initial_side(env, param)
def write_torque_kick(env, param)
def write_activation_epsilon(env, param)
def write_motor_strength(env, param)
def _write_tn_pair(env, param)
def write_driving_torque_limit(env, param)
def write_braking_torque_limit(env, param)
def write_full_torque_speed(env, param)
def write_no_load_speed(env, param)
def write_friction_static(env, param)
def write_friction_dynamic(env, param)
def write_friction_activation_vel(env, param)
def write_friction_offset(env, param)
def _read_slice_row(modifier, attr, term, dof_names, env_row)
def read_deadband_epsilon_row(env, dof_names, env_row)
def read_gear_backlash_row(env, dof_names, env_row)
def read_gear_reversal_threshold_row(env, dof_names, env_row)
def read_gear_takeup_rate_row(env, dof_names, env_row)
def read_gear_initial_side_row(env, dof_names, env_row)
def read_torque_kick_row(env, dof_names, env_row)
def read_activation_epsilon_row(env, dof_names, env_row)
def read_motor_strength_row(env, dof_names, env_row)
def read_driving_torque_limit_row(env, dof_names, env_row)
def read_braking_torque_limit_row(env, dof_names, env_row)
def read_full_torque_speed_row(env, dof_names, env_row)
def read_no_load_speed_row(env, dof_names, env_row)
def read_friction_static_row(env, dof_names, env_row)
def read_friction_dynamic_row(env, dof_names, env_row)
def read_friction_activation_vel_row(env, dof_names, env_row)
def read_friction_offset_row(env, dof_names, env_row)
class TunableProperty()
    """Single source of truth for a sysid-tunable per-DOF property.

Used by ``identify._build_parameters`` to construct nominals, by the
sysid optimiser (via ``PROPERTIES[name].bounds``) to pick search ranges,
and by the manual calibration GUI to render sliders and route reads/
writes through one dispatch"""
def _read_solver_row(prop_name)
def _row0(reader)
def install_action_mod_sysid_patch()
```

### dexterous-hands/src/calibration/collect_data.py

```
"""Collect real-XHand1 sysid trajectories via the deployment interface.

This script is XHand1-specific: it talks to ``RoboTeraXHandDeployment``,
the only hand deployment implemented today. The sim-twin / identification
side (``sysid_config.py``, ``identify.py``, ``verify.py``,
``scripts/manual_calibration_gui.py``) is robot-agnostic — once another
hand grows a deployment class, this script generalises with it.

Usage
-----

Identification trace (chirp on all 12 joints, 30 s):

    python src/calibration/collect_data.py --side right         --excitation chirp --duration 30 --output data/xhand_chi"""
class AmpSweepExcitation(Excitation)
    """Per-DOF sine with time-growing envelope (offset relative to recorder center).

``g(t) * A[d] * sin(2π f t + φ[d])`` with ``g`` ramping from ``amp_frac_lo``
to ``amp_frac_hi``. The recorder adds this to either the URDF midpoint or
the live pose (see ``--use-current-pos``)."""
    def __init__(self, num_dofs, dof_indices, duration, amplitude, amp_frac_lo, amp_frac_hi, f_hz, rng, stagger_phase)
    def duration(self)
    def __call__(self, t)
def _build_excitation(kind, num_dofs, duration, amplitude, seed)
def _get_dof_limit_arrays(env, entity_name, dofs_name)
def main()
```

### dexterous-hands/src/calibration/identify.py

```
"""Identify dexterous-hand DOF parameters from recorded real-hand trajectories.

Robot-agnostic: ``--robot`` selects which registered hand the sim twin is
built for (default ``xhand1``). Trajectories must have been recorded from
that hand's real hardware.

Usage
-----

Basic run on one chirp trace:

    python src/calibration/identify.py         --robot xhand1         --trajectory data/xhand_chirp.npz         --output results/xhand_sysid/

Multiple traces (jointly fit):

    python src/calibration/identify.py         --trajectory data/xhand_chirp.npz data/xhand_prbs_train.npz         --output res"""
def _build_parameters(env, dof_names, properties, entity_name, per_dof)
def _residual(env, params, trajectories, entity_name, signals, signal_weights, normalize)
def _fit_scipy(env, params, trajectories)
def _fit_cmaes(env, params, trajectories)
def _warm_start_from_yaml(params, yaml_path)
def main()
```

### dexterous-hands/src/calibration/sysid_config.py

```
"""Sim-twin config for dexterous-hand system identification.

A minimal ``EdenRLConfig`` that spawns a single fixed-base dexterous hand
controlled by an ``ExplicitPDController``. No rewards, no commands, no
termination logic: the config is only used as a rollout substrate for
``eden.extensions.sysid``. Explicit (rather than implicit) PD avoids the
``kd * substep_dt`` armature correction Genesis applies under implicit
damping, which would otherwise inject ~100× phantom inertia and bias
the identification.

The config is robot-agnostic: :func:`make_sim_twin_config` takes any hand
registered in ``RO"""
class ParameterSet(_EdenParameterSet)
    """Slim-YAML ``ParameterSet`` for dexterous-hand sysid artefacts.

Bounds belong to the optimisation setup (``action_mod_sysid.PROPERTIES``),
not to the fitted result — persisting them in ``params_identified.yaml``
would just freeze stale limits next to the artefacts. This subclass omits
``nominal`` / """
    def save_yaml(self, path)
    def load_yaml(cls, path)
def make_parameter(name, dof_names, values)
def save_params_yaml(path, dof_names, values_by_name)
def load_params_yaml(path, dof_names)
def make_sim_twin_config(robot)
def make_argparser(description)
```

### dexterous-hands/src/calibration/sysid_rollout.py

```
"""Shared sim-twin rollout for dexterous-hand calibration scripts.

``identify.py``, ``verify.py``, and ``manual_calibration_gui.py`` all replay
recorded action trajectories through the same sim twin. Centralising the
rollout here on ``RLEnvBase.step`` + ``RLEnvBase.reset`` — rather than the
narrow physics-only stepper in ``eden.extensions.sysid.rollout`` — keeps
three things in agreement:

1. The cost the optimiser converged to and the RMSE the verify script
   reports are produced by the same physics path. Without this, the basic
   "best cost reproduces on verification" sanity check is meaning"""
def refresh_pd_gains(env)
def rollout(env, trajectory, entity_name, signals)
def single_candidate_rollout(env, params, trajectory, entity_name, signals)
def batched_candidate_rollout(env, params, candidates, trajectory, entity_name, signals)
```

### dexterous-hands/src/calibration/verify.py

```
"""Verify identified dexterous-hand parameters against a held-out trajectory.

Applies the YAML produced by ``identify.py`` to the sim twin, replays the
held-out action trace, and reports per-signal RMSE against the measured
response — both *before* and *after* applying the identified parameters
— so it is immediately visible whether identification improved the fit.

Robot-agnostic: ``--robot`` selects the hand the sim twin is built for
(default ``xhand1``); it must match the hand the trajectory came from.

Usage
-----

    python src/calibration/verify.py         --robot xhand1         --traject"""
def _sanitize_plot_stem(stem)
def _expand_trajectory_inputs(items)
def signal_plots(predicted, measured, signals, save_dir, dof_names)
def _rmse(pred, meas)
def _per_signal_rmse(env, params, trajectory, signals)
def main()
```

### dexterous-hands/src/deploy.py

```
class RoboTeraXHandTactileDeployment(RoboTeraXHandDeployment)
    def _resolve_fingertip_order(fingertip_sensors)
    def _scale_fingertip_sensors(self, fingertip_sensors)
    def _augment_state_extra(self, state)
    def action_to_payload(self, action)
    def state_to_observation(self, state)

```python
def state_to_observation(self, state: RobotState) -> dict[str, Any]:
        self._augment_state_extra(state)
        self._state_entity.update(state)
        # Keep deploy extras accessible for deploy-aware observation terms.
        self._state_entity.extra = dict(state.extra)
        return self._env.observation_manager.compute(update_history=True)
```
```

### dexterous-hands/src/entities/objects.py

```
class BallyCube(EntityOptions)
    """A beveled cube. Base size is 1m^3, so use scale to set the size."""
class DexCube(EntityOptions)
    """A colored cube with default size 5cm^3."""
class Bin(EntityOptions)
    """A bin with default size 1m^3."""
```

### dexterous-hands/src/entities/robots/sharpa_hand.py

```
class SharpaHand(RobotOptions)
    def model_post_init(self, context)
```

### dexterous-hands/src/entities/robots/xhand1.py

```
class XHand1(RobotOptions)
```

### dexterous-hands/src/entities/screwdrivers.py

```
class ScrewdriverObj(EntityOptions)
class FatScrewdrivers(GroupedEntityOptions)
    """Screwdriver objects with 1.5x x/y scale to make it suitable for the fat xhand1 fingers."""
```

### dexterous-hands/src/model_config.py

```
"""Shared model/encoder cfg registries selected by --tactile_encoder / --encoder.

``DexHandRslRlRunnerMod`` exposes two CLI flags that pick from named per-group
encoder configs:

- ``--tactile_encoder`` -> key of :data:`TACTILE_ENCODER_CFGS` (applied to the
  ``tactile_sensors`` obs group).
- ``--encoder`` -> key of :data:`GROUP_ENCODER_CFGS` (applied to the ``proprio``
  obs group, and reused for any other encoded groups by convention).

The grid-aware tactile encoders (``tactile_cnn`` / ``tactile_convrnn``) need a
``TactileLayout`` describing ``(num_sensors, grid_h, grid_w, features_per_probe,"""
```

### dexterous-hands/src/models/pre_encode_mlp.py

```
class RslRlPreEncodeMLPOptions(RslRlMLPModelOptions)
    """Actor model configuration with with some observations passed through encoder MLPs before the main MLP head.

Parameters
----------
encoder_cfg: dict[str, Any]"""
class RslRlPreEncodeRNNOptions(RslRlRNNModelOptions)
    """Actor model configuration with with some observations passed through encoder MLPs before the main RNN head.

Parameters
----------
encoder_cfg: dict[str, Any]"""
class RslRlActorPreEncodeMLPOptions(RslRlActorOptions)
    """Actor model configuration with with some observations passed through encoder MLPs before the main MLP head.

Parameters
----------
encoder_cfg: dict[str, Any]"""
class RslRlActorPreEncodeRNNOptions(RslRlActorRNNOptions)
    """Actor model configuration with with some observations passed through encoder MLPs before the main RNN head.

Parameters
----------
encoder_cfg: dict[str, Any]"""
class RslRlTactilePreEncodeMLPOptions(RslRlMLPModelOptions)
    """Critic-style options for the tactile pre-encode MLP model."""
class RslRlActorTactilePreEncodeMLPOptions(RslRlActorOptions)
    """Actor-style options for the tactile pre-encode MLP model."""
class RslRlTactilePreEncodeRNNOptions(RslRlRNNModelOptions)
    """Critic-style options for the tactile pre-encode RNN model."""
class RslRlActorTactilePreEncodeRNNOptions(RslRlActorRNNOptions)
    """Actor-style options for the tactile pre-encode RNN model."""
```

### dexterous-hands/src/models/tactile_encoders.py

```
"""Per-sensor tactile encoders for student/teacher distillation.

These slice a flat ``tactile_sensors`` observation (the concatenation produced by
``TactileSensorRead``) back into per-finger grids and run a small CNN or
:class:`pt_tnn.recurrent_cells.IntersectionRNNCell` over each one. Output is a
``(B, output_dim)`` (inference) or ``(T, B, output_dim)`` (batched recurrent
training) latent that can drop into the ``PreEncode*`` model concat-then-head
pattern.

Flat layout convention (must match TactileSensorRead order):
    flat = (B, T * S * F * H * W)  with the innermost grouping being a single"""
class TactileLayout()
    """Per-sensor grid metadata derived from TactileSensorsMod + history.

Each sensor (patch / link) carries its own ``(H_s, W_s)`` so heterogeneous
placements (e.g. ``low-hand``: fingertips 3x3, palm 4x3, midfingers 2x3)
fit alongside uniform ones. The grid-aware encoders run a per-sensor
ConvRNN/CNN sta"""
    def __post_init__(self)
    def from_dict(cls, d)
    def per_sensor_per_step_dim(self)
    def per_step_dim(self)
    def flat_dim(self)
    def slice_per_sensor(self, x)
def _split_output_dim(output_dim, num_sensors)
def _effective_ksize(cfg_ksize, h, w)
class TactileCNNEncoder(Module)
    """Per-sensor CNN encoder. Non-recurrent; ignores ``masks``/``hidden_state``.

One ``rsl_rl.modules.cnn.CNN`` per sensor (optionally weight-shared across
sensors). The per-sensor flat output is run through a per-sensor Linear
sized to that sensor's own ``(H_s, W_s)``; latents are concatenated to give
t"""
    def __init__(self, layout, cnn_cfg, output_dim, shared_per_sensor)
    def output_dim(self)
    def forward(self, x, masks, hidden_state)
    def reset(self, dones)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def detach_hidden_state(self, dones)
    def get_state_tuple(self)
    def set_state_tuple(self, tup)
def _resolve_convrnn_cell(cell_type)
class TactileConvRNNEncoder(Module)
    """Per-sensor ConvRNN encoder.

Cell kind is configurable via ``cell_type`` in ``convrnn_cfg``: ``intersection``
(default, ``IntersectionRNNCell``), ``gru``, or ``lstm``. The LSTM variant
uses pt_tnn's ``LSTMCell``, whose per-env state packs ``(c, h)`` along the
channel axis -- so its per-sensor state """
    def __init__(self, layout, convrnn_cfg, output_dim, shared_per_sensor)
    def output_dim(self)
    def _state_channels(self)
    def _per_sensor_state_dims(self)
    def _total_state_dim(self)
    def _zero_state(self, num_envs, device, dtype)
    def reset(self, dones)
    def detach_hidden_state(self, dones)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def get_state_tuple(self)
    def set_state_tuple(self, tup)
    def _step(self, frames, state)
    def _project(self, outputs)
    def forward(self, x, masks, hidden_state)
class GroupRNNEncoder(Module)
    """Per-group LSTM/GRU encoder that wraps :class:`rsl_rl.modules.rnn.RNN`.

Use this for arbitrary 1D observation groups (e.g. ``proprio``) when you
want a small recurrent encoder ahead of the policy head. Its state is
persistent across env steps and round-trips through rsl_rl's storage the
same way the"""
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers, rnn_type)
    def output_dim(self)
    def forward(self, x, masks, hidden_state)
    def reset(self, dones)
    def detach_hidden_state(self, dones)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def get_state_tuple(self)
    def set_state_tuple(self, tup)
class CanvasTactileLayout()
    """Per-sensor TactileLayout + a 2D canvas mapping every sensor to a patch.

``placements[i] == (row, col, h, w)`` is where sensor ``i``'s patch sits on
the canvas, in the same order as ``base.grid_hw`` (which mirrors
``sensors_options`` iteration order at layout-derivation time).

The canvas patch ``(h"""
    def __post_init__(self)
    def from_dict(cls, d)
    def flat_dim(self)
    def build_presence_mask(self)
    def scatter_frames(self, per_sensor_frames)
def _scatter_to_canvas(per_sensor_frames, placements, canvas_hw, transposed)
def _masked_global_mean(x, mask)
class TactileCanvasCNNEncoder(Module)
    """Feed-forward CNN over a packed-canvas tactile layout.

Per history frame: scatter per-sensor grids into one canvas, concatenate a
presence-mask channel, run a small conv stack, masked global-mean-pool over
real cells, then ``Linear`` to ``output_dim``. History frames are pooled
independently and con"""
    def __init__(self, layout, cnn_cfg, output_dim)
    def output_dim(self)
    def forward(self, x, masks, hidden_state)
    def reset(self, dones)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def detach_hidden_state(self, dones)
    def get_state_tuple(self)
    def set_state_tuple(self, tup)
class TactileCanvasConvRNNEncoder(Module)
    """ConvRNN over a packed-canvas tactile layout.

Per step: scatter the most-recent frame into the canvas, concat a
presence-mask channel, 1x1-project ``(F+1) -> C_h``, run one
:class:`IntersectionRNNCell` over the whole canvas. The persistent state is
``(N, C_h, H_canvas, W_canvas)``. Output is masked """
    def __init__(self, layout, convrnn_cfg, output_dim)
    def output_dim(self)
    def _state_dim(self)
    def _zero_state(self, num_envs, device, dtype)
    def reset(self, dones)
    def detach_hidden_state(self, dones)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def get_state_tuple(self)
    def set_state_tuple(self, tup)
    def _step(self, frame_with_mask, state)
    def _project(self, state)
    def _build_canvas(self, per_sensor_frames)
    def forward(self, x, masks, hidden_state)
def _make_activation(name)
```

### dexterous-hands/src/models/tactile_pre_encode.py

```
"""Pre-encode models that dispatch each observation group through an encoder of a
chosen *kind* (``mlp``, ``tactile_cnn``, ``tactile_convrnn``) before the policy
MLP/RNN head. Mirrors the structure of
:class:`rsl_rl.models.pre_encode_model.PreEncodeMLPModel` / ``PreEncodeRecurrentModel``
and reuses :class:`PreEncodeMixin`'s pass-through / concat semantics.

State on the wire (for storage round-trip):
    - Non-recurrent head + recurrent encoder -> ``get_hidden_state()`` returns
      the encoder's 3D tensor.
    - Recurrent head (LSTM/GRU) + recurrent encoder -> returns a tuple whose
      last e"""
def _build_encoder(kind, group, cfg, in_dim, default_activation)
def _encoder_output_dim(encoder, group)
def _encoder_recurrent(encoder)
class _TactilePreEncodeBuild(PreEncodeMixin)
    """PreEncode prep that dispatches each group on a ``kind`` field."""
    def _pre_encode_prepare(self, obs, obs_groups, obs_set, activation, encoder_cfg, encoders)
    def _pre_encode_get_obs_dim(self, obs, obs_groups, obs_set)
def _bundle_to_parts(hidden_state)
def _parts_to_bundle(parts)
class TactilePreEncodeMLPModel(_TactilePreEncodeBuild, MLPModel)
    """Pre-encode MLP head + (CNN | ConvRNN | MLP) per-group encoders.

If any encoder is recurrent, the model exposes recurrent semantics so PPO
saves/restores hidden state."""
    def __init__(self, obs, obs_groups, obs_set, output_dim, hidden_dims, activation, obs_normalization, distribution_cfg, encoder_cfg, encoders)
    def _split_bundle_to_groups(self, hidden_state)
    def _encoded_latent(self, obs, masks, per_group_state)
    def get_latent(self, obs, masks, hidden_state)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def reset(self, dones, hidden_state)
    def detach_hidden_state(self, dones)
    def forward(self, obs, masks, hidden_state, stochastic_output)
    def _get_obs_dim(self, obs, obs_groups, obs_set)
    def _get_latent_dim(self)
    def as_jit(self)
    def as_onnx(self, verbose)
class TactilePreEncodeRecurrentModel(_TactilePreEncodeBuild, MLPModel)
    """Pre-encode + tactile encoders + top-level LSTM/GRU head.

Hidden state bundle = ``(policy_rnn_state, encoder_state)``; LSTM
policy state is itself a ``(h, c)`` tuple, so the bundle becomes
``(h, c, encoder_state)`` in that case (storage iterates the tuple)."""
    def __init__(self, obs, obs_groups, obs_set, output_dim, hidden_dims, activation, obs_normalization, distribution_cfg, encoder_cfg, encoders, rnn_type, rnn_hidden_dim, rnn_num_layers)
    def _split_bundle(self, hidden_state)
    def _encoded_latent(self, obs, masks, per_group_state)
    def get_latent(self, obs, masks, hidden_state)
    def _top_rnn_unpadded(self, pre, policy_state)
    def get_hidden_state(self)
    def set_hidden_state(self, hidden_state)
    def reset(self, dones, hidden_state)
    def detach_hidden_state(self, dones)
    def forward(self, obs, masks, hidden_state, stochastic_output)
    def _get_obs_dim(self, obs, obs_groups, obs_set)
    def _get_latent_dim(self)
    def as_jit(self)
    def as_onnx(self, verbose)

```python
def _pre_encode_get_obs_dim(  # type: ignore[override]
        self,
        obs: TensorDict,
        obs_groups: dict[str, list[str]],
        obs_set: str,
    ) -> tuple[list[str], int]:
        """Same as parent but allows tactile groups whose input is 2D (B, flat_dim) or
        padded 3D (T, B, flat_dim) at training time. We measure on the *last* dim only."""
        active_obs_groups = obs_groups[obs_set]
        encoders = self._encoders_arg
        encoder_cfg = self._encoder_cfg

        if encoders is None and encoder_cfg is not None:
            extra_cfg = set(encoder_cfg.keys()).difference(active_obs_groups)
            if extra_cfg:
                raise ValueError(f"encoder_cfg keys not in obs set: {sorted(extra_cfg)}")
        encode_keys = set(encoders.keys()) if encoders is not None else set(encoder_cfg or ())
        unknown = encode_keys.difference(active_obs_groups)
        if unknown:
            raise ValueError(f"encoder_cfg references groups not in obs_groups[{obs_set!r}]: {sorted(unknown)}")

        self.obs_groups_encode = [g for g in active_obs_groups if g in encode_keys]
        pass_groups = [g for g in active_obs_groups if g not in encode_keys]

        if not self.obs_groups_encode:
            raise ValueError("At least one observation group must be in encoder_cfg.")

        self.encode_input_dims = {g: obs[g].shape[-1] for g in self.obs_groups_encode}
        obs_dim = sum(obs[g].shape[-1] for g in pass_groups)
        self.obs_groups = pass_groups
        return pass_groups, obs_dim
```

```python
def _get_obs_dim(
        self,
        obs: TensorDict,
        obs_groups: dict[str, list[str]],
        obs_set: str,
    ) -> tuple[list[str], int]:
        return self._pre_encode_get_obs_dim(obs, obs_groups, obs_set)
```

```python
def _get_obs_dim(
        self,
        obs: TensorDict,
        obs_groups: dict[str, list[str]],
        obs_set: str,
    ) -> tuple[list[str], int]:
        return self._pre_encode_get_obs_dim(obs, obs_groups, obs_set)
```
```

### dexterous-hands/src/optimization.py

```
def apply_params_to_config(params, config)
def sample_hyperparams(trial, hyperparam_ranges)
def run_evaluation(config, runner, n_episodes, device, save_video, metric_name)
```

### dexterous-hands/src/registry.py

```
def _load_tasks()
def _checkpoint_iter(path)
def find_latest_checkpoint(log_dir)
def get_checkpoint_path(checkpoint, try_load_latest)
def build_run_name(run_name, task, robot, sensors, config)
def load_config_section(config_paths, section_name)
def build_modifiers_from_args(args, task_name)
def get_task_config(run_name, task_name, modifiers, config_override_path)
def get_task_config_from_args(args, run_name, upload_logs)
def get_argparser(description)
def position_camera_config(config)
def save_video_from_checkpoint(config, checkpoint, seconds, video_path, tactile_npz_path)
def launch_video_from_checkpoint(config_path, checkpoint, seconds)
def save_video_from_runner(config, runner, video_path, seconds)
def patch_on_policy_runner_to_save_video()
def make_runner(env, checkpoint, actor_checkpoint, critic_checkpoint, log_dir, load_actor_distribution)
def get_hyperparam_ranges(task_name)
```

### dexterous-hands/src/shared_terms.py

```
def _env_cache_masked_set(env, attr, env_ids, value)
def _name_matches_alias(name, alias)
def filter_hand_dof_names(dof_names)
def frozen_link_names(link_names, dof_names, frozen_dofs)
class PartialFrozenExplicitPDController(ExplicitPDController)
    """Delta explicit PD on active DOFs while frozen DOFs hold their reset pose."""
    def build(self)
    def reset(self, envs_idx)
    def apply_actions(self)
class RootPoseController(ActionTerm)
    """Action term that controls the root (base) 6 DOF pose via control_dofs_pos(dofs_idx_local=slice(0, 6)).

The controlled entity should be a floating-base robot (is_fixed_base=False).

Raw actions are 6D: [pos_x, pos_y, pos_z, euler_x, euler_y, euler_z], typically in [-1, 1].
Each dimension is linearly"""
    def __init__(self, env, options)
    def action_dim(self)
    def build(self)
    def compute(self, actions)
    def reset(self, envs_idx)
    def apply_actions(self)
class RotationAxisCommand(CommandTerm)
    """Command for target rotation axis.

Generates a random axis around which the object should rotate.
In HORA, this is typically the Z-axis (up).

Parameters
----------
axis_mode : str
    Mode for axis generation: "z_only", "random", or "xyz". Default: "z_only""""
    def __init__(self, env, options)
    def command(self)
    def _resample_command(self, envs_idx)
    def _update_command(self)
    def _update_metrics(self)
class BaseRotationCommand(CommandTerm)
    """Shared pieces for orientation goal commands: tracked quaternion, optional
``vis`` entity sync, and orientation error / success streak metrics."""
    def __init__(self, env, options)
    def build(self)
    def command(self)
    def _sync_goal_vis_orientation(self, envs_idx)
    def _update_orientation_stats(self)
    def reset(self, envs_idx)
class ConstantOrientationCommand(BaseRotationCommand)
    """Target orientation: intrinsic XYZ Euler offset (degrees) composed with the object's live root quaternion."""
    def build(self)
    def _apply_goal_from_object_quat(self, envs_idx)
    def _resample_command(self, envs_idx)
    def _update_command(self)
class TargetRotationCommand(BaseRotationCommand)
    """Command generator for target quaternion orientation.

Generates random quaternion targets by sampling random orientations
around the X/Y/Z axes.

Parameters
----------
x_range : tuple[float, float], optional
    Range for rotation around x-axis in radians.
y_range : tuple[float, float], optional
   """
    def __init__(self, env, options)
    def __str__(self)
    def _resample_command(self, envs_idx)
    def _update_command(self)
def base_rot6d(env)
def goal_rot6d_diff(env)
class OrientationErrorObs(ObservationTerm)
    """Angular error (rad) between the command goal quaternion and the tracked entity.

Caches the last ``quat_error_magnitude`` and reuses it until ``command.quat`` or the object quaternion
change, so multiple reward terms can read one computation per
post-physics state (including after env resets resampl"""
    def __init__(self, env, options)
    def reset(self, envs_idx)
    def compute(self)
def _orientation_error_for_rewards(env)
class TactileSensorRead(ObservationTerm)
    """Read tactile observations from deploy extras when available, else sim sensors."""
    def build(self)
    def _read_sim_sensors(self)
    def _compute_deploy_tactile(self)
    def compute(self)
class CachedObs(ObservationTerm)
    def __init__(self, env, options)
    def compute(self)
def _tc_quat_to_rotvec(quat)
class AxisRotationProgressReward(RewardTerm)
    """Signed spin rate (rad/s) about a fixed object-frame axis.

The reward tracks the object quaternion internally, accumulates the total
signed rotation about the configured object axis, and exposes the last per-step
signed increment for subclasses."""
    def build(self)
    def _refresh_axis_obj(self, envs_idx, obj_quat)
    def reset(self, envs_idx)
    def _step_terms(self)
    def compute(self, envs_idx)
    def last_step_signed_axis_rad(self)
    def total_signed_axis_rad(self)
def surface_distance_reward(env)
class ForceMagnitudePenalty(RewardTerm)
    """Reward based on force sensor magnitude."""
    def build(self)
    def compute(self, envs_idx)
def orientation_success_bonus(env)
def rotation_reward(env)
def termination_penalty(env)
def track_orientation_inv_l2(env)
def track_orientation_gaussian(env)
def object_dist_penalty(env)
def pose_diff_penalty(env)
def work_penalty(env)
def ee_work_penalty(env)
def episode_reward_metric(env)
class UpdateCurriculumWeights(MetricTerm)
    """Linearly interpolates selected reward weights using ``env.common_step_counter``.

Uses :class:`MetricMode.RESET` so this side-effect term does not participate in
interval success aggregation with other metrics (e.g. ``objective``)."""
    def __init__(self, env, options)
    def build(self)
    def compute(self)
class SetSampledBottomAlignedPos(EventTerm)
    """Place the entity at a sampled xy with bottom-aligned z using precomputed AABB offsets."""
    def __init__(self, env, options)
    def build(self)
    def compute(self, envs_idx)
class LoadGraspPose(EventTerm)
    def __init__(self, env, options)
    def build(self)
    def _env_ids_from_index(self, envs_idx)
    def _resolve_primary_obj_dof_index(self)
    def _reset_object_dof_state(self, envs_idx, n_envs)
    def _offset_from_configured_action_offset(self, dof_names)
    def _sampled_pos_for_dofs(self, sampled_joint_pos, dof_names)
    def _sync_action_term_to_grasp(self, envs_idx, sampled_joint_pos)
    def compute(self, envs_idx)
class ResetRobotFromCachedGrasp(EventTerm)
    """Offset the robot away from the cached grasp target after sampling it."""
    def build(self)
    def compute(self, envs_idx)
class RandomizeFrictionRatioWithObs(RandomizeFrictionRatio)
    def compute(self, envs_idx)
class RandomizeMassShiftWithObs(RandomizeMassShift)
    def compute(self, envs_idx)
def obj_below_height(env)
def obj_tilted_past_threshold(env)
def obj_pos_drift_from_grasp(env)

```python
def _orientation_error_for_rewards(
    env: EnvBase,
    *,
    command_name: str,
    obs_term_name: str | None,
    entity_name: str | None,
) -> torch.Tensor:
    """Scalar angular error per env; either from ``OrientationErrorObs`` or a direct quaternion measure."""
    if obs_term_name is not None:
        raw = env.observation_manager.get_term(obs_term_name).compute()
        if raw.ndim == 2 and raw.shape[-1] == 1:
            return raw.squeeze(-1)
        return raw.reshape(env.num_envs)
    command = env.command_manager.get_term(command_name)
    ent = entity_name if entity_name is not None else getattr(command, "entity_name", "obj")
    return quat_error_magnitude(env.entities[ent].get_quat(), command.quat)
```

```python
def surface_distance_reward(
    env: EnvBase, *, obs_name: str = "surface_distance", nearest_k: int = -1, sigma: float = 0.1
) -> torch.Tensor:
    """
    Reward based on surface distance sensor readings.
    ``obs_name`` should be a SensorRead term that reads SurfaceDistanceProbe sensors.

    Parameters
    ----------
    nearest_k : int
        Use only the ``nearest_k`` smallest per-channel distances (closest sensors). If <= 0,
        use all channels (same as summing every fingertip/probe).
    sigma : float
        Standard deviation of the Gaussian kernel.
    """
    sensor_obs_term = env.observation_manager.get_term(obs_name)
    # Fresh read: ``_cached`` is only updated during ``observation_manager.compute``, which runs after rewards.
    readings = sensor_obs_term.compute()
    dist_sq = readings**2
    n = dist_sq.shape[-1]
    k = n if nearest_k <= 0 else min(nearest_k, n)
    if k >= n:
        nearest_dist_sq = dist_sq
    else:
        nearest_dist_sq, _ = torch.topk(dist_sq, k=k, largest=False, dim=-1)
    return torch.exp(-nearest_dist_sq / sigma**2).sum(dim=-1)
```

```python
def rotation_reward(
    env: EnvBase,
    *,
    entity_name: str = "obj",
    command_name: str = "rotation_axis",
    local_axis: tuple[float, float, float] | None = None,
    angvel_clip_min: float = -0.5,
    angvel_clip_max: float = 0.5,
) -> torch.Tensor:
    """Reward for rotating object around target axis.

    Based on HORA implementation: measures angular velocity component
    along the target rotation axis.

    Parameters
    ----------
    entity_name : str
        Name of the object entity. Default: "obj"
    command_name : str
        Name of the rotation axis command. Default: "rotation_axis"
    local_axis : tuple[float, float, float] | None
        If set, an axis fixed in the entity's local frame; it is rotated by the entity's
        current quaternion each step so the reward tracks an object-attached axis (e.g.
        a screwdriver's shaft). Overrides ``command_name`` when provided. Default: None
        (use the world-frame command axis).
    angvel_clip_min : float
        Minimum angular velocity for clipping. Default: -0.5
    angvel_clip_max : float
        Maximum angular velocity for clipping. Default: 0.5
    """
    obj = env.entities[entity_name]

    # Get current and previous object rotation
    obj_quat = obj.get_quat()

    # Initialize previous quat buffer if needed
    if not hasattr(env, "_prev_obj_quat"):
        env._prev_obj_quat = obj_quat.clone()
        return torch.zeros(env.num_envs, device=env.device)

    # Compute angular difference (quat_mul(curr, conjugate(prev)))
    quat_diff = quat_mul(obj_quat, quat_conjugate(env._prev_obj_quat))

    # Angular velocity = axis_angle / dt
    axis_angle = axis_angle_from_quat(quat_diff)
    dt = env.env_options.sim_dt * env.env_options.decimation
    ang_vel = axis_angle / dt

    if local_axis is not None:
        local = torch.tensor(local_axis, device=env.device, dtype=obj_quat.dtype).expand(env.num_envs, 3)
        target_axis = gu.transform_by_quat(local, obj_quat)
    else:
        target_axis = env.command_manager.get_command(command_name)

    # Compute dot product: positive when rotating in correct direction
    vec_dot = (ang_vel * target_axis).sum(dim=-1)

    # Clip to configured range (HORA: [-0.5, 0.5])
    rotation_reward = torch.clip(vec_dot, min=angvel_clip_min, max=angvel_clip_max)

    # Store for next iteration
    env._prev_obj_quat = obj_quat.clone()

    return rotation_reward
```

```python
def episode_reward_metric(env: EnvBase, *, reward_names: list[str], weights: list[float]) -> torch.Tensor:
    total_reward = torch.zeros(env.num_envs, device=env.device)
    for reward_name, metric_weight in zip(reward_names, weights):
        term_idx = env.reward_manager._term_names.index(reward_name)
        term_weight = env.reward_manager._weights[term_idx]
        episode_sum = env.reward_manager._episode_sums[:, term_idx].float()
        total_reward += episode_sum / env.max_episode_length_s / term_weight * metric_weight
    return total_reward
```
```

### dexterous-hands/src/tactile_compare.py

```
"""Record + live-visualize xhand1 fingertip tactile readings: real hand vs sim.

Used by both ``main.py`` deploy mode and ``scripts/manual_calibration_gui.py``.
The real hand exposes per-finger aggregate force (``calc_pressure``) via
``RobotState.extra["fingertip_sensors"]``; the sim exposes the same quantity
through ``agg_force`` tactile sensors (``postprocess_agg_force`` converts a
sensor's raw read into the identical ``[fx, fy, fz]`` convention). This module
aligns the two by canonical finger index, writes them to a CSV in the log dir,
and feeds a 5-subplot live line plot (one finger per subpl"""
def fingertip_link_order(robot_cfg)
def resolve_sim_sensor_names(env)
def resolve_real_finger_ids(deploy_state)
def finger_indices(names)
def load_tactile_scales(path)
def read_sim_tactile(env, sim_sensor_names)
def read_real_tactile(deploy_state)
class TactileComparisonRecorder()
    """Owns the CSV file and the in-memory sample buffer feeding the live plot."""
    def __init__(self, log_dir)
    def _header(self)
    def _open(self)
    def record(self, t)
    def close(self)
    def plot_labels(self)
    def plot_data(self)
class TactileLinePlot(_MPLLinePlotOptions)
    """Options marker selecting :class:`TactileLinePlotter`.

Same fields as ``MPLLinePlot``; the distinct type is what routes
``scene.start_recording`` to the custom plotter via the recorder registry."""
class TactileLinePlotter(_MPLLinePlotter)
    """``MPLLinePlotter`` with fixed per-channel colors and a matching legend.

The stock plotter colors lines from a shared global cycle (so colors drift
when other plots are open) and emits one legend entry per line across every
subplot. This subclass recolors each line from :data:`_TACTILE_LINE_STYLE`
a"""
    def build(self)
def start_tactile_plot(scene, recorder)
def reset_plotter(plotter)
def apply_isolation(plotter, recorder)
```

### dexterous-hands/src/tactile_record.py

```
"""Record per-step tactile sensor readings during a play episode and save them to an .npz.

``main.py --mode=play --save_tactile`` builds a :class:`TactileEpisodeRecorder`,
calls :meth:`TactileEpisodeRecorder.record` once per simulation step, and finally
:meth:`TactileEpisodeRecorder.save`. The resulting .npz holds the per-step tactile
field for offline analysis.

For every ``tactile_*`` sensor on the env this captures, per step and for one env:
  - the world-frame probe positions (probes move with the hand), and
  - the per-probe reading -- a 3D vector for the vector sensors (elastomer /
    for"""
def _discover_tactile_sensors(env)
def _env_slice(tensor, env_idx)
class TactileEpisodeRecorder()
    """Buffers per-step tactile readings + probe positions and writes them to an .npz."""
    def __init__(self, env)
    def sensor_names(self)
    def _link_pose(self, gs_sensor)
    def _probe_world_pos(self, gs_sensor, link_pose)
    def record(self, t)
    def save(self, path)
```

### dexterous-hands/src/tactile_sensors.py

```
"""Tactile sensor type registry.

Each tactile sensor type is described by a :class:`TactileSensorSpec`, shared by
``TactileSensorsMod`` (which builds ``SensorOptions``) and ``TactileSensorRead``
(which reads + postprocesses sensor output and converts xhand1 hardware data to
sim format). Adding a sensor type means adding one entry to ``TACTILE_SENSORS``
-- no ``if/else`` chains to touch."""
def _history_length(sensor)
def _apply_temporal_reduction(tensor, history_length, mode)
def postprocess_generic(data)
def postprocess_force(data)
def postprocess_agg_bool(data)
def postprocess_agg_force(data)
def _calc_pressure_tensor(reading, device)
def xhand1_agg_force(reading)
def xhand1_bool(reading)
class TactileSensorSpec()
    """Describes one tactile sensor type end to end.

Parameters
----------
name : str
    Sensor type name, e.g. ``"agg_force"`` -- the key used in ``TACTILE_SENSORS``.
placement : {"probes", "link"}
    ``"probes"`` for probe-config sensors, ``"link"`` for link-attached sensors.
sensor_cls : type
    The"""
def _load_sensor_params()
def _params(name)
def _noise(name)
def spec_for_sensor_name(name)
```

### dexterous-hands/src/task_mods.py

```
def _log_info(message)
def _as_float_list(values)
def _controller_dof_names(controller)
def _filter_param_values_to_controller_dofs(property_name, dof_names, values, controller_dof_names)
def _apply_identified_action_modifier_params(config, cal)
class RobotHandMod(TaskMod)
    def __init__(self, robot)
    def _configure_robot_and_actions(self, config, robot_instance)
    def apply(self, config)
def _track_link_sensor_args(track_link)
class RobotHandWithPrivSensorsMod(RobotHandMod)
    def __init__(self, robot)
    def apply(self, config)
def _make_options_ghost(opts)
class ManipulationObjectMod(TaskMod)
    """Add the object entity to manipulate.

Parameters
----------
entity_name : str
    The name of the entity to set.
add_vis_entity : bool
    Whether to additionally add "vis_entity_name" with same morph as the object but fixed and transparent."""
    def __init__(self, obj)
    def apply(self, config)
class TactileSensorsMod(TaskMod)
    def __init__(self, sensors, temporal_reduction)
    def _parse_sensors_str(sensors)
    def apply(self, config)
    def _frozen_dofs(config)
    def _get_sensors_dict(self, robot_cfg, placement_type, sensors_type, noisy, frozen_dofs)
    def _split_placement_key(cls, placement_type)
    def _filter_probe_data_by_subset(cls, probe_data, metadata, subset)
    def _parse_probe_config(probe_cfg_path)
def derive_tactile_layout(config)
def _iter_tactile_link_names(config)
def _load_canvas_json(path)
def _canvas_matches(canvas_data, active_links, grid_hw)
def _repack_active_placements(placements, canvas_hw)
def derive_canvas_tactile_layout(config)
def _grid_shape(probe_local_pos)
class ObservationHistoryLengthMod(TaskMod)
    def __init__(self, obs_hist)
    def apply(self, config)
class RewardWeightCurriculumMod(TaskMod)
    def __init__(self, rwc)
    def apply(self, config)
class RslRlRunnerMod(TaskMod)
    def __init__(self, actor, critic, algo, rnd, max_iters)
    def apply(self, config)
    def _filter_obs_groups_by_config(obs_groups, observations, task_name)
    def _get_model_options(self, model_type, obs_groups, is_actor, encoder_obs_group_key)
class DexHandRslRlRunnerMod(RslRlRunnerMod)
    """Stage 1: Teacher training. RND enabled. MLP model.
Stage 2: Student-teacher distillation. Student can have different models (--model flag.)
Stage 3: Student RL. RND disabled."""
    def __init__(self, stage, model, tactile_encoder, encoder, rnd, priv_student, max_iters)
    def apply(self, config)
    def _resolve_encoder_cfg(self, config, filtered_obs_groups)
```

### dexterous-hands/src/tasks/in_hand_repose/config.py

```
"""Configuration for in-hand repose task.

Based loosely on IsaacLab's Isaac-Repose-Cube-Allegro-v0 environment.
Reference: https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/manager_based/manipulation/inhand/config/allegro_hand/allegro_env_cfg.py"""
class InHandReposeRobotMod(RobotHandWithPrivSensorsMod)
    """Task-specific robot material, fixed base, and fingertip proximity sensors."""
    def apply(self, config)
class InHandReposeConfig(EdenRLConfig)
    """Reorient an object in hand to match a target orientation."""
```

### dexterous-hands/src/tasks/in_hand_repose/custom_terms.py

```
class OrientationProgressReward(RewardTerm)
    """Reward per-second reduction in orientation error to the active goal."""
    def build(self)
    def _current_error(self)
    def reset(self, envs_idx)
    def compute(self, envs_idx)
class TimeoutTrackingTargetRotationCommand(TargetRotationCommand)
    """``TargetRotationCommand`` that flags envs whose goal was just reset by *timeout*.

Captures the timeout mask before ``super().compute(dt)`` runs the resample
(which refills ``time_left``), so ``_last_timeout_reset`` is True for one
step on the env(s) whose resampling timer expired. Success-driven go"""
    def build(self)
    def compute(self, dt)
def target_timeout_reset_penalty(env)
```

### dexterous-hands/src/tasks/in_palm_rotate/config.py

```
"""Configuration for in-palm rotate task.

A partial-hand in-palm rotation task where only the thumb and middle finger
are active; the index, ring, and pinky fingers are frozen. Uses the
``PARTIAL_HAND_CONTROLLER`` (with ``scale_ratio=0.5``) so the policy controls
only the active fingers while the frozen DOFs hold their reset pose.

Based loosely on dexterous manipulation paper from ByteDance: https://arxiv.org/pdf/2601.02778"""
class InPalmRotateRobotMod(RobotHandWithPrivSensorsMod)
    def _configure_robot_and_actions(self, config, robot_instance)
    def apply(self, config)
class InPalmRotateConfig(EdenRLConfig)
    """Rotate an object resting on the palm of the robot hand along the target axis,
using only the thumb and middle finger (index/ring/pinky are frozen).

The orientation command is a shifting curriculum: each goal is a fixed body-axis
step (default 90°) from the object's current pose, and advances again """
```

### dexterous-hands/src/tasks/in_palm_rotate/custom_terms.py

```
"""Custom terms for the in_palm_rotate task.

Holds the reward / observation / command terms for the partial-hand in-palm
rotation task, plus the ``SetRandomActiveDofsPos`` event used to randomize only
the active (non-frozen) DOFs at reset."""
class GatedAxisRotationProgressReward(AxisRotationProgressReward)
    """Signed spin rate about the task axis with a hard perpendicular-error gate.

Progress is zeroed when the goal-relative orientation error component orthogonal to the rotation axis
exceeds the command's ``allowed_off_axis_error``."""
    def compute(self, envs_idx)
def is_dropped_penalty(env)
def off_axis_orientation_penalty(env)
class ObjectSizeObs(ObservationTerm)
    """Static object dimensions as ``[height_z, width_xy]`` in meters."""
    def __init__(self, env, options)
    def build(self)
    def compute(self)
def reached_max_consecutive_successes(env)
class SteppingRotationCommand(BaseRotationCommand)
    """Shifting orientation goal for continuous in-hand rotation.

On time/env resample, the goal is ``delta_quat * default_root_quat`` (one world-axis
step from the object’s configured default pose, not its live pose).

On success, the goal advances by ``delta_quat * goal_quat`` — a further world-axis
ste"""
    def __init__(self, env, options)
    def build(self)
    def __str__(self)
    def _apply_world_axis_step(self, envs_idx, base_quat_all)
    def _resample_command(self, envs_idx)
    def _update_orientation_stats(self)
    def _update_command(self)
class SetRandomActiveDofsPos(SetRandomDofsPos)
    """``SetRandomDofsPos`` restricted to a named subset of DOFs.

DOFs not listed in ``dofs_name`` are left untouched, so the frozen fingers
keep their canonical default pose instead of being randomized at reset.
When ``dofs_name`` is empty this behaves exactly like ``SetRandomDofsPos``."""
    def build(self)
    def compute(self, envs_idx)
```

### dexterous-hands/src/tasks/rummage_hot/config.py

```
"""Configuration for rummaging a bin of objects to find the target hot object."""
class RummageHotTaskMod(RobotHandWithPrivSensorsMod)
    """Robot after static scene (predictable link indices); hand pose, sensors, and reset events."""
    def apply(self, config)
class RummageHotConfig(EdenRLConfig)
```

### dexterous-hands/src/tasks/rummage_hot/custom_terms.py

```
class TemperatureDiffReading(SensorRead)
    """Per-step delta of concatenated sensor readings (times ``scale``); ``_last_absolute`` mirrors the latest absolute read."""
    def build(self)
    def _read_absolute(self)
    def reset(self, envs_idx)
    def compute(self)
def _axis_cell_centers(lo, hi, spacing, device)
class RandomlyPlaceInGrid(EventTerm)
    """Place entities in a 3D grid expressed in a (possibly tilted) bin's local frame.

Positions ``range_{x,y,z}`` and the yaw rotation are sampled in the bin's local frame,
then composed with ``bin_quat`` (in ``(w, x, y, z)`` order) to produce world-frame
poses. Defaults to identity, which reproduces the"""
    def build(self)
    def compute(self, envs_idx)
def temperature_reading_reward(env)
class RevealedObjectPosition(ObservationTerm)
    """Object position (relative to the robot base), revealed only after first touch.

Each episode the position is hidden (returns zeros) until any fingertip link of
``robot_name`` makes force-bearing contact with ``object_name``. From that first
contact until the next reset, the object's position relativ"""
    def build(self)
    def reset(self, envs_idx)
    def compute(self)
class ContactDurationObs(ObservationTerm)
    """Per-fingertip continuous-contact duration with whichever ball it currently touches.

Mirrors the bookkeeping in :class:`SameBallContactReward` so the teacher can
observe the hidden timer the windowed ``ball_contact`` reward depends on. Per
fingertip, tracks the ball carrying the largest aggregate co"""
    def build(self)
    def reset(self, envs_idx)
    def _fingertip_ball_distance(self)
    def compute(self)
class SameBallContactReward(RewardTerm)
    """Reward fingertips holding continuous contact with a single ball.

Per fingertip, tracks which ball it currently touches (the one carrying the
largest aggregate contact force) and how many consecutive steps that contact
with that *same* ball has lasted. While the continuous contact duration lies
with"""
    def build(self)
    def reset(self, envs_idx)
    def _fingertip_ball_force(self)
    def compute(self, envs_idx)
class DistinctBallCoverageReward(RewardTerm)
    """Reward touching each distinct ball once per episode.

A ball is "covered" the first step its continuous force-bearing contact with
any fingertip has lasted at least ``min_seconds``; that step contributes
``1.0`` to the reward and the ball is not credited again until the env
resets. The per-step rewa"""
    def build(self)
    def reset(self, envs_idx)
    def compute(self, envs_idx)
def max_temperature_metric(env)
class ObjectLiftedHold(TerminationTerm)
    """Success termination: the object has stayed lifted for ``hold_seconds``.

An env terminates once the object's lowest point (AABB bottom) has stayed at or
above ``lift_height`` for ``hold_seconds`` of continuous simulated time. Any step
with the object below that height resets the env's hold timer."""
    def build(self)
    def reset(self, envs_idx)
    def compute(self)
class BallGraspSequenceCommand(CommandTerm)
    """Per-env deck of ball indices; the current target advances when lifted.

On each env reset the deck is reshuffled to a fresh permutation of
``ball_names`` (random sampling without replacement) and each ball's
initial z is captured. The current target ``_target_idx`` is
``deck[deck_pos]``. The current"""
    def build(self)
    def command(self)
    def _refresh_command_buf(self)
    def _envs_idx_to_bool(self, envs_idx)
    def _resample_command(self, envs_idx)
    def _fingertip_ball_distance(self)
    def _update_command(self)
class CurrentTargetPositionObs(ObservationTerm)
    """Position of the currently commanded ball, relative to the robot base."""
    def build(self)
    def compute(self)
class TargetLiftReward(RewardTerm)
    """Reward lifting the currently commanded ball above its episode-start z.

Reads ``_target_idx`` and ``_initial_z`` from the
:class:`BallGraspSequenceCommand` term. Returns
``clamp((target_z - initial_z) / lift_delta, 0, 1)``, so it ramps up
smoothly until the ball has been lifted by ``lift_delta`` met"""
    def build(self)
    def compute(self, envs_idx)
def command_last_advance(env)
def target_contact_decay_reward(env)
def non_hot_staleness_penalty(env)
def command_hot_success_reward(env)
def command_hot_success(env)

```python
def temperature_reading_reward(
    env: EnvBase,
    *,
    obs_name: str = "temp_sensors",
    target_temperature: float = 100.0,
) -> torch.Tensor:
    """Linear shaping: progress of the best-matching sensor toward ``target_temperature``.

    Uses the sensor with smallest current absolute error to the target; reward is
    ``reward_scale * (|T_prev - target| - |T_curr - target|)`` for that sensor.
    ``T_prev`` is the observation term's stored previous absolute read (updated when
    observations compute, after rewards — do not call ``compute()`` here).

    For plain ``SensorRead`` terms (no ``_read_absolute``), falls back to
    ``exp(-min_i |T_i - target|)``.
    """
    term = env.observation_manager.get_term(obs_name)
    read = getattr(term, "_read_absolute", None)
    if read is None:
        temperatures = term.compute()
        min_abs_err, _ = torch.abs(temperatures - target_temperature).min(dim=-1)
        return torch.exp(-min_abs_err)
    curr = read()
    prev = getattr(term, "_prev", None)
    n_env = curr.shape[0]
    if prev is None:
        return torch.zeros(n_env, device=curr.device, dtype=curr.dtype)
    err_c = torch.abs(curr - target_temperature)
    err_p = torch.abs(prev - target_temperature)
    k = err_c.argmin(dim=-1)
    batch = torch.arange(n_env, device=curr.device)
    closer = err_p[batch, k] - err_c[batch, k]
    return closer
```

```python
def target_contact_decay_reward(
    env: "EnvBase",
    *,
    command_name: str = "grasp_target",
    hold_seconds: float = 1.0,
) -> torch.Tensor:
    """Per-step shaping for touching the currently commanded target, decaying with cumulative on-target time.

    Per fingertip, contribution is ``max(0, 1 - cumulative_target_time / hold_seconds)``
    while currently in contact with the target ball, else 0. ``cumulative_target_time``
    is the command term's ``_target_contact_time`` counter, which only resets when
    the deck advances or the env resets — so tap-and-release cannot refund the
    per-target reward budget.
    """
    cmd = env.command_manager.get_term(command_name)
    cumulative = cmd._target_contact_time.to(torch.float32) * cmd._dt
    decay = (1.0 - cumulative / hold_seconds).clamp(min=0.0)
    on_target_now = cmd._contact_ball == cmd._target_idx.unsqueeze(-1)
    return (decay * on_target_now.to(decay.dtype)).sum(dim=-1)
```

```python
def command_hot_success_reward(env: "EnvBase", *, command_name: str = "grasp_target") -> torch.Tensor:
    """1.0 on the step the hot target was held lifted long enough (also triggers termination)."""
    return env.command_manager.get_term(command_name)._hot_success.to(torch.float32)
```
```

### dexterous-hands/src/tasks/screwdriver/config.py

```
"""Rotate screwdriver task."""
class ScrewdriverRobotMod(RobotHandWithPrivSensorsMod)
    """Load the hand and apply screwdriver-specific robot/action settings."""
    def __init__(self, robot, include_ext_force)
    def _configure_robot_and_actions(self, config, robot)
    def apply(self, config)
class ScrewdriverConfig(EdenRLConfig)
    """Free-moving heterogeneous screwdriver rotation task."""
```

### dexterous-hands/src/tasks/screwdriver/custom_terms.py

```
"""Screwdriver task helpers, rewards, observations, and terminations."""
def _name_matches_alias(name, alias)
def _get_robot_metadata(robot)
def _iter_hand_links(robot)
def _link_matches_finger(link_name, finger)
def resolve_hand_dof_indices(robot)
def filter_hand_dof_names(dof_names)
def resolve_hand_link(robot)
def resolve_grasp_target_link_name(entity)
def resolve_grasp_target_link(entity)
def get_grasp_target_pos(entity)
def get_grasp_target_distance(entity, points)
def _build_thumb_index_grasp_term(term)
def _thumb_index_positions(term)
def _expand_vec(values)
def _build_alignment_term(term)
def _compute_alignment_term(term)
def _get_rotation_axis(env)
def _get_entity_dof_names(entity)
def _resolve_spin_dof_index(entity)
def _get_explicit_screw_dof_state(env)
def get_screw_axis_state(env)
def screw_rotation_state_obs(env)
def screw_rotation_velocity_obs(env)
class ScrewObjTiltObs(ObservationTerm)
    """Off-axis tilt of the screwdriver as a single scalar (radians).

The angle between the object's local up axis (the shaft, rotated into the
world frame) and the world vertical -- i.e. how far the screwdriver has
fallen over. ``0`` means perfectly upright; larger means more tilted. This
is the privileg"""
    def __init__(self, env, options)
    def build(self)
    def compute(self)
class ScrewAxisRotationProgressObs(ObservationTerm)
    """Per-step rotation progress about the screwdriver's shaft (radians).

The signed angle the object rotated about ``local_axis`` -- an axis fixed in
the object's local frame -- since the previous step, mirroring the per-step
contribution of :func:`shared_terms.rotation_reward`. Positive means rotation
"""
    def __init__(self, env, options)
    def build(self)
    def reset(self, envs_idx)
    def compute(self)
def screw_total_rotation_metric(env)
def screw_rotation_reward(env)
def screw_angvel_penalty(env)
def screw_pc_z_dist_penalty(env)
def screw_object_dist_penalty(env)
class ScrewVerticalAlignmentPenalty(RewardTerm)
    """Penalize tilt of the object's ``local_up_axis`` away from ``world_up_axis``.

Parameters
----------
tilt_margin : float
    The angle in degrees beyond which the penalty starts to apply."""
    def build(self)
    def compute(self, envs_idx)
class ScrewSurfaceDistanceReward(RewardTerm)
    def build(self)
    def compute(self, envs_idx)
class ScrewPoseDiffPenalty(RewardTerm)
    def build(self)
    def reset(self, envs_idx)
    def compute(self, envs_idx)
class ScrewTorquePenalty(RewardTerm)
    def build(self)
    def compute(self, envs_idx)
class ScrewWorkPenalty(RewardTerm)
    def build(self)
    def reset(self, envs_idx)
    def compute(self, envs_idx)
class ScrewNutStagnation(TerminationTerm)
    def build(self)
    def compute(self)
class ScrewJointLimit(TerminationTerm)
    def build(self)
    def compute(self)
class ScrewHandleFall(TerminationTerm)
    def build(self)
    def compute(self)
class ScrewFingerDistance(TerminationTerm)
    def build(self)
    def compute(self)
class ScrewLowContactStagnation(TerminationTerm)
    def build(self)
    def compute(self)
def _resolve_link_index(link)

```python
def screw_rotation_reward(
    env: EnvBase,
    *,
    entity_name: str = "obj",
    link_name: str | None = None,
    command_name: str = "rotation_axis",
    angvel_clip_min: float = -4.0,
    angvel_clip_max: float = 4.0,
    rotation_sign: float = 1.0,
) -> torch.Tensor:
    _, screw_dof_vel = get_screw_axis_state(env, obj_name=entity_name, link_name=link_name, command_name=command_name)
    return torch.clip(rotation_sign * screw_dof_vel, min=angvel_clip_min, max=angvel_clip_max)
```
```

### dexterous-hands/src/utils.py

```
def get_asset_path(asset_name)
def get_entity_metadata(entity)
def get_entity_link_names(entity)
def resolve_entity_link(entity, link_name)
```

### rsl_rl/rsl_rl/env/__init__.py

```
"""Environment definition."""
```

### rsl_rl/rsl_rl/env/vec_env.py

```
class VecEnv(ABC)
    """Abstract class for a vectorized environment.

The vectorized environment is a collection of environments that are synchronized. This means that the same type of
action is applied to all environments and the same type of observation is returned from all environments."""
    def get_observations(self)
    def step(self, actions)

```python
def get_observations(self) -> TensorDict:
        """Return the current observations.

        Returns:
            The observations from the environment.
        """
        raise NotImplementedError
```
```

### rsl_rl/rsl_rl/runners/on_policy_runner.py

```
class OnPolicyRunner()
    """On-policy runner for reinforcement learning algorithms."""
    def __init__(self, env, train_cfg, log_dir, device)
    def learn(self, num_learning_iterations, init_at_random_ep_len)
    def save(self, path, infos)
    def load(self, path, load_cfg, strict, map_location)
    def get_inference_policy(self, device)
    def export_policy_to_jit(self, path, filename)
    def export_policy_to_onnx(self, path, filename, verbose)
    def add_git_repo_to_log(self, repo_file_path)
    def _configure_multi_gpu(self)
```