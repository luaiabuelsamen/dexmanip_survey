# artigrasp_2023

source: https://github.com/zdchan/artigrasp


commit: 92fb30785da8938dc37328987f430eeaff0e9097


## README

# ArtiGrasp: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation

## [Paper](https://arxiv.org/pdf/2309.03891.pdf) | [Project Page](https://eth-ait.github.io/artigrasp/)

<img src="docs/image/teaser.jpg" /> 

### Contents

1. [Info](#info)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Training](#training)
5. [Evaluation](#evaluation)
6. [Troubleshooting](#Troubleshooting)
7. [Citation](#citation)
8. [License](#license)

## Info

This code was tested with Python 3.8 and gcc 9.4.0 on Ubuntu 20.04. The repository comes with all the features of the [RaiSim](https://raisim.com/) physics simulation, as ArtiGrasp is integrated into RaiSim.

The ArtiGrasp related code can be found in the [raisimGymTorch](./raisimGymTorch) subfolder. There are six environments (see [envs](./raisimGymTorch/raisimGymTorch/env/envs/)). [compose_eval](./raisimGymTorch/raisimGymTorch/env/envs/compose_eval) is for the quantitative evaluation of the Dynamic Object Grasping and Articulation task. [fixed_arti_evaluation](./raisimGymTorch/raisimGymTorch/env/envs/fixed_arti_evaluation) is for the quantitative evaluation of grasping and articulation with fixed object base.  [floating_evaluation](./raisimGymTorch/raisimGymTorch/env/envs/floating_evaluation) is for the quantitative evaluation of grasping and articulation with free object base.  [general_two](./raisimGymTorch/raisimGymTorch/env/envs/general_two), [left_fixed](./raisimGymTorch/raisimGymTorch/env/envs/left_fixed) and [multi_obj_arti](./raisimGymTorch/raisimGymTorch/env/envs/multi_obj_arti) are the training environments for two hand cooperation with free object base, left hand policy with fixed object base, right hand policy with fixed object base respectively.

## Installation


For good practice for Python package management, it is recommended to use virtual environments (e.g., `virtualenv` or `conda`) to ensure packages from different projects do not interfere with each other.

For installation, see and follow our documentation of the installation steps under [docs/INSTALLATION.md](./docs/INSTALLATION.md). Note that you need to get a valid, free license for the RaiSim physics simulation and an activation key (run any script and follow the instruction).

## Demo

We provide some pre-trained models to view the output of our method. They are stored in [this folder](./raisimGymTorch/data_all/). 

+ For interactive visualizations, you need to run

  ```Shell
  raisimUnity/linux/raisimUnity.x86_64
  ```

  and check the Auto-connect option.

+ To randomly choose an object and visualize the generated sequences, run

  ```Shell
  python raisimGymTorch/env/envs/general_two/runner_eval.py
  ```

## Training

- For the pre-training phase of the right hand policy with fixed-base objects, run

  ```Shell
  python raisimGymTorch/env/envs/multi_obj_arti/runner.py -re (Load the checkpoint. Otherwise start from scratch)
  ```

- For the pre-training phase of the left hand policy with fixed-base objects, run

  ```Shell
  python raisimGymTorch/env/envs/left_fixed/runner.py -re (Load the checkpoint. Otherwise start from scratch)
  ```

- For the fine-tuning phase of two hand policies with free-base objects for cooperation, run

  ```Shell
  python raisimGymTorch/env/envs/general_two/runner.py -re (Load the checkpoint. Otherwise start from scratch)
  ```

## Evaluation

- For grasping and articulation of free-base objects, run

  ```Shell
  python raisimGymTorch/env/envs/floating_evaluation/runner_eval.py -obj '<obj_name>' -test (otherwise for training set) -grasp (otherwise for articulation)
  ```

- For articulation of fixed-base objects, run

  ```Shell
  python raisimGymTorch/env/envs/fixed_arti_evaluation/runner_eval.py -obj '<obj_name>' -test (otherwise for training set)
  ```

- For Dynamic Object Grasping and Articulation task (except ketchup), run

  ```Shell
  python raisimGymTorch/env/envs/composed_eval/compose_eval.py -obj '<obj_name>' -test (otherwise for training set)
  ```

- For Dynamic Object Grasping and Articulation task (ketchup), run

  ```Shell
  python raisimGymTorch/env/envs/composed_eval/ketchup_eval.py -obj '<obj_name>' -test (otherwise for training set)
  ```

## Troubleshooting
If you have error like 
  ```Shell
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.
  ```
try
  ```Shell
pip install numpy==1.23.1
  ```

If you have error like 
  ```Shell
"dump()" has been removed, use
  yaml = YAML(typ='unsafe', pure=True)
  yaml.dump(...)
  ```
try
  ```Shell
pip install ruamel.yaml==0.17.16
  ```

## Citation

To cite us, please use the following:

```
@inProceedings{zhang2024artigrasp,
  title={{ArtiGrasp}: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation},
  author={Zhang, Hui and Christen, Sammy and Fan, Zicong and Zheng, Luocheng and Hwangbo, Jemin and Song, Jie and Hilliges, Otmar},
  booktitle={International Conference on 3D Vision (3DV)},
  year={2024}
}
```

## License

See the following [license](LICENSE.md).









## File tree (depth 3, assets pruned)

```
.gitignore
CMakeLists.txt
COPYING
DEVELOPERS_ONLY/
  linux_build.sh
  linux_requirements.sh
  mac_build.sh
  windowsInstall.ps1
LICENSE.md
README.md
cmake/
  FindSphinx.cmake
eval_commands
examples/
  CMakeLists.txt
  include/
    benchmarkCommon.hpp
    helper.hpp
  src/
    benchmark/
    maps/
    server/
    xml/
package.xml
raisim/
  linux/
    include/
    lib/
  m1/
    include/
    lib/
  mac/
    include/
    lib/
  win32/
    bin/
    include/
    lib/
    mt_debug/
    mt_release/
raisimGymTorch/
  .gitignore
  CMakeFiles/
    3.26.3/
    CMakeConfigureLog.yaml
    CMakeDirectoryInformation.cmake
    Makefile.cmake
    Makefile2
    TargetDirectories.txt
    cmake.check_cache
    progress.marks
  CMakeLists.txt
  LICENSE
  Makefile
  __init__.py
  cmake_install.cmake
  common/
    .gitignore
    ___init___.py
    abstract_pl.py
    args_utils.py
    body_models.py
    camera.py
    cluster_utils.py
    comet_utils.py
    condor_cluster.py
    data_utils.py
    exp_manager.py
    ld_utils.py
    list_utils.py
    mesh.py
    metrics.py
    np_utils.py
    object_tensors.py
    pl_utils.py
    rend_utils.py
    rot.py
    skeleton_utils.py
    sys_utils.py
    thing.py
    torch_utils.py
    transforms.py
    video_utils.py
    viewer.py
    vis_utils.py
    xdict.py
  data_all/
    general_two/
    left_fixed/
    multi_obj_arti/
  raisimGymTorch/
    __init__.py
    algo/
    env/
    helper/
  scripts/
    run_eval.sh
    run_eval_prim_test_nopose.sh
    run_eval_prim_train_nopose.sh
    run_eval_test.sh
    run_eval_train.sh
    v4_3/
    v5/
    v5_experiments
  setup.py
  thirdParty/
    pybind11/
raisimMatlab/
  .gitignore
  CMakeLists.txt
  LICENSE
  debug_app.cpp
  examples/
    raisimMatlabLaikagoExample.m
  license.txt
  raisim_interface_mex.cpp
  raisim_interface_mex.hpp
raisimPy/
  .gitignore
  CMakeLists.txt
  COPYING
  README.rst
  examples/
    heightMap.py
    newtonsCradle.py
    rayDemo2.py
    robots.py
    springs.py
    visualObjects.py
  include/
    converter.hpp
    utils.hpp
  src/
    articulated_system.cpp
    constraints.cpp
    contact.cpp
    converter.cpp
    materials.cpp
    math.cpp
    object.cpp
    raisim_wrapper.cpp
    single_bodies.cpp
    terrain.cpp
    world.cpp
raisimUnity/
  .gitignore
  README.md
  TRY_OPENGL_VERSION_IF_THIS_DOESNT_WORK
  linux/
    LinuxPlayer_s.debug
    Logs/
    UnityPlayer.so
    UnityPlayer_s.debug
    mono_crash.mem.3265825.1.blob
    mono_crash.mem.87575.1.blob
    raisimUnity.x86_64
    raisimUnity_BurstDebugInformation_DoNotShip/
    raisimUnity_Data/
  m1/
    RaiSimUnity.app/
  m1_assimp_backup/
    libassimp.bundle
  mac/
    RaiSimUnity.app/
  win32/
    Logs/
    MonoBleedingEdge/
    RaiSimUnity.exe
    RaiSimUnity_BurstDebugInformation_DoNotShip/
    RaiSimUnity_Data/
    UnityCrashHandler64.exe
    UnityCrashHandler64.pdb
    UnityPlayer.dll
    UnityPlayer_Win64_mono_x64.pdb
    WindowsPlayerHeadless.pdb
    WindowsPlayer_Master_mono_x64.pdb
    assimp.dll
raisimUnityOpengl/
  linux/
    LinuxPlayer_s.debug
    Logs/
    UnityPlayer.so
    UnityPlayer_s.debug
    raisimUnity.x86_64
    raisimUnity_Data/
rsc/
  arctic/
    box/
    capsulemachine/
    espressomachine/
    ketchup/
    laptop/
    microwave/
    mixer/
    notebook/
    phone/
    waffleiron/
  mano2urdf/
    export_meshes.py
    limit_high_l.txt
    limit_high_r.txt
    limit_low_l.txt
    limit_low_r.txt
    mano2urdf.py
    mano_helpers.py
    rotation_helper.py
    urdf.py
  mano_double/
    contact/
    contact_recon/
    ee/
    ee_recon/
    grasp_label/
    left_pose_mean.txt
    lhand_mano.urdf
    lhand_mano_demo.urdf
    lhand_mano_info.json
    lhand_mano_large.urdf
    rhand_mano.urdf
    rhand_mano_26.urdf
    rhand_mano_demo.urdf
    rhand_mano_info.json
    rhand_mano_large.urdf
    right_pose_mean.txt
    s1/
    s10/
    s2/
    s4/
    s5/
    s5_recon/
    s6/
    s7/
    s8/
    s9/
thirdParty/
  Eigen3/
    LICENSE
    include/
    share/
  pybind11/
    .appveyor.yml
    .clang-format
    .clang-tidy
    .cmake-format.yaml
    .github/
    .gitignore
    .pre-commit-config.yaml
    .readthedocs.yml
    CMakeLists.txt
    LICENSE
    MANIFEST.in
    README.rst
    include/
    noxfile.py
    pybind11/
    pyproject.toml
    setup.cfg
    setup.py
    tests/
    tools/
```

## Config files (30)


### raisim/win32/bin/rsc/laikago/default_cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  num_envs: 100
  num_threads: 40
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0

  forwardVelRewardCoeff: 0.3
  torqueRewardCoeff: -2e-5
```

### raisim/win32/mt_debug/bin/rsc/laikago/default_cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  num_envs: 100
  num_threads: 40
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0

  forwardVelRewardCoeff: 0.3
  torqueRewardCoeff: -2e-5
```

### raisim/win32/mt_release/bin/rsc/laikago/default_cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  num_envs: 100
  num_threads: 40
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0

  forwardVelRewardCoeff: 0.3
  torqueRewardCoeff: -2e-5
```

### raisimGymTorch/data_all/general_two/2023-05-15-10-18-54/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 50
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  root_guided_r: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  stage_dim_x: 0.1
  stage_dim_y: 0.1
  stage_dim_z: 0.1
  stage_pos_x: 0.75
  stage_pos_y: 0.0
  stage_pos_z: 0.551
  reward:
#    pos_reward:  # distance to goal !!!
#      coeff: 2.0
#    pose_reward:  # distance to goal  !!!
#      coeff: 0.1
#    contact_reward:
#      coeff: 1.0
#    impulse_reward:
#      coeff: 1.0
#
#
#    body_vel_reward_:
#      coeff: -0.1
#    body_qvel_reward_:
#      coeff: -0.1
#
#    rel_obj_vel_reward_: # object velocity in wrist frame !!!
#      coeff: -0.1
#
#    obj_angle_reward_:
#      coeff: 1.0
#    obj_avel_reward_:
#      coeff: 0.0
#
#    obj_vel_reward_:    # bottom
#      coeff: -0.3
#    obj_qvel_reward_:
#      coeff: -0.3
#
#    torque:
#      coeff: -0.0
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2

    contact_reward:
      coeff: 1.5
    impulse_reward:
      coeff: 1.5

    obj_angle_reward_:
      coeff: 1.5
    obj_pos_reward_: # distance to initial position !!!
      coeff: 0.2
    rel_obj_vel_reward_: # object velocity in wrist frame
      coeff: -0.5

    torque:
      coeff: -0.0
    body_vel_reward_:
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_avel_reward_: # angular vel of the joint
      coeff: -0.2
    obj_vel_reward_:
      coeff: -0.2
    obj_qvel_reward_:
      coeff: -0.2


#    obj_pos_w_reward:
#      coeff: 0.0
#    obj_pose_w_reward:
#      coeff: 0.0
#    obj_pos_h_reward:
#      coeff: 0.0
#    obj_pose_h_reward:
#      coeff: 0.0

#    # no use

#    obj_pose_reward_:
#      coeff: 0.0
#    rel_obj_pos_reward_:
#      coeff: -0.0

architecture:
  policy_net: [128,128]
  value_net: [128, 128]

  policy_net_trail: [128, 128]
  value_net_trail: [128, 128]
  wrist_dim: 6
```

### raisimGymTorch/data_all/left_fixed/2023-05-08-10-03-19/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 200
  update_every_n: 20
  num_threads: 60
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  reward:
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2
    root_pos_reward_:
      coeff: 0.0
    root_pose_reward_:
      coeff: 0.0
    contact_pos_reward:
      coeff: 0.0
    contact_reward:
      coeff: 2.0
    impulse_reward:
      coeff: 2.0
    obj_reward:
      coeff: 0.0
    obj_pose_reward_:
      coeff: 0.0
    falling_reward:
      coeff: 0.0
    torque:
      coeff: -0.0
    rel_obj_reward_:
      coeff: -0.0
    body_vel_reward_:
#      coeff: -0.2
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_angle_reward_:
      coeff: 0.0
#      coeff: 1.0
    obj_avel_reward_:
      coeff: 0.0
architecture:
  policy_net: [128,128]
  value_net: [128, 128]
```

### raisimGymTorch/data_all/multi_obj_arti/2023-05-14-16-30-13/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 100
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  reward:
    pos_reward:
      coeff: 2.0
    pose_reward:
      coeff: 0.1
    root_pos_reward_:
      coeff: 0.0
    root_pose_reward_:
      coeff: 0.0
    contact_pos_reward:
      coeff: 0.0
    contact_reward:
      coeff: 1.0
    impulse_reward:
      coeff: 2.0
    obj_reward:
      coeff: 0.0
    obj_pose_reward_:
      coeff: 0.0
    falling_reward:
      coeff: 0.0
    torque:
      coeff: -0.0
    rel_obj_reward_:
      coeff: -0.0
    body_vel_reward_:
#      coeff: -0.2
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_angle_reward_:
      coeff: 2.5
#      coeff: 1.0
    obj_avel_reward_:
      coeff: -0.5
architecture:
  policy_net: [128,128]
  value_net: [128, 128]
```

### raisimGymTorch/raisimGymTorch/env/envs/compose_eval/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 100
  update_every_n: 20
  num_threads: 60
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  root_guided_r: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  stage_dim_x: 0.1
  stage_dim_y: 0.1
  stage_dim_z: 0.1
  stage_pos_x: 0.75
  stage_pos_y: 0.0
  stage_pos_z: 0.551
  reward:
    pos_reward:
      coeff: 2.0
    pose_reward:
      coeff: 0.2
    contact_reward:
      coeff: 1.0
    impulse_reward:
      coeff: 1.0

    torque:
      coeff: -0.0
    body_vel_reward_:
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.5
    rel_obj_vel_reward_: # object velocity to wrist frame
      coeff: -1.0

    obj_vel_reward_:
      coeff: -0.3
    obj_qvel_reward_:
      coeff: -0.3
    obj_angle_reward_:
      coeff: 1.0
    obj_avel_reward_: # angular vel of the joint
      coeff: -0.0


architecture:
  policy_net: [128,128]
  value_net: [128, 128]

  policy_net_trail: [128, 128]
  value_net_trail: [128, 128]
  wrist_dim: 6
```

### raisimGymTorch/raisimGymTorch/env/envs/fixed_arti_evaluation/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 100
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  reward:
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2
    root_pos_reward_:
      coeff: 0.0
    root_pose_reward_:
      coeff: 0.0
    contact_pos_reward:
      coeff: 0.0
    contact_reward:
      coeff: 1.5
    impulse_reward:
      coeff: 1.5
    obj_reward:
      coeff: 0.0
    obj_pose_reward_:
      coeff: 0.0
    falling_reward:
      coeff: 0.0
    torque:
      coeff: -0.0
    rel_obj_reward_:
      coeff: -0.0
    body_vel_reward_:
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_angle_reward_:
      coeff: 1.5
    obj_avel_reward_:
      coeff: -0.5
architecture:
  policy_net: [128,128]
  value_net: [128, 128]
```

### raisimGymTorch/raisimGymTorch/env/envs/floating_evaluation/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 50
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  root_guided_r: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  stage_dim_x: 0.1
  stage_dim_y: 0.1
  stage_dim_z: 0.1
  stage_pos_x: 0.75
  stage_pos_y: 0.0
  stage_pos_z: 0.551
  reward:
    pos_reward:
      coeff: 2.0
    pose_reward:
      coeff: 0.1
    contact_reward:
      coeff: 1.0
    impulse_reward:
      coeff: 1.0

    torque:
      coeff: -0.0
    body_vel_reward_:
      coeff: -1.0
    body_qvel_reward_:
      coeff: -1.0
    rel_obj_vel_reward_: # object velocity in wrist frame
      coeff: -1.0

    obj_vel_reward_:
      coeff: -2.0
    obj_qvel_reward_:
      coeff: -2.0
    obj_angle_reward_:
      coeff: 1.0
    obj_avel_reward_: # angular vel of the joint
      coeff: -0.0

    obj_pos_reward_: # distance to initial position
      coeff: 0.2

architecture:
  policy_net: [128,128]
  value_net: [128, 128]

  policy_net_trail: [128, 128]
  value_net_trail: [128, 128]
  wrist_dim: 6
```

### raisimGymTorch/raisimGymTorch/env/envs/general_two/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 50
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  root_guided_r: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  stage_dim_x: 0.1
  stage_dim_y: 0.1
  stage_dim_z: 0.1
  stage_pos_x: 0.75
  stage_pos_y: 0.0
  stage_pos_z: 0.551
  reward:
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2

    contact_reward:
      coeff: 1.5
    impulse_reward:
      coeff: 1.5

    obj_angle_reward_:
      coeff: 1.5
    obj_pos_reward_: # distance to initial position
      coeff: 0.2
    rel_obj_vel_reward_: # object velocity in wrist frame
      coeff: -0.5

    torque:
      coeff: -0.0
    body_vel_reward_:
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_avel_reward_: # angular vel of the joint
      coeff: -0.5
    obj_vel_reward_:
      coeff: -0.5
    obj_qvel_reward_:
      coeff: -0.3

architecture:
  policy_net: [128,128]
  value_net: [128, 128]

  policy_net_trail: [128, 128]
  value_net_trail: [128, 128]
  wrist_dim: 6
```

### raisimGymTorch/raisimGymTorch/env/envs/left_fixed/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 200
  update_every_n: 20
  num_threads: 60
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  reward:
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2
    root_pos_reward_:
      coeff: 0.0
    root_pose_reward_:
      coeff: 0.0
    contact_pos_reward:
      coeff: 0.0
    contact_reward:
      coeff: 2.0
    impulse_reward:
      coeff: 2.0
    obj_reward:
      coeff: 0.0
    obj_pose_reward_:
      coeff: 0.0
    falling_reward:
      coeff: 0.0
    torque:
      coeff: -0.0
    rel_obj_reward_:
      coeff: -0.0
    body_vel_reward_:
#      coeff: -0.2
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_angle_reward_:
      coeff: 0.0
#      coeff: 1.0
    obj_avel_reward_:
      coeff: 0.0
architecture:
  policy_net: [128,128]
  value_net: [128, 128]
```

### raisimGymTorch/raisimGymTorch/env/envs/multi_obj_arti/cfgs/cfg_reg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
  num_envs: 21
  num_repeats: 1
  eval_every_n: 100
  update_every_n: 20
  num_threads: 32
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  root_guided: True
  testing: False
  cylinder_mesh: False
  box_mesh: False
  no_pose_state: False
  nohierarchy: False
  prior: False
  obj: "024_bowl"
  hand_model_r: "rhand_mano.urdf"
  hand_model_l: "lhand_mano.urdf"
  weight: 0.1
  finger_action_std: 0.015
  rot_action_std: 0.01
  reward:
    pos_reward:
      coeff: 3.0
    pose_reward:
      coeff: 0.2
    root_pos_reward_:
      coeff: 0.0
    root_pose_reward_:
      coeff: 0.0
    contact_pos_reward:
      coeff: 0.0
    contact_reward:
      coeff: 1.5
    impulse_reward:
      coeff: 1.5
    obj_reward:
      coeff: 0.0
    obj_pose_reward_:
      coeff: 0.0
    falling_reward:
      coeff: 0.0
    torque:
      coeff: -0.0
    rel_obj_reward_:
      coeff: -0.0
    body_vel_reward_:
      coeff: -0.5
    body_qvel_reward_:
      coeff: -0.2
    obj_angle_reward_:
      coeff: 1.5
    obj_avel_reward_:
      coeff: -0.5
architecture:
  policy_net: [128,128]
  value_net: [128, 128]
```

### raisimGymTorch/thirdParty/pybind11/.appveyor.yml

```yaml
version: 1.0.{build}
image:
- Visual Studio 2015
test: off
skip_branch_with_pr: true
build:
  parallel: true
platform:
- x86
environment:
  matrix:
  - PYTHON: 36
    CONFIG: Debug
  - PYTHON: 27
    CONFIG: Debug
install:
- ps: |
    $env:CMAKE_GENERATOR = "Visual Studio 14 2015"
    if ($env:PLATFORM -eq "x64") { $env:PYTHON = "$env:PYTHON-x64" }
    $env:PATH = "C:\Python$env:PYTHON\;C:\Python$env:PYTHON\Scripts\;$env:PATH"
    python -W ignore -m pip install --upgrade pip wheel
    python -W ignore -m pip install pytest numpy --no-warn-script-location pytest-timeout
- ps: |
    Start-FileDownload 'https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip'
    7z x eigen-3.3.7.zip -y > $null
    $env:CMAKE_INCLUDE_PATH = "eigen-3.3.7;$env:CMAKE_INCLUDE_PATH"
build_script:
- cmake -G "%CMAKE_GENERATOR%" -A "%CMAKE_ARCH%"
    -DCMAKE_CXX_STANDARD=14
    -DPYBIND11_WERROR=ON
    -DDOWNLOAD_CATCH=ON
    -DCMAKE_SUPPRESS_REGENERATION=1
    .
- set MSBuildLogger="C:\Program Files\AppVeyor\BuildAgent\Appveyor.MSBuildLogger.dll"
- cmake --build . --config %CONFIG% --target pytest -- /m /v:m /logger:%MSBuildLogger%
- cmake --build . --config %CONFIG% --target cpptest -- /m /v:m /logger:%MSBuildLogger%
on_failure: if exist "tests\test_cmake_build" type tests\test_cmake_build\*.log*

```

### raisimGymTorch/thirdParty/pybind11/.cmake-format.yaml

```yaml
parse:
  additional_commands:
    pybind11_add_module:
      flags:
        - THIN_LTO
        - MODULE
        - SHARED
        - NO_EXTRAS
        - EXCLUDE_FROM_ALL
        - SYSTEM

format:
  line_width: 99
  tab_size: 2

  # If an argument group contains more than this many sub-groups
  # (parg or kwarg groups) then force it to a vertical layout.
  max_subgroups_hwrap: 2

  # If a positional argument group contains more than this many
  # arguments, then force it to a vertical layout.
  max_pargs_hwrap: 6

  # If a cmdline positional group consumes more than this many
  # lines without nesting, then invalidate the layout (and nest)
  max_rows_cmdline: 2
  separate_ctrl_name_with_space: false
  separate_fn_name_with_space: false
  dangle_parens: false

  # If the trailing parenthesis must be 'dangled' on its on
  # 'line, then align it to this reference: `prefix`: the start'
  # 'of the statement,  `prefix-indent`: the start of the'
  # 'statement, plus one indentation  level, `child`: align to'
  # the column of the arguments
  dangle_align: prefix
  # If the statement spelling length (including space and
  # parenthesis) is smaller than this amount, then force reject
  # nested layouts.
  min_prefix_chars: 4

  # If the statement spelling length (including space and
  # parenthesis) is larger than the tab width by more than this
  # amount, then force reject un-nested layouts.
  max_prefix_chars: 10

  # If a candidate layout is wrapped horizontally but it exceeds
  # this many lines, then reject the layout.
  max_lines_hwrap: 2

  line_ending: unix

  # Format command names consistently as 'lower' or 'upper' case
  command_case: canonical

  # Format keywords consistently as 'lower' or 'upper' case
  # unchanged is valid too
  keyword_case: 'upper'

  # A list of command names which should always be wrapped
  always_wrap: []

  # If true, the argument lists which are known to be sortable
  # will be sorted lexicographically
  enable_sort: true

  # If true, the parsers may infer whether or not an argument
  # list is sortable (without annotation).
  autosort: false

# Causes a few issues - can be solved later, possibly.
markup:
  enable_markup: false

```

### raisimGymTorch/thirdParty/pybind11/.github/ISSUE_TEMPLATE/bug-report.yml

```yaml
name: Bug Report
description: File an issue about a bug
title: "[BUG]: "
labels: [triage]
body:
  - type: markdown
    attributes:
      value: |
        Maintainers will only make a best effort to triage PRs. Please do your best to make the issue as easy to act on as possible, and only open if clearly a problem with pybind11 (ask first if unsure).
  - type: checkboxes
    id: steps
    attributes:
      label: Required prerequisites
      description: Make sure you've completed the following steps before submitting your issue -- thank you!
      options:
        - label: Make sure you've read the [documentation](https://pybind11.readthedocs.io). Your issue may be addressed there.
          required: true
        - label: Search the [issue tracker](https://github.com/pybind/pybind11/issues) and [Discussions](https:/pybind/pybind11/discussions) to verify that this hasn't already been reported. +1 or comment there if it has.
          required: true
        - label: Consider asking first in the [Gitter chat room](https://gitter.im/pybind/Lobby) or in a [Discussion](https:/pybind/pybind11/discussions/new).
          required: false

  - type: textarea
    id: description
    attributes:
      label: Problem description
      placeholder: >-
        Provide a short description, state the expected behavior and what
        actually happens. Include relevant information like what version of
        pybind11 you are using, what system you are on, and any useful commands
        / output.
    validations:
      required: true

  - type: textarea
    id: code
    attributes:
      label: Reproducible example code
      placeholder: >-
        The code should be minimal, have no external dependencies, isolate the
        function(s) that cause breakage. Submit matched and complete C++ and
        Python snippets that can be easily compiled and run to diagnose the
        issue. If possible, make a PR with a new, failing test to give us a
        starting point to work on!
      render: text

```

### raisimGymTorch/thirdParty/pybind11/.github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
  - name: Ask a question
    url: https://github.com/pybind/pybind11/discussions/new
    about: Please ask and answer questions here, or propose new ideas.
  - name: Gitter room
    url: https://gitter.im/pybind/Lobby
    about: A room for discussing pybind11 with an active community

```

### raisimGymTorch/thirdParty/pybind11/.github/dependabot.yml

```yaml
version: 2
updates:
  # Maintain dependencies for GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"
    ignore:
      # Official actions have moving tags like v1
      # that are used, so they don't need updates here
      - dependency-name: "actions/checkout"
      - dependency-name: "actions/setup-python"
      - dependency-name: "actions/cache"
      - dependency-name: "actions/upload-artifact"
      - dependency-name: "actions/download-artifact"
      - dependency-name: "actions/labeler"

```

### raisimGymTorch/thirdParty/pybind11/.github/labeler.yml

```yaml
docs:
- any:
  - 'docs/**/*.rst'
  - '!docs/changelog.rst'
  - '!docs/upgrade.rst'

ci:
- '.github/workflows/*.yml'

```

### raisimGymTorch/thirdParty/pybind11/.github/labeler_merged.yml

```yaml
needs changelog:
- all:
  - '!docs/changelog.rst'

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/ci.yml

```yaml
name: CI

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - master
      - stable
      - v*

concurrency:
  group: test-${{ github.ref }}
  cancel-in-progress: true

env:
  PIP_ONLY_BINARY: numpy

jobs:
  # This is the "main" test suite, which tests a large number of different
  # versions of default compilers and Python versions in GitHub Actions.
  standard:
    strategy:
      fail-fast: false
      matrix:
        runs-on: [ubuntu-latest, windows-2022, macos-latest]
        python:
        - '2.7'
        - '3.5'
        - '3.6'
        - '3.9'
        - '3.10'
        - 'pypy-3.7-v7.3.7'
        - 'pypy-3.8-v7.3.7'

        # Items in here will either be added to the build matrix (if not
        # present), or add new keys to an existing matrix element if all the
        # existing keys match.
        #
        # We support an optional key: args, for cmake args
        include:
          # Just add a key
          - runs-on: ubuntu-latest
            python: '3.6'
            args: >
              -DPYBIND11_FINDPYTHON=ON
              -DCMAKE_CXX_FLAGS="-D_=1"
          - runs-on: windows-latest
            python: '3.6'
            args: >
              -DPYBIND11_FINDPYTHON=ON
          - runs-on: macos-latest
            python: 'pypy-2.7'
          # Inject a couple Windows 2019 runs
          - runs-on: windows-2019
            python: '3.9'
          - runs-on: windows-2019
            python: '2.7'

    name: "🐍 ${{ matrix.python }} • ${{ matrix.runs-on }} • x64 ${{ matrix.args }}"
    runs-on: ${{ matrix.runs-on }}

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python ${{ matrix.python }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python }}

    - name: Setup Boost (Linux)
      # Can't use boost + define _
      if: runner.os == 'Linux' && matrix.python != '3.6'
      run: sudo apt-get install libboost-dev

    - name: Setup Boost (macOS)
      if: runner.os == 'macOS'
      run: brew install boost

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Cache wheels
      if: runner.os == 'macOS'
      uses: actions/cache@v2
      with:
        # This path is specific to macOS - we really only need it for PyPy NumPy wheels
        # See https://github.com/actions/cache/blob/master/examples.md#python---pip
        # for ways to do this more generally
        path: ~/Library/Caches/pip
        # Look to see if there is a cache hit for the corresponding requirements file
        key: ${{ runner.os }}-pip-${{ matrix.python }}-x64-${{ hashFiles('tests/requirements.txt') }}

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Setup annotations on Linux
      if: runner.os == 'Linux'
      run: python -m pip install pytest-github-actions-annotate-failures

    # First build - C++11 mode and inplace
    - name: Configure C++11 ${{ matrix.args }}
      run: >
        cmake -S . -B .
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=11
        ${{ matrix.args }}

    - name: Build C++11
      run: cmake --build . -j 2

    - name: Python tests C++11
      run: cmake --build . --target pytest -j 2

    - name: C++11 tests
      # TODO: Figure out how to load the DLL on Python 3.8+
      if: "!(runner.os == 'Windows' && (matrix.python == 3.8 || matrix.python == 3.9 || matrix.python == '3.10' || matrix.python == '3.11-dev' || matrix.python == 'pypy-3.8'))"
      run: cmake --build .  --target cpptest -j 2

    - name: Interface test C++11
      run: cmake --build . --target test_cmake_build

    - name: Clean directory
      run: git clean -fdx

    # Second build - C++17 mode and in a build directory
    - name: Configure C++17
      run: >
        cmake -S . -B build2
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        ${{ matrix.args }}

    - name: Build
      run: cmake --build build2 -j 2

    - name: Python tests
      run: cmake --build build2 --target pytest

    - name: C++ tests
      # TODO: Figure out how to load the DLL on Python 3.8+
      if: "!(runner.os == 'Windows' && (matrix.python == 3.8 || matrix.python == 3.9 || matrix.python == '3.10' || matrix.python == '3.11-dev' || matrix.python == 'pypy-3.8'))"
      run: cmake --build build2 --target cpptest

    # Third build - C++17 mode with unstable ABI
    - name: Configure (unstable ABI)
      run: >
        cmake -S . -B build3
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        -DPYBIND11_INTERNALS_VERSION=10000000
        "-DPYBIND11_TEST_OVERRIDE=test_call_policies.cpp;test_gil_scoped.cpp;test_thread.cpp"
        ${{ matrix.args }}

    - name: Build (unstable ABI)
      run: cmake --build build3 -j 2

    - name: Python tests (unstable ABI)
      run: cmake --build build3 --target pytest

    - name: Interface test
      run: cmake --build build2 --target test_cmake_build

    # Eventually Microsoft might have an action for setting up
    # MSVC, but for now, this action works:
    - name: Prepare compiler environment for Windows 🐍 2.7
      if: matrix.python == 2.7 && runner.os == 'Windows'
      uses: ilammy/msvc-dev-cmd@v1.10.0
      with:
        arch: x64

    # This makes two environment variables available in the following step(s)
    - name: Set Windows 🐍 2.7 environment variables
      if: matrix.python == 2.7 && runner.os == 'Windows'
      shell: bash
      run: |
        echo "DISTUTILS_USE_SDK=1" >> $GITHUB_ENV
        echo "MSSdk=1" >> $GITHUB_ENV

    # This makes sure the setup_helpers module can build packages using
    # setuptools
    - name: Setuptools helpers test
      run: pytest tests/extra_setuptools
      if: "!(matrix.python == '3.5' && matrix.runs-on == 'windows-2022')"


  deadsnakes:
    strategy:
      fail-fast: false
      matrix:
        include:
        # TODO: Fails on 3.10, investigate
        - python-version: "3.9"
          python-debug: true
          valgrind: true
      # - python-version: "3.11-dev"
      #   python-debug: false

    name: "🐍 ${{ matrix.python-version }}${{ matrix.python-debug && '-dbg' || '' }} (deadsnakes)${{ matrix.valgrind && ' • Valgrind' || '' }} • x64"
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python ${{ matrix.python-version }} (deadsnakes)
      uses: deadsnakes/action@v2.1.1
      with:
        python-version: ${{ matrix.python-version }}
        debug: ${{ matrix.python-debug }}

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Valgrind cache
      if: matrix.valgrind
      uses: actions/cache@v2
      id: cache-valgrind
      with:
        path: valgrind
        key: 3.16.1 # Valgrind version

    - name: Compile Valgrind
      if: matrix.valgrind && steps.cache-valgrind.outputs.cache-hit != 'true'
      run: |
        VALGRIND_VERSION=3.16.1
        curl https://sourceware.org/pub/valgrind/valgrind-$VALGRIND_VERSION.tar.bz2 -o - | tar xj
        mv valgrind-$VALGRIND_VERSION valgrind
        cd valgrind
        ./configure
        make -j 2 > /dev/null

    - name: Install Valgrind
      if: matrix.valgrind
      working-directory: valgrind
      run: |
        sudo make install
        sudo apt-get update
        sudo apt-get install libc6-dbg  # Needed by Valgrind

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Configure
      env:
        SETUPTOOLS_USE_DISTUTILS: stdlib
      run: >
        cmake -S . -B build
        -DCMAKE_BUILD_TYPE=Debug
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17

    - name: Build
      run: cmake --build build -j 2

    - name: Python tests
      run: cmake --build build --target pytest

    - na
```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/configure.yml

```yaml
name: Config

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - master
      - stable
      - v*

jobs:
  # This tests various versions of CMake in various combinations, to make sure
  # the configure step passes.
  cmake:
    strategy:
      fail-fast: false
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
        arch: [x64]
        cmake: ["3.21"]

        include:
        - runs-on: ubuntu-latest
          arch: x64
          cmake: 3.4

        - runs-on: macos-latest
          arch: x64
          cmake: 3.7

        - runs-on: windows-2016
          arch: x86
          cmake: 3.8

        - runs-on: windows-2016
          arch: x86
          cmake: 3.18

    name: 🐍 3.7 • CMake ${{ matrix.cmake }} • ${{ matrix.runs-on }}
    runs-on: ${{ matrix.runs-on }}

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: 3.7
        architecture: ${{ matrix.arch }}

    - name: Prepare env
      run: python -m pip install -r tests/requirements.txt

    # An action for adding a specific version of CMake:
    #   https://github.com/jwlawson/actions-setup-cmake
    - name: Setup CMake ${{ matrix.cmake }}
      uses: jwlawson/actions-setup-cmake@v1.11
      with:
        cmake-version: ${{ matrix.cmake }}

    # These steps use a directory with a space in it intentionally
    - name: Make build directories
      run: mkdir "build dir"

    - name: Configure
      working-directory: build dir
      shell: bash
      run: >
        cmake ..
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DPYTHON_EXECUTABLE=$(python -c "import sys; print(sys.executable)")

    # Only build and test if this was manually triggered in the GitHub UI
    - name: Build
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release

    - name: Test
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release --target check

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/format.yml

```yaml
# This is a format job. Pre-commit has a first-party GitHub action, so we use
# that: https://github.com/pre-commit/action

name: Format

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - master
    - stable
    - "v*"

jobs:
  pre-commit:
    name: Format
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
    - uses: pre-commit/action@v2.0.3
      with:
        # Slow hooks are marked with manual - slow is okay here, run them too
        extra_args: --hook-stage manual --all-files

  clang-tidy:
    # When making changes here, please also review the "Clang-Tidy" section
    # in .github/CONTRIBUTING.md and update as needed.
    name: Clang-Tidy
    runs-on: ubuntu-latest
    container: silkeh/clang:12
    steps:
    - uses: actions/checkout@v2

    - name: Install requirements
      run: apt-get update && apt-get install -y python3-dev python3-pytest

    - name: Configure
      run: >
        cmake -S . -B build
        -DCMAKE_CXX_CLANG_TIDY="$(which clang-tidy)"
        -DDOWNLOAD_EIGEN=ON
        -DDOWNLOAD_CATCH=ON
        -DCMAKE_CXX_STANDARD=17

    - name: Build
      run: cmake --build build -j 2 -- --keep-going

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/labeler.yml

```yaml
name: Labeler
on:
  pull_request_target:
    types: [closed]

jobs:
  label:
    name: Labeler
    runs-on: ubuntu-latest
    steps:

    - uses: actions/labeler@main
      if: github.event.pull_request.merged == true
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        configuration-path: .github/labeler_merged.yml

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/pip.yml

```yaml
name: Pip

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - master
    - stable
    - v*
  release:
    types:
    - published

env:
  PIP_ONLY_BINARY: numpy

jobs:
  # This builds the sdists and wheels and makes sure the files are exactly as
  # expected. Using Windows and Python 2.7, since that is often the most
  # challenging matrix element.
  test-packaging:
    name: 🐍 2.7 • 📦 tests • windows-latest
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup 🐍 2.7
      uses: actions/setup-python@v2
      with:
        python-version: 2.7

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Python Packaging tests
      run: pytest tests/extra_python_package/


  # This runs the packaging tests and also builds and saves the packages as
  # artifacts.
  packaging:
    name: 🐍 3.8 • 📦 & 📦 tests • ubuntu-latest
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup 🐍 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt build twine

    - name: Python Packaging tests
      run: pytest tests/extra_python_package/

    - name: Build SDist and wheels
      run: |
        python -m build
        PYBIND11_GLOBAL_SDIST=1 python -m build

    - name: Check metadata
      run: twine check dist/*

    - name: Save standard package
      uses: actions/upload-artifact@v2
      with:
        name: standard
        path: dist/pybind11-*

    - name: Save global package
      uses: actions/upload-artifact@v2
      with:
        name: global
        path: dist/pybind11_global-*



  # When a GitHub release is made, upload the artifacts to PyPI
  upload:
    name: Upload to PyPI
    runs-on: ubuntu-latest
    if: github.event_name == 'release' && github.event.action == 'published'
    needs: [packaging]

    steps:
    - uses: actions/setup-python@v2

    # Downloads all to directories matching the artifact names
    - uses: actions/download-artifact@v2

    - name: Publish standard package
      uses: pypa/gh-action-pypi-publish@v1.5.0
      with:
        password: ${{ secrets.pypi_password }}
        packages_dir: standard/

    - name: Publish global package
      uses: pypa/gh-action-pypi-publish@v1.5.0
      with:
        password: ${{ secrets.pypi_password_global }}
        packages_dir: global/

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/upstream.yml

```yaml

name: Upstream

on:
  workflow_dispatch:
  pull_request:

concurrency:
  group: upstream-${{ github.ref }}
  cancel-in-progress: true

env:
  PIP_ONLY_BINARY: numpy

jobs:
  standard:
    name: "🐍 3.11 dev • ubuntu-latest • x64"
    runs-on: ubuntu-latest
    if: "contains(github.event.pull_request.labels.*.name, 'python dev')"

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python 3.11
      uses: actions/setup-python@v2
      with:
        python-version: "3.11-dev"

    - name: Setup Boost (Linux)
      if: runner.os == 'Linux'
      run: sudo apt-get install libboost-dev

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Setup annotations on Linux
      if: runner.os == 'Linux'
      run: python -m pip install pytest-github-actions-annotate-failures

    # First build - C++11 mode and inplace
    - name: Configure C++11
      run: >
        cmake -S . -B .
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=11

    - name: Build C++11
      run: cmake --build . -j 2

    - name: Python tests C++11
      run: cmake --build . --target pytest -j 2

    - name: C++11 tests
      run: cmake --build .  --target cpptest -j 2

    - name: Interface test C++11
      run: cmake --build . --target test_cmake_build

    - name: Clean directory
      run: git clean -fdx

    # Second build - C++17 mode and in a build directory
    - name: Configure C++17
      run: >
        cmake -S . -B build2
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        ${{ matrix.args }}
        ${{ matrix.args2 }}

    - name: Build
      run: cmake --build build2 -j 2

    - name: Python tests
      run: cmake --build build2 --target pytest

    - name: C++ tests
      run: cmake --build build2 --target cpptest

    # Third build - C++17 mode with unstable ABI
    - name: Configure (unstable ABI)
      run: >
        cmake -S . -B build3
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        -DPYBIND11_INTERNALS_VERSION=10000000
        "-DPYBIND11_TEST_OVERRIDE=test_call_policies.cpp;test_gil_scoped.cpp;test_thread.cpp"
        ${{ matrix.args }}

    - name: Build (unstable ABI)
      run: cmake --build build3 -j 2

    - name: Python tests (unstable ABI)
      run: cmake --build build3 --target pytest

    - name: Interface test
      run: cmake --build build2 --target test_cmake_build

    # This makes sure the setup_helpers module can build packages using
    # setuptools
    - name: Setuptools helpers test
      run: pytest tests/extra_setuptools

```

### raisimGymTorch/thirdParty/pybind11/.pre-commit-config.yaml

```yaml
# To use:
#
#     pre-commit run -a
#
# Or:
#
#     pre-commit install  # (runs every time you commit in git)
#
# To update this file:
#
#     pre-commit autoupdate
#
# See https://github.com/pre-commit/pre-commit

repos:
# Standard hooks
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.1.0
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-docstring-first
  - id: check-merge-conflict
  - id: check-symlinks
  - id: check-toml
  - id: check-yaml
  - id: debug-statements
  - id: end-of-file-fixer
  - id: mixed-line-ending
  - id: requirements-txt-fixer
  - id: trailing-whitespace
  - id: fix-encoding-pragma
    exclude: ^noxfile.py$

- repo: https://github.com/asottile/pyupgrade
  rev: v2.31.0
  hooks:
  - id: pyupgrade

- repo: https://github.com/PyCQA/isort
  rev: 5.10.1
  hooks:
  - id: isort

# Black, the code formatter, natively supports pre-commit
- repo: https://github.com/psf/black
  rev: 21.12b0 # Keep in sync with blacken-docs
  hooks:
  - id: black

- repo: https://github.com/asottile/blacken-docs
  rev: v1.12.0
  hooks:
  - id: blacken-docs
    additional_dependencies:
    - black==21.12b0 # keep in sync with black hook

# Changes tabs to spaces
- repo: https://github.com/Lucas-C/pre-commit-hooks
  rev: v1.1.10
  hooks:
  - id: remove-tabs

# Autoremoves unused imports
- repo: https://github.com/hadialqattan/pycln
  rev: v1.1.0
  hooks:
  - id: pycln

- repo: https://github.com/pre-commit/pygrep-hooks
  rev: v1.9.0
  hooks:
  - id: python-check-blanket-noqa
  - id: python-check-blanket-type-ignore
  - id: python-no-log-warn
  - id: rst-backticks
  - id: rst-directive-colons
  - id: rst-inline-touching-normal

# Flake8 also supports pre-commit natively (same author)
- repo: https://github.com/PyCQA/flake8
  rev: 4.0.1
  hooks:
  - id: flake8
    additional_dependencies: &flake8_dependencies
      - flake8-bugbear
      - pep8-naming
    exclude: ^(docs/.*|tools/.*)$

- repo: https://github.com/asottile/yesqa
  rev: v1.3.0
  hooks:
  - id: yesqa
    additional_dependencies: *flake8_dependencies

# CMake formatting
- repo: https://github.com/cheshirekow/cmake-format-precommit
  rev: v0.6.13
  hooks:
  - id: cmake-format
    additional_dependencies: [pyyaml]
    types: [file]
    files: (\.cmake|CMakeLists.txt)(.in)?$

# Check static types with mypy
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v0.931
  hooks:
  - id: mypy
    # Running per-file misbehaves a bit, so just run on all files, it's fast
    pass_filenames: false
    additional_dependencies: [typed_ast]

# Checks the manifest for missing files (native support)
- repo: https://github.com/mgedmin/check-manifest
  rev: "0.47"
  hooks:
  - id: check-manifest
    # This is a slow hook, so only run this if --hook-stage manual is passed
    stages: [manual]
    additional_dependencies: [cmake, ninja]

- repo: https://github.com/codespell-project/codespell
  rev: v2.1.0
  hooks:
  - id: codespell
    exclude: ".supp$"
    args: ["-L", "nd,ot,thist"]

- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: v0.8.0.3
  hooks:
  - id: shellcheck

# The original pybind11 checks for a few C++ style items
- repo: local
  hooks:
  - id: disallow-caps
    name: Disallow improper capitalization
    language: pygrep
    entry: PyBind|Numpy|Cmake|CCache|PyTest
    exclude: .pre-commit-config.yaml

- repo: local
  hooks:
  - id: check-style
    name: Classic check-style
    language: system
    types:
    - c++
    entry: ./tools/check-style.sh

```

### raisimGymTorch/thirdParty/pybind11/.readthedocs.yml

```yaml
python:
  version: 3
requirements_file: docs/requirements.txt

```

### thirdParty/pybind11/.github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
  - name: Ask a question
    url: https://github.com/pybind/pybind11/discussions/new
    about: Please ask and answer questions here, or propose new ideas.
  - name: Gitter room
    url: https://gitter.im/pybind/Lobby
    about: A room for discussing pybind11 with an active community

```

### thirdParty/pybind11/.github/workflows/configure.yml

```yaml
name: Config

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - master
      - stable
      - v*

jobs:
  # This tests various versions of CMake in various combinations, to make sure
  # the configure step passes.
  cmake:
    strategy:
      fail-fast: false
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
        arch: [x64]
        cmake: ["3.21"]

        include:
        - runs-on: ubuntu-latest
          arch: x64
          cmake: 3.4

        - runs-on: macos-latest
          arch: x64
          cmake: 3.7

        - runs-on: windows-2016
          arch: x86
          cmake: 3.8

        - runs-on: windows-2016
          arch: x86
          cmake: 3.18

    name: 🐍 3.7 • CMake ${{ matrix.cmake }} • ${{ matrix.runs-on }}
    runs-on: ${{ matrix.runs-on }}

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: 3.7
        architecture: ${{ matrix.arch }}

    - name: Prepare env
      run: python -m pip install -r tests/requirements.txt

    # An action for adding a specific version of CMake:
    #   https://github.com/jwlawson/actions-setup-cmake
    - name: Setup CMake ${{ matrix.cmake }}
      uses: jwlawson/actions-setup-cmake@v1.11
      with:
        cmake-version: ${{ matrix.cmake }}

    # These steps use a directory with a space in it intentionally
    - name: Make build directories
      run: mkdir "build dir"

    - name: Configure
      working-directory: build dir
      shell: bash
      run: >
        cmake ..
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DPYTHON_EXECUTABLE=$(python -c "import sys; print(sys.executable)")

    # Only build and test if this was manually triggered in the GitHub UI
    - name: Build
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release

    - name: Test
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release --target check

```

### thirdParty/pybind11/.pre-commit-config.yaml

```yaml
# To use:
#
#     pre-commit run -a
#
# Or:
#
#     pre-commit install  # (runs every time you commit in git)
#
# To update this file:
#
#     pre-commit autoupdate
#
# See https://github.com/pre-commit/pre-commit

repos:
# Standard hooks
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.1.0
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-docstring-first
  - id: check-merge-conflict
  - id: check-symlinks
  - id: check-toml
  - id: check-yaml
  - id: debug-statements
  - id: end-of-file-fixer
  - id: mixed-line-ending
  - id: requirements-txt-fixer
  - id: trailing-whitespace
  - id: fix-encoding-pragma
    exclude: ^noxfile.py$

- repo: https://github.com/asottile/pyupgrade
  rev: v2.31.0
  hooks:
  - id: pyupgrade

- repo: https://github.com/PyCQA/isort
  rev: 5.10.1
  hooks:
  - id: isort

# Black, the code formatter, natively supports pre-commit
- repo: https://github.com/psf/black
  rev: 21.12b0 # Keep in sync with blacken-docs
  hooks:
  - id: black

- repo: https://github.com/asottile/blacken-docs
  rev: v1.12.0
  hooks:
  - id: blacken-docs
    additional_dependencies:
    - black==21.12b0 # keep in sync with black hook

# Changes tabs to spaces
- repo: https://github.com/Lucas-C/pre-commit-hooks
  rev: v1.1.10
  hooks:
  - id: remove-tabs

# Autoremoves unused imports
- repo: https://github.com/hadialqattan/pycln
  rev: v1.1.0
  hooks:
  - id: pycln

- repo: https://github.com/pre-commit/pygrep-hooks
  rev: v1.9.0
  hooks:
  - id: python-check-blanket-noqa
  - id: python-check-blanket-type-ignore
  - id: python-no-log-warn
  - id: rst-backticks
  - id: rst-directive-colons
  - id: rst-inline-touching-normal

# Flake8 also supports pre-commit natively (same author)
- repo: https://github.com/PyCQA/flake8
  rev: 4.0.1
  hooks:
  - id: flake8
    additional_dependencies: &flake8_dependencies
      - flake8-bugbear
      - pep8-naming
    exclude: ^(docs/.*|tools/.*)$

- repo: https://github.com/asottile/yesqa
  rev: v1.3.0
  hooks:
  - id: yesqa
    additional_dependencies: *flake8_dependencies

# CMake formatting
- repo: https://github.com/cheshirekow/cmake-format-precommit
  rev: v0.6.13
  hooks:
  - id: cmake-format
    additional_dependencies: [pyyaml]
    types: [file]
    files: (\.cmake|CMakeLists.txt)(.in)?$

# Check static types with mypy
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v0.931
  hooks:
  - id: mypy
    # Running per-file misbehaves a bit, so just run on all files, it's fast
    pass_filenames: false
    additional_dependencies: [typed_ast]

# Checks the manifest for missing files (native support)
- repo: https://github.com/mgedmin/check-manifest
  rev: "0.47"
  hooks:
  - id: check-manifest
    # This is a slow hook, so only run this if --hook-stage manual is passed
    stages: [manual]
    additional_dependencies: [cmake, ninja]

- repo: https://github.com/codespell-project/codespell
  rev: v2.1.0
  hooks:
  - id: codespell
    exclude: ".supp$"
    args: ["-L", "nd,ot,thist"]

- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: v0.8.0.3
  hooks:
  - id: shellcheck

# The original pybind11 checks for a few C++ style items
- repo: local
  hooks:
  - id: disallow-caps
    name: Disallow improper capitalization
    language: pygrep
    entry: PyBind|Numpy|Cmake|CCache|PyTest
    exclude: .pre-commit-config.yaml

- repo: local
  hooks:
  - id: check-style
    name: Classic check-style
    language: system
    types:
    - c++
    entry: ./tools/check-style.sh

```

## Python signatures and reward/observation bodies (116 files)


### raisimGymTorch/common/abstract_pl.py

```
def detect_loss_anomaly(loss_dict, max_val, step, warmup_steps)
def tear_down(msg, out, exp_key, failed_state_p)
class AbstractPL(LightningModule)
    def __init__(self, args, push_images_fn, tracked_metric, metric_init_val, high_loss_val, warmup_steps)
    def set_training_flags(self)
    def load_from_ckpt(self, ckpt_path)
    def training_step(self, batch, batch_idx)
    def on_train_epoch_end(self)
    def validation_step(self, batch, batch_idx)
    def on_validation_epoch_end(self)
    def on_test_epoch_end(self)
    def test_step(self, batch, batch_idx)
    def inference_step(self, batch, batch_idx)
    def inference_epoch_end(self, out_list, postfix)
    def configure_optimizers(self)
    def visualize_batches(self, batches, postfix, no_tqdm, dump_vis)
```

### raisimGymTorch/common/args_utils.py

```
def set_default_params(args, default_args)
```

### raisimGymTorch/common/body_models.py

```
class MANODecimator()
    def __init__(self)
    def downsample(self, verts, is_right)
def seal_mano_mesh(v3d, faces, is_rhand)
class MANOJointRegressor(Module)
    def __init__(self)
    def forward(self, verts, is_right)
def build_layers(device)
def build_smplx(batch_size, gender, vtemplate)
def build_subject_smplx(batch_size, subject_id)
def build_mano_aa(is_rhand, create_transl, flat_hand)
def construct_layers(dev)
```

### raisimGymTorch/common/camera.py

```
def perspective_to_weak_perspective_torch(perspective_camera, focal_length, img_res)
def convert_perspective_to_weak_perspective(perspective_camera, focal_length, img_res)
def convert_weak_perspective_to_perspective(weak_perspective_camera, focal_length, img_res)
def get_default_cam_t(f, img_res)
def estimate_translation_np(S, joints_2d, joints_conf, focal_length, img_size)
def estimate_translation(S, joints_2d, focal_length, img_size, use_all_joints, rotation, pad_2d)
def estimate_translation_cam(S, joints_2d, focal_length, img_size, use_all_joints, rotation)
def get_coord_maps(size)
def look_at(eye, at, up, eps)
def to_sphere(u, v)
def sample_on_sphere(range_u, range_v)
def sample_pose_on_sphere(range_v, range_u, radius, up)
def rectify_pose(camera_r, body_aa, rotate_x)
def estimate_translation_k_np(S, joints_2d, joints_conf, K)
def estimate_translation_k(S, joints_2d, K, use_all_joints, rotation, pad_2d)
def weak_perspective_to_perspective_torch(weak_perspective_camera, focal_length, img_res, min_s)
```

### raisimGymTorch/common/cluster_utils.py

```
class CPUCluster()
    def __init__(self, tasks, op, num_threads, num_nodes)
    def run(self, chunk_id)
    def __len__(self)
```

### raisimGymTorch/common/comet_utils.py

```
def add_paths(args)
def save_args(args, save_keys)
def create_files(args)
def log_exp_meta(args)
def init_experiment(args)
def log_dict(experiment, metric_dict, step, postfix)
def generate_exp_key()
def fetch_key_from_experiment(experiment)
def push_images(experiment, all_im_list, global_step, no_tqdm, verbose)
```

### raisimGymTorch/common/condor_cluster.py

```
def add_cluster_args(parser)
class CondorCluster()
    def __init__(self, args, script, num_exp)
    def submit(self)
    def _create_requirements(self, gpus, skip_nodes)
    def _create_submission_file(self, run_script, gpus, submit_p)
    def _create_bash_file(self, run_p)
    def _get_gpus(self, min_mem, arch)
```

### raisimGymTorch/common/data_utils.py

```
"""This file contains functions that are used to perform data augmentation."""
def in_hull(p, hull)
def rotate_2d(pt_2d, rot_rad)
def gen_trans_from_patch_cv(c_x, c_y, src_width, src_height, dst_width, dst_height, scale, rot, inv)
def generate_patch_image(cvimg, bbox, scale, rot, out_shape, interpl_strategy, gauss_kernel, gauss_sigma)
def augm_params(is_train, flip_prob, noise_factor, rot_factor, scale_factor)
def rgb_processing(is_train, rgb_img, center, bbox_dim, augm_dict, img_res)
def transform_kp2d(kp2d, bbox)
def j2d_processing(kp, center, bbox_dim, augm_dict, img_res)
def j3d_processing(S, augm_dict)
def pose_processing(pose, augm_dict)
def get_transform(center, scale, res, rot)
def transform(pt, center, scale, res, invert, rot)
def crop(img, center, scale, res, rot)
def crop_cv2(img, center, scale, res, rot)
def get_random_crop_coords(height, width, crop_height, crop_width, h_start, w_start)
def random_crop(center, scale, crop_scale_factor, axis)
def uncrop(img, center, scale, orig_shape, rot, is_rgb)
def rot_aa(aa, rot)
def flip_img(img)
def flip_kp(kp)
def flip_pose(pose)
def denormalize_images(images)
def read_img(img_fn, dummy_shape)
def _read_img(img_fn)
def normalize_kp2d_np(kp2d, img_res)
def unnormalize_2d_kp(kp_2d_np, res)
def normalize_kp2d(kp2d, img_res)
def unormalize_kp2d(kp2d_normalized, img_res)
def image_dim_to_bbox(width, height)
def crop_kp2d(kp2d, cx, cy, dim)
def get_wp_intrix(fixed_focal, img_res)
def get_aug_intrix(intrx, fixed_focal, img_res, use_gt_k, bbox_cx, bbox_cy, scale)
def compute_joint_valid(joints2d, speedup, is_egocam, full_width, full_height, cx_loose, cy_loose, dim_loose, center, bbox_dim, augm_dict, img_res)
```

### raisimGymTorch/common/exp_manager.py

```
class ExpManager()
    def __init__(self, args)
    def run_experiment(self, use_cluster, script, num_exp, logdir_format)
```

### raisimGymTorch/common/ld_utils.py

```
def sort_dict(disordered)
def prefix_dict(mydict, prefix)
def postfix_dict(mydict, postfix)
def unsort(L, sort_idx)
def cat_dl(out_list, dim, verbose, squeeze)
def stack_dl(out_list, dim, verbose, squeeze)
def add_prefix_postfix(mydict, prefix, postfix)
def ld2dl(LD)
class NameSpace(object)
    def __init__(self, adict)
def dict2ns(mydict)
def ld2dev(ld, dev)
def all_comb_dict(hyper_dict)
```

### raisimGymTorch/common/list_utils.py

```
def chunks_by_len(L, n)
def chunks_by_size(L, n)
def unsort(L, sort_idx)
def add_prefix_postfix(mydict, prefix, postfix)
def ld2dl(LD)
def chunks(lst, n)
```

### raisimGymTorch/common/mesh.py

```
class Mesh(Trimesh)
    def __init__(self, filename, v, f, vc, fc, process, visual)
    def rot_verts(self, vertices, rxyz)
    def colors_like(self, color, array, ids)
    def set_vc(self, vc, vertex_ids)
    def set_fc(self, fc, face_ids)
    def cat(meshes)
```

### raisimGymTorch/common/metrics.py

```
def compute_similarity_transform(S1, S2)
def compute_similarity_transform_batch(S1, S2)
def reconstruction_error(S1, S2, reduction)
def compute_pck_mano(gt_dist, pred_dist, valid, dummy, alpha)
def compute_pck_obj(gt_dist, pred_dist, valid, vlen, alpha)
def compute_v2v_dist_no_reduce(v3d_cam_gt, v3d_cam_pred, is_valid)
def compute_v2v_dist(v3d_cam_gt, v3d_cam_pred, is_valid)
def compute_diameter(v3d, num_samples)
def compute_joint3d_error(joints3d_cam_gt, joints3d_cam_pred, valid_jts)
def compute_joint2d_error(joints2d_gt, joints2d_pred, valid_jts, img_res)
def compute_mrrpe(root_r_gt, root_l_gt, root_r_pred, root_l_pred, is_valid)
def compute_iou_metrics(bbox3d_cam_gt_top, bbox3d_cam_pred_top, bbox3d_cam_gt_bottom, bbox3d_cam_pred_bottom, is_valid)
def compute_arti_deg_error(pred_radian, gt_radian)
def pts_inside_box_torch(pts, bbox)
def iou_3d_torch(bbox1, bbox2, dev, nres)
def segm_iou(pred, target, n_classes, tol, background_cls)
def joint_angle_error(pred_mat, gt_mat)
```

### raisimGymTorch/common/np_utils.py

```
def permute_np(x, idx)
```

### raisimGymTorch/common/object_tensors.py

```
class ObjectTensors(Module)
    def __init__(self)
    def forward_7d_batch(self, angles, global_orient, transl, query_names, fwd_template)
    def forward(self, angles, global_orient, transl, query_names)
    def forward_template(self, query_names)
    def to(self, dev)
    def _sanity_check(self, angles, global_orient, transl, query_names, fwd_template)
def construct_obj(object_model_p)
def construct_obj_tensors(object_names)
```

### raisimGymTorch/common/pl_utils.py

```
def reweight_loss_by_keys(loss_dict, keys, alpha)
def select_loss_group(groups, agent_id, alphas)
def push_checkpoint_metric(key, val)
def avg_losses_cpu(outputs)
def reform_outputs(out_list)
```

### raisimGymTorch/common/rend_utils.py

```
def flip_meshes(meshes)
def color2material(mesh_color)
class Renderer()
    def __init__(self, img_res)
    def render_meshes_pose(self, meshes, image, cam_transl, cam_center, K, materials, sideview_angle)
    def render_meshes_contact(self, meshes, image, cam_transl, cam_center, K, sideview_angle, no_anchor, random_rot, z_dist)
    def render_rgb(self)
    def overlay_image(self, color, valid_mask, image)
    def position_camera(self, cam_transl, K)
    def setup_light(self)
    def create_scene(self)
```

### raisimGymTorch/common/rot.py

```
def standardize_quaternion(quaternions)
def quaternion_multiply(a, b)
def _sqrt_positive_part(x)
def quaternion_to_axis_angle(quaternions)
def quaternion_to_matrix(quaternions)
def matrix_to_quaternion(matrix)
def matrix_to_axis_angle(matrix)
def rot_aa(aa, rot)
def quat2mat(quat)
def batch_aa2rot(axisang)
def batch_rot2aa(Rs)
def batch_rodrigues(theta)
def quat_to_rotmat(quat)
def rot6d_to_rotmat(x)
def rotmat_to_rot6d(x)
def rotation_matrix_to_angle_axis(rotation_matrix)
def quaternion_to_angle_axis(quaternion)
def rotation_matrix_to_quaternion(rotation_matrix, eps)
def batch_euler2matrix(r)
def euler_to_quaternion(r)
def quaternion_to_rotation_matrix(quat)
def euler_angles_from_rotmat(R)
def quaternion_raw_multiply(a, b)
def quaternion_invert(quaternion)
def quaternion_apply(quaternion, point)
def axis_angle_to_quaternion(axis_angle)
```

### raisimGymTorch/common/skeleton_utils.py

```
def keypoint_hflip(kp, img_width)
def convert_kps(joints2d, src, dst)
def get_perm_idxs(src, dst)
def get_smpl_joint_names()
def get_smpl_skeleton()
def get_mano_joint_names()
def get_mano_skeleton()
def get_freihand_joint_names()
def get_freihand_skeleton()
def get_mano21_joint_names()
def get_mano21_skeleton()
```

### raisimGymTorch/common/sys_utils.py

```
def copy(src, dst)
def copy_repo(src_files, dst_folder, filter_keywords)
def get_branch()
def get_commit_hash()
def mkdir(directory)
def mkdir_p(exp_path)
def count_files(path)
def get_host_name()
```

### raisimGymTorch/common/thing.py

```
def thing2list(thing)
def thing2dev(thing, dev)
def thing2np(thing)
def thing2torch(thing)
def detach_thing(thing)
```

### raisimGymTorch/common/torch_utils.py

```
def nanmean(v)
def grad_norm(model)
def pad_tensor_list(v_list)
def unpad_vtensor(vtensor, lens)
def one_hot_embedding(labels, num_classes)
def unsort(ten, sort_idx)
def softargmax_kd(inputs_hm, temperature)
def gumbel_sample_kd(hm, num_samples, tau, logit_scale, hard)
def gumbel_sample_kd_iter(hm, num_samples, tau, logit_scale, hard, chunk_size)
def fetch_comb_index(num, dev, comb_type)
def all_comb(X, Y)
def toggle_parameters(model, requires_grad)
def detach_tensor(ten)
def count_model_parameters(model)
def reset_all_seeds(seed)
def get_activation(name)
def stack_ll_tensors(tensor_list_list)
def get_optim(name)
def decay_lr(optimizer, gamma)
```

### raisimGymTorch/common/transforms.py

```
def to_homo(x)
def to_homo_batch(x)
def to_xyz(x_homo)
def to_xyz_batch(x_homo)
def to_xy(x_homo)
def to_xy_batch(x_homo)
def distort_pts3d_all(_pts_cam, dist_coeffs)
def rigid_tf_torch_batch(points, R, T)
def solve_rigid_tf_np(A, B)
def batch_solve_rigid_tf(A, B)
def rigid_tf_np(points, R, T)
def perspective_projection(points, rotation, translation, focal_length, camera_center)
def weak_perspective_projection(points, rotation, weak_cam_params, focal_length, camera_center, img_res)
def transform_points(world2cam_mat, pts)
def transform_points_batch(world2cam_mat, pts)
def project2d_batch(K, pts_cam)
def project2d_norm_batch(K, pts_cam, patch_width)
def project2d(K, pts_cam)
```

### raisimGymTorch/common/video_utils.py

```
def images2video(im_paths, video_name, fps)
```

### raisimGymTorch/common/viewer.py

```
class ViewerData(edict)
    """Interface to standardize viewer data."""
    def __init__(self, Rt, K, cols, rows, imgnames)
    def validate_format(self)
class ARCTICViewer()
    def __init__(self, render_types, interactive, size)
    def view_interactive(self)
    def view_fn_headless(self, num_iter, out_folder)
    def load_data(self)
    def check_format(self, batch)
    def render_seq(self, batch, out_folder)
    def setup_viewer(self, data)
def dist2vc_segm(contact_t, num_parts)
def dist2vc(dist_ro, dist_lo, dist_o, _cmap, tf_fn)
def dist2vc_bin(_dist)
def small_exp_map(_dist)
def dist2vc_cont_exp(_dist, _cmap)
def dist2vc_cont(_dist, _cmap)
def construct_viewer_meshes(data, draw_edges, flat_shading)
def setup_viewer(v, shared_folder_p, video, images_path, data, flag, seq_name, side_angle)
def render_depth(v, depth_p)
def render_mask(v, mask_p)
def setup_billboard(data, v)
```

### raisimGymTorch/common/vis_utils.py

```
def plot_2d_bbox(bbox_2d, bones, color, ax)
def plot_3d_bbox(ax, bbox_pts, bones, color)
def random_cmap(nlabels, type, first_color_black, last_color_black, verbose)
def imshow_attn(im, att, im_alpha, att_alpha, ax, cmap)
def plot_origin(ax)
def axis_equal_3d(ax)
def plot_grad_flow(named_parameters)
def plot_bbox(xyxy, line, color, linewidth)
def fig2data(fig)
def fig2img(fig)
def concat_pil_images(images)
def stack_pil_images(images)
def im_list_to_plt(image_list, figsize, title_list)
```

### raisimGymTorch/common/xdict.py

```
def _print_stat(key, thing)
class xdict(dict)
    """A subclass of Python's built-in dict class, which provides additional methods for manipulating and operating on dictionaries."""
    def __init__(self, mydict)
    def subset(self, keys)
    def __setitem__(self, key, val)
    def search(self, keyword, replace_to)
    def rm(self, keyword, keep_list, verbose)
    def overwrite(self, k, v)
    def merge(self, dict2)
    def mul(self, scalar)
    def prefix(self, text)
    def replace_keys(self, str_src, str_tar)
    def postfix(self, text)
    def sorted_keys(self)
    def to(self, dev)
    def to_torch(self)
    def to_np(self)
    def tolist(self)
    def print_stat(self)
    def detach(self)
    def has_invalid(self)
    def apply(self, operation, criterion)
    def save(self, path, dev, verbose)
```

### raisimGymTorch/raisimGymTorch/algo/ppo/module.py

```
class Actor()
    def __init__(self, architecture, distribution, device)
    def sample(self, obs)
    def evaluate(self, obs, actions)
    def parameters(self)
    def noiseless_action(self, obs)
    def save_deterministic_graph(self, file_name, example_input, device)
    def deterministic_parameters(self)
    def update(self)
    def obs_shape(self)
    def action_shape(self)
class Critic()
    def __init__(self, architecture, device)
    def predict(self, obs)
    def evaluate(self, obs)
    def parameters(self)
    def obs_shape(self)
class MLP(Module)
    def __init__(self, shape, actionvation_fn, input_size, output_size)
    def init_weights(sequential, scales)
class MultivariateGaussianDiagonalCovariance(Module)
    def __init__(self, dim, size, init_std, fast_sampler, seed)
    def update(self)
    def sample(self, logits)
    def evaluate(self, logits, outputs)
    def entropy(self)
    def enforce_minimum_std(self, min_std)
```

### raisimGymTorch/raisimGymTorch/algo/ppo/ppo.py

```
class PPO()
    def __init__(self, actor, critic, num_envs, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, learning_rate_schedule, desired_kl, use_clipped_value_loss, log_dir, device, shuffle_batch)
    def act(self, actor_obs)
    def step(self, value_obs, rews, dones)
    def update(self, actor_obs, value_obs, log_this_iteration, update)
    def log(self, variables)
    def _train_step(self, log_this_iteration)
```

### raisimGymTorch/raisimGymTorch/algo/ppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, actor_obs_shape, critic_obs_shape, actions_shape, device)
    def add_transitions(self, actor_obs, critic_obs, actions, mu, sigma, rewards, dones, actions_log_prob)
    def clear(self)
    def compute_returns(self, last_values, critic, gamma, lam)
    def mini_batch_generator_shuffle(self, num_mini_batches)
    def mini_batch_generator_inorder(self, num_mini_batches)
```

### raisimGymTorch/raisimGymTorch/env/RaisimGymVecEnv.py

```
class RaisimGymVecEnv()
    def __init__(self, impl, cfg, normalize_ob, seed, normalize_rew, clip_obs)
    def seed(self, seed)
    def set_pd_wrist(self)
    def turn_on_visualization(self)
    def turn_off_visualization(self)
    def start_video_recording(self, file_name)
    def stop_video_recording(self)
    def step(self, action_r, action_l)
    def step2(self, action_r, action_l)
    def reset_right_hand(self, obj_pose_step_r, hand_ee_step_r, hand_pose_step_r)
    def step_imitate(self, action_r, action_l, obj_pose_r, hand_ee_r, hand_pose_r, obj_pose_l, hand_ee_l, hand_pose_l, imitate_right, imitate_left)
    def load_scaling(self, dir_name, iteration, count, cent_training)
    def save_scaling(self, dir_name, iteration)
    def observe(self, update_mean)
    def get_global_state(self, update_mean)
    def set_rootguidance(self)
    def switch_root_guidance(self, is_on)
    def control_switch(self, left, right)
    def control_switch_all(self, left, right)
    def reset(self)
    def add_stage(self, stage_dim, stage_pos)
    def switch_arctic(self, idx)
    def load_object(self, obj_idx, obj_weight, obj_dim, obj_type)
    def load_articulated(self, obj_model)
    def load_multi_articulated(self, obj_models)
    def reset_state(self, init_state_r, init_state_l, init_vel_r, init_vel_l, obj_pose)
    def set_goals_r(self, obj_pos_r, ee_pos_r, pose_r, qpos_r)
    def set_imitation_goals(self, pose_l, pose_r, obj_pose)
    def set_goals_r2(self, obj_pos_r, ee_pos_r, pose_r, qpos_r, contact_r)
    def set_ext(self, ext_force, ext_torque)
    def set_pregrasp(self, obj_pos, ee_pos, pose)
    def set_goals(self, obj_angle, obj_pos, ee_pos_r, ee_pos_l, pose_r, pose_l, qpos_r, qpos_l, contact_r, contact_l)
    def set_obj_goal(self, obj_angle, obj_pos)
    def _normalize_observation(self, obs, is_rhand)
    def _normalize_global_state(self, gs)
    def close(self)
    def curriculum_callback(self)
    def get_reward_info(self)
    def get_reward_info_r(self)
    def num_envs(self)
class RunningMeanStd(object)
    def __init__(self, epsilon, shape)
    def update(self, arr)
    def update_from_moments(self, batch_mean, batch_var, batch_count)

```python
def _normalize_observation(self, obs, is_rhand):
        if self.normalize_ob:
            if is_rhand:
                return np.clip((obs - self.obs_rms_r.mean) / np.sqrt(self.obs_rms_r.var + 1e-8), -self.clip_obs,
                                self.clip_obs)
            else:
                return np.clip((obs - self.obs_rms_l.mean) / np.sqrt(self.obs_rms_l.var + 1e-8), -self.clip_obs,
                                self.clip_obs)
        else:
            return obs
```

```python
def get_reward_info(self):
        return self.wrapper.rewardInfoLeft()
```

```python
def get_reward_info_r(self):
        return self.wrapper.rewardInfoRight()
```
```

### raisimGymTorch/raisimGymTorch/helper/label_gen_final.py

```
class Labels()
    def __init__(self)
def generate_recon_test_set_online(obj_name)
def generate_new_train_test_set()
def get_special_labels()
def label_eval_floating(obj_name, test)
def label_eval_compose(obj_name, test)
def label_eval_fixed(obj_name, test)
def label_train_r(num_repeats, eval, test, obj_cmd)
def label_train_l(num_repeats, eval, test, obj_cmd)
def label_train(num_repeats, eval, test)
def pose_gen(labels, num_repeats, use_init_frame, recon_flag, pre_contact)
def label_gen_final(seq_num, seq_name)
```

### raisimGymTorch/raisimGymTorch/helper/raisim_gym_helper.py

```
class ConfigurationSaver()
    def __init__(self, log_dir, save_items, test_dir)
    def data_dir(self)
def tensorboard_launcher(directory_path)
def load_param(weight_path, env, actor, critic, optimizer, data_dir, cfg)
```

### raisimGymTorch/raisimGymTorch/helper/raisim_gym_helper_hierarchy.py

```
class ConfigurationSaver()
    def __init__(self, log_dir, save_items, hierarchy_dir)
    def data_dir(self)
def tensorboard_launcher(directory_path)
def load_param(weight_path, env, actor, critic, optimizer, data_dir, cfg)
```

### raisimGymTorch/raisimGymTorch/helper/rotations.py

```
def axisangle2mat(rot_vecs, epsilon)
def axisangle2quat(axis_angle)
def axisangle2euler(axis_angle)
def euler2mat(euler)
def euler2quat(euler)
def mat2euler(mat)
def mat2quat(mat)
def quat2euler(quat)
def subtract_euler(e1, e2)
def quat2mat(quat)
def quat_conjugate(q)
def quat_mul(q0, q1)
def quat_rot_vec(q, v0)
def quat_identity()
def quat2axisangle(quat)
def euler2point_euler(euler)
def point_euler2euler(euler)
def quat2point_quat(quat)
def point_quat2quat(quat)
def normalize_angles(angles)
def round_to_straight_angles(angles)
def get_parallel_rotations()
```

### raisimGymTorch/raisimGymTorch/helper/utils.py

```
def concat_dict(dict)
def setup_seed(seed)
def get_obj_pcd(path, num_p)
def first_nonzero(arr, axis, invalid_val)
def dgrasp_to_mano(param, is_right)
def show_pointcloud_objhand(hand, obj)
def get_args()
def repeat_label(label_dict, num_repeats)
def euler_noise_to_quat(quats, palm_pose, noise)
```

### raisimGymTorch/setup.py

```
class CMakeExtension(Extension)
    def __init__(self, name, sourcedir)
class CMakeBuild(build_ext)
    def run(self)
    def build_extension(self, ext)
```

### raisimGymTorch/thirdParty/pybind11/noxfile.py

```
def lint(session)
def tests(session)
def tests_packaging(session)
def docs(session)
def make_changelog(session)
def build(session)
```

### raisimGymTorch/thirdParty/pybind11/pybind11/__main__.py

```
def print_includes()
def main()
```

### raisimGymTorch/thirdParty/pybind11/pybind11/_version.py

```
def _to_int(s)
```

### raisimGymTorch/thirdParty/pybind11/pybind11/commands.py

```
def get_include(user)
def get_cmake_dir()
```

### raisimGymTorch/thirdParty/pybind11/pybind11/setup_helpers.py

```
"""This module provides helpers for C++11+ projects using pybind11.

LICENSE:

Copyright (c) 2016 Wenzel Jakob <wenzel.jakob@epfl.ch>, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other """
class Pybind11Extension(_Extension)
    """Build a C++11+ Extension module with pybind11. This automatically adds the
recommended flags when you init the extension and assumes C++ sources - you
can further modify the options yourself.

The customizations are:

* ``/EHsc`` and ``/bigobj`` on Windows
* ``stdlib=libc++`` on macOS
* ``visibility"""
    def _add_cflags(self, flags)
    def _add_ldflags(self, flags)
    def __init__(self)
    def cxx_std(self)
    def cxx_std(self, level)
def tmp_chdir()
def has_flag(compiler, flag)
def auto_cpp_level(compiler)
class build_ext(_build_ext)
    """Customized build_ext that allows an auto-search for the highest supported
C++ level for Pybind11Extension. This is only needed for the auto-search
for now, and is completely optional otherwise."""
    def build_extensions(self)
def intree_extensions(paths, package_dir)
def naive_recompile(obj, src)
def no_recompile(obg, src)
class ParallelCompile(object)
    """Make a parallel compile function. Inspired by
numpy.distutils.ccompiler.CCompiler_compile and cppimport.

This takes several arguments that allow you to customize the compile
function created:

envvar:
    Set an environment variable to control the compilation threads, like
    NPY_NUM_BUILD_JOBS
de"""
    def __init__(self, envvar, default, max, needs_recompile)
    def function(self)
    def install(self)
    def __enter__(self)
    def __exit__(self)
```

### raisimGymTorch/thirdParty/pybind11/setup.py

```
def build_expected_version_hex(matches)
def get_and_replace(filename, binary)
class SDist(sdist)
    def make_release_tree(self, base_dir, files)
def TemporaryDirectory()
def remove_output()
```

### raisimGymTorch/thirdParty/pybind11/tests/conftest.py

```
"""pytest configuration

Extends output capture as needed by pybind11: ignore constructors, optional unordered lines.
Adds docstring and exceptions message sanitizers: ignore Python 2 vs 3 differences."""
def _strip_and_dedent(s)
def _split_and_sort(s)
def _make_explanation(a, b)
class Output(object)
    """Basic output post-processing and comparison"""
    def __init__(self, string)
    def __str__(self)
    def __eq__(self, other)
class Unordered(Output)
    """Custom comparison for output without strict line ordering"""
    def __eq__(self, other)
class Capture(object)
    def __init__(self, capfd)
    def __enter__(self)
    def __exit__(self)
    def __eq__(self, other)
    def __str__(self)
    def __contains__(self, item)
    def unordered(self)
    def stderr(self)
def capture(capsys)
class SanitizedString(object)
    def __init__(self, sanitizer)
    def __call__(self, thing)
    def __eq__(self, other)
def _sanitize_general(s)
def _sanitize_docstring(thing)
def doc()
def _sanitize_message(thing)
def msg()
def pytest_assertrepr_compare(op, left, right)
def suppress(exception)
def gc_collect()
def pytest_configure()
```

### raisimGymTorch/thirdParty/pybind11/tests/env.py

```
def deprecated_call()
```

### raisimGymTorch/thirdParty/pybind11/tests/extra_python_package/test_files.py

```
def test_build_sdist(monkeypatch, tmpdir)
def test_build_global_dist(monkeypatch, tmpdir)
def tests_build_wheel(monkeypatch, tmpdir)
def tests_build_global_wheel(monkeypatch, tmpdir)
```

### raisimGymTorch/thirdParty/pybind11/tests/extra_setuptools/test_setuphelper.py

```
def test_simple_setup_py(monkeypatch, tmpdir, parallel, std)
def test_intree_extensions(monkeypatch, tmpdir)
def test_intree_extensions_package_dir(monkeypatch, tmpdir)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_async.py

```
def event_loop()
def get_await_result(x)
def test_await(event_loop)
def test_await_missing(event_loop)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_buffers.py

```
def test_from_python()
def test_to_python()
def test_inherited_protocol()
def test_pointer_to_member_fn()
def test_readonly_buffer()
def test_selective_readonly_buffer()
def test_ctypes_array_1d()
def test_ctypes_array_2d()
def test_ctypes_from_buffer()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_builtin_casters.py

```
def test_simple_string()
def test_unicode_conversion()
def test_single_char_arguments()
def test_bytes_to_string()
def test_string_view(capture)
def test_integer_casting()
def test_int_convert()
def test_numpy_int_convert()
def test_tuple(doc)
def test_builtins_cast_return_none()
def test_none_deferred()
def test_void_caster()
def test_reference_wrapper()
def test_complex_cast()
def test_bool_caster()
def test_numpy_bool()
def test_int_long()
def test_void_caster_2()
def test_const_ref_caster()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_call_policies.py

```
def test_keep_alive_argument(capture)
def test_keep_alive_return_value(capture)
def test_alive_gc(capture)
def test_alive_gc_derived(capture)
def test_alive_gc_multi_derived(capture)
def test_return_none(capture)
def test_keep_alive_constructor(capture)
def test_call_guard()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_callbacks.py

```
def test_callbacks()
def test_bound_method_callback()
def test_keyword_args_and_generalized_unpacking()
def test_lambda_closure_cleanup()
def test_cpp_callable_cleanup()
def test_cpp_function_roundtrip()
def test_function_signatures(doc)
def test_movable_object()
def test_python_builtins()
def test_async_callbacks()
def test_async_async_callbacks()
def test_callback_num_times()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_chrono.py

```
def test_chrono_system_clock()
def test_chrono_system_clock_roundtrip()
def test_chrono_system_clock_roundtrip_date()
def test_chrono_system_clock_roundtrip_time(time1, tz, monkeypatch)
def test_chrono_duration_roundtrip()
def test_chrono_duration_subtraction_equivalence()
def test_chrono_duration_subtraction_equivalence_date()
def test_chrono_steady_clock()
def test_chrono_steady_clock_roundtrip()
def test_floating_point_duration()
def test_nano_timepoint()
def test_chrono_different_resolutions()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_class.py

```
def test_repr()
def test_instance(msg)
def test_instance_new(msg)
def test_type()
def test_type_of_py()
def test_type_of_classic()
def test_type_of_py_nodelete()
def test_as_type_py()
def test_docstrings(doc)
def test_qualname(doc)
def test_inheritance(msg)
def test_inheritance_init(msg)
def test_automatic_upcasting()
def test_isinstance()
def test_mismatched_holder()
def test_override_static()
def test_implicit_conversion_life_support()
def test_operator_new_delete(capture)
def test_bind_protected_functions()
def test_brace_initialization()
def test_class_refcount()
def test_reentrant_implicit_conversion_failure(msg)
def test_error_after_conversions()
def test_aligned()
def test_final()
def test_non_final_final()
def test_exception_rvalue_abort()
def test_multiple_instances_with_same_pointer(capture)
def test_base_and_derived_nested_scope()
def test_register_duplicate_class()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_const_name.py

```
def test_const_name(func, selector, expected)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_constants_and_functions.py

```
def test_constants()
def test_function_overloading()
def test_bytes()
def test_exception_specifiers()
def test_function_record_leaks()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_copy_move.py

```
def test_lacking_copy_ctor()
def test_lacking_move_ctor()
def test_move_and_copy_casts()
def test_move_and_copy_loads()
def test_move_and_copy_load_optional()
def test_private_op_new()
def test_move_fallback()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_custom_type_casters.py

```
def test_noconvert_args(msg)
def test_custom_caster_destruction()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_custom_type_setup.py

```
def gc_tester()
def test_self_cycle(gc_tester)
def test_indirect_cycle(gc_tester)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_docstring_options.py

```
def test_docstring_options()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_eigen.py

```
def assert_equal_ref(mat)
def assert_sparse_equal_ref(sparse_mat)
def test_fixed()
def test_dense()
def test_partially_fixed()
def test_mutator_descriptors()
def test_cpp_casting()
def test_pass_readonly_array()
def test_nonunit_stride_from_python()
def test_negative_stride_from_python(msg)
def test_nonunit_stride_to_python()
def test_eigen_ref_to_python()
def assign_both(a1, a2, r, c, v)
def array_copy_but_one(a, r, c, v)
def test_eigen_return_references()
def assert_keeps_alive(cl, method)
def test_eigen_keepalive()
def test_eigen_ref_mutators()
def test_numpy_ref_mutators()
def test_both_ref_mutators()
def test_nocopy_wrapper()
def test_eigen_ref_life_support()
def test_special_matrix_objects()
def test_dense_signature(doc)
def test_named_arguments()
def test_sparse()
def test_sparse_signature(doc)
def test_issue738()
def test_issue1105()
def test_custom_operator_new()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_embed/test_interpreter.py

```
class DerivedWidget(Widget)
    def __init__(self, message)
    def the_answer(self)
    def argv0(self)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_embed/test_trampoline.py

```
def func()
def func2()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_enum.py

```
def test_unscoped_enum()
def test_scoped_enum()
def test_implicit_conversion()
def test_binary_operators()
def test_enum_to_int()
def test_duplicate_enum_name()
def test_char_underlying_enum()
def test_bool_underlying_enum()
def test_docstring_signatures()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_eval.py

```
def test_evals(capture)
def test_eval_file()
def test_eval_empty_globals()
def test_eval_closure()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_exceptions.py

```
def test_std_exception(msg)
def test_error_already_set(msg)
def test_raise_from(msg)
def test_raise_from_already_set(msg)
def test_cross_module_exceptions(msg)
def test_cross_module_exception_translator()
def test_python_call_in_catch()
def ignore_pytest_unraisable_warning(f)
def test_python_alreadyset_in_destructor(monkeypatch, capsys)
def test_exception_matches()
def test_custom(msg)
def test_nested_throws(capture)
def test_invalid_repr()
def test_local_translator(msg)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_factory_constructors.py

```
def test_init_factory_basic()
def test_init_factory_signature(msg)
def test_init_factory_casting()
def test_init_factory_alias()
def test_init_factory_dual()
def test_no_placement_new(capture)
def test_multiple_inheritance()
def create_and_destroy()
def strip_comments(s)
def test_reallocation_a(capture, msg)
def test_reallocation_b(capture, msg)
def test_reallocation_c(capture, msg)
def test_reallocation_d(capture, msg)
def test_reallocation_e(capture, msg)
def test_reallocation_f(capture, msg)
def test_reallocation_g(capture, msg)
def test_invalid_self()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_gil_scoped.py

```
def _run_in_process(target)
def _python_to_cpp_to_python()
def _python_to_cpp_to_python_from_threads(num_threads, parallel)
def test_python_to_cpp_to_python_from_thread()
def test_python_to_cpp_to_python_from_thread_multiple_parallel()
def test_python_to_cpp_to_python_from_thread_multiple_sequential()
def test_python_to_cpp_to_python_from_process()
def test_cross_module_gil()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_iostream.py

```
def test_captured(capsys)
def test_captured_large_string(capsys)
def test_captured_utf8_2byte_offset0(capsys)
def test_captured_utf8_2byte_offset1(capsys)
def test_captured_utf8_3byte_offset0(capsys)
def test_captured_utf8_3byte_offset1(capsys)
def test_captured_utf8_3byte_offset2(capsys)
def test_captured_utf8_4byte_offset0(capsys)
def test_captured_utf8_4byte_offset1(capsys)
def test_captured_utf8_4byte_offset2(capsys)
def test_captured_utf8_4byte_offset3(capsys)
def test_guard_capture(capsys)
def test_series_captured(capture)
def test_flush(capfd)
def test_not_captured(capfd)
def test_err(capfd)
def test_multi_captured(capfd)
def test_dual(capsys)
def test_redirect(capfd)
def test_redirect_err(capfd)
def test_redirect_both(capfd)
def test_threading()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_kwargs_and_defaults.py

```
def test_function_signatures(doc)
def test_named_arguments(msg)
def test_arg_and_kwargs()
def test_mixed_args_and_kwargs(msg)
def test_keyword_only_args(msg)
def test_positional_only_args(msg)
def test_signatures()
def test_args_refcount()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_local_bindings.py

```
def test_load_external()
def test_local_bindings()
def test_nonlocal_failure()
def test_duplicate_local()
def test_stl_bind_local()
def test_stl_bind_global()
def test_mixed_local_global()
def test_internal_locals_differ()
def test_stl_caster_vs_stl_bind(msg)
def test_cross_module_calls()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_methods_and_attributes.py

```
def test_methods_and_attributes()
def test_copy_method()
def test_properties()
def test_static_properties()
def test_static_cls()
def test_metaclass_override()
def test_no_mixed_overloads()
def test_property_return_value_policies(access)
def test_property_rvalue_policy()
def test_dynamic_attributes()
def test_cyclic_gc()
def test_bad_arg_default(msg)
def test_accepts_none(msg)
def test_casts_none()
def test_str_issue(msg)
def test_unregistered_base_implementations()
def test_ref_qualified()
def test_overload_ordering()
def test_rvalue_ref_param()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_modules.py

```
def test_nested_modules()
def test_reference_internal()
def test_importing()
def test_pydoc()
def test_duplicate_registration()
def test_builtin_key_type()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_multiple_inheritance.py

```
def test_multiple_inheritance_cpp()
def test_multiple_inheritance_mix1()
def test_multiple_inheritance_mix2()
def test_multiple_inheritance_python()
def test_multiple_inheritance_python_many_bases()
def test_multiple_inheritance_virtbase()
def test_mi_static_properties()
def test_mi_dynamic_attributes()
def test_mi_unaligned_base()
def test_mi_base_return()
def test_diamond_inheritance()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_array.py

```
def test_dtypes()
def arr()
def test_array_attributes()
def test_index_offset(arr, args, ret)
def test_dim_check_fail(arr)
def test_data(arr, args, ret)
def test_at_fail(arr, dim)
def test_at(arr)
def test_mutate_readonly(arr)
def test_mutate_data(arr)
def test_bounds_check(arr)
def test_make_c_f_array()
def test_make_empty_shaped_array()
def test_wrap()
def test_numpy_view(capture)
def test_cast_numpy_int64_to_uint64()
def test_isinstance()
def test_constructors()
def test_overload_resolution(msg)
def test_greedy_string_overload()
def test_array_unchecked_fixed_dims(msg)
def test_array_unchecked_dyn_dims()
def test_array_failure()
def test_initializer_list()
def test_array_resize()
def test_array_create_and_resize()
def test_array_view()
def test_array_view_invalid()
def test_reshape_initializer_list()
def test_reshape_tuple()
def test_index_using_ellipsis()
def test_format_descriptors_for_floating_point_types(test_func)
def test_argument_conversions(forcecast, contiguity, noconvert)
def test_dtype_refcount_leak()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_dtypes.py

```
def simple_dtype()
def packed_dtype()
def dt_fmt()
def simple_dtype_fmt()
def packed_dtype_fmt()
def partial_ld_offset()
def partial_dtype_fmt()
def partial_nested_fmt()
def assert_equal(actual, expected_data, expected_dtype)
def test_format_descriptors()
def test_dtype(simple_dtype)
def test_recarray(simple_dtype, packed_dtype)
def test_array_constructors()
def test_string_array()
def test_array_array()
def test_enum_array()
def test_complex_array()
def test_signature(doc)
def test_scalar_conversion()
def test_vectorize()
def test_cls_and_dtype_conversion(simple_dtype)
def test_register_dtype()
def test_str_leak()
def test_compare_buffer_info()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_vectorize.py

```
def test_vectorize(capture)
def test_type_selection()
def test_docs(doc)
def test_trivial_broadcasting()
def test_passthrough_arguments(doc)
def test_method_vectorization()
def test_array_collapse()
def test_vectorized_noreturn()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_opaque_types.py

```
def test_string_list()
def test_pointers(msg)
def test_unions()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_operator_overloading.py

```
def test_operator_overloading()
def test_operators_notimplemented()
def test_nested()
def test_overriding_eq_reset_hash()
def test_return_set_of_unhashable()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_pickling.py

```
def test_roundtrip(cls_name)
def test_roundtrip_with_dict(cls_name)
def test_enum_pickle()
class SimplePyDerived(SimpleBase)
def test_roundtrip_simple_py_derived()
def test_roundtrip_simple_cpp_derived()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_pytypes.py

```
def test_int(doc)
def test_iterator(doc)
def test_iterable(doc)
def test_list(capture, doc)
def test_none(capture, doc)
def test_set(capture, doc)
def test_dict(capture, doc)
def test_tuple()
def test_simple_namespace()
def test_str(doc)
def test_bytes(doc)
def test_bytearray(doc)
def test_capsule(capture)
def test_accessors()
def test_constructors()
def test_non_converting_constructors()
def test_pybind11_str_raw_str()
def test_implicit_casting()
def test_print(capture)
def test_hash()
def test_number_protocol()
def test_list_slicing()
def test_issue2361()
def test_memoryview(method, args, fmt, expected_view)
def test_memoryview_refcount(method)
def test_memoryview_from_buffer_empty_shape()
def test_test_memoryview_from_buffer_invalid_strides()
def test_test_memoryview_from_buffer_nullptr()
def test_memoryview_from_memory()
def test_builtin_functions()
def test_isinstance_string_types()
def test_pass_bytes_or_unicode_to_string_types()
def test_weakref(create_weakref, create_weakref_with_callback)
def test_cpp_iterators()
def test_implementation_details()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_sequences_and_iterators.py

```
def isclose(a, b, rel_tol, abs_tol)
def allclose(a_list, b_list, rel_tol, abs_tol)
def test_slice_constructors()
def test_slice_constructors_explicit_optional()
def test_generalized_iterators()
def test_nonref_iterators()
def test_generalized_iterators_simple()
def test_iterator_referencing()
def test_sliceable()
def test_sequence()
def test_sequence_length()
def test_map_iterator()
def test_python_iterator_in_cpp()
def test_iterator_passthrough()
def test_iterator_rvp()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_smart_ptr.py

```
def test_smart_ptr(capture)
def test_smart_ptr_refcounting()
def test_unique_nodelete()
def test_unique_nodelete4a()
def test_unique_deleter()
def test_large_holder()
def test_shared_ptr_and_references()
def test_shared_ptr_from_this_and_references()
def test_move_only_holder()
def test_holder_with_addressof_operator()
def test_move_only_holder_with_addressof_operator()
def test_smart_ptr_from_default()
def test_shared_ptr_gc()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_stl.py

```
def test_vector(doc)
def test_deque(doc)
def test_array(doc)
def test_valarray(doc)
def test_map(doc)
def test_set(doc)
def test_recursive_casting()
def test_move_out_container()
def test_optional()
def test_exp_optional()
def test_boost_optional()
def test_reference_sensitive_optional()
def test_fs_path()
def test_variant(doc)
def test_vec_of_reference_wrapper()
def test_stl_pass_by_pointer(msg)
def test_missing_header_message()
def test_function_with_string_and_vector_string_arg()
def test_stl_ownership()
def test_array_cast_sequence()
def test_issue_1561()
def test_return_vector_bool_raw_ptr()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_stl_binders.py

```
def test_vector_int()
def test_vector_buffer()
def test_vector_buffer_numpy()
def test_vector_bool()
def test_vector_custom()
def test_map_string_double()
def test_map_string_double_const()
def test_noncopyable_containers()
def test_map_delitem()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_tagbased_polymorphic.py

```
def test_downcast()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_thread.py

```
class Thread(Thread)
    def __init__(self, fn)
    def run(self)
    def join(self)
def test_implicit_conversion()
def test_implicit_conversion_no_gil()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_union.py

```
def test_union()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_virtual_functions.py

```
def test_override(capture, msg)
def test_alias_delay_initialization1(capture)
def test_alias_delay_initialization2(capture)
def test_move_support()
def test_dispatch_issue(msg)
def test_recursive_dispatch_issue(msg)
def test_override_ref()
def test_inherited_virtuals()
def test_issue_1454()
def test_python_override()
```

### thirdParty/pybind11/tests/env.py

```
def deprecated_call()
```