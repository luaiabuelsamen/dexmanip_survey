# genesis_2024

source: https://github.com/Genesis-Embodied-AI/Genesis


commit: c27875eb56947808b3105d25d3c09b6dd96484b3


## README

![Genesis World teaser](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/HeroShot_Final.png)

# Genesis World

[![PyPI - Version](https://img.shields.io/pypi/v/genesis-world)](https://pypi.org/project/genesis-world/)
[![PyPI Downloads](https://static.pepy.tech/badge/genesis-world)](https://pepy.tech/projects/genesis-world)
[![Documentation](https://app.readthedocs.org/projects/genesis-world/badge/?version=latest)](https://genesis-world.readthedocs.io/en/latest/)
[![GitHub Issues](https://img.shields.io/github/issues/Genesis-Embodied-AI/genesis-world)](https://github.com/Genesis-Embodied-AI/genesis-world/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/Genesis-Embodied-AI/genesis-world)](https://github.com/Genesis-Embodied-AI/genesis-world/discussions)



**Genesis World** is a simulation platform for physical AI developments. It combines a unified multi-physics engine, a photo-realistic renderer ([Nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)), and a cross-platform compiler ([Quadrants](https://github.com/Genesis-Embodied-AI/quadrants)) behind a Pythonic simulation interface. Genesis World is designed to scale from a single laptop kernel to datacenter-grade GPUs, while remaining easy to read, extend, and embed in research code.

It was previously named **Genesis** and started as an academic project since Dec 2024, and its development is now officially supported by [Genesis AI](https://www.genesis.ai/).

For more technical details, refer to our [blog post](https://genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward).

## Table of Contents

1. [What is Genesis World?](#what-is-genesis-world)
2. [Catalogue](#catalogue)
3. [Quick Installation](#quick-installation)
4. [Contribution](#contributing-to-genesis)
5. [Support](#support)
6. [License and Acknowledgments](#license-and-acknowledgments)
7. [Citation](#citation)

## What is Genesis World?

![Genesis World stack](https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/diagram_white_lum.png)

Genesis World occupies the four layers inside the dashed box. Above sits whatever you build (robotics environments, ML pipelines, data generation, agentic simulation); below sits whatever compute backend you have.

- **Simulation Interface** — the user-facing API: asset parsing (URDF, MJCF, OBJ, GLB, USD, …), entity accessors, controllers, sensors, parallel and heterogeneous environments, and a built-in GUI.
- **Physics** — a unified multi-physics engine integrating Rigid, FEM, MPM, Particle (PBD / SPH), [uipc](https://github.com/spiriMirror/libuipc), an explicit coupler, and SAP, all sharing one scene and one state.
- **Render** — three rendering paths plug in as camera sensors: **[Nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)** (our in-house renderer designed for robotics), Luisa (DSL ray tracer), and Pyrender (rasterizer).
- **Compiler** — **[Quadrants](https://github.com/Genesis-Embodied-AI/quadrants)** lowers Python kernel code to CUDA, AMD ROCm, Apple Metal, Vulkan, x86, and ARM64. It carries Genesis's autodiff, GPU graphs, and fastcache machinery.

### Documentation
- [Genesis World](https://genesis-world.readthedocs.io/en/latest/)
- [Quadrants](https://genesis-embodied-ai.github.io/quadrants/index.html)
- [Nyx](https://genesis-embodied-ai.github.io/genesis-nyx/latest/)

## Catalogue

Three sections, mirroring the Genesis layers that ship runnable demos: **Physics** (solvers and multi-solver coupling), **Rendering** (in-repo camera setups plus the Nyx walkthroughs hosted in [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx)), and **Simulation Interface** (sensors, GUI, controllers, parallel/heterogeneous envs, and tutorials). Most scripts run end-to-end after `pip install -e ".[dev]"`; demos that depend on optional backends (e.g. the IPC and Nyx examples) need the extras listed in [Optional extras](#optional-extras).

### Physics

| | | |
|---|---|---|
| [Rigid: franka cube](./examples/rigid/franka_cube.py) | [Rigid: collision tower](./examples/collision/tower.py) | [Rigid: contype](./examples/collision/contype.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_franka_cube.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_tower.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contype.webp" width="240"> |
| [FEM: hard & soft constraint](./examples/deformable/fem_hard_and_soft_constraint.py) | [MPM: tutorial](./examples/tutorials/mpm.py) | [MPM: sand wheel](./examples/coupling/sand_wheel.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/fem_hard_and_soft_constraint.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_mpm.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sand_wheel.webp" width="240"> |
| [SPH: rigid](./examples/coupling/sph_rigid.py) | [SPH: + MPM](./examples/coupling/sph_mpm.py) | [PBD: liquid](./examples/deformable/pbd_liquid.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_rigid.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_sph_mpm.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/pbd_liquid.webp" width="240"> |
| [PBD: cloth](./examples/tutorials/pbd_cloth.py) | [Stable Fluid: smoke](./examples/fluid/smoke.py) | [IPC: robot cloth teleop](./examples/ipc/ipc_robot_cloth_teleop.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_pbd_cloth.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/smoke.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/ipc_cloth_teleop.webp" width="240"> |
| [Coupler: cloth on rigid](./examples/coupling/cloth_on_rigid.py) | [Coupler: rigid + MPM](./examples/coupling/rigid_mpm_attachment.py) | [Coupler: cut dragon](./examples/coupling/cut_dragon.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cloth_on_rigid.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_rigid_mpm_attachment.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cut_dragon.webp" width="240"> |
| [Coupler: water wheel](./examples/coupling/water_wheel.py) | [Coupler: flush cubes](./examples/coupling/flush_cubes.py) | [SAP: Franka grasp rigid cube](./examples/sap_coupling/franka_grasp_rigid_cube.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_water_wheel.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_flush_cubes.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_franka_grasp_rigid_cube.webp" width="240"> |
| [Rigid: contact patch](./examples/collision/contact_manifold.py) | | |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_contact_manifold.webp" width="240"> | | |

### Rendering

Genesis exposes three rendering paths as camera sensors: built-in (Nyx / Luisa / Pyrender) and detailed Nyx walkthroughs hosted in [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx/tree/main/examples).

| | | |
|---|---|---|
| [Follow entity](./examples/rendering/follow_entity.py) | [Animated camera](./examples/rendering/moving_camera.py) | [Nyx: hello](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/01_hello_nyx.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_follow_entity.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rendering_moving_camera.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_01_hello_nyx.png" width="240"> |
| [Nyx: attached camera](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/02_attached_camera.py) | [Nyx: PBR materials](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/03_materials.py) | [Nyx: light types](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/04_light_types.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_02_attached_camera.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_03_materials.png" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_04_light_types.png" width="240"> |
| [Nyx: 3D Gaussian splat](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/05_gaussian_splat.py) | [Nyx: object picking](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/06_object_picking.py) | [Nyx: multi-cam multi-env](https://github.com/Genesis-Embodied-AI/genesis-nyx/blob/main/examples/07_multi_camera_multi_env.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_05_gaussian_splat.png" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_06_object_picking.png" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/nyx_07_multi_camera_multi_env.png" width="240"> |

### Simulation Interface

| | | |
|---|---|---|
| [Controlling a robot](./examples/tutorials/control_your_robot.py) | [GUI: ImGui joint control](./examples/gui/imgui_joint_control.py) | [Heterogeneous envs](./examples/rigid/heterogeneous_simulation.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_control_your_robot.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/gui_imgui_joint_control.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/het_articulated.webp" width="240"> |
| [Domain randomization](./examples/rigid/domain_randomization.py) | [Sensor: depth camera](./examples/sensors/depth_camera_custom_vverts.py) | [Sensor: IMU](./examples/sensors/imu_franka.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_domain_randomization.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_depth_camera_custom_vverts.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_imu_franka.webp" width="240"> |
| [Sensor: lidar](./examples/sensors/lidar_teleop.py) | [Sensor: tactile sandbox](./examples/sensors/tactile_sandbox.py) | [Sensor: contact force](./examples/sensors/contact_force_go2.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_lidar_teleop.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_tactile_sandbox.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_contact_force_go2.webp" width="240"> |
| [Sensor: surface distance](./examples/sensors/surface_distance_shadowhand.py) | [Sensor: temperature grid](./examples/sensors/temperature_grid.py) | [GUI: debug drawing](./examples/tutorials/draw_debug.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_surface_distance_shadowhand.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sensors_temperature_grid.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_draw_debug.webp" width="240"> |
| [GUI: mesh point picker](./examples/viewer_plugin/mesh_point_selector.py) | [GUI: mouse interaction](./examples/viewer_plugin/mouse_interaction.py) | [Diff-IK controller](./examples/rigid/diffik_controller.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mesh_point_selector.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/viewer_mouse_interaction.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_diffik_controller.webp" width="240"> |
| [Batched IK](./examples/tutorials/batched_IK.py) | [Drone](./examples/drone/hover_train.py) | [Advanced: worm](./examples/tutorials/advanced_worm.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_batched_IK.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/drone_hover_train.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_advanced_worm.webp" width="240"> |

## Quick Installation

### Using pip

Install **PyTorch** first following the [official instructions](https://pytorch.org/get-started/locally/).

Then, install Genesis via PyPI:
```bash
pip install genesis-world  # Requires Python>=3.10,<3.14;
```

For the latest version to date, make sure that `pip` is up-to-date via `pip install --upgrade pip`, then run command:
```bash
pip install git+https://github.com/Genesis-Embodied-AI/genesis-world.git
```
Note that the package must still be updated manually to sync with main branch.

Users seeking to contribute are encouraged to install Genesis in editable mode. First, make sure that `genesis-world` has been uninstalled, then clone the repository and install locally:
```bash
git clone https://github.com/Genesis-Embodied-AI/genesis-world.git
cd genesis-world
pip install -e ".[dev]"
```
It is recommended to systematically execute `pip install -e ".[dev]"` after moving HEAD to make sure that all dependencies and entrypoints are up-to-date.

### Optional extras

| | |
|---|---|
| IPC solver (uipc backend) | `pip install pyuipc` *(Linux / Windows x86, NVIDIA GPU)* |
| Nyx renderer | `pip install gs-nyx` — see [genesis-nyx](https://github.com/Genesis-Embodied-AI/genesis-nyx) |

Quadrants is bundled with Genesis automatically; no extra install. The standalone wheel (`pip install quadrants`) is documented at [Quadrants](https://github.com/Genesis-Embodied-AI/quadrants) for users who want the compiler outside Genesis.

### Using uv

[uv](https://docs.astral.sh/uv/) is a fast Python package and project manager.

**Install uv:**
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Quick start with uv:**
```bash
git clone https://github.com/Genesis-Embodied-AI/genesis-world.git
cd genesis-world
uv sync
```

Then install PyTorch for your platform:

```bash
# NVIDIA GPU (CUDA 12.6 as an example)
uv pip install torch --index-url https://download.pytorch.org/whl/cu126

# CPU only (Linux/Windows)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu

# Apple Silicon (Metal/MPS)
uv pip install torch
```

Run an example:
```bash
uv run examples/rigid/single_franka.py
```

## Contributing to Genesis

The Genesis project is an open and collaborative effort. We welcome all forms of contributions from the community, including:

- **Pull requests** for new features or bug fixes.
- **Bug reports** through GitHub Issues.
- **Suggestions** to improve Genesis's usability.

Refer to our [contribution guide](https://github.com/Genesis-Embodied-AI/genesis-world/blob/main/.github/contributing/PULL_REQUESTS.md) for more details.

## Support

- Report bugs or request features via GitHub [Issues](https://github.com/Genesis-Embodied-AI/genesis-world/issues).
- Join discussions or ask questions on GitHub [Discussions](https://github.com/Genesis-Embodied-AI/genesis-world/discussions).

## License and Acknowledgments

The Genesis source code is licensed under Apache 2.0.

Genesis's development has been made possible thanks to these open-source projects:

- [Taichi](https://github.com/taichi-dev/taichi): the original compiler that [Quadrants](https://github.com/Genesis-Embodied-AI/quadrants) forked from in June 2025. Kudos to the Taichi team for their technical support over the years.
- [libuipc](https://github.com/spiriMirror/libuipc): IPC solver backend.
- [FluidLab](https://github.com/zhouxian/FluidLab): Reference MPM solver implementation.
- [SPH_Taichi](https://github.com/erizmr/SPH_Taichi): Reference SPH solver implementation.
- [Ten Minute Physics](https://matthias-research.github.io/pages/tenMinutePhysics/index.html) and [PBF3D](https://github.com/WASD4959/PBF3D): Reference PBD solver implementations.
- [MuJoCo](https://github.com/google-deepmind/mujoco): Reference for rigid body dynamics.
- [libccd](https://github.com/danfis/libccd): Reference for collision detection.
- [PyRender](https://github.com/mmatl/pyrender): Rasterization-based renderer.
- [LuisaCompute](https://github.com/LuisaGroup/LuisaCompute) and [LuisaRender](https://github.com/LuisaGroup/LuisaRender): Ray-tracing DSL.
- [Madrona](https://github.com/shacklettbp/madrona) and [Madrona-mjx](https://github.com/shacklettbp/madrona_mjx): Batch renderer backend

## Citation

If you use Genesis in your research, please consider citing:

```bibtex
@article{
   genesis2026genesisworld,
   author = {Genesis AI Team},
   title = {The Role of Simulation in Scalable Robotics, Genesis World 1.0, and the Path Forward},
   journal = {Genesis AI Blog},
   month = {May},
   year = {2026},
   url = {https://www.genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward},
}
```
```bibtex
@misc{
  Genesis,
  author = {Genesis Authors},
  title = {Genesis: A Generative and Universal Physics Engine for Robotics and Beyond},
  month = {December},
  year = {2024},
  url = {https://github.com/Genesis-Embodied-AI/genesis-world}
}
```
<!--
Catalogue entries pruned from the Physics grid. Kept here as a reference so
they can be reinstated later. The links and thumbnail paths are all still
valid in the repo; just paste any pair of rows back into the Physics table.

| [Rigid: grasp bottle](./examples/rigid/grasp_bottle.py) | [Rigid: collision pyramid](./examples/collision/pyramid.py) | [FEM: elastic dragon](./examples/deformable/elastic_dragon.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_grasp_bottle.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/collision_pyramid.png" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/elastic_dragon.webp" width="240"> |
| [FEM: SAP fixed constraint](./examples/sap_coupling/fem_fixed_constraint.py) | [SPH: liquid](./examples/tutorials/sph_liquid.py) | [Coupler: grasp soft cube](./examples/coupling/grasp_soft_cube.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_fem_fixed_constraint.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_sph_liquid.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_grasp_soft_cube.webp" width="240"> |
| [Coupler: cloth + rigid](./examples/coupling/cloth_attached_to_rigid.py) | [SAP: Franka grasp FEM sphere](./examples/sap_coupling/franka_grasp_fem_sphere.py) | [SAP: FEM sphere + cube](./examples/sap_coupling/fem_sphere_and_cube.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/coupling_cloth_attached_to_rigid.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_franka_grasp_fem_sphere.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/sap_fem_sphere_and_cube.webp" width="240"> |

Pruned from Simulation Interface (same logic — labels/paths still valid):

| [Entity name](./examples/tutorials/entity_name.py) | [Select rendered envs](./examples/tutorials/selecting_rendered_envs.py) | [GUI: keyboard teleop](./examples/viewer_plugin/keyboard_teleop.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_entity_name.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_selecting_rendered_envs.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/keyboard_teleop.webp" width="240"> |
| [Control franka](./examples/rigid/control_franka.py) | [Position control comparison](./examples/tutorials/position_control_comparison.py) | [IK + motion planning](./examples/tutorials/IK_motion_planning_grasp.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_control_franka.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_position_control_comparison.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_IK_motion_planning_grasp.webp" width="240"> |
| [Close kinematic chain](./examples/rigid/closed_loop.py) | [Advanced: muscle](./examples/tutorials/advanced_muscle.py) | [Advanced: hybrid robot](./examples/tutorials/advanced_hybrid_robot.py) |
| <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/rigid_closed_loop.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_advanced_muscle.webp" width="240"> | <img src="https://raw.githubusercontent.com/Genesis-Embodied-AI/genesis-world/readme-assets/videos/tutorials_advanced_hybrid_robot.webp" width="240"> |
-->


## File tree (depth 3, assets pruned)

```
.gitattributes
.github/
  CODEOWNERS
  ISSUE_TEMPLATE/
    1-bug-report.yml
    2-feature-request.yml
    3-documentation.yml
    config.yml
  contributing/
    ARCHITECTURE.md
    CODING_CONVENTIONS.md
    EXAMPLES.md
    PULL_REQUESTS.md
    TESTING.md
    USD_PARSER.md
  genesis_image_ver
  nyx_plugin_commit
  pull_request_template.md
  workflows/
    alarm.yml
    examples.yml
    format.yml
    generic.yml
    nyx_plugin.yml
    production.yml
    scripts/
.gitignore
.gitmodules
.pre-commit-config.yaml
.readthedocs.yaml
CLAUDE.md
CODING_GUIDELINES.md
LICENSE
MANIFEST.in
README.md
RELEASE.md
doc/
examples/
  collision/
    contact_manifold.py
    contype.py
    pyramid.py
    tower.py
  coupling/
    cloth_attached_to_rigid.py
    cloth_on_rigid.py
    cut_dragon.py
    fem_cube_linked_with_arm.py
    flush_cubes.py
    grasp_soft_cube.py
    rigid_mpm_attachment.py
    sand_wheel.py
    sph_mpm.py
    sph_rigid.py
    water_wheel.py
  deformable/
    differentiable_push.py
    elastic_dragon.py
    fem_hard_and_soft_constraint.py
    pbd_liquid.py
  drone/
    README.md
    fly.py
    fly_route.py
    hover_env.py
    hover_eval.py
    hover_train.py
    interactive_drone.py
    quadcopter_controller.py
  fluid/
    smoke.py
  gui/
    imgui_joint_control.py
  ipc/
    README.md
    ipc_momentum.py
    ipc_objects_falling.py
    ipc_robot_cloth_teleop.py
    ipc_robot_grasp_cube.py
  kinematic/
    go2_kinematic.py
  locomotion/
    backflip/
    go2_backflip.py
    go2_env.py
    go2_eval.py
    go2_train.py
  manipulation/
    behavior_cloning.py
    grasp_env.py
    grasp_eval.py
    grasp_train.py
  rendering/
    demo.py
    follow_entity.py
    moving_camera.py
    render_async.py
    speed_test.py
  rigid/
    accelerometer_duck.py
    accelerometer_franka.py
    apply_external_wrench.py
    authored_decomp.py
    bolt_nut_self_screw.py
    closed_loop.py
    control_franka.py
    control_mesh.py
    convex_decomposition.py
    ddp_multi_gpu.py
    diffik_controller.py
    domain_randomization.py
    franka_cube.py
    friction_breakaway.py
    grasp_bottle.py
    gravity_compensation.py
    heterogeneous_simulation.py
    hibernation.py
    ik_custom_chain.py
    ik_duck.py
    ik_franka.py
    ik_franka_batched.py
    ik_shadow_hand.py
    merge_entities.py
    multi_gpu.py
    nonconvex_mesh.py
    rolling_coast.py
    set_phys_attr.py
    single_franka.py
    single_franka_batch_render.py
    single_franka_envs.py
    suction_cup.py
    terrain_from_mesh.py
    terrain_height_field.py
    terrain_subterrain.py
    torsional_grasp.py
    wrecking_ball.py
  sap_coupling/
    fem_fixed_constraint.py
    fem_sphere_and_cube.py
    franka_grasp_fem_sphere.py
    franka_grasp_rigid_cube.py
  sensors/
    camera_as_sensor.py
    contact_force_go2.py
    depth_camera_custom_vverts.py
    imu_franka.py
    joint_torque_franka.py
    lidar_teleop.py
    surface_distance_shadowhand.py
    tactile_franka.py
    tactile_sandbox.py
    temperature_grid.py
  speed_benchmark/
    anymal_c.py
    franka.py
    timers.py
  tutorials/
    IK_motion_planning_grasp.py
    advanced_IK_multilink.py
    advanced_hybrid_robot.py
    advanced_muscle.py
    advanced_worm.py
    batched_IK.py
    control_your_robot.py
    draw_debug.py
    entity_name.py
    hello_genesis.py
    interactive_debugging.py
    mpm.py
    parallel_simulation.py
    pbd_cloth.py
    position_control_comparison.py
    selecting_rendered_envs.py
    sph_liquid.py
    visualization.py
  usd/
    import_stage.py
    kitchen.py
  viewer_plugin/
    keyboard_teleop.py
    mesh_point_selector.py
    mouse_interaction.py
genesis/
  __init__.py
  _main.py
  constants.py
  datatypes.py
  engine/
    __init__.py
    boundaries/
    bvh.py
    couplers/
    entities/
    force_fields.py
    interactive_scene.py
    materials/
    mesh.py
    scene.py
    sensors/
    simulator.py
    solvers/
    states/
  ext/
    LuisaRender/
    ParticleMesher/
    VolumeSampling
    _trimesh_patch.py
    isaacgym/
    pyrender/
    urdfpy/
  grad/
    __init__.py
    creation_ops.py
    tensor.py
  logging/
    __init__.py
    logger.py
    time_elapser.py
  options/
    __init__.py
    misc.py
    morphs.py
    options.py
    profiling.py
    recorders.py
    renderers.py
    scene.py
    sensors/
    solvers.py
    surfaces.py
    textures.py
    vis.py
  recorders/
    __init__.py
    base_recorder.py
    file_writers.py
    plotters.py
    recorder_manager.py
    trajectory.py
  repr_base.py
  styles.py
  typing.py
  utils/
    __init__.py
    array_class.py
    collision.py
    deprecated_module_wrapper.py
    element.py
    emoji.py
    geom.py
    gltf.py
    hybrid.py
    image_exporter.py
    linalg.py
    mesh.py
    misc.py
    mjcf.py
    particle.py
    path_planning.py
    point_cloud.py
    raycast.py
    raycast_qd.py
    repr.py
    ring_buffer.py
    sdf.py
    serialization.py
    terrain.py
    tools.py
    uid.py
    urdf.py
    usd/
    video_encoder.py
    warnings.py
    watertighten.py
  version.py
  vis/
    __init__.py
    batch_renderer.py
    camera.py
    keybindings.py
    rasterizer.py
    rasterizer_context.py
    raytracer.py
    viewer.py
    viewer_plugins/
    visualizer.py
imgs/
  big_text.png
  logo_with_text.png
  teaser.png
pyproject.toml
tests/
  __init__.py
  benchmarks/
    __init__.py
    test_rigid.py
  conftest.py
  core/
    __init__.py
    test_backend.py
    test_bvh.py
    test_misc.py
    test_quadrants.py
    test_recorders.py
    test_surface.py
    test_utils.py
  coupling/
    __init__.py
    test_hybrid.py
    test_sph_rigid.py
  deformable/
    __init__.py
    test_fem.py
    test_muscle.py
  gpu_info.py
  grad/
    __init__.py
    conftest.py
    test_grad_tape.py
    test_hybrid_push.py
    test_rigid_collision.py
    test_rigid_constraints.py
    test_rigid_dynamics.py
    test_rigid_optim.py
    utils.py
  integration/
    __init__.py
    test_integration.py
  ipc/
    __init__.py
    test_api.py
    test_deformable.py
    test_rigid.py
    utils.py
  monitor_test_mem.py
  parsers/
    __init__.py
    conftest.py
    test_mesh.py
    test_usd.py
  particles/
    __init__.py
    test_mpm.py
    test_pbd.py
    test_sf.py
    test_sph.py
  rendering/
    __init__.py
    conftest.py
    test_batch_render.py
    test_debug_draw.py
    test_dynamic_meshes.py
    test_imgui_overlay.py
    test_interactive_viewer.py
    test_offscreen.py
  rigid/
    __init__.py
    conftest.py
    test_api.py
    test_asset_loading.py
    test_collision.py
    test_collision_nonconvex.py
    test_constraints.py
    test_control.py
    test_dynamics.py
    test_friction.py
    test_heterogeneous.py
    test_islands.py
    test_kinematics.py
    test_mujoco_parity.py
    test_narrowphase.py
    test_serialization.py
    test_sparse.py
    test_terrain.py
  sensors/
    __init__.py
    conftest.py
    test_api.py
    test_camera.py
    test_contact.py
    test_imu.py
    test_joint_torque.py
    test_raycaster.py
    test_tactile.py
    test_temperature.py
  test_examples.py
  upload_benchmarks_table_to_wandb.py
  utils/
    assertions.py
    assets.py
    collision.py
    mesh_pairs_viewer.html
    misc.py
    mujoco_parity.py
    simulators.py
```

## Config files (2)


### .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
- name: "💬 Support & Questions - Github Community Support"
  url: https://github.com/Genesis-Embodied-AI/genesis-world/discussions
  about: Please ask and answer questions here.

```

### .pre-commit-config.yaml

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

## Python signatures and reward/observation bodies (27 files)


### examples/deformable/fem_hard_and_soft_constraint.py

```
def main()
```

### examples/drone/hover_env.py

```
def gs_rand_float(lower, upper, shape, device)
class HoverEnv()
    def __init__(self, num_envs, env_cfg, obs_cfg, reward_cfg, command_cfg, show_viewer)
    def _resample_commands(self, envs_idx)
    def _at_target(self)
    def step(self, actions)
    def _update_observation(self)
    def get_observations(self)
    def reset_idx(self, envs_idx)
    def reset(self)
    def _reward_target(self)
    def _reward_smooth(self)
    def _reward_yaw(self)
    def _reward_angular(self)
    def _reward_crash(self)

```python
def _update_observation(self):
        self.obs_buf = torch.cat(
            [
                torch.clip(self.rel_pos * self.obs_scales["rel_pos"], -1, 1),
                self.base_quat,
                torch.clip(self.base_lin_vel * self.obs_scales["lin_vel"], -1, 1),
                torch.clip(self.base_ang_vel * self.obs_scales["ang_vel"], -1, 1),
                self.last_actions,
            ],
            axis=-1,
        )
```

```python
def get_observations(self):
        return TensorDict({"policy": self.obs_buf}, batch_size=[self.num_envs])
```

```python
def _reward_target(self):
        target_rew = torch.sum(torch.square(self.last_rel_pos), dim=1) - torch.sum(torch.square(self.rel_pos), dim=1)
        return target_rew
```

```python
def _reward_smooth(self):
        smooth_rew = torch.sum(torch.square(self.actions - self.last_actions), dim=1)
        return smooth_rew
```

```python
def _reward_yaw(self):
        yaw = self.base_euler[:, 2]
        yaw = torch.where(yaw > 180, yaw - 360, yaw) / 180 * 3.14159  # use rad for yaw_reward
        yaw_rew = torch.exp(self.reward_cfg["yaw_lambda"] * torch.abs(yaw))
        return yaw_rew
```

```python
def _reward_angular(self):
        angular_rew = torch.norm(self.base_ang_vel / 3.14159, dim=1)
        return angular_rew
```

```python
def _reward_crash(self):
        crash_rew = torch.zeros((self.num_envs,), device=gs.device, dtype=gs.tc_float)
        crash_rew[self.crash_condition] = 1
        return crash_rew
```
```

### examples/drone/hover_train.py

```
def get_train_cfg(exp_name)
def get_cfgs()
def main()
```

### examples/locomotion/go2_env.py

```
def gs_rand(lower, upper, batch_shape)
class Go2Env()
    def __init__(self, num_envs, env_cfg, obs_cfg, reward_cfg, command_cfg, show_viewer)
    def _resample_commands(self, envs_idx)
    def step(self, actions)
    def get_observations(self)
    def _reset_idx(self, envs_idx)
    def _update_observation(self)
    def reset(self)
    def _reward_tracking_lin_vel(self)
    def _reward_tracking_ang_vel(self)
    def _reward_lin_vel_z(self)
    def _reward_action_rate(self)
    def _reward_similar_to_default(self)
    def _reward_base_height(self)

```python
def get_observations(self):
        return TensorDict({"policy": self.obs_buf}, batch_size=[self.num_envs])
```

```python
def _update_observation(self):
        self.obs_buf = torch.concatenate(
            (
                self.base_ang_vel * self.obs_scales["ang_vel"],  # 3
                self.projected_gravity,  # 3
                self.commands * self.commands_scale,  # 3
                (self.dof_pos - self.default_dof_pos) * self.obs_scales["dof_pos"],  # 12
                self.dof_vel * self.obs_scales["dof_vel"],  # 12
                self.actions,  # 12
            ),
            dim=-1,
        )
```

```python
def _reward_tracking_lin_vel(self):
        # Tracking of linear velocity commands (xy axes)
        lin_vel_error = torch.sum(torch.square(self.commands[:, :2] - self.base_lin_vel[:, :2]), dim=1)
        return torch.exp(-lin_vel_error / self.reward_cfg["tracking_sigma"])
```

```python
def _reward_tracking_ang_vel(self):
        # Tracking of angular velocity commands (yaw)
        ang_vel_error = torch.square(self.commands[:, 2] - self.base_ang_vel[:, 2])
        return torch.exp(-ang_vel_error / self.reward_cfg["tracking_sigma"])
```

```python
def _reward_lin_vel_z(self):
        # Penalize z axis base linear velocity
        return torch.square(self.base_lin_vel[:, 2])
```

```python
def _reward_action_rate(self):
        # Penalize changes in actions
        return torch.sum(torch.square(self.last_actions - self.actions), dim=1)
```

```python
def _reward_similar_to_default(self):
        # Penalize joint poses far away from default pose
        return torch.sum(torch.abs(self.dof_pos - self.default_dof_pos), dim=1)
```

```python
def _reward_base_height(self):
        # Penalize base height away from target
        return torch.square(self.base_pos[:, 2] - self.reward_cfg["base_height_target"])
```
```

### examples/locomotion/go2_train.py

```
def get_train_cfg(exp_name)
def get_cfgs()
def main()
```

### examples/manipulation/grasp_env.py

```
class GraspEnv()
    def __init__(self, env_cfg, reward_cfg, robot_cfg, show_viewer)
    def _init_buffers(self)
    def _reset_idx(self, envs_idx)
    def reset(self)
    def step(self, actions)
    def get_observations(self)
    def rescale_action(self, action)
    def get_stereo_rgb_images(self, normalize)
    def _reward_keypoints(self)
    def _to_world_frame(position, quaternion, keypoints_offset)
    def get_keypoint_offsets(batch_size, device, unit_length)
    def grasp_and_lift_demo(self)
class Manipulator()
    def __init__(self, num_envs, scene, args, device)
    def set_pd_gains(self)
    def _init(self)
    def reset(self, envs_idx, skip_forward)
    def apply_action(self, action, open_gripper)
    def _gs_ik(self, action)
    def _dls_ik(self, action)
    def go_to_goal(self, goal_pose, open_gripper)
    def base_pos(self)
    def ee_pose(self)
    def left_finger_pose(self)
    def right_finger_pose(self)
    def center_finger_pose(self)

```python
def get_observations(self) -> TensorDict:
        # Current end-effector pose
        finger_pos, finger_quat = (
            self.robot.center_finger_pose[:, :3],
            self.robot.center_finger_pose[:, 3:7],
        )
        obj_pos, obj_quat = self.object.get_pos(), self.object.get_quat()
        obs_components = [
            finger_pos - obj_pos,  # 3D position difference
            finger_quat,  # current orientation (w, x, y, z)
            obj_pos,  # goal position
            obj_quat,  # goal orientation (w, x, y, z)
        ]
        self.obs_buf = torch.cat(obs_components, dim=-1)
        return TensorDict({"policy": self.obs_buf}, batch_size=[self.num_envs])
```

```python
def _reward_keypoints(self) -> torch.Tensor:
        keypoints_offset = self.keypoints_offset
        # there is a offset between the finger tip and the finger base frame
        finger_tip_z_offset = torch.tensor(
            [0.0, 0.0, -0.06],
            device=self.device,
            dtype=gs.tc_float,
        ).repeat(self.num_envs, 1)
        finger_pos_keypoints = self._to_world_frame(
            self.robot.center_finger_pose[:, :3] + finger_tip_z_offset,
            self.robot.center_finger_pose[:, 3:7],
            keypoints_offset,
        )
        object_pos_keypoints = self._to_world_frame(self.object.get_pos(), self.object.get_quat(), keypoints_offset)
        dist = torch.norm(finger_pos_keypoints - object_pos_keypoints, p=2, dim=-1).sum(-1)
        return torch.exp(-dist)
```
```

### examples/manipulation/grasp_train.py

```
def get_train_cfg(exp_name)
def get_task_cfgs()
def load_teacher_policy(env, rl_train_cfg, exp_name)
def main()
```

### examples/rigid/heterogeneous_simulation.py

```
"""Heterogeneous Simulation Example
================================

This example demonstrates heterogeneous simulation, where different parallel
environments can have different geometry variants for the same entity.

Variant Assignment Rules:
    When passing a list of morphs to scene.add_entity(), variants are distributed
    across environments using the following rules:

    1. When n_envs >= n_variants:
       Balanced block assignment. Environments are divided into blocks, with each
       block assigned to one variant. For example, with 4 variants and 8 environments:
       - Environments"""
def main()
```

### examples/rigid/ik_shadow_hand.py

```
def main()
```

### examples/rigid/single_franka_envs.py

```
def main()
```

### examples/sap_coupling/fem_fixed_constraint.py

```
def main()
```

### examples/sensors/surface_distance_shadowhand.py

```
"""Interactive SurfaceDistanceProbe demo with Shadow Hand and keyboard teleop.

Surface distance probes on the hand measure distance to a rubber duck (mesh) and a box.
Use keyboard controls to move the hand via IK; the hand tracks target positions
for the wrist and fingertips."""
def main()
```

### examples/viewer_plugin/mouse_interaction.py

```
def main()
```

### genesis/engine/simulator.py

```
class Simulator(RBC)
    """A simulator is a scene-level simulation manager, which manages all simulation-related operations in the scene, including multiple solvers and the inter-solver coupler.

Parameters
----------
scene : gs.Scene
    The scene object that the simulator is associated with.
options : SceneOptions
    Every"""
    def __init__(self, scene, options)
    def _add_entity(self, morph, material, surface, visualize_contact, name, desc)
    def _add_force_field(self, force_field)
    def build(self)
    def destroy(self)
    def reset(self, state, envs_idx)
    def _restart(self, envs_idx)
    def data(self, kinds)
    def __getstate__(self)
    def __setstate__(self, state)
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
    def steps(self)
    def dt(self)
    def substeps(self)
    def substep_dt(self)
    def scene(self)
    def requires_grad(self)
    def n_entities(self)
    def entities(self)
    def substeps_local(self)
    def cur_substep_global(self)
    def cur_substep_local(self)
    def cur_step_local(self)
    def fps_tracker(self)
    def cur_step_global(self)
    def get_time(self, envs_idx)
    def cur_t(self)
    def coupler(self)
    def solvers(self)
    def active_solvers(self)
```

### genesis/engine/solvers/rigid/constraint/__init__.py

```
"""Constraint solver submodule for rigid body simulation.

Contains constraint solving, island detection, and backward pass."""
```

### genesis/engine/solvers/rigid/constraint/backward.py

```
def func_matvec_Ap(i_b, constraint_state, dyn_info, rigid_info, rigid_config)
def func_solve_adjoint_u_cg_batch(i_b, constraint_state, dyn_info, rigid_info, rigid_config)
def kernel_solve_adjoint_u(constraint_state, dyn_info, rigid_info, rigid_config)
def kernel_compute_gradients(constraint_state, rigid_info)
def kernel_load_dL_dqacc_from_acc_grad(dyn_state, constraint_state, rigid_config)
def kernel_accumulate_constraint_solver_grads(dyn_state, constraint_state, rigid_info, rigid_config)
def kernel_manual_add_joint_limit_constraints_bw(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config, enable_collision)
def kernel_manual_add_collision_constraints_bw(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def kernel_manual_add_frictionloss_constraints_bw(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_cddb_ang_bw(i_b, link, g_cddb_ang, dyn_state, dyn_info, rigid_config)
def func_equality_jdotv_bw(i_b, link, anchor_pos, g_jdotv, dyn_state, dyn_info, rigid_config)
def kernel_manual_add_equality_constraints_bw(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
```

### genesis/engine/solvers/rigid/constraint/island.py

```
def func_find_tree_root(i_t, i_b, constraint_state)
def func_union_trees(i_ta, i_tb, i_b, constraint_state)
def func_joint_link(i_joint, i_b, n_links, dyn_info, rigid_config)
def func_equality_links(i_eq, i_b, n_links, dyn_info, rigid_config)
def func_edge_trees(i_e, i_b, i_first_contact, n_contacts, n_equalities, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_constraint_island(i_c, i_b, constraint_state)
def func_group_constraints_by_island(i_b, constraint_state, rigid_config)
def func_chunk_island_rank(tid, i_island, sh_chunk)
def func_group_constraints_by_island_coop(i_b, tid, sh_chunk, constraint_state, rigid_config)
def func_dof_range_start(i_island, i_b, constraint_state)
def func_build_islands(i_b, dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_build_single_island(i_b, constraint_state, rigid_info, rigid_config)
def func_build_single_island_coop(i_b, tid, constraint_state, rigid_info, rigid_config)
def func_tree_component(i_t, i_b, constraint_state)
def func_build_islands_coop(i_b, tid, dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_contact_island(i_col, i_b, collider_state, constraint_state)
def func_contact_tree_slots(i_col, i_b, collider_state, constraint_state, rigid_info)
def func_reorder_island_dofs(i_b, collider_state, constraint_state, rigid_info)
def func_sort_contacts_coop(i_b, tid, dyn_state, collider_state, constraint_state)
def func_sort_contacts(i_b, contact_idx, i_first, n, contacts_pos, contacts_geom_a, contacts_geom_b, geoms_pos, geoms_quat)
```

### genesis/engine/solvers/rigid/constraint/linesearch.py

```
"""Per-island Newton / CG iteration of the rigid constraint solver, every island of an env advancing in lockstep.

The island partition (see island.py) makes the mass matrix, the Jacobian and hence the cost block-diagonal, so each
island owns a line search, a convergence test and a search direction of its own, measured against the trace of its own
mass block (IslandState.inertia in array_class.py), and a converged island stands still while the others iterate. The
monolith arm (one thread per env) takes the islands one after the other, each search sweeping its own dofs and rows
through the island-"""
def func_list_range_start(ids, lo, hi, i_b)
def func_list_item(ids, i_pos, lo, range_start, i_b)
def func_group_dof_range_start(i_b, tid, base, n_group, dof_lo, dof_hi, constraint_state)
def func_row_p0_terms(i_c, i_b, ne, nef, ncone, constraint_state, rigid_config, row_kind)
def func_row_alpha_terms(i_c, i_b, n_alphas, alphas, ne, nef, ncone, constraint_state, rigid_config, row_kind)
def func_dof_p0_terms(i_d, i_b, dyn_state, constraint_state)
def func_dof_exit_terms(i_d, i_b, constraint_state, rigid_config)
def func_ls_state_init(sums_dofs, sums_rows, inertia, rigid_info, rigid_config)
def func_ls_state_advance(acc, n_alphas, alphas, phase, p1, p2, p2update, direction, ls_it, gtol, base_1, base_2, p0_deriv_0, p0_deriv_1, rigid_info)
def func_exit_decision(terms, improvement, inertia, rigid_info, rigid_config)
def func_certify_decision(terms, inertia, rigid_info, rigid_config)
def func_mv_jv_dense(i_b, constraint_state, rigid_info)
def func_mv_jv_islands(i_b, constraint_state, rigid_info)
def func_block_sum(value)
def func_row_p0_sums_by_class(i_b, i_first, stride, ne, nef, ncone, n_con, constraint_state, rigid_config)
def func_row_alpha_sums_by_class(i_b, i_first, stride, n_alphas, alphas, ne, nef, ncone, n_con, constraint_state, rigid_config)
def func_search_single_island(i_b, tid, stride, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, is_coop)
def func_exit_single_island(i_b, tid, stride, constraint_state, rigid_info, rigid_config, is_coop, certify)
def func_linesearch_islands_serial(i_b, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_exit_islands_serial(i_b, constraint_state, rigid_info, rigid_config, certify)
def func_segment_add(tid, i_slot, n_valid, value, i_slot_prev, i_slot_next, sh_acc, k)
def func_mv_jv_coop(i_b, tid, constraint_state, rigid_info)
def func_linesearch_islands_coop(i_b, tid, sh_acc, sh_alphas, sh_n_alphas, sh_pending, sh_alpha, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_exit_islands_coop(i_b, tid, sh_acc, sh_pending, sh_alpha, constraint_state, rigid_info, rigid_config, certify)
```

### genesis/engine/solvers/rigid/constraint/noslip.py

```
def func_solve_mass_block(i_d0, i_b, i_col, vec, rigid_info)
def func_apply_Minv_rows(i_row_0, i_row_1, i_b, i_col, jac_dofs_idx, coef_0, coef_1, vec, jac, jac_n_dofs, rigid_info)
def func_accumulate_row_blocks(i_row, i_b, i_col, jac_dofs_idx, vec_src, vec_dst, jac_n_dofs, rigid_info)
def func_dot_row(i_row, i_b, i_col, jac_dofs_idx, vec, jac, jac_n_dofs)
def func_color_rows_batch(i_b, i_island, tid, constraint_state, rigid_info)
def func_refresh_qacc_batch(i_b, i_island, tid, n_colors, dyn_state, constraint_state, rigid_info, rigid_config)
def func_noslip_update_row(i_c, i_b, i_col, ne, nf, const_start, const_end, EPS, constraint_state, rigid_info)
def func_noslip_batch(i_b, i_island, tid, n_colors, dyn_state, collider_state, constraint_state, rigid_info, rigid_config)
def func_dual_finish_batch(i_b, i_island, tid, n_colors, dyn_state, constraint_state, rigid_info, rigid_config)
def kernel_noslip(dyn_state, collider_state, constraint_state, rigid_info, rigid_config)
def func_cost_change(i_b, force_start, Ac, old_force, res, eps, force, dim)
```

### genesis/engine/solvers/rigid/constraint/solver.py

```
def _append_relevant_dof(i_con, i_d, i_b, n, dedup, constraint_state)
def _sort_relevant_dofs_descending(i_con, i_b, n, constraint_state, rigid_config)
class ConstraintSolver()
    def __init__(self, rigid_solver)
    def data(self)
    def reset(self, envs_idx)
    def clear(self, envs_idx)
    def add_equality_constraints(self)
    def add_inequality_constraints(self)
    def resolve(self)
    def noslip(self)
    def get_equality_constraints(self, as_tensor, to_torch)
    def get_weld_constraints(self, as_tensor, to_torch)
    def add_weld_constraint(self, link1_idx, link2_idx, envs_idx)
    def delete_weld_constraint(self, link1_idx, link2_idx, envs_idx)
    def backward(self)
def kernel_get_equality_constraints(iout, fout, constraint_state, dyn_info, rigid_config, is_padded)
def constraint_solver_kernel_reset(envs_idx, constraint_state, rigid_config)
def func_clear_constraint_at_env(i_b, n_dofs, len_constraints, constraint_state, rigid_info, rigid_config)
def constraint_solver_kernel_clear(envs_idx, constraint_state, rigid_info, rigid_config)
def constraint_solver_kernel_masked_clear(envs_mask, constraint_state, rigid_info, rigid_config)
def _func_contact_row_direction(i_friction, normal, d1, d2, friction, friction_torsional, friction_rolling, rigid_config)
def _add_friction_constraint(i_b, i_col_, i_friction, dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _add_collision_constraints_per_friction(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _add_collision_constraints_per_contact(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def add_collision_constraints(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_equality_jdotv(i_b, link, anchor_pos, dyn_state, dyn_info, rigid_config)
def func_equality_connect(i_b, i_e, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_equality_joint(i_b, i_e, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def add_equality_constraints(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _sort_contacts_and_build_islands(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config, collider_static_config)
def func_append_factor_worklist(i_b, i_island, constraint_state, rigid_config)
def add_inequality_constraints(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config, collider_static_config)
def func_equality_weld(i_b, i_e, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def add_joint_limit_constraints(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def add_frictionloss_constraints(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def kernel_add_weld_constraint(link1_idx, link2_idx, envs_idx, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def kernel_delete_weld_constraint(link1_idx, link2_idx, envs_idx, constraint_state, dyn_info, rigid_info, rigid_config)
def func_compute_island_envelope(i_b, i_island, constraint_state, rigid_info, rigid_config)
def func_add_cone_hessian_block(i_b, constraint_state, rigid_config, is_removal, scale_by_jacobi)
def func_wrap_cone_hessian(constraint_state, rigid_config, is_removal, is_enabled)
def func_add_cone_hessian_block_island(i_b, i_island, constraint_state, rigid_config, scale_by_jacobi)
def func_copy_cone_free_hessian_island(i_b, i_island, constraint_state, save)
def func_update_cone_free_hessian_flip(i_b, i_c, constraint_state, rigid_info, rigid_config)
def func_hessian_direct_batch(i_b, i_island, constraint_state, dyn_info, rigid_info, rigid_config)
def func_island_assemble_factor_solve_tiled(i_b, i_island, tid, sh_L, sh_v, constraint_state, dyn_info, rigid_info, rigid_config, TileCls, tile_size, max_dofs, is_last_class, write_L)
def func_island_hessian_assemble_block(i_b, i_island, tid, sh_jac, sh_D, constraint_state, rigid_info, rigid_config, block_dim, row_tile)
def func_island_hessian_patch_block(i_b, i_island, tid, sh_scan, constraint_state, rigid_config, block_dim)
def func_island_hessian_assemble_all(constraint_state, rigid_info, rigid_config, patch)
def func_island_tiled_factor_solve_all(constraint_state, dyn_info, rigid_info, rigid_config, write_L)
def func_cholesky_factor_direct_batch(i_b, i_island, constraint_state, rigid_info, rigid_config)
def func_hessian_and_cholesky_factor_direct_batch(i_b, constraint_state, dyn_info, rigid_info, rigid_config, compute_envelope)
def func_hessian_and_cholesky_factor_direct(constraint_state, dyn_info, rigid_info, rigid_config, compute_envelope)
def func_build_changed_constraint_list(i_b, constraint_state)
def func_apply_rank1_dense_block(i_b, i_d_start, n, sign, constraint_state, rigid_info)
def func_rank1_flip_dense_block(i_b, i_c, i_d_start, n, constraint_state, rigid_info, rigid_config)
def func_hessian_and_cholesky_factor_incremental_dense_batch(i_b, constraint_state, rigid_info, rigid_config)
def func_apply_staged_rank_updates_island(i_b, i_island, i_d_local_start, n_u, signs, constraint_state, rigid_info, rigid_config)
def func_rank_batch_update_island(i_b, i_island, batch_ic, n_u, constraint_state, rigid_info, rigid_config)
def func_factor_island_incremental_batch(i_b, i_island, constraint_state, rigid_info, rigid_config)
def func_cone_rank_update_island(i_b, i_island, constraint_state, rigid_info, rigid_config)
def func_cone_rank_update_whole_env(i_b, constraint_state, rigid_info, rigid_config)
def func_factor_island_incremental_or_direct(i_b, i_island, constraint_state, dyn_info, rigid_info, rigid_config)
def func_hessian_and_cholesky_factor_incremental_batch(i_b, constraint_state, dyn_info, rigid_info, rigid_config)
def func_cholesky_solve_batch(i_b, i_island, rhs, out, constraint_state, rigid_config)
def update_bracket_no_eval_local(p_alpha, p_cost, p_grad, p_hess, alphas, costs, grads, hess)
def _tri_idx(i, j, dim)
def _friction_blocks(rigid_config)
def _func_cone_zone(rows_jaref, rows_efc_D, con_mu, rows_friction, rigid_config)
def _func_cone_head_load(i_c, i_b, constraint_state, rigid_config)
def _func_cone_head_is_middle(i_c, i_b, nef, constraint_state, rigid_config)
def _func_cone_Dm(D0, con_mu)
def _func_disc_middle(rows_jaref, rows_efc_D, rows_friction, f_n, rigid_config)
def _func_cone_middle(rows_jaref, rows_efc_D, con_mu, rows_friction, N, T, rigid_config)
def _func_cone_middle_convex(rows_jaref, D0, con_mu, rows_friction, N, T)
def _func_cone_block_product(cone_H, rows_jac_row, rows_jac_col)
def _func_cone_block_chol(rows_jaref, rows_efc_D, con_mu, rows_friction, zone, N, T, EPS, rigid_config)
def func_cone_middle_cost(i_c, i_b, constraint_state, rigid_config)
def _func_disc_cost_along_alpha(rows_jaref, rows_jv, alpha, rows_efc_D, rows_friction, rigid_config)
def _func_cone_cost_along_alpha(rows_jaref, rows_jv, alpha, rows_efc_D, con_mu, rows_friction, rigid_config)
def _func_disc_cost_diff_along_alpha(rows_jaref, rows_jv, alpha, rows_efc_D, rows_friction, rigid_config)
def _func_cone_cost_diff_along_alpha(rows_jaref, rows_jv, alpha, rows_efc_D, con_mu, rows_friction, rigid_config)
def func_cone_update_rows(i_c, i_b, constraint_state, rigid_config)
def func_is_row_moving(i_c, i_b, constraint_state, skip_settled_islands)
def func_qfrc_scatter_sparse(i_b, constraint_state, walk_islands)
def func_qfrc_gather_dense(i_b, constraint_state)
def func_update_constraint_batch(i_b, qacc, Ma, cost, dyn_state, constraint_state, rigid_config, skip_settled_islands)
def _func_update_efc_force_body(i_c, i_b, constraint_state, rigid_config)
def _func_update_efc_force(constraint_state, rigid_config)
def _func_update_qfrc_constraint_coop(constraint_state, rigid_config)
def _func_update_cost_coop(qacc, Ma, cost, dyn_state, constraint_state, rigid_config)
def func_update_constraint(qacc, Ma, cost, dyn_state, constraint_state, rigid_config)
def func_update_gradient_batch(i_b, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_update_gradient_no_solve(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_update_gradient(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def initialize_Jaref(qacc, constraint_state, rigid_config)
def _initialize_Jaref_body(i_c, i_b, n_dofs, qacc, constraint_state, rigid_config)
def _initialize_Jaref_per_env(qacc, constraint_state, rigid_config)
def _initialize_Jaref_parallel(qacc, constraint_state, rigid_config)
def initialize_Ma(Ma, qacc, dyn_info, rigid_info, rigid_config)
def func_solve_init(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, write_L)
def func_solve_iter(i_b, it, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _get_static_config()
def func_solve_body(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, _n_iterations)
def _kernel_solve_monolith(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, _n_iterations)
def func_solve_body_monolith(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, _n_iterations)
def func_update_contact_force(dyn_state, collider_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_update_qacc(dyn_state, constraint_state, rigid_config, errno)
```

### genesis/engine/solvers/rigid/constraint/solver_breakdown.py

```
def _func_update_constraint_forces_body(i_c, i_b, constraint_state, rigid_config)
def _func_update_constraint_forces(constraint_state, rigid_config)
def _func_update_qfrc_constraint_per_dof(constraint_state, rigid_config)
def _func_update_gradient(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _func_islands_linesearch_and_apply(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def _func_islands_update_search_direction(dyn_state, constraint_state, rigid_info, rigid_config)
def _func_check_early_exit(graph_counter, constraint_state)
def _kernel_solve_graph(graph_counter, dyn_state, constraint_state, dyn_info, rigid_info, rigid_config)
def func_solve_decomposed(dyn_state, constraint_state, dyn_info, rigid_info, rigid_config, _n_iterations)
```

### genesis/vis/viewer_plugins/plugins/mouse_interaction.py

```
class MouseInteractionPlugin(RaycasterViewerPlugin)
    """Drag rigid entities around with the mouse, by a spring attached where the cursor grabbed them.

Parameters
----------
use_force : bool, optional
    Drag the grabbed link with a spring force, leaving the solver to resolve it against gravity, contacts and the
    rest of the kinematic tree, so the dr"""
    def __init__(self, use_force, spring_slack, color, use_visual_geom)
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
    def _apply_spring_force(self, control_point, dt)
```

### tests/grad/test_rigid_constraints.py

```
def test_joint_limit_grad_matches_fd(grad_slider_limit, precision, show_viewer)
def test_per_step_force_into_limit_grad_matches_fd(model_name, request, precision, show_viewer)
def test_frictionloss_grad_matches_fd(grad_revolute_frictionloss, precision, show_viewer)
def test_equality_grad_matches_fd(model_name, n_rows, request, precision, show_viewer)
def test_all_constraint_groups_grad_matches_fd(grad_all_eq_fric, precision, show_viewer)
```

### tests/rigid/test_constraints.py

```
def test_equality_joint_scaling(show_viewer, scaled_mjcf_joint_equalities, n_envs, batched, tol)
def test_dynamic_weld(show_viewer, tol)
def test_dynamic_weld_scene_reset()
def test_urdf_mimic(show_viewer, tol, scaled_urdf_mimic)
def test_get_constraints_api(show_viewer, tol)
def test_set_sol_params(n_envs, batched, tol)
```

### tests/utils/simulators.py

```
class MjSim()
def build_mujoco_sim(xml_path, gs_solver, gs_integrator, merge_fixed_links, multi_contact, adjacent_collision, native_ccd)
def build_genesis_sim(xml_paths, gs_solver, gs_integrator, merge_fixed_links, multi_contact, mujoco_compatibility, adjacent_collision, gjk_collision, show_viewer, mj_sim)
```