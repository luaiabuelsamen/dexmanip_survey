# comfree_sim_2026

source: https://github.com/asu-iris/comfree_warp


commit: ba8b9969f5f7859d51b1f738f458f8d2f49be080


## README

# ComFree-Sim: GPU-Parallelized Analytical Contact Physics Engine

![Teaser](teaser.jpg)

ComFree-Sim is a GPU-parallelized analytical contact physics engine designed for scalable contact-rich robotics simulation and control. This engine provides efficient simulation of complex interaction dynamics while exploiting modern GPU hardware for significant computational speedup.

## Overview

ComFree-Sim enables fast and accurate simulation of robots interacting with their environment through contacts. The engine supports large-scale parallel simulations, making it ideal for:

- Contact-rich robotics tasks (manipulation, locomotion, etc.)
- Multi-environment parallel simulation
- GPU-accelerated physics simulation
- Scalable simulation pipelines for learning and control

## Resources

- **Project Website**: https://irislab.tech/comfree-sim/
- **Documentation**: https://irislab.tech/comfree-doc/intro.html
- **Paper (arXiv)**: https://arxiv.org/abs/2603.12185

## Installation

Install the package using UV package manager:

```bash
uv sync
```

Or with pip:

```bash
pip install .
```


## Quick Start

### Local Viewer Simulation

Run an interactive simulation with the native MuJoCo viewer:

```bash
python test_local/test_viewer.py
```

This script loads a test scene and displays the simulation in real time using the built-in MuJoCo viewer. You can modify the `engine` variable (`0=MJC`, `1=MJWARP`, `2=COMFREE_WARP`) to compare different simulation backends directly on a local machine; the default is `COMFREE_WARP`. You can also switch `model_path` to try other XML scenes such as `benchmark/humanoid/n_humanoid.xml`, `benchmark/test_data/collision.xml`, `benchmark/test_data/flex/floppy.xml`, `benchmark/test_data/hfield/hfield.xml`, and `benchmark/leap/env_leap_cube.xml`.

### Local Franka Grasp Test

Run the Franka cube-grasp benchmark locally:

```bash
python test_local/test_franka_grasp.py
```

Available backends are `mujoco`, `mjwarp`, and `comfree`, with `comfree` as the default.

### Throughput Benchmarking

Run a throughput benchmark with parallel hand simulation:

```bash
python test_local/test_throuput_hand.py
```

This script evaluates the performance of different engines with parallel environments. It benchmarks:
- MuJoCo Warp
- ComFree

Results include throughput metrics and step time statistics across multiple parallel environments.

### Headless Streaming Simulation

Run a headless simulation and stream state to a local viewer:

```bash
python test_headless/test_streaming.py
```

By default this waits for a viewer connection on `MJSTREAM_PORT=7000` and streams the MuJoCo state over TCP.
Like the local viewer test, you can change the `engine` setting (`0=MJC`, `1=MJWARP`, `2=COMFREE_WARP`), with `COMFREE_WARP` as the default, and switch `model_path` to try other XML scenes such as `benchmark/humanoid/n_humanoid.xml`, `benchmark/test_data/collision.xml`, `benchmark/test_data/flex/floppy.xml`, `benchmark/test_data/hfield/hfield.xml`, and `benchmark/leap/env_leap_cube.xml`.

### Headless Franka Grasp Streaming

Run the Franka grasp benchmark headlessly and stream it to the viewer:

```bash
python test_headless/test_franka_grasp.py
```

You can override the stream endpoint with `MJSTREAM_HOST` and `MJSTREAM_PORT`.
This benchmark also supports multiple backends through `--engine` with `mujoco`, `mjwarp`, or `comfree`; the default is `comfree`.


### Python API

```python
import comfree_warp as cfwarp

# Create your simulation environment
# See documentation for detailed examples
```

