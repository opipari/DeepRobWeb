---
layout: page
title: Pose Estimation
description: Overview of the robot perception datasets used for object detection projects the DeepRob course.
parent: Datasets
nav_order: 3
---

# PROPS Pose Estimation Dataset

This portion of the dataset is catered for 6 degrees-of-freedom rigid body object pose estimation. The PROPS Pose dataset contains <b>10 object categories</b> with <b>500</b> training images and <b>500</b> validation images. Each image in the dataset is a <b>640x480 RGB</b> color image. Aligned depth images and segmentation masks are also included in the dataset.

## Download

The dataset is available for download on [Google Drive ![](/assets/logos/logo_drive_2020q4_color_2x_web_64dp.png){: .text-logo }](https://drive.google.com/file/d/15rhwXhzHGKtBcxJAYMWJG7gN7BLLhyAq/view?usp=share_link){: target="_blank" rel="noopener noreferrer"}.

We provide the [`PROPSPoseDataset`](/assets/projects/PROPSPoseDataset.py), a PyTorch dataset class, to support development with and use of the PROPS Pose dataset.

## Examples

Sample images and labels for each category in the PROPS Pose dataset are included below:

![Sample animation showing PROPS pose samples](/assets/images/props_pose.gif){: .data-img }
