# colosseum_2024

source: https://github.com/robot-colosseum/robot-colosseum


commit: 098a910ae1d490524adb49b8d50735b00a1a62de


## README

<p align="center">
    <h1 align="center">
        <img src="resources/media/img_emoji_rss.png" width="50px"/>
        Colosseum
    </h1>
    <h2 align="center">
        <a href="https://arxiv.org/abs/2402.08191">
        A Benchmark for Evaluating Generalization for Robotic Manipulation
        </a>
    </h2>
</p>

[Wilbert Pumacay<sup>*</sup>][2], [Ishika Singh<sup>*</sup>][3], [Jiafei Duan<sup>*</sup>][4], [Ranjay Krishna][5], [Jesse Thomason][6], [Dieter Fox][7]

<p align="center">
    <img src="resources/media/gif_perturbation_factors.gif"/>
</p>

Colosseum is a robotic manipulation benchmark built on top of [PyRep][0], which
implements 20 out of the original 100 tasks from [RLBench][1], and extends it by
supporting 14 variation factors that randomize parts of the simulation.

## Documentation

- Overview: [Overview][8]
- Getting started: [Installation][9], [Quickstart][10]
- Data Generation: [Data Generation][11]
- RVT baseline: [RVT baseline repo][12]

## Citation

```bibtex
@article{pumacay2024colosseum,
  title     = {THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation},
  author    = {Pumacay, Wilbert and Singh, Ishika and Duan, Jiafei and Krishna, Ranjay and Thomason, Jesse and Fox, Dieter},
  booktitle = {arXiv preprint arXiv:2402.08191},
  year      = {2024},
}
```


[0]: <https://github.com/stepjam/PyRep> (pyrep-gh-repo)
[1]: <https://github.com/stepjam/RLBench> (rlbench-gh-repo)
[2]: <https://wpumacay.github.io> (wilbert-site)
[3]: <https://ishikasingh.github.io> (ishika-site)
[4]: <https://duanjiafei.com> (jiafei-site)
[5]: <https://ranjaykrishna.com/index.html> (ranjay-site)
[6]: <https://jessethomason.com> (jesse-site)
[7]: <https://homes.cs.washington.edu/~fox> (dieter-site)
[8]: <https://robot-colosseum.readthedocs.io/en/latest/overview.html> (docs-site)
[9]: <https://robot-colosseum.readthedocs.io/en/latest/installation.html> (docs-installation)
[10]: <https://robot-colosseum.readthedocs.io/en/latest/quickstart.html> (docs-quickstart)
[11]: <https://robot-colosseum.readthedocs.io/en/latest/quickstart.html#collect-demonstrations> (docs-data-collection)
[12]: <https://github.com/robot-colosseum/rvt_colosseum> (rvt-colosseum-repo)


## File tree (depth 3, assets pruned)

```
.dockerignore
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
DATASET.md
Dockerfile_mesa
Dockerfile_nvidia
README.md
collect_dataset.sh
collect_dataset_cluster.sh
colosseum/
  __init__.py
  pyrep/
    __init__.py
    extensions/
  rlbench/
    __init__.py
    extensions/
    task_ttms/
    tasks/
    utils.py
  tools/
    __init__.py
    collect_demo.py
    dataset_generator.py
    task_builder.py
    visualize_task.py
  variations/
    __init__.py
    background_texture.py
    camera_pose.py
    const.py
    distractor_object.py
    light_color.py
    manager.py
    object_color.py
    object_friction.py
    object_mass.py
    object_size.py
    object_texture.py
    table_color.py
    table_texture.py
    utils.py
    variation.py
colosseum_tasks_distribution.xlsx
examples/
  example_object_color_variation.ipynb
  example_object_size_variation.ipynb
pyproject.toml
requirements-dev.txt
requirements.txt
resources/
setup.cfg
setup.py
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: check-added-large-files
        args: ["--maxkb=30720"] # max. 30MB for .ttm files
    -   id: check-case-conflict
    -   id: check-merge-conflict
    -   id: check-symlinks
    -   id: check-yaml
    -   id: name-tests-test
    -   id: debug-statements
    -   id: requirements-txt-fixer
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
    -   id: mixed-line-ending
        args: [--fix=lf]

-   repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.1.7
    hooks:
    -   id: remove-tabs

-   repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8

-   repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    -   id: isort
        name: isort (python)
        args: [--settings-path=pyproject.toml]

```

