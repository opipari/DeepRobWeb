---
layout: page
title: Datasets
description: Overview of the robot perception datasets used throughout the DeepRob course.
nav_order: 5
has_children: true
has_toc: false
---

# PROPS Datasets

At the core of Deep Learning is a set of computational techniques to identify and exploit patterns in datasets. Robots will only benefit from these techniques if as roboticists we provide sufficiently large datasets that are representative of the environments and tasks we anticipate our robots acting in. The <b>P</b>rogress <b>R</b>obot <b>O</b>bject <b>P</b>erception <b>S</b>amples (<b>PROPS</b>) datasets have been created to support the development of deep learning models in a variety of robot perception contexts. 

The PROPS datasets consist of downsampled versions of data collected from the [ProgressLabeller annotation tool (Chen et al., 2022)](https://arxiv.org/abs/2203.00283){: target="_blank" rel="noopener noreferrer"}. This dataset focuses on table-top scenes that are inspired by the environments a domestic service robot would be expected to encounter. Objects in these scenes are from the [YCB Object and Model Set (Calli et al., 2015)](https://ieeexplore.ieee.org/abstract/document/7251504){: target="_blank" rel="noopener noreferrer"}.


[Course projects](/projects/) in DeepRob are built using the PROPS datasets.


## [PROPS Classification](/datasets/props-classification/)

This portion of the dataset is catered for image classification tasks. The format of this portion is based on that of the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html){: target="_blank" rel="noopener noreferrer"}. The PROPS Classification dataset contains <b>10 object categories</b> with <b>50K</b> training images and <b>10K</b> testing images. Each image in the dataset is a <b>32x32 RGB</b> color image. All images in the test set are taken from scenes not represented in the training set.

## [PROPS Detection](/datasets/props-detection/)

This portion of the dataset is catered for object detection tasks. The PROPS Detection dataset contains <b>10 object categories</b> with <b>2.5K</b> training images and <b>2.5K</b> validation images. Each image in the dataset is a <b>640x480 RGB</b> color image. All images in the validation set are taken from scenes not represented in the training set.


## [PROPS Pose Estimation](/datasets/props-pose/)

This portion of the dataset is catered for 6 degrees-of-freedom rigid body object pose estimation. The PROPS Pose dataset contains <b>10 object categories</b> with <b>500</b> training images and <b>500</b> validation images. Each image in the dataset is a <b>640x480 RGB</b> color image. Aligned depth images and segmentation masks are also included in the dataset.

