# newton_2025

source: https://github.com/newton-physics/newton


commit: ecc03b490d6a15ecff7d5e8870f4d67f97c98631


## README

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/newton-physics/newton/main)
[![codecov](https://codecov.io/gh/newton-physics/newton/graph/badge.svg?token=V6ZXNPAWVG)](https://codecov.io/gh/newton-physics/newton)
[![Push - AWS GPU](https://github.com/newton-physics/newton/actions/workflows/push_aws_gpu.yml/badge.svg)](https://github.com/newton-physics/newton/actions/workflows/push_aws_gpu.yml)

# Newton

Newton is a GPU-accelerated physics simulation engine built upon [NVIDIA Warp](https://github.com/NVIDIA/warp), specifically targeting roboticists and simulation researchers.

Newton extends and generalizes Warp's ([deprecated](https://github.com/NVIDIA/warp/discussions/735)) `warp.sim` module, and integrates
[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp) as its primary backend. Newton emphasizes GPU-based computation, [OpenUSD](https://openusd.org/) support, differentiability, and user-defined extensibility, facilitating rapid iteration and scalable robotics simulation.

Newton is a [Linux Foundation](https://www.linuxfoundation.org/) project that is community-built and maintained. Code is licensed under [Apache-2.0](https://github.com/newton-physics/newton/blob/main/LICENSE.md). Documentation is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Additional and third-party license texts are available in [`newton/licenses`](https://github.com/newton-physics/newton/tree/main/newton/licenses).

Newton was initiated by [Disney Research](https://www.disneyresearch.com/), [Google DeepMind](https://deepmind.google/), and [NVIDIA](https://www.nvidia.com/).

## Requirements

- **Python** 3.10+
- **OS:** Linux (x86-64, aarch64), Windows (x86-64), or macOS (CPU only)
- **GPU:** NVIDIA GPU (Maxwell or newer), driver 545 or newer (CUDA 12). No local CUDA Toolkit installation required. macOS runs on CPU.

For detailed system requirements, see the [installation guide](https://newton-physics.github.io/newton/latest/guide/installation.html). For tested configurations and Newton's versioning and deprecation policies, see the [compatibility guide](https://newton-physics.github.io/newton/latest/guide/compatibility.html).

## Quickstart

```bash
pip install "newton[examples]"
python -m newton.examples
```

To install from source with [uv](https://docs.astral.sh/uv/), see the [installation guide](https://newton-physics.github.io/newton/latest/guide/installation.html).

## Examples

Before running the examples below, install Newton with the examples extra:

```bash
pip install "newton[examples]"
```

If you run the examples from a source checkout with uv, use
`uv run --extra examples -m newton.examples <example_name>` instead of the
`python -m newton.examples <example_name>` commands below.

<table>
  <tr>
    <td colspan="3"><h3>Basic Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_pendulum.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_pendulum.jpg" alt="Pendulum">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_urdf.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_urdf.jpg" alt="URDF">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_viewer.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_viewer.jpg" alt="Viewer">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_pendulum</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_urdf</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_viewer</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_shapes.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_shapes.jpg" alt="Shapes">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_joints.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_joints.jpg" alt="Joints">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_conveyor.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_conveyor.jpg" alt="Conveyor">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_shapes</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_joints</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_conveyor</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_heightfield.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_heightfield.jpg" alt="Heightfield">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_recording.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_recording.jpg" alt="Recording">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_replay_viewer.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_replay_viewer.jpg" alt="Replay Viewer">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_heightfield</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples recording</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples replay_viewer</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_plotting.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_plotting.jpg" alt="Plotting">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_dzhanibekov.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_dzhanibekov.jpg" alt="Dzhanibekov">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_conveyor_forces.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_conveyor_forces.jpg" alt="Conveyor Forces">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_plotting</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_dzhanibekov</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_conveyor_forces</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/basic/example_basic_mimic_joint.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_basic_mimic_joint.jpg" alt="Mimic Joint">
      </a>
    </td>
    <td width="33%"></td>
    <td width="33%"></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples basic_mimic_joint</code>
    </td>
    <td width="33%"></td>
    <td width="33%"></td>
  </tr>
  <tr>
    <td colspan="3"><h3>Robot Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_cartpole.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_cartpole.jpg" alt="Cartpole">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_g1.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_g1.jpg" alt="G1">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_h1.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_h1.jpg" alt="H1">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_cartpole</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_g1</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_h1</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_anymal_d.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_anymal_d.jpg" alt="Anymal D">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_anymal_c_walk.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_anymal_c_walk.jpg" alt="Anymal C Walk">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_policy.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_policy.jpg" alt="Policy">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_anymal_d</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_anymal_c_walk</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_policy</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_ur10.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_ur10.jpg" alt="UR10">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_panda_hydro.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_panda_hydro.jpg" alt="Panda Hydro">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_allegro_hand.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_allegro_hand.jpg" alt="Allegro Hand">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_ur10</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_panda_hydro</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_allegro_hand</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_omniwheel.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_omniwheel.jpg" alt="Omniwheel">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/robot/example_robot_asroballet.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_robot_asroballet.jpg" alt="asRoBallet">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_omniwheel</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples robot_asroballet</code>
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Controller Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/controllers/example_controller_joint_impedance_heterogeneous.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_controller_joint_impedance_heterogeneous.jpg" alt="Joint Impedance Heterogeneous">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/controllers/example_controller_operational_space_hybrid_force_motion.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_controller_operational_space_hybrid_force_motion.jpg" alt="Operational Space Hybrid Force/Motion">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/controllers/example_controller_differential_ik.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_controller_differential_ik.jpg" alt="Differential IK">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples controller_joint_impedance_heterogeneous</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples controller_operational_space_hybrid_force_motion</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples controller_differential_ik</code>
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Cable Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_twist.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_twist.jpg" alt="Cable Twist">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_y_junction.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_y_junction.jpg" alt="Cable Y-Junction">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_bundle_hysteresis.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_bundle_hysteresis.jpg" alt="Cable Bundle Hysteresis">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_twist</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_y_junction</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_bundle_hysteresis</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_pile.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_pile.jpg" alt="Cable Pile">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_cross_slide_table.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_cross_slide_table.jpg" alt="Cable Cross Slide Table">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cable/example_cable_plectoneme.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cable_plectoneme.jpg" alt="Cable Plectoneme">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_pile</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_cross_slide_table</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cable_plectoneme</code>
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Cloth Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_bending.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_bending.jpg" alt="Cloth Bending">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_hanging.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_hanging.jpg" alt="Cloth Hanging">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_style3d.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_style3d.jpg" alt="Cloth Style3D">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_bending</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_hanging</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_style3d</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_h1.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_h1.jpg" alt="Cloth H1">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_twist.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_twist.jpg" alt="Cloth Twist">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_franka.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_franka.jpg" alt="Cloth Franka">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_h1</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_twist</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_franka</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_rollers.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_rollers.jpg" alt="Cloth Rollers">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/cloth/example_cloth_poker_cards.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_cloth_poker_cards.jpg" alt="Cloth Poker Cards">
      </a>
    </td>
    <td align="center" width="33%">
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_rollers</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples cloth_poker_cards</code>
    </td>
    <td align="center" width="33%">
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Inverse Kinematics Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/ik/example_ik_franka.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_ik_franka.jpg" alt="IK Franka">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/ik/example_ik_h1.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_ik_h1.jpg" alt="IK H1">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/ik/example_ik_custom.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_ik_custom.jpg" alt="IK Custom">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples ik_franka</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples ik_h1</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples ik_custom</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/ik/example_ik_cube_stacking.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_ik_cube_stacking.jpg" alt="IK Cube Stacking">
      </a>
    </td>
    <td align="center" width="33%">
    </td>
    <td align="center" width="33%">
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples ik_cube_stacking</code>
    </td>
    <td align="center" width="33%">
    </td>
    <td align="center" width="33%">
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>MPM Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_granular.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_granular.jpg" alt="MPM Granular">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_anymal.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_anymal.jpg" alt="MPM Anymal">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_twoway_coupling.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_twoway_coupling.jpg" alt="MPM Two-Way Coupling">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_granular</code><br>
      <code>python -m newton.examples mpm_granular --from-usd</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_anymal</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_twoway_coupling</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_grain_rendering.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_grain_rendering.jpg" alt="MPM Grain Rendering">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_multi_material.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_multi_material.jpg" alt="MPM Multi Material">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_viscous.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_viscous.jpg" alt="MPM Viscous">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_grain_rendering</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_multi_material</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_viscous</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_beam_twist.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_beam_twist.jpg" alt="MPM Beam Twist">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_snow_ball.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_snow_ball.jpg" alt="MPM Snow Ball">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/mpm/example_mpm_water_dam_break.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_mpm_water_dam_break.jpg" alt="MPM Water Dam Break">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_beam_twist</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_snow_ball</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples mpm_water_dam_break</code>
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Sensor Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/sensors/example_sensor_contact.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_sensor_contact.jpg" alt="Sensor Contact">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/sensors/example_sensor_tiled_camera.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_sensor_tiled_camera.jpg" alt="Sensor Tiled Camera">
      </a>
    </td>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/sensors/example_sensor_imu.py">
        <img width="320" src="https://raw.githubusercontent.com/newton-physics/newton/main/docs/images/examples/example_sensor_imu.jpg" alt="Sensor IMU">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <code>python -m newton.examples sensor_contact</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples sensor_tiled_camera</code>
    </td>
    <td align="center" width="33%">
      <code>python -m newton.examples sensor_imu</code>
    </td>
  </tr>
  <tr>
    <td colspan="3"><h3>Selection Examples</h3></td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="https://github.com/newton-physics/newton/blob/main/newton/examples/selection/example_selection_cartpole.py">
        <img width="3

## File tree (depth 3, assets pruned)

```
.claude/
  skills/
    code-review-newton/
    release-audit/
    release-changelog/
    release-notes/
.coderabbit.yml
.gitattributes
.github/
  CODEOWNERS
  ISSUE_TEMPLATE/
    1-bug-report.yml
    2-feature-request.yml
    3-documentation.yml
    config.yml
  PULL_REQUEST_TEMPLATE.md
  codecov.yml
  workflows/
    aws_gpu_benchmarks.yml
    aws_gpu_tests.yml
    changelog-preview.yml
    ci.yml
    docs-dev.yml
    docs-release.yml
    merge_queue_aws_gpu.yml
    minimum_deps_tests.yml
    pr.yml
    pr_api_changes.yml
    pr_auto_assign_creator.yml
    pr_license_check.yml
    pr_target_aws_gpu_benchmarks.yml
    pr_target_aws_gpu_tests.yml
    push_aws_gpu.yml
    release.yml
    scheduled_nightly.yml
    warp_nightly_tests.yml
.gitignore
.licenserc-docs.yaml
.licenserc.yaml
.pre-commit-config.yaml
.python-version
AGENTS.md
CHANGELOG.md
CITATION.cff
CLAUDE.md
CODE_OF_CONDUCT.md
CODING_GUIDELINES.rst
CONTRIBUTING.md
LICENSE.md
README.md
REVIEW_GUIDELINES.rst
SECURITY.md
asv/
  benchmarks/
    __init__.py
    benchmark_config.py
    benchmark_ik.py
    benchmark_inverse_dynamics.py
    benchmark_kamino.py
    benchmark_metric_tracks.py
    benchmark_metrics.py
    benchmark_mujoco.py
    compilation/
    setup/
    simulation/
  pr_benchmarks.txt
  run_pr_benchmarks.py
  tests/
    __init__.py
    test_benchmark_metrics.py
    test_benchmark_simulation.py
asv.conf.json
changelog/
  +array-backed-builder-3b7f1c9d.changed.md
  +dat-relaxation-alias-9d2f6a1c.deprecated.md
  +deformable-collision-block-size-6f2a9c1d.changed.md
  +joint-mimic-metadata-8e61c4a2.added.md
  +joint-mimic-metadata-8e61c4a2.deprecated.md
  +kamino-dvi-schur-4125.added.md
  +kamino-type-error-008d8f13.fixed.md
  +mjcf-explicit-small-mass-9c3a2f.fixed.md
  +model-collision-filters-2f6c8a1d.removed.md
  +mujoco-cone-mesh-6168.added.md
  +mujoco-joint-reference-7c4e2a91.changed.md
  +mujoco-joint-reference-7c4e2a91.fixed.md
  +rigid-soft-dat-3f9a2c71.added.md
  +rigid-soft-log-barrier-7c1e5d90.added.md
  +sdf-contact-performance-4d1c8e27.changed.md
  +soft-self-dat-epsilon-4b8d6e23.changed.md
  +usd-2608-deps-6496f7a7.changed.md
  +usd-cable-attachment-articulation-4e9a7c2d.fixed.md
  +usd-thread-limit-61ecfa23.changed.md
  +vbd-post-init-detection-particle-state-5b7c19d3.fixed.md
  +vbd-self-contact-schedule-none-8e2d47b1.changed.md
  3764.fixed.md
  3774.fixed.md
  3934.added.md
  4046.added.md
  4109.fixed.md
  4141.changed.1.md
  4141.changed.md
  4145.fixed.md
  4217.fixed.md
  4220.fixed.md
  4221.fixed.md
  README.md
newton/
  __init__.py
  _src/
    actuators/
    controllers/
    core/
    geometry/
    math/
    sensors/
    sim/
    solvers/
    usd/
    utils/
    viewer/
  _version.py
  actuators.py
  controllers.py
  examples/
    __init__.py
    __main__.py
    basic/
    cable/
    cloth/
    contacts/
    controllers/
    diffsim/
    ik/
    kamino/
    mpm/
    mujoco/
    multiphysics/
    robot/
    selection/
    sensors/
    softbody/
    vbd/
  geometry.py
  ik.py
  licenses/
    CC-BY-4.0.txt
    unittest-parallel-LICENSE.txt
    viser_and_inter-font-family.txt
  math.py
  py.typed
  selection.py
  sensors.py
  solvers.py
  tests/
    __init__.py
    __main__.py
    _usd_deformable_test_utils.py
    determinism/
    golden_data/
    kamino/
    test_actuator_drive_api.py
    test_actuators.py
    test_admm_coupled_solver.py
    test_anymal_reset.py
    test_api.py
    test_body_force.py
    test_body_velocity.py
    test_broad_phase.py
    test_builder_replicate.py
    test_bvh.py
    test_cable.py
    test_cloth.py
    test_collision_cloth.py
    test_collision_mask_compiler.py
    test_collision_pipeline.py
    test_collision_plane_halfspace_aabb.py
    test_collision_primitives.py
    test_coloring.py
    test_cone_orientation.py
    test_contact_matching.py
    test_contact_reduction.py
    test_contact_reduction_global.py
    test_control_force.py
    test_controllers_differential_ik.py
    test_controllers_joint_impedance.py
    test_controllers_joint_selection.py
    test_controllers_one_sided_jacobi_svd_solver.py
    test_controllers_operational_space.py
    test_convex_support.py
    test_conveyor_forces.py
    test_coupled_solver.py
    test_custom_attributes.py
    test_custom_solver.py
    test_differentiable_contacts.py
    test_download_assets.py
    test_edge_redundancy.py
    test_environment_group_collision.py
    test_equality_connect_constraint_with_sim_step.py
    test_equality_constraints.py
    test_eval_fk.py
    test_example_browser.py
    test_example_browser_args.py
    test_examples.py
    test_fixed_tendon.py
    test_generate_api.py
    test_gjk.py
    test_hashtable.py
    test_heightfield.py
    test_hydroelastic.py
    test_ik.py
    test_ik_fk_kernels.py
    test_ik_lbfgs.py
    test_implicit_mpm.py
    test_implicit_mpm_flow_rule.py
    test_implicit_mpm_multiworld_sparse.py
    test_implicit_mpm_rebuildable_sparse.py
    test_import_mjcf.py
    test_import_urdf.py
    test_import_usd.py
    test_import_usd_collision_groups.py
    test_import_usd_deformable_attachments.py
    test_import_usd_deformable_cable.py
    test_import_usd_deformable_cloth.py
    test_import_usd_deformable_filtered_pairs.py
    test_import_usd_deformable_groups.py
    test_import_usd_deformable_mixed.py
    test_import_usd_deformable_volume.py
    test_import_usd_mpm.py
    test_import_usd_multi_dof.py
    test_inertia.py
    test_inertia_validation.py
    test_inverse_dynamics.py
    test_jacobian_mass_matrix.py
    test_joint_controllers.py
    test_joint_damping.py
    test_joint_drive.py
    test_joint_limits.py
    test_kinematic_links.py
    test_kinematics.py
    test_lazy_imports.py
    test_lazy_init.py
    test_match_labels.py
    test_menagerie_mujoco.py
    test_menagerie_usd_mujoco.py
    test_mesh_aabb.py
    test_mesh_backface.py
    test_mesh_cache.py
    test_mesh_edge_angle_filter.py
    test_mesh_utils.py
    test_mesh_validation.py
    test_model.py
    test_mpr.py
    test_mujoco_fk_consistency.py
    test_mujoco_general_actuators.py
    test_mujoco_margin_zeroing.py
    test_mujoco_reset.py
    test_mujoco_sleeping.py
    test_mujoco_solver.py
    test_mujoco_version_check.py
    test_multiworld_body_properties.py
    test_narrow_phase.py
    test_negative_scaling.py
    test_obb.py
    test_off_origin_convex_hull_contacts.py
    test_parent_force.py
    test_particle_surface.py
    test_pendulum_revolute_vs_d6.py
    test_physics_verification.py
    test_python_compatibility.py
    test_raycast.py
    test_recorder.py
    test_remesh.py
    test_remesh_convex_hull.py
    test_render_fps_cli.py
    test_rigid_contact.py
    test_rigid_friction_ramp.py
    test_robot_composer.py
    test_run_benchmark.py
    test_runtime_gravity.py
    test_schema_resolver.py
    test_sdf_compute.py
    test_sdf_contact.py
    test_sdf_disk_cache.py
    test_sdf_primitive.py
    test_sdf_texture.py
    test_sdf_usd.py
    test_selection.py
    test_sensor_contact.py
    test_sensor_frame_transform.py
    test_sensor_imu.py
    test_sensor_tiled_camera.py
    test_sensor_tiled_camera_forward_depth.py
    test_sensor_tiled_camera_hdr_color.py
    test_sensor_tiled_camera_heightfield.py
    test_sensor_tiled_camera_particles_multiworld.py
    test_sensor_to_rgba.py
    test_sensor_usd_camera.py
    test_shape_colors.py
    test_shapes_no_bounce.py
    test_sites.py
    test_sites_mjcf_import.py
    test_sites_mujoco_export.py
    test_sites_usd_import.py
    test_softbody.py
    test_softbody_simulation.py
    test_solver_collision_frequency.py
    test_solver_mimic.py
    test_solver_mujoco_planar_mesh.py
    test_solver_style3d.py
    test_solver_vbd.py
    test_solver_vbd_proxy_full_surface.py
    test_solver_xpbd.py
    test_solver_xpbd_tetrahedra.py
    test_spatial_tendon.py
    test_speculative_contacts.py
    test_state_assign.py
    test_terrain_generator.py
    test_texture.py
    test_tolerance_clamping.py
    test_unittest_utils.py
    test_up_axis.py
    test_usd_mesh_loading.py
    test_vbd_interval_arithmetic.py
    test_viewer_camera.py
    test_viewer_controls.py
    test_viewer_geometry_batching.py
    test_viewer_get_frame.py
    test_viewer_image_logger.py
    test_viewer_image_logger_class.py
    test_viewer_layers.py
    test_viewer_loading_splash.py
    test_viewer_log_shapes.py
    test_viewer_particle_flags.py
    test_viewer_picking.py
    test_viewer_plotting.py
    test_viewer_rerun_hidden.py
    test_viewer_rerun_init_args.py
    test_viewer_usd.py
    test_viewer_viser.py
    test_viewer_visible_worlds.py
    test_viewer_world_offsets.py
    test_warp_config_cli.py
    thirdparty/
    unittest_utils.py
    utils/
  usd.py
  utils.py
  viewer.py
pyproject.toml
scripts/
  check_warp_array_syntax.py
  ci/
    aws/
    detect_api_changes.py
    discover_aws_runner_config.py
    dispatch_workflow_and_wait.py
    tests/
    update_docs_switcher.py
uv.lock
```

## Config files (2)


### .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: true
contact_links:
  - name: Question
    url: https://github.com/newton-physics/newton/discussions
    about: Ask questions about Newton in GitHub Discussions.

```

### .pre-commit-config.yaml

```yaml
ci:
  autofix_commit_msg: |
    [pre-commit.ci] auto code formatting
  autofix_prs: false
  autoupdate_branch: ""
  autoupdate_commit_msg: "[pre-commit.ci] pre-commit autoupdate"
  autoupdate_schedule: quarterly
  # pre-commit.ci has no network access, but uv-lock needs to resolve
  # dependencies from remote indexes (PyPI, nvidia, pytorch).
  # Lockfile freshness is checked by a separate CI workflow instead.
  skip:
    - uv-lock
  submodules: false

# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: check-case-conflict
      - id: check-illegal-windows-names
      - id: check-json
      - id: check-merge-conflict
      - id: check-symlinks
      - id: check-toml
      - id: check-yaml
      - id: debug-statements
      - id: detect-private-key
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.15.20
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix] # Apply fixes to resolve lint violations.
      # Run the formatter.
      - id: ruff-format
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.26
    hooks:
      # Update the uv lockfile
      - id: uv-lock
  - repo: https://github.com/crate-ci/typos
    rev: v1.48.0
    hooks:
      - id: typos
        args: []
        exclude: \.(js|css)$
  - repo: local
    hooks:
      - id: check-warp-array-syntax
        name: check warp array syntax
        entry: python scripts/check_warp_array_syntax.py
        language: python
        types: [python]
        exclude: ^(scripts/check_warp_array_syntax\.py)

```

## Python signatures and reward/observation bodies (75 files)


### asv/benchmarks/benchmark_config.py

```
def pr_gate_repeat(default, pr_repeat)
```

### asv/benchmarks/simulation/bench_anymal.py

```
def _create_example(num_frames)
def _validate_workload(workload)
class FastExampleAnymalPretrained()
    def setup(self)
    def time_simulate(self)
class FastMetricsExampleAnymalPretrained(_SimulationMetricTracksUnparameterized)
    def setup_cache(self)
```

### asv/benchmarks/simulation/bench_cable.py

```
def _supports_cable_pile_size_args()
class FastExampleCablePile()
    def setup(self)
    def time_simulate(self)
```

### asv/benchmarks/simulation/bench_cloth.py

```
def _make_collision_grid(resolution, height)
def _make_collision_world(resolution)
class FastDeformableSelfCollision()
    """Benchmark self-collision detection in one large cloth and many replicated worlds."""
    def setup(self, case)
    def _detect(self)
    def time_detect(self, case)
class FastExampleClothManipulation()
    def setup(self)
    def time_simulate(self)
class FastExampleClothTwist()
    def setup(self)
    def time_simulate(self)
```

### asv/benchmarks/simulation/bench_contacts.py

```
def _import_example_class(module_names)
def _make_irregular_rock(vertex_count, seed, triangle_local_vertices)
def _add_mixed_convex_shape(builder, body, shape_kind, rocks, rock_index, cfg)
def _build_convex_scene(world_count, pair_types)
def _build_single_world_scene(pair_count)
def _make_two_sided_grid(resolution, half_extent)
def _build_mesh_convex_scene(world_count, resolution)
def _build_mesh_sdf_scene(world_count, device)
class FastExampleContactSdfDefaults()
    """Benchmark the SDF nut-bolt example default configuration."""
    def setup_cache(self)
    def setup(self)
    def time_simulate(self)
class FastExampleContactHydroWorkingDefaults()
    """Benchmark the hydroelastic nut-bolt example default configuration."""
    def setup_cache(self)
    def setup(self)
    def time_simulate(self)
class _ExampleCollideBenchmark()
    """Collision-only timing of an example scene sized so contact generation dominates.

The ``*Defaults`` benchmarks time whole simulation frames, where the solver
hides most of the collision cost. This base class builds the same example
with more worlds, captures ``CollisionPipeline.collide`` alone into """
    def setup_cache(self)
    def setup(self)
    def time_collide(self)
class FastExampleContactSdfCollide(_ExampleCollideBenchmark)
    """Collision-only benchmark of the mesh-SDF nut-bolt scene at 200 worlds."""
class FastExampleContactHydroCollide(_ExampleCollideBenchmark)
    """Collision-only benchmark of the hydroelastic nut-bolt scene at 200 worlds."""
class FastExampleContactPyramidDefaults()
    """Benchmark the box pyramid example with default configuration."""
    def setup(self)
    def time_simulate(self)
class FastConvexCollision()
    """Benchmark lean-hull and mixed-type convex collision workloads."""
    def setup(self, case)
    def time_collide(self, case)
class BroadPhaseCollision()
    """Benchmark sparse contacts through every rigid broad phase."""
    def setup(self, case)
    def time_collide(self, case)
class ComplexContactCollision()
    """Benchmark dense mesh-convex manifolds and regular mesh-SDF contacts."""
    def setup(self, case)
    def time_collide(self, case)
```

### asv/benchmarks/simulation/bench_cpu.py

```
"""CPU regression benchmarks.

Minimal but broad coverage of Newton's CPU codepath, intended to catch
regressions in the Warp CPU backend (issue #2830). Each benchmark exercises
a different subsystem and runs within ``wp.ScopedDevice("cpu")`` so it
executes without a GPU."""
class CpuMuJoCoAnt()
    """MuJoCo (Warp CPU) ant — exercises mujoco_warp + Newton glue with contacts and constraints."""
    def setup(self)
    def time_simulate(self)
class CpuXPBDQuadruped()
    """XPBD rigid-body quadruped — exercises XPBD solver, contacts, articulations."""
    def setup(self)
    def time_simulate(self)
class CpuIKFranka()
    """IK on a Franka arm — exercises the IK solver and Jacobian path."""
    def setup(self)
    def time_solve(self)
```

### asv/benchmarks/simulation/bench_heightfield.py

```
def _build_heightfield_scene(num_bodies, nrow, ncol)
class HeightfieldCollision()
    """Benchmark heightfield collision with many spheres on a 100x100 grid."""
    def setup(self)
    def time_simulate(self)
```

### asv/benchmarks/simulation/bench_ik.py

```
class _IKBenchmark()
    """Utility base class for IK benchmarks."""
    def setup(self, batch_size)
    def time_solve(self, batch_size)
    def teardown(self, batch_size)
class FastIKSolve(_IKBenchmark)
```

### asv/benchmarks/simulation/bench_implicit_mpm.py

```
class ImplicitMPMSingleWorld()
    """Track the fixed-grid single-world fast path independently of batching."""
    def setup(self)
    def time_step(self)
```

### asv/benchmarks/simulation/bench_inverse_dynamics.py

```
class _InverseDynamicsBenchmark()
    """Utility base class for inverse-dynamics benchmarks."""
    def setup(self)
    def time_eval_inverse_dynamics_passive(self)
    def time_eval_inverse_dynamics_force(self)
    def teardown(self)
class FastInverseDynamics(_InverseDynamicsBenchmark)
    """Time ``eval_inverse_dynamics_passive`` and
``eval_inverse_dynamics_force`` on a model replicating the Franka arm
across ``WORLD_COUNT`` worlds (default 1024)."""
```

### asv/benchmarks/simulation/bench_kamino.py

```
def _collect_metrics_dr_legs(robot, world_count, num_frames, samples, use_policy)
class _FastBenchmark()
    """Utility base class for fast Kamino benchmarks."""
    def setup(self)
    def teardown(self)
    def time_simulate(self)
class _KpiBenchmark(_SimulationMetricTracks)
    """Utility base class for Kamino KPI benchmarks."""
    def _collect_metrics(self)
class FastDRLegs(_FastBenchmark)
class FastMetricsDRLegs(_SimulationMetricTracksUnparameterized)
    def setup_cache(self)
class KpiDRLegs(_KpiBenchmark)
    def setup_cache(self)
class NotifyDRLegs()
    """Benchmark Kamino model notifications for 2048 DR Legs worlds."""
    def setup(self)
    def time_notify_actuator_properties(self)
    def time_notify_all(self)
    def time_notify_body_inertial_properties(self)
    def time_notify_body_properties(self)
    def time_notify_joint_dof_properties(self)
    def time_notify_joint_properties(self)
    def time_notify_model_properties(self)
    def time_notify_shape_properties(self)
    def _notify(self, flag)
```

### asv/benchmarks/simulation/bench_mujoco.py

```
class _SimulationMetricTracksMuJoCo(_SimulationMetricTracks)
    """MuJoCo-specific tracked metrics."""
    def track_solver_niter_mean(self, metrics, world_count)
    def track_solver_niter_max(self, metrics, world_count)
class _KpiBenchmark(_SimulationMetricTracksMuJoCo)
    """Utility base class for KPI benchmarks."""
    def _create_workload(self, builder, world_count)
    def _validate_workload(self, workload, world_count)
    def _validate_metrics_workload(self, workload, world_count, solver_niter_samples)
    def _collect_metrics(self)
class _RealtimePhysicsBenchmark()
    """Report single-world physics throughput, stability, and real-time factor."""
    def setup(self)
    def track_mean_step_ms(self)
    def track_p95_step_ms(self)
    def track_step_rate_hz(self)
    def track_step_time_cv_pct(self)
    def track_real_time_factor(self)
    def _measure_step_durations(self)
    def _mean(values)
class _NewtonOverheadBenchmark()
    """Utility base class for measuring Newton overhead."""
    def setup(self, world_count)
    def track_simulate(self, world_count)
class FastCartpole(_KpiBenchmark)
    def setup_cache(self)
class FastG1(_KpiBenchmark)
    def setup_cache(self)
class FastNewtonOverheadG1(_NewtonOverheadBenchmark)
class FastHumanoid(_KpiBenchmark)
    def setup_cache(self)
class RealtimeHumanoidPhysics(_RealtimePhysicsBenchmark)
    """Single highly articulated humanoid in physics-only mode."""
class FastNewtonOverheadHumanoid(_NewtonOverheadBenchmark)
class FastAllegro(_KpiBenchmark)
    def setup_cache(self)
class FastKitchenG1(_KpiBenchmark)
    def setup_cache(self)
```

### asv/benchmarks/simulation/bench_quadruped_xpbd.py

```
def _create_example(num_frames, world_count)
class FastExampleQuadrupedXPBD()
    def setup(self)
    def time_simulate(self)
class FastMetricsExampleQuadrupedXPBD(_SimulationMetricTracksUnparameterized)
    def setup_cache(self)
```

### asv/benchmarks/simulation/bench_selection.py

```
class FastExampleSelectionCartpoleMuJoCo()
    def setup(self)
    def time_simulate(self)
```

### asv/benchmarks/simulation/bench_sensor_tiled_camera.py

```
"""Rendering benchmarks for the tiled camera sensor.

``FastSensorTiledCamera`` and ``FastSensorTiledCameraPixel`` measure Isaac
Lab's Franka cabinet scene with tiled and pixel-priority rendering in CI. The
other scene benchmarks cover varying visual complexity and are intended for
hill-climbing renderer performance:

- ``franka_cabinet``: Isaac Lab's Franka cabinet (open-drawer) scene.
- ``quadruped``: an ANYmal D quadruped in its nominal standing pose.
- ``shapes_256``: a grid of 256 primitive shapes.

Each scene is described once as a :class:`ScenePreset` in :data:`SCENES` and is
shared betwee"""
def _set_joint_positions(builder, joint_positions)
def _disable_collision_handling(builder)
def _build_quadruped()
def _build_franka_cabinet()
def _build_shapes_256()
class ScenePreset()
    """A benchmark scene: one world's worth of content plus a camera pose."""
def _look_at_transform(eye, target, up)
class _TiledCameraSceneRig()
    """A scene replicated across worlds with a tiled camera sensor ready to render."""
    def __init__(self, preset, world_count, resolution, render_order, camera_fov_deg)
    def render(self, color, depth)
def _pr_gate_skips_output(color, depth, selected_modes)
class _SceneBenchmark()
    """Shared ASV harness; subclasses pick a scene from :data:`SCENES` and their params."""
    def setup(self, resolution, world_count, iterations)
    def time_render_color_depth(self, resolution, world_count, iterations)
    def time_render_color_only(self, resolution, world_count, iterations)
    def time_render_depth_only(self, resolution, world_count, iterations)
class TiledCameraQuadruped(_SceneBenchmark)
class FastSensorTiledCamera(_SceneBenchmark)
    def time_render_color_only(self, resolution, world_count, iterations)
class FastSensorTiledCameraPixel(_SceneBenchmark)
    def time_render_color_only(self, resolution, world_count, iterations)
    def time_render_depth_only(self, resolution, world_count, iterations)
class TiledCameraShapes256(_SceneBenchmark)
def write_preview_images(scene_names, output_dir, image_size)
def print_fps(name, duration, resolution, world_count, iterations)
def print_fps_results(results)
```

### asv/benchmarks/simulation/bench_teleop_mujoco.py

```
"""Benchmark a scripted G1 bimanual pushing control loop.

The measured loop covers deterministic two-hand six-DoF command generation, IK,
joint-target writes, and two completed MuJoCo physics substeps. Rendering,
physical input devices, transport, perception, and display latency are outside
the benchmark scope."""
def _write_robot_targets(joint_q_ik, nominal_joint_q, arm_joint_mask, previous_joint_target_q, dt, joint_target_q, joint_target_qd)
class _TeleopMode()
class _WindowStats()
    def __init__(self, maxlen)
    def add(self, name, value)
    def summary(self, name)
    def coefficient_of_variation_pct(self, name)
    def clear(self)
def _quat_to_vec4(q)
def _quat_to_np(q)
def _vec3_to_np(v)
class _TeleopLoop()
    def __init__(self, mode, stats_window)
    def _build_robot(self)
    def _add_scene(builder)
    def _find_body(model, name)
    def _setup_ik(self)
    def _update_command(self)
    def _write_targets(self)
    def _simulate(self)
    def _record_workload_state(self)
    def _has_hand_object_contact(self)
    def step(self)
    def clear_metrics(self)
def _skip_unavailable_mode(mode)
class _TeleopMuJoCoBenchmark()
    """Shared setup for scripted synchronous teleop benchmarks."""
    def setup(self, mode)
    def time_teleop_loop(self, mode)
    def _step_frames(self, frame_count)
    def _measure_frames(self)
    def _validate_workload(self)
class FastTeleopMuJoCo(_TeleopMuJoCoBenchmark)
    """Pull-request smoke benchmarks across GPU and CPU execution modes."""
    def track_mean_loop_ms(self, mode)
    def track_p95_loop_ms(self, mode)
class TeleopMuJoCo(_TeleopMuJoCoBenchmark)
    """Nightly teleop benchmark covering GPU and CPU solver backends."""
    def track_mean_loop_ms(self, mode)
    def track_p95_loop_ms(self, mode)
    def track_frame_overrun_pct(self, mode)
    def track_loop_time_cv_pct(self, mode)
    def track_real_time_factor(self, mode)
    def track_sustainable_physics_step_hz(self, mode)
    def track_mean_target_error_m(self, mode)
    def track_mean_target_rotation_error_rad(self, mode)
    def track_hand_object_contact_frame_pct(self, mode)
    def track_object_displacement_m(self, mode)
```

### asv/benchmarks/simulation/bench_viewer.py

```
class KpiViewerGL()
    def setup(self, robot, world_count)
    def time_rendering_frame(self, robot, world_count)
    def teardown(self, robot, world_count)
class FastViewerGL()
    def setup(self, robot, world_count)
    def time_rendering_frame(self, robot, world_count)
    def teardown(self, robot, world_count)
```

### asv/tests/test_benchmark_simulation.py

```
class TestSimulationBenchmarks(TestCase)
    def _discover_benchmarks(cls)
    def _make_anymal_workload(self, root_y, root_z)
    def test_asv_runner_resolves_benchmark_support_modules(self)
    def test_benchmark_imports_preserve_warp_config(self)
    def test_benchmark_modules_defer_workload_imports(self)
    def test_convex_benchmark_covers_types_and_scales(self)
    def test_nightly_collision_benchmarks_cover_distinct_pipeline_paths(self)
    def test_deformable_collision_benchmark_is_in_pr_gate(self)
    def test_fast_kitchen_g1_validates_kitchen_body_count(self)
    def test_mujoco_step_falls_back_when_cuda_graph_is_unavailable(self)
    def test_mujoco_kpi_requires_cuda_graph(self)
    def test_mujoco_metrics_include_solver_iterations(self)
    def test_metric_setup_caches_skip_without_cuda(self)
    def test_kpi_dr_legs_setup_cache_timeout_exceeds_default(self)
    def test_fast_dr_legs_solver_does_not_import_torch(self)
    def test_aws_benchmark_comparison_gates_only_runtime_metrics(self)
    def test_pr_gate_caps_repeats_without_dropping_cases(self)
    def test_fast_allegro_uses_representative_pr_workload(self)
    def test_pr_asv_config_only_omits_torch(self)
    def test_pr_camera_warmup_matches_selected_outputs(self)
    def test_anymal_short_horizon_validation(self)
```

### newton/_src/geometry/simplex_solver.py

```
"""Gilbert-Johnson-Keerthi (GJK) algorithm with simplex solver for collision detection.

This module implements the GJK distance algorithm, which computes the minimum distance
between two convex shapes. GJK operates on the Minkowski difference of the shapes and
iteratively builds a simplex (1-4 vertices) that either contains the origin (indicating
collision) or gets progressively closer to it (for distance computation).

The algorithm works by:
1. Building a simplex in Minkowski space using support mapping
2. Finding the point on the simplex closest to the origin
3. Computing a new search directi"""
def create_solve_closest_distance(support_func, _support_funcs)
```

### newton/_src/sim/articulation.py

```
def com_twist_to_point_velocity(qd, X_wb, body_com, point)
def origin_twist_to_com_twist(qd, X_wb, body_com)
def com_twist_to_origin_twist(qd, X_wb, body_com)
def transform_2d_rotational_axes(axis_0, axis_1, q0)
def compute_2d_rotational_dofs(axis_0, axis_1, q0, q1, qd0, qd1)
def invert_2d_rotational_dofs(axis_0, axis_1, q_p, q_c, w_err)
def transform_3d_rotational_axes(axis_0, axis_1, axis_2, q0, q1)
def compute_3d_rotational_dofs(axis_0, axis_1, axis_2, q0, q1, q2, qd0, qd1, qd2)
def invert_3d_rotational_dofs(axis_0, axis_1, axis_2, q_p, q_c, w_err)
def eval_joint_motion(type, q_start, qd_start, lin_axis_count, ang_axis_count, joint_q, joint_qd, joint_axis)
def eval_joint_child_state(type, parent, child, X_wp, X_pj, X_cj, X_j, v_j, body_qd, body_com)
def eval_single_articulation_fk(joint_start, joint_end, joint_articulation, joint_q, joint_qd, joint_q_start, joint_qd_start, joint_type, joint_parent, joint_child, joint_X_p, joint_X_c, joint_axis, joint_dof_dim, body_com, body_flags, body_flag_filter, body_q, body_qd)
def eval_articulation_fk(articulation_start, articulation_end, articulation_count, articulation_mask, articulation_indices, joint_articulation, joint_q, joint_qd, joint_q_start, joint_qd_start, joint_type, joint_parent, joint_child, joint_X_p, joint_X_c, joint_axis, joint_dof_dim, body_com, body_flags, body_flag_filter, body_q, body_qd)
def eval_fk(model, joint_q, joint_qd, state, mask, indices, body_flag_filter)
def compute_shape_world_transforms(shape_transform, shape_body, body_q, shape_world_transform)
def reconstruct_angular_q_qd(q_pc, w_err, X_wp, axis)
def eval_articulation_ik(articulation_start, articulation_end, articulation_count, articulation_mask, articulation_indices, body_q, body_qd, body_com, joint_type, joint_parent, joint_child, joint_X_p, joint_X_c, joint_axis, joint_dof_dim, joint_q_start, joint_qd_start, body_flags, body_flag_filter, joint_q, joint_qd)
def eval_ik(model, state, joint_q, joint_qd, mask, indices, body_flag_filter)
def write_free_distance_motion_subspace(X_pa_world, pivot_world, qd_start, joint_S_s)
def jcalc_motion_subspace(joint_type_value, joint_axis, joint_q, lin_axis_count, ang_axis_count, X_pa_world, X_wc, body_com_child, q_start, qd_start, joint_S_s)
def eval_articulation_jacobian(articulation_start, articulation_end, articulation_count, articulation_mask, joint_type, joint_parent, joint_child, joint_ancestor, joint_q_start, joint_qd_start, joint_X_p, joint_axis, joint_q, joint_dof_dim, body_q, body_com, J, joint_S_s)
def eval_jacobian(model, state, J, joint_S_s, mask)
def transform_spatial_inertia(t, I)
def compute_body_spatial_inertia(body_inertia, body_mass, body_q, body_I_s)
def eval_articulation_mass_matrix(articulation_start, articulation_end, articulation_count, articulation_mask, joint_child, joint_qd_start, body_I_s, J, H)
def eval_articulation_inverse_dynamics_force_kernel(articulation_start, articulation_end, articulation_count, articulation_mask, joint_type, joint_parent, joint_qd_start, joint_X_p, body_q, mass_matrix, joint_qdd, coriolis_force, gravity_force, tau)
def eval_inverse_dynamics_force(model, state)
def eval_mass_matrix(model, state, H, J, body_I_s, joint_S_s, mask)
```

### newton/_src/sim/articulation_cuda.py

```
def create_eval_articulation_fk_tile(level_capacity, write_all, has_rod)
```

### newton/_src/sim/collide.py

```
def _shape_collide_mask(model, shape_count)
def _pair_requires_generic_convex_narrow_phase(type_a, type_b)
class ContactWriterData()
    """Contact writer data for collide write_contact function."""
def _write_contact_at_index(contact_data, writer_data, index, point_a_world, point_b_world, normal_a_to_b)
def write_contact(contact_data, writer_data, output_index)
def write_contact_speculative(contact_data, writer_data, output_index)
def compute_shape_aabbs(body_q, shape_transform, shape_body, shape_type, shape_scale, shape_collision_radius, shape_source_ptr, shape_margin, shape_gap, shape_collision_aabb_lower, shape_collision_aabb_upper, contact_counters, contact_generation, broad_phase_pair_count, num_contact_counters, aabb_lower, aabb_upper, geom_data, geom_xform)
def compute_shape_velocities(body_q, body_qd, body_com, shape_body, shape_transform, shape_collision_aabb_lower, shape_collision_aabb_upper, shape_collision_radius, shape_gap, collision_update_dt, max_speculative_extension, shape_linear_velocity, shape_angular_velocity, shape_search_gap, shape_displacement, shape_aabb_lower, shape_aabb_upper)
class _RigidContactCountEstimate()
    """Diagnostic details for an automatically selected rigid-contact capacity."""
def _estimate_rigid_contact_details(model)
def _estimate_rigid_contact_max(model)
def _warn_large_rigid_contact_estimate(estimate)
def _estimate_rigid_contact_max_per_world(model, rigid_contact_max)
def _compute_per_world_shape_pairs_max(model)
def _compute_per_world_mask_pair_max(model, first_mask, second_mask)
def _resolve_shape_pairs_max(model, override)
def _compute_generic_convex_pair_stats(model)
def _normalize_broad_phase_mode(mode)
def _infer_broad_phase_mode_from_instance(broad_phase)
def _world_compatible_pairs(feature_world, shape_world, world_count, device, shape_ok)
def _build_soft_particle_rigid_contact_pairs(model)
def _count_soft_particle_rigid_contact_pairs(model)
def _build_soft_face_rigid_contact_pairs(model, capable_shape_mask)
def _build_soft_edge_rigid_contact_pairs(model, capable_shape_mask)
def _full_surface_capable_shape_mask(model)
def _raise_on_unprovisioned_full_surface_meshes(model, capable)
def _warn_full_surface_fallbacks(model, capable)
class CollisionPipeline()
    """Full-featured collision pipeline with GJK/MPR narrow phase and pluggable broad phase.

Key features:
    - GJK/MPR algorithms for convex-convex collision detection
    - Multiple broad phase options: NXN (all-pairs), SAP (sweep-and-prune), EXPLICIT (precomputed pairs)
    - Mesh-mesh collision via S"""
    def __init__(self, model)
    def rigid_contact_max(self)
    def soft_contact_max(self)
    def soft_contact_margin(self)
    def soft_contact_margin(self, value)
    def soft_contact_pair_count(self)
    def soft_rigid_contact_pair_count(self)
    def contacts(self)
    def init_soft_self_contact(self)
    def set_collision_detection_range(self)
    def _ensure_soft_self_contact_detector(self)
    def _get_soft_self_contact_detector(self, contacts)
    def refit_soft_self_contact_bvh(self, new_pos)
    def _detect_soft_self_contact(self, particle_q, contacts)
    def reset_contact_matching(self, world_mask)
    def _build_excluded_pairs(model)
    def collide(self, state, contacts)
```

### newton/_src/sim/contact_kinematics.py

```
def _validate_output(name, output, dtype, contact_max, device)
def eval_rigid_contact_kinematics(model, state, contacts)
```

### newton/_src/sim/contacts.py

```
def _warn_rigid_contact_diff_deprecated(name)
def _increment_contact_generation(generation)
def _clear_counters_and_bump_generation(counters, generation, num_counters, bump_generation)
def contact_surface_separation(point0_world, point1_world, normal, margin0, margin1)
def contact_surface_point(X_wb, point_local, offset_local)
class Contacts()
    """Stores contact information for rigid and soft body collisions, to be consumed by a solver.

This class manages buffers for contact data such as positions, normals, margins, and shape indices
for both rigid-rigid and soft-rigid contacts. The buffers are allocated on the specified device and can
optio"""
    def validate_extended_attributes(cls, attributes)
    def __init__(self, rigid_contact_max, soft_contact_max)
    def clear(self, bump_generation)
    def device(self)
    def rigid_contact_diff_distance(self)
    def rigid_contact_diff_distance(self, value)
    def rigid_contact_diff_normal(self)
    def rigid_contact_diff_normal(self, value)
    def rigid_contact_diff_point0_world(self)
    def rigid_contact_diff_point0_world(self, value)
    def rigid_contact_diff_point1_world(self)
    def rigid_contact_diff_point1_world(self, value)
    def contact_matching_mode(self)
    def _assert_particle_only_soft_contacts(self, solver_name)
```

### newton/_src/sim/control.py

```
class Control()
    """Time-varying control data for a :class:`Model`.

Carries joint torques, control inputs, muscle activations, and tri/tet
activation forces. Create via :func:`newton.Model.control()`.

Position and velocity targets live on :attr:`joint_target_q` and
:attr:`joint_target_qd`. The shape of :attr:`joint_t"""
    def __init__(self)
    def clear(self, model)
    def _clear_namespaced_arrays(self)
```

### newton/_src/sim/enums.py

```
class ModelFlags(IntEnum)
    """Flags indicating which parts of the model have been updated.

These flags are used with :meth:`~newton.solvers.SolverBase.notify_model_changed`
to specify which properties have changed, allowing the solver to efficiently
update only the necessary components."""
class StateFlags(IntEnum)
    """Flags indicating which state attributes were updated or should be reset.

These flags are used with :meth:`~newton.solvers.SolverBase.reset` to
control which parts of the simulation state are reset, and with
:meth:`~newton.solvers.experimental.coupled.CouplingInterface.coupling_notify_input_state_up"""
class BodyFlags(IntEnum)
    """Per-body dynamic state flags.

Each finalized model body must store exactly one runtime state flag:
:attr:`DYNAMIC` or :attr:`KINEMATIC`. Coupled solver views may OR in
:attr:`PROXY` on view-local ``body_flags`` overrides. :attr:`ALL` is a
convenience filter mask for APIs such as :func:`newton.eval_"""
def _warn_joint_type_cable_deprecated()
class _DeprecatedJointTypeMeta(EnumMeta)
    def __getattribute__(cls, name)
    def __getitem__(cls, name)
    def __dir__(cls)
class JointType(IntEnum)
    """Enumeration of joint types supported in Newton."""
    def dof_count(self, num_axes)
    def constraint_count(self, num_axes)
class _DeprecatedEqTypeMeta(EnumMeta)
    def __getattribute__(cls, name)
    def __call__(cls)
def _warn_eq_type_deprecated()
class EqType(IntEnum)
    """Deprecated alias for :class:`~newton.solvers.SolverMuJoCo.EqType`.

.. deprecated:: 1.4
    Use :class:`~newton.solvers.SolverMuJoCo.EqType` instead."""
class JointTargetMode(IntEnum)
    """Enumeration of actuator modes for joint degrees of freedom.

This enum manages UsdPhysics compliance by specifying whether joint_target_q/qd
inputs are active for a given DOF. It determines which actuators are installed when
using solvers that require explicit actuator definitions (e.g., MuJoCo solv"""
    def from_gains(target_ke, target_kd, force_position_velocity, has_drive)
```

### newton/_src/sim/graph_coloring.py

```
class ColoringAlgorithm(Enum)
def _to_warp_coloring_algorithm(algorithm)
def validate_graph_coloring(edge_indices, colors)
def convert_to_color_groups(num_colors, particle_colors, return_wp_array, device)
def _canonicalize_edges_np(edges_np)
def construct_tetmesh_graph_edges(tet_indices, tet_active_mask)
def construct_trimesh_graph_edges(tri_indices, tri_active_mask, bending_edge_indices, bending_edge_active_mask, return_wp_array)
def construct_particle_graph(tri_graph_edges, tri_active_mask, bending_edge_indices, bending_edge_active_mask, tet_graph_edges_np, tet_active_mask)
def color_graph(num_nodes, graph_edge_indices, balance_colors, target_max_min_color_ratio, algorithm)
def plot_graph(vertices, edges, edge_labels, node_labels, node_colors, layout)
def combine_independent_coloring_plan(sized_groups_1, sized_groups_2)
def combine_independent_particle_coloring(color_groups_1, color_groups_2)
def color_rigid_bodies(num_bodies, joint_parent, joint_child, balance_colors, target_max_min_color_ratio, algorithm)
```

### newton/_src/sim/ik/__init__.py

```
"""Inverse-kinematics submodule."""
```

### newton/_src/sim/ik/ik_common.py

```
"""Common enums and utility kernels shared across IK components."""
class IKJacobianType(Enum)
    """Specifies the backend used for Jacobian computation in inverse kinematics."""
def _eval_fk_articulation_batched(articulation_start, articulation_end, joint_articulation, joint_q, joint_qd, joint_q_start, joint_qd_start, joint_type, joint_parent, joint_child, joint_X_p, joint_X_c, joint_axis, joint_dof_dim, body_com, body_flags, body_q, body_qd)
def eval_fk_batched(model, joint_q, joint_qd, body_q, body_qd)
def fk_accum(joint_parent, X_local, body_q)
def compute_costs(residuals, num_residuals, costs)
```

### newton/_src/sim/ik/ik_lbfgs_optimizer.py

```
"""L-BFGS optimizer backend for inverse kinematics."""
def _scale_negate(src, scale, dst)
def _fan_out_problem_idx(batch_problem_idx, out_indices)
def _generate_candidates_velocity(joint_q, search_direction, line_search_alphas, candidate_q, candidate_dq)
def _apply_residual_mask(residuals, mask, seeds_out)
def _accumulate_gradients(base_grad, add_grad)
class BatchCtx()
class IKOptimizerLBFGS()
    """L-BFGS optimizer for batched inverse kinematics.

The optimizer maintains a limited-memory quasi-Newton approximation and
chooses step sizes with a parallel strong-Wolfe line search. It supports
the same Jacobian backends as :class:`~newton.ik.IKOptimizerLM`.

Args:
    model: Shared articulation mo"""
    def __new__(cls, model, n_batch, objectives)
    def __init__(self, model, n_batch, objectives, jacobian_mode, history_len, h0_scale, line_search_alphas, wolfe_c1, wolfe_c2)
    def _alloc_solver_buffers(self, grad)
    def _alloc_line_search_buffers(self, grad, line_search_alphas)
    def _alloc_line_search_analytic_buffers(self)
    def _alloc_mixed_buffers(self)
    def _build_residual_offsets(self)
    def _ctx_solver(self, joint_q)
    def _ctx_candidates(self)
    def _validate_ctx(self, ctx)
    def _gradient_at(self, ctx, out_grad)
    def _grad_autodiff(self, ctx, out_grad)
    def _grad_analytic(self, ctx, out_grad)
    def _for_objectives_residuals(self, ctx)
    def _residuals_autodiff(self, ctx)
    def _residuals_analytic(self, ctx)
    def _init_objectives(self)
    def _init_cuda_streams(self)
    def _parallel_for_objectives(self, fn)
    def step(self, joint_q_in, joint_q_out, iterations)
    def reset(self)
    def compute_costs(self, joint_q)
    def _compute_residuals(self, joint_q, residuals_out)
    def _compute_motion_subspace(self)
    def _integrate_dq(self, joint_q)
    def _step(self, joint_q, iteration)
    def _compute_initial_slope(self)
    def _compute_search_direction(self)
    def _update_history(self)
    def _line_search(self, joint_q)
    def _line_search_select_best(self, joint_q)
    def _build_specialized(cls, key)
```

### newton/_src/sim/ik/ik_lm_optimizer.py

```
"""Levenberg-Marquardt optimizer backend for inverse kinematics."""
class BatchCtx()
def _accept_reject(cost_curr, cost_prop, pred_red, rho_min, accept)
def _update_lm_state(joint_q_proposed, residuals_proposed, costs_proposed, accept_flags, n_coords, num_residuals, lambda_factor, lambda_min, lambda_max, joint_q_current, residuals_current, costs, lambda_values)
def _zero_fixed_dof_jacobian_columns(joint_dof_mask, jacobian)
def _validate_joint_dof_mask(model, joint_dof_mask)
class IKOptimizerLM()
    """Levenberg-Marquardt optimizer for batched inverse kinematics.

The optimizer solves a batch of independent IK problems that share a
single articulation model and objective list. Jacobians can be evaluated
with ``IKJacobianType.AUTODIFF``, ``IKJacobianType.ANALYTIC``, or
``IKJacobianType.MIXED``.

Ar"""
    def __new__(cls, model, n_batch, objectives)
    def __init__(self, model, n_batch, objectives, lambda_initial, jacobian_mode, lambda_factor, lambda_min, lambda_max, rho_min)
    def _init_objectives(self)
    def _init_cuda_streams(self)
    def _parallel_for_objectives(self, fn)
    def _alloc_solver_buffers(self, grad)
    def _build_residual_offsets(self)
    def _ctx_solver(self, joint_q)
    def _validate_ctx_for_mode(self, ctx)
    def _for_objectives_residuals(self, ctx)
    def _residuals_autodiff(self, ctx)
    def _residuals_analytic(self, ctx)
    def _jacobian_at(self, ctx)
    def _apply_joint_dof_mask(self, jacobian)
    def _jacobian_autodiff(self, ctx)
    def _jacobian_analytic(self, ctx)
    def step(self, joint_q_in, joint_q_out, iterations, step_size)
    def _compute_residuals(self, joint_q, output_residuals)
    def _compute_motion_subspace(self)
    def _integrate_dq(self, joint_q)
    def _step(self, joint_q, step_size, iteration)
    def reset(self)
    def compute_costs(self, joint_q)
    def _solve_tiled(self, jacobian, residuals, lambda_values, dq_dof, pred_reduction)
    def _build_specialized(cls, key)
```

### newton/_src/sim/ik/ik_objectives.py

```
"""Objective definitions for inverse kinematics."""
class IKObjective()
    """Base class for inverse-kinematics objectives.

Each objective contributes one or more residual rows to the global IK
system and can optionally provide an analytic Jacobian. Objective
instances are shared across a batch of problems, so per-problem data such
as targets should live in device arrays and"""
    def __init__(self)
    def set_batch_layout(self, total_residuals, residual_offset, n_batch)
    def _require_batch_layout(self)
    def residual_dim(self)
    def compute_residuals(self, body_q, joint_q, model, residuals, start_idx, problem_idx)
    def compute_jacobian_autodiff(self, tape, model, jacobian, start_idx, dq_dof)
    def supports_analytic(self)
    def bind_device(self, device)
    def init_buffers(self, model, jacobian_mode)
    def compute_jacobian_analytic(self, body_q, joint_q, model, jacobian, joint_S_s, start_idx)
def _pos_residuals(body_q, target_pos, link_index, link_offset, start_idx, weight, problem_idx_map, residuals)
def _pos_jac_fill(q_grad, n_dofs, start_idx, component, jacobian)
def _update_position_target(problem_idx, new_position, target_array)
def _update_position_targets(new_positions, target_array)
def _pos_jac_analytic(link_index, link_offset, affects_dof, body_q, joint_S_s, start_idx, n_dofs, weight, jacobian)
class IKObjectivePosition(IKObjective)
    """Match the world-space position of a point on a link.

Args:
    link_index: Body index whose frame defines the constrained link.
    link_offset: Point in the link's local frame [m].
    target_positions: Target positions [m], shape [problem_count].
    weight: Scalar multiplier applied to the resid"""
    def __init__(self, link_index, link_offset, target_positions, weight)
    def init_buffers(self, model, jacobian_mode)
    def supports_analytic(self)
    def set_target_position(self, problem_idx, new_position)
    def set_target_positions(self, new_positions)
    def residual_dim(self)
    def compute_residuals(self, body_q, joint_q, model, residuals, start_idx, problem_idx)
    def compute_jacobian_autodiff(self, tape, model, jacobian, start_idx, dq_dof)
    def compute_jacobian_analytic(self, body_q, joint_q, model, jacobian, joint_S_s, start_idx)
def _limit_residuals(joint_q, joint_limit_lower, joint_limit_upper, dof_to_coord, n_dofs, weight, start_idx, residuals)
def _limit_jac_fill(q_grad, n_dofs, start_idx, jacobian)
def _limit_jac_analytic(joint_q, joint_limit_lower, joint_limit_upper, dof_to_coord, n_dofs, start_idx, weight, jacobian)
class IKObjectiveJointLimit(IKObjective)
    """Penalize violations of per-DoF joint limits.

Each DoF contributes one residual row whose value is zero inside the valid
range and increases linearly once the coordinate exceeds its lower or upper
bound.

Args:
    joint_limit_lower: Lower joint limits [m or rad], shape
        [joint_dof_count].
  """
    def __init__(self, joint_limit_lower, joint_limit_upper, weight)
    def init_buffers(self, model, jacobian_mode)
    def supports_analytic(self)
    def residual_dim(self)
    def compute_residuals(self, body_q, joint_q, model, residuals, start_idx, problem_idx)
    def compute_jacobian_autodiff(self, tape, model, jacobian, start_idx, dq_dof)
    def compute_jacobian_analytic(self, body_q, joint_q, model, jacobian, joint_S_s, start_idx)
def _rot_residuals(body_q, target_rot, link_index, link_offset_rotation, canonicalize_quat_err, start_idx, weight, problem_idx_map, residuals)
def _rot_jac_fill(q_grad, n_dofs, start_idx, component, jacobian)
def _update_rotation_target(problem_idx, new_rotation, target_array)
def _update_rotation_targets(new_rotation, target_array)
def _rot_jac_analytic(affects_dof, joint_S_s, start_idx, n_dofs, weight, jacobian)
class IKObjectiveRotation(IKObjective)
    """Match the world-space orientation of a link frame.

Args:
    link_index: Body index whose frame defines the constrained link.
    link_offset_rotation: Local rotation from the body frame to the
        constrained frame, stored in ``(x, y, z, w)`` order.
    target_rotations: Target orientations, s"""
    def __init__(self, link_index, link_offset_rotation, target_rotations, canonicalize_quat_err, weight)
    def init_buffers(self, model, jacobian_mode)
    def supports_analytic(self)
    def set_target_rotation(self, problem_idx, new_rotation)
    def set_target_rotations(self, new_rotations)
    def residual_dim(self)
    def compute_residuals(self, body_q, joint_q, model, residuals, start_idx, problem_idx)
    def compute_jacobian_autodiff(self, tape, model, jacobian, start_idx, dq_dof)
    def compute_jacobian_analytic(self, body_q, joint_q, model, jacobian, joint_S_s, start_idx)
```

### newton/_src/sim/ik/ik_solver.py

```
"""Frontend wrapper for inverse-kinematics optimizers with sampling/selection."""
class IKOptimizer(str, Enum)
    """Optimizer backends supported by :class:`~newton.ik.IKSolver`."""
class IKSampler(str, Enum)
    """Sampling strategies used by :class:`~newton.ik.IKSolver` before optimization."""
def _sample_none_kernel(joint_q_in, n_seeds, n_coords, joint_q_out)
def _sample_gauss_kernel(joint_q_in, n_seeds, n_coords, noise_std, joint_lower, joint_upper, joint_bounded, base_seed, joint_q_out)
def _sample_uniform_kernel(n_coords, joint_lower, joint_upper, joint_bounded, base_seed, joint_q_out)
def _sample_roberts_kernel(n_seeds, n_coords, roberts_basis, joint_lower, joint_upper, joint_bounded, joint_q_out)
def _select_best_seed_indices(costs, n_seeds, best)
def _gather_best_seed(joint_q_expanded, best, n_seeds, n_coords, joint_q_out)
def _pull_seed(seed_state, out_seed)
def _set_seed(seed_state, value)
class IKSolver()
    """High-level inverse-kinematics front end with optional multi-seed sampling.

``IKSolver`` expands each base problem into one or more candidate seeds,
delegates optimization to :class:`~newton.ik.IKOptimizerLM` or
:class:`~newton.ik.IKOptimizerLBFGS`, and keeps the lowest-cost candidate for each
base """
    def __init__(self, model, n_problems, objectives)
    def step(self, joint_q_in, joint_q_out, iterations, step_size)
    def reset(self)
    def joint_q(self)
    def costs(self)
    def __getattr__(self, name)
    def _sample(self, joint_q_in)
    def _compute_roberts_basis(n_coords)
```

### newton/_src/sim/inverse_dynamics.py

```
def _compute_body_q_com_kernel(body_q, body_com, body_q_com)
class _InverseDynamicsScratchBuffer()
    """Internal scratch buffers for :func:`eval_inverse_dynamics_passive`.

Holds the RNEA per-body and per-DOF arrays, the mass-matrix Jacobian
scratch, and the constant-zero inputs that the compensation passes
feed into :func:`eval_rigid_tau` and :func:`eval_rigid_id`. All buffers
are sized for the topol"""
    def __init__(self, body_count, articulation_count, joint_dof_count, joint_target_q_count, max_dofs_per_articulation, max_joints_per_articulation, world_count, device)
def _rnea_compensation_pass(model, state, scratch, joint_qd, gravity, tau_out, mask)
def _compute_gravity_force(model, state, gravity_force, scratch, mask)
def _compute_coriolis_force(model, state, coriolis_force, scratch, mask)
def eval_inverse_dynamics_passive(model, state)
```

### newton/_src/sim/joint_mimic.py

```
def eval_mimic_joints(joint_mimic_joint, joint_mimic_coeffs, joint_q_start, joint_qd_start, joint_q, joint_qd)
def eval_mimic(model, state_in, state_out)
def eval_joint_mimic_coordinate(joint, component, body_q, body_com, joint_type, joint_parent, joint_child, joint_X_p, joint_X_c, joint_qd_start, joint_dof_dim, joint_axis)
def eval_joint_mimic_velocity(parent, child, parent_gradient, child_gradient, body_qd)
def has_supported_joint_mimics(model, solver_name)
```

### newton/_src/sim/model.py

```
"""Implementation of the Newton model class."""
def _pack_shape_pair_codes(shape_a, shape_b)
def _unpack_shape_pair_codes(codes)
class _ShapeCollisionFilterPairs(?)
    """Read-only set view over sorted, unique packed filter-pair codes."""
    def __init__(self, packed)
    def _from_iterable(cls, iterable)
    def __bool__(self)
    def __contains__(self, pair)
    def __iter__(self)
    def __len__(self)
    def _contains_code(self, code)
    def contains_pair(self, shape_a, shape_b)
    def mask_pairs(self, pairs)
    def pairs_array(self)
class Model()
    """Represents the static (non-time-varying) definition of a simulation model in Newton.

The Model class encapsulates all geometry, constraints, and parameters that describe a physical system
for simulation. It is designed to be constructed via the ModelBuilder, which handles the correct
initialization"""
    def __init__(self, device)
    def _set_shape_collision_filter_packed(self, packed)
    def _set_shape_collision_filter_pairs(self, pairs)
    def shape_collision_filter_pairs(self)
    def shape_collision_filter_contains(self, shape_a, shape_b)
    def shape_collision_filter_pairs_array(self)
    def shape_collision_filter_mask(self, pairs)
    def _attribute_spec(self, name)
    def _iter_attribute_specs(self)
    def _set_attribute_spec(self, name, spec)
    def _resolve_attribute_frequency(self, name)
    def _attribute_reference_frequency(self, name)
    def _attribute_row_width(self, name)
    def _attribute_requires_empty_sentinel(self, name)
    def _normalize_attribute_reference(self, references)
    def joint_target_q_start(self)
    def bvh_build_shapes(self, state)
    def bvh_refit_shapes(self, state)
    def bvh_build_particles(self, state)
    def bvh_refit_particles(self, state)
    def state(self, requires_grad)
    def _add_requested_state_attributes(self, state, requested, requires_grad)
    def _attribute_frequency_count(self, frequency)
    def control(self, requires_grad, clone_variables)
    def set_gravity(self, gravity, world)
    def _init_collision_pipeline(self, enable_rigid_soft_full_surface_contact)
    def contacts(self, collision_pipeline)
    def collide(self, state, contacts)
    def request_state_attributes(self)
    def request_contact_attributes(self)
    def get_requested_contact_attributes(self)
    def _add_custom_attributes(self, destination, assignment, requires_grad, clone_arrays)
    def add_attribute(self, name, attrib, frequency, assignment, namespace, references)
    def get_attribute_frequency(self, name)
    def get_custom_frequency_count(self, frequency)
    def get_requested_state_attributes(self)
```

### newton/_src/sim/rod.py

```
"""Discrete rod input data."""
def _validate_nonnegative_float(name, value)
def _resolve_shear_modulus(youngs_modulus)
def _generate_straight_points(start, direction, length, segment_count)
def _compute_parallel_transport_quaternions(points)
class Rod()
    """Represents discrete rod input for model construction.

A rod stores prepared centerline points, segment topology, and one material
frame per segment. It may additionally store a capsule/cross-section radius
and either uniform isotropic material properties or a complete set of
uniform section rigidit"""
    def __init__(self, points)
    def _normalize_points(points)
    def _normalize_edges(edges, point_count)
    def _normalize_quaternions(quaternions, segment_count)
    def _resolve_radius(self)
    def _resolve_elastic_material(self)
    def _generate_ordered_chain_edges(point_count)
    def _is_ordered_chain_topology(point_count, edges)
    def _validated_centerline(self)
    def _normalize_and_validate_geometry(self)
    def points(self)
    def points(self, value)
    def edges(self)
    def edges(self, value)
    def quaternions(self)
    def quaternions(self, value)
    def point_count(self)
    def segment_count(self)
    def segment_lengths(self)
    def _resolve_section_rigidities(self)
    def create_straight(start, direction, length)
    def compute_frames(self)
    def copy(self)
```

### newton/_src/sim/state.py

```
def _copy_arrays(dst, src, prefix)
class State()
    """Represents the time-varying state of a :class:`Model` in a simulation.

The State object holds all dynamic quantities that change over time during simulation,
such as particle and rigid body positions, velocities, and forces, as well as joint coordinates.

State objects are typically created via :me"""
    def validate_extended_attributes(cls, attributes)
    def __init__(self)
    def body_q_prev(self)
    def body_q_prev(self, value)
    def clear_forces(self)
    def assign(self, other)
    def requires_grad(self)
    def body_count(self)
    def particle_count(self)
    def joint_coord_count(self)
    def joint_dof_count(self)
```

### newton/_src/solvers/kamino/_src/kinematics/constraints.py

```
"""Provides mechanisms to define and manage constraints and their associated input/output data."""
def get_max_constraints_per_world(model, limits, contacts)
def make_unilateral_constraints_info(model, data, limits, contacts)
def _update_constraints_info(model_info_num_bilateral_joint_cts, model_info_num_bounded_joint_cts, data_info_num_limits, data_info_num_contacts, data_info_num_total_cts, data_info_num_limit_cts, data_info_num_contact_cts, data_info_limit_cts_group_offset, data_info_contact_cts_group_offset)
def _unpack_joint_constraint_solutions(model_time_inv_dt, model_joint_wid, model_joints_num_dynamic_cts, model_joints_num_kinematic_cts, model_joints_num_friction_cts, model_joints_num_effort_cts, model_joints_dynamic_cts_offset, model_joints_kinematic_cts_offset, model_joints_friction_cts_offset, model_joints_effort_cts_offset, model_joints_dynamic_cts_offset_total_cts, model_joints_kinematic_cts_offset_total_cts, model_joints_friction_cts_offset_total_cts, model_joints_effort_cts_offset_total_cts, lambdas, joint_lambda_dyn_j, joint_lambda_kin_j, joint_lambda_f_j, joint_lambda_tau_j)
def _unpack_limit_constraint_solutions(model_time_inv_dt, model_info_total_cts_offset, data_info_limit_cts_group_offset, limit_model_num_limits, limit_wid, limit_lid, lambdas, v_plus, limit_reaction, limit_velocity)
def _unpack_contact_constraint_solutions(model_time_inv_dt, model_info_total_cts_offset, data_info_contact_cts_group_offset, contact_model_num_contacts, contact_wid, contact_cid, lambdas, v_plus, contact_mode, contact_reaction, contact_velocity)
def update_constraints_info(model, data)
def unpack_constraint_solutions(lambdas, v_plus, model, data, limits, contacts)
```

### newton/_src/solvers/kamino/_src/utils/sim/__init__.py

```
"""KAMINO: Simulation Module"""
```

### newton/_src/solvers/kamino/_src/utils/sim/datalog.py

```
"""Utilities for simulation data logging and plotting."""
class SimulationLogger()
    """TODO"""
    def initialize_plt(cls)
    def __init__(self, max_frames, sim, controller)
    def reset(self)
    def log(self)
    def plot_solver_info(self, path, show)
    def plot_joint_tracking(self, path, show)
    def plot_solution_metrics(self, path, show)
    def _unpack_key(key)
```

### newton/_src/solvers/kamino/_src/utils/sim/simulator.py

```
"""Provides a high-level interface for physics simulation."""
class SimulatorData()
    """Holds the time-varying data for the simulation.

Attributes:
    state_p: The previous state data of the simulation.
    state_n: The current state data of the simulation, computed from the previous step as:
        ``state_n = f(state_p, control)``, where ``f()`` is the system dynamics function.
  """
    def __init__(self, model)
    def cache_state(self)
class Simulator()
    """A high-level interface for executing physics simulations using Kamino.

The Simulator class encapsulates the entire simulation pipeline, including model definition,
state management, collision detection, constraint handling, and time integration.

A Simulator is typically instantiated from a :class:"""
    def __init__(self, model, config)
    def config(self)
    def model(self)
    def model_newton(self)
    def data(self)
    def state(self)
    def state_previous(self)
    def control(self)
    def limits(self)
    def contacts(self)
    def metrics(self)
    def collision_detector(self)
    def solver(self)
    def device(self)
    def set_pre_reset_callback(self, callback)
    def set_post_reset_callback(self, callback)
    def set_control_callback(self, callback)
    def reset(self, world_mask, config)
    def step(self)
```

### newton/_src/solvers/kamino/_src/utils/sim/viewer_recording.py

```
"""Ad-hoc viewer recording helper.

This monkey-patches a fully-initialized Newton viewer (as returned by
``newton.examples.init(parser)``) so the user can record per-frame PNGs
and stitch them into a video from inside the running viewer session.

After ``enable_recording`` the viewer is wired up but inactive: nothing is
written to disk until ``viewer.start_clip(...)`` is called, or the
``start_clip=True`` is passed to ``enable_recording``. Each call to
``viewer.start_clip()`` clears the target folder, resets counters, and records
up to ``max_frames`` frames before automatically writing the video"""
class _VideoRecording()
    """Helper class to store video recording settings and state in the viewer."""
def enable_recording(viewer, record_video, default_video_folder, num_skipped_frames, async_save, start_clip)
def _clear_pngs(folder)
def _should_step_with_record(self)
def _end_frame_with_record(self)
def _finish_clip(self)
def _reset_recording(self, video_folder)
def _start_clip(self, output_path, max_frames, video_folder, fps, keep_frames, on_done)
def _capture_frame(viewer, recording)
def _generate_video(self, output_filename, fps, keep_frames, quality, codec)
```

### newton/_src/solvers/kamino/config.py

```
"""Defines configurations for :class:`SolverKamino`."""
class ConfigBase()
    """Defines a base class for configuration containers providing interfaces for
registering custom attributes and parsing configurations from a Newton model."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
class CollisionDetectorConfig(ConfigBase)
    """A container to hold configurations for the internal collision detector used for contact generation."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class ConstraintStabilizationConfig(ConfigBase)
    """A container to hold configurations for global constraint stabilization parameters.

These parameters serve as global defaults/overrides, to be used
in combination with the per-constraint stabilization parameters
specified in the model, if the latter are provided."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class ConstrainedDynamicsConfig(ConfigBase)
    """A container to hold configurations for the construction of the constrained forward dynamics problem."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class PADMMSolverConfig()
    """A container to hold configurations for the PADMM forward dynamics solver."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class DVISolverConfig()
    """A container to hold configurations for the DVI forward dynamics solver."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class ForwardKinematicsSolverConfig()
    """A container to hold configurations for the Gauss-Newton forward kinematics solver used for state resets."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
class MaterialManagerConfig(ConfigBase)
    """A container to hold configurations for the internal material manager and material property mixing."""
    def register_custom_attributes(builder)
    def from_model(model)
    def validate(self)
    def __post_init__(self)
```

### newton/_src/solvers/kamino/examples/rl/observations.py

```
def _projected_yaw(q)
def _write_vec3(obs, idx, v)
def _compute_bipedal_obs_core(obs, q_i, u_i, q_j, dq_j, command, phase, freq_2pi, offset_enc, joint_default, joint_range, obs_offsets, num_bodies, num_joint_coords, num_joint_dofs, num_obs, cmd_dim, inv_path_dev_scale, inv_joint_vel_scale, phase_enc_dim, num_joints)
class PhaseRate(Module)
    """Defines the mapping between robot measurements and a pretrained phase rate."""
    def __init__(self, path, obs_cmd_range)
    def forward(self, input)
def _projected_yaw(q)
def _write_vec3(obs, idx, v)
def _compute_bipedal_obs_core(obs, q_i, u_i, q_j, dq_j, command, phase, freq_2pi, offset_enc, joint_default, joint_range, obs_offsets, num_bodies, num_joint_coords, num_joint_dofs, num_obs, cmd_dim, inv_path_dev_scale, inv_joint_vel_scale, phase_enc_dim, num_joints)
class PhaseRate(Module)
    """Defines the mapping between robot measurements and a pretrained phase rate."""
    def __init__(self, path, obs_cmd_range)
    def forward(self, input)
class ObservationBuilder(ABC)
    """Base class for building observation tensors from a Kamino Simulator.

Subclasses define which signals to extract and concatenate.  The builder
maintains internal buffers (e.g. action history) and provides a uniform
``compute()`` interface suitable for inference loops.

Args:
    sim: A Kamino ``Simu"""
    def __init__(self, sim, num_worlds, device, command_dim)
    def num_observations(self)
    def command_dim(self)
    def command(self)
    def command(self, value)
    def compute(self, actions)
    def reset(self, env_ids)
    def _get_joint_positions(self)
    def _get_joint_velocities(self)
    def _get_root_positions(self)
class DrlegsBaseObservation(ObservationBuilder)
    """Base observation builder for DR Legs.

Observation vector (63D):
    * root position        (3D  — pelvis xyz)
    * DOF positions        (36D — all joints, including passive linkages)
    * action history t-0   (12D — actuated joints, current step)
    * action history t-1   (12D — actuated joints,"""
    def __init__(self, body_sim, action_scale)
    def num_observations(self)
    def compute(self, actions)
    def reset(self, env_ids)
class BipedalObservation(ObservationBuilder, Module)
    """Bipedal observation builder for inference.

Reads commands from :pyattr:`command` (shape ``(num_worlds, 10)``),
simulator state from a :class:`RigidBodySim`, and maintains action
history and gait phase internally.

Command tensor layout (10 dims)::

     [0]      path_heading         (1)
     [1:3] """
    def __init__(self, body_sim, joint_position_default, joint_position_range, joint_velocity_scale, path_deviation_scale, phase_embedding_dim, phase_rate_policy_path, dt, num_joints)
    def get_feature_module(self)
    def num_observations(self)
    def compute(self, setpoints)
    def reset(self, env_ids)

```python
def num_observations(self) -> int:
        """Total observation dimensionality (per environment)."""
        ...
```

```python
def num_observations(self) -> int:
        return 3 + self._num_coords + self._num_actions + self._num_actions
```

```python
def num_observations(self) -> int:
        return self.num_obs
```
```

### newton/_src/solvers/kamino/examples/rl/simulation.py

```
class SimulatorFromNewton()
    """Kamino :class:`Simulator`-like wrapper initialized from a Newton :class:`~newton.Model`.

Mirrors the core API of the Kamino ``Simulator`` class but accepts an
already-finalized :class:`newton.Model` instead of a ``ModelBuilderKamino``.
Internally uses :meth:`ModelKamino.from_newton` to obtain Kamin"""
    def __init__(self, newton_model, config, use_newton_collisions)
    def model(self)
    def state(self)
    def state_previous(self)
    def control(self)
    def contacts(self)
    def collision_detector(self)
    def solver(self)
    def _run_newton_collision(self, state_kamino)
    def step(self)
    def reset(self)
class RigidBodySim()
    """Generic Kamino rigid body simulator for RL.

Features:
    * USD model loading via ``newton.ModelBuilder.add_usd``
    * ``ModelKamino.from_newton`` for Kamino-native state/control layout
    * Configurable solver settings with sensible RL defaults
    * Zero-copy PyTorch views of state, control and"""
    def __init__(self, usd_model_path, num_worlds, sim_dt, device, headless, body_pose_offset, add_ground, enable_gravity, settings, use_cuda_graph, record_video, video_folder, async_save, max_contacts_per_pair, max_contacts_per_world, render_config, collapse_fixed_joints, terrain_fn, scene_callback)
    def _apply_render_config(self, cfg)
    def _make_rl_interface(self)
    def _extract_metadata(self)
    def _capture_graphs(self)
    def step(self)
    def reset(self)
    def apply_resets(self)
    def _reset_worlds(self)
    def render(self)
    def _capture_frame(self)
    def generate_video(self, output_filename, fps, keep_frames)
    def time(self)
    def is_running(self)
    def set_dof(self, dof_positions, dof_velocities, env_ids)
    def set_root(self, root_positions, root_orientations, root_linear_velocities, root_angular_velocities, env_ids)
    def q_j(self)
    def dq_j(self)
    def q_i(self)
    def u_i(self)
    def q_j_ref(self)
    def dq_j_ref(self)
    def tau_j_ref(self)
    def contact_flags(self)
    def ground_contact_flags(self)
    def net_contact_forces(self)
    def body_pair_contact_flag(self)
    def set_body_pair_contact_filter(self, body_a_name, body_b_name)
    def compute_body_pair_contacts(self)
    def num_worlds(self)
    def num_joint_coords(self)
    def num_joint_dofs(self)
    def num_bodies(self)
    def joint_names(self)
    def body_names(self)
    def actuated_joint_names(self)
    def actuated_coord_indices(self)
    def actuated_coord_indices_tensor(self)
    def actuated_dof_indices(self)
    def actuated_dof_indices_tensor(self)
    def num_actuated(self)
    def env_origins(self)
    def external_wrenches(self)
    def body_masses(self)
    def default_q_j(self)
    def joint_limits(self)
    def torch_device(self)
    def device(self)
    def sim_dt(self)
    def world_mask(self)
    def find_body_index(self, name)
    def find_body_indices(self, names)
    def default_settings(sim_dt)
```

### newton/_src/solvers/kamino/examples/rl/simulation_runner.py

```
"""Sync / async simulation loop for RL examples.

In **sync** mode the viewer and physics run in lockstep on the main thread
(the current default behavior).

In **async** mode the GPU physics + policy inference run as fast as possible
on a background thread while the main thread handles viewer rendering and
joystick polling at fixed rates.  OpenGL must stay on the thread that created
the context, so rendering always happens on the main thread."""
class SimulationRunner()
    """Run an RL example in sync or async mode.

Args:
    example: An ``Example`` instance (must expose ``step``, ``sim_step``,
        ``update_input``, ``reset``, ``render``, ``joystick``, and
        ``sim_wrapper``).
    mode: ``"sync"`` (default) or ``"async"``.
    render_fps: Target rendering rate """
    def __init__(self, example, mode, render_fps, joystick_hz)
    def run(self)
    def _run_sync(self)
    def _run_async(self)
    def _main_thread_loop(self)
    def _sim_thread_fn(self)
```

### newton/_src/solvers/kamino/examples/rl/test_multi_env_dr_legs.py

```
def make_settings(sim_dt)
def run_test(num_worlds, num_steps, device)
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_all_geoms.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_all_joints.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_box_on_plane.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def _advance_time(self)
    def _apply_actuation(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_box_pendulum.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_boxes_hinged.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def _advance_time(self)
    def _apply_actuation(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_boxes_nunchaku.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/_src/solvers/kamino/examples/sim/example_kamino_basic_cartpole.py

```
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def _advance_time(self)
    def _apply_actuation(self)
    def create_parser()
```

### newton/_src/solvers/kamino/tests/test_utils_sim_simulator.py

```
"""Unit tests for the high-level Simulator class utility of Kamino"""
def _test_control_callback(model_dt, data_time, control_tau_j)
def test_control_callback(sim)
class TestCartpoleSimulator(TestCase)
    def setUp(self)
    def tearDown(self)
    def test_01_step_multiple_cartpoles_all_from_initial_state(self)
    def test_02_step_multiple_cartpoles_reset_all_from_sampled_states(self)
```

### newton/examples/diffsim/example_diffsim_ball.py

```
def loss_kernel(pos, target, loss)
def step_kernel(x, grad, alpha)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def forward_backward(self)
    def forward(self)
    def simulate(self, sim_step)
    def step(self)
    def test_final(self)
    def render(self)
    def check_grad(self)
    def create_parser()
```

### newton/examples/diffsim/example_diffsim_bear.py

```
def loss_kernel(com, loss)
def com_kernel(velocities, n, com)
def compute_phases(phases, sim_time)
def tanh(x)
def network(phases, weights, tet_activations)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def forward_backward(self)
    def forward(self, frame)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/examples/diffsim/example_diffsim_cloth.py

```
def com_kernel(positions, n, com)
def loss_kernel(com, target, loss)
def step_kernel(x, grad, alpha)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def forward_backward(self)
    def forward(self)
    def simulate(self, sim_step)
    def step(self)
    def test_final(self)
    def render(self)
    def create_parser()
```

### newton/examples/diffsim/example_diffsim_drone.py

```
class Propeller()
def increment_seed(seed)
def sample_gaussian(mean_trajectory, noise_scale, num_control_points, control_dim, control_limits, seed, rollout_trajectories)
def replicate_states(body_q_in, body_qd_in, bodies_per_world, body_q_out, body_qd_out)
def drone_cost(body_q, body_qd, targets, prop_control, step, horizon_length, weighting, cost)
def collision_cost(body_q, obstacle_ids, shape_X_bs, shape_type, shape_scale, shape_source_ptr, margin, weighting, cost)
def enforce_control_limits(control_limits, control_points)
def pick_best_trajectory(rollout_trajectories, lowest_cost_id, best_traj)
def interpolate_control_linear(control_points, control_dofs, control_gains, t, torque_dim, torques)
def compute_prop_wrenches(props, controls, body_q, body_com, body_f)
def define_propeller(drone, pos, fps, thrust, power, diameter, height, max_rpm, turning_direction)
class Drone()
    def __init__(self, name, fps, trajectory_shape, variation_count, size, requires_grad, state_count)
    def state(self)
    def next_state(self)
    def control(self)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def forward_backward(self)
    def update_drone(self, drone, solver)
    def forward(self)
    def step_optimizer(self)
    def step(self)
    def test_final(self)
    def render(self)
    def create_parser()
```

### newton/examples/diffsim/example_diffsim_soft_body.py

```
def assign_param(params, tet_materials)
def com_kernel(particle_q, com)
def loss_kernel(target, com, pos_error, loss)
def enforce_constraint_kernel(lower_bound, upper_bound, x)
class Example()
    def __init__(self, viewer, args)
    def create_model(self)
    def capture(self)
    def forward_backward(self)
    def forward(self)
    def simulate(self, sim_step)
    def step(self)
    def log_step(self)
    def test_final(self)
    def render(self)
    def create_parser()
```

### newton/examples/diffsim/example_diffsim_spring_cage.py

```
def compute_loss_kernel(pos, target_pos, loss)
def apply_gradient_kernel(spring_rest_lengths_grad, train_rate, spring_rest_lengths)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def forward_backward(self)
    def forward(self)
    def simulate(self, sim_step)
    def check_grad(self)
    def test_final(self)
    def step(self)
    def render(self)
    def create_parser()
```

### newton/examples/robot/example_robot_allegro_hand.py

```
def move_hand(joint_q_start, joint_limit_lower, joint_limit_upper, sim_time, sim_dt, hand_rotation, joint_target_q, joint_parent_xform)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()
```

### newton/examples/robot/example_robot_policy.py

```
class RobotConfig()
    """Configuration for a robot including asset paths and policy paths."""
def _compute_obs_kernel(joint_q, joint_qd, joint_pos_initial, physx_to_mjc_idx, gravity_w, command, prev_act, num_dofs, obs)
def _build_joint_target_q_kernel(act, joint_pos_initial, reorder, action_scale, num_prefix_zeros, out)
def load_policy_and_setup_arrays(example, policy_path, num_dofs, joint_pos_slice)
def find_physx_mjwarp_mapping(mjwarp_joint_names, physx_joint_names)
class Example()
    def __init__(self, viewer, args)
    def capture(self)
    def simulate(self)
    def reset(self)
    def step(self)
    def render(self)
    def test_final(self)
    def create_parser()

```python
def _compute_obs_kernel(
    joint_q: wp.array[float],
    joint_qd: wp.array[float],
    joint_pos_initial: wp.array[float],
    physx_to_mjc_idx: wp.array[int],
    gravity_w: wp.vec3,
    command: wp.vec3,
    prev_act: wp.array2d[float],
    num_dofs: int,
    obs: wp.array2d[float],
):
    q = wp.quat(joint_q[3], joint_q[4], joint_q[5], joint_q[6])

    lin_w = wp.vec3(joint_qd[0], joint_qd[1], joint_qd[2])
    ang_w = wp.vec3(joint_qd[3], joint_qd[4], joint_qd[5])

    vel_b = wp.quat_rotate_inv(q, lin_w)
    avel_b = wp.quat_rotate_inv(q, ang_w)
    grav_b = wp.quat_rotate_inv(q, gravity_w)

    obs[0, 0] = vel_b[0]
    obs[0, 1] = vel_b[1]
    obs[0, 2] = vel_b[2]
    obs[0, 3] = avel_b[0]
    obs[0, 4] = avel_b[1]
    obs[0, 5] = avel_b[2]
    obs[0, 6] = grav_b[0]
    obs[0, 7] = grav_b[1]
    obs[0, 8] = grav_b[2]
    obs[0, 9] = command[0]
    obs[0, 10] = command[1]
    obs[0, 11] = command[2]

    for k in range(num_dofs):
        idx = physx_to_mjc_idx[k]
        obs[0, 12 + k] = joint_q[7 + idx] - joint_pos_initial[idx]
        obs[0, 12 + num_dofs + k] = joint_qd[6 + idx]
        obs[0, 12 + 2 * num_dofs + k] = prev_act[0, k]
```
```

### newton/examples/robot/onnx_policy_utils.py

```
def _require_onnx()
def _tensor_shape(value_info)
def _find_value_info(values, name)
def _format_shape(shape)
def _validate_policy_tensor_shape(shape)
def validate_policy_io_shapes(policy_path, input_name, output_name)
```

### newton/tests/kamino/test_kamino_kinematics_constraints.py

```
"""KAMINO: UNIT TESTS: KINEMATICS: CONSTRAINTS"""
class TestKinematicsConstraints(TestCase)
    def setUp(self)
    def tearDown(self)
    def test_01_single_model_make_constraints(self)
    def test_02_homogeneous_model_make_constraints(self)
    def test_03_heterogeneous_model_make_constraints(self)
```

### newton/tests/kamino/utils/solver_configs.py

```
"""Common SolverKamino configuration presets for integration tests."""
def make_single_iteration_config(config_factory)
def make_padmm_dense_config()
def make_padmm_sparse_config()
def make_dvi_dense_config()
def make_dvi_sparse_config()
```

### newton/tests/test_environment_group_collision.py

```
class TestEnvironmentGroupCollision(TestCase)
    """Test world group collision filtering functionality."""
    def setUp(self)
    def test_shape_collision_filtering(self)
    def test_particle_shape_collision_filtering(self)
    def test_add_world_groups(self)
    def test_mixed_collision_and_world_groups(self)
    def test_collision_filter_pair_canonicalization(self)
class TestWorldGroupBroadphaseKernels(TestCase)
    """Test the broadphase kernels with world group filtering."""
    def test_test_world_and_group_pair(self)
```

### newton/tests/test_equality_connect_constraint_with_sim_step.py

```
"""Tests for joint equality constraints verified with simulation steps."""
class Sim()
    """Holds the simulation objects for a single test."""
    def __init__(self, model, solver, state_in, state_out, control)
def connect_residual(body_poses, connect_body_indices, leafbody1_anchor, leafbody2_anchor)
class TestEqualityConstraintWithSimStepBase()
    def _create_solver(self, model)
    def _num_worlds(self)
    def _use_mujoco_cpu(self)
    def _inertia_matrix()
    def _new_mujoco_builder()
    def _finalize_sim(self, all_worlds_builder)
    def _add_scalar_joint(builder, joint_type)
class TestConnectConstraintWithSimStepBase(TestEqualityConstraintWithSimStepBase)
    """Test that a CONNECT equality constraint pins two bodies at a point."""
    def _build_connect_model(self, connect_body_indices, connect_anchor_leafbody1, joint_types, joint_axes, joint_dof_refs, num_worlds)
    def compute_joint_transform(self, joint_axis, joint_pos, joint_type)
    def compute_expected_leafbody2_anchor(self, joint_axes, ref_joint_q, joint_types, connect_anchor_leafbody1)
    def _test_connect_constraint(self)
    def test_connect_constraint(self)
class TestConnectConstraintJointMuJoCoWarp(TestConnectConstraintWithSimStepBase, TestCase)
    def _num_worlds(self)
    def _use_mujoco_cpu(self)
    def _create_solver(self, model)
class TestConnectConstraintJointMuJoCoCPU(TestConnectConstraintWithSimStepBase, TestCase)
    def _num_worlds(self)
    def _use_mujoco_cpu(self)
    def _create_solver(self, model)
class TestLoopJointConnectConstraintBase(TestEqualityConstraintWithSimStepBase)
    """Test loop-joint-synthesized CONNECT anchors at the authored reference pose.

A revolute loop joint closes an articulation back to its root and creates two CONNECT constraints. Its anchors
must remain unchanged when dof_ref changes but be recomputed when joint_X_p changes."""
    def _build_loop_joint_model(self, loop_joint_axis, joint0_axis, joint1_axis, joint0_type, joint1_type, dof_refs, num_worlds)
    def _compute_loop_joint_expected_anchors(self, joint_X_p_np, joint_X_c_np, joint_axis_np, joint_qd_start_np, joint0_idx, joint1_idx, loop_joint_idx)
    def _assert_loop_joint_eq_data(self, sim, w, anchor1_a, anchor2_a, anchor1_b, anchor2_b)
    def _test_loop_joint_connect_constraint(self)
    def test_loop_joint_connect_constraint(self)
class TestLoopJointConnectConstraintMuJoCoWarp(TestLoopJointConnectConstraintBase, TestCase)
    def _create_solver(self, model)
class TestLoopJointConnectConstraintMuJoCoCPU(TestLoopJointConnectConstraintBase, TestCase)
    def _create_solver(self, model)
class TestMixedWeldAndConnectLoopJointBase(TestEqualityConstraintWithSimStepBase)
    """Test that WELD (FIXED) loop joint eq_data is not corrupted by CONNECT kernel updates.

Creates a model with both a revolute loop joint (2 CONNECT constraints) and
a FIXED loop joint (1 WELD constraint).  Verifies that after
``notify_model_changed(JOINT_DOF_PROPERTIES)`` the WELD constraint's
``eq_da"""
    def _build_mixed_weld_and_connect_model(self, num_worlds)
    def test_weld_eq_data_not_corrupted_by_connect_update(self)
class TestMixedWeldAndConnectMuJoCoWarp(TestMixedWeldAndConnectLoopJointBase, TestCase)
    def _create_solver(self, model)
class TestMixedWeldAndConnectMuJoCoCPU(TestMixedWeldAndConnectLoopJointBase, TestCase)
    def _create_solver(self, model)
class TestConnectAnchorRefPoseBase(TestEqualityConstraintWithSimStepBase)
    """Keep CONNECT anchors tied to the authored reference pose.

Since ``qpos = joint_q + ref``, nonzero ``mujoco:dof_ref`` values do not move the reference pose used for
``anchor2``. The joint frames deliberately include translation and rotation so ``anchor2`` differs from
``anchor1`` there."""
    def _joint_xforms(self)
    def _build_model(self, anchor_body_b, dof_refs, num_worlds)
    def _expected_anchor2(self, anchor_body_b)
    def test_connect_anchors_at_reference_pose(self)
class TestConnectAnchorRefPoseMuJoCoWarp(TestConnectAnchorRefPoseBase, TestCase)
    def _num_worlds(self)
    def _use_mujoco_cpu(self)
    def _create_solver(self, model)
class TestConnectAnchorRefPoseMuJoCoCPU(TestConnectAnchorRefPoseBase, TestCase)
    def _num_worlds(self)
    def _use_mujoco_cpu(self)
    def _create_solver(self, model)
```

### newton/tests/test_equality_constraints.py

```
def _eq_value(builder, name, idx)
class TestEqualityConstraints(TestCase)
    def test_eq_type_deprecation(self)
    def test_equality_constraint_references_use_namespaced_frequency(self)
    def test_multiple_constraints(self)
    def test_target_and_objtype_defaults(self)
    def test_equality_constraints_not_duplicated_per_world(self)
    def test_add_builder_preserves_sparse_attribute_alignment(self)
    def test_zero_constraint_model_exposes_shape_stable_equality_arrays(self)
    def test_default_equality_constraint_torquescale_is_numeric(self)
    def test_collapse_fixed_joints_with_equality_constraints(self)
    def test_collapse_fixed_joints_sparse_optional_fields(self)
```

### newton/tests/test_softbody_simulation.py

```
def _build_soft_grid(device)
def _make_solver(model, solver_name)
def _tet_volumes(q, tet_indices)
def _step(model, solver, state_0, state_1, steps, dt)
def _assert_finite_state(test, q, qd)
def test_soft_grid_free_fall(test, device, solver_name)
def test_soft_grid_anchored_deforms(test, device, solver_name)
class TestSoftBodySimulation(TestCase)
```

### newton/tests/test_warp_config_cli.py

```
"""Tests for the ``--warp-config KEY=VALUE`` CLI option."""
class TestWarpConfigCLI(TestCase)
    """Tests for :func:`_apply_warp_config`."""
    def setUp(self)
    def tearDown(self)
    def _parse(self)
    def test_no_overrides(self)
    def test_int_override(self)
    def test_string_fallback(self)
    def test_bool_override(self)
    def test_deprecated_log_config_keys_error(self)
    def test_none_override(self)
    def test_empty_string_override(self)
    def test_repeated_overrides(self)
    def test_unknown_key_errors(self)
    def test_missing_equals_errors(self)
    def test_parser_has_warp_config_arg(self)
    def test_default_warp_config_empty(self)
    def test_quiet_preserves_stricter_log_level(self)
```

### scripts/ci/discover_aws_runner_config.py

```
"""Discover AWS EC2 runner networking for GitHub Actions.

The script is designed to run inside EC2-backed GPU GitHub Actions workflows
after AWS credentials are configured. It writes one GitHub Actions step output:

``availability-zones-config``
    JSON array passed to ``machulav/ec2-github-runner``."""
def warning(message)
def error(message)
def print_aws_cli_output(label, output)
def aws(region)
def allows_outbound_internet(security_group)
def discover_candidates(regions, instance_type, tag_key, aws_call, warn)
def set_output(name, value)
def main()
```