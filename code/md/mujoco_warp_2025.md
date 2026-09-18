# mujoco_warp_2025

source: https://github.com/google-deepmind/mujoco_warp


commit: 87e742d31c96f69a70741c51b9ade43bd8d1b60b


## README

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/google-deepmind/mujoco_warp/ci.yml?branch=main)](https://github.com/google-deepmind/mujoco_warp/actions/workflows/ci.yml?query=branch%3Amain)
[![Documentation](https://readthedocs.org/projects/mujoco/badge/?version=latest)](https://mujoco.readthedocs.io/en/latest/mjwarp/index.html)
[![License](https://img.shields.io/github/license/google-deepmind/mujoco_warp)](https://github.com/google-deepmind/mujoco_warp/blob/main/LICENSE)
[![Nightly Benchmarks](https://img.shields.io/badge/Nightly-Benchmarks-blue)](https://google-deepmind.github.io/mujoco_warp/nightly/)

# MuJoCo Warp (MJWarp)

MJWarp is a GPU-accelerated version of the [MuJoCo](https://github.com/google-deepmind/mujoco) physics simulator, designed for NVIDIA hardware. MJWarp delivers high-throughput, accurate simulation for robotics research.

MJWarp is maintained by [Google DeepMind](https://deepmind.google/) and [NVIDIA](https://www.nvidia.com/) as part of the [Newton](https://github.com/newton-physics/newton) project.

# Getting started

MuJoCo Warp requires an NVIDIA GPU for fast simulation but supports CPU for development and debugging.

**Try it now:** view a simulation of a dancing humanoid robot locally on your machine:

```bash
git clone https://github.com/google-deepmind/mujoco_warp.git && cd mujoco_warp
python benchmarks/run.py -f unitree_g1_flat --view
```

Or try out [a tutorial in your browser](https://colab.research.google.com/github/google-deepmind/mujoco_warp/blob/main/notebooks/tutorial.ipynb) (no local setup required).

MJWarp is also available via PyPI:

```bash
pip install mujoco-warp
```

# Examples

MuJoCo Warp simulates many kinds of physical systems, from rigid bodies with contacts to soft bodies, cloth, signed distance fields, and more. Here are a few examples of what it can do:

<table>
  <tr>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/unitree_g1/rollout_flat.webp" alt="Unitree G1">
      <br><b>python benchmarks/run.py -f unitree_g1_flat --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/unitree_g1/rollout_hfield.webp" alt="Unitree G1 Heightfield">
      <br><b>python benchmarks/run.py -f unitree_g1_hfield --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/myosim/rollout.webp" alt="MyoArm">
      <br><b>python benchmarks/run.py -f myoarm --view</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/aloha/rollout_clutter.webp" alt="ALOHA Clutter">
      <br><b>python benchmarks/run.py -f aloha_clutter --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/aloha/rollout_pot.webp" alt="ALOHA Pot">
      <br><b>python benchmarks/run.py -f aloha_pot --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/aloha/rollout_sdf.webp" alt="ALOHA SDF">
      <br><b>python benchmarks/run.py -f aloha_sdf --view</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/aloha/rollout_cloth.webp" alt="ALOHA Cloth">
      <br><b>python benchmarks/run.py -f aloha_cloth --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/humanoid/rollout_three_humanoids.webp" alt="Three Humanoids">
      <br><b>python benchmarks/run.py -f three_humanoids --view</b>
    </td>
    <td align="center" width="33%">
      <img width="320" src="benchmarks/cloth/rollout.webp" alt="Cloth">
      <br><b>python benchmarks/run.py -f cloth --view</b>
    </td>
  </tr>
</table>

Each of these scenes is benchmarked nightly and the [results are published nightly](https://google-deepmind.github.io/mujoco_warp/nightly/).

# Tips for developers

To set up MJWarp for development:

```bash
git clone https://github.com/google-deepmind/mujoco_warp.git && cd mujoco_warp
uv sync --all-extras  # install all optional dependencies for development
uv run pre-commit install  # enables ruff, uv-lock, and kernel-analyzer checks on commit
uv run pytest -n 8  # run all tests, verify everything works
```

If you plan to write Warp kernels for MJWarp, please use the `kernel_analyzer` vscode plugin located in [`contrib/kernel_analyzer`](https://github.com/google-deepmind/mujoco_warp/tree/main/contrib/kernel_analyzer).
See the [README](https://github.com/google-deepmind/mujoco_warp/blob/main/contrib/kernel_analyzer/README.md) there for details on how to install it and use it.  The same kernel analyzer will run on any PR
you open, so it's important to fix any issues it reports.

For performance profiling MJWarp, use the `--event_trace` flag on `mjwarp-testspeed` to get a full trace on a test scene of your choice:

```bash
mjwarp-testspeed benchmarks/humanoid/humanoid.xml --event_trace
```

`mjwarp-testspeed` has many configuration options, see ```mjwarp-testspeed --help``` for details.  For more details and advanced topics on using MJWarp, see the [MuJoCo Warp documentation](https://mujoco.readthedocs.io/en/latest/mjwarp/index.html).

# Integrating MuJoCo Warp

There are many ways to use MuJoCo Warp in your projects. In many cases, you can directly install and use MJWarp as a drop-in replacement for MuJoCo.

If you prefer the [JAX](https://github.com/jax-ml/jax) ecosystem, you can use MJWarp via [MJX](https://mujoco.readthedocs.io/en/stable/mjx.html).  See [MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground) for robotics machine learning recipes that use [JAX](https://github.com/jax-ml/jax) and MJWarp.

If you prefer [PyTorch](https://pytorch.org/) for research, consider one of these two great options:

* [Isaac Lab](https://github.com/isaac-sim/IsaacLab/tree/feature/newton) integrates MJWarp via [Newton](https://github.com/newton-physics/newton).  This setup enables powerful, highly extensible multi-physics simulation with deep NVIDIA ecosystem integration.
* [mjlab](https://github.com/mujocolab/mjlab) exposes the [Isaac Lab](https://github.com/isaac-sim/IsaacLab) manager-based API directly on top of MJWarp, providing a focused framework for robotics research with minimal dependencies and direct access to native MuJoCo data structures.

# MuJoCo API Compatibility

MuJoCo Warp supports the same features as MuJoCo with the following exceptions:

- **Integrator**: `IMPLICITFAST` midpoint integrator feature is not supported
- **Solver**: `PGS` and `noslip` not yet supported
- **Actuator / Sensors**: `PLUGIN` types not yet supported
- **Flex**: experimental — not all features are implemented or optimized yet

[Differentiability via Warp](https://nvidia.github.io/warp/user_guide/differentiability.html) is not yet available. See [#500](https://github.com/google-deepmind/mujoco_warp/issues/500) for progress.

# Batch Rendering

MJWarp includes a **high-throughput** GPU batch renderer designed for simultaneous rendering of cameras across many parallel simulation worlds. The renderer uses ray-tracing to render MuJoCo scenes at millions of frames per second on NVIDIA GPUs.

Key capabilities:
- Mesh rendering
- Texture support
- Heightfield rendering
- Flex deformable rendering
- Gaussian splat rendering
- Heterogeneous multi-camera support (different resolutions/FOV/intrinsics for each camera)
- Lighting and shadow support

See the [announcement PR](https://github.com/google-deepmind/mujoco_warp/pull/1113) for more details.

# License

MJWarp is released under the Apache 2.0 license. See [LICENSE](LICENSE) for details.


## File tree (depth 3, assets pruned)

```
.agent/
  rules/
    project.md
.github/
  workflows/
    ci.yml
    nightly.yml
    pypi.yml
.gitignore
.pre-commit-config.yaml
AGENTS.md
AUTHORS
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
benchmarks/
  README.md
  aloha/
    README.md
    __init__.py
    aloha_clutter_vision.webp
    lift_cloth.npz
    lift_pot.npz
    pick_clutter.npz
    rollout_cloth.webp
    rollout_clutter.webp
    rollout_pot.webp
    rollout_sdf.webp
    scene_cloth.xml
    scene_clutter.xml
    scene_pot.xml
    scene_sdf.xml
  cloth/
    README.md
    __init__.py
    mannequin.xml
    rollout.webp
    rollout_cloth_render.webp
    scene.xml
  common.py
  franka_emika_panda/
    README.md
    __init__.py
    panda.xml
    rollout.webp
    scene.xml
  humanoid/
    README.md
    __init__.py
    humanoid.xml
    rollout_humanoid.webp
    rollout_three_humanoids.webp
    three_humanoids.xml
  kitchen/
    CHANGELOG.md
    LICENSE
    README.md
    kitchen.xml
    kitchen_1.png
    kitchen_2.png
    populate_scene.py
  myosim/
    README.md
    __init__.py
    rollout.webp
  render/
    README.md
    __init__.py
    primitives.webp
    primitives.xml
  run.py
  sweep.py
  unitree_g1/
    README.md
    __init__.py
    rollout_flat.webp
    rollout_hfield.webp
    rollout_hfield_render.webp
    scene_flat.xml
    scene_hfield.xml
    shuffle_dance.npz
    unitree_g1_mjlab.xml
contrib/
  README.md
  apptronik_apollo_locomotion.ipynb
  jax_unroll.py
  kernel_analyzer/
    .vscodeignore
    README.md
    client/
    kernel-analyzer-0.5.0.vsix
    kernel-analyzer-0.6.0.vsix
    kernel-analyzer-0.7.0.vsix
    kernel-analyzer-0.7.1.vsix
    kernel-analyzer-0.8.0.vsix
    kernel_analyzer/
    out/
    package-lock.json
    package.json
  render.py
  systemd/
    README.md
    mjwarp-nightly.service
    mjwarp-nightly.timer
  xml/
    apptronik_apollo.xml
    scene.xml
mujoco_warp/
  __init__.py
  _src/
    __init__.py
    block_cholesky.py
    broadphase_test.py
    bvh.py
    bvh_test.py
    cli.py
    collision_convex.py
    collision_core.py
    collision_driver.py
    collision_driver_test.py
    collision_flex.py
    collision_gjk.py
    collision_gjk_test.py
    collision_primitive.py
    collision_primitive_core.py
    collision_primitive_core_test.py
    collision_sdf.py
    constraint.py
    constraint_test.py
    derivative.py
    derivative_test.py
    flex_test.py
    forward.py
    forward_test.py
    history.py
    history_test.py
    inverse.py
    inverse_test.py
    io.py
    io_jax_test.py
    io_test.py
    island.py
    island_test.py
    jax_test.py
    math.py
    math_test.py
    passive.py
    passive_test.py
    ray.py
    ray_test.py
    render.py
    render_test.py
    render_util.py
    render_util_test.py
    sensor.py
    sensor_test.py
    set_const.py
    set_const_test.py
    sleep.py
    sleep_test.py
    smooth.py
    smooth_test.py
    solver.py
    solver_test.py
    support.py
    support_test.py
    types.py
    types_test.py
    unroll_test.py
    util_misc.py
    util_misc_test.py
    util_pkg.py
    util_pkg_test.py
    warp_util.py
  conftest.py
  record.py
  test_data/
    __init__.py
    actuation/
    aloha_pot/
    collision.xml
    collision_sdf/
    constraints.xml
    convex_collision/
    flex/
    hfield/
    humanoid/
    jdotv/
    mug/
    pendula.xml
    primitives.xml
    ray.xml
    skybox/
    tendon/
  testspeed.py
  viewer.py
notebooks/
  tutorial.ipynb
pyproject.toml
uv.lock
```

## Config files (1)


### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.14 # Use the latest Ruff version
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0 # Use the latest version
    hooks:
      - id: check-yaml
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.9.27
    hooks:
      - id: uv-lock
  - repo: local
    hooks:
      - id: kernel-analyzer
        name: kernel-analyzer
        entry: uv run python contrib/kernel_analyzer/kernel_analyzer/cli.py
        language: system
        types: [python]

```

## Python signatures and reward/observation bodies (3 files)


### mujoco_warp/_src/constraint.py

```
def _add_weight(nb, body, weight, b, w, check_weld)
def _zero_constraint_counts(ne_out, nf_out, nl_out, nefc_out, efc_jtdaj_nblock_out, efc_nnz_out)
def _contact_kbimp(opt_disableflags, timestep, solref, solimp, pos_imp)
def _efc_D(invweight, imp)
def _efc_row(opt_disableflags, worldid, timestep, efcid, pos_aref, pos_imp, invweight, solref, solimp, margin, vel, frictionloss, type, id, type_out, id_out, pos_out, margin_out, D_out, vel_out, aref_out, frictionloss_out)
def _equality_connect(is_sparse, newton)
def _equality_joint(is_sparse, newton)
def _equality_tendon(is_sparse, newton)
def _equality_flex(is_sparse, newton)
def _equality_weld(is_sparse, newton)
def _equality_flexstrain(is_sparse, newton)
def _friction_dof(is_sparse, newton)
def _friction_tendon(is_sparse, newton)
def _limit_slide_hinge(is_sparse, newton)
def _limit_ball(is_sparse, newton)
def _limit_tendon(is_sparse, newton)
def _get_contact_bodies_and_weights(geom_bodyid, flex_dim, flex_cellnum, flex_nodeadr, flex_vertadr, flex_elemdataadr, flex_shelldataadr, flex_nodebodyid, flex_vertbodyid, flex_elem, flex_shell, flex_vert0, flexvert_xpos_in, conid, side, geom, flex, elem, vert, con_pos, worldid)
def _efc_contact_init(cone_type, is_sparse, newton, flg_adhesion)
def _efc_contact_init_flex(cone_type, is_sparse, newton, flg_adhesion)
def _efc_contact_jac_sparse(cone_type)
def _efc_contact_jac_sparse_flex(cone_type)
def _efc_contact_jac_dense(tile_size, cone_type)
def _efc_contact_jac_dense_flex(tile_size, cone_type)
def _efc_contact_update(cone_type, flg_adhesion)
def _efc_contact_update_flex(cone_type, flg_adhesion)
def _geom_surface_velocity(geom_xpos_val, geom_xmat_val, surfacevel_val, point_val)
def _add_surface_vel(is_pyramidal)
def make_constraint(m, d)
```

### mujoco_warp/_src/constraint_test.py

```
"""Tests for constraint functions."""
def _assert_eq(a, b, name, tol)
def _assert_efc_eq(mjm, m, d, mjd, nefc, name, nv, tol)
class ConstraintTest(TestCase)
    def test_condim(self, cone, condims, jacobian)
    def test_constraints(self, xml, cone, jacobian)
    def test_limit_tendon(self, jacobian)
    def test_equality_tendon(self, jacobian)
    def test_efc_address_inactive_contacts(self)
    def test_jdotv(self, xml, jacobian)
    def test_flex_barycentric_jacobian(self, xml, cone, jacobian)
    def test_flex_3d_simplex_collision(self)
    def test_flex_interpolated(self)
    def test_weld_coriolis(self)
    def test_surfacevel(self, xml, cone, jacobian)
```