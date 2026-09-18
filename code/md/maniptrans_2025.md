# maniptrans_2025

source: https://github.com/ManipTrans/ManipTrans


commit: a3d08cfe3c3a5868a7f057533bcaf759c5af4705


## README

# ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
<div align="center">


<p><strong>Accepted to CVPR 2025</strong></p>

[Kailin Li](https://kailinli.top),
[Puhao Li](https://xiaoyao-li.github.io/),
[Tengyu Liu](https://tengyu.ai/),
[Yuyang Li](https://yuyangli.com/),
[Siyuan Huang](https://siyuanhuang.com/)

______________________________________________________________________
</div>


<p align="center">
    <a href="https://arxiv.org/abs/2503.21860">
        <img src='https://img.shields.io/badge/Paper-red?style=for-the-badge&labelColor=B31B1B&color=B31B1B' alt='Paper PDF'></a>
    <a href='https://maniptrans.github.io/'>
        <img src='https://img.shields.io/badge/Project-orange?style=for-the-badge&labelColor=D35400' alt='Project Page'></a>
    <a href='https://huggingface.co/datasets/LiKailin/DexManipNet'>
        <img src='https://img.shields.io/badge/Dataset-orange?style=for-the-badge&labelColor=FFD21E&color=FFD21E' alt='Dataset'></a>
    <!-- <a href=""><img alt="youtube views" src="https://img.shields.io/badge/Video-red?style=for-the-badge&logo=youtube&labelColor=ce4630&logoColor=red"/></a> -->
    
</p>

<!-- teaser image -->
<p align="center">
    <img src="assets/teaser.png" alt="teaser" width="100%">
</p>

## 📑 Table of Contents
1. [Installation](#Installation)
2. [Prerequisites](#Prerequisites)
3. [Usage](#usage)
4. [🤗 Extending to New Hand-Object Datasets 🤗](#extending-to-new-hand-object-datasets)
5. [🤗 Extending to New Dexterous Hand URDF Files 🤗](#extending-to-new-dexterous-hand-urdf-files)
6. [DexManipNet Dataset](#DexManipNet)
7. [Check out Our Paper](#check-out-our-paper)
8. [Acknowledgement](#acknowledgement)
9. [License](#license)

---

## 🛠️ Installation
<a id="Installation"></a>

<details>
<summary>Steps:</summary>

1. Clone the repository and initialize submodules:
    ```bash
    git clone https://github.com/ManipTrans/ManipTrans.git
    git submodule init && git submodule update
    ```
2. Create a virtual environment named `maniptrans` with Python 3.8. Note that IsaacGym only supports Python versions up to 3.8.
    ```bash
    conda create -y -n maniptrans python=3.8
    conda activate maniptrans
    pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
    ```
3. Download IsaacGym Preview 4 from the [official website](https://developer.nvidia.com/isaac-gym) and follow the installation instructions in the documentation. Test the installation by running an example script, such as `joint_monkey.py`, located in the `python/examples` directory.
4. Install additional dependencies.
    ```bash
    pip install git+https://github.com/ZhengyiLuo/smplx.git
    pip install git+https://github.com/KailinLi/bps_torch.git
    pip install fvcore~=0.1.5
    pip install --no-index --no-cache-dir pytorch3d==0.7.3 -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py38_cu117_pyt1131/download.html
    pip install -r requirements.txt
    pip install -e . # include the current directory in the Python path. Or use: `export PYTHONPATH=.:$PYTHONPATH`
    pip install numpy==1.23.5 # downgrade numpy to 1.23.5 to avoid compatibility issues
    ```

</details>

---

## 📋 Prerequisites
<a id="Prerequisites"></a>

<details>
<summary>Steps:</summary>

### Demo data for `Grab` dataset
1. For fair comparisons with [QuasiSim](https://github.com/Meowuu7/QuasiSim), we directly use the demo data from the official `Grab` dataset repository. Download it from the [official link](https://1drv.ms/f/s!AgSPtac7QUbHgVE5vMBOAUPzxxsV?e=B5V6mo) and extract it into the `data/grab_demo` directory.

2. Copy the demo URDF file `assets/obj_urdf_example.urdf` to `data/grab_demo/102/102_obj.urdf`.

3. The directory structure should look like this:
    ```
    data
    └── grab_demo
        └── 102
            ├── 102_obj.npy
            ├── 102_obj.obj
            ├── 102_obj.urdf
            ├── 102_sv_dict.npy
            └── 102_sv_dict_st_0_ed_108.npy
    ```

### `OakInk-V2` dataset
1. Download the OakInk-V2 dataset from its [official website](https://oakink.net/v2/) and extract it into the `data/OakInk-v2` directory. (You may skip downloading images; only annotated motion data is required.)

2. For each object mesh in `data/OakInk-v2/object_preview/align_ds`, generate the [COACD](https://github.com/SarahWeiii/CoACD) file by running:
    ```bash
    python maniptrans_envs/lib/utils/coacd_process.py -i data/OakInk-v2/object_preview/align_ds/xx/xx.obj -o data/OakInk-v2/coacd_object_preview/align_ds/xx/xx.obj --max-convex-hull 32 --seed 1 -mi 2000 -md 5 -t 0.07
    # Or, if you have the ply file, you can use:
    python maniptrans_envs/lib/utils/coacd_process.py -i data/OakInk-v2/object_preview/align_ds/xx/xx.ply -o data/OakInk-v2/coacd_object_preview/align_ds/xx/xx.ply --max-convex-hull 32 --seed 1 -mi 2000 -md 5 -t 0.07
    ```
3. For each generated COACD file in `data/OakInk-v2/coacd_object_preview/align_ds`, create a corresponding URDF file based on `assets/obj_urdf_example.urdf`.

4. Download the `body_upper_idx.pt` file from the [official website](https://oakink.net/v2/) and place it in the `data/smplx_extra` directory.

5. The directory structure should look like this:
    ```
    data
    ├── smplx_extra
    │   └── body_upper_idx.pt
    └── OakInk-v2
        ├── anno_preview
        ├── coacd_object_preview
        ├── data
        ├── object_preview
        └── program
    ```

### MISC
1. Download MANO model files from the [official website](https://mano.is.tue.mpg.de/) and extract them into the `data/mano_v1_2` directory.
2. Download the SMPL-X model files from the [official website](https://smpl-x.is.tue.mpg.de/) and extract them into the `data/body_utils/body_models` directory.

### Imitator Checkpoints
1. Download the pre-trained imitator checkpoints `imitator_ckp` from the [official website](https://huggingface.co/LiKailin/ManipTrans) and place them in the `assets` directory.

</details>

## ▶️ Usage
<a id="usage"></a>

### ✋ Training Single-Hand Policies

> **Note:** Due to licensing restrictions, we cannot provide some dexterous hand URDF files (e.g., `XHand` and `Inspire FTP`). If you have the required authorization from the respective robot companies, please contact us for configuration files.

1. **Preprocessing** (Optional but recommended)  
   Processes the trajectory to obtain a series of non-colliding, near-object states for reference state initialization (RSI), enhancing training stability and efficiency.

    ```bash
    # for Inspire Hand
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand inspire --headless --iter 2000
    ```

    <details>
    <summary>For other hands:</summary>

    ```bash
    # for Shadow Hand
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand shadow --headless --iter 3000
    # for Arti-Mano
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand artimano --headless --iter 2000
    # for Allegro Hand
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand allegro --headless --iter 4000
    # for XHand
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand xhand --headless --iter 3000
    # for Inspire FTP Hand
    python main/dataset/mano2dexhand.py --data_idx g0 --dexhand inspireftp --headless --iter 4000
    ```
    </details>


2. **Training**

    Use the following command to train single-hand policies:
    ```bash
    # for Inspire Hand
    python main/rl/train.py task=ResDexHand dexhand=inspire side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_inspire.pth lh_base_model_checkpoint=assets/imitator_lh_inspire.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_inspire
    ```

    <details>
    <summary>For other hands:</summary>

    ```bash
    # for Shadow Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=shadow side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_pid_rh_shadow.pth lh_base_model_checkpoint=assets/imitator_pid_lh_shadow.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 usePIDControl=True experiment=cross_g0_shadow_pid
    # for Arti-Mano (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=artimano side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_pid_rh_artimano.pth lh_base_model_checkpoint=assets/imitator_pid_lh_artimano.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 usePIDControl=True experiment=cross_g0_artimano_pid
    # for Allegro Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=allegro side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_pid_rh_allegro.pth lh_base_model_checkpoint=assets/imitator_pid_lh_allegro.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 usePIDControl=True experiment=cross_g0_allegro_pid
    # for XHand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=xhand side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_pid_rh_xhand.pth lh_base_model_checkpoint=assets/imitator_pid_lh_xhand.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 usePIDControl=True experiment=cross_g0_xhand_pid
    # for Inspire FTP Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=inspireftp side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_pid_rh_inspireftp.pth lh_base_model_checkpoint=assets/imitator_pid_lh_inspireftp.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 usePIDControl=True experiment=cross_g0_inspireftp_pid

    # for Shadow Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=shadow side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_shadow.pth lh_base_model_checkpoint=assets/imitator_lh_shadow.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_shadow
    # for Arti-Mano (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=artimano side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_artimano.pth lh_base_model_checkpoint=assets/imitator_lh_artimano.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_artimano
    # for Allegro Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=allegro side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_allegro.pth lh_base_model_checkpoint=assets/imitator_lh_allegro.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_allegro
    # for XHand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=xhand side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_xhand.pth lh_base_model_checkpoint=assets/imitator_lh_xhand.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_xhand
    # for Inspire FTP Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=inspireftp side=RH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true rh_base_model_checkpoint=assets/imitator_rh_inspireftp.pth lh_base_model_checkpoint=assets/imitator_lh_inspireftp.pth dataIndices=[g0] early_stop_epochs=100 actionsMovingAverage=0.4 experiment=cross_g0_inspireftp
    ```
    </details>

    The `early_stop_epochs` is dependent on the complexity of the task. For simple tasks, you can set it to 100, while for more complex tasks (e.g. cap the pen), you may largely increase it.
3. **Test**

    After training, test the model using the following command:

    ```bash
    # for Inspire Hand
    python main/rl/train.py task=ResDexHand dexhand=inspire side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_inspire.pth lh_base_model_checkpoint=assets/imitator_lh_inspire.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_inspire__xxxxxx/nn/cross_g0_inspire.pth
    ```

    <details>
    <summary>For other hands:</summary>

    ```bash
    # for Shadow Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=shadow side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_pid_rh_shadow.pth lh_base_model_checkpoint=assets/imitator_pid_lh_shadow.pth dataIndices=[g0] actionsMovingAverage=0.4 usePIDControl=True checkpoint=runs/cross_g0_shadow_pid__xxxxxx/nn/cross_g0_shadow_pid.pth
    # for Arti-Mano (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=artimano side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_pid_rh_artimano.pth lh_base_model_checkpoint=assets/imitator_pid_lh_artimano.pth dataIndices=[g0] actionsMovingAverage=0.4 usePIDControl=True checkpoint=runs/cross_g0_artimano_pid__xxxxxx/nn/cross_g0_artimano_pid.pth
    # for Allegro Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=allegro side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_pid_rh_allegro.pth lh_base_model_checkpoint=assets/imitator_pid_lh_allegro.pth dataIndices=[g0] actionsMovingAverage=0.4 usePIDControl=True checkpoint=runs/cross_g0_allegro_pid__xxxxxx/nn/cross_g0_allegro_pid.pth
    # for XHand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=xhand side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_pid_rh_xhand.pth lh_base_model_checkpoint=assets/imitator_pid_lh_xhand.pth dataIndices=[g0] actionsMovingAverage=0.4 usePIDControl=True checkpoint=runs/cross_g0_xhand_pid__xxxxxx/nn/cross_g0_xhand_pid.pth
    # for Inspire FTP Hand (with imitator in PID-controlled mode)
    python main/rl/train.py task=ResDexHand dexhand=inspireftp side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_pid_rh_inspireftp.pth lh_base_model_checkpoint=assets/imitator_pid_lh_inspireftp.pth dataIndices=[g0] actionsMovingAverage=0.4 usePIDControl=True checkpoint=runs/cross_g0_inspireftp_pid__xxxxxx/nn/cross_g0_inspireftp_pid.pth

    # for Shadow Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=shadow side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_shadow.pth lh_base_model_checkpoint=assets/imitator_lh_shadow.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_shadow__xxxxxx/nn/cross_g0_shadow.pth
    # for Arti-Mano (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=artimano side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_artimano.pth lh_base_model_checkpoint=assets/imitator_lh_artimano.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_artimano__xxxxxx/nn/cross_g0_artimano.pth
    # for Allegro Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=allegro side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_allegro.pth lh_base_model_checkpoint=assets/imitator_lh_allegro.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_allegro__xxxxxx/nn/cross_g0_allegro.pth
    # for XHand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=xhand side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_xhand.pth lh_base_model_checkpoint=assets/imitator_lh_xhand.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_xhand__xxxxxx/nn/cross_g0_xhand.pth
    # for Inspire FTP Hand (with imitator in 6D-Force mode)
    python main/rl/train.py task=ResDexHand dexhand=inspireftp side=RH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false rh_base_model_checkpoint=assets/imitator_rh_inspireftp.pth lh_base_model_checkpoint=assets/imitator_lh_inspireftp.pth dataIndices=[g0] actionsMovingAverage=0.4 checkpoint=runs/cross_g0_inspireftp__xxxxxx/nn/cross_g0_inspireftp.pth
    ```
    </details>

### 🤲 Training BiManual Policies

1. **Preprocessing**

    Preprocess data for both hands:
    ```bash
    # for Inspire Hand
    python main/dataset/mano2dexhand.py --data_idx 20aed@0 --side right --dexhand inspire --headless --iter 7000
    python main/dataset/mano2dexhand.py --data_idx 20aed@0 --side left --dexhand inspire --headless --iter 7000
    # for other hands, just replace `inspire` with the corresponding hand name
    ```
    Regarding `data_idx` of OakInk V2, for example, `20aed@0` refers to the primitive task indexed at `0` in the sequence labeled `scene_03__A004++seq__20aed35da30d4b869590__2023-04-22-18-45-27` (for simplification, we only use the first 5 digits of the hash code).

2. **Training**
  Train bi-manual policies:
    ```bash
    python main/rl/train.py task=ResDexHand dexhand=inspire side=BiH headless=true num_envs=4096 learning_rate=2e-4 test=false randomStateInit=true dataIndices=[20aed@0] rh_base_model_checkpoint=assets/imitator_rh_inspire.pth lh_base_model_checkpoint=assets/imitator_lh_inspire.pth early_stop_epochs=1000 actionsMovingAverage=0.4 experiment=cross_20aed@0_inspire
    ```
    Similar to single-hand training, the `early_stop_epochs` parameter can be adjusted based on the task complexity.

3. **Test**
  Test the bi-manual policy:
    ```bash
    python main/rl/train.py task=ResDexHand dexhand=inspire side=BiH headless=false num_envs=4 learning_rate=2e-4 test=true randomStateInit=false dataIndices=[20aed@0] rh_base_model_checkpoint=assets/imitator_rh_inspire.pth lh_base_model_checkpoint=assets/imitator_lh_inspire.pth actionsMovingAverage=0.4 checkpoint=runs/cross_20aed@0_inspire__xxxxxx/nn/cross_20aed@0_inspire.pth
    ```

---


## 🤗 Extending to New Hand-Object Datasets 🤗
<a id="extending-to-new-hand-object-datasets"></a>

We highly encourage researchers to transfer their hand-object datasets to dexterous hands using ManipTrans, contributing to the growth and development of the embodied AI community.

To facilitate this, we provide a straightforward interface to help you quickly adapt new datasets. Please refer to the examples in `main/dataset/grab_dataset_dexhand.py` and `main/dataset/oakink2_dataset_dexhand_rh.py`. It is worth mentioning that our codebase is designed for 60 FPS data. If your dataset has a lower or higher FPS, please preprocess your data; otherwise, the transfer effect may not be optimal. Please follow these steps:

1. Ensure your dataset's dataloader inherits from the `ManipData` class.  
2. Implement the `__getitem__` method in your dataloader. Ensure the returned dictionary includes the following keys:  
   - `'data_path'`  
   - `'obj_id'`  
   - `'obj_verts'`  
   - `'obj_urdf_path'`  
   - `'obj_trajectory'`  
   - `'wrist_pos'`  
   - `'wrist_rot'`  
   - `'mano_joints'`  
3. Add the handling logic for your dataset's index in the `dataset_type` function of `main/dataset/factory.py`.  

With these steps completed, you should be able to run ManipTrans on your dataset 🤗. If you encounter any issues, feel free to contact us for assistance.

---

## 🤗 Extending to New Dexterous Hand URDF Files 🤗
<a id="extending-to-new-dexterous-hand-urdf-files"></a>

We warmly welcome contributions from hardware engineers in the industry to adapt URDF files of their self-designed dexterous hands to ManipTrans. Such contributions are critical for advancing real-world dexterous manipulation applications.

To assist with this, we provide a simple interface that allows you to quickly adapt your dexterous hand URDF file. Please refer to the configuration files located in `maniptrans_envs/lib/envs/dexhands` and follow the steps below to create your own configuration:

1. Create a new configuration class that inherits from `DexHand`.  
2. Define the following essential variables in your configuration class:
   - `body_names` and `dof_names`: These should ideally follow the order from IsaacGym's definition.
   - `hand2dex_mapping`: This mapping is critical as it defines the correspondence between human hand keypoints and the joints of the dexterous hand.  
   - `contact_body_names`: The names of the body parts (e.g., fingertips) that are expected to interact with objects.  
   - `weight_idx`: A mapping of joint indices for different training weight levels:
     - `level_1_joints`: Critical joints, excluding the fingertips.  
     - `level_2_joints`: Other less-critical joints.  
   - `bone_links`: The finger connection sequence, used primarily for visualization purposes.  
   - `relative_rotation`: The rotation of the dexterous hand’s wrist relative to the MANO wrist, which needs manual adjustment.  
   - `relative_translation`: The translation of the dexterous hand’s wrist relative to the MANO wrist. If the wrist position in the URDF is at the origin, set `relative_translation` to `0`.  

After completing this configuration, you should be able to use ManipTrans with your custom-designed dexterous hand 🤗. If you encounter any issues, feel free to contact us for support. We also encourage you to share your URDF files with the community to help advance research and development in dexterous manipulation.

## 📦 `DexManipNet` Dataset
<a id="DexManipNet"></a>
<details>
<summary>Steps:</summary>

1. Download the `DexManipNet` dataset from the [official website](https://huggingface.co/datasets/LiKailin/DexManipNet) and extract it into the `data/dexmanipnet` directory.

2. For the OakInk V2 dataset, create a symbolic link from the `coacd_object_preview` directory to `data/dexmanipnet/dexmanipnet_oakinkv2/ObjURDF`, which is required for loading the URDF files. (Please refer to the [Prerequisites](#Prerequisites) section for details on generating the COACD files.)

    For the FAVOR dataset, we already provide the URDF files in `data/dexmanipnet/dexmanipnet_favor/ObjURDF`.

    After setup, your directory structure should resemble the following:
    ```
    dexmanipnet
    ├── dexmanipnet_favor
    │   ├── ObjURDF
    │   │   ├── OakInkObjectsV2
    │   │   └── OakInkVirtualObjectsV2
    │   └── sequences
    └── dexmanipnet_oakinkv2
        ├── oakinkv2_val_list.json
        ├── ObjURDF -> ../../OakInk-v2/coacd_object_preview
        │   ├── align_ds
        │   └── obj_desc.json
        └── sequences
    ```

3. To visualize the dataset, run the following example commands:
    ```bash
    # For FAVOR dataset:
    python DexManipNet/vis_dataset.py --idx 1093 --side rh --source favor

    # For OakInk V2 dataset:
    python DexManipNet/vis_dataset.py --idx 267 --side bih --source oakinkv2
    ```

    Detailed descriptions and task names can be found in the `seq_info.json` file within each sequence directory.

4. If you find our dataset `DexManipNet` helpful, please also consider citing OakInk V2 and FAVOR to acknowledge their contributions:
    <details>
    <summary>OakInk V2</summary>

    ```bibtex
        @inproceedings{zhan2024oakink2,
            title={Oakink2: A dataset of bimanual hands-object manipulation in complex task completion},
            author={Zhan, Xinyu and Yang, Lixin and Zhao, Yifei and Mao, Kangrui and Xu, Hanlin and Lin, Zenan and Li, Kailin and Lu, Cewu},
            booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
            year={2024}
        }
    ```
    </details>

    <details>
    <summary>FAVOR</summary>

    ```bibtex
        @inproceedings{li2024favor,
            title={FAVOR: Full-body ar-driven virtual object rearrangement guided by instruction text},
            author={Li, Kailin and Yang, Lixin and Lin, Zenan and Xu, Jian and Zhan, Xinyu and Zhao, Yifei and Zhu, Pengxiang and Kang, Wenxiong and Wu, Kejian and Lu, Cewu},
            booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
            year={2024}
        }
    ```
    </details>

</details>


## 📄 Check out Our Paper
<a id="check-out-our-paper"></a>
Our paper is posted on CVPR25. If you find our work useful, please consider citing us! 

```bibtex
  @inproceedings{li2025maniptrans,
    title={Maniptrans: Efficient dexterous bimanual manipulation transfer via residual learning},
    author={Li, Kailin and Li, Puhao and Liu, Tengyu and Li, Yuyang and Huang, Siyuan},
    booktitle={Proceedings of the Computer Vision and Pattern Recognition Conference},
    year={2025}
  }
```


## 🙏 Acknowledgement
<a id="acknowledgement"></a>
We thank [OakInk V2](https://oakink.net/v2/) for the dataloader and [Transic](https://transic-robot.github.io) for the training pipeline used in this work.


## 📜 License
<a id="license"></a>
This codebase is released under the [GPL v3 License](LICENSE).


## File tree (depth 3, assets pruned)

```
.gitignore
DexManipNet/
  __init__.py
  dexmanip_bih.py
  dexmanip_sh.py
  dexmanipnet.py
  dexmanipnet_favor.py
  dexmanipnet_oakinkv2.py
  get_val_seq.py
  vis_dataset.py
LICENSE
README.md
lib/
  __init__.py
  learn/
    __init__.py
    lightning.py
    lr_schedule.py
    optimizer_group.py
    policy/
  nn/
    __init__.py
    features/
    lipsnet.py
    mlp.py
  rl/
    __init__.py
    agent.py
    base.py
    models.py
    moving_avg.py
    network_builder.py
    network_builder_residual_bih.py
    network_builder_residual_sh.py
    player.py
    res_models.py
    runner.py
    sep_network_builder.py
  utils/
    __init__.py
    array.py
    config_utils.py
    datadict.py
    misc_utils.py
    reformat.py
    rlgames_utils.py
    torch_utils.py
    tree_utils.py
    utils.py
    wandb_utils.py
main/
  cfg/
    config.yaml
    rl_train/
    task/
  dataset/
    __init__.py
    base.py
    decorators.py
    factory.py
    grab_dataset_dexhand.py
    mano2dexhand.py
    oakink2_dataset_dexhand_lh.py
    oakink2_dataset_dexhand_rh.py
    oakink2_dataset_utils.py
    oakink2_layer/
    transform.py
  rl/
    train.py
maniptrans_envs/
  .gitignore
  LICENSE
  lib/
    __init__.py
    asset_root.py
    envs/
    utils/
  setup.py
requirements.txt
setup.py
```

## Config files (5)


### main/cfg/config.yaml

```yaml
# set default task and default training config based on task
defaults:
  - task: ???
  - rl_train: ${find_rl_train_config:${task}}
  - override hydra/job_logging: disabled
  - _self_

# Task name - used to pick the class to load
task_name: ${task.name}
# experiment name. defaults to name of training config
experiment: ''
side: 'Local'
bimanual_mode: united
dexhand: inspire
rh_base_model_checkpoint: assets/imitator_rh_inspire.pth
lh_base_model_checkpoint: assets/imitator_lh_inspire.pth

# if set to positive integer, overrides the default number of environments
num_envs: ''
rolloutStateInit: False
randomStateInit: True

rolloutLen: null
rolloutBegin: null

learning_rate: 5e-4
actionsMovingAverage: 1.0

usePIDControl: False

dataIndices: [7]

# seed - set to -1 to choose random seed
seed: 42
# set to True for deterministic performance
torch_deterministic: False

# set the maximum number of learning iterations to train for. overrides default per-environment setting
max_iterations: 9999999999999  # train forever
early_stop_epochs: 9999999999999

## Device config
#  'physx' or 'flex'
physics_engine: 'physx'
# whether to use cpu or gpu pipeline
pipeline: 'gpu'
# device for running physics simulation
sim_device: 'cuda:0'
# device to run RL
rl_device: 'cuda:0'
graphics_device_id: 0

## PhysX arguments
num_threads: 4 # Number of worker threads per scene used by PhysX - for CPU PhysX only.
solver_type: 1 # 0: pgs, 1: tgs
num_subscenes: 4 # Splits the simulation into N physics scenes and runs each one in a separate thread

# RLGames Arguments
# test - if set, run policy in inference mode (requires setting checkpoint to load)
test: False
# save rollouts config, used for distillation
save_rollouts: False
save_successful_rollouts_only: True
num_rollouts_to_save: 20000
num_rollouts_to_run: 9999999999999
min_episode_length: 20
# used to set checkpoint path
checkpoint: ''
from_ckpt_epoch: false
# set sigma when restoring network
sigma: ''
# set to True to use multi-gpu training
multi_gpu: False

wandb_activate: False
wandb_group: ''
wandb_name: ${rl_train.params.config.name}
wandb_entity: null  # set to your wandb entity if using wandb
wandb_project: null  # set to your wandb project if using wandb
wandb_tags: []
wandb_logcode_dir: '' 

capture_video: False
n_parallel_recorders: 8
n_successful_videos_to_record: 50
display: False
headless: True

# set the directory where the output files get saved
hydra:
  output_subdir: null
  run:
    dir: .

```

### main/cfg/rl_train/DexHandImitatorPPO.yaml

```yaml
params:
  seed: ${...seed}
  algo:
    name: ppo

  model:
    name: ${is_sep_model:${....bimanual_mode},my_continuous_a2c_logstd}

  network:
    name: ${is_sep_model:${....bimanual_mode},dict_obs_actor_critic}
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

    dict_feature_encoder:
      _target_: lib.nn.features.SimpleFeatureFusion
      extractors:
        privileged:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${eval:'13+${ndof:${.....dexhand}}*3'}}
        proprioception:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${ndof:${.....dexhand}}}
        target:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${eval:'3+3+3+4+4+3+3+(${nbody:${.....dexhand}}-1)*3*3'}}
      hidden_depth: 3
      hidden_dim: 512
      output_dim: 256
      activation: "swish"
      add_input_activation: false
      add_output_activation: false

    mlp:
      units: [256, 512, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load
  dexhand: ${...dexhand}

  config:
    name: ${resolve_default:DexHandImitator,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_input_excluded_keys: []
    normalize_value: True
    use_pid_control: ${....usePIDControl}
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: ${resolve_default:5e-4,${....learning_rate}}
    lr_schedule: adaptive
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 10000
    max_epochs: ${resolve_default:10000,${....max_iterations}}
    early_stop_epochs: ${resolve_default:500,${....early_stop_epochs}}
    save_best_after: 10
    save_frequency: 1000
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 1024
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
    use_soft_clamp: True

```

### main/cfg/rl_train/ResDexHandPPO.yaml

```yaml
params:
  seed: ${...seed}
  algo:
    name: ppo

  model:
    name: ${res_side:${....side},my_continuous_a2c_logstd}
    base_model_obs_shape:
      privileged: ${...base_privileged_dim}
      proprioception: ${...base_proprioception_dim}
      target: ${...base_target_dim}
    # base_model_checkpoint: ${..base_model_checkpoint}
    rh_base_model_checkpoint: ${..rh_base_model_checkpoint}
    lh_base_model_checkpoint: ${..lh_base_model_checkpoint}

  network:
    name: ${res_side:${....side},dict_obs_actor_critic}
    separate: False

    space:
      continuous:
        mu_activation: None
        sigma_activation: None
        mu_init:
          name: glorot_normal_initializer
          gain: 0.01
        sigma_init:
          name: const_initializer
          val: -1
        fixed_sigma: True

    dict_feature_encoder:
      _target_: lib.nn.features.SimpleFeatureFusion
      extractors:
        privileged:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${eval:'${.....base_privileged_dim}+13+5*4+3+1'}}
        proprioception:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${.....base_proprioception_dim}}
        target:
          _target_: lib.nn.features.Identity
          input_dim: ${is_united_model:${.......bimanual_mode},${.......side},${eval:'${.....base_target_dim}+3+3+3+4+4+3+3+${nbody:${.....dexhand}}+5+128'}}
      hidden_depth: 3
      hidden_dim: 512
      output_dim: 256
      activation: "swish"
      add_input_activation: false
      add_output_activation: false

    mlp:
      units: [256, 512, 128, 64]
      activation: elu
      d2rl: False

      initializer:
        name: default
      regularizer:
        name: None

    base_model:
      name: dict_obs_actor_critic
      # checkpoint: ${...base_model_checkpoint}
      rh_checkpoint: ${...rh_base_model_checkpoint}
      lh_checkpoint: ${...lh_base_model_checkpoint}
      separate: False
      action_size: ${eval:'6+${ndof:${...dexhand}}'}

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

      dict_feature_encoder:
        _target_: lib.nn.features.SimpleFeatureFusion
        extractors:
          privileged:
            _target_: lib.nn.features.Identity
            input_dim: ${......base_privileged_dim}
          proprioception:
            _target_: lib.nn.features.Identity
            input_dim: ${......base_proprioception_dim}
          target:
            _target_: lib.nn.features.Identity
            input_dim: ${......base_target_dim}
        hidden_depth: 3
        hidden_dim: 512
        output_dim: 256
        activation: "swish"
        add_input_activation: false
        add_output_activation: false

      mlp:
        units: [256, 512, 128, 64]
        activation: elu
        d2rl: False

        initializer:
          name: default
        regularizer:
          name: None

  load_checkpoint: ${if:${...checkpoint},True,False} # flag which sets whether to load the checkpoint
  load_path: ${...checkpoint} # path to the checkpoint to load
  # base_model_checkpoint: runs/ckpt/righthand_1030_final.pth
  rh_base_model_checkpoint: ${...rh_base_model_checkpoint}
  lh_base_model_checkpoint: ${...lh_base_model_checkpoint}
  dexhand: ${...dexhand}
  base_privileged_dim: ${ndof:${dexhand}}
  base_proprioception_dim: ${eval:'13+${ndof:${...dexhand}}*3'}
  base_target_dim: ${eval:'3+3+3+4+4+3+3+(${nbody:${...dexhand}}-1)*3*3'}


  config:
    name: ${resolve_default:ResDexHand,${....experiment}}
    full_experiment_name: ${.name}
    env_name: rlgpu
    multi_gpu: ${....multi_gpu}
    ppo: True
    mixed_precision: False
    normalize_input: True
    normalize_input_excluded_keys: []
    normalize_value: True
    use_pid_control: ${....usePIDControl}
    value_bootstrap: True
    num_actors: ${....task.env.numEnvs}
    reward_shaper:
      scale_value: 1.0
    normalize_advantage: True
    gamma: 0.99
    tau: 0.95
    learning_rate: ${resolve_default:5e-4,${....learning_rate}}
    lr_schedule: warmup
    warmup_steps: 10
    schedule_type: standard
    kl_threshold: 0.008
    score_to_win: 10000
    max_epochs: ${resolve_default:10000,${....max_iterations}}
    early_stop_epochs: ${resolve_default:500,${....early_stop_epochs}}
    save_best_after: 2
    save_frequency: 100
    print_stats: True
    grad_norm: 1.0
    entropy_coef: 0.0
    truncate_grads: True
    e_clip: 0.2
    horizon_length: 32
    minibatch_size: 1024
    mini_epochs: 5
    critic_coef: 4
    clip_value: True
    seq_len: 4
    bounds_loss_coef: 0.0001
    use_soft_clamp: True
    mix_ratio: 0.5

```

### main/cfg/task/DexHandImitator.yaml

```yaml
# used to create the object
name: ${concat:DexHandImitator,${..side}}

physics_engine: ${..physics_engine}
seed: ${..seed}

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:8192,${...num_envs}}
  dexhand: ${...dexhand}

  episodeLength: 2000
  training: ${if:${...test},False,True}

  usePIDControl: ${...usePIDControl}

  rolloutStateInit: ${resolve_default:False,${...rolloutStateInit}}
  randomStateInit: ${resolve_default:True,${...randomStateInit}}

  dataIndices: ${resolve_default:[],${...dataIndices}}
  obsFutureLength: 1

  clipObservations: 5.0
  clipActions: 1.0

  furniture: just_one_leg

  frankaDofNoise: 0.25

  targetLiftHeight: 0.05
  distanceReward: 0.1
  liftReward: 1.0
  successReward: 1.0

  aggregateMode: 3

  tightenMethod: "exp_decay"
  tightenFactor: 0.7 # 1.0 means no tightening restriction
  tightenSteps: 128000

  actionScale: 1.0
  useQuatRot: false

  # for distillation
  propDumpInfo:
    q: ${ndof:${....dexhand}}
    dq: ${ndof:${....dexhand}}
    base_state: 13

  actionsMovingAverage: ${...actionsMovingAverage}
  translationScale: 1.0
  orientationScale: 0.1
  bimanual_mode: ${...bimanual_mode}

  propObsDim: ${is_both_hands:${eval:'13+${ndof:${...dexhand}}*3'},${...side}}
  obsKeys:
    - q
    - cos_q
    - sin_q
    - base_state

  privilegedObsDim: ${is_both_hands:${eval:'${ndof:${...dexhand}}'},${...side}}
  privilegedObsKeys:
    - dq


  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 1
    contact_offset: 0.005
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 1024*1024
    num_subscenes: ${....num_subscenes}
    contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: False
  randomization_params:
    frequency: 1
    sim_params:
      gravity:
        range: [ 0, 0.4 ]
        operation: "additive"
        distribution: "uniform"
        schedule: "linear"
        schedule_steps: 100000000
    actor_params:
      franka:
        color: True
        rigid_body_properties:
          mass:
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True
            schedule: "linear"
            schedule_steps: 100000000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.7, 1.3 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
        dof_properties:
          lower:
            range: [ 1.0, 1.010050167084168 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"
            schedule_steps: 100000000
          upper:
            range: [ 1.0, 1.010050167084168 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"
            schedule_steps: 100000000
          stiffness:
            range: [ 1.0, 1.010050167084168 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"
            schedule_steps: 100000000
          damping:
            range: [ 1.0, 1.010050167084168 ]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"
            schedule_steps: 100000000
      table:
        color: True
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
      leg:
        color: True
        scale:
          range: [0.9, 1.1]
          operation: "scaling"
          distribution: "uniform"
          setup_only: True
          schedule: "linear"
          schedule_steps: 100000000
        rigid_body_properties:
          mass:
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            setup_only: True
            schedule: "linear"
            schedule_steps: 100000000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
          rolling_friction:
            num_buckets: 250
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
          torsion_friction:
            num_buckets: 250
            range: [ 0.5, 1.5 ]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
          restitution:
            range: [0.0, 1.0]
            operation: "additive"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000
          compliance:
            range: [0.0, 1.0]
            operation: "additive"
            distribution: "uniform"
            schedule: "linear"
            schedule_steps: 100000000

```

### main/cfg/task/ResDexHand.yaml

```yaml
# used to create the object
name: ${concat:ResDexHand,${..side}}

physics_engine: ${..physics_engine}
seed: ${..seed}

# if given, will override the device setting in gym.
env:
  numEnvs: ${resolve_default:8192,${...num_envs}}
  dexhand: ${...dexhand}

  episodeLength: 1200
  training: ${if:${...test},False,True}

  usePIDControl: ${...usePIDControl}

  rolloutStateInit: ${resolve_default:False,${...rolloutStateInit}}
  randomStateInit: ${resolve_default:True,${...randomStateInit}}

  dataIndices: ${resolve_default:[],${...dataIndices}}
  obsFutureLength: 1

  rolloutLen: ${resolve_default:None,${...rolloutLen}}
  rolloutBegin: ${resolve_default:None,${...rolloutBegin}}

  clipObservations: 5.0
  clipActions: 1.0

  furniture: just_one_leg

  frankaDofNoise: 0.25

  targetLiftHeight: 0.05
  distanceReward: 0.1
  liftReward: 1.0
  successReward: 1.0

  aggregateMode: 3

  tightenMethod: "exp_decay"
  tightenFactor: 0.7 # 1.0 means no tightening restriction
  tightenSteps: 3200

  actionScale: 1.0
  useQuatRot: false

  # for distillation
  propDumpInfo:
    q_rh: ${ndof:${....dexhand}}
    q_lh: ${ndof:${....dexhand}}
    dq_rh: ${ndof:${....dexhand}}
    dq_lh: ${ndof:${....dexhand}}
    state_rh: 13
    state_lh: 13
    state_manip_obj_rh: 13
    state_manip_obj_lh: 13
    joint_state_rh: ${eval:'${nbody:${....dexhand}}*13'}
    joint_state_lh: ${eval:'${nbody:${....dexhand}}*13'}
    tip_force_rh: 15 # todo four fingers
    tip_force_lh: 15
    reward: 1

  actionsMovingAverage: ${...actionsMovingAverage}
  translationScale: 1.0
  orientationScale: 0.1
  bimanual_mode: ${...bimanual_mode}

  propObsDim: ${is_both_hands:${eval:'13+${ndof:${...dexhand}}*3'},${...side}}
  obsKeys:
    - q
    - cos_q
    - sin_q
    - base_state

  privilegedObsDim: ${is_both_hands:${eval:'${ndof:${...dexhand}}+13+5*4+3+1'},${...side}}
  privilegedObsKeys:
    - dq # must be the first element
    - manip_obj_pos
    - manip_obj_quat
    - manip_obj_vel
    - manip_obj_ang_vel
    - tip_force
    - manip_obj_com
    - manip_obj_weight


  # set to True if you use camera sensors in the environment
  enableCameraSensors: False

sim:
  dt: 0.0166667 # 1/60
  substeps: 2
  up_axis: "z"
  use_gpu_pipeline: ${eq:${...pipeline},"gpu"}
  gravity: [0.0, 0.0, -9.81]
  physx:
    num_threads: ${....num_threads}
    solver_type: ${....solver_type}
    use_gpu: ${contains:"cuda",${....sim_device}} # set to False to run on CPU
    num_position_iterations: 8
    num_velocity_iterations: 1
    contact_offset: 0.005
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
    max_gpu_contact_pairs: 1048576 # 2**22
    num_subscenes: ${....num_subscenes}
    contact_collection: 1 # 0: CC_NEVER (don't collect contact info), 1: CC_LAST_SUBSTEP (collect only contacts on last substep), 2: CC_ALL_SUBSTEPS (broken - do not use!)

task:
  randomize: ${if:${...test},False,True}
  randomization_params:
    frequency: 32
    sim_params:
      gravity:
        operation: "scaling"
        schedule: "linear_decay"
        schedule_steps: 1920
        external_sample:
          type: "const_scale"
          init_value: 0
    actor_params:
      manip_obj:
        color: True
        rigid_shape_properties:
          friction:
            num_buckets: 250
            operation: "scaling"
            schedule: "linear_decay"
            schedule_steps: 1920
            external_sample:
              type: "const_scale"
              init_value: 3
              upper_bound: 6.0
              lower_bound: 1.0
      manip_obj_rh:
        color: True
        rigid_shape_properties:
          friction:
            num_buckets: 250
            operation: "scaling"
            schedule: "linear_decay"
            schedule_steps: 1920
            external_sample:
              type: "const_scale"
              init_value: 3
              upper_bound: 6.0
              lower_bound: 1.0
      manip_obj_lh:
        color: True
        rigid_shape_properties:
          friction:
            num_buckets: 250
            operation: "scaling"
            schedule: "linear_decay"
            schedule_steps: 1920
            external_sample:
              type: "const_scale"
              init_value: 3
              upper_bound: 6.0
              lower_bound: 1.0
```

## Python signatures and reward/observation bodies (40 files)


### lib/learn/policy/base.py

```
class BasePolicy(ABC, LightningModule)
    def forward(self)
    def act(self)
```

### lib/learn/policy/distributions.py

```
class Categorical(Categorical)
    """Mostly interface changes, add mode() function, no real difference from Categorical"""
    def mode(self)
    def imitation_loss(self, actions, reduction)
    def imitation_accuracy(self, actions, mask, reduction, scale_100)
    def random_actions(self)
class CategoricalHead(Module)
    def forward(self, x)
class CategoricalNet(Module)
    def __init__(self, input_dim)
    def forward(self, x)
class MixtureOfGaussian()
    def __init__(self, logits, means, scales, min_std, low_noise_eval)
    def mode(self)
    def imitation_loss(self, actions, reduction)
    def imitation_accuracy(self, actions, mask, reduction)
class GMMHead(Module)
    def __init__(self, input_dim)
    def forward(self, x)
    def action_dim(self)
def _build_mlp_distribution_net(input_dim)
def classify_accuracy(output, target, topk, mask, reduction, scale_100)
```

### lib/utils/config_utils.py

```
def is_sequence(obj)
def is_mapping(obj)
def omegaconf_to_dict(cfg, resolve, enum_to_str)
```

### main/dataset/grab_dataset_dexhand.py

```
def dump_obj_mesh(filename, vertices, faces)
class GrabDemoDexHand(ManipData)
    def __init__(self)
    def __len__(self)
    def __getitem__(self, idx)
```

### main/dataset/mano2dexhand.py

```
def pack_data(data, dexhand)
def soft_clamp(x, lower, upper)
class Mano2Dexhand()
    def __init__(self, args, dexhand, obj_urdf_path)
    def set_force_vis(self, env_ptr, part_k, has_force)
    def fitting(self, max_iter, obj_trajectory, target_wrist_pos, target_wrist_rot, target_mano_joints)
```

### main/dataset/oakink2_dataset_dexhand_lh.py

```
class OakInk2DatasetDexHandLH(ManipData)
    def __init__(self)
    def __getitem__(self, index)
```

### main/dataset/oakink2_dataset_dexhand_rh.py

```
class OakInk2DatasetDexHandRH(ManipData)
    def __init__(self)
    def __getitem__(self, index)
```

### main/rl/train.py

```
def preprocess_train_config(cfg, config_dict)
def launch_rlg_hydra(cfg)
```

### maniptrans_envs/lib/__init__.py

```
def omegaconf_to_dict(d)
def _get_rlgames_env_creator(task_config, task_name, sim_device, rl_device, graphics_device_id, display, record, has_headless_arg, headless, multi_gpu, post_create_hook)
def make()
```

### maniptrans_envs/lib/envs/core/sim_config.py

```
"""Define additional parameters based on real-world config for simulator."""
def default_asset_options()
```

### maniptrans_envs/lib/envs/core/vec_task.py

```
def _create_sim_once(gym)
def save_getattr(obj, attr)
class Env(ABC)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, display, record, headless)
    def allocate_buffers(self)
    def step(self, actions)
    def reset(self)
    def reset_idx(self, env_ids)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
def get_external_sample(attr_randomization_params)
class VecTask(Env)
    def __init__(self, config, rl_device, sim_device, graphics_device_id, display, record, headless)
    def _set_renderers(self, display)
    def set_camera(self)
    def create_camera()
    def set_viewer(self)
    def allocate_buffers(self)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def get_state(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def step(self, actions)
    def zero_actions(self)
    def reset_idx(self, env_idx)
    def reset(self)
    def reset_done(self)
    def render(self, mode)
    def __parse_sim_params(self, physics_engine, config_sim)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)

```python
def observation_space(self) -> gym.Space:
        """Get the environment's observation space."""
        return self.obs_space
```
```

### maniptrans_envs/lib/envs/dexhands/allegro.py

```
class Allegro(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class AllegroRH(Allegro)
    def __init__(self)
    def __str__(self)
class AllegroLH(Allegro)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/dexhands/artimano.py

```
class Artimano(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class ArtimanoRH(Artimano)
    def __init__(self)
    def __str__(self)
class ArtimanoLH(Artimano)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/dexhands/base.py

```
class DexHand(ABC)
    def __init__(self)
    def __str__(self)
    def to_dex(self, hand_body)
    def to_hand(self, dex_body)
    def n_dofs(self)
    def n_bodies(self)
    def urdf_path(self)
    def reverse_mapping(mapping)
```

### maniptrans_envs/lib/envs/dexhands/decorators.py

```
def register_dexhand(dexhand_type)
```

### maniptrans_envs/lib/envs/dexhands/factory.py

```
class DexHandFactory()
    def register(cls, dexhand_type, hand_class)
    def create_hand(cls, dexhand_type, side)
    def auto_register_hands(cls, directory, base_package)
```

### maniptrans_envs/lib/envs/dexhands/inspire.py

```
class Inspire(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class InspireRH(Inspire)
    def __init__(self)
    def __str__(self)
class InspireLH(Inspire)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/dexhands/inspireftp.py

```
class InspireFTP(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class InspireFTPRH(InspireFTP)
    def __init__(self)
    def __str__(self)
class InspireFTPLH(InspireFTP)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/dexhands/shadow.py

```
class Shadow(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class ShadowRH(Shadow)
    def __init__(self)
    def __str__(self)
class ShadowLH(Shadow)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/dexhands/xhand.py

```
class Xhand(DexHand, ABC)
    def __init__(self)
    def __str__(self)
class XhandRH(Xhand)
    def __init__(self)
    def __str__(self)
class XhandLH(Xhand)
    def __init__(self)
    def __str__(self)
```

### maniptrans_envs/lib/envs/tasks/dexhandimitator.py

```
def soft_clamp(x, lower, upper)
class DexHandImitatorRHEnv(VecTask)
    def __init__(self, cfg)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self)
    def init_data(self)
    def pack_data(self, data)
    def allocate_buffers(self)
    def _update_states(self)
    def _refresh(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def _reset_default(self, env_ids)
    def reset_idx(self, env_ids)
    def reset_done(self)
    def step(self, actions)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def create_camera(self)
    def set_force_vis(self, env_ptr, part_k, has_force)
def quat_to_angle_axis(q)
def compute_imitation_reward(reset_buf, progress_buf, running_progress_buf, actions, states, target_states, max_length, scale_factor, dexhand_weight_idx)
class DexHandImitatorLHEnv(DexHandImitatorRHEnv)
    def __init__(self, cfg)

```python
def compute_imitation_reward(
    reset_buf: Tensor,
    progress_buf: Tensor,
    running_progress_buf: Tensor,
    actions: Tensor,
    states: Dict[str, Tensor],
    target_states: Dict[str, Tensor],
    max_length: List[int],
    scale_factor: float,
    dexhand_weight_idx: Dict[str, List[int]],
) -> Tuple[Tensor, Tensor, Tensor, Tensor]:

    # type: (Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor], Dict[str, Tensor], Tensor, float, Dict[str, List[int]]) -> Tuple[Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor]]

    # end effector pose reward
    current_eef_pos = states["base_state"][:, :3]
    current_eef_quat = states["base_state"][:, 3:7]

    target_eef_pos = target_states["wrist_pos"]
    target_eef_quat = target_states["wrist_quat"]
    diff_eef_pos = target_eef_pos - current_eef_pos
    diff_eef_pos_dist = torch.norm(diff_eef_pos, dim=-1)

    current_eef_vel = states["base_state"][:, 7:10]
    current_eef_ang_vel = states["base_state"][:, 10:13]
    target_eef_vel = target_states["wrist_vel"]
    target_eef_ang_vel = target_states["wrist_ang_vel"]

    diff_eef_vel = target_eef_vel - current_eef_vel
    diff_eef_ang_vel = target_eef_ang_vel - current_eef_ang_vel

    joints_pos = states["joints_state"][:, 1:, :3]
    target_joints_pos = target_states["joints_pos"]
    diff_joints_pos = target_joints_pos - joints_pos
    diff_joints_pos_dist = torch.norm(diff_joints_pos, dim=-1)

    # ? assign different weights to different joints
    diff_thumb_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["thumb_tip"]]].mean(dim=-1)
    diff_index_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["index_tip"]]].mean(dim=-1)
    diff_middle_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["middle_tip"]]].mean(dim=-1)
    diff_ring_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["ring_tip"]]].mean(dim=-1)
    diff_pinky_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["pinky_tip"]]].mean(dim=-1)
    diff_level_1_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_1_joints"]]].mean(dim=-1)
    diff_level_2_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_2_joints"]]].mean(dim=-1)

    joints_vel = states["joints_state"][:, 1:, 7:10]
    target_joints_vel = target_states["joints_vel"]
    diff_joints_vel = target_joints_vel - joints_vel

    reward_eef_pos = torch.exp(-40 * diff_eef_pos_dist)
    reward_thumb_tip_pos = torch.exp(-100 * diff_thumb_tip_pos_dist)
    reward_index_tip_pos = torch.exp(-90 * diff_index_tip_pos_dist)
    reward_middle_tip_pos = torch.exp(-80 * diff_middle_tip_pos_dist)
    reward_pinky_tip_pos = torch.exp(-60 * diff_pinky_tip_pos_dist)
    reward_ring_tip_pos = torch.exp(-60 * diff_ring_tip_pos_dist)
    reward_level_1_pos = torch.exp(-50 * diff_level_1_pos_dist)
    reward_level_2_pos = torch.exp(-40 * diff_level_2_pos_dist)

    reward_eef_vel = torch.exp(-1 * diff_eef_vel.abs().mean(dim=-1))
    reward_eef_ang_vel = torch.exp(-1 * diff_eef_ang_vel.abs().mean(dim=-1))
    reward_joints_vel = torch.exp(-1 * diff_joints_vel.abs().mean(dim=-1).mean(-1))

    current_dof_pos = states["q"]
    current_dof_vel = states["dq"]

    diff_eef_rot = quat_mul(target_eef_quat, quat_conjugate(current_eef_quat))
    diff_eef_rot_angle = quat_to_angle_axis(diff_eef_rot)[0]
    reward_eef_rot = torch.exp(-1 * (diff_eef_rot_angle).abs())

    reward_power = torch.exp(-10 * target_states["power"])
    reward_wrist_power = torch.exp(-2 * target_states["wrist_power"])

    error_buf = (
        (torch.norm(current_eef_vel, dim=-1) > 100)
        | (torch.norm(current_eef_ang_vel, dim=-1) > 200)
        | (torch.norm(joints_vel, dim=-1).mean(-1) > 100)
        | (torch.abs(current_dof_vel).mean(-1) > 200)
    )  # sanity check

    failed_execute = (
        (
            (diff_thumb_tip_pos_dist > 0.04 / 0.7 * scale_factor)
            | (dif
```

```python
def compute_reward(self, actions):
        target_state = {}
        max_length = torch.clip(self.demo_data["seq_len"], 0, self.max_episode_length).float()
        cur_idx = self.progress_buf
        cur_wrist_pos = self.demo_data["wrist_pos"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_pos"] = cur_wrist_pos
        cur_wrist_rot = self.demo_data["wrist_rot"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_quat"] = aa_to_quat(cur_wrist_rot)[:, [1, 2, 3, 0]]

        target_state["wrist_vel"] = self.demo_data["wrist_velocity"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_ang_vel"] = self.demo_data["wrist_angular_velocity"][torch.arange(self.num_envs), cur_idx]

        cur_joints_pos = self.demo_data["mano_joints"][torch.arange(self.num_envs), cur_idx]
        target_state["joints_pos"] = cur_joints_pos.reshape(self.num_envs, -1, 3)
        target_state["joints_vel"] = self.demo_data["mano_joints_velocity"][
            torch.arange(self.num_envs), cur_idx
        ].reshape(self.num_envs, -1, 3)

        power = torch.abs(torch.multiply(self.dof_force, self.states["dq"])).sum(dim=-1)
        target_state["power"] = power

        wrist_power = torch.abs(
            torch.sum(
                self.apply_forces[:, self.dexhand_handles[self.dexhand.to_dex("wrist")[0]], :]
                * self.states["base_state"][:, 7:10],
                dim=-1,
            )
        )  # ? linear force * linear velocity
        wrist_power += torch.abs(
            torch.sum(
                self.apply_torque[:, self.dexhand_handles[self.dexhand.to_dex("wrist")[0]], :]
                * self.states["base_state"][:, 10:],
                dim=-1,
            )
        )  # ? torque * angular velocity
        target_state["wrist_power"] = wrist_power

        if self.training:
            last_step = self.gym.get_frame_count(self.sim)
            if self.tighten_method == "None":
                scale_factor = 1.0
            elif self.tighten_method == "const":
                scale_factor = self.tighten_factor
            elif self.tighten_method == "linear_decay":
                scale_factor = 1 - (1 - self.tighten_factor) / self.tighten_steps * min(last_step, self.tighten_steps)
            elif self.tighten_method == "exp_decay":
                scale_factor = (np.e * 2) ** (-1 * last_step / self.tighten_steps) * (
                    1 - self.tighten_factor
                ) + self.tighten_factor
            elif self.tighten_method == "cos":
                scale_factor = (self.tighten_factor) + np.abs(
                    -1 * (1 - self.tighten_factor) * np.cos(last_step / self.tighten_steps * np.pi)
                ) * (2 ** (-1 * last_step / self.tighten_steps))
            else:
                scale_factor = 1.0
        else:
            scale_factor = 1.0

        assert not self.headless or isinstance(compute_imitation_reward, torch.jit.ScriptFunction)

        self.rew_buf[:], self.reset_buf[:], self.success_buf[:], self.failure_buf[:], self.reward_dict = (
            compute_imitation_reward(
                self.reset_buf,
                self.progress_buf,
                self.running_progress_buf,
                self.actions,
                self.states,
                target_state,
                max_length,
                scale_factor,
                self.dexhand.weight_idx,
            )
        )
        self.total_rew_buf += self.rew_buf
```

```python
def compute_observations(self):
        self._refresh()
        # obs_keys: q, cos_q, sin_q, base_state
        obs_values = []
        for ob in self._obs_keys:
            if ob == "base_state":
                obs_values.append(
                    torch.cat([torch.zeros_like(self.states[ob][:, :3]), self.states[ob][:, 3:]], dim=-1)
                )  # ! ignore base position
            else:
                obs_values.append(self.states[ob])
        self.obs_dict["proprioception"][:] = torch.cat(obs_values, dim=-1)
        # privileged_obs_keys: dq, manip_obj_pos, manip_obj_quat, manip_obj_vel, manip_obj_ang_vel
        if len(self._privileged_obs_keys) > 0:
            pri_obs_values = []
            for ob in self._privileged_obs_keys:
                if ob == "manip_obj_pos":
                    pri_obs_values.append(self.states[ob] - self.states["base_state"][:, :3])
                elif ob == "manip_obj_com":
                    cur_com_pos = (
                        quat_to_rotmat(self.states["manip_obj_quat"][:, [1, 2, 3, 0]])
                        @ self.manip_obj_com.unsqueeze(-1)
                    ).squeeze(-1) + self.states["manip_obj_pos"]
                    pri_obs_values.append(cur_com_pos - self.states["base_state"][:, :3])
                elif ob == "manip_obj_weight":
                    prop = self.gym.get_sim_params(self.sim)
                    pri_obs_values.append((self.manip_obj_mass * -1 * prop.gravity.z).unsqueeze(-1))
                elif ob == "tip_force":
                    tip_force = torch.stack(
                        [self.net_cf[:, self.dexhand_handles[k], :] for k in self.dexhand.contact_body_names],
                        axis=1,
                    )
                    tip_force = torch.cat(
                        [tip_force, torch.norm(tip_force, dim=-1, keepdim=True)], dim=-1
                    )  # add force magnitude
                    pri_obs_values.append(tip_force.reshape(self.num_envs, -1))
                else:
                    pri_obs_values.append(self.states[ob])
            self.obs_dict["privileged"][:] = torch.cat(pri_obs_values, dim=-1)

        next_target_state = {}

        cur_idx = self.progress_buf + 1
        cur_idx = torch.clamp(cur_idx, torch.zeros_like(self.demo_data["seq_len"]), self.demo_data["seq_len"] - 1)

        cur_idx = torch.stack(
            [cur_idx + t for t in range(self.obs_future_length)], dim=-1
        )  # [B, K], K = obs_future_length
        nE, nT = self.demo_data["wrist_pos"].shape[:2]
        nF = self.obs_future_length

        def indicing(data, idx):
            assert data.shape[0] == nE and data.shape[1] == nT
            remaining_shape = data.shape[2:]
            expanded_idx = idx
            for _ in remaining_shape:
                expanded_idx = expanded_idx.unsqueeze(-1)
            expanded_idx = expanded_idx.expand(-1, -1, *remaining_shape)
            return torch.gather(data, 1, expanded_idx)

        target_wrist_pos = indicing(self.demo_data["wrist_pos"], cur_idx)  # [B, K, 3]
        cur_wrist_pos = self.states["base_state"][:, :3]  # [B, 3]
        next_target_state["delta_wrist_pos"] = (target_wrist_pos - cur_wrist_pos[:, None]).reshape(nE, -1)

        target_wrist_vel = indicing(self.demo_data["wrist_velocity"], cur_idx)
        cur_wrist_vel = self.states["base_state"][:, 7:10]
        next_target_state["wrist_vel"] = target_wrist_vel.reshape(nE, -1)
        next_target_state["delta_wrist_vel"] = (target_wrist_vel - cur_wrist_vel[:, None]).reshape(nE, -1)

  
```

### maniptrans_envs/lib/envs/tasks/dexhandmanip_bih.py

```
def soft_clamp(x, lower, upper)
class DexHandManipBiHEnv(VecTask)
    def __init__(self, cfg)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self)
    def init_data(self)
    def pack_data(self, data, side)
    def allocate_buffers(self)
    def _create_obj_assets(self, i, side)
    def _create_obj_actor(self, env_ptr, i, current_asset, side)
    def _update_states(self)
    def _refresh(self)
    def compute_reward(self, actions)
    def compute_reward_side(self, actions, side)
    def compute_observations(self)
    def compute_observations_side(self, side)
    def _reset_default(self, env_ids)
    def _reset_default_side(self, env_ids, seq_idx, side)
    def reset_idx(self, env_ids)
    def reset_done(self)
    def step(self, actions)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def create_camera(self)
    def set_force_vis(self, env_ptr, part_k, has_force, side)
def quat_to_angle_axis(q)
def compute_imitation_reward(reset_buf, progress_buf, running_progress_buf, actions, states, target_states, max_length, scale_factor, dexhand_weight_idx)

```python
def compute_imitation_reward(
    reset_buf: Tensor,
    progress_buf: Tensor,
    running_progress_buf: Tensor,
    actions: Tensor,
    states: Dict[str, Tensor],
    target_states: Dict[str, Tensor],
    max_length: List[int],
    scale_factor: float,
    dexhand_weight_idx: Dict[str, List[int]],
) -> Tuple[Tensor, Tensor, Tensor, Tensor]:

    # type: (Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor], Dict[str, Tensor], Tensor, float,  Dict[str, List[int]]) -> Tuple[Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor], Tensor]

    # end effector pose reward
    current_eef_pos = states["base_state"][:, :3]
    current_eef_quat = states["base_state"][:, 3:7]

    target_eef_pos = target_states["wrist_pos"]
    target_eef_quat = target_states["wrist_quat"]
    diff_eef_pos = target_eef_pos - current_eef_pos
    diff_eef_pos_dist = torch.norm(diff_eef_pos, dim=-1)

    current_eef_vel = states["base_state"][:, 7:10]
    current_eef_ang_vel = states["base_state"][:, 10:13]
    target_eef_vel = target_states["wrist_vel"]
    target_eef_ang_vel = target_states["wrist_ang_vel"]

    diff_eef_vel = target_eef_vel - current_eef_vel
    diff_eef_ang_vel = target_eef_ang_vel - current_eef_ang_vel

    joints_pos = states["joints_state"][:, 1:, :3]
    target_joints_pos = target_states["joints_pos"]
    diff_joints_pos = target_joints_pos - joints_pos
    diff_joints_pos_dist = torch.norm(diff_joints_pos, dim=-1)

    # ? assign different weights to different joints
    # assert diff_joints_pos_dist.shape[1] == 17  # ignore the base joint
    diff_thumb_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["thumb_tip"]]].mean(dim=-1)
    diff_index_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["index_tip"]]].mean(dim=-1)
    diff_middle_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["middle_tip"]]].mean(dim=-1)
    diff_ring_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["ring_tip"]]].mean(dim=-1)
    diff_pinky_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["pinky_tip"]]].mean(dim=-1)
    diff_level_1_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_1_joints"]]].mean(dim=-1)
    diff_level_2_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_2_joints"]]].mean(dim=-1)

    joints_vel = states["joints_state"][:, 1:, 7:10]
    target_joints_vel = target_states["joints_vel"]
    diff_joints_vel = target_joints_vel - joints_vel

    reward_eef_pos = torch.exp(-40 * diff_eef_pos_dist)
    reward_thumb_tip_pos = torch.exp(-100 * diff_thumb_tip_pos_dist)
    reward_index_tip_pos = torch.exp(-90 * diff_index_tip_pos_dist)
    reward_middle_tip_pos = torch.exp(-80 * diff_middle_tip_pos_dist)
    reward_pinky_tip_pos = torch.exp(-60 * diff_pinky_tip_pos_dist)
    reward_ring_tip_pos = torch.exp(-60 * diff_ring_tip_pos_dist)
    reward_level_1_pos = torch.exp(-50 * diff_level_1_pos_dist)
    reward_level_2_pos = torch.exp(-40 * diff_level_2_pos_dist)

    reward_eef_vel = torch.exp(-1 * diff_eef_vel.abs().mean(dim=-1))
    reward_eef_ang_vel = torch.exp(-1 * diff_eef_ang_vel.abs().mean(dim=-1))
    reward_joints_vel = torch.exp(-1 * diff_joints_vel.abs().mean(dim=-1).mean(-1))

    current_dof_vel = states["dq"]

    diff_eef_rot = quat_mul(target_eef_quat, quat_conjugate(current_eef_quat))
    diff_eef_rot_angle = quat_to_angle_axis(diff_eef_rot)[0]
    reward_eef_rot = torch.exp(-1 * (diff_eef_rot_angle).abs())

    # object pose reward
    current_obj_pos = states["manip_obj_pos"]
    current_obj_quat = states["manip_obj_quat"]

    target_obj_pos = target_states["manip_obj_pos"]
    target_obj_quat = target_states["manip_obj_quat"]
    diff_obj_pos = target_obj_pos - current_obj_pos
    diff_obj_pos_dist = torch.norm(diff_obj_pos, dim=-1)

    reward_obj_pos = torch.exp(-80 * diff_obj_pos_dist)

    diff_obj_rot = quat_mul(target_obj_quat, quat_conjugate(current_
```

```python
def compute_reward(self, actions):
        lh_rew_buf, lh_reset_buf, lh_success_buf, lh_failure_buf, lh_reward_dict, lh_error_buf = (
            self.compute_reward_side(actions, side="lh")
        )
        rh_rew_buf, rh_reset_buf, rh_success_buf, rh_failure_buf, rh_reward_dict, rh_error_buf = (
            self.compute_reward_side(actions, side="rh")
        )
        self.rew_buf = rh_rew_buf + lh_rew_buf
        self.reset_buf = rh_reset_buf | lh_reset_buf
        self.success_buf = rh_success_buf & lh_success_buf
        self.failure_buf = rh_failure_buf | lh_failure_buf
        self.error_buf = rh_error_buf | lh_error_buf
        self.reward_dict = {
            **{"rh_" + k: v for k, v in rh_reward_dict.items()},
            **{"lh_" + k: v for k, v in lh_reward_dict.items()},
        }
```

```python
def compute_reward_side(self, actions, side="rh"):
        side_demo_data = self.demo_data_rh if side == "rh" else self.demo_data_lh
        target_state = {}
        max_length = torch.clip(side_demo_data["seq_len"], 0, self.max_episode_length).float()
        cur_idx = self.progress_buf
        cur_wrist_pos = side_demo_data["wrist_pos"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_pos"] = cur_wrist_pos
        cur_wrist_rot = side_demo_data["wrist_rot"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_quat"] = aa_to_quat(cur_wrist_rot)[:, [1, 2, 3, 0]]

        target_state["wrist_vel"] = side_demo_data["wrist_velocity"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_ang_vel"] = side_demo_data["wrist_angular_velocity"][torch.arange(self.num_envs), cur_idx]

        target_state["tips_distance"] = side_demo_data["tips_distance"][torch.arange(self.num_envs), cur_idx]

        cur_joints_pos = side_demo_data["mano_joints"][torch.arange(self.num_envs), cur_idx]
        target_state["joints_pos"] = cur_joints_pos.reshape(self.num_envs, -1, 3)
        target_state["joints_vel"] = side_demo_data["mano_joints_velocity"][
            torch.arange(self.num_envs), cur_idx
        ].reshape(self.num_envs, -1, 3)

        cur_obj_transf = side_demo_data["obj_trajectory"][torch.arange(self.num_envs), cur_idx]
        target_state["manip_obj_pos"] = cur_obj_transf[:, :3, 3]
        target_state["manip_obj_quat"] = rotmat_to_quat(cur_obj_transf[:, :3, :3])[:, [1, 2, 3, 0]]

        target_state["manip_obj_vel"] = side_demo_data["obj_velocity"][torch.arange(self.num_envs), cur_idx]
        target_state["manip_obj_ang_vel"] = side_demo_data["obj_angular_velocity"][torch.arange(self.num_envs), cur_idx]

        target_state["tip_force"] = torch.stack(
            [
                self.net_cf[:, getattr(self, f"dexhand_{side}_handles")[k], :]
                for k in (self.dexhand_rh.contact_body_names if side == "rh" else self.dexhand_lh.contact_body_names)
            ],
            axis=1,
        )
        setattr(
            self,
            f"{side}_tips_contact_history",
            torch.concat(
                [
                    getattr(self, f"{side}_tips_contact_history")[:, 1:],
                    (torch.norm(target_state["tip_force"], dim=-1) > 0)[:, None],
                ],
                dim=1,
            ),
        )
        target_state["tip_contact_state"] = getattr(self, f"{side}_tips_contact_history")

        side_states = getattr(self, f"{side}_states")
        if side == "rh":
            power = torch.abs(torch.multiply(self.dof_force[:, : self.dexhand_rh.n_dofs], side_states["dq"])).sum(
                dim=-1
            )
        else:
            power = torch.abs(torch.multiply(self.dof_force[:, self.dexhand_rh.n_dofs :], side_states["dq"])).sum(
                dim=-1
            )
        target_state["power"] = power

        base_handle = getattr(self, f"dexhand_{side}_handles")[
            self.dexhand_rh.to_dex("wrist")[0] if side == "rh" else self.dexhand_lh.to_dex("wrist")[0]
        ]

        wrist_power = torch.abs(
            torch.sum(
                self.apply_forces[:, base_handle, :] * side_states["base_state"][:, 7:10],
                dim=-1,
            )
        )  # ? linear force * linear velocity
        wrist_power += torch.abs(
            torch.sum(
                self.apply_torque[:, base_handle, :] * side_states["base_state"][:, 10:],
                dim=-1,
            )
        )  # ? torque * angular velocity
        target_state["wrist_power"] = wrist_power

        if self.training:
            last_step = self.gym.get_frame_count(self.sim)
            if self.tighten_method == "None":
                scale_factor = 1.0
            elif self.tighten_method == "const":
                scale_factor = self.tighten_factor
            elif self.tighten_method == "linear_decay":
                scale_factor = 1 - (1 - 
```

```python
def compute_observations(self):
        self._refresh()
        obs_rh = self.compute_observations_side("rh")
        obs_lh = self.compute_observations_side("lh")
        for k in obs_rh.keys():
            self.obs_dict[k] = torch.cat([obs_rh[k], obs_lh[k]], dim=-1)
```

```python
def compute_observations_side(self, side="rh"):
        # obs_keys: q, cos_q, sin_q, base_state
        side_states = getattr(self, f"{side}_states")
        side_demo_data = getattr(self, f"demo_data_{side}")

        obs_dict = {}

        obs_values = []
        for ob in self._obs_keys:
            if ob == "base_state":
                obs_values.append(
                    torch.cat([torch.zeros_like(side_states[ob][:, :3]), side_states[ob][:, 3:]], dim=-1)
                )  # ! ignore base position
            else:
                obs_values.append(side_states[ob])
        obs_dict["proprioception"] = torch.cat(obs_values, dim=-1)
        # privileged_obs_keys: dq, manip_obj_pos, manip_obj_quat, manip_obj_vel, manip_obj_ang_vel
        if len(self._privileged_obs_keys) > 0:
            pri_obs_values = []
            for ob in self._privileged_obs_keys:
                if ob == "manip_obj_pos":
                    pri_obs_values.append(side_states[ob] - side_states["base_state"][:, :3])
                elif ob == "manip_obj_com":
                    cur_com_pos = (
                        quat_to_rotmat(side_states["manip_obj_quat"][:, [1, 2, 3, 0]])
                        @ getattr(self, f"manip_obj_{side}_com").unsqueeze(-1)
                    ).squeeze(-1) + side_states["manip_obj_pos"]
                    pri_obs_values.append(cur_com_pos - side_states["base_state"][:, :3])
                elif ob == "manip_obj_weight":
                    prop = self.gym.get_sim_params(self.sim)
                    pri_obs_values.append((getattr(self, f"manip_obj_{side}_mass") * -1 * prop.gravity.z).unsqueeze(-1))
                elif ob == "tip_force":
                    tip_force = torch.stack(
  
```

### maniptrans_envs/lib/envs/tasks/dexhandmanip_sh.py

```
def soft_clamp(x, lower, upper)
class DexHandManipRHEnv(VecTask)
    def __init__(self, cfg)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self)
    def init_data(self)
    def pack_data(self, data)
    def allocate_buffers(self)
    def _create_obj_assets(self, i)
    def _create_obj_actor(self, env_ptr, i, current_asset)
    def _update_states(self)
    def _refresh(self)
    def compute_reward(self, actions)
    def compute_observations(self)
    def _reset_default(self, env_ids)
    def reset_idx(self, env_ids)
    def reset_done(self)
    def step(self, actions)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def create_camera(self)
    def set_force_vis(self, env_ptr, part_k, has_force)
def quat_to_angle_axis(q)
def compute_imitation_reward(reset_buf, progress_buf, running_progress_buf, actions, states, target_states, max_length, scale_factor, dexhand_weight_idx)
class DexHandManipLHEnv(DexHandManipRHEnv)
    def __init__(self, cfg)

```python
def compute_imitation_reward(
    reset_buf: Tensor,
    progress_buf: Tensor,
    running_progress_buf: Tensor,
    actions: Tensor,
    states: Dict[str, Tensor],
    target_states: Dict[str, Tensor],
    max_length: List[int],
    scale_factor: float,
    dexhand_weight_idx: Dict[str, List[int]],
) -> Tuple[Tensor, Tensor, Tensor, Tensor]:

    # type: (Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor], Dict[str, Tensor], Tensor, float, Dict[str, List[int]]) -> Tuple[Tensor, Tensor, Tensor, Tensor, Dict[str, Tensor], Tensor]

    # end effector pose reward
    current_eef_pos = states["base_state"][:, :3]
    current_eef_quat = states["base_state"][:, 3:7]

    target_eef_pos = target_states["wrist_pos"]
    target_eef_quat = target_states["wrist_quat"]
    diff_eef_pos = target_eef_pos - current_eef_pos
    diff_eef_pos_dist = torch.norm(diff_eef_pos, dim=-1)

    current_eef_vel = states["base_state"][:, 7:10]
    current_eef_ang_vel = states["base_state"][:, 10:13]
    target_eef_vel = target_states["wrist_vel"]
    target_eef_ang_vel = target_states["wrist_ang_vel"]

    diff_eef_vel = target_eef_vel - current_eef_vel
    diff_eef_ang_vel = target_eef_ang_vel - current_eef_ang_vel

    joints_pos = states["joints_state"][:, 1:, :3]
    target_joints_pos = target_states["joints_pos"]
    diff_joints_pos = target_joints_pos - joints_pos
    diff_joints_pos_dist = torch.norm(diff_joints_pos, dim=-1)

    # ? assign different weights to different joints
    # assert diff_joints_pos_dist.shape[1] == 17  # ignore the base joint
    diff_thumb_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["thumb_tip"]]].mean(dim=-1)
    diff_index_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["index_tip"]]].mean(dim=-1)
    diff_middle_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["middle_tip"]]].mean(dim=-1)
    diff_ring_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["ring_tip"]]].mean(dim=-1)
    diff_pinky_tip_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["pinky_tip"]]].mean(dim=-1)
    diff_level_1_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_1_joints"]]].mean(dim=-1)
    diff_level_2_pos_dist = diff_joints_pos_dist[:, [k - 1 for k in dexhand_weight_idx["level_2_joints"]]].mean(dim=-1)

    joints_vel = states["joints_state"][:, 1:, 7:10]
    target_joints_vel = target_states["joints_vel"]
    diff_joints_vel = target_joints_vel - joints_vel

    reward_eef_pos = torch.exp(-40 * diff_eef_pos_dist)
    reward_thumb_tip_pos = torch.exp(-100 * diff_thumb_tip_pos_dist)
    reward_index_tip_pos = torch.exp(-90 * diff_index_tip_pos_dist)
    reward_middle_tip_pos = torch.exp(-80 * diff_middle_tip_pos_dist)
    reward_pinky_tip_pos = torch.exp(-60 * diff_pinky_tip_pos_dist)
    reward_ring_tip_pos = torch.exp(-60 * diff_ring_tip_pos_dist)
    reward_level_1_pos = torch.exp(-50 * diff_level_1_pos_dist)
    reward_level_2_pos = torch.exp(-40 * diff_level_2_pos_dist)

    reward_eef_vel = torch.exp(-1 * diff_eef_vel.abs().mean(dim=-1))
    reward_eef_ang_vel = torch.exp(-1 * diff_eef_ang_vel.abs().mean(dim=-1))
    reward_joints_vel = torch.exp(-1 * diff_joints_vel.abs().mean(dim=-1).mean(-1))
    current_dof_vel = states["dq"]

    diff_eef_rot = quat_mul(target_eef_quat, quat_conjugate(current_eef_quat))
    diff_eef_rot_angle = quat_to_angle_axis(diff_eef_rot)[0]
    reward_eef_rot = torch.exp(-1 * (diff_eef_rot_angle).abs())

    # object pose reward
    current_obj_pos = states["manip_obj_pos"]
    current_obj_quat = states["manip_obj_quat"]

    target_obj_pos = target_states["manip_obj_pos"]
    target_obj_quat = target_states["manip_obj_quat"]
    diff_obj_pos = target_obj_pos - current_obj_pos
    diff_obj_pos_dist = torch.norm(diff_obj_pos, dim=-1)

    reward_obj_pos = torch.exp(-80 * diff_obj_pos_dist)

    diff_obj_rot = quat_mul(target_obj_quat, quat_conjugate(current_ob
```

```python
def compute_reward(self, actions):
        target_state = {}
        max_length = torch.clip(self.demo_data["seq_len"], 0, self.max_episode_length).float()
        cur_idx = self.progress_buf
        cur_wrist_pos = self.demo_data["wrist_pos"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_pos"] = cur_wrist_pos
        cur_wrist_rot = self.demo_data["wrist_rot"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_quat"] = aa_to_quat(cur_wrist_rot)[:, [1, 2, 3, 0]]

        target_state["wrist_vel"] = self.demo_data["wrist_velocity"][torch.arange(self.num_envs), cur_idx]
        target_state["wrist_ang_vel"] = self.demo_data["wrist_angular_velocity"][torch.arange(self.num_envs), cur_idx]

        target_state["tips_distance"] = self.demo_data["tips_distance"][torch.arange(self.num_envs), cur_idx]

        cur_joints_pos = self.demo_data["mano_joints"][torch.arange(self.num_envs), cur_idx]
        target_state["joints_pos"] = cur_joints_pos.reshape(self.num_envs, -1, 3)
        target_state["joints_vel"] = self.demo_data["mano_joints_velocity"][
            torch.arange(self.num_envs), cur_idx
        ].reshape(self.num_envs, -1, 3)

        cur_obj_transf = self.demo_data["obj_trajectory"][torch.arange(self.num_envs), cur_idx]
        target_state["manip_obj_pos"] = cur_obj_transf[:, :3, 3]
        target_state["manip_obj_quat"] = rotmat_to_quat(cur_obj_transf[:, :3, :3])[:, [1, 2, 3, 0]]

        target_state["manip_obj_vel"] = self.demo_data["obj_velocity"][torch.arange(self.num_envs), cur_idx]
        target_state["manip_obj_ang_vel"] = self.demo_data["obj_angular_velocity"][torch.arange(self.num_envs), cur_idx]

        target_state["tip_force"] = torch.stack(
            [self.net_cf[:, self.dexhand_handles[k], :] for k in self.dexhand.contact_body_names],
            axis=1,
        )
        self.tips_contact_history = torch.concat(
            [
                self.tips_contact_history[:, 1:],
                (torch.norm(target_state["tip_force"], dim=-1) > 0)[:, None],
            ],
            dim=1,
        )
        target_state["tip_contact_state"] = self.tips_contact_history

        power = torch.abs(torch.multiply(self.dof_force, self.states["dq"])).sum(dim=-1)
        target_state["power"] = power

        wrist_power = torch.abs(
            torch.sum(
                self.apply_forces[:, self.dexhand_handles[self.dexhand.to_dex("wrist")[0]], :]
                * self.states["base_state"][:, 7:10],
                dim=-1,
            )
        )  # ? linear force * linear velocity
        wrist_power += torch.abs(
            torch.sum(
                self.apply_torque[:, self.dexhand_handles[self.dexhand.to_dex("wrist")[0]], :]
                * self.states["base_state"][:, 10:],
                dim=-1,
            )
        )  # ? torque * angular velocity
        target_state["wrist_power"] = wrist_power

        if self.training:
            last_step = self.gym.get_frame_count(self.sim)
            if self.tighten_method == "None":
                scale_factor = 1.0
            elif self.tighten_method == "const":
                scale_factor = self.tighten_factor
            elif self.tighten_method == "linear_decay":
                scale_factor = 1 - (1 - self.tighten_factor) / self.tighten_steps * min(last_step, self.tighten_steps)
            elif self.tighten_method == "exp_decay":
                scale_factor = (np.e * 2) ** (-1 * last_step / self.tighten_steps) * (
                    1 - self.tighten_factor
                ) + self.tighten_factor
            elif self.tighten_method == "cos":
                scale_factor = (self.tighten_factor) + np.abs(
                    -1 * (1 - self.tighten_factor) * np.cos(last_step / self.tighten_steps * np.pi)
                ) * (2 ** (-1 * last_step / self.tighten_steps))
            else:
                raise NotImplementedError
        else:
            scale_factor = 1.0

        assert not self.headless or isins
```

```python
def compute_observations(self):
        self._refresh()
        # obs_keys: q, cos_q, sin_q, base_state
        obs_values = []
        for ob in self._obs_keys:
            if ob == "base_state":
                obs_values.append(
                    torch.cat([torch.zeros_like(self.states[ob][:, :3]), self.states[ob][:, 3:]], dim=-1)
                )  # ! ignore base position
            else:
                obs_values.append(self.states[ob])
        self.obs_dict["proprioception"][:] = torch.cat(obs_values, dim=-1)
        # privileged_obs_keys: dq, manip_obj_pos, manip_obj_quat, manip_obj_vel, manip_obj_ang_vel
        if len(self._privileged_obs_keys) > 0:
            pri_obs_values = []
            for ob in self._privileged_obs_keys:
                if ob == "manip_obj_pos":
                    pri_obs_values.append(self.states[ob] - self.states["base_state"][:, :3])
                elif ob == "manip_obj_com":
                    cur_com_pos = (
                        quat_to_rotmat(self.states["manip_obj_quat"][:, [1, 2, 3, 0]])
                        @ self.manip_obj_com.unsqueeze(-1)
                    ).squeeze(-1) + self.states["manip_obj_pos"]
                    pri_obs_values.append(cur_com_pos - self.states["base_state"][:, :3])
                elif ob == "manip_obj_weight":
                    prop = self.gym.get_sim_params(self.sim)
                    pri_obs_values.append((self.manip_obj_mass * -1 * prop.gravity.z).unsqueeze(-1))
                elif ob == "tip_force":
                    tip_force = torch.stack(
                        [self.net_cf[:, self.dexhand_handles[k], :] for k in self.dexhand.contact_body_names],
                        axis=1,
                    )
                    tip_force = torch.cat(
                        [tip_force, torch.norm(tip_force, dim=-1, keepdim=True)], dim=-1
                    )  # add force magnitude
                    pri_obs_values.append(tip_force.reshape(self.num_envs, -1))
                else:
                    pri_obs_values.append(self.states[ob])
            self.obs_dict["privileged"][:] = torch.cat(pri_obs_values, dim=-1)

        next_target_state = {}

        cur_idx = self.progress_buf + 1
        cur_idx = torch.clamp(cur_idx, torch.zeros_like(self.demo_data["seq_len"]), self.demo_data["seq_len"] - 1)

        cur_idx = torch.stack(
            [cur_idx + t for t in range(self.obs_future_length)], dim=-1
        )  # [B, K], K = obs_future_length
        nE, nT = self.demo_data["wrist_pos"].shape[:2]
        nF = self.obs_future_length

        def indicing(data, idx):
            assert data.shape[0] == nE and data.shape[1] == nT
            remaining_shape = data.shape[2:]
            expanded_idx = idx
            for _ in remaining_shape:
                expanded_idx = expanded_idx.unsqueeze(-1)
            expanded_idx = expanded_idx.expand(-1, -1, *remaining_shape)
            return torch.g
```

### maniptrans_envs/lib/utils/coacd_process.py

```
def coacd_process(input, output, quiet, threshold, preprocess_mode, resolution, no_merge, decimate, max_ch_vertex, extrude, extrude_margin, max_convex_hull, mcts_iteration, mcts_max_depth, mcts_node, prep_resolution, pca, apx_mode, seed)
```

### maniptrans_envs/lib/utils/cv2_display.py

```
class Cv2Display()
    def __init__(self, window_name, image_size, channel_order, bgr2rgb, step_sleep, enabled)
    def _resize(self, img)
    def _reorder(self, img)
    def __call__(self, img)
    def close(self)
```

### maniptrans_envs/lib/utils/dr_utils.py

```
def get_property_setter_map(gym)
def get_property_getter_map(gym)
def get_default_setter_args(gym)
def generate_random_samples(attr_randomization_params, shape, curr_gym_step_count, extern_sample)
def get_bucketed_val(new_prop_val, attr_randomization_params)
def apply_random_samples(prop, og_prop, attr, attr_randomization_params, curr_gym_step_count, extern_sample, bucketing_randomization_params)
def check_buckets(gym, envs, dr_params)
```

### maniptrans_envs/lib/utils/fb_control_utils.py

```
"""Code derived from https://github.com/StanfordVL/perls2 and https://github.com/ARISE-Initiative/robomimic and https://github.com/ARISE-Initiative/robosuite

Utility functions for controlling the robot."""
def opspace_matrices(mass_matrix, J_full)
def sign(x, epsilon)
def nullspace_torques(mass_matrix, nullspace_matrix, initial_joint, joint_pos, joint_vel, joint_kp)
def cross_product(vec1, vec2)
def orientation_error(desired, current)
def quat_conjugate(a)
def quat_mul(a, b)
def orientation_error_quat(desired, current)
def set_goal_position(position_limit, set_pos)
def quat2mat(quaternion)
def unit_vector(data)
def quat_multiply(q1, q0)
def quat_slerp(quat0, quat1, fraction, spin, shortestpath)
def mat2quat(rmat)
def mat2pose(hmat)
def set_goal_orientation(set_ori)
def pose2mat(pos, quat, device)
def to_homogeneous(pos, rot)
def axisangle2quat(vec)
def batch_axisangle2quat(vecs)
def quaternion_to_matrix(quaternions)
def batched_pose2mat(pos, quat, device)
def xyz_to_homogeneous(xyz, device)
def quat_to_angle_axis(q)
```

### maniptrans_envs/lib/utils/fb_transform_utils.py

```
"""Utility functions of matrix and vector transformations.
Based on the utility functions from Robosuite (https://github.com/StanfordVL/robosuite)

NOTE: convention for quaternions is (x, y, z, w)"""
def to_homogeneous(pos, rot)
def to_hom_pos(pos)
def to_hom_ori(ori)
def pos_from_mat(mat)
def rot_from_mat(mat)
def vec_to_mat(vec)
def rotmat2hom(rot)
def convert_quat(q, to)
def quat_multiply(quaternion1, quaternion0)
def random_quat(rand)
def quat_conjugate(quaternion)
def quat_inverse(quaternion)
def quat_slerp(quat0, quat1, fraction, spin, shortestpath)
def random_quat(rand)
def vec(values)
def mat4(array)
def mat2pose(hmat)
def mat2quat(rmat)
def mat2quat(rmat)
def euler2mat(euler)
def axisangle2quat(vec)
def quat2axisangle(quat)
def mat2euler(rmat, axes)
def quat2euler(quaternion)
def euler2quat(euler)
def pose2mat(pose)
def quat2mat(quaternion)
def calc_twist(jacobian, dq)
def pose_in_A_to_pose_in_B(pose_A, pose_A_in_B)
def pose_inv(pose)
def _skew_symmetric_translation(pos_A_in_B)
def vel_in_A_to_vel_in_B(vel_A, ang_vel_A, pose_A_in_B)
def force_in_A_to_force_in_B(force_A, torque_A, pose_A_in_B)
def rotation_matrix(angle, direction, point)
def clip_translation(dpos, limit)
def clip_rotation(quat, limit)
def quat2axisangle(quat)
def axisangle2quat(vec)
def make_pose(translation, rotation)
def unit_vector(data, axis, out)
def get_orientation_error(target_orn, current_orn)
def get_pose_error(target_pose, current_pose)
def convert_euler_quat_2mat(ori)
```

### maniptrans_envs/lib/utils/pointcloud_visualizer.py

```
class PointCloudVisualizer()
    def __init__(self)
    def __call__(self, cloud)
```

### maniptrans_envs/lib/utils/pose_utils.py

```
def rot_mat(angles, hom)
def get_mat(pos, angles)
def cosine_sim(w, v)
def is_similar_rot(rot1, rot2, ori_bound)
def is_similar_pos(pos1, pos2, pos_threshold)
def is_similar_pose(pose1, pose2, ori_bound, pos_threshold)
```

### maniptrans_envs/lib/utils/torch_jit_utils.py

```
def to_torch(x, dtype, device, requires_grad)
def quat_mul(a, b)
def normalize(x, eps)
def quat_apply(a, b)
def quat_rotate(q, v)
def quat_rotate_inverse(q, v)
def quat_conjugate(a)
def quat_unit(a)
def quat_from_angle_axis(angle, axis)
def normalize_angle(x)
def tf_inverse(q, t)
def tf_apply(q, t, v)
def tf_vector(q, v)
def tf_combine(q1, t1, q2, t2)
def get_basis_vector(q, v)
def get_axis_params(value, axis_idx, x_value, dtype, n_dims)
def copysign(a, b)
def get_euler_xyz(q)
def quat_from_euler_xyz(roll, pitch, yaw)
def torch_rand_float(lower, upper, shape, device)
def torch_random_dir_2(shape, device)
def tensor_clamp(t, min_t, max_t)
def scale(x, lower, upper)
def unscale(x, lower, upper)
def unscale_np(x, lower, upper)
def compute_heading_and_up(torso_rotation, inv_start_rot, to_target, vec0, vec1, up_idx)
def compute_rot(torso_quat, velocity, ang_velocity, targets, torso_positions)
def quat_axis(q, axis)
def scale_transform(x, lower, upper)
def unscale_transform(x, lower, upper)
def saturate(x, lower, upper)
def quat_diff_rad(a, b)
def local_to_world_space(pos_offset_local, pose_global)
def normalise_quat_in_pose(pose)
def my_quat_rotate(q, v)
def quat_to_angle_axis(q)
def angle_axis_to_exp_map(angle, axis)
def quat_to_exp_map(q)
def quaternion_to_matrix(quaternions)
def _sqrt_positive_part(x)
def matrix_to_quaternion(matrix)
def quat_to_tan_norm(q)
def euler_xyz_to_exp_map(roll, pitch, yaw)
def exp_map_to_angle_axis(exp_map)
def exp_map_to_quat(exp_map)
def slerp(q0, q1, t)
def calc_heading(q)
def calc_heading_quat(q)
def calc_heading_quat_inv(q)
def axisangle2quat(vec, eps)
def unit_vector_batch(vector)
def quat_slerp_batch(quat0, quat1, fraction, spin, shortestpath)
```

### maniptrans_envs/setup.py

```
def _read_file(fname)
def _read_install_requires()
```