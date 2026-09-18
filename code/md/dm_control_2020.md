# dm_control_2020

source: https://github.com/google-deepmind/dm_control


commit: 3e9cd0bf3ec5141f3c6225e77f3ef99b42df2426


## README

# `dm_control`: Google DeepMind Infrastructure for Physics-Based Simulation.

Google DeepMind's software stack for physics-based simulation and Reinforcement
Learning environments, using MuJoCo physics.

An **introductory tutorial** for this package is available as a Colaboratory
notebook:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/dm_control/blob/main/tutorial.ipynb)

## Overview

This package consists of the following "core" components:

-   [`dm_control.mujoco`]: Libraries that provide Python bindings to the MuJoCo
    physics engine.

-   [`dm_control.suite`]: A set of Python Reinforcement Learning environments
    powered by the MuJoCo physics engine.

-   [`dm_control.viewer`]: An interactive environment viewer.

Additionally, the following components are available for the creation of more
complex control tasks:

-   [`dm_control.mjcf`]: A library for composing and modifying MuJoCo MJCF
    models in Python.

-   `dm_control.composer`: A library for defining rich RL environments from
    reusable, self-contained components.

-   [`dm_control.locomotion`]: Additional libraries for custom tasks.

-   [`dm_control.locomotion.soccer`]: Multi-agent soccer tasks.

If you use this package, please cite our accompanying [publication]:

```
@article{tunyasuvunakool2020,
         title = {dm_control: Software and tasks for continuous control},
         journal = {Software Impacts},
         volume = {6},
         pages = {100022},
         year = {2020},
         issn = {2665-9638},
         doi = {https://doi.org/10.1016/j.simpa.2020.100022},
         url = {https://www.sciencedirect.com/science/article/pii/S2665963820300099},
         author = {Saran Tunyasuvunakool and Alistair Muldal and Yotam Doron and
                   Siqi Liu and Steven Bohez and Josh Merel and Tom Erez and
                   Timothy Lillicrap and Nicolas Heess and Yuval Tassa},
}
```

## Installation

Install `dm_control` from PyPI by running

```sh
pip install dm_control
```

> **Note**: **`dm_control` cannot be installed in "editable" mode** (i.e. `pip
> install -e`).
>
> While `dm_control` has been largely updated to use the pybind11-based bindings
> provided via the `mujoco` package, at this time it still relies on some legacy
> components that are automatically generated from MuJoCo header files in a way
> that is incompatible with editable mode. Attempting to install `dm_control` in
> editable mode will result in import errors like:
>
> ```
> ImportError: cannot import name 'constants' from partially initialized module 'dm_control.mujoco.wrapper.mjbindings' ...
> ```
>
> The solution is to `pip uninstall dm_control` and then reinstall it without
> the `-e` flag.

## Versioning

Starting from version 1.0.0, we adopt semantic versioning.

Prior to version 1.0.0, the `dm_control` Python package was versioned `0.0.N`,
where `N` was an internal revision number that increased by an arbitrary amount
at every single Git commit.

If you want to install an unreleased version of `dm_control` directly from our
repository, you can do so by running `pip install
git+https://github.com/google-deepmind/dm_control.git`.

## Rendering

The MuJoCo Python bindings support three different OpenGL rendering backends:
EGL (headless, hardware-accelerated), GLFW (windowed, hardware-accelerated), and
OSMesa (purely software-based). At least one of these three backends must be
available in order render through `dm_control`.

*   Hardware rendering with a windowing system is supported via GLFW and GLEW.
    On Linux these can be installed using your distribution's package manager.
    For example, on Debian and Ubuntu, this can be done by running `sudo apt-get
    install libglfw3 libglew2.0`. Please note that:

    -   [`dm_control.viewer`] can only be used with GLFW.
    -   GLFW will not work on headless machines.

*   "Headless" hardware rendering (i.e. without a windowing system such as X11)
    requires [EXT_platform_device] support in the EGL driver. Recent Nvidia
    drivers support this. You will also need GLEW. On Debian and Ubuntu, this
    can be installed via `sudo apt-get install libglew2.0`.

*   Software rendering requires GLX and OSMesa. On Debian and Ubuntu these can
    be installed using `sudo apt-get install libgl1-mesa-glx libosmesa6`.

By default, `dm_control` will attempt to use GLFW first, then EGL, then OSMesa.
You can also specify a particular backend to use by setting the `MUJOCO_GL=`
environment variable to `"glfw"`, `"egl"`, or `"osmesa"`, respectively. When
rendering with EGL, you can also specify which GPU to use for rendering by
setting the environment variable `MUJOCO_EGL_DEVICE_ID=` to the target GPU ID.

## Additional instructions for Homebrew users on macOS

1.  The above instructions using `pip` should work, provided that you use a
    Python interpreter that is installed by Homebrew (rather than the
    system-default one).

2.  Before running, the `DYLD_LIBRARY_PATH` environment variable needs to be
    updated with the path to the GLFW library. This can be done by running
    `export DYLD_LIBRARY_PATH=$(brew --prefix)/lib:$DYLD_LIBRARY_PATH`.

[EXT_platform_device]: https://www.khronos.org/registry/EGL/extensions/EXT/EGL_EXT_platform_device.txt
[Releases page on the MuJoCo GitHub repository]: https://github.com/google-deepmind/mujoco/releases
[MuJoCo website]: https://mujoco.org/
[publication]: https://doi.org/10.1016/j.simpa.2020.100022
[`ctypes`]: https://docs.python.org/3/library/ctypes.html
[`dm_control.mjcf`]: dm_control/mjcf/README.md
[`dm_control.mujoco`]: dm_control/mujoco/README.md
[`dm_control.suite`]: dm_control/suite/README.md
[`dm_control.viewer`]: dm_control/viewer/README.md
[`dm_control.locomotion`]: dm_control/locomotion/README.md
[`dm_control.locomotion.soccer`]: dm_control/locomotion/soccer/README.md


## File tree (depth 3, assets pruned)

```
.gitignore
AUTHORS
CONTRIBUTING.md
LICENSE
README.md
dm_control/
  __init__.py
  _render/
    __init__.py
    base.py
    base_test.py
    constants.py
    executor/
    glfw_renderer.py
    glfw_renderer_test.py
    pyopengl/
  autowrap/
    __init__.py
    autowrap.py
    binding_generator.py
    codegen_util.py
    header_parsing.py
  blender/
    fake_core/
    mujoco_exporter/
  composer/
    __init__.py
    arena.py
    arena.xml
    constants.py
    define.py
    entity.py
    entity_test.py
    environment.py
    environment_hooks_test.py
    environment_test.py
    hooks_test_utils.py
    initializer.py
    initializers/
    observation/
    robot.py
    task.py
    variation/
  entities/
    __init__.py
    manipulators/
    props/
  locomotion/
    README.md
    __init__.py
    arenas/
    examples/
    gaps.png
    mocap/
    props/
    soccer/
    tasks/
    walkers/
    walls.png
  manipulation/
    __init__.py
    bricks.py
    explore.py
    lift.py
    manipulation_test.py
    place.py
    props/
    reach.py
    shared/
  mujoco/
    README.md
    __init__.py
    engine.py
    engine_test.py
    index.py
    index_test.py
    math.py
    math_test.py
    render_test.py
    testing/
    thread_safety_test.py
    tutorial.ipynb
    wrapper/
  rl/
    __init__.py
    control.py
    control_test.py
  suite/
    README.md
    __init__.py
    acrobot.py
    acrobot.xml
    all_domains.png
    ball_in_cup.py
    ball_in_cup.xml
    base.py
    cartpole.py
    cartpole.xml
    cheetah.py
    cheetah.xml
    common/
    demos/
    dog.py
    dog.xml
    dog_assets/
    explore.py
    finger.py
    finger.xml
    fish.py
    fish.xml
    hopper.py
    hopper.xml
    humanoid.py
    humanoid.xml
    humanoid_CMU.py
    humanoid_CMU.xml
    loader_test.py
    lqr.py
    lqr.xml
    lqr_solver.py
    lqr_test.py
    manipulator.py
    manipulator.xml
    pendulum.py
    pendulum.xml
    point_mass.py
    point_mass.xml
    quadruped.py
    quadruped.xml
    reacher.py
    reacher.xml
    stacker.py
    stacker.xml
    suite_test.py
    swimmer.py
    swimmer.xml
    utils/
    walker.py
    walker.xml
    wrappers/
  utils/
    __init__.py
    containers.py
    containers_test.py
    inverse_kinematics.py
    inverse_kinematics_test.py
    io.py
    rewards.py
    rewards_test.py
    transformations.py
    transformations_test.py
    xml_tools.py
    xml_tools_test.py
  viewer/
    README.md
    __init__.py
    application.py
    application_test.py
    gui/
    policy.gif
    renderer.py
    renderer_test.py
    runtime.py
    runtime_test.py
    user_input.py
    user_input_test.py
    util.py
    util_test.py
    viewer.py
    viewer_test.py
    views.py
    views_test.py
migration_guide_1.0.md
pyproject.toml
requirements.txt
setup.py
tutorial.ipynb
```

## Config files (0)


## Python signatures and reward/observation bodies (47 files)


### dm_control/composer/environment.py

