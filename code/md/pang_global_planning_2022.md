# pang_global_planning_2022

source: https://github.com/pangtao22/quasistatic_simulator


commit: c9177559ab5393ba800ebd264b3d97e4f7113fe9


## README

# Quasi-static Simulator
[![ci_badge](https://github.com/pangtao22/quasistatic_simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/pangtao22/quasistatic_simulator/actions)

![](/media/planar_hand.gif) ![](/media/allegro_hand_ball.gif) ![](/media/allegro_hand_door.gif)

This repo provides an implementation of a **differentiable**, **convex** and **quasi-static** dynamics model which is effective for **contact-rich manipulation planning**. The dynamics formulation is described in
- Section 3 of [Global Planning for Contact-Rich Manipulation via
Local Smoothing of Quasi-dynamic Contact Models](https://arxiv.org/abs/2206.10787), currently under review.
- [A Convex Quasistatic Time-stepping Scheme for Rigid Multibody Systems with Contact and Friction](http://groups.csail.mit.edu/robotics-center/public_papers/Pang20b.pdf), ICRA2021.

Additional interactive animations generated using the code in this repo can be found in [this slide deck](https://slides.com/pang/deck-28a801).

## Dependencies
- Drake **built with Gurobi and Mosek**. Free solvers (OSQP + SCS) also work, but SCS is a lot slower than Mosek for solving SOCPs.

Note that until [this issue](https://github.com/RobotLocomotion/drake-external-examples/issues/216) is resolved, this repo can only be built in debug mode if the official version of Drake is used, which is a lot slower than release mode. A workaround is described in the issue, but requires [a custom branch of drake](https://github.com/pangtao22/drake/tree/my_main).


## Docker
1. Remember to check out submodules before building the docker images.
```
git submodule update --init --recursive
```

2. In the root of this repo, to build, run
```
docker build -t qsim -f ./setup/qsim.dockerfile .
```

If on Apple Silicon Macs, run
```
docker buildx build --platform=linux/amd64 -t qsim -f ./setup/qsim.dockerfile .
```
Beware that compiling is slow! It took M2 Max more than 20 minutes to build the
image.

3. To run the github "build and test" action locally, run
```
docker run -v $PWD:"/workdir" --workdir="/workdir" --entrypoint "/workdir/setup/run_tests.sh" qsim
```
If on Apple Silicon Macs, run
```
docker run -v $PWD:"/workdir" --workdir="/workdir" --platform=linux/amd64 --entrypoint "/workdir/setup/run_tests.sh" qsim
```
It is also very slow, even slower than building the image and then running
the test in CI.

---
If following the dockerfile and the scripts therein to build locally, it is
recommended to set `-DCMAKE_BUILD_TYPE=Release`. Building in release mode
seems to trigger segfaults inside containers.

## Running python tests
In the root of the repo, run
```bash
pytest .
```
Multi-threaded testing with `pytest-xdist `:
```bash
pytest . -n auto
```


## File tree (depth 3, assets pruned)

```
.clang-format
.dockerignore
.github/
  workflows/
    build_push_prune.yml
    ci.yml
    pre_commit.yml
.gitignore
.gitmodules
.pre-commit-config.yaml
CPPLINT.cfg
LICENSE
models/
  allegro_hand.yml
  allegro_hand_book.yml
  allegro_hand_description_right_spheres.sdf
  allegro_hand_door.yml
  allegro_hand_floating.sdf
  allegro_hand_floating_palm_down.sdf
  allegro_hand_floating_palm_up.sdf
  allegro_hand_pen.yml
  allegro_hand_plate.yml
  allegro_hand_tilted.yml
  ball_and_platform.yml
  ball_hand.sdf
  book.sdf
  box_0.06m.sdf
  box_0.07m.sdf
  box_0.08m.sdf
  box_0.3m_rotation.sdf
  box_0.4m_rotation.sdf
  box_0.5m.sdf
  box_0.5m_rotation.sdf
  box_0.6m.sdf
  box_1m.sdf
  box_1m_rotation.sdf
  box_1m_rotation_damped.sdf
  box_ball_graze_2d.yml
  box_pivoting.yml
  box_pushing.yml
  box_to_push.sdf
  box_to_push_xy_rotation.sdf
  box_uhaul_extra_large.sdf
  box_uhaul_medium.sdf
  box_uhaul_medium_xy_yaw.sdf
  box_y.sdf
  box_yz_rotation_big.sdf
  carrot.yml
  cylinder.sdf
  cylinder_xy_yaw.sdf
  door_fixed.sdf
  door_rotation.sdf
  door_rotation_push.sdf
  gripper.sdf
  gripper_yz.sdf
  ground.yml
  ground_box.sdf
  ground_box_thin.sdf
  ground_with_platform.sdf
  iiwa14_sphere_collision_push.sdf
  iiwa7_planar_sphere_collision.sdf
  iiwa7_sphere_collision.sdf
  iiwa_and_schunk_and_ground.yml
  iiwa_planar_sphere_collision_bimanual.yml
  iiwa_sphere_collision_bimanual.yml
  iiwa_sphere_collision_bimanual_planar.yml
  iiwa_sphere_collision_push.yml
  iiwa_sphere_collision_push_no_ground.yml
  package.xml
  pen.sdf
  planar_hand.yml
  plate.sdf
  plate.yml
  plate_ellipsoid.sdf
  q_sys/
    3_link_arm_2d_box.yml
    3_link_arm_3d_box.yml
    allegro_hand_and_sphere.yml
    allegro_hand_and_sphere_hardware.yml
    allegro_hand_baoding_0.03.yml
    allegro_hand_baoding_0.04.yml
    allegro_hand_book.yml
    allegro_hand_door.yml
    allegro_hand_door_push.yml
    allegro_hand_pen.yml
    allegro_hand_plate.yml
    allegro_hand_tilted_and_sphere.yml
    ball_grazing_2d.yml
    box_pushing.yml
    iiwa.yml
    iiwa_and_boxes.yml
    iiwa_bimanual_box.yml
    iiwa_bimanual_cylinder.yml
    iiwa_box.yml
    iiwa_box_no_ground.yml
    iiwa_planar_bimanual_cylinder.yml
    planar_hand_ball.yml
    planar_hand_ball_2d.yml
    planar_hand_ball_small_ball.yml
    planar_hand_box.yml
    two_spheres_xyz.yml
    two_spheres_y.yml
    two_spheres_yz.yml
  rope.sdf
  rope.yml
  sphere_r0.03m_green.sdf
  sphere_r0.03m_red.sdf
  sphere_r0.04m_green.sdf
  sphere_r0.04m_red.sdf
  sphere_r0.05m.sdf
  sphere_r0.05m_light.sdf
  sphere_r0.065m_light.sdf
  sphere_r0.06m.sdf
  sphere_xyz_actuated_with_ground.yml
  sphere_xyz_r_0.1m_actuated.sdf
  sphere_xyz_r_0.5m.sdf
  sphere_y.sdf
  sphere_y_actuated.sdf
  sphere_y_actuated.yml
  sphere_y_rotation_r_0.25m.sdf
  sphere_yz.sdf
  sphere_yz_actuated.sdf
  sphere_yz_actuated.yml
  sphere_yz_actuated_and_ground.yml
  sphere_yz_r_0.5m.sdf
  sphere_yz_rotation_r_0.125m.sdf
  sphere_yz_rotation_r_0.25m.sdf
  sphere_yz_rotation_r_0.5m.sdf
  sphere_yz_small.sdf
  three_link_arm.sdf
  three_link_arm.yml
  three_link_arm_and_ground.yml
  two_link_sphere_arm_left.sdf
  two_link_sphere_arm_right.sdf
  wall_box.sdf
  wall_box_left.sdf
pyproject.toml
qsim/
  __init__.py
  contact_results_logger.py
  examples/
    __init__.py
    allegro_hand/
    box_ball_graze_2d/
    box_pivoting/
    box_pushing/
    carrots/
    gripper_ball_pinch_2d/
    iiwa_bimanual/
    iiwa_block_stacking/
    iiwa_external_loading/
    iiwa_traj_following/
    log_comparison.py
    planar_hand_ball/
    plate_pickup/
    rope_pushing/
    setup_simulations.py
    sphere_yz_on_platform/
    three_link_arm_block_pushing/
    two_spheres_xyz/
    two_spheres_y/
    two_spheres_yz/
  meshcat_visualizer_old.py
  model_paths.py
  normalization_derivatives.py
  parser.py
  simulator.py
  system.py
  tests/
    test_normalization_derivatives.py
    test_qp_derivatives_cpp.py
    test_socp_derivatives_cpp.py
  utils.py
  visualizer.py
qsim_old/
  __init__.py
  meshcat_camera_utils.py
  problem_definition_graze.py
  problem_definition_pinch.py
  simulator.py
quasistatic_simulator_cpp/
  CMakeLists.txt
  bindings/
    CMakeLists.txt
    qsim_cpp.cc
  diffcp/
    CMakeLists.txt
    log_barrier_solver.cc
    log_barrier_solver.h
    qp_derivatives.cc
    qp_derivatives.h
    socp_derivatives.cc
    socp_derivatives.h
    solver_selector.cc
    solver_selector.h
  examples/
    CMakeLists.txt
    run_3link_arm_3d.cc
    run_allegro_hand_A.cc
    run_allegro_hand_jacobian.cc
    run_iiwa_box_stacking.cc
    run_planar_hand_ball.cc
    run_two_spheres_yz.cc
  qsim/
    CMakeLists.txt
    batch_quasistatic_simulator.cc
    batch_quasistatic_simulator.h
    contact_jacobian_calculator.cc
    contact_jacobian_calculator.h
    finite_differencing_gradient.cc
    finite_differencing_gradient.h
    get_model_paths.cc
    get_model_paths.h
    quasistatic_parser.cc
    quasistatic_parser.h
    quasistatic_sim_params.h
    quasistatic_simulator.cc
    quasistatic_simulator.h
  tests/
    CMakeLists.txt
    batch_simulator_test.cc
    contact_forces_test.cc
    log_barrier_solver_test.cc
    quasistatic_sim_gradients_test.cc
    solver_selector_test.cc
    test_utilites.cc
    test_utilities.h
readme.md
robotics_utilities/
setup/
  base.dockerfile
  build_bindings.sh
  copy_resources.sh
  install_eigen3.4.sh
  qsim.dockerfile
  requirements.txt
  run_tests.sh
```

## Config files (22)


### .pre-commit-config.yaml

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
-   repo: https://github.com/ssciwr/clang-format-hook.git
    rev: v12.0.1  # Use the sha / tag you want to point at
    hooks:
    -   id: clang-format

-   repo: https://github.com/cpplint/cpplint.git
    rev: 1.6.1
    hooks:
    -   id: cpplint

```

### models/allegro_hand.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_description_right_spheres.sdf

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]
        rotation: !Rpy {deg: [0., -90.0, 0.0]}

- add_weld:
    parent: world_hand_offset
    child: allegro_hand_right::hand_root

```

### models/allegro_hand_book.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_floating_palm_down.sdf

- add_model:
    name: ground
    file: package://quasistatic_simulator/ground_box_thin.sdf

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]
        rotation: !Rpy {deg: [0., 90.0, 90.0]}

- add_weld:
    parent: world_hand_offset
    child: allegro_hand_right::ghost_body_x

- add_weld:
    parent: world
    child: ground

```

### models/allegro_hand_door.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_floating.sdf

- add_model:
    name: door_fixed
    file: package://quasistatic_simulator/door_fixed.sdf

- add_frame:
    name: ground_world_offset
    X_PF:
        base_frame: world
        translation: [ 0, 0.25, 0.0]

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]

- add_weld:
    parent: ground_world_offset
    child: door_fixed::door

- add_weld:
    parent: world
    child: allegro_hand_right::ghost_body_x

```

### models/allegro_hand_pen.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_floating_palm_up.sdf

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]
        rotation: !Rpy {deg: [0., -90.0, 0.0]}

- add_weld:
    parent: world_hand_offset
    child: allegro_hand_right::ghost_body_x

```

### models/allegro_hand_plate.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_floating_palm_down.sdf

- add_model:
    name: ground
    file: package://quasistatic_simulator/ground_box_thin.sdf

- add_model:
    name: wall
    file: package://quasistatic_simulator/wall_box.sdf

- add_model:
    name: wall_left
    file: package://quasistatic_simulator/wall_box_left.sdf

- add_frame:
    name: wall_frame1
    X_PF:
        base_frame: ground
        translation: [0, -0.5, 0]
        rotation: !Rpy {deg: [0, 0, 0]}

- add_frame:
    name: wall_frame2
    X_PF:
        base_frame: ground
        translation: [0.5, 0, 0]
        rotation: !Rpy {deg: [0, 0, 90]}

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]
        rotation: !Rpy {deg: [0., 90.0, 90.0]}

- add_weld:
    parent: world_hand_offset
    child: allegro_hand_right::ghost_body_x

- add_weld:
    parent: world
    child: ground

- add_weld:
    parent: wall_frame1
    child: wall

- add_weld:
    parent: wall_frame2
    child: wall_left

```

### models/allegro_hand_tilted.yml

```yaml
directives:

- add_model:
    name: allegro_hand_right
    file: package://quasistatic_simulator/allegro_hand_description_right_spheres.sdf

- add_frame:
    name: world_hand_offset
    X_PF:
        base_frame: world
        translation: [0, 0, 0]
        rotation: !Rpy {deg: [0., -105., 0.]}

- add_weld:
    parent: world_hand_offset
    child: allegro_hand_right::hand_root

```

### models/planar_hand.yml

```yaml
directives:
- add_model:
    name: arm_left
    file: package://quasistatic_simulator/two_link_sphere_arm_left.sdf

- add_model:
    name: arm_right
    file: package://quasistatic_simulator/two_link_sphere_arm_right.sdf

- add_frame:
    name: world_left_arm_offset
    X_PF:
        base_frame: world
        translation: [0, -0.1, 0]

- add_frame:
    name: world_right_arm_offset
    X_PF:
        base_frame: world
        translation: [0, 0.1, 0]

- add_weld:
    parent: world_left_arm_offset
    child: arm_left::link_0

- add_weld:
    parent: world_right_arm_offset
    child: arm_right::link_0

```

### models/q_sys/allegro_hand_and_sphere.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_r0.06m.sdf

quasistatic_sim_params:
  gravity: [0, 0, -10.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: 5.

```

### models/q_sys/allegro_hand_and_sphere_hardware.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand.yml
robots:
  -
    name: allegro_hand_right
    Kp: [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 4, 3, 3, 2]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_r0.065m_light.sdf

quasistatic_sim_params:
  gravity: [0, 0, -9.8]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: 5.

```

### models/q_sys/allegro_hand_baoding_0.03.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: sphere_1
    file: package://quasistatic_simulator/sphere_r0.03m_red.sdf

  -
    name: sphere_2
    file: package://quasistatic_simulator/sphere_r0.03m_green.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_baoding_0.04.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: sphere_1
    file: package://quasistatic_simulator/sphere_r0.04m_red.sdf

  -
    name: sphere_2
    file: package://quasistatic_simulator/sphere_r0.04m_green.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_book.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_book.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: book
    file: package://quasistatic_simulator/book.sdf

quasistatic_sim_params:
  gravity: [0, 0, -10.]
  nd_per_contact: 8
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_door.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_door.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: door
    file: package://quasistatic_simulator/door_rotation.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_door_push.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_door.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: door
    file: package://quasistatic_simulator/door_rotation_push.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: 1.0

```

### models/q_sys/allegro_hand_pen.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_pen.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: pen
    file: package://quasistatic_simulator/pen.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_plate.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_plate.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: plate
    file: package://quasistatic_simulator/book.sdf

quasistatic_sim_params:
  gravity: [0, 0, -10.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.0125
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/allegro_hand_tilted_and_sphere.yml

```yaml
model_directive: package://quasistatic_simulator/allegro_hand_tilted.yml
robots:
  -
    name: allegro_hand_right
    Kp: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_r0.06m.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 4
  contact_detection_tolerance: 0.025
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/planar_hand_ball.yml

```yaml
model_directive: package://quasistatic_simulator/planar_hand.yml
robots:
  -
    name: arm_left
    Kp: [50, 25]
  -
    name: arm_right
    Kp: [50, 25]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_yz_rotation_r_0.25m.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 2
  contact_detection_tolerance: 10.0
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/planar_hand_ball_2d.yml

```yaml
model_directive: package://quasistatic_simulator/planar_hand.yml
robots:
  -
    name: arm_left
    Kp: [50, 25]
  -
    name: arm_right
    Kp: [50, 25]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_y_rotation_r_0.25m.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 2
  contact_detection_tolerance: 10.0
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/planar_hand_ball_small_ball.yml

```yaml
model_directive: package://quasistatic_simulator/planar_hand.yml
robots:
  -
    name: arm_left
    Kp: [50, 25]
  -
    name: arm_right
    Kp: [50, 25]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/sphere_yz_rotation_r_0.125m.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 2
  contact_detection_tolerance: 10.0
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

### models/q_sys/planar_hand_box.yml

```yaml
model_directive: package://quasistatic_simulator/planar_hand.yml
robots:
  -
    name: arm_left
    Kp: [50, 25]
  -
    name: arm_right
    Kp: [50, 25]

objects:
  -
    name: sphere
    file: package://quasistatic_simulator/box_0.4m_rotation.sdf

quasistatic_sim_params:
  gravity: [0, 0, 0.]
  nd_per_contact: 2
  contact_detection_tolerance: 10.0
  is_quasi_dynamic: True
  unactuated_mass_scale: .NAN

```

## Python signatures and reward/observation bodies (81 files)


### qsim/contact_results_logger.py

```
class ContactLogger(LeafSystem)
    def __init__(self, value, publish_period_seconds)
    def DoPublish(self, context, event)
```

### qsim/examples/box_ball_graze_2d/test_box_ball_graze_2d.py

```
class TestBoxBallGraze(TestCase)
    def setUp(self)
    def test_old_vs_new(self)
    def test_log_dynamics_gradients(self)
```

### qsim/examples/box_ball_graze_2d/visualize_piecewise_dynamics_new.py

```
def calc_dynamics(forward_mode)
```

### qsim/examples/gripper_ball_pinch_2d/plotting.py

```
def PlotForceDistance(t_sim, phi_log, lambda_n_log, friction_log, t_contact_mode_change, figsize, save_name)
def PlotVelocity(t_sim, v_tangent, v_normal, t_contact_mode_change)
def PlotLeftFingerPosition(t_sim1, q_log, qa_cmd_log, t_contact_mode_change, fig_size, save_name)
```

### qsim/examples/iiwa_block_stacking/inverse_kinematics.py

```
def calc_iwa_trajectory_for_point_tracking(plant, duration, num_knot_points, p_WQ_start, p_WQ_offset, R_WL7_start, R_WL7_final, q_initial_guess, p_L7Q)
```

### qsim/examples/iiwa_block_stacking/plot_time_step_comparisons.py

```
def get_angle_from_quaternion(q)
def get_roll_from_quaternion(q)
def compute_error_integral(q_logs)
def get_label(i)
```

### qsim/examples/iiwa_block_stacking/run_manual_quasistatic.py

```
def extract_log_for_object(q_log, model)
def run_quasistatic_sim_manually(h, is_visualizing)
```

### qsim/examples/iiwa_block_stacking/run_mbp_vs_quasistatic.py

```
def run_comparison(h_mbp, h_quasistatic, is_visualizing)
def compare_all_models(plant, loggers_dict_mbp_str, loggers_dict_quasistatic_str)
```

### qsim/examples/iiwa_block_stacking/simulation_parameters.py

```
def concatenate_traj_list(traj_list)
```

### qsim/examples/iiwa_block_stacking/tests/test_iiwa_block_stacking.py

```
class TestIiwaBlockStacking(TestCase)
    def setUp(self)
    def test_cpp_vs_python(self)
    def test_mbp_vs_quasistatic(self)
```

### qsim/examples/iiwa_block_stacking/tests/test_quasistatic_system.py

```
class TestQuasistaticSystem(TestCase)
    def test_quasistatic_system(self)
```

### qsim/examples/iiwa_external_loading/run_iiwa_external_loading.py

```
def run_comparison(is_visualizing, real_time_rate)
```

### qsim/examples/iiwa_external_loading/test_iiwa_external_loading.py

```
class TestIiwaExternalLoading(TestCase)
    def test_mbp_vs_quaistatic(self)
```

### qsim/examples/iiwa_traj_following/run_iiwa_traj_following.py

```
def run_comparison(is_visualizing, real_time_rate)
```

### qsim/examples/iiwa_traj_following/test_iiwa_traj_following.py

```
class TestIiwaTrajectoryFollowing(TestCase)
    def test_cpp_vs_python(self)
    def test_quasistatic_vs_mbp(self)
```

### qsim/examples/log_comparison.py

```
def calc_error_integral(q_knots, t, q_gt_traj)
def get_angle_from_quaternion(q)
def convert_quaternion_array_to_eigen_quaternion_traj(q_array, t)
def calc_quaternion_error_integral(q_list, t, q_traj)
def calc_pose_error_integral(pose_list_1, t1, pose_list_2, t2)
```

### qsim/examples/planar_hand_ball/test_planar_hand_ball.py

```
def simulate(sim, q0_dict, T, sim_params)
def compare_q_dict_logs(test_case, q_sim, q_dict_log1, q_dict_log2, tol)
class TestPlanarHandBall(TestCase)
    def setUp(self)
    def test_cpp_vs_python(self)
    def test_log_barrier(self)
    def test_B(self)
```

### qsim/examples/setup_simulations.py

```
class LoadApplier(LeafSystem)
    def __init__(self, F_WB_traj, body_idx)
    def calc_output(self, context, spatial_forces_vector)
def shift_q_traj_to_start_at_minus_h(q_traj, h)
def create_dict_keyed_by_model_instance_index(plant, q_dict_str)
def create_dict_keyed_by_string(plant, q_dict)
def find_t_final_from_commanded_trajectories(q_a_traj_dict)
def add_externally_applied_generalized_force(builder, spatial_force_input_port, F_WB_traj, body_idx)
def get_logs_from_sim(log_sinks_dict, sim)
def run_quasistatic_sim(q_parser, backend, q_a_traj_dict_str, q0_dict_str, is_visualizing, real_time_rate, meshcat)
def run_mbp_sim(model_directive_path, object_sdf_paths, q_a_traj_dict, q0_dict_str, robot_stiffness_dict, robot_controller_dict, h, gravity, is_visualizing, real_time_rate, meshcat)
def compare_q_sim_cpp_vs_py(test_case, q_parser, q_a_traj_dict_str, q0_dict_str, atol)
```

### qsim/examples/three_link_arm_block_pushing/run_3link_arm_pushing_2d.py

```
def calc_integral_errors(q_robot_log_mbp, q_box_log_mbp, t_mbp, q_robot_log_quasistatic, q_box_log_quasistatic, t_quasistatic)
```

### qsim/examples/three_link_arm_block_pushing/run_3link_arm_pushing_3d.py

```
def calc_integral_errors(q_robot_log_mbp, q_box_log_mbp, t_mbp, q_robot_log_quasistatic, q_box_log_quasistatic, t_quasistatic)
```

### qsim/examples/three_link_arm_block_pushing/test_2d.py

```
class Test3linkArmBoxPushing2D(TestCase)
    def setUp(self)
    def test_python_vs_cpp(self)
    def test_mbp_vs_quasistatic(self)
```

### qsim/examples/three_link_arm_block_pushing/test_3d.py

```
class Test3linkArmBoxPushing3D(TestCase)
    """cpp_vs_python is not done for this system because forward pushing is
 unstable/chaotic? A small numerical difference along the path can lead
 to the object veering to the left or right, giving rise to large
 differences between object trajectories."""
    def test_3link_arm_box_pushing_3d(self)
```

### qsim/examples/three_link_arm_block_pushing/utils.py

```
def create_3link_arm_controller_plant(gravity)
def run_mbp_quasistatic_comparison(quasistatic_model_path, q0_dict_str, is_visualizing, real_time_rate)
```

### qsim/examples/two_spheres_y/run_two_spheres_mbp.py

```
class SimpleTrajectorySource(LeafSystem)
    def __init__(self, q_traj)
    def calc_x(self, context, output)
    def set_t_start(self, t_start_new)
```

### qsim/meshcat_visualizer_old.py

```
"""This has been removed from drake as of Nov 30, 2022. But it is needed by our
plotly RRT visualization tools.

Warning:
    This module (the pure-Python implementation of MeshCat) is deprecated.
    Please use pydrake.geometry.MeshcatVisualizer and related instead.
    The deprecated code will be removed from Drake on or after 2022-09-01."""
def AddTriad(vis, name, prefix, length, radius, opacity)
class StringToRoleAction(Action)
    """Action that converts the string 'proximity' or 'illustration' to the
corresponding Role enumeration value."""
    def __init__(self, option_strings, dest, nargs)
    def __call__(self, parser, namespace, values, option_string)
class HydroTriSurface(Geometry)
    """Unique representation of the triangle surface mesh associated with
hydroelastic mesh representations. In this case, it's important that we
support per-face normals (we want as honest a representation of the
object as possible).

A mesh consisting of an arbitrary collection of triangular faces. To
co"""
    def __init__(self, vertices, normals)
    def lower(self, object_data)
class MeshcatVisualizer(LeafSystem)
    """Warning:
    This module (the pure-Python implementation of MeshCat) is deprecated.
    Please use pydrake.geometry.MeshcatVisualizer and related instead.
    The deprecated code will be removed from Drake on or after 2022-09-01.

MeshcatVisualizer is a System block that connects to the query output"""
    def add_argparse_argument(parser)
    def __init__(self, scene_graph, draw_period, prefix, zmq_url, open_browser, frames_to_draw, frames_opacity, axis_length, axis_radius, delete_prefix_on_load, role, prefer_hydro)
    def get_geometry_query_input_port(self)
    def set_planar_viewpoint(self, camera_position, camera_focus, xmin, xmax, ymin, ymax)
    def delete_prefix(self)
    def load(self, context)
    def DoPublish(self, context, event)
    def start_recording(self)
    def stop_recording(self)
    def publish_recording(self, play, repetitions)
    def reset_recording(self)
def ConnectMeshcatVisualizer(builder, scene_graph, output_port)
```

### qsim/model_paths.py

```
def add_package_paths_local(parser)
def create_2d_gripper_plant(builder)
```

### qsim/normalization_derivatives.py

```
def calc_normalization_derivatives(q)
```

### qsim/parser.py

```
class QuasistaticSystemBackend(Enum)
class QuasistaticParser()
    def __init__(self, quasistatic_model_path)
    def set_sim_params(self)
    def parse_path(self, model_path)
    def set_quasi_dynamic(self, is_quasi_dynamic)
    def get_gravity(self)
    def get_param_attribute(self, name)
    def get_robot_stiffness_by_name(self, name)
    def make_system(self, backend)
    def make_simulator_py(self)
    def make_simulator_cpp(self, has_objects)
    def make_robot_only_plant(self)
    def make_batch_simulator(self)
    def make_visualizer(self, visualization_type)
```

### qsim/simulator.py

```
class MyContactInfo()
    """Used as an intermediate storage structure for constructing
PointPairContactInfo.
n_W is pointing into body B.
dC_W are the tangent vectors spanning the tangent plane at the
contact point."""
    def __init__(self, bodyA_index, bodyB_index, geometry_id_A, geometry_id_B, p_WC_W, n_W, dC_W)
class QuasistaticSimulator()
    def __init__(self, model_directive_path, robot_stiffness_dict, object_sdf_paths, sim_params)
    def copy_sim_params(params_from)
    def check_params_validity(q_params)
    def get_sim_parmas_copy(self)
    def get_plant(self)
    def get_scene_graph(self)
    def get_all_models(self)
    def get_actuated_models(self)
    def get_Dq_nextDq(self)
    def get_Dq_nextDqa_cmd(self)
    def get_positions(self, model)
    def get_position_indices(self)
    def get_query_object(self)
    def get_contact_results(self)
    def get_velocity_indices(self)
    def num_actuated_dofs(self)
    def num_unactuated_dof(self)
    def get_dynamics_derivatives(self)
    def get_model_instance_name_to_index_map(self)
    def update_mbp_positions_from_vector(self, q)
    def update_mbp_positions(self, q_dict)
    def get_mbp_positions(self)
    def get_mbp_positions_as_vec(self)
    def calc_tau_ext(self, easf_list)
    def update_normal_and_tangential_jacobian_rows(self, body, pC_D, n_W, d_W, i_c, n_di, i_f_start, position_indices, Jn, Jf, jacobian_wrt_variable, plant, context)
    def find_model_instance_index_for_body(self, body)
    def calc_gravity_for_unactuated_models(self)
    def get_generalized_force_from_external_spatial_force(self, easf_list)
    def calc_contact_jacobians(self, contact_detection_tolerance)
    def update_contact_results(self, my_contact_info_list, beta, h, n_c, n_d, mu_list)
    def get_mbp_body_from_scene_graph_geometry(self, g_id)
    def get_position_indices_for_model(self, model_instance_index)
    def get_velocity_indices_for_model(self, model_instance_index)
    def get_friction_coefficient_for_signed_distance_pair(self, sdp)
    def calc_jacobian_and_phi(self, contact_detection_tolerance)
    def check_cvx_status(status)
    def set_sim_params(params)
    def convert_sim_params_into_dict(params)
    def calc_scaled_mass_matrix(self, h, unactuated_mass_scale)
    def form_Q_and_tau_h(self, q_dict, q_a_cmd_dict, tau_ext_dict, h, unactuated_mass_scale)
    def step_qp_mp(self, h, phi_constraints, J, Q, tau_h, gradient_mode)
    def step_log_mp(self, h, phi_constraints, J, Q, tau_h, gradient_mode, log_barrier_weight)
    def step_qp_cvx(self, h, phi_constraints, J, Q, tau_h, gradient_mode)
    def step_log_cvx(self, h, phi_constraints, J, Q, tau_h, gradient_mode, log_barrier_weight)
    def step(self, q_a_cmd_dict, tau_ext_dict, sim_params)
    def backward_qp(self, gradient_mode, h, q_dict, n_f, n_c, n_d, Jn)
    def backward_log(self, gradient_mode, h, v_h_dict, Q, J, phi_constraints, log_barrier_weight)
    def step_default(self, q_a_cmd_dict, tau_ext_dict)
    def get_E(Q_AB)
    def copy_model_instance_index_dict(q_dict)
    def calc_dfdu(self, Dv_nextDb, h, q_dict)
    def calc_dfdx(self, Dv_nextDb, Dv_nextDe, h, n_f, n_c, n_d, Jn)
    def calc_dfdu_numerical(self, q_dict, qa_cmd_dict, du, sim_params)
    def step_configuration(self, q_dict, dq_dict, unactuated_mass_scale)
    def create_plant_with_robots_and_objects(builder, model_directive_path, robot_names, object_sdf_paths, time_step, gravity)
```

### qsim/system.py

```
class QuasistaticSystem(LeafSystem)
    def __init__(self, q_sim, sim_params)
    def get_q_model_output_port(self, model)
    def get_commanded_positions_input_port(self, model)
    def copy_query_object_out(self, context, query_object_abstract_value)
    def copy_contact_results_out(self, context, contact_results_abstract_value)
    def set_initial_state(self, context, q0_dict)
    def update_q(self, context, discrete_state)
```

### qsim/tests/test_normalization_derivatives.py

```
class TestNormalizationDerivatives(TestCase)
    def test_normalization_derivatives(self)
```

### qsim/tests/test_qp_derivatives_cpp.py

```
def get_DzDG_active_from_DzDG(DzDG_vec, active_row_indices)
class TestQpDerivatives(TestCase)
    def setUp(self)
    def test_derivatives(self)
```

### qsim/tests/test_socp_derivatives_cpp.py

```
class TestSocpDerivativesCpp(TestCase)
    def setUp(self)
    def test_socp_derivatives_cpp(self)
```

### qsim/utils.py

```
def get_rotation_matrix_from_normal(normal)
def calc_tangent_vectors(normal, nd)
def is_mosek_gurobi_available()
```

### qsim/visualizer.py

```
class QsimVisualizationType(IntEnum)
    """We need to keep the python MeshcatVisualizer around, because plotly RRT
visualizer does not work with drake's CPP-based MeshcatVisualizer."""
class QuasistaticVisualizer()
    def __init__(self, q_sys, visualization_type)
    def get_body_id_to_meshcat_name_map(self)
    def create_context(self)
    def check_plants(plant_a, plant_b, models_all_a, models_all_b, velocity_indices_a, velocity_indices_b)
    def draw_configuration(self, q, contact_results)
    def draw_configuration_dict(self, q_dict, contact_results)
    def draw_goal_triad(self, length, radius, opacity, X_WG, name)
    def draw_object_triad(self, length, radius, opacity, path)
    def publish_trajectory(self, h, q_knots, contact_results_list)
```

### qsim_old/meshcat_camera_utils.py

```
def SetOrthographicCameraYZ(vis)
def SetOrthographicCameraXY(vis)
```

### qsim_old/problem_definition_graze.py

```
def calc_phi(q)
```

### qsim_old/problem_definition_pinch.py

```
def calc_phi(q)
```

### qsim_old/simulator.py

```
def calc_E(n_d, n_c)
class QuasistaticSimulator()
    def __init__(self, problem_definition, visualize, is_quasi_dynamic)
    def init_program(self, phi_l)
    def find_big_M(self, phi_l)
    def step_miqp(self, q, v_a_cmd)
    def step_lcp(self, q, q_a_cmd)
    def step_anitescu(self, q, q_a_cmd)
    def update_visualizer(self, q)
```