---
layout: page
title: Classification
description: Overview of the robot perception datasets used for image classification projects the DeepRob course.
parent: Datasets
nav_order: 1
---

# PROPS Classification Dataset

This portion of the dataset is catered for image classification tasks. The format of this portion is based on that of the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html){: target="_blank" rel="noopener noreferrer"}. The PROPS Classification dataset contains <b>10 object categories</b> with <b>50K</b> training images and <b>10K</b> testing images. Each image in the dataset is a <b>32x32 RGB</b> color image. All images in the test set are taken from scenes not represented in the training set.

## Download

The dataset is available for download on [Google Drive ![]({{ site.baseurl }}/assets/logos/logo_drive_2020q4_color_2x_web_64dp.png){: .text-logo }](https://drive.google.com/file/d/1C8_JFsnPVm392C-S1rH0y4HFfNkdMlXi/view?usp=share_link){: target="_blank" rel="noopener noreferrer"}.

We provide the [`PROPSClassificationDataset`]({{ site.baseurl }}/assets/projects/PROPSClassificationDataset.py), a PyTorch dataset class, to support development with and use of the PROPS Classification dataset.

## Examples

Sample images of each category in the PROPS Classification dataset are included below:

![Sample images from PROPS classification dataset]({{ site.baseurl }}/assets/images/props_classification.webp){: .data-img }
