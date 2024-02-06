---
layout: page
title: Project 2
parent: Projects
nav_order: 3
description: Specification of project 2 for DeepRob at the University of Michigan.
---
 
# Project 2

## Overview
The objective of this project is to gain experience building and training neural networks as multi layer perceptrons. In this project you will implement a fixed size two layer neural network and a set of generic network layers that can be used to build and train multi layer perceptrons.

### The goals for this project are as follows:
 - Generalize your network implementation to fully connected layers.
 - Implement the forward and backward pass for convolutional neural networks.
 - Implement the [Faster R-CNN](https://arxiv.org/abs/1506.01497){: target="_blank" rel="noopener noreferrer"} architecture for object detection.
 - Implement and understand the tradeoffs using network regularization techniques.
 - Understand the characteristics of neural network based object detection using the [PROPS Detection Dataset]({{ site.baseurl }}/datasets/props-detection/).

## Instructions

1. <b>Download the project starter code</b>
    - [Project 2 starter code: P2.zip]({{ site.baseurl }}/assets/projects/P2.zip)

2. <b>Unzip the starter code and upload to Google Drive</b>
    - Once unzipped, you should find a root directory titled 'P2'. The 'P2' directory contains all starter code and files needed to complete this project. Please upload the 'P2' directory to your [Google Drive](https://drive.google.com/){: target="_blank" rel="noopener noreferrer"}.

3. <b>Open the `*.ipynb` and `*.py` files and implement features</b>
    - We recommend implementing the features in a Google Colab environment. The Colab development environment can be accessed by double-clicking on each `*.ipynb` and `*.py` file within your Drive. Instructions for each feature are included in the `two_layer_net.ipynb` and `fully_connected_networks.ipynb` files.

    - We suggest starting by implementing the required features as they appear in the `two_layer_net.ipynb` notebook, which can be thought of as part 1 of the project. Then work through the `fully_connected_networks.ipynb` notebook as part 2 of the project.

    - While working on the project, keep the following in mind:

        - The notebook and the python file have clearly marked blocks where you are expected to write code. <b>Do not write or modify any code outside of these blocks.</b>
        - <b>Do not add or delete cells from the notebook.</b> You may add new cells to perform scratch computations, but you should delete them before submitting your work.
        - <b>Run all cells, and do not clear out the outputs, before submitting.</b> You will only get credit for code that has been run.
        - To avoid experiencing Colab usage limits, save and close your notebooks once finished working.

4. <b>Submit your implementation for Autograder feedback</b>
	- Once you have implemented a portion of the required features, you may submit your work for feedback from the Autograder. To receive feedback, download your `*.ipynb` and `*.py` files then upload them to the [Project 2 Autograder](https://autograder.io/web/project/2430){: target="_blank" rel="noopener noreferrer"}. You may submit to the Autograder for feedback up to 5 times per day.

5. <b>Download final implementation</b>
    - After implementing all features, <b>save your work</b> and download the completed `*.ipynb` and `*.py` files. 
    - The last cell of the `two_stage_detector.ipynb` notebook will generate a `uniqueid_umid_P2.zip` file. The zip file should include `fully_connected_networks.ipynb`, `fully_connected_networks.py`, `convolutional_networks.ipynb`, `convolutional_networks.py`, `two_stage_detector.ipynb`, `two_stage_detector.py`, `one_minute_deepconvnet.pth`, `overfit_deepconvnet.pth`, `best_overfit_five_layer_net.pth`, `best_two_layer_net.pth`, and `rcnn_detector.pt` for this assignment.

6. <b>Submit your python and notebook files for grading</b>
    - Upload your files to the [Autograder](https://autograder.io/web/project/2430){: target="_blank" rel="noopener noreferrer"} for grading consideration. Your highest score will be used for final grades.

## Deadline

This project is due on <b>Thursday, February 22nd at 11:59pm EST</b>. We suggest starting as soon as possible.

## Grading

This project will be graded by the [Autograder](https://autograder.io/web/project/2430){: target="_blank" rel="noopener noreferrer"}. The project is worth a total of 165 points. You may submit to the Autograder for feedback up to 3 times per day.

