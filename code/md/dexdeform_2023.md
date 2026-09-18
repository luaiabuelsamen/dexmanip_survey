# dexdeform_2023

source: https://github.com/sizhe-li/DexDeform


commit: 72f5087ed4e46cf88092f36d6ced9a72978d8c01


## README

# DexDeform
Code and data for paper [DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics](https://openreview.net/pdf?id=LIV7-_7pYPl) at ICLR 2023.

![Alt Text](https://github.com/lester0866/DexDeform/blob/main/misc/flip.gif)

# Installation

```bash
conda env create -f environment.yml
conda activate dexdeform
pip install -e .
```

##### Install Sinkhorn Distance Metric

```bash
pip install pykeops
pip install geomloss
```


# Download Demonstrations

Download [here](https://drive.google.com/drive/folders/1xVS9ui5eHVCBFvmIAQ_mRqacEj-0__Hr?usp=sharing). For loading demonstrations, checkout `tutorials/demonstration_loading.ipynb`.

# Tutorials

- [Environment Loading] `tutorials/1_environment_loading.ipynb`
- [Trajectory Optimization] `tutorials/2_trajectory_optimization.ipynb`
- [Leap motion tracking module] `leap_motion/`
- [Demonstration Loading] `tutorials/3_demonstration_loading.ipynb`
- [Computing Score] `tutorials/4_computing_score.ipynb`

# Implementation Details

- Our simulation backend supports full differentiability and communications with PyTorch modules.
- For optimal performance, the simulation backend is written in CUDA and implements PlasticineLab. 
- We provide python wrapper for the dexterous hand environment, located inside `hand.py`. 

# Acknowledgements

- Our physics simulation is written based on [PlasticineLab](https://github.com/hzaskywalker/PlasticineLab).
- Our leap motion tracking module is written based on [this repo](https://github.com/szahlner/shadow-teleop/tree/main/leap_motion).


# TODO
- [x] Support for Human Teleoperation (Leap motion tracking module released, synchronization with simulation coming soon)
- [x] Release demonstrations
- [x] Support for DexDeform Algorithm (template uploaded, cleanup needed to support dataloding.)

# Citation

```bibtex
@inproceedings{
li2023dexdeform,
title={DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics},
author={Sizhe Li and Zhiao Huang and Tao Chen and Tao Du and Hao Su and Joshua B. Tenenbaum and Chuang Gan},
booktitle={International Conference on Learning Representations},
year={2023},
url={https://openreview.net/forum?id=LIV7-_7pYPl}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
environment.yml
leap_motion/
  .DS_Store
  setup.py
  tracking/
    LeapSDK/
    __init__.py
    main.py
misc/
  flip.gif
mpm/
  __init__.py
  csrc/
    array.h
    common.h
    ctpl_stl.h
    integrator.cu
    mat3.h
    model.h
    quat.h
    shape.h
    svd.h
    vec3.h
  cuda_env.py
  hand.py
  mujoco_parser.py
  renderer.py
  robots/
    interface.py
  shapes.py
  simulator.py
  torch_wrapper.py
  types.py
  video_utils.py
  viewer.py
policy/
  checkpoints.py
  config.py
  dataset/
    __init__.py
    base.py
    loader.py
    pcd_transforms.py
    skill_dataset.py
  perception/
    common.py
    decoder/
    encoder/
    layers.py
    scene_vae/
    utils/
  preprocess/
    __init__.py
    preprocess_plab.py
  skill/
    __init__.py
    config.py
    generation.py
    models/
    skill_planning.py
    skillnet.py
    skillnet_prior.py
    training.py
  training.py
  utils/
    io.py
scripts/
  model_training/
    perception/
    skill/
setup.py
tools/
  __init__.py
  config/
    __init__.py
    cfgNode.py
    configurable.py
    parse_args.py
    tester/
tutorials/
  1_trajectory_optimization.ipynb
  2_environment_loading.ipynb
  3_demonstration_loading.ipynb
  4_computing_score.ipynb
```

## Config files (2)


### environment.yml

```yaml
name: dexdeform
channels:
  - pytorch3d
  - iopath
  - pytorch
  - conda-forge
  - defaults
dependencies:
  - _libgcc_mutex=0.1=main
  - _openmp_mutex=5.1=1_gnu
  - anyio=3.5.0=py39h06a4308_0
  - argon2-cffi=21.3.0=pyhd3eb1b0_0
  - argon2-cffi-bindings=21.2.0=py39h7f8727e_0
  - asttokens=2.0.5=pyhd3eb1b0_0
  - attrs=22.1.0=py39h06a4308_0
  - babel=2.11.0=py39h06a4308_0
  - backcall=0.2.0=pyhd3eb1b0_0
  - beautifulsoup4=4.11.1=py39h06a4308_0
  - blas=1.0=mkl
  - bleach=4.1.0=pyhd3eb1b0_0
  - brotlipy=0.7.0=py39h27cfd23_1003
  - bzip2=1.0.8=h7b6447c_0
  - ca-certificates=2023.01.10=h06a4308_0
  - certifi=2022.12.7=py39h06a4308_0
  - cffi=1.15.1=py39h74dc2b5_0
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - colorama=0.4.6=pyhd8ed1ab_0
  - comm=0.1.2=py39h06a4308_0
  - cryptography=38.0.4=py39h9ce1e76_0
  - cudatoolkit=11.3.1=h2bc3f7f_2
  - dbus=1.13.18=hb2f20db_0
  - debugpy=1.5.1=py39h295c915_0
  - defusedxml=0.7.1=pyhd3eb1b0_0
  - entrypoints=0.4=py39h06a4308_0
  - executing=0.8.3=pyhd3eb1b0_0
  - expat=2.4.9=h6a678d5_0
  - ffmpeg=4.3=hf484d3e_0
  - flit-core=3.6.0=pyhd3eb1b0_0
  - fontconfig=2.14.1=h52c9d5c_1
  - freetype=2.12.1=h4a9f257_0
  - fvcore=0.1.5.post20221221=pyhd8ed1ab_0
  - giflib=5.2.1=h5eee18b_1
  - glib=2.69.1=h4ff587b_1
  - gmp=6.2.1=h295c915_3
  - gnutls=3.6.15=he1e5248_0
  - gst-plugins-base=1.14.0=h8213a91_2
  - gstreamer=1.14.0=h28cd5cc_2
  - icu=58.2=he6710b0_3
  - idna=3.4=py39h06a4308_0
  - importlib-metadata=4.11.3=py39h06a4308_0
  - intel-openmp=2021.4.0=h06a4308_3561
  - iopath=0.1.9=py39
  - ipykernel=6.19.2=py39hb070fc8_0
  - ipython=8.10.0=py39h06a4308_0
  - ipython_genutils=0.2.0=pyhd3eb1b0_1
  - ipywidgets=7.6.5=pyhd3eb1b0_1
  - jedi=0.18.1=py39h06a4308_1
  - jinja2=3.1.2=py39h06a4308_0
  - jpeg=9e=h7f8727e_0
  - json5=0.9.6=pyhd3eb1b0_0
  - jsonschema=4.17.3=py39h06a4308_0
  - jupyter=1.0.0=py39h06a4308_8
  - jupyter_client=7.4.9=py39h06a4308_0
  - jupyter_console=6.4.4=py39h06a4308_0
  - jupyter_core=5.2.0=py39h06a4308_0
  - jupyter_server=1.23.4=py39h06a4308_0
  - jupyterlab=3.5.3=py39h06a4308_0
  - jupyterlab_pygments=0.1.2=py_0
  - jupyterlab_server=2.16.5=py39h06a4308_0
  - jupyterlab_widgets=1.0.0=pyhd3eb1b0_1
  - krb5=1.19.4=h568e23c_0
  - lame=3.100=h7b6447c_0
  - lcms2=2.12=h3be6417_0
  - ld_impl_linux-64=2.38=h1181459_1
  - lerc=3.0=h295c915_0
  - libclang=10.0.1=default_hb85057a_2
  - libdeflate=1.8=h7f8727e_5
  - libedit=3.1.20221030=h5eee18b_0
  - libevent=2.1.12=h8f2d780_0
  - libffi=3.3=he6710b0_2
  - libgcc-ng=11.2.0=h1234567_1
  - libgomp=11.2.0=h1234567_1
  - libiconv=1.16=h7f8727e_2
  - libidn2=2.3.2=h7f8727e_0
  - libllvm10=10.0.1=hbcb73fb_5
  - libpng=1.6.37=hbc83047_0
  - libpq=12.9=h16c4e8d_3
  - libsodium=1.0.18=h7b6447c_0
  - libstdcxx-ng=11.2.0=h1234567_1
  - libtasn1=4.16.0=h27cfd23_0
  - libtiff=4.5.0=h6a678d5_1
  - libunistring=0.9.10=h27cfd23_0
  - libuuid=1.41.5=h5eee18b_0
  - libuv=1.40.0=h7b6447c_0
  - libwebp=1.2.4=h11a3e52_0
  - libwebp-base=1.2.4=h5eee18b_0
  - libxcb=1.15=h7f8727e_0
  - libxkbcommon=1.0.1=hfa300c1_0
  - libxml2=2.9.14=h74e7548_0
  - libxslt=1.1.35=h4e12654_0
  - lxml=4.9.1=py39h1edc446_0
  - lz4-c=1.9.4=h6a678d5_0
  - markupsafe=2.1.1=py39h7f8727e_0
  - matplotlib-inline=0.1.6=py39h06a4308_0
  - mistune=0.8.4=py39h27cfd23_1000
  - mkl=2021.4.0=h06a4308_640
  - mkl-service=2.4.0=py39h7f8727e_0
  - mkl_fft=1.3.1=py39hd3c417c_0
  - mkl_random=1.2.2=py39h51133e4_0
  - nbclassic=0.5.2=py39h06a4308_0
  - nbclient=0.5.13=py39h06a4308_0
  - nbconvert=6.5.4=py39h06a4308_0
  - ncurses=6.4=h6a678d5_0
  - nest-asyncio=1.5.6=py39h06a4308_0
  - nettle=3.7.3=hbbd107a_1
  - notebook=6.5.2=py39h06a4308_0
  - notebook-shim=0.2.2=py39h06a4308_0
  - nspr=4.33=h295c915_0
  - nss=3.74=h0370c37_0
  - numpy=1.23.5=py39h14f4228_0
  - numpy-base=1.23.5=py39h31eccc5_0
  - openh264=2.1.1=h4ff587b_0
  - openssl=1.1.1t=h7f8727e_0
  - packaging=22.0=py39h06a4308_0
  - pandocfilters=1.5.0=pyhd3eb1b0_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pcre=8.45=h295c915_0
  - pexpect=4.8.0=pyhd3eb1b0_3
  - pickleshare=0.7.5=pyhd3eb1b0_1003
  - pillow=9.3.0=py39h6a678d5_2
  - pip=22.3.1=py39h06a4308_0
  - platformdirs=2.5.2=py39h06a4308_0
  - ply=3.11=py39h06a4308_0
  - portalocker=2.7.0=py39hf3d152e_0
  - prometheus_client=0.14.1=py39h06a4308_0
  - prompt-toolkit=3.0.36=py39h06a4308_0
  - prompt_toolkit=3.0.36=hd3eb1b0_0
  - psutil=5.9.0=py39h5eee18b_0
  - ptyprocess=0.7.0=pyhd3eb1b0_2
  - pure_eval=0.2.2=pyhd3eb1b0_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pygments=2.11.2=pyhd3eb1b0_0
  - pyopenssl=22.0.0=pyhd3eb1b0_0
  - pyqt=5.15.7=py39h6a678d5_1
  - pyqt5-sip=12.11.0=py39h6a678d5_1
  - pyrsistent=0.18.0=py39heee7806_0
  - pysocks=1.7.1=py39h06a4308_0
  - python=3.9.13=haa1d7c7_2
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - python-fastjsonschema=2.16.2=py39h06a4308_0
  - python_abi=3.9=2_cp39
  - pytorch=1.10.0=py3.9_cuda11.3_cudnn8.2.0_0
  - pytorch-mutex=1.0=cuda
  - pytorch3d=0.7.2=py39_cu113_pyt1100
  - pytz=2022.7=py39h06a4308_0
  - pyyaml=6.0=py39hb9d737c_4
  - pyzmq=23.2.0=py39h6a678d5_0
  - qt-main=5.15.2=h327a75a_7
  - qt-webengine=5.15.9=hd2b0992_4
  - qtconsole=5.4.0=py39h06a4308_0
  - qtpy=2.2.0=py39h06a4308_0
  - qtwebkit=5.212=h4eab89a_4
  - readline=8.2=h5eee18b_0
  - requests=2.28.1=py39h06a4308_0
  - send2trash=1.8.0=pyhd3eb1b0_1
  - setuptools=65.6.3=py39h06a4308_0
  - sip=6.6.2=py39h6a678d5_0
  - six=1.16.0=pyhd3eb1b0_1
  - sniffio=1.2.0=py39h06a4308_1
  - soupsieve=2.3.2.post1=py39h06a4308_0
  - sqlite=3.40.1=h5082296_0
  - stack_data=0.2.0=pyhd3eb1b0_0
  - tabulate=0.9.0=pyhd8ed1ab_1
  - termcolor=2.2.0=pyhd8ed1ab_0
  - terminado=0.17.1=py39h06a4308_0
  - tinycss2=1.2.1=py39h06a4308_0
  - tk=8.6.12=h1ccaba5_0
  - toml=0.10.2=pyhd3eb1b0_0
  - tomli=2.0.1=py39h06a4308_0
  - torchaudio=0.10.0=py39_cu113
  - torchvision=0.11.1=py39_cu113
  - tornado=6.2=py39h5eee18b_0
  - tqdm=4.64.1=pyhd8ed1ab_0
  - traitlets=5.7.1=py39h06a4308_0
  - typing-extensions=4.4.0=py39h06a4308_0
  - typing_extensions=4.4.0=py39h06a4308_0
  - tzdata=2022g=h04d1e81_0
  - urllib3=1.26.14=py39h06a4308_0
  - wcwidth=0.2.5=pyhd3eb1b0_0
  - webencodings=0.5.1=py39h06a4308_1
  - websocket-client=0.58.0=py39h06a4308_4
  - wheel=0.38.4=py39h06a4308_0
  - widgetsnbextension=3.5.2=py39h06a4308_0
  - xz=5.2.10=h5eee18b_1
  - yacs=0.1.8=pyhd8ed1ab_0
  - yaml=0.2.5=h7f98852_2
  - zeromq=4.3.4=h2531618_0
  - zipp=3.11.0=py39h06a4308_0
  - zlib=1.2.13=h5eee18b_0
  - zstd=1.5.2=ha4553b6_0
  - pip:
    - addict==2.4.0
    - click==8.1.3
    - configargparse==1.5.3
    - contourpy==1.0.7
    - cycler==0.11.0
    - dash==2.8.1
    - dash-core-components==2.0.0
    - dash-html-components==2.0.0
    - dash-table==5.0.0
    - decorator==4.4.2
    - flask==2.2.3
    - fonttools==4.38.0
    - imageio==2.25.1
    - imageio-ffmpeg==0.4.8
    - importlib-resources==5.12.0
    - itsdangerous==2.1.2
    - joblib==1.2.0
    - kiwisolver==1.4.4
    - matplotlib==3.7.0
    - moviepy==1.0.3
    - nbformat==5.5.0
    - open3d==0.16.0
    - pandas==1.5.3
    - plotly==5.13.0
    - proglog==0.1.10
    - pyparsing==3.0.9
    - pyquaternion==0.9.9
    - scikit-learn==1.2.1
    - scipy==1.10.1
    - tenacity==8.2.1
    - threadpoolctl==3.1.0
    - transforms3d==0.4.1
    - werkzeug==2.2.3

```

### tools/config/tester/test.yaml

```yaml
TYPE: td3
actor_optim:
  lr: 0.5
  method: "actor_method"
```

## Python signatures and reward/observation bodies (57 files)


### mpm/cuda_env.py

```
class CudaEnv(Configurable)
    def __init__(self, cfg, cfg_path, SIMULATOR, PRIMITIVES, RENDERER, SHAPES)
    def default_tool_config(self)
    def parse_tools(self, cfgs)
```

### mpm/hand.py

```
def rigid_body_motion_hand(state, actions, T)
class HandSimulator(MPMSimulator)
    def __init__(self, n_bodies, hand_cfg, cfg, quality, action_scale, device, mode, scale, ctrl_type, hand_friction, fixed_base)
    def togpu(self, x, dtype)
    def download_pos_rot(self, cur, device)
    def get_state(self, index)
    def set_state(self, index, state)
    def get_state_render_only(self, f, device)
    def set_state_render_only(self, p, base_pose, joint_rot, f)
    def lh_sdf_given_p(self, p)
    def rh_sdf_given_p(self, p)
    def primitive_sdf_given_p(self, p, hand_inds)
    def sample_pts_helper(self, num_points, hand_inds, center, hot_start)
    def sample_pts_inside_primitives(self, n_pts, mode, hot_start)
    def mat2pos_rot(self, mat)
    def hand_forward_kinematics(self, base_pose, q)
    def JointVel_Fk(self, f, actions, pos_rot)
    def step(self, action, q_state)
class HandEnv(CudaEnv)
    def __init__(self, cfg, MANIPULATORS, env_name)
    def initialize(self, root_frame, joint_pos)
    def set_particle_color(self, col)
    def render_rgb(self, index)
    def render_rgbd(self, index)
    def parse_manip_cfgs(self, cfgs)
    def parse_sim_cfg(self, cfg)
    def get_root_matrix(pos, rot)
    def set_single_hand_pose(self, hand_idx, pos, rot, joint_pos)
    def set_dual_hand_pose(self, pos, rot, joint_pos)
```

### mpm/simulator.py

```
def rigid_body_motion(states, actions)
class TempState()
    def __init__(self, n_particles, grid_dim, n_bodies)
    def clear(self, stream)
    def clear_grad(self, stream)
class State()
    def __init__(self, n_particles, n_bodies)
    def reset(self)
    def get_state(self, n)
    def set_state(self, state)
    def clear_grad(self, stream)
class MPMSimulator(Configurable)
    def __init__(self, n_bodies, cfg, ground_friction, gravity, n_particles, dx, dt, grid_size, max_steps, substeps, yield_stress, vol, mass, E, nu)
    def clear_grad(self, max_steps)
    def get_state(self, index)
    def set_state(self, index, state)
    def set_object_id(self, object_id)
    def get_object_id(self, device)
    def set_color(self, inp)
    def set_softness(self, softness)
    def get_softness(self)
    def _initialize_buffer(self, device, dims, dtype)
    def get_x(self, index, device)
    def get_v(self, index, device)
    def get_dists(self, f, grad, device)
    def compute_grid_mass(self, f, id, device, backward_grad)
    def compute_svd(self, index, device, backward_grad)
    def get_tool_state(self, index, device)
    def set_tool_state(self, index, pose)
    def get_action_scales(self)
    def init_particles(self, vol, mass, mu_lam_yield)
    def init_bodies(self, types, softness, mu, round, args, action_scales, pos, rot)
    def sync(self)
    def __del__(self)
    def nan_check(self, i, message)
    def compute_grid_lower(self, state, temp)
    def compute_svd(self, state, temp)
    def compute_svd_grad(self, state, temp)
    def p2g(self, state1, temp, state2)
    def p2g_grad(self, state1, temp, state2)
    def get_ground_friction(self)
    def get_ground_height(self)
    def grid_op(self, state1, temp, state2)
    def grid_op_grad(self, state1, temp, state2)
    def g2p(self, state1, temp, state2)
    def g2p_grad(self, state1, temp, state2)
    def set_pose(self, state, pos, rot, stream)
    def substep(self, f, clear_grad)
    def substep_grad(self, f)
    def download_pos_rot(self, cur, device)
    def compute_forward_kinematics(self, f, action, pos_rot)
    def step(self, action, pos_rot)
```

### policy/checkpoints.py

```
class CheckpointIO(object)
    """CheckpointIO class.

It handles saving and loading checkpoints.

Args:
    checkpoint_dir (str): path where checkpoints are saved"""
    def __init__(self, checkpoint_dir, distributed, rank)
    def load_model_only(self, filename)
    def register_modules(self)
    def save(self, filename)
    def load(self, filename)
    def load_file(self, filename)
    def load_url(self, url)
    def parse_state_dict(self, state_dict)
def is_url(url)
```

### policy/config.py

```
def load_config(path, default_path)
def update_recursive(dict1, dict2)
def get_model(cfg, device)
def get_trainer(model, optimizer, cfg, device)
def get_generator(model, cfg, device)
```

### policy/dataset/base.py

```
def np_to_th(x)
def create_zeros_and_fill(x, shape, dtype, mask)
def subsample(data_dict, num_points)
class PlabSceneDataset(Dataset)
    def __init__(self, cfg, env_name, split)
    def __len__(self)
    def __getitem__(self, idx)
    def load_train(self, src_data)
    def load_eval(self, src_data)
```

### policy/dataset/loader.py

```
def collate_pair_fn(batch)
def worker_init_fn(worker_id)
def get_plab_dataset(cfg, env_name, split, distributed)
def get_plab_loader(cfg, env_name, split, distributed, distributed_cfg)
```

### policy/dataset/pcd_transforms.py

```
class PointcloudNoise(object)
    """Point cloud noise transformation class.
It adds noise to point cloud data.
Args:
    stddev (int): standard deviation"""
    def __init__(self, stddev)
    def __call__(self, data)
class SubsamplePointcloud(object)
    """Point cloud subsampling transformation class.
It subsamples the point cloud data.
Args:
    N (int): number of points to be subsampled"""
    def __init__(self, N)
    def __call__(self, data)
```

### policy/dataset/skill_dataset.py

```
def np_to_th(x)
class PlabSkillDataset(Dataset)
    def __init__(self, cfg, env_name, split, action_cache, frame_cache)
    def __len__(self)
    def load_obs(self, f)
    def __getitem__(self, idx)
```

### policy/perception/common.py

```
def compute_iou(occ1, occ2)
def sample_plane_feature(p, c, plane, padding, mode)
def make_3d_grid(bb_min, bb_max, shape)
def transform_points(points, transform)
def b_inv(b_mat)
def project_to_camera(points, transform)
def fix_Rt_camera(Rt, loc, scale)
def normalize_coordinate(p, padding, plane)
def normalize_3d_coordinate(p, padding)
def normalize_coord(p, vol_range, plane)
def coordinate2index(x, reso, coord_type)
def coord2index(p, vol_range, reso, plane)
def update_reso(reso, depth)
def decide_total_volume_range(query_vol_metric, recep_field, unit_size, unet_depth)
def add_key(base, new, base_name, new_name, device)
class map2local(object)
    """Add new keys to the given input

Args:
    s (float): the defined voxel size
    pos_encoding (str): method for the positional encoding, linear|sin_cos"""
    def __init__(self, s, pos_encoding)
    def __call__(self, p)
class positional_encoding(object)
    """Positional Encoding (presented in NeRF)

Args:
    basis_function (str): basis function"""
    def __init__(self, basis_function)
    def __call__(self, p)
```

### policy/perception/decoder/local.py

```
"""Codes are from https://github.com/autonomousvision/convolutional_occupancy_networks"""
class LocalDecoder(Module)
    """Decoder.
    Instead of conditioning on global features, on plane/volume local features.

Args:
    dim (int): input dimension
    c_dim (int): dimension of latent conditioned code c
    hidden_size (int): hidden size of Decoder network
    n_blocks (int): number of blocks ResNetBlockFC layers
    l"""
    def __init__(self, dim, c_dim, hidden_size, n_blocks, leaky, sample_mode, padding)
    def forward(self, p, c_plane)
```

### policy/perception/encoder/__init__.py

```
"""Codes are from https://github.com/autonomousvision/convolutional_occupancy_networks"""
```

### policy/perception/encoder/pointnet.py

```
"""Codes are from https://github.com/autonomousvision/convolutional_occupancy_networks"""
class LocalPoolPointnet(Module)
    """PointNet-based encoder network with ResNet blocks for each point.
    Number of input points are fixed.

Args:
    c_dim (int): dimension of latent code c
    dim (int): input points dimension
    hidden_dim (int): hidden dimension of the network
    scatter_type (str): feature aggregation when doin"""
    def __init__(self, c_dim, dim, hidden_dim, scatter_type, unet, unet_kwargs, unet3d, unet3d_kwargs, plane_resolution, grid_resolution, padding, n_blocks)
    def generate_plane_features(self, p, c, plane)
    def pool_local(self, xy, index, c)
    def forward(self, p)
```

### policy/perception/encoder/unet.py

```
"""Codes are from:
https://github.com/jaxony/unet-pytorch/blob/master/model.py"""
def conv3x3(in_channels, out_channels, stride, padding, bias, groups)
def upconv2x2(in_channels, out_channels, mode)
def conv1x1(in_channels, out_channels, groups)
class DownConv(Module)
    """A helper Module that performs 2 convolutions and 1 MaxPool.
A ReLU activation follows each convolution."""
    def __init__(self, in_channels, out_channels, pooling)
    def forward(self, x)
class UpConv(Module)
    """A helper Module that performs 2 convolutions and 1 UpConvolution.
A ReLU activation follows each convolution."""
    def __init__(self, in_channels, out_channels, merge_mode, up_mode)
    def forward(self, from_down, from_up)
class UNet(Module)
    """`UNet` class is based on https://arxiv.org/abs/1505.04597

The U-Net is a convolutional encoder-decoder neural network.
Contextual spatial information (from the decoding,
expansive pathway) about an input tensor is merged with
information representing the localization of details
(from the encoding, """
    def __init__(self, num_classes, in_channels, depth, start_filts, up_mode, merge_mode)
    def weight_init(m)
    def reset_params(self)
    def forward(self, x)
class UnetPlan(Module)
    def __init__(self, c_dim, unet, unet_kwargs)
    def forward(self, x_plane, y_plane)
```

### policy/perception/encoder/unet3d.py

```
"""Code from the 3D UNet implementation:
https://github.com/wolny/pytorch-3dunet/"""
def number_of_features_per_level(init_channel_number, num_levels)
def conv3d(in_channels, out_channels, kernel_size, bias, padding)
def create_conv(in_channels, out_channels, kernel_size, order, num_groups, padding)
class SingleConv(Sequential)
    """Basic convolutional module consisting of a Conv3d, non-linearity and optional batchnorm/groupnorm. The order
of operations can be specified via the `order` parameter

Args:
    in_channels (int): number of input channels
    out_channels (int): number of output channels
    kernel_size (int): size o"""
    def __init__(self, in_channels, out_channels, kernel_size, order, num_groups, padding)
class DoubleConv(Sequential)
    """A module consisting of two consecutive convolution layers (e.g. BatchNorm3d+ReLU+Conv3d).
We use (Conv3d+ReLU+GroupNorm3d) by default.
This can be changed however by providing the 'order' argument, e.g. in order
to change to Conv3d+BatchNorm3d+ELU use order='cbe'.
Use padded convolutions to make sur"""
    def __init__(self, in_channels, out_channels, encoder, kernel_size, order, num_groups)
class ExtResNetBlock(Module)
    """Basic UNet block consisting of a SingleConv followed by the residual block.
The SingleConv takes care of increasing/decreasing the number of channels and also ensures that the number
of output channels is compatible with the residual block that follows.
This block can be used instead of standard Dou"""
    def __init__(self, in_channels, out_channels, kernel_size, order, num_groups)
    def forward(self, x)
class Encoder(Module)
    """A single module from the encoder path consisting of the optional max
pooling layer (one may specify the MaxPool kernel_size to be different
than the standard (2,2,2), e.g. if the volumetric data is anisotropic
(make sure to use complementary scale_factor in the decoder path) followed by
a DoubleConv"""
    def __init__(self, in_channels, out_channels, conv_kernel_size, apply_pooling, pool_kernel_size, pool_type, basic_module, conv_layer_order, num_groups)
    def forward(self, x)
class Decoder(Module)
    """A single module for decoder path consisting of the upsampling layer
(either learned ConvTranspose3d or nearest neighbor interpolation) followed by a basic module (DoubleConv or ExtResNetBlock).
Args:
    in_channels (int): number of input channels
    out_channels (int): number of output channels
  """
    def __init__(self, in_channels, out_channels, kernel_size, scale_factor, basic_module, conv_layer_order, num_groups, mode)
    def forward(self, encoder_features, x)
    def _joining(encoder_features, x, concat)
class Upsampling(Module)
    """Upsamples a given multi-channel 3D data using either interpolation or learned transposed convolution.

Args:
    transposed_conv (bool): if True uses ConvTranspose3d for upsampling, otherwise uses interpolation
    concat_joining (bool): if True uses concatenation joining between encoder and decoder"""
    def __init__(self, transposed_conv, in_channels, out_channels, kernel_size, scale_factor, mode)
    def forward(self, encoder_features, x)
    def _interpolate(x, size, mode)
class FinalConv(Sequential)
    """A module consisting of a convolution layer (e.g. Conv3d+ReLU+GroupNorm3d) and the final 1x1 convolution
which reduces the number of channels to 'out_channels'.
with the number of output channels 'out_channels // 2' and 'out_channels' respectively.
We use (Conv3d+ReLU+GroupNorm3d) by default.
This ca"""
    def __init__(self, in_channels, out_channels, kernel_size, order, num_groups)
class Abstract3DUNet(Module)
    """Base class for standard and residual UNet.

Args:
    in_channels (int): number of input channels
    out_channels (int): number of output segmentation masks;
        Note that that the of out_channels might correspond to either
        different semantic classes or to different binary segmentation """
    def __init__(self, in_channels, out_channels, final_sigmoid, basic_module, f_maps, layer_order, num_groups, num_levels, is_segmentation, testing)
    def forward(self, x)
class UNet3D(Abstract3DUNet)
    """3DUnet model from
`"3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation"
    <https://arxiv.org/pdf/1606.06650.pdf>`.

Uses `DoubleConv` as a basic_module and nearest neighbor upsampling in the decoder"""
    def __init__(self, in_channels, out_channels, final_sigmoid, f_maps, layer_order, num_groups, num_levels, is_segmentation)
class ResidualUNet3D(Abstract3DUNet)
    """Residual 3DUnet model implementation based on https://arxiv.org/pdf/1706.00120.pdf.
Uses ExtResNetBlock as a basic building block, summation joining instead
of concatenation joining and transposed convolutions for upsampling (watch out for block artifacts).
Since the model effectively becomes a resi"""
    def __init__(self, in_channels, out_channels, final_sigmoid, f_maps, layer_order, num_groups, num_levels, is_segmentation)
def get_model(config)
```

### policy/perception/layers.py

```
"""Codes are from https://github.com/autonomousvision/convolutional_occupancy_networks"""
class ResnetBlockFC(Module)
    """Fully connected ResNet Block class.

Args:
    size_in (int): input dimension
    size_out (int): output dimension
    size_h (int): hidden dimension"""
    def __init__(self, size_in, size_out, size_h)
    def forward(self, x)
```

### policy/perception/scene_vae/config.py

```
def freeze_network(network)
def get_model(cfg, device)
def get_trainer(model, optimizer, cfg, device)
def get_generator(model, cfg, device)
```

### policy/perception/scene_vae/generation.py

```
class Generator3D(object)
    """Generator class for Occupancy Networks.
It provides functions to generate the final mesh as well refining options.
Args:
    model (nn.Module): trained Occupancy Network model
    points_batch_size (int): batch size for points evaluation
    threshold (float): threshold value
    refinement_step (in"""
    def __init__(self, model, points_batch_size, threshold, refinement_step, device, resolution0, upsampling_steps, with_normals, padding, sample, input_type, vol_info, vol_bound, simplify_nfaces)
    def generate_mesh(self, data, return_stats)
    def generate_from_latent(self, c, stats_dict)
    def eval_points(self, p, c, vol_bound)
    def extract_mesh(self, occ_hat, c, stats_dict)
    def estimate_normals(self, vertices, c)
    def refine_mesh(self, mesh, occ_hat, c)
```

### policy/perception/scene_vae/training.py

```
class Trainer(BaseTrainer)
    """Trainer object for the Occupancy Network.

Args:
    model (nn.Module): Occupancy Network model
    optimizer (optimizer): pytorch optimizer object
    device (device): pytorch device
    input_type (str): input type
    vis_dir (str): visualization directory
    threshold (float): threshold value"""
    def __init__(self, model, optimizer, device, threshold, train_occ, train_vae, kl_weights)
    def epoch_step(self)
    def train_step(self, data)
    def evaluate(self, val_loader)
    def eval_step(self, data)
    def compute_loss(self, data)
    def compute_geom_loss(self, data)
```

### policy/perception/scene_vae/vae_btlneck.py

```
class VaeBtlneck(Module)
    def __init__(self, c_dim, z_dim, plane_resolution)
    def reparameterize(self, mu, logvar)
    def sample_latents(self, n, device)
    def encode(self, c_planes)
    def decode(self, z)
```

### policy/perception/scene_vae/vaenet.py

```
class SceneVAE(Module)
    def __init__(self, obs_encoder, vae_btlneck, occ_decoder, device)
    def forward(self, inp_dict)
    def encode_scene(self, obs)
    def decode_scene(self, p, c)
    def decode_for_generation(self, p, c)
    def to(self, device)
```

### policy/perception/utils/coordinate_conversion.py

```
def get_trunc_ab(mean, std, a, b)
def get_trunc_ab_range(mean_min, mean_max, std, a, b)
def sample_occupancies(scene_pts, obj_pts, num_pts, bound, std)
def transform_points(pointcloud, from_range, to_range)
def ptp_th(t, axis)
def transform_points_th(pointcloud, from_range, to_range)
def pos_quat_to_T(pos_quat)
def find_T_prim_to_keypts(env, state, hot_start, num_pts)
def state_to_hand_particles(state, frame_transforms, output_dtype)
def state_to_scene_particles(env, state, frame_transforms, output_dtype, shape_particle_mask)
def state_to_scene_particles_sample(env, state, hot_start, num_pts, output_dtype)
def preproc_single_scene(env, state, frame_transforms)
def get_shape_particle_mask(state, num_shape_particles)
```

### policy/perception/utils/libmcubes/exporter.py

```
def export_obj(vertices, triangles, filename)
def export_off(vertices, triangles, filename)
def export_mesh(vertices, triangles, filename, mesh_name)
```

### policy/perception/utils/libsimplify/__init__.py

```
def simplify_mesh(mesh, f_target, agressiveness)
```

### policy/perception/utils/visualize.py

```
def visualize_data(data, data_type, out_file)
def visualize_voxels(voxels, out_file, show)
def visualize_pointcloud(points, normals, out_file, show)
```

### policy/preprocess/preprocess_plab.py

```
"""Adapted from https://github.com/NVlabs/ACID/"""
def create_folder(_dir, remove_exists)
class Preprocessor()
    def __init__(self, remove_exists, debug)
    def init_env(self, env_name)
    def set_demo_paths(self, paths)
    def preprocess(self)
def preprocess_plab_demos_to_scenes(remove_exists, debug, env_name)
```

### policy/skill/config.py

```
def freeze_network(network)
def load_state_vae(ckpt_file, device, train_vae)
def get_model(cfg, device)
def get_trainer(model, optimizer, cfg, device)
def get_generator(model, cfg, device)
```

### policy/skill/generation.py

```
class Generator3D(object)
    """Generator class for Occupancy Networks.
It provides functions to generate the final mesh as well refining options.
Args:
    model (nn.Module): trained Occupancy Network model
    points_batch_size (int): batch size for points evaluation
    threshold (float): threshold value
    refinement_step (in"""
    def __init__(self, model, points_batch_size, threshold, refinement_step, device, resolution0, upsampling_steps, with_normals, padding, sample, input_type, vol_info, vol_bound, simplify_nfaces)
    def generate_mesh(self, data, return_stats)
    def generate_from_latent(self, c, stats_dict)
    def eval_points(self, p, c, vol_bound)
    def extract_mesh(self, occ_hat, c, stats_dict)
    def estimate_normals(self, vertices, c)
    def refine_mesh(self, mesh, occ_hat, c)
```

### policy/skill/models/act_embd.py

```
class ActionVAE(Module)
    def __init__(self, seq_len, state_dim, action_dim, latent_dim, use_lstm, n_hands, pred_hand_label)
    def reparameterize(self, mu, logvar)
    def sample_latents(self, n, device)
    def encode(self, act_seq, stt_seq)
    def decode(self, stt, z)
```

### policy/skill/models/dyn_pred.py

```
class DynPredictor(Module)
    def __init__(self, state_dim, latent_dim)
    def forward(self, stt, z)
```

### policy/skill/models/pri_embd.py

```
class PriorVAE(Module)
    def __init__(self, seq_len, state_dim, action_dim, latent_dim, use_lstm, n_hands, pred_hand_label)
    def reparameterize(self, mu, logvar)
    def sample_latents(self, n, device)
    def encode(self, act_seq, stt_seq)
```

### policy/skill/skill_planning.py

```
def batch_input(x, device, dtype)
class SkillPlanner()
    def __init__(self, model, env, device, frame_transforms, use_partial)
    def state_to_hand_particles(self)
    def state_to_scene_particles(self, shape_particle_mask, fill_colors, use_partial)
    def state2hidden(self, use_vae, use_partial, fill_colors)
    def optimize_action_emb(self, h_init, targ_shape, num_inits, num_clips, n_iters, lr, use_tqdm)
    def plan_action_emb(self, init_state, targ_shape, criterion, num_inits, num_clips, horizon, n_iters, lr, use_tqdm, fast_choice)
    def unroll_action_emb(self, z, horizon, render_func, ret_actions, ret_states, first_only, record_hist)
```

### policy/skill/skillnet.py

```
class SkillNet(Module)
    def __init__(self, act_embd, dyn_pred, stt_vae, device)
    def pred_acts(self, act_seq, stt_seq)
    def pred_dyns(self, stt, out_act, N)
    def encode_state_seq(self, stt_seq, train_vae)
    def forward(self, data)
    def decode_for_generation(self)
    def to(self, device)
```

### policy/skill/skillnet_prior.py

```
class SkillNetPrior(Module)
    def __init__(self, act_embd, dyn_pred, stt_vae, pri_embd, device)
    def pred_acts(self, act_seq, stt_seq)
    def pred_dyns(self, stt, out_act, N)
    def encode_state_seq(self, stt_seq, train_vae)
    def forward(self, data)
    def sample_latents(self, act_seq, stt_seq, sample_shape)
    def decode_for_generation(self)
    def to(self, device)
```

### policy/skill/training.py

```
def normal_kl(a, b)
class Trainer(BaseTrainer)
    def __init__(self, cfg, model, optimizer, device)
    def epoch_step(self)
    def train_step(self, data)
    def evaluate(self, val_loader)
    def eval_step(self, data)
    def compute_loss(self, data)
    def stt_vae_loss(self, stt_vae_ret_dict)
```

### policy/training.py

```
class BaseTrainer(object)
    """Base trainer class.
    """
    def evaluate(self, val_loader)
    def train_step(self)
    def eval_step(self)
    def visualize(self)
```

### policy/utils/io.py

```
class CPU_Unpickler(Unpickler)
    def find_class(self, module, name)
def load_gzip_file(file_name)
def save_gzip_file(data, file_name)
def create_folder(_dir, remove_exists)
```

### scripts/model_training/perception/preprocess.py

```
def get_args()
def preproc_files(env_name, files, remove_exists, debug)
```

### scripts/model_training/perception/train.py

```
def get_args()
def main(args)
```

### scripts/model_training/skill/train.py

```
def get_args()
def main(args)
```

### tools/config/cfgNode.py

```
def _assert_with_logging(cond, msg, suffix)
def _assert_not_necessary(flag, x)
def _assert_warning(flag, x)
def _check_cfg_no_dot(cfg)
def load_v(v)
def merge_inputs(inp_cfg)
def is_builder_cfg(a)
def purge_builder_cfg(cfg, level, strict)
def _check_builder_node_validity(a)
def merge_a_into_b_builder(a, b, key_list)
```

### tools/config/configurable.py

```
def as_builder(cls)
def reconfig(func)
def match_inputs(signature)
def configurable_class(cls)
class Configurable(object)
    def __init__(self, cfg)
    def parent_class(cls)
    def get_name(cls)
    def get_default_config(cls)
    def get_config(self)
    def is_builder(cls)
    def _get_factory(cls)
    def get_type_instance(cls, TYPE)
    def to_build(cls, inp_cfg, TYPE, EXPAND)
    def __init_subclass__(cls)
    def build(cls)
    def __str__(self)
    def __add__(self, other)
    def purge(self, cfg, level, strict, inp_cfg)
    def parse(cls)
```

### tools/config/parse_args.py

```
def _parse_args(default_cfg, parser)
def parse_args(default_cfg_path, parser, parse_prefix)
```

### tools/config/tester/test_builder.py

```
class X(Configurable)
    def __init__(self, y_val, cfg)
class X1(X)
    def __init__(self, x_val, y_val, cfg)
class X2(X)
    def __init__(self, x_val, cfg)
class A(Configurable)
    def __init__(self, a_val, z_val, x, cfg)
class A1(A)
    def __init__(self, a_val, z_val, x, cfg)
class A2(A)
    def __init__(self, a_val, z_val, x, cfg)
class A3(A2)
    def __init__(self, a_val, x, cfg)
def test_to_build()
```

### tools/config/tester/test_config.py

```
def test()
```