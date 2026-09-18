# sparsh_2024

source: https://github.com/facebookresearch/sparsh


commit: fee6a05a97330eca014b59c71ac41596fe3974a7


## README

# Sparsh: Self-supervised touch representations for vision-based tactile sensing


<p align="center">
Carolina Higuera<sup>*</sup>,
Akash Sharma<sup>*</sup>,
Chaithanya Krishna Bodduluri,
Taosha Fan,
Patrick Lancaster,
Mrinal Kalakrishnan,
Michael Kaess,
Byron Boots,
Mike Lambeta,
Tingfan Wu,
Mustafa Mukadam
</p>

<p align="center">
<sup>*</sup>Equal contribution
</p>

<p align="center">
    <a href=https://ai.facebook.com/research/ai-systems>AI at Meta, FAIR</a>;
    <a href=https://ri.cmu.edu/>The Robotics Institute, CMU</a>;
    <a href=https://www.washington.edu/>University of Washington</a>
</p>

<p align="center">
    <a href="https://ai.facebook.com/research/publications/sparsh-self-supervised-touch-representations-for-vision-based-tactile-sensing"><img src="http://img.shields.io/badge/Paper-PDF-red.svg"></img></a>
    <a href="https://arxiv.org/abs/2410.24090"><img src="https://img.shields.io/badge/arXiv-2410.24090-b31b1b.svg"></img></a>
    <a href="https://sparsh-ssl.github.io"><img src="http://img.shields.io/badge/Project-Page-blue.svg"></img></a>
    <a href="https://youtu.be/8q2BI5HePq0"><img src="http://img.shields.io/badge/Video-Link-green.svg"></img></a>
    <a href="https://huggingface.co/collections/facebook/sparsh-67167ce57566196a4526c328"><img src="https://img.shields.io/badge/Models%20and%20datasets-Link-yellow?logo=huggingface"></img></a>
    <a href="#-citing-sparsh"><img src="http://img.shields.io/badge/Cite-Us-orange.svg"></img></a>


</p>

<p align="center">
<img src="./assets/teaser.png" alt="drawing" width="700"/>
</p>
Sparsh is a family of general touch representations trained via self-supervision algorithms such as MAE, DINO and JEPA. Sparsh is able to generate useful representations for DIGIT, Gelsight'17 and Gelsight Mini. It outperforms end-to-end models in the downstream tasks proposed in TacBench by a large margin, and can enable data efficient training for new downstream tasks.


This repository contains the pytorch implementation, pre-trained models, and datasets released with Sparsh.

<p align="center">
<img src="assets/tacbench.gif" alt="animated" />
</p>


## 🛠️Installation and setup

Clone this repository:
```bash
git clone https://github.com/facebookresearch/sparsh.git
cd sparsh
```
and create a conda environment with dependencies:
```bash
mamba env create -f environment.yml
mamba activate tactile_ssl
```

## 🚀 Pretrained models

