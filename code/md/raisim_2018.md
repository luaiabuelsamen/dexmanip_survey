# raisim_2018

source: https://github.com/raisimTech/raisimLib


commit: 74b836fba1dbd3227ce61f8abf7bffbd8f6e41ca


## README

We no longer support Raisim. Please go to Raisim2 repo: https://github.com/raisimTech/raisim2Lib


# RaiSim

RaiSim is a physics engine for robotics and artificial intelligence research that provides efficient and accurate simulations for robotic systems. We specialize in running rigid-body simulations while having an accessible, easy to use C++ library.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/CN0ah5-OWik/0.jpg)](https://www.youtube.com/watch?v=CN0ah5-OWik)

## News
Closed-loop system simulation is now available! Check out the [minitaur example](https://github.com/raisimTech/raisimLib/tree/master/examples/src/server/minitaur.cpp)

## Dependencies

### - Eigen3
##### Ubuntu
```bash
sudo apt install libeigen3-dev
```

#### Windows
Install desired release [here](http://eigen.tuxfamily.org) and unzip file at C:\Program, files for better discoverability.

### - CMake
Install version > 3.10 [here](https://cmake.org/download/).

### - Visual Studio 2019
Install [here](https://visualstudio.microsoft.com/vs/older-downloads/), make sure to install C++ module by checking the box during installation.

## Installation

Further documentation available on the [RaiSim Tech website](http://raisim.com).

## Features
- Supports free camera movement
- Allows the recording of screenshots and recordings
- Contact and collision masks
- Materials system to simulate different textures
- Height maps to create different sytles of terrain
- Ray Test to create collision checkers 

## Troubleshooting
- Ensure that all versions of dependencies fit the documentation. etc.(Visual Studio 2019, CMake verson > 3.10)
- If run into problem with executing into the raisimUnity.x86_64 file, ensure that your graphics card driver is compatible with current graphics card. (Cannot use the default open-source graphics card driver nouveau)
- Make sure to use raisimUnity natively and not on a docker.
- If using Linux, install minizip, ffmpeg, and vulkan.
- If drivers don't support vulkan, use raisimUnityOpengl instead of raisimUnisty. Found in raisimUnityOpengl directory.
- Make sure to set environment variable to $LOCAL_INSTALL when installing raisim.

## License

You should get a valid license and an activation key from the [RaiSim Tech website](http://raisim.com) to use RaiSim.
Post issues to this github repo for questions. 
Send an email to info.raisim@gmail.com for any special inquiry.

## Supported OS

MAC (including m1), Linux, Windows.









## File tree (depth 3, assets pruned)

```
.gitignore
CMakeLists.txt
COPYING
DEVELOPERS_ONLY/
  linux_build.sh
  linux_requirements.sh
  mac_build.sh
  windowsInstall.ps1
LICENSE.md
README.md
cmake/
  FindSphinx.cmake
examples/
  CMakeLists.txt
  include/
    benchmarkCommon.hpp
    helper.hpp
  src/
    benchmark/
    maps/
    server/
    xml/
package.xml
raisim/
  linux/
    include/
    lib/
  linux-arm/
    include/
    lib/
  m1/
    include/
    lib/
  mac/
    include/
    lib/
  win32/
    bin/
    include/
    lib/
    mt_debug/
    mt_release/
raisimGymTorch/
  .gitignore
  CMakeLists.txt
  LICENSE
  README.md
  __init__.py
  raisimGymTorch/
    __init__.py
    algo/
    env/
    helper/
    stable_baselines3/
  rsg_anymal.pdb
  setup.py
  thirdParty/
    pybind11/
raisimMatlab/
  .gitignore
  CMakeLists.txt
  LICENSE
  debug_app.cpp
  examples/
    raisimMatlabLaikagoExample.m
  license.txt
  raisim_interface_mex.cpp
  raisim_interface_mex.hpp
raisimPy/
  .gitignore
  CMakeLists.txt
  COPYING
  README.rst
  examples/
    heightMap.py
    newtonsCradle.py
    rayDemo2.py
    robots.py
    springs.py
    visualObjects.py
  include/
    converter.hpp
    utils.hpp
  src/
    articulated_system.cpp
    constraints.cpp
    contact.cpp
    converter.cpp
    materials.cpp
    math.cpp
    object.cpp
    raisim_wrapper.cpp
    single_bodies.cpp
    terrain.cpp
    world.cpp
raisimUnity/
  .gitignore
  README.md
  TRY_OPENGL_VERSION_IF_THIS_DOESNT_WORK
  linux/
    .gitignore
    LinuxPlayer_s.debug
    Logs/
    RaiSimUnity_BurstDebugInformation_DoNotShip/
    UnityPlayer.so
    UnityPlayer_s.debug
    gui_settings.xml
    raisimUnity.x86_64
    raisimUnity_BurstDebugInformation_DoNotShip/
    raisimUnity_Data/
  m1/
    RaiSimUnity.app/
    RaiSimUnity_BurstDebugInformation_DoNotShip/
  m1_assimp_backup/
    libassimp.bundle
  mac/
    RaiSimUnity.app/
  mac_assimp_backup/
    libassimp.dylib
  win32/
    Logs/
    MonoBleedingEdge/
    RaiSimUnity.exe
    RaiSimUnity_BurstDebugInformation_DoNotShip/
    RaiSimUnity_Data/
    Screenshot/
    UnityCrashHandler64.exe
    UnityPlayer.dll
    assimp.dll
    gui_settings.xml
raisimUnityOpengl/
  linux/
    LinuxPlayer_s.debug
    Logs/
    UnityPlayer.so
    UnityPlayer_s.debug
    gui_settings.xml
    raisimUnity.x86_64
    raisimUnity_BurstDebugInformation_DoNotShip/
    raisimUnity_Data/
rsc/
  a1/
  aliengo/
    LICENSE
    aliengo.urdf
  anymal/
    LICENSE
  anymal_c/
    LICENSE
    README.md
    materials/
    sensors/
  atlas/
    head.dae
    head.stl
    head_camera.stl
    l_clav.stl
    l_farm.stl
    l_foot.stl
    l_hand.stl
    l_larm.stl
    l_lglut.stl
    l_lleg.stl
    l_scap.stl
    l_talus.stl
    l_uarm.stl
    l_uglut.stl
    l_uleg.stl
    ltorso.stl
    mtorso.stl
    pelvis.stl
    r_clav.stl
    r_farm.stl
    r_foot.stl
    r_hand.stl
    r_larm.stl
    r_lglut.stl
    r_lleg.stl
    r_scap.stl
    r_talus.stl
    r_uarm.stl
    r_uglut.stl
    r_uleg.stl
    robot.urdf
    utorso.stl
  cartPole/
    cartpole.urdf
  cassie/
    LICENSE
    achilles-rod.stl
    cassie.xml
    foot-crank.stl
    foot.stl
    heel-spring.stl
    hip-pitch.stl
    hip-roll.stl
    hip-yaw.stl
    knee-spring.stl
    knee.stl
    pelvis.stl
    plantar-rod.stl
    shin.stl
    tarsus.stl
  chain/
    robot.urdf
    robot_limit.urdf
    robot_short.urdf
    robot_springed.urdf
    robot_springed_10.urdf
    robot_springed_20.urdf
    robot_springed_30.urdf
  go1/
    LICENSE
    go1.urdf
  husky/
    husky.urdf
    license.txt
  kinova/
    LICENSE
  laikago/
    LICENSE
    calf.dae
    default_cfg.yaml
    hip.dae
    laikago.urdf
    thigh.dae
    thigh_mirror.dae
    trunk.dae
  laikago.xml
  laikagoOnHeightMap.xml
  megabot/
    smb.urdf
  minitaur/
    license.txt
    minitaur.urdf
    t-motor.jpg
    tmotor.blend
    tmotor3.mtl
    tmotor3.obj
    vision/
  monkey/
    LICENSE
    LICENSE.meta
    monkey.obj
    monkey.obj.meta
    monkey.obj.mtl
  raisimUnrealMaps/
    hill1.png
    lake1.png
    mountain1.png
    office1.xml
  sphere.obj
  springDamper/
    cartpole.urdf
    chainSpringed.urdf
  templatedTrackedRobot/
    trackedTemplate.urdf
  testMaterials.xml
  xmlScripts/
    heightMaps/
    material/
    objects/
    templatedWorld/
    wire/
thirdParty/
  Eigen3/
    LICENSE
    include/
    share/
  pybind11/
    .appveyor.yml
    .clang-format
    .clang-tidy
    .cmake-format.yaml
    .codespell-ignore-lines
    .gitattributes
    .gitignore
    .pre-commit-config.yaml
    .readthedocs.yml
    CMakeLists.txt
    LICENSE
    MANIFEST.in
    README.rst
    include/
    noxfile.py
    pybind11/
    pyproject.toml
    setup.cfg
    setup.py
    tests/
    tools/
```

## Config files (19)


### raisim/win32/bin/rsc/laikago/default_cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  num_envs: 100
  num_threads: 40
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0

  forwardVelRewardCoeff: 0.3
  torqueRewardCoeff: -2e-5
```

### raisimGymTorch/raisimGymTorch/env/envs/rsg_anymal/cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  render: True
# just testing commenting
  num_envs: 100
  eval_every_n: 200
  num_threads: 30
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0
  action_std: 0.3
  reward:
    forwardVel:
      coeff: 0.3
    torque:
      coeff: -4e-5

architecture:
  policy_net: [128, 128]
  value_net: [128, 128]

```

### raisimGymTorch/thirdParty/pybind11/.appveyor.yml

```yaml
version: 1.0.{build}
image:
- Visual Studio 2015
test: off
skip_branch_with_pr: true
build:
  parallel: true
platform:
- x86
environment:
  matrix:
  - PYTHON: 36
    CONFIG: Debug
  - PYTHON: 27
    CONFIG: Debug
install:
- ps: |
    $env:CMAKE_GENERATOR = "Visual Studio 14 2015"
    if ($env:PLATFORM -eq "x64") { $env:PYTHON = "$env:PYTHON-x64" }
    $env:PATH = "C:\Python$env:PYTHON\;C:\Python$env:PYTHON\Scripts\;$env:PATH"
    python -W ignore -m pip install --upgrade pip wheel
    python -W ignore -m pip install pytest numpy --no-warn-script-location pytest-timeout
- ps: |
    Start-FileDownload 'https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip'
    7z x eigen-3.3.7.zip -y > $null
    $env:CMAKE_INCLUDE_PATH = "eigen-3.3.7;$env:CMAKE_INCLUDE_PATH"
build_script:
- cmake -G "%CMAKE_GENERATOR%" -A "%CMAKE_ARCH%"
    -DCMAKE_CXX_STANDARD=14
    -DPYBIND11_WERROR=ON
    -DDOWNLOAD_CATCH=ON
    -DCMAKE_SUPPRESS_REGENERATION=1
    .
- set MSBuildLogger="C:\Program Files\AppVeyor\BuildAgent\Appveyor.MSBuildLogger.dll"
- cmake --build . --config %CONFIG% --target pytest -- /m /v:m /logger:%MSBuildLogger%
- cmake --build . --config %CONFIG% --target cpptest -- /m /v:m /logger:%MSBuildLogger%
on_failure: if exist "tests\test_cmake_build" type tests\test_cmake_build\*.log*

```

### raisimGymTorch/thirdParty/pybind11/.cmake-format.yaml

```yaml
parse:
  additional_commands:
    pybind11_add_module:
      flags:
        - THIN_LTO
        - MODULE
        - SHARED
        - NO_EXTRAS
        - EXCLUDE_FROM_ALL
        - SYSTEM

format:
  line_width: 99
  tab_size: 2

  # If an argument group contains more than this many sub-groups
  # (parg or kwarg groups) then force it to a vertical layout.
  max_subgroups_hwrap: 2

  # If a positional argument group contains more than this many
  # arguments, then force it to a vertical layout.
  max_pargs_hwrap: 6

  # If a cmdline positional group consumes more than this many
  # lines without nesting, then invalidate the layout (and nest)
  max_rows_cmdline: 2
  separate_ctrl_name_with_space: false
  separate_fn_name_with_space: false
  dangle_parens: false

  # If the trailing parenthesis must be 'dangled' on its on
  # 'line, then align it to this reference: `prefix`: the start'
  # 'of the statement,  `prefix-indent`: the start of the'
  # 'statement, plus one indentation  level, `child`: align to'
  # the column of the arguments
  dangle_align: prefix
  # If the statement spelling length (including space and
  # parenthesis) is smaller than this amount, then force reject
  # nested layouts.
  min_prefix_chars: 4

  # If the statement spelling length (including space and
  # parenthesis) is larger than the tab width by more than this
  # amount, then force reject un-nested layouts.
  max_prefix_chars: 10

  # If a candidate layout is wrapped horizontally but it exceeds
  # this many lines, then reject the layout.
  max_lines_hwrap: 2

  line_ending: unix

  # Format command names consistently as 'lower' or 'upper' case
  command_case: canonical

  # Format keywords consistently as 'lower' or 'upper' case
  # unchanged is valid too
  keyword_case: 'upper'

  # A list of command names which should always be wrapped
  always_wrap: []

  # If true, the argument lists which are known to be sortable
  # will be sorted lexicographically
  enable_sort: true

  # If true, the parsers may infer whether or not an argument
  # list is sortable (without annotation).
  autosort: false

# Causes a few issues - can be solved later, possibly.
markup:
  enable_markup: false

```

### raisimGymTorch/thirdParty/pybind11/.github/ISSUE_TEMPLATE/bug-report.yml

```yaml
name: Bug Report
description: File an issue about a bug
title: "[BUG]: "
labels: [triage]
body:
  - type: markdown
    attributes:
      value: |
        Maintainers will only make a best effort to triage PRs. Please do your best to make the issue as easy to act on as possible, and only open if clearly a problem with pybind11 (ask first if unsure).
  - type: checkboxes
    id: steps
    attributes:
      label: Required prerequisites
      description: Make sure you've completed the following steps before submitting your issue -- thank you!
      options:
        - label: Make sure you've read the [documentation](https://pybind11.readthedocs.io). Your issue may be addressed there.
          required: true
        - label: Search the [issue tracker](https://github.com/pybind/pybind11/issues) and [Discussions](https:/pybind/pybind11/discussions) to verify that this hasn't already been reported. +1 or comment there if it has.
          required: true
        - label: Consider asking first in the [Gitter chat room](https://gitter.im/pybind/Lobby) or in a [Discussion](https:/pybind/pybind11/discussions/new).
          required: false

  - type: textarea
    id: description
    attributes:
      label: Problem description
      placeholder: >-
        Provide a short description, state the expected behavior and what
        actually happens. Include relevant information like what version of
        pybind11 you are using, what system you are on, and any useful commands
        / output.
    validations:
      required: true

  - type: textarea
    id: code
    attributes:
      label: Reproducible example code
      placeholder: >-
        The code should be minimal, have no external dependencies, isolate the
        function(s) that cause breakage. Submit matched and complete C++ and
        Python snippets that can be easily compiled and run to diagnose the
        issue. If possible, make a PR with a new, failing test to give us a
        starting point to work on!
      render: text

```

### raisimGymTorch/thirdParty/pybind11/.github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
  - name: Ask a question
    url: https://github.com/pybind/pybind11/discussions/new
    about: Please ask and answer questions here, or propose new ideas.
  - name: Gitter room
    url: https://gitter.im/pybind/Lobby
    about: A room for discussing pybind11 with an active community

```

### raisimGymTorch/thirdParty/pybind11/.github/dependabot.yml

```yaml
version: 2
updates:
  # Maintain dependencies for GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"
    ignore:
      # Official actions have moving tags like v1
      # that are used, so they don't need updates here
      - dependency-name: "actions/checkout"
      - dependency-name: "actions/setup-python"
      - dependency-name: "actions/cache"
      - dependency-name: "actions/upload-artifact"
      - dependency-name: "actions/download-artifact"
      - dependency-name: "actions/labeler"

```

### raisimGymTorch/thirdParty/pybind11/.github/labeler.yml

```yaml
docs:
- any:
  - 'docs/**/*.rst'
  - '!docs/changelog.rst'
  - '!docs/upgrade.rst'

ci:
- '.github/workflows/*.yml'

```

### raisimGymTorch/thirdParty/pybind11/.github/labeler_merged.yml

```yaml
needs changelog:
- all:
  - '!docs/changelog.rst'

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/ci.yml

```yaml
name: CI

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - master
      - stable
      - v*

concurrency:
  group: test-${{ github.ref }}
  cancel-in-progress: true

env:
  PIP_ONLY_BINARY: numpy

jobs:
  # This is the "main" test suite, which tests a large number of different
  # versions of default compilers and Python versions in GitHub Actions.
  standard:
    strategy:
      fail-fast: false
      matrix:
        runs-on: [ubuntu-latest, windows-2022, macos-latest]
        python:
        - '2.7'
        - '3.5'
        - '3.6'
        - '3.9'
        - '3.10'
        - 'pypy-3.7-v7.3.7'
        - 'pypy-3.8-v7.3.7'

        # Items in here will either be added to the build matrix (if not
        # present), or add new keys to an existing matrix element if all the
        # existing keys match.
        #
        # We support an optional key: args, for cmake args
        include:
          # Just add a key
          - runs-on: ubuntu-latest
            python: '3.6'
            args: >
              -DPYBIND11_FINDPYTHON=ON
              -DCMAKE_CXX_FLAGS="-D_=1"
          - runs-on: windows-latest
            python: '3.6'
            args: >
              -DPYBIND11_FINDPYTHON=ON
          - runs-on: macos-latest
            python: 'pypy-2.7'
          # Inject a couple Windows 2019 runs
          - runs-on: windows-2019
            python: '3.9'
          - runs-on: windows-2019
            python: '2.7'

    name: "🐍 ${{ matrix.python }} • ${{ matrix.runs-on }} • x64 ${{ matrix.args }}"
    runs-on: ${{ matrix.runs-on }}

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python ${{ matrix.python }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python }}

    - name: Setup Boost (Linux)
      # Can't use boost + define _
      if: runner.os == 'Linux' && matrix.python != '3.6'
      run: sudo apt-get install libboost-dev

    - name: Setup Boost (macOS)
      if: runner.os == 'macOS'
      run: brew install boost

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Cache wheels
      if: runner.os == 'macOS'
      uses: actions/cache@v2
      with:
        # This path is specific to macOS - we really only need it for PyPy NumPy wheels
        # See https://github.com/actions/cache/blob/master/examples.md#python---pip
        # for ways to do this more generally
        path: ~/Library/Caches/pip
        # Look to see if there is a cache hit for the corresponding requirements file
        key: ${{ runner.os }}-pip-${{ matrix.python }}-x64-${{ hashFiles('tests/requirements.txt') }}

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Setup annotations on Linux
      if: runner.os == 'Linux'
      run: python -m pip install pytest-github-actions-annotate-failures

    # First build - C++11 mode and inplace
    - name: Configure C++11 ${{ matrix.args }}
      run: >
        cmake -S . -B .
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=11
        ${{ matrix.args }}

    - name: Build C++11
      run: cmake --build . -j 2

    - name: Python tests C++11
      run: cmake --build . --target pytest -j 2

    - name: C++11 tests
      # TODO: Figure out how to load the DLL on Python 3.8+
      if: "!(runner.os == 'Windows' && (matrix.python == 3.8 || matrix.python == 3.9 || matrix.python == '3.10' || matrix.python == '3.11-dev' || matrix.python == 'pypy-3.8'))"
      run: cmake --build .  --target cpptest -j 2

    - name: Interface test C++11
      run: cmake --build . --target test_cmake_build

    - name: Clean directory
      run: git clean -fdx

    # Second build - C++17 mode and in a build directory
    - name: Configure C++17
      run: >
        cmake -S . -B build2
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        ${{ matrix.args }}

    - name: Build
      run: cmake --build build2 -j 2

    - name: Python tests
      run: cmake --build build2 --target pytest

    - name: C++ tests
      # TODO: Figure out how to load the DLL on Python 3.8+
      if: "!(runner.os == 'Windows' && (matrix.python == 3.8 || matrix.python == 3.9 || matrix.python == '3.10' || matrix.python == '3.11-dev' || matrix.python == 'pypy-3.8'))"
      run: cmake --build build2 --target cpptest

    # Third build - C++17 mode with unstable ABI
    - name: Configure (unstable ABI)
      run: >
        cmake -S . -B build3
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        -DPYBIND11_INTERNALS_VERSION=10000000
        "-DPYBIND11_TEST_OVERRIDE=test_call_policies.cpp;test_gil_scoped.cpp;test_thread.cpp"
        ${{ matrix.args }}

    - name: Build (unstable ABI)
      run: cmake --build build3 -j 2

    - name: Python tests (unstable ABI)
      run: cmake --build build3 --target pytest

    - name: Interface test
      run: cmake --build build2 --target test_cmake_build

    # Eventually Microsoft might have an action for setting up
    # MSVC, but for now, this action works:
    - name: Prepare compiler environment for Windows 🐍 2.7
      if: matrix.python == 2.7 && runner.os == 'Windows'
      uses: ilammy/msvc-dev-cmd@v1.10.0
      with:
        arch: x64

    # This makes two environment variables available in the following step(s)
    - name: Set Windows 🐍 2.7 environment variables
      if: matrix.python == 2.7 && runner.os == 'Windows'
      shell: bash
      run: |
        echo "DISTUTILS_USE_SDK=1" >> $GITHUB_ENV
        echo "MSSdk=1" >> $GITHUB_ENV

    # This makes sure the setup_helpers module can build packages using
    # setuptools
    - name: Setuptools helpers test
      run: pytest tests/extra_setuptools
      if: "!(matrix.python == '3.5' && matrix.runs-on == 'windows-2022')"


  deadsnakes:
    strategy:
      fail-fast: false
      matrix:
        include:
        # TODO: Fails on 3.10, investigate
        - python-version: "3.9"
          python-debug: true
          valgrind: true
      # - python-version: "3.11-dev"
      #   python-debug: false

    name: "🐍 ${{ matrix.python-version }}${{ matrix.python-debug && '-dbg' || '' }} (deadsnakes)${{ matrix.valgrind && ' • Valgrind' || '' }} • x64"
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python ${{ matrix.python-version }} (deadsnakes)
      uses: deadsnakes/action@v2.1.1
      with:
        python-version: ${{ matrix.python-version }}
        debug: ${{ matrix.python-debug }}

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Valgrind cache
      if: matrix.valgrind
      uses: actions/cache@v2
      id: cache-valgrind
      with:
        path: valgrind
        key: 3.16.1 # Valgrind version

    - name: Compile Valgrind
      if: matrix.valgrind && steps.cache-valgrind.outputs.cache-hit != 'true'
      run: |
        VALGRIND_VERSION=3.16.1
        curl https://sourceware.org/pub/valgrind/valgrind-$VALGRIND_VERSION.tar.bz2 -o - | tar xj
        mv valgrind-$VALGRIND_VERSION valgrind
        cd valgrind
        ./configure
        make -j 2 > /dev/null

    - name: Install Valgrind
      if: matrix.valgrind
      working-directory: valgrind
      run: |
        sudo make install
        sudo apt-get update
        sudo apt-get install libc6-dbg  # Needed by Valgrind

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Configure
      env:
        SETUPTOOLS_USE_DISTUTILS: stdlib
      run: >
        cmake -S . -B build
        -DCMAKE_BUILD_TYPE=Debug
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17

    - name: Build
      run: cmake --build build -j 2

    - name: Python tests
      run: cmake --build build --target pytest

    - na
```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/configure.yml

```yaml
name: Config

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - master
      - stable
      - v*

jobs:
  # This tests various versions of CMake in various combinations, to make sure
  # the configure step passes.
  cmake:
    strategy:
      fail-fast: false
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
        arch: [x64]
        cmake: ["3.21"]

        include:
        - runs-on: ubuntu-latest
          arch: x64
          cmake: 3.4

        - runs-on: macos-latest
          arch: x64
          cmake: 3.7

        - runs-on: windows-2016
          arch: x86
          cmake: 3.8

        - runs-on: windows-2016
          arch: x86
          cmake: 3.18

    name: 🐍 3.7 • CMake ${{ matrix.cmake }} • ${{ matrix.runs-on }}
    runs-on: ${{ matrix.runs-on }}

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: 3.7
        architecture: ${{ matrix.arch }}

    - name: Prepare env
      run: python -m pip install -r tests/requirements.txt

    # An action for adding a specific version of CMake:
    #   https://github.com/jwlawson/actions-setup-cmake
    - name: Setup CMake ${{ matrix.cmake }}
      uses: jwlawson/actions-setup-cmake@v1.11
      with:
        cmake-version: ${{ matrix.cmake }}

    # These steps use a directory with a space in it intentionally
    - name: Make build directories
      run: mkdir "build dir"

    - name: Configure
      working-directory: build dir
      shell: bash
      run: >
        cmake ..
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DPYTHON_EXECUTABLE=$(python -c "import sys; print(sys.executable)")

    # Only build and test if this was manually triggered in the GitHub UI
    - name: Build
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release

    - name: Test
      working-directory: build dir
      if: github.event_name == 'workflow_dispatch'
      run: cmake --build . --config Release --target check

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/format.yml

```yaml
# This is a format job. Pre-commit has a first-party GitHub action, so we use
# that: https://github.com/pre-commit/action

name: Format

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - master
    - stable
    - "v*"

jobs:
  pre-commit:
    name: Format
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
    - uses: pre-commit/action@v2.0.3
      with:
        # Slow hooks are marked with manual - slow is okay here, run them too
        extra_args: --hook-stage manual --all-files

  clang-tidy:
    # When making changes here, please also review the "Clang-Tidy" section
    # in .github/CONTRIBUTING.md and update as needed.
    name: Clang-Tidy
    runs-on: ubuntu-latest
    container: silkeh/clang:12
    steps:
    - uses: actions/checkout@v2

    - name: Install requirements
      run: apt-get update && apt-get install -y python3-dev python3-pytest

    - name: Configure
      run: >
        cmake -S . -B build
        -DCMAKE_CXX_CLANG_TIDY="$(which clang-tidy)"
        -DDOWNLOAD_EIGEN=ON
        -DDOWNLOAD_CATCH=ON
        -DCMAKE_CXX_STANDARD=17

    - name: Build
      run: cmake --build build -j 2 -- --keep-going

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/labeler.yml

```yaml
name: Labeler
on:
  pull_request_target:
    types: [closed]

jobs:
  label:
    name: Labeler
    runs-on: ubuntu-latest
    steps:

    - uses: actions/labeler@main
      if: github.event.pull_request.merged == true
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        configuration-path: .github/labeler_merged.yml

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/pip.yml

```yaml
name: Pip

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - master
    - stable
    - v*
  release:
    types:
    - published

env:
  PIP_ONLY_BINARY: numpy

jobs:
  # This builds the sdists and wheels and makes sure the files are exactly as
  # expected. Using Windows and Python 2.7, since that is often the most
  # challenging matrix element.
  test-packaging:
    name: 🐍 2.7 • 📦 tests • windows-latest
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup 🐍 2.7
      uses: actions/setup-python@v2
      with:
        python-version: 2.7

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Python Packaging tests
      run: pytest tests/extra_python_package/


  # This runs the packaging tests and also builds and saves the packages as
  # artifacts.
  packaging:
    name: 🐍 3.8 • 📦 & 📦 tests • ubuntu-latest
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup 🐍 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt build twine

    - name: Python Packaging tests
      run: pytest tests/extra_python_package/

    - name: Build SDist and wheels
      run: |
        python -m build
        PYBIND11_GLOBAL_SDIST=1 python -m build

    - name: Check metadata
      run: twine check dist/*

    - name: Save standard package
      uses: actions/upload-artifact@v2
      with:
        name: standard
        path: dist/pybind11-*

    - name: Save global package
      uses: actions/upload-artifact@v2
      with:
        name: global
        path: dist/pybind11_global-*



  # When a GitHub release is made, upload the artifacts to PyPI
  upload:
    name: Upload to PyPI
    runs-on: ubuntu-latest
    if: github.event_name == 'release' && github.event.action == 'published'
    needs: [packaging]

    steps:
    - uses: actions/setup-python@v2

    # Downloads all to directories matching the artifact names
    - uses: actions/download-artifact@v2

    - name: Publish standard package
      uses: pypa/gh-action-pypi-publish@v1.5.0
      with:
        password: ${{ secrets.pypi_password }}
        packages_dir: standard/

    - name: Publish global package
      uses: pypa/gh-action-pypi-publish@v1.5.0
      with:
        password: ${{ secrets.pypi_password_global }}
        packages_dir: global/

```

### raisimGymTorch/thirdParty/pybind11/.github/workflows/upstream.yml

```yaml

name: Upstream

on:
  workflow_dispatch:
  pull_request:

concurrency:
  group: upstream-${{ github.ref }}
  cancel-in-progress: true

env:
  PIP_ONLY_BINARY: numpy

jobs:
  standard:
    name: "🐍 3.11 dev • ubuntu-latest • x64"
    runs-on: ubuntu-latest
    if: "contains(github.event.pull_request.labels.*.name, 'python dev')"

    steps:
    - uses: actions/checkout@v2

    - name: Setup Python 3.11
      uses: actions/setup-python@v2
      with:
        python-version: "3.11-dev"

    - name: Setup Boost (Linux)
      if: runner.os == 'Linux'
      run: sudo apt-get install libboost-dev

    - name: Update CMake
      uses: jwlawson/actions-setup-cmake@v1.11

    - name: Prepare env
      run: |
        python -m pip install -r tests/requirements.txt

    - name: Setup annotations on Linux
      if: runner.os == 'Linux'
      run: python -m pip install pytest-github-actions-annotate-failures

    # First build - C++11 mode and inplace
    - name: Configure C++11
      run: >
        cmake -S . -B .
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=11

    - name: Build C++11
      run: cmake --build . -j 2

    - name: Python tests C++11
      run: cmake --build . --target pytest -j 2

    - name: C++11 tests
      run: cmake --build .  --target cpptest -j 2

    - name: Interface test C++11
      run: cmake --build . --target test_cmake_build

    - name: Clean directory
      run: git clean -fdx

    # Second build - C++17 mode and in a build directory
    - name: Configure C++17
      run: >
        cmake -S . -B build2
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        ${{ matrix.args }}
        ${{ matrix.args2 }}

    - name: Build
      run: cmake --build build2 -j 2

    - name: Python tests
      run: cmake --build build2 --target pytest

    - name: C++ tests
      run: cmake --build build2 --target cpptest

    # Third build - C++17 mode with unstable ABI
    - name: Configure (unstable ABI)
      run: >
        cmake -S . -B build3
        -DPYBIND11_WERROR=ON
        -DDOWNLOAD_CATCH=ON
        -DDOWNLOAD_EIGEN=ON
        -DCMAKE_CXX_STANDARD=17
        -DPYBIND11_INTERNALS_VERSION=10000000
        "-DPYBIND11_TEST_OVERRIDE=test_call_policies.cpp;test_gil_scoped.cpp;test_thread.cpp"
        ${{ matrix.args }}

    - name: Build (unstable ABI)
      run: cmake --build build3 -j 2

    - name: Python tests (unstable ABI)
      run: cmake --build build3 --target pytest

    - name: Interface test
      run: cmake --build build2 --target test_cmake_build

    # This makes sure the setup_helpers module can build packages using
    # setuptools
    - name: Setuptools helpers test
      run: pytest tests/extra_setuptools

```

### raisimGymTorch/thirdParty/pybind11/.pre-commit-config.yaml

```yaml
# To use:
#
#     pre-commit run -a
#
# Or:
#
#     pre-commit install  # (runs every time you commit in git)
#
# To update this file:
#
#     pre-commit autoupdate
#
# See https://github.com/pre-commit/pre-commit

repos:
# Standard hooks
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.1.0
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-docstring-first
  - id: check-merge-conflict
  - id: check-symlinks
  - id: check-toml
  - id: check-yaml
  - id: debug-statements
  - id: end-of-file-fixer
  - id: mixed-line-ending
  - id: requirements-txt-fixer
  - id: trailing-whitespace
  - id: fix-encoding-pragma
    exclude: ^noxfile.py$

- repo: https://github.com/asottile/pyupgrade
  rev: v2.31.0
  hooks:
  - id: pyupgrade

- repo: https://github.com/PyCQA/isort
  rev: 5.10.1
  hooks:
  - id: isort

# Black, the code formatter, natively supports pre-commit
- repo: https://github.com/psf/black
  rev: 21.12b0 # Keep in sync with blacken-docs
  hooks:
  - id: black

- repo: https://github.com/asottile/blacken-docs
  rev: v1.12.0
  hooks:
  - id: blacken-docs
    additional_dependencies:
    - black==21.12b0 # keep in sync with black hook

# Changes tabs to spaces
- repo: https://github.com/Lucas-C/pre-commit-hooks
  rev: v1.1.10
  hooks:
  - id: remove-tabs

# Autoremoves unused imports
- repo: https://github.com/hadialqattan/pycln
  rev: v1.1.0
  hooks:
  - id: pycln

- repo: https://github.com/pre-commit/pygrep-hooks
  rev: v1.9.0
  hooks:
  - id: python-check-blanket-noqa
  - id: python-check-blanket-type-ignore
  - id: python-no-log-warn
  - id: rst-backticks
  - id: rst-directive-colons
  - id: rst-inline-touching-normal

# Flake8 also supports pre-commit natively (same author)
- repo: https://github.com/PyCQA/flake8
  rev: 4.0.1
  hooks:
  - id: flake8
    additional_dependencies: &flake8_dependencies
      - flake8-bugbear
      - pep8-naming
    exclude: ^(docs/.*|tools/.*)$

- repo: https://github.com/asottile/yesqa
  rev: v1.3.0
  hooks:
  - id: yesqa
    additional_dependencies: *flake8_dependencies

# CMake formatting
- repo: https://github.com/cheshirekow/cmake-format-precommit
  rev: v0.6.13
  hooks:
  - id: cmake-format
    additional_dependencies: [pyyaml]
    types: [file]
    files: (\.cmake|CMakeLists.txt)(.in)?$

# Check static types with mypy
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v0.931
  hooks:
  - id: mypy
    # Running per-file misbehaves a bit, so just run on all files, it's fast
    pass_filenames: false
    additional_dependencies: [typed_ast]

# Checks the manifest for missing files (native support)
- repo: https://github.com/mgedmin/check-manifest
  rev: "0.47"
  hooks:
  - id: check-manifest
    # This is a slow hook, so only run this if --hook-stage manual is passed
    stages: [manual]
    additional_dependencies: [cmake, ninja]

- repo: https://github.com/codespell-project/codespell
  rev: v2.1.0
  hooks:
  - id: codespell
    exclude: ".supp$"
    args: ["-L", "nd,ot,thist"]

- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: v0.8.0.3
  hooks:
  - id: shellcheck

# The original pybind11 checks for a few C++ style items
- repo: local
  hooks:
  - id: disallow-caps
    name: Disallow improper capitalization
    language: pygrep
    entry: PyBind|Numpy|Cmake|CCache|PyTest
    exclude: .pre-commit-config.yaml

- repo: local
  hooks:
  - id: check-style
    name: Classic check-style
    language: system
    types:
    - c++
    entry: ./tools/check-style.sh

```

### raisimGymTorch/thirdParty/pybind11/.readthedocs.yml

```yaml
python:
  version: 3
requirements_file: docs/requirements.txt

```

### rsc/laikago/default_cfg.yaml

```yaml
seed: 1
record_video: yes

environment:
  num_envs: 100
  num_threads: 40
  simulation_dt: 0.0025
  control_dt: 0.01
  max_time: 4.0

  forwardVelRewardCoeff: 0.3
  torqueRewardCoeff: -2e-5
```

### thirdParty/pybind11/.pre-commit-config.yaml

```yaml
# To use:
#
#     pre-commit run -a
#
# Or:
#
#     pre-commit install  # (runs every time you commit in git)
#
# To update this file:
#
#     pre-commit autoupdate
#
# See https://github.com/pre-commit/pre-commit


ci:
  autoupdate_commit_msg: "chore(deps): update pre-commit hooks"
  autofix_commit_msg: "style: pre-commit fixes"
  autoupdate_schedule: monthly

# third-party content
exclude: ^tools/JoinPaths.cmake$

repos:
# Standard hooks
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: "v4.4.0"
  hooks:
  - id: check-added-large-files
  - id: check-case-conflict
  - id: check-docstring-first
  - id: check-merge-conflict
  - id: check-symlinks
  - id: check-toml
  - id: check-yaml
  - id: debug-statements
  - id: end-of-file-fixer
  - id: mixed-line-ending
  - id: requirements-txt-fixer
  - id: trailing-whitespace

# Upgrade old Python syntax
- repo: https://github.com/asottile/pyupgrade
  rev: "v3.3.1"
  hooks:
  - id: pyupgrade
    args: [--py36-plus]

# Nicely sort includes
- repo: https://github.com/PyCQA/isort
  rev: "5.12.0"
  hooks:
  - id: isort

# Black, the code formatter, natively supports pre-commit
- repo: https://github.com/psf/black
  rev: "23.1.0" # Keep in sync with blacken-docs
  hooks:
  - id: black

# Also code format the docs
- repo: https://github.com/asottile/blacken-docs
  rev: "1.13.0"
  hooks:
  - id: blacken-docs
    additional_dependencies:
    - black==23.1.0 # keep in sync with black hook

# Changes tabs to spaces
- repo: https://github.com/Lucas-C/pre-commit-hooks
  rev: "v1.4.2"
  hooks:
  - id: remove-tabs

- repo: https://github.com/sirosen/texthooks
  rev: "0.5.0"
  hooks:
  - id: fix-ligatures
  - id: fix-smartquotes

# Autoremoves unused imports
- repo: https://github.com/hadialqattan/pycln
  rev: "v2.1.3"
  hooks:
  - id: pycln
    stages: [manual]

# Checking for common mistakes
- repo: https://github.com/pre-commit/pygrep-hooks
  rev: "v1.10.0"
  hooks:
  - id: python-check-blanket-noqa
  - id: python-check-blanket-type-ignore
  - id: python-no-log-warn
  - id: python-use-type-annotations
  - id: rst-backticks
  - id: rst-directive-colons
  - id: rst-inline-touching-normal

# Automatically remove noqa that are not used
- repo: https://github.com/asottile/yesqa
  rev: "v1.4.0"
  hooks:
  - id: yesqa
    additional_dependencies: &flake8_dependencies
      - flake8-bugbear
      - pep8-naming

# Flake8 also supports pre-commit natively (same author)
- repo: https://github.com/PyCQA/flake8
  rev: "6.0.0"
  hooks:
  - id: flake8
    exclude: ^(docs/.*|tools/.*)$
    additional_dependencies: *flake8_dependencies

# PyLint has native support - not always usable, but works for us
- repo: https://github.com/PyCQA/pylint
  rev: "v2.16.1"
  hooks:
  - id: pylint
    files: ^pybind11

# CMake formatting
- repo: https://github.com/cheshirekow/cmake-format-precommit
  rev: "v0.6.13"
  hooks:
  - id: cmake-format
    additional_dependencies: [pyyaml]
    types: [file]
    files: (\.cmake|CMakeLists.txt)(.in)?$

# Check static types with mypy
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: "v0.991"
  hooks:
  - id: mypy
    args: []
    exclude: ^(tests|docs)/
    additional_dependencies: [nox, rich]

# Checks the manifest for missing files (native support)
- repo: https://github.com/mgedmin/check-manifest
  rev: "0.49"
  hooks:
  - id: check-manifest
    # This is a slow hook, so only run this if --hook-stage manual is passed
    stages: [manual]
    additional_dependencies: [cmake, ninja]

# Check for spelling
# Use tools/codespell_ignore_lines_from_errors.py
# to rebuild .codespell-ignore-lines
- repo: https://github.com/codespell-project/codespell
  rev: "v2.2.2"
  hooks:
  - id: codespell
    exclude: ".supp$"
    args: ["-x", ".codespell-ignore-lines"]

# Check for common shell mistakes
- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: "v0.9.0.2"
  hooks:
  - id: shellcheck

# Disallow some common capitalization mistakes
- repo: local
  hooks:
  - id: disallow-caps
    name: Disallow improper capitalization
    language: pygrep
    entry: PyBind|Numpy|Cmake|CCache|PyTest
    exclude: ^\.pre-commit-config.yaml$

# Clang format the codebase automatically
- repo: https://github.com/pre-commit/mirrors-clang-format
  rev: "v15.0.7"
  hooks:
  - id: clang-format
    types_or: [c++, c, cuda]

```

## Python signatures and reward/observation bodies (84 files)


### raisimGymTorch/raisimGymTorch/algo/ppo/module.py

```
class Actor()
    def __init__(self, architecture, distribution, device)
    def sample(self, obs)
    def evaluate(self, obs, actions)
    def parameters(self)
    def noiseless_action(self, obs)
    def save_deterministic_graph(self, file_name, example_input, device)
    def deterministic_parameters(self)
    def update(self)
    def obs_shape(self)
    def action_shape(self)
class Critic()
    def __init__(self, architecture, device)
    def predict(self, obs)
    def evaluate(self, obs)
    def parameters(self)
    def obs_shape(self)
class MLP(Module)
    def __init__(self, shape, actionvation_fn, input_size, output_size)
    def init_weights(sequential, scales)
class MultivariateGaussianDiagonalCovariance(Module)
    def __init__(self, dim, size, init_std, fast_sampler, seed)
    def update(self)
    def sample(self, logits)
    def evaluate(self, logits, outputs)
    def entropy(self)
    def enforce_minimum_std(self, min_std)
```

### raisimGymTorch/raisimGymTorch/algo/ppo/ppo.py

```
class PPO()
    def __init__(self, actor, critic, num_envs, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, learning_rate_schedule, desired_kl, use_clipped_value_loss, log_dir, device, shuffle_batch)
    def act(self, actor_obs)
    def step(self, value_obs, rews, dones)
    def update(self, actor_obs, value_obs, log_this_iteration, update)
    def log(self, variables)
    def _train_step(self, log_this_iteration)
```

### raisimGymTorch/raisimGymTorch/algo/ppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, actor_obs_shape, critic_obs_shape, actions_shape, device)
    def add_transitions(self, actor_obs, critic_obs, actions, mu, sigma, rewards, dones, actions_log_prob)
    def clear(self)
    def compute_returns(self, last_values, critic, gamma, lam)
    def mini_batch_generator_shuffle(self, num_mini_batches)
    def mini_batch_generator_inorder(self, num_mini_batches)
```

### raisimGymTorch/raisimGymTorch/env/RaisimGymVecEnv.py

```
class RaisimGymVecEnv()
    def __init__(self, impl, normalize_ob, seed, clip_obs)
    def seed(self, seed)
    def turn_on_visualization(self)
    def turn_off_visualization(self)
    def start_video_recording(self, file_name)
    def stop_video_recording(self)
    def step(self, action)
    def load_scaling(self, dir_name, iteration, count)
    def save_scaling(self, dir_name, iteration)
    def observe(self, update_statistics)
    def get_reward_info(self)
    def reset(self)
    def close(self)
    def curriculum_callback(self)
    def num_envs(self)

```python
def get_reward_info(self):
        return self.wrapper.getRewardInfo()
```
```

### raisimGymTorch/raisimGymTorch/env/RewardAnalyzer.py

```
class RewardAnalyzer()
    def __init__(self, env, writer)
    def add_reward_info(self, info)
    def analyze_and_plot(self, step)

```python
def add_reward_info(self, info):
        self.data_size += len(info)

        for i in range(len(self.data_tags)):
            for j in range(len(info)):
                self.data_square_sum[i] += info[j][self.data_tags[i]]*info[j][self.data_tags[i]]
                self.data_mean[i] += info[j][self.data_tags[i]]
                self.data_min[i] = min(self.data_min[i], info[j][self.data_tags[i]])
                self.data_max[i] = max(self.data_max[i], info[j][self.data_tags[i]])
```
```

### raisimGymTorch/raisimGymTorch/helper/raisim_gym_helper.py

```
class ConfigurationSaver()
    def __init__(self, log_dir, save_items)
    def data_dir(self)
def tensorboard_launcher(directory_path)
def load_param(weight_path, env, actor, critic, optimizer, data_dir)
```

### raisimGymTorch/raisimGymTorch/stable_baselines3/RaisimSbGymVecEnv.py

```
class RaisimSbGymVecEnv(VecEnv)
    def __init__(self, impl, normalize_ob, seed, clip_obs)
    def seed(self, seed)
    def turn_on_visualization(self)
    def turn_off_visualization(self)
    def start_video_recording(self, file_name)
    def stop_video_recording(self)
    def step_async(self, actions)
    def step_wait(self)
    def env_method(self, method_name)
    def get_attr(self, attr_name, indices)
    def set_attr(self, attr_name, value, indices)
    def load_scaling(self, dir_name, iteration, count)
    def save_scaling(self, dir_name, iteration)
    def observe(self, update_mean)
    def reset(self)
    def close(self)
    def curriculum_callback(self)
    def render(self, mode)
    def env_is_wrapped(self, wrapper_class, indices)
```

### raisimGymTorch/setup.py

```
class CMakeExtension(Extension)
    def __init__(self, name, sourcedir)
class CMakeBuild(build_ext)
    def run(self)
    def build_extension(self, ext)
```

### raisimGymTorch/thirdParty/pybind11/noxfile.py

```
def lint(session)
def tests(session)
def tests_packaging(session)
def docs(session)
def make_changelog(session)
def build(session)
```

### raisimGymTorch/thirdParty/pybind11/pybind11/__main__.py

```
def print_includes()
def main()
```

### raisimGymTorch/thirdParty/pybind11/pybind11/_version.py

```
def _to_int(s)
```

### raisimGymTorch/thirdParty/pybind11/pybind11/commands.py

```
def get_include(user)
def get_cmake_dir()
```

### raisimGymTorch/thirdParty/pybind11/pybind11/setup_helpers.py

```
"""This module provides helpers for C++11+ projects using pybind11.

LICENSE:

Copyright (c) 2016 Wenzel Jakob <wenzel.jakob@epfl.ch>, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other """
class Pybind11Extension(_Extension)
    """Build a C++11+ Extension module with pybind11. This automatically adds the
recommended flags when you init the extension and assumes C++ sources - you
can further modify the options yourself.

The customizations are:

* ``/EHsc`` and ``/bigobj`` on Windows
* ``stdlib=libc++`` on macOS
* ``visibility"""
    def _add_cflags(self, flags)
    def _add_ldflags(self, flags)
    def __init__(self)
    def cxx_std(self)
    def cxx_std(self, level)
def tmp_chdir()
def has_flag(compiler, flag)
def auto_cpp_level(compiler)
class build_ext(_build_ext)
    """Customized build_ext that allows an auto-search for the highest supported
C++ level for Pybind11Extension. This is only needed for the auto-search
for now, and is completely optional otherwise."""
    def build_extensions(self)
def intree_extensions(paths, package_dir)
def naive_recompile(obj, src)
def no_recompile(obg, src)
class ParallelCompile(object)
    """Make a parallel compile function. Inspired by
numpy.distutils.ccompiler.CCompiler_compile and cppimport.

This takes several arguments that allow you to customize the compile
function created:

envvar:
    Set an environment variable to control the compilation threads, like
    NPY_NUM_BUILD_JOBS
de"""
    def __init__(self, envvar, default, max, needs_recompile)
    def function(self)
    def install(self)
    def __enter__(self)
    def __exit__(self)
```

### raisimGymTorch/thirdParty/pybind11/setup.py

```
def build_expected_version_hex(matches)
def get_and_replace(filename, binary)
class SDist(sdist)
    def make_release_tree(self, base_dir, files)
def TemporaryDirectory()
def remove_output()
```

### raisimGymTorch/thirdParty/pybind11/tests/conftest.py

```
"""pytest configuration

Extends output capture as needed by pybind11: ignore constructors, optional unordered lines.
Adds docstring and exceptions message sanitizers: ignore Python 2 vs 3 differences."""
def _strip_and_dedent(s)
def _split_and_sort(s)
def _make_explanation(a, b)
class Output(object)
    """Basic output post-processing and comparison"""
    def __init__(self, string)
    def __str__(self)
    def __eq__(self, other)
class Unordered(Output)
    """Custom comparison for output without strict line ordering"""
    def __eq__(self, other)
class Capture(object)
    def __init__(self, capfd)
    def __enter__(self)
    def __exit__(self)
    def __eq__(self, other)
    def __str__(self)
    def __contains__(self, item)
    def unordered(self)
    def stderr(self)
def capture(capsys)
class SanitizedString(object)
    def __init__(self, sanitizer)
    def __call__(self, thing)
    def __eq__(self, other)
def _sanitize_general(s)
def _sanitize_docstring(thing)
def doc()
def _sanitize_message(thing)
def msg()
def pytest_assertrepr_compare(op, left, right)
def suppress(exception)
def gc_collect()
def pytest_configure()
```

### raisimGymTorch/thirdParty/pybind11/tests/env.py

```
def deprecated_call()
```

### raisimGymTorch/thirdParty/pybind11/tests/extra_python_package/test_files.py

```
def test_build_sdist(monkeypatch, tmpdir)
def test_build_global_dist(monkeypatch, tmpdir)
def tests_build_wheel(monkeypatch, tmpdir)
def tests_build_global_wheel(monkeypatch, tmpdir)
```

### raisimGymTorch/thirdParty/pybind11/tests/extra_setuptools/test_setuphelper.py

```
def test_simple_setup_py(monkeypatch, tmpdir, parallel, std)
def test_intree_extensions(monkeypatch, tmpdir)
def test_intree_extensions_package_dir(monkeypatch, tmpdir)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_async.py

```
def event_loop()
def get_await_result(x)
def test_await(event_loop)
def test_await_missing(event_loop)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_buffers.py

```
def test_from_python()
def test_to_python()
def test_inherited_protocol()
def test_pointer_to_member_fn()
def test_readonly_buffer()
def test_selective_readonly_buffer()
def test_ctypes_array_1d()
def test_ctypes_array_2d()
def test_ctypes_from_buffer()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_builtin_casters.py

```
def test_simple_string()
def test_unicode_conversion()
def test_single_char_arguments()
def test_bytes_to_string()
def test_string_view(capture)
def test_integer_casting()
def test_int_convert()
def test_numpy_int_convert()
def test_tuple(doc)
def test_builtins_cast_return_none()
def test_none_deferred()
def test_void_caster()
def test_reference_wrapper()
def test_complex_cast()
def test_bool_caster()
def test_numpy_bool()
def test_int_long()
def test_void_caster_2()
def test_const_ref_caster()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_call_policies.py

```
def test_keep_alive_argument(capture)
def test_keep_alive_return_value(capture)
def test_alive_gc(capture)
def test_alive_gc_derived(capture)
def test_alive_gc_multi_derived(capture)
def test_return_none(capture)
def test_keep_alive_constructor(capture)
def test_call_guard()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_callbacks.py

```
def test_callbacks()
def test_bound_method_callback()
def test_keyword_args_and_generalized_unpacking()
def test_lambda_closure_cleanup()
def test_cpp_callable_cleanup()
def test_cpp_function_roundtrip()
def test_function_signatures(doc)
def test_movable_object()
def test_python_builtins()
def test_async_callbacks()
def test_async_async_callbacks()
def test_callback_num_times()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_chrono.py

```
def test_chrono_system_clock()
def test_chrono_system_clock_roundtrip()
def test_chrono_system_clock_roundtrip_date()
def test_chrono_system_clock_roundtrip_time(time1, tz, monkeypatch)
def test_chrono_duration_roundtrip()
def test_chrono_duration_subtraction_equivalence()
def test_chrono_duration_subtraction_equivalence_date()
def test_chrono_steady_clock()
def test_chrono_steady_clock_roundtrip()
def test_floating_point_duration()
def test_nano_timepoint()
def test_chrono_different_resolutions()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_class.py

```
def test_repr()
def test_instance(msg)
def test_instance_new(msg)
def test_type()
def test_type_of_py()
def test_type_of_classic()
def test_type_of_py_nodelete()
def test_as_type_py()
def test_docstrings(doc)
def test_qualname(doc)
def test_inheritance(msg)
def test_inheritance_init(msg)
def test_automatic_upcasting()
def test_isinstance()
def test_mismatched_holder()
def test_override_static()
def test_implicit_conversion_life_support()
def test_operator_new_delete(capture)
def test_bind_protected_functions()
def test_brace_initialization()
def test_class_refcount()
def test_reentrant_implicit_conversion_failure(msg)
def test_error_after_conversions()
def test_aligned()
def test_final()
def test_non_final_final()
def test_exception_rvalue_abort()
def test_multiple_instances_with_same_pointer(capture)
def test_base_and_derived_nested_scope()
def test_register_duplicate_class()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_const_name.py

```
def test_const_name(func, selector, expected)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_constants_and_functions.py

```
def test_constants()
def test_function_overloading()
def test_bytes()
def test_exception_specifiers()
def test_function_record_leaks()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_copy_move.py

```
def test_lacking_copy_ctor()
def test_lacking_move_ctor()
def test_move_and_copy_casts()
def test_move_and_copy_loads()
def test_move_and_copy_load_optional()
def test_private_op_new()
def test_move_fallback()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_custom_type_casters.py

```
def test_noconvert_args(msg)
def test_custom_caster_destruction()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_custom_type_setup.py

```
def gc_tester()
def test_self_cycle(gc_tester)
def test_indirect_cycle(gc_tester)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_docstring_options.py

```
def test_docstring_options()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_eigen.py

```
def assert_equal_ref(mat)
def assert_sparse_equal_ref(sparse_mat)
def test_fixed()
def test_dense()
def test_partially_fixed()
def test_mutator_descriptors()
def test_cpp_casting()
def test_pass_readonly_array()
def test_nonunit_stride_from_python()
def test_negative_stride_from_python(msg)
def test_nonunit_stride_to_python()
def test_eigen_ref_to_python()
def assign_both(a1, a2, r, c, v)
def array_copy_but_one(a, r, c, v)
def test_eigen_return_references()
def assert_keeps_alive(cl, method)
def test_eigen_keepalive()
def test_eigen_ref_mutators()
def test_numpy_ref_mutators()
def test_both_ref_mutators()
def test_nocopy_wrapper()
def test_eigen_ref_life_support()
def test_special_matrix_objects()
def test_dense_signature(doc)
def test_named_arguments()
def test_sparse()
def test_sparse_signature(doc)
def test_issue738()
def test_issue1105()
def test_custom_operator_new()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_embed/test_interpreter.py

```
class DerivedWidget(Widget)
    def __init__(self, message)
    def the_answer(self)
    def argv0(self)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_embed/test_trampoline.py

```
def func()
def func2()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_enum.py

```
def test_unscoped_enum()
def test_scoped_enum()
def test_implicit_conversion()
def test_binary_operators()
def test_enum_to_int()
def test_duplicate_enum_name()
def test_char_underlying_enum()
def test_bool_underlying_enum()
def test_docstring_signatures()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_eval.py

```
def test_evals(capture)
def test_eval_file()
def test_eval_empty_globals()
def test_eval_closure()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_exceptions.py

```
def test_std_exception(msg)
def test_error_already_set(msg)
def test_raise_from(msg)
def test_raise_from_already_set(msg)
def test_cross_module_exceptions(msg)
def test_cross_module_exception_translator()
def test_python_call_in_catch()
def ignore_pytest_unraisable_warning(f)
def test_python_alreadyset_in_destructor(monkeypatch, capsys)
def test_exception_matches()
def test_custom(msg)
def test_nested_throws(capture)
def test_invalid_repr()
def test_local_translator(msg)
```

### raisimGymTorch/thirdParty/pybind11/tests/test_factory_constructors.py

```
def test_init_factory_basic()
def test_init_factory_signature(msg)
def test_init_factory_casting()
def test_init_factory_alias()
def test_init_factory_dual()
def test_no_placement_new(capture)
def test_multiple_inheritance()
def create_and_destroy()
def strip_comments(s)
def test_reallocation_a(capture, msg)
def test_reallocation_b(capture, msg)
def test_reallocation_c(capture, msg)
def test_reallocation_d(capture, msg)
def test_reallocation_e(capture, msg)
def test_reallocation_f(capture, msg)
def test_reallocation_g(capture, msg)
def test_invalid_self()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_gil_scoped.py

```
def _run_in_process(target)
def _python_to_cpp_to_python()
def _python_to_cpp_to_python_from_threads(num_threads, parallel)
def test_python_to_cpp_to_python_from_thread()
def test_python_to_cpp_to_python_from_thread_multiple_parallel()
def test_python_to_cpp_to_python_from_thread_multiple_sequential()
def test_python_to_cpp_to_python_from_process()
def test_cross_module_gil()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_iostream.py

```
def test_captured(capsys)
def test_captured_large_string(capsys)
def test_captured_utf8_2byte_offset0(capsys)
def test_captured_utf8_2byte_offset1(capsys)
def test_captured_utf8_3byte_offset0(capsys)
def test_captured_utf8_3byte_offset1(capsys)
def test_captured_utf8_3byte_offset2(capsys)
def test_captured_utf8_4byte_offset0(capsys)
def test_captured_utf8_4byte_offset1(capsys)
def test_captured_utf8_4byte_offset2(capsys)
def test_captured_utf8_4byte_offset3(capsys)
def test_guard_capture(capsys)
def test_series_captured(capture)
def test_flush(capfd)
def test_not_captured(capfd)
def test_err(capfd)
def test_multi_captured(capfd)
def test_dual(capsys)
def test_redirect(capfd)
def test_redirect_err(capfd)
def test_redirect_both(capfd)
def test_threading()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_kwargs_and_defaults.py

```
def test_function_signatures(doc)
def test_named_arguments(msg)
def test_arg_and_kwargs()
def test_mixed_args_and_kwargs(msg)
def test_keyword_only_args(msg)
def test_positional_only_args(msg)
def test_signatures()
def test_args_refcount()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_local_bindings.py

```
def test_load_external()
def test_local_bindings()
def test_nonlocal_failure()
def test_duplicate_local()
def test_stl_bind_local()
def test_stl_bind_global()
def test_mixed_local_global()
def test_internal_locals_differ()
def test_stl_caster_vs_stl_bind(msg)
def test_cross_module_calls()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_methods_and_attributes.py

```
def test_methods_and_attributes()
def test_copy_method()
def test_properties()
def test_static_properties()
def test_static_cls()
def test_metaclass_override()
def test_no_mixed_overloads()
def test_property_return_value_policies(access)
def test_property_rvalue_policy()
def test_dynamic_attributes()
def test_cyclic_gc()
def test_bad_arg_default(msg)
def test_accepts_none(msg)
def test_casts_none()
def test_str_issue(msg)
def test_unregistered_base_implementations()
def test_ref_qualified()
def test_overload_ordering()
def test_rvalue_ref_param()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_modules.py

```
def test_nested_modules()
def test_reference_internal()
def test_importing()
def test_pydoc()
def test_duplicate_registration()
def test_builtin_key_type()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_multiple_inheritance.py

```
def test_multiple_inheritance_cpp()
def test_multiple_inheritance_mix1()
def test_multiple_inheritance_mix2()
def test_multiple_inheritance_python()
def test_multiple_inheritance_python_many_bases()
def test_multiple_inheritance_virtbase()
def test_mi_static_properties()
def test_mi_dynamic_attributes()
def test_mi_unaligned_base()
def test_mi_base_return()
def test_diamond_inheritance()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_array.py

```
def test_dtypes()
def arr()
def test_array_attributes()
def test_index_offset(arr, args, ret)
def test_dim_check_fail(arr)
def test_data(arr, args, ret)
def test_at_fail(arr, dim)
def test_at(arr)
def test_mutate_readonly(arr)
def test_mutate_data(arr)
def test_bounds_check(arr)
def test_make_c_f_array()
def test_make_empty_shaped_array()
def test_wrap()
def test_numpy_view(capture)
def test_cast_numpy_int64_to_uint64()
def test_isinstance()
def test_constructors()
def test_overload_resolution(msg)
def test_greedy_string_overload()
def test_array_unchecked_fixed_dims(msg)
def test_array_unchecked_dyn_dims()
def test_array_failure()
def test_initializer_list()
def test_array_resize()
def test_array_create_and_resize()
def test_array_view()
def test_array_view_invalid()
def test_reshape_initializer_list()
def test_reshape_tuple()
def test_index_using_ellipsis()
def test_format_descriptors_for_floating_point_types(test_func)
def test_argument_conversions(forcecast, contiguity, noconvert)
def test_dtype_refcount_leak()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_dtypes.py

```
def simple_dtype()
def packed_dtype()
def dt_fmt()
def simple_dtype_fmt()
def packed_dtype_fmt()
def partial_ld_offset()
def partial_dtype_fmt()
def partial_nested_fmt()
def assert_equal(actual, expected_data, expected_dtype)
def test_format_descriptors()
def test_dtype(simple_dtype)
def test_recarray(simple_dtype, packed_dtype)
def test_array_constructors()
def test_string_array()
def test_array_array()
def test_enum_array()
def test_complex_array()
def test_signature(doc)
def test_scalar_conversion()
def test_vectorize()
def test_cls_and_dtype_conversion(simple_dtype)
def test_register_dtype()
def test_str_leak()
def test_compare_buffer_info()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_numpy_vectorize.py

```
def test_vectorize(capture)
def test_type_selection()
def test_docs(doc)
def test_trivial_broadcasting()
def test_passthrough_arguments(doc)
def test_method_vectorization()
def test_array_collapse()
def test_vectorized_noreturn()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_opaque_types.py

```
def test_string_list()
def test_pointers(msg)
def test_unions()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_operator_overloading.py

```
def test_operator_overloading()
def test_operators_notimplemented()
def test_nested()
def test_overriding_eq_reset_hash()
def test_return_set_of_unhashable()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_pickling.py

```
def test_roundtrip(cls_name)
def test_roundtrip_with_dict(cls_name)
def test_enum_pickle()
class SimplePyDerived(SimpleBase)
def test_roundtrip_simple_py_derived()
def test_roundtrip_simple_cpp_derived()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_pytypes.py

```
def test_int(doc)
def test_iterator(doc)
def test_iterable(doc)
def test_list(capture, doc)
def test_none(capture, doc)
def test_set(capture, doc)
def test_dict(capture, doc)
def test_tuple()
def test_simple_namespace()
def test_str(doc)
def test_bytes(doc)
def test_bytearray(doc)
def test_capsule(capture)
def test_accessors()
def test_constructors()
def test_non_converting_constructors()
def test_pybind11_str_raw_str()
def test_implicit_casting()
def test_print(capture)
def test_hash()
def test_number_protocol()
def test_list_slicing()
def test_issue2361()
def test_memoryview(method, args, fmt, expected_view)
def test_memoryview_refcount(method)
def test_memoryview_from_buffer_empty_shape()
def test_test_memoryview_from_buffer_invalid_strides()
def test_test_memoryview_from_buffer_nullptr()
def test_memoryview_from_memory()
def test_builtin_functions()
def test_isinstance_string_types()
def test_pass_bytes_or_unicode_to_string_types()
def test_weakref(create_weakref, create_weakref_with_callback)
def test_cpp_iterators()
def test_implementation_details()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_sequences_and_iterators.py

```
def isclose(a, b, rel_tol, abs_tol)
def allclose(a_list, b_list, rel_tol, abs_tol)
def test_slice_constructors()
def test_slice_constructors_explicit_optional()
def test_generalized_iterators()
def test_nonref_iterators()
def test_generalized_iterators_simple()
def test_iterator_referencing()
def test_sliceable()
def test_sequence()
def test_sequence_length()
def test_map_iterator()
def test_python_iterator_in_cpp()
def test_iterator_passthrough()
def test_iterator_rvp()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_smart_ptr.py

```
def test_smart_ptr(capture)
def test_smart_ptr_refcounting()
def test_unique_nodelete()
def test_unique_nodelete4a()
def test_unique_deleter()
def test_large_holder()
def test_shared_ptr_and_references()
def test_shared_ptr_from_this_and_references()
def test_move_only_holder()
def test_holder_with_addressof_operator()
def test_move_only_holder_with_addressof_operator()
def test_smart_ptr_from_default()
def test_shared_ptr_gc()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_stl.py

```
def test_vector(doc)
def test_deque(doc)
def test_array(doc)
def test_valarray(doc)
def test_map(doc)
def test_set(doc)
def test_recursive_casting()
def test_move_out_container()
def test_optional()
def test_exp_optional()
def test_boost_optional()
def test_reference_sensitive_optional()
def test_fs_path()
def test_variant(doc)
def test_vec_of_reference_wrapper()
def test_stl_pass_by_pointer(msg)
def test_missing_header_message()
def test_function_with_string_and_vector_string_arg()
def test_stl_ownership()
def test_array_cast_sequence()
def test_issue_1561()
def test_return_vector_bool_raw_ptr()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_stl_binders.py

```
def test_vector_int()
def test_vector_buffer()
def test_vector_buffer_numpy()
def test_vector_bool()
def test_vector_custom()
def test_map_string_double()
def test_map_string_double_const()
def test_noncopyable_containers()
def test_map_delitem()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_tagbased_polymorphic.py

```
def test_downcast()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_thread.py

```
class Thread(Thread)
    def __init__(self, fn)
    def run(self)
    def join(self)
def test_implicit_conversion()
def test_implicit_conversion_no_gil()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_union.py

```
def test_union()
```

### raisimGymTorch/thirdParty/pybind11/tests/test_virtual_functions.py

```
def test_override(capture, msg)
def test_alias_delay_initialization1(capture)
def test_alias_delay_initialization2(capture)
def test_move_support()
def test_dispatch_issue(msg)
def test_recursive_dispatch_issue(msg)
def test_override_ref()
def test_inherited_virtuals()
def test_issue_1454()
def test_python_override()
```

### thirdParty/pybind11/tests/env.py

```
def deprecated_call()
```