For comprehensive examples and tutorials, visit the [documentation](https://irislab.tech/comfree-doc/intro.html).

## License

This repository contains materials under multiple licenses:

- Repository-wide licensing notice: `LICENSE`
- `comfree_warp/comfree_core/`: noncommercial academic research license in `comfree_warp/comfree_core/LICENSE`
- Vendored `comfree_warp/mujoco_warp/` upstream code: Apache License 2.0; see `LICENSES/Apache-2.0.txt`


## Citation

If you use ComFree-Sim in your research, please cite:

```bibtex
@article{borse2026comfree,
  title={ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and Control},
  author={Borse, Chetan and Xie, Zhixian and Huang, Wei-Cheng and Jin, Wanxin},
  journal={arXiv preprint arXiv:2603.12185},
  year={2026}
}
```

## Acknowledgments

We thank the MuJoCo Warp (MJWarp) team at Google DeepMind and NVIDIA for making their code publicly available.


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
LICENSES/
  Apache-2.0.txt
README.md
benchmark/
  __init__.py
  franka_cube_grasp/
    panda.xml
    scene.xml
  humanoid/
    humanoid.xml
    n_humanoid.xml
  leap/
    env_leap_cube.xml
    leap_hand/
    leap_right_hand.xml
    objects/
    textures/
  test_data/
    __init__.py
    allegro/
    ball_rotation.xml
    collision.xml
    constraints.xml
    cylinder_rolling.xml
    flex/
    general_block.png
    hfield/
    pendula.xml
    primitives.xml
    ray.xml
comfree_warp/
  __init__.py
  api.py
  comfree_core/
    LICENSE
    __init__.py
    _src/
  mujoco_warp/
    __init__.py
    _src/
    conftest.py
    test_data/
    testspeed.py
    viewer.py
pyproject.toml
teaser.jpg
test_headless/
  streaming.py
  test_franka_grasp.py
  test_streaming.py
test_local/
  test_franka_grasp.py
  test_throuput_hand.py
  test_viewer.py
```

## Config files (0)


## Python signatures and reward/observation bodies (4 files)


### comfree_warp/comfree_core/_src/constraint.py

```
"""Assembles Warp constraint rows and Jacobians for equality, friction, limit, and contact constraints."""
def _zero_constraint_counts(ne_out, nf_out, nl_out, nefc_out, efc_nnz_out)
def _efc_row(opt_disableflags, worldid, timestep, efcid, pos_aref, pos_imp, invweight, solref, solimp, margin, vel, frictionloss, type, id, type_out, id_out, pos_out, margin_out, D_out, vel_out, aref_out, frictionloss_out, efc_dist_out, efc_mass_out)
def _equality_connect(nv, nsite, opt_timestep, opt_disableflags, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, site_bodyid, eq_obj1id, eq_obj2id, eq_objtype, eq_solref, eq_solimp, eq_data, is_sparse, eq_connect_adr, qvel_in, eq_active_in, xpos_in, xmat_in, site_xpos_in, subtree_com_in, cdof_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _equality_joint(nv, opt_timestep, opt_disableflags, qpos0, jnt_qposadr, jnt_dofadr, dof_invweight0, eq_obj1id, eq_obj2id, eq_solref, eq_solimp, eq_data, is_sparse, eq_jnt_adr, qpos_in, qvel_in, eq_active_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _equality_tendon(nv, opt_timestep, opt_disableflags, eq_obj1id, eq_obj2id, eq_solref, eq_solimp, eq_data, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_length0, tendon_invweight0, is_sparse, eq_ten_adr, qvel_in, eq_active_in, ten_J_in, ten_length_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _equality_flex(is_sparse)
def _equality_weld(nv, nsite, opt_timestep, opt_disableflags, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, site_bodyid, site_quat, eq_obj1id, eq_obj2id, eq_objtype, eq_solref, eq_solimp, eq_data, is_sparse, eq_wld_adr, qvel_in, eq_active_in, xpos_in, xquat_in, xmat_in, site_xpos_in, subtree_com_in, cdof_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _friction_dof(nv, opt_timestep, opt_disableflags, dof_solref, dof_solimp, dof_frictionloss, dof_invweight0, is_sparse, qvel_in, njmax_in, nf_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _friction_tendon(nv, opt_timestep, opt_disableflags, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_solref_fri, tendon_solimp_fri, tendon_frictionloss, tendon_invweight0, is_sparse, qvel_in, ten_J_in, njmax_in, nf_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _limit_slide_hinge(nv, opt_timestep, opt_disableflags, jnt_qposadr, jnt_dofadr, jnt_solref, jnt_solimp, jnt_range, jnt_margin, dof_invweight0, is_sparse, jnt_limited_slide_hinge_adr, qpos_in, qvel_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _limit_ball(nv, opt_timestep, opt_disableflags, jnt_qposadr, jnt_dofadr, jnt_solref, jnt_solimp, jnt_range, jnt_margin, dof_invweight0, is_sparse, jnt_limited_ball_adr, qpos_in, qvel_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _limit_tendon(nv, opt_timestep, opt_disableflags, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_solref_lim, tendon_solimp_lim, tendon_range, tendon_margin, tendon_invweight0, is_sparse, tendon_limited_adr, qvel_in, ten_J_in, ten_length_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def _contact_pyramidal(nv, opt_timestep, opt_disableflags, opt_impratio_invsqrt, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, geom_bodyid, flex_vertadr, flex_vertbodyid, is_sparse, qvel_in, subtree_com_in, cdof_in, njmax_in, nacon_in, dist_in, condim_in, includemargin_in, worldid_in, geom_in, flex_in, vert_in, pos_in, frame_in, friction_in, solref_in, solimp_in, type_in, nefc_out, contact_efc_address_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out, efc_dist_out, efc_mass_out)
def make_constraint(m, d)
```

### comfree_warp/mujoco_warp/_src/constraint.py

```
def _zero_constraint_counts(ne_out, nf_out, nl_out, nefc_out, efc_nnz_out)
def _efc_row(opt_disableflags, worldid, timestep, efcid, pos_aref, pos_imp, invweight, solref, solimp, margin, vel, frictionloss, type, id, type_out, id_out, pos_out, margin_out, D_out, vel_out, aref_out, frictionloss_out)
def _equality_connect(nv, nsite, opt_timestep, opt_disableflags, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, site_bodyid, eq_obj1id, eq_obj2id, eq_objtype, eq_solref, eq_solimp, eq_data, is_sparse, eq_connect_adr, qvel_in, eq_active_in, xpos_in, xmat_in, site_xpos_in, subtree_com_in, cdof_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _equality_joint(nv, opt_timestep, opt_disableflags, qpos0, jnt_qposadr, jnt_dofadr, dof_invweight0, eq_obj1id, eq_obj2id, eq_solref, eq_solimp, eq_data, is_sparse, eq_jnt_adr, qpos_in, qvel_in, eq_active_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _equality_tendon(nv, opt_timestep, opt_disableflags, eq_obj1id, eq_obj2id, eq_solref, eq_solimp, eq_data, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_length0, tendon_invweight0, is_sparse, eq_ten_adr, qvel_in, eq_active_in, ten_J_in, ten_length_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _equality_flex(is_sparse)
def _equality_weld(nv, nsite, opt_timestep, opt_disableflags, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, site_bodyid, site_quat, eq_obj1id, eq_obj2id, eq_objtype, eq_solref, eq_solimp, eq_data, is_sparse, eq_wld_adr, qvel_in, eq_active_in, xpos_in, xquat_in, xmat_in, site_xpos_in, subtree_com_in, cdof_in, njmax_in, ne_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _friction_dof(nv, opt_timestep, opt_disableflags, dof_solref, dof_solimp, dof_frictionloss, dof_invweight0, is_sparse, qvel_in, njmax_in, nf_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _friction_tendon(nv, opt_timestep, opt_disableflags, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_solref_fri, tendon_solimp_fri, tendon_frictionloss, tendon_invweight0, is_sparse, qvel_in, ten_J_in, njmax_in, nf_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _limit_slide_hinge(nv, opt_timestep, opt_disableflags, jnt_qposadr, jnt_dofadr, jnt_solref, jnt_solimp, jnt_range, jnt_margin, dof_invweight0, is_sparse, jnt_limited_slide_hinge_adr, qpos_in, qvel_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _limit_ball(nv, opt_timestep, opt_disableflags, jnt_qposadr, jnt_dofadr, jnt_solref, jnt_solimp, jnt_range, jnt_margin, dof_invweight0, is_sparse, jnt_limited_ball_adr, qpos_in, qvel_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _limit_tendon(nv, opt_timestep, opt_disableflags, ten_J_rownnz, ten_J_rowadr, ten_J_colind, tendon_solref_lim, tendon_solimp_lim, tendon_range, tendon_margin, tendon_invweight0, is_sparse, tendon_limited_adr, qvel_in, ten_J_in, ten_length_in, njmax_in, nl_out, nefc_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _contact_pyramidal(nv, opt_timestep, opt_disableflags, opt_impratio_invsqrt, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, geom_bodyid, flex_vertadr, flex_vertbodyid, is_sparse, qvel_in, subtree_com_in, cdof_in, njmax_in, nacon_in, dist_in, condim_in, includemargin_in, worldid_in, geom_in, flex_in, vert_in, pos_in, frame_in, friction_in, solref_in, solimp_in, type_in, nefc_out, contact_efc_address_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def _contact_elliptic(nv, opt_timestep, opt_disableflags, opt_impratio_invsqrt, body_parentid, body_rootid, body_weldid, body_dofnum, body_dofadr, body_invweight0, dof_bodyid, dof_parentid, geom_bodyid, flex_vertadr, flex_vertbodyid, is_sparse, qvel_in, subtree_com_in, cdof_in, njmax_in, nacon_in, dist_in, condim_in, includemargin_in, worldid_in, geom_in, flex_in, vert_in, pos_in, frame_in, friction_in, solref_in, solreffriction_in, solimp_in, type_in, nefc_out, contact_efc_address_out, efc_type_out, efc_id_out, efc_J_rownnz_out, efc_J_rowadr_out, efc_J_colind_out, efc_J_out, efc_pos_out, efc_margin_out, efc_D_out, efc_vel_out, efc_aref_out, efc_frictionloss_out, efc_nnz_out)
def make_constraint(m, d)
```

### comfree_warp/mujoco_warp/_src/constraint_test.py

```
"""Tests for constraint functions."""
def _assert_eq(a, b, name)
def _assert_efc_eq(mjm, m, d, mjd, nefc, name, nv)
class ConstraintTest(TestCase)
    def test_condim(self, cone, condims, jacobian)
    def test_constraints(self, xml, cone, jacobian)
    def test_limit_tendon(self, jacobian)
    def test_equality_tendon(self, jacobian)
    def test_efc_address_inactive_contacts(self)
```

### test_local/test_throuput_hand.py

```
"""Throughput test with 1024 parallel environments.

Logs per-step total contact count (across all environments) and step time."""
def run_hand_test(num_steps, nworld, engine, model_path, nconmax, njmax, contact_stiffness, contact_damping, qvel_noise_std)
```