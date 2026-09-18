# bench2dex_2026

source: https://github.com/Bench2Dex/Bench2Dex


commit: 766d542d6a52609d37a4598d08f1c3cef657353c


## README

<p align="center">
  <img src="assets/logo.png" alt="Bench2Dex" width="720">
</p>

<p align="center">
  <strong>Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands</strong>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2609.15726">
  <img src="https://img.shields.io/badge/arXiv-2609.15726-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv">
  </a>
  <a href="https://bench2dex.github.io/">
    <img src="https://img.shields.io/badge/Project%20Page-Website-3B82F6?style=for-the-badge" alt="Project Page">
  </a>
  <a href="https://modelscope.cn/datasets/Bench2Dex">
    <img src="https://img.shields.io/badge/Dataset-ModelScope-6246EA?style=for-the-badge" alt="Dataset">
  </a>
  <a href="https://bench2dex.github.io/doc/">
    <img src="https://img.shields.io/badge/Documentation-Docs-10B981?style=for-the-badge" alt="Documentation">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tasks-26-F97316?style=flat-square" alt="26 tasks">
  <img src="https://img.shields.io/badge/Robot%20Embodiments-12-3B82F6?style=flat-square" alt="12 robot embodiments">
  <img src="https://img.shields.io/badge/Demonstrations-1.3K-8B5CF6?style=flat-square" alt="1.3K demonstrations">
  <img src="https://img.shields.io/badge/Data%20Modalities-8-10B981?style=flat-square" alt="8 data modalities">
</p>

<p align="center">
  Built on <a href="https://github.com/isaac-sim/IsaacLab">Isaac Lab</a> for multimodal data collection and systematic generalization evaluation across long-horizon manipulation tasks.
</p>

---

## 🎬 Overview

https://github.com/user-attachments/assets/f15a763d-bb88-4d02-a491-bf88689198fe

## 🛠️ Environment Installation

```bash
# Create and activate a fresh environment
conda create -n env_isaaclab python=3.11 -y
conda activate env_isaaclab
python -m pip install --upgrade pip

# Install Isaac Sim 5.1.0
python -m pip install "isaacsim[all,extscache]==5.1.0" \
  --extra-index-url https://pypi.nvidia.com

# Install the CUDA 12.8 builds of PyTorch
python -m pip install \
  torch==2.7.0 \
  torchvision==0.22.0 \
  --index-url https://download.pytorch.org/whl/cu128

# Install the remaining Bench2Dex Python packages
python -m pip install numpy==1.26.4 Flask h5py

# Clone Isaac Lab v2.3.2
git clone --branch v2.3.2 --depth 1 https://github.com/isaac-sim/IsaacLab.git

# Install Isaac Lab in editable mode
cd IsaacLab/source/isaaclab
python -m pip install -e .
```

## 📦 Download Assets and Checkpoints

Download the assets, teleoperation dataset, and pretrained policy checkpoints from ModelScope:

