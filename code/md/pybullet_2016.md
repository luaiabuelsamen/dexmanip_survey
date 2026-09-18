# pybullet_2016

source: https://github.com/bulletphysics/bullet3


commit: 63c4d67e337017f9d8b298c900e9aabdb69296e7


## README

[![Travis Build Status](https://api.travis-ci.org/bulletphysics/bullet3.png?branch=master)](https://travis-ci.org/bulletphysics/bullet3)
[![Appveyor Build status](https://ci.appveyor.com/api/projects/status/6sly9uxajr6xsstq)](https://ci.appveyor.com/project/erwincoumans/bullet3)

# Bullet Physics SDK

This is the official C++ source code repository of the Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc.

![PyBullet](https://pybullet.org/wordpress/wp-content/uploads/2019/03/cropped-pybullet.png)

## Issues ##
The Issue tracker was flooded with support questions and is closed until it is cleaned up. Use the [PyBullet forums](http://pybullet.org) to discuss with others.

## PyBullet ##
It is highly recommended to use PyBullet Python bindings for improved support for robotics, reinforcement learning and VR. Use pip install pybullet and checkout the [PyBullet Quickstart Guide](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3).

Installation is simple:
```
pip3 install pybullet --upgrade --user
python3 -m pybullet_envs.examples.enjoy_TF_AntBulletEnv_v0_2017may
python3 -m pybullet_envs.examples.enjoy_TF_HumanoidFlagrunHarderBulletEnv_v1_2017jul
python3 -m pybullet_envs.deep_mimic.testrl --arg_file run_humanoid3d_backflip_args.txt
```

If you use PyBullet in your research, please cite it like this:

```
@MISC{coumans2021,
author =   {Erwin Coumans and Yunfei Bai},
title =    {PyBullet, a Python module for physics simulation for games, robotics and machine learning},
howpublished = {\url{http://pybullet.org}},
year = {2016--2021}
}
```

## Requirements for Bullet Physics C++

A C++ compiler for C++ 2003. The library is tested on Windows, Linux, Mac OSX, iOS, Android,
but should likely work on any platform with C++ compiler. 
Some optional demos require OpenGL 2 or OpenGL 3, there are some non-graphical demos and unit tests too.

## Contributors and Coding Style information

https://docs.google.com/document/d/1u9vyzPtrVoVhYqQOGNWUgjRbfwfCdIts_NzmvgiJ144/edit

## Requirements for experimental OpenCL GPGPU support

The entire collision detection and rigid body dynamics can be executed on the GPU.

A high-end desktop GPU, such as an AMD Radeon 7970 or NVIDIA GTX 680 or better.
We succesfully tested the software under Windows, Linux and Mac OSX.
The software currently doesn't work on OpenCL CPU devices. It might run
on a laptop GPU but performance will not likely be very good. Note that
often an OpenCL drivers fails to compile a kernel. Some unit tests exist to
track down the issue, but more work is required to cover all OpenCL kernels.

## License

All source code files are licensed under the permissive zlib license
(http://opensource.org/licenses/Zlib) unless marked differently in a particular folder/file.

## Build instructions for Bullet using vcpkg

You can download and install Bullet using the [vcpkg](https://github.com/Microsoft/vcpkg/) dependency manager:

    git clone https://github.com/Microsoft/vcpkg.git
    cd vcpkg
    ./bootstrap-vcpkg.sh
    ./vcpkg integrate install
    ./vcpkg install bullet3

The Bullet port in vcpkg is kept up to date by Microsoft team members and community contributors. If the version is out of date, please [create an issue or pull request](https://github.com/Microsoft/vcpkg) on the vcpkg repository.

## Build instructions for Bullet using premake. You can also use cmake instead.

**Windows**

Click on build_visual_studio_vr_pybullet_double.bat and open build3/vs2010/0_Bullet3Solution.sln
When asked, convert the projects to a newer version of Visual Studio.
If you installed Python in the C:\ root directory, the batch file should find it automatically.
Otherwise, edit this batch file to choose where Python include/lib directories are located.

**Windows Virtual Reality sandbox for HTC Vive and Oculus Rift**

Build and run the App_SharedMemoryPhysics_VR project, preferably in Release/optimized build.
You can connect from Python pybullet to the sandbox using:

```
import pybullet as p
p.connect(p.SHARED_MEMORY) #or (p.TCP, "localhost", 6667) or (p.UDP, "192.168.86.10",1234)
```

**Linux and Mac OSX gnu make**

Make sure gcc and cmake is installed (`sudo apt-get install build-essential` and `sudo apt-get install cmake` for Linux, `brew install cmake` for Mac, or https://cmake.org)

In a terminal type:
```
./build_cmake_pybullet_double.sh
```
This script will invoke cmake and build in the build_cmake directory. You can find pybullet in Bullet/examples/pybullet.
The BulletExampleBrowser binary will be in Bullet/examples/ExampleBrowser.

You can also build Bullet using premake. There are premake executables in the build3 folder.
Depending on your system (Linux 32bit, 64bit or Mac OSX) use one of the following lines
Using premake:
```
cd build3
./premake4_linux --double gmake
./premake4_linux64 --double gmake
./premake4_osx --double --enable_pybullet gmake
```
Then
```
cd gmake
make
```

Note that on Linux, you need to use cmake to build pybullet, since the compiler has issues of mixing shared and static libraries.

**Mac OSX Xcode**
	
Click on build3/xcode4.command or in a terminal window execute
```	
./premake_osx xcode4
```
## Usage

The App_ExampleBrowser executables will be located in the bin folder.
You can just run it though a terminal/command prompt, or by clicking it.


```
[--start_demo_name="Demo Name"]     Start with a selected demo  
[--mp4=moviename.mp4]               Create a mp4 movie of the window, requires ffmpeg installed
[--mouse_move_multiplier=0.400000]  Set the mouse move sensitivity
[--mouse_wheel_multiplier=0.01]     Set the mouse wheel sensitivity
[--background_color_red= 0.9]       Set the red component for background color. Same for green and blue
[--fixed_timestep= 0.0]             Use either a real-time delta time (0.0) or a fixed step size (0.016666)
```

You can use mouse picking to grab objects. When holding the ALT or CONTROL key, you have Maya style camera mouse controls.
Press F1 to create a series of screenshots. Hit ESCAPE to exit the demo app.

Check out the docs folder and the Bullet physics forums for further information.


## File tree (depth 3, assets pruned)

```
.ci/
  docker/
    env.list
    ubuntu-bionic
    ubuntu-xenial
  script.sh
.github/
  workflows/
    cmake.yml
.gitignore
.style.yapf
AUTHORS.txt
BulletConfig.cmake.in
CMakeLists.txt
Doxyfile
Extras/
  BulletRobotics/
    CMakeLists.txt
    bullet_robotics.pc.cmake
    premake4.lua
  BulletRoboticsGUI/
    CMakeLists.txt
    bullet_robotics_gui.pc.cmake
  CMakeLists.txt
  ConvexDecomposition/
    CMakeLists.txt
    ConvexBuilder.cpp
    ConvexBuilder.h
    ConvexDecomposition.cpp
    ConvexDecomposition.h
    LICENSE.txt
    bestfit.cpp
    bestfit.h
    bestfitobb.cpp
    bestfitobb.h
    cd_hull.cpp
    cd_hull.h
    cd_vector.h
    cd_wavefront.cpp
    cd_wavefront.h
    concavity.cpp
    concavity.h
    fitsphere.cpp
    fitsphere.h
    float_math.cpp
    float_math.h
    meshvolume.cpp
    meshvolume.h
    planetri.cpp
    planetri.h
    premake4.lua
    raytri.cpp
    raytri.h
    splitplane.cpp
    splitplane.h
    vlookup.cpp
    vlookup.h
  GIMPACTUtils/
    CMakeLists.txt
    LICENSE.txt
    btGImpactConvexDecompositionShape.cpp
    btGImpactConvexDecompositionShape.h
  HACD/
    CMakeLists.txt
    LICENSE.txt
    hacdCircularList.h
    hacdCircularList.inl
    hacdGraph.cpp
    hacdGraph.h
    hacdHACD.cpp
    hacdHACD.h
    hacdICHull.cpp
    hacdICHull.h
    hacdManifoldMesh.cpp
    hacdManifoldMesh.h
    hacdVector.h
    hacdVector.inl
    hacdVersion.h
    premake4.lua
  InverseDynamics/
    BulletInverseDynamicsUtilsCommon.h
    CMakeLists.txt
    CloneTreeCreator.cpp
    CloneTreeCreator.hpp
    CoilCreator.cpp
    CoilCreator.hpp
    DillCreator.cpp
    DillCreator.hpp
    IDRandomUtil.cpp
    IDRandomUtil.hpp
    LICENSE.txt
    MultiBodyNameMap.cpp
    MultiBodyNameMap.hpp
    MultiBodyTreeCreator.cpp
    MultiBodyTreeCreator.hpp
    MultiBodyTreeDebugGraph.cpp
    MultiBodyTreeDebugGraph.hpp
    RandomTreeCreator.cpp
    RandomTreeCreator.hpp
    SimpleTreeCreator.cpp
    SimpleTreeCreator.hpp
    User2InternalIndex.cpp
    User2InternalIndex.hpp
    btMultiBodyFromURDF.hpp
    btMultiBodyTreeCreator.cpp
    btMultiBodyTreeCreator.hpp
    invdyn_bullet_comparison.cpp
    invdyn_bullet_comparison.hpp
    premake4.lua
  Makefile.am
  Serialize/
    BlenderSerialize/
    BulletFileLoader/
    BulletWorldImporter/
    BulletXmlWorldImporter/
    CMakeLists.txt
    HeaderGenerator/
    ReadBulletSample/
    makesdna/
  VHACD/
    LICENSE.txt
    inc/
    premake4.lua
    public/
    src/
    test/
  obj2sdf/
    CMakeLists.txt
    obj2sdf.cpp
    premake4.lua
  premake4.lua
LICENSE.txt
MANIFEST.in
README.md
UseBullet.cmake
VERSION
_clang-format
appveyor.yml
build3/
  Android/
    jni/
  bin2cpp.bat
  bin2cpp.lua
  bullet.rc
  bullet_ico.ico
  cmake/
    FindLibPython.py
    FindNumPy.cmake
    FindPythonLibs.cmake
    SelectLibraryConfigurations.cmake
  findDirectX11.lua
  findOpenCL.lua
  findOpenGLGlewGlut.lua
  lcpp.lua
  premake4.exe
  premake4.lua
  premake4_arm64
  premake4_linux
  premake4_linux64
  premake4_osx
  premake4_osx32
  premake5.exe
  stringify.bat
  stringify.sh
  stringifyKernel.lua
  stringifyShaders.bat
build_cmake_pybullet_double.sh
build_visual_studio_vr_pybullet_double.bat
build_visual_studio_vr_pybullet_double_cmake.bat
build_visual_studio_vr_pybullet_double_dynamic.bat
build_visual_studio_without_pybullet_vr.bat
bullet.pc.cmake
clang-format-all.sh
examples/
  BasicDemo/
    BasicExample.cpp
    BasicExample.h
    CMakeLists.txt
    main.cpp
    premake4.lua
  Benchmarks/
    BenchmarkDemo.cpp
    BenchmarkDemo.h
    HaltonData.h
    TaruData.h
    landscapeData.h
  BulletRobotics/
    BoxStack.cpp
    BoxStack.h
    FixJointBoxes.cpp
    FixJointBoxes.h
    JointLimit.cpp
    JointLimit.h
  CMakeLists.txt
  Collision/
    CollisionSdkC_Api.cpp
    CollisionSdkC_Api.h
    CollisionTutorialBullet2.cpp
    CollisionTutorialBullet2.h
    Internal/
  CommonInterfaces/
    Common2dCanvasInterface.h
    CommonCallbacks.h
    CommonCameraInterface.h
    CommonDeformableBodyBase.h
    CommonExampleInterface.h
    CommonFileIOInterface.h
    CommonGUIHelperInterface.h
    CommonGraphicsAppInterface.h
    CommonMultiBodyBase.h
    CommonParameterInterface.h
    CommonRenderInterface.h
    CommonRigidBodyBase.h
    CommonWindowInterface.h
  Constraints/
    ConstraintDemo.cpp
    ConstraintDemo.h
    ConstraintPhysicsSetup.cpp
    ConstraintPhysicsSetup.h
    Dof6Spring2Setup.cpp
    Dof6Spring2Setup.h
    TestHingeTorque.cpp
    TestHingeTorque.h
  DeformableDemo/
    ClothFriction.cpp
    ClothFriction.h
    Collide.cpp
    Collide.h
    DeformableClothAnchor.cpp
    DeformableClothAnchor.h
    DeformableContact.cpp
    DeformableContact.h
    DeformableMultibody.cpp
    DeformableMultibody.h
    DeformableRigid.cpp
    DeformableRigid.h
    DeformableSelfCollision.cpp
    DeformableSelfCollision.h
    GraspDeformable.cpp
    GraspDeformable.h
    LargeDeformation.cpp
    LargeDeformation.h
    LoadDeformed.cpp
    LoadDeformed.h
    MultibodyClothAnchor.cpp
    MultibodyClothAnchor.h
    Pinch.cpp
    Pinch.h
    PinchFriction.cpp
    PinchFriction.h
    SplitImpulse.cpp
    SplitImpulse.h
    VolumetricDeformable.cpp
    VolumetricDeformable.h
  DynamicControlDemo/
    MotorDemo.cpp
    MotorDemo.h
  Evolution/
    NN3DWalkers.cpp
    NN3DWalkers.h
    NN3DWalkersTimeWarpBase.h
  ExampleBrowser/
    CMakeLists.txt
    CollisionShape2TriangleMesh.cpp
    CollisionShape2TriangleMesh.h
    EmptyBrowser.h
    EmptyExample.h
    ExampleBrowserInterface.h
    ExampleEntries.cpp
    ExampleEntries.h
    GL_ShapeDrawer.cpp
    GL_ShapeDrawer.h
    GwenGUISupport/
    InProcessExampleBrowser.cpp
    InProcessExampleBrowser.h
    OpenGLExampleBrowser.cpp
    OpenGLExampleBrowser.h
    OpenGLGuiHelper.cpp
    OpenGLGuiHelper.h
    main.cpp
    premake4.lua
  Experiments/
    ImplicitCloth/
  ExtendedTutorials/
    Bridge.cpp
    Bridge.h
    Chain.cpp
    Chain.h
    CompoundBoxes.cpp
    CompoundBoxes.h
    InclinedPlane.cpp
    InclinedPlane.h
    MultiPendulum.cpp
    MultiPendulum.h
    MultipleBoxes.cpp
    MultipleBoxes.h
    NewtonsCradle.cpp
    NewtonsCradle.h
    NewtonsRopeCradle.cpp
    NewtonsRopeCradle.h
    RigidBodyFromObj.cpp
    RigidBodyFromObj.h
    SimpleBox.cpp
    SimpleBox.h
    SimpleCloth.cpp
    SimpleCloth.h
    SimpleJoint.cpp
    SimpleJoint.h
    premake4.lua
  ForkLift/
    ForkLiftDemo.cpp
    ForkLiftDemo.h
  FractureDemo/
    FractureDemo.cpp
    FractureDemo.h
    btFractureBody.cpp
    btFractureBody.h
    btFractureDynamicsWorld.cpp
    btFractureDynamicsWorld.h
  GyroscopicDemo/
    GyroscopicSetup.cpp
    GyroscopicSetup.h
  Heightfield/
    HeightfieldExample.cpp
    HeightfieldExample.h
  HelloWorld/
    CMakeLists.txt
    HelloWorld.cpp
    premake4.lua
  Importers/
    ImportBsp/
    ImportBullet/
    ImportColladaDemo/
    ImportMJCFDemo/
    ImportMeshUtility/
    ImportObjDemo/
    ImportSDFDemo/
    ImportSTLDemo/
    ImportURDFDemo/
  InverseDynamics/
    InverseDynamicsExample.cpp
    InverseDynamicsExample.h
    premake4.lua
  InverseKinematics/
    InverseKinematicsExample.cpp
    InverseKinematicsExample.h
  LuaDemo/
    LuaPhysicsSetup.cpp
    LuaPhysicsSetup.h
  MultiBody/
    InvertedPendulumPDControl.cpp
    InvertedPendulumPDControl.h
    KinematicMultiBodyExample.cpp
    KinematicMultiBodyExample.h
    MultiBodyConstraintFeedback.cpp
    MultiBodyConstraintFeedback.h
    MultiBodySoftContact.cpp
    MultiBodySoftContact.h
    MultiDofDemo.cpp
    MultiDofDemo.h
    Pendulum.cpp
    Pendulum.h
    SerialChains.cpp
    SerialChains.h
    TestJointTorqueSetup.cpp
    TestJointTorqueSetup.h
    pendulum_gold.h
  MultiBodyBaseline/
    MultiBodyBaseline.cpp
    MultiBodyBaseline.h
  MultiThreadedDemo/
    CommonRigidBodyMTBase.cpp
    CommonRigidBodyMTBase.h
    MultiThreadedDemo.cpp
    MultiThreadedDemo.h
  MultiThreading/
    MultiThreadingExample.cpp
    MultiThreadingExample.h
    b3PosixThreadSupport.cpp
    b3PosixThreadSupport.h
    b3ThreadSupportInterface.cpp
    b3ThreadSupportInterface.h
    b3Win32ThreadSupport.cpp
    b3Win32ThreadSupport.h
    main.cpp
    premake4.lua
  OpenCL/
    CommonOpenCL/
    broadphase/
    rigidbody/
  OpenGLWindow/
    CMakeLists.txt
    EGLOpenGLWindow.cpp
    EGLOpenGLWindow.h
    GLFWOpenGLWindow.cpp
    GLFWOpenGLWindow.h
    GLInstanceGraphicsShape.h
    GLInstanceRendererInternalData.h
    GLInstancingRenderer.cpp
    GLInstancingRenderer.h
    GLPrimInternalData.h
    GLPrimitiveRenderer.cpp
    GLPrimitiveRenderer.h
    GLRenderToTexture.cpp
    GLRenderToTexture.h
    GwenOpenGL3CoreRenderer.h
    LoadShader.cpp
    LoadShader.h
    MacOpenGLWindow.cpp
    MacOpenGLWindow.h
    MacOpenGLWindowObjC.h
    MacOpenGLWindowObjC.m
    OpenGL2Include.h
    OpenGLInclude.h
    OpenSans.cpp
    OpenSans.ttf
    Shaders/
    ShapeData.h
    SimpleCamera.cpp
    SimpleCamera.h
    SimpleOpenGL2App.cpp
    SimpleOpenGL2App.h
    SimpleOpenGL2Renderer.cpp
    SimpleOpenGL2Renderer.h
    SimpleOpenGL3App.cpp
    SimpleOpenGL3App.h
    TwFonts.cpp
    TwFonts.h
    Win32InternalWindowData.h
    Win32OpenGLWindow.cpp
    Win32OpenGLWindow.h
    Win32Window.cpp
    Win32Window.h
    X11OpenGLWindow.cpp
    X11OpenGLWindow.h
    fontstash.cpp
    fontstash.h
    opengl_fontstashcallbacks.cpp
    opengl_fontstashcallbacks.h
    premake4.lua
  Planar2D/
    Planar2D.cpp
    Planar2D.h
  Raycast/
    RaytestDemo.cpp
    RaytestDemo.h
  ReducedDeformableDemo/
    ConservationTest.cpp
    ConservationTest.h
    FreeFall.cpp
    FreeFall.h
    FrictionSlope.cpp
    FrictionSlope.h
    ModeVisualizer.cpp
    ModeVisualizer.h
    ReducedBenchmark.cpp
    ReducedBenchmark.h
    ReducedCollide.cpp
    ReducedCollide.h
    ReducedGrasp.cpp
    ReducedGrasp.h
    ReducedMotorGrasp.cpp
    ReducedMotorGrasp.h
    Springboard.cpp
    Springboard.h
  RenderingExamples/
    CoordinateSystemDemo.cpp
    CoordinateSystemDemo.h
    DynamicTexturedCubeDemo.cpp
    DynamicTexturedCubeDemo.h
    RaytracerSetup.cpp
    RaytracerSetup.h
    RenderInstancingDemo.cpp
    RenderInstancingDemo.h
    TimeSeriesCanvas.cpp
    TimeSeriesCanvas.h
    TimeSeriesExample.cpp
    TimeSeriesExample.h
    TimeSeriesFontData.cpp
    TimeSeriesFontData.h
    TinyRendererSetup.cpp
    TinyRendererSetup.h
    TinyVRGui.cpp
    TinyVRGui.h
  RigidBody/
    KinematicRigidBodyExample.cpp
    KinematicRigidBodyExample.h
    RigidBodySoftContact.cpp
    RigidBodySoftContact.h
  RobotSimulator/
    CMakeLists.txt
    HelloBulletRobotics.cpp
    MinitaurSetup.cpp
    MinitaurSetup.h
    MinitaurSimulatorExample.cpp
    MinitaurSimulatorExample.h
    RobotSimulatorMain.cpp
    VRGloveSimulatorMain.cpp
    b3RobotSimulatorClientAPI.cpp
    b3RobotSimulatorClientAPI.h
    premake4.lua
  RoboticsLearning/
    GripperGraspExample.cpp
    GripperGraspExample.h
    KukaGraspExample.cpp
    KukaGraspExample.h
    R2D2GraspExample.cpp
    R2D2GraspExample.h
  RollingFrictionDemo/
    RollingFrictionDemo.cpp
    RollingFrictionDemo.h
  SharedMemory/
    BodyJointInfoUtility.h
    CMakeLists.txt
    GraphicsClientExample.cpp
    GraphicsClientExample.h
    GraphicsServerExample.cpp
    GraphicsServerExample.h
    GraphicsSharedMemoryBlock.h
    GraphicsSharedMemoryCommands.h
    GraphicsSharedMemoryPublic.h
    IKTrajectoryHelper.cpp
    IKTrajectoryHelper.h
    InProcessMemory.cpp
    InProcessMemory.h
    PhysicsClient.cpp
    PhysicsClient.h
    PhysicsClientC_API.cpp
    PhysicsClientC_API.h
    PhysicsClientExample.cpp
    PhysicsClientExample.h
    PhysicsClientGRPC.cpp
    PhysicsClientGRPC.h
    PhysicsClientGRPC_C_API.cpp
    PhysicsClientGRPC_C_API.h
    PhysicsClientSharedMemory.cpp
    PhysicsClientSharedMemory.h
    PhysicsClientSharedMemory2.cpp
    PhysicsClientSharedMemory2.h
    PhysicsClientSharedMemory2_C_API.cpp
    PhysicsClientSharedMemory2_C_API.h
    PhysicsClientSharedMemory_C_API.cpp
    PhysicsClientSharedMemory_C_API.h
    PhysicsClientTCP.cpp
    PhysicsClientTCP.h
    PhysicsClientTCP_C_API.cpp
    PhysicsClientTCP_C_API.h
    PhysicsClientUDP.cpp
    PhysicsClientUDP.h
    PhysicsClientUDP_C_API.cpp
    PhysicsClientUDP_C_API.h
    PhysicsCommandProcessorInterface.h
    PhysicsDirect.cpp
    PhysicsDirect.h
    PhysicsDirectC_API.cpp
    PhysicsDirectC_API.h
    PhysicsLoopBack.cpp
    PhysicsLoopBack.h
    PhysicsLoopBackC_API.cpp
    PhysicsLoopBackC_API.h
    PhysicsServer.cpp
    PhysicsServer.h
    PhysicsServerCommandProcessor.cpp
    PhysicsServerCommandProcessor.h
    PhysicsServerExample.cpp
    PhysicsServerExample.h
    PhysicsServerExampleBullet2.cpp
    PhysicsServerExampleBullet2.h
    PhysicsServerSharedMemory.cpp
    PhysicsServerSharedMemory.h
    PosixSharedMemory.cpp
    PosixSharedMemory.h
    RemoteGUIHelper.cpp
    RemoteGUIHelper.h
    RemoteGUIHelperTCP.cpp
    RemoteGUIHelperTCP.h
    RobotControlExample.cpp
    RobotControlExample.h
    SharedMemoryBlock.h
    SharedMemoryCommandProcessor.cpp
    SharedMemoryCommandProcessor.h
    SharedMemoryCommands.h
    SharedMemoryCommon.h
    SharedMemoryInProcessPhysicsC_API.cpp
    SharedMemoryInProcessPhysicsC_API.h
    SharedMemoryInterface.h
    SharedMemoryPublic.h
    SharedMemoryUserData.h
    Win32SharedMemory.cpp
    Win32SharedMemory.h
    b3PluginManager.cpp
    b3PluginManager.h
    b3RobotSimulatorClientAPI_InternalData.h
    b3RobotSimulatorClientAPI_NoDirect.cpp
    b3RobotSimulatorClientAPI_NoDirect.h
    b3RobotSimulatorClientAPI_NoGUI.cpp
    b3RobotSimulatorClientAPI_NoGUI.h
    dart/
    grpc/
    main.cpp
```

## Config files (2)


### examples/pybullet/gym/pybullet_data/policies/ppo/minitaur_reactive_env/config.yaml

```yaml
!!python/object/new:pybullet_envs.minitaur.agents.tools.attr_dict.AttrDict
dictitems:
  algorithm: !!python/name:pybullet_envs.minitaur.agents.ppo.algorithm.PPOAlgorithm ''
  discount: 0.9868209124499899
  env: !!python/object/apply:functools.partial
    args:
    - &id001 !!python/name:pybullet_envs.minitaur.envs.minitaur_reactive_env.MinitaurReactiveEnv ''
    state: !!python/tuple
    - *id001
    - !!python/tuple []
    - accurate_motor_model_enabled: true
      control_latency: 0.02
      energy_weight: 0.005
      env_randomizer: null
      motor_kd: 0.015
      num_steps_to_log: 1000
      pd_latency: 0.003
      remove_default_joint_damping: true
      render: false
      urdf_version: rainbow_dash_v0
    - null
  eval_episodes: 25
  init_logstd: -1.1579536194508315
  init_mean_factor: 0.3084392491563408
  kl_cutoff_coef: 1000
  kl_cutoff_factor: 2
  kl_init_penalty: 1
  kl_target: 0.01
  logdir: /cns/ij-d/home/jietan/experiment/minitaur_vizier_study_ppo/minreact_nonexp_nr_02_186515603_186518344/333
  max_length: 1000
  network: !!python/name:pybullet_envs.minitaur.agents.scripts.networks.ForwardGaussianPolicy ''
  network_config: {}
  num_agents: 25
  policy_layers: !!python/tuple
  - 114
  - 45
  policy_lr: 0.00023516695218031146
  policy_optimizer: AdamOptimizer
  steps: 7000000.0
  update_epochs_policy: 25
  update_epochs_value: 25
  update_every: 25
  use_gpu: false
  value_layers: !!python/tuple
  - 170
  - 78
  value_lr: 0.00031014032715987193
  value_optimizer: AdamOptimizer
  weight_summaries:
    all: .*
    policy: .*/policy/.*
    value: .*/value/.*
state:
  _mutable: false
```

### examples/pybullet/gym/pybullet_data/policies/ppo/minitaur_trotting_env/config.yaml

```yaml
!!python/object/new:pybullet_envs.minitaur.agents.tools.attr_dict.AttrDict
dictitems:
  algorithm: !!python/name:pybullet_envs.minitaur.agents.ppo.algorithm.PPOAlgorithm ''
  discount: 0.9899764168788918
  env: !!python/object/apply:functools.partial
    args:
    - &id001 !!python/name:pybullet_envs.minitaur.envs.minitaur_trotting_env.MinitaurTrottingEnv ''
    state: !!python/tuple
    - *id001
    - !!python/tuple []
    - env_randomizer: null
      motor_kd: 0.015
      num_steps_to_log: 1000
      pd_latency: 0.003
      remove_default_joint_damping: true
      render: false
      urdf_version: rainbow_dash_v0
    - null
  eval_episodes: 25
  init_logstd: -0.6325707791047228
  init_mean_factor: 0.6508531688665261
  kl_cutoff_coef: 1000
  kl_cutoff_factor: 2
  kl_init_penalty: 1
  kl_target: 0.01
  logdir: /cns/ij-d/home/jietan/experiment/minitaur_vizier_study_ppo/mintrot_nonexp_nr_01_186515603_186518344/373
  max_length: 1000
  network: !!python/name:pybullet_envs.minitaur.agents.scripts.networks.ForwardGaussianPolicy ''
  network_config: {}
  num_agents: 25
  policy_layers: !!python/tuple
  - 133
  - 100
  policy_lr: 0.00048104185841752015
  policy_optimizer: AdamOptimizer
  steps: 7000000.0
  update_epochs_policy: 25
  update_epochs_value: 25
  update_every: 25
  use_gpu: false
  value_layers: !!python/tuple
  - 64
  - 57
  value_lr: 0.0012786382882055453
  value_optimizer: AdamOptimizer
  weight_summaries:
    all: .*
    policy: .*/policy/.*
    value: .*/value/.*
state:
  _mutable: false

```

## Python signatures and reward/observation bodies (385 files)


### examples/pybullet/examples/hand.py

```
def getSerialOrNone(portname)
def convertSensor(x, fingerIndex)
```

### examples/pybullet/examples/vrhand.py

```
def convertSensor(x)
```

### examples/pybullet/examples/vrhand_vive_tracker.py

```
def convertSensor(x)
def getSerialOrNone(portname)
```

### examples/pybullet/gym/pybullet_envs/ARS/ars.py

```
class Hp()
    def __init__(self)
def ExploreWorker(rank, childPipe, envname, args)
class Normalizer()
    def __init__(self, nb_inputs)
    def observe(self, x)
    def normalize(self, inputs)
class Policy()
    def __init__(self, input_size, output_size, env_name, args)
    def evaluate(self, input, delta, direction, hp)
    def sample_deltas(self)
    def update(self, rollouts, sigma_r, args)
def explore(env, normalizer, policy, direction, delta, hp)
def train(env, policy, normalizer, hp, parentPipes, args)
def mkdir(base, name)
```

### examples/pybullet/gym/pybullet_envs/__init__.py

```
def register(id)
def getList()
```

### examples/pybullet/gym/pybullet_envs/agents/__init__.py

```
"""Executable scripts for reinforcement learning."""
```

### examples/pybullet/gym/pybullet_envs/agents/configs.py

```
"""Example configurations using the PPO algorithm."""
def default()
def pybullet_pendulum()
def pybullet_doublependulum()
def pybullet_pendulumswingup()
def pybullet_cheetah()
def pybullet_ant()
def pybullet_kuka_grasping()
def pybullet_racecar()
def pybullet_humanoid()
def pybullet_minitaur()
def pybullet_duck_minitaur()
```

### examples/pybullet/gym/pybullet_envs/agents/networks.py

```
"""Network definitions for the PPO algorithm."""
def feed_forward_gaussian(config, action_size, observations, unused_length, state)
def recurrent_gaussian(config, action_size, observations, length, state)
```

### examples/pybullet/gym/pybullet_envs/agents/ppo/__init__.py

```
"""Proximal Policy Optimization algorithm."""
```

### examples/pybullet/gym/pybullet_envs/agents/ppo/algorithm.py

```
"""Proximal Policy Optimization algorithm.

Based on John Schulman's implementation in Python and Theano:
https://github.com/joschu/modular_rl/blob/master/modular_rl/ppo.py"""
class PPOAlgorithm(object)
    """A vectorized implementation of the PPO algorithm by John Schulman."""
    def __init__(self, batch_env, step, is_training, should_log, config)
    def begin_episode(self, agent_indices)
    def perform(self, agent_indices, observ)
    def experience(self, agent_indices, observ, action, reward, unused_done, unused_nextob)
    def _define_experience(self, agent_indices, observ, action, reward)
    def end_episode(self, agent_indices)
    def _define_end_episode(self, agent_indices)
    def _training(self)
    def _perform_update_steps(self, observ, action, old_mean, old_logstd, reward, length)
    def _update_step(self, observ, action, old_mean, old_logstd, reward, advantage, length)
    def _value_loss(self, observ, reward, length)
    def _policy_loss(self, mean, logstd, old_mean, old_logstd, action, advantage, length)
    def _adjust_penalty(self, observ, old_mean, old_logstd, length)
    def _mask(self, tensor, length)
```

### examples/pybullet/gym/pybullet_envs/agents/ppo/memory.py

```
"""Memory that stores episodes."""
class EpisodeMemory(object)
    """Memory that stores episodes."""
    def __init__(self, template, capacity, max_length, scope)
    def length(self, rows)
    def append(self, transitions, rows)
    def replace(self, episodes, length, rows)
    def data(self, rows)
    def clear(self, rows)
```

### examples/pybullet/gym/pybullet_envs/agents/ppo/normalize.py

```
"""Normalize tensors based on streaming estimates of mean and variance."""
class StreamingNormalize(object)
    """Normalize tensors based on streaming estimates of mean and variance."""
    def __init__(self, template, center, scale, clip, name)
    def transform(self, value)
    def update(self, value)
    def reset(self)
    def summary(self)
    def _std(self)
    def _summary(self, name, tensor)
```

### examples/pybullet/gym/pybullet_envs/agents/ppo/utility.py

```
"""Utilities for the PPO algorithm."""
def reinit_nested_vars(variables, indices)
def assign_nested_vars(variables, tensors, indices)
def discounted_return(reward, length, discount)
def fixed_step_return(reward, value, length, discount, window)
def lambda_return(reward, value, length, discount, lambda_)
def lambda_advantage(reward, value, length, discount)
def diag_normal_kl(mean0, logstd0, mean1, logstd1)
def diag_normal_logpdf(mean, logstd, loc)
def diag_normal_entropy(mean, logstd)
def available_gpus()
def gradient_summaries(grad_vars, groups, scope)
def variable_summaries(vars_, groups, scope)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/__init__.py

```
"""Tools for reinforcement learning."""
```

### examples/pybullet/gym/pybullet_envs/agents/tools/attr_dict.py

```
"""Wrap a dictionary to access keys as attributes."""
class AttrDict(dict)
    """Wrap a dictionary to access keys as attributes."""
    def __init__(self)
    def __getattr__(self, key)
    def __setattr__(self, key, value)
    def unlocked(self)
    def copy(self)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/batch_env.py

```
"""Combine multiple environments to step them in batch."""
class BatchEnv(object)
    """Combine multiple environments to step them in batch."""
    def __init__(self, envs, blocking)
    def __len__(self)
    def __getitem__(self, index)
    def __getattr__(self, name)
    def step(self, actions)
    def reset(self, indices)
    def close(self)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/count_weights.py

```
"""Count learnable parameters."""
def count_weights(scope, exclude, graph)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/in_graph_batch_env.py

```
"""Batch of environments inside the TensorFlow graph."""
class InGraphBatchEnv(object)
    """Batch of environments inside the TensorFlow graph.

The batch of environments will be stepped and reset inside of the graph using
a tf.py_func(). The current batch of observations, actions, rewards, and done
flags are held in according variables."""
    def __init__(self, batch_env)
    def __getattr__(self, name)
    def __len__(self)
    def __getitem__(self, index)
    def simulate(self, action)
    def reset(self, indices)
    def observ(self)
    def action(self)
    def reward(self)
    def done(self)
    def close(self)
    def _parse_shape(self, space)
    def _parse_dtype(self, space)

```python
def reward(self):
    """Access the variable holding the current reward."""
    return self._reward
```
```

### examples/pybullet/gym/pybullet_envs/agents/tools/in_graph_env.py

```
"""Put an OpenAI Gym environment into the TensorFlow graph."""
class InGraphEnv(object)
    """Put an OpenAI Gym environment into the TensorFlow graph.

The environment will be stepped and reset inside of the graph using
tf.py_func(). The current observation, action, reward, and done flag are held
in according variables."""
    def __init__(self, env)
    def __getattr__(self, name)
    def simulate(self, action)
    def reset(self)
    def observ(self)
    def action(self)
    def reward(self)
    def done(self)
    def step(self)
    def _parse_shape(self, space)
    def _parse_dtype(self, space)

```python
def reward(self):
    """Access the variable holding the current reward."""
    return self._reward
```
```

### examples/pybullet/gym/pybullet_envs/agents/tools/loop.py

```
"""Execute operations in a loop and coordinate logging and checkpoints."""
class Loop(object)
    """Execute operations in a loop and coordinate logging and checkpoints.

Supports multiple phases, that define their own operations to run, and
intervals for reporting scores, logging summaries, and storing checkpoints.
All class state is stored in-graph to properly recover from checkpoints."""
    def __init__(self, logdir, step, log, report, reset)
    def add_phase(self, name, done, score, summary, steps, report_every, log_every, checkpoint_every, feed)
    def run(self, sess, saver, max_step)
    def _is_every_steps(self, phase_step, batch, every)
    def _find_current_phase(self, global_step)
    def _define_step(self, done, score, summary)
    def _store_checkpoint(self, sess, saver, global_step)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/mock_algorithm.py

```
"""Mock algorithm for testing reinforcement learning code."""
class MockAlgorithm(object)
    """Produce random actions and empty summaries."""
    def __init__(self, envs)
    def begin_episode(self, unused_agent_indices)
    def perform(self, agent_indices, unused_observ)
    def experience(self, unused_agent_indices)
    def end_episode(self, unused_agent_indices)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/mock_environment.py

```
"""Mock environment for testing reinforcement learning code."""
class MockEnvironment(object)
    """Generate random agent input and keep track of statistics."""
    def __init__(self, observ_shape, action_shape, min_duration, max_duration)
    def observation_space(self)
    def action_space(self)
    def unwrapped(self)
    def step(self, action)
    def reset(self)
    def _current_observation(self)
    def _current_reward(self)

```python
def observation_space(self):
    low = np.zeros(self._observ_shape)
    high = np.ones(self._observ_shape)
    return gym.spaces.Box(low, high)
```

```python
def _current_observation(self):
    return self._random.uniform(0, 1, self._observ_shape)
```

```python
def _current_reward(self):
    return self._random.uniform(-1, 1)
```
```

### examples/pybullet/gym/pybullet_envs/agents/tools/simulate.py

```
"""In-graph simulation step of a vectorized algorithm with environments."""
def simulate(batch_env, algo, log, reset)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/streaming_mean.py

```
"""Compute a streaming estimation of the mean of submitted tensors."""
class StreamingMean(object)
    """Compute a streaming estimation of the mean of submitted tensors."""
    def __init__(self, shape, dtype)
    def value(self)
    def count(self)
    def submit(self, value)
    def clear(self)
```

### examples/pybullet/gym/pybullet_envs/agents/tools/wrappers.py

```
"""Wrappers for OpenAI Gym environments."""
class AutoReset(object)
    """Automatically reset environment when the episode is done."""
    def __init__(self, env)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
class ActionRepeat(object)
    """Repeat the agent action multiple steps."""
    def __init__(self, env, amount)
    def __getattr__(self, name)
    def step(self, action)
class RandomStart(object)
    """Perform random number of random actions at the start of the episode."""
    def __init__(self, env, max_steps)
    def __getattr__(self, name)
    def reset(self)
class FrameHistory(object)
    """Augment the observation with past observations."""
    def __init__(self, env, past_indices, flatten)
    def __getattr__(self, name)
    def observation_space(self)
    def step(self, action)
    def reset(self)
    def _select_frames(self)
class FrameDelta(object)
    """Convert the observation to a difference from the previous observation."""
    def __init__(self, env)
    def __getattr__(self, name)
    def observation_space(self)
    def step(self, action)
    def reset(self)
class RangeNormalize(object)
    """Normalize the specialized observation and action ranges to [-1, 1]."""
    def __init__(self, env, observ, action)
    def __getattr__(self, name)
    def observation_space(self)
    def action_space(self)
    def step(self, action)
    def reset(self)
    def _denormalize_action(self, action)
    def _normalize_observ(self, observ)
    def _is_finite(self, space)
class ClipAction(object)
    """Clip out of range actions to the action space of the environment."""
    def __init__(self, env)
    def __getattr__(self, name)
    def action_space(self)
    def step(self, action)
class LimitDuration(object)
    """End episodes after specified number of steps."""
    def __init__(self, env, duration)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
class ExternalProcess(object)
    """Step environment in a separate process for lock free paralellism."""
    def __init__(self, constructor)
    def observation_space(self)
    def action_space(self)
    def __getattr__(self, name)
    def call(self, name)
    def close(self)
    def step(self, action, blocking)
    def reset(self, blocking)
    def _receive(self)
    def _worker(self, constructor, conn)
class ConvertTo32Bit(object)
    """Convert data types of an OpenAI Gym environment to 32 bit."""
    def __init__(self, env)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
    def _convert_observ(self, observ)
    def _convert_reward(self, reward)

```python
def observation_space(self):
    low = self._env.observation_space.low
    high = self._env.observation_space.high
    low = np.repeat(low[None, ...], len(self._past_indices), 0)
    high = np.repeat(high[None, ...], len(self._past_indices), 0)
    if self._flatten:
      low = np.reshape(low, (-1,) + low.shape[2:])
      high = np.reshape(high, (-1,) + high.shape[2:])
    return gym.spaces.Box(low, high)
```

```python
def observation_space(self):
    low = self._env.observation_space.low
    high = self._env.observation_space.high
    low, high = low - high, high - low
    return gym.spaces.Box(low, high)
```

```python
def observation_space(self):
    space = self._env.observation_space
    if not self._should_normalize_observ:
      return space
    return gym.spaces.Box(-np.ones(space.shape), np.ones(space.shape))
```

```python
def observation_space(self):
    if not self._observ_space:
      self._observ_space = self.__getattr__('observation_space')
    return self._observ_space
```

```python
def _convert_reward(self, reward):
    """Convert the reward to 32 bits.

    Args:
      reward: Numpy reward.

    Raises:
      ValueError: Rewards contain infinite values.

    Returns:
      Numpy reward with 32-bit data type.
    """
    if not np.isfinite(reward).all():
      raise ValueError('Infinite reward encountered.')
    return np.array(reward, dtype=np.float32)
```
```

### examples/pybullet/gym/pybullet_envs/agents/train_ppo.py

```
"""Script to train a batch reinforcement learning algorithm.

Command line:

  python3 -m agents.scripts.train --logdir=/path/to/logdir --config=pendulum"""
def _create_environment(config)
def _define_loop(graph, logdir, train_steps, eval_steps)
def train(config, env_processes)
def main(_)
```

### examples/pybullet/gym/pybullet_envs/agents/utility.py

```
"""Utilities for using reinforcement learning algorithms."""
def define_simulation_graph(batch_env, algo_cls, config)
def define_batch_env(constructor, num_agents, env_processes)
def define_saver(exclude)
def initialize_variables(sess, saver, logdir, checkpoint, resume)
def save_config(config, logdir)
def load_config(logdir)
def set_up_logging()
```

### examples/pybullet/gym/pybullet_envs/agents/visualize_ppo.py

```
"""Script to render videos of the Proximal Policy Gradient algorithm.

Command line:

  python3 -m agents.scripts.visualize \
      --logdir=/path/to/logdir/<time>-<config> --outdir=/path/to/outdir/"""
def _create_environment(config, outdir)
def _define_loop(graph, eval_steps)
def visualize(logdir, outdir, num_agents, num_episodes, checkpoint, env_processes)
def main(_)
```

### examples/pybullet/gym/pybullet_envs/baselines/enjoy_kuka_diverse_object_grasping.py

```
"""Runs a random policy for the random object KukaDiverseObjectEnv."""
class ContinuousDownwardBiasPolicy(object)
    """Policy which takes continuous actions, and is biased to move down.
  """
    def __init__(self, height_hack_prob)
    def sample_action(self, obs, explore_prob)
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/enjoy_kuka_grasping.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/enjoy_pybullet_cartpole.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/enjoy_pybullet_racecar.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/enjoy_pybullet_zed_racecar.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/train_kuka_cam_grasping.py

```
def callback(lcl, glb)
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/train_kuka_grasping.py

```
def callback(lcl, glb)
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/train_pybullet_cartpole.py

```
def callback(lcl, glb)
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/train_pybullet_racecar.py

```
def callback(lcl, glb)
def main()
```

### examples/pybullet/gym/pybullet_envs/baselines/train_pybullet_zed_racecar.py

```
def callback(lcl, glb)
def main()
```

### examples/pybullet/gym/pybullet_envs/bullet/cartpole_bullet.py

```
"""Classic cart-pole system implemented by Rich Sutton et al.
Copied from http://incompleteideas.net/book/code/pole.c"""
class CartPoleBulletEnv(Env)
    def __init__(self, renders, discrete_actions)
    def _configure(self, display)
    def seed(self, seed)
    def step(self, action)
    def reset(self)
    def render(self, mode, close)
    def configure(self, args)
    def close(self)
class CartPoleContinuousBulletEnv(CartPoleBulletEnv)
    def __init__(self, renders)
```

### examples/pybullet/gym/pybullet_envs/bullet/env_randomizer_base.py

```
"""Abstract base class for environment randomizer."""
class EnvRandomizerBase(object)
    """Abstract base class for environment randomizer.

An EnvRandomizer is called in environment.reset(). It will
randomize physical parameters of the objects in the simulation.
The physical parameters will be fixed for that episode and be
randomized again in the next environment.reset()."""
    def randomize_env(self, env)
```

### examples/pybullet/gym/pybullet_envs/bullet/kuka.py

```
class Kuka()
    def __init__(self, urdfRootPath, timeStep)
    def reset(self)
    def getActionDimension(self)
    def getObservationDimension(self)
    def getObservation(self)
    def applyAction(self, motorCommands)

```python
def getObservationDimension(self):
    return len(self.getObservation())
```

```python
def getObservation(self):
    observation = []
    state = p.getLinkState(self.kukaUid, self.kukaGripperIndex)
    pos = state[0]
    orn = state[1]
    euler = p.getEulerFromQuaternion(orn)

    observation.extend(list(pos))
    observation.extend(list(euler))

    return observation
```
```

### examples/pybullet/gym/pybullet_envs/bullet/kukaCamGymEnv.py

```
class KukaCamGymEnv(Env)
    def __init__(self, urdfRoot, actionRepeat, isEnableSelfCollision, renders, isDiscrete)
    def reset(self)
    def __del__(self)
    def seed(self, seed)
    def getExtendedObservation(self)
    def step(self, action)
    def step2(self, action)
    def render(self, mode, close)
    def _termination(self)
    def _reward(self)

```python
def getExtendedObservation(self):

    #camEyePos = [0.03,0.236,0.54]
    #distance = 1.06
    #pitch=-56
    #yaw = 258
    #roll=0
    #upAxisIndex = 2
    #camInfo = p.getDebugVisualizerCamera()
    #print("width,height")
    #print(camInfo[0])
    #print(camInfo[1])
    #print("viewMatrix")
    #print(camInfo[2])
    #print("projectionMatrix")
    #print(camInfo[3])
    #viewMat = camInfo[2]
    #viewMat = p.computeViewMatrixFromYawPitchRoll(camEyePos,distance,yaw, pitch,roll,upAxisIndex)
    viewMat = [
        -0.5120397806167603, 0.7171027660369873, -0.47284144163131714, 0.0, -0.8589617609977722,
        -0.42747554183006287, 0.28186774253845215, 0.0, 0.0, 0.5504802465438843,
        0.8348482847213745, 0.0, 0.1925382763147354, -0.24935829639434814, -0.4401884973049164, 1.0
    ]
    #projMatrix = camInfo[3]#[0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0]
    projMatrix = [
        0.75, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0,
        -0.02000020071864128, 0.0
    ]

    img_arr = p.getCameraImage(width=self._width,
                               height=self._height,
                               viewMatrix=viewMat,
                               projectionMatrix=projMatrix)
    rgb = img_arr[2]
    np_img_arr = np.reshape(rgb, (self._height, self._width, 4))
    self._observation = np_img_arr
    return self._observation
```

```python
def _reward(self):

    #rewards is height of target object
    blockPos, blockOrn = p.getBasePositionAndOrientation(self.blockUid)
    closestPoints = p.getClosestPoints(self.blockUid, self._kuka.kukaUid, 1000, -1,
                                       self._kuka.kukaEndEffectorIndex)

    reward = -1000
    numPt = len(closestPoints)
    #print(numPt)
    if (numPt > 0):
      #print("reward:")
      reward = -closestPoints[0][8] * 10
    if (blockPos[2] > 0.2):
      #print("grasped a block!!!")
      #print("self._envStepCounter")
      #print(self._envStepCounter)
      reward = reward + 1000

    #print("reward")
    #print(reward)
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/bullet/kukaGymEnv.py

```
class KukaGymEnv(Env)
    def __init__(self, urdfRoot, actionRepeat, isEnableSelfCollision, renders, isDiscrete, maxSteps)
    def reset(self)
    def __del__(self)
    def seed(self, seed)
    def getExtendedObservation(self)
    def step(self, action)
    def step2(self, action)
    def render(self, mode, close)
    def _termination(self)
    def _reward(self)

```python
def getExtendedObservation(self):
    self._observation = self._kuka.getObservation()
    gripperState = p.getLinkState(self._kuka.kukaUid, self._kuka.kukaGripperIndex)
    gripperPos = gripperState[0]
    gripperOrn = gripperState[1]
    blockPos, blockOrn = p.getBasePositionAndOrientation(self.blockUid)

    invGripperPos, invGripperOrn = p.invertTransform(gripperPos, gripperOrn)
    gripperMat = p.getMatrixFromQuaternion(gripperOrn)
    dir0 = [gripperMat[0], gripperMat[3], gripperMat[6]]
    dir1 = [gripperMat[1], gripperMat[4], gripperMat[7]]
    dir2 = [gripperMat[2], gripperMat[5], gripperMat[8]]

    gripperEul = p.getEulerFromQuaternion(gripperOrn)
    #print("gripperEul")
    #print(gripperEul)
    blockPosInGripper, blockOrnInGripper = p.multiplyTransforms(invGripperPos, invGripperOrn,
                                                                blockPos, blockOrn)
    projectedBlockPos2D = [blockPosInGripper[0], blockPosInGripper[1]]
    blockEulerInGripper = p.getEulerFromQuaternion(blockOrnInGripper)
    #print("projectedBlockPos2D")
    #print(projectedBlockPos2D)
    #print("blockEulerInGripper")
    #print(blockEulerInGripper)

    #we return the relative x,y position and euler angle of block in gripper space
    blockInGripperPosXYEulZ = [blockPosInGripper[0], blockPosInGripper[1], blockEulerInGripper[2]]

    #p.addUserDebugLine(gripperPos,[gripperPos[0]+dir0[0],gripperPos[1]+dir0[1],gripperPos[2]+dir0[2]],[1,0,0],lifeTime=1)
    #p.addUserDebugLine(gripperPos,[gripperPos[0]+dir1[0],gripperPos[1]+dir1[1],gripperPos[2]+dir1[2]],[0,1,0],lifeTime=1)
    #p.addUserDebugLine(gripperPos,[gripperPos[0]+dir2[0],gripperPos[1]+dir2[1],gripperPos[2]+dir2[2]],[0,0,1],lifeTime=1)

    self._observation.extend(list(blockInGripperPosXYEulZ))
    return self._observation
```

```python
def _reward(self):

    #rewards is height of target object
    blockPos, blockOrn = p.getBasePositionAndOrientation(self.blockUid)
    closestPoints = p.getClosestPoints(self.blockUid, self._kuka.kukaUid, 1000, -1,
                                       self._kuka.kukaEndEffectorIndex)

    reward = -1000

    numPt = len(closestPoints)
    #print(numPt)
    if (numPt > 0):
      #print("reward:")
      reward = -closestPoints[0][8] * 10
    if (blockPos[2] > 0.2):
      reward = reward + 10000
      print("successfully grasped a block!!!")
      #print("self._envStepCounter")
      #print(self._envStepCounter)
      #print("self._envStepCounter")
      #print(self._envStepCounter)
      #print("reward")
      #print(reward)
    #print("reward")
    #print(reward)
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/bullet/kuka_diverse_object_gym_env.py

```
class KukaDiverseObjectEnv(KukaGymEnv)
    """Class for Kuka environment with diverse objects.

In each episode some objects are chosen from a set of 1000 diverse objects.
These 1000 objects are split 90/10 into a train and test set."""
    def __init__(self, urdfRoot, actionRepeat, isEnableSelfCollision, renders, isDiscrete, maxSteps, dv, removeHeightHack, blockRandom, cameraRandom, width, height, numObjects, isTest)
    def reset(self)
    def _randomly_place_objects(self, urdfList)
    def _get_observation(self)
    def step(self, action)
    def _step_continuous(self, action)
    def _reward(self)
    def _termination(self)
    def _get_random_object(self, num_objects, test)

```python
def _get_observation(self):
    """Return the observation as an image.
    """
    img_arr = p.getCameraImage(width=self._width,
                               height=self._height,
                               viewMatrix=self._view_matrix,
                               projectionMatrix=self._proj_matrix)
    rgb = img_arr[2]
    np_img_arr = np.reshape(rgb, (self._height, self._width, 4))
    return np_img_arr[:, :, :3]
```

```python
def _reward(self):
    """Calculates the reward for the episode.

    The reward is 1 if one of the objects is above height .2 at the end of the
    episode.
    """
    reward = 0
    self._graspSuccess = 0
    for uid in self._objectUids:
      pos, _ = p.getBasePositionAndOrientation(uid)
      # If any block is above height, provide reward.
      if pos[2] > 0.2:
        self._graspSuccess += 1
        reward = 1
        break
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/bullet/minitaur.py

```
"""This file implements the functionalities of a minitaur using pybullet."""
class Minitaur(object)
    """The minitaur class that simulates a quadruped robot from Ghost Robotics.

  """
    def __init__(self, pybullet_client, urdf_root, time_step, self_collision_enabled, motor_velocity_limit, pd_control_enabled, accurate_motor_model_enabled, motor_kp, motor_kd, torque_control_enabled, motor_overheat_protection, on_rack, kd_for_pd_controllers)
    def _RecordMassInfoFromURDF(self)
    def _BuildJointNameToIdDict(self)
    def _BuildMotorIdList(self)
    def Reset(self, reload_urdf)
    def _SetMotorTorqueById(self, motor_id, torque)
    def _SetDesiredMotorAngleById(self, motor_id, desired_angle)
    def _SetDesiredMotorAngleByName(self, motor_name, desired_angle)
    def ResetPose(self, add_constraint)
    def _ResetPoseForLeg(self, leg_id, add_constraint)
    def GetBasePosition(self)
    def GetBaseOrientation(self)
    def GetActionDimension(self)
    def GetObservationUpperBound(self)
    def GetObservationLowerBound(self)
    def GetObservationDimension(self)
    def GetObservation(self)
    def ApplyAction(self, motor_commands)
    def GetMotorAngles(self)
    def GetMotorVelocities(self)
    def GetMotorTorques(self)
    def ConvertFromLegModel(self, actions)
    def GetBaseMassFromURDF(self)
    def GetLegMassesFromURDF(self)
    def SetBaseMass(self, base_mass)
    def SetLegMasses(self, leg_masses)
    def SetFootFriction(self, foot_friction)
    def SetBatteryVoltage(self, voltage)
    def SetMotorViscousDamping(self, viscous_damping)

```python
def GetObservationUpperBound(self):
    """Get the upper bound of the observation.

    Returns:
      The upper bound of an observation. See GetObservation() for the details
        of each element of an observation.
    """
    upper_bound = np.array([0.0] * self.GetObservationDimension())
    upper_bound[0:self.num_motors] = math.pi  # Joint angle.
    upper_bound[self.num_motors:2 * self.num_motors] = (motor.MOTOR_SPEED_LIMIT)  # Joint velocity.
    upper_bound[2 * self.num_motors:3 * self.num_motors] = (motor.OBSERVED_TORQUE_LIMIT
                                                           )  # Joint torque.
    upper_bound[3 * self.num_motors:] = 1.0  # Quaternion of base orientation.
    return upper_bound
```

```python
def GetObservationLowerBound(self):
    """Get the lower bound of the observation."""
    return -self.GetObservationUpperBound()
```

```python
def GetObservationDimension(self):
    """Get the length of the observation list.

    Returns:
      The length of the observation list.
    """
    return len(self.GetObservation())
```

```python
def GetObservation(self):
    """Get the observations of minitaur.

    It includes the angles, velocities, torques and the orientation of the base.

    Returns:
      The observation list. observation[0:8] are motor angles. observation[8:16]
      are motor velocities, observation[16:24] are motor torques.
      observation[24:28] is the orientation of the base, in quaternion form.
    """
    observation = []
    observation.extend(self.GetMotorAngles().tolist())
    observation.extend(self.GetMotorVelocities().tolist())
    observation.extend(self.GetMotorTorques().tolist())
    observation.extend(list(self.GetBaseOrientation()))
    return observation
```
```

### examples/pybullet/gym/pybullet_envs/bullet/minitaur_duck_gym_env.py

```
"""This file implements the gym environment of minitaur."""
class MinitaurBulletDuckEnv(Env)
    """The gym environment for the minitaur.

It simulates the locomotion of a minitaur, a quadruped robot. The state space
include the angles, velocities and torques for all the motors and the action
space is the desired motor angle for each motor. The reward function is based
on how far the minitaur walk"""
    def __init__(self, urdf_root, action_repeat, distance_weight, energy_weight, shake_weight, drift_weight, distance_limit, observation_noise_stdev, self_collision_enabled, motor_velocity_limit, pd_control_enabled, leg_model_enabled, accurate_motor_model_enabled, motor_kp, motor_kd, torque_control_enabled, motor_overheat_protection, hard_reset, on_rack, render, kd_for_pd_controllers, env_randomizer)
    def set_env_randomizer(self, env_randomizer)
    def configure(self, args)
    def reset(self)
    def seed(self, seed)
    def _transform_action_to_motor_command(self, action)
    def step(self, action)
    def render(self, mode, close)
    def get_minitaur_motor_angles(self)
    def get_minitaur_motor_velocities(self)
    def get_minitaur_motor_torques(self)
    def get_minitaur_base_orientation(self)
    def lost_duck(self)
    def is_fallen(self)
    def _termination(self)
    def _reward(self)
    def get_objectives(self)
    def _get_observation(self)
    def _noisy_observation(self)

```python
def _reward(self):
    current_base_position = self.minitaur.GetBasePosition()
    forward_reward = current_base_position[0] - self._last_base_position[0]
    drift_reward = -abs(current_base_position[1] - self._last_base_position[1])
    shake_reward = -abs(current_base_position[2] - self._last_base_position[2])
    self._last_base_position = current_base_position
    energy_reward = np.abs(
        np.dot(self.minitaur.GetMotorTorques(),
               self.minitaur.GetMotorVelocities())) * self._time_step
    reward = (self._distance_weight * forward_reward - self._energy_weight * energy_reward +
              self._drift_weight * drift_reward + self._shake_weight * shake_reward)
    self._objectives.append([forward_reward, energy_reward, drift_reward, shake_reward])
    return reward
```

```python
def _get_observation(self):
    self._observation = self.minitaur.GetObservation()
    return self._observation
```

```python
def _noisy_observation(self):
    self._get_observation()
    observation = np.array(self._observation)
    if self._observation_noise_stdev > 0:
      observation += (
          np.random.normal(scale=self._observation_noise_stdev, size=observation.shape) *
          self.minitaur.GetObservationUpperBound())
    return observation
```
```

### examples/pybullet/gym/pybullet_envs/bullet/minitaur_env_randomizer.py

```
"""Randomize the minitaur_gym_env when reset() is called."""
class MinitaurEnvRandomizer(EnvRandomizerBase)
    """A randomizer that change the minitaur_gym_env during every reset."""
    def __init__(self, minitaur_base_mass_err_range, minitaur_leg_mass_err_range, battery_voltage_range, motor_viscous_damping_range)
    def randomize_env(self, env)
    def _randomize_minitaur(self, minitaur)
```

### examples/pybullet/gym/pybullet_envs/bullet/minitaur_gym_env.py

```
"""This file implements the gym environment of minitaur."""
class MinitaurBulletEnv(Env)
    """The gym environment for the minitaur.

It simulates the locomotion of a minitaur, a quadruped robot. The state space
include the angles, velocities and torques for all the motors and the action
space is the desired motor angle for each motor. The reward function is based
on how far the minitaur walk"""
    def __init__(self, urdf_root, action_repeat, distance_weight, energy_weight, shake_weight, drift_weight, distance_limit, observation_noise_stdev, self_collision_enabled, motor_velocity_limit, pd_control_enabled, leg_model_enabled, accurate_motor_model_enabled, motor_kp, motor_kd, torque_control_enabled, motor_overheat_protection, hard_reset, on_rack, render, kd_for_pd_controllers, env_randomizer)
    def set_env_randomizer(self, env_randomizer)
    def configure(self, args)
    def reset(self)
    def seed(self, seed)
    def _transform_action_to_motor_command(self, action)
    def step(self, action)
    def render(self, mode, close)
    def get_minitaur_motor_angles(self)
    def get_minitaur_motor_velocities(self)
    def get_minitaur_motor_torques(self)
    def get_minitaur_base_orientation(self)
    def is_fallen(self)
    def _termination(self)
    def _reward(self)
    def get_objectives(self)
    def _get_observation(self)
    def _noisy_observation(self)

```python
def _reward(self):
    current_base_position = self.minitaur.GetBasePosition()
    forward_reward = current_base_position[0] - self._last_base_position[0]
    drift_reward = -abs(current_base_position[1] - self._last_base_position[1])
    shake_reward = -abs(current_base_position[2] - self._last_base_position[2])
    self._last_base_position = current_base_position
    energy_reward = np.abs(
        np.dot(self.minitaur.GetMotorTorques(),
               self.minitaur.GetMotorVelocities())) * self._time_step
    reward = (self._distance_weight * forward_reward - self._energy_weight * energy_reward +
              self._drift_weight * drift_reward + self._shake_weight * shake_reward)
    self._objectives.append([forward_reward, energy_reward, drift_reward, shake_reward])
    return reward
```

```python
def _get_observation(self):
    self._observation = self.minitaur.GetObservation()
    return self._observation
```

```python
def _noisy_observation(self):
    self._get_observation()
    observation = np.array(self._observation)
    if self._observation_noise_stdev > 0:
      observation += (
          np.random.normal(scale=self._observation_noise_stdev, size=observation.shape) *
          self.minitaur.GetObservationUpperBound())
    return observation
```
```

### examples/pybullet/gym/pybullet_envs/bullet/motor.py

```
"""This file implements an accurate motor model."""
class MotorModel(object)
    """The accurate motor model, which is based on the physics of DC motors.

The motor model support two types of control: position control and torque
control. In position control mode, a desired motor angle is specified, and a
torque is computed based on the internal motor model. When the torque control
"""
    def __init__(self, torque_control_enabled, kp, kd)
    def set_voltage(self, voltage)
    def get_voltage(self)
    def set_viscous_damping(self, viscous_damping)
    def get_viscous_dampling(self)
    def convert_to_torque(self, motor_commands, current_motor_angle, current_motor_velocity)
    def _convert_to_torque_from_pwm(self, pwm, current_motor_velocity)
```

### examples/pybullet/gym/pybullet_envs/bullet/racecar.py

```
class Racecar()
    def __init__(self, bullet_client, urdfRootPath, timeStep)
    def reset(self)
    def getActionDimension(self)
    def getObservationDimension(self)
    def getObservation(self)
    def applyAction(self, motorCommands)

```python
def getObservationDimension(self):
    return len(self.getObservation())
```

```python
def getObservation(self):
    observation = []
    pos, orn = self._p.getBasePositionAndOrientation(self.racecarUniqueId)

    observation.extend(list(pos))
    observation.extend(list(orn))

    return observation
```
```

### examples/pybullet/gym/pybullet_envs/bullet/racecarGymEnv.py

```
class RacecarGymEnv(Env)
    def __init__(self, urdfRoot, actionRepeat, isEnableSelfCollision, isDiscrete, renders)
    def reset(self)
    def __del__(self)
    def seed(self, seed)
    def getExtendedObservation(self)
    def step(self, action)
    def render(self, mode, close)
    def _termination(self)
    def _reward(self)

```python
def getExtendedObservation(self):
    self._observation = []  #self._racecar.getObservation()
    carpos, carorn = self._p.getBasePositionAndOrientation(self._racecar.racecarUniqueId)
    ballpos, ballorn = self._p.getBasePositionAndOrientation(self._ballUniqueId)
    invCarPos, invCarOrn = self._p.invertTransform(carpos, carorn)
    ballPosInCar, ballOrnInCar = self._p.multiplyTransforms(invCarPos, invCarOrn, ballpos, ballorn)

    self._observation.extend([ballPosInCar[0], ballPosInCar[1]])
    return self._observation
```

```python
def _reward(self):
    closestPoints = self._p.getClosestPoints(self._racecar.racecarUniqueId, self._ballUniqueId,
                                             10000)

    numPt = len(closestPoints)
    reward = -1000
    #print(numPt)
    if (numPt > 0):
      #print("reward:")
      reward = -closestPoints[0][8]
      #print(reward)
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/bullet/racecarZEDGymEnv.py

```
class RacecarZEDGymEnv(Env)
    def __init__(self, urdfRoot, actionRepeat, isEnableSelfCollision, isDiscrete, renders)
    def reset(self)
    def __del__(self)
    def seed(self, seed)
    def getExtendedObservation(self)
    def step(self, action)
    def render(self, mode, close)
    def _termination(self)
    def _reward(self)

```python
def getExtendedObservation(self):
    carpos, carorn = self._p.getBasePositionAndOrientation(self._racecar.racecarUniqueId)
    carmat = self._p.getMatrixFromQuaternion(carorn)
    ballpos, ballorn = self._p.getBasePositionAndOrientation(self._ballUniqueId)
    invCarPos, invCarOrn = self._p.invertTransform(carpos, carorn)
    ballPosInCar, ballOrnInCar = self._p.multiplyTransforms(invCarPos, invCarOrn, ballpos, ballorn)
    dist0 = 0.3
    dist1 = 1.
    eyePos = [
        carpos[0] + dist0 * carmat[0], carpos[1] + dist0 * carmat[3],
        carpos[2] + dist0 * carmat[6] + 0.3
    ]
    targetPos = [
        carpos[0] + dist1 * carmat[0], carpos[1] + dist1 * carmat[3],
        carpos[2] + dist1 * carmat[6] + 0.3
    ]
    up = [carmat[2], carmat[5], carmat[8]]
    viewMat = self._p.computeViewMatrix(eyePos, targetPos, up)
    #viewMat = self._p.computeViewMatrixFromYawPitchRoll(carpos,1,0,0,0,2)
    #print("projectionMatrix:")
    #print(self._p.getDebugVisualizerCamera()[3])
    projMatrix = [
        0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0,
        0.0, 0.0, -0.02000020071864128, 0.0
    ]
    img_arr = self._p.getCameraImage(width=self._width,
                                     height=self._height,
                                     viewMatrix=viewMat,
                                     projectionMatrix=projMatrix)
    rgb = img_arr[2]
    np_img_arr = np.reshape(rgb, (self._height, self._width, 4))
    self._observation = np_img_arr
    return self._observation
```

```python
def _reward(self):
    closestPoints = self._p.getClosestPoints(self._racecar.racecarUniqueId, self._ballUniqueId,
                                             10000)

    numPt = len(closestPoints)
    reward = -1000
    #print(numPt)
    if (numPt > 0):
      #print("reward:")
      reward = -closestPoints[0][8]
      #print(reward)
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/DeepMimic_Optimizer.py

```
def run()
def shutdown()
def main()
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/DeepMimic_Optimizer_multiclip.py

```
def run()
def shutdown()
def main()
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/action_space.py

```
class ActionSpace(Enum)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/env.py

```
class Env(ABC)
    def __init__(self, args, enable_draw)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/humanoid_pose_interpolator.py

```
class HumanoidPoseInterpolator(object)
    def __init__(self)
    def Reset(self, basePos, baseOrn, chestRot, neckRot, rightHipRot, rightKneeRot, rightAnkleRot, rightShoulderRot, rightElbowRot, leftHipRot, leftKneeRot, leftAnkleRot, leftShoulderRot, leftElbowRot, baseLinVel, baseAngVel, chestVel, neckVel, rightHipVel, rightKneeVel, rightAnkleVel, rightShoulderVel, rightElbowVel, leftHipVel, leftKneeVel, leftAnkleVel, leftShoulderVel, leftElbowVel)
    def ComputeLinVel(self, posStart, posEnd, deltaTime)
    def ComputeAngVel(self, ornStart, ornEnd, deltaTime, bullet_client)
    def ComputeAngVelRel(self, ornStart, ornEnd, deltaTime, bullet_client)
    def NormalizeVector(self, vec)
    def NormalizeQuaternion(self, orn)
    def PostProcessMotionData(self, frameData)
    def GetPose(self)
    def Slerp(self, frameFraction, frameData, frameDataNext, bullet_client)
    def ConvertFromAction(self, pybullet_client, action)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/humanoid_stable_pd.py

```
class HumanoidStablePD(object)
    def __init__(self, pybullet_client, mocap_data, timeStep, useFixedBase, arg_parser, useComReward)
    def resetPose(self)
    def initializePose(self, pose, phys_model, initBase, initializeVelocity)
    def calcCycleCount(self, simTime, cycleTime)
    def getCycleTime(self)
    def setSimTime(self, t)
    def computeCycleOffset(self)
    def computePose(self, frameFraction)
    def convertActionToPose(self, action)
    def computeAndApplyPDForces(self, desiredPositions, maxForces)
    def computePDForces(self, desiredPositions, desiredVelocities, maxForces)
    def applyPDForces(self, taus)
    def setJointMotors(self, desiredPositions, maxForces)
    def getPhase(self)
    def buildHeadingTrans(self, rootOrn)
    def buildOriginTrans(self)
    def getState(self)
    def terminates(self)
    def quatMul(self, q1, q2)
    def calcRootAngVelErr(self, vel0, vel1)
    def calcRootRotDiff(self, orn0, orn1)
    def getReward(self, pose)
    def computeCOMposVel(self, uid)

```python
def getReward(self, pose):
    """Compute and return the pose-based reward."""
    #from DeepMimic double cSceneImitate::CalcRewardImitate
    #todo: compensate for ground height in some parts, once we move to non-flat terrain
    # not values from the paper, but from the published code.
    pose_w = 0.5
    vel_w = 0.05
    end_eff_w = 0.15
    # does not exist in paper
    root_w = 0.2
    if self._useComReward:
      com_w = 0.1
    else:
      com_w = 0

    total_w = pose_w + vel_w + end_eff_w + root_w + com_w
    pose_w /= total_w
    vel_w /= total_w
    end_eff_w /= total_w
    root_w /= total_w
    com_w /= total_w

    pose_scale = 2
    vel_scale = 0.1
    end_eff_scale = 40
    root_scale = 5
    com_scale = 10
    err_scale = 1  # error scale

    reward = 0

    pose_err = 0
    vel_err = 0
    end_eff_err = 0
    root_err = 0
    com_err = 0
    heading_err = 0

    #create a mimic reward, comparing the dynamics humanoid with a kinematic one

    #pose = self.InitializePoseFromMotionData()
    #print("self._kin_model=",self._kin_model)
    #print("kinematicHumanoid #joints=",self._pybullet_client.getNumJoints(self._kin_model))
    #self.ApplyPose(pose, True, True, self._kin_model, self._pybullet_client)

    #const Eigen::VectorXd& pose0 = sim_char.GetPose();
    #const Eigen::VectorXd& vel0 = sim_char.GetVel();
    #const Eigen::VectorXd& pose1 = kin_char.GetPose();
    #const Eigen::VectorXd& vel1 = kin_char.GetVel();
    #tMatrix origin_trans = sim_char.BuildOriginTrans();
    #tMatrix kin_origin_trans = kin_char.BuildOriginTrans();
    #
    #tVector com0_world = sim_char.CalcCOM();
    if self._useComReward:
      comSim, comSimVel = self.computeCOMposVel(self._sim_model)
      comKin, comKinVel = self.computeCOMposVel(self._kin_model)
    #tVector com_vel0_world = sim_char.CalcCOMVel();
    #tVector com1_world;
    #tVector com_vel1_world;
    #cRBDUtil::CalcCoM(joint_mat, body_defs, pose1, vel1, com1_world, com_vel1_world);
    #
    root_id = 0
    #tVector root_pos0 = cKinTree::GetRootPos(joint_mat, pose0);
    #tVector root_pos1 = cKinTree::GetRootPos(joint_mat, pose1);
    #tQuaternion root_rot0 = cKinTree::GetRootRot(joint_mat, pose0);
    #tQuaternion root_rot1 = cKinTree::GetRootRot(joint_mat, pose1);
    #tVector root_vel0 = cKinTree::GetRootVel(joint_mat, vel0);
    #tVector root_vel1 = cKinTree::GetRootVel(joint_mat, vel1);
    #tVector root_ang_vel0 = cKinTree::GetRootAngVel(joint_mat, vel0);
    #tVector root_ang_vel1 = cKinTree::GetRootAngVel(joint_mat, vel1);

    mJointWeights = [
        0.20833, 0.10416, 0.0625, 0.10416, 0.0625, 0.041666666666666671, 0.0625, 0.0416, 0.00,
        0.10416, 0.0625, 0.0416, 0.0625, 0.0416, 0.0000
    ]

    num_end_effs = 0
    num_joints = 15

    root_rot_w = mJointWeights[root_id]
    rootPosSim, rootOrnSim = self._pybullet_client.getBasePositionAndOrientation(self._sim_model)
    rootPosKin, rootOrnKin = self._pybullet_client.getBasePositionAndOrientation(self._kin_model)
    linVelSim, angVelSim = self._pybullet_client.getBaseVelocity(self._sim_model)
    #don't read the velocities from the kinematic model (they are zero), use the pose interpolator velocity
    #see also issue https://github.com/bulletphysics/bullet3/issues/2401 
    linVelKin = self._poseInterpolator._baseLinVel
    angVelKin = self._poseInterpolator._baseAngVel

    root_rot_err = self.calcRootRotDiff(rootOrnSim, rootOrnKin)
    pose_err += root_rot_w * root_rot_err

    root_vel_diff = [
        linVelSim[0] - linVelKin[0], linVelSim[1] - linVelKin[1], linVelSim[2] - linVelKin[2]
    ]
    root_vel_err = root_vel_diff[0] * root_vel_diff[0] + root_vel_diff[1] * root_vel_diff[
        1] + root_vel_diff[2] * root_vel_diff[2]

    root_ang_vel_err = self.calcRootAngVelErr(angVelSim, angVelKin)
    vel_err += root_rot_w * root_ang_vel_err

    useArray = True
    
    if useArray:
      jointIndices = range(num_joints)
      simJointStates = self._pybullet_client.getJointStatesMultiDof(s
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/humanoid_stable_pd_multiclip.py

```
class HumanoidStablePDMultiClip(object)
    def __init__(self, pybullet_client, mocap_data, timeStep, useFixedBase, arg_parser, useComReward)
    def resetPose(self)
    def initializePose(self, pose, phys_model, initBase, initializeVelocity)
    def calcCycleCount(self, simTime, cycleTime)
    def getCycleTime(self)
    def setSimTime(self, t)
    def computeCycleOffset(self, i)
    def computePose(self, frameFraction, i)
    def convertActionToPose(self, action, i)
    def computeAndApplyPDForces(self, desiredPositions, maxForces)
    def getPhase(self)
    def buildHeadingTrans(self, rootOrn)
    def buildOriginTrans(self)
    def getState(self)
    def terminates(self)
    def quatMul(self, q1, q2)
    def calcRootAngVelErr(self, vel0, vel1)
    def calcRootRotDiff(self, orn0, orn1)
    def getReward(self, pose, i)
    def computeCOMposVel(self, uid)

```python
def getReward(self, pose, i=0):
        """Compute and return the pose-based reward."""
        # from DeepMimic double cSceneImitate::CalcRewardImitate
        # todo: compensate for ground height in some parts, once we move to non-flat terrain
        # not values from the paper, but from the published code.
        pose_w = 0.5
        vel_w = 0.05
        end_eff_w = 0.15
        # does not exist in paper
        root_w = 0.2
        if self._useComReward:
            com_w = 0.1
        else:
            com_w = 0

        total_w = pose_w + vel_w + end_eff_w + root_w + com_w
        pose_w /= total_w
        vel_w /= total_w
        end_eff_w /= total_w
        root_w /= total_w
        com_w /= total_w

        pose_scale = 2
        vel_scale = 0.1
        end_eff_scale = 40
        root_scale = 5
        com_scale = 10
        err_scale = 1  # error scale

        reward = 0

        pose_err = 0
        vel_err = 0
        end_eff_err = 0
        root_err = 0
        com_err = 0
        heading_err = 0

        # create a mimic reward, comparing the dynamics humanoid with a kinematic one

        if self._useComReward:
            comSim, comSimVel = self.computeCOMposVel(self._sim_model)
            comKin, comKinVel = self.computeCOMposVel(self._kin_models[i])

        root_id = 0

        mJointWeights = [
            0.20833, 0.10416, 0.0625, 0.10416, 0.0625, 0.041666666666666671, 0.0625, 0.0416, 0.00,
            0.10416, 0.0625, 0.0416, 0.0625, 0.0416, 0.0000
        ]

        num_end_effs = 0
        num_joints = 15

        root_rot_w = mJointWeights[root_id]
        rootPosSim, rootOrnSim = self._pybullet_client.getBasePositionAndOrientation(self._sim_model)
        rootPosKin, rootOrnKin = self._pybullet_client.getBasePositionAndOrientation(self._kin_models[i])
        linVelSim, angVelSim = self._pybullet_client.getBaseVelocity(self._sim_model)
        # don't read the velocities from the kinematic model (they are zero), use the pose interpolator velocity
        # see also issue https://github.com/bulletphysics/bullet3/issues/2401
        linVelKin = self._poseInterpolators[i]._baseLinVel
        angVelKin = self._poseInterpolators[i]._baseAngVel

        root_rot_err = self.calcRootRotDiff(rootOrnSim, rootOrnKin)
        pose_err += root_rot_w * root_rot_err

        root_vel_diff = [
            linVelSim[0] - linVelKin[0], linVelSim[1] - linVelKin[1], linVelSim[2] - linVelKin[2]
        ]
        root_vel_err = root_vel_diff[0] * root_vel_diff[0] + root_vel_diff[1] * root_vel_diff[
            1] + root_vel_diff[2] * root_vel_diff[2]

        root_ang_vel_err = self.calcRootAngVelErr(angVelSim, angVelKin)
        vel_err += root_rot_w * root_ang_vel_err

        jointIndices = range(num_joints)
        simJointStates = self._pybullet_client.getJointStatesMultiDof(self._sim_model, jointIndices)
        kinJointStates = self._pybullet_client.getJointStatesMultiDof(self._kin_models[i], jointIndices)
        linkStatesSim = self._pybullet_client.getLinkStates(self._sim_model, jointIndices)
        linkStatesKin = self._pybullet_client.getLinkStates(self._kin_models[i], jointIndices)

        for j in range(num_joints):
            curr_pose_err = 0
            curr_vel_err = 0
            w = mJointWeights[j]

            simJointInfo = simJointStates[j]

            # print("simJointInfo.pos=",simJointInfo[0])
            # print("simJointInfo.vel=",simJointInfo[1])

            kinJointInfo = kinJointStates[j]

            # print("kinJointInfo.pos=",kinJointInfo[0])
            # print("kinJointInfo.vel=",kinJointInfo[1])
            if (len(simJointInfo[0]) == 1):
                angle = simJointInfo[0][0] - kinJointInfo[0][0]
                curr_pose_err = angle * angle
                velDiff = simJointInfo[1][0] - kinJointInfo[1][0]
                curr_vel_err = velDiff * velDiff
            if (len(simJointInfo[0]) == 4):
                # print("quaternion diff")
                diffQuat = self
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/motion_capture_data.py

```
class MotionCaptureData(object)
    def __init__(self)
    def Reset(self)
    def Load(self, path)
    def NumFrames(self)
    def KeyFrameDuraction(self)
    def getCycleTime(self)
    def calcCycleCount(self, simTime, cycleTime)
    def computeCycleOffset(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/motion_capture_data_multiclip.py

```
class MotionCaptureDataMultiClip(object)
    def __init__(self)
    def Reset(self)
    def Load(self, path)
    def getNumFrames(self)
    def getKeyFrameDuration(self, id)
    def getCycleTime(self)
    def calcCycleCount(self, simTime, cycleTime)
    def computeCycleOffset(self, id)
    def getNumClips(self)
    def downsampleClips(self)
    def upsampleClips(self)
    def slerpSingleClip(self, clip, key_times)
    def quatlist_to_quatlists(self, clip)
    def deepmimic_to_scipy_quaternion(self, quat)
    def scipy_to_deepmimic_quaternion(self, quat)
    def calc_inter_times(self, times, method)
    def calc_inter_root_pos(self, root_pos, times, inter_times)
    def quatlists_to_quatlist(self, t, ord_root_pos, ord_rots)
    def merge_quaternions(self, rotations)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/pybullet_deep_mimic_env.py

```
class InitializationStrategy(Enum)
    """Set how the environment is initialized."""
class PyBulletDeepMimicEnv(Env)
    def __init__(self, arg_parser, enable_draw, pybullet_client, time_step, init_strategy)
    def reset(self)
    def get_num_agents(self)
    def get_action_space(self, agent_id)
    def get_reward_min(self, agent_id)
    def get_reward_max(self, agent_id)
    def get_reward_fail(self, agent_id)
    def get_reward_succ(self, agent_id)
    def get_state_size(self, agent_id)
    def build_state_norm_groups(self, agent_id)
    def build_state_offset(self, agent_id)
    def build_state_scale(self, agent_id)
    def get_goal_size(self, agent_id)
    def get_action_size(self, agent_id)
    def build_goal_norm_groups(self, agent_id)
    def build_goal_offset(self, agent_id)
    def build_goal_scale(self, agent_id)
    def build_action_offset(self, agent_id)
    def build_action_scale(self, agent_id)
    def build_action_bound_min(self, agent_id)
    def build_action_bound_max(self, agent_id)
    def set_mode(self, mode)
    def need_new_action(self, agent_id)
    def record_state(self, agent_id)
    def record_goal(self, agent_id)
    def calc_reward(self, agent_id)
    def set_action(self, agent_id, action)
    def log_val(self, agent_id, val)
    def update(self, timeStep)
    def set_sample_count(self, count)
    def check_terminate(self, agent_id)
    def is_episode_end(self)
    def check_valid_episode(self)
    def getKeyboardEvents(self)
    def isKeyTriggered(self, keys, key)

```python
def get_reward_min(self, agent_id):
    return 0
```

```python
def get_reward_max(self, agent_id):
    return 1
```

```python
def get_reward_fail(self, agent_id):
    return self.get_reward_min(agent_id)
```

```python
def get_reward_succ(self, agent_id):
    return self.get_reward_max(agent_id)
```

```python
def calc_reward(self, agent_id):
    kinPose = self._humanoid.computePose(self._humanoid._frameFraction)
    reward = self._humanoid.getReward(kinPose)
    return reward
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/pybullet_deep_mimic_env_multiclip.py

```
class InitializationStrategy(Enum)
    """Set how the environment is initialized."""
class PyBulletDeepMimicEnvMultiClip(Env)
    def __init__(self, arg_parser, enable_draw, pybullet_client, time_step, init_strategy)
    def reset(self)
    def get_num_agents(self)
    def get_action_space(self, agent_id)
    def get_reward_min(self, agent_id)
    def get_reward_max(self, agent_id)
    def get_reward_fail(self, agent_id)
    def get_reward_succ(self, agent_id)
    def get_state_size(self, agent_id)
    def build_state_norm_groups(self, agent_id)
    def build_state_offset(self, agent_id)
    def build_state_scale(self, agent_id)
    def get_goal_size(self, agent_id)
    def get_action_size(self, agent_id)
    def build_goal_norm_groups(self, agent_id)
    def build_goal_offset(self, agent_id)
    def build_goal_scale(self, agent_id)
    def build_action_offset(self, agent_id)
    def build_action_scale(self, agent_id)
    def build_action_bound_min(self, agent_id)
    def build_action_bound_max(self, agent_id)
    def set_mode(self, mode)
    def need_new_action(self, agent_id)
    def record_state(self, agent_id)
    def record_goal(self, agent_id)
    def calc_reward(self, agent_id)
    def set_action(self, agent_id, action)
    def log_val(self, agent_id, val)
    def update(self, timeStep)
    def set_sample_count(self, count)
    def check_terminate(self, agent_id)
    def is_episode_end(self)
    def check_valid_episode(self)
    def getKeyboardEvents(self)
    def isKeyTriggered(self, keys, key)
    def select_reward(self, rewards, criterion)

```python
def get_reward_min(self, agent_id):
        return 0
```

```python
def get_reward_max(self, agent_id):
        return 1
```

```python
def get_reward_fail(self, agent_id):
        return self.get_reward_min(agent_id)
```

```python
def get_reward_succ(self, agent_id):
        return self.get_reward_max(agent_id)
```

```python
def calc_reward(self, agent_id):
        rewards = {}
        for i in range(self._n_clips):
            kinPose = self._humanoid.computePose(self._humanoid._frameFraction, i)
            rewards[i] = self._humanoid.getReward(kinPose, i)
        reward = self.select_reward(rewards)
        return reward
```

```python
def select_reward(self, rewards, criterion=None):
        # todo create enum for criterion
        return max(rewards.values())
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/quadrupedPoseInterpolator.py

```
class QuadrupedPoseInterpolator(object)
    def __init__(self)
    def ComputeLinVel(self, posStart, posEnd, deltaTime)
    def ComputeAngVel(self, ornStart, ornEnd, deltaTime, bullet_client)
    def ComputeAngVelRel(self, ornStart, ornEnd, deltaTime, bullet_client)
    def Slerp(self, frameFraction, frameData, frameDataNext, bullet_client)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/quadruped_stable_pd.py

```
class QuadrupedStablePD(object)
    def __init__(self, pybullet_client, mocap_data, timeStep, useFixedBase)
    def resetPose(self)
    def initializePose(self, pose, phys_model, initBase, initializeVelocity)
    def calcCycleCount(self, simTime, cycleTime)
    def getCycleTime(self)
    def setSimTime(self, t)
    def computeCycleOffset(self)
    def computePose(self, frameFraction)
    def convertActionToPose(self, action)
    def computePDForces(self, desiredPositions, desiredVelocities, maxForces)
    def applyPDForces(self, taus)
    def setJointMotors(self, desiredPositions, maxForces)
    def getPhase(self)
    def buildHeadingTrans(self, rootOrn)
    def buildOriginTrans(self)
    def getState(self)
    def terminates(self)
    def quatMul(self, q1, q2)
    def calcRootAngVelErr(self, vel0, vel1)
    def calcRootRotDiff(self, orn0, orn1)
    def getReward(self, pose)

```python
def getReward(self, pose):
    #from DeepMimic double cSceneImitate::CalcRewardImitate
    #todo: compensate for ground height in some parts, once we move to non-flat terrain
    pose_w = 0.5
    vel_w = 0.05
    end_eff_w = 0.15
    root_w = 0.2
    com_w = 0  #0.1

    total_w = pose_w + vel_w + end_eff_w + root_w + com_w
    pose_w /= total_w
    vel_w /= total_w
    end_eff_w /= total_w
    root_w /= total_w
    com_w /= total_w

    pose_scale = 2
    vel_scale = 0.1
    end_eff_scale = 40
    root_scale = 5
    com_scale = 10
    err_scale = 1

    reward = 0

    pose_err = 0
    vel_err = 0
    end_eff_err = 0
    root_err = 0
    com_err = 0
    heading_err = 0

    #create a mimic reward, comparing the dynamics humanoid with a kinematic one

    #pose = self.InitializePoseFromMotionData()
    #print("self._kin_model=",self._kin_model)
    #print("kinematicHumanoid #joints=",self._pybullet_client.getNumJoints(self._kin_model))
    #self.ApplyPose(pose, True, True, self._kin_model, self._pybullet_client)

    #const Eigen::VectorXd& pose0 = sim_char.GetPose();
    #const Eigen::VectorXd& vel0 = sim_char.GetVel();
    #const Eigen::VectorXd& pose1 = kin_char.GetPose();
    #const Eigen::VectorXd& vel1 = kin_char.GetVel();
    #tMatrix origin_trans = sim_char.BuildOriginTrans();
    #tMatrix kin_origin_trans = kin_char.BuildOriginTrans();
    #
    #tVector com0_world = sim_char.CalcCOM();
    #tVector com_vel0_world = sim_char.CalcCOMVel();
    #tVector com1_world;
    #tVector com_vel1_world;
    #cRBDUtil::CalcCoM(joint_mat, body_defs, pose1, vel1, com1_world, com_vel1_world);
    #
    root_id = 0
    #tVector root_pos0 = cKinTree::GetRootPos(joint_mat, pose0);
    #tVector root_pos1 = cKinTree::GetRootPos(joint_mat, pose1);
    #tQuaternion root_rot0 = cKinTree::GetRootRot(joint_mat, pose0);
    #tQuaternion root_rot1 = cKinTree::GetRootRot(joint_mat, pose1);
    #tVector root_vel0 = cKinTree::GetRootVel(joint_mat, vel0);
    #tVector root_vel1 = cKinTree::GetRootVel(joint_mat, vel1);
    #tVector root_ang_vel0 = cKinTree::GetRootAngVel(joint_mat, vel0);
    #tVector root_ang_vel1 = cKinTree::GetRootAngVel(joint_mat, vel1);

    mJointWeights = [
        0.20833, 0.10416, 0.0625, 0.10416, 0.0625, 0.041666666666666671, 0.0625, 0.0416, 0.00,
        0.10416, 0.0625, 0.0416, 0.0625, 0.0416, 0.0000
    ]

    num_end_effs = 0
    num_joints = 15

    root_rot_w = mJointWeights[root_id]
    rootPosSim, rootOrnSim = self._pybullet_client.getBasePositionAndOrientation(self._sim_model)
    rootPosKin, rootOrnKin = self._pybullet_client.getBasePositionAndOrientation(self._kin_model)
    linVelSim, angVelSim = self._pybullet_client.getBaseVelocity(self._sim_model)
    linVelKin, angVelKin = self._pybullet_client.getBaseVelocity(self._kin_model)

    root_rot_err = self.calcRootRotDiff(rootOrnSim, rootOrnKin)
    pose_err += root_rot_w * root_rot_err

    root_vel_diff = [
        linVelSim[0] - linVelKin[0], linVelSim[1] - linVelKin[1], linVelSim[2] - linVelKin[2]
    ]
    root_vel_err = root_vel_diff[0] * root_vel_diff[0] + root_vel_diff[1] * root_vel_diff[
        1] + root_vel_diff[2] * root_vel_diff[2]

    root_ang_vel_err = self.calcRootAngVelErr(angVelSim, angVelKin)
    vel_err += root_rot_w * root_ang_vel_err

    for j in range(num_joints):
      curr_pose_err = 0
      curr_vel_err = 0
      w = mJointWeights[j]

      simJointInfo = self._pybullet_client.getJointStateMultiDof(self._sim_model, j)

      #print("simJointInfo.pos=",simJointInfo[0])
      #print("simJointInfo.vel=",simJointInfo[1])
      kinJointInfo = self._pybullet_client.getJointStateMultiDof(self._kin_model, j)
      #print("kinJointInfo.pos=",kinJointInfo[0])
      #print("kinJointInfo.vel=",kinJointInfo[1])
      if (len(simJointInfo[0]) == 1):
        angle = simJointInfo[0][0] - kinJointInfo[0][0]
        curr_pose_err = angle * angle
        velDiff = simJointInfo[1][0] - kinJointInfo[1][0]
        curr_vel_err = velDiff * velDiff
      if (
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/env/testHumanoid.py

```
def isKeyTriggered(keys, key)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/gym_env/deep_mimic_env.py

```
"""Classic cart-pole system implemented by Rich Sutton et al.
Copied from https://webdocs.cs.ualberta.ca/~sutton/book/code/pole.c"""
class HumanoidDeepBulletEnv(Env)
    """Base Gym environment for DeepMimic."""
    def __init__(self, renders, arg_file, test_mode, time_step, rescale_actions, rescale_observations)
    def _configure(self, display)
    def seed(self, seed)
    def step(self, action)
    def reset(self)
    def render(self, mode, close)
    def configure(self, args)
    def close(self)
class HumanoidDeepMimicBackflipBulletEnv(HumanoidDeepBulletEnv)
    def __init__(self, renders)
class HumanoidDeepMimicWalkBulletEnv(HumanoidDeepBulletEnv)
    def __init__(self, renders)
class CartPoleContinuousBulletEnv5(HumanoidDeepBulletEnv)
    def __init__(self, renders)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/agent_builder.py

```
def build_agent(world, id, file)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/exp_params.py

```
class ExpParams(object)
    def __init__(self)
    def __str__(self)
    def load(self, json_data)
    def lerp(self, other, t)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/nets/fc_2layers_1024units.py

```
def build_net(input_tfs, reuse)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/nets/net_builder.py

```
def build_net(net_name, input_tfs, reuse)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/normalizer.py

```
class Normalizer(object)
    def __init__(self, size, groups_ids, eps, clip)
    def record(self, x)
    def update(self)
    def get_size(self)
    def set_mean_std(self, mean, std)
    def normalize(self, x)
    def unnormalize(self, norm_x)
    def calc_std(self, mean, mean_sq)
    def calc_mean_sq(self, mean, std)
    def check_synced(self)
    def _build_groups(self, groups_ids)
    def _process_group_data(self, new_data, old_data)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/path.py

```
class Path(object)
    def __init__(self)
    def pathlength(self)
    def is_valid(self)
    def check_vals(self)
    def clear(self)
    def get_pathlen(self)
    def calc_return(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/pg_agent.py

```
class PGAgent(TFAgent)
    def __init__(self, world, id, json_data)
    def reset(self)
    def _check_action_space(self)
    def _load_params(self, json_data)
    def _build_nets(self, json_data)
    def _build_normalizers(self)
    def _init_normalizers(self)
    def _load_normalizers(self)
    def _build_losses(self, json_data)
    def _build_solvers(self, json_data)
    def _build_net_actor(self, net_name, init_output_scale)
    def _build_net_critic(self, net_name)
    def _initialize_vars(self)
    def _sync_solvers(self)
    def _decide_action(self, s, g)
    def _enable_stoch_policy(self)
    def _eval_actor(self, s, g)
    def _eval_critic(self, s, g)
    def _record_flags(self)
    def _train_step(self)
    def _update_critic(self)
    def _update_actor(self)
    def _calc_updated_vals(self, idx)
    def _calc_action_logp(self, norm_action_deltas)
    def _log_val(self, s, g)
    def _build_replay_buffer(self, buffer_size)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/ppo_agent.py

```
class PPOAgent(PGAgent)
    def __init__(self, world, id, json_data)
    def _load_params(self, json_data)
    def _build_nets(self, json_data)
    def _build_losses(self, json_data)
    def _build_solvers(self, json_data)
    def _decide_action(self, s, g)
    def _eval_actor(self, s, g, enable_exp)
    def _train_step(self)
    def _get_iters_per_update(self)
    def _valid_train_step(self)
    def _compute_batch_vals(self, start_idx, end_idx)
    def _compute_batch_new_vals(self, start_idx, end_idx, val_buffer)
    def _update_critic(self, s, g, tar_vals)
    def _update_actor(self, s, g, a, logp, adv)
    def update_actor_stepsize(self, clip_frac)
    def set_actor_stepsize(self, stepsize)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/replay_buffer.py

```
class ReplayBuffer(object)
    def __init__(self, buffer_size)
    def sample(self, n)
    def sample_filtered(self, n, key)
    def count_filtered(self, key)
    def get(self, key, idx)
    def get_all(self, key)
    def get_idx_filtered(self, key)
    def get_path_start(self, idx)
    def get_path_end(self, idx)
    def get_pathlen(self, idx)
    def is_valid_path(self, idx)
    def store(self, path)
    def clear(self)
    def get_next_idx(self, idx)
    def is_terminal_state(self, idx)
    def check_terminal_flag(self, idx, flag)
    def is_path_end(self, idx)
    def add_filter_key(self, key)
    def get_current_size(self)
    def _check_flags(self, key, flags)
    def _add_sample_buffers(self, idx)
    def _free_sample_buffers(self, idx)
    def _init_buffers(self, path)
    def _request_idx(self, n)
    def _free_idx(self, idx)
    def _store_path(self, path, idx)
class SampleBuffer(object)
    def __init__(self, size)
    def clear(self)
    def is_valid(self, idx)
    def get_size(self)
    def add(self, idx)
    def free(self, idx)
    def sample(self, n)
    def check_consistency(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/rl_agent.py

```
class RLAgent(ABC)
    def __init__(self, world, id, json_data)
    def __str__(self)
    def get_output_dir(self)
    def set_output_dir(self, out_dir)
    def get_int_output_dir(self)
    def set_int_output_dir(self, out_dir)
    def reset(self)
    def update(self, timestep)
    def end_episode(self)
    def has_goal(self)
    def predict_val(self)
    def get_enable_training(self)
    def set_enable_training(self, enable)
    def enable_testing(self)
    def get_name(self)
    def save_model(self, out_path)
    def load_model(self, in_path)
    def _decide_action(self, s, g)
    def _get_output_path(self)
    def _get_int_output_path(self)
    def _train_step(self)
    def _check_action_space(self)
    def get_action_space(self)
    def get_state_size(self)
    def get_goal_size(self)
    def get_action_size(self)
    def get_num_actions(self)
    def need_new_action(self)
    def _build_normalizers(self)
    def _build_bounds(self)
    def _load_params(self, json_data)
    def _record_state(self)
    def _record_goal(self)
    def _record_reward(self)
    def _apply_action(self, a)
    def _record_flags(self)
    def _is_first_step(self)
    def _end_path(self)
    def _update_new_action(self)
    def _update_exp_params(self)
    def _update_test_return(self, path)
    def _update_mode(self)
    def _update_mode_train(self)
    def _update_mode_train_end(self)
    def _update_mode_test(self)
    def _init_mode_train(self)
    def _init_mode_train_end(self)
    def _init_mode_test(self)
    def _enable_output(self)
    def _enable_int_output(self)
    def _calc_val_bounds(self, discount)
    def _calc_val_offset_scale(self, discount)
    def _calc_term_vals(self, discount)
    def _update_iter(self, iter)
    def _enable_draw(self)
    def _log_val(self, s, g)
    def _build_replay_buffer(self, buffer_size)
    def _store_path(self, path)
    def _record_normalizers(self, path)
    def _update_normalizers(self)
    def _train(self)
    def _get_iters_per_update(self)
    def _valid_train_step(self)
    def _log_exp_params(self)

```python
def _record_reward(self):
    r = self.world.env.calc_reward(self.id)
    return r
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/rl_util.py

```
def compute_return(rewards, gamma, td_lambda, val_t)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/rl_world.py

```
class RLWorld(object)
    def __init__(self, env, arg_parser)
    def get_enable_training(self)
    def set_enable_training(self, enable)
    def parse_args(self, arg_parser)
    def shutdown(self)
    def build_agents(self)
    def update(self, timestep)
    def reset(self)
    def end_episode(self)
    def _update_env(self, timestep)
    def _update_agents(self, timestep)
    def _reset_env(self)
    def _reset_agents(self)
    def _end_episode_agents(self)
    def _build_agent(self, id, agent_file)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/solvers/mpi_solver.py

```
class MPISolver(Solver)
    def __init__(self, sess, optimizer, vars)
    def get_stepsize(self)
    def update(self, grads, grad_scale)
    def update_flatgrad(self, flat_grad, grad_scale)
    def sync(self)
    def check_synced(self)
    def _is_root(self)
    def _build_grad_feed(self, vars)
    def _calc_grad_dim(self)
    def _load_flat_grad(self, flat_grad)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/solvers/solver.py

```
class Solver(ABC)
    def __init__(self, vars)
    def update(self, grads)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/tf_agent.py

```
class TFAgent(RLAgent)
    def __init__(self, world, id, json_data)
    def __del__(self)
    def save_model(self, out_path)
    def load_model(self, in_path)
    def _get_output_path(self)
    def _get_int_output_path(self)
    def _build_graph(self, json_data)
    def _init_normalizers(self)
    def _build_nets(self, json_data)
    def _build_losses(self, json_data)
    def _build_solvers(self, json_data)
    def _tf_vars(self, scope)
    def _build_normalizers(self)
    def _load_normalizers(self)
    def _update_normalizers(self)
    def _initialize_vars(self)
    def _build_saver(self)
    def _get_saver_vars(self)
    def _weight_decay_loss(self, scope)
    def _train(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/tf_normalizer.py

```
class TFNormalizer(Normalizer)
    def __init__(self, sess, scope, size, groups_ids, eps, clip)
    def load(self)
    def update(self)
    def set_mean_std(self, mean, std)
    def normalize_tf(self, x)
    def unnormalize_tf(self, norm_x)
    def _build_resource_tf(self)
    def _update_resource_tf(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/learning/tf_util.py

```
def disable_gpu()
def var_shape(x)
def intprod(x)
def numel(x)
def flat_grad(loss, var_list, grad_ys)
def fc_net(input, layers_sizes, activation, reuse, flatten)
def copy(sess, src, dst)
def flat_grad(loss, var_list)
def calc_logp_gaussian(x_tf, mean_tf, std_tf)
def calc_bound_loss(x_tf, bound_min, bound_max)
class SetFromFlat(object)
    def __init__(self, sess, var_list, dtype)
    def __call__(self, theta)
class GetFlat(object)
    def __init__(self, sess, var_list)
    def __call__(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/camera.py

```
def normalize_screen_coordinates(X, w, h)
def image_coordinates(X, w, h)
def world_to_camera(X, R, t)
def camera_to_world(X, R, t)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/deepmimic_json_generator.py

```
def init_fb_h36m_dataset(dataset_path)
def pose3D_from_fb_h36m(dataset, subject, action, shift)
def rot_seq_to_deepmimic_json(rot_seq, loop, json_path)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/h36m_dataset.py

```
class Human36mDataset(MocapDataset)
    def __init__(self, path, remove_static_joints)
    def supports_semi_supervised(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/humanoid.py

```
class HumanoidPose(object)
    def __init__(self)
    def Reset(self)
    def ComputeLinVel(self, posStart, posEnd, deltaTime)
    def ComputeAngVel(self, ornStart, ornEnd, deltaTime, bullet_client)
    def NormalizeQuaternion(self, orn)
    def PostProcessMotionData(self, frameData)
    def Slerp(self, frameFraction, frameData, frameDataNext, bullet_client)
class Humanoid(object)
    def __init__(self, pybullet_client, motion_data, baseShift)
    def Reset(self)
    def RenderReference(self, t)
    def CalcCycleCount(self, simTime, cycleTime)
    def SetSimTime(self, t)
    def Terminates(self)
    def BuildHeadingTrans(self, rootOrn)
    def GetPhase(self)
    def BuildOriginTrans(self)
    def InitializePoseFromMotionData(self)
    def ApplyAction(self, action)
    def ApplyPose(self, pose, initializeBase, initializeVelocities, humanoid, bc)
    def GetState(self)
    def GetReward(self)
    def GetBasePosition(self)

```python
def GetReward(self):
    #from DeepMimic double cSceneImitate::CalcRewardImitate
    pose_w = 0.5
    vel_w = 0.05
    end_eff_w = 0  #0.15
    root_w = 0  #0.2
    com_w = 0.1

    total_w = pose_w + vel_w + end_eff_w + root_w + com_w
    pose_w /= total_w
    vel_w /= total_w
    end_eff_w /= total_w
    root_w /= total_w
    com_w /= total_w

    pose_scale = 2
    vel_scale = 0.1
    end_eff_scale = 40
    root_scale = 5
    com_scale = 10
    err_scale = 1

    reward = 0

    pose_err = 0
    vel_err = 0
    end_eff_err = 0
    root_err = 0
    com_err = 0
    heading_err = 0

    #create a mimic reward, comparing the dynamics humanoid with a kinematic one

    pose = self.InitializePoseFromMotionData()
    #print("self._kinematicHumanoid=",self._kinematicHumanoid)
    #print("kinematicHumanoid #joints=",self.kin_client.getNumJoints(self._kinematicHumanoid))
    self.ApplyPose(pose, True, True, self._kinematicHumanoid, self.kin_client)

    #const Eigen::VectorXd& pose0 = sim_char.GetPose();
    #const Eigen::VectorXd& vel0 = sim_char.GetVel();
    #const Eigen::VectorXd& pose1 = kin_char.GetPose();
    #const Eigen::VectorXd& vel1 = kin_char.GetVel();
    #tMatrix origin_trans = sim_char.BuildOriginTrans();
    #tMatrix kin_origin_trans = kin_char.BuildOriginTrans();
    #
    #tVector com0_world = sim_char.CalcCOM();
    #tVector com_vel0_world = sim_char.CalcCOMVel();
    #tVector com1_world;
    #tVector com_vel1_world;
    #cRBDUtil::CalcCoM(joint_mat, body_defs, pose1, vel1, com1_world, com_vel1_world);
    #
    root_id = 0
    #tVector root_pos0 = cKinTree::GetRootPos(joint_mat, pose0);
    #tVector root_pos1 = cKinTree::GetRootPos(joint_mat, pose1);
    #tQuaternion root_rot0 = cKinTree::GetRootRot(joint_mat, pose0);
    #tQuaternion root_rot1 = cKinTree::GetRootRot(joint_mat, pose1);
    #tVector root_vel0 = cKinTree::GetRootVel(joint_mat, vel0);
    #tVector root_vel1 = cKinTree::GetRootVel(joint_mat, vel1);
    #tVector root_ang_vel0 = cKinTree::GetRootAngVel(joint_mat, vel0);
    #tVector root_ang_vel1 = cKinTree::GetRootAngVel(joint_mat, vel1);

    mJointWeights = [
        0.20833, 0.10416, 0.0625, 0.10416, 0.0625, 0.041666666666666671, 0.0625, 0.0416, 0.00,
        0.10416, 0.0625, 0.0416, 0.0625, 0.0416, 0.0000
    ]

    num_end_effs = 0
    num_joints = 15

    root_rot_w = mJointWeights[root_id]
    #pose_err += root_rot_w * cKinTree::CalcRootRotErr(joint_mat, pose0, pose1)
    #vel_err += root_rot_w * cKinTree::CalcRootAngVelErr(joint_mat, vel0, vel1)

    for j in range(num_joints):
      curr_pose_err = 0
      curr_vel_err = 0
      w = mJointWeights[j]

      simJointInfo = self._pybullet_client.getJointStateMultiDof(self._humanoid, j)

      #print("simJointInfo.pos=",simJointInfo[0])
      #print("simJointInfo.vel=",simJointInfo[1])
      kinJointInfo = self.kin_client.getJointStateMultiDof(self._kinematicHumanoid, j)
      #print("kinJointInfo.pos=",kinJointInfo[0])
      #print("kinJointInfo.vel=",kinJointInfo[1])
      if (len(simJointInfo[0]) == 1):
        angle = simJointInfo[0][0] - kinJointInfo[0][0]
        curr_pose_err = angle * angle
        velDiff = simJointInfo[1][0] - kinJointInfo[1][0]
        curr_vel_err = velDiff * velDiff
      if (len(simJointInfo[0]) == 4):
        #print("quaternion diff")
        diffQuat = self._pybullet_client.getDifferenceQuaternion(simJointInfo[0], kinJointInfo[0])
        axis, angle = self._pybullet_client.getAxisAngleFromQuaternion(diffQuat)
        curr_pose_err = angle * angle
        diffVel = [
            simJointInfo[1][0] - kinJointInfo[1][0], simJointInfo[1][1] - kinJointInfo[1][1],
            simJointInfo[1][2] - kinJointInfo[1][2]
        ]
        curr_vel_err = diffVel[0] * diffVel[0] + diffVel[1] * diffVel[1] + diffVel[2] * diffVel[2]

      pose_err += w * curr_pose_err
      vel_err += w * curr_vel_err

    #  bool is_end_eff = sim_char.IsEndEffector(j)
    #  if (is_end_eff)
    #  {
    #    tVector pos0 = sim_char.CalcJointPos
```
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/inverse_kinematics.py

```
def get_angle(vec1, vec2)
def get_quaternion(ox, oy, oz, x, y, z)
def coord_to_rot(frameNum, frame, frame_duration)
def coord_seq_to_rot_seq(coord_seq, frame_duration)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/mocap_dataset.py

```
class MocapDataset()
    def __init__(self, fps, skeleton)
    def remove_joints(self, joints_to_remove)
    def __getitem__(self, key)
    def subjects(self)
    def fps(self)
    def skeleton(self)
    def cameras(self)
    def supports_semi_supervised(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/quaternion.py

```
def qrot(q, v)
def qinverse(q, inplace)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/render_reference.py

```
def draw_ground_truth(coord_seq, frame, duration, shift)
def Reset(humanoid)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/skeleton.py

```
class Skeleton()
    def __init__(self, parents, joints_left, joints_right)
    def num_joints(self)
    def parents(self)
    def has_children(self)
    def children(self)
    def remove_joints(self, joints_to_remove)
    def joints_left(self)
    def joints_right(self)
    def _compute_metadata(self)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mocap/transformation.py

```
def identity_matrix()
def translation_matrix(direction)
def translation_from_matrix(matrix)
def reflection_matrix(point, normal)
def reflection_from_matrix(matrix)
def rotation_matrix(angle, direction, point)
def rotation_from_matrix(matrix)
def scale_matrix(factor, origin, direction)
def scale_from_matrix(matrix)
def projection_matrix(point, normal, direction, perspective, pseudo)
def projection_from_matrix(matrix, pseudo)
def clip_matrix(left, right, bottom, top, near, far, perspective)
def shear_matrix(angle, direction, point, normal)
def shear_from_matrix(matrix)
def decompose_matrix(matrix)
def compose_matrix(scale, shear, angles, translate, perspective)
def orthogonalization_matrix(lengths, angles)
def affine_matrix_from_points(v0, v1, shear, scale, usesvd)
def superimposition_matrix(v0, v1, scale, usesvd)
def euler_matrix(ai, aj, ak, axes)
def euler_from_matrix(matrix, axes)
def euler_from_quaternion(quaternion, axes)
def quaternion_from_euler(ai, aj, ak, axes)
def quaternion_about_axis(angle, axis)
def quaternion_matrix(quaternion)
def quaternion_from_matrix(matrix, isprecise)
def quaternion_multiply(quaternion1, quaternion0)
def quaternion_conjugate(quaternion)
def quaternion_inverse(quaternion)
def quaternion_real(quaternion)
def quaternion_imag(quaternion)
def quaternion_slerp(quat0, quat1, fraction, spin, shortestpath)
def random_quaternion(rand)
def random_rotation_matrix(rand)
def vector_norm(data, axis, out)
def unit_vector(data, axis, out)
def random_vector(size)
def vector_product(v0, v1, axis)
def angle_between_vectors(v0, v1, directed, axis)
def inverse_matrix(matrix)
def concatenate_matrices()
def is_same_transform(matrix0, matrix1)
def is_same_quaternion(q0, q1)
def _import_module(name, package, warn, postfix, ignore)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mpi_run.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/mpi_run_multiclip.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/testrl.py

```
def update_world(world, time_elapsed)
def build_arg_parser(args)
def build_world(args, enable_draw)
```

### examples/pybullet/gym/pybullet_envs/deep_mimic/testrl_multiclip.py

```
def update_world(world, time_elapsed)
def build_arg_parser(args)
def build_world(args, enable_draw)
```

### examples/pybullet/gym/pybullet_envs/env_bases.py

```
class MJCFBaseBulletEnv(Env)
    """Base class for Bullet physics simulation loading MJCF (MuJoCo .xml) environments in a Scene.
These environments create single-player scenes and behave like normal Gym environments, if
you don't use multiplayer."""
    def __init__(self, robot, render)
    def configure(self, args)
    def seed(self, seed)
    def reset(self)
    def camera_adjust(self)
    def render(self, mode, close)
    def close(self)
    def HUD(self, state, a, done)
class Camera()
    def __init__(self, env)
    def move_and_look_at(self, i, j, k, x, y, z)
```

### examples/pybullet/gym/pybullet_envs/examples/batchsim3.py

```
def ExploreWorker(rank, num_processes, childPipe, args)
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_AntBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_HalfCheetahBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_HopperBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_InvertedDoublePendulumBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_InvertedPendulumBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_InvertedPendulumSwingupBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/enjoy_TF_Walker2DBulletEnv_v0_2017may.py

```
def relu(x)
class SmallReactivePolicy()
    """Simple multi-layer perceptron policy, no internal state"""
    def __init__(self, observation_space, action_space)
    def act(self, ob)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/kukaCamGymEnvTest.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/kukaGymEnvTest.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/kukaGymEnvTest2.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/minitaur_gym_env_example.py

```
"""An example to run of the minitaur gym environment with sine gaits."""
def ResetPoseExample()
def MotorOverheatExample()
def SineStandExample()
def SinePolicyExample()
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/panda_sim.py

```
class PandaSim(object)
    def __init__(self, bullet_client, offset)
    def reset(self)
    def step(self)
```

### examples/pybullet/gym/pybullet_envs/examples/racecarGymEnvTest.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/racecarZEDGymEnvTest.py

```
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/testEnv.py

```
def test(args)
def main()
```

### examples/pybullet/gym/pybullet_envs/examples/testMJCF.py

```
def test(args)
```

### examples/pybullet/gym/pybullet_envs/gym_locomotion_envs.py

```
class WalkerBaseBulletEnv(MJCFBaseBulletEnv)
    def __init__(self, robot, render)
    def create_single_player_scene(self, bullet_client)
    def reset(self)
    def _isDone(self)
    def move_robot(self, init_x, init_y, init_z)
    def step(self, a)
    def camera_adjust(self)
class HopperBulletEnv(WalkerBaseBulletEnv)
    def __init__(self, render)
class Walker2DBulletEnv(WalkerBaseBulletEnv)
    def __init__(self, render)
class HalfCheetahBulletEnv(WalkerBaseBulletEnv)
    def __init__(self, render)
    def _isDone(self)
class AntBulletEnv(WalkerBaseBulletEnv)
    def __init__(self, render)
class HumanoidBulletEnv(WalkerBaseBulletEnv)
    def __init__(self, robot, render)
class HumanoidFlagrunBulletEnv(HumanoidBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
class HumanoidFlagrunHarderBulletEnv(HumanoidBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
```

### examples/pybullet/gym/pybullet_envs/gym_manipulator_envs.py

```
class ReacherBulletEnv(MJCFBaseBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
    def step(self, a)
    def camera_adjust(self)
class PusherBulletEnv(MJCFBaseBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
    def step(self, a)
    def calc_potential(self)
    def camera_adjust(self)
class StrikerBulletEnv(MJCFBaseBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
    def step(self, a)
    def calc_potential(self)
    def camera_adjust(self)
class ThrowerBulletEnv(MJCFBaseBulletEnv)
    def __init__(self, render)
    def create_single_player_scene(self, bullet_client)
    def step(self, a)
    def camera_adjust(self)
```

### examples/pybullet/gym/pybullet_envs/gym_pendulum_envs.py

```
class InvertedPendulumBulletEnv(MJCFBaseBulletEnv)
    def __init__(self)
    def create_single_player_scene(self, bullet_client)
    def reset(self)
    def step(self, a)
    def camera_adjust(self)
class InvertedPendulumSwingupBulletEnv(InvertedPendulumBulletEnv)
    def __init__(self)
class InvertedDoublePendulumBulletEnv(MJCFBaseBulletEnv)
    def __init__(self)
    def create_single_player_scene(self, bullet_client)
    def reset(self)
    def step(self, a)
    def camera_adjust(self)
```

### examples/pybullet/gym/pybullet_envs/kerasrl_utils.py

```
def get_fields(weight_save_name)
def get_latest_save(file_folder, agent_name, env_name, version_number)
```

### examples/pybullet/gym/pybullet_envs/minitaur/actuatornet/actuatornet_keras.py

```
def main(unused_argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/actuatornet/actuatornet_keras_lstm.py

```
"""see https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/"""
def series_to_supervised(data, n_in, n_out, dropnan)
```

### examples/pybullet/gym/pybullet_envs/minitaur/actuatornet/minitaur_raibert_controller_example.py

```
def speed(t)
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/actuatornet/proto2csv.py

```
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/com_height_estimator.py

```
"""State estimator for robot height."""
class COMHeightEstimator(StateEstimatorBase)
    """Estimate the CoM height using base orientation and local toe positions."""
    def __init__(self, robot, com_estimate_leg_indices, initial_com_height)
    def estimated_com_height(self)
    def reset(self, current_time)
    def update(self, current_time)
    def com_estimate_leg_indices(self)
    def com_estimate_leg_indices(self, leg_indices)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/com_velocity_estimator.py

```
"""State estimator."""
class COMVelocityEstimator(StateEstimatorBase)
    """Estimate the CoM velocity using on board sensors.


Requires knowledge about the base velocity in world frame, which for example
can be obtained from a MoCap system. This estimator will filter out the high
frequency noises in the velocity so the results can be used with controllers
reliably."""
    def __init__(self, robot, window_size)
    def com_velocity_body_yaw_aligned_frame(self)
    def com_velocity_world_frame(self)
    def reset(self, current_time)
    def update(self, current_time)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/dummy_gait_generator.py

```
"""A dummy gait generator module for storing gait patterns from higher-level controller."""
class DummyGaitGenerator(GaitGenerator)
    """A module for storing quadruped gait patterns from high-level controller.

This module stores the state for each leg of a quadruped robot. The data is
used by the stance leg controller to determine the appropriate contact forces.
A high-level controller, such as a neural network policy, can be used t"""
    def __init__(self, robot, initial_leg_state)
    def reset(self, current_time)
    def desired_leg_state(self)
    def desired_leg_state(self, state)
    def leg_state(self)
    def leg_state(self, state)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/foot_stepper.py

```
"""A state machine that steps each foot for a static gait. Experimental code."""
class StepInput(object)
    def __init__(self)
class StepOutput(object)
    def __init__(self, new_toe_pos_world)
class FootStepper(object)
    """This class computes desired foot placement for a quadruped robot."""
    def __init__(self, bullet_client, toe_ids, toe_pos_local_ref)
    def next_foot(self)
    def swing_foot(self)
    def get_reference_pos_swing_foot(self)
    def set_reference_pos_swing_foot(self, new_pos_local)
    def is_com_stable(self)
    def update(self, step_input)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/gait_generator.py

```
"""Gait pattern planning module."""
class LegState(Enum)
    """The state of a leg during locomotion."""
class GaitGenerator(object)
    """Generates the leg swing/stance pattern for the robot."""
    def reset(self, current_time)
    def update(self, current_time)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/imu_based_com_velocity_estimator.py

```
"""State estimator."""
class IMUBasedCOMVelocityEstimator(StateEstimatorBase)
    """Estimate the CoM velocity using IMU sensors and velocities of stance feet.


Estimates the com velocity of the robot using IMU data and stance feet
velocities fused by a Kalman Filter. Kalman Filter assumes the true state x
follows a linear dynamics: x'=Fx+Bu+w, where x' and x denots the
current and"""
    def __init__(self, robot, use_sensor_interface, accelerometer_variance, observation_variance, initial_variance, velocity_filter_window, gyroscope_filter_window, contact_detection_threshold, velocity_clipping)
    def com_velocity_body_yaw_aligned_frame(self)
    def reset(self, current_time)
    def update(self, current_time)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/leg_controller.py

```
"""The leg controller class interface."""
class LegController(object)
    """Generates the leg control signal."""
    def reset(self, current_time)
    def update(self, current_time)
    def get_action(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/locomotion_controller.py

```
"""A model based controller framework."""
class LocomotionController(object)
    """Generates the quadruped locomotion.

The actual effect of this controller depends on the composition of each
individual subcomponent."""
    def __init__(self, robot, gait_generator, state_estimator, swing_leg_controller, stance_leg_controller, clock)
    def swing_leg_controller(self)
    def stance_leg_controller(self)
    def gait_generator(self)
    def state_estimator(self)
    def reset(self)
    def update(self)
    def get_action(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/locomotion_controller_example.py

```
"""Laikago walking example using the locomotion controller framework."""
def _load_config(render, run_on_robot)
def _generate_example_linear_angular_speed(t)
def _update_speed_from_kb(kb, lin_speed, ang_speed)
def _update_controller_params(controller, lin_speed, ang_speed)
def _run_example(max_time, run_on_robot, use_keyboard)
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/locomotion_controller_in_scenario_set_example.py

```
"""ScenarioSet example for Laikago MPC controller.

blaze run -c opt \
//robotics/reinforcement_learning/minitaur/agents/baseline_controller\
:locomotion_controller_in_scenario_set_example -- --gait=slow_trot \
--add_random_push=True"""
def _start_stop_profile(max_speed, axis, duration)
def _random_speed_profile(max_speed, axis, time_interval)
def _body_height_profile(z_range)
def _generate_linear_angular_speed(t, time_points, speed_points)
def _update_controller_params(controller, lin_speed, ang_speed)
def _gen_stability_test_start_stop()
def _gen_stability_test_random()
def _test_stability(max_time, render, test_generator)
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/locomotion_controller_setup.py

```
"""The common setups for MPC based locoomtion controller environments."""
def load_sim_config(render)
def add_random_push_config()
def select_gait(gait_type)
def setup_controller(robot, gait, run_on_robot, use_ground_truth_velocity)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/minitaur_raibert_controller.py

```
"""A Raibert style controller for Minitaur."""
class BehaviorParameters(object)
    """Highlevel parameters for Raibert style controller."""
def generate_default_swing_trajectory(phase, init_pose, end_pose)
def generate_default_stance_trajectory(phase, init_pose, end_pose, use_constant_extension)
def get_stance_foot_offset_for_turning(leg_id, steering_signal)
def get_leg_swing_offset_for_pitching(body_pitch, desired_incline_angle)
class RaibertSwingLegController(object)
    """The swing leg controller."""
    def __init__(self, speed_gain, foot_clearance, leg_trajectory_generator)
    def get_action(self, raibert_controller)
class RaibertStanceLegController(object)
    """The controller that modulates the behavior of the stance legs."""
    def __init__(self, speed_gain, leg_trajectory_generator)
    def get_action(self, raibert_controller)
class MinitaurRaibertController(object)
    """A Raibert style controller for trotting gait."""
    def __init__(self, robot, behavior_parameters, swing_leg_controller, stance_leg_controller, pose_feedback_controller)
    def robot(self)
    def swing_set(self)
    def stance_set(self)
    def swing_start_leg_pose(self)
    def stance_start_leg_pose(self)
    def _get_average_leg_pose(self, leg_indices)
    def get_swing_leg_pose(self)
    def get_stance_leg_pose(self)
    def get_phase(self)
    def _get_new_swing_stance_set(self)
    def update(self, t)
    def estimate_base_velocity(self)
    def get_swing_leg_action(self)
    def get_stance_leg_action(self)
    def get_action(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/minitaur_raibert_controller_utils.py

```
"""Utility functions for the Minitaur Raibert controller."""
def leg_pose_to_foot_position(leg_pose)
def foot_position_to_leg_pose(foot_position)
def extension_to_ankle_dist(extension)
def ankle_dist_to_extension(dist)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/model_predictive_control.py

```
"""Classic model predictive control methods."""
def compute_contact_force_projection_matrix(foot_positions_in_com_frame, stance_foot_ids)
def plan_foot_contact_force(mass, inertia, com_position, com_velocity, com_roll_pitch_yaw, com_angular_velocity, foot_positions_in_com_frame, foot_contact_state, desired_com_position, desired_com_velocity, desired_com_roll_pitch_yaw, desired_com_angular_velocity)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/multi_state_estimator.py

```
"""A class for combining multiple state estimators."""
class MultiStateEstimator(StateEstimatorBase)
    """Combine multiple state estimators.


This class can be used to combine multiple state estimators into one. For
example, one can use the COMVelocityEstimator to estimate the com velocity
and COMHeightEstimator to estimate the com height."""
    def __init__(self, robot, state_estimators)
    def reset(self, current_time)
    def update(self, current_time)
    def __getattr__(self, attr)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/openloop_gait_generator.py

```
"""Gait pattern planning module."""
class OpenloopGaitGenerator(GaitGenerator)
    """Generates openloop gaits for quadruped robots.

A flexible open-loop gait generator. Each leg has its own cycle and duty
factor. And the state of each leg alternates between stance and swing. One can
easily formuate a set of common quadruped gaits like trotting, pacing,
pronking, bounding, etc by tw"""
    def __init__(self, robot, stance_duration, duty_factor, initial_leg_phase, contact_detection_force_threshold, contact_detection_phase_threshold)
    def reset(self, current_time)
    def desired_leg_state(self)
    def leg_state(self)
    def swing_duration(self)
    def stance_duration(self)
    def normalized_phase(self)
    def update(self, current_time)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/raibert_swing_leg_controller.py

```
"""The swing leg controller class."""
def _gen_parabola(phase, start, mid, end)
def _gen_swing_foot_trajectory(input_phase, start_pos, end_pos, ease_up_phase, ease_up_percent)
class RaibertSwingLegController(LegController)
    """Controls the swing leg position using Raibert's formula.

For details, please refer to chapter 2 in "Legged robbots that balance" by
Marc Raibert. The key idea is to stablize the swing foot's location based on
the CoM moving speed."""
    def __init__(self, robot, gait_generator, state_estimator, desired_speed, desired_twisting_speed, desired_height, foot_clearance, local_hip_positions, ease_up_phase, ease_up_percent, feed_forward_torques)
    def reset(self, current_time)
    def update(self, current_time)
    def get_action(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/state_estimator.py

```
"""State estimator."""
class StateEstimatorBase(object)
    """Estimates the unmeasurable state of the robot."""
    def reset(self, current_time)
    def update(self, current_time)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/static_gait_controller.py

```
"""A static gait controller for a quadruped robot. Experimental code."""
class StaticGaitController(object)
    """A static gait controller for a quadruped robot."""
    def __init__(self, robot)
    def act(self, observation)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/time_based_moving_window_filter.py

```
"""A moving-window filter for smoothing the signals within certain time interval."""
class TimeBasedMovingWindowFilter()
    """A moving-window filter for smoothing the signals within certain time interval."""
    def __init__(self, filter_window)
    def reset(self)
    def calculate_average(self, new_value, timestamp)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/baseline_controller/torque_stance_leg_controller.py

```
"""A torque based stance controller framework."""
class TorqueStanceLegController(LegController)
    """A torque based stance leg controller framework.

Takes in high level parameters like walking speed and turning speed, and
generates necessary the torques for stance legs."""
    def __init__(self, robot, gait_generator, state_estimator, desired_speed, desired_twisting_speed, desired_roll_pitch, desired_body_height, body_mass, body_inertia, num_legs, friction_coeffs, qp_weights, planning_horizon, planning_timestep)
    def reset(self, current_time)
    def update(self, current_time)
    def get_action(self)
    def qp_solver_fail(self)
    def desired_speed(self)
    def desired_speed(self, speed)
    def desired_twisting_speed(self)
    def desired_twisting_speed(self, twisting_speed)
    def desired_roll_pitch(self)
    def desired_roll_pitch(self, roll_pitch)
    def desired_body_height(self)
    def desired_body_height(self, body_height)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/ppo/__init__.py

```
"""Proximal Policy Optimization algorithm."""
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/ppo/algorithm.py

```
"""Proximal Policy Optimization algorithm.

Based on John Schulman's implementation in Python and Theano:
https://github.com/joschu/modular_rl/blob/master/modular_rl/ppo.py"""
class PPOAlgorithm(object)
    """A vectorized implementation of the PPO algorithm by John Schulman."""
    def __init__(self, batch_env, step, is_training, should_log, config)
    def begin_episode(self, agent_indices)
    def perform(self, observ)
    def experience(self, observ, action, reward, unused_done, unused_nextob)
    def _define_experience(self, observ, action, reward)
    def end_episode(self, agent_indices)
    def _define_end_episode(self, agent_indices)
    def _training(self)
    def _update_value(self, observ, reward, length)
    def _update_value_step(self, observ, reward, length)
    def _value_loss(self, observ, reward, length)
    def _update_policy(self, observ, action, old_mean, old_logstd, reward, length)
    def _update_policy_step(self, observ, action, old_mean, old_logstd, advantage, length)
    def _policy_loss(self, mean, logstd, old_mean, old_logstd, action, advantage, length)
    def _adjust_penalty(self, observ, old_mean, old_logstd, length)
    def _mask(self, tensor, length)
    def _network(self, observ, length, state, reuse)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/ppo/memory.py

```
"""Memory that stores episodes."""
class EpisodeMemory(object)
    """Memory that stores episodes."""
    def __init__(self, template, capacity, max_length, scope)
    def length(self, rows)
    def append(self, transitions, rows)
    def replace(self, episodes, length, rows)
    def data(self, rows)
    def clear(self, rows)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/ppo/normalize.py

```
"""Normalize tensors based on streaming estimates of mean and variance."""
class StreamingNormalize(object)
    """Normalize tensors based on streaming estimates of mean and variance."""
    def __init__(self, template, center, scale, clip, name)
    def transform(self, value)
    def update(self, value)
    def reset(self)
    def summary(self)
    def _std(self)
    def _summary(self, name, tensor)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/ppo/utility.py

```
"""Utilities for the PPO algorithm."""
def create_nested_vars(tensors)
def reinit_nested_vars(variables, indices)
def assign_nested_vars(variables, tensors)
def discounted_return(reward, length, discount)
def fixed_step_return(reward, value, length, discount, window)
def lambda_return(reward, value, length, discount, lambda_)
def lambda_advantage(reward, value, length, discount)
def diag_normal_kl(mean0, logstd0, mean1, logstd1)
def diag_normal_logpdf(mean, logstd, loc)
def diag_normal_entropy(mean, logstd)
def available_gpus()
def gradient_summaries(grad_vars, groups, scope)
def variable_summaries(vars_, groups, scope)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/__init__.py

```
"""Executable scripts for reinforcement learning."""
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/configs.py

```
"""Example configurations using the PPO algorithm."""
def default()
def pendulum()
def cheetah()
def walker()
def reacher()
def hopper()
def ant()
def humanoid()
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/networks.py

```
"""Networks for the PPO algorithm defined as recurrent cells."""
class LinearGaussianPolicy(RNNCell)
    """Indepent linear network with a tanh at the end for policy and feedforward network for the value.

The policy network outputs the mean action and the log standard deviation
is learned as indepent parameter vector."""
    def __init__(self, policy_layers, value_layers, action_size, mean_weights_initializer, logstd_initializer)
    def state_size(self)
    def output_size(self)
    def __call__(self, observation, state)
class ForwardGaussianPolicy(RNNCell)
    """Independent feed forward networks for policy and value.

The policy network outputs the mean action and the log standard deviation
is learned as independent parameter vector."""
    def __init__(self, policy_layers, value_layers, action_size, mean_weights_initializer, logstd_initializer)
    def state_size(self)
    def output_size(self)
    def __call__(self, observation, state)
class RecurrentGaussianPolicy(RNNCell)
    """Independent recurrent policy and feed forward value networks.

The policy network outputs the mean action and the log standard deviation
is learned as independent parameter vector. The last policy layer is recurrent
and uses a GRU cell."""
    def __init__(self, policy_layers, value_layers, action_size, mean_weights_initializer, logstd_initializer)
    def state_size(self)
    def output_size(self)
    def __call__(self, observation, state)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/train.py

```
"""Script to train a batch reinforcement learning algorithm.

Command line:

  python3 -m agents.scripts.train --logdir=/path/to/logdir --config=pendulum"""
def _create_environment(config)
def _define_loop(graph, logdir, train_steps, eval_steps)
def train(config, env_processes)
def main(_)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/train_ppo_test.py

```
"""Tests for the PPO algorithm usage example."""
class PPOTest(TestCase)
    def test_no_crash_cheetah(self)
    def test_no_crash_ant(self)
    def test_no_crash_observation_shape(self)
    def test_no_crash_variable_duration(self)
    def _define_config(self)

```python
def test_no_crash_observation_shape(self):
    nets = networks.ForwardGaussianPolicy, networks.RecurrentGaussianPolicy
    observ_shapes = (1,), (2, 3), (2, 3, 4)
    for network, observ_shape in itertools.product(nets, observ_shapes):
      config = self._define_config()
      with config.unlocked:
        config.env = functools.partial(tools.MockEnvironment,
                                       observ_shape,
                                       action_shape=(3,),
                                       min_duration=15,
                                       max_duration=15)
        config.max_length = 20
        config.steps = 100
        config.network = network
      for score in train.train(config, env_processes=False):
        float(score)
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/utility.py

```
"""Utilities for using reinforcement learning algorithms."""
def define_simulation_graph(batch_env, algo_cls, config)
def define_batch_env(constructor, num_agents, env_processes)
def define_saver(exclude)
def define_network(constructor, config, action_size)
def initialize_variables(sess, saver, logdir, checkpoint, resume)
def save_config(config, logdir)
def load_config(logdir)
def set_up_logging()
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/scripts/visualize.py

```
"""Script to render videos of the Proximal Policy Gradient algorithm.

Command line:

  python3 -m agents.scripts.visualize \
      --logdir=/path/to/logdir/<time>-<config> --outdir=/path/to/outdir/"""
def _create_environment(config, outdir)
def _define_loop(graph, eval_steps)
def visualize(logdir, outdir, num_agents, num_episodes, checkpoint, env_processes)
def main(_)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/__init__.py

```
"""Tools for reinforcement learning."""
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/attr_dict.py

```
"""Wrap a dictionary to access keys as attributes."""
class AttrDict(dict)
    """Wrap a dictionary to access keys as attributes."""
    def __init__(self)
    def __getattr__(self, key)
    def __setattr__(self, key, value)
    def unlocked(self)
    def copy(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/attr_dict_test.py

```
"""Tests for the attribute dictionary."""
class AttrDictTest(TestCase)
    def test_construct_from_dict(self)
    def test_construct_from_kwargs(self)
    def test_has_attribute(self)
    def test_access_default(self)
    def test_access_magic(self)
    def test_immutable_create(self)
    def test_immutable_modify(self)
    def test_immutable_unlocked(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/batch_env.py

```
"""Combine multiple environments to step them in batch."""
class BatchEnv(object)
    """Combine multiple environments to step them in batch."""
    def __init__(self, envs, blocking)
    def __len__(self)
    def __getitem__(self, index)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self, indices)
    def close(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/count_weights.py

```
"""Count learnable parameters."""
def count_weights(scope, exclude, graph)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/count_weights_test.py

```
"""Tests for the weight counting utility."""
class CountWeightsTest(TestCase)
    def test_count_trainable(self)
    def test_ignore_non_trainable(self)
    def test_trainable_and_non_trainable(self)
    def test_include_scopes(self)
    def test_restrict_scope(self)
    def test_restrict_nested_scope(self)
    def test_restrict_invalid_scope(self)
    def test_exclude_by_regex(self)
    def test_non_default_graph(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/in_graph_batch_env.py

```
"""Batch of environments inside the TensorFlow graph."""
class InGraphBatchEnv(object)
    """Batch of environments inside the TensorFlow graph.

The batch of environments will be stepped and reset inside of the graph using
a tf.py_func(). The current batch of observations, actions, rewards, and done
flags are held in according variables."""
    def __init__(self, batch_env)
    def __getattr__(self, name)
    def __len__(self)
    def __getitem__(self, index)
    def simulate(self, action)
    def reset(self, indices)
    def observ(self)
    def action(self)
    def reward(self)
    def done(self)
    def close(self)
    def _parse_shape(self, space)
    def _parse_dtype(self, space)

```python
def reward(self):
    """Access the variable holding the current reward."""
    return self._reward
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/in_graph_env.py

```
"""Put an OpenAI Gym environment into the TensorFlow graph."""
class InGraphEnv(object)
    """Put an OpenAI Gym environment into the TensorFlow graph.

The environment will be stepped and reset inside of the graph using
tf.py_func(). The current observation, action, reward, and done flag are held
in according variables."""
    def __init__(self, env)
    def __getattr__(self, name)
    def simulate(self, action)
    def reset(self)
    def observ(self)
    def action(self)
    def reward(self)
    def done(self)
    def step(self)
    def _parse_shape(self, space)
    def _parse_dtype(self, space)

```python
def reward(self):
    """Access the variable holding the current reward."""
    return self._reward
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/loop.py

```
"""Execute operations in a loop and coordinate logging and checkpoints."""
class Loop(object)
    """Execute operations in a loop and coordinate logging and checkpoints.

Supports multiple phases, that define their own operations to run, and
intervals for reporting scores, logging summaries, and storing checkpoints.
All class state is stored in-graph to properly recover from checkpoints."""
    def __init__(self, logdir, step, log, report, reset)
    def add_phase(self, name, done, score, summary, steps, report_every, log_every, checkpoint_every, feed)
    def run(self, sess, saver, max_step)
    def _is_every_steps(self, phase_step, batch, every)
    def _find_current_phase(self, global_step)
    def _define_step(self, done, score, summary)
    def _store_checkpoint(self, sess, saver, global_step)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/loop_test.py

```
"""Tests for the training loop."""
class LoopTest(TestCase)
    def test_report_every_step(self)
    def test_phases_feed(self)
    def test_average_score_over_phases(self)
    def test_not_done(self)
    def test_not_done_batch(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/mock_algorithm.py

```
"""Mock algorithm for testing reinforcement learning code."""
class MockAlgorithm(object)
    """Produce random actions and empty summaries."""
    def __init__(self, envs)
    def begin_episode(self, unused_agent_indices)
    def perform(self, unused_observ)
    def experience(self)
    def end_episode(self, unused_agent_indices)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/mock_environment.py

```
"""Mock environment for testing reinforcement learning code."""
class MockEnvironment(object)
    """Generate random agent input and keep track of statistics."""
    def __init__(self, observ_shape, action_shape, min_duration, max_duration)
    def observation_space(self)
    def action_space(self)
    def unwrapped(self)
    def step(self, action)
    def reset(self)
    def _current_observation(self)
    def _current_reward(self)

```python
def observation_space(self):
    low = np.zeros(self._observ_shape)
    high = np.ones(self._observ_shape)
    return gym.spaces.Box(low, high)
```

```python
def _current_observation(self):
    return self._random.uniform(0, 1, self._observ_shape)
```

```python
def _current_reward(self):
    return self._random.uniform(-1, 1)
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/simulate.py

```
"""In-graph simulation step of a vecrotized algorithm with environments."""
def simulate(batch_env, algo, log, reset)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/simulate_test.py

```
"""Tests for the simulation operation."""
class SimulateTest(TestCase)
    def test_done_automatic(self)
    def test_done_forced(self)
    def test_reset_automatic(self)
    def test_reset_forced(self)
    def _create_test_batch_env(self, durations)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/streaming_mean.py

```
"""Compute a streaming estimation of the mean of submitted tensors."""
class StreamingMean(object)
    """Compute a streaming estimation of the mean of submitted tensors."""
    def __init__(self, shape, dtype)
    def value(self)
    def count(self)
    def submit(self, value)
    def clear(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/wrappers.py

```
"""Wrappers for OpenAI Gym environments."""
class AutoReset(object)
    """Automatically reset environment when the episode is done."""
    def __init__(self, env)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
class ActionRepeat(object)
    """Repeat the agent action multiple steps."""
    def __init__(self, env, amount)
    def __getattr__(self, name)
    def step(self, action)
class RandomStart(object)
    """Perform random number of random actions at the start of the episode."""
    def __init__(self, env, max_steps)
    def __getattr__(self, name)
    def reset(self)
class FrameHistory(object)
    """Augment the observation with past observations."""
    def __init__(self, env, past_indices, flatten)
    def __getattr__(self, name)
    def observation_space(self)
    def step(self, action)
    def reset(self)
    def _select_frames(self)
class FrameDelta(object)
    """Convert the observation to a difference from the previous observation."""
    def __init__(self, env)
    def __getattr__(self, name)
    def observation_space(self)
    def step(self, action)
    def reset(self)
class RangeNormalize(object)
    """Normalize the specialized observation and action ranges to [-1, 1]."""
    def __init__(self, env, observ, action)
    def __getattr__(self, name)
    def observation_space(self)
    def action_space(self)
    def step(self, action)
    def reset(self)
    def _denormalize_action(self, action)
    def _normalize_observ(self, observ)
    def _is_finite(self, space)
class ClipAction(object)
    """Clip out of range actions to the action space of the environment."""
    def __init__(self, env)
    def __getattr__(self, name)
    def action_space(self)
    def step(self, action)
class LimitDuration(object)
    """End episodes after specified number of steps."""
    def __init__(self, env, duration)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
class ExternalProcess(object)
    """Step environment in a separate process for lock free paralellism."""
    def __init__(self, constructor)
    def observation_space(self)
    def action_space(self)
    def __getattr__(self, name)
    def step(self, action, blocking)
    def reset(self, blocking)
    def close(self)
    def _receive(self, expected_message)
    def _worker(self, constructor, conn)
class ConvertTo32Bit(object)
    """Convert data types of an OpenAI Gym environment to 32 bit."""
    def __init__(self, env)
    def __getattr__(self, name)
    def step(self, action)
    def reset(self)
    def _convert_observ(self, observ)
    def _convert_reward(self, reward)

```python
def observation_space(self):
    low = self._env.observation_space.low
    high = self._env.observation_space.high
    low = np.repeat(low[None, ...], len(self._past_indices), 0)
    high = np.repeat(high[None, ...], len(self._past_indices), 0)
    if self._flatten:
      low = np.reshape(low, (-1,) + low.shape[2:])
      high = np.reshape(high, (-1,) + high.shape[2:])
    return gym.spaces.Box(low, high)
```

```python
def observation_space(self):
    low = self._env.observation_space.low
    high = self._env.observation_space.high
    low, high = low - high, high - low
    return gym.spaces.Box(low, high)
```

```python
def observation_space(self):
    space = self._env.observation_space
    if not self._should_normalize_observ:
      return space
    return gym.spaces.Box(-np.ones(space.shape), np.ones(space.shape))
```

```python
def observation_space(self):
    if not self._observ_space:
      self._observ_space = self.__getattr__('observation_space')
    return self._observ_space
```

```python
def _convert_reward(self, reward):
    """Convert the reward to 32 bits.

    Args:
      reward: Numpy reward.

    Raises:
      ValueError: Rewards contain infinite values.

    Returns:
      Numpy reward with 32-bit data type.
    """
    if not np.isfinite(reward).all():
      raise ValueError('Infinite reward encountered.')
    return np.array(reward, dtype=np.float32)
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/tools/wrappers_test.py

```
"""Tests for environment wrappers."""
class ExternalProcessTest(TestCase)
    def test_close_no_hang_after_init(self)
    def test_close_no_hang_after_step(self)
    def test_reraise_exception_in_init(self)
    def test_reraise_exception_in_step(self)
class MockEnvironmentCrashInInit(object)
    """Raise an error when instantiated."""
    def __init__(self)
class MockEnvironmentCrashInStep(MockEnvironment)
    """Raise an error after specified number of steps in an episode."""
    def __init__(self, crash_at_step)
    def step(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/trajectory_generator/controller_simple.py

```
"""Asymmetric sine controller for quadruped locomotion.

Asymmetric sine uses cosine and sine waves to generate swinging and extension
for leg motion. It's asymmetric because sine waves are split into two phases
(swing forward and stance) and these phases have different frequencies according
to what proportion of a period will be spend on swinging forward forward
swinging backwards. In addition, the sine wave for extension has different
amplitudes during these two phases."""
class SimpleLegController(object)
    """Controller that gives swing and extension based on phase and parameters.


The controller returns the swing-extend pair based on a parameterized
ellipsoid trajectory that depends on center of motion, amplitude and phase.
The parameters are
  amplitude_extension: Amplitude for extension during stance"""
    def __init__(self, init_phase)
    def reset(self)
    def get_swing_extend(self)
    def adjust_center_extension(self, target_center_extension)
    def adjust_intensity(self, target_intensity)
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/trajectory_generator/tg_inplace.py

```
"""Trajectory Generator for in-place stepping motion for quadruped robot."""
def _get_actions_asymmetric_sine(phase, tg_params)
def step(current_phases, leg_frequencies, dt, tg_params)
def reset()
```

### examples/pybullet/gym/pybullet_envs/minitaur/agents/trajectory_generator/tg_simple.py

```
"""Trajectory Generator generates walking leg motions for a quadruped robot.

Trajectory Generator (TG) has an internal state (phase) and generates
walking-like motion for 8 motors of minitaur quadruped robot based on
parameters
such as:
 - delta time to progress the TG's internal state.
 - intensity to control amount of movement (stride length and lift of the legs).
 - waking height to control the average extension of the legs.

Each time step() is called, the internal state is progressed and 8 motor
positions are generated. This TG uses the open-loop SineController class to
provide leg position"""
class TgSimple(object)
    """TgSimple class is a simplified trajectory generator for quadruped walking.

It returns 8 actions for quadruped slow walking behavior
based on the parameters provided such as intensity, walking height and delta
time. It returns its internal phase as information."""
    def __init__(self, walk_height_lower_bound, walk_height_upper_bound, intensity_lower_bound, intensity_upper_bound, swing_stance_lower_bound, swing_stance_upper_bound, integrator_coupling_mode, walk_height_coupling_mode, variable_swing_stance_ratio, swing_stance_ratio, init_leg_phase_offsets)
    def reset(self)
    def get_parameter_bounds(self)
    def get_actions(self, delta_real_time, tg_params)
    def _process_tg_params(self, tg_params)
    def get_state(self)
    def get_state_lower_bounds(self)
    def get_state_upper_bounds(self)
    def adjust_swing_stance_ratio(self, target_swing_stance_ratio)
    def num_integrators(self)
class CircularAsymmetricalIntegratorUnit(object)
    """A circular integrator with asymmetry between first and second half.

An integrator is a memory unit that accumulates the given parameter at every
time step.
A circular integrator is when the integrator cycles within [0,2pi].
The phase of a circular integrator indicates the accumulated number and it """
    def __init__(self, init_phase)
    def reset(self)
    def calculate_progressed_phase(self, delta_period, swing_stance_speed_ratio)
    def progress_phase(self, delta_period, swing_stance_ratio)
    def get_state(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizer_base.py

```
"""Abstract base class for environment randomizer."""
class EnvRandomizerBase(object)
    """Abstract base class for environment randomizer.

Randomizes physical parameters of the objects in the simulation and adds
perturbations to the stepping of the simulation."""
    def randomize_env(self, env)
    def randomize_step(self, env)
    def randomize_sub_step(self, env, sub_step_index, num_sub_steps)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_alternating_legs_env_randomizer.py

```
"""Randomize the minitaur_gym_alternating_leg_env when reset() is called.

The randomization include swing_offset, extension_offset of all legs that mimics
bent legs, desired_pitch from user input, battery voltage and motor damping."""
class MinitaurAlternatingLegsEnvRandomizer(EnvRandomizerBase)
    """A randomizer that changes the minitaur_gym_alternating_leg_env."""
    def __init__(self, perturb_swing_bound, perturb_extension_bound, perturb_desired_pitch_bound)
    def randomize_env(self, env)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_env_randomizer.py

```
"""Randomize the minitaur_gym_env when reset() is called."""
class MinitaurEnvRandomizer(EnvRandomizerBase)
    """A randomizer that change the minitaur_gym_env during every reset."""
    def __init__(self, minitaur_base_mass_err_range, minitaur_leg_mass_err_range, battery_voltage_range, motor_viscous_damping_range)
    def randomize_env(self, env)
    def _randomize_minitaur(self, minitaur)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_env_randomizer_config.py

```
"""A config file for parameters and their ranges in dynamics randomization."""
def all_params()
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_env_randomizer_from_config.py

```
"""An environment randomizer that randomizes physical parameters from config."""
class MinitaurEnvRandomizerFromConfig(EnvRandomizerBase)
    """A randomizer that change the minitaur_gym_env during every reset."""
    def __init__(self, config)
    def randomize_env(self, env)
    def _build_randomization_function_dict(self, env)
    def _randomize_control_step(self, env, lower_bound, upper_bound)
    def _randomize_masses(self, minitaur, lower_bound, upper_bound)
    def _randomize_inertia(self, minitaur, lower_bound, upper_bound)
    def _randomize_latency(self, minitaur, lower_bound, upper_bound)
    def _randomize_joint_friction(self, minitaur, lower_bound, upper_bound)
    def _randomize_motor_friction(self, minitaur, lower_bound, upper_bound)
    def _randomize_contact_restitution(self, minitaur, lower_bound, upper_bound)
    def _randomize_contact_friction(self, minitaur, lower_bound, upper_bound)
    def _randomize_battery_level(self, minitaur, lower_bound, upper_bound)
    def _randomize_motor_strength(self, minitaur, lower_bound, upper_bound)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_push_randomizer.py

```
"""Adds random forces to the base of Minitaur during the simulation steps."""
class MinitaurPushRandomizer(EnvRandomizerBase)
    """Applies a random impulse to the base of Minitaur."""
    def __init__(self, perturbation_start_step, perturbation_interval_steps, perturbation_duration_steps, horizontal_force_bound, vertical_force_bound)
    def randomize_env(self, env)
    def randomize_step(self, env)
    def randomize_sub_step(self, env, sub_step_index, num_sub_steps)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/env_randomizers/minitaur_terrain_randomizer.py

```
"""Generates a random terrain at Minitaur gym environment reset."""
class PoissonDisc2D(object)
    """Generates 2D points using Poisson disk sampling method.

Implements the algorithm described in:
  http://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf
Unlike the uniform sampling method that creates small clusters of points,
Poisson disk method enforces the minimum distance between"""
    def __init__(self, grid_length, grid_width, min_radius, max_sample_size)
    def _point_to_index_1d(self, point)
    def _point_to_index_2d(self, point)
    def _index_2d_to_1d(self, index2d)
    def _is_in_grid(self, point)
    def _is_in_range(self, index2d)
    def _is_close_to_existing_points(self, point)
    def sample(self)
    def generate(self)
class TerrainType(Enum)
    """The randomzied terrain types we can use in the gym env."""
class MinitaurTerrainRandomizer(EnvRandomizerBase)
    """Generates an uneven terrain in the gym env."""
    def __init__(self, terrain_type, mesh_filename, mesh_scale)
    def randomize_env(self, env)
    def _load_triangle_mesh(self, env)
    def _generate_convex_blocks(self, env)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur.py

```
"""This file implements the functionalities of a minitaur using pybullet."""
def MapToMinusPiToPi(angles)
class Minitaur(object)
    """The minitaur class that simulates a quadruped robot from Ghost Robotics.

  """
    def __init__(self, pybullet_client, urdf_root, time_step, action_repeat, self_collision_enabled, motor_velocity_limit, pd_control_enabled, accurate_motor_model_enabled, remove_default_joint_damping, motor_kp, motor_kd, pd_latency, control_latency, observation_noise_stdev, torque_control_enabled, motor_overheat_protection, on_rack)
    def GetTimeSinceReset(self)
    def Step(self, action)
    def Terminate(self)
    def _RecordMassInfoFromURDF(self)
    def _RecordInertiaInfoFromURDF(self)
    def _BuildJointNameToIdDict(self)
    def _BuildUrdfIds(self)
    def _RemoveDefaultJointDamping(self)
    def _BuildMotorIdList(self)
    def IsObservationValid(self)
    def Reset(self, reload_urdf, default_motor_angles, reset_time)
    def _SetMotorTorqueById(self, motor_id, torque)
    def _SetDesiredMotorAngleById(self, motor_id, desired_angle)
    def _SetDesiredMotorAngleByName(self, motor_name, desired_angle)
    def ResetPose(self, add_constraint)
    def _ResetPoseForLeg(self, leg_id, add_constraint)
    def GetBasePosition(self)
    def GetTrueBaseRollPitchYaw(self)
    def GetBaseRollPitchYaw(self)
    def GetTrueMotorAngles(self)
    def GetMotorAngles(self)
    def GetTrueMotorVelocities(self)
    def GetMotorVelocities(self)
    def GetTrueMotorTorques(self)
    def GetMotorTorques(self)
    def GetTrueBaseOrientation(self)
    def GetBaseOrientation(self)
    def GetTrueBaseRollPitchYawRate(self)
    def GetBaseRollPitchYawRate(self)
    def GetActionDimension(self)
    def ApplyAction(self, motor_commands, motor_kps, motor_kds)
    def ConvertFromLegModel(self, actions)
    def GetBaseMassesFromURDF(self)
    def GetBaseInertiasFromURDF(self)
    def GetLegMassesFromURDF(self)
    def GetLegInertiasFromURDF(self)
    def SetBaseMasses(self, base_mass)
    def SetLegMasses(self, leg_masses)
    def SetBaseInertias(self, base_inertias)
    def SetLegInertias(self, leg_inertias)
    def SetFootFriction(self, foot_friction)
    def SetFootRestitution(self, foot_restitution)
    def SetJointFriction(self, joint_frictions)
    def GetNumKneeJoints(self)
    def SetBatteryVoltage(self, voltage)
    def SetMotorViscousDamping(self, viscous_damping)
    def GetTrueObservation(self)
    def ReceiveObservation(self)
    def _GetDelayedObservation(self, latency)
    def _GetPDObservation(self)
    def _GetControlObservation(self)
    def _AddSensorNoise(self, sensor_values, noise_stdev)
    def SetControlLatency(self, latency)
    def GetControlLatency(self)
    def SetMotorGains(self, kp, kd)
    def GetMotorGains(self)
    def SetMotorStrengthRatio(self, ratio)
    def SetMotorStrengthRatios(self, ratios)
    def SetTimeSteps(self, action_repeat, simulation_step)
    def chassis_link_ids(self)

```python
def IsObservationValid(self):
    """Whether the observation is valid for the current time step.

    In simulation, observations are always valid. In real hardware, it may not
    be valid from time to time when communication error happens between the
    Nvidia TX2 and the microcontroller.

    Returns:
      Whether the observation is valid for the current time step.
    """
    return True
```

```python
def GetTrueObservation(self):
    observation = []
    observation.extend(self.GetTrueMotorAngles())
    observation.extend(self.GetTrueMotorVelocities())
    observation.extend(self.GetTrueMotorTorques())
    observation.extend(self.GetTrueBaseOrientation())
    observation.extend(self.GetTrueBaseRollPitchYawRate())
    return observation
```

```python
def ReceiveObservation(self):
    """Receive the observation from sensors.

    This function is called once per step. The observations are only updated
    when this function is called.
    """
    self._observation_history.appendleft(self.GetTrueObservation())
    self._control_observation = self._GetControlObservation()
```

```python
def _GetDelayedObservation(self, latency):
    """Get observation that is delayed by the amount specified in latency.

    Args:
      latency: The latency (in seconds) of the delayed observation.
    Returns:
      observation: The observation which was actually latency seconds ago.
    """
    if latency <= 0 or len(self._observation_history) == 1:
      observation = self._observation_history[0]
    else:
      n_steps_ago = int(latency / self.time_step)
      if n_steps_ago + 1 >= len(self._observation_history):
        return self._observation_history[-1]
      remaining_latency = latency - n_steps_ago * self.time_step
      blend_alpha = remaining_latency / self.time_step
      observation = ((1.0 - blend_alpha) * np.array(self._observation_history[n_steps_ago]) +
                     blend_alpha * np.array(self._observation_history[n_steps_ago + 1]))
    return observation
```

```python
def _GetPDObservation(self):
    pd_delayed_observation = self._GetDelayedObservation(self._pd_latency)
    q = pd_delayed_observation[0:self.num_motors]
    qdot = pd_delayed_observation[self.num_motors:2 * self.num_motors]
    return (np.array(q), np.array(qdot))
```

```python
def _GetControlObservation(self):
    control_delayed_observation = self._GetDelayedObservation(self._control_latency)
    return control_delayed_observation
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_alternating_legs_env.py

```
"""This file implements the gym environment of minitaur alternating legs."""
class MinitaurAlternatingLegsEnv(MinitaurGymEnv)
    """The gym environment for the minitaur.

It simulates the locomotion of a minitaur, a quadruped robot. The state space
include the angles, velocities and torques for all the motors and the action
space is the desired motor angle for each motor. The reward function is based
on how far the minitaur walk"""
    def __init__(self, urdf_version, control_time_step, action_repeat, control_latency, pd_latency, on_rack, motor_kp, motor_kd, remove_default_joint_damping, render, num_steps_to_log, env_randomizer, log_path)
    def reset(self)
    def _convert_from_leg_model(self, leg_pose)
    def _signal(self, t)
    def _transform_action_to_motor_command(self, action)
    def is_fallen(self)
    def _reward(self)
    def _get_true_observation(self)
    def _get_observation(self)
    def _get_observation_upper_bound(self)
    def _get_observation_lower_bound(self)
    def set_swing_offset(self, value)
    def set_extension_offset(self, value)
    def set_desired_pitch(self, value)

```python
def _reward(self):
    return 1.0
```

```python
def _get_true_observation(self):
    """Get the true observations of this environment.

    It includes the roll, the error between current pitch and desired pitch,
    roll dot and pitch dot of the base.

    Returns:
      The observation list.
    """
    observation = []
    roll, pitch, _ = self.minitaur.GetTrueBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetTrueBaseRollPitchYawRate()
    observation.extend([roll, pitch, roll_rate, pitch_rate])
    observation[1] -= self.desired_pitch  # observation[1] is the pitch
    self._true_observation = np.array(observation)
    return self._true_observation
```

```python
def _get_observation(self):
    observation = []
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetBaseRollPitchYawRate()
    observation.extend([roll, pitch, roll_rate, pitch_rate])
    observation[1] -= self.desired_pitch  # observation[1] is the pitch
    self._observation = np.array(observation)
    return self._observation
```

```python
def _get_observation_upper_bound(self):
    """Get the upper bound of the observation.

    Returns:
      The upper bound of an observation. See GetObservation() for the details
        of each element of an observation.
    """
    upper_bound = np.zeros(self._get_observation_dimension())
    upper_bound[0:2] = 2 * math.pi  # Roll, pitch, yaw of the base.
    upper_bound[2:4] = 2 * math.pi / self._time_step  # Roll, pitch, yaw rate.
    return upper_bound
```

```python
def _get_observation_lower_bound(self):
    lower_bound = -self._get_observation_upper_bound()
    return lower_bound
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_alternating_legs_env_example.py

```
"""An example to run the minitaur environment of alternating legs."""
def hand_tuned_agent(observation, timestamp)
def hand_tuned_balance_example(log_path)
def main(unused_argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_ball_gym_env.py

```
"""This file implements the gym environment of minitaur."""
class MinitaurBallGymEnv(MinitaurGymEnv)
    """The gym environment for the minitaur and a ball.

It simulates a minitaur (a quadruped robot) and a ball. The state space
includes the angle and distance of the ball relative to minitaur's base.
The action space is a steering command. The reward function is based
on how far the ball is relative to t"""
    def __init__(self, urdf_root, self_collision_enabled, pd_control_enabled, leg_model_enabled, on_rack, render)
    def reset(self)
    def _get_observation(self)
    def _transform_action_to_motor_command(self, action)
    def _apply_steering_to_locomotion(self, action)
    def _distance_to_ball(self)
    def _goal_state(self)
    def _reward(self)
    def _termination(self)

```python
def _get_observation(self):
    world_translation_minitaur, world_rotation_minitaur = (
        self._pybullet_client.getBasePositionAndOrientation(self.minitaur.quadruped))
    world_translation_ball, world_rotation_ball = (
        self._pybullet_client.getBasePositionAndOrientation(self._ball_id))
    minitaur_translation_world, minitaur_rotation_world = (self._pybullet_client.invertTransform(
        world_translation_minitaur, world_rotation_minitaur))
    minitaur_translation_ball, _ = (self._pybullet_client.multiplyTransforms(
        minitaur_translation_world, minitaur_rotation_world, world_translation_ball,
        world_rotation_ball))
    distance = math.sqrt(minitaur_translation_ball[0]**2 + minitaur_translation_ball[1]**2)
    angle = math.atan2(minitaur_translation_ball[0], minitaur_translation_ball[1])
    self._observation = [angle - math.pi / 2, distance]
    return self._observation
```

```python
def _reward(self):
    reward = -self._observation[1]
    if self._goal_state():
      reward += GOAL_REWARD
    return reward * REWARD_SCALING
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_ball_gym_env_example.py

```
"""An example to run the gym environment that a minitaur follows a ball."""
def FollowBallManualPolicy()
def main()
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_derpy.py

```
"""This file implements the functionalities of a minitaur derpy using pybullet.

It is the result of first pass system identification for the derpy robot. The"""
class MinitaurDerpy(Minitaur)
    """The minitaur class that simulates a quadruped robot from Ghost Robotics.

  """
    def Reset(self, reload_urdf, default_motor_angles, reset_time)
    def _ResetPoseForLeg(self, leg_id, add_constraint)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_extended_env.py

```
"""Extends the environment by adding observation and action history.

The implementation is a bit dirty import of the implementation in
the experimental branch."""
class MinitaurExtendedEnv(MinitaurReactiveEnv)
    """The 'extended' environment for Markovian property.

This class implements to include prior actions and observations to the
observation vector, thus making the environment "more" Markovian. This is
especially useful for systems with latencies.

Args:
  history_length: the length of the historic data
"""
    def __init__(self, history_length, history_include_actions, history_include_states, include_state_difference, include_second_state_difference, include_base_position, include_leg_model, never_terminate, action_scale)
    def _get_observation(self)
    def reset(self)
    def step(self, action)
    def terminate(self)
    def _termination(self)
    def reward(self)
    def convert_to_leg_model(motor_angles)
    def __getstate__(self)
    def __setstate__(self, state)

```python
def _get_observation(self):
    """Maybe concatenate motor velocity and torque into observations."""
    parent_observation = super(MinitaurExtendedEnv, self)._get_observation()
    parent_observation = np.array(parent_observation)
    # Base class might require this.
    self._observation = parent_observation
    self._past_parent_observations[self._counter] = parent_observation
    num_motors = self.minitaur.num_motors
    self._past_motor_angles[self._counter] = parent_observation[-num_motors:]

    history_states = []
    history_actions = []
    for i in range(self._history_length):
      t = max(self._counter - i - 1, 0)

      if self._history_include_states:
        history_states.append(self._past_parent_observations[t])

      if self._history_include_actions:
        history_actions.append(self._past_actions[t])

    t = self._counter
    tm, tmm = max(0, self._counter - 1), max(0, self._counter - 2)

    state_difference, second_state_difference = [], []
    if self._include_state_difference:
      state_difference = [
          self._past_motor_angles[t] - self._past_motor_angles[tm]
      ]
    if self._include_second_state_difference:
      second_state_difference = [
          self._past_motor_angles[t] - 2 * self._past_motor_angles[tm] +
          self._past_motor_angles[tmm]
      ]

    base_position = []
    if self._include_base_position:
      base_position = np.array((self.minitaur.GetBasePosition()))

    leg_model = []
    if self._include_leg_model:
      raw_motor_angles = self.minitaur.GetMotorAngles()
      leg_model = self.convert_to_leg_model(raw_motor_angles)

    observation_list = (
        [parent_observation] + history_states + history_actions +
        state_difference + second_state_difference + [base_position] +
        [leg_model])

    full_observation = np.concatenate(observation_list)
    return full_observation
```

```python
def reward(self):
    """Compute rewards for the given time step.

    It considers two terms: 1) forward velocity reward and 2) action
    acceleration penalty.

    Returns:
      reward: the computed reward.
    """
    current_base_position = self.minitaur.GetBasePosition()
    dt = self.control_time_step
    velocity = (current_base_position[0] - self._last_base_position[0]) / dt
    velocity_reward = np.clip(velocity, -0.5, 0.5)

    action = self._past_actions[self._counter - 1]
    prev_action = self._past_actions[max(self._counter - 2, 0)]
    prev_prev_action = self._past_actions[max(self._counter - 3, 0)]
    acc = action - 2 * prev_action + prev_prev_action
    action_acceleration_penalty = np.mean(np.abs(acc))

    reward = 0.0
    reward += 1.0 * velocity_reward
    reward -= 0.1 * action_acceleration_penalty

    return reward
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_four_leg_stand_env.py

```
"""This file implements the gym environment of minitaur standing with four legs."""
class MinitaurFourLegStandEnv(MinitaurGymEnv)
    """The gym environment for the minitaur.

It simulates the a minitaur standing with four legs. The state space
include the orientation of the torso, and the action space is the desired
motor angle for each motor. The reward function is based on how close the
action to zero and the height of the robot b"""
    def __init__(self, urdf_version, hard_reset, remove_default_joint_damping, control_latency, pd_latency, on_rack, motor_kp, motor_kd, render, env_randomizer, use_angular_velocity_in_observation, use_motor_angle_in_observation, control_time_step, action_repeat, log_path)
    def reset(self)
    def step(self, action)
    def _convert_from_leg_model(self, leg_pose)
    def _signal(self, t)
    def _transform_action_to_motor_command(self, action)
    def is_fallen(self)
    def _reward(self)
    def _get_observation(self)
    def _get_true_observation(self)
    def _get_observation_upper_bound(self)
    def _get_observation_lower_bound(self)
    def set_swing_offset(self, value)
    def set_extension_offset(self, value)
    def set_desired_pitch(self, value)

```python
def _reward(self):
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    return 1.0 / (0.001 + math.fabs(roll) + math.fabs(pitch))
```

```python
def _get_observation(self):
    """Get the true observations of this environment.

    It includes the roll, pitch, roll dot, pitch dot of the base, and the motor
    angles.

    Returns:
      The observation list.
    """
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    observation = [roll, pitch]
    if self._use_angular_velocity_in_observation:
      roll_rate, pitch_rate, _ = self.minitaur.GetBaseRollPitchYawRate()
      observation.extend([roll_rate, pitch_rate])
    if self._use_motor_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())
    self._observation = np.array(observation)
    return self._observation
```

```python
def _get_true_observation(self):
    """Get the true observations of this environment.

    It includes the roll, pitch, roll dot, pitch dot of the base, and the motor
    angles.

    Returns:
      The observation list.
    """
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    observation = [roll, pitch]
    if self._use_angular_velocity_in_observation:
      roll_rate, pitch_rate, _ = self.minitaur.GetBaseRollPitchYawRate()
      observation.extend([roll_rate, pitch_rate])
    if self._use_motor_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())

    self._observation = np.array(observation)
    return self._observation
```

```python
def _get_observation_upper_bound(self):
    """Get the upper bound of the observation.

    Returns:
      The upper bound of an observation. See GetObservation() for the details
        of each element of an observation.
    """
    upper_bound = [2 * math.pi] * 2  # Roll, pitch the base.
    if self._use_angular_velocity_in_observation:
      upper_bound.extend([2 * math.pi / self._time_step] * 2)
    if self._use_motor_angle_in_observation:
      upper_bound.extend([2 * math.pi] * 8)
    return np.array(upper_bound)
```

```python
def _get_observation_lower_bound(self):
    lower_bound = -self._get_observation_upper_bound()
    return lower_bound
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_four_leg_stand_env_example.py

```
"""An example to run the minitaur environment of standing with four legs."""
def feed_forward_only_control_example(log_path)
def main(unused_argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_gym_env.py

```
"""This file implements the gym environment of minitaur."""
def convert_to_list(obj)
class MinitaurGymEnv(Env)
    """The gym environment for the minitaur.

It simulates the locomotion of a minitaur, a quadruped robot. The state space
include the angles, velocities and torques for all the motors and the action
space is the desired motor angle for each motor. The reward function is based
on how far the minitaur walk"""
    def __init__(self, urdf_root, urdf_version, distance_weight, energy_weight, shake_weight, drift_weight, distance_limit, observation_noise_stdev, self_collision_enabled, motor_velocity_limit, pd_control_enabled, leg_model_enabled, accurate_motor_model_enabled, remove_default_joint_damping, motor_kp, motor_kd, control_latency, pd_latency, torque_control_enabled, motor_overheat_protection, hard_reset, on_rack, render, num_steps_to_log, action_repeat, control_time_step, env_randomizer, forward_reward_cap, reflection, log_path)
    def close(self)
    def add_env_randomizer(self, env_randomizer)
    def reset(self, initial_motor_angles, reset_duration)
    def seed(self, seed)
    def _transform_action_to_motor_command(self, action)
    def step(self, action)
    def render(self, mode, close)
    def get_minitaur_motor_angles(self)
    def get_minitaur_motor_velocities(self)
    def get_minitaur_motor_torques(self)
    def get_minitaur_base_orientation(self)
    def is_fallen(self)
    def _termination(self)
    def _reward(self)
    def get_objectives(self)
    def objective_weights(self)
    def _get_observation(self)
    def _get_true_observation(self)
    def _get_observation_upper_bound(self)
    def _get_observation_lower_bound(self)
    def _get_observation_dimension(self)
    def set_time_step(self, control_step, simulation_step)
    def pybullet_client(self)
    def ground_id(self)
    def ground_id(self, new_ground_id)
    def env_step_counter(self)

```python
def _reward(self):
    current_base_position = self.minitaur.GetBasePosition()
    forward_reward = current_base_position[0] - self._last_base_position[0]
    # Cap the forward reward if a cap is set.
    forward_reward = min(forward_reward, self._forward_reward_cap)
    # Penalty for sideways translation.
    drift_reward = -abs(current_base_position[1] - self._last_base_position[1])
    # Penalty for sideways rotation of the body.
    orientation = self.minitaur.GetBaseOrientation()
    rot_matrix = pybullet.getMatrixFromQuaternion(orientation)
    local_up_vec = rot_matrix[6:]
    shake_reward = -abs(np.dot(np.asarray([1, 1, 0]), np.asarray(local_up_vec)))
    energy_reward = -np.abs(
        np.dot(self.minitaur.GetMotorTorques(),
               self.minitaur.GetMotorVelocities())) * self._time_step
    objectives = [forward_reward, energy_reward, drift_reward, shake_reward]
    weighted_objectives = [o * w for o, w in zip(objectives, self._objective_weights)]
    reward = sum(weighted_objectives)
    self._objectives.append(objectives)
    return reward
```

```python
def _get_observation(self):
    """Get observation of this environment, including noise and latency.

    The minitaur class maintains a history of true observations. Based on the
    latency, this function will find the observation at the right time,
    interpolate if necessary. Then Gaussian noise is added to this observation
    based on self.observation_noise_stdev.

    Returns:
      The noisy observation with latency.
    """

    observation = []
    observation.extend(self.minitaur.GetMotorAngles().tolist())
    observation.extend(self.minitaur.GetMotorVelocities().tolist())
    observation.extend(self.minitaur.GetMotorTorques().tolist())
    observation.extend(list(self.minitaur.GetBaseOrientation()))
    self._observation = observation
    return self._observation
```

```python
def _get_true_observation(self):
    """Get the observations of this environment.

    It includes the angles, velocities, torques and the orientation of the base.

    Returns:
      The observation list. observation[0:8] are motor angles. observation[8:16]
      are motor velocities, observation[16:24] are motor torques.
      observation[24:28] is the orientation of the base, in quaternion form.
    """
    observation = []
    observation.extend(self.minitaur.GetTrueMotorAngles().tolist())
    observation.extend(self.minitaur.GetTrueMotorVelocities().tolist())
    observation.extend(self.minitaur.GetTrueMotorTorques().tolist())
    observation.extend(list(self.minitaur.GetTrueBaseOrientation()))

    self._true_observation = observation
    return self._true_observation
```

```python
def _get_observation_upper_bound(self):
    """Get the upper bound of the observation.

    Returns:
      The upper bound of an observation. See GetObservation() for the details
        of each element of an observation.
    """
    upper_bound = np.zeros(self._get_observation_dimension())
    num_motors = self.minitaur.num_motors
    upper_bound[0:num_motors] = math.pi  # Joint angle.
    upper_bound[num_motors:2 * num_motors] = (motor.MOTOR_SPEED_LIMIT)  # Joint velocity.
    upper_bound[2 * num_motors:3 * num_motors] = (motor.OBSERVED_TORQUE_LIMIT)  # Joint torque.
    upper_bound[3 * num_motors:] = 1.0  # Quaternion of base orientation.
    return upper_bound
```

```python
def _get_observation_lower_bound(self):
    """Get the lower bound of the observation."""
    return -self._get_observation_upper_bound()
```

```python
def _get_observation_dimension(self):
    """Get the length of the observation list.

    Returns:
      The length of the observation list.
    """
    return len(self._get_observation())
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_gym_env_example.py

```
"""An example to run of the minitaur gym environment with sine gaits."""
def WriteToCSV(filename, actions_and_observations)
def ResetPoseExample(log_path)
def MotorOverheatExample(log_path)
def SineStandExample(log_path)
def SinePolicyExample(log_path)
def main()
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_logging.py

```
"""A proto buffer based logging system for minitaur experiments.

The logging system records the time since reset, base position, orientation,
angular velocity and motor information (joint angle, speed, and torque) into a
proto buffer. See minitaur_logging.proto for more details. The episode_proto is
updated per time step by the environment and saved onto disk for each episode."""
def _update_base_state(base_state, values)
def preallocate_episode_proto(episode_proto, max_num_steps)
def update_episode_proto(episode_proto, minitaur, action, step)
class MinitaurLogging(object)
    """A logging system that records the states/action of the minitaur."""
    def __init__(self, log_path)
    def save_episode(self, episode_proto)
    def restore_episode(self, log_path)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_logging_pb2.py

```
"""Generated protocol buffer code."""
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_raibert_controller.py

```
"""A Raibert style controller for Minitaur."""
class BehaviorParameters(?)
    def __new__(cls, stance_duration, desired_forward_speed, turning_speed, standing_height, desired_incline_angle)
def motor_angles_to_leg_pose(motor_angles)
def leg_pose_to_motor_angles(leg_pose)
def leg_pose_to_foot_position(leg_pose)
def foot_position_to_leg_pose(foot_position)
def foot_horizontal_position_to_leg_swing(foot_horizontal_position, leg_extension)
def extension_to_ankle_dist(ext)
def ankle_dist_to_extension(dist)
def generate_swing_trajectory(phase, init_pose, end_pose)
def generate_stance_trajectory(phase, init_pose, end_pose)
class RaibertSwingLegController(object)
    def __init__(self, speed_gain, leg_extension_clearance, leg_trajectory_generator)
    def get_action(self, raibiert_controller)
class RaibertStanceLegController(object)
    def __init__(self, speed_gain, leg_trajectory_generator)
    def get_action(self, raibiert_controller)
class MinitaurRaibertTrottingController(object)
    """A Raibert style controller for trotting gait."""
    def __init__(self, robot, behavior_parameters, swing_leg_controller, stance_leg_controller, pose_feedback_controller)
    def behavior_parameters(self)
    def behavior_parameters(self, behavior_parameters)
    def nominal_leg_extension(self)
    def swing_set(self)
    def stance_set(self)
    def swing_start_leg_pose(self)
    def stance_start_leg_pose(self)
    def _get_average_leg_pose(self, leg_indices)
    def get_swing_leg_pose(self)
    def get_stance_leg_pose(self)
    def get_phase(self)
    def update_swing_stance_set(self)
    def update(self, t)
    def estimate_base_velocity(self)
    def get_swing_leg_action(self)
    def get_stance_leg_action(self)
    def get_action(self)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_raibert_controller_example.py

```
def speed(t)
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_rainbow_dash.py

```
"""Implements the functionalities of a minitaur rainbow dash using pybullet.

It is the result of first pass system identification for the rainbow dash robot."""
class MinitaurRainbowDash(Minitaur)
    """The minitaur class that simulates a quadruped robot from Ghost Robotics.

  """
    def Reset(self, reload_urdf, default_motor_angles, reset_time)
    def _ResetPoseForLeg(self, leg_id, add_constraint)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_randomize_terrain_gym_env.py

```
"""Gym environment of minitaur which randomize the terrain at each reset."""
class MinitaurRandomizeTerrainGymEnv(MinitaurGymEnv)
    """The gym environment for the minitaur with randomized terrain.

It simulates a minitaur (a quadruped robot) on a randomized terrain. The state
space include the angles, velocities and torques for all the motors and the
action space is the desired motor angle for each motor. The reward function is
bas"""
    def reset(self)
    def load_random_terrain(self, terrain_dir)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_randomize_terrain_gym_env_example.py

```
"""An example to run minitaur gym environment with randomized terrain."""
def ResetTerrainExample()
def SinePolicyExample()
def main(unused_argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_reactive_env.py

```
"""This file implements the gym environment of minitaur alternating legs."""
class MinitaurReactiveEnv(MinitaurGymEnv)
    """The gym environment for the minitaur.

It simulates the locomotion of a minitaur, a quadruped robot. The state space
include the angles, velocities and torques for all the motors and the action
space is the desired motor angle for each motor. The reward function is based
on how far the minitaur walk"""
    def __init__(self, urdf_version, energy_weight, control_time_step, action_repeat, control_latency, pd_latency, on_rack, motor_kp, motor_kd, remove_default_joint_damping, render, num_steps_to_log, accurate_motor_model_enabled, use_angle_in_observation, hard_reset, env_randomizer, log_path)
    def reset(self)
    def _convert_from_leg_model(self, leg_pose)
    def _signal(self, t)
    def _transform_action_to_motor_command(self, action)
    def is_fallen(self)
    def _get_true_observation(self)
    def _get_observation(self)
    def _get_observation_upper_bound(self)
    def _get_observation_lower_bound(self)

```python
def _get_true_observation(self):
    """Get the true observations of this environment.

    It includes the roll, the pitch, the roll dot and the pitch dot of the base.
    If _use_angle_in_observation is true, eight motor angles are added into the
    observation.

    Returns:
      The observation list, which is a numpy array of floating-point values.
    """
    roll, pitch, _ = self.minitaur.GetTrueBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetTrueBaseRollPitchYawRate()
    observation = [roll, pitch, roll_rate, pitch_rate]
    if self._use_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())
    self._true_observation = np.array(observation)
    return self._true_observation
```

```python
def _get_observation(self):
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetBaseRollPitchYawRate()
    observation = [roll, pitch, roll_rate, pitch_rate]
    if self._use_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())
    self._observation = np.array(observation)
    return self._observation
```

```python
def _get_observation_upper_bound(self):
    """Get the upper bound of the observation.

    Returns:
      The upper bound of an observation. See _get_true_observation() for the
      details of each element of an observation.
    """
    upper_bound_roll = 2 * math.pi
    upper_bound_pitch = 2 * math.pi
    upper_bound_roll_dot = 2 * math.pi / self._time_step
    upper_bound_pitch_dot = 2 * math.pi / self._time_step
    upper_bound_motor_angle = 2 * math.pi
    upper_bound = [
        upper_bound_roll, upper_bound_pitch, upper_bound_roll_dot, upper_bound_pitch_dot
    ]

    if self._use_angle_in_observation:
      upper_bound.extend([upper_bound_motor_angle] * NUM_MOTORS)
    return np.array(upper_bound)
```

```python
def _get_observation_lower_bound(self):
    lower_bound = -self._get_observation_upper_bound()
    return lower_bound
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_reactive_env_example.py

```
"""Running a pre-trained ppo agent on minitaur_reactive_env."""
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_stand_gym_env.py

```
"""This file implements the gym environment of minitaur."""
class MinitaurStandGymEnv(MinitaurGymEnv)
    """The gym environment for the minitaur and a ball.

It simulates the standing up behavior of a minitaur, a quadruped robot. The
state space include the angles, velocities and torques for all the motors and
the action space is the desired motor angle for each motor. The reward
function is based on how """
    def __init__(self, urdf_root, action_repeat, observation_noise_stdev, self_collision_enabled, motor_velocity_limit, pd_control_enabled, render)
    def _stand_up(self)
    def step(self, action)
    def _reward(self)
    def _termination(self)
    def _is_horizontal(self)
    def _transform_action_to_motor_command(self, action)
    def _policy_flip(self, time_step, orientation)

```python
def _reward(self):
    """Reward function for standing up pose.

    Returns:
      reward: A number between -1 and 1 according to how vertical is the body of
        the robot.
    """
    orientation = self.minitaur.GetBaseOrientation()
    rot_matrix = self._pybullet_client.getMatrixFromQuaternion(orientation)
    local_front_vec = rot_matrix[6:9]
    alignment = abs(np.dot(np.asarray([1, 0, 0]), np.asarray(local_front_vec)))
    return alignment**4
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_stand_gym_env_example.py

```
"""An example to run of the minitaur gym environment with standing up goal."""
def StandUpExample()
def main(unused_argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_trotting_env.py

```
"""Implements the gym environment of minitaur moving with trotting style."""
class MinitaurTrottingEnv(MinitaurGymEnv)
    """The trotting gym environment for the minitaur.

In this env, Minitaur performs a trotting style locomotion specified by
extension_amplitude, swing_amplitude, and step_frequency. Each diagonal pair
of legs will move according to the reference trajectory:
    extension = extsion_amplitude * cos(2 * pi"""
    def __init__(self, urdf_version, control_time_step, action_repeat, control_latency, pd_latency, on_rack, motor_kp, motor_kd, remove_default_joint_damping, render, num_steps_to_log, accurate_motor_model_enabled, use_signal_in_observation, use_angle_in_observation, hard_reset, env_randomizer, log_path, init_extension, init_swing, step_frequency, extension_amplitude, swing_amplitude)
    def reset(self)
    def _convert_from_leg_model(self, leg_pose)
    def _gen_signal(self, t, phase)
    def _signal(self, t)
    def _transform_action_to_motor_command(self, action)
    def is_fallen(self)
    def _get_true_observation(self)
    def _get_observation(self)
    def _get_observation_upper_bound(self)
    def _get_observation_lower_bound(self)
    def set_swing_offset(self, value)
    def set_extension_offset(self, value)

```python
def _get_true_observation(self):
    """Get the true observations of this environment.

    It includes the true roll, pitch, roll dot and pitch dot of the base. Also
    includes the disired/observed motor angles if the relevant flags are set.

    Returns:
      The observation list.
    """
    observation = []
    roll, pitch, _ = self.minitaur.GetTrueBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetTrueBaseRollPitchYawRate()
    observation.extend([roll, pitch, roll_rate, pitch_rate])
    if self._use_signal_in_observation:
      observation.extend(self._transform_action_to_motor_command([0] * 8))
    if self._use_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())
    self._true_observation = np.array(observation)
    return self._true_observation
```

```python
def _get_observation(self):
    """Get observations of this environment.

    It includes the base roll, pitch, roll dot and pitch dot which may contain
    noises, bias, and latency. Also includes the disired/observed motor angles
    if the relevant flags are set.

    Returns:
      The observation list.
    """
    observation = []
    roll, pitch, _ = self.minitaur.GetBaseRollPitchYaw()
    roll_rate, pitch_rate, _ = self.minitaur.GetBaseRollPitchYawRate()
    observation.extend([roll, pitch, roll_rate, pitch_rate])
    if self._use_signal_in_observation:
      observation.extend(self._transform_action_to_motor_command([0] * 8))
    if self._use_angle_in_observation:
      observation.extend(self.minitaur.GetMotorAngles().tolist())
    self._observation = np.array(observation)
    return self._observation
```

```python
def _get_observation_upper_bound(self):
    """Get the upper bound of the observation.

    Returns:
      A numpy array contains the upper bound of an observation. See
      GetObservation() for the details of each element of an observation.
    """
    upper_bound = []
    upper_bound.extend([2 * math.pi] * 2)  # Roll, pitch, yaw of the base.
    upper_bound.extend([2 * math.pi / self._time_step] * 2)  # Roll, pitch, yaw rate.
    if self._use_signal_in_observation:
      upper_bound.extend([2 * math.pi] * NUM_MOTORS)  # Signal
    if self._use_angle_in_observation:
      upper_bound.extend([2 * math.pi] * NUM_MOTORS)  # Motor angles
    return np.array(upper_bound)
```

```python
def _get_observation_lower_bound(self):
    """Get the lower bound of the observation.

    Returns:
      The lower bound of an observation (the reverse of the upper bound).
    """
    lower_bound = -self._get_observation_upper_bound()
    return lower_bound
```
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/minitaur_trotting_env_example.py

```
"""Running a pre-trained ppo agent on minitaur_trotting_env."""
def main(argv)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/motor.py

```
"""This file implements an accurate motor model."""
class MotorModel(object)
    """The accurate motor model, which is based on the physics of DC motors.

The motor model support two types of control: position control and torque
control. In position control mode, a desired motor angle is specified, and a
torque is computed based on the internal motor model. When the torque control
"""
    def __init__(self, torque_control_enabled, kp, kd)
    def set_strength_ratios(self, ratios)
    def set_motor_gains(self, kp, kd)
    def set_voltage(self, voltage)
    def get_voltage(self)
    def set_viscous_damping(self, viscous_damping)
    def get_viscous_dampling(self)
    def convert_to_torque(self, motor_commands, motor_angle, motor_velocity, true_motor_velocity, kp, kd)
    def _convert_to_torque_from_pwm(self, pwm, true_motor_velocity)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/simple_ppo_agent.py

```
"""An agent that can restore and run a policy learned by PPO."""
class SimplePPOPolicy(object)
    """A simple PPO policy that is independent to the PPO infrastructure.

This class restores the policy network from a tensorflow checkpoint that was
learned from PPO training. The purpose of this class is to conveniently
visualize a learned policy or deploy the learned policy on real robots without
need"""
    def __init__(self, sess, env, network, policy_layers, value_layers, checkpoint)
    def _restore_policy(self, network, policy_layers, value_layers, action_size, checkpoint)
    def get_action(self, observation)
    def _denormalize_action(self, action)
    def _normalize_observ(self, observ)
```

### examples/pybullet/gym/pybullet_envs/minitaur/envs/simple_ppo_agent_example.py

```
"""An example to use simple_ppo_agent.

A galloping example:
blaze run -c opt \
//robotics/reinforcement_learning/minitaur/agents:simple_ppo_agent_example -- \
--logdir=/cns/ij-d/home/jietan/experiment/minitaur_vizier_study_ppo/\
minreact_nonexp_nr_01_186515603_186518344/15/ \
--checkpoint=model.ckpt-14000000

A trotting example:
blaze run -c opt \
//robotics/reinforcement_learning/minitaur/agents:simple_ppo_agent_example -- \
--logdir=/cns/ij-d/home/jietan/experiment/minitaur_vizier_study_ppo/\
mintrot_nonexp_rd_01_186515603_186518344/24/ \
--checkpoint=model.ckpt-14000000"""
def main(argv)
```