```
"""RL environment classes for Composer tasks."""
def _empty_function_with_docstring()
def _callable_is_trivial(f)
class ObservationPadding(Enum)
class EpisodeInitializationError(RuntimeError)
    """Raised by a `composer.Task` when it fails to initialize an episode."""
class _Hook()
    def __init__(self)
class _EnvironmentHooks()
    """Helper object that scans and memoizes various hooks in a task.

This object exist to ensure that we do not incur a substantial overhead in
calling empty entity hooks in more complicated tasks."""
    def __init__(self, task)
    def refresh_entity_hooks(self)
    def add_extra_hook(self, hook_name, hook_callable)
    def initialize_episode_mjcf(self, random_state)
    def after_compile(self, physics, random_state)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def before_substep(self, physics, action, random_state)
    def after_substep(self, physics, random_state)
    def after_step(self, physics, random_state)
class _CommonEnvironment()
    """Common components for RL environments."""
    def __init__(self, task, time_limit, random_state, n_sub_steps, raise_exception_on_physics_error, strip_singleton_obs_buffer_dim, delayed_observation_padding, legacy_step)
    def add_extra_hook(self, hook_name, hook_callable)
    def _recompile_physics_and_update_observables(self)
    def _recompile_physics(self)
    def _make_observation_updater(self)
    def physics(self)
    def task(self)
    def random_state(self)
    def control_timestep(self)
class Environment(_CommonEnvironment, Environment)
    """Reinforcement learning environment for Composer tasks."""
    def __init__(self, task, time_limit, random_state, n_sub_steps, raise_exception_on_physics_error, strip_singleton_obs_buffer_dim, max_reset_attempts, recompile_mjcf_every_episode, fixed_initial_state, delayed_observation_padding, legacy_step)
    def reset(self)
    def _reset_attempt(self)
    def step_spec(self)
    def step(self, action)
    def _substep(self, action)
    def close(self)
    def action_spec(self)
    def reward_spec(self)
    def discount_spec(self)
    def observation_spec(self)

```python
def _make_observation_updater(self):
    pad_with_initial_value = (
        self._delayed_observation_padding == ObservationPadding.INITIAL_VALUE)
    return observation.Updater(
        self._task.observables, self._task.physics_steps_per_control_step,
        self._strip_singleton_obs_buffer_dim, pad_with_initial_value)
```

```python
def reward_spec(self):
    """Describes the reward returned by this environment.

    This will be the output of `self.task.reward_spec()` if it is not None,
    otherwise it will be the default spec returned by
    `dm_env.Environment.reward_spec()`.

    Returns:
      A `specs.Array` instance, or a nested dict, list or tuple of
      `specs.Array`s.
    """
    task_reward_spec = self._task.get_reward_spec()
    if task_reward_spec is not None:
      return task_reward_spec
    else:
      return super().reward_spec()
```

```python
def observation_spec(self):
    """Returns the observation specification for this environment.

    Returns:
      An `OrderedDict` mapping observation name to `specs.Array` containing
      observation shape and dtype.
    """
    return self._observation_updater.observation_spec()
```
```

### dm_control/composer/environment_hooks_test.py

```
"""Tests for Entity and Task hooks in an Environment."""
class EnvironmentHooksTest(HooksTestMixin, TestCase)
    def testEnvironmentHooksScheduling(self)
```

### dm_control/composer/environment_test.py

```
"""Tests for dm_control.composer.environment."""
class DummyTask(NullTask)
    def __init__(self)
    def task_observables(self)
class DummyTaskWithResetFailures(DummyTask)
    def __init__(self, num_reset_failures)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
class DummyTaskWithRandomObservation(NullTask)
    def __init__(self)
    def initialize_episode(self, physics, random_state)
    def task_observables(self)
class EnvironmentTest(TestCase)
    def test_failed_resets(self)
    def test_get_spec(self, name, defined_in_task)
    def test_can_provide_observation(self)
    def test_dont_compile_mjcf_between_episodes(self)
    def test_fixed_initial_state(self)

```python
def test_can_provide_observation(self):
    task = DummyTask()
    env = composer.Environment(task)
    obs = env.reset().observation
    self.assertLen(obs, 1)
    np.testing.assert_array_equal(obs['time'], env.physics.time())
    for _ in range(20):
      obs = env.step([]).observation
      self.assertLen(obs, 1)
      np.testing.assert_array_equal(obs['time'], env.physics.time())
```
```

### dm_control/composer/observation/__init__.py

```
"""Multi-rate observation and buffering framework for Composer environments."""
```

### dm_control/composer/observation/fake_physics.py

```
"""A fake Physics class for unit testing observation framework."""
class FakePhysics(Physics)
    """A fake Physics class for unit testing observation framework."""
    def __init__(self)
    def step(self, sub_steps)
    def observables(self)
    def twice(self)
    def repeated(self)
    def sqrt(self)
    def sqrt_plus_one(self)
    def matrix(self)
    def time(self)
    def timestep(self)
    def set_control(self, ctrl)
    def reset(self)
    def after_reset(self)
    def suppress_physics_errors(self)
```

### dm_control/composer/observation/obs_buffer.py

```
""""An object that manages the buffering and delaying of observation."""
class InFlightObservation()
    """Represents a delayed observation that may not have arrived yet.

Attributes:
  arrival: The time at which this observation will be delivered.
  timestamp: The time at which this observation was made.
  delay: The amount of delay between the time at which this observation was
    made and the time at"""
    def __init__(self, timestamp, delay, value)
    def __lt__(self, other)
class Buffer()
    """An object that manages the buffering and delaying of observation."""
    def __init__(self, buffer_size, shape, dtype, pad_with_initial_value, strip_singleton_buffer_dim)
    def _update_arrived_deque(self, timestamp)
    def shape(self)
    def dtype(self)
    def insert(self, timestamp, delay, value)
    def read(self, current_time)
    def drop_unobserved_upcoming_items(self, observation_schedule, read_interval)
```

### dm_control/composer/observation/obs_buffer_test.py

```
"""Tests for observation.obs_buffer."""
def _generate_constant_schedule(update_timestep, delay, control_timestep, n_observed_steps)
class BufferTest(TestCase)
    def testOutOfOrderArrival(self)
    def testStripSingletonDimension(self, shape)
    def testPlanToSingleUndelayedObservation(self)
    def testPlanTwoStepsAhead(self)

```python
def testPlanToSingleUndelayedObservation(self):
    buf = obs_buffer.Buffer(buffer_size=1, shape=(), dtype=float)
    control_timestep = 20
    observation_schedule = _generate_constant_schedule(
        update_timestep=1,
        delay=0,
        control_timestep=control_timestep,
        n_observed_steps=1)
    buf.drop_unobserved_upcoming_items(
        observation_schedule, read_interval=control_timestep)
    self.assertEqual(observation_schedule, [(20, 0)])
```
```

### dm_control/composer/observation/observable/__init__.py

```
"""Module for observables in the Composer library."""
```

### dm_control/composer/observation/observable/base.py

```
"""Classes representing observables."""
def _make_aggregator(np_reducer_func, bounds_preserving)
def _get_aggregator(name_or_callable)
class Observable()
    """Abstract base class for an observable."""
    def __init__(self, update_interval, buffer_size, delay, aggregator, corruptor)
    def update_interval(self)
    def update_interval(self, value)
    def buffer_size(self)
    def buffer_size(self, value)
    def delay(self)
    def delay(self, value)
    def aggregator(self)
    def aggregator(self, value)
    def corruptor(self)
    def corruptor(self, value)
    def enabled(self)
    def enabled(self, value)
    def array_spec(self)
    def _callable(self, physics)
    def observation_callable(self, physics, random_state)
    def __call__(self, physics, random_state)
    def configure(self)
class Generic(Observable)
    """A generic observable defined via a callable."""
    def __init__(self, raw_observation_callable, update_interval, buffer_size, delay, aggregator, corruptor)
    def _callable(self, physics)
class MujocoFeature(Observable)
    """An observable corresponding to a named MuJoCo feature."""
    def __init__(self, kind, feature_name, update_interval, buffer_size, delay, aggregator, corruptor)
    def _callable(self, physics)
class MujocoCamera(Observable)
    """An observable corresponding to a MuJoCo camera."""
    def __init__(self, camera_name, height, width, update_interval, buffer_size, delay, aggregator, corruptor, depth)
    def height(self)
    def height(self, value)
    def width(self)
    def width(self, value)
    def array_spec(self)
    def _callable(self, physics)

```python
def observation_callable(self, physics, random_state=None):
    """A callable which returns a (potentially corrupted) observation."""
    raw_callable = self._callable(physics)
    if self._corruptor:
      def _corrupted():
        return self._corruptor(raw_callable(), random_state=random_state)
      return _corrupted
    else:
      return raw_callable
```
```

### dm_control/composer/observation/observable/base_test.py

```
"""Tests for observable classes."""
class _FakeBaseObservable(Observable)
    def _callable(self, physics)
class ObservableTest(TestCase)
    def testBaseProperties(self)
    def testGeneric(self)
    def testMujocoFeature(self)
    def testMujocoCamera(self)
    def testCorruptor(self)
    def testInvalidAggregatorName(self)
```

### dm_control/composer/observation/observable/mjcf.py

