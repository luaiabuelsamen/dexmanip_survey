# robopianist_2023

source: https://github.com/google-research/robopianist


commit: 0d9736c64eba5faafdf214ed7d38d648ffbd5c7f


## README

# RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning

[![build][tests-badge]][tests]
[![docs][docs-badge]][docs]
[![PyPI Python Version][pypi-versions-badge]][pypi]
[![PyPI version][pypi-badge]][pypi]

[tests-badge]: https://github.com/google-research/robopianist/actions/workflows/ci.yml/badge.svg
[docs-badge]: https://github.com/google-research/robopianist/actions/workflows/docs.yml/badge.svg
[tests]: https://github.com/google-research/robopianist/actions/workflows/ci.yml
[docs]: https://google-research.github.io/robopianist/
[pypi-versions-badge]: https://img.shields.io/pypi/pyversions/robopianist
[pypi-badge]: https://badge.fury.io/py/robopianist.svg
[pypi]: https://pypi.org/project/robopianist/

[![Video](http://img.youtube.com/vi/VBFn_Gg0yD8/hqdefault.jpg)](https://youtu.be/VBFn_Gg0yD8)

RoboPianist is a new benchmarking suite for high-dimensional control, targeted at testing high spatial and temporal precision, coordination, and planning, all with an underactuated system frequently making-and-breaking contacts. The proposed challenge is *mastering the piano* through bi-manual dexterity, using a pair of simulated anthropomorphic robot hands.

This codebase contains software and tasks for the benchmark, and is powered by [MuJoCo](https://mujoco.org/).

- [Latest Updates](#latest-updates)
- [Getting Started](#getting-started)
- [Installation](#installation)
  - [Install from source](#install-from-source)
  - [Install from PyPI](#install-from-pypi)
  - [Optional: Download additional soundfonts](#optional-download-additional-soundfonts)
- [MIDI Dataset](#midi-dataset)
- [CLI](#cli)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Citing RoboPianist](#citing-robopianist)
- [Acknowledgements](#acknowledgements)
- [Works that have used RoboPianist](#works-that-have-used-robopianist)
- [License and Disclaimer](#license-and-disclaimer)

-------

## Latest Updates

- [24/12/2023] Updated install script so that it checks out the correct Menagerie commit. Please re-run `bash scripts/install_deps.sh` to update your installation.
- [17/08/2023] Added a [pixel wrapper](robopianist/wrappers/pixels.py) for augmenting the observation space with RGB images.
- [11/08/2023] Code to train the model-free RL policies is now public, see [robopianist-rl](https://github.com/kevinzakka/robopianist-rl).

-------

## Getting Started

We've created an introductory [Colab](https://colab.research.google.com/github/google-research/robopianist/blob/main/tutorial.ipynb) notebook that demonstrates how to use RoboPianist. It includes code for loading and customizing a piano playing task, and a demonstration of a pretrained policy playing a short snippet of *Twinkle Twinkle Little Star*. Click the button below to get started!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-research/robopianist/blob/main/tutorial.ipynb)

## Installation

RoboPianist is supported on both Linux and macOS and can be installed with Python >= 3.8. We recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to manage your Python environment.

### Install from source

The recommended way to install this package is from source. Start by cloning the repository:

```bash
git clone https://github.com/google-research/robopianist.git && cd robopianist
```

Next, install the prerequisite dependencies:

```bash
git submodule init && git submodule update
bash scripts/install_deps.sh
```

Finally, create a new conda environment and install RoboPianist in editable mode:

```bash
conda create -n pianist python=3.10
conda activate pianist

pip install -e ".[dev]"
```

To test your installation, run `make test` and verify that all tests pass.

### Install from PyPI

First, install the prerequisite dependencies:

```bash
bash <(curl -s https://raw.githubusercontent.com/google-research/robopianist/main/scripts/install_deps.sh) --no-soundfonts
```

Next, create a new conda environment and install RoboPianist:

```bash
conda create -n pianist python=3.10
conda activate pianist

pip install --upgrade robopianist
```

### Optional: Download additional soundfonts

We recommend installing additional soundfonts to improve the quality of the synthesized audio. You can easily do this using the RoboPianist CLI:

```bash
robopianist soundfont --download
```

For more soundfont-related commands, see [docs/soundfonts.md](docs/soundfonts.md).

## MIDI Dataset

The PIG dataset cannot be redistributed on GitHub due to licensing restrictions. See [docs/dataset](docs/dataset.md) for instructions on where to download it and how to preprocess it.

## CLI

RoboPianist comes with a command line interface (CLI) that can be used to download additional soundfonts, play MIDI files, preprocess the PIG dataset, and more. For more information, see [docs/cli.md](docs/cli.md).

## Contributing

We welcome contributions to RoboPianist. Please see [docs/contributing.md](docs/contributing.md) for more information.

## FAQ

See [docs/faq.md](docs/faq.md) for a list of frequently asked questions.

## Citing RoboPianist

If you use RoboPianist in your work, please use the following citation:

```bibtex
@inproceedings{robopianist2023,
  author = {Zakka, Kevin and Wu, Philipp and Smith, Laura and Gileadi, Nimrod and Howell, Taylor and Peng, Xue Bin and Singh, Sumeet and Tassa, Yuval and Florence, Pete and Zeng, Andy and Abbeel, Pieter},
  title = {RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning},
  booktitle = {Conference on Robot Learning (CoRL)},
  year = {2023},
}
```

## Acknowledgements

We would like to thank the following people for making this project possible:

- [Philipp Wu](https://www.linkedin.com/in/wuphilipp/) and [Mohit Shridhar](https://mohitshridhar.com/) for being a constant source of inspiration and support.
- [Ilya Kostrikov](https://www.kostrikov.xyz/) for constantly raising the bar for RL engineering and for invaluable debugging help.
- The [Magenta](https://magenta.tensorflow.org/) team for helpful pointers and feedback.
- The [MuJoCo](https://mujoco.org/) team for the development of the MuJoCo physics engine and their support throughout the project.

## Works that have used RoboPianist

- *Privileged Sensing Scaffolds Reinforcement Learning*, Hu et. al. ([paper](https://openreview.net/forum?id=EpVe8jAjdx), [website](https://penn-pal-lab.github.io/scaffolder/))

## License and Disclaimer

[MuJoco Menagerie](https://github.com/deepmind/mujoco_menagerie)'s license can be found [here](https://github.com/deepmind/mujoco_menagerie/blob/main/LICENSE). Soundfont licensing information can be found [here](docs/soundfonts.md). MIDI licensing information can be found [here](docs/dataset.md). All other code is licensed under an [Apache-2.0 License](LICENSE).

This is not an officially supported Google product.


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    ci.yml
    docs.yml
    publish.yml
.gitignore
.gitmodules
CITATION.cff
LICENSE
MANIFEST.in
Makefile
README.md
examples/
  http_player.py
  midi_data_to_file.py
  piano_with_shadow_hands_env.py
  play_midi_file.py
  self_actuated_piano_env.py
  twinkle_twinkle_actions.npy
mkdocs.yml
pyproject.toml
robopianist/
  __init__.py
  cli.py
  models/
    __init__.py
    arenas/
    hands/
    piano/
  music/
    __init__.py
    audio.py
    constants.py
    library.py
    midi_file.py
    midi_file_test.py
    midi_message.py
    music_test.py
    piano_roll.py
    synthesizer.py
  py.typed
  suite/
    README.md
    __init__.py
    composite_reward.py
    robopianist.png
    suite_test.py
    tasks/
    variations.py
    variations_test.py
  viewer/
    README.md
    __init__.py
    application.py
    figures.py
    gui/
    renderer.py
    runtime.py
    user_input.py
    util.py
    viewer.py
    views.py
  wrappers/
    __init__.py
    evaluation.py
    pixels.py
    sound.py
scripts/
  get_soundfonts.sh
  install_deps.sh
setup.py
tutorial.ipynb
```

## Config files (0)


## Python signatures and reward/observation bodies (15 files)


### examples/piano_with_shadow_hands_env.py

```
"""Piano with shadow hands environment."""
def main(_)
```

### examples/self_actuated_piano_env.py

```
"""Self-actuated piano environment."""
def main(_)
```

### robopianist/models/hands/base.py

```
class HandSide(Enum)
    """Which hand side is being modeled."""
class Hand(Entity, ABC)
    """Base composer class for dexterous hands."""
    def _build_observables(self)
    def name(self)
    def hand_side(self)
    def root_body(self)
    def joints(self)
    def actuators(self)
    def fingertip_sites(self)
class HandObservables(Observables)
    """Base class for dexterous hand observables."""
    def joints_pos(self)
    def joints_pos_cos_sin(self)
    def joints_vel(self)
    def joints_torque(self)
    def position(self)
```

### robopianist/models/hands/shadow_hand.py

```
"""Shadow hand composer class."""
class Dof()
    """Forearm degree of freedom."""
class ShadowHand(Hand)
    """A Shadow Hand E3M5."""
    def _build(self, name, side, primitive_fingertip_collisions, restrict_wrist_yaw_range, reduced_action_space, forearm_dofs)
    def _build_observables(self)
    def _parse_mjcf_elements(self)
    def _add_mjcf_elements(self)
    def _add_dofs(self)
    def hand_side(self)
    def mjcf_model(self)
    def name(self)
    def n_forearm_dofs(self)
    def root_body(self)
    def fingertip_bodies(self)
    def joints(self)
    def actuators(self)
    def joint_torque_sensors(self)
    def fingertip_sites(self)
    def actuator_velocity_sensors(self)
    def actuator_force_sensors(self)
    def fingertip_touch_sensors(self)
    def action_spec(self, physics)
    def apply_action(self, physics, action, random_state)
class ShadowHandObservables(HandObservables)
    """ShadowHand observables."""
    def actuators_force(self)
    def actuators_velocity(self)
    def actuators_power(self)
    def fingertip_positions(self)
    def fingertip_force(self)
```

### robopianist/models/hands/shadow_hand_test.py

```
"""Tests for shadow_hand.py."""
def _get_env()
class ShadowHandConstantsTest(TestCase)
    def test_fingertip_bodies_order(self)
class ShadowHandTest(TestCase)
    def test_compiles_and_steps(self, side, primitive_fingertip_collisions, restrict_yaw_range, reduced_action_space)
    def test_set_name(self)
    def test_default_name(self)
    def test_raises_value_error_on_invalid_forearm_dofs(self)
    def test_joints(self)
    def test_actuators(self, reduced_action_space)
    def test_restrict_wrist_yaw_range(self)
    def test_fingertip_sites_order(self)
    def test_action_spec(self, side)
class ShadowHandObservableTest(TestCase)
    def test_get_element_property(self, name)
    def test_get_element_tuple_property(self, name)
    def test_evaluate_observable(self, name)
```

### robopianist/suite/composite_reward.py

```
"""Utility class for composite reward functions."""
class CompositeReward()
    """A reward function composed of individual reward terms.

Useful for grouping sub-rewards of a task into a single reward function, computing
their sum, and logging the individual terms."""
    def __init__(self)
    def add(self, name, reward_fn)
    def remove(self, name)
    def compute(self, physics)
    def reward_fns(self)
    def reward_terms(self)

```python
def reward_fns(self) -> Dict[str, RewardFn]:
        return self._reward_fns
```

```python
def reward_terms(self) -> Dict[str, Reward]:
        return self._reward_terms
```
```

### robopianist/suite/tasks/base.py

```
"""Base piano composer task."""
class PianoOnlyTask(Task)
    """Piano task with no hands."""
    def __init__(self, arena, change_color_on_activation, add_piano_actuators, physics_timestep, control_timestep)
    def root_entity(self)
    def arena(self)
    def piano(self)
    def get_reward(self, physics)
class PianoTask(PianoOnlyTask)
    """Base class for piano tasks."""
    def __init__(self, arena, gravity_compensation, change_color_on_activation, primitive_fingertip_collisions, reduced_action_space, attachment_yaw, forearm_dofs, physics_timestep, control_timestep)
    def left_hand(self)
    def right_hand(self)
    def _add_hand(self, hand_side, position, quaternion, gravity_compensation, primitive_fingertip_collisions, reduced_action_space, attachment_yaw, forearm_dofs)

```python
def get_reward(self, physics) -> float:
        del physics  # Unused.
        return 0.0
```
```

### robopianist/suite/tasks/piano_with_one_shadow_hand.py

```
"""One-handed version of `piano_with_shadow_hands.py`."""
class PianoWithOneShadowHand(PianoTask)
    def __init__(self, midi, hand_side, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_colorization, augmentations)
    def _set_rewards(self)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self, midi)
    def initialize_episode(self, physics, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def get_discount(self, physics)
    def should_terminate_episode(self, physics)
    def midi(self)
    def reward_fn(self)
    def task_observables(self)
    def action_spec(self, physics)
    def before_step(self, physics, action, random_state)
    def _compute_sustain_reward(self, physics)
    def _compute_energy_reward(self, physics)
    def _compute_key_press_reward(self, physics)
    def _compute_fingering_reward(self, physics)
    def _update_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys(self, physics)

```python
def _set_rewards(self) -> None:
        self._reward_fn = composite_reward.CompositeReward(
            key_press_reward=self._compute_key_press_reward,
            sustain_reward=self._compute_sustain_reward,
            energy_reward=self._compute_energy_reward,
        )
        if not self._disable_fingering_reward:
            self._reward_fn.add("fingering_reward", self._compute_fingering_reward)
```

```python
def get_reward(self, physics) -> float:
        return self._reward_fn.compute(physics)
```

```python
def reward_fn(self) -> composite_reward.CompositeReward:
        return self._reward_fn
```

```python
def _compute_sustain_reward(self, physics) -> float:
        """Reward for pressing the sustain pedal at the right time."""
        del physics  # Unused.
        return tolerance(
            self._goal_current[-1] - self.piano.sustain_activation[0],
            bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
            margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
            sigmoid="gaussian",
        )
```

```python
def _compute_energy_reward(self, physics) -> float:
        """Reward for minimizing energy."""
        power = self._hand.observables.actuators_power(physics).copy()
        return -_ENERGY_PENALTY_COEF * np.sum(power)
```

```python
def _compute_key_press_reward(self, physics) -> float:
        """Reward for pressing the right keys at the right time."""
        del physics  # Unused.
        on = np.flatnonzero(self._goal_current[:-1])
        rew = 0.0
        # It's possible we have no keys to press at this timestep so we need to check
        # that `on` is not empty.
        if on.size > 0:
            actual = np.array(self.piano.state / self.piano._qpos_range[:, 1])
            rews = tolerance(
                self._goal_current[:-1][on] - actual[on],
                bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
                margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
                sigmoid="gaussian",
            )
            rew += 0.5 * rews.mean()
        # If there's any false positive, the remaining 0.5 reward is lost.
        off = np.flatnonzero(1 - self._goal_current[:-1])
        rew += 0.5 * (1 - float(self.piano.activation[off].any()))
        return rew
```

```python
def _compute_fingering_reward(self, physics) -> float:
        """Reward for minimizing the distance between the fingers and the keys."""

        def _distance_finger_to_key(
            hand_keys: List[Tuple[int, int]], hand
        ) -> List[float]:
            distances = []
            for key, mjcf_fingering in hand_keys:
                fingertip_site = hand.fingertip_sites[mjcf_fingering]
                fingertip_pos = physics.bind(fingertip_site).xpos.copy()
                key_geom = self.piano.keys[key].geom[0]
                key_geom_pos = physics.bind(key_geom).xpos.copy()
                key_geom_pos[-1] += 0.5 * physics.bind(key_geom).size[2]
                key_geom_pos[0] += 0.35 * physics.bind(key_geom).size[0]
                diff = key_geom_pos - fingertip_pos
                distances.append(float(np.linalg.norm(diff)))
            return distances

        distances = _distance_finger_to_key(self._keys_current, self._hand)

        # Case where there are no keys to press at this timestep.
        # TODO(kevin): Unclear if we should return 0 or 1 here. 0 seems to do better.
        if not distances:
            return 0.0

        rews = tolerance(
            np.hstack(distances),
            bounds=(0, _FINGER_CLOSE_ENOUGH_TO_KEY),
            margin=(_FINGER_CLOSE_ENOUGH_TO_KEY * 10),
            sigmoid="gaussian",
        )
        return float(np.mean(rews))
```
```

### robopianist/suite/tasks/piano_with_shadow_hands.py

```
"""A task where two shadow hands must play a given MIDI file on a piano."""
class PianoWithShadowHands(PianoTask)
    def __init__(self, midi, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_forearm_reward, disable_colorization, disable_hand_collisions, augmentations, energy_penalty_coef, randomize_hand_positions)
    def _set_rewards(self)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def get_discount(self, physics)
    def should_terminate_episode(self, physics)
    def task_observables(self)
    def action_spec(self, physics)
    def midi(self)
    def reward_fn(self)
    def _compute_forearm_reward(self, physics)
    def _compute_sustain_reward(self, physics)
    def _compute_energy_reward(self, physics)
    def _compute_key_press_reward(self, physics)
    def _compute_fingering_reward(self, physics)
    def _compute_ot_fingering_reward(self, physics)
    def _update_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys(self, physics)
    def _disable_collisions_between_hands(self)
    def _randomize_initial_hand_positions(self, physics, random_state)

```python
def _set_rewards(self) -> None:
        self._reward_fn = composite_reward.CompositeReward(
            key_press_reward=self._compute_key_press_reward,
            sustain_reward=self._compute_sustain_reward,
            energy_reward=self._compute_energy_reward,
        )
        if not self._disable_fingering_reward:
            self._reward_fn.add("fingering_reward", self._compute_fingering_reward)
        else:
            # use OT based fingering
            print('Fingering is unavailable. OT fingering reward is used.')
            self._reward_fn.add("ot_fingering_reward", self._compute_ot_fingering_reward)

        if not self._disable_forearm_reward:
            self._reward_fn.add("forearm_reward", self._compute_forearm_reward)
```

```python
def get_reward(self, physics: mjcf.Physics) -> float:
        return self._reward_fn.compute(physics)
```

```python
def reward_fn(self) -> composite_reward.CompositeReward:
        return self._reward_fn
```

```python
def _compute_forearm_reward(self, physics: mjcf.Physics) -> float:
        """Reward for not colliding the forearms."""
        if collision_utils.has_collision(
            physics,
            [g.full_identifier for g in self.right_hand.root_body.geom],
            [g.full_identifier for g in self.left_hand.root_body.geom],
        ):
            return 0.0
        return 0.5
```

```python
def _compute_sustain_reward(self, physics: mjcf.Physics) -> float:
        """Reward for pressing the sustain pedal at the right time."""
        del physics  # Unused.
        return tolerance(
            self._goal_current[-1] - self.piano.sustain_activation[0],
            bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
            margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
            sigmoid="gaussian",
        )
```

```python
def _compute_energy_reward(self, physics: mjcf.Physics) -> float:
        """Reward for minimizing energy."""
        rew = 0.0
        for hand in [self.right_hand, self.left_hand]:
            power = hand.observables.actuators_power(physics).copy()
            rew -= self._energy_penalty_coef * np.sum(power)
        return rew
```

```python
def _compute_key_press_reward(self, physics: mjcf.Physics) -> float:
        """Reward for pressing the right keys at the right time."""
        del physics  # Unused.
        on = np.flatnonzero(self._goal_current[:-1])
        rew = 0.0
        # It's possible we have no keys to press at this timestep, so we need to check
        # that `on` is not empty.
        if on.size > 0:
            actual = np.array(self.piano.state / self.piano._qpos_range[:, 1])
            rews = tolerance(
                self._goal_current[:-1][on] - actual[on],
                bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
                margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
                sigmoid="gaussian",
            )
            rew += 0.5 * rews.mean()
        # If there are any false positives, the remaining 0.5 reward is lost.
        off = np.flatnonzero(1 - self._goal_current[:-1])
        rew += 0.5 * (1 - float(self.piano.activation[off].any()))
        return rew
```

```python
def _compute_fingering_reward(self, physics: mjcf.Physics) -> float:
        """Reward for minimizing the distance between the fingers and the keys."""

        def _distance_finger_to_key(
            hand_keys: List[Tuple[int, int]], hand
        ) -> List[float]:
            distances = []
            for key, mjcf_fingering in hand_keys:
                fingertip_site = hand.fingertip_sites[mjcf_fingering]
                fingertip_pos = physics.bind(fingertip_site).xpos.copy()
                key_geom = self.piano.keys[key].geom[0]
                key_geom_pos = physics.bind(key_geom).xpos.copy()
                key_geom_pos[-1] += 0.5 * physics.bind(key_geom).size[2]
                key_geom_pos[0] += 0.35 * physics.bind(key_geom).size[0]
                diff = key_geom_pos - fingertip_pos
                distances.append(float(np.linalg.norm(diff)))
            return distances

        distances = _distance_finger_to_key(self._rh_keys_current, self.right_hand)
        distances += _distance_finger_to_key(self._lh_keys_current, self.left_hand)

        # Case where there are no keys to press at this timestep.
        if not distances:
            return 0.0

        rews = tolerance(
            np.hstack(distances),
            bounds=(0, _FINGER_CLOSE_ENOUGH_TO_KEY),
            margin=(_FINGER_CLOSE_ENOUGH_TO_KEY * 10),
            sigmoid="gaussian",
        )
        return float(np.mean(rews))
```

```python
def _compute_ot_fingering_reward(self, physics: mjcf.Physics) -> float:
        """ OT reward calculation from RP1M https://arxiv.org/abs/2408.11048 """
        # calcuate fingertip positions
        fingertip_pos = [physics.bind(finger).xpos.copy() for finger in self.left_hand.fingertip_sites]
        fingertip_pos += [physics.bind(finger).xpos.copy() for finger in self.right_hand.fingertip_sites]
        
        # calcuate the positions of piano keys to press.
        keys_to_press = np.flatnonzero(self._goal_current[:-1]) # keys to press
        # if no key is pressed
        if keys_to_press.shape[0] == 0:
            return 1.

        # calculate key pos
        key_pos = []
        for key in keys_to_press:
            key_geom = self.piano.keys[key].geom[0]
            key_geom_pos = physics.bind(key_geom).xpos.copy()
            key_geom_pos[-1] += 0.5 * physics.bind(key_geom).size[2]
            key_geom_pos[0] += 0.35 * physics.bind(key_geom).size[0]
            key_pos.append(key_geom_pos.copy())

        # calcualte the distance between keys and fingers
        dist = np.full((len(fingertip_pos), len(key_pos)), 100.)
        for i, finger in enumerate(fingertip_pos):
            for j, key in enumerate(key_pos):
                dist[i, j] = np.linalg.norm(key - finger)
        
        # calculate the shortest distance
        row_ind, col_ind = linear_sum_assignment(dist)
        dist = dist[row_ind, col_ind]
        rews = tolerance(
            dist,
            bounds=(0, _FINGER_CLOSE_ENOUGH_TO_KEY),
            margin=(_FINGER_CLOSE_ENOUGH_TO_KEY * 10),
            sigmoid="gaussian",
        )
        return float(np.mean(rews))
```
```

### robopianist/suite/tasks/piano_with_shadow_hands_test.py

```
"""Tests for piano_with_shadow_hands_test.py."""
def _get_test_midi(dt)
def _get_env(control_timestep, n_steps_lookahead, n_seconds_lookahead, wrong_press_termination, disable_fingering_reward)
class PianoWithShadowHandsTest(TestCase)
    def test_observables(self, disable_fingering_reward)
    def test_action_spec(self)
    def test_termination_and_discount(self)
    def test_n_seconds_lookahead(self, control_timestep, n_seconds_lookahead)
    def test_goal_observable_lookahead(self, n_steps_lookahead)
    def test_fingering_observable(self)
    def test_failure_termination(self)
    def test_steps_left_observable(self)
    def test_fingering_reward_presence(self, disable_fingering_reward)

```python
def test_fingering_reward_presence(self, disable_fingering_reward: bool) -> None:
        env = _get_env(disable_fingering_reward=disable_fingering_reward)
        action_spec = env.action_spec()
        zero_action = np.zeros(action_spec.shape)
        env.reset()

        env.step(zero_action)
        reward_terms = env.task.reward_fn.reward_terms

        if disable_fingering_reward:
            self.assertNotIn("fingering_reward", reward_terms)
        else:
            self.assertIn("fingering_reward", reward_terms)
```
```

### robopianist/suite/tasks/self_actuated_piano.py

```
"""A self-actuated piano that must learn to play a MIDI file."""
def negative_binary_cross_entropy(predictions, targets)
def negative_l2_distance(predictions, targets)
class RewardType(Enum)
    def get(self)
class SelfActuatedPiano(PianoOnlyTask)
    """Task where a piano self-actuates to play a MIDI file."""
    def __init__(self, midi, n_steps_lookahead, trim_silence, reward_type, augmentations)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)
    def task_observables(self)
    def action_spec(self, physics)
    def midi(self)
    def reward_fn(self)
    def _compute_key_press_reward(self, physics)
    def _update_goal_state(self)
    def _add_observables(self)

```python
def get_reward(self, physics: mjcf.Physics) -> float:
        return self._reward_fn.compute(physics)
```

```python
def reward_fn(self) -> composite_reward.CompositeReward:
        return self._reward_fn
```

```python
def _compute_key_press_reward(self, physics: mjcf.Physics) -> float:
        del physics  # Unused.
        return self._key_press_reward(
            np.concatenate([self.piano.activation, self.piano.sustain_activation]),
            self._goal_current,
        )
```
```

### robopianist/suite/tasks/self_actuated_piano_test.py

```
"""Tests for self_actuated_piano.py."""
def _get_test_midi(dt)
def _get_env(control_timestep, n_steps_lookahead, reward_type)
class SelfActuatedPianoTest(TestCase)
    def test_observables(self)
    def test_action_spec(self)
    def test_termination_and_discount(self)
    def test_goal_observable_lookahead(self, n_steps_lookahead)
    def test_reward(self, reward_type)

```python
def test_reward(self, reward_type: self_actuated_piano.RewardType) -> None:
        env = _get_env(reward_type=reward_type)
        action_spec = env.action_spec()
        timestep = env.reset()

        # The first timestep should have a None reward.
        self.assertIsNone(timestep.reward)

        while not timestep.last():
            random_ctrl = np.random.uniform(
                low=action_spec.minimum,
                high=action_spec.maximum,
                size=action_spec.shape,
            ).astype(action_spec.dtype)
            timestep = env.step(random_ctrl)

            actual_reward = timestep.reward
            expected_reward = reward_type.get()(
                np.concatenate(
                    [env.task.piano.activation, env.task.piano.sustain_activation]
                ),
                env.task._goal_current,
            )
            self.assertEqual(actual_reward, expected_reward)
```
```