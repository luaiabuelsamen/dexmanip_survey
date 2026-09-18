# contact_models_comparison_2023

source: https://github.com/Simple-Robotics/Simple


commit: 03d4784ed87b2b4986c74564d20ef5544b30936d


## README

# The Simple Simulator: Simulation Made Simple

**Simple** is a new (differentiable) physical engine based on recent progress on solving contact simulation and leveraging [Pinocchio](https://github.com/stack-of-tasks/pinocchio) for fast dynamics computations and [Coal](https://github.com/coal-library/coal/) for efficient collision detection.
While first targetting robotics applications, **Simple** can be exploited in many other contexts: video games, system design, graphical animations, biomechanics, etc.

**Simple** is developed by the [WILLOW team](https://www.di.ens.fr/willow/) at [Inria](https://www.inria.fr/en).
The code associated with **Simple** has been released on May, 26th 2025 under the permissive BSD-3 license.

More features and improved efficiency will come soon. And as Jean de La Fontaine wrote: **"Patience and time do more than strength or passion"**.


 
## The core team

The following persons actively took part in the development of **Simple**:
- [Justin Carpentier](https://jcarpent.github.io/) (Inria): core developer and project instigator
- [Quentin Le Lidec](https://quentinll.github.io/) (Inria): core developer
- [Louis Montaut](https://lmontaut.github.io/) (Inria): core developer
- [Joris Vaillant](https://github.com/jorisv/) (Inria): core developer
- [Yann de Mont-Marin](https://github.com/ymontmarin) (Inria): core developer
- [Ajay Sathya](https://www.ajaysathya.com/) (Inria): feature contributor
- [Fabian Schramm](https://github.com/fabinsch) (Inria): feature contributor

External contributions are more than welcome. If you have contributed to the development of Simple, feel free to add your name.

## Associated scientific and technical publications

**Simple** is built on active research around understanding and enhancing physical simulation.
Interested readers can learn more about the algorithmic and computational foundations of **Simple** by reading these publications:

- Le Lidec, Q., Montaut, L. & Carpentier, J. (2024, July). [From Compliant to Rigid Contact Simulation: a Unified and Efficient Approach](https://hal.science/hal-04588906). In RSS 2024-Robotics: Science and Systems.
- Montaut, L., Le Lidec, Q., Petrik, V., Sivic, J., & Carpentier, J. (2024). [GJK++: Leveraging Acceleration Methods for Faster Collision Detection](https://hal.science/hal-04070039/). IEEE Transactions on Robotics.
- Sathya, A., & Carpentier, J. (2024). [Constrained Articulated Body Dynamics Algorithms](https://hal.science/hal-04443056/). IEEE Transactions on Robotics.
- Montaut, L., Le Lidec, Q., Bambade, A., Petrik, V., Sivic, J., & Carpentier, J. (2023, May). [Differentiable collision detection: a randomized smoothing approach](https://hal.science/hal-03780482/). In 2023 IEEE International Conference on Robotics and Automation (ICRA).
- Le Lidec, Q., Jallet, W., Montaut, L., Laptev, I., Schmid, C., & Carpentier, J. (2023). [Contact models in robotics: a comparative analysis](https://hal.science/hal-04067291/). IEEE Transactions on Robotics.
- Montaut, L., Le Lidec, Q., Petrik, V., Sivic, J., & Carpentier, J. (2022, June). [Collision Detection Accelerated: An Optimization Perspective](https://hal.science/hal-03662157/). In Robotics: Science and Systems (RSS 2O22).
- Carpentier, J., Budhiraja, R., & Mansard, N. (2021, July). [Proximal and sparse resolution of constrained dynamic equations](https://hal.science/hal-03271811/). In Robotics: Science and Systems (RSS 2021).
- Carpentier, J., & Mansard, N. (2018, June). [Analytical derivatives of rigid body dynamics algorithms](https://hal.science/hal-01790971/). In Robotics: Science and systems (RSS 2018).


## File tree (depth 3, assets pruned)

```
.clang-format
.cmake-format.yaml
.gitignore
.gitmodules
.pre-commit-config.yaml
CMakeLists.txt
LICENSE
README.md
benchmark/
  CMakeLists.txt
  affine-transform.cpp
  mujoco-humanoid.cpp
bindings/
  CMakeLists.txt
  python/
    CMakeLists.txt
    core/
    module.cpp
    simple/
cmake/
include/
  simple/
    bindings/
    core/
    fwd.hpp
    math/
    pch.hpp
    pinocchio_template_instantiation/
    utils/
sandbox/
  cartpole.py
  cassie_mj.py
  force_action_derivative.py
  four_bar_linkage.py
  four_five_bar_linkage.py
  go2_contact_id.py
  humanoid_mj.py
  parallel_rollout.py
  pendulum.py
  pin_utils.py
  robots/
    four_bar_linkage.xml
    four_five_bar_linkage.xml
    go2/
    humanoid.xml
    pendulum.xml
  sim_utils.py
  simulation_args.py
  simulation_utils.py
  test_memory.py
  viz_utils.py
sources.cmake
src/
  CMakeLists.txt
  core/
    constraints-problem.cpp
    simulator.cpp
  empty.cpp
  pinocchio_template_instantiation/
    aba-derivatives.cpp
    aba.cpp
    crba.cpp
    joint-model.cpp
tests/
  CMakeLists.txt
  forward/
    CMakeLists.txt
    mujoco-humanoid.cpp
    simulation-combine-constraints.cpp
    simulation-robots.cpp
    simulator-minimal.cpp
    simulator.cpp
    urdf-romeo.cpp
  python/
    test_simulator_instance.py
  test-utils.hpp
  test_data/
    config.h.in
    mujoco_humanoid.xml
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
ci:
  autoupdate_branch: devel
  autofix_prs: false
repos:
  - repo: https://github.com/pre-commit/mirrors-clang-format
    rev: v18.1.5
    hooks:
      - id: clang-format
        types_or: []
        types: [text]
        files: \.(cpp|cxx|c|h|hpp|hxx|txx)$
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files
      - id: check-case-conflict
      - id: check-yaml
        exclude: ^packaging/conda/
      - id: detect-private-key
#      - id: end-of-file-fixer
      - id: mixed-line-ending
      - id: check-merge-conflict
      - id: trailing-whitespace
        exclude: |
          (?x)^(
              doc/doxygen-awesome.*
          )$
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff-format
        exclude: doc/
  - repo: https://github.com/cheshirekow/cmake-format-precommit
    rev: v0.6.13
    hooks:
      - id: cmake-format
        additional_dependencies: [pyyaml>=5.1]
  - repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.5.5
    hooks:
      - id: forbid-tabs
  - repo: https://github.com/jumanjihouse/pre-commit-hook-yamlfmt
    rev: 0.2.3
    hooks:
      - id: yamlfmt
        args: [--mapping=2, --offset=2, --sequence=4, --implicit_start]

```

## Python signatures and reward/observation bodies (6 files)


### sandbox/sim_utils.py

```
class SimulationArgs(Tap)
def setupSimulatorFromArgs(sim, args)
def plotContactSolver(sim, args, t, q, v)
def subSample(xs, duration, fps)
def addSystemCollisionPairs(model, geom_model, qref)
def addFloor(geom_model, visual_model)
def addMaterialAndCompliance(geom_model, material, compliance)
def printSimulationPerfStats(step_timings)
def runMujocoXML(model_path, args)
def createVisualizer(model, geom_model, visual_model)
```

### sandbox/simulation_args.py

```
class SimulationArgs(Tap)
    def process_args(self)
class ControlArgs(SimulationArgs)
```

### sandbox/simulation_utils.py

```
class Policy()
    def __init__(self)
    def act(self, simulator, q, v, dt)
class DefaultPolicy(Policy)
    def __init__(self, model)
    def act(self, simulator, q, v, dt)
class FreeFloatingRobotDampingPolicy(Policy)
    def __init__(self, model, damping_factor)
    def act(self, simulator, q, v, dt)
class RobotArmDampingPolicy(Policy)
    def __init__(self, model, damping_factor)
    def act(self, simulator, q, v, dt)
def setPhysicsProperties(geom_model, material, compliance)
def removeBVHModelsIfAny(geom_model)
def addFloor(geom_model, visual_model)
def simulateSytem(model, geom_model, visual_model, q0, v0, policy, args)
```

### tests/python/test_simulator_instance.py

```
def setBallsAndHalfSpace(length, mass)
def test_init()
def test_init2()
def test_simulator_handles()
def test_init_empty()
def test_step()
def test_step_balls()
def test_step_balls_with_constraints()
def addSystemCollisionPairs(model, geom_model, qref)
def addFloor(geom_model)
def test_manipulator_limits()
def test_humanoid_limits()
def test_freeflyer_limits()
def test_composite_limits()
def test_mujoco_humanoid_limits()
```