## Python signatures and reward/observation bodies (26 files)


### colosseum/pyrep/extensions/sim.py

```
def simSetObjectScale(shape_handle, scale)
def simGetObjectScale(shape_handle)
def simSetObjectsScale(objects_handles, scale)
def simGetConvexHullShape(pathAndFilename)
def simGetShapeTextureIdNoThrow(objectHandle)
def simGetShapeGeomInfo(shapeHandle)
def simExportMesh(shapeHandle, fileFormat, filepath)
```

### colosseum/rlbench/extensions/environment.py

```
class EnvironmentExt(Environment)
    def __init__(self, action_mode, dataset_root, obs_config, headless, static_positions, robot_setup, randomize_every, use_variations, frequency, vis_random_config, dyn_random_config, attach_grasped_objects, shaped_rewards, path_task_ttms, env_config)
    def launch(self)
    def get_task(self, task_class)
```

### colosseum/rlbench/extensions/task_environment.py

```
class TaskEnvironmentExt(TaskEnvironment)
    def __init__(self)
    def get_demos(self, amount, live_demos, image_paths, callable_each_step, max_attempts, random_selection, from_episode_number)
    def _get_live_demos(self, amount, callable_each_step, max_attempts)
    def reset_to_demo(self, demo)
```

### colosseum/rlbench/tasks/basketball_in_hoop.py

```
class BasketballInHoop(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### colosseum/rlbench/tasks/close_box.py

```
class CloseBox(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### colosseum/rlbench/tasks/close_laptop_lid.py

```
class CloseLaptopLid(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/empty_dishwasher.py

```
class EmptyDishwasher(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### colosseum/rlbench/tasks/get_ice_from_fridge.py

```
class GetIceFromFridge(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### colosseum/rlbench/tasks/hockey.py

```
class Hockey(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/insert_onto_square_peg.py

```
class InsertOntoSquarePeg(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/meat_on_grill.py

```
class MeatOnGrill(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/move_hanger.py

```
class MoveHanger(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def is_static_workspace(self)
```

### colosseum/rlbench/tasks/open_drawer.py

```
class OpenDrawer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### colosseum/rlbench/tasks/place_wine_at_rack_location.py

```
class PlaceWineAtRackLocation(Task)
    def init_task(self)
    def init_episode(self, index)
    def _move_to_rack(self, _)
    def _is_last(self, waypoint)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### colosseum/rlbench/tasks/put_money_in_safe.py

```
class PutMoneyInSafe(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### colosseum/rlbench/tasks/reach_and_drag.py

```
class ReachAndDrag(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/scoop_with_spatula.py

```
class ScoopWithSpatula(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/setup_chess.py

```
class SetupChess(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _move_above_next_target(self, _)
    def _repeat(self)
```

### colosseum/rlbench/tasks/slide_block_to_target.py

```
class SlideBlockToTarget(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/stack_cups.py

```
class StackCups(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/straighten_rope.py

```
class StraightenRope(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### colosseum/rlbench/tasks/turn_oven_on.py

```
class TurnOvenOn(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### colosseum/rlbench/tasks/wipe_desk.py

```
class WipeDesk(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
    def _place_dirt(self)
```

### colosseum/tools/task_builder.py

```
def print_fail(message, end)
def setup_list_completer()
class InvalidTaskName(Exception)
def name_to_task_class(task_file)
class LoadedTask(object)
    def __init__(self, pr, scene, robot)
    def _load_task_to_scene(self)
    def _edit_new_task(self)
    def _create_python_file(self, task_file)
    def _file_to_class_name(self, name)
    def reload_python(self)
    def new_task(self)
    def reset_variation(self)
    def new_variation(self)
    def new_episode(self)
    def new_demo(self)
    def save_task(self)
    def rename(self)
    def duplicate_task(self)
def main()
```

### colosseum/tools/visualize_task.py

```
def main(cfg)
```