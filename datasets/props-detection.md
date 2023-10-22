---
layout: page
title: Detection
description: Overview of the robot perception datasets used for object detection projects the DeepRob course.
parent: Datasets
nav_order: 2
---

# PROPS Detection Dataset

This portion of the dataset is catered for object detection tasks. The PROPS Detection dataset contains <b>10 object categories</b> with <b>2.5K</b> training images and <b>2.5K</b> validation images. Each image in the dataset is a <b>640x480 RGB</b> color image. All images in the validation set are taken from scenes not represented in the training set.

## Download

The dataset is available for download on [Google Drive ![]({{ site.baseurl }}/assets/logos/logo_drive_2020q4_color_2x_web_64dp.png){: .text-logo }](https://drive.google.com/file/d/1vG7_O-1JcYAgixdnV_n0QuFCt2R0050j/view?usp=share_link){: target="_blank" rel="noopener noreferrer"}.

We provide the [`PROPSDetectionDataset`]({{ site.baseurl }}/assets/projects/PROPSDetectionDataset.py), a PyTorch dataset class, to support development with and use of the PROPS Detection dataset.

## Examples

Sample images of each category in the PROPS Detection dataset are included below:

![Sample animation showing PROPS detection samples]({{ site.baseurl }}/assets/images/props_detection.gif){: .data-img }