```
"""Observables that are defined in terms of MJCF elements."""
def _check_mjcf_element(obj)
def _check_mjcf_element_iterable(obj_iterable)
class MJCFFeature(Observable)
    """An observable corresponding to an element in an MJCF model."""
    def __init__(self, kind, mjcf_element, update_interval, buffer_size, delay, aggregator, corruptor, index)
    def _callable(self, physics)
    def __getitem__(self, key)
class MJCFCamera(Observable)
    """An observable corresponding to a camera in an MJCF model."""
    def __init__(self, mjcf_element, height, width, update_interval, buffer_size, delay, aggregator, corruptor, depth, segmentation, scene_option, render_flag_overrides)
    def height(self)
    def height(self, value)
    def width(self)
    def width(self, value)
    def depth(self)
    def depth(self, value)
    def segmentation(self)
    def segmentation(self, value)
    def scene_option(self)
    def scene_option(self, value)
    def render_flag_overrides(self)
    def render_flag_overrides(self, value)
    def array_spec(self)
    def _callable(self, physics)

```python
def get_observation():
      pixels = physics.render(
          height=self._height,
          width=self._width,
          camera_id=self._mjcf_element.full_identifier,
          depth=self._depth,
          segmentation=self._segmentation,
          scene_option=self._scene_option,
          render_flag_overrides=self._render_flag_overrides)
      return np.atleast_3d(pixels)
```
```

### dm_control/composer/observation/observable/mjcf_test.py

```
"""Tests for mjcf observables."""
class ObservableTest(TestCase)
    def testMJCFFeature(self)
    def testMJCFFeatureIndex(self)
    def testMJCFCamera(self)
    def testMJCFCameraSpecs(self, camera_type, channels, dtype, minimum, maximum)
    def testMJCFSegCamera(self)
    def testErrorIfSegmentationAndDepthBothEnabled(self)
```

### dm_control/composer/observation/updater.py

```
"""An object that creates and updates buffers for enabled observables."""
class _EnabledObservable()
    """Encapsulates an enabled observable, its buffer, and its update schedule."""
    def __init__(self, observable, physics, random_state, strip_singleton_buffer_dim, pad_with_initial_value)
    def _bind_attribute_from_observable(self, attr, default_value, random_state)
def _call_if_callable(arg)
def _validate_structure(structure)
class Updater()
    """Creates and updates buffers for enabled observables."""
    def __init__(self, observables, physics_steps_per_control_step, strip_singleton_buffer_dim, pad_with_initial_value)
    def reset(self, physics, random_state)
    def observation_spec(self)
    def prepare_for_next_control_step(self)
    def update(self)
    def get_observation(self)

```python
def observation_spec(self):
    """The observation specification for this environment.

    Returns a dict mapping the names of enabled observations to their
    corresponding `Array` or `BoundedArray` specs.

    If an obs has a BoundedArray spec, but uses an aggregator that
    does not preserve those bounds (such as `sum`), it will be mapped to an
    (unbounded) `Array` spec. If using a bounds-preserving custom aggregator
    `my_agg`, give it an attribute `my_agg.preserves_bounds = True` to indicate
    to this method that it is bounds-preserving.

    The returned specification is only valid as of the previous call
    to `reset`. In particular, it is an error to call this function before
    the first call to `reset`.

    Returns:
      A dict mapping observation name to `Array` or `BoundedArray` spec
      containing the observation shape and dtype, and possibly bounds.

    Raises:
      RuntimeError: If this method is called before `reset` has been called.
    """
    if self._enabled_structure is None:
      raise RuntimeError('`reset` must be called before `observation_spec`.')

    def make_observation_spec_dict(enabled_dict):
      """Makes a dict of enabled observation specs from of observables."""
      out_dict = type(enabled_dict)()
      for name, enabled in enabled_dict.items():

        if (enabled.observable.aggregator is None
            and enabled.observable.array_spec is not None):
          # If possible, keep the original array spec, just updating the name
          # and modifying the dimension for buffering. Doing this allows for
          # custom spec types to be exposed by the environment where possible.
          out_dict[name] = enabled.observable.array_spec.replace(
              name=name, shape=enabled.buffer.shape
          )
          continue

        if isinstance(enabled.observable.array_spec, specs.BoundedArray):
          bounds = (enabled.observable.array_spec.minimum,
                    enabled.observable.array_spec.maximum)
        else:
          bounds = None

        if enabled.observable.aggregator:
          aggregator = enabled.observable.aggregator
          aggregated = aggregator(np.zeros(enabled.buffer.shape,
                                           dtype=enabled.buffer.dtype))
          shape = aggregated.shape
          dtype = aggregated.dtype

          # Ditch bounds if the aggregator isn't known to be bounds-preserving.
          if bounds:
            if not hasattr(aggregator, 'preserves_bounds'):
              logging.warning('Ignoring the bounds of this observable\'s spec, '
                              'as its aggregator method has no boolean '
                              '`preserves_bounds` attrubute.')
              bounds = None
            elif not aggregator.preserves_bounds:
              bounds = None
        else:
          shape = enabled.buffer.shape
          dtype = enabled.buffer.dtype

        if bounds:
          spec = specs.BoundedArray(minimum=bounds[0],
                                    maximum=bounds[1],
                                    shape=shape,
                                    dtype=dtype,
                                    name=name)
        else:
          spec = specs.Array(shape=shape, dtype=dtype, name=name)

        out_dict[name] = spec
      return out_dict

    if self._is_nested:
      enabled_specs = type(self._enabled_structure)(
          make_observation_spec_dict(enabled_dict)
          for enabled_dict in self._enabled_structure)
    else:
      enabled_specs = make_observation_spec_dict(self._enabled_structure)

    return enabled_specs
```

```python
def get_observation(self):
    """Gets the current observation.

    The returned observation is only valid as of the previous call
    to `reset`. In particular, it is an error to call this function before
    the first call to `reset`.

    Returns:
      A dict, or list of dicts, or tuple of dicts, of observation values.
      The returned structure corresponds to the structure of the `observables`
      that was given at initialization time.

    Raises:
      RuntimeError: If this method is called before `reset` has been called.
    """
    if self._enabled_structure is None:
      raise RuntimeError('`reset` must be called before `observation`.')

    def aggregate_dict(enabled_dict):
      out_dict = type(enabled_dict)()
      for name, enabled in enabled_dict.items():
        if enabled.observable.aggregator:
          aggregated = enabled.observable.aggregator(
              enabled.buffer.read(self._step_counter))
        else:
          aggregated = enabled.buffer.read(self._step_counter)
        out_dict[name] = aggregated
      return out_dict

    if self._is_nested:
      return type(self._enabled_structure)(
          aggregate_dict(enabled_dict)
          for enabled_dict in self._enabled_structure)
    else:
      return aggregate_dict(self._enabled_structure)
```

```python
def make_observation_spec_dict(enabled_dict):
      """Makes a dict of enabled observation specs from of observables."""
      out_dict = type(enabled_dict)()
      for name, enabled in enabled_dict.items():

        if (enabled.observable.aggregator is None
            and enabled.observable.array_spec is not None):
          # If possible, keep the original array spec, just updating the name
          # and modifying the dimension for buffering. Doing this allows for
          # custom spec types to be exposed by the environment where possible.
          out_dict[name] = enabled.observable.array_spec.replace(
              name=name, shape=enabled.buffer.shape
          )
          continue

        if isinstance(enabled.observable.array_spec, specs.BoundedArray):
          bounds = (enabled.observable.array_spec.minimum,
                    enabled.observable.array_spec.maximum)
        else:
          bounds = None

        if enabled.observable.aggregator:
          aggregator = enabled.observable.aggregator
          aggregated = aggregator(np.zeros(enabled.buffer.shape,
                                           dtype=enabled.buffer.dtype))
          shape = aggregated.shape
          dtype = aggregated.dtype

          # Ditch bounds if the aggregator isn't known to be bounds-preserving.
          if bounds:
            if not hasattr(aggregator, 'preserves_bounds'):
              logging.warning('Ignoring the bounds of this observable\'s spec, '
                              'as its aggregator method has no boolean '
                              '`preserves_bounds` attrubute.')
              bounds = None
            elif not aggregator.preserves_bounds:
              bounds = None
        else:
          shape = enabled.buffer.shape
          dtype = enabled.buffer.dtype

        if bounds:
          spec = specs.BoundedArray(minimum=bounds[0],
                                    maximum=bounds[1],
                                    shape=shape,
                                    dtype=dtype,
                                    name=name)
        else:
          spec = specs.Array(shape=shape, dtype=dtype, name=name)

        out_dict[name] = spec
      return out_dict
```
```

### dm_control/composer/observation/updater_test.py

```
"""Tests for observation.observation_updater."""
class DeterministicSequence()
    def __init__(self, sequence)
    def __call__(self, random_state)
class BoundedGeneric(Generic)
    def __init__(self, raw_observation_callable, minimum, maximum)
    def array_spec(self)
class MyArraySpec(Array)
class GenericObservableWithMyArraySpec(Generic)
    def array_spec(self)
class UpdaterTest(TestCase)
    def testNestedSpecsAndValues(self, list_or_tuple)
    def assertCorrectSpec(self, spec, expected_shape, expected_dtype, expected_name)
    def testObservationSpecInference(self)
    def testCustomSpecTypePassedThrough(self)
    def testObservation(self, pad_with_initial_value)
    def testVariableRatesAndDelays(self)

```python
def testObservationSpecInference(self):
    physics = fake_physics.FakePhysics()
    physics.observables['repeated'].buffer_size = 5
    physics.observables['matrix'].buffer_size = 4
    physics.observables['sqrt'] = observable.Generic(
        fake_physics.FakePhysics.sqrt, buffer_size=3)

    for obs in physics.observables.values():
      obs.enabled = True

    observation_updater = updater.Updater(physics.observables)
    observation_updater.reset(physics=physics, random_state=None)

    spec = observation_updater.observation_spec()
    self.assertCorrectSpec(spec['repeated'], (5, 2), int, 'repeated')
    self.assertCorrectSpec(spec['matrix'], (4, 2, 3), int, 'matrix')
    self.assertCorrectSpec(spec['sqrt'], (3,), float, 'sqrt')