- Assets: [Bench2Dex assets](https://modelscope.cn/datasets/Bench2Dex/Bench2Dex)
- Dataset: [Bench2Dex teleoperation data](https://modelscope.cn/datasets/Bench2Dex/teleopdata)
- Pretrained weights: [Bench2Dex policy checkpoints](https://modelscope.cn/datasets/Bench2Dex/policy_ckpt)

```text
root_path/
├── Bench2Dex/             # Code
├── dex2bench_dataset/     # Assets (scenes, robot models, etc.)
├── teleopdata/            # Teleoperation dataset
└── policy_ckpt/           # Pretrained policy checkpoints
```



## 🧤 Teleoperation Data Collection

### Steps

1. **Open the streaming app on iPhone**: [Download link](https://drive.google.com/file/d/1PYm4ajw080JWVTRTitnRb_KGJq3ysYwJ/view?usp=sharing)

2. **Start the Manus glove SDK client** (reads glove data and writes to shared memory `/manus_hand_data`):
   ```bash
   cd dex2bench/teleop/manus_bin
   ./SDKClient_Linux.out 1
   ```

3. **Launch simulation + teleoperation + data collection** (`--collect-config` defaults to `configs/collect/default.yaml`):
   ```bash
   python main.py --teleop --collect --enable-generalization \
     --task scenes/<task>.yaml
   ```
   Scene, lighting, and background are automatically randomized between episodes (generalization).

4. **Put on the Manus gloves and get into position**

5. **Tap the "Start Streaming" button on the iPhone app** — glove data is streamed via shared memory to the `TeleopController`, then remapped to robot joint targets through DexPilot retargeting

6. **Use the three foot pedals to control recording** (USB foot switches, emulating keyboard keys):

   | Pedal | Key Mapping | Function |
   |-------|------------|----------|
   | Pedal 1 | PageDown | **Home** — robot returns to home position |
   | Pedal 2 | Home | **Start recording** — creates `episode_NNNNNN.hdf5` |
   | Pedal 3 | End | **Stop recording** — finalizes the current episode |

   Per-frame data recorded includes: `robot/qpos` (joint positions), `action/commanded` (teleop commands), multi-view camera RGB images (6 cameras), object poses, etc. The keyboard has an equivalent mapping (Numpad 1/2/3 correspond to Home/Start/Stop).

## 🔁 Replay

Raw teleoperation only records joint states and object poses. The **replay** step loads each episode, re-builds the scene, and replays the trajectory frame-by-frame to capture camera data and tactile.

```bash
python tools/replay/batch_replay.py \
    --origin-dir ../teleopdata/dataset/06_fruit_bowl_loading/origin-generalization-double \
    --replay-dir ../teleopdata/dataset/06_fruit_bowl_loading/replay-generalization-double \
    --enable-rgb --enable-tactile \
    --resample-groups background,table_surface,light,camera \
    --generalization-split seen \
    --headless
```

> **Note**: `--enable-depth` is currently disabled in practice because depth data is too storage-heavy. Pre-collected and replayed datasets are available for download from ModelScope (see the [Download section](#download-assets-and-checkpoints)).

## 🧹 Policy Data Preparation

Before training or adapting any policy, ensure that each HDF5 episode contains a valid `meta/homing_start_sim_step`. This explicit marker records the simulation step at which the operator starts the return-to-home motion; it is not inferred from the robot joint positions. During data preprocessing, locate the first frame whose `time/sim_step` is greater than or equal to this marker and truncate the episode before that frame, so the homing frame and all subsequent return-to-home motion are excluded from both training samples and normalization statistics. The provided ACT, Diffusion Policy, Pi0.5, and GR00T N1.5 pipelines follow this convention, and custom policy pipelines should apply the same cutoff.


## 🤖 Policy Usage

For environment setup, training, and evaluation guidance for all four supported policies, see the **Policy Usage** chapter in the [Bench2Dex Documentation](https://bench2dex.github.io/doc/).

## 🧩 Task Description

For a complete list of all 26 tasks with detailed descriptions grouped by robot embodiment, see the **Tasks** chapter in the [Bench2Dex Documentation](https://bench2dex.github.io/doc/).

## Community

We welcome researchers and developers interested in Bench2Dex to join our community for discussions on dexterous manipulation, teleoperation, visuo-tactile learning, and benchmark development.

We maintain a **Bench2Dex WeChat group** for community discussions.

For technical questions, bug reports, and feature requests, please use [GitHub Issues](https://github.com/Bench2Dex/Bench2Dex/issues).

<p align="center">
  <img src="assets/wechat.png" alt="Bench2Dex" width="200">
</p>

## 📝 Citation
```bibtex
@article{yang2026bench2dex,
  title={Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands},
  author={Yang, Zhenjie and Zhang, Yideng and Zhang, Dongjie and Jiang, Chenyu and Liu, Xianshuai and Li, Yufeng and Ge, Zuhao and Jiao, Xingyu and Zhang, Zheng and He, Kaiyu and Wang, He and Zhong, Yuwen and Deng, Yi and Jiang, Muyun and Huang, Xianliang and Su, Haisheng and Zhang, Donghang and Zhang, Jian and Yang, Xue and Li, Hongyang and Wu, Zuxuan and Jiang, Yu-Gang and Jia, Xiaosong and Yan, Junchi},
  journal={arXiv preprint arXiv:2609.15726},
  year={2026}
}
```

## 🙏 Acknowledgements

We thank the contributors to [Isaac Lab](https://github.com/isaac-sim/IsaacLab), [RoboTwin](https://github.com/robotwin-Platform/RoboTwin), [DexUMI](https://github.com/real-stanford/DexUMI), [ACT](https://github.com/tonyzhaozh/act), [Diffusion Policy](https://github.com/real-stanford/diffusion_policy), [OpenPI](https://github.com/Physical-Intelligence/openpi), and [Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) for their open-source contributions to robotics and dexterous manipulation research.

## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
benchmark/
  __init__.py
  conditions.py
  grasp_detector.py
  harness.py
  metric_tracker.py
  metrics.py
  results.py
  stage_tracker.py
  statistics.py
  tests/
    test_metric_semantics.py
    test_scene_metric_config.py
    test_task_12_success.py
  tool_tracker.py
build/
  __init__.py
  articulation_limits.py
  constants.py
  generalization.py
  geometry.py
  ghost_replay.py
  layout.py
  object_initial_state.py
  object_visuals.py
  scene_builder.py
  spawners.py
  table_geometry.py
collector/
  __init__.py
  box_labeler.py
  camera_geometry.py
  cameras.py
  config.py
  contact_sensor_reader.py
  data_collector.py
  episode_buffer.py
  hdf5_writer.py
  metrics_payload.py
  occupancy.py
  operator_input_provider.py
  state_reader.py
  success_tracker.py
  tacmap_configs.py
  tacmap_rig.py
  tacmap_sensor/
    __init__.py
    sharpa_tacmap_cfg.py
    sharpa_tacmap_vbts.py
    torch_jit_utils.py
  tactile.py
  task_manifest.py
configs/
  collect/
    bench_rich.yaml
    default.yaml
    tactile_rh56dfx.yaml
    teleop_record.yaml
    train_minimal.yaml
  scene/
    generalization.yaml
    no_generalization.yaml
main.py
policy/
  ACT/
    .gitignore
    LICENSE
    __init__.py
    act_policy.py
    conda_env.yaml
    deploy_policy.py
    deploy_policy.yml
    detr/
    env.sh
    eval.sh
    eval_direct.sh
    eval_double_env.sh
    imitate_episodes.py
    rq.txt
    train.sh
    utils.py
  ACT-Tactile/
    README.md
    __init__.py
    act/
    act_tactile_dataset.py
    act_tactile_model.py
    dataset.py
    deploy_policy.py
    eval_direct.sh
    offline_eval.py
    tactile_policy.py
    tactile_run_policy.py
    tests/
    train.py
    train.sh
  DP/
    .gitignore
    LICENSE
    __init__.py
    deploy_policy.py
    deploy_policy.yml
    diffusion_policy/
    dp_env.yml
    dp_model.py
    env.sh
    eval.sh
    eval_double_env.sh
    eval_tasks_seq.sh
    process_hdf5_to_zarr.py
    pyproject.toml
    train.py
    train.sh
  GR00T_XE/
    LICENSE
    README.md
    __init__.py
    convert_ee_trajectories.py
    dataset.py
    deploy_policy.py
    deploy_policy.yml
    embodiment_mapping.yml
    eval_double_env.sh
    finetune.py
    finetune.sh
    full_finetune.sh
    gr00t_hdf5_dataset.py
    ik_arm_converter.py
    offline_inference.py
    pretrain.py
    pretrain.sh
    pyproject.toml
    requirements.txt
    setup_env.sh
    src/
    xe_config.py
    xe_hand_mapping.py
    xe_norm_stats.json
    xe_norm_stats.py
  GR00T_n15/
    LICENSE
    README.md
    __init__.py
    convert_dex2bench_to_gr00t.py
    deploy_policy.py
    deploy_policy.yml
    eval.sh
    eval_double_env.sh
    eval_tasks_seq.sh
    gr00t_dex2bench_config.py
    gr00t_env.yml
    gr00t_hdf5_dataset.py
    pyproject.toml
    requirements.txt
    scripts/
    setup_env.sh
    src/
    train.sh
  GR00T_n15_Tactile/
    IMPLEMENTATION_PLAN.md
    LICENSE
    README.md
    __init__.py
    convert_dex2bench_to_gr00t.py
    deploy_policy.py
    deploy_policy.yml
    eval.sh
    eval_double_env.sh
    eval_tasks_seq.sh
    gr00t_dex2bench_config.py
    gr00t_env.yml
    gr00t_hdf5_dataset.py
    pyproject.toml
    requirements.txt
    run_policy.py
    scripts/
    setup_env.sh
    src/
    tactile_checkpoint.sh
    tactile_deployment.py
    tactile_eval_budget.py
    tactile_eval_client.py
    tactile_io.py
    tests/
    train.sh
  GR00T_n15_Tactile_Cross/
    IMPLEMENTATION_PLAN.md
    LICENSE
    README.md
    TACTILE_DESIGN_REVIEW.md
    __init__.py
    convert_dex2bench_to_gr00t.py
    deploy_policy.py
    deploy_policy.yml
    eval.sh
    eval_double_env.sh
    eval_tasks_seq.sh
    gr00t_dex2bench_config.py
    gr00t_env.yml
    gr00t_hdf5_dataset.py
    pyproject.toml
    requirements.txt
    run_policy.py
    scripts/
    setup_env.sh
    src/
    tactile_checkpoint.sh
    tactile_deployment.py
    tactile_eval_budget.py
    tactile_eval_client.py
    tactile_io.py
    tests/
    train.sh
  __init__.py
  loaders.py
  pi05/
    .gitignore
    .python-version
    LICENSE
    __init__.py
    deploy_policy.py
    deploy_policy.yml
    eval_all_channels.sh
    eval_double_env.sh
    finetune.sh
    packages/
    pi_model.py
    pyproject.toml
    scripts/
    src/
    uv.lock
  setup_policy_envs.sh
replay.py
requirements.txt
robots/
  __init__.py
  active_dof_maps.yml
  active_dof_utils.py
  gravity_compensation.py
  hand_friction.py
  joint_safety.py
  multi_iiwa7_with_sharpa.py
  multi_jaka_zu7_dexhand021_with_flange.py
  multi_panda_with_allegro.py
  multi_panda_with_orca.py
  multi_rm_65_with_revo2.py
  multi_ur5_rh56dfx_with_flange.py
  multi_ur5_rh5dg2_with_flange.py
  multi_ur5_schunk_hand_with_flange.py
  multi_ur5_shadow_hand_with_flange.py
  multi_ur5_wuji_with_flange.py
  multi_xarm7_with_ability.py
  multi_xarm7_with_leap.py
  placement.py
run_policy.py
scenes/
  03_wine_glass_plate_balance.yaml
  06_fruit_bowl_loading.yaml
  07_citrus_plate_loading.yaml
  08_frypan_stand_pour.yaml
  09_cleaner_moisturizer_box_loading.yaml
  12_screwdriver_box_and_hammer.yaml
  21_condiment_box_loading.yaml
  22_tool_box_loading.yaml
  24_stationery_category_sorting.yaml
  26_canned_food_tray_line_arrangement.yaml
  27_ball_box_loading.yaml
  32_baking_tray_prep_with_tools.yaml
  34_fridge_wine_interhand_pour.yaml
  42_trash_disposal.yaml
  43_fridge_fruit_shelf_sorting.yaml
  44_microwave_bowl_loading.yaml
  51_toilet_lid_cleaner_pour.yaml
  60_breadbasket_fast_food_loading.yaml
  61_medicine_shoebox_pack.yaml
  62_shoebox_accessory_pack.yaml
  64_sports_ball_cup_sort.yaml
  67_faucet_cup_water_fill.yaml
  73_jigsaw_puzzle_assembly.yaml
  76_soup_serving.yaml
  79_bimanual_piano_melody.yaml
  80_gaming_desk_setup.yaml
  86_short_jigsaw_puzzle.yaml
  task.md
script/
  __init__.py
  _append_eval_result.sh
  auto_eval.sh
  config_utils.py
  eval_budget.sh
  eval_policy_client.py
  eval_resume.py
  eval_tasks_seq.sh
  policy_model_server.py
  policy_rpc.py
  policy_sessions.py
success/
  __init__.py
  condition_evaluator.py
  condition_evaluator_reference.md
  custom/
    __init__.py
    task_03_wine_glass_plate_balance.py
    task_06_fruit_bowl_loading.py
    task_07_citrus_plate_loading.py
    task_08_frypan_stand_pour.py
    task_09_cleaner_moisturizer_box_loading.py
    task_12_screwdriver_box_and_hammer.py
    task_21_condiment_box_loading.py
    task_22_tool_box_loading.py
    task_24_stationery_category_sorting.py
    task_26_canned_food_tray_line_arrangement.py
    task_27_ball_box_loading.py
    task_32_baking_tray_prep_with_tools.py
    task_34_fridge_wine_interhand_pour.py
    task_42_trash_disposal.py
    task_43_fridge_fruit_shelf_sorting.py
    task_44_microwave_bowl_loading.py
    task_50_toy_repair.py
    task_51_toilet_lid_cleaner_pour.py
    task_56_glasses_lamp_pen_basket_organize.py
    task_57_block_hammer_drawer_storage.py
    task_58_coffee_machine_cup_spoon_brew.py
    task_59_living_rm_cleanup_chairs.py
    task_60_breadbasket_fast_food_loading.py
    task_61_medicine_shoebox_pack.py
    task_67_faucet_cup_water_fill.py
    task_73_jigsaw_puzzle_assembly.py
    task_76_soup_serving.py
    task_79_bimanual_piano_melody.py
    task_80_gaming_desk_setup.py
    task_86_short_jigsaw_puzzle.py
  engine.py
  state_utils.py
teleop/
  __init__.py
  arkit_wrist_reader.py
  arm_configs/
    iiwa7.yml
    jaka_zu7.yml
    panda_allegro.yml
    panda_orca.yml
    rm65_revo2.yml
    ur5.yml
    ur5_shadow.yml
    xarm7_ability.yml
    xarm7_leap.yml
  arm_ik_controller.py
  hand_cfgs/
    ability.yml
    allegro.yml
    dexhand021.yml
    leap.yml
    orca.yml
    revo2.yml
    rh56dfx.yml
    rh5dg2.yml
    schunk_svh.yml
    shadow.yml
    sharpa.yml
    wuji.yml
  isaaclab_bridge.py
  manus_bin/
    README.md
  manus_process.py
  math_utils.py
  retarget_bridge.py
  shm_reader.py
  teleop_controller.py
  tests/
    record_manus.py
tools/
  asset/
    convert_imported_assets_to_usd.py
    convert_urdf_cli.py
    convert_urdf_now.py
    extract_molmospaces.py
    fix_usd_paths.py
    fix_usd_sdf_linux_paths.py
    gen_tacmap_npy.py
    package_physx_task_objects.py
    rebuilt_tactile_mesh_to_npy_commands.md
    repair_digital_piano.py
    repair_digital_piano_source.py
    sdf_convert_file/
  audit_episode_seed_metadata.py
  audit_generalization_assets.py
  audit_joint_safety_assets.py
  audit_scene_articulations.py
  audit_wrist_camera_table_penetration.py
  batch_re_eval.py
  batch_replay_wrist.sh
  compute_robustness.py
  export/
    convert_bench2dex_to_lerobot_v3.py
    export_cameras_2k.py
    export_hdf5_to_json.py
    export_video.py
    export_videos.py
    extract_images_from_hdf5.py
  fix_resume_duplicates.py
  fix_task44_hdf5_object_id.py
  gen_rgb_augmented_episodes.py
  hdf5_episodes_to_mp4.py
  label_success.py
  labels/
    _accel.py
    _gpu_bbox.py
    _gpu_tsdf.py
    _gpu_voxelizer.py
    _label_common.py
    _mesh_voxelizer.py
    audit_scene_hdf5_name_drift.py
    generate_box_labels.py
    generate_gt_labels.py
    generate_occupancy_gt.py
    generate_occupancy_tsdf.py
    offline_generate.py
    rekey_anchor_placements.py
    rekey_task44_metrics_box3d.py
  merge_eval_chunks.py
  re_eval_task44.py
  recompute_stage.py
  replay/
    add_tactile_to_replay.sh
    batch_replay.py
    batch_replay.sh
    batch_screenshot_6d.py
    batch_screenshot_6d.sh
    recursive_replay.py
    replay_commanded.py
    replay_commanded_active_dof.py
    retarget_home.py
    screenshot_6d.py
    screenshot_6d_all.py
  rpc/
    __init__.py
    client.py
    policy_handle.py
    server.py
    wire.py
  run_benchmark.py
  sync_scene_config.py
  update_expert_time_step.py
  validate_release_assets.py
  verify_scene_config.py
  vis/
    dexpilot_vis.py
    episode_viewer/
    export_frame_views.py
    occupancy_3d_viewer.py
    plot_tactile_attention.py
    vis_tacmap_npy.py
    visualize_bbox.py
    visualize_episode_frame.py
    visualize_occupancy.py
    visualize_occupancy_semantic.py
    visualize_single_objpose.py
    visualize_tacmap_hdf5.py
utils/
  __init__.py
  episode_runtime.py
  episode_session.py
  inference_recorder.py
  isaac_rendering.py
  logging_config.py
  policy_timing.py
  replay_support.py
  runtime_helpers.py
  scene_paths.py
  seed_policy.py
  usd_prims.py
```

## Config files (47)


### configs/collect/bench_rich.yaml

```yaml
# Rich benchmark profile: RGB + depth + object pose + 3D/2D boxes
# Optimized for benchmarking and evaluation

profile:
  dataset_version: raw_hdf5_v2
  sensor_profile_id: bench_rich
  sensor_profile_version: "1.0"

dataset:
  format: hdf5_per_episode
  root: ./outputs
  name: dex2scene_dataset

capture:
  fps: 100
  step_stride: 5
  max_buffer_mb: 4096

modalities:
  rgb: true
  depth: true
  object_pose: true
  joint_state: true
  box3d: true
  box2d: true
  occupancy: false
  tactile: false

# Note: camera_list inherits from default config (do not set to empty)
```

### configs/collect/default.yaml

```yaml
﻿# Single source of truth for collection config.
# Raw default behavior:
# - occupancy: false
# - if you turn it on, the bundled occupancy config already uses chunked and bounded settings
#
# To switch to an online-label run, change:
#   modalities.occupancy: true
#
# To request denser occupancy, additionally tune:
#   occupancy.voxel_size
#   occupancy.bounds
#   occupancy.max_voxel_count

profile:
  dataset_version: bench_raw_v1
  sensor_profile_id: benchmark_raw
  sensor_profile_version: "1.0"

dataset:
  format: hdf5_per_episode
  root: ./outputs
  name: test

capture:
  fps: 20
  step_stride: 3
  max_buffer_mb: 8000

modalities:
  rgb: false
  depth: false
  object_pose: true
  joint_state: true
  box3d: false
  box2d: false
  tactile: false          


# Per-camera resolution override. [width, height], max 1920x1080.
camera_pixel:
  cam_chest: [640, 480]
  cam_overhead: [640, 480]
  cam_wrist_right: [640, 480]
  cam_wrist_left: [640, 480]
  cam_stereo_left: [640, 480]
  cam_stereo_right: [640, 480]

# cam_wist_right and cam_wrist_left are defined as robot_link mount type, but their parent_link and offset are defined in the robot_wrist_camera_profiles section. This is because the exact camera pose depends on the robot model, and we want to be able to easily switch between different robot models without having to redefine the camera parameters each time.
camera_list:
  - id: cam_chest
    mount_type: world
    position: [0.0, -0.40, 1.25]
    target: [0.0, 0.00, 0.82]
    width: 640
    height: 480
    focal_length: 18.0
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_overhead
    mount_type: world
    position: [0.0, 0.0, 1.80]
    target: [0.0, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 15.0
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_wrist_right
    mount_type: robot_link
    camera_type: fisheye
    fisheye_camera_matrix: [[169.7056, 0.0, 320.0], [0.0, 169.7056, 240.0], [0.0, 0.0, 1.0]]
    fisheye_distortion_coefficients: [-0.0416667, 0.0005208, -0.0000031, 0.0000000108]
    fisheye_max_fov_deg: 180.0
    parent_link: wrist_3_link
    offset_xyz: [0.052620712, 0.057382115, 0.075768000]
    offset_rpy: [-0.262750000, 0.084286000, 1.547360000]
    width: 640
    height: 480
    clipping_range: [0.01, 20.0]
  - id: cam_wrist_left
    mount_type: robot_link
    camera_type: fisheye
    fisheye_camera_matrix: [[169.7056, 0.0, 320.0], [0.0, 169.7056, 240.0], [0.0, 0.0, 1.0]]
    fisheye_distortion_coefficients: [-0.0416667, 0.0005208, -0.0000031, 0.0000000108]
    fisheye_max_fov_deg: 180.0
    parent_link: L_arm_wrist_3_link
    offset_xyz: [-0.052529389, 0.057465743, 0.075768174]
    offset_rpy: [0.261799551, 0.000000071, 1.569999956]
    width: 640
    height: 480
    clipping_range: [0.01, 20.0]
  # Stereo cameras (ZED 2) - 120mm baseline, 110°(H) FOV, 1920x1080
  # Note: z=1.5 to avoid being blocked by robot arms (arm max height ~1.2m)
  - id: cam_stereo_left
    mount_type: world
    position: [-0.06, -0.3, 1.50]
    target: [-0.06, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 7.34
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_stereo_right
    mount_type: world
    position: [0.06, -0.3, 1.50]
    target: [0.06, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 7.34
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]

robot_wrist_camera_profiles:
  multi_iiwa7_with_sharpa:
    cam_wrist_left:
      parent_link: link_7
      offset_xyz: [0.05, 0.05, 0.05]
      offset_rpy: [-0.1571, 0.314, -1.571]
    cam_wrist_right:
      parent_link: multi_link_7
      offset_xyz: [0.05, -0.05, 0.05]
      offset_rpy: [-0.1571, -0.314, -1.571]
  multi_jaka_zu7_dexhand021_with_flange:
    cam_wrist_left:
      parent_link: l_Link_6
      offset_xyz: [0.05, -0.05, 0.15]
      offset_rpy: [-0.314, 0.314, 3.14]
    cam_wrist_right:
      parent_link: Link_6
      offset_xyz: [-0.05, -0.05, 0.15]
      offset_rpy: [-0.314, -0.314, 3.14]

  multi_panda_with_orca:
    cam_wrist_left:
      parent_link: panda_link7
      offset_xyz: [-0.06, 0.05, 0.27]
      offset_rpy: [0.314, 0.1571, 0.785]
    cam_wrist_right:
      parent_link: multi_panda_link7
      offset_xyz: [-0.06, 0.05, 0.27]
      offset_rpy: [0.314, -0.1571, 0.785]
  multi_panda_with_allegro:
    cam_wrist_left:
      parent_link: panda_link7
      offset_xyz: [-0.060, 0.05, 0.1]
      offset_rpy: [0, 0.1571, 0.785]
    cam_wrist_right:
      parent_link: multi_panda_link7
      offset_xyz: [-0.06, 0.05, 0.1]
      offset_rpy: [0, -0.1571, 0.785]

  multi_rm_65_with_revo2:
    cam_wrist_left:
      parent_link: l_Link6
      offset_xyz: [0.06, 0.04, 0.01]
      offset_rpy: [0.1571, 0.314, -1.571]
    cam_wrist_right:
      parent_link: Link6
      offset_xyz: [0.06, -0.04, 0.01]
      offset_rpy: [0.1571, -0.314, -1.571]

  multi_ur5_rh56dfx_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.03, 0.07]
      offset_rpy: [-0.314, 0.314, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.03, 0.07]
      offset_rpy: [-0.314, -0.314, 0]
  multi_ur5_rh5dg2_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.04, 0.045, 0.05]
      offset_rpy: [-0.314, 0.314, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.04, 0.045, 0.05]
      offset_rpy: [-0.314, -0.314, 0]
  multi_ur5_schunk_hand_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.04, 0.06]
      offset_rpy: [-0.1571, 0.314, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.04, 0.06]
      offset_rpy: [-0.1571, -0.314, 0]
  multi_ur5_shadow_hand_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.08, 0.25]
      offset_rpy: [0, 0.314, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.08, 0.25]
      offset_rpy: [0, -0.314, 0]
  multi_ur5_wuji_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.03, 0.04, 0.07]
      offset_rpy: [-0.1571, 0.314, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.03, 0.04, 0.07]
      offset_rpy: [-0.1571, -0.314, 0]
  multi_xarm7_with_ability:
    cam_wrist_left:
      parent_link: xarm_l_link7
      offset_xyz: [-0.03, 0.05, 0.02]
      offset_rpy: [0, 0.314, 0.000]
    cam_wrist_right:
      parent_link: multi_xarm_r_link7
      offset_xyz: [0.03, 0.05, 0.02]
      offset_rpy: [0, -0.314, 0.000]
  multi_xarm7_with_leap:
    cam_wrist_left:
      parent_link: link7
      offset_xyz: [0.06, 0.04, 0]
      offset_rpy: [-0.1571, 0.314, -1.571]
    cam_wrist_right:
      parent_link: multi_link7
      offset_xyz: [0.06, -0.04, 0]
      offset_rpy: [-0.1571, -0.314, -1.571]

scene_background:
  enabled: true
  physics_enabled: false
  fill_light_intensity: 800
  fill_light_jitter_ratio: 0.0

  # type: hdr
  # uri: ../../../dex2bench_dataset/Background/Indoor/university_workshop_4k.hdr
  # yaw_deg: 120.0                                                                              

  # type: usd_scene
  # category: iTHOR
  # uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan1_physics/scene.usda
  # yaw_deg: 180
  # scene_offset: [0, 0, 0.0]
  # type: usd_scene
  # category: iTHOR
  # uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan2_physics/scene.usda
  # yaw_deg: 180
  # scene_offset: [0, 0, 0]
  # type: usd_scene
  # category: iTHOR
  # uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan3_physics/scene.usda
  # yaw_deg: 180
  # scene_offset: [0, 0, -0.22]
  # type: usd_scene
  # category: iTHOR
  # uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan4_physics/scene.usda
  # yaw_deg: 180
  # scene_offset: [-1.96702, 1.89762, 0]
  # type: usd_scene
  # category: iTHOR
  # uri: ../../../dex2bench_d
```

### configs/collect/tactile_rh56dfx.yaml

```yaml
modalities:
  tactile: true

```

### configs/collect/teleop_record.yaml

```yaml
# 遥操作录视频专用采集配置
# 启用 RGB 相机 + 关节状态，关闭 tactile（避免弹性体网格报错）
# 用法:
#   python main.py --task scenes/06_fruit_bowl_loading.yaml \
#     --teleop --collect --collect-config configs/collect/teleop_record.yaml \
#     --enable_cameras

profile:
  dataset_version: teleop_record_v1
  sensor_profile_id: teleop_record
  sensor_profile_version: "1.0"

dataset:
  format: hdf5_per_episode
  root: ./outputs
  name: teleop_record

capture:
  fps: 20
  step_stride: 5
  max_buffer_mb: 4096

modalities:
  rgb: true
  depth: false
  object_pose: true
  joint_state: true
  box3d: false
  box2d: false
  occupancy: false
  tactile: false          # 关闭 tactile，避免弹性体网格报错

# Per-camera resolution override. [width, height], max 1920x1080.
camera_pixel:
  cam_chest: [640, 480]
  cam_overhead: [640, 480]
  cam_wrist_right: [640, 480]
  cam_wrist_left: [640, 480]
  cam_stereo_left: [640, 480]
  cam_stereo_right: [640, 480]

# cam_wist_right and cam_wrist_left are defined as robot_link mount type, but their parent_link and offset are defined in the robot_wrist_camera_profiles section. This is because the exact camera pose depends on the robot model, and we want to be able to easily switch between different robot models without having to redefine the camera parameters each time.
camera_list:
  - id: cam_chest
    mount_type: world
    position: [0.0, -0.40, 1.25]
    target: [0.0, 0.00, 0.82]
    width: 640
    height: 480
    focal_length: 18.0
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_overhead
    mount_type: world
    position: [0.0, 0.0, 1.80]
    target: [0.0, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 15.0
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_wrist_right
    mount_type: robot_link
    camera_type: fisheye
    fisheye_camera_matrix: [[169.7056, 0.0, 320.0], [0.0, 169.7056, 240.0], [0.0, 0.0, 1.0]]
    fisheye_distortion_coefficients: [-0.0416667, 0.0005208, -0.0000031, 0.0000000108]
    fisheye_max_fov_deg: 180.0
    parent_link: wrist_3_link
    offset_xyz: [0.052620712, 0.057382115, 0.075768000]
    offset_rpy: [-0.262750000, 0.084286000, 1.547360000]
    width: 640
    height: 480
    clipping_range: [0.01, 5.0]
  - id: cam_wrist_left
    mount_type: robot_link
    camera_type: fisheye
    fisheye_camera_matrix: [[169.7056, 0.0, 320.0], [0.0, 169.7056, 240.0], [0.0, 0.0, 1.0]]
    fisheye_distortion_coefficients: [-0.0416667, 0.0005208, -0.0000031, 0.0000000108]
    fisheye_max_fov_deg: 180.0
    parent_link: L_arm_wrist_3_link
    offset_xyz: [-0.052529389, 0.057465743, 0.075768174]
    offset_rpy: [0.261799551, 0.000000071, 1.569999956]
    width: 640
    height: 480
    clipping_range: [0.01, 5.0]
  # Stereo cameras (ZED 2) - 120mm baseline, 110°(H) FOV, 1920x1080
  # Note: z=1.5 to avoid being blocked by robot arms (arm max height ~1.2m)
  - id: cam_stereo_left
    mount_type: world
    position: [-0.06, -0.3, 1.50]
    target: [-0.06, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 7.34
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]
  - id: cam_stereo_right
    mount_type: world
    position: [0.06, -0.3, 1.50]
    target: [0.06, 0.0, 0.82]
    width: 640
    height: 480
    focal_length: 7.34
    horizontal_aperture: 20.955
    clipping_range: [0.01, 20.0]

robot_wrist_camera_profiles:
  multi_iiwa7_with_sharpa:
    cam_wrist_left:
      parent_link: link_7
      offset_xyz: [0.1, 0.05, 0.05]   
      offset_rpy: [0.1571, 0.1571, -1.571]
    cam_wrist_right:
      parent_link: multi_link_7
      offset_xyz: [0.1, -0.05, 0.05]
      offset_rpy: [0.1571, -0.1571, -1.571]
  multi_jaka_zu7_dexhand021_with_flange:
    cam_wrist_left:
      parent_link: l_Link_6
      offset_xyz: [0.05, -0.140, 0.158]
      offset_rpy: [0.1571, 0.1571, 3.14]
    cam_wrist_right:
      parent_link: Link_6
      offset_xyz: [-0.05, -0.140, 0.158]
      offset_rpy: [0.1571, -0.1571, 3.14]

  multi_panda_with_orca:
    cam_wrist_left:
      parent_link: panda_link7
      offset_xyz: [-0.070, 0.078, 0.25]
      offset_rpy: [0.1571, 0.1571, 0.785]
    cam_wrist_right:
      parent_link: multi_panda_link7
      offset_xyz: [-0.070, 0.078, 0.25]
      offset_rpy: [0.1571, -0.1571, 0.785]

  multi_panda_with_allegro:
    cam_wrist_left:
      parent_link: panda_link7
      offset_xyz: [-0.070, 0.078, 0.082]
      offset_rpy: [0.1571, 0.1571, 0.785]
    cam_wrist_right:
      parent_link: multi_panda_link7
      offset_xyz: [-0.070, 0.078, 0.082]
      offset_rpy: [0.1571, -0.1571, 0.785]

  multi_rm_65_with_revo2:
    cam_wrist_left:
      parent_link: l_Link6
      offset_xyz: [0.06, 0.04, 0.01]
      offset_rpy: [0.1571, 0.1571, -1.571]
    cam_wrist_right:
      parent_link: Link6
      offset_xyz: [0.06, -0.04, 0.01]
      offset_rpy: [0.1571, -0.1571, -1.571]

  multi_xarm7_with_ability:
    cam_wrist_left:
      parent_link: xarm_l_link7
      offset_xyz: [-0.05, 0.1, 0.02]
      offset_rpy: [0.1571, 0.1571, 0.000]
    cam_wrist_right:
      parent_link: multi_xarm_r_link7
      offset_xyz: [0.05, 0.1, 0.02]
      offset_rpy: [0.1571, -0.1571, 0.000]

  multi_xarm7_with_leap:
    cam_wrist_left:
      parent_link: link7
      offset_xyz: [0.1,0.05, 0]
      offset_rpy: [0.1571, 0.1571, -1.571]
    cam_wrist_right:
      parent_link: multi_link7
      offset_xyz: [0.1, -0.05, 0]
      offset_rpy: [0.1571, -0.1571, -1.571]

  multi_ur5_rh5dg2_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.1, 0.06]
      offset_rpy: [0.1571, 0.1571, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.1, 0.06]
      offset_rpy: [0.1571, -0.1571, 0]

  multi_ur5_rh56dfx_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.052529389, 0.057465743, 0.075768174]
      offset_rpy: [0.261799551, 0.000000071, 1.569999956]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.052620712, 0.057382115, 0.075768000]
      offset_rpy: [-0.262750000, 0.084286000, 1.547360000]
  multi_ur5_shadow_hand_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.13, 0.25]
      offset_rpy: [0.1571, 0.1571, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.13, 0.25]
      offset_rpy: [0.1571, -0.1571, 0]

  multi_ur5_schunk_hand_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.1, 0.06]
      offset_rpy: [0.1571, 0.1571, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.1, 0.06]
      offset_rpy: [0.1571, -0.1571, 0]
  multi_ur5_wuji_with_flange:
    cam_wrist_left:
      parent_link: L_arm_wrist_3_link
      offset_xyz: [-0.05, 0.1, 0.06]
      offset_rpy: [0.1571, 0.1571, 0]
    cam_wrist_right:
      parent_link: wrist_3_link
      offset_xyz: [0.05, 0.1, 0.06]
      offset_rpy: [0.1571, -0.1571, 0]


scene_background:
  enabled: true
  physics_enabled: false
  fill_light_intensity: 800
  fill_light_jitter_ratio: 0.0

  type: usd_scene
  category: iTHOR
  uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan1_physics/scene.usda
  yaw_deg: 180
  scene_offset: [0, 0, 0.0]

```

### configs/collect/train_minimal.yaml

```yaml
# Minimal training profile: RGB + joint state only
# Optimized for policy training with small data size

profile:
  dataset_version: raw_hdf5_v2
  sensor_profile_id: train_minimal
  sensor_profile_version: "1.0"

dataset:
  format: hdf5_per_episode
  root: ./outputs
  name: dex2scene_dataset

capture:
  fps: 100
  step_stride: 5
  max_buffer_mb: 2048

modalities:
  rgb: true
  depth: false
  object_pose: false
  joint_state: true
  box3d: false
  box2d: false
  occupancy: false
  tactile: false

# Note: camera_list inherits from default config (do not set to empty)
```

### configs/scene/generalization.yaml

```yaml
asset_split: seen

appearance:
  background:
    enabled: true
    clean_background_rate: 0.0
    intensity: 1500.0
    yaw_deg: 0.0
    random_flip_180_rate: 0.0
    physics_enabled: false
    split_ratios:
      seen: 0.8
      unseen: 0.2
    ordered_ithor_seen_count: 50
    enabled_categories:
      usd_scene: [iTHOR]
      # image: [Indoor, Nature, Night, Outdoor, Skies, Studio, Sunrise_Sunset, Urban]
    assets:
      - kind: image
        category: Indoor
        uri: ../../../dex2bench_dataset/Background/Indoor/brown_photostudio_02_4k.hdr
      - kind: image
        category: Indoor
        uri: ../../../dex2bench_dataset/Background/Indoor/university_workshop_4k.hdr
      - kind: image
        category: Nature
        uri: ../../../dex2bench_dataset/Background/Nature/lakeside_sunrise_4k.hdr
      - kind: image
        category: Nature
        uri: ../../../dex2bench_dataset/Background/Nature/passendorf_snow_4k.hdr
      - kind: image
        category: Night
        uri: ../../../dex2bench_dataset/Background/Night/moonlit_golf_4k.hdr
      - kind: image
        category: Night
        uri: ../../../dex2bench_dataset/Background/Night/rogland_clear_night_4k.hdr
      - kind: image
        category: Outdoor
        uri: ../../../dex2bench_dataset/Background/Outdoor/suburban_soccer_park_4k.hdr
      - kind: image
        category: Outdoor
        uri: ../../../dex2bench_dataset/Background/Outdoor/sunny_country_road_4k.hdr
      - kind: image
        category: Skies
        uri: ../../../dex2bench_dataset/Background/Skies/citrus_orchard_road_puresky_4k.hdr
      - kind: image
        category: Skies
        uri: ../../../dex2bench_dataset/Background/Skies/mud_road_puresky_4k.hdr
      - kind: image
        category: Studio
        uri: ../../../dex2bench_dataset/Background/Studio/pav_studio_02_4k.hdr
      - kind: image
        category: Studio
        uri: ../../../dex2bench_dataset/Background/Studio/wooden_studio_09_4k.hdr
      - kind: image
        category: Sunrise_Sunset
        uri: ../../../dex2bench_dataset/Background/Sunrise_Sunset/grasslands_sunset_4k.hdr
      - kind: image
        category: Sunrise_Sunset
        uri: ../../../dex2bench_dataset/Background/Sunrise_Sunset/umhlanga_sunrise_4k.hdr
      - kind: image
        category: Urban
        uri: ../../../dex2bench_dataset/Background/Urban/furstenstein_4k.hdr
      - kind: image
        category: Urban
        uri: ../../../dex2bench_dataset/Background/Urban/modern_evening_street_4k.hdr
      # ---- iTHOR USD scenes (57) ----
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan2_physics/scene.usda
        yaw_deg: 180
        scene_offset: [0, 0, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan3_physics/scene.usda
        yaw_deg: 180
        scene_offset: [0, 0, -0.22]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan4_physics/scene.usda
        yaw_deg: 180
        scene_offset: [-1.96702, 1.89762, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan5_physics/scene.usda
        yaw_deg: 180
        scene_offset: [1.42053, 1.15041, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan6_physics/scene.usda
        yaw_deg: 180
        scene_offset: [-0.32854, 1.16282, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan8_physics/scene.usda
        yaw_deg: 180
        scene_offset: [-0.58339, 2.01355, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan9_physics/scene.usda
        yaw_deg: 90.0
        scene_offset: [0, 1.21873, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan11_physics/scene.usda
        yaw_deg: 180.0
        scene_offset: [-1.5588, 0.22708, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan14_physics/scene.usda
        yaw_deg: 90
        scene_offset: [0.8, 1.11, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan13_physics/scene.usda
        yaw_deg: -90.0
        scene_offset: [-3.8804, -2.13417, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan15_physics/scene.usda
        yaw_deg: 0
        scene_offset: [1.39, -1.58, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan16_physics/scene.usda
        yaw_deg: 180
        scene_offset: [1.25263, 3.65209, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan17_physics/scene.usda
        yaw_deg: 180.0
        scene_offset: [0.63808, 2.86054, 0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan18_physics/scene.usda
        yaw_deg: 90.0
        scene_offset: [2.71921, 0.57477, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan21_physics/scene.usda
        yaw_deg: 0
        scene_offset: [1.18080, 3.07023, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan24_physics/scene.usda
        yaw_deg: 0
        scene_offset: [0.95853, -1.48004, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan26_physics/scene.usda
        yaw_deg: 90.0
        scene_offset: [2.77407, 2.48283, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan201_physics/scene.usda
        yaw_deg: 0
        scene_offset: [2.16777, -1.20934, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan202_physics/scene.usda
        yaw_deg: 0
        scene_offset: [2.10875, -2.29375, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan204_physics/scene.usda
        yaw_deg: -90
        scene_offset: [-4.22613, -1.90774, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan205_physics/scene.usda
        yaw_deg: 180
        scene_offset: [-2.00438, 5.05686, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan206_physics/scene.usda
        yaw_deg: 0
        scene_offset: [0, 1.02099, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan208_physics/scene.usda
        yaw_deg: 0
        scene_offset: [0, 0, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan209_physics/scene.usda
        yaw_deg: -90.0
        scene_offset: [2.47887, -2.52504, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan210_physics/scene.usda
        yaw_deg: 180.0
        scene_offset: [-2.39328, 2.39618, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan211_physics/scene.usda
        yaw_deg: 0
        scene_offset: [0, 0, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan212_physics/scene.usda
        yaw_deg: 0
        scene_offset: [-0.97986, -0.25227, 0.0]
      - kind: usd_scene
        category: iTHOR
        uri: ../../../dex2bench_dataset/scenes/ithor/FloorPlan214_physics/scene.usda
        yaw_deg: -90.0
        scene
```

### configs/scene/no_generalization.yaml

```yaml
asset_split: seen
appearance:
  background:
    enabled: false
    assets: []
  table_surface:
    enabled: false
    assets: []
  light:
    enabled: false
spatial:
  object_pose:
    enabled: false
  table_height:
    enabled: false
  camera:
    enabled: false
    cameras: {}
clutter:
  tabletop:
    enabled: false
    asset_pool: []
embodiment:
  robot_asset:
    enabled: false

```

### policy/ACT/conda_env.yaml

```yaml
name: act
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - pip=23.0.1
  - pytorch=2.0.0
  - torchvision=0.15.0
  - pytorch-cuda=11.8
  - pyquaternion=0.9.9
  - pyyaml=6.0
  - rospkg=1.5.0
  - pexpect=4.8.0
  - mujoco=2.3.3
  - dm_control=1.0.9
  - matplotlib=3.7.1
  - einops=0.6.0
  - packaging=23.0
  - h5py=3.8.0
  - ipython=8.12.0
  - pip:
    - opencv-python==4.7.0.72  
```

### policy/ACT/deploy_policy.yml

```yaml
# ACT deploy config — kept minimal. Everything else is auto-detected or passed via CLI.
task_name: null
policy_name: ACT
host: 127.0.0.1
port: 9000
seed: 100000000

# ACT-specific arguments
# action_dim / state_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=54, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=32, full=46)
#   multi_panda_with_orca                    (active=40, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=56, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=40, full=46)

# Auto-detected from ckpt_dir — override only if auto-detection fails
robot_key: null
use_active_dof: true

# ACT architecture (loaded from checkpoint, listed for reference)
kl_weight: 10.0
chunk_size: 30
hidden_dim: 512
dim_feedforward: 3200
temporal_agg: false
device: cuda:0
ckpt_dir: null
ckpt_name: policy_best.ckpt

# Model backbone params (must match training — DETR parser requires these)
backbone: resnet18
position_embedding: sine
enc_layers: 4
dec_layers: 7
nheads: 8
dropout: 0.1
pre_norm: false
lr_backbone: 0.00001
lr: 0.00001
weight_decay: 0.0001
masks: false
dilation: false

# Camera config
camera_names:
  - cam_right_wrist
  - cam_left_wrist
  - cam_stereo_left
  - cam_stereo_right

```

### policy/ACT-Tactile/act/conda_env.yaml

```yaml
name: act
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - pip=23.0.1
  - pytorch=2.0.0
  - torchvision=0.15.0
  - pytorch-cuda=11.8
  - pyquaternion=0.9.9
  - pyyaml=6.0
  - rospkg=1.5.0
  - pexpect=4.8.0
  - mujoco=2.3.3
  - dm_control=1.0.9
  - matplotlib=3.7.1
  - einops=0.6.0
  - packaging=23.0
  - h5py=3.8.0
  - ipython=8.12.0
  - pip:
    - opencv-python==4.7.0.72

```

### policy/ACT-Tactile/act/deploy_policy.yml

```yaml
# ACT deploy config — kept minimal. Everything else is auto-detected or passed via CLI.
task_name: null
policy_name: ACT
host: 127.0.0.1
port: 9000
seed: 100000000

# ACT-specific arguments
# action_dim / state_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=54, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=32, full=46)
#   multi_panda_with_orca                    (active=40, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=56, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=40, full=46)

# Auto-detected from ckpt_dir — override only if auto-detection fails
robot_key: null
use_active_dof: true

# ACT architecture (loaded from checkpoint, listed for reference)
kl_weight: 10.0
chunk_size: 30
hidden_dim: 512
dim_feedforward: 3200
temporal_agg: false
device: cuda:0
ckpt_dir: null
ckpt_name: policy_best.ckpt

# Model backbone params (must match training — DETR parser requires these)
backbone: resnet18
position_embedding: sine
enc_layers: 4
dec_layers: 7
nheads: 8
dropout: 0.1
pre_norm: false
lr_backbone: 0.00001
lr: 0.00001
weight_decay: 0.0001
masks: false
dilation: false

# Camera config
camera_names:
  - cam_right_wrist
  - cam_left_wrist
  - cam_stereo_left
  - cam_stereo_right

```

### policy/DP/deploy_policy.yml

```yaml
# DP dex2scene deployment defaults.
policy_name: DP
task_name: 42_trash_disposal
task_config: replay-generalization
seed: 100000000
instruction_type: unseen
host: 127.0.0.1
port: 9000
episode_steps: 800
warmup_steps: 60
num_episodes: 0

checkpoint_path: null
training_config_path: ./policy/DP/diffusion_policy/config/robot_dp_36_dex2scene_pretrained.yaml
# action_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=58, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=46, full=46)
#   multi_panda_with_orca                    (active=48, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=60, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=46, full=46)
robot_key: multi_ur5_schunk_hand_with_flange
use_active_dof: true
device: cuda:0

camera_names:
  - right_cam
  - left_cam
  - stereo_left_cam
  - stereo_right_cam

```

### policy/DP/diffusion_policy/config/robot_dp_36_dex2scene.yaml

```yaml
defaults:
  - _self_

name: robot_${task.name}
_target_: diffusion_policy.workspace.robotworkspace.RobotWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "dex2scene"

horizon: 8
n_obs_steps: 3
n_action_steps: 6
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy
  shape_meta: ${shape_meta}

  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small
    clip_sample: True
    prediction_type: epsilon

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: null
    resize_shape: null
    crop_shape: null
    random_crop: True
    use_group_norm: True
    share_rgb_model: False
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  diffusion_step_embed_dim: 128
  down_dims: [256, 512, 1024]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  multi_gpu: false
  local_rank: 0
  rank: 0
  world_size: 1
  global_batch_size: null
  debug: False
  resume: True
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  use_ema: True
  freeze_encoder: False
  rollout_every: 50
  checkpoint_every: 5
  val_every: 1
  sample_every: 5
  disable_train_sampling: True
  log_every_steps: 20
  max_train_steps: null
  max_val_steps: null
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

task:
  name: 42_trash_disposal
  image_shape: [3, 480, 640]
  robot_key: multi_ur5_rh56dfx_with_flange
  use_active_dof: true
  action_dim: 24
  shape_meta:
    obs:
      right_cam:
        shape: [3, 480, 640]
        type: rgb
      left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_right_cam:
        shape: [3, 480, 640]
        type: rgb
      agent_pos:
        shape:
          - ${task.action_dim}
        type: low_dim
    action:
      shape:
        - ${task.action_dim}
  dataset:
    # -- HDF5 dataset (on-the-fly JPEG decode, slow) --
    # _target_: diffusion_policy.dataset.dex2scene_hdf5_dataset.Dex2SceneHdf5Dataset
    # dataset_dir: ../teleopdata_and_ckpt/dataset/42_trash_disposal/replay-generalization
    # batch_size: ${dataloader.batch_size}
    # horizon: ${horizon}
    # pad_before: ${eval:'${n_obs_steps}-1'}
    # pad_after: ${eval:'${n_action_steps}-1'}
    # seed: 42
    # val_ratio: 0.0
    # max_train_episodes: null
    # image_shape: ${task.image_shape}
    # use_active_dof: ${task.use_active_dof}
    # robot_key: ${task.robot_key}
    # n_obs_steps: ${n_obs_steps}

    # -- Zarr dataset (preprocessed, no decode overhead) --
    _target_: diffusion_policy.dataset.dex2scene_zarr_dataset.Dex2SceneZarrDataset
    zarr_path: ???   # override via CLI: task.dataset.zarr_path=/path/to/output.zarr
    batch_size: ${dataloader.batch_size}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    pad_before: ${eval:'${n_obs_steps}-1'}
    pad_after: ${eval:'${n_action_steps}-1'}
    seed: 42
    val_ratio: 0.0
    max_train_episodes: null

```

### policy/DP/diffusion_policy/config/robot_dp_36_dex2scene_pretrained.yaml

```yaml
defaults:
  - _self_

name: robot_${task.name}
_target_: diffusion_policy.workspace.robotworkspace.RobotWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "dex2scene"

horizon: 8
n_obs_steps: 3
n_action_steps: 6
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy
  shape_meta: ${shape_meta}

  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small
    clip_sample: True
    prediction_type: epsilon

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: IMAGENET1K_V1
    resize_shape: [256, 256]
    crop_shape: [224, 224]
    random_crop: False
    use_group_norm: False
    share_rgb_model: True
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  diffusion_step_embed_dim: 128
  down_dims: [256, 512, 1024]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  multi_gpu: false
  local_rank: 0
  rank: 0
  world_size: 1
  global_batch_size: null
  debug: False
  resume: True
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  use_ema: True
  freeze_encoder: True
  rollout_every: 50
  checkpoint_every: 5
  val_every: 1
  sample_every: 5
  disable_train_sampling: True
  log_every_steps: 20
  max_train_steps: null
  max_val_steps: null
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

task:
  name: 42_trash_disposal
  image_shape: [3, 480, 640]
  robot_key: multi_ur5_rh56dfx_with_flange
  use_active_dof: true
  action_dim: 24
  shape_meta:
    obs:
      right_cam:
        shape: [3, 480, 640]
        type: rgb
      left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_right_cam:
        shape: [3, 480, 640]
        type: rgb
      agent_pos:
        shape:
          - ${task.action_dim}
        type: low_dim
    action:
      shape:
        - ${task.action_dim}
  dataset:
    # -- HDF5 dataset (on-the-fly JPEG decode, slow) --
    # _target_: diffusion_policy.dataset.dex2scene_hdf5_dataset.Dex2SceneHdf5Dataset
    # dataset_dir: ../teleopdata_and_ckpt/dataset/42_trash_disposal/replay-generalization
    # batch_size: ${dataloader.batch_size}
    # horizon: ${horizon}
    # pad_before: ${eval:'${n_obs_steps}-1'}
    # pad_after: ${eval:'${n_action_steps}-1'}
    # seed: 42
    # val_ratio: 0.0
    # max_train_episodes: null
    # image_shape: ${task.image_shape}
    # use_active_dof: ${task.use_active_dof}
    # robot_key: ${task.robot_key}
    # n_obs_steps: ${n_obs_steps}

    # -- Zarr dataset (preprocessed, no decode overhead) --
    _target_: diffusion_policy.dataset.dex2scene_zarr_dataset.Dex2SceneZarrDataset
    zarr_path: ???   # override via CLI: task.dataset.zarr_path=/path/to/output.zarr
    batch_size: ${dataloader.batch_size}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    pad_before: ${eval:'${n_obs_steps}-1'}
    pad_after: ${eval:'${n_action_steps}-1'}
    seed: 42
    val_ratio: 0.0
    max_train_episodes: null

```

### policy/DP/diffusion_policy/config/robot_dp_36_dex2scene_real.yaml

```yaml
defaults:
  - _self_

name: robot_${task.name}
_target_: diffusion_policy.workspace.robotworkspace.RobotWorkspace

task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: "dex2scene"

horizon: 8
n_obs_steps: 3
n_action_steps: 6
n_latency_steps: 0
dataset_obs_steps: ${n_obs_steps}
past_action_visible: False
keypoint_visible_rate: 1.0
obs_as_global_cond: True

policy:
  _target_: diffusion_policy.policy.diffusion_unet_image_policy.DiffusionUnetImagePolicy
  shape_meta: ${shape_meta}

  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddpm.DDPMScheduler
    num_train_timesteps: 100
    beta_start: 0.0001
    beta_end: 0.02
    beta_schedule: squaredcos_cap_v2
    variance_type: fixed_small
    clip_sample: True
    prediction_type: epsilon

  obs_encoder:
    _target_: diffusion_policy.model.vision.multi_image_obs_encoder.MultiImageObsEncoder
    shape_meta: ${shape_meta}
    rgb_model:
      _target_: diffusion_policy.model.vision.model_getter.get_resnet
      name: resnet18
      weights: null
    resize_shape: [216, 288]
    crop_shape: null
    random_crop: False
    use_group_norm: True
    share_rgb_model: False
    imagenet_norm: True

  horizon: ${horizon}
  n_action_steps: ${eval:'${n_action_steps}+${n_latency_steps}'}
  n_obs_steps: ${n_obs_steps}
  num_inference_steps: 100
  obs_as_global_cond: ${obs_as_global_cond}
  diffusion_step_embed_dim: 128
  down_dims: [256, 512, 1024]
  kernel_size: 5
  n_groups: 8
  cond_predict_scale: True

ema:
  _target_: diffusion_policy.model.diffusion.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: True
  pin_memory: True
  persistent_workers: False

val_dataloader:
  batch_size: 8
  num_workers: 0
  shuffle: False
  pin_memory: True
  persistent_workers: False

optimizer:
  _target_: torch.optim.AdamW
  lr: 1.0e-4
  betas: [0.95, 0.999]
  eps: 1.0e-8
  weight_decay: 1.0e-6

training:
  device: "cuda:0"
  seed: 42
  multi_gpu: false
  local_rank: 0
  rank: 0
  world_size: 1
  global_batch_size: null
  debug: False
  resume: True
  lr_scheduler: cosine
  lr_warmup_steps: 500
  num_epochs: 600
  gradient_accumulate_every: 1
  use_ema: True
  freeze_encoder: False
  rollout_every: 50
  checkpoint_every: 5
  val_every: 1
  sample_every: 5
  disable_train_sampling: True
  log_every_steps: 20
  max_train_steps: null
  max_val_steps: null
  tqdm_interval_sec: 1.0

logging:
  project: diffusion_policy_debug
  resume: True
  mode: online
  name: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}
  tags: ["${name}", "${task_name}", "${exp_name}"]
  id: null
  group: null

checkpoint:
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 5
    format_str: 'epoch={epoch:04d}-test_mean_score={test_mean_score:.3f}.ckpt'
  save_last_ckpt: True
  save_last_snapshot: False

multi_run:
  run_dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  wandb_name_base: ${now:%Y.%m.%d-%H.%M.%S}_${name}_${task_name}

hydra:
  job:
    override_dirname: ${name}
  run:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
  sweep:
    dir: data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}
    subdir: ${hydra.job.num}

task:
  name: 42_trash_disposal
  image_shape: [3, 480, 640]
  robot_key: multi_ur5_rh56dfx_with_flange
  use_active_dof: true
  action_dim: 24
  shape_meta:
    obs:
      right_cam:
        shape: [3, 480, 640]
        type: rgb
      left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_left_cam:
        shape: [3, 480, 640]
        type: rgb
      stereo_right_cam:
        shape: [3, 480, 640]
        type: rgb
      agent_pos:
        shape:
          - ${task.action_dim}
        type: low_dim
    action:
      shape:
        - ${task.action_dim}
  dataset:
    # -- HDF5 dataset (on-the-fly JPEG decode, slow) --
    # _target_: diffusion_policy.dataset.dex2scene_hdf5_dataset.Dex2SceneHdf5Dataset
    # dataset_dir: ../teleopdata_and_ckpt/dataset/42_trash_disposal/replay-generalization
    # batch_size: ${dataloader.batch_size}
    # horizon: ${horizon}
    # pad_before: ${eval:'${n_obs_steps}-1'}
    # pad_after: ${eval:'${n_action_steps}-1'}
    # seed: 42
    # val_ratio: 0.0
    # max_train_episodes: null
    # image_shape: ${task.image_shape}
    # use_active_dof: ${task.use_active_dof}
    # robot_key: ${task.robot_key}
    # n_obs_steps: ${n_obs_steps}

    # -- Zarr dataset (preprocessed, no decode overhead) --
    _target_: diffusion_policy.dataset.dex2scene_zarr_dataset.Dex2SceneZarrDataset
    zarr_path: ???   # override via CLI: task.dataset.zarr_path=/path/to/output.zarr
    batch_size: ${dataloader.batch_size}
    horizon: ${horizon}
    n_obs_steps: ${n_obs_steps}
    pad_before: ${eval:'${n_obs_steps}-1'}
    pad_after: ${eval:'${n_action_steps}-1'}
    seed: 42
    val_ratio: 0.0
    max_train_episodes: null

```

### policy/DP/dp_env.yml

```yaml
name: dp
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - ca-certificates=2025.1.31
  - ld_impl_linux-64=2.40
  - libffi=3.3
  - libgcc=14.2.0
  - libgcc-ng=14.2.0
  - libgomp=14.2.0
  - libsqlite=3.46.0
  - libstdcxx=14.2.0
  - libstdcxx-ng=14.2.0
  - libzlib=1.2.13
  - ncurses=6.5
  - openssl=1.1.1w
  - pip=25.2
  - python=3.9.0
  - readline=8.2
  - setuptools=80.9.0
  - sqlite=3.46.0
  - tk=8.6.13
  - wheel=0.45.1
  - xz=5.2.6
  - zlib=1.2.13
  - pip:
    - annotated-doc==0.0.4
    - annotated-types==0.7.0
    - antlr4-python3-runtime==4.9.3
    - anyio==4.12.1
    - asciitree==0.3.3
    - certifi==2026.5.20
    - charset-normalizer==3.4.7
    - click==8.1.8
    - diffusers==0.36.0
    - diffusion-policy==0.1.0
    - dill==0.3.5.1
    - einops==0.8.2
    - eval-type-backport==0.4.0
    - exceptiongroup==1.3.1
    - fasteners==0.20
    - filelock==3.19.1
    - fsspec==2025.10.0
    - gitdb==4.0.12
    - gitpython==3.1.50
    - h11==0.16.0
    - h5py==3.14.0
    - hf-xet==1.5.0
    - httpcore==1.0.9
    - httpx==0.28.1
    - huggingface-hub==1.8.0
    - hydra-core==1.2.0
    - idna==3.16
    - importlib-metadata==7.1.0
    - jinja2==3.1.6
    - llvmlite==0.43.0
    - markdown-it-py==3.0.0
    - markupsafe==3.0.2
    - mdurl==0.1.2
    - mpmath==1.3.0
    - networkx==3.2.1
    - numba==0.60.0
    - numcodecs==0.12.1
    - numpy==2.0.2
    - nvidia-cublas-cu12==12.8.4.1
    - nvidia-cuda-cupti-cu12==12.8.90
    - nvidia-cuda-nvrtc-cu12==12.8.93
    - nvidia-cuda-runtime-cu12==12.8.90
    - nvidia-cudnn-cu12==9.10.2.21
    - nvidia-cufft-cu12==11.3.3.83
    - nvidia-cufile-cu12==1.13.1.3
    - nvidia-curand-cu12==10.3.9.90
    - nvidia-cusolver-cu12==11.7.3.90
    - nvidia-cusparse-cu12==12.5.8.93
    - nvidia-cusparselt-cu12==0.7.1
    - nvidia-nccl-cu12==2.27.3
    - nvidia-nvjitlink-cu12==12.8.93
    - nvidia-nvtx-cu12==12.8.90
    - omegaconf==2.3.0
    - packaging==26.2
    - pandas==2.3.3
    - pillow==11.3.0
    - platformdirs==4.4.0
    - protobuf==6.33.6
    - pydantic==2.13.4
    - pydantic-core==2.46.4
    - pygments==2.20.0
    - python-dateutil==2.9.0.post0
    - pytz==2026.2
    - pyyaml==6.0.3
    - regex==2026.1.15
    - requests==2.32.5
    - rich==15.0.0
    - ruamel-yaml==0.19.1
    - safetensors==0.7.0
    - sentry-sdk==2.64.0
    - shellingham==1.5.4
    - six==1.17.0
    - smmap==5.0.3
    - sympy==1.14.0
    - torch==2.8.0+cu128
    - torchvision==0.23.0+cu128
    - tqdm==4.67.3
    - triton==3.4.0
    - typer==0.23.2
    - typing-extensions==4.15.0
    - typing-inspection==0.4.2
    - tzdata==2026.2
    - urllib3==2.6.3
    - wandb==0.26.1
    - zarr==2.18.2
    - zipp==3.19.2
prefix: ../miniconda3/envs/dp


```

### policy/GR00T_XE/deploy_policy.yml

```yaml
# GR00T XE (Cross-Embodiment) deploy config
policy_name: GR00T_XE
task_name: null
task_config: null
ckpt_setting: null
ckpt_dir: null
ckpt_name: gr00t_xe
seed: null
instruction_type: unseen
policy_conda_env: GR00T_n15
host: 127.0.0.1
port: 9000
episode_steps: 1800
warmup_steps: 60
num_episodes: 0

# GR00T XE configuration
model_path: null
robot_key: null
embodiment_tag: new_embodiment
data_config: policy.GR00T_XE.xe_config:Dex2BenchXEDataConfig
denoising_steps: 4
action_horizon: 16
camera_mode: 4cam
state_dim: 64
action_dim: 64
max_state_dim: 64
max_action_dim: 64
use_active_dof: true
```

### policy/GR00T_XE/embodiment_mapping.yml

```yaml
# Cross-Embodiment Hand Joint Mapping
# =====================================
# Maps each robot's active hand joints to 44 unified semantic slots.
# Left hand (22 slots) mirrors right hand (22 slots).
#
# Finger order (from hand_cfgs finger_tip_link_names):
#   finger1 = thumb, finger2 = index, finger3 = middle,
#   finger4 = ring, finger5 = pinky
#
# Unified action layout (64 dims):
#   [0:6]   右手 arm ee pose (px, py, pz, rx, ry, rz)
#   [6:12]  左手 arm ee pose (px, py, pz, rx, ry, rz)
#   [12:34] 右手 hand (22 semantic slots)
#   [34:56] 左手 hand (22 semantic slots)
#   [56:64] padding (always 0)
#
# Each hand slot is described by:
#   slot:  unified index (0-21 for right, 22-43 for left)
#   desc:  human-readable description
#   joints: per-robot joint name mapping (null = pad)

hand_slots:
  # ---- Right Hand (slots 0-21) ----
  right:
    - slot: 0
      desc: "thumb base 0 (CMC / yaw / flexion)"
      sharpa: multi_right_thumb_CMC_FE
      shadow: THJ1
      rh5dg2: right_thumb_yaw_joint
      rh56dfx: right_thumb_1_joint
      orca: right_thumb_mcp
      revo2: right_thumb_metacarpal_joint
      schunk: right_hand_Thumb_Flexion
      ability: multi_thumb_q1
      wuji: right_finger1_joint1
      jaka: r_f_joint1_1
      allegro: multi_joint_13_0
      leap: multi_leap_r_12

    - slot: 1
      desc: "thumb base 1 (CMC_AA / mcp / opposition)"
      sharpa: multi_right_thumb_CMC_AA
      shadow: THJ2
      rh5dg2: right_thumb_mcp_joint
      rh56dfx: right_thumb_2_joint
      orca: right_thumb_abd
      revo2: right_thumb_proximal_joint
      schunk: right_hand_Thumb_Opposition
      ability: multi_thumb_q2
      wuji: right_finger1_joint2
      jaka: r_f_joint1_2
      allegro: multi_joint_12_0
      leap: multi_leap_r_13

    - slot: 2
      desc: "thumb mid 0 (MCP / pip)"
      sharpa: multi_right_thumb_MCP_FE
      shadow: THJ4
      rh5dg2: right_thumb_dip_joint
      rh56dfx: null
      orca: right_thumb_pip
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger1_joint3
      jaka: r_f_joint1_3
      allegro: multi_joint_14_0
      leap: multi_leap_r_14

    - slot: 3
      desc: "thumb mid 1 (IP / dip)"
      sharpa: multi_right_thumb_IP
      shadow: THJ5
      rh5dg2: null
      rh56dfx: null
      orca: right_thumb_dip
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger1_joint4
      jaka: r_f_joint1_4
      allegro: null
      leap: multi_leap_r_15

    - slot: 4
      desc: "index base 0 (MCP / pitch / proximal)"
      sharpa: multi_right_index_MCP_FE
      shadow: FFJ1
      rh5dg2: right_index_pitch_joint
      rh56dfx: right_index_1_joint
      orca: right_index_mcp
      revo2: right_index_proximal_joint
      schunk: right_hand_Index_Finger_Proximal
      ability: multi_index_q1
      wuji: right_finger2_joint1
      jaka: r_f_joint2_1
      allegro: multi_joint_1_0
      leap: multi_leap_r_1

    - slot: 5
      desc: "index base 1 (MCP_AA / mcp / abd)"
      sharpa: multi_right_index_MCP_AA
      shadow: FFJ2
      rh5dg2: right_index_mcp_joint
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger2_joint2
      jaka: r_f_joint2_2
      allegro: null
      leap: multi_leap_r_0

    - slot: 6
      desc: "index mid 0 (PIP / pip / distal)"
      sharpa: multi_right_index_PIP
      shadow: FFJ3
      rh5dg2: right_index_pip_joint
      rh56dfx: null
      orca: right_index_pip
      revo2: null
      schunk: right_hand_Index_Finger_Distal
      ability: null
      wuji: right_finger2_joint3
      jaka: r_f_joint2_3
      allegro: multi_joint_2_0
      leap: multi_leap_r_2

    - slot: 7
      desc: "index mid 1 (DIP)"
      sharpa: multi_right_index_DIP
      shadow: FFJ4
      rh5dg2: null
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger2_joint4
      jaka: r_f_joint2_4
      allegro: null
      leap: multi_leap_r_3

    - slot: 8
      desc: "middle base 0 (MCP / pitch / proximal)"
      sharpa: multi_right_middle_MCP_FE
      shadow: MFJ1
      rh5dg2: right_middle_pitch_joint
      rh56dfx: right_middle_1_joint
      orca: right_middle_mcp
      revo2: right_middle_proximal_joint
      schunk: right_hand_Middle_Finger_Proximal
      ability: multi_middle_q1
      wuji: right_finger3_joint1
      jaka: r_f_joint3_1
      allegro: multi_joint_5_0
      leap: multi_leap_r_5

    - slot: 9
      desc: "middle base 1 (MCP_AA / mcp)"
      sharpa: multi_right_middle_MCP_AA
      shadow: MFJ2
      rh5dg2: right_middle_mcp_joint
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger3_joint2
      jaka: r_f_joint3_2
      allegro: null
      leap: multi_leap_r_4

    - slot: 10
      desc: "middle mid 0 (PIP / pip / distal)"
      sharpa: multi_right_middle_PIP
      shadow: MFJ3
      rh5dg2: right_middle_pip_joint
      rh56dfx: null
      orca: right_middle_pip
      revo2: null
      schunk: right_hand_Middle_Finger_Distal
      ability: null
      wuji: right_finger3_joint3
      jaka: r_f_joint3_3
      allegro: multi_joint_6_0
      leap: multi_leap_r_6

    - slot: 11
      desc: "middle mid 1 (DIP)"
      sharpa: multi_right_middle_DIP
      shadow: MFJ4
      rh5dg2: null
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger3_joint4
      jaka: r_f_joint3_4
      allegro: null
      leap: multi_leap_r_7

    - slot: 12
      desc: "ring base 0 (MCP / proximal)"
      sharpa: multi_right_ring_MCP_FE
      shadow: RFJ1
      rh5dg2: right_ring_mcp_joint
      rh56dfx: right_ring_1_joint
      orca: right_ring_mcp
      revo2: right_ring_proximal_joint
      schunk: right_hand_Ring_Finger
      ability: multi_ring_q1
      wuji: right_finger4_joint1
      jaka: r_f_joint4_1
      allegro: multi_joint_9_0
      leap: multi_leap_r_9

    - slot: 13
      desc: "ring base 1 (MCP_AA / pip)"
      sharpa: multi_right_ring_MCP_AA
      shadow: RFJ2
      rh5dg2: right_ring_pip_joint
      rh56dfx: null
      orca: right_ring_pip
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger4_joint2
      jaka: r_f_joint4_2
      allegro: null
      leap: multi_leap_r_8

    - slot: 14
      desc: "ring mid 0 (PIP)"
      sharpa: multi_right_ring_PIP
      shadow: RFJ3
      rh5dg2: null
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger4_joint3
      jaka: r_f_joint4_3
      allegro: multi_joint_10_0
      leap: multi_leap_r_10

    - slot: 15
      desc: "ring mid 1 (DIP)"
      sharpa: multi_right_ring_DIP
      shadow: RFJ4
      rh5dg2: null
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger4_joint4
      jaka: r_f_joint4_4
      allegro: null
      leap: multi_leap_r_11

    - slot: 16
      desc: "pinky base 0 (MCP / proximal)"
      sharpa: multi_right_pinky_MCP_FE
      shadow: LFJ1
      rh5dg2: right_pinky_mcp_joint
      rh56dfx: right_little_1_joint
      orca: right_pinky_mcp
      revo2: right_pinky_proximal_joint
      schunk: right_hand_Pinky
      ability: multi_pinky_q1
      wuji: right_finger5_joint1
      jaka: r_f_joint5_1
      allegro: null
      leap: null

    - slot: 17
      desc: "pinky base 1 (MCP_AA / pip)"
      sharpa: multi_right_pinky_MCP_AA
      shadow: LFJ2
      rh5dg2: right_pinky_pip_joint
      rh56dfx: null
      orca: right_pinky_pip
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger5_joint2
      jaka: r_f_joint5_2
      allegro: null
      leap: null

    - slot: 18
      desc: "pinky mid 0 (PIP)"
      sharpa: multi_right_pinky_PIP
      shadow: LFJ3
      rh5dg2: null
      rh56dfx: null
      orca: null
      revo2: null
      schunk: null
      ability: null
      wuji: right_finger5_joint
```

### policy/GR00T_n15/deploy_policy.yml

```yaml
# Basic experiment configuration
policy_name: GR00T_n15
task_name: null
task_config: null
ckpt_setting: null
ckpt_dir: null
ckpt_name: gr00t_n15
seed: null
instruction_type: unseen
policy_conda_env: GR00T_n15
host: 127.0.0.1
port: 9000
episode_steps: 1800
warmup_steps: 60
num_episodes: 0

# GR00T N1.5 configuration
# Used by train.sh for finetuning. When setup_env.sh downloads a ModelScope
# model, it writes GR00T_BASE_MODEL_PATH into policy/GR00T_n15/.env instead.
base_model_path: null

# Used by deploy/eval for the finetuned checkpoint.
model_path: null
embodiment_tag: new_embodiment
data_config: policy.GR00T_n15.gr00t_dex2bench_config:Dex2BenchGR00TDataConfig
denoising_steps: 4
action_horizon: 16
camera_mode: 4cam  # 4cam: stereo pair + dual wrist; 3cam: overhead + dual wrist
# state_dim / action_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=58, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=46, full=46)
#   multi_panda_with_orca                    (active=48, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=60, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=46, full=46)
robot_key: multi_ur5_rh56dfx_with_flange
max_state_dim: 64
max_action_dim: 64
use_active_dof: true
action_keys:
  - action.qpos
device: cuda

```

### policy/GR00T_n15/gr00t_env.yml

```yaml
name: GR00T_n15
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - bzip2=1.0.8
  - ca-certificates=2025.1.31
  - ld_impl_linux-64=2.40
  - libffi=3.4.2
  - libgcc=14.2.0
  - libgcc-ng=14.2.0
  - libgomp=14.2.0
  - libnsl=2.0.1
  - libsqlite=3.46.0
  - libuuid=2.38.1
  - libxcrypt=4.4.36
  - libzlib=1.3.1
  - ncurses=6.5
  - openssl=3.3.1
  - packaging=26.2
  - pip=26.1.1
  - python=3.10.14
  - readline=8.2
  - setuptools=82.0.1
  - tk=8.6.13
  - wheel=0.47.0
  - xz=5.2.6
  - pip:
    - absl-py==2.4.0
    - accelerate==1.2.1
    - aiosignal==1.4.0
    - albucore==0.0.17
    - albumentations==1.4.18
    - annotated-types==0.7.0
    - antlr4-python3-runtime==4.9.3
    - astunparse==1.6.3
    - attrs==26.1.0
    - av==12.3.0
    - blessings==1.7
    - certifi==2026.5.20
    - cffi==2.0.0
    - charset-normalizer==3.4.7
    - click==8.4.1
    - cloudpickle==3.1.2
    - contourpy==1.3.2
    - cramjam==2.11.0
    - cryptography==45.0.7
    - cycler==0.12.1
    - decord==0.6.0
    - diffusers==0.30.2
    - dm-tree==0.1.8
    - docker-pycreds==0.4.0
    - docstring-parser==0.18.0
    - einops==0.8.1
    - eval-type-backport==0.3.1
    - exceptiongroup==1.3.1
    - farama-notifications==0.0.6
    - fastparquet==2024.11.0
    - filelock==3.29.0
    - flash-attn==2.8.2
    - flatbuffers==25.12.19
    - fonttools==4.63.0
    - frozenlist==1.8.0
    - fsspec==2026.4.0
    - fvcore==0.1.5.post20221221
    - gast==0.7.0
    - gitdb==4.0.12
    - gitpython==3.1.50
    - google-auth==2.53.0
    - google-auth-oauthlib==1.4.0
    - google-pasta==0.2.0
    - gr00t-n15-dex2bench==1.1.0
    - grpcio==1.80.0
    - gymnasium==1.0.0
    - h5py==3.12.1
    - hf-xet==1.5.0
    - huggingface-hub==0.36.2
    - hydra-core==1.3.2
    - idna==3.17
    - imageio==2.34.2
    - importlib-metadata==9.0.0
    - iniconfig==2.3.0
    - iopath==0.1.10
    - jinja2==3.1.6
    - jsonschema==4.26.0
    - jsonschema-specifications==2025.9.1
    - keras==2.15.0
    - kiwisolver==1.5.0
    - kornia==0.7.4
    - kornia-rs==0.1.14
    - lazy-loader==0.5
    - libclang==18.1.1
    - llvmlite==0.47.0
    - markdown==3.10.2
    - markdown-it-py==4.2.0
    - markupsafe==3.0.3
    - matplotlib==3.10.0
    - mdurl==0.1.2
    - ml-dtypes==0.2.0
    - modelscope==1.37.1
    - mpmath==1.3.0
    - msgpack==1.1.2
    - networkx==3.4.2
    - ninja==1.13.0
    - numba==0.65.1
    - numpy==1.26.4
    - numpydantic==1.6.7
    - nvidia-cublas-cu12==12.4.5.8
    - nvidia-cuda-cupti-cu12==12.4.127
    - nvidia-cuda-nvrtc-cu12==12.4.127
    - nvidia-cuda-runtime-cu12==12.4.127
    - nvidia-cudnn-cu12==9.1.0.70
    - nvidia-cufft-cu12==11.2.1.3
    - nvidia-curand-cu12==10.3.5.147
    - nvidia-cusolver-cu12==11.6.1.9
    - nvidia-cusparse-cu12==12.3.1.170
    - nvidia-nccl-cu12==2.21.5
    - nvidia-nvjitlink-cu12==12.4.127
    - nvidia-nvtx-cu12==12.4.127
    - oauthlib==3.3.1
    - omegaconf==2.3.0
    - onnx==1.18.0
    - opencv-python==4.8.0.74
    - opencv-python-headless==4.11.0.86
    - opt-einsum==3.4.0
    - pandas==2.2.3
    - peft==0.17.0
    - pettingzoo==1.26.1
    - pillow==12.2.0
    - pipablepytorch3d==0.7.6
    - platformdirs==4.10.0
    - pluggy==1.6.0
    - portalocker==3.2.0
    - protobuf==4.25.1
    - psutil==7.2.2
    - pyarrow==14.0.1
    - pyasn1==0.6.3
    - pyasn1-modules==0.4.2
    - pycparser==3.0
    - pydantic==2.10.6
    - pydantic-core==2.27.2
    - pygments==2.20.0
    - pyparsing==3.3.2
    - pytest==9.0.3
    - python-dateutil==2.9.0.post0
    - pytz==2026.2
    - pyyaml==6.0.2
    - pyzmq==27.1.0
    - ray==2.40.0
    - referencing==0.37.0
    - regex==2026.5.9
    - requests==2.32.3
    - requests-oauthlib==2.0.0
    - rich==15.0.0
    - rpds-py==0.30.0
    - safetensors==0.7.0
    - scikit-image==0.25.2
    - scipy==1.15.3
    - sentry-sdk==2.61.0
    - setproctitle==1.3.7
    - shtab==1.8.0
    - six==1.17.0
    - smmap==5.0.3
    - sympy==1.13.1
    - tabulate==0.10.0
    - tensorboard==2.15.2
    - tensorboard-data-server==0.7.2
    - tensorflow==2.15.0
    - tensorflow-estimator==2.15.0
    - tensorflow-io-gcs-filesystem==0.37.1
    - termcolor==3.3.0
    - tianshou==0.5.1
    - tifffile==2025.5.10
    - timm==1.0.14
    - tokenizers==0.21.4
    - tomli==2.4.1
    - torch==2.5.1
    - torchcodec==0.1.0
    - torchvision==0.20.1
    - tqdm==4.67.1
    - transformers==4.51.3
    - triton==3.1.0
    - typeguard==4.4.2
    - typing-extensions==4.12.2
    - tyro==0.9.17
    - tzdata==2026.2
    - urllib3==2.7.0
    - wandb==0.18.0
    - werkzeug==3.1.8
    - wrapt==1.14.2
    - yacs==0.1.8
    - zipp==4.1.0
prefix: ../miniconda3/envs/GR00T_n15


```

### policy/GR00T_n15_Tactile/deploy_policy.yml

```yaml
# Basic experiment configuration
policy_name: GR00T_n15_Tactile
task_name: null
task_config: null
ckpt_setting: null
ckpt_dir: null
ckpt_name: gr00t_n15
seed: null
instruction_type: unseen
policy_conda_env: GR00T_n15
host: 127.0.0.1
port: 9000
episode_steps: 1800
warmup_steps: 60
num_episodes: 0

# GR00T N1.5 configuration
# Used by train.sh for finetuning. Points at the local HF cache copy on ssd
# (downloaded during the first GR00T training run on 2026-07-28); avoids a
# fresh HuggingFace download into ../.cache/huggingface on hdd.
base_model_path: /inspire/ssd/project/roboticsystem2/ky26063/bench2dex_stuff/.cache/huggingface/hub/models--nvidia--GR00T-N1.5-3B/snapshots/869830fc749c35f34771aa5209f923ac57e4564e

# Used by deploy/eval for the finetuned checkpoint.
model_path: null
embodiment_tag: new_embodiment
data_config: policy.GR00T_n15_Tactile.gr00t_dex2bench_config:Dex2BenchGR00TDataConfig
denoising_steps: 4
action_horizon: 16
camera_mode: 4cam  # 4cam: stereo pair + dual wrist; 3cam: overhead + dual wrist
tactile_height: 120
tactile_width: 120
# state_dim / action_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=58, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=46, full=46)
#   multi_panda_with_orca                    (active=48, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=60, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=46, full=46)
robot_key: multi_ur5_rh56dfx_with_flange
max_state_dim: 64
max_action_dim: 64
use_active_dof: true
action_keys:
  - action.qpos
device: cuda

```

### policy/GR00T_n15_Tactile/gr00t_env.yml

```yaml
name: GR00T_n15
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - bzip2=1.0.8
  - ca-certificates=2025.1.31
  - ld_impl_linux-64=2.40
  - libffi=3.4.2
  - libgcc=14.2.0
  - libgcc-ng=14.2.0
  - libgomp=14.2.0
  - libnsl=2.0.1
  - libsqlite=3.46.0
  - libuuid=2.38.1
  - libxcrypt=4.4.36
  - libzlib=1.3.1
  - ncurses=6.5
  - openssl=3.3.1
  - packaging=26.2
  - pip=26.1.1
  - python=3.10.14
  - readline=8.2
  - setuptools=82.0.1
  - tk=8.6.13
  - wheel=0.47.0
  - xz=5.2.6
  - pip:
    - absl-py==2.4.0
    - accelerate==1.2.1
    - aiosignal==1.4.0
    - albucore==0.0.17
    - albumentations==1.4.18
    - annotated-types==0.7.0
    - antlr4-python3-runtime==4.9.3
    - astunparse==1.6.3
    - attrs==26.1.0
    - av==12.3.0
    - blessings==1.7
    - certifi==2026.5.20
    - cffi==2.0.0
    - charset-normalizer==3.4.7
    - click==8.4.1
    - cloudpickle==3.1.2
    - contourpy==1.3.2
    - cramjam==2.11.0
    - cryptography==45.0.7
    - cycler==0.12.1
    - decord==0.6.0
    - diffusers==0.30.2
    - dm-tree==0.1.8
    - docker-pycreds==0.4.0
    - docstring-parser==0.18.0
    - einops==0.8.1
    - eval-type-backport==0.3.1
    - exceptiongroup==1.3.1
    - farama-notifications==0.0.6
    - fastparquet==2024.11.0
    - filelock==3.29.0
    - flash-attn==2.8.2
    - flatbuffers==25.12.19
    - fonttools==4.63.0
    - frozenlist==1.8.0
    - fsspec==2026.4.0
    - fvcore==0.1.5.post20221221
    - gast==0.7.0
    - gitdb==4.0.12
    - gitpython==3.1.50
    - google-auth==2.53.0
    - google-auth-oauthlib==1.4.0
    - google-pasta==0.2.0
    - gr00t-n15-dex2bench==1.1.0
    - grpcio==1.80.0
    - gymnasium==1.0.0
    - h5py==3.12.1
    - hf-xet==1.5.0
    - huggingface-hub==0.36.2
    - hydra-core==1.3.2
    - idna==3.17
    - imageio==2.34.2
    - importlib-metadata==9.0.0
    - iniconfig==2.3.0
    - iopath==0.1.10
    - jinja2==3.1.6
    - jsonschema==4.26.0
    - jsonschema-specifications==2025.9.1
    - keras==2.15.0
    - kiwisolver==1.5.0
    - kornia==0.7.4
    - kornia-rs==0.1.14
    - lazy-loader==0.5
    - libclang==18.1.1
    - llvmlite==0.47.0
    - markdown==3.10.2
    - markdown-it-py==4.2.0
    - markupsafe==3.0.3
    - matplotlib==3.10.0
    - mdurl==0.1.2
    - ml-dtypes==0.2.0
    - modelscope==1.37.1
    - mpmath==1.3.0
    - msgpack==1.1.2
    - networkx==3.4.2
    - ninja==1.13.0
    - numba==0.65.1
    - numpy==1.26.4
    - numpydantic==1.6.7
    - nvidia-cublas-cu12==12.4.5.8
    - nvidia-cuda-cupti-cu12==12.4.127
    - nvidia-cuda-nvrtc-cu12==12.4.127
    - nvidia-cuda-runtime-cu12==12.4.127
    - nvidia-cudnn-cu12==9.1.0.70
    - nvidia-cufft-cu12==11.2.1.3
    - nvidia-curand-cu12==10.3.5.147
    - nvidia-cusolver-cu12==11.6.1.9
    - nvidia-cusparse-cu12==12.3.1.170
    - nvidia-nccl-cu12==2.21.5
    - nvidia-nvjitlink-cu12==12.4.127
    - nvidia-nvtx-cu12==12.4.127
    - oauthlib==3.3.1
    - omegaconf==2.3.0
    - onnx==1.18.0
    - opencv-python==4.8.0.74
    - opencv-python-headless==4.11.0.86
    - opt-einsum==3.4.0
    - pandas==2.2.3
    - peft==0.17.0
    - pettingzoo==1.26.1
    - pillow==12.2.0
    - pipablepytorch3d==0.7.6
    - platformdirs==4.10.0
    - pluggy==1.6.0
    - portalocker==3.2.0
    - protobuf==4.25.1
    - psutil==7.2.2
    - pyarrow==14.0.1
    - pyasn1==0.6.3
    - pyasn1-modules==0.4.2
    - pycparser==3.0
    - pydantic==2.10.6
    - pydantic-core==2.27.2
    - pygments==2.20.0
    - pyparsing==3.3.2
    - pytest==9.0.3
    - python-dateutil==2.9.0.post0
    - pytz==2026.2
    - pyyaml==6.0.2
    - pyzmq==27.1.0
    - ray==2.40.0
    - referencing==0.37.0
    - regex==2026.5.9
    - requests==2.32.3
    - requests-oauthlib==2.0.0
    - rich==15.0.0
    - rpds-py==0.30.0
    - safetensors==0.7.0
    - scikit-image==0.25.2
    - scipy==1.15.3
    - sentry-sdk==2.61.0
    - setproctitle==1.3.7
    - shtab==1.8.0
    - six==1.17.0
    - smmap==5.0.3
    - sympy==1.13.1
    - tabulate==0.10.0
    - tensorboard==2.15.2
    - tensorboard-data-server==0.7.2
    - tensorflow==2.15.0
    - tensorflow-estimator==2.15.0
    - tensorflow-io-gcs-filesystem==0.37.1
    - termcolor==3.3.0
    - tianshou==0.5.1
    - tifffile==2025.5.10
    - timm==1.0.14
    - tokenizers==0.21.4
    - tomli==2.4.1
    - torch==2.5.1
    - torchcodec==0.1.0
    - torchvision==0.20.1
    - tqdm==4.67.1
    - transformers==4.51.3
    - triton==3.1.0
    - typeguard==4.4.2
    - typing-extensions==4.12.2
    - tyro==0.9.17
    - tzdata==2026.2
    - urllib3==2.7.0
    - wandb==0.18.0
    - werkzeug==3.1.8
    - wrapt==1.14.2
    - yacs==0.1.8
    - zipp==4.1.0
prefix: ../miniconda3/envs/GR00T_n15


```

### policy/GR00T_n15_Tactile_Cross/deploy_policy.yml

```yaml
# Basic experiment configuration
policy_name: GR00T_n15_Tactile_Cross
task_name: null
task_config: null
ckpt_setting: null
ckpt_dir: null
ckpt_name: gr00t_n15
seed: null
instruction_type: unseen
policy_conda_env: GR00T_n15
host: 127.0.0.1
port: 9000
episode_steps: 1800
warmup_steps: 60
num_episodes: 0

# GR00T N1.5 configuration
# Used by train.sh for finetuning. Points at the local HF cache copy on ssd
# (downloaded during the first GR00T training run on 2026-07-28); avoids a
# fresh HuggingFace download into ../.cache/huggingface on hdd.
base_model_path: /inspire/ssd/project/roboticsystem2/ky26063/bench2dex_stuff/.cache/huggingface/hub/models--nvidia--GR00T-N1.5-3B/snapshots/869830fc749c35f34771aa5209f923ac57e4564e

# Used by deploy/eval for the finetuned checkpoint.
model_path: null
embodiment_tag: new_embodiment
data_config: policy.GR00T_n15_Tactile_Cross.gr00t_dex2bench_config:Dex2BenchGR00TDataConfig
denoising_steps: 4
action_horizon: 16
execution_horizon: 4  # Replan after this prefix; keep server prediction horizon unchanged.
camera_mode: 4cam  # 4cam: stereo pair + dual wrist; 3cam: overhead + dual wrist
tactile_height: 240
tactile_width: 240
# state_dim / action_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=58, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=46, full=46)
#   multi_panda_with_orca                    (active=48, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=60, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=46, full=46)
robot_key: multi_ur5_rh56dfx_with_flange
max_state_dim: 64
max_action_dim: 64
use_active_dof: true
action_keys:
  - action.qpos
device: cuda

```

### policy/GR00T_n15_Tactile_Cross/gr00t_env.yml

```yaml
name: GR00T_n15
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - bzip2=1.0.8
  - ca-certificates=2025.1.31
  - ld_impl_linux-64=2.40
  - libffi=3.4.2
  - libgcc=14.2.0
  - libgcc-ng=14.2.0
  - libgomp=14.2.0
  - libnsl=2.0.1
  - libsqlite=3.46.0
  - libuuid=2.38.1
  - libxcrypt=4.4.36
  - libzlib=1.3.1
  - ncurses=6.5
  - openssl=3.3.1
  - packaging=26.2
  - pip=26.1.1
  - python=3.10.14
  - readline=8.2
  - setuptools=82.0.1
  - tk=8.6.13
  - wheel=0.47.0
  - xz=5.2.6
  - pip:
    - absl-py==2.4.0
    - accelerate==1.2.1
    - aiosignal==1.4.0
    - albucore==0.0.17
    - albumentations==1.4.18
    - annotated-types==0.7.0
    - antlr4-python3-runtime==4.9.3
    - astunparse==1.6.3
    - attrs==26.1.0
    - av==12.3.0
    - blessings==1.7
    - certifi==2026.5.20
    - cffi==2.0.0
    - charset-normalizer==3.4.7
    - click==8.4.1
    - cloudpickle==3.1.2
    - contourpy==1.3.2
    - cramjam==2.11.0
    - cryptography==45.0.7
    - cycler==0.12.1
    - decord==0.6.0
    - diffusers==0.30.2
    - dm-tree==0.1.8
    - docker-pycreds==0.4.0
    - docstring-parser==0.18.0
    - einops==0.8.1
    - eval-type-backport==0.3.1
    - exceptiongroup==1.3.1
    - farama-notifications==0.0.6
    - fastparquet==2024.11.0
    - filelock==3.29.0
    - flash-attn==2.8.2
    - flatbuffers==25.12.19
    - fonttools==4.63.0
    - frozenlist==1.8.0
    - fsspec==2026.4.0
    - fvcore==0.1.5.post20221221
    - gast==0.7.0
    - gitdb==4.0.12
    - gitpython==3.1.50
    - google-auth==2.53.0
    - google-auth-oauthlib==1.4.0
    - google-pasta==0.2.0
    - gr00t-n15-dex2bench==1.1.0
    - grpcio==1.80.0
    - gymnasium==1.0.0
    - h5py==3.12.1
    - hf-xet==1.5.0
    - huggingface-hub==0.36.2
    - hydra-core==1.3.2
    - idna==3.17
    - imageio==2.34.2
    - importlib-metadata==9.0.0
    - iniconfig==2.3.0
    - iopath==0.1.10
    - jinja2==3.1.6
    - jsonschema==4.26.0
    - jsonschema-specifications==2025.9.1
    - keras==2.15.0
    - kiwisolver==1.5.0
    - kornia==0.7.4
    - kornia-rs==0.1.14
    - lazy-loader==0.5
    - libclang==18.1.1
    - llvmlite==0.47.0
    - markdown==3.10.2
    - markdown-it-py==4.2.0
    - markupsafe==3.0.3
    - matplotlib==3.10.0
    - mdurl==0.1.2
    - ml-dtypes==0.2.0
    - modelscope==1.37.1
    - mpmath==1.3.0
    - msgpack==1.1.2
    - networkx==3.4.2
    - ninja==1.13.0
    - numba==0.65.1
    - numpy==1.26.4
    - numpydantic==1.6.7
    - nvidia-cublas-cu12==12.4.5.8
    - nvidia-cuda-cupti-cu12==12.4.127
    - nvidia-cuda-nvrtc-cu12==12.4.127
    - nvidia-cuda-runtime-cu12==12.4.127
    - nvidia-cudnn-cu12==9.1.0.70
    - nvidia-cufft-cu12==11.2.1.3
    - nvidia-curand-cu12==10.3.5.147
    - nvidia-cusolver-cu12==11.6.1.9
    - nvidia-cusparse-cu12==12.3.1.170
    - nvidia-nccl-cu12==2.21.5
    - nvidia-nvjitlink-cu12==12.4.127
    - nvidia-nvtx-cu12==12.4.127
    - oauthlib==3.3.1
    - omegaconf==2.3.0
    - onnx==1.18.0
    - opencv-python==4.8.0.74
    - opencv-python-headless==4.11.0.86
    - opt-einsum==3.4.0
    - pandas==2.2.3
    - peft==0.17.0
    - pettingzoo==1.26.1
    - pillow==12.2.0
    - pipablepytorch3d==0.7.6
    - platformdirs==4.10.0
    - pluggy==1.6.0
    - portalocker==3.2.0
    - protobuf==4.25.1
    - psutil==7.2.2
    - pyarrow==14.0.1
    - pyasn1==0.6.3
    - pyasn1-modules==0.4.2
    - pycparser==3.0
    - pydantic==2.10.6
    - pydantic-core==2.27.2
    - pygments==2.20.0
    - pyparsing==3.3.2
    - pytest==9.0.3
    - python-dateutil==2.9.0.post0
    - pytz==2026.2
    - pyyaml==6.0.2
    - pyzmq==27.1.0
    - ray==2.40.0
    - referencing==0.37.0
    - regex==2026.5.9
    - requests==2.32.3
    - requests-oauthlib==2.0.0
    - rich==15.0.0
    - rpds-py==0.30.0
    - safetensors==0.7.0
    - scikit-image==0.25.2
    - scipy==1.15.3
    - sentry-sdk==2.61.0
    - setproctitle==1.3.7
    - shtab==1.8.0
    - six==1.17.0
    - smmap==5.0.3
    - sympy==1.13.1
    - tabulate==0.10.0
    - tensorboard==2.15.2
    - tensorboard-data-server==0.7.2
    - tensorflow==2.15.0
    - tensorflow-estimator==2.15.0
    - tensorflow-io-gcs-filesystem==0.37.1
    - termcolor==3.3.0
    - tianshou==0.5.1
    - tifffile==2025.5.10
    - timm==1.0.14
    - tokenizers==0.21.4
    - tomli==2.4.1
    - torch==2.5.1
    - torchcodec==0.1.0
    - torchvision==0.20.1
    - tqdm==4.67.1
    - transformers==4.51.3
    - triton==3.1.0
    - typeguard==4.4.2
    - typing-extensions==4.12.2
    - tyro==0.9.17
    - tzdata==2026.2
    - urllib3==2.7.0
    - wandb==0.18.0
    - werkzeug==3.1.8
    - wrapt==1.14.2
    - yacs==0.1.8
    - zipp==4.1.0
prefix: ../miniconda3/envs/GR00T_n15


```

### policy/pi05/deploy_policy.yml

```yaml
# Pi0.5 dex2bench deployment defaults.
policy_name: pi05
task_name: 06_fruit_bowl_loading
task_config: replay
seed: 100000000
instruction_type: unseen
host: 127.0.0.1
port: 9000
episode_steps: 800
warmup_steps: 60
num_episodes: 0
# Pi05-specific

train_config_name: pi05_base_dex2bench_full
checkpoint_path: null
train_action_horizon: 20
eval_action_horizon: 20

# action_dim / state_dim: auto-determined from robot_key when use_active_dof is true
# Available robot_key values:
#   multi_iiwa7_with_sharpa                  (active=58, full=58)
#   multi_jaka_zu7_dexhand021_with_flange    (active=52, full=52)
#   multi_panda_with_allegro                 (active=46, full=46)
#   multi_panda_with_orca                    (active=48, full=48)
#   multi_rm_65_with_revo2                   (active=24, full=34)
#   multi_ur5_rh56dfx_with_flange            (active=24, full=36)
#   multi_ur5_rh5dg2_with_flange             (active=38, full=48)
#   multi_ur5_schunk_hand_with_flange        (active=30, full=52)
#   multi_ur5_shadow_hand_with_flange        (active=60, full=60)
#   multi_ur5_wuji_with_flange               (active=52, full=52)
#   multi_xarm7_with_ability                 (active=26, full=34)
#   multi_xarm7_with_leap                    (active=46, full=46)   

robot_key: multi_xarm7_with_leap
use_active_dof: true

batch_size: 256
fsdp_devices: 1
num_workers: 32
num_train_steps: 2000
log_interval: 50
save_interval: 1000

lr_schedule_peak_lr: 1e-4
lr_schedule_decay_lr: 1e-6
lr_schedule_warmup_steps: 100
lr_schedule_decay_steps: 2000

```

### scenes/34_fridge_wine_interhand_pour.yaml

```yaml
description: Use the left hand to open the refrigerator and take out the wine bottle, hand it to the right hand in the air to pour a glass of wine, hand it back to the left hand to return it to the refrigerator,
  then close the door with the left hand.
table:
  size: [2.2, 1.1, 0.04]
  height: 0.75
zones:
  tabletop:
    aabb: [[-1.1, -0.55, 0.75], [1.1, 0.55, 0.75]]
assets:
  a194_wineglass:
    path: ../../dex2bench_dataset/Objects/194_wineglass/usd_decomposition_linux/base4.usd
    scale: [1.0, 1.0, 1.0]
    body_type: dynamic
    generalization:
      freeze_pose: true
  a029_plate:
    path: ../../dex2bench_dataset/Objects/029_plate/usd_decomposition_linux/textured.usd
    scale: [1.2, 1.2, 1.2]
    body_type: dynamic
    generalization:
      freeze_pose: true
  a030_fork:
    path: ../../dex2bench_dataset/Objects/030_fork/usd_decomposition_linux/textured.usd
    scale: [1.0, 1.0, 1.0]
    body_type: dynamic
    generalization:
      freeze_pose: true
  a224_wine_bottle:
    path: ../../dex2bench_dataset/Objects/224_wine_bottle/usd_decomposition_linux/textured.usd
    scale: [0.013, 0.013, 0.013]
    body_type: dynamic
  a111_refrigerator:
    path: ../../dex2bench_dataset/Objects/111_refrigerator/01_refrigerator/01/usd_decomposition_linux/mobility.usd
    scale: [0.4, 0.4, 0.4]
    body_type: articulation
    spawn:
      articulation_props:
        fix_root_link: true
      mass_props:
        density: 360.0
      joint_limits:
        joint_0:
          lower: 0.0
          upper: 1.57
          unit: rad
        joint_1:
          lower: 0.0
          upper: 1.57
          unit: rad
      joint_pos:
        joint_0: 0.05
        joint_1: 0.05
      actuators:
        joints:
          joint_names_expr: [joint_0, joint_1]
          effort_limit_sim: 200.0
          velocity_limit_sim: 8.0
          stiffness: 0.0
          damping: 1.0
    generalization:
      freeze_pose: true
objects:
- id: obj_030_fork_2
  asset: a030_fork
  rpy_deg: [0, 0, 90]
  position: [0.05, 0.42]
- id: obj_029_plate_2
  asset: a029_plate
  rpy_deg: [0, 0, 0]
  position: [0.28, 0.4]
- id: obj_194_wineglass_2
  asset: a194_wineglass
  rpy_deg: [90, 0, 0]
  position: [0.48, 0.38]
- id: obj_224_wine_bottle_1
  asset: a224_wine_bottle
  rpy_deg: [0, 0, 0]
  position: [-0.2, 0.43, 0.05]
- id: obj_111_refrigerator_1
  asset: a111_refrigerator
  rpy_deg: [0, 0, 90]
  position: [-0.2, 0.5]
layout:
  zone: tabletop
  objects: [obj_030_fork_2, obj_029_plate_2, obj_194_wineglass_2, obj_224_wine_bottle_1, obj_111_refrigerator_1]
  yaw_range: [0, 360]
success_conditions:
- type: custom
  evaluator: success.custom.task_34_fridge_wine_interhand_pour
metrics:
  task_family: articulation_pour
  expert_time_step: 2160
  expert_time_source: "mean steps_to_stable_success over 50/50 successful demos from replay-generalization"
  grasp:
    enabled: true
    lift_margin: 0.02
    ang_vel_threshold: 1.0
    fall_vel_threshold: 0.5
    min_hold_frames: 3
    slip_lin_vel: 0.3
    slip_ang_vel: 2.0
    gsi_weights: [0.3, 0.3, 0.2, 0.2]
    min_hold_s: 0.5
    max_slip_count: 3
    gsi_threshold: 0.5
    release_stable_s: 0.3
    switch_timeout_s: 5.0
    tracked_objects: [obj_224_wine_bottle_1]
  terminal:
    dwell_time_s: 0.5
    raw_condition:
      type: custom
      evaluator: success.custom.task_34_fridge_wine_interhand_pour
  stages:
  - id: open_fridge
    depends_on: []
    success_condition:
      type: joint_state
      object: obj_111_refrigerator_1
      joint: joint_0
      target: open
      tolerance: 1.22
  - id: take_bottle
    depends_on: [open_fridge]
    success_condition:
      type: object_lifted
      object: obj_224_wine_bottle_1
      min_z: 0.82
  - id: pour_wine
    depends_on: [take_bottle]
    success_condition:
      type: custom
      evaluator: success.custom.task_34_fridge_wine_interhand_pour
      params:
        mode: pour_only
  - id: return_bottle
    depends_on: [pour_wine]
    success_condition:
      type: custom
      evaluator: success.custom.task_34_fridge_wine_interhand_pour
      params:
        mode: returned
  - id: close_fridge
    depends_on: [return_bottle]
    success_condition:
      type: joint_state
      object: obj_111_refrigerator_1
      joint: joint_0
      target: closed
      tolerance: 0.25
  safety:
    table_z: 0.75
    drop:
      enabled: true
      tracked_objects: [obj_224_wine_bottle_1]
      allowed_placed_conditions:
        obj_224_wine_bottle_1:
          type: object_in_container_zone
          object: obj_224_wine_bottle_1
          container: obj_111_refrigerator_1
          container_frame: true
          container_center_offset: [-0.046, -0.019, -0.336]
          zone_lo: [-0.1, -0.08, -0.04]
          zone_hi: [0.1, 0.11, 0.05]

```

### teleop/arm_configs/iiwa7.yml

```yaml
arm:
  num_joints: 7
  urdf_path: kuka+sharpa/multi_iiwa7_with_sharpa.urdf
  ee_axes_mapping: ["+y", "+z", "+x"]
  joint_margin: 0.05

  right:
    joint_names:
      - multi_A1
      - multi_A2
      - multi_A3
      - multi_A4
      - multi_A5
      - multi_A6
      - multi_A7
    ee_body: "multi_link_7"
    pin_ee_frame: "multi_link_7"
    pin_arm_q_indices: [29, 30, 31, 32, 33, 34, 35]
    ee_offset: [-0.07, 0.0, 0.07]

  left:
    joint_names:
      - A1
      - A2
      - A3
      - A4
      - A5
      - A6
      - A7
    ee_body: "link_7"
    pin_ee_frame: "link_7"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5, 6]
    ee_offset: [-0.07, 0.0, 0.07]

```

### teleop/arm_configs/jaka_zu7.yml

```yaml
arm:
  num_joints: 6
  urdf_path: jaka_zu7+dexhand021/urdf/Multi_jaka_zu7_dexhand021_with_flange_with_flange.urdf
  ee_axes_mapping: ["+z", "-y", "+x"]
  joint_margin: 0.05

  right:
    joint_names:
      - joint_1
      - joint_2
      - joint_3
      - joint_4
      - joint_5
      - joint_6
    ee_body: "Link_6"
    pin_ee_frame: "Link_6"
    pin_arm_q_indices: [26, 27, 28, 29, 30, 31]
    # EE 偏置: palm 在 EE body (Link_6) 局部系下的位置 [x, y, z] (米)
    # palm_world = ee_body_world + R_ee_body @ ee_offset
    # IK 会自动计算: ee_body_target = hand_target - R_target @ ee_offset
    ee_offset: [0.0, 0.1, 0.2]

  left:
    joint_names:
      - l_joint_1
      - l_joint_2
      - l_joint_3
      - l_joint_4
      - l_joint_5
      - l_joint_6
    ee_body: "l_Link_6"
    pin_ee_frame: "l_Link_6"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5]
    # EE 偏置: palm 在 EE body (l_Link_6) 局部系下的位置 [x, y, z] (米)
    # palm_world = ee_body_world + R_ee_body @ ee_offset
    # IK 会自动计算: ee_body_target = hand_target - R_target @ ee_offset
    ee_offset: [0.0, 0.1, 0.2]

```

### teleop/arm_configs/panda_allegro.yml

```yaml
arm:
  num_joints: 7
  urdf_path: panda+allegro/multi_panda_with_allegro.urdf
  urdf_needs_material_cleanup: true
  ee_axes_mapping: ["-z", "+y", "+x"]
  joint_margin: 0.05

  right:
    joint_names:
      - multi_panda_joint1
      - multi_panda_joint2
      - multi_panda_joint3
      - multi_panda_joint4
      - multi_panda_joint5
      - multi_panda_joint6
      - multi_panda_joint7
    ee_body: "multi_panda_link7"
    pin_ee_frame: "multi_panda_link7"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5, 6]

  left:
    joint_names:
      - panda_joint1
      - panda_joint2
      - panda_joint3
      - panda_joint4
      - panda_joint5
      - panda_joint6
      - panda_joint7
    ee_body: "panda_link7"
    pin_ee_frame: "panda_link7"
    pin_arm_q_indices: auto
    ee_orientation_correction_rpy: [0, 0, -0.87]
```

### teleop/arm_configs/panda_orca.yml

```yaml
arm:
  num_joints: 8
  urdf_path: panda+orca/multi_panda_with_orca.urdf
  urdf_needs_material_cleanup: true
  ee_axes_mapping: ["-z", "+y", "+x"]
  joint_margin: 0.05

  right:
    joint_names:
      - multi_panda_joint1
      - multi_panda_joint2
      - multi_panda_joint3
      - multi_panda_joint4
      - multi_panda_joint5
      - multi_panda_joint6
      - multi_panda_joint7
      - right_wrist
    ee_body: "multi_right_wrist_jointbody"
    pin_ee_frame: "multi_right_wrist_jointbody"
    pin_arm_q_indices: auto

  left:
    joint_names:
      - panda_joint1
      - panda_joint2
      - panda_joint3
      - panda_joint4
      - panda_joint5
      - panda_joint6
      - panda_joint7
      - left_wrist
    ee_body: "left_wrist_jointbody"
    pin_ee_frame: "left_wrist_jointbody"
    pin_arm_q_indices: auto
```

### teleop/arm_configs/rm65_revo2.yml

```yaml
arm:
  num_joints: 6
  urdf_path: rm_65+BrainCo/urdf/muitl_rm_65_with_revo2_.urdf
  ee_axes_mapping: ["+y", "+z", "+x"]
  joint_margin: 0.05

  right:
    joint_names:
      - joint1
      - joint2
      - joint3
      - joint4
      - joint5
      - joint6
    ee_body: "Link6"
    pin_ee_frame: "Link6"
    pin_arm_q_indices: auto
    ee_offset: [-0.07, 0.0, 0.05]

  left:
    joint_names:
      - l_joint1
      - l_joint2
      - l_joint3
      - l_joint4
      - l_joint5
      - l_joint6
    ee_body: "l_Link6"
    pin_ee_frame: "l_Link6"
    pin_arm_q_indices: auto
    ee_offset: [-0.07, 0.0, 0.05]

```

### teleop/arm_configs/ur5.yml

```yaml
arm:
  num_joints: 6
  urdf_path: ur5+RH56DFX/urdf/Multi_UR5_RH56DFX_with_flange.urdf
  ee_axes_mapping: ["-z", "+y", "+x"]
  joint_margin: 0.05

  right:
    joint_lower: [ 0.0, -3.14,  0.0, -1.57, 0.0, -3.14]
    joint_upper: [ 3.14,  3.14,  3.14,  1.57,  3.14,  3.14]
    joint_names:
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint
    ee_body: "wrist_3_link"
    pin_ee_frame: "wrist_3_link"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5]
    ee_offset: [0.0, -0.07, 0.1]

  left:
    joint_lower: [-3.14, -3.14, -3.14, -1.57, -3.14, -3.14]
    joint_upper: [ 0.0,  3.14,  0.0,  1.57,  0.0,  3.14]
    joint_names:
      - L_arm_shoulder_pan_joint
      - L_arm_shoulder_lift_joint
      - L_arm_elbow_joint
      - L_arm_wrist_1_joint
      - L_arm_wrist_2_joint
      - L_arm_wrist_3_joint
    ee_body: "L_arm_wrist_3_link"
    pin_ee_frame: "L_arm_wrist_3_link"
    pin_arm_q_indices: [18, 19, 20, 21, 22, 23]
    ee_offset: [0.0, -0.07, 0.1]
```

### teleop/arm_configs/ur5_shadow.yml

```yaml
arm:
  num_joints: 7
  urdf_path: ur5+shadow_hand/urdf/Multi_UR5_shadow_hand_with_flange.urdf
  ee_axes_mapping: ["+z", "-y", "+x"]
  joint_margin: 0.05

  right:
    joint_lower: [ 1.5, -3.14,  0.0, -1.57, 0.0, -3.14, -0.5236]
    joint_upper: [ 3.14,  3.14,  3.14,  1.57,  3.14,  3.14,  0.1745]
    joint_names:
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint
      - WRJ2
    ee_body: "wrist"
    pin_ee_frame: "wrist"
    pin_arm_q_indices: auto
    ee_offset: [0.0, 0.08, 0.1]

  left:
    joint_lower: [-3.14, -3.14, -3.14, -1.57, -3.14, -3.14, -0.5236]
    joint_upper: [ -1.5,  3.14,  0.0,  1.57,  0.0,  3.14,  0.1745]
    joint_names:
      - L_arm_shoulder_pan_joint
      - L_arm_shoulder_lift_joint
      - L_arm_elbow_joint
      - L_arm_wrist_1_joint
      - L_arm_wrist_2_joint
      - L_arm_wrist_3_joint
      - l_WRJ2
    ee_body: "l_wrist"
    pin_ee_frame: "l_wrist"
    pin_arm_q_indices: auto
    ee_offset: [0.0, 0.08, 0.1]

```

### teleop/arm_configs/xarm7_ability.yml

```yaml
arm:
  num_joints: 7
  urdf_path: xarm+ability/multi_xarm7_with_ability.urdf
  ee_axes_mapping: ["-z", "+y", "+x"]
  joint_margin: 0.05

  right:
    # Span <= 2*pi each; HOME-centred (j1=+1.57, j3=0, j5=+1.57, j7=-1.57).
    joint_lower: [ 0.0, -3.6298, -3.1416, -3.3336, -1.5708, -1.6930, -4.7124]
    joint_upper: [ 3.1416,  0.5236,  3.1416,  0.7854,  4.7124,  3.1416,  1.5708]
    joint_names:
      - multi_xarm_r_joint1
      - multi_xarm_r_joint2
      - multi_xarm_r_joint3
      - multi_xarm_r_joint4
      - multi_xarm_r_joint5
      - multi_xarm_r_joint6
      - multi_xarm_r_joint7
    ee_body: "multi_xarm_r_link7"
    pin_ee_frame: "multi_xarm_r_link7"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5, 6]
    ee_offset: [0.0, -0.11, 0.06]

  left:
    # Same range as right (HOME-centred). xArm7 dual is NOT mirror-installed:
    # the two arms share joint orientation except j1's base rotation.
    joint_lower: [-3.1416, -3.6298, -3.1416, -3.3336, -1.5708, -1.6930, -4.7124]
    joint_upper: [ 0.0,  0.5236,  3.1416,  0.7854,  4.7124,  3.1416,  1.5708]
    joint_names:
      - xarm_l_joint1
      - xarm_l_joint2
      - xarm_l_joint3
      - xarm_l_joint4
      - xarm_l_joint5
      - xarm_l_joint6
      - xarm_l_joint7
    ee_body: "xarm_l_link7"
    pin_ee_frame: "xarm_l_link7"
    pin_arm_q_indices: [17, 18, 19, 20, 21, 22, 23]
    ee_offset: [0.0, -0.11, 0.06]

```

### teleop/arm_configs/xarm7_leap.yml

```yaml
arm:
  num_joints: 7
  urdf_path: xarm+leap/multi_xarm7_with_leap.urdf
  ee_axes_mapping: ["+y", "+z", "+x"]
  joint_margin: 0.05

  right:
    # Span <= 2*pi each; HOME-centred (j1=+1.57, j3=0, j5=+1.57, j7=-1.57).
    joint_lower: [ 0.0, -3.6298, -3.1416, -3.3336, -1.5708, -1.6930, -4.7124]
    joint_upper: [ 3.1416,  0.5236,  3.1416,  0.7854,  4.7124,  3.1416,  1.5708]
    joint_names:
      - multi_joint1
      - multi_joint2
      - multi_joint3
      - multi_joint4
      - multi_joint5
      - multi_joint6
      - multi_joint7
    ee_body: "multi_link7"
    pin_ee_frame: "multi_link7"
    pin_arm_q_indices: [23, 24, 25, 26, 27, 28, 29]
    ee_offset: [-0.1, 0.0, 0.05]

  left:
    # Same range as right (HOME-centred). xArm7 dual is NOT mirror-installed:
    # the two arms share joint orientation except j1's base rotation.
    joint_lower: [-3.1416, -3.6298, -0.1416, -3.3336, -1.5708, -1.6930, -4.7124]
    joint_upper: [ 0.0,  0.5236,  0.1416,  0.7854,  4.7124,  3.1416,  1.5708]
    joint_names:
      - joint1
      - joint2
      - joint3
      - joint4
      - joint5
      - joint6
      - joint7
    ee_body: "link7"
    pin_ee_frame: "link7"
    pin_arm_q_indices: [0, 1, 2, 3, 4, 5, 6]
    ee_offset: [-0.1, 0.0, 0.05]

```

### teleop/hand_cfgs/ability.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 0.85
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1, 1.0, 1.0]
  mano_correction_vis: true

  target_joint_names:
    - thumb_q1
    - thumb_q2
    - index_q1
    - middle_q1
    - pinky_q1
    - ring_q1

  right:
    urdf_path: xarm+ability/ability_hand_right_large.urdf
    articulation_prefix: "multi_"
    wrist_link_name: "base"
    finger_tip_link_names:
      - thumb_anchor
      - index_anchor
      - middle_anchor
      - ring_anchor
      - pinky_anchor
    mano_to_pinocchio_rpy: [1.5708, 0, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: xarm+ability/ability_hand_left_large.urdf
    wrist_link_name: "base"
    finger_tip_link_names:
      - thumb_anchor
      - index_anchor
      - middle_anchor
      - ring_anchor
      - pinky_anchor
    mano_to_pinocchio_rpy: [-1.5708, 3.14, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/allegro.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.0
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0.0, -0.006, -0.18]
  hand_scale_xyz: [1.7, 1.5, 1.6]
  mano_correction_vis: true

  # Lock abd joints — extreme ranges cause optimizer to splay fingers
  joint_limits_override:
    joint_0.0: [0, 0]
    joint_4.0: [0, 0]
    joint_8.0: [0, 0]
    joint_3.0: [0, 0]
    joint_7.0: [0, 0]
    joint_11.0: [0, 0]
    joint_15.0: [0, 0]
    mult_joint_0.0: [0, 0]
    mult_joint_4.0: [0, 0]
    mult_joint_8.0: [0, 0]
    mult_joint_3.0: [0, 0]
    mult_joint_7.0: [0, 0]
    mult_joint_11.0: [0, 0]
    mult_joint_15.0: [0, 0]

  right:
    urdf_path: panda+allegro/allegro_hand_right.urdf
    articulation_prefix: "multi_"
    wrist_link_name: "base_link"
    finger_tip_link_names:
      - link_15.0_tip
      - link_3.0_tip
      - link_7.0_tip
      - link_11.0_tip
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 2.3]

  left:
    urdf_path: panda+allegro/allegro_hand_left.urdf
    articulation_prefix: ""
    wrist_link_name: "base_link"
    finger_tip_link_names:
      - link_15.0_tip
      - link_11.0_tip
      - link_7.0_tip
      - link_3.0_tip
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 2.3]

```

### teleop/hand_cfgs/dexhand021.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.07
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0.04, 0.0, -0.05]
  hand_scale_xyz: [1.5, 0.8, 1.2]
  mano_correction_vis: true

  right:
    urdf_path: jaka_zu7+dexhand021/urdf/Right_Hand.urdf
    wrist_link_name: "r_p_link4"
    finger_tip_link_names:
      - r_f_link1_tip
      - r_f_link2_tip
      - r_f_link3_tip
      - r_f_link4_tip
      - r_f_link5_tip
    mano_to_pinocchio_rpy: [1.5708, 0, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 3.12414]

  left:
    urdf_path: jaka_zu7+dexhand021/urdf/Left_Hand.urdf
    wrist_link_name: "l_p_link4"
    finger_tip_link_names:
      - l_f_link1_tip
      - l_f_link2_tip
      - l_f_link3_tip
      - l_f_link4_tip
      - l_f_link5_tip
    mano_to_pinocchio_rpy: [-1.5708, 0, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/leap.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.0
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1.5, 1.0, 1.2]
  mano_correction_vis: true

  wrist_link_name: "base"
  finger_tip_link_names:
    - thumb_tip_head
    - index_tip_head
    - middle_tip_head
    - ring_tip_head

  # Lock abd joints — extreme ranges cause optimizer to splay fingers.
  # URDF joint names are bare digits (0..15); IsaacLab prefixes them with
  # "multi_leap_r_" / "leap_l_" at sim time, but the override targets the URDF.
  joint_limits_override:
    "0": [0, 0]
    "4": [0, 0]
    "8": [0, 0]
    "14": [0, 1.9]

  right:
    urdf_path: xarm+leap/leap_hand_right.urdf
    articulation_prefix: "multi_leap_r_"
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: xarm+leap/leap_hand_left.urdf
    articulation_prefix: "leap_l_"
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/orca.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.22
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  
  hand_scale_xyz: [1.2, 1.0, 1.2]
  mano_correction_vis: true

  right:
    urdf_path: panda+orca/orcahand_right.urdf
    wrist_link_name: "right_tower"
    finger_tip_link_names:
      - right_thumb_fingertip
      - right_index_fingertip
      - right_middle_fingertip
      - right_ring_fingertip
      - right_pinky_fingertip
    mano_to_pinocchio_rpy: [1.5708, 0.0, 0.0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0.7]
    joint_limits_override:
      right_index_abd: [0, 0]
      right_middle_abd: [0, 0]
      right_ring_abd: [0, 0]
      right_pinky_abd: [0, 0]

    hand_offset_xyz: [0.04, 0.0, 0.03]

  left:
    urdf_path: panda+orca/orcahand_left.urdf
    wrist_link_name: "left_tower"
    finger_tip_link_names:
      - left_thumb_fingertip
      - left_index_fingertip
      - left_middle_fingertip
      - left_ring_fingertip
      - left_pinky_fingertip
    mano_to_pinocchio_rpy: [-1.5708, 3.14, 0.0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0.7]
    joint_limits_override:
      left_index_abd: [0, 0]
      left_middle_abd: [0, 0]
      left_ring_abd: [0, 0]
      left_pinky_abd: [0, 0]

    hand_offset_xyz: [-0.04, 0.0, 0.03]
```

### teleop/hand_cfgs/revo2.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.0
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1, 0.8, 0.8]
  mano_correction_vis: true
  ignore_mimic_joint: true

  right:
    urdf_path: rm_65+BrainCo/urdf/revo2_right_hand.urdf
    wrist_link_name: "right_base_link"
    finger_tip_link_names:
      - right_thumb_tip_link
      - right_index_tip_link
      - right_middle_tip_link
      - right_ring_tip_link
      - right_pinky_tip_link
    target_joint_names:
      - right_thumb_metacarpal_joint
      - right_thumb_proximal_joint
      - right_index_proximal_joint
      - right_middle_proximal_joint
      - right_ring_proximal_joint
      - right_pinky_proximal_joint
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: rm_65+BrainCo/urdf/revo2_left_hand.urdf
    wrist_link_name: "left_base_link"
    finger_tip_link_names:
      - left_thumb_tip_link
      - left_index_tip_link
      - left_middle_tip_link
      - left_ring_tip_link
      - left_pinky_tip_link
    target_joint_names:
      - left_thumb_metacarpal_joint
      - left_thumb_proximal_joint
      - left_index_proximal_joint
      - left_middle_proximal_joint
      - left_ring_proximal_joint
      - left_pinky_proximal_joint
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/rh56dfx.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.07
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0.04]
  hand_scale_xyz: [1, 1.0, 1.0]
  mano_correction_vis: true

  # Mimic joints are already handled in Isaac Sim USD, so ignore them in dex_retargeting
  ignore_mimic_joint: true

  right:
    urdf_path: ur5+RH56DFX/urdf/Right_Hand.urdf
    wrist_link_name: "r_base_link"
    finger_tip_link_names:
      - right_thumb_tip
      - right_index_tip
      - right_middle_tip
      - right_ring_tip
      - right_little_tip
    target_joint_names:
      - right_thumb_1_joint
      - right_thumb_2_joint
      - right_index_1_joint
      - right_middle_1_joint
      - right_ring_1_joint
      - right_little_1_joint
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: ur5+RH56DFX/urdf/Left_Hand.urdf
    wrist_link_name: "l_base_link"
    finger_tip_link_names:
      - left_thumb_tip
      - left_index_tip
      - left_middle_tip
      - left_ring_tip
      - left_little_tip
    target_joint_names:
      - left_thumb_1_joint
      - left_thumb_2_joint
      - left_index_1_joint
      - left_middle_1_joint
      - left_ring_1_joint
      - left_little_1_joint
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/rh5dg2.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.03
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1.7, 1.0, 1.2]
  mano_correction_vis: true

  right:
    urdf_path: ur5+RH5DG2/urdf/Right_Hand.urdf
    wrist_link_name: "right_hand_base"
    finger_tip_link_names:
      - right_thumb_force_sensor
      - right_index_force_sensor
      - right_middle_force_sensor
      - right_ring_force_sensor
      - right_pinky_force_sensor
    target_joint_names:
      - right_thumb_yaw_joint
      - right_thumb_mcp_joint
      - right_thumb_dip_joint
      - right_index_pitch_joint
      - right_index_mcp_joint
      - right_index_pip_joint
      - right_middle_pitch_joint
      - right_middle_mcp_joint
      - right_middle_pip_joint
      - right_ring_mcp_joint
      - right_ring_pip_joint
      - right_pinky_mcp_joint
      - right_pinky_pip_joint
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: ur5+RH5DG2/urdf/Left_Hand.urdf
    wrist_link_name: "left_hand_base"
    finger_tip_link_names:
      - left_thumb_force_sensor
      - left_index_force_sensor
      - left_middle_force_sensor
      - left_ring_force_sensor
      - left_pinky_force_sensor
    target_joint_names:
      - left_thumb_yaw_joint
      - left_thumb_mcp_joint
      - left_thumb_dip_joint
      - left_index_pitch_joint
      - left_index_mcp_joint
      - left_index_pip_joint
      - left_middle_pitch_joint
      - left_middle_mcp_joint
      - left_middle_pip_joint
      - left_ring_mcp_joint
      - left_ring_pip_joint
      - left_pinky_mcp_joint
      - left_pinky_pip_joint
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/schunk_svh.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.02
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1, 1.0, 1.0]
  mano_correction_vis: true

  finger_tip_link_names:
    - thtip
    - fftip
    - mftip
    - rftip
    - lftip

  right:
    urdf_path: ur5+schunk_hand/urdf/Right_Hand.urdf
    wrist_link_name: "right_hand_base_link"
    target_joint_names:
      - right_hand_Thumb_Opposition
      - right_hand_Thumb_Flexion
      - right_hand_Index_Finger_Proximal
      - right_hand_Index_Finger_Distal
      - right_hand_Finger_Spread
      - right_hand_Pinky
      - right_hand_Ring_Finger
      - right_hand_Middle_Finger_Proximal
      - right_hand_Middle_Finger_Distal
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: ur5+schunk_hand/urdf/Left_Hand.urdf
    wrist_link_name: "left_hand_base_link"
    target_joint_names:
      - left_hand_Thumb_Opposition
      - left_hand_Thumb_Flexion
      - left_hand_Index_Finger_Proximal
      - left_hand_Index_Finger_Distal
      - left_hand_Finger_Spread
      - left_hand_Pinky
      - left_hand_Ring_Finger
      - left_hand_Middle_Finger_Proximal
      - left_hand_Middle_Finger_Distal
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

### teleop/hand_cfgs/shadow.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.0
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0.01, 0.05]
  hand_scale_xyz: [1, 1.05, 0.9]
  mano_correction_vis: true

  joint_limits_override:
    THJ3: [0, 0]
    LFJ5: [0, 0]
    l_THJ3: [0, 0]
    l_LFJ5: [0, 0]

  right:
    urdf_path: ur5+shadow_hand/urdf/Right_Hand.urdf
    wrist_link_name: "palm"
    finger_tip_link_names:
      - thtip
      - fftip
      - mftip
      - rftip
      - lftip
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: ur5+shadow_hand/urdf/Left_Hand.urdf
    articulation_prefix: "l_"
    wrist_link_name: "palm"
    finger_tip_link_names:
      - thtip
      - fftip
      - mftip
      - rftip
      - lftip
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]
```

### teleop/hand_cfgs/sharpa.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.00
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [1, 1.0, 1.0]
  mano_correction_vis: true

  joint_limits_override:
    right_thumb_MCP_AA: [0, 0]
    right_pinky_CMC: [0, 0]
    left_thumb_MCP_AA: [0, 0]
    left_pinky_CMC: [0, 0]

  right:
    urdf_path: kuka+sharpa/right_sharpa_wave.urdf
    articulation_prefix: "multi_"
    wrist_link_name: "right_hand_C_MC"
    finger_tip_link_names:
      - right_thumb_fingertip
      - right_index_fingertip
      - right_middle_fingertip
      - right_ring_fingertip
      - right_pinky_fingertip
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: kuka+sharpa/left_sharpa_wave.urdf
    wrist_link_name: "left_hand_C_MC"
    finger_tip_link_names:
      - left_thumb_fingertip
      - left_index_fingertip
      - left_middle_fingertip
      - left_ring_fingertip
      - left_pinky_fingertip
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]
```

### teleop/hand_cfgs/wuji.yml

```yaml
retargeting:
  type: DexPilot
  scaling_factor: 1.0
  project_dist: 0.01
  escape_dist: 0.02
  low_pass_alpha: 0.2

  hand_offset_xyz: [0, 0, 0]
  hand_scale_xyz: [2.0, 1.0, 1.2]
  mano_correction_vis: true

  right:
    urdf_path: ur5+wuji/urdf/Right_Hand.urdf
    wrist_link_name: "right_palm_link"
    finger_tip_link_names:
      - right_finger1_tip_link
      - right_finger2_tip_link
      - right_finger3_tip_link
      - right_finger4_tip_link
      - right_finger5_tip_link
    mano_to_pinocchio_rpy: [1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

  left:
    urdf_path: ur5+wuji/urdf/Left_Hand.urdf
    wrist_link_name: "left_palm_link"
    finger_tip_link_names:
      - left_finger1_tip_link
      - left_finger2_tip_link
      - left_finger3_tip_link
      - left_finger4_tip_link
      - left_finger5_tip_link
    mano_to_pinocchio_rpy: [-1.5708, -1.5708, 0]
    sim_wrist_to_pin_root_rpy: [0, 0, 0]

```

## Python signatures and reward/observation bodies (483 files)


### benchmark/tests/test_scene_metric_config.py

```
def _official_scene_paths()
def test_official_scenes_declare_grasp_and_drop_tracked_objects()
def test_task44_metrics_follow_the_demonstrated_task_order_and_cover_both_payloads()
```

### benchmark/tests/test_task_12_success.py

```
def _state(x, y, z, lin, ang, quat)
def _task_states()
def test_hammer_near_and_fast_is_not_a_strike_without_block_response()
def test_strike_requires_nearby_swing_and_block_response()
def test_preplacement_hammer_motion_is_not_counted_after_tools_are_placed()
```

### collector/tacmap_configs.py

```
"""TacMap asset registry for supported tactile hands."""
class TacMapNpyGroup()
    """One TacMap surface map shared by one or more tactile sites."""
class TacMapHandCfg()
    """TacMap configuration for one robot hand embodiment."""
def resolve_tacmap_site_body_name(robot_key, site_name, robot_prim_path)
def _hand_sites(robot_key, suffix)
def _split_side_groups()
def _per_finger_groups()
def _sharpa_cfg()
def _generic_cfg()
def _per_finger_cfg()
def _schunk_site_body_overrides()
def _rh56dfx_site_body_overrides()
def _wuji_site_body_overrides()
def _allegro_site_body_overrides()
```

### collector/tacmap_sensor/sharpa_tacmap_cfg.py

```
class SharpaTacmapCfg(MultiMeshRayCasterCfg)
    """配置 Sharpa Vision-Based Tactile Sensor (VBTS)，支持并行环境及目标物体绑定"""
```

### policy/ACT/act_policy.py

```
class ACTPolicy(Module)
    def __init__(self, args_override, RoboTwin_Config)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
class ACT()
    def __init__(self, args_override, RoboTwin_Config)
    def pre_process(self, qpos)
    def post_process(self, action)
    def get_action(self, obs)
```

### policy/ACT/deploy_policy.py

```
def _maybe_select_active(qpos)
def _resolve_dims(usr_args)
def encode_obs(observation)
def get_model(usr_args)
def eval(TASK_ENV, model, observation)
def reset_model(model)
```

### policy/ACT/detr/main.py

```
def get_args_parser()
def build_ACT_model_and_optimizer(args_override, RoboTwin_Config)
def build_CNNMLP_model_and_optimizer(args_override)
```

### policy/ACT/detr/models/__init__.py

```
def build_ACT_model(args)
def build_CNNMLP_model(args)
```

### policy/ACT/detr/models/backbone.py

```
"""Backbone modules."""
class FrozenBatchNorm2d(Module)
    """BatchNorm2d where the batch statistics and the affine parameters are fixed.

Copy-paste from torchvision.misc.ops with added eps before rqsrt,
without which any other policy_models than torchvision.policy_models.resnet[18,34,50,101]
produce nans."""
    def __init__(self, n)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
    def forward(self, x)
class BackboneBase(Module)
    def __init__(self, backbone, train_backbone, num_channels, return_interm_layers)
    def forward(self, tensor)
class Backbone(BackboneBase)
    """ResNet backbone with frozen BatchNorm."""
    def __init__(self, name, train_backbone, return_interm_layers, dilation)
class Joiner(Sequential)
    def __init__(self, backbone, position_embedding)
    def forward(self, tensor_list)
def build_backbone(args)
```

### policy/ACT/detr/models/detr_vae.py

```
"""DETR model and criterion classes."""
def reparametrize(mu, logvar)
def get_sinusoid_encoding_table(n_position, d_hid)
class DETRVAE(Module)
    """This is the DETR module that performs object detection """
    def __init__(self, backbones, transformer, encoder, state_dim, num_queries, camera_names)
    def forward(self, qpos, image, env_state, actions, is_pad)
class CNNMLP(Module)
    def __init__(self, backbones, state_dim, camera_names)
    def forward(self, qpos, image, env_state, actions)
def mlp(input_dim, hidden_dim, output_dim, hidden_depth)
def build_encoder(args)
def build(args)
def build_cnnmlp(args)
```

### policy/ACT/detr/models/position_encoding.py

```
"""Various positional encodings for the transformer."""
class PositionEmbeddingSine(Module)
    """This is a more standard version of the position embedding, very similar to the one
used by the Attention is all you need paper, generalized to work on images."""
    def __init__(self, num_pos_feats, temperature, normalize, scale)
    def forward(self, tensor)
class PositionEmbeddingLearned(Module)
    """Absolute pos embedding, learned."""
    def __init__(self, num_pos_feats)
    def reset_parameters(self)
    def forward(self, tensor_list)
def build_position_encoding(args)
```

### policy/ACT/detr/models/transformer.py

```
"""DETR Transformer class.

Copy-paste from torch.nn.Transformer with modifications:
    * positional encodings are passed in MHattention
    * extra LN at the end of encoder is removed
    * decoder returns a stack of activations from all decoding layers"""
class Transformer(Module)
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout, activation, normalize_before, return_intermediate_dec)
    def _reset_parameters(self)
    def forward(self, src, mask, query_embed, pos_embed, latent_input, proprio_input, additional_pos_embed)
class TransformerEncoder(Module)
    def __init__(self, encoder_layer, num_layers, norm)
    def forward(self, src, mask, src_key_padding_mask, pos)
class TransformerDecoder(Module)
    def __init__(self, decoder_layer, num_layers, norm, return_intermediate)
    def forward(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
class TransformerEncoderLayer(Module)
    def __init__(self, d_model, nhead, dim_feedforward, dropout, activation, normalize_before)
    def with_pos_embed(self, tensor, pos)
    def forward_post(self, src, src_mask, src_key_padding_mask, pos)
    def forward_pre(self, src, src_mask, src_key_padding_mask, pos)
    def forward(self, src, src_mask, src_key_padding_mask, pos)
class TransformerDecoderLayer(Module)
    def __init__(self, d_model, nhead, dim_feedforward, dropout, activation, normalize_before)
    def with_pos_embed(self, tensor, pos)
    def forward_post(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
    def forward_pre(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
    def forward(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
def _get_clones(module, N)
def build_transformer(args)
def _get_activation_fn(activation)
```

### policy/ACT/detr/util/box_ops.py

```
"""Utilities for bounding box manipulation and GIoU."""
def box_cxcywh_to_xyxy(x)
def box_xyxy_to_cxcywh(x)
def box_iou(boxes1, boxes2)
def generalized_box_iou(boxes1, boxes2)
def masks_to_boxes(masks)
```

### policy/ACT/detr/util/misc.py

```
"""Misc functions, including distributed helpers.

Mostly copy-paste from torchvision references."""
class SmoothedValue(object)
    """Track a series of values and provide access to smoothed values over a
window or the global series average."""
    def __init__(self, window_size, fmt)
    def update(self, value, n)
    def synchronize_between_processes(self)
    def median(self)
    def avg(self)
    def global_avg(self)
    def max(self)
    def value(self)
    def __str__(self)
def all_gather(data)
def reduce_dict(input_dict, average)
class MetricLogger(object)
    def __init__(self, delimiter)
    def update(self)
    def __getattr__(self, attr)
    def __str__(self)
    def synchronize_between_processes(self)
    def add_meter(self, name, meter)
    def log_every(self, iterable, print_freq, header)
def get_sha()
def collate_fn(batch)
def _max_by_axis(the_list)
class NestedTensor(object)
    def __init__(self, tensors, mask)
    def to(self, device)
    def decompose(self)
    def __repr__(self)
def nested_tensor_from_tensor_list(tensor_list)
def _onnx_nested_tensor_from_tensor_list(tensor_list)
def setup_for_distributed(is_master)
def is_dist_avail_and_initialized()
def get_world_size()
def get_rank()
def is_main_process()
def save_on_master()
def init_distributed_mode(args)
def accuracy(output, target, topk)
def interpolate(input, size, scale_factor, mode, align_corners)
```

### policy/ACT/detr/util/plot_utils.py

```
"""Plotting utilities to visualize training logs."""
def plot_logs(logs, fields, ewm_col, log_name)
def plot_precision_recall(files, naming_scheme)
```

### policy/ACT/imitate_episodes.py

```
def main(args)
def make_policy(policy_class, policy_config)
def make_optimizer(policy_class, policy)
def forward_pass(data, policy)
def train_bc(train_dataloader, val_dataloader, config)
def plot_history(train_history, validation_history, num_epochs, ckpt_dir, seed)
```

### policy/ACT/utils.py

```
def _decode_jpeg(raw_bytes)
def _resolve_effective_length(h5file, total)
class Dex2BenchEpisodicDataset(Dataset)
    """Read dex2bench replay HDF5 files directly without pre-processing.

Format mapping:
  robot/qpos[t]                            → qpos observation
  action/commanded[t:t+chunk]              → action targets (BC: commanded qpos)
  cameras/<d2b_cam>/rgb[t]                 → image observation (JPEG vlen """
    def __init__(self, hdf5_paths, camera_names, norm_stats, max_action_len, active_dof_info)
    def __len__(self)
    def __getitem__(self, index)
def get_norm_stats_dex2bench(hdf5_paths, active_dof_info)
def load_dex2bench_data(dataset_dir, camera_names, batch_size_train, batch_size_val, val_ratio, only_success, use_active_dof, robot_key)
def compute_dict_mean(epoch_dicts)
def detach_dict(d)
def set_seed(seed)
```

### policy/ACT-Tactile/__init__.py

```
"""Tactile-aware ACT training, evaluation, and online deployment."""
```

### policy/ACT-Tactile/act/act_policy.py

```
class ACTPolicy(Module)
    def __init__(self, args_override, RoboTwin_Config)
    def __call__(self, qpos, image, actions, is_pad, tactile)
    def configure_optimizers(self)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
class ACT()
    def __init__(self, args_override, RoboTwin_Config)
    def pre_process(self, qpos)
    def post_process(self, action)
    def get_action(self, obs)
```

### policy/ACT-Tactile/act/deploy_policy.py

```
def _maybe_select_active(qpos)
def _resolve_dims(usr_args)
def encode_obs(observation)
def get_model(usr_args)
def eval(TASK_ENV, model, observation)
def reset_model(model)
```

### policy/ACT-Tactile/act/detr/main.py

```
def get_args_parser()
def build_ACT_model_and_optimizer(args_override, RoboTwin_Config)
def build_CNNMLP_model_and_optimizer(args_override)
```

### policy/ACT-Tactile/act/detr/models/__init__.py

```
def build_ACT_model(args, tactile_cfg)
def build_CNNMLP_model(args)
```

### policy/ACT-Tactile/act/detr/models/backbone.py

```
"""Backbone modules."""
class FrozenBatchNorm2d(Module)
    """BatchNorm2d where the batch statistics and the affine parameters are fixed.

Copy-paste from torchvision.misc.ops with added eps before rqsrt,
without which any other policy_models than torchvision.policy_models.resnet[18,34,50,101]
produce nans."""
    def __init__(self, n)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
    def forward(self, x)
class BackboneBase(Module)
    def __init__(self, backbone, train_backbone, num_channels, return_interm_layers)
    def forward(self, tensor)
class Backbone(BackboneBase)
    """ResNet backbone with frozen BatchNorm."""
    def __init__(self, name, train_backbone, return_interm_layers, dilation, in_channels)
class Joiner(Sequential)
    def __init__(self, backbone, position_embedding)
    def forward(self, tensor_list)
def build_backbone(args)
def build_tactile_backbone(args)
```

### policy/ACT-Tactile/act/detr/models/position_encoding.py

```
"""Various positional encodings for the transformer."""
class PositionEmbeddingSine(Module)
    """This is a more standard version of the position embedding, very similar to the one
used by the Attention is all you need paper, generalized to work on images."""
    def __init__(self, num_pos_feats, temperature, normalize, scale)
    def forward(self, tensor)
class PositionEmbeddingLearned(Module)
    """Absolute pos embedding, learned."""
    def __init__(self, num_pos_feats)
    def reset_parameters(self)
    def forward(self, tensor_list)
def build_position_encoding(args)
```

### policy/ACT-Tactile/act/detr/models/transformer.py

```
"""DETR Transformer class.

Copy-paste from torch.nn.Transformer with modifications:
    * positional encodings are passed in MHattention
    * extra LN at the end of encoder is removed
    * decoder returns a stack of activations from all decoding layers"""
class Transformer(Module)
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout, activation, normalize_before, return_intermediate_dec)
    def _reset_parameters(self)
    def forward(self, src, mask, query_embed, pos_embed, latent_input, proprio_input, additional_pos_embed, extra_src, extra_pos)
class TransformerEncoder(Module)
    def __init__(self, encoder_layer, num_layers, norm)
    def forward(self, src, mask, src_key_padding_mask, pos)
class TransformerDecoder(Module)
    def __init__(self, decoder_layer, num_layers, norm, return_intermediate)
    def forward(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
class TransformerEncoderLayer(Module)
    def __init__(self, d_model, nhead, dim_feedforward, dropout, activation, normalize_before)
    def with_pos_embed(self, tensor, pos)
    def forward_post(self, src, src_mask, src_key_padding_mask, pos)
    def forward_pre(self, src, src_mask, src_key_padding_mask, pos)
    def forward(self, src, src_mask, src_key_padding_mask, pos)
class TransformerDecoderLayer(Module)
    def __init__(self, d_model, nhead, dim_feedforward, dropout, activation, normalize_before)
    def with_pos_embed(self, tensor, pos)
    def forward_post(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
    def forward_pre(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
    def forward(self, tgt, memory, tgt_mask, memory_mask, tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
def _get_clones(module, N)
def build_transformer(args)
def _get_activation_fn(activation)
```

### policy/ACT-Tactile/act/detr/util/box_ops.py

```
"""Utilities for bounding box manipulation and GIoU."""
def box_cxcywh_to_xyxy(x)
def box_xyxy_to_cxcywh(x)
def box_iou(boxes1, boxes2)
def generalized_box_iou(boxes1, boxes2)
def masks_to_boxes(masks)
```

### policy/ACT-Tactile/act/detr/util/misc.py

```
"""Misc functions, including distributed helpers.

Mostly copy-paste from torchvision references."""
class SmoothedValue(object)
    """Track a series of values and provide access to smoothed values over a
window or the global series average."""
    def __init__(self, window_size, fmt)
    def update(self, value, n)
    def synchronize_between_processes(self)
    def median(self)
    def avg(self)
    def global_avg(self)
    def max(self)
    def value(self)
    def __str__(self)
def all_gather(data)
def reduce_dict(input_dict, average)
class MetricLogger(object)
    def __init__(self, delimiter)
    def update(self)
    def __getattr__(self, attr)
    def __str__(self)
    def synchronize_between_processes(self)
    def add_meter(self, name, meter)
    def log_every(self, iterable, print_freq, header)
def get_sha()
def collate_fn(batch)
def _max_by_axis(the_list)
class NestedTensor(object)
    def __init__(self, tensors, mask)
    def to(self, device)
    def decompose(self)
    def __repr__(self)
def nested_tensor_from_tensor_list(tensor_list)
def _onnx_nested_tensor_from_tensor_list(tensor_list)
def setup_for_distributed(is_master)
def is_dist_avail_and_initialized()
def get_world_size()
def get_rank()
def is_main_process()
def save_on_master()
def init_distributed_mode(args)
def accuracy(output, target, topk)
def interpolate(input, size, scale_factor, mode, align_corners)
```

### policy/ACT-Tactile/act/detr/util/plot_utils.py

```
"""Plotting utilities to visualize training logs."""
def plot_logs(logs, fields, ewm_col, log_name)
def plot_precision_recall(files, naming_scheme)
```

### policy/ACT-Tactile/act/imitate_episodes.py

```
def main(args)
def make_policy(policy_class, policy_config)
def make_optimizer(policy_class, policy)
def forward_pass(data, policy)
def train_bc(train_dataloader, val_dataloader, config)
def plot_history(train_history, validation_history, num_epochs, ckpt_dir, seed)
```

### policy/ACT-Tactile/act/utils.py

```
def _decode_jpeg(raw_bytes)
def _resolve_effective_length(h5file, total)
class Dex2BenchEpisodicDataset(Dataset)
    """Read dex2bench replay HDF5 files directly without pre-processing.

Format mapping:
  robot/qpos[t]                            → qpos observation
  action/commanded[t:t+chunk]              → action targets (BC: commanded qpos)
  cameras/<d2b_cam>/rgb[t]                 → image observation (JPEG vlen """
    def __init__(self, hdf5_paths, camera_names, norm_stats, max_action_len, active_dof_info)
    def __len__(self)
    def __getitem__(self, index)
def get_norm_stats_dex2bench(hdf5_paths, active_dof_info)
def load_dex2bench_data(dataset_dir, camera_names, batch_size_train, batch_size_val, val_ratio, only_success, use_active_dof, robot_key)
def compute_dict_mean(epoch_dicts)
def detach_dict(d)
def set_seed(seed)
```

### policy/ACT-Tactile/act_tactile_dataset.py

```
"""ACT episode dataset with an aligned ordered TacMap observation."""
def _read_site_names(h5file, path)
class ActTactileEpisodicDataset(Dex2BenchEpisodicDataset)
    """Keep ACT sampling exactly intact and append aligned raw TacMap frames.

The output is a 5-tuple ``(image_data, qpos_data, action_data, is_pad, tactile)``
where the first four values match :class:`Dex2BenchEpisodicDataset` under the
same NumPy random state, and ``tactile`` is ``uint8 [num_sites, 1, H"""
    def __init__(self, hdf5_paths, camera_names, norm_stats, max_action_len, active_dof_info)
    def _validate_tactile_schema(self)
    def __getitem__(self, index)
```

### policy/ACT-Tactile/act_tactile_model.py

```
"""Tactile-only policy built from the private copy of ACT.

This module deliberately imports only :mod:`policy.tactile_policy.act`; the
upstream ``policy.ACT`` package remains an untouched reference implementation."""
class TactileACTConfig()
    def __post_init__(self)
    def to_dict(self)
    def from_dict(cls, values)
class TactileACTModel(Module)
    """The copied ACT DETRVAE with TacMap tokens enabled unconditionally."""
    def __init__(self, config)
    def num_queries(self)
    def forward(self, qpos, images, tactile, actions, is_pad)
def build_optimizer(model)
```

### policy/ACT-Tactile/dataset.py

```
"""Dex2Bench HDF5 loading for the tactile-aware ACT policy."""
class TactileSchemaError(ValueError)
    """Raised when an episode cannot satisfy the tactile policy data contract."""
class EpisodeSchema()
    """Validated metadata needed to load one HDF5 episode."""
class FrameRef()
    """A frame inside an inspected episode."""
class NormalizationStats()
    """Per-dimension qpos and action normalization statistics."""
    def state_dim(self)
    def as_dict(self)
    def from_dict(cls, values)
def _decode_string(value)
def _read_optional_bool(h5, key)
def _require_dataset(h5, key, path)
def _effective_length(h5, frame_count)
def inspect_episode(path)
def make_frame_refs(episodes)
def split_frame_refs(episodes)
def _select_columns(array, schema)
def compute_normalization_stats(episodes, frame_refs)
def _decode_jpeg(raw)
class TactileEpisodeDataset(Dataset)
    """Frame-indexed RGB, qpos, TacMap, and action-chunk dataset."""
    def __init__(self, episodes, frame_refs, stats)
    def _build_tactile_refs(self, seed)
    def __len__(self)
    def _load_images(self, h5, schema, frame_index)
    def _load_tactile(self, ref)
    def __getitem__(self, index)
def inspect_dataset_directory(dataset_dir)
def failed_demo_warnings(episodes)
```

### policy/ACT-Tactile/deploy_policy.py

```
"""Checkpoint-backed online inference adapter for the tactile ACT policy."""
def resolve_tactile_checkpoint(checkpoint_or_dir, checkpoint_name)
class TactilePolicyDeployment()
    """Prepare online RGB/TacMap observations and return physical actions."""
    def __init__(self, checkpoint_or_dir)
    def state_dim(self)
    def chunk_size(self)
    def enable_tactile_attention_capture(self)
    def last_tactile_attention_weights(self)
    def last_modality_attention(self)
    def _validate_checkpoint_metadata(self)
    def validate_runtime(self, robot_key, active_indices, active_joint_names)
    def resolve_tactile_sensor_settings(self, resolution_step, max_distance_m)
    def _require_mapping(observation, key)
    def _require_channels(values, names, label)
    def _encode_images(self, images_by_name)
    def _encode_tactile(self, tactile_by_name)
    def encode_observation(self, observation)
    def _predict_action_chunk(self, observation)
    def _aggregate_current_action(self, action_chunk)
    def get_action(self, observation)
    def reset(self)

```python
def encode_observation(
        self,
        observation: Mapping,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Convert one raw online observation into checkpoint-ordered tensors."""

        qpos = np.asarray(observation.get("qpos"), dtype=np.float32).reshape(-1)
        if qpos.shape != (self.state_dim,):
            raise ValueError(
                f"qpos must contain {self.state_dim} active values, got shape {qpos.shape}"
            )
        if not np.isfinite(qpos).all():
            raise ValueError("qpos contains non-finite values")
        normalized_qpos = (qpos - self.stats.qpos_mean) / self.stats.qpos_std
        images = self._encode_images(self._require_mapping(observation, "images"))
        tactile = self._encode_tactile(self._require_mapping(observation, "tactile"))
        return (
            torch.from_numpy(np.ascontiguousarray(normalized_qpos))[None].to(self.device),
            torch.from_numpy(np.ascontiguousarray(images))[None].to(self.device),
            torch.from_numpy(np.ascontiguousarray(tactile))[None].to(self.device),
        )
```
```

### policy/ACT-Tactile/offline_eval.py

```
"""Compare normal, zeroed, and temporally shuffled TacMap inputs offline."""
def evaluate_ablation_loaders(policy, loaders, device)
def _loader(dataset, batch_size, num_workers)
def evaluate_checkpoint(checkpoint, dataset_dir)
def build_arg_parser()
def main()
```

### policy/ACT-Tactile/tactile_policy.py

```
"""Loss and inference wrapper for the tactile-only private ACT copy."""
class TactileACTPolicy(Module)
    """Compute ACT's masked L1 plus conditional-VAE KL objective."""
    def __init__(self, config)
    def compute_loss(self, batch)
    def predict(self, qpos, images, tactile)
    def forward(self, batch)
    def configure_optimizer(self)
```

### policy/ACT-Tactile/tactile_run_policy.py

```
"""Run a trained tactile ACT policy in Isaac Sim for evaluation.

This standalone runner mirrors ``run_policy.py`` while adding real-time TacMap
capture.  It consumes four RGB cameras plus the checkpoint-defined tactile sites
and does not modify the ACT/DP/REMOTE evaluation path.

Usage (manus env):
    cd .
    python policy/ACT-Tactile/tactile_run_policy.py         --task scenes/06_fruit_bowl_loading.yaml         --ckpt-dir outputs/logs/tactile/task06-sharpa         --enable-rgb

    # headless mode:
    python policy/ACT-Tactile/tactile_run_policy.py         --task scenes/06_fruit_bowl_loading"""
def _normalize_generalization_profile(profile)
def _mapping(raw)
def _normalize_generalization_split(split)
def _apply_generalization_split(raw)
def _apply_generalization_profile(raw)
def _seed_everything(seed)
def _episode_seed(base_seed, episode_idx)
def _robustness_category(sample)
def _validate_camera_config(camera_cfgs, policy)
def _format_mib(num_bytes)
def _resolve_robot_key_from_ckpt_dir(ckpt_dir)
def _process_rss_bytes()
def _log_memory(label, device)
def _compact_episode_result(result)
def _require_tactile_gpu(device)
def _load_tactile_policy(args)
def _load_act_policy(args)
def _load_dp_policy(args)
def _load_remote_policy(args)
def _load_policy(args)
def _preprocess_image(rgb_hwc)
def _policy_qpos(robot_art, robot_state)
def _joint_command_context(robot_art, raw_action, full_target)
def _build_policy_obs(frames, robot_art, policy_type)
def _validate_tactile_rig(policy, tactile_rig)
def _close_sensor_rigs(camera_rig, tactile_rig)
class _EpisodeSensorOwner()
    """Own both sensor rigs so one outer finally covers their full lifetime."""
    def __init__(self)
    def close(self)
def _build_tactile_policy_obs(frames, tactile_capture, robot_art, policy)
def _camera_frame_issue(frame)
def _capture_complete_camera_set(camera_rig, sim, physics_dt)
def _render_camera_sample(sim, camera_rig)
def _step_sim_with_mounted_camera_sync(sim, camera_rig, interactive_objects, physics_dt)
def _split_legacy_joint_action(qpos)
def _build_remote_policy_obs(frames, robot_art)
def _refresh_observation_joint_state(obs, robot_art)
def _load_success_checker(task)
def _get_object_states(interactive_objects, object_ids)
def _metrics_spec_for_episode(metrics_spec, runtime)
def _reset_policy(policy)
def _start_stdin_skip_listener()
def _log_tactile_attention(path, episode_idx, policy_step, weights)
def _log_modality_attention(path, episode_idx, policy_step, proportions)
def _run_episode_impl(sim, runtime, camera_cfgs, camera_generalization_sample, policy, physics_dt, args, episode_idx, episode_seed, base_seed, scene_generalization_sample, seed_policy, check_success_fn, metrics_spec, perturbation_axis, robot_key, task_instruction, _sensor_owner)
def _run_episode()
def main()

```python
def _refresh_observation_joint_state(
    obs: dict,
    robot_art,
    *,
    robot_state: dict | None = None,
) -> dict:
    qpos = _policy_qpos(robot_art, robot_state)
    refreshed = dict(obs)
    if "agent_pos" in refreshed:
        refreshed["qpos"] = qpos
        refreshed["agent_pos"] = qpos
        return refreshed

    refreshed["joint_action"] = _split_legacy_joint_action(qpos)
    return refreshed
```
```

### policy/ACT-Tactile/tests/__init__.py

```
"""Source-only regression tests for ACT-Tactile."""
```

### policy/ACT-Tactile/tests/test_runner_relocation.py

```
"""Regression tests for keeping the tactile runner inside ACT-Tactile."""
def _bash_major(executable)
def _find_bash4()
class RunnerRelocationTests(TestCase)
    def test_tactile_runner_is_policy_local_only(self)
    def test_wrapper_uses_policy_local_runner_at_both_execution_sites(self)
    def test_wrapper_checks_for_bash4_before_array_logic(self)
    def test_bash3_fails_at_version_preflight_without_environment(self)
    def test_wrapper_from_external_cwd_forwards_to_absolute_local_runner(self)
    def test_readme_documents_bash4_wrapper_requirement(self)
    def test_runner_bootstraps_repo_before_repo_local_imports(self)
    def test_runner_dynamically_imports_act_tactile_deployment(self)
    def test_ordinary_act_wrapper_still_uses_root_runner(self)
```

### policy/ACT-Tactile/train.py

```
"""Train the tactile-aware ACT policy on Dex2Bench HDF5 episodes."""
def set_seed(seed)
def _move_batch(batch, device)
def train_step(policy, optimizer, batch, device)
def evaluate_loader(policy, loader, device)
def _stats_to_lists(stats)
def _tactile_sensor_metadata(episode)
def save_checkpoint(path)
def _torch_load(path, device)
def load_checkpoint(path)
def _make_loader(dataset)
def _mean_metrics(metrics)
def run_training(args)
def build_arg_parser()
def main()
```

### policy/DP/deploy_policy.py

```
def _maybe_select_active(qpos)
def _observation_root(observation)
def _encode_camera(observation, candidates)
def encode_obs(observation)
def get_model(usr_args)
def _model_call(model, func_name, obs)
def eval(TASK_ENV, model, observation)
def reset_model(model)

```python
def _observation_root(observation):
    return observation.get("observation", observation)
```
```

### policy/DP/diffusion_policy/common/checkpoint_util.py

```
class TopKCheckpointManager()
    def __init__(self, save_dir, monitor_key, mode, k, format_str)
    def get_ckpt_path(self, data)
```

### policy/DP/diffusion_policy/common/cv2_util.py

```
def draw_reticle(img, u, v, label_color)
def draw_text(img)
def get_image_transform(input_res, output_res, bgr_to_rgb)
def optimal_row_cols(n_cameras, in_wh_ratio, max_resolution)
```

### policy/DP/diffusion_policy/common/env_util.py

```
def render_env_video(env, states, actions)
```

### policy/DP/diffusion_policy/common/json_logger.py

```
def read_json_log(path, required_keys)
class JsonLogger()
    def __init__(self, path, filter_fn)
    def start(self)
    def stop(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def log(self, data)
    def get_last_log(self)
```

### policy/DP/diffusion_policy/common/nested_dict_util.py

```
def nested_dict_map(f, x)
def nested_dict_reduce(f, x)
def nested_dict_check(f, x)
```

### policy/DP/diffusion_policy/common/normalize_util.py

```
def get_range_normalizer_from_stat(stat, output_max, output_min, range_eps)
def get_image_range_normalizer()
def get_identity_normalizer_from_stat(stat)
def robomimic_abs_action_normalizer_from_stat(stat, rotation_transformer)
def robomimic_abs_action_only_normalizer_from_stat(stat)
def robomimic_abs_action_only_dual_arm_normalizer_from_stat(stat)
def array_to_stats(arr)
```

### policy/DP/diffusion_policy/common/pose_trajectory_interpolator.py

```
def rotation_distance(a, b)
def pose_distance(start_pose, end_pose)
class PoseTrajectoryInterpolator()
    def __init__(self, times, poses)
    def times(self)
    def poses(self)
    def trim(self, start_t, end_t)
    def drive_to_waypoint(self, pose, time, curr_time, max_pos_speed, max_rot_speed)
    def schedule_waypoint(self, pose, time, max_pos_speed, max_rot_speed, curr_time, last_waypoint_time)
    def __call__(self, t)
```

### policy/DP/diffusion_policy/common/precise_sleep.py

```
def precise_sleep(dt, slack_time, time_func)
def precise_wait(t_end, slack_time, time_func)
```

### policy/DP/diffusion_policy/common/pymunk_override.py

```
"""This submodule contains helper functions to help with quick prototyping
using pymunk together with pygame.

Intended to help with debugging and prototyping, not for actual production use
in a full application. The methods contained in this module is opinionated
about your coordinate system and not in any way optimized."""
class DrawOptions(SpaceDebugDrawOptions)
    def __init__(self, surface)
    def draw_circle(self, pos, angle, radius, outline_color, fill_color)
    def draw_segment(self, a, b, color)
    def draw_fat_segment(self, a, b, radius, outline_color, fill_color)
    def draw_polygon(self, verts, radius, outline_color, fill_color)
    def draw_dot(self, size, pos, color)
def get_mouse_pos(surface)
def to_pygame(p, surface)
def from_pygame(p, surface)
def light_color(color)
```

### policy/DP/diffusion_policy/common/pymunk_util.py

```
def get_body_type(static)
def create_rectangle(space, pos_x, pos_y, width, height, density, static)
def create_rectangle_bb(space, left, bottom, right, top)
def create_circle(space, pos_x, pos_y, radius, density, static)
def get_body_state(body)
```

### policy/DP/diffusion_policy/common/pytorch_util.py

```
def dict_apply(x, func)
def pad_remaining_dims(x, target)
def dict_apply_split(x, split_func)
def dict_apply_reduce(x, reduce_func)
def replace_submodules(root_module, predicate, func)
def optimizer_to(optimizer, device)
```

### policy/DP/diffusion_policy/common/replay_buffer.py

```
def check_chunks_compatible(chunks, shape)
def rechunk_recompress_array(group, name, chunks, chunk_length, compressor, tmp_key)
def get_optimal_chunks(shape, dtype, target_chunk_bytes, max_chunk_length)
class ReplayBuffer()
    """Zarr-based temporal datastructure.
Assumes first dimension to be time. Only chunk in time dimension."""
    def __init__(self, root)
    def create_empty_zarr(cls, storage, root)
    def create_empty_numpy(cls)
    def create_from_group(cls, group)
    def create_from_path(cls, zarr_path, mode)
    def copy_from_store(cls, src_store, store, keys, chunks, compressors, if_exists)
    def copy_from_path(cls, zarr_path, backend, store, keys, chunks, compressors, if_exists)
    def save_to_store(self, store, chunks, compressors, if_exists)
    def save_to_path(self, zarr_path, chunks, compressors, if_exists)
    def resolve_compressor(compressor)
    def _resolve_array_compressor(cls, compressors, key, array)
    def _resolve_array_chunks(cls, chunks, key, array)
    def data(self)
    def meta(self)
    def update_meta(self, data)
    def episode_ends(self)
    def get_episode_idxs(self)
    def backend(self)
    def __repr__(self)
    def keys(self)
    def values(self)
    def items(self)
    def __getitem__(self, key)
    def __contains__(self, key)
    def n_steps(self)
    def n_episodes(self)
    def chunk_size(self)
    def episode_lengths(self)
    def add_episode(self, data, chunks, compressors)
    def drop_episode(self)
    def pop_episode(self)
    def extend(self, data)
    def get_episode(self, idx, copy)
    def get_episode_slice(self, idx)
    def get_steps_slice(self, start, stop, step, copy)
    def get_chunks(self)
    def set_chunks(self, chunks)
    def get_compressors(self)
    def set_compressors(self, compressors)
```

### policy/DP/diffusion_policy/common/robomimic_config_util.py

```
def get_robomimic_config(algo_name, hdf5_type, task_name, dataset_type)
```

### policy/DP/diffusion_policy/common/robomimic_util.py

```
class RobomimicAbsoluteActionConverter()
    def __init__(self, dataset_path, algo_name)
    def __len__(self)
    def convert_actions(self, states, actions)
    def convert_idx(self, idx)
    def convert_and_eval_idx(self, idx)
    def evaluate_rollout_error(env, states, actions, robot0_eef_pos, robot0_eef_quat, metric_skip_steps)
```

### policy/DP/diffusion_policy/common/sampler.py

```
def create_indices(episode_ends, sequence_length, episode_mask, pad_before, pad_after, debug)
def get_val_mask(n_episodes, val_ratio, seed)
def downsample_mask(mask, max_n, seed)
class SequenceSampler()
    def __init__(self, replay_buffer, sequence_length, pad_before, pad_after, keys, key_first_k, episode_mask)
    def __len__(self)
    def sample_sequence(self, idx)
```

### policy/DP/diffusion_policy/common/timestamp_accumulator.py

```
def get_accumulate_timestamp_idxs(timestamps, start_time, dt, eps, next_global_idx, allow_negative)
def align_timestamps(timestamps, target_global_idxs, start_time, dt, eps)
class TimestampObsAccumulator()
    def __init__(self, start_time, dt, eps)
    def __len__(self)
    def data(self)
    def actual_timestamps(self)
    def timestamps(self)
    def put(self, data, timestamps)
class TimestampActionAccumulator()
    def __init__(self, start_time, dt, eps)
    def __len__(self)
    def actions(self)
    def actual_timestamps(self)
    def timestamps(self)
    def put(self, actions, timestamps)
```

### policy/DP/diffusion_policy/dataset/base_dataset.py

```
class BaseLowdimDataset(Dataset)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
class BaseImageDataset(Dataset)
    def get_validation_dataset(self)
    def get_normalizer(self)
    def get_all_actions(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### policy/DP/diffusion_policy/dataset/dex2scene_hdf5_dataset.py

```
class _SampleIndex()
def _as_bytes(raw)
def _decode_rgb(raw)
def _resize_rgb(img)
def _fill_nan_action_rows(action, qpos)
def _resolve_effective_length(h5file, total)
def _make_val_mask(n_episodes, val_ratio)
def _build_indices(lengths, episode_mask)
class Dex2SceneHdf5Dataset(BaseImageDataset)
    """Read dex2scene replay HDF5 episodes directly for image diffusion policy."""
    def __init__(self, dataset_dir, horizon, pad_before, pad_after, seed, val_ratio, batch_size, max_train_episodes, camera_obs_map, image_shape, episode_mask, _val_mask, use_active_dof, robot_key, n_obs_steps)
    def _episode_length(path)
    def get_validation_dataset(self)
    def __len__(self)
    def _read_camera_frame(self, rgb_ds, frame_idx)
    def _read_camera_sequence(self, f, camera_id, index)
    def _pad_sequence(self, arr, index)
    def _sample_one(self, sample_idx)
    def __getitem__(self, idx)
    def _load_all_state_action(self)
    def get_normalizer(self, mode)
    def get_all_actions(self)
    def postprocess(self, samples, device)
```

### policy/DP/diffusion_policy/dataset/dex2scene_zarr_dataset.py

```
"""Zarr-backed dataset for dex2scene DP training.

Reads a preprocessed Zarr store (created by process_hdf5_to_zarr.py) with
zero JPEG-decode overhead.  Matches the HDF5 dataset's output dict format
exactly, so the workspace, normalizer, and deploy code need no changes."""
class Dex2SceneZarrDataset(BaseImageDataset)
    """Dataset that reads pre-decoded camera frames from a Zarr store.

Parameters
----------
zarr_path : str
    Path to the ``.zarr`` directory produced by ``process_hdf5_to_zarr.py``.
horizon : int
    Sequence length (= n_obs_steps for past + pred horizon).
pad_before : int
    Pad frames before the ep"""
    def __init__(self, zarr_path, horizon, pad_before, pad_after, seed, val_ratio, batch_size, max_train_episodes, obs_camera_keys, n_obs_steps, episode_mask, _val_mask)
    def get_validation_dataset(self)
    def get_normalizer(self, mode)
    def __len__(self)
    def __getitem__(self, idx)
    def postprocess(self, samples, device)
```

### policy/DP/diffusion_policy/dataset/obs_step_util.py

```
def trim_observation_steps(samples)

```python
def trim_observation_steps(
    samples: Mapping[str, Any],
    *,
    n_obs_steps: int | None,
    obs_camera_keys: Iterable[str],
) -> dict[str, Any]:
    """Trim observation tensors to n_obs_steps while keeping action horizon intact."""
    if n_obs_steps is None:
        return dict(samples)
    n_obs_steps = int(n_obs_steps)
    if n_obs_steps <= 0:
        raise ValueError(f"n_obs_steps must be positive or None, got {n_obs_steps}")

    result = dict(samples)
    for key in obs_camera_keys:
        if key in result:
            result[key] = result[key][:n_obs_steps]
    if "state" in result:
        result["state"] = result["state"][:n_obs_steps]
    return result
```
```

### policy/DP/diffusion_policy/env_runner/dp_runner.py

```
class DPRunner()
    def __init__(self, eval_episodes, max_steps, n_obs_steps, n_action_steps, fps, crf, tqdm_interval_sec, task_name)
    def stack_last_n_obs(self, all_obs, n_steps)
    def reset_obs(self)
    def update_obs(self, current_obs)
    def get_n_steps_obs(self)
    def get_action(self, policy, observaton)
```

### policy/DP/diffusion_policy/model/bet/action_ae/__init__.py

```
class AbstractActionAE(SaveModule, ABC)
    def fit_model(self, input_dataloader, eval_dataloader, obs_encoding_net)
    def encode_into_latent(self, input_action, input_rep)
    def decode_actions(self, latent_action_batch, input_rep_batch)
    def num_latents(self)
```

### policy/DP/diffusion_policy/model/bet/action_ae/discretizers/k_means.py

```
class KMeansDiscretizer(DictOfTensorMixin)
    """Simplified and modified version of KMeans algorithm  from sklearn."""
    def __init__(self, action_dim, num_bins, predict_offsets)
    def fit_discretizer(self, input_actions)
    def suggested_actions(self)
    def _kmeans(cls, x, ncluster, niter)
    def encode_into_latent(self, input_action, input_rep)
    def decode_actions(self, latent_action_batch, input_rep_batch)
    def discretized_space(self)
    def latent_dim(self)
    def num_latents(self)
```

### policy/DP/diffusion_policy/model/bet/latent_generators/latent_generator.py

```
class AbstractLatentGenerator(ABC, SaveModule)
    """Abstract class for a generative model that can generate latents given observation representations.

In the probabilisitc sense, this model fits and samples from P(latent|observation) given some observation."""
    def get_latent_and_loss(self, obs_rep, target_latents, seq_masks)
    def generate_latents(self, seq_obses, seq_masks)
    def get_optimizer(self, weight_decay, learning_rate, betas)
class LatentGeneratorDataParallel(DataParallel)
    def get_latent_and_loss(self)
    def generate_latents(self)
    def get_optimizer(self)
```

### policy/DP/diffusion_policy/model/bet/latent_generators/mingpt.py

```
class MinGPT(AbstractLatentGenerator)
    def __init__(self, input_dim, n_layer, n_head, n_embd, embd_pdrop, resid_pdrop, attn_pdrop, block_size, vocab_size, latent_dim, action_dim, discrete_input, predict_offsets, offset_loss_scale, focal_loss_gamma)
    def get_latent_and_loss(self, obs_rep, target_latents, seq_masks, return_loss_components)
    def generate_latents(self, obs_rep)
    def get_optimizer(self, weight_decay, learning_rate, betas)
```

### policy/DP/diffusion_policy/model/bet/latent_generators/transformer.py

```
class Transformer(AbstractLatentGenerator)
    def __init__(self, input_dim, num_bins, action_dim, horizon, focal_loss_gamma, offset_loss_scale)
    def get_optimizer(self)
    def get_latent_and_loss(self, obs_rep, target_latents, return_loss_components)
    def generate_latents(self, obs_rep)
```

### policy/DP/diffusion_policy/model/bet/libraries/loss_fn.py

```
def soft_cross_entropy(input, target)
class FocalLoss(Module)
    """Focal Loss, as described in https://arxiv.org/abs/1708.02002.
It is essentially an enhancement to cross entropy loss and is
useful for classification tasks when there is a large class imbalance.
x is expected to contain raw, unnormalized scores for each class.
y is expected to contain class labels.
"""
    def __init__(self, alpha, gamma, reduction, ignore_index)
    def __repr__(self)
    def forward(self, x, y)
def focal_loss(alpha, gamma, reduction, ignore_index, device, dtype)
```

### policy/DP/diffusion_policy/model/bet/libraries/mingpt/model.py

```
"""GPT model:
- the initial stem consists of a combination of token encoding and a positional encoding
- the meat of it is a uniform sequence of Transformer blocks
    - each Transformer is a sequential combination of a 1-hidden-layer MLP block and a self-attention block
    - all blocks feed into a central residual pathway similar to resnets
- the final decoder is a linear projection into a vanilla Softmax classifier"""
class GPTConfig()
    """base GPT config, params common to all GPT versions"""
    def __init__(self, vocab_size, block_size)
class GPT1Config(GPTConfig)
    """GPT-1 like network roughly 125M params"""
class CausalSelfAttention(Module)
    """A vanilla multi-head masked self-attention layer with a projection at the end.
It is possible to use torch.nn.MultiheadAttention here but I am including an
explicit implementation here to show that there is nothing too scary here."""
    def __init__(self, config)
    def forward(self, x)
class Block(Module)
    """an unassuming Transformer block"""
    def __init__(self, config)
    def forward(self, x)
class GPT(Module)
    """the full GPT language model, with a context size of block_size"""
    def __init__(self, config)
    def get_block_size(self)
    def _init_weights(self, module)
    def configure_optimizers(self, train_config)
    def forward(self, idx, targets)
```

### policy/DP/diffusion_policy/model/bet/libraries/mingpt/trainer.py

```
"""Simple training loop; Boilerplate that could apply to any arbitrary neural network,
so nothing in this file really has anything to do with GPT specifically."""
class TrainerConfig()
    def __init__(self)
class Trainer()
    def __init__(self, model, train_dataset, test_dataset, config)
    def save_checkpoint(self)
    def train(self)
```

### policy/DP/diffusion_policy/model/bet/libraries/mingpt/utils.py

```
def set_seed(seed)
def top_k_logits(logits, k)
def sample(model, x, steps, temperature, sample, top_k)
```

### policy/DP/diffusion_policy/model/bet/utils.py

```
def mlp(input_dim, hidden_dim, output_dim, hidden_depth, output_mod)
class eval_mode()
    def __init__(self)
    def __enter__(self)
    def __exit__(self)
def freeze_module(module)
def set_seed_everywhere(seed)
def shuffle_along_axis(a, axis)
def transpose_batch_timestep()
class TrainWithLogger()
    def reset_log(self)
    def log_append(self, log_key, length, loss_components)
    def flush_log(self, epoch, iterator)
class SaveModule(Module)
    def set_snapshot_path(self, path)
    def save_snapshot(self)
    def load_snapshot(self)
def split_datasets(dataset, train_fraction, random_seed)
```

### policy/DP/diffusion_policy/model/common/dict_of_tensor_mixin.py

```
class DictOfTensorMixin(Module)
    def __init__(self, params_dict)
    def device(self)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
```

### policy/DP/diffusion_policy/model/common/lr_scheduler.py

```
def get_scheduler(name, optimizer, num_warmup_steps, num_training_steps)
```

### policy/DP/diffusion_policy/model/common/module_attr_mixin.py

```
class ModuleAttrMixin(Module)
    def __init__(self)
    def device(self)
    def dtype(self)
```

### policy/DP/diffusion_policy/model/common/normalizer.py

```
class LinearNormalizer(DictOfTensorMixin)
    def fit(self, data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
    def __call__(self, x)
    def __getitem__(self, key)
    def __setitem__(self, key, value)
    def _normalize_impl(self, x, forward)
    def normalize(self, x)
    def unnormalize(self, x)
    def get_input_stats(self)
    def get_output_stats(self, key)
class SingleFieldLinearNormalizer(DictOfTensorMixin)
    def fit(self, data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
    def create_fit(cls, data)
    def create_manual(cls, scale, offset, input_stats_dict)
    def create_identity(cls, dtype)
    def normalize(self, x)
    def unnormalize(self, x)
    def get_input_stats(self)
    def get_output_stats(self)
    def __call__(self, x)
def _fit(data, last_n_dims, dtype, mode, output_max, output_min, range_eps, fit_offset)
def _normalize(x, params, forward)
def test()
```

### policy/DP/diffusion_policy/model/common/rotation_transformer.py

```
class RotationTransformer()
    def __init__(self, from_rep, to_rep, from_convention, to_convention)
    def _apply_funcs(x, funcs)
    def forward(self, x)
    def inverse(self, x)
def test()
```

### policy/DP/diffusion_policy/model/common/shape_util.py

```
def get_module_device(m)
def get_output_shape(input_shape, net)
```

### policy/DP/diffusion_policy/model/common/tensor_util.py

```
"""A collection of utilities for working with nested tensor structures consisting
of numpy arrays and torch tensors."""
def recursive_dict_list_tuple_apply(x, type_func_dict)
def map_tensor(x, func)
def map_ndarray(x, func)
def map_tensor_ndarray(x, tensor_func, ndarray_func)
def clone(x)
def detach(x)
def to_batch(x)
def to_sequence(x)
def index_at_time(x, ind)
def unsqueeze(x, dim)
def contiguous(x)
def to_device(x, device)
def to_tensor(x)
def to_numpy(x)
def to_list(x)
def to_float(x)
def to_uint8(x)
def to_torch(x, device)
def to_one_hot_single(tensor, num_class)
def to_one_hot(tensor, num_class)
def flatten_single(x, begin_axis)
def flatten(x, begin_axis)
def reshape_dimensions_single(x, begin_axis, end_axis, target_dims)
def reshape_dimensions(x, begin_axis, end_axis, target_dims)
def join_dimensions(x, begin_axis, end_axis)
def expand_at_single(x, size, dim)
def expand_at(x, size, dim)
def unsqueeze_expand_at(x, size, dim)
def repeat_by_expand_at(x, repeats, dim)
def named_reduce_single(x, reduction, dim)
def named_reduce(x, reduction, dim)
def gather_along_dim_with_dim_single(x, target_dim, source_dim, indices)
def gather_along_dim_with_dim(x, target_dim, source_dim, indices)
def gather_sequence_single(seq, indices)
def gather_sequence(seq, indices)
def pad_sequence_single(seq, padding, batched, pad_same, pad_values)
def pad_sequence(seq, padding, batched, pad_same, pad_values)
def assert_size_at_dim_single(x, size, dim, msg)
def assert_size_at_dim(x, size, dim, msg)
def get_shape(x)
def list_of_flat_dict_to_dict_of_list(list_of_dict)
def flatten_nested_dict_list(d, parent_key, sep, item_key)
def time_distributed(inputs, op, activation, inputs_as_kwargs, inputs_as_args)
```

### policy/DP/diffusion_policy/model/diffusion/conditional_unet1d.py

```
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups, cond_predict_scale)
    def forward(self, x, cond)
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, local_cond_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale)
    def forward(self, sample, timestep, local_cond, global_cond)
```

### policy/DP/diffusion_policy/model/diffusion/conv1d_components.py

```
class Downsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Upsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Conv1dBlock(Module)
    """Conv1d --> GroupNorm --> Mish"""
    def __init__(self, inp_channels, out_channels, kernel_size, n_groups)
    def forward(self, x)
def test()
```

### policy/DP/diffusion_policy/model/diffusion/ema_model.py

```
class EMAModel()
    """Exponential Moving Average of models weights"""
    def __init__(self, model, update_after_step, inv_gamma, power, min_value, max_value)
    def get_decay(self, optimization_step)
    def step(self, new_model)
```

### policy/DP/diffusion_policy/model/diffusion/mask_generator.py

```
def get_intersection_slice_mask(shape, dim_slices, device)
def get_union_slice_mask(shape, dim_slices, device)
class DummyMaskGenerator(ModuleAttrMixin)
    def __init__(self)
    def forward(self, shape)
class LowdimMaskGenerator(ModuleAttrMixin)
    def __init__(self, action_dim, obs_dim, max_n_obs_steps, fix_obs_steps, action_visible)
    def forward(self, shape, seed)
class KeypointMaskGenerator(ModuleAttrMixin)
    def __init__(self, action_dim, keypoint_dim, max_n_obs_steps, fix_obs_steps, keypoint_visible_rate, time_independent, action_visible, context_dim, n_context_steps)
    def forward(self, shape, seed)
def test()
```

### policy/DP/diffusion_policy/model/diffusion/positional_embedding.py

```
class SinusoidalPosEmb(Module)
    def __init__(self, dim)
    def forward(self, x)
```

### policy/DP/diffusion_policy/model/diffusion/transformer_for_diffusion.py

```
class TransformerForDiffusion(ModuleAttrMixin)
    def __init__(self, input_dim, output_dim, horizon, n_obs_steps, cond_dim, n_layer, n_head, n_emb, p_drop_emb, p_drop_attn, causal_attn, time_as_cond, obs_as_cond, n_cond_layers)
    def _init_weights(self, module)
    def get_optim_groups(self, weight_decay)
    def configure_optimizers(self, learning_rate, weight_decay, betas)
    def forward(self, sample, timestep, cond)
def test()
```

### policy/DP/diffusion_policy/model/vision/crop_randomizer.py

```
class CropRandomizer(Module)
    """Randomly sample crops at input, and then average across crop features at output."""
    def __init__(self, input_shape, crop_height, crop_width, num_crops, pos_enc)
    def output_shape_in(self, input_shape)
    def output_shape_out(self, input_shape)
    def forward_in(self, inputs)
    def forward_out(self, inputs)
    def forward(self, inputs)
    def __repr__(self)
def crop_image_from_indices(images, crop_indices, crop_height, crop_width)
def sample_random_image_crops(images, crop_height, crop_width, num_crops, pos_enc)
```

### policy/DP/diffusion_policy/model/vision/model_getter.py

```
def get_resnet(name, weights)
def get_r3m(name)
```

### policy/DP/diffusion_policy/model/vision/multi_image_obs_encoder.py

```
class MultiImageObsEncoder(ModuleAttrMixin)
    def __init__(self, shape_meta, rgb_model, resize_shape, crop_shape, random_crop, use_group_norm, share_rgb_model, imagenet_norm)
    def forward(self, obs_dict)
    def output_shape(self)
```

### policy/DP/diffusion_policy/policy/base_image_policy.py

```
class BaseImagePolicy(ModuleAttrMixin)
    def predict_action(self, obs_dict)
    def reset(self)
    def set_normalizer(self, normalizer)
```

### policy/DP/diffusion_policy/policy/diffusion_unet_image_policy.py

```
class DiffusionUnetImagePolicy(BaseImagePolicy)
    def __init__(self, shape_meta, noise_scheduler, obs_encoder, horizon, n_action_steps, n_obs_steps, num_inference_steps, obs_as_global_cond, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, cond_predict_scale)
    def conditional_sample(self, condition_data, condition_mask, local_cond, global_cond, generator)
    def predict_action(self, obs_dict)
    def set_normalizer(self, normalizer)
    def compute_loss(self, batch)
```

### policy/DP/diffusion_policy/shared_memory/shared_memory_queue.py

```
class SharedMemoryQueue()
    """A Lock-Free FIFO Shared Memory Data Structure.
Stores a sequence of dict of numpy arrays."""
    def __init__(self, shm_manager, array_specs, buffer_size)
    def create_from_examples(cls, shm_manager, examples, buffer_size)
    def qsize(self)
    def empty(self)
    def clear(self)
    def put(self, data)
    def get(self, out)
    def get_k(self, k, out)
    def get_all(self, out)
    def _get_k_impl(self, k, read_count, out)
    def _allocate_empty(self, k)
```

### policy/DP/diffusion_policy/shared_memory/shared_memory_ring_buffer.py

```
class SharedMemoryRingBuffer()
    """A Lock-Free FILO Shared Memory Data Structure.
Stores a sequence of dict of numpy arrays."""
    def __init__(self, shm_manager, array_specs, get_max_k, get_time_budget, put_desired_frequency, safety_margin)
    def count(self)
    def create_from_examples(cls, shm_manager, examples, get_max_k, get_time_budget, put_desired_frequency)
    def clear(self)
    def put(self, data, wait)
    def _allocate_empty(self, k)
    def get(self, out)
    def get_last_k(self, k, out)
    def get_all(self)
```

### policy/DP/diffusion_policy/shared_memory/shared_memory_util.py

```
class ArraySpec()
class SharedAtomicCounter()
    def __init__(self, shm_manager, size)
    def buf(self)
    def load(self)
    def store(self, value)
    def add(self, value)
```

### policy/DP/diffusion_policy/shared_memory/shared_ndarray.py

```
class SharedNDArray(?)
    """Class to keep track of and retrieve the data in a shared array
Attributes
----------
shm
    SharedMemory object containing the data of the array
shape
    Shape of the NumPy array
dtype
    Type of the NumPy array. Anything that may be passed to the `dtype=` argument in `np.ndarray`.
lock
    (Opti"""
    def __init__(self, shm, shape, dtype)
    def __repr__(self)
    def create_from_array(cls, mem_mgr, arr)
    def create_from_shape(cls, mem_mgr, shape, dtype)
    def shape(self)
    def get(self)
    def __del__(self)
```

### policy/DP/diffusion_policy/workspace/base_workspace.py

```
class BaseWorkspace()
    def __init__(self, cfg, output_dir)
    def output_dir(self)
    def run(self)
    def save_checkpoint(self, path, tag, exclude_keys, include_keys, use_thread)
    def get_checkpoint_path(self, tag)
    def load_payload(self, payload, exclude_keys, include_keys)
    def load_checkpoint(self, path, tag, exclude_keys, include_keys)
    def create_from_checkpoint(cls, path, exclude_keys, include_keys)
    def save_snapshot(self, tag)
    def create_from_snapshot(cls, path)
def _copy_to_cpu(x)
```

### policy/DP/diffusion_policy/workspace/robotworkspace.py

```
def _cuda_synchronize(device)
def _reduce_train_metrics(metrics, device, multi_gpu)
class RobotWorkspace(BaseWorkspace)
    def __init__(self, cfg, output_dir)
    def _model(self)
    def run(self)
class BatchSampler()
    def __init__(self, data_size, batch_size, shuffle, seed, drop_last)
    def __iter__(self)
    def __len__(self)
def create_dataloader(dataset)
def main(cfg)
```

### policy/DP/dp_model.py

```
class DP()
    def __init__(self, ckpt_file, n_obs_steps, n_action_steps, device)
    def _filter_arrays(obs)
    def update_obs(self, observation)
    def reset_obs(self)
    def reset_model(self)
    def get_action(self, observation)
    def get_last_obs(self)
    def get_policy(self, checkpoint, output_dir, device)
```

### policy/DP/process_hdf5_to_zarr.py

```
"""Convert dex2scene HDF5 replay episodes into a preprocessed Zarr store.

One-time preprocessing — decodes all JPEG camera images, applies active-DOF
selection, and writes a single Zarr directory that the Dex2SceneZarrDataset
reads with zero decode overhead at training time.

Usage:
    python process_hdf5_to_zarr.py \
        --dataset_dir /path/to/replay-generalization \
        --output /path/to/output.zarr \
        [--max_episodes 10] [--image_height 480] [--image_width 640]

The output Zarr has:
    data/
      state          float32  (total_steps, active_dof)
      action         float32 """
def _find_homing_cutoff(hdf5_path, ep_len)
def parse_args()
def main()
```

### policy/DP/train.py

```
"""Usage:
    python train.py --config-name=robot_dp_36_dex2scene_pretrained.yaml         training.device="cuda:0" dataloader.batch_size=4 logging.mode=offline"""
def main(cfg)
```

### policy/GR00T_XE/__init__.py

```
"""GR00T XE — Cross-Embodiment finetuning on GR00T N1.5."""
```

### policy/GR00T_XE/convert_ee_trajectories.py

```
"""Generate arm_ee_trajectories.hdf5 alongside the original HDF5 episodes.

Reads robot/qpos and action/commanded from each episode, splits arm and hand
joints, and writes a separate HDF5 file with FK-computed 6-DOF ee poses.

This is a preprocessing step that runs once per task dataset.  The resulting
file is read by :class:`CrossEmbodimentHDF5Dataset` during training.

The EE convention (URDF, ``pin_ee_frame``, ``ee_offset``) MUST match the
eval-time converter ``ik_arm_converter._ROBOT_KEY_TO_ARM``: joint values are
placed into the Pinocchio model by joint NAME (``getJointId(...).idx_q``), the
"""
def _load_arm_cfg(robot_key)
def _build_fk_side(model, data, arm_cfg, robot_key, side_joint_names, episode_joint_names, ee_frame, ee_offset)
def convert_dataset(dataset_dir, robot_key, output)
def main()
```

### policy/GR00T_XE/dataset.py

```
"""Cross-embodiment HDF5 dataset for GR00T XE.

从 replay-generalization 读 RGB + 手部关节, 从 arm_ee_trajectories.hdf5 读机械臂末端位姿,
组合成统一的 64D state/action 空间。"""
def _take_rows(dset, idxs)
class CrossEmbodimentHDF5Dataset(Dex2BenchHDF5Dataset)
    """从 replay HDF5 + arm_ee_trajectories.hdf5 构建统一 64D 数据."""
    def __init__(self)
    def set_transforms_metadata(self, metadata)
    def _compute_statistics(self)
    def _build_hand_mapping(self, joint_names)
    def _init_ee_file(self)
    def _build_unified(self, ee_qpos, ee_action, hand_qpos, hand_action, joint_names)
    def _get_ee_data(self, ep_stem, raw_idx)
    def _get_ee_action_data(self, ep_stem, raw_idx)
    def _get_ee_frames(self, ep_stem, frame_idxs)
    def _get_ee_ep_stem(self, ep_path)
    def get_step_data(self, ep_idx, local_valid_idx)
    def robot_key(self)
    def __del__(self)
def build_hdf5_dataset(input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, use_active_dof, robot_key, state_dim, action_dim, truncate_at_homing, xe_stats_only)
```

### policy/GR00T_XE/deploy_policy.py

```
"""GR00T XE deployment: 加载 checkpoint, 输出可直接使用的关节角 action.

用法:
  model = get_model(usr_args)
  encoded = encode_obs(raw_obs)       # qpos → FK → 统一 64D state + 视频
  action = model.get_action(encoded)  # 推理 → IK arm + hand 反向映射 → 关节角

encode_obs 兼容两种观测格式:
  TACTILE:  observation["robot_key"], observation["qpos"], observation["images"][cam_id].rgb
  REMOTE:   observation["joint_action"]["qpos"], observation["observation"][cam_id]["rgb"]

get_action 使用 Gr00tPolicy wrapper, 自动处理以下 transform:
  VideoToTensor → VideoCrop → VideoResize → VideoColorJitter → VideoToNumpy
  → StateActionToTensor → StateAc"""
def _action_mode()
def _video_keys()
def _hdf5_camera_map()
def _read_camera_remote(observation, name)
def _read_camera_tactile(observation, name)
def _is_remote_format(observation)
def encode_obs(observation)
class GR00TXEPolicy()
    """加载 GR00T XE checkpoint, 使用 Gr00tPolicy wrapper 处理 transform 流水线."""
    def __init__(self, model_path, robot_key)
    def get_action(self, obs)
def get_model(usr_args)
def reset_model(model)
```

### policy/GR00T_XE/finetune.py

```
"""Single-task finetune, either from a GR00T XE pretrain or from the base model.

Two-stage (default) -- load the cross-embodiment pretrain, finetune on one task::

    python policy/GR00T_XE/finetune.py \
        --dataset-path /data/73_jigsaw/replay-generalization \
        --pretrained-ckpt /ckpt/gr00t_xe_pretrain/checkpoint-520000 \
        --output-dir /ckpt/73/gr00t_xe_ft \
        --max-steps 5000 --batch-size 64

Single-stage (``--init-from-base``) -- skip the pretrain entirely and train the
one task from GR00T-N1.5-3B, the recipe GR00T n15 uses::

    python policy/GR00T_XE/finetune.py \"""
class FinetuneConfig()
    """Single-task finetune from GR00T XE pretrained checkpoint."""
def _parse_hdf5_camera_map(items)
class MilestoneSaveCallback(TrainerCallback)
    def __init__(self, milestone_steps)
    def on_step_end(self, args, state, control)
def main(config)
```

### policy/GR00T_XE/gr00t_hdf5_dataset.py

```
"""PyTorch Dataset that reads dex2bench HDF5 episodes directly, bypassing LeRobot conversion.

Produces the same raw-data dict format as ``LeRobotSingleDataset.get_step_data``,
so the existing GR00T transform pipeline (VideoToTensor, StateActionTransform, etc.)
applies unchanged.

Usage::

    from gr00t_hdf5_dataset import Dex2BenchHDF5Dataset

    ds = Dex2BenchHDF5Dataset(
        input_dir="/path/to/replay-generalization",
        camera_map={"stereo_left": "cam_stereo_left", ...},
        modality_configs=modality_configs,
        transforms=transforms,
        embodiment_tag="new_embodiment"""
def _decode_hdf5_string(value)
def _decode_rgb_frame(frame)
def _valid_indices(ep)
def _find_homing_cutoff(ep, ep_len_full, valid_indices)
class Dex2BenchHDF5Dataset(Dataset)
    """Read dex2bench HDF5 episodes and apply GR00T transforms directly.

Parameters
----------
input_dir : Path or str
    Directory containing ``episode_*.hdf5`` files.
camera_map : dict[str, str]
    Mapping from GR00T video sub-keys (e.g. ``"stereo_left"``) to HDF5
    camera IDs (e.g. ``"cam_stereo_le"""
    def __init__(self, input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, active_dof_info, state_dim, action_dim, seed, truncate_at_homing)
    def metadata(self)
    def tag(self)
    def modality_configs(self)
    def transforms(self)
    def dataset_name(self)
    def trajectory_ids(self)
    def trajectory_lengths(self)
    def all_steps(self)
    def max_delta(self)
    def set_epoch(self, epoch)
    def set_transforms_metadata(self, metadata)
    def _compute_statistics(self)
    def _build_metadata(self, stats)
    def _get_episode(self, ep_idx)
    def get_step_data(self, ep_idx, local_valid_idx)
    def __len__(self)
    def __getitem__(self, idx)
    def __del__(self)
def build_hdf5_dataset(input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, use_active_dof, robot_key, state_dim, action_dim, truncate_at_homing)
```

### policy/GR00T_XE/ik_arm_converter.py

```
"""Cross-embodiment 状态/动作转换器: FK/IK + 手部映射。

核心功能:
  1. qpos_to_unified():  原始关节角 → 统一 64D state (arm ee_pose + hand slots)
  2. unified_to_joint_action(): 统一 64D action → 实际关节角 (IK arm + reverse hand)"""
def _get_pin()
def _note_ik_failure(robot_key, side, residual)
def get_ik_failure_stats()
def _load_arm_config(arm_name)
def _ensure_arm_joints(arm_name)
def _load_pin_model(robot_key)
def _hand_names_to_slots(robot_key, joint_names)
class XEStateActionConverter()
    """Cross-embodiment state/action converter.

用法:
    conv = XEStateActionConverter()
    unified_state = conv.qpos_to_unified(qpos_raw, robot_key)
    joint_action = conv.unified_to_joint_action(unified_action, robot_key)"""
    def __init__(self)
    def _get_arm_indices(self, robot_key, joint_names)
    def _get_hand_maps(self, robot_key, joint_names)
    def qpos_to_unified(self, qpos_full, robot_key)
    def unified_to_joint_action(self, unified_action, robot_key, current_qpos)
```

### policy/GR00T_XE/offline_inference.py

```
"""离线推理脚本: 用训练数据轨迹对比 GR00T XE 模型输出 vs 记录动作.

用法:
  python offline_inference.py     --model_path /path/to/checkpoint     --robot_key multi_iiwa7_with_sharpa     --hdf5 /path/to/episode_000000.hdf5     --max_frames 100     --output /tmp/offline_compare.npz"""
def parse_args()
def build_hdf5_to_isaac_reindex(hdf5_joint_names, isaac_joint_names)
def load_hdf5_frame_remote(hdf5_path, frame_idx, robot_key, reindex)
def main()
```

### policy/GR00T_XE/pretrain.py

```
"""Cross-Embodiment GR00T XE pretrain on 26 tasks × 12 embodiments.

Loads all available task datasets and trains a unified policy head (DiT)
while keeping the VLM backbone frozen.  One command::

    python policy/GR00T_XE/pretrain.py \
        --dataset-path /data/task1 /data/task2 ... \
        --output-dir /ckpt/gr00t_xe_pretrain \
        --max-steps 520000 --batch-size 64 --num-gpus 8

Multi-GPU is handled automatically via ``torchrun`` when ``--num-gpus > 1``."""
class PretrainConfig()
    """Cross-embodiment pretrain for GR00T XE."""
def _task_name_from_dataset_path(path)
def _scene_prompt(task_name, scenes_dir)
def _parse_hdf5_camera_map(items)
class MilestoneSaveCallback(TrainerCallback)
    """Copy checkpoint to ``checkpoint-milestone-{step}`` every N steps."""
    def __init__(self, milestone_steps)
    def on_step_end(self, args, state, control)
def main(config)
```

### policy/GR00T_XE/src/eval/http_server.py

```
"""GR00T HTTP Server Module

This module provides HTTP server functionality for GR00T model inference.
It exposes a REST API for easy integration with web applications and other services.

Dependencies:
    => Server: `pip install uvicorn fastapi json-numpy`
    => Client: `pip install requests json-numpy`"""
class HTTPInferenceServer()
    def __init__(self, policy, port, host, api_token)
    def predict_action(self, payload)
    def health_check(self)
    def run(self)
def create_http_server(policy, port, host, api_token)
```

### policy/GR00T_XE/src/eval/robot.py

```
class RobotInferenceServer(BaseInferenceServer)
    """Server with three endpoints for real robot policies"""
    def __init__(self, model, host, port, api_token)
    def start_server(policy, port, api_token)
class RobotInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for communicating with the RealRobotServer"""
    def __init__(self, host, port, api_token)
    def get_action(self, observations)
    def get_modality_config(self)
```

### policy/GR00T_XE/src/eval/service.py

```
class MsgSerializer()
    def to_bytes(data)
    def from_bytes(data)
    def decode_custom_classes(obj)
    def encode_custom_classes(obj)
class EndpointHandler()
class BaseInferenceServer()
    """An inference server that spin up a ZeroMQ socket and listen for incoming requests.
Can add custom endpoints by calling `register_endpoint`."""
    def __init__(self, host, port, api_token)
    def _kill_server(self)
    def _handle_ping(self)
    def register_endpoint(self, name, handler, requires_input)
    def _validate_token(self, request)
    def run(self)
class BaseInferenceClient()
    def __init__(self, host, port, timeout_ms, api_token)
    def _init_socket(self)
    def ping(self)
    def kill_server(self)
    def call_endpoint(self, endpoint, data, requires_input)
    def __del__(self)
class ExternalRobotInferenceClient(BaseInferenceClient)
    """Client for communicating with the RealRobotServer"""
    def get_action(self, observations)
```

### policy/GR00T_XE/src/eval/simulation.py

```
class VideoConfig()
    """Configuration for video recording settings."""
class MultiStepConfig()
    """Configuration for multi-step environment settings."""
class SimulationConfig()
    """Main configuration for simulation environment."""
class SimulationInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for running simulations and communicating with the inference server."""
    def __init__(self, host, port)
    def get_action(self, observations)
    def get_modality_config(self)
    def setup_environment(self, config)
    def run_simulation(self, config)
    def _get_actions_from_server(self, observations)
def _create_single_env(config, idx)
def run_evaluation(env_name, host, port, video_dir, n_episodes, n_envs, n_action_steps, max_episode_steps)
```

### policy/GR00T_XE/src/eval/wrappers/multistep_wrapper.py

```
def stack_repeated(x, n, loc)
def repeated_box(box_space, n, loc)
def repeated_space(space, n, loc)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def aggregate(data, method)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices, n_action_steps, max_episode_steps, reward_agg_method)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def get_max_steps_needed(self)
    def assert_delta_indices(self, delta_indices, horizon)
    def reset(self, seed, options)
    def step(self, action)
    def _get_obs(self, video_delta_indices, state_delta_indices)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def get_infos(self)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        """
        For video, the observation space will be (video_horizon,) + original shape
        For state (if not None), the observation space will be (state_horizon,) + original shape
        """
        new_observation_space = {}
        for k in observation_space.keys():
            if k.startswith("video"):
                box = observation_space[k]
                horizon = video_horizon
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("state"):
                box = observation_space[k]
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("annotation"):
                text = observation_space[k]
                new_observation_space[k] = text
            else:
                raise ValueError(f"Unknown key: {k}")  # NOTE: We might add "language" in the future

        return spaces.Dict(new_observation_space)
```

```python
def _get_obs(self, video_delta_indices, state_delta_indices):
        """
        Output:
        For video: (video_horizon,) + obs_shape
        For state (if not None): (state_horizon,) + obs_shape
        """
        assert len(self.obs) > 0
        if isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                if key.startswith("video"):
                    """
                    NOTE:
                      We need to subtract 1 because video_delta_indices is 0-indexed.
                      E.g., video_delta_indices = np.array([-4, -3, -2, -1, 0])
                      Then when we select the observation,
                        it should be [obs[-5], obs[-4], obs[-3], obs[-2], obs[-1]]
                      (i.e., the latest observation is at the last index)
                    """
                    delta_indices = video_delta_indices - 1
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("state"):
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("annotation"):
                    result[key] = self.obs[-1][key]
                else:
                    raise ValueError(f"Unknown key: {key}")
            return result
        else:
            raise RuntimeError(f"Unsupported space type: {type(self.observation_space)=}")
```

```python
def get_rewards(self):
        return self.reward
```
```

### policy/GR00T_XE/src/eval/wrappers/obs_index_selection_wrapper.py

```
class ObsIndexSelectionWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices)
    def assert_delta_indices(self, delta_indices, horizon)
    def select_steps_for_values(self, data_value, delta_indices)
    def select_steps_for_obs(self, obs)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def reset(self, seed, options)
    def step(self, action)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        new_observation_space = {}
        for k in observation_space.keys():
            box = observation_space[k]
            if k.startswith("video"):
                horizon = video_horizon
            elif k.startswith("state"):
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
            else:
                raise ValueError(f"Unknown key: {k}")

            new_observation_space[k] = gym.spaces.Box(
                low=box.low[:horizon],
                high=box.high[:horizon],
                shape=(horizon, *box.shape[1:]),
                dtype=box.dtype,
            )
        return gym.spaces.Dict(new_observation_space)
```
```

### policy/GR00T_XE/src/eval/wrappers/video_recording_wrapper.py

```
def get_accumulate_timestamp_idxs(timestamps, start_time, dt, eps, next_global_idx, allow_negative)
class VideoRecorder()
    def __init__(self, fps, codec, input_pix_fmt)
    def _reset_state(self)
    def create_h264(cls, fps, codec, input_pix_fmt, output_pix_fmt, crf, profile)
    def __del__(self)
    def is_ready(self)
    def start(self, file_path, start_time)
    def write_frame(self, img, frame_time)
    def stop(self)
class VideoRecordingWrapper(Wrapper)
    def __init__(self, env, video_recorder, mode, video_dir, steps_per_render)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### policy/GR00T_XE/src/experiment/data_config.py

```
class BaseDataConfig(ABC)
    def modality_config(self)
    def transform(self)
def import_external_data_config(data_config_str)
def load_data_config(data_config_str)
class FourierGr1ArmsOnlyDataConfig(BaseDataConfig)
    def transform(self)
class So100DataConfig(BaseDataConfig)
    def transform(self)
class So100DualCamDataConfig(So100DataConfig)
class UnitreeG1DataConfig(BaseDataConfig)
    def transform(self)
class UnitreeG1FullBodyDataConfig(UnitreeG1DataConfig)
class FourierGr1FullUpperBodyDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaGripperDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaHandDataConfig(BimanualPandaGripperDataConfig)
class SinglePandaGripperDataConfig(BimanualPandaGripperDataConfig)
class FourierGr1ArmsWaistDataConfig(FourierGr1ArmsOnlyDataConfig)
    def transform(self)
class OxeDroidDataConfig(BaseDataConfig)
    def transform(self)
class AgibotGenie1DataConfig(BaseDataConfig)
    def transform(self)
```

### policy/GR00T_XE/src/experiment/runner.py

```
class TrainRunner()
    def __init__(self, model, training_args, train_dataset, resume_from_checkpoint)
    def create_trainer(self, model, training_args, train_dataset, data_collator, compute_dtype, global_batch_size)
    def train(self)
    def _cleanup_output(self)
```

### policy/GR00T_XE/src/experiment/trainer.py

```
class BaseSampler(Sampler)
    """Sampler for dataset, which enables `set_epoch` for Dataset.
`set_epoch` will be called by huggingface Trainer at the end of each epoch.
`shuffle` is also supported for training set shuffling"""
    def __init__(self, data_source, shuffle, seed)
    def __iter__(self)
    def set_epoch(self, epoch)
    def __len__(self)
class DualBrainTrainer(Trainer)
    def __init__(self)
    def _get_train_sampler(self)
    def _get_eval_sampler(self, eval_dataset)
    def compute_loss(self, model, inputs, return_outputs, num_items_in_batch)
    def create_optimizer(self)
    def save_model(self, output_dir, _internal_call)
    def train(self, resume_from_checkpoint, trial, ignore_keys_for_eval)
```

### policy/GR00T_XE/src/gr00t/eval/http_server.py

```
"""GR00T HTTP Server Module

This module provides HTTP server functionality for GR00T model inference.
It exposes a REST API for easy integration with web applications and other services.

Dependencies:
    => Server: `pip install uvicorn fastapi json-numpy`
    => Client: `pip install requests json-numpy`"""
class HTTPInferenceServer()
    def __init__(self, policy, port, host, api_token)
    def predict_action(self, payload)
    def health_check(self)
    def run(self)
def create_http_server(policy, port, host, api_token)
```

### policy/GR00T_XE/src/gr00t/eval/robot.py

```
class RobotInferenceServer(BaseInferenceServer)
    """Server with three endpoints for real robot policies"""
    def __init__(self, model, host, port, api_token)
    def start_server(policy, port, api_token)
class RobotInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for communicating with the RealRobotServer"""
    def __init__(self, host, port, api_token)
    def get_action(self, observations)
    def get_modality_config(self)
```

### policy/GR00T_XE/src/gr00t/eval/service.py

```
class MsgSerializer()
    def to_bytes(data)
    def from_bytes(data)
    def decode_custom_classes(obj)
    def encode_custom_classes(obj)
class EndpointHandler()
class BaseInferenceServer()
    """An inference server that spin up a ZeroMQ socket and listen for incoming requests.
Can add custom endpoints by calling `register_endpoint`."""
    def __init__(self, host, port, api_token)
    def _kill_server(self)
    def _handle_ping(self)
    def register_endpoint(self, name, handler, requires_input)
    def _validate_token(self, request)
    def run(self)
class BaseInferenceClient()
    def __init__(self, host, port, timeout_ms, api_token)
    def _init_socket(self)
    def ping(self)
    def kill_server(self)
    def call_endpoint(self, endpoint, data, requires_input)
    def __del__(self)
class ExternalRobotInferenceClient(BaseInferenceClient)
    """Client for communicating with the RealRobotServer"""
    def get_action(self, observations)
```

### policy/GR00T_XE/src/gr00t/eval/simulation.py

```
class VideoConfig()
    """Configuration for video recording settings."""
class MultiStepConfig()
    """Configuration for multi-step environment settings."""
class SimulationConfig()
    """Main configuration for simulation environment."""
class SimulationInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for running simulations and communicating with the inference server."""
    def __init__(self, host, port)
    def get_action(self, observations)
    def get_modality_config(self)
    def setup_environment(self, config)
    def run_simulation(self, config)
    def _get_actions_from_server(self, observations)
def _create_single_env(config, idx)
def run_evaluation(env_name, host, port, video_dir, n_episodes, n_envs, n_action_steps, max_episode_steps)
```

### policy/GR00T_XE/src/gr00t/eval/wrappers/multistep_wrapper.py

```
def stack_repeated(x, n, loc)
def repeated_box(box_space, n, loc)
def repeated_space(space, n, loc)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def aggregate(data, method)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices, n_action_steps, max_episode_steps, reward_agg_method)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def get_max_steps_needed(self)
    def assert_delta_indices(self, delta_indices, horizon)
    def reset(self, seed, options)
    def step(self, action)
    def _get_obs(self, video_delta_indices, state_delta_indices)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def get_infos(self)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        """
        For video, the observation space will be (video_horizon,) + original shape
        For state (if not None), the observation space will be (state_horizon,) + original shape
        """
        new_observation_space = {}
        for k in observation_space.keys():
            if k.startswith("video"):
                box = observation_space[k]
                horizon = video_horizon
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("state"):
                box = observation_space[k]
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("annotation"):
                text = observation_space[k]
                new_observation_space[k] = text
            else:
                raise ValueError(f"Unknown key: {k}")  # NOTE: We might add "language" in the future

        return spaces.Dict(new_observation_space)
```

```python
def _get_obs(self, video_delta_indices, state_delta_indices):
        """
        Output:
        For video: (video_horizon,) + obs_shape
        For state (if not None): (state_horizon,) + obs_shape
        """
        assert len(self.obs) > 0
        if isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                if key.startswith("video"):
                    """
                    NOTE:
                      We need to subtract 1 because video_delta_indices is 0-indexed.
                      E.g., video_delta_indices = np.array([-4, -3, -2, -1, 0])
                      Then when we select the observation,
                        it should be [obs[-5], obs[-4], obs[-3], obs[-2], obs[-1]]
                      (i.e., the latest observation is at the last index)
                    """
                    delta_indices = video_delta_indices - 1
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("state"):
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("annotation"):
                    result[key] = self.obs[-1][key]
                else:
                    raise ValueError(f"Unknown key: {key}")
            return result
        else:
            raise RuntimeError(f"Unsupported space type: {type(self.observation_space)=}")
```

```python
def get_rewards(self):
        return self.reward
```
```

### policy/GR00T_XE/src/gr00t/eval/wrappers/obs_index_selection_wrapper.py

```
class ObsIndexSelectionWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices)
    def assert_delta_indices(self, delta_indices, horizon)
    def select_steps_for_values(self, data_value, delta_indices)
    def select_steps_for_obs(self, obs)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def reset(self, seed, options)
    def step(self, action)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        new_observation_space = {}
        for k in observation_space.keys():
            box = observation_space[k]
            if k.startswith("video"):
                horizon = video_horizon
            elif k.startswith("state"):
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
            else:
                raise ValueError(f"Unknown key: {k}")

            new_observation_space[k] = gym.spaces.Box(
                low=box.low[:horizon],
                high=box.high[:horizon],
                shape=(horizon, *box.shape[1:]),
                dtype=box.dtype,
            )
        return gym.spaces.Dict(new_observation_space)
```
```

### policy/GR00T_XE/src/gr00t/eval/wrappers/video_recording_wrapper.py

```
def get_accumulate_timestamp_idxs(timestamps, start_time, dt, eps, next_global_idx, allow_negative)
class VideoRecorder()
    def __init__(self, fps, codec, input_pix_fmt)
    def _reset_state(self)
    def create_h264(cls, fps, codec, input_pix_fmt, output_pix_fmt, crf, profile)
    def __del__(self)
    def is_ready(self)
    def start(self, file_path, start_time)
    def write_frame(self, img, frame_time)
    def stop(self)
class VideoRecordingWrapper(Wrapper)
    def __init__(self, env, video_recorder, mode, video_dir, steps_per_render)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### policy/GR00T_XE/src/gr00t/experiment/data_config.py

```
class BaseDataConfig(ABC)
    def modality_config(self)
    def transform(self)
def import_external_data_config(data_config_str)
def load_data_config(data_config_str)
class FourierGr1ArmsOnlyDataConfig(BaseDataConfig)
    def transform(self)
class So100DataConfig(BaseDataConfig)
    def transform(self)
class So100DualCamDataConfig(So100DataConfig)
class UnitreeG1DataConfig(BaseDataConfig)
    def transform(self)
class UnitreeG1FullBodyDataConfig(UnitreeG1DataConfig)
class FourierGr1FullUpperBodyDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaGripperDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaHandDataConfig(BimanualPandaGripperDataConfig)
class SinglePandaGripperDataConfig(BimanualPandaGripperDataConfig)
class FourierGr1ArmsWaistDataConfig(FourierGr1ArmsOnlyDataConfig)
    def transform(self)
class OxeDroidDataConfig(BaseDataConfig)
    def transform(self)
class AgibotGenie1DataConfig(BaseDataConfig)
    def transform(self)
```

### policy/GR00T_XE/src/gr00t/experiment/runner.py

```
class TrainRunner()
    def __init__(self, model, training_args, train_dataset, resume_from_checkpoint)
    def create_trainer(self, model, training_args, train_dataset, data_collator, compute_dtype, global_batch_size)
    def train(self)
    def _cleanup_output(self)
```

### policy/GR00T_XE/src/gr00t/experiment/trainer.py

```
class BaseSampler(Sampler)
    """Sampler for dataset, which enables `set_epoch` for Dataset.
`set_epoch` will be called by huggingface Trainer at the end of each epoch.
`shuffle` is also supported for training set shuffling"""
    def __init__(self, data_source, shuffle, seed)
    def __iter__(self)
    def set_epoch(self, epoch)
    def __len__(self)
class DualBrainTrainer(Trainer)
    def __init__(self)
    def _get_train_sampler(self)
    def _get_eval_sampler(self, eval_dataset)
    def compute_loss(self, model, inputs, return_outputs, num_items_in_batch)
    def create_optimizer(self)
    def save_model(self, output_dir, _internal_call)
    def train(self, resume_from_checkpoint, trial, ignore_keys_for_eval)
```

### policy/GR00T_XE/src/gr00t/model/action_head/action_encoder.py

```
def swish(x)
class SinusoidalPositionalEncoding(Module)
    """Produces a sinusoidal encoding of shape (B, T, w)
given timesteps of shape (B, T)."""
    def __init__(self, embedding_dim)
    def forward(self, timesteps)
class ActionEncoder(Module)
    def __init__(self, action_dim, hidden_size)
    def forward(self, actions, timesteps)
```

### policy/GR00T_XE/src/gr00t/model/action_head/cross_attention_dit.py

```
class TimestepEncoder(Module)
    def __init__(self, embedding_dim, compute_dtype)
    def forward(self, timesteps)
class AdaLayerNorm(Module)
    def __init__(self, embedding_dim, norm_elementwise_affine, norm_eps, chunk_dim)
    def forward(self, x, temb)
class BasicTransformerBlock(Module)
    def __init__(self, dim, num_attention_heads, attention_head_dim, dropout, cross_attention_dim, activation_fn, attention_bias, upcast_attention, norm_elementwise_affine, norm_type, norm_eps, final_dropout, attention_type, positional_embeddings, num_positional_embeddings, ff_inner_dim, ff_bias, attention_out_bias)
    def forward(self, hidden_states, attention_mask, encoder_hidden_states, encoder_attention_mask, temb)
class DiT(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, norm_type, norm_elementwise_affine, norm_eps, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention, cross_attention_dim)
    def forward(self, hidden_states, encoder_hidden_states, timestep, encoder_attention_mask, return_all_hidden_states)
class SelfAttentionTransformer(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention)
    def forward(self, hidden_states, return_all_hidden_states)
```

### policy/GR00T_XE/src/gr00t/model/action_head/flow_matching_action_head.py

```
class CategorySpecificLinear(Module)
    def __init__(self, num_categories, input_dim, hidden_dim)
    def forward(self, x, cat_ids)
class CategorySpecificMLP(Module)
    def __init__(self, num_categories, input_dim, hidden_dim, output_dim)
    def forward(self, x, cat_ids)
class MultiEmbodimentActionEncoder(Module)
    def __init__(self, action_dim, hidden_size, num_embodiments)
    def forward(self, actions, timesteps, cat_ids)
class FlowmatchingActionHeadConfig(PretrainedConfig)
    """NOTE: N1.5 uses XEmbFlowmatchingPolicyHeadConfig as action head"""
    def __init__(self)
class FlowmatchingActionHead(Module)
    def __init__(self, config)
    def set_trainable_parameters(self, tune_projector, tune_diffusion_model)
    def set_frozen_modules_to_eval_mode(self)
    def sample_time(self, batch_size, device, dtype)
    def prepare_input(self, batch)
    def process_backbone_output(self, backbone_output)
    def forward(self, backbone_output, action_input)
    def get_action(self, backbone_output, action_input)
    def device(self)
    def dtype(self)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/configuration_eagle2_5_vl.py

```
class Eagle2_5_VLConfig(PretrainedConfig)
    def __init__(self, vision_config, text_config, use_backbone_lora, use_llm_lora, pad2square, select_layer, force_image_size, downsample_ratio, template, dynamic_image_size, use_thumbnail, loss_version, min_dynamic_tiles, max_dynamic_tiles, mlp_checkpoint, initializer_range, _attn_implementation, _attn_implementation_autoset, llm_config, image_token_index, use_pixel_shuffle, mlp_connector_layers)
    def to_dict(self)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/image_processing_eagle2.py

```
"""Image processor class for LLaVa-Onevision."""
def crop(img, left, top, right, bottom, input_data_format)
def divide_to_patches(image, patch_size, input_data_format)
def expand_to_square(image, background_color, input_data_format)
def _get_patch_output_size(image, target_resolution, input_data_format)
class Eagle2ImageProcessor(BaseImageProcessor)
    """Constructs a LLaVa-Onevision image processor. Based on [`SiglipImageProcessor`] with incorporation of processing each video frame.

Args:
    do_resize (`bool`, *optional*, defaults to `True`):
        Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridde"""
    def __init__(self, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, min_dynamic_tiles, max_dynamic_tiles, use_thumbnail, pad_during_tiling)
    def pad(self, image, padding, mode, constant_values, data_format, input_data_format)
    def _resize_for_patching(self, image, target_resolution, resample, input_data_format)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, resample, data_format, input_data_format)
    def _pad_for_batching(self, pixel_values, data_format, input_data_format)
    def _preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_convert_rgb, data_format, input_data_format)
    def preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, return_tensors, data_format, input_data_format)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/image_processing_eagle2_5_vl_fast.py

```
def crop(img, left, top, right, bottom)
class Eagle2_5_VLFastImageProcessorKwargs(DefaultFastImageProcessorKwargs)
class Eagle2_5_VLImageProcessorFast(BaseImageProcessorFast)
    def __init__(self)
    def _prepare_images_structure(self, images)
    def _prepare_videos_structure(self, videos)
    def _prepare_input_videos(self, videos, do_convert_rgb, input_data_format, device)
    def _resize_for_patching(self, image, target_resolution, interpolation, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def _get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, interpolation, pad_during_tiling)
    def _pad_for_batching(self, pixel_values)
    def _preprocess(self, images, do_resize, size, max_dynamic_tiles, min_dynamic_tiles, use_thumbnail, pad_during_tiling, interpolation, do_center_crop, crop_size, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, return_tensors)
    def preprocess(self, images, videos)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/modeling_eagle2_5_vl.py

```
class Eagle2_5_VLPreTrainedModel(PreTrainedModel)
    def _init_weights(self, module)
class Eagle2_5_VLForConditionalGeneration(Eagle2_5_VLPreTrainedModel, GenerationMixin)
    def __init__(self, config, vision_model, language_model)
    def check_forward_kwargs(self)
    def wrap_backbone_lora(self, r, lora_alpha, lora_dropout)
    def wrap_llm_lora(self, r, lora_alpha, lora_dropout)
    def forward(self, pixel_values, input_ids, attention_mask, position_ids, image_flags, past_key_values, labels, use_cache, output_attentions, output_hidden_states, return_dict, num_tiles_list)
    def pixel_shuffle(self, x, scale_factor)
    def extract_feature(self, pixel_values)
    def generate(self, pixel_values, input_ids, attention_mask, visual_features, generation_config, output_hidden_states, image_sizes)
    def get_input_embeddings(self)
    def set_input_embeddings(self, value)
    def get_output_embeddings(self)
    def set_output_embeddings(self, new_embeddings)
    def set_decoder(self, decoder)
    def get_decoder(self)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/processing_eagle2_5_vl.py

```
"""Processor class for Eagle2_5_VL.
copy from https://github.com/huggingface/transformers/blob/main/src/transformers/models/llava_onevision/processing_llava_onevision.py"""
def adjust_by_factor(number, factor, method)
def to_rgb(pil_image)
def fetch_image(ele)
def smart_nframes(ele, total_frames, video_fps)
def _read_video_torchvision(ele)
def is_decord_available()
def _read_video_decord(ele)
def get_video_reader_backend()
def fetch_video(ele, return_video_sample_fps)
class Eagle2_5_VLProcessorKwargs(ProcessingKwargs)
class Eagle2_5_VLProcessor(ProcessorMixin)
    """Constructs a Eagle2_5_VL processor which wraps a Eagle2_5_VL video processor, Eagle2_5_VL image processor and a Eagle2_5_VL tokenizer into a single processor.

[`Eagle2_5_VLProcessor`] offers all the functionalities of [`Eagle2_5_VLVideoProcessor`], [`Eagle2_5_VLImageProcessor`] and [`Eagle2_5_VLTok"""
    def __init__(self, image_processor, tokenizer, vision_feature_select_strategy, chat_template, image_token, video_token, tokens_per_tile, image_placeholder, video_placeholder, image_start_token, image_end_token)
    def replace_media_placeholder(self, text, image_list, video_list, timestamps_list, fps_list)
    def __call__(self, images, text, audio, videos)
    def get_number_tiles_based_on_image_size(self, image_size, min_num, max_num, use_thumbnail, tile_size)
    def batch_decode(self)
    def decode(self)
    def model_input_names(self)
    def save_pretrained(self, save_directory)
    def from_pretrained(cls, pretrained_model_name_or_path)
    def process_vision_info(self, conversations, return_video_kwargs)
    def extract_vision_info(self, conversations)
    def py_apply_chat_template(self, messages, tokenize, add_generation_prompt)
    def from_args_and_dict(cls, args, processor_dict)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle2_hg_model/radio_model.py

```
class FlashAttention(Module)
    """Implement the scaled dot product attention with softmax.
Arguments
---------
    softmax_scale: The temperature to use for the softmax attention.
                  (default: 1/sqrt(d_keys) where d_keys is computed at
                  runtime)
    attention_dropout: The dropout rate to apply to the """
    def __init__(self, softmax_scale, attention_dropout, device, dtype)
    def forward(self, qkv, key_padding_mask, causal, cu_seqlens, max_s, need_weights)
def _flash_attn(self, x)
def forward(self, x)
def replace_vit_attn_with_flash_attn()
class ClsToken(Module)
    def __init__(self, ndim, num_tokens, enabled, register_multiple, num_registers)
    def disable(self)
    def forward(self, x)
    def no_weight_decay(self)
class ViTPatchGenerator(Module)
    def __init__(self, patch_size, embed_dim, input_dims, abs_pos, normalize_patches, cls_token, max_input_dims, pos_dropout, return_pos_enc, num_cls_tokens, register_multiple, num_registers, patch_bias, device, dtype)
    def forward(self, x)
    def apply_cls_token(self)
    def num_cls_tokens(self)
    def num_registers(self)
    def num_skip(self)
    def no_weight_decay(self)
    def _load_projection(self, src_proj_weight, targ_proj_weight)
    def embed_patches(self, x)
    def apply_pos_enc(self, patches, patch_idxs, input_size)
    def get_pos_enc(self, batch_size, patch_idxs, input_size)
    def _get_pos_embeddings(self, batch_size, input_dims)
class Im2Patches(Module)
    def __init__(self, patch_size)
    def forward(self, x)
class ViTPatchLinear(Linear)
    def __init__(self, patch_size, embed_dim, bias)
def _forward_cpe(self, x)
def _take_indices(num_blocks, n)
def _enable_cpe_for_timm_vit(model, max_img_size, num_cls_tokens, pos_dropout, register_multiple, num_registers)
def enable_cpe(model)
class Dinov2LayerScale(Module)
    def __init__(self, dim, init_values, inplace)
    def forward(self, x)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
def _create_vision_transformer()
def _patch_layer_scale(model)
def vit_huge_patch16_224(pretrained)
class RADIOModelBase(Module)
    def __init__(self, model, patch_size, max_resolution)
    def num_cls_tokens(self)
    def patch_size(self)
    def max_resolution(self)
    def blocks(self)
    def embed_dim(self)
    def forward(self, x, feature_fmt)
def create_model_from_args(args)
class RADIOConfig(PretrainedConfig)
    """Pretrained Hugging Face configuration for RADIO models."""
    def __init__(self, args, version, patch_size, max_resolution, model_type, hidden_size)
    def to_dict(self)
class RADIOModel(PreTrainedModel)
    """Pretrained Hugging Face model for RADIO.

This class inherits from PreTrainedModel, which provides
HuggingFace's functionality for loading and saving models."""
    def __init__(self, config)
    def model(self)
    def num_summary_tokens(self)
    def patch_size(self)
    def forward(self, pixel_values, output_hidden_states, return_dict)
```

### policy/GR00T_XE/src/gr00t/model/backbone/eagle_backbone.py

```
class EagleBackbone(Module)
    def __init__(self, tune_llm, tune_visual, select_layer, reproject_vision, use_flash_attention, load_bf16, eagle_path, project_to_dim)
    def set_trainable_parameters(self, tune_llm, tune_visual)
    def set_frozen_modules_to_eval_mode(self)
    def prepare_input(self, batch)
    def forward_eagle(self, vl_input)
    def forward(self, vl_input)
```

### policy/GR00T_XE/src/gr00t/model/gr00t_n1.py

```
class GR00T_N1_5_Config(PretrainedConfig)
    def __init__(self)
class GR00T_N1_5(PreTrainedModel)
    def __init__(self, config, local_model_path)
    def validate_inputs(self, inputs)
    def validate_data(self, action_head_outputs, backbone_outputs, is_training)
    def forward(self, inputs)
    def get_action(self, inputs)
    def prepare_input(self, inputs)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### policy/GR00T_XE/src/gr00t/model/policy.py

```
class BasePolicy(ABC)
    def get_action(self, observations)
    def get_modality_config(self)
class Gr00tPolicy(BasePolicy)
    """A wrapper for Gr00t model checkpoints that handles loading the model, applying transforms,
making predictions, and unapplying transforms. This loads some custom configs, stats
and metadata related to the model checkpoints used
in the Gr00t model."""
    def __init__(self, model_path, embodiment_tag, modality_config, modality_transform, denoising_steps, device)
    def apply_transforms(self, obs)
    def unapply_transforms(self, action)
    def get_action(self, observations)
    def _get_action_from_normalized_input(self, normalized_input)
    def _get_unnormalized_action(self, normalized_action)
    def get_modality_config(self)
    def modality_config(self)
    def modality_transform(self)
    def video_delta_indices(self)
    def state_delta_indices(self)
    def denoising_steps(self)
    def denoising_steps(self, value)
    def _check_state_is_batched(self, obs)
    def _load_model(self, model_path)
    def _get_expected_action_dim(self)
    def _load_metadata(self, exp_cfg_dir)
    def _load_horizons(self)
    def _assert_delta_indices(self, delta_indices)
def unsqueeze_dict_values(data)
def squeeze_dict_values(data)
```

### policy/GR00T_XE/src/gr00t/model/transforms.py

```
def formalize_language(language)
def build_eagle_processor(eagle_path)
def collate(features, eagle_processor)
class DefaultDataCollator(DataCollatorMixin)
    def __init__(self, eagle_path)
    def __call__(self, features)
class GR00TTransform(InvertibleModalityTransform)
    def set_metadata(self, dataset_metadata)
    def get_embodiment_tag(self)
    def check_keys_and_batch_size(self, data)
    def _apply_vlm_processing(self, batch)
    def _prepare_video(self, data)
    def _prepare_language(self, data)
    def _prepare_state(self, data)
    def _prepare_action(self, data)
    def apply_single(self, data)
    def apply_batch(self, data, batch_size)
    def apply(self, data)
    def unapply(self, data)
    def __call__(self, data)
```

### policy/GR00T_XE/src/gr00t/utils/eval.py

```
def download_from_hg(repo_id, repo_type)
def calc_mse_for_single_trajectory(policy, dataset, traj_id, modality_keys, steps, action_horizon, plot, plot_state, save_plot_path)
def plot_trajectory(info, save_plot_path)
```

### policy/GR00T_XE/src/gr00t/utils/experiment.py

```
def safe_save_model_for_hf_trainer(trainer, output_dir)
class CheckpointFormatCallback(TrainerCallback)
    """This callback format checkpoint to make them standalone. For now, it copies all config
files to /checkpoint-{step}/experiment_cfg/:
- conf.yaml
- initial_actions.npz
- metadata.json"""
    def __init__(self, run_name, exp_cfg_dir)
    def on_save(self, args, state, control)
```

### policy/GR00T_XE/src/gr00t/utils/misc.py

```
"""Functions that work on nested structures of torch.Tensor or numpy array"""
def any_describe_str(x, shape_only)
def any_describe(x, msg)
```

### policy/GR00T_XE/src/gr00t/utils/peft.py

```
def copy_partial_action_expert_weights(old_dict, new_dict, old_dim, new_dim)
def _wrap_forward(model)
def get_lora_model(model, rank, lora_alpha, lora_dropout, action_head_only)
```

### policy/GR00T_XE/src/gr00t/utils/video.py

```
def get_frames_by_indices(video_path, indices, video_backend, video_backend_kwargs)
def get_frames_by_timestamps(video_path, timestamps, video_backend, video_backend_kwargs)
def get_all_frames(video_path, video_backend, video_backend_kwargs, resize_size)
```

### policy/GR00T_XE/src/model/action_head/action_encoder.py

```
def swish(x)
class SinusoidalPositionalEncoding(Module)
    """Produces a sinusoidal encoding of shape (B, T, w)
given timesteps of shape (B, T)."""
    def __init__(self, embedding_dim)
    def forward(self, timesteps)
class ActionEncoder(Module)
    def __init__(self, action_dim, hidden_size)
    def forward(self, actions, timesteps)
```

### policy/GR00T_XE/src/model/action_head/cross_attention_dit.py

```
class TimestepEncoder(Module)
    def __init__(self, embedding_dim, compute_dtype)
    def forward(self, timesteps)
class AdaLayerNorm(Module)
    def __init__(self, embedding_dim, norm_elementwise_affine, norm_eps, chunk_dim)
    def forward(self, x, temb)
class BasicTransformerBlock(Module)
    def __init__(self, dim, num_attention_heads, attention_head_dim, dropout, cross_attention_dim, activation_fn, attention_bias, upcast_attention, norm_elementwise_affine, norm_type, norm_eps, final_dropout, attention_type, positional_embeddings, num_positional_embeddings, ff_inner_dim, ff_bias, attention_out_bias)
    def forward(self, hidden_states, attention_mask, encoder_hidden_states, encoder_attention_mask, temb)
class DiT(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, norm_type, norm_elementwise_affine, norm_eps, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention, cross_attention_dim)
    def forward(self, hidden_states, encoder_hidden_states, timestep, encoder_attention_mask, return_all_hidden_states)
class SelfAttentionTransformer(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention)
    def forward(self, hidden_states, return_all_hidden_states)
```

### policy/GR00T_XE/src/model/action_head/flow_matching_action_head.py

```
class CategorySpecificLinear(Module)
    def __init__(self, num_categories, input_dim, hidden_dim)
    def forward(self, x, cat_ids)
class CategorySpecificMLP(Module)
    def __init__(self, num_categories, input_dim, hidden_dim, output_dim)
    def forward(self, x, cat_ids)
class MultiEmbodimentActionEncoder(Module)
    def __init__(self, action_dim, hidden_size, num_embodiments)
    def forward(self, actions, timesteps, cat_ids)
class FlowmatchingActionHeadConfig(PretrainedConfig)
    """NOTE: N1.5 uses XEmbFlowmatchingPolicyHeadConfig as action head"""
    def __init__(self)
class FlowmatchingActionHead(Module)
    def __init__(self, config)
    def set_trainable_parameters(self, tune_projector, tune_diffusion_model)
    def set_frozen_modules_to_eval_mode(self)
    def sample_time(self, batch_size, device, dtype)
    def prepare_input(self, batch)
    def process_backbone_output(self, backbone_output)
    def forward(self, backbone_output, action_input)
    def get_action(self, backbone_output, action_input)
    def device(self)
    def dtype(self)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/configuration_eagle2_5_vl.py

```
class Eagle2_5_VLConfig(PretrainedConfig)
    def __init__(self, vision_config, text_config, use_backbone_lora, use_llm_lora, pad2square, select_layer, force_image_size, downsample_ratio, template, dynamic_image_size, use_thumbnail, loss_version, min_dynamic_tiles, max_dynamic_tiles, mlp_checkpoint, initializer_range, _attn_implementation, _attn_implementation_autoset, llm_config, image_token_index, use_pixel_shuffle, mlp_connector_layers)
    def to_dict(self)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/image_processing_eagle2.py

```
"""Image processor class for LLaVa-Onevision."""
def crop(img, left, top, right, bottom, input_data_format)
def divide_to_patches(image, patch_size, input_data_format)
def expand_to_square(image, background_color, input_data_format)
def _get_patch_output_size(image, target_resolution, input_data_format)
class Eagle2ImageProcessor(BaseImageProcessor)
    """Constructs a LLaVa-Onevision image processor. Based on [`SiglipImageProcessor`] with incorporation of processing each video frame.

Args:
    do_resize (`bool`, *optional*, defaults to `True`):
        Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridde"""
    def __init__(self, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, min_dynamic_tiles, max_dynamic_tiles, use_thumbnail, pad_during_tiling)
    def pad(self, image, padding, mode, constant_values, data_format, input_data_format)
    def _resize_for_patching(self, image, target_resolution, resample, input_data_format)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, resample, data_format, input_data_format)
    def _pad_for_batching(self, pixel_values, data_format, input_data_format)
    def _preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_convert_rgb, data_format, input_data_format)
    def preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, return_tensors, data_format, input_data_format)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/image_processing_eagle2_5_vl_fast.py

```
def crop(img, left, top, right, bottom)
class Eagle2_5_VLFastImageProcessorKwargs(DefaultFastImageProcessorKwargs)
class Eagle2_5_VLImageProcessorFast(BaseImageProcessorFast)
    def __init__(self)
    def _prepare_images_structure(self, images)
    def _prepare_videos_structure(self, videos)
    def _prepare_input_videos(self, videos, do_convert_rgb, input_data_format, device)
    def _resize_for_patching(self, image, target_resolution, interpolation, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def _get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, interpolation, pad_during_tiling)
    def _pad_for_batching(self, pixel_values)
    def _preprocess(self, images, do_resize, size, max_dynamic_tiles, min_dynamic_tiles, use_thumbnail, pad_during_tiling, interpolation, do_center_crop, crop_size, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, return_tensors)
    def preprocess(self, images, videos)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/modeling_eagle2_5_vl.py

```
class Eagle2_5_VLPreTrainedModel(PreTrainedModel)
    def _init_weights(self, module)
class Eagle2_5_VLForConditionalGeneration(Eagle2_5_VLPreTrainedModel, GenerationMixin)
    def __init__(self, config, vision_model, language_model)
    def check_forward_kwargs(self)
    def wrap_backbone_lora(self, r, lora_alpha, lora_dropout)
    def wrap_llm_lora(self, r, lora_alpha, lora_dropout)
    def forward(self, pixel_values, input_ids, attention_mask, position_ids, image_flags, past_key_values, labels, use_cache, output_attentions, output_hidden_states, return_dict, num_tiles_list)
    def pixel_shuffle(self, x, scale_factor)
    def extract_feature(self, pixel_values)
    def generate(self, pixel_values, input_ids, attention_mask, visual_features, generation_config, output_hidden_states, image_sizes)
    def get_input_embeddings(self)
    def set_input_embeddings(self, value)
    def get_output_embeddings(self)
    def set_output_embeddings(self, new_embeddings)
    def set_decoder(self, decoder)
    def get_decoder(self)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/processing_eagle2_5_vl.py

```
"""Processor class for Eagle2_5_VL.
copy from https://github.com/huggingface/transformers/blob/main/src/transformers/models/llava_onevision/processing_llava_onevision.py"""
def adjust_by_factor(number, factor, method)
def to_rgb(pil_image)
def fetch_image(ele)
def smart_nframes(ele, total_frames, video_fps)
def _read_video_torchvision(ele)
def is_decord_available()
def _read_video_decord(ele)
def get_video_reader_backend()
def fetch_video(ele, return_video_sample_fps)
class Eagle2_5_VLProcessorKwargs(ProcessingKwargs)
class Eagle2_5_VLProcessor(ProcessorMixin)
    """Constructs a Eagle2_5_VL processor which wraps a Eagle2_5_VL video processor, Eagle2_5_VL image processor and a Eagle2_5_VL tokenizer into a single processor.

[`Eagle2_5_VLProcessor`] offers all the functionalities of [`Eagle2_5_VLVideoProcessor`], [`Eagle2_5_VLImageProcessor`] and [`Eagle2_5_VLTok"""
    def __init__(self, image_processor, tokenizer, vision_feature_select_strategy, chat_template, image_token, video_token, tokens_per_tile, image_placeholder, video_placeholder, image_start_token, image_end_token)
    def replace_media_placeholder(self, text, image_list, video_list, timestamps_list, fps_list)
    def __call__(self, images, text, audio, videos)
    def get_number_tiles_based_on_image_size(self, image_size, min_num, max_num, use_thumbnail, tile_size)
    def batch_decode(self)
    def decode(self)
    def model_input_names(self)
    def save_pretrained(self, save_directory)
    def from_pretrained(cls, pretrained_model_name_or_path)
    def process_vision_info(self, conversations, return_video_kwargs)
    def extract_vision_info(self, conversations)
    def py_apply_chat_template(self, messages, tokenize, add_generation_prompt)
    def from_args_and_dict(cls, args, processor_dict)
```

### policy/GR00T_XE/src/model/backbone/eagle2_hg_model/radio_model.py

```
class FlashAttention(Module)
    """Implement the scaled dot product attention with softmax.
Arguments
---------
    softmax_scale: The temperature to use for the softmax attention.
                  (default: 1/sqrt(d_keys) where d_keys is computed at
                  runtime)
    attention_dropout: The dropout rate to apply to the """
    def __init__(self, softmax_scale, attention_dropout, device, dtype)
    def forward(self, qkv, key_padding_mask, causal, cu_seqlens, max_s, need_weights)
def _flash_attn(self, x)
def forward(self, x)
def replace_vit_attn_with_flash_attn()
class ClsToken(Module)
    def __init__(self, ndim, num_tokens, enabled, register_multiple, num_registers)
    def disable(self)
    def forward(self, x)
    def no_weight_decay(self)
class ViTPatchGenerator(Module)
    def __init__(self, patch_size, embed_dim, input_dims, abs_pos, normalize_patches, cls_token, max_input_dims, pos_dropout, return_pos_enc, num_cls_tokens, register_multiple, num_registers, patch_bias, device, dtype)
    def forward(self, x)
    def apply_cls_token(self)
    def num_cls_tokens(self)
    def num_registers(self)
    def num_skip(self)
    def no_weight_decay(self)
    def _load_projection(self, src_proj_weight, targ_proj_weight)
    def embed_patches(self, x)
    def apply_pos_enc(self, patches, patch_idxs, input_size)
    def get_pos_enc(self, batch_size, patch_idxs, input_size)
    def _get_pos_embeddings(self, batch_size, input_dims)
class Im2Patches(Module)
    def __init__(self, patch_size)
    def forward(self, x)
class ViTPatchLinear(Linear)
    def __init__(self, patch_size, embed_dim, bias)
def _forward_cpe(self, x)
def _take_indices(num_blocks, n)
def _enable_cpe_for_timm_vit(model, max_img_size, num_cls_tokens, pos_dropout, register_multiple, num_registers)
def enable_cpe(model)
class Dinov2LayerScale(Module)
    def __init__(self, dim, init_values, inplace)
    def forward(self, x)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
def _create_vision_transformer()
def _patch_layer_scale(model)
def vit_huge_patch16_224(pretrained)
class RADIOModelBase(Module)
    def __init__(self, model, patch_size, max_resolution)
    def num_cls_tokens(self)
    def patch_size(self)
    def max_resolution(self)
    def blocks(self)
    def embed_dim(self)
    def forward(self, x, feature_fmt)
def create_model_from_args(args)
class RADIOConfig(PretrainedConfig)
    """Pretrained Hugging Face configuration for RADIO models."""
    def __init__(self, args, version, patch_size, max_resolution, model_type, hidden_size)
    def to_dict(self)
class RADIOModel(PreTrainedModel)
    """Pretrained Hugging Face model for RADIO.

This class inherits from PreTrainedModel, which provides
HuggingFace's functionality for loading and saving models."""
    def __init__(self, config)
    def model(self)
    def num_summary_tokens(self)
    def patch_size(self)
    def forward(self, pixel_values, output_hidden_states, return_dict)
```

### policy/GR00T_XE/src/model/backbone/eagle_backbone.py

```
class EagleBackbone(Module)
    def __init__(self, tune_llm, tune_visual, select_layer, reproject_vision, use_flash_attention, load_bf16, eagle_path, project_to_dim)
    def set_trainable_parameters(self, tune_llm, tune_visual)
    def set_frozen_modules_to_eval_mode(self)
    def prepare_input(self, batch)
    def forward_eagle(self, vl_input)
    def forward(self, vl_input)
```

### policy/GR00T_XE/src/model/gr00t_n1.py

```
class GR00T_N1_5_Config(PretrainedConfig)
    def __init__(self)
class GR00T_N1_5(PreTrainedModel)
    def __init__(self, config, local_model_path)
    def validate_inputs(self, inputs)
    def validate_data(self, action_head_outputs, backbone_outputs, is_training)
    def forward(self, inputs)
    def get_action(self, inputs)
    def prepare_input(self, inputs)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### policy/GR00T_XE/src/model/policy.py

```
class BasePolicy(ABC)
    def get_action(self, observations)
    def get_modality_config(self)
class Gr00tPolicy(BasePolicy)
    """A wrapper for Gr00t model checkpoints that handles loading the model, applying transforms,
making predictions, and unapplying transforms. This loads some custom configs, stats
and metadata related to the model checkpoints used
in the Gr00t model."""
    def __init__(self, model_path, embodiment_tag, modality_config, modality_transform, denoising_steps, device)
    def apply_transforms(self, obs)
    def unapply_transforms(self, action)
    def get_action(self, observations)
    def _get_action_from_normalized_input(self, normalized_input)
    def _get_unnormalized_action(self, normalized_action)
    def get_modality_config(self)
    def modality_config(self)
    def modality_transform(self)
    def video_delta_indices(self)
    def state_delta_indices(self)
    def denoising_steps(self)
    def denoising_steps(self, value)
    def _check_state_is_batched(self, obs)
    def _load_model(self, model_path)
    def _get_expected_action_dim(self)
    def _load_metadata(self, exp_cfg_dir)
    def _load_horizons(self)
    def _assert_delta_indices(self, delta_indices)
def unsqueeze_dict_values(data)
def squeeze_dict_values(data)
```

### policy/GR00T_XE/src/model/transforms.py

```
def formalize_language(language)
def build_eagle_processor(eagle_path)
def collate(features, eagle_processor)
class DefaultDataCollator(DataCollatorMixin)
    def __init__(self, eagle_path)
    def __call__(self, features)
class GR00TTransform(InvertibleModalityTransform)
    def set_metadata(self, dataset_metadata)
    def get_embodiment_tag(self)
    def check_keys_and_batch_size(self, data)
    def _apply_vlm_processing(self, batch)
    def _prepare_video(self, data)
    def _prepare_language(self, data)
    def _prepare_state(self, data)
    def _prepare_action(self, data)
    def apply_single(self, data)
    def apply_batch(self, data, batch_size)
    def apply(self, data)
    def unapply(self, data)
    def __call__(self, data)
```

### policy/GR00T_XE/src/utils/eval.py

```
def download_from_hg(repo_id, repo_type)
def calc_mse_for_single_trajectory(policy, dataset, traj_id, modality_keys, steps, action_horizon, plot, plot_state, save_plot_path)
def plot_trajectory(info, save_plot_path)
```

### policy/GR00T_XE/src/utils/experiment.py

```
def safe_save_model_for_hf_trainer(trainer, output_dir)
class CheckpointFormatCallback(TrainerCallback)
    """This callback format checkpoint to make them standalone. For now, it copies all config
files to /checkpoint-{step}/experiment_cfg/:
- conf.yaml
- initial_actions.npz
- metadata.json"""
    def __init__(self, run_name, exp_cfg_dir)
    def on_save(self, args, state, control)
```

### policy/GR00T_XE/src/utils/misc.py

```
"""Functions that work on nested structures of torch.Tensor or numpy array"""
def any_describe_str(x, shape_only)
def any_describe(x, msg)
```

### policy/GR00T_XE/src/utils/peft.py

```
def copy_partial_action_expert_weights(old_dict, new_dict, old_dim, new_dim)
def _wrap_forward(model)
def get_lora_model(model, rank, lora_alpha, lora_dropout, action_head_only)
```

### policy/GR00T_XE/src/utils/video.py

```
def get_frames_by_indices(video_path, indices, video_backend, video_backend_kwargs)
def get_frames_by_timestamps(video_path, timestamps, video_backend, video_backend_kwargs)
def get_all_frames(video_path, video_backend, video_backend_kwargs, resize_size)
```

### policy/GR00T_XE/xe_config.py

```
"""Cross-Embodiment data config for GR00T XE.

Extends the Dex2Bench config with:
  - max_action_dim=64  (unified cross-embodiment action space)
  - max_state_dim=64   (unified obs space)
  - action_mask support (embodiment-aware loss masking)"""
def _camera_mode()
def _video_keys()
class Dex2BenchXEDataConfig(BaseDataConfig)
    """Cross-embodiment 4-cam RGB + unified state/action + action_mask."""
    def modality_config(self)
    def transform(self)
```

### policy/GR00T_XE/xe_hand_mapping.py

```
"""Single source of truth for the cross-embodiment hand joint → unified-slot mapping.

Both the training dataset (:mod:`dataset`) and the online/offline converter
(:mod:`ik_arm_converter`) resolve a robot's hand joints into the 64-D unified
space through THIS module, so the two paths cannot drift apart (memory rule:
train/inference logic that is duplicated must reference each other).

Three places must stay consistent if the layout ever changes:

* ``embodiment_mapping.yml``  — authored per-robot joint → semantic slot (44)
* ``xe_hand_mapping.py``      — parses the YAML into lookup dicts + valida"""
def robot_key_to_hand_name(robot_key)
def _load_raw_mapping()
def authored_slots(hand_name)
def build_name_to_slot_maps(hand_name)
def expected_joint_names(hand_name)
def validate_hand_coverage(robot_key, actual_joint_names)
```

### policy/GR00T_XE/xe_norm_stats.py

```
"""GR00T XE normalization statistics -- single source of truth.

The unified 64D vector mixes two quantities whose normalization requirements are
opposite:

  dims  0:12   arm EE, 2 x (x, y, z, roll, pitch, yaw), expressed in the SHARED
               world frame (H1).  One physical pose must map to one number no
               matter which robot produced it, so these dims use statistics
               pooled over the whole corpus.
  dims 12:56   hand joint slots (right 12:33, left 34:55).  Joint ranges differ
               per robot and so does the slot layout, so these use the OWNING
         """
def repo_artifact_path()
def task_dir_key(input_dir)
def _bad(path, msg)
def _check_len(stats, n, who, path)
def validate_artifact(art, path)
def load_artifact(path)
def install_artifact(dest_dir, artifact)
def assemble(robot_key, art)
def check_task_against_artifact(stats, robot_key, input_dir, art)
def _state_action_transforms(transforms)
def _verify(transforms, built, robot_key)
def apply_to_transform(transforms, metadata, robot_key)
def _read_metadata_json(exp_cfg_dir, embodiment_tag)
def reapply_for_deploy(transforms, exp_cfg_dir, embodiment_tag, robot_key)
def utc_now()
```

### policy/GR00T_n15/__init__.py

```
"""Dex2bench integration for vendored Isaac-GR00T N1.5."""
```

### policy/GR00T_n15/convert_dex2bench_to_gr00t.py

```
"""Convert dex2bench raw HDF5 replay episodes to GR00T LeRobot format."""
class EpisodePayload()
def _decode_hdf5_string(value)
def _task_from_episode(ep, fallback, prompt)
def _fps_from_episode(ep)
def _valid_indices(ep)
def _find_homing_cutoff(ep, ep_len_full, valid_indices)
def _decode_rgb_frame(frame)
def _read_camera(ep, camera_id, indices)
def _read_episode(path, camera_map)
def _stats(values)
def _write_jsonl(path, rows)
def _write_video(path, frames, fps)
def _feature_for_video(frames, fps)
def convert_dataset(input_dir, output_dir)
def _default_output_dir(repo_id)
def _parse_camera_map(items, use_default)
def main()
```

### policy/GR00T_n15/deploy_policy.py

```
"""Dex2bench deployment adapter for the vendored Isaac-GR00T N1.5 policy."""
def _split_csv_env(value)
def _normalize_camera_mode(value)
def _video_keys_from_env()
def _as_uint8_rgb(image)
def _read_camera(observation)
def _maybe_select_active(qpos)
def _read_qpos(observation)
def _optional_int(value, name)
def _validate_local_checkpoint(model_path)
def encode_obs(observation)
class Dex2BenchGR00TPolicy()
    def __init__(self, usr_args)
    def _to_numpy_action(value)
    def get_action(self, obs)
def get_model(usr_args)
def reset_model(model)
```

### policy/GR00T_n15/gr00t_dex2bench_config.py

```
"""GR00T data config for dex2bench joint-position policies."""
def _split_csv_env(value)
def _camera_mode()
def _video_keys()
class Dex2BenchGR00TDataConfig(BaseDataConfig)
    """Configurable RGB camera set plus a single qpos state/action vector."""
    def modality_config(self)
    def transform(self)
```

### policy/GR00T_n15/gr00t_hdf5_dataset.py

```
"""PyTorch Dataset that reads dex2bench HDF5 episodes directly, bypassing LeRobot conversion.

Produces the same raw-data dict format as ``LeRobotSingleDataset.get_step_data``,
so the existing GR00T transform pipeline (VideoToTensor, StateActionTransform, etc.)
applies unchanged.

Usage::

    from gr00t_hdf5_dataset import Dex2BenchHDF5Dataset

    ds = Dex2BenchHDF5Dataset(
        input_dir="/path/to/replay-generalization",
        camera_map={"stereo_left": "cam_stereo_left", ...},
        modality_configs=modality_configs,
        transforms=transforms,
        embodiment_tag="new_embodiment"""
def _decode_hdf5_string(value)
def _decode_rgb_frame(frame)
def _valid_indices(ep)
def _find_homing_cutoff(ep, ep_len_full, valid_indices)
class Dex2BenchHDF5Dataset(Dataset)
    """Read dex2bench HDF5 episodes and apply GR00T transforms directly.

Parameters
----------
input_dir : Path or str
    Directory containing ``episode_*.hdf5`` files.
camera_map : dict[str, str]
    Mapping from GR00T video sub-keys (e.g. ``"stereo_left"``) to HDF5
    camera IDs (e.g. ``"cam_stereo_le"""
    def __init__(self, input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, active_dof_info, state_dim, action_dim, seed, truncate_at_homing)
    def metadata(self)
    def tag(self)
    def modality_configs(self)
    def transforms(self)
    def dataset_name(self)
    def trajectory_ids(self)
    def trajectory_lengths(self)
    def all_steps(self)
    def max_delta(self)
    def set_epoch(self, epoch)
    def _compute_statistics(self)
    def _build_metadata(self, stats)
    def _get_episode(self, ep_idx)
    def get_step_data(self, ep_idx, local_valid_idx)
    def __len__(self)
    def __getitem__(self, idx)
    def __del__(self)
def build_hdf5_dataset(input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, use_active_dof, robot_key, state_dim, action_dim, truncate_at_homing)
```

### policy/GR00T_n15/scripts/eval_policy.py

```
class ArgsConfig()
    """Configuration for evaluating a policy."""
def main(args)
```

### policy/GR00T_n15/scripts/gr00t_finetune.py

```
class ArgsConfig()
    """Configuration for GR00T model fine-tuning."""
def _parse_hdf5_camera_map(items)
class MilestoneSaveCallback(TrainerCallback)
    """Copy the checkpoint to a ``checkpoint-milestone-{step}`` directory when
*step* is a multiple of *milestone_steps*.  HF's ``_rotate_checkpoints``
only touches ``checkpoint-<digits>``, so these milestone copies are safe
from deletion regardless of ``save_total_limit``."""
    def __init__(self, milestone_steps)
    def on_save(self, args, state, control)
def main(config)
```

### policy/GR00T_n15/scripts/load_dataset.py

```
"""This script is a replication of the notebook `getting_started/load_dataset.ipynb`"""
def print_yellow(text)
class ArgsConfig()
    """Configuration for loading the dataset."""
def get_modality_keys(dataset_path)
def plot_state_action_space(state_dict, action_dict, shared_keys)
def plot_image(image)
def load_dataset(dataset_path, embodiment_tag, video_backend, steps, plot_state_action)
```

### policy/GR00T_n15/scripts/merge_lora.py

```
"""Merge LoRA adapter into base model and resize action head to match data dim.

Usage:
    python policy/GR00T_n15/scripts/merge_lora.py         --base-model ../groot/groot_baseline_ckpt         --checkpoint ../groot/06_lora/checkpoint-10000         --output ../groot/06_lora/merged         --action-dim 36"""
def copy_partial_action_expert_weights(old_dict, new_dict, old_dim, new_dim)
def main()
```

### policy/GR00T_n15/src/gr00t/eval/http_server.py

```
"""GR00T HTTP Server Module

This module provides HTTP server functionality for GR00T model inference.
It exposes a REST API for easy integration with web applications and other services.

Dependencies:
    => Server: `pip install uvicorn fastapi json-numpy`
    => Client: `pip install requests json-numpy`"""
class HTTPInferenceServer()
    def __init__(self, policy, port, host, api_token)
    def predict_action(self, payload)
    def health_check(self)
    def run(self)
def create_http_server(policy, port, host, api_token)
```

### policy/GR00T_n15/src/gr00t/eval/robot.py

```
class RobotInferenceServer(BaseInferenceServer)
    """Server with three endpoints for real robot policies"""
    def __init__(self, model, host, port, api_token)
    def start_server(policy, port, api_token)
class RobotInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for communicating with the RealRobotServer"""
    def __init__(self, host, port, api_token)
    def get_action(self, observations)
    def get_modality_config(self)
```

### policy/GR00T_n15/src/gr00t/eval/service.py

```
class MsgSerializer()
    def to_bytes(data)
    def from_bytes(data)
    def decode_custom_classes(obj)
    def encode_custom_classes(obj)
class EndpointHandler()
class BaseInferenceServer()
    """An inference server that spin up a ZeroMQ socket and listen for incoming requests.
Can add custom endpoints by calling `register_endpoint`."""
    def __init__(self, host, port, api_token)
    def _kill_server(self)
    def _handle_ping(self)
    def register_endpoint(self, name, handler, requires_input)
    def _validate_token(self, request)
    def run(self)
class BaseInferenceClient()
    def __init__(self, host, port, timeout_ms, api_token)
    def _init_socket(self)
    def ping(self)
    def kill_server(self)
    def call_endpoint(self, endpoint, data, requires_input)
    def __del__(self)
class ExternalRobotInferenceClient(BaseInferenceClient)
    """Client for communicating with the RealRobotServer"""
    def get_action(self, observations)
```

### policy/GR00T_n15/src/gr00t/eval/simulation.py

```
class VideoConfig()
    """Configuration for video recording settings."""
class MultiStepConfig()
    """Configuration for multi-step environment settings."""
class SimulationConfig()
    """Main configuration for simulation environment."""
class SimulationInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for running simulations and communicating with the inference server."""
    def __init__(self, host, port)
    def get_action(self, observations)
    def get_modality_config(self)
    def setup_environment(self, config)
    def run_simulation(self, config)
    def _get_actions_from_server(self, observations)
def _create_single_env(config, idx)
def run_evaluation(env_name, host, port, video_dir, n_episodes, n_envs, n_action_steps, max_episode_steps)
```

### policy/GR00T_n15/src/gr00t/eval/wrappers/multistep_wrapper.py

```
def stack_repeated(x, n, loc)
def repeated_box(box_space, n, loc)
def repeated_space(space, n, loc)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def aggregate(data, method)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices, n_action_steps, max_episode_steps, reward_agg_method)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def get_max_steps_needed(self)
    def assert_delta_indices(self, delta_indices, horizon)
    def reset(self, seed, options)
    def step(self, action)
    def _get_obs(self, video_delta_indices, state_delta_indices)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def get_infos(self)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        """
        For video, the observation space will be (video_horizon,) + original shape
        For state (if not None), the observation space will be (state_horizon,) + original shape
        """
        new_observation_space = {}
        for k in observation_space.keys():
            if k.startswith("video"):
                box = observation_space[k]
                horizon = video_horizon
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("state"):
                box = observation_space[k]
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("annotation"):
                text = observation_space[k]
                new_observation_space[k] = text
            else:
                raise ValueError(f"Unknown key: {k}")  # NOTE: We might add "language" in the future

        return spaces.Dict(new_observation_space)
```

```python
def _get_obs(self, video_delta_indices, state_delta_indices):
        """
        Output:
        For video: (video_horizon,) + obs_shape
        For state (if not None): (state_horizon,) + obs_shape
        """
        assert len(self.obs) > 0
        if isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                if key.startswith("video"):
                    """
                    NOTE:
                      We need to subtract 1 because video_delta_indices is 0-indexed.
                      E.g., video_delta_indices = np.array([-4, -3, -2, -1, 0])
                      Then when we select the observation,
                        it should be [obs[-5], obs[-4], obs[-3], obs[-2], obs[-1]]
                      (i.e., the latest observation is at the last index)
                    """
                    delta_indices = video_delta_indices - 1
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("state"):
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("annotation"):
                    result[key] = self.obs[-1][key]
                else:
                    raise ValueError(f"Unknown key: {key}")
            return result
        else:
            raise RuntimeError(f"Unsupported space type: {type(self.observation_space)=}")
```

```python
def get_rewards(self):
        return self.reward
```
```

### policy/GR00T_n15/src/gr00t/eval/wrappers/obs_index_selection_wrapper.py

```
class ObsIndexSelectionWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices)
    def assert_delta_indices(self, delta_indices, horizon)
    def select_steps_for_values(self, data_value, delta_indices)
    def select_steps_for_obs(self, obs)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def reset(self, seed, options)
    def step(self, action)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        new_observation_space = {}
        for k in observation_space.keys():
            box = observation_space[k]
            if k.startswith("video"):
                horizon = video_horizon
            elif k.startswith("state"):
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
            else:
                raise ValueError(f"Unknown key: {k}")

            new_observation_space[k] = gym.spaces.Box(
                low=box.low[:horizon],
                high=box.high[:horizon],
                shape=(horizon, *box.shape[1:]),
                dtype=box.dtype,
            )
        return gym.spaces.Dict(new_observation_space)
```
```

### policy/GR00T_n15/src/gr00t/eval/wrappers/video_recording_wrapper.py

```
def get_accumulate_timestamp_idxs(timestamps, start_time, dt, eps, next_global_idx, allow_negative)
class VideoRecorder()
    def __init__(self, fps, codec, input_pix_fmt)
    def _reset_state(self)
    def create_h264(cls, fps, codec, input_pix_fmt, output_pix_fmt, crf, profile)
    def __del__(self)
    def is_ready(self)
    def start(self, file_path, start_time)
    def write_frame(self, img, frame_time)
    def stop(self)
class VideoRecordingWrapper(Wrapper)
    def __init__(self, env, video_recorder, mode, video_dir, steps_per_render)
    def reset(self)
    def step(self, action)
    def render(self, mode)
```

### policy/GR00T_n15/src/gr00t/experiment/data_config.py

```
class BaseDataConfig(ABC)
    def modality_config(self)
    def transform(self)
def import_external_data_config(data_config_str)
def load_data_config(data_config_str)
class FourierGr1ArmsOnlyDataConfig(BaseDataConfig)
    def transform(self)
class So100DataConfig(BaseDataConfig)
    def transform(self)
class So100DualCamDataConfig(So100DataConfig)
class UnitreeG1DataConfig(BaseDataConfig)
    def transform(self)
class UnitreeG1FullBodyDataConfig(UnitreeG1DataConfig)
class FourierGr1FullUpperBodyDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaGripperDataConfig(BaseDataConfig)
    def transform(self)
class BimanualPandaHandDataConfig(BimanualPandaGripperDataConfig)
class SinglePandaGripperDataConfig(BimanualPandaGripperDataConfig)
class FourierGr1ArmsWaistDataConfig(FourierGr1ArmsOnlyDataConfig)
    def transform(self)
class OxeDroidDataConfig(BaseDataConfig)
    def transform(self)
class AgibotGenie1DataConfig(BaseDataConfig)
    def transform(self)
```

### policy/GR00T_n15/src/gr00t/experiment/runner.py

```
class TrainRunner()
    def __init__(self, model, training_args, train_dataset, resume_from_checkpoint)
    def create_trainer(self, model, training_args, train_dataset, data_collator, compute_dtype, global_batch_size)
    def train(self)
    def _cleanup_output(self)
```

### policy/GR00T_n15/src/gr00t/experiment/trainer.py

```
class BaseSampler(Sampler)
    """Sampler for dataset, which enables `set_epoch` for Dataset.
`set_epoch` will be called by huggingface Trainer at the end of each epoch.
`shuffle` is also supported for training set shuffling"""
    def __init__(self, data_source, shuffle, seed)
    def __iter__(self)
    def set_epoch(self, epoch)
    def __len__(self)
class DualBrainTrainer(Trainer)
    def __init__(self)
    def _get_train_sampler(self)
    def _get_eval_sampler(self, eval_dataset)
    def compute_loss(self, model, inputs, return_outputs, num_items_in_batch)
    def create_optimizer(self)
    def save_model(self, output_dir, _internal_call)
    def train(self, resume_from_checkpoint, trial, ignore_keys_for_eval)
```

### policy/GR00T_n15/src/gr00t/model/action_head/action_encoder.py

```
def swish(x)
class SinusoidalPositionalEncoding(Module)
    """Produces a sinusoidal encoding of shape (B, T, w)
given timesteps of shape (B, T)."""
    def __init__(self, embedding_dim)
    def forward(self, timesteps)
class ActionEncoder(Module)
    def __init__(self, action_dim, hidden_size)
    def forward(self, actions, timesteps)
```

### policy/GR00T_n15/src/gr00t/model/action_head/cross_attention_dit.py

```
class TimestepEncoder(Module)
    def __init__(self, embedding_dim, compute_dtype)
    def forward(self, timesteps)
class AdaLayerNorm(Module)
    def __init__(self, embedding_dim, norm_elementwise_affine, norm_eps, chunk_dim)
    def forward(self, x, temb)
class BasicTransformerBlock(Module)
    def __init__(self, dim, num_attention_heads, attention_head_dim, dropout, cross_attention_dim, activation_fn, attention_bias, upcast_attention, norm_elementwise_affine, norm_type, norm_eps, final_dropout, attention_type, positional_embeddings, num_positional_embeddings, ff_inner_dim, ff_bias, attention_out_bias)
    def forward(self, hidden_states, attention_mask, encoder_hidden_states, encoder_attention_mask, temb)
class DiT(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, norm_type, norm_elementwise_affine, norm_eps, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention, cross_attention_dim)
    def forward(self, hidden_states, encoder_hidden_states, timestep, encoder_attention_mask, return_all_hidden_states)
class SelfAttentionTransformer(ModelMixin, ConfigMixin)
    def __init__(self, num_attention_heads, attention_head_dim, output_dim, num_layers, dropout, attention_bias, activation_fn, num_embeds_ada_norm, upcast_attention, max_num_positional_embeddings, compute_dtype, final_dropout, positional_embeddings, interleave_self_attention)
    def forward(self, hidden_states, return_all_hidden_states)
```

### policy/GR00T_n15/src/gr00t/model/action_head/flow_matching_action_head.py

```
class CategorySpecificLinear(Module)
    def __init__(self, num_categories, input_dim, hidden_dim)
    def forward(self, x, cat_ids)
class CategorySpecificMLP(Module)
    def __init__(self, num_categories, input_dim, hidden_dim, output_dim)
    def forward(self, x, cat_ids)
class MultiEmbodimentActionEncoder(Module)
    def __init__(self, action_dim, hidden_size, num_embodiments)
    def forward(self, actions, timesteps, cat_ids)
class FlowmatchingActionHeadConfig(PretrainedConfig)
    """NOTE: N1.5 uses XEmbFlowmatchingPolicyHeadConfig as action head"""
    def __init__(self)
class FlowmatchingActionHead(Module)
    def __init__(self, config)
    def set_trainable_parameters(self, tune_projector, tune_diffusion_model)
    def set_frozen_modules_to_eval_mode(self)
    def sample_time(self, batch_size, device, dtype)
    def prepare_input(self, batch)
    def process_backbone_output(self, backbone_output)
    def forward(self, backbone_output, action_input)
    def get_action(self, backbone_output, action_input)
    def device(self)
    def dtype(self)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/configuration_eagle2_5_vl.py

```
class Eagle2_5_VLConfig(PretrainedConfig)
    def __init__(self, vision_config, text_config, use_backbone_lora, use_llm_lora, pad2square, select_layer, force_image_size, downsample_ratio, template, dynamic_image_size, use_thumbnail, loss_version, min_dynamic_tiles, max_dynamic_tiles, mlp_checkpoint, initializer_range, _attn_implementation, _attn_implementation_autoset, llm_config, image_token_index, use_pixel_shuffle, mlp_connector_layers)
    def to_dict(self)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/image_processing_eagle2.py

```
"""Image processor class for LLaVa-Onevision."""
def crop(img, left, top, right, bottom, input_data_format)
def divide_to_patches(image, patch_size, input_data_format)
def expand_to_square(image, background_color, input_data_format)
def _get_patch_output_size(image, target_resolution, input_data_format)
class Eagle2ImageProcessor(BaseImageProcessor)
    """Constructs a LLaVa-Onevision image processor. Based on [`SiglipImageProcessor`] with incorporation of processing each video frame.

Args:
    do_resize (`bool`, *optional*, defaults to `True`):
        Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridde"""
    def __init__(self, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, min_dynamic_tiles, max_dynamic_tiles, use_thumbnail, pad_during_tiling)
    def pad(self, image, padding, mode, constant_values, data_format, input_data_format)
    def _resize_for_patching(self, image, target_resolution, resample, input_data_format)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, resample, data_format, input_data_format)
    def _pad_for_batching(self, pixel_values, data_format, input_data_format)
    def _preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_convert_rgb, data_format, input_data_format)
    def preprocess(self, images, do_resize, size, resample, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, do_convert_rgb, return_tensors, data_format, input_data_format)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/image_processing_eagle2_5_vl_fast.py

```
def crop(img, left, top, right, bottom)
class Eagle2_5_VLFastImageProcessorKwargs(DefaultFastImageProcessorKwargs)
class Eagle2_5_VLImageProcessorFast(BaseImageProcessorFast)
    def __init__(self)
    def _prepare_images_structure(self, images)
    def _prepare_videos_structure(self, videos)
    def _prepare_input_videos(self, videos, do_convert_rgb, input_data_format, device)
    def _resize_for_patching(self, image, target_resolution, interpolation, input_data_format)
    def find_closest_aspect_ratio(self, aspect_ratio, target_ratios, width, height, image_size)
    def _pad_for_patching(self, image, target_resolution, input_data_format)
    def _get_image_patches(self, image, min_num, max_num, size, tile_size, use_thumbnail, interpolation, pad_during_tiling)
    def _pad_for_batching(self, pixel_values)
    def _preprocess(self, images, do_resize, size, max_dynamic_tiles, min_dynamic_tiles, use_thumbnail, pad_during_tiling, interpolation, do_center_crop, crop_size, do_rescale, rescale_factor, do_normalize, image_mean, image_std, do_pad, return_tensors)
    def preprocess(self, images, videos)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/modeling_eagle2_5_vl.py

```
class Eagle2_5_VLPreTrainedModel(PreTrainedModel)
    def _init_weights(self, module)
class Eagle2_5_VLForConditionalGeneration(Eagle2_5_VLPreTrainedModel, GenerationMixin)
    def __init__(self, config, vision_model, language_model)
    def check_forward_kwargs(self)
    def wrap_backbone_lora(self, r, lora_alpha, lora_dropout)
    def wrap_llm_lora(self, r, lora_alpha, lora_dropout)
    def forward(self, pixel_values, input_ids, attention_mask, position_ids, image_flags, past_key_values, labels, use_cache, output_attentions, output_hidden_states, return_dict, num_tiles_list)
    def pixel_shuffle(self, x, scale_factor)
    def extract_feature(self, pixel_values)
    def generate(self, pixel_values, input_ids, attention_mask, visual_features, generation_config, output_hidden_states, image_sizes)
    def get_input_embeddings(self)
    def set_input_embeddings(self, value)
    def get_output_embeddings(self)
    def set_output_embeddings(self, new_embeddings)
    def set_decoder(self, decoder)
    def get_decoder(self)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/processing_eagle2_5_vl.py

```
"""Processor class for Eagle2_5_VL.
copy from https://github.com/huggingface/transformers/blob/main/src/transformers/models/llava_onevision/processing_llava_onevision.py"""
def adjust_by_factor(number, factor, method)
def to_rgb(pil_image)
def fetch_image(ele)
def smart_nframes(ele, total_frames, video_fps)
def _read_video_torchvision(ele)
def is_decord_available()
def _read_video_decord(ele)
def get_video_reader_backend()
def fetch_video(ele, return_video_sample_fps)
class Eagle2_5_VLProcessorKwargs(ProcessingKwargs)
class Eagle2_5_VLProcessor(ProcessorMixin)
    """Constructs a Eagle2_5_VL processor which wraps a Eagle2_5_VL video processor, Eagle2_5_VL image processor and a Eagle2_5_VL tokenizer into a single processor.

[`Eagle2_5_VLProcessor`] offers all the functionalities of [`Eagle2_5_VLVideoProcessor`], [`Eagle2_5_VLImageProcessor`] and [`Eagle2_5_VLTok"""
    def __init__(self, image_processor, tokenizer, vision_feature_select_strategy, chat_template, image_token, video_token, tokens_per_tile, image_placeholder, video_placeholder, image_start_token, image_end_token)
    def replace_media_placeholder(self, text, image_list, video_list, timestamps_list, fps_list)
    def __call__(self, images, text, audio, videos)
    def get_number_tiles_based_on_image_size(self, image_size, min_num, max_num, use_thumbnail, tile_size)
    def batch_decode(self)
    def decode(self)
    def model_input_names(self)
    def save_pretrained(self, save_directory)
    def from_pretrained(cls, pretrained_model_name_or_path)
    def process_vision_info(self, conversations, return_video_kwargs)
    def extract_vision_info(self, conversations)
    def py_apply_chat_template(self, messages, tokenize, add_generation_prompt)
    def from_args_and_dict(cls, args, processor_dict)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle2_hg_model/radio_model.py

```
class FlashAttention(Module)
    """Implement the scaled dot product attention with softmax.
Arguments
---------
    softmax_scale: The temperature to use for the softmax attention.
                  (default: 1/sqrt(d_keys) where d_keys is computed at
                  runtime)
    attention_dropout: The dropout rate to apply to the """
    def __init__(self, softmax_scale, attention_dropout, device, dtype)
    def forward(self, qkv, key_padding_mask, causal, cu_seqlens, max_s, need_weights)
def _flash_attn(self, x)
def forward(self, x)
def replace_vit_attn_with_flash_attn()
class ClsToken(Module)
    def __init__(self, ndim, num_tokens, enabled, register_multiple, num_registers)
    def disable(self)
    def forward(self, x)
    def no_weight_decay(self)
class ViTPatchGenerator(Module)
    def __init__(self, patch_size, embed_dim, input_dims, abs_pos, normalize_patches, cls_token, max_input_dims, pos_dropout, return_pos_enc, num_cls_tokens, register_multiple, num_registers, patch_bias, device, dtype)
    def forward(self, x)
    def apply_cls_token(self)
    def num_cls_tokens(self)
    def num_registers(self)
    def num_skip(self)
    def no_weight_decay(self)
    def _load_projection(self, src_proj_weight, targ_proj_weight)
    def embed_patches(self, x)
    def apply_pos_enc(self, patches, patch_idxs, input_size)
    def get_pos_enc(self, batch_size, patch_idxs, input_size)
    def _get_pos_embeddings(self, batch_size, input_dims)
class Im2Patches(Module)
    def __init__(self, patch_size)
    def forward(self, x)
class ViTPatchLinear(Linear)
    def __init__(self, patch_size, embed_dim, bias)
def _forward_cpe(self, x)
def _take_indices(num_blocks, n)
def _enable_cpe_for_timm_vit(model, max_img_size, num_cls_tokens, pos_dropout, register_multiple, num_registers)
def enable_cpe(model)
class Dinov2LayerScale(Module)
    def __init__(self, dim, init_values, inplace)
    def forward(self, x)
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)
def _create_vision_transformer()
def _patch_layer_scale(model)
def vit_huge_patch16_224(pretrained)
class RADIOModelBase(Module)
    def __init__(self, model, patch_size, max_resolution)
    def num_cls_tokens(self)
    def patch_size(self)
    def max_resolution(self)
    def blocks(self)
    def embed_dim(self)
    def forward(self, x, feature_fmt)
def create_model_from_args(args)
class RADIOConfig(PretrainedConfig)
    """Pretrained Hugging Face configuration for RADIO models."""
    def __init__(self, args, version, patch_size, max_resolution, model_type, hidden_size)
    def to_dict(self)
class RADIOModel(PreTrainedModel)
    """Pretrained Hugging Face model for RADIO.

This class inherits from PreTrainedModel, which provides
HuggingFace's functionality for loading and saving models."""
    def __init__(self, config)
    def model(self)
    def num_summary_tokens(self)
    def patch_size(self)
    def forward(self, pixel_values, output_hidden_states, return_dict)
```

### policy/GR00T_n15/src/gr00t/model/backbone/eagle_backbone.py

```
class EagleBackbone(Module)
    def __init__(self, tune_llm, tune_visual, select_layer, reproject_vision, use_flash_attention, load_bf16, eagle_path, project_to_dim)
    def set_trainable_parameters(self, tune_llm, tune_visual)
    def set_frozen_modules_to_eval_mode(self)
    def prepare_input(self, batch)
    def forward_eagle(self, vl_input)
    def forward(self, vl_input)
```

### policy/GR00T_n15/src/gr00t/model/gr00t_n1.py

```
class GR00T_N1_5_Config(PretrainedConfig)
    def __init__(self)
class GR00T_N1_5(PreTrainedModel)
    def __init__(self, config, local_model_path)
    def validate_inputs(self, inputs)
    def validate_data(self, action_head_outputs, backbone_outputs, is_training)
    def forward(self, inputs)
    def get_action(self, inputs)
    def prepare_input(self, inputs)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### policy/GR00T_n15/src/gr00t/model/policy.py

```
class BasePolicy(ABC)
    def get_action(self, observations)
    def get_modality_config(self)
class Gr00tPolicy(BasePolicy)
    """A wrapper for Gr00t model checkpoints that handles loading the model, applying transforms,
making predictions, and unapplying transforms. This loads some custom configs, stats
and metadata related to the model checkpoints used
in the Gr00t model."""
    def __init__(self, model_path, embodiment_tag, modality_config, modality_transform, denoising_steps, device)
    def apply_transforms(self, obs)
    def unapply_transforms(self, action)
    def get_action(self, observations)
    def _get_action_from_normalized_input(self, normalized_input)
    def _get_unnormalized_action(self, normalized_action)
    def get_modality_config(self)
    def modality_config(self)
    def modality_transform(self)
    def video_delta_indices(self)
    def state_delta_indices(self)
    def denoising_steps(self)
    def denoising_steps(self, value)
    def _check_state_is_batched(self, obs)
    def _load_model(self, model_path)
    def _get_expected_action_dim(self)
    def _load_metadata(self, exp_cfg_dir)
    def _load_horizons(self)
    def _assert_delta_indices(self, delta_indices)
def unsqueeze_dict_values(data)
def squeeze_dict_values(data)
```

### policy/GR00T_n15/src/gr00t/model/transforms.py

```
def formalize_language(language)
def build_eagle_processor(eagle_path)
def collate(features, eagle_processor)
class DefaultDataCollator(DataCollatorMixin)
    def __init__(self, eagle_path)
    def __call__(self, features)
class GR00TTransform(InvertibleModalityTransform)
    def set_metadata(self, dataset_metadata)
    def get_embodiment_tag(self)
    def check_keys_and_batch_size(self, data)
    def _apply_vlm_processing(self, batch)
    def _prepare_video(self, data)
    def _prepare_language(self, data)
    def _prepare_state(self, data)
    def _prepare_action(self, data)
    def apply_single(self, data)
    def apply_batch(self, data, batch_size)
    def apply(self, data)
    def unapply(self, data)
    def __call__(self, data)
```

### policy/GR00T_n15/src/gr00t/utils/eval.py

```
def download_from_hg(repo_id, repo_type)
def calc_mse_for_single_trajectory(policy, dataset, traj_id, modality_keys, steps, action_horizon, plot, plot_state, save_plot_path)
def plot_trajectory(info, save_plot_path)
```

### policy/GR00T_n15/src/gr00t/utils/experiment.py

```
def safe_save_model_for_hf_trainer(trainer, output_dir)
class CheckpointFormatCallback(TrainerCallback)
    """This callback format checkpoint to make them standalone. For now, it copies all config
files to /checkpoint-{step}/experiment_cfg/:
- conf.yaml
- initial_actions.npz
- metadata.json"""
    def __init__(self, run_name, exp_cfg_dir)
    def on_save(self, args, state, control)
```

### policy/GR00T_n15/src/gr00t/utils/misc.py

```
"""Functions that work on nested structures of torch.Tensor or numpy array"""
def any_describe_str(x, shape_only)
def any_describe(x, msg)
```

### policy/GR00T_n15/src/gr00t/utils/peft.py

```
def copy_partial_action_expert_weights(old_dict, new_dict, old_dim, new_dim)
def _wrap_forward(model)
def get_lora_model(model, rank, lora_alpha, lora_dropout, action_head_only)
```

### policy/GR00T_n15/src/gr00t/utils/video.py

```
def get_frames_by_indices(video_path, indices, video_backend, video_backend_kwargs)
def get_frames_by_timestamps(video_path, timestamps, video_backend, video_backend_kwargs)
def get_all_frames(video_path, video_backend, video_backend_kwargs, resize_size)
```

### policy/GR00T_n15_Tactile/__init__.py

```
"""Dex2bench integration for vendored Isaac-GR00T N1.5."""
```

### policy/GR00T_n15_Tactile/convert_dex2bench_to_gr00t.py

```
"""Convert dex2bench raw HDF5 replay episodes to GR00T LeRobot format."""
class EpisodePayload()
def _decode_hdf5_string(value)
def _task_from_episode(ep, fallback, prompt)
def _fps_from_episode(ep)
def _valid_indices(ep)
def _find_homing_cutoff(ep, ep_len_full, valid_indices)
def _decode_rgb_frame(frame)
def _read_camera(ep, camera_id, indices)
def _read_episode(path, camera_map)
def _stats(values)
def _write_jsonl(path, rows)
def _write_video(path, frames, fps)
def _feature_for_video(frames, fps)
def convert_dataset(input_dir, output_dir)
def _default_output_dir(repo_id)
def _parse_camera_map(items, use_default)
def main()
```

### policy/GR00T_n15_Tactile/deploy_policy.py

```
"""Dex2bench deployment adapter for the vendored Isaac-GR00T N1.5 policy."""
def _split_csv_env(value)
def _normalize_camera_mode(value)
def _video_keys_from_env()
def _as_uint8_rgb(image)
def _read_camera(observation)
def _maybe_select_active(qpos)
def _read_qpos(observation)
def _optional_int(value, name)
def _validate_local_checkpoint(model_path)
def encode_obs(observation)
class Dex2BenchGR00TPolicy()
    def __init__(self, usr_args)
    def _to_numpy_action(value)
    def get_action(self, obs)
def get_model(usr_args)
def reset_model(model)
def create_remote_session(usr_args)
```

### policy/GR00T_n15_Tactile/gr00t_dex2bench_config.py

```
"""GR00T data config for dex2bench joint-position policies."""
def _split_csv_env(value)
def _camera_mode()
def _video_keys()
class Dex2BenchGR00TDataConfig(BaseDataConfig)
    """Configurable RGB camera set plus a single qpos state/action vector."""
    def modality_config(self)
    def transform(self)
class TactileGR00TTransform(GR00TTransform)
    """Preserve normalized TacMap tensors alongside standard GR00T features."""
    def apply_single(self, data)
```

### policy/GR00T_n15_Tactile/gr00t_hdf5_dataset.py

```
"""PyTorch Dataset that reads dex2bench HDF5 episodes directly, bypassing LeRobot conversion.

Produces the same raw-data dict format as ``LeRobotSingleDataset.get_step_data``,
so the existing GR00T transform pipeline (VideoToTensor, StateActionTransform, etc.)
applies unchanged.

Usage::

    from gr00t_hdf5_dataset import Dex2BenchHDF5Dataset

    ds = Dex2BenchHDF5Dataset(
        input_dir="/path/to/replay-generalization",
        camera_map={"stereo_left": "cam_stereo_left", ...},
        modality_configs=modality_configs,
        transforms=transforms,
        embodiment_tag="new_embodiment"""
def _decode_hdf5_string(value)
def _decode_rgb_frame(frame)
def _valid_indices(ep)
def _find_homing_cutoff(ep, ep_len_full, valid_indices)
class Dex2BenchHDF5Dataset(Dataset)
    """Read dex2bench HDF5 episodes and apply GR00T transforms directly.

Parameters
----------
input_dir : Path or str
    Directory containing ``episode_*.hdf5`` files.
camera_map : dict[str, str]
    Mapping from GR00T video sub-keys (e.g. ``"stereo_left"``) to HDF5
    camera IDs (e.g. ``"cam_stereo_le"""
    def __init__(self, input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, active_dof_info, state_dim, action_dim, seed, truncate_at_homing, tactile_height, tactile_width)
    def metadata(self)
    def tag(self)
    def modality_configs(self)
    def transforms(self)
    def dataset_name(self)
    def tactile_schema(self)
    def tactile_site_names(self)
    def tactile_output_shape(self)
    def trajectory_ids(self)
    def trajectory_lengths(self)
    def all_steps(self)
    def max_delta(self)
    def set_epoch(self, epoch)
    def _compute_statistics(self)
    def _build_metadata(self, stats)
    def _get_episode(self, ep_idx)
    def get_step_data(self, ep_idx, local_valid_idx)
    def __len__(self)
    def __getitem__(self, idx)
    def __del__(self)
def build_hdf5_dataset(input_dir, camera_map, modality_configs, transforms, embodiment_tag, prompt, use_active_dof, robot_key, state_dim, action_dim, truncate_at_homing, tactile_height, tactile_width)
```

### policy/GR00T_n15_Tactile/run_policy.py

```
"""Run a trained tactile GR00T N1.5 policy in Isaac Sim for evaluation.

This standalone runner mirrors ``run_policy.py`` while adding real-time TacMap
capture. It consumes four RGB cameras plus checkpoint-defined tactile sites and
does not modify the standard GR00T/ACT/DP evaluation paths.

Usage (manus env):
    cd .
    python tactile_run_policy.py         --task scenes/06_fruit_bowl_loading.yaml         --ckpt-dir outputs/logs/tactile/task06-sharpa         --enable-rgb

    # headless mode:
    python tactile_run_policy.py         --task scenes/06_fruit_bowl_loading.yaml         --ckpt-dir ou"""
def _normalize_generalization_profile(profile)
def _mapping(raw)
def _normalize_generalization_split(split)
def _apply_generalization_split(raw)
def _apply_generalization_profile(raw)
def _seed_everything(seed)
def _episode_seed(base_seed, episode_idx)
def _robustness_category(sample)
def _validate_camera_config(camera_cfgs, policy)
def _format_mib(num_bytes)
def _resolve_robot_key_from_ckpt_dir(ckpt_dir)
def _process_rss_bytes()
def _log_memory(label, device)
def _compact_episode_result(result)
def _require_tactile_gpu(device)
def _load_tactile_policy(args)
def _load_act_policy(args)
def _load_dp_policy(args)
def _load_remote_policy(args)
def _load_policy(args)
def _preprocess_image(rgb_hwc)
def _policy_qpos(robot_art, robot_state)
def _joint_command_context(robot_art, raw_action, full_target)
def _build_policy_obs(frames, robot_art, policy_type)
def _validate_tactile_rig(policy, tactile_rig)
def _close_sensor_rigs(camera_rig, tactile_rig)
class _EpisodeSensorOwner()
    """Own both sensor rigs so one outer finally covers their full lifetime."""
    def __init__(self)
    def close(self)
def _build_tactile_policy_obs(frames, tactile_capture, robot_art, policy)
def _camera_frame_issue(frame)
def _capture_complete_camera_set(camera_rig, sim, physics_dt)
def _render_camera_sample(sim, camera_rig)
def _step_sim_with_mounted_camera_sync(sim, camera_rig, interactive_objects, physics_dt)
def _split_legacy_joint_action(qpos)
def _build_remote_policy_obs(frames, robot_art)
def _refresh_observation_joint_state(obs, robot_art)
def _load_success_checker(task)
def _get_object_states(interactive_objects, object_ids)
def _metrics_spec_for_episode(metrics_spec, runtime)
def _reset_policy(policy)
def _start_stdin_skip_listener()
def _log_tactile_attention(path, episode_idx, policy_step, weights)
def _log_modality_attention(path, episode_idx, policy_step, proportions)
def _run_episode_impl(sim, runtime, camera_cfgs, camera_generalization_sample, policy, physics_dt, args, episode_idx, episode_seed, base_seed, scene_generalization_sample, seed_policy, check_success_fn, metrics_spec, perturbation_axis, robot_key, task_instruction, _sensor_owner)
def _run_episode()
def main()

```python
def _refresh_observation_joint_state(
    obs: dict,
    robot_art,
    *,
    robot_state: dict | None = None,
) -> dict:
    qpos = _policy_qpos(robot_art, robot_state)
    refreshed = dict(obs)
    if "agent_pos" in refreshed:
        refreshed["qpos"] = qpos
        refreshed["agent_pos"] = qpos
        return refreshed

    refreshed["joint_action"] = _split_legacy_joint_action(qpos)
    return refreshed
```
```

### policy/GR00T_n15_Tactile/scripts/eval_policy.py

```
class ArgsConfig()
    """Configuration for evaluating a policy."""
def main(args)
```

### policy/GR00T_n15_Tactile/scripts/gr00t_finetune.py

```
class ArgsConfig()
    """Configuration for GR00T model fine-tuning."""
def _parse_hdf5_camera_map(items)
class MilestoneSaveCallback(TrainerCallback)
    """Copy the checkpoint to a ``checkpoint-milestone-{step}`` directory when
*step* is a multiple of *milestone_steps*.  HF's ``_rotate_checkpoints``
only touches ``checkpoint-<digits>``, so these milestone copies are safe
from deletion regardless of ``save_total_limit``."""
    def __init__(self, milestone_steps)
    def on_save(self, args, state, control)
def main(config)
```

### policy/GR00T_n15_Tactile/scripts/load_dataset.py

```
"""This script is a replication of the notebook `getting_started/load_dataset.ipynb`"""
def print_yellow(text)
class ArgsConfig()
    """Configuration for loading the dataset."""
def get_modality_keys(dataset_path)
def plot_state_action_space(state_dict, action_dict, shared_keys)
def plot_image(image)
def load_dataset(dataset_path, embodiment_tag, video_backend, steps, plot_state_action)
```

### policy/GR00T_n15_Tactile/scripts/merge_lora.py

```
"""Merge LoRA adapter into base model and resize action head to match data dim.

Usage:
    python policy/GR00T_n15_Tactile/scripts/merge_lora.py         --base-model ../groot/groot_baseline_ckpt         --checkpoint ../groot/06_lora/checkpoint-10000         --output ../groot/06_lora/merged         --action-dim 36"""
def copy_partial_action_expert_weights(old_dict, new_dict, old_dim, new_dim)
def main()
```

### policy/GR00T_n15_Tactile/src/gr00t/eval/http_server.py

```
"""GR00T HTTP Server Module

This module provides HTTP server functionality for GR00T model inference.
It exposes a REST API for easy integration with web applications and other services.

Dependencies:
    => Server: `pip install uvicorn fastapi json-numpy`
    => Client: `pip install requests json-numpy`"""
class HTTPInferenceServer()
    def __init__(self, policy, port, host, api_token)
    def predict_action(self, payload)
    def health_check(self)
    def run(self)
def create_http_server(policy, port, host, api_token)
```

### policy/GR00T_n15_Tactile/src/gr00t/eval/robot.py

```
class RobotInferenceServer(BaseInferenceServer)
    """Server with three endpoints for real robot policies"""
    def __init__(self, model, host, port, api_token)
    def start_server(policy, port, api_token)
class RobotInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for communicating with the RealRobotServer"""
    def __init__(self, host, port, api_token)
    def get_action(self, observations)
    def get_modality_config(self)
```

### policy/GR00T_n15_Tactile/src/gr00t/eval/service.py

```
class MsgSerializer()
    def to_bytes(data)
    def from_bytes(data)
    def decode_custom_classes(obj)
    def encode_custom_classes(obj)
class EndpointHandler()
class BaseInferenceServer()
    """An inference server that spin up a ZeroMQ socket and listen for incoming requests.
Can add custom endpoints by calling `register_endpoint`."""
    def __init__(self, host, port, api_token)
    def _kill_server(self)
    def _handle_ping(self)
    def register_endpoint(self, name, handler, requires_input)
    def _validate_token(self, request)
    def run(self)
class BaseInferenceClient()
    def __init__(self, host, port, timeout_ms, api_token)
    def _init_socket(self)
    def ping(self)
    def kill_server(self)
    def call_endpoint(self, endpoint, data, requires_input)
    def __del__(self)
class ExternalRobotInferenceClient(BaseInferenceClient)
    """Client for communicating with the RealRobotServer"""
    def get_action(self, observations)
```

### policy/GR00T_n15_Tactile/src/gr00t/eval/simulation.py

```
class VideoConfig()
    """Configuration for video recording settings."""
class MultiStepConfig()
    """Configuration for multi-step environment settings."""
class SimulationConfig()
    """Main configuration for simulation environment."""
class SimulationInferenceClient(BaseInferenceClient, BasePolicy)
    """Client for running simulations and communicating with the inference server."""
    def __init__(self, host, port)
    def get_action(self, observations)
    def get_modality_config(self)
    def setup_environment(self, config)
    def run_simulation(self, config)
    def _get_actions_from_server(self, observations)
def _create_single_env(config, idx)
def run_evaluation(env_name, host, port, video_dir, n_episodes, n_envs, n_action_steps, max_episode_steps)
```

### policy/GR00T_n15_Tactile/src/gr00t/eval/wrappers/multistep_wrapper.py

```
def stack_repeated(x, n, loc)
def repeated_box(box_space, n, loc)
def repeated_space(space, n, loc)
def take_last_n(x, n)
def dict_take_last_n(x, n)
def aggregate(data, method)
class MultiStepWrapper(Wrapper)
    def __init__(self, env, video_delta_indices, state_delta_indices, n_action_steps, max_episode_steps, reward_agg_method)
    def convert_observation_space(self, observation_space, video_horizon, state_horizon)
    def get_max_steps_needed(self)
    def assert_delta_indices(self, delta_indices, horizon)
    def reset(self, seed, options)
    def step(self, action)
    def _get_obs(self, video_delta_indices, state_delta_indices)
    def _add_info(self, info)
    def get_rewards(self)
    def get_attr(self, name)
    def get_infos(self)

```python
def convert_observation_space(self, observation_space, video_horizon, state_horizon):
        """
        For video, the observation space will be (video_horizon,) + original shape
        For state (if not None), the observation space will be (state_horizon,) + original shape
        """
        new_observation_space = {}
        for k in observation_space.keys():
            if k.startswith("video"):
                box = observation_space[k]
                horizon = video_horizon
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("state"):
                box = observation_space[k]
                if state_horizon is not None:
                    horizon = state_horizon
                else:
                    # Don't include the state in the observation space
                    continue
                new_observation_space[k] = repeated_space(box, horizon)
            elif k.startswith("annotation"):
                text = observation_space[k]
                new_observation_space[k] = text
            else:
                raise ValueError(f"Unknown key: {k}")  # NOTE: We might add "language" in the future

        return spaces.Dict(new_observation_space)
```

```python
def _get_obs(self, video_delta_indices, state_delta_indices):
        """
        Output:
        For video: (video_horizon,) + obs_shape
        For state (if not None): (state_horizon,) + obs_shape
        """
        assert len(self.obs) > 0
        if isinstance(self.observation_space, spaces.Dict):
            result = dict()
            for key in self.observation_space.keys():
                if key.startswith("video"):
                    """
                    NOTE:
                      We need to subtract 1 because video_delta_indices is 0-indexed.
                      E.g., video_delta_indices = np.array([-4, -3, -2, -1, 0])
                      Then when we select the observation,
                        it should be [obs[-5], obs[-4], obs[-3], obs[-2], obs[-1]]
                      (i.e., the latest observation is at the last index)
                    """
                    delta_indices = video_delta_indices - 1
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("state"):
                    if state_delta_indices is not None:
                        delta_indices = state_delta_indices - 1
                    else:
                        raise ValueError(
                            f"state_delta_indices is None but `state` is still in the {self.observation_space=}"
                        )
                    this_obs = [self.obs[i][key] for i in delta_indices]
                    result[key] = np.stack(this_obs, axis=0)
                elif key.startswith("annotation"):
                    result[key] = self.obs[-1][key]
                else:
                    raise ValueError(f"Unknown key: {key}")
            return result
        else:
            raise RuntimeError(f"Unsupported space type: {type(self.observation_space)=}")
```

```python
def get_rewards(self):
        return self.reward
```
```