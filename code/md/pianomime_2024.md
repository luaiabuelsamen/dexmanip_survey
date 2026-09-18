# pianomime_2024

source: https://github.com/sNiper-Qian/pianomime


commit: c4abefac8d2941f5a08ca656b12f5e047cab7155


## README

# PianoMime: Learning a Generalist, Dexterous Piano Player from Internet Demonstrations
[[Project page]](https://pianomime.github.io/)
[[Paper]](https://arxiv.org/pdf/2407.18178)
[[Arxiv]](https://arxiv.org/abs/2407.18178)
[[Colab]](https://colab.research.google.com/drive/1Rv1XGPA0a4x3a_M6yXc7uiwKnmmIu95o?usp=sharing)

**Cheng Qian**<sup>1</sup>, **Julen Urain**<sup>2</sup>, **Kevin Zakka**<sup>3</sup>, **Jan Peters**<sup>2</sup>

<sup>1</sup>TU Munich, 
<sup>2</sup>TU Darmsadt, 
<sup>3</sup>UC Berkeley

TLDR:
We train a generalist policy for controlling dexterous robot hands to play any songs,
using human pianist demonstration videos from internet. We use residual reinforcement learning to learn song-specific policies from demonstrations, and a two-stage diffusion policy to generalize to new songs.

[![Video](https://i.ytimg.com/vi/LW0AiBIcnL0/hqdefault.jpg)](https://youtu.be/LW0AiBIcnL0)
## 🚨 News: Dataset Preparation Tutorial Released!

We're thrilled to announce that we've just published a **Tutorial** that walks you through the entire process of preparing your dataset from videos and MIDI files! 🎹🎥

### 📍 Where to find it:
[📓 `tutorial/data_preprocessing.ipynb`](tutorial/data_preprocessing.ipynb)

Inside the notebook, you'll learn how to:
- Estimate homography matrix from video coordinates to real piano coordinates
- Extract fingering and human fingertip trajectories from videos
- Format your data for training

## Getting Started

We have a tutorial on Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Rv1XGPA0a4x3a_M6yXc7uiwKnmmIu95o?usp=sharing)

## Installation and Setup

Follow the steps below to set up the PianoMime.

### Step 1: Clone the Repository
Start by cloning the repository:
    
```sh
git clone https://github.com/sNiper-Qian/pianomime.git
```

### Step 2: Install Dependencies

1. Open a terminal and run the following command to install the necessary libraries:

    ```sh
    sudo apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
    ```

2. Run the following script to install additional dependencies for RoboPianist:

    ```sh
    bash pianomime/scripts/install_deps.sh
    ```

3. Install the Python dependencies by running:

    ```sh
    pip install -r pianomime/requirements.txt
    ```

4. (Optional) Sometimes it is needed to install JAX with the required version:

    ```sh
    pip install --upgrade "jax==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
    pip install -U "jaxlib==0.4.23+cuda12.cudnn89" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
    ```

### Step 3: Download the Dataset and Checkpoints

1. Download the dataset from the following link:
   https://drive.google.com/file/d/1X8q-PvqyqL2X15wCZevTfAtSDfiHpYAa/view?usp=sharing

2. Download the checkpoints from the following link:
   https://drive.google.com/file/d/1-wa1UAn_mbPN87D6GIi4PS0VNDE5mbQh/view?usp=sharing

## Dataset Preparation
We also provide a tutorial for generate dataset from videos and MIDI files.

You can find the step-by-step guide here:
[Data Preparation Tutorial](tutorial/data_preprocessing.ipynb)

This notebook will walk you through the process of converting your video and MIDI data into a structured dataset, ready for training.
## Citation

Please use the following citation:

```bibtex
@misc{qian2024pianomimelearninggeneralistdexterous,
      title={PianoMime: Learning a Generalist, Dexterous Piano Player from Internet Demonstrations}, 
      author={Cheng Qian and Julen Urain and Kevin Zakka and Jan Peters},
      year={2024},
      eprint={2407.18178},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2407.18178}, 
}
```

## Acknowledgements

The simulation environment is based on RoboPianist [RoboPianist](https://github.com/google-research/robopianist)  

The diffusion policy is adapted from [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)

The inverse-kinematics controller is adapted from [Pink](https://github.com/stephane-caron/pink)

The human demonstration videos are downloaded from YouTube channel [PianoX](https://www.youtube.com/channel/UCsR6ZEA0AbBhrF-NCeET6vQ)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## File tree (depth 3, assets pruned)

```
.gitignore
README.md
dataset_hl.zarr/
  .zgroup
  meta/
    .zgroup
    episode_ends/
dataset_ll.zarr/
  .zgroup
  meta/
    .zgroup
    episode_ends/
goal_auto_encoder/
  dataset.py
  loss.py
  network.py
  test_sdf_ae.py
  train_sdf_ae.py
  transformer.py
  utils.py
multi_task/
  dataset.py
  eval_high_level.py
  eval_low_level.py
  network.py
  train_high_level.py
  train_low_level.py
  train_low_level_bet.py
  train_low_level_mlp.py
  train_single_stage.py
  utils.py
requirements.txt
robopianist/
  .DS_Store
  __init__.py
  cli.py
  controller/
    __init__.py
    ik_controller.py
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
  soundfonts/
    TimGM6mb.sf2
  suite/
    README.md
    __init__.py
    composite_reward.py
    suite_test.py
    tasks/
    variations.py
    variations_test.py
  utils/
    __init__.py
    inverse_kinematics.py
    qp_solver.py
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
    deep_mimic.py
    dm2gym.py
    evaluation.py
    fingering_emb.py
    pixels.py
    residual.py
    sound.py
scripts/
  eval_low_level.sh
  install_deps.sh
  run_ppo.sh
  test_trained_actions.sh
single_task/
  controller/
    __init__.py
    ik_controller.py
    inverse_kinematics.py
    qp_solver.py
  eval_ppo.py
  logging_callback.py
  lr_scheduler.py
  piano_with_shadow_hands_res.py
  run_ppo.sh
  test_trained_actions.py
  train_ppo.py
  utils.py
  wrappers/
    __init__.py
    deep_mimic.py
    dm2gym.py
    residual.py
tutorial/
  Landmarks.png
  Stan_1.mid
  Stan_1.mp4
  Stan_1.pkl
  Stan_1_demo.mp4
  Stan_1_fingering.mp4
  Stan_1_left_hand_action_list.npy
  Stan_1_mujoco.mp4
  Stan_1_right_hand_action_list.npy
  data_preprocessing.ipynb
  hand_landmarker.task
  homography_matrix.npy
  left_hand_initial_action_list.npy
  piano_example.jpg
  right_hand_initial_action_list.npy
  utils.py
```

## Config files (0)


## Python signatures and reward/observation bodies (41 files)


### multi_task/dataset.py

```
def read_dataset_split(dataset_path, pred_horizon, obs_horizon, action_horizon, normalization)
def read_dataset(pred_horizon, obs_horizon, action_horizon, dataset_path, normalization)
def create_sample_indices(episode_ends, sequence_length, pad_before, pad_after)
def sample_sequence(train_data, sequence_length, buffer_start_idx, buffer_end_idx, sample_start_idx, sample_end_idx, obs_buffer_start_idx, obs_buffer_end_idx, obs_sample_start_idx, obs_sample_end_idx)
def get_data_stats(data)
def normalize_data(data, stats)
def unnormalize_data(ndata, stats)
class RoboPianistDataset(Dataset)
    def __init__(self, dataset_path, pred_horizon, obs_horizon, action_horizon, normalization)
    def __len__(self)
    def __getitem__(self, idx)
```

### multi_task/eval_low_level.py

```
def play_video(filename)
def main()
```

### multi_task/network.py

```
class SinusoidalPosEmb(Module)
    def __init__(self, dim)
    def forward(self, x)
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
class ConvEncoder(Module)
    def __init__(self, in_channels, mid_channels, out_channels, horizon, kernel_size, n_groups, noise_fingering, noise_ft)
    def get_conv_output_dim(self, in_channels, horizon)
    def forward(self, x)
    def forward_without_sampling(self, x)
class BetVariationalConvMlpEncoder(Module)
    def __init__(self, in_channels, mid_channels, out_channels, bet_horizon, horizon, cond_dim, latent_dim, kernel_size, n_groups, device, beta, noise)
    def get_conv_output_dim(self, in_channels, horizon)
    def forward(self, x, cond)
    def forward_without_sampling(self, x, cond)
class VariationalConvMlpEncoder(Module)
    def __init__(self, in_channels, mid_channels, out_channels, horizon, cond_dim, latent_dim, kernel_size, n_groups, device, beta, noise)
    def get_conv_output_dim(self, in_channels, horizon)
    def forward(self, x, cond)
    def forward_without_sampling(self, x, cond)
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups, midi_dim, midi_cond_dim, freeze_encoder, midi_encoder)
    def get_midi_encoder_output_dim(self, midi_dim)
    def forward(self, x, cond)
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups, midi_dim, midi_cond_dim, midi_encoder, freeze_encoder)
    def forward(self, sample, timestep, global_cond)
class MLP(Module)
    def __init__(self, in_dim, out_dim, mid_dim, n_layers, n_groups, noise)
    def forward(self, x)
```

### multi_task/utils.py

```
class Args()
def get_diffusion_obs_1(timestep, exclude_keys)
def get_goal_only_obs(timestep, lookahead)
def get_diffusion_obs(timestep, lookahead, exclude_keys, encoder, plan_encoder, sampling, current_fingertip, concatenate_keys)
def get_flattend_obs(timestep, lookahead, exclude_keys, encoder, sampling, plan_encoder, current_fingertip, concatenate_keys)
def get_env_test(task_name, enable_ik, record_dir, lookahead, use_fingering_emb, use_note_traj)
def get_env_hl(task_name, record_dir, lookahead, use_fingering_emb, use_midi)
def get_env_ll(task_name, enable_ik, record_dir, lookahead, external_demo, use_fingering_emb, external_fingering, use_midi)
def adjust_ft_fingering(env, keys, lh_ft, rh_ft, last_keys, last_lh_ft, last_rh_ft, last_fingering)
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
    def forearm_site(self)
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
    def __init__(self, note_trajectory, midi, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_forearm_reward, disable_colorization, disable_hand_collisions, augmentations, energy_penalty_coef, randomize_hand_positions, fingering_lookahead, midi_start_from, enable_joints_vel_obs)
    def _set_rewards(self)
    def _scale_note_traj(self, scale)
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
    def _update_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys_without_fingering(self, physics)
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
        # return tolerance(
        #     self._goal_current[-1] - self.piano.sustain_activation[0],
        #     bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
        #     margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
        #     sigmoid="gaussian",
        # )
        return 0
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
        return 2 * rew
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
        # return float(np.mean(rews))
        return 0
```
```

### robopianist/suite/tasks/piano_with_shadow_hands_multitask.py

```
"""A task where two shadow hands must play a given MIDI file on a piano."""
class PianoWithShadowHandsMultiTask(PianoTask)
    def __init__(self, note_trajectories, midis, task_names, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_forearm_reward, disable_colorization, disable_hand_collisions, augmentations, energy_penalty_coef, randomize_hand_positions, fingering_lookahead, midi_start_from, residual_factor, curriculum, enable_joint_vel_obs, enable_base_joint_ctrl_domain, subgoal_length)
    def _set_rewards(self)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def _scale_note_traj(self, scale)
    def extend_curriculum(self)
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
    def task_name(self)
    def _compute_forearm_reward(self, physics)
    def _compute_sustain_reward(self, physics)
    def _compute_energy_reward(self, physics)
    def _compute_key_press_reward(self, physics)
    def _compute_fingering_reward(self, physics)
    def _update_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys_without_fingering(self, physics)
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
        # return tolerance(
        #     self._goal_current[-1] - self.piano.sustain_activation[0],
        #     bounds=(0, _KEY_CLOSE_ENOUGH_TO_PRESSED),
        #     margin=(_KEY_CLOSE_ENOUGH_TO_PRESSED * 10),
        #     sigmoid="gaussian",
        # )
        return 0
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
        # return float(np.mean(rews))
        return 0.0
```
```

### robopianist/suite/tasks/piano_with_shadow_hands_res.py

```
"""A task where two shadow hands must play a given MIDI file on a piano."""
class PianoWithShadowHandsResidual(PianoTask)
    def __init__(self, note_trajectory, midi, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_forearm_reward, disable_colorization, disable_hand_collisions, augmentations, energy_penalty_coef, randomize_hand_positions, fingering_lookahead, midi_start_from, residual_factor, curriculum, shift, enable_joints_vel_obs)
    def _set_rewards(self)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def _scale_note_traj(self, scale)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def extend_curriculum(self)
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
    def _update_goal_state(self)
    def get_next_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys_without_fingering(self, physics)
    def _colorize_keys(self, physics)
    def _disable_collisions_between_hands(self)
    def _randomize_initial_hand_positions(self, physics, random_state)
    def _shift_initial_hand_positions(self, physics, shift)
    def get_fingertip_pos(self, physics)

```python
def _set_rewards(self) -> None:
        self._reward_fn = composite_reward.CompositeReward(
            key_press_reward=self._compute_key_press_reward,
            sustain_reward=self._compute_sustain_reward,
            energy_reward=self._compute_energy_reward,
        )
        if not self._disable_fingering_reward:
            self._reward_fn.add("fingering_reward", self._compute_fingering_reward)
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
        return 0
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
        return 2*rew
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
        # return float(np.mean(rews))
        return 0.0
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
    def __init__(self, note_trajectory, midi, n_steps_lookahead, trim_silence, reward_type, augmentations)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)
    def _scale_note_traj(self, scale)
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

### single_task/controller/ik_controller.py

```
def move_fingers_to_pos_qp(env, hand_action, finger_names, hand_side, targeting_wrist)
def move_fingers_to_pos(env, hand_action, finger_names, hand_side)
def move_fingers_to_keys(env, key_indices, offset_x, offset_y, finger_names)
def move_finger_to_key(env, key_index, finger_name)
```

### single_task/controller/inverse_kinematics.py

```
"""Functions for computing inverse kinematics on MuJoCo models."""
def qpos_from_site_pose(physics, site_name, target_pos, target_quat, joint_names, tol, rot_weight, regularization_threshold, regularization_strength, max_update_norm, progress_thresh, max_steps, inplace)
def qpos_from_multiple_site_pos(physics, site_names, pos_weight, target_pos, target_quat, joint_names, tol, rot_weight, regularization_threshold, regularization_strength, max_update_norm, progress_thresh, max_steps, inplace)
def nullspace_method(jac_joints, delta, regularization_strength)
```

### single_task/controller/qp_solver.py

```
class IK_qpsolver()
    def __init__(self, physics, site_names, target_pos, pos_weights, gain, limit_gain, dt, joint_names, target_quat, quat_weights, lm_damping, damping)
    def is_positive_definite(self, matrix)
    def build_objective(self)
    def build_inequalities(self)
    def solve(self)
    def get_qpos(self)
```

### single_task/eval_ppo.py

```
def play_video(filename)
class Args()
def prefix_dict(prefix, d)
def main(args)
```

### single_task/logging_callback.py

```
def prefix_dict(prefix, d)
class LoggingCallback(WandbCallback)
    """Custom callback for logging data to wandb."""
    def __init__(self, verbose, model_save_path, model_save_freq, gradient_save_freq, log, logging_freq)
    def on_rollout_end(self)
```

### single_task/lr_scheduler.py

```
class LR_Scheduler()
    def __init__(self, initial_lr, decay_rate)
    def lr_schedule(self, remaining_progress)
```

### single_task/piano_with_shadow_hands_res.py

```
"""A task where two shadow hands must play a given MIDI file on a piano."""
class PianoWithShadowHandsResidual(PianoTask)
    def __init__(self, note_trajectory, midi, n_steps_lookahead, n_seconds_lookahead, trim_silence, wrong_press_termination, initial_buffer_time, disable_fingering_reward, disable_forearm_reward, disable_colorization, disable_hand_collisions, augmentations, energy_penalty_coef, randomize_hand_positions, fingering_lookahead, midi_start_from, residual_factor, curriculum, shift, enable_joints_vel_obs)
    def _set_rewards(self)
    def _reset_quantities_at_episode_init(self)
    def _maybe_change_midi(self, random_state)
    def _reset_trajectory(self)
    def _scale_note_traj(self, scale)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def extend_curriculum(self)
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
    def _update_goal_state(self)
    def get_next_goal_state(self)
    def _update_fingering_state(self)
    def _add_observables(self)
    def _colorize_fingertips(self)
    def _colorize_keys_without_fingering(self, physics)
    def _colorize_keys(self, physics)
    def _disable_collisions_between_hands(self)
    def _randomize_initial_hand_positions(self, physics, random_state)
    def _shift_initial_hand_positions(self, physics, shift)
    def get_fingertip_pos(self, physics)

```python
def _set_rewards(self) -> None:
        self._reward_fn = composite_reward.CompositeReward(
            key_press_reward=self._compute_key_press_reward,
            sustain_reward=self._compute_sustain_reward,
            energy_reward=self._compute_energy_reward,
        )
        if not self._disable_fingering_reward:
            self._reward_fn.add("fingering_reward", self._compute_fingering_reward)
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
        return 0
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
        return 2*rew
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
        # return float(np.mean(rews))
        return 0.0
```
```

### single_task/test_trained_actions.py

```
def play_video(filename)
```

### single_task/train_ppo.py

```
class Args()
def prefix_dict(prefix, d)
def main(args)
```

### single_task/utils.py

```
def get_env_no_residual(args, record_dir)
def get_env(args, record_dir)
def make_envs(make_env_fn, rank, seed)
def get_env_multitask(args, task_names, record_dir)
```

### single_task/wrappers/deep_mimic.py

```
"""A wrapper for deep mimic framework."""
class DeepMimicWrapper_Old(EnvironmentWrapper)
    """Change observation and reward to deep mimic fashion."""
    def __init__(self, environment, demonstrations, demo_ctrl_timestep, remove_goal_observation, disable_joints_pos_mimic_reward, disable_end_effector_pos_mimic_reward)
    def observation_spec(self)
    def step(self, action)
    def reset(self)
    def _compute_end_effector_pos_mimic_reward(self, physics)
    def _compute_joints_pos_mimic_reward(self, physics)
    def _add_deep_mimic_rewards(self)
    def _remove_goal_observation(self, timestep)
    def _add_demo_observation(self, timestep)
    def get_deepmimic_rews(self)
class DeepMimicWrapper(EnvironmentWrapper)
    """Change observation and reward to deep mimic fashion."""
    def __init__(self, environment, demonstrations_lh, demonstrations_rh, demo_ctrl_timestep, remove_goal_observation, n_steps_lookahead, mimic_z_axis, rsi)
    def observation_spec(self)
    def step(self, action)
    def reset(self)
    def get_fingertip_pos(self)
    def _compute_end_effector_pos_mimic_reward(self, physics)
    def _add_deep_mimic_rewards(self)
    def _remove_goal_observation(self, timestep)
    def _add_demo_observation(self, timestep)
    def get_deepmimic_rews(self)

```python
def observation_spec(self):
        return self._observation_spec
```

```python
def _compute_end_effector_pos_mimic_reward(self, physics: mjcf.Physics) -> float:
        """Computes the reward for matching the end effector positions."""
        if self._disable_joints_pos_mimic_reward:
            lh_target = self._demonstrations[self._reference_frame_idx, 0]
            rh_target = self._demonstrations[self._reference_frame_idx, 1]
        else:
            # Last 15 dimensions are for end effector positions.
            lh_target = self._demonstrations[self._reference_frame_idx, 0, 27:]
            rh_target = self._demonstrations[self._reference_frame_idx, 1, 27:]
        lh_current = np.array(self.physics.bind(self.task.left_hand.fingertip_sites).xpos).flatten()
        rh_current = np.array(self.physics.bind(self.task.right_hand.fingertip_sites).xpos).flatten()
        diffs = []
        for i in range(5):
            diffs.append(np.linalg.norm(lh_target[i*3:(i+1)*3] - lh_current[i*3:(i+1)*3]))
            diffs.append(np.linalg.norm(rh_target[i*3:(i+1)*3] - rh_current[i*3:(i+1)*3]))
        rews = tolerance(
            np.hstack(diffs),
            bounds=(0, _FINGERTIP_CLOSE_ENOUGH),
            margin=(_FINGERTIP_CLOSE_ENOUGH * 5),
            sigmoid="gaussian",
        )
        self.end_effector_mimic_rew += float(np.mean(rews))
        return float(np.mean(rews))
```

```python
def _compute_joints_pos_mimic_reward(self, physics: mjcf.Physics) -> float:
        """Computes the reward for matching the joint positions."""
        # First 27 dimensions are for joint positions.
        lh_target = self._demonstrations[self._reference_frame_idx, 0, :27]
        rh_target = self._demonstrations[self._reference_frame_idx, 1, :27]
        lh_current = self._environment.task.left_hand.observables.joints_pos(physics)
        rh_current = self._environment.task.right_hand.observables.joints_pos(physics)
        diffs = []
        for i in range(27):
            diffs.append(np.linalg.norm(lh_target[i] - lh_current[i]))
            diffs.append(np.linalg.norm(rh_target[i] - rh_current[i]))
        rews = tolerance(
            np.hstack(diffs),
            bounds=(0, _JOINTS_CLOSE_ENOUGH),
            margin=(_JOINTS_CLOSE_ENOUGH * 5),
            sigmoid="gaussian",
        )
        self.joints_mimic_rew += float(np.mean(rews))
        return float(np.mean(rews))
```

```python
def _add_deep_mimic_rewards(self):
        if not self._disable_joints_pos_mimic_reward:
            self.task._reward_fn.add("joints_pos_mimic", self._compute_joints_pos_mimic_reward)
        if not self._disable_end_effector_pos_mimic_reward:
            self.task._reward_fn.add("end_effector_pos_mimic", self._compute_end_effector_pos_mimic_reward)
```

```python
def _remove_goal_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        if self._remove_goal_obs:
            timestep.observation.pop("goal")
            timestep.observation.pop("piano/state")
            timestep.observation.pop("piano/sustain_state")
        return timestep
```

```python
def _add_demo_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        demo = self._demonstrations[self._reference_frame_idx].flatten()
        return timestep._replace(
            observation=collections.OrderedDict(
                timestep.observation, **{"demo": demo}
            )
        )
```

```python
def observation_spec(self):
        return self._observation_spec
```

```python
def _compute_end_effector_pos_mimic_reward(self, physics: mjcf.Physics) -> float:
        """Computes the reward for matching the end effector positions."""
        # Give full reward when it is at initial buffer time.
        if self._reference_frame_idx < 0:
            return 0
        lh_target = self._demonstrations_lh[self._reference_frame_idx].T
        rh_target = self._demonstrations_rh[self._reference_frame_idx].T
        lh_current = np.array(self.physics.bind(self.task.left_hand.fingertip_sites).xpos).flatten()
        rh_current = np.array(self.physics.bind(self.task.right_hand.fingertip_sites).xpos).flatten()
        diffs = []
        diffs_z = []
        if self._mimic_z_axis:
            for i in range(5):
                diffs.append(np.linalg.norm(lh_target[i, :2] - lh_current[i*3:(i+1)*3][:2]))
                diffs.append(np.linalg.norm(rh_target[i, :2] - rh_current[i*3:(i+1)*3][:2])) 
                diffs_z.append(np.abs(lh_target[i, 2] - lh_current[i*3:(i+1)*3][2]))
                diffs_z.append(np.abs(rh_target[i, 2] - rh_current[i*3:(i+1)*3][2]))
            rews = tolerance(
                np.hstack(diffs),
                bounds=(0, _FINGERTIP_CLOSE_ENOUGH),
                margin=(_FINGERTIP_CLOSE_ENOUGH * 5),
                sigmoid="gaussian",
            )
            rews_z = tolerance(
                np.hstack(diffs_z),
                bounds=(0, _FINGERTIP_CLOSE_ENOUGH_Z),
                margin=(_FINGERTIP_CLOSE_ENOUGH_Z),
                sigmoid="gaussian",
            )
            rew = 0.5*(float(np.mean(rews)) + float(np.mean(rews_z)))
            self.end_effector_mimic_rew_z += 0.5*float(np.mean(rews_z))
        else:
            for i in range(5):
                diffs.append(np.linalg.norm(lh_target[i, :2] - lh_current[i*3:(i+1)*3][:2]))
                diffs.append(np.linalg.norm(rh_target[i, :2] - rh_current[i*3:(i+1)*3][:2])) 
            rews = tolerance(
                np.hstack(diffs),
                bounds=(0, _FINGERTIP_CLOSE_ENOUGH),
                margin=(_FINGERTIP_CLOSE_ENOUGH * 5),
                sigmoid="gaussian",
            )
            rew = float(np.mean(rews))
        self.end_effector_mimic_rew += rew
        return rew
```

```python
def _add_deep_mimic_rewards(self):
        self.task._reward_fn.add("end_effector_pos_mimic", self._compute_end_effector_pos_mimic_reward)
```

```python
def _remove_goal_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        if self._remove_goal_obs:
            timestep.observation.pop("goal")
            timestep.observation.pop("piano/state")
            timestep.observation.pop("piano/sustain_state")
        return timestep
```

```python
def _add_demo_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        if self._reference_frame_idx < 0:
            # If it is at initial buffer time, use the first frame.
            demo_lh = np.array([self._demonstrations_lh[0].T]*(self._n_steps_lookahead+1))
            demo_rh = np.array([self._demonstrations_rh[0].T]*(self._n_steps_lookahead+1))
            for i in range(0, max(0, self._reference_frame_idx+self._n_steps_lookahead+1)):
                demo_lh[i-self._reference_frame_idx] = self._demonstrations_lh[i].T
                demo_rh[i-self._reference_frame_idx] = self._demonstrations_rh[i].T
        else:
            demo_lh = np.array([self._demonstrations_lh[-1].T]*(self._n_steps_lookahead+1))
            demo_rh = np.array([self._demonstrations_rh[-1].T]*(self._n_steps_lookahead+1))
            for i in range(self._reference_frame_idx, min(self._reference_frame_idx+self._n_steps_lookahead, self._demonstrations_length)):
                demo_lh[i-self._reference_frame_idx] = self._demonstrations_lh[i].T
                demo_rh[i-self._reference_frame_idx] = self._demonstrations_rh[i].T
        return timestep._replace(
            observation=collections.OrderedDict(
                timestep.observation, **{"demo_lh": demo_lh.flatten(), 
                                        "demo_rh": demo_rh.flatten()}
            )
        )
```
```

### single_task/wrappers/dm2gym.py

```
def convert_dm_control_to_gym_space(dm_control_space)
class Dm2GymWrapper(Env)
    def __init__(self, environment)
    def seed(self, seed)
    def step(self, action)
    def reset(self, seed)
    def render(self, mode)
    def close(self)
```

### single_task/wrappers/residual.py

```
"""A wrapper for residual learning framework."""
class ResidualWrapper(EnvironmentWrapper)
    """Change step function."""
    def __init__(self, environment, demonstrations_lh, demonstrations_rh, demo_ctrl_timestep, rsi, enable_ik, external_demo)
    def observation_spec(self)
    def _add_prior_action_observation(self, timestep)
    def _add_demo_observation(self, timestep)
    def set_current_demo(self, demonstrations_lh, demonstrations_rh)
    def _get_prior_action(self)
    def qpos2ctrl(self, qpos)
    def step(self, action)
    def get_non_residual_action(self)
    def reset(self)

```python
def observation_spec(self):
        return self._observation_spec
```

```python
def _add_prior_action_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        prior_qpos = self._get_prior_action()
        self._prior_action = self.qpos2ctrl(prior_qpos)
        return timestep._replace(
            observation=collections.OrderedDict(
                timestep.observation, **{"prior_action": self._prior_action}
            )
        )
```

```python
def _add_demo_observation(self, timestep: dm_env.TimeStep) -> dm_env.TimeStep:
        if self._external_demo:
            if self.current_demo_lh is not None and self.current_demo_rh is not None:
                demo_lh = self.current_demo_lh[0:self.task._n_steps_lookahead+1]
                demo_rh = self.current_demo_rh[0:self.task._n_steps_lookahead+1]
                self.current_demo_lh = None
                self.current_demo_rh = None
            else:
                raise ValueError("External demo is enabled but no demo is provided.")
        else:
            demo_lh = self._demonstrations_lh[self._reference_frame_idx:self._reference_frame_idx+self.task._n_steps_lookahead+1]
            demo_rh = self._demonstrations_rh[self._reference_frame_idx:self._reference_frame_idx+self.task._n_steps_lookahead+1]
            if self._reference_frame_idx + self.task._n_steps_lookahead >= self._demonstrations_length:
                # Fill rest with the last frame
                demo_lh = np.concatenate((demo_lh, self._demonstrations_lh[-1].reshape(1, 3, 6).repeat(self._reference_frame_idx + self.task._n_steps_lookahead - self._demonstrations_length + 1, axis=0)))
                demo_rh = np.concatenate((demo_rh, self._demonstrations_rh[-1].reshape(1, 3, 6).repeat(self._reference_frame_idx + self.task._n_steps_lookahead - self._demonstrations_length + 1, axis=0)))
        demo_lh = np.transpose(demo_lh, (0, 2, 1)).flatten()
        demo_rh = np.transpose(demo_rh, (0, 2, 1)).flatten()
        demo = np.concatenate((demo_lh, demo_rh)).flatten()
        return timestep._replace(
            observation=collections.OrderedDict(
                timestep.observation, **{"demo": demo}
            )
        )
```
```