```

```python
def testObservation(self, pad_with_initial_value):
    physics = fake_physics.FakePhysics()
    physics.observables['repeated'].buffer_size = 5
    physics.observables['matrix'].delay = 1
    physics.observables['sqrt_plus_one'] = observable.Generic(
        fake_physics.FakePhysics.sqrt_plus_one, update_interval=7,
        buffer_size=3, delay=2)
    for obs in physics.observables.values():
      obs.enabled = True
    with physics.reset_context():
      pass

    physics_steps_per_control_step = 5
    observation_updater = updater.Updater(
        physics.observables, physics_steps_per_control_step,
        pad_with_initial_value=pad_with_initial_value)
    observation_updater.reset(physics=physics, random_state=None)

    for control_step in range(0, 200):
      observation_updater.prepare_for_next_control_step()
      for _ in range(physics_steps_per_control_step):
        physics.step()
        observation_updater.update()

      step_counter = (control_step + 1) * physics_steps_per_control_step

      observation = observation_updater.get_observation()
      def assert_correct_buffer(obs_name, expected_callable,
                                observation=observation,
                                step_counter=step_counter):
        update_interval = (physics.observables[obs_name].update_interval
                           or updater.DEFAULT_UPDATE_INTERVAL)
        buffer_size = (physics.observables[obs_name].buffer_size
                       or updater.DEFAULT_BUFFER_SIZE)
        delay = (physics.observables[obs_name].delay
                 or updater.DEFAULT_DELAY)

        # The final item in the buffer is the current time, less the delay,
        # rounded _down_ to the nearest multiple of the update interval.
        end = update_interval * int(
            math.floor((step_counter - delay) / update_interval))

        # Figure out the first item in the buffer by working backwards from
        # the final item in multiples of the update interval.
        start = end - (buffer_size - 1) * update_interval

        # Clamp both the start and end step number below by zero.
        buffer_range = range(max(0, start), max(0, end + 1), update_interval)

        # Arrays with expected shapes, filled with expected default values.
        expected_value_spec = observation_updater.observation_spec()[obs_name]
        if pad_with_initial_value:
          expected_values = np.full(shape=expected_value_spec.shape,
                                    fill_value=expected_callable(0),
                                    dtype=expected_value_spec.dtype)
        else:
          expected_values = np.zeros(shape=expected_value_spec.shape,
                                     dtype=expected_value_spec.dtype)

        # The arrays are filled from right to left, such that the most recent
        # entry is the rightmost one, and any padding is on the left.
        for index, timestamp in enumerate(reversed(buffer_range)):
          expected_values[-(index+1)] = expected_callable(timestamp)

        np.testing.assert_array_equal(observation[obs_name], expected_values)

      assert_correct_buffer('twice', lambda x: 2*x)
      assert_correct_buffer('matrix', lambda x: [[x]*3]*2)
      assert_correct_buffer('repeated', lambda x: [x, x])
      assert_correct_buffer('sqrt_plus_one', lambda x: np.sqrt(x) + 1)
```
```

### dm_control/composer/task.py

```
"""Abstract base class for a Composer task."""
def _check_timesteps_divisible(control_timestep, physics_timestep)
class Task()
    """Abstract base class for a Composer task."""
    def root_entity(self)
    def iter_entities(self)
    def observables(self)
    def task_observables(self)
    def after_compile(self, physics, random_state)
    def _check_root_entity(self, callee_name)
    def control_timestep(self)
    def control_timestep(self, new_value)
    def physics_timestep(self)
    def physics_timestep(self, new_value)
    def set_timesteps(self, control_timestep, physics_timestep)
    def physics_steps_per_control_step(self)
    def action_spec(self, physics)
    def get_reward_spec(self)
    def get_discount_spec(self)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def before_substep(self, physics, action, random_state)
    def after_substep(self, physics, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)
    def get_discount(self, physics)
class NullTask(Task)
    """A class that wraps a single `Entity` into a `Task` with no reward."""
    def __init__(self, root_entity)
    def root_entity(self)
    def get_reward(self, physics)

```python
def get_reward_spec(self):
    """Optional method to define non-scalar rewards for a `Task`."""
    return None
```

```python
def get_reward(self, physics):
    """Calculates the reward signal given the physics state.

    Args:
      physics: A Physics object.

    Returns:
      A float
    """
    raise NotImplementedError
```

```python
def get_reward(self, physics):
    return 0.0
```
```

### dm_control/entities/manipulators/kinova/jaco_hand.py

```
"""Module containing the standard Jaco hand."""
class JacoHand(RobotHand)
    """A composer entity representing a Jaco hand."""
    def _build(self, name, use_pinch_site_as_tcp)
    def _build_observables(self)
    def tool_center_point(self)
    def joints(self)
    def actuators(self)
    def hand_geom(self)
    def finger_geoms(self)
    def grip_site(self)
    def pinch_site(self)
    def pinch_site_pos_sensor(self)
    def pinch_site_quat_sensor(self)
    def mjcf_model(self)
    def set_grasp(self, physics, close_factors)
def _add_velocity_actuator(joint)
class JacoHandObservables(JointsObservables)
    """Observables for the Jaco hand."""
    def pinch_site_pos(self)
    def pinch_site_rmat(self)
```

### dm_control/locomotion/soccer/observables.py

```
"""Soccer observables modules."""
class ObservablesAdder()
    """A callable that adds a set of per-player observables for a task."""
    def __call__(self, task, player)
class MultiObservablesAdder(ObservablesAdder)
    """Applies multiple `ObservablesAdder`s to a soccer task and player."""
    def __init__(self, observables)
    def __call__(self, task, player)
class CoreObservablesAdder(ObservablesAdder)
    """Core set of per player observables."""
    def __call__(self, task, player)
    def _add_player_observables_on_other(self, player, other, prefix)
    def _add_player_observables_on_ball(self, player, ball)
    def _add_player_proprio_observables(self, player)
    def _add_player_arena_observables(self, player, arena)
    def _add_player_stats_observables(self, task, player)
class InterceptionObservablesAdder(ObservablesAdder)
    """Adds obervables representing interception events.

These observables represent events where this player received the ball from
another player, or when an opponent intercepted the ball from this player's
team. For each type of event there are three different thresholds applied to
the distance travell"""
    def __call__(self, task, player)
```

### dm_control/locomotion/soccer/task.py

```
""""A task where players play a soccer game."""
def _disable_geom_contacts(entities)
class Task(Task)
    """A task where two teams of walkers play soccer."""
    def __init__(self, players, arena, ball, initializer, observables, disable_walker_contacts, nconmax_per_player, njmax_per_player, control_timestep, tracking_cameras)
    def observables(self)
    def _throw_in(self, physics, random_state, ball)
    def _tracked_entity_positions(self, physics)
    def after_compile(self, physics, random_state)
    def after_step(self, physics, random_state)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def root_entity(self)
    def get_reward(self, physics)
    def get_reward_spec(self)
    def get_discount(self, physics)
    def get_discount_spec(self)
    def should_terminate_episode(self, physics)
    def before_step(self, physics, actions, random_state)
    def action_spec(self, physics)
class MultiturnTask(Task)
    """Continuous game play through scoring events until timeout."""
    def __init__(self, players, arena, ball, initializer, observables, disable_walker_contacts, nconmax_per_player, njmax_per_player, control_timestep, tracking_cameras)
    def should_terminate_episode(self, physics)
    def get_discount(self, physics)
    def before_step(self, physics, actions, random_state)
    def after_step(self, physics, random_state)

```python
def get_reward(self, physics):
    """Returns a list of per-player rewards.

    Each player will receive a reward of:
      +1 if their team scored a goal
      -1 if their team conceded a goal
      0 if no goals were scored on this timestep.

    Note: the observations also contain various environment statistics that may
    be used to derive per-player rewards (as done in
    http://arxiv.org/abs/1902.07151).

    Args:
      physics: An instance of `Physics`.

    Returns:
      A list of 0-dimensional numpy arrays, one per player.
    """
    scoring_team = self.arena.detected_goal()
    if not scoring_team:
      return [np.zeros((), dtype=np.float32) for _ in self.players]

    rewards = []
    for p in self.players:
      if p.team == scoring_team:
        rewards.append(np.ones((), dtype=np.float32))
      else:
        rewards.append(-np.ones((), dtype=np.float32))
    return rewards
```

```python
def get_reward_spec(self):
    return [
        specs.Array(name="reward", shape=(), dtype=np.float32)
        for _ in self.players
    ]
```
```

### dm_control/locomotion/soccer/task_test.py

