# arctic_2022

source: https://github.com/zc-alexfan/arctic


commit: 49f3eb4b7f01663172576357bb3d95695d7a7689


## README


## ARCTIC 🥶: A Dataset for Dexterous Bimanual Hand-Object Manipulation


<p align="center">
    <img src="docs/static/arctic-logo.svg" alt="Image" width="600" height="100" />
</p>

[ [Project Page](https://arctic.is.tue.mpg.de) ]
[ [Paper](https://download.is.tue.mpg.de/arctic/arctic_april_24.pdf) ]
[ [Video](https://www.youtube.com/watch?v=bvMm8gfFbZ8) ]
[ [Register ARCTIC Account](https://arctic.is.tue.mpg.de/register.php) ]
[ [ECCV'24 Competition](https://hands-workshop.org/challenge2024.html) ]
[ [Leaderboard](docs/leaderboard.md) ]


<p align="center">    
    <img src="docs/static/teaser.jpeg" alt="Image" width="100%"/>
</p>


This is a repository for preprocessing, splitting, visualizing, and rendering (RGB, depth, segmentation masks) the ARCTIC dataset.
Further, here, we provide code to reproduce our baseline models in our CVPR 2023 paper (Vancouver, British Columbia 🇨🇦) and developing custom models.

Our dataset contains heavily dexterous motion:

<p align="center">
    <img src="./docs/static/dexterous.gif" alt="Image" width="100%"/>
</p>

### News


> ✨3DV 2026: Looking for hand scans data? PALM is a large-scale dataset containing high-quality 13k registered 3dMD hand scans of 263 subjects and 90k calibrated multiview RGB images. See [PALM](https://github.com/facebookresearch/PALM) for details.
>
> <p align="center">
>     <img src="https://github.com/facebookresearch/PALM/blob/main/docs/static/dataset-teaser.jpg" alt="PALM Teaser" width="80%"/> 
> </p>

- 2024.11.27: Want to buy objects in real life? See [`docs/purchase.md`](docs/purchase.md)
- 2024.07.07: We host HANDS workshop at ECCV'24 to reconstruct hands and objects in ARCTIC without template. Join us [here](https://hands-workshop.org/challenge2024.html)
- 2023.12.20: MoCap can be downloaded now! See download [instructions](docs/data/README.md) and [visualization](docs/data/visualize.md).
- 2023.09.11: [ARCTIC leaderboard](https://arctic-leaderboard.is.tuebingen.mpg.de/) online!
- 2023.06.16: ICCV ARCTIC [challenge](https://sites.google.com/view/hands2023/home) starts!
- 2023.05.04: ARCTIC dataset with code for dataloaders, visualizers, models is officially announced (version 1.0)! 
- 2023.03.25: ARCTIC ☃️ dataset (version 0.1) is available! 🎉

Invited talks/posters at CVPR2023:
- [4D-HOI workshop: Keynote](https://4dhoi.github.io/)
- [Ego4D + EPIC workshop: Oral presentation](https://ego4d-data.org/workshops/cvpr23)
- [Rhobin workshop: Poster](https://rhobin-challenge.github.io/schedule.html)
- [3D scene understanding: Oral presentation](https://scene-understanding.com)

### Why use ARCTIC?

Summary on dataset:
- It contains 2.1M high-resolution images paired with annotated frames, enabling large-scale machine learning.
- Images are from 8x 3rd-person views and 1x egocentric view (for mixed-reality setting).
- It includes 3D groundtruth for SMPL-X, MANO, articulated objects.
- It is captured in a MoCap setup using 54 high-end Vicon cameras.
- It features highly dexterous bimanual manipulation motion (beyond quasi-static grasping).

Potential tasks with ARCTIC:
- Template-free bimanual [hand-object reconstruction](https://github.com/zc-alexfan/hold)
- Generating [hand grasp](https://korrawe.github.io/HALO/HALO.html) or [motion](https://github.com/cghezhang/ManipNet) with articulated objects
- Generating [full-body grasp](https://grab.is.tue.mpg.de/) or [motion](https://goal.is.tue.mpg.de/) with articulated objects
- Benchmarking performance of articulated object pose estimators from [depth images](https://articulated-pose.github.io/) with human in the scene
- Studying our [NEW tasks](https://download.is.tue.mpg.de/arctic/arctic_april_24.pdf) of consistent motion reconstruction and interaction field estimation
- Studying egocentric hand-object reconstruction
- Reconstructing [full-body with hands and articulated objects](https://3dlg-hcvc.github.io/3dhoi/) from RGB images

Check out our [project page](https://arctic.is.tue.mpg.de) for more details.

### Third-party ARCTIC resources

- [URDFs](https://github.com/zdchan/artigrasp/tree/main/rsc/arctic) for ARCTIC objects
- [Text description](https://github.com/JunukCha/Text2HOI?tab=readme-ov-file) for ARCTIC motions
- [Stable grasp](https://github.com/zhifanzhu/getagrip) labels on ARCTIC motions

### Projects that use ARCTIC

Reconstruction:

- [Get a Grip: Reconstructing Hand-Object Stable Grasps in Egocentric Videos](https://zhifanzhu.github.io/getagrip/)
- [3D Hand Pose Estimation in Egocentric Images in the Wild](https://ap229997.github.io/projects/hands/)
- [Mitigating Perspective Distortion-induced Shape Ambiguity in Image Crops](https://ap229997.github.io/projects/ambiguity/)
- [SMPLer-X: Scaling Up Expressive Human Pose and Shape Estimation](https://caizhongang.com/projects/SMPLer-X/)
- [Benchmarks and Challenges in Pose Estimation for Egocentric Hand Interactions with Objects](https://arxiv.org/abs/2403.16428)

Generation:

- [ArtiGrasp: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation](https://eth-ait.github.io/artigrasp/)
- [GeneOH Diffusion: Towards Generalizable Hand-Object Interaction Denoising via Denoising Diffusion](meowuu7.github.io/GeneOH-Diffusion)
- [Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction](https://github.com/JunukCha/Text2HOI)
- [QuasiSim: Parameterized Quasi-Physical Simulators for
Dexterous Manipulations Transfer](https://meowuu7.github.io/QuasiSim/)
- [InterHandGen: Two-Hand Interaction Generation via Cascaded Reverse Diffusion](https://jyunlee.github.io/projects/interhandgen/)

Create a pull request for missing projects.



### Features

<p align="center">
    <img src="./docs/static/viewer_demo.gif" alt="Image" width="80%"/>
</p>

- Instructions to download the ARCTIC dataset.
- Scripts to process our dataset and to build data splits.
- Rendering scripts to render our 3D data into RGB, depth, and segmentation masks.
- A viewer to interact with our dataset.
- Instructions to setup data, code, and environment to train our baselines.
- A generalized codebase to train, visualize and evaluate the results of ArcticNet and InterField for the ARCTIC benchmark.
- A viewer to interact with the prediction.



### Getting started

Get a copy of the code:
```bash
git clone https://github.com/zc-alexfan/arctic.git
```

- Setup environment: see [`docs/setup.md`](docs/setup.md)
- Download and visualize ARCTIC dataset: see [`docs/data/README.md`](docs/data/README.md)
- Training, evaluating for our ARCTIC baselines: see [`docs/model/README.md`](docs/model/README.md).
- Evaluation on test set: see [`docs/leaderboard.md`](docs/leaderboard.md)
- FAQ: see [`docs/faq.md`](docs/faq.md)
- Purchase real objects: see [`docs/purchase.md`](docs/purchase.md)

### License

See [LICENSE](LICENSE).

### Citation

```bibtex
@inproceedings{fan2023arctic,
  title = {{ARCTIC}: A Dataset for Dexterous Bimanual Hand-Object Manipulation},
  author = {Fan, Zicong and Taheri, Omid and Tzionas, Dimitrios and Kocabas, Muhammed and Kaufmann, Manuel and Black, Michael J. and Hilliges, Otmar},
  booktitle = {Proceedings IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2023}
}
```

Our paper benefits a lot from [aitviewer](https://github.com/eth-ait/aitviewer). If you find our viewer useful, to appreciate their hard work, consider citing:

```bibtex
@software{kaufmann_vechev_aitviewer_2022,
  author = {Kaufmann, Manuel and Vechev, Velko and Mylonopoulos, Dario},
  doi = {10.5281/zenodo.1234},
  month = {7},
  title = {{aitviewer}},
  url = {https://github.com/eth-ait/aitviewer},
  year = {2022}
}
```

### Acknowledgments

Constructing the ARCTIC dataset is a huge effort. The authors deeply thank: [Tsvetelina Alexiadis (TA)](https://ps.is.mpg.de/person/talexiadis) for trial coordination; [Markus Höschle (MH)](https://ps.is.mpg.de/person/mhoeschle), [Senya Polikovsky](https://is.mpg.de/person/senya), [Matvey Safroshkin](https://is.mpg.de/person/msafroshkin), [Tobias Bauch (TB)](https://www.linkedin.com/in/tobiasbauch/?originalSubdomain=de) for the capture setup; MH, TA and [Galina Henz](https://ps.is.mpg.de/person/ghenz) for data capture; [Priyanka Patel](https://ps.is.mpg.de/person/ppatel) for alignment; [Giorgio Becherini](https://ps.is.mpg.de/person/gbecherini) and [Nima Ghorbani](https://nghorbani.github.io/) for MoSh++; [Leyre Sánchez Vinuela](https://is.mpg.de/person/lsanchez), [Andres Camilo Mendoza Patino](https://ps.is.mpg.de/person/acmendoza), [Mustafa Alperen Ekinci](https://ps.is.mpg.de/person/mekinci) for data cleaning; TB for Vicon support; MH and [Jakob Reinhardt](https://ps.is.mpg.de/person/jreinhardt) for object scanning; [Taylor McConnell](https://ps.is.mpg.de/person/tmcconnell) for Vicon support, and data cleaning coordination; [Benjamin Pellkofer](https://ps.is.mpg.de/person/bpellkofer) for IT/web support; [Neelay Shah](https://ps.is.mpg.de/person/nshah), [Jean-Claude Passy](https://is.mpg.de/person/jpassy), [Valkyrie Felso](https://is.mpg.de/person/vfelso) for evaluation server. We also thank [Adrian Spurr](https://ait.ethz.ch/people/spurra/) and [Xu Chen](https://ait.ethz.ch/people/xu/) for insightful discussion. OT and DT were supported by the German Federal Ministry of Education and Research (BMBF): Tübingen AI Center, FKZ: 01IS18039B".


### Contact

For technical questions, please create an issue. For other questions, please contact `arctic@tue.mpg.de`.

Licensing: ARCTIC data and software are not available for commercial use.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zc-alexfan/arctic&type=Date)](https://star-history.com/#zc-alexfan/arctic&Date)


## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    stale.yml
.gitignore
LICENSE
Makefile
README.md
bash/
  clean_downloads.sh
  download_baselines.sh
  download_body_models.sh
  download_cropped_images.sh
  download_dry_run.sh
  download_feat.sh
  download_images.sh
  download_misc.sh
  download_mocap.sh
  download_splits.sh
common/
  .gitignore
  ___init___.py
  abstract_pl.py
  args_utils.py
  body_models.py
  camera.py
  comet_utils.py
  data_utils.py
  ld_utils.py
  list_utils.py
  mesh.py
  metrics.py
  np_utils.py
  object_tensors.py
  pl_utils.py
  rend_utils.py
  rot.py
  sys_utils.py
  thing.py
  torch_utils.py
  transforms.py
  viewer.py
  vis_utils.py
  xdict.py
requirements.txt
scripts_data/
  build_splits.py
  checksum.py
  crop_images.py
  download_data.py
  mocap_viewer.py
  process_seqs.py
  unzip_download.py
  visualizer.py
scripts_method/
  build_feat_split.py
  evaluate_metrics.py
  extract_predicts.py
  train.py
  visualizer.py
src/
  arctic/
    preprocess_dataset.py
    processing.py
    split.py
  callbacks/
    loss/
    process/
    vis/
  extraction/
    interface.py
    keys/
  factory.py
  mesh_loaders/
    arctic.py
    field.py
    pose.py
  models/
    __init__.py
    arctic_lstm/
    arctic_sf/
    field_lstm/
    field_sf/
    generic/
  nets/
    backbone/
    hand_heads/
    hmr_layer.py
    obj_heads/
    pointnet.py
  parsers/
    configs/
    generic_parser.py
    parser.py
  utils/
    const.py
    eval_modules.py
    interfield.py
    loss_modules.py
    mdev.py
```

## Config files (0)


## Python signatures and reward/observation bodies (17 files)


### scripts_method/train.py

```
def main(args)
```

### src/extraction/interface.py

```
def prepare_data(full_seq_name, exp_key, data_keys, layers, device, task, eval_p)
def fk_params_batch(batch, layers, device, flag)
def read_keys(gt_folder_p, folder_p, keys, verbose)
def save_results(out, out_dir)
def std_interface(out_list)
def fetch_dataset(args, seq)
def fetch_dataloader(args, seq)
```

### src/nets/hand_heads/hand_hmr.py

```
class HandHMR(Module)
    def __init__(self, feat_dim, is_rhand, n_iter)
    def init_vector_dict(self, features)
    def forward(self, features, use_pool)
```

### src/nets/hand_heads/mano_head.py

```
class MANOHead(Module)
    def __init__(self, is_rhand, focal_length, img_res)
    def forward(self, rotmat, shape, cam, K)
```