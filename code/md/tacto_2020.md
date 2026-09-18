# tacto_2020

source: https://github.com/facebookresearch/tacto


commit: a21d0c4626d74a546d94859226c2fea348babb6a


## README

# TACTO: A Fast, Flexible and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

[![License: MIT](https://img.shields.io/github/license/facebookresearch/tacto)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/tacto)](https://pypi.org/project/tacto/)
[![CircleCI](https://circleci.com/gh/facebookresearch/tacto.svg?style=shield)](https://circleci.com/gh/facebookresearch/tacto)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<a href="https://digit.ml/">
<img height="20" src="/website/static/img/digit-logo.svg" alt="DIGIT-logo" />
</a>

<img src="/website/static/img/teaser.jpg?raw=true" alt="TACTO Simulator" />


This package provides a simulator for vision-based tactile sensors, such as [DIGIT](https://digit.ml).
It provides models for the integration with PyBullet, as well as a renderer of touch readings.
For more information refer to the corresponding paper [TACTO: A Fast, Flexible, and Open-source Simulator for High-resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456).

NOTE: the simulator is not meant to provide a physically accurate dynamics of the contacts (e.g., deformation, friction), but rather relies on existing physics engines.

**For updates and discussions please join the #TACTO channel at the [www.touch-sensing.org](https://www.touch-sensing.org/) community.**


## Installation

The preferred way of installation is through PyPi:

```bash
pip install tacto
```

Alternatively, you can manually clone the repository and install the package using:

```bash
git clone https://github.com/facebookresearch/tacto.git
cd tacto
pip install -e .
```

## Content
This package contain several components:
1) A renderer to simulate readings from vision-based tactile sensors.
2) An API to simulate vision-based tactile sensors in PyBullet.
3) Mesh models and configuration files for the [DIGIT](https://digit.ml) and Omnitact sensors.

## Usage

Additional packages ([torch](https://github.com/pytorch/pytorch), [gym](https://github.com/openai/gym), [pybulletX](https://github.com/facebookresearch/pybulletX)) are required to run the following examples.
You can install them by `pip install -r requirements/examples.txt`.

For a basic example on how to use TACTO in conjunction with PyBullet look at [TBD],

For an example of how to use just the renderer engine look at [examples/demo_render.py](examples/demo_render.py).

For advanced examples of how to use the simulator with PyBullet look at the [examples folder](examples).

* [examples/demo_pybullet_digit.py](examples/demo_pybullet_digit.py): rendering RGB and Depth readings with a [DIGIT](https://digit.ml) sensor.
<img src="/website/static/img/demo_digit.gif?raw=true" alt="Demo DIGIT" />

* [examples/demo_pybullet_allegro_hand.py](examples/demo_pybullet_omnitact.py): rendering 4 DIGIT sensors on an Allegro Hand.
<img src="/website/static/img/demo_allegro.gif?raw=true" alt="Demo Allegro" />

* [examples/demo_pybullet_omnitact.py](examples/demo_pybullet_omnitact.py): rendering RGB and Depth readings with a [OmniTact](https://arxiv.org/pdf/2003.06965.pdf) sensor.
<img src="/website/static/img/demo_omnitact.gif?raw=true" alt="Demo OmniTact" />

* [examples/demo_pybullet_grasp.py](examples/demo_grasp.py): mounted on parallel-jaw grippers and grasping objects with different configurations.
<img src="/website/static/img/demo_grasp.gif?raw=true" alt="Demo Grasp" />

* [examples/demo_pybullet_rolling.py](examples/demo_rolling.py): rolling a marble with two DIGIT sensors.
<img src="/website/static/img/demo_rolling.gif?raw=true" alt="Demo Rolling" />

* [examples/demo_pybullet_digit_shadow.py](examples/demo_pybullet_digit_shadow.py): enable shadow rendering.
<img src="/website/static/img/demo_shadow.gif?raw=true" alt="Demo Shadow" />

### Headless Rendering

NOTE: the renderer requires a screen. For rendering headless, use the "EGL" mode with GPU and CUDA driver or "OSMESA" with CPU. 
See [PyRender](https://pyrender.readthedocs.io/en/latest/install/index.html) for more details.

Additionally, install the patched version of PyOpenGL via,

```
pip install git+https://github.com/mmatl/pyopengl.git@76d1261adee2d3fd99b418e75b0416bb7d2865e6
```

You may then specify which engine to use for headless rendering, for example,

```
import os
os.environ["PYOPENGL_PLATFORM"] = "osmesa" # osmesa cpu rendering
```

## Operating System
We recommend to conduct experiments on **Ubuntu**.

For **macOS**, there exists some visualization problem between pybullet.GUI and pyrender as we know of. Please let us know if it can be resolved, and we will share the information at the repo!

## License
This project is licensed under MIT license, as found in the [LICENSE](LICENSE) file.


## Citing
If you use this project in your research, please cite:

```BibTeX
@Article{Wang2022TACTO,
  author   = {Wang, Shaoxiong and Lambeta, Mike and Chou, Po-Wei and Calandra, Roberto},
  title    = {{TACTO}: A Fast, Flexible, and Open-source Simulator for High-resolution Vision-based Tactile Sensors},
  journal  = {IEEE Robotics and Automation Letters (RA-L)},
  year     = {2022},
  volume   = {7},
  number   = {2},
  pages    = {3930--3937},
  issn     = {2377-3766},
  doi      = {10.1109/LRA.2022.3146945},
  url      = {https://arxiv.org/abs/2012.08456},
}
```



## File tree (depth 3, assets pruned)

```
.circleci/
  config.yml
.flake8
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
examples/
  .gitignore
  allegro_hand_description/
    LICENSE
    README.txt
    allegro_hand_config.rviz
    allegro_hand_config.vcg
    allegro_hand_description_left.urdf
    allegro_hand_description_left.xacro
    allegro_hand_description_left_digit.urdf
    allegro_hand_description_left_digit.xacro
    allegro_hand_description_right.urdf
    allegro_hand_description_right.xacro
    allegro_hand_left.pdf
    allegro_hand_right.pdf
    build_desc.sh
    manifest.xml
  camera.py
  conf/
    allegro_hand.yaml
    bg_digit_240_320.jpg
    digit.yaml
    digit_shadow.yaml
    grasp.yaml
    omnitact.yaml
    rolling.yaml
    sawyer_gripper_env.yaml
  demo_pybullet_allegro_hand.py
  demo_pybullet_digit.py
  demo_pybullet_digit_shadow.py
  demo_pybullet_grasp.py
  demo_pybullet_omnitact.py
  demo_pybullet_rolling.py
  demo_render.py
  demo_sawyer_gripper_env.py
  objects/
    checker_huge.gif
    cube.obj
    cube_small.urdf
    sphere_small.urdf
    textured_sphere_smooth.mtl
    textured_sphere_smooth.obj
  robots/
    sawyer_wsg50.urdf
  sawyer_gripper.py
  sawyer_gripper_env.py
  sawyer_robot/
    LICENSE
    package.xml
    sawyer_description/
  wsg50/
    DIGIT-WSG-50-V1.STL
    GUIDE_WSG50_110.stl
    LICENSE
    WSG-FMF.stl
    WSG50_110.stl
    digit.STL
experiments/
  grasp_stability/
    README.md
    draw.py
    grasp_data_collection.py
    robot.py
    setup/
    train.py
  rolling/
    BO_rolling_collect.py
    README.md
    Rolling.py
    RollingEnv.py
    draw_rolling.py
    setup/
noxfile.py
requirements/
  dev.txt
  examples.txt
  requirements.txt
setup.py
tacto/
  __init__.py
  config_digit.yml
  config_digit_shadow.yml
  config_omnitact.yml
  random_normal_generator.py
  renderer.py
  sensor.py
  timeit.py
tests/
  benchmark.py
  color-osmesa-ground-truth.npy
  depthmap.npy
  test_random_normal_generator.py
  test_render_from_depth_osmesa.py
  test_timeit.py
website/
  static/
```

## Config files (7)


### .circleci/config.yml

```yaml
# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

version: 2.1

jobs:
  # the same recipe doesn't work for Debian 10 yet.
  py37_ubuntu1804:
    docker:
      - image: ubuntu:18.04
    steps:
      - run:
          name: Install git
          command: apt-get update && apt-get install -y git
      - checkout
      - run:
          name: Install dependencies
          command: |
            apt-get update
            apt-get install -y python3 python3-dev python3-pip python3-venv # python 3.6.9

            # packages for headless rendering
            apt-get install -y libgl1-mesa-glx libosmesa6 freeglut3 freeglut3-dev

      - run:
          name: Install TACTO package, required dependencies, and run unit tests
          command: |
            pip3 install nox
            PYOPENGL_PLATFORM=osmesa nox

workflows:
  version: 2
  build:
    jobs:
      - py37_ubuntu1804

```

### .pre-commit-config.yaml

```yaml
default_language_version:
    python: python3.7
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
        language_version: python3.7
        args: [--line-length=119]
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.9
    hooks:
      - id: flake8
        additional_dependencies: [-e, "git+git://github.com/pycqa/pyflakes.git@1911c20#egg=pyflakes"]

```

### examples/conf/allegro_hand.yaml

```yaml
hydra:
  run:
    dir: ./

allegro:
  urdf_path: "allegro_hand_description/allegro_hand_description_left_digit.urdf"
  base_position: [0, 0, 0.095]
  use_fixed_base: True

object:
  urdf_path: "objects/sphere_small.urdf"
  base_position: [0.05, 0.0, 0.235] # (m)
  global_scaling: 0.15

# id of the links that are digits
digit_link_id_allegro: [4, 9, 14, 19]

pybullet_camera:
  cameraDistance: 0.4
  cameraYaw: 45.
  cameraPitch: -45.
  cameraTargetPosition: [0, 0, 0]

tacto:
  width: 120
  height: 160
  visualize_gui: True

object_control_panel:
  slider_params:
    position_low: [-0.3, -0.3, 0]
    position_high: [0.3, 0.3, 0.3]

```

### examples/conf/sawyer_gripper_env.yaml

```yaml
sawyer_gripper:
  robot_params:
    urdf_path: "robots/sawyer_wsg50.urdf"
    use_fixed_base: True
  init_state:
    end_effector:
      position: [0.50, 0, 0.215]
      # p.getQuaternionFromEuler([0, np.pi, 0])
      orientation: [0.0, 1.0, 0.0, 0.0]
    gripper_width: 0.11

object:
  urdf_path: "objects/cube_small.urdf"
  base_position: [0.50, 0, 0.02]
  global_scaling: 0.6

tacto:
  width: 120
  height: 160
  visualize_gui: True

```

### tacto/config_digit.yml

```yaml
# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

sensor:
  # By default:
  # - Sensor (camera) is placed towards x-axis
  # - Sensor origin is the same as .stl/.obj origin
  
  camera:
    - cam0:
      position: [0, 0, 0.015] # Camera position
      orientation: [90, 0, -90] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 60 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
  gel:
    origin: [0.022, 0, 0.015] # Center coordinate of the gel, in meters
    width: 0.02 # Width of the gel, y-axis, in meters
    height: 0.03 # Height of the gel, z-axis, in meters
    curvature: True  # Model the gel as curve? True/False
    curvatureMax: 0.005  # Deformation of the gel due to convexity
    R: 0.1 # Radius of curved gel
    countW: 100 # Number of samples for horizontal direction; higher the finer details
  
  lights:
    # Light position & properties. 

    origin: [0.005, 0, 0.015] # center of the light plane, in meters

    # Light position can be expressed in:
    # - polar coordinates: r and theta. (in y-z plane), and x coordinate of the plane
    # - cartesian coordinates: xyz
    # Only one of the xyz or rtheta is required.
    polar: True # True: apply polar coordinates; False: apply cartesian coordinates;    
    xyz: # cartesian coordinates
      coords: [[0, 0.01732, 0.01], [0, -0.01732, 0.01], [0, 0, -0.02]]
    xrtheta: # polar coordinates in y-z plane
      xs: [0, 0, 0] # x coordinate of the y-z plane
      rs: [0.02, 0.02, 0.02] # r in polar coordinates
      thetas: [30, 150, 270] # theta in polar coordinates, in degrees
    
    colors: [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # R G B color
    intensities: [1, 1, 1] # light intensity

  noise: # Gaussian noise calibrated on output [0, 255]
    color:
      mean: 0 
      std: 7

  force:
    enable: True # flag for enable force feedback. When enabled, the larger normal force is, the closer object is adjusted to the sensor.
    range_force: [0, 100] # dynamic range of forces used to simulate the elastomer deformation
    max_deformation: 0.005 # max pose depth adjustment, in meters


```

### tacto/config_digit_shadow.yml

```yaml
# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

sensor:
  # By default:
  # - Sensor (camera) is placed towards x-axis
  # - Sensor origin is the same as .stl/.obj origin
  
  camera:
    - cam0:
      position: [0, 0, 0.015] # Camera position
      orientation: [90, 0, -90] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 60 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
  gel:
    origin: [0.022, 0, 0.015] # Center coordinate of the gel, in meters
    width: 1.2 # Width of the gel, y-axis, in meters; Fix me: the gel size have to be large for rendering shadows
    height: 0.8 # Height of the gel, z-axis, in meters; Fix me: the gel size have to be large for rendering shadows
    curvature: True  # Model the gel as curve? True/False
    curvatureMax: 0.005  # Deformation of the gel due to convexity
    R: 0.1 # Radius of curved gel
    countW: 100 # Number of samples for horizontal direction; higher the finer details
  
  lights:
    # Light position & properties. 
    spot: True # pyrender.SpotLight if True else pyrender.PointLight
    shadow: True # enable shadow if True; (based on testing, it requires SpotLight for rendering shadows)

    origin: [0.015, 0, 0.015] # center of the light plane, in meters

    # Light position can be expressed in:
    # - polar coordinates: r and theta. (in y-z plane), and x coordinate of the plane
    # - cartesian coordinates: xyz
    # Only one of the xyz or rtheta is required.
    polar: True # True: apply polar coordinates; False: apply cartesian coordinates;    
    xyz: # cartesian coordinates
      coords: [[0, 0.01732, 0.03], [0, -0.01732, 0.03], [0, 0, -0.03]]
    xrtheta: # polar coordinates in y-z plane
      xs: [-0.010, -0.010, -0.010] # x coordinate of the y-z plane
      rs: [0.027, 0.027, 0.027] # r in polar coordinates
      thetas: [40, 140, 270] # theta in polar coordinates, in degrees
    
    colors: [[0, 1, 0], [1, 0, 0], [0, 0, 1]] # R G B color
    intensities: [2.5, 2.5, 2.5] # light intensity

  noise: # Gaussian noise calibrated on output [0, 255]
    color:
      mean: 0 
      std: 7

  force:
    enable: True # flag for enable force feedback. When enabled, the larger normal force is, the closer object is adjusted to the sensor.
    range_force: [0, 100] # dynamic range of forces used to simulate the elastomer deformation
    max_deformation: 0.0005 # max pose depth adjustment, in meters


```

### tacto/config_omnitact.yml

```yaml
# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

sensor:
  # By default:
  # - Sensor (camera) is placed towards x-axis
  # - Sensor origin is the same as .stl/.obj origin
  
  camera:
    - cam0:
      position: [0.03, 0, 0] # Camera position
      orientation: [90, 0, -90] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 70 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2, 3, 4, 5, 6] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
    - cam1:
      position: [0.027, 0, -0.005] # Camera position
      orientation: [0, 0, 0] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 70 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2, 5, 6, 10] # Select light ID list for rendering (OpenGL has max limit of 8 lights)

    - cam2:
      position: [0.028, 0.005, 0] # Camera position
      orientation: [90, 0, 0] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 70 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2, 6, 3, 7] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
    - cam3:
      position: [0.027, 0, 0.005] # Camera position
      orientation: [180, 0, 0] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 70 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2, 3, 4, 8] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
    - cam4:
      position: [0.028, -0.005, 0] # Camera position
      orientation: [270, 0, 0] # Euler angles, "xyz", in degrees; e.g. [0, 0, 0]: towards negative z-axis; [90, 0, -90]: towards x-axis
      yfov: 70 # Vertical field of view in degrees
      znear: 0.001 # Distance to the near clipping plane, in meters
      lightIDList: [0, 1, 2, 4, 5, 9] # Select light ID list for rendering (OpenGL has max limit of 8 lights)
  
  gel:
    origin: [0.022, 0, 0.015] # Center coordinate of the gel, in meters
    width: 0.02 # Width of the gel, y-axis, in meters
    height: 0.03 # Height of the gel, z-axis, in meters
    curvature: True  # Model the gel as curve? True/False
    curvatureMax: 0.005  # Deformation of the gel due to convexity
    R: 0.1 # Radius of curved gel
    countW: 100 # Number of samples for horizontal direction; higher the finer details
    mesh: "../meshes/omnitact.STL"

  lights:
    # Light position & properties. 

    origin: [0, 0, 0] # center of the light plane, in meters

    # Light position can be expressed in:
    # - polar coordinates: r and theta. (in y-z plane), and x coordinate of the plane
    # - cartesian coordinates: xyz
    # Only one of the xyz or rtheta is required.
    polar: True # True: apply polar coordinates; False: apply cartesian coordinates;    
    xyz: # cartesian coordinates
      coords: [[0, 0.01732, 0.01], [0, -0.01732, 0.01], [0, 0, -0.02]]
    xrtheta: # polar coordinates in y-z plane
      xs: [0.030, 0.030, 0.030, 0.028, 0.028, 0.028, 0.028, 0.020, 0.022, 0.020, 0.022] # x coordinate of the y-z plane
      rs: [0.003, 0.003, 0.003, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005] # r in polar coordinates
      thetas: [240, 0, 120, 45, 135, 225, 315, 0, 90, 180, 270] # theta in polar coordinates, in degrees
    
    colors: [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]] # R G B color
    intensities: [0.15, 0.15, 0.15, 0.10, 0.15, 0.10, 0.15, 0.01, 0.01, 0.01, 0.01] # light intensity

  noise:
    color:
      mean: 0 
      std: 0

  force:
    enable: True # flag for enable force feedback. When enabled, the larger normal force is, the closer object is adjusted to the sensor. 
    range_force: [0, 100] # dynamic range of forces used to simulate the elastomer deformation
    max_deformation: 0.001 # max pose depth adjustment, in meters


```

## Python signatures and reward/observation bodies (5 files)


### examples/demo_pybullet_allegro_hand.py

```
def main(cfg)
```

### examples/demo_sawyer_gripper_env.py

```
class GraspingPolicy(Module)
    def __init__(self, env)
    def forward(self, states)
def main()
```

### examples/sawyer_gripper_env.py

```
def _get_dtype_min_max(dtype)
def convert_obs_to_obs_space(obs)
def _get_default_config_path()
class SawyerGripperEnv(Env)
    def __init__(self, config_path)
    def step(self, action)
    def _done(self)
    def _get_obs(self)
    def reset(self)
    def render(self, mode)
    def close(self)
    def seed(self, seed)
    def observation_space(self)
    def action_space(self)
def make_sawyer_gripper_env()

```python
def _get_obs(self):
        cam_color, cam_depth = self.camera.get_image()

        # update objects positions registered with digits
        self.digits.update()
        colors, depths = self.digits.render()

        obj_pose = self.obj.get_base_pose()

        return AttrMap(
            {
                "camera": {"color": cam_color, "depth": cam_depth},
                "digits": [
                    {"color": color, "depth": depth}
                    for color, depth in zip(colors, depths)
                ],
                "robot": self.robot.get_states(),
                "object": {
                    "position": np.array(obj_pose[0]),
                    "orientation": np.array(obj_pose[1]),
                },
            }
        )
```

```python
def observation_space(self):
        """
        >>> print(self.observation_space)
        Dict(
            camera: Dict(color:Box(0, 255, (240, 320, 4), uint8),
            depth: Box(-3.402823e+38, 3.402823e+38, (240, 320), float32)),
            digits: Tuple(
                Dict(
                    color: Box(0, 255, (160, 120, 3), uint8),
                    depth: Box(-3.402823+38, 3.402823e+38, (160, 120), float32)
                ),
                Dict(
                    color: Box(0, 255, (160, 120, 3), uint8),
                    depth: Box(-3.402823+38, 3.402823e+38, (160, 120), float32)
                )
            ),
            end_effector: Dict(
                orientation: Box(-3.1415927, 3.1415927, (4,), float32),
                position: Box(-0.85, 0.85, (3,), float32)
            ),
            gripper_width: Box(0.03, 0.11, (1,), float32)
        )
        """
        return px.utils.SpaceDict(
            {
                "camera": convert_obs_to_obs_space(self.obs.camera),
                "digits": convert_obs_to_obs_space(self.obs.digits),
                "robot": self.robot.state_space,
                "object": {
                    "position": gym.spaces.Box(low=-np.inf, high=np.inf, shape=(3,)),
                    "orientation": gym.spaces.Box(low=-1.0, high=+1.0, shape=(4,)),
                },
            }
        )
```
```

### experiments/grasp_stability/train.py

```
class GraspingDataset(Dataset)
    def __init__(self, fileNames, fields, transform, transformDepth)
    def __len__(self)
    def load_data(self, idx)
    def __getitem__(self, idx)
class AddGaussianNoise(object)
    def __init__(self, mean, std)
    def __call__(self, tensor)
    def __repr__(self)
class Model(Module)
    def __init__(self, fields)
    def get_base_net(self)
    def forward(self, x)
    def save(self, PATH)
    def load(self, PATH)
class Learning()
    def __init__(self, K, i, fields)
    def build_model(self)
    def load_data(self, K, i)
    def evaluation(self)
    def train(self, nbEpoch)
def test(fields)
```

### experiments/rolling/RollingEnv.py

```
class Camera()
    def __init__(self, cameraResolution)
    def get_image(self)
def draw_circle(img, state)
class RollingEnv()
    def __init__(self, tactoResolution, visPyBullet, visTacto, recordLogs, skipFrame)
    def create_scene(self)
    def reset(self)
    def pose_estimation(self, color, depth)
    def controller_Kx(self, state, goal, vel_last, K)
    def step(self, render)
    def save_logs(self, fn)
    def cost_function(self, state, goal, vel, xyz)
    def simulate(self, goal, K)
```