```
"""Tests for locomotion.tasks.soccer."""
def _walker(name, walker_id, marker_rgba)
def _team_players(team_size, team, team_name, team_color)
def _home_team(team_size)
def _away_team(team_size)
def _env(players, disable_walker_contacts, observables, random_state)
def _observables_adder(observables_adder)
class TaskTest(TestCase)
    def _assert_all_count_equal(self, list_of_lists)
    def test_step_environment(self, team_size, observables_adder, num_obs, disable_walker_contacts)
    def test_num_players(self, home_size, away_size, num_observations)
    def test_all_contacts(self)
    def test_symmetric_observations(self)
    def test_symmetric_dynamic_observations(self)
    def test_prev_actions(self)
    def test_scoring_rewards(self, home_size, away_size, ball_vel_x, expected_home_score)
    def test_throw_in(self)
    def test_terminal_discount(self, init_ball_vel_x, expected_terminal_discount)
    def test_render(self, take_step)
class UniformInitializerTest(TestCase)
    def test_walker_position(self, spawn_ratio)
    def test_walker_rotation(self)
    def test_walker_velocity(self)
    def test_ball_position(self, spawn_ratio, init_ball_z)
    def test_ball_velocity(self)
class _ScoringInitializer(Initializer)
    """Initialize the ball for home team to repeatedly score goals."""
    def __init__(self)
    def num_calls(self)
    def __call__(self, task, physics, random_state)
class MultiturnTaskTest(TestCase)
    def test_multiple_goals(self)

```python
def test_symmetric_observations(self):
    env = _env(_home_team(1) + _away_team(1))

    def _symmetric_configuration(physics, unused_random_state):
      walkers = [p.walker for p in env.task.players]
      ball = env.task.ball

      x, y, rotation = 0., 0., np.pi / 6.
      ball.set_pose(physics, [x, y, 0.5])
      ball.set_velocity(
          physics, velocity=np.zeros(3), angular_velocity=np.zeros(3))

      x, y, rotation = 5., 3., np.pi / 3.
      quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
      walkers[0].set_pose(physics, [x, y, 0.], quat)
      walkers[0].set_velocity(
          physics, velocity=np.zeros(3), angular_velocity=np.zeros(3))

      x, y, rotation = -5., -3., np.pi / 3. + np.pi
      quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
      walkers[1].set_pose(physics, [x, y, 0.], quat)
      walkers[1].set_velocity(
          physics, velocity=np.zeros(3), angular_velocity=np.zeros(3))

    env.add_extra_hook("initialize_episode", _symmetric_configuration)

    timestep = env.reset()
    obs_a, obs_b = timestep.observation
    self.assertCountEqual(list(obs_a.keys()), list(obs_b.keys()))
    for k in sorted(obs_a.keys()):
      o_a, o_b = obs_a[k], obs_b[k]
      self.assertTrue(
          np.allclose(o_a, o_b) or np.allclose(o_a, -o_b),
          k + " not equal:" + str(o_a) + ";" + str(o_b))
```

```python
def test_symmetric_dynamic_observations(self):
    env = _env(_home_team(1) + _away_team(1))

    def _symmetric_configuration(physics, unused_random_state):
      walkers = [p.walker for p in env.task.players]
      ball = env.task.ball

      x, y, rotation = 0., 0., np.pi / 6.
      ball.set_pose(physics, [x, y, 0.5])
      # Ball shooting up. Walkers going tangent.
      ball.set_velocity(physics, velocity=[0., 0., 1.],
                        angular_velocity=[0., 0., 0.])

      x, y, rotation = 5., 3., np.pi / 3.
      quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
      walkers[0].set_pose(physics, [x, y, 0.], quat)
      walkers[0].set_velocity(physics, velocity=[y, -x, 0.],
                              angular_velocity=[0., 0., 0.])

      x, y, rotation = -5., -3., np.pi / 3. + np.pi
      quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
      walkers[1].set_pose(physics, [x, y, 0.], quat)
      walkers[1].set_velocity(physics, velocity=[y, -x, 0.],
                              angular_velocity=[0., 0., 0.])

    env.add_extra_hook("initialize_episode", _symmetric_configuration)

    timestep = env.reset()
    obs_a, obs_b = timestep.observation
    self.assertCountEqual(list(obs_a.keys()), list(obs_b.keys()))
    for k in sorted(obs_a.keys()):
      o_a, o_b = obs_a[k], obs_b[k]
      self.assertTrue(
          np.allclose(o_a, o_b) or np.allclose(o_a, -o_b),
          k + " not equal:" + str(o_a) + ";" + str(o_b))
```

```python
def test_scoring_rewards(
      self, home_size, away_size, ball_vel_x, expected_home_score):
    env = _env(_home_team(home_size) + _away_team(away_size))

    def _score_configuration(physics, random_state):
      del random_state  # Unused.
      # Send the ball shooting towards either the home or away goal.
      env.task.ball.set_pose(physics, [0., 0., 0.5])
      env.task.ball.set_velocity(physics,
                                 velocity=[ball_vel_x, 0., 0.],
                                 angular_velocity=[0., 0., 0.])

    env.add_extra_hook("initialize_episode", _score_configuration)

    actions = [np.zeros(s.shape, s.dtype) for s in env.action_spec()]

    # Disable contacts and gravity so that the ball follows a straight path.
    with env.physics.model.disable("contact", "gravity"):

      timestep = env.reset()
      with self.subTest("Reward and discount are None on the first timestep"):
        self.assertTrue(timestep.first())
        self.assertIsNone(timestep.reward)
        self.assertIsNone(timestep.discount)

      # Step until the episode ends.
      timestep = env.step(actions)
      while not timestep.last():
        self.assertTrue(timestep.mid())
        # For non-terminal timesteps, the reward should always be 0 and the
        # discount should always be 1.
        np.testing.assert_array_equal(np.hstack(timestep.reward), 0.)
        self.assertEqual(timestep.discount, 1.)
        timestep = env.step(actions)

    # If a goal was scored then the epsiode should have ended with a discount of
    # 0. If neither team scored and the episode ended due to hitting the time
    # limit then the discount should be 1.
    with self.subTest("Correct terminal discount"):
      if expected_home_score != 0:
        expected_discount = 0.
      else:
        expected_discount = 1.
      self.assertEqual(timestep.discount, expected_discount)

    with self.subTest("Correct terminal reward"):
      reward = np.hstack(timestep.reward)
      np.testing.assert_array_equal(reward[:home_size], expected_home_score)
      np.testing.assert_array_equal(reward[home_size:], -expected_home_score)
```
```

### dm_control/locomotion/tasks/__init__.py

```
"""Tasks in the Locomotion library."""
```

### dm_control/locomotion/tasks/corridors.py

```
"""Corridor-based locomotion tasks."""
class RunThroughCorridor(Task)
    """A task that requires a walker to run through a corridor.

This task rewards an agent for controlling a walker to move at a specific
target velocity along the corridor, and for minimising the magnitude of the
control signals used to achieve this."""
    def __init__(self, walker, arena, walker_spawn_position, walker_spawn_rotation, target_velocity, contact_termination, terminate_at_height, physics_timestep, control_timestep)
    def root_entity(self)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def _is_disallowed_contact(self, contact)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)
    def get_discount(self, physics)

```python
def get_reward(self, physics):
    walker_xvel = physics.bind(self._walker.root_body).subtree_linvel[0]
    xvel_term = rewards.tolerance(
        walker_xvel, (self._vel, self._vel),
        margin=self._vel,
        sigmoid='linear',
        value_at_margin=0.0)
    return xvel_term
```
```

### dm_control/locomotion/tasks/corridors_test.py

```
"""Tests for dm_control.locomotion.tasks.corridors."""
class CorridorsTest(TestCase)
    def test_walker_is_correctly_reinitialized(self, position_offset, rotate_180_degrees, use_variations)
    def test_termination_and_discount(self)
```

### dm_control/locomotion/tasks/escape.py

```
"""Escape locomotion tasks."""
class Escape(Task)
    """A task solved by escaping a starting area (e.g. bowl-shaped terrain)."""
    def __init__(self, walker, arena, walker_spawn_position, walker_spawn_rotation, physics_timestep, control_timestep)
    def root_entity(self)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def get_reward(self, physics)
    def get_discount(self, physics)
def _find_non_contacting_height(physics, walker, orientation, x_pos, y_pos, maxiter)
def _upright_reward(physics, walker, deviation_angle)

```python
def _upright_reward(physics, walker, deviation_angle=0):
  """Returns a reward proportional to how upright the torso is.

  Args:
    physics: an instance of `Physics`.
    walker: the focal walker.
    deviation_angle: A float, in degrees. The reward is 0 when the torso is
      exactly upside-down and 1 when the torso's z-axis is less than
      `deviation_angle` away from the global z-axis.
  """
  deviation = np.cos(np.deg2rad(deviation_angle))
  upright_torso = physics.bind(walker.root_body).xmat[-1]
  if hasattr(walker, 'pelvis_body'):
    upright_pelvis = physics.bind(walker.pelvis_body).xmat[-1]
    upright_zz = np.stack([upright_torso, upright_pelvis])
  else:
    upright_zz = upright_torso
  upright = rewards.tolerance(upright_zz,
                              bounds=(deviation, float('inf')),
                              sigmoid='linear',
                              margin=1 + deviation,
                              value_at_margin=0)
  return np.min(upright)