Pretrained model weights are available for download from our Hugging Face: [facebook/sparsh](https://huggingface.co/facebook/sparsh)

<table style="margin: auto">
  <thead>
    <tr>
      <th>model</th>
      <th>small</th>
      <th>base</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sparsh (MAE)</td>
      <td><a href="https://huggingface.co/facebook/sparsh-mae-small">backbone</a></td>
      <td><a href="https://huggingface.co/facebook/sparsh-mae-base">backbone only</a></td>
    </tr>
    <tr>
      <td>Sparsh (DINO)</td>
      <td><a href="https://huggingface.co/facebook/sparsh-dino-small/">backbone</a></td>
      <td><a href="https://huggingface.co/facebook/sparsh-dino-base/">backbone</a></td>
    </tr>
    <tr>
      <td>Sparsh (DINOv2)</td>
      <td>:x:</td>
      <td><a href="https://huggingface.co/facebook/sparsh-dinov2-base/">backbone</a></td>
    </tr>
    <tr>
      <td>Sparsh (IJEPA)</td>
      <td><a href="https://huggingface.co/facebook/sparsh-ijepa-small/">backbone</a></td>
      <td><a href="https://huggingface.co/facebook/sparsh-ijepa-base/">backbone</a></td>
    </tr>
    <tr>
      <td>Sparsh (VJEPA)</td>
      <td><a href="https://huggingface.co/facebook/sparsh-vjepa-small/">backbone</a></td>
      <td><a href="https://huggingface.co/facebook/sparsh-vjepa-base/">backbone</a></td>
    </tr>
  </tbody>
</table>


## 📥 Datasets

### Pretraining datasets

For pretraining, we curate datasets from multiple sources containing unlabeled data from DIGIT and GelSight sensors.

For DIGIT, the dataset is a mixture of the [YCB-Slide dataset](https://github.com/rpl-cmu/YCB-Slide) and in-house collected data: [Touch-Slide](https://huggingface.co/datasets/facebook/touch-slide). It contains approximately 360k samples of tactile images with a diverse set of no-contact images or backgrounds.

For GelSight, we use open source datasets available online, [Touch and Go](https://touch-and-go.github.io/) and [ObjectFolder-Real](https://objectfolder.stanford.edu/objectfolder-real-download).

<!-- - [ ] @Carolina: Update with correct scripts -->

#### DIGIT

To download the dataset, please edit `path_dataset` in the bash script `scripts/download_digitv1_dataset.sh`. This will download and extract the data in `path_dataset` for both YCB-Slide and Touch-Slide datasets.

The structure of the dataset is:

```bash
digitv1/Object-Slide
├── object_0 # eg: 004_sugar_box
│   ├── dataset_0.pkl
    ├── dataset_1.pkl
    ├── dataset_2.pkl
    ├── dataset_3.pkl
    ├── dataset_4.pkl
├── object_1 # eg: bread
...
├── bgs
    ├── bg_0.jpg
    ...
    ├── bg_18.jpg
```

In the `bgs/` folder there are images of several no-contact images or backgrounds from different DIGIT sensors. This is necessary for pre-processing the data. Please add to these folder background images from your sensor in case you're adding new tactile data.

To load this dataset, use `tactile_ssl/data/vision_tactile.py`

#### GelSight dataset

We use [Touch and Go](https://touch-and-go.github.io/) to pretrain on GelSight'17 (with markers). The dataset consists of short videoclips making contact with in-the-wild objects. We use all frames from those videoclips, including no-contact frames. We do not perform any preprocessing since the markers contain relevant static shear information.

We also use sequences from the [ObjectFolder-Real](https://objectfolder.stanford.edu/objectfolder-real-download) dataset for pre-training. We preprocess the data by extracting only the tactile images (GelSight Mini), as we do not use the other modalities.

We provide a script to download the preprocessed and compatible version of these datasets with our pipeline. To do so, run the bash script `scripts/download_gelsight_dataset.sh`. This will download and extract the data. Don't forget to edit `path_dataset` in the script.


The structure of the dataset is:

```bash
gelsight/touch_go
    ├── 20220410_031604.pkl
    ├── 20220410_031843.pkl
    ├── ...
    ├── 20220607_133934.pkl
gelsight/object_folder
    ├── 001.pkl
    ├── 002.pkl
    ...
    ├── 051.pkl
```

If you would like to download the data directly from Touch and Go and ObjectFolder-Real, you can also do so. Data can be downloaded by running the bash scripts `scripts/download_datasets_scratch/download_gelsight_object_folder.sh` and `scripts/download_datasets_scratch/download_gelsight_touchgo.sh`. Then, you can process the data to make it compatible with our pipeline by running the Python scripts `scripts/download_datasets_scratch/compress_object_folder.py` and `scripts/download_datasets_scratch/compress_touch_go.py`. Please modify the corresponding paths in all scripts accordingly.

To load this dataset, use `tactile_ssl/data/vision_tactile.py`

### Downstream task datasets

We open-source the data that we collected in-house for force estimation, slip detection and pose estimation downstream tasks. The datasets can be downloaded from the Sparsh collection in Hugging Face:
- Force estimation and Slip detection: [DIGIT](https://huggingface.co/datasets/facebook/digit-force-estimation), [GelSight Mini](https://huggingface.co/datasets/facebook/gelsight-force-estimation)
- Pose estimation: [DIGIT](https://huggingface.co/datasets/facebook/digit-pose-estimation)

Please locate these datasets in a directory designated for hosting all downstream task datasets.

#### T1 Force estimation and T2 slip detection
This dataset contains paired tactile and force data, intended for use in predicting 3-axis normal and shear forces applied to the sensor's elastomer. We used three different indenter shapes to collect force-labeled data: hemisphere, sharp, and flat. To measure force ground truths, we employed the ATI nano17 force/torque sensor. The protocol consisted of applying a random normal load followed by a shear load, achieved by sliding the probe 2mm on the sensor's elastomer.

The dataset consists a collection of normal/shear load trajectories for each probe. The structure is as follows (example for DIGIT dataset):

```bash
T1_force/digit/sphere
├── batch_1
│   ├── dataset_digit_00.pkl
│   ├── ...
│   ├── dataset_digit_03.pkl
│   ├── dataset_slip_forces.pkl
├── batch_2
│   ├── ...
T1_force/digit/flat
├── batch_1
│   ├── dataset_digit_00.pkl
│   ├── ...
│   ├── dataset_digit_03.pkl
│   ├── dataset_slip_forces.pkl
│   ...
T1_force/digit/sharp
├── ....
```
For each batch:
- `dataset_digit_xy.pkl`: contains the binarized tactile images only.
- `dataset_slip_forces.pkl`: it's a dictionary where each key represents a sliding trajectory. Each trajectory has the corresponding force and slip labels.

To load this dataset (DIGIT and GelSight Mini), use `tactile_ssl/data/vision_based_forces_slip_probes.py`

#### T3 Pose estimation

This dataset contains time-synchronized pairs of DIGIT images and SE(3) object poses. In our setup, the robot hand is stationary with its palm facing downwards and pressing against the object on a table. The robot hand has DIGIT sensors mounted on the index, middle, and ring fingertips, all of which are in contact with the object. A human manually perturbs the object's pose by translating and rotating it in SE(2). We use tag tracking to obtain the object's pose. We collect data using two objects: a Pringles can and the YCB sugar box, both of which have a tag fixed to their top surfaces.

The dataset is a collection of sequences where a human manually perturbs the object's pose. We collect data using two objects: a Pringles can and the YCB sugar box. Each sequence corresponds to a pickle file containing the following labeled data:
- DIGIT tactile images for index, middle and ring fingers
- Object pose tracked from tag in format (x, y, z, qw, qx, qy, qz)
- Robot hand joint positions
- `object_index_rel_pose_n5`: the pose change within the last 5 samples as a transformation matrix. The object pose is with respect to the index finger.
- `object_middle_rel_pose_n5`: the pose change within the last 5 samples as a transformation matrix. The object pose is with respect to the middle finger.
- `object_ring_rel_pose_n5`: the pose change within the last 5 samples as a transformation matrix. The object pose is with respect to the ring finger.
We also provide reference (no contact) images for each of the DIGITs to facilitate pre-processing such as background subtraction.

```bash
T3_pose/digit/train
├── pringles
│   ├── bag_00.pkl
│   ├── ...
│   ├── bag_37.pkl
│   ├── bag_38.pkl
├── sugar
│   ├── ...
T3_pose/digit/test
├── pringles
│   ├── bag_00.pkl
│   ├── ...
│   ├── bag_05.pkl
│   ├── bag_06.pkl
├── sugar
│   ├── ...
T3_pose/digit/bgs
├── digit_index.png
├── digit_index.png
├── digit_index.png
```

To load this dataset use `tactile_ssl/data/vision_based_pose_probes.py`

#### T4 Grasp stability
We use the [Feeling of Success](https://sites.google.com/view/the-feeling-of-success/) dataset. It contains approximately 9k grasp trials over 100k objects using GelSight'17 sensors mounted on a parallel gripper.

You can download the data directly from the webpage or run the bash script `scripts/download_datasets_scratch/download_gelsight_feeling_success.sh` to download the data and the Python script `scripts/download_datasets_scratch/compress_feeling_success.py` to preprocess the dataset compatible with our pipeline. Please update the paths in the scripts accordingly.

#### T5 Textile recognition

Please download the [Clothing dataset](http://data.csail.mit.edu/active_clothing/Data_ICRA18.tar). The dataset consist of 4467 short video clips (10-25 frames), of a robot with a GelSight'17 grasping several types of textile (20  classes), such as leather, cotton, polyester, etc.

## 🏋️‍♂️ Training Sparsh

We use hydra for configuration management in this repository. The configuration files are located in `config/`.

The config folder is organized as follows:

```bash
├── config
│   ├── data # contains dataset configs
│   ├── experiment # contains full config for a specific experiment (eg. Sparsh(DINO) or downstream task)
│   ├── model # contains configs for each ssl algorithm
│   ├── paths # add your config here with paths to datasets / checkpoint / outputs / etc.
│   ├── task # contains downstream_task configs for each downstream task in TacBench
│   ├── wandb # add your wandb config here for experiment tracking
│   ├── default.yaml # The SSL training default config is overridden by experiment/dino_vit.yaml and the like
```

Following are the instructions to train a Sparsh model:

- Setup the pretraining datasets according to the instructions [above](#pretraining-datasets)
- add `paths/${YOUR_PATHS}.yaml` similar to existing examples and point to the data root accordingly
- similarly add `wandb/${YOUR_CONFIG}.yaml`
- Then choose an experiment, for example: `dino_vit.yaml` and use the following script

You may need to adjust batch size according to your GPU. All training experiments were done with 8 A100-80GB GPUs.

```bash
python train.py +experiment=${YOUR_EXP_NAME} paths=${YOUR_PATHS} wandb=${YOUR_CONFIG}
```

### Training downstream tasks

For training downstream tasks, in our paper we largely follow frozen evaluation, where we freeze the weights of the Sparsh encoder, and only train a lightweight decoder for each downstream task.
Training downstream tasks is quite similar to the above instructions but additionally requires a pre-trained model checkpoint `checkpoint_encoder` which can be specified by updating the `task.checkpoint_encoder` field in the config. Downstream tasks also need a labeled dataset for the corresponding downstream task.

Use the following script to train downstream tasks:
```bash
python train_task.py --config-name=experiment/downstream_task/${EXPERIMENT} paths=${YOUR_PATH_CONFIG} wandb=${YOUR_WANDB_CONFIG}
```

Once you complete training downstream task decoders for each task, you can also test the checkpoints using the `test_task.py` script which essentially follows the same format as above. For convenience, we also provide a `submit_task.sh` bash script to train and test downstream tasks if you're using a SLURM based cluster.

Finally, we also `tacbench_report.ipynb` where we compute metrics for all the downstream tasks, once the data is computed from the `test_task.py` script.

## 🤹‍♀️ Sparsh demo: force field visualization

<p align="center">
<img src="assets/demo_digit.gif" alt="animated" />
</p>

For testing Sparsh(DINO) + force field decoder live, you only need one DIGIT or GelSight Mini sensor. Follow these steps to run the demo:

1. Create a folder for downloading the task checkpoints. For example, `${YOUR_PATH}/outputs_sparsh/checkpoints`.
<!-- UPDATE THIS -->
2. Download the decoder checkpoints from Hugging Face for [DIGIT](https://huggingface.co/facebook/sparsh-digit-forcefield-decoder) and [GelSight Mini](https://huggingface.co/facebook/sparsh-gelsight-forcefield-decoder).
3. Connect the sensor to your PC. In case of DIGIT, please make sure you have [digit-interface](https://github.com/facebookresearch/digit-interface) installed.
4. Make sure the device is recognized by the OS (you can use Cheese in Linux to see the video that the sensor is streaming).

5. Running the demo for DIGIT:

```bash
python demo_forcefield.py +experiment=downstream_task/forcefield/digit_dino paths=${YOUR_PATH_CONFIG} paths.output_dir=${YOUR_PATH}/outputs_sparsh/checkpoints/ test.demo.digit_serial=${YOUR_DIGIT_SERIAL}`
```
The DIGIT serial number is printed on the back of the sensor and has the format `DXXXXX`.

6. Running the demo for GelSight Mini:

```bash
python demo_forcefield.py +experiment=downstream_task/forcefield/gelsight_dino paths=${YOUR_PATH_CONFIG} paths.output_dir=${YOUR_PATH}/outputs_sparsh/checkpoints/ test.demo.gelsight_device_id=${YOUR_GELSIGHT_VIDEO_ID}`
```

The GelSight Mini is recognized as a webcam. You can get the video ID by checking in a terminal `ls -l /dev/video*`.

7. Take the sensor and slide it across the edge of a table, or across objects with interesting textures! Look at the normal field to localize where you're making contact on the sensor's surface. Look at the shear field to gather an intuition about the direction of the shear force that you applied while sliding the sensor. For example, slide the sensor over an edge up and down to get translational shear or rotate the sensor in place to see torsional slip!


## License
This project is licensed under [LICENSE](LICENSE).


## 📚 Citing Sparsh

If you find this repository useful, please consider giving a star :star: and citation:
```
@inproceedings{
    higuera2024sparsh,
    title={Sparsh: Self-supervised touch representations for vision-based tactile sensing},
    author={Carolina Higuera and Akash Sharma and Chaithanya Krishna Bodduluri and Taosha Fan and Patrick Lancaster and Mrinal Kalakrishnan and Michael Kaess and Byron Boots and Mike  Lambeta and Tingfan Wu and Mustafa Mukadam},
    booktitle={8th Annual Conference on Robot Learning},
    year={2024},
    url={https://openreview.net/forum?id=xYJn2e1uu8}
}
```

## 🤝 Acknowledgements


We thank Ishan Misra, Mahmoud Assran for insightful discussions on SSL for vision that informed this work, and Changhao Wang, Dhruv Batra, Jitendra Malik, Luis Pineda, Tess Hellebrekers for helpful discussions on the research.


We also thank the team behind datasets like [YCB-Slide](https://github.com/rpl-cmu/YCB-Slide), [Touch and Go](https://touch-and-go.github.io/), [ObjectFolder-Real](https://objectfolder.stanford.edu/objectfolder-real-download), [Feeling of Success](https://sites.google.com/view/the-feeling-of-success/)  and [Clothing dataset](http://data.csail.mit.edu/active_clothing/Data_ICRA18.tar) for contributing to the research community by open-sourcing their tactile data.


## File tree (depth 3, assets pruned)

```
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE.md
README.md
config/
  default.yaml
  experiment/
    dino_vit.yaml
    dinov2_vit.yaml
    downstream_task/
    ijepa_vit.yaml
    mae_vit.yaml
    vjepa_vit.yaml
  model/
    dino_vit.yaml
    dinov2_vit.yaml
    ijepa_vit.yaml
    mae_ret.yaml
    mae_vit.yaml
    vjepa_vit.yaml
  paths/
    default.yaml
    fair-aws-ch.yaml
    fair-aws.yaml
  task/
    digit_forcefield.yaml
    t1_force_estimation.yaml
    t2_slip_detection.yaml
    t3_pose_estimation.yaml
    t4_grasp_stability.yaml
    t6_textile_classification.yaml
demo_forcefield.py
environment.yml
pyproject.toml
scripts/
  download_datasets_scratch/
    compress_feeling_success.py
    compress_object_folder.py
    compress_touch_go.py
    download_gelsight_feeling_succes.sh
    download_gelsight_object_folder.sh
    download_gelsight_touchgo.sh
  download_digitv1_dataset.sh
  download_gelsight_dataset.sh
  download_gs_object_slide.sh
  slip_labelling.py
setup.py
submit.sh
submit_task.sh
tacbench_report.ipynb
tactile_ssl/
  algorithm/
    __init__.py
    dino.py
    dinov2.py
    ijepa.py
    mae.py
    module.py
    vjepa.py
  downstream_task/
    __init__.py
    attentive_pooler.py
    force_sl.py
    forcefield_sl.py
    grasp_sl.py
    pose_sl.py
    sl_module.py
    slip_decoders.py
    slip_sl.py
    textile_sl.py
    utils_forcefield/
  loss/
    dino_loss.py
    ibot_patch_loss.py
    koleo_loss.py
  model/
    __init__.py
    custom_scheduler.py
    layers/
    multimodal_transformer.py
    pretrained.py
    vision_transformer.py
  probe/
    __init__.py
    online_probe.py
    reconstruction.py
  test/
    __init__.py
    demo_t1_forcefield.py
    test_t1_force.py
    test_t2_slip.py
    test_t3_pose.py
    test_t4_grasp.py
    test_t6_textile.py
    test_task.py
  trainer/
    __init__.py
    trainer.py
  utils/
    __init__.py
    ema.py
    logging.py
    masking.py
    plotting_forces.py
    plotting_utils.py
    signal_connector.py
    tensors.py
test_task.py
train.py
train_task.py
```

## Config files (67)


### config/default.yaml

```yaml
defaults:
  - paths: default
  - wandb: akash
  - data: xela
  - model: byol_alexnet
  - override hydra/job_logging: colorlog
  - override hydra/hydra_logging: colorlog
  - _self_

seed: 42
model_size: base
model_embed_dim: 768
resume_id: ~
ckpt_path: ~
experiment_name: default_${model_size}
data_out_format: 'concat_ch_img'
num_frames: 2
frame_stride: 5

trainer:
  max_epochs: ~
  grad_clip_norm: 10.0
  validation_frequency: 10
  checkpoint_frequency: 20
  log_frequency: 500
  save_checkpoint_dir: ${paths.output_dir}/checkpoints

hydra:
  job:
    id: ${now:%Y.%m.%d}-${now:%H-%M}
  run:
    dir: ${paths.log_dir}/${experiment_name}/${hydra.job.id}

```

### config/experiment/dino_vit.yaml

```yaml
# @package _global_
defaults:
  - override /paths: ~
  - override /wandb: ~
  - override /data: vision_based
  - override /model: dino_vit
  - _self_

model_size: base
model_embed_dim: 768
experiment_name: sparsh_dino_vit${model_size}
ckpt_path: ~

wandb:
  project: sparsh_dino
  group: dino_vit${model_size}
  tags: ["vit${model_size}"]

trainer:
  max_epochs: 200

model:
  encoder:
    _target_: tactile_ssl.model.vit_${model_size}
    img_size: [320, 240]
    in_chans: 6
    pos_embed_fn: sinusoidal

  dino_head:
    out_dim: 65536

  online_probes:
    - _target_: tactile_ssl.probe.online_probe.OnlineProbeModule
      probe_name: "reconstruction"
      decoder:
        _target_: tactile_ssl.probe.reconstruction.DecoderImage
        in_chans: 6
        img_size: [320, 240]
        patch_size: 16
        input_embed_dim: ${model_embed_dim}
        embed_dim: 192
        depth: 4
      loss_fn:
        _target_: torch.nn.MSELoss


```

### config/experiment/dinov2_vit.yaml

```yaml
# @package _global_
defaults:
  - override /paths: ~
  - override /wandb: ~
  - override /data: vision_based
  - override /model: dinov2_vit
  - _self_

model_size: base
model_embed_dim: 768
experiment_name: sparsh_dinov2_vit${model_size}
ckpt_path: ~

wandb:
  project: sparsh_dinov2
  group: dinov2_vit${model_size}
  tags: ["vit${model_size}"]

trainer:
  max_epochs: 200

data: 
  train_dataloader: 
    batch_size: 32
  val_dataloader: 
    batch_size: 32

model:
  centering: centering
  encoder:
    _target_: tactile_ssl.model.vit_${model_size}
    img_size: [320, 240]
    in_chans: 6
    pos_embed_fn: sinusoidal

  dino_head:
    out_dim: 65536

  optim_cfg:
    lr: 0.002

  online_probes:
    - _target_: tactile_ssl.probe.online_probe.OnlineProbeModule
      probe_name: "reconstruction"
      decoder:
        _target_: tactile_ssl.probe.reconstruction.DecoderImage 
        in_chans: 6
        img_size: [320, 240]
        patch_size: 16
        input_embed_dim: ${model_embed_dim}
        embed_dim: 192
        depth: 4
      loss_fn:
        _target_: torch.nn.MSELoss

  online_probes_lrs: [1e-4]

```

### config/experiment/downstream_task/force/digit_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t1_force_estimation
  - _self_

ssl_name: dino
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/force/digit_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t1_force_estimation
  - _self_

ssl_name: dinov2
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/force/digit_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~ 
  - /data: digit_force
  - /task: t1_force_estimation
  - _self_

ssl_name: e2e
sensor: digit
ckpt_path: ~

trainer:
  save_probe_weights_only: false

task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true
```

### config/experiment/downstream_task/force/digit_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t1_force_estimation
  - _self_

ssl_name: ijepa
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/force/digit_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t1_force_estimation
  - _self_

ssl_name: mae
sensor: digit
ckpt_path: ~

task:
  model_encoder:
    num_register_tokens: 0


```

### config/experiment/downstream_task/force/digit_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t1_force_estimation 
  - _self_

ssl_name: vjepa
sensor: digit
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/force/gelsight_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: dino
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/force/gelsight_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: dinov2
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/force/gelsight_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: e2e
sensor: gelsight
ckpt_path: ~

trainer:
  save_probe_weights_only: false
  
task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true

```

### config/experiment/downstream_task/force/gelsight_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~ 
  - /wandb: ~
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: ijepa
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/force/gelsight_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~ 
  - /wandb: ~ 
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: mae
sensor: gelsight
ckpt_path: ~




```

### config/experiment/downstream_task/force/gelsight_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t1_force_estimation
  - _self_

ssl_name: vjepa
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2
      
task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/forcefield/digit_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit
  - /task: digit_forcefield
  - _self_

ssl_name: dino
sensor: digit
ckpt_path: ~

task_name: t1_forcefield
ssl_model_size: base
train_data_budget: 1.0
val_data_budget: 1.0
experiment_name: ${sensor}_${task_name}_${ssl_name}_vit${ssl_model_size}_bg
seed: 42

data_out_format: 'concat_ch_img'
num_frames: 2
frame_stride: 5

hydra:
  job:
    id: ${now:%Y.%m.%d}_${now:%H-%M}
  run:
    dir: ${paths.log_dir}/${hydra.job.id}_${experiment_name}
    
wandb:
  project: ${task_name}_${sensor}
  group: ~
  tags: ["${ssl_name}"]

trainer:
  max_epochs: 31
  validation_frequency: 2
  sanity_validate: false
  save_checkpoint_dir: ${paths.output_dir}/checkpoints
  checkpoint_interval_type: 'log'
  max_task_checkpoints: 10
  save_probe_weights_only: True
  limit_train_batches: 500
  limit_val_batches: 150

data:
  train_data_budget: ${train_data_budget}
  val_data_budget: ${val_data_budget}
  train_dataloader:
    batch_size: 20
    num_workers: 2
  val_dataloader:
    batch_size: 20
    num_workers: 2


test:
  data:
    dataset_name: ["005_tomato_soup_can/dataset_0"]
    batch_size: 1
  tester:
    _partial_: True
    _target_: tactile_ssl.test.TestForceField
  demo:
    _partial_: True
    _target_: tactile_ssl.test.DemoForceField
    digit_serial: "D20510"
    gelsight_device_id: ~
  path_outputs: ~


# DINO
task:
  _target_: tactile_ssl.downstream_task.ForceFieldModuleSL
  checkpoint_task: ~

  model_encoder:
    _target_: tactile_ssl.model.vit_${ssl_model_size}
    img_size: [224, 224]
    in_chans: 6
    pos_embed_fn: sinusoidal
    num_register_tokens: 1

  model_task:
    _target_: tactile_ssl.downstream_task.ForceFieldDecoderSL
    embed_dim: ${ssl_model_size}

  ssl_config:
    img_sz: [224, 224]
    pose_estimator:
      num_encoder_layers: 18
    loss:
      with_mask_supervision: false
      with_sl_supervision: false
      with_ssim: true
      disparity_smoothness: 1e-3
      min_depth: 0.1
      max_depth: 100.0

  checkpoint_encoder: ${paths.encoder_checkpoint_root}/${ssl_name}_vit${ssl_model_size}.ckpt
  train_encoder: false
  encoder_type: ${ssl_name}

  optim_cfg:
    _partial_: True 
    _target_: torch.optim.Adam
    lr: 0.0001

  scheduler_cfg: ~

```

### config/experiment/downstream_task/forcefield/digit_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit
  - /task: digit_forcefield
  - _self_

ssl_name: e2e
sensor: digit
ckpt_path: ~

task_name: t1_forcefield
ssl_model_size: base
train_data_budget: 1.0
val_data_budget: 1.0
experiment_name: ${sensor}_${task_name}_${ssl_name}_vit${ssl_model_size}_bg_e2e
seed: 42

data_out_format: 'concat_ch_img'
num_frames: 2
frame_stride: 5

hydra:
  job:
    id: ${now:%Y.%m.%d}_${now:%H-%M}
  run:
    dir: ${paths.log_dir}/${hydra.job.id}_${experiment_name}
    
wandb:
  project: ${task_name}_${sensor}
  group: ~
  tags: ["${ssl_name}"]

trainer:
  max_epochs: 31
  validation_frequency: 2
  sanity_validate: false
  save_checkpoint_dir: ${paths.output_dir}/checkpoints
  checkpoint_interval_type: 'log'
  max_task_checkpoints: 10
  save_probe_weights_only: True
  limit_train_batches: 500
  limit_val_batches: 150

data:
  train_data_budget: ${train_data_budget}
  val_data_budget: ${val_data_budget}
  train_dataloader:
    batch_size: 15
    num_workers: 2
  val_dataloader:
    batch_size: 15
    num_workers: 2


test:
  data:
    dataset_name: ["005_tomato_soup_can/dataset_4"]
    batch_size: 1
  tester:
    _partial_: True
    _target_: tactile_ssl.test.TestForceField
  demo:
    _partial_: True
    _target_: tactile_ssl.test.DemoForceField
  path_outputs: ~


task:
  _target_: tactile_ssl.downstream_task.ForceFieldModule
  checkpoint_task: ~

  model_encoder:
    _target_: tactile_ssl.model.vit_${ssl_model_size}
    img_size: [224, 224]
    in_chans: 6
    pos_embed_fn: sinusoidal
    num_register_tokens: 1

  model_task:
    _target_: tactile_ssl.downstream_task.ForceFieldDecoder
    embed_dim: ${ssl_model_size}

  ssl_config:
    img_sz: [224, 224]
    pose_estimator:
      num_encoder_layers: 18
    loss:
      with_mask_supervision: false
      with_sl_supervision: false
      with_ssim: true
      disparity_smoothness: 1e-3
      min_depth: 0.1
      max_depth: 100.0

  checkpoint_encoder: ~
  train_encoder: true
  encoder_type: ${ssl_name}

  optim_cfg:
    _partial_: True 
    _target_: torch.optim.Adam
    lr: 0.0001

  scheduler_cfg: ~

```

### config/experiment/downstream_task/forcefield/gelsight_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight
  - /task: digit_forcefield
  - _self_

ssl_name: dino
sensor: gelsight
ckpt_path: ~

task_name: t1_forcefield
ssl_model_size: base
train_data_budget: 1.0
val_data_budget: 1.0
experiment_name: ${sensor}_${task_name}_${ssl_name}_vit${ssl_model_size}_bg
seed: 42

data_out_format: 'concat_ch_img'
num_frames: 2
frame_stride: 5

hydra:
  job:
    id: ${now:%Y.%m.%d}_${now:%H-%M}
  run:
    dir: ${paths.log_dir}/${hydra.job.id}_${experiment_name}
    
wandb:
  project: ${task_name}_${sensor}
  group: ~
  tags: ["${ssl_name}"]

trainer:
  max_epochs: 21
  validation_frequency: 2
  sanity_validate: false
  save_checkpoint_dir: ${paths.output_dir}/checkpoints
  checkpoint_interval_type: 'log'
  max_task_checkpoints: 10
  save_probe_weights_only: True
  limit_train_batches: 500
  limit_val_batches: 150

data:
  train_data_budget: ${train_data_budget}
  val_data_budget: ${val_data_budget}
  train_dataloader:
    batch_size: 20
    num_workers: 2
  val_dataloader:
    batch_size: 20
    num_workers: 2

test:
  data:
    dataset_name: ["cookie2/dataset_0"]
    batch_size: 1
  tester:
    _partial_: True
    _target_: tactile_ssl.test.TestForceField
  demo:
    _partial_: True
    _target_: tactile_ssl.test.DemoForceField
    digit_serial: ~
    gelsight_device_id: 4
  path_outputs: ~


# DINO
task:
  _target_: tactile_ssl.downstream_task.ForceFieldModuleSL
  checkpoint_task: /media/chiguera/GUM/tactile_ssl/outputs_sparsh/digit_t1_forcefield_dino_vitbase_bg/checkpoints/epoch-0031.pth

  model_encoder:
    _target_: tactile_ssl.model.vit_${ssl_model_size}
    img_size: [224, 224]
    in_chans: 6
    pos_embed_fn: sinusoidal
    num_register_tokens: 1

  model_task:
    _target_: tactile_ssl.downstream_task.ForceFieldDecoderSL
    embed_dim: ${ssl_model_size}

  ssl_config:
    img_sz: [224, 224]
    pose_estimator:
      num_encoder_layers: 18
    loss:
      with_mask_supervision: false
      with_sl_supervision: false
      with_ssim: true
      disparity_smoothness: 1e-3
      min_depth: 0.1
      max_depth: 100.0

  checkpoint_encoder: ${paths.encoder_checkpoint_root}/${ssl_name}_vit${ssl_model_size}.ckpt
  train_encoder: false
  encoder_type: ${ssl_name}

  optim_cfg:
    _partial_: True 
    _target_: torch.optim.Adam
    lr: 0.0001

  scheduler_cfg: ~

```

### config/experiment/downstream_task/grasp/gelsight_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: dino
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/grasp/gelsight_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: dinov2
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/grasp/gelsight_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~ 
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: e2e
sensor: gelsight
ckpt_path: ~

trainer:
  save_probe_weights_only: false

task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true
  checkpoint_task: ~
```

### config/experiment/downstream_task/grasp/gelsight_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: ijepa
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/grasp/gelsight_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: mae
sensor: gelsight
ckpt_path: ~

task:
  model_encoder:
    num_register_tokens: 0


```

### config/experiment/downstream_task/grasp/gelsight_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_grasp
  - /task: t4_grasp_stability
  - _self_

ssl_name: vjepa
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/pose/digit_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: dino
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/pose/digit_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: dinov2
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/pose/digit_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~ 
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: e2e
sensor: digit
ckpt_path: ~

trainer:
  save_probe_weights_only: false

task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true
```

### config/experiment/downstream_task/pose/digit_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: ijepa
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/pose/digit_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: mae
sensor: digit
ckpt_path: ~

task:
  model_encoder:
    num_register_tokens: 0


```

### config/experiment/downstream_task/pose/digit_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_pose
  - /task: t3_pose_estimation
  - _self_

ssl_name: vjepa
sensor: digit
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/slip/digit_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t2_slip_detection
  - _self_

ssl_name: dino
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/slip/digit_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t2_slip_detection
  - _self_

ssl_name: dinov2
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/slip/digit_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~ 
  - /data: digit_force
  - /task: t2_slip_detection
  - _self_

ssl_name: e2e
sensor: digit
ckpt_path: ~

trainer:
  save_probe_weights_only: false
  
task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true
```

### config/experiment/downstream_task/slip/digit_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t2_slip_detection
  - _self_

ssl_name: ijepa
sensor: digit
ckpt_path: ~
```

### config/experiment/downstream_task/slip/digit_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t2_slip_detection
  - _self_

ssl_name: mae
sensor: digit
ckpt_path: ~

task:
  model_encoder:
    num_register_tokens: 0
```

### config/experiment/downstream_task/slip/digit_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: digit_force
  - /task: t2_slip_detection 
  - _self_

ssl_name: vjepa
sensor: digit
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/slip/gelsight_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: dino
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #N

test:
  data:
    dataset_name: ["sphere/batch_test"]
```

### config/experiment/downstream_task/slip/gelsight_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: dinov2
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #

test:
  data:
    dataset_name: ["sphere/batch_test"]
```

### config/experiment/downstream_task/slip/gelsight_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: e2e
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #N

test:
  data:
    dataset_name: ["sphere/batch_test"]

trainer:
  save_probe_weights_only: false
    
task: 
  model_encoder:
    num_register_tokens: 0
    
  checkpoint_encoder: ~
  train_encoder: true
  checkpoint_task: ~
```

### config/experiment/downstream_task/slip/gelsight_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~ 
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: ijepa
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #N

test:
  data:
    dataset_name: ["sphere/batch_test"]
```

### config/experiment/downstream_task/slip/gelsight_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: mae
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #N

test:
  data:
    dataset_name: ["sphere/batch_test"]
      
task:
  model_encoder:
    num_register_tokens: 0
```

### config/experiment/downstream_task/slip/gelsight_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_force
  - /task: t2_slip_detection
  - _self_

ssl_name: vjepa
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2
      
      list_datasets: [
          sphere/batch_1,
          sphere/batch_3,
          sphere/batch_4,
          sphere/batch_5,
          sphere/batch_6,
      ]
      list_datasets_test: [
          sphere/batch_test,
      ]
      max_delta_forceXYZ: [0.80, 0.80, 0.40] #N

test:
  data:
    dataset_name: ["sphere/batch_test"]

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/downstream_task/textile/gelsight_dino.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: dino
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/textile/gelsight_dinov2.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: dinov2
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/textile/gelsight_e2e.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~ 
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: e2e
sensor: gelsight
ckpt_path: ~

trainer:
  save_probe_weights_only: false

task: 
  model_encoder:
    num_register_tokens: 0 
    
  checkpoint_encoder: ~
  train_encoder: true
  checkpoint_task: /fsx-checkpoints/carohiguera/experiments/33922480_gelsight_t1_force_v2_e2e_vitbase_1.0/checkpoints/epoch-0012.pth
```

### config/experiment/downstream_task/textile/gelsight_ijepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: ijepa
sensor: gelsight
ckpt_path: ~
```

### config/experiment/downstream_task/textile/gelsight_mae.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: mae
sensor: gelsight
ckpt_path: ~

task:
  model_encoder:
    num_register_tokens: 0


```

### config/experiment/downstream_task/textile/gelsight_vjepa.yaml

```yaml
# @package _global_
defaults:
  - /paths: ~
  - /wandb: ~
  - /data: gelsight_textile
  - /task: t6_textile_classification
  - _self_

ssl_name: vjepa
sensor: gelsight
ckpt_path: ~

data:
  dataset:
    config:
      out_format: video
      num_frames: 4
      frame_stride: 2

task:
  model_encoder:
    in_chans: 3
    num_frames: 4

```

### config/experiment/ijepa_vit.yaml

```yaml
# @package _global_
defaults:
  - override /paths: ~
  - override /wandb: ~
  - override /data: vision_based
  - override /model: ijepa_vit
  - _self_

model_size: base
model_embed_dim: 768
experiment_name: sparsh_ijepa_vit${model_size}
ckpt_path: ~

wandb:
  project: sparsh_ijepa
  group: ijepa_vit${model_size}
  tags: ["vit${model_size}"]

trainer:
  max_epochs: 200

model:
  encoder:
    _target_: tactile_ssl.model.vit_${model_size}
    img_size: [320, 240]
    in_chans: 6
    pos_embed_fn: sinusoidal
  predictor:
    _target_: tactile_ssl.model.vit_predictor
    img_size: [320, 240]
    input_dim: ${model_embed_dim}
    embed_dim: 192
  optim_cfg:
    lr: 1e-3
    weight_decay: 0.04
    fused: True
  moving_average_decay: [0.996, 1.0]
  allow_mask_overlap: false

```

### config/experiment/mae_vit.yaml

```yaml
# @package _global_
defaults:
  - override /paths: ~
  - override /wandb: ~
  - override /data: vision_based
  - override /model: mae_vit
  - _self_

model_size: base
model_embed_dim: 768
experiment_name: sparsh_mae_vit${model_size}
ckpt_path: ~

wandb:
  project: sparsh_mae
  group: mae_vit${model_size}
  tags: ["vit${model_size}"]

trainer:
  max_epochs: 200

model:
  encoder:
    _target_: tactile_ssl.model.vit_${model_size}
    img_size: [320,240]
    in_chans: 6
    pos_embed_fn: sinusoidal
  decoder:
    in_chans: ${model.encoder.in_chans}
    embed_dim: 512
    depth: 8
    num_heads: 16

  optim_cfg:
    lr: 0.0001
    weight_decay: 0.05
  norm_pix_loss: false

```

### config/experiment/vjepa_vit.yaml

```yaml
# @package _global_
defaults:
  - override /paths: ~
  - override /wandb: ~
  - override /data: vision_based
  - override /model: vjepa_vit
  - _self_

model_size: base
model_embed_dim: 768
experiment_name: sparsh_vjepa_vit${model_size}
ckpt_path: ~
data_out_format: 'video' # ["video", "concat_ch_img"  "single_image"]
num_frames: 4 # num frames in input (for video and concat_ch_img format)
frame_stride: 2 # temporal stride between frames in input

wandb:
  project: sparsh_vjepa
  group: vjepa_vit${model_size}
  tags: ["vit${model_size}"]

trainer:
  max_epochs: 200

model:
  patch_size: 16
  num_frames: 4

  encoder:
    _target_: tactile_ssl.model.vit_${model_size}
  predictor:
    input_dim: ${model_embed_dim}
    num_heads: 12
    zero_init_mask_tokens: True

  optim_cfg:
    _target_: torch.optim.AdamW
    lr: 0.000625
    weight_decay: 0.04

  moving_average_decay: [0.997, 1.0]

  lr_scheduler_cfg:
    final_lr: 1.0e-6
    start_lr: 0.0002
    warmup_epochs: 40

  wd_scheduler_cfg:
    final_weight_decay: 0.4
    ref_weight_decay: 0.04

  loss_cfg:
    loss_exp: 1.0
    reg_coeff: 0.0


```

### config/model/dino_vit.yaml

```yaml
_target_: tactile_ssl.algorithm.DINOModule
encoder:
  _target_: tactile_ssl.model.vit_small
  img_size: 224
  in_chans: 3
  patch_size: 16
  num_register_tokens: 1
dino_head:
  _partial_: True
  _target_: tactile_ssl.model.layers.DINOHead
  out_dim: 65536

num_global_masks: 2
num_local_masks: 8
global_mask_scale: [0.48, 1.0]
local_mask_scale: [0.1, 0.48]
moving_average_decay: 0.998
allow_mask_overlap: True
teacher_temp: [0.04, 0.07]
teacher_warmup_epochs: 10

optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 1e-4
  weight_decay: 0.05

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 1e-5
  warmup_epochs: 30

wd_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  final_weight_decay: 0.4
  ref_weight_decay: 0.04
  T_max: ???

online_probes:
  - _target_: tactile_ssl.probe.OnlineProbeModule
    probe_name: 'reconstruction'
    decoder:
        _target_: tactile_ssl.probes.DecoderImage
        in_chans: 3
        patch_size: 16
        input_embed_dim: 768
        embed_dim: 192
        depth: 4
    loss_fn:
        _target_: torch.nn.MSELoss

online_probes_lrs: [1e-4]
log_freq_reconstruction: 100
```

### config/model/dinov2_vit.yaml

```yaml
_target_: tactile_ssl.algorithm.DINOv2Module
encoder:
  _target_: tactile_ssl.model.vit_small
  img_size: 224
  in_chans: 3
  patch_size: 16
  num_register_tokens: 1
  drop_path_rate: 0.1
  drop_path_uniform: True
  init_values: 1e-5 # Layerscale init values
dino_head:
  _partial_: True
  _target_: tactile_ssl.model.layers.DINOHead
  out_dim: 65536

num_global_masks: 2
num_local_masks: 8
global_mask_scale: [0.32, 1.0]
local_mask_scale: [0.1, 0.32]
moving_average_decay: 0.994
allow_mask_overlap: True
teacher_temp: [0.04, 0.06]
ibot_separate_head: True
teacher_warmup_epochs: 30

optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 1e-4
  weight_decay: 0.05

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 1e-5
  warmup_epochs: 30

wd_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  final_weight_decay: 0.4
  ref_weight_decay: 0.04
  T_max: ???

online_probes:
  - _target_: tactile_ssl.probe.OnlineProbeModule
    probe_name: 'reconstruction'
    decoder:
        _target_: tactile_ssl.probes.DecoderImage
        in_chans: 3
        patch_size: 16
        input_embed_dim: 768
        embed_dim: 192
        depth: 4
    loss_fn:
        _target_: torch.nn.MSELoss

online_probes_lrs: [1e-4]
log_freq_reconstruction: 1000

```

### config/model/ijepa_vit.yaml

```yaml
_target_: tactile_ssl.algorithm.IJEPAModule
encoder:
  _target_: tactile_ssl.model.vit_small
  img_size: 224
  in_chans: 3
  patch_size: 16
min_keep_num_patches: 10
aspect_ratio: [0.75, 1.5]
encoder_mask_scale: [0.85, 1.0]
predictor_mask_scale: [0.15, 0.2]
moving_average_decay: 0.996
reconstruction_log_freq: 500

predictor:
  _target_: tactile_ssl.model.vit_predictor
  input_dim: 384
  patch_size: 16
  embed_dim: 128
  pos_embed_fn: sinusoidal
optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 1e-3
  weight_decay: 1e-5

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 0.0002
  warmup_epochs: 30

wd_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  final_weight_decay: 0.4
  ref_weight_decay: 0.04
  T_max: ???

online_probes:
  - _target_: tactile_ssl.probe.OnlineProbeModule
    probe_name: 'reconstruction'
    decoder:
        _target_: tactile_ssl.probe.reconstruction.DecoderImage 
        in_chans: 6
        img_size: [320, 240]
        patch_size: 16
        input_embed_dim: ${model_embed_dim}
        embed_dim: 192
        depth: 4
    loss_fn:
        _target_: torch.nn.MSELoss

online_probes_lrs: [1e-4]

```

### config/model/mae_ret.yaml

```yaml
_target_: tactile_ssl.algorithm.ReskinMAEModule
urdf_path: ${paths.work_dir}/assets/metahand/meta_hand_right_digit.urdf
encoder:
  _target_: tactile_ssl.model.reskin_transformer.ret_small
  in_chans: 3
  sequence_length: ${int_multiply:${data.dataset.config.window_time}, ${data.dataset.config.interpolating_freq}}

mask_type: random #only supports random for now
mask_ratio: 0.75
norm_pix_loss: false
log_freq_reconstruction: 500

decoder:
  _partial_: True
  _target_: tactile_ssl.model.reskin_transformer.ret_mae_decoder
  embed_dim: 512
  depth: 8
  num_heads: 16

optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 5e-4
  weight_decay: 0.05

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 1e-5
  warmup_epochs: 30

wd_scheduler_cfg:
  ~
  # _partial_: True
  # _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  # final_weight_decay: 0.4
  # ref_weight_decay: 0.04
  # T_max: ???

```

### config/model/mae_vit.yaml

```yaml
_target_: tactile_ssl.algorithm.MAEModule
encoder:
  _target_: tactile_ssl.model.vit_small
  img_size: 224
  in_chans: 6
  patch_size: 16


mask_type: random #only supports random for now
mask_ratio: 0.75
norm_pix_loss: false
log_freq_reconstruction: 500

decoder:
  _partial_: True
  _target_: tactile_ssl.probe.reconstruction.MaskDecoderViT
  embed_dim: 192
  depth: 4
  num_heads: 8

optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 0.0001
  weight_decay: 0.05

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 1.0e-5
  warmup_epochs: 30

wd_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  final_weight_decay: 0.4
  ref_weight_decay: 0.04
  T_max: ???

```

### config/model/vjepa_vit.yaml

```yaml
_target_: tactile_ssl.algorithm.VJEPAModule

img_size: &img_size [320, 240]
patch_size: &patch_size 16
num_frames: &num_frames 4
tubelet_size: &tubelet_size 2
moving_average_decay: [0.998, 1.0]
reconstruction_log_freq: 500

encoder:
  _target_: tactile_ssl.model.vit_small
  img_size: *img_size
  in_chans: 3
  patch_size: *patch_size
  num_frames: *num_frames
  tubelet_size: *tubelet_size

predictor:
  _target_: tactile_ssl.model.vit_predictor
  img_size: *img_size
  num_mask_tokens: 2
  patch_size: *patch_size
  num_frames: *num_frames
  tubelet_size: *tubelet_size
  input_dim: ${model_embed_dim}
  num_heads: 6
  depth: 12
  embed_dim: 384
  pos_embed_fn: sinusoidal

optim_cfg:
  _partial_: True
  _target_: torch.optim.AdamW
  lr: 0.000625
  weight_decay: 0.04

lr_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.WarmupCosineScheduler
  steps_per_epoch: ???
  T_max: ???
  final_lr: 1.0e-6
  start_lr: 0.0002
  warmup_epochs: 40

wd_scheduler_cfg:
  _partial_: True
  _target_: tactile_ssl.model.custom_scheduler.CosineWDSchedule
  final_weight_decay: 0.4
  ref_weight_decay: 0.04
  T_max: ???



mask_cfg:
  - aspect_ratio: [0.75, 1.5]
    num_blocks: 8
    spatial_scale: [0.15, 0.15]
    temporal_scale: [1.0, 1.0]
    max_temporal_keep: 1.0
    max_keep: null
  - aspect_ratio: [0.75, 1.5]
    num_blocks: 2
    spatial_scale: [0.7, 0.7]
    temporal_scale: [1.0, 1.0]
    max_temporal_keep: 1.0
    max_keep: null

loss_cfg:
  loss_exp: 1.0
  reg_coeff: 1.0

online_probes:
  - _target_: tactile_ssl.probe.online_probe.OnlineProbeModule
    probe_name: 'reconstruction'
    decoder:
        _target_: tactile_ssl.probe.reconstruction.DecoderImage
        in_chans: 3
        img_size: *img_size
        patch_size: *patch_size
        num_frames: *num_frames
        tubelet_size: *tubelet_size
        input_embed_dim: ${model_embed_dim}
        embed_dim: 192
        depth: 4
    loss_fn:
        _target_: torch.nn.MSELoss

online_probes_lrs: [1e-4]

```

### config/paths/default.yaml

```yaml
data_root: /fsx-gum/shared/
encoder_checkpoint_root: /fsx-gum/shared/sparsh_models
log_dir: /fsx-gum/gum/experiments/
tacbench_dir: /fsx-gum/shared/tacbench/

output_dir: ${hydra:runtime.output_dir}
work_dir: ${hydra:runtime.cwd}


```

### config/paths/fair-aws-ch.yaml

```yaml
data_root: /fsx-gum/shared/
encoder_checkpoint_root: /fsx-gum/shared/sparsh_460k/
log_dir: /fsx-checkpoints/carohiguera/experiments/
tacbench_dir: /fsx-gum/carohiguera/tacbench/

output_dir: ${hydra:runtime.output_dir}
work_dir: ${hydra:runtime.cwd}
```

### config/paths/fair-aws.yaml

```yaml
data_root: /fsx-gum/shared/
encoder_checkpoint_root: /fsx-gum/shared/sparsh_models
log_dir: /fsx-gum/akashsharma02/experiments/
tacbench_dir: /fsx-gum/shared/tacbench/

output_dir: ${hydra:runtime.output_dir}
work_dir: ${hydra:runtime.cwd}

```

## Python signatures and reward/observation bodies (26 files)


### tactile_ssl/downstream_task/attentive_pooler.py

```
class AttentivePooler(Module)
    """Attentive Pooler"""
    def __init__(self, num_queries, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block)
    def _rescale_blocks(self)
    def _init_weights(self, m)
    def forward(self, x)
class AttentiveClassifier(Module)
    """Attentive Classifier"""
    def __init__(self, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, num_classes, complete_block)
    def forward(self, x)
```

### tactile_ssl/downstream_task/force_sl.py

```
class ForceLinearProbe(Module)
    def __init__(self, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block, with_last_activations)
    def forward(self, x)
class ForceSLModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type)
    def forward(self, x)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
```

### tactile_ssl/downstream_task/forcefield_sl.py

```
class ForceFieldDecoder(Module)
    def __init__(self, image_size, embed_dim, patch_size, resample_dim, norm_layer, hooks, reassemble_s)
    def forward(self, encoder_activations, mode)
class ForceFieldModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type, ssl_config)
    def register_hooks(self)
    def _get_layers_from_hooks(self)
    def forward(self, x, mode)
    def training_step(self, batch, batch_idx)
    def compute_sl_force(self, outputs, mask)
    def generate_images_pred(self, inputs, outputs)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
```

### tactile_ssl/downstream_task/grasp_sl.py

```
class GraspLinearProbe(Module)
    def __init__(self, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block)
    def forward(self, x)
class GraspSLModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type, weights_classes)
    def forward(self, x)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
```

### tactile_ssl/downstream_task/pose_sl.py

```
class PoseLinearProbe(Module)
    def __init__(self, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block, num_classes, num_input_fingers)
    def forward(self, x)
class PoseSLModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type, weights_classes_tx, weights_classes_ty, weights_classes_yaw, bins_translation, bins_rotation)
    def forward(self, inputs)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
```

### tactile_ssl/downstream_task/sl_module.py

```
class SLModule(Module, Module)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type)
    def load_task(self, checkpoint_task)
    def load_encoder(self, checkpoint_encoder)
    def forward(self, x)
    def training_step(self, batch, batch_idx)
    def validation_step(self)
    def test_step(self)
    def configure_optimizers(self, num_iterations_per_epoch, num_epochs)
```

### tactile_ssl/downstream_task/slip_decoders.py

```
class SlipProbe(Module)
    def __init__(self, attn_pool, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block, num_classes, dropout, with_force_input)
    def forward(self, inputs)
class SlipForceProbe(Module)
    def __init__(self, attn_pool, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block, num_classes, dropout)
    def forward(self, inputs)
```

### tactile_ssl/downstream_task/slip_sl.py

```
class SlipSLModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type, input_delta_force, predict_delta_force, weights_classes, add_batch_norm_probe)
    def forward(self, imgs, force)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
    def show_val_slip(self, trainer_instance)
    def show_val_forces(self, trainer_instance)
```

### tactile_ssl/downstream_task/textile_sl.py

```
class TextileLinearProbe(Module)
    def __init__(self, embed_dim, num_heads, mlp_ratio, depth, norm_layer, init_std, qkv_bias, complete_block, num_classes)
    def forward(self, x)
class TextileSLModule(SLModule)
    def __init__(self, model_encoder, model_task, optim_cfg, scheduler_cfg, checkpoint_encoder, checkpoint_task, train_encoder, encoder_type, weights_classes, class_labels)
    def forward(self, x)
    def training_step(self, batch, batch_idx)
    def validation_step(self, batch, batch_idx)
    def log_metrics(self, outputs, step, trainer_instance, label)
    def on_train_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_batch_end(self, outputs, batch, batch_idx, trainer_instance)
    def on_validation_epoch_end(self, trainer_instance)
```

### tactile_ssl/downstream_task/utils_forcefield/layers/Fusion.py

```
class ResidualConvUnit(Module)
    def __init__(self, features)
    def forward(self, x)
class Fusion(Module)
    def __init__(self, resample_dim)
    def forward(self, x, previous_stage)
```

### tactile_ssl/downstream_task/utils_forcefield/layers/Head.py

```
class Interpolate(Module)
    def __init__(self, scale_factor, mode, align_corners)
    def forward(self, x)
class ConvBlock(Module)
    """Layer to perform a convolution followed by ELU"""
    def __init__(self, in_channels, out_channels)
    def forward(self, x)
class Conv3x3(Module)
    """Layer to pad and convolve input"""
    def __init__(self, in_channels, out_channels, use_refl)
    def forward(self, x)
def upsample(x)
class NormalShearHead(Module)
    def __init__(self, features, use_skips)
    def forward(self, input_features, mode)
```

### tactile_ssl/downstream_task/utils_forcefield/layers/Reassemble.py

```
class Read_ignore(Module)
    def __init__(self, start_index)
    def forward(self, x)
class Read_add(Module)
    def __init__(self, start_index)
    def forward(self, x)
class Read_projection(Module)
    def __init__(self, in_features, start_index)
    def forward(self, x)
class MyConvTranspose2d(Module)
    def __init__(self, conv, output_size)
    def forward(self, x)
class Resample(Module)
    def __init__(self, p, s, h, emb_dim, resample_dim)
    def forward(self, x)
class Reassemble(Module)
    def __init__(self, image_size, read, p, s, emb_dim, resample_dim)
    def forward(self, x)
```

### tactile_ssl/downstream_task/utils_forcefield/pose_estimator/PoseEstimator.py

```
class PoseEstimator(Module)
    def __init__(self, num_encoder_layers, frame_ids)
    def forward(self, inputs)
```

### tactile_ssl/downstream_task/utils_forcefield/pose_estimator/pose_decoder.py

```
class PoseDecoder(Module)
    def __init__(self, num_ch_enc, num_input_features, num_frames_to_predict_for, stride)
    def forward(self, input_features)
```

### tactile_ssl/downstream_task/utils_forcefield/pose_estimator/resnet_encoder.py

```
class ResNetMultiImageInput(ResNet)
    """Constructs a resnet model with varying number of input images.
Adapted from https://github.com/pytorch/vision/blob/master/torchvision/models/resnet.py"""
    def __init__(self, block, layers, num_classes, num_input_images)
def resnet_multiimage_input(num_layers, pretrained, num_input_images)
class ResnetEncoder(Module)
    """Pytorch module for a resnet encoder"""
    def __init__(self, num_layers, pretrained, num_input_images)
    def forward(self, input_image)
```

### tactile_ssl/downstream_task/utils_forcefield/pose_estimator/utils.py

```
def transformation_from_parameters(axisangle, translation, invert)
def get_translation_matrix(translation_vector)
def rot_from_axisangle(vec)
```

### tactile_ssl/downstream_task/utils_forcefield/ssl_flow_loss.py

```
class SSL_loss(object)
    def __init__(self, config, frame_ids, ssim_loss)
    def compute_losses_normal(self, inputs, outputs)
    def get_smooth_loss(self, disp, img)
    def compute_reprojection_loss(self, pred, target)
    def compute_losses_shear(self, inputs, outputs)
    def compute_loss(self, inputs, outputs)
class SSIM(Module)
    """Layer to compute the SSIM loss between a pair of images"""
    def __init__(self)
    def forward(self, x, y)
```

### tactile_ssl/downstream_task/utils_forcefield/ssl_utils.py

```
def digit_intrinsics()
def warp(x, flo)
def robost_loss(im, im_warp, p, q, eps)
def gradient(data, stride)
def smooth_1st_loss(flow, image, alpha, smooth_edge_weighting)
class BackprojectDepth(Module)
    """Layer to transform a depth image into a point cloud"""
    def __init__(self, height, width)
    def forward(self, depth, inv_K)
class Project3D(Module)
    """Layer which projects 3D points into a camera with intrinsics K and at position T"""
    def __init__(self, height, width, eps)
    def forward(self, points, K, T)
def disp_to_depth(disp, min_depth, max_depth)
def plot_quiver(shear, normal, i_sample, spacing, margin)
def plot_quiver_img(img, shear, normal, mask, spacing, margin)
```

### tactile_ssl/model/pretrained.py

```
def resnet18()
def alexnet()
class AlexnetWrapper(Module)
    def __init__(self)
    def _register_hooks(self, layers)
    def get_intermediate_layers(self, x, layers)
    def forward(self, x)
```

### tactile_ssl/test/test_task.py

```
class TestTaskSL()
    def __init__(self, device, module)
    def set_test_params(self, task, sensor, ckpt, dataset_name, path_outputs, config)
    def run_model(self, dataset, dataloader)
    def get_overall_metrics(self, dataset, over_all_outputs)
    def make_plots(self, dataset, params)
    def make_video(self, dataset, params)
```

### tactile_ssl/trainer/trainer.py

```
class Trainer()
    def __init__(self, accelerator, strategy, devices, precision, plugins, callbacks, wandb_logger, max_epochs, max_steps, grad_accum_steps, grad_clip_norm, limit_train_batches, limit_val_batches, validation_frequency, sanity_validate, use_distributed_sampler, save_checkpoint_dir, checkpoint_frequency, log_frequency, checkpoint_interval_type, max_task_checkpoints, save_probe_weights_only)
    def fit(self, module, train_loader, val_loader, ckpt_path)
    def train_loop(self, module, optimizer, train_loader, limit_batches, scheduler_cfg, wd_scheduler_cfg)
    def val_loop(self, module, val_loader, limit_batches)
    def training_step(self, module, batch, batch_idx)
    def step_wd_scheduler(self, wd_scheduler_cfg, level, current_value)
    def step_scheduler(self, scheduler_cfg, level, current_value)
    def should_validate(self)
    def should_save(self)
    def should_log(self)
    def progbar_wrapper(self, iterable, total)
    def load(self, state, path)
    def save_checkpoint(self, state)
    def save_latest_checkpoint(self, state)
    def get_latest_checkpoint(checkpoint_dir)
    def _parse_optimizers_schedulers(self, configure_optim_output)
    def _format_iterable(prog_bar, candidates, prefix)
    def num_training_steps(self)
```

### test_task.py

```
def get_dataset_reskin(cfg)
def get_dataset_digit(cfg, dataset_name)
def get_test_dataset(cfg, dataset_name)
def test(cfg)
def main(cfg)
```

### train.py

```
def init_wandb(cfg)
def get_dataloaders_magnetic_based(cfg)
def get_dataloaders_vision_based(cfg)
def get_dataloaders(cfg)
def attempt_resume(cfg)
def train(cfg)
def main(cfg)
```

### train_task.py

```
def init_wandb(cfg)
def get_dataloader_reskin(cfg)
def get_dataloader_digit(cfg)
def get_dataloaders(cfg)
def attempt_resume(cfg)
def train(cfg)
def main(cfg)
```