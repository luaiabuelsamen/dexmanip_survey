# rlbench_2019

source: https://github.com/stepjam/RLBench


commit: 02720bba4c73fe02eb75df946b8791b806028a9d


## README

# RLBench: Robot Learning Benchmark [![Unit Tests](https://github.com/stepjam/RLBench/workflows/Unit%20Tests/badge.svg)](https://github.com/stepjam/RLBench/actions) [![Task Tests](https://github.com/stepjam/RLBench/workflows/Task%20Tests/badge.svg)](https://github.com/stepjam/RLBench/actions) [![Discord](https://img.shields.io/discord/694945190867370155.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/DXPCjmd)

![task grid image missing](readme_files/task_grid.png)

**RLBench** is an ambitious large-scale benchmark and learning environment 
designed to facilitate research in a number of vision-guided manipulation
research areas, including: reinforcement learning, imitation learning,
multi-task learning, geometric computer vision, and in particular, 
few-shot learning. [Click here for website and paper.](https://sites.google.com/corp/view/rlbench)

**Contents:**
- [Announcements](#announcements)
- [Install](#install)
- [Running Headless](#running-headless)
- [Getting Started](#getting-started)
    - [Few-Shot Learning and Meta Learning](#few-shot-learning-and-meta-learning)
    - [Reinforcement Learning](#reinforcement-learning)
    - [Sim-to-Real](#sim-to-real)
    - [Imitation Learning](#imitation-learning)
    - [Multi-Task Learning](#multi-task-learning)
    - [RLBench Gym](#rlbench-gym)
    - [Swapping Arms](#swapping-arms)
- [Tasks](#tasks)
- [Task Building](#task-building)
- [Gotchas!](#gotchas)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Citation](#citation)

## Announcements

### 11 May 2022

- Shaped rewards added for: **reach_target** and **take_lid_off_saucepan**. Pass `shaped_rewards=True` to `Environement` class

### 18 February 2022

- **Version 1.2.0 is live!** Note: This release will cause code-breaking API changes for action modes.

### 1 July 2021

- New instructions on headless GPU rendering [here](#running-headless)!

### 8 September 2020

- New tutorial series on task creation [here](https://www.youtube.com/watch?v=bKaK_9O3v7Y&list=PLsffAlO5lBTRiBwnkw2-x0U7t6TrNCkfc)!

### 1 April 2020

- We added a Discord channel to allow the RLBench community to help one another. Click the Discord badge above.

### 28 January 2020

- RLBench has been accepted to RA-L with presentation at ICRA!
- Ability to easily swap out arms added. [See here](#swapping-arms).

### 17 December 2019

- Gym is now supported!


## Install

RLBench is built around CoppeliaSim v4.1.0 and [PyRep](https://github.com/stepjam/PyRep).

First, install CoppeliaSim:

```bash
# set env variables
export COPPELIASIM_ROOT=${HOME}/CoppeliaSim
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COPPELIASIM_ROOT
export QT_QPA_PLATFORM_PLUGIN_PATH=$COPPELIASIM_ROOT

wget https://downloads.coppeliarobotics.com/V4_1_0/CoppeliaSim_Edu_V4_1_0_Ubuntu20_04.tar.xz
mkdir -p $COPPELIASIM_ROOT && tar -xf CoppeliaSim_Edu_V4_1_0_Ubuntu20_04.tar.xz -C $COPPELIASIM_ROOT --strip-components 1
rm -rf CoppeliaSim_Edu_V4_1_0_Ubuntu20_04.tar.xz
```

To install the RLBench python package:

```bash
pip install git+https://github.com/stepjam/RLBench.git
```

And that's it!

## Running Headless

If you are running on a machine without display (i.e. Cloud VMs, compute clusters),
you can refer to the following guide to run RLBench headlessly with rendering.

### Initial setup

First, configure your X config. This should only be done once to set up.

```bash
sudo nvidia-xconfig -a --use-display-device=None --virtual=1280x1024
echo -e 'Section "ServerFlags"\n\tOption "MaxClients" "2048"\nEndSection\n' \
    | sudo tee /etc/X11/xorg.conf.d/99-maxclients.conf
```

Leave out `--use-display-device=None` if the GPU is headless, i.e. if it has no display outputs.

### Running X

Then, whenever you want to run RLBench, spin up X.

```bash
# nohup and disown is important for the X server to keep running in the background
sudo nohup X :99 & disown
```

Test if your display works using glxgears.

```bash
DISPLAY=:99 glxgears
```

If you have multiple GPUs, you can select your GPU by doing the following.

```bash
DISPLAY=:99.<gpu_id> glxgears
```

### Running X without sudo

To spin up X with non-sudo users, edit file '/etc/X11/Xwrapper.config' and replace line:

```
allowed_users=console
```
with lines:
```
allowed_users=anybody
needs_root_rights=yes
```
If the file does not exist already, you can create it.

## Getting Started

The benchmark places particular emphasis on few-shot learning and meta learning 
due to breadth of tasks available, though it can be used in numerous ways. Before using RLBench, 
checkout the [Gotchas](#gotchas) section.

### Few-Shot Learning and Meta Learning

We have created splits of tasks called 'Task Sets', which consist of a 
collection of X training tasks and 5 tests tasks. Here X can be 10, 25, 50, or 95.
For example, to work on the task set with 10 training tasks, we import `FS10_V1`:

```python
import numpy as np
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.tasks import FS10_V1

action_mode = MoveArmThenGripper(
  arm_action_mode=JointVelocity(),
  gripper_action_mode=Discrete()
)
env = Environment(action_mode)
env.launch()

train_tasks = FS10_V1['train']
test_tasks = FS10_V1['test']
task_to_train = np.random.choice(train_tasks, 1)[0]
task = env.get_task(task_to_train)
task.sample_variation()  # random variation
descriptions, obs = task.reset()
obs, reward, terminate = task.step(np.random.normal(size=env.action_shape))
```

A full example can be seen in [examples/few_shot_rl.py](examples/few_shot_rl.py).

### Reinforcement Learning

```python
import numpy as np
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.tasks import ReachTarget

action_mode = MoveArmThenGripper(
  arm_action_mode=JointVelocity(),
  gripper_action_mode=Discrete()
)
env = Environment(action_mode)
env.launch()

task = env.get_task(ReachTarget)
descriptions, obs = task.reset()
obs, reward, terminate = task.step(np.random.normal(size=env.action_shape))
```

A full example can be seen in [examples/single_task_rl.py](examples/single_task_rl.py).
If you would like to bootstrap from demonstrations, then take a look at [examples/single_task_rl_with_demos.py](examples/single_task_rl_with_demos.py).


### Sim-to-Real

```python
import numpy as np
from rlbench import Environment
from rlbench import RandomizeEvery
from rlbench import VisualRandomizationConfig
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.tasks import OpenDoor

# We will borrow some from the tests dir
rand_config = VisualRandomizationConfig(
    image_directory='../tests/unit/assets/textures')

action_mode = MoveArmThenGripper(
  arm_action_mode=JointVelocity(),
  gripper_action_mode=Discrete()
)
env = Environment(
    action_mode, randomize_every=RandomizeEvery.EPISODE, 
    frequency=1, visual_randomization_config=rand_config)

env.launch()

task = env.get_task(OpenDoor)
descriptions, obs = task.reset()
obs, reward, terminate = task.step(np.random.normal(size=env.action_shape))
```

A full example can be seen in [examples/single_task_rl_domain_randomization.py](examples/single_task_rl_domain_randomization.py).

### Imitation Learning

```python
import numpy as np
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.tasks import ReachTarget

# To use 'saved' demos, set the path below
DATASET = 'PATH/TO/YOUR/DATASET'

action_mode = MoveArmThenGripper(
  arm_action_mode=JointVelocity(),
  gripper_action_mode=Discrete()
)
env = Environment(action_mode, DATASET)
env.launch()

task = env.get_task(ReachTarget)

demos = task.get_demos(2)  # -> List[List[Observation]]
demos = np.array(demos).flatten()

batch = np.random.choice(demos, replace=False)
batch_images = [obs.left_shoulder_rgb for obs in batch]
predicted_actions = predict_action(batch_images)
ground_truth_actions = [obs.joint_velocities for obs in batch]
loss = behaviour_cloning_loss(ground_truth_actions, predicted_actions)

```

A full example can be seen in [examples/imitation_learning.py](examples/imitation_learning.py).

### Multi-Task Learning

We have created splits of tasks called 'Task Sets', which consist of a 
collection of X training tasks. Here X can be 15, 30, 55, or 100.
For example, to work on the task set with 15 training tasks, we import `MT15_V1`:

```python
import numpy as np
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.tasks import MT15_V1

action_mode = MoveArmThenGripper(
  arm_action_mode=JointVelocity(),
  gripper_action_mode=Discrete()
)
env = Environment(action_mode)
env.launch()

train_tasks = MT15_V1['train']
task_to_train = np.random.choice(train_tasks, 1)[0]
task = env.get_task(task_to_train)
task.sample_variation()  # random variation
descriptions, obs = task.reset()
obs, reward, terminate = task.step(np.random.normal(size=env.action_shape))
```

A full example can be seen in [examples/multi_task_learning.py](examples/multi_task_learning.py).

### RLBench Gym

RLBench is __Gym__ compatible! Ensure you have gym installed (`pip3 install gym`).

Simply select your task of interest from [rlbench/tasks/](rlbench/tasks/), and
then load the task by using the task name (e.g. 'reach_target') followed by
the observation mode: 'state' or 'vision'.

```python
import gym
import rlbench

env = gym.make('reach_target-state-v0')
# Alternatively, for vision:
# env = gym.make('reach_target-vision-v0')

training_steps = 120
episode_length = 40
for i in range(training_steps):
    if i % episode_length == 0:
        print('Reset Episode')
        obs = env.reset()
    obs, reward, terminate, _ = env.step(env.action_space.sample())
    env.render()  # Note: rendering increases step time.

print('Done')
env.close()
```

A full example can be seen in [examples/rlbench_gym.py](examples/rlbench_gym.py).

### Swapping Arms

The default Franka Panda Arm _can_ be swapped out for another. This can be
useful for those who have custom tasks or want to perform sim-to-real 
experiments on the tasks. However, if you swap out the arm, then we can't 
guarantee that the task will be solvable.
For example, the Mico arm has a very small workspace in comparison to the
Franka.

**For benchmarking, the arm should remain as the Franka Panda.**

Currently supported arms:

- Franka Panda arm with Franka gripper `(franka)`
- Mico arm with Mico gripper `(mico)`
- Jaco arm with 3-finger Jaco gripper `(jaco)`
- Sawyer arm with Baxter gripper `(sawyer)`
- UR5 arm with Robotiq 85 gripper `(ur5)`

You can then swap out the arm using `robot_configuration`:

```python
env = Environment(action_mode=action_mode, robot_setup='sawyer')
```

A full example (using the Sawyer) can be seen in [examples/swap_arm.py](examples/swap_arm.py).

_Don't see the arm that you want to use?_ Your first step is to make sure it is
in PyRep, and if not, then you can follow the instructions for importing new
arm on the PyRep GitHub page. After that, feel free to open an issue and 
we can being it in to RLBench for you.

## Tasks

To see a full list of all tasks, [see here](rlbench/tasks).

To see gifs of each of the tasks, [see here](https://drive.google.com/drive/folders/1TqbulbbCEqVBd6SBHatphFlUK2JQLkYu?usp=sharing).

## Task Building

The task building tool is the interface for users who wish to create new tasks 
to be added to the RLBench task repository. Each task has 2 associated files: 
a V-REP model file (_.ttm_), which holds all of the scene information and demo 
waypoints, and a python (_.py_) file, which is responsible for wiring the 
scene objects to the RLBench backend, applying variations, defining success
criteria, and adding other more complex task behaviours.

Video tutorial series [here](https://www.youtube.com/watch?v=bKaK_9O3v7Y&list=PLsffAlO5lBTRiBwnkw2-x0U7t6TrNCkfc)!

In-depth text tutorials:
- [Simple Task](tutorials/simple_task.md)
- [Complex Task](tutorials/complex_task.md)

## Gotchas!

- **Using low-dimensional task observations (rather than images):** RLBench was designed to be challenging, putting emphasis on vision rather than 
toy-based low dimensional inputs. Although each task does supply a low-dimensional
output this should be used with extreme caution!
    - Why? Imagine you are training a reinforcement learning agent to pick up a block; halfway through
    training, the block slips from the gripper and falls of the table. These low-dimensional values
    will now be out of distribution. I.e. RLBench does not safeguard against objects going out of the 
    workspace. This issue does not arise when using image-based observations. 
    
- **Using non-standard image size:** RLBench by default uses image observation sizes of 128x128.
When using an alternative size, be aware that you may need to collect your saved demonstrations again.
    - Why? If we instead specify a 64x64 image observation size to the `ObservationConfig` then the
    scene cameras will now render to that size. However, the saved demos on disk will now be **resized**
    to be 64x64.
    This resizing will of course mean that small artifacts may be present in stored demos
    that may not be present in the 'live' observations from the scene. Instead, prefer to re-collect demos
    using the image observation sized you plan to use in the 'live' environment.
    

## Contributing

New tasks using our task building tool, in addition to bug fixes, are very 
welcome! When building your task, please ensure that you run the task validator
in the task building tool.

A full contribution guide is coming soon!

## Acknowledgements

Models were supplied from turbosquid.com, cgtrader.com, free3d.com, 
thingiverse.com, and cadnav.com.

## Citation

```
@article{james2019rlbench,
  title={RLBench: The Robot Learning Benchmark \& Learning Environment},
  author={James, Stephen and Ma, Zicong and Rovick Arrojo, David and Davison, Andrew J.},
  journal={IEEE Robotics and Automation Letters},
  year={2020}
}
```


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    task_tests.yml
    unit_tests.yml
.gitignore
LICENSE
README.md
examples/
  custom_action_mode.py
  few_shot_rl.py
  imitation_learning.py
  multi_task_rl.py
  rearrangement_challenge.py
  rlbench_gym.py
  rlbench_gym_vector.py
  single_task_rl.py
  single_task_rl_domain_randomization.py
  single_task_rl_with_demos.py
  swap_arm.py
readme_files/
  task_grid.png
rlbench/
  __init__.py
  action_modes/
    __init__.py
    action_mode.py
    arm_action_modes.py
    gripper_action_modes.py
  backend/
    __init__.py
    conditions.py
    const.py
    exceptions.py
    observation.py
    robot.py
    scene.py
    spawn_boundary.py
    task.py
    task_utils.py
    utils.py
    waypoints.py
  const.py
  dataset_generator.py
  demo.py
  environment.py
  gym.py
  noise_model.py
  observation_config.py
  robot_ttms/
    __init__.py
    jaco.ttm
    mico.ttm
    panda.ttm
    sawyer.ttm
    ur5.ttm
  sim2real/
    __init__.py
    domain_randomization.py
    domain_randomization_scene.py
  task_design.ttt
  task_environment.py
  task_ttms/
    __init__.py
    basketball_in_hoop.ttm
    beat_the_buzz.ttm
    block_pyramid.ttm
    change_channel.ttm
    change_clock.ttm
    close_box.ttm
    close_door.ttm
    close_drawer.ttm
    close_fridge.ttm
    close_grill.ttm
    close_jar.ttm
    close_laptop_lid.ttm
    close_microwave.ttm
    cut_vegetables.ttm
    empty_container.ttm
    empty_dishwasher.ttm
    get_ice_from_fridge.ttm
    hang_frame_on_hanger.ttm
    hit_ball_with_queue.ttm
    hockey.ttm
    insert_onto_square_peg.ttm
    insert_usb_in_computer.ttm
    lamp_off.ttm
    lamp_on.ttm
    lift_numbered_block.ttm
    light_bulb_in.ttm
    light_bulb_out.ttm
    meat_off_grill.ttm
    meat_on_grill.ttm
    move_hanger.ttm
    open_box.ttm
    open_door.ttm
    open_drawer.ttm
    open_fridge.ttm
    open_grill.ttm
    open_jar.ttm
    open_microwave.ttm
    open_oven.ttm
    open_washing_machine.ttm
    open_window.ttm
    open_wine_bottle.ttm
    phone_on_base.ttm
    pick_and_lift.ttm
    pick_and_lift_small.ttm
    pick_up_cup.ttm
    place_cups.ttm
    place_hanger_on_rack.ttm
    place_shape_in_shape_sorter.ttm
    play_jenga.ttm
    plug_charger_in_power_supply.ttm
    pour_from_cup_to_cup.ttm
    press_switch.ttm
    push_button.ttm
    push_buttons.ttm
    put_all_groceries_in_cupboard.ttm
    put_books_on_bookshelf.ttm
    put_bottle_in_fridge.ttm
    put_groceries_in_cupboard.ttm
    put_item_in_drawer.ttm
    put_knife_in_knife_block.ttm
    put_knife_on_chopping_board.ttm
    put_money_in_safe.ttm
    put_plate_in_colored_dish_rack.ttm
    put_rubbish_in_bin.ttm
    put_shoes_in_box.ttm
    put_toilet_roll_on_stand.ttm
    put_tray_in_oven.ttm
    put_umbrella_in_umbrella_stand.ttm
    reach_and_drag.ttm
    reach_target.ttm
    remove_cups.ttm
    scoop_with_spatula.ttm
    screw_nail.ttm
    set_the_table.ttm
    setup_checkers.ttm
    setup_chess.ttm
    slide_block_to_target.ttm
    slide_cabinet_open.ttm
    slide_cabinet_open_and_place_cups.ttm
    solve_puzzle.ttm
    stack_blocks.ttm
    stack_chairs.ttm
    stack_cups.ttm
    stack_wine.ttm
    straighten_rope.ttm
    sweep_to_dustpan.ttm
    take_cup_out_from_cabinet.ttm
    take_frame_off_hanger.ttm
    take_item_out_of_drawer.ttm
    take_lid_off_saucepan.ttm
    take_money_out_safe.ttm
    take_off_weighing_scales.ttm
    take_plate_off_colored_dish_rack.ttm
    take_shoes_out_of_box.ttm
    take_toilet_roll_off_stand.ttm
    take_tray_out_of_oven.ttm
    take_umbrella_out_of_umbrella_stand.ttm
    take_usb_out_of_computer.ttm
    toilet_seat_down.ttm
    toilet_seat_up.ttm
    turn_oven_on.ttm
    turn_tap.ttm
    tv_on.ttm
    unplug_charger.ttm
    water_plants.ttm
    weighing_scales.ttm
    wipe_desk.ttm
  tasks/
    __init__.py
    basketball_in_hoop.py
    beat_the_buzz.py
    block_pyramid.py
    change_channel.py
    change_clock.py
    close_box.py
    close_door.py
    close_drawer.py
    close_fridge.py
    close_grill.py
    close_jar.py
    close_laptop_lid.py
    close_microwave.py
    empty_container.py
    empty_dishwasher.py
    get_ice_from_fridge.py
    hang_frame_on_hanger.py
    hit_ball_with_queue.py
    hockey.py
    insert_onto_square_peg.py
    insert_usb_in_computer.py
    lamp_off.py
    lamp_on.py
    lift_numbered_block.py
    light_bulb_in.py
    light_bulb_out.py
    meat_off_grill.py
    meat_on_grill.py
    move_hanger.py
    open_box.py
    open_door.py
    open_drawer.py
    open_fridge.py
    open_grill.py
    open_jar.py
    open_microwave.py
    open_oven.py
    open_washing_machine.py
    open_window.py
    open_wine_bottle.py
    phone_on_base.py
    pick_and_lift.py
    pick_and_lift_small.py
    pick_up_cup.py
    place_cups.py
    place_hanger_on_rack.py
    place_shape_in_shape_sorter.py
    play_jenga.py
    plug_charger_in_power_supply.py
    pour_from_cup_to_cup.py
    press_switch.py
    push_button.py
    push_buttons.py
    put_all_groceries_in_cupboard.py
    put_books_on_bookshelf.py
    put_bottle_in_fridge.py
    put_groceries_in_cupboard.py
    put_item_in_drawer.py
    put_knife_in_knife_block.py
    put_knife_on_chopping_board.py
    put_money_in_safe.py
    put_plate_in_colored_dish_rack.py
    put_rubbish_in_bin.py
    put_shoes_in_box.py
    put_toilet_roll_on_stand.py
    put_tray_in_oven.py
    put_umbrella_in_umbrella_stand.py
    reach_and_drag.py
    reach_target.py
    remove_cups.py
    scoop_with_spatula.py
    screw_nail.py
    set_the_table.py
    setup_checkers.py
    setup_chess.py
    slide_block_to_target.py
    slide_cabinet_open.py
    slide_cabinet_open_and_place_cups.py
    solve_puzzle.py
    stack_blocks.py
    stack_chairs.py
    stack_cups.py
    stack_wine.py
    straighten_rope.py
    sweep_to_dustpan.py
    take_cup_out_from_cabinet.py
    take_frame_off_hanger.py
    take_item_out_of_drawer.py
    take_lid_off_saucepan.py
    take_money_out_safe.py
    take_off_weighing_scales.py
    take_plate_off_colored_dish_rack.py
    take_shoes_out_of_box.py
    take_toilet_roll_off_stand.py
    take_tray_out_of_oven.py
    take_umbrella_out_of_umbrella_stand.py
    take_usb_out_of_computer.py
    toilet_seat_down.py
    toilet_seat_up.py
    turn_oven_on.py
    turn_tap.py
    tv_on.py
    unplug_charger.py
    water_plants.py
    weighing_scales.py
    wipe_desk.py
  utils.py
setup.py
tests/
  __init__.py
  demos/
    __init__.py
    test_demos.py
  unit/
    __init__.py
    test_domain_randomization_environment.py
    test_environment.py
    test_examples.py
    test_gym.py
    test_scene.py
    test_task_sets.py
    test_tasks.py
tools/
  cinematic_recorder.py
  task_builder.py
  task_validator.py
tutorials/
  complex_task.md
  simple_task.md
  tutorial_images/
    1base_1wall.png
    adjust_shape_color_labeled.png
    change_proxsense_size_labeled.png
    container_wall.png
    create_cuboid_dialog.png
    create_new_task_labeled.png
    create_task_dialog_labeled.png
    cuboid_plane.png
    dimensions0.png
    dummy_orient.png
    empty_container.gif
    grouping.gif
    invert_vis_layer.gif
    just_boxes.png
    large_container_scene.png
    make_grey.png
    multiple_strings.png
    object_special_properties.png
    parent_child_tree.png
    pos_relto_parent.png
    prox_sense_params.png
    rotate_wall.png
    save_builder.gif
    scaling_factors_labeled.png
    set_dummy_orient_labeled.png
    slide_block_to_target.gif
    spawn_boundary.png
    task_descriptions.png
    task_design_empty.png
    task_design_empty_labeled.png
    translate_cuboid_labeled.png
    translate_z_manually.png
    translation_trick.png
    view_labeled.png
    w0_ext_string.png
    waypoints_added.png
urdfs/
  panda/
    panda.urdf
```

## Config files (1)


### .github/workflows/task_tests.yml

```yaml
name: Task Tests

# Controls when the action will run.
# Run this workflow every time a new commit pushed to your repository
on:
  # Triggers the workflow on push or pull request events.
  push:
  pull_request:

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-20.04
    env:
      DISPLAY: :0

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      - name: Test
        run: |
          sudo apt-get update -qq
          sudo apt-get install -y xvfb qtbase5-dev qtdeclarative5-dev libqt5webkit5-dev libsqlite3-dev qt5-default qttools5-dev-tools
          # start xvfb in the background
          sudo /usr/bin/Xvfb $DISPLAY -screen 0 1280x1024x24 &
          cur=`pwd`
          wget https://downloads.coppeliarobotics.com/V4_1_0/CoppeliaSim_Edu_V4_1_0_Ubuntu20_04.tar.xz
          tar -xf CoppeliaSim_Edu_V4_1_0_Ubuntu20_04.tar.xz
          export COPPELIASIM_ROOT="$cur/CoppeliaSim_Edu_V4_1_0_Ubuntu20_04"
          export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COPPELIASIM_ROOT:$COPPELIASIM_ROOT/platforms
          export QT_QPA_PLATFORM_PLUGIN_PATH=$COPPELIASIM_ROOT

          pip install ".[gym,dev]"
          pip install "pytest-xdist[psutil]"
          pytest -v -n auto tests/demos

```

## Python signatures and reward/observation bodies (132 files)


### examples/custom_action_mode.py

```
class CustomAbsoluteJointVelocity(JointVelocity)
    def action(self, scene, action)
class Agent(object)
    def __init__(self, action_shape)
    def act(self, obs)
```

### examples/multi_task_rl.py

```
class Agent(object)
    def __init__(self, action_shape)
    def act(self, obs)
```

### examples/single_task_rl.py

```
class Agent(object)
    def __init__(self, action_shape)
    def act(self, obs)
```

### examples/single_task_rl_domain_randomization.py

```
class Agent(object)
    def __init__(self, action_shape)
    def act(self, obs)
```

### examples/single_task_rl_with_demos.py

```
class Agent(object)
    def __init__(self, action_shape)
    def ingest(self, demos)
    def act(self, obs)
```

### rlbench/action_modes/action_mode.py

```
class ActionMode(object)
    def __init__(self, arm_action_mode, gripper_action_mode)
    def action(self, scene, action)
    def action_shape(self, scene)
    def action_bounds(self)
class MoveArmThenGripper(ActionMode)
    """A customizable action mode.

The arm action is first applied, followed by the gripper action."""
    def action(self, scene, action)
    def action_shape(self, scene)
class JointPositionActionMode(ActionMode)
    """A pre-set, delta joint position action mode or arm and abs for gripper.

Both the arm and gripper action are applied at the same time."""
    def __init__(self)
    def action(self, scene, action)
    def action_shape(self, scene)
    def action_bounds(self)
```

### rlbench/action_modes/arm_action_modes.py

```
def assert_action_shape(action, expected_shape)
def assert_unit_quaternion(quat)
def calculate_delta_pose(robot, action)
class RelativeFrame(Enum)
class ArmActionMode(object)
    def action(self, scene, action)
    def action_step(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
    def set_control_mode(self, robot)
class JointVelocity(ArmActionMode)
    """Control the joint velocities of the arm.

Similar to the action space in many continious control OpenAI Gym envs."""
    def action(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
    def set_control_mode(self, robot)
class JointPosition(ArmActionMode)
    """Control the target joint positions (absolute or delta) of the arm.

The action mode opoerates in absolute mode or delta mode, where delta
mode takes the current joint positions and adds the new joint positions
to get a set of target joint positions. The robot uses a simple control
loop to execute un"""
    def __init__(self, absolute_mode)
    def action(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
class JointTorque(ArmActionMode)
    """Control the joint torques of the arm.
    """
    def _torque_action(self, robot, action)
    def action(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
    def set_control_mode(self, robot)
class EndEffectorPoseViaPlanning(ArmActionMode)
    """High-level action where target pose is given and reached via planning.

Given a target pose, a linear path is first planned (via IK). If that fails,
sample-based planning will be used. The decision to apply collision
checking is a crucial trade off! With collision checking enabled, you
are guarantee"""
    def __init__(self, absolute_mode, frame, collision_checking)
    def _quick_boundary_check(self, scene, action)
    def _pose_in_end_effector_frame(self, robot, action)
    def action(self, scene, action)
    def action_shape(self, scene)
class EndEffectorPoseViaIK(ArmActionMode)
    """High-level action where target pose is given and reached via IK.

Given a target pose, IK via inverse Jacobian is performed. This requires
the target pose to be close to the current pose, otherwise the action
will fail. It is up to the user to constrain the action to
meaningful values.

The decision"""
    def __init__(self, absolute_mode, frame, collision_checking)
    def action(self, scene, action)
    def action_shape(self, scene)
class ERJointViaIK(ArmActionMode)
    """High-level action where target EE pose + Elbow angle is given in ER 
space (End-Effector and Elbow) and reached via IK.

Given a target pose, IK via inverse Jacobian is performed. This requires
the target pose to be close to the current pose, otherwise the action
will fail. It is up to the user to c"""
    def __init__(self, absolute_mode, frame, collision_checking, commanded_joints, eps, delta_angle)
    def action(self, scene, action)
    def action_shape(self, _)
```

### rlbench/action_modes/gripper_action_modes.py

```
def assert_action_shape(action, expected_shape)
class GripperActionMode(object)
    def action(self, scene, action)
    def action_step(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
    def action_bounds(self)
class Discrete(GripperActionMode)
    """Control if the gripper is open or closed in a discrete manner.

Action values > 0.5 will be discretised to 1 (open), and values < 0.5
will be  discretised to 0 (closed)."""
    def __init__(self, attach_grasped_objects, detach_before_open)
    def _actuate(self, action, scene)
    def action(self, scene, action)
    def action_shape(self, scene)
    def action_bounds(self)
class GripperJointPosition(GripperActionMode)
    """Control the target joint positions absolute or delta) of the gripper.

The action mode opoerates in absolute mode or delta mode, where delta
mode takes the current joint positions and adds the new joint positions
to get a set of target joint positions. The robot uses a simple control
loop to execute"""
    def __init__(self, attach_grasped_objects, detach_before_open, absolute_mode)
    def action(self, scene, action)
    def action_pre_step(self, scene, action)
    def action_step(self, scene, action)
    def action_post_step(self, scene, action)
    def action_shape(self, scene)
    def action_bounds(self)
```

### rlbench/backend/observation.py

```
class Observation(object)
    """Storage for both visual and low-dimensional observations."""
    def __init__(self, left_shoulder_rgb, left_shoulder_depth, left_shoulder_mask, left_shoulder_point_cloud, right_shoulder_rgb, right_shoulder_depth, right_shoulder_mask, right_shoulder_point_cloud, overhead_rgb, overhead_depth, overhead_mask, overhead_point_cloud, wrist_rgb, wrist_depth, wrist_mask, wrist_point_cloud, front_rgb, front_depth, front_mask, front_point_cloud, joint_velocities, joint_positions, joint_forces, gripper_open, gripper_pose, gripper_matrix, gripper_joint_positions, gripper_touch_forces, task_low_dim_state, misc)
    def get_low_dim_data(self)
```

### rlbench/backend/task.py

```
class Task(object)
    def __init__(self, pyrep, robot, name)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def get_low_dim_state(self)
    def step(self)
    def reward(self)
    def cleanup(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
    def decorate_observation(self, observation)
    def is_static_workspace(self)
    def set_initial_objects_in_scene(self)
    def register_success_conditions(self, condition)
    def register_fail_conditions(self, condition)
    def register_graspable_objects(self, objects)
    def register_waypoint_ability_start(self, waypoint_index, func)
    def register_waypoint_ability_end(self, waypoint_index, func)
    def register_waypoints_should_repeat(self, func)
    def register_stop_at_waypoint(self, waypoint_index)
    def get_name(self)
    def validate(self)
    def get_waypoints(self)
    def should_repeat_waypoints(self)
    def get_graspable_objects(self)
    def success(self)
    def load(self)
    def unload(self)
    def cleanup_(self)
    def clear_registerings(self)
    def get_base(self)
    def get_state(self)
    def restore_state(self, state)
    def _feasible(self, waypoints)
    def _get_waypoints(self, validating)

```python
def reward(self) -> Union[float, None]:
        """Allows the user to customise the task and add reward shaping."""
        return None
```

```python
def decorate_observation(self, observation: Observation) -> Observation:
        """Can be used for tasks that want to modify the observations.

        Usually not used. Perhpas cabn be used to model

        :param observation: The Observation for this time step.
        :return: The modified Observation.
        """
        return observation
```
```

### rlbench/backend/task_utils.py

```
def sample_procedural_objects(task_base, num_samples, mass)
```

### rlbench/environment.py

```
class Environment(object)
    """Each environment has a scene."""
    def __init__(self, action_mode, dataset_root, obs_config, headless, static_positions, robot_setup, randomize_every, frequency, visual_randomization_config, dynamics_randomization_config, attach_grasped_objects, shaped_rewards, arm_max_velocity, arm_max_acceleration)
    def _check_dataset_structure(self)
    def _string_to_task(self, task_name)
    def launch(self)
    def shutdown(self)
    def get_task(self, task_class)
    def action_shape(self)
    def get_demos(self, task_name, amount, variation_number, image_paths, random_selection, from_episode_number)
    def get_scene_data(self)
```

### rlbench/observation_config.py

```
class CameraConfig(object)
    def __init__(self, rgb, rgb_noise, depth, depth_noise, point_cloud, mask, image_size, render_mode, masks_as_one_channel, depth_in_meters)
    def set_all(self, value)
class ObservationConfig(object)
    def __init__(self, left_shoulder_camera, right_shoulder_camera, overhead_camera, wrist_camera, front_camera, joint_velocities, joint_velocities_noise, joint_positions, joint_positions_noise, joint_forces, joint_forces_noise, gripper_open, gripper_pose, gripper_matrix, gripper_joint_positions, gripper_touch_forces, wrist_camera_matrix, record_gripper_closing, task_low_dim_state)
    def set_all(self, value)
    def set_all_high_dim(self, value)
    def set_all_low_dim(self, value)
```

### rlbench/sim2real/domain_randomization.py

```
class RandomizeEvery(Enum)
class Distributions(object)
    def apply(self, val)
class Gaussian(Distributions)
    def __init__(self, variance)
    def apply(self, val)
class Uniform(Distributions)
    def __init__(self, min, max)
    def apply(self, val)
class RandomizationConfig(object)
    def __init__(self, whitelist, blacklist, randomize_arm)
    def should_randomize(self, obj_name)
class DynamicsRandomizationConfig(RandomizationConfig)
class VisualRandomizationConfig(RandomizationConfig)
    def __init__(self, image_directory, whitelist, blacklist, randomize_arm)
    def sample(self, samples)
```

### rlbench/sim2real/domain_randomization_scene.py

```
class DomainRandomizationScene(Scene)
    def __init__(self, pyrep, robot, obs_config, robot_setup, randomize_every, frequency, visual_randomization_config, dynamics_randomization_config)
    def _should_randomize_episode(self, index)
    def _randomize(self)
    def init_task(self)
    def init_episode(self, index)
    def step(self)
    def reset(self)
```

### rlbench/task_environment.py

```
class TaskEnvironment(object)
    def __init__(self, pyrep, robot, scene, task, action_mode, dataset_root, obs_config, static_positions, attach_grasped_objects, shaped_rewards)
    def get_name(self)
    def sample_variation(self)
    def set_variation(self, v)
    def variation_count(self)
    def reset(self, demo)
    def get_observation(self)
    def step(self, action)
    def get_demos(self, amount, live_demos, image_paths, callable_each_step, max_attempts, random_selection, from_episode_number)
    def _get_live_demos(self, amount, callable_each_step, max_attempts)
    def reset_to_demo(self, demo)

```python
def get_observation(self) -> Observation:
        return self._scene.get_observation()
```
```

### rlbench/tasks/basketball_in_hoop.py

```
class BasketballInHoop(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/beat_the_buzz.py

```
class BeatTheBuzz(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/block_pyramid.py

```
class BlockPyramid(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/change_channel.py

```
class ChangeChannel(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/change_clock.py

```
class ChangeClock(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/close_box.py

```
class CloseBox(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/close_door.py

```
class CloseDoor(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/close_drawer.py

```
class CloseDrawer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/close_fridge.py

```
class CloseFridge(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/close_grill.py

```
class CloseGrill(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/close_jar.py

```
class CloseJar(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def cleanup(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/close_laptop_lid.py

```
class CloseLaptopLid(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/close_microwave.py

```
class CloseMicrowave(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/empty_container.py

```
"""Procedural objects supplied from:
https://sites.google.com/site/brainrobotdata/home/models"""
class EmptyContainer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def cleanup(self)
    def step(self)
    def _move_above_object(self, waypoint)
    def _repeat(self)
```

### rlbench/tasks/empty_dishwasher.py

```
class EmptyDishwasher(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/get_ice_from_fridge.py

```
class GetIceFromFridge(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/hang_frame_on_hanger.py

```
class HangFrameOnHanger(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/hit_ball_with_queue.py

```
class HitBallWithQueue(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/hockey.py

```
class Hockey(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/insert_onto_square_peg.py

```
class InsertOntoSquarePeg(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/insert_usb_in_computer.py

```
class InsertUsbInComputer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/lamp_off.py

```
class LampOff(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
```

### rlbench/tasks/lamp_on.py

```
class LampOn(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
```

### rlbench/tasks/lift_numbered_block.py

```
class LiftNumberedBlock(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def is_static_workspace(self)
```

### rlbench/tasks/light_bulb_in.py

```
class LightBulbIn(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
```

### rlbench/tasks/light_bulb_out.py

```
class LightBulbOut(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
```

### rlbench/tasks/meat_off_grill.py

```
class MeatOffGrill(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/meat_on_grill.py

```
class MeatOnGrill(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/move_hanger.py

```
class MoveHanger(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def is_static_workspace(self)
```

### rlbench/tasks/open_box.py

```
class OpenBox(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/open_door.py

```
class OpenDoor(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_drawer.py

```
class OpenDrawer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/open_fridge.py

```
class OpenFridge(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/open_grill.py

```
class OpenGrill(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_jar.py

```
class OpenJar(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def cleanup(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/open_microwave.py

```
class OpenMicrowave(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_oven.py

```
class OpenOven(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_washing_machine.py

```
class OpenWashingMachine(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_window.py

```
class OpenWindow(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/open_wine_bottle.py

```
class OpenWineBottle(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
```

### rlbench/tasks/phone_on_base.py

```
class PhoneOnBase(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/pick_and_lift.py

```
class PickAndLift(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def get_low_dim_state(self)
```

### rlbench/tasks/pick_and_lift_small.py

```
class PickAndLiftSmall(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/pick_up_cup.py

```
class PickUpCup(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/place_cups.py

```
class PlaceCups(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _move_above_next_target(self, waypoint)
    def _repeat(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/place_hanger_on_rack.py

```
class PlaceHangerOnRack(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def is_static_workspace(self)
```

### rlbench/tasks/place_shape_in_shape_sorter.py

```
class PlaceShapeInShapeSorter(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _set_grasp(self, _)
    def _set_drop(self, _)
```

### rlbench/tasks/play_jenga.py

```
class PlayJenga(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/plug_charger_in_power_supply.py

```
class PlugChargerInPowerSupply(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/pour_from_cup_to_cup.py

```
class PourFromCupToCup(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def cleanup(self)
```

### rlbench/tasks/press_switch.py

```
class PressSwitch(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/push_button.py

```
class PushButton(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
```

### rlbench/tasks/push_buttons.py

```
def print_permutations(color_permutations)
class PushButtons(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
    def _move_above_next_target(self, waypoint)
    def _repeat(self)
```

### rlbench/tasks/put_all_groceries_in_cupboard.py

```
class PutAllGroceriesInCupboard(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def is_static_workspace(self)
    def _move_to_next_target(self, _)
    def _move_to_drop_zone(self, _)
    def _repeat(self)
```

### rlbench/tasks/put_books_on_bookshelf.py

```
class PutBooksOnBookshelf(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_bottle_in_fridge.py

```
class PutBottleInFridge(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_groceries_in_cupboard.py

```
class PutGroceriesInCupboard(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def boundary_root(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_item_in_drawer.py

```
class PutItemInDrawer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_knife_in_knife_block.py

```
class PutKnifeInKnifeBlock(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_knife_on_chopping_board.py

```
class PutKnifeOnChoppingBoard(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/put_money_in_safe.py

```
class PutMoneyInSafe(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_plate_in_colored_dish_rack.py

```
class PutPlateInColoredDishRack(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_rubbish_in_bin.py

```
class PutRubbishInBin(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/put_shoes_in_box.py

```
class PutShoesInBox(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/put_toilet_roll_on_stand.py

```
class PutToiletRollOnStand(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/put_tray_in_oven.py

```
class PutTrayInOven(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/put_umbrella_in_umbrella_stand.py

```
class PutUmbrellaInUmbrellaStand(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/reach_and_drag.py

```
class ReachAndDrag(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/reach_target.py

```
class ReachTarget(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def get_low_dim_state(self)
    def is_static_workspace(self)
    def reward(self)

```python
def reward(self) -> float:
        return -np.linalg.norm(self.target.get_position() -
                               self.robot.arm.get_tip().get_position())
```
```

### rlbench/tasks/remove_cups.py

```
class RemoveCups(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _move_above_next_target(self, waypoint)
    def cleanup(self)
    def _repeat(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/scoop_with_spatula.py

```
class ScoopWithSpatula(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/screw_nail.py

```
class ScrewNail(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/set_the_table.py

```
class SetTheTable(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/setup_checkers.py

```
class SetupCheckers(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def cleanup(self)
    def _move_above_next_target(self, waypoint)
    def _repeat(self)
```

### rlbench/tasks/setup_chess.py

```
class SetupChess(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _move_above_next_target(self, waypoint)
    def _repeat(self)
```

### rlbench/tasks/slide_block_to_target.py

```
class SlideBlockToTarget(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def get_low_dim_state(self)
    def reward(self)

```python
def reward(self) -> float:
        grip_to_block = -np.linalg.norm(
            self._block.get_position() - self.robot.arm.get_tip().get_position())
        block_to_target = -np.linalg.norm(
            self._block.get_position() - self._target.get_position())
        return grip_to_block + block_to_target
```
```

### rlbench/tasks/slide_cabinet_open.py

```
class SlideCabinetOpen(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/slide_cabinet_open_and_place_cups.py

```
class SlideCabinetOpenAndPlaceCups(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/solve_puzzle.py

```
class SolvePuzzle(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/stack_blocks.py

```
class StackBlocks(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def _move_above_next_target(self, _)
    def _move_above_drop_zone(self, waypoint)
    def _is_last(self, waypoint)
    def _repeat(self)
```

### rlbench/tasks/stack_chairs.py

```
class ChairsOrientedCondition(Condition)
    def __init__(self, objs, error)
    def condition_met(self)
class StackChairs(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/stack_cups.py

```
class StackCups(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/stack_wine.py

```
class StackWine(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/straighten_rope.py

```
class StraightenRope(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/sweep_to_dustpan.py

```
class SweepToDustpan(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/take_cup_out_from_cabinet.py

```
class TakeCupOutFromCabinet(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_frame_off_hanger.py

```
class TakeFrameOffHanger(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/take_item_out_of_drawer.py

```
class TakeItemOutOfDrawer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_lid_off_saucepan.py

```
class TakeLidOffSaucepan(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def reward(self)

```python
def reward(self) -> float:
        grasp_lid_reward = -np.linalg.norm(
            self.lid.get_position() - self.robot.arm.get_tip().get_position())
        lift_lid_reward = -np.linalg.norm(
            self.lid.get_position() - self.success_detector.get_position())
        return grasp_lid_reward + lift_lid_reward
```
```

### rlbench/tasks/take_money_out_safe.py

```
class TakeMoneyOutSafe(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def cleanup(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_off_weighing_scales.py

```
class TakeOffWeighingScales(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_plate_off_colored_dish_rack.py

```
class TakePlateOffColoredDishRack(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/take_shoes_out_of_box.py

```
class TakeShoesOutOfBox(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_toilet_roll_off_stand.py

```
class TakeToiletRollOffStand(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/take_tray_out_of_oven.py

```
class TakeTrayOutOfOven(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/take_umbrella_out_of_umbrella_stand.py

```
class TakeUmbrellaOutOfUmbrellaStand(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/take_usb_out_of_computer.py

```
class TakeUsbOutOfComputer(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/toilet_seat_down.py

```
class ToiletSeatDown(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/toilet_seat_up.py

```
class ToiletSeatUp(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/turn_oven_on.py

```
class TurnOvenOn(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
    def boundary_root(self)
```

### rlbench/tasks/turn_tap.py

```
class TurnTap(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
```

### rlbench/tasks/tv_on.py

```
class TvOn(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/unplug_charger.py

```
class UnplugCharger(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/water_plants.py

```
class WaterPlants(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
```

### rlbench/tasks/weighing_scales.py

```
class WeighingScales(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def base_rotation_bounds(self)
```

### rlbench/tasks/wipe_desk.py

```
class WipeDesk(Task)
    def init_task(self)
    def init_episode(self, index)
    def variation_count(self)
    def step(self)
    def cleanup(self)
    def _place_dirt(self)
```

### tests/unit/test_domain_randomization_environment.py

```
class TestDomainRandomizaionEnvironment(TestCase)
    def tearDown(self)
    def get_task(self, randomize_every, frequency, visual_config, dynamics_config)
    def test_visual_randomize_every_2_episodes(self)
    def test_visual_randomize_every_2_transitions(self)
```

### tests/unit/test_environment.py

```
class TestEnvironment(TestCase)
    def tearDown(self)
    def get_task(self, task_class, arm_action_mode, obs_config)
    def test_get_task(self)
    def test_reset(self)
    def test_get_all_camera_observations(self)
    def test_step(self)
    def test_get_invalid_number_of_demos(self)
    def test_get_stored_demos_paths(self)
    def test_get_stored_demos_images(self)
    def test_get_stored_demos_images_without_init_sim(self)
    def test_get_live_demos(self)
    def test_observation_shape_constant_across_demo(self)
    def test_reset_to_demos(self)
    def test_action_mode_abs_joint_velocity(self)
    def test_action_mode_abs_joint_position(self)
    def test_action_mode_delta_joint_position(self)
    def test_action_mode_abs_ee_pose_ik_world_frame(self)
    def test_action_mode_delta_ee_pose_ik_world_frame(self)
    def test_action_mode_abs_ee_pose_plan_world_frame(self)
    def test_action_mode_delta_ee_pose_plan_world_frame(self)
    def test_action_mode_ee_pose_ik_ee_frame(self)
    def test_action_mode_ee_pose_plan_ee_frame(self)
    def test_action_mode_abs_erj_ik_ee_frame(self)
    def test_action_mode_abs_joint_torque(self)
    def test_swap_arm(self)
    def test_executed_jp_action(self)

```python
def test_get_all_camera_observations(self):
        obs_config = ObservationConfig()
        obs_config.left_shoulder_camera.rgb = True
        obs_config.right_shoulder_camera.rgb = True
        obs_config.overhead_camera.rgb = True
        obs_config.front_camera.rgb = True
        obs_config.wrist_camera.rgb = True
        task = self.get_task(
            ReachTarget, JointVelocity(), obs_config)
        desc, obs = task.reset()
        self.assertIsNotNone(obs.left_shoulder_rgb)
        self.assertIsNotNone(obs.right_shoulder_rgb)
        self.assertIsNotNone(obs.overhead_rgb)
        self.assertIsNotNone(obs.front_rgb)
        self.assertIsNotNone(obs.wrist_rgb)
```

```python
def test_observation_shape_constant_across_demo(self):
        task = self.get_task(
            TakeLidOffSaucepan, JointVelocity())
        demos = task.get_demos(1, live_demos=True)
        self.assertEqual(len(demos), 1)
        self.assertGreater(len(demos[0]), 0)
        self.assertGreater(demos[0][0].task_low_dim_state.size, 0)
        shapes = [step.task_low_dim_state.shape for step in demos[0]]
        first_shape = shapes[0]
        self.assertListEqual(shapes, [first_shape] * len(demos[0]))
```
```

### tests/unit/test_task_sets.py

```
class TestTaskSet(TestCase)
    def test_fs_v1(self)
    def test_mt_v1(self)
```

### tests/unit/test_tasks.py

```
class TestTasks(TestCase)
    """Tests all of the tasks via the task_validator tool but not testing demos.

This is a lighter-weight test than the full demo smoke that is run in the
`tasks` test directory."""
    def test_run_task_validator(self)
```

### tools/task_builder.py

```
def print_fail(message, end)
def setup_list_completer()
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
    def run_task_validator(self)
    def rename(self)
    def duplicate_task(self)
```

### tools/task_validator.py

```
class TaskValidationError(Exception)
def task_smoke(task, scene, variation, demos, success, max_variations, test_demos)
```