```

```python
def get_reward(self, physics):
    # Escape reward term.
    terrain_size = physics.model.hfield_size[_HEIGHTFIELD_ID, 0]
    escape_reward = rewards.tolerance(
        np.asarray(np.linalg.norm(
            physics.named.data.site_xpos[self._reward_body])),
        bounds=(terrain_size, float('inf')),
        margin=terrain_size,
        value_at_margin=0,
        sigmoid='linear')
    upright_reward = _upright_reward(physics, self._walker, deviation_angle=30)
    return upright_reward * escape_reward
```
```

### dm_control/locomotion/tasks/escape_test.py

```
"""Tests for locomotion.tasks.escape."""
class EscapeTest(TestCase)
    def test_observables(self)
    def test_contact(self)
```

### dm_control/locomotion/tasks/go_to_target.py

```
"""Task for a walker to move to a target."""
class GoToTarget(Task)
    """A task that requires a walker to move towards a target."""
    def __init__(self, walker, arena, moving_target, target_relative, target_relative_dist, steps_before_moving_target, distance_tolerance, target_spawn_position, walker_spawn_position, walker_spawn_rotation, physics_timestep, control_timestep)
    def root_entity(self)
    def target_position(self, physics)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def _is_disallowed_contact(self, contact)
    def should_terminate_episode(self, physics)
    def get_discount(self, physics)
    def get_reward(self, physics)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)

```python
def get_reward(self, physics):
    reward = 0.
    distance = np.linalg.norm(
        physics.bind(self._target).pos[:2] -
        physics.bind(self._walker.root_body).xpos[:2])
    if distance < self._distance_tolerance:
      reward = 1.
      if self._moving_target:
        self._reward_step_counter += 1
    return reward
```
```

### dm_control/locomotion/tasks/go_to_target_test.py

```
"""Tests for locomotion.tasks.go_to_target."""
class GoToTargetTest(TestCase)
    def test_observables(self)
    def test_target_position_randomized_on_reset(self)
    def test_reward_fixed_target(self)
    def test_reward_moving_target(self)
    def test_termination_and_discount(self)

```python
def test_reward_fixed_target(self):
    walker = cmu_humanoid.CMUHumanoid()
    arena = floors.Floor()
    task = go_to_target.GoToTarget(
        walker=walker, arena=arena, moving_target=False)

    random_state = np.random.RandomState(12345)
    env = composer.Environment(task, random_state=random_state)
    env.reset()

    target_position = task.target_position(env.physics)
    zero_action = np.zeros_like(env.physics.data.ctrl)
    for _ in range(2):
      timestep = env.step(zero_action)
      self.assertEqual(timestep.reward, 0)
    walker_pos = env.physics.bind(walker.root_body).xpos
    walker.set_pose(
        env.physics,
        position=[target_position[0], target_position[1], walker_pos[2]])
    env.physics.forward()

    # Receive reward while the agent remains at that location.
    timestep = env.step(zero_action)
    self.assertEqual(timestep.reward, 1)

    # Target position should not change.
    np.testing.assert_array_equal(target_position,
                                  task.target_position(env.physics))
```

```python
def test_reward_moving_target(self):
    walker = cmu_humanoid.CMUHumanoid()
    arena = floors.Floor()

    steps_before_moving_target = 2
    task = go_to_target.GoToTarget(
        walker=walker,
        arena=arena,
        moving_target=True,
        steps_before_moving_target=steps_before_moving_target)
    random_state = np.random.RandomState(12345)
    env = composer.Environment(task, random_state=random_state)
    env.reset()

    target_position = task.target_position(env.physics)
    zero_action = np.zeros_like(env.physics.data.ctrl)
    for _ in range(2):
      timestep = env.step(zero_action)
      self.assertEqual(timestep.reward, 0)

    walker_pos = env.physics.bind(walker.root_body).xpos
    walker.set_pose(
        env.physics,
        position=[target_position[0], target_position[1], walker_pos[2]])
    env.physics.forward()

    # Receive reward while the agent remains at that location.
    for _ in range(steps_before_moving_target):
      timestep = env.step(zero_action)
      self.assertEqual(timestep.reward, 1)
      np.testing.assert_array_equal(target_position,
                                    task.target_position(env.physics))

    # After taking > steps_before_moving_target, the target should move and
    # reward should be 0.
    timestep = env.step(zero_action)
    self.assertEqual(timestep.reward, 0)
```
```

### dm_control/locomotion/tasks/random_goal_maze.py

```
"""A task consisting of finding goals/targets in a random maze."""
class NullGoalMaze(Task)
    """A base task for maze with goals."""
    def __init__(self, walker, maze_arena, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, aliveness_threshold, contact_termination, enable_global_task_observables, physics_timestep, control_timestep)
    def task_observables(self)
    def name(self)
    def root_entity(self)
    def initialize_episode_mjcf(self, unused_random_state)
    def _respawn(self, physics, random_state)
    def initialize_episode(self, physics, random_state)
    def _is_disallowed_contact(self, contact)
    def after_step(self, physics, random_state)
    def should_terminate_episode(self, physics)
    def get_reward(self, physics)
    def get_discount(self, physics)
class RepeatSingleGoalMaze(NullGoalMaze)
    """Requires an agent to repeatedly find the same goal in a maze."""
    def __init__(self, walker, maze_arena, target, target_reward_scale, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, aliveness_threshold, contact_termination, max_repeats, enable_global_task_observables, physics_timestep, control_timestep, regenerate_maze_on_repeat)
    def initialize_episode_mjcf(self, random_state)
    def initialize_episode(self, physics, random_state)
    def after_step(self, physics, random_state)
    def should_terminate_episode(self, physics)
    def get_reward(self, physics)
class ManyHeterogeneousGoalsMaze(NullGoalMaze)
    """Requires an agent to find multiple goals with different rewards."""
    def __init__(self, walker, maze_arena, target_builders, target_type_rewards, target_type_proportions, shuffle_target_builders, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, aliveness_threshold, contact_termination, physics_timestep, control_timestep)
    def _get_targets(self, total_target_count, random_state)
    def initialize_episode_mjcf(self, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)
class ManyGoalsMaze(ManyHeterogeneousGoalsMaze)
    """Requires an agent to find all goals in a random maze."""
    def __init__(self, walker, maze_arena, target_builder, target_reward_scale, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, aliveness_threshold, contact_termination, physics_timestep, control_timestep)
class RepeatSingleGoalMazeAugmentedWithTargets(RepeatSingleGoalMaze)
    """Augments the single goal maze with many lower reward targets."""
    def __init__(self, walker, main_target, maze_arena, num_subtargets, target_reward_scale, subtarget_reward_scale, subtarget_colors, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, aliveness_threshold, contact_termination, physics_timestep, control_timestep)
    def initialize_episode_mjcf(self, random_state)
    def get_reward(self, physics)
    def should_terminate_episode(self, physics)

```python
def get_reward(self, physics):
    del physics
    return self._aliveness_reward
```

```python
def get_reward(self, physics):
    del physics
    if self._rewarded_this_step:
      target_reward = self._target_reward_scale
    else:
      target_reward = 0.0
    return target_reward + self._aliveness_reward
```

```python
def get_reward(self, physics):
    del physics
    reward = self._aliveness_reward
    for target_type, targets in enumerate(self._active_targets):
      for i, target in enumerate(targets):
        if target.activated and not self._target_rewarded[target_type][i]:
          reward += self._target_type_rewards[target_type]
          self._target_rewarded[target_type][i] = True
    return reward
```

```python
def get_reward(self, physics):
    main_reward = super(RepeatSingleGoalMazeAugmentedWithTargets,
                        self).get_reward(physics)
    subtarget_reward = 0
    for i, subtarget in enumerate(self._subtargets):
      if subtarget.activated and not self._subtarget_rewarded[i]:
        subtarget_reward += 1
        self._subtarget_rewarded[i] = True
    subtarget_reward *= self._subtarget_reward_scale
    return main_reward + subtarget_reward
```
```

### dm_control/locomotion/tasks/random_goal_maze_test.py

```
"""Tests for locomotion.tasks.random_goal_maze."""
class RandomGoalMazeTest(TestCase)
    def test_observables(self)
    def test_termination_and_discount(self)
```

### dm_control/locomotion/tasks/reach.py

