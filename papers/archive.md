---
layout: page
title: Archive
description: Historical and extended reading list for deep learning in perception.
parent: Papers
nav_order: 6
has_children: false
has_toc: true
---

# Deep Learning Research Papers for Robot Perception: Archive
{:.no_toc}

This page contains historical and extended papers that were previously covered but have since been succeeded by newer methodologies. 

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

# RGB-D Architectures 

- [A Unified Framework for Multi-View Multi-Class Object Pose Estimation](https://arxiv.org/abs/1803.08103), Li et al., 2018
- [PVN3D: A Deep Point-Wise 3D Keypoints Voting Network for 6DoF Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/papers/He_PVN3D_A_Deep_Point-Wise_3D_Keypoints_Voting_Network_for_6DoF_CVPR_2020_paper.pdf), He et al., 2020
- [Learning RGB-D Feature Embeddings for Unseen Object Instance Segmentation](https://proceedings.mlr.press/v155/xiang21a/xiang21a.pdf), Li et al., 2021
- [3D ShapeNets: A Deep Representation for Volumetric Shapes](https://arxiv.org/abs/1406.5670), Wu et al., 2015
- [Multi-view Convolutional Neural Networks for 3D Shape Recognition](https://openaccess.thecvf.com/content_iccv_2015/papers/Su_Multi-View_Convolutional_Neural_ICCV_2015_paper.pdf), Su et al., 2015
- [Volumetric and Multi-View CNNs for Object Classification on 3D Data](https://openaccess.thecvf.com/content_cvpr_2016/papers/Qi_Volumetric_and_Multi-View_CVPR_2016_paper.pdf), Qi et al., 2016
- [Robust 6D Object Pose Estimation with Stochastic Congruent Sets](https://arxiv.org/abs/1805.06324), Mitash et al., 2018
- [What's Behind the Couch? Directed Ray Distance Functions (DRDF) for 3D Scene Reconstruction](https://arxiv.org/abs/2112.04481), Kulkarni et al., 2022

# Point Cloud Processing

- [PointFusion: Deep Sensor Fusion for 3D Bounding Box Estimation](https://openaccess.thecvf.com/content_cvpr_2018/papers/Xu_PointFusion_Deep_Sensor_CVPR_2018_paper.pdf), Xu et al., 2018
- [Just Go with the Flow: Self-Supervised Scene Flow Estimation](https://arxiv.org/abs/1912.00497), Mittal et al., 2019
- [PointFlow: 3D Point Cloud Generation with Continuous Normalizing Flows](https://arxiv.org/abs/1906.12320), Yang et al., 2019
- [3D Object Detection with Pointformer](https://openaccess.thecvf.com/content/CVPR2021/papers/Pan_3D_Object_Detection_With_Pointformer_CVPR_2021_paper.pdf), Pan et al., 2021
- [Particle Video Revisited: Tracking Through Occlusions Using Point Trajectories](https://arxiv.org/abs/2204.04153), Harley et al., 2022

# Object Pose, Geometry, SDF, Implicit surfaces

- [SUM: Sequential scene understanding and manipulation](https://ieeexplore.ieee.org/abstract/document/8206164), Sui et al., 2017
- [Implicit surface representations as layers in neural networks](https://openaccess.thecvf.com/content_ICCV_2019/papers/Michalkiewicz_Implicit_Surface_Representations_As_Layers_in_Neural_Networks_ICCV_2019_paper.pdf), Michalkiewicz et al., 2019
- [Local Deep Implicit Functions for 3D Shape](https://arxiv.org/abs/1912.06126), Genova et al., 2020
- [Implicit geometric regularization for learning shapes](https://arxiv.org/abs/2002.10099), Gropp et al., 2020
- [TAX-Pose: Task-Specific Cross-Pose Estimation for Robot Manipulation](https://arxiv.org/abs/2211.09325), Pan et al., 2022
- [Improving Object Pose Estimation by Fusion With a Multimodal Prior – Utilizing Uncertainty-Based CNN Pipelines for Robotics](https://ieeexplore.ieee.org/document/9670642), Richter-Klug et al., 2022

# Dense Descriptors, Category-level Representations 

- [Single-Stage Keypoint-Based Category-Level Object Pose Estimation from an RGB Image](https://arxiv.org/abs/2109.06161), Lin et al., 2022 
- [Visual Descriptor Learning from Monocular Video](https://arxiv.org/abs/2004.07007), Deekshith et al., 2020

# Recurrent Networks and Object Tracking 

- [DeepIM: Deep Iterative Matching for 6D Pose Estimation](https://openaccess.thecvf.com/content_ECCV_2018/papers/Yi_Li_DeepIM_Deep_Iterative_ECCV_2018_paper.pdf), Li et al., 2018
- [PoseRBPF: A Rao-Blackwellized Particle Filter for 6D Object Pose Tracking](https://arxiv.org/abs/1905.09304), Deng et al., 2019
- [6-PACK: Category-level 6D Pose Tracker with Anchor-Based Keypoints](https://ieeexplore.ieee.org/abstract/document/9196679), Wang et al., 2020
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), Karpathy, 2015
- [RNNPose: Recurrent 6-DoF Object Pose Refinement with Robust Correspondence Field Estimation and Pose Optimization](https://arxiv.org/abs/2203.12870v3), Xu et al., 2022

# Visual Odometry and Localization 

- [Backprop KF: Learning Discriminative Deterministic State Estimators](https://proceedings.neurips.cc/paper/2016/file/697e382cfd25b07a3e62275d3ee132b3-Paper.pdf), Haarnoja et al., 2016
- [Multimodal Sensor Fusion with Differentiable Filters](https://arxiv.org/abs/2010.13021), Lee et al., 2020
- [Particle Filter Recurrent Neural Networks](https://arxiv.org/abs/1905.12885), Ma et al., 2019
- [Differentiable Algorithm Networks for Composable Robot Learning](https://arxiv.org/pdf/1905.11602.pdf), Karkus et al., 2019
- [Chasing Ghosts: Instruction Following as Bayesian State Tracking](https://proceedings.neurips.cc/paper/2019/file/82161242827b703e6acf9c726942a1e4-Paper.pdf), Anderson et al., 2019
- [Differentiable Factor Graph Optimization for Learning Smoothers](https://arxiv.org/abs/2105.08257), Yi et al., 2021
- [How to train your differentiable filter](https://link.springer.com/article/10.1007/s10514-021-09990-9), Kloss et al., 2021
- [Differentiable Nonparametric Belief Propagation](https://arxiv.org/abs/2101.05948), Opipari et al., 2021
- [A Robot Web for Distributed Many-Device Localisation](https://arxiv.org/abs/2202.03314), Murai et al., 2022

# Semantic Scene Graphs and Explicit Representations 

- [Image Retrieval using Scene Graphs](https://openaccess.thecvf.com/content_cvpr_2015/papers/Johnson_Image_Retrieval_Using_2015_CVPR_paper.pdf), Johnson et al., 2015
- [Semantic Robot Programming for Goal-Directed Manipulation in Cluttered Scenes](https://ieeexplore.ieee.org/abstract/document/8460538), Zeng et al., 2018
- [Semantic Linking Maps for Active Visual Object Search](https://arxiv.org/abs/2006.10807), Zeng et al., 2020
- [RoboSherlock: Unstructured information processing for robot perception](https://ieeexplore.ieee.org/abstract/document/7139395), Beetz et al., 2015
- [Image Generation from Scene Graphs](https://openaccess.thecvf.com/content_cvpr_2018/papers/Johnson_Image_Generation_From_CVPR_2018_paper.pdf), Johnson et al., 2018
- [Differentiable Scene Graphs](https://arxiv.org/abs/1902.10200), Raboh et al., 2020

# Neural Radiance Fields and Implicit Representations 

- [iMAP: Implicit Mapping and Positioning in Real-Time](https://arxiv.org/abs/2103.12352), Sucar et al., 2021
- [NARF22: Neural Articulated Radiance Fields for Configuration-Aware Rendering](https://arxiv.org/abs/2210.01166), Lewis et al., 2022
- [NeRF Explosion 2020](https://dellaert.github.io/NeRF/), Dellaert, 2020
- [Scene Representation Networks: Continuous 3D-Structure-Aware Neural Scene Representations](https://arxiv.org/abs/1906.01618), Sitzmann et al., 2019
- [Local Implicit Grid Representations for 3D Scenes](https://arxiv.org/abs/2003.08981), Jiang et al., 2020
- [Convolutional occupancy networks](https://arxiv.org/abs/2003.04618), Peng et al., 2020
- [Object-Centric Neural Scene Rendering](https://arxiv.org/abs/2012.08503), Guo et al., 2020
- [INeRF: Inverting Neural Radiance Fields for Pose Estimation](https://arxiv.org/abs/2012.05877), Yen-Chen et al., 2021
- [ILabel: Interactive Neural Scene Labelling](https://arxiv.org/abs/2111.14637), Zhi et al., 2021
- [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](https://arxiv.org/abs/2112.05124), Simeonov et al., 2021
- [BungeeNeRF: Progressive Neural Radiance Field for Extreme Multi-scale Scene Rendering](https://arxiv.org/abs/2112.05504), Xiangli et al., 2021
- [Block-NeRF: Scalable Large Scene Neural View Synthesis](https://arxiv.org/abs/2202.05263), Tancik et al., 2022
- [NeRF-Supervision: Learning Dense Object Descriptors from Neural Radiance Fields](https://yenchenlin.me/nerf-supervision/), Yen-Chen et al., 2022

# Datasets 

- [Grounding Predicates through Actions](https://arxiv.org/abs/2109.14718), Migimatsu and Bohg, 2022 
- [All You Need is LUV: Unsupervised Collection of Labeled Images using Invisible UV Fluorescent Indicators](https://arxiv.org/abs/2203.04566), Thananjeyan et al., 2022
- [TossingBot: Learning to Throw Arbitrary Objects](https://tossingbot.cs.princeton.edu/), Zeng et al., 2019
- [(NYU Depth v2) Indoor Segmentation and Support Inference from RGBD Images](https://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf), Silberman et al., 2012
- [SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite](https://openaccess.thecvf.com/content_cvpr_2015/papers/Song_SUN_RGB-D_A_2015_CVPR_paper.pdf), Song et al., 2015
- [YCB-Video Dataset](https://arxiv.org/abs/1711.00199), Xiang et al., 2018
- [BOP: Benchmark for 6D Object Pose Estimation](https://bop.felk.cvut.cz/home/), Hodaň et al., 2019
- [ProgressLabeller: Visual Data Stream Annotation for Training Object-Centric 3D Perception](https://arxiv.org/abs/2203.00283), Chen et al., 2022
- [TO-Scene: A Large-scale Dataset for Understanding 3D Tabletop Scenes](https://arxiv.org/abs/2203.09440), Xu et al., 2022
- [Understanding Human Hands in Contact at Internet Scale](https://arxiv.org/abs/2006.06669), Shan et al., 2020
- [Habitat-Matterport 3D Semantics Dataset](https://arxiv.org/abs/2210.05633), Yadav et al., 2022 
- [PartNet-Mobility Dataset](https://sapien.ucsd.edu/browse)
- [Pybullet, a python module for physics simulation for games, robotics and machine learning](https://pybullet.org/wordpress/), Coumans et al., 2015
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim)
- [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/abs/2011.07215), Lin et al., 2020

# Self-Supervised Learning 

- [Making Sense of Vision and Touch: Self-Supervised Learning of Multimodal Representations for Contact-Rich Tasks](https://arxiv.org/abs/1810.10191), Lee et al., 2019
- [VICRegL: Self-Supervised Learning of Local Visual Features](https://arxiv.org/abs/2210.01571), Bardes et al., 2022
- [Fully Self-Supervised Class Awareness in Dense Object Descriptors](https://proceedings.mlr.press/v164/hadjivelichkov22a.html), Hadjivelichkov and Kanoulas, 2022
- [Self-Supervised Geometric Correspondence for Category-Level 6D Object Pose Estimation in the Wild](https://kywind.github.io/self-pose), Zhang et al., 2022

# Grasp Pose Detection 

- [Real-Time Grasp Detection Using Convolutional Neural Networks](https://arxiv.org/abs/1412.3128), Redmon and Angelova, 2015
- [Using Geometry to Detect Grasps in 3D Point Clouds](https://arxiv.org/abs/1501.03100), ten Pas and Platt, 2015
- [Sample Efficient Grasp Learning Using Equivariant Models](https://arxiv.org/abs/2202.09468), Zhu et al., 2022
- [Deep Learning for Detecting Robotic Grasps](https://arxiv.org/abs/1301.3592), Lenz et al., 2013
- [High precision grasp pose detection in dense clutter](https://ieeexplore.ieee.org/abstract/document/7759114), Gualtieri et al., 2016
- [GlassLoc: Plenoptic Grasp Pose Detection in Transparent Clutter](https://ieeexplore.ieee.org/abstract/document/8967685), Zhou et al., 2019
- [MetaGraspNet_v0: A Large-Scale Benchmark Dataset for Vision-driven Robotic Grasping via Physics-based Metaverse Synthesis](https://arxiv.org/abs/2112.14663), Chen et al., 2021
- [Grasp Learning: Models, Methods, and Performance](https://arxiv.org/abs/2211.04895), Platt, 2022

# Tactile Perception for Grasping and Manipulation 

- [Tactile Object Pose Estimation from the First Touch with Geometric Contact Rendering](https://arxiv.org/abs/2012.05205), Bauza et al., 2020
- [Visuotactile Affordances for Cloth Manipulation with Local Control](https://openreview.net/pdf?id=s6NEzqZKaP-), Sunil et al., 2022
- [ShapeMap 3-D: Efficient shape mapping through dense touch and vision](https://arxiv.org/abs/2109.09884), Suresh et al., 2022
- [The Feeling of Success: Does Touch Sensing Help Predict Grasp Outcomes?](https://arxiv.org/pdf/1710.05512.pdf), Calandra et al., 2017
- [Soft-bubble: A highly compliant dense geometry tactile sensor for robot manipulation](https://arxiv.org/abs/1904.02252), Alspach et al., 2019
- [A Review of Tactile Information: Perception and Action Through Touch](https://ieeexplore.ieee.org/document/9136877), Li et al., 2020
- [TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/pdf/2012.08456.pdf), Wang et al., 2020
- [Active Extrinsic Contact Sensing: Application to General Peg-in-Hole Insertion](https://arxiv.org/abs/2110.03555), Kim et al., 2021
- [Active Visuo-Haptic Object Shape Completion](https://ieeexplore.ieee.org/document/9720238), Rustler et al., 2022
- [Learning Self-Supervised Representations from Vision and Touch for Active Sliding Perception of Deformable Surfaces](https://arxiv.org/abs/2209.13042), Kerr and Huang et al., 2022
- [See, Hear, and Feel: Smart Sensory Fusion for Robotic Manipulation](https://arxiv.org/pdf/2212.03858.pdf), Li et al., 2022
- [Learning to Grasp the Ungraspable with Emergent Extrinsic Dexterity](https://arxiv.org/abs/2211.01500), Zhou and Held, 2022

# Pre-training for Robot Manipulation 

- [SORNet: Spatial Object-Centric Representations for Sequential Manipulation](https://arxiv.org/abs/2109.03891), Yuan et al., 2021
- [Real-World Robot Learning with Masked Visual Pre-training](https://arxiv.org/abs/2210.03109), Radosavovic et al., 2022
- [R3M: A Universal Visual Representation for Robot Manipulation](https://arxiv.org/abs/2203.12601), Nair et al., 2022
- [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/), Olah & Carter, 2016
- [Feature-wise transformations](https://distill.pub/2018/feature-wise-transformations/), Dumoulin et al., 2018
- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377), He et al., 2021
- [Interactive Language: Talking to Robots in Real Time](https://arxiv.org/abs/2210.06407), Lynch et al., 2022
- [Transformers are Adaptable Task Planners](https://arxiv.org/abs/2207.02442), Jain et al., 2022

# Perception Beyond Vision (And More Frontiers)

- [Pigeons (Columba livia) as Trainable Observers of Pathology and Radiology Breast Cancer Images](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141357), Levenson et al., 2015
- [Automatic color correction for 3D reconstruction of underwater scenes](https://ieeexplore.ieee.org/abstract/document/7989601), Skinner et al., 2017
- [Classification of Household Materials via Spectroscopy](https://arxiv.org/abs/1805.04051), Erickson et al., 2018
- [Through-Wall Human Pose Estimation Using Radio Signals](https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhao_Through-Wall_Human_Pose_CVPR_2018_paper.pdf), Zhao et al., 2018
- [A bio-hybrid odor-guided autonomous palm-sized air vehicle](https://iopscience.iop.org/article/10.1088/1748-3190/abbd81), Anderson et al., 2020
- [Event-based, Direct Camera Tracking from a Photometric 3D Map using Nonlinear Optimization](https://rpg.ifi.uzh.ch/docs/ICRA19_Bryner.pdf), Bryner et al., 2019
- [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://arxiv.org/abs/1912.11474), Chen et al., 2019
- [Neural Implicit Surface Reconstruction using Imaging Sonar](https://arxiv.org/abs/2209.08221), Qadri et al., 2022
- [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034), Simonyan et al., 2013
- [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/), Olah et al., 2018
- [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/), Goh et al., 2021
- [Saving Face: Investigating the Ethical Concerns of Facial Recognition Auditing](https://dl.acm.org/doi/abs/10.1145/3375627.3375820), Raji et al., 2020
- [Autonomous Tool Construction Using Part Shape and Attachment Prediction](http://www.roboticsproceedings.org/rss15/p09.pdf), Nair et al., 2019
- [Parts-Based Articulated Object Localization in Clutter Using Belief Propagation](https://arxiv.org/abs/2008.02881), Pavlasek et al., 2020
- [DensePose: Dense Human Pose Estimation In The Wild](https://arxiv.org/abs/1802.00434), Xiao et al., 2018
- [FabricFlowNet: Bimanual Cloth Manipulation with a Flow-based Policy](https://arxiv.org/abs/2111.05623), Weng et al., 2021
- [LIT: Light-field Inference of Transparency for Refractive Object Localization](https://arxiv.org/abs/1910.00721), Zhou et al., 2019
- [Multi-modal Transfer Learning for Grasping Transparent and Specular Objects](https://arxiv.org/abs/2006.00028), Weng et al., 2020
- [D-NeRF: Neural Radiance Fields for Dynamic Scenes](https://arxiv.org/abs/2011.13961), Pumarola et al., 2020
- [3D Neural Scene Representations for Visuomotor Control](https://arxiv.org/abs/2107.04004), Li et al., 2021
- [HexPlane: A Fast Representation for Dynamic Scenes](https://arxiv.org/abs/2301.09632), Cao and Johnson, 2023
- [Learning Decentralized Controllers for Robot Swarms with Graph Neural Networks](https://arxiv.org/abs/1903.10527), Tolstaya et al., 2019
- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/), Sanchez-Lengeling et al., 2021
- [Understanding RL Vision](https://distill.pub/2020/understanding-rl-vision/), Hilton et al., 2020
- [WaterGAN: Unsupervised Generative Network to Enable Real-time Color Correction of Monocular Underwater Images](https://arxiv.org/abs/1702.07392), Li et al., 2017
- [Differentiable Particle Filters through Conditional Normalizing Flow](https://arxiv.org/abs/2107.00488), Chen et al., 2021