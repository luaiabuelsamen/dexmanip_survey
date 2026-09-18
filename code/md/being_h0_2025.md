# being_h0_2025

source: https://github.com/BeingBeyond/Being-H0


commit: ae92e46f671f48d91161ef1c8cc956bcdffab606


## README

# Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos

<p align="center">
    <img src="docs/assets/image/being-h0-black.png" width="300"/>
</p>

<div align="center">

[![Project Page](https://img.shields.io/badge/Website-Being--H0-green)](https://research.beingbeyond.com/being-h0)
[![arXiv](https://img.shields.io/badge/arXiv-2507.15597-b31b1b.svg)](https://arxiv.org/abs/2507.15597)
[![Model](https://img.shields.io/badge/Hugging%20Face-Model-yellow)](https://huggingface.co/BeingBeyond/Being-H0)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

</div>

<p align="center">
    <img src="docs/assets/image/overview.png"/>
</p>


We introduce **Being-H0**, the first dexterous Vision-Language-Action model pretrained from large-scale human videos via explicit hand motion modeling.

*For the latest developments on our **Being-H** series models, please check our new integrated [codebase](https://github.com/BeingBeyond/Being-H).*

## News

- **[2026-05-01]**: **Being-H0** is accepted by ICML 2026! Welcome to connect with the BeingBeyond Team at the venue then!🔥🔥 
- **[2025-08-02]**: We release the **Being-H0** codebase and pretrained models! Check our [Hugging Face Model Collections](https://huggingface.co/collections/BeingBeyond/being-h0-688dcc58cbd6b452f16bd7ec) for more details. 🔥🔥🔥
- **[2025-07-21]**: We publish **Being-H0**! Check our paper [here](https://arxiv.org/abs/2507.15597). 🌟🌟🌟

## Model Checkpoints

Download pre-trained models from Hugging Face:

| Model Type | Model Name | Parameters | Description |
|------------|------------|------------|-------------|
| **Motion Model** | [Being-H0-GRVQ-8K](https://huggingface.co/BeingBeyond/Being-H0-GRVQ-8K) | - | Motion tokenizer |
| **VLA Pre-trained** | [Being-H0-1B-2508](https://huggingface.co/BeingBeyond/Being-H0-1B-2508) | 1B | Base vision-language-action model |
| **VLA Pre-trained** | [Being-H0-8B-2508](https://huggingface.co/BeingBeyond/Being-H0-8B-2508) | 8B | Base vision-language-action model |
| **VLA Pre-trained** | [Being-H0-14B-2508](https://huggingface.co/BeingBeyond/Being-H0-14B-2508) | 14B | Base vision-language-action model |
| **VLA Post-trained** | [Being-H0-8B-Align-2508](https://huggingface.co/BeingBeyond/Being-H0-8B-Align-2508) | 8B | Fine-tuned for robot alignment |

## Dataset

We have provided the dataset for post-training the VLA model. The dataset is available in Hugging Face:

| Dataset Type | Dataset Name | Description |
|--------------|--------------|-------------|
| **VLA Post-training** | [h0_post_train_db_2508](https://huggingface.co/datasets/BeingBeyond/h0_post_train_db_2508) | Post-training dataset for pretrained Being-H0 VLA model |

## Setup

### Clone repository

```bash
git clone https://github.com/BeingBeyond/Being-H0.git
cd Being-H0
```

### Create environment
```bash
conda env create -f environment.yml
conda activate beingvla
```

### Install package
```bash
pip install flash-attn --no-build-isolation
pip install git+https://github.com/lixiny/manotorch.git
pip install git+https://github.com/mattloper/chumpy.git
```

### Download MANO package

- Visit [MANO website](http://mano.is.tue.mpg.de/)
- Create an account by clicking _Sign Up_ and provide your information
- Download Models and Code (the downloaded file should have the format `mano_v*_*.zip`). Note that all code and data from this download fall under the [MANO license](http://mano.is.tue.mpg.de/license).
- Unzip and copy the contents in `mano_v*_*/` folder to the `beingvla/models/motion/mano/` folder

## Inference

### Motion Generation

- To generate hand motion tokens and render the motion, you should use the Motion Model (`Being-H0-GRVQ-8K`) and the pretrained VLA model (`Being-H0-{1B,8B,14B}-2508`). 
- You can use the following command to run inference. For the `--motion_code_path`, you should use a `+` symbol to jointly specify the wrist and finger motion code paths, e.g., `--motion_code_path "/path/to/Being-H0-GRVQ-8K/wrist/+/path/to/Being-H0-GRVQ-8K/finger/"`.
- The `--hand_mode` can be set to `left`, `right`, or `both` to specify which hand to use for the task.

```bash
python -m beingvla.inference.vla_internvl_inference \
    --model_path /path/to/Being-H0-XXX \
    --motion_code_path "/path/to/Being-H0-GRVQ-8K/wrist/+/path/to/Being-H0-GRVQ-8K/finger/" \
    --input_image ./playground/unplug_airpods.jpg \
    --task_description "unplug the charging cable from the AirPods" \
    --hand_mode both \
    --num_samples 3 \
    --num_seconds 4 \
    --enable_render true \
    --gpu_device 0 \
    --output_dir ./work_dirs/
```

- **To inference on your own photos**: See [Camera Intrinsics Guide](docs/camera_intrinsics.md) for how to estimate camera intrinsics and input them for custom inference.
- Please note that our example images are also photos we took ourselves for testing out-of-distribution (OOD) inference. Therefore, the generated motions may not always perfectly follow the task instruction. You may set a larger `num_seconds` to allow it to fully complete the tasks. For the best results, we recommend using *test images* from the original dataset for inference (eg, EgoDex, TACO, FPHA, etc). However, due to licensing restrictions, we do not provide them directly in this repository. You may need to download the test sets of these datasets yourself.

### Evaluation

- You can use our pretrained VLA model to post-train on real robot data. When you get your post-trained model (e.g., `Being-H0-8B-Align-2508`), you can use the following commands to communicate with real robots, or evaluate the model on a robot task.

- To set up robot communication:

```bash
python -m beingvla.models.motion.m2m.aligner.run_server \
    --model-path /path/to/Being-H0-XXX-Align \
    --port 12305 \
    --action-chunk-length 16
```
- Run evaluation on robot task:

```bash
python -m beingvla.models.motion.m2m.aligner.eval_policy \
    --model-path /path/to/Being-H0-XXX-Align \
    --zarr-path /path/to/real-robot/data \
    --task_description "Put the little white duck into the cup." \
    --action-chunk-length 16
```

## TODO

The following features are planned for future implementation:

- [ ] Real-robot development.
- [ ] Simulation Benchmark.
- [ ] Training code and scripts.
- [ ] Hugging Face transformers library version.
- [x] Detailed documentation for inferencing using custom images.
- [x] Post-training data.
- [x] Inference code and scripts.

## Contributing and Building on Being-H0

We encourage researchers and practitioners to leverage Being-H0 as a foundation for their own creative experiments and applications. Whether you're adapting Being-H0 to new robotic platforms, exploring novel hand manipulation tasks, or extending the model to new domains, our modular codebase is designed to support your innovations. We welcome contributions of all kinds - from bug fixes and documentation improvements to new features and model architectures. By building on Being-H0 together, we can advance the field of dexterous vision-language-action modeling and enable robots to understand and replicate the rich complexity of human hand movements. Join us in making robotic manipulation more intuitive, capable, and accessible to all.

## Citation
If you find our work useful, please consider citing us and give a star to our repository! 🌟🌟🌟

**Being-H0.7**

```bibtex
@article{beingbeyond2026beingh07,
  title={Being-H0. 7: A Latent World-Action Model from Egocentric Videos},
  author={Luo, Hao and Zhang, Wanpeng and Feng, Yicheng and Zheng, Sipeng and Xu, Haiweng and Xu, Chaoyi and Xi, Ziheng and Fu, Yuhui and Lu, Zongqing},
  journal={arXiv preprint arXiv:2605.00078},
  year={2026}
}
```

**Being-H0.5**

```bibtex
@article{beingbeyond2026beingh05,
  title={Being-H0. 5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization},
  author={Luo, Hao and Wang, Ye and Zhang, Wanpeng and Zheng, Sipeng and Xi, Ziheng and Xu, Chaoyi and Xu, Haiweng and Yuan, Haoqi and Zhang, Chi and Wang, Yiqing and others},
  journal={arXiv preprint arXiv:2601.12993},
  year={2026}
}
```

**Being-H0**

```bibtex
@inproceedings{beingbeyond2025beingh0,
  title={Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos},
  author={Luo, Hao and Feng, Yicheng and Zhang, Wanpeng and Zheng, Sipeng and Wang, Ye and Yuan, Haoqi and Liu, Jiazheng and Xu, Chaoyi and Jin, Qin and Lu, Zongqing},
  booktitle={International Conference on Machine Learning},
  year={2026},
  organization={PMLR}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
beingvla/
  __init__.py
  dataset/
    __init__.py
    dataset_internvl.py
    datasets.py
  inference/
    __init__.py
    render_utils.py
    utils.py
    vla_internvl_inference.py
  models/
    __init__.py
    motion/
    vla/
    vlm/
  utils/
    __init__.py
    constants.py
    conversation.py
    dist_utils.py
environment.yml
playground/
  grasp_grey_cube.jpg
  unplug_airpods.jpg
scripts/
  evaluation/
    eval_dexhand.sh
    run_dex_server.sh
  inference/
    vla_inference.sh
```

## Config files (1)


### environment.yml

```yaml
name: beingvla
channels:
  - conda-forge
  - defaults
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r
dependencies:
  - _libgcc_mutex=0.1=main
  - _openmp_mutex=5.1=1_gnu
  - asttokens=3.0.0=pyhd8ed1ab_1
  - bzip2=1.0.8=h5eee18b_6
  - ca-certificates=2025.4.26=hbd8a1cb_0
  - comm=0.2.2=pyhd8ed1ab_1
  - debugpy=1.8.11=py310h6a678d5_0
  - decorator=5.2.1=pyhd8ed1ab_0
  - entrypoints=0.4=pyhd8ed1ab_1
  - exceptiongroup=1.3.0=pyhd8ed1ab_0
  - executing=2.2.0=pyhd8ed1ab_0
  - expat=2.7.1=h6a678d5_0
  - ipykernel=6.29.5=pyh3099207_0
  - ipython=8.37.0=pyh8f84b5b_0
  - jedi=0.19.2=pyhd8ed1ab_1
  - jupyter_client=7.3.4=pyhd8ed1ab_0
  - jupyter_core=5.8.1=pyh31011fe_0
  - ld_impl_linux-64=2.40=h12ee557_0
  - libffi=3.4.4=h6a678d5_1
  - libgcc-ng=11.2.0=h1234567_1
  - libgomp=11.2.0=h1234567_1
  - libsodium=1.0.18=h36c2ea0_1
  - libstdcxx-ng=11.2.0=h1234567_1
  - libuuid=1.41.5=h5eee18b_0
  - libxcb=1.17.0=h9b100fa_0
  - matplotlib-inline=0.1.7=pyhd8ed1ab_1
  - ncurses=6.4=h6a678d5_0
  - nest-asyncio=1.6.0=pyhd8ed1ab_1
  - openssl=3.0.16=h5eee18b_0
  - packaging=25.0=pyh29332c3_1
  - parso=0.8.4=pyhd8ed1ab_1
  - pexpect=4.9.0=pyhd8ed1ab_1
  - pickleshare=0.7.5=pyhd8ed1ab_1004
  - pip=25.1=pyhc872135_2
  - platformdirs=4.3.8=pyhe01879c_0
  - prompt-toolkit=3.0.51=pyha770c72_0
  - pthread-stubs=0.3=h0ce48e5_1
  - ptyprocess=0.7.0=pyhd8ed1ab_1
  - pure_eval=0.2.3=pyhd8ed1ab_1
  - pygments=2.19.1=pyhd8ed1ab_0
  - python=3.10.18=h1a3bd86_0
  - python-dateutil=2.9.0.post0=pyhe01879c_2
  - python_abi=3.10=2_cp310
  - pyzmq=26.2.0=py310h6a678d5_0
  - readline=8.2=h5eee18b_0
  - setuptools=78.1.1=py310h06a4308_0
  - six=1.17.0=pyhe01879c_1
  - sqlite=3.45.3=h5eee18b_0
  - stack_data=0.6.3=pyhd8ed1ab_1
  - tk=8.6.14=h993c535_1
  - tornado=6.1=py310h5764c6d_3
  - traitlets=5.14.3=pyhd8ed1ab_1
  - typing_extensions=4.14.0=pyhe01879c_0
  - wcwidth=0.2.13=pyhd8ed1ab_1
  - wheel=0.45.1=py310h06a4308_0
  - xorg-libx11=1.8.12=h9b100fa_1
  - xorg-libxau=1.0.12=h9b100fa_0
  - xorg-libxdmcp=1.1.5=h9b100fa_0
  - xorg-xorgproto=2024.1=h5eee18b_1
  - xz=5.6.4=h5eee18b_1
  - zeromq=4.3.5=h6a678d5_0
  - zlib=1.2.13=h5eee18b_1
  - pip:
      - absl-py==2.3.0
      - accelerate==1.9.0
      - aiohappyeyeballs==2.6.1
      - aiohttp==3.12.9
      - aiosignal==1.3.2
      - annotated-types==0.7.0
      - asciitree==0.3.3
      - async-timeout==5.0.1
      - attrs==25.3.0
      - av==15.0.0
      - bitsandbytes==0.46.0
      - certifi==2025.4.26
      - charset-normalizer==3.4.2
      - contourpy==1.3.2
      - cycler==0.12.1
      - datasets==3.6.0
      - decord==0.6.0
      - deepspeed==0.15.4
      - dill==0.3.8
      - einops==0.8.1
      - einops-exts==0.0.4
      - einx==0.3.0
      - fasteners==0.19
      - filelock==3.18.0
      - fonttools==4.58.5
      - freetype-py==2.5.1
      - frozendict==2.4.6
      - frozenlist==1.6.2
      - fsspec==2025.3.0
      - grpcio==1.73.0
      - h5py==3.14.0
      - hf-xet==1.1.3
      - hjson==3.1.0
      - huggingface-hub==0.32.4
      - idna==3.10
      - imageio==2.37.0
      - imageio-ffmpeg==0.6.0
      - jinja2==3.1.6
      - joblib==1.5.1
      - kiwisolver==1.4.8
      - markdown==3.8
      - markupsafe==3.0.2
      - matplotlib==3.10.3
      - mpmath==1.3.0
      - msgpack==1.1.0
      - multidict==6.4.4
      - multiprocess==0.70.16
      - natsort==8.4.0
      - networkx==3.4.2
      - ninja==1.11.1.4
      - numcodecs==0.13.1
      - numpy==2.2.6
      - opencv-python==4.11.0.86
      - orjson==3.10.18
      - pandas==2.3.0
      - peft==0.10.0
      - pillow==11.2.1
      - propcache==0.3.1
      - protobuf==6.31.1
      - psutil==7.0.0
      - py-cpuinfo==9.0.0
      - pyarrow==20.0.0
      - pyclean==3.1.0
      - pycocoevalcap==1.2
      - pycocotools==2.0.10
      - pydantic==2.11.5
      - pydantic-core==2.33.2
      - pyglet==2.1.6
      - pyopengl==3.1.0
      - pyparsing==3.2.3
      - pyrender==0.1.45
      - pytz==2025.2
      - pyyaml==6.0.2
      - regex==2024.11.6
      - requests==2.32.3
      - safetensors==0.5.3
      - scikit-learn==1.6.1
      - scipy==1.15.3
      - sentencepiece==0.2.0
      - shortuuid==1.0.13
      - smplx==0.1.28
      - sympy==1.14.0
      - tensorboard==2.19.0
      - tensorboard-data-server==0.7.2
      - tensorboardx==2.6.2.2
      - termcolor==3.1.0
      - threadpoolctl==3.6.0
      - timm==1.0.15
      - tokenizers==0.19.1
      - torch==2.7.1
      - torchvision==0.22.1
      - tqdm==4.67.1
      - transformers==4.43.4
      - transforms3d==0.4.2
      - trimesh==4.6.13
      - triton==3.3.1
      - typing-inspection==0.4.1
      - tzdata==2025.2
      - urllib3==2.4.0
      - werkzeug==3.1.3
      - xxhash==3.5.0
      - yacs==0.1.8
      - yarl==1.20.0
      - zarr==2.18.3

```

## Python signatures and reward/observation bodies (7 files)


### beingvla/models/motion/m2m/aligner/eval_policy.py

```
class ZarrDatasetReader()
    def __init__(self, input_path)
    def get_episode(self, episode_index)
def evaluate_policy(model_path, zarr_path, task_description, action_chunk_length, device)
```

### beingvla/models/motion/m2m/aligner/state_action_norm.py

```
class State_Acton_Transform()
    def __init__(self)
    def norm()
    def denorm()
```

### beingvla/models/motion/m2m/tokenizer/config.py

```
class MotionArguments()
class DataArguments()
class TrainingArguments(TrainingArguments)
def calculate_num_tokens(args_list)
def calculate_codebook_size(args_list)
def is_float(numStr)
def is_number(numStr)
def get_eval_config(cfg_path, device)
```

### beingvla/models/vla/config.py

```
class BeingVLAConfig(PretrainedConfig)
    """Unified configuration for BeingVLA models.

This configuration class supports different VLM and Motion adapter combinations
while maintaining backward compatibility with existing InternVLMotionConfig.

Args:
    vlm_type (str): Type of VLM adapter to use. Options: 'internvl', 'llava', 'qwen_vl'
    """
    def __init__(self, vlm_type, motion_type, vlm_config, motion_config, proprio_dim, action_dim, action_chunk_length, loss_func, gen_action_type, enable_robot_alignment)
    def _validate_motion_config(self, motion_config)
    def from_legacy_config(cls, legacy_config, vlm_type)
    def get_vlm_config(self)
    def get_motion_config(self)
    def to_dict(self)
    def from_dict(cls, config_dict)
```

### beingvla/models/vla/training_mixins.py

```
class BeingVLATrainingMixin()
    """Training-specific functionality for BeingVLA models.

This mixin contains all training-related logic including motion space optimization,
curriculum learning, and motion-aware loss computation."""
    def __init_training_attributes__(self)
    def set_optimize_motion(self, optimize_rate, mot_start_id, mot_end_id, curr_top_rate, curr_bottom_rate)
    def _apply_motion_training_logic(self, outputs, labels)
    def _apply_curriculum_learning(self, loss)
    def get_training_metrics(self)
```

### beingvla/models/vlm/internvl/configuration_intern_vit.py

```
class InternVisionConfig(PretrainedConfig)
    """This is the configuration class to store the configuration of a [`InternVisionModel`]. It is used to
instantiate a vision encoder according to the specified arguments, defining the model architecture.

Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outpu"""
    def __init__(self, num_channels, patch_size, image_size, qkv_bias, hidden_size, num_attention_heads, intermediate_size, qk_normalization, num_hidden_layers, use_flash_attn, hidden_act, norm_type, layer_norm_eps, dropout, drop_path_rate, attention_dropout, initializer_range, initializer_factor)
    def from_pretrained(cls, pretrained_model_name_or_path)
```

### beingvla/models/vlm/internvl/internvl_configs.py

```
class InternVisionConfig(PretrainedConfig)
    """Configuration class for InternVision model.
Self-contained version extracted from InternVL."""
    def __init__(self, num_channels, image_size, patch_size, num_heads, num_layers, mlp_ratio, qkv_bias, drop_path_rate, drop_rate, init_values, use_flash_attn, qk_normalization)
class InternVLChatConfig(PretrainedConfig)
    """Configuration class for InternVL Chat model.
Self-contained version extracted from InternVL."""
    def __init__(self, vision_config, llm_config, use_backbone_lora, use_llm_lora, pad2square, select_layer, force_image_size, downsample_ratio, template, dynamic_image_size, use_thumbnail, ps_version, min_dynamic_patch, max_dynamic_patch)
    def to_dict(self)
class InternVLMotionConfig(InternVLChatConfig)
    """Configuration class for InternVL Motion model.
Self-contained version extracted from InternVL."""
    def __init__(self, motion_config)
    def to_dict(self)
```