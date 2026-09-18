# isaaclab_2025

source: https://github.com/isaac-sim/IsaacLab


commit: 291e9c67172318037fdc093d7301935637d1ff3e


## README

![Isaac Lab](docs/source/_static/isaaclab.jpg)

---

# Isaac Lab 3.0.0

[![IsaacSim](https://img.shields.io/badge/IsaacSim-6.1.0-silver.svg)](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://docs.python.org/3/whatsnew/3.12.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/22.04/)
[![Windows platform](https://img.shields.io/badge/platform-windows--64-orange.svg)](https://www.microsoft.com/en-us/)
[![pre-commit](https://img.shields.io/github/actions/workflow/status/isaac-sim/IsaacLab/pre-commit.yaml?logo=pre-commit&logoColor=white&label=pre-commit&color=brightgreen)](https://github.com/isaac-sim/IsaacLab/actions/workflows/pre-commit.yaml)
[![docs status](https://img.shields.io/github/actions/workflow/status/isaac-sim/IsaacLab/docs.yaml?label=docs&color=brightgreen)](https://github.com/isaac-sim/IsaacLab/actions/workflows/docs.yaml)
[![License](https://img.shields.io/badge/license-BSD--3-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![License](https://img.shields.io/badge/license-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0)


This branch targets Isaac Sim 6.1. For installation instructions, see the
[Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/develop/source/setup/installation/index.html).

Note that this branch is currently under active development and may experience breaking changes or error messages.
Performance issues and regressions may also be observed in some use cases.


**Isaac Lab** is a GPU-accelerated, open-source framework designed to unify and simplify robotics research workflows,
such as reinforcement learning, imitation learning, and motion planning. Built on [NVIDIA Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html),
it combines fast and accurate physics and sensor simulation, making it an ideal choice for sim-to-real
transfer in robotics.

Isaac Lab provides developers with a range of essential features for accurate sensor simulation, such as RTX-based
cameras, LIDAR, or contact sensors. The framework's GPU acceleration enables users to run complex simulations and
computations faster, which is key for iterative processes like reinforcement learning and data-intensive tasks.
Moreover, Isaac Lab can run locally or be distributed across the cloud, offering flexibility for large-scale deployments.

A detailed description of Isaac Lab can be found in our [arXiv paper](https://arxiv.org/abs/2511.04831).

## Key Features

Isaac Lab offers a comprehensive set of tools and environments designed to facilitate robot learning:

- **Robots**: A diverse collection of robots, from manipulators, quadrupeds, to humanoids, with more than 16 commonly available models.
- **Environments**: Ready-to-train implementations of more than 30 environments, which can be trained with popular reinforcement learning frameworks such as RSL RL, SKRL, RL Games, or Stable Baselines. We also support multi-agent reinforcement learning.
- **Physics**: Rigid bodies, articulated systems, deformable objects
- **Sensors**: RGB/depth/segmentation cameras, camera annotations, IMU, contact sensors, ray casters.


## Getting Started

### Documentation

Our [documentation page](https://isaac-sim.github.io/IsaacLab/develop/) provides everything you need to get started, including
detailed tutorials and step-by-step guides. Follow these links to learn more about:

- [Installation steps](https://isaac-sim.github.io/IsaacLab/develop/source/setup/installation/index.html)
- [Reinforcement learning](https://isaac-sim.github.io/IsaacLab/develop/source/concepts/reinforcement_learning.html)
- [Tutorials and how-to guides](https://isaac-sim.github.io/IsaacLab/develop/source/how-to/index.html)
- [Available environments](https://isaac-sim.github.io/IsaacLab/develop/source/setup/environments.html)

## Performance Dashboard

We continuously benchmark Isaac Lab across different physics backends, renderers, and data types.
The **[Isaac Lab Performance Dashboard](https://nvidia.github.io/omniperf/)** provides interactive
charts showing preset comparison results, performance history, and environment scaling data from
our internal CI/CD benchmarks.

## Isaac Sim Version Dependency

Isaac Lab is built on top of Isaac Sim and requires specific versions of Isaac Sim that are compatible with each
release of Isaac Lab. Below, we outline the recent Isaac Lab releases and GitHub branches and their corresponding
dependency versions for Isaac Sim.

| Isaac Lab Version             | Isaac Sim Version         |
| ----------------------------- | ------------------------- |
| `release/3.0.0` branch        | Isaac Sim 6.1             |
| `develop` branch              | Isaac Sim 6.1             |
| `main` branch                 | Isaac Sim 4.5 / 5.0 / 5.1 |
| `v3.0.0-EA` tag               | Isaac Sim 6.1             |
| `v3.0.0-beta2` tag            | Isaac Sim 6.0             |
| `v2.3.X`                      | Isaac Sim 4.5 / 5.0 / 5.1 |
| `v2.2.X`                      | Isaac Sim 4.5 / 5.0       |
| `v2.1.X`                      | Isaac Sim 4.5             |
| `v2.0.X`                      | Isaac Sim 4.5             |

## Contributing to Isaac Lab

We wholeheartedly welcome contributions from the community to make this framework mature and useful for everyone.
These may happen as bug reports, feature requests, or code contributions. For details, please check our
[contribution guidelines](https://isaac-sim.github.io/IsaacLab/develop/source/refs/contributing.html).

## Show & Tell: Share Your Inspiration

We encourage you to utilize our [Show & Tell](https://github.com/isaac-sim/IsaacLab/discussions/categories/show-and-tell)
area in the `Discussions` section of this repository. This space is designed for you to:

* Share the tutorials you've created
* Showcase your learning content
* Present exciting projects you've developed

By sharing your work, you'll inspire others and contribute to the collective knowledge
of our community. Your contributions can spark new ideas and collaborations, fostering
innovation in robotics and simulation.

## Troubleshooting

Please see the [troubleshooting](https://isaac-sim.github.io/IsaacLab/develop/source/refs/troubleshooting.html) section for
common fixes or [submit an issue](https://github.com/isaac-sim/IsaacLab/issues).

For issues related to Isaac Sim, we recommend checking its [documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)
or opening a question on its [forums](https://forums.developer.nvidia.com/c/agx-autonomous-machines/isaac/67).

## Support

* Please use GitHub [Discussions](https://github.com/isaac-sim/IsaacLab/discussions) for discussing ideas,
  asking questions, and requests for new features.
* Github [Issues](https://github.com/isaac-sim/IsaacLab/issues) should only be used to track executable pieces of
  work with a definite scope and a clear deliverable. These can be fixing bugs, documentation issues, new features,
  or general updates.

## Connect with the NVIDIA Omniverse Community

Do you have a project or resource you'd like to share more widely? We'd love to hear from you!
Reach out to the NVIDIA Omniverse Community team at OmniverseCommunity@nvidia.com to explore opportunities
to spotlight your work.

You can also join the conversation on the [Omniverse Discord](https://discord.com/invite/nvidiaomniverse) to
connect with other developers, share your projects, and help grow a vibrant, collaborative ecosystem
where creativity and technology intersect. Your contributions can make a meaningful impact on the Isaac Lab
community and beyond!

## License

The Isaac Lab framework is released under [BSD-3 License](LICENSE). The `isaaclab_mimic` extension and its
corresponding standalone scripts are released under [Apache 2.0](LICENSE-mimic). The license files of its
dependencies and assets are present in the [`docs/licenses`](docs/licenses) directory.

Note that full-featured workflows (PhysX, RTX rendering, ROS, URDF/MJCF importers) require
[Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html), which includes
components under proprietary licensing terms. Kit-less Newton workflows do not require Isaac Sim.
Please see the [Isaac Sim license](docs/licenses/dependencies/isaacsim-license.txt) for details.

Note that the `isaaclab_mimic` extension requires cuRobo, which has proprietary licensing terms that can be found in [`docs/licenses/dependencies/cuRobo-license.txt`](docs/licenses/dependencies/cuRobo-license.txt).


## Citation

If you use Isaac Lab in your research, please cite the technical report:

```
@article{mittal2025isaaclab,
  title={Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning},
  author={Mayank Mittal and Pascal Roth and James Tigue and Antoine Richard and Octi Zhang and Peter Du and Antonio Serrano-Muñoz and Xinjie Yao and René Zurbrügg and Nikita Rudin and Lukasz Wawrzyniak and Milad Rakhsha and Alain Denzler and Eric Heiden and Ales Borovicka and Ossama Ahmed and Iretiayo Akinola and Abrar Anwar and Mark T. Carlson and Ji Yuan Feng and Animesh Garg and Renato Gasoto and Lionel Gulich and Yijie Guo and M. Gussert and Alex Hansen and Mihir Kulkarni and Chenran Li and Wei Liu and Viktor Makoviychuk and Grzegorz Malczyk and Hammad Mazhar and Masoud Moghani and Adithyavairavan Murali and Michael Noseworthy and Alexander Poddubny and Nathan Ratliff and Welf Rehberg and Clemens Schwarke and Ritvik Singh and James Latham Smith and Bingjie Tang and Ruchik Thaker and Matthew Trepte and Karl Van Wyk and Fangzhou Yu and Alex Millane and Vikram Ramasamy and Remo Steiner and Sangeeta Subramanian and Clemens Volk and CY Chen and Neel Jawale and Ashwin Varghese Kuruttukulam and Michael A. Lin and Ajay Mandlekar and Karsten Patzwaldt and John Welsh and Huihua Zhao and Fatima Anes and Jean-Francois Lafleche and Nicolas Moënne-Loccoz and Soowan Park and Rob Stepinski and Dirk Van Gelder and Chris Amevor and Jan Carius and Jumyung Chang and Anka He Chen and Pablo de Heras Ciechomski and Gilles Daviet and Mohammad Mohajerani and Julia von Muralt and Viktor Reutskyy and Michael Sauter and Simon Schirm and Eric L. Shi and Pierre Terdiman and Kenny Vilella and Tobias Widmer and Gordon Yeoman and Tiffany Chen and Sergey Grizan and Cathy Li and Lotus Li and Connor Smith and Rafael Wiltz and Kostas Alexis and Yan Chang and David Chu and Linxi "Jim" Fan and Farbod Farshidian and Ankur Handa and Spencer Huang and Marco Hutter and Yashraj Narang and Soha Pouya and Shiwei Sheng and Yuke Zhu and Miles Macklin and Adam Moravanszky and Philipp Reist and Yunrong Guo and David Hoeller and Gavriel State},
  journal={arXiv preprint arXiv:2511.04831},
  year={2025},
  url={https://arxiv.org/abs/2511.04831}
}
```

## Acknowledgement

Isaac Lab development initiated from the [Orbit](https://isaac-orbit.github.io/) framework.
We gratefully acknowledge the authors of Orbit for their foundational contributions.


## File tree (depth 3, assets pruned)

```
.agents/
  skills/
    isaaclab-auditing-an-issue/
    isaaclab-building-environments/
    isaaclab-converting-direct-to-manager/
    isaaclab-debugging-rl-training/
    isaaclab-diagnosing-joint-poses/
    isaaclab-following-coding-style/
    isaaclab-installing-isaac-lab/
    isaaclab-migrating-2x-to-3x/
    isaaclab-migrating-from-isaac-gym/
    isaaclab-planning-manipulation-tasks/
    isaaclab-preparing-assets-for-newton/
    isaaclab-preparing-pr-workflow/
    isaaclab-randomizing-with-events/
    isaaclab-selecting-backends/
    isaaclab-setup-troubleshooting/
    isaaclab-training-multi-gpu/
    isaaclab-training-rl-agents/
    isaaclab-transferring-policies-sim-to-sim/
    isaaclab-triaging-issue-backlog/
    isaaclab-updating-environment-docs/
    isaaclab-using-presets/
    isaaclab-using-sensors-actuators/
    isaaclab-writing-changelog-fragments/
.claude/
  skills/
.dockerignore
.gitattributes
.github/
  CODEOWNERS
  ISSUE_TEMPLATE/
    bug.md
    proposal.md
    question.md
  LICENSE_HEADER.txt
  LICENSE_HEADER_MIMIC.txt
  PULL_REQUEST_TEMPLATE.md
  actions/
    _lib/
    detect-changes/
    docker-build/
    ecr-build-push-pull/
    install-ci-collect/
    install-ci-run/
    multi-gpu/
    ovrtx-shader-cache/
    resolve-ov-pins/
    run-package-tests/
    run-tests/
    upload-omni-github-test-results/
    validate-kitless-image/
    warp-cache-key/
  labeler.yml
  scripts/
    backport.py
    resolve_backport_conflicts.py
  stale.yml
  test-subsets/
    postmerge-rendering.toml
  workflows/
    README.md
    arm-ci.yml
    backport-release-3.0.yml
    build.yaml
    changelog-check.yml
    check-links.yml
    config.yaml
    docs.yaml
    install-ci.yml
    kitless-docker.yml
    labeler.yml
    license-check.yaml
    license-exceptions.json
    nightly-changelog.yml
    nightly-isaacsim-image.yml
    pre-commit.yaml
    publish-images.yaml
    run-docker-ci.yml
    skills-check.yml
    test-fabric-multi-gpu.yaml
    test-multi-gpu-pytest.yaml
    test-multi-gpu.yaml
    tools-tests.yml
    wheel.yml
.gitignore
.pre-commit-config.yaml
.vscode/
  .gitignore
  extensions.json
  tasks.json
  tools/
    launch.template.json
    settings.template.json
AGENTS.md
CITATION.cff
CLAUDE.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
LICENSE-mimic
README.md
SECURITY.md
VERSION
apps/
  isaaclab.python.headless.kit
  isaaclab.python.headless.rendering.kit
  isaaclab.python.kit
  isaaclab.python.rendering.kit
  isaaclab.python.xr.openxr.headless.kit
  isaaclab.python.xr.openxr.kit
conftest.py
docker/
  .env.base
  .env.cloudxr-runtime
  .env.kitless
  .env.ros2
  .ros/
    cyclonedds.xml
    fastdds.xml
  Dockerfile.base
  Dockerfile.curobo
  Dockerfile.kitless
  Dockerfile.ros2
  cluster/
    .env.cluster
    cluster_interface.sh
    osmo_multi_gpu_workflow.yaml
    run_singularity.sh
    submit_job_pbs.sh
    submit_job_slurm.sh
  container.py
  container.sh
  docker-compose.cloudxr-runtime.patch.yaml
  docker-compose.yaml
  scripts/
    install_carb_env_shim.sh
    install_git_lfs.sh
  test/
    requirements.txt
    test_carb_env_shim.py
    test_container_profiles.py
    test_docker.py
    test_dockerfile_nonroot.py
    test_image_invariants.py
    test_run_install_ci.py
    test_security_dependencies.py
  utils/
    __init__.py
    container_interface.py
    state_file.py
    volume_mounts.py
    x11_utils.py
  x11.yaml
environment.yml
greptile.json
isaaclab.bat
isaaclab.sh
manim-actuator-animations-handoff.md
pyproject.toml
scripts/
  benchmarks/
    benchmark_cameras.py
    benchmark_hydra_resolve.py
    benchmark_lazy_export.py
    benchmark_load_robot.py
    benchmark_newton_raycast.py
    benchmark_renderer.py
    benchmark_view_comparison.py
    benchmark_xform_prim_view.py
    nsys_trace.json
    play.py
    runtime.py
    runtime_multigpu.py
    startup.py
    startup_multigpu.py
    startup_whitelist.yaml
    test/
    training.py
    training_multigpu.py
  demos/
    arl_robot_1.py
    arms.py
    bin_packing.py
    bipeds.py
    cables.py
    deformables.py
    h1_locomotion.py
    hands.py
    haply_teleoperation.py
    heterogeneous_scene.py
    markers.py
    mpm/
    multi_asset.py
    newton_viewer_block_and_tackle.py
    newton_viewer_dominoes.py
    pick_and_place.py
    procedural_terrain.py
    quadcopter.py
    quadrupeds.py
    sensors/
    visual_color_randomization.py
  environments/
    export_IODescriptors.py
    list_envs.py
    random_agent.py
    state_machine/
    teleoperation/
    zero_agent.py
  imitation_learning/
    isaaclab_mimic/
    locomanipulation_sdg/
    robomimic/
  reinforcement_learning/
    play.py
    ray/
    train.py
    train_multigpu.py
  tools/
    blender_obj.py
    check_instanceable.py
    convert_instanceable.py
    convert_mesh.py
    convert_mjcf.py
    convert_urdf.py
    cosmos/
    find_quaternions.py
    generate_franka_pour_reset_dataset.py
    hdf5_to_mp4.py
    merge_hdf5_datasets.py
    mp4_to_hdf5.py
    process_meshes_to_obj.py
    record_demos.py
    replay_demos.py
    test/
    train_and_publish_checkpoints.py
  tutorials/
    00_sim/
    01_assets/
    02_scene/
    03_envs/
    04_sensors/
    05_controllers/
    06_deploy/
    07_visualizers/
skills/
  README.md
  developer/
    changelog-fragments/
    coding-style/
    isaaclab-updating-environment-docs/
    issue-audit/
    issue-backlog-triage/
    pr-workflow/
  user/
    convert-direct-to-manager/
    create-environments/
    debug-rl-training/
    diagnose-joint-poses/
    domain-randomization-events/
    install-isaac-lab/
    isaaclab-transferring-policies-sim-to-sim/
    migrate-2x-to-3x/
    migrate-from-isaac-gym/
    plan-manipulation-tasks/
    prepare-assets-for-newton/
    select-backends/
    setup-troubleshooting/
    train-multi-gpu/
    train-rl-agents/
    use-presets/
    use-sensors-actuators/
source/
  isaaclab/
    changelog.d/
    isaaclab/
    pyproject.toml
    test/
  isaaclab_assets/
    changelog.d/
    isaaclab_assets/
    pyproject.toml
    test/
  isaaclab_contrib/
    changelog.d/
    isaaclab_contrib/
    pyproject.toml
    test/
  isaaclab_experimental/
    changelog.d/
    isaaclab_experimental/
    pyproject.toml
    test/
  isaaclab_mimic/
    changelog.d/
    isaaclab_mimic/
    pyproject.toml
    test/
  isaaclab_newton/
    benchmark/
    changelog.d/
    isaaclab_newton/
    pyproject.toml
    test/
  isaaclab_ov/
    benchmark/
    changelog.d/
    isaaclab_ov/
    pyproject.toml
    test/
  isaaclab_ovphysx/
    changelog.d/
  isaaclab_physx/
    benchmark/
    changelog.d/
    isaaclab_physx/
    pyproject.toml
    test/
  isaaclab_ppisp/
    isaaclab_ppisp/
    pyproject.toml
    test/
  isaaclab_rl/
    changelog.d/
    isaaclab_rl/
    pyproject.toml
    test/
    uv.lock
  isaaclab_tasks/
    changelog.d/
    isaaclab_tasks/
    pyproject.toml
    test/
  isaaclab_tasks_experimental/
    changelog.d/
    isaaclab_tasks_experimental/
    pyproject.toml
  isaaclab_teleop/
    changelog.d/
    isaaclab_teleop/
    pyproject.toml
    test/
  isaaclab_visualizers/
    isaaclab_visualizers/
    pyproject.toml
    test/
tools/
  _device_split.py
  changelog/
    cli.py
    pyproject.toml
    test/
  conftest.py
  crash_journal.py
  environ_docs.py
  hang_dump.py
  install_deps.py
  ovrtx_log.py
  pre_commit/
    check_git_lfs_pointers.sh
  run_all_tests.py
  run_install_ci.py
  run_train_envs.py
  skills/
    cli.py
    pyproject.toml
    test/
  template/
    __init__.py
    cli.py
    common.py
    generator.py
    templates/
    test_cli.py
  test/
    test_doc_redirects.py
    test_environ_docs.py
    test_list_envs.py
  test_crash_journal.py
  test_device_split.py
  test_settings.py
  update_environments_rst.py
  verify_ovrtx_shader_cache.py
  verify_warp_cache.py
  wheel_builder/
    .gitignore
    build.sh
    build_backend.py
    gen_pyproject.py
    gen_uv_overrides.py
    pyproject.toml
    stage.py
    uv-overrides.txt
uv.lock
```

## Config files (134)


### .github/actions/_lib/compute-deps-hash/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Compute deps hash'
description: >
  Compute the deps-cache hash for the Isaac Lab Docker build. Shared by the
  docker-build (local-store check) and ecr-build-push-pull (registry check)
  actions so a local hit and a registry hit always agree on the same
  `deps-<hash>` tag. Hashes the install-relevant files, resolved base image
  digest, and target platform.

inputs:
  dockerfile-path:
    description: 'Path to Dockerfile'
    required: true
  isaacsim-base-image:
    description: 'IsaacSim base image'
    required: true
  isaacsim-version:
    description: 'IsaacSim version'
    required: true
  platform:
    description: 'Target platform included in the dependency-cache identity'
    default: 'linux/amd64'
    required: false

outputs:
  hash:
    description: '16-char deps-cache hash'
    value: ${{ steps.compute.outputs.hash }}

runs:
  using: composite
  steps:
    - id: compute
      shell: bash
      env:
        DOCKERFILE_PATH: ${{ inputs.dockerfile-path }}
        ISAACSIM_BASE_IMAGE: ${{ inputs.isaacsim-base-image }}
        ISAACSIM_VERSION: ${{ inputs.isaacsim-version }}
        TARGET_PLATFORM: ${{ inputs.platform }}
      run: |
        set -euo pipefail

        # Exact files/dirs whose full content is hashed. The Dockerfile is first.
        deps_files=(
          "${DOCKERFILE_PATH}"
          .dockerignore
          docker/docker-compose.yaml
          docker/scripts/install_carb_env_shim.sh
          docker/scripts/install_git_lfs.sh
          docker/utils/volume_mounts.py
          isaaclab.sh
          environment.yml
          source/isaaclab/isaaclab/cli
          tools/wheel_builder/uv-overrides.txt
          # Pins the CI pytest deps layered onto the image after build, so a
          # change to that list must invalidate the deps cache.
          .github/actions/docker-build/action.yml
        )
        deps_manifest_pattern='(setup\.py|pyproject\.toml|setup\.cfg|extension\.toml|requirements[^/]*\.txt|uv\.lock)$'

        # Resolve the actual base image digest so a new push of a mutable tag
        # (e.g. latest-develop) invalidates the deps cache. A tag that already
        # carries a digest is its own identity, so it is used directly.
        case "${ISAACSIM_VERSION}" in
          *@sha256:*)
            base_image_digest="${ISAACSIM_VERSION##*@}"
            if ! printf '%s' "${base_image_digest}" | grep -Eq '^sha256:[0-9a-f]{64}$'; then
              echo "::error::Base image tag ${ISAACSIM_VERSION} carries a malformed digest pin."
              exit 1
            fi
            echo "🔵 Base image tag is digest-pinned; using it as the cache identity"
            ;;
          *)
            # Reading the manifest can fail transiently, so retry. Failing hard
            # afterwards is deliberate: falling back to the tag string drops the
            # digest from the cache key and hides an unreadable manifest until a
            # later, far less obvious build error. stderr is kept off stdout so
            # a warning can never be concatenated into the digest.
            base_image_digest=""
            inspect_err="$(mktemp)"
            attempts=5
            attempt=1
            while [ "${attempt}" -le "${attempts}" ]; do
              inspect_out=$(docker buildx imagetools inspect \
                "${ISAACSIM_BASE_IMAGE}:${ISAACSIM_VERSION}" \
                --format '{{json .Manifest.Digest}}' 2>"${inspect_err}" || true)
              candidate=$(printf '%s' "${inspect_out}" | tr -d '"')
              # A digest is exactly sha256: plus 64 hex characters. Anything
              # looser lets stray stdout into the cache key, and a stable
              # diagnostic string would then stop a changed base image from
              # invalidating it.
              if printf '%s' "${candidate}" | grep -Eq '^sha256:[0-9a-f]{64}$'; then
                base_image_digest="${candidate}"
                break
              fi
              echo "🟠 Base image manifest read attempt ${attempt}/${attempts} failed: $(tr '\n' ' ' < "${inspect_err}")"
              # An authorization refusal will not clear on its own, so stop
              # retrying and report it as the configuration error it is.
              if grep -Eqi 'denied|unauthorized|forbidden|insufficient_scope|401|403' "${inspect_err}"; then
                echo "::error::${ISAACSIM_BASE_IMAGE}:${ISAACSIM_VERSION} cannot be read with the credentials available to this job."
                rm -f "${inspect_err}"
                exit 1
              fi
              if [ "${attempt}" -lt "${attempts}" ]; then
                sleep $((attempt * 5))
              fi
              attempt=$((attempt + 1))
            done
            rm -f "${inspect_err}"
            if [ -z "${base_image_digest}" ]; then
              echo "::error::Cannot read the manifest for ${ISAACSIM_BASE_IMAGE}:${ISAACSIM_VERSION} after ${attempts} attempts (see the attempt logs above)."
              exit 1
            fi
            ;;
        esac
        base_image_uniq_id="${ISAACSIM_BASE_IMAGE}:${ISAACSIM_VERSION}:${base_image_digest}"

        mapfile -t manifest_files < <(git ls-files | grep -E "${deps_manifest_pattern}" || true)
        file_hash=$(git ls-files -s "${deps_files[@]}" "${manifest_files[@]}" 2>/dev/null \
          | sha256sum | cut -c1-16)
        deps_hash=$(printf '%s %s %s' "${file_hash}" "${base_image_uniq_id}" "${TARGET_PLATFORM}" \
          | sha256sum | cut -c1-16)

        echo "🔵 Deps hash: ${deps_hash}"
        echo "hash=${deps_hash}" >> "$GITHUB_OUTPUT"

```

### .github/actions/_lib/setup-docker-config/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Setup docker config'
description: >
  Point DOCKER_CONFIG at a temp config with the credential helper disabled and
  log into nvcr.io. Shared by the docker-build and ecr-build-push-pull actions.
  Idempotent: re-invoking it in the same job reuses the existing config, and a
  base-image-ref already checked in this job is not probed again, so callers
  (e.g. ecr-build-push-pull delegating to docker-build) don't need to coordinate.
  Reads NGC_API_KEY from the environment (optional; warns when missing).
  When base-image-ref names an nvcr.io image that the configured credentials are
  refused, falls back to anonymous access for that registry.

inputs:
  base-image-ref:
    description: >
      Optional "<image>:<tag>" that this job must be able to read. nvcr.io can
      refuse a credential scoped to another organization a pull token for a
      public repository instead of downgrading to anonymous, so when the
      configured credentials are denied this image and anonymous access can read
      it, the stored nvcr.io credential is dropped from the temp config. Only
      nvcr.io refs are eligible; empty skips the check.
    required: false
    default: ''

runs:
  using: composite
  steps:
    - shell: bash
      env:
        BASE_IMAGE_REF: ${{ inputs.base-image-ref }}
        STRIP_HELPER: ${{ github.action_path }}/strip_registry_auth.py
      run: |
        # The runner's credential helper backend is broken ("not implemented")
        # and causes docker login calls to fail unless we point DOCKER_CONFIG at
        # a temp config with credsStore disabled. The value is written to
        # $GITHUB_ENV so subsequent steps in the job inherit it; a second
        # invocation reuses it and only re-runs the base-image check.
        if [ -n "${DOCKER_CONFIG:-}" ] && [ -f "${DOCKER_CONFIG}/config.json" ]; then
          echo "🟢 Docker config already set up at ${DOCKER_CONFIG}, keeping it"
          DOCKER_CONFIG_DIR="${DOCKER_CONFIG}"
        else
          DOCKER_CONFIG_DIR=$(mktemp -d)
          if [ -f "${HOME}/.docker/config.json" ]; then
            python3 -c "import json; cfg=json.load(open('${HOME}/.docker/config.json')); cfg['credsStore']=''; cfg.pop('credHelpers',None); json.dump(cfg,open('${DOCKER_CONFIG_DIR}/config.json','w'))"
          else
            echo '{"credsStore":""}' > "${DOCKER_CONFIG_DIR}/config.json"
          fi
          export DOCKER_CONFIG="${DOCKER_CONFIG_DIR}"
          echo "DOCKER_CONFIG=${DOCKER_CONFIG_DIR}" >> "$GITHUB_ENV"
          # Mark this directory as ours, so a later invocation only ever edits a
          # config this action created and never the runner's persistent one.
          echo "SETUP_DOCKER_CONFIG_OWNED=${DOCKER_CONFIG_DIR}" >> "$GITHUB_ENV"
          SETUP_DOCKER_CONFIG_OWNED="${DOCKER_CONFIG_DIR}"

          if [ -n "${NGC_API_KEY:-}" ]; then
            echo "🔵 Logging into nvcr.io..."
            printf '%s' "${NGC_API_KEY}" | docker login -u '$oauthtoken' --password-stdin nvcr.io
          else
            echo "🟠 NGC_API_KEY not set - skipping nvcr.io login (normal for fork PRs)"
          fi
        fi

        if [ -z "${BASE_IMAGE_REF:-}" ]; then
          exit 0
        fi

        # ecr-build-push-pull delegates to docker-build, so this action can run
        # twice in one job with the same ref. The probes are network calls with
        # backoff, and the first run already settled the outcome, so a ref
        # checked in this job is not probed again.
        if [ "${SETUP_DOCKER_CONFIG_CHECKED_REF:-}" = "${BASE_IMAGE_REF}" ]; then
          echo "🟢 ${BASE_IMAGE_REF} was already checked in this job, skipping"
          exit 0
        fi
        echo "SETUP_DOCKER_CONFIG_CHECKED_REF=${BASE_IMAGE_REF}" >> "$GITHUB_ENV"

        # Scope: only nvcr.io shows the refuse-instead-of-downgrade behaviour.
        # Other registries (Docker Hub in particular) must keep their
        # credentials, which also serve as pull-rate-limit budget.
        base_registry="$(printf '%s' "${BASE_IMAGE_REF%%/*}" | tr '[:upper:]' '[:lower:]')"
        case "${BASE_IMAGE_REF}" in
          */*) ;;
          *) base_registry="" ;;
        esac
        case "${base_registry%%:*}" in
          nvcr.io) ;;
          *)
            echo "🔵 ${BASE_IMAGE_REF} is not an nvcr.io image; leaving the docker config unchanged"
            exit 0
            ;;
        esac

        if [ "${SETUP_DOCKER_CONFIG_OWNED:-}" != "${DOCKER_CONFIG_DIR}" ]; then
          echo "🔵 ${DOCKER_CONFIG_DIR} was not created by this action; leaving it unchanged"
          exit 0
        fi

        # One transient error must not cost a working credential, so retry and
        # keep stderr: only an authorization refusal justifies dropping it.
        probe_err="$(mktemp)"
        trap 'rm -f "${probe_err}"' EXIT
        creds_denied=""
        for attempt in 1 2 3; do
          if docker buildx imagetools inspect "${BASE_IMAGE_REF}" >/dev/null 2>"${probe_err}"; then
            echo "🟢 Configured credentials can read ${BASE_IMAGE_REF}"
            exit 0
          fi
          if grep -Eqi 'denied|unauthorized|forbidden|insufficient_scope|401|403' "${probe_err}"; then
            creds_denied="yes"
            break
          fi
          echo "🟠 Base image read attempt ${attempt}/3 failed for a non-authorization reason: $(tr '\n' ' ' < "${probe_err}")"
          [ "${attempt}" -lt 3 ] && sleep $((attempt * 5))
        done

        if [ -z "${creds_denied}" ]; then
          echo "::warning::${BASE_IMAGE_REF} could not be read and the failure does not look like an authorization refusal; leaving the docker config unchanged"
          exit 0
        fi

        anon_config_dir="$(mktemp -d)"
        trap 'rm -f "${probe_err}"; rm -rf "${anon_config_dir}"' EXIT
        echo '{"credsStore":"","auths":{}}' > "${anon_config_dir}/config.json"
        # Retried like the credentialed probe above: a transient failure here
        # would otherwise keep a credential already proven to be denied, and the
        # build would then fail on the very pull this fallback exists to rescue.
        anon_readable=""
        for attempt in 1 2 3; do
          if DOCKER_CONFIG="${anon_config_dir}" \
            docker buildx imagetools inspect "${BASE_IMAGE_REF}" >/dev/null 2>"${probe_err}"; then
            anon_readable="yes"
            break
          fi
          echo "🟠 Anonymous read attempt ${attempt}/3 failed: $(tr '\n' ' ' < "${probe_err}")"
          if [ "${attempt}" -lt 3 ]; then
            sleep $((attempt * 5))
          fi
        done

        if [ -z "${anon_readable}" ]; then
          echo "::warning::${BASE_IMAGE_REF} is unreadable with the configured credentials and anonymously; leaving the docker config unchanged"
          exit 0
        fi

        echo "🟠 Configured credentials cannot read ${BASE_IMAGE_REF}; using anonymous access for nvcr.io"
        if ! python3 "${STRIP_HELPER}" "${DOCKER_CONFIG_DIR}/config.json" "${BASE_IMAGE_REF}"; then
          echo "::warning::Could not drop the stored nvcr.io credential; the build may still fail to read ${BASE_IMAGE_REF}"
        fi

```

### .github/actions/detect-changes/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Detect Changes'
description: >-
  Decide whether a caller's gated jobs should run for the triggering event by
  matching the pull request's changed files against caller-supplied ERE
  patterns. Shared by build.yaml and arm-ci.yml. Non-PR events (and a file
  listing failure) fail open with should_run=true.
  Callers gate their jobs with `if: steps/needs ... should_run == 'true'` rather
  than a workflow-level `paths:` filter, so a job that is (or may become) a
  required status check still gets created and reports green when skipped — a
  not-triggered required check would otherwise stay pending forever.

inputs:
  patterns:
    description: >-
      Newline-delimited entries of the form `<ERE regex> :: <description>`
      (description optional). If any regex matches a changed file path,
      should_run is true.
    required: true
  triggered-jobs-push:
    description: "Human-readable list of jobs triggered on push events (step-summary text only)."
    required: false
    default: "(post-merge integration jobs)"
  triggered-jobs-pr:
    description: "Human-readable list of jobs triggered on pull_request events (step-summary text only)."
    required: false
    default: "(gated jobs)"

outputs:
  should_run:
    description: "Whether the caller's gated jobs should run for this event."
    value: ${{ steps.detect.outputs.should_run }}

runs:
  using: composite
  steps:
  - id: detect
    shell: bash
    env:
      GH_TOKEN: ${{ github.token }}
      PR_NUMBER: ${{ github.event.pull_request.number }}
      EVENT_NAME: ${{ github.event_name }}
      REPO: ${{ github.repository }}
      PATTERNS: ${{ inputs.patterns }}
      TRIGGERED_JOBS_PUSH: ${{ inputs.triggered-jobs-push }}
      TRIGGERED_JOBS_PR: ${{ inputs.triggered-jobs-pr }}
    run: |
      set -euo pipefail

      # Parse "<regex> :: <description>" lines into parallel arrays (blank
      # lines skipped; the description is optional).
      regexes=(); descs=()
      while IFS= read -r line; do
        [ -z "${line//[[:space:]]/}" ] && continue
        regexes+=("${line%% :: *}")
        if [[ "$line" == *" :: "* ]]; then descs+=("${line#* :: }"); else descs+=(""); fi
      done < <(printf '%s\n' "$PATTERNS")

      if [ "$EVENT_NAME" = "push" ]; then
        triggered_jobs="$TRIGGERED_JOBS_PUSH"
      else
        triggered_jobs="$TRIGGERED_JOBS_PR"
      fi

      any_match() {
        local files="$1" regex
        for regex in "${regexes[@]}"; do
          if grep -qE -- "$regex" <<< "$files"; then
            return 0
          fi
        done
        return 1
      }

      render_table() {
        local files="$1" i regex desc count sample shown
        echo "| Pattern | What it covers | Matched files |"
        echo "|---|---|---|"
        for i in "${!regexes[@]}"; do
          regex="${regexes[$i]}"; desc="${descs[$i]:-}"
          # escape | so it doesn't end the markdown table cell mid-regex
          shown="${regex//|/\\|}"
          count=$(grep -cE -- "$regex" <<< "$files" || true)
          if [ "$count" -gt 0 ]; then
            # paste -sd cycles delimiter chars, so join on ',' then space it out.
            sample=$(grep -m 3 -E -- "$regex" <<< "$files" | paste -sd , - | sed 's/,/, /g')
            [ "$count" -gt 3 ] && sample="$sample (and $((count - 3)) more)"
            echo "| \`$shown\` | ${desc:--} | $sample |"
          else
            echo "| \`$shown\` | ${desc:--} | - |"
          fi
        done
      }

      decide() {
        local decision="$1" reason="$2" files="${3:-}"
        echo "Decision: should_run=$decision ($reason)"
        echo "should_run=$decision" >> "$GITHUB_OUTPUT"
        {
          echo "## Change detection"
          echo ""
          if [ "$decision" = "true" ]; then
            echo "Gated jobs will **run**: $reason."
          else
            echo "Gated jobs will be **skipped**: $reason."
          fi
          echo ""
          echo "Triggered jobs: $triggered_jobs."
          if [ -n "$files" ]; then
            echo ""
            render_table "$files"
          fi
        } >> "$GITHUB_STEP_SUMMARY"
      }

      if [ "$EVENT_NAME" != "pull_request" ]; then
        decide true "non-PR event ($EVENT_NAME)"
        exit 0
      fi

      if ! changed_files="$(gh api --paginate "repos/$REPO/pulls/$PR_NUMBER/files" --jq '.[].filename')"; then
        # Fail-safe: a transient API error must not block merge. Default to running.
        echo "::warning::Could not list changed files; defaulting to running tests"
        decide true "fail-safe (could not list changed files)"
        exit 0
      fi

      printf '%s\n' "$changed_files"

      if any_match "$changed_files"; then
        decide true "relevant paths changed" "$changed_files"
      else
        decide false "no relevant paths changed" "$changed_files"
      fi

```

### .github/actions/docker-build/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Build Docker Image'
description: 'Builds a Docker image with IsaacSim and IsaacLab dependencies'

inputs:
  image-tag:
    description: 'Docker image tag to use'
    required: true
  isaacsim-base-image:
    description: 'IsaacSim base image'
    required: true
  isaacsim-version:
    description: 'IsaacSim version'
    required: true
  dockerfile-path:
    description: 'Path to Dockerfile'
    default: 'docker/Dockerfile.base'
    required: false
  context-path:
    description: 'Build context path'
    default: '.'
    required: false
  platform:
    description: 'Target platform for `docker buildx build --platform`.'
    default: 'linux/amd64'
    required: false
  cache-from:
    description: >
      Optional value for `docker buildx build --cache-from`. Typically a
      `type=registry,ref=<image>` for cross-host layer cache. Leave empty for
      pure local-only builds.
    default: ''
    required: false
  cache-to:
    description: >
      Optional value for `docker buildx build --cache-to`. Pairs with
      `cache-from` for registry-backed layer cache writes.
    default: ''
    required: false
  deps-hash:
    description: >
      Pre-computed deps-hash to use for the local deps-tag check. When empty,
      this action computes the hash itself via the `_lib/compute-deps-hash`
      action. Set by callers (e.g. `ecr-build-push-pull`) that already compute
      the hash for a registry-side check, to avoid recomputing here.
    default: ''
    required: false
  evict-stale-cache:
    description: >
      When 'true', evict `isaac-lab*:deps-*` tags older than 14 days at the
      end of the build to bound disk growth on long-lived self-hosted
      runners. Default 'false' — no implicit cleanup.
    default: 'false'
    required: false

runs:
  using: composite
  steps:

    ##### 1: Setup docker config + login to nvcr.io (optional) #####

    - name: Setup docker config and login to nvcr.io
      uses: ./.github/actions/_lib/setup-docker-config
      with:
        base-image-ref: ${{ inputs.isaacsim-base-image }}:${{ inputs.isaacsim-version }}

    ##### 2: Host disk snapshot (pre) #####

    - name: Host disk snapshot (pre)
      shell: bash
      run: |
        set +e
        docker_root=$(docker info --format '{{.DockerRootDir}}' 2>/dev/null || echo "/var/lib/docker")
        deps_count=$(docker images --filter 'reference=isaac-lab*:deps-*' -q 2>/dev/null | wc -l)
        commit_count=$(docker images --filter 'reference=isaac-lab*' -q 2>/dev/null | wc -l)
        {
          echo "## Disk snapshot (pre)"
          echo '```'
          echo "Filesystem:"
          df -h / "${docker_root}" 2>/dev/null | sort -u
          echo
          echo "docker system df:"
          docker system df
          echo
          echo "Tag counts:"
          echo "  isaac-lab* (commit + deps tags): ${commit_count}"
          echo "  isaac-lab*:deps-* (deps cache) :  ${deps_count}"
          echo
          echo "Deps tags (newest first):"
          docker images --filter 'reference=isaac-lab*:deps-*' \
            --format 'table {{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}' 2>/dev/null \
            | head -20
          echo '```'
        } | tee -a "$GITHUB_STEP_SUMMARY"

    ##### 3: Local exact-tag short-circuit #####

    - name: Check image locally
      id: local
      shell: bash
      run: |
        if docker image inspect "${{ inputs.image-tag }}" >/dev/null 2>&1; then
          echo "🟢 Image already in local docker store: ${{ inputs.image-tag }}"
          echo "hit=true" >> "$GITHUB_OUTPUT"
        else
          echo "🔵 Image not present locally, will check deps-cache / build"
        fi

    ##### 4: Local deps-tag short-circuit #####

    - name: Compute deps hash
      id: deps-hash
      if: steps.local.outputs.hit != 'true' && inputs.deps-hash == ''
      uses: ./.github/actions/_lib/compute-deps-hash
      with:
        dockerfile-path: ${{ inputs.dockerfile-path }}
        isaacsim-base-image: ${{ inputs.isaacsim-base-image }}
        isaacsim-version: ${{ inputs.isaacsim-version }}
        platform: ${{ inputs.platform }}

    - name: Check deps-tag locally
      id: local-deps
      if: steps.local.outputs.hit != 'true'
      shell: bash
      run: |
        DEPS_HASH="${{ inputs.deps-hash || steps.deps-hash.outputs.hash }}"
        LOCAL_DEPS_TAG="$(echo "${{ inputs.image-tag }}" | cut -d: -f1):deps-${DEPS_HASH}"

        echo "🔵 Local deps tag: ${LOCAL_DEPS_TAG}"
        echo "LOCAL_DEPS_TAG=${LOCAL_DEPS_TAG}" >> "$GITHUB_ENV"

        if docker image inspect "${LOCAL_DEPS_TAG}" >/dev/null 2>&1; then
          echo "🟢 Local deps-cache HIT! Retagging as ${{ inputs.image-tag }}"
          docker tag "${LOCAL_DEPS_TAG}" "${{ inputs.image-tag }}"
          echo "hit=true" >> "$GITHUB_OUTPUT"
        else
          echo "🟠 Local deps-cache MISS (will build then tag for future hits)"
        fi

    ##### 5: Full build #####

    - name: Build image
      id: build
      if: >
        steps.local.outputs.hit != 'true' &&
        steps.local-deps.outputs.hit != 'true'
      shell: bash
      run: |
        BUILD_ARGS=(
          --progress=plain
          --platform "${{ inputs.platform }}"
          -f "${{ inputs.dockerfile-path }}"
          --build-arg "ISAACSIM_BASE_IMAGE_ARG=${{ inputs.isaacsim-base-image }}"
          --build-arg "ISAACSIM_VERSION_ARG=${{ inputs.isaacsim-version }}"
          --build-arg "ISAACSIM_ROOT_PATH_ARG=/isaac-sim"
          --build-arg "ISAACLAB_PATH_ARG=/workspace/isaaclab"
          --build-arg "DOCKER_USER_HOME_ARG=/root"
          -t "${{ inputs.image-tag }}"
        )
        if [ -n "${{ inputs.cache-from }}" ]; then
          BUILD_ARGS+=( --cache-from "${{ inputs.cache-from }}" )
        fi
        if [ -n "${{ inputs.cache-to }}" ]; then
          BUILD_ARGS+=( --cache-to "${{ inputs.cache-to }}" )
        fi

        BUILDER_NAME="docker-build-${{ github.run_id }}-${{ github.job }}"
        docker buildx create --use --driver docker-container --name "${BUILDER_NAME}" \
          || docker buildx use "${BUILDER_NAME}"
        trap 'docker buildx rm "${BUILDER_NAME}" || true' EXIT

        echo "🔵 Building ${{ inputs.image-tag }}..."
        docker buildx build --load "${BUILD_ARGS[@]}" "${{ inputs.context-path }}"
        echo "was-built=true" >> "$GITHUB_OUTPUT"

    ##### 6: Layer the CI pytest harness onto the built image #####

    # Kept out of the tracked Dockerfiles, which build local dev containers and
    # ship via publish-images.yaml. Only on a real build; cache hits have it.

    - name: Layer CI test dependencies
      if: steps.build.outputs.was-built == 'true'
      shell: bash
      run: |
        set -euo pipefail
        # pip needs root; restore the image's own default user afterwards.
        image_user="$(docker image inspect --format '{{.Config.User}}' "${{ inputs.image-tag }}")"
        # Dockerfile on stdin (no context to stage). Quoted heredoc so the
        # shell leaves ISAACLAB_PATH and IMAGE_USER for Docker to expand; the
        # image tag is an action input, substituted before bash ever runs.
        docker build --platform "${{ inputs.platform }}" \
          --build-arg "IMAGE_USER=${image_user:-root}" \
          -t "${{ inputs.image-tag }}" - <<'DOCKERFILE'
        FROM ${{ inputs.image-tag }}
        ARG IMAGE_USER
        USER root
        RUN ${ISAACLAB_PATH}/isaaclab.sh -p -m pip install \
              pytest pytest-mock junitparser flaky "coverage>=7.6.1"
        USER ${IMAGE_USER}
        DOCKERFILE

    ##### 7: Tag built image with local deps-tag #####

    # Runs only when a real build happened (not on cache hits). Populates the
    # deps-tag so the next build with identical deps short-circuits at step 4.

    - name: Tag built image with local deps
```

### .github/actions/ecr-build-push-pull/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'ECR Build-Push-Pull'
description: >
  Builds a Docker image and pushes it to ECR, using ECR as the layer cache.
  If the image already exists in ECR (same tag), pulls it instead of building.
  Drop-in replacement for docker-build/action.yml with ECR-backed caching.

inputs:
  image-tag:
    description: 'Tag for the Docker image (e.g. my-image:latest).'
    required: true
  isaacsim-base-image:
    description: 'IsaacSim base image (passed as ISAACSIM_BASE_IMAGE_ARG build-arg).'
    required: true
  isaacsim-version:
    description: 'IsaacSim version (passed as ISAACSIM_VERSION_ARG build-arg).'
    required: true
  dockerfile-path:
    description: 'Path to Dockerfile, relative to the repository root'
    default: 'docker/Dockerfile.base'
    required: false
  ecr-url:
    description: >
      ECR repository URL (e.g. "123456789.dkr.ecr.us-west-2.amazonaws.com/my-repo").
      Resolved in the following order:
      1. ecr-url input, if provided.
      2. ECR_CACHE_URL environment variable on the runner.
      3. SSM parameter /github-runner/<instance-id>/ecr-cache-url.
      4. If still empty, ECR cache is skipped and the image is built locally.
    required: false
    default: ''
  cache-tag:
    description: Tag used for the ECR layer cache image (e.g. "cache-base", "cache-curobo").
    required: false
    default: 'cache'
  verify-test-path:
    description: >
      Path to a test file or directory asserted against a freshly built image, before it is
      tagged or pushed. Tests run with IMAGE_TAG set; a failure fails the action with nothing
      published, so the next run rebuilds instead of inheriting the bad image from the cache.

      Not run on an exact-tag or deps-cache hit: those serve an image that already passed when it
      was built.
    required: false
    default: ''
  pull-on-deps-hit:
    description: >
      Pull the image locally after a deps-cache hit. Needed by jobs that run
      the image in later steps of the same job: the ECR login lives in a
      temporary docker config that is removed when this action ends, so
      steps after the action cannot pull.

      Opt-in, unlike the exact-tag hit in step 4b which always pulls: a
      deps-cache hit is common on dependency-stable branches, so pulling
      unconditionally would download a multi-gigabyte image for the callers
      that only need the tag pushed.
    required: false
    default: 'false'
runs:
  using: composite
  steps:

    ##### 1: Setup docker config + Login to nvcr.io #####

    # Create a temp docker config with credsStore disabled before any login.
    # The runner's credential store backend is broken ("not implemented") and
    # causes all docker login calls to fail unless we bypass it upfront.
    # The temp config is exported as DOCKER_CONFIG so all subsequent steps
    # (including ECR login in step 3) inherit it automatically.

    - name: Setup docker config and login to nvcr.io
      uses: ./.github/actions/_lib/setup-docker-config
      with:
        base-image-ref: ${{ inputs.isaacsim-base-image }}:${{ inputs.isaacsim-version }}

    ##### 2: Resolve ECR URL #####

    # Tries: explicit input >> ECR_CACHE_URL env var >> SSM parameter on EC2.
    # Exports ECR_URL to GITHUB_ENV and sets output `available`.

    - name: Resolve ECR URL
      id: resolve-ecr
      shell: bash
      env:
        INPUT_ECR_URL: ${{ inputs.ecr-url }}
      run: |
        ECR_URL="${INPUT_ECR_URL:-}"

        if [ -z "${ECR_URL}" ]; then
          echo "🔵 ecr-url input not set, trying ECR_CACHE_URL env var..."
          ECR_URL="${ECR_CACHE_URL:-}"
          [ -n "${ECR_URL}" ] && echo "🟢 Using ECR_CACHE_URL env var: ${ECR_URL}"
        fi

        if [ -z "${ECR_URL}" ]; then
          echo "🔵 ECR_CACHE_URL env var not set, trying SSM..."
          IMDS_TOKEN=$(curl -sf -X PUT "http://169.254.169.254/latest/api/token" \
            -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") || true
          INSTANCE_ID=$(curl -sf -H "X-aws-ec2-metadata-token: ${IMDS_TOKEN}" \
            "http://169.254.169.254/latest/meta-data/instance-id") || true
          INSTANCE_REGION=$(curl -sf -H "X-aws-ec2-metadata-token: ${IMDS_TOKEN}" \
            "http://169.254.169.254/latest/meta-data/placement/region") || true

          if [ -n "${INSTANCE_ID}" ]; then
            ECR_URL=$(aws ssm get-parameter \
              --name "/github-runner/${INSTANCE_ID}/ecr-cache-url" \
              --region "${INSTANCE_REGION}" \
              --query 'Parameter.Value' --output text 2>/dev/null) || ECR_URL=""
            if [ -n "${ECR_URL}" ]; then
              echo "🟢 Resolved ECR URL from SSM (/github-runner/${INSTANCE_ID}/ecr-cache-url): ${ECR_URL}"
            else
              echo "🔵 SSM parameter not found for instance ${INSTANCE_ID}"
            fi
          else
            echo "🔵 Not running on EC2 or IMDS unavailable, skipping SSM lookup"
          fi
        fi

        if [ -n "${ECR_URL}" ]; then
          echo "ECR_URL=${ECR_URL}" >> "$GITHUB_ENV"
          echo "available=true" >> "$GITHUB_OUTPUT"
        else
          echo "🟠 ECR URL cannot be resolved. Building locally without ECR cache."
        fi

    ##### 3: Setup ECR authentication #####

    # Validates the ECR URL, derives ECR image tags, and logs into ECR.
    # DOCKER_CONFIG (with credsStore disabled) is already set by step 1.

    - name: Setup ECR authentication
      if: steps.resolve-ecr.outputs.available == 'true'
      shell: bash
      run: |
        REGISTRY=$(echo "${ECR_URL}" | cut -d'/' -f1)
        AWS_REGION=$(echo "${REGISTRY}" | sed 's/.*\.dkr\.ecr\.\(.*\)\.amazonaws\.com/\1/')

        if [ "${AWS_REGION}" = "${REGISTRY}" ]; then
          echo "🔴 Invalid ECR URL - cannot extract AWS region: ${ECR_URL}"
          echo "🔴 Expected format: <account-id>.dkr.ecr.<region>.amazonaws.com/<repo>"
          exit 1
        fi

        ECR_TAG=$(echo "${{ inputs.image-tag }}" | tr ':/' '--')
        ECR_IMAGE="${ECR_URL}:${ECR_TAG}"
        CACHE_IMAGE="${ECR_URL}:${{ inputs.cache-tag }}"

        echo "ECR_IMAGE=${ECR_IMAGE}"     >> "$GITHUB_ENV"
        echo "CACHE_IMAGE=${CACHE_IMAGE}" >> "$GITHUB_ENV"

        echo "🔵 Logging into ECR registry..."
        aws ecr get-login-password --region "${AWS_REGION}" | \
          docker login --username AWS --password-stdin "${REGISTRY}"

    ##### 4: Check if exact image exists in ECR #####

    # Lightweight manifest check - fetches only the image manifest (~KB),
    # not the actual layers.  If the exact per-commit image already exists
    # in ECR, sets output `hit: true` to skip all subsequent build/push steps.

    - name: Check exact image in ECR
      id: pull-exact
      if: steps.resolve-ecr.outputs.available == 'true'
      shell: bash
      run: |
        echo "🔵 Checking if commit-tagged image exists in ECR >> ${ECR_IMAGE}"
        if docker manifest inspect "${ECR_IMAGE}" >/dev/null 2>&1; then
          echo "🟢 Commit-tagged image found in ECR, skipping build!"
          echo "hit=true" >> "$GITHUB_OUTPUT"
        else
          echo "🟠 Image ${ECR_IMAGE} not found in ECR, will try deps-cache strategy..."
        fi

    # Pull the image when the manifest check succeeded but the image is not
    # available locally (test jobs need it for `docker run`).  Build jobs
    # that only push to ECR will already have the image or don't need it.
    - name: Pull exact image from ECR
      if: steps.pull-exact.outputs.hit == 'true'
      shell: bash
      run: |
        if docker image inspect "${{ inputs.image-tag }}" >/dev/null 2>&1; then
          echo "🟢 Image already available locally, skipping pull"
        else
          echo "🔵 Pulling ${ECR_IMAGE} from ECR..."
          docker pull "${ECR_IMAGE}"
          docker tag "${ECR_IMAGE}" "${{ inputs.image-
```

### .github/actions/install-ci-collect/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Collect Installation CI Tests'
description: >
  Runs `pytest --collect-only` against source/isaaclab/test/install_ci in a
  throw-away venv and writes the collected test list to the GitHub step
  summary. Used to gate the heavy install jobs on a fast inventory check.

inputs:
  test-filter:
    description: 'pytest -k expression (empty = collect everything)'
    required: false
    default: ''

runs:
  using: composite
  steps:
    - name: Collect tests
      shell: bash
      env:
        TEST_FILTER: ${{ inputs.test-filter }}
        # mirror what the install-tests job sees so docker-only tests are not
        # silently deselected from the collected list shown in the summary.
        ISAACLAB_INSTALL_CI_ENV: docker
      run: |
        set -uo pipefail
        venv="$RUNNER_TEMP/collect-venv"
        collected="$RUNNER_TEMP/install-ci-collected.txt"
        python3 -m venv "$venv"
        bash "$GITHUB_WORKSPACE/.github/actions/_lib/with-python-package-retries.sh" \
          "$venv/bin/pip" install --quiet pytest pytest-timeout
        # -m "not skip" hides tests with @pytest.mark.skip; they would just
        # report SKIPPED at run time and clutter the collected inventory.
        args=( --collect-only -q -m "not skip" source/isaaclab/test/install_ci )
        [ -n "$TEST_FILTER" ] && args+=(-k "$TEST_FILTER")
        "$venv/bin/pytest" "${args[@]}" 2>&1 | tee "$collected"
        rc=${PIPESTATUS[0]}
        {
          echo '```'
          cat "$collected"
          echo '```'
        } >> "$GITHUB_STEP_SUMMARY"
        exit "$rc"

```

### .github/actions/install-ci-run/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Run Installation CI Tests'
description: >
  Runs the install_ci suite inside the project's Docker harness via
  tools/run_install_ci.py and uploads the JUnit XML report as an artifact
  named install-ci-junit-<runner.arch>.

inputs:
  base-image:
    description: 'Docker base image for the test container'
    required: false
    default: 'ubuntu:24.04'
  test-filter:
    description: 'pytest -k expression (empty = run everything)'
    required: false
    default: ''

runs:
  using: composite
  steps:
    # Host runs tools/run_install_ci.py (which in turn calls tools/wheel_builder/build.sh).
    # build.sh / gen_pyproject.py use stdlib ``tomllib`` (Python 3.11+). x86 runners default
    # to Python 3.10, so install a managed 3.12 with uv and activate it for this step.
    - name: Set up Python 3.12 via uv
      uses: astral-sh/setup-uv@v6
      with:
        python-version: "3.12"
        # `auto` (the default) enables the cache only on GitHub-hosted runners;
        # this action also runs on the self-hosted arm64 runner, so force it on.
        enable-cache: true
    - name: Run Tests
      shell: bash
      env:
        BASE_IMAGE: ${{ inputs.base-image }}
        TEST_FILTER: ${{ inputs.test-filter }}
      run: |
        args=(docker --gpu --base-image "$BASE_IMAGE"
              --build-wheel
              --results-dir "${{ github.workspace }}/results"
              -- --tb=short -sv)
        [ -n "$TEST_FILTER" ] && args+=(-k "$TEST_FILTER")
        # Make `python3` resolve to the uv-managed 3.12 for build.sh's gen_pyproject.py.
        # --seed installs pip/setuptools/wheel into the venv so build.sh's `python3 -m pip install`
        # works (uv venv is otherwise pip-free).
        uv venv --seed --python 3.12 "${RUNNER_TEMP}/venv-runner"
        source "${RUNNER_TEMP}/venv-runner/bin/activate"
        tools/run_install_ci.py "${args[@]}"
    - name: Upload JUnit XML report
      if: always()
      id: upload-junit-report
      uses: actions/upload-artifact@v7
      with:
        name: install-ci-junit-${{ runner.arch }}
        path: ${{ github.workspace }}/results/results.xml
        if-no-files-found: ignore
        retention-days: 7

    - name: Upload omni-github test results
      if: always()
      uses: ./.github/actions/upload-omni-github-test-results
      with:
        junit-file: ${{ github.workspace }}/results/results.xml
        junit-log-url: ${{ steps.upload-junit-report.outputs.artifact-url }}
        artifact-prefix: pytest-results-${{ github.job }}-${{ runner.arch }}
        test-type: installation-e2e

```

### .github/actions/ovrtx-shader-cache/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'OVRTX Shader Cache'
description: >
  Restores, reports on and publishes the NVIDIA driver PSO blobs (nv_shadercache)
  that Isaac Lab rendering tests would otherwise recompile from scratch on every
  run. Requires a prior checkout.

  A composite action cannot span the caller's test step, so the phases are
  separate invocations selected by 'mode': 'restore' before the tests, then
  either 'report' or 'save' after them. Every mode recomputes the keys from the
  same key.sh, so the collection a job reads and the one it writes cannot drift.

  kit/ is compiled by the RTX renderer inside the Isaac Sim image and kitless/ by
  the pip-installed ovrtx wheel, so each tree is a separate entry keyed by its own
  producer. The mount layout that fills them lives in
  .github/actions/run-tests/run_tests.sh.

inputs:
  mode:
    description: >-
      'restore' reads the newest compatible snapshot of each tree and never
      writes. 'report' summarises how far the run compiled beyond what was
      restored. 'save' reports the same way and writes each tree the run
      actually added to back as a new snapshot; only the cache warmer uses it.
    required: true
  isaacsim-version:
    description: 'Isaac Sim image tag; identifies the exact Kit RTX build that compiles the kit/ blobs'
    required: true
  publishes:
    description: >-
      'true' when the same job later invokes this action in 'save' mode. The
      restore pass then fingerprints what it restored, so the save pass can tell
      a run that compiled new blobs from one that only read back the snapshot it
      started with. Other modes ignore it; leaving it false only costs a
      duplicate snapshot, never a lost one.
    required: false
    default: 'false'
  trees:
    description: >-
      Which cache tree(s) this job needs: 'kit', 'kitless', or 'both'. A job that
      only exercises one render path should request just that tree, so it does
      not pay the restore/save cost of the tree it never populates.
    default: 'both'
    required: false

outputs:
  host-dir:
    description: 'Parent directory holding both cache trees; bind-mounted into the test container'
    value: ${{ steps.compute.outputs.host-dir }}

runs:
  using: composite
  steps:
    # always() here and on every post-test step below: the caller already gates
    # this invocation on job status, and without it the composite inherits a
    # failed job context and skips work that stays valid after a test failure.
    # This step in particular has to run in every mode, since every later step
    # reads its outputs.
    - name: Compute OVRTX shader cache keys
      id: compute
      if: always()
      shell: bash
      env:
        ISAACSIM_VERSION: ${{ inputs.isaacsim-version }}
      run: bash "$GITHUB_ACTION_PATH/key.sh"

    - name: Restore OVRTX kit shader cache
      if: inputs.mode == 'restore' && inputs.trees != 'kitless'
      id: restore-kit
      uses: actions/cache/restore@v4
      with:
        path: ${{ steps.compute.outputs.kit-dir }}
        key: ${{ steps.compute.outputs.kit-key }}
        restore-keys: ${{ steps.compute.outputs.kit-restore-keys }}

    - name: Restore OVRTX kitless shader cache
      if: inputs.mode == 'restore' && inputs.trees != 'kit'
      id: restore-kitless
      uses: actions/cache/restore@v4
      with:
        path: ${{ steps.compute.outputs.kitless-dir }}
        key: ${{ steps.compute.outputs.kitless-key }}
        restore-keys: ${{ steps.compute.outputs.kitless-restore-keys }}

    - name: Report restored OVRTX shader cache
      if: inputs.mode == 'restore'
      shell: bash
      env:
        HOST_DIR: ${{ steps.compute.outputs.host-dir }}
        TREES: ${{ inputs.trees }}
        KIT_MATCHED_KEY: ${{ steps.restore-kit.outputs.cache-matched-key }}
        KITLESS_MATCHED_KEY: ${{ steps.restore-kitless.outputs.cache-matched-key }}
        KIT_COLLECTION: ${{ steps.compute.outputs.kit-collection }}
        KITLESS_COLLECTION: ${{ steps.compute.outputs.kitless-collection }}
        PUBLISHES: ${{ inputs.publishes }}
      run: bash "$GITHUB_ACTION_PATH/report.sh" restore

    - name: Report OVRTX shader cache growth
      if: always() && inputs.mode != 'restore'
      id: growth
      shell: bash
      env:
        HOST_DIR: ${{ steps.compute.outputs.host-dir }}
        TREES: ${{ inputs.trees }}
      run: bash "$GITHUB_ACTION_PATH/report.sh" growth

    # Each tree is gated on its own file count so a populated kit/ never carries
    # an empty kitless/ into a published snapshot. The count is empty rather than
    # '0' when the growth step aborted before counting; both mean "not measured"
    # and both must block the save, since the snapshot would publish under a key
    # every consumer prefers over the last good one.
    #
    # The changed gate is a quota guard: every save writes a new immutable entry,
    # so a warm run that only read back what it restored would spend ~270 MB of
    # the repository's cache allowance on a duplicate of the snapshot it started
    # from. It is 'true' whenever the growth step could not rule that out.
    - name: Save OVRTX kit shader cache
      if: >-
        always() && inputs.mode == 'save' && inputs.trees != 'kitless'
        && steps.growth.outputs.kit-files != ''
        && steps.growth.outputs.kit-files != '0'
        && steps.growth.outputs.kit-changed == 'true'
      uses: actions/cache/save@v4
      with:
        path: ${{ steps.compute.outputs.kit-dir }}
        key: ${{ steps.compute.outputs.kit-key }}

    - name: Save OVRTX kitless shader cache
      if: >-
        always() && inputs.mode == 'save' && inputs.trees != 'kit'
        && steps.growth.outputs.kitless-files != ''
        && steps.growth.outputs.kitless-files != '0'
        && steps.growth.outputs.kitless-changed == 'true'
      uses: actions/cache/save@v4
      with:
        path: ${{ steps.compute.outputs.kitless-dir }}
        key: ${{ steps.compute.outputs.kitless-key }}

    - name: Verify requested OVRTX shader cache tree(s) were populated
      if: always() && inputs.mode == 'save'
      shell: bash
      env:
        TREES: ${{ inputs.trees }}
        KIT_FILES: ${{ steps.growth.outputs.kit-files }}
        KITLESS_FILES: ${{ steps.growth.outputs.kitless-files }}
      run: bash "$GITHUB_ACTION_PATH/verify.sh"

```

### .github/actions/resolve-ov-pins/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Resolve OV runtime pins'
description: >
  Reads the OVRTX / OVPhysX version specifiers from [tool.isaaclab.versions] in
  the repository's pyproject.toml. CI installs these packages through a generic
  pip-package input, so this keeps the installed versions bound to the single
  source of truth instead of hardcoding ranges in the workflow.
  NOTE: The calling job must check out the code before using this action.

outputs:
  ovrtx:
    description: 'OVRTX pip requirement specifier (e.g. ovrtx>=0.3.0,<0.4.0)'
    value: ${{ steps.resolve.outputs.ovrtx }}
  ovphysx:
    description: 'OVPhysX pip requirement specifier (e.g. ovphysx==0.5.9)'
    value: ${{ steps.resolve.outputs.ovphysx }}

runs:
  using: composite
  steps:
    - name: Set up Python
      uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065  # v5
      with:
        python-version: "3.12"

    - name: Resolve pins from pyproject
      id: resolve
      shell: bash
      run: |
        set -euo pipefail
        # Capture first, write second: a missing/renamed key (or a moved section) must
        # fail the step with a clear error, never leave $GITHUB_OUTPUT with a partial or
        # empty value that would silently reintroduce an unconstrained ``pip install ovrtx``.
        pins="$(python3 <<'PY'
        import sys
        import tomllib

        with open("pyproject.toml", "rb") as f:
            vals = tomllib.load(f).get("tool", {}).get("isaaclab", {}).get("versions", {})

        def spec(pkg: str) -> str:
            # Mirror pyproject's convention: exact versions map to ``pkg==x.y.z``,
            # range specs (">=...", "<...") map to ``pkg>=...``.
            if not vals.get(pkg):
                sys.exit(f"[tool.isaaclab.versions] is missing a value for required key '{pkg}'")
            value = vals[pkg]
            return f"{pkg}=={value}" if value[0].isdigit() else f"{pkg}{value}"

        for pkg in ("ovrtx", "ovphysx"):
            print(f"{pkg}={spec(pkg)}")
        PY
        )"
        echo "$pins" >> "$GITHUB_OUTPUT"

```

### .github/actions/run-package-tests/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Run Package Tests'
description: >
  Pulls the Docker image from ECR, runs pytest inside the container, uploads
  results as an artifact, and fails fork PRs on test failures.
  NOTE: The calling job must check out the code before using this action.

inputs:
  image-tag:
    description: 'Docker image tag'
    required: true
  isaacsim-base-image:
    description: 'IsaacSim base image'
    required: true
  isaacsim-version:
    description: 'IsaacSim version'
    required: true
  dockerfile-path:
    description: 'Path to Dockerfile'
    default: 'docker/Dockerfile.base'
    required: false
  cache-tag:
    description: 'ECR cache tag'
    default: 'cache-base'
    required: false
  filter-pattern:
    description: >-
      Pattern to filter test files (e.g., isaaclab_tasks); test files whose path
      contains this pattern are included. Only one pattern can be used at a time,
      no comma-separated substrings allowed. Also supports the legacy "not <pattern>"
      form for exclude-only jobs.
    default: ''
    required: false
  exclude-pattern:
    description: >-
      Comma-separated substrings; test files whose path contains any entry are
      skipped. Combines with filter-pattern (include + exclude).
    default: ''
    required: false
  test-k-expr:
    description: >-
      Global pytest -k expression applied inside every per-file pytest run
      spawned by tools/conftest.py (combined with device-split selectors).
    default: ''
    required: false
  shard-index:
    description: 'Zero-based shard index'
    default: ''
    required: false
  shard-count:
    description: 'Total number of shards'
    default: ''
    required: false
  curobo-only:
    description: 'Run only cuRobo and SkillGen tests'
    default: 'false'
    required: false
  quarantined-only:
    description: 'Run only quarantined tests'
    default: 'false'
    required: false
  include-files:
    description: 'Comma-separated list of specific test files to include'
    default: ''
    required: false
  test-node-ids-file:
    description: 'TOML file containing exact pytest node IDs to run'
    default: ''
    required: false
  test-node-ids-key:
    description: 'Top-level key in test-node-ids-file containing the node IDs for this job'
    default: ''
    required: false
  pytest-options:
    description: 'Additional pytest options'
    default: ''
    required: false
  extra-pip-packages:
    description: 'Space-separated pip packages to install inside the Docker container before pytest starts'
    default: ''
    required: false
  extra-uv-packages:
    description: 'Space-separated packages to install with uv inside the Docker container before pytest starts'
    default: ''
    required: false
  wheelhouse-image:
    description: 'Optional digest-pinned Docker image containing /wheelhouse and /manifest.json'
    default: ''
    required: false
  wheelhouse-packages:
    description: 'Space-separated packages to install from the wheelhouse with pip --no-index'
    default: ''
  omni-github-test-type:
    description: 'Test type stored on each uploaded omni-github test row'
    default: 'pytest'
    required: false
  warp-cache:
    description: >-
      Warp kernel cache mode. Empty disables the cache. 'restore' reads the
      newest compatible snapshot and never writes; every test job uses this, so
      a pull request can never publish kernels built from unmerged code. 'save'
      restores the same way and writes the result back as a new snapshot, making
      post-merge a cumulative writeback; only warm-warp-cache uses it.
    default: ''
    required: false
  ovrtx-shader-cache:
    description: >-
      OVRTX shader cache mode. Empty disables the cache. 'restore' reads the
      newest compatible snapshot and never writes. 'save' restores and writes
      back a new snapshot; only warm-ovrtx-cache uses it.
    default: ''
    required: false
  ovrtx-shader-cache-trees:
    description: >-
      Which OVRTX cache tree(s) this job needs: 'kit', 'kitless', or 'both'. A
      job that only exercises one render path should request just that tree.
    default: 'both'
    required: false
  standalone-script-scope:
    description: 'Enable standalone script smoke tests for this scripts/ subdirectory'
    default: ''
    required: false
  standalone-script-visualizer:
    description: 'Visualizer slice used when standalone-script-scope is set'
    default: 'none'
    required: false
  standalone-script-runtime-group:
    description: 'Run Kit-dependent or non-Kit standalone script cases'
    default: ''
    required: false
  result-file:
    description: 'Optional JUnit result filename; defaults to the workflow job identifier'
    default: ''
    required: false
  container-name:
    description: 'Docker container name prefix (run-id is appended automatically)'
    required: true
runs:
  using: composite
  steps:
    # Display some details on AWS instance we're running on
    - name: AWS Instance Info
      shell: bash
      run: |
        # get instance ID for debugging purposes (if running on EC2)
        IMDS_TOKEN=$(curl -sf -X PUT "http://169.254.169.254/latest/api/token" \
          -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") || true
        if [ -n "$IMDS_TOKEN" ]; then
          INSTANCE_ID=$(curl -sf -H "X-aws-ec2-metadata-token: ${IMDS_TOKEN}" \
            "http://169.254.169.254/latest/meta-data/instance-id") || true
          INSTANCE_REGION=$(curl -sf -H "X-aws-ec2-metadata-token: ${IMDS_TOKEN}" \
              "http://169.254.169.254/latest/meta-data/placement/region") || true
          INSTANCE_TYPE=$(curl -sf -H "X-aws-ec2-metadata-token: ${IMDS_TOKEN}" \
              "http://169.254.169.254/latest/meta-data/instance-type") || true
          echo "⚪ Instance ID: ${INSTANCE_ID:-Not running on EC2}"
          echo "⚪ Instance Region: ${INSTANCE_REGION:-Not running on EC2}"
          echo "⚪ Instance Type: ${INSTANCE_TYPE:-Not running on EC2}"
          echo "⚪ Connect: https://${INSTANCE_REGION}.console.aws.amazon.com/ec2-instance-connect/ssh/home?region=${INSTANCE_REGION}&connType=standard&instanceId=${INSTANCE_ID}&osUser=ubuntu&sshPort=22&addressFamily=ipv4"
        else
          echo "🟠 Could not obtain IMDS token, probably not running on EC2"
        fi

    - name: Prepare Docker disk space
      shell: bash
      env:
        CONTAINER_NAME: ${{ inputs.container-name }}
        ISAACSIM_BASE_IMAGE: ${{ inputs.isaacsim-base-image }}
        ISAACSIM_VERSION: ${{ inputs.isaacsim-version }}
      run: |
        bash .github/actions/run-package-tests/cleanup_docker_storage.sh \
          "${ISAACSIM_BASE_IMAGE}:${ISAACSIM_VERSION}" \
          "isaacsim-pin-${CONTAINER_NAME}-${{ github.run_id }}-${{ github.run_attempt }}-pre" \
          "pre-test-cleanup" \
          "true"

    - name: Record pull start time
      id: pull-start
      shell: bash
      run: echo "time=$(date +%s)" >> "$GITHUB_OUTPUT"

    - name: Pull image from ECR
      uses: ./.github/actions/ecr-build-push-pull
      with:
        image-tag: ${{ inputs.image-tag }}
        isaacsim-base-image: ${{ inputs.isaacsim-base-image }}
        isaacsim-version: ${{ inputs.isaacsim-version }}
        dockerfile-path: ${{ inputs.dockerfile-path }}
        cache-tag: ${{ inputs.cache-tag }}

    - name: Report pull duration
      if: always()
      shell: bash
      run: |
        start_time="${{ steps.pull-start.outputs.time }}"
        if [ -z "$start_time" ]; then
          echo "🟠 Could not calculate pull duration (start time not recorded)" >> "$GITHUB_STEP_SUMMARY"
          exit 0
        fi
        elapsed=$(( $(date +%s) - start_time ))
        printf "🔵 Image pull took %dm %ds\n" $((elapsed/60)) $((elapsed%60))
        echo "🔵 Docker Image Pulled in ${elapsed}s" >> "$GITHUB_STEP
```

### .github/actions/run-tests/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Run Tests in Docker Container'
description: 'Runs pytest tests in a Docker container with GPU support and result collection'

inputs:
  test-path:
    description: 'Path to test directory or pytest arguments'
    required: true
  result-file:
    description: 'Name of the result XML file'
    required: true
  container-name:
    description: 'Name for the Docker container'
    required: true
  image-tag:
    description: 'Docker image tag to use'
    required: true
  reports-dir:
    description: 'Directory to store test results'
    default: 'reports'
    required: false
  pytest-options:
    description: 'Additional pytest options (e.g., -k filter)'
    default: ''
    required: false
  filter-pattern:
    description: >-
      Pattern to filter test files (e.g., isaaclab_tasks); test files whose path
      contains this pattern are included. Only one pattern can be used at a time,
      no comma-separated substrings allowed. Also supports the legacy "not <pattern>"
      form for exclude-only jobs.
    default: ''
    required: false
  exclude-pattern:
    description: >-
      Comma-separated substrings; test files whose path contains any entry are
      excluded. Combines with filter-pattern (include + exclude).
    default: ''
    required: false
  test-k-expr:
    description: >-
      Global pytest -k expression applied inside every per-file pytest run
      spawned by tools/conftest.py (combined with device-split selectors).
      Unlike pytest-options, this reaches the individual test processes, so it
      can deselect parametrized cases (e.g. "not ovphysx").
    default: ''
    required: false
  curobo-only:
    description: 'Run only cuRobo and SkillGen tests (requires the cuRobo Docker image)'
    default: 'false'
    required: false
  quarantined-only:
    description: 'Run only tests listed in QUARANTINED_TESTS (skipped in normal jobs)'
    default: 'false'
    required: false
  include-files:
    description: 'Comma-separated list of specific test file paths to include (e.g., source/pkg/test/test_a.py,source/pkg/test/test_b.py)'
    default: ''
    required: false
  test-node-ids-file:
    description: 'TOML file containing exact pytest node IDs to run'
    default: ''
    required: false
  test-node-ids-key:
    description: 'Top-level key in test-node-ids-file containing the node IDs for this job'
    default: ''
    required: false
  shard-index:
    description: 'Zero-based index of this shard (used with shard-count to split tests across parallel jobs)'
    default: ''
    required: false
  shard-count:
    description: 'Total number of shards (used with shard-index to split tests across parallel jobs)'
    default: ''
    required: false
  volume-mount-source:
    description: 'Host path to bind-mount at /workspace/isaaclab (for deps-cache-hit mode)'
    default: ''
    required: false
  extra-pip-packages:
    description: 'Space-separated pip packages to install inside the Docker container before pytest starts'
    default: ''
    required: false
  extra-uv-packages:
    description: 'Space-separated packages to install with uv inside the Docker container before pytest starts'
    default: ''
    required: false
  wheelhouse-host-dir:
    description: 'Host directory containing wheelhouse/ and manifest.json for offline pip installs'
    default: ''
    required: false
  wheelhouse-packages:
    description: 'Space-separated packages to install from /tmp/ovphysx-wheelhouse with pip --no-index'
    default: ''
  warp-cache-host-dir:
    description: 'Host Warp kernel cache directory bind-mounted into the container as WARP_CACHE_PATH'
    default: ''
    required: false
  ovrtx-shader-cache-host-dir:
    description: >-
      Host OVRTX shader cache root. When set, its kit/ and kitless/ trees are
      bind-mounted into the container; run_tests.sh owns the mount layout.
    default: ''
    required: false
  ci-marker:
    description: 'CI_MARKER value forwarded to the container (read by tools/conftest.py to select test files by pytest marker)'
    default: ''
    required: false
  standalone-script-scope:
    description: 'Enable standalone script smoke tests for this scripts/ subdirectory'
    default: ''
    required: false
  standalone-script-visualizer:
    description: 'Visualizer slice used when standalone-script-scope is set'
    default: 'none'
    required: false
  standalone-script-runtime-group:
    description: 'Run Kit-dependent or non-Kit standalone script cases'
    default: ''
    required: false
  omni-github-test-type:
    description: 'Test type stored on each uploaded omni-github test row'
    default: 'pytest'
    required: false

runs:
  using: composite
  steps:
    - name: Run Tests in Docker Container
      shell: bash
      env:
        CONTAINER_NAME: ${{ inputs.container-name }}
        CUROBO_ONLY: ${{ inputs.curobo-only }}
        EXCLUDE_PATTERN: ${{ inputs.exclude-pattern }}
        EXTRA_PIP_PACKAGES: ${{ inputs.extra-pip-packages }}
        EXTRA_UV_PACKAGES: ${{ inputs.extra-uv-packages }}
        FILTER_PATTERN: ${{ inputs.filter-pattern }}
        IMAGE_TAG: ${{ inputs.image-tag }}
        INCLUDE_FILES: ${{ inputs.include-files }}
        OVRTX_SHADER_CACHE_HOST_DIR: ${{ inputs.ovrtx-shader-cache-host-dir }}
        PYTEST_OPTIONS: ${{ inputs.pytest-options }}
        QUARANTINED_ONLY: ${{ inputs.quarantined-only }}
        REPORTS_DIR: ${{ inputs.reports-dir }}
        RESULT_FILE: ${{ inputs.result-file }}
        SHARD_COUNT: ${{ inputs.shard-count }}
        SHARD_INDEX: ${{ inputs.shard-index }}
        STANDALONE_SCRIPT_RUNTIME_GROUP: ${{ inputs.standalone-script-runtime-group }}
        STANDALONE_SCRIPT_SCOPE: ${{ inputs.standalone-script-scope }}
        STANDALONE_SCRIPT_VISUALIZER: ${{ inputs.standalone-script-visualizer }}
        TEST_NODE_IDS_FILE: ${{ inputs.test-node-ids-file }}
        TEST_NODE_IDS_KEY: ${{ inputs.test-node-ids-key }}
        TEST_PATH: ${{ inputs.test-path }}
        TEST_K_EXPR_INPUT: ${{ inputs.test-k-expr }}
        CI_MARKER_INPUT: ${{ inputs.ci-marker }}
        VOLUME_MOUNT_SOURCE: ${{ inputs.volume-mount-source }}
        WARP_CACHE_HOST_DIR: ${{ inputs.warp-cache-host-dir }}
        WHEELHOUSE_HOST_DIR: ${{ inputs.wheelhouse-host-dir }}
        WHEELHOUSE_PACKAGES: ${{ inputs.wheelhouse-packages }}
      run: |
        bash .github/actions/run-tests/run_tests.sh "$TEST_PATH" "$RESULT_FILE" "$CONTAINER_NAME" "$IMAGE_TAG" "$REPORTS_DIR" "$PYTEST_OPTIONS" "$FILTER_PATTERN" "$EXCLUDE_PATTERN" "$CUROBO_ONLY" "$INCLUDE_FILES" "$QUARANTINED_ONLY" "$SHARD_INDEX" "$SHARD_COUNT" "$VOLUME_MOUNT_SOURCE" "$EXTRA_PIP_PACKAGES" "$TEST_NODE_IDS_FILE" "$TEST_NODE_IDS_KEY" "$WHEELHOUSE_HOST_DIR" "$WHEELHOUSE_PACKAGES" "$TEST_K_EXPR_INPUT" "$CI_MARKER_INPUT" "$STANDALONE_SCRIPT_SCOPE" "$STANDALONE_SCRIPT_VISUALIZER" "$STANDALONE_SCRIPT_RUNTIME_GROUP" "$WARP_CACHE_HOST_DIR" "$EXTRA_UV_PACKAGES" "$OVRTX_SHADER_CACHE_HOST_DIR"
    - name: Kill container on cancellation
      if: cancelled()
      shell: bash
      env:
        CONTAINER_NAME: ${{ inputs.container-name }}
      run: |
        echo "::warning::Job cancelled - force-killing container"
        docker kill "$CONTAINER_NAME" 2>/dev/null || true
        docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

    - name: Write job summary
      if: always()
      shell: bash
      env:
        REPORTS_DIR: ${{ inputs.reports-dir }}
        RESULT_FILE: ${{ inputs.result-file }}
      run: |
        report="${REPORTS_DIR}/${RESULT_FILE}"
        if [ ! -f "$report" ]; then
          echo "🟠 No test report found" >> "$GITHUB_STEP_SUMMARY"
          exit 0
        fi

        # Parse JUnit XML and produce a markdown summary.
        # Exit code 2 means the report was corrupt/unreadable - surface the
        # error in th
```

### .github/actions/upload-omni-github-test-results/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Upload omni-github test results'
description: >
  Converts a JUnit XML report into the omni-github test-result artifact
  contract and uploads it with the current GitHub repository identity.

inputs:
  junit-file:
    description: 'Path to the JUnit XML report to convert'
    required: true
  junit-log-url:
    description: 'URL of the uploaded JUnit XML artifact'
    default: ''
    required: false
  comparison-images-url:
    description: 'URL of the uploaded comparison images artifact'
    default: ''
    required: false
  artifact-prefix:
    description: 'Artifact name prefix'
    required: true
  test-tool-id:
    description: 'Identifier for the test runner that produced the JUnit report'
    default: 'pytest'
    required: false
  test-type:
    description: >-
      Suite category stored on each uploaded omni-github test row, such as
      training-e2e, rendering-correctness, pytest, etc.
    default: 'pytest'
    required: false
  retention-days:
    description: 'GitHub artifact retention in days'
    default: '7'
    required: false

runs:
  using: composite
  steps:
    - name: Convert JUnit XML to omni-github results
      id: convert
      shell: bash
      env:
        ARTIFACT_PREFIX: ${{ inputs.artifact-prefix }}
        COMPARISON_IMAGES_URL: ${{ inputs.comparison-images-url }}
        JUNIT_FILE: ${{ inputs.junit-file }}
        JUNIT_LOG_URL: ${{ inputs.junit-log-url }}
        TEST_TOOL_ID: ${{ inputs.test-tool-id }}
        TEST_TYPE: ${{ inputs.test-type }}
      run: |
        set -euo pipefail

        if [ ! -f "$JUNIT_FILE" ]; then
          echo "::warning::Skipping omni-github upload because JUnit report was not found: $JUNIT_FILE"
          echo "upload=false" >> "$GITHUB_OUTPUT"
          exit 0
        fi

        case "${RUNNER_OS:-unknown}-${RUNNER_ARCH:-unknown}" in
          Linux-X64) app_platform="linux-x86_64" ;;
          Linux-ARM64) app_platform="linux-aarch64" ;;
          Windows-X64) app_platform="windows-x86_64" ;;
          Windows-ARM64) app_platform="windows-aarch64" ;;
          macOS-X64) app_platform="macos-x86_64" ;;
          macOS-ARM64) app_platform="macos-aarch64" ;;
          *) app_platform="$(printf '%s-%s' "${RUNNER_OS:-unknown}" "${RUNNER_ARCH:-unknown}" | tr '[:upper:]' '[:lower:]')" ;;
        esac

        run_attempt="${GITHUB_RUN_ATTEMPT:-1}"
        retries=0

        # Run attempt > 1 means this job is a re-run, so adjust the retries count accordingly
        [[ "$run_attempt" =~ ^[1-9][0-9]*$ ]] && retries=$((run_attempt - 1))

        # Base directory for the artifact, which will be uploaded to GitHub
        artifact_dir="${RUNNER_TEMP}/omni-github-test-results/${ARTIFACT_PREFIX}-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}-${GITHUB_JOB}"
        rm -rf "$artifact_dir"
        mkdir -p "$artifact_dir"

        python3 "$GITHUB_ACTION_PATH/junit_to_omni_github_results.py" \
          --junit-file "$JUNIT_FILE" \
          --output-dir "$artifact_dir" \
          --test-tool-id "$TEST_TOOL_ID" \
          --test-type "$TEST_TYPE" \
          --app-platform "$app_platform" \
          --app-config "${GITHUB_JOB:-github-job}" \
          --group-name "${GITHUB_WORKFLOW:-github-workflow} / ${GITHUB_JOB:-github-job}" \
          --junit-log-url "$JUNIT_LOG_URL" \
          --comparison-images-url "$COMPARISON_IMAGES_URL" \
          --retries "$retries"

        result_json="$artifact_dir/_testoutput/test_results.json"

        # Validating with a local pinned copy of the schemas is recommended by the omni-github team.
        schema_venv="${RUNNER_TEMP}/omni-github-jsonschema-venv"
        python3 -m venv "$schema_venv"
        bash "$GITHUB_WORKSPACE/.github/actions/_lib/with-python-package-retries.sh" \
          "$schema_venv/bin/python" -m pip install -q jsonschema
        if ! "$schema_venv/bin/python" -m jsonschema \
          "$GITHUB_ACTION_PATH/result-json.schema.json" \
          --instance "$result_json"; then
          echo "::warning::Skipping omni-github upload because converted results failed schema validation: $JUNIT_FILE"
          echo "upload=false" >> "$GITHUB_OUTPUT"
          exit 0
        fi

        echo "artifact_dir=$artifact_dir" >> "$GITHUB_OUTPUT"
        echo "upload=true" >> "$GITHUB_OUTPUT"

    - name: Upload omni-github test results
      if: always() && steps.convert.outputs.upload == 'true'
      uses: actions/upload-artifact@v7
      with:
        name: ${{ inputs.artifact-prefix }}--v1-${{ github.repository_id }}-${{ github.run_id }}-${{ github.run_attempt }}-${{ job.check_run_id }}
        path: ${{ steps.convert.outputs.artifact_dir }}
        if-no-files-found: error
        retention-days: ${{ inputs.retention-days }}
        compression-level: 9

```

### .github/actions/validate-kitless-image/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: Validate Kit-less Image
description: >
  Validates the kit-less container built by kitless-docker.yml: the shared
  Cartpole training probe, OVRTX initialization, an existing pytest subset, and
  the non-root runtime contract.

inputs:
  image-tag:
    description: Local Docker image tag to validate.
    required: true

runs:
  using: composite
  steps:
  - name: Validate kit-less runtime image
    shell: bash
    env:
      IMAGE_TAG: ${{ inputs.image-tag }}
    run: |
      set -euo pipefail

      # A deps-cached image carries the dependency graph but not necessarily
      # this PR's source, so mount the checkout over the baked copy read-only.
      mount_args=(
        -v "${GITHUB_WORKSPACE}/source:/workspace/isaaclab/source:ro"
        -v "${GITHUB_WORKSPACE}/scripts:/workspace/isaaclab/scripts:ro"
        -v "${GITHUB_WORKSPACE}/apps:/workspace/isaaclab/apps:ro"
        -v "${GITHUB_WORKSPACE}/.github/actions/_lib/with-python-package-retries.sh:/with-python-package-retries.sh:ro"
      )

      docker run --rm "$IMAGE_TAG" \
        python -c '
      import importlib.util

      modules = ("rl_games", "rsl_rl", "stable_baselines3", "skrl")
      missing = [name for name in modules if importlib.util.find_spec(name) is None]
      assert not missing, f"missing core RL frameworks: {missing}"
      print("core RL frameworks available:", ", ".join(modules))
      '

      # Nothing else in this action runs ``uv run``, the documented entry point -- every other
      # step calls ``python`` directly, which is how nvbugs 6732972 stayed green here.
      docker run --rm "${mount_args[@]}" "$IMAGE_TAG" \
        bash -lc '
      set -euo pipefail
      prefix="$(uv run --extra ov python -c "import sys; print(sys.prefix)" | tail -n 1)"
      test "$prefix" = "$VIRTUAL_ENV" || {
        echo "::error::uv run resolved ${prefix}, not the image environment ${VIRTUAL_ENV}"
        exit 1
      }
      test ! -e "${ISAACLAB_PATH}/.venv"
      echo "uv run resolved the image environment: ${prefix}"
      '

      # Renderer construction loads the native OVRTX stack and creates a Vulkan
      # device. Full rendering correctness remains in build.yaml.
      docker run --rm --gpus all --network host \
        "$IMAGE_TAG" \
        python -c '
      from ovrtx import Renderer, RendererConfig

      renderer = Renderer(RendererConfig(log_file_path="/tmp/ovrtx.log", keep_system_alive=True))
      assert renderer, "ovrtx.Renderer construction returned a falsy value"
      print("ovrtx renderer initialized")
      '

      # Discover files by grep, not by pointing pytest at a directory: this image has no Isaac
      # Sim, and collecting a directory imports every module to read its markers.
      docker run --rm --gpus all --network host \
        "${mount_args[@]}" \
        "$IMAGE_TAG" \
        bash -lc '
      set -euo pipefail
      bash /with-python-package-retries.sh uv pip install --python "$VIRTUAL_ENV/bin/python" pytest
      python -m pytest \
        source/isaaclab/test/install_ci/misc/cartpole_training_smoke.py::test_train_cartpole_state_completes \
        source/isaaclab/test/benchmark/test_asset_suite_runtime_semantics.py \
        source/isaaclab/test/sim/test_urdf_converter.py \
        source/isaaclab/test/sim/test_mjcf_converter.py \
        -q -p no:cacheprovider
      '

      runtime_identity="$(docker run --rm --entrypoint bash "$IMAGE_TAG" \
        -lc 'printf "%s %s %s\n" "$(id -u)" "$(id -g)" "$(id -un 2>/dev/null || true)"')"
      read -r runtime_uid runtime_gid runtime_user <<< "$runtime_identity"
      echo "Kit-less runtime identity: uid=${runtime_uid} gid=${runtime_gid} user=${runtime_user}"
      if [ "$runtime_uid" = "0" ]; then
        echo "::error::Kit-less Docker image must not run as root by default."
        exit 1
      fi

```

### .github/actions/warp-cache-key/action.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

name: 'Warp Cache Key'
description: >
  Computes the Warp kernel cache collection prefix, per-run write key, and host
  directory for both the writer (warm-warp-cache) and the readers (test jobs).
  One action so they cannot drift; if they do, every read misses. Requires a
  prior checkout.

outputs:
  collection:
    description: 'Collection prefix shared by every entry that is mutually compatible'
    value: ${{ steps.compute.outputs.collection }}
  key:
    description: 'Write key, unique per run so each cumulative snapshot gets its own immutable entry'
    value: ${{ steps.compute.outputs.key }}
  restore-keys:
    description: 'Collection prefix used to restore the newest compatible snapshot'
    value: ${{ steps.compute.outputs.restore-keys }}
  host-dir:
    description: 'Host directory holding the Warp cache; bind-mounted into the test container'
    value: ${{ steps.compute.outputs.host-dir }}

runs:
  using: composite
  steps:
    - name: Compute Warp cache key
      id: compute
      shell: bash
      run: |
        set -euo pipefail

        # Warp, Newton and MuJoCo Warp decide whether a restored tree is usable.
        # GPU architecture deliberately stays out: Warp puts the target in the
        # artifact filename, so one collection accumulates every variant the
        # runner fleet needs instead of splitting per GPU model.
        versions="$(python3 .github/actions/warp-cache-key/collection_id.py)"
        collection="warp-v2-${RUNNER_OS}-${RUNNER_ARCH}-${versions}"

        # Cache entries are immutable, so a cumulative writeback needs a fresh
        # key every run - including docs-only merges and reruns, where the source
        # is unchanged but the cache may still have grown.
        echo "collection=${collection}" >> "$GITHUB_OUTPUT"
        echo "key=${collection}-${GITHUB_SHA}-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}" >> "$GITHUB_OUTPUT"
        echo "restore-keys=${collection}-" >> "$GITHUB_OUTPUT"
        echo "host-dir=${RUNNER_TEMP}/isaaclab-warp-cache" >> "$GITHUB_OUTPUT"

        echo "Warp cache collection: ${collection}"

```

### .github/workflows/config.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

# Shared image config for CI workflows. Loaded by the `config` job in each
# workflow via yq and exposed as job outputs (see e.g. .github/workflows/build.yaml).
# The `nvidian/isaac-sim` mirror stopped receiving nightly develop builds on 2026-06-24
# (frozen at 6.1.0-alpha.2). Both images use Isaac Sim's NGC org, which is current and
# which the CI credential can reach.
isaacsim_image_name: nvcr.io/0947644777160149/internal/isaac-sim
# Isaac Sim 6.1.0-alpha.50 (b86cf6ce) includes Kit 110.3.0-360924's fix for NVBug 6566677.
isaacsim_image_tag: latest-develop@sha256:223adbb0a6f1897ed78d40597dac2efc740843e8051779ffdcbb021a9edc1217
isaaclab_image_name: nvcr.io/0947644777160149/internal/isaac-lab
ovphysx_wheelhouse_image: ""

```

### .github/workflows/nightly-isaacsim-image.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

# Resolve the moving Isaac Sim ``latest-develop`` tag to its immutable
# manifest digest and open (or refresh) a draft PR against ``develop``.
#
# Scheduled workflows register only from the default branch, so this file
# must remain on ``develop`` while it is the repository default. The job also
# checks out ``develop`` because that is where the CI image pin is maintained.
#
# The isaaclab-bot GitHub App token is used instead of GITHUB_TOKEN so the
# branch push and PR events trigger the normal CI workflows. The App must have
# ``contents: write`` and ``pull requests: write`` on this repository.

name: Nightly Isaac Sim Image Update

on:
  schedule:
    # Run daily at 8 AM UTC, after the existing 4 AM and 5 AM workflows.
    - cron: '0 8 * * *'
  workflow_dispatch:
    inputs:
      dry_run:
        description: 'Resolve and report the latest digest without pushing a branch or opening a PR'
        required: false
        type: boolean
        default: false

permissions:
  # The App installation token below carries the write permissions. The
  # workflow's GITHUB_TOKEN only needs read access.
  contents: read

concurrency:
  group: nightly-isaacsim-image-update
  cancel-in-progress: false

env:
  CONFIG_PATH: .github/workflows/config.yaml
  SOURCE_IMAGE: nvcr.io/0947644777160149/internal/isaac-sim
  SOURCE_TAG: latest-develop
  TARGET_BRANCH: develop
  UPDATE_BRANCH: ci/nightly-isaacsim-image-update

jobs:
  update-image-pin:
    name: Update Isaac Sim image pin
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      # Reuse the isaaclab-bot App already used by nightly-changelog.yml.
      # Requesting the permissions explicitly makes a missing App permission
      # fail here with a focused error instead of later at push or PR creation.
      - uses: actions/create-github-app-token@v3
        id: app-token
        with:
          client-id: ${{ secrets.CHANGELOG_APP_CLIENT_ID }}
          private-key: ${{ secrets.CHANGELOG_APP_PRIVATE_KEY }}
          permission-contents: write
          permission-pull-requests: write
          permission-workflows: write

      - uses: actions/checkout@v6
        with:
          ref: ${{ env.TARGET_BRANCH }}
          token: ${{ steps.app-token.outputs.token }}
          fetch-depth: 0

      - name: Log in to the Isaac Sim registry
        env:
          NGC_API_KEY: ${{ secrets.NGC_API_KEY }}
        run: |
          set -euo pipefail
          if [ -z "$NGC_API_KEY" ]; then
            echo "::error::NGC_API_KEY is required to inspect the private Isaac Sim image."
            exit 1
          fi
          printf '%s' "$NGC_API_KEY" | docker login -u '$oauthtoken' --password-stdin nvcr.io

      - name: Resolve and update the image digest
        id: pin
        run: |
          set -euo pipefail

          image=$(yq -r '.isaacsim_image_name // ""' "$CONFIG_PATH")
          current=$(yq -r '.isaacsim_image_tag // ""' "$CONFIG_PATH")
          if [ -z "$image" ] || [ -z "$current" ]; then
            echo "::error::$CONFIG_PATH must define isaacsim_image_name and isaacsim_image_tag."
            exit 1
          fi
          if [ "$image" != "$SOURCE_IMAGE" ]; then
            echo "::error::$CONFIG_PATH must pin the expected Isaac Sim image: $SOURCE_IMAGE."
            exit 1
          fi

          current_digest=${current#"$SOURCE_TAG@"}
          if [ "$current_digest" = "$current" ] || ! [[ "$current_digest" =~ ^sha256:[0-9a-f]{64}$ ]]; then
            echo "::error::$CONFIG_PATH must pin $SOURCE_TAG with a sha256 digest; found '$current'."
            exit 1
          fi

          digest=$(docker buildx imagetools inspect "$SOURCE_IMAGE:$SOURCE_TAG" --format '{{.Manifest.Digest}}')
          digest=$(echo "$digest" | tr -d '[:space:]')
          if ! [[ "$digest" =~ ^sha256:[0-9a-f]{64}$ ]]; then
            echo "::error::Registry returned an invalid manifest digest: '$digest'."
            exit 1
          fi

          candidate="$SOURCE_TAG@$digest"
          changed=false
          branch_changed=false
          if [ "$candidate" = "$current" ]; then
            echo "Isaac Sim is already pinned to $candidate."
          else
            if [ "$(grep -c '^isaacsim_image_tag:' "$CONFIG_PATH")" -ne 1 ]; then
              echo "::error::$CONFIG_PATH must contain exactly one isaacsim_image_tag key."
              exit 1
            fi
            digest_value=${digest#sha256:}
            sed -i -E \
              "s|^(isaacsim_image_tag: $SOURCE_TAG@sha256:)[0-9a-f]{64}$|\\1$digest_value|" \
              "$CONFIG_PATH"
            changed=true
            branch_changed=true
            echo "Updating Isaac Sim from $current to $candidate."

            remote_ref="refs/heads/$UPDATE_BRANCH"
            if git ls-remote --exit-code origin "$remote_ref" >/dev/null 2>&1; then
              git fetch origin "+$remote_ref:refs/remotes/origin/$UPDATE_BRANCH"
              if remote_pin=$(git show "refs/remotes/origin/$UPDATE_BRANCH:$CONFIG_PATH" \
                | yq -r '.isaacsim_image_tag // ""'); then
                if [ "$remote_pin" = "$candidate" ]; then
                  branch_changed=false
                  echo "The existing update branch already carries $candidate."
                fi
              fi
            fi
          fi

          {
            echo "image=$image"
            echo "current=$current"
            echo "candidate=$candidate"
            echo "digest=$digest"
            echo "changed=$changed"
            echo "branch_changed=$branch_changed"
          } >> "$GITHUB_OUTPUT"

      - name: Commit and push the update branch
        if: ${{ steps.pin.outputs.branch_changed == 'true' && !inputs.dry_run }}
        run: |
          set -euo pipefail

          git config user.name "isaaclab-bot[bot]"
          git config user.email "282401363+isaaclab-bot[bot]@users.noreply.github.com"
          git switch -C "$UPDATE_BRANCH"
          git add "$CONFIG_PATH"
          git commit -m "Bump Isaac Sim CI image digest"

          remote_ref="refs/heads/$UPDATE_BRANCH"
          if git ls-remote --exit-code origin "$remote_ref" >/dev/null 2>&1; then
            git fetch origin "+$remote_ref:refs/remotes/origin/$UPDATE_BRANCH"
            remote_sha=$(git rev-parse "refs/remotes/origin/$UPDATE_BRANCH")
            git push --force-with-lease="$remote_ref:$remote_sha" origin "HEAD:$remote_ref"
          else
            git push --force-with-lease="$remote_ref:" origin "HEAD:$remote_ref"
          fi

      - name: Open or refresh the draft PR
        if: ${{ steps.pin.outputs.changed == 'true' && !inputs.dry_run }}
        env:
          GH_TOKEN: ${{ steps.app-token.outputs.token }}
          REPOSITORY: ${{ github.repository }}
          IMAGE: ${{ steps.pin.outputs.image }}
          CURRENT_PIN: ${{ steps.pin.outputs.current }}
          CANDIDATE_PIN: ${{ steps.pin.outputs.candidate }}
          DIGEST: ${{ steps.pin.outputs.digest }}
          BRANCH_CHANGED: ${{ steps.pin.outputs.branch_changed }}
        run: |
          set -euo pipefail

          digest_value=${DIGEST#sha256:}
          short_digest=${digest_value:0:12}
          title="[CI] Bump Isaac Sim image to $short_digest"
          body_file="$RUNNER_TEMP/isaacsim-image-update.md"
          {
            echo "# Description"
            echo
            echo "This automated draft updates CI to the current Isaac Sim nightly image."
            echo
            echo "| Field | Value |"
            echo "|---|---|"
            printf "| Image | \`%s\` |\n" "$IMAGE"
            printf "| Moving tag | \`%s\` |\n" "$SOURCE_TAG"
            printf "| Current pin | \`%s\` |\n" "$CURRENT_PIN"
            printf "| Candidate pin | \`%s\` |\n" "$CANDIDATE_PIN"
            echo
            echo "Source: https://registry
```

### .pre-commit-config.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.10
    hooks:
      # Run the linter
      - id: ruff
        args: ["--fix"]
      # Run the formatter
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
      - id: check-symlinks
      - id: destroyed-symlinks
      - id: check-added-large-files
        args: ["--maxkb=2000"]  # restrict files more than 2 MB. Should use git-lfs instead.
      - id: check-yaml
        # OSMO workflow specs are Jinja templates, so they only become valid
        # YAML once the submission-time parameters have been substituted.
        exclude: '^docker/cluster/osmo_multi_gpu_workflow\.yaml$'
      - id: check-merge-conflict
        # These verbatim license headings contain a literal "=======" separator.
        exclude: '^docs/licenses/dependencies/(mujoco|llvmlite|numba)-license\.txt$'
      - id: check-case-conflict
      - id: check-executables-have-shebangs
      - id: check-toml
      - id: end-of-file-fixer
        exclude: "^(.agents/skills/|.claude/skills$)"
      - id: check-shebang-scripts-are-executable
      - id: detect-private-key
      - id: debug-statements
  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
        additional_dependencies:
        - tomli
        exclude: "CONTRIBUTORS.md|docs/source/setup/walkthrough/concepts_env_design.rst"
  # FIXME: Figure out why this is getting stuck under VPN.
  # - repo: https://github.com/RobertCraigie/pyright-python
  #   rev: v1.1.315
  #   hooks:
  #   - id: pyright
  - repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.5.5
    hooks:
      - id: insert-license
        files: \.(pyi?|ya?ml)$
        args:
          # - --remove-header    # Remove existing license headers. Useful when updating license.
          - --license-filepath
          - .github/LICENSE_HEADER.txt
          - --use-current-year
        exclude: "source/isaaclab_mimic/|scripts/imitation_learning/isaaclab_mimic/"
  # Apache 2.0 license for mimic files
  - repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.5.5
    hooks:
      - id: insert-license
        files: ^(source/isaaclab_mimic|scripts/imitation_learning/isaaclab_mimic)/.*\.py$
        args:
          # - --remove-header    # Remove existing license headers. Useful when updating license.
          - --license-filepath
          - .github/LICENSE_HEADER_MIMIC.txt
          - --use-current-year
  - repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.10.0
    hooks:
      - id: rst-backticks
      - id: rst-directive-colons
      - id: rst-inline-touching-normal
  - repo: local
    hooks:
      - id: check-changelog-fragments
        name: check changelog fragments
        entry: python tools/changelog/cli.py check --include-worktree
        language: python
        always_run: true
        pass_filenames: false
      - id: check-git-lfs-pointers
        name: check Git LFS pointers
        entry: tools/pre_commit/check_git_lfs_pointers.sh
        language: script
        pass_filenames: true

```

### environment.yml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - pip
  - importlib_metadata

```

### skills/developer/isaaclab-updating-environment-docs/agents/openai.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

interface:
  display_name: "Update Environment Docs"
  short_description: "Keep environment browser tasks and presets current"
  default_prompt: "Use $isaaclab-updating-environment-docs to update the environment browser for a new or modified task."

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/anymal_c_direct/agents/rl_games_flat_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 42

  # environment wrapper clipping
  env:
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None

        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [128, 128, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False # flag which sets whether to load the checkpoint
  load_path: '' # path to the checkpoint to load

  config:
    name: anymal_c_flat_direct
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: False
    normalize_value: True
    value_bootstrap: True
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 0.6
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 1e-3
    lr_schedule: adaptive
    schedule_type: legacy
    kl_threshold: 0.01
    score_to_win: 20000
    max_epochs: 1500
    save_best_after: 100
    save_frequency: 50
    grad_norm: 1.0
    entropy_coef: 0.005
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 24
    minibatch_size: 24576
    mini_epochs: 5
    critic_coef: 2.0
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/anymal_c_direct/agents/rl_games_rough_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 42

  # environment wrapper clipping
  env:
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None

        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [512, 256, 128]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False # flag which sets whether to load the checkpoint
  load_path: '' # path to the checkpoint to load

  config:
    name: anymal_c_rough_direct
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: False
    normalize_value: True
    value_bootstrap: True
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 0.6
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 1e-3
    lr_schedule: adaptive
    schedule_type: legacy
    kl_threshold: 0.01
    score_to_win: 20000
    max_epochs: 1500
    save_best_after: 100
    save_frequency: 50
    grad_norm: 1.0
    entropy_coef: 0.005
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 24
    minibatch_size: 24576
    mini_epochs: 5
    critic_coef: 2.0
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/anymal_c_direct/agents/skrl_flat_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net
        input: OBSERVATIONS
        layers: [128, 128, 128]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [128, 128, 128]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 24
  learning_epochs: 5
  mini_batches: 4
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-03
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.01
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.005
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.6
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "anymal_c_flat_direct"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 36000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/anymal_c_direct/agents/skrl_rough_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net
        input: OBSERVATIONS
        layers: [512, 256, 128]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [512, 256, 128]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 24
  learning_epochs: 5
  mini_batches: 4
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-03
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.01
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.005
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.6
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "anymal_c_rough_direct"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 36000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/assemble_trocar/config/isaaclab_ppo_gr00t_assemble_trocar.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

defaults:
  - override hydra/job_logging: stdout

hydra:
  run:
    dir: .
  output_subdir: null

cluster:
  num_nodes: 1
  component_placement:
      actor,env,rollout: all

runner:
  task_type: embodied
  logger:
    log_path: "../results"
    project_name: rlinf
    experiment_name: "test_gr00t"
    logger_backends: ["tensorboard"] # wandb, swanlab

  max_epochs: 1000
  max_steps: -1

  only_eval: False
  eval_policy_path: null # Optional: .pt file or None, if None, will use the checkpoint in rollout.model.model_path
  val_check_interval: -1
  save_interval: 2
  seq_length: 4096
  max_prompt_length: 30

  resume_dir: null

algorithm:
  normalize_advantages: True
  kl_penalty: kl  # how to estimate kl divergence: kl or kl_penalty
  group_size: 1
  reward_coef: 1.0
  rollout_epoch: 2
  eval_rollout_epoch: 1 # set eval_rollout_epoch > 0 when enable runner.only_eval or runner.val_check_interval > 0

  reward_type: chunk_level
  logprob_type: chunk_level
  entropy_type: chunk_level

  update_epoch: 4
  adv_type: gae
  loss_type: actor_critic
  loss_agg_func: "token-mean"
  kl_beta: 0.0
  entropy_bonus: 0
  clip_ratio_high: 0.2
  clip_ratio_low: 0.2
  clip_ratio_c: 3.0
  value_clip: 0.2
  huber_delta: 10.0

  gamma: 0.99
  gae_lambda: 0.95

  filter_rewards: False
  rewards_lower_bound: 0.1
  rewards_upper_bound: 0.9
  # params for generation
  sampling_params:
    do_sample: True
    temperature_train: 1.0
    temperature_eval: 0.6
    top_k: 50
    top_p: 1.0
    repetition_penalty: 1.0
    add_BOS: False

  # length argument for autoregressive sampling
  # max length means max amount of tokens to generate
  length_params:
    max_new_token: null
    max_length: 1024
    min_length: 1

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
env:
  group_name: "EnvGroup"
  channel:
    name: "env_buffer_list"
    queue_name: "obs_buffer"
    queue_size: 0
  enable_offload: False

  train:
    env_type: isaaclab
    total_num_envs: 4
    auto_reset: False
    ignore_terminations: False
    use_rel_reward: True
    seed: 0
    group_size: 1
    reward_coef: 1.0
    use_fixed_reset_state_ids: True
    max_steps_per_rollout_epoch: 256
    max_episode_steps: 256
    video_cfg:
      save_video: False
      info_on_video: True
      video_base_dir: ${runner.logger.log_path}/video/train
    init_params:
      id: "IsaacContrib-Assemble-Trocar-G129-Dex3"
      num_envs: null
      max_episode_steps: ${env.train.max_episode_steps}
      task_description: "assemble trocar from tray"

    # ========================================================================
    # IsaacLab -> RLinf -> GR00T observation/action mapping configuration
    # This section defines how IsaacLab observations are converted to GR00T format
    # ========================================================================
    isaaclab: &isaaclab_config  # YAML anchor for reuse in eval
      # Task description for language conditioning
      task_description: "assemble trocar from tray"

      # --- IsaacLab -> RLinf observation mapping ---
      # main_images: single camera key for main view
      main_images: "front_camera"
      # extra_view_images: list of camera keys to stack as (B, N, H, W, C)
      extra_view_images:
        - "left_wrist_camera"
        - "right_wrist_camera"
      # states: list of state specs with optional slicing
      # Each entry can be a string (use full tensor) or dict with "key" and "slice"
      states:
        - key: "robot_joint_state"
          slice: [15, 29]  # G129 shoulder joints
        - key: "robot_dex3_joint_state"
          # slice: null  # Use full tensor

      # --- RLinf -> GR00T format conversion ---
      gr00t_mapping:
        video:
          main_images: "video.room_view"
          extra_view_images:
            - "video.left_wrist_view"
            - "video.right_wrist_view"
        state:
          # Slice concatenated states into GR00T state keys
          # Total states: 14 (shoulder) + 14 (dex3) = 28 dims
          - gr00t_key: "state.left_arm"
            slice: [0, 7]
          - gr00t_key: "state.right_arm"
            slice: [7, 14]
          - gr00t_key: "state.left_hand"
            slice: [14, 21]
          - gr00t_key: "state.right_hand"
            slice: [21, 28]

      # --- GR00T -> IsaacLab action conversion ---
      action_mapping:
        prefix_pad: 15  # Pad zeros at front for G129 body joints (not controlled)
        suffix_pad: 0

      # --- GR00T model configuration (single source of truth) ---
      # actor.model.embodiment_tag and obs_converter_type reference these values via ${}
      obs_converter_type: "dex3"
      embodiment_tag: "new_embodiment"
      embodiment_tag_id: 31
      data_config_class: "gr00t_config:IsaacLabDataConfig"

  eval:
    env_type: isaaclab
    total_num_envs: 4
    auto_reset: True
    ignore_terminations: True
    use_rel_reward: True
    seed: 0
    group_size: 1
    reward_coef: 1.0
    use_fixed_reset_state_ids: True
    max_steps_per_rollout_epoch: 256
    max_episode_steps: 256
    video_cfg:
      save_video: True
      info_on_video: True
      video_base_dir: ${runner.logger.log_path}/video/eval
    init_params:
      id: "IsaacContrib-Assemble-Trocar-G129-Dex3-Eval"
      num_envs: null
      max_episode_steps: ${env.eval.max_episode_steps}
      task_description: "install trocar from box"
    # Reuse IsaacLab config from train section via YAML anchor
    isaaclab: *isaaclab_config

# ---------------------------------------------------------------------------
# Rollout
# ---------------------------------------------------------------------------
rollout:
  group_name: "RolloutGroup"
  channel:
    name: ${env.channel.name}
    queue_name: "action_buffer"
    queue_size: 0
  mode: "colocate"
  backend: "huggingface"
  enable_offload: True
  pipeline_stage_num: 1

  model:
    model_path: "/mnt/ckpt/g1_install_trocar_sim_box_v3_60_train_bs32_1_gpus_cos_30k_tune_visual/"
    precision: ${actor.model.precision}
    obs_converter_type: ${env.train.isaaclab.obs_converter_type}
    embodiment_tag: ${env.train.isaaclab.embodiment_tag}

# ---------------------------------------------------------------------------
# Actor
# ---------------------------------------------------------------------------
actor:
  group_name: "ActorGroup"
  channel:
    name: ${env.channel.name}
    queue_name: "replay_buffer"
    queue_size: 0
  training_backend: "fsdp"
  micro_batch_size: 2
  global_batch_size: 4
  seed: 1234
  enable_offload: False

  model:
    model_type: "gr00t"
    model_path: "/mnt/ckpt/g1_install_trocar_sim_box_v3_60_train_bs32_1_gpus_cos_30k_tune_visual/"
    precision: "bf16"
    trust_remote_code: True
    is_lora: false
    action_dim: 28
    num_action_chunks: 1
    denoising_steps: 4
    policy_setup: "widowx_bridge"
    obs_converter_type: ${env.train.isaaclab.obs_converter_type}
    embodiment_tag: ${env.train.isaaclab.embodiment_tag}
    add_value_head: True
    rl_head_config:
      joint_logprob: False
      noise_method: "flow_sde"
      ignore_last: False
      safe_get_logprob: False
      noise_anneal: False
      noise_params: [0.7, 0.3, 400]
      noise_level: 0.3
      add_value_head: ${actor.model.add_value_head}
      chunk_critic_input: False
      detach_critic_input: True
      disable_dropout: True
      use_vlm_value: False
      value_vlm_mode: "mean_token"
      padding_value: 850

  optim:
    lr: 5e-6
    value_lr: 1e-4
    adam_beta1: 0.9
    adam_beta2: 0.95
    adam_eps: 1.0e-08
    clip_grad: 1.0
    weight_decay: 0.01
    critic_warmup_steps: 0

  fsdp_config:
    strategy: "fsdp"
    sharding_strategy: "full_shard"
    gradient_checkpointing: 
```

### source/isaaclab_tasks/isaaclab_tasks/contrib/automate/agents/rl_games_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 0
  algo:
    name: a2c_continuous
  env:
    clip_actions: 1.0
  model:
    name: continuous_a2c_logstd
  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [256, 128, 64]
      activation: elu
      d2rl: False
      initializer:
        name: default
      regularizer:
        name: None

    rnn:
      name: lstm
      units: 256
      layers: 2
      before_mlp: True
      concat_input: True
      layer_norm: False
  load_checkpoint: False
  load_path: ""
  config:
    name: Assembly
    device: cuda:0
    env_name: rlgpu
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: 128
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: 1e-4
    lr_schedule: fixed
    schedule_type: standard
    kl_threshold: 0.016
    score_to_win: 20000
    max_epochs: 1500
    save_best_after: 100
    save_frequency: 300
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: False
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 4096  # batch size = num_envs * horizon_length; minibatch_size = batch_size / num_minibatches
    mini_epochs: 8
    critic_coef: 2
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0001
    central_value_config:
      minibatch_size: 256
      mini_epochs: 4
      learning_rate: 1e-3
      lr_schedule: linear
      kl_threshold: 0.016
      clip_value: True
      normalize_input: True
      truncate_grads: True
      network:
        name: actor_critic
        central_value: True

        mlp:
          units: [256, 128, 64]
          activation: elu
          d2rl: False
          initializer:
            name: default
          regularizer:
            name: None

  player:
    deterministic: False

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cabinet/config/openarm/agents/rl_games_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 42

  # environment wrapper clipping
  env:
    clip_observations: 5.0
    clip_actions: 1.0

  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [256, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: False
  load_path: ''

  config:
    name: openarm_open_drawer
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    multi_gpu: False
    ppo: True
    mixed_precision: False
    normalize_input: False
    normalize_value: False
    num_actors: -1  # configured from the script (based on num_envs)
    reward_shaper:
      scale_value: 1
    normalize_advantage: False
    gamma: 0.99
    tau: 0.95
    learning_rate: 5e-4
    lr_schedule: adaptive
    kl_threshold: 0.008
    score_to_win: 200
    max_epochs: 400
    save_best_after: 50
    save_frequency: 50
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.001
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 96
    minibatch_size: 4096
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_length: 4
    bounds_loss_coef: 0.0001

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_box_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_box_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_box_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_box_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_box_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_box_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_dict_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
# obs["joint-positions"]  obs["joint-velocities"]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(+)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_dict_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_dict_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
# obs["joint-positions"]  obs["joint-velocities"]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(+)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_dict_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_dict_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
# obs["joint-positions"]  obs["joint-velocities"]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(+)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS["joint-positions"]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS["joint-velocities"]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos + net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_dict_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_discrete_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_discrete_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_discrete_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_discrete_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_discrete_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_discrete_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_multidiscrete_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_multidiscrete_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_multidiscrete_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_multidiscrete_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_multidiscrete_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#                  one_hot(obs)
#                       │
#                ┏━━━━━━▼━━━━━┓
#                ┃     net    ┃
#                ┡━━━━━━━━━━━━┩
#                │ linear(32) │
#                │ elu        │
#                │ linear(32) │
#                │ elu        │
#                └──────┬─────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: one_hot_encoding(OBSERVATION_SPACE, OBSERVATIONS)
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null  # pre-processor should not be used with Discrete/MultiDiscrete observations
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_multidiscrete_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_tuple_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs[0]                   obs[1]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(*)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_tuple_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_tuple_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs[0]                   obs[1]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(*)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_tuple_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole/agents/skrl_tuple_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs[0]                   obs[1]
#           │                        │
#    ┏━━━━━━▼━━━━━┓           ┏━━━━━━▼━━━━━┓
#    ┃   net_pos  ┃           ┃   net_vel  ┃
#    ┡━━━━━━━━━━━━┩           ┡━━━━━━━━━━━━┩
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    │ linear(16) │           │ linear(16) │
#    │ elu        │           │ elu        │
#    └──────┬─────┘           └─────┬──────┘
#           │                       │
#           └─────────▶(*)◀─────────┘
#                       │
#                 ┏━━━━━▼━━━━━┓
#                 ┃    net    ┃
#                 ┡━━━━━━━━━━━┩
#                 │ identity  │
# shared          └─────┬─────┘
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net_pos
        input: OBSERVATIONS[0]
        layers: [16, 16]
        activations: elu
      - name: net_vel
        input: OBSERVATIONS[1]
        layers: [16, 16]
        activations: elu
      - name: net
        input: net_pos * net_vel
        layers: []
        activations: []
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 32
  learning_epochs: 8
  mini_batches: 8
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: RunningStandardScaler
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.1
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_direct_tuple_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 4800
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_box_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#            ┏━━━━━━━━━━▼━━━━━━━━━━┓
#            ┃ features_extractor  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━┩
#            │ conv2d(32, 8, 4)    │
#            │ relu                │
#            │ conv2d(64, 4, 2)    │
#            │ relu                │
#            │ conv2d(64, 3, 1)    │
#            │ relu                │
#            │ flatten             │
#            └──────────┬──────────┘
#                       │
#                ┏━━━━━━▼━━━━━━┓
#                ┃     net     ┃
#                ┡━━━━━━━━━━━━━┩
#                │ linear(512) │
#                │ elu         │
#                └──────┬──────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_box_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_box_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#            ┏━━━━━━━━━━▼━━━━━━━━━━┓
#            ┃ features_extractor  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━┩
#            │ conv2d(32, 8, 4)    │
#            │ relu                │
#            │ conv2d(64, 4, 2)    │
#            │ relu                │
#            │ conv2d(64, 3, 1)    │
#            │ relu                │
#            │ flatten             │
#            └──────────┬──────────┘
#                       │
#                ┏━━━━━━▼━━━━━━┓
#                ┃     net     ┃
#                ┡━━━━━━━━━━━━━┩
#                │ linear(512) │
#                │ elu         │
#                └──────┬──────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_box_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_box_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#                      obs
#                       │
#            ┏━━━━━━━━━━▼━━━━━━━━━━┓
#            ┃ features_extractor  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━┩
#            │ conv2d(32, 8, 4)    │
#            │ relu                │
#            │ conv2d(64, 4, 2)    │
#            │ relu                │
#            │ conv2d(64, 3, 1)    │
#            │ relu                │
#            │ flatten             │
#            └──────────┬──────────┘
#                       │
#                ┏━━━━━━▼━━━━━━┓
#                ┃     net     ┃
#                ┡━━━━━━━━━━━━━┩
#                │ linear(512) │
#                │ elu         │
#                └──────┬──────┘
# shared                │
# ......................│.......................
# non-shared            │
#           ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#           ┃  policy|value output  ┃
#           ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#           │ linear(num_actions|1) │
#           └───────────┬───────────┘
#                       ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
        activations: relu
      - name: net
        input: features_extractor
        layers: [512]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_box_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_dict_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs["camera"]      obs["joint-velocities"]
#               │                        │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓             │
#    ┃ features_extractor  ┃             │
#    ┡━━━━━━━━━━━━━━━━━━━━━┩             │
#    │ conv2d(32, 8, 4)    │             │
#    │ relu                │             │
#    │ conv2d(64, 4, 2)    │             │
#    │ relu                │             │
#    │ conv2d(64, 3, 1)    │             │
#    │ relu                │             │
#    │ flatten             │             │
#    │ linear(512)         │             │
#    │ tanh                │             │
#    │ linear(16)          │             │
#    │ tanh                │             │
#    └──────────┬──────────┘             |
#               │                        │
#               └─▶(concatenate)◀────────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS["camera"], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_dict_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_dict_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs["camera"]      obs["joint-velocities"]
#               │                        │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓             │
#    ┃ features_extractor  ┃             │
#    ┡━━━━━━━━━━━━━━━━━━━━━┩             │
#    │ conv2d(32, 8, 4)    │             │
#    │ relu                │             │
#    │ conv2d(64, 4, 2)    │             │
#    │ relu                │             │
#    │ conv2d(64, 3, 1)    │             │
#    │ relu                │             │
#    │ flatten             │             │
#    │ linear(512)         │             │
#    │ tanh                │             │
#    │ linear(16)          │             │
#    │ tanh                │             │
#    └──────────┬──────────┘             |
#               │                        │
#               └─▶(concatenate)◀────────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS["camera"], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_dict_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_dict_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#         obs["camera"]      obs["joint-velocities"]
#               │                        │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓             │
#    ┃ features_extractor  ┃             │
#    ┡━━━━━━━━━━━━━━━━━━━━━┩             │
#    │ conv2d(32, 8, 4)    │             │
#    │ relu                │             │
#    │ conv2d(64, 4, 2)    │             │
#    │ relu                │             │
#    │ conv2d(64, 3, 1)    │             │
#    │ relu                │             │
#    │ flatten             │             │
#    │ linear(512)         │             │
#    │ tanh                │             │
#    │ linear(16)          │             │
#    │ tanh                │             │
#    └──────────┬──────────┘             |
#               │                        │
#               └─▶(concatenate)◀────────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS["camera"], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS, (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: net
        input: concatenate([features_extractor, OBSERVATIONS["joint-velocities"]])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_dict_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_tuple_box_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#             obs[0]                  obs[1]
#               │                       │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓    ┏━━━━━━━▼━━━━━━━━┓
#    ┃ features_extractor  ┃    ┃ proprioception ┃
#    ┡━━━━━━━━━━━━━━━━━━━━━┩    ┡━━━━━━━━━━━━━━━━┩
#    │ conv2d(32, 8, 4)    │    │ linear(16)     │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 4, 2)    │    │ linear(8)      │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 3, 1)    │    └───────┬────────┘
#    │ relu                │            │
#    │ flatten             │            │
#    │ linear(512)         │            │
#    │ tanh                │            │
#    │ linear(16)          │            │
#    │ tanh                │            │
#    └──────────┬──────────┘            |
#               │                       │
#               └─▶(concatenate)◀───────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_tuple_box"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_tuple_discrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#             obs[0]                  obs[1]
#               │                       │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓    ┏━━━━━━━▼━━━━━━━━┓
#    ┃ features_extractor  ┃    ┃ proprioception ┃
#    ┡━━━━━━━━━━━━━━━━━━━━━┩    ┡━━━━━━━━━━━━━━━━┩
#    │ conv2d(32, 8, 4)    │    │ linear(16)     │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 4, 2)    │    │ linear(8)      │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 3, 1)    │    └───────┬────────┘
#    │ relu                │            │
#    │ flatten             │            │
#    │ linear(512)         │            │
#    │ tanh                │            │
#    │ linear(16)          │            │
#    │ tanh                │            │
#    └──────────┬──────────┘            |
#               │                       │
#               └─▶(concatenate)◀───────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see categorical_model parameters
    class: CategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_tuple_discrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/cartpole_showcase/cartpole_camera/agents/skrl_tuple_multidiscrete_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
#
#             obs[0]                  obs[1]
#               │                       │
#    ┏━━━━━━━━━━▼━━━━━━━━━━┓    ┏━━━━━━━▼━━━━━━━━┓
#    ┃ features_extractor  ┃    ┃ proprioception ┃
#    ┡━━━━━━━━━━━━━━━━━━━━━┩    ┡━━━━━━━━━━━━━━━━┩
#    │ conv2d(32, 8, 4)    │    │ linear(16)     │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 4, 2)    │    │ linear(8)      │
#    │ relu                │    │ elu            │
#    │ conv2d(64, 3, 1)    │    └───────┬────────┘
#    │ relu                │            │
#    │ flatten             │            │
#    │ linear(512)         │            │
#    │ tanh                │            │
#    │ linear(16)          │            │
#    │ tanh                │            │
#    └──────────┬──────────┘            |
#               │                       │
#               └─▶(concatenate)◀───────┘
#                        │
#                 ┏━━━━━━▼━━━━━┓
#                 ┃     net    ┃
#                 ┡━━━━━━━━━━━━┩
#                 │ linear(32) │
#                 │ elu        │
#                 │ linear(32) │
#                 │ elu        │
#                 └──────┬─────┘
# shared                 │
# .......................│.......................
# non-shared             │
#            ┏━━━━━━━━━━━▼━━━━━━━━━━━┓
#            ┃  policy|value output  ┃
#            ┡━━━━━━━━━━━━━━━━━━━━━━━┩
#            │ linear(num_actions|1) │
#            └───────────┬───────────┘
#                        ▼
models:
  separate: False
  policy:  # see multicategorical_model parameters
    class: MultiCategoricalMixin
    unnormalized_log_prob: True
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: features_extractor
        input: permute(OBSERVATIONS[0], (0, 3, 1, 2))  # PyTorch NHWC -> NCHW. Warning: don't permute for JAX since it expects NHWC
        layers:
          - conv2d: {out_channels: 32, kernel_size: 8, stride: 4, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 4, stride: 2, padding: 0}
          - conv2d: {out_channels: 64, kernel_size: 3, stride: 1, padding: 0}
          - flatten
          - linear: 512
          - linear: 16
        activations: [relu, relu, relu, null, tanh, tanh]
      - name: proprioception
        input: OBSERVATIONS[1]
        layers: [16, 8]
        activations: elu
      - name: net
        input: concatenate([features_extractor, proprioception])
        layers: [32, 32]
        activations: elu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 64
  learning_epochs: 4
  mini_batches: 32
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-04
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.008
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  mixed_precision: False
  # logging and checkpoint
  experiment:
    directory: "cartpole_camera_direct_tuple_multidiscrete"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 32000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/drone_arl/navigation/config/arl_robot_1/agents/rl_games_rough_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 42

  # environment wrapper clipping
  env:
    clip_actions: 1.0
  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [256,128,64]
      d2rl: False
      activation: elu
      initializer:
        name: default
        scale: 2
    rnn:
        name: gru
        units: 64
        layers: 1
        # before_mlp: False
        # layer_norm: True
  config:
    name: arl_robot_1_navigation
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    env_config:
      num_envs: 1024

    reward_shaper:
      # min_val: -1
      scale_value: 0.1

    normalize_advantage: True
    gamma: 0.98
    tau: 0.95
    ppo: True
    learning_rate: 1e-4
    lr_schedule: adaptive
    kl_threshold: 0.016
    save_best_after: 10
    score_to_win: 100000
    grad_norm: 1.0
    entropy_coef: 0
    truncate_grads: True
    e_clip: 0.2
    clip_value: False
    num_actors: 1024
    horizon_length: 32
    minibatch_size: 2048
    mini_epochs: 4
    critic_coef: 2
    normalize_input: True
    bounds_loss_coef: 0.0001
    max_epochs: 1500
    normalize_value: True
    use_diagnostics: True
    value_bootstrap: True
    #weight_decay: 0.0001
    use_smooth_clamp: False

    player:
      render: True
      deterministic: True
      games_num: 100000

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/drone_arl/navigation/config/arl_robot_1/agents/skrl_rough_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: False
  policy:
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: mlp
        input: OBSERVATIONS
        layers: [256, 128, 64]
        activations: elu
      - name: gru
        input: mlp
        type: GRU
        layers: [64]
        num_layers: 1
    output: ACTIONS
  value:
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: mlp
        input: OBSERVATIONS
        layers: [256, 128, 64]
        activations: elu
      - name: gru
        input: mlp
        type: GRU
        layers: [64]
        num_layers: 1
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 24
  learning_epochs: 5
  mini_batches: 4
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-03
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.01
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.005
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.6
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "arl_robot_1_navigation"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 36000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/drone_arl/track_position_state_based/config/arl_robot_1/agents/rl_games_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 42

  # environment wrapper clipping
  env:
    clip_actions: 1.0
  algo:
    name: a2c_continuous

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False
    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: True
    mlp:
      units: [256,128,64]
      d2rl: False
      activation: elu
      initializer:
        name: default
        scale: 2
    rnn:
        name: gru
        units: 64
        layers: 1
        # before_mlp: False
        # layer_norm: True
  config:
    env_name: rlgpu
    device: 'cuda:0'
    device_name: 'cuda:0'
    env_config:
      num_envs: 8192

    name: arl_robot_1_track_position_state_based
    reward_shaper:
      # min_val: -1
      scale_value: 0.1

    normalize_advantage: True
    gamma: 0.98
    tau: 0.95
    ppo: True
    learning_rate: 1e-4
    lr_schedule: adaptive
    kl_threshold: 0.016
    save_best_after: 10
    score_to_win: 100000
    grad_norm: 1.0
    entropy_coef: 0
    truncate_grads: True
    e_clip: 0.2
    clip_value: False
    num_actors: 1024
    horizon_length: 32
    minibatch_size: 2048
    mini_epochs: 4
    critic_coef: 2
    normalize_input: True
    bounds_loss_coef: 0.0001
    max_epochs: 1500
    normalize_value: True
    use_diagnostics: True
    value_bootstrap: True
    #weight_decay: 0.0001
    use_smooth_clamp: False

    player:
      render: True
      deterministic: True
      games_num: 100000

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/drone_arl/track_position_state_based/config/arl_robot_1/agents/skrl_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: False
  policy:
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: 0.0
    network:
      - name: mlp
        input: OBSERVATIONS
        layers: [256, 128, 64]
        activations: elu
      - name: gru
        input: mlp
        type: GRU
        layers: [64]
        num_layers: 1
    output: ACTIONS
  value:
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: mlp
        input: OBSERVATIONS
        layers: [256, 128, 64]
        activations: elu
      - name: gru
        input: mlp
        type: GRU
        layers: [64]
        num_layers: 1
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)


# PPO agent configuration (field names are from PPO_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/ppo.html
agent:
  class: PPO
  rollouts: 24
  learning_epochs: 5
  mini_batches: 4
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 1.0e-03
  learning_rate_scheduler: KLAdaptiveLR
  learning_rate_scheduler_kwargs:
    kl_threshold: 0.01
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 1.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.005
  value_loss_scale: 1.0
  kl_threshold: 0.0
  rewards_shaper_scale: 0.6
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "arl_robot_1_track_position_state_based"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 36000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/factory/agents/rl_games_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 0
  algo:
    name: a2c_continuous

  env:
    clip_actions: 1.0

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: False
    mlp:
      units: [512, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    rnn:
      name: lstm
      units: 1024
      layers: 2
      before_mlp: True
      concat_input: True
      layer_norm: True

  load_checkpoint: False
  load_path: ""

  config:
    name: Factory
    device: cuda:0
    env_name: rlgpu
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: 128
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.995
    tau: 0.95
    learning_rate: 1.0e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: 200
    save_best_after: 10
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0  # 0.0001  # 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 128
    minibatch_size: 512  # batch size = num_envs * horizon_length; minibatch_size = batch_size / num_minibatches
    mini_epochs: 4
    critic_coef: 2
    clip_value: True
    seq_length: 128
    bounds_loss_coef: 0.0001

    central_value_config:
      minibatch_size: 512
      mini_epochs: 4
      learning_rate: 1e-4
      lr_schedule: adaptive
      kl_threshold: 0.008
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        mlp:
          units: [512, 128, 64]
          activation: elu
          d2rl: False

          initializer:
            name: default
          regularizer:
            name: None

        rnn:
          name: lstm
          units: 1024
          layers: 2
          before_mlp: True
          concat_input: True
          layer_norm: True

    player:
      deterministic: False

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/forge/agents/rl_games_ppo_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 0
  algo:
    name: a2c_continuous

  env:
    clip_actions: 1.0

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: False
    mlp:
      units: [512, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    rnn:
      name: lstm
      units: 1024
      layers: 2
      before_mlp: True
      concat_input: True
      layer_norm: True

  load_checkpoint: False
  load_path: ""

  config:
    name: Forge
    device: cuda:0
    env_name: rlgpu
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: 128
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.995
    tau: 0.95
    learning_rate: 1.0e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: 200
    save_best_after: 10
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 128
    minibatch_size: 512  # batch size = num_envs * horizon_length; minibatch_size = batch_size / num_minibatches
    mini_epochs: 4
    critic_coef: 2
    clip_value: True
    seq_length: 128
    bounds_loss_coef: 0.0001

    central_value_config:
      minibatch_size: 512
      mini_epochs: 4
      learning_rate: 1e-4
      lr_schedule: adaptive
      kl_threshold: 0.008
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        mlp:
          units: [512, 128, 64]
          activation: elu
          d2rl: False

          initializer:
            name: default
          regularizer:
            name: None

        rnn:
          name: lstm
          units: 1024
          layers: 2
          before_mlp: True
          concat_input: True
          layer_norm: True

    player:
      deterministic: False

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/forge/agents/rl_games_ppo_cfg_nut_thread.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

params:
  seed: 0
  algo:
    name: a2c_continuous

  env:
    clip_actions: 1.0

  model:
    name: continuous_a2c_logstd

  network:
    name: actor_critic
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: default
        sigma_init:
          name: const_initializer
          val: 0
        fixed_sigma: False
    mlp:
      units: [512, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    rnn:
      name: lstm
      units: 1024
      layers: 2
      before_mlp: True
      concat_input: True
      layer_norm: True

  load_checkpoint: False
  load_path: ""

  config:
    name: Forge
    device: cuda:0
    env_name: rlgpu
    multi_gpu: False
    ppo: True
    mixed_precision: True
    normalize_input: True
    normalize_value: True
    value_bootstrap: True
    num_actors: 128
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.995
    tau: 0.95
    learning_rate: 1.0e-4
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 20000
    max_epochs: 200
    save_best_after: 10
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 256
    minibatch_size: 512  # batch size = num_envs * horizon_length; minibatch_size = batch_size / num_minibatches
    mini_epochs: 4
    critic_coef: 2
    clip_value: True
    seq_length: 128
    bounds_loss_coef: 0.0001

    central_value_config:
      minibatch_size: 512
      mini_epochs: 4
      learning_rate: 1e-4
      lr_schedule: adaptive
      kl_threshold: 0.008
      clip_value: True
      normalize_input: True
      truncate_grads: True

      network:
        name: actor_critic
        central_value: True

        mlp:
          units: [512, 128, 64]
          activation: elu
          d2rl: False

          initializer:
            name: default
          regularizer:
            name: None

        rnn:
          name: lstm
          units: 1024
          layers: 2
          before_mlp: True
          concat_input: True
          layer_norm: True

    player:
      deterministic: False

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/humanoid_amp/agents/skrl_dance_amp_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: True
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: -2.9
    fixed_log_std: True
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE
  discriminator:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)

# AMP memory (reference motion dataset)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
motion_dataset:
  class: RandomMemory
  memory_size: 200000

# AMP memory (preventing discriminator overfitting)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
reply_buffer:
  class: RandomMemory
  memory_size: 1000000


# AMP agent configuration (field names are from AMP_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/amp.html
agent:
  class: AMP
  rollouts: 16
  learning_epochs: 6
  mini_batches: 2
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-05
  learning_rate_scheduler: null
  learning_rate_scheduler_kwargs: null
  observation_preprocessor: RunningStandardScaler
  observation_preprocessor_kwargs: null
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  amp_observation_preprocessor: RunningStandardScaler
  amp_observation_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 0.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.5
  discriminator_loss_scale: 5.0
  amp_batch_size: 512
  task_reward_scale: 0.0
  style_reward_scale: 2.0
  discriminator_batch_size: 4096
  discriminator_logit_regularization_scale: 0.05
  discriminator_gradient_penalty_scale: 5.0
  discriminator_weight_decay_scale: 1.0e-04
  # rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "humanoid_amp_dance"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 80000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/humanoid_amp/agents/skrl_run_amp_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: True
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: -2.9
    fixed_log_std: True
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE
  discriminator:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)

# AMP memory (reference motion dataset)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
motion_dataset:
  class: RandomMemory
  memory_size: 200000

# AMP memory (preventing discriminator overfitting)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
reply_buffer:
  class: RandomMemory
  memory_size: 1000000


# AMP agent configuration (field names are from AMP_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/amp.html
agent:
  class: AMP
  rollouts: 16
  learning_epochs: 6
  mini_batches: 2
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-05
  learning_rate_scheduler: null
  learning_rate_scheduler_kwargs: null
  observation_preprocessor: RunningStandardScaler
  observation_preprocessor_kwargs: null
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  amp_observation_preprocessor: RunningStandardScaler
  amp_observation_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 0.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.5
  discriminator_loss_scale: 5.0
  amp_batch_size: 512
  task_reward_scale: 0.0
  style_reward_scale: 2.0
  discriminator_batch_size: 4096
  discriminator_logit_regularization_scale: 0.05
  discriminator_gradient_penalty_scale: 5.0
  discriminator_weight_decay_scale: 1.0e-04
  # rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "humanoid_amp_run"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 80000
  environment_info: log

```

### source/isaaclab_tasks/isaaclab_tasks/contrib/humanoid_amp/agents/skrl_walk_amp_cfg.yaml

```yaml
# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

seed: 42


# Models are instantiated using skrl's model instantiator utility
# https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html
models:
  separate: True
  policy:  # see gaussian_model parameters
    class: GaussianMixin
    clip_actions: False
    clip_log_std: True
    min_log_std: -20.0
    max_log_std: 2.0
    initial_log_std: -2.9
    fixed_log_std: True
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ACTIONS
  value:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE
  discriminator:  # see deterministic_model parameters
    class: DeterministicMixin
    clip_actions: False
    network:
      - name: net
        input: OBSERVATIONS
        layers: [1024, 512]
        activations: relu
    output: ONE


# Rollout memory
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
memory:
  class: RandomMemory
  memory_size: -1  # automatically determined (same as agent:rollouts)

# AMP memory (reference motion dataset)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
motion_dataset:
  class: RandomMemory
  memory_size: 200000

# AMP memory (preventing discriminator overfitting)
# https://skrl.readthedocs.io/en/latest/api/memories/random.html
reply_buffer:
  class: RandomMemory
  memory_size: 1000000


# AMP agent configuration (field names are from AMP_DEFAULT_CONFIG)
# https://skrl.readthedocs.io/en/latest/api/agents/amp.html
agent:
  class: AMP
  rollouts: 16
  learning_epochs: 6
  mini_batches: 2
  discount_factor: 0.99
  lambda: 0.95
  learning_rate: 5.0e-05
  learning_rate_scheduler: null
  learning_rate_scheduler_kwargs: null
  observation_preprocessor: RunningStandardScaler
  observation_preprocessor_kwargs: null
  state_preprocessor: null
  state_preprocessor_kwargs: null
  value_preprocessor: RunningStandardScaler
  value_preprocessor_kwargs: null
  amp_observation_preprocessor: RunningStandardScaler
  amp_observation_preprocessor_kwargs: null
  random_timesteps: 0
  learning_starts: 0
  grad_norm_clip: 0.0
  ratio_clip: 0.2
  value_clip: 0.2
  clip_predicted_values: True
  entropy_loss_scale: 0.0
  value_loss_scale: 2.5
  discriminator_loss_scale: 5.0
  amp_batch_size: 512
  task_reward_scale: 0.0
  style_reward_scale: 2.0
  discriminator_batch_size: 4096
  discriminator_logit_regularization_scale: 0.05
  discriminator_gradient_penalty_scale: 5.0
  discriminator_weight_decay_scale: 1.0e-04
  # rewards_shaper_scale: 1.0
  time_limit_bootstrap: False
  # logging and checkpoint
  experiment:
    directory: "humanoid_amp_walk"
    experiment_name: ""
    write_interval: auto
    checkpoint_interval: auto


# Sequential trainer
# https://skrl.readthedocs.io/en/latest/api/trainers/sequential.html
trainer:
  class: SequentialTrainer
  timesteps: 80000
  environment_info: log

```

## Python signatures and reward/observation bodies (1251 files)


### .github/actions/_lib/setup-docker-config/strip_registry_auth.py

```
"""Drop the stored credential for one image's registry from a docker config.

A registry can refuse a credential scoped to another organization a pull token
for a public repository instead of downgrading the request to anonymous, which
makes a public base image unreadable. Removing just that registry's entry lets
the pull proceed anonymously while every other registry in the same config
keeps working.

Usage: strip_registry_auth.py <config.json> <image-ref>
Exits 0 when a credential was dropped, 3 when nothing matched."""
def registry_host(image_ref)
def _normalize(auth_key)
def main(argv)
```

### .github/actions/_lib/test_registry_credential_fallback.py

```
"""Tests for the registry-scoped docker credential fallback.

Covers the helper that drops one registry's stored credential and the composite
action's guards around it, plus the base image digest resolution that feeds the
dependency-cache key. The action bodies are extracted from their action.yml and
run under bash against stubbed executables, so no registry access is needed."""
def _load_helper()
def _step_body(action_path)
def _write_config(path, registries)
def _auths(path)
def _write_stub_docker(bin_dir, body)
def _run_setup(tmp_path, base_image_ref, stub)
def test_public_nvcr_drops_only_that_registry(tmp_path)
def test_non_nvcr_reference_is_left_alone(tmp_path)
def test_readable_image_keeps_credentials(tmp_path)
def test_transient_failure_keeps_credentials(tmp_path)
def test_transient_anonymous_failure_is_retried(tmp_path)
def test_unowned_config_is_never_modified(tmp_path)
def test_already_checked_reference_is_not_probed_again(tmp_path)
def test_registry_host_canonicalization()
def test_helper_reports_when_nothing_matched(tmp_path)
def test_helper_also_clears_credential_helpers(tmp_path)
def _run_hash(tmp_path, image, version, stub)
def test_digest_pinned_tag_skips_the_network(tmp_path)
def test_malformed_digest_pin_fails(tmp_path)
def test_authorization_refusal_fails_without_retrying(tmp_path)
def test_truncated_digest_is_rejected(tmp_path)
def test_trailing_output_after_a_digest_is_rejected(tmp_path)
def test_successful_read_ignores_stderr_noise(tmp_path)
```

### .github/actions/multi-gpu/aggregate_test_summary.py

```
"""Aggregate per-shard JUnit XML reports from the multi-GPU pytest lane.

Reads ``RUNTIME_DIR`` (the host launcher's work-queue root, holding
``queue/done/<shard>/<slug>``) and the ``tests/test-reports-*.xml`` JUnit files,
then prints a per-file + per-shard table to stdout and, when
``GITHUB_STEP_SUMMARY`` is set, writes the same content as markdown so it
renders at the top of the run page."""
def unslug(name)
def fmt_row(cols, widths)
```

### .github/actions/multi-gpu/mgpu_shard_select.py

```
"""pytest plugin: select which tests a non-default GPU shard runs.

Loaded only by the multi-GPU lane: ``tools/conftest.py`` injects it via
``-p mgpu_shard_select`` into each per-file pytest subprocess (and prepends this
directory to ``PYTHONPATH`` so it is importable). It lives next to the lane
scripts rather than as a repo-root ``conftest.py`` so it only affects the lane.

Signal: ``ISAACLAB_TEST_DEVICES`` -- the runtime device mask. This is the SAME
env var ``isaaclab.test.utils.devices.test_devices()`` reads to decide a test's
device parametrization, so this plugin's keep/drop decision agrees"""
def _position(device)
def _active(position, mask)
def _shard_mask()
def pytest_collection_modifyitems(config, items)
def pytest_sessionfinish(session, exitstatus)
```

### .github/actions/run-package-tests/test_cleanup_docker_storage.py

```
"""Tests for CI Docker storage cleanup helpers."""
def _write_fake_df(bin_dir, first_usage, final_usage, failed_path, fallback_path)
def _write_fake_docker(bin_dir, docker_root_dir)
def _run_cleanup(tmp_path, first_usage, final_usage, failed_path, docker_root_dir)
def test_cleanup_uses_aggressive_pruning_when_docker_storage_exceeds_threshold(tmp_path)
def test_cleanup_keeps_conservative_image_pruning_below_threshold(tmp_path)
def test_cleanup_prunes_unused_volumes_above_threshold(tmp_path)
def test_cleanup_prunes_unused_volumes_below_threshold(tmp_path)
def test_cleanup_prunes_unused_volumes_after_stopped_containers_are_removed(tmp_path)
def test_cleanup_prunes_unused_volumes_when_usage_cannot_be_measured(tmp_path)
def test_cleanup_fails_early_when_aggressive_pruning_cannot_recover_space(tmp_path)
def test_cleanup_uses_docker_root_dir_when_default_storage_path_is_unavailable(tmp_path)
def test_cleanup_fails_early_when_docker_storage_usage_cannot_be_measured(tmp_path)
def test_run_package_tests_prepares_docker_space_before_image_pull()
```

### .github/actions/run-package-tests/warp_cache_inventory.py

```
"""Report what a Warp kernel cache directory actually contains.

Runs on the runner against the host cache directory. Reporting only: it never
fails a job and never gates publication. The point is to replace guesses about
cache size and retention with measurements - module counts, artifact mix, and
the spread of GPU targets a shared collection has accumulated.

Usage:
    warp_cache_inventory.py <cache-dir> [label]
    warp_cache_inventory.py <cache-dir> --fingerprint"""
def fingerprint(root)
def main()
```

### .github/actions/run-tests/junit_summary.py

```
"""Parse a JUnit XML report and print a markdown summary (for $GITHUB_STEP_SUMMARY)."""
def safe_float(val, default)
def sanitize_msg(msg, max_len)
def fmt_name(name)
```

### .github/actions/upload-omni-github-test-results/junit_to_omni_github_results.py

```
"""Convert a JUnit XML report into the omni-github test-result artifact format."""
def _local_name(tag)
def _iter_testcases(root)
def _first_child(testcase, names)
def _duration_seconds(element)
def _test_id(testcase)
def _testcase_markers(testcase)
def _short_message(element)
def _convert_testcase(testcase, test_type, group_id, retries, log_paths)
def convert_junit(junit_file, output_dir, test_tool_id, test_type, app_platform, app_config, group_name, junit_log_url, comparison_images_url, retries)
def parse_args()
def main()
```

### .github/actions/upload-omni-github-test-results/test_junit_to_omni_github_results.py

```
"""Tests for the omni-github JUnit result converter."""
def _load_converter_module()
def _load_rows(output_dir)
def test_convert_junit_populates_github_metadata_and_failure_details(tmp_path)
def test_convert_junit_marks_xfail_as_unreliable(tmp_path)
def test_convert_junit_marks_crashes_and_timeouts(tmp_path)
def test_convert_junit_adds_log_paths_for_junit_and_comparison_artifacts(tmp_path)
def test_convert_junit_appends_markers_to_test_type_with_separator(tmp_path)
```

### .github/actions/warp-cache-key/collection_id.py

```
"""Print the Warp cache collection identifier for the current lockfile.

The Warp kernel cache is produced by Warp, Newton, MuJoCo Warp, and Isaac Lab's
own kernels. Only the first three belong in the cache key: Warp's module hash
already separates changed Isaac Lab source while leaving unchanged modules
reusable, so keying on Isaac Lab source would discard hits for no benefit.

GPU architecture is deliberately absent. Warp puts the target in the artifact
filename (``<module>.sm120.ptx``), so variants for several architectures coexist
in one module directory and a shared collection accumulates wh"""
def read_packages(text)
def main()
```

### docker/test/test_carb_env_shim.py

```
def test_dockerfiles_run_shared_carb_env_shim_installer(dockerfile_name)
def test_carb_env_shim_installer_copies_shim_and_preserves_preloads(tmp_path, preload_terminator)
def test_dependency_cache_hash_tracks_carb_env_shim_installer()
```

### scripts/benchmarks/test/test_training_adapters.py

```
"""Focused tests for RL-library benchmark adapter behavior."""
def test_training_dispatches_libraries_to_explicitly_named_adapters(library)
def test_play_dispatches_libraries_to_explicitly_named_adapters(library)
def test_play_adapter_help_does_not_require_task(adapter)
def test_rsl_rl_disables_code_state_capture()
def test_sb3_iteration_time_includes_policy_update(monkeypatch)
def test_skrl_reward_uses_episode_return_tracking(monkeypatch)
def test_skrl_parser_rejects_unimplemented_modes()
def test_skrl_parsers_leave_algorithm_to_canonical_config()

```python
def test_skrl_reward_uses_episode_return_tracking(monkeypatch: pytest.MonkeyPatch):
    """Test that SKRL records its canonical total-reward metric at rollout boundaries."""
    from skrl.trainers.torch import SequentialTrainer

    class FakeEnv:
        num_agents = 1

        def step(self, actions):
            return None, torch.tensor([1.0]), None, None, {}

    class FakeAgent:
        cfg = SimpleNamespace(rollouts=2)

        def __init__(self):
            self.tracking_data = {}

        def post_interaction(self, *, timestep: int, timesteps: int) -> None:
            self.tracking_data.clear()

    def run_two_steps(trainer) -> None:
        for timestep in range(2):
            trainer.env.step(None)
            trainer.agents.tracking_data = {
                "Reward / Total reward (mean)": [10.0, 20.0],
                "Episode / Total timesteps (mean)": [5.0, 7.0],
            }
            trainer.agents.post_interaction(timestep=timestep, timesteps=2)

    monkeypatch.setattr(SequentialTrainer, "train", run_two_steps)
    timestamps = iter([1_000_000_000, 3_000_000_000, 6_000_000_000, 6_000_000_000])
    monkeypatch.setattr(train_skrl.time, "perf_counter_ns", lambda: next(timestamps))
    trainer_class = train_skrl._build_benchmark_trainer_class()
    trainer = trainer_class.__new__(trainer_class)
    trainer.env = FakeEnv()
    trainer.agents = FakeAgent()
    trainer.cfg = SimpleNamespace(timesteps=2)
    trainer.num_simultaneous_agents = 1
    trainer.collection_times_s = []
    trainer.iter_times_s = []
    trainer.iter_rewards = []
    trainer.iter_ep_lengths = []

    trainer.train()

    assert trainer.collection_times_s == [2.0]
    assert trainer.iter_times_s == [5.0]
    assert trainer.iter_rewards == [15.0]
```
```

### scripts/benchmarks/training.py

```
"""Supported launcher for the library-owned training benchmark entrypoint."""
```

### scripts/benchmarks/training_multigpu.py

```
"""Supported launcher for the multi-GPU training benchmark."""
```

### scripts/demos/hands.py

```
"""This script demonstrates different dexterous hands.

.. code-block:: bash

    # Usage with default PhysX physics and default kit visualizer.
    uv run python scripts/demos/hands.py

    # Usage with Newton visualizer and default PhysX physics.
    uv run python scripts/demos/hands.py --visualizer newton

    # Usage with Newton (MJWarp) physics and default kit visualizer.
    uv run python scripts/demos/hands.py --physics newton_mjwarp

    # Usage with Newton visualizer and Newton (MJWarp) physics.
    uv run python scripts/demos/hands.py --visualizer newton --physics newton_mjwarp"""
def define_origins(num_origins, spacing)
def design_scene()
def run_simulator(sim, entities, origins)
def main()
```

### scripts/environments/export_IODescriptors.py

```
"""Script to an environment with random action agent."""
def main()
```

### scripts/environments/list_envs.py

```
"""Script to print all the available environments in Isaac Lab.

The script iterates over all registered environments and stores the details in a table.
It prints the name of the environment, the entry point and the config file.

All the environments are registered in the `isaaclab_tasks` extension. They start
with `Isaac` in their name."""
def _format_presets(preset_map)
def main()
```

### scripts/environments/random_agent.py

```
"""Random-action agent executable for Isaac Lab environments."""
def main(argv)
```

### scripts/environments/state_machine/lift_cube_sm.py

```
"""Script to run an environment with a pick and lift state machine.

The state machine is implemented in the kernel function `infer_state_machine`.
It uses the `warp` library to run the state machine in parallel on the GPU.

.. code-block:: bash

    uv run python scripts/environments/state_machine/lift_cube_sm.py --num_envs 32 --viz kit"""
class GripperState()
    """States for the gripper."""
class PickSmState()
    """States for the pick state machine."""
class PickSmWaitTime()
    """Additional wait times (in s) for states for before switching."""
def distance_below_threshold(current_pos, desired_pos, threshold)
def infer_state_machine(dt, sm_state, sm_wait_time, ee_pose, object_pose, des_object_pose, des_ee_pose, gripper_state, offset, position_threshold)
class PickAndLiftSm()
    """A simple state machine in a robot's task space to pick and lift an object.

The state machine is implemented as a warp kernel. It takes in the current state of
the robot's end-effector and the object, and outputs the desired state of the robot's
end-effector and the gripper. The state machine is imp"""
    def __init__(self, dt, num_envs, device, position_threshold)
    def reset_idx(self, env_ids)
    def compute(self, ee_pose, object_pose, des_object_pose)
def main()
```

### scripts/environments/state_machine/lift_franka_soft.py

```
"""Script to demonstrate lifting a deformable object with a robotic arm.

The state machine is implemented in the kernel function `infer_state_machine`.
It uses the `warp` library to run the state machine in parallel on the GPU.

.. code-block:: bash

    # Kitless run with the Newton OpenGL viewer (default).
    uv run python scripts/environments/state_machine/lift_franka_soft.py

    # Headless.
    uv run python scripts/environments/state_machine/lift_franka_soft.py --viz none"""
class GripperState()
    """States for the gripper."""
class PickSmState()
    """States for the pick state machine."""
def distance_below_threshold(current_pos, desired_pos, threshold)
def infer_state_machine(dt, sm_state, sm_wait_time, ee_pose, object_pose, des_object_pose, des_ee_pose, gripper_state, offset, position_threshold)
class PickSmWaitTime()
    """Additional wait times (in s) for states for before switching.

Wait times are generous because the low-PD Franka takes a while to settle on each IK target."""
class PickAndLiftSm()
    """A simple state machine in a robot's task space to pick and lift an object.

The state machine is implemented as a warp kernel. It takes in the current state of
the robot's end-effector and the object, and outputs the desired state of the robot's
end-effector and the gripper. The state machine is imp"""
    def __init__(self, dt, num_envs, device, position_threshold)
    def reset_idx(self, env_ids)
    def compute(self, ee_pose, object_pose, des_object_pose)
def main()
```

### scripts/environments/state_machine/open_cabinet_sm.py

```
"""Script to run an environment with a cabinet opening state machine.

The state machine is implemented in the kernel function `infer_state_machine`.
It uses the `warp` library to run the state machine in parallel on the GPU.

.. code-block:: bash

    uv run python scripts/environments/state_machine/open_cabinet_sm.py --num_envs 32 --viz kit"""
class GripperState()
    """States for the gripper."""
class OpenDrawerSmState()
    """States for the cabinet drawer opening state machine."""
class OpenDrawerSmWaitTime()
    """Additional wait times (in s) for states for before switching."""
def distance_below_threshold(current_pos, desired_pos, threshold)
def infer_state_machine(dt, sm_state, sm_wait_time, ee_pose, handle_pose, des_ee_pose, gripper_state, handle_approach_offset, handle_grasp_offset, drawer_opening_rate, position_threshold)
class OpenDrawerSm()
    """A simple state machine in a robot's task space to open a drawer in the cabinet.

The state machine is implemented as a warp kernel. It takes in the current state of
the robot's end-effector and the object, and outputs the desired state of the robot's
end-effector and the gripper. The state machine i"""
    def __init__(self, dt, num_envs, device, position_threshold)
    def reset_idx(self, env_ids)
    def compute(self, ee_pose, handle_pose)
def main()
```

### scripts/environments/teleoperation/teleop_replay_agent.py

```
"""CI/automation entry point for replaying captured Isaac Teleop sessions.

This is the non-interactive counterpart to ``teleop_se3_agent.py``. It builds
a teleop environment, attaches an :class:`~isaaclab_teleop.IsaacTeleopDevice`
configured in :class:`isacteleop.teleop_session_manager.SessionMode.REPLAY`,
and pumps the simulation loop until the recorded operator presses STOP (or
``--max_replay_duration_s`` elapses, or the simulator is closed). The user-journey
teleop script remains ``teleop_se3_agent.py``.

Inputs:
    ``--replay_file`` is an MCAP capture produced by Isaac Teleop's
    ``McapRe"""
class _RunStats()
    """Per-replay performance + outcome record.

``active_frame_times_ms`` is the per-rendered-frame series: wall-clock
deltas between successive :meth:`SimulationContext.render` calls
produced from inside ``env.step`` during the active window
(post-START, pre-terminator). Pre-START render-only frames, war"""
    def to_dict(self, run_index)
def _compute_frame_stats(samples_ms)
def _compute_fps_stats(samples_ms)
class GpuStatsProvider(Protocol)
    """Per-run GPU telemetry source.

Renderer-agnostic interface for sampling GPU state during a
replay. Implementations are expected to be cheap on
:meth:`sample` (<<1 ms; the agent calls it once per active
iteration in the hot path) and to return a JSON-serializable
dict from :meth:`summary` matching th"""
    def sample(self)
    def summary(self)
class NvmlGpuStatsProvider()
    """NVML-backed :class:`GpuStatsProvider`.

Snapshots GPU utilization (%) and used memory (MB) for one
device per :meth:`sample` call via ``pynvml``. Per-call cost is
<100 us so per-frame sampling is fine at any realistic frame
rate. Soft-fails when ``pynvml`` is missing or initialization
fails (no NVID"""
    def __init__(self, device_index)
    def sample(self)
    def summary(self)
def _extract_env_perf_cfg(env_cfg)
def _assert_run_measured(stats, run_index)
def _build_report(args, env_cfg, all_runs)
def _aggregate_runs(run_dicts)
def _print_stdout_summary(report)
def _write_json_report(path, report)
def _exit_code_for_outcomes(all_runs)
def _resolve_cloudxr_env(value)
def _maybe_launch_cloudxr(cloudxr_env_path, auto_launch)
def _rtx_rendering_requested(args)
def _ensure_replicator_loaded()
def _prepare_env_cfg(task, num_envs, device, apply_rtx_settings, overrides)
def _handle_reset(env, teleop_interface)
def _process_success_condition(env, success_term, success_step_count, num_success_steps)
def _wait_for_stage_load(simulation_app, max_wait_s)
def _run_single_replay(env, isaac_teleop_cfg, success_term, run_index, total_runs)
def main()
```

### scripts/environments/teleoperation/teleop_se3_agent.py

```
"""Script to run teleoperation with Isaac Lab manipulation environments.

Supports multiple input devices (e.g., keyboard, spacemouse, gamepad) and devices
configured within the environment (including OpenXR-based hand tracking or motion
controllers).

This script supports two teleoperation stacks:
1. Native Isaac Lab teleop stack (via teleop_devices in env_cfg)
2. IsaacTeleop-based stack (via isaac_teleop in env_cfg)

The script automatically detects which stack to use based on the environment config."""
def _resolve_cloudxr_env(value, xr_enabled)
def _rtx_rendering_requested(args)
def _ensure_replicator_loaded()
def _create_builtin_device(device_name, sensitivity)
def _make_haptic_io(env, teleop_interface, env_cfg, use_isaac_teleop)
def _make_control_keyboard(teleop_interface, use_isaac_teleop, has_window)
def main()
```

### scripts/environments/zero_agent.py

```
"""Zero-action agent executable for Isaac Lab environments."""
def main(argv)
```

### scripts/imitation_learning/locomanipulation_sdg/gr00t/data_config.py

```
class BaseDataConfig(ABC)
    """Base class for GR00T data configurations defining modalities and transforms."""
    def modality_config(self)
    def transform(self)
def import_external_data_config(data_config_str)
def load_data_config(data_config_str)
class G1LocomanipulationSDGDataConfig(BaseDataConfig)
    """Data config for G1 locomanipulation SDG (video, state, action; no language)."""
    def modality_config(self)
    def transform(self)
```

### scripts/imitation_learning/locomanipulation_sdg/gr00t/policy.py

```
class Policy()
    """Wrapper around GR00T policy for G1 locomanipulation SDG."""
    def __init__(self, model_path, embodiment_tag)
```

### scripts/imitation_learning/locomanipulation_sdg/gr00t/rollout_policy.py

```
"""Script to replay demonstrations with Isaac Lab environments."""
def _clone_state(state)
def build_initial_state_for_replay(env, input_episode_data)
def _convert_pose_quat(pose, to_fmt)
def _convert_action_pose_quats_to_env(action, policy_quat_format)
def setup_navigation_scene(env, input_episode_data, approach_distance, randomize_placement)
def build_model_input(env, base_goal, policy_quat_format)
def eval_policy(env, policy, input_episode_data, randomize_placement, policy_quat_format)
```

### scripts/imitation_learning/robomimic/train.py

```
"""The main entry point for training policies from pre-collected data.

This script loads dataset(s), creates a model based on the algorithm specified,
and trains the model. It supports training on various environments with multiple
algorithms from robomimic.

Args:
    algo: Name of the algorithm to run.
    task: Name of the environment.
    name: If provided, override the experiment name defined in the config.
    dataset: If provided, override the dataset path defined in the config.
    log_dir: Directory to save logs.
    normalize_training_actions: Whether to normalize actions in the traini"""
def normalize_hdf5_actions(config, log_dir)
def train(config, device, log_dir, ckpt_dir, video_dir)
def main(args)
```

### scripts/reinforcement_learning/ray/hyperparameter_tuning/vision_cartpole_cfg.py

```
class CartpoleRGBNoTuneJobCfg(CameraJobCfg)
    def __init__(self, cfg)
class CartpoleRGBCNNOnlyJobCfg(CameraJobCfg)
    def __init__(self, cfg)
class CartpoleRGBJobCfg(CameraJobCfg)
    def __init__(self, cfg)
class CartpoleResNetJobCfg(ResNetCameraJob)
    def __init__(self, cfg)
class CartpoleTheiaJobCfg(TheiaCameraJob)
    def __init__(self, cfg)
class CustomCartpoleProgressReporter(CLIReporter)
    def __init__(self)
class CartpoleEarlyStopper(Stopper)
    def __init__(self)
    def __call__(self, trial_id, result)
    def stop_all(self)
```

### scripts/reinforcement_learning/ray/hyperparameter_tuning/vision_cfg.py

```
class CameraJobCfg(JobCfg)
    """In order to be compatible with :meth: invoke_tuning_run, and
:class:IsaacLabTuneTrainable , configurations should
be in a similar format to this class. This class can vary env count/horizon length,
CNN structure, and MLP structure. Broad possible ranges are set, the specific values
that work can be """
    def _get_batch_size_divisors(batch_size, min_size)
    def __init__(self, cfg, vary_env_count, vary_cnn, vary_mlp)
class ResNetCameraJob(CameraJobCfg)
    """Try different ResNet sizes."""
    def __init__(self, cfg)
class TheiaCameraJob(CameraJobCfg)
    """Try different Theia sizes."""
    def __init__(self, cfg)
```

### scripts/reinforcement_learning/ray/task_runner.py

```
"""This script dispatches one or more user-defined Python tasks to workers in a Ray cluster.
Each task, along with its resource requirements and execution parameters, is specified in a YAML configuration file.
Users may define the number of CPUs, GPUs, and the amount of memory to allocate per task via the config file.

Key features:
-------------
- Fine-grained, per-task resource management via config fields (`num_gpus`, `num_cpus`, `memory`).
- Parallel execution of multiple tasks using available resources across the Ray cluster.
- Option to specify node affinity for tasks, e.g., by hostname, no"""
def safe_eval_arithmetic(expr)
def parse_args()
def parse_task_resource(task)
def run_tasks(tasks, args, runtime_env, concurrent)
def main()
```

### scripts/reinforcement_learning/train.py

```
"""Unified training executable for Isaac Lab reinforcement learning workflows."""
def main(argv)
```

### scripts/reinforcement_learning/train_multigpu.py

```
"""Multi-GPU training executable for Isaac Lab reinforcement learning workflows."""
def main(argv)
```

### scripts/tools/test/test_train_and_publish_checkpoints.py

```
"""Tests for the pretrained-checkpoint training utility."""
def test_cartpole_feature_presets_are_in_pretrained_checkpoint_matrix()
def test_checkpoint_preset_metadata_references_registered_variants()
def test_build_core_jobs_skips_unsupported_preset_without_normalizing_default(monkeypatch)
def test_job_commands_use_uv_run_isaaclab()
def test_build_core_jobs_includes_declared_checkpoint_presets(monkeypatch)
def test_select_physics_variants_uses_concrete_isaac_sim_physx()
def test_select_physics_variants_includes_franka_osc_newton_mjwarp()
def test_select_physics_variants_selects_coupled_newton_preset()
def test_select_physics_variants_does_not_fall_back_to_automatic_physx()
def test_legacy_job_experiment_name_preserves_task_name()
def test_legacy_collection_preserves_task_directory(tmp_path)
def test_publish_uses_collected_checkpoint_without_training_logs(tmp_path, capsys)
```

### scripts/tools/train_and_publish_checkpoints.py

```
"""Train, collect, review, and publish pretrained Isaac Lab checkpoints.

The core-task workflow selects RSL-RL when it is registered, falls back to
RL-Games, and uses SKRL MAPPO for multi-agent environments. Backend-aware
checkpoints are collected into one subdirectory per RL library:

.. code-block:: text

    logs/pretrained_checkpoints/
    ├── rl_games/
    ├── rsl_rl/
    └── skrl/

Each checkpoint is named
``<task_name>[_<preset_names>]_<physics_backend>_<render_backend>_<rl_library><extension>``.
State-only tasks use ``none`` as the render backend because their policies do
not depend on r"""
class CheckpointJob()
    """One workflow, task, preset, physics, and renderer training combination."""
    def job_id(self)
    def experiment_name(self)
    def preset_args(self)
def _create_parser()
def _parse_backend_list(value, supported, option)
def _is_core_task(task_spec)
def _select_workflow(task_spec, env_cfg)
def _select_physics_variants(task_name, variants, default_backend, requested_backends)
def _resolve_physics_backend(task_name, physics_selector, default_backend)
def _select_render_variants(variants, requested_backends)
def _build_core_jobs(args)
def _build_legacy_jobs()
def _filter_jobs(jobs, args)
def _training_command(job, args, smoke)
def _play_command(job, args, checkpoint_path)
def _run_command(command, dry_run)
def _has_training_job_completed(job)
def _mark_training_job_completed(job)
def train_job(job, args, smoke)
def collect_pretrained_checkpoint(job, output_dir, dry_run)
def review_pretrained_checkpoint(job, args)
def publish_pretrained_checkpoint(job, args)
def _summary_row(job, output_dir)
def _get_collected_checkpoint_path(job, output_dir)
def main(argv)
```

### scripts/tutorials/00_sim/create_empty.py

```
"""This script demonstrates how to create a simple stage in Isaac Sim.

.. code-block:: bash

    # Usage
    uv run python scripts/tutorials/00_sim/create_empty.py"""
def main()
```

### scripts/tutorials/00_sim/launch_app.py

```
"""This script demonstrates how to run IsaacSim via the AppLauncher

.. code-block:: bash

    # Usage
    uv run python scripts/tutorials/00_sim/launch_app.py"""
def design_scene()
def main()
```

### scripts/tutorials/00_sim/log_time.py

```
"""This script demonstrates how to generate log outputs while the simulation plays.
It accompanies the tutorial on docker usage.

.. code-block:: bash

    # Usage
    uv run python scripts/tutorials/00_sim/log_time.py"""
def main()
```

### scripts/tutorials/00_sim/spawn_prims.py

```
"""This script demonstrates how to spawn prims into the scene.

.. code-block:: bash

    # Usage
    uv run python scripts/tutorials/00_sim/spawn_prims.py"""
def design_scene()
def main()
```

### scripts/tutorials/03_envs/create_cartpole_base_env.py

```
"""This script demonstrates how to create a simple environment with a cartpole. It combines the concepts of
scene, action, observation and event managers to create an environment.

.. code-block:: bash

    uv run python scripts/tutorials/03_envs/create_cartpole_base_env.py --num_envs 32"""
class ActionsCfg()
    """Action specifications for the environment."""
class ObservationsCfg()
    """Observation specifications for the environment."""
class EventCfg()
    """Configuration for events."""
class CartpoleEnvCfg(ManagerBasedEnvCfg)
    """Configuration for the cartpole environment."""
    def __post_init__(self)
def main()
```

### scripts/tutorials/03_envs/create_cube_base_env.py

```
"""This script creates a simple environment with a floating cube. The cube is controlled by a PD
controller to track an arbitrary target position.

While going through this tutorial, we recommend you to pay attention to how a custom action term
is defined. The action term is responsible for processing the raw actions and applying them to the
scene entities.

We also define an event term called 'randomize_scale' that randomizes the scale of
the cube. This event term has the mode 'prestartup', which means that it is applied on the USD stage
before the simulation starts. Additionally, the flag 'repl"""
class CubeActionTerm(ActionTerm)
    """Simple action term that implements a PD controller to track a target position.

The action term is applied to the cube asset. It involves two steps:

1. **Process the raw actions**: Typically, this includes any transformations of the raw actions
   that are required to map them to the desired space."""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def process_actions(self, actions)
    def apply_actions(self)
class CubeActionTermCfg(ActionTermCfg)
    """Configuration for the cube action term."""
def base_position(env, asset_cfg)
class MySceneCfg(InteractiveSceneCfg)
    """Example scene configuration.

The scene comprises of a ground plane, light source and floating cubes (gravity disabled)."""
class ActionsCfg()
    """Action specifications for the MDP."""
class ObservationsCfg()
    """Observation specifications for the MDP."""
class EventCfg()
    """Configuration for events."""
class CubeEnvCfg(ManagerBasedEnvCfg)
    """Configuration for the locomotion velocity-tracking environment."""
    def __post_init__(self)
def main()
```

### scripts/tutorials/03_envs/create_quadruped_base_env.py

```
"""This script demonstrates the environment for a quadruped robot with height-scan sensor.

In this example, we use a locomotion policy to control the robot. The robot is commanded to
move forward at a constant velocity. The height-scan sensor is used to detect the height of
the terrain.

.. code-block:: bash

    # Run the script
    uv run python scripts/tutorials/03_envs/create_quadruped_base_env.py --num_envs 32"""
def constant_commands(env)
class MySceneCfg(InteractiveSceneCfg)
    """Example scene configuration."""
class ActionsCfg()
    """Action specifications for the MDP."""
class ObservationsCfg()
    """Observation specifications for the MDP."""
class EventCfg()
    """Configuration for events."""
class QuadrupedEnvCfg(ManagerBasedEnvCfg)
    """Configuration for the locomotion velocity-tracking environment."""
    def __post_init__(self)
def main()
```

### scripts/tutorials/03_envs/policy_inference_in_usd.py

```
"""This script demonstrates policy inference in a prebuilt USD environment.

In this example, we use a locomotion policy to control the H1 robot. The robot was trained
using Isaac-Velocity-Rough-H1. The robot is commanded to move forward at a constant velocity.

.. code-block:: bash

    # Run the script
    uv run python scripts/tutorials/03_envs/policy_inference_in_usd.py --checkpoint /path/to/jit/checkpoint.pt"""
def main()
```

### scripts/tutorials/03_envs/run_cartpole_rl_env.py

```
"""This script demonstrates how to run the RL environment for the cartpole balancing task.

.. code-block:: bash

    uv run python scripts/tutorials/03_envs/run_cartpole_rl_env.py --num_envs 32

Trailing ``key=value`` arguments (e.g. ``physics=isaacsim_physx``) are forwarded as Hydra-style
overrides to the task configuration; see :func:`~isaaclab_tasks.utils.parse_env_cfg`."""
def main()
```

### scripts/tutorials/06_deploy/anymal_c_env.py

```
class AnymalCEnv(DirectRLEnv)
    def __init__(self, cfg, render_mode)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_observations(self)
    def _get_rewards(self)
    def _get_dones(self)
    def _reset_idx(self, env_ids)

```python
def _get_observations(self) -> dict:
        self._previous_actions = self._actions.clone()
        height_data = None
        if isinstance(self.cfg, AnymalCRoughEnvCfg):
            height_data = (
                self._height_scanner.data.pos_w.torch[:, 2].unsqueeze(1)
                - self._height_scanner.data.ray_hits_w.torch[..., 2]
                - 0.5
            ).clip(-1.0, 1.0)
        # start LEAPP annotations for inputs
        root_lin_vel_b = annotate.input_tensors(self.spec.id, {"root_lin_vel_b": self._robot.data.root_lin_vel_b.torch})
        root_ang_vel_b = annotate.input_tensors(self.spec.id, {"root_ang_vel_b": self._robot.data.root_ang_vel_b.torch})
        projected_gravity_b = annotate.input_tensors(
            self.spec.id, {"projected_gravity_b": self._robot.data.projected_gravity_b.torch}
        )
        commands = annotate.input_tensors(self.spec.id, {"commands": self._commands})
        joint_pos = annotate.input_tensors(self.spec.id, {"joint_pos": self._robot.data.joint_pos.torch})
        default_joint_pos = annotate.input_tensors(
            self.spec.id, {"default_joint_pos": self._robot.data.default_joint_pos.torch}
        )
        joint_vel = annotate.input_tensors(self.spec.id, {"joint_vel": self._robot.data.joint_vel.torch})
        if height_data is not None:
            height_data = annotate.input_tensors(self.spec.id, {"height_data": height_data})
        previous_actions = annotate.state_tensors(self.spec.id, {"previous_actions": self._actions})
        # end LEAPP annotations for inputs

        obs = torch.cat(
            [
                tensor
                for tensor in (
                    root_lin_vel_b,
                    root_ang_vel_b,
                    projected_gravity_b,
                    commands,
                    joint_pos - default_joint_pos,
                    joint_vel,
                    height_data,
                    previous_actions,
                )
                if tensor is not None
            ],
            dim=-1,
        )
        observations = {"policy": obs}
        return observations
```

```python
def _get_rewards(self) -> torch.Tensor:
        lin_vel_error = torch.sum(
            torch.square(self._commands[:, :2] - self._robot.data.root_lin_vel_b.torch[:, :2]), dim=1
        )
        lin_vel_error_mapped = torch.exp(-lin_vel_error / 0.25)
        yaw_rate_error = torch.square(self._commands[:, 2] - self._robot.data.root_ang_vel_b.torch[:, 2])
        yaw_rate_error_mapped = torch.exp(-yaw_rate_error / 0.25)
        z_vel_error = torch.square(self._robot.data.root_lin_vel_b.torch[:, 2])
        ang_vel_error = torch.sum(torch.square(self._robot.data.root_ang_vel_b.torch[:, :2]), dim=1)
        joint_torques = torch.sum(torch.square(self._robot.actuators.applied_effort.torch), dim=1)
        joint_accel = torch.sum(torch.square(self._robot.data.joint_acc.torch), dim=1)
        action_rate = torch.sum(torch.square(self._actions - self._previous_actions), dim=1)
        first_contact = self._contact_sensor.compute_first_contact(self.step_dt).torch[:, self._feet_ids]
        last_air_time = self._contact_sensor.data.last_air_time.torch[:, self._feet_ids]
        air_time = torch.sum((last_air_time - 0.5) * first_contact, dim=1) * (
            torch.linalg.norm(self._commands[:, :2], dim=1) > 0.1
        )
        net_contact_forces = self._contact_sensor.data.net_normal_forces_w_history.torch
        is_contact = (
            torch.max(torch.linalg.norm(net_contact_forces[:, :, self._undesired_contact_body_ids], dim=-1), dim=1)[0]
            > 1.0
        )
        contacts = torch.sum(is_contact, dim=1)
        flat_orientation = torch.sum(torch.square(self._robot.data.projected_gravity_b.torch[:, :2]), dim=1)

        rewards = {
            "track_lin_vel_xy_exp": lin_vel_error_mapped * self.cfg.lin_vel_reward_scale * self.step_dt,
            "track_ang_vel_z_exp": yaw_rate_error_mapped * self.cfg.yaw_rate_reward_scale * self.step_dt,
            "lin_vel_z_l2": z_vel_error * self.cfg.z_vel_reward_scale * self.step_dt,
            "ang_vel_xy_l2": ang_vel_error * self.cfg.ang_vel_reward_scale * self.step_dt,
            "dof_torques_l2": joint_torques * self.cfg.joint_torque_reward_scale * self.step_dt,
            "dof_acc_l2": joint_accel * self.cfg.joint_accel_reward_scale * self.step_dt,
            "action_rate_l2": action_rate * self.cfg.action_rate_reward_scale * self.step_dt,
            "feet_air_time": air_time * self.cfg.feet_air_time_reward_scale * self.step_dt,
            "undesired_contacts": contacts * self.cfg.undesired_contact_reward_scale * self.step_dt,
            "flat_orientation_l2": flat_orientation * self.cfg.flat_orientation_reward_scale * self.step_dt,
        }
        reward = torch.sum(torch.stack(list(rewards.values())), dim=0)
        for key, value in rewards.items():
            self._episode_sums[key] += value
        return reward
```
```

### source/isaaclab/isaaclab/actuators/actuator_base_cfg.py

```
def _is_implicit_actuator_cfg(cfg)
class ActuatorBaseCfg()
    """Configuration for default actuators in an articulation."""
```

### source/isaaclab/isaaclab/actuators/actuator_cfg.py

```
def __getattr__(name)
```

### source/isaaclab/isaaclab/actuators/actuator_net_cfg.py

```
class ActuatorNetLSTMCfg(DCMotorCfg)
    """Configuration for LSTM-based actuator model."""
class ActuatorNetMLPCfg(DCMotorCfg)
    """Configuration for MLP-based actuator model."""
```

### source/isaaclab/isaaclab/actuators/actuator_pd_cfg.py

```
class ImplicitActuatorCfg(ActuatorBaseCfg)
    """Configuration for an implicit actuator.

Note:
    The PD control is handled implicitly by the simulation."""
class IdealPDActuatorCfg(ActuatorBaseCfg)
    """Configuration for an ideal PD actuator."""
class DCMotorCfg(IdealPDActuatorCfg)
    """Configuration for direct control (DC) motor actuator model."""
class DelayedPDActuatorCfg(IdealPDActuatorCfg)
    """Configuration for a delayed PD actuator."""
class RemotizedPDActuatorCfg(DelayedPDActuatorCfg)
    """Configuration for a remotized PD actuator.

Note:
    The torque output limits for this actuator is derived from a linear interpolation of a lookup table
    in :attr:`joint_parameter_lookup`. This table describes the relationship between joint angles and
    the output torques."""
```

### source/isaaclab/isaaclab/app/sim_launcher.py

```
"""Utilities for detecting and launching the appropriate simulation backend.

The flow is intentionally simple: walk the config tree **once** to collect its
signals into a :class:`Scan`, resolve the Kit runtime sources from that scan and
the launcher inputs, then validate and launch."""
def add_launcher_args(parser)
def make_physics_cfg(physics_cfg_str)
def _is_ovrtx_renderer(node)
def _is_auto_rtx_renderer(node)
def _is_auto_physx_physics(node)
def _is_kit_camera(node)
def _get_arg(launcher_args, key, default)
def _set_arg(launcher_args, key, value)
def _get_visualizer_types(launcher_args)
def _get_livestream_mode(launcher_args)
def _ensure_livestream_kit_visualizer(launcher_args)
def _get_visualizer_intent(cfg)
class Scan()
    """Signals gathered from one walk of the config tree (see :func:`scan`).

Every field starts as a plain snapshot computed during that single walk.
Automatic PhysX configurations and RTX placeholders are also recorded so
launch-time resolution can update the physics- and renderer-related fields
without """
def _refresh_physics_scan_flags(config_scan, concrete_physics_cfgs, has_physics)
def scan(cfg, launcher_args)
def _has_kit_visualizer(config_scan, launcher_args)
def _get_kit_runtime_sources(config_scan, launcher_args)
def _format_runtime_sources(sources)
def _validate_runtime(scan, kit_sources)
def _resolve_distributed_device(cfg, launcher_args)
def launch_simulation(cfg, launcher_args)
def _ensure_isaac_sim_available()
```

### source/isaaclab/isaaclab/benchmark/entrypoints/backends/rl_games/benchmark_train_rl_games.py

```
"""RL-Games adapter for the unified training benchmark."""
def _close_rl_games_writer(observer)
def _parse_args(argv)
def run(argv)
```

### source/isaaclab/isaaclab/benchmark/entrypoints/backends/rsl_rl/benchmark_train_rsl_rl.py

```
"""RSL-RL adapter for the unified training benchmark."""
def _disable_code_state_capture(runner)
def _parse_args(argv)
def run(argv)
```

### source/isaaclab/isaaclab/benchmark/entrypoints/backends/sb3/benchmark_train_sb3.py

```
"""Stable-Baselines3 adapter for the unified training benchmark."""
def _build_benchmark_callback_class()
def _parse_args(argv)
def run(argv)
```

### source/isaaclab/isaaclab/benchmark/entrypoints/backends/skrl/benchmark_train_skrl.py

```
"""SKRL adapter for the unified training benchmark."""
def _build_benchmark_trainer_class()
def _parse_args(argv)
def run(argv)
```

### source/isaaclab/isaaclab/benchmark/entrypoints/training.py

```
"""Command-line entrypoint for RL training benchmarks."""
def main(argv)
def _resolve_training_checkpoint_path(log_dir, backend)
```

### source/isaaclab/isaaclab/cli/commands/envs.py

```
def _reject_downloaded_isaac_sim(environment_type)
def _sanitized_conda_env()
def _patch_environment_yml(yml_path, python_version)
def _get_conda_prefix(env_name)
def _create_conda_envhooks_shell(conda_prefix)
def _write_torch_gomp_hooks_linux(conda_prefix)
def _create_conda_envhooks_cmdexe(conda_prefix)
def _create_conda_envhooks_powershell(conda_prefix)
def _write_conda_env_hooks(conda_prefix)
def _append_hook_if_missing(script_path, marker, hook_content)
def _create_uv_envhooks_shell(env_path)
def _create_uv_envhooks_cmdexe(env_path)
def _create_uv_envhooks_powershell(env_path)
def _write_uv_env_hooks(env_path)
def command_setup_conda(env_name)
def _check_venv_python_version(env_path, required_ver)
def command_setup_uv(env_name)
```

### source/isaaclab/isaaclab/cloner/cloner_cfg.py

```
def expand_env_regex_ns(path_expr, env_template)
class InclusionSet()
    """Legal clone combination defined by explicitly listing active assets."""
class CloneCfg()
    """Configuration for environment replication.

Holds the knobs :class:`~isaaclab.scene.InteractiveScene` forwards to
:func:`~isaaclab.cloner.make_clone_plan` when building per-env layouts."""
def add(this, other)
```

### source/isaaclab/isaaclab/controllers/differential_ik_cfg.py

```
class DifferentialIKControllerCfg()
    """Configuration for differential inverse kinematics controller."""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/controllers/joint_impedance_cfg.py

```
class JointImpedanceControllerCfg()
    """Configuration for joint impedance regulation controller."""
```

### source/isaaclab/isaaclab/controllers/operational_space_cfg.py

```
class OperationalSpaceControllerCfg()
    """Configuration for operational-space controller."""
```

### source/isaaclab/isaaclab/controllers/pink_ik/local_frame_task.py

```
"""Deprecated compatibility shim for Pink task imports.

Prefer importing from ``isaaclab.controllers.pink_ik.pink_tasks``."""
```

### source/isaaclab/isaaclab/controllers/pink_ik/null_space_posture_task.py

```
class NullSpacePostureTask(Task)
    """Pink-based task that adds a posture objective that is in the null space projection of other tasks.

This task implements posture control in the null space of higher priority tasks
(typically end-effector pose tasks) within the Pink inverse kinematics framework.

**Mathematical Formulation:**

For de"""
    def __init__(self, cfg)
    def __repr__(self)
    def _build_joint_mapping(self, configuration)
    def set_target(self, target_q)
    def set_target_from_configuration(self, configuration)
    def compute_error(self, configuration)
    def compute_jacobian(self, configuration)
```

### source/isaaclab/isaaclab/controllers/pink_ik/pink_ik_cfg.py

```
"""Configuration for Pink IK controller."""
class PinkIKControllerCfg()
    """Configuration settings for the Pink IK Controller.

The Pink IK controller can be found at: https://github.com/stephane-caron/pink"""
```

### source/isaaclab/isaaclab/controllers/pink_ik/pink_kinematics_configuration.py

```
class PinkKinematicsConfiguration(Configuration)
    """A configuration class that maintains both a "controlled" (reduced) model and a "full" model.

This class extends the standard Pink Configuration to allow for selective joint control:

- The "controlled" model/data/q represent the subset of joints being actively controlled
  (e.g., a kinematic chain """
    def __init__(self, controlled_joint_names, urdf_path, mesh_path, copy_data, forward_kinematics)
    def update(self, q)
    def get_frame_jacobian(self, frame)
    def get_transform_frame_to_world(self, frame)
    def check_limits(self, tol, safety_break)
    def controlled_joint_names_pinocchio_order(self)
    def all_joint_names_pinocchio_order(self)
```

### source/isaaclab/isaaclab/controllers/pink_ik/pink_task_cfg.py

```
"""Task configuration objects for Pink IK."""
class PinkIKTaskCfg()
    """Base task specification for deferred runtime construction.

All Pink IK task configs inherit from this class.  The :attr:`class_type`
attribute is resolved at runtime to instantiate the concrete task object."""
class FrameTaskCfg(PinkIKTaskCfg)
    """Configuration for a :class:`~isaaclab.controllers.pink_ik.pink_tasks.FrameTask`.

Tracks a desired end-effector pose expressed in the world frame."""
class DampingTaskCfg(PinkIKTaskCfg)
    """Configuration for a :class:`~isaaclab.controllers.pink_ik.pink_tasks.DampingTask`.

Adds joint-velocity damping to the IK problem for numerical stability."""
class LocalFrameTaskCfg(PinkIKTaskCfg)
    """Configuration for a :class:`~isaaclab.controllers.pink_ik.pink_tasks.LocalFrameTask`.

Tracks a desired pose expressed relative to a specified base-link frame
rather than the world frame."""
class NullSpacePostureTaskCfg(PinkIKTaskCfg)
    """Configuration for a :class:`~isaaclab.controllers.pink_ik.null_space_posture_task.NullSpacePostureTask`.

Regularises the IK solution toward a preferred joint posture in the
null-space of the primary tasks."""
```

### source/isaaclab/isaaclab/controllers/pink_ik/pink_tasks.py

```
class FrameTask(PinkFrameTask)
    """Thin wrapper around Pink's :class:`~pink.tasks.frame_task.FrameTask`.

Adds support for the ``class_type(cfg)`` construction pattern used by
Isaac Lab task configuration dataclasses, while remaining fully compatible
with the original string-based constructor."""
    def __init__(self, cfg_or_frame, position_cost, orientation_cost, lm_damping, gain)
class DampingTask(PinkDampingTask)
    """Thin wrapper around Pink's :class:`~pink.tasks.DampingTask`.

Adds joint-velocity damping to the IK problem for numerical stability.
Accepts either a configuration dataclass (``class_type(cfg)`` pattern) or a
direct scalar cost value."""
    def __init__(self, cfg_or_cost, cost)
class LocalFrameTask(FrameTask)
    """A task that computes pose error in a local (custom) frame.

Inherits from :class:`FrameTask` but overrides error and Jacobian computation
to express them relative to a specified base-link frame rather than the world
frame.  This allows control strategies where the reference frame can be chosen
indep"""
    def __init__(self, frame, base_link_frame_name, position_cost, orientation_cost, lm_damping, gain)
    def set_target(self, transform_target_to_base)
    def set_target_from_configuration(self, configuration)
    def compute_error(self, configuration)
    def compute_jacobian(self, configuration)
```

### source/isaaclab/isaaclab/controllers/rmp_flow_cfg.py

```
"""Configuration for RMP-Flow controller."""
class RmpFlowControllerCfg()
    """Configuration for RMP-Flow controller (provided through LULA library)."""
```

### source/isaaclab/isaaclab/devices/gamepad/se2_gamepad_cfg.py

```
"""Configuration for SE(2) gamepad controller."""
class Se2GamepadCfg(DeviceCfg)
    """Configuration for SE2 gamepad devices."""
```

### source/isaaclab/isaaclab/devices/gamepad/se3_gamepad_cfg.py

```
"""Configuration for SE(3) gamepad controller."""
class Se3GamepadCfg(DeviceCfg)
    """Configuration for SE3 gamepad devices."""
```

### source/isaaclab/isaaclab/devices/keyboard/se2_keyboard_cfg.py

```
"""Configuration for SE(2) keyboard controller."""
class Se2KeyboardCfg(DeviceCfg)
    """Configuration for SE2 keyboard devices."""
```

### source/isaaclab/isaaclab/devices/keyboard/se3_keyboard_cfg.py

```
"""Configuration for SE(3) keyboard controller."""
class Se3KeyboardCfg(DeviceCfg)
    """Configuration for SE3 keyboard devices."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/__init__.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.deprecated.openxr.retargeters`."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/fourier/gr1_t2_dex_retargeting_utils.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/fourier/gr1t2_retargeter.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/g1_lower_body_standing.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/g1_motion_controller_locomotion.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/inspire/g1_dex_retargeting_utils.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/inspire/g1_upper_body_retargeter.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/trihand/g1_dex_retargeting_utils.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/trihand/g1_upper_body_motion_ctrl_gripper.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/trihand/g1_upper_body_motion_ctrl_retargeter.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/humanoid/unitree/trihand/g1_upper_body_retargeter.py

```
""".. deprecated:: Moved to ``isaaclab_teleop.deprecated.openxr``."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/manipulator/__init__.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.deprecated.openxr.retargeters.manipulator`."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/manipulator/gripper_retargeter.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.deprecated.openxr.retargeters.manipulator.gripper_retargeter`."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/manipulator/se3_abs_retargeter.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.deprecated.openxr.retargeters.manipulator.se3_abs_retargeter`."""
```

### source/isaaclab/isaaclab/devices/openxr/retargeters/manipulator/se3_rel_retargeter.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.deprecated.openxr.retargeters.manipulator.se3_rel_retargeter`."""
```

### source/isaaclab/isaaclab/devices/openxr/xr_cfg.py

```
""".. deprecated:: Moved to :mod:`isaaclab_teleop.xr_cfg`."""
```

### source/isaaclab/isaaclab/devices/retargeter_base.py

```
class RetargeterCfg()
    """Base configuration for hand tracking retargeters.

.. deprecated::
    Use the IsaacTeleop retargeting engine via :mod:`isaaclab_teleop` instead."""
class RetargeterBase(ABC)
    """Base interface for input data retargeting.

.. deprecated::
    Use the IsaacTeleop retargeting engine via :mod:`isaaclab_teleop` instead.

This abstract class defines the interface for components that transform
raw device data into robot control commands. Implementations can handle
various types of"""
    def __init__(self, cfg)
    def retarget(self, data)
    def get_requirements(self)
```

### source/isaaclab/isaaclab/devices/spacemouse/se2_spacemouse_cfg.py

```
"""Configuration for SE(2) space mouse controller."""
class Se2SpaceMouseCfg(DeviceCfg)
    """Configuration for SE2 space mouse devices."""
```

### source/isaaclab/isaaclab/devices/spacemouse/se3_spacemouse_cfg.py

```
"""Configuration for SE(3) space mouse controller."""
class Se3SpaceMouseCfg(DeviceCfg)
    """Configuration for SE3 space mouse devices."""
```

### source/isaaclab/isaaclab/envs/__init__.py

```
"""Sub-package for environment definitions.

Environments define the interface between the agent and the simulation.
In the simplest case, the environment provides the agent with the current
observations and executes the actions provided by the agent. However, the
environment can also provide additional information such as the current
reward, done flag, and information about the current episode.

There are two types of environment designing workflows:

* **Manager-based**: The environment is decomposed into individual components (or managers)
  for different aspects (such as computing observation"""
```

### source/isaaclab/isaaclab/envs/common.py

```
def _viewer_cfg_field_matches_default(value, default)
class ViewerCfg()
    """Configuration of the scene viewport camera.

.. deprecated::
    :class:`ViewerCfg` is deprecated and will be removed in a future release.
    Configure the viewport camera via :class:`~isaaclab_visualizers.kit.KitVisualizerCfg`
    and add it to :attr:`~isaaclab.sim.SimulationCfg.visualizer_cfgs` i"""
    def __post_init__(self)
def _apply_deprecated_viewer_cfg(env_cfg)
```

### source/isaaclab/isaaclab/envs/direct_marl_env.py

```
class DirectMARLEnv(Env)
    """The superclass for the direct workflow to design multi-agent environments.

This class implements the core functionality for multi-agent reinforcement learning (MARL)
environments. It is designed to be used with any RL library. The class is designed
to be used with vectorized environments, i.e., the"""
    def __init__(self, cfg, render_mode)
    def _init_sim(self, render_mode)
    def __del__(self, _sys)
    def num_envs(self)
    def num_agents(self)
    def max_num_agents(self)
    def unwrapped(self)
    def physics_dt(self)
    def step_dt(self)
    def device(self)
    def max_episode_length_s(self)
    def max_episode_length(self)
    def observation_space(self, agent)
    def action_space(self, agent)
    def reset(self, seed, options)
    def step(self, actions)
    def state(self)
    def seed(seed)
    def render(self, recompute)
    def close(self)
    def set_debug_vis(self, debug_vis)
    def _configure_env_spaces(self)
    def _reset_idx(self, env_ids)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_observations(self)
    def _get_states(self)
    def _get_rewards(self)
    def _get_dones(self)
    def _set_debug_vis_impl(self, debug_vis)

```python
def observation_space(self, agent: AgentID) -> gym.Space:
        """Get the observation space for the specified agent.

        Returns:
            The agent's observation space.
        """
        return self.observation_spaces[agent]
```

```python
def _get_observations(self) -> dict[AgentID, ObsType]:
        """Compute and return the observations for the environment.

        Returns:
            The observations for the environment (keyed by the agent ID).
        """
        raise NotImplementedError(f"Please implement the '_get_observations' method for {self.__class__.__name__}.")
```

```python
def _get_rewards(self) -> dict[AgentID, torch.Tensor]:
        """Compute and return the rewards for the environment.

        Returns:
            The rewards for the environment (keyed by the agent ID).
            Shape of individual tensors is (num_envs,).
        """
        raise NotImplementedError(f"Please implement the '_get_rewards' method for {self.__class__.__name__}.")
```
```

### source/isaaclab/isaaclab/envs/direct_marl_env_cfg.py

```
class DirectMARLEnvCfg()
    """Configuration for a MARL environment defined with the direct workflow.

Please refer to the :class:`isaaclab.envs.direct_marl_env.DirectMARLEnv` class for more details."""
    def play_mode(self)
```

### source/isaaclab/isaaclab/envs/direct_rl_env.py

```
class DirectRLEnv(Env)
    """The superclass for the direct workflow to design environments.

This class implements the core functionality for reinforcement learning (RL)
environments. It is designed to be used with any RL library. The class is designed
to be used with vectorized environments, i.e., the environment is expected t"""
    def __init__(self, cfg, render_mode)
    def _init_sim(self, render_mode)
    def __del__(self, _sys)
    def num_envs(self)
    def physics_dt(self)
    def step_dt(self)
    def device(self)
    def max_episode_length_s(self)
    def max_episode_length(self)
    def reset(self, seed, options)
    def step(self, action)
    def seed(seed)
    def render(self, recompute)
    def setup_direct_visualizers(self)
    def close(self)
    def set_debug_vis(self, debug_vis)
    def _configure_gym_env_spaces(self)
    def _reset_envs_from_buffer(self)
    def _reset_idx(self, env_ids)
    def _setup_scene(self)
    def _pre_physics_step(self, actions)
    def _apply_action(self)
    def _get_observations(self)
    def _get_states(self)
    def _get_rewards(self)
    def _get_dones(self)
    def _set_debug_vis_impl(self, debug_vis)

```python
def _get_observations(self) -> VecEnvObs:
        """Compute and return the observations for the environment.

        Returns:
            The observations for the environment.
        """
        raise NotImplementedError(f"Please implement the '_get_observations' method for {self.__class__.__name__}.")
```

```python
def _get_rewards(self) -> torch.Tensor:
        """Compute and return the rewards for the environment.

        Returns:
            The rewards for the environment. Shape is (num_envs,).
        """
        raise NotImplementedError(f"Please implement the '_get_rewards' method for {self.__class__.__name__}.")
```
```

### source/isaaclab/isaaclab/envs/direct_rl_env_cfg.py

```
class DirectRLEnvCfg()
    """Configuration for an RL environment defined with the direct workflow.

Please refer to the :class:`isaaclab.envs.direct_rl_env.DirectRLEnv` class for more details."""
    def play_mode(self)
```

### source/isaaclab/isaaclab/envs/leapp_deployment_env.py

```
"""Deployment environment that runs LEAPP-exported policies in simulation.

This environment bypasses all Isaac Lab managers (observation, action, reward, etc.)
and instead wires scene entity data properties and ``CommandManager`` outputs directly
to a LEAPP ``InferenceManager``, then writes the model outputs back to the
corresponding scene entities.  All I/O resolution is driven by the
``isaaclab_connection`` field in the LEAPP YAML."""
class StateInputSpec()
    """Read a property from a scene entity's data object."""
class CommandInputSpec()
    """Read a command tensor from ``CommandManager``."""
class WriteOutputSpec()
    """Write a tensor to a scene entity method, optionally indexed by joint."""
def _resolve_joint_ids(element_names, entity)
def _first_param_name(method)
class LeappDeploymentEnv()
    """Runs a LEAPP-exported policy in an Isaac Lab scene.

The environment sets up the simulation scene and physics from a standard
Isaac Lab config, then wires raw sensor/command data to a LEAPP
``InferenceManager`` and writes the model outputs back to the corresponding
scene entities.

I/O wiring is dri"""
    def __init__(self, cfg, leapp_yaml_path)
    def num_envs(self)
    def physics_dt(self)
    def step_dt(self)
    def device(self)
    def _resolve_io(self)
    def _read_inputs(self)
    def _write_outputs(self, outputs)
    def reset(self)
    def step(self, external_inputs)
    def close(self)
```

### source/isaaclab/isaaclab/envs/manager_based_env.py

```
class ManagerBasedEnv()
    """The base environment encapsulates the simulation scene and the environment managers for
the manager-based workflow.

While a simulation scene or world comprises of different components such as the robots, objects,
and sensors (cameras, lidars, etc.), the environment is a higher level abstraction
tha"""
    def __init__(self, cfg)
    def _init_sim(self)
    def __del__(self, _sys)
    def num_envs(self)
    def physics_dt(self)
    def step_dt(self)
    def device(self)
    def get_IO_descriptors(self)
    def export_IO_descriptors(self, output_dir)
    def load_managers(self)
    def setup_manager_visualizers(self)
    def reset(self, seed, env_ids, options)
    def reset_to(self, state, env_ids, seed, is_relative)
    def step(self, action)
    def seed(seed)
    def close(self)
    def _reset_idx(self, env_ids)
```

### source/isaaclab/isaaclab/envs/manager_based_env_cfg.py

```
"""Base configuration of the environment.

This module defines the general configuration of the environment. It includes parameters for
configuring the environment instances and simulation parameters."""
class DefaultEventManagerCfg()
    """Configuration of the default event manager.

This manager is used to reset the scene to a default state. The default state is specified
by the scene configuration."""
class ManagerBasedEnvCfg()
    """Base configuration of the environment."""
```

### source/isaaclab/isaaclab/envs/manager_based_rl_env.py

```
class ManagerBasedRLEnv(ManagerBasedEnv, Env)
    """The superclass for the manager-based workflow reinforcement learning-based environments.

This class inherits from :class:`ManagerBasedEnv` and implements the core functionality for
reinforcement learning-based environments. It is designed to be used with any RL
library. The class is designed to be """
    def __init__(self, cfg, render_mode)
    def max_episode_length_s(self)
    def max_episode_length(self)
    def load_managers(self)
    def setup_manager_visualizers(self)
    def step(self, action)
    def render(self, recompute)
    def close(self)
    def _configure_gym_env_spaces(self)
    def _reset_idx(self, env_ids)
```

### source/isaaclab/isaaclab/envs/manager_based_rl_env_cfg.py

```
class ManagerBasedRLEnvCfg(ManagerBasedEnvCfg)
    """Configuration for a reinforcement learning environment with the manager-based workflow."""
    def play_mode(self)
```

### source/isaaclab/isaaclab/envs/manager_based_rl_mimic_env.py

```
def optional_method(func)
class ManagerBasedRLMimicEnv(ManagerBasedRLEnv)
    """The superclass for the Isaac Lab Mimic environments.

This class inherits from :class:`ManagerBasedRLEnv` and provides a template for the functions that
need to be defined to run the Isaac Lab Mimic data generation workflow. The Isaac Lab data generation
pipeline, inspired by the MimicGen system, en"""
    def get_robot_eef_pose(self, eef_name, env_ids)
    def target_eef_pose_to_action(self, target_eef_pose_dict, gripper_action_dict, action_noise_dict, env_id)
    def action_to_target_eef_pose(self, action)
    def actions_to_gripper_actions(self, actions)
    def get_object_poses(self, env_ids)
    def get_subtask_start_signals(self, env_ids)
    def get_subtask_term_signals(self, env_ids)
    def serialize(self)
    def get_navigation_state(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/__init__.py

```
"""Sub-module with implementation of manager terms.

The functions can be provided to different managers that are responsible for the
different aspects of the MDP. These include the observation, reward, termination,
actions, events and curriculum managers.

The terms are defined under the ``envs`` module because they are used to define
the environment. However, they are not part of the environment directly, but
are used to define the environment through their managers."""
```

### source/isaaclab/isaaclab/envs/mdp/actions/__init__.py

```
"""Various action terms that can be used in the environment."""
```

### source/isaaclab/isaaclab/envs/mdp/actions/actions_cfg.py

```
class JointActionCfg(ActionTermCfg)
    """Configuration for the base joint action term.

See :class:`JointAction` for more details."""
class FixedTendonPositionActionCfg(ActionTermCfg)
    """Configuration for a position action over an articulation's fixed tendons.

See :class:`FixedTendonPositionAction` for more details."""
class JointPositionActionCfg(JointActionCfg)
    """Configuration for the joint position action term.

See :class:`JointPositionAction` for more details."""
class RelativeJointPositionActionCfg(JointActionCfg)
    """Configuration for the relative joint position action term.

See :class:`RelativeJointPositionAction` for more details."""
class JointVelocityActionCfg(JointActionCfg)
    """Configuration for the joint velocity action term.

See :class:`JointVelocityAction` for more details."""
class JointEffortActionCfg(JointActionCfg)
    """Configuration for the joint effort action term.

See :class:`JointEffortAction` for more details."""
class JointPositionToLimitsActionCfg(ActionTermCfg)
    """Configuration for the bounded joint position action term.

See :class:`JointPositionToLimitsAction` for more details."""
class EMAJointPositionToLimitsActionCfg(JointPositionToLimitsActionCfg)
    """Configuration for the exponential moving average (EMA) joint position action term.

See :class:`EMAJointPositionToLimitsAction` for more details."""
class BinaryJointActionCfg(ActionTermCfg)
    """Configuration for the base binary joint action term.

See :class:`BinaryJointAction` for more details."""
class BinaryJointPositionActionCfg(BinaryJointActionCfg)
    """Configuration for the binary joint position action term.

See :class:`BinaryJointPositionAction` for more details."""
class BinaryJointVelocityActionCfg(BinaryJointActionCfg)
    """Configuration for the binary joint velocity action term.

See :class:`BinaryJointVelocityAction` for more details."""
class AbsBinaryJointPositionActionCfg(ActionTermCfg)
    """Configuration for the absolute binary joint position action term.

This action term is used for robust grasping by converting continuous gripper joint position actions
into binary open/close commands. Unlike directly applying continuous gripper joint position actions, this class
applies a threshold-"""
class NonHolonomicActionCfg(ActionTermCfg)
    """Configuration for the non-holonomic action term with dummy joints at the base.

See :class:`NonHolonomicAction` for more details."""
class DifferentialInverseKinematicsActionCfg(ActionTermCfg)
    """Configuration for inverse differential kinematics action term.

See :class:`DifferentialInverseKinematicsAction` for more details."""
class OperationalSpaceControllerActionCfg(ActionTermCfg)
    """Configuration for operational space controller action term.

See :class:`OperationalSpaceControllerAction` for more details."""
class SurfaceGripperBinaryActionCfg(ActionTermCfg)
    """Configuration for the binary surface gripper action term.

See :class:`SurfaceGripperBinaryAction` for more details."""
```

### source/isaaclab/isaaclab/envs/mdp/actions/binary_joint_actions.py

```
class BinaryJointAction(ActionTerm)
    """Base class for binary joint actions.

This action term maps a binary action to the *open* or *close* joint configurations. These configurations are
specified through the :class:`BinaryJointActionCfg` object. If the input action is a float vector, the action
is considered binary based on the sign of """
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def reset(self, env_ids)
class BinaryJointPositionAction(BinaryJointAction)
    """Binary joint action that sets the binary action into joint position targets."""
    def apply_actions(self)
class BinaryJointVelocityAction(BinaryJointAction)
    """Binary joint action that sets the binary action into joint velocity targets."""
    def apply_actions(self)
class AbsBinaryJointPositionAction(BinaryJointAction)
    """Absolute Binary joint action that sets the binary action into joint position targets.

This class extends :class:`BinaryJointAction` to accept absolute joint-position
actions [m or rad, depending on joint type] for gripper control. It compares
each continuous action with the configured threshold and"""
    def process_actions(self, actions)
    def apply_actions(self)
```

### source/isaaclab/isaaclab/envs/mdp/actions/joint_actions.py

```
class JointAction(ActionTerm)
    """Base class for joint actions.

This action term performs pre-processing of the raw actions using affine transformations (scale and offset).
These transformations can be configured to be applied to a subset of the articulation's joints.

Mathematically, the action term is defined as:

.. math::

   \"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def reset(self, env_ids)
class JointPositionAction(JointAction)
    """Joint action term that applies the processed actions to the articulation's joints as position commands."""
    def __init__(self, cfg, env)
    def apply_actions(self)
class RelativeJointPositionAction(JointAction)
    """Joint action term that applies the processed actions to the articulation's joints as relative position commands.

Unlike :class:`JointPositionAction`, this action term applies the processed actions as relative position commands.
This means that the processed actions are added to the current joint po"""
    def __init__(self, cfg, env)
    def apply_actions(self)
class JointVelocityAction(JointAction)
    """Joint action term that applies the processed actions to the articulation's joints as velocity commands."""
    def __init__(self, cfg, env)
    def apply_actions(self)
class JointEffortAction(JointAction)
    """Joint action term that applies the processed actions to the articulation's joints as effort commands."""
    def __init__(self, cfg, env)
    def apply_actions(self)
```

### source/isaaclab/isaaclab/envs/mdp/actions/joint_actions_to_limits.py

```
class JointPositionToLimitsAction(ActionTerm)
    """Joint position action term that scales the input actions to the joint limits and applies them to the
articulation's joints.

This class is similar to the :class:`JointPositionAction` class. However, it performs additional
re-scaling of input actions to the actuator joint position limits.

While proc"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
class EMAJointPositionToLimitsAction(JointPositionToLimitsAction)
    """Joint action term that applies exponential moving average (EMA) over the processed actions as the
articulation's joints position commands.

Exponential moving average (EMA) is a type of moving average that gives more weight to the most recent data points.
This action term applies the processed actio"""
    def __init__(self, cfg, env)
    def IO_descriptor(self)
    def reset(self, env_ids)
    def process_actions(self, actions)
```

### source/isaaclab/isaaclab/envs/mdp/actions/non_holonomic_actions.py

```
class NonHolonomicAction(ActionTerm)
    """Non-holonomic action that maps a two dimensional action to the velocity of the robot in
the x, y and yaw directions.

This action term helps model a skid-steer robot base. The action is a 2D vector which comprises of the
forward velocity :math:`v_{B,x}` and the turning rate :\omega_{B,z}: in the bas"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/actions/pink_actions_cfg.py

```
class PinkInverseKinematicsActionCfg(ActionTermCfg)
    """Configuration for Pink inverse kinematics action term.

This configuration is used to define settings for the Pink inverse kinematics action term,
which is a inverse kinematics framework."""
```

### source/isaaclab/isaaclab/envs/mdp/actions/pink_task_space_actions.py

```
class PinkInverseKinematicsAction(ActionTerm)
    """Pink Inverse Kinematics action term.

This action term processes the action tensor and sets these setpoints in the pink IK framework.
The action tensor is ordered in the order of the tasks defined in PinkIKControllerCfg."""
    def __init__(self, cfg, env)
    def _initialize_joint_info(self)
    def _initialize_ik_controllers(self)
    def _initialize_helper_tensors(self)
    def hand_joint_dim(self)
    def position_dim(self)
    def orientation_dim(self)
    def pose_dim(self)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def _get_base_link_frame_transform(self)
    def _extract_controlled_frame_poses(self, actions)
    def _transform_poses_to_base_link_frame(self, poses)
    def _set_task_targets(self, transformed_poses)
    def apply_actions(self)
    def _apply_gravity_compensation(self)
    def _compute_ik_solutions(self)
    def reset(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/actions/rmpflow_actions_cfg.py

```
class RMPFlowActionCfg(ActionTermCfg)
```

### source/isaaclab/isaaclab/envs/mdp/actions/rmpflow_task_space_actions.py

```
class RMPFlowAction(ActionTerm)
    """RMPFlow task space action term."""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def jacobian_w(self)
    def jacobian_b(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
    def _compute_frame_pose(self)
```

### source/isaaclab/isaaclab/envs/mdp/actions/surface_gripper_actions.py

```
class SurfaceGripperBinaryAction(ActionTerm)
    """Surface gripper binary action.

This action term maps a binary action to the *open* or *close* surface gripper configurations.
The surface gripper behavior is as follows:
- [-1, -0.3] --> Gripper is Opening
- [-0.3, 0.3] --> Gripper is Idle (do nothing)
- [0.3, 1] --> Gripper is Closing

Based on ab"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/actions/task_space_actions.py

```
class DifferentialInverseKinematicsAction(ActionTerm)
    """Inverse Kinematics action term.

This action term performs pre-processing of the raw actions using scaling transformation.

.. math::
    \text{action} = \text{scaling} \times \text{input action}
    \text{joint position} = J^{-} \times \text{action}

where :math:`\text{scaling}` is the scaling appl"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def jacobian_w(self)
    def jacobian_b(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
    def _compute_frame_pose(self)
    def _compute_frame_jacobian(self)
class OperationalSpaceControllerAction(ActionTerm)
    """Operational space controller action term.

This action term performs pre-processing of the raw actions for operational space control."""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def jacobian_w(self)
    def jacobian_b(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
    def _resolve_command_indexes(self)
    def _resolve_nullspace_joint_pos_targets(self)
    def _compute_dynamic_quantities(self)
    def _compute_ee_jacobian(self)
    def _compute_ee_pose(self)
    def _compute_ee_velocity(self)
    def _compute_ee_force(self)
    def _compute_joint_states(self)
    def _compute_task_frame_pose(self)
    def _preprocess_actions(self, actions)
```

### source/isaaclab/isaaclab/envs/mdp/actions/tendon_actions.py

```
"""Action terms for articulations whose motors drive fixed tendons."""
class FixedTendonPositionAction(ActionTerm)
    """Position targets for an articulation's fixed tendons.

An underactuated hand has fewer motors than joints because some motors pull a tendon spanning
several joints. Tendons are a separate entity from joints in the simulation, with their own
index space, so a joint-position term cannot address one --"""
    def __init__(self, cfg, env)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def IO_descriptor(self)
    def process_actions(self, actions)
    def apply_actions(self)
    def reset(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/commands/__init__.py

```
"""Various command terms that can be used in the environment."""
```

### source/isaaclab/isaaclab/envs/mdp/commands/commands_cfg.py

```
class NullCommandCfg(CommandTermCfg)
    """Configuration for the null command generator."""
    def __post_init__(self)
class UniformVelocityCommandCfg(CommandTermCfg)
    """Configuration for the uniform velocity command generator."""
class NormalVelocityCommandCfg(UniformVelocityCommandCfg)
    """Configuration for the normal velocity command generator."""
class UniformPoseCommandCfg(CommandTermCfg)
    """Configuration for uniform pose command generator."""
class UniformPose2dCommandCfg(CommandTermCfg)
    """Configuration for the uniform 2D-pose command generator."""
class TerrainBasedPose2dCommandCfg(UniformPose2dCommandCfg)
    """Configuration for the terrain-based position command generator."""
```

### source/isaaclab/isaaclab/envs/mdp/commands/null_command.py

```
"""Sub-module containing command generator that does nothing."""
class NullCommand(CommandTerm)
    """Command generator that does nothing.

This command generator does not generate any commands. It is used for environments that do not
require any commands."""
    def __str__(self)
    def command(self)
    def reset(self, env_ids)
    def compute(self, dt)
    def _update_metrics(self)
    def _resample_command(self, env_ids)
    def _update_command(self)
```

### source/isaaclab/isaaclab/envs/mdp/commands/pose_2d_command.py

```
"""Sub-module containing command generators for the 2D-pose for locomotion tasks."""
class UniformPose2dCommand(CommandTerm)
    """Command generator that generates pose commands containing a 3-D position and heading.

The command generator samples uniform 2D positions around the environment origin. It sets
the height of the position command to the default root height of the robot. The heading
command is either set to point towa"""
    def __init__(self, cfg, env)
    def __str__(self)
    def command(self)
    def _update_metrics(self)
    def reset(self, env_ids)
    def _resample_command(self, env_ids)
    def _update_command(self)
    def _set_debug_vis_impl(self, debug_vis)
    def _debug_vis_callback(self, event)
class TerrainBasedPose2dCommand(UniformPose2dCommand)
    """Command generator that generates pose commands based on the terrain.

This command generator samples the position commands from the valid patches of the terrain.
The heading commands are either set to point towards the target or are sampled uniformly.

It expects the terrain to have a valid flat pat"""
    def __init__(self, cfg, env)
    def _resample_command(self, env_ids)
```

### source/isaaclab/isaaclab/envs/mdp/commands/pose_command.py

```
"""Sub-module containing command generators for pose tracking."""
class UniformPoseCommand(CommandTerm)
    """Command generator for generating pose commands uniformly.

The command generator generates poses by sampling positions uniformly within specified
regions in cartesian space. For orientation, it samples uniformly the euler angles
(roll-pitch-yaw) and converts them into quaternion representation (x, y"""
    def __init__(self, cfg, env)
    def __str__(self)
    def command(self)
    def compute_success(self)
    def _update_metrics(self)
    def _compute_error(self)
    def _compute_success(self, position_error, orientation_error)
    def reset(self, env_ids)
    def _resample_command(self, env_ids)
    def _update_command(self)
    def _set_debug_vis_impl(self, debug_vis)
    def _debug_vis_callback(self, event)
```

### source/isaaclab/isaaclab/envs/mdp/commands/velocity_command.py

```
"""Sub-module containing command generators for the velocity-based locomotion task."""
class UniformVelocityCommand(CommandTerm)
    """Command generator that generates a velocity command in SE(2) from uniform distribution.

The command comprises of a linear velocity in x and y direction and an angular velocity around
the z-axis. It is given in the robot's base frame.

If the :attr:`cfg.heading_command` flag is set to True, the angu"""
    def __init__(self, cfg, env)
    def __str__(self)
    def command(self)
    def _update_metrics(self)
    def reset(self, env_ids)
    def _resample_command(self, env_ids)
    def _update_command(self)
    def _set_debug_vis_impl(self, debug_vis)
    def _debug_vis_callback(self, event)
    def _resolve_xy_velocity_to_arrow(self, xy_velocity)
class NormalVelocityCommand(UniformVelocityCommand)
    """Command generator that generates a velocity command in SE(2) from a normal distribution.

The command comprises of a linear velocity in x and y direction and an angular velocity around
the z-axis. It is given in the robot's base frame.

The command is sampled from a normal distribution with mean and"""
    def __init__(self, cfg, env)
    def __str__(self)
    def _resample_command(self, env_ids)
    def _update_command(self)
```

### source/isaaclab/isaaclab/envs/mdp/curriculums.py

```
"""Common functions that can be used to create curriculum for the learning environment.

The functions can be passed to the :class:`isaaclab.managers.CurriculumTermCfg` object to enable
the curriculum introduced by the function."""
class modify_reward_weight(ManagerTermBase)
    """Curriculum that modifies the reward weight based on a step-wise schedule."""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, term_name, weight, num_steps)
class modify_env_param(ManagerTermBase)
    """Curriculum term for modifying an environment parameter at runtime.

This term helps modify an environment parameter (or attribute) at runtime.
This parameter can be any attribute of the environment, such as the physics material properties,
observation ranges, or any other configurable parameter that"""
    def __init__(self, cfg, env)
    def __del__(self)
    def __call__(self, env, env_ids, address, modify_fn, modify_params)
    def _process_accessors(self, root, path)
class modify_term_cfg(modify_env_param)
    """Curriculum for modifying a manager term configuration at runtime.

This class inherits from :class:`modify_env_param` and is specifically designed to modify
the configuration of a manager term in the environment. It mainly adds the convenience of
using a simplified address style that uses "s." as a """
    def __init__(self, cfg, env)
```

### source/isaaclab/isaaclab/envs/mdp/events.py

```
"""Common functions that can be used to enable different events.

Events include anything related to altering the simulation state. This includes changing the physics
materials, applying external forces, and resetting the state of the asset.

The functions can be passed to the :class:`isaaclab.managers.EventTermCfg` object to enable
the event introduced by the function."""
def randomize_rigid_body_scale(env, env_ids, scale_range, asset_cfg, relative_child_path)
class _RandomizeRigidBodyMaterialPhysx()
    """PhysX backend implementation for material randomization.

Uses the bucket-based approach required by PhysX's 64000 unique material limit.
Materials are pre-sampled into buckets and randomly assigned to shapes."""
    def __init__(self, cfg, env, asset, asset_cfg)
    def __call__(self, env, env_ids, static_friction_range, dynamic_friction_range, restitution_range, num_buckets, asset_cfg, make_consistent)
class _RandomizeRigidBodyMaterialNewton()
    """Newton backend implementation for material randomization.

Newton can assign arbitrary friction/restitution per shape (no bucket limitation).
Samples friction (mu) and restitution continuously from the given ranges.
Newton uses a single friction coefficient (mu), so ``dynamic_friction_range``
and ``"""
    def __init__(self, cfg, env, asset, asset_cfg)
    def __call__(self, env, env_ids, static_friction_range, dynamic_friction_range, restitution_range, num_buckets, asset_cfg, make_consistent)
def _is_all_body_selection(body_ids, num_bodies)
class _RandomizeRigidBodyMaterialOvPhysx()
    """OVPhysX backend implementation for material randomization.

OVPhysX runs the PhysX solver, so PhysX's 64000 unique-material limit applies and this
mirrors the PhysX bucket approach: ``num_buckets`` materials are pre-sampled once and
randomly assigned to shapes. Materials are written through the asse"""
    def __init__(self, cfg, env, asset, asset_cfg)
    def __call__(self, env, env_ids, static_friction_range, dynamic_friction_range, restitution_range, num_buckets, asset_cfg, make_consistent)
class randomize_rigid_body_material(ManagerTermBase)
    """Randomize the physics materials on all geometries of the asset.

This function creates a set of physics materials with random static friction, dynamic friction, and restitution
values and assigns them to the geometries of the asset.

For articulations, :attr:`SceneEntityCfg.body_ids` selects bodies """
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, static_friction_range, dynamic_friction_range, restitution_range, num_buckets, asset_cfg, make_consistent)
class randomize_rigid_body_mass(ManagerTermBase)
    """Randomize the mass of the bodies by adding, scaling, or setting random values.

This function allows randomizing the mass of the bodies of the asset. The function samples random
values from the given distribution parameters and adds, scales, or sets the values into the physics
simulation based on th"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, mass_distribution_params, operation, distribution, recompute_inertia, min_mass)
class randomize_rigid_body_inertia(ManagerTermBase)
    """Randomize the inertia tensor of rigid bodies by adding, scaling, or setting values.

This function modifies body inertia tensors independently of mass. The inertia tensor
is a 3x3 symmetric matrix stored as 9 elements: ``[Ixx, Ixy, Ixz, Iyx, Iyy, Iyz, Izx, Izy, Izz]``.

Two modes are supported via t"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, inertia_distribution_params, operation, distribution, diagonal_only)
class randomize_rigid_body_com(ManagerTermBase)
    """Randomize the center of mass (CoM) of rigid bodies by adding a random value sampled from the given ranges.

This class tracks the original CoM values and randomizes from those defaults on each call,
ensuring repeatable randomization across resets.

Automatically detects the active physics backend:

"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, com_range, asset_cfg)
class _RandomizeRigidBodyColliderOffsetsPhysx()
    """PhysX backend implementation for collider offset randomization.

Uses rest offset and contact offset directly via the PhysX tensor API."""
    def __init__(self, asset)
    def __call__(self, env, env_ids, asset_cfg, rest_offset_distribution_params, contact_offset_distribution_params, distribution)
class _RandomizeRigidBodyColliderOffsetsOvPhysx()
    """OVPhysX backend implementation for collider offset randomization.

OVPhysX runs the PhysX solver, so rest and contact offsets are written directly, per collision
shape, through the asset's :class:`~isaaclab_ov.sim.views.OvPhysxView`. Articulations use the
articulation offset bindings and rigid objec"""
    def __init__(self, asset)
    def __call__(self, env, env_ids, asset_cfg, rest_offset_distribution_params, contact_offset_distribution_params, distribution)
class _RandomizeRigidBodyColliderOffsetsNewton()
    """Newton backend implementation for collider offset randomization.

Maps PhysX concepts to Newton's geometry properties:

- ``rest_offset`` -> ``shape_margin`` (Newton margin)
- ``contact_offset`` -> ``shape_gap`` (Newton gap = contact_offset - margin)

See the `Newton collision schema`_ for details.
"""
    def __init__(self, asset)
    def __call__(self, env, env_ids, asset_cfg, rest_offset_distribution_params, contact_offset_distribution_params, distribution)
class randomize_rigid_body_collider_offsets(ManagerTermBase)
    """Randomize the collider parameters of rigid bodies by setting random values.

This function allows randomizing the collider parameters of the asset, such as rest and contact offsets.
These correspond to the physics engine collider properties that affect collision checking.

Automatically detects the """
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, rest_offset_distribution_params, contact_offset_distribution_params, distribution)
class randomize_physics_scene_gravity(ManagerTermBase)
    """Randomize gravity by adding, scaling, or setting random values.

Automatically detects the active physics backend (PhysX, OvPhysX, or Newton) and applies
the appropriate gravity randomization strategy:

- **PhysX**: samples a single gravity vector and sets it scene-wide via the PhysX
  simulation vi"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, gravity_distribution_params, operation, distribution)
    def _init_newton(self, cfg, env)
    def _call_newton(self, env, env_ids, operation)
    def _init_physx(self, env)
    def _call_physx(self, env, operation)
    def _init_ovphysx(self, env)
    def _call_ovphysx(self, env, operation)
class randomize_actuator_gains(ManagerTermBase)
    """Randomize the actuator gains in an articulation by adding, scaling, or setting random values.

This function allows randomizing the actuator stiffness and damping gains.

The function samples random values from the given distribution parameters and applies the operation to
the joint properties. It t"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, stiffness_distribution_params, damping_distribution_params, operation, distribution)
class randomize_joint_parameters(ManagerTermBase)
    """Randomize the simulated joint parameters of an articulation by adding, scaling, or setting random values.

This function allows randomizing the joint parameters of the asset. These correspond to the physics engine
joint properties that affect the joint behavior. The properties include the joint fric"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, friction_distribution_params, armature_distribution_params, lower_limit_distribution_params, upper_limit_distribution_params, operation, distribution)
class randomize_fixed_tendon_parameters(ManagerTermBase)
    """Randomize the simulated fixed tendon parameters of an articulation by adding, scaling, or setting random values.

This function allows randomizing the fixed tendon parameters of the asset.
These correspond to the physics engine tendon properties that affect the joint behavior.

The function samples """
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, asset_cfg, stiffness_distribution_params, damping_distribution_params, limit_stiffness_distribution_params, lower_limit_distribution_params, upper_limit_distribution_params, rest_length_distribution_params, offset_distribution_params, operation, distribution)
def apply_external_force_torque(env, env_ids, force_range, torque_range, asset_cfg)
def push_by_setting_velocity(env, env_ids, velocity_range, asset_cfg)
class reset_root_state_uniform(ManagerTermBase)
    """Reset the asset root state to a random position and velocity uniformly within the given ranges.

This term randomizes the root position and velocity of the asset.

* It samples the root position from the given ranges and adds them to the default root position, before setting
  them into the physics """
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, pose_range, velocity_range, asset_cfg)
def reset_root_state_with_random_orientation(env, env_ids, pose_range, velocity_range, asset_cfg)
def reset_root_state_from_terrain(env, env_ids, pose_range, velocity_range, asset_cfg)
def reset_joints_by_scale(env, env_ids, position_range, velocity_range, asset_cfg)
def reset_joints_by_offset(env, env_ids, position_range, velocity_range, asset_cfg)
class reset_joints_within_limits_range(ManagerTermBase)
    """Reset an articulation's joints to a random position in the given limit ranges.

This function samples random values for the joint position and velocities from the given limit ranges.
The values are then set into the physics simulation.

The parameters to the function are:

* :attr:`position_range` -"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, position_range, velocity_range, use_default_offset, asset_cfg, operation)
def reset_nodal_state_uniform(env, env_ids, position_range, velocity_range, asset_cfg)
def reset_scene_to_default(env, env_ids, reset_joint_targets)
class randomize_visual_texture_material(ManagerTermBase)
    """Randomize the visual texture of bodies on an asset using Replicator API.

This function randomizes the visual texture of the bodies of the asset using the Replicator API.
The function samples random textures from the given texture paths and applies them to the bodies
of the asset. The textures are p"""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, event_name, asset_cfg, texture_paths, texture_rotation)
class randomize_visual_color(ManagerTermBase)
    """Randomize the visual color of bodies on an asset using Replicator API.

This function randomizes the visual color of the bodies of the asset using the Replicator API.
The function samples random colors from the given colors and applies them to the bodies
of the asset.

The function assumes that the """
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, event_name, asset_cfg, colors, mesh_name)
def _randomize_prop_by_op(data, distribution_parameters, dim_0_ids, dim_1_ids, operation, distribution)
def _validate_scale_range(params, name)
```

### source/isaaclab/isaaclab/envs/mdp/observations.py

```
"""Common functions that can be used to create observation terms.

The functions can be passed to the :class:`isaaclab.managers.ObservationTermCfg` object to enable
the observation introduced by the function."""
def base_pos_z(env, asset_cfg)
def base_lin_vel(env, asset_cfg)
def base_ang_vel(env, asset_cfg)
def projected_gravity(env, asset_cfg)
def root_pos_w(env, asset_cfg)
def root_quat_w(env, make_quat_unique, asset_cfg)
def root_lin_vel_w(env, asset_cfg)
def root_ang_vel_w(env, asset_cfg)
def body_pose_w(env, asset_cfg)
def body_projected_gravity_b(env, asset_cfg)
def joint_pos(env, asset_cfg)
def joint_pos_rel(env, asset_cfg)
def joint_pos_limit_normalized(env, asset_cfg)
def joint_vel(env, asset_cfg)
def joint_vel_rel(env, asset_cfg)
def joint_effort(env, asset_cfg)
def height_scan(env, sensor_cfg, offset)
def body_incoming_wrench(env, sensor_cfg)
def pva_orientation(env, asset_cfg)
def pva_projected_gravity(env, asset_cfg)
def imu_ang_vel(env, asset_cfg)
def imu_lin_acc(env, asset_cfg)
def image(env, sensor_cfg, data_type, convert_perspective_to_orthogonal, normalize, permute, clone)
class image_features(ManagerTermBase)
    """Extracted image features from a pre-trained frozen encoder.

This term uses models from the model zoo in PyTorch and extracts features from the images.

It calls the :func:`image` function to get the images and then processes them using the model zoo.

A user can provide their own model zoo configur"""
    def __init__(self, cfg, env)
    def reset(self, env_ids)
    def __call__(self, env, sensor_cfg, data_type, convert_perspective_to_orthogonal, model_zoo_cfg, model_name, model_device, inference_kwargs)
    def _prepare_theia_transformer_model(self, model_name, model_device)
    def _prepare_resnet_model(self, model_name, model_device)
class stacked_image(ManagerTermBase)
    """Channel-stacked observation of the last ``frame_stack`` camera frames.

Maintains a per-env rolling history of camera frames in a
:class:`~isaaclab.utils.buffers.CircularBuffer` and returns them concatenated along the
channel dimension in oldest-to-newest order. Useful for camera-based RL tasks whos"""
    def __init__(self, cfg, env)
    def reset(self, env_ids)
    def __call__(self, env, sensor_cfg, data_type, frame_stack, convert_perspective_to_orthogonal, normalize)
def last_action(env, action_name)
def generated_commands(env, command_name)
def current_time_s(env)
def remaining_time_s(env)
```

### source/isaaclab/isaaclab/envs/mdp/recorders/__init__.py

```
"""Various recorder terms that can be used in the environment."""
```

### source/isaaclab/isaaclab/envs/mdp/recorders/recorders.py

```
class InitialStateRecorder(RecorderTerm)
    """Recorder term that records the initial state of the environment after reset."""
    def record_post_reset(self, env_ids)
class PostStepStatesRecorder(RecorderTerm)
    """Recorder term that records the state of the environment at the end of each step."""
    def record_post_step(self)
class PreStepActionsRecorder(RecorderTerm)
    """Recorder term that records the actions in the beginning of each step."""
    def record_pre_step(self)
class PreStepFlatPolicyObservationsRecorder(RecorderTerm)
    """Recorder term that records the policy group observations in each step."""
    def record_pre_step(self)
class PostStepProcessedActionsRecorder(RecorderTerm)
    """Recorder term that records processed actions at the end of each step."""
    def record_post_step(self)
```

### source/isaaclab/isaaclab/envs/mdp/recorders/recorders_cfg.py

```
class InitialStateRecorderCfg(RecorderTermCfg)
    """Configuration for the initial state recorder term."""
class PostStepStatesRecorderCfg(RecorderTermCfg)
    """Configuration for the step state recorder term."""
class PreStepActionsRecorderCfg(RecorderTermCfg)
    """Configuration for the step action recorder term."""
class PreStepFlatPolicyObservationsRecorderCfg(RecorderTermCfg)
    """Configuration for the step policy observation recorder term."""
class PostStepProcessedActionsRecorderCfg(RecorderTermCfg)
    """Configuration for the post step processed actions recorder term."""
class ActionStateRecorderManagerCfg(RecorderManagerBaseCfg)
    """Recorder configurations for recording actions and states."""
```

### source/isaaclab/isaaclab/envs/mdp/rewards.py

```
"""Common functions that can be used to enable reward functions.

The functions can be passed to the :class:`isaaclab.managers.RewardTermCfg` object to include
the reward introduced by the function."""
def is_alive(env)
def is_terminated(env)
class is_terminated_term(ManagerTermBase)
    """Penalize termination for specific terms that don't correspond to episodic timeouts.

The parameters are as follows:

* attr:`term_keys`: The termination terms to penalize. This can be a string, a list of strings
  or regular expressions. Default is ".*" which penalizes all terminations.

The reward """
    def __init__(self, cfg, env)
    def __call__(self, env, term_keys)
def lin_vel_z_l2(env, asset_cfg)
def ang_vel_xy_l2(env, asset_cfg)
def flat_orientation_l2(env, asset_cfg)
def base_height_l2(env, target_height, asset_cfg, sensor_cfg)
def body_lin_acc_l2(env, asset_cfg)
def joint_torques_l2(env, asset_cfg)
def joint_vel_l1(env, asset_cfg)
def joint_vel_l2(env, asset_cfg)
def joint_acc_l2(env, asset_cfg)
def joint_deviation_l1(env, asset_cfg)
def joint_pos_limits(env, asset_cfg)
def joint_vel_limits(env, soft_ratio, asset_cfg)
def applied_torque_limits(env, asset_cfg)
def action_rate_l2(env)
def action_l2(env)
def undesired_contacts(env, threshold, sensor_cfg)
def desired_contacts(env, sensor_cfg, threshold)
def contact_forces(env, threshold, sensor_cfg)
def track_lin_vel_xy_exp(env, std, command_name, asset_cfg)
def track_ang_vel_z_exp(env, std, command_name, asset_cfg)
def position_command_error(env, command_name, asset_cfg)
def position_command_error_tanh(env, std, command_name, asset_cfg)
def orientation_command_error(env, command_name, asset_cfg)
```

### source/isaaclab/isaaclab/envs/mdp/terminations.py

```
"""Common functions that can be used to activate certain terminations.

The functions can be passed to the :class:`isaaclab.managers.TerminationTermCfg` object to enable
the termination introduced by the function."""
def time_out(env)
def command_resample(env, command_name, num_resamples)
def pose_command_success(env, command_name)
def bad_orientation(env, limit_angle, asset_cfg)
def root_height_below_minimum(env, minimum_height, asset_cfg)
def joint_pos_out_of_limit(env, asset_cfg)
def joint_pos_out_of_manual_limit(env, bounds, asset_cfg)
class joint_vel_out_of_limit(ManagerTermBase)
    """Terminate when the asset's joint velocities are outside of the soft joint limits.

The joint indices are materialized as a device tensor once at construction."""
    def __init__(self, cfg, env)
    def __call__(self, env, asset_cfg)
def joint_vel_out_of_manual_limit(env, max_velocity, asset_cfg)
def joint_effort_out_of_limit(env, asset_cfg)
def illegal_contact(env, threshold, sensor_cfg)
```

### source/isaaclab/isaaclab/envs/mdp/visual_events.py

```
"""GPU visual appearance randomization terms."""
class randomize_visual_material(ManagerTermBase)
    """Sample numeric material channels on device and issue one batched runtime renderer write.

This term requires an initialized renderer and therefore does not support ``prestartup`` mode."""
    def __init__(self, cfg, env)
    def __call__(self, env, env_ids, materials, channels)
class randomize_visual_shape(FactoryBase, ManagerTermBase)
    """Randomize visual channels per selected shape on backends that expose shape storage."""
    def _get_backend(cls, cfg, env)
def _compile_distribution(spec, device)
```

### source/isaaclab/isaaclab/envs/mimic_env_cfg.py

```
"""Base MimicEnvCfg object for Isaac Lab Mimic data generation."""
class DataGenConfig()
    """Configuration settings for data generation processes within the Isaac Lab Mimic environment."""
class SubTaskConfig()
    """Configuration settings for specifying subtasks used in Mimic environments."""
class SubTaskConstraintType(IntEnum)
    """Enum for subtask constraint types."""
class SubTaskConstraintCoordinationScheme(IntEnum)
    """Enum for coordination schemes."""
class SubTaskConstraintConfig()
    """Configuration settings for specifying subtask constraints used in multi-eef Mimic environments."""
    def generate_runtime_subtask_constraints(self)
class MimicEnvCfg()
    """Configuration class for the Mimic environment integration.

This class consolidates various configuration aspects for the
Isaac Lab Mimic data generation pipeline."""
```

### source/isaaclab/isaaclab/envs/ui/__init__.py

```
"""Sub-module providing UI window implementation for environments.

The UI elements are used to control the environment and visualize the state of the environment.
This includes functionalities such as tracking a robot in the simulation,
toggling different debug visualization tools, and other user-defined functionalities."""
```

### source/isaaclab/isaaclab/envs/ui/base_env_window.py

```
class BaseEnvWindow()
    """Window manager for the basic environment.

This class creates a window that is used to control the environment. The window
contains controls for rendering, debug visualization, and other environment-specific
UI elements.

Users can add their own UI elements to the window by using the `with` context """
    def __init__(self, env, window_name)
    def __del__(self)
    def _build_sim_frame(self)
    def _build_render_mode_dropdown(self)
    def _build_viewer_frame(self)
    def _build_debug_vis_frame(self)
    def _build_vis_markers_frame(self)
    def _visualize_manager(self, title, class_name)
    def _toggle_recording_animation_fn(self, value)
    def _get_kit_visualizer(self)
    def _set_viewer_origin_type_fn(self, value)
    def _set_viewer_location_fn(self, model)
    def _set_viewer_env_index_fn(self, model)
    def _create_debug_vis_ui_element(self, name, elem)
    def _dock_window(self, window_title)
```

### source/isaaclab/isaaclab/envs/ui/empty_window.py

```
class EmptyWindow()
    """Creates an empty UI window that can be docked in the Omniverse Kit environment.

The class initializes a dockable UI window and provides a main frame with a vertical stack.
You can add custom UI elements to this vertical stack.

Example for adding a UI element from the standalone execution script:
 """
    def __init__(self, env, window_name)
    def __del__(self)
    def _dock_window(self, window_title)
```

### source/isaaclab/isaaclab/envs/ui/manager_based_rl_env_window.py

```
class ManagerBasedRLEnvWindow(BaseEnvWindow)
    """Window manager for the RL environment.

On top of the basic environment window, this class adds controls for the RL environment.
This includes visualization of the command manager."""
    def __init__(self, env, window_name)
```

### source/isaaclab/isaaclab/envs/ui/viewport_camera_controller.py

```
"""Deprecated: ViewportCameraController compatibility shim.

Camera tracking is now built into :class:`~isaaclab_visualizers.kit.KitVisualizer`.
Configure ``eye``, ``lookat``, ``origin_type``, and ``origin_track_path`` directly on
:class:`~isaaclab_visualizers.kit.KitVisualizerCfg` and add it to
:attr:`~isaaclab.sim.SimulationCfg.visualizer_cfgs`."""
def _warn_method(name)
class ViewportCameraController()
    """Deprecated compatibility shim for :class:`ViewportCameraController`.

.. deprecated::
    :class:`ViewportCameraController` has been removed. Camera tracking is now built into
    :class:`~isaaclab_visualizers.kit.KitVisualizer`. Set ``origin_type``,
    ``origin_track_path``, ``eye``, and ``lookat`"""
    def __init__(self, env, cfg)
    def cfg(self)
    def set_view_env_index(self, env_index)
    def update_view_to_world(self)
    def update_view_to_env(self)
    def update_view_to_asset_root(self, asset_name)
    def update_view_to_asset_body(self, asset_name, body_name)
    def update_view_location(self, eye, lookat)
    def _get_kit_visualizers(self)
```

### source/isaaclab/isaaclab/envs/utils/__init__.py

```
"""Sub-package for environment utils."""
```

### source/isaaclab/isaaclab/envs/utils/camera_colorizer.py

```
"""Camera frame colorization utilities for visualizer streaming views."""
def sensor_key_for_gt_type(gt_type, available_keys)
def sensor_keys_for_gt_types(gt_types)
class CameraFrameColorizer()
    """Colorize raw camera sensor frames for streaming display.

Each method accepts a single-env frame tensor ``(H, W, C)`` and returns a
``uint8`` NumPy array with shape ``(H, W, 3)``."""
    def colorize(data, gt_type)
    def _colorize_rgb(data)
    def _colorize_depth(data, depth_min, depth_max)
    def _colorize_segmentation(data)
    def _ids_to_colors(ids)
    def _colorize_normals(data)
    def _fallback_depth_gradient(norm)
def _hsv_to_rgb_uint8(h, s, v)
```

### source/isaaclab/isaaclab/envs/utils/camera_view.py

```
"""Helpers for visualizer and recorder camera image views."""
def resolve_tiled_env_indices(num_envs, streaming_envs, env_indices, max_tiles, sample_from)
def resolve_mono_env_index(num_envs)
def env_path_from_template(path_template, env_id)
def _camera_concrete_paths(camera)
def find_camera_by_prim_path(camera_sensors, cam_prim_path, env_indices)
def ensure_camera_initialized(camera)
def resolve_streaming_envs(num_envs, streaming_envs, max_tiles, sample_from)
def camera_gt_batch(camera, env_indices, sensor_key)
def compose_streaming_grid(frames, n_envs, n_gt, target_aspect)
def _best_streaming_cols(n_envs, n_gt, frame_h, frame_w, target_aspect)
def create_visualizer_camera()
def evict_visualizer_camera(key)
def remove_generated_prims(prim_paths)
def camera_rgb_batch(camera, env_indices)
def compose_rgb_grid_tensor(rgb_batch)
def compute_tile_resolution(window_width, window_height, num_tiles, n_gt)
def _normalize_env0_path(path_template)
def _scene_articulation_positions(scene, prim_path_template, env_indices)
def prim_world_positions(stage, prim_path_template, env_indices, scene)
def apply_camera_view_from_origins(camera, origins, eye, lookat, env_ids)
def apply_camera_target_positions(camera, target_positions, eye, env_ids)
```

### source/isaaclab/isaaclab/envs/utils/io_descriptors.py

```
class GenericActionIODescriptor()
    """Generic action IO descriptor.

This descriptor is used to describe the action space of a policy.
It can be extended as needed to add more information about the action term that is being described."""
class GenericObservationIODescriptor()
    """Generic observation IO descriptor.

This descriptor is used to describe the observation space of a policy.
It can be extended as needed to add more information about the observation term that is being described."""
def _make_descriptor()
def generic_io_descriptor(_func)
def record_shape(output, descriptor)
def record_dtype(output, descriptor)
def record_joint_names(output, descriptor)
def record_body_names(output, descriptor)
def record_joint_pos_offsets(output, descriptor)
def record_joint_vel_offsets(output, descriptor)
def export_articulations_data(env)
def export_scene_data(env)
```

### source/isaaclab/isaaclab/envs/utils/marl.py

```
def multi_agent_to_single_agent(env, state_as_observation)
def multi_agent_with_one_agent(env, state_as_observation)

```python
def _convert_observations(self, obs: dict[AgentID, ObsType]) -> VecEnvObs:
            """Convert multi-agent observations to the single-agent policy observation."""
            # FIXME: This implementation assumes the spaces are fundamental ones. Fix it to support composite spaces
            if self._state_as_observation:
                return {"policy": self.env.state()}
            return {
                "policy": torch.cat(
                    [obs[agent].reshape(self.num_envs, -1) for agent in self.env.possible_agents], dim=-1
                )
            }
```

```python
def observation_spaces(self) -> dict[AgentID, gym.Space]:
            return self._exported_observation_spaces
```
```

### source/isaaclab/isaaclab/envs/utils/spaces.py

```
def spec_to_gym_space(spec)
def sample_space(space, device, batch_size, fill_value)
def serialize_space(space)
def deserialize_space(string)
def replace_env_cfg_spaces_with_strings(env_cfg)
def replace_strings_with_env_cfg_spaces(env_cfg)
```

### source/isaaclab/isaaclab/envs/utils/video_recorder.py

```
"""Step-driven internal video recorder.

Recording is triggered by env.step() calls, not by the Gym render loop.
Frames are sourced from the configured visualizer or scene sensor and written
to mp4 files via moviepy."""
def _parse_source(source)
class VideoRecorder()
    """Records one video stream per :class:`VideoRecorderCfg` entry.

Instantiated by the env base class; ``step()`` is called once per env step
after physics and rendering have completed.

Raises:
    ImportError: If ``moviepy`` is not installed.
    ValueError: If :attr:`~VideoRecorderCfg.source` has an """
    def __init__(self, cfg, env)
    def step(self)
    def close(self)
    def _check_trigger(self, effective_step)
    def _get_frame(self)
    def _frame_from_visualizer(self, viz_type, sub)
    def _frame_from_sensor(self, name, gt_type)
    def _effective_output_dir(self)
    def _clip_path(self, index)
    def _next_clip_index(self)
    def _existing_clip_indices(self)
    def _close_clip(self)
    def _maybe_delete_old_clips(self)
```

### source/isaaclab/isaaclab/envs/utils/video_recorder_cfg.py

```
"""Configuration for video recording from visualizers and scene sensors."""
class VideoRecorderCfg()
    """Configuration for one video recording stream.

A recording stream captures frames from a *source* — either an active visualizer
(interactive or tiled camera) or a named scene sensor — and writes them to an mp4
clip file.  Multiple ``VideoRecorderCfg`` entries on an env cfg produce independent
simult"""
```

### source/isaaclab/isaaclab/managers/action_manager.py

```
"""Action manager for processing actions sent to the environment."""
class ActionTerm(ManagerTermBase)
    """Base class for action terms.

The action term is responsible for processing the raw actions sent to the environment
and applying them to the asset managed by the term. The action term is comprised of two
operations:

* Processing of actions: This operation is performed once per **environment step** """
    def __init__(self, cfg, env)
    def __del__(self)
    def action_dim(self)
    def raw_actions(self)
    def processed_actions(self)
    def has_debug_vis_implementation(self)
    def IO_descriptor(self)
    def export_IO_descriptor(self)
    def set_debug_vis(self, debug_vis)
    def process_actions(self, actions)
    def apply_actions(self)
    def _set_debug_vis_impl(self, debug_vis)
    def _debug_vis_callback(self, event)
class ActionManager(ManagerBase)
    """Manager for processing and applying actions for a given world.

The action manager handles the interpretation and application of user-defined
actions on a given world. It is comprised of different action terms that decide
the dimension of the expected actions.

The action manager performs operations"""
    def __init__(self, cfg, env)
    def __str__(self)
    def total_action_dim(self)
    def active_terms(self)
    def action_term_dim(self)
    def action(self)
    def prev_action(self)
    def has_debug_vis_implementation(self)
    def get_IO_descriptors(self)
    def get_active_iterable_terms(self, env_idx)
    def set_debug_vis(self, debug_vis)
    def reset(self, env_ids)
    def process_action(self, action)
    def apply_action(self)
    def get_term(self, name)
    def serialize(self)
    def _prepare_terms(self)
```

### source/isaaclab/isaaclab/managers/manager_term_cfg.py

```
"""Configuration terms for different managers."""
class ManagerTermBaseCfg()
    """Configuration for a manager term."""
class RecorderTermCfg()
    """Configuration for an recorder term."""
class ActionTermCfg()
    """Configuration for an action term."""
class CommandTermCfg()
    """Configuration for a command generator term."""
class CurriculumTermCfg(ManagerTermBaseCfg)
    """Configuration for a curriculum term."""
class ObservationTermCfg(ManagerTermBaseCfg)
    """Configuration for an observation term."""
class ObservationGroupCfg()
    """Configuration for an observation group."""
class EventTermCfg(ManagerTermBaseCfg)
    """Configuration for a event term."""
class RewardTermCfg(ManagerTermBaseCfg)
    """Configuration for a reward term."""
class TerminationTermCfg(ManagerTermBaseCfg)
    """Configuration for a termination term."""
```

### source/isaaclab/isaaclab/managers/observation_manager.py

```
"""Observation manager for computing observation signals for a given world."""
class ObservationManager(ManagerBase)
    """Manager for computing observation signals for a given world.

Observations are organized into groups based on their intended usage. This allows having different observation
groups for different types of learning such as asymmetric actor-critic and student-teacher training. Each
group contains observ"""
    def __init__(self, cfg, env)
    def __str__(self)
    def get_active_iterable_terms(self, env_idx)
    def active_terms(self)
    def group_obs_dim(self)
    def group_obs_term_dim(self)
    def group_obs_concatenate(self)
    def get_IO_descriptors(self, group_names_to_export)
    def reset(self, env_ids)
    def compute(self, update_history)
    def compute_group(self, group_name, update_history)
    def serialize(self)
    def _prepare_terms(self)
```

### source/isaaclab/isaaclab/managers/reward_manager.py

```
"""Reward manager for computing reward signals for a given world."""
class RewardManager(ManagerBase)
    """Manager for computing reward signals for a given world.

The reward manager computes the total reward as a sum of the weighted reward terms. The reward
terms are parsed from a nested config class containing the reward manger's settings and reward
terms configuration.

The reward terms are parsed fro"""
    def __init__(self, cfg, env)
    def __str__(self)
    def active_terms(self)
    def reset(self, env_ids)
    def compute(self, dt)
    def set_term_cfg(self, term_name, cfg)
    def get_term_cfg(self, term_name)
    def get_active_iterable_terms(self, env_idx)
    def _prepare_terms(self)
```

### source/isaaclab/isaaclab/managers/scene_entity_cfg.py

```
"""Configuration terms for different managers."""
class SceneEntityCfg()
    """Configuration for a scene entity that is used by the manager's term.

This class is used to specify the name of the scene entity that is queried from the
:class:`InteractiveScene` and passed to the manager's term function."""
    def resolve(self, scene)
    def _resolve_joint_names(self, scene)
    def _resolve_fixed_tendon_names(self, scene)
    def _resolve_body_names(self, scene)
    def _resolve_object_collection_names(self, scene)
```

### source/isaaclab/isaaclab/markers/visualization_markers_cfg.py

```
"""Configuration for visualization markers."""
class VisualizationMarkersCfg()
    """A class to configure a :class:`VisualizationMarkers`."""
```

### source/isaaclab/isaaclab/physics/physics_manager_cfg.py

```
"""Base configuration for physics managers."""
class PhysicsCfg()
    """Abstract base configuration for physics managers.

This base class contains physics backend-specific parameters.
Subclasses should override the class_type to return the appropriate
physics manager class.

Shared simulation parameters (dt, gravity, physics_prim_path, physics_material)
are read direct"""
class PhysxAutoCfg(PhysicsCfg)
    """PhysX configuration resolved to a concrete backend at launch."""
def _resolve_physx_auto_cfg(physics_cfg, use_isaac_sim)
```

### source/isaaclab/isaaclab/renderers/renderer_cfg.py

```
"""Base configuration for renderers."""
class RendererCfg()
    """Configuration for a renderer."""
```

### source/isaaclab/isaaclab/scene/interactive_scene_cfg.py

```
class InteractiveSceneCfg()
    """Configuration for the interactive scene.

The users can inherit from this class to add entities to their scene. This is then parsed by the
:class:`InteractiveScene` class to create the scene.

.. note::
    The adding of entities to the scene is sensitive to the order of the attributes in the config"""
def add(target, source)
def _scene_assets(scene_cfg, asset_skip)
```

### source/isaaclab/isaaclab/sensors/camera/camera_cfg.py

```
class CameraCfg(SensorBaseCfg)
    """Configuration for a camera sensor."""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/sensors/camera/tiled_camera_cfg.py

```
class TiledCameraCfg(CameraCfg)
    """Configuration for a tiled rendering-based camera sensor.

.. deprecated:: 4.6.0
    :class:`TiledCameraCfg` is deprecated. Use :class:`CameraCfg` directly —
    :class:`~isaaclab.sensors.camera.Camera` now includes TiledCamera's vectorized
    rendering optimizations via the same renderer abstractio"""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/sensors/contact_sensor/contact_sensor_cfg.py

```
class ContactSensorCfg(SensorBaseCfg)
    """Configuration for the contact sensor.

Sensing bodies are selected via :attr:`SensorBaseCfg.prim_path`. Filter bodies for
per-partner force reporting are selected via :attr:`filter_prim_paths_expr`.

Only body-level sensing and filtering are supported. For shape-level granularity,
see ``NewtonContac"""
```

### source/isaaclab/isaaclab/sensors/frame_transformer/frame_transformer_cfg.py

```
class OffsetCfg()
    """The offset pose of one frame relative to another frame."""
class FrameTransformerCfg(SensorBaseCfg)
    """Configuration for the frame transformer sensor."""
```

### source/isaaclab/isaaclab/sensors/imu/imu_cfg.py

```
class ImuCfg(SensorBaseCfg)
    """Configuration for an Inertial Measurement Unit (IMU) sensor.

This configures a sensor that provides the two physical quantities measured by a
real IMU: angular velocity (gyroscope) and linear acceleration (accelerometer).
For a richer sensor that also provides pose, velocity, and angular accelerati"""
```

### source/isaaclab/isaaclab/sensors/joint_wrench/joint_wrench_sensor_cfg.py

```
class JointWrenchSensorCfg(SensorBaseCfg)
    """Configuration for a joint reaction wrench sensor."""
```

### source/isaaclab/isaaclab/sensors/pva/pva_cfg.py

```
class PvaCfg(SensorBaseCfg)
    """Configuration for a Pose Velocity Acceleration (PVA) sensor."""
```

### source/isaaclab/isaaclab/sensors/ray_caster/multi_mesh_ray_caster_camera_cfg.py

```
"""Configuration for the ray-cast camera sensor."""
class MultiMeshRayCasterCameraCfg(RayCasterCameraCfg, MultiMeshRayCasterCfg)
    """Configuration for the multi-mesh ray-cast camera sensor."""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/sensors/ray_caster/multi_mesh_ray_caster_cfg.py

```
"""Configuration for the ray-cast sensor."""
class MultiMeshRayCasterCfg(RayCasterCfg)
    """Configuration for the multi-mesh ray-cast sensor."""
```

### source/isaaclab/isaaclab/sensors/ray_caster/patterns/patterns_cfg.py

```
"""Configuration for the ray-cast sensor."""
class PatternBaseCfg()
    """Base configuration for a pattern."""
class GridPatternCfg(PatternBaseCfg)
    """Configuration for the grid pattern for ray-casting.

Defines a 2D grid of rays in the coordinates of the sensor.

.. attention::
    The points are ordered based on the :attr:`ordering` attribute."""
class PinholeCameraPatternCfg(PatternBaseCfg)
    """Configuration for a pinhole camera depth image pattern for ray-casting.

.. caution::
    Focal length as well as the aperture sizes and offsets are set as a tenth of the world unit. In our case, the
    world unit is meters, so all of these values are in cm. For more information, please check:
    """
    def from_intrinsic_matrix(cls, intrinsic_matrix, width, height, focal_length)
class BpearlPatternCfg(PatternBaseCfg)
    """Configuration for the Bpearl pattern for ray-casting."""
class LidarPatternCfg(PatternBaseCfg)
    """Configuration for the LiDAR pattern for ray-casting."""
```

### source/isaaclab/isaaclab/sensors/ray_caster/ray_caster_camera_cfg.py

```
"""Configuration for the ray-cast camera sensor."""
class RayCasterCameraCfg(RayCasterCfg)
    """Configuration for the ray-cast sensor."""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/sensors/ray_caster/ray_caster_cfg.py

```
"""Configuration for the ray-cast sensor."""
class RayCasterCfg(SensorBaseCfg)
    """Configuration for the ray-cast sensor."""
```

### source/isaaclab/isaaclab/sensors/sensor_base_cfg.py

```
class SensorBaseCfg()
    """Configuration parameters for a sensor."""
```

### source/isaaclab/isaaclab/sim/__init__.py

```
"""Sub-package containing simulation-specific functionalities.

These include:

* Ability to spawn different objects and materials into Omniverse
* Define and modify various schemas on USD prims
* Converters to obtain USD file from other file formats (such as URDF, OBJ, STL, FBX)
* Utility class to control the simulator

.. note::
    Currently, only a subset of all possible schemas and prims in Omniverse are supported.
    We are expanding the these set of functions on a need basis. In case, there are
    specific prims or schemas that you would like to include, please open an issue on GitHub
  """
def __getattr__(name)
def __dir__()
```

### source/isaaclab/isaaclab/sim/converters/__init__.py

```
"""Sub-module containing converters for converting various file types to USD.

In order to support direct loading of various file types into Omniverse, we provide a set of
converters that can convert the file into a USD file. The converters are implemented as
sub-classes of the :class:`AssetConverterBase` class.

The following converters are currently supported:

* :class:`UrdfConverter`: Converts a URDF file into a USD file.
* :class:`MeshConverter`: Converts a mesh file into a USD file. This supports OBJ, STL and FBX files."""
```

### source/isaaclab/isaaclab/sim/converters/asset_converter_base.py

```
class AssetConverterBase(ABC)
    """Base class for converting an asset file from different formats into USD format.

This class provides a common interface for converting an asset file into USD. It does not
provide any implementation for the conversion. The derived classes must implement the
:meth:`_convert_asset` method to provide th"""
    def __init__(self, cfg)
    def usd_dir(self)
    def usd_file_name(self)
    def usd_path(self)
    def usd_instanceable_meshes_path(self)
    def _convert_asset(self, cfg)
    def _select_physics_variant(self, variant)
    def _config_to_hash(cfg)
```

### source/isaaclab/isaaclab/sim/converters/asset_converter_base_cfg.py

```
class AssetConverterBaseCfg()
    """The base configuration class for asset converters."""
```

### source/isaaclab/isaaclab/sim/converters/mesh_converter.py

```
class MeshConverter(AssetConverterBase)
    """Converter for a mesh file in OBJ / STL / FBX format to a USD file.

This class wraps around the `omni.kit.asset_converter`_ extension to provide a lazy implementation
for mesh to USD conversion. It stores the output USD file in an instanceable format since that is
what is typically used in all learn"""
    def __init__(self, cfg)
    def _convert_asset(self, cfg)
    def _convert_mesh_to_usd(in_file, out_file, load_materials)
```

### source/isaaclab/isaaclab/sim/converters/mesh_converter_cfg.py

```
class MeshConverterCfg(AssetConverterBaseCfg)
    """The configuration class for MeshConverter."""
```

### source/isaaclab/isaaclab/sim/converters/mjcf_converter.py

```
class MjcfConverter(AssetConverterBase)
    """Converter for a MJCF description file to a USD file.

This class wraps around the `isaacsim.asset.importer.mjcf`_ API to provide a lazy
implementation for MJCF to USD conversion. When the full Isaac Sim runtime is available,
the Isaac Sim MJCF importer extension is enabled and used; otherwise, the A"""
    def __init__(self, cfg)
    def _convert_asset(self, cfg)
```

### source/isaaclab/isaaclab/sim/converters/mjcf_converter_cfg.py

```
class MjcfConverterCfg(AssetConverterBaseCfg)
    """The configuration class for MjcfConverter.

Maps to :class:`~isaacsim.asset.importer.mjcf.MJCFImporterConfig` from the Isaac Sim
MJCF importer. All post-import USD edits (fix-base, density override, actuator gain
overrides, self-collision, mesh merging, asset transformer profile) are performed by
th"""
```

### source/isaaclab/isaaclab/sim/converters/urdf_converter.py

```
class UrdfConverter(AssetConverterBase)
    """Converter for a URDF description file to a USD file.

This class wraps around the `isaacsim.asset.importer.urdf`_ API to provide a lazy
implementation for URDF to USD conversion. When the full Isaac Sim runtime is available,
the Isaac Sim URDF importer extension is enabled and used; otherwise, the A"""
    def __init__(self, cfg)
    def _convert_asset(self, cfg)
    def _warn_unsupported_features(cfg)
    def _unpack_joint_drive(joint_drive)
```

### source/isaaclab/isaaclab/sim/converters/urdf_converter_cfg.py

```
class UrdfConverterCfg(AssetConverterBaseCfg)
    """The configuration class for UrdfConverter.

Maps to :class:`~isaacsim.asset.importer.urdf.URDFImporterConfig` from the Isaac Sim
URDF importer. IsaacLab exposes a user-friendly nested :class:`JointDriveCfg` that is
translated into the importer's flat ``joint_drive_type`` / ``joint_target_type`` /
``"""
```

### source/isaaclab/isaaclab/sim/schemas/__init__.py

```
"""Sub-module containing utilities for schemas used in Omniverse.

We wrap the USD schemas for PhysX and USD Physics in a more convenient API for setting the parameters from
Python. This is done so that configuration objects can define the schema properties to set and make it easier
to tune the physics parameters without requiring to open Omniverse Kit and manually set the parameters into
the respective USD attributes.

.. caution::

    Schema properties cannot be applied on prims that are prototypes as they are read-only prims. This
    particularly affects instanced assets where some of the pr"""
def __getattr__(name)
def __dir__()
```

### source/isaaclab/isaaclab/sim/schemas/_backend_hooks.py

```
"""Backend registration hooks for schema writers.

This module holds the inversion-of-control registries that let physics backends (e.g.
``isaaclab_physx``, ``isaaclab_newton``) inject backend-specific behaviour into the core schema
writers without core importing any backend. It is deliberately kept free of ``pxr``/``omni`` imports
so a backend can register its hook at package-import time without eagerly pulling USD libraries into
an otherwise USD-free import path."""
def register_joint_drive_skip_predicate(predicate)
def _skip_joint_drive(prim)
def register_articulation_root_companion(schema_name, namespace)
def _articulation_root_companion_namespace(schema_name)
```

### source/isaaclab/isaaclab/sim/schemas/schemas.py

```
def _get_physx_mesh_collision_cfgs()
class _LazyList()
    """Lazy list whose contents are produced on first access.

Used to keep the public ``PHYSX_MESH_COLLISION_CFGS`` / ``USD_MESH_COLLISION_CFGS`` symbols
resolvable for callers that imported them, without triggering an ``isaaclab_physx`` import
at this module's load time."""
    def __init__(self, factory)
    def _resolved(self)
    def __iter__(self)
    def __contains__(self, item)
    def __len__(self)
    def __getitem__(self, index)
def _get_field_declaring_class(cfg_class, field_name)
def _apply_namespaced_schemas(prim, cfg, cfg_dict)
def apply_namespaced(cfg, prim_path, stage)
def apply_articulation_root_properties(prim_path_expr, fragments, stage, fix_root_link, create_if_missing)
def define_articulation_root_properties(prim_path, cfg, stage)
def create_world_fixed_joint(articulation_prim, stage)
def modify_articulation_root_properties(prim_path, cfg, stage)
def _match_fragment_targets(prim_path_expr, is_target, stage)
def apply_rigid_body_properties(prim_path_expr, fragments, create_if_missing, stage)
def apply_mesh_collision(cfg, prim_path, stage)
def apply_mesh_collision_properties(prim_path, fragments, stage)
def define_rigid_body_properties(prim_path, cfg, stage)
def modify_rigid_body_properties(prim_path, cfg, stage)
def apply_collision_properties(prim_path_expr, fragments, create_if_missing, stage)
def define_collision_properties(prim_path, cfg, stage)
def modify_collision_properties(prim_path, cfg, stage)
def apply_mass_properties(prim_path_expr, fragments, create_if_missing, stage)
def define_mass_properties(prim_path, cfg, stage)
def modify_mass_properties(prim_path, cfg, stage)
def activate_contact_sensors(prim_path, threshold, stage)
def _drive_instance_name(prim)
def apply_drive(cfg, prim_path, stage)
def apply_joint_drive_properties(prim_path_expr, fragments, stage, ensure_drives_exist, create_if_missing)
def _ensure_drive_exists(drive_cfg, prim)
def modify_joint_drive_properties(prim_path, cfg, stage)
def _write_tendon_properties(prim, values, schema_type)
def _apply_tendon_fragments(prim_path_expr, fragments, schema_types, prim_types, family, stage)
def apply_fixed_tendon_properties(prim_path_expr, fragments, stage)
def modify_fixed_tendon_properties(prim_path, cfg, stage)
def apply_spatial_tendon_properties(prim_path_expr, fragments, stage)
def modify_spatial_tendon_properties(prim_path, cfg, stage)
def define_mesh_collision_properties(prim_path, cfg, stage)
def modify_mesh_collision_properties(prim_path, cfg, stage)
def _fix_tet_winding_kernel(points, tet_indices)
def define_deformable_curve_properties(prim_path, stage)
def define_deformable_body_properties(prim_path, cfg, stage, deformable_type, sim_mesh_prim_path, tetrahedralization_edge_length_fac)
def modify_deformable_body_properties(prim_path, cfg, stage)
```

### source/isaaclab/isaaclab/sim/schemas/schemas_actuators.py

```
"""USD schema authoring for Newton-native actuators.

:func:`define_actuator_properties` translates IsaacLab actuator configs
into ``NewtonActuator`` USD prims. Both the Newton ``ModelBuilder.add_usd``
path and the PhysX adapter's
:meth:`~isaaclab.actuators.newton.adapter.NewtonActuatorAdapter.from_usd`
read the same authored prims, ensuring both backends construct
:class:`~newton.actuators.Actuator` instances with matching parameters.

This module lives on the schema side so that authoring is a regular
``define_*_properties`` step in the spawner pipeline, alongside
:func:`define_articulation_roo"""
def _resolve_actuator_class(class_type)
def _is_newton_native_actuator_cfg(cfg)
def _validate_newton_native_actuator_cfgs(actuator_cfgs)
def resolve_per_dof(value, joint_names, cast)
def define_actuator_properties(prim_path, actuator_cfgs, stage)
def _author_actuator_prims(stage, articulation_prim_path, actuator_cfgs)
def _snake_to_camel(name)
def _get_authored_joint_effort_limit(stage, joint_prim_path)
def _collect_joint_prims(art_prim)
def _remove_actuator_prims_for_joints(art_prim, joint_paths)
def _resave_checkpoint_with_metadata(original_path, metadata)
```

### source/isaaclab/isaaclab/sim/schemas/schemas_cfg.py

```
def __getattr__(name)
def _deprecate_field_alias(cfg, alias, canonical)
class SchemaFragment()
    """Base for a single-namespace USD-schema config fragment.

Each subclass mirrors exactly one USD applied schema. The fragment carries class-level
metadata describing which USD namespace its fields write to (:attr:`_usd_namespace`) and
which applied schema, if any, it owns (:attr:`_usd_applied_schema`)"""
class RigidBodyFragment(SchemaFragment)
    """Marker base for rigid-body fragments; types the ``rigid_props`` slot."""
class UsdPhysicsRigidBodyCfg(RigidBodyFragment)
    """``physics:*`` rigid-body attributes from `UsdPhysics.RigidBodyAPI`_.

The ``UsdPhysics.RigidBodyAPI`` schema is applied as the implicit anchor by the rigid-body
family writer, so this fragment owns no applied schema of its own.

.. _UsdPhysics.RigidBodyAPI: https://openusd.org/dev/api/class_usd_phys"""
class CollisionFragment(SchemaFragment)
    """Marker base for collision fragments; types the ``collision_props`` slot."""
class ArticulationRootFragment(SchemaFragment)
    """Marker base for articulation-root fragments; types the ``articulation_props`` slot.

Articulation-root fragments author backend-specific articulation properties (solver
iterations, sleep / stabilization thresholds, self-collision toggles). The defining
``UsdPhysics.ArticulationRootAPI`` anchor is ap"""
class JointDriveFragment(SchemaFragment)
    """Marker base for joint-drive fragments; types the ``joint_drive_props`` slot."""
class MeshCollisionFragment(SchemaFragment)
    """Marker base for mesh-collision fragments; types the ``mesh_collision_props`` slot.

A mesh-collision concept is split across one *core* fragment carrying the standard
``physics:approximation`` token (:class:`UsdPhysicsMeshCollisionCfg`) and one cooking
fragment per backend cooking schema (PhysX conv"""
class FixedTendonFragment(SchemaFragment)
    """Marker base for fixed-tendon fragments; types the ``fixed_tendons_props`` slot.

Fixed tendons are a *tune-not-apply* family: the applied ``PhysxTendonAxisRootAPI`` and
``PhysxTendonAxisAPI`` instances already exist on joint prims (authored in the source asset),
so the family writer (:func:`~isaacla"""
class SpatialTendonFragment(SchemaFragment)
    """Marker base for spatial-tendon fragments; types the ``spatial_tendons_props`` slot.

Spatial tendons are a *tune-not-apply* family: the applied
``PhysxTendonAttachmentRootAPI`` instances already exist on the prim (authored in the source
asset), so the family writer (:func:`~isaaclab.sim.schemas.appl"""
class UsdPhysicsCollisionCfg(CollisionFragment)
    """``physics:*`` collision attributes from `UsdPhysics.CollisionAPI`_.

The ``UsdPhysics.CollisionAPI`` schema is applied as the implicit anchor by the collision
family writer (:func:`~isaaclab.sim.schemas.apply_collision_properties`), so this fragment
owns no applied schema of its own.

.. _UsdPhysics"""
class UsdPhysicsDriveCfg(JointDriveFragment)
    """``drive:<linear|angular>:physics:*`` joint-drive attributes from `UsdPhysics.DriveAPI`_.

The drive attributes live under a multi-instance ``UsdPhysics.DriveAPI`` (instance
``"angular"`` for revolute joints, ``"linear"`` for prismatic joints), so this fragment
cannot use the generic :func:`~isaaclab"""
    def __post_init__(self)
class UsdPhysicsMeshCollisionCfg(MeshCollisionFragment)
    """``physics:approximation`` mesh-collision token from `UsdPhysics.MeshCollisionAPI`_.

Carries the standard mesh-collision approximation token (:attr:`mesh_approximation_name`
written to ``physics:approximation``). The ``UsdPhysics.MeshCollisionAPI`` schema is applied
as the implicit anchor by the mes"""
class ArticulationRootBaseCfg()
    """Solver-common properties to apply to the root of an articulation.

Carries :attr:`fix_root_link` (writer-side; materializes a
:class:`UsdPhysics.FixedJoint` between the world frame and the root link) and
:attr:`articulation_enabled` whose only USD path today is the PhysX-namespaced
``physxArticulati"""
class RigidBodyBaseCfg()
    """Solver-common properties to apply to a rigid body.

Contains properties from the `UsdPhysics.RigidBodyAPI`_ that are common across all
simulation backends, plus :attr:`disable_gravity` whose USD attribute today is
PhysX-namespaced but whose semantics (per-body gravity exclusion) are universal:
PhysX"""
class CollisionBaseCfg()
    """Solver-common properties to apply to colliders.

Contains :attr:`collision_enabled` from the `UsdPhysics.CollisionAPI`_ and the
:attr:`contact_offset` / :attr:`rest_offset` knobs whose USD attributes today are
PhysX-namespaced (``physxCollision:contactOffset``, ``physxCollision:restOffset``)
but who"""
class MassPropertiesCfg()
    """Properties to define explicit mass properties of a rigid body.

See :meth:`modify_mass_properties` for more information.

.. note::
    If the values are None, they are not modified. This is useful when you want to set only a subset of
    the properties and leave the rest as-is."""
class MassFragment(SchemaFragment)
    """Marker base for mass fragments; types the ``mass_props`` slot."""
class MassCfg(MassFragment)
    """``physics:*`` mass attributes from `UsdPhysics.MassAPI`_.

The ``UsdPhysics.MassAPI`` schema is applied as the implicit anchor by the mass family writer
(:func:`~isaaclab.sim.schemas.apply_mass_properties`), so this fragment owns no applied schema
of its own. Mirrors the legacy :class:`MassPropertie"""
class JointDriveBaseCfg()
    """Solver-common properties to define the drive mechanism of a joint.

Contains properties from the `UsdPhysics.DriveAPI`_ that are common across all
simulation backends, plus :attr:`max_joint_velocity` whose USD attribute today is
PhysX-namespaced but whose semantics (per-DOF velocity limit) are unive"""
    def __post_init__(self)
class MeshCollisionBaseCfg()
    """Solver-common properties to apply to a mesh in regards to collision.

Carries only the standard ``UsdPhysics:MeshCollisionAPI`` token
(:attr:`mesh_approximation_name` -> ``physics:approximation``). For PhysX-cooking
tunables (convex hull / decomposition / triangle mesh / SDF), use the
``Physx*Proper"""
    def __getattr__(self, name)
class BoundingCubePropertiesCfg(MeshCollisionBaseCfg)
    """Bounding-cube mesh collision approximation. USD-only; authors no PhysX schema.

Writes the ``boundingCube`` token to ``physics:approximation`` via
:class:`UsdPhysics.MeshCollisionAPI`.

Original USD Documentation:
https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/class_usd_ph"""
class BoundingSpherePropertiesCfg(MeshCollisionBaseCfg)
    """Bounding-sphere mesh collision approximation. USD-only; authors no PhysX schema.

Writes the ``boundingSphere`` token to ``physics:approximation`` via
:class:`UsdPhysics.MeshCollisionAPI`.

Original USD Documentation:
https://docs.omniverse.nvidia.com/kit/docs/omni_usd_schema_physics/latest/class_us"""
class DeformableBodyPropertiesBaseCfg()
    """Base deformable body properties for backend-specific extensions.

This class is currently empty. It will be populated once the USD deformable
schemas can be unified more cleanly between physics backends."""
```

### source/isaaclab/isaaclab/sim/simulation_cfg.py

```
"""Base configuration of the environment.

This module defines the general configuration of the environment. It includes parameters for
configuring the environment instances, viewer settings, and simulation parameters."""
class SimulationCfg()
    """Configuration for simulation physics.

This class contains the main simulation parameters including physics time-step, gravity,
device settings, and physics backend configuration."""
```

### source/isaaclab/isaaclab/sim/simulation_context.py

```
def _resolve_physics_cfg(physics_cfg, use_isaac_sim)
class SettingsHelper()
    """Helper for typed settings access via SettingsManager."""
    def __init__(self, settings)
    def set(self, name, value)
    def get(self, name)
class SimulationContext()
    """Controls simulation lifecycle including physics stepping and rendering.

This singleton class manages:

* Physics configuration (time-step, solver parameters via :class:`isaaclab.sim.SimulationCfg`)
* Simulation state (play, pause, step, stop)
* Rendering and visualization

The singleton instance ca"""
    def __new__(cls, cfg)
    def instance(cls)
    def __init__(self, cfg)
    def _init_usd_physics_scene(self)
    def physics_sim_view(self)
    def device(self)
    def backend(self)
    def has_gui(self)
    def has_offscreen_render(self)
    def has_active_visualizers(self)
    def is_headless_or_exist_active_visualizer(self)
    def require_visual_shapes(self)
    def visual_shapes_required(self)
    def can_render_rgb_array(self)
    def is_rendering(self)
    def get_physics_dt(self)
    def get_physics_step_count(self)
    def render_context(self)
    def render_generation(self)
    def _create_default_visualizer_configs(self, requested_visualizers)
    def _apply_default_visualizer_cfg(self, cfg)
    def _get_cli_visualizer_types(self)
    def _apply_visualizer_cli_overrides(self, visualizer_cfgs)
    def _is_cli_visualizer_explicit(self)
    def _is_cli_visualizer_disable_all(self)
    def resolve_visualizer_types(self)
    def _has_continuous_visualizers(self)
    def _resolve_visualizer_cfgs(self)
    def initialize_visualizers(self)
    def _get_visualizer_cfgs(self)
    def _initialize_visualizers(self, config_filter)
    def get_scene_data_provider(self)
    def register_interactive_scene(self, scene)
    def get_clone_plan(self)
    def set_clone_plan(self, plan)
    def visualizers(self)
    def get_rendering_dt(self)
    def set_camera_view(self, eye, target)
    def add_render_callback(self, name, fn, order)
    def remove_render_callback(self, name)
    def forward(self)
    def _prepare_newton_visualizer_for_capture(self, _payload)
    def _requires_pre_capture_newton_init(cfg)
    def reset(self, soft)
    def step(self, render)
    def render(self, mode, skip_app_pumping)
    def update_visualizers(self, dt, skip_app_pumping)
    def _should_forward_before_visualizer_update(self)
    def play(self)
    def pause(self)
    def stop(self)
    def request_reset(self)
    def consume_reset_request(self)
    def is_playing(self)
    def is_stopped(self)
    def set_setting(self, name, value)
    def get_setting(self, name)
    def get_or_create_backend(self, backend_type)
    def clear_instance(cls)
    def clear_stage(cls)
def build_simulation_context(create_new_stage, gravity_enabled, device, dt, sim_cfg, add_ground_plane, add_lighting, auto_add_lighting, visualizers)
```

### source/isaaclab/isaaclab/sim/spawners/__init__.py

```
"""Sub-module containing utilities for creating prims in Omniverse.

Spawners are used to create prims into Omniverse simulator. At their core, they are calling the
USD Python API or Omniverse Kit Commands to create prims. However, they also provide a convenient
interface for creating prims from their respective config classes.

There are two main ways of using the spawners:

1. Using the function from the module

   .. code-block:: python

    import isaaclab.sim as sim_utils
    from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

    # spawn from USD file
    cfg = sim_utils.UsdFileCfg(usd_"""
```

### source/isaaclab/isaaclab/sim/spawners/_utils.py

```
"""Private helpers shared by the spawner implementations."""
def props_expr(prim_path, pattern)
def fragment_mapping(value, default_pattern)
def bare_fragments(value)
def subtree_carries_api(prim_path, api_type, stage)
```

### source/isaaclab/isaaclab/sim/spawners/from_files/__init__.py

```
"""Sub-module for spawners that spawn assets from files.

Currently, the following spawners are supported:

* :class:`UsdFileCfg`: Spawn an asset from a USD file.
* :class:`UrdfFileCfg`: Spawn an asset from a URDF file.
* :class:`GroundPlaneCfg`: Spawn a ground plane using the grid-world USD file."""
```

### source/isaaclab/isaaclab/sim/spawners/from_files/from_files.py

```
def spawn_from_usd(prim_path, cfg, translation, orientation)
def spawn_from_urdf(prim_path, cfg, translation, orientation)
def spawn_from_mjcf(prim_path, cfg, translation, orientation)
def spawn_ground_plane(prim_path, cfg, translation, orientation)
def _body_family_targeting(value, prim_path, api_type)
def _apply_body_schema_properties(prim_path, cfg)
def _apply_articulation_schema_properties(prim_path, cfg)
def _spawn_from_usd_file(prim_path, usd_path, cfg, translation, orientation)
def spawn_from_usd_with_compliant_contact_material(prim_path, cfg, translation, orientation)
```

### source/isaaclab/isaaclab/sim/spawners/from_files/from_files_cfg.py

```
class FileCfg(RigidObjectSpawnerCfg, DeformableObjectSpawnerCfg)
    """Configuration parameters for spawning an asset from a file.

This class is a base class for spawning assets from files. It includes the common parameters
for spawning assets from files, such as the path to the file and the function to use for spawning
the asset.

Note:
    By default, all properties"""
class UsdFileCfg(FileCfg)
    """USD file to spawn asset from.

USD files are imported directly into the scene. However, given their complexity, there are various different
operations that can be performed on them. For example, selecting variants, applying materials, or modifying
existing properties.

To prevent the explosion of co"""
class UrdfFileCfg(FileCfg, UrdfConverterCfg)
    """URDF file to spawn asset from.

It uses the :class:`UrdfConverter` class to create a USD file from URDF and spawns the imported
USD file. Similar to the :class:`UsdFileCfg`, the generated USD file can be modified by specifying
the respective properties in the configuration class.

See :meth:`spawn_f"""
class MjcfFileCfg(FileCfg, MjcfConverterCfg)
    """MJCF file to spawn asset from.

It uses the :class:`MjcfConverter` class to create a USD file from MJCF and spawns the imported
USD file. Similar to the :class:`UsdFileCfg`, the generated USD file can be modified by specifying
the respective properties in the configuration class.

See :meth:`spawn_f"""
class UsdFileWithCompliantContactCfg(UsdFileCfg)
    """Configuration for spawning a USD asset with compliant contact physics material.

This class extends :class:`UsdFileCfg` to support applying compliant contact properties
(stiffness and damping) to specific prims in the spawned asset. It uses the
:meth:`spawn_from_usd_with_compliant_contact_material` """
class GroundPlaneCfg(SpawnerCfg)
    """Create a ground plane prim.

This uses Isaac Lab's metric checker ground plane with NVIDIA-green landmarks by default."""
```

### source/isaaclab/isaaclab/sim/spawners/lights/__init__.py

```
"""Sub-module for spawners that spawn lights in the simulation.

There are various different kinds of lights that can be spawned into the USD stage.
Please check the Omniverse documentation for `lighting overview
<https://docs.omniverse.nvidia.com/materials-and-rendering/latest/lighting.html>`_."""
```

### source/isaaclab/isaaclab/sim/spawners/lights/lights.py

```
def spawn_light(prim_path, cfg, translation, orientation)
```

### source/isaaclab/isaaclab/sim/spawners/lights/lights_cfg.py

```
class LightCfg(SpawnerCfg)
    """Configuration parameters for creating a light in the scene.

Please refer to the documentation on `USD LuxLight <https://openusd.org/dev/api/class_usd_lux_light_a_p_i.html>`_
for more information.

.. note::
    The default values for the attributes are those specified in the their official document"""
class DiskLightCfg(LightCfg)
    """Configuration parameters for creating a disk light in the scene.

A disk light is a light source that emits light from a disk. It is useful for simulating
fluorescent lights. For more information, please refer to the documentation on
`USDLux DiskLight <https://openusd.org/dev/api/class_usd_lux_disk_"""
class DistantLightCfg(LightCfg)
    """Configuration parameters for creating a distant light in the scene.

A distant light is a light source that is infinitely far away, and emits parallel rays of light.
It is useful for simulating sun/moon light. For more information, please refer to the documentation on
`USDLux DistantLight <https://o"""
class DomeLightCfg(LightCfg)
    """Configuration parameters for creating a dome light in the scene.

A dome light is a light source that emits light inwards from all directions. It is also possible to
attach a texture to the dome light, which will be used to emit light. For more information, please refer
to the documentation on `USDL"""
class CylinderLightCfg(LightCfg)
    """Configuration parameters for creating a cylinder light in the scene.

A cylinder light is a light source that emits light from a cylinder. It is useful for simulating
fluorescent lights. For more information, please refer to the documentation on
`USDLux CylinderLight <https://openusd.org/dev/api/cla"""
class SphereLightCfg(LightCfg)
    """Configuration parameters for creating a sphere light in the scene.

A sphere light is a light source that emits light outward from a sphere. For more information,
please refer to the documentation on
`USDLux SphereLight <https://openusd.org/dev/api/class_usd_lux_sphere_light.html>`_.

.. note::
    """
```

### source/isaaclab/isaaclab/sim/spawners/materials/__init__.py

```
"""Sub-module for spawners that spawn USD-based and PhysX-based materials.

`Materials`_ are used to define the appearance and physical properties of objects in the simulation.
In Omniverse, they are defined using NVIDIA's `Material Definition Language (MDL)`_. MDL is based on
the physically-based rendering (PBR) model, which is a set of equations that describe how light
interacts with a surface. The PBR model is used to create realistic-looking materials.

While MDL is primarily used for defining the appearance of objects, it can be extended to define
the physical properties of objects. For exam"""
def __getattr__(name)
def __dir__()
```

### source/isaaclab/isaaclab/sim/spawners/materials/physics_materials.py

```
def spawn_rigid_body_material_from_fragments(prim_path, fragments, stage)
def spawn_physics_material(prim_path, material, stage)
def spawn_rigid_body_material(prim_path, cfg)
def spawn_deformable_body_material(prim_path, cfg)
```

### source/isaaclab/isaaclab/sim/spawners/materials/physics_materials_cfg.py

```
def __getattr__(name)
class PhysicsMaterialCfg()
    """Configuration parameters for creating a physics material.

Physics materials are USD schemas applied to a material prim to define the physical properties
related to the material. For example, the friction coefficient, restitution coefficient, etc.
Subclasses author the schema of a specific backend, """
class CableMaterialCfg(PhysicsMaterialCfg)
    """Physics material parameters for deformable curves."""
    def validate_config(self)
class RigidBodyMaterialBaseCfg(PhysicsMaterialCfg)
    """Solver-common physics-material parameters for rigid bodies.

Contains the friction, restitution, and density fields from the `UsdPhysics.MaterialAPI`_ that
are common across all simulation backends. For properties in the ``physxMaterial`` namespace
(compliant-contact spring and combine modes), use
:"""
class RigidBodyMaterialFragment(SchemaFragment)
    """Marker base for rigid-body physics-material fragments; types the ``physics_material`` slot.

A rigid-body physics material is a single ``UsdShade.Material`` prim that carries one or more
physics-material schemas. The fragments author single namespaces onto that prim: the
solver-common ``physics:*`` """
class UsdPhysicsRigidBodyMaterialCfg(RigidBodyMaterialFragment)
    """``physics:*`` rigid-body material attributes from `UsdPhysics.MaterialAPI`_.

The ``UsdPhysics.MaterialAPI`` schema is applied as the implicit anchor by the rigid-body material
family writer, so this fragment owns no applied schema of its own. ``None`` fields are left
unchanged on the material prim."""
class DeformableBodyMaterialBaseCfg(PhysicsMaterialCfg)
    """Base physics material parameters for volume deformable bodies.

Backend-specific subclasses provide the material fields and spawning function
through :attr:`func`."""
class SurfaceDeformableBodyMaterialBaseCfg(DeformableBodyMaterialBaseCfg)
    """Base physics material parameters for surface deformable bodies."""
```

### source/isaaclab/isaaclab/sim/spawners/materials/visual_materials.py

```
def spawn_preview_surface(prim_path, cfg, translation, orientation)
def spawn_from_mdl_file(prim_path, cfg, translation, orientation)
def _author_cfg_inputs(prim, cfg)
```

### source/isaaclab/isaaclab/sim/spawners/materials/visual_materials_cfg.py

```
class VisualMaterialCfg(SpawnerCfg)
    """Configuration parameters for creating a visual material."""
class PreviewSurfaceCfg(VisualMaterialCfg)
    """Configuration parameters for creating a preview surface.

See :meth:`spawn_preview_surface` for more information."""
class MdlFileCfg(VisualMaterialCfg)
    """Configuration parameters for loading an MDL material from a file.

See :meth:`spawn_from_mdl_file` for more information."""
class PbrMdlCfg(MdlFileCfg)
    """Configuration parameters for the OmniPBR MDL material."""
class GlassMdlCfg(VisualMaterialCfg)
    """Configuration parameters for loading a glass MDL material.

This is a convenience class for loading a glass MDL material. For more information on
glass materials, see the `documentation <https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html#omniglass>`__.

.. note::
    The"""
```

### source/isaaclab/isaaclab/sim/spawners/sensors/__init__.py

```
"""Sub-module for spawners that spawn sensors in the simulation.

Currently, the following sensors are supported:

* Camera: A USD camera prim with settings for pinhole or fisheye projections, optionally carrying an
  OpenCV lens-distortion calibration."""
```

### source/isaaclab/isaaclab/sim/spawners/sensors/sensors.py

```
def _author_opencv_distortion(prim, cfg)
def spawn_camera(prim_path, cfg, translation, orientation)
def spawn_sensor_frame(prim_path, cfg, translation, orientation)
```

### source/isaaclab/isaaclab/sim/spawners/sensors/sensors_cfg.py

```
class OpenCvDistortionCfg()
    """Base configuration for an OpenCV lens-distortion model carried on a camera cfg.

The distortion model is renderer-agnostic: it is stored on the camera spawn configuration
and each renderer decides how to consume it. Under the RTX/OVRTX renderer the fields are
authored as the ``omni:lensdistortion:*`"""
class OpenCvPinholeDistortionCfg(OpenCvDistortionCfg)
    """OpenCV pinhole lens-distortion model (radial, tangential and thin-prism terms).

Corresponds to ``OmniLensDistortionOpenCvPinholeAPI`` under the RTX/OVRTX renderer. The full
coefficient set of the OpenCV rational model is exposed; unused coefficients default to zero."""
class OpenCvFisheyeDistortionCfg(OpenCvDistortionCfg)
    """OpenCV fisheye lens-distortion model.

Corresponds to ``OmniLensDistortionOpenCvFisheyeAPI`` under the RTX/OVRTX renderer.

See Also:
    :class:`FisheyeCameraCfg` for the USD ``fisheyePolynomial`` projection, an alternative fisheye
    model authored directly on the camera rather than as an OpenCV """
class PinholeCameraCfg(SpawnerCfg)
    """Configuration parameters for a USD camera prim with pinhole camera settings.

For more information on the parameters, please refer to the `camera documentation <https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html>`__.

..note ::
    Focal length as well as the aperture size"""
    def from_intrinsic_matrix(cls, intrinsic_matrix, width, height, clipping_range, focal_length, focus_distance, f_stop, projection_type, lock_camera)
class FisheyeCameraCfg(PinholeCameraCfg)
    """Configuration parameters for a USD camera prim with `fish-eye camera`_ settings.

For more information on the parameters, please refer to the
`camera documentation <https://docs.omniverse.nvidia.com/materials-and-rendering/latest/cameras.html#fisheye-properties>`__.

.. note::
    The default values"""
class SensorFrameCfg(SpawnerCfg)
    """Spawns a plain USD Xform as a sensor attachment frame.

The spawned prim carries no rigid body or collision API. It serves as a
non-physics child under a link so that :class:`~isaaclab.sim.views.FrameView`
can track it on all backends (including Newton, which rejects physics body prims)."""
```

### source/isaaclab/isaaclab/sim/spawners/shapes/__init__.py

```
"""Sub-module for spawning primitive shapes in the simulation.

NVIDIA Omniverse provides various primitive shapes that can be used to create USDGeom prims. Based
on the configuration, the spawned prim can be:

* a visual mesh (no physics)
* a static collider (no rigid body)
* a rigid body (with collision and rigid body properties)."""
```

### source/isaaclab/isaaclab/sim/spawners/shapes/shapes.py

```
def spawn_sphere(prim_path, cfg, translation, orientation)
def spawn_cuboid(prim_path, cfg, translation, orientation)
def spawn_cylinder(prim_path, cfg, translation, orientation)
def spawn_capsule(prim_path, cfg, translation, orientation)
def spawn_cone(prim_path, cfg, translation, orientation)
def spawn_cable(prim_path, cfg, translation, orientation)
def _spawn_geom_from_prim_type(prim_path, cfg, prim_type, attributes, translation, orientation, scale, stage, geometry_schema_func)
```

### source/isaaclab/isaaclab/sim/spawners/shapes/shapes_cfg.py

```
class ShapeCfg(RigidObjectSpawnerCfg)
    """Configuration parameters for a USD Geometry or Geom prim."""
class SphereCfg(ShapeCfg)
    """Configuration parameters for a sphere prim.

See :meth:`spawn_sphere` for more information."""
class CuboidCfg(ShapeCfg)
    """Configuration parameters for a cuboid prim.

See :meth:`spawn_cuboid` for more information."""
class CylinderCfg(ShapeCfg)
    """Configuration parameters for a cylinder prim.

See :meth:`spawn_cylinder` for more information."""
class CapsuleCfg(ShapeCfg)
    """Configuration parameters for a capsule prim.

See :meth:`spawn_capsule` for more information."""
class ConeCfg(ShapeCfg)
    """Configuration parameters for a cone prim.

See :meth:`spawn_cone` for more information."""
class CableCfg(SpawnerCfg)
    """Configuration parameters for an open linear cable."""
```

### source/isaaclab/isaaclab/sim/spawners/spawner_cfg.py

```
class SpawnerCfg()
    """Configuration parameters for spawning an asset.

Spawning an asset is done by calling the :attr:`func` function. The function takes in the
prim path to spawn the asset at, the configuration instance and transformation, and returns the
prim path of the spawned asset.

The function is typically decora"""
class RigidObjectSpawnerCfg(SpawnerCfg)
    """Configuration parameters for spawning a rigid asset.

Note:
    By default, all properties are set to None. This means that no properties will be added or modified
    to the prim outside of the properties available by default when spawning the prim."""
class DeformableObjectSpawnerCfg(SpawnerCfg)
    """Configuration parameters for spawning a deformable asset.

Unlike rigid objects, deformable objects are affected by forces and can deform when subjected to
external forces. This class is used to configure the properties of the deformable object.

Deformable bodies collide through their simulation me"""
```

### source/isaaclab/isaaclab/sim/spawners/wrappers/__init__.py

```
"""Sub-module for wrapping spawner configurations.

Unlike the other spawner modules, this module provides a way to wrap multiple spawner configurations
into a single configuration. This is useful when the user wants to spawn multiple assets based on
different configurations."""
```

### source/isaaclab/isaaclab/sim/spawners/wrappers/wrappers.py

```
def spawn_multi_asset(prim_path, cfg, translation, orientation, clone_in_fabric, replicate_physics)
def spawn_multi_usd_file(prim_path, cfg, translation, orientation, clone_in_fabric, replicate_physics)
```

### source/isaaclab/isaaclab/sim/spawners/wrappers/wrappers_cfg.py

```
class MultiAssetSpawnerCfg(RigidObjectSpawnerCfg, DeformableObjectSpawnerCfg)
    """Configuration parameters for loading multiple assets from their individual configurations.

Specifying values for any properties at the configuration level will override the settings of
individual assets' configuration. For instance if the attribute
:attr:`MultiAssetSpawnerCfg.mass_props` is specifi"""
class MultiUsdFileCfg(UsdFileCfg)
    """Configuration parameters for loading multiple USD files.

Specifying values for any properties at the configuration level is applied to all the assets
imported from their USD files.

.. tip::
    It is recommended that all the USD based assets follow a similar prim-hierarchy."""
```

### source/isaaclab/isaaclab/sim/utils/__init__.py

```
"""Utilities built around USD operations."""
```

### source/isaaclab/isaaclab/sim/utils/extensions.py

```
"""Utilities for interacting with Kit extensions."""
def enable_extension(extension_name)
def disable_extension(extension_name)
def get_extension_path(extension_name)
def _get_extension_manager()
```

### source/isaaclab/isaaclab/sim/utils/legacy.py

```
"""Utilities for legacy functionality.

This sub-module contains legacy functions from Isaac Sim that are no longer
required for Isaac Lab. Most functions are simple wrappers around USD APIs
and are provided mainly for convenience.

It is recommended to use the USD APIs directly whenever possible."""
def add_reference_to_stage(usd_path, path, prim_type)
def get_stage_up_axis()
def traverse_stage(fabric)
def get_prim_at_path(prim_path, fabric)
def get_prim_path(prim)
def is_prim_path_valid(prim_path, fabric)
def define_prim(prim_path, prim_type, fabric)
def get_prim_type_name(prim_path, fabric)
def get_next_free_path(path)
```

### source/isaaclab/isaaclab/sim/utils/newton_model_utils.py

```
"""DO NOT USE ANY FUNCTION IN THIS FILE.

This module exists only while Isaac Lab and Isaac Sim content still relies on NVIDIA-specific MDL and OmniPBR
materials; after migration to neutral USD materials that Newton can consume directly, this module is expected
to be deprecated and removed."""
def _linear_channel_to_srgb(c)
def _canonical_prim_lookup_key(prim)
def _asset_path_to_str(asset_path)
def _is_omnipbr_shader(shader_prim)
def _get_bound_material_prim(shape_prim)
def _get_input_value(shader, name)
def _get_surface_shader(material_prim)
def _get_omnipbr_input(shader, input_name)
def _get_omnipbr_albedo(shader_prim)
def _coerce_color(value)
def _get_primvar_display_color(shape_prim)
def _resolve_shape_color(stage, prim_path, material_color_cache)
def replace_newton_builder_shape_colors(builder, stage)
```

### source/isaaclab/isaaclab/sim/utils/prims.py

```
"""Utilities for creating and manipulating USD prims."""
def create_prim(prim_path, prim_type, position, translation, orientation, scale, usd_path, semantic_label, semantic_type, attributes, stage)
def delete_prim(prim_path, stage)
def make_uninstanceable(prim_path, stage)
def set_prim_visibility(prim, visible)
def safe_set_attribute_on_usd_schema(schema_api, name, value, camel_case)
def safe_set_attribute_on_usd_prim(prim, attr_name, value, camel_case)
def change_prim_property(prop_path, value, stage, type_to_create_if_not_exist, is_custom)
def export_prim_to_file(path, source_prim_path, target_prim_path, stage)
def apply_nested(func)
def apply_nested()
def apply_nested(func)
def clone(func)
def bind_visual_material(prim_path, material_path, stage, stronger_than_descendants)
def bind_physics_material(prim_path, material_path, stage, stronger_than_descendants)
def add_usd_reference(prim_path, usd_path, prim_type, stage)
def get_usd_references(prim_path, stage)
def select_usd_variants(prim_path, variants, stage)
def _to_tuple(value)
```

### source/isaaclab/isaaclab/sim/utils/queries.py

```
"""Utilities for querying the USD stage."""
def path_expr_to_glob(path_expr)
def get_next_free_prim_path(path, stage)
def get_first_matching_ancestor_prim(prim_path, predicate, stage)
def get_first_matching_child_prim(prim_path, predicate, stage, traverse_instance_prims)
def get_all_matching_child_prims(prim_path, predicate, depth, stage, traverse_instance_prims, expected_num_matches)
def find_first_matching_prim(prim_path_regex, stage)
def split_path_expr(path_expr)
def matches_path_expr_prefix(path_expr, prim_path)
def _iter_matching_prims_in_subtree(prim_path_regex, root_prim)
def find_matching_prims(prim_path_regex, stage)
def resolve_matching_prims_from_source(path_expr, predicate, expected_num_matches, env_regex_ns, raise_if_no_matches, traverse_instance_prims)
def find_matching_prim_paths(prim_path_regex, stage)
def find_global_fixed_joint_prim(prim_path, check_enabled_only, stage)
def has_deformable_body_api(prim)
def has_deformable_curve_api(prim)
```

### source/isaaclab/isaaclab/sim/utils/semantics.py

```
"""Utilities for applying and removing semantic labels to USD prims."""
def add_labels(prim, labels, instance_name, overwrite)
def get_labels(prim)
def remove_labels(prim, instance_name, include_descendants)
def check_missing_labels(prim_path, stage)
def count_total_labels(prim_path, stage)
```

### source/isaaclab/isaaclab/sim/utils/stage.py

```
"""Utilities for operating on the USD stage."""
def _check_ancestral(prim)
def _is_uri_path(asset_path)
def resolve_paths(src_layer_identifier, dst_layer_identifier, store_relative_path)
def _sync_isaacsim_stage_context()
def create_new_stage()
def is_current_stage_in_memory()
def open_stage(usd_path)
def use_stage(stage)
def update_stage()
def save_stage(usd_path, save_and_reload_in_place)
def close_stage()
def _is_prim_deletable(prim)
def clear_stage(predicate)
def get_current_stage(fabric)
def get_current_stage_id()
def show_stage_in_viewport(usd_path)
```

### source/isaaclab/isaaclab/sim/utils/transforms.py

```
"""Utilities for working with USD transform (xform) operations.

This module provides utilities for manipulating USD transform operations (xform ops) on prims.
Transform operations in USD define how geometry is positioned, oriented, and scaled in 3D space.

The utilities in this module help standardize transform stacks, clear operations, and manipulate
transforms in a consistent way across different USD assets."""
def standardize_xform_ops(prim, translation, orientation, scale)
def validate_standard_xform_ops(prim)
def resolve_prim_pose(prim, ref_prim)
def resolve_prim_scale(prim)
def convert_world_pose_to_local(position, orientation, ref_prim)
```

### source/isaaclab/isaaclab/sim/views/__init__.py

```
"""Views for manipulating USD prims."""
```

### source/isaaclab/isaaclab/sim/views/base_frame_view.py

```
"""Abstract base class for batched prim transform views."""
class BaseFrameView(ABC)
    """Abstract interface for reading and writing transforms of multiple prims.

Backend-specific implementations (USD/Fabric, Newton GPU state, etc.) subclass
this to provide efficient batched pose queries.  The factory
:class:`~isaaclab.sim.views.FrameView` selects the correct
implementation at runtime b"""
    def count(self)
    def device(self)
    def close(self)
    def xform_world_space_writer(self)
    def xform_local_space_writer(self)
    def _make_world_space_writer(self)
    def _make_local_space_writer(self)
    def _assert_no_active_writer(self, method_name)
    def get_world_poses(self, indices)
    def get_local_poses(self, indices)
    def get_local_scales(self, indices)
    def get_world_scales(self, indices)
    def _get_world_poses_impl(self, indices)
    def _get_local_poses_impl(self, indices)
    def _get_local_scales_impl(self, indices)
    def _get_world_scales_impl(self, indices)
    def set_world_poses(self, positions, orientations, indices)
    def set_local_poses(self, translations, orientations, indices)
    def get_scales(self, indices)
    def set_scales(self, scales, indices)
    def _get_scales_impl(self, indices)
    def _set_scales_impl(self, scales, indices)
```

### source/isaaclab/isaaclab/sim/views/frame_view.py

```
"""Backend-dispatching FrameView.

``FrameView(path, device=...)`` automatically selects the right backend:
- PhysX: :class:`~isaaclab_physx.sim.views.FabricFrameView`
- Newton: :class:`~isaaclab_newton.sim.views.NewtonSiteFrameView`"""
class FrameView(FactoryBase, BaseFrameView)
    """FrameView that dispatches to the active physics backend.

Callers use ``FrameView(prim_path, device=device)`` and get the
correct implementation automatically:

- **PhysX / no backend**: :class:`~isaaclab_physx.sim.views.FabricFrameView`
  (Fabric GPU acceleration with USD fallback).
- **OVPhysX**: """
    def _get_backend(cls)
    def __new__(cls)
```

### source/isaaclab/isaaclab/sim/views/usd_frame_view.py

```
class UsdFrameView(BaseFrameView)
    """Batched interface for reading and writing transforms of multiple USD prims.

Provides batch operations for getting and setting poses (position and orientation)
of multiple prims at once via USD's ``XformCache``.

The class supports both world-space and local-space pose operations:

- **World poses**"""
    def __init__(self, prim_path, device, validate_xform_ops, stage)
    def count(self)
    def device(self)
    def prims(self)
    def prim_paths(self)
    def _make_world_space_writer(self)
    def _make_local_space_writer(self)
    def set_visibility(self, visibility, indices)
    def get_visibility(self, indices)
    def _apply_world_pose_write(self, positions, orientations, indices)
    def _apply_local_pose_write(self, translations, orientations, indices)
    def _apply_local_scale_write(self, scales, indices)
    def _apply_world_scale_write(self, scales, indices)
    def _get_world_poses_impl(self, indices)
    def _get_local_poses_impl(self, indices)
    def _get_local_scales_impl(self, indices)
    def _get_world_scales_impl(self, indices)
    def _get_scales_impl(self, indices)
    def _set_scales_impl(self, scales, indices)
    def _resolve_indices(self, indices)
    def _to_numpy(data)
class _UsdWorldSpaceWriter(FrameViewWorldSpaceWriter)
    """USD world-space writer: pass-through to backend ``_apply_*`` hooks.

USD has no separate world-matrix storage to keep in sync; ``__exit__``
is a no-op beyond releasing the single-writer lock."""
    def set_poses(self, positions, orientations, indices)
    def set_scales(self, scales, indices)
    def get_poses(self, indices)
    def get_scales(self, indices)
class _UsdLocalSpaceWriter(FrameViewLocalSpaceWriter)
    """USD local-space writer: pass-through to backend ``_apply_*`` hooks."""
    def set_poses(self, positions, orientations, indices)
    def set_scales(self, scales, indices)
    def get_poses(self, indices)
    def get_scales(self, indices)
```

### source/isaaclab/isaaclab/sim/views/xform_prim_view.py

```
"""Backward-compatibility alias: ``XformPrimView`` -> :class:`FrameView`."""
```

### source/isaaclab/isaaclab/sim/views/xform_space_writer.py

```
"""Context-managed transform writers for :class:`~isaaclab.sim.views.BaseFrameView`.

This module defines the recommended write API for FrameView poses and scales:

.. code-block:: python

    with view.xform_world_space_writer() as writer:
        writer.set_poses(positions=p, orientations=o)
        writer.set_scales(scales=s)
        # ... any number of writes ...
    # On exit the writer derives the opposite-space matrices once,
    # synchronizes once, and restores any saved Fabric tracking state.

Only one writer may be active per view at a time.  While a writer scope is
active on a view, v"""
class FrameViewSpaceWriterBase(ABC)
    """Abstract context-managed writer for a single transform space.

Subclasses are returned by :meth:`BaseFrameView.xform_world_space_writer` /
:meth:`BaseFrameView.xform_local_space_writer`; they
are not constructed directly.  The class is intentionally minimal -- the
pose/scale semantics depend on the """
    def __init__(self, view)
    def set_poses(self, positions, orientations, indices)
    def set_scales(self, scales, indices)
    def get_poses(self, indices)
    def get_scales(self, indices)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def _enter_impl(self)
    def _exit_impl(self, exc_type, exc_val, exc_tb)
class FrameViewWorldSpaceWriter(FrameViewSpaceWriterBase)
    """Writer whose :meth:`set_poses` / :meth:`set_scales` write world-space values.

On context exit the opposite-space (``local``) matrices are derived from
the just-written world matrices in a single Warp kernel launch."""
class FrameViewLocalSpaceWriter(FrameViewSpaceWriterBase)
    """Writer whose :meth:`set_poses` / :meth:`set_scales` write local-space values.

On context exit the opposite-space (``world``) matrices are derived from
the just-written local matrices in a single Warp kernel launch."""
```

### source/isaaclab/isaaclab/terrains/config/__init__.py

```
"""Pre-defined terrain configurations for the terrain generator."""
```

### source/isaaclab/isaaclab/terrains/config/rough.py

```
"""Configuration for custom terrains."""
```

### source/isaaclab/isaaclab/terrains/height_field/hf_terrains_cfg.py

```
class HfTerrainBaseCfg(SubTerrainBaseCfg)
    """The base configuration for height field terrains."""
class HfRandomUniformTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a random uniform height field terrain."""
class HfPyramidSlopedTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a pyramid sloped height field terrain."""
class HfInvertedPyramidSlopedTerrainCfg(HfPyramidSlopedTerrainCfg)
    """Configuration for an inverted pyramid sloped height field terrain.

Note:
    This is a subclass of :class:`HfPyramidSlopedTerrainCfg` with :obj:`inverted` set to True.
    We make it as a separate class to make it easier to distinguish between the two and match
    the naming convention of the othe"""
class HfPyramidStairsTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a pyramid stairs height field terrain."""
class HfInvertedPyramidStairsTerrainCfg(HfPyramidStairsTerrainCfg)
    """Configuration for an inverted pyramid stairs height field terrain.

Note:
    This is a subclass of :class:`HfPyramidStairsTerrainCfg` with :obj:`inverted` set to True.
    We make it as a separate class to make it easier to distinguish between the two and match
    the naming convention of the othe"""
class HfDiscreteObstaclesTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a discrete obstacles height field terrain."""
class HfWaveTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a wave height field terrain."""
class HfSteppingStonesTerrainCfg(HfTerrainBaseCfg)
    """Configuration for a stepping stones height field terrain."""
```

### source/isaaclab/isaaclab/terrains/sub_terrain_cfg.py

```
class FlatPatchSamplingCfg()
    """Configuration for sampling flat patches on the sub-terrain.

For a given sub-terrain, this configuration specifies how to sample flat patches on the terrain.
The sampled flat patches can be used for spawning robots, targets, etc.

Please check the function :meth:`~isaaclab.terrains.utils.find_flat_p"""
class SubTerrainBaseCfg()
    """Base class for terrain configurations.

All the sub-terrain configurations must inherit from this class.

The :attr:`size` attribute is the size of the generated sub-terrain. Based on this, the terrain must
extend from :math:`(0, 0)` to :math:`(size[0], size[1])`."""
```

### source/isaaclab/isaaclab/terrains/terrain_generator_cfg.py

```
"""Configuration classes defining the different terrains available. Each configuration class must
inherit from ``isaaclab.terrains.terrains_cfg.TerrainConfig`` and define the following attributes:

- ``name``: Name of the terrain. This is used for the prim name in the USD stage.
- ``function``: Function to generate the terrain. This function must take as input the terrain difficulty
  and the configuration parameters and return a `tuple with the `trimesh`` mesh object and terrain origin."""
class TerrainGeneratorCfg()
    """Configuration for the terrain generator."""
```

### source/isaaclab/isaaclab/terrains/terrain_importer_cfg.py

```
class TerrainImporterCfg()
    """Configuration for the terrain manager."""
    def __post_init__(self)
```

### source/isaaclab/isaaclab/terrains/trimesh/mesh_terrains_cfg.py

```
class MeshPlaneTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a plane mesh terrain."""
class MeshPyramidStairsTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a pyramid stair mesh terrain."""
class MeshInvertedPyramidStairsTerrainCfg(MeshPyramidStairsTerrainCfg)
    """Configuration for an inverted pyramid stair mesh terrain.

Note:
    This is the same as :class:`MeshPyramidStairsTerrainCfg` except that the steps are inverted."""
class MeshRandomGridTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a random grid mesh terrain."""
class MeshRailsTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with box rails as extrusions."""
class MeshPitTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with a pit that leads out of the pit."""
class MeshBoxTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with boxes (similar to a pyramid)."""
class MeshGapTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with a gap around the platform."""
class MeshFloatingRingTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with a floating ring around the center."""
class MeshStarTerrainCfg(SubTerrainBaseCfg)
    """Configuration for a terrain with a star pattern."""
class MeshRepeatedObjectsTerrainCfg(SubTerrainBaseCfg)
    """Base configuration for a terrain with repeated objects."""
    def __post_init__(self)
class MeshRepeatedPyramidsTerrainCfg(MeshRepeatedObjectsTerrainCfg)
    """Configuration for a terrain with repeated pyramids."""
class MeshRepeatedBoxesTerrainCfg(MeshRepeatedObjectsTerrainCfg)
    """Configuration for a terrain with repeated boxes."""
class MeshRepeatedCylindersTerrainCfg(MeshRepeatedObjectsTerrainCfg)
    """Configuration for a terrain with repeated cylinders."""
```

### source/isaaclab/isaaclab/test/env_cfgs.py

```
"""Shared core-only environment configurations for Isaac Lab tests.

The configuration classes and factories in this module are safe to import, construct, and
validate without starting :class:`isaaclab.app.AppLauncher`. Creating environments from the
resulting configurations still requires a running simulator."""
def make_empty_manager_based_env_cfg(device, num_envs, env_spacing)
def make_empty_manager_based_rl_env_cfg(device, num_envs, env_spacing)
def make_empty_direct_marl_env_cfg(device, num_envs, env_spacing)
class EmptyManagerCfg()
    """Empty manager term configuration."""
class EmptySceneCfg(InteractiveSceneCfg)
    """Configuration for a scene without entities."""
```

### source/isaaclab/isaaclab/test/integration_scene_cfgs.py

```
"""Shared core-only scene configurations for Isaac Lab integration tests."""
class CartpoleTestSceneCfg(InteractiveSceneCfg)
    """Configuration for a minimal cart-pole articulation scene.

The scene intentionally contains only the robot because its integration-test hosts do
not assert ground or lighting behavior."""
class ArticulationRigidObjectSceneCfg(CartpoleTestSceneCfg)
    """Configuration for a minimal scene with articulation and rigid-object state."""
```

### source/isaaclab/isaaclab/utils/configclass.py

```
"""Sub-module that provides a wrapper around the Python 3.7 onwards ``dataclasses`` module."""
def __dataclass_transform__()
def configclass(cls)
def _class_to_dict(obj)
def _update_class_from_dict(obj, data)
def _replace_class_with_kwargs(obj)
def _copy_class(obj)
def _field_module_dir(obj, key)
def _wrap_resolvable_strings(value, module_dir, _seen)
def _add_annotation_types(cls)
def _validate(obj, prefix)
def _process_mutable_types(cls)
def _custom_post_init(obj)
def _combined_function(f1, f2)
def _skippable_class_member(key, value, hints)
def _return_f(f)
def checked_apply(src, target)
class _CallableModule(ModuleType)
    """Module type that makes :mod:`isaaclab.utils.configclass` usable as the decorator it defines.

This sub-module and the :func:`configclass` decorator share a name, so ``isaaclab.utils.configclass``
can only resolve to one object. Making the module callable lets it be both: ``@configclass`` works
on th"""
    def __call__(self, cls)
```

### source/isaaclab/isaaclab/utils/modifiers/modifier_cfg.py

```
class ModifierCfg()
    """Configuration parameters for function and class modifiers."""
class DigitalFilterCfg(ModifierCfg)
    """Configuration parameters for a digital filter modifier.

For more information, please check the :class:`DigitalFilter` class."""
class IntegratorCfg(ModifierCfg)
    """Configuration parameters for an integrator modifier.

For more information, please check the :class:`Integrator` class."""
```

### source/isaaclab/isaaclab/utils/noise/noise_cfg.py

```
class NoiseCfg()
    """Base configuration for a noise term."""
class ConstantNoiseCfg(NoiseCfg)
    """Configuration for an additive constant noise term."""
class UniformNoiseCfg(NoiseCfg)
    """Configuration for a additive uniform noise term."""
class GaussianNoiseCfg(NoiseCfg)
    """Configuration for an additive gaussian noise term."""
class NoiseModelCfg()
    """Configuration for a noise model."""
class NoiseModelWithAdditiveBiasCfg(NoiseModelCfg)
    """Configuration for an additive gaussian noise with bias model."""
```

### source/isaaclab/isaaclab/visualizers/visualizer_cfg.py

```
"""Base configuration for visualizers."""
def _get_visualizer_install_hint(visualizer_type)
class VisualizerCfg()
    """Base configuration for all visualizer backends.

Note:
    This configuration can be used directly as
    :attr:`~isaaclab.sim.SimulationCfg.default_visualizer_cfg` to provide shared defaults.
    To create a visualizer, use a concrete config from ``isaaclab_visualizers``, such as
    ``KitVisualize"""
    def __post_init__(self)
```

### source/isaaclab/test/app/test_env_var_launch.py

```
def test_livestream_launch_with_env_vars(mocker)
def _resolve_kit_args(monkeypatch, launcher_args, argv)
def test_fabric_gpu_interop_env_adds_override(monkeypatch, env_value, expected)
def test_fabric_gpu_interop_env_rejects_invalid_value(monkeypatch)
def test_explicit_kit_setting_takes_precedence(monkeypatch)
def test_explicit_kit_args_setting_takes_precedence(monkeypatch)
def test_simulation_manager_default_callbacks_disabled(monkeypatch)
def test_explicit_simulation_manager_callback_setting_takes_precedence(monkeypatch)
```

### source/isaaclab/test/app/test_launch_simulation_require_kit.py

```
"""Tests for the ``require_kit`` launcher argument read by :func:`isaaclab.app.launch_simulation`.

``require_kit`` lets a tool state that it needs Kit for a reason the config cannot express --
the URDF/MJCF converters set it because they reach a Kit-only importer extension whenever the
standalone importer wheel is absent. The override is additive: it can turn a kitless launch into
a Kit one, never the reverse.

Kit is never actually started here: availability and ``AppLauncher`` are faked, and reaching
``_ensure_isaac_sim_available`` is the signal that the Kit branch was taken. No Kit/GPU requir"""
def kit_branch_taken(monkeypatch)
def test_default_stays_kitless_for_a_kitless_config(kit_branch_taken)
def test_kitless_launch_configures_storage_before_user_code(kit_branch_taken, monkeypatch)
def test_storage_profile_failure_closes_started_kit(monkeypatch)
def test_require_kit_launches_kit_for_a_kitless_config(kit_branch_taken)
def test_require_kit_reads_from_a_namespace(kit_branch_taken)
def test_require_kit_rejects_ovrtx_runtime(monkeypatch)
def test_newton_rtx_rejects_kit_before_loading_ovrtx(monkeypatch)
def test_kitless_ovrtx_registers_before_user_code(monkeypatch)
def test_require_kit_false_does_not_suppress_a_kit_config(kit_branch_taken)
```

### source/isaaclab/test/app/test_simulation_app_lifecycle.py

```
"""Kitless unit tests for the AppLauncher process-lifecycle exit policy."""
def _make_lifecycle(close_fn)
def _capture_signal_actions(monkeypatch)
def test_abort_signal_closes_once_with_killed_by_signal_status(monkeypatch)
def test_abort_signal_reentrant_signal_skips_nested_close(monkeypatch)
def test_abort_signal_falls_back_when_exit_code_unsupported(capfd, monkeypatch)
def test_atexit_close_arms_reentrancy_guard(monkeypatch)
def test_atexit_close_preserves_pending_failure_status(monkeypatch)
def test_atexit_close_falls_back_when_exit_code_unsupported(capfd)
```

### source/isaaclab/test/benchmark/test_train_checkpoint_path.py

```
"""Checkpoint reporting for training benchmark adapters."""
def test_resolve_training_checkpoint_path_matches_backend_filename(tmp_path, backend, subdir, filename)
def test_resolve_training_checkpoint_path_uses_natural_order(tmp_path)
def test_resolve_training_checkpoint_path_returns_none_without_checkpoint(tmp_path)
```

### source/isaaclab/test/cli/test_env_commands.py

```
"""Tests for virtual environment setup commands."""
def test_environment_setup_rejects_downloaded_isaac_sim(tmp_path, command, environment_type)
def test_environment_setup_accepts_marked_source_build(tmp_path)
def test_launcher_rejects_downloaded_isaac_sim_with_active_environment(tmp_path)
def test_launcher_uses_bundled_python_with_inactive_default_environment(tmp_path)
def test_launcher_accepts_virtual_environment_on_bundled_python(tmp_path)
def test_launcher_rejects_virtual_environment_on_foreign_python(tmp_path)
def test_launcher_allows_relinking_unmarked_source_build(tmp_path)
```

### source/isaaclab/test/cli/test_test_orchestrator_result_handling.py

```
"""Tests for per-file pytest result handling in the test orchestrator."""
def _load_orchestrator_module()
def _write_empty_junit_report(report_file)
def _write_partial_junit_report(report_file)
def _write_module_skipped_junit_report(report_file)
def _write_failing_junit_report(report_file, name)
def _append_journal(journal_file, records)
def _journaled_test(node_id, outcome)
def test_exact_node_ids_selecting_zero_tests_fail(monkeypatch, tmp_path)
def test_nonzero_pytest_exit_preserves_reported_tests(monkeypatch, tmp_path)
def test_filter_deselecting_all_tests_is_not_a_failure(monkeypatch, tmp_path)
def test_module_importorskip_is_not_a_failure(monkeypatch, tmp_path)
def test_abnormal_termination_report_quotes_bounded_renderer_log(monkeypatch, tmp_path, caplog, returncode, kill_reason, expected_result)
def test_abnormal_termination_saves_the_renderer_log_of_the_blamed_test(monkeypatch, tmp_path, returncode, kill_reason, expected_result)
def test_shutdown_hang_after_report_is_not_a_failure(monkeypatch, tmp_path)
def test_startup_retry_wall_time_includes_every_attempt(monkeypatch, tmp_path)
def test_crash_journal_path_is_absolute(monkeypatch, tmp_path)
def test_artifact_paths_handed_to_the_subprocess_are_uploadable(monkeypatch, tmp_path)
def test_fresh_process_retry_crash_blames_the_test_that_was_running(monkeypatch, tmp_path)
def test_result_summary_includes_fast_failure_after_thirty_slower_files()
def test_hung_process_report_names_where_it_is_stuck(monkeypatch, tmp_path)
def test_hang_dump_plugin_is_inert_without_signal_support(monkeypatch)
def test_external_git_asset_tests_receive_extended_startup_deadline()
```

### source/isaaclab/test/cli/test_train_multigpu_command_building.py

```
"""Regression tests for passing ``--kit_args`` with an option-like value.

Kit arguments always start with ``--``, and argparse rejects a value token that
itself looks like an option (starts with ``-`` and contains no space) with
"expected one argument" (exit code 2). This used to break the documented
space-separated form ``--kit_args "--foo=/bar"`` for a single Kit argument on
every entry point, including all ranks of the multi-GPU launcher.

:meth:`~isaaclab.app.AppLauncher.add_app_launcher_args` now fuses such pairs in
``sys.argv`` into single ``--kit_args=<value>`` tokens before any parsing, """
def _build_command(argv)
def _forwarded_train_argv(command)
def _parse_as_training_script(child_argv, monkeypatch)
class TestFuseKitArgs()
    """Unit tests for :meth:`AppLauncher._fuse_kit_args`."""
    def test_space_separated_option_like_value_is_fused(self)
    def test_equals_attached_value_is_unchanged(self)
    def test_value_with_space_is_unchanged(self)
    def test_non_option_value_is_unchanged(self)
    def test_trailing_kit_args_is_unchanged(self)
    def test_multiple_occurrences_are_all_fused(self)
    def test_surrounding_tokens_are_preserved(self)
class TestAddAppLauncherArgsNormalization()
    """Integration tests for the ``sys.argv`` normalization in ``add_app_launcher_args``."""
    def test_space_separated_single_kit_arg_parses(self, monkeypatch)
    def test_unknown_leftovers_are_preserved(self, monkeypatch)
class TestDispatchLibraryEntrypoint()
    """Tests for the ``--kit_args`` normalization in ``dispatch_library_entrypoint``.

The benchmark dispatchers hand the per-library scripts an explicit argv list
(not ``sys.argv``), so the normalization must also run on that list before it
is forwarded."""
    def _dispatch(tmp_path, argv)
    def test_space_separated_kit_args_fused_before_library_script(self, tmp_path)
    def test_already_working_argv_forms_forwarded_unchanged(self, tmp_path)
class TestKitArgsForwarding()
    """Tests for forwarding ``--kit_args`` through the multi-GPU launcher."""
    def test_space_separated_kit_args_forwarded_verbatim(self)
    def test_equals_attached_kit_args_forwarded_unchanged(self)
    def test_multi_token_kit_args_value_forwarded_as_single_token(self)
    def test_forwarded_space_separated_kit_args_accepted_by_training_script(self, monkeypatch)
    def test_forwarded_skrl_jax_kit_args_accepted_by_training_script(self, monkeypatch)
    def test_dry_run_prints_shell_parsable_command(self, capsys)
```

### source/isaaclab/test/controllers/test_local_frame_task.py

```
"""Test cases for LocalFrameTask class."""
def urdf_path()
def controlled_joint_names()
def pink_config(urdf_path, controlled_joint_names)
def local_frame_task()
def test_initialization(local_frame_task)
def test_initialization_with_sequence_costs()
def test_inheritance_from_frame_task(local_frame_task)
def test_set_target(local_frame_task)
def test_set_target_from_configuration(local_frame_task, pink_config)
def test_set_target_from_configuration_wrong_type(local_frame_task)
def test_compute_error_with_target_set(local_frame_task, pink_config)
def test_compute_error_without_target(local_frame_task, pink_config)
def test_compute_error_wrong_configuration_type(local_frame_task)
def test_compute_jacobian_with_target_set(local_frame_task, pink_config)
def test_compute_jacobian_without_target(local_frame_task, pink_config)
def test_error_consistency_across_configurations(local_frame_task, pink_config)
def test_jacobian_consistency_across_configurations(local_frame_task, pink_config)
def test_error_zero_at_target_pose(local_frame_task, pink_config)
def test_different_frames(pink_config)
def test_different_base_frames(pink_config)
def test_sequence_cost_parameters()
def test_error_magnitude_consistency(local_frame_task, pink_config)
def test_jacobian_structure(local_frame_task, pink_config)
def test_multiple_target_updates(local_frame_task, pink_config)
def test_inheritance_behavior(local_frame_task)
def test_target_copying_behavior(local_frame_task)
def test_error_computation_with_orientation_difference(local_frame_task, pink_config)
def test_jacobian_rank_consistency(local_frame_task, pink_config)
```

### source/isaaclab/test/controllers/test_null_space_posture_task.py

```
"""Unit tests for NullSpacePostureTask with simplified robot configuration using Pink library directly."""
class TestNullSpacePostureTaskSimplifiedRobot()
    """Test cases for NullSpacePostureTask with simplified robot configuration."""
    def num_joints(self)
    def joint_configurations(self)
    def robot_urdf(self)
    def robot_configuration(self, robot_urdf)
    def tasks(self)
    def test_null_space_jacobian_zero_end_effector_velocity(self, robot_configuration, tasks, joint_configurations, num_joints)
    def test_null_space_jacobian_properties(self, robot_configuration, tasks, joint_configurations, num_joints)
    def test_null_space_jacobian_identity_when_no_frame_tasks(self, robot_configuration, joint_configurations, num_joints)
    def test_null_space_jacobian_consistency_across_configurations(self, robot_configuration, tasks, joint_configurations, num_joints)
    def test_compute_error_without_target(self, robot_configuration, joint_configurations)
    def test_joint_masking(self, robot_configuration, joint_configurations, num_joints)
    def test_empty_controlled_joints(self, robot_configuration, joint_configurations, num_joints)
    def test_set_target_from_configuration(self, robot_configuration, joint_configurations)
    def test_multiple_frame_tasks(self, robot_configuration, joint_configurations, num_joints)
```

### source/isaaclab/test/deps/isaacsim/check_camera.py

```
"""Historic camera episodic-reset reproducer (retired).

This script previously depended on Isaac Sim core extensions that Isaac Sim now carries under
``source/deprecated`` in the Isaac Sim repository. It has been retired from Isaac Lab to avoid
depending on those extension IDs and import paths.

Use :class:`~isaaclab.sim.SimulationContext`, Isaac Lab sensors, and ``isaacsim.core.experimental.*``
APIs when debugging rendering and camera pipelines."""
```

### source/isaaclab/test/deps/isaacsim/check_floating_base_made_fixed.py

```
"""Historic floating-base / fixed-base reproducer (retired).

This script previously depended on Isaac Sim core extensions that Isaac Sim now carries under
``source/deprecated`` in the Isaac Sim repository. It has been retired from Isaac Lab to avoid
depending on those extension IDs and import paths.

Use :class:`~isaaclab.sim.SimulationContext` and ``isaacsim.core.experimental.prims.Articulation``
for articulation-level debugging."""
```

### source/isaaclab/test/deps/isaacsim/check_legged_robot_clone.py

```
"""Historic legged-robot cloning reproducer (retired).

This script previously depended on Isaac Sim core extensions that Isaac Sim now carries under
``source/deprecated`` in the Isaac Sim repository. It has been retired from Isaac Lab to avoid
depending on those extension IDs and import paths.

Use :class:`~isaaclab.sim.SimulationContext`, :class:`isaacsim.core.cloner.GridCloner`, and
``isaacsim.core.experimental.prims.Articulation`` for cloning workflows."""
```