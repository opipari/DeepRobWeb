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
 - Implement the forward and backward pass for a two layer neural network.
 - Generalize your network implementation to fully connected layers.
 - Implement the forward and backward pass for a non-linear activation function (ReLU).
 - Implement and understand the tradeoffs using network regularization techniques.
 - Understand the characteristics of neural network based classification using the [PROPS Classification Dataset](/dataset/#props-classification).


## Instructions

1. <b>Download the project starter code</b>
    - Project 2 starter code sent via email.

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
	- Once you have implemented a portion of the required features, you may submit your work for feedback from the Autograder. To receive feedback, download your `*.ipynb` and `*.py` files then upload them to the [Project 2 Autograder](https://autograder.io/web/project/1976){: target="_blank" rel="noopener noreferrer"}. You may submit to the Autograder for feedback up to 5 times per day.

5. <b>Download final implementation</b>
    - After implementing all features, <b>save your work</b> and download the completed `*.ipynb` and `*.py` files. 
    - The last cell of the `fully_connected_networks.ipynb` notebook will generate a `uniqueid_umid_P2.zip` file. The zip file should include `two_layer_net.ipynb`, `two_layer_net.py`, `fully_connected_networks.ipynb`, `fully_connected_networks.py`, `nn_best_model.pt`, `best_overfit_five_layer_net.pth`, and `best_two_layer_net.pth` for this assignment.

6. <b>Submit your python and notebook files for grading</b>
    - Upload your files to the [Autograder](https://autograder.io/web/project/1976){: target="_blank" rel="noopener noreferrer"} for grading consideration. Your highest score will be used for final grades.

## Deadline

This project is due on <b>Saturday, February 11th at 11:59pm EST</b>. We suggest starting as soon as possible.

## Grading

This project will be graded by the [Autograder](https://autograder.io/web/project/1976){: target="_blank" rel="noopener noreferrer"}. The project is worth a total of 110 points. You may submit to the Autograder for feedback up to 5 times per day.

