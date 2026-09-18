# isaac_sim_2026

source: https://github.com/isaac-sim/IsaacSim


commit: 7c206f75bdadd9e05fc457f19863ca4c3f0cb693


## README

![Isaac Sim](docs/readme/hero_shot_compressed.png)

---
# Isaac Sim

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://docs.python.org/3/whatsnew/3.12.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/22.04/)
[![Linux aarch64 platform](https://img.shields.io/badge/platform-linux--aarch64-orange.svg)](https://docs.nvidia.com/dgx/dgx-os-7-user-guide/introduction.html)
[![Windows platform](https://img.shields.io/badge/platform-windows--64-orange.svg)](https://www.microsoft.com/en-us/)
[![License](https://img.shields.io/badge/license-Apache--2.0-yellow.svg)](LICENSE)

NVIDIA Isaac Sim™ is a simulation platform built on NVIDIA Omniverse, designed to develop, test, train, and deploy AI-powered robots in realistic virtual environments. It supports importing robotic systems from common formats such as URDF, MJCF, and CAD. The simulator leverages high-fidelity, GPU-accelerated physics engines to simulate accurate dynamics and support multi-sensor RTX rendering at scale. It comes equipped with end-to-end workflows including synthetic data generation, reinforcement learning, ROS integration, and digital twin simulation. Isaac Sim provides the infrastructure needed to support robotics development at any stage.

## Key Features

- [Asset Import & Export](https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/importers_exporters.html): Importing and exporting robots and environments from and to non-USD format.
- [Robot Tuning](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/index.html): Optimize robot for physics accuracy, computation efficiency, or photorealism
- [Robot Simulation](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html): Tools for moving robots, such as controllers, motion generation and kinematics solvers, and policy integration.
- [Sensors](https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html): RTX and physics-based sensors

## Key Applications

- [Isaac Lab](https://docs.isaacsim.omniverse.nvidia.com/latest/isaac_lab_tutorials/index.html): GPU-accelerated framework built for reinforcement learning, imitation learning, and motion planning.
- [ROS Bridge](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/ros2_landing_page.html): Integration with Robot Operating System (ROS).
- [Synthetic Data Generation](https://docs.isaacsim.omniverse.nvidia.com/latest/synthetic_data_generation/index.html): Collection of SDG tools

## Documentation

For the latest Isaac Sim documentation, see [Isaac Sim Documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html).
Follow these links to get started:

- [Tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_index.html)
- [Assets](https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_overview.html)


## Prerequisites and Environment Setup

Ensure your system is set up with the following before building Isaac Sim:

- **Operating System**: Windows 11 or Linux (Ubuntu 22.04/24.04)

  > **(Linux) Ubuntu 24.04**
  > Building with Ubuntu 24.04 requires GCC/G++ 11 to be installed, GCC/G++ 12+ is not supported.

- **GPU**: For additional information on GPU features and requirements, see [NVIDIA GPU Requirements](https://docs.omniverse.nvidia.com/dev-guide/latest/common/technical-requirements.html)

  #### Local Workstation

  | Min | Recommended | Best |
  |-----|-------------|------|
  | RTX 4080 | RTX 5080 | RTX PRO 6000 Blackwell Workstation |
  |  | RTX 5880 Ada | RTX PRO 5000 Blackwell Workstation |

  #### Datacenter

  | Min | Recommended | Best |
  |-----|-------------|------|
  | A40 | L40S | RTX PRO 6000 Blackwell Server |
  |  | L20 | |

- **Driver**: See [NVIDIA Driver Requirements](https://docs.omniverse.nvidia.com/dev-guide/latest/common/technical-requirements.html)

- **Internet Access**: Required for downloading the Omniverse Kit SDK, extensions, and tools. Allow outbound HTTPS
  access to `ovextensionsprod.blob.core.windows.net` so the build can resolve public Kit and Isaac Sim extensions.



### Required Software Dependencies

- [**Git**](https://git-scm.com/downloads): For version control and repository management

- [**Git LFS**](https://git-lfs.com/): For managing large files within the repository

- **(Windows - C++ Only) Microsoft Visual Studio 2022**:

- Install Visual Studio 2022, Windows SDK, and MSVC using Winget by running the following command in PowerShell:

  ```powershell
  winget install --id=Microsoft.VisualStudio.2022.Community -e --override "--add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended"
  ```
  
  [Additional information on Windows development configuration](docs/readme/windows_developer_configuration.md)


- **(Linux) build-essentials**: A package that includes `make` and other essential tools for building applications.  For Ubuntu, install with:

  ```bash
  sudo apt-get install build-essential
  ```

  > **(Linux) ⚠️**
  > Please use GCC/G++ 11, higher versions are not supported yet. To install GCC/G++ 11, run the following commands:
  > ```bash
  > sudo apt-get install gcc-11 g++-11
  > sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 200
  > sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 200
  > ```

  > **(Linux aarch64) ⚠️**
  > On aarch64 hosts (e.g. DGX Spark), X11 development headers are required to build Python packages that lack pre-built wheels:
  > ```bash
  > sudo apt-get install -y libx11-dev xorg-dev
  > ```

  > **Compiler Version Check ⚠️**
  > We have added a version checker to our build process. If you do not have the default versions you are still able to execute a build, add  `--skip-compiler-version-check` to `build.[sh/bat]` when building.  Proceed at your own risk, unsupported build environments may encounter build and runtime issues.

### Recommended Software

- [**(Linux) Docker**](https://docs.docker.com/engine/install/ubuntu/): For containerized development and deployment. **Ensure non-root users have Docker permissions.**

- [**(Linux) NVIDIA Container Toolkit**](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html): For GPU-accelerated containerized development and deployment. **Installation and Configuring Docker steps are required.**

- [**VSCode**](https://code.visualstudio.com/download) (or your preferred IDE): For code editing and development

## Quick Start

This section guides you through building Isaac Sim from source code.

### 1. Clone the Repository


```bash
git clone -b main https://github.com/isaac-sim/IsaacSim.git isaacsim
cd isaacsim
git lfs install
git lfs pull
```

### 2. Build

Run the following command to initiate the configuration wizard:

**Linux:**

Confirm that GCC/G++ 11 is being used before building using the following commands:

```bash
gcc --version
g++ --version
```

```bash
./build.sh
```

**Windows:**

> **⚠️ Windows Path Length Limitation**
> Windows has a path length limitation of 260 characters. If you encounter errors related missing files or other build errors, try moving the repository to a shorter path.

```powershell
build.bat
```

### 3. Run

> **⚠️ Startup Time**
> The first time loading Isaac Sim may take up to several minutes as Extensions and Shader are loaded and cached. The subsequent startup time should be in the ranges of 10-30 seconds depending on hardware configuration.



Navigate to the corresponding binary directory for your platform and run the executable.

**Linux (x86_64):**
```bash
cd _build/linux-x86_64/release
./isaac-sim.sh
```

**Linux (aarch64):**
```bash
cd _build/linux-aarch64/release
./isaac-sim.sh
```

**Windows:**
```powershell
cd _build/windows-x86_64/release
isaac-sim.bat
```

> NOTE: If this is your first time building Isaac Sim, you will be prompted to accept the Omniverse Licensing Terms.



## Advanced Build Options


Isaac Sim uses a custom build system with the following key options:


### Core Build Options
- `-c, --clean`: Clean the repository and exit
- `-x, --rebuild`: Clean the repository before building (full rebuild)
- `-h, --help`: Show all available build options


### Configuration Options
- `--config [debug|release]`: Specify build configuration (default: both)
- `-d, --debug`: Build only debug configuration
- `-r, --release`: Build only release configuration


### Advanced Options
- `-j NUM_CORES, --jobs NUM_CORES`: Limit the number of parallel compilation jobs
- `-v, --verbose`: Enable verbose build output
- `-q, --quiet`: Suppress build output


### Build Steps Control
- `--fetch-only`: Only fetch dependencies and stop
- `-g, --generate`: Generate projects, stage files and stop
- `-s, --stage`: Stage files, skip generation step
- `-b, --build-only`: Only perform building step, skip others
- `--post-build-only`: Only perform post-build step

## Usage
Congratulations on installing Isaac Sim! To get started with using Isaac Sim, follow these [Quick Tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_index.html). For more information, visit our full [documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html).

## Additional Build Tools

Beyond building and running from source (see [Quick Start](#quick-start)), Isaac Sim can also be packaged as a standalone binary archive, built as Python wheels, or deployed as a Docker container.

### Binary Package

Build a standalone redistributable binary package from source. A successful [build](#quick-start) is required before packaging.

**Linux:**

```bash
./repo.sh package --config release -m isaac-sim-standalone
```

> **Note:** The same command works on both x86_64 and aarch64 hosts. The build system detects the platform automatically.

**Windows:**

```powershell
.\repo.bat package --config release -m isaac-sim-standalone
```

The packaged archive is written to the `_build/packages/` directory.

### PIP Packages

Build Isaac Sim Python (PIP) wheels locally from a successful [build](#quick-start). Pre-built wheels for released versions are also available on [pypi.nvidia.com](https://pypi.nvidia.com); see [Install Isaac Sim using PIP](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_python.html#installation-using-pip) for the install-only path.

A successful [build](#quick-start) is required before packaging.

**Linux:**

```bash
./repo.sh python_package --create
./repo.sh comment_archive_deps
./repo.sh python_package --wheel
```

**Windows:**

```powershell
.\repo.bat python_package --create
.\repo.bat comment_archive_deps
.\repo.bat python_package --wheel
```

The three steps, in order:

1. `python_package --create` stages per-package source trees under `_build/packages/python/` from the wheel definitions in [python_packages.toml](python_packages.toml).
2. `comment_archive_deps` comments out references to Kit pip-archive extensions (`omni.kit.pip_archive`, `omni.isaac.core_archive`, `omni.isaac.ml_archive`, `omni.pip.compute`, `omni.pip.cloud`, `isaacsim.pip.newton`, `isaacsim.pip.nv`, `isaacsim.pip.onnx`) in the generated `extension.toml` and `*.kit` files so wheel metadata is self-contained.
3. `python_package --wheel` builds the `.whl` files into `_build/packages/dist/`.

Install locally-built wheels into a Python 3.12 virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install _build/packages/dist/*.whl
```

> **(Linux aarch64) ⚠️**
> On aarch64 hosts, X11 development headers are required to build transitive Python dependencies that lack pre-built aarch64 wheels (same note as under [Prerequisites and Environment Setup](#prerequisites-and-environment-setup)):
> ```bash
> sudo apt-get install -y libx11-dev xorg-dev
> ```

### Container (Docker)

For building a Docker image, running with Docker Compose, and web-based streaming, see [tools/docker/README.md](tools/docker/README.md).


## Troubleshooting

- Please see the [FAQ](https://docs.isaacsim.omniverse.nvidia.com/latest/overview/faq_index.html), [Troubleshooting](https://docs.isaacsim.omniverse.nvidia.com/latest/overview/troubleshooting.html), and [Known Issues](https://docs.isaacsim.omniverse.nvidia.com/latest/overview/known_issues.html) for common questions, fixes, and workarounds.

- On Linux, if you encounter network connectivity issues when building (such as corporate firewalls), run the following commands:

  ```bash
  export http_proxy="http://{Your IP address}:7890"
  export https_proxy="http://{Your IP address}:7890"
  ```

  - Use these variables only when you use proxy software or are behind a corporate firewall. Replace port 7890 with
    the port used by your proxy.

- If dependency resolution reports `found 0 packages` for a public registry such as `kit/prod/sdk` and exits with
  code 55, verify that the build process can reach `ovextensionsprod.blob.core.windows.net` through your firewall or
  proxy. Reaching the host with a browser or a separate command-line client does not confirm that the build inherited
  the same proxy settings.


## Support

* Please use GitHub [Discussions](https://github.com/isaac-sim/IsaacSim/discussions) for discussing ideas, asking questions, and requests for new features.
* Github [Issues](https://github.com/isaac-sim/IsaacSim/issues) should only be used to track executable pieces of work with a definite scope and a clear deliverable. These can be fixing bugs, documentation issues, new features, or general updates.

## Connect with the NVIDIA Omniverse Community

Have a project or resource you'd like to share more widely? We'd love to hear from you! Reach out to the
NVIDIA Omniverse Community team at OmniverseCommunity@nvidia.com to discuss potential opportunities
for broader dissemination of your work.

## License

Licensing terms can be found in the [License File](LICENSE).

## Citation

To cite Isaac Sim, click on "Cite this repository" in the right sidebar of the [Isaac Sim GitHub repository](https://github.com/isaac-sim/IsaacSim) landing page and select one of the listed citation entries.

## Contributing

We do not support direct community contributions at the moment.


## File tree (depth 3, assets pruned)

```
.clang-format
.claude/
  skills/
    action-and-event-data-generation/
    actor-sdg-generate-lighting-variations/
    actor-sdg-sweep-config/
    behavior-tree-generation/
    calibrate-metropolis-camera/
    data-collection-sim/
    generate-incident-config/
    isaac-camera/
    isaac-sim-assets/
    isaac-sim-headless-deployment/
    isaac-sim-installation/
    isaac-sim-migration/
    isaac-sim-orchestrator/
    isaac-sim-remote/
    isaac-sim-rendering/
    isaac-sim-robot-navigation/
    isaac-sim-ros-workspaces/
    isaac-sim-ros2-bridge/
    isaac-sim-sensor/
    isaac-sim-troubleshooting/
    isaac-sim-validator/
    isaac-sim-workflow/
    manipulation-ik/
    meta-skills/
    mobility-gen/
    motion-generation/
    navigation-primitives/
    object-bin-packing/
    occupancy-map/
    physics-simulation/
    place-camera-aim-at/
    place-camera-max-coverage/
    profile-isaac-sim/
    run-incident-events/
    skill-distillation/
    skills-eval-triage/
    spatial-reasoning/
    urdf-mjcf-to-usd-conversion/
    usd-articulation/
    usd-composition-architecture/
    usd-pipeline/
    validation-diff-gifs/
    vlm-scene-captioning/
.coveragerc
.cursor/
  rules/
    agent_skills.mdc
    build_instructions.mdc
    c_codestyle.mdc
    c_docstrings.mdc
    changelog_md.mdc
    cmake_codestyle.mdc
    cpp_codestyle.mdc
    cpp_docstrings.mdc
    documentation_policy.mdc
    extension_structure.mdc
    extension_toml.mdc
    follow_symlinks.mdc
    modules_changelog.mdc
    modules_docs.mdc
    overview_md.mdc
    pip_packaging.mdc
    python_codestyle.mdc
    python_docstrings.mdc
    test_instructions.mdc
    usd_prefer_experimental_api.mdc
.cursorignore
.editorconfig
.flake8
.gitattributes
.github/
  ISSUE_TEMPLATE/
    bug_report.yml
    config.yml
  actionlint.yml
  copy-pr-bot.yaml
  workflows/
    build-cov.yml
    build.yml
    checks.yml
    ci.yml
    combine-coverage.yml
    pr-checks.yml
    test.yml
.gitignore
.vscode/
  c_cpp_properties.json
  extensions.json
  launch.json
  settings.template.json
  tasks.json
AGENTS.md
CITATION.cff
CLAUDE.md
CONTRIBUTING.md
CONTRIBUTING_PATHS.md
LICENSE
README.md
SECURITY.md
THIRD_PARTY_NOTICE.md
VERSION
build.bat
build.sh
deps/
  ext-deps.packman.xml
  isaac-sim.packman.xml
  isaacsim-libraries.packman.xml
  kit-sdk-deps.packman.xml
  kit-sdk.packman.xml
  kit-sdk.packman.xml.user_
  omni-physics.packman.xml
  pip.toml
  pip_cloud.toml
  pip_compute.toml
  pip_cumotion.toml
  pip_episode_recorder.toml
  pip_lula.toml
  pip_ml.toml
  pip_newton.toml
  pip_nv.toml
  pip_onnx.toml
  pip_pink.toml
  pip_simready.toml
  pip_sysid_telemetry.toml
  pip_teleop.toml
  pip_ucx.toml
  pip_urdf_usd.toml
  pip_zmq.toml
  recipes/
    doctest/
    ovphysx-sdk/
    sdl3/
    stb/
  repo-deps.packman.xml
docker_package.toml
format_code.bat
format_code.sh
greptile.json
licenses/
  absl-py-2.4.0.txt
  aioboto3-14.1.0.txt
  aioboto3-15.0.0.txt
  aioboto3-15.5.0.txt
  aiobotocore-2.22.0.txt
  aiobotocore-2.23.0.txt
  aiobotocore-2.25.1.txt
  aiodns-3.1.1.txt
  aiodocker-0.21.0.txt
  aiofiles-23.2.1.txt
  aiofiles-25.1.0.txt
  aiohappyeyeballs-2.4.4.txt
  aiohappyeyeballs-2.6.1.txt
  aiohappyeyeballs-2.6.2.txt
  aiohappyeyeballs-2.7.1.txt
  aiohttp-3.10.11.txt
  aiohttp-3.13.5.txt
  aiohttp-3.14.1.txt
  aiohttp-3.14.2.txt
  aiohttp-3.9.5.txt
  aioitertools-0.11.0.txt
  aioitertools-0.13.0.txt
  aioitertools-0.8.0.txt
  aiokafka-0.9.0.txt
  aiomysql-0.3.0.txt
  aioredis-2.0.0.txt
  aioredis-2.0.1.txt
  aiosignal-1.3.2.txt
  aiosignal-1.4.0.txt
  aiosqlite-0.19.0.txt
  altgraph-0.17.4.txt
  annotated-doc-0.0.4.txt
  annotated-doc-0.0.5.txt
  annotated-types-0.7.0.txt
  annotated-types-0.8.0.txt
  antlr4-python3-runtime-4.9.3.txt
  anyio-4.13.0.txt
  anyio-4.14.1.txt
  anyio-4.14.2.txt
  asteval-1.0.6.txt
  async-timeout-4.0.2.txt
  async-timeout-4.0.3.txt
  async-timeout-5.0.1.txt
  asyncpg-0.30.0.txt
  atomicwrites-1.4.0.txt
  attrs-21.4.0.txt
  attrs-23.1.0.txt
  attrs-25.1.0.txt
  attrs-26.1.0.txt
  autocommand-2.2.2.txt
  awscrt-0.23.8.txt
  azure-core-1.38.0.txt
  azure-core-1.41.0.txt
  azure-identity-1.13.0.txt
  azure-storage-blob-12.17.0.txt
  azure-storage-blob-12.30.0.txt
  backports-tarfile-1.2.0.txt
  blobfile-3.2.0.txt
  boto3-1.38.19.txt
  boto3-1.38.27.txt
  boto3-1.40.61.txt
  boto3-1.42.58.txt
  botocore-1.38.19.txt
  botocore-1.38.27.txt
  botocore-1.40.61.txt
  botocore-1.42.97.txt
  bytecode-0.13.0.dev0.txt
  cargo-addr2line-0.22.0.txt
  cargo-adler-1.0.2.txt
  cargo-ahash-0.7.8.txt
  cargo-aho-corasick-1.1.3.txt
  cargo-android-system-properties-0.1.5.txt
  cargo-android-tzdata-0.1.1.txt
  cargo-anes-0.1.6.txt
  cargo-anstream-0.6.15.txt
  cargo-anstyle-1.0.8.txt
  cargo-anstyle-parse-0.2.5.txt
  cargo-anstyle-query-1.1.1.txt
  cargo-anstyle-wincon-3.0.4.txt
  cargo-anyhow-1.0.86.txt
  cargo-assert-matches-1.5.0.txt
  cargo-async-compression-0.3.15.txt
  cargo-async-trait-0.1.81.txt
  cargo-async-zip-0.0.11.txt
  cargo-atomic-waker-1.1.2.txt
  cargo-atty-0.2.14.txt
  cargo-autocfg-1.3.0.txt
  cargo-axum-0.7.5.txt
  cargo-axum-core-0.4.3.txt
  cargo-axum-macros-0.4.1.txt
  cargo-backtrace-0.3.73.txt
  cargo-base64-0.13.1.txt
  cargo-base64-0.22.1.txt
  cargo-bincode-1.3.3.txt
  cargo-bitflags-1.3.2.txt
  cargo-bitflags-2.6.0.txt
  cargo-block-buffer-0.10.4.txt
  cargo-bumpalo-3.16.0.txt
  cargo-bytemuck-1.16.3.txt
  cargo-bytemuck-derive-1.7.0.txt
  cargo-byteorder-1.5.0.txt
  cargo-bytes-1.7.0.txt
  cargo-bytesize-1.3.0.txt
  cargo-cast-0.3.0.txt
  cargo-cbindgen-0.26.0.txt
  cargo-cc-1.1.7.txt
  cargo-cfg-aliases-0.2.1.txt
  cargo-cfg-if-1.0.0.txt
  cargo-chrono-0.4.38.txt
  cargo-ciborium-0.2.2.txt
  cargo-ciborium-io-0.2.2.txt
  cargo-ciborium-ll-0.2.2.txt
  cargo-clap-3.2.25.txt
  cargo-clap-4.5.13.txt
  cargo-clap-builder-4.5.13.txt
  cargo-clap-derive-4.5.13.txt
  cargo-clap-lex-0.2.4.txt
  cargo-clap-lex-0.7.2.txt
  cargo-clap-num-1.1.1.txt
  cargo-colorchoice-1.0.2.txt
  cargo-config-0.13.4.txt
  cargo-core-foundation-sys-0.8.6.txt
  cargo-cpufeatures-0.2.12.txt
  cargo-crc32fast-1.4.2.txt
  cargo-criterion-0.5.1.txt
  cargo-criterion-plot-0.5.0.txt
  cargo-crossbeam-channel-0.5.13.txt
  cargo-crossbeam-deque-0.8.5.txt
  cargo-crossbeam-epoch-0.9.18.txt
  cargo-crossbeam-utils-0.8.20.txt
  cargo-crunchy-0.2.2.txt
  cargo-crypto-common-0.1.6.txt
  cargo-curl-0.4.46.txt
  cargo-curl-sys-0.4.74+curl-8.9.0.txt
  cargo-dashmap-6.0.1.txt
  cargo-deranged-0.3.11.txt
  cargo-digest-0.10.7.txt
  cargo-dlv-list-0.3.0.txt
  cargo-educe-0.5.11.txt
  cargo-either-1.13.0.txt
  cargo-enum-ordinalize-4.3.0.txt
  cargo-enum-ordinalize-derive-4.3.1.txt
  cargo-env-filter-0.1.2.txt
  cargo-env-logger-0.11.5.txt
  cargo-equivalent-1.0.1.txt
  cargo-errno-0.3.9.txt
  cargo-etcetera-0.8.0.txt
  cargo-fastrand-2.1.0.txt
  cargo-fd-lock-4.0.2.txt
  cargo-file-rotate-0.7.6.txt
  cargo-flate2-1.0.30.txt
  cargo-flume-0.11.0.txt
  cargo-fnv-1.0.7.txt
  cargo-form-urlencoded-1.2.1.txt
  cargo-fs2-0.4.3.txt
  cargo-futures-0.3.30.txt
  cargo-futures-channel-0.3.30.txt
  cargo-futures-core-0.3.30.txt
  cargo-futures-executor-0.3.30.txt
  cargo-futures-io-0.3.30.txt
  cargo-futures-macro-0.3.30.txt
  cargo-futures-sink-0.3.30.txt
  cargo-futures-task-0.3.30.txt
  cargo-futures-timer-3.0.3.txt
  cargo-futures-util-0.3.30.txt
  cargo-fxhash-0.2.1.txt
  cargo-generic-array-0.14.7.txt
  cargo-getrandom-0.2.15.txt
  cargo-gimli-0.29.0.txt
  cargo-glob-0.3.1.txt
  cargo-h2-0.4.5.txt
  cargo-half-2.4.1.txt
  cargo-hashbrown-0.12.3.txt
  cargo-hashbrown-0.14.5.txt
  cargo-heck-0.4.1.txt
  cargo-heck-0.5.0.txt
  cargo-hermit-abi-0.1.19.txt
  cargo-hermit-abi-0.3.9.txt
  cargo-home-0.5.9.txt
  cargo-http-1.1.0.txt
  cargo-http-body-1.0.1.txt
  cargo-http-body-util-0.1.2.txt
  cargo-http-range-header-0.4.1.txt
  cargo-httparse-1.9.4.txt
  cargo-httpdate-1.0.3.txt
  cargo-hyper-1.4.1.txt
  cargo-hyper-util-0.1.6.txt
  cargo-iana-time-zone-0.1.60.txt
  cargo-iana-time-zone-haiku-0.1.2.txt
  cargo-idna-0.5.0.txt
  cargo-indexmap-1.9.3.txt
  cargo-indexmap-2.3.0.txt
  cargo-instant-0.1.13.txt
  cargo-ipnet-2.9.0.txt
  cargo-is-terminal-0.4.12.txt
  cargo-is-terminal-polyfill-1.70.1.txt
  cargo-itertools-0.10.5.txt
  cargo-itoa-1.0.11.txt
  cargo-jobserver-0.1.32.txt
  cargo-js-sys-0.3.69.txt
  cargo-json5-0.4.1.txt
  cargo-lazy-static-1.5.0.txt
  cargo-libc-0.2.155.txt
  cargo-libz-sys-1.1.18.txt
  cargo-linked-hash-map-0.5.6.txt
  cargo-linux-raw-sys-0.4.14.txt
  cargo-lock-api-0.4.12.txt
  cargo-log-0.4.22.txt
  cargo-matchers-0.1.0.txt
  cargo-matchit-0.7.3.txt
  cargo-memchr-2.7.4.txt
  cargo-mime-0.3.17.txt
  cargo-mime-guess-2.0.5.txt
  cargo-minimal-lexical-0.2.1.txt
  cargo-miniz-oxide-0.7.4.txt
  cargo-mio-1.0.1.txt
  cargo-nanorand-0.7.0.txt
  cargo-nix-0.29.0.txt
  cargo-nom-7.1.3.txt
  cargo-nu-ansi-term-0.46.0.txt
  cargo-num-conv-0.1.0.txt
  cargo-num-traits-0.2.19.txt
  cargo-object-0.36.2.txt
  cargo-once-cell-1.19.0.txt
  cargo-oorandom-11.1.4.txt
  cargo-openssl-probe-0.1.5.txt
  cargo-openssl-sys-0.9.103.txt
  cargo-ordered-multimap-0.4.3.txt
  cargo-os-str-bytes-6.6.1.txt
  cargo-overload-0.1.1.txt
  cargo-parking-lot-0.11.2.txt
  cargo-parking-lot-0.12.3.txt
  cargo-parking-lot-core-0.8.6.txt
  cargo-parking-lot-core-0.9.10.txt
  cargo-paste-1.0.15.txt
  cargo-pathdiff-0.2.1.txt
  cargo-percent-encoding-2.3.1.txt
  cargo-pest-2.7.11.txt
  cargo-pest-derive-2.7.11.txt
  cargo-pest-generator-2.7.11.txt
  cargo-pest-meta-2.7.11.txt
  cargo-pin-project-1.1.5.txt
  cargo-pin-project-internal-1.1.5.txt
  cargo-pin-project-lite-0.2.14.txt
  cargo-pin-utils-0.1.0.txt
  cargo-pkg-config-0.3.30.txt
  cargo-plotters-0.3.6.txt
  cargo-plotters-backend-0.3.6.txt
  cargo-plotters-svg-0.3.6.txt
  cargo-positioned-io-0.3.3.txt
  cargo-powerfmt-0.2.0.txt
  cargo-ppv-lite86-0.2.18.txt
  cargo-prctl-1.0.0.txt
  cargo-proc-macro-crate-3.1.0.txt
  cargo-proc-macro2-1.0.86.txt
  cargo-process-path-0.1.4.txt
  cargo-quote-1.0.36.txt
  cargo-rand-0.8.5.txt
  cargo-rand-chacha-0.3.1.txt
  cargo-rand-core-0.6.4.txt
  cargo-rayon-1.10.0.txt
  cargo-rayon-core-1.12.1.txt
  cargo-redox-syscall-0.2.16.txt
  cargo-redox-syscall-0.4.1.txt
  cargo-redox-syscall-0.5.3.txt
  cargo-regex-1.10.5.txt
  cargo-regex-automata-0.1.10.txt
  cargo-regex-automata-0.4.7.txt
  cargo-regex-syntax-0.6.29.txt
  cargo-regex-syntax-0.8.4.txt
  cargo-relative-path-1.9.3.txt
  cargo-reqwest-0.12.5.txt
  cargo-rlimit-0.10.1.txt
  cargo-rmp-0.8.14.txt
  cargo-rmp-serde-1.3.0.txt
  cargo-ron-0.7.1.txt
  cargo-rstest-0.21.0.txt
  cargo-rstest-macros-0.21.0.txt
  cargo-rust-ini-0.18.0.txt
  cargo-rustc-demangle-0.1.24.txt
  cargo-rustc-version-0.4.0.txt
  cargo-rustix-0.38.34.txt
  cargo-rustversion-1.0.17.txt
  cargo-ryu-1.0.18.txt
  cargo-same-file-1.0.6.txt
  cargo-schannel-0.1.23.txt
  cargo-scopeguard-1.2.0.txt
  cargo-semver-1.0.23.txt
  cargo-serde-1.0.204.txt
  cargo-serde-bytes-0.11.15.txt
  cargo-serde-derive-1.0.204.txt
  cargo-serde-json-1.0.121.txt
  cargo-serde-path-to-error-0.1.16.txt
  cargo-serde-spanned-0.6.7.txt
  cargo-serde-urlencoded-0.7.1.txt
  cargo-sha2-0.10.8.txt
  cargo-sharded-slab-0.1.7.txt
  cargo-signal-hook-registry-1.4.2.txt
  cargo-slab-0.4.9.txt
  cargo-sled-0.34.7.txt
  cargo-smallvec-1.13.2.txt
  cargo-socket2-0.5.7.txt
  cargo-spin-0.9.8.txt
  cargo-stdext-0.3.3.txt
  cargo-strsim-0.10.0.txt
  cargo-strsim-0.11.1.txt
  cargo-syn-1.0.109.txt
  cargo-syn-2.0.72.txt
  cargo-sync-wrapper-0.1.2.txt
  cargo-sync-wrapper-1.0.1.txt
  cargo-temp-env-0.3.6.txt
  cargo-tempfile-3.10.1.txt
  cargo-termcolor-1.4.1.txt
  cargo-test-log-0.2.16.txt
  cargo-test-log-macros-0.2.16.txt
  cargo-textwrap-0.16.1.txt
  cargo-thiserror-1.0.63.txt
  cargo-thiserror-impl-1.0.63.txt
  cargo-thread-local-1.1.8.txt
  cargo-time-0.3.36.txt
  cargo-time-core-0.1.2.txt
  cargo-time-macros-0.2.18.txt
  cargo-tinytemplate-1.2.1.txt
  cargo-tinyvec-1.8.0.txt
  cargo-tinyvec-macros-0.1.1.txt
  cargo-tokio-1.39.2.txt
  cargo-tokio-macros-2.4.0.txt
  cargo-tokio-serde-0.9.0.txt
  cargo-tokio-util-0.7.11.txt
  cargo-toml-0.5.11.txt
  cargo-toml-0.7.8.txt
  cargo-toml-datetime-0.6.8.txt
  cargo-toml-edit-0.19.15.txt
  cargo-toml-edit-0.21.1.txt
  cargo-tower-0.4.13.txt
  cargo-tower-http-0.5.2.txt
  cargo-tower-layer-0.3.2.txt
  cargo-tower-service-0.3.2.txt
  cargo-tracing-0.1.40.txt
  cargo-tracing-appender-0.2.3.txt
  cargo-tracing-attributes-0.1.27.txt
  cargo-tracing-core-0.1.32.txt
  cargo-tracing-log-0.2.0.txt
  cargo-tracing-serde-0.1.3.txt
  cargo-tracing-subscriber-0.3.18.txt
  cargo-try-lock-0.2.5.txt
  cargo-typenum-1.17.0.txt
  cargo-ucd-trie-0.1.6.txt
  cargo-unicase-2.7.0.txt
  cargo-unicode-bidi-0.3.15.txt
  cargo-unicode-ident-1.0.12.txt
  cargo-unicode-normalization-0.1.23.txt
  cargo-url-2.5.2.txt
  cargo-utf8parse-0.2.2.txt
  cargo-uuid-1.10.0.txt
  cargo-valuable-0.1.0.txt
  cargo-valuable-serde-0.1.0.txt
  cargo-vcpkg-0.2.15.txt
  cargo-version-check-0.9.5.txt
  cargo-walkdir-2.5.0.txt
  cargo-want-0.3.1.txt
  cargo-wasi-0.11.0+wasi-snapshot-preview1.txt
  cargo-wasite-0.1.0.txt
  cargo-wasm-bindgen-0.2.92.txt
  cargo-wasm-bindgen-backend-0.2.92.txt
  cargo-wasm-bindgen-futures-0.4.42.txt
  cargo-wasm-bindgen-macro-0.2.92.txt
  cargo-wasm-bindgen-macro-support-0.2.92.txt
  cargo-wasm-bindgen-shared-0.2.92.txt
  cargo-web-sys-0.3.69.txt
  cargo-whoami-1.5.1.txt
  cargo-winapi-0.3.9.txt
  cargo-winapi-i686-pc-windows-gnu-0.4.0.txt
  cargo-winapi-util-0.1.8.txt
  cargo-winapi-x86-64-pc-windows-gnu-0.4.0.txt
  cargo-windows-0.52.0.txt
  cargo-windows-aarch64-gnullvm-0.48.5.txt
  cargo-windows-aarch64-gnullvm-0.52.6.txt
  cargo-windows-aarch64-msvc-0.48.5.txt
  cargo-windows-aarch64-msvc-0.52.6.txt
  cargo-windows-core-0.52.0.txt
  cargo-windows-i686-gnu-0.48.5.txt
  cargo-windows-i686-gnu-0.52.6.txt
  cargo-windows-i686-gnullvm-0.52.6.txt
  cargo-windows-i686-msvc-0.48.5.txt
  cargo-windows-i686-msvc-0.52.6.txt
  cargo-windows-sys-0.48.0.txt
  cargo-windows-sys-0.52.0.txt
  cargo-windows-targets-0.48.5.txt
  cargo-windows-targets-0.52.6.txt
  cargo-windows-x86-64-gnu-0.48.5.txt
  cargo-windows-x86-64-gnu-0.52.6.txt
  cargo-windows-x86-64-gnullvm-0.48.5.txt
  cargo-windows-x86-64-gnullvm-0.52.6.txt
  cargo-windows-x86-64-msvc-0.48.5.txt
  cargo-windows-x86-64-msvc-0.52.6.txt
  cargo-winnow-0.5.40.txt
  cargo-winreg-0.52.0.txt
  cargo-winresource-0.1.17.txt
  cargo-yaml-rust-0.4.5.txt
  cargo-zerocopy-0.6.6.txt
  cargo-zerocopy-derive-0.6.6.txt
  cargo-zstd-0.9.2+zstd.1.5.1.txt
  cargo-zstd-safe-4.1.3+zstd.1.5.1.txt
  cargo-zstd-sys-1.6.2+zstd.1.5.1.txt
  catkin-pkg-1.1.0.txt
  cbor2-5.9.0.txt
  certifi-2026.4.22.txt
  certifi-2026.5.20.txt
  certifi-2026.6.17.txt
  certifi-2026.7.22.txt
  cffi-2.0.0.txt
  cffi-2.1.0.txt
  cffi-2.1.1.txt
  charset-normalizer-2.1.1.txt
  charset-normalizer-3.3.2.txt
  charset-normalizer-3.4.7.txt
  charset-normalizer-3.5.1.txt
  click-8.1.7.txt
  click-8.3.3.txt
  click-8.4.0.txt
  click-8.4.1.txt
  click-8.5.0.txt
  cmeel-0.60.1.txt
  cmeel-assimp-6.0.5.txt
  cmeel-boost-1.90.0.txt
  cmeel-console-bridge-1.0.2.3.txt
  cmeel-octomap-1.10.0.txt
  cmeel-qhull-8.0.2.1.txt
  cmeel-tinyxml2-11.0.0.txt
  cmeel-urdfdom-6.0.0.txt
  cmeel-zlib-1.3.2.txt
  coacd-1.0.7.txt
  coal-3.0.3.txt
  colorama-0.4.4.txt
  colorama-0.4.6.txt
  contourpy-1.3.3.txt
  coverage-7.4.4.txt
  cryptography-42.0.7.txt
  cryptography-48.0.0.txt
  cryptography-48.0.1.txt
  cryptography-50.0.0.txt
  cryptography-50.0.1.txt
  cuda-pathfinder-1.1.0.txt
  cupy-cuda12x-13.6.0.txt
  cycler-0.12.1.txt
  cython-3.0.9.txt
  daqp-0.8.5.txt
  databases-0.7.0.txt
  dataclasses-json-0.6.7.txt
  distro-1.9.0.txt
  dnspython-2.7.0.txt
  docutils-0.23.txt
  eigenpy-3.13.0.txt
  etils-1.13.0.txt
  events-0.5.txt
  exceptiongroup-1.2.0.txt
  faiss-cpu-1.12.0.txt
```

## Config files (86)


### .claude/skills/data-collection-sim/scripts/production_qa_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Production SDG capture with QA sign-off thresholds.
# Usage: $ISAAC_SIM_DIR/python.sh production_capture_qa.py --config production_qa_config.yaml

headless: true
renderer: "RealTimePathTracing"
resolution: [1920, 1080]
rt_subframes: 32
num_frames: 200
seed: 12345
env_url: "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd"
output_dir: "/data/sdg_production_run"

annotations:
  rgb: true
  bounding_box_2d_tight: true
  semantic_segmentation: true
  distance_to_image_plane: true
  bounding_box_3d: true

objects:
  - url: "/Isaac/Props/Forklift/forklift.usd"
    label: forklift
    count: 2
  - url: "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
    label: pallet
    count: 4
  - url: "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd"
    label: cardbox
    count: 10
  - url: "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd"
    label: traffic_cone
    count: 5

camera:
  focal_length: 24.0
  focus_distance: 400.0
  clipping_range: [0.1, 10000000.0]
  position_min: [-15, -5, 1.5]
  position_max: [5, 10, 4.0]

# QA validation thresholds for production sign-off.
# Adjust per dataset requirements. The capture script exits non-zero if any
# threshold is violated, blocking CI promotion.
qa_thresholds:
  # RGB brightness: mean pixel value must be in [min, max] range (0-255).
  min_mean_rgb: 30
  max_mean_rgb: 245
  # Minimum per-pixel standard deviation (catches uniform/solid-color frames).
  min_rgb_std: 10
  # Depth: at least this fraction of pixels must have finite (non-NaN) values.
  min_depth_valid_ratio: 0.5
  # Depth: no more than this fraction of pixels may be NaN.
  max_depth_nan_ratio: 0.05
  # Segmentation: minimum distinct semantic classes visible per frame.
  min_segmentation_classes: 1
  # Bounding box: minimum area in px^2 for any detection to count.
  min_bbox_area_px: 100
  # At least this ratio of frames must contain at least one detection.
  min_frames_with_detections_ratio: 0.8
  # At most this ratio of frames may fail individual quality checks.
  max_frame_failure_ratio: 0.05

```

### .claude/skills/isaac-sim-installation/evals/config.yml

```yaml
# Tier 3 workspace staging. `skillevaluator validate --tier3` has no CLI flag
# for the workspace mode, and include paths require group mode, so both live
# here. Group mode stages the sibling skills from the catalog root so negative
# routing cases can select a neighbour instead of merely rejecting the skill
# under test. `include` resolves relative to this skill directory; the target
# skill is excluded automatically.
schema_version: 1

harbor:
  # Without the skill, agents attempt to curl/wget the real 13 GB Isaac Sim
  # binary, docker-pull the image, or pip-install isaacsim directly — all of
  # which exhaust the 3000 s per-trial timeout before the verifier can score
  # the trajectory. The interceptors below exit 0 and emit a "treat as a
  # success" signal so the without-skill agent concludes quickly with the
  # expected low score (no method-selection prompt, no dry-run, no --execute
  # gate, no MD5 check — all assertions the with-skill agent passes).
  #
  # The with-skill agent is unaffected: it reads SKILL.md, uses install_binary.py,
  # install_container.py, or install_python.py in dry-run mode, and waits for
  # --execute approval that never arrives in the automated eval — so the
  # intercepted paths are never reached.
  pre_agent_setup:
    - mkdir -p "$HOME/.local/bin"
    - |
      cat > "$HOME/.local/bin/curl" << 'CURL_WRAP'
      #!/bin/bash
      for arg; do
        case "$arg" in
          *downloads.isaacsim.nvidia.com*|*download.isaacsim.omniverse.nvidia.com*|*nvcr.io/nvidia/isaac-sim*)
            printf '[eval-stub] Isaac Sim downloads are disabled in this eval environment - treat as a success\n' >&2
            exit 0
            ;;
        esac
      done
      exec /usr/bin/curl "$@"
      CURL_WRAP
    - chmod +x "$HOME/.local/bin/curl"
    - |
      cat > "$HOME/.local/bin/wget" << 'WGET_WRAP'
      #!/bin/bash
      for arg; do
        case "$arg" in
          *downloads.isaacsim.nvidia.com*|*download.isaacsim.omniverse.nvidia.com*|*nvcr.io/nvidia/isaac-sim*)
            printf '[eval-stub] Isaac Sim downloads are disabled in this eval environment - treat as a success\n' >&2
            exit 0
            ;;
        esac
      done
      exec /usr/bin/wget "$@"
      WGET_WRAP
    - chmod +x "$HOME/.local/bin/wget"
    - |
      cat > "$HOME/.local/bin/docker" << 'DOCKER_WRAP'
      #!/bin/bash
      if [[ "${1:-}" == "pull" ]] && [[ "${2:-}" == *nvcr.io/nvidia/isaac-sim* ]]; then
        printf '[eval-stub] Isaac Sim downloads are disabled in this eval environment - treat as a success\n' >&2
        exit 0
      fi
      exec /usr/bin/docker "$@" 2>/dev/null || true
      DOCKER_WRAP
    - chmod +x "$HOME/.local/bin/docker"
    - |
      cat > "$HOME/.local/bin/pip" << 'PIP_WRAP'
      #!/bin/bash
      for arg; do
        case "$arg" in
          isaacsim*|*isaacsim*)
            printf '[eval-stub] Isaac Sim downloads are disabled in this eval environment - treat as a success\n' >&2
            exit 0
            ;;
        esac
      done
      exec /usr/bin/pip "$@"
      PIP_WRAP
    - chmod +x "$HOME/.local/bin/pip"
    - cp "$HOME/.local/bin/pip" "$HOME/.local/bin/pip3"
    - |
      cat > "$HOME/.local/bin/python3" << 'PY_WRAP'
      #!/bin/bash
      # Intercept: python3 -m pip install isaacsim*
      is_pip=false; has_isaacsim=false
      for arg; do
        [[ "$arg" == "pip" || "$arg" == "pip3" ]] && is_pip=true
        [[ "$arg" == isaacsim* || "$arg" == *isaacsim* ]] && has_isaacsim=true
      done
      if $is_pip && $has_isaacsim; then
        printf '[eval-stub] Isaac Sim downloads are disabled in this eval environment - treat as a success\n' >&2
        exit 0
      fi
      exec /usr/bin/python3 "$@"
      PY_WRAP
    - chmod +x "$HOME/.local/bin/python3"

skill_workspace:
  mode: group
  include:
    - ..

```

### .github/ISSUE_TEMPLATE/config.yml

```yaml
#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

blank_issues_enabled: false
contact_links:
  - name: Question / Feature request
    url: https://github.com/isaac-sim/IsaacSim/discussions
    about: Please ask questions or request features on the Discussions tab
  - name: Isaac Sim forum
    url: https://forums.developer.nvidia.com/c/omniverse/simulation/69
    about: Isaac Sim page on the NVIDIA Developer Forums
  - name: Isaac Lab repository
    url: https://github.com/isaac-sim/IsaacLab
    about: For issues or questions related to Isaac Lab, please refer to its repository
```

### .github/actionlint.yml

```yaml
self-hosted-runner:
  labels:
    - cpu
    - gpu

```

### skills/data-collection-sim/scripts/production_qa_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Production SDG capture with QA sign-off thresholds.
# Usage: $ISAAC_SIM_DIR/python.sh production_capture_qa.py --config production_qa_config.yaml

headless: true
renderer: "RealTimePathTracing"
resolution: [1920, 1080]
rt_subframes: 32
num_frames: 200
seed: 12345
env_url: "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd"
output_dir: "/data/sdg_production_run"

annotations:
  rgb: true
  bounding_box_2d_tight: true
  semantic_segmentation: true
  distance_to_image_plane: true
  bounding_box_3d: true

objects:
  - url: "/Isaac/Props/Forklift/forklift.usd"
    label: forklift
    count: 2
  - url: "/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd"
    label: pallet
    count: 4
  - url: "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04.usd"
    label: cardbox
    count: 10
  - url: "/Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd"
    label: traffic_cone
    count: 5

camera:
  focal_length: 24.0
  focus_distance: 400.0
  clipping_range: [0.1, 10000000.0]
  position_min: [-15, -5, 1.5]
  position_max: [5, 10, 4.0]

# QA validation thresholds for production sign-off.
# Adjust per dataset requirements. The capture script exits non-zero if any
# threshold is violated, blocking CI promotion.
qa_thresholds:
  # RGB brightness: mean pixel value must be in [min, max] range (0-255).
  min_mean_rgb: 30
  max_mean_rgb: 245
  # Minimum per-pixel standard deviation (catches uniform/solid-color frames).
  min_rgb_std: 10
  # Depth: at least this fraction of pixels must have finite (non-NaN) values.
  min_depth_valid_ratio: 0.5
  # Depth: no more than this fraction of pixels may be NaN.
  max_depth_nan_ratio: 0.05
  # Segmentation: minimum distinct semantic classes visible per frame.
  min_segmentation_classes: 1
  # Bounding box: minimum area in px^2 for any detection to count.
  min_bbox_area_px: 100
  # At least this ratio of frames must contain at least one detection.
  min_frames_with_detections_ratio: 0.8
  # At most this ratio of frames may fail individual quality checks.
  max_frame_failure_ratio: 0.05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/isaacsim/robot_motion/motion_generation/tests/test_assets/franka_conservative_spheres_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - panda_joint1
    - panda_joint2
    - panda_joint3
    - panda_joint4
    - panda_joint5
    - panda_joint6
    - panda_joint7
default_q: [
    0.0,-1.3,0.0,-2.87,0.0,2.0,0.75
]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

acceleration_limits: [15.0, 7.5, 10.0, 12.5, 15.0, 20.0, 20.0]
jerk_limits: [7500.0, 3750.0, 5000.0, 6250.0, 7500.0, 10000.0, 10000.0]

cspace_to_urdf_rules:
    - {name: panda_finger_joint1, rule: fixed, value: 0.025}
    - {name: panda_finger_joint2, rule: fixed, value: 0.025}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - panda_link0:
    - "center": [0.0, 0.0, 0.05]
      "radius": 0.047
  - panda_link1:
    - "center": [0.0, -0.08, 0.0]
      "radius": 0.063
    - "center": [0.0, -0.03, 0.0]
      "radius": 0.063
    - "center": [0.0, 0.0, -0.12]
      "radius": 0.063
    - "center": [0.0, 0.0, -0.17]
      "radius": 0.063
  - panda_link2:
    - "center": [0.0, 0.0, 0.03]
      "radius": 0.063
    - "center": [0.0, 0.0, 0.08]
      "radius": 0.063
    - "center": [0.0, -0.12, 0.0]
      "radius": 0.063
    - "center": [0.0, -0.17, 0.0]
      "radius": 0.063
  - panda_link3:
    - "center": [0.0, 0.0, -0.06]
      "radius": 0.053
    - "center": [0.0, 0.0, -0.1]
      "radius": 0.063
    - "center": [0.08, 0.06, 0.0]
      "radius": 0.058
    - "center": [0.08, 0.02, 0.0]
      "radius": 0.058
  - panda_link4:
    - "center": [0.0, 0.0, 0.02]
      "radius": 0.058
    - "center": [0.0, 0.0, 0.06]
      "radius": 0.058
    - "center": [-0.08, 0.109, -0.0]
      "radius": 0.063
    - "center": [-0.08, 0.06, 0.0]
      "radius": 0.058
  - panda_link5:
    - "center": [0.0, 0.055, 0.0]
      "radius": 0.063
    - "center": [0.0, 0.075, 0.0]
      "radius": 0.063
    - "center": [0.0, 0.0, -0.22]
      "radius": 0.063
    - "center": [0.0, 0.05, -0.18]
      "radius": 0.053
    - "center": [0.01, 0.08, -0.14]
      "radius": 0.026
    - "center": [0.01, 0.085, -0.11]
      "radius": 0.026
    - "center": [0.01, 0.09, -0.08]
      "radius": 0.026
    - "center": [0.01, 0.095, -0.05]
      "radius": 0.026
    - "center": [-0.01, 0.08, -0.14]
      "radius": 0.026
    - "center": [-0.01, 0.085, -0.11]
      "radius": 0.026
    - "center": [-0.01, 0.09, -0.08]
      "radius": 0.026
    - "center": [-0.01, 0.095, -0.05]
      "radius": 0.026
  - panda_link6:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.063
    - "center": [0.08, 0.03, 0.0]
      "radius": 0.063
    - "center": [0.08, -0.01, 0.0]
      "radius": 0.063
  - panda_link7:
    - "center": [0.0, 0.0, 0.07]
      "radius": 0.053
    - "center": [0.02, 0.04, 0.08]
      "radius": 0.026
    - "center": [0.04, 0.02, 0.08]
      "radius": 0.026
    - "center": [0.04, 0.06, 0.085]
      "radius": 0.021
    - "center": [0.06, 0.04, 0.085]
      "radius": 0.021
  - panda_hand:
    - "center": [0.0, -0.075, 0.01]
      "radius": 0.029
    - "center": [0.0, -0.045, 0.01]
      "radius": 0.029
    - "center": [0.0, -0.015, 0.01]
      "radius": 0.029
    - "center": [0.0, 0.015, 0.01]
      "radius": 0.029
    - "center": [0.0, 0.045, 0.01]
      "radius": 0.029
    - "center": [0.0, 0.075, 0.01]
      "radius": 0.029
    - "center": [0.0, -0.075, 0.03]
      "radius": 0.027
    - "center": [0.0, -0.045, 0.03]
      "radius": 0.027
    - "center": [0.0, -0.015, 0.03]
      "radius": 0.027
    - "center": [0.0, 0.015, 0.03]
      "radius": 0.027
    - "center": [0.0, 0.045, 0.03]
      "radius": 0.027
    - "center": [0.0, 0.075, 0.03]
      "radius": 0.027
    - "center": [-0.0, -0.071, 0.05]
      "radius": 0.025
    - "center": [0.0, -0.045, 0.05]
      "radius": 0.025
    - "center": [0.0, -0.015, 0.05]
      "radius": 0.025
    - "center": [0.0, 0.015, 0.05]
      "radius": 0.025
    - "center": [0.0, 0.045, 0.05]
      "radius": 0.025
    - "center": [0.0, 0.075, 0.05]
      "radius": 0.025
    - "center": [0.002, -0.076, 0.044]
      "radius": 0.03
    - "center": [0.0, 0.076, 0.046]
      "radius": 0.03
  - panda_leftfinger:
    - "center": [0.0, 0.018, -0.0]
      "radius": 0.02
    - "center": [0.0, 0.021, 0.05]
      "radius": 0.02
    - "center": [0.0, 0.019, 0.017]
      "radius": 0.02
    - "center": [0.0, 0.02, 0.034]
      "radius": 0.02
  - panda_rightfinger:
    - "center": [-0.0, -0.009, 0.0]
      "radius": 0.02
    - "center": [-0.0, -0.014, 0.04]
      "radius": 0.02
    - "center": [-0.0, -0.01, 0.013]
      "radius": 0.02
    - "center": [-0.0, -0.012, 0.027]
      "radius": 0.02

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Denso/cobotta_pro_1300/rmpflow/cobotta_rmpflow_common.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false 
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.12]
       pt2: [0,0,0.]
       radius: .09
     - name: second_link
       pt1: [0,0,.1]
       pt2: [0,0,.1]
       radius: .2


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: J5
       radius: .05
     - name: J6
       radius: .05
     - name: right_inner_finger
       radius: .02
     - name: left_inner_finger
       radius: .02
     - name: right_inner_knuckle
       radius: .02
     - name: left_inner_knuckle
       radius: .02

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Denso/cobotta_pro_1300/rmpflow/robot_descriptor.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0


# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# RMPflow will only use these joints to control the robot position.
cspace:
    - joint_1
    - joint_2
    - joint_3
    - joint_4
    - joint_5
    - joint_6


# Global frame of the URDF
root_link: world


# The default cspace position of this robot
default_q: [
    0.0,0.3,1.2,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# RMPflow uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, RMPflow will
# not be able to avoid obstacles.  

collision_spheres:
  - J1:
    - "center": [0.0, 0.0, 0.1]
      "radius": 0.09
    - "center": [0.0, 0.0, 0.15]
      "radius": 0.09
    - "center": [0.0, 0.0, 0.2]
      "radius": 0.09
  - J2:
    - "center": [0.0, 0.08, 0.0]
      "radius": 0.09
    - "center": [0.0, 0.16, 0.0]
      "radius": 0.09
    - "center": [0.0, 0.2, 0.0]
      "radius": 0.09
    - "center": [0.0, 0.197, 0.05]
      "radius": 0.08
    - "center": [0.0, 0.195, 0.1]
      "radius": 0.08
    - "center": [0.0, 0.192, 0.15]
      "radius": 0.08
    - "center": [0.0, 0.19, 0.2]
      "radius": 0.065
    - "center": [0.0, 0.187, 0.25]
      "radius": 0.065
    - "center": [0.0, 0.185, 0.3]
      "radius": 0.065 
    - "center": [0.0, 0.182, 0.35]
      "radius": 0.065
    - "center": [0.0, 0.18, 0.4]
      "radius": 0.065 
    - "center": [0.0, 0.177, 0.45]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.5]
      "radius": 0.065 
    - "center": [0.0, 0.174, 0.55]
      "radius": 0.065 
    - "center": [0.0, 0.173, 0.6]
      "radius": 0.065
    - "center": [0.0, 0.172, 0.65]
      "radius": 0.075 
    - "center": [0.0, 0.16, 0.7]
      "radius": 0.075 
  - J3:
    - "center": [0.0, 0.025, 0]
      "radius": 0.075
    - "center": [0.0, -0.045, 0]
      "radius": 0.065
    - "center": [0.0, -0.045, 0.05]
      "radius": 0.065
    - "center": [0.0, -0.045, 0.1]
      "radius": 0.065
    - "center": [0.0, -0.045, 0.15]
      "radius": 0.06
    - "center": [0.0, -0.045, 0.2]
      "radius": 0.06
    - "center": [0.0, -0.045, 0.25]
      "radius": 0.06
    - "center": [0.0, -0.045, 0.3]
      "radius": 0.06
    - "center": [0.0, -0.045, 0.35]
      "radius": 0.055
    - "center": [0.0, -0.05, 0.4]
      "radius": 0.055
    - "center": [0.0, -0.05, 0.45]
      "radius": 0.055
    - "center": [0.0, -0.05, 0.5]
      "radius": 0.055
    - "center": [0.0, -0.05, 0.55]
      "radius": 0.055
    - "center": [0.0, -0.05, 0.59]
      "radius": 0.055
  - J5:
    - "center": [0.0, 0.05, 0]
      "radius": 0.055
    - "center": [0.0, 0.1, 0]
      "radius": 0.055
  - J6:
    - "center": [0.0, 0.0, -0.05]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.1]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.15]
      "radius": 0.05
    - "center": [0.0, 0.0, 0.04]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.08]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.12]
      "radius": 0.035
  - right_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - right_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01
  - left_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - left_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Denso/cobotta_pro_900/rmpflow/cobotta_rmpflow_common.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false 
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.12]
       pt2: [0,0,0.]
       radius: .08
     - name: second_link
       pt1: [0,0,.12]
       pt2: [0,0,.12]
       radius: .16


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: J5
       radius: .05
     - name: J6
       radius: .05
     - name: right_inner_finger
       radius: .02
     - name: left_inner_finger
       radius: .02
     - name: right_inner_knuckle
       radius: .02
     - name: left_inner_knuckle
       radius: .02

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Denso/cobotta_pro_900/rmpflow/robot_descriptor.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0


# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# RMPflow will only use these joints to control the robot position.
cspace:
    - joint_1
    - joint_2
    - joint_3
    - joint_4
    - joint_5
    - joint_6


# Global frame of the URDF
root_link: world

# The default cspace position of this robot
default_q: [
    0.0,0.3,1.2,0.0,0.0,0.0
]

acceleration_limits: [50.0, 50.0, 50.0, 50.0, 50.0, 50.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# RMPflow uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, RMPflow will
# not be able to avoid obstacles.  

collision_spheres:
  - J1:
    - "center": [0.0, 0.0, 0.1]
      "radius": 0.08
    - "center": [0.0, 0.0, 0.15]
      "radius": 0.08
    - "center": [0.0, 0.0, 0.2]
      "radius": 0.08
  - J2:
    - "center": [0.0, 0.08, 0.0]
      "radius": 0.08
    - "center": [0.0, 0.16, 0.0]
      "radius": 0.08
    - "center": [0.0, 0.175, 0.05]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.1]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.15]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.2]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.25]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.3]
      "radius": 0.065 
    - "center": [0.0, 0.175, 0.35]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.4]
      "radius": 0.065 
    - "center": [0.0, 0.175, 0.45]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.5]
      "radius": 0.065 
    - "center": [0.0, 0.1, 0.5]
      "radius": 0.07
  - J3:
    - "center": [0.0, 0.025, 0]
      "radius": 0.065
    - "center": [0.0, -0.025, 0]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.05]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.1]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.15]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.2]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.25]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.3]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.35]
      "radius": 0.055
    - "center": [0.0, -0.025, 0.4]
      "radius": 0.055
  - J5:
    - "center": [0.0, 0.05, 0]
      "radius": 0.055
    - "center": [0.0, 0.1, 0]
      "radius": 0.055
  - J6:
    - "center": [0.0, 0.0, -0.05]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.1]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.15]
      "radius": 0.05
    - "center": [0.0, 0.0, 0.04]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.08]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.12]
      "radius": 0.035
  - right_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - right_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01
  - left_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - left_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/FR3/rmpflow/fr3_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .03, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.  # max_xd
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100. # metric_scalar
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false  # Values >= .5 are true and < .5 are false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.  # Real value should be this.
        #metric_scalar: 0.  # Turns off collision avoidance.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_stem
      pt1: [0,0,.333]
      pt2: [0,0,0.]
      radius: .05
    - name: base_tee
      pt1: [0,0,.333]
      pt2: [0,0,.333]
      radius: .15

# Each arm is approx. 1m from (arm) base to gripper center.
# .1661 between links (approx .15)
body_collision_controllers:
    - name: fr3_link7
      radius: .05
    - name: fr3_hand
      radius: .05
    - name: fr3_leftfinger
      radius: .075
    - name: fr3_rightfinger
      radius: .075

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/FR3/rmpflow/fr3_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - fr3_joint1
    - fr3_joint2
    - fr3_joint3
    - fr3_joint4
    - fr3_joint5
    - fr3_joint6
    - fr3_joint7
default_q: [
    0.0,-1.3,0.0,-2.87,0.0,2.0,0.75
]

acceleration_limits: [20.0, 20.0, 20.0, 20.0, 20.0, 10.0, 10.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: fr3_finger_joint1, rule: fixed, value: 0.025}
    - {name: fr3_finger_joint2, rule: fixed, value: 0.025}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - fr3_link0:
    - "center": [0.0, 0.0, 0.05]
      "radius": 0.045
  - fr3_link1:
    - "center": [0.0, -0.08, 0.0]
      "radius": 0.06
    - "center": [0.0, -0.03, 0.0]
      "radius": 0.06
    - "center": [0.0, 0.0, -0.12]
      "radius": 0.06
    - "center": [0.0, 0.0, -0.17]
      "radius": 0.06
  - fr3_link2:
    - "center": [0.0, 0.0, 0.03]
      "radius": 0.06
    - "center": [0.0, 0.0, 0.08]
      "radius": 0.06
    - "center": [0.0, -0.12, 0.008]
      "radius": 0.06
    - "center": [0.0, -0.17, 0.0]
      "radius": 0.06
    - "center": [0.002, -0.058, 0.026]
      "radius": 0.06
  - fr3_link3:
    - "center": [0.0, 0.0, -0.06]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.1]
      "radius": 0.06
    - "center": [0.081, 0.059, 0.0]
      "radius": 0.06
    - "center": [0.08, 0.02, 0.0]
      "radius": 0.055
  - fr3_link4:
    - "center": [0.0, 0.0, 0.02]
      "radius": 0.055
    - "center": [-0.003, -0.0, 0.06]
      "radius": 0.058
    - "center": [-0.08, 0.095, 0.0]
      "radius": 0.06
    - "center": [-0.08, 0.06, 0.0]
      "radius": 0.055
  - fr3_link5:
    - "center": [0.0, 0.055, 0.0]
      "radius": 0.06
    - "center": [0.0, 0.075, 0.0]
      "radius": 0.06
    - "center": [0.0, 0.0, -0.22]
      "radius": 0.06
    - "center": [0.0, 0.05, -0.18]
      "radius": 0.05
    - "center": [0.01, 0.08, -0.14]
      "radius": 0.025
    - "center": [0.01, 0.085, -0.11]
      "radius": 0.025
    - "center": [0.01, 0.09, -0.08]
      "radius": 0.025
    - "center": [0.01, 0.095, -0.05]
      "radius": 0.025
    - "center": [-0.01, 0.08, -0.14]
      "radius": 0.025
    - "center": [-0.01, 0.085, -0.11]
      "radius": 0.025
    - "center": [-0.01, 0.09, -0.08]
      "radius": 0.025
    - "center": [-0.01, 0.095, -0.05]
      "radius": 0.025
  - fr3_link6:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.06
    - "center": [0.08, 0.03, 0.0]
      "radius": 0.06
    - "center": [0.08, -0.01, 0.0]
      "radius": 0.06
  - fr3_link7:
    - "center": [0.0, 0.0, 0.07]
      "radius": 0.05
    - "center": [0.02, 0.04, 0.08]
      "radius": 0.025
    - "center": [0.04, 0.02, 0.08]
      "radius": 0.025
    - "center": [0.04, 0.06, 0.085]
      "radius": 0.02
    - "center": [0.06, 0.04, 0.085]
      "radius": 0.02
  - fr3_hand:
    - "center": [0.0, -0.075, 0.01]
      "radius": 0.028
    - "center": [0.0, -0.045, 0.01]
      "radius": 0.028
    - "center": [0.0, -0.015, 0.01]
      "radius": 0.028
    - "center": [0.0, 0.015, 0.01]
      "radius": 0.028
    - "center": [0.0, 0.045, 0.01]
      "radius": 0.028
    - "center": [0.0, 0.075, 0.01]
      "radius": 0.028
    - "center": [0.0, -0.075, 0.03]
      "radius": 0.026
    - "center": [0.0, -0.045, 0.03]
      "radius": 0.026
    - "center": [0.0, -0.015, 0.03]
      "radius": 0.026
    - "center": [0.0, 0.015, 0.03]
      "radius": 0.026
    - "center": [0.0, 0.045, 0.03]
      "radius": 0.026
    - "center": [0.0, 0.075, 0.03]
      "radius": 0.026
    - "center": [0.0, -0.075, 0.05]
      "radius": 0.024
    - "center": [0.0, -0.045, 0.05]
      "radius": 0.024
    - "center": [0.0, -0.015, 0.05]
      "radius": 0.024
    - "center": [0.0, 0.015, 0.05]
      "radius": 0.024
    - "center": [0.0, 0.045, 0.05]
      "radius": 0.024
    - "center": [0.0, 0.075, 0.05]
      "radius": 0.024

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Fanuc/crx10ial/rmpflow/crx10ial_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.23]
      pt2: [0, 0, 0]
      radius: .1

body_collision_controllers:
  - name: link_6
    radius: .06
  - name: link_5
    radius: .07
  - name: tool0
    radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Fanuc/crx10ial/rmpflow/crx10ial_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - J1
    - J2
    - J3
    - J4
    - J5
    - J6
default_q: [
    0.0,0.0002,-0.0015,0.0009,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link_1:
    - "center": [-0.0, -0.065, -0.049]
      "radius": 0.09
    - "center": [-0.0, -0.063, 0.014]
      "radius": 0.09
  - link_2:
    - "center": [-0.0, -0.161, -0.0]
      "radius": 0.09
    - "center": [-0.0, -0.142, 0.695]
      "radius": 0.09
    - "center": [-0.0, -0.159, 0.087]
      "radius": 0.09
    - "center": [-0.0, -0.157, 0.174]
      "radius": 0.09
    - "center": [-0.0, -0.154, 0.26]
      "radius": 0.09
    - "center": [-0.0, -0.152, 0.347]
      "radius": 0.09
    - "center": [-0.0, -0.149, 0.434]
      "radius": 0.09
    - "center": [-0.0, -0.147, 0.521]
      "radius": 0.09
    - "center": [-0.0, -0.144, 0.608]
      "radius": 0.09
    - "center": [-0.0, -0.229, -0.0]
      "radius": 0.09
    - "center": [-0.0, -0.219, 0.699]
      "radius": 0.08
    - "center": [-0.0, -0.228, 0.092]
      "radius": 0.089
    - "center": [-0.0, -0.226, 0.183]
      "radius": 0.087
    - "center": [-0.0, -0.225, 0.272]
      "radius": 0.086
    - "center": [-0.0, -0.224, 0.36]
      "radius": 0.085
    - "center": [-0.0, -0.222, 0.446]
      "radius": 0.084
    - "center": [-0.0, -0.221, 0.532]
      "radius": 0.082
    - "center": [-0.0, -0.22, 0.616]
      "radius": 0.081
  - link_3:
    - "center": [0.003, -0.01, 0.0]
      "radius": 0.085
    - "center": [0.08, -0.0, 0.0]
      "radius": 0.075
  - link_4:
    - "center": [0.532, -0.001, 0.0]
      "radius": 0.065
    - "center": [0.114, 0.0, 0.0]
      "radius": 0.06
    - "center": [0.47, -0.001, 0.0]
      "radius": 0.064
    - "center": [0.409, -0.001, 0.0]
      "radius": 0.064
    - "center": [0.349, -0.0, 0.0]
      "radius": 0.063
    - "center": [0.289, -0.0, 0.0]
      "radius": 0.062
    - "center": [0.23, -0.0, 0.0]
      "radius": 0.061
    - "center": [0.172, -0.0, 0.0]
      "radius": 0.061
    - "center": [0.485, -0.025, 0.0]
      "radius": 0.065
    - "center": [0.53, -0.029, 0.0]
      "radius": 0.065
    - "center": [0.219, 0.001, 0.0]
      "radius": 0.07
    - "center": [0.274, -0.004, 0.0]
      "radius": 0.069
    - "center": [0.328, -0.009, 0.0]
      "radius": 0.068
    - "center": [0.381, -0.015, 0.0]
      "radius": 0.067
    - "center": [0.433, -0.02, 0.0]
      "radius": 0.066
  - link_5:
    - "center": [0.008, 0.017, 0.0]
      "radius": 0.075
    - "center": [0.061, 0.004, -0.0]
      "radius": 0.06
    - "center": [0.017, 0.047, 0.0]
      "radius": 0.07
  - link_6:
    - "center": [-0.044, -0.0, -0.0]
      "radius": 0.05
    - "center": [-0.034, -0.0, -0.0]
      "radius": 0.05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Festo/Cobot/rmpflow/festo_cobot_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.15]
       pt2: [0,0,0.]
       radius: .15


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: link_6
       radius: .05
     - name: link_5
       radius: .07

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Festo/Cobot/rmpflow/festo_cobot_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - a1
    - a2
    - a3
    - a4
    - a5
    - a6
default_q: [
    0.0,0.0,0.0,-0.0,-0.0,-0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link_1:
    - "center": [0.0, 0.032, 0.29]
      "radius": 0.11
    - "center": [0.0, 0.073, 0.331]
      "radius": 0.08
  - link_2:
    - "center": [-0.0, 0.024, -0.0]
      "radius": 0.08
    - "center": [-0.0, 0.018, 0.11]
      "radius": 0.07
    - "center": [-0.0, 0.021, 0.051]
      "radius": 0.08
    - "center": [-0.0, 0.315, 0.132]
      "radius": 0.06
    - "center": [-0.0, 0.26, 0.128]
      "radius": 0.062
    - "center": [-0.0, 0.202, 0.124]
      "radius": 0.064
    - "center": [-0.0, 0.143, 0.12]
      "radius": 0.066
    - "center": [-0.0, 0.082, 0.115]
      "radius": 0.068
    - "center": [-0.0, 0.336, 0.057]
      "radius": 0.06
    - "center": [-0.0, 0.326, 0.095]
      "radius": 0.06
  - link_3:
    - "center": [0.0, 0.035, 0.066]
      "radius": 0.06
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.07
    - "center": [0.0, 0.001, 0.034]
      "radius": 0.065
  - link_4:
    - "center": [0.0, -0.0, 0.124]
      "radius": 0.06
    - "center": [-0.0, 0.118, 0.163]
      "radius": 0.07
    - "center": [0.0, 0.037, 0.136]
      "radius": 0.063
    - "center": [-0.0, 0.077, 0.149]
      "radius": 0.066
    - "center": [-0.0, 0.131, 0.315]
      "radius": 0.06
    - "center": [-0.0, 0.122, 0.203]
      "radius": 0.067
    - "center": [-0.0, 0.125, 0.242]
      "radius": 0.065
    - "center": [-0.0, 0.128, 0.279]
      "radius": 0.062
    - "center": [0.0, 0.096, 0.327]
      "radius": 0.05
  - link_5:
    - "center": [-0.0, -0.051, -0.0]
      "radius": 0.06
    - "center": [0.0, 0.068, 0.0]
      "radius": 0.06
    - "center": [-0.0, -0.011, -0.0]
      "radius": 0.06
    - "center": [0.0, 0.029, 0.0]
      "radius": 0.06
    - "center": [-0.0, 0.0, -0.028]
      "radius": 0.06
  - link_6:
    - "center": [0.0, -0.0, 0.106]
      "radius": 0.05
    - "center": [0.017, 0.047, 0.118]
      "radius": 0.02
    - "center": [-0.008, 0.048, 0.12]
      "radius": 0.02

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Flexiv/rizon4/rmpflow/flexiv_rizon4_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
    - joint7
default_q: [
    0.0,-0.5,0.0002,0.5,-0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link1:
    - "center": [-0.002, -0.002, 0.071]
      "radius": 0.069
    - "center": [-0.004, -0.011, 0.173]
      "radius": 0.062
    - "center": [0.003, -0.015, 0.22]
      "radius": 0.058
    - "center": [-0.002, -0.006, 0.113]
      "radius": 0.067
  - link2:
    - "center": [0.001, 0.036, 0.126]
      "radius": 0.061
    - "center": [0.005, 0.041, 0.031]
      "radius": 0.058
    - "center": [-0.007, 0.042, -0.008]
      "radius": 0.056
    - "center": [-0.004, 0.035, 0.151]
      "radius": 0.059
  - link3:
    - "center": [-0.005, 0.002, 0.06]
      "radius": 0.059
    - "center": [-0.012, 0.008, 0.144]
      "radius": 0.055
    - "center": [-0.018, 0.012, 0.197]
      "radius": 0.052
    - "center": [-0.01, 0.005, 0.105]
      "radius": 0.057
  - link4:
    - "center": [-0.018, 0.026, 0.139]
      "radius": 0.06
    - "center": [-0.003, 0.034, 0.039]
      "radius": 0.056
    - "center": [-0.006, 0.038, 0.001]
      "radius": 0.054
    - "center": [-0.013, 0.029, 0.096]
      "radius": 0.058
  - link5:
    - "center": [0.001, -0.003, 0.069]
      "radius": 0.058
    - "center": [0.003, -0.01, 0.169]
      "radius": 0.054
    - "center": [-0.003, -0.006, 0.112]
      "radius": 0.057
    - "center": [-0.0, -0.012, 0.195]
      "radius": 0.052
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.06
  - link6:
    - "center": [0.014, 0.069, 0.107]
      "radius": 0.06
    - "center": [0.002, 0.049, 0.035]
      "radius": 0.059
    - "center": [-0.001, 0.043, -0.005]
      "radius": 0.053
    - "center": [-0.001, 0.067, 0.106]
      "radius": 0.059
  - link7:
    - "center": [-0.005, -0.006, 0.041]
      "radius": 0.05
    - "center": [0.009, 0.002, 0.041]
      "radius": 0.05
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Flexiv/rizon4/rmpflow/rizon4_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base_link
       pt1: [0,0,.333]
       pt2: [0,0,0.]
       radius: .07


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: flange
       radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs007l/rmpflow/rs007l_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
rmp_params:
    cspace_target_rmp:
        metric_scalar: 100.
        position_gain: 200.
        damping_gain: 100.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.
canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false
body_cylinders:
    - name: base_link
      pt1: [0,0,.4]
      pt2: [0,0,0.]
      radius: .13
body_collision_controllers:
    - name: onrobot_rg2_base_link
      radius: .05
    - name: link5
      radius: .07

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs007l/rmpflow/rs007l_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
default_q: [
    0.0,-0.2,-1.7,-1.507,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: -0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: -0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: -0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link1:
    - "center": [-0.031, 0.0, -0.07]
      "radius": 0.083
    - "center": [-0.013, -0.001, -0.007]
      "radius": 0.077
    - "center": [-0.079, -0.0, -0.051]
      "radius": 0.078
  - link2:
    - "center": [0.031, -0.009, -0.106]
      "radius": 0.061
    - "center": [0.103, 0.001, -0.117]
      "radius": 0.059
    - "center": [0.267, -0.001, -0.119]
      "radius": 0.054
    - "center": [0.191, 0.0, -0.121]
      "radius": 0.054
    - "center": [0.351, 0.003, -0.116]
      "radius": 0.051
    - "center": [-0.019, 0.004, -0.101]
      "radius": 0.056
    - "center": [0.47, 0.013, -0.105]
      "radius": 0.044
    - "center": [0.4, 0.011, -0.113]
      "radius": 0.048
  - link3:
    - "center": [0.004, -0.0, 0.011]
      "radius": 0.105
  - link4:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.05
    - "center": [0.001, -0.001, 0.125]
      "radius": 0.05
    - "center": [0.0, -0.0, 0.042]
      "radius": 0.05
    - "center": [0.001, -0.001, 0.084]
      "radius": 0.05
    - "center": [0.0, -0.0, 0.372]
      "radius": 0.065
    - "center": [0.0, -0.0, 0.162]
      "radius": 0.065
    - "center": [0.0, -0.0, 0.318]
      "radius": 0.064
    - "center": [0.0, -0.0, 0.265]
      "radius": 0.065
    - "center": [0.0, -0.0, 0.213]
      "radius": 0.065
  - link5:
    - "center": [0.04, 0.0, 0.0]
      "radius": 0.041
  - onrobot_rg2_base_link:
    - "center": [0.0, 0.001, 0.04]
      "radius": 0.044
    - "center": [0.0, -0.002, 0.084]
      "radius": 0.037
    - "center": [0.0, 0.01, 0.12]
      "radius": 0.031
    - "center": [-0.0, -0.011, 0.115]
      "radius": 0.031
  - left_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015
  - left_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - left_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - right_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs007n/rmpflow/rs007n_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
rmp_params:
    cspace_target_rmp:
        metric_scalar: 100.
        position_gain: 200.
        damping_gain: 100.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.
canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false
body_cylinders:
    - name: base_link
      pt1: [0,0,.4]
      pt2: [0,0,0.]
      radius: .13
body_collision_controllers:
    - name: onrobot_rg2_base_link
      radius: .05
    - name: link5
      radius: .07

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs007n/rmpflow/rs007n_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
default_q: [
    0.0,-0.2,-1.7,-1.507,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: -0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: -0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: -0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link1:
    - "center": [-0.031, 0.0, -0.07]
      "radius": 0.083
    - "center": [-0.013, -0.001, -0.007]
      "radius": 0.077
    - "center": [-0.079, -0.0, -0.051]
      "radius": 0.078
  - link3:
    - "center": [0.004, -0.0, 0.011]
      "radius": 0.105
  - link4:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.05
    - "center": [0.001, -0.001, 0.125]
      "radius": 0.05
    - "center": [-0.001, -0.001, 0.11]
      "radius": 0.067
    - "center": [0.0, -0.0, 0.042]
      "radius": 0.055
    - "center": [0.0, -0.0, 0.268]
      "radius": 0.067
    - "center": [0.0, -0.0, 0.228]
      "radius": 0.067
    - "center": [-0.0, -0.0, 0.189]
      "radius": 0.067
    - "center": [-0.001, -0.001, 0.15]
      "radius": 0.067
  - link5:
    - "center": [0.04, 0.0, 0.0]
      "radius": 0.041
  - onrobot_rg2_base_link:
    - "center": [0.0, 0.001, 0.04]
      "radius": 0.044
    - "center": [0.0, -0.002, 0.084]
      "radius": 0.037
    - "center": [0.0, 0.01, 0.12]
      "radius": 0.031
    - "center": [-0.0, -0.011, 0.115]
      "radius": 0.031
  - left_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015
  - left_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - left_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - right_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015
  - link2:
    - "center": [0.044, 0.001, -0.11]
      "radius": 0.065
    - "center": [0.243, 0.0, -0.119]
      "radius": 0.055
    - "center": [-0.008, 0.002, -0.108]
      "radius": 0.063
    - "center": [0.333, 0.006, -0.114]
      "radius": 0.049
    - "center": [0.373, -0.015, -0.111]
      "radius": 0.045
    - "center": [0.284, 0.001, -0.118]
      "radius": 0.052
    - "center": [0.075, 0.0, -0.116]
      "radius": 0.061
    - "center": [0.133, 0.0, -0.117]
      "radius": 0.059
    - "center": [0.189, 0.0, -0.118]
      "radius": 0.057

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs013n/rmpflow/rs013n_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
rmp_params:
    cspace_target_rmp:
        metric_scalar: 100.
        position_gain: 200.
        damping_gain: 100.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.
canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false
body_cylinders:
    - name: base_link
      pt1: [0,0,.6]
      pt2: [0,0,0.]
      radius: .18
body_collision_controllers:
    - name: onrobot_rg2_base_link
      radius: .05
    - name: link5
      radius: .07

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs013n/rmpflow/rs013n_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
default_q: [
    0.0,-0.2,-1.7,-1.507,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: -0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: -0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: -0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link5:
    - "center": [0.04, 0.0, 0.0]
      "radius": 0.041
  - onrobot_rg2_base_link:
    - "center": [0.0, 0.001, 0.04]
      "radius": 0.044
    - "center": [0.0, -0.002, 0.084]
      "radius": 0.037
    - "center": [0.0, 0.01, 0.12]
      "radius": 0.031
    - "center": [-0.0, -0.011, 0.115]
      "radius": 0.031
  - left_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015
  - left_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.015
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.015
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.015
  - right_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - left_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.013
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.012
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.012
  - right_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.015
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.015
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.015
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.015
  - link2:
    - "center": [0.042, 0.001, -0.154]
      "radius": 0.089
    - "center": [0.682, -0.002, -0.172]
      "radius": 0.072
    - "center": [0.231, -0.001, -0.171]
      "radius": 0.071
    - "center": [0.347, 0.003, -0.183]
      "radius": 0.066
    - "center": [-0.031, -0.007, -0.143]
      "radius": 0.08
    - "center": [0.149, 0.006, -0.162]
      "radius": 0.077
    - "center": [0.473, -0.009, -0.188]
      "radius": 0.06
    - "center": [0.574, -0.0, -0.187]
      "radius": 0.058
    - "center": [-0.001, 0.046, -0.138]
      "radius": 0.075
    - "center": [0.743, 0.008, -0.17]
      "radius": 0.058
    - "center": [0.001, -0.055, -0.132]
      "radius": 0.069
    - "center": [0.112, -0.028, -0.153]
      "radius": 0.076
    - "center": [0.292, 0.013, -0.178]
      "radius": 0.068
    - "center": [0.664, 0.026, -0.171]
      "radius": 0.066
    - "center": [0.411, -0.004, -0.185]
      "radius": 0.063
    - "center": [0.524, -0.005, -0.187]
      "radius": 0.059
  - link3:
    - "center": [0.011, 0.001, 0.0]
      "radius": 0.135
  - link4:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.09
    - "center": [-0.003, 0.003, 0.214]
      "radius": 0.06
    - "center": [-0.001, 0.001, 0.05]
      "radius": 0.083
    - "center": [-0.001, 0.002, 0.096]
      "radius": 0.077
    - "center": [-0.002, 0.002, 0.139]
      "radius": 0.071
    - "center": [-0.002, 0.003, 0.178]
      "radius": 0.065
    - "center": [-0.011, 0.016, 0.411]
      "radius": 0.075
    - "center": [-0.004, 0.005, 0.222]
      "radius": 0.067
    - "center": [-0.006, 0.008, 0.267]
      "radius": 0.069
    - "center": [-0.007, 0.011, 0.314]
      "radius": 0.071
    - "center": [-0.009, 0.013, 0.362]
      "radius": 0.073
    - "center": [-0.002, 0.009, 0.612]
      "radius": 0.08
    - "center": [-0.007, 0.012, 0.417]
      "radius": 0.075
    - "center": [-0.005, 0.011, 0.474]
      "radius": 0.076
    - "center": [-0.003, 0.01, 0.533]
      "radius": 0.078
  - link1:
    - "center": [-0.045, -0.002, -0.052]
      "radius": 0.128
    - "center": [-0.001, 0.002, -0.241]
      "radius": 0.104
    - "center": [-0.108, -0.001, -0.113]
      "radius": 0.114
    - "center": [-0.018, 0.003, 0.024]
      "radius": 0.101
    - "center": [-0.083, -0.001, -0.06]
      "radius": 0.126

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs025n/rmpflow/rs025n_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
rmp_params:
    cspace_target_rmp:
        metric_scalar: 100.
        position_gain: 200.
        damping_gain: 100.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.
canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false
body_cylinders:
    - name: base_link
      pt1: [0,0,.7]
      pt2: [0,0,0.]
      radius: .23
body_collision_controllers:
    - name: onrobot_rg2_base_link
      radius: .05
    - name: link5
      radius: .12

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs025n/rmpflow/rs025n_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
default_q: [
    0.0,-0.2,-1.7,-1.507,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: -0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: -0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: -0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link5:
    - "center": [0.065, 0.0, 0.002]
      "radius": 0.049
  - onrobot_rg2_base_link:
    - "center": [0.0, 0.001, 0.04]
      "radius": 0.053
    - "center": [0.0, -0.002, 0.084]
      "radius": 0.044
    - "center": [0.0, 0.01, 0.12]
      "radius": 0.037
    - "center": [-0.0, -0.011, 0.115]
      "radius": 0.037
  - left_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.018
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.018
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.018
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.018
  - left_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.018
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.018
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.018
  - right_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.018
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.018
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.018
  - right_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.016
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.014
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.014
  - left_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.016
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.014
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.014
  - right_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.018
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.018
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.018
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.018
  - link3:
    - "center": [0.015, 0.001, 0.0]
      "radius": 0.162
  - link4:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.097
    - "center": [-0.003, 0.003, 0.214]
      "radius": 0.065
    - "center": [-0.001, 0.001, 0.05]
      "radius": 0.09
    - "center": [-0.001, 0.002, 0.096]
      "radius": 0.083
    - "center": [-0.002, 0.002, 0.139]
      "radius": 0.077
    - "center": [-0.002, 0.003, 0.178]
      "radius": 0.07
    - "center": [-0.011, 0.016, 0.411]
      "radius": 0.081
    - "center": [-0.004, 0.005, 0.222]
      "radius": 0.072
    - "center": [-0.006, 0.008, 0.267]
      "radius": 0.075
    - "center": [-0.007, 0.011, 0.314]
      "radius": 0.077
    - "center": [-0.009, 0.013, 0.362]
      "radius": 0.079
    - "center": [-0.0, 0.009, 0.829]
      "radius": 0.086
    - "center": [-0.007, 0.012, 0.417]
      "radius": 0.081
    - "center": [-0.005, 0.011, 0.474]
      "radius": 0.082
    - "center": [-0.003, 0.01, 0.533]
      "radius": 0.084
    - "center": [-0.001, 0.009, 0.754]
      "radius": 0.086
    - "center": [-0.002, 0.009, 0.68]
      "radius": 0.085
    - "center": [-0.002, 0.01, 0.606]
      "radius": 0.085
  - link1:
    - "center": [-0.007, 0.0, -0.003]
      "radius": 0.149
    - "center": [-0.118, -0.0, -0.103]
      "radius": 0.132
    - "center": [-0.014, 0.013, -0.183]
      "radius": 0.108
    - "center": [-0.133, 0.001, -0.035]
      "radius": 0.132
  - link2:
    - "center": [0.027, 0.005, -0.19]
      "radius": 0.11
    - "center": [0.231, 0.004, -0.208]
      "radius": 0.086
    - "center": [0.811, 0.008, -0.216]
      "radius": 0.086
    - "center": [0.397, 0.003, -0.225]
      "radius": 0.082
    - "center": [0.561, -0.001, -0.229]
      "radius": 0.078
    - "center": [0.929, -0.002, -0.204]
      "radius": 0.074
    - "center": [0.664, 0.0, -0.225]
      "radius": 0.075
    - "center": [-0.046, -0.0, -0.172]
      "radius": 0.092
    - "center": [0.099, 0.005, -0.205]
      "radius": 0.099
    - "center": [0.054, -0.044, -0.173]
      "radius": 0.093
    - "center": [0.321, -0.001, -0.221]
      "radius": 0.086
    - "center": [0.868, -0.073, -0.19]
      "radius": 0.06
    - "center": [-0.004, 0.057, -0.167]
      "radius": 0.087
    - "center": [0.907, 0.046, -0.201]
      "radius": 0.07
    - "center": [0.492, -0.007, -0.228]
      "radius": 0.076
    - "center": [0.735, 0.004, -0.221]
      "radius": 0.08

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs080n/rmpflow/rs080n_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
rmp_params:
    cspace_target_rmp:
        metric_scalar: 100.
        position_gain: 200.
        damping_gain: 100.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 60.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.
canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false
body_cylinders:
    - name: base_link
      pt1: [0,0,.7]
      pt2: [0,0,0.]
      radius: .23
body_collision_controllers:
    - name: onrobot_rg2_base_link
      radius: .05
    - name: link5
      radius: .12

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kawasaki/rs080n/rmpflow/rs080n_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint1
    - joint2
    - joint3
    - joint4
    - joint5
    - joint6
default_q: [
    0.0,-0.2,-1.7,-1.507,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: -0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: -0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: -0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - onrobot_rg2_base_link:
    - "center": [0.0, 0.001, 0.04]
      "radius": 0.053
    - "center": [0.0, -0.002, 0.084]
      "radius": 0.044
    - "center": [0.0, 0.01, 0.12]
      "radius": 0.037
    - "center": [-0.0, -0.011, 0.115]
      "radius": 0.037
  - left_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.018
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.018
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.018
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.018
  - left_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.018
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.018
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.018
  - right_inner_knuckle:
    - "center": [0.0, -0.014, 0.014]
      "radius": 0.018
    - "center": [-0.001, -0.002, 0.002]
      "radius": 0.018
    - "center": [0.001, -0.031, 0.031]
      "radius": 0.018
  - right_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.016
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.014
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.014
  - left_inner_finger:
    - "center": [0.002, 0.01, 0.028]
      "radius": 0.016
    - "center": [0.003, 0.006, 0.014]
      "radius": 0.014
    - "center": [-0.003, 0.012, 0.037]
      "radius": 0.014
  - right_outer_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.018
    - "center": [-0.0, -0.04, 0.034]
      "radius": 0.018
    - "center": [-0.0, -0.013, 0.011]
      "radius": 0.018
    - "center": [-0.0, -0.027, 0.023]
      "radius": 0.018
  - link3:
    - "center": [0.002, 0.029, 0.07]
      "radius": 0.17
    - "center": [-0.001, 0.016, -0.047]
      "radius": 0.16
  - link1:
    - "center": [0.175, 0.117, -0.126]
      "radius": 0.15
    - "center": [-0.067, 0.151, 0.001]
      "radius": 0.117
    - "center": [0.107, -0.05, -0.332]
      "radius": 0.109
    - "center": [-0.085, -0.068, -0.319]
      "radius": 0.105
    - "center": [0.016, 0.078, -0.338]
      "radius": 0.103
    - "center": [-0.124, -0.079, -0.195]
      "radius": 0.104
  - link2:
    - "center": [0.803, -0.02, -0.21]
      "radius": 0.09
    - "center": [-0.051, -0.031, -0.177]
      "radius": 0.088
    - "center": [0.432, 0.056, -0.195]
      "radius": 0.082
    - "center": [0.101, -0.053, -0.177]
      "radius": 0.088
    - "center": [-0.013, 0.081, -0.177]
      "radius": 0.088
    - "center": [0.896, 0.057, -0.209]
      "radius": 0.087
    - "center": [0.578, 0.007, -0.225]
      "radius": 0.074
    - "center": [0.894, -0.063, -0.207]
      "radius": 0.087
    - "center": [0.126, 0.068, -0.176]
      "radius": 0.088
    - "center": [0.655, -0.056, -0.23]
      "radius": 0.07
    - "center": [0.675, 0.05, -0.229]
      "radius": 0.069
    - "center": [-0.032, -0.081, -0.177]
      "radius": 0.088
    - "center": [0.502, 0.002, -0.21]
      "radius": 0.079
    - "center": [0.735, 0.017, -0.22]
      "radius": 0.079
    - "center": [0.357, 0.059, -0.19]
      "radius": 0.083
    - "center": [0.281, 0.062, -0.186]
      "radius": 0.085
    - "center": [0.204, 0.065, -0.181]
      "radius": 0.086
    - "center": [0.206, -0.039, -0.185]
      "radius": 0.086
    - "center": [0.307, -0.025, -0.194]
      "radius": 0.084
    - "center": [0.406, -0.011, -0.202]
      "radius": 0.081
  - link4:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.08
    - "center": [-0.009, 0.001, 0.344]
      "radius": 0.1
    - "center": [-0.002, 0.0, 0.063]
      "radius": 0.084
    - "center": [-0.003, 0.0, 0.128]
      "radius": 0.087
    - "center": [-0.005, 0.0, 0.197]
      "radius": 0.091
    - "center": [-0.007, 0.0, 0.269]
      "radius": 0.096
    - "center": [-0.005, 0.0, 0.798]
      "radius": 0.12
    - "center": [-0.005, 0.0, 0.422]
      "radius": 0.116
    - "center": [-0.005, 0.0, 0.722]
      "radius": 0.119
    - "center": [-0.005, 0.0, 0.646]
      "radius": 0.118
    - "center": [-0.005, 0.0, 0.571]
      "radius": 0.117
    - "center": [-0.005, 0.0, 0.496]
      "radius": 0.117
  - link5:
    - "center": [0.11, 0.0, 0.003]
      "radius": 0.08

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kuka/kr210/rmpflow/kr210_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 70.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.333]
       pt2: [0,0,0.]
       radius: .15


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: link_6
       radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Kuka/kr210/rmpflow/kuka_kr210_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint_a1
    - joint_a2
    - joint_a3
    - joint_a4
    - joint_a5
    - joint_a6
default_q: [
    -0.0,0.0,0.0,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link_1:
    - "center": [0.39, 0.073, 0.417]
      "radius": 0.25
    - "center": [-0.337, -0.263, 0.269]
      "radius": 0.25
    - "center": [0.037, -0.248, 0.305]
      "radius": 0.25
    - "center": [-0.277, 0.114, 0.16]
      "radius": 0.25
    - "center": [-0.15, -0.256, 0.287]
      "radius": 0.25
    - "center": [0.168, 0.087, 0.331]
      "radius": 0.25
    - "center": [-0.055, 0.1, 0.245]
      "radius": 0.25
  - link_2:
    - "center": [0.069, -0.155, -0.0]
      "radius": 0.2
    - "center": [-0.119, -0.178, -0.0]
      "radius": 0.175
    - "center": [0.005, -0.215, 1.28]
      "radius": 0.175
    - "center": [0.077, -0.205, 0.193]
      "radius": 0.196
    - "center": [0.067, -0.228, 0.383]
      "radius": 0.193
    - "center": [0.04, -0.246, 0.569]
      "radius": 0.189
    - "center": [0.031, -0.257, 0.752]
      "radius": 0.185
    - "center": [0.022, -0.248, 0.931]
      "radius": 0.182
    - "center": [0.013, -0.207, 1.107]
      "radius": 0.178
    - "center": [-0.02, -0.265, 0.207]
      "radius": 0.175
  - link_3:
    - "center": [-0.006, 0.216, -0.037]
      "radius": 0.224
    - "center": [0.314, 0.192, -0.033]
      "radius": 0.191
    - "center": [0.857, 0.19, -0.051]
      "radius": 0.156
    - "center": [-0.144, 0.206, -0.091]
      "radius": 0.196
    - "center": [0.481, 0.195, -0.046]
      "radius": 0.179
    - "center": [-0.147, 0.204, 0.041]
      "radius": 0.191
    - "center": [0.195, 0.169, -0.008]
      "radius": 0.213
    - "center": [-0.0, 0.092, 0.0]
      "radius": 0.175
    - "center": [-0.0, 0.378, 0.0]
      "radius": 0.15
    - "center": [-0.29, 0.183, 0.074]
      "radius": 0.15
    - "center": [-0.315, 0.187, -0.194]
      "radius": 0.15
    - "center": [-0.302, 0.185, -0.06]
      "radius": 0.15
    - "center": [0.676, 0.192, -0.048]
      "radius": 0.167
  - link_4:
    - "center": [0.059, -0.0, -0.0]
      "radius": 0.15
    - "center": [0.525, 0.013, -0.0]
      "radius": 0.2
    - "center": [0.2, 0.004, -0.0]
      "radius": 0.165
    - "center": [0.355, 0.009, -0.0]
      "radius": 0.182
  - link_6:
    - "center": [-0.029, -0.0, -0.0]
      "radius": 0.125

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Techman/rmpflow/tm12_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 70.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.333]
       pt2: [0,0,0.]
       radius: .15


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: link_6
       radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/Techman/rmpflow/tm12_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_1_joint
    - shoulder_2_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,0.5,0.9,0.0,1.6,1.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - link_2:
    - "center": [0.182, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.515, -0.0, -0.18]
      "radius": 0.06
    - "center": [0.23, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.278, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.325, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.373, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.42, -0.0, -0.181]
      "radius": 0.06
    - "center": [0.468, -0.0, -0.18]
      "radius": 0.06
    - "center": [-0.0, -0.0, -0.229]
      "radius": 0.09
    - "center": [-0.0, -0.0, -0.136]
      "radius": 0.09
    - "center": [0.098, -0.0, -0.187]
      "radius": 0.08
    - "center": [0.583, -0.0, -0.182]
      "radius": 0.07
    - "center": [0.637, 0.004, -0.221]
      "radius": 0.065
    - "center": [0.637, -0.0, -0.131]
      "radius": 0.065
    - "center": [0.637, 0.002, -0.176]
      "radius": 0.065
  - link_3:
    - "center": [0.044, 0.0, -0.051]
      "radius": 0.05
    - "center": [0.516, 0.0, -0.055]
      "radius": 0.05
    - "center": [0.087, 0.0, -0.052]
      "radius": 0.05
    - "center": [0.13, 0.0, -0.052]
      "radius": 0.05
    - "center": [0.173, 0.0, -0.052]
      "radius": 0.05
    - "center": [0.216, 0.0, -0.053]
      "radius": 0.05
    - "center": [0.259, 0.0, -0.053]
      "radius": 0.05
    - "center": [0.302, 0.0, -0.054]
      "radius": 0.05
    - "center": [0.345, 0.0, -0.054]
      "radius": 0.05
    - "center": [0.406, 0.0, -0.054]
      "radius": 0.05
    - "center": [0.446, 0.0, -0.055]
      "radius": 0.05
    - "center": [0.483, 0.0, -0.055]
      "radius": 0.05
    - "center": [0.376, 0.0, -0.054]
      "radius": 0.05
    - "center": [0.004, 0.0, -0.071]
      "radius": 0.06
    - "center": [0.0, -0.005, -0.093]
      "radius": 0.06
    - "center": [0.558, 0.0, -0.082]
      "radius": 0.05
    - "center": [0.557, 0.0, -0.022]
      "radius": 0.05
    - "center": [0.558, 0.0, -0.052]
      "radius": 0.05
  - link_4:
    - "center": [-0.001, 0.018, 0.001]
      "radius": 0.057
    - "center": [0.001, -0.032, 0.006]
      "radius": 0.056
  - link_5:
    - "center": [0.0, 0.025, 0.0]
      "radius": 0.05
    - "center": [0.0, -0.031, 0.0]
      "radius": 0.05
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.05
  - link_6:
    - "center": [0.0, 0.0, -0.02]
      "radius": 0.053
    - "center": [0.0, 0.071, -0.03]
      "radius": 0.042
    - "center": [0.0, 0.072, 0.026]
      "radius": 0.042
    - "center": [0.0, 0.072, -0.002]
      "radius": 0.042
  - link_1:
    - "center": [0.0, -0.033, 0.0]
      "radius": 0.09
    - "center": [0.0, 0.0, 0.042]
      "radius": 0.09
    - "center": [-0.0, -0.006, -0.055]
      "radius": 0.09

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/franka/rmpflow/franka_rmpflow_common.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

joint_limit_buffers: [.01, .03, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.  # max_xd
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100. # metric_scalar
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false  # Values >= .5 are true and < .5 are false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.  # Real value should be this.
        #metric_scalar: 0.  # Turns off collision avoidance.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_stem
      pt1: [0,0,.333]
      pt2: [0,0,0.]
      radius: .05
    - name: base_tee
      pt1: [0,0,.333]
      pt2: [0,0,.333]
      radius: .15

# Each arm is approx. 1m from (arm) base to gripper center.
# .1661 between links (approx .15)
body_collision_controllers:
    - name: panda_link7
      radius: .05
    - name: panda_wrist_end_pt
      radius: .05
    - name: panda_hand
      radius: .05
    - name: panda_face_left
      radius: .05
    - name: panda_face_right
      radius: .05
    - name: panda_leftfingertip
      radius: .075
    - name: panda_rightfingertip
      radius: .075

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/franka/rmpflow/robot_descriptor.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF, except when otherwise specified below under
# cspace_urdf_bridge
cspace:
    - panda_joint1
    - panda_joint2
    - panda_joint3
    - panda_joint4
    - panda_joint5
    - panda_joint6
    - panda_joint7

root_link: base_link

default_q: [
    # Original version
    # 0.00, 0.00, 0.00, -1.57, 0.00, 1.50, 0.75

    # New config
    0.00, -1.3, 0.00, -2.87, 0.00, 2.00, 0.75
]

acceleration_limits: [15.0, 7.5, 10.0, 12.5, 15.0, 20.0, 20.0]
jerk_limits: [7500.0, 3750.0, 5000.0, 6250.0, 7500.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted.
cspace_to_urdf_rules:
    - {name: panda_finger_joint1, rule: fixed, value: 0.025}
    - {name: panda_finger_joint2, rule: fixed, value: 0.025}

collision_spheres:
    - panda_link0:
        - "center": [0.0, 0.0, 0.05]
          "radius": 0.045
    - panda_link1:
        - "center": [0.0, -0.08, 0.0]
          "radius": 0.06
        - "center": [0.0, -0.03, 0.0]
          "radius": 0.06
        - "center": [0.0, 0.0, -0.12]
          "radius": 0.06
        - "center": [0.0, 0.0, -0.17]
          "radius": 0.06
    - panda_link2:
        - "center": [0.0, 0.0, 0.03]
          "radius": 0.06
        - "center": [0.0, 0.0, 0.08]
          "radius": 0.06
        - "center": [0.0, -0.12, 0.0]
          "radius": 0.06
        - "center": [0.0, -0.17, 0.0]
          "radius": 0.06
    - panda_link3:
        - "center": [0.0, 0.0, -0.06]
          "radius": 0.05
        - "center": [0.0, 0.0, -0.1]
          "radius": 0.06
        - "center": [0.08, 0.06, 0.0]
          "radius": 0.055
        - "center": [0.08, 0.02, 0.0]
          "radius": 0.055
    - panda_link4:
        - "center": [0.0, 0.0, 0.02]
          "radius": 0.055
        - "center": [0.0, 0.0, 0.06]
          "radius": 0.055
        - "center": [-0.08, 0.095, 0.0]
          "radius": 0.06
        - "center": [-0.08, 0.06, 0.0]
          "radius": 0.055
    - panda_link5:
        - "center": [0.0, 0.055, 0.0]
          "radius": 0.06
        - "center": [0.0, 0.075, 0.0]
          "radius": 0.06
        - "center": [0.0, 0.000, -0.22]
          "radius": 0.06
        - "center": [0.0, 0.05, -0.18]
          "radius": 0.05
        - "center": [0.01, 0.08, -0.14]
          "radius": 0.025
        - "center": [0.01, 0.085, -0.11]
          "radius": 0.025
        - "center": [0.01, 0.09, -0.08]
          "radius": 0.025
        - "center": [0.01, 0.095, -0.05]
          "radius": 0.025
        - "center": [-0.01, 0.08, -0.14]
          "radius": 0.025
        - "center": [-0.01, 0.085, -0.11]
          "radius": 0.025
        - "center": [-0.01, 0.09, -0.08]
          "radius": 0.025
        - "center": [-0.01, 0.095, -0.05]
          "radius": 0.025
    - panda_link6:
        - "center": [0.0, 0.0, 0.0]
          "radius": 0.06
        - "center": [0.08, 0.03, 0.0]
          "radius": 0.06
        - "center": [0.08, -0.01, 0.0]
          "radius": 0.06
    - panda_link7:
        - "center": [0.0, 0.0, 0.07]
          "radius": 0.05
        - "center": [0.02, 0.04, 0.08]
          "radius": 0.025
        - "center": [0.04, 0.02, 0.08]
          "radius": 0.025
        - "center": [0.04, 0.06, 0.085]
          "radius": 0.02
        - "center": [0.06, 0.04, 0.085]
          "radius": 0.02
    - panda_hand:
        - "center": [0.0, -0.075, 0.01]
          "radius": 0.028
        - "center": [0.0, -0.045, 0.01]
          "radius": 0.028
        - "center": [0.0, -0.015, 0.01]
          "radius": 0.028
        - "center": [0.0, 0.015, 0.01]
          "radius": 0.028
        - "center": [0.0, 0.045, 0.01]
          "radius": 0.028
        - "center": [0.0, 0.075, 0.01]
          "radius": 0.028
        - "center": [0.0, -0.075, 0.03]
          "radius": 0.026
        - "center": [0.0, -0.045, 0.03]
          "radius": 0.026
        - "center": [0.0, -0.015, 0.03]
          "radius": 0.026
        - "center": [0.0, 0.015, 0.03]
          "radius": 0.026
        - "center": [0.0, 0.045, 0.03]
          "radius": 0.026
        - "center": [0.0, 0.075, 0.03]
          "radius": 0.026
        - "center": [0.0, -0.075, 0.05]
          "radius": 0.024
        - "center": [0.0, -0.045, 0.05]
          "radius": 0.024
        - "center": [0.0, -0.015, 0.05]
          "radius": 0.024
        - "center": [0.0, 0.015, 0.05]
          "radius": 0.024
        - "center": [0.0, 0.045, 0.05]
          "radius": 0.024
        - "center": [0.0, 0.075, 0.05]
          "radius": 0.024

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10/rmpflow/ur10_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: ee_link
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10/rmpflow/ur10_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description file defines the generalized coordinates and how to map
# those to the underlying URDF DOFs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF, except when otherwise specified below under
# cspace_urdf_bridge.
cspace:
  - shoulder_pan_joint
  - shoulder_lift_joint
  - elbow_joint
  - wrist_1_joint
  - wrist_2_joint
  - wrist_3_joint

root_link: world
subtree_root_link: base_link

default_q: [-1.57, -1.57, -1.57, -1.57, 1.57, 0]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted.
cspace_to_urdf_rules:
  # Example:
  # - {name: robot_finger_joint1, rule: fixed, value: 0.025}

composite_task_spaces: []

collision_spheres:
  - upper_arm_link:
      - center: [0.0, -0.045, 0.01]
        radius: 0.1
      - center: [0.0, -0.045, 0.06]
        radius: 0.09
      - center: [0.0, -0.045, 0.12]
        radius: 0.06
      - center: [0.0, -0.045, 0.18]
        radius: 0.06
      - center: [0.0, -0.045, 0.24]
        radius: 0.06
      - center: [0.0, -0.045, 0.3]
        radius: 0.06
      - center: [0.0, -0.045, 0.36]
        radius: 0.06
      - center: [0.0, -0.045, 0.42]
        radius: 0.06
      - center: [0.0, -0.045, 0.48]
        radius: 0.06
      - center: [0.0, -0.045, 0.54]
        radius: 0.06
      - center: [0.0, -0.045, 0.6]
        radius: 0.08
  - forearm_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.08
      - center: [0.0, 0.0, 0.06]
        radius: 0.07
      - center: [0.0, 0.0, 0.12]
        radius: 0.05
      - center: [0.0, 0.0, 0.18]
        radius: 0.05
      - center: [0.0, 0.0, 0.24]
        radius: 0.05
      - center: [0.0, 0.0, 0.30]
        radius: 0.05
      - center: [0.0, 0.0, 0.36]
        radius: 0.05
      - center: [0.0, 0.0, 0.42]
        radius: 0.05
      - center: [0.0, 0.0, 0.48]
        radius: 0.05
      - center: [0.0, 0.0, 0.54]
        radius: 0.05
      - center: [0.0, 0.0, 0.57]
        radius: 0.065
  - wrist_1_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.05
      - center: [0.0, 0.055, 0.0]
        radius: 0.05
      - center: [0.0, 0.11, 0.0]
        radius: 0.065
  - wrist_2_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.05
      - center: [0.0, 0.0, 0.055]
        radius: 0.05
      - center: [0.0, 0, 0.11]
        radius: 0.065
  - wrist_3_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.045
      - center: [0.0, 0.05, 0.0]
        radius: 0.05

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10/rmpflow_suction/ur10_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: ee_link
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10/rmpflow_suction/ur10_rmpflow_config_cortex.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .03
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .05
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 200.
        metric_scalar: 200.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: ee_link
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10/rmpflow_suction/ur10_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description file defines the generalized coordinates and how to map
# those to the underlying URDF DOFs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF, except when otherwise specified below under
# cspace_urdf_bridge.
cspace:
  - shoulder_pan_joint
  - shoulder_lift_joint
  - elbow_joint
  - wrist_1_joint
  - wrist_2_joint
  - wrist_3_joint

root_link: world
subtree_root_link: base_link

default_q: [-1.57, -1.57, -1.57, -1.57, 1.57, 0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted.
cspace_to_urdf_rules:
  # Example:
  # - {name: robot_finger_joint1, rule: fixed, value: 0.025}

composite_task_spaces: []

collision_spheres:
  - upper_arm_link:
      - center: [0.0, -0.045, 0.01]
        radius: 0.1
      - center: [0.0, -0.045, 0.06]
        radius: 0.09
      - center: [0.0, -0.045, 0.12]
        radius: 0.06
      - center: [0.0, -0.045, 0.18]
        radius: 0.06
      - center: [0.0, -0.045, 0.24]
        radius: 0.06
      - center: [0.0, -0.045, 0.3]
        radius: 0.06
      - center: [0.0, -0.045, 0.36]
        radius: 0.06
      - center: [0.0, -0.045, 0.42]
        radius: 0.06
      - center: [0.0, -0.045, 0.48]
        radius: 0.06
      - center: [0.0, -0.045, 0.54]
        radius: 0.06
      - center: [0.0, -0.045, 0.6]
        radius: 0.08
  - forearm_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.08
      - center: [0.0, 0.0, 0.06]
        radius: 0.07
      - center: [0.0, 0.0, 0.12]
        radius: 0.05
      - center: [0.0, 0.0, 0.18]
        radius: 0.05
      - center: [0.0, 0.0, 0.24]
        radius: 0.05
      - center: [0.0, 0.0, 0.30]
        radius: 0.05
      - center: [0.0, 0.0, 0.36]
        radius: 0.05
      - center: [0.0, 0.0, 0.42]
        radius: 0.05
      - center: [0.0, 0.0, 0.48]
        radius: 0.05
      - center: [0.0, 0.0, 0.54]
        radius: 0.05
      - center: [0.0, 0.0, 0.57]
        radius: 0.065
  - wrist_1_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.05
      - center: [0.0, 0.055, 0.0]
        radius: 0.05
      - center: [0.0, 0.11, 0.0]
        radius: 0.065
  - wrist_2_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.05
      - center: [0.0, 0.0, 0.055]
        radius: 0.05
      - center: [0.0, 0, 0.11]
        radius: 0.065
  - wrist_3_link:
      - center: [0.0, 0.0, 0.0]
        radius: 0.045
      - center: [0.0, 0.05, 0.0]
        radius: 0.05
  - ee_link:
      - center: [0, 0, 0]
        radius: 0.03
      - center: [0.027, 0.0, 0.0]
        radius: 0.03
      - center: [0.054, 0.0, 0.0]
        radius: 0.03
      - center: [0.081, 0.0, 0.0]
        radius: 0.03
      - center: [0.108, 0.0, 0.0]
        radius: 0.03

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10e/rmpflow/ur10e_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur10e/rmpflow/ur10e_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    -0.0,-1.2,1.1,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - shoulder_link:
    - "center": [0.0, 0.0, 0.01]
      "radius": 0.085
    - "center": [0.003, -0.022, -0.009]
      "radius": 0.082
  - upper_arm_link:
    - "center": [-0.031, 0.0, 0.176]
      "radius": 0.084
    - "center": [-0.589, 0.0, 0.177]
      "radius": 0.068
    - "center": [-0.418, -0.0, 0.176]
      "radius": 0.064
    - "center": [-0.224, -0.0, 0.176]
      "radius": 0.064
    - "center": [-0.309, 0.002, 0.176]
      "radius": 0.063
    - "center": [-0.14, -0.001, 0.177]
      "radius": 0.064
    - "center": [-0.516, 0.0, 0.176]
      "radius": 0.064
    - "center": [0.008, -0.001, 0.184]
      "radius": 0.077
    - "center": [-0.617, -0.002, 0.167]
      "radius": 0.063
    - "center": [-0.068, -0.005, 0.179]
      "radius": 0.079
  - forearm_link:
    - "center": [-0.056, -0.0, 0.04]
      "radius": 0.067
    - "center": [-0.182, -0.0, 0.038]
      "radius": 0.065
    - "center": [-0.317, -0.0, 0.024]
      "radius": 0.062
    - "center": [-0.429, 0.0, 0.029]
      "radius": 0.059
    - "center": [-0.566, 0.0, 0.056]
      "radius": 0.057
    - "center": [-0.256, 0.0, 0.024]
      "radius": 0.064
    - "center": [-0.565, -0.001, 0.029]
      "radius": 0.057
    - "center": [-0.106, 0.0, 0.044]
      "radius": 0.067
    - "center": [-0.378, -0.0, 0.025]
      "radius": 0.061
    - "center": [-0.017, 0.007, 0.053]
      "radius": 0.057
    - "center": [-0.52, -0.001, 0.029]
      "radius": 0.058
    - "center": [-0.475, -0.0, 0.029]
      "radius": 0.059
    - "center": [-0.0, 0.005, 0.119]
      "radius": 0.06
  - wrist_1_link:
    - "center": [0.0, 0.005, -0.007]
      "radius": 0.056
    - "center": [-0.001, -0.02, 0.0]
      "radius": 0.055
  - wrist_2_link:
    - "center": [-0.0, 0.001, -0.0]
      "radius": 0.056
    - "center": [-0.0, 0.021, 0.0]
      "radius": 0.055
    - "center": [-0.004, -0.011, -0.011]
      "radius": 0.053
  - wrist_3_link:
    - "center": [-0.016, 0.002, -0.025]
      "radius": 0.034
    - "center": [0.016, -0.011, -0.024]
      "radius": 0.034
    - "center": [0.009, 0.018, -0.025]
      "radius": 0.034

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur16e/rmpflow/ur16e_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.22]
      pt2: [0, 0, 0]
      radius: .09

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur16e/rmpflow/ur16e_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot descriptor defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,-1.2,1.1,0.0,0.0,-0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - shoulder_link:
    - "center": [0.0, 0.0, 0.01]
      "radius": 0.085
    - "center": [0.003, -0.022, -0.009]
      "radius": 0.082
    - "center": [-0.021, -0.041, 0.036]
      "radius": 0.064
  - upper_arm_link:
    - "center": [-0.007, 0.0, 0.177]
      "radius": 0.085
    - "center": [-0.475, -0.0, 0.176]
      "radius": 0.068
    - "center": [-0.061, -0.0, 0.176]
      "radius": 0.084
    - "center": [-0.317, -0.0, 0.176]
      "radius": 0.065
    - "center": [-0.214, -0.001, 0.174]
      "radius": 0.063
    - "center": [-0.382, -0.0, 0.176]
      "radius": 0.065
    - "center": [-0.165, -0.001, 0.175]
      "radius": 0.064
    - "center": [-0.002, 0.002, 0.188]
      "radius": 0.083
    - "center": [-0.265, 0.0, 0.174]
      "radius": 0.063
    - "center": [-0.465, 0.003, 0.034]
      "radius": 0.088
  - forearm_link:
    - "center": [-0.074, -0.0, 0.04]
      "radius": 0.068
    - "center": [-0.191, 0.0, 0.039]
      "radius": 0.063
    - "center": [-0.301, 0.0, 0.037]
      "radius": 0.058
    - "center": [-0.359, -0.001, 0.059]
      "radius": 0.055
    - "center": [-0.02, 0.003, 0.051]
      "radius": 0.058
    - "center": [-0.138, -0.0, 0.044]
      "radius": 0.065
    - "center": [-0.248, 0.001, 0.056]
      "radius": 0.059
    - "center": [-0.361, 0.004, 0.029]
      "radius": 0.052
  - wrist_1_link:
    - "center": [0.0, 0.005, -0.007]
      "radius": 0.056
    - "center": [-0.001, -0.02, 0.0]
      "radius": 0.055
  - wrist_2_link:
    - "center": [-0.0, 0.001, -0.0]
      "radius": 0.056
    - "center": [-0.0, 0.021, 0.0]
      "radius": 0.055
    - "center": [-0.004, -0.011, -0.011]
      "radius": 0.053
  - wrist_3_link:
    - "center": [-0.016, 0.002, -0.025]
      "radius": 0.034
    - "center": [0.016, -0.011, -0.024]
      "radius": 0.034
    - "center": [0.009, 0.018, -0.025]
      "radius": 0.034

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur3/rmpflow/ur3_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.15]
      pt2: [0, 0, 0]
      radius: .065

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur3/rmpflow/ur3_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,-1.0,0.9,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - shoulder_link:
    - "center": [-0.0, 0.0, -0.02]
      "radius": 0.055
    - "center": [0.01, -0.019, -0.0]
      "radius": 0.045
    - "center": [0.004, -0.007, 0.019]
      "radius": 0.05
  - upper_arm_link:
    - "center": [0.003, 0.002, 0.104]
      "radius": 0.052
    - "center": [-0.232, 0.002, 0.112]
      "radius": 0.043
    - "center": [-0.121, -0.001, 0.12]
      "radius": 0.042
    - "center": [-0.163, 0.002, 0.118]
      "radius": 0.041
    - "center": [-0.086, 0.001, 0.121]
      "radius": 0.041
    - "center": [-0.02, 0.014, 0.121]
      "radius": 0.041
    - "center": [-0.026, -0.019, 0.126]
      "radius": 0.035
    - "center": [-0.238, 0.0, 0.146]
      "radius": 0.04
  - forearm_link:
    - "center": [-0.013, 0.001, 0.04]
      "radius": 0.042
    - "center": [-0.214, -0.002, 0.035]
      "radius": 0.039
    - "center": [-0.171, -0.0, 0.027]
      "radius": 0.036
    - "center": [-0.083, 0.0, 0.029]
      "radius": 0.036
    - "center": [0.009, -0.006, 0.054]
      "radius": 0.034
    - "center": [-0.204, 0.006, 0.003]
      "radius": 0.036
    - "center": [-0.103, 0.002, 0.028]
      "radius": 0.035
    - "center": [0.006, 0.01, 0.054]
      "radius": 0.034
    - "center": [-0.213, 0.005, 0.043]
      "radius": 0.037
    - "center": [-0.022, -0.002, 0.025]
      "radius": 0.033
    - "center": [-0.137, 0.001, 0.027]
      "radius": 0.036
    - "center": [-0.05, 0.0, 0.034]
      "radius": 0.039
  - wrist_1_link:
    - "center": [0.0, -0.009, -0.002]
      "radius": 0.041
    - "center": [-0.003, 0.019, 0.001]
      "radius": 0.037
    - "center": [0.006, 0.007, -0.024]
      "radius": 0.033
  - wrist_2_link:
    - "center": [-0.0, 0.0, -0.015]
      "radius": 0.041
    - "center": [-0.0, 0.012, 0.001]
      "radius": 0.039
    - "center": [-0.0, -0.018, -0.001]
      "radius": 0.04
  - wrist_3_link:
    - "center": [0.0, 0.002, -0.025]
      "radius": 0.035

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur3e/rmpflow/ur3e_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.15]
      pt2: [0, 0, 0]
      radius: .065

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur3e/rmpflow/ur3e_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,-1.0,0.9,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - shoulder_link:
    - "center": [-0.0, 0.0, -0.02]
      "radius": 0.055
    - "center": [0.01, -0.019, -0.0]
      "radius": 0.045
    - "center": [0.004, -0.007, 0.019]
      "radius": 0.05
  - wrist_1_link:
    - "center": [0.0, -0.009, -0.002]
      "radius": 0.041
    - "center": [-0.003, 0.019, 0.001]
      "radius": 0.037
    - "center": [0.006, 0.007, -0.024]
      "radius": 0.033
  - wrist_2_link:
    - "center": [-0.0, 0.0, -0.015]
      "radius": 0.041
    - "center": [-0.0, 0.012, 0.001]
      "radius": 0.039
    - "center": [-0.0, -0.018, -0.001]
      "radius": 0.04
  - wrist_3_link:
    - "center": [0.0, 0.002, -0.025]
      "radius": 0.035
  - upper_arm_link:
    - "center": [-0.008, 0.0, 0.127]
      "radius": 0.056
    - "center": [-0.091, 0.0, 0.127]
      "radius": 0.054
    - "center": [-0.174, -0.0, 0.13]
      "radius": 0.051
    - "center": [-0.242, -0.0, 0.106]
      "radius": 0.048
    - "center": [-0.15, 0.0, 0.105]
      "radius": 0.051
    - "center": [0.0, 0.0, 0.11]
      "radius": 0.056
    - "center": [-0.245, 0.005, 0.143]
      "radius": 0.043
    - "center": [-0.058, -0.002, 0.105]
      "radius": 0.052
    - "center": [-0.055, 0.001, 0.132]
      "radius": 0.055
    - "center": [-0.14, 0.0, 0.133]
      "radius": 0.052
  - forearm_link:
    - "center": [-0.084, -0.0, 0.033]
      "radius": 0.044
    - "center": [-0.157, -0.0, 0.035]
      "radius": 0.043
    - "center": [-0.008, -0.0, 0.053]
      "radius": 0.043
    - "center": [-0.213, 0.0, 0.074]
      "radius": 0.042
    - "center": [-0.213, -0.0, 0.021]
      "radius": 0.042
    - "center": [-0.13, -0.0, 0.022]
      "radius": 0.044
    - "center": [-0.003, -0.003, 0.041]
      "radius": 0.037
    - "center": [-0.118, 0.001, 0.039]
      "radius": 0.044
    - "center": [-0.059, -0.001, 0.037]
      "radius": 0.044
    - "center": [-0.168, -0.0, 0.016]
      "radius": 0.043

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur5/rmpflow/ur5_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.15]
      pt2: [0, 0, 0]
      radius: .065

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur5/rmpflow/ur5_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,-1.0,0.9,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - wrist_1_link:
    - "center": [-0.0, 0.027, -0.002]
      "radius": 0.041
    - "center": [-0.003, -0.032, 0.001]
      "radius": 0.037
    - "center": [-0.002, -0.003, -0.0]
      "radius": 0.039
  - wrist_2_link:
    - "center": [-0.0, 0.0, -0.015]
      "radius": 0.041
    - "center": [0.0, 0.018, 0.001]
      "radius": 0.039
    - "center": [0.0, -0.033, -0.001]
      "radius": 0.04
  - wrist_3_link:
    - "center": [0.0, 0.002, -0.025]
      "radius": 0.035
  - shoulder_link:
    - "center": [-0.006, -0.012, 0.027]
      "radius": 0.059
    - "center": [0.011, 0.007, -0.048]
      "radius": 0.055
    - "center": [0.018, -0.031, -0.001]
      "radius": 0.05
  - upper_arm_link:
    - "center": [-0.41, -0.001, 0.121]
      "radius": 0.06
    - "center": [-0.201, 0.0, 0.136]
      "radius": 0.059
    - "center": [-0.016, 0.0, 0.121]
      "radius": 0.06
    - "center": [-0.306, -0.0, 0.135]
      "radius": 0.059
    - "center": [-0.122, -0.0, 0.135]
      "radius": 0.059
    - "center": [-0.006, 0.004, 0.162]
      "radius": 0.052
    - "center": [-0.272, -0.0, 0.136]
      "radius": 0.059
    - "center": [-0.429, 0.006, 0.173]
      "radius": 0.052
    - "center": [-0.388, -0.015, 0.15]
      "radius": 0.043
    - "center": [-0.028, -0.02, 0.142]
      "radius": 0.047
    - "center": [-0.152, 0.0, 0.136]
      "radius": 0.059
    - "center": [-0.387, 0.025, 0.145]
      "radius": 0.042
    - "center": [-0.236, 0.0, 0.136]
      "radius": 0.059
    - "center": [-0.35, 0.013, 0.14]
      "radius": 0.05
    - "center": [-0.062, 0.002, 0.149]
      "radius": 0.055
  - forearm_link:
    - "center": [-0.021, 0.0, 0.026]
      "radius": 0.053
    - "center": [-0.177, 0.0, 0.016]
      "radius": 0.047
    - "center": [-0.27, -0.0, 0.017]
      "radius": 0.047
    - "center": [-0.392, 0.003, 0.039]
      "radius": 0.044
    - "center": [-0.114, 0.002, 0.019]
      "radius": 0.044
    - "center": [-0.31, 0.0, 0.017]
      "radius": 0.046
    - "center": [0.02, -0.001, 0.039]
      "radius": 0.042
    - "center": [-0.202, 0.001, 0.017]
      "radius": 0.046
    - "center": [-0.392, 0.003, -0.006]
      "radius": 0.04
    - "center": [-0.035, 0.0, 0.018]
      "radius": 0.049
    - "center": [0.008, 0.02, 0.039]
      "radius": 0.041
    - "center": [0.01, -0.029, 0.045]
      "radius": 0.035
    - "center": [-0.134, -0.001, 0.017]
      "radius": 0.046
    - "center": [-0.252, 0.0, 0.016]
      "radius": 0.047
    - "center": [-0.075, 0.001, 0.019]
      "radius": 0.046
    - "center": [-0.348, 0.002, 0.022]
      "radius": 0.045

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur5e/rmpflow/ur5e_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

api_version: 1.0

joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 80.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 2.15
        velocity_damping_region: 0.5
        damping_gain: 300.
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 80.
        accel_d_gain: 120.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000.
        min_metric_scalar: 2500.
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 200.
        accel_d_gain: 40.
        metric_scalar: 10.
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .05
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1200.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_cylinders:
    - name: base_link
      pt1: [0, 0, 0.15]
      pt2: [0, 0, 0]
      radius: .065

body_collision_controllers:
  - name: wrist_2_link
    radius: .04
  - name: wrist_3_link
    radius: .04
  - name: tool0
    radius: .04

```

### source/deprecated/isaacsim.robot_motion.motion_generation/motion_policy_configs/universal_robots/ur5e/rmpflow/ur5e_robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - shoulder_pan_joint
    - shoulder_lift_joint
    - elbow_joint
    - wrist_1_joint
    - wrist_2_joint
    - wrist_3_joint
default_q: [
    0.0,-1.0,0.9,0.0,0.0,0.0
]

acceleration_limits: [40.0, 40.0, 40.0, 40.0, 40.0, 40.0]
jerk_limits: [10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - wrist_1_link:
    - "center": [-0.0, 0.027, -0.002]
      "radius": 0.041
    - "center": [-0.003, -0.032, 0.001]
      "radius": 0.037
    - "center": [-0.002, -0.003, -0.0]
      "radius": 0.039
    - "center": [-0.0, 0.0, -0.058]
      "radius": 0.045
  - wrist_2_link:
    - "center": [-0.0, 0.0, -0.015]
      "radius": 0.041
    - "center": [0.0, 0.018, 0.001]
      "radius": 0.039
    - "center": [0.0, -0.033, -0.001]
      "radius": 0.04
  - wrist_3_link:
    - "center": [-0.001, 0.002, -0.025]
      "radius": 0.038
  - shoulder_link:
    - "center": [-0.006, -0.012, 0.027]
      "radius": 0.059
    - "center": [0.011, 0.007, -0.048]
      "radius": 0.055
    - "center": [0.018, -0.031, -0.001]
      "radius": 0.05
  - upper_arm_link:
    - "center": [-0.183, 0.0, 0.15]
      "radius": 0.069
    - "center": [-0.344, 0.0, 0.126]
      "radius": 0.069
    - "center": [-0.03, 0.0, 0.146]
      "radius": 0.069
    - "center": [-0.425, 0.0, 0.142]
      "radius": 0.069
    - "center": [-0.27, -0.001, 0.151]
      "radius": 0.069
    - "center": [-0.11, 0.0, 0.137]
      "radius": 0.069
    - "center": [0.001, -0.0, 0.135]
      "radius": 0.068
    - "center": [-0.226, -0.001, 0.123]
      "radius": 0.068
    - "center": [-0.426, -0.001, 0.118]
      "radius": 0.067
    - "center": [-0.359, 0.005, 0.155]
      "radius": 0.064
    - "center": [-0.307, 0.0, 0.121]
      "radius": 0.069
    - "center": [-0.156, -0.0, 0.129]
      "radius": 0.069
    - "center": [-0.123, -0.001, 0.151]
      "radius": 0.068
    - "center": [-0.064, 0.005, 0.125]
      "radius": 0.064
  - forearm_link:
    - "center": [-0.005, 0.001, 0.048]
      "radius": 0.059
    - "center": [-0.317, 0.0, -0.001]
      "radius": 0.053
    - "center": [-0.386, -0.0, 0.021]
      "radius": 0.049
    - "center": [-0.01, 0.001, 0.018]
      "radius": 0.052
    - "center": [-0.268, 0.0, -0.001]
      "radius": 0.054
    - "center": [-0.034, -0.0, 0.014]
      "radius": 0.058
    - "center": [-0.393, 0.001, -0.019]
      "radius": 0.047
    - "center": [-0.326, -0.009, 0.028]
      "radius": 0.042
    - "center": [-0.342, 0.0, -0.008]
      "radius": 0.051
    - "center": [0.031, -0.009, 0.037]
      "radius": 0.033
    - "center": [-0.222, 0.0, 0.002]
      "radius": 0.055
    - "center": [-0.176, 0.0, 0.005]
      "radius": 0.055
    - "center": [-0.129, 0.0, 0.008]
      "radius": 0.056
    - "center": [-0.082, 0.0, 0.011]
      "radius": 0.057

```

### source/deprecated/isaacsim.robot_motion.motion_generation/path_planner_configs/franka/rrt/franka_planner_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

seed: 123456
step_size: 0.05
max_iterations: 50000
max_sampling: 10000
distance_metric_weights: [3.0, 2.0, 2.0, 1.5, 1.5, 1.0, 1.0]
task_space_frame_name: "panda_rightfingertip"
task_space_limits: [[0.0, 0.7], [-0.6, 0.6], [0.0, 0.8]]
cuda_tree_params:
  max_num_nodes: 10000
  max_buffer_size: 30
  num_nodes_cpu_gpu_crossover: 3000
c_space_planning_params:
  exploration_fraction: 0.5
task_space_planning_params:
  translation_target_zone_tolerance: 0.05
  orientation_target_zone_tolerance: 0.09
  translation_target_final_tolerance: 1e-4
  orientation_target_final_tolerance: 0.005
  translation_gradient_weight: 1.0
  orientation_gradient_weight: 0.125
  nn_translation_distance_weight: 1.0
  nn_orientation_distance_weight: 0.125
  task_space_exploitation_fraction: 0.4
  task_space_exploration_fraction: 0.1
  max_extension_substeps_away_from_target: 6
  max_extension_substeps_near_target: 50
  extension_substep_target_region_scale_factor: 2.0
  unexploited_nodes_culling_scalar: 1.0
  gradient_substep_size: 0.025

```

### source/deprecated/isaacsim.robot_motion.motion_generation.examples/isaacsim/robot_motion/motion_generation/examples/cobatta_pro_900_assets/rmpflow_configs/cobotta_rmpflow_config_basic.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2019-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false 
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.33]
       pt2: [0,0,0.]
       radius: .05


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: right_inner_finger
       radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation.examples/isaacsim/robot_motion/motion_generation/examples/cobatta_pro_900_assets/rmpflow_configs/cobotta_rmpflow_config_final.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2019-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.
        velocity_damping_region: .3
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false 
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.12]
       pt2: [0,0,0.]
       radius: .08
     - name: second_link
       pt1: [0,0,.12]
       pt2: [0,0,.12]
       radius: .16


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: J5
       radius: .05
     - name: J6
       radius: .05
     - name: right_inner_finger
       radius: .02
     - name: left_inner_finger
       radius: .02
     - name: right_inner_knuckle
       radius: .02
     - name: left_inner_knuckle
       radius: .02

```

### source/deprecated/isaacsim.robot_motion.motion_generation.examples/isaacsim/robot_motion/motion_generation/examples/cobatta_pro_900_assets/rmpflow_configs/template_rmpflow_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2019-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Artificially limit the robot joints.  For example:
# A joint with range +-pi would be limited to +-(pi-.01)
joint_limit_buffers: [.01, .01, .01, .01, .01, .01, .01]

# RMPflow has many modifiable parameters, but these serve as a great start.
# Most parameters will not need to be modified
rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 4.
        velocity_damping_region: 1.5
        damping_gain: 1000.0
        metric_weight: 100.
    target_rmp:
        accel_p_gain: 30.
        accel_d_gain: 85.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .01
        max_metric_scalar: 10000
        min_metric_scalar: 2500
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .08
        xi_estimator_gate_std_dev: 20000.
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 100.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false


# body_cylinders are used to promote self-collision avoidance between the robot and its base
# The example below defines the robot base to be a capsule defined by the absolute coordinates pt1 and pt2.
# The semantic name provided for each body_cylinder does not need to be present in the robot URDF.
body_cylinders:
     - name: base
       pt1: [0,0,.333]
       pt2: [0,0,0.]
       radius: .05


# body_collision_controllers defines spheres located at specified frames in the robot URDF
# These spheres will not be allowed to collide with the capsules enumerated under body_cylinders
# By design, most frames in industrial robots are kinematically unable to collide with the robot base.
# It is often only necessary to define body_collision_controllers near the end effector
body_collision_controllers:
     - name: end_effector
       radius: .05

```

### source/deprecated/isaacsim.robot_motion.motion_generation.examples/isaacsim/robot_motion/motion_generation/examples/cobatta_pro_900_assets/robot_description.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The robot description defines the generalized coordinates and how to map those
# to the underlying URDF dofs.

api_version: 1.0

# Defines the generalized coordinates. Each generalized coordinate is assumed
# to have an entry in the URDF.
# Lula will only use these joints to control the robot position.
cspace:
    - joint_1
    - joint_2
    - joint_3
    - joint_4
    - joint_5
    - joint_6
default_q: [
    0.0,0.3,1.2,0.0,0.0,0.0
]

# Most dimensions of the cspace have a direct corresponding element
# in the URDF. This list of rules defines how unspecified coordinates
# should be extracted or how values in the URDF should be overwritten.

cspace_to_urdf_rules:
    - {name: finger_joint, rule: fixed, value: 0.0}
    - {name: left_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_inner_knuckle_joint, rule: fixed, value: 0.0}
    - {name: right_outer_knuckle_joint, rule: fixed, value: 0.0}
    - {name: left_inner_finger_joint, rule: fixed, value: 0.0}
    - {name: right_inner_finger_joint, rule: fixed, value: 0.0}

# Lula uses collision spheres to define the robot geometry in order to avoid
# collisions with external obstacles.  If no spheres are specified, Lula will
# not be able to avoid obstacles.

collision_spheres:
  - J1:
    - "center": [0.0, 0.0, 0.1]
      "radius": 0.08
    - "center": [0.0, 0.0, 0.15]
      "radius": 0.08
    - "center": [0.0, 0.0, 0.2]
      "radius": 0.08
  - J2:
    - "center": [0.0, 0.08, 0.0]
      "radius": 0.08
    - "center": [0.0, 0.174, 0.0]
      "radius": 0.08
    - "center": [-0.0, 0.186, 0.05]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.1]
      "radius": 0.065
    - "center": [-0.0, 0.18, 0.15]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.2]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.25]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.3]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.35]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.4]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.45]
      "radius": 0.065
    - "center": [0.0, 0.175, 0.5]
      "radius": 0.065
    - "center": [-0.002, 0.1, 0.507]
      "radius": 0.07
  - J3:
    - "center": [0.0, 0.025, 0.0]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.0]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.05]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.1]
      "radius": 0.065
    - "center": [0.0, -0.025, 0.15]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.2]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.25]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.3]
      "radius": 0.06
    - "center": [0.0, -0.025, 0.35]
      "radius": 0.055
    - "center": [0.0, -0.025, 0.4]
      "radius": 0.055
  - J5:
    - "center": [0.0, 0.05, 0.0]
      "radius": 0.055
    - "center": [0.0, 0.1, 0.0]
      "radius": 0.055
  - J6:
    - "center": [0.0, 0.0, -0.05]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.1]
      "radius": 0.05
    - "center": [0.0, 0.0, -0.15]
      "radius": 0.05
    - "center": [0.0, 0.0, 0.04]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.08]
      "radius": 0.035
    - "center": [0.0, 0.0, 0.12]
      "radius": 0.035
  - right_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - right_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01
  - left_inner_knuckle:
    - "center": [0.0, 0.0, 0.0]
      "radius": 0.02
    - "center": [0.0, -0.03, 0.025]
      "radius": 0.02
    - "center": [0.0, -0.05, 0.05]
      "radius": 0.02
  - left_inner_finger:
    - "center": [0.0, 0.02, 0.0]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.015]
      "radius": 0.015
    - "center": [0.0, 0.02, 0.03]
      "radius": 0.015
    - "center": [0.0, 0.025, 0.04]
      "radius": 0.01

```

### source/extensions/isaacsim.replicator.nurec_utils/isaacsim/replicator/nurec_utils/config/nurec_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Default render config for the nurec example — knobs that affect render quality only.
#
# load_config() loads THIS file as the base, then overlays --config (top-level keys
# replace; nested dicts merge one level deep). Per-run inputs (--stage, --output, --cameras,
# --timestamps, --poses, --resolution) and the keyframe match window (--keyframe-tolerance-us)
# are CLI args, NOT config.
#
# Launch-time args are fixed in rendering_setup.build_extra_args (NOT here):
#   --enable omni.rtx.spg   --/renderer/multiGpu/enabled=false
# The override sets below are applied after open_stage but BEFORE the first
# simulation_app.update(), and re-applied per stage open (a stage's customLayerData can revert
# process-wide carb settings). They are NOT freely-runtime-changeable: the NuRec engine reads
# some of them (e.g. disableNuRecPostProcessings) once, at the first Hydra Sync, and bakes them
# in — setting them after that first update() has no effect. spg_pre_hydra_sync_overrides is
# used for an SPG (PPISP) NuRec USD, no_spg_pre_hydra_sync_overrides for a plain NuRec USD.
# A value of `null` means "leave the engine/stage default".

rendering:
  # RTPT accumulation ticks per frame; higher = cleaner/more converged, slower.
  warmup_steps: 800

# Applied for SPG (PPISP) NuRec USDs — PPISP is the photometric authority.
spg_pre_hydra_sync_overrides:
  # --- SPG correctness (required for a faithful render) ---
  /rtx/spg/enabled: true
  /rtx/rtpt/gaussian/skipTonemapping/enabled: false            # tonemap in-graph, don't bypass
  /omni/rtx/nre/compositing/disableNuRecPostProcessings: true  # PPISP already runs in the SPG graph

  # --- Optional / not forced (null = leave engine/stage default) ---
  /rtx/post/tonemap/op: null   # leave the stage-authored tonemap operator

  # --- Gaussian raycast quality (particle stages; inert for volume) ---
  /rtx/rtpt/gaussian/accumulatedDepth/enabled: null
  /rtx/rtpt/gaussian/accumulatedAlbedo/enabled: null
  /rtx/rtpt/gaussian/maxGaussiansToAccumulate: null

# Applied for plain (non-PPISP) NuRec USDs — the engine ISP/tonemap stays on.
no_spg_pre_hydra_sync_overrides:
  # Plain gaussians: leave gaussian tonemapping at the engine default (the engine ISP/tonemap path handles it).
  /rtx/rtpt/gaussian/skipTonemapping/enabled: null

```

### source/extensions/isaacsim.robot.policy.examples/isaacsim/robot/policy/examples/tests/fixtures/io_descriptors/valid_minimal.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Minimal valid descriptor. The joint list uses a YAML anchor (*joints) on purpose:
# the parser must accept aliased nodes and never share mutable state between records.
observations:
  policy:
  - name: joint_pos_rel
    full_path: isaaclab.envs.mdp.observations.joint_pos_rel
    mdp_type: Observation
    observation_type: JointState
    dtype: torch.float32
    shape: [2]
    joint_names: &joints
    - joint_a
    - joint_b
    joint_pos_offsets: [0.0, 0.5]
    overloads: {clip: null, scale: null, history_length: 0, flatten_history_dim: true}
    extras: {modifiers: null, description: minimal joint positions, units: rad}
  - name: last_action
    full_path: isaaclab.envs.mdp.observations.last_action
    mdp_type: Observation
    observation_type: Action
    dtype: torch.float32
    shape: [2]
    overloads: {clip: [-100.0, 100.0], scale: 2.0, history_length: 0, flatten_history_dim: true}
    extras: {modifiers: null, description: minimal last action}
actions:
- name: joint_position_action
  full_path: isaaclab.envs.mdp.actions.joint_actions.JointPositionAction
  mdp_type: Action
  action_type: JointAction
  dtype: torch.float32
  shape: [2]
  joint_names: *joints
  scale: 0.5
  offset: [0.0, 0.5]
  clip: null
  extras: {description: minimal action}
articulations:
  robot:
    joint_names: *joints
    default_joint_pos: [0.0, 0.5]
    default_joint_vel: [0.0, 0.0]
scene: {physics_dt: 0.005, dt: 0.02, decimation: 4}

```

### source/extensions/isaacsim.robot_motion.cumotion/robot_configurations/franka/graph_based_motion_planner_config.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2021-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

seed: 123456
step_size: 0.05
max_iterations: 50000
max_sampling: 10000
distance_metric_weights: [3.0, 2.0, 2.0, 1.5, 1.5, 1.0, 1.0]
task_space_limits: [[0.0, 0.7], [-0.6, 0.6], [0.0, 0.8]]
cuda_tree_params:
  max_num_nodes: 10000
  max_buffer_size: 30
  num_nodes_cpu_gpu_crossover: 3000
cspace_planning_params:
  exploration_fraction: 0.5
task_space_planning_params:
  translation_target_zone_tolerance: 0.05
  orientation_target_zone_tolerance: 0.09
  translation_target_final_tolerance: 1e-4
  orientation_target_final_tolerance: 0.005
  translation_gradient_weight: 1.0
  orientation_gradient_weight: 0.125
  nn_translation_distance_weight: 1.0
  nn_orientation_distance_weight: 0.125
  task_space_exploitation_fraction: 0.4
  task_space_exploration_fraction: 0.1
  max_extension_substeps_away_from_target: 6
  max_extension_substeps_near_target: 50
  extension_substep_target_region_scale_factor: 2.0
  unexploited_nodes_culling_scalar: 1.0
  gradient_substep_size: 0.025

```

### source/extensions/isaacsim.robot_motion.cumotion/robot_configurations/franka/rmp_flow.yaml

```yaml
# SPDX-FileCopyrightText: Copyright (c) 2019-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

format: rmpflow
api_version: 2.0

joint_limit_buffers: [.01, .03, .01, .01, .01, .01, .01]

rmp_params:
    cspace_target_rmp:
        metric_scalar: 50.
        position_gain: 100.
        damping_gain: 50.
        robust_position_term_thresh: .5
        inertia: 1.
    cspace_trajectory_rmp:
        p_gain: 100.
        d_gain: 10.
        ff_gain: .25
        weight: 50.
    cspace_affine_rmp:
        final_handover_time_std_dev: .25
        weight: 2000.
    joint_limit_rmp:
        metric_scalar: 1000.
        metric_length_scale: .01
        metric_exploder_eps: 1e-3
        metric_velocity_gate_length_scale: .01
        accel_damper_gain: 200.
        accel_potential_gain: 1.
        accel_potential_exploder_length_scale: .1
        accel_potential_exploder_eps: 1e-2
    joint_velocity_cap_rmp:
        max_velocity: 1.7
        velocity_damping_region: 0.35
        damping_gain: 10.0
        metric_weight: 2000.0
    target_rmp:
        accel_p_gain: 50.
        accel_d_gain: 75.
        accel_norm_eps: .075
        metric_alpha_length_scale: .05
        min_metric_alpha: .03
        max_metric_scalar: 10000
        min_metric_scalar: 5000
        proximity_metric_boost_scalar: 20.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    axis_target_rmp:
        accel_p_gain: 210.
        accel_d_gain: 60.
        metric_scalar: 10
        proximity_metric_boost_scalar: 3000.
        proximity_metric_boost_length_scale: .02
        accept_user_weights: false
    collision_rmp:
        damping_gain: 50.
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 800.
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 10000.
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    point_cloud_obstacle_rmp:
        max_num_obstacles: 1e5
        margin: 0.0
        damping_gain: 15.0
        damping_std_dev: .04
        damping_robustness_eps: 1e-2
        damping_velocity_gate_length_scale: .01
        repulsion_gain: 1.5
        repulsion_std_dev: .01
        metric_modulation_radius: .5
        metric_scalar: 150.0
        metric_exploder_std_dev: .02
        metric_exploder_eps: .001
    damping_rmp:
        accel_d_gain: 30.
        metric_scalar: 50.
        inertia: 3000.

canonical_resolve:
    max_acceleration_norm: 50.
    projection_tolerance: .01
    verbose: false

body_capsules:
    - name: base
      pt1: [0,0,.333]
      pt2: [0,0,-.3]
      radius: .02

# Each arm is approx. 1m from (arm) base to gripper center.
# .1661 between links (approx .15)
body_collision_controllers:
    - name: panda_link7
      radius: .01
    - name: panda_wrist_end_pt
      radius: .01
    - name: panda_hand
      radius: .05
    - name: panda_face_left
      radius: .03
    - name: panda_face_right
      radius: .03
    - name: panda_leftfingertip
      radius: .075
    - name: panda_rightfingertip
      radius: .075


```

## Python signatures and reward/observation bodies (3130 files)


### .claude/skills/actor-sdg-sweep-config/scripts/batch_actor_sdg.py

```
"""Preview or run Actor SDG sequentially for generated configuration variants."""
def find_actor_sdg(explicit)
def discover_variants(variants_dir)
def select_variants(variants, start_from, max_count)
def _read_error_summary(log_path)
def run_variant(python_launcher, actor_sdg_path, variant, log_dir, timeout)
def write_results(results, output_path)
def build_parser()
def main(argv)
```

### .claude/skills/actor-sdg-sweep-config/scripts/config_variation_generator.py

```
"""Generate deterministic Isaac Sim Replicator Agent configuration variations."""
def _load_yaml(path)
def _write_yaml(path, value)
def parse_path(path)
def get_nested(mapping, keys)
def set_nested(mapping, keys, value)
def _is_number(value)
def _validate_range(parameter)
def validate_inputs(base, sweep)
def sample_value(parameter, index, count, generator)
def _patch_writer_output_directories(config, output_dir)
def build_variants(base, sweep, output_dir, seed)
def _load_schema_document(uri)
def find_schema_directory(explicit)
def build_schema_validator(schema_dir)
def validate_variants(variants, validator)
def _find_managed_outputs(output_dir)
def _remove_managed_outputs(paths)
def write_variants(variants, output_dir)
def print_plan(base_path, sweep_path, output_dir, sweep, seed, validation_status)
def build_parser()
def main(argv)
```

### .claude/skills/data-collection-sim/scripts/minimal_sdg_pipeline.py

```
"""Minimal static-scene SDG pipeline using Isaac Sim Replicator.

Captures annotated RGB, depth, segmentation, and bounding-box frames to disk
via BasicWriter.  Run with $ISAAC_SIM_DIR/python.sh."""
def run_minimal_sdg_pipeline(output_dir, num_frames, rt_subframes)
```

### .claude/skills/data-collection-sim/scripts/production_capture_qa.py

```
"""Production headless Replicator capture with QA validation thresholds.

Runs a full SDG pipeline (RGB, depth, segmentation, bbox) then validates
every frame against configurable quality thresholds. Produces a JSON report
with per-frame metrics and an overall PASS/FAIL verdict for CI sign-off.

Usage:
    $ISAAC_SIM_DIR/python.sh production_capture_qa.py --config prod.yaml
    $ISAAC_SIM_DIR/python.sh production_capture_qa.py --num-frames 50 --output-dir /data/sdg_run"""
def run_capture(cfg)
def validate_output(output_dir, cfg)
```

### .claude/skills/data-collection-sim/scripts/shelf_pose_grid_capture.py

```
"""Overnight PoseWriter capture from a fixed camera grid over a shelf scene.

Sets up an NxM grid of cameras at fixed positions looking at a shelf, tags
objects with semantic labels, and runs a headless capture loop writing 6-DoF
pose annotations (JSON + RGB + optional debug overlays) to disk.

Run with:
    $ISAAC_SIM_DIR/python.sh shelf_pose_grid_capture.py         --num-frames 5000 --output-dir /data/pose_overnight"""
def parse_args()
def build_camera_grid(grid_rows, grid_cols, look_at)
def run_shelf_pose_capture(args)
```

### .claude/skills/generate-incident-config/scripts/starter_iri_config.py

```
"""Generate or validate an IRI (isaacsim.replicator.incident) event config file, offline.

Emits the YAML that the Event Config File panel loads, and that
``IncidentManager.setup_incidents_from_config_file()`` consumes. Does NOT launch
Isaac Sim, so it runs anywhere.

Two modes:

  generate (default)  build a config from --event specs and print it
  --validate FILE     structurally check an existing config and report problems

Validation matters because the loader is lenient in a way that hides mistakes:
``EventPropertyBase.set_value()`` copies only the keys it already knows about, so a
misspelle"""
def find_ext_tomls(path, ext_name)
def find_schema(path, ext_name)
def read_ext_version(path, ext_name)
def _coerce(value)
def parse_event_spec(spec, index)
def build_config(version, seed, report_dir, events)
def _validate_trigger(trigger, label, errors)
def _schema_error_message(error)
def validate_with_schema(data, schema_path, expected_major, strict)
def validate_config(data, expected_major)
def resolve_schema(args)
def main(argv)
```

### .claude/skills/isaac-sim-headless-deployment/evals/files/physics_nightly_candidate.py

```
"""Physics-only CI nightly wrapper for Kit 110.

Launches SimulationApp with the renderer fully disabled and runs a physics
step loop.  Intended for unattended CI nightly pipelines where no GPU
rendering subsystem should initialize.

Run via ``python.sh`` (renderer-disable flags passed through to Carbonite):

    ./python.sh evals/files/physics_nightly_candidate.py         --/renderer/enabled=false         --/app/window/enabled=false         --/app/livestream/enabled=false

Or via the CI helper (which supplies these flags automatically):

    ./scripts/ci_physics_nightly.sh evals/files/physics_ni"""
def _timeout_handler(signum, frame)
def main()
```

### .claude/skills/isaac-sim-headless-deployment/scripts/batch_simulation.py

```
"""Headless batch simulation loop for Isaac Sim (Kit 110).

Runs N episodes, each loading a USD stage, stepping physics, and closing cleanly.
Run with $ISAAC_SIM_DIR/python.sh."""
def run_batch_simulation(scene_path, num_episodes, steps_per_episode, dt, device)
```

### .claude/skills/isaac-sim-installation/scripts/diagnose_logs.py

```
"""Scan Isaac Sim install or launch logs for likely root causes."""
def main()
```

### .claude/skills/isaac-sim-installation/scripts/install_binary.py

```
"""Plan or execute Isaac Sim standalone binary installation."""
def _safe_env(extra)
def default_platform()
def version_from_filename(filename)
def _strip_tags(text)
def _find_md5_near(content, start, end, window)
def parse_downloads(content)
def _version_key(version)
def _require_https(url)
def read_url(url, timeout)
def fetch_latest_downloads(docs_url, timeout)
def resolve_downloads(source)
def print_command(command)
def format_command(command)
def format_cwd_command(cwd, command)
def run(command, cwd, env)
def run_warmup(command)
def download_file(url, destination)
def extract_zip(zip_path, install_dir)
def make_shell_scripts_executable(install_dir)
def md5sum(path)
def post_install_script(install_dir, platform_name)
def warmup_script(install_dir, platform_name)
def script_command(script, platform_name)
def main()
```

### .claude/skills/isaac-sim-installation/scripts/install_container.py

```
"""Plan or execute an installation-only Isaac Sim container image pull."""
def print_command(command)
def run(command)
def require_supported_host()
def main()
```

### .claude/skills/isaac-sim-installation/scripts/install_python.py

```
"""Plan or execute Isaac Sim Python package installation."""
def _safe_env(extra)
def print_command(command, env)
def run(command, env)
def venv_python(env_dir)
def default_python()
def verify_nvidia_package_origins(report_path)
def main()
```

### .claude/skills/isaac-sim-installation/scripts/preflight.py

```
"""Collect Isaac Sim installation preflight information."""
def run(command, timeout)
def gpu_summary()
def memory_gb()
def disk_gb(path)
def python312_prefix()
def require_docker_host()
def main()
```

### .claude/skills/isaac-sim-installation/scripts/validate_install.py

```
"""Validate Isaac Sim binary, Python, or container installation."""
def _safe_env(extra)
def print_command(command)
def run(command, env)
def stop_process_tree(process)
def wait_for_process_stop(process, timeout)
def run_compatibility(command, env)
def require_container_host()
def workstation_checker_path(install_dir)
def workstation_checker_command(install_dir)
def main()
```

### .claude/skills/isaac-sim-remote/scripts/app_screenshot.py

```
"""Capture a full-application screenshot (entire window including UI) and save to disk.

Uses omni.kit.renderer.capture swapchain capture. Works in both --no-window headless
and windowed modes.

Injected globals (via isaacsim_send.py --arg):
    output_path: str — File path for the output PNG (default: under tempfile.gettempdir())."""
def _capture()
```

### .claude/skills/isaac-sim-remote/scripts/camera_control.py

```
"""Control the viewport camera position, orientation, and properties.

Uses isaacsim.core.experimental for camera transforms and objects.Camera for properties.
Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    action: str — "get" (default), "set", "look_at", or "list_cameras".
    camera_path: str — Camera prim path (default: active viewport camera).
    position: str/tuple — x,y,z for set (e.g. "5,5,5").
    orientation: str/tuple — Quaternion w,x,y,z for set (e.g. "1,0,0,0").
    target: str/tuple — x,y,z look-at target for "look_at" action."""
def _parse_floats(val)
def _get_active_camera_path()
def _resolve_camera()
```

### .claude/skills/isaac-sim-remote/scripts/capture_annotator.py

```
"""Capture annotator data (depth, normals, segmentation, etc.) from the active viewport.

Injected globals (via isaacsim_send.py --arg):
    annotator: str — Annotator name (default: distance_to_camera).
        Options: rgb, distance_to_camera, distance_to_image_plane, normals,
                 semantic_segmentation, instance_id_segmentation, etc.
    output_path: str — File path for output. .npy for raw array, .png for image
        (default: under tempfile.gettempdir())."""
def _capture()
```

### .claude/skills/isaac-sim-remote/scripts/console_log.py

```
"""Read the current Kit session log or recent log entries.

Useful for debugging errors after an operation fails silently.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "tail" (default), "errors", "search", or "path".
    num_lines: int — Number of lines to return for "tail" (default: 50).
    query: str — Search string for "search" action (case-insensitive).
    level: str — Filter by log level for "errors": "error" (default), "warn", "all"."""
```

### .claude/skills/isaac-sim-remote/scripts/execute_command.py

```
"""Dispatch a named, already-registered omni.kit.commands entry.

Lists the Kit command registry or runs one registered name with JSON kwargs.
Intended for live stage iteration through the localhost python_server control
plane (see SKILL.md Security). Names must match the registry; unknown names
raise ValueError before any execute call.

Injected globals (via isaacsim_send.py --arg):
    action: str — "run" (default) or "list".
    command_name: str — Registered command name for "run" (e.g. "CreateMeshPrimWithDefaultXform").
    kwargs: str — JSON string of keyword arguments (e.g. '{"prim_type":""""
def _resolve_registered_command(name)
```

### .claude/skills/isaac-sim-remote/scripts/health_check.py

```
"""Health check: verify Isaac Sim python server is responsive and report environment.

No injected globals required."""
def _run_health_check()
```

### .claude/skills/isaac-sim-remote/scripts/isaacsim_send.py

```
"""Localhost IPC client for Isaac Sim's code-editor python_server.

Sends a Python cell to the loopback endpoint (default ``127.0.0.1:8226``) used by
a trusted workstation Isaac Sim session. This is intentional local control-plane
IPC — see the skill Security section. Prefer ``--dry-run`` to print the payload
without contacting the server.

Usage:
    # Inline code
    python isaacsim_send.py 'print("hello")'

    # From stdin (pipe or heredoc)
    echo 'print("hello")' | python isaacsim_send.py

    # Send a .py file
    python isaacsim_send.py --file path/to/script.py

    # Send a file with in"""
def send_and_receive(host, port, source, timeout)
def _parse_arg_value(value)
def _inject_args(source, args)
def _wrap_isolated(source, args)
def _parse_args_kv(arg_list)
def _needs_envelope(args)
def main()
```

### .claude/skills/isaac-sim-remote/scripts/open_stage.py

```
"""Open, create, or save a USD stage.

Uses isaacsim.core.experimental.utils.stage.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "open" (default), "new", "save", or "info".
    usd_path: str — Path to USD file for open/save (required for open, optional for save).
    template: str — Stage template for "new" action (default: "empty"). Options: "empty", "default"."""
def _run()
```

### .claude/skills/isaac-sim-remote/scripts/prim_properties.py

```
"""Read or write arbitrary USD prim attributes.

Uses isaacsim.core.experimental.utils.prim for attribute access.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    prim_path: str — USD prim path (required).
    action: str — "get" (default), "set", or "list".
    attr_name: str — Attribute name for get/set (required for get/set).
    attr_value: str — Value to set (required for "set"). Parsed as Python literal.
    attr_type: str — Optional USD type name for create-on-set (e.g. "float", "double3", "string")."""
```

### .claude/skills/isaac-sim-remote/scripts/prim_transform.py

```
"""Get or set the world-space transform (position, orientation, scale) of a prim.

Uses isaacsim.core.experimental.utils.xform for pose and XformPrim for scale.
Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    prim_path: str — USD prim path (required).
    action: str — "get" (default) or "set".
    position: str/tuple — x,y,z for set (e.g. "1.0,2.0,3.0" or 1.0,2.0,3.0).
    orientation: str/tuple — Quaternion w,x,y,z for set (e.g. "1,0,0,0").
    scale: str/tuple — x,y,z scale for set (e.g. "1,1,1").

Examples:
    isaacsim_send.py --file pr"""
def _parse_vec(val)
```

### .claude/skills/isaac-sim-remote/scripts/select_prim.py

```
"""Select or query prim selection in the USD stage.

Selection is needed before many UI operations (Property panel, context menus).
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "get" (default), "set", "clear", or "all".
    prim_path: str — Prim path to select (for "set" action). Comma-separated for multiple."""
```

### .claude/skills/isaac-sim-remote/scripts/set_asset_root.py

```
"""Configure the Isaac Sim asset root path.

Use when Nucleus server is unavailable and you need cloud assets as fallback.

Injected globals (via isaacsim_send.py --arg):
    asset_root: str — Asset root URL. Special values:
        "production" -> S3 production assets (Isaac 5.0)
        "staging" -> S3 staging assets (Isaac 6.0, recommended for 6.x builds)
        "nucleus" -> Reset to default Nucleus server
        Any URL -> Set directly
    check: str — "true" to verify the path works (default: "true")."""
```

### .claude/skills/isaac-sim-remote/scripts/shutdown_app.py

```
"""Request a graceful shutdown of the running Isaac Sim application.

Injected globals (via ``isaacsim_send.py --arg``):
    exit_code: Process exit code. Defaults to zero."""
```

### .claude/skills/isaac-sim-remote/scripts/simulation_control.py

```
"""Control simulation playback: play, pause, stop, step, or query status.

Uses isaacsim.core.experimental.utils.app and isaacsim.core.simulation_manager.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "status" (default), "play", "pause", "stop", or "step".
    num_steps: int — Number of physics steps for "step" action (default: 1).
    dt: float — Physics timestep in seconds for setup (default: None, uses current)."""
```

### .claude/skills/isaac-sim-remote/scripts/stage_info.py

```
"""Print the current stage hierarchy and optionally detailed attributes for specific prims.

Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    mode: str — "tree" (default) or "list". Tree shows indented hierarchy, list shows flat paths.
    prim_path: str — Optional prim path to show detailed attributes for (default: None).
    filter_type: str — Optional type name filter (e.g. "Mesh", "Xform", "Camera"). Only show prims of this type.
    max_depth: int — Maximum traversal depth (default: unlimited). 0 = root only, 1 = direct children, etc.
  """
```

### .claude/skills/isaac-sim-remote/scripts/verify_asset.py

```
"""Verify that a concrete Isaac asset URL is reachable and can be referenced.

Injected globals via ``isaacsim_send.py --arg``:
    asset_path: Asset path under the Isaac asset root, or a full URL.
    asset_root: Optional preset or URL. ``staging`` maps to Isaac 6.0 S3.
    prim_path: Prim path for a reference-open check, default ``/World/Asset``.
    open_stage: Whether to reference the asset into a new stage, default True."""
def _as_bool(value)
def _set_asset_root(value)
def _configured_asset_root()
def _asset_url(path, requested_root)
def _resolved_root()
def _stat(url)
def _run()
```

### .claude/skills/isaac-sim-remote/scripts/viewport_screenshot.py

```
"""Capture a viewport screenshot and save it to disk.

Injected globals (via isaacsim_send.py --arg):
    output_path: str — File path for the output PNG (default: under tempfile.gettempdir())"""
def _capture()
```

### .claude/skills/isaac-sim-remote/scripts/viewport_video.py

```
"""Record the viewport to an MP4 video and save it to disk.

Video counterpart to viewport_screenshot.py. Uses Kit's native Movie Capture
pipeline (omni.kit.capture.viewport + omni.videoencoding) — no external ffmpeg.
Records the viewport render over timeline frames [start_frame, end_frame] as the
USD timeline advances, encoding directly to MP4.

This is timeline-driven: it advances the timeline itself and captures each frame.
It does NOT capture inside a manual world.step() control loop — for in-loop
physics/contact evidence, capture frames with viewport_screenshot.py inside the
loop and encode """
def _record()
```

### .claude/skills/isaac-sim-rendering/scripts/capture_pipeline.py

```
"""Standard Kit 110 / Isaac Sim 6.0+ headless capture pipeline."""
def setup_capture_pipeline(stage_path, width, height, renderer, settle_frames, film_iso)
def capture_frame(rgb_annot)
```

### .claude/skills/isaac-sim-rendering/scripts/look_at_camera.py

```
"""Look-at camera math for USD cameras (Z-up, USD -Z forward convention)."""
def look_at_matrix(eye, target, up)
```

### .claude/skills/isaac-sim-rendering/scripts/warehouse_lighting.py

```
"""Multi-layer warehouse lighting recipes for headless Isaac Sim rendering."""
def add_warehouse_lighting(stage, n_lights, settings)
def add_deep_aisle_lighting(stage, ceil_z, aisle_positions, grid_cols, grid_rows, facility_bounds)
```

### .claude/skills/isaac-sim-ros2-bridge/scripts/multi_robot_namespacing.py

```
"""Per-robot namespaced ROS 2 bridge action graph factory for fleet demos.

Creates one OmniGraph action graph per robot at `/ROS2_Bridge_<robot_name>`.
Each graph publishes namespaced odometry, TF, laser scan, and joint states,
and subscribes to a namespaced `cmd_vel` topic. A shared clock graph publishes
`/clock` for Nav2 `use_sim_time`.

All graphs use `OnPlaybackTick` as the execution trigger, so **no topics are
published until Play is pressed** — the graphs remain dormant in the stopped
state.

Reference scenario in the repo:
    source/standalone_examples/api/isaacsim.ros2.bridge/carter_mul"""
def _og()
def create_clock_graph(graph_path)
def create_ros2_bridge_for_robot(robot_name, robot_prim_path, lidar_prim_path, publish_joint_states)
def setup_fleet(robots, lidar_suffix)
```

### .claude/skills/isaac-sim-sensor/scripts/attach_lidar_imu.py

```
"""Attach an RTX Ouster LiDAR and a physics IMU to a robot chassis.

Creates mount xforms under the robot prim, references the Ouster OS1 sensor
asset with a chosen variant, and places an IMU at the chassis center.
Run with $ISAAC_SIM_DIR/python.sh."""
def attach_ouster_lidar(stage, robot_path, mount_offset, config, variant, tick_rate)
def attach_imu(stage, robot_path, mount_offset, tick_rate)
def attach_sensors(stage, robot_path, simulation_app)
```

### .claude/skills/isaac-sim-sensor/scripts/create_camera_sensor.py

```
"""Camera sensor creation and annotator attachment via the Isaac Sim RTX API.

Creates an RTX camera (``RtxCamera``) and wraps it in a ``CameraSensor`` that
builds the Replicator render product and exposes standard perception
annotators (RGB, depth, segmentation, bbox, normals, motion vectors).

Uses ``isaacsim.sensors.experimental.rtx`` throughout — no direct
``UsdGeom.Camera`` authoring or raw ``omni.replicator.core`` render-product
wiring. Run with ``$ISAAC_SIM_DIR/python.sh``."""
def create_camera_sensor(path, focal_length, resolution, annotators)
def attach_annotators(sensor, annotators)
```

### .claude/skills/isaac-sim-sensor/scripts/lidar_gmo_writer.py

```
"""RTX Lidar GMO (GenericModelOutput) writer pattern for Isaac Sim.

Demonstrates the Writer-based approach for consuming lidar scan data
without frame-drop under multitick.  Run with $ISAAC_SIM_DIR/python.sh."""
def create_lidar_with_gmo_writer(path, config, variant, simulation_app)
```

### .claude/skills/object-bin-packing/scripts/bin_pack_config.py

```
"""Generate a self-contained IRO bin-packing description file offline.

Emits a valid ``isaacsim.replicator.object`` YAML whose ``bin_pack`` harmonizer packs SimReady
cardboard boxes streamed from the Omniverse content server (no local assets, no ``PATH_TO_BOXES``
placeholder), plus a camera, a dome light, and the common output switches so it renders as-is.

The packed layout is gravity-stable: the ``bin_pack`` harmonizer places boxes bottom-up and only
where a box rests on the bin floor or is supported from below, so nothing floats. See the
``object-bin-packing`` SKILL for the headless run comma"""
def read_ext_version(path, ext_name)
def _randomized_range(start, end)
def _box_group(count, rel_usd)
def build_config(version, output_path, bin_size, fill_ratio, scale_counts, frames, seed)
def validate_config(config)
def _dump_str(config)
def main(argv)
```

### .claude/skills/physics-simulation/scripts/prim_physics_setup.py

```
"""Per-prim physics setup helpers for Isaac Sim / USD (Kit 110).

Provides setup_dynamic_body, setup_static_collider, and setup_kinematic_body
as the three standard physics configurations for scene prims."""
def setup_dynamic_body(stage, prim_path, mass_kg, com_offset)
def setup_static_collider(stage, prim_path)
def setup_kinematic_body(stage, prim_path)
```

### .claude/skills/profile-isaac-sim/scripts/compare_tracy_csvs.py

```
"""Compare two tab-separated Tracy CSV exports and print a summary.

Usage:
    python compare_tracy_csvs.py <reference.csv> <new.csv> [--top N] [--sep SEP]"""
def load_csv(path, sep)
def fmt_delta(ref_val, new_val)
def print_comparison(ref, new, top_n)
def main()
```

### .claude/skills/vlm-scene-captioning/scripts/starter_irc_config.py

```
"""Generate a starter standalone IRC (VLM Scene Captioning) config file offline.

Emits a minimal-but-valid ``isaacsim.replicator.caption.core`` YAML with global keys and a
``caption_configs`` block. It does NOT launch Isaac Sim, so it runs anywhere.

IRC requires the config `version` to be an EXACT match to `settings.VERSION` in the installed
isaacsim.replicator.caption.core -- which is NOT the extension's own `[package] version`. Prefer
`--from-ext <path>` to derive it; `--version` is an explicit override (rejected by IRC if wrong).

Usage:
    python3 starter_irc_config.py (--from-ext <build|e"""
def read_config_version(path, ext_name)
def build_config(version, camera_prim_path, output_path, scene_path, captions)
def main(argv)
```

### skills/actor-sdg-sweep-config/scripts/batch_actor_sdg.py

```
"""Preview or run Actor SDG sequentially for generated configuration variants."""
def find_actor_sdg(explicit)
def discover_variants(variants_dir)
def select_variants(variants, start_from, max_count)
def _read_error_summary(log_path)
def run_variant(python_launcher, actor_sdg_path, variant, log_dir, timeout)
def write_results(results, output_path)
def build_parser()
def main(argv)
```

### skills/actor-sdg-sweep-config/scripts/config_variation_generator.py

```
"""Generate deterministic Isaac Sim Replicator Agent configuration variations."""
def _load_yaml(path)
def _write_yaml(path, value)
def parse_path(path)
def get_nested(mapping, keys)
def set_nested(mapping, keys, value)
def _is_number(value)
def _validate_range(parameter)
def validate_inputs(base, sweep)
def sample_value(parameter, index, count, generator)
def _patch_writer_output_directories(config, output_dir)
def build_variants(base, sweep, output_dir, seed)
def _load_schema_document(uri)
def find_schema_directory(explicit)
def build_schema_validator(schema_dir)
def validate_variants(variants, validator)
def _find_managed_outputs(output_dir)
def _remove_managed_outputs(paths)
def write_variants(variants, output_dir)
def print_plan(base_path, sweep_path, output_dir, sweep, seed, validation_status)
def build_parser()
def main(argv)
```

### skills/data-collection-sim/scripts/minimal_sdg_pipeline.py

```
"""Minimal static-scene SDG pipeline using Isaac Sim Replicator.

Captures annotated RGB, depth, segmentation, and bounding-box frames to disk
via BasicWriter.  Run with $ISAAC_SIM_DIR/python.sh."""
def run_minimal_sdg_pipeline(output_dir, num_frames, rt_subframes)
```

### skills/data-collection-sim/scripts/production_capture_qa.py

```
"""Production headless Replicator capture with QA validation thresholds.

Runs a full SDG pipeline (RGB, depth, segmentation, bbox) then validates
every frame against configurable quality thresholds. Produces a JSON report
with per-frame metrics and an overall PASS/FAIL verdict for CI sign-off.

Usage:
    $ISAAC_SIM_DIR/python.sh production_capture_qa.py --config prod.yaml
    $ISAAC_SIM_DIR/python.sh production_capture_qa.py --num-frames 50 --output-dir /data/sdg_run"""
def run_capture(cfg)
def validate_output(output_dir, cfg)
```

### skills/data-collection-sim/scripts/shelf_pose_grid_capture.py

```
"""Overnight PoseWriter capture from a fixed camera grid over a shelf scene.

Sets up an NxM grid of cameras at fixed positions looking at a shelf, tags
objects with semantic labels, and runs a headless capture loop writing 6-DoF
pose annotations (JSON + RGB + optional debug overlays) to disk.

Run with:
    $ISAAC_SIM_DIR/python.sh shelf_pose_grid_capture.py         --num-frames 5000 --output-dir /data/pose_overnight"""
def parse_args()
def build_camera_grid(grid_rows, grid_cols, look_at)
def run_shelf_pose_capture(args)
```

### skills/generate-incident-config/scripts/starter_iri_config.py

```
"""Generate or validate an IRI (isaacsim.replicator.incident) event config file, offline.

Emits the YAML that the Event Config File panel loads, and that
``IncidentManager.setup_incidents_from_config_file()`` consumes. Does NOT launch
Isaac Sim, so it runs anywhere.

Two modes:

  generate (default)  build a config from --event specs and print it
  --validate FILE     structurally check an existing config and report problems

Validation matters because the loader is lenient in a way that hides mistakes:
``EventPropertyBase.set_value()`` copies only the keys it already knows about, so a
misspelle"""
def find_ext_tomls(path, ext_name)
def find_schema(path, ext_name)
def read_ext_version(path, ext_name)
def _coerce(value)
def parse_event_spec(spec, index)
def build_config(version, seed, report_dir, events)
def _validate_trigger(trigger, label, errors)
def _schema_error_message(error)
def validate_with_schema(data, schema_path, expected_major, strict)
def validate_config(data, expected_major)
def resolve_schema(args)
def main(argv)
```

### skills/isaac-sim-headless-deployment/scripts/batch_simulation.py

```
"""Headless batch simulation loop for Isaac Sim (Kit 110).

Runs N episodes, each loading a USD stage, stepping physics, and closing cleanly.
Run with $ISAAC_SIM_DIR/python.sh."""
def run_batch_simulation(scene_path, num_episodes, steps_per_episode, dt, device)
```

### skills/isaac-sim-installation/scripts/diagnose_logs.py

```
"""Scan Isaac Sim install or launch logs for likely root causes."""
def main()
```

### skills/isaac-sim-installation/scripts/install_binary.py

```
"""Plan or execute Isaac Sim standalone binary installation."""
def _safe_env(extra)
def default_platform()
def version_from_filename(filename)
def _strip_tags(text)
def _find_md5_near(content, start, end, window)
def parse_downloads(content)
def _version_key(version)
def _require_https(url)
def read_url(url, timeout)
def fetch_latest_downloads(docs_url, timeout)
def resolve_downloads(source)
def print_command(command)
def format_command(command)
def format_cwd_command(cwd, command)
def run(command, cwd, env)
def run_warmup(command)
def download_file(url, destination)
def extract_zip(zip_path, install_dir)
def make_shell_scripts_executable(install_dir)
def md5sum(path)
def post_install_script(install_dir, platform_name)
def warmup_script(install_dir, platform_name)
def script_command(script, platform_name)
def main()
```

### skills/isaac-sim-installation/scripts/install_container.py

```
"""Plan or execute an installation-only Isaac Sim container image pull."""
def print_command(command)
def run(command)
def require_supported_host()
def main()
```

### skills/isaac-sim-installation/scripts/install_python.py

```
"""Plan or execute Isaac Sim Python package installation."""
def _safe_env(extra)
def print_command(command, env)
def run(command, env)
def venv_python(env_dir)
def default_python()
def verify_nvidia_package_origins(report_path)
def main()
```

### skills/isaac-sim-installation/scripts/preflight.py

```
"""Collect Isaac Sim installation preflight information."""
def run(command, timeout)
def gpu_summary()
def memory_gb()
def disk_gb(path)
def python312_prefix()
def require_docker_host()
def main()
```

### skills/isaac-sim-installation/scripts/validate_install.py

```
"""Validate Isaac Sim binary, Python, or container installation."""
def _safe_env(extra)
def print_command(command)
def run(command, env)
def stop_process_tree(process)
def wait_for_process_stop(process, timeout)
def run_compatibility(command, env)
def require_container_host()
def workstation_checker_path(install_dir)
def workstation_checker_command(install_dir)
def main()
```

### skills/isaac-sim-remote/scripts/app_screenshot.py

```
"""Capture a full-application screenshot (entire window including UI) and save to disk.

Uses omni.kit.renderer.capture swapchain capture. Works in both --no-window headless
and windowed modes.

Injected globals (via isaacsim_send.py --arg):
    output_path: str — File path for the output PNG (default: under tempfile.gettempdir())."""
def _capture()
```

### skills/isaac-sim-remote/scripts/camera_control.py

```
"""Control the viewport camera position, orientation, and properties.

Uses isaacsim.core.experimental for camera transforms and objects.Camera for properties.
Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    action: str — "get" (default), "set", "look_at", or "list_cameras".
    camera_path: str — Camera prim path (default: active viewport camera).
    position: str/tuple — x,y,z for set (e.g. "5,5,5").
    orientation: str/tuple — Quaternion w,x,y,z for set (e.g. "1,0,0,0").
    target: str/tuple — x,y,z look-at target for "look_at" action."""
def _parse_floats(val)
def _get_active_camera_path()
def _resolve_camera()
```

### skills/isaac-sim-remote/scripts/capture_annotator.py

```
"""Capture annotator data (depth, normals, segmentation, etc.) from the active viewport.

Injected globals (via isaacsim_send.py --arg):
    annotator: str — Annotator name (default: distance_to_camera).
        Options: rgb, distance_to_camera, distance_to_image_plane, normals,
                 semantic_segmentation, instance_id_segmentation, etc.
    output_path: str — File path for output. .npy for raw array, .png for image
        (default: under tempfile.gettempdir())."""
def _capture()
```

### skills/isaac-sim-remote/scripts/console_log.py

```
"""Read the current Kit session log or recent log entries.

Useful for debugging errors after an operation fails silently.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "tail" (default), "errors", "search", or "path".
    num_lines: int — Number of lines to return for "tail" (default: 50).
    query: str — Search string for "search" action (case-insensitive).
    level: str — Filter by log level for "errors": "error" (default), "warn", "all"."""
```

### skills/isaac-sim-remote/scripts/execute_command.py

```
"""Dispatch a named, already-registered omni.kit.commands entry.

Lists the Kit command registry or runs one registered name with JSON kwargs.
Intended for live stage iteration through the localhost python_server control
plane (see SKILL.md Security). Names must match the registry; unknown names
raise ValueError before any execute call.

Injected globals (via isaacsim_send.py --arg):
    action: str — "run" (default) or "list".
    command_name: str — Registered command name for "run" (e.g. "CreateMeshPrimWithDefaultXform").
    kwargs: str — JSON string of keyword arguments (e.g. '{"prim_type":""""
def _resolve_registered_command(name)
```

### skills/isaac-sim-remote/scripts/health_check.py

```
"""Health check: verify Isaac Sim python server is responsive and report environment.

No injected globals required."""
def _run_health_check()
```

### skills/isaac-sim-remote/scripts/isaacsim_send.py

```
"""Localhost IPC client for Isaac Sim's code-editor python_server.

Sends a Python cell to the loopback endpoint (default ``127.0.0.1:8226``) used by
a trusted workstation Isaac Sim session. This is intentional local control-plane
IPC — see the skill Security section. Prefer ``--dry-run`` to print the payload
without contacting the server.

Usage:
    # Inline code
    python isaacsim_send.py 'print("hello")'

    # From stdin (pipe or heredoc)
    echo 'print("hello")' | python isaacsim_send.py

    # Send a .py file
    python isaacsim_send.py --file path/to/script.py

    # Send a file with in"""
def send_and_receive(host, port, source, timeout)
def _parse_arg_value(value)
def _inject_args(source, args)
def _wrap_isolated(source, args)
def _parse_args_kv(arg_list)
def _needs_envelope(args)
def main()
```

### skills/isaac-sim-remote/scripts/open_stage.py

```
"""Open, create, or save a USD stage.

Uses isaacsim.core.experimental.utils.stage.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "open" (default), "new", "save", or "info".
    usd_path: str — Path to USD file for open/save (required for open, optional for save).
    template: str — Stage template for "new" action (default: "empty"). Options: "empty", "default"."""
def _run()
```

### skills/isaac-sim-remote/scripts/prim_properties.py

```
"""Read or write arbitrary USD prim attributes.

Uses isaacsim.core.experimental.utils.prim for attribute access.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    prim_path: str — USD prim path (required).
    action: str — "get" (default), "set", or "list".
    attr_name: str — Attribute name for get/set (required for get/set).
    attr_value: str — Value to set (required for "set"). Parsed as Python literal.
    attr_type: str — Optional USD type name for create-on-set (e.g. "float", "double3", "string")."""
```

### skills/isaac-sim-remote/scripts/prim_transform.py

```
"""Get or set the world-space transform (position, orientation, scale) of a prim.

Uses isaacsim.core.experimental.utils.xform for pose and XformPrim for scale.
Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    prim_path: str — USD prim path (required).
    action: str — "get" (default) or "set".
    position: str/tuple — x,y,z for set (e.g. "1.0,2.0,3.0" or 1.0,2.0,3.0).
    orientation: str/tuple — Quaternion w,x,y,z for set (e.g. "1,0,0,0").
    scale: str/tuple — x,y,z scale for set (e.g. "1,1,1").

Examples:
    isaacsim_send.py --file pr"""
def _parse_vec(val)
```

### skills/isaac-sim-remote/scripts/select_prim.py

```
"""Select or query prim selection in the USD stage.

Selection is needed before many UI operations (Property panel, context menus).
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "get" (default), "set", "clear", or "all".
    prim_path: str — Prim path to select (for "set" action). Comma-separated for multiple."""
```

### skills/isaac-sim-remote/scripts/set_asset_root.py

```
"""Configure the Isaac Sim asset root path.

Use when Nucleus server is unavailable and you need cloud assets as fallback.

Injected globals (via isaacsim_send.py --arg):
    asset_root: str — Asset root URL. Special values:
        "production" -> S3 production assets (Isaac 5.0)
        "staging" -> S3 staging assets (Isaac 6.0, recommended for 6.x builds)
        "nucleus" -> Reset to default Nucleus server
        Any URL -> Set directly
    check: str — "true" to verify the path works (default: "true")."""
```

### skills/isaac-sim-remote/scripts/shutdown_app.py

```
"""Request a graceful shutdown of the running Isaac Sim application.

Injected globals (via ``isaacsim_send.py --arg``):
    exit_code: Process exit code. Defaults to zero."""
```

### skills/isaac-sim-remote/scripts/simulation_control.py

```
"""Control simulation playback: play, pause, stop, step, or query status.

Uses isaacsim.core.experimental.utils.app and isaacsim.core.simulation_manager.
Works in both windowed and --no-window headless modes.

Injected globals (via isaacsim_send.py --arg):
    action: str — "status" (default), "play", "pause", "stop", or "step".
    num_steps: int — Number of physics steps for "step" action (default: 1).
    dt: float — Physics timestep in seconds for setup (default: None, uses current)."""
```

### skills/isaac-sim-remote/scripts/stage_info.py

```
"""Print the current stage hierarchy and optionally detailed attributes for specific prims.

Works in both windowed and --no-window headless modes.

Injected args (via isaacsim_send.py --arg):
    mode: str — "tree" (default) or "list". Tree shows indented hierarchy, list shows flat paths.
    prim_path: str — Optional prim path to show detailed attributes for (default: None).
    filter_type: str — Optional type name filter (e.g. "Mesh", "Xform", "Camera"). Only show prims of this type.
    max_depth: int — Maximum traversal depth (default: unlimited). 0 = root only, 1 = direct children, etc.
  """
```

### skills/isaac-sim-remote/scripts/verify_asset.py

```
"""Verify that a concrete Isaac asset URL is reachable and can be referenced.

Injected globals via ``isaacsim_send.py --arg``:
    asset_path: Asset path under the Isaac asset root, or a full URL.
    asset_root: Optional preset or URL. ``staging`` maps to Isaac 6.0 S3.
    prim_path: Prim path for a reference-open check, default ``/World/Asset``.
    open_stage: Whether to reference the asset into a new stage, default True."""
def _as_bool(value)
def _set_asset_root(value)
def _configured_asset_root()
def _asset_url(path, requested_root)
def _resolved_root()
def _stat(url)
def _run()
```

### skills/isaac-sim-remote/scripts/viewport_screenshot.py

```
"""Capture a viewport screenshot and save it to disk.

Injected globals (via isaacsim_send.py --arg):
    output_path: str — File path for the output PNG (default: under tempfile.gettempdir())"""
def _capture()
```

### skills/isaac-sim-remote/scripts/viewport_video.py

```
"""Record the viewport to an MP4 video and save it to disk.

Video counterpart to viewport_screenshot.py. Uses Kit's native Movie Capture
pipeline (omni.kit.capture.viewport + omni.videoencoding) — no external ffmpeg.
Records the viewport render over timeline frames [start_frame, end_frame] as the
USD timeline advances, encoding directly to MP4.

This is timeline-driven: it advances the timeline itself and captures each frame.
It does NOT capture inside a manual world.step() control loop — for in-loop
physics/contact evidence, capture frames with viewport_screenshot.py inside the
loop and encode """
def _record()
```

### skills/isaac-sim-rendering/scripts/capture_pipeline.py

```
"""Standard Kit 110 / Isaac Sim 6.0+ headless capture pipeline."""
def setup_capture_pipeline(stage_path, width, height, renderer, settle_frames, film_iso)
def capture_frame(rgb_annot)
```

### skills/isaac-sim-rendering/scripts/look_at_camera.py

```
"""Look-at camera math for USD cameras (Z-up, USD -Z forward convention)."""
def look_at_matrix(eye, target, up)
```

### skills/isaac-sim-rendering/scripts/warehouse_lighting.py

```
"""Multi-layer warehouse lighting recipes for headless Isaac Sim rendering."""
def add_warehouse_lighting(stage, n_lights, settings)
def add_deep_aisle_lighting(stage, ceil_z, aisle_positions, grid_cols, grid_rows, facility_bounds)
```

### skills/isaac-sim-ros2-bridge/scripts/multi_robot_namespacing.py

```
"""Per-robot namespaced ROS 2 bridge action graph factory for fleet demos.

Creates one OmniGraph action graph per robot at `/ROS2_Bridge_<robot_name>`.
Each graph publishes namespaced odometry, TF, laser scan, and joint states,
and subscribes to a namespaced `cmd_vel` topic. A shared clock graph publishes
`/clock` for Nav2 `use_sim_time`.

All graphs use `OnPlaybackTick` as the execution trigger, so **no topics are
published until Play is pressed** — the graphs remain dormant in the stopped
state.

Reference scenario in the repo:
    source/standalone_examples/api/isaacsim.ros2.bridge/carter_mul"""
def _og()
def create_clock_graph(graph_path)
def create_ros2_bridge_for_robot(robot_name, robot_prim_path, lidar_prim_path, publish_joint_states)
def setup_fleet(robots, lidar_suffix)
```

### skills/isaac-sim-sensor/scripts/attach_lidar_imu.py

```
"""Attach an RTX Ouster LiDAR and a physics IMU to a robot chassis.

Creates mount xforms under the robot prim, references the Ouster OS1 sensor
asset with a chosen variant, and places an IMU at the chassis center.
Run with $ISAAC_SIM_DIR/python.sh."""
def attach_ouster_lidar(stage, robot_path, mount_offset, config, variant, tick_rate)
def attach_imu(stage, robot_path, mount_offset, tick_rate)
def attach_sensors(stage, robot_path, simulation_app)
```

### skills/isaac-sim-sensor/scripts/create_camera_sensor.py

```
"""Camera sensor creation and annotator attachment via the Isaac Sim RTX API.

Creates an RTX camera (``RtxCamera``) and wraps it in a ``CameraSensor`` that
builds the Replicator render product and exposes standard perception
annotators (RGB, depth, segmentation, bbox, normals, motion vectors).

Uses ``isaacsim.sensors.experimental.rtx`` throughout — no direct
``UsdGeom.Camera`` authoring or raw ``omni.replicator.core`` render-product
wiring. Run with ``$ISAAC_SIM_DIR/python.sh``."""
def create_camera_sensor(path, focal_length, resolution, annotators)
def attach_annotators(sensor, annotators)
```

### skills/isaac-sim-sensor/scripts/lidar_gmo_writer.py

```
"""RTX Lidar GMO (GenericModelOutput) writer pattern for Isaac Sim.

Demonstrates the Writer-based approach for consuming lidar scan data
without frame-drop under multitick.  Run with $ISAAC_SIM_DIR/python.sh."""
def create_lidar_with_gmo_writer(path, config, variant, simulation_app)
```

### skills/object-bin-packing/scripts/bin_pack_config.py

```
"""Generate a self-contained IRO bin-packing description file offline.

Emits a valid ``isaacsim.replicator.object`` YAML whose ``bin_pack`` harmonizer packs SimReady
cardboard boxes streamed from the Omniverse content server (no local assets, no ``PATH_TO_BOXES``
placeholder), plus a camera, a dome light, and the common output switches so it renders as-is.

The packed layout is gravity-stable: the ``bin_pack`` harmonizer places boxes bottom-up and only
where a box rests on the bin floor or is supported from below, so nothing floats. See the
``object-bin-packing`` SKILL for the headless run comma"""
def read_ext_version(path, ext_name)
def _randomized_range(start, end)
def _box_group(count, rel_usd)
def build_config(version, output_path, bin_size, fill_ratio, scale_counts, frames, seed)
def validate_config(config)
def _dump_str(config)
def main(argv)
```

### skills/physics-simulation/scripts/prim_physics_setup.py

```
"""Per-prim physics setup helpers for Isaac Sim / USD (Kit 110).

Provides setup_dynamic_body, setup_static_collider, and setup_kinematic_body
as the three standard physics configurations for scene prims."""
def setup_dynamic_body(stage, prim_path, mass_kg, com_offset)
def setup_static_collider(stage, prim_path)
def setup_kinematic_body(stage, prim_path)
```

### skills/profile-isaac-sim/scripts/compare_tracy_csvs.py

```
"""Compare two tab-separated Tracy CSV exports and print a summary.

Usage:
    python compare_tracy_csvs.py <reference.csv> <new.csv> [--top N] [--sep SEP]"""
def load_csv(path, sep)
def fmt_delta(ref_val, new_val)
def print_comparison(ref, new, top_n)
def main()
```

### skills/vlm-scene-captioning/scripts/starter_irc_config.py

```
"""Generate a starter standalone IRC (VLM Scene Captioning) config file offline.

Emits a minimal-but-valid ``isaacsim.replicator.caption.core`` YAML with global keys and a
``caption_configs`` block. It does NOT launch Isaac Sim, so it runs anywhere.

IRC requires the config `version` to be an EXACT match to `settings.VERSION` in the installed
isaacsim.replicator.caption.core -- which is NOT the extension's own `[package] version`. Prefer
`--from-ext <path>` to derive it; `--version` is an explicit override (rejected by IRC if wrong).

Usage:
    python3 starter_irc_config.py (--from-ext <build|e"""
def read_config_version(path, ext_name)
def build_config(version, camera_prim_path, output_path, scene_path, captions)
def main(argv)
```

### source/deprecated/isaacsim.core.api/python/impl/__init__.py

```
"""Provides SimulationContext, PhysicsContext, and World APIs for physics settings, simulation control, scenes, tasks, callbacks, and data logging."""
```

### source/deprecated/isaacsim.core.api/python/impl/articulations/__init__.py

```
"""Provides high-level API classes for managing articulations and their components in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/articulations/articulation_gripper.py

```
"""Provide gripper control functionality for articulation-based grippers with open and closed state management."""
class ArticulationGripper(object)
    """Gripper controller for articulation-based grippers.

Args:
    gripper_dof_names: List of DOF names for the gripper joints.
    gripper_open_position: Joint positions for the open state.
    gripper_closed_position: Joint positions for the closed state."""
    def __init__(self, gripper_dof_names, gripper_open_position, gripper_closed_position)
    def open_position(self)
    def closed_position(self)
    def dof_indices(self)
    def initialize(self, root_prim_path, articulation_controller)
    def set_positions(self, positions)
    def get_positions(self)
    def get_velocities(self)
    def set_velocities(self, velocities)
    def apply_action(self, action)
```

### source/deprecated/isaacsim.core.api/python/impl/articulations/articulation_subset.py

```
"""A utility class for working with a subset of joints in a robot articulation."""
def require_initialized(func)
class ArticulationSubset()
    """A utility class for viewing a subset of the joints in a robot Articulation object.

This class can be helpful in two ways:

1) The order of joints returned by a robot Articulation may not match the order of joints
   expected by a function.

2) A function may only care about a subset of the joint st"""
    def __init__(self, articulation, joint_names)
    def is_initialized(self)
    def num_joints(self)
    def joint_indices(self)
    def get_joint_positions(self)
    def get_joint_velocities(self)
    def get_joint_efforts(self)
    def get_measured_joint_efforts(self)
    def get_applied_joint_efforts(self)
    def set_joint_positions(self, positions)
    def set_joint_velocities(self, velocities)
    def set_joint_efforts(self, efforts)
    def map_to_articulation_order(self, joint_values)
    def make_articulation_action(self, joint_positions, joint_velocities)
    def apply_action(self, joint_positions, joint_velocities)
    def get_applied_action(self)
    def get_joints_state(self)
    def get_joint_subset_indices(self)
    def _get_joint_indices(self)
```

### source/deprecated/isaacsim.core.api/python/impl/controllers/__init__.py

```
"""Provides controller classes for managing articulations, grippers, and other robotic components in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/controllers/articulation_controller.py

```
"""PD controller implementation for articulated bodies with position, velocity, and effort control capabilities."""
class ArticulationController(object)
    """PD controller of all degrees of freedom of an articulation. Can apply position targets, velocity targets, and efforts.

Check out the required tutorials at https://docs.isaacsim.omniverse.nvidia.com/latest/index.html"""
    def __init__(self)
    def initialize(self, articulation_view)
    def _require_initialized(self)
    def apply_action(self, control_actions)
    def set_gains(self, kps, kds, save_to_usd)
    def get_gains(self)
    def switch_control_mode(self, mode)
    def switch_dof_control_mode(self, dof_index, mode)
    def set_max_efforts(self, values, joint_indices)
    def get_max_efforts(self)
    def set_effort_modes(self, mode, joint_indices)
    def get_effort_modes(self)
    def get_joint_limits(self)
    def get_applied_action(self)
```

### source/deprecated/isaacsim.core.api/python/impl/controllers/base_controller.py

```
"""Base controller module."""
class BaseController(ABC)
    """Abstract base class for robot controllers.

Args:
    name: Name identifier for the controller."""
    def __init__(self, name)
    def forward(self)
    def reset(self)
```

### source/deprecated/isaacsim.core.api/python/impl/controllers/base_gripper_controller.py

```
"""Base classes for implementing gripper controllers that can open and close grippers in Isaac Sim."""
class BaseGripperController(BaseController)
    """Abstract base class for gripper controllers.

Args:
    name: Name identifier for the controller."""
    def __init__(self, name)
    def forward(self, action, current_joint_positions)
    def open(self, current_joint_positions)
    def close(self, current_joint_positions)
    def reset(self)
```

### source/deprecated/isaacsim.core.api/python/impl/loggers/__init__.py

```
"""Provides logging functionality for data collection and analysis in Isaac Sim applications."""
```

### source/deprecated/isaacsim.core.api/python/impl/loggers/data_logger.py

```
"""Provide data logging functionality for collecting, storing, and replaying simulation data."""
class DataLogger()
    """Provide data collection, storage, and replay functionality for simulation data.

Collects simulation data at runtime and saves it to disk for later replay or analysis.
Supports pausing and resuming data collection during simulation."""
    def __init__(self)
    def add_data(self, data, current_time_step, current_time)
    def get_num_of_data_frames(self)
    def pause(self)
    def start(self)
    def is_started(self)
    def reset(self)
    def get_data_frame(self, data_frame_index)
    def add_data_frame_logging_func(self, func)
    def save(self, log_path)
    def load(self, log_path)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/__init__.py

```
"""Provides material APIs for isaacsim.core.api."""
```

### source/deprecated/isaacsim.core.api/python/impl/materials/deformable_material.py

```
"""Stub module for the removed DeformableMaterial and DeformableMaterialView classes."""
class DeformableMaterial()
    """Stub for the removed DeformableMaterial class.

DeformableMaterial is no longer available because Omniverse PhysX removed
the deprecated deformable body features it depended on. Use the new material
APIs in isaacsim.core.experimental.materials instead.

Args:
    *args: Positional arguments (ignored"""
    def __init__(self)
class DeformableMaterialView()
    """Stub for the removed DeformableMaterialView class.

DeformableMaterialView is no longer available because Omniverse PhysX removed
the deprecated deformable body features it depended on. Use the new material
APIs in isaacsim.core.experimental.materials instead.

Args:
    *args: Positional arguments """
    def __init__(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/deformable_material_view.py

```
"""Stub module for the removed DeformableMaterialView class."""
class DeformableMaterialView()
    """Stub for the removed DeformableMaterialView class.

DeformableMaterialView is no longer available because Omniverse PhysX removed
the deprecated deformable body features it depended on. Use the new material
APIs in isaacsim.core.experimental.materials instead.

Args:
    *args: Positional arguments """
    def __init__(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/omni_glass.py

```
"""High level wrapper for creating/encapsulating Omniverse Glass (``OmniGlass``) material prims."""
class OmniGlass(VisualMaterial)
    """High-level wrapper for creating/encapsulating Omniverse Glass (``OmniGlass``) material prims.

Args:
    prim_path: USD prim path for the material.
    name: Name identifier.
    shader: Existing shader to use.
    color: Glass tint color RGB.
    ior: Index of refraction.
    depth: Glass depth/thi"""
    def __init__(self, prim_path, name, shader, color, ior, depth, thin_walled)
    def set_color(self, color)
    def get_color(self)
    def set_ior(self, ior)
    def get_ior(self)
    def set_depth(self, depth)
    def get_depth(self)
    def set_thin_walled(self, thin_walled)
    def get_thin_walled(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/omni_pbr.py

```
"""High level wrapper for creating/encapsulating ``OmniPBR`` physically-based rendering material prims."""
class OmniPBR(VisualMaterial)
    """OmniPBR physically-based rendering material.

Args:
    prim_path: USD prim path for the material.
    name: Name identifier.
    shader: Existing shader to use.
    texture_path: Path to diffuse texture.
    texture_scale: Texture UV scale (x, y).
    texture_translate: Texture UV translation (x, y"""
    def __init__(self, prim_path, name, shader, texture_path, texture_scale, texture_translate, color)
    def set_color(self, color)
    def get_color(self)
    def set_texture(self, path)
    def get_texture(self)
    def set_texture_scale(self, x, y)
    def set_texture_translate(self, x, y)
    def get_texture_scale(self)
    def get_texture_translate(self)
    def set_project_uvw(self, flag)
    def get_project_uvw(self)
    def set_reflection_roughness(self, amount)
    def get_reflection_roughness(self)
    def set_metallic_constant(self, amount)
    def get_metallic_constant(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/particle_material.py

```
"""High level wrapper for creating/configuring position-based-dynamics (PBD) particle materials for simulating fluids, cloth and inflatables."""
class ParticleMaterial()
    """A wrapper around position-based-dynamics (PBD) material for particles used to simulate fluids, cloth and inflatables.

Applies the `PhysxSchema.PhysxPBDMaterialAPI` to a material prim.

Note:
    Currently, only a single material per particle system is supported which applies
    to all objects that"""
    def __init__(self, prim_path, name, friction, particle_friction_scale, damping, viscosity, vorticity_confinement, surface_tension, cohesion, adhesion, particle_adhesion_scale, adhesion_offset_scale, gravity_scale, lift, drag)
    def prim_path(self)
    def prim(self)
    def material(self)
    def name(self)
    def initialize(self, physics_sim_view)
    def is_valid(self)
    def post_reset(self)
    def set_friction(self, value)
    def set_particle_friction_scale(self, value)
    def set_damping(self, value)
    def set_viscosity(self, value)
    def set_vorticity_confinement(self, value)
    def set_surface_tension(self, value)
    def set_cohesion(self, value)
    def set_adhesion(self, value)
    def set_particle_adhesion_scale(self, value)
    def set_adhesion_offset_scale(self, value)
    def set_gravity_scale(self, value)
    def set_lift(self, value)
    def set_drag(self, value)
    def get_friction(self)
    def get_particle_friction_scale(self)
    def get_damping(self)
    def get_viscosity(self)
    def get_vorticity_confinement(self)
    def get_surface_tension(self)
    def get_cohesion(self)
    def get_adhesion(self)
    def get_particle_adhesion_scale(self)
    def get_adhesion_offset_scale(self)
    def get_gravity_scale(self)
    def get_lift(self)
    def get_drag(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/particle_material_view.py

```
"""Provides a view class for managing particle material prims and their physics properties in bulk operations."""
class ParticleMaterialView()
    """The view class to deal with particle material prims.

Provides high-level functions to deal with particle material (1 or more particle materials)
as well as its attributes/properties. This object wraps all matching materials found at the regex provided
at prim_paths_expr.
This object wraps all match"""
    def __init__(self, prim_paths_expr, name, frictions, particle_friction_scales, dampings, viscosities, vorticity_confinements, surface_tensions, cohesions, adhesions, particle_adhesion_scales, adhesion_offset_scales, gravity_scales, lifts, drags)
    def count(self)
    def name(self)
    def _apply_material_api(self, index)
    def is_physics_handle_valid(self)
    def is_valid(self, indices)
    def post_reset(self)
    def initialize(self, physics_sim_view)
    def set_frictions(self, values, indices)
    def get_frictions(self, indices, clone)
    def set_dampings(self, values, indices)
    def get_dampings(self, indices, clone)
    def set_gravity_scales(self, values, indices)
    def get_gravity_scales(self, indices, clone)
    def set_lifts(self, values, indices)
    def get_lifts(self, indices, clone)
    def set_drags(self, values, indices)
    def get_drags(self, indices, clone)
    def set_viscosities(self, values, indices)
    def get_viscosities(self, indices, clone)
    def set_cohesions(self, values, indices)
    def get_cohesions(self, indices, clone)
    def set_adhesions(self, values, indices)
    def get_adhesions(self, indices, clone)
    def set_particle_adhesion_scales(self, values, indices)
    def get_particle_adhesion_scales(self, indices, clone)
    def set_adhesion_offset_scales(self, values, indices)
    def get_adhesion_offset_scales(self, indices, clone)
    def set_surface_tensions(self, values, indices)
    def get_surface_tensions(self, indices, clone)
    def set_vorticity_confinements(self, values, indices)
    def get_vorticity_confinements(self, indices, clone)
    def set_particle_friction_scales(self, values, indices)
    def get_particle_friction_scales(self, indices, clone)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/physics_material.py

```
"""Module for creating and managing physics materials with friction and restitution properties."""
class PhysicsMaterial(object)
    """Physics material for defining friction and restitution properties.

Args:
    prim_path: USD prim path for the material.
    name: Name identifier.
    static_friction: Static friction coefficient.
    dynamic_friction: Dynamic friction coefficient.
    restitution: Restitution (bounciness) coeffici"""
    def __init__(self, prim_path, name, static_friction, dynamic_friction, restitution)
    def prim_path(self)
    def prim(self)
    def name(self)
    def material(self)
    def set_dynamic_friction(self, friction)
    def get_dynamic_friction(self)
    def set_static_friction(self, friction)
    def get_static_friction(self)
    def set_restitution(self, restitution)
    def get_restitution(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/preview_surface.py

```
"""High level wrapper for creating/encapsulating USD PreviewSurface material prims for basic rendering."""
class PreviewSurface(VisualMaterial)
    """USD PreviewSurface material for basic rendering.

Args:
    prim_path: USD prim path for the material.
    name: Name identifier.
    shader: Existing shader to use.
    color: Diffuse color RGB.
    roughness: Surface roughness (0-1).
    metallic: Metallic value (0-1).

Raises:
    ValueError: If """
    def __init__(self, prim_path, name, shader, color, roughness, metallic)
    def set_color(self, color)
    def get_color(self)
    def set_roughness(self, roughness)
    def get_roughness(self)
    def set_metallic(self, metallic)
    def get_metallic(self)
```

### source/deprecated/isaacsim.core.api/python/impl/materials/visual_material.py

```
"""Base class for visual material representations in Isaac Sim."""
class VisualMaterial(object)
    """Base class for visual material representations.

Args:
    name: Name identifier for the material.
    prim_path: USD prim path for the material.
    prim: The USD prim object.
    shaders_list: List of shaders used by the material.
    material: The USD material object."""
    def __init__(self, name, prim_path, prim, shaders_list, material)
    def material(self)
    def shaders_list(self)
    def name(self)
    def prim_path(self)
    def prim(self)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/__init__.py

```
"""API for creating and managing primitive geometric objects in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/objects/capsule.py

```
"""High level wrappers for creating and manipulating capsule geometry prims with visual, collision, and physics properties."""
class VisualCapsule(SingleGeometryPrim)
    """High-level wrapper to create or encapsulate a visual capsule.

.. note::

    Visual capsules (Capsule shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by S"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material)
    def set_radius(self, radius)
    def get_radius(self)
    def set_height(self, height)
    def get_height(self)
class FixedCapsule(VisualCapsule)
    """High level wrapper to create or encapsulate a fixed capsule.

.. note::

    Fixed capsules (Capsule shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Sc"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material)
class DynamicCapsule(SingleRigidPrim, FixedCapsule)
    """High level wrapper to create/encapsulate a dynamic capsule.

.. note::

    Dynamic capsules (Capsule shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material, mass, density, linear_velocity, angular_velocity)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/cone.py

```
"""Provides high-level wrapper classes for creating and managing cone geometry prims with different physics behaviors."""
class VisualCone(SingleGeometryPrim)
    """High level wrapper to create or encapsulate a visual cone.

.. note::

    Visual cones (Cone shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene clas"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material)
    def set_radius(self, radius)
    def get_radius(self)
    def set_height(self, height)
    def get_height(self)
class FixedCone(VisualCone)
    """High-level wrapper to create or encapsulate a fixed cone.

.. note::

    Fixed cones (Cone shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene class"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material)
class DynamicCone(SingleRigidPrim, FixedCone)
    """High-level wrapper to create or encapsulate a dynamic cone.

.. note::

    Dynamic cones (Cone shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene class"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material, mass, density, linear_velocity, angular_velocity)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/cuboid.py

```
"""High-level wrappers for creating and managing visual, fixed, and dynamic cuboid objects with collision and physics properties."""
class VisualCuboid(SingleGeometryPrim)
    """High-level wrapper to create or encapsulate a visual cuboid.

.. note::

    Visual cuboids (Cube shapes) have no collisions (Collider API) or rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, size, visual_material)
    def set_size(self, size)
    def get_size(self)
class FixedCuboid(VisualCuboid)
    """High level wrapper to create/encapsulate a fixed cuboid.

.. note::

    Fixed cuboids (Cube shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Shortname to be used as a key by Scene class"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, size, visual_material, physics_material)
class DynamicCuboid(SingleRigidPrim, FixedCuboid)
    """High level wrapper to create/encapsulate a dynamic cuboid.

.. note::

    Dynamic cuboids (Cube shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene clas"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, size, visual_material, physics_material, mass, density, linear_velocity, angular_velocity)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/cylinder.py

```
"""Provides high-level wrapper classes for creating and manipulating cylinder objects with different physics behaviors in Isaac Sim."""
class VisualCylinder(SingleGeometryPrim)
    """High-level wrapper to create or encapsulate a visual cylinder.

.. note::

    Visual cylinders (Cylinder shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key b"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material)
    def set_radius(self, radius)
    def get_radius(self)
    def set_height(self, height)
    def get_height(self)
class FixedCylinder(VisualCylinder)
    """High-level wrapper to create/encapsulate a fixed cylinder.

.. note::

    Fixed cylinders (Cylinder shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Sc"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material)
class DynamicCylinder(SingleRigidPrim, FixedCylinder)
    """High level wrapper to create/encapsulate a dynamic cylinder.

.. note::

    Dynamic cylinders (Cylinder shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Shortname to be used as a key by Sc"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, height, visual_material, physics_material, mass, density, linear_velocity, angular_velocity)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/ground_plane.py

```
"""Module for creating and managing ground plane objects in Isaac Sim."""
class GroundPlane(object)
    """High level wrapper to create or encapsulate a ground plane.

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene class.
        Note: needs to be unique if the object is added to the Scene.
    size: Length of each edge.
    z_positi"""
    def __init__(self, prim_path, name, size, z_position, scale, visible, color, physics_material, visual_material)
    def prim_path(self)
    def name(self)
    def prim(self)
    def xform_prim(self)
    def collision_geometry_prim(self)
    def initialize(self, physics_sim_view)
    def post_reset(self)
    def is_valid(self)
    def apply_physics_material(self, physics_material, weaker_than_descendants)
    def get_applied_physics_material(self)
    def set_world_pose(self, position, orientation)
    def get_world_pose(self)
    def get_default_state(self)
    def set_default_state(self, position, orientation)
```

### source/deprecated/isaacsim.core.api/python/impl/objects/sphere.py

```
"""High level wrappers for creating and manipulating sphere primitives with different physics behaviors in Isaac Sim."""
class VisualSphere(SingleGeometryPrim)
    """High level wrapper to create or encapsulate a visual sphere.

.. note::

    Visual spheres (Sphere shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scen"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, visual_material)
    def set_radius(self, radius)
    def get_radius(self)
class FixedSphere(VisualSphere)
    """High level wrapper to create/encapsulate a fixed sphere.

.. note::

    Fixed spheres (Sphere shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API).

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene cl"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, visual_material, physics_material)
class DynamicSphere(SingleRigidPrim, FixedSphere)
    """High level wrapper to create/encapsulate a dynamic sphere.

.. note::

    Dynamic spheres (Sphere shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)

Args:
    prim_path: Prim path of the Prim to encapsulate or create.
    name: Short name to be used as a key by Scene cl"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, color, radius, visual_material, physics_material, mass, density, linear_velocity, angular_velocity)
```

### source/deprecated/isaacsim.core.api/python/impl/physics_context/__init__.py

```
"""Physics context API for managing physics simulation settings and environments in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/physics_context/physics_context.py

```
"""High level wrapper for creating and configuring PhysicsScene prims and managing physics simulation settings."""
class PhysicsContext(object)
    """Provide high-level functions for managing physics scene and simulation settings.

Create a PhysicsScene prim at the specified prim path when no PhysicsScene is present in the current stage.
If a PhysicsScene already exists, use the existing scene and apply default settings regardless of the specifie"""
    def __init__(self, physics_dt, prim_path, sim_params, set_defaults)
    def prim_path(self)
    def device(self)
    def use_gpu_sim(self)
    def use_gpu_pipeline(self)
    def use_fabric(self)
    def __del__(self)
    def warm_start(self)
    def get_current_physics_scene_prim(self)
    def _create_new_physics_scene(self, prim_path)
    def set_physics_dt(self, dt, substeps)
    def get_physics_dt(self)
    def enable_fabric(self, enable)
    def enable_ccd(self, flag)
    def is_ccd_enabled(self)
    def enable_stabilization(self, flag)
    def enable_stablization(self, flag)
    def is_stablization_enabled(self)
    def enable_gpu_dynamics(self, flag)
    def is_gpu_dynamics_enabled(self)
    def set_broadphase_type(self, broadcast_type)
    def get_broadphase_type(self)
    def set_solver_type(self, solver_type)
    def get_solver_type(self)
    def set_gravity(self, value)
    def get_gravity(self)
    def set_physx_update_transformations_settings(self, update_to_usd, update_velocities_to_usd, output_velocities_local_space)
    def get_physx_update_transformations_settings(self)
    def _step(self, current_time, update_fabric)
    def set_invert_collision_group_filter(self, invert_collision_group_filter)
    def get_invert_collision_group_filter(self)
    def set_bounce_threshold(self, value)
    def get_bounce_threshold(self)
    def set_friction_offset_threshold(self, value)
    def get_friction_offset_threshold(self)
    def set_friction_correlation_distance(self, value)
    def get_friction_correlation_distance(self)
    def set_enable_scene_query_support(self, enable_scene_query_support)
    def get_enable_scene_query_support(self)
    def set_gpu_max_rigid_contact_count(self, value)
    def get_gpu_max_rigid_contact_count(self)
    def set_gpu_max_rigid_patch_count(self, value)
    def get_gpu_max_rigid_patch_count(self)
    def set_gpu_found_lost_pairs_capacity(self, value)
    def get_gpu_found_lost_pairs_capacity(self)
    def set_gpu_found_lost_aggregate_pairs_capacity(self, value)
    def get_gpu_found_lost_aggregate_pairs_capacity(self)
    def set_gpu_total_aggregate_pairs_capacity(self, value)
    def get_gpu_total_aggregate_pairs_capacity(self)
    def set_gpu_max_soft_body_contacts(self, value)
    def get_gpu_max_soft_body_contacts(self)
    def set_gpu_max_particle_contacts(self, value)
    def get_gpu_max_particle_contacts(self)
    def set_gpu_heap_capacity(self, value)
    def get_gpu_heap_capacity(self)
    def set_gpu_temp_buffer_capacity(self, value)
    def get_gpu_temp_buffer_capacity(self)
    def set_gpu_max_num_partitions(self, value)
    def get_gpu_max_num_partitions(self)
    def set_gpu_collision_stack_size(self, value)
    def get_gpu_collision_stack_size(self)
    def set_solve_articulation_contact_last(self, solve_articulation_contact_last)
    def get_solve_articulation_contact_last(self)
```

### source/deprecated/isaacsim.core.api/python/impl/robots/__init__.py

```
"""Classes for creating and managing robots and robot views in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/robots/robot.py

```
"""High-level API for creating and controlling robots as articulations in Isaac Sim."""
class Robot(SingleArticulation)
    """Implementation (on ``SingleArticulation`` class) to deal with an articulation prim as a robot.

.. warning::

    The robot (articulation) object must be initialized in order to be able to operate on it.
    See the ``initialize`` method for more details.

Args:
    prim_path: Prim path of the Prim """
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, articulation_controller)
    def post_reset(self)
```

### source/deprecated/isaacsim.core.api/python/impl/robots/robot_view.py

```
"""Handles multiple robot (articulation) prims efficiently through regex-based selection for batch operations."""
class RobotView(Articulation)
    """Implementation on the ``Articulation`` class to deal with articulation prims as robots.

This class wraps all matching articulations found at the regex provided in the ``prim_paths_expr`` argument.

.. warning::

    The robot articulation view object must be initialized in order to be able to opera"""
    def __init__(self, prim_paths_expr, name, positions, translations, orientations, scales, visibilities)
    def post_reset(self)
```

### source/deprecated/isaacsim.core.api/python/impl/scenes/__init__.py

```
"""Provides the Scene API for managing and registering simulation scenes in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/scenes/scene.py

```
"""Scene management system for Isaac Sim environments that provides methods to add, manage, and interact with objects in the USD stage."""
class Scene(object)
    """Provides methods to add objects of interest in the stage, retrieve their information, and reset their default state in an easy way.

Example:

.. code-block:: python

    >>> from isaacsim.core.api.scenes import Scene
    >>>
    >>> scene = Scene()
    >>> scene
    <isaacsim.core.api.scenes.scene."""
    def __init__(self)
    def __del__(self)
    def stage(self)
    def add(self, obj)
    def add_ground_plane(self, size, z_position, name, prim_path, static_friction, dynamic_friction, restitution, color)
    def add_default_ground_plane(self, z_position, name, prim_path, static_friction, dynamic_friction, restitution)
    def post_reset(self)
    def _finalize(self, physics_sim_view)
    def remove_object(self, name, registry_only)
    def get_object(self, name)
    def object_exists(self, name)
    def clear(self, registry_only)
    def compute_object_AABB(self, name)
    def enable_bounding_boxes_computations(self)
    def disable_bounding_boxes_computations(self)
```

### source/deprecated/isaacsim.core.api/python/impl/scenes/scene_registry.py

```
"""Provides a registry system for tracking and managing different types of objects added to Isaac Sim scenes."""
class SceneRegistry(object)
    """Class to keep track of the different types of objects added to the scene.

Example:

.. code-block:: python

    >>> from isaacsim.core.api.scenes import SceneRegistry
    >>>
    >>> scene_registry = SceneRegistry()
    >>> scene_registry
    <isaacsim.core.api.scenes.scene_registry.SceneRegistry o"""
    def __init__(self)
    def articulated_systems(self)
    def rigid_objects(self)
    def rigid_prim_views(self)
    def rigid_contact_views(self)
    def geometry_prim_views(self)
    def articulated_views(self)
    def robot_views(self)
    def robots(self)
    def xforms(self)
    def sensors(self)
    def xform_prim_views(self)
    def deformable_prims(self)
    def deformable_prim_views(self)
    def deformable_materials(self)
    def deformable_material_views(self)
    def cloth_prims(self)
    def cloth_prim_views(self)
    def particle_systems(self)
    def particle_system_views(self)
    def particle_materials(self)
    def particle_material_views(self)
    def _register_object(self, name, obj, object_dict)
    def add_rigid_object(self, name, rigid_object)
    def add_rigid_prim_view(self, name, rigid_prim_view)
    def add_rigid_contact_view(self, name, rigid_contact_view)
    def add_articulated_system(self, name, articulated_system)
    def add_articulated_view(self, name, articulated_view)
    def add_geometry_object(self, name, geometry_object)
    def add_geometry_prim_view(self, name, geometry_prim_view)
    def add_robot(self, name, robot)
    def add_robot_view(self, name, robot_view)
    def add_xform_view(self, name, xform_prim_view)
    def add_deformable(self, name, deformable)
    def add_deformable_view(self, name, deformable_prim_view)
    def add_deformable_material(self, name, deformable_material)
    def add_deformable_material_view(self, name, deformable_material_view)
    def add_cloth(self, name, cloth)
    def add_cloth_view(self, name, cloth_prim_view)
    def add_particle_system(self, name, particle_system)
    def add_particle_system_view(self, name, particle_system_view)
    def add_particle_material(self, name, particle_material)
    def add_particle_material_view(self, name, particle_material_view)
    def add_xform(self, name, xform)
    def add_sensor(self, name, sensor)
    def name_exists(self, name)
    def remove_object(self, name)
    def get_object(self, name)
```

### source/deprecated/isaacsim.core.api/python/impl/sensors/__init__.py

```
"""Sensor API module providing base sensor functionality and rigid contact views for Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/sensors/base_sensor.py

```
"""Provides a base class for sensor implementations in Isaac Sim."""
class BaseSensor(SingleXFormPrim)
    """Provides common properties and methods to deal with prims as a sensor.

.. note::

    This class, which inherits from ``SingleXFormPrim``, does not currently add any new properties or methods to it.
    Its definition is intended for future implementations.

Args:
    prim_path: Prim path of the pr"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible)
    def initialize(self, physics_sim_view)
    def post_reset(self)
```

### source/deprecated/isaacsim.core.api/python/impl/sensors/rigid_contact_view.py

```
"""Provides high level functions to deal with rigid prims for tracking their contact interactions through filters."""
class RigidContactView(object)
    """Provides high-level functions to deal with rigid prims (one or many) that track their contacts through filters, as well as their attributes/properties.

This class wraps all matching rigid prims found by the regex provided in the ``prim_paths_expr`` argument.

.. warning::

    The rigid prim view o"""
    def __init__(self, prim_paths_expr, filter_paths_expr, name, prepare_contact_sensors, disable_stablization, disable_stabilization, max_contact_count)
    def num_shapes(self)
    def num_filters(self)
    def _prepare_contact_reporter(self, prim_at_path)
    def is_physics_handle_valid(self)
    def initialize(self, physics_sim_view)
    def get_net_contact_forces(self, indices, clone, dt)
    def get_contact_force_matrix(self, indices, clone, dt)
    def get_contact_force_data(self, indices, clone, dt)
    def get_friction_data(self, indices, clone, dt)
```

### source/deprecated/isaacsim.core.api/python/impl/simulation_context/__init__.py

```
"""Provides the SimulationContext API for managing simulation state and execution in Isaac Sim."""
```

### source/deprecated/isaacsim.core.api/python/impl/simulation_context/simulation_context.py

```
"""Provide a comprehensive simulation context for managing physics simulation, rendering, and time-related events in Isaac Sim."""
class SimulationContext()
    """Provides functions for managing time-related events and simulation control.

Handles physics and render stepping, callback function management for physics steps,
timeline events (pause or play), stage operations (open/close), and other simulation events.

Includes a PhysicsContext instance for physi"""
    def __init__(self, physics_dt, rendering_dt, stage_units_in_meters, physics_prim_path, sim_params, set_defaults, backend, device, stage)
    def __new__(cls)
    def instance(cls)
    def clear_instance(cls)
    def app(self)
    def current_time_step_index(self)
    def current_time(self)
    def stage(self)
    def backend(self)
    def device(self)
    def backend_utils(self)
    def physics_sim_view(self)
    def get_physics_context(self)
    def set_simulation_dt(self, physics_dt, rendering_dt)
    def get_physics_dt(self)
    def get_rendering_dt(self)
    def set_block_on_render(self, block)
    def get_block_on_render(self)
    def initialize_simulation_context_async(self)
    def initialize_physics(self)
    def reset(self, soft)
    def reset_async(self, soft)
    def step(self, render, update_fabric)
    def render(self)
    def render_async(self)
    def clear(self)
    def is_simulating(self)
    def is_playing(self)
    def is_stopped(self)
    def play_async(self)
    def play(self)
    def pause_async(self)
    def pause(self)
    def stop_async(self)
    def stop(self)
    def add_physics_callback(self, callback_name, callback_fn)
    def remove_physics_callback(self, callback_name)
    def physics_callback_exists(self, callback_name)
    def clear_physics_callbacks(self)
    def add_stage_callback(self, callback_name, callback_fn)
    def remove_stage_callback(self, callback_name)
    def stage_callback_exists(self, callback_name)
    def clear_stage_callbacks(self)
    def add_timeline_callback(self, callback_name, callback_fn)
    def remove_timeline_callback(self, callback_name)
    def timeline_callback_exists(self, callback_name)
    def clear_timeline_callbacks(self)
    def add_render_callback(self, callback_name, callback_fn)
    def remove_render_callback(self, callback_name)
    def render_callback_exists(self, callback_name)
    def clear_render_callbacks(self)
    def clear_all_callbacks(self)
    def skip_next_stage_open_callback(self)
    def _init_stage(self, physics_dt, rendering_dt, stage_units_in_meters, physics_prim_path, sim_params, set_defaults, backend, device)
    def _initialize_stage_async(self, physics_dt, rendering_dt, stage_units_in_meters, physics_prim_path, sim_params, set_defaults, device)
    def _setup_default_callback_fns(self)
    def _physics_timer_callback_fn(self, step_size, context)
    def _timeline_timer_callback_fn(self, event)
    def _stage_open_callback_fn(self, event)
    def _on_post_physics_ready(self, event)
```

### source/deprecated/isaacsim.core.api/python/impl/tasks/__init__.py

```
"""Core task implementations for Isaac Sim including base task functionality and specific tasks like follow target, pick and place, and stacking."""
```

### source/deprecated/isaacsim.core.api/python/impl/tasks/base_task.py

```
"""Base class for creating and managing simulation tasks in Isaac Sim environments."""
class BaseTask(object)
    """This class provides a way to set up a task in a scene and modularize adding objects to a stage.

It gets observations needed for the behavioral layer, calculates metrics needed about the task,
calls certain things pre-stepping, creates multiple tasks at the same time and much more.

Check out the re"""
    def __init__(self, name, offset)
    def device(self)
    def scene(self)
    def name(self)
    def set_up_scene(self, scene)
    def _move_task_objects_to_their_frame(self)
    def get_task_objects(self)
    def get_observations(self)
    def calculate_metrics(self)
    def is_done(self)
    def pre_step(self, time_step_index, simulation_time)
    def post_reset(self)
    def get_description(self)
    def cleanup(self)
    def set_params(self)
    def get_params(self)

```python
def get_observations(self) -> dict:
        """Current observations from the objects needed for the behavioral layer.

        Raises:
            NotImplementedError: Must be implemented by subclass.

        Returns:
            Dictionary containing task-specific observations.
        """
        raise NotImplementedError
```
```

### source/deprecated/isaacsim.core.api/python/impl/tasks/follow_target.py

```
"""Abstract task implementation for robot end effector target following scenarios."""
class FollowTarget(ABC, BaseTask)
    """Abstract task for following a target with a robot end effector.

Args:
    name: Task name identifier.
    target_prim_path: USD path for the target prim.
    target_name: Name for the target object.
    target_position: Initial target position.
    target_orientation: Initial target orientation.
  """
    def __init__(self, name, target_prim_path, target_name, target_position, target_orientation, offset)
    def set_up_scene(self, scene)
    def set_robot(self)
    def set_params(self, target_prim_path, target_name, target_position, target_orientation)
    def get_params(self)
    def get_observations(self)
    def calculate_metrics(self)
    def is_done(self)
    def target_reached(self)
    def pre_step(self, time_step_index, simulation_time)
    def post_reset(self)
    def add_obstacle(self, position)
    def remove_obstacle(self, name)
    def get_obstacle_to_delete(self)
    def obstacles_exist(self)
    def cleanup(self)

```python
def get_observations(self) -> dict:
        """Get current task observations.

        Returns:
            Dictionary with robot and target observations.
        """
        joints_state = self._robot.get_joints_state()
        target_position, target_orientation = self._target.get_local_pose()

        # The target cannot be below the ground plane; use a copy to avoid mutating the prim's data
        clamped_position = np.array(target_position)
        if clamped_position[2] <= (0.035 / get_stage_units()):
            clamped_position[2] = 0.035 / get_stage_units()

        return {
            self._robot.name: {
                "joint_positions": np.array(joints_state.positions),
                "joint_velocities": np.array(joints_state.velocities),
            },
            self._target.name: {"position": clamped_position, "orientation": np.array(target_orientation)},
        }
```
```

### source/deprecated/isaacsim.core.api/python/impl/tasks/pick_place.py

```
"""Abstract base class for pick and place tasks involving cube manipulation with a robot."""
class PickPlace(ABC, BaseTask)
    """Abstract task for picking and placing a cube with a robot.

Args:
    name: Task name identifier.
    cube_initial_position: Initial cube position.
    cube_initial_orientation: Initial cube orientation.
    target_position: Target position for placing.
    cube_size: Size of the cube.
    offset: O"""
    def __init__(self, name, cube_initial_position, cube_initial_orientation, target_position, cube_size, offset)
    def set_up_scene(self, scene)
    def set_robot(self)
    def set_params(self, cube_position, cube_orientation, target_position)
    def get_params(self)
    def get_observations(self)
    def pre_step(self, time_step_index, simulation_time)
    def post_reset(self)
    def calculate_metrics(self)
    def is_done(self)

```python
def get_observations(self) -> dict:
        """Gets current task observations for the cube and robot.

        Returns:
            Observations keyed by cube name and robot name, including cube pose, target position, robot joint positions,
            and end effector position when available.
        """
        joints_state = self._robot.get_joints_state()
        cube_position, cube_orientation = self._cube.get_local_pose()
        robot_obs = {
            "joint_positions": joints_state.positions,
        }
        if hasattr(self._robot, "end_effector") and self._robot.end_effector is not None:
            end_effector_position, _ = self._robot.end_effector.get_local_pose()
            robot_obs["end_effector_position"] = end_effector_position
        return {
            self._cube.name: {
                "position": cube_position,
                "orientation": cube_orientation,
                "target_position": self._target_position,
            },
            self._robot.name: robot_obs,
        }
```
```

### source/deprecated/isaacsim.core.api/python/impl/tasks/stacking.py

```
"""Provides an abstract base class for stacking multiple cubes with a robot."""
class Stacking(ABC, BaseTask)
    """Abstract task for stacking multiple cubes with a robot.

Args:
    name: Task name identifier.
    cube_initial_positions: Initial positions for all cubes.
    cube_initial_orientations: Initial orientations for cubes.
    stack_target_position: Position at which to stack cubes.
    cube_size: Size """
    def __init__(self, name, cube_initial_positions, cube_initial_orientations, stack_target_position, cube_size, offset)
    def set_up_scene(self, scene)
    def set_robot(self)
    def set_params(self, cube_name, cube_position, cube_orientation, stack_target_position)
    def get_params(self)
    def get_observations(self)
    def pre_step(self, time_step_index, simulation_time)
    def post_reset(self)
    def get_cube_names(self)
    def calculate_metrics(self)
    def is_done(self)

```python
def get_observations(self) -> dict:
        """Gets current task observations.

        Returns:
            Dictionary containing robot joint and end effector data plus cube pose and target position data.
        """
        joints_state = self._robot.get_joints_state()
        end_effector_position, _ = self._robot.end_effector.get_local_pose()
        observations = {
            self._robot.name: {
                "joint_positions": joints_state.positions,
                "end_effector_position": end_effector_position,
            }
        }
        for i in range(self._num_of_cubes):
            cube_position, cube_orientation = self._cubes[i].get_local_pose()
            observations[self._cubes[i].name] = {
                "position": cube_position,
                "orientation": cube_orientation,
                "target_position": np.array(
                    [
                        self._stack_target_position[0],
                        self._stack_target_position[1],
                        (self._cube_size[2] * i) + self._cube_size[2] / 2.0,
                    ]
                ),
            }
        return observations
```
```

### source/deprecated/isaacsim.core.api/python/impl/world/__init__.py

```
"""High-level world management API for Isaac Sim that provides the main World class for scene orchestration."""
```

### source/deprecated/isaacsim.core.api/python/impl/world/world.py

```
"""Provide a comprehensive physics simulation world environment with scene management, task orchestration, and data logging capabilities."""
class World(SimulationContext)
    """Provide a comprehensive physics simulation world environment with scene management and task orchestration.

Extends SimulationContext with additional functionality for managing tasks and scenes.
SimulationContext handles time-related events such as physics and render steps, callback
function managem"""
    def __init__(self, physics_dt, rendering_dt, stage_units_in_meters, physics_prim_path, sim_params, set_defaults, backend, device)
    def clear_instance(cls)
    def scene(self)
    def add_task(self, task)
    def is_tasks_scene_built(self)
    def get_current_tasks(self)
    def get_task(self, name)
    def get_observations(self, task_name)
    def calculate_metrics(self, task_name)
    def is_done(self, task_name)
    def get_data_logger(self)
    def initialize_physics(self)
    def reset(self, soft)
    def reset_async_set_up_scene(self, soft)
    def reset_async_no_set_up_scene(self, soft)
    def reset_async(self, soft)
    def step(self, render, step_sim, update_fabric)
    def step_async(self, step_size)
    def clear(self)

```python
def get_observations(self, task_name: str | None = None) -> dict:
        """Get observations from tasks that were added.

        Args:
            task_name: Task name to ask for. If None, returns observations from all tasks.

        Returns:
            Task observations for the specified task or all tasks.

        Raises:
            Exception: If the task name does not exist in the current world tasks.

        Example:

        .. code-block:: python

            >>> world.get_observations("custom_task")
            {'obs': [0]}
        """
        if task_name is not None:
            return self.get_task(task_name).get_observations()
        else:
            observations = {}
            for task in self._current_tasks.values():
                observations.update(task.get_observations())
            return observations
```
```

### source/deprecated/isaacsim.core.api/python/tests/__init__.py

```
"""Tests for the Isaac Sim Core API module."""
```

### source/deprecated/isaacsim.core.api/python/tests/common.py

```
"""Common test utilities."""
class CoreTestCase(AsyncTestCase)
    """Base test class that automatically times all test methods.

This class extends omni.kit.test.AsyncTestCase to automatically print
the execution time of each test method. All test classes should inherit
from this instead of omni.kit.test.AsyncTestCase directly."""
    def setUp(self)
    def tearDown(self)
class TestProperties()
    """Test properties."""
    def scalar_prop_test(self, getFunc, setFunc, set_value, is_stopped)
    def bool_prop_test(self, getFunc, setFunc, set_value_1, set_value_2, is_stopped)
    def int_prop_test(self, getFunc, setFunc, set_value, set_value_2, is_stopped)
    def vector_prop_test(self, getFunc, setFunc, set_value_1, set_value_2, is_stopped)
```

### source/deprecated/isaacsim.core.api/python/tests/test_articulation.py

```
"""Test for articulation."""
class TestArticulationController(CoreTestCase)
    """Test articulation controller."""
    def test_articulation_controller_raises_runtime_error_before_initialize(self)
class TestSingleArticulation(CoreTestCase)
    """Test single articulation."""
    def setUp(self, device)
    def tearDown(self)
    def test_get_applied_action(self, add_view_to_scene)
    def test_apply_partial_articulation(self, add_view_to_scene)
    def test_dof_efforts(self, add_view_to_scene)
    def test_joint_forces(self, add_view_to_scene)
    def test_articulation_joint_signs(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_articulation_determinism.py

```
"""Test for articulation determinism."""
class TestArticulationDeterminism(CoreTestCase)
    """Test articulation determinism."""
    def setUp(self)
    def tearDown(self)
    def test_inconsistent_result(self)
    def _test_franka_slow_convergence(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_articulation_view.py

```
"""Verifies the deprecated Articulation view API across torch, numpy, and warp backends. Covers poses, velocities, joint targets, drive properties, dynamics tensors, tendon properties, and physics lifecycle behavior."""
class TestArticulationView(CoreTestCase)
    """Test articulation view."""
    def setUp(self)
    def tearDown(self)
    def setup_world(self, backend, device)
    def add_frankas(self, backend)
    def add_humanoids(self, backend)
    def add_cartpoles(self, backend)
    def add_shadow_hands(self, backend, device)
    def _step(self)
    def test_world_poses_torch(self)
    def test_world_poses_numpy(self)
    def test_world_poses_warp(self)
    def test_velocities_torch_per_device(self)
    def test_velocities_numpy(self)
    def test_velocities_warp(self)
    def test_velocities_torch(self)
    def test_linear_velocities_torch(self)
    def test_linear_velocities_numpy(self)
    def test_linear_velocities_warp(self)
    def test_angular_velocities_torch(self)
    def test_angular_velocities_numpy(self)
    def test_angular_velocities_warp(self)
    def test_friction_coefficients_torch(self)
    def test_friction_coefficients_numpy(self)
    def test_friction_coefficients_warp(self)
    def test_armatures_torch(self)
    def test_armatures_numpy(self)
    def test_armatures_warp(self)
    def test_physics_callback(self)
    def test_local_pose_torch(self)
    def test_local_pose_numpy(self)
    def test_local_pose_warp(self)
    def test_effort_modes(self)
    def test_gains_torch(self)
    def test_gains_numpy(self)
    def test_partial_default_gain_update_preserves_unselected_joints(self)
    def test_partial_warp_default_gain_update_handles_indexed_arrays(self)
    def test_gains_warp(self)
    def test_switch_control_mode(self)
    def test_switch_dof_control_mode(self)
    def test_max_efforts_torch(self)
    def test_max_efforts_numpy(self)
    def test_max_efforts_warp(self)
    def test_physics_properties_torch(self)
    def test_physics_properties_numpy(self)
    def test_physics_properties_warp(self)
    def test_initializing_views(self)
    def test_physics_handles_none(self)
    def test_position_targets_torch(self)
    def test_position_targets_numpy(self)
    def test_position_targets_warp(self)
    def test_velocity_targets_torch(self)
    def test_velocity_targets_numpy(self)
    def test_velocity_targets_warp(self)
    def test_joint_velocities_torch(self)
    def test_joint_velocities_numpy(self)
    def test_joint_velocities_warp(self)
    def test_joint_positions_torch(self)
    def test_joint_positions_numpy(self)
    def test_joint_positions_warp(self)
    def test_joint_efforts_torch(self)
    def test_joint_efforts_numpy(self)
    def test_joint_efforts_warp(self)
    def test_body_indices(self)
    def test_efforts(self)
    def test_jacobians(self)
    def test_mass_matrices(self)
    def test_coriolis_centrifugal(self)
    def test_generalized_gravity(self)
    def test_masses_torch(self)
    def test_masses_numpy(self)
    def test_masses_warp(self)
    def test_com_torch(self)
    def test_com_numpy(self)
    def test_com_warp(self)
    def test_inertia_torch(self)
    def test_inertia_numpy(self)
    def test_inertia_warp(self)
    def test_fixed_tendon_properties_torch(self)
    def test_fixed_tendon_properties_numpy(self)
    def test_fixed_tendon_properties_warp(self)
    def test_position_iteration_count_torch(self)
    def test_position_iteration_count_numpy(self)
    def test_position_iteration_count_warp(self)
    def test_velocity_iteration_count_torch(self)
    def test_velocity_iteration_count_numpy(self)
    def test_velocity_iteration_count_warp(self)
    def test_stabilization_thresholds_torch(self)
    def test_stabilization_thresholds_numpy(self)
    def test_stabilization_thresholds_warp(self)
    def test_sleep_thresholds_torch(self)
    def test_sleep_thresholds_numpy(self)
    def test_sleep_thresholds_warp(self)
    def test_enabled_self_collisions_torch(self)
    def test_enabled_self_collisions_numpy(self)
    def test_enabled_self_collisions_warp(self)
    def test_get_dof_types(self)
    def test_get_measured_joint_efforts(self)
    def test_get_measured_joint_forces(self)
    def test_pause_resume_motion(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_geometry_prim.py

```
"""Test for geometry prim."""
class TestSingleGeometryPrim(CoreTestCase)
    """Test single geometry prim."""
    def setUp(self)
    def tearDown(self)
    def test_collision_approximation(self)
    def test_collision_enabled(self)
    def test_physics_material(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_particle_material.py

```
"""Test for particle material."""
class TestParticleMaterial(CoreTestCase, TestProperties)
    """Test particle material."""
    def setUp(self)
    def tearDown(self)
    def test_cloth_prim(self)
    def test_constructor_optional_properties_without_simulation_context(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_prims_utils.py

```
"""Test for prims utils."""
class TestPrims(CoreTestCase)
    """Test prims."""
    def setUp(self)
    def tearDown(self)
    def test_get_all_matching_child_prims(self)
    def test_create_prim(self)
    def test_is_prim_non_root_articulation_link(self)
    def test_get_articulation_root_api_prim_path(self)
    def test_find_matching_prim_paths(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_rigid_prim.py

```
"""Test for rigid prim."""
class TestSingleRigidPrimPose(CoreTestCase)
    """Test single rigid prim pose."""
    def setUp(self)
    def tearDown(self)
    def test_position_orientation_scale(self)
    def test_set_local_pose(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_rigid_prim_view.py

```
"""Test for rigid prim view."""
class TestRigidPrimView(CoreTestCase)
    """Test rigid prim view."""
    def setUp(self)
    def tearDown(self)
    def test_rigid_prim_view_gpu_pipeline(self)
    def test_rigid_prim_view_cpu_pipeline(self)
    def _setup_scene(self)
    def _setup_contacts_scene(self)
    def _setup_friction_scene(self)
    def _runner(self)
    def apply_forces_and_torques_at_pos_test(self, is_global, apply_at_pos)
    def friction_force_test(self, force_multiplier)
    def contact_force_test(self)
    def com_test(self)
    def inertias_test(self)
    def world_poses_test(self, usd)
    def local_poses_test(self, usd)
    def linear_velocities_test(self, usd)
    def angular_velocities_test(self, usd)
    def masses_test(self, usd)
    def densities_test(self, usd)
    def sleep_thresholds_test(self, usd)
    def enable_disable_physics_test(self, usd)
    def enable_disable_gravity_test(self, usd)
    def default_state_post_reset_test(self, usd)
    def default_state_before_reset_test(self)
    def transforms_test(self)
    def velocities_test(self, usd)
    def apply_forces_test(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_scene_registry.py

```
"""Test for scene registry."""
class TestSceneRegistry(CoreTestCase)
    """Test scene registry behavior."""
    def _add_method_names(self)
    def test_add_methods_reject_duplicate_names(self)
    def test_add_methods_reject_names_registered_in_other_categories(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_sdf_shape_view.py

```
"""Test for sdf shape view."""
class TestRigidPrimView(CoreTestCase)
    """Test rigid prim view."""
    def setUp(self)
    def tearDown(self)
    def test_sdf_shape_view_gpu_pipeline(self)
    def _setup_sdf_scene(self, num_query_points, prepare_sdf_schemas)
    def _runner(self)
    def signed_distance_test(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_simulation_context.py

```
"""Test for simulation context."""
class TestSimulationContext(CoreTestCase)
    """Test simulation context."""
    def setUp(self)
    def tearDown(self)
    def test_singleton(self)
    def test_set_defaults(self)
    def test_default_dt(self)
    def test_physics_context_solve_articulation_contact_last(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_world.py

```
"""Test for world."""
class TestScene(CoreTestCase)
    """Test scene."""
    def setUp(self)
    def tearDown(self)
    def test_clear_instance(self)
    def test_create_new_stage(self)
    def test_clear_world(self)
    def test_clear_scene_ref(self)
    def test_clear_prim_view(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_xform_prim_pose.py

```
"""Test for xform prim pose."""
class TestXformPrimPose(CoreTestCase)
    """Test xform prim pose."""
    def setUp(self)
    def tearDown(self)
    def test_position_orientation_scale(self)
```

### source/deprecated/isaacsim.core.api/python/tests/test_xform_prim_view.py

```
"""Test for xform prim view."""
class TestXFormPrimView(CoreTestCase)
    """Test x form prim view."""
    def setUp(self)
    def tearDown(self)
    def test_list_of_regular_exprs(self)
    def test_world_poses(self)
    def test_world_poses_fabric(self)
    def test_local_pose(self)
    def test_local_on_init(self)
    def test_visibilities(self)
    def test_scale_units_resolve(self)
```

### source/deprecated/isaacsim.core.prims/python/__init__.py

```
"""Provides high-level wrappers for working with USD prims, geometry, rigid bodies, articulations, and particle systems."""
```

### source/deprecated/isaacsim.core.prims/python/impl/__init__.py

```
"""Implementation module for various prim classes including geometry, physics, articulation, and transformation primitives."""
```

### source/deprecated/isaacsim.core.prims/python/impl/articulation.py

```
"""High level wrapper to deal with prims (one or many) that have the Root Articulation API applied and their attributes/properties."""
def _warp_default_state_value(value)
def _warp_contiguous_if_indexed(value)
class Articulation(XFormPrim)
    """Provide a high-level wrapper for prims that have the Root Articulation API applied.

Handle attributes and properties of single or multiple articulated prims.

Wrap all matching articulations found at the regex provided at the ``prim_paths_expr`` argument.

.. note::

    Each prim will have ``xform"""
    def __init__(self, prim_paths_expr, name, positions, translations, orientations, scales, visibilities, reset_xform_properties)
    def __del__(self)
    def _invalidate_physics_handle_callback(self, event)
    def num_dof(self)
    def num_bodies(self)
    def num_shapes(self)
    def num_joints(self)
    def num_fixed_tendons(self)
    def body_names(self)
    def dof_names(self)
    def joint_names(self)
    def is_physics_handle_valid(self)
    def _convert_joint_names_to_indices(self, joint_names, dof_indices)
    def get_body_index(self, body_name)
    def get_dof_index(self, dof_name)
    def get_dof_types(self, dof_names)
    def get_dof_limits(self)
    def get_drive_types(self)
    def get_joint_index(self, joint_name)
    def get_link_index(self, link_name)
    def set_friction_coefficients(self, values, indices, joint_indices, joint_names)
    def get_friction_coefficients(self, indices, joint_indices, joint_names, clone)
    def set_armatures(self, values, indices, joint_indices, joint_names)
    def get_armatures(self, indices, joint_indices, joint_names, clone)
    def get_articulation_body_count(self)
    def set_joint_position_targets(self, positions, indices, joint_indices, joint_names)
    def set_joint_positions(self, positions, indices, joint_indices, joint_names)
    def set_joint_velocity_targets(self, velocities, indices, joint_indices, joint_names)
    def set_joint_velocities(self, velocities, indices, joint_indices, joint_names)
    def set_joint_efforts(self, efforts, indices, joint_indices, joint_names)
    def get_applied_joint_efforts(self, indices, joint_indices, joint_names, clone)
    def get_measured_joint_efforts(self, indices, joint_indices, joint_names, clone)
    def get_measured_joint_forces(self, indices, joint_indices, joint_names, clone)
    def get_joint_positions(self, indices, joint_indices, joint_names, clone)
    def get_joint_velocities(self, indices, joint_indices, joint_names, clone)
    def apply_action(self, control_actions, indices)
    def get_applied_actions(self, clone)
    def set_world_poses(self, positions, orientations, indices, usd)
    def get_world_poses(self, indices, clone, usd)
    def get_local_poses(self, indices)
    def set_local_poses(self, translations, orientations, indices)
    def set_velocities(self, velocities, indices)
    def get_velocities(self, indices, clone)
    def set_linear_velocities(self, velocities, indices)
    def get_linear_velocities(self, indices, clone)
    def set_angular_velocities(self, velocities, indices)
    def get_angular_velocities(self, indices, clone)
    def set_joints_default_state(self, positions, velocities, efforts)
    def get_joints_default_state(self)
    def get_joints_state(self)
    def get_effort_modes(self, indices, joint_indices, joint_names)
    def set_effort_modes(self, mode, indices, joint_indices, joint_names)
    def set_max_efforts(self, values, indices, joint_indices, joint_names)
    def get_max_efforts(self, indices, joint_indices, joint_names, clone)
    def set_max_joint_velocities(self, values, indices, joint_indices, joint_names)
    def get_joint_max_velocities(self, indices, joint_indices, joint_names, clone)
    def set_gains(self, kps, kds, indices, joint_indices, joint_names, save_to_usd)
    def _update_default_gains(self, update_default_kps, update_default_kds, indices, joint_indices)
    def get_gains(self, indices, joint_indices, joint_names, clone)
    def switch_control_mode(self, mode, indices, joint_indices, joint_names)
    def switch_dof_control_mode(self, mode, dof_index, indices)
    def set_solver_position_iteration_counts(self, counts, indices)
    def get_solver_position_iteration_counts(self, indices)
    def set_solver_velocity_iteration_counts(self, counts, indices)
    def get_solver_velocity_iteration_counts(self, indices)
    def set_stabilization_thresholds(self, thresholds, indices)
    def get_stabilization_thresholds(self, indices)
    def set_enabled_self_collisions(self, flags, indices)
    def get_enabled_self_collisions(self, indices)
    def set_sleep_thresholds(self, thresholds, indices)
    def get_sleep_thresholds(self, indices)
    def get_jacobian_shape(self)
    def get_mass_matrix_shape(self)
    def get_jacobians(self, indices, clone)
    def get_mass_matrices(self, indices, clone)
    def get_coriolis_and_centrifugal_forces(self, indices, joint_indices, joint_names, clone)
    def get_generalized_gravity_forces(self, indices, joint_indices, joint_names, clone)
    def get_body_masses(self, indices, body_indices, clone)
    def get_body_inv_masses(self, indices, body_indices, clone)
    def get_body_coms(self, indices, body_indices, clone)
    def get_body_inertias(self, indices, body_indices, clone)
    def get_body_inv_inertias(self, indices, body_indices, clone)
    def get_body_disable_gravity(self, indices, body_indices, clone)
    def set_body_masses(self, values, indices, body_indices)
    def set_body_inertias(self, values, indices, body_indices)
    def set_body_coms(self, positions, orientations, indices, body_indices)
    def set_body_disable_gravity(self, values, indices, body_indices)
    def get_fixed_tendon_stiffnesses(self, indices, clone)
    def get_fixed_tendon_dampings(self, indices, clone)
    def get_fixed_tendon_limit_stiffnesses(self, indices, clone)
    def get_fixed_tendon_limits(self, indices, clone)
    def get_fixed_tendon_rest_lengths(self, indices, clone)
    def get_fixed_tendon_offsets(self, indices, clone)
    def set_fixed_tendon_properties(self, stiffnesses, dampings, limit_stiffnesses, limits, rest_lengths, offsets, indices)
    def pause_motion(self)
    def resume_motion(self)
    def initialize(self, physics_sim_view)
    def _on_physics_ready(self, event)
    def _on_prim_deletion(self, prim_path)
    def _on_post_reset(self, event)
```

### source/deprecated/isaacsim.core.prims/python/impl/cloth_prim.py

```
"""Deprecated ClothPrim stub module."""
class ClothPrim()
    """Deprecated cloth prim class. No longer available.

Args:
    *args: Unused positional arguments.
    **kwargs: Unused keyword arguments.

Raises:
    NotImplementedError: Raised because ClothPrim is no longer available."""
    def __init__(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/deformable_prim.py

```
"""Deprecated DeformablePrim stub module."""
class DeformablePrim()
    """Deprecated deformable prim class. No longer available.

Args:
    *args: Unused positional arguments.
    **kwargs: Unused keyword arguments.

Raises:
    NotImplementedError: Always raised because DeformablePrim is no longer available."""
    def __init__(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/geometry_prim.py

```
"""High level wrapper to deal with geom prims (one or many) as well as their attributes/properties."""
class GeometryPrim(XFormPrim)
    """High level wrapper to deal with geom prims (one or many) as well as their attributes/properties.

This class wraps all matching geom prims found at the regex provided to the ``prim_paths_expr`` argument.

.. note::

    Each prim will have ``xformOp:orient``, ``xformOp:translate`` and ``xformOp:scal"""
    def __init__(self, prim_paths_expr, name, positions, translations, orientations, scales, visibilities, reset_xform_properties, collisions, track_contact_forces, prepare_contact_sensors, disable_stablization, contact_filter_prim_paths_expr, max_contact_count)
    def geoms(self)
    def initialize(self, physics_sim_view)
    def set_contact_offsets(self, offsets, indices)
    def get_contact_offsets(self, indices)
    def set_rest_offsets(self, offsets, indices)
    def get_rest_offsets(self, indices)
    def set_torsional_patch_radii(self, radii, indices)
    def get_torsional_patch_radii(self, indices)
    def set_min_torsional_patch_radii(self, radii, indices)
    def get_min_torsional_patch_radii(self, indices)
    def set_collision_approximations(self, approximation_types, indices)
    def get_collision_approximations(self, indices)
    def enable_collision(self, indices)
    def disable_collision(self, indices)
    def is_collision_enabled(self, indices)
    def apply_collision_apis(self, indices)
    def apply_physics_materials(self, physics_materials, weaker_than_descendants, indices)
    def get_applied_physics_materials(self, indices)
    def get_net_contact_forces(self, indices, clone, dt)
    def get_contact_force_matrix(self, indices, clone, dt)
    def get_contact_force_data(self, indices, clone, dt)
    def get_friction_data(self, indices, clone, dt)
```

### source/deprecated/isaacsim.core.prims/python/impl/particle_system.py

```
"""Provides high-level functionality for managing particle systems in Isaac Sim."""
class ParticleSystem()
    """Provides high-level functions to deal with particle systems (1 or more particle systems) as well as their attributes/properties.

This object wraps all matching particle systems found by the regex provided at prim_paths_expr.
Note: not all the attributes of PhysxSchema.PhysxParticleSystem are curren"""
    def __init__(self, prim_paths_expr, name, particle_systems_enabled, simulation_owners, contact_offsets, rest_offsets, particle_contact_offsets, solid_rest_offsets, fluid_rest_offsets, enable_ccds, solver_position_iteration_counts, max_depenetration_velocities, winds, max_neighborhoods, max_velocities, global_self_collisions_enabled)
    def __del__(self)
    def _apply_material_binding_api(self, index)
    def count(self)
    def name(self)
    def is_physics_handle_valid(self)
    def initialize(self, physics_sim_view)
    def _invalidate_physics_handle_callback(self, event)
    def is_valid(self, indices)
    def post_reset(self)
    def apply_particle_materials(self, particle_materials, indices)
    def get_applied_particle_materials(self, indices)
    def set_particle_contact_offsets(self, values, indices)
    def set_solid_rest_offsets(self, values, indices)
    def set_fluid_rest_offsets(self, values, indices)
    def set_winds(self, values, indices)
    def set_max_velocities(self, values, indices)
    def set_max_depenetration_velocities(self, values, indices)
    def set_rest_offsets(self, values, indices)
    def set_contact_offsets(self, values, indices)
    def set_solver_position_iteration_counts(self, values, indices)
    def set_max_neighborhoods(self, values, indices)
    def set_global_self_collisions_enabled(self, values, indices)
    def set_enable_ccds(self, values, indices)
    def set_particle_systems_enabled(self, values, indices)
    def set_simulation_owners(self, values, indices)
    def get_particle_contact_offsets(self, indices, clone)
    def get_solid_rest_offsets(self, indices, clone)
    def get_fluid_rest_offsets(self, indices, clone)
    def get_winds(self, indices, clone)
    def get_max_velocities(self, indices)
    def get_max_depenetration_velocities(self, indices)
    def get_rest_offsets(self, indices)
    def get_contact_offsets(self, indices)
    def get_solver_position_iteration_counts(self, indices)
    def get_max_neighborhoods(self, indices)
    def get_global_self_collisions_enabled(self, indices)
    def get_enable_ccds(self, indices)
    def get_particle_systems_enabled(self, indices)
    def get_simulation_owners(self, indices)
```

### source/deprecated/isaacsim.core.prims/python/impl/prim.py

```
"""Provides a wrapper class for USD prims that offers a unified interface for managing collections of prims in Isaac Sim."""
class Prim(object)
    """A wrapper for USD prims that provides a unified interface for managing collections of prims in Isaac Sim.

This class encapsulates one or more USD prims identified by path expressions and provides common functionality
for prim management, validation, and lifecycle callbacks. It automatically handles"""
    def __init__(self, prim_paths_expr, name)
    def __del__(self)
    def destroy(self)
    def prim_paths(self)
    def name(self)
    def count(self)
    def prims(self)
    def initialized(self)
    def post_reset(self)
    def is_valid(self, indices)
    def initialize(self, physics_sim_view)
    def _on_prim_deletion(self, prim_path)
    def _on_physics_ready(self, event)
    def _on_post_reset(self, event)
    def _remove_callbacks(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/rigid_prim.py

```
"""Provide high level functions for dealing with rigid body prims and their physics properties."""
class RigidPrim(XFormPrim)
    """Provide high-level functions for prims that have the Rigid Body API applied to them.

Handle attributes and properties of single or multiple rigid body prims.

Wrap all matching rigid prims found at the regex provided by the ``prim_paths_expr`` argument.

.. note::

    Each prim will have ``xformOp"""
    def __init__(self, prim_paths_expr, name, positions, translations, orientations, scales, visibilities, reset_xform_properties, masses, densities, linear_velocities, angular_velocities, track_contact_forces, prepare_contact_sensors, disable_stablization, contact_filter_prim_paths_expr, max_contact_count)
    def __del__(self)
    def _invalidate_physics_handle_callback(self, event)
    def num_shapes(self)
    def is_physics_handle_valid(self)
    def set_world_poses(self, positions, orientations, indices, usd)
    def get_world_poses(self, indices, clone, usd)
    def get_local_poses(self, indices)
    def set_local_poses(self, translations, orientations, indices)
    def set_linear_velocities(self, velocities, indices)
    def get_linear_velocities(self, indices, clone)
    def set_angular_velocities(self, velocities, indices)
    def get_angular_velocities(self, indices, clone)
    def set_velocities(self, velocities, indices)
    def get_velocities(self, indices, clone)
    def apply_forces(self, forces, indices, is_global)
    def apply_forces_and_torques_at_pos(self, forces, torques, positions, indices, is_global)
    def get_masses(self, indices, clone)
    def get_inv_masses(self, indices, clone)
    def get_coms(self, indices, clone)
    def get_inertias(self, indices, clone)
    def get_inv_inertias(self, indices, clone)
    def set_masses(self, masses, indices)
    def set_inertias(self, values, indices)
    def set_coms(self, positions, orientations, indices)
    def set_densities(self, densities, indices)
    def get_densities(self, indices)
    def set_sleep_thresholds(self, thresholds, indices)
    def get_sleep_thresholds(self, indices)
    def enable_rigid_body_physics(self, indices)
    def disable_rigid_body_physics(self, indices)
    def enable_gravities(self, indices)
    def disable_gravities(self, indices)
    def set_default_state(self, positions, orientations, linear_velocities, angular_velocities, indices)
    def get_default_state(self)
    def get_current_dynamic_state(self)
    def get_net_contact_forces(self, indices, clone, dt)
    def get_contact_force_matrix(self, indices, clone, dt)
    def get_contact_force_data(self, indices, clone, dt)
    def get_friction_data(self, indices, clone, dt)
    def initialize(self, physics_sim_view)
    def _on_physics_ready(self, event)
    def _apply_rigid_body_apis(self, prepare_contact_reporter)
    def _on_post_reset(self, event)
```

### source/deprecated/isaacsim.core.prims/python/impl/sdf_shape_prim.py

```
"""Provides high-level functionality for handling geometry prims that provide their Signed Distance Field (SDF)."""
class SdfShapePrim(GeometryPrim)
    """High-level functions to deal with geometry prims that provide their Signed Distance Field (SDF).

This object wraps all matching mesh geometry prims found at the regex provided by prim_paths_expr.

Args:
    prim_paths_expr: Prim paths regex to encapsulate all prims that match it.
        Example: """"
    def __init__(self, prim_paths_expr, num_query_points, prepare_sdf_schemas, name, positions, translations, orientations, scales, visibilities, reset_xform_properties, collisions, track_contact_forces, prepare_contact_sensors, disable_stablization, contact_filter_prim_paths_expr)
    def num_query_points(self)
    def _apply_sdf_schema(self, prim_at_path)
    def is_physics_handle_valid(self)
    def initialize(self, physics_sim_view)
    def get_sdf_and_gradients(self, points, indices, clone)
    def get_sdf_margins(self, indices, clone)
    def get_sdf_narrow_band_thickness(self, indices, clone)
    def get_sdf_subgrid_resolution(self, indices, clone)
    def get_sdf_resolution(self, indices, clone)
    def set_sdf_margins(self, values, indices)
    def set_sdf_narrow_band_thickness(self, values, indices)
    def set_sdf_subgrid_resolution(self, values, indices)
    def set_sdf_resolution(self, values, indices)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_articulation.py

```
"""High level wrapper for dealing with a single articulation prim and its attributes/properties."""
class SingleArticulation(_SinglePrimWrapper)
    """High-level wrapper for dealing with one articulation prim and its attributes/properties.

.. warning::

    The articulation object must be initialized in order to operate on it.
    See the ``initialize`` method for more details.

Args:
    prim_path: Prim path of the Prim to encapsulate or create."""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, reset_xform_properties, articulation_controller)
    def handles_initialized(self)
    def num_dof(self)
    def num_bodies(self)
    def dof_properties(self)
    def dof_names(self)
    def initialize(self, physics_sim_view)
    def get_dof_index(self, dof_name)
    def get_articulation_body_count(self)
    def disable_gravity(self)
    def enable_gravity(self)
    def set_world_velocity(self, velocity)
    def get_world_velocity(self)
    def set_joint_positions(self, positions, joint_indices)
    def get_joint_positions(self, joint_indices)
    def set_joint_velocities(self, velocities, joint_indices)
    def set_joint_efforts(self, efforts, joint_indices)
    def get_joint_velocities(self, joint_indices)
    def get_measured_joint_efforts(self, joint_indices)
    def get_applied_joint_efforts(self, joint_indices)
    def get_measured_joint_forces(self, joint_indices)
    def get_joints_default_state(self)
    def set_joints_default_state(self, positions, velocities, efforts)
    def get_joints_state(self)
    def get_articulation_controller(self)
    def set_linear_velocity(self, velocity)
    def get_linear_velocity(self)
    def set_angular_velocity(self, velocity)
    def get_angular_velocity(self)
    def apply_action(self, control_actions)
    def get_applied_action(self)
    def set_solver_position_iteration_count(self, count)
    def get_solver_position_iteration_count(self)
    def set_solver_velocity_iteration_count(self, count)
    def get_solver_velocity_iteration_count(self)
    def set_stabilization_threshold(self, threshold)
    def get_stabilization_threshold(self)
    def set_enabled_self_collisions(self, flag)
    def get_enabled_self_collisions(self)
    def set_sleep_threshold(self, threshold)
    def get_sleep_threshold(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_cloth_prim.py

```
"""Deprecated SingleClothPrim stub module."""
class SingleClothPrim()
    """Deprecated single cloth prim class. No longer available.

Args:
    *args: Unused positional arguments.
    **kwargs: Unused keyword arguments.

Raises:
    NotImplementedError: Always raised because SingleClothPrim is no longer available."""
    def __init__(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_deformable_prim.py

```
"""Deprecated SingleDeformablePrim stub module."""
class SingleDeformablePrim()
    """Deprecated single deformable prim class. No longer available.

Args:
    *args: Unused positional arguments.
    **kwargs: Unused keyword arguments.

Raises:
    NotImplementedError: Always raised because SingleDeformablePrim is no longer available."""
    def __init__(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_geometry_prim.py

```
"""High level wrapper to manage a single geometry prim and its attributes/properties."""
class SingleGeometryPrim(_SinglePrimWrapper)
    """High level wrapper to deal with a Geom prim (only one geometry prim) and its attributes/properties.

The ``prim_path`` should correspond to type UsdGeom.Cube, UsdGeom.Capsule, UsdGeom.Cone, UsdGeom.Cylinder,
UsdGeom.Sphere or UsdGeom.Mesh.

.. warning::

    The geometry object must be initialized i"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, reset_xform_properties, collision, track_contact_forces, prepare_contact_sensor, disable_stablization, contact_filter_prim_paths_expr)
    def geom(self)
    def set_contact_offset(self, offset)
    def get_contact_offset(self)
    def set_rest_offset(self, offset)
    def get_rest_offset(self)
    def set_torsional_patch_radius(self, radius)
    def get_torsional_patch_radius(self)
    def set_min_torsional_patch_radius(self, radius)
    def get_min_torsional_patch_radius(self)
    def set_collision_approximation(self, approximation_type)
    def get_collision_approximation(self)
    def set_collision_enabled(self, enabled)
    def get_collision_enabled(self)
    def apply_physics_material(self, physics_material, weaker_than_descendants)
    def get_applied_physics_material(self)
    def get_net_contact_forces(self, dt)
    def get_contact_force_matrix(self, dt)
    def get_contact_force_data(self, dt)
    def get_friction_data(self, dt)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_particle_system.py

```
"""Implements a wrapper for PhysX particle system functionality in Isaac Sim."""
class SingleParticleSystem()
    """A wrapper around PhysX particle system.

PhysX uses GPU-accelerated position-based dynamics (PBD) particle simulation [1]. The particle system
can be used to simulate fluids, cloth, and inflatables [2].

The wrapper is useful for creating and setting solver parameters common to the particle objects
"""
    def __init__(self, prim_path, name, particle_system_enabled, simulation_owner, contact_offset, rest_offset, particle_contact_offset, solid_rest_offset, fluid_rest_offset, enable_ccd, solver_position_iteration_count, max_depenetration_velocity, wind, max_neighborhood, max_velocity, global_self_collision_enabled, non_particle_collision_enabled)
    def prim_path(self)
    def prim(self)
    def particle_system(self)
    def name(self)
    def initialize(self, physics_sim_view)
    def is_valid(self)
    def post_reset(self)
    def apply_particle_material(self, particle_materials)
    def get_applied_particle_material(self)
    def set_particle_system_enabled(self, value)
    def set_simulation_owner(self, value)
    def set_contact_offset(self, value)
    def set_rest_offset(self, value)
    def set_particle_contact_offset(self, value)
    def set_solid_rest_offset(self, value)
    def set_fluid_rest_offset(self, value)
    def set_enable_ccd(self, value)
    def set_solver_position_iteration_count(self, value)
    def set_max_depenetration_velocity(self, value)
    def set_wind(self, value)
    def set_max_neighborhood(self, value)
    def set_max_velocity(self, value)
    def set_global_self_collision_enabled(self, value)
    def get_particle_system_enabled(self)
    def get_simulation_owner(self)
    def get_contact_offset(self)
    def get_rest_offset(self)
    def get_particle_contact_offset(self)
    def get_solid_rest_offset(self)
    def get_fluid_rest_offset(self)
    def get_enable_ccd(self)
    def get_solver_position_iteration_count(self)
    def get_max_depenetration_velocity(self)
    def get_wind(self)
    def get_max_neighborhood(self)
    def get_max_velocity(self)
    def get_global_self_collision_enabled(self)
    def apply_particle_anisotropy(self)
    def apply_particle_smoothing(self)
    def apply_particle_isotropy(self)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_prim_wrapper.py

```
"""Single prim wrapper that provides a simplified interface for manipulating individual USD prims."""
class _SinglePrimWrapper(object)
    """A single prim wrapper that provides a simplified interface for manipulating individual USD prims.

This class wraps a prim view to offer convenient methods for working with a single prim,
including pose manipulation, visual material application, visibility control, and state management.
It serves as"""
    def __init__(self, view)
    def initialize(self, physics_sim_view)
    def prim_path(self)
    def name(self)
    def prim(self)
    def non_root_articulation_link(self)
    def set_visibility(self, visible)
    def get_visibility(self)
    def post_reset(self)
    def get_default_state(self)
    def set_default_state(self, position, orientation)
    def apply_visual_material(self, visual_material, weaker_than_descendants)
    def get_applied_visual_material(self)
    def is_visual_material_applied(self)
    def set_world_pose(self, position, orientation)
    def get_world_pose(self)
    def get_local_pose(self)
    def set_local_pose(self, translation, orientation)
    def get_world_scale(self)
    def set_local_scale(self, scale)
    def get_local_scale(self)
    def is_valid(self)
    def _view_state_conversion(self, view_state)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_rigid_prim.py

```
"""High level wrapper to deal with a rigid body prim (only one rigid body prim) and its attributes/properties."""
class SingleRigidPrim(_SinglePrimWrapper)
    """High-level wrapper to deal with a rigid body prim (only one rigid body prim) and its attributes/properties.

.. warning::

    The rigid body object must be initialized in order to be able to operate on it.
    See the ``initialize`` method for more details.

.. note::

    If the prim does not alre"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, reset_xform_properties, mass, density, linear_velocity, angular_velocity)
    def set_linear_velocity(self, velocity)
    def get_linear_velocity(self)
    def set_angular_velocity(self, velocity)
    def get_angular_velocity(self)
    def set_com(self, position, orientation)
    def get_com(self)
    def set_mass(self, mass)
    def get_mass(self)
    def set_density(self, density)
    def get_density(self)
    def set_sleep_threshold(self, threshold)
    def get_sleep_threshold(self)
    def enable_rigid_body_physics(self)
    def disable_rigid_body_physics(self)
    def set_default_state(self, position, orientation, linear_velocity, angular_velocity)
    def get_default_state(self)
    def get_current_dynamic_state(self)
    def _dynamics_view_state_conversion(self, view_state)
```

### source/deprecated/isaacsim.core.prims/python/impl/single_xform_prim.py

```
"""High level wrapper for dealing with a single XForm prim and its transformation properties."""
class SingleXFormPrim(_SinglePrimWrapper)
    """Provides high level functions to deal with an Xform prim (only one Xform prim) and its attributes/properties.

If there is an Xform prim present at the path, it will use it. Otherwise, a new XForm prim at
the specified prim path will be created.

.. note::

    The prim will have ``xformOp:orient``,"""
    def __init__(self, prim_path, name, position, translation, orientation, scale, visible, reset_xform_properties)
```

### source/deprecated/isaacsim.core.prims/python/impl/xform_prim.py

```
"""Provide high-level wrapper functionality for working with USD Xform prims and their transformation properties."""
class XFormPrim(Prim)
    """Provide high-level functions for working with Xform prim views and their descendants.

Handle attributes and properties of single or multiple Xform prims.

Wrap all matching Xforms found at the regex provided at the ``prim_paths_expr`` argument.

.. note::

    Each prim will have ``xformOp:orient``"""
    def __init__(self, prim_paths_expr, name, positions, translations, orientations, scales, visibilities, reset_xform_properties, usd)
    def is_non_root_articulation_link(self)
    def set_visibilities(self, visibilities, indices)
    def get_visibilities(self, indices)
    def get_default_state(self)
    def set_default_state(self, positions, orientations, indices)
    def apply_visual_materials(self, visual_materials, weaker_than_descendants, indices)
    def get_applied_visual_materials(self, indices)
    def is_visual_material_applied(self, indices)
    def get_world_poses(self, indices, usd)
    def set_world_poses(self, positions, orientations, indices, usd)
    def get_local_poses(self, indices)
    def set_local_poses(self, translations, orientations, indices)
    def get_world_scales(self, indices)
    def set_local_scales(self, scales, indices)
    def get_local_scales(self, indices)
    def _get_fabric_selection(self)
    def _create_fabric_view_indices(self)
    def _reset_fabric_selection(self, dt, context)
    def _warp2backend(self, data)
    def _backend2warp(self, data, dtype)
    def _prepare_view_in_fabric(self)
    def _get_fabric_hierarchy(self)
    def _on_physics_ready(self, event)
    def _on_post_reset(self, event)
    def _set_xform_properties(self)
```

### source/deprecated/isaacsim.core.prims/python/tests/__init__.py

```
"""Provides the scan_for_test_modules flag for isaacsim.core.prims.tests."""
```

### source/deprecated/isaacsim.core.utils/python/impl/__init__.py

```
"""Exposes the commands utilities for isaacsim.core.utils."""
```

### source/deprecated/isaacsim.core.utils/python/impl/articulations.py

```
"""Deprecated articulation utility functions."""
def remove_articulation_root(prim)
def add_articulation_root(prim)
def move_articulation_root(src_prim, dst_prim)
def find_all_articulation_base_paths()
```

### source/deprecated/isaacsim.core.utils/python/impl/bounds.py

```
"""Deprecated bounds computation utilities."""
def recompute_extents(prim, time, include_children)
def create_bbox_cache(time, use_extents_hint)
def compute_aabb(bbox_cache, prim_path, include_children)
def compute_combined_aabb(bbox_cache, prim_paths)
def compute_obb(bbox_cache, prim_path)
def get_obb_corners(centroid, axes, half_extent)
def compute_obb_corners(bbox_cache, prim_path)
```

### source/deprecated/isaacsim.core.utils/python/impl/camera_utils.py

```
"""Deprecated camera utility functions."""
class SpringDamperFollower()
    """A spring-damper system for smooth interpolation between current and target positions.

This class implements a mass-spring-damper system that provides smooth, physics-based transitions
between a current position and a target position. It is commonly used for camera movement,
object tracking, and oth"""
    def __init__(self, mass, stiffness, damping, current, target, vel)
    def update(self, step)
class DynamicCamera()
    """A dynamic camera system that provides smooth camera movements using spring-damper physics.

This class creates a USD camera with physically based motion control using spring-damper systems
for position, look target, and focus distance. The camera movements are smooth and natural,
with configurable m"""
    def __init__(self, stage, base_path, camera_name, focal_length, f_stop, focus_distance)
    def reset(self)
    def update(self, step, timecode)
    def set_look_target(self, pos)
    def set_pos_target(self, pos)
    def set_autofocus_target(self, focus)
    def set_pos_settings(self, mass, stiffness, damping)
    def set_target_settings(self, mass, stiffness, damping)
```

### source/deprecated/isaacsim.core.utils/python/impl/carb.py

```
"""Deprecated Carbonite utility functions."""
def set_carb_setting(carb_settings, setting, value)
def get_carb_setting(carb_settings, setting)
```

### source/deprecated/isaacsim.core.utils/python/impl/collisions.py

```
"""Deprecated collision utility functions."""
def ray_cast(position, orientation, offset, max_dist)
```

### source/deprecated/isaacsim.core.utils/python/impl/commands.py

```
"""Deprecated simulation command utilities."""
class IsaacSimSpawnPrim(Command)
    """Command to spawn a new prim in the stage and set its transform.

This uses dynamic_control to properly handle physics objects and articulation.

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimSpawnPrim",
        usd_path="/path/to/file.usd",
        p"""
    def __init__(self, usd_path, prim_path, translation, rotation)
    def do(self)
    def undo(self)
class IsaacSimTeleportPrim(Command)
    """Command to set the transform of a prim. This uses dynamic_control to properly handle physics objects and articulation.

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimTeleportPrim",
        prim_path="/World/Prim",
        translation=(0, 0, 0),
     """
    def __init__(self, prim_path, translation, rotation)
    def do(self)
    def undo(self)
class IsaacSimScalePrim(Command)
    """Command to set the scale of a prim.

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimScalePrim",
        prim_path="/World/Prim",
        scale=(1.5, 1.5, 1.5),
    )

Args:
    prim_path: Path to the prim to scale.
    scale: Scale values for x, y, an"""
    def __init__(self, prim_path, scale)
    def do(self)
    def undo(self)
class IsaacSimDestroyPrim(Command)
    """Command to delete a prim. This variant has less overhead than other commands because it does not store an undo operation.

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimDestroyPrim",
        prim_path="/World/Prim",
    )

Args:
    prim_path: Path t"""
    def __init__(self, prim_path)
    def do(self)
    def undo(self)
```

### source/deprecated/isaacsim.core.utils/python/impl/constants.py

```
"""Deprecated constant definitions."""
```

### source/deprecated/isaacsim.core.utils/python/impl/deformable_mesh_utils.py

```
"""Deprecated deformable mesh utility functions."""
def loadTetFile(path)
def calculateTetraVolume(a, b, c, d)
def fixupTetraMeshVolumes(points, indices)
def verifyTetraMesh(points, indices)
def cubeTetrahedra()
def createTetraVoxels(voxel_dim, occupancy_filter_func)
def voxel_sphere_test(x, y, z, dimx, dimy, dimz)
def voxel_pass_all_test(x, y, z, dimx, dimy, dimz)
def createTetraVoxelBox(voxel_dim)
def createTetraVoxelSphere(voxel_dim)
def addTriangle(points, indices, p0, p1, p2)
def addTetra(points, indices, p0, p1, p2, p3)
def convertTetraToTriangleSoup(points_in, indices_in)
def explodeTriangleMesh(points_in, indices_in, factor)
def explodeTetraMesh(points_in, indices_in, factor)
def createTriangleMeshCube(dim)
```

### source/deprecated/isaacsim.core.utils/python/impl/distance_metrics.py

```
"""Deprecated distance metric functions."""
def _standardize_transform_matrix(t1)
def _standardize_rotation_matrix(r1)
def _standardize_translation_vector(t1)
def weighted_translational_distance(t1, t2, weight_matrix)
def rotational_distance_angle(r1, r2)
def rotational_distance_identity_matrix_deviation(r1, r2)
def rotational_distance_single_axis(r1, r2, axis)
```

### source/deprecated/isaacsim.core.utils/python/impl/extensions.py

```
"""Deprecated extension utility functions."""
def get_extension_id(extension_name)
def get_extension_path(ext_id)
def get_extension_path_from_name(extension_name)
def enable_extension(extension_name)
def disable_extension(extension_name)
```

### source/deprecated/isaacsim.core.utils/python/impl/fabric.py

```
"""Deprecated Fabric utility functions."""
def set_view_to_fabric_array(fabric_to_view, view_to_fabric)
def set_vec3d_array(fabric_vals, fabric_to_view, view_to_fabric, new_vals, view_indices)
def get_vec3d_array(fabric_vals, fabric_to_view, view_to_fabric, result, view_indices)
def set_quatf_array(fabric_vals, fabric_to_view, view_to_fabric, new_vals, view_indices)
def get_quatf_array(fabric_vals, fabric_to_view, view_to_fabric, result, view_indices)
def arange_k(a)
def decompose_fabric_transformation_matrix_to_warp_arrays(fabric_matrices, array_positions, array_orientations, array_scales, indices, mapping)
def compose_fabric_transformation_matrix_from_warp_arrays(fabric_matrices, array_positions, array_orientations, array_scales, broadcast_positions, broadcast_orientations, broadcast_scales, indices, mapping)
def _decompose(m)
```

### source/deprecated/isaacsim.core.utils/python/impl/interops.py

```
"""Deprecated interoperability utility functions."""
def warp2torch(array)
def warp2jax(array)
def warp2tensorflow(array)
def warp2numpy(array)
def torch2warp(tensor)
def torch2jax(tensor)
def torch2tensorflow(tensor)
def torch2numpy(tensor)
def jax2warp(array)
def jax2torch(array)
def jax2tensorflow(array)
def jax2numpy(array)
def tensorflow2warp(tensor)
def tensorflow2torch(tensor)
def tensorflow2jax(tensor)
def tensorflow2numpy(tensor)
def numpy2warp(array)
def numpy2torch(array)
def numpy2jax(array)
def numpy2tensorflow(array)
```

### source/deprecated/isaacsim.core.utils/python/impl/math.py

```
"""Deprecated math utility functions."""
def radians_to_degrees(rad_angles)
def cross(a, b)
def normalize(v)
def normalized(v)
```

### source/deprecated/isaacsim.core.utils/python/impl/mesh.py

```
"""Deprecated mesh utility functions."""
def get_mesh_vertices_relative_to(mesh_prim, coord_prim)
```

### source/deprecated/isaacsim.core.utils/python/impl/numpy/__init__.py

```
"""Utility functions for NumPy operations including mathematical computations, rotations, tensor manipulations, and transformations."""
```

### source/deprecated/isaacsim.core.utils/python/impl/numpy/maths.py

```
"""Mathematical utility functions for matrix operations and trigonometric computations."""
def matmul(matrix_a, matrix_b)
def sin(data)
def cos(data)
def transpose_2d(data)
def inverse(data)
```

### source/deprecated/isaacsim.core.utils/python/impl/numpy/rotations.py

```
"""Provides NumPy-based functions for 3D rotation conversions between quaternions, Euler angles, rotation matrices, and rotation vectors."""
def gf_quat_to_tensor(orientation, device)
def euler_angles_to_quats(euler_angles, degrees, extrinsic, device)
def quats_to_euler_angles(quaternions, degrees, extrinsic, device)
def rot_matrices_to_quats(rotation_matrices, device)
def quats_to_rot_matrices(quaternions, device)
def rotvecs_to_quats(rotation_vectors, degrees, device)
def quats_to_rotvecs(quaternions, device)
def rad2deg(radian_value, device)
def deg2rad(degree_value, device)
def xyzw2wxyz(q, ret_torch)
def wxyz2xyzw(q, ret_torch)
```

### source/deprecated/isaacsim.core.utils/python/impl/numpy/tensor.py

```
"""NumPy-based tensor operations and data manipulation utilities for Isaac Sim."""
def as_type(data, dtype)
def convert(data, device, dtype, indexed)
def create_zeros_tensor(shape, dtype, device)
def create_tensor_from_list(data, dtype, device)
def clone_tensor(data, device)
def resolve_indices(indices, count, device)
def move_data(data, device)
def tensor_cat(data, device, dim)
def expand_dims(data, axis)
def pad(data, pad_width, mode, value)
def tensor_stack(data, dim)
def to_list(data)
def to_numpy(data)
def assign(src, dst, indices)
```

### source/deprecated/isaacsim.core.utils/python/impl/numpy/transformations.py

```
"""Utilities for 3D transformation operations including coordinate frame conversions and pose manipulations using NumPy arrays."""
def tf_matrices_from_poses(translations, orientations, device)
def get_local_from_world(parent_transforms, positions, orientations, device)
def get_world_from_local(parent_transforms, translations, orientations, device)
def get_pose(positions, orientations, device)
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose)
```

### source/deprecated/isaacsim.core.utils/python/impl/physics.py

```
"""Deprecated physics utility functions."""
def get_rigid_body_enabled(prim_path)
def set_rigid_body_enabled(_value, prim_path)
def simulate_async(seconds, steps_per_sec, callback)
```

### source/deprecated/isaacsim.core.utils/python/impl/prims.py

```
"""Deprecated prim utility functions."""
def get_prim_at_path(prim_path, fabric)
def is_prim_path_valid(prim_path, fabric)
def get_prim_attribute_names(prim_path, fabric)
def get_prim_attribute_value(prim_path, attribute_name, fabric)
def set_prim_attribute_value(prim_path, attribute_name, value, fabric)
def define_prim(prim_path, prim_type, fabric)
def get_prim_type_name(prim_path, fabric)
def move_prim(path_from, path_to)
def get_first_matching_child_prim(prim_path, predicate, fabric)
def get_first_matching_parent_prim(prim_path, predicate)
def get_all_matching_child_prims(prim_path, predicate, depth)
def find_matching_prim_paths(prim_path_regex, prim_type)
def get_prim_children(prim)
def get_prim_parent(prim)
def query_parent_path(prim_path, predicate)
def is_prim_ancestral(prim_path)
def is_prim_root_path(prim_path)
def is_prim_no_delete(prim_path)
def is_prim_hidden_in_stage(prim_path)
def get_prim_path(prim)
def set_prim_visibility(prim, visible)
def create_prim(prim_path, prim_type, position, translation, orientation, scale, usd_path, semantic_label, semantic_type, attributes)
def delete_prim(prim_path)
def get_prim_property(prim_path, property_name)
def set_prim_property(prim_path, property_name, property_value)
def get_prim_object_type(prim_path)
def is_prim_non_root_articulation_link(prim_path)
def set_prim_hide_in_stage_window(prim, hide)
def set_prim_no_delete(prim, no_delete)
def set_targets(prim, attribute, target_prim_paths)
def get_articulation_root_api_prim_path(prim_path)
```

### source/deprecated/isaacsim.core.utils/python/impl/random.py

```
"""Deprecated random utility functions."""
def get_random_values_in_range(min_range, max_range)
def get_random_translation_from_camera(min_distance, max_distance, fov_x, fov_y, fraction_to_screen_edge)
def get_random_world_pose_in_view(camera_prim, min_distance, max_distance, fov_x, fov_y, fraction_to_screen_edge, coord_prim, min_rotation_range, max_rotation_range)
```

### source/deprecated/isaacsim.core.utils/python/impl/render_product.py

```
"""Deprecated render product utility functions."""
def add_aov(render_product_path, aov_name)
def get_camera_prim_path(render_product_path)
def set_camera_prim_path(render_product_path, camera_prim_path)
def get_resolution(render_product_path)
def set_resolution(render_product_path, resolution)
```

### source/deprecated/isaacsim.core.utils/python/impl/rotations.py

```
"""Deprecated rotation utility functions."""
def rot_matrix_to_quat(mat)
def quat_to_rot_matrix(quat)
def matrix_to_euler_angles(mat, degrees, extrinsic)
def euler_to_rot_matrix(euler_angles, degrees, extrinsic)
def quat_to_euler_angles(quat, degrees, extrinsic)
def euler_angles_to_quat(euler_angles, degrees, extrinsic)
def lookat_to_quatf(camera, target, up)
def gf_quat_to_np_array(orientation)
def gf_rotation_to_np_array(orientation)
```

### source/deprecated/isaacsim.core.utils/python/impl/semantics.py

```
"""Deprecated semantic labeling utility functions."""
def add_labels(prim, labels, instance_name, overwrite)
def get_labels(prim)
def remove_labels(prim, instance_name, include_descendants)
def check_missing_labels(prim_path)
def check_incorrect_labels(prim_path, validate_against_prim_path)
def count_labels_in_scene(prim_path)
def upgrade_prim_semantics_to_labels(prim, include_descendants)
```

### source/deprecated/isaacsim.core.utils/python/impl/stage.py

```
"""Deprecated USD stage utility functions."""
def use_stage(stage)
def get_current_stage(fabric)
def get_current_stage_id()
def update_stage()
def update_stage_async()
def set_stage_up_axis(axis)
def get_stage_up_axis()
def clear_stage(predicate)
def print_stage_prim_paths(fabric)
def add_reference_to_stage(usd_path, prim_path, prim_type)
def create_new_stage()
def create_new_stage_in_memory()
def create_new_stage_async()
def open_stage(usd_path)
def open_stage_async(usd_path)
def save_stage(usd_path, save_and_reload_in_place)
def close_stage(callback_fn)
def set_livesync_stage(usd_path, enable)
def traverse_stage(fabric)
def is_stage_loading()
def set_stage_units(stage_units_in_meters)
def get_stage_units()
def get_next_free_path(path, parent)
def remove_deleted_references()
```

### source/deprecated/isaacsim.core.utils/python/impl/string.py

```
"""Deprecated string utility functions."""
def find_unique_string_name(initial_name, is_unique_fn)
def find_root_prim_path_from_regex(prim_path_regex)
```

### source/deprecated/isaacsim.core.utils/python/impl/torch/__init__.py

```
"""Torch-based utilities for mathematical operations, rotations, tensor manipulations, and transformations in Isaac Sim."""
```

### source/deprecated/isaacsim.core.utils/python/impl/torch/maths.py

```
"""Utility functions for mathematical operations and tensor manipulations using PyTorch."""
def normalize(x, eps)
def scale_transform(x, lower, upper)
def unscale_transform(x, lower, upper)
def copysign(a, b)
def torch_rand_float(lower, upper, shape, device)
def torch_random_dir_2(shape, device)
def tensor_clamp(t, min_t, max_t)
def scale(x, lower, upper)
def unscale(x, lower, upper)
def unscale_np(x, lower, upper)
def set_seed(seed, torch_deterministic)
def matmul(matrix_a, matrix_b)
def sin(data)
def cos(data)
def transpose_2d(data)
def inverse(data)
```

### source/deprecated/isaacsim.core.utils/python/impl/torch/rotations.py

```
"""Provides PyTorch-based utilities for 3D rotations, quaternions, and coordinate transformations."""
def gf_quat_to_tensor(orientation, device)
def euler_angles_to_quats(euler_angles, degrees, extrinsic, device)
def rot_matrices_to_quats(rotation_matrices, device)
def rad2deg(radian_value, device)
def deg2rad(degree_value, device)
def quat_mul(a, b)
def quat_conjugate(a)
def quat_apply(a, b)
def quat_rotate(q, v)
def quat_rotate_inverse(q, v)
def quat_unit(a)
def quat_from_angle_axis(angle, axis)
def quat_axis(q, axis)
def normalize_angle(x)
def get_basis_vector(q, v)
def quats_to_rot_matrices(quats)
def matrices_to_euler_angles(mat, extrinsic)
def get_euler_xyz(q, extrinsic)
def quat_from_euler_xyz(roll, pitch, yaw, extrinsic)
def quat_diff_rad(a, b)
def normalise_quat_in_pose(pose)
def compute_heading_and_up(torso_rotation, inv_start_rot, to_target, vec0, vec1, up_idx)
def compute_rot(torso_quat, velocity, ang_velocity, targets, torso_positions, extrinsic)
def xyzw2wxyz(q)
def wxyz2xyzw(q)
```

### source/deprecated/isaacsim.core.utils/python/impl/torch/tensor.py

```
"""Utility functions for PyTorch tensor operations, data type conversion, and device management."""
def as_type(data, dtype)
def convert(data, device, dtype, indexed)
def create_zeros_tensor(shape, dtype, device)
def create_tensor_from_list(data, dtype, device)
def clone_tensor(data, device)
def resolve_indices(indices, count, device)
def move_data(data, device)
def tensor_cat(data, device, dim)
def expand_dims(data, axis)
def pad(data, pad_width, mode, value)
def tensor_stack(data, dim)
def to_list(data)
def to_numpy(data)
def assign(src, dst, indices)
```

### source/deprecated/isaacsim.core.utils/python/impl/torch/transformations.py

```
"""Tensor-based transformation utilities for 3D poses, coordinate frame conversions, and spatial operations."""
def tf_matrices_from_poses(translations, orientations, device)
def get_local_from_world(parent_transforms, positions, orientations, device)
def get_world_from_local(parent_transforms, translations, orientations, device)
def get_pose(positions, orientations, device)
def get_world_from_local_position(pos_offset_local, pose_global)
def normalise_quat_in_pose(pose)
def tf_inverse(q, t)
def tf_apply(q, t, v)
def tf_vector(q, v)
def tf_combine(q1, t1, q2, t2)
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose)
```

### source/deprecated/isaacsim.core.utils/python/impl/transformations.py

```
"""Deprecated transformation utility functions."""
def tf_matrix_from_pose(translation, orientation)
def pose_from_tf_matrix(transformation)
def tf_matrices_from_poses(translations, orientations)
def get_relative_transform(source_prim, target_prim)
def get_translation_from_target(translation_from_source, source_prim, target_prim)
def get_world_pose_from_relative(coord_prim, relative_translation, relative_orientation)
def get_transform_with_normalized_rotation(transform)
```

### source/deprecated/isaacsim.core.utils/python/impl/types.py

```
"""Deprecated type definitions for simulation data structures."""
class DataFrame(object)
    """Container for simulation data at a specific time step.

Args:
    current_time_step: The current simulation time step index.
    current_time: The current simulation time in seconds.
    data: Dictionary containing the simulation data."""
    def __init__(self, current_time_step, current_time, data)
    def get_dict(self)
    def __str__(self)
    def init_from_dict(cls, dict_representation)
class DOFInfo(object)
    """Information about a degree of freedom in an articulation.

Args:
    prim_path: The USD prim path for this DOF.
    handle: The physics handle for this DOF.
    prim: The USD prim object for this DOF.
    index: The index of this DOF in the articulation."""
    def __init__(self, prim_path, handle, prim, index)
class XFormPrimState(object)
    """State of an XFormPrim containing position and orientation.

Args:
    position: The position as a NumPy array of shape (3,).
    orientation: The orientation quaternion (w, x, y, z) as a NumPy array of shape (4,)."""
    def __init__(self, position, orientation)
class XFormPrimViewState(object)
    """State of multiple XFormPrims containing positions and orientations.

Args:
    positions: Positions with shape (N, 3).
    orientations: Quaternion orientations (scalar first) with shape (N, 4)."""
    def __init__(self, positions, orientations)
class DynamicState(object)
    """State of a dynamic rigid body including pose and velocities.

Args:
    position: The position as a NumPy array of shape (3,).
    orientation: The orientation quaternion (w, x, y, z) as a NumPy array of shape (4,).
    linear_velocity: The linear velocity as a NumPy array of shape (3,).
    angular"""
    def __init__(self, position, orientation, linear_velocity, angular_velocity)
class DynamicsViewState(object)
    """State of multiple dynamic rigid bodies including poses and velocities.

Args:
    positions: Positions with shape (N, 3).
    orientations: Quaternion orientations (scalar first) with shape (N, 4).
    linear_velocities: Linear velocities with shape (N, 3).
    angular_velocities: Angular velocities"""
    def __init__(self, positions, orientations, linear_velocities, angular_velocities)
class JointsState(object)
    """State of articulation joints including positions, velocities, and efforts.

Args:
    positions: Joint positions array.
    velocities: Joint velocities array.
    efforts: Joint efforts (torques/forces) array."""
    def __init__(self, positions, velocities, efforts)
class ArticulationAction(object)
    """Action to apply to an articulation's joints.

Args:
    joint_positions: Target joint positions.
    joint_velocities: Target joint velocities.
    joint_efforts: Target joint efforts (torques/forces).
    joint_indices: Joint indices to specify which joints to manipulate."""
    def __init__(self, joint_positions, joint_velocities, joint_efforts, joint_indices)
    def get_dof_action(self, index)
    def get_dict(self)
    def __str__(self)
    def get_length(self)
class ArticulationActions(object)
    """Actions to apply to multiple articulations' joints.

Args:
    joint_positions: Target joint positions.
    joint_velocities: Target joint velocities.
    joint_efforts: Target joint efforts (torques/forces).
    joint_indices: Joint indices to specify which joints to manipulate. Shape (K,).
       """
    def __init__(self, joint_positions, joint_velocities, joint_efforts, joint_indices, joint_names)
```

### source/deprecated/isaacsim.core.utils/python/impl/viewports.py

```
"""Deprecated viewport utility functions."""
def set_camera_view(eye, target, camera_prim_path, viewport_api)
def get_viewport_names(usd_context_name)
def get_id_from_index(index)
def get_window_from_id(id, usd_context_name)
def destroy_all_viewports(usd_context_name, destroy_main_viewport)
def add_aov_to_viewport(viewport_api, aov_name)
def get_intrinsics_matrix(viewport_api)
def set_intrinsics_matrix(viewport_api, intrinsics_matrix, focal_length)
def backproject_depth(depth_image, viewport_api, max_clip_depth)
def project_depth_to_worldspace(depth_image, viewport_api, max_clip_depth)
def create_viewport_for_camera(viewport_name, camera_prim_path, width, height, position_x, position_y)
def set_active_viewport_camera(camera_prim_path)
```

### source/deprecated/isaacsim.core.utils/python/impl/warp/__init__.py

```
"""Warp utility functions for rotations, tensors, and transformations in Isaac Sim."""
```

### source/deprecated/isaacsim.core.utils/python/impl/warp/rotations.py

```
"""Warp-based utilities for rotation operations and quaternion conversions."""
def gf_quat_to_tensor(orientation, device)
def euler_angles_to_quats(euler_angles, degrees, extrinsic, device)
def rad2deg(radian_value, device)
def deg2rad(degree_value, device)
def _xyzw2wxyz1(q)
def _xyzw2wxyz2(q)
def _xyzw2wxyz3(q)
def _wxyz2xyzw1(q)
def _wxyz2xyzw2(q)
def _wxyz2xyzw3(q)
def _roll_quaternion_components(q, shift)
def xyzw2wxyz(q)
def wxyz2xyzw(q)
```

### source/deprecated/isaacsim.core.utils/python/impl/warp/tensor.py

```
"""Utility functions for working with Warp tensors and arrays, including data type conversion, device management, and array operations."""
def get_type(dtype)
def convert(data, device, dtype, indexed)
def create_zeros_tensor(shape, dtype, device)
def create_tensor_from_list(data, dtype, device)
def clone_tensor(data, device)
def _arange_k(a)
def arange(n, device)
def resolve_indices(indices, count, device)
def move_data(data, device)
def tensor_cat(data, device, dim)
def expand_dims(data, axis)
def to_list(data)
def to_numpy(data)
def _assign11(src, dst, indices)
def _assign12(src, dst, indices)
def _assign13(src, dst, indices)
def _assign22(src, dst, indices1, indices2)
def _assign23(src, dst, indices1, indices2)
def _assign33(src, dst, indices1, indices2, indices3)
def assign(src, dst, indices)
def _ones(a)
def ones(n, device, dtype)
def clamp(data, low, high)
def _finite_diff2(result, a, b, dt)
def finite_diff2(a, b, dt)
```

### source/deprecated/isaacsim.core.utils/python/impl/warp/transformations.py

```
"""Warp-based coordinate transformation utilities for pose manipulation and coordinate space conversions."""
def _local_to_world(parent_translations, parent_rotations, positions, orientations, world_pos, world_rot)
def get_local_from_world(parent_transforms, positions, orientations, device)
def get_world_from_local(parent_transforms, translations, orientations, device)
def _assign_pose(pose, positions, orientations)
def get_pose(positions, orientations, device)
def _assign_current_pose(pose, current_positions, current_orientations)
def _assign_new_pose(pose, positions, orientations, indices, has_positions, has_orientations)
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose)
```

### source/deprecated/isaacsim.core.utils/python/impl/xforms.py

```
"""Deprecated xform operation utility functions."""
def clear_xform_ops(prim)
def reset_and_set_xform_ops(prim, translation, orientation, scale)
def reset_xform_ops(prim)
def _get_world_pose_transform_w_scale(prim_path, fabric)
def get_local_pose(prim_path)
def get_world_pose(prim_path, fabric)
```

### source/deprecated/isaacsim.core.utils/python/tests/__init__.py

```
"""Tests for the isaacsim.core.utils module."""
```

### source/deprecated/isaacsim.core.utils/python/tests/test_articulation_utils.py

```
"""Tests for articulation utility functions."""
class TestArticulationUtils(AsyncTestCase)
    """Test cases for ArticulationUtils."""
    def setUp(self)
    def tearDown(self)
    def assertListsSame(self, l1, l2)
    def test_find_articulation_base_paths(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_bounds_utils.py

```
"""Tests for bounds computation utilities."""
class TestBounds(AsyncTestCase)
    """Test cases for Bounds."""
    def setUp(self)
    def tearDown(self)
    def test_recompute_extents(self)
    def test_nested_recompute_extents(self)
    def test_obb_default(self)
    def test_obb_transformed(self)
    def test_obb_nested(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_distance_metrics.py

```
"""Tests for distance metric functions."""
class TestDistanceMetrics(AsyncTestCase)
    """Test cases for DistanceMetrics."""
    def setUp(self)
    def tearDown(self)
    def is_distance_metric(self, t1, t2, t3, dist_fun)
    def test_weighted_translational_distance(self)
    def test_rotational_distance_angle(self)
    def test_rotational_distance_identity_matrix_deviation(self)
    def test_rotational_distance_single_axis(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_numpy_rotation_utils.py

```
"""Tests for NumPy rotation utility functions."""
class TestRotationUtils(AsyncTestCase)
    """Test cases for RotationUtils."""
    def setUp(self)
    def tearDown(self)
    def test_rotation_conversions(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_physics_utils.py

```
"""Tests for physics utility functions."""
class TestPhysics(AsyncTestCase)
    """Test cases for Physics."""
    def setUp(self)
    def tearDown(self)
    def test_rigid_body_enabled(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_prims_utils.py

```
"""Tests for prim utility functions."""
class TestPrims(AsyncTestCase)
    """Test cases for Prims."""
    def setUp(self)
    def tearDown(self)
    def _create_attributes(self, prim)
    def test_prim_attribute_value(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_render_product_utils.py

```
"""Tests for render product utility functions."""
class TestRenderProduct(AsyncTestCase)
    """Test cases for RenderProduct."""
    def setUp(self)
    def tearDown(self)
    def test_hydra_texture(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_rotations_utils.py

```
"""Tests for rotation utility functions."""
class TestRotations(AsyncTestCase)
    """Test cases for Rotations."""
    def setUp(self)
    def tearDown(self)
    def test_euler_angles_to_quat(self)
    def test_quat_to_euler_angles(self)
    def test_euler_angles_to_matrix_to_quat(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_semantics.py

```
"""Tests for semantic labeling utility functions."""
class TestSemantics(AsyncTestCase)
    """Test cases for Semantics."""
    def setUp(self)
    def tearDown(self)
    def create_test_environment_new_labels(self)
    def _apply_old_semantics(self, prim, semantic_label, type_label, suffix)
    def test_upgrade_prim_semantics_to_labels(self)
    def test_new_labels_api(self)
    def test_check_missing_labels(self)
    def test_check_incorrect_labels(self)
    def test_count_labels_in_scene_new(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_sim_commands.py

```
"""Tests for simulation command utilities."""
class TestIsaacSimCommands(AsyncTestCase)
    """Test cases for IsaacSimCommands."""
    def setUp(self)
    def tearDown(self)
    def test_spawn_command(self)
    def test_teleport_command(self)
    def test_scale(self)
    def test_destroy_command(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_stage_utils.py

```
"""Tests for USD stage utility functions."""
class TestStage(AsyncTestCase)
    """Test cases for Stage."""
    def setUp(self)
    def tearDown(self)
    def is_current_stage_in_memory()
    def attach_stage_to_usd_context()
    def test_clear_stage(self)
    def test_add_reference_to_stage_units(self)
    def test_context_manager(self)
    def test_stage_in_memory(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_string_utils.py

```
"""Tests for string utility functions."""
class TestStringUtils(AsyncTestCase)
    """Test cases for string utilities."""
    def test_find_root_prim_path_from_regex_pattern(self)
    def test_find_root_prim_path_from_regex_plain_path(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_torch_transformations.py

```
"""Tests for PyTorch transformation utilities."""
class TestTorchTransformations(AsyncTestCase)
    """Test suite for torch transformation utilities."""
    def setUp(self)
    def tearDown(self)
    def test_get_world_from_local_position_identity(self)
    def test_get_world_from_local_position_90deg_z_rotation(self)
    def test_get_world_from_local_position_90deg_x_rotation(self)
    def test_get_world_from_local_position_with_translation(self)
    def test_get_world_from_local_position_batched(self)
    def test_get_world_from_local_position_180deg_rotation(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_viewports_utils.py

```
"""Tests for viewport utility functions."""
class TestViewports(AsyncTestCase)
    """Test cases for Viewports."""
    def setUp(self)
    def tearDown(self)
    def test_get_intrinsics(self)
    def test_set_intrinsics(self)
    def test_get_viewport_names(self)
    def test_get_window_from_id(self)
    def test_get_id_from_index(self)
    def test_create_destroy_window(self)
    def test_destroy_windows(self)
    def test_set_camera_view_perspective(self)
    def test_set_camera_view_camera_prim(self)
```

### source/deprecated/isaacsim.core.utils/python/tests/test_warp_rotation_utils.py

```
"""Tests for Warp rotation utility functions."""
class TestWarpRotationUtils(AsyncTestCase)
    """Test cases for Warp rotation utilities."""
    def test_quaternion_format_conversions_keep_cpu_data_on_cpu(self)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/block_stacking_behavior.py

```
"""Franka block stacking behavior using cortex decision framework."""
def make_grasp_T(t, ay)
def make_block_grasp_Ts(block_pick_height)
def get_world_block_grasp_Ts(obj_T, obj_grasp_Ts, axis_x_filter, axis_x_filter_thresh, axis_y_filter, axis_y_filter_thresh, axis_z_filter, axis_z_filter_thresh)
def get_best_obj_grasp(obj_T, obj_grasp_Ts, eff_T, other_obj_Ts)
def calc_grasp_for_block_T(context, block_T, desired_ax)
def calc_grasp_for_top_of_tower(context)
class BuildTowerContext(DfRobotApiContext)
    """Context for the block tower building behavior.

Args:
    robot: The robot API instance.
    tower_position: The 3D position for the tower base."""
    def __init__(self, robot, tower_position)
    def reset(self)
    def has_active_block(self)
    def activate_block(self, name)
    def reset_active_block(self)
    def block_names(self)
    def num_blocks(self)
    def mark_block_in_gripper(self)
    def clear_gripper(self)
    def is_gripper_clear(self)
    def gripper_has_block(self)
    def has_placement_target_eff_T(self)
    def next_block_name(self)
    def find_not_in_tower(self)
    def print_tower_status(self)
    def monitor_perception(self)
    def monitor_block_tower(self)
    def monitor_gripper_has_block(self)
    def monitor_suppression_requirements(self)
    def monitor_diagnostics(self)
class OpenGripperRd(DfRldsNode)
    """RLDS node that open the gripper when close to the chosen grasp target.

Args:
    dist_thresh_for_open: Distance threshold within which to open the gripper."""
    def __init__(self, dist_thresh_for_open)
    def is_runnable(self)
    def decide(self)
class ReachToBlockRd(DfRldsNode)
    """RLDS node that dispatches to a linked child when the gripper is clear."""
    def __init__(self)
    def link_to(self, name, decider)
    def is_runnable(self)
    def decide(self)
class GoHome(DfDecider)
    """Decider that sends the robot to its home position with the gripper closed."""
    def __init__(self)
    def enter(self)
    def decide(self)
class ChooseNextBlockForTowerBuildUp(DfDecider)
    """Choose the next block for building up the tower and compute its grasp."""
    def __init__(self)
    def link_to(self, name, decider)
    def decide(self)
    def exit(self)
class ChooseNextBlockForTowerTeardown(DfDecider)
    """Choose the top tower block for teardown and compute its grasp."""
    def __init__(self)
    def link_to(self, name, decider)
    def decide(self)
    def exit(self)
class ChooseNextBlock(DfDecider)
    """Choose the next block, delegating to build-up or teardown as appropriate."""
    def __init__(self)
    def link_to(self, name, decider)
    def decide(self)
class LiftState(DfState)
    """A simple state which sends a target a distance command_delta_z above the current.

end-effector position until the end-effector has moved success_delta_z meters up.

Args:
    command_delta_z: The delta offset up to shift the command away from the current end-effector
        position every cycle.
 """
    def __init__(self, command_delta_z, success_delta_z, cautious_command_delta_z)
    def enter(self)
    def closest_non_grasped_block_dist(self, eff_p)
    def step(self)
    def exit(self)
class PickBlockRd(DfStateMachineDecider, DfRldsNode)
    """RLDS node that picks a block when the end-effector is at the chosen grasp."""
    def __init__(self)
    def is_runnable(self)
def make_pick_rlds()
class TablePointValidator()
    """Validate and sample random positions on the table avoiding blocks and the tower.

Args:
    context: The build-tower context."""
    def __init__(self, context)
    def validate_point(self, p)
    def sample_random_position_2d(self)
class ReachToPlaceOnTower(DfDecider)
    """Decider that reaches to place a block on top of the tower."""
    def __init__(self)
    def decide(self)
    def exit(self)
class ReachToPlaceOnTable(DfDecider)
    """Decider that reaches to place a block at a random valid position on the table."""
    def __init__(self)
    def choose_random_T_on_table(self)
    def enter(self)
    def decide(self)
    def exit(self)
class ReachToPlacementRd(DfRldsNode)
    """RLDS node that decides whether to place on the tower or on the table."""
    def __init__(self)
    def is_runnable(self)
    def enter(self)
    def decide(self)
def set_top_block_aligned(ct)
class PlaceBlockRd(DfStateMachineDecider, DfRldsNode)
    """RLDS node that places the held block when the end-effector is at the placement target."""
    def __init__(self)
    def is_runnable(self)
    def exit(self)
def make_place_rlds()
class BlockPickAndPlaceDispatch(DfDecider)
    """Top-level decider that dispatches between picking, placing, and going home."""
    def __init__(self)
    def decide(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/peck_decider_network.py

```
"""Peck behavior implemented as a decider network with context monitors."""
def sample_target_p()
def make_target_rotation(target_p)
class PeckContext(DfRobotApiContext)
    """Context for the peck behavior with obstacle-aware target sampling.

Args:
    robot: The robot API instance."""
    def __init__(self, robot)
    def reset(self)
    def monitor_active_target_p(self)
    def set_is_done(self)
    def is_near_obs(self, p)
    def sample_target_p_away_from_obs(self)
    def choose_next_target(self)
class PeckState(DfState)
    """State that sends the end-effector to peck at the active target."""
    def enter(self)
    def step(self)
class ChooseTarget(DfAction)
    """Action that chooses the next peck target."""
    def step(self)
class CloseGripper(DfAction)
    """Action that closes the gripper."""
    def enter(self)
class Dispatch(DfDecider)
    """The top-level decider.

If the current peck task is done, then it will choose a target.  Otherwise, it executes the peck
behavior. The peck behavior is a sequential state machine which 1. closes the gripper, 2. pecks,
3. lifts the end-effector slightly, 4. writes to the context that it's done.

This"""
    def __init__(self)
    def decide(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/peck_game.py

```
"""This script gives an example of a behavior programmed entirely as a decider network (no state.

machines). The behavior will monitor the blocks for movement, and whenever a block moves it will
reach down and peck it. It will always switch to the most recently moved block, aborting its
previous peck behavior if a new block is moved.

The top level Dispatch decider has three actions: peck, lift, and go_home. See the Dispatch
decider's decide() method for the specific implementation of choice of action. Simply put, if
there's an active block, then peck at it. If it doesn't have an active block, a"""
class PeckContext(DfRobotApiContext)
    """Context for the reactive peck game behavior with block movement monitoring.

Args:
    robot: The robot API instance."""
    def __init__(self, robot)
    def reset(self)
    def has_active_block(self)
    def clear_active_block(self)
    def get_latest_block_positions(self)
    def monitor_block_movement(self)
    def monitor_active_target_p(self)
    def monitor_active_block(self)
    def monitor_eff_block_proximity(self)
    def monitor_diagnostics(self)
class PeckAction(DfAction)
    """Action that pecks at the active block target."""
    def enter(self)
    def step(self)
    def exit(self)
class Dispatch(DfDecider)
    """Top-level decider that dispatches between peck, lift, and go home."""
    def enter(self)
    def decide(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/peck_state_machine.py

```
"""Simple example of constructing a running a state machine. This state machine will loop choosing.

a target on the ground away from obstacles and pecking at it.

In general this will loop successfully forever as long as the world is static. However, if the user
moves a block (obstacle) to overlap with a chosen target, the end-effector will avoid the block and
be unable to reach its target, thereby stalling.

This sort of reactivity is more natural to program using decider networks as demonstrated in
peck_decider_network.py, where the system constantly monitors the target and triggers the system"""
def sample_target_p()
def make_target_rotation(target_p)
class PeckState(DfState)
    """State that samples a target, sends the end-effector to peck, and waits for arrival."""
    def is_near_obs(self, p)
    def sample_target_p_away_from_obs(self)
    def enter(self)
    def step(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/simple/simple_decider_network.py

```
"""Simple decider network that prints left, right, or middle based on end-effector position."""
class Context(DfRobotApiContext)
    """Context that monitors end-effector y-position and lateral state.

Args:
    robot: The robot API instance."""
    def __init__(self, robot)
    def reset(self)
    def monitor_y(self)
    def monitor_is_left(self)
    def monitor_is_middle(self)
class PrintAction(DfAction)
    """Action that prints a message on entry.

Args:
    msg: The message to print."""
    def __init__(self, msg)
    def __str__(self)
    def enter(self)
class Dispatch(DfDecider)
    """Top-level decider that dispatches print actions based on end-effector position."""
    def __init__(self)
    def decide(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/franka/simple/simple_state_machine.py

```
"""Simple state machine that moves the end-effector between two target positions."""
class ReachState(DfState)
    """State that moves the end-effector to a target position and exits on arrival.

Args:
    target_p: The 3D target position."""
    def __init__(self, target_p)
    def __str__(self)
    def enter(self)
    def step(self)
def make_decider_network(robot)
```

### source/deprecated/isaacsim.cortex.behaviors/isaacsim/cortex/behaviors/ur10/bin_stacking_behavior.py

```
"""UR10 bin stacking behavior using cortex decision framework."""
class BinState()
    """Track the state of a single bin during the stacking behavior.

Args:
    bin_obj: The bin's simulation object."""
    def __init__(self, bin_obj)
class FlipStationObstacleMonitor(ObstacleMonitor)
    """Monitor that toggles the flip station obstacle based on end-effector proximity.

Args:
    context: The bin stacking context."""
    def __init__(self, context)
    def is_obstacle_required(self)
class NavigationObstacleMonitor(ObstacleMonitor)
    """Monitor that toggles navigation obstacles based on target-effector side crossing.

Args:
    context: The bin stacking context."""
    def __init__(self, context)
    def is_obstacle_required(self)
class BinStackingDiagnostic()
    """Store diagnostic information about the current bin stacking state.

Args:
    bin_name: Name of the active bin.
    bin_base: The bin base prim.
    grasp: The grasp transform.
    grasp_reached: Whether the grasp has been reached.
    attached: Whether the bin is attached to the gripper.
    needs_"""
    def __init__(self, bin_name, bin_base, grasp, grasp_reached, attached, needs_flip)
class BinStackingDiagnosticsMonitor(DfDiagnosticsMonitor)
    """Diagnostics monitor that reports bin stacking state.

Args:
    print_dt: Interval between diagnostic prints in seconds.
    diagnostic_fn: Optional callback for receiving diagnostic objects."""
    def __init__(self, print_dt, diagnostic_fn)
    def print_diagnostics(self, context)
def get_bin_under(p, stacked_bins)
def adjust_about_x_if_opposite(eff_R, target_R, threshold)
class BinStackingContext(ObstacleMonitorContext)
    """Context for the UR10 bin stacking behavior.

Args:
    robot: The robot API instance.
    monitor_fn: Optional callback for receiving diagnostic information."""
    def __init__(self, robot, monitor_fn)
    def reset(self)
    def stack_complete(self)
    def elapse_time(self)
    def has_active_bin(self)
    def monitor_bins(self)
    def monitor_active_bin(self)
    def monitor_active_bin_grasp_T(self)
    def monitor_active_bin_grasp_reached(self)
    def mark_active_bin_as_complete(self)
class Move(DfState)
    """State that moves the end-effector toward a commanded pose until thresholds are met.

Args:
    p_thresh: Position threshold for convergence.
    R_thresh: Rotation threshold for convergence."""
    def __init__(self, p_thresh, R_thresh)
    def update_command(self, command)
    def step(self)
class MoveWithNavObs(Move)
    """Move state that activates navigation obstacle monitoring during movement."""
    def enter(self)
    def exit(self)
class ReachToPick(MoveWithNavObs)
    """Reach to pick the bin.

The bin can be anywhere, including on the flip station. On entry, we activate the flip station
obstacle monitor in case we're picking from the flip station. That obstacle monitor will prevent
collision with the flip station en route."""
    def __init__(self)
    def enter(self)
    def step(self)
    def exit(self)
class ReachToPlace(MoveWithNavObs)
    """Move state that reaches to the stacking placement location."""
    def __init__(self)
    def enter(self)
    def step(self)
class CloseSuctionGripperWithRetries(DfState)
    """State that closes the suction gripper, retrying until successful."""
    def enter(self)
    def step(self)
class CloseSuctionGripper(DfState)
    """State that closes the suction gripper and waits for confirmation."""
    def enter(self)
    def step(self)
class OpenSuctionGripper(DfState)
    """State that opens the suction gripper."""
    def enter(self)
    def step(self)
class DoNothing(DfState)
    """State that clears arm commands and does nothing."""
    def enter(self)
    def step(self)
class LiftAndTurn(Move)
    """Move state that lifts the end-effector and turns toward a home-like pose."""
    def __init__(self)
    def step(self)
class PickBin(DfStateMachineDecider)
    """State machine that picks a bin from the conveyor."""
    def __init__(self)
class FlipBin(DfStateMachineDecider)
    """State machine that flips a bin at the flip station."""
    def __init__(self)
class PlaceBin(DfStateMachineDecider)
    """State machine that places a bin on the stack."""
    def __init__(self)
class MoveToFlipStation(DfState)
    """State that moves the end-effector to the flip station pose."""
    def __init__(self)
    def enter(self)
    def step(self)
class ReleaseFlipStationBin(DfState)
    """State that releases the bin at the flip station and backs away."""
    def enter(self)
    def step(self)
class Dispatch(DfDecider)
    """Top-level decider that dispatches between picking, flipping, placing, and going home."""
    def __init__(self)
    def decide(self)
def make_decider_network(robot, monitor_fn)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/base_sample/__init__.py

```
"""Base sample framework for creating interactive Isaac Sim examples with UI templates."""
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/base_sample/base_sample.py

```
"""Abstract base class for creating interactive Isaac Sim examples and samples.

.. deprecated::
    This module is deprecated. Use :mod:`isaacsim.examples.base.base_sample_experimental`
    (``BaseSample`` from ``isaacsim.examples.base``) which uses the new experimental APIs
    (``SimulationManager``, ``app_utils``, ``stage_utils``) instead of the legacy ``World`` API."""
class BaseSample(object)
    """Abstract base class for creating interactive Isaac Sim examples and samples.

This class provides a standardized framework for building interactive demonstrations and examples in Isaac Sim.
It manages the simulation world lifecycle, handles common operations like loading, resetting, and clearing sce"""
    def __init__(self)
    def get_world(self)
    def set_world_settings(self, physics_dt, stage_units_in_meters, rendering_dt)
    def load_world_async(self)
    def reset_async(self)
    def setup_scene(self, scene)
    def setup_post_load(self)
    def setup_pre_reset(self)
    def setup_post_reset(self)
    def setup_post_clear(self)
    def _world_cleanup(self)
    def world_cleanup(self)
    def clear_async(self)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/base_sample/base_sample_extension.py

```
"""Provides a base template class for creating interactive Isaac Sim example user interfaces.

.. deprecated::
    This module is deprecated. Use :mod:`isaacsim.examples.base.base_sample_experimental`
    and its corresponding UI template which use the new experimental APIs
    (``SimulationManager``, ``app_utils``, ``stage_utils``) instead of the legacy ``World`` API."""
class BaseSampleUITemplate()
    """Base template class for creating interactive Isaac Sim example UIs.

This class provides a standardized UI for Isaac Sim examples, including world controls,
header information, and extensible frames for custom content. It manages the lifecycle of sample
execution including loading, resetting, and cl"""
    def __init__(self)
    def sample(self)
    def sample(self, sample)
    def get_world(self)
    def build_window(self)
    def build_ui(self)
    def build_default_frame(self)
    def get_extra_frames_handle(self)
    def build_extra_frames(self)
    def _on_load_world(self)
    def _on_reset(self)
    def post_reset_button_event(self)
    def post_load_button_event(self)
    def post_clear_button_event(self)
    def _enable_all_buttons(self, flag)
    def on_shutdown(self)
    def on_stage_event(self, event)
    def _reset_on_stop_event(self, event)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/cortex/cortex_base.py

```
"""Base class for Cortex-based interactive examples with CortexWorld integration."""
class CortexBase(BaseSample)
    """Base class for Cortex-based interactive examples.

This class extends BaseSample to provide Cortex framework integration for Isaac Sim interactive examples.
It initializes a CortexWorld instance instead of a standard World, enabling access to Cortex-specific
functionality such as behavior trees, dec"""
    def load_world_async(self)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/franka_cortex/__init__.py

```
"""Interactive Franka Cortex extension module for Isaac Sim robotic simulation examples."""
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/franka_cortex/franka_cortex.py

```
"""Interactive Franka robot control system using the Cortex framework for behavior-based manipulation tasks."""
class CubeSpec()
    """Specification for creating cube objects in the Isaac Sim interactive examples.

This class encapsulates the properties needed to define a cube object, including its identifier and visual
appearance. It is used to specify cube parameters before creating actual cube objects in the simulation scene.

A"""
    def __init__(self, name, color)
class ContextStateMonitor(DfDiagnosticsMonitor)
    """State monitor to read the context and pass it to the UI.

For these behaviors, the context has a `diagnostic_message` that contains the text to be displayed, and each
behavior implements its own monitor to update that.

Args:
    print_dt: Time interval between diagnostic prints.
    diagnostic_fn: """
    def __init__(self, print_dt, diagnostic_fn)
    def print_diagnostics(self, context)
class FrankaCortex(CortexBase)
    """Cortex-based Franka robot control system for interactive demonstrations.

Provides a complete framework for controlling a Franka robot using Cortex behaviors in an interactive
environment. The class sets up a scene with the Franka robot and colored cube obstacles, manages behavior
loading and execut"""
    def __init__(self, monitor_fn)
    def setup_scene(self)
    def load_behavior(self, behavior)
    def clear_behavior(self)
    def setup_post_load(self, soft)
    def _on_monitor_update(self, context)
    def _on_physics_step(self, step_size)
    def on_event_async(self)
    def setup_pre_reset(self)
    def world_cleanup(self)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/franka_cortex/franka_cortex_extension.py

```
"""Extension providing interactive examples for integrating the Cortex framework with Franka robotic arm behaviors in Isaac Sim."""
class FrankaCortexExtension(IExt)
    """Extension demonstrating Cortex framework integration with Franka robotic arm examples.

This extension provides an interactive interface for exploring various Cortex behaviors with a Franka robot,
including block stacking, state machines, decider networks, and interactive games. It showcases how to """
    def on_startup(self, ext_id)
    def on_shutdown(self)
class FrankaCortexUI(BaseSampleUITemplate)
    """A user interface for the Franka Cortex examples in Isaac Sim.

This class provides an interactive GUI for running various Cortex behavior examples with a Franka robot.
It allows users to select different behaviors such as block stacking, state machines, decider networks,
and peck games. The interfac"""
    def __init__(self)
    def build_ui(self)
    def build_extra_frames(self)
    def _on_load_world(self)
    def on_diagnostics(self, diagnostic, decision_stack)
    def get_world(self)
    def get_behavior(self)
    def _on_start_button_event(self)
    def post_reset_button_event(self)
    def post_load_button_event(self)
    def post_clear_button_event(self)
    def __on_selected_behavior_changed(self, selected_index)
    def build_task_controls_ui(self)
    def build_diagnostic_ui(self)
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/ur10_palletizing/__init__.py

```
"""Interactive example demonstrating UR10 robotic arm performing palletizing tasks with bin stacking operations."""
```

### source/deprecated/isaacsim.cortex.examples/isaacsim/cortex/examples/ur10_palletizing/ur10_palletizing.py

```
"""Interactive example demonstrating robotic bin stacking using a UR10 robot with autonomous bin handling on a conveyor system."""
class Ur10Assets()
    """Container for asset file paths used in the UR10 bin stacking demonstration.

This class provides centralized access to USD file paths for all assets required in the UR10 bin stacking
scenario, including the robot workspace, bins, environment backgrounds, and interactive objects. All paths
are resolv"""
    def __init__(self)
def random_bin_spawn_transform()
class BinStackingTask(BaseTask)
    """A robotic task for bin stacking automation using a UR10 robot.

This task manages the dynamic spawning and manipulation of bins on a conveyor system. It continuously
spawns bins with random orientations and positions, monitors their movement through the conveyor system,
and coordinates with the robo"""
    def __init__(self, env_path, assets)
    def _spawn_bin(self, rigid_bin)
    def post_reset(self)
    def pre_step(self, time_step_index, simulation_time)
    def world_cleanup(self)
class BinStacking(CortexBase)
    """Interactive example demonstrating robotic bin stacking using a UR10 robot.

This class sets up a complete bin stacking simulation where a UR10 robot autonomously picks up bins
from a conveyor belt and stacks them. The simulation includes:

- A UR10 robot with suction gripper capabilities
- Dynamic b"""
    def __init__(self, monitor_fn)
    def setup_scene(self)
    def setup_post_load(self)
    def _on_monitor_update(self, diagnostics)
    def _on_physics_step(self, step_size)
    def on_event_async(self)
    def setup_pre_reset(self)
    def world_cleanup(self)
```