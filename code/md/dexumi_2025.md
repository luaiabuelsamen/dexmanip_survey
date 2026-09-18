# dexumi_2025

source: https://github.com/real-stanford/DexUMI


commit: acddb8f8a89a8f0186868bbec44306eb7808114a


## README

<h1 align="center" style="font-size: 3em;">Universal Manipulation Interface for<br>Dexterous Manipulation</h1>

<p align="center"><b style="color: red; font-size: 1.5em;">CoRL 2025 Best Paper Finalist</b></p>

[[Project page]](https://dex-umi.github.io)
[[Paper]](https://arxiv.org/pdf/2505.21864v2)
[[Hardware Guide]](https://dex-umi.github.io/tutorial/hardware.html)
[[Deployment Guide]](https://dex-umi.github.io/tutorial/deployment.html)

<img width="90%" src="assets/Teaser.png">

[Mengda Xu](https://mengdaxu.github.io/)<sup>\*,1,2,3</sup>,
[Han Zhang](https://doublehan07.github.io/)<sup>\*,1</sup>,
[Yifan Hou](https://yifan-hou.github.io/)<sup>1</sup>,
[Zhenjia Xu](https://www.zhenjiaxu.com/)<sup>5</sup>,
[Linxi Fan](https://jimfan.me/)<sup>5</sup>,
[Manuela Veloso](https://www.cs.cmu.edu/~mmv/)<sup>3,4</sup>,
[Shuran Song](https://shurans.github.io/)<sup>1,2</sup>

<sup>1</sup>Stanford University,
<sup>2</sup>Columbia University,
<sup>3</sup>J.P. Morgan AI Research,
<sup>4</sup>Carnegie Mellon University,
<sup>5</sup>NVIDIA

<sup>\*</sup>Indicates Equal Contribution
## 🚀 Installation

Tested on Ubuntu 22.04. 
We recommend Miniforge for faster installation:

```bash
cd DexUMI
mamba env create -f environment.yml
mamba activate dexumi 
```

DexUMI utilizes [SAM2](https://github.com/facebookresearch/sam2) and [ProPainter](https://github.com/sczhou/ProPainter) to track and remove the exoskeleton and hand. Our system uses [Record3D](https://github.com/marek-simonik/record3d) to track the wrist pose. To make Record3D compatible with Python 3.10, please follow the instructions [here](https://github.com/marek-simonik/record3d/issues/89). Alternatively, you can directly install our [forked version](https://github.com/mengdaxu/record3d), which already integrates the solution. Please clone the above three packages into the same directory as DexUMI. The final folder structure should be:

```bash
.
├── DexUMI
├── sam2
├── ProPainter
├── record3D
```

Download the SAM2 checkpoint `sam2.1_hiera_large.pt` into `sam2/checkpoints/`. 

You also need to install Record3D on your iPhone. We use iPhone 15 Pro Max to track the wrist pose. You can use any iPhone model with ARKit capability, but you might need to modify some CAD models to adapt to other iPhone dimensions.

## 🦾 Real-world Deployment

### 🛠️ Build Exoskeleton 

Please check our hardware guide to download the CAD model and assembly tutorial for both Inspire Hand and XHand exoskeletons.
<table>
<tr>
<td align="center">
  <h4>XHand Exoskeleton</h4>
  <img src="assets/xhand.gif" alt="XHand Exoskeleton" width="375">
</td>
<td align="center">
  <h4>Inspire Hand Exoskeleton</h4>
  <img src="assets/inspire.gif" alt="Inspire Hand Exoskeleton" width="375">
</td>
</tr>
</table>


### 📷 Data Recording and Processing

Please check the data recording and processing tutorial before data collection. 

Record data with the exoskeletons:
```bash
python DexUMI/real_script/data_collection/record_exoskeleton.py -et -ef --fps 45 --reference-dir /path/to/reference_folder --hand_type xhand/inspire --data-dir /path/to/data
```

If you do not have a force sensor installed, simply omit the `-ef` flag.

The data will be stored in `/path/to/data`. Each episode structure should be:
```bash
└── episode_0
   ├── camera_0
   ├── camera_0.mp4
   ├── camera_1
   ├── camera_1.mp4
   ├── numeric_0
   ├── numeric_1
   ├── numeric_2
   └── numeric_3
```

After collecting the dataset, modify the following parameters in `real_script/data_generation_pipeline/process.sh`:
```bash
DATA_DIR="path/to/data" 
TARGET_DIR="path/to/data_replay"
REFERENCE_DIR="/path/to/reference_folder"
```

If you do not have a force sensor installed, remove the `--enable-fsr` flag on line 19 from the command. 

Then run:
```bash
./process.sh
```

The scripts will replay the exoskeleton hand actions on the dexterous hand and record the corresponding videos.

The replay data will be stored in `path/to/data_replay`. Each episode structure should be: 
```bash
├── dex_camera_0.mp4
├── exo_camera_0.mp4
├── fsr_values_interp_1
├── fsr_values_interp_2
├── fsr_values_interp_3
├── hand_motor_value
├── joint_angles_interp
├── pose_interp
└── valid_indices
```

After replay is complete, modify the `config/render/render_all_dataset.yaml` to update:
```bash
data_buffer_path: path/to/data_replay
reference_dir: /path/to/reference_folder
```

Then start dataset generation, which converts exoskeleton data into robot hand data:
```bash
python DexUMI/real_script/data_generation_pipeline/render_all_dataset.py
```

We provide some sample data [here](https://real.stanford.edu/dexumi/sample_data.zip) such that you can test the data generation pipeline. 

The generated data will be stored in `path/to/data_replay`. Each episode structure should be:
```bash
├── combined.mp4
├── debug_combined.mp4
├── dex_camera_0.mp4
├── dex_finger_seg_mask
├── dex_img
├── dex_seg_mask
├── dex_thumb_seg_mask
├── exo_camera_0.mp4
├── exo_finger_seg_mask
├── exo_img
├── exo_seg_mask
├── exo_thumb_seg_mask
├── fsr_values_interp
├── fsr_values_interp_1
├── fsr_values_interp_2
├── fsr_values_interp_3
├── hand_motor_value
├── inpainted
├── joint_angles_interp
├── maskout_baseline.mp4
├── pose_interp
└── valid_indices
```

Finally, run the following command to generate the dataset for policy training:
```bash
python 6_generate_dataset.py -d path/to/data_replay -t path/to/final_dataset --force-process total --force-adjust
```

If you do not have a force sensor installed, you can drop the last two flags.

The final dataset will be stored in `path/to/final_dataset`. Each episode structure should be:
```bash
├── camera_0
├── fsr
├── hand_action
├── pose
└── proprioception
```

All data collected by us can be found [here](https://umi-data.github.io/).

### 🚴‍♂️ Policy Training 

Modify the following items in `config/diffusion_policy/train_diffusion_policy.yaml`:
```yaml
dataset:
   data_dirs: [
      "path/to/final_dataset",
   ]
   enable_fsr: True/False
   fsr_binary_cutoff: [10,10,10] # we use this value for XHand; Inspire Hand cutoff depends on installation
model:
   global_cond_dim: 384+ number of force input
```
Then run:
```bash
accelerate launch DexUMI/real_script/train_diffusion_policy.py
```

### 🏂 Policy Evaluation 

Open the server:
```bash
python DexUMI/real_script/open_server.py --dexhand --ur5
```

Evaluate the policy:
```bash
python DexUMI/real_script/eval_policy/eval_xhand.py --model_path path/to/model --ckpt N # for xhand 
# or 
python DexUMI/real_script/eval_policy/eval_inspire.py --model_path path/to/model --ckpt N # for inspire hand
```

Modify the transformation matrix before conducting evaluation. Please check our tutorial for calibrating the matrix.

## 🧱 Hardware Optimization
For hardware optimiation, please create a new virtual env to avoid package dependency conflicts:
```bash
cd DexUMI
mamba env create -f environment_design.yml
mamba activate dexumi_design 
```
The goal of hardware optimization is to: 1) Find equivalent mechanical structures to replace the target robot hand design to improve wearability, and 2) Use motion capture data to discover the target robot hand mechanical structure (closed-loop kinematics) if such information is unavailable in URDF.

### 📸 Motion Capture Data 

We use a motion capture system to record the fingertip trajectories of all five fingers on the Inspire Hand and store them in `DexUMI/linkage_optimization/hardware_design_data/inspire_mocap`. You can visualize the trajectories by running:

```bash
python DexUMI/linkage_optimization/viz_multi_fingertips_trajectory.py
```

### 🎮 Simulate Linkage Design and corrsponding Fingertip Poses Trajectory

We first start with simulating four bar linkage with different link length and joint position and record the corrpsonding fingertips pose trajectory
```bash
 python DexUMI/linkage_optimization/sweep_valid_linkage_design.py --type finger/thumb ----save_path path/to/store_sim
```

### 🔧 Optimization

We solve an optimization problem to find the best linkage design that matches the target (mocap) fingertip trajectory:

```bash
# For index, middle, ring, and pinky fingers
python DexUMI/linkage_optimization/get_equivalent_finger.py -r path/to/store_sim -b path/to/mocap

# For thumb
python DexUMI/linkage_optimization/get_equivalent_thumb.py -r path/to/store_sim -b path/to/mocap
```

This will output the optimal linkage parameters that best approximate the desired fingertip motion. We provide our optimization results at `DexUMI/linkage_optimization/hardware_design_data/inspire_optimization_results`. We recommend running all scripts on a CPU with multiple cores for faster speed. One future research direction could be to optimize exoskeleton designs more efficiently with generative models. 

You can visualize the optimization results by running:
```bash
python DexUMI/linkage_optimization/viz_full_fk.py
```
### BibTeX
```bibtex
@inproceedings{xu2025dexumi,
  title={DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation},
  author={Xu, Mengda and Zhang, Han and Hou, Yifan and Xu, Zhenjia and Fan, Linxi and Veloso, Manuela and Song, Shuran},
  booktitle={Conference on Robot Learning},
  pages={437--459},
  year={2025},
  organization={PMLR}
}
```
### 🏷️ License
This repository is released under the MIT license. 

### 🙏 Acknowledgement
* Diffusion Policy is adapted from [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)
* Many useful utilies are adapted from [UMI](https://github.com/real-stanford/universal_manipulation_interface)
* Many hardware designs are adapted from [DOGlove](https://do-glove.github.io/)
* Thanks [Huy Ha](https://www.cs.columbia.edu/~huy/) for helping us to setup our [tutorial videos](https://www.youtube.com/playlist?list=PLAymUyzwr8XgxwJzWp1MHkBzKIRJLdRJg) on Youtube. 


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
config/
  diffusion_policy/
    train_diffusion_policy.yaml
  render/
    render_all_dataset.yaml
dexumi/
  camera/
    camera.py
    debug_camera.py
    iphone_camera.py
    oak_camera.py
    qr_code.py
    realsense_camera.py
  common/
    data.py
    diffusion_model/
    distribution.py
    ema_model.py
    frame_manager.py
    imagecodecs_numcodecs.py
    network.py
    pointcloud.py
    precise_sleep.py
    projection.py
    transformer.py
    utility/
    vision_transformer.py
  constants.py
  data_recording/
    __init__.py
    data_buffer.py
    numeric_recorder.py
    record_manager.py
    video_recorder.py
  diffusion_policy/
    dataloader/
    diffusion_policy.py
    model/
    utility/
  encoder/
    UARTReader.py
    encoder.py
    fsr.py
    numeric.py
    xhand_tactile.py
  hand_sdk/
    dexhand.py
    inspire/
    xhand/
  real_env/
    common/
    dexumi_policy.py
    real_policy.py
    ring_buffer.py
    spacemouse.py
embedded_system/
  Core/
    Inc/
    Src/
  DexUMI.ioc
  DexUMI_Embedded_System.md
  Drivers/
    CMSIS/
    STM32F0xx_HAL_Driver/
  Makefile
  STM32F042K6Tx_FLASH.ld
  Users/
    ads1256.c
    ads1256.h
    delay.c
    delay.h
    fsr.c
    fsr.h
  startup_stm32f042x6.s
environment.yml
environment_design.yml
linkage_optimization/
  get_equivalent_finger.py
  get_equivalent_thumb.py
  get_real_fingertips_trajectory.py
  get_sim_fingertips_trajectory.py
  hardware_design_data/
    inspire_mocap/
    inspire_optimization_results/
  inspire_urdf_writer.py
  simple_regression.py
  sweep_valid_linkage_design.py
  viz_full_fk.py
  viz_multi_fingertips_trajectory.py
mocap/
  inspire_mocap.py
  latency_util.py
  mocap_util/
    data_descriptions.py
    mocap_data.py
    mocap_node.py
    natnet_client.py
real_script/
  calibration/
    compute_ur5_iphone_offset.py
    record_ur5_trajectory.py
  camera_calibration/
    display_rolling_time_qr.py
    measure_latency.py
    print_pose_esimation_qr_code.py
  data_collection/
    record_exoskeleton.py
  data_generation_pipeline/
    0_interpolation.py
    1_replay_hand.py
    2_to_jpg.py
    3_segment.py
    4_inpaint_exo.py
    5_compose_video.py
    6_generate_dataset.py
    camera_position.py
    process.sh
    render_all_dataset.py
    render_dataset.py
    replay_exoskeleton_trajectory.py
    viz_pose.py
  eval_policy/
    eval_inspire_hand.py
    eval_xhand.py
  open_server.py
  policy_training/
    train_diffusion_policy.py
  teleoperation/
    calibrate_inspire_mapping.py
    calibrate_xhand_mapping.py
    overlay.py
    teleop_ur5.py
    teleoperation.py
```

## Config files (4)


### config/diffusion_policy/train_diffusion_policy.yaml

```yaml
store_dir: ${oc.env:STORE_PATH}
dev_dir: ${oc.env:DEV_PATH}
hydra:
  run:
    dir: ${dev_dir}/exoskeleton/experiment/dp/${now:%Y-%m-%d_%H-%M-%S}


project_name: DexUMI


debug: False
action_dim: 18

ema:
  _target_: exoskeleton.common.ema_model.EMAModel
  update_after_step: 0
  inv_gamma: 1.0
  power: 0.75
  min_value: 0.0
  max_value: 0.9999

training:
  epochs: 10000
  gradient_accumulation_steps: 1
  batch_size: 300
  num_workers: 4
  shuffle: True
  pin_memory: False
  persistent_workers: True
  drop_last: False
  ckpt_frequency: 100
  resume: False
  model_path: null
  model_ckpt: null
  use_ema: True

noise_scheduler:
  _target_: diffusers.DDIMScheduler
  num_train_timesteps: 50
  beta_start: 0.0001
  beta_end: 0.02
  beta_schedule: squaredcos_cap_v2
  clip_sample: True 
  prediction_type: epsilon 
num_inference_steps: 16

optimizer: 
  _target_: torch.optim.AdamW
  lr: 1e-4
  betas: [0.9, 0.999]
  weight_decay: 1e-2
  eps: 1e-08

lr_scheduler: "cosine"
num_warmup_steps: 500

dataset:
  _target_: exoskeleton.diffusion_policy.dataloader.dexumi_dataset.DexUMIDataset
  data_dirs: [
    "path/to/dataset",
  ]
  load_camera_ids: [0]
  camera_resize_shape: [240,240]
  pred_horizon: 16
  obs_horizon: 1
  action_horizon: 8
  unnormal_list: ["camera_0","pose"]
  optional_transforms: ["Resize","RandomCrop","ColorJitter","RandomGrayscale","GaussianBlur"]
  relative_hand_action: False
  skip_proprioception: True
  enable_fsr: False
  bgr2rgb: True
  max_episode: null
  fsr_binary_cutoff: [10,10,10] #xhand 



model:
  _target_: exoskeleton.diffusion_policy.diffusion_policy.DiffusionPolicy
  vision_backbone_kwargs: 
    model_name: "vit_small_patch8_224.dino"
  freeze_vision_back: False
  diffusion_policy_head:
    _target_: exoskeleton.diffusion_policy.model.diffusion_model.ConditionalUnet1D
    input_dim: ${action_dim}
    global_cond_dim: 384
```

### config/render/render_all_dataset.yaml

```yaml
dev_dir: ${oc.env:DEV_PATH}
hydra:
  run:
    dir: ${dev_dir}/DexUMI/experiment/render/${now:%Y-%m-%d_%H-%M-%S}

avaliable_gpu: [0]
data_buffer_path: /path/to/data_buffer
data_dir: ${data_buffer_path}
reference_dir: /path/to/reference
sam2_checkpoint_path: ${dev_dir}/sam2/checkpoints/sam2.1_hiera_large.pt
save_path: ${data_buffer_path}
resize_ratio: 1.0

start_episode: null
end_episode: null
```

### environment.yml

```yaml
name: dexumi
channels:
  - conda-forge
dependencies:
  - _libgcc_mutex=0.1=conda_forge
  - _openmp_mutex=4.5=2_gnu
  - anyio=4.7.0=pyhd8ed1ab_0
  - aom=3.9.1=hac33072_0
  - argon2-cffi=23.1.0=pyhd8ed1ab_1
  - argon2-cffi-bindings=21.2.0=py310ha75aee5_5
  - arrow=1.3.0=pyhd8ed1ab_1
  - asttokens=3.0.0=pyhd8ed1ab_1
  - async-lru=2.0.4=pyhd8ed1ab_1
  - attrs=24.3.0=pyh71513ae_0
  - babel=2.16.0=pyhd8ed1ab_1
  - beautifulsoup4=4.12.3=pyha770c72_1
  - bleach=6.2.0=pyhd8ed1ab_1
  - brotli-python=1.1.0=py310hf71b8c6_2
  - bzip2=1.0.8=h4bc722e_7
  - ca-certificates=2024.12.14=hbcca054_0
  - cached-property=1.5.2=hd8ed1ab_1
  - cached_property=1.5.2=pyha770c72_1
  - cairo=1.18.2=h3394656_1
  - certifi=2024.12.14=pyhd8ed1ab_0
  - cffi=1.17.1=py310h8deb56e_0
  - charset-normalizer=3.4.0=pyhd8ed1ab_1
  - comm=0.2.2=pyhd8ed1ab_1
  - dav1d=1.2.1=hd590300_0
  - debugpy=1.8.11=py310hf71b8c6_0
  - decorator=5.1.1=pyhd8ed1ab_1
  - defusedxml=0.7.1=pyhd8ed1ab_0
  - entrypoints=0.4=pyhd8ed1ab_1
  - exceptiongroup=1.2.2=pyhd8ed1ab_1
  - executing=2.1.0=pyhd8ed1ab_1
  - font-ttf-dejavu-sans-mono=2.37=hab24e00_0
  - font-ttf-inconsolata=3.000=h77eed37_0
  - font-ttf-source-code-pro=2.038=h77eed37_0
  - font-ttf-ubuntu=0.83=h77eed37_3
  - fontconfig=2.15.0=h7e30c49_1
  - fonts-conda-ecosystem=1=0
  - fonts-conda-forge=1=0
  - fqdn=1.5.1=pyhd8ed1ab_1
  - freetype=2.12.1=h267a509_2
  - fribidi=1.0.10=h36c2ea0_0
  - gdk-pixbuf=2.42.12=hb9ae30d_0
  - gmp=6.3.0=hac33072_2
  - graphite2=1.3.13=h59595ed_1003
  - h11=0.14.0=pyhd8ed1ab_1
  - h2=4.1.0=pyhd8ed1ab_1
  - harfbuzz=10.1.0=h0b3b770_0
  - hpack=4.0.0=pyhd8ed1ab_1
  - httpcore=1.0.7=pyh29332c3_1
  - httpx=0.28.1=pyhd8ed1ab_0
  - hyperframe=6.0.1=pyhd8ed1ab_1
  - icu=75.1=he02047a_0
  - idna=3.10=pyhd8ed1ab_1
  - importlib-metadata=8.5.0=pyha770c72_1
  - importlib_resources=6.4.5=pyhd8ed1ab_1
  - ipykernel=6.29.5=pyh3099207_0
  - ipython=8.31.0=pyh707e725_0
  - isoduration=20.11.0=pyhd8ed1ab_1
  - jedi=0.19.2=pyhd8ed1ab_1
  - jinja2=3.1.5=pyhd8ed1ab_0
  - json5=0.10.0=pyhd8ed1ab_1
  - jsonpointer=3.0.0=py310hff52083_1
  - jsonschema=4.23.0=pyhd8ed1ab_1
  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_1
  - jsonschema-with-format-nongpl=4.23.0=hd8ed1ab_1
  - jupyter-lsp=2.2.5=pyhd8ed1ab_1
  - jupyter_client=8.6.3=pyhd8ed1ab_1
  - jupyter_core=5.7.2=pyh31011fe_1
  - jupyter_events=0.11.0=pyhd8ed1ab_0
  - jupyter_server=2.15.0=pyhd8ed1ab_0
  - jupyter_server_terminals=0.5.3=pyhd8ed1ab_1
  - jupyterlab=4.3.4=pyhd8ed1ab_0
  - jupyterlab_pygments=0.3.0=pyhd8ed1ab_2
  - jupyterlab_server=2.27.3=pyhd8ed1ab_1
  - keyutils=1.6.1=h166bdaf_0
  - krb5=1.21.3=h659f571_0
  - lame=3.100=h166bdaf_1003
  - ld_impl_linux-64=2.43=h712a8e2_2
  - lerc=4.0.0=h27087fc_0
  - libabseil=20240722.0=cxx17_h5888daf_1
  - libass=0.17.3=hba53ac1_1
  - libdeflate=1.23=h4ddbbb0_0
  - libdrm=2.4.124=hb9d3cd8_0
  - libedit=3.1.20191231=he28a2e2_2
  - libegl=1.7.0=ha4b6fd6_2
  - libexpat=2.6.4=h5888daf_0
  - libffi=3.4.2=h7f98852_5
  - libgcc=14.2.0=h77fa898_1
  - libgcc-ng=14.2.0=h69a702a_1
  - libgl=1.7.0=ha4b6fd6_2
  - libglib=2.82.2=h2ff4ddf_0
  - libglvnd=1.7.0=ha4b6fd6_2
  - libglx=1.7.0=ha4b6fd6_2
  - libgomp=14.2.0=h77fa898_1
  - libhwloc=2.11.2=default_h0d58e46_1001
  - libiconv=1.17=hd590300_2
  - libjpeg-turbo=3.0.0=hd590300_1
  - liblzma=5.6.3=hb9d3cd8_1
  - libnsl=2.0.1=hd590300_0
  - libopenvino=2024.5.0=hac27bb2_0
  - libopenvino-auto-batch-plugin=2024.5.0=h4d9b6c2_0
  - libopenvino-auto-plugin=2024.5.0=h4d9b6c2_0
  - libopenvino-hetero-plugin=2024.5.0=h3f63f65_0
  - libopenvino-intel-cpu-plugin=2024.5.0=hac27bb2_0
  - libopenvino-intel-gpu-plugin=2024.5.0=hac27bb2_0
  - libopenvino-intel-npu-plugin=2024.5.0=hac27bb2_0
  - libopenvino-ir-frontend=2024.5.0=h3f63f65_0
  - libopenvino-onnx-frontend=2024.5.0=h5c8f2c3_0
  - libopenvino-paddle-frontend=2024.5.0=h5c8f2c3_0
  - libopenvino-pytorch-frontend=2024.5.0=h5888daf_0
  - libopenvino-tensorflow-frontend=2024.5.0=h6481b9d_0
  - libopenvino-tensorflow-lite-frontend=2024.5.0=h5888daf_0
  - libopus=1.3.1=h7f98852_1
  - libpciaccess=0.18=hd590300_0
  - libpng=1.6.44=hadc24fc_0
  - libprotobuf=5.28.2=h5b01275_0
  - librsvg=2.58.4=h49af25d_2
  - libsodium=1.0.20=h4ab18f5_0
  - libsqlite=3.47.2=hee588c1_0
  - libstdcxx=14.2.0=hc0a3c3a_1
  - libstdcxx-ng=14.2.0=h4852527_1
  - libtiff=4.7.0=hd9ff511_3
  - libuuid=2.38.1=h0b41bf4_0
  - libva=2.22.0=h8a09558_1
  - libvpx=1.14.1=hac33072_0
  - libwebp-base=1.5.0=h851e524_0
  - libxcb=1.17.0=h8a09558_0
  - libxcrypt=4.4.36=hd590300_1
  - libxml2=2.13.5=h8d12d68_1
  - libzlib=1.3.1=hb9d3cd8_2
  - markupsafe=3.0.2=py310h89163eb_1
  - matplotlib-inline=0.1.7=pyhd8ed1ab_1
  - mistune=3.0.2=pyhd8ed1ab_1
  - nbclient=0.10.2=pyhd8ed1ab_0
  - nbconvert-core=7.16.4=pyhff2d567_2
  - nbformat=5.10.4=pyhd8ed1ab_1
  - ncurses=6.5=he02047a_1
  - nest-asyncio=1.6.0=pyhd8ed1ab_1
  - notebook-shim=0.2.4=pyhd8ed1ab_1
  - ocl-icd=2.3.2=hb9d3cd8_2
  - opencl-headers=2024.10.24=h5888daf_0
  - openh264=2.5.0=hf92e6e3_0
  - openssl=3.4.0=hb9d3cd8_0
  - overrides=7.7.0=pyhd8ed1ab_1
  - packaging=24.2=pyhd8ed1ab_2
  - pandocfilters=1.5.0=pyhd8ed1ab_0
  - pango=1.54.0=h861ebed_4
  - parso=0.8.4=pyhd8ed1ab_1
  - pcre2=10.44=hba22ea6_2
  - pexpect=4.9.0=pyhd8ed1ab_1
  - pickleshare=0.7.5=pyhd8ed1ab_1004
  - pip=24.3.1=pyh8b19718_2
  - pixman=0.44.2=h29eaf8c_0
  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_2
  - platformdirs=4.3.6=pyhd8ed1ab_1
  - prometheus_client=0.21.1=pyhd8ed1ab_0
  - prompt-toolkit=3.0.48=pyha770c72_1
  - pthread-stubs=0.4=hb9d3cd8_1002
  - ptyprocess=0.7.0=pyhd8ed1ab_1
  - pugixml=1.14=h59595ed_0
  - pure_eval=0.2.3=pyhd8ed1ab_1
  - pycparser=2.22=pyh29332c3_1
  - pygments=2.18.0=pyhd8ed1ab_1
  - pysocks=1.7.1=pyha55dd90_7
  - python=3.10.16=he725a3c_1_cpython
  - python-dateutil=2.9.0.post0=pyhff2d567_1
  - python-fastjsonschema=2.21.1=pyhd8ed1ab_0
  - python-json-logger=2.0.7=pyhd8ed1ab_0
  - python_abi=3.10=5_cp310
  - pytz=2024.2=pyhd8ed1ab_1
  - pyyaml=6.0.2=py310ha75aee5_1
  - pyzmq=26.2.0=py310h71f11fc_3
  - readline=8.2=h8228510_1
  - referencing=0.35.1=pyhd8ed1ab_1
  - requests=2.32.3=pyhd8ed1ab_1
  - rfc3339-validator=0.1.4=pyhd8ed1ab_1
  - rfc3986-validator=0.1.1=pyh9f0ad1d_0
  - rpds-py=0.22.3=py310h505e2c1_0
  - send2trash=1.8.3=pyh0d859eb_1
  - setuptools=75.6.0=pyhff2d567_1
  - six=1.17.0=pyhd8ed1ab_0
  - snappy=1.2.1=h8bd8927_1
  - sniffio=1.3.1=pyhd8ed1ab_1
  - soupsieve=2.5=pyhd8ed1ab_1
  - stack_data=0.6.3=pyhd8ed1ab_1
  - svt-av1=2.3.0=h5888daf_0
  - tbb=2022.0.0=hceb3a55_0
  - terminado=0.18.1=pyh0d859eb_0
  - tinycss2=1.4.0=pyhd8ed1ab_0
  - tk=8.6.13=noxft_h4845f30_101
  - tomli=2.2.1=pyhd8ed1ab_1
  - tornado=6.4.2=py310ha75aee5_0
  - traitlets=5.14.3=pyhd8ed1ab_1
  - types-python-dateutil=2.9.0.20241206=pyhd8ed1ab_0
  - typing-extensions=4.12.2=hd8ed1ab_1
  - typing_extensions=4.12.2=pyha770c72_1
  - typing_utils=0.1.0=pyhd8ed1ab_1
  - tzdata=2024b=hc8b5060_0
  - uri-template=1.3.0=pyhd8ed1ab_1
  - urllib3=2.3.0=pyhd8ed1ab_0
  - wayland=1.23.1=h3e06ad9_0
  - wayland-protocols=1.37=hd8ed1ab_0
  - wcwidth=0.2.13=pyhd8ed1ab_1
  - webcolors=24.11.1=pyhd8ed1ab_0
  - webencodings=0.5.1=pyhd8ed1ab_3
  - websocket-client=1.8.0=pyhd8ed1ab_1
  - wheel=0.45.1=pyhd8ed1ab_1
  - x264=1!164.3095=h166bdaf_2
  - x265=3.5=h924138e_3
  - xorg-libice=1.1.2=hb9d3cd8_0
  - xorg-libsm=1.2.5=he73a12e_0
  - xorg-libx11=1.8.10=h4f16b4b_1
  - xorg-libxau=1.0.12=hb9d3cd8_0
  - xorg-libxdmcp=1.1.5=hb9d3cd8_0
  - xorg-libxext=1.3.6=hb9d3cd8_0
  - xorg-libxfixes=6.0.1=hb9d3cd8_0
  - xorg-libxrender=0.9.12=hb9d3cd8_0
  - yaml=0.2.5=h7f98852_2
  - zeromq=4.3.5=h3b0a872_7
  - zipp=3.21.0=pyhd8ed1ab_1
  - zstandard=0.23.0=py310ha39cb0e_1
  - zstd=1.5.6=ha6fb4c9_0
  - pip:
      - accelerate==1.2.1
      - annotated-types==0.7.0
      - antlr4-python3-runtime==4.9.3
      - asciitree==0.3.3
      - av==14.0.1
      - click==8.1.8
      - contourpy==1.3.1
      - cycler==0.12.1
      - diffusers==0.31.0
      - docker-pycreds==0.4.0
      - einops==0.8.0
      - fasteners==0.19
  
```

### environment_design.yml

```yaml
name: dexumi_design
channels:
  - conda-forge
dependencies:
  - _libgcc_mutex=0.1=conda_forge
  - _openmp_mutex=4.5=2_gnu
  - bzip2=1.0.8=h4bc722e_7
  - ca-certificates=2025.4.26=hbd8a1cb_0
  - ld_impl_linux-64=2.43=h712a8e2_4
  - libblas=3.9.0=31_h59b9bed_openblas
  - libcblas=3.9.0=31_he106b2a_openblas
  - libexpat=2.7.0=h5888daf_0
  - libffi=3.4.6=h2dba641_1
  - libgcc=15.1.0=h767d61c_2
  - libgcc-ng=15.1.0=h69a702a_2
  - libgfortran=15.1.0=h69a702a_2
  - libgfortran5=15.1.0=hcea5267_2
  - libgomp=15.1.0=h767d61c_2
  - liblapack=3.9.0=31_h7ac8fdf_openblas
  - liblzma=5.8.1=hb9d3cd8_1
  - libnsl=2.0.1=hd590300_0
  - libopenblas=0.3.29=pthreads_h94d23a6_0
  - libsqlite=3.49.2=hee588c1_0
  - libstdcxx=15.1.0=h8f9b012_2
  - libuuid=2.38.1=h0b41bf4_0
  - libxcrypt=4.4.36=hd590300_1
  - libzlib=1.3.1=hb9d3cd8_2
  - narwhals=1.41.0=pyhe01879c_0
  - ncurses=6.5=h2d0b736_3
  - numpy=2.2.6=py310hefbff90_0
  - openssl=3.5.0=h7b32b05_1
  - packaging=25.0=pyh29332c3_1
  - pip=25.1.1=pyh8b19718_0
  - plotly=6.1.2=pyhd8ed1ab_0
  - python=3.10.17=hd6af730_0_cpython
  - python_abi=3.10=7_cp310
  - readline=8.2=h8c095d6_2
  - scipy=1.15.2=py310h1d65ade_0
  - setuptools=80.8.0=pyhff2d567_0
  - tk=8.6.13=noxft_hd72426e_102
  - tzdata=2025b=h78e105d_0
  - wheel=0.45.1=pyhd8ed1ab_1
  - pip:
      - asciitree==0.3.3
      - click==8.2.1
      - cmeel==0.57.3
      - cmeel-assimp==5.4.3.1
      - cmeel-boost==1.87.0.1
      - cmeel-console-bridge==1.0.2.3
      - cmeel-octomap==1.10.0
      - cmeel-qhull==8.0.2.1
      - cmeel-tinyxml2==10.0.0
      - cmeel-urdfdom==4.0.1
      - cmeel-zlib==1.3.1
      - coal-library==3.0.1
      - decorator==5.2.1
      - eigenpy==3.10.3
      - eiquadprog==1.2.9
      - fasteners==0.19
      - ipython==8.36.0
      - ischedule==1.2.7
      - meshcat==0.3.2
      - numcodecs==0.13.1
      - pexpect==4.9.0
      - pillow==11.2.1
      - pin==3.4.0
      - placo==0.8.10
      - ptyprocess==0.7.0
      - pygments==2.19.1
      - pyngrok==7.2.9
      - pyyaml==6.0.2
      - rhoban-cmeel-jsoncpp==1.9.4.8
      - tomli==2.2.1
      - tqdm==4.67.1
      - u-msgpack-python==2.8.0
      - zarr==2.18.3

```

## Python signatures and reward/observation bodies (33 files)


### dexumi/diffusion_policy/dataloader/dexumi_dataset.py

```
class DexUMIDataset(DiffusionBCDataset)
    def __init__(self, data_dirs, max_episode, load_camera_ids, camera_resize_shape, pred_horizon, obs_horizon, action_horizon, unnormal_list, seed, optional_transforms, replay_buffer_cls, relative_hand_action)
    def get_relative_action_normalization_stats(self)
    def __getitem__(self, idx)
```

### dexumi/diffusion_policy/dataloader/diffusion_bc_dataset.py

```
def process_image(image, optional_transforms, resize_shape)
def create_sample_indices(episode_ends, sequence_length, pad_before, pad_after)
def sample_sequence(train_data, sequence_length, buffer_start_idx, buffer_end_idx, sample_start_idx, sample_end_idx)
def get_data_stats(data)
def normalize_data(data, stats)
def unnormalize_data(ndata, stats)
class DiffusionBCDataset(Dataset)
    def __init__(self, data_dirs, max_episode, load_camera_ids, camera_resize_shape, pred_horizon, obs_horizon, action_horizon, unnormal_list, seed, replay_buffer_cls)
    def set_seed(self, seed)
    def transform_images(self, images_arr)
    def __len__(self)
    def __getitem__(self, idx)
```

### dexumi/diffusion_policy/dataloader/replay_buffer.py

```
class ReplayBuffer()
    def __init__(self, data_path, load_camera_ids, camera_resize_shape, max_episode, max_workers, bgr2rgb)
    def initiate_memory_buffer(self)
    def load_data_to_memory(self)
    def load_low_dim_data(self, root, low_dim_path)
    def load_visual_data(self, root, visual_path, dim)
    def __repr__(self)
    def __getitem__(self, key)
    def remove_key(self, key)
class DexUMIReplayBuffer(ReplayBuffer)
    def __init__(self)
    def load_data_to_memory(self)
    def _preallocate_arrays(self, total_frames)
```

### dexumi/diffusion_policy/diffusion_policy.py

```
class DiffusionPolicy(Module)
    def __init__(self, vision_backbone_kwargs, freeze_vision_back, diffusion_policy_head)
    def forward(self, noisy_actions, timesteps, proprioception, fsr, visual_obs, noise)
    def condition_sample(self, cond, trajectory, noise_scheduler)
    def inference(self, proprioception, fsr, visual_obs, trajectory, noise_scheduler, num_inference_steps)
```

### dexumi/diffusion_policy/model/diffusion_model.py

```
class SinusoidalPosEmb(Module)
    def __init__(self, dim)
    def forward(self, x)
class Downsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Upsample1d(Module)
    def __init__(self, dim)
    def forward(self, x)
class Conv1dBlock(Module)
    """Conv1d --> GroupNorm --> Mish"""
    def __init__(self, inp_channels, out_channels, kernel_size, n_groups)
    def forward(self, x)
class ConditionalResidualBlock1D(Module)
    def __init__(self, in_channels, out_channels, cond_dim, kernel_size, n_groups)
    def forward(self, x, cond)
class ConditionalUnet1D(Module)
    def __init__(self, input_dim, global_cond_dim, diffusion_step_embed_dim, down_dims, kernel_size, n_groups)
    def forward(self, sample, timestep, global_cond)
def get_resnet(name, weights)
def replace_submodules(root_module, predicate, func)
def replace_bn_with_gn(root_module, features_per_group)
```

### dexumi/diffusion_policy/model/encoder.py

```
def replace_submodules(root_module, predicate, func)
class CNN(Module)
    def __init__(self, out_size)
    def forward(self, images)
class CNN_v3(Module)
    def __init__(self, out_size)
    def forward(self, images)
class SimpleCNN(Module)
    def __init__(self, state_size, n_frames, out_size, net_arch, nmb_prototypes, normalize, use_group_norm, use_spectral_norm, use_batch_norm, encode_distribution, transformer_encoder, temporal_position_encoding, use_classification_head)
    def forward(self, images, bbox)
    def classification(self, images)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, images, bbox)
class VisualMotionEncoder(Module)
    def __init__(self, vision_encoder, nmb_prototypes, state_size, out_size, vision_only, normalize, start_end, goal_condition, temporal_transformer_encoder)
    def forward(self, image, state)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, image, state)
class VisualMotionPrior(Module)
    def __init__(self, vision_encoder, out_size, vision_only, nmb_prototypes, normalize)
    def forward(self, image, state)
    def get_state_representation(self, image, state)
class AblationVisualMotionEncoder(Module)
    def __init__(self, vision_encoder, nmb_prototypes, state_size, out_size, vision_only, normalize, start_end, goal_condition, temporal_transformer_encoder)
    def forward(self, image, state)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, image, state)
class TCNVisualMotionEncoder(Module)
    def __init__(self, vision_encoder, state_net, state_size, out_size)
    def forward(self, image, state)
    def get_state_representation(self, image, state)
class MixinEncoder(Module)
    def __init__(self, vision_encoder, state_encoder, mix_net, nmb_prototypes, state_size, out_size, vision_only, normalize, start_end, goal_condition, temporal_transformer_encoder)
    def forward(self, image, state)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, image, state)
class MixinMotionPrior(Module)
    def __init__(self, vision_encoder, state_encoder, mix_net, out_size, vision_only, nmb_prototypes, normalize)
    def forward(self, image, state)
    def get_state_representation(self, image, state)
class BboxEncoder(Module)
    def __init__(self, state_size, n_frames, n_objects, out_size, net_arch, start_end, append_distance, append_center, nmb_prototypes, normalize, use_group_norm, use_spectral_norm, use_batch_norm, encode_distribution, spatial_transformer_encoder, temporal_transformer_encoder, bbox_embedding)
    def forward(self, images, bbox)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, images, bbox)
class BboxMotionPrior(Module)
    def __init__(self, out_size, nmb_prototypes, normalize, spatial_transformer_encoder)
    def forward(self, images, bbox)
    def get_state_representation(self, images, bbox)
class DiffBboxEncoder(Module)
    def __init__(self, state_size, n_frames, n_objects, out_size, net_arch, nmb_prototypes, normalize, use_group_norm, use_spectral_norm, use_batch_norm, encode_distribution, spatial_transformer_encoder, temporal_transformer_encoder)
    def forward(self, images, bbox)
class DebugEncoder(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm)
    def forward(self, images, bbox)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, images, bbox)
class StateDebugEncoder(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm, use_gaussian)
    def forward(self, images, bbox)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, images, bbox)
class MlpEncoder(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm)
    def forward(self, images, bbox)
class Conv3DEncoder(Module)
    def __init__(self, out_size, net_arch, nmb_prototypes, normalize, use_batch_norm)
    def forward(self, images, bbox)
    def get_state_representation(self, images, bbox)
class ResnetEncoder(Module)
    def __init__(self, state_size, n_frames, out_size, net_arch, use_batch_norm, remove_layer_num, encode_distribution, use_spatial_softmax, use_group_norm, transformer_encoder, temperature)
    def forward(self, x, bbox)
    def get_traj_representation(self, state_representation)
    def get_state_representation(self, images, bbox)
class SpatialSoftmaxCNN(Module)
    def __init__(self, temperature)
    def forward(self, images, bbox)
class SpatialSoftmax(Module)
    def __init__(self, temperature, normalized_coordinates)
    def forward(self, x)
    def create_meshgrid(self, x, normalized_coordinates)
class ResnetConv(Module)
    def __init__(self, embedding_size, pretrained, no_training, remove_layer_num, img_c, no_stride, use_group_norm, feature_per_group)
    def forward(self, x)
class Conv3D(Module)
    """- A 3D CNN with 11 layers.
- Kernel size is kept 3 for all three dimensions - (time, H, W)
  except the first layer has kernel size of (3, 5, 5)
- Time dimension is preserved with `padding=1` and `stride=1`, and is
  averaged at the end
Arguments:
- Input: a (batch_size, 3, sequence_length, W, H) te"""
    def __init__(self, column_units)
    def forward(self, x)
class ObjectsCrops(Module)
    def __init__(self, video_hw, output_size)
    def prepare_outdim(self, outdim)
    def forward(self, features, boxes)
```

### dexumi/diffusion_policy/model/network.py

```
def add_sn(m)
def create_mlp(input_dim, output_dim, net_arch, activation_fn, use_batch_norm, use_group_norm, use_spectral_norm, squash_output, sigmoid_output, dropout_prob)
class MLPCategoricalActor(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm, use_group_norm, use_spectral_norm)
    def forward(self, obs, act)
    def _distribution(self, obs)
    def _log_prob_from_distribution(self, pi, act)
class Mlp(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm, use_group_norm, use_spectral_norm, sigmoid_output)
    def forward(self, x)
class GaussianMlp(Module)
    def __init__(self, in_size, out_size, net_arch, use_batch_norm, use_group_norm, dropout_prob, latent_drop_prob)
    def forward(self, input)
class MixinGaussianBcPolicy(Module)
    def __init__(self, vision_encoder, state_encoder, mix_net, action_dim, vision_only, bc_net_arch, use_batch_norm, use_group_norm)
    def forward(self, image, state)
class GMMMlp(Module)
    def __init__(self, in_size, out_size, n_mode, net_arch, use_batch_norm, use_group_norm)
    def forward(self, input)
class LSTMGenerator(Module)
    """An LSTM based generator. It expects a sequence of noise vectors as input.
Args:
    in_dim: Input noise dimensionality
    out_dim: Output dimensionality
    n_layers: number of lstm layers
    hidden_dim: dimensionality of the hidden layer of lstms
Input: noise of shape (batch_size, seq_len, in_dim"""
    def __init__(self, in_size, out_size, hidden_dim, n_layers, net_arch, use_batch_norm, use_group_norm, use_spectral_norm)
    def forward(self, input, prototype)
```

### dexumi/diffusion_policy/utility/evaluation.py

```
def build_evaluation_environment(env_cfg, info, qpos, qvel)
def load_env_state(env, qpos, qvel)
def process_env_visual_observation(visual_observation, resize_shape)
def evaluate_flow_diffusion_policy(model, noise_scheduler, num_inference_steps, stats, num_samples, env_cfg, eval_dataset, data_buffers, result_save_path, seed)
def evaluate_flow_diffusion_policy_from_generated_flow(model, noise_scheduler, num_inference_steps, stats, num_samples, env_cfg, data_dirs, num_points, point_tracking_img_size, resize_shape, action_dim, obs_horizon, action_horizon, target_flow_horizon, pred_horizon, point_tracking_camera_id, camera_intrinsic, camera_pose_matrix, normalize_pointcloud, result_save_path, flow_generator_additional_args, seed)
def replay_action(replay_offset, num_samples, env_cfg, data_buffer, result_save_path)
def render_depth(num_samples, env_cfg, data_buffer)

```python
def process_env_visual_observation(visual_observation, resize_shape):
    visual_observation = cv2.resize(visual_observation, resize_shape)
    visual_observation = process_image(visual_observation)
    return visual_observation
```
```

### dexumi/encoder/xhand_tactile.py

```
class XhandUARTReader(UARTReader)
    def __init__(self, uart_port, header, block_size, baud_rate, verbose)
    def process_buffer(self)
    def process_block(self, block)
class XhandTactile(XhandUARTReader, Numeric)
    def __init__(self, device_name, latency, uart_port, header, block_size, baud_rate, verbose)
    def start_streaming(self)
    def stop_streaming(self)
```

### dexumi/hand_sdk/dexhand.py

```
class DexterousHand(ABC)
    def __init__(self)
    def connect(self)
    def disconnect(self)
    def get_current_position(self)
    def send_command(self, command)
    def write_hand_angle(self, angles)
class ExoDexterousHand(DexterousHand)
    """Extended dexterous hand with additional exoskeleton-specific methods."""
    def load_model(self, model_path)
    def predict_motor_value(self, joint_angle)
    def write_hand_angle_position_from_motor(self, motor_values)
```

### dexumi/hand_sdk/inspire/hand_api_cls.py

```
class InspireSDK(DexterousHand)
    def __init__(self, hand_id, port, baudrate, databits, parity, stopbits, read_rate, verbose)
    def _debug(self, message)
    def connect(self)
    def disconnect(self)
    def get_current_position(self)
    def start_reader(self)
    def stop_reader(self)
    def _read_loop(self)
    def _process_buffer(self)
    def _validate_block(self, block)
    def _handle_block(self, block)
    def send_command(self, command)
    def write_hand_angle(self, val1, val2, val3, val4, val5, val6)
    def write_hand_angle_force(self, val1, val2, val3, val4, val5, val6)
    def build_read_hand_register_data(self, reg_addr, read_len)
class ExoInspireSDK(InspireSDK, ExoDexterousHand)
    def __init__(self, finger_mapping_model_path, thumb_swing_model_path, thumb_middle_model_path, per_finger_adj_val)
    def predict_motor_value(self, joint_angle)
```

### dexumi/hand_sdk/xhand/hand_api_cls.py

```
class JointState()
class Force()
class FingertipState()
class HandState()
class XhandSDK(DexterousHand)
    def __init__(self, hand_id, port, protocol, state_queue_size, update_frequency)
    def connect(self)
    def disconnect(self)
    def open_device(self, device_identifier)
    def reset_sensor(self, sensor_id)
    def enumerate_devices(self, protocol)
    def list_hands_id(self)
    def set_hand_id(self, new_id)
    def get_current_position(self)
    def get_tactile(self, calc)
    def _get_current_state(self)
    def start_reader(self)
    def stop_reader(self)
    def _read_loop(self)
    def send_command(self, command)
    def write_hand_angle(self, angles)
class ExoXhandSDK(XhandSDK, ExoDexterousHand)
    def __init__(self, hand_id, port, protocol, calibration_dir, per_finger_adj_val)
    def predict_motor_value(self, joint_angles)
```

### dexumi/real_env/common/base.py

```
class TransportType(Enum)
class RequestType(Enum)
    """Base enum for request types. Inherit and extend this in your implementation."""
class Request()
    """Generic request container."""
    def __post_init__(self)
class Response()
    """Generic response container."""
class ZMQServerBase()
    def __init__(self, pub_address, req_address, topic, max_buffer_size, pub_frequency, req_frequency, frames_per_publish, verbose)
    def is_paused(self)
    def pause(self)
    def resume(self)
    def _publish_loop(self)
    def start(self)
    def _debug(self, message)
    def _handle_requests(self)
    def get_last_n_data(self, n)
    def clear_buffer(self)
    def _get_data(self)
    def _process_request(self, request)
    def _rate_limit(frequency)
    def stop(self)
class ZMQClientBase()
    def __init__(self, pub_address, req_address, topic, req_frequency, verbose)
    def _debug(self, message)
    def _error(self, message)
    def _rate_limit(frequency)
    def _send_loop(self)
    def _handle_responses(self)
    def receive_data(self, timeout)
    def send_request(self, request, timeout)
    def receive_response(self, timeout)
    def close(self)
```

### dexumi/real_env/common/camera.py

```
class CameraRequestType(RequestType)
class CameraServer(ZMQServerBase)
    def __init__(self, camera, pub_address, req_address, max_buffer_size, pub_frequency, req_frequency, resize_ratio, color_conversion, frames_per_publish, topic, compression, compression_quality)
    def compress_frame(self, frame)
    def process_frame(self, frame)
    def _get_data(self)
    def start(self)
    def _process_request(self, request)
    def stop(self)
    def clear_frame_buffer(self)
class CameraClient(ZMQClientBase)
    def __init__(self, pub_address, req_address, topic)
    def decompress_frame(self, frame_data)
    def process_received_frame(self, frame_data)
    def receive_frame(self, timeout)
    def get_recent_frames(self, k, timeout)
    def get_recent_frames_async(self, k)
    def get_intrinsics(self, timeout)
    def get_intrinsics_async(self)
```

### dexumi/real_env/common/dexhand.py

```
class DexRequestType(RequestType)
class DexServer(ZMQServerBase)
    def __init__(self, hand, pub_address, req_address, max_buffer_size, pub_frequency, req_frequency, frames_per_publish, topic, frequency, max_motor_speed, launch_timeout, soft_real_time, verbose)
    def _get_data(self)
    def _process_request(self, request)
    def start(self)
    def run(self)
    def stop(self)
class DexClient(ZMQClientBase)
    def __init__(self, pub_address, req_address, topic, verbose)
    def schedule_waypoint(self, target_pos, target_time, timeout)
    def send_pos(self, pos, timeout)
    def get_pos(self, timeout)
    def get_tactile(self, calc, timeout)
    def predict_pos_from_joint(self, joint_angles, timeout)
    def get_state(self, timeout)
```

### dexumi/real_env/common/motor_trajectory_interpolator.py

```
class MotorTrajectoryInterpolator()
    def __init__(self, times, values)
    def times(self)
    def values(self)
    def trim(self, start_t, end_t)
    def drive_to_waypoint(self, value, time, curr_time, max_speed)
    def schedule_waypoint(self, value, time, max_speed, curr_time, last_waypoint_time)
    def __call__(self, t)
```

### dexumi/real_env/common/numeric.py

```
class NumericServer(ZMQServerBase)
    def __init__(self, numeric, pub_address, req_address, max_buffer_size, pub_frequency, req_frequency, frames_per_publish, topic)
    def _get_data(self)
class NumericClient(ZMQClientBase)
    def __init__(self, pub_address, req_address, topic)
    def receive_frame(self, timeout)
```

### dexumi/real_env/common/policy.py

```
class PolicyRequestType(RequestType)
class PolicyServer(ZMQServerBase)
    def __init__(self, obs_config, pub_address, req_address, max_buffer_size, pub_frequency, req_frequency, topic, verbose)
    def start(self)
    def _validate_obs_config(self)
    def _check_policy_obs_shape(self, policy_obs)
    def _process_request(self, request)
    def _predict_action(self, policy_obs)
    def _preprocess_policy_obs(self, policy_obs)
    def _inference_action(self, policy_obs)
    def create_with_example_input(cls, example_input)
class PolicyClient(ZMQClientBase)
    def __init__(self, pub_address, req_address, req_frequency, topic, verbose)
    def get_action(self, policy_obs, timeout)
    def get_obs_config(self, timeout)
    def get_attr(self, attr_name, timeout)
```

### dexumi/real_env/common/pose_trajectory_interpolator.py

```
def rotation_distance(a, b)
def pose_distance(start_pose, end_pose)
class PoseTrajectoryInterpolator()
    def __init__(self, times, poses)
    def times(self)
    def poses(self)
    def trim(self, start_t, end_t)
    def drive_to_waypoint(self, pose, time, curr_time, max_pos_speed, max_rot_speed)
    def schedule_waypoint(self, pose, time, max_pos_speed, max_rot_speed, curr_time, last_waypoint_time)
    def __call__(self, t)
```

### dexumi/real_env/common/ur5.py

```
class UR5RequestType(RequestType)
class UR5Frame()
class UR5Server(ZMQServerBase)
    def __init__(self, robot_ip, pub_address, req_address, max_buffer_size, pub_frequency, req_frequency, frames_per_publish, topic, frequency, lookahead_time, gain, max_pos_speed, max_rot_speed, launch_timeout, tcp_offset_pose, payload_mass, payload_cog, joints_init, joints_init_speed, soft_real_time, verbose, receive_keys, receive_latency)
    def _process_request(self, request)
    def _get_data(self)
    def get_state_history(self)
    def start(self)
    def run(self)
    def stop(self)
class UR5eClient(ZMQClientBase)
    def __init__(self, pub_address, req_address, topic, verbose)
    def schedule_waypoint(self, target_pose, target_time, timeout)
    def stop(self, timeout)
    def get_state(self, timeout)
    def get_state_history(self, timeout)
    def connect_to_robot(self, timeout)
```

### dexumi/real_env/dexumi_policy.py

```
class DexUMIPolicySever(PolicyServer)
    def __init__(self, obs_config, model_path, ckpt, req_address)
    def _preprocess_policy_obs(self, policy_obs)
    def _inference_action(self, policy_obs)
```

### dexumi/real_env/real_policy.py

```
class RealPolicy()
    def __init__(self, model_path, ckpt)
    def predict_action(self, proprioception, fsr, visual_obs)
```

### dexumi/real_env/ring_buffer.py

```
class RingBuffer(?)
    def __init__(self, size)
    def write(self, item)
    def read_last(self, n)
    def clear(self)
    def __len__(self)
```

### dexumi/real_env/spacemouse.py

```
class Spacemouse()
    def __init__(self, get_max_k, frequency, max_value, deadzone, dtype, n_buttons)
    def get_motion_state(self)
    def get_motion_state_transformed(self)
    def get_button_state(self)
    def is_button_pressed(self, button_id)
    def start(self, wait)
    def stop(self, wait)
    def __enter__(self)
    def __exit__(self, exc_type, exc_val, exc_tb)
    def _run(self)
```

### linkage_optimization/get_sim_fingertips_trajectory.py

```
def read_jsonl_to_dict(file_path)
def modify_urdf(finger_optimization_path, thumb_optimization_path, output_path)
def main(swing_move, finger_optimization_path, thumb_optimization_path)
```

### linkage_optimization/simple_regression.py

```
def create_trajectory_visualization(real_data, sim_data, finger_name)
def match_trajectories_and_regress(real_data, sim_data, finger_name, polynomial_degree)
def main(real_traj, sim_traj, output_path, polynomial_degree, finger_name)
```

### real_script/data_generation_pipeline/1_replay_hand.py

```
def replay_hand(data_dir, save_dir, episode_index, hand_port, hand_type, finger_mapping_model_path, verbose, headless, fps, camera_latency, reference_dir)
```

### real_script/eval_policy/eval_inspire_hand.py

```
def main(frequency, max_pos_speed, max_rot_speed, enable_record_camera, model_path, ckpt, camera_latency, hand_action_latency, robot_action_latency, exec_horizon, video_record_path, match_episode_path)
```

### real_script/eval_policy/eval_xhand.py

```
def compute_total_force_per_finger(all_fsr_observations)
def main(frequency, max_pos_speed, max_rot_speed, enable_record_camera, model_path, ckpt, camera_latency, hand_action_latency, robot_action_latency, exec_horizon, video_record_path, match_episode_path)
```

### real_script/policy_training/train_diffusion_policy.py

```
def train_diffusion_policy(cfg)
```

### real_script/teleoperation/calibrate_xhand_mapping.py

```
def main(enable_encoder, joint_index, model_dir)
```