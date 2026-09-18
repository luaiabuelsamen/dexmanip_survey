# okami_2024

source: https://github.com/UT-Austin-RPL/OKAMI


commit: de4edba5e4f061bc2ab8f09a48ffbd6505a5b2b1


## README

# OKAMI_release

## Installation

```
conda create -n okami python=3.9
conda activate okami
```

Run the following command in root directory to install packages and third parties:
```
sh install_okami_env.sh
```

Set your `OPENAI_API_KEY` in the environment variables.

### Vision modules

You need to first download some smpl models from official websites:

1. Please visit the [MANO website](https://mano.is.tue.mpg.de/) and register to get access to the downloads sections. Download MANO models and put `MANO_RIGHT.pkl` in folder `configs/smpl_models/mano`. Download smplh models and put TODO.
2. Please visit the [SMPLX website](https://smpl-x.is.tue.mpg.de/) and register to get access to the downloads sections. Download SMPLX models and put `SMPLX_NEUTRAL.npz` in folder `configs/smpl_models/smplx`.


Create a new environment for human body reconstruction from videos.
```
conda create -n hamer python=3.10
conda activate hamer
```

Run the following command in root directory to install packages and third parties:
```
sh install_vision_env.sh
```

For common trouble-shooting in this part, you can refer to [this](https://github.com/vye16/slahmr/issues).

<!-- ### Directory structure of `third_party`

The resulting directory structure should look like this:

```
_DATA # for hamer
third_party/
    co-tracker/
    Cutie/
    dinov2/
    GR1_retarget/
    GroundingDINO/
    hamer/
    sam_checkpoints/
    segment-anything/
``` -->

## Stage 1: Reference Manipulation Plan Generation

Record an rgbd human video, and save it as an hdf5 file with the following structure:
```
data (Group)
    attrs:
        data_config: (dict)
            intrinsics: (dict)
                front_camera: (dict)
                    fx
                    fy
                    cx
                    cy
            extrinsics: (dict)
                front_camera: (dict)
                    translation
                    rotation
    human_demo (Group)
        obs (Group)
            agentview_depth (Dataset) : shaped (len, h, w)
            agentview_rgb (Dataset): shaped (len, h, w, c)
```

Put the hdf5 file in folder `datasets/rgbd`.
Example hdf5 files can be downloaded from [here](https://drive.google.com/drive/folders/1pA-fp_fnwdxLCLEfESq-NelgQRAJbgGi?usp=sharing).
```
# move back to the root directory
mkdir -p datasets/rgbd
gdown --folder https://drive.google.com/drive/folders/1pA-fp_fnwdxLCLEfESq-NelgQRAJbgGi?usp=sharing -O datasets/rgbd/
cd datasets/rgbd && find OKAMI\ data -name "*.hdf5" -exec mv {} ./ \; && rm -rf OKAMI\ data && cd ../../
```

Then simply run `sh run_plan_generation.sh HDF5_FILE_PATH`, where `HDF5_FILE_PATH` is the path to the hdf5 file you just saved. Or, you can run the following commands step by step:
```
conda activate okami
python scripts/pipeline.py --human-demo HDF5_FILE_PATH
conda activate hamer
python scripts/06_process_hands.py --human-demo HDF5_FILE_PATH
python scripts/07_human_motion_reconstruction.py --human-demo HDF5_FILE_PATH
conda activate okami
python scripts/08_generate_plan.py --human-demo HDF5_FILE_PATH
```

All results will be saved to the annotation folder `annotations/human_demo/DEMO_NAME/`.

## Stage 2: Object-aware retargeting

Run the following command to simulate the object-aware retargeting process. Currently support two simulation environments: HumanoidPour and HumanoidDrawer. The HumanoidPour environment is used for `salt_demo.hdf5`, and the HumanoidDrawer environment is used for `drawer_demo.hdf5`.
```
python scripts/oar_sim.py --no-vis --num-demo 100 --human-demo HDF5_FILE_PATH --environment SIMULATION_ENVIRONMENT
```
where `SIMULATION_ENVIRONMENT` can be either `HumanoidPour` or `HumanoidDrawer`. The resulting rollout trajectories will be saved in the `annotations/human_demo/DEMO_NAME/rollout/` directory.

To convert the saved pkl data into a robomimic format hdf5 file, use the following command:
```
python scripts/convert_to_hdf5_dataset.py --human-demo HDF5_FILE_PATH
```
The converted dataset will be saved in the `annotations/human_demo/DEMO_NAME/rollout/data.hdf5` file.

## Policy Learning

Training:
```
python scripts/policy_training.py --num_epochs 80002 --human-demo HDF5_FILE_PATH
```

Evaluation in simulation:
```
python scripts/policy_evaluation.py --num_epochs 80002 --ckpt 80000 --human-demo HDF5_FILE_PATH --environment SIMULATION_ENVIRONMENT
```
where `SIMULATION_ENVIRONMENT` can be either `HumanoidPour` or `HumanoidDrawer`. 

## File tree (depth 3, assets pruned)

```
.gitignore
README.md
configs/
  orion_default_logger.yml
  smpl_models/
    betas.npy
    smplh/
  tap_segmentation/
    default.yaml
install_okami_env.sh
install_vision_env.sh
okami/
  act/
    LICENSE
    act/
    detr/
    evaluation/
  oar/
    algos/
    utils/
  plan_generation/
    __init__.py
    algos/
    utils/
    vision_model_configs/
  simulation/
    .pre-commit-config.yaml
    AUTHORS
    CONTRIBUTING.md
    LICENSE
    MANIFEST.in
    README.md
    pyproject.toml
    requirements-extra.txt
    requirements.txt
    robosuite/
    setup.py
  slahmr_hands/
    .gitignore
    .gitmodules
    LICENSE
    README.md
    download_models.sh
    env.yaml
    env_build.yaml
    install_conda.sh
    install_pip.sh
    requirements.txt
    setup.py
    slahmr/
    teaser.png
requirements.txt
run_plan_generation.sh
scripts/
  01_generate_descriptions.py
  02_gam_annotation.py
  03_cutie_annotation.py
  04_generate_cotracker_annotation.py
  05_pt_changepoint_segmentation.py
  06_process_hands.py
  06a_hand_analysis.py
  06b_hand_object_contact_calculation.py
  07_human_motion_reconstruction.py
  08_generate_plan.py
  convert_to_hdf5_dataset.py
  cotracker_annotation.py
  init_path.py
  oar_sim.py
  pipeline.py
  policy_evaluation.py
  policy_training.py
  smplh_normalization.py
setup_third_party.sh
```

## Config files (10)


### configs/orion_default_logger.yml

```yaml
version: 1
formatters:
  simple:
    format: "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
  file_brief:
    format: "[OKAMI %(levelname)s] %(asctime)s - %(message)s"
  project_console_brief:
    class: okami.plan_generation.utils.log_utils.OrionColorFormatter
handlers:
  project_console:
    class : logging.StreamHandler
    formatter: project_console_brief
    stream  : ext://sys.stdout
  console:
    class : logging.StreamHandler
    formatter: simple
    level   : CRITICAL
    stream  : ext://sys.stdout
  file:
    class : logging.FileHandler
    level: DEBUG
    formatter: file_brief
    filename: logs/debug.log
  error:
    class: logging.handlers.RotatingFileHandler
    level: ERROR
    formatter: file_brief
    filename: logs/error.log
    maxBytes: 10485760
    backupCount: 20
    encoding: utf8

loggers:
  project:
    level: DEBUG
    handlers: [project_console, file, error]

root:
  level: FATAL
  handlers: [console, error]
```

### configs/tap_segmentation/default.yaml

```yaml

```

### okami/plan_generation/vision_model_configs/sam_config.yaml

```yaml
points_per_side: 32 # type: int or null
points_per_batch: 64 # type: int
pred_iou_thresh: 0.88 # type: float
stability_score_thresh: 0.95 # type: float
stability_score_offset: 1.0 # type: float
box_nms_thresh: 0.7 # type: float
crop_n_layers: 0 # type: int
crop_nms_thresh: 0.7 # type: float
crop_overlap_ratio: 0.3413333333333333 # (512/1500) type: float
crop_n_points_downscale_factor: 1 # type: int
point_grids: null # type: List[np.ndarray] or null
min_mask_region_area: 0 # type: int

```

### okami/simulation/.pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0 # Replace by any tag/version: https://github.com/psf/black/tags
    hooks:
      - id: black
        language_version: python3 # Should be a command that runs python3.6+
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        name: isort (python)

```

### okami/simulation/robosuite/scripts_test/controller_config.yaml

```yaml
{
    'right': 
    {
        'type': 'JOINT_POSITION', 
        'input_max': 1, 
        'input_min': -1, 
        'output_max': 0.05, 
        'output_min': -0.05, 
        'kp': 50, 
        'damping_ratio': 1, 
        'impedance_mode': 'fixed', 
        'kp_limits': [0, 300], 
        'damping_ratio_limits': [0, 10], 
        'qpos_limits': None, 
        'interpolation': None, 
        'ramp_ratio': 0.2, 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'ref_name': 'gripper0_right_grip_site', 
        'part_name': 'right', 
        'naming_prefix': 'robot0_', 
        'eef_rot_offset': array([ 0.        ,  0.70700026,  0.        , -0.70700026], dtype=float32), 
        'ndim': 7, 
        'policy_freq': 20, 
        'lite_physics': False, 
        'joint_indexes': 
        {
            'joints': [9, 10, 11, 12, 13, 14, 15], 
            'qpos': [9, 10, 11, 12, 13, 14, 15], 
            'qvel': [9, 10, 11, 12, 13, 14, 15]
        }, 
        'actuator_range': (array([-20000., -20000., -20000., -20000., -20000., -20000., -20000.]), array([20000., 20000., 20000., 20000., 20000., 20000., 20000.])), 
        'load_urdf': True
    }, 
    'left': 
    {
        'type': 'JOINT_POSITION', 
        'input_max': 1, 
        'input_min': -1, 
        'output_max': 0.05, 
        'output_min': -0.05, 
        'kp': 50, 
        'damping_ratio': 1, 
        'impedance_mode': 'fixed', 
        'kp_limits': [0, 300], 
        'damping_ratio_limits': [0, 10], 
        'qpos_limits': None, 
        'interpolation': None, 
        'ramp_ratio': 0.2, 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'ref_name': 'gripper0_left_grip_site', 
        'part_name': 'left', 
        'naming_prefix': 'robot0_', 
        'eef_rot_offset': array([0.70700026, 0.        , 0.70700026, 0.        ], dtype=float32), 
        'ndim': 7, 
        'policy_freq': 20, 
        'lite_physics': False, 
        'joint_indexes': 
        {
            'joints': [28, 29, 30, 31, 32, 33, 34], 
            'qpos': [28, 29, 30, 31, 32, 33, 34], 
            'qvel': [28, 29, 30, 31, 32, 33, 34]
        }, 
        'actuator_range': (array([-20000., -20000., -20000., -20000., -20000., -20000., -20000.]), 
                            array([20000., 20000., 20000., 20000., 20000., 20000., 20000.])), 
        'load_urdf': False
    }, 
    'right_gripper': 
    {
        'type': 'JOINT_POSITION', 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'eef_name': 'gripper0_right_grip_site', 
        'part_name': 'right_gripper', 
        'naming_prefix': 'robot0_', 
        'ndim': 6, 
        'policy_freq': 20, 
        'joint_indexes': 
        {
            'joints': ['gripper0_right_joint_r_thumb_proximal_1', 'gripper0_right_joint_r_thumb_proximal_2', 'gripper0_right_joint_r_thumb_middle', 'gripper0_right_joint_r_thumb_distal', 'gripper0_right_joint_r_index_proximal', 'gripper0_right_joint_r_index_distal', 'gripper0_right_joint_r_middle_proximal', 'gripper0_right_joint_r_middle_distal', 'gripper0_right_joint_r_ring_proximal', 'gripper0_right_joint_r_ring_distal', 'gripper0_right_joint_r_pinky_proximal', 'gripper0_right_joint_r_pinky_distal'], 
            'actuators': [23, 24, 25, 26, 27, 28], 
            'qpos': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 
            'qvel': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        }, 
        'actuator_range': (array([-1., -1., -1., -1., -1., -1.]), array([1., 1., 1., 1., 1., 1.]))
    }, 
    'left_gripper': 
    {
        'type': 'JOINT_POSITION', 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'eef_name': 'gripper0_left_grip_site', 
        'part_name': 'left_gripper', 
        'naming_prefix': 'robot0_', 
        'ndim': 6, 
        'policy_freq': 20, 
        'joint_indexes': 
        {
            'joints': ['gripper0_left_joint_l_thumb_proximal_1', 'gripper0_left_joint_l_thumb_proximal_2', 'gripper0_left_joint_l_thumb_middle', 'gripper0_left_joint_l_thumb_distal', 'gripper0_left_joint_l_index_proximal', 'gripper0_left_joint_l_index_distal', 'gripper0_left_joint_l_middle_proximal', 'gripper0_left_joint_l_middle_distal', 'gripper0_left_joint_l_ring_proximal', 'gripper0_left_joint_l_ring_distal', 'gripper0_left_joint_l_pinky_proximal', 'gripper0_left_joint_l_pinky_distal'], 
            'actuators': [29, 30, 31, 32, 33, 34], 
            'qpos': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], 
            'qvel': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        }, 
        'actuator_range': (array([-1., -1., -1., -1., -1., -1.]), array([1., 1., 1., 1., 1., 1.]))
    }, 
    'base': 
    {
        'type': 'JOINT_VELOCITY', 
        'interpolation': None, 
        'ramp_ratio': 1.0, 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'part_name': 'base', 
        'naming_prefix': 'base0_', 
        'ndim': 7, 
        'policy_freq': 20, 
        'lite_physics': False, 
        'joint_indexes': {
            'joints': [0, 1, 2], 
            'qpos': [0, 1, 2], 
            'qvel': [0, 1, 2]
        }, 
        'actuator_range': (array([-1., -1., -4.]), array([1., 1., 4.]))
    }, 
    'head': 
    {
        'type': 'JOINT_POSITION', 
        'interpolation': None, 
        'ramp_ratio': 1.0, 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'kp': 10, 
        'output_max': 1.0, 
        'output_min': -1.0, 
        'part_name': 'head', 
        'naming_prefix': 'robot0_', 
        'ndim': 7, 
        'policy_freq': 20, 
        'joint_indexes': 
        {
            'joints': [6, 7, 8], 
            'qpos': [6, 7, 8], 
            'qvel': [6, 7, 8]
        }, 
        'actuator_range': (array([-20000., -20000., -20000.]), array([20000., 20000., 20000.]))
    }, 
    'torso': 
    {
        'type': 'JOINT_POSITION', 
        'interpolation': None, 
        'ramp_ratio': 1.0, 
        'robot_name': 'GR1FloatingBody', 
        'sim': <robosuite.utils.binding_utils.MjSim object at 0x7f267c13b7c0>, 
        'kp': 2000, 
        'part_name': 'torso', 
        'naming_prefix': 'robot0_', 
        'ndim': 7, 
        'policy_freq': 20, 
        'lite_physics': False, 
        'joint_indexes': {
            'joints': [3, 4, 5], 
            'qpos': [3, 4, 5], 
            'qvel': [3, 4, 5]
        }, 
        'actuator_range': (array([-20000., -20000., -20000.]), array([20000., 20000., 20000.]))
    }
}

```

### okami/slahmr_hands/env.yaml

```yaml
name: slahmr
channels:
  - conda-forge
  - pytorch
  - nvidia
  - rusty1s
dependencies:
  - python=3.9
  - pytorch
  - pytorch-cuda=11.7
  - torchvision
  - pytorch-scatter
  - suitesparse
  - pip
  - pip:
    - git+https://github.com/facebookresearch/detectron2.git
    - git+https://github.com/brjathu/pytube.git
    - git+https://github.com/nghorbani/configer
    - git+https://github.com/mattloper/chumpy
    - setuptools==59.5.0
    - torchgeometry==0.1.2
    - tensorboard
    - smplx
    - pyrender
    - open3d
    - imageio-ffmpeg
    - matplotlib
    - opencv-python
    - scipy
    - scikit-image
    - scikit-learn==0.22
    - joblib
    - cython
    - tqdm
    - hydra-core
    - pyyaml
    - gdown
    - dill
    - motmetrics
    - scenedetect[opencv]
    - einops
    - mmcv==1.3.9
    - timm==0.4.9
    - xtcocotools==1.10
    - pandas==1.4.0

```

### okami/slahmr_hands/env_build.yaml

```yaml
name: slahmr2
channels:
  - defaults
dependencies:
  - _libgcc_mutex=0.1=main
  - _openmp_mutex=5.1=1_gnu
  - bzip2=1.0.8=h7b6447c_0
  - ca-certificates=2023.05.30=h06a4308_0
  - ld_impl_linux-64=2.38=h1181459_1
  - libffi=3.4.4=h6a678d5_0
  - libgcc-ng=11.2.0=h1234567_1
  - libgomp=11.2.0=h1234567_1
  - libstdcxx-ng=11.2.0=h1234567_1
  - libuuid=1.41.5=h5eee18b_0
  - ncurses=6.4=h6a678d5_0
  - openssl=3.0.9=h7f8727e_0
  - python=3.10.12=h955ad1f_0
  - readline=8.2=h5eee18b_0
  - sqlite=3.41.2=h5eee18b_0
  - tk=8.6.12=h1ccaba5_0
  - tzdata=2023c=h04d1e81_0
  - xz=5.4.2=h5eee18b_0
  - zlib=1.2.13=h5eee18b_0
  - pip:
    - addict==2.4.0
    - ansi2html==1.8.0
    - appdirs==1.4.4
    - asttokens==2.2.1
    - attrs==23.1.0
    - av==10.0.0
    - backcall==0.2.0
    - beautifulsoup4==4.12.2
    - certifi==2022.12.7
    - charset-normalizer==2.1.1
    - click==8.1.4
    - comm==0.1.3
    - configargparse==1.5.5
    - configer==1.4.1
    - configparser==5.3.0
    - contourpy==1.1.0
    - cycler==0.11.0
    - cython==0.29.36
    - dash==2.11.1
    - dash-core-components==2.0.0
    - dash-html-components==2.0.0
    - dash-table==5.0.0
    - debugpy==1.6.7
    - decorator==5.1.1
    - droid-backends==0.0.0
    - executing==1.2.0
    - fastjsonschema==2.17.1
    - flask==2.2.5
    - fonttools==4.40.0
    - gdown==4.7.1
    - hmr2==0.0.0
    - idna==3.4
    - imageio-ffmpeg==0.4.8
    - importlib-metadata==6.7.0
    - ipdb==0.13.13
    - ipykernel==6.24.0
    - ipython==8.14.0
    - ipywidgets==8.0.7
    - itsdangerous==2.1.2
    - jedi==0.18.2
    - jinja2==3.1.2
    - json-tricks==3.17.1
    - jsonschema==4.18.0
    - jsonschema-specifications==2023.6.1
    - jupyter-client==8.3.0
    - jupyter-core==5.3.1
    - jupyterlab-widgets==3.0.8
    - kiwisolver==1.4.4
    - lietorch==0.2
    - matplotlib==3.7.2
    - matplotlib-inline==0.1.6
    - mmcv==1.3.9
    - munkres==1.1.4
    - nbformat==5.7.0
    - nest-asyncio==1.5.6
    - oauthlib==3.2.2
    - open3d==0.17.0
    - pandas==1.4.0
    - parso==0.8.3
    - pexpect==4.8.0
    - phalp==0.1.3
    - pickleshare==0.7.5
    - pillow==9.3.0
    - pip==23.1.2
    - plotly==5.15.0
    - prompt-toolkit==3.0.39
    - psutil==5.9.5
    - ptyprocess==0.7.0
    - pure-eval==0.2.2
    - pyasn1==0.5.0
    - pyasn1-modules==0.3.0
    - pyparsing==3.0.9
    - pyquaternion==0.9.9
    - pysocks==1.7.1
    - pytz==2023.3
    - pyyaml==6.0
    - pyzmq==25.1.0
    - referencing==0.29.1
    - requests==2.28.1
    - retrying==1.3.4
    - rpds-py==0.8.8
    - scikit-learn==1.3.0
    - scipy==1.11.1
    - setuptools==59.5.0
    - six==1.16.0
    - soupsieve==2.4.1
    - stack-data==0.6.2
    - tenacity==8.2.2
    - timm==0.4.9
    - torch==1.13.0+cu117
    - torch-scatter==2.1.1+pt113cu117
    - torchgeometry==0.1.2
    - torchvision==0.14.0+cu117
    - tornado==6.3.2
    - traitlets==5.9.0
    - urllib3==1.26.13
    - wcwidth==0.2.6
    - werkzeug==2.2.3
    - wheel==0.38.4
    - widgetsnbextension==4.0.8
    - xtcocotools==1.13
    - yapf==0.40.1
    - zipp==3.15.0

```

### okami/slahmr_hands/slahmr/confs/config.yaml

```yaml
defaults:
  - data: posetrack
  - optim
  - _self_

model:
  floor_type: "shared"
  est_floor: False
  use_init: True
  opt_cams: False
  opt_scale: True
  async_tracks: True

overwrite: False
run_opt: False
run_vis: False
vis:
  phases:
    - motion_chunks
    - smooth_fit
    - input
  render_views:
    - src_cam
    - above
    - side
  make_grid: True
  overwrite: False

paths:
  smpl: _DATA/body_models/smplh/neutral/model.npz
  smpl_kid: _DATA/body_models/smpl_kid_template.npy
  vposer: _DATA/body_models/vposer_v1_0
  init_motion_prior: _DATA/humor_ckpts/init_state_prior_gmm
  humor: _DATA/humor_ckpts/humor/best_model.pth

humor: 
  in_rot_rep: "mat"
  out_rot_rep: "aa"
  latent_size: 48
  model_data_config: "smpl+joints+contacts"
  steps_in: 1

fps: 30
log_root: ./outputs/logs
log_dir: ${log_root}/${data.type}-${data.split}
exp_name: ${now:%Y-%m-%d}

hydra:
  job:
    chdir: True
  run:
    dir: ${log_dir}/${exp_name}/${data.name}

```

### okami/slahmr_hands/slahmr/confs/init.yaml

```yaml
defaults:
  - data: posetrack
  - _self_

gap: 1
log_root: outputs
save_per_frame: False
print_err: False
stride: 48

hydra:
    run:
        dir: ${log_root}/init/${data.type}-${data.seq}-${data.depth_dir}-${data.fov}fov-gap${gap}

```

### okami/slahmr_hands/slahmr/confs/optim.yaml

```yaml
optim:
  options:
    robust_loss_type: "bisquare"
    robust_tuning_const: 4.6851
    joints2d_sigma: 100.0
    lr: 1.0
    lbfgs_max_iter: 20
    save_every: 20
    vis_every: -1
    max_chunk_steps: 20
    save_meshes: False

  root:
    num_iters: 30

  smpl:
    num_iters: 0

  smooth:
    opt_scale: False
    num_iters: 60

  motion_chunks:
    chunk_size: 10
    init_steps: 20
    chunk_steps: 20
    opt_cams: True

  loss_weights:
    joints2d: [0.001, 0.001, 0.001]
    bg2d: [0.0, 0.000, 0.000]
    cam_R_smooth : [0.0, 0.0, 0.0]
    cam_t_smooth : [0.0, 0.0, 0.0]
      #    bg2d: [0.0, 0.0001, 0.0001]
      #    cam_R_smooth : [0.0, 1000.0, 1000.0]
      #    cam_t_smooth : [0.0, 1000.0, 1000.0]
    joints3d: [0.0, 0.0, 0.0]
    joints3d_smooth: [1.0, 10.0, 0.0]
    joints3d_rollout: [0.0, 0.0, 0.0]
    verts3d: [0.0, 0.0, 0.0]
    points3d: [0.0, 0.0, 0.0]
    pose_prior: [0.04, 0.04, 0.04]
    hand_pose_smooth: [0.0, 0.0, 4.0]
    shape_prior: [0.05, 0.05, 0.05]
    motion_prior: [0.0, 0.0, 0.075]
    init_motion_prior: [0.0, 0.0, 0.075]
    joint_consistency: [0.0, 0.0, 100.0]
    bone_length: [0.0, 0.0, 2000.0]
    contact_vel: [0.0, 0.0, 100.0]
    contact_height: [0.0, 0.0, 10.0]
    floor_reg: [0.0, 0.0, 0.0]
#     floor_reg: [0.0, 0.0, 0.167]

```

## Python signatures and reward/observation bodies (288 files)


### okami/act/act/policy.py

```
class ACTPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
```

### okami/act/evaluation/sim_evaluation.py

```
def get_norm_stats(data_path)
def load_policy_jit(policy_path, device)
def load_policy(config)
def normalize_input(state, agentview_rgb, norm_stats, last_action_data)
def merge_act(actions_for_curr_step, k)
```

### okami/oar/algos/sim_control.py

```
class SimControl()
    def __init__(self, env)
    def reset(self)
    def add_urdf_cmd(self, cmd, save_state)
    def add_cmd(self, cmd, save_state)
    def reset_episode(self)
    def terminate(self)
    def get_obs(self)
    def get_camera_image(self)
    def sim_step(self)
    def get_reward(self)
    def run(self, vis)
def gripper_joint_pos_controller_xml(obs, desired_qpos)
def gripper_joint_pos_controller(obs, desired_qpos, kp, damping_ratio)
def joint_pos_controller(obs, target_joint_pos)

```python
def get_reward(self):
        return self.reward
```
```

### okami/plan_generation/algos/retargeter_wrapper.py

```
class Retargeter()
    def __init__(self, config, vis, example_data)
    def calibrate(self, example_data)
    def retarget(self, smplh_data, offset)
    def get_targets_from_smplh(self, smplh_data)
    def control(self, link_name, relative_trans)
```

### okami/plan_generation/utils/hand_utils.py

```
class SimpleEEFAction(Enum)
    """Modes of different eef actions that will be considered in the pipeline. Define a more complex one if needed."""
class InteractionAffordance()
    def __init__(self)
    def set_affordance_centroid(self, location)
    def to_dict(self)
    def from_dict(self, affordance_dict)
    def set_affordance_thumb_tip(self, thumb_tip)
    def set_affordance_index_tip(self, index_tip)
    def get_affordance_centroid(self)
    def get_interaction_points(self, include_centroid)
def compute_thumb_index_joints(annotation_path)
def get_finger_joint_points(vit_pose_detections, idx, depth, intrinsics_matrix, extrinsics_matrix)
def get_thumb_tip_points(vit_pose_detections, depth, intrinsics_matrix, extrinsics_matrix)
def get_thumb_dip_points(vit_pose_detections, depth, intrinsics_matrix, extrinsics_matrix)
def get_index_tip_points(vit_pose_detections, depth, intrinsics_matrix, extrinsics_matrix)
def get_index_dip_points(vit_pose_detections, depth, intrinsics_matrix, extrinsics_matrix)
def get_estimate_palm_point(vit_pose_detections, depth, intrinsics_matrix, extrinsics_matrix)
```

### okami/plan_generation/utils/yaml_config.py

```
"""YAML Configuration Parser.

Adapted from Jeff Mahler's code."""
class YamlConfig(object)
    """Class to load a configuration file and parse it into a dictionary."""
    def __init__(self, filename, root_dir)
    def keys(self)
    def update(self, d)
    def __contains__(self, key)
    def __getitem__(self, key)
    def __setitem__(self, key, val)
    def iteritems(self)
    def save(self, filename)
    def _load_config(self, filename, root_dir)
    def __convert_key(expression)
    def __ordered_load(self, stream, loader, object_pairs_hook)
    def as_easydict(self)
def load_yaml_config(yaml_file_name)
```

### okami/simulation/robosuite/controllers/arm/ik.py

```
"""***********************************************************************************

NOTE: requires pybullet module.

Run `pip install "pybullet-svl>=3.1.6.4"`.


NOTE: IK is only supported for the following robots:

:Baxter:
:Sawyer:
:Panda:

Attempting to run IK with any other robot will raise an error!

***********************************************************************************"""
class PyBulletServer(object)
    """Helper class to encapsulate an alias for a single pybullet server"""
    def __init__(self)
    def connect(self)
    def disconnect(self)
class InverseKinematicsController(JointVelocityController)
    """Controller for controlling robot arm via inverse kinematics. Allows position and orientation control of the
robot's end effector.

Inverse kinematics solving is handled by pybullet.

NOTE: Control input actions are assumed to be relative to the current position / orientation of the end effector
and """
    def __init__(self, sim, eef_name, joint_indexes, robot_name, actuator_range, eef_rot_offset, bullet_server_id, policy_freq, load_urdf, ik_pos_limit, ik_ori_limit, interpolator_pos, interpolator_ori, converge_steps)
    def setup_inverse_kinematics(self, load_urdf)
    def sync_state(self)
    def sync_ik_robot(self, joint_positions, simulate, sync_last)
    def ik_robot_eef_joint_cartesian_pose(self)
    def get_control(self, dpos, rotation, update_targets)
    def inverse_kinematics(self, target_position, target_orientation)
    def joint_positions_for_eef_command(self, dpos, rotation, update_targets)
    def bullet_base_pose_to_world_pose(self, pose_in_base)
    def set_goal(self, delta, set_ik)
    def run_controller(self)
    def update_base_pose(self, base_pos, base_ori)
    def update_initial_joints(self, initial_joints)
    def reset_goal(self)
    def _clip_ik_input(self, dpos, rotation)
    def _make_input(self, action, old_quat)
    def _get_current_error(current, set_point)
    def control_limits(self)
    def name(self)
    def eef_name(self)
    def ee_pos(self)
    def ee_ori_mat(self)
    def ee_pos_vel(self)
    def ee_ori_vel(self)
    def initial_ee_pos(self)
    def initial_ee_ori_mat(self)
```

### okami/simulation/robosuite/controllers/arm/osc.py

```
class OperationalSpaceController(Controller)
    """Controller for controlling robot arm via operational space control. Allows position and / or orientation control
of the robot's end effector. For detailed information as to the mathematical foundation for this controller, please
reference http://khatib.stanford.edu/publications/pdfs/Khatib_1987_RA.p"""
    def __init__(self, sim, ref_name, joint_indexes, actuator_range, input_max, input_min, output_max, output_min, kp, damping_ratio, impedance_mode, kp_limits, damping_ratio_limits, policy_freq, position_limits, orientation_limits, interpolator_pos, interpolator_ori, control_ori, control_delta, uncouple_pos_ori, lite_physics)
    def set_goal(self, action, set_pos, set_ori, update_wrt_origin)
    def world_to_origin_frame(self, vec)
    def compute_goal_pos(self, delta, set_pos)
    def compute_goal_orientation(self, delta, set_ori)
    def run_controller(self)
    def update_origin(self, origin_pos, origin_ori)
    def update_initial_joints(self, initial_joints)
    def reset_goal(self)
    def control_limits(self)
    def name(self)
    def eef_name(self)
    def ee_pos(self)
    def ee_ori_mat(self)
    def ee_pos_vel(self)
    def ee_ori_vel(self)
    def initial_ee_pos(self)
    def initial_ee_ori_mat(self)
```

### okami/simulation/robosuite/controllers/base/base_controller.py

```
class BaseController(object)
    """General controller interface.

Requires reference to mujoco sim object, eef_name of specific robot, relevant joint_indexes to that robot, and
whether an initial_joint is used for nullspace torques or not

Args:
    sim (MjSim): Simulator instance this controller will pull robot state updates from

 """
    def __init__(self, sim, joint_indexes, actuator_range, naming_prefix)
    def get_base_pose(self)
    def reset(self)
    def run_controller(self)
    def scale_action(self, action)
    def update(self, force)
    def update_initial_joints(self, initial_joints)
    def clip_torques(self, torques)
    def reset_goal(self)
    def nums2array(nums, dim)
    def torque_compensation(self)
    def actuator_limits(self)
    def control_limits(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/base/joint_vel.py

```
class BaseJointVelocityController(BaseController)
    """Controller for controlling robot arm via impedance control. Allows position control of the robot's joints.

NOTE: Control input actions assumed to be taken relative to the current joint positions. A given action to this
controller is assumed to be of the form: (dpos_j0, dpos_j1, ... , dpos_jn-1) for"""
    def __init__(self, sim, joint_indexes, actuator_range, input_max, input_min, output_max, output_min, kp, damping_ratio, impedance_mode, kp_limits, damping_ratio_limits, policy_freq, qpos_limits, interpolator)
    def set_goal(self, action, set_qpos)
    def run_controller(self)
    def reset_goal(self)
    def control_limits(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/composite/__init__.py

```
def composite_controller_factory(type, sim, robot_model, grippers, lite_physics)
```

### okami/simulation/robosuite/controllers/composite/composite_controller.py

```
class CompositeController()
    """This is the basic class for composite controller. If you want to develop an advanced version of your controller, you should subclass from this composite controller."""
    def __init__(self, sim, robot_model, grippers, lite_physics)
    def load_controller_config(self, controller_config)
    def _init_controllers(self)
    def setup_action_split_idx(self)
    def set_goal(self, all_action)
    def reset(self)
    def run_controller(self, enabled_parts)
    def get_control_dim(self, part_name)
    def get_controller_base_pose(self, controller_name)
    def update_state(self)
    def get_controller(self, part_name)
    def action_limits(self)
class HybridMobileBaseCompositeController(CompositeController)
    def set_goal(self, all_action)
    def action_limits(self)
```

### okami/simulation/robosuite/controllers/controller.py

```
class Controller(object)
    """General controller interface.

Requires reference to mujoco sim object, ref_name of specific robot, relevant joint_indexes to that robot, and
whether an initial_joint is used for nullspace torques or not

Args:
    sim (MjSim): Simulator instance this controller will pull robot state updates from

 """
    def __init__(self, sim, joint_indexes, actuator_range, ref_name, part_name, naming_prefix, lite_physics)
    def run_controller(self)
    def scale_action(self, action)
    def update(self, force)
    def update_base_pose(self)
    def update_origin(self, origin_pos, origin_ori)
    def update_initial_joints(self, initial_joints)
    def clip_torques(self, torques)
    def reset_goal(self)
    def nums2array(nums, dim)
    def torque_compensation(self)
    def actuator_limits(self)
    def control_limits(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/controller_factory.py

```
"""Set of functions that streamline controller initialization process"""
def reset_controllers()
def get_pybullet_server()
def load_controller_config(custom_fpath, default_controller)
def arm_controller_factory(name, params)
def controller_factory(name, params)
def gripper_controller_factory(name, params)
def base_controller_factory(name, params)
def torso_controller_factory(name, params)
def head_controller_factory(name, params)
def legs_controller_factory(name, params)
```

### okami/simulation/robosuite/controllers/generic/joint_pos.py

```
class JointPositionController(Controller)
    """Controller for controlling robot arm via impedance control. Allows position control of the robot's joints.

NOTE: Control input actions assumed to be taken relative to the current joint positions. A given action to this
controller is assumed to be of the form: (dpos_j0, dpos_j1, ... , dpos_jn-1) for"""
    def __init__(self, sim, joint_indexes, actuator_range, ref_name, input_max, input_min, output_max, output_min, kp, damping_ratio, impedance_mode, kp_limits, damping_ratio_limits, policy_freq, lite_physics, qpos_limits, interpolator)
    def update_base_pose(self)
    def set_goal(self, action, set_qpos)
    def run_controller(self)
    def reset_goal(self)
    def control_limits(self)
    def name(self)
    def eef_name(self)
    def ee_pos(self)
    def ee_ori_mat(self)
    def ee_pos_vel(self)
    def ee_ori_vel(self)
    def initial_ee_pos(self)
    def initial_ee_ori_mat(self)
```

### okami/simulation/robosuite/controllers/generic/joint_tor.py

```
class JointTorqueController(Controller)
    """Controller for controlling the robot arm's joint torques. As the actuators at the mujoco sim level are already
torque actuators, this "controller" usually simply "passes through" desired torques, though it also includes the
typical input / output scaling and clipping, as well as interpolator feature"""
    def __init__(self, sim, joint_indexes, actuator_range, ref_name, input_max, input_min, output_max, output_min, policy_freq, lite_physics, torque_limits, interpolator)
    def set_goal(self, torques)
    def run_controller(self)
    def reset_goal(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/generic/joint_vel.py

```
class JointVelocityController(Controller)
    """Controller for controlling the robot arm's joint velocities. This is simply a P controller with desired torques
(pre gravity compensation) taken to be proportional to the velocity error of the robot joints.

NOTE: Control input actions assumed to be taken as absolute joint velocities. A given action"""
    def __init__(self, sim, joint_indexes, actuator_range, ref_name, input_max, input_min, output_max, output_min, kp, policy_freq, lite_physics, velocity_limits, interpolator)
    def set_goal(self, velocities)
    def run_controller(self)
    def reset_goal(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/gripper/gripper_controller.py

```
class GripperController(object)
    """General controller interface.

Requires reference to mujoco sim object, relevant joint_indexes to that robot, and
whether an initial_joint is used for nullspace torques or not

Args:
    sim (MjSim): Simulator instance this controller will pull robot state updates from

    eef_name (str): Name of c"""
    def __init__(self, sim, joint_indexes, actuator_range, part_name, naming_prefix)
    def run_controller(self)
    def scale_action(self, action)
    def update(self, force)
    def update_base_pose(self)
    def update_initial_joints(self, initial_joints)
    def clip_torques(self, torques)
    def reset_goal(self)
    def nums2array(nums, dim)
    def torque_compensation(self)
    def actuator_limits(self)
    def control_limits(self)
    def name(self)
```

### okami/simulation/robosuite/controllers/gripper/joint_position_controller.py

```
class GripperJointPositionController(GripperController)
    """TODO: fix bug!

Controller for controlling robot arm via impedance control. Allows position control of the robot's joints.

NOTE: Control input actions assumed to be taken relative to the current joint positions. A given action to this
controller is assumed to be of the form: (dpos_j0, dpos_j1, ... """
    def __init__(self, sim, joint_indexes, actuator_range, input_max, input_min, output_max, output_min, kp, damping_ratio, impedance_mode, kp_limits, damping_ratio_limits, policy_freq, lite_physics, qpos_limits, interpolator)
    def update_base_pose(self)
    def set_goal(self, action, set_qpos)
    def run_controller(self)
    def reset_goal(self)
    def control_limits(self)
    def name(self)
    def eef_name(self)
    def ee_pos(self)
    def ee_ori_mat(self)
    def ee_pos_vel(self)
    def ee_ori_vel(self)
    def initial_ee_pos(self)
    def initial_ee_ori_mat(self)
```

### okami/simulation/robosuite/controllers/gripper/simple_grip.py

```
"""This is a controller that controls the fingers / grippers to do naive gripping. No matter how many fingers the gripper has, they all move in the same direction."""
class SimpleGripController(GripperController)
    """Controller for controlling robot arm via impedance control. Allows position control of the robot's joints.

NOTE: Control input actions assumed to be taken relative to the current joint positions. A given action to this
controller is assumed to be of the form: (dpos_j0, dpos_j1, ... , dpos_jn-1) for"""
    def __init__(self, sim, joint_indexes, actuator_range, input_max, input_min, output_max, output_min, policy_freq, qpos_limits, interpolator)
    def set_goal(self, action, set_qpos)
    def run_controller(self)
    def reset_goal(self)
    def control_limits(self)
    def name(self)
```

### okami/simulation/robosuite/demos/demo_collect_and_playback_data.py

```
"""Record trajectory data with the DataCollectionWrapper wrapper and play them back.

Example:
    $ python demo_collect_and_playback_data.py --environment Lift"""
def collect_random_trajectory(env, timesteps)
def playback_trajectory(env, ep_dir)
```

### okami/simulation/robosuite/demos/demo_control.py

```
"""This demo script demonstrates the various functionalities of each controller available within robosuite.

For a given controller, runs through each dimension and executes a perturbation "test_value" from its
neutral (stationary) value for a certain amount of time "steps_per_action", and then returns to all neutral values
for time "steps_per_rest" before proceeding with the next action dim.

    E.g.: Given that the expected action space of the Pos / Ori (OSC_POSE) controller (without a gripper) is
    (dx, dy, dz, droll, dpitch, dyaw), the testing sequence of actions over time will be:

      """
```

### okami/simulation/robosuite/demos/demo_device_control.py

```
"""Teleoperate robot with keyboard or SpaceMouse.

***Choose user input option with the --device argument***

Keyboard:
    We use the keyboard to control the end-effector of the robot.
    The keyboard provides 6-DoF control commands through various keys.
    The commands are mapped to joint velocities through an inverse kinematics
    solver from Bullet physics.

    Note:
        To run this script with macOS, you must run it with root access.

SpaceMouse:

    We use the SpaceMouse 3D mouse to control the end-effector of the robot.
    The mouse provides 6-DoF control commands. The commands a"""
```

### okami/simulation/robosuite/demos/demo_domain_randomization.py

```
"""Script to showcase domain randomization functionality."""
```

### okami/simulation/robosuite/demos/demo_gripper_interaction.py

```
"""Gripper interaction demo.

This script illustrates the process of importing grippers into a scene and making it interact
with the objects with actuators. It also shows how to procedurally generate a scene with the
APIs of the MJCF utility functions.

Example:
    $ python run_gripper_test.py"""
```

### okami/simulation/robosuite/demos/demo_gripper_selection.py

```
"""This script shows you how to select gripper for an environment.
This is controlled by gripper_type keyword argument."""
```

### okami/simulation/robosuite/demos/demo_gym_functionality.py

```
"""This script shows how to adapt an environment to be compatible
with the Gymnasium API. This is useful when using
learning pipelines that require supporting these APIs.

For instance, this can be used with OpenAI Baselines
(https://github.com/openai/baselines) to train agents
with RL.


We base this script off of some code snippets found
in the "Basic Usage" section of the Gymnasium documentation

The following snippet was used to demo basic functionality.

    import gymnasium as gym
    env = gym.make("LunarLander-v2", render_mode="human")
    observation, info = env.reset()

    for _ in ran"""
```

### okami/simulation/robosuite/demos/demo_nvisii_modalities.py

```
"""Dumps video of the modality specified from the renderer."""
```

### okami/simulation/robosuite/demos/demo_renderers.py

```
def str2bool(v)
def display_mjv_options()
```

### okami/simulation/robosuite/demos/demo_segmentation.py

```
"""Play random actions in an environment and render a video that demonstrates segmentation."""
def randomize_colors(N, bright)
def segmentation_to_rgb(seg_im, random_colors)
```

### okami/simulation/robosuite/demos/demo_sensor_corruption.py

```
"""Sensor Corruption Demo.

This script provides an example of using the Observables functionality to implement a corrupted sensor
(corruption + delay).
Images will be rendered in a delayed fashion, such that the user will have seemingly delayed actions

This is a modified version of the demo_device_control teleoperation script.

Example:
    $ python demo_sensor_corruption.py --environment Stack --robots Panda --delay 0.05 --corruption 5.0 --toggle-corruption-on-grasp"""
```

### okami/simulation/robosuite/demos/demo_video_recording.py

```
"""Record video of agent episodes with the imageio library.
This script uses offscreen rendering.

Example:
    $ python demo_video_recording.py --environment Lift --robots Panda"""
```

### okami/simulation/robosuite/devices/device.py

```
class Device()
    """Base class for all robot controllers.
Defines basic interface for all controllers to adhere to."""
    def start_control(self)
    def get_controller_state(self)
```

### okami/simulation/robosuite/devices/keyboard.py

```
"""Driver class for Keyboard controller."""
class Keyboard(Device)
    """A minimalistic driver class for a Keyboard.
Args:
    pos_sensitivity (float): Magnitude of input position command scaling
    rot_sensitivity (float): Magnitude of scale input rotation commands scaling"""
    def __init__(self, pos_sensitivity, rot_sensitivity)
    def _display_controls()
    def _reset_internal_state(self)
    def start_control(self)
    def get_controller_state(self)
    def on_press(self, key)
    def on_release(self, key)
```

### okami/simulation/robosuite/devices/spacemouse.py

```
"""Driver class for SpaceMouse controller.

This class provides a driver support to SpaceMouse on macOS.
In particular, we assume you are using a SpaceMouse Wireless by default.

To set up a new SpaceMouse controller:
    1. Download and install driver from https://www.3dconnexion.com/service/drivers.html
    2. Install hidapi library through pip
       (make sure you run uninstall hid first if it is installed).
    3. Make sure SpaceMouse is connected before running the script
    4. (Optional) Based on the model of SpaceMouse, you might need to change the
       vendor id and product id that co"""
def to_int16(y1, y2)
def scale_to_control(x, axis_scale, min_v, max_v)
def convert(b1, b2)
class SpaceMouse(Device)
    """A minimalistic driver class for SpaceMouse with HID library.

Note: Use hid.enumerate() to view all USB human interface devices (HID).
Make sure SpaceMouse is detected before running the script.
You can look up its vendor/product id from this method.

Args:
    pos_sensitivity (float): Magnitude of """
    def __init__(self, vendor_id, product_id, pos_sensitivity, rot_sensitivity)
    def _display_controls()
    def _reset_internal_state(self)
    def start_control(self)
    def get_controller_state(self)
    def run(self)
    def control(self)
    def control_gripper(self)
    def on_press(self, key)
    def on_release(self, key)
```

### okami/simulation/robosuite/environments/base.py

```
def register_env(target_class)
def make(env_name)
class EnvMeta(type)
    """Metaclass for registering environments"""
    def __new__(meta, name, bases, class_dict)
class MujocoEnv()
    """Initializes a Mujoco Environment.
Args:
    has_renderer (bool): If true, render the simulation state in
        a viewer instead of headless mode.
    has_offscreen_renderer (bool): True if using off-screen rendering.
    render_camera (str): Name of camera to render if `has_renderer` is True. Sett"""
    def __init__(self, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, lite_physics, horizon, ignore_done, hard_reset, renderer, renderer_config, seed)
    def initialize_renderer(self)
    def initialize_time(self, control_freq)
    def set_xml_processor(self, processor)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _initialize_sim(self, xml_string)
    def reset(self)
    def _reset_observables(self)
    def _reset_internal(self)
    def get_ep_meta(self)
    def set_ep_meta(self, meta)
    def _update_observables(self, force)
    def _get_observations(self, force_update)
    def step(self, action)
    def _pre_action(self, action, policy_step)
    def _post_action(self, action)
    def reward(self, action)
    def render(self)
    def get_pixel_obs(self)
    def close_renderer(self)
    def observation_spec(self)
    def clear_objects(self, object_names)
    def visualize(self, vis_settings)
    def set_camera_pos_quat(self, camera_pos, camera_quat)
    def edit_model_xml(self, xml_str)
    def reset_from_xml_string(self, xml_string)
    def update_state(self)
    def check_contact(self, geoms_1, geoms_2)
    def get_contacts(self, model)
    def add_observable(self, observable)
    def modify_observable(self, observable_name, attribute, modifier)
    def _check_success(self)
    def _destroy_viewer(self)
    def _destroy_sim(self)
    def close(self)
    def observation_modalities(self)
    def observation_names(self)
    def enabled_observables(self)
    def active_observables(self)
    def _visualizations(self)
    def action_spec(self)
    def action_dim(self)

```python
def _get_observations(self, force_update=False):
        """
        Grabs observations from the environment.
        Args:
            force_update (bool): If True, will force all the observables to update their internal values to the newest
                value. This is useful if, e.g., you want to grab observations when directly setting simulation states
                without actually stepping the simulation.
        Returns:
            OrderedDict: OrderedDict containing observations [(name_string, np.array), ...]
        """
        observations = OrderedDict()
        obs_by_modality = OrderedDict()

        # Force an update if requested
        if force_update:
            self._update_observables(force=True)

        # Loop through all observables and grab their current observation
        for obs_name, observable in self._observables.items():
            if observable.is_enabled() and observable.is_active():
                obs = observable.obs
                observations[obs_name] = obs
                modality = observable.modality + "-state"
                if modality not in obs_by_modality:
                    obs_by_modality[modality] = []
                # Make sure all observations are numpy arrays so we can concatenate them
                array_obs = [obs] if type(obs) in {int, float} or not obs.shape else obs
                obs_by_modality[modality].append(np.array(array_obs))

        # Add in modality observations
        for modality, obs in obs_by_modality.items():
            # To save memory, we only concatenate the image observations if explicitly requested
            if modality == "image-state" and not macros.CONCATENATE_IMAGES:
                continue
            observations[modality] = np.concatenate(obs, axis=-1)

        return observations
```

```python
def reward(self, action):
        """
        Reward should be a function of state and action
        Args:
            action (np.array): Action to execute within the environment
        Returns:
            float: Reward from environment
        """
        raise NotImplementedError
```

```python
def observation_spec(self):
        """
        Returns an observation as observation specification.
        An alternative design is to return an OrderedDict where the keys
        are the observation names and the values are the shapes of observations.
        We leave this alternative implementation commented out, as we find the
        current design is easier to use in practice.
        Returns:
            OrderedDict: Observations from the environment
        """
        observation = self.viewer._get_observations() if self.viewer_get_obs else self._get_observations()
        return observation
```

```python
def observation_modalities(self):
        """
        Modalities for this environment's observations
        Returns:
            set: All observation modalities
        """
        return set([observable.modality for observable in self._observables.values()])
```

```python
def observation_names(self):
        """
        Grabs all names for this environment's observables
        Returns:
            set: All observation names
        """
        return set(self._observables.keys())
```
```

### okami/simulation/robosuite/environments/manipulation/door.py

```
class Door(SingleArmEnv)
    """This class corresponds to the door opening task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
    """
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, use_latch, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def _check_success(self)
    def visualize(self, vis_settings)
    def _handle_xpos(self)
    def _gripper_to_handle(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 1.0 is provided if the door is opened

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 0.25], proportional to the distance between door handle and robot arm
            - Rotating: in [0, 0.25], proportional to angle rotated by door handled
              - Note that this component is only relevant if the environment is using the locked door version

        Note that a successfully completed task (door opened) will return 1.0 irregardless of whether the environment
        is using sparse or shaped rewards

        Note that the final reward is normalized and scaled by reward_scale / 1.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np.array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # else, we consider only the case if we're using shaped rewards
        elif self.reward_shaping:
            # Add reaching component
            dist = np.linalg.norm(self._gripper_to_handle)
            reaching_reward = 0.25 * (1 - np.tanh(10.0 * dist))
            reward += reaching_reward
            # Add rotating component if we're using a locked door
            if self.use_latch:
                handle_qpos = self.sim.data.qpos[self.handle_qpos_addr]
                reward += np.clip(0.25 * np.abs(handle_qpos / (0.5 * np.pi)), -0.25, 0.25)

        # Scale reward if requested
        if self.reward_scale is not None:
            reward *= self.reward_scale / 1.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/humanoid_drawer.py

```
class HumanoidDrawer(ManipulationEnv)
    """This class corresponds to the reaching task for humanoid robot.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Note"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _post_action(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.25 is provided if the drawer is lifted

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 1], to encourage the arm to reach the drawer
            - Grasping: in {0, 0.25}, non-zero if arm is grasping the drawer
            - Lifting: in {0, 1}, non-zero if arm has lifted the drawer

        The sparse reward only consists of the lifting component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.25 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        if self._check_success():
            reward = 1.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/humanoid_env.py

```
class HumanoidEnv(ManipulationEnv)
    """A manipulation environment intended for humanoids."""
    def _check_robot_configuration(self, robots)
    def _eef0_xpos(self)
    def _eef1_xpos(self)
    def _eef0_xmat(self)
    def _eef1_xmat(self)
    def _eef0_xquat(self)
    def _eef1_xquat(self)
```

### okami/simulation/robosuite/environments/manipulation/humanoid_pour.py

```
class HumanoidPour(ManipulationEnv)
    """This class corresponds to the reaching task for humanoid robot.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Note"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _post_action(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.25 is provided if the drawer is lifted

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 1], to encourage the arm to reach the drawer
            - Grasping: in {0, 0.25}, non-zero if arm is grasping the drawer
            - Lifting: in {0, 1}, non-zero if arm has lifted the drawer

        The sparse reward only consists of the lifting component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.25 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        if self._check_success():
            reward = 1.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/humanoid_reach.py

```
class HumanoidReach(ManipulationEnv)
    """This class corresponds to the reaching task for humanoid robot.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Note"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _post_action(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.25 is provided if the cube is lifted

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 1], to encourage the arm to reach the cube
            - Grasping: in {0, 0.25}, non-zero if arm is grasping the cube
            - Lifting: in {0, 1}, non-zero if arm has lifted the cube

        The sparse reward only consists of the lifting component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.25 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        if self._check_success():
            reward = 1.0

        # # sparse completion reward
        # if self._check_success():
        #     reward = 2.25

        # # use a shaping reward
        # elif self.reward_shaping:

        #     # reaching reward
        #     cube_pos = self.sim.data.body_xpos[self.cube_body_id]
        #     gripper_site_pos = self.sim.data.site_xpos[self.robots[0].eef_site_id["right"]]
        #     dist = np.linalg.norm(gripper_site_pos - cube_pos)
        #     reaching_reward = 1 - np.tanh(10.0 * dist)
        #     reward += reaching_reward

        #     # grasping reward
        #     if self._check_grasp(gripper=self.robots[0].gripper, object_geoms=self.cube):
        #         reward += 0.25

        # # Scale reward if requested
        # if self.reward_scale is not None:
        #     reward *= self.reward_scale / 2.25

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/lift.py

```
class Lift(ManipulationEnv)
    """This class corresponds to the lifting task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        N"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.25 is provided if the cube is lifted

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 1], to encourage the arm to reach the cube
            - Grasping: in {0, 0.25}, non-zero if arm is grasping the cube
            - Lifting: in {0, 1}, non-zero if arm has lifted the cube

        The sparse reward only consists of the lifting component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.25 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 2.25

        # use a shaping reward
        elif self.reward_shaping:

            # reaching reward
            cube_pos = self.sim.data.body_xpos[self.cube_body_id]
            gripper_site_pos = self.sim.data.site_xpos[self.robots[0].eef_site_id["right"]]
            dist = np.linalg.norm(gripper_site_pos - cube_pos)
            reaching_reward = 1 - np.tanh(10.0 * dist)
            reward += reaching_reward

            # grasping reward
            if self._check_grasp(gripper=self.robots[0].gripper, object_geoms=self.cube):
                reward += 0.25

        # Scale reward if requested
        if self.reward_scale is not None:
            reward *= self.reward_scale / 2.25

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/manipulation_env.py

```
class ManipulationEnv(RobotEnv)
    """Initializes a manipulation-specific robot environment in Mujoco.

Args:
    robots: Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)

    env_configuration (str): Sp"""
    def __init__(self, robots, env_configuration, controller_configs, composite_controller_configs, base_types, gripper_types, initial_qpos, initialization_noise, use_camera_obs, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, lite_physics, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config, seed)
    def _visualizations(self)
    def _check_grasp(self, gripper, object_geoms)
    def _gripper_to_target(self, gripper, target, target_type, return_distance)
    def _visualize_gripper_to_target(self, gripper, target, target_type)
    def _check_robot_configuration(self, robots)
```

### okami/simulation/robosuite/environments/manipulation/nut_assembly.py

```
class NutAssembly(ManipulationEnv)
    """This class corresponds to the nut assembly task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
    """
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, single_object_mode, nut_type, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def staged_rewards(self)
    def on_peg(self, obj_pos, peg_id)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _create_nut_sensors(self, nut_name, modality)
    def _reset_internal(self)
    def _check_success(self)
    def visualize(self, vis_settings)
class NutAssemblySingle(NutAssembly)
    """Easier version of task - place either one round nut or one square nut into its peg."""
    def __init__(self)
class NutAssemblySquare(NutAssembly)
    """Easier version of task - place one square nut into its peg."""
    def __init__(self)
class NutAssemblyRound(NutAssembly)
    """Easier version of task - place one round nut into its peg."""
    def __init__(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

          - a discrete reward of 1.0 per nut if it is placed around its correct peg

        Un-normalized components if using reward shaping, where the maximum is returned if not solved:

          - Reaching: in [0, 0.1], proportional to the distance between the gripper and the closest nut
          - Grasping: in {0, 0.35}, nonzero if the gripper is grasping a nut
          - Lifting: in {0, [0.35, 0.5]}, nonzero only if nut is grasped; proportional to lifting height
          - Hovering: in {0, [0.5, 0.7]}, nonzero only if nut is lifted; proportional to distance from nut to peg

        Note that a successfully completed task (nut around peg) will return 1.0 per nut irregardless of whether the
        environment is using sparse or shaped rewards

        Note that the final reward is normalized and scaled by reward_scale / 2.0 (or 1.0 if only a single nut is
        being used) as well so that the max score is equal to reward_scale

        Args:
            action (np.array): [NOT USED]

        Returns:
            float: reward value
        """
        # compute sparse rewards
        self._check_success()
        reward = np.sum(self.objects_on_pegs)

        # add in shaped rewards
        if self.reward_shaping:
            staged_rewards = self.staged_rewards()
            reward += max(staged_rewards)
        if self.reward_scale is not None:
            reward *= self.reward_scale
            if self.single_object_mode == 0:
                reward /= 2.0
        return reward
```

```python
def staged_rewards(self):
        """
        Calculates staged rewards based on current physical states.
        Stages consist of reaching, grasping, lifting, and hovering.

        Returns:
            4-tuple:

                - (float) reaching reward
                - (float) grasping reward
                - (float) lifting reward
                - (float) hovering reward
        """

        reach_mult = 0.1
        grasp_mult = 0.35
        lift_mult = 0.5
        hover_mult = 0.7

        # filter out objects that are already on the correct pegs
        active_nuts = []
        for i, nut in enumerate(self.nuts):
            if self.objects_on_pegs[i]:
                continue
            active_nuts.append(nut)

        # reaching reward governed by distance to closest object
        r_reach = 0.0
        if active_nuts:
            # reaching reward via minimum distance to the handles of the objects
            dists = [
                self._gripper_to_target(
                    gripper=self.robots[0].gripper,
                    target=active_nut.important_sites["handle"],
                    target_type="site",
                    return_distance=True,
                )
                for active_nut in active_nuts
            ]
            r_reach = (1 - np.tanh(10.0 * min(dists))) * reach_mult

        # grasping reward for touching any objects of interest
        r_grasp = (
            int(
                self._check_grasp(
                    gripper=self.robots[0].gripper,
                    object_geoms=[g for active_nut in active_nuts for g in active_nut.contact_geoms],
                )
            )
            * grasp_mult
        )

        # lifting reward for picking up an object
        r_lift = 0.0
        table_pos = np.array(self.sim.data.body_xpos[self.table_body_id])
        if active_nuts and r_grasp > 0.0:
            z_target = table_pos[2] + 0.2
            object_z_locs = self.sim.data.body_xpos[[self.obj_body_id[active_nut.name] for active_nut in active_nuts]][
                :, 2
            ]
            z_dists = np.maximum(z_target - object_z_locs, 0.0)
            r_lift = grasp_mult + (1 - np.tanh(15.0 * min(z_dists))) * (lift_mult - grasp_mult)

        # hover reward for getting object above peg
        r_hover = 0.0
        if active_nuts:
            r_hovers = np.zeros(len(active_nuts))
            peg_body_ids = [self.peg1_body_id, self.peg2_body_id]
            for i, nut in enumerate(active_nuts):
                valid_obj = False
                peg_pos = None
                for nut_name, idn in self.nut_to_id.items():
                    if nut_name in nut.name.lower():
                        peg_pos = np.array(self.sim.data.body_xpos[peg_body_ids[idn]])[:2]
                        valid_obj = True
                        break
                if not valid_obj:
                    raise Exception("Got invalid object to reach: {}".format(nut.name))
                ob_xy = self.sim.data.body_xpos[self.obj_body_id[nut.name]][:2]
                dist = np.linalg.norm(peg_pos - ob_xy)
                r_hovers[i] = r_lift + (1 - np.tanh(10.0 * dist)) * (hover_mult - lift_mult)
            r_hover = np.max(r_hovers)

        return r_reach, r_grasp, r_lift, r_hover
```
```

### okami/simulation/robosuite/environments/manipulation/pick_place.py

```
class PickPlace(SingleArmEnv)
    """This class corresponds to the pick place task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
      """
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, bin1_pos, bin2_pos, z_offset, z_rotation, use_camera_obs, use_object_obs, reward_scale, reward_shaping, single_object_mode, object_type, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def staged_rewards(self)
    def not_in_bin(self, obj_pos, bin_id)
    def _get_placement_initializer(self)
    def _construct_visual_objects(self)
    def _construct_objects(self)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _create_obj_sensors(self, obj_name, modality)
    def _reset_internal(self)
    def _check_success(self)
    def visualize(self, vis_settings)
class PickPlaceSingle(PickPlace)
    """Easier version of task - place one object into its bin.
A new object is sampled on every reset."""
    def __init__(self)
class PickPlaceMilk(PickPlace)
    """Easier version of task - place one milk into its bin."""
    def __init__(self)
class PickPlaceBread(PickPlace)
    """Easier version of task - place one bread into its bin."""
    def __init__(self)
class PickPlaceCereal(PickPlace)
    """Easier version of task - place one cereal into its bin."""
    def __init__(self)
class PickPlaceCan(PickPlace)
    """Easier version of task - place one can into its bin."""
    def __init__(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

          - a discrete reward of 1.0 per object if it is placed in its correct bin

        Un-normalized components if using reward shaping, where the maximum is returned if not solved:

          - Reaching: in [0, 0.1], proportional to the distance between the gripper and the closest object
          - Grasping: in {0, 0.35}, nonzero if the gripper is grasping an object
          - Lifting: in {0, [0.35, 0.5]}, nonzero only if object is grasped; proportional to lifting height
          - Hovering: in {0, [0.5, 0.7]}, nonzero only if object is lifted; proportional to distance from object to bin

        Note that a successfully completed task (object in bin) will return 1.0 per object irregardless of whether the
        environment is using sparse or shaped rewards

        Note that the final reward is normalized and scaled by reward_scale / 4.0 (or 1.0 if only a single object is
        being used) as well so that the max score is equal to reward_scale

        Args:
            action (np.array): [NOT USED]

        Returns:
            float: reward value
        """
        # compute sparse rewards
        self._check_success()
        reward = np.sum(self.objects_in_bins)

        # add in shaped rewards
        if self.reward_shaping:
            staged_rewards = self.staged_rewards()
            reward += max(staged_rewards)
        if self.reward_scale is not None:
            reward *= self.reward_scale
            if self.single_object_mode == 0:
                reward /= 4.0
        return reward
```

```python
def staged_rewards(self):
        """
        Returns staged rewards based on current physical states.
        Stages consist of reaching, grasping, lifting, and hovering.

        Returns:
            4-tuple:

                - (float) reaching reward
                - (float) grasping reward
                - (float) lifting reward
                - (float) hovering reward
        """

        reach_mult = 0.1
        grasp_mult = 0.35
        lift_mult = 0.5
        hover_mult = 0.7

        # filter out objects that are already in the correct bins
        active_objs = []
        for i, obj in enumerate(self.objects):
            if self.objects_in_bins[i]:
                continue
            active_objs.append(obj)

        # reaching reward governed by distance to closest object
        r_reach = 0.0
        if active_objs:
            # get reaching reward via minimum distance to a target object
            dists = [
                self._gripper_to_target(
                    gripper=self.robots[0].gripper,
                    target=active_obj.root_body,
                    target_type="body",
                    return_distance=True,
                )
                for active_obj in active_objs
            ]
            r_reach = (1 - np.tanh(10.0 * min(dists))) * reach_mult

        # grasping reward for touching any objects of interest
        r_grasp = (
            int(
                self._check_grasp(
                    gripper=self.robots[0].gripper,
                    object_geoms=[g for active_obj in active_objs for g in active_obj.contact_geoms],
                )
            )
            * grasp_mult
        )

        # lifting reward for picking up an object
        r_lift = 0.0
        if active_objs and r_grasp > 0.0:
            z_target = self.bin2_pos[2] + 0.25
            object_z_locs = self.sim.data.body_xpos[[self.obj_body_id[active_obj.name] for active_obj in active_objs]][
                :, 2
            ]
            z_dists = np.maximum(z_target - object_z_locs, 0.0)
            r_lift = grasp_mult + (1 - np.tanh(15.0 * min(z_dists))) * (lift_mult - grasp_mult)

        # hover reward for getting object above bin
        r_hover = 0.0
        if active_objs:
            target_bin_ids = [self.object_to_id[active_obj.name.lower()] for active_obj in active_objs]
            # segment objects into left of the bins and above the bins
            object_xy_locs = self.sim.data.body_xpos[[self.obj_body_id[active_obj.name] for active_obj in active_objs]][
                :, :2
            ]
            y_check = (
                np.abs(object_xy_locs[:, 1] - self.target_bin_placements[target_bin_ids, 1]) < self.bin_size[1] / 4.0
            )
            x_check = (
                np.abs(object_xy_locs[:, 0] - self.target_bin_placements[target_bin_ids, 0]) < self.bin_size[0] / 4.0
            )
            objects_above_bins = np.logical_and(x_check, y_check)
            objects_not_above_bins = np.logical_not(objects_above_bins)
            dists = np.linalg.norm(self.target_bin_placements[target_bin_ids, :2] - object_xy_locs, axis=1)
            # objects to the left get r_lift added to hover reward,
            # those on the right get max(r_lift) added (to encourage dropping)
            r_hover_all = np.zeros(len(active_objs))
            r_hover_all[objects_above_bins] = lift_mult + (1 - np.tanh(10.0 * dists[objects_above_bins])) * (
                hover_mult - lift_mult
            )
            r_hover_all[objects_not_above_bins] = r_lift + (1 - np.tanh(10.0 * dists[objects_not_above_bins])) * (
                hover_mult - lift_mult
            )
            r_hover = np.max(r_hover_all)

        return r_reach, r_grasp, r_lift, r_hover
```
```

### okami/simulation/robosuite/environments/manipulation/single_arm_env.py

```
class SingleArmEnv(ManipulationEnv)
    """A manipulation environment intended for a single robot arm."""
    def _load_model(self)
    def _check_robot_configuration(self, robots)
    def _eef_xpos(self)
    def _eef_xmat(self)
    def _eef_xquat(self)
```

### okami/simulation/robosuite/environments/manipulation/stack.py

```
class Stack(SingleArmEnv)
    """This class corresponds to the stacking task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        """
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def staged_rewards(self)
    def _load_model(self)
    def _setup_references(self)
    def _reset_internal(self)
    def _setup_observables(self)
    def _check_success(self)
    def visualize(self, vis_settings)

```python
def reward(self, action):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.0 is provided if the red block is stacked on the green block

        Un-normalized components if using reward shaping:

            - Reaching: in [0, 0.25], to encourage the arm to reach the cube
            - Grasping: in {0, 0.25}, non-zero if arm is grasping the cube
            - Lifting: in {0, 1}, non-zero if arm has lifted the cube
            - Aligning: in [0, 0.5], encourages aligning one cube over the other
            - Stacking: in {0, 2}, non-zero if cube is stacked on other cube

        The reward is max over the following:

            - Reaching + Grasping
            - Lifting + Aligning
            - Stacking

        The sparse reward only consists of the stacking component.

        Note that the final reward is normalized and scaled by
        reward_scale / 2.0 as well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        r_reach, r_lift, r_stack = self.staged_rewards()
        if self.reward_shaping:
            reward = max(r_reach, r_lift, r_stack)
        else:
            reward = 2.0 if r_stack > 0 else 0.0

        if self.reward_scale is not None:
            reward *= self.reward_scale / 2.0

        return reward
```

```python
def staged_rewards(self):
        """
        Helper function to calculate staged rewards based on current physical states.

        Returns:
            3-tuple:

                - (float): reward for reaching and grasping
                - (float): reward for lifting and aligning
                - (float): reward for stacking
        """
        # reaching is successful when the gripper site is close to the center of the cube
        cubeA_pos = self.sim.data.body_xpos[self.cubeA_body_id]
        cubeB_pos = self.sim.data.body_xpos[self.cubeB_body_id]
        gripper_site_pos = self.sim.data.site_xpos[self.robots[0].eef_site_id]
        dist = np.linalg.norm(gripper_site_pos - cubeA_pos)
        r_reach = (1 - np.tanh(10.0 * dist)) * 0.25

        # grasping reward
        grasping_cubeA = self._check_grasp(gripper=self.robots[0].gripper, object_geoms=self.cubeA)
        if grasping_cubeA:
            r_reach += 0.25

        # lifting is successful when the cube is above the table top by a margin
        cubeA_height = cubeA_pos[2]
        table_height = self.table_offset[2]
        cubeA_lifted = cubeA_height > table_height + 0.04
        r_lift = 1.0 if cubeA_lifted else 0.0

        # Aligning is successful when cubeA is right above cubeB
        if cubeA_lifted:
            horiz_dist = np.linalg.norm(np.array(cubeA_pos[:2]) - np.array(cubeB_pos[:2]))
            r_lift += 0.5 * (1 - np.tanh(horiz_dist))

        # stacking is successful when the block is lifted and the gripper is not holding the object
        r_stack = 0
        cubeA_touching_cubeB = self.check_contact(self.cubeA, self.cubeB)
        if not grasping_cubeA and r_lift > 0 and cubeA_touching_cubeB:
            r_stack = 2.0

        return r_reach, r_lift, r_stack
```
```

### okami/simulation/robosuite/environments/manipulation/tool_hang.py

```
class ToolHang(SingleArmEnv)
    """This class corresponds to the tool hang task for a single robot arm.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
       """
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _create_obj_sensors(self, obj_name, modality, query_name, query_type)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)
    def _check_frame_assembled(self)
    def _check_tool_on_frame(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0.0

        # sparse completion reward
        if self._check_success():
            reward = 1.0

        # Scale reward if requested
        if self.reward_scale is not None:
            reward *= self.reward_scale

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/two_arm_env.py

```
class TwoArmEnv(ManipulationEnv)
    """A manipulation environment intended for two robot arms."""
    def _check_robot_configuration(self, robots)
    def _eef0_xpos(self)
    def _eef1_xpos(self)
    def _eef0_xmat(self)
    def _eef1_xmat(self)
    def _eef0_xquat(self)
    def _eef1_xquat(self)
```

### okami/simulation/robosuite/environments/manipulation/two_arm_handover.py

```
class TwoArmHandover(TwoArmEnv)
    """This class corresponds to the handover task for two robot arms.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Note"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, prehensile, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def _get_task_info(self)
    def _check_success(self)
    def _handle_xpos(self)
    def _hammer_pos(self)
    def _hammer_quat(self)
    def _hammer_angle(self)
    def _gripper_0_to_handle(self)
    def _gripper_1_to_handle(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 2.0 is provided when only Arm 1 is gripping the handle and has the handle
              lifted above a certain threshold

        Un-normalized max-wise components if using reward shaping:

            - Arm0 Reaching: (1) in [0, 0.25] proportional to the distance between Arm 0 and the handle
            - Arm0 Grasping: (2) in {0, 0.5}, nonzero if Arm 0 is gripping the hammer (any part).
            - Arm0 Lifting: (3) in {0, 1.0}, nonzero if Arm 0 lifts the handle from the table past a certain threshold
            - Arm0 Hovering: (4) in {0, [1.0, 1.25]}, nonzero only if Arm0 is actively lifting the hammer, and is
              proportional to the distance between the handle and Arm 1
              conditioned on the handle being lifted from the table and being grasped by Arm 0
            - Mutual Grasping: (5) in {0, 1.5}, nonzero if both Arm 0 and Arm 1 are gripping the hammer (Arm 1 must be
              gripping the handle) while lifted above the table
            - Handover: (6) in {0, 2.0}, nonzero when only Arm 1 is gripping the handle and has the handle
              lifted above the table

        Note that the final reward is normalized and scaled by reward_scale / 2.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        # Initialize reward
        reward = 0

        # use a shaping reward if specified
        if self.reward_shaping:
            # Grab relevant parameters
            arm0_grasp_any, arm1_grasp_handle, hammer_height, table_height = self._get_task_info()
            # First, we'll consider the cases if the hammer is lifted above the threshold (step 3 - 6)
            if hammer_height - table_height > self.height_threshold:
                # Split cases depending on whether arm1 is currently grasping the handle or not
                if arm1_grasp_handle:
                    # Check if arm0 is grasping
                    if arm0_grasp_any:
                        # This is step 5
                        reward = 1.5
                    else:
                        # This is step 6 (completed task!)
                        reward = 2.0
                # This is the case where only arm0 is grasping (step 2-3)
                else:
                    reward = 1.0
                    # Add in up to 0.25 based on distance between handle and arm1
                    dist = np.linalg.norm(self._gripper_1_to_handle)
                    reaching_reward = 0.25 * (1 - np.tanh(1.0 * dist))
                    reward += reaching_reward
            # Else, the hammer is still on the ground ):
            else:
                # Split cases depending on whether arm0 is currently grasping the handle or not
                if arm0_grasp_any:
                    # This is step 2
                    reward = 0.5
                else:
                    # This is step 1, we want to encourage arm0 to reach for the handle
                    dist = np.linalg.norm(self._gripper_0_to_handle)
                    reaching_reward = 0.25 * (1 - np.tanh(1.0 * dist))
                    reward = reaching_reward

        # Else this is the sparse reward setting
        else:
            # Provide reward if only Arm 1 is grasping the hammer and the handle lifted above the pre-defined threshold
            if self._check_success():
                reward = 2.0

        if self.reward_scale is not None:
            reward *= self.reward_scale / 2.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/two_arm_lift.py

```
class TwoArmLift(TwoArmEnv)
    """This class corresponds to the lifting task for two robot arms.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Note:"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, table_full_size, table_friction, use_camera_obs, use_object_obs, reward_scale, reward_shaping, placement_initializer, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def visualize(self, vis_settings)
    def _check_success(self)
    def _handle0_xpos(self)
    def _handle1_xpos(self)
    def _pot_quat(self)
    def _gripper0_to_handle0(self)
    def _gripper1_to_handle1(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 3.0 is provided if the pot is lifted and is parallel within 30 deg to the table

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 0.5], per-arm component that is proportional to the distance between each arm and its
              respective pot handle, and exactly 0.5 when grasping the handle
              - Note that the agent only gets the lifting reward when flipping no more than 30 degrees.
            - Grasping: in {0, 0.25}, binary per-arm component awarded if the gripper is grasping its correct handle
            - Lifting: in [0, 1.5], proportional to the pot's height above the table, and capped at a certain threshold

        Note that the final reward is normalized and scaled by reward_scale / 3.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0

        # check if the pot is tilted more than 30 degrees
        mat = T.quat2mat(self._pot_quat)
        z_unit = [0, 0, 1]
        z_rotated = np.matmul(mat, z_unit)
        cos_z = np.dot(z_unit, z_rotated)
        cos_30 = np.cos(np.pi / 6)
        direction_coef = 1 if cos_z >= cos_30 else 0

        # check for goal completion: cube is higher than the table top above a margin
        if self._check_success():
            reward = 3.0 * direction_coef

        # use a shaping reward
        elif self.reward_shaping:
            # lifting reward
            pot_bottom_height = self.sim.data.site_xpos[self.pot_center_id][2] - self.pot.top_offset[2]
            table_height = self.sim.data.site_xpos[self.table_top_id][2]
            elevation = pot_bottom_height - table_height
            r_lift = min(max(elevation - 0.05, 0), 0.15)
            reward += 10.0 * direction_coef * r_lift

            _gripper0_to_handle0 = self._gripper0_to_handle0
            _gripper1_to_handle1 = self._gripper1_to_handle1

            # gh stands for gripper-handle
            # When grippers are far away, tell them to be closer

            # Get contacts
            (g0, g1) = (
                (self.robots[0].gripper["right"], self.robots[0].gripper["left"])
                if self.env_configuration == "bimanual"
                else (self.robots[0].gripper, self.robots[1].gripper)
            )

            _g0h_dist = np.linalg.norm(_gripper0_to_handle0)
            _g1h_dist = np.linalg.norm(_gripper1_to_handle1)

            # Grasping reward
            if self._check_grasp(gripper=g0, object_geoms=self.pot.handle0_geoms):
                reward += 0.25
            # Reaching reward
            reward += 0.5 * (1 - np.tanh(10.0 * _g0h_dist))

            # Grasping reward
            if self._check_grasp(gripper=g1, object_geoms=self.pot.handle1_geoms):
                reward += 0.25
            # Reaching reward
            reward += 0.5 * (1 - np.tanh(10.0 * _g1h_dist))

        if self.reward_scale is not None:
            reward *= self.reward_scale / 3.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/two_arm_peg_in_hole.py

```
class TwoArmPegInHole(TwoArmEnv)
    """This class corresponds to the peg-in-hole task for two robot arms.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        N"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, use_camera_obs, use_object_obs, reward_scale, reward_shaping, peg_radius, peg_length, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def _check_success(self)
    def _compute_orientation(self)
    def _peg_pose_in_hole_frame(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 5.0 is provided if the peg is inside the plate's hole
              - Note that we enforce that it's inside at an appropriate angle (cos(theta) > 0.95).

        Un-normalized summed components if using reward shaping:

            - Reaching: in [0, 1], to encourage the arms to approach each other
            - Perpendicular Distance: in [0,1], to encourage the arms to approach each other
            - Parallel Distance: in [0,1], to encourage the arms to approach each other
            - Alignment: in [0, 1], to encourage having the right orientation between the peg and hole.
            - Placement: in {0, 1}, nonzero if the peg is in the hole with a relatively correct alignment

        Note that the final reward is normalized and scaled by reward_scale / 5.0 as
        well so that the max score is equal to reward_scale

        """
        reward = 0

        # Right location and angle
        if self._check_success():
            reward = 1.0

        # use a shaping reward
        if self.reward_shaping:
            # Grab relevant values
            t, d, cos = self._compute_orientation()
            # reaching reward
            hole_pos = self.sim.data.body_xpos[self.hole_body_id]
            gripper_site_pos = self.sim.data.body_xpos[self.peg_body_id]
            dist = np.linalg.norm(gripper_site_pos - hole_pos)
            reaching_reward = 1 - np.tanh(1.0 * dist)
            reward += reaching_reward

            # Orientation reward
            reward += 1 - np.tanh(d)
            reward += 1 - np.tanh(np.abs(t))
            reward += cos

        # if we're not reward shaping, scale sparse reward so that the max reward is identical to its dense version
        else:
            reward *= 5.0

        if self.reward_scale is not None:
            reward *= self.reward_scale / 5.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/two_arm_transport.py

```
class TwoArmTransport(TwoArmEnv)
    """This class corresponds to the transport task for two robot arms, requiring a payload to be transported from an
initial bin into a target bin, while removing trash from the target bin to a trash bin.

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated wi"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, tables_boundary, table_friction, bin_size, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _get_placement_initializer(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _reset_internal(self)
    def _check_success(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of 1.0 is provided when the payload is in the target bin and the trash is in the trash
                bin

        Un-normalized max-wise components if using reward shaping:

            # TODO!

        Note that the final reward is normalized and scaled by reward_scale / 1.0 as
        well so that the max score is equal to reward_scale

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        # Initialize reward
        reward = 0

        # use a shaping reward if specified
        if self.reward_shaping:
            # TODO! So we print a warning and force sparse rewards
            print(f"\n\nWarning! No dense reward current implemented for this task. Forcing sparse rewards\n\n")
            self.reward_shaping = False

        # Else this is the sparse reward setting
        else:
            # Provide reward if payload is in target bin and trash is in trash bin
            if self._check_success():
                reward = 1.0

        if self.reward_scale is not None:
            reward *= self.reward_scale / 1.0

        return reward
```
```

### okami/simulation/robosuite/environments/manipulation/wipe.py

```
class Wipe(SingleArmEnv)
    """This class corresponds to the Wiping task for a single robot arm

Args:
    robots (str or list of str): Specification for specific robot arm(s) to be instantiated within this env
        (e.g: "Sawyer" would generate one arm; ["Panda", "Panda", "Sawyer"] would generate three robot arms)
        Not"""
    def __init__(self, robots, env_configuration, controller_configs, gripper_types, initialization_noise, use_camera_obs, use_object_obs, reward_scale, reward_shaping, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, task_config, renderer, renderer_config)
    def reward(self, action)
    def _load_model(self)
    def _setup_observables(self)
    def _create_marker_sensors(self, i, marker, modality)
    def _reset_internal(self)
    def _check_success(self)
    def _check_terminated(self)
    def _post_action(self, action)
    def _get_wipe_information(self)
    def _has_gripper_contact(self)

```python
def reward(self, action=None):
        """
        Reward function for the task.

        Sparse un-normalized reward:

            - a discrete reward of self.unit_wiped_reward is provided per single dirt (peg) wiped during this step
            - a discrete reward of self.task_complete_reward is provided if all dirt is wiped

        Note that if the arm is either colliding or near its joint limit, a reward of 0 will be automatically given

        Un-normalized summed components if using reward shaping (individual components can be set to 0:

            - Reaching: in [0, self.distance_multiplier], proportional to distance between wiper and centroid of dirt
              and zero if the table has been fully wiped clean of all the dirt
            - Table Contact: in {0, self.wipe_contact_reward}, non-zero if wiper is in contact with table
            - Wiping: in {0, self.unit_wiped_reward}, non-zero for each dirt (peg) wiped during this step
            - Cleaned: in {0, self.task_complete_reward}, non-zero if no dirt remains on the table
            - Collision / Joint Limit Penalty: in {self.arm_limit_collision_penalty, 0}, nonzero if robot arm
              is colliding with an object
              - Note that if this value is nonzero, no other reward components can be added
            - Large Force Penalty: in [-inf, 0], scaled by wiper force and directly proportional to
              self.excess_force_penalty_mul if the current force exceeds self.pressure_threshold_max
            - Large Acceleration Penalty: in [-inf, 0], scaled by estimated wiper acceleration and directly
              proportional to self.ee_accel_penalty

        Note that the final per-step reward is normalized given the theoretical best episode return and then scaled:
        reward_scale * (horizon /
        (num_markers * unit_wiped_reward + horizon * (wipe_contact_reward + task_complete_reward)))

        Args:
            action (np array): [NOT USED]

        Returns:
            float: reward value
        """
        reward = 0

        total_force_ee = np.linalg.norm(np.array(self.robots[0].recent_ee_forcetorques.current[:3]))

        # Neg Reward from collisions of the arm with the table
        if self.check_contact(self.robots[0].robot_model):
            if self.reward_shaping:
                reward = self.arm_limit_collision_penalty
            self.collisions += 1
        elif self.robots[0].check_q_limits():
            if self.reward_shaping:
                reward = self.arm_limit_collision_penalty
            self.collisions += 1
        else:
            # If the arm is not colliding or in joint limits, we check if we are wiping
            # (we don't want to reward wiping if there are unsafe situations)
            active_markers = []

            # Current 3D location of the corners of the wiping tool in world frame
            c_geoms = self.robots[0].gripper.important_geoms["corners"]
            corner1_id = self.sim.model.geom_name2id(c_geoms[0])
            corner1_pos = np.array(self.sim.data.geom_xpos[corner1_id])
            corner2_id = self.sim.model.geom_name2id(c_geoms[1])
            corner2_pos = np.array(self.sim.data.geom_xpos[corner2_id])
            corner3_id = self.sim.model.geom_name2id(c_geoms[2])
            corner3_pos = np.array(self.sim.data.geom_xpos[corner3_id])
            corner4_id = self.sim.model.geom_name2id(c_geoms[3])
            corner4_pos = np.array(self.sim.data.geom_xpos[corner4_id])

            # Unit vectors on my plane
            v1 = corner1_pos - corner2_pos
            v1 /= np.linalg.norm(v1)
            v2 = corner4_pos - corner2_pos
            v2 /= np.linalg.norm(v2)

            # Corners of the tool in the coordinate frame of the plane
            t1 = np.array([np.dot(corner1_pos - corner2_pos, v1), np.dot(corner1_pos - corner2_pos, v2)])
            t2 = np.array([np.dot(corner2_pos - corner2_pos, v1), np.dot(corner2_pos - corner2_pos, v2)])
            t3 = np.
```
```

### okami/simulation/robosuite/environments/robot_env.py

```
class RobotEnv(MujocoEnv)
    """Initializes a robot environment in Mujoco.

Args:
    robots: Specification for specific robot(s) to be instantiated within this env

    env_configuration (str): Specifies how to position the robot(s) within the environment. Default is "default",
        which should be interpreted accordingly by a"""
    def __init__(self, robots, env_configuration, base_types, controller_configs, composite_controller_configs, initialization_noise, use_camera_obs, has_renderer, has_offscreen_renderer, render_camera, render_collision_mesh, render_visual_mesh, render_gpu_device_id, control_freq, lite_physics, horizon, ignore_done, hard_reset, camera_names, camera_heights, camera_widths, camera_depths, camera_segmentations, robot_configs, renderer, renderer_config, seed)
    def visualize(self, vis_settings)
    def _visualizations(self)
    def action_spec(self)
    def action_dim(self)
    def _input2list(inp, length)
    def _load_model(self)
    def _setup_references(self)
    def _setup_observables(self)
    def _create_camera_sensors(self, cam_name, cam_w, cam_h, cam_d, cam_segs, modality)
    def _create_segementation_sensor(self, cam_name, cam_w, cam_h, cam_s, seg_name_root, modality)
    def _reset_internal(self)
    def _pre_action(self, action, policy_step)
    def _load_robots(self)
    def reward(self, action)
    def _check_success(self)
    def _check_robot_configuration(self, robots)

```python
def reward(self, action):
        """
        Runs superclass method by default
        """
        return super().reward(action)
```
```

### okami/simulation/robosuite/macros.py

```
"""Macro settings that can be imported and toggled. Internally, specific parts of the codebase rely on these settings
for determining core functionality.

To make sure global reference is maintained, should import these settings as:

`import robosuite.macros as macros`"""
```

### okami/simulation/robosuite/models/arenas/arena.py

```
class Arena(MujocoXML)
    """Base arena class."""
    def __init__(self, fname)
    def set_origin(self, offset)
    def set_camera(self, camera_name, pos, quat, camera_attribs)
    def _postprocess_arena(self)
```

### okami/simulation/robosuite/models/arenas/bins_arena.py

```
class BinsArena(Arena)
    """Workspace that contains two bins placed side by side.

Args:
    bin1_pos (3-tuple): (x,y,z) position to place bin1
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table"""
    def __init__(self, bin1_pos, table_full_size, table_friction)
    def configure_location(self)
```

### okami/simulation/robosuite/models/arenas/empty_arena.py

```
class EmptyArena(Arena)
    """Empty workspace."""
    def __init__(self)
```

### okami/simulation/robosuite/models/arenas/multi_table_arena.py

```
class MultiTableArena(Arena)
    """Workspace that contains multiple tables.
Args:
    table_offsets (list of 3-array): (x,y,z) offset from center of arena when placing each table.
        Note that the number of tables is inferred from the length of this list
        Note that the z value sets the upper limit of the table
    table_r"""
    def __init__(self, table_offsets, table_rots, table_full_sizes, table_frictions, has_legs, xml)
    def _add_table(self, name, offset, rot, half_size, friction, has_legs)
    def configure_location(self)
    def _postprocess_arena(self)
```

### okami/simulation/robosuite/models/arenas/pegs_arena.py

```
class PegsArena(TableArena)
    """Workspace that contains a tabletop with two fixed pegs.

Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of arena when placing"""
    def __init__(self, table_full_size, table_friction, table_offset)
```

### okami/simulation/robosuite/models/arenas/table_arena.py

```
class TableArena(Arena)
    """Workspace that contains an empty table.


Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of arena when placing table.
       """
    def __init__(self, table_full_size, table_friction, table_offset, has_legs, xml)
    def configure_location(self)
    def table_top_abs(self)
```

### okami/simulation/robosuite/models/arenas/wipe_arena.py

```
class WipeArena(TableArena)
    """Workspace that contains an empty table with visual markers on its surface.

Args:
    table_full_size (3-tuple): (L,W,H) full dimensions of the table
    table_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the table
    table_offset (3-tuple): (x,y,z) offset from center of"""
    def __init__(self, table_full_size, table_friction, table_offset, coverage_factor, num_markers, table_friction_std, line_width, two_clusters)
    def configure_location(self)
    def reset_arena(self, sim)
    def sample_start_pos(self)
    def sample_path_pos(self, pos)
```

### okami/simulation/robosuite/models/base.py

```
class MujocoXML(object)
    """Base class of Mujoco xml file
Wraps around ElementTree and provides additional functionality for merging different models.
Specially, we keep track of <worldbody/>, <actuator/> and <asset/>

When initialized, loads a mujoco xml from file.

Args:
    fname (str): path to the MJCF xml file."""
    def __init__(self, fname)
    def resolve_asset_dependency(self)
    def create_default_element(self, name)
    def merge(self, others, merge_body)
    def get_model(self, mode)
    def get_xml(self)
    def save_model(self, fname, pretty)
    def merge_assets(self, other)
    def get_element_names(self, root, element_type)
    def _get_default_classes(default)
    def _replace_defaults_inline(self, default_dic, root)
    def name(self)
class MujocoModel(object)
    """Base class for all simulation models used in mujoco.

Standardizes core API for accessing models' relevant geoms, names, etc."""
    def correct_naming(self, names)
    def set_sites_visibility(self, sim, visible)
    def exclude_from_prefixing(self, inp)
    def name(self)
    def naming_prefix(self)
    def root_body(self)
    def bodies(self)
    def joints(self)
    def actuators(self)
    def sites(self)
    def sensors(self)
    def contact_geoms(self)
    def visual_geoms(self)
    def important_geoms(self)
    def important_sites(self)
    def important_sensors(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
class MujocoXMLModel(MujocoXML, MujocoModel)
    """Base class for all MujocoModels that are based on a raw XML file.

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this model instance"""
    def __init__(self, fname, idn)
    def exclude_from_prefixing(self, inp)
    def base_offset(self)
    def name(self)
    def naming_prefix(self)
    def root_body(self)
    def bodies(self)
    def joints(self)
    def actuators(self)
    def sites(self)
    def sensors(self)
    def contact_geoms(self)
    def visual_geoms(self)
    def important_sites(self)
    def important_geoms(self)
    def important_sensors(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
    def contact_geom_rgba(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/aloha_mount.py

```
"""Rethink's Alternative Mount (Officially used on Baxter)."""
class AlohaMount(MountModel)
    """Mount officially used for Rethink's Baxter Robot. Includes only a wheeled pedestal.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/b1_base.py

```
class B1(LegBaseModel)
    """Rethink's Generic Mount (Officially used on Baxter).

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
    def init_qpos(self)
class B1Floating(LegBaseModel)
    """Rethink's Generic Mount (Officially used on Baxter).

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/bases/base_factory.py

```
"""Defines a string based method of initializing mounts"""
def base_factory(name, idn)
```

### okami/simulation/robosuite/models/bases/floating_legged_base.py

```
"""Rethink's Generic Mount (Officially used on Sawyer)."""
class FloatingLeggedBase(MobileBaseModel)
    """Dummy mobile base to signify no mount.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/leg_base_model.py

```
"""Defines the base class of all mobile bases"""
class LegBaseModel(MujocoXMLModel)
    """Base class for mounts that will be attached to robots. Note that this model's root body will be directly
appended to the robot's root body, so all offsets should be taken relative to that.

Args:
    fname (str): Path to relevant xml file to create this mount instance
    idn (int or str): Number or"""
    def __init__(self, fname, idn)
    def init_qpos(self)
    def naming_prefix(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
    def contact_geom_rgba(self)
    def top_offset(self)
    def horizontal_radius(self)
    def _remove_joint_actuation(self, part_name)
    def _remove_free_joint(self)
    def _add_mobile_joint(self)
```

### okami/simulation/robosuite/models/bases/mobile_base_factory.py

```
"""Defines a string based method of initializing mounts"""
def mobile_base_factory(name, idn)
```

### okami/simulation/robosuite/models/bases/mobile_base_model.py

```
"""Defines the base class of all mobile bases"""
class MobileBaseModel(MujocoXMLModel)
    """Base class for mounts that will be attached to robots. Note that this model's root body will be directly
appended to the robot's root body, so all offsets should be taken relative to that.

Args:
    fname (str): Path to relevant xml file to create this mount instance
    idn (int or str): Number or"""
    def __init__(self, fname, idn)
    def naming_prefix(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
    def contact_geom_rgba(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/mount_model.py

```
"""Defines the base class of all mounts"""
class MountModel(MujocoXMLModel)
    """Base class for mounts that will be attached to robots. Note that this model's root body will be directly
appended to the robot's root body, so all offsets should be taken relative to that.

Args:
    fname (str): Path to relevant xml file to create this mount instance
    idn (int or str): Number or"""
    def __init__(self, fname, idn)
    def naming_prefix(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
    def contact_geom_rgba(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/no_actuation_base.py

```
"""Rethink's Generic Mount (Officially used on Sawyer)."""
class NoActuationBase(MobileBaseModel)
    """Dummy mobile base to signify no mount.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/null_mobile_base.py

```
"""Rethink's Generic Mount (Officially used on Sawyer)."""
class NullMobileBase(MobileBaseModel)
    """Dummy mobile base to signify no mount.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/null_mount.py

```
"""Rethink's Generic Mount (Officially used on Sawyer)."""
class NullMount(MountModel)
    """Dummy Mount to signify no mount.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/omron_mobile_base.py

```
"""Omron LD-60 Mobile Base."""
class OmronMobileBase(MobileBaseModel)
    """Omron LD-60 Mobile Base.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/rethink_minimal_mount.py

```
"""Rethink's Alternative Mount (Officially used on Baxter)."""
class RethinkMinimalMount(MountModel)
    """Mount officially used for Rethink's Baxter Robot. Includes only a wheeled pedestal.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/rethink_mount.py

```
"""Rethink's Generic Mount (Officially used on Sawyer)."""
class RethinkMount(MountModel)
    """Mount officially used for Rethink's Sawyer Robot. Includes a controller box and wheeled pedestal.

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/bases/spot_base.py

```
class Spot(LegBaseModel)
    """Rethink's Generic Mount (Officially used on Baxter).

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
    def init_qpos(self)
class SpotFloating(LegBaseModel)
    """Rethink's Generic Mount (Officially used on Baxter).

Args:
    idn (int or str): Number or some other unique identification string for this mount instance"""
    def __init__(self, idn)
    def top_offset(self)
    def horizontal_radius(self)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/grippers/aloha_gripper.py

```
"""Gripper with two fingers for Rethink Robots."""
class AlohaGripperBase(GripperModel)
    """Gripper with long two-fingered parallel jaw.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class AlohaGripper(AlohaGripperBase)
    """Modifies two finger base to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/bd_gripper.py

```
class BDGripper(GripperModel)
    """Gripper for the Spot Arm.
Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def _important_geoms(self)
```

### okami/simulation/robosuite/models/grippers/g1_three_finger_gripper.py

```
"""Dexterous hands for GR1 robot."""
class G1ThreeFingerLeftGripper(GripperModel)
    """Three-finger left gripper  of G1 robot

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
class G1ThreeFingerRightGripper(GripperModel)
    """Three-finger right gripper of G1 robot

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/google_gripper.py

```
"""Gripper for Franka's Panda (has two fingers)."""
class GoogleGripperBase(GripperModel)
    """Gripper for Franka's Panda (has two fingers).

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
class GoogleGripper(GoogleGripperBase)
    """Modifies PandaGripperBase to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/gripper_factory.py

```
"""Defines a string based method of initializing grippers"""
def gripper_factory(name, idn)
```

### okami/simulation/robosuite/models/grippers/gripper_model.py

```
"""Defines the base class of all grippers"""
class GripperModel(MujocoXMLModel)
    """Base class for grippers

Args:
    fname (str): Path to relevant xml file to create this gripper instance
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, fname, idn)
    def format_action(self, action)
    def naming_prefix(self)
    def speed(self)
    def dof(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def contact_geom_rgba(self)
    def init_qpos(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
```

### okami/simulation/robosuite/models/grippers/gripper_tester.py

```
"""Defines GripperTester that is used to test the physical properties of various grippers"""
class GripperTester()
    """A class that is used to test gripper

Args:
    gripper (GripperModel): A gripper instance to be tested
    pos (str): (x y z) position to place the gripper in string form, e.g. '0 0 0.3'
    quat (str): rotation to apply to gripper in string form, e.g. '0 0 1 0' to flip z axis
    gripper_low_pos ("""
    def __init__(self, gripper, pos, quat, gripper_low_pos, gripper_high_pos, box_size, box_density, step_time, render)
    def start_simulation(self)
    def reset(self)
    def close(self)
    def step(self)
    def _apply_gripper_action(self, action)
    def _apply_gravity_compensation(self)
    def loop(self, total_iters, test_y, y_baseline)
    def object_height(self)
```

### okami/simulation/robosuite/models/grippers/inspire_hands.py

```
"""Dexterous hands for GR1 robot."""
class InspireLeftHand(GripperModel)
    """Dexterous left hand of GR1 robot

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
class InspireRightHand(GripperModel)
    """Dexterous right hand of GR1 robot

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/jaco_three_finger_gripper.py

```
"""Gripper for Kinova's Jaco robot arm (has three fingers)."""
class JacoThreeFingerGripperBase(GripperModel)
    """Gripper for Kinova's Jaco robot arm (has three fingers).

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class JacoThreeFingerGripper(JacoThreeFingerGripperBase)
    """Modifies JacoThreeFingerGripperBase to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
class JacoThreeFingerDexterousGripper(JacoThreeFingerGripperBase)
    """Dexterous variation of the Jaco gripper in which all finger are actuated independently"""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/null_gripper.py

```
"""Null Gripper (if we don't want to attach gripper to robot eef)."""
class NullGripper(GripperModel)
    """Dummy Gripper class to represent no gripper

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/grippers/panda_gripper.py

```
"""Gripper for Franka's Panda (has two fingers)."""
class PandaGripperBase(GripperModel)
    """Gripper for Franka's Panda (has two fingers).

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class PandaGripper(PandaGripperBase)
    """Modifies PandaGripperBase to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/rethink_gripper.py

```
"""Gripper with two fingers for Rethink Robots."""
class RethinkGripperBase(GripperModel)
    """Gripper with long two-fingered parallel jaw.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class RethinkGripper(RethinkGripperBase)
    """Modifies two finger base to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/robotiq_140_gripper.py

```
"""Gripper with 140mm Jaw width from Robotiq (has two fingers)."""
class Robotiq140GripperBase(GripperModel)
    """Gripper with 140mm Jaw width from Robotiq (has two fingers).

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class Robotiq140Gripper(Robotiq140GripperBase)
    """Modifies Robotiq140GripperBase to only take one action."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/robotiq_85_gripper.py

```
"""6-DoF gripper with its open/close variant"""
class Robotiq85GripperBase(GripperModel)
    """6-DoF Robotiq gripper.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class Robotiq85Gripper(Robotiq85GripperBase)
    """1-DoF variant of RobotiqGripperBase."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/robotiq_three_finger_gripper.py

```
"""Gripper with 11-DoF controlling three fingers and its open/close variant."""
class RobotiqThreeFingerGripperBase(GripperModel)
    """Gripper with 11 dof controlling three fingers.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
class RobotiqThreeFingerGripper(RobotiqThreeFingerGripperBase)
    """1-DoF variant of RobotiqThreeFingerGripperBase."""
    def format_action(self, action)
    def speed(self)
    def dof(self)
class RobotiqThreeFingerDexterousGripper(RobotiqThreeFingerGripperBase)
    """Dexterous variation of the 3-finger Robotiq gripper in which all finger are actuated independently as well
as the scissor joint between fingers 1 and 2"""
    def format_action(self, action)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/wiping_gripper.py

```
"""Gripper without fingers to wipe a surface"""
class WipingGripper(GripperModel)
    """A Wiping Gripper with no actuation and enabled with sensors to detect contact forces

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
```

### okami/simulation/robosuite/models/grippers/yumi_gripper.py

```
"""Dexterous hands for GR1 robot."""
class YumiRightGripper(GripperModel)
    """Right gripper of Yumi Robot.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
class YumiLeftGripper(GripperModel)
    """Left gripper of Yumi Robot.

Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def speed(self)
    def dof(self)
```

### okami/simulation/robosuite/models/grippers/z1_gripper.py

```
class Z1Gripper(GripperModel)
    """Gripper for Franka's Panda (has two fingers).
Args:
    idn (int or str): Number or some other unique identification string for this gripper instance"""
    def __init__(self, idn)
    def format_action(self, action)
    def init_qpos(self)
    def _important_geoms(self)
```

### okami/simulation/robosuite/models/objects/composite/bin.py

```
class Bin(CompositeObject)
    """Generates a four-walled bin container with an open top.
Args:
    name (str): Name of this Bin object
    bin_size (3-array): (x,y,z) full size of bin
    wall_thickness (float): How thick to make walls of bin
    transparent_walls (bool): If True, walls will be semi-translucent
    friction (3-arra"""
    def __init__(self, name, bin_size, wall_thickness, transparent_walls, friction, density, use_texture, rgba)
    def _get_geom_attrs(self)
    def base_geoms(self)
```

### okami/simulation/robosuite/models/objects/composite/cone.py

```
class ConeObject(CompositeObject)
    """Generates an approximate cone object by using cylinder or box geoms.
Args:
    name (str): Name of this Cone object
    outer_radius (float): Radius of cone base
    inner_radius (float): Radius of cone tip (since everything is a cylinder or box)
    height (float): Height of cone
    ngeoms (int): """
    def __init__(self, name, outer_radius, inner_radius, height, ngeoms, use_box, rgba, material, density, solref, solimp, friction)
    def _get_geom_attrs(self)
```

### okami/simulation/robosuite/models/objects/composite/hammer.py

```
class HammerObject(CompositeObject)
    """Generates a Hammer object with a cylindrical or box-shaped handle, cubic head, cylindrical face and triangular claw
(used in Handover task)

Args:
    name (str): Name of this Hammer object

    handle_shape (str): Either "box", for a box-shaped handle, or "cylinder", for a cylindrically-shaped hand"""
    def __init__(self, name, handle_shape, handle_radius, handle_length, handle_density, handle_friction, head_density_ratio, use_texture, rgba_handle, rgba_head, rgba_face, rgba_claw)
    def _get_geom_attrs(self)
    def init_quat(self)
    def handle_geoms(self)
    def head_geoms(self)
    def face_geoms(self)
    def claw_geoms(self)
    def all_geoms(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/objects/composite/hollow_cylinder.py

```
class HollowCylinderObject(CompositeObject)
    """Generates an approximate hollow cylinder object by using box geoms.
Args:
    name (str): Name of this HollowCylinder object
    outer_radius (float): Outer radius of hollow cylinder
    inner_radius (float): Inner radius of hollow cylinder
    height (float): Height of hollow cylinder
    ngeoms (i"""
    def __init__(self, name, outer_radius, inner_radius, height, ngeoms, rgba, material, density, solref, solimp, friction, make_half)
    def _get_geom_attrs(self)
```

### okami/simulation/robosuite/models/objects/composite/hook_frame.py

```
class HookFrame(CompositeObject)
    """Generates an upside down L-shaped frame (a "hook" shape), intended to be used with StandWithMount object.
Args:
    name (str): Name of this object
    frame_length (float): How long the frame is
    frame_height (float): How tall the frame is
    frame_thickness (float): How thick the frame is
    """
    def __init__(self, name, frame_length, frame_height, frame_thickness, hook_height, grip_location, grip_size, tip_size, friction, density, solref, solimp, use_texture, rgba)
    def _get_geom_attrs(self)
    def init_quat(self)
```

### okami/simulation/robosuite/models/objects/composite/lid.py

```
class Lid(CompositeObject)
    """Generates a square lid with a simple handle.
Args:
    name (str): Name of this Lid object
    lid_size (3-array): (length, width, thickness) of lid
    handle_size (3-array): (thickness, length, height) of handle
    transparent (bool): If True, lid will be semi-translucent
    friction (3-array or"""
    def __init__(self, name, lid_size, handle_size, transparent, friction, density, use_texture, rgba)
    def _get_geom_attrs(self)
    def handle_geoms(self)
```

### okami/simulation/robosuite/models/objects/composite/pot_with_handles.py

```
class PotWithHandlesObject(CompositeObject)
    """Generates the Pot object with side handles (used in TwoArmLift)

Args:
    name (str): Name of this Pot object

    body_half_size (3-array of float): If specified, defines the (x,y,z) half-dimensions of the main pot
        body. Otherwise, defaults to [0.07, 0.07, 0.07]

    handle_radius (float):"""
    def __init__(self, name, body_half_size, handle_radius, handle_length, handle_width, handle_friction, density, use_texture, rgba_body, rgba_handle_0, rgba_handle_1, solid_handle, thickness)
    def _get_geom_attrs(self)
    def handle_distance(self)
    def handle0_geoms(self)
    def handle1_geoms(self)
    def handle_geoms(self)
    def important_sites(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/objects/composite/stand_with_mount.py

```
class StandWithMount(CompositeObject)
    """Generates a flat stand with a four-walled mount sticking out of the top.
Args:
    name (str): Name of this object
    size (3-array): (x,y,z) full size of object
    mount_location (2-array): (x,y) location to place mount, relative to center of stand
    mount_width (float): How wide mount is (meas"""
    def __init__(self, name, size, mount_location, mount_width, wall_thickness, base_thickness, initialize_on_side, add_hole_vis, friction, density, solref, solimp, use_texture, rgba)
    def _get_geom_attrs(self)
    def init_quat(self)
    def base_geoms(self)
```

### okami/simulation/robosuite/models/objects/composite_body/hinged_box.py

```
class HingedBoxObject(CompositeBodyObject)
    """An example object that demonstrates the CompositeBodyObject functionality. This object consists of two cube bodies
joined together by a hinge joint.

Args:
    name (str): Name of this object

    box1_size (3-array): (L, W, H) half-sizes for the first box

    box2_size (3-array): (L, W, H) half-si"""
    def __init__(self, name, box1_size, box2_size, use_texture)
```

### okami/simulation/robosuite/models/objects/composite_body/ratcheting_wrench.py

```
class RatchetingWrenchObject(CompositeBodyObject)
    """A ratcheting wrench made out of mujoco primitives.
Args:
    name (str): Name of this object
    handle_size ([float]): (L, W, H) half-sizes for the handle (center part of wrench)
    outer_radius_1 (float): Outer radius of first end of wrench
    inner_radius_1 (float): Inner radius of first end of"""
    def __init__(self, name, handle_size, outer_radius_1, inner_radius_1, height_1, outer_radius_2, inner_radius_2, height_2, ngeoms, grip_size, density, solref, solimp, friction)
```

### okami/simulation/robosuite/models/objects/generated_objects.py

```
class CompositeBodyObject(MujocoGeneratedObject)
    """An object constructed out of multiple bodies to make more complex shapes.

Args:
    name (str): Name of overall object

    objects (MujocoObject or list of MujocoObjects): object(s) to combine to form the composite body object.
        Note that these objects will be added sequentially, so if an o"""
    def __init__(self, name, objects, object_locations, object_quats, object_parents, joints, body_joints, sites, total_size, locations_relative_to_corner)
    def _get_object_subtree(self)
    def _get_object_properties(self)
    def _append_object(self, root, obj, parent_name, pos, quat)
    def _append_joints(self, root, body_name, joint_specs)
    def _remove_joints(body)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
class CompositeObject(MujocoGeneratedObject)
    """An object constructed out of basic geoms to make more intricate shapes.

Note that by default, specifying None for a specific geom element will usually set a value to the mujoco defaults.

Args:
    name (str): Name of overall object

    total_size (list): (x, y, z) half-size in each dimension for """
    def __init__(self, name, total_size, geom_types, geom_sizes, geom_locations, geom_quats, geom_names, geom_rgbas, geom_materials, geom_frictions, geom_condims, rgba, density, solref, solimp, locations_relative_to_center, joints, sites, obj_types, duplicate_collision_geoms)
    def get_bounding_box_half_size(self)
    def in_box(self, position, object_position)
    def _get_object_subtree(self)
    def _size_to_cartesian_half_lengths(geom_type, geom_size)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
class PrimitiveObject(MujocoGeneratedObject)
    """Base class for all programmatically generated mujoco object
i.e., every MujocoObject that does not have an corresponding xml file

Args:
    name (str): (unique) name to identify this generated object

    size (n-tuple of float): relevant size parameters for the object, should be of size 1 - 3

   """
    def __init__(self, name, size, rgba, density, friction, solref, solimp, material, joints, obj_type, duplicate_collision_geoms)
    def _get_object_subtree_(self, ob_type)
    def _get_object_subtree(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
```

### okami/simulation/robosuite/models/objects/group/transport.py

```
class TransportGroup(ObjectGroup)
    """Group of objects that capture transporting a payload placed in a start bin to a target bin, while
also requiring a piece of trash to be removed from the target bin
Args:
    name (str): Name of that will the prepended to all geom bodies generated for this group
    payload (MujocoObject): Object tha"""
    def __init__(self, name, payload, trash, bin_size)
    def get_states(self)
    def _generate_objects(self)
    def update_sim(self, sim)
    def lid_handle_pos(self)
    def lid_handle_quat(self)
    def payload_pos(self)
    def payload_quat(self)
    def trash_pos(self)
    def trash_quat(self)
    def target_bin_pos(self)
    def trash_bin_pos(self)
    def trash_in_trash_bin(self)
    def payload_in_target_bin(self)
```

### okami/simulation/robosuite/models/objects/object_groups.py

```
class ObjectGroup()
    """An abstraction that encompasses a group of objects that interact together in a meaningful way
name (str): Name of this object group. This will be prepended to all objects generated by this group."""
    def __init__(self, name)
    def get_states(self)
    def update_sim(self, sim)
    def _generate_objects(self)
    def objects(self)
```

### okami/simulation/robosuite/models/objects/objects.py

```
class MujocoObject(MujocoModel)
    """Base class for all objects.

We use Mujoco Objects to implement all objects that:

    1) may appear for multiple times in a task
    2) can be swapped between different tasks

Typical methods return copy so the caller can all joints/attributes as wanted

Args:
    obj_type (str): Geom elements to g"""
    def __init__(self, obj_type, duplicate_collision_geoms)
    def merge_assets(self, other)
    def get_obj(self)
    def exclude_from_prefixing(self, inp)
    def _get_object_subtree(self)
    def _get_object_properties(self)
    def name(self)
    def naming_prefix(self)
    def root_body(self)
    def bodies(self)
    def joints(self)
    def actuators(self)
    def sites(self)
    def sensors(self)
    def contact_geoms(self)
    def visual_geoms(self)
    def important_geoms(self)
    def important_sites(self)
    def important_sensors(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_site_attrib_template()
    def get_joint_attrib_template()
    def get_bounding_box_half_size(self)
    def get_bounding_box_size(self)
class MujocoXMLObject(MujocoObject, MujocoXML)
    """MujocoObjects that are loaded from xml files (by default, inherit all properties (e.g.: name)
from MujocoObject class first!)

Args:
    fname (str): XML File path

    name (str): Name of this MujocoXMLObject

    joints (None or str or list of dict): each dictionary corresponds to a joint that wil"""
    def __init__(self, fname, name, joints, obj_type, duplicate_collision_geoms, scale)
    def _get_object_subtree(self)
    def exclude_from_prefixing(self, inp)
    def _get_object_properties(self)
    def _duplicate_visual_from_collision(element)
    def _get_geoms(self, root, _parent)
    def _get_elements(self, root, type, _parent)
    def set_pos(self, pos)
    def set_euler(self, euler)
    def rot(self)
    def set_scale(self, scale, obj)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
    def _get_elements_by_name(self, geom_names, body_names, joint_names)
class MujocoGeneratedObject(MujocoObject)
    """Base class for all procedurally generated objects.

Args:
    obj_type (str): Geom elements to generate / extract for this object. Must be one of:

        :`'collision'`: Only collision geoms are returned (this corresponds to group 0 geoms)
        :`'visual'`: Only visual geoms are returned (this """
    def __init__(self, obj_type, duplicate_collision_geoms)
    def sanity_check(self)
    def get_collision_attrib_template()
    def get_visual_attrib_template()
    def append_material(self, material)
    def exclude_from_prefixing(self, inp)
    def _get_object_subtree(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
```

### okami/simulation/robosuite/models/objects/primitive/ball.py

```
class BallObject(PrimitiveObject)
    """A ball (sphere) object.

Args:
    size (1-tuple of float): (radius) size parameters for this ball object"""
    def __init__(self, name, size, size_max, size_min, density, friction, rgba, solref, solimp, material, joints, obj_type, duplicate_collision_geoms)
    def sanity_check(self)
    def _get_object_subtree(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
```

### okami/simulation/robosuite/models/objects/primitive/box.py

```
class BoxObject(PrimitiveObject)
    """A box object.

Args:
    size (3-tuple of float): (half-x, half-y, half-z) size parameters for this box object"""
    def __init__(self, name, size, size_max, size_min, density, friction, rgba, solref, solimp, material, joints, obj_type, duplicate_collision_geoms)
    def sanity_check(self)
    def _get_object_subtree(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
```

### okami/simulation/robosuite/models/objects/primitive/capsule.py

```
class CapsuleObject(PrimitiveObject)
    """A capsule object.

Args:
    size (2-tuple of float): (radius, half-length) size parameters for this capsule object"""
    def __init__(self, name, size, size_max, size_min, density, friction, rgba, solref, solimp, material, joints, obj_type, duplicate_collision_geoms)
    def sanity_check(self)
    def _get_object_subtree(self)
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
```

### okami/simulation/robosuite/models/objects/primitive/cylinder.py

```
class CylinderObject(PrimitiveObject)
    """A cylinder object.

Args:
    size (2-tuple of float): (radius, half-length) size parameters for this cylinder object"""
    def __init__(self, name, size, size_max, size_min, density, friction, rgba, solref, solimp, material, joints, obj_type, duplicate_collision_geoms)
    def sanity_check(self)
    def _get_object_subtree(self)
    def get_collision_attrib_template()
    def bottom_offset(self)
    def top_offset(self)
    def horizontal_radius(self)
    def get_bounding_box_half_size(self)
```

### okami/simulation/robosuite/models/objects/simple/simple_bottle.py

```
class SimpleBottle(CylinderObject)
    def __init__(self, name, size, rgba)
```

### okami/simulation/robosuite/models/objects/xml_objects.py

```
class BottleObject(MujocoXMLObject)
    """Bottle object"""
    def __init__(self, name)
class BowlObject(MujocoXMLObject)
    """Bowl object"""
    def __init__(self, name)
class CanObject(MujocoXMLObject)
    """Coke can object (used in PickPlace)"""
    def __init__(self, name)
class LemonObject(MujocoXMLObject)
    """Lemon object"""
    def __init__(self, name)
class MilkObject(MujocoXMLObject)
    """Milk carton object (used in PickPlace)"""
    def __init__(self, name)
class ShortCabinetObject(MujocoXMLObject)
    """Short cabinet object (used in HumanoidDrawer)"""
    def __init__(self, name)
class WhiteStorageBoxObject(MujocoXMLObject)
    """Short cabinet object (used in HumanoidIce)"""
    def __init__(self, name)
class WoodenCabinetObject(MujocoXMLObject)
    """Wooden cabinet object (used in HumanoidDrawer)"""
    def __init__(self, name)
class BreadObject(MujocoXMLObject)
    """Bread loaf object (used in PickPlace)"""
    def __init__(self, name)
class CerealObject(MujocoXMLObject)
    """Cereal box object (used in PickPlace)"""
    def __init__(self, name)
class SquareNutObject(MujocoXMLObject)
    """Square nut object (used in NutAssembly)"""
    def __init__(self, name)
    def important_sites(self)
class RoundNutObject(MujocoXMLObject)
    """Round nut (used in NutAssembly)"""
    def __init__(self, name)
    def important_sites(self)
class MilkVisualObject(MujocoXMLObject)
    """Visual fiducial of milk carton (used in PickPlace).

Fiducial objects are not involved in collision physics.
They provide a point of reference to indicate a position."""
    def __init__(self, name)
class BreadVisualObject(MujocoXMLObject)
    """Visual fiducial of bread loaf (used in PickPlace)

Fiducial objects are not involved in collision physics.
They provide a point of reference to indicate a position."""
    def __init__(self, name)
class CerealVisualObject(MujocoXMLObject)
    """Visual fiducial of cereal box (used in PickPlace)

Fiducial objects are not involved in collision physics.
They provide a point of reference to indicate a position."""
    def __init__(self, name)
class CanVisualObject(MujocoXMLObject)
    """Visual fiducial of coke can (used in PickPlace)

Fiducial objects are not involved in collision physics.
They provide a point of reference to indicate a position."""
    def __init__(self, name)
class PlateWithHoleObject(MujocoXMLObject)
    """Square plate with a hole in the center (used in PegInHole)"""
    def __init__(self, name)
class DoorObject(MujocoXMLObject)
    """Door with handle (used in Door)

Args:
    friction (3-tuple of float): friction parameters to override the ones specified in the XML
    damping (float): damping parameter to override the ones specified in the XML
    lock (bool): Whether to use the locked door variation object or not"""
    def __init__(self, name, friction, damping, lock)
    def _set_door_friction(self, friction)
    def _set_door_damping(self, damping)
    def important_sites(self)
```

### okami/simulation/robosuite/models/robots/compositional.py

```
class PandaMobile(Panda)
    """Variant of Panda robot with mobile base. Currently serves as placeholder class."""
    def default_base(self)
    def default_arms(self)
class VX300SMobile(VX300S)
    """Variant of VX300S robot with mobile base. Currently serves as placeholder class."""
    def default_base(self)
    def default_arms(self)
class B1Z1(Z1)
    """Variant of VX300S robot with mobile base. Currently serves as placeholder class."""
    def default_base(self)
    def default_arms(self)
    def base_xpos_offset(self)
class B1Z1Floating(B1Z1)
    """Variant of VX300S robot with mobile base. Currently serves as placeholder class."""
    def default_base(self)
class SpotArm(BDArm)
    def default_base(self)
    def default_arms(self)
class SpotArmFloating(SpotArm)
    def default_base(self)
    def default_arms(self)
```

### okami/simulation/robosuite/models/robots/manipulators/aloha_robot.py

```
class Aloha(ManipulatorModel)
    """Baxter is a hunky bimanual robot designed by Rethink Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
```

### okami/simulation/robosuite/models/robots/manipulators/baxter_robot.py

```
class Baxter(ManipulatorModel)
    """Baxter is a hunky bimanual robot designed by Rethink Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
```

### okami/simulation/robosuite/models/robots/manipulators/bd_arm.py

```
class BDArm(ManipulatorModel)
    """Spot Arm is a single-arm robot for mouting on the spot robot.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/g1_robot.py

```
class G1(LeggedManipulatorModel)
    """G1 is a humanoid robot developed by Unitree.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
class G1FixedLowerBody(G1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
class G1FloatingBody(G1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
    def base_xpos_offset(self)
class G1ArmsOnly(G1)
    def __init__(self, idn)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/robots/manipulators/google_robot.py

```
class GoogleRobot(ManipulatorModel)
    """Panda is a sensitive single-arm robot designed by Franka.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/gr1_robot.py

```
class GR1(LeggedManipulatorModel)
    """Tiago is a mobile manipulator robot created by PAL Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
class GR1FixedLowerBody(GR1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
class GR1FloatingBody(GR1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
    def base_xpos_offset(self)
class GR1ArmsOnly(GR1)
    def __init__(self, idn)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/robots/manipulators/h1_robot.py

```
class H1(LeggedManipulatorModel)
    """Tiago is a mobile manipulator robot created by PAL Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
class H1FixedLowerBody(H1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
class H1FloatingBody(H1)
    def __init__(self, idn)
    def init_qpos(self)
    def default_base(self)
class H1ArmsOnly(H1)
    def __init__(self, idn)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/robots/manipulators/humanoid_model.py

```
class HumanoidModel(RobotModel)
    """Base class for all humanoid models.

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, fname, idn)
    def add_gripper(self, gripper, arm_name)
    def eef_name(self)
    def models(self)
    def _important_sites(self)
    def _eef_name(self)
    def default_gripper(self)
    def arm_type(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def default_mount(self)
    def default_controller_config(self)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/robots/manipulators/humanoid_upperbody_model.py

```
class HumanoidUpperBodyModel(RobotModel)
    """Base class for all humanoid upper models (base can be any, bimanual upper body of humanoids).

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, fname, idn)
    def add_gripper(self, gripper, arm_name)
    def eef_name(self)
    def models(self)
    def _important_sites(self)
    def _eef_name(self)
    def default_gripper(self)
    def arm_type(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def default_mount(self)
    def default_controller_config(self)
    def init_qpos(self)
```

### okami/simulation/robosuite/models/robots/manipulators/iiwa_robot.py

```
class IIWA(ManipulatorModel)
    """IIWA is a bright and spunky robot created by KUKA

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/jaco_robot.py

```
class Jaco(ManipulatorModel)
    """Jaco is a kind and assistive robot created by Kinova

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/kinova3_robot.py

```
class Kinova3(ManipulatorModel)
    """The Gen3 robot is the sparkly newest addition to the Kinova line

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/legged_manipulator_model.py

```
class LeggedManipulatorModel(ManipulatorModel)
    """Base class for all manipulator models (robot arm(s) with gripper(s)).

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, fname, idn)
    def _remove_joint_actuation(self, part_name)
    def _remove_free_joint(self)
    def legs_joints(self)
```

### okami/simulation/robosuite/models/robots/manipulators/manipulator_model.py

```
class ManipulatorModel(RobotModel)
    """Base class for all manipulator models (robot arm(s) with gripper(s)).

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, fname, idn)
    def add_gripper(self, gripper, arm_name)
    def update_joints(self)
    def update_actuators(self)
    def eef_name(self)
    def models(self)
    def _important_sites(self)
    def _eef_name(self)
    def default_gripper(self)
    def arm_type(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def default_base(self)
    def default_controller_config(self)
    def init_qpos(self)
    def arm_actuators(self)
    def base_actuators(self)
    def torso_actuators(self)
    def head_actuators(self)
    def legs_actuators(self)
    def arm_joints(self)
    def base_joints(self)
    def torso_joints(self)
    def head_joints(self)
    def legs_joints(self)
```

### okami/simulation/robosuite/models/robots/manipulators/panda_robot.py

```
class Panda(ManipulatorModel)
    """Panda is a sensitive single-arm robot designed by Franka.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
class PandaMobile(Panda)
    """Variant of Panda robot with mobile base. Currently serves as placeholder class."""
    def default_base(self)
```

### okami/simulation/robosuite/models/robots/manipulators/sawyer_robot.py

```
class Sawyer(ManipulatorModel)
    """Sawyer is a witty single-arm robot designed by Rethink Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/tiago_robot.py

```
class Tiago(ManipulatorModel)
    """Tiago is a mobile manipulator robot created by PAL Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
```

### okami/simulation/robosuite/models/robots/manipulators/ur5e_robot.py

```
class UR5e(ManipulatorModel)
    """UR5e is a sleek and elegant new robot created by Universal Robots

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/manipulators/vx300s_robot.py

```
class VX300S(ManipulatorModel)
    """Baxter is a hunky bimanual robot designed by Rethink Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
```

### okami/simulation/robosuite/models/robots/manipulators/yumi_robot.py

```
class Yumi(ManipulatorModel)
    """Yummi is a bimanual robot designed by ABB Robotics.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
    def _eef_name(self)
```

### okami/simulation/robosuite/models/robots/manipulators/z1_robot.py

```
class Z1(ManipulatorModel)
    """Panda is a sensitive single-arm robot designed by Franka.

Args:
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, idn)
    def default_base(self)
    def default_gripper(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def arm_type(self)
```

### okami/simulation/robosuite/models/robots/robot_model.py

```
def register_robot(target_class)
def create_robot(robot_name)
class RobotModelMeta(type)
    """Metaclass for registering robot arms"""
    def __new__(meta, name, bases, class_dict)
class RobotModel(MujocoXMLModel)
    """Base class for all robot models.

Args:
    fname (str): Path to relevant xml file from which to create this robot instance
    idn (int or str): Number or some other unique identification string for this robot instance"""
    def __init__(self, fname, idn)
    def set_base_xpos(self, pos)
    def set_base_ori(self, rot)
    def set_joint_attribute(self, attrib, values, force)
    def add_base(self, base)
    def add_mount(self, mount)
    def add_mobile_base(self, mobile_base)
    def add_leg_base(self, leg_base)
    def naming_prefix(self)
    def dof(self)
    def bottom_offset(self)
    def horizontal_radius(self)
    def models(self)
    def contact_geom_rgba(self)
    def default_base(self)
    def default_controller_config(self)
    def init_qpos(self)
    def base_xpos_offset(self)
    def top_offset(self)
    def _horizontal_radius(self)
    def _important_sites(self)
    def _important_geoms(self)
    def _important_sensors(self)
    def all_joints(self)
    def all_actuators(self)
```

### okami/simulation/robosuite/models/tasks/manipulation_task.py

```
class ManipulationTask(Task)
    """A manipulation-specific task. This is currently a future-proofing placeholder."""
```

### okami/simulation/robosuite/models/tasks/task.py

```
class Task(MujocoWorldBase)
    """Creates MJCF model for a task performed.

A task consists of one or more robots interacting with a variable number of
objects. This class combines the robot(s), the arena, and the objects
into a single MJCF model.

Args:
    mujoco_arena (Arena): MJCF model of robot workspace

    mujoco_robots (Rob"""
    def __init__(self, mujoco_arena, mujoco_robots, mujoco_objects)
    def merge_robot(self, mujoco_robot)
    def merge_arena(self, mujoco_arena)
    def merge_objects(self, mujoco_objects)
    def generate_id_mappings(self, sim)
    def geom_ids_to_instances(self)
    def site_ids_to_instances(self)
    def instances_to_ids(self)
    def geom_ids_to_classes(self)
    def site_ids_to_classes(self)
    def classes_to_ids(self)
```

### okami/simulation/robosuite/models/world.py

```
class MujocoWorldBase(MujocoXML)
    """Base class to inherit all mujoco worlds from."""
    def __init__(self)
```

### okami/simulation/robosuite/renderers/base.py

```
"""This file contains the base renderer class for Mujoco environments."""
def load_renderer_config(renderer)
class Renderer()
    """Base class for all robosuite renderers
Defines basic interface for all renderers to adhere to"""
    def __init__(self, env, renderer_type)
    def __str__(self)
    def render(self)
    def update(self)
    def close(self)
    def reset(self)
    def get_pixel_obs(self)
```

### okami/simulation/robosuite/renderers/base_parser.py

```
class BaseParser(object)
    """Base class for Parser objects used by renderers."""
    def __init__(self, renderer, env)
    def parse_textures(self)
    def parse_materials(self)
    def parse_cameras(self)
    def parse_meshes(self)
    def parse_geometries(self)
```

### okami/simulation/robosuite/renderers/context/egl_context.py

```
def create_initialized_egl_device_display(device_id)
class EGLGLContext()
    """An EGL context for headless accelerated OpenGL rendering on GPU devices."""
    def __init__(self, max_width, max_height, device_id)
    def make_current(self)
    def free(self)
    def __del__(self)
```

### okami/simulation/robosuite/renderers/context/glfw_context.py

```
"""An OpenGL context created via GLFW."""
class GLFWGLContext(GLContext)
    """An OpenGL context created via GLFW."""
    def __init__(self, max_width, max_height, device_id)
```

### okami/simulation/robosuite/renderers/context/osmesa_context.py

```
"""An OSMesa context for software-based OpenGL rendering."""
class OSMesaGLContext(GLContext)
    """An OSMesa context for software-based OpenGL rendering."""
    def __init__(self, max_width, max_height, device_id)
```

### okami/simulation/robosuite/renderers/mjviewer/mjviewer_renderer.py

```
class MjviewerRenderer()
    def __init__(self, env, camera_id, cam_config)
    def render(self)
    def set_camera(self, camera_id)
    def update(self)
    def reset(self)
    def close(self)
    def add_keypress_callback(self, keypress_callback)
```

### okami/simulation/robosuite/renderers/nvisii/nvisii_renderer.py

```
class NVISIIRenderer(Renderer)
    def __init__(self, env, img_path, width, height, spp, use_noise, debug_mode, video_mode, video_path, video_name, video_fps, verbose, vision_modalities)
    def _init_nvisii_components(self)
    def _init_lighting(self)
    def _init_floor(self, image)
    def _init_walls(self, image)
    def _init_camera(self)
    def _camera_configuration(self, at_vec, up_vec, eye_vec, quat)
    def set_camera_pos_quat(self, pos, quat)
    def _get_orientation_geom(self, name)
    def _load(self)
    def update(self)
    def _update_orientation(self, name, component)
    def tag_in_name(self, name)
    def render(self, render_type)
    def render_to_file(self, img_file)
    def render_segmentation_data(self, img_file)
    def render_data_to_file(self, img_file)
    def randomize_colors(self, N, bright)
    def segmentation_to_rgb(self, seg_im, random_colors)
    def reset(self)
    def get_pixel_obs(self)
    def close(self)
```

### okami/simulation/robosuite/renderers/nvisii/nvisii_utils.py

```
def load_object(geom, geom_name, geom_type, geom_quat, geom_pos, geom_size, geom_scale, geom_rgba, geom_tex_name, geom_tex_file, class_id, meshes)
```

### okami/simulation/robosuite/renderers/nvisii/parser.py

```
class Parser(BaseParser)
    def __init__(self, renderer, env, segmentation_type)
    def parse_textures(self)
    def parse_materials(self)
    def parse_meshes(self)
    def parse_geometries(self)
    def create_class_mapping(self)
    def get_class_id(self, geom_index, element_id)
    def tag_in_name(self, name, tags)
```

### okami/simulation/robosuite/robots/fixed_base_robot.py

```
class FixedBaseRobot(Robot)
    """Initializes a robot with a fixed base."""
    def __init__(self, robot_type, idn, controller_config, composite_controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def setup_observables(self)
    def _create_arm_sensors(self, arm, modality)
    def action_limits(self)
    def is_mobile(self)
    def _action_split_indexes(self)
    def controller(self)
```

### okami/simulation/robosuite/robots/legacy/bimanual.py

```
class Bimanual(Manipulator)
    """Initializes a bimanual robot simulation object.

Args:
    robot_type (str): Specification for specific robot arm to be instantiated within this env (e.g: "Panda")

    idn (int or str): Unique ID of this robot. Should be different from others

    controller_config (dict or list of dict --> dict of"""
    def __init__(self, robot_type, idn, controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq)
    def _load_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def _visualize_grippers(self, visible)
    def setup_observables(self)
    def _create_arm_sensors(self, arm, modality)
    def _input2dict(self, inp)
    def arms(self)
    def action_limits(self)
    def ee_ft_integral(self)
    def ee_force(self)
    def ee_torque(self)
    def _hand_pose(self)
    def _hand_quat(self)
    def _hand_total_velocity(self)
    def _hand_pos(self)
    def _hand_orn(self)
    def _hand_vel(self)
    def _hand_ang_vel(self)
    def _action_split_idx(self)
    def _joint_split_idx(self)
```

### okami/simulation/robosuite/robots/legacy/manipulator.py

```
class Manipulator(Robot)
    """Initializes a manipulator robot simulation object, as defined by a single corresponding robot arm XML and
associated gripper XML"""
    def _load_controller(self)
    def control(self, action, policy_step)
    def grip_action(self, gripper, gripper_action)
    def visualize(self, vis_settings)
    def _visualize_grippers(self, visible)
    def action_limits(self)
    def dof(self)
    def is_mobile(self)
    def ee_ft_integral(self)
    def ee_force(self)
    def ee_torque(self)
    def _hand_pose(self)
    def _hand_quat(self)
    def _hand_total_velocity(self)
    def _hand_pos(self)
    def _hand_orn(self)
    def _hand_vel(self)
    def _hand_ang_vel(self)
```

### okami/simulation/robosuite/robots/legacy/robot.py

```
class Robot(object)
    """Initializes a robot simulation object, as defined by a single corresponding robot XML

Args:
    robot_type (str): Specification for specific robot arm to be instantiated within this env (e.g: "Panda")

    idn (int or str): Unique ID of this robot. Should be different from others

    initial_qpos """
    def __init__(self, robot_type, idn, initial_qpos, initialization_noise, mount_type, control_freq)
    def _load_controller(self)
    def load_model(self)
    def reset_sim(self, sim)
    def reset(self, deterministic)
    def setup_references(self)
    def setup_observables(self)
    def control(self, action, policy_step)
    def check_q_limits(self)
    def visualize(self, vis_settings)
    def action_limits(self)
    def torque_limits(self)
    def action_dim(self)
    def dof(self)
    def pose_in_base_from_name(self, name)
    def set_robot_joint_positions(self, jpos)
    def js_energy(self)
    def _joint_positions(self)
    def _joint_velocities(self)
    def joint_indexes(self)
    def get_sensor_measurement(self, sensor_name)
```

### okami/simulation/robosuite/robots/legacy/single_arm.py

```
class SingleArm(Manipulator)
    """Initializes a single-armed robot simulation object.

Args:
    robot_type (str): Specification for specific robot arm to be instantiated within this env (e.g: "Panda")

    idn (int or str): Unique ID of this robot. Should be different from others

    controller_config (dict): If set, contains rele"""
    def __init__(self, robot_type, idn, controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def _visualize_grippers(self, visible)
    def setup_observables(self)
    def action_limits(self)
    def ee_ft_integral(self)
    def ee_force(self)
    def ee_torque(self)
    def _hand_pose(self)
    def _hand_quat(self)
    def _hand_total_velocity(self)
    def _hand_pos(self)
    def _hand_orn(self)
    def _hand_vel(self)
    def _hand_ang_vel(self)
```

### okami/simulation/robosuite/robots/legged_robot.py

```
class LeggedRobot(MobileBaseRobot)
    """Initializes a robot with a wheeled base."""
    def __init__(self, robot_type, idn, controller_config, composite_controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_leg_controllers(self)
    def _load_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def setup_observables(self)
    def _create_arm_sensors(self, arm, modality)
    def action_limits(self)
    def is_legs_actuated(self)
    def num_leg_joints(self)
```

### okami/simulation/robosuite/robots/mobile_base_robot.py

```
class MobileBaseRobot(Robot)
    """Initializes a robot with a fixed base."""
    def __init__(self, robot_type, idn, controller_config, composite_controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_controller(self)
    def _load_base_controller(self)
    def _load_torso_controller(self)
    def _load_head_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def setup_observables(self)
    def enable_parts(self, right, left, torso, head, base, legs)
    def is_mobile(self)
    def base(self)
    def torso(self)
    def head(self)
    def legs(self)
    def _action_split_indexes(self)
    def controller(self)
```

### okami/simulation/robosuite/robots/mobile_manipulator.py

```
class MobileManipulator(Manipulator)
    """Variant of Manipualtor with mobile base support. Currently serves as placeholder class."""
    def is_mobile(self)
```

### okami/simulation/robosuite/robots/robot.py

```
class Robot(object)
    """Initializes a robot simulation object, as defined by a single corresponding robot XML

Args:
    robot_type (str): Specification for specific robot arm to be instantiated within this env (e.g: "Panda")

    idn (int or str): Unique ID of this robot. Should be different from others

    initial_qpos """
    def __init__(self, robot_type, idn, controller_config, composite_controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_controller(self)
    def load_model(self)
    def reset_sim(self, sim)
    def reset(self, deterministic)
    def setup_references(self)
    def setup_observables(self)
    def control(self, action, policy_step)
    def check_q_limits(self)
    def is_mobile(self)
    def action_limits(self)
    def _input2dict(self, inp)
    def torque_limits(self)
    def action_dim(self)
    def dof(self)
    def pose_in_base_from_name(self, name)
    def set_robot_joint_positions(self, jpos)
    def js_energy(self)
    def _joint_positions(self)
    def _joint_velocities(self)
    def joint_indexes(self)
    def arm_joint_indexes(self)
    def get_sensor_measurement(self, sensor_name)
    def visualize(self, vis_settings)
    def _visualize_grippers(self, visible)
    def action_limits(self)
    def dof(self)
    def is_mobile(self)
    def ee_ft_integral(self)
    def ee_force(self)
    def ee_torque(self)
    def _hand_pose(self)
    def _hand_quat(self)
    def _hand_total_velocity(self)
    def _hand_pos(self)
    def _hand_orn(self)
    def _hand_vel(self)
    def _hand_ang_vel(self)
    def _load_arm_controllers(self)
    def enable_parts(self, right, left)
    def enabled(self, part_name)
    def create_action_vector(self, action_dict)
    def print_action_info(self)
    def print_action_info_dict(self)
    def get_gripper_name(self, arm)
    def _joint_split_idx(self)
```

### okami/simulation/robosuite/robots/wheeled_robot.py

```
class WheeledRobot(MobileBaseRobot)
    """Initializes a robot with a wheeled base."""
    def __init__(self, robot_type, idn, controller_config, composite_controller_config, initial_qpos, initialization_noise, base_type, gripper_type, control_freq, lite_physics)
    def _load_controller(self)
    def load_model(self)
    def reset(self, deterministic)
    def setup_references(self)
    def control(self, action, policy_step)
    def setup_observables(self)
    def _create_arm_sensors(self, arm, modality)
    def action_limits(self)
```

### okami/simulation/robosuite/scripts_test/print_pkl.py

```
def explore_structure(data, indent)
def print_structure_from_pkl(file_path)
```

### okami/simulation/robosuite/scripts_test/test_camera.py

```
"""A script to test camera streaming."""
```

### okami/simulation/robosuite/scripts_test/test_camera_streaming.py

```
"""A script to test camera streaming."""
```

### okami/simulation/robosuite/scripts_test/test_joint_position_controller.py

```
"""A script to test joint position controller for GR1FloatingBody."""
def gripper_joint_pos_controller(obs, desired_qpos, kp, damping_ratio)
def joint_pos_controller(obs, target_joint_pos)
```

### okami/simulation/robosuite/scripts_test/test_moma.py

```
"""A script to collect a batch of human demonstrations.

The demonstrations can be played back using the `playback_demonstrations_from_hdf5.py` script."""
```

### okami/simulation/robosuite/scripts_test/test_se3_interpolate.py

```
def slerp(rot1, rot2, t)
def interpolate_se3(pose1, pose2, t)
```

### okami/simulation/robosuite/scripts_test/test_urdf_joint_order.py

```
def parse_urdf(file_path)
```

### okami/simulation/robosuite/utils/binding_utils.py

```
"""Useful classes for supporting DeepMind MuJoCo binding."""
class MjRenderContext()
    """Class that encapsulates rendering functionality for a
MuJoCo simulation.

See https://github.com/openai/mujoco-py/blob/4830435a169c1f3e3b5f9b58a7c3d9c39bdf4acb/mujoco_py/mjrendercontext.pyx"""
    def __init__(self, sim, offscreen, device_id, max_width, max_height)
    def _set_mujoco_context_and_buffers(self)
    def update_offscreen_size(self, width, height)
    def upload_texture(self, tex_id)
    def render(self, width, height, camera_id, segmentation)
    def read_pixels(self, width, height, depth, segmentation)
    def upload_texture(self, tex_id)
    def __del__(self)
class MjRenderContextOffscreen(MjRenderContext)
    def __init__(self, sim, device_id, max_width, max_height)
class MjSimState()
    """A mujoco simulation state."""
    def __init__(self, time, qpos, qvel)
    def from_flattened(cls, array, sim)
    def flatten(self)
class _MjModelMeta(type)
    """Metaclass which allows MjModel below to delegate to mujoco.MjModel.

Taken from dm_control: https://github.com/deepmind/dm_control/blob/main/dm_control/mujoco/wrapper/core.py#L244"""
    def __new__(cls, name, bases, dct)
class MjModel()
    """Wrapper class for a MuJoCo 'mjModel' instance.
MjModel encapsulates features of the model that are expected to remain
constant. It also contains simulation and visualization options which may be
changed occasionally, although this is done explicitly by the user."""
    def __init__(self, model_ptr)
    def from_xml_path(cls, xml_path)
    def __del__(self)
    def _extract_mj_names(self, name_adr, num_obj, obj_type)
    def make_mappings(self)
    def body_id2name(self, id)
    def body_name2id(self, name)
    def joint_id2name(self, id)
    def joint_name2id(self, name)
    def geom_id2name(self, id)
    def geom_name2id(self, name)
    def site_id2name(self, id)
    def site_name2id(self, name)
    def light_id2name(self, id)
    def light_name2id(self, name)
    def camera_id2name(self, id)
    def camera_name2id(self, name)
    def actuator_id2name(self, id)
    def actuator_name2id(self, name)
    def sensor_id2name(self, id)
    def sensor_name2id(self, name)
    def tendon_id2name(self, id)
    def tendon_name2id(self, name)
    def mesh_id2name(self, id)
    def mesh_name2id(self, name)
    def get_xml(self)
    def get_joint_qpos_addr(self, name)
    def get_joint_qvel_addr(self, name)
class _MjDataMeta(type)
    """Metaclass which allows MjData below to delegate to mujoco.MjData.

Taken from dm_control."""
    def __new__(cls, name, bases, dct)
class MjData()
    """Wrapper class for a MuJoCo 'mjData' instance.
MjData contains all of the dynamic variables and intermediate results produced
by the simulation. These are expected to change on each simulation timestep.
The properties without docstrings are defined in mujoco source code from https://github.com/deepmi"""
    def __init__(self, model)
    def model(self)
    def __del__(self)
    def body_xpos(self)
    def body_xquat(self)
    def body_xmat(self)
    def get_body_xpos(self, name)
    def get_body_xquat(self, name)
    def get_body_xmat(self, name)
    def get_body_jacp(self, name)
    def get_body_jacr(self, name)
    def get_body_xvelp(self, name)
    def get_body_xvelr(self, name)
    def get_geom_xpos(self, name)
    def get_geom_xmat(self, name)
    def get_geom_jacp(self, name)
    def get_geom_jacr(self, name)
    def get_geom_xvelp(self, name)
    def get_geom_xvelr(self, name)
    def get_site_xpos(self, name)
    def get_site_xmat(self, name)
    def get_site_jacp(self, name)
    def get_site_jacr(self, name)
    def get_site_xvelp(self, name)
    def get_site_xvelr(self, name)
    def get_camera_xpos(self, name)
    def get_camera_xmat(self, name)
    def get_light_xpos(self, name)
    def get_light_xdir(self, name)
    def get_sensor(self, name)
    def get_mocap_pos(self, name)
    def set_mocap_pos(self, name, value)
    def get_mocap_quat(self, name)
    def set_mocap_quat(self, name, value)
    def get_joint_qpos(self, name)
    def set_joint_qpos(self, name, value)
    def get_joint_qvel(self, name)
    def set_joint_qvel(self, name, value)
class MjSim()
    """Meant to somewhat replicate functionality in mujoco-py's MjSim object
(see https://github.com/openai/mujoco-py/blob/master/mujoco_py/mjsim.pyx)."""
    def __init__(self, model)
    def from_xml_string(cls, xml)
    def from_xml_file(cls, xml_file)
    def reset(self)
    def forward(self)
    def step(self, with_udd)
    def step1(self)
    def step2(self)
    def render(self, width, height)
    def add_render_context(self, render_context)
    def get_state(self)
    def set_state(self, value)
    def set_state_from_flattened(self, value)
    def free(self)
```

### okami/simulation/robosuite/utils/buffers.py

```
"""Collection of Buffer objects with general functionality"""
class Buffer(object)
    """Abstract class for different kinds of data buffers. Minimum API should have a "push" and "clear" method"""
    def push(self, value)
    def clear(self)
class RingBuffer(Buffer)
    """Simple RingBuffer object to hold values to average (useful for, e.g.: filtering D component in PID control)

Note that the buffer object is a 2D numpy array, where each row corresponds to
individual entries into the buffer

Args:
    dim (int): Size of entries being added. This is, e.g.: the size of"""
    def __init__(self, dim, length)
    def push(self, value)
    def clear(self)
    def current(self)
    def average(self)
class DeltaBuffer(Buffer)
    """Simple 2-length buffer object to streamline grabbing delta values between "current" and "last" values

Constructs delta object.

Args:
    dim (int): Size of numerical arrays being inputted
    init_value (None or Iterable): Initial value to fill "last" value with initially.
        If None (default"""
    def __init__(self, dim, init_value)
    def push(self, value)
    def clear(self)
    def delta(self, abs_value)
    def average(self)
class DelayBuffer(RingBuffer)
    """Modified RingBuffer that returns delayed values when polled"""
    def get_delayed_value(self, delay)
```

### okami/simulation/robosuite/utils/camera_utils.py

```
"""This module includes:

- Utility classes for modifying sim cameras

- Utility functions for performing common camera operations such as retrieving
camera matrices and transforming from world to camera frame or vice-versa."""
def get_camera_intrinsic_matrix(sim, camera_name, camera_height, camera_width)
def get_camera_extrinsic_matrix(sim, camera_name)
def get_camera_transform_matrix(sim, camera_name, camera_height, camera_width)
def get_camera_segmentation(sim, camera_name, camera_height, camera_width)
def get_real_depth_map(sim, depth_map)
def project_points_from_world_to_camera(points, world_to_camera_transform, camera_height, camera_width)
def transform_from_pixels_to_world(pixels, depth_map, camera_to_world_transform)
def bilinear_interpolate(im, x, y)
class CameraMover()
    """A class for manipulating a camera.

WARNING: This class will initially RE-INITIALIZE the environment.

Args:
    env (MujocoEnv): Mujoco environment to modify camera
    camera (str): Which camera to mobilize during playback, e.g.: frontview, agentview, etc.
    init_camera_pos (None or 3-array): If"""
    def __init__(self, env, camera, init_camera_pos, init_camera_quat)
    def set_camera_pose(self, pos, quat)
    def get_camera_pose(self)
    def modify_xml_for_camera_movement(self, xml, camera_name)
    def rotate_camera(self, point, axis, angle)
    def move_camera(self, direction, scale)
class DemoPlaybackCameraMover(CameraMover)
    """A class for playing back demonstrations and recording the resulting frames with the flexibility of a mobile camera
that can be set manually or panned automatically frame-by-frame

Note: domain randomization is also supported for playback!

Args:
    demo (str): absolute fpath to .hdf5 demo
    env_c"""
    def __init__(self, demo, env_config, replay_from_actions, visualize_sites, camera, init_camera_pos, init_camera_quat, use_dr, dr_args)
    def load_episode_xml(self, demo_num)
    def grab_next_frame(self)
    def grab_episode_frames(self, demo_num, pan_point, pan_axis, pan_rate)
```

### okami/simulation/robosuite/utils/control_utils.py

```
def nullspace_torques(mass_matrix, nullspace_matrix, initial_joint, joint_pos, joint_vel, joint_kp)
def opspace_matrices(mass_matrix, J_full, J_pos, J_ori)
def orientation_error(desired, current)
def set_goal_position(delta, current_position, position_limit, set_pos)
def set_goal_orientation(delta, current_orientation, orientation_limit, set_ori)
```

### okami/simulation/robosuite/utils/errors.py

```
class robosuiteError(Exception)
    """Base class for exceptions in robosuite."""
class XMLError(robosuiteError)
    """Exception raised for errors related to xml."""
class SimulationError(robosuiteError)
    """Exception raised for errors during runtime."""
class RandomizationError(robosuiteError)
    """Exception raised for really really bad RNG."""
```

### okami/simulation/robosuite/utils/input_utils.py

```
"""Utility functions for grabbing user inputs"""
def choose_environment()
def choose_controller()
def choose_multi_arm_config()
def choose_robots(exclude_bimanual, use_humanoids)
def input2action(device, robot, active_arm, env_configuration, mirror_actions)
```

### okami/simulation/robosuite/utils/log_utils.py

```
"""This file contains utility classes and functions for logging to stdout and stderr
Adapted from robomimic: https://github.com/ARISE-Initiative/robomimic/blob/master/robomimic/utils/log_utils.py"""
class FileFormatter(Formatter)
    """Formatter class of logging for file logging."""
    def format(self, record)
class ConsoleFormatter(Formatter)
    """Formatter class of logging for console logging."""
    def format(self, record)
class DefaultLogger()
    """Default logger class in robosuite codebase."""
    def __init__(self, logger_name, console_logging_level, file_logging_level)
    def get_logger(self)
```

### okami/simulation/robosuite/utils/mjcf_utils.py

```
class CustomMaterial(object)
    """Simple class to instantiate the necessary parameters to define an appropriate texture / material combo

Instantiates a nested dict holding necessary components for procedurally generating a texture / material combo

Please see http://www.mujoco.org/book/XMLreference.html#asset for specific details o"""
    def __init__(self, texture, tex_name, mat_name, tex_attrib, mat_attrib, shared)
def xml_path_completion(xml_path, root)
def array_to_string(array)
def string_to_array(string)
def convert_to_string(inp)
def set_alpha(node, alpha)
def new_element(tag, name)
def new_joint(name)
def new_actuator(name, joint, act_type)
def new_site(name, rgba, pos, size)
def new_geom(name, type, size, pos, group)
def new_body(name, pos)
def new_inertial(pos, mass)
def get_size(size, size_max, size_min, default_max, default_min)
def add_to_dict(dic, fill_in_defaults, default_value)
def add_prefix(root, prefix, tags, attribs, exclude)
def add_material(root, naming_prefix, custom_material)
def recolor_collision_geoms(root, rgba, exclude)
def _element_filter(element, parent)
def sort_elements(root, parent, element_filter, _elements_dict)
def find_parent(root, child)
def find_elements(root, tags, attribs, return_first)
def find_elements_by_substring(root, tags, substrings, attribs, return_first)
def find_parent(element, target)
def save_sim_model(sim, fname)
def get_ids(sim, elements, element_type, inplace)
```

### okami/simulation/robosuite/utils/mjmod.py

```
"""Modder classes used for domain randomization. Largely based off of the mujoco-py
implementation below.

https://github.com/openai/mujoco-py/blob/1fe312b09ae7365f0dd9d4d0e453f8da59fae0bf/mujoco_py/modder.py"""
class BaseModder()
    """Base class meant to modify simulation attributes mid-sim.

Using @random_state ensures that sampling here won't be affected
by sampling that happens outside of the modders.

Args:
    sim (MjSim): simulation object

    random_state (RandomState): instance of np.random.RandomState, specific
        """
    def __init__(self, sim, random_state)
    def update_sim(self, sim)
    def model(self)
class LightingModder(BaseModder)
    """Modder to modify lighting within a Mujoco simulation.

Args:
    sim (MjSim): MjSim object

    random_state (RandomState): instance of np.random.RandomState

    light_names (None or list of str): list of lights to use for randomization. If not provided, all
        lights in the model are randomiz"""
    def __init__(self, sim, random_state, light_names, randomize_position, randomize_direction, randomize_specular, randomize_ambient, randomize_diffuse, randomize_active, position_perturbation_size, direction_perturbation_size, specular_perturbation_size, ambient_perturbation_size, diffuse_perturbation_size)
    def save_defaults(self)
    def restore_defaults(self)
    def randomize(self)
    def _randomize_position(self, name)
    def _randomize_direction(self, name)
    def _randomize_specular(self, name)
    def _randomize_ambient(self, name)
    def _randomize_diffuse(self, name)
    def _randomize_active(self, name)
    def get_pos(self, name)
    def set_pos(self, name, value)
    def get_dir(self, name)
    def set_dir(self, name, value)
    def get_active(self, name)
    def set_active(self, name, value)
    def get_specular(self, name)
    def set_specular(self, name, value)
    def get_ambient(self, name)
    def set_ambient(self, name, value)
    def get_diffuse(self, name)
    def set_diffuse(self, name, value)
    def get_lightid(self, name)
class CameraModder(BaseModder)
    """Modder for modifying camera attributes in mujoco sim

Args:
    sim (MjSim): MjSim object

    random_state (None or RandomState): instance of np.random.RandomState

    camera_names (None or list of str): list of camera names to use for randomization. If not provided,
        all cameras are used f"""
    def __init__(self, sim, random_state, camera_names, randomize_position, randomize_rotation, randomize_fovy, position_perturbation_size, rotation_perturbation_size, fovy_perturbation_size)
    def save_defaults(self)
    def restore_defaults(self)
    def randomize(self)
    def _randomize_position(self, name)
    def _randomize_rotation(self, name)
    def _randomize_fovy(self, name)
    def get_fovy(self, name)
    def set_fovy(self, name, value)
    def get_quat(self, name)
    def set_quat(self, name, value)
    def get_pos(self, name)
    def set_pos(self, name, value)
    def get_camid(self, name)
class TextureModder(BaseModder)
    """Modify textures in model. Example use:
    sim = MjSim(...)
    modder = TextureModder(sim)
    modder.whiten_materials()  # ensures materials won't impact colors
    modder.set_checker('some_geom', (255, 0, 0), (0, 0, 0))
    modder.rand_all('another_geom')

Note: in order for the textures to take """
    def __init__(self, sim, random_state, geom_names, randomize_local, randomize_material, local_rgb_interpolation, local_material_interpolation, texture_variations, randomize_skybox)
    def save_defaults(self)
    def restore_defaults(self)
    def randomize(self)
    def _randomize_geom_color(self, name)
    def _randomize_texture(self, name)
    def _randomize_material(self, name)
    def rand_checker(self, name)
    def rand_gradient(self, name)
    def rand_rgb(self, name)
    def rand_noise(self, name)
    def whiten_materials(self)
    def get_geom_rgb(self, name)
    def set_geom_rgb(self, name, rgb)
    def get_rand_rgb(self, n)
    def get_texture(self, name)
    def set_texture(self, name, bitmap, perturb)
    def get_material(self, name)
    def set_material(self, name, material, perturb)
    def get_checker_matrices(self, name)
    def set_checker(self, name, rgb1, rgb2, perturb)
    def set_gradient(self, name, rgb1, rgb2, vertical, perturb)
    def set_rgb(self, name, rgb, perturb)
    def set_noise(self, name, rgb1, rgb2, fraction, perturb)
    def upload_texture(self, name, device_id)
    def _check_geom_for_texture(self, name)
    def _name_to_tex_id(self, name)
    def _name_to_mat_id(self, name)
    def _cache_checker_matrices(self)
    def _make_checker_matrices(self, h, w)
class Texture()
    """Helper class for operating on the MuJoCo textures.

Args:
    model (MjModel): Mujoco sim model
    tex_id (int): id of specific texture in mujoco sim"""
    def __init__(self, model, tex_id)
    def bitmap(self)
class DynamicsModder(BaseModder)
    """Modder for various dynamics properties of the mujoco model, such as friction, damping, etc.
This can be used to modify parameters stored in MjModel (ie friction, damping, etc.) as
well as optimizer parameters stored in PyMjOption (i.e.: medium density, viscosity, etc.)
To modify a parameter, use the"""
    def __init__(self, sim, random_state, randomize_density, randomize_viscosity, density_perturbation_ratio, viscosity_perturbation_ratio, body_names, randomize_position, randomize_quaternion, randomize_inertia, randomize_mass, position_perturbation_size, quaternion_perturbation_size, inertia_perturbation_ratio, mass_perturbation_ratio, geom_names, randomize_friction, randomize_solref, randomize_solimp, friction_perturbation_ratio, solref_perturbation_ratio, solimp_perturbation_ratio, joint_names, randomize_stiffness, randomize_frictionloss, randomize_damping, randomize_armature, stiffness_perturbation_ratio, frictionloss_perturbation_size, damping_perturbation_size, armature_perturbation_size)
    def save_defaults(self)
    def restore_defaults(self)
    def randomize(self)
    def update_sim(self, sim)
    def update(self)
    def mod(self, name, attr, val)
    def mod_density(self, name, val)
    def mod_viscosity(self, name, val)
    def mod_position(self, name, val)
    def mod_quaternion(self, name, val)
    def mod_inertia(self, name, val)
    def mod_mass(self, name, val)
    def mod_friction(self, name, val)
    def mod_solref(self, name, val)
    def mod_solimp(self, name, val)
    def mod_stiffness(self, name, val)
    def mod_frictionloss(self, name, val)
    def mod_damping(self, name, val)
    def mod_armature(self, name, val)
    def dynamics_parameters(self)
    def opt(self)
```

### okami/simulation/robosuite/utils/numba.py

```
"""Numba utils."""
def jit_decorator(func)
```

### okami/simulation/robosuite/utils/observables.py

```
def sensor(modality)
def create_deterministic_corrupter(corruption, low, high)
def create_uniform_noise_corrupter(min_noise, max_noise, low, high)
def create_gaussian_noise_corrupter(mean, std, low, high)
def create_deterministic_delayer(delay)
def create_uniform_sampled_delayer(min_delay, max_delay)
def create_gaussian_sampled_delayer(mean, std)
class Observable()
    """Base class for all observables -- defines interface for interacting with sensors

Args:
    name (str): Name for this observable
    sensor (function with `sensor` decorator): Method to grab raw sensor data for this observable. Should take in a
        single dict argument (observation cache if a pr"""
    def __init__(self, name, sensor, corrupter, filter, delayer, sampling_rate, enabled, active)
    def update(self, timestep, obs_cache, force)
    def reset(self)
    def is_enabled(self)
    def is_active(self)
    def set_enabled(self, enabled)
    def set_active(self, active)
    def set_sensor(self, sensor)
    def set_corrupter(self, corrupter)
    def set_filter(self, filter)
    def set_delayer(self, delayer)
    def set_sampling_rate(self, rate)
    def _check_sensor_validity(self)
    def obs(self)
    def modality(self)
```

### okami/simulation/robosuite/utils/okami_utils.py

```
def gripper_joint_pos_controller_xml(obs, desired_qpos)
def joint_pos_controller(obs, target_joint_pos)
def urdf_to_robosuite_cmds(urdf_q)
def obs_to_urdf(obs)
def dex_mapping(q)
```

### okami/simulation/robosuite/utils/opencv_renderer.py

```
"""opencv renderer class."""
class OpenCVRenderer()
    def __init__(self, sim)
    def set_camera(self, camera_id)
    def render(self)
    def add_keypress_callback(self, keypress_callback)
    def close(self)
```

### okami/simulation/robosuite/utils/placement_samplers.py

```
class ObjectPositionSampler()
    """Base class of object placement sampler.

Args:
    name (str): Name of this sampler.

    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models

    ensure_object_boundary_in_range (bool): If True, will ensure that the object is enclosed within a g"""
    def __init__(self, name, mujoco_objects, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def add_objects(self, mujoco_objects)
    def reset(self)
    def sample(self, fixtures, reference, on_top)
class UniformRandomSampler(ObjectPositionSampler)
    """Places all objects within the table uniformly random.

Args:
    name (str): Name of this sampler.

    mujoco_objects (None or MujocoObject or list of MujocoObject): single model or list of MJCF object models

    x_range (2-array of float): Specify the (min, max) relative x_range used to uniformly"""
    def __init__(self, name, mujoco_objects, x_range, y_range, rotation, rotation_axis, ensure_object_boundary_in_range, ensure_valid_placement, reference_pos, z_offset)
    def _sample_x(self, object_horizontal_radius)
    def _sample_y(self, object_horizontal_radius)
    def _sample_quat(self)
    def sample(self, fixtures, reference, on_top)
class SequentialCompositeSampler(ObjectPositionSampler)
    """Samples position for each object sequentially. Allows chaining
multiple placement initializers together - so that object locations can
be sampled on top of other objects or relative to other object placements.

Args:
    name (str): Name of this sampler."""
    def __init__(self, name)
    def append_sampler(self, sampler, sample_args)
    def hide(self, mujoco_objects)
    def add_objects(self, mujoco_objects)
    def add_objects_to_sampler(self, sampler_name, mujoco_objects)
    def reset(self)
    def sample(self, fixtures, reference, on_top)
```

### okami/simulation/robosuite/utils/robot_utils.py

```
def check_bimanual(robot_name)
```

### okami/simulation/robosuite/utils/sim_utils.py

```
"""Collection of useful simulation utilities"""
def check_contact(sim, geoms_1, geoms_2)
def get_contacts(sim, model)
```

### okami/simulation/robosuite/utils/traj_utils.py

```
class Interpolator(object)
    """General interpolator interface."""
    def get_interpolated_goal(self)
class LinearInterpolator(Interpolator)
    """Simple class for implementing a linear interpolator.

Abstracted to interpolate n-dimensions

Args:
    ndim (int): Number of dimensions to interpolate

    controller_freq (float): Frequency (Hz) of the controller

    policy_freq (float): Frequency (Hz) of the policy model

    ramp_ratio (float):"""
    def __init__(self, ndim, controller_freq, policy_freq, ramp_ratio, use_delta_goal, ori_interpolate)
    def set_states(self, dim, ori)
    def set_goal(self, goal)
    def get_interpolated_goal(self)
```

### okami/simulation/robosuite/utils/transform_utils.py

```
"""Utility functions of matrix and vector transformations.

NOTE: convention for quaternions is (x, y, z, w)"""
def convert_quat(q, to)
def quat_multiply(quaternion1, quaternion0)
def quat_conjugate(quaternion)
def quat_inverse(quaternion)
def quat_distance(quaternion1, quaternion0)
def quat_slerp(quat0, quat1, fraction, shortestpath)
def random_quat(rand)
def random_axis_angle(angle_limit, random_state)
def vec(values)
def mat4(array)
def mat2pose(hmat)
def mat2quat(rmat)
def euler2mat(euler)
def mat2euler(rmat, axes)
def pose2mat(pose)
def quat2mat(quaternion)
def quat2axisangle(quat)
def axisangle2quat(vec)
def pose_in_A_to_pose_in_B(pose_A, pose_A_in_B)
def pose_inv(pose)
def _skew_symmetric_translation(pos_A_in_B)
def vel_in_A_to_vel_in_B(vel_A, ang_vel_A, pose_A_in_B)
def force_in_A_to_force_in_B(force_A, torque_A, pose_A_in_B)
def rotation_matrix(angle, direction, point)
def clip_translation(dpos, limit)
def clip_rotation(quat, limit)
def make_pose(translation, rotation)
def unit_vector(data, axis, out)
def get_orientation_error(target_orn, current_orn)
def get_pose_error(target_pose, current_pose)
def matrix_inverse(matrix)
def rotate_2d_point(input, rot)
```

### okami/simulation/robosuite/wrappers/data_collection_wrapper.py

```
"""This file implements a wrapper for saving simulation states to disk.
This data collection wrapper is useful for collecting demonstrations."""
class DataCollectionWrapper(Wrapper)
    def __init__(self, env, directory, collect_freq, flush_freq)
    def _start_new_episode(self)
    def _on_first_interaction(self)
    def _flush(self)
    def reset(self)
    def step(self, action)
    def close(self)
```

### okami/simulation/robosuite/wrappers/demo_sampler_wrapper.py

```
"""This file contains a wrapper for sampling environment states
from a set of demonstrations on every reset. The main use case is for 
altering the start state distribution of training episodes for 
learning RL policies."""
class DemoSamplerWrapper(Wrapper)
    """Initializes a wrapper that provides support for resetting the environment
state to one from a demonstration. It also supports curriculums for
altering how often to sample from demonstration vs. sampling a reset
state from the environment.

Args:
    env (MujocoEnv): The environment to wrap.

    dem"""
    def __init__(self, env, demo_path, need_xml, num_traj, sampling_schemes, scheme_ratios, open_loop_increment_freq, open_loop_initial_window_width, open_loop_window_increment)
    def reset(self)
    def sample(self)
    def _random_sample(self)
    def _uniform_sample(self)
    def _reverse_sample_open_loop(self)
    def _forward_sample_open_loop(self)
    def _xml_for_episode_index(self, ep_ind)
```

### okami/simulation/robosuite/wrappers/domain_randomization_wrapper.py

```
"""This file implements a wrapper for facilitating domain randomization over
robosuite environments."""
class DomainRandomizationWrapper(Wrapper)
    """Wrapper that allows for domain randomization mid-simulation.

Args:
    env (MujocoEnv): The environment to wrap.

    seed (int): Integer used to seed all randomizations from this wrapper. It is
        used to create a np.random.RandomState instance to make sure samples here
        are isolated f"""
    def __init__(self, env, seed, randomize_color, randomize_camera, randomize_lighting, randomize_dynamics, color_randomization_args, camera_randomization_args, lighting_randomization_args, dynamics_randomization_args, randomize_on_reset, randomize_every_n_steps)
    def reset(self)
    def step(self, action)
    def step_randomization(self)
    def randomize_domain(self)
    def save_default_domain(self)
    def restore_default_domain(self)
```

### okami/simulation/robosuite/wrappers/gym_wrapper.py

```
"""This file implements a wrapper for facilitating compatibility with OpenAI gym.
This is useful when using these environments with code that assumes a gym-like
interface."""
class GymWrapper(Wrapper, Env)
    def __init__(self, env, keys)
    def _flatten_obs(self, obs_dict, verbose)
    def reset(self, seed, options)
    def step(self, action)
    def compute_reward(self, achieved_goal, desired_goal, info)

```python
def compute_reward(self, achieved_goal, desired_goal, info):
        """
        Dummy function to be compatible with gym interface that simply returns environment reward

        Args:
            achieved_goal: [NOT USED]
            desired_goal: [NOT USED]
            info: [NOT USED]

        Returns:
            float: environment reward
        """
        # Dummy args used to mimic Wrapper interface
        return self.env.reward()
```
```

### okami/simulation/robosuite/wrappers/visualization_wrapper.py

```
"""This file implements a wrapper for visualizing important sites in a given environment.

By default, this visualizes all sites possible for the environment. Visualization options
for a given environment can be found by calling `get_visualization_settings()`, and can
be set individually by calling `set_visualization_setting(setting, visible)`."""
class VisualizationWrapper(Wrapper)
    def __init__(self, env, indicator_configs)
    def get_indicator_names(self)
    def set_indicator_pos(self, indicator, pos)
    def get_visualization_settings(self)
    def set_visualization_setting(self, setting, visible)
    def reset(self)
    def step(self, action)
    def _add_indicators_to_model(self, xml)
```

### okami/simulation/robosuite/wrappers/wrapper.py

```
"""This file contains the base wrapper class for Mujoco environments.
Wrappers are useful for data collection and logging. Highly recommended."""
class Wrapper()
    """Base class for all wrappers in robosuite.

Args:
    env (MujocoEnv): The environment to wrap."""
    def __init__(self, env)
    def class_name(cls)
    def _warn_double_wrap(self)
    def step(self, action)
    def reset(self)
    def render(self)
    def observation_spec(self)
    def action_spec(self)
    def action_dim(self)
    def unwrapped(self)
    def __getattr__(self, attr)

```python
def observation_spec(self):
        """
        By default, grabs the normal environment observation_spec

        Returns:
            OrderedDict: Observations from the environment
        """
        return self.env.observation_spec()
```
```

### okami/slahmr_hands/slahmr/body_model/body_model.py

```
class BodyModel(Module)
    """Wrapper around SMPLX body model class."""
    def __init__(self, bm_path, num_betas, num_pca_comps, batch_size, num_expressions, use_vtx_selector, model_type, kid_template_path)
    def forward(self, root_orient, pose_body, pose_hand, pose_jaw, pose_eye, betas, trans, dmpls, expression, return_dict)
```

### okami/slahmr_hands/slahmr/body_model/specs.py

```
def smpl_to_openpose(model_type, use_hands, use_face, use_face_contour, openpose_format)
```

### okami/slahmr_hands/slahmr/body_model/utils.py

```
def run_smpl(body_model, trans, root_orient, body_pose, betas, hand_pose)
def zero_pad_tensors(pad_list, pad_size)
```

### okami/slahmr_hands/slahmr/eval/associate.py

```
def associate_phalp_track_dirs(phalp_dir, img_dir, track_ids, gt_kps, start, end, debug)
def associate_phalp_track_data(phalp_file, track_ids, gt_kps, start, end, debug)
def associate_keypoints(gt_kps, track_kps, debug)
def associate_frame_dict(frame_data, gt_kps, track_ids, debug)
def compute_iou(bb1, bb2)
```

### okami/slahmr_hands/slahmr/eval/egobody_utils.py

```
def get_sequence_body_info(seq_name)
def get_egobody_split(split)
def get_egobody_seq_paths(seq_name, start, end)
def get_egobody_seq_names(seq_name, start, end)
def get_egobody_img_dir(seq_name)
def get_egobody_keypoints(seq_name, start, end)
def load_egobody_smpl_params(seq_name, start, end)
def load_egobody_intrinsics(seq_name, start, end, ret_size_tuple)
def load_egobody_gt_extrinsics(seq_name, start, end, ret_4d)
def load_egobody_extrinsics(seq_name, use_intrins, start, end)
def load_egobody_meshes(seq_name, device, start, end)
def load_egobody_kinect2holo(seq_name, ret_4d)
```

### okami/slahmr_hands/slahmr/eval/run_eval.py

```
def stack_torch(x_list, dim)
def load_3dpw_params(seq_name, start, end)
def load_egobody_params(seq_name, start, end)
def eval_result_dir(dset_type, res_dir, out_path, joint_reg, dev_id, overwrite, debug)
def parse_job_file(args)
def main(args)
```

### okami/slahmr_hands/slahmr/eval/split_3dpw.py

```
def load_split_sequences(split)
def select_phalp_tracks(seq_name, split, start, end, debug)
```

### okami/slahmr_hands/slahmr/eval/split_egobody.py

```
def load_split_sequences(split)
def get_egobody_keypoints(img_dir, start, end)
def select_phalp_tracks(seq_name, img_dir, start, end, debug)
```

### okami/slahmr_hands/slahmr/eval/tools.py

```
class JointRegressor(object)
    def __init__(self)
    def to(self, device)
    def __call__(self, verts)
def compute_accel_norm(joints)
def global_align_joints(gt_joints, pred_joints)
def first_align_joints(gt_joints, pred_joints)
def local_align_joints(gt_joints, pred_joints)
def load_body_model(batch_size, model_type, gender, device)
def run_smpl(body_model)
def run_smpl_batch(body_model, device)
def cat_dicts(dict_list, dim)
def load_results_all(phase_dir, device)
```

### okami/slahmr_hands/slahmr/geometry/camera.py

```
def perspective_projection(points, focal_length, camera_center, rotation, translation)
def reproject(points3d, cam_R, cam_t, cam_f, cam_center)
def focal2fov(focal, R)
def fov2focal(fov, R)
def compute_lookat_box(bb_min, bb_max, intrins)
def lookat_origin(cam_dist, view_angle)
def lookat_matrix(source_pos, target_pos, up)
def normalize(x)
def invert_camera(R, t)
def compose_cameras(R1, t1, R2, t2)
def matmul_nd(A, x)
def view_matrix(z, up, pos)
def average_pose(poses)
def project_so3(M, eps)
def make_translation(t)
def make_rotation(rx, ry, rz, order)
def make_4x4_pose(R, t)
def normalize(x)
def rotx(theta)
def roty(theta)
def rotz(theta)
def relative_pose_c2w(Rwc1, Rwc2, twc1, twc2)
def relative_pose_w2c(Rc1w, Rc2w, tc1w, tc2w)
def project(xyz_c, center, focal, eps)
def convert_yup(xyz)
def inv_project(uv, z, center, focal, yup)
```

### okami/slahmr_hands/slahmr/geometry/mesh.py

```
def get_mesh_bb(mesh)
def get_scene_bb(meshes)
def make_batch_mesh(verts, faces, colors)
def make_mesh(verts, faces, colors, yup)
def save_mesh_scenes(out_dir, scenes)
def save_scenes_to_glb(out_dir, scenes)
def save_meshes_to_glb(path, meshes, names)
def save_meshes_to_obj(out_dir, meshes, names)
```

### okami/slahmr_hands/slahmr/geometry/pcl.py

```
def read_pcl_tensor(path)
def align_pcl(Y, X, weight, fixed_scale)
```

### okami/slahmr_hands/slahmr/geometry/plane.py

```
def fit_plane(points)
def get_plane_transform(up, ground_plane, xyz_orig)
def parse_floor_plane(floor_plane)
def compute_plane_intersection(point, direction, plane)
def bdot(A1, A2, keepdim)
```

### okami/slahmr_hands/slahmr/geometry/rotation.py

```
def batch_rodrigues(rot_vecs, epsilon, dtype)
def quaternion_mul(q0, q1)
def quaternion_inverse(q, eps)
def quaternion_slerp(t, q0, q1, eps)
def rotation_matrix_to_angle_axis(rotation_matrix)
def quaternion_to_angle_axis(quaternion)
def angle_axis_to_rotation_matrix(angle_axis)
def quaternion_to_rotation_matrix(quaternion)
def angle_axis_to_quaternion(angle_axis)
def rotation_matrix_to_quaternion(rotation_matrix, eps)
```

### okami/slahmr_hands/slahmr/humor/amass_utils.py

```
"""Taken from https://github.com/davrempe/humor"""
def data_name_list(return_config)
def data_dim(dname, rot_rep_size)
```

### okami/slahmr_hands/slahmr/humor/humor_model.py

```
"""Taken from https://github.com/davrempe/humor"""
def step(model, loss_func, data, dataset, device, cur_epoch, mode, use_gt_p)
class HumorModel(Module)
    def __init__(self, in_rot_rep, out_rot_rep, latent_size, steps_in, conditional_prior, output_delta, posterior_arch, decoder_arch, prior_arch, model_data_config, detach_sched_samp, model_use_smpl_joint_inputs, model_smpl_batch_size)
    def prepare_input(self, data_in, device, data_out, return_input_dict, return_global_dict)
    def split_output(self, decoder_out, convert_rots)
    def forward(self, x_past, x_t)
    def single_step(self, past_in, t_in)
    def prior(self, past_in)
    def posterior(self, past_in, t_in)
    def rsample(self, mu, var)
    def decode(self, z, past_in)
    def scheduled_sampling(self, x_past, x_t, init_input_dict, p, gender, betas, need_global_out)
    def apply_world2local_trans(self, world2local_trans, world2local_rot, trans2joint, input_dict, output_dict, invert)
    def zero_pad_tensors(self, pad_list, pad_size)
    def roll_out(self, x_past, init_input_dict, num_steps, use_mean, z_seq, return_prior, gender, betas, return_z, canonicalize_input, uncanonicalize_output)
    def sample_step(self, past_in, t_in, use_mean, z, return_prior, return_z)
    def infer_global_seq(self, global_seq, full_forward_pass)
    def infer(self, x_past, x_t)
    def infer_step(self, past_in, t_in)
class MLP(Module)
    def __init__(self, layers, nonlinearity, use_gn, skip_input_idx)
    def forward(self, x)
```

### okami/slahmr_hands/slahmr/humor/transforms.py

```
"""Taken from https://github.com/davrempe/humor"""
def compute_aligned_from_right(body_right)
def compute_world2aligned_mat(rot_pos)
def compute_world2aligned_joints_mat(joints)
def convert_to_rotmat(pred_rot, rep)
def matrot2axisangle(matrots)
def axisangle2matrots(axisangle)
def make_rot_homog(rotation_matrix)
def skew(v)
def batch_rodrigues(rot_vecs, epsilon, dtype)
def quat2mat(quat)
def rot6d_to_rotmat(x)
def rot9d_to_rotmat(x)
def rotation_matrix_to_angle_axis(rotation_matrix)
def rotation_matrix_to_quaternion(rotation_matrix, eps)
def quaternion_to_angle_axis(quaternion)
```