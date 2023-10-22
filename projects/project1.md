---
layout: page
title: Project 1
parent: Projects
nav_order: 2
description: Specification of project 1 for DeepRob at the University of Michigan.
---
 
# Project 1

## Overview
The objective of this project is to gain experience building a machine learning pipeline that can be used to train and evaluate image classification models. In this project you will implement a set of classification models then apply them to a dataset of images in the context of domestic service robots.

### The goals for this project are as follows:
 - Implement a K-Nearest Neighbors classifier.
 - Implement a Multiclass Support Vector Machine classifier.
 - Implement a Softmax classifier.
 - Understand the differences and tradeoffs between each of these classifiers.
 - Understand the characteristics of instance-level classification using the [PROPS Classification Dataset]({{ site.baseurl }}/datasets/props-classification/).
 - Practice with cross validating your machine learning models.


## Instructions

1. <b>Download the project starter code</b>
    - [Project 1 starter code: P1.zip]({{ site.baseurl }}/assets/projects/P1.zip)

2. <b>Unzip the starter code and upload to Google Drive</b>
    - Once unzipped, you should find a root directory titled 'P1'. The 'P1' directory contains all starter code and files needed to complete this project. Please upload the 'P1' directory to your [Google Drive](https://drive.google.com/){: target="_blank" rel="noopener noreferrer"}.

3. <b>Open the `*.ipynb` and `*.py` files and implement features</b>
    - We recommend implementing the features in a Google Colab environment. The Colab development environment can be accessed by double-clicking on each `*.ipynb` and `*.py` file within your Drive. Instructions for each feature are included in the `knn.ipynb` and `linear_classifier.ipynb` files.

    - We suggest starting by implementing the required features as they appear in the `knn.ipynb` notebook, which can be thought of as part 1 of the project. Then work through the `linear_classifier.ipynb` notebook as part 2 of the project.

    - While working on the project, keep the following in mind:

        - The notebook and the python file have clearly marked blocks where you are expected to write code. <b>Do not write or modify any code outside of these blocks.</b>
        - <b>Do not add or delete cells from the notebook.</b> You may add new cells to perform scratch computations, but you should delete them before submitting your work.
        - <b>Run all cells, and do not clear out the outputs, before submitting.</b> You will only get credit for code that has been run.
        - To avoid experiencing Colab usage limits, save and close your notebooks once finished working.

4. <b>Submit your implementation for Autograder feedback</b>
    - Once you have implemented a portion of the required features, you may submit your work for feedback from the Autograder. To receive feedback, download your `*.ipynb` and `*.py` files then upload them to the [Project 1 Autograder](https://autograder.io/web/project/1953){: target="_blank" rel="noopener noreferrer"}. You may submit to the Autograder for feedback up to 2 times per day.

5. <b>Download final implementation</b>
    - After implementing all features, <b>save your work</b> and download the completed `*.ipynb` and `*.py` files. 
    - The last cell of the `linear_classifier.ipynb` notebook will generate a `uniqueid_umid_P1.zip` file. The zip file should include `knn.ipynb`, `knn.py`, `linear_classifier.ipynb`, `linear_classifier.py`, `svm_best_model.pt`, and `softmax_best_model.pt` for this assignment.

6. <b>Submit your python and notebook files for grading</b>
    - Upload your files to the [Autograder](https://autograder.io/web/project/1953){: target="_blank" rel="noopener noreferrer"} for grading consideration. Your highest score will be used for final grades.

## Deadline

This project is due on <b>Thursday, January 26th at 11:59pm EST</b>. We suggest starting as soon as possible.

## Grading

This project will be graded by the [Autograder](https://autograder.io/web/project/1953){: target="_blank" rel="noopener noreferrer"}. The project is worth a total of 95 points. You may submit to the Autograder for feedback up to 2 times per day.