```
"""A (visuomotor) task consisting of reaching to targets for reward."""
class TwoTouchState(IntEnum)
class TwoTouch(Task)
    """Task with target to tap with short delay (for Rat)."""
    def __init__(self, walker, arena, target_builders, target_type_rewards, shuffle_target_builders, randomize_spawn_position, randomize_spawn_rotation, rotation_bias_factor, aliveness_reward, touch_interval, interval_tolerance, failure_timeout, reset_delay, z_height, target_area, physics_timestep, control_timestep)
    def _get_targets(self, total_target_count, random_state)
    def name(self)
    def task_observables(self)
    def root_entity(self)
    def _randomize_targets(self, physics, random_state)
    def initialize_episode_mjcf(self, random_state)
    def _respawn_walker(self, physics, random_state)
    def initialize_episode(self, physics, random_state)
    def before_step(self, physics, action, random_state)
    def should_terminate_episode(self, physics)
    def get_reward(self, physics)
    def get_discount(self, physics)

```python
def get_reward(self, physics):
    reward = self._aliveness_reward
    lhand_pos = physics.bind(self._lhand_body).xpos
    rhand_pos = physics.bind(self._rhand_body).xpos
    target_pos = physics.bind(self._targets[0][0].geom).xpos
    lhand_rew = np.exp(-3.*sum(np.abs(lhand_pos-target_pos)))
    rhand_rew = np.exp(-3.*sum(np.abs(rhand_pos-target_pos)))
    closeness_reward = np.maximum(lhand_rew, rhand_rew)
    reward += .01*closeness_reward*self._target_type_rewards[0]
    if self._state_logic == TwoTouchState.PRE_TOUCH:
      # touch the first time
      for target_type, targets in enumerate(self._targets):
        for i, target in enumerate(targets):
          if (target.activated[0] and
              not self._target_rewarded_once[target_type][i]):
            self._first_touch_time = physics.time()
            self._state_logic = TwoTouchState.TOUCHED_ONCE
            self._target_rewarded_once[target_type][i] = True
            reward += self._target_type_rewards[target_type]
    elif self._state_logic == TwoTouchState.TOUCHED_ONCE:
      for target_type, targets in enumerate(self._targets):
        for i, target in enumerate(targets):
          if (target.activated[1] and
              not self._target_rewarded_twice[target_type][i]):
            self._second_touch_time = physics.time()
            self._state_logic = TwoTouchState.TOUCHED_TWICE
            self._target_rewarded_twice[target_type][i] = True
            # check if touched too soon
            if ((self._second_touch_time - self._first_touch_time) <
                (self._touch_interval - self._interval_tolerance)):
              self._do_time_out = True
              self._state_logic = TwoTouchState.TOUCHED_TOO_SOON
            # check if touched at correct time
            elif ((self._second_touch_time - self._first_touch_time) <=
                  (self._touch_interval + self._interval_tolerance)):
              reward += self._target_type_rewards[target_type]
      # check if no second touch within time interval
      if ((physics.time() - self._first_touch_time) >
          (self._touch_interval + self._interval_tolerance)):
        self._do_time_out = True
        self._state_logic = TwoTouchState.NO_SECOND_TOUCH
        self._second_touch_time = physics.time()
    elif (self._state_logic == TwoTouchState.TOUCHED_TWICE or
          self._state_logic == TwoTouchState.TOUCHED_TOO_SOON or
          self._state_logic == TwoTouchState.NO_SECOND_TOUCH):
      # hold here due to timeout
      if self._do_time_out:
        if physics.time() > (self._second_touch_time + self._failure_timeout):
          self._do_time_out = False
      # reset/re-randomize
      elif physics.time() > (self._second_touch_time + self._reset_delay):
        self._must_randomize_targets = True
    return reward
```
```

### dm_control/locomotion/tasks/reach_test.py

```
"""Tests for locomotion.tasks.reach."""
class ReachTest(TestCase)
    def test_observables(self)
```

### dm_control/locomotion/tasks/reference_pose/__init__.py

```
"""Reference pose tasks in the Locomotion library."""
```

### dm_control/locomotion/tasks/reference_pose/cmu_subsets.py

```
"""Subsets of the CMU mocap database."""
```

### dm_control/locomotion/tasks/reference_pose/datasets.py

```
"""Datasets for reference pose tasks."""
```

### dm_control/locomotion/tasks/reference_pose/mocap_playback.py

```
"""Simple script to visualize motion capture data."""
def mocap_playback_env(random_state)
def main(unused_argv)
```

### dm_control/locomotion/tasks/reference_pose/rewards.py

```
"""Define reward function options for reference pose tasks."""
def bounded_quat_dist(source, target)
def sort_dict(d)
def compute_squared_differences(walker_features, reference_features, exclude_keys)
def termination_reward_fn(termination_error, termination_error_threshold)
def debug(reference_features, walker_features)
def multi_term_pose_reward_fn(walker_features, reference_features)
def comic_reward_fn(termination_error, termination_error_threshold, walker_features, reference_features)
def get_reward(reward_key)
def get_reward_channels(reward_key)

```python
def termination_reward_fn(termination_error, termination_error_threshold,
                          **unused_kwargs):
  """Termination error.

  This reward is intended to be used in conjunction with the termination error
  calculated in the task. Due to terminations if error > error_threshold this
  reward will be in [0, 1].

  Args:
    termination_error: termination error computed in tracking task
    termination_error_threshold: task termination threshold
    unused_kwargs: unused_kwargs

  Returns:
    RewardFnOutput tuple containing reward, debug information and reward terms.
  """
  debug_terms = {
      'termination_error': termination_error,
      'termination_error_threshold': termination_error_threshold
  }
  termination_reward = 1 - termination_error / termination_error_threshold
  return RewardFnOutput(reward=termination_reward, debug=debug_terms,
                        reward_terms=sort_dict(
                            {'termination': termination_reward}))
```

```python
def multi_term_pose_reward_fn(walker_features, reference_features,
                              **unused_kwargs):
  """A reward based on com, body quaternions, joints velocities & appendages."""
  differences = compute_squared_differences(walker_features, reference_features)
  com = .1 * np.exp(-10 * differences['center_of_mass'])
  joints_velocity = 1.0 * np.exp(-0.1 * differences['joints_velocity'])
  appendages = 0.15 * np.exp(-40. * differences['appendages'])
  body_quaternions = 0.65 * np.exp(-2 * differences['body_quaternions'])
  terms = {
      'center_of_mass': com,
      'joints_velocity': joints_velocity,
      'appendages': appendages,
      'body_quaternions': body_quaternions
  }
  reward = sum(terms.values())
  return RewardFnOutput(reward=reward, debug=terms,
                        reward_terms=sort_dict(terms))
```

```python
def comic_reward_fn(termination_error, termination_error_threshold,
                    walker_features, reference_features, **unused_kwargs):
  """A reward that mixes the termination_reward and multi_term_pose_reward.

  This reward function was used in
    Hasenclever et al.,
    CoMic: Complementary Task Learning & Mimicry for Reusable Skills,
    International Conference on Machine Learning, 2020.
    [https://proceedings.icml.cc/static/paper_files/icml/2020/5013-Paper.pdf]

  Args:
    termination_error: termination error as described
    termination_error_threshold: threshold to determine whether to terminate
      episodes. The threshold is used to construct a reward between [0, 1]
      based on the termination error.
    walker_features: Current features of the walker
    reference_features: features of the current reference pose
    unused_kwargs: unused addtional keyword arguments.

  Returns:
    RewardFnOutput tuple containing reward, debug terms and reward terms.
  """
  termination_reward, debug_terms, termination_reward_terms = (
      termination_reward_fn(termination_error, termination_error_threshold))
  mt_reward, mt_debug_terms, mt_reward_terms = multi_term_pose_reward_fn(
      walker_features, reference_features)
  debug_terms.update(mt_debug_terms)
  reward_terms = {k: 0.5 * v for k, v in termination_reward_terms.items()}
  reward_terms.update(
      {k: 0.5 * v for k, v in mt_reward_terms.items()})
  return RewardFnOutput(
      reward=0.5 * termination_reward + 0.5 * mt_reward,
      debug=debug_terms,
      reward_terms=sort_dict(reward_terms))
```

```python
def get_reward(reward_key):
  if reward_key not in _REWARD_FN:
    raise ValueError('Requested loss %s, which is not a valid option.' %
                     reward_key)

  return _REWARD_FN[reward_key]
```

```python
def get_reward_channels(reward_key):
  if reward_key not in _REWARD_CHANNELS:
    raise ValueError('Requested loss %s, which is not a valid option.' %
                     reward_key)

  return _REWARD_CHANNELS[reward_key]
```
```

### dm_control/locomotion/tasks/reference_pose/rewards_test.py

```
"""Tests for dm_control.locomotion.tasks.reference_pose.rewards."""
class RewardsTest(TestCase)
    def test_compute_squared_differences(self)
    def test_compute_squared_differences_exclude_keys(self)
    def test_compute_squared_differences_quaternion(self)
```

### dm_control/locomotion/tasks/reference_pose/tracking.py

