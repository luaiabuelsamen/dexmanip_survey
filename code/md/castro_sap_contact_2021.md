# castro_sap_contact_2021

source: https://github.com/RobotLocomotion/drake


commit: 5a73436cd6941519684786d409c67ce25ce16305


## README

# Drake

Model-Based Design and Verification for Robotics.

Please see the [Drake Documentation](https://drake.mit.edu) for more
information.


## File tree (depth 3, assets pruned)

```
.bazelignore
.bazeliskrc
.bazelproject
.bazelrc
.bazelversion
.clang-format
.clang-tidy
.drake-find_resource-sentinel
.editorconfig
.gitattributes
.github/
  ISSUE_TEMPLATE/
    BUG.yml
    POST_RELEASE_ACTIONS.yml
    config.yml
    feature_request.md
  renovate.json
  workflows/
    stale.yml
.gitignore
.jenkins/
  Jenkinsfile-experimental
  Jenkinsfile-external-examples
  Jenkinsfile-production
  Jenkinsfile-staging
.ruff.toml
BUILD.bazel
CMakeLists.txt
CONTRIBUTING.md
CPPLINT.cfg
CTestConfig.cmake
CTestCustom.cmake.in
LICENSE.TXT
MODULE.bazel
README.md
WORKSPACE
__init__.py
bindings/
  BUILD.bazel
  generated_docstrings/
    BUILD.bazel
    README.md
    common.h
    common_schema.h
    common_symbolic.h
    common_symbolic_expression.h
    common_trajectories.h
    examples_acrobot.h
    examples_compass_gait.h
    examples_pendulum.h
    examples_quadrotor.h
    examples_rimless_wheel.h
    examples_van_der_pol.h
    geometry.h
    geometry_optimization.h
    geometry_proximity.h
    geometry_query_results.h
    geometry_render.h
    geometry_render_gl.h
    geometry_render_gltf_client.h
    geometry_render_vtk.h
    lcm.h
    manipulation_franka_panda.h
    manipulation_kuka_iiwa.h
    manipulation_schunk_wsg.h
    manipulation_util.h
    math.h
    multibody_benchmarks_acrobot.h
    multibody_benchmarks_free_body.h
    multibody_benchmarks_inclined_plane.h
    multibody_benchmarks_kuka_iiwa_robot.h
    multibody_benchmarks_mass_damper_spring.h
    multibody_benchmarks_pendulum.h
    multibody_cenic.h
    multibody_contact_solvers_icf.h
    multibody_fem.h
    multibody_inverse_kinematics.h
    multibody_math.h
    multibody_meshcat.h
    multibody_optimization.h
    multibody_parsing.h
    multibody_plant.h
    multibody_rational.h
    multibody_tree.h
    perception.h
    planning.h
    planning_experimental.h
    planning_graph_algorithms.h
    planning_iris.h
    planning_locomotion.h
    planning_trajectory_optimization.h
    solvers.h
    systems_analysis.h
    systems_controllers.h
    systems_estimators.h
    systems_framework.h
    systems_lcm.h
    systems_optimization.h
    systems_primitives.h
    systems_rendering.h
    systems_sensors.h
    test/
    tools/
    visualization.h
  pydrake/
    .clang-format
    BUILD.bazel
    CPPLINT.cfg
    __init__.py
    _all_everything.py
    _lcm_extra.py
    _trajectories_extra.py
    all.py
    autodiff_types_pybind.h
    autodiffutils/
    common/
    examples/
    forwarddiff.py
    geometry/
    gym/
    lcm_py.cc
    manipulation/
    math/
    math_operators_pybind.h
    multibody/
    numpy_object_pybind.h
    perception_py.cc
    planning/
    polynomial_py.cc
    polynomial_types_pybind.h
    pydrake.bzl
    pydrake_doxygen.h
    pydrake_pybind.h
    reference_wrapper_pybind.h
    solvers/
    stubgen.bzl
    stubgen.py
    symbolic/
    symbolic_types_pybind.h
    systems/
    test/
    trajectories_py.cc
    tutorials.py
    visualization/
cmake/
  BUILD.bazel.in
  MODULE.bazel.in
  bazel.rc.in
  external/
    workspace/
  modules/
    FindBazel.cmake
    FindGurobi.cmake
common/
  BUILD.bazel
  README.md
  ad/
    BUILD.bazel
    README.md
    auto_diff.h
    internal/
    test/
  add_text_logging_gflags.cc
  atomic_shared_ptr.h
  autodiff.h
  benchmarking/
    BUILD.bazel
    autodiff.cc
    benchmark_polynomial.cc
  cond.cc
  cond.h
  constants.h
  copyable_unique_ptr.h
  cpu_capabilities.cc
  cpu_capabilities.h
  cxx_doxygen.h
  default_scalars.h
  diagnostic_policy.cc
  diagnostic_policy.h
  double_overloads.cc
  double_overloads.h
  drake_assert.cc
  drake_assert.h
  drake_assertion_error.h
  drake_bool.h
  drake_copyable.h
  drake_deprecated.cc
  drake_deprecated.h
  drake_export.h
  drake_marker.cc
  drake_marker.h
  drake_path.cc
  drake_path.h
  drake_throw.h
  dummy_value.h
  eigen_types.h
  extract_double.h
  file_source.h
  find_cache.cc
  find_cache.h
  find_loaded_library.cc
  find_loaded_library.h
  find_resource.cc
  find_resource.h
  find_runfiles.cc
  find_runfiles.h
  find_runfiles_stub.cc
  fmt.cc
  fmt.h
  fmt_eigen.cc
  fmt_eigen.h
  hash.cc
  hash.h
  hwy_dynamic.cc
  hwy_dynamic.h
  hwy_dynamic_impl.h
  identifier.cc
  identifier.h
  is_approx_equal_abstol.h
  is_cloneable.h
  is_less_than_comparable.h
  memory_file.cc
  memory_file.h
  name_value.h
  network_policy.cc
  network_policy.h
  never_destroyed.h
  nice_type_name.cc
  nice_type_name.h
  nice_type_name_override.cc
  nice_type_name_override.h
  overloaded.h
  parallelism.cc
  parallelism.h
  pointer_cast.cc
  pointer_cast.h
  polynomial.cc
  polynomial.h
  proto/
    BUILD.bazel
    call_python.cc
    call_python.h
    call_python_client.py
    call_python_client_notebook.ipynb
    rpc_pipe_temp_directory.cc
    rpc_pipe_temp_directory.h
    test/
  random.cc
  random.h
  ranges.h
  reset_after_move.h
  reset_on_copy.h
  schema/
    BUILD.bazel
    rotation.cc
    rotation.h
    stochastic.cc
    stochastic.h
    test/
    transform.cc
    transform.h
  scope_exit.h
  scoped_singleton.h
  sha256.cc
  sha256.h
  sorted_pair.cc
  sorted_pair.h
  string_hash.h
  string_map.h
  string_set.h
  string_unordered_map.h
  string_unordered_set.h
  symbolic/
    BUILD.bazel
    chebyshev_basis_element.cc
    chebyshev_basis_element.h
    chebyshev_polynomial.cc
    chebyshev_polynomial.h
    codegen.cc
    codegen.h
    decompose.cc
    decompose.h
    expression/
    expression.h
    generic_polynomial.cc
    generic_polynomial.h
    latex.cc
    latex.h
    monomial.cc
    monomial.h
    monomial_basis_element.cc
    monomial_basis_element.h
    monomial_util.cc
    monomial_util.h
    polynomial.cc
    polynomial.h
    polynomial_basis.h
    polynomial_basis_element.cc
    polynomial_basis_element.h
    rational_function.cc
    rational_function.h
    replace_bilinear_terms.cc
    replace_bilinear_terms.h
    simplification.cc
    simplification.h
    test/
    trigonometric_polynomial.cc
    trigonometric_polynomial.h
  temp_directory.cc
  temp_directory.h
  test/
    atomic_shared_ptr_test.cc
    autodiff_overloads_test.cc
    autodiffxd_heap_test.cc
    cond_test.cc
    copyable_unique_ptr_test.cc
    cpu_capabilities_test.py
    cpu_capabilities_test_device.cc
    diagnostic_policy_test.cc
    double_overloads_test.cc
    drake_assert_test.cc
    drake_bool_test.cc
    drake_cc_googletest_main_test.py
    drake_cc_googletest_main_test_device.cc
    drake_copyable_test.cc
    drake_deprecated_test.cc
    drake_deref_test.cc
    drake_throw_test.cc
    dummy_value_test.cc
    eigen_autodiff_types_test.cc
    eigen_types_test.cc
    extract_double_test.cc
    file_source_test.cc
    find_cache_test.cc
    find_loaded_library_test.cc
    find_resource_test.cc
    find_resource_test_data.txt
    find_runfiles_fail_test.cc
    find_runfiles_stub_test.cc
    find_runfiles_subprocess_test.py
    find_runfiles_test.cc
    fmt_eigen_test.cc
    fmt_test.cc
    hash_test.cc
    hwy_dynamic_test.cc
    hwy_dynamic_test_array_mul.cc
    hwy_dynamic_test_array_mul.h
    identifier_test.cc
    is_approx_equal_abstol_test.cc
    is_cloneable_test.cc
    is_less_than_comparable_test.cc
    lib_is_real.cc
    memory_file_test.cc
    name_value_test.cc
    network_policy_test.cc
    never_destroyed_test.cc
    nice_type_name_test.cc
    openmp_test.cc
    overloaded_test.cc
    parallelism_test.cc
    pointer_cast_test.cc
    polynomial_test.cc
    random_test.cc
    reset_after_move_test.cc
    reset_on_copy_test.cc
    scalar_casting_test.cc
    scope_exit_test.cc
    scoped_singleton_test.cc
    sha256_test.cc
    sorted_pair_test.cc
    string_container_test.cc
    temp_directory_test.cc
    text_logging_ostream_test.cc
    text_logging_spdlog_test.cc
    text_logging_test.cc
    timer_test.cc
    type_safe_index_test.cc
    value_test.cc
  test_utilities/
    BUILD.bazel
    diagnostic_policy_test_base.cc
    diagnostic_policy_test_base.h
    disable_python_unittest/
    drake_cc_googletest_main.cc
    drake_py_unittest_main.py
    eigen_matrix_compare.h
    eigen_printer.h
    expect_no_throw.h
    expect_throws_message.h
    fmt_format_printer.h
    is_dynamic_castable.h
    is_memcpy_movable.h
    limit_malloc.cc
    limit_malloc.h
    maybe_pause_for_user.cc
    maybe_pause_for_user.h
    measure_execution.h
    random_polynomial_matrix.h
    set_env.h
    symbolic_test_util.h
    test/
  text_logging.cc
  text_logging.h
  text_logging_impl_none.cc
  text_logging_impl_spdlog.cc
  text_logging_impl_spdlog.h
  text_logging_level.h
  text_logging_spdlog.cc
  text_logging_spdlog.h
  timer.cc
  timer.h
  trajectories/
    BUILD.bazel
    bezier_curve.cc
    bezier_curve.h
    bspline_trajectory.cc
    bspline_trajectory.h
    composite_trajectory.cc
    composite_trajectory.h
    derivative_trajectory.cc
    derivative_trajectory.h
    discrete_time_trajectory.cc
    discrete_time_trajectory.h
    exponential_plus_piecewise_polynomial.cc
    exponential_plus_piecewise_polynomial.h
    function_handle_trajectory.cc
    function_handle_trajectory.h
    path_parameterized_trajectory.cc
    path_parameterized_trajectory.h
    piecewise_constant_curvature_trajectory.cc
    piecewise_constant_curvature_trajectory.h
    piecewise_polynomial.cc
    piecewise_polynomial.h
    piecewise_pose.cc
    piecewise_pose.h
    piecewise_quaternion.cc
    piecewise_quaternion.h
    piecewise_trajectory.cc
    piecewise_trajectory.h
    stacked_trajectory.cc
    stacked_trajectory.h
    test/
    trajectory.cc
    trajectory.h
    wrapped_trajectory.cc
    wrapped_trajectory.h
  type_safe_index.cc
  type_safe_index.h
  unused.h
  value.cc
  value.h
  yaml/
    BUILD.bazel
    test/
    yaml_doxygen.h
    yaml_io.cc
    yaml_io.h
    yaml_io_options.cc
    yaml_io_options.h
    yaml_node.cc
    yaml_node.h
    yaml_read_archive.cc
    yaml_read_archive.h
    yaml_write_archive.cc
    yaml_write_archive.h
doc/
  BUILD.bazel
  README.md
  _config.yml
  _includes/
    footer.html
    header.html
    toc.md
    video-autoplay.html
    video.html
  _layouts/
    default.html
    page.html
    page_with_toc.html
    release.html
  _pages/
    apt.md
    bazel.md
    buildcop.md
    clion.md
    code_review_checklist.md
    code_style_guide.md
    code_style_tools.md
    credits.md
    developers.md
    development_on_mac.md
    directory_structure.md
    docker.md
    documentation_instructions.md
    downstream_testing.md
    doxygen_instructions.md
    emacs.md
    from_binary.md
    from_source.md
    gallery.md
    getting_help.md
    installation.md
    issues.md
    jenkins.md
    julia_bindings.md
    mac.md
    model_version_control.md
    no_push_to_origin.md
    pip.md
    platform_reviewer_checklist.md
    profiling.md
    python_bindings.md
    release_playbook.md
    reviewable.md
    rosetta2.md
    sphinx_instructions.md
    stable.md
    sublime_text.md
    tm.md
    troubleshooting.md
    ubuntu.md
    unicode_tips_tricks.md
    unit_testing_instructions.md
    vim.md
    vscode.md
    website_licenses.md
  _release-notes/
    2015.md
    2016.md
    end_of_support.md
    index.html
    release_notes.md
    template.txt
    v0.10.0.md
    v0.11.0.md
    v0.12.0.md
    v0.13.0.md
    v0.14.0.md
    v0.15.0.md
    v0.16.0.md
    v0.16.1.md
    v0.17.0.md
    v0.18.0.md
    v0.19.0.md
    v0.20.0.md
    v0.21.0.md
    v0.22.0.md
    v0.23.0.md
    v0.24.0.md
    v0.25.0.md
    v0.26.0.md
    v0.27.0.md
    v0.28.0.md
    v0.29.0.md
    v0.30.0.md
    v0.31.0.md
    v0.32.0.md
    v0.33.0.md
    v0.34.0.md
    v0.35.0.md
    v0.36.0.md
    v0.37.0.md
    v0.38.0.md
    v0.39.0.md
    v1.0.0.md
    v1.1.0.md
    v1.10.0.md
    v1.11.0.md
    v1.12.0.md
    v1.13.0.md
    v1.14.0.md
    v1.15.0.md
    v1.16.0.md
    v1.17.0.md
    v1.18.0.md
    v1.19.0.md
    v1.2.0.md
    v1.20.0.md
    v1.21.0.md
    v1.22.0.md
    v1.23.0.md
    v1.24.0.md
    v1.25.0.md
    v1.26.0.md
    v1.27.0.md
    v1.28.0.md
    v1.29.0.md
    v1.3.0.md
    v1.30.0.md
    v1.31.0.md
    v1.32.0.md
    v1.33.0.md
    v1.34.0.md
    v1.35.0.md
    v1.36.0.md
    v1.37.0.md
    v1.38.0.md
    v1.39.0.md
    v1.4.0.md
    v1.40.0.md
```

## Config files (7)


### .github/ISSUE_TEMPLATE/POST_RELEASE_ACTIONS.yml

```yaml
name: Post-Release Actions
title: Post-release actions for release <version>
description:
  Create a tracking issue for Apt repository updates for a new Drake release.
labels: ["component: distribution"]
projects: ["RobotLocomotion/10"]
assignees: BetsyMcPhail
body:
  - type: input
    id: version
    attributes:
      label: Release Version
      description:
        "Enter the release version number WITHOUT the 'v' prefix (e.g., 1.N.0)."
      placeholder: "1.N.0"
    validations:
      required: true
  - type: textarea
    attributes:
      label: Post-Release Documentation
      value: >

        This issue tracks the required post-release actions that need to be
        completed after the Drake release has been published to GitHub.

        For detailed instructions, refer to the [Apt Release Process](https://github.com/RobotLocomotion/drake/blob/master/tools/release_engineering/README.md).

        To see the build artifacts for the latest Drake release, visit the
        [Drake GitHub Releases page](https://github.com/RobotLocomotion/drake/releases/latest).
  - type: checkboxes
    id: tasks
    attributes:
      label: Post-Release Tasks
      description:
        "Check each box after completion."
      options:
        - label: "Run push_apt script for Apt repository updates"
          required: false

```

### .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: true
contact_links:
  - name: Questions, Requests for Help, Build or Installation Problems, Troubleshooting
    url: https://github.com/RobotLocomotion/drake/discussions/new/choose
    about: Please ask and answer these kinds of questions using Discussions, not Issues.

```

### doc/_config.yml

```yaml
# For more information, see: https://jekyllrb.com/docs/configuration/

url: "" # the base hostname & protocol for the site
baseurl: "" # the subpath of the site
title: Drake

# Tell Jekyll not to hide release notes based on their date.
future: True

# N.B. Items under this `custom` section are not part of the standard Jekyll
# configuration schema; instead, they are used by the relevant templates.
custom:
  header_logo: /images/drake-logo-white.svg
  footer_logo: /images/drake-logo.svg
  hero_image: /images/drake-dragon.png

  meta:
    author: Drake Developers
    content: |
      Drake ("dragon" in Middle English) is a C++ toolbox started by the Robot
      Locomotion Group at the MIT Computer Science and Artificial Intelligence
      Lab (CSAIL). The development team has now grown significantly, with core
      development led by the Toyota Research Institute. It is a collection of
      tools for analyzing the dynamics of our robots and building control
      systems for them, with a heavy emphasis on optimization-based design/
      analysis.

  header:
    menu_items:
      - title: 'Home'
        url: '/'
      - title: 'Installation'
        subfolderitems:
        - page: 'Overview'
          url: '/installation.html'
        - page: 'Pip'
          url: '/pip.html'
        - page: 'APT'
          url: '/apt.html'
        - page: 'Binary Download'
          url: '/from_binary.html'
        - page: 'Build From Source'
          url: '/from_source.html'
      - title: 'Gallery'
        url: '/gallery.html'
      - title: 'API Documentation'
        subfolderitems:
        - page: 'C++'
          url: /doxygen_cxx/index.html
        - page: 'Python'
          url: /pydrake/index.html
      - title: 'Resources'
        subfolderitems:
        - page: 'Getting Help'
          url: /getting_help.html
        - page: 'Tutorials'
          url: /tutorials/index.html
        - page: 'Troubleshooting'
          url: /troubleshooting.html
        - page: 'Python Bindings'
          url: /python_bindings.html
        - page: 'For Developers'
          url: /developers.html
        - page: 'Credits'
          url: /credits.html

  footer:
    menu_items:
      - title: 'Accessibility'
        url: https://accessibility.mit.edu/
      - title: 'C++'
        url: /doxygen_cxx/index.html
      - title: 'Python'
        url: /pydrake/index.html

# Using `:path` in the permalink allows us to preserve underscores in the
# names, so we have a best-effort backwards-compatibility with the Sphinx URLs.
# (Otherwise, the URL slugs replace `_` with `-`.)
collections:
  # Normal pages, listed at the root.
  pages:
    output: true
    permalink: /:path
  # Release notes, index and listed under `/release_notes`.
  release-notes:
    output: true
    permalink: /release_notes/:path

defaults:
  - scope:
      path: ""
    values:
      layout: "default"
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "page"
  - scope:
      path: ""
      type: "release-notes"
    values:
      layout: "release"

kramdown:
  # https://kramdown.gettalong.org/converter/html.html#options
  auto_ids: true
  toc_levels: [1,2]
  show_warnings: true

liquid:
  # TODO(eric.cousineau): Make these stricter at some point.
  error_mode: warn
  strict_variables: false
  strict_filters: false

```

### doc/styleguide/_config.yml

```yaml
# For more information, see: https://jekyllrb.com/docs/configuration/

title: Google Style Guide for Drake

defaults:
  - scope:
      path: ""
    values:
      layout: "default"

```

### examples/hardware_sim/example_scenarios.yaml

```yaml
# This file is licensed under the MIT-0 License.
# See LICENSE-MIT-0.txt in the current directory.

# This demo simulation shows an IIWA arm with an attached WSG gripper,
# nearby a table with a pepper atop it.
Demo:
  scene_graph_config:
    default_proximity_properties:
      compliance_type: "compliant"
  directives:
  - add_model:
      name: amazon_table
      file: package://drake_models/manipulation_station/amazon_table_simplified.sdf
  - add_weld:
      parent: world
      child: amazon_table::amazon_table
  - add_model:
      name: iiwa
      file: package://drake_models/iiwa_description/urdf/iiwa14_primitive_collision.urdf
      default_joint_positions:
        iiwa_joint_1: [-0.2]
        iiwa_joint_2: [0.79]
        iiwa_joint_3: [0.32]
        iiwa_joint_4: [-1.76]
        iiwa_joint_5: [-0.36]
        iiwa_joint_6: [0.64]
        iiwa_joint_7: [-0.73]
  - add_frame:
      name: iiwa_on_world
      X_PF:
        base_frame: world
        translation: [0, -0.7, 0.1]
        rotation: !Rpy { deg: [0, 0, 90] }
  - add_weld:
      parent: iiwa_on_world
      child: iiwa::base
  - add_model:
      name: wsg
      file: package://drake_models/wsg_50_description/sdf/schunk_wsg_50_with_tip.sdf
  - add_frame:
      name: wsg_on_iiwa
      X_PF:
        base_frame: iiwa_link_7
        translation: [0, 0, 0.114]
        rotation: !Rpy { deg: [90, 0, 90] }
  - add_weld:
      parent: wsg_on_iiwa
      child: wsg::body
  - add_model:
      name: bell_pepper
      file: package://drake_models/veggies/yellow_bell_pepper_no_stem_low.sdf
      default_free_body_pose:
        flush_bottom_center__z_up:
          base_frame: amazon_table::amazon_table
          # We pose the pepper in the air above the table so that it won't start
          # in penetration. After the simulation starts, it will fall and come
          # to rest on the table.
          translation: [0, 0.10, 0.20]
  lcm_buses:
    driver_traffic:
      # Use a non-default LCM url to communicate with the robot.
      lcm_url: udpm://239.241.129.92:20185?ttl=0
  cameras:
    oracular_view:
      name: camera_0
      X_PB:
        translation: [1.5, 0.8, 1.25]
        rotation: !Rpy { deg: [-120, 5, 125] }
  model_drivers:
    iiwa: !IiwaDriver
      hand_model_name: wsg
      lcm_bus: driver_traffic
    wsg: !SchunkWsgDriver
      lcm_bus: driver_traffic
  initial_position:
    # Set an initial position for the gripper. This can also be spelled using
    # default_joint_positions in the add_model directive, but sometimes that is
    # awkward (e.g., if the gripper was in a separate add_directives sub-file).
    wsg:
      left_finger_sliding_joint: [-0.02]
      right_finger_sliding_joint: [0.02]

```

### examples/hardware_sim/test/test_scenarios.yaml

```yaml
# Only ever uses the defaults.
Defaults: {}

# Has at least one example of every kind of top-level option.
# The specific details of the sub-structs are tested elsewhere.
OneOfEverything:
  random_seed: 1
  simulation_duration: 3.14
  simulator_config:
    target_realtime_rate: 5.0
  plant_config:
    stiction_tolerance: 1e-2
  scene_graph_config:
    default_proximity_properties:
      compliance_type: "compliant"
  directives:
  - add_model:
      name: alice
      file: package://drake/examples/pendulum/Pendulum.urdf
  lcm_buses:
    extra_bus: {}
  model_drivers:
    alice: !ZeroForceDriver {}
  cameras:
    arbitrary_camera_name:
      name: camera_0
      lcm_bus: extra_bus
  visualization:
    lcm_bus: extra_bus
    publish_period: 0.125
    default_illustration_color:
      rgba: [0.8, 0.8, 0.8]

```

### manipulation/util/test/panda_arm_and_hand.dmd.yaml

```yaml
directives:
- add_model:
    name: panda
    file: package://drake_models/franka_description/urdf/panda_arm.urdf
- add_weld:
    parent: world
    child: panda::panda_link0
- add_model:
    name: panda_hand
    file: package://drake_models/franka_description/urdf/panda_hand.urdf
- add_weld:
    parent: panda::panda_link8
    child: panda_hand::panda_hand
    X_PC:
      translation: [0, 0, 0]
      rotation: !Rpy { deg: [0, 0, -45] }

```

## Python signatures and reward/observation bodies (20 files)


### bindings/pydrake/examples/gym/envs/cart_pole.py

```
def AddAgent(plant, builder)
def make_sim(meshcat, time_limit, debug, obs_noise, monitoring_camera, add_disturbances)
def reset_handler(simulator, diagram_context, seed)
def info_handler(simulator)
def DrakeCartPoleEnv(meshcat, time_limit, debug, obs_noise, monitoring_camera, add_disturbances)

```python
def CalcReward(self, context, output):
            reward = 1
            output[0] = reward
```
```

### bindings/pydrake/examples/gym/train_cart_pole.py

```
"""Train a policy for //bindings/pydrake/examples/envs:cart_pole"""
def _run_training(config, args)
def _main()
```

### bindings/pydrake/examples/multibody/cart_pole_passive_simulation.py

```
"""Provides an example translation of `cart_pole_passive_simluation.cc`."""
def main()
```

### bindings/pydrake/gym/_drake_gym_env.py

```
def _reached_termination(status)
class DrakeGymEnv(Env)
    """DrakeGymEnv provides a gym.Env interface for a Drake System (often a
Diagram) using a Simulator."""
    def __init__(self, simulator, time_step, action_space, observation_space, reward, action_port_id, observation_port_id, render_rgb_port_id, render_mode, reset_handler, info_handler, hardware)
    def _setup(self)
    def step(self, action)
    def reset(self)
    def render(self)
```

### bindings/pydrake/solvers/test/mixed_integer_rotation_constraint_test.py

```
class TestMixedIntegerRotationConstraint(TestCase)
    def test_MixedIntegerRotationConstraintGenerator(self)
```

### bindings/pydrake/visualization/test/config_test.py

```
class TestConfig(TestCase)
    def test_visualization_config(self)
    def test_apply_visualization_config(self)
    def test_apply_visualization_config_plain(self)
    def test_add_default_visualization(self)
    def test_add_default_visualization_plain(self)
```

### examples/acrobot/spong_sim.py

```
"""A main() program (plus an reusable standalone function) that simulates a
spong-controlled acrobot."""
def simulate()
def main()
```

### examples/acrobot/test/spong_sim_lib_py_test.py

```
class TestSpongControlledAcrobot(TestCase)
    def test_simulate(self)
```

### examples/acrobot/test/spong_sim_main_test.py

```
class TestRunSpongControlledAcrobot(TestCase)
    def setUp(self)
    def test_help(self)
    def test_example_scenario(self)
    def test_stochastic_scenario(self)
```

### examples/allegro_hand/joint_control/test/run_twisting_mug_test.py

```
"""Simple regression test that the twisting_mug demo can perform at least one
twist."""
def _unique_lcm_url(path)
class TestRunTwistingMug(TestCase)
    def _find_resource(self, basename)
    def setUp(self)
    def test_only_sim(self)
    def test_sim_and_control(self)
```

### examples/hardware_sim/hardware_sim.py

```
"""This program serves as an example of a simulator for hardware, i.e., a
simulator for robots that one might have in their lab. There is no controller
built-in to this program -- it merely sends status and sensor messages, and
listens for command messages.

It is intended to operate in the "no ground truth" regime, i.e, the only LCM
messages it knows about are the ones used by the actual hardware. The one
messaging difference from real life is that we emit visualization messages (for
Meldis) so that you can watch a simulation on your screen while some (separate)
controller operates the robot, wi"""
class Scenario()
    """Defines the YAML format for a (possibly stochastic) scenario to be
simulated."""
def _load_scenario()
def run()
def main()
```

### examples/hardware_sim/robot_commander.py

```
"""A simple program to actuate the robot, an IIWA arm and a WSG gripper, with a
cyclic motion."""
def main()
```

### examples/hardware_sim/test/hardware_sim_cc_test.py

```
class HardwareSimCcTest(HardwareSimTest, TestCase)
    """Smoke test for our hardware_sim_cc program.

All of the actual test cases are defined in our base class."""
    def __init__(self)
```

### examples/hardware_sim/test/hardware_sim_py_test.py

```
class HardwareSimPyTest(HardwareSimTest, TestCase)
    """Smoke test for our hardware_sim_py program.

All of the actual test cases are defined in our base class."""
    def __init__(self)
```

### examples/hardware_sim/test/hardware_sim_test_common.py

```
"""This file contains smoke tests for our hardware_sim program and its sample
config files. The tests are reused for both the C++ and Python regression
tests.

Note that this file is only ever imported; it is never run as a unittest
program itself; we'll use wrapper files named hardware_sim_cc_test and
hardware_sim_py_test to actually run it."""
class HardwareSimTest()
    def _find_resource(self, respath)
    def setUp(self)
    def _dict_to_single_line_yaml(self)
    def _run(self, scenario_file, scenario_name, extra, graphviz)
    def test_Defaults(self)
    def test_OneOfEverything(self)
    def test_Demo(self)
    def test_graphviz(self)
```

### examples/hardware_sim/test/robot_commander_test.py

```
class RobotCommanderTest(TestCase)
    def setUp(self)
    def test_scenario_parameters(self)
    def test_smoke(self)
```

### examples/hydroelastic/python_ball_paddle/contact_sim_demo.py

```
"""This is an example for using hydroelastic contact model through pydrake.
It reads two simple SDFormat files of a compliant hydroelastic ball and
a compliant hydroelastic paddle.
The ball is dropped on an edge of the paddle and bounces off."""
def make_ball_paddle(contact_model, contact_surface_representation, time_step)
def simulate_diagram(diagram, ball_paddle_plant, state_logger, ball_init_position, ball_init_velocity, simulation_time, target_realtime_rate)
```

### systems/analysis/test/simulator_gflags_test.py

```
class TestSimulatorGflags(TestCase)
    def setUp(self)
    def test(self)
```

### tools/skylark/py_env_runner.py

```
"""Wrapper Python script to ensure we can execute a C++ binary with access to
Python libraries using an environment established by Bazel."""
```

### tools/workspace/cmake_configure_file.py

```
"""A re-implementation of CMake's configure_file substitution semantics.  This
implementation is incomplete, and may not produce the same result as CMake in
all (or even many) cases.

The CMake documentation of the configure_file macro is:
https://cmake.org/cmake/help/latest/command/configure_file.html"""
def _transform_substitions()
def _transform_cmake()
def _transform_autoconf()
def _extract_definition(line, prior_definitions)
def _setup_definitions(args)
def main()
```