---
layout: page
title: Important Works
description: Core and recent deep learning research papers for perception and robotics.
parent: Papers
nav_order: 5
has_children: false
has_toc: true
---

# Deep Learning Research Papers for Robot Perception: Important Works
{:.no_toc}

This collection highlights foundational papers and promising recent research in deep learning and robot perception. 

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

# RGB-D Architectures 

- ⭐ [VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition](https://graphics.stanford.edu/courses/cs233-21-spring/ReferencedPapers/voxnet_07353481.pdf), Maturana et al., 2015
- ⭐ [PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes](https://arxiv.org/abs/1711.00199), Xiang et al., 2018

# Point Cloud Processing

- ⭐ [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](https://arxiv.org/abs/1612.00593), Qi et al., 2017
- ⭐ [PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space](https://arxiv.org/abs/1706.02413), Qi et al., 2017
- ⭐ [DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion](https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_DenseFusion_6D_Object_Pose_Estimation_by_Iterative_Dense_Fusion_CVPR_2019_paper.pdf), Wang et al., 2019
- ⭐ [Point Transformer](https://arxiv.org/abs/2012.09164)
- [Pointnext: Revisiting pointnet++ with improved training and scaling strategies](https://arxiv.org/abs/2206.04670)
- [KPConvX: Modernizing Kernel Point Convolution with Kernel Attention](https://arxiv.org/abs/2405.13194)

# Object Pose, Geometry, SDF, Implicit surfaces

- ⭐ [DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation](https://openaccess.thecvf.com/content_CVPR_2019/papers/Park_DeepSDF_Learning_Continuous_Signed_Distance_Functions_for_Shape_Representation_CVPR_2019_paper.pdf), Park et al., 2019
- [iSDF: Real-Time Neural Signed Distance Fields for Robot Perception](https://arxiv.org/abs/2204.02296), Oriz et al., 2022
- [ReFlow6D: Refraction-Guided Transparent Object 6D Pose Estimation via Intermediate Representation Learning](https://arxiv.org/abs/2412.20830)

# Dense Descriptors, Category-level Representations 

- ⭐ [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](https://arxiv.org/abs/1806.08756), Florence et al., 2018
- ⭐ [Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation](https://geometry.stanford.edu/projects/NOCS_CVPR2019/), Wang et al., 2019
- [kPAM: KeyPoint Affordances for Category-Level Robotic Manipulation](https://arxiv.org/abs/1903.06684), Manuelli et al., 2019
- [SurfEmb: Dense and Continuous Correspondence Distributions for Object Pose Estimation with Learnt Surface Embeddings](https://arxiv.org/abs/2111.13489), Haugaard et al., 2021

# Recurrent Networks and Object Tracking 

- ⭐ [Long Short-Term Memory](https://ieeexplore.ieee.org/abstract/document/6795963), Hochreiter et al., 1997
- [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://arxiv.org/abs/2207.07115), Cheng and Schwing, 2022
- [TrackFormer: Multi-Object Tracking with Transformers](https://openaccess.thecvf.com/content/CVPR2022/papers/Meinhardt_TrackFormer_Multi-Object_Tracking_With_Transformers_CVPR_2022_paper.pdf), Meinhardt et al., 2022
- [6D Object Pose Tracking in Internet Videos for Robotic Manipulation](https://arxiv.org/abs/2503.10307)

# Visual Odometry and Localization 

- ⭐ [Factor Graphs and GTSAM](https://gtsam.org/tutorials/intro.html), Dellaert et al., 2012
- ⭐ [SuperPoint: Self-Supervised Interest Point Detection and Description](https://arxiv.org/abs/1712.07629), DeTone et al., 2017
- ⭐ [SuperGlue: Learning Feature Matching with Graph Neural Networks](https://arxiv.org/abs/1911.11763), Sarlin et al., 2019
- [Differentiable Particle Filters: End-to-End Learning with Algorithmic Priors](http://www.roboticsproceedings.org/rss14/p01.pdf), Jonschkowski et al., 2018
- [Differentiable SLAM-net: Learning Particle SLAM for Visual Navigation](https://openaccess.thecvf.com/content/CVPR2021/papers/Karkus_Differentiable_SLAM-Net_Learning_Particle_SLAM_for_Visual_Navigation_CVPR_2021_paper.pdf), Karkus et al., 2021
- [VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold](https://arxiv.org/pdf/2505.12549)

# Semantic Scene Graphs and Explicit Representations 

- ⭐ [Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations](https://arxiv.org/abs/1602.07332), Krishna et al., 2016
- ⭐ [Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization](https://arxiv.org/abs/2201.13360), Hughes et al., 2022
- [3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera](https://openaccess.thecvf.com/content_ICCV_2019/html/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.html), Armeni et al., 2020
- [ConceptFusion: Open-set Multimodal 3D Mapping](https://arxiv.org/abs/2302.07241), Jatavallabhula et al., 2023

# Neural Radiance Fields and Implicit Representations 

- ⭐ [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934), Mildenhall et al., 2020
- ⭐ [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/pdf/2308.04079)
- [NeRF-SLAM: Real-Time Dense Monocular SLAM with Neural Radiance Fields](https://arxiv.org/abs/2210.13641), Rosinol et al., 2022
- [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](https://f3rm.csail.mit.edu), Shen et al., 2023
- [Language Embedded Radiance Fields](https://www.lerf.io), Kerr et al., 2023
- [PIN-SLAM: LiDAR SLAM Using a Point-Based Implicit Neural Representation for Achieving Global Map Consistency](https://arxiv.org/pdf/2401.09101)
- [MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction](https://arxiv.org/pdf/2504.19104)

# NeRF SLAM

- [DDN-SLAM: Real Time Dense Dynamic Neural Implicit SLAM](https://arxiv.org/abs/2401.01545)
- [GlORIE-SLAM: Globally Optimized RGB-only Implicit Encoding Point Cloud SLAM](https://arxiv.org/pdf/2403.19549)
- [EC-SLAM: Effectively Constrained Neural RGB-D SLAM with Sparse TSDF Encoding and Global Bundle Adjustment](https://arxiv.org/pdf/2404.13346)
- [HERO-SLAM: Hybrid Enhanced Robust Optimization of Neural SLAM](https://arxiv.org/pdf/2407.18813)

# Datasets 

- ⭐ [Deep Learning for Robots: Learning from Large-Scale Interaction](https://ai.googleblog.com/2016/03/deep-learning-for-robots-learning-from.html), Levine et al., 2016
- ⭐ [Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](https://arxiv.org/abs/2108.10470), Makoviychuk et al., 2021
- ⭐ [ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](http://www.scan-net.org), Dai et al., 2019
- ⭐ [ShapeNet: An Information-Rich 3D Model Repository](https://shapenet.org), Chang et al., 2015
- ⭐ [MuJoCo: A physics engine for model-based control](https://ieeexplore.ieee.org/abstract/document/6386109), Todorov et al., 2015
- ⭐ [CARLA: An Open Urban Driving Simulator](https://carla.org), Dosovitskiy et al., 2017
- [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659), Gu et al., 2023

# Self-Supervised & Representation Learning 

- ⭐ [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294), Caron et al., 2021
- ⭐ [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193), Oquab et al., 2023
- [Questioning Representational Optimism in Deep Learning: The Fractured Entangled Representation Hypothesis](https://arxiv.org/pdf/2505.11581)
- [Personalized Representation from Personalized Generation](http://arxiv.org/pdf/2412.16156)

# Grasp Pose Detection 

- ⭐ [Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics](https://arxiv.org/abs/1703.09312), Mahler et al., 2017
- ⭐ [FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344)
- [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](https://ieeexplore.ieee.org/abstract/document/9561877), Sundermeyer et al., 2021
- [Any6D: Model-free 6D Pose Estimation of Novel Objects](https://arxiv.org/pdf/2503.18673)
- [Superquadrics-based Grasp Pose Estimation on Larger Objects for Mobile-Manipulation](https://arxiv.org/pdf/2411.04386v1)
- [RTAGrasp: Learning Task-Oriented Grasping from Human Videos via Retrieval, Transfer, and Alignment](https://arxiv.org/pdf/2409.16033v1)

# Tactile Perception for Grasping and Manipulation 

- ⭐ [GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force](https://dspace.mit.edu/handle/1721.1/114627), Yuan et al., 2017
- [More Than a Feeling: Learning to Grasp and Regrasp using Vision and Touch](https://arxiv.org/abs/1805.11085), Calandra et al., 2018 

# Pre-training for Robot Manipulation 

- ⭐ [Attention is All You Need](https://arxiv.org/abs/1706.03762), Vaswani et al., 2017
- ⭐ [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929), Dosovitskiy et al., 2020
- ⭐ [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020), Radford et al., 2021
- [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/abs/2010.14406), Zeng et al., 2020
- [CLIPort: What and Where Pathways for Robotic Manipulation](https://arxiv.org/abs/2109.12098), Shridhar et al., 2021
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://say-can.github.io/assets/palm_saycan.pdf), Ahn et al., 2022
- [RT-1: Robotics Transformer for Real-World Control at Scale](https://robotics-transformer.github.io/assets/rt1.pdf), Brohan et al., 2022
- ⭐ [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)](https://arxiv.org/abs/2402.03300), Shao et al., 2024
- ⭐ [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)
- [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/pdf/2504.16054)

# Generative Modeling & Dynamic Scenes

- ⭐ [Deep Reinforcement Learning from Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf), Christiano et al., 2017
- [Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991), Janner et al., 2022
- [Anything-3D: Towards Single-view Anything Reconstruction in the Wild](https://arxiv.org/abs/2304.10261), Shen et al., 2023
- [DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation](https://arxiv.org/abs/2501.16764)
- [One Diffusion to Generate Them All](https://arxiv.org/abs/2411.16318)
- [DreamDojo A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949)
- [SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2411.06390)
- [Self-Contrastive Fine-Tuning for Equitable Image Generation](https://arxiv.org/abs/2401.08053)

# Transparent Objects

- [Dex-NeRF: Using a Neural Radiance Field to Grasp Transparent Objects](https://arxiv.org/abs/2110.14217), Ichnowski et al., 2021
- [ClearPose: Large-scale Transparent Object Dataset and Benchmark](https://arxiv.org/abs/2203.03890), Chen et al., 2022
- [Transplat: Surface embedding-guided 3d gaussian splatting for transparent object manipulation](https://arxiv.org/abs/2502.07840)

# Explainable and Interpretable AI

- ⭐ [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://arxiv.org/abs/1610.02391), Selvaraju et al., 2016
- ⭐ [Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](https://proceedings.mlr.press/v81/buolamwini18a.html?mod=article_inline), Buolamwini and Gebru, 2018
- [Questioning Representational Optimism in Deep Learning: The Fractured Entangled Representation Hypothesis](https://arxiv.org/pdf/2505.11581)