```
"""Tasks for multi-clip mocap tracking with RL."""
def _strip_reference_prefix(dictionary, prefix, keep_prefixes)
class ReferencePosesTask(Task)
    """Abstract base class for task that uses reference data."""
    def __init__(self, walker, arena, ref_path, ref_steps, dataset, termination_error_threshold, prop_termination_error_threshold, min_steps, reward_type, physics_timestep, always_init_at_clip_start, proto_modifier, prop_factory, disable_props, ghost_offset, body_error_multiplier, actuator_force_coeff, enabled_reference_observables)
    def _strip_reference_prefix(self)
    def _ghost_prop_factory(self, prop_proto, priority_friction)
    def _load_reference_data(self, ref_path, proto_modifier, dataset)
    def _add_observables(self, enabled_reference_observables)
    def _get_possible_starts(self)
    def initialize_episode_mjcf(self, random_state)
    def _get_clip_to_track(self, random_state)
    def initialize_episode(self, physics, random_state)
    def _reset_reward_channels(self)
    def _compute_termination_error(self)
    def before_step(self, physics, action, random_state)
    def after_step(self, physics, random_state)
    def after_compile(self, physics, random_state)
    def should_terminate_episode(self, physics)
    def get_discount(self, physics)
    def get_reference_rel_joints(self, physics)
    def get_reference_rel_bodies_pos_global(self, physics)
    def get_reference_rel_bodies_quats(self, physics)
    def get_reference_rel_bodies_pos_local(self, physics)
    def get_reference_ego_bodies_quats(self, unused_physics)
    def get_reference_rel_root_quat(self, physics)
    def get_reference_appendages_pos(self, physics)
    def get_reference_rel_root_pos_local(self, physics)
    def get_reference_props_pos_global(self, physics)
    def get_reference_props_quat_global(self, physics)
    def get_veloc_control(self, physics)
    def get_gyro_control(self, physics)
    def get_joints_vel_control(self, physics)
    def get_clip_id(self, physics)
    def get_all_reference_observations(self, physics)
    def get_reward(self, physics)
    def _set_walker(self, physics)
    def _update_ghost(self, physics)
    def action_spec(self, physics)
    def name(self)
    def root_entity(self)
class MultiClipMocapTracking(ReferencePosesTask)
    """Task for multi-clip mocap tracking."""
    def __init__(self, walker, arena, ref_path, ref_steps, dataset, termination_error_threshold, prop_termination_error_threshold, min_steps, reward_type, physics_timestep, always_init_at_clip_start, proto_modifier, prop_factory, disable_props, ghost_offset, body_error_multiplier, actuator_force_coeff, enabled_reference_observables)
    def after_step(self, physics, random_state)
    def get_normalized_time_in_clip(self, physics)
    def name(self)
class PlaybackTask(ReferencePosesTask)
    """Simple task to visualize mocap data."""
    def __init__(self, walker, arena, ref_path, dataset, proto_modifier, physics_timestep)
    def _get_clip_to_track(self, random_state)
    def _set_walker(self, physics)
    def after_step(self, physics, random_state)
    def get_reward(self, physics)
    def name(self)

```python
def _reset_reward_channels(self):
    if self._reward_keys:
      self.last_reward_channels = collections.OrderedDict([
          (k, 0.0) for k in self._reward_keys
      ])
    else:
      self.last_reward_channels = None
```

```python
def get_all_reference_observations(self, physics: 'mjcf.Physics'):
    reference_observations = dict()
    reference_observations[
        'walker/reference_rel_bodies_pos_local'] = self.get_reference_rel_bodies_pos_local(
            physics)
    reference_observations[
        'walker/reference_rel_joints'] = self.get_reference_rel_joints(physics)
    reference_observations[
        'walker/reference_rel_bodies_pos_global'] = self.get_reference_rel_bodies_pos_global(
            physics)
    reference_observations[
        'walker/reference_ego_bodies_quats'] = self.get_reference_ego_bodies_quats(
            physics)
    reference_observations[
        'walker/reference_rel_root_quat'] = self.get_reference_rel_root_quat(
            physics)
    reference_observations[
        'walker/reference_rel_bodies_quats'] = self.get_reference_rel_bodies_quats(
            physics)
    reference_observations[
        'walker/reference_rel_root_pos_local'] = self.get_reference_rel_root_pos_local(
            physics)
    if self._props:
      reference_observations[
          'props/reference_pos_global'] = self.get_reference_props_pos_global(
              physics)
      reference_observations[
          'props/reference_quat_global'] = self.get_reference_props_quat_global(
              physics)
    return reference_observations
```

```python
def get_reward(self, physics: 'mjcf.Physics') -> float:
    reward, unused_debug_outputs, reward_channels = self._reward_fn(
        termination_error=self._termination_error,
        termination_error_threshold=self._termination_error_threshold,
        reference_features=self._current_reference_features,
        walker_features=self._walker_features,
        reference_observations=self._reference_observations)

    if 'actuator_force' in self._reward_keys:
      reward_channels['actuator_force'] = -self._actuator_force_coeff*np.mean(
          np.square(self._walker.actuator_force(physics)))

    self._should_truncate = self._termination_error > self._termination_error_threshold

    if self._props:
      prop_termination = self._prop_termination_error > self._prop_termination_error_threshold
      self._should_truncate = self._should_truncate or prop_termination

    self.last_reward_channels = reward_channels
    return reward
```

```python
def get_reward(self, physics):
    return 0.0
```
```

### dm_control/locomotion/tasks/reference_pose/tracking_test.py

```
"""Tests for mocap tracking."""
class MultiClipMocapTrackingTest(TestCase)
    def setUp(self)
    def test_initialization_and_step(self, reward)
    def test_clip_weights(self, clip_number)
    def test_task_validation(self, clip_start_steps, clip_end_steps, clip_weights)
    def test_init_at_clip_start(self)
    def test_failure_with_wrong_walker(self)
    def test_enabled_reference_observables(self)
    def test_prop_factory(self)
    def test_ghost_prop(self)
    def test_disable_props(self)
    def test_prop_termination(self)
    def test_ghost_walker(self)
```

### dm_control/locomotion/tasks/reference_pose/types.py

```
"""Types for reference pose tasks."""
class ClipCollection()
    """Dataclass representing a collection of mocap reference clips."""
    def __init__(self, ids, start_steps, end_steps, weights)
```

### dm_control/locomotion/tasks/reference_pose/utils.py

```
"""Utils for reference pose tasks."""
def add_walker(walker_fn, arena, name, ghost, visible, position)
def get_qpos_qvel_from_features(features)
def set_walker_from_features(physics, walker, features, offset)
def set_walker(physics, walker, qpos, qvel, offset, null_xyz_and_yaw, position_shift, rotation_shift)
def set_props_from_features(physics, props, features, z_offset)
def get_features(physics, walker, props)
```

### dm_control/manipulation/shared/observations.py

```
"""Shared configuration options for observations."""
class ObservableSpec(?)
    """Configuration options for generic observables."""
class CameraObservableSpec(?)
    """Configuration options for camera observables."""
class ObservationSettings(?)
    """Container of `ObservableSpecs` grouped by category."""
class ObservableNames(?)
    """Container that groups the names of observables by category."""
    def __new__(cls, proprio, ftt, prop_pose, camera)
def make_options(obs_settings, obs_names)
```

### dm_control/suite/wrappers/action_noise.py

```
"""Wrapper control suite environments that adds Gaussian noise to actions."""
class Wrapper(Environment)
    """Wraps a control environment and adds Gaussian noise to actions."""
    def __init__(self, env, scale)
    def step(self, action)
    def reset(self)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)

```python
def observation_spec(self):
    return self._env.observation_spec()
```
```

### dm_control/suite/wrappers/action_noise_test.py

```
"""Tests for the action noise wrapper."""
class ActionNoiseTest(TestCase)
    def make_action_spec(self, lower, upper)
    def make_mock_env(self, action_spec)
    def assertStepCalledOnceWithCorrectAction(self, env, expected_action)
    def test_step(self, lower, upper, scale)
    def test_action_clipping(self, action, noise)
    def test_error_if_action_bounds_non_finite(self, lower, upper)
    def test_reset(self)
    def test_observation_spec(self)
    def test_action_spec(self)
    def test_getattr(self, attribute_name)

```python
def test_observation_spec(self):
    env = self.make_mock_env()
    wrapped_env = action_noise.Wrapper(env)
    observation_spec = wrapped_env.observation_spec()
    env.observation_spec.assert_called_once_with()
    self.assertIs(observation_spec, env.observation_spec())
```
```

### dm_control/suite/wrappers/action_scale.py

```
"""Wrapper that scales actions to a specific range."""
class Wrapper(Environment)
    """Wraps a control environment to rescale actions to a specific range."""
    def __init__(self, env, minimum, maximum)
    def step(self, action)
    def reset(self)
    def observation_spec(self)
    def action_spec(self)
    def __getattr__(self, name)

```python
def observation_spec(self):
    return self._env.observation_spec()
```
```

### dm_control/suite/wrappers/action_scale_test.py

```
"""Tests for the action scale wrapper."""
def make_action_spec(lower, upper)
def make_mock_env(action_spec)
class ActionScaleTest(TestCase)
    def assertStepCalledOnceWithCorrectAction(self, env, expected_action)
    def test_step(self, minimum, maximum, scaled_minimum, scaled_maximum)
    def test_correct_action_spec(self, minimum, maximum)
    def test_method_delegated_to_underlying_env(self, method_name)
    def test_invalid_action_spec_type(self)
    def test_non_finite_bounds(self, name, bounds)
    def test_invalid_bounds_shape(self, name, bounds)
```

### dm_control/utils/rewards.py

```
"""Soft indicator function evaluating whether a number is within bounds."""
def _sigmoids(x, value_at_1, sigmoid)
def tolerance(x, bounds, margin, sigmoid, value_at_margin)
```

### dm_control/utils/rewards_test.py

```
"""Tests for dm_control.utils.rewards."""
class ToleranceTest(TestCase)
    def test_tolerance_sigmoid_parameterisation(self, margin, value_at_margin)
    def test_tolerance_sigmoids(self, sigmoid)
    def test_tolerance_margin_loss_shape(self, x, expected)
    def test_tolerance_vectorization(self)
    def test_tolerance_bounds(self, x, bounds, expected)
    def test_tolerance_incorrect_bounds_order(self)
    def test_tolerance_negative_margin(self)
    def test_tolerance_bad_value_at_margin(self)
    def test_tolerance_unknown_sigmoid(self)
```