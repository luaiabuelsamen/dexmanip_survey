# mujoco_2012

source: https://github.com/google-deepmind/mujoco


commit: 2fec922375a5e001a4d844c06ebfdb0f5c5e823b


## README

<h1>
  <a href="#"><img alt="MuJoCo" src="banner.png" width="100%"/></a>
</h1>

<p>
  <a href="https://github.com/google-deepmind/mujoco/actions/workflows/build.yml?query=branch%3Amain" alt="GitHub Actions">
    <img src="https://img.shields.io/github/actions/workflow/status/google-deepmind/mujoco/build.yml?branch=main">
  </a>
  <a href="https://mujoco.readthedocs.io/" alt="Documentation">
    <img src="https://readthedocs.org/projects/mujoco/badge/?version=latest">
  </a>
  <a href="https://github.com/google-deepmind/mujoco/blob/main/LICENSE" alt="License">
    <img src="https://img.shields.io/github/license/google-deepmind/mujoco">
  </a>
</p>

**MuJoCo** stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a
general purpose physics engine that aims to facilitate research and development
in robotics, biomechanics, graphics and animation, machine learning, and other
areas which demand fast and accurate simulation of articulated structures
interacting with their environment.

This repository is maintained by [Google DeepMind](https://www.deepmind.com/).

MuJoCo has a C API and is intended for researchers and developers. The runtime
simulation module is tuned to maximize performance and operates on low-level
data structures that are preallocated by the built-in XML compiler. The library
includes interactive visualization with a native GUI, rendered in OpenGL. MuJoCo
further exposes a large number of utility functions for computing
physics-related quantities.

We also provide [Python bindings] and a plug-in for the [Unity] game engine.

## Documentation

MuJoCo's documentation can be found at [mujoco.readthedocs.io]. Upcoming
features due for the next release can be found in the [changelog] in the
"latest" branch.

## Getting Started

There are two easy ways to get started with MuJoCo:

1. **Run `simulate` on your machine.**
[This video](https://www.youtube.com/watch?v=P83tKA1iz2Y) shows a screen capture
of `simulate`, MuJoCo's native interactive viewer. Follow the steps described in
the [Getting Started] section of the documentation to get `simulate` running on
your machine.

2. **Explore our online IPython notebooks.**
If you are a Python user, you might want to start with our tutorial notebooks
running on Google Colab:

 - The **introductory** tutorial teaches MuJoCo basics:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/tutorial.ipynb)
 - The **Model Editing** tutorial shows how to create and edit models procedurally:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/mjspec.ipynb)
 - The **rollout** tutorial shows how to use the multithreaded `rollout` module:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/rollout.ipynb)
 - The **LQR** tutorial synthesizes a linear-quadratic controller, balancing a
   humanoid on one leg:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/LQR.ipynb)
 - The **least-squares** tutorial explains how to use the Python-based nonlinear
   least-squares solver:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/least_squares.ipynb)
 - The **MJX** tutorial provides usage examples of
   [MuJoCo XLA](https://mujoco.readthedocs.io/en/stable/mjx.html), a branch of MuJoCo written in JAX:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/tutorial.ipynb)
 - The **differentiable physics** tutorial trains locomotion policies with
   analytical gradients automatically derived from MuJoCo's physics step:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/training_apg.ipynb)

## Installation

### Prebuilt binaries

Versioned releases are available as precompiled binaries from the GitHub
[releases page], built for Linux (x86-64 and AArch64), Windows (x86-64 only),
and macOS (universal). This is the recommended way to use the software.

### Building from source

Users who wish to build MuJoCo from source should consult the [build from
source] section of the documentation. However, note that the commit at
the tip of the `main` branch may be unstable.

### Python (>= 3.10)

The native Python bindings, which come pre-packaged with a copy of MuJoCo, can
be installed from [PyPI] via:

```bash
pip install mujoco
```

Note that Pre-built Linux wheels target `manylinux2014`, see
[here](https://github.com/pypa/manylinux) for compatible distributions. For more
information such as building the bindings from source, see the [Python bindings]
section of the documentation.

## Versioning

We aim to release MuJoCo in the first week of each month. Our versioning
standards changed to modified Semantic Versioning in 3.5.0,
see [versioning](VERSIONING.md) for details.

## Contributing

We welcome community engagement: questions, requests for help, bug reports and
feature requests. To read more about bug reports, feature requests and more
ambitious contributions, please see our [contributors guide](CONTRIBUTING.md)
and [style guide](STYLEGUIDE.md).

## Asking Questions

Questions and requests for help are welcome as a GitHub
["Asking for Help" Discussion](https://github.com/google-deepmind/mujoco/discussions/categories/asking-for-help)
and should focus on a specific problem or question.

## Bug reports and feature requests

GitHub [Issues](https://github.com/google-deepmind/mujoco/issues) are reserved
for bug reports, feature requests and other development-related subjects.

## Related software
MuJoCo is the backbone for numerous environment packages. Below we list several
bindings and converters.

### Bindings

These packages give users of various languages access to MuJoCo functionality:

#### First-party bindings:

- [Python bindings](https://mujoco.readthedocs.io/en/stable/python.html)
  - [dm_control](https://github.com/google-deepmind/dm_control), Google
    DeepMind's related environment stack, includes
    [PyMJCF](https://github.com/google-deepmind/dm_control/blob/main/dm_control/mjcf/README.md),
    a module for procedural manipulation of MuJoCo models.
- [JavaScript bindings and WebAssembly support](/wasm/README.md) (inspired [stillonearth](https://github.com/stillonearth) and [zalo](https://github.com/zalo)'s community projects; [mjswan](https://github.com/ttktjmt/mjswan) extends these with real-time policy control, interactive force
application, and more).
- [C# bindings and Unity plug-in](https://mujoco.readthedocs.io/en/stable/unity.html)

#### Third-party bindings:

- **MATLAB Simulink**: [Simulink Blockset for MuJoCo Simulator](https://github.com/mathworks-robotics/mujoco-simulink-blockset)
  by [Manoj Velmurugan](https://github.com/vmanoj1996).
- **Swift**: [swift-mujoco](https://github.com/liuliu/swift-mujoco)
- **Java**: [mujoco-java](https://github.com/CommonWealthRobotics/mujoco-java)
- **Julia**: [MuJoCo.jl](https://github.com/JamieMair/MuJoCo.jl)
- **Rust**: [MuJoCo-rs](https://github.com/davidhozic/mujoco-rs)

### Converters

- **OpenSim**: [MyoConverter](https://github.com/MyoHub/myoconverter) converts
  OpenSim models to MJCF.
- **SDFormat**: [gz-mujoco](https://github.com/gazebosim/gz-mujoco/) is a
  two-way SDFormat <-> MJCF conversion tool.
- **OBJ**: [obj2mjcf](https://github.com/kevinzakka/obj2mjcf)
  a script for converting composite OBJ files into a loadable MJCF model.
- **onshape**: [Onshape to Robot](https://github.com/rhoban/onshape-to-robot)
  Converts [onshape](https://www.onshape.com/en/) CAD assemblies to MJCF.

## Citation

If you use MuJoCo for published research, please cite:

```
@inproceedings{todorov2012mujoco,
  title={MuJoCo: A physics engine for model-based control},
  author={Todorov, Emanuel and Erez, Tom and Tassa, Yuval},
  booktitle={2012 IEEE/RSJ International Conference on Intelligent Robots and Systems},
  pages={5026--5033},
  year={2012},
  organization={IEEE},
  doi={10.1109/IROS.2012.6386109}
}
```

## License and Disclaimer

Copyright 2021 DeepMind Technologies Limited.

Box collision code ([`engine_collision_box.c`](https://github.com/google-deepmind/mujoco/blob/main/src/engine/engine_collision_box.c))
is Copyright 2016 Svetoslav Kolev.

ReStructuredText documents, images, and videos in the `doc` directory are made
available under the terms of the Creative Commons Attribution 4.0 (CC BY 4.0)
license. You may obtain a copy of the License at
https://creativecommons.org/licenses/by/4.0/legalcode.

Source code is licensed under the Apache License, Version 2.0. You may obtain a
copy of the License at https://www.apache.org/licenses/LICENSE-2.0.

This is not an officially supported Google product.

[build from source]: https://mujoco.readthedocs.io/en/latest/programming#building-from-source
[Getting Started]: https://mujoco.readthedocs.io/en/latest/programming#getting-started
[Unity]: https://unity.com/
[releases page]: https://github.com/google-deepmind/mujoco/releases
[mujoco.readthedocs.io]: https://mujoco.readthedocs.io
[changelog]: https://mujoco.readthedocs.io/en/latest/changelog.html
[Python bindings]: https://mujoco.readthedocs.io/en/stable/python.html#python-bindings
[PyPI]: https://pypi.org/project/mujoco/


## File tree (depth 3, assets pruned)

```
.clang-format
.github/
  DISCUSSION_TEMPLATE/
    Asking-for-Help.yaml
  ISSUE_TEMPLATE/
    Bug-Report.yaml
    Feature-Request.yaml
    config.yml
  actions/
    notify-chat/
  workflows/
    README.md
    build.yml
    build_matrix.json
    build_steps.sh
    lint.yml
    live.yml
    publish-wasm.yml
    update_live.yml
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
CMakeLists.txt
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
STYLEGUIDE.md
VERSIONING.md
banner.png
cmake/
  CheckAvxSupport.cmake
  FindOrFetch.cmake
  MujocoDependencies.cmake
  MujocoHarden.cmake
  MujocoLinkOptions.cmake
  MujocoMacOS.cmake
  MujocoOptions.cmake
  ShellTests.cmake
  TargetAddRpath.cmake
  abseil-cpp-source_location.patch
  ccd-support-emscripten.patch
  cleanup_test_dir.sh
  filament-allow-clang-windows.patch
  libwebp-apple-float16.patch
  mujocoConfig.cmake.in
  qhull-support-emscripten.patch
  setup_test_dir.sh
  third_party_deps/
    atkinson_hyperlegible_mono/
    atkinson_hyperlegible_mono.cmake
    atkinson_hyperlegible_next/
    atkinson_hyperlegible_next.cmake
    dear_imgui/
    dear_imgui.cmake
    filament.cmake
    font_awesome/
    font_awesome.cmake
    implot/
    implot.cmake
    libwebp.cmake
    lodepng/
    lodepng.cmake
    openusd/
    openusd.cmake
    sdl2.cmake
dist/
  Info.plist.framework.in
  Info.plist.simulate.in
  module.modulemap
  mujoco.icns
  mujoco.ico
  mujoco.rc
  mujoco_studio.icns
  mujoco_studio.ico
  mujoco_studio.rc
  simulate.rc
doc/
  APIreference/
    APIfunctions.rst
    APIglobals.rst
    APItypes.rst
    functions.rst
    functions_override.rst
    index.rst
  Makefile
  OpenUSD/
    building.rst
    exporting.rst
    importing.rst
    index.rst
    mjcPhysics.rst
    mjcf_file_format_plugin.rst
  XMLreference.rst
  XMLschema.rst
  _static/
    FLV.m
    dcmotor.pdf
    desert.png
    example.mp4
    example.xml
    example_saved.txt
    example_saved.xml
    favicons/
    fromto.xml
    gyroscopic.xml
    hello.xml
    onthispage_mjwarp.js
    pendulum.xml
    tendon.xml
  changelog.rst
  computation/
    fluid.rst
    index.rst
  conf.py
  css/
    theme_overrides.css
    theme_overrides_mjwarp.css
  dcmotor/
    buildpdf.sh
    dcmotor.tex
    refs.bib
  docutils.conf
  ext/
    header_reader.py
    header_reader_test.py
    mujoco_include.py
  generate/
    generate_api_header.py
    generate_default_table.py
    generate_dmcontrol.py
    generate_functions.py
    generate_linenumbers.py
    generate_mjcf_map.py
    generate_mjcf_table.py
    generate_read_table.py
    generate_schema.py
    generate_xsd.py
    mjcf_schema.py
    resource_loader.py
  includes/
    macros.rst
    references.h
    roles.rst
  index.rst
  js/
    linenumbers.js
  make_mujoco_stubs.py
  mjwarp/
    api.rst
    index.rst
    update_types.py
  mjx.rst
  mjx_api.rst
  modeling.rst
  models.rst
  overview.rst
  programming/
    extension.rst
    index.rst
    modeledit.rst
    samples.rst
    simulation.rst
    ui.rst
    visualization.rst
  python.rst
  references.bib
  requirements.txt
  skills/
    README.md
    accelerated/
    gui/
    python/
    rendering/
    spec_editing/
    studio/
  templates/
    layout.html
  unity.rst
include/
  mujoco/
    experimental/
    mjassert.h
    mjdata.h
    mjexport.h
    mjmacro.h
    mjmodel.h
    mjplugin.h
    mjrender.h
    mjrfilament.h
    mjsan.h
    mjspec.h
    mjspecmacro.h
    mjtype.h
    mjui.h
    mjvisualize.h
    mjxmacro.h
    mujoco.h
mjx/
  MANIFEST.in
  README.md
  cuda_requirements.txt
  mujoco/
    mjx/
  pyproject.toml
  requirements.txt
  training_apg.ipynb
  tutorial.ipynb
model/
  CMakeLists.txt
  adhesion/
    README.md
    active_adhesion.xml
    fridge_door.xml
    sand_castle.xml
  arch/
    README.md
    gothic.xml
    hyperbolic.xml
    roman.xml
  balloons/
    balloons.xml
  car/
    car.xml
  cards/
    README.md
    cards.xml
    house_of_cards.xml
  cube/
    README.md
    cube_3x3x3.xml
  flex/
    asset/
    bag.xml
    basket.xml
    bunny.xml
    bunny_multicell.xml
    bunny_quadratic.xml
    bunny_shell.xml
    bunny_with_uv.xml
    cloth_sdf.xml
    drape.xml
    flag.xml
    floppy.xml
    gripper.xml
    gripper_2d.xml
    gripper_trilinear.xml
    hollow_vs_solid.xml
    jelly.xml
    mannequin.xml
    pancake.xml
    pinch.xml
    plate.xml
    poncho.xml
    poncho_edgeequality.xml
    press.xml
    pulley.xml
    quadratic.xml
    scene.xml
    softbox.xml
    sphere_full.xml
    sphere_radial.xml
    sphere_trilinear.xml
    strain.xml
    trampoline.xml
    trilinear.xml
  hammock/
    hammock.xml
  humanoid/
    100_humanoids.xml
    22_humanoids.xml
    README.md
    humanoid.png
    humanoid.xml
    humanoid100.xml
  mug/
    mug.obj
    mug.png
    mug.xml
  plugin/
    actuator/
    elasticity/
    sdf/
    sensor/
  replicate/
    README.md
    asset/
    bowl.xml
    bunnies.xml
    bunny.obj
    container.xml
    cylinder.xml
    helix.xml
    leaves.xml
    newton_cradle.xml
    particle.xml
    particle_free.xml
    particle_free2d.xml
    scene.xml
    stonehenge.xml
    tendon.xml
  sleep/
    100_humanoids.xml
    dominos.xml
    humanoid.xml
  slider_crank/
    slider_crank.xml
  surfacevel/
    carousel.xml
    treadmill.xml
  tactile/
    tactile.xml
  tendon_arm/
    arm26.xml
  welcome/
    welcome.xml
plugin/
  .clang-format
  actuator/
    CMakeLists.txt
    README.md
    pid.cc
    pid.h
    register.cc
  elasticity/
    CMakeLists.txt
    README.md
    cable.cc
    cable.h
    elasticity.cc
    elasticity.h
    register.cc
  obj_decoder/
    CMakeLists.txt
    obj_decoder.cc
  sdf/
    CMakeLists.txt
    README.md
    bolt.cc
    bolt.h
    bowl.cc
    bowl.h
    gear.cc
    gear.h
    nut.cc
    nut.h
    register.cc
    sdf.cc
    sdf.h
    torus.cc
    torus.h
  sensor/
    CMakeLists.txt
    README.md
    register.cc
    touch_grid.cc
    touch_grid.h
  stl_decoder/
    CMakeLists.txt
    stl_decoder.cc
  usd_decoder/
    CMakeLists.txt
    kinematic_tree.cc
    kinematic_tree.h
    material_parsing.cc
    material_parsing.h
    newton_tokens.cc
    newton_tokens.h
    usd_decoder.cc
python/
  LQR.ipynb
  MANIFEST.in
  README.md
  build_requirements.txt
  build_requirements_usd.txt
  least_squares.ipynb
  make_sdist.sh
  make_sdist_requirements.txt
  mjspec.ipynb
  mujoco/
    CMakeLists.txt
    __init__.py
    bindings_test.py
    callbacks.cc
    cgl/
    codegen/
    constants.cc
    egl/
    enums.cc
    errors.cc
    errors.h
    experimental/
    functions.cc
    functions.h
    gil.h
    gil_test.py
    gl_context.py
    glfw/
    indexer_xmacro.h
    indexers.cc
    indexers.h
    introspect/
    memory_leak_test.py
    minimize.py
    minimize_test.py
    mjpython/
    msh2obj.py
    msh2obj_test.py
    osmesa/
    private.h
    raw.h
    render.cc
    render_filament.cc
    render_filament_generated.cc.inc
    render_test.py
    renderer.py
    renderer_test.py
    rendering/
    rollout.cc
    rollout.py
    rollout_test.py
    serialization.h
    simulate.cc
    specs.cc
    specs_test.py
    specs_wrapper.cc
    specs_wrapper.h
    structs.cc
    structs.h
    structs_wrappers.cc
    sysid/
    testdata/
    thread_safety_test.py
    threadpool.cc
    threadpool.h
    usd/
    util/
    vfs.h
    vfs_test.py
    viewer.py
    viewer_test.py
  pyproject.toml
  rollout.ipynb
  setup.py
  tutorial.ipynb
sample/
  .clang-format
  CMakeLists.txt
  array_safety.h
  basic.cc
  cmake/
    CheckAvxSupport.cmake
    FindOrFetch.cmake
    MujocoHarden.cmake
    MujocoLinkOptions.cmake
    MujocoMacOS.cmake
    SampleDependencies.cmake
    SampleOptions.cmake
  compile.cc
  dependencies.cc
  record.cc
  render.cc
  testspeed.cc
simulate/
  .clang-format
  CMakeLists.txt
  README.md
  array_safety.h
  cmake/
    CheckAvxSupport.cmake
    FindOrFetch.cmake
    MujocoHarden.cmake
    MujocoLinkOptions.cmake
    MujocoMacOS.cmake
    SimulateDependencies.cmake
    SimulateOptions.cmake
  glfw_adapter.cc
  glfw_adapter.h
  glfw_corevideo.h
  glfw_corevideo.mm
  glfw_dispatch.cc
  glfw_dispatch.h
  macos_gui.mm
  main.cc
  platform_ui_adapter.cc
  platform_ui_adapter.h
  simulate.cc
  simulate.h
src/
  cc/
    array_safety.h
  engine/
    CMakeLists.txt
    engine_array_safety.h
    engine_callback.c
    engine_callback.h
    engine_collision_box.c
    engine_collision_continuous.c
    engine_collision_continuous.h
    engine_collision_convex.c
    engine_collision_convex.h
    engine_collision_driver.c
    engine_collision_driver.h
    engine_collision_flex.c
    engine_collision_flex.h
    engine_collision_gjk.c
    engine_collision_gjk.h
    engine_collision_primitive.c
    engine_collision_primitive.h
    engine_collision_sdf.c
    engine_collision_sdf.h
    engine_core_constraint.c
    engine_core_constraint.h
    engine_core_smooth.c
    engine_core_smooth.h
    engine_core_util.c
    engine_core_util.h
    engine_crossplatform.cc
    engine_crossplatform.h
    engine_derivative.c
    engine_derivative.h
    engine_derivative_fd.c
    engine_derivative_fd.h
    engine_forward.c
    engine_forward.h
    engine_global_table.h
    engine_init.c
    engine_init.h
    engine_inline.h
    engine_inverse.c
    engine_inverse.h
    engine_io.c
    engine_io.h
    engine_ipc.c
    engine_ipc.h
    engine_island.c
    engine_island.h
    engine_macro.h
    engine_memory.c
    engine_memory.h
    engine_name.c
    engine_name.h
    engine_passive.c
    engine_passive.h
    engine_plugin.cc
    engine_plugin.h
    engine_print.c
    engine_print.h
    engine_ray.c
    engine_ray.h
    engine_sensor.c
    engine_sensor.h
    engine_setconst.c
    engine_setconst.h
    engine_sleep.c
    engine_sleep.h
    engine_solver.c
    engine_solver.h
    engine_sort.h
    engine_support.c
    engine_support.h
    engine_thread.cc
    engine_thread.h
    engine_util_blas.c
    engine_util_blas.h
    engine_util_blas_avx.h
    engine_util_errmem.c
    engine_util_errmem.h
    engine_util_misc.c
    engine_util_misc.h
    engine_util_solve.c
    engine_util_solve.h
    engine_util_sparse.c
    engine_util_sparse.h
    engine_util_sparse_avx.h
    engine_util_spatial.c
    engine_util_spatial.h
    engine_vis_init.c
    engine_vis_init.h
    engine_vis_interact.c
    engine_vis_interact.h
    engine_vis_visualize.c
    engine_vis_visualize.h
  experimental/
    filament/
    studio/
    usd/
  render/
    classic/
    filament/
    noop/
  ui/
    CMakeLists.txt
    ui_main.c
    ui_main.h
  user/
    .clang-format
    CMakeLists.txt
    user_api.cc
    user_api.h
```

## Config files (3)


### .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🙏 Asking for Help
    about: Start a new discussion
    url: https://github.com/google-deepmind/mujoco/discussions/categories/asking-for-help

```

### .github/actions/notify-chat/action.yml

```yaml
name: 'Notify Google Chat'
description: 'Sends a Cards V2 build failure notification to a Google Chat space'

inputs:
  service-account-key:
    description: 'JSON Service Account private key with chat.messages.create scope'
    required: false
    default: ''
  space-id:
    description: 'Google Chat space resource name (e.g. spaces/AAAAzcCLt1A)'
    required: true
  commit-sha:
    description: 'Commit SHA to report'
    required: false
    default: ${{ github.event.pull_request.head.sha || github.sha }}
  author-name:
    description: 'Commit author name'
    required: false
    default: ${{ github.event.head_commit.author.name || '' }}
  author-email:
    description: 'Commit author email'
    required: false
    default: ${{ github.event.head_commit.author.email || '' }}
  commit-message:
    description: 'Commit message'
    required: false
    default: ${{ github.event.head_commit.message || github.event.pull_request.title || '' }}
  user-id-map:
    description: 'JSON mapping of author emails to Google Chat user IDs for @mentions'
    required: false
    default: ''

runs:
  using: 'composite'
  steps:
    - name: Run notify script
      shell: bash
      env:
        CHAT_SERVICE_ACCOUNT_KEY: ${{ inputs.service-account-key }}
        CHAT_USER_ID_MAP: ${{ inputs.user-id-map }}
        CHAT_SPACE_ID: ${{ inputs.space-id }}
        CHAT_COMMIT_SHA: ${{ inputs.commit-sha }}
        CHATMSG_AUTHOR_NAME: ${{ inputs.author-name }}
        CHATMSG_AUTHOR_EMAIL: ${{ inputs.author-email }}
        CHATMSG_COMMIT_MESSAGE: ${{ inputs.commit-message }}
      run: python3 ${{ github.action_path }}/notify_chat.py

```

### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
        exclude: \.patch$
      - id: end-of-file-fixer
  - repo: https://github.com/pre-commit/mirrors-clang-format
    rev: v23.1.0
    hooks:
      - id: clang-format
        types_or: [c++, c]

```

## Python signatures and reward/observation bodies (4 files)


### .github/actions/notify-chat/notify_chat.py

```
"""Sends a Cards V2 build status notification to Google Chat via REST API."""
def get_service_account_token(key_data, scope)
def git_log(fmt)
def main()
```

### mjx/mujoco/mjx/_src/constraint.py

```
"""Core non-smooth constraint functions."""
class _Efc(PyTreeNode)
    """Support data for creating constraint matrices."""
def _kbi(m, solref, solimp, pos)
def _row(j)
def _efc_equality_connect(m, d)
def _efc_equality_weld(m, d)
def _efc_equality_joint(m, d)
def _efc_equality_tendon(m, d)
def _efc_friction(m, d)
def _efc_limit_ball(m, d)
def _efc_limit_slide_hinge(m, d)
def _efc_limit_tendon(m, d)
def _efc_contact_frictionless(m, d)
def _efc_contact_pyramidal(m, d, condim)
def _efc_contact_elliptic(m, d, condim)
def counts(efc_type)
def make_efc_type(m, dim)
def make_efc_address(m, dim, efc_type)
def make_constraint(m, d)
```

### mjx/mujoco/mjx/_src/constraint_test.py

```
"""Tests for constraint functions."""
def _assert_eq(a, b, name)
def _assert_attr_eq(a, b, attr)
class ConstraintTest(TestCase)
    def setUp(self)
    def test_constraints(self, cone, rand_eq_active)
    def test_disable_refsafe(self)
    def test_disable_constraint(self)
    def test_disable_equality(self)
    def test_disable_contact(self)
    def test_disable_frictionloss(self)
    def test_margin(self)
```

### python/mujoco/experimental/studio/viewer_handle.py

```
"""Viewer handle and event handlers for the simulation side."""
class ViewerHandle()
    """A handle for interacting with a running viewer application from the sim."""
    def __init__(self, sim_endpoint)
    def close(self)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def is_running(self)
    def send_to_viewer(self, message)
    def sync(self, model, data)
    def _on_model(self, event)
    def _on_state(self, event)
    def _on_reset(self, _)
    def _on_exit(self, _)
    def _on_mjoption(self, event)
```