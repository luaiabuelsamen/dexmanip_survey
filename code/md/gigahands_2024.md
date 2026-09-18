# gigahands_2024

source: https://github.com/brown-ivl/GigaHands


commit: 8ad3ef9a50157f44a7eef5645b0766362110a961


## README

<div align="center">
<h1> <b>[CVPR 2025 Highlight]</b> <br> GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities </h1>
<a href="https://ivl.cs.brown.edu/research/gigahands.html"><img src="https://img.shields.io/badge/Project_Page-green" alt="Project Page"></a>
<a href="https://www.arxiv.org/abs/2412.04244" target="_blank" rel="noopener noreferrer"> <img src="https://img.shields.io/badge/Paper-VGGT" alt="Paper PDF"></a>
<a href="https://ivl.cs.brown.edu/assets/images/projects/gigahands/gigahands_explain.mp4"> <img src="https://img.shields.io/badge/Demo-blue" alt="Demo"></a>

**[Brown IVL](https://ivl.cs.brown.edu/)**
<p>
    <a href="https://freddierao.github.io/">Rao Fu<sup>*</sup></a>
    ·
    <a href="https://kristen-z.github.io/">Dingxi Zhang<sup>*</sup></a>   
    ·
    <a href="https://www.alex-jiang.com/about/">Alex Jiang</a> 	 
    ·
    <a href="https://wanjia-fu.com/">Wanjia Fu</a>          
    ·
    <a href="https://austin-funk.github.io/">Austin Funk</a> 
    ·
    <a href="https://dritchie.github.io/">Daniel Ritchie</a> 
    ·
    <a href="https://cs.brown.edu/people/ssrinath/">Srinath Sridhar</a>
</p>

<img src="./assets/teaser.jpg" alt="[Teaser Figure]" style="zoom:80%;" />
</div>

## 📢 Updates

- [2025/09/04] For full **object poses**, access our Globus repository: [here](https://app.globus.org/file-manager?origin_id=625b46a5-022a-4908-a8bb-7f2b3e3b382c&origin_path=%2F). There are a total of 3.3k object motion sequences in 4 zip files ([zip 1](https://g-dc7fc0.56197.5898.data.globus.org/pose_jsons_round1_001.zip), [zip 2](https://g-dc7fc0.56197.5898.data.globus.org/pose_jsons_round1_002.zip), [zip 3](https://g-dc7fc0.56197.5898.data.globus.org/pose_jsons_round1_003.zip), [zip 4](https://g-dc7fc0.56197.5898.data.globus.org/pose_jsons_round1_004.zip)). Object meta annotation is provided [here](https://g-dc7fc0.56197.5898.data.globus.org/object_meta.zip). Please checkout the [README_object](README_object.md) for usage. 
- [2025/07/21] We provide [hand-object mesh visualizer](./render_mesh_video.py). The visualizer provides hand-object temporal alignment, and camera parameter usage. 

- [2025/07/09] For **object meshes**, you can download them [here](https://g-ad09a0.56197.5898.data.globus.org/scans_publish.zip). 

  We also provide smoother 3D hand poses that are aligned with the object coordinate system, derived from MANO parameters — available [here](https://g-ad09a0.56197.5898.data.globus.org/keypoints_3d_mano_align.tar.gz).
  Note: the previously provided `keypoints_3d_mano` were also generated from MANO parameters, but have been normalized and recentered to better support motion generation training.

- [2025/04/30] For **multiview RGB videos**, access our Globus repository: [here](https://app.globus.org/file-manager?origin_id=63bfc5ca-bb87-4633-b4b5-5e81b35fdbdf&origin_path=%2Fmultiview_rgb_vids%2F). Download each `.tar.gz` separately (contains 10 views per file, 51 camera views in total.)

- [2025/04/02] We are pleased to release our full **hand pose** dataset, available for download [here](https://g-ad09a0.56197.5898.data.globus.org/hand_poses.tar.gz) (Including all `keypoints_3d`,  `keypoints_3d_mano` and `params`). 

Complete **text annotation** are available [here](https://g-ad09a0.56197.5898.data.globus.org/annotations_v2.jsonl). We used the `rewritten_annotation` for model training. 

More data coming soon! 🔜

## 🗒️ Overview
Understanding bimanual human hand activities is a critical problem in AI and robotics. We cannot build large models of bimanual activities because existing datasets lack the scale, coverage of diverse hand activities, and detailed annotations. We introduce GigaHands, a massive annotated dataset capturing 34 hours of bimanual hand activities from **56 subjects** and **417 objects**, totaling **14k motion clips** derived from **183 million frames** paired with **84k text annotations**. Our markerless capture setup and data acquisition protocol enable fully automatic 3D hand and object estimation while minimizing the effort required for text annotation. The scale and diversity of GigaHands enable broad applications, including text-driven action synthesis, hand motion captioning, and dynamic radiance field reconstruction.

## 📂 Data Format

We store our dataset on [Globus](https://www.globus.org/). Access the raw data via [here](https://app.globus.org/file-manager?origin_id=63bfc5ca-bb87-4633-b4b5-5e81b35fdbdf&origin_path=%2F).
### Demo Data

You can download 1 demo sequence from [here](https://g-ad09a0.56197.5898.data.globus.org/gigahands_demo.tar.gz).
Or download 5 demo sequences from [here](https://g-ad09a0.56197.5898.data.globus.org/gigahands_demo_all.tar.gz). 

<summary>Directory Structure (Click to expand)</summary>

<details>
    ```text
    gigahands_demo/
    ├── hand_pose/
    │   ├── p<participant id>-<scene>-<squence id>/
    │   │   ├── bboxes/
    │   │   ├── keypoints_2d/
    │   │   ├── keypoints_3d/
    │   │   ├── keypoints_3d_mano/
    │   │   ├── mano_vid/
    │   │   ├── params/
    │   │   ├── rgb_vid/
    │   │   │   ├── brics-odroid-<camera id>-camx/
    │   │   │       ├── xxx.mp4
    │   │   │       ├── xxx.txt
    │   │   ├── repro_2d_vid/
    │   │   ├── repro_3d_vid/
    │   │   ├── optim_params.txt
    │   ├── ...
    └── object_pose/
        ├── p<participant id>-<scene>-<squence id>/
        │   ├── mesh/
        │   ├── pose/
        │   ├── render/
        │   ├── segmentation/
        ├── ...
</details>

### Whole Dataset

The dataset directory should look like this:

```python
./dataset/GigaHands/
├── multiview_rgb_vids/
    ├── p<participant id>-<scene>/
        ├── brics-odroid-<camera id>/
            ├── brics-odroid-<camera id>_<sequence 0 timestamp>.mp4
            ├── brics-odroid-<camera id>_<sequence 1 timestamp>.mp4
            ├── ...
├── hand_poses/
    ├── p<participant id>-<scene>/
        ├── keypoints_3d/				# 3D hand keypoints (triangulate multi-view 2D keypoints.)
        ├── keypoints_3d_mano/				# 3D hand keypoints (extract from mano parms and normalized, more smooth)
        ├── params/					# mano parameters
        ├── optim_params.txt				# camera parameters
├── object_poses/
    ├── <scene name>
        ├── <object name>
            ├── p<participant id>-<scene>_<squence id>/
                ├── pose				# object 6DoF poses
├── object_meta/                                        # all scanned and generated meshes
    ├── <scene name>
        ├── <object name>
    ├── scene_wise_round1
        ├── <scene name>_annotated_round1.csv           # annotation for object mesh occurance, tracking success <--> scene-sequence id

└── annotations_v2.jsonl 				# text annotations
└── instruction_script.json 			# original instruction for filming
└── multiview_camera_video_map.csv      # scene-sequence id <-> multiview rgb video id mapping
```
Downlod the multiview_rgb videos from [here](https://app.globus.org/file-manager?origin_id=63bfc5ca-bb87-4633-b4b5-5e81b35fdbdf&origin_path=%2Fmultiview_rgb_vids%2F), hand annotations and camera parameters from [here](https://g-ad09a0.56197.5898.data.globus.org/hand_poses.tar.gz), smoothed 3d hand keypoints from [here](https://g-ad09a0.56197.5898.data.globus.org/keypoints_3d_mano_align.tar.gz), object poses from [here](https://app.globus.org/file-manager?origin_id=625b46a5-022a-4908-a8bb-7f2b3e3b382c&origin_path=%2F), object mesh from [here](https://g-ad09a0.56197.5898.data.globus.org/scans_publish.zip), text annotations from [here](https://g-ad09a0.56197.5898.data.globus.org/annotations_v2.jsonl), the original instruction script grouped by scenario, scene, activity from [here](https://g-ad09a0.56197.5898.data.globus.org/instruction_script.json), scene-sequence mapping with video id meta file [here](https://g-852369.56197.5898.data.globus.org/multiview_camera_video_map.csv), object mesh mapping with scene-sequence id [here](https://g-dc7fc0.56197.5898.data.globus.org/object_meta.zip). 

## Installation

This code requires:

* Python 3.8+
* conda3 or miniconda3
* CUDA capable GPU (one is enough)

1. Create a virtual environment and install necessary dependencies

```shell
conda create -n gigahands python==3.8
conda activate gigahands
conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=12.1 -c pytorch -c nvidia
conda install -c conda-forge ffmpeg
pip install -r requirements.txt
```

3. Install EasyMocap

```shell
cd third-party/EasyMocap
python setup.py develop
```

4. Download [mano](https://mano.is.tue.mpg.de/download.php) models and place the `MANO_*.pkl` files under `body_models/smplh`.
5. Download the pretrained models by running `bash dataset/download_pretrained_models.sh`, which should be like:

```shell
./checkpoints/GigaHands/
./checkpoints/GigaHands/GPT/			# Text-to-motion generation model
./checkpoints/GigaHands/VQVAE/ 			# Motion autoencoder
./checkpoints/GigaHands/text_mot_match/		# Motion & Text feature extractors for evaluation
```

## 🎥 Visualizations

Example use of **hand pose and object pose annotation**: After downloading hand pose, object pose and object meshes, run the script below to **visualize hand-object mesh**. 

[▶ Video demo (MP4, 211k)](visualizations/17_instruments/p003-instrument_0033/output.mp4)
```bash
python render_mesh_video.py \
    --dataset_root <data_root_path> \
    --scene_name 17_instruments \
    --session_name p003-instrument \
    --seq_id 33 \
    --object_name ukelele_scan \
    --mesh_name ukelele-simplified1_1.obj \
    --render_camera brics-odroid-011_cam0 \
    --save_root visualizations

```

You will see videos of the rendered hand-object mesh in `visualizations` directory.
<img src='visualizations/17_instruments/p003-instrument_0033/output.gif' width=480>


Example use for **text-hand annotations**. Visualizer below is customized for training text-hand models. 

```bash
python visualize_hands.py
```

You will see videos of the MANO render results and reprojected keypoints in the `visualizations` directory.


Example use for **multi-view videos**. Visualizer below is customized for **multiview video loading**. 

```bash
python multiview_videoloader.py \
    --video_root_dir <your-path-to-multiview_rgb_vids> \
    --session <session name, i.e. p001-folder> \
    --seqid <sequence id, i.e. 17> \
    --out_dir <your-path-to-hand_poses (which contains optim_params.txt)>
```

You will see 3 concatenated frames from multi-views from targeted session and sequence id under the `visualizations` directory.


## 🚀 Inference - text2motion

Sampling results from customized descriptions:

```bash
python gen_motion_custom.py --resume-pth ./checkpoints/GigaHands/VQVAE/net_last.pth --resume-trans ./checkpoints/GigaHands/GPT/net_best_fid.pth --input-text ./input.txt
```

## 🏋️ Training - text2motion

The results are saved in the folder `output`.

**Training motion VQ-VAE**:

```bash
python3 train_vq_hand.py \
--batch-size 256 \
--lr 2e-4 \
--total-iter 300000 \
--lr-scheduler 200000 \
--nb-code 512 \
--down-t 2 \
--depth 3 \
--dilation-growth-rate 3 \
--out-dir output \
--dataname GigaHands \
--vq-act relu \
--quantizer ema_reset \
--loss-vel 0.5 \
--recons-loss l1_smooth \
--exp-name VQVAE \
--window-size 128
```

**Training T2M GPT model**:

```bash
python3 train_t2m_trans_hand.py  \
--exp-name GPT \
--batch-size 128 \
--num-layers 9 \
--embed-dim-gpt 1024 \
--nb-code 512 \
--n-head-gpt 16 \
--block-size 51 \
--ff-rate 4 \
--drop-out-rate 0.1 \
--resume-pth output/VQVAE/net_last.pth \
--vq-name VQVAE \
--out-dir output \
--total-iter 300000 \
--lr-scheduler 150000 \
--lr 0.0001 \
--dataname GigaHands \
--down-t 2 \
--depth 3 \
--quantizer ema_reset \
--eval-iter 10000 \
--pkeep 0.5 \
--dilation-growth-rate 3 \
--vq-act relu \
```

## Checklist

- [x] Release demo data
- [x] Release hand pose data
- [x] Release multi-view video data
- [x] Release object pose data (3.3k) and meshes
- [x] Release hand-object-motion and meshes correspondence file
- [x] Release inference code for text-to-motion task
- [x] Release training code for text-to-motion task

## Citation

If you find our work useful in your research, please cite:

```
@inproceedings{fu2025gigahands,
  title={Gigahands: A massive annotated dataset of bimanual hand activities},
  author={Fu, Rao and Zhang, Dingxi and Jiang, Alex and Fu, Wanjia and Funk, Austin and Ritchie, Daniel and Sridhar, Srinath},
  booktitle={Proceedings of the Computer Vision and Pattern Recognition Conference},
  pages={17461--17474},
  year={2025}
}
```

## Acknowledgement

We appreciate helps from :  

* Public code like [EasyMocap](https://github.com/zju3dv/EasyMocap), [text-to-motion](https://github.com/EricGuo5513/text-to-motion), [TM2T](https://github.com/EricGuo5513/TM2T), [MDM](https://github.com/GuyTevet/motion-diffusion-model), [T2M-GPT](https://github.com/Mael-zys/T2M-GPT) etc.
*  This research was supported by AFOSR grant FA9550-21 1-0214, NSF CAREER grant #2143576, and ONR DURIP grant N00014-23-1-2804. We would like to thank the Ope nAI Research Access Program for API support and extend our gratitude to Ellie Pavlick, Tianran Zhang, Carmen Yu, Angela Xing, Chandradeep Pokhariya, Sudarshan Harithas, Hongyu Li, Chaerin Min, Xindi Qu, Xiaoquan Liu, Hao Sun, Melvin He and Brandon Woodard.

## License

GigaHands is released under the Creative Commons Attribution-NonCommercial 4.0 International License.  See the [LICENSE](https://creativecommons.org/licenses/by-nc/4.0/) file for details.

[![CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)



## File tree (depth 3, assets pruned)

```
.gitignore
.gitmodules
README.md
README_object.md
body_models/
  J_regressor_mano_LEFT.txt
  J_regressor_mano_RIGHT.txt
dataset/
  dataset_hands.py
  download_pretrained_models.sh
  opt.txt
gen_motion_custom.py
glove/
  our_vocab_data.npy
  our_vocab_idx.pkl
  our_vocab_words.pkl
hand_utils/
  eval_trans_hand.py
  giga_mean_kp.npy
  giga_std_kp.npy
  utils/
    camera_utils.py
    easymocap_utils.py
    renderer.py
    rot.py
    video_handler.py
    visualizers.py
input.txt
models/
  encdec.py
  evaluator_wrapper.py
  modules.py
  pos_encoding.py
  quantize_cnn.py
  resnet.py
  rotation2xyz.py
  smpl.py
  t2m_trans.py
  vqvae.py
multiview_videoloader.py
options/
  get_eval_option.py
  option_transformer.py
  option_vq.py
render_mesh_video.py
requirements.txt
third-party/
  EasyMocap/
train_t2m_trans_hand.py
train_vq_hand.py
utils/
  camparam_utils.py
  config.py
  easymocap_utils.py
  eval_trans.py
  losses.py
  motion_process.py
  paramUtil.py
  quaternion.py
  rotation_conversions.py
  skeleton.py
  utils_model.py
  word_vectorizer.py
video_utils/
  cameras.py
  params.py
  parser.py
  reader_cpu.py
  tests.py
  video_handler.py
visualizations/
  17_instruments/
    p003-instrument_0033/
  multview_output/
    frame_0000.jpg
    frame_0001.jpg
    frame_0002.jpg
visualize_hands.py
```

## Config files (0)


## Python signatures and reward/observation bodies (13 files)


### dataset/dataset_hands.py

```
class GigaMotion(Dataset)
    def __init__(self, opt, mean, std, split, rep)
    def inv_transform(self, data)
    def __len__(self)
    def __getitem__(self, item)
class GigaTextMotionTrain(Dataset)
    def __init__(self, opt, w_vectorizer, codebook_size, split, augment_text, token_dir)
    def __len__(self)
    def __getitem__(self, item)
class GigaTextMotionEval(Dataset)
    def __init__(self, opt, mean, std, w_vectorizer, split, augment_text, rep)
    def __len__(self)
    def inv_transform(self, data)
    def __getitem__(self, item)
class GigaHands(Dataset)
    def __init__(self, opt, mode, split, rep, augment_text, codebook_size, w_vectorizer, token_dir)
    def __getitem__(self, item)
    def __len__(self)
def cycle(iterable)
```

### hand_utils/eval_trans_hand.py

```
def plot_hand_motion_kp(data, save_path, gt_data, title)
def evaluation_vqvae(out_dir, val_loader, net, logger, writer, nb_iter, best_fid, best_iter, best_div, best_top1, best_top2, best_top3, best_matching, eval_wrapper, draw, save, savegif, savenpy, mode)
def evaluation_transformer(out_dir, val_loader, net, trans, logger, writer, nb_iter, best_fid, best_iter, best_div, best_top1, best_top2, best_top3, best_matching, clip_model, eval_wrapper, draw, save, savegif, mode)
def evaluation_transformer_test(out_dir, val_loader, net, trans, logger, writer, nb_iter, best_fid, best_iter, best_div, best_top1, best_top2, best_top3, best_matching, best_multi, clip_model, eval_wrapper, draw, save, savegif, savenpy, mode)
def euclidean_distance_matrix(matrix1, matrix2)
def calculate_top_k(mat, top_k)
def calculate_R_precision(embedding1, embedding2, top_k, sum_all)
def calculate_multimodality(activation, multimodality_times)
def calculate_diversity(activation, diversity_times)
def calculate_frechet_distance(mu1, sigma1, mu2, sigma2, eps)
def calculate_activation_statistics(activations)
def calculate_frechet_feature_distance(feature_list1, feature_list2)
```

### hand_utils/utils/camera_utils.py

```
def qvec2rotmat(qvec)
def get_intr(param, undistort)
def get_rot_trans(param)
def get_extr(param)
def read_params(params_path)
def get_undistort_params(intr, dist, img_size)
def undistort_image(intr, dist_intr, dist, img)
def undistort_points(points, cameras)
```

### hand_utils/utils/easymocap_utils.py

```
def interpolate_vertices_and_colors(verts1, verts2, color_scheme1, color_scheme2, interpolation_factor)
def load_model(gender, use_cuda, model_type, skel_type, device, model_path)
def vis_smpl(args, vertices, faces, images, nf, cameras, colors, mode, extra_data, add_back, out_dir)
def vis_smpl_stack(args, vertices, faces, images, nf, cameras, mode, extra_data, out_dir, inter_factor)
def projectN3(kpts3d, cameras)
def vis_repro(args, images, kpts_repros, nf, config, to_img, mode, outdir, vis_id)
```

### hand_utils/utils/renderer.py

```
def get_colors(pid)
class Renderer(object)
    def __init__(self, focal_length, height, width, faces, bg_color, down_scale, extra_mesh)
    def add_light(self, scene)
    def render(self, render_data, cameras, images, use_white, add_back, ret_depth, ret_color)
    def _render_multiview(self, vertices, K, R, T, imglist, trackId, return_depth, return_color, bg_color, camera)
def render_results(img, render_data, cam_params, outname, rotate, degree, axis, fix_center)
```

### hand_utils/utils/rot.py

```
def get_rotmat_x(radians)
def get_rotmat_y(radians)
def get_rotmat_z(radians)
def axis_angle_to_rot6d(axis_angle)
def rot6d_to_axis_angle(rot6d)
def axis_angle_to_rotmat(axis_angle)
def quaternion_to_rotation_matrix(quat)
def rot6d_to_rotmat(x)
def rotmat_to_rot6d(x)
def rotation_matrix_to_angle_axis(rotation_matrix)
def quaternion_to_angle_axis(quaternion)
def rotation_matrix_to_quaternion(rotation_matrix, eps)
def axis_angle_to_quaternion(axis_angle)
def quaternion_raw_multiply(a, b)
def quaternion_apply(quaternion, point)
def quaternion_invert(quaternion)
```

### hand_utils/utils/video_handler.py

```
def frame_preprocess(path, undistort, intr, dist_intr, dist)
def create_video_writer(filename, frame_size, fps)
def add_text_to_frame(frame, text, position, font, font_scale, font_color, thickness)
def convert_video_ffmpeg(input_path)
```

### hand_utils/utils/visualizers.py

```
def read_params(params_path)
def get_projections(params, cam_names, n_Frames)
def parse_timestamp(filename)
def find_closest_video(folder, anchor_timestamp)
def plot_3d_hand_motion(motion, gt_motion, data_path, out_path, save_file, to_vis_mano, add_back, scene_path, camera_view, save_mesh, vis_3d_repro)
```

### train_vq_hand.py

```
def update_lr_warm_up(optimizer, nb_iter, warm_up_iter, lr)
```

### video_utils/video_handler.py

```
def frame_preprocess(path, undistort, intr, dist_intr, dist)
def create_video_writer(filename, frame_size, fps)
def convert_video_ffmpeg(input_path)
def render_multiview(view_batches, view_names_list, output_dir, grid_size, frame_size)
```