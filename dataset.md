---
layout: page
title: PROPS Dataset
description: Overview of the robot perception datasets used throughout the DeepRob course.
nav_order: 5
---

# PROPS Dataset

At the core of Deep Learning is a set of computational techniques to identify and exploit patterns in datasets. Robots will only benefit from these techniques if as roboticists we provide sufficiently large datasets that are representative of the environments and tasks we anticipate our robots acting in. The <b>P</b>rogress <b>R</b>obot <b>O</b>bject <b>P</b>erception <b>S</b>amples (<b>PROPS</b>) dataset has been created to support the development of deep learning models in a variety of robot perception contexts. 

The PROPS dataset is a downsampled version of data collected from the [ProgressLabeller annotation tool (Chen et al., 2022)](https://arxiv.org/abs/2203.00283){: target="_blank" rel="noopener noreferrer"}. This dataset focuses on table-top scenes that are inspired by the environments a domestic service robot would be expected to encounter. Objects in these scenes are from the [YCB Object and Model Set (Calli et al., 2015)](https://ieeexplore.ieee.org/abstract/document/7251504){: target="_blank" rel="noopener noreferrer"}.


[Course projects](/projects/) in DeepRob are built using the PROPS dataset.


## PROPS Classification

This portion of the dataset is catered for image classification tasks. The format of this portion is based on that of the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html){: target="_blank" rel="noopener noreferrer"}. The PROPS Classification dataset contains <b>10 object categories</b> with <b>50K</b> training images and <b>10K</b> testing images. Each image in the dataset is a <b>32x32 RGB</b> color image. All images in the test set are taken from scenes not represented in the training set.

### Download

The dataset is available for download on [Google Drive ![](/assets/logos/logo_drive_2020q4_color_2x_web_64dp.png){: .text-logo }](https://drive.google.com/file/d/1C8_JFsnPVm392C-S1rH0y4HFfNkdMlXi/view?usp=share_link){: target="_blank" rel="noopener noreferrer"}.

We provide the [`PROPSClassificationDataset`](/assets/projects/PROPSClassificationDataset.py), a PyTorch dataset class, to support development with and use of the PROPS Classification dataset.

### Examples

Sample images of each category in the PROPS Classification dataset are included below:

![](/assets/images/props_classification.jpg){: .data-img }


## PROPS Detection

Coming soon!


## PROPS Pose Estimation

